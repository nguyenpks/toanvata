# -*- coding: utf-8 -*-
"""Hình 2D TĨNH cho câu hỏi tự luyện (TikZ thuần → SVG qua mb_pgf.texsvg).
Mọi nhãn (tên điểm, số trên trục, tên đường) được đặt bằng bộ chọn chỗ trống:
mỗi ứng viên vị trí bị phạt khi hộp nhãn chạm nét vẽ (đồ thị, trục, nét đứt) hoặc nhãn khác → nét vẽ không đi qua nhãn."""
import math
from fractions import Fraction as F
from mb_pgf import texsvg, col, _USED

GREEN, ORANGE, BLUE = '046b4d', 'c2410c', '1d4ed8'

def pitex(fr, frac='\\frac'):
    """Bội của π (Fraction) → TeX."""
    fr = F(fr)
    if fr == 0: return '0'
    n, d = abs(fr.numerator), fr.denominator; s = '-' if fr < 0 else ''
    num = ('' if n == 1 else str(n)) + '\\pi'
    return s + (num if d == 1 else '%s{%s}{%d}' % (frac, num, d))

class Canvas:
    def __init__(s): s.o = []; s.polys = []; s.boxes = []
    def poly(s, pts, style, close=False):
        s.polys.append(list(pts) + ([pts[0]] if close else []))
        s.o.append('\\draw[%s] %s%s;' % (style, ' -- '.join('(%.3f,%.3f)' % p for p in pts), ' -- cycle' if close else ''))
    def seg_only(s, pts):            # tính vào vật cản nhưng không vẽ (ví dụ đường tròn vẽ riêng)
        s.polys.append(list(pts))
    def hits(s, box):
        x0, y0, x1, y1 = box; k = 0
        for P in s.polys:
            for (ax, ay), (bx, by) in zip(P, P[1:]):
                L = math.hypot(bx - ax, by - ay); m = max(2, int(L / 0.04))
                for i in range(m + 1):
                    x = ax + (bx - ax) * i / m; y = ay + (by - ay) * i / m
                    if x0 <= x <= x1 and y0 <= y <= y1: k += 1
        for b in s.boxes:
            if not (x1 < b[0] or b[2] < x0 or y1 < b[1] or b[3] < y0): k += 50
        return k
    def label(s, x, y, tex, w, h, cands, white=False):
        """cands: các vectơ (dx, dy) cm từ (x, y) tới TÂM nhãn – thử lần lượt, chọn chỗ ít va chạm nhất (ưu tiên thứ tự)."""
        best = None
        for j, (dx, dy) in enumerate(cands):
            cx, cy = x + dx, y + dy; box = (cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2)
            p = s.hits(box) * 10 + j
            if best is None or p < best[0]: best = (p, cx, cy, box)
        _, cx, cy, box = best; s.boxes.append(box)
        s.o.append('\\node[font=\\small, text=ink, inner sep=0.5pt%s] at (%.3f,%.3f) {%s};' % (', fill=white' if white else '', cx, cy, tex))
        return best[0]
    def dot(s, x, y, color=GREEN, open_=False):
        s.boxes.append((x - 0.07, y - 0.07, x + 0.07, y + 0.07))
        if open_: s.o.append('\\draw[draw=%s, fill=white, line width=1pt] (%.3f,%.3f) circle (2.2pt);' % (col(color), x, y))
        else: s.o.append('\\fill[color=%s] (%.3f,%.3f) circle (2.2pt);' % (col(color), x, y))
    def svg(s):
        return texsvg('\\begin{tikzpicture}\n' + '\n'.join(s.o) + '\n\\end{tikzpicture}')

def lw(tex):
    """Ước lượng kích thước hộp nhãn (cm)."""
    import re
    t = re.sub(r'\\(frac|dfrac|tfrac)\{([^{}]*)\}\{([^{}]*)\}', lambda m: max(m.group(2), m.group(3), key=len), tex)
    t = re.sub(r'\\pi', 'p', t); t = re.sub(r'\\sqrt\{?(\w)\}?', r'v\1', t); t = re.sub(r'[\\${}]|text|mathrm', '', t)
    h = 0.62 if 'frac' in tex else 0.36
    return 0.14 + 0.17 * len(t), h

AROUND = [(0.28, 0.28), (-0.28, 0.28), (0.28, -0.28), (-0.28, -0.28), (0.36, 0), (-0.36, 0), (0, 0.32), (0, -0.32)]

def ring(r, n=16, start=0):
    return [(r * math.cos(math.radians(start + 360 * i / n)), r * math.sin(math.radians(start + 360 * i / n))) for i in range(n)]

# ---------------------------------------------------------------- đường tròn lượng giác
def circle_svg(pts, segs=(), proj=None, showA=True, R=1.9, dashed=(), rays=()):
    """pts: [(góc độ, tên hoặc None)]; segs: [(góc1, góc2)] nối hai điểm (nét liền); dashed: tương tự (nét đứt);
    proj: (góc, nhãn_x, nhãn_y) vẽ hình chiếu nét đứt của điểm xuống hai trục kèm nhãn số."""
    c = Canvas(); E = 1.38 * R
    c.poly([(-E, 0), (E, 0)], 'ink!85, line width=0.7pt, -{Stealth[length=2.4mm]}')
    c.poly([(0, -E), (0, E)], 'ink!85, line width=0.7pt, -{Stealth[length=2.4mm]}')
    circ = [(R * math.cos(2 * math.pi * i / 120), R * math.sin(2 * math.pi * i / 120)) for i in range(121)]
    c.seg_only(circ); c.o.append('\\draw[color=%s, line width=1.1pt] (0,0) circle (%.3f);' % (col(GREEN), R))
    P = lambda a: (R * math.cos(math.radians(a)), R * math.sin(math.radians(a)))
    for a, b in segs: c.poly([P(a), P(b)], 'ink, line width=0.8pt')
    for a in rays: c.poly([(0, 0), P(a)], 'ink, line width=0.8pt')
    for a, b in dashed: c.poly([P(a), P(b)], 'ink, line width=0.7pt, dash pattern=on 4pt off 3pt')
    if proj:
        a, lx, ly = proj; x, y = P(a)
        c.poly([(x, y), (x, 0)], 'asy, line width=0.6pt, dash pattern=on 3pt off 2.5pt')
        c.poly([(x, y), (0, y)], 'asy, line width=0.6pt, dash pattern=on 3pt off 2.5pt')
    c.o.append('\\node[font=\\small, text=ink] at (%.3f,-0.25) {$x$};' % (E - 0.05)); c.boxes.append((E - 0.25, -0.45, E + 0.15, -0.05))
    c.o.append('\\node[font=\\small, text=ink] at (-0.25,%.3f) {$y$};' % (E - 0.05)); c.boxes.append((-0.45, E - 0.25, -0.05, E + 0.15))
    for a, nm in pts:
        x, y = P(a); c.dot(x, y)
    if showA: c.dot(R, 0)
    # nhãn: điểm trước (hướng ra ngoài), rồi O, A, nhãn chiếu
    for a, nm in pts:
        if not nm: continue
        x, y = P(a); w, h = lw(nm); cands = []
        for da in (0, 16, -16, 30, -30):
            t = math.radians(a + da); cands.append((0.36 * math.cos(t), 0.36 * math.sin(t)))
        c.label(x, y, '$%s$' % nm, w, h, cands)
    if showA: c.label(R, 0, '$A$', 0.3, 0.36, [(0.22, -0.26), (0.22, 0.26), (0.3, -0.3)])
    c.label(0, 0, '$O$', 0.3, 0.36, [(-0.2, -0.24), (0.2, -0.24), (-0.2, 0.24), (0.2, 0.24)])
    if proj:
        a, lx, ly = proj; x, y = P(a)
        w, h = lw(lx); sx_ = -1 if x > 0 else 1; vy = -0.42 if y > 0 else 0.42
        c.label(x, 0, '$%s$' % lx, w, h, [(0, vy), (sx_ * 0.3, vy), (sx_ * 0.5, vy), (0, -vy), (sx_ * 0.4, -vy)])
        w, h = lw(ly); hx = -0.5 if x > 0 else 0.5; vy_ = -1 if y > 0 else 1
        c.label(0, y, '$%s$' % ly, w, h, [(hx, 0), (hx, vy_ * 0.3), (hx, vy_ * 0.5), (-hx, 0), (-hx, vy_ * 0.4)])
    return c.svg()

# ---------------------------------------------------------------- đồ thị hàm số (TikZ thuần)
def graph_svg(curves, xr, yr, xticks, yticks, hlines=(), vlines=(), dots=(), W=9.0, H=4.6, names=('x', 'y'), hlabel=True):
    """curves: [(f, màu)] f trả None ngoài miền; xticks: [(giá trị, tex)]; yticks: [(giá trị, tex)];
    hlines/vlines: [(giá trị, tex hoặc None)] nét đứt; dots: [(x, y, rỗng?)]."""
    (x0, x1), (y0, y1) = xr, yr
    sx = W / (x1 - x0); sy = H / (y1 - y0); X = lambda x: (x - x0) * sx; Y = lambda y: (y - y0) * sy
    c = Canvas()
    oy = Y(0) if y0 <= 0 <= y1 else 0.0; ox = X(0) if x0 <= 0 <= x1 else 0.0
    c.poly([(0, oy), (W + 0.35, oy)], 'ink!85, line width=0.7pt, -{Stealth[length=2.4mm]}')
    c.poly([(ox, 0), (ox, H + 0.35)], 'ink!85, line width=0.7pt, -{Stealth[length=2.4mm]}')
    for v, t in hlines: c.poly([(0, Y(v)), (W, Y(v))], 'asy, line width=0.8pt, dash pattern=on 5pt off 3.5pt')
    for v, t in vlines: c.poly([(X(v), 0), (X(v), H)], 'asy, line width=0.8pt, dash pattern=on 5pt off 3.5pt')
    for f, colr in curves:
        cur = []
        N = 600
        for i in range(N + 1):
            x = x0 + (x1 - x0) * i / N
            try: y = f(x)
            except (ZeroDivisionError, ValueError): y = None
            if y is None or not (y0 - 1e-9 <= y <= y1 + 1e-9):
                if len(cur) > 1: c.poly(cur, 'color=%s, line width=1.3pt' % col(colr))
                cur = []
            else: cur.append((X(x), Y(y)))
        if len(cur) > 1: c.poly(cur, 'color=%s, line width=1.3pt' % col(colr))
    for x, y, op in dots: c.dot(X(x), Y(y), ORANGE if op else GREEN, open_=op)
    for v, t in xticks:
        c.o.append('\\draw[ink!70] (%.3f,%.3f) -- (%.3f,%.3f);' % (X(v), oy - 0.07, X(v), oy + 0.07))
    for v, t in yticks:
        c.o.append('\\draw[ink!70] (%.3f,%.3f) -- (%.3f,%.3f);' % (ox - 0.07, Y(v), ox + 0.07, Y(v)))
    c.o.append('\\node[font=\\small, text=ink] at (%.3f,%.3f) {$%s$};' % (W + 0.3, oy - 0.28, names[0])); c.boxes.append((W + 0.05, oy - 0.5, W + 0.55, oy - 0.06))
    c.o.append('\\node[font=\\small, text=ink] at (%.3f,%.3f) {$%s$};' % (ox - 0.3, H + 0.3, names[1])); c.boxes.append((ox - 0.55, H + 0.08, ox - 0.05, H + 0.5))
    for v, t in xticks:
        w, h = lw(t); d = h / 2 + 0.1
        c.label(X(v), oy, '$%s$' % t, w, h, [(0, -d), (0, d), (0.12, -d), (-0.12, -d), (0.12, d), (-0.12, d)], white=True)
    for v, t in yticks:
        w, h = lw(t); d = w / 2 + 0.1
        c.label(ox, Y(v), '$%s$' % t, w, h, [(-d, 0), (d, 0), (-d, h / 2 + 0.08), (d, h / 2 + 0.08), (-d, -h / 2 - 0.08), (d, -h / 2 - 0.08)], white=True)
    if x0 < 0 < x1 and y0 < 0 < y1: c.label(ox, oy, '$O$', 0.3, 0.36, [(-0.2, -0.24), (0.2, -0.24), (-0.2, 0.24), (0.2, 0.24), (-0.2, -0.5), (0.2, -0.5)])
    if hlabel:
        for v, t in hlines:
            if t: w, h = lw(t); c.label(W, Y(v), '$%s$' % t, w, h, [(-w / 2, 0.3), (-w / 2, -0.3), (-w / 2 - 1, 0.3), (-w / 2 - 1, -0.3), (-w / 2 - 2, 0.3), (-w / 2 - 2, -0.3)], white=True)
        for v, t in vlines:
            if t: w, h = lw(t); c.label(X(v), H, '$%s$' % t, w, h, [(w / 2 + 0.1, -0.1), (-w / 2 - 0.1, -0.1), (w / 2 + 0.1, -0.8), (-w / 2 - 0.1, -0.8)], white=True)
    return c.svg()

def pi_ticks(lo, hi, step):
    """Các vạch bội của step·π trong [lo; hi] (Fraction của π), bỏ 0."""
    out = []; k = math.ceil(F(lo) / F(step))
    while k * F(step) <= F(hi):
        v = k * F(step)
        if v != 0: out.append((float(v) * math.pi, pitex(v)))
        k += 1
    return out

def int_ticks(lo, hi, step=1, skip0=True, fmt=str):
    out = []; v = math.ceil(lo / step) * step
    while v <= hi + 1e-9:
        if not (skip0 and abs(v) < 1e-9): out.append((v, fmt(v)))
        v += step
    return out

def img(fn, alt, px=420):
    import html as _h
    _USED.append(fn)
    return ('<img src="../../../img/tex/%s" alt="%s" loading="lazy" style="display:block;margin:8px auto;width:min(100%%,%dpx);height:auto">' % (fn, _h.escape(alt, quote=True), px))
def FIG(fn, alt_en='Figure', alt_vi='Hình vẽ', px=420):
    return (img(fn, alt_en, px), img(fn, alt_vi, px))

# ---------------------------------------------------------------- biểu đồ tần số dạng cột liền (histogram)
def hist_svg(edges, fs, xlab, ylab, W=7.2, H=4.2, pct=False, vi=False):
    k = len(fs); bw = W / k; m = max(fs); step = 1 if m <= 8 else 2 if m <= 16 else 5
    top = (m // step + 1) * step; sy = H / top
    o = ['\\draw[ink!85, line width=0.7pt, -{Stealth[length=2.4mm]}] (0,0) -- (%.3f,0);' % (W + 0.5),
         '\\draw[ink!85, line width=0.7pt, -{Stealth[length=2.4mm]}] (0,0) -- (0,%.3f);' % (H + 0.4)]
    for i, f in enumerate(fs):
        o.append('\\draw[draw=%s, fill=%s, line width=0.6pt] (%.3f,0) rectangle (%.3f,%.3f);' % (col('046b4d'), col('86e0bd'), i * bw, (i + 1) * bw, f * sy))
        lbl = ('%s' % f) if not pct else (('%g' % f).replace('.', '{,}') if vi else '%g' % f) + '\\%'
        o.append('\\node[font=\\small, text=ink, above] at (%.3f,%.3f) {$%s$};' % ((i + 0.5) * bw, f * sy, lbl))
    for i, e in enumerate(edges):
        o.append('\\draw[ink!70] (%.3f,0) -- (%.3f,-0.08) node[below, font=\\small, text=ink] {$%s$};' % (i * bw, i * bw, e))
    v = step
    while v <= top:
        o.append('\\draw[ink!70] (0,%.3f) -- (-0.08,%.3f) node[left, font=\\small, text=ink] {$%s$};' % (v * sy, v * sy, v)); v += step
    o.append('\\node[font=\\small, text=ink, anchor=north east] at (%.3f,-0.55) {%s};' % (W + 0.5, xlab))
    o.append('\\node[font=\\small, text=ink, anchor=south west] at (0.12,%.3f) {%s};' % (H + 0.4, ylab))
    return texsvg('\\begin{tikzpicture}\n' + '\n'.join(o) + '\n\\end{tikzpicture}')
