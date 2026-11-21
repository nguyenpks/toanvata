# -*- coding: utf-8 -*-
"""Kiểm định ĐỘC LẬP các câu thêm ngày 21/11/2026 cho lớp 12, Bài 5–8 (g12-optim-01, g12-vec-01, g12-coord-01, g12-coord-02).
Không dùng mã sinh câu (sp_g12r5, sp_g12r, …): đọc trang đã dựng và nguồn TeX của hình, tự dựng lại dữ kiện rồi tính đáp số
bằng cách khác (vét cạn trên lưới số, dựng tọa độ khác, kiểm tra từng phương án). Trắc nghiệm: đúng MỘT phương án khớp.

    python tools/audit_g12r5.py          # in số câu đúng / tổng số; liệt kê câu sai, câu không nhận ra dạng
    python tools/audit_g12r5.py --mutate # thử đột biến: đổi đáp án trang, mọi câu phải bị bắt lỗi
"""
import os, re, sys, math, itertools, html as _h
from fractions import Fraction as F
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from question_bank import parse_page          # chỉ dùng để tách câu hỏi khỏi trang HTML

PAGES = {'g12-optim-01': 'lessons/grade12/derivative-applications/optimization-problems.html',
         'g12-vec-01': 'lessons/grade12/vectors-in-space/vectors-in-space.html',
         'g12-coord-01': 'lessons/grade12/vectors-in-space/coordinate-system-oxyz.html',
         'g12-coord-02': 'lessons/grade12/vectors-in-space/vector-coordinates.html'}

# ------------------------------------------------------------------ đọc văn bản, số, phương án
def plain(h): return re.sub(r'\s+', ' ', _h.unescape(re.sub(r'<[^>]+>', ' ', h))).strip()
def en_opt(o):
    m = re.search(r'<span class="en">(.*?)</span>', o, re.S); return plain(m.group(1) if m else o)
def val(s):
    """'\\(\\dfrac{3}{7}\\)', '-\\dfrac{1}{2}', '12', '25.2' → Fraction."""
    s = s.replace('\\(', '').replace('\\)', '').replace('{,}', '.').replace(' ', '')
    m = re.fullmatch(r'(-?)\\dfrac\{(\d+)\}\{(\d+)\}', s)
    if m: return (-1 if m.group(1) else 1) * F(int(m.group(2)), int(m.group(3)))
    m = re.fullmatch(r'-?\d+(?:\.\d+)?', s)
    return F(s) if m else None
def pt(s, name):
    m = re.search(re.escape(name) + r'\((-?\d+);\\,(-?\d+);\\,(-?\d+)\)', s)
    return tuple(int(x) for x in m.groups()) if m else None
def vec(s, name):
    m = re.search(re.escape(name) + r'=\((-?\d+);\\,(-?\d+);\\,(-?\d+)\)', s)
    return tuple(int(x) for x in m.groups()) if m else None
def triple(o):
    m = re.fullmatch(r'\\\(\((-?\d+|-?\\dfrac\{\d+\}\{\d+\});\\,(-?\d+|-?\\dfrac\{\d+\}\{\d+\});\\,(-?\d+|-?\\dfrac\{\d+\}\{\d+\})\)\\\)', o.strip())
    return tuple(val(x) for x in m.groups()) if m else None
def num_after(s, rx):
    m = re.search(rx, s); return int(m.group(1)) if m else None
def dot(a, b): return sum(x * y for x, y in zip(a, b))
def sub(a, b): return tuple(x - y for x, y in zip(a, b))

# ------------------------------------------------------------------ BÀI 5
def tex_of(img): return open(os.path.join(ROOT, 'img', 'tex', os.path.basename(img)[:-4] + '.tex'), encoding='utf-8').read()
def graph_vmax(q):
    """Đồ thị V'(t): đọc trục, đường cong, vạch chia và nhãn → thời điểm V'(t) đổi dấu từ + sang −."""
    t = tex_of(q['images'][0])
    ax = re.search(r'\\draw\[ink!85.*?\] \((-?[\d.]+),(-?[\d.]+)\) -- \((-?[\d.]+),(-?[\d.]+)\);', t); oy = float(ax.group(2))
    cur = []
    for m in re.finditer(r'\\draw\[color=\{rgb,255:red,4;green,107;blue,77\}, line width=1.3pt\] (.*?);', t):
        cur += [(float(a), float(b)) for a, b in re.findall(r'\((-?[\d.]+),(-?[\d.]+)\)', m.group(1))]
    ticks = [float(x) for x in re.findall(r'\\draw\[ink!70\] \((-?[\d.]+),', t)]
    labs = re.findall(r'fill=white\] at \([^)]*\) \{\$([^$]*)\$\}', t)
    assert len(ticks) == len(labs)
    cross = [(cur[i][0] + cur[i + 1][0]) / 2 for i in range(len(cur) - 1) if cur[i][1] - oy > 1e-3 and cur[i + 1][1] - oy <= 1e-3]
    assert len(cross) == 1, cross
    k = min(range(len(ticks)), key=lambda i: abs(ticks[i] - cross[0])); assert abs(ticks[k] - cross[0]) < 0.05
    # V tăng trên đoạn đầu (đồ thị V' ở trên trục), không còn đổi dấu nữa → lớn nhất tại điểm đổi dấu
    assert cur[-1][1] < oy
    return F(labs[k])

def grid_max(f, a, b, n=20000):
    best = None
    for i in range(n + 1):
        x = a + (b - a) * F(i, n); y = f(x)
        if best is None or y > best[1]: best = (x, y)
    return best

def solve_optim(q):
    s = q['en']
    if 'V′(t)' in s and q['images']: return ('mcq', graph_vmax(q))
    m = re.search(r's\(t\)=-t\^3\+(\d+)t\^2\+(\d+)t', s)
    if m:
        A, B = int(m.group(1)), int(m.group(2)); T = num_after(s, r'0\\le t\\le (\d+)') or num_after(s, r'\[0;\\,(\d+)\]') or num_after(s, r'first \\\((\d+)\\\) seconds')
        v = lambda t: -3 * t * t + 2 * A * t + B
        return ('mcq', grid_max(v, F(0), F(T), 600 * T)[1])
    m = re.search(r'AB=(\d+)\\?\)? m.*?AC=(\d+)', plain(s))
    if m and ('rectang' in s and 'BC' in s):
        a, b = int(m.group(1)), int(m.group(2))
        return ('mcq', grid_max(lambda x: x * b * (1 - x / a), F(0), F(a), 4 * a)[1])
    m = re.search(r'N\(t\)=t\^3-([\d.]+)t\^2\+(\d+)t\+(\d+)', s)
    if m:
        c2, c1, c0 = F(m.group(1)), int(m.group(2)), int(m.group(3)); N = lambda t: t ** 3 - c2 * t * t + c1 * t + c0
        T = num_after(s, r'0\\le t\\le (\d+)') or num_after(s, r'\[0;\\,(\d+)\]'); k = num_after(s, r'at \\\(t=(\d+)\\\)')
        pts = [F(i, 100) for i in range(0, 100 * T + 1)]; vals = [N(x) for x in pts]
        if 'largest' in s: tt = pts[vals.index(max(vals))]
        else: tt = pts[vals.index(min(vals))]
        return ('tf', tt == k)
    m = re.search(r'(?:area|garden of) \\\((\d+)\\ \\text\{m\}\^2\\\)', s)
    if m and 'wall' in s:
        S = int(m.group(1)); pr = [int(x) for x in re.findall(r'\\\((\d)00\\,000\\\)', s)]; p1, p2 = pr[0], pr[1]
        cost = lambda x: (p1 * x + p2 * (x + 2 * S / x)) / 10           # triệu đồng
        best = min(((F(i, 10), cost(F(i, 10))) for i in range(1, 10 * S + 1)), key=lambda z: z[1])
        return ('short', best[0] if re.search(r'Find \\\(x\\\)', s) else best[1])
    return None

# ------------------------------------------------------------------ BÀI 6
SKEW = {'A': (0, 0, 0), 'B': (F(5, 2), F(1, 3), 0), 'D': (F(2, 3), F(7, 4), 0), 'A′': (F(1, 2), F(3, 5), F(9, 4))}
def hop(P0):
    P = dict(P0); A, B, D, A1 = P['A'], P['B'], P['D'], P['A′']
    add = lambda *v: tuple(sum(x) for x in zip(*v))
    P['C'] = add(B, sub(D, A)); P['B′'] = add(B, sub(A1, A)); P['D′'] = add(D, sub(A1, A)); P['C′'] = add(P['C'], sub(A1, A)); return P
def solve_vec(q):
    s = q['en']; t = plain(s)
    m = re.search(r'equal to \\\(\\overrightarrow\{(\w′?)(\w′?)\}\\\)|opposite to \\\(\\overrightarrow\{(\w′?)(\w′?)\}\\\)', s)
    if m and 'parallelepiped' in s:
        P = hop(SKEW); names = list(P)
        if m.group(1): p, r_ = m.group(1), m.group(2); u = sub(P[r_], P[p]); n = sum(1 for x in names for y in names if x != y and sub(P[y], P[x]) == u and (x, y) != (p, r_))
        else: p, r_ = m.group(3), m.group(4); u = sub(P[r_], P[p]); n = sum(1 for x in names for y in names if x != y and sub(P[y], P[x]) == tuple(-c for c in u))
        return ('mcq', F(n))
    m = re.search(r'AB=(\d+)\\\) m, \\\(AD=(\d+)\\\) m, (?:height )?\\\(AA′=(\d+)\\\) m', s)
    if m:
        a, b, c = (int(x) for x in m.groups())
        P = {'A': (0, 0, 0), 'B': (a, 0, 0), 'D': (0, b, 0), 'A′': (0, 0, c)}; P = hop(P)
        vs = re.findall(r'\\overrightarrow\{(\w′?)(\w′?)\}', s)[:2]
        u, w = sub(P[vs[0][1]], P[vs[0][0]]), sub(P[vs[1][1]], P[vs[1][0]])
        cs = dot(u, w) / math.sqrt(dot(u, u) * dot(w, w)); return ('mcq', F(cs).limit_denominator(1000))
    m = re.search(r'OA=(\d+)\\?\)? dm.*?SO=(\d+)', t)
    if m and 'S.ABCD' in s:
        e, h = int(m.group(1)), int(m.group(2)); ang = 0.3                       # đáy xoay một góc tùy ý
        P = {'A': (e * math.cos(ang), e * math.sin(ang), 0), 'B': (-e * math.sin(ang), e * math.cos(ang), 0), 'C': (-e * math.cos(ang), -e * math.sin(ang), 0), 'S': (0, 0, h)}
        X = re.search(r'\\overrightarrow\{SA\}\\cdot\\overrightarrow\{S(\w)\}', s).group(1)
        return ('mcq', F(round(dot(sub(P['A'], P['S']), sub(P[X], P['S'])), 6)).limit_denominator(100))
    if 'cube' in s and ('perp' in s or 'perpendicular' in s or '=0' in s):
        C = hop({'A': (0, 0, 0), 'B': (1, 0, 0), 'D': (0, 1, 0), 'A′': (0, 0, 1)})
        vs = re.findall(r'\\overrightarrow\{(\w′?)(\w′?)\}', s)[:2]
        return ('tf', dot(sub(C[vs[0][1]], C[vs[0][0]]), sub(C[vs[1][1]], C[vs[1][0]])) == 0)
    m = re.search(r'AB=(\d+)\\\), \\\(CD=(\d+)\\\).*?(\d+)\^\\circ', s)
    if m and 'midpoints of \\(AD\\)' in s:
        p, r_, ang = (int(x) for x in m.groups()); ph = math.radians(ang)
        A = (0, 0, 0); B = (p, 0, 0); D = (0.7, 1.3, 2.1); C = (D[0] + r_ * math.cos(ph), D[1] + r_ * math.sin(ph), D[2])   # DC tạo với AB góc φ
        M = tuple((x + y) / 2 for x, y in zip(A, D)); N = tuple((x + y) / 2 for x, y in zip(B, C))
        return ('short', F(round(math.dist(M, N), 6)).limit_denominator(100))
    return None

# ------------------------------------------------------------------ BÀI 7
def solve_c7(q):
    s = q['en']
    if 'coordinates of \\(\\overrightarrow{AB}\\)' in s or 'vector \\(\\overrightarrow{AB}\\)' in s or '\\(\\overrightarrow{AB}=\\)…' in s:
        A, B = pt(s, 'A'), pt(s, 'B'); return ('mcq3', sub(B, A))
    m = re.search(r'\\\((\d+)\\\) m from (?:the wall )?\\\(\(Oyz\)\\\), \\\((\d+)\\\) m from (?:the wall )?\\\(\(Oxz\)\\\) and (?:\\\((\d+)\\\) m above the floor|at height \\\((\d+)\\\) m)', s)
    if m:
        dx, dy, h = int(m.group(1)), int(m.group(2)), int(m.group(3) or m.group(4))
        return ('mcq3pred', lambda P: P[0] > 0 and P[1] > 0 and P[2] > 0 and abs(P[0]) == dx and abs(P[1]) == dy and abs(P[2]) == h)
    m = re.search(r'cube \\\(ABCD\.A′B′C′D′\\\)(?: with| of)? edge \\\((\d+)\\\)|has edge \\\((\d+)\\\)', s)
    if m and 'Oxyz' in s or (m and 'origin' in s):
        a = int(m.group(1) or m.group(2)); C = hop({'A': (0, 0, 0), 'B': (a, 0, 0), 'D': (0, a, 0), 'A′': (0, 0, a)})
        avg = lambda ks: tuple(F(sum(C[k][i] for k in ks), len(ks)) for i in range(3))
        if 'center \\(I\\) of the cube' in s: I = avg(list(C))
        else:
            f = re.search(r'face \\\((\w′?)(\w′?)(\w′?)(\w′?)\\\)', s); e = re.search(r'edge \\\((\w′?)(\w′?)\\\)\. ?|midpoint \\\(I\\\) of the edge \\\((\w′?)(\w′?)\\\)', s)
            if f: I = avg(list(f.groups()))
            else:
                g = re.search(r'midpoint \\\(I\\\) of the edge \\\((\w′?)(\w′?)\\\)', s); I = avg([g.group(1), g.group(2)])
        return ('mcq3', I)
    m = re.search(r'M\((\d+);\\,(\d+);\\,(\d+)\)', s)
    if m and ('plane' in s or 'd\\left(M' in s) and q['type'] == 'tf':
        M = tuple(int(x) for x in m.groups()); pl = re.search(r'\((O[xyz]{2})\)', s).group(1)
        v = int(re.search(r'(?:equals|distance) \\\((\d+)\\\)|\)=(\d+)\\\)', s).group(1) or re.search(r'\)=(\d+)\\\)', s).group(1)) if re.search(r'(?:equals|distance) \\\((\d+)\\\)', s) else int(re.search(r'\\right\)=(\d+)', s).group(1))
        nrm = {'Oxy': (0, 0, 1), 'Oyz': (1, 0, 0), 'Oxz': (0, 1, 0)}[pl]
        return ('tf', abs(dot(M, nrm)) == v)
    if 'overrightarrow{AB}=(' in s and q['type'] == 'short':
        A = pt(s, 'A'); u = vec(s, '\\overrightarrow{AB}'); B = tuple(x + y for x, y in zip(A, u))
        if 'x_B+y_B+z_B' in s: return ('short', F(sum(B)))
        c = re.search(r'the \\\(([xyz])\\\)-coordinate', s).group(1); return ('short', F(B['xyz'.index(c)]))
    return None

# ------------------------------------------------------------------ BÀI 8
def solve_c8(q):
    s = q['en']
    m = re.search(r'\\vec a=\((-?\d+);\\,m;\\,(-?\d+)\)\\\),? (?:and )?\\\(\\vec b=\((-?\d+|-?\\dfrac\{\d+\}\{\d+\});\\,(-?\d+);\\,n\)', s)
    if m:
        p, qq, bp, s_ = int(m.group(1)), int(m.group(2)), val(m.group(3)), int(m.group(4))
        def ok(o):
            mm = re.search(r'm=(-?[\d]+|-?\\dfrac\{\d+\}\{\d+\}),\\ n=(-?[\d]+|-?\\dfrac\{\d+\}\{\d+\})', o); mv, nv_ = val(mm.group(1)), val(mm.group(2))
            a, b = (p, mv, qq), (bp, s_, nv_)
            cr = (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]); return cr == (0, 0, 0)
        return ('mcqpred', ok)
    m = re.search(r'\\vec F=\((-?\d+);\\,(-?\d+);\\,(-?\d+)\)', s)
    if m and 'work' in s:
        Fv = tuple(int(x) for x in m.groups()); A, B = pt(s, 'A'), pt(s, 'B'); return ('mcq', F(dot(Fv, sub(B, A))))
    if 'x\\vec a+y\\vec b' in s:
        a, b, c = vec(s, '\\vec a'), vec(s, '\\vec b'), vec(s, '\\vec c')
        sols = [(x, y) for x in range(-12, 13) for y in range(-12, 13) if tuple(x * i + y * j for i, j in zip(a, b)) == c]
        assert len(sols) == 1, sols
        if 'x+y' in s: return ('mcq', F(sum(sols[0])))
        return ('mcqpred', lambda o: re.search(r'x=(-?\d+),\\ y=(-?\d+)', o) and tuple(int(z) for z in re.search(r'x=(-?\d+),\\ y=(-?\d+)', o).groups()) == sols[0])
    if q['type'] == 'tf' and pt(s, 'M') and pt(s, 'A') and pt(s, 'B'):
        A, B, M = pt(s, 'A'), pt(s, 'B'), pt(s, 'M'); X = re.search(r'(?:router at|nearer to|closer to lamp) \\\(([AB])\\\)', s).group(1)
        dA, dB = math.dist(M, A), math.dist(M, B); return ('tf', (dA < dB) == (X == 'A'))
    m = re.search(r'\\vec u=\((-?\d+);\\,(-?\d+);\\,(-?\d+)\)', s)
    if m and q['type'] == 'short':
        u = tuple(int(x) for x in m.groups()); v = vec(s, '\\vec v')
        return ('short', F(round(math.degrees(math.acos(dot(u, v) / math.sqrt(dot(u, u) * dot(v, v)))))))
    return None

SOLVERS = {'g12-optim-01': solve_optim, 'g12-vec-01': solve_vec, 'g12-coord-01': solve_c7, 'g12-coord-02': solve_c8}
NEW = (3, 2, 2)                   # số câu cũ ở A, B, C trước đợt này; câu mới nằm sau đó

def new_items(qs):
    out = []
    for lv in (1, 2, 3):
        for sec, k in zip('ABC', NEW):
            out += [q for q in qs if q['level'] == lv and q['section'].startswith(sec)][k:]
    return out

def check(q, solver):
    q = dict(q, en=_h.unescape(q['en']).replace("'", '′'))       # trang ghi A' (dấu nháy), mã kiểm định dùng A′
    r = solver(q)
    if r is None: return None, 'không nhận ra dạng'
    kind, want = r
    if q['type'] == 'tf':
        return (('true' if want else 'false') == q['answer']), 'đáp án tự tính: %s' % want
    if q['type'] == 'short':
        got = val(q['answer'].replace(',', '.')); return got == F(want), 'tự tính %s, trang %s' % (want, q['answer'])
    opts = [en_opt(o) for o in q['options']]; raw = [re.search(r'<span class="en">(.*?)</span>', o, re.S).group(1) if '<span class="en">' in o else o for o in q['options']]
    if kind == 'mcq': hits = [i for i, o in enumerate(raw) if val(o) == F(want)]
    elif kind == 'mcq3': hits = [i for i, o in enumerate(raw) if triple(o) == tuple(F(x) for x in want)]
    elif kind == 'mcq3pred': hits = [i for i, o in enumerate(raw) if triple(o) and want(triple(o))]
    else: hits = [i for i, o in enumerate(raw) if want(o)]
    return (len(hits) == 1 and 'abcd'[hits[0]] == q['answer']), 'phương án khớp: %s, trang: %s' % (['abcd'[i] for i in hits], q['answer'])

def main():
    mutate = '--mutate' in sys.argv
    tot = good = 0; bad = []; caught = 0
    for lid, path in PAGES.items():
        qs = parse_page(open(os.path.join(ROOT, path), encoding='utf-8').read()); items = new_items(qs)
        assert len(items) == 15, (lid, len(items))
        for q in items:
            tot += 1; ok, msg = check(q, SOLVERS[lid])
            if ok: good += 1
            else: bad.append((lid, q['level'], q['section'][:1], msg, plain(q['en'])[:110]))
            if mutate and ok:
                q2 = dict(q)
                if q['type'] == 'tf': q2['answer'] = 'false' if q['answer'] == 'true' else 'true'
                elif q['type'] == 'short': q2['answer'] = str(val(q['answer'].replace(',', '.')) + 1)
                else: q2['answer'] = 'abcd'[('abcd'.index(q['answer']) + 1) % 4]
                caught += not check(q2, SOLVERS[lid])[0]
    print('Kiểm định độc lập Bài 5–8 (câu mới): %d / %d đúng.' % (good, tot))
    for b in bad: print('  ✗', *b)
    if mutate: print('Thử đột biến: bắt được %d / %d.' % (caught, good))
    sys.exit(1 if bad else 0)

if __name__ == '__main__':
    main()
