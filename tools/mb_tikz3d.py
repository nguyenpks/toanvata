# -*- coding: utf-8 -*-
"""Hình không gian TĨNH vẽ bằng TikZ (pdflatex) rồi chuyển sang SVG (pdftocairo -svg).

Dùng chung cấu hình với GEO3D cũ:
  cfg = {'points': {'A': (x, y, z), ...},
         'solid': True | ['S', 'A', ...],          # các đỉnh của khối (bao lồi) -> tự tính nét khuất
         'segments': [['A', 'B', {'color': '#c2410c', 'width': 4, 'dash': True, 'arrow': True}], ...],
         'polygons': [['A', 'B', 'C'] | {'points': [...], 'fill': '#86e0bd', 'opacity': .4, 'outline': True}],
         'proj': 'geo' (mặc định: hình biểu diễn SGK, trục sâu chéo 45°, hệ số 1/2) | 'oxyz' (Ox hướng xuống trái),
         'axes': False | True (vẽ Ox, Oy, Oz),  'nolabel': ['G', ...],  'labelpos': {'O': 'below'},
         'angles': [['S', 'B', 'A']] (đánh dấu góc), 'right': [['S', 'A', 'B']] (kí hiệu góc vuông tại đỉnh giữa)}
Nét khuất được tính đúng bằng hình học: một điểm bị che nếu tia từ điểm đó về phía người nhìn cắt khối.
Kết quả lưu ở img/fig3d/<md5>.svg (có bộ nhớ đệm: tex không đổi thì không biên dịch lại)."""
import os, re, math, hashlib, subprocess, tempfile, shutil, itertools

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
OUT = os.path.join(ROOT, 'img', 'fig3d')
def _proj(kind, K, W):
    """Ma trận chiếu song song (ảnh của e_x, e_y, e_z trên giấy) và hướng nhìn d (P·d = 0, từ người xem vào hình)."""
    ka, kb = K * math.cos(math.radians(W)), K * math.sin(math.radians(W))
    if kind == 'oxyz': return ((-ka, -kb), (1, 0), (0, 1)), (-1, -ka, -kb)
    return ((1, 0), (ka, kb), (0, 1)), (-ka, 1, -kb)

def _sub(a, b): return tuple(x - y for x, y in zip(a, b))
def _dot(a, b): return sum(x * y for x, y in zip(a, b))
def _cross(a, b): return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
def _norm(a): return math.sqrt(_dot(a, a))

def hull_faces(P):
    """Các mặt của bao lồi: list (n_ra_ngoài, c, [tên đỉnh theo vòng]). Dùng cho số đỉnh nhỏ (≤ 12)."""
    names = list(P); pts = [P[k] for k in names]
    cen = tuple(sum(p[i] for p in pts) / len(pts) for i in range(3))
    faces, seen = [], set()
    for i, j, k in itertools.combinations(range(len(pts)), 3):
        n = _cross(_sub(pts[j], pts[i]), _sub(pts[k], pts[i]))
        L = _norm(n)
        if L < 1e-9: continue
        n = tuple(x / L for x in n); c = _dot(n, pts[i])
        side = [_dot(n, p) - c for p in pts]
        if max(side) > 1e-7 and min(side) < -1e-7: continue
        if max(side) > 1e-7: n = tuple(-x for x in n); c = -c; side = [-s for s in side]
        on = tuple(sorted(t for t in range(len(pts)) if abs(side[t]) <= 1e-7))
        if on in seen: continue
        seen.add(on)
        fc = tuple(sum(pts[t][q] for t in on) / len(on) for q in range(3))
        e1 = _sub(pts[on[0]], fc); e1 = tuple(x / (_norm(e1) or 1) for x in e1); e2 = _cross(n, e1)
        ring = sorted(on, key=lambda t: math.atan2(_dot(_sub(pts[t], fc), e2), _dot(_sub(pts[t], fc), e1)))
        faces.append((n, c, [names[t] for t in ring]))
    return faces

def hidden(p, faces, d, eps=1e-6):
    """Điểm p bị khối che nếu tia p - t·d (t > 0, đi về phía người nhìn) đi qua phần trong của khối."""
    if not faces: return False
    t0, t1 = -1e18, 1e18
    for n, c, _ in faces:
        a = -_dot(n, d); b = c - _dot(n, p)     # n·(p - t d) <= c  <=>  a t <= b
        if abs(a) < 1e-12:
            if b < -eps: return False
            continue
        if a > 0: t1 = min(t1, b / a)
        else: t0 = max(t0, b / a)
    lo, hi = max(t0, 0.0), t1
    return hi - lo > 1e-4 and hi > 1e-4

def _col(h, defs):
    h = h.lstrip('#').upper()
    if h not in defs: defs[h] = 'c%d' % len(defs)
    return defs[h]

def _lab(name): return name.replace('′', "'").replace('″', "''")

def _anchor(dx, dy):
    a = math.degrees(math.atan2(dy, dx)) % 360
    names = ['west', 'south west', 'south', 'south east', 'east', 'north east', 'north', 'north west']   # anchor đối diện hướng đặt nhãn
    return names[int(((a + 22.5) % 360) // 45)]

POS = {'above': 'south', 'below': 'north', 'left': 'east', 'right': 'west', 'above left': 'south east', 'above right': 'south west', 'below left': 'north east', 'below right': 'north west'}

def tikz(cfg):
    P = {k: tuple(float(x) for x in v) for k, v in cfg['points'].items()}
    solid0 = cfg.get('solid'); n0 = len(P) if solid0 is True else len(solid0 or [])
    # hộp/lập phương (8 đỉnh): trục sâu 30°, hệ số 1/2 (tránh đường chéo đi qua đỉnh); chóp, tứ diện: 42°, 0,6 cho đáy rộng hơn
    K, Wd = cfg.get('oblique') or ((0.5, 30) if n0 == 8 or cfg.get('proj') == 'oxyz' else (0.6, 42))
    M, d = _proj(cfg.get('proj', 'geo'), K, Wd)
    pr = lambda p: (sum(M[i][0] * p[i] for i in range(3)), sum(M[i][1] * p[i] for i in range(3)))
    solid = cfg.get('solid')
    sn = (list(P) if solid is True else list(solid)) if solid else []
    faces = hull_faces({k: P[k] for k in sn}) if len(sn) >= 4 else []
    # khung và tỉ lệ
    extra = []
    if cfg.get('axes'):
        L = cfg.get('axislen') or max(max(abs(c) for c in p) for p in P.values()) * 1.25 + 0.5
        extra = [(L, 0, 0), (0, L, 0), (0, 0, L), (0, 0, 0)]
    for sp in cfg.get('spheres', []):
        C = P[sp['c']]; Rr = sp['R']
        extra += [tuple(C[i] + Rr * e[i] for i in range(3)) for e in ((1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1))]
    xy = [pr(p) for p in list(P.values()) + extra]
    W_ = max(x for x, _ in xy) - min(x for x, _ in xy) or 1; H_ = max(y for _, y in xy) - min(y for _, y in xy) or 1
    s = min(cfg.get('width', 7.0) / W_, cfg.get('height', 5.6) / H_)
    defs = {'475569': 'c_ax', 'C2410C': 'c_hl'}
    body = []
    drawn = []
    def seg(a, b, color='1F2937', width=1.0, dash=None, arrow=False, auto=True):
        """Đoạn 3D a->b, tự chia nét liền / nét đứt theo phần bị che."""
        drawn.append((a, b))
        N = 48
        flags = [hidden(tuple(a[i] + (b[i] - a[i]) * (k + .5) / N for i in range(3)), faces, d) if (auto and dash is None) else bool(dash) for k in range(N)]
        runs, st = [], 0
        for k in range(1, N + 1):
            if k == N or flags[k] != flags[st]: runs.append((st, k, flags[st])); st = k
        cn = _col(color, defs)
        for i, (u, v, h) in enumerate(runs):
            pa = tuple(a[q] + (b[q] - a[q]) * u / N for q in range(3)); pb = tuple(a[q] + (b[q] - a[q]) * v / N for q in range(3))
            (x1, y1), (x2, y2) = pr(pa), pr(pb)
            opt = [cn, 'line width=%.2fpt' % (width * (0.8 if h else 1))]
            if h: opt.append('dash pattern=on 3pt off 2pt')
            if arrow and i == len(runs) - 1: opt.append('-{Stealth[length=5pt]}')
            body.append('\\draw[%s] (%.4f,%.4f) -- (%.4f,%.4f);' % (','.join(opt), x1, y1, x2, y2))
    # mặt tô màu
    for pg in cfg.get('polygons', []):
        if isinstance(pg, dict): names, fill, op, outline = pg['points'], pg.get('fill', '#86e0bd'), pg.get('opacity', .35), pg.get('outline', True)
        else: names, fill, op, outline = pg, '#86e0bd', .3, True
        cn = _col(fill, defs)
        body.insert(0, '\\fill[%s,fill opacity=%.2f] %s -- cycle;' % (cn, op, ' -- '.join('(%.4f,%.4f)' % pr(P[n]) for n in names)))
        if outline:
            for i in range(len(names)): extra_seg = (names[i], names[(i + 1) % len(names)]); cfg.setdefault('_poly_edges', []).append(extra_seg)
    # trục tọa độ
    if cfg.get('axes'):
        L = cfg.get('axislen') or max(max(abs(c) for c in p) for p in P.values()) * 1.25 + 0.5
        for e, nm in (((L, 0, 0), 'x'), ((0, L, 0), 'y'), ((0, 0, L), 'z')):
            seg((0, 0, 0), e, '475569', 0.7, arrow=True)
            x, y = pr(e); body.append('\\node[anchor=%s,text=c_ax] at (%.4f,%.4f) {$%s$};' % (_anchor(x, y), x, y, nm))
    # cạnh của khối + đoạn khai báo + cạnh đa giác
    done = set()
    declared = {}
    for sgm in cfg.get('segments', []):
        declared[frozenset(sgm[:2])] = sgm[2] if len(sgm) > 2 else {}
    for n, c, ring in faces:
        for i in range(len(ring)):
            e = frozenset((ring[i], ring[(i + 1) % len(ring)]))
            if e in done: continue
            done.add(e); o = declared.get(e, {})
            a, b = sorted(e)
            seg(P[a], P[b], (o.get('color') or '#1F2937').lstrip('#'), 0.45 * o.get('width', 2.2), o.get('dash') if 'dash' in o and o.get('force') else None)
    for sgm in cfg.get('segments', []):
        e = frozenset(sgm[:2])
        if e in done: continue
        done.add(e); o = sgm[2] if len(sgm) > 2 else {}
        dash = o.get('dash') if o.get('force') else None
        seg(P[sgm[0]], P[sgm[1]], (o.get('color') or '#1F2937').lstrip('#'), 0.45 * o.get('width', 2.2), dash, o.get('arrow', False))
    for a, b in cfg.pop('_poly_edges', []):
        e = frozenset((a, b))
        if e in done: continue
        done.add(e); seg(P[a], P[b], '1F2937', 0.8)
    # mặt cầu (đường viền tròn) và đường tròn nằm ngang (nửa sau nét đứt)
    for sp in cfg.get('spheres', []):
        x, y = pr(P[sp['c']]); body.append('\\draw[line width=0.9pt] (%.4f,%.4f) circle[radius=%.4f];' % (x, y, sp['R']))
        if sp.get('fill'): body.insert(0, '\\shade[ball color=%s!25!white,opacity=.35] (%.4f,%.4f) circle[radius=%.4f];' % (_col(sp['fill'], defs), x, y, sp['R']))
    for hc in cfg.get('hcircles', []):
        C = P[hc['c']]; Rr = hc['R']; N = 120; cn = _col(hc.get('color', '#1F2937'), defs)
        pts = [(C[0] + Rr * math.cos(2 * math.pi * k / N), C[1] + Rr * math.sin(2 * math.pi * k / N), C[2]) for k in range(N + 1)]
        back = [_dot(_sub(q, C), d) > 1e-9 for q in pts]
        k = 0
        while k < N:
            j = k
            while j < N and back[j] == back[k]: j += 1
            path = ' -- '.join('(%.4f,%.4f)' % pr(pts[t]) for t in range(k, j + 1))
            body.append('\\draw[%s,line width=%.2fpt%s] %s;' % (cn, 0.8 if back[k] else 1.0, ',dash pattern=on 3pt off 2pt' if back[k] else '', path))
            k = j
    # góc vuông, góc
    for a, o_, b in cfg.get('right', []):
        A3, O3, B3 = P[a], P[o_], P[b]; r = cfg.get('rsize', 0.35)
        u = _sub(A3, O3); v = _sub(B3, O3); u = tuple(x / _norm(u) * r for x in u); v = tuple(x / _norm(v) * r for x in v)
        q1 = tuple(O3[i] + u[i] for i in range(3)); q2 = tuple(O3[i] + u[i] + v[i] for i in range(3)); q3 = tuple(O3[i] + v[i] for i in range(3))
        body.append('\\draw[line width=0.5pt] (%.4f,%.4f) -- (%.4f,%.4f) -- (%.4f,%.4f);' % (pr(q1) + pr(q2) + pr(q3)))
    for a, o_, b in cfg.get('angles', []):
        (xa, ya), (xo, yo), (xb, yb) = pr(P[a]), pr(P[o_]), pr(P[b])
        t1 = math.degrees(math.atan2(ya - yo, xa - xo)); t2 = math.degrees(math.atan2(yb - yo, xb - xo))
        if (t2 - t1) % 360 > 180: t1, t2 = t2, t1
        if t2 < t1: t2 += 360
        r = cfg.get('asize', 0.6)
        body.append('\\draw[c_hl,line width=0.7pt] (%.4f,%.4f) arc[start angle=%.2f,end angle=%.2f,radius=%.3f];' % (xo + r * math.cos(math.radians(t1)), yo + r * math.sin(math.radians(t1)), t1, t2, r))
    # điểm và nhãn
    allp = [pr(p) for p in P.values()]
    cx = sum(x for x, _ in allp) / len(allp); cy = sum(y for _, y in allp) / len(allp)
    nol = set(cfg.get('nolabel', [])); lp = cfg.get('labelpos', {})
    for k, p in P.items():
        x, y = pr(p)
        if k not in sn and not k.startswith('_') and k not in nol: body.append('\\fill (%.4f,%.4f) circle[radius=1.3pt];' % (x, y))
        if k.startswith('_') or k in nol: continue
        if k in lp: anc = POS[lp[k]]
        else:
            dirs = []
            for a3, b3 in drawn:
                ab = _sub(b3, a3); L2 = _dot(ab, ab)
                if L2 < 1e-12: continue
                t = _dot(_sub(p, a3), ab) / L2; q = tuple(a3[i] + t * ab[i] for i in range(3))
                if _norm(_sub(q, p)) > 1e-6 or t < -1e-6 or t > 1 + 1e-6: continue
                (xa, ya), (xb, yb) = pr(a3), pr(b3)
                if t > 1e-6: dirs.append(math.atan2(ya - y, xa - x))
                if t < 1 - 1e-6: dirs.append(math.atan2(yb - y, xb - x))
            out = math.atan2(y - cy, x - cx) if math.hypot(x - cx, y - cy) > 1e-6 else -math.pi / 2
            def score(th):
                gap = min([abs((th - d0 + math.pi) % (2 * math.pi) - math.pi) for d0 in dirs] or [math.pi])
                return min(gap, math.radians(70)) + 0.25 * math.cos(th - out)
            best = max((math.radians(45 * i) for i in range(8)), key=score)
            anc = _anchor(math.cos(best), math.sin(best))
        body.append('\\node[anchor=%s,inner sep=2pt] at (%.4f,%.4f) {$%s$};' % (anc, x, y, _lab(k)))
    cols = ''.join('\\definecolor{%s}{HTML}{%s}\n' % (v, k) for k, v in defs.items())
    return ('\\documentclass[tikz,border=3pt]{standalone}\n\\usetikzlibrary{arrows.meta}\n\\begin{document}\n%s'
            '\\begin{tikzpicture}[x=%.4fcm,y=%.4fcm,line cap=round,line join=round]\n%s\n\\end{tikzpicture}\n\\end{document}\n') % (cols, s, s, '\n'.join(body))

def svg(cfg):
    """Biên dịch (có bộ nhớ đệm) và trả về tên tệp SVG trong img/fig3d/."""
    tex = tikz(dict(cfg))
    h = hashlib.md5(tex.encode('utf-8')).hexdigest()[:16]
    os.makedirs(OUT, exist_ok=True)
    fn = os.path.join(OUT, h + '.svg')
    if not os.path.exists(fn):
        tmp = tempfile.mkdtemp()
        try:
            open(os.path.join(tmp, 'f.tex'), 'w', encoding='utf-8').write(tex)
            r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'f.tex'], cwd=tmp, capture_output=True, text=True)
            if r.returncode: raise RuntimeError('TikZ lỗi:\n' + r.stdout[-2500:] + '\n' + tex)
            subprocess.run(['pdftocairo', '-svg', 'f.pdf', 'f.svg'], cwd=tmp, check=True)
            shutil.copy(os.path.join(tmp, 'f.svg'), fn)
            open(os.path.join(OUT, h + '.tex'), 'w', encoding='utf-8').write(tex)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    return h + '.svg'
