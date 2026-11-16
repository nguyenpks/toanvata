# -*- coding: utf-8 -*-
"""Hiệu chỉnh lớp 10 – đợt 14/11/2026: Bài 7–11 (vectơ). Mỗi mức 18 câu: giữ 7 câu A–C cũ, thêm 2 câu A + 1 câu B có hình,
phần D mới 8 câu (8 DẠNG khác nhau, khác các dạng ở A–C), phần lớn câu mới có hình vẽ (TikZ → SVG, nhãn tự tránh nét vẽ).
Mỗi hàm sinh (r, lv, ctx) → dict như sp_g12r4 (opts[0] đúng; truth; key; fig = (html_en, html_vi)).
Kiểm tra độc lập: tools/audit_g10r.py."""
import math, random
from fractions import Fraction as F
from sp_g11r import tx, ne, nv, nopt, nopts, key
from sp_g11r2 import V, frt, fo
from sp_g12r4 import build, old_sets, M, tt
import fig2d as G
from fig2d import Canvas, lw
from mb_pgf import col

def ov(p, q): return '\\overrightarrow{%s%s}' % (p, q)
def OV(p, q): return M(ov(p, q))
def vsub(a, b): return (a[0] - b[0], a[1] - b[1])
def vadd(a, b): return (a[0] + b[0], a[1] + b[1])
def smul(k, a): return (k * a[0], k * a[1])
def vdot(a, b): return a[0] * b[0] + a[1] * b[1]
def P2(p): return '(%s;\\,%s)' % (frt(p[0]), frt(p[1]))
def sqt(n):
    """√n rút gọn (n nguyên ≥ 0) → TeX."""
    n = int(n); a, b = 1, n; k = 2
    while k * k <= b:
        while b % (k * k) == 0: b //= k * k; a *= k
        k += 1
    if b == 1: return str(a)
    return ('' if a == 1 else str(a)) + '\\sqrt{%d}' % b
def ksq(c, n):
    """c·√n với c nguyên dương."""
    s = sqt(n)
    if '\\sqrt' not in s: return str(c * int(s))
    a = s.split('\\sqrt')[0]; a = int(a) if a else 1
    return ('' if c * a == 1 else str(c * a)) + '\\sqrt' + s.split('\\sqrt')[1]

GREEN, ORANGE, BLUE, INK = '046b4d', 'c2410c', '1d4ed8', '123428'
ARW = 'color=%s, line width=1.2pt, -{Stealth[length=2.8mm]}'
AROUND = [(0.3, 0.3), (-0.3, 0.3), (0.3, -0.3), (-0.3, -0.3), (0.4, 0), (-0.4, 0), (0, 0.36), (0, -0.36)]

def PF(P, segs=(), vecs=(), dashed=(), right=(), marks=(), size=4.6, px=300, alt='Figure', vlabels=(), hide=()):
    """Hình phẳng: P = {tên: (x, y)} (tên bắt đầu bằng '_' không ghi nhãn); segs: đoạn thẳng; vecs: [(A, B, màu)] mũi tên;
    dashed: đoạn nét đứt; right: [(A, O, B)] kí hiệu góc vuông tại O; marks: [(x, y, tex)] nhãn tự do; vlabels: [(A, B, tex)] tên vectơ."""
    xs = [p[0] for p in P.values()]; ys = [p[1] for p in P.values()]
    s = size / max(max(xs) - min(xs), max(ys) - min(ys), 1e-9); x0, y0 = min(xs), min(ys)
    T = lambda p: ((p[0] - x0) * s, (p[1] - y0) * s)
    Q = {k: T(v) for k, v in P.items()}
    c = Canvas()
    for a, b in segs: c.poly([Q[a], Q[b]], 'ink, line width=0.9pt')
    for a, b in dashed: c.poly([Q[a], Q[b]], 'ink, line width=0.7pt, dash pattern=on 3pt off 2pt')
    for a, b, k in vecs: c.poly([Q[a], Q[b]], ARW % col(k))
    for a, o, b in right:
        A, O_, B = Q[a], Q[o], Q[b]; r = 0.28
        u = vsub(A, O_); L = math.hypot(*u); u = (u[0] / L * r, u[1] / L * r)
        v = vsub(B, O_); L = math.hypot(*v); v = (v[0] / L * r, v[1] / L * r)
        c.poly([vadd(O_, u), vadd(vadd(O_, u), v), vadd(O_, v)], 'ink, line width=0.6pt')
    for k, p in Q.items():
        if not k.startswith('_') and k not in hide: c.dot(*p, color=INK)
    for k, p in Q.items():
        if k.startswith('_') or k in hide: continue
        w, h = lw(k); c.label(p[0], p[1], '$%s$' % k.replace("'", "'"), w, h, AROUND)
    for a, b, t in vlabels:
        A, B = Q[a], Q[b]; m = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2); d = vsub(B, A); L = math.hypot(*d); n = (-d[1] / L * 0.32, d[0] / L * 0.32)
        w, h = lw(t); c.label(m[0], m[1], '$%s$' % t, w, h, [n, (-n[0], -n[1]), (n[0] * 1.5, n[1] * 1.5), (-n[0] * 1.5, -n[1] * 1.5)], white=True)
    for x, y, t in marks:
        X, Y = T((x, y)); w, h = lw(t); c.label(X, Y, '$%s$' % t, w, h, [(0, 0), (0.15, 0.15), (-0.15, 0.15)])
    fn = c.svg(); return (G.img(fn, alt, px), G.img(fn, alt, px))

def GRID(xr, yr, pts=None, vecs=(), axes=True, px=None, alt='Grid figure', unit=0.42):
    """Lưới ô vuông (mỗi ô 1 đơn vị). pts: {tên: (x, y)}; vecs: [((x1, y1), (x2, y2), tex nhãn, màu)]. axes: vẽ Ox, Oy và số 1 trên mỗi trục.
    Độ rộng ảnh tỉ lệ với số ô để chữ có cùng cỡ ở mọi hình."""
    (a, b), (c0, d) = xr, yr
    while b - a < 7: b += 1; a -= 1 if b - a < 7 else 0
    while d - c0 < 6: d += 1; c0 -= 1 if d - c0 < 6 else 0
    u = unit; X = lambda x: (x - a) * u; Y = lambda y: (y - c0) * u
    if px is None: px = int(max(170, min(380, 26 * (b - a + 2))))
    c = Canvas()
    for x in range(a, b + 1): c.o.append('\\draw[ink!14, line width=0.4pt] (%.3f,%.3f) -- (%.3f,%.3f);' % (X(x), Y(c0), X(x), Y(d)))
    for y in range(c0, d + 1): c.o.append('\\draw[ink!14, line width=0.4pt] (%.3f,%.3f) -- (%.3f,%.3f);' % (X(a), Y(y), X(b), Y(y)))
    if axes:
        c.poly([(X(a), Y(0)), (X(b) + 0.3, Y(0))], 'ink!85, line width=0.7pt, -{Stealth[length=2.2mm]}')
        c.poly([(X(0), Y(c0)), (X(0), Y(d) + 0.3)], 'ink!85, line width=0.7pt, -{Stealth[length=2.2mm]}')
        c.o.append('\\node[font=\\small, text=ink] at (%.3f,%.3f) {$x$};' % (X(b) + 0.3, Y(0) - 0.25)); c.boxes.append((X(b) + 0.1, Y(0) - 0.45, X(b) + 0.5, Y(0) - 0.05))
        c.o.append('\\node[font=\\small, text=ink] at (%.3f,%.3f) {$y$};' % (X(0) - 0.25, Y(d) + 0.3)); c.boxes.append((X(0) - 0.45, Y(d) + 0.1, X(0) - 0.05, Y(d) + 0.5))
    for p, q, t, k in vecs:
        c.poly([(X(p[0]), Y(p[1])), (X(q[0]), Y(q[1]))], ARW % col(k))
    for k_, p in (pts or {}).items(): c.dot(X(p[0]), Y(p[1]), color=INK)
    _all = [(X(q[0]), Y(q[1])) for q in (pts or {}).values()]
    for k_, p in (pts or {}).items():
        w, h = lw(k_); px_, py_ = X(p[0]), Y(p[1])
        def _sc(o):   # nhãn phải gần điểm của nó hơn hẳn mọi điểm khác (tránh đọc nhầm nhãn)
            L = (px_ + o[0], py_ + o[1]); own = math.hypot(o[0], o[1])
            oth = min([math.hypot(L[0] - a, L[1] - b) for a, b in _all if (a, b) != (px_, py_)] or [9])
            return oth - own
        cand = sorted(AROUND, key=lambda o: -min(_sc(o), 0.25))
        c.label(px_, py_, '$%s$' % k_, w, h, cand, white=True)
    for p, q, t, k in vecs:
        if not t: continue
        A, B = (X(p[0]), Y(p[1])), (X(q[0]), Y(q[1])); m = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2); dd = vsub(B, A); L = math.hypot(*dd); n = (-dd[1] / L * 0.3, dd[0] / L * 0.3)
        w, h = lw(t); c.label(m[0], m[1], '$%s$' % t, w, h, [n, (-n[0], -n[1]), (n[0] * 1.6, n[1] * 1.6), (-n[0] * 1.6, -n[1] * 1.6)], white=True)
    if axes:
        c.label(X(0), Y(0), '$O$', 0.3, 0.36, [(-0.2, -0.22), (-0.22, 0.2), (0.2, -0.22), (0.22, 0.22)], white=True)
        c.label(X(1), Y(0), '$1$', 0.22, 0.32, [(0, -0.22), (0, 0.22), (0.15, -0.22)], white=True)
        c.label(X(0), Y(1), '$1$', 0.22, 0.32, [(-0.2, 0), (0.2, 0), (-0.2, 0.15)], white=True)
    fn = c.svg(); return (G.img(fn, alt, px), G.img(fn, alt, px))

def lay(vs, names, color, first=None):
    """Đặt mỗi vectơ vào một ô 4×4 riêng (không chồng nhau). vs: [(dx, dy)]; first: (vectơ, tên, màu) đặt ở ô đầu."""
    out = []; items = ([first] if first else []) + [(v, n, color) for v, n in zip(vs, names)]
    for i, (v, n, k) in enumerate(items):
        cx, cy = (i % 3) * 7, -(i // 3) * 6
        st = (cx + max(0, -v[0]), cy + max(0, -v[1])); out.append((st, (st[0] + v[0], st[1] + v[1]), n, k))
    return out
def GRIDV(vecs, alt):
    xs = [p for e in vecs for p in (e[0][0], e[1][0])]; ys = [p for e in vecs for p in (e[0][1], e[1][1])]
    return GRID((min(xs) - 1, max(xs) + 1), (min(ys) - 1, max(ys) + 1), vecs=vecs, axes=False, alt=alt)

def eqset(P, pair, names):
    """Các vectơ (khác pair) có hai đầu trong names và bằng vectơ pair."""
    d = vsub(P[pair[1]], P[pair[0]])
    return [(a, b) for a in names for b in names if a != b and (a, b) != tuple(pair) and vsub(P[b], P[a]) == d]

# ====================================================================== BÀI 7 – Các khái niệm mở đầu
TRI = {'A': (F(1), F(4)), 'B': (F(0), F(0)), 'C': (F(6), F(0))}
def tri_mid():
    P = dict(TRI); P['M'] = tuple((x + y) / 2 for x, y in zip(P['A'], P['B'])); P['N'] = tuple((x + y) / 2 for x, y in zip(P['A'], P['C'])); P['P'] = tuple((x + y) / 2 for x, y in zip(P['B'], P['C']))
    return P
TRIFIG = None
def fig_tri_mid(extra=None):
    P = {k: (float(v[0]), float(v[1])) for k, v in tri_mid().items()}
    if extra: P.update(extra)
    return PF(P, segs=[('A', 'B'), ('B', 'C'), ('C', 'A'), ('M', 'N'), ('N', 'P'), ('P', 'M')], alt='Triangle ABC with the midpoints M, N, P of AB, AC, BC')

def v7_mid_equal(r, lv, ctx):
    P = tri_mid(); names = list('ABCMNP')
    tg = r.choice([('M', 'N'), ('N', 'P'), ('M', 'P'), ('N', 'M'), ('P', 'N')]); eq = eqset(P, tg, names)
    eq = [e for e in eq if len(e) == 2]; good = r.choice(eq)
    d = vsub(P[tg[1]], P[tg[0]])
    bad = [(b, a) for a, b in eq] + [(a, b) for a in names for b in names if a != b and vsub(P[b], P[a]) != d and abs(vsub(P[b], P[a])[0]) + abs(vsub(P[b], P[a])[1]) > 0]
    bad = [x for x in bad if vsub(P[x[1]], P[x[0]]) != d]; r.shuffle(bad); bad.sort(key=lambda x: 0 if vsub(P[x[1]], P[x[0]]) == smul(-1, d) else 1)
    opts = [OV(*good)] + [OV(*x) for x in bad[:3]]
    qe = V(lv, ['\\(M\\), \\(N\\), \\(P\\) are the midpoints of \\(AB\\), \\(AC\\), \\(BC\\) (figure). Which vector is equal to \\(%s\\)?', 'In the figure, \\(M\\), \\(N\\), \\(P\\) are the midpoints of the sides of triangle \\(ABC\\). The vector equal to \\(%s\\) is…', 'Look at the figure (\\(M\\), \\(N\\), \\(P\\): midpoints of \\(AB\\), \\(AC\\), \\(BC\\)). Choose the vector that equals \\(%s\\).'])
    qv = V(lv, ['\\(M\\), \\(N\\), \\(P\\) lần lượt là trung điểm của \\(AB\\), \\(AC\\), \\(BC\\) (hình vẽ). Vectơ nào bằng \\(%s\\)?', 'Trong hình, \\(M\\), \\(N\\), \\(P\\) là trung điểm các cạnh của tam giác \\(ABC\\). Vectơ bằng \\(%s\\) là…', 'Quan sát hình (\\(M\\), \\(N\\), \\(P\\) là trung điểm của \\(AB\\), \\(AC\\), \\(BC\\)). Chọn vectơ bằng \\(%s\\).'])
    return dict(en=qe % ov(*tg), vi=qv % ov(*tg), opts=opts, fig=fig_tri_mid(),
                ee='The midline is parallel to the third side and half as long; \\(%s\\) has the same direction and length as \\(%s\\).' % (ov(*good), ov(*tg)),
                ev='Đường trung bình song song và bằng nửa cạnh thứ ba; \\(%s\\) cùng hướng, cùng độ dài với \\(%s\\).' % (ov(*good), ov(*tg)))

DIRS = [(2, 1), (1, 2), (2, -1), (3, 0), (0, 2), (1, -2), (-2, 1)]
def v7_grid_dir(r, lv, ctx):
    a = r.choice(DIRS); kinds = [1, 2, -1, F(1, 1)]
    for _ in range(200):
        ks = [r.choice([1, 2, -1, -2, None, None]) for _ in range(4)]
        vs = []
        for k in ks:
            if k is None:
                d = r.choice([x for x in DIRS if x[0] * a[1] != x[1] * a[0]]); vs.append(d)
            else: vs.append(smul(k, a))
        cnt = {'same': sum(1 for k in ks if k is not None and k > 0), 'col': sum(1 for k in ks if k is not None), 'eq': sum(1 for k in ks if k == 1)}
        what = ['same', 'col', 'eq'][(lv - 1) % 3]
        if 0 <= cnt[what] <= 3 and len(set(vs)) == 4: break
    names = ['\\vec b', '\\vec c', '\\vec d', '\\vec e']
    fig = GRIDV(lay(vs, names, GREEN, (a, '\\vec a', ORANGE)), 'Vectors drawn on a square grid')
    good = cnt[what]
    W = {'same': ('have the same direction as', 'cùng hướng với'), 'col': ('are collinear with', 'cùng phương với'), 'eq': ('are equal to', 'bằng')}[what]
    return dict(en='Among the vectors \\(\\vec b\\), \\(\\vec c\\), \\(\\vec d\\), \\(\\vec e\\) in the figure, how many %s \\(\\vec a\\)?' % W[0],
                vi='Trong các vectơ \\(\\vec b\\), \\(\\vec c\\), \\(\\vec d\\), \\(\\vec e\\) ở hình bên, có bao nhiêu vectơ %s \\(\\vec a\\)?' % W[1],
                opts=nopts(r, good, [good + 1, good - 1 if good else 4, cnt['col'] if what != 'col' else cnt['same'], 4]), fig=fig,
                ee='Count the arrows that are parallel to \\(\\vec a\\)%s: %d.' % ({'same': ' and point the same way', 'col': '', 'eq': ', point the same way and have the same length'}[what], good),
                ev='Đếm các mũi tên song song với \\(\\vec a\\)%s: %d.' % ({'same': ' và chỉ cùng phía', 'col': '', 'eq': ', chỉ cùng phía và cùng độ dài'}[what], good))

RECT = {'A': (0, 0), 'B': (5, 0), 'C': (5, 3), 'D': (0, 3), 'O': (2.5, 1.5)}
R7 = [(('\\(\\overrightarrow{OA}\\) and \\(\\overrightarrow{OC}\\) are opposite vectors.', '\\(\\overrightarrow{OA}\\) và \\(\\overrightarrow{OC}\\) là hai vectơ đối nhau.'), True, ('\\(O\\) is the midpoint of \\(AC\\).', '\\(O\\) là trung điểm của \\(AC\\).')),
      (('\\(\\overrightarrow{AC}=\\overrightarrow{BD}\\).', '\\(\\overrightarrow{AC}=\\overrightarrow{BD}\\).'), False, ('Same length but not the same direction.', 'Cùng độ dài nhưng không cùng hướng.')),
      (('\\(|\\overrightarrow{OA}|=|\\overrightarrow{OB}|\\).', '\\(|\\overrightarrow{OA}|=|\\overrightarrow{OB}|\\).'), True, ('The diagonals of a rectangle are equal and bisect each other.', 'Hai đường chéo của hình chữ nhật bằng nhau và cắt nhau tại trung điểm mỗi đường.')),
      (('\\(\\overrightarrow{AB}\\) and \\(\\overrightarrow{CD}\\) have the same direction.', '\\(\\overrightarrow{AB}\\) và \\(\\overrightarrow{CD}\\) cùng hướng.'), False, ('They are opposite: \\(\\overrightarrow{CD}=\\overrightarrow{BA}\\).', 'Chúng ngược hướng: \\(\\overrightarrow{CD}=\\overrightarrow{BA}\\).')),
      (('\\(\\overrightarrow{AO}=\\overrightarrow{OC}\\).', '\\(\\overrightarrow{AO}=\\overrightarrow{OC}\\).'), True, ('Same direction and \\(AO=OC\\).', 'Cùng hướng và \\(AO=OC\\).')),
      (('\\(\\overrightarrow{DA}\\) and \\(\\overrightarrow{BC}\\) are equal vectors.', '\\(\\overrightarrow{DA}\\) và \\(\\overrightarrow{BC}\\) là hai vectơ bằng nhau.'), False, ('They have opposite directions.', 'Chúng ngược hướng.'))]
def v7_tf_rect(r, lv, ctx):
    (e, v), truth, (ee, ev) = R7[(lv - 1) % 3 * 2 + r.randrange(2)]
    return dict(en='\\(ABCD\\) is a rectangle with center \\(O\\) (figure). ' + e, vi='Cho hình chữ nhật \\(ABCD\\) tâm \\(O\\) (hình vẽ). ' + v, truth=truth,
                fig=PF(RECT, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('A', 'C'), ('B', 'D')], right=[('B', 'A', 'D')], alt='Rectangle ABCD with center O'), ee=ee, ev=ev)

# ---- D, Bài 7
TWO = {'A': (0, 0), 'B': (2.4, 0), 'C': (4.8, 0), 'D': (1, 1.8), 'E': (3.4, 1.8), 'F': (5.8, 1.8)}
def v7_d_count(r, lv, ctx):
    tg = [('A', 'B'), ('A', 'D'), ('A', 'E')][(lv - 1) % 3]; eq = eqset(TWO, tg, list('ABCDEF')); good = len(eq)
    return dict(en='The figure shows two equal parallelograms \\(ABED\\) and \\(BCFE\\). How many vectors, other than \\(%s\\), with both ends among the six points are equal to \\(%s\\)?' % (ov(*tg), ov(*tg)),
                vi='Hình vẽ gồm hai hình bình hành bằng nhau \\(ABED\\) và \\(BCFE\\). Có bao nhiêu vectơ khác \\(%s\\), có hai đầu mút là hai trong sáu điểm, bằng \\(%s\\)?' % (ov(*tg), ov(*tg)),
                opts=nopts(r, good, [good + 1, 2 * good + 1, good + 3, 0]), fig=PF(TWO, segs=[('A', 'C'), ('D', 'F'), ('A', 'D'), ('B', 'E'), ('C', 'F')], alt='Two parallelograms side by side'),
                ee='Equal vectors: %s.' % ', '.join('\\(%s\\)' % ov(*x) for x in eq), ev='Các vectơ bằng nhau: %s.' % ', '.join('\\(%s\\)' % ov(*x) for x in eq))

def v7_d_rhombus(r, lv, ctx):
    a = r.choice([2, 3, 4, 5, 6, 8]); ang = [60, 120, 60][(lv - 1) % 3]; tgt = ['AC', 'AC', 'BD'][(lv - 1) % 3]
    short, long_ = M(str(a)), M(ksq(a, 3))
    good = long_ if (ang == 60) == (tgt == 'AC') else short
    t = math.radians(ang); P = {'A': (0, 0), 'B': (3, 0), 'D': (3 * math.cos(t), 3 * math.sin(t))}; P['C'] = vadd(P['B'], P['D'])
    opts = [good] + [x for x in [short, long_, M(str(2 * a)), M(ksq(a, 2))] if x != good][:3]
    return dict(en='\\(ABCD\\) is a rhombus with side \\(%d\\) and \\(\\widehat{BAD}=%d^\\circ\\) (figure). Then \\(|%s|=\\)…' % (a, ang, ov(*tgt)), vi='Hình thoi \\(ABCD\\) cạnh \\(%d\\) có \\(\\widehat{BAD}=%d^\\circ\\) (hình vẽ). Khi đó \\(|%s|=\\)…' % (a, ang, ov(*tgt)),
                opts=opts, fig=PF(P, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('A', 'C'), ('B', 'D')], alt='Rhombus ABCD', marks=[(0.95 * math.cos(math.radians(ang * 3 / 4 + 0)), 0.95 * math.sin(math.radians(ang * 3 / 4)), '%d^\\circ' % ang)]),
                ee='With \\(\\widehat{BAD}=%d^\\circ\\), triangle %s is equilateral; the other diagonal is \\(%s\\).' % (ang, 'ABD' if ang == 60 else 'ABC', ksq(a, 3)), ev='Vì \\(\\widehat{BAD}=%d^\\circ\\) nên tam giác %s đều; đường chéo còn lại bằng \\(%s\\).' % (ang, 'ABD' if ang == 60 else 'ABC', ksq(a, 3)))

E7 = [(('Since \\(|\\overrightarrow{AB}|=|\\overrightarrow{CD}|\\), we get \\(\\overrightarrow{AB}=\\overrightarrow{CD}\\).', 'Vì \\(|\\overrightarrow{AB}|=|\\overrightarrow{CD}|\\) nên \\(\\overrightarrow{AB}=\\overrightarrow{CD}\\).'),
       ('Wrong: equal vectors also need the same direction.', 'Sai: hai vectơ bằng nhau còn phải cùng hướng.')),
      (('Since \\(\\overrightarrow{AB}\\) and \\(\\overrightarrow{CD}\\) are collinear, they have the same direction.', 'Vì \\(\\overrightarrow{AB}\\) và \\(\\overrightarrow{CD}\\) cùng phương nên chúng cùng hướng.'),
       ('Wrong: collinear vectors may have opposite directions.', 'Sai: hai vectơ cùng phương có thể ngược hướng.')),
      (('Since \\(\\overrightarrow{AB}=\\overrightarrow{DC}\\), the four points \\(A\\), \\(B\\), \\(C\\), \\(D\\) always form a parallelogram.', 'Vì \\(\\overrightarrow{AB}=\\overrightarrow{DC}\\) nên bốn điểm \\(A\\), \\(B\\), \\(C\\), \\(D\\) luôn tạo thành hình bình hành.'),
       ('Wrong: the four points may lie on one line.', 'Sai: bốn điểm có thể cùng nằm trên một đường thẳng.'))]
def v7_d_error(r, lv, ctx):
    (e, v), good = E7[(lv - 1) % 3]
    O = [good, ('The reasoning is correct.', 'Lập luận đúng.'), ('Wrong: the conclusion holds only for a square.', 'Sai: kết luận chỉ đúng với hình vuông.'), ('Wrong: vectors can never be compared.', 'Sai: không thể so sánh hai vectơ.')]
    return dict(en='A student wrote: "%s" Which comment is correct?' % e, vi='Một bạn viết: "%s" Nhận xét nào đúng?' % v, opts=[tt(*x) for x in O], ee=good[0], ev=good[1])

Z7 = [(('The zero vector has the same direction as every vector.', 'Vectơ-không cùng hướng với mọi vectơ.'), ('The zero vector has length 1.', 'Vectơ-không có độ dài bằng 1.'), ('\\(\\overrightarrow{AA}\\) and \\(\\overrightarrow{BB}\\) are different vectors.', '\\(\\overrightarrow{AA}\\) và \\(\\overrightarrow{BB}\\) là hai vectơ khác nhau.'), ('The zero vector is collinear with no vector.', 'Vectơ-không không cùng phương với vectơ nào.')),
      (('\\(\\overrightarrow{MM}=\\overrightarrow{NN}=\\vec0\\) for all points \\(M\\), \\(N\\).', '\\(\\overrightarrow{MM}=\\overrightarrow{NN}=\\vec0\\) với mọi điểm \\(M\\), \\(N\\).'), ('\\(|\\vec0|=1\\).', '\\(|\\vec0|=1\\).'), ('\\(\\vec0\\) has no length.', '\\(\\vec0\\) không có độ dài.'), ('If \\(|\\overrightarrow{AB}|=0\\) then \\(A\\ne B\\).', 'Nếu \\(|\\overrightarrow{AB}|=0\\) thì \\(A\\ne B\\).')),
      (('\\(|\\overrightarrow{AB}|=0\\) exactly when \\(A\\equiv B\\).', '\\(|\\overrightarrow{AB}|=0\\) khi và chỉ khi \\(A\\equiv B\\).'), ('The zero vector has the opposite direction to every vector only.', 'Vectơ-không chỉ ngược hướng với mọi vectơ.'), ('\\(\\overrightarrow{AA}\\) has length \\(2\\).', '\\(\\overrightarrow{AA}\\) có độ dài bằng \\(2\\).'), ('A zero vector needs two different points.', 'Vectơ-không cần hai điểm phân biệt.'))]
def v7_d_zero(r, lv, ctx):
    S = Z7[(lv - 1) % 3]
    qe = V(lv, ['Which statement about the zero vector is correct?', 'Choose the true statement.', 'Which of the following is true?'])
    qv = V(lv, ['Khẳng định nào về vectơ-không là đúng?', 'Chọn khẳng định đúng.', 'Khẳng định nào sau đây đúng?'])
    return dict(en=qe, vi=qv, opts=[tt(*x) for x in S], ee='A zero vector has equal start and end points; it has length 0 and is collinear with (and has the same direction as) every vector.',
                ev='Vectơ-không có điểm đầu trùng điểm cuối, độ dài bằng 0, cùng phương và cùng hướng với mọi vectơ.')

O7 = [(('Car X drives east at \\(60\\) km/h and car Y drives west at \\(v\\) km/h on the same straight road.', 'Xe X chạy về hướng đông với vận tốc \\(60\\) km/h, xe Y chạy về hướng tây với vận tốc \\(v\\) km/h trên cùng một đường thẳng.'), 60, 'km/h'),
      (('One lift goes up at \\(3\\) m/s while another goes down at \\(v\\) m/s.', 'Một thang máy đi lên với vận tốc \\(3\\) m/s, thang máy khác đi xuống với vận tốc \\(v\\) m/s.'), 3, 'm/s'),
      (('A boat moves north at \\(15\\) km/h; a second boat moves south at \\(v\\) km/h.', 'Một ca nô đi về hướng bắc với vận tốc \\(15\\) km/h; ca nô thứ hai đi về hướng nam với vận tốc \\(v\\) km/h.'), 15, 'km/h')]
def v7_d_opposite(r, lv, ctx):
    (e, v), s, u = O7[(lv - 1) % 3]
    O = [('exactly when \\(v=%d\\)' % s, 'khi và chỉ khi \\(v=%d\\)' % s), ('for every \\(v\\gt0\\)', 'với mọi \\(v\\gt0\\)'), ('never, because they move on different sides', 'không bao giờ, vì chúng ở hai phía khác nhau'), ('exactly when \\(v=0\\)', 'khi và chỉ khi \\(v=0\\)')]
    if lv == 1: H = {'_s1': (0, 0), '_e1': (2.6, 0), '_s2': (3.2, 1), '_e2': (0.6, 1)}; W_ = 210
    else: H = {'_s1': (0, 0), '_e1': (0, 2.4), '_s2': (2.0, 2.4), '_e2': (2.0, 0)}; W_ = 230   # thang máy, ca nô: phương thẳng đứng
    fig = PF(H, vecs=[('_s1', '_e1', ORANGE), ('_s2', '_e2', BLUE)], vlabels=[('_s1', '_e1', '\\vec v_1'), ('_s2', '_e2', '\\vec v_2')], size=3.2, px=W_, alt='Two velocity vectors with opposite directions')
    return dict(en='%s Their velocity vectors are opposite vectors…' % e, vi='%s Hai vectơ vận tốc là hai vectơ đối nhau…' % v, opts=[tt(*x) for x in O], fig=fig,
                ee='They already have opposite directions; opposite vectors also need equal lengths: \\(v=%d\\).' % s, ev='Hai vectơ đã ngược hướng; vectơ đối còn cần cùng độ dài: \\(v=%d\\).' % s)

PYT = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15), (12, 16, 20), (7, 24, 25)]
def v7_d_median(r, lv, ctx):
    p, q, h = r.choice(PYT); good = F(h, 2)
    P = {'A': (0, 0), 'B': (0, 3), 'C': (4, 0)}; P['M'] = (2, 1.5)
    return dict(en='Triangle \\(ABC\\) is right-angled at \\(A\\) with \\(AB=%d\\), \\(AC=%d\\); \\(M\\) is the midpoint of \\(BC\\) (figure). Then \\(|\\overrightarrow{AM}|=\\)…' % (p, q),
                vi='Tam giác \\(ABC\\) vuông tại \\(A\\) có \\(AB=%d\\), \\(AC=%d\\); \\(M\\) là trung điểm của \\(BC\\) (hình vẽ). Khi đó \\(|\\overrightarrow{AM}|=\\)…' % (p, q),
                opts=nopts(r, good, [h, F(p + q, 2), F(p, 2), F(q, 2)]), fig=PF(P, segs=[('A', 'B'), ('B', 'C'), ('C', 'A')], vecs=[('A', 'M', ORANGE)], right=[('B', 'A', 'C')], alt='Right triangle with the median AM'),
                ee='\\(BC=\\sqrt{%d^2+%d^2}=%d\\); the median to the hypotenuse is half of it: \\(%s\\).' % (p, q, h, ne(good)), ev='\\(BC=\\sqrt{%d^2+%d^2}=%d\\); trung tuyến ứng với cạnh huyền bằng nửa cạnh huyền: \\(%s\\).' % (p, q, h, nv(good)))

PG = {'A': (0, 0), 'B': (4, 0), 'C': (5.2, 2.6), 'D': (1.2, 2.6)}
PT7 = [(('A', 'M'), ('D', 'C'), 'B'), (('B', 'M'), ('A', 'D'), 'C'), (('M', 'C'), ('A', 'B'), 'D'), (('D', 'M'), ('A', 'B'), 'C'), (('M', 'A'), ('C', 'D'), 'B'), (('M', 'D'), ('B', 'C'), 'A')]
def v7_d_point(r, lv, ctx):
    (s, t), (u, w), good = PT7[(lv - 1) * 2 + r.randrange(2)]
    lhs = ov(s, t)
    others = [x for x in 'ABCD' if x != good]
    opts = [tt('\\(M\\equiv %s\\)' % good, '\\(M\\equiv %s\\)' % good)] + [tt('\\(M\\equiv %s\\)' % x, '\\(M\\equiv %s\\)' % x) for x in others[:2]] + [tt('\\(M\\) is the midpoint of \\(AC\\)', '\\(M\\) là trung điểm của \\(AC\\)')]
    return dict(en='\\(ABCD\\) is a parallelogram (figure). The point \\(M\\) satisfies \\(%s=%s\\). Then…' % (lhs, ov(u, w)), vi='Cho hình bình hành \\(ABCD\\) (hình vẽ). Điểm \\(M\\) thỏa mãn \\(%s=%s\\). Khi đó…' % (lhs, ov(u, w)),
                opts=opts, fig=PF(PG, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')], alt='Parallelogram ABCD'),
                ee='In the parallelogram the opposite sides give equal vectors, so \\(M\\equiv %s\\).' % good, ev='Trong hình bình hành các cặp cạnh đối cho các vectơ bằng nhau nên \\(M\\equiv %s\\).' % good)

def v7_d_collinear(r, lv, ctx):
    S = [('the vectors \\(\\overrightarrow{AB}\\) and \\(\\overrightarrow{AC}\\) are collinear', 'hai vectơ \\(\\overrightarrow{AB}\\) và \\(\\overrightarrow{AC}\\) cùng phương'),
         ('the vectors \\(\\overrightarrow{AB}\\) and \\(\\overrightarrow{AC}\\) have the same direction', 'hai vectơ \\(\\overrightarrow{AB}\\) và \\(\\overrightarrow{AC}\\) cùng hướng'),
         ('\\(|\\overrightarrow{AB}|=|\\overrightarrow{AC}|\\)', '\\(|\\overrightarrow{AB}|=|\\overrightarrow{AC}|\\)'), ('\\(\\overrightarrow{AB}=\\overrightarrow{CA}\\)', '\\(\\overrightarrow{AB}=\\overrightarrow{CA}\\)')]
    qe = V(lv, ['Three different points \\(A\\), \\(B\\), \\(C\\) lie on one line exactly when…', 'Three distinct points \\(A\\), \\(B\\), \\(C\\) are collinear if and only if…', 'For distinct points \\(A\\), \\(B\\), \\(C\\), which condition means they lie on a line?'])
    qv = V(lv, ['Ba điểm phân biệt \\(A\\), \\(B\\), \\(C\\) thẳng hàng khi và chỉ khi…', 'Ba điểm phân biệt \\(A\\), \\(B\\), \\(C\\) thẳng hàng khi và chỉ khi điều kiện nào xảy ra?', 'Với ba điểm phân biệt \\(A\\), \\(B\\), \\(C\\), điều kiện nào cho biết chúng thẳng hàng?'])
    return dict(en=qe, vi=qv, opts=[tt(*x) for x in S], ee='Collinear is enough; the directions may be the same or opposite (\\(A\\) may lie between \\(B\\) and \\(C\\)).',
                ev='Chỉ cần cùng phương; hai vectơ có thể cùng hướng hoặc ngược hướng (\\(A\\) có thể nằm giữa \\(B\\) và \\(C\\)).')

B7 = dict(A=[v7_mid_equal, v7_grid_dir], B=[v7_tf_rect], C=[], D=[v7_d_count, v7_d_rhombus, v7_d_error, v7_d_zero, v7_d_opposite, v7_d_median, v7_d_point, v7_d_collinear])

# ====================================================================== BÀI 8 – Tổng và hiệu của hai vectơ
PAIRS = [((2, 1), (1, 2)), ((3, 0), (1, 2)), ((2, -1), (1, 3)), ((1, 2), (3, -1)), ((2, 2), (2, -1)), ((0, 3), (2, 1))]
def s8_grid_sum(r, lv, ctx):
    a, b = r.choice(PAIRS); op = ['+', '+', '-'][(lv - 1) % 3]; g = vadd(a, b) if op == '+' else vsub(a, b)
    cands = [g, vsub(b, a) if op == '+' else vadd(a, b), vsub(a, b) if op == '+' else vsub(b, a), (g[1], g[0]), (-g[0], -g[1]), (g[0] + 1, g[1])]
    seen = []
    for c in cands:
        if c not in seen and c != (0, 0) and c not in (a, b): seen.append(c)
    seen = seen[:4]
    if len(seen) < 4 or seen[0] != g: raise AssertionError
    names = ['\\vec x', '\\vec y', '\\vec z', '\\vec w']; idx = list(range(4)); r.shuffle(idx)
    order = [seen[i] for i in idx]
    L = lay([a, b] + order, ['\\vec a', '\\vec b'] + names, GREEN); L[0] = L[0][:3] + (ORANGE,); L[1] = L[1][:3] + (BLUE,)
    fig = GRIDV(L, 'Vectors a, b and four other vectors on a grid')
    good = names[order.index(g)]
    qe = V(lv, ['In the figure, which vector is equal to \\(\\vec a%s\\vec b\\)?', 'Using the grid, find the vector equal to \\(\\vec a%s\\vec b\\).', 'Which of the vectors drawn equals \\(\\vec a%s\\vec b\\)?'])
    qv = V(lv, ['Trong hình vẽ, vectơ nào bằng \\(\\vec a%s\\vec b\\)?', 'Dựa vào lưới ô vuông, tìm vectơ bằng \\(\\vec a%s\\vec b\\).', 'Trong các vectơ đã vẽ, vectơ nào bằng \\(\\vec a%s\\vec b\\)?'])
    return dict(en=qe % op, vi=qv % op,
                opts=[M(good)] + [M(n) for n in names if n != good], fig=fig,
                ee='Count the squares: \\(\\vec a%s\\vec b\\) moves %d square(s) horizontally and %d vertically (signs give the direction), exactly like \\(%s\\).' % (op, g[0], g[1], good), ev='Đếm ô: \\(\\vec a%s\\vec b\\) dịch %d ô theo phương ngang và %d ô theo phương dọc (dấu chỉ chiều), giống hệt \\(%s\\).' % (op, g[0], g[1], good))

MS8 = [(('A', 'M'), ('A', 'N'), ('A', 'P')), (('B', 'M'), ('B', 'P'), ('B', 'N')), (('C', 'N'), ('C', 'P'), ('C', 'M'))]
def s8_mid_rule(r, lv, ctx):
    u, w, good = MS8[(lv - 1) % 3]; P = tri_mid()
    s_ = vadd(vsub(P[u[1]], P[u[0]]), vsub(P[w[1]], P[w[0]])); assert s_ == vsub(P[good[1]], P[good[0]])
    names = list('ABCMNP'); cand = [(a, b) for a in names for b in names if a != b and vsub(P[b], P[a]) != s_]
    r.shuffle(cand); cand.sort(key=lambda x: 0 if x[0] == good[0] else 1)
    return dict(en='\\(M\\), \\(N\\), \\(P\\) are the midpoints of \\(AB\\), \\(AC\\), \\(BC\\) (figure). Then \\(%s+%s=\\)…' % (ov(*u), ov(*w)), vi='\\(M\\), \\(N\\), \\(P\\) là trung điểm của \\(AB\\), \\(AC\\), \\(BC\\) (hình vẽ). Khi đó \\(%s+%s=\\)…' % (ov(*u), ov(*w)),
                opts=[OV(*good)] + [OV(*x) for x in cand[:3]], fig=fig_tri_mid(),
                ee='\\(%s%s%s%s\\) is a parallelogram, so by the parallelogram rule the sum is the diagonal \\(%s\\).' % (u[0], u[1], good[1], w[1], ov(*good)),
                ev='\\(%s%s%s%s\\) là hình bình hành nên theo quy tắc hình bình hành tổng bằng vectơ đường chéo \\(%s\\).' % (u[0], u[1], good[1], w[1], ov(*good)))

CENT = {'A': (1.2, 4.2), 'B': (0, 0), 'C': (6, 0)}
CENT['G'] = (sum(p[0] for p in CENT.values()) / 3, sum(p[1] for p in CENT.values()) / 3)
CENT['I'] = (3, 0)
T8 = [(('\\(\\overrightarrow{GA}+\\overrightarrow{GB}+\\overrightarrow{GC}=\\vec0\\).', '\\(\\overrightarrow{GA}+\\overrightarrow{GB}+\\overrightarrow{GC}=\\vec0\\).'), True, ('Property of the centroid.', 'Tính chất trọng tâm tam giác.')),
      (('\\(\\overrightarrow{IB}+\\overrightarrow{IC}=\\overrightarrow{BC}\\).', '\\(\\overrightarrow{IB}+\\overrightarrow{IC}=\\overrightarrow{BC}\\).'), False, ('\\(I\\) is the midpoint of \\(BC\\): \\(\\overrightarrow{IB}+\\overrightarrow{IC}=\\vec0\\).', '\\(I\\) là trung điểm của \\(BC\\): \\(\\overrightarrow{IB}+\\overrightarrow{IC}=\\vec0\\).')),
      (('\\(\\overrightarrow{GB}+\\overrightarrow{GC}=\\overrightarrow{AG}\\).', '\\(\\overrightarrow{GB}+\\overrightarrow{GC}=\\overrightarrow{AG}\\).'), True, ('\\(\\overrightarrow{GB}+\\overrightarrow{GC}=-\\overrightarrow{GA}=\\overrightarrow{AG}\\).', '\\(\\overrightarrow{GB}+\\overrightarrow{GC}=-\\overrightarrow{GA}=\\overrightarrow{AG}\\).')),
      (('\\(\\overrightarrow{GA}+\\overrightarrow{GB}=\\overrightarrow{GC}\\).', '\\(\\overrightarrow{GA}+\\overrightarrow{GB}=\\overrightarrow{GC}\\).'), False, ('\\(\\overrightarrow{GA}+\\overrightarrow{GB}=-\\overrightarrow{GC}=\\overrightarrow{CG}\\).', '\\(\\overrightarrow{GA}+\\overrightarrow{GB}=-\\overrightarrow{GC}=\\overrightarrow{CG}\\).')),
      (('\\(\\overrightarrow{AB}-\\overrightarrow{AC}=\\overrightarrow{CB}\\).', '\\(\\overrightarrow{AB}-\\overrightarrow{AC}=\\overrightarrow{CB}\\).'), True, ('Difference rule: \\(\\overrightarrow{AB}-\\overrightarrow{AC}=\\overrightarrow{CB}\\).', 'Quy tắc hiệu: \\(\\overrightarrow{AB}-\\overrightarrow{AC}=\\overrightarrow{CB}\\).')),
      (('\\(\\overrightarrow{BA}+\\overrightarrow{AI}=\\overrightarrow{BC}\\).', '\\(\\overrightarrow{BA}+\\overrightarrow{AI}=\\overrightarrow{BC}\\).'), False, ('Chasles: \\(\\overrightarrow{BA}+\\overrightarrow{AI}=\\overrightarrow{BI}\\ne\\overrightarrow{BC}\\).', 'Quy tắc ba điểm: \\(\\overrightarrow{BA}+\\overrightarrow{AI}=\\overrightarrow{BI}\\ne\\overrightarrow{BC}\\).'))]
def fig_cent(): return PF(CENT, segs=[('A', 'B'), ('B', 'C'), ('C', 'A'), ('A', 'I')], dashed=[('B', 'G'), ('C', 'G')], alt='Triangle ABC with centroid G and the midpoint I of BC')
def s8_tf_cent(r, lv, ctx):
    (e, v), truth, (ee, ev) = T8[(lv - 1) % 3 * 2 + r.randrange(2)]
    return dict(en='\\(G\\) is the centroid of triangle \\(ABC\\) and \\(I\\) is the midpoint of \\(BC\\) (figure). ' + e, vi='\\(G\\) là trọng tâm tam giác \\(ABC\\), \\(I\\) là trung điểm của \\(BC\\) (hình vẽ). ' + v,
                truth=truth, fig=fig_cent(), ee=ee, ev=ev)

# ---- D, Bài 8
def s8_d_equil(r, lv, ctx):
    a = r.choice([2, 3, 4, 5, 6, 8]); k = (lv - 1) % 3
    expr, good = [('\\overrightarrow{AB}+\\overrightarrow{AC}', M(ksq(a, 3))), ('\\overrightarrow{AB}-\\overrightarrow{AC}', M(str(a))), ('\\overrightarrow{AB}+\\overrightarrow{AC}', M(ksq(a, 3)))][k]
    P = {'A': (0, 0), 'B': (4, 0), 'C': (2, 2 * math.sqrt(3))}
    opts = [good] + [x for x in [M(str(a)), M(ksq(a, 3)), M(str(2 * a)), M(ksq(a, 2))] if x != good][:3]
    return dict(en='Triangle \\(ABC\\) is equilateral with side \\(%d\\) (figure). Then \\(|%s|=\\)…' % (a, expr), vi='Tam giác \\(ABC\\) đều cạnh \\(%d\\) (hình vẽ). Khi đó \\(|%s|=\\)…' % (a, expr),
                opts=opts, fig=PF(P, segs=[('A', 'B'), ('B', 'C'), ('C', 'A')], alt='Equilateral triangle ABC'),
                ee=('Sum: twice the median from \\(A\\): \\(2\\cdot\\frac{%d\\sqrt3}{2}=%s\\).' % (a, ksq(a, 3))) if k != 1 else ('\\(\\overrightarrow{AB}-\\overrightarrow{AC}=\\overrightarrow{CB}\\), length \\(%d\\).' % a),
                ev=('Tổng bằng hai lần vectơ trung tuyến từ \\(A\\): \\(2\\cdot\\frac{%d\\sqrt3}{2}=%s\\).' % (a, ksq(a, 3))) if k != 1 else ('\\(\\overrightarrow{AB}-\\overrightarrow{AC}=\\overrightarrow{CB}\\), độ dài \\(%d\\).' % a))

E8 = [('\\overrightarrow{AB}-\\overrightarrow{AC}=\\overrightarrow{BC}', '\\overrightarrow{AB}-\\overrightarrow{AC}=\\overrightarrow{CB}'), ('\\overrightarrow{MN}-\\overrightarrow{MP}=\\overrightarrow{NP}', '\\overrightarrow{MN}-\\overrightarrow{MP}=\\overrightarrow{PN}'), ('\\overrightarrow{OA}-\\overrightarrow{OB}=\\overrightarrow{AB}', '\\overrightarrow{OA}-\\overrightarrow{OB}=\\overrightarrow{BA}')]
def s8_d_error(r, lv, ctx):
    w, c = E8[(lv - 1) % 3]
    O = [('Wrong: the correct result is \\(%s\\).' % c, 'Sai: kết quả đúng là \\(%s\\).' % c), ('Correct.', 'Đúng.'), ('Wrong: the difference of two vectors is always \\(\\vec0\\).', 'Sai: hiệu hai vectơ luôn bằng \\(\\vec0\\).'), ('Wrong: one must add the vectors instead.', 'Sai: phải cộng hai vectơ.')]
    return dict(en='A student wrote \\(%s\\). Which comment is correct?' % w, vi='Một bạn viết \\(%s\\). Nhận xét nào đúng?' % w, opts=[tt(*x) for x in O],
                ee='Difference rule: \\(\\overrightarrow{OX}-\\overrightarrow{OY}=\\overrightarrow{YX}\\), so \\(%s\\).' % c, ev='Quy tắc hiệu: \\(\\overrightarrow{OX}-\\overrightarrow{OY}=\\overrightarrow{YX}\\) nên \\(%s\\).' % c)

PT8 = [('\\overrightarrow{MA}-\\overrightarrow{MB}+\\overrightarrow{MC}=\\vec0', 'ABCM'), ('\\overrightarrow{MB}-\\overrightarrow{MC}+\\overrightarrow{MA}=\\vec0', 'BCAM'), ('\\overrightarrow{MC}-\\overrightarrow{MA}+\\overrightarrow{MB}=\\vec0', 'CABM')]
def s8_d_point(r, lv, ctx):
    e, good = PT8[(lv - 1) % 3]
    O = [('\\(%s\\) is a parallelogram' % good, '\\(%s\\) là hình bình hành' % good), ('\\(M\\) is the centroid of triangle \\(ABC\\)', '\\(M\\) là trọng tâm tam giác \\(ABC\\)'),
         ('\\(M\\) is the midpoint of \\(%s%s\\)' % (good[0], good[2]), '\\(M\\) là trung điểm của \\(%s%s\\)' % (good[0], good[2])), ('\\(%s%s%s%s\\) is a parallelogram' % (good[0], good[2], good[1], 'M'), '\\(%s%s%s%s\\) là hình bình hành' % (good[0], good[2], good[1], 'M'))]
    return dict(en='Given triangle \\(ABC\\) and a point \\(M\\) with \\(%s\\). Then…' % e, vi='Cho tam giác \\(ABC\\) và điểm \\(M\\) thỏa mãn \\(%s\\). Khi đó…' % e, opts=[tt(*x) for x in O],
                ee='\\(\\overrightarrow{M%s}-\\overrightarrow{M%s}=\\overrightarrow{%s%s}\\), so \\(\\overrightarrow{M%s}=\\overrightarrow{%s%s}\\): \\(%s\\) is a parallelogram.' % (good[0], good[1], good[1], good[0], good[2], good[0], good[1], good),
                ev='\\(\\overrightarrow{M%s}-\\overrightarrow{M%s}=\\overrightarrow{%s%s}\\) nên \\(\\overrightarrow{M%s}=\\overrightarrow{%s%s}\\): \\(%s\\) là hình bình hành.' % (good[0], good[1], good[1], good[0], good[2], good[0], good[1], good))

def s8_d_forces(r, lv, ctx):
    Fv = r.choice([10, 20, 30, 40, 50, 60]); ang = [60, 120, 90][(lv - 1) % 3]
    good = {60: M('%s\\ \\text{N}' % ksq(Fv, 3)), 120: M('%d\\ \\text{N}' % Fv), 90: M('%s\\ \\text{N}' % ksq(Fv, 2))}[ang]
    alls = [M('%s\\ \\text{N}' % ksq(Fv, 3)), M('%d\\ \\text{N}' % Fv), M('%s\\ \\text{N}' % ksq(Fv, 2)), M('%d\\ \\text{N}' % (2 * Fv))]
    t = math.radians(ang); P = {'O': (0, 0), '_1': (3, 0), '_2': (3 * math.cos(t), 3 * math.sin(t))}; P['_3'] = vadd(P['_1'], P['_2'])
    fig = PF(P, vecs=[('O', '_1', ORANGE), ('O', '_2', ORANGE), ('O', '_3', GREEN)], dashed=[('_1', '_3'), ('_2', '_3')], vlabels=[('O', '_1', '\\vec F_1'), ('O', '_2', '\\vec F_2')], alt='Two forces and their resultant')
    return dict(en='Two forces \\(\\vec F_1\\), \\(\\vec F_2\\), each of \\(%d\\) N, act on an object at \\(O\\); the angle between them is \\(%d^\\circ\\) (figure). The magnitude of the resultant force is…' % (Fv, ang),
                vi='Hai lực \\(\\vec F_1\\), \\(\\vec F_2\\), mỗi lực \\(%d\\) N, cùng tác động vào vật tại \\(O\\); góc giữa chúng là \\(%d^\\circ\\) (hình vẽ). Độ lớn hợp lực là…' % (Fv, ang),
                opts=[good] + [x for x in alls if x != good], fig=fig,
                ee='The resultant is the diagonal of a rhombus with angle \\(%d^\\circ\\).' % ang, ev='Hợp lực là đường chéo của hình thoi có góc \\(%d^\\circ\\).' % ang)

HX = {k: (math.cos(math.radians(60 * i)), math.sin(math.radians(60 * i))) for i, k in enumerate('ABCDEF')}; HX['O'] = (0, 0)
HS8 = [(('A', 'B'), ('A', 'F'), ('A', 'O')), (('O', 'B'), ('O', 'F'), ('O', 'A')), (('C', 'B'), ('C', 'D'), ('C', 'O'))]
def s8_d_hex(r, lv, ctx):
    u, w, g = HS8[(lv - 1) % 3]; s_ = vadd(vsub(HX[u[1]], HX[u[0]]), vsub(HX[w[1]], HX[w[0]]))
    cand = [(a, b) for a in 'ABCDEFO' for b in 'ABCDEFO' if a != b and math.dist(vsub(HX[b], HX[a]), s_) > 1e-9]
    r.shuffle(cand); cand.sort(key=lambda x: 0 if x[0] == g[0] else 1)
    return dict(en='\\(ABCDEF\\) is a regular hexagon with center \\(O\\) (figure). Then \\(%s+%s=\\)…' % (ov(*u), ov(*w)), vi='\\(ABCDEF\\) là lục giác đều tâm \\(O\\) (hình vẽ). Khi đó \\(%s+%s=\\)…' % (ov(*u), ov(*w)),
                opts=[OV(*g)] + [OV(*x) for x in cand[:3]], fig=PF(HX, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'A'), ('A', 'D'), ('B', 'E'), ('C', 'F')], alt='Regular hexagon ABCDEF with center O'),
                ee='The two vectors are sides of a rhombus whose diagonal is \\(%s\\).' % ov(*g), ev='Hai vectơ là hai cạnh của một hình thoi có đường chéo \\(%s\\).' % ov(*g))

def s8_d_ineq(r, lv, ctx):
    p, q = sorted(r.sample(range(2, 10), 2)); good = r.randint(q - p + 1, p + q - 1); bads = [p + q + 1, p + q + 3, q - p - 1 if q - p - 1 > 0 else p + q + 2]
    O = [nopt(good)] + [nopt(b) for b in dict.fromkeys(bads)]
    if len(set(O)) < 4: raise AssertionError
    qe = V(lv, ['\\(|\\vec a|=%d\\) and \\(|\\vec b|=%d\\). Which value can \\(|\\vec a+\\vec b|\\) take?', 'Two displacements have lengths %d m and %d m. Which value can the length of their sum be (in m)?', 'Forces of %d N and %d N act at one point. Which value is possible for the resultant (in N)?'])
    qv = V(lv, ['\\(|\\vec a|=%d\\), \\(|\\vec b|=%d\\). \\(|\\vec a+\\vec b|\\) có thể nhận giá trị nào?', 'Hai độ dời có độ dài %d m và %d m. Độ dài của tổng hai độ dời có thể bằng bao nhiêu (m)?', 'Hai lực %d N và %d N cùng tác động tại một điểm. Giá trị nào có thể là độ lớn hợp lực (N)?'])
    return dict(en=qe % (p, q), vi=qv % (p, q), opts=O, ee='\\(%d-%d\\le|\\vec a+\\vec b|\\le%d+%d\\); only \\(%d\\) lies in \\([%d;\\,%d]\\).' % (q, p, q, p, good, q - p, p + q),
                ev='\\(%d-%d\\le|\\vec a+\\vec b|\\le%d+%d\\); chỉ \\(%d\\) thuộc \\([%d;\\,%d]\\).' % (q, p, q, p, good, q - p, p + q))

CS8 = [(('G', 'A'), ('G', 'B'), ('C', 'G')), (('G', 'B'), ('G', 'C'), ('A', 'G')), (('G', 'C'), ('G', 'A'), ('B', 'G'))]
def s8_d_cent(r, lv, ctx):
    u, w, g = CS8[(lv - 1) % 3]
    O = [OV(*g), OV(*g[::-1]), OV(u[1], w[1]), M('\\vec0')]
    return dict(en='\\(G\\) is the centroid of triangle \\(ABC\\) (figure). Then \\(%s+%s=\\)…' % (ov(*u), ov(*w)), vi='\\(G\\) là trọng tâm tam giác \\(ABC\\) (hình vẽ). Khi đó \\(%s+%s=\\)…' % (ov(*u), ov(*w)),
                opts=O, fig=fig_cent(), ee='From \\(\\overrightarrow{GA}+\\overrightarrow{GB}+\\overrightarrow{GC}=\\vec0\\): the sum equals \\(-\\overrightarrow{G%s}=%s\\).' % (g[0] if g[1] == 'G' else g[1], ov(*g)),
                ev='Từ \\(\\overrightarrow{GA}+\\overrightarrow{GB}+\\overrightarrow{GC}=\\vec0\\): tổng bằng \\(-\\overrightarrow{G%s}=%s\\).' % (g[0] if g[1] == 'G' else g[1], ov(*g)))

def s8_d_rect(r, lv, ctx):
    p, q, h = r.choice(PYT); good = 2 * h
    P = {'A': (0, 0), 'B': (5, 0), 'C': (5, 3), 'D': (0, 3)}
    E = ['\\overrightarrow{AB}+\\overrightarrow{AD}+\\overrightarrow{AC}', '\\overrightarrow{AB}+\\overrightarrow{AC}+\\overrightarrow{AD}', '\\overrightarrow{AC}+\\overrightarrow{AB}+\\overrightarrow{AD}'][(lv - 1) % 3]
    return dict(en='\\(ABCD\\) is a rectangle with \\(AB=%d\\), \\(AD=%d\\) (figure). Then \\(|%s|=\\)…' % (p, q, E), vi='Hình chữ nhật \\(ABCD\\) có \\(AB=%d\\), \\(AD=%d\\) (hình vẽ). Khi đó \\(|%s|=\\)…' % (p, q, E),
                opts=nopts(r, good, [h, p + q + h, 3 * h, p + q]), fig=PF(P, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')], dashed=[('A', 'C')], right=[('B', 'A', 'D')], alt='Rectangle ABCD'),
                ee='\\(\\overrightarrow{AB}+\\overrightarrow{AD}=\\overrightarrow{AC}\\), so the sum is \\(2\\overrightarrow{AC}\\) with length \\(2\\cdot%d=%d\\).' % (h, good), ev='\\(\\overrightarrow{AB}+\\overrightarrow{AD}=\\overrightarrow{AC}\\) nên tổng bằng \\(2\\overrightarrow{AC}\\), độ dài \\(2\\cdot%d=%d\\).' % (h, good))

B8 = dict(A=[s8_grid_sum, s8_mid_rule], B=[s8_tf_cent], C=[], D=[s8_d_equil, s8_d_error, s8_d_point, s8_d_forces, s8_d_hex, s8_d_ineq, s8_d_cent, s8_d_rect])

# ====================================================================== BÀI 9 – Tích của một vectơ với một số
def seg_fig(n, pts):
    """Đoạn AB chia n phần bằng nhau; pts = {tên: chỉ số 0..n} (A = 0)."""
    P = {k: (i * 1.0, 0.0) for k, i in pts.items()}
    for i in range(n + 1):
        if i not in pts.values(): P['_%d' % i] = (i * 1.0, 0.0)
    P['_top'] = (0, 0.6); P['_bot'] = (0, -0.6)
    names = sorted(pts, key=lambda k: pts[k])
    c = Canvas(); s = 5.6 / n
    c.poly([(0, 0), (n * s, 0)], 'ink, line width=0.9pt')
    for i in range(n + 1): c.poly([(i * s, -0.09), (i * s, 0.09)], 'ink, line width=0.7pt')
    for k, i in pts.items():
        if not k.startswith('_'): c.dot(i * s, 0, color=INK)
    for k, i in pts.items():
        if not k.startswith('_'): c.label(i * s, 0, '$%s$' % k, 0.3, 0.36, [(0, 0.32), (0, -0.32)])
    fn = c.svg(); return (G.img(fn, 'Segment divided into %d equal parts' % n, 360), G.img(fn, 'Đoạn thẳng chia %d phần bằng nhau' % n, 360))

def k9_seg(r, lv, ctx):
    n = r.choice([4, 5, 6, 8]); i, j = sorted(r.sample(range(1, n), 2)); pts = {'A': 0, 'B': n, 'M': i, 'N': j}
    pairs = [(('M', 'N'), ('A', 'B')), (('N', 'A'), ('M', 'B')), (('B', 'M'), ('N', 'A'))][(lv - 1) % 3]
    (p, q), (u, w) = pairs; k = F(pts[q] - pts[p], pts[w] - pts[u])
    O = [M(frt(k)), M(frt(-k)), M(frt(1 / k)), M(frt(-1 / k))] if abs(k) != 1 else [M(frt(k)), M(frt(-k)), M(frt(2 * k)), M(frt(k / 2))]
    if len(set(O)) < 4: raise AssertionError
    return dict(en='The segment \\(AB\\) is divided into %d equal parts (figure). If \\(%s=k\\,%s\\), then \\(k=\\)…' % (n, ov(p, q), ov(u, w)), vi='Đoạn thẳng \\(AB\\) được chia thành %d phần bằng nhau (hình vẽ). Nếu \\(%s=k\\,%s\\) thì \\(k=\\)…' % (n, ov(p, q), ov(u, w)),
                opts=O, fig=seg_fig(n, pts), ee='\\(%s%s=%d\\) parts, \\(%s%s=%d\\) parts, %s direction: \\(k=%s\\).' % (p, q, abs(pts[q] - pts[p]), u, w, abs(pts[w] - pts[u]), 'same' if k > 0 else 'opposite', frt(k)),
                ev='\\(%s%s=%d\\) phần, \\(%s%s=%d\\) phần, %s hướng: \\(k=%s\\).' % (p, q, abs(pts[q] - pts[p]), u, w, abs(pts[w] - pts[u]), 'cùng' if k > 0 else 'ngược', frt(k)))

def k9_grid_k(r, lv, ctx):
    d = r.choice([(1, 2), (2, 1), (1, -1), (2, -1), (1, 3), (3, 1)]); m, n_ = r.choice([(1, 2), (2, 1), (3, 1), (1, 3), (2, 3), (3, 2)]); sg = r.choice([1, -1])
    u = smul(m, d); v = smul(sg * n_, d); k = F(sg * n_, m)
    fig = GRIDV(lay([u, v], ['\\vec u', '\\vec v'], GREEN), 'Two collinear vectors on a grid')
    qe = V(lv, ['In the figure, \\(\\vec v=k\\,\\vec u\\). Find \\(k\\).', 'Using the grid, the number \\(k\\) with \\(\\vec v=k\\,\\vec u\\) is…', 'The vectors in the figure satisfy \\(\\vec v=k\\,\\vec u\\). Then \\(k=\\)…'])
    qv = V(lv, ['Trong hình vẽ, \\(\\vec v=k\\,\\vec u\\). Tìm \\(k\\).', 'Dựa vào lưới ô vuông, số \\(k\\) thỏa mãn \\(\\vec v=k\\,\\vec u\\) là…', 'Hai vectơ trong hình thỏa mãn \\(\\vec v=k\\,\\vec u\\). Khi đó \\(k=\\)…'])
    O = list(dict.fromkeys([M(frt(k)), M(frt(-k)), M(frt(1 / k)), M(frt(-1 / k)), M(frt(k + 1))]))[:4]
    return dict(en=qe, vi=qv, opts=O, fig=fig, ee='\\(|\\vec v|:|\\vec u|=%d:%d\\), %s direction: \\(k=%s\\).' % (n_, m, 'same' if sg > 0 else 'opposite', frt(k)),
                ev='\\(|\\vec v|:|\\vec u|=%d:%d\\), %s hướng: \\(k=%s\\).' % (n_, m, 'cùng' if sg > 0 else 'ngược', frt(k)))

def k9_tf_seg(r, lv, ctx):
    n = r.choice([3, 4, 5, 6]); i = r.randrange(1, n); pts = {'A': 0, 'B': n, 'M': i}
    k = F(i, n); truth = r.random() < .5; claim = k if truth else r.choice([1 - k, -k, F(i, n - i)])
    if claim == k and not truth: raise AssertionError
    E = [('\\overrightarrow{AM}', '\\overrightarrow{AB}'), ('\\overrightarrow{AM}', '\\overrightarrow{AB}'), ('\\overrightarrow{AM}', '\\overrightarrow{AB}')][(lv - 1) % 3]
    qe = V(lv, ['The segment \\(AB\\) is divided into %d equal parts (figure). Then \\(%s=%s\\,%s\\).', 'In the figure (\\(AB\\) is cut into %d equal parts), \\(%s=%s\\,%s\\).', 'From the figure with %d equal parts, \\(%s=%s\\,%s\\).'])
    qv = V(lv, ['Đoạn thẳng \\(AB\\) được chia thành %d phần bằng nhau (hình vẽ). Khi đó \\(%s=%s\\,%s\\).', 'Trong hình (\\(AB\\) được chia thành %d phần bằng nhau), \\(%s=%s\\,%s\\).', 'Theo hình có %d phần bằng nhau, \\(%s=%s\\,%s\\).'])
    return dict(en=qe % (n, E[0], frt(claim), E[1]), vi=qv % (n, E[0], frt(claim), E[1]), truth=truth, fig=seg_fig(n, pts),
                ee='\\(AM=%d\\) parts, \\(AB=%d\\) parts, same direction: \\(%s=%s\\,%s\\).' % (i, n, E[0], frt(k), E[1]), ev='\\(AM=%d\\) phần, \\(AB=%d\\) phần, cùng hướng: \\(%s=%s\\,%s\\).' % (i, n, E[0], frt(k), E[1]))

# ---- D, Bài 9
BASES = [((2, 0), (1, 2)), ((2, 1), (0, 2)), ((1, 1), (2, -1)), ((3, 0), (1, 1))]
def k9_d_decomp(r, lv, ctx):
    a, b = r.choice(BASES); x, y = r.choice([1, 2, -1]), r.choice([1, -1, 2, F(1, 2)])
    u = vadd(smul(x, a), smul(y, b))
    if F(u[0]).denominator != 1 or F(u[1]).denominator != 1 or u == (0, 0): raise AssertionError
    u = (int(u[0]), int(u[1]))
    fig = GRIDV(lay([a, b, u], ['\\vec a', '\\vec b', '\\vec u'], GREEN), 'Vectors a, b and u on a grid')
    def ex(p, q): return M('%s\\vec a%s\\vec b' % (('' if p == 1 else '-' if p == -1 else frt(p)), ('+' if q > 0 else '-') + ('' if abs(q) == 1 else frt(abs(q)))))
    O = list(dict.fromkeys([ex(x, y), ex(y, x) if y != x else ex(x, -y), ex(-x, y), ex(x, -y), ex(x + 1, y)]))[:4]
    qe = V(lv, ['In the figure, the vector \\(\\vec u\\) equals…', 'Express \\(\\vec u\\) in terms of \\(\\vec a\\) and \\(\\vec b\\) (figure).', 'Using the grid, write \\(\\vec u=x\\,\\vec a+y\\,\\vec b\\). The correct expression is…'])
    qv = V(lv, ['Trong hình vẽ, vectơ \\(\\vec u\\) bằng…', 'Biểu diễn \\(\\vec u\\) theo \\(\\vec a\\) và \\(\\vec b\\) (hình vẽ).', 'Dựa vào lưới ô vuông, viết \\(\\vec u=x\\,\\vec a+y\\,\\vec b\\). Biểu thức đúng là…'])
    return dict(en=qe, vi=qv, opts=O, fig=fig, ee='Check by counting squares: \\(%s\\) gives \\(%s\\).' % (O[0].strip('\\()'), P2(u)), ev='Kiểm tra bằng cách đếm ô: \\(%s\\) cho \\(%s\\).' % (O[0].strip('\\()'), P2(u)))

CG9 = [('\\overrightarrow{AG}', '\\dfrac13\\overrightarrow{AB}+\\dfrac13\\overrightarrow{AC}', ['\\dfrac23\\overrightarrow{AB}+\\dfrac23\\overrightarrow{AC}', '\\dfrac12\\overrightarrow{AB}+\\dfrac12\\overrightarrow{AC}', '\\overrightarrow{AB}+\\overrightarrow{AC}']),
       ('\\overrightarrow{AI}', '\\dfrac12\\overrightarrow{AB}+\\dfrac12\\overrightarrow{AC}', ['\\dfrac13\\overrightarrow{AB}+\\dfrac13\\overrightarrow{AC}', '\\overrightarrow{AB}+\\overrightarrow{AC}', '\\dfrac12\\overrightarrow{AB}-\\dfrac12\\overrightarrow{AC}']),
       ('\\overrightarrow{GA}', '-\\dfrac13\\overrightarrow{AB}-\\dfrac13\\overrightarrow{AC}', ['\\dfrac13\\overrightarrow{AB}+\\dfrac13\\overrightarrow{AC}', '-\\dfrac23\\overrightarrow{AB}-\\dfrac23\\overrightarrow{AC}', '\\dfrac23\\overrightarrow{AB}+\\dfrac13\\overrightarrow{AC}'])]
def k9_d_centroid(r, lv, ctx):
    v, good, bads = CG9[(lv - 1) % 3]
    return dict(en='\\(G\\) is the centroid of triangle \\(ABC\\) and \\(I\\) is the midpoint of \\(BC\\) (figure). Then \\(%s=\\)…' % v, vi='\\(G\\) là trọng tâm tam giác \\(ABC\\), \\(I\\) là trung điểm của \\(BC\\) (hình vẽ). Khi đó \\(%s=\\)…' % v,
                opts=[M(good)] + [M(b) for b in bads], fig=fig_cent(), ee='\\(\\overrightarrow{AI}=\\frac12(\\overrightarrow{AB}+\\overrightarrow{AC})\\) and \\(\\overrightarrow{AG}=\\frac23\\overrightarrow{AI}\\).',
                ev='\\(\\overrightarrow{AI}=\\frac12(\\overrightarrow{AB}+\\overrightarrow{AC})\\) và \\(\\overrightarrow{AG}=\\frac23\\overrightarrow{AI}\\).')

def k9_d_error(r, lv, ctx):
    E = [('"\\(\\vec a\\) and \\(\\vec b\\) are collinear, so there is a number \\(k\\) with \\(\\vec b=k\\vec a\\)."', '"\\(\\vec a\\) và \\(\\vec b\\) cùng phương nên có số \\(k\\) để \\(\\vec b=k\\vec a\\)."'),
         ('"If \\(k\\vec a=\\vec 0\\) then \\(\\vec a=\\vec 0\\)."', '"Nếu \\(k\\vec a=\\vec 0\\) thì \\(\\vec a=\\vec 0\\)."'),
         ('"\\(|k\\vec a|=k|\\vec a|\\) for every number \\(k\\)."', '"\\(|k\\vec a|=k|\\vec a|\\) với mọi số \\(k\\)."')][(lv - 1) % 3]
    G_ = [('Wrong when \\(\\vec a=\\vec0\\) and \\(\\vec b\\ne\\vec0\\); it needs \\(\\vec a\\ne\\vec0\\).', 'Sai khi \\(\\vec a=\\vec0\\), \\(\\vec b\\ne\\vec0\\); cần thêm \\(\\vec a\\ne\\vec0\\).'),
          ('Wrong: \\(k\\) may be \\(0\\).', 'Sai: có thể \\(k=0\\).'), ('Wrong: it should be \\(|k|\\,|\\vec a|\\).', 'Sai: phải là \\(|k|\\,|\\vec a|\\).')][(lv - 1) % 3]
    O = [G_, ('Always correct.', 'Luôn đúng.'), ('Wrong: collinear vectors are always equal.', 'Sai: hai vectơ cùng phương luôn bằng nhau.'), ('Wrong: \\(k\\) must be positive.', 'Sai: \\(k\\) phải là số dương.')]
    return dict(en='A student claims %s Which comment is correct?' % E[0], vi='Một bạn khẳng định %s Nhận xét nào đúng?' % E[1], opts=[tt(*x) for x in O], ee=G_[0], ev=G_[1])

def k9_d_point(r, lv, ctx):
    p, q = r.choice([(1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2)]); k = F(q, p + q)
    n = p + q; pts = {'A': 0, 'B': n}
    for i in range(1, n): pts['_%d' % i] = i
    O = list(dict.fromkeys([M(frt(k)), M(frt(1 - k)), M(frt(F(q, p))), M(frt(F(p, q))), M(frt(-k))]))[:4]
    qe = V(lv, ['The point \\(M\\) satisfies \\(%d\\overrightarrow{MA}+%d\\overrightarrow{MB}=\\vec0\\). Then \\(\\overrightarrow{AM}=k\\,\\overrightarrow{AB}\\) with \\(k=\\)…', 'Find \\(k\\) such that \\(\\overrightarrow{AM}=k\\,\\overrightarrow{AB}\\), given \\(%d\\overrightarrow{MA}+%d\\overrightarrow{MB}=\\vec0\\).', '\\(%d\\overrightarrow{MA}+%d\\overrightarrow{MB}=\\vec0\\). The point \\(M\\) lies on \\(AB\\) with \\(\\overrightarrow{AM}=k\\,\\overrightarrow{AB}\\), \\(k=\\)…'])
    qv = V(lv, ['Điểm \\(M\\) thỏa mãn \\(%d\\overrightarrow{MA}+%d\\overrightarrow{MB}=\\vec0\\). Khi đó \\(\\overrightarrow{AM}=k\\,\\overrightarrow{AB}\\) với \\(k=\\)…', 'Tìm \\(k\\) để \\(\\overrightarrow{AM}=k\\,\\overrightarrow{AB}\\), biết \\(%d\\overrightarrow{MA}+%d\\overrightarrow{MB}=\\vec0\\).', '\\(%d\\overrightarrow{MA}+%d\\overrightarrow{MB}=\\vec0\\). Điểm \\(M\\) thuộc \\(AB\\) với \\(\\overrightarrow{AM}=k\\,\\overrightarrow{AB}\\), \\(k=\\)…'])
    E = lambda t, a, b: t.replace('%d\\overrightarrow{MA}', ('' if a == 1 else '%d' % a) + '\\overrightarrow{MA}').replace('+%d\\overrightarrow{MB}', '+' + ('' if b == 1 else '%d' % b) + '\\overrightarrow{MB}')
    return dict(en=E(qe, p, q), vi=E(qv, p, q), opts=O, fig=seg_fig(n, pts),
                ee='\\(\\overrightarrow{MB}=\\overrightarrow{MA}+\\overrightarrow{AB}\\), so \\(%d\\overrightarrow{MA}+%s\\overrightarrow{AB}=\\vec0\\) and \\(\\overrightarrow{AM}=\\frac{%d}{%d}\\overrightarrow{AB}\\).' % (n, '' if q == 1 else q, q, n),
                ev='\\(\\overrightarrow{MB}=\\overrightarrow{MA}+\\overrightarrow{AB}\\) nên \\(%d\\overrightarrow{MA}+%s\\overrightarrow{AB}=\\vec0\\) và \\(\\overrightarrow{AM}=\\frac{%d}{%d}\\overrightarrow{AB}\\).' % (n, '' if q == 1 else q, q, n))

def k9_d_collin(r, lv, ctx):
    a, b = r.choice([(2, -3), (1, 2), (3, 1), (2, 5), (-1, 4)]); t = r.choice([2, 3, -2]); m = a * t
    E = '\\overrightarrow{AB}=%d\\vec u%s%d\\vec v' % (a, '+' if b > 0 else '-', abs(b)); E2 = '\\overrightarrow{AC}=m\\vec u%s%d\\vec v' % ('+' if b * t > 0 else '-', abs(b * t))
    E = E.replace('=1\\vec', '=\\vec').replace('=-1\\vec', '=-\\vec').replace('+1\\vec', '+\\vec').replace('-1\\vec', '-\\vec')
    E2 = E2.replace('+1\\vec', '+\\vec').replace('-1\\vec', '-\\vec')
    qe = V(lv, ['\\(\\vec u\\), \\(\\vec v\\) are not collinear; \\(%s\\), \\(%s\\). The points \\(A\\), \\(B\\), \\(C\\) are collinear when \\(m=\\)…', 'Find \\(m\\) so that \\(A\\), \\(B\\), \\(C\\) lie on a line, where \\(%s\\), \\(%s\\) (\\(\\vec u\\), \\(\\vec v\\) not collinear).', 'Given \\(%s\\) and \\(%s\\) with non-collinear \\(\\vec u\\), \\(\\vec v\\). For which \\(m\\) are \\(A\\), \\(B\\), \\(C\\) collinear?'])
    qv = V(lv, ['\\(\\vec u\\), \\(\\vec v\\) không cùng phương; \\(%s\\), \\(%s\\). Ba điểm \\(A\\), \\(B\\), \\(C\\) thẳng hàng khi \\(m=\\)…', 'Tìm \\(m\\) để \\(A\\), \\(B\\), \\(C\\) thẳng hàng, biết \\(%s\\), \\(%s\\) (\\(\\vec u\\), \\(\\vec v\\) không cùng phương).', 'Cho \\(%s\\), \\(%s\\) với \\(\\vec u\\), \\(\\vec v\\) không cùng phương. Với giá trị nào của \\(m\\) thì \\(A\\), \\(B\\), \\(C\\) thẳng hàng?'])
    return dict(en=qe % (E, E2), vi=qv % (E, E2), opts=nopts(r, m, [-m, a, t, a + t]), ee='Need \\(\\overrightarrow{AC}=%d\\,\\overrightarrow{AB}\\), so \\(m=%d\\cdot%d=%d\\).' % (t, t, a, m), ev='Cần \\(\\overrightarrow{AC}=%d\\,\\overrightarrow{AB}\\) nên \\(m=%d\\cdot%d=%d\\).' % (t, t, a, m))

def k9_d_trap(r, lv, ctx):
    a, b = r.choice([(6, 10), (4, 8), (5, 9), (7, 13), (3, 11), (8, 12)]); good = F(a + b, 2)
    P = {'A': (0, 0), 'B': (6, 0), 'C': (4.6, 3), 'D': (1.6, 3)}; P['M'] = vadd(smul(0.5, P['A']), smul(0.5, P['D'])); P['N'] = vadd(smul(0.5, P['B']), smul(0.5, P['C']))
    return dict(en='\\(ABCD\\) is a trapezoid with \\(AB\\parallel CD\\), \\(AB=%d\\), \\(CD=%d\\); \\(M\\), \\(N\\) are the midpoints of \\(AD\\), \\(BC\\) (figure). Using \\(\\overrightarrow{MN}=\\frac12(\\overrightarrow{AB}+\\overrightarrow{DC})\\), \\(|\\overrightarrow{MN}|=\\)…' % (b, a),
                vi='\\(ABCD\\) là hình thang có \\(AB\\parallel CD\\), \\(AB=%d\\), \\(CD=%d\\); \\(M\\), \\(N\\) là trung điểm của \\(AD\\), \\(BC\\) (hình vẽ). Dùng \\(\\overrightarrow{MN}=\\frac12(\\overrightarrow{AB}+\\overrightarrow{DC})\\), \\(|\\overrightarrow{MN}|=\\)…' % (b, a),
                opts=nopts(r, good, [a + b, F(b - a, 2), b - a, F(a + b, 4)]), fig=PF(P, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')], vecs=[('M', 'N', ORANGE)], alt='Trapezoid ABCD with the midline MN'),
                ee='\\(\\overrightarrow{AB}\\), \\(\\overrightarrow{DC}\\) have the same direction: \\(MN=\\frac{%d+%d}{2}=%s\\).' % (b, a, ne(good)), ev='\\(\\overrightarrow{AB}\\), \\(\\overrightarrow{DC}\\) cùng hướng: \\(MN=\\frac{%d+%d}{2}=%s\\).' % (b, a, nv(good)))

PO9 = [('\\overrightarrow{AO}', '\\dfrac12\\overrightarrow{AB}+\\dfrac12\\overrightarrow{AD}', ['\\overrightarrow{AB}+\\overrightarrow{AD}', '\\dfrac12\\overrightarrow{AB}-\\dfrac12\\overrightarrow{AD}', '2\\overrightarrow{AB}+2\\overrightarrow{AD}']),
       ('\\overrightarrow{BO}', '\\dfrac12\\overrightarrow{AD}-\\dfrac12\\overrightarrow{AB}', ['\\dfrac12\\overrightarrow{AB}-\\dfrac12\\overrightarrow{AD}', '\\overrightarrow{AD}-\\overrightarrow{AB}', '\\dfrac12\\overrightarrow{AB}+\\dfrac12\\overrightarrow{AD}']),
       ('\\overrightarrow{OC}', '\\dfrac12\\overrightarrow{AB}+\\dfrac12\\overrightarrow{AD}', ['-\\dfrac12\\overrightarrow{AB}-\\dfrac12\\overrightarrow{AD}', '\\overrightarrow{AB}+\\overrightarrow{AD}', '\\dfrac12\\overrightarrow{AD}-\\dfrac12\\overrightarrow{AB}'])]
def k9_d_para(r, lv, ctx):
    v, good, bads = PO9[(lv - 1) % 3]; P = dict(PG); P['O'] = vadd(smul(0.5, PG['A']), smul(0.5, PG['C']))
    return dict(en='\\(ABCD\\) is a parallelogram with center \\(O\\) (figure). Then \\(%s=\\)…' % v, vi='\\(ABCD\\) là hình bình hành tâm \\(O\\) (hình vẽ). Khi đó \\(%s=\\)…' % v,
                opts=[M(good)] + [M(b) for b in bads], fig=PF(P, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('A', 'C'), ('B', 'D')], alt='Parallelogram ABCD with center O'),
                ee='\\(\\overrightarrow{AC}=\\overrightarrow{AB}+\\overrightarrow{AD}\\), \\(\\overrightarrow{BD}=\\overrightarrow{AD}-\\overrightarrow{AB}\\), and \\(O\\) is the midpoint of both diagonals.',
                ev='\\(\\overrightarrow{AC}=\\overrightarrow{AB}+\\overrightarrow{AD}\\), \\(\\overrightarrow{BD}=\\overrightarrow{AD}-\\overrightarrow{AB}\\), \\(O\\) là trung điểm của hai đường chéo.')

SP9 = [(('A car drives east at \\(40\\) km/h (velocity \\(\\vec v\\)); a truck drives west at \\(60\\) km/h (velocity \\(\\vec w\\)).', 'Ô tô chạy về hướng đông với vận tốc \\(40\\) km/h (vectơ vận tốc \\(\\vec v\\)); xe tải chạy về hướng tây với vận tốc \\(60\\) km/h (vectơ vận tốc \\(\\vec w\\)).'), F(-3, 2)),
       (('A drone flies north at \\(12\\) m/s (velocity \\(\\vec v\\)); a bird flies north at \\(4\\) m/s (velocity \\(\\vec w\\)).', 'Thiết bị bay bay về hướng bắc với vận tốc \\(12\\) m/s (vectơ \\(\\vec v\\)); một con chim bay về hướng bắc với vận tốc \\(4\\) m/s (vectơ \\(\\vec w\\)).'), F(1, 3)),
       (('A boat moves downstream at \\(15\\) km/h (velocity \\(\\vec v\\)); a raft moves upstream at \\(5\\) km/h (velocity \\(\\vec w\\)).', 'Ca nô xuôi dòng với vận tốc \\(15\\) km/h (vectơ \\(\\vec v\\)); chiếc bè đi ngược dòng với vận tốc \\(5\\) km/h (vectơ \\(\\vec w\\)).'), F(-1, 3))]
def k9_d_speed(r, lv, ctx):
    (e, v), k = SP9[(lv - 1) % 3]
    O = [M(frt(k)), M(frt(-k)), M(frt(1 / k)), M(frt(-1 / k))]
    return dict(en='%s Then \\(\\vec w=k\\,\\vec v\\) with \\(k=\\)…' % e, vi='%s Khi đó \\(\\vec w=k\\,\\vec v\\) với \\(k=\\)…' % v, opts=O,
                ee='\\(|k|\\) is the ratio of the speeds; \\(k\\lt0\\) when the directions are opposite: \\(k=%s\\).' % frt(k), ev='\\(|k|\\) là tỉ số hai tốc độ; \\(k\\lt0\\) khi hai hướng ngược nhau: \\(k=%s\\).' % frt(k))

B9 = dict(A=[k9_seg, k9_grid_k], B=[k9_tf_seg], C=[], D=[k9_d_decomp, k9_d_centroid, k9_d_error, k9_d_point, k9_d_collin, k9_d_trap, k9_d_para, k9_d_speed])

# ====================================================================== BÀI 10 – Vectơ trong mặt phẳng tọa độ
def gpt(r, lo=-4, hi=5): return (r.randint(lo, hi), r.randint(lo, hi))
def box(*ps, pad=1):
    xs = [p[0] for p in ps] + [0]; ys = [p[1] for p in ps] + [0]
    return (min(xs) - pad, max(xs) + pad), (min(ys) - pad, max(ys) + pad)
def V2(p): return P2(p)

def c10_read_vec(r, lv, ctx):
    for _ in range(100):
        A = gpt(r); B = gpt(r)
        if A != B and A[0] != B[0] and A[1] != B[1] and 0 not in A: break
    u = vsub(B, A); xr, yr = box(A, B)
    fig = GRID(xr, yr, vecs=[(A, B, '\\vec u', ORANGE)], alt='A vector u on the coordinate grid')
    O = list(dict.fromkeys([M(V2(u)), M(V2((u[1], u[0]))), M(V2(smul(-1, u))), M(V2(B)), M(V2(vadd(A, B)))]))[:4]
    qe = V(lv, ['The figure shows the vector \\(\\vec u\\) in the coordinate plane. Its coordinates are…', 'Read the coordinates of \\(\\vec u\\) from the grid.', 'Using the grid (each square has side 1), \\(\\vec u=\\)…'])
    qv = V(lv, ['Hình vẽ biểu diễn vectơ \\(\\vec u\\) trong mặt phẳng tọa độ. Tọa độ của \\(\\vec u\\) là…', 'Đọc tọa độ của \\(\\vec u\\) trên lưới ô vuông.', 'Dựa vào lưới ô vuông (mỗi ô cạnh 1), \\(\\vec u=\\)…'])
    return dict(en=qe, vi=qv, opts=O, fig=fig, ee='From the start to the end: \\(%d\\) horizontally, \\(%d\\) vertically: \\(\\vec u=%s\\).' % (u[0], u[1], V2(u)),
                ev='Từ điểm đầu tới điểm cuối: \\(%d\\) theo phương ngang, \\(%d\\) theo phương dọc: \\(\\vec u=%s\\).' % (u[0], u[1], V2(u)))

TRIP2 = [(3, 4, 5), (4, 3, 5), (6, 8, 10), (8, 6, 10), (0, 5, 5), (5, 0, 5)]
def c10_read_len(r, lv, ctx):
    a, b, h = r.choice(TRIP2); A = gpt(r, -3, 2); B = (A[0] + a * r.choice([1, -1]), A[1] + b * r.choice([1, -1]))
    xr, yr = box(A, B)
    if xr[1] - xr[0] > 13 or yr[1] - yr[0] > 13: raise AssertionError
    fig = GRID(xr, yr, pts={'A': A, 'B': B}, alt='Points A and B on the coordinate grid')
    qe = V(lv, ['Read the coordinates of \\(A\\) and \\(B\\) in the figure. Then \\(|\\overrightarrow{AB}|=\\)…', 'From the figure, the length of \\(\\overrightarrow{AB}\\) is…', 'Using the grid, find \\(AB\\).'])
    qv = V(lv, ['Đọc tọa độ của \\(A\\), \\(B\\) trên hình. Khi đó \\(|\\overrightarrow{AB}|=\\)…', 'Theo hình vẽ, độ dài của \\(\\overrightarrow{AB}\\) là…', 'Dựa vào lưới ô vuông, tính \\(AB\\).'])
    return dict(en=qe, vi=qv, opts=nopts(r, h, [a + b, h * h, abs(a - b) if a != b else h + 2, h + 1]), fig=fig,
                ee='\\(A%s\\), \\(B%s\\), \\(\\overrightarrow{AB}=%s\\), \\(AB=\\sqrt{%d^2+%d^2}=%d\\).' % (V2(A), V2(B), V2(vsub(B, A)), a, b, h),
                ev='\\(A%s\\), \\(B%s\\), \\(\\overrightarrow{AB}=%s\\), \\(AB=\\sqrt{%d^2+%d^2}=%d\\).' % (V2(A), V2(B), V2(vsub(B, A)), a, b, h))

def c10_tf_mid(r, lv, ctx):
    for _ in range(100):
        A = gpt(r); B = (A[0] + 2 * r.randint(1, 3) * r.choice([1, -1]), A[1] + 2 * r.randint(1, 3) * r.choice([1, -1]))
        if max(abs(B[0]), abs(B[1])) <= 6: break
    I = ((A[0] + B[0]) // 2, (A[1] + B[1]) // 2); truth = r.random() < .5
    C = I if truth else r.choice([(I[0] + 1, I[1]), (I[0], I[1] - 1), (I[0] - 1, I[1] + 1)])
    if C in (A, B): raise AssertionError
    xr, yr = box(A, B, C)
    W = [('\\(C\\) is the midpoint of \\(AB\\).', '\\(C\\) là trung điểm của \\(AB\\).'), ('\\(\\overrightarrow{AC}=\\overrightarrow{CB}\\).', '\\(\\overrightarrow{AC}=\\overrightarrow{CB}\\).'), ('\\(\\overrightarrow{CA}+\\overrightarrow{CB}=\\vec0\\).', '\\(\\overrightarrow{CA}+\\overrightarrow{CB}=\\vec0\\).')][(lv - 1) % 3]
    return dict(en='Points \\(A\\), \\(B\\), \\(C\\) are shown on the coordinate grid. ' + W[0], vi='Các điểm \\(A\\), \\(B\\), \\(C\\) được biểu diễn trên lưới tọa độ. ' + W[1], truth=truth,
                fig=GRID(xr, yr, pts={'A': A, 'B': B, 'C': C}, alt='Points A, B, C on the coordinate grid'),
                ee='The midpoint of \\(AB\\) is \\(%s\\); \\(C%s\\).' % (V2(I), V2(C)), ev='Trung điểm của \\(AB\\) là \\(%s\\); \\(C%s\\).' % (V2(I), V2(C)))

# ---- D, Bài 10
def c10_d_comb(r, lv, ctx):
    for _ in range(200):
        a = gpt(r, -3, 3); b = gpt(r, -3, 3); x, y = r.choice([1, 2, -1, 3]), r.choice([1, -1, 2, -2])
        if a[0] * b[1] - a[1] * b[0] != 0: break
    c = vadd(smul(x, a), smul(y, b))
    O = list(dict.fromkeys([M('x=%d,\\ y=%d' % (x, y)), M('x=%d,\\ y=%d' % (y, x)), M('x=%d,\\ y=%d' % (-x, y)), M('x=%d,\\ y=%d' % (x, -y)), M('x=%d,\\ y=%d' % (x + 1, y))]))[:4]
    qe = V(lv, ['\\(\\vec a=%s\\), \\(\\vec b=%s\\), \\(\\vec c=%s\\). If \\(\\vec c=x\\vec a+y\\vec b\\), then…', 'Write \\(\\vec c=%s\\) as \\(x\\vec a+y\\vec b\\) with \\(\\vec a=%s\\), \\(\\vec b=%s\\).', 'Find \\(x\\), \\(y\\) such that \\(x\\vec a+y\\vec b=\\vec c\\), where \\(\\vec a=%s\\), \\(\\vec b=%s\\), \\(\\vec c=%s\\).'])
    qv = V(lv, ['\\(\\vec a=%s\\), \\(\\vec b=%s\\), \\(\\vec c=%s\\). Nếu \\(\\vec c=x\\vec a+y\\vec b\\) thì…', 'Biểu diễn \\(\\vec c=%s\\) dưới dạng \\(x\\vec a+y\\vec b\\) với \\(\\vec a=%s\\), \\(\\vec b=%s\\).', 'Tìm \\(x\\), \\(y\\) sao cho \\(x\\vec a+y\\vec b=\\vec c\\), với \\(\\vec a=%s\\), \\(\\vec b=%s\\), \\(\\vec c=%s\\).'])
    args = (V2(c), V2(a), V2(b)) if lv == 2 else (V2(a), V2(b), V2(c))
    return dict(en=qe % args, vi=qv % args, opts=O, ee='Solve \\(%d=%dx%+dy\\), \\(%d=%dx%+dy\\): \\(x=%d\\), \\(y=%d\\).' % (c[0], a[0], b[0], c[1], a[1], b[1], x, y),
                ev='Giải hệ \\(%d=%dx%+dy\\), \\(%d=%dx%+dy\\): \\(x=%d\\), \\(y=%d\\).' % (c[0], a[0], b[0], c[1], a[1], b[1], x, y))

def c10_d_axis(r, lv, ctx):
    for _ in range(300):
        A = gpt(r, -4, 4); B = gpt(r, -4, 4)
        if A[1] * B[1] != 0 and A[1] != B[1] and A != B:
            x = F(A[0] * B[1] - B[0] * A[1], B[1] - A[1])
            if x.denominator == 1 and abs(x) <= 8: break
    else: raise AssertionError
    xr, yr = box(A, B, (int(x), 0))
    if xr[1] - xr[0] > 15: raise AssertionError
    return dict(en='Points \\(A%s\\), \\(B%s\\) are shown in the figure. The point \\(M\\) on the axis \\(Ox\\) with \\(A\\), \\(B\\), \\(M\\) collinear is…' % (V2(A), V2(B)),
                vi='Các điểm \\(A%s\\), \\(B%s\\) như hình vẽ. Điểm \\(M\\) trên trục \\(Ox\\) sao cho \\(A\\), \\(B\\), \\(M\\) thẳng hàng là…' % (V2(A), V2(B)),
                opts=list(dict.fromkeys([M('M%s' % V2((x, 0))), M('M%s' % V2((0, x))), M('M%s' % V2((-x, 0))), M('M%s' % V2((x + 1, 0))), M('M%s' % V2((x - 2, 0)))]))[:4],
                fig=GRID(xr, yr, pts={'A': A, 'B': B}, alt='Points A and B on the coordinate grid'),
                ee='\\(M(m;0)\\): \\(\\overrightarrow{AM}\\), \\(\\overrightarrow{AB}\\) collinear gives \\(m=%s\\).' % frt(x), ev='\\(M(m;0)\\): \\(\\overrightarrow{AM}\\), \\(\\overrightarrow{AB}\\) cùng phương cho \\(m=%s\\).' % frt(x))

def c10_d_sym(r, lv, ctx):
    A = gpt(r, -3, 3); B = gpt(r, -2, 3)
    if A == B: raise AssertionError
    C = (2 * B[0] - A[0], 2 * B[1] - A[1])
    xr, yr = box(A, B, C)
    if xr[1] - xr[0] > 15 or yr[1] - yr[0] > 15: raise AssertionError
    O = list(dict.fromkeys([M('C%s' % V2(C)), M('C%s' % V2((2 * A[0] - B[0], 2 * A[1] - B[1]))), M('C%s' % V2(((A[0] + B[0]) / 2, (A[1] + B[1]) / 2))), M('C%s' % V2(vadd(A, B))), M('C%s' % V2(vsub(B, A)))]))[:4]
    qe = V(lv, ['\\(C\\) is the point symmetric to \\(A\\) with respect to \\(B\\) (figure). Then…', 'Find the point \\(C\\) such that \\(B\\) is the midpoint of \\(AC\\) (figure).', 'The reflection of \\(A\\) through the point \\(B\\) (figure) is…'])
    qv = V(lv, ['\\(C\\) là điểm đối xứng với \\(A\\) qua \\(B\\) (hình vẽ). Khi đó…', 'Tìm điểm \\(C\\) sao cho \\(B\\) là trung điểm của \\(AC\\) (hình vẽ).', 'Điểm đối xứng với \\(A\\) qua điểm \\(B\\) (hình vẽ) là…'])
    return dict(en=qe, vi=qv, opts=O, fig=GRID(xr, yr, pts={'A': A, 'B': B}, alt='Points A and B on the coordinate grid'),
                ee='\\(A%s\\), \\(B%s\\): \\(C=2B-A=%s\\).' % (V2(A), V2(B), V2(C)), ev='\\(A%s\\), \\(B%s\\): \\(C=2B-A=%s\\).' % (V2(A), V2(B), V2(C)))

def c10_d_error(r, lv, ctx):
    for _ in range(100):
        A = gpt(r, -3, 3); B = gpt(r, -3, 4)
        if A != B and vsub(A, B) != vsub(B, A): break
    xr, yr = box(A, B)
    w = vsub(A, B)
    O = [('Wrong: \\(\\overrightarrow{AB}=%s\\) (end minus start).' % V2(vsub(B, A)), 'Sai: \\(\\overrightarrow{AB}=%s\\) (tọa độ điểm cuối trừ điểm đầu).' % V2(vsub(B, A))), ('Correct.', 'Đúng.'),
         ('Wrong: \\(\\overrightarrow{AB}=%s\\).' % V2(vadd(A, B)), 'Sai: \\(\\overrightarrow{AB}=%s\\).' % V2(vadd(A, B))), ('Wrong: \\(\\overrightarrow{AB}=%s\\).' % V2(B), 'Sai: \\(\\overrightarrow{AB}=%s\\).' % V2(B))]
    return dict(en='For the points \\(A\\), \\(B\\) in the figure a student wrote \\(\\overrightarrow{AB}=%s\\). Which comment is correct?' % V2(w), vi='Với hai điểm \\(A\\), \\(B\\) trong hình, một bạn viết \\(\\overrightarrow{AB}=%s\\). Nhận xét nào đúng?' % V2(w),
                opts=[tt(*x) for x in O], fig=GRID(xr, yr, pts={'A': A, 'B': B}, alt='Points A and B on the coordinate grid'),
                ee='\\(A%s\\), \\(B%s\\): \\(\\overrightarrow{AB}=(x_B-x_A;\\,y_B-y_A)=%s\\).' % (V2(A), V2(B), V2(vsub(B, A))), ev='\\(A%s\\), \\(B%s\\): \\(\\overrightarrow{AB}=(x_B-x_A;\\,y_B-y_A)=%s\\).' % (V2(A), V2(B), V2(vsub(B, A))))

def c10_d_third(r, lv, ctx):
    A = gpt(r); B = gpt(r); G_ = gpt(r, -2, 3)
    if A == B: raise AssertionError
    C = (3 * G_[0] - A[0] - B[0], 3 * G_[1] - A[1] - B[1])
    O = list(dict.fromkeys([M('C%s' % V2(C)), M('C%s' % V2((G_[0] - A[0] - B[0], G_[1] - A[1] - B[1]))), M('C%s' % V2((3 * G_[0] + A[0] + B[0], 3 * G_[1] + A[1] + B[1]))), M('C%s' % V2((2 * G_[0] - A[0], 2 * G_[1] - A[1])))]))
    if len(O) < 4: raise AssertionError
    qe = V(lv, ['Triangle \\(ABC\\) has \\(A%s\\), \\(B%s\\) and centroid \\(G%s\\). Then…', 'Find the vertex \\(C\\) of triangle \\(ABC\\), knowing \\(A%s\\), \\(B%s\\) and the centroid \\(G%s\\).', 'The centroid of triangle \\(ABC\\) is \\(G%s\\) with \\(A%s\\), \\(B%s\\). The third vertex is…'])
    qv = V(lv, ['Tam giác \\(ABC\\) có \\(A%s\\), \\(B%s\\) và trọng tâm \\(G%s\\). Khi đó…', 'Tìm đỉnh \\(C\\) của tam giác \\(ABC\\), biết \\(A%s\\), \\(B%s\\) và trọng tâm \\(G%s\\).', 'Trọng tâm tam giác \\(ABC\\) là \\(G%s\\), với \\(A%s\\), \\(B%s\\). Đỉnh còn lại là…'])
    args = (V2(G_), V2(A), V2(B)) if lv == 3 else (V2(A), V2(B), V2(G_))
    return dict(en=qe % args, vi=qv % args, opts=O[:4], ee='\\(C=3G-A-B=%s\\).' % V2(C), ev='\\(C=3G-A-B=%s\\).' % V2(C))

def c10_d_divide(r, lv, ctx):
    k = r.choice([2, 3]); A = gpt(r, -3, 3); t = (r.choice([-1, 1, 2]), r.choice([-1, 1, -2])); B = (A[0] + (k + 1) * t[0], A[1] + (k + 1) * t[1])
    Mp = ((A[0] + k * B[0]) // (k + 1), (A[1] + k * B[1]) // (k + 1))
    O = list(dict.fromkeys([M('M%s' % V2(Mp)), M('M%s' % V2(((k * A[0] + B[0]) / F(k + 1), (k * A[1] + B[1]) / F(k + 1)))), M('M%s' % V2(((A[0] + B[0]) / F(2), (A[1] + B[1]) / F(2)))), M('M%s' % V2((2 * B[0] - A[0], 2 * B[1] - A[1])))]))
    if len(O) < 4: raise AssertionError
    xr, yr = box(A, B)
    qe = V(lv, ['Points \\(A\\), \\(B\\) are shown in the figure. The point \\(M\\) with \\(\\overrightarrow{MA}=-%d\\,\\overrightarrow{MB}\\) is…', 'Read \\(A\\), \\(B\\) from the grid and find \\(M\\) such that \\(\\overrightarrow{MA}=-%d\\,\\overrightarrow{MB}\\).', 'Using the figure, the point \\(M\\) satisfying \\(\\overrightarrow{MA}=-%d\\,\\overrightarrow{MB}\\) has coordinates…'])
    qv = V(lv, ['Các điểm \\(A\\), \\(B\\) như hình vẽ. Điểm \\(M\\) thỏa mãn \\(\\overrightarrow{MA}=-%d\\,\\overrightarrow{MB}\\) là…', 'Đọc tọa độ \\(A\\), \\(B\\) trên lưới rồi tìm \\(M\\) sao cho \\(\\overrightarrow{MA}=-%d\\,\\overrightarrow{MB}\\).', 'Dựa vào hình vẽ, điểm \\(M\\) thỏa mãn \\(\\overrightarrow{MA}=-%d\\,\\overrightarrow{MB}\\) có tọa độ…'])
    return dict(en=qe % k, vi=qv % k,
                opts=O, fig=GRID(xr, yr, pts={'A': A, 'B': B}, alt='Points A and B on the coordinate grid'),
                ee='\\(A%s\\), \\(B%s\\): \\(M=\\dfrac{A+%dB}{%d}=%s\\).' % (V2(A), V2(B), k, k + 1, V2(Mp)), ev='\\(A%s\\), \\(B%s\\): \\(M=\\dfrac{A+%dB}{%d}=%s\\).' % (V2(A), V2(B), k, k + 1, V2(Mp)))

def c10_d_scale(r, lv, ctx):
    a, b, h = r.choice([(3, 4, 5), (4, 3, 5), (6, 8, 10), (5, 12, 13), (8, 6, 10)]); a *= r.choice([1, -1]); b *= r.choice([1, -1]); L = h * r.choice([2, 3])
    k = F(L, h); same = lv != 2; good = smul(k if same else -k, (a, b))
    O = list(dict.fromkeys([M(V2(good)), M(V2(smul(-1, good))), M(V2((good[1], good[0]))), M(V2(smul(L, (a, b))))]))
    if len(O) < 4: raise AssertionError
    W = ('the same direction as', 'cùng hướng với') if same else ('the opposite direction to', 'ngược hướng với')
    return dict(en='The vector \\(\\vec v\\) has %s \\(\\vec u=%s\\) and \\(|\\vec v|=%d\\). Then \\(\\vec v=\\)…' % (W[0], V2((a, b)), L), vi='Vectơ \\(\\vec v\\) %s \\(\\vec u=%s\\) và \\(|\\vec v|=%d\\). Khi đó \\(\\vec v=\\)…' % (W[1], V2((a, b)), L),
                opts=O, ee='\\(|\\vec u|=%d\\), so \\(\\vec v=%s\\vec u=%s\\).' % (h, frt(k if same else -k), V2(good)), ev='\\(|\\vec u|=%d\\) nên \\(\\vec v=%s\\vec u=%s\\).' % (h, frt(k if same else -k), V2(good)))

def c10_d_perim(r, lv, ctx):
    for _ in range(500):
        A = gpt(r, -2, 2); (a1, b1, h1) = r.choice(TRIP2); B = (A[0] + a1, A[1] + b1); (a2, b2, h2) = r.choice(TRIP2); C = (B[0] - a2 * r.choice([1, -1]), B[1] + b2 * r.choice([1, -1]))
        d = vsub(C, A); h3 = math.isqrt(vdot(d, d))
        if h3 * h3 == vdot(d, d) and h3 > 0 and (B[0] - A[0]) * (C[1] - A[1]) != (B[1] - A[1]) * (C[0] - A[0]):
            xr, yr = box(A, B, C)
            if xr[1] - xr[0] <= 14 and yr[1] - yr[0] <= 14: break
    else: raise AssertionError
    good = h1 + h2 + h3
    qe = V(lv, ['Read the vertices of triangle \\(ABC\\) from the figure. Its perimeter is…', 'Using the coordinate grid, find the perimeter of triangle \\(ABC\\).', 'The perimeter of triangle \\(ABC\\) shown on the grid is…'])
    qv = V(lv, ['Đọc tọa độ các đỉnh tam giác \\(ABC\\) trên hình. Chu vi tam giác là…', 'Dựa vào lưới tọa độ, tính chu vi tam giác \\(ABC\\).', 'Chu vi tam giác \\(ABC\\) trên lưới tọa độ là…'])
    return dict(en=qe, vi=qv,
                opts=nopts(r, good, [good + 1, good - 2, h1 + h2, 2 * good]), fig=GRID(xr, yr, pts={'A': A, 'B': B, 'C': C}, alt='Triangle ABC on the coordinate grid'),
                ee='\\(AB=%d\\), \\(BC=%d\\), \\(CA=%d\\); perimeter \\(%d\\).' % (h1, h2, h3, good), ev='\\(AB=%d\\), \\(BC=%d\\), \\(CA=%d\\); chu vi \\(%d\\).' % (h1, h2, h3, good))

B10 = dict(A=[c10_read_vec, c10_read_len], B=[c10_tf_mid], C=[], D=[c10_d_comb, c10_d_axis, c10_d_sym, c10_d_error, c10_d_third, c10_d_divide, c10_d_scale, c10_d_perim])

# ====================================================================== BÀI 11 – Tích vô hướng
SQ = {'A': (0, 0), 'B': (3, 0), 'C': (3, 3), 'D': (0, 3)}
SQ11 = [('\\overrightarrow{AB}\\cdot\\overrightarrow{AC}', 1), ('\\overrightarrow{AC}\\cdot\\overrightarrow{BD}', 0), ('\\overrightarrow{AB}\\cdot\\overrightarrow{CD}', -1)]
def d11_square(r, lv, ctx):
    a = r.choice([2, 3, 4, 5, 6]); e, c = SQ11[(lv - 1) % 3]; good = c * a * a
    return dict(en='\\(ABCD\\) is a square with side \\(%d\\) (figure). Then \\(%s=\\)…' % (a, e), vi='Hình vuông \\(ABCD\\) có cạnh \\(%d\\) (hình vẽ). Khi đó \\(%s=\\)…' % (a, e),
                opts=nopts(r, good, [-good if good else a * a, 2 * a * a, a * a if good != a * a else 0, a]), fig=PF(SQ, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('A', 'C'), ('B', 'D')], right=[('B', 'A', 'D')], alt='Square ABCD'),
                ee='Use \\(|\\vec u||\\vec v|\\cos(\\vec u,\\vec v)\\): result \\(%d\\).' % good, ev='Dùng \\(|\\vec u||\\vec v|\\cos(\\vec u,\\vec v)\\): kết quả \\(%d\\).' % good)

def d11_righttri(r, lv, ctx):
    p, q, h = r.choice(PYT); k = (lv - 1) % 3
    e, good = [('\\overrightarrow{BA}\\cdot\\overrightarrow{BC}', p * p), ('\\overrightarrow{CA}\\cdot\\overrightarrow{CB}', q * q), ('\\overrightarrow{AB}\\cdot\\overrightarrow{BC}', -p * p)][k]
    P = {'A': (0, 0), 'B': (0, 3), 'C': (4, 0)}
    return dict(en='Triangle \\(ABC\\) is right-angled at \\(A\\) with \\(AB=%d\\), \\(AC=%d\\) (figure). Then \\(%s=\\)…' % (p, q, e), vi='Tam giác \\(ABC\\) vuông tại \\(A\\) có \\(AB=%d\\), \\(AC=%d\\) (hình vẽ). Khi đó \\(%s=\\)…' % (p, q, e),
                opts=nopts(r, good, [-good, p * q, h * h, p * h]), fig=PF(P, segs=[('A', 'B'), ('B', 'C'), ('C', 'A')], right=[('B', 'A', 'C')], alt='Right triangle ABC'),
                ee='Use \\(\\cos\\) of the angle at the vertex (or the projection): result \\(%d\\).' % good, ev='Dùng côsin của góc tại đỉnh (hoặc hình chiếu): kết quả \\(%d\\).' % good)

T11 = [(('\\(\\overrightarrow{AB}\\cdot\\overrightarrow{AD}=0\\).', '\\(\\overrightarrow{AB}\\cdot\\overrightarrow{AD}=0\\).'), True, ('\\(AB\\perp AD\\).', '\\(AB\\perp AD\\).')),
       (('\\(\\overrightarrow{AB}\\cdot\\overrightarrow{CD}=AB^2\\).', '\\(\\overrightarrow{AB}\\cdot\\overrightarrow{CD}=AB^2\\).'), False, ('The angle is \\(180^\\circ\\): \\(-AB^2\\).', 'Góc giữa hai vectơ là \\(180^\\circ\\): \\(-AB^2\\).')),
       (('\\(\\overrightarrow{AC}\\cdot\\overrightarrow{BD}=0\\).', '\\(\\overrightarrow{AC}\\cdot\\overrightarrow{BD}=0\\).'), False, ('The diagonals of a non-square rectangle are not perpendicular.', 'Hai đường chéo của hình chữ nhật không vuông thì không vuông góc.')),
       (('\\(\\overrightarrow{AB}\\cdot\\overrightarrow{DC}=AB^2\\).', '\\(\\overrightarrow{AB}\\cdot\\overrightarrow{DC}=AB^2\\).'), True, ('\\(\\overrightarrow{DC}=\\overrightarrow{AB}\\).', '\\(\\overrightarrow{DC}=\\overrightarrow{AB}\\).')),
       (('\\(\\overrightarrow{AD}\\cdot\\overrightarrow{BC}=AD^2\\).', '\\(\\overrightarrow{AD}\\cdot\\overrightarrow{BC}=AD^2\\).'), True, ('\\(\\overrightarrow{BC}=\\overrightarrow{AD}\\).', '\\(\\overrightarrow{BC}=\\overrightarrow{AD}\\).')),
       (('\\(\\overrightarrow{BA}\\cdot\\overrightarrow{BC}\\gt0\\).', '\\(\\overrightarrow{BA}\\cdot\\overrightarrow{BC}\\gt0\\).'), False, ('\\(BA\\perp BC\\): the product is \\(0\\).', '\\(BA\\perp BC\\): tích bằng \\(0\\).'))]
def d11_tf_rect(r, lv, ctx):
    (e, v), truth, (ee, ev) = T11[(lv - 1) % 3 * 2 + r.randrange(2)]
    return dict(en='\\(ABCD\\) is a rectangle with \\(AB\\ne AD\\) (figure). ' + e, vi='Cho hình chữ nhật \\(ABCD\\) có \\(AB\\ne AD\\) (hình vẽ). ' + v, truth=truth,
                fig=PF(RECT, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('A', 'C'), ('B', 'D')], right=[('B', 'A', 'D')], hide=('O',), alt='Rectangle ABCD'), ee=ee, ev=ev)

# ---- D, Bài 11
def d11_d_proj(r, lv, ctx):
    bh, hc = r.choice([(2, 4), (3, 5), (1, 5), (4, 2), (2, 7), (3, 3)]); bc = bh + hc; good = bh * bc
    P = {'B': (0, 0), 'C': (6, 0), 'H': (6 * bh / bc, 0)}; P['A'] = (P['H'][0], 3.2)
    return dict(en='In triangle \\(ABC\\), \\(H\\) is the foot of the altitude from \\(A\\), \\(BH=%d\\), \\(HC=%d\\) (figure). Using projections, \\(\\overrightarrow{BA}\\cdot\\overrightarrow{BC}=\\)…' % (bh, hc),
                vi='Trong tam giác \\(ABC\\), \\(H\\) là chân đường cao kẻ từ \\(A\\), \\(BH=%d\\), \\(HC=%d\\) (hình vẽ). Dùng hình chiếu, \\(\\overrightarrow{BA}\\cdot\\overrightarrow{BC}=\\)…' % (bh, hc),
                opts=nopts(r, good, [bh * hc, bc * bc, hc * bc, -good]), fig=PF(P, segs=[('A', 'B'), ('B', 'C'), ('C', 'A')], dashed=[('A', 'H')], right=[('A', 'H', 'C')], alt='Triangle ABC with the altitude AH'),
                ee='The projection of \\(\\overrightarrow{BA}\\) on \\(BC\\) is \\(\\overrightarrow{BH}\\): \\(BH\\cdot BC=%d\\cdot%d=%d\\).' % (bh, bc, good), ev='Hình chiếu của \\(\\overrightarrow{BA}\\) lên \\(BC\\) là \\(\\overrightarrow{BH}\\): \\(BH\\cdot BC=%d\\cdot%d=%d\\).' % (bh, bc, good))

def d11_d_diff(r, lv, ctx):
    a, b = r.choice([(3, 5), (2, 4), (4, 6), (3, 8), (5, 8), (2, 6)]); ang = [60, 120, 90][(lv - 1) % 3]
    c = {60: F(1, 2), 120: F(-1, 2), 90: 0}[ang]; v = a * a + b * b - 2 * a * b * c; assert F(v).denominator == 1; v = int(v)
    O = list(dict.fromkeys([M(sqt(v)), M(sqt(a * a + b * b + 2 * a * b * c)), M(str(b - a)), M(sqt(a * a + b * b)), M(str(a + b)), M(sqt(a * b))]))
    t = math.radians(ang); P = {'O': (0, 0), '_a': (3, 0), '_b': (2.6 * math.cos(t), 2.6 * math.sin(t))}
    return dict(en='\\(|\\vec a|=%d\\), \\(|\\vec b|=%d\\), \\((\\vec a,\\vec b)=%d^\\circ\\) (figure). Then \\(|\\vec a-\\vec b|=\\)…' % (a, b, ang), vi='\\(|\\vec a|=%d\\), \\(|\\vec b|=%d\\), \\((\\vec a,\\vec b)=%d^\\circ\\) (hình vẽ). Khi đó \\(|\\vec a-\\vec b|=\\)…' % (a, b, ang),
                opts=O[:4], fig=PF(P, vecs=[('O', '_a', ORANGE), ('O', '_b', BLUE)], dashed=[('_a', '_b')], vlabels=[('O', '_a', '\\vec a'), ('O', '_b', '\\vec b')], alt='Two vectors with a given angle'),
                ee='\\(|\\vec a-\\vec b|^2=%d+%d-2\\cdot%d\\cdot%d\\cos%d^\\circ=%d\\).' % (a * a, b * b, a, b, ang, v), ev='\\(|\\vec a-\\vec b|^2=%d+%d-2\\cdot%d\\cdot%d\\cos%d^\\circ=%d\\).' % (a * a, b * b, a, b, ang, v))

def d11_d_error(r, lv, ctx):
    a = r.choice([2, 4, 6, 8, 10]); e = ['\\overrightarrow{AB}\\cdot\\overrightarrow{BC}', '\\overrightarrow{BC}\\cdot\\overrightarrow{CA}', '\\overrightarrow{CA}\\cdot\\overrightarrow{AB}'][(lv - 1) % 3]
    P = {'A': (0, 0), 'B': (4, 0), 'C': (2, 2 * math.sqrt(3))}
    O = [('Wrong: the angle between the two vectors is \\(120^\\circ\\), so the result is \\(%d\\).' % (-a * a // 2), 'Sai: góc giữa hai vectơ là \\(120^\\circ\\) nên kết quả là \\(%d\\).' % (-a * a // 2)), ('Correct.', 'Đúng.'),
         ('Wrong: the result is \\(%d\\).' % (a * a), 'Sai: kết quả là \\(%d\\).' % (a * a)), ('Wrong: the result is \\(0\\).', 'Sai: kết quả là \\(0\\).')]
    return dict(en='Triangle \\(ABC\\) is equilateral with side \\(%d\\) (figure). A student wrote: \\(%s=%d\\cdot%d\\cdot\\cos60^\\circ=%d\\). Which comment is correct?' % (a, e, a, a, a * a // 2),
                vi='Tam giác \\(ABC\\) đều cạnh \\(%d\\) (hình vẽ). Một bạn viết: \\(%s=%d\\cdot%d\\cdot\\cos60^\\circ=%d\\). Nhận xét nào đúng?' % (a, e, a, a, a * a // 2),
                opts=[tt(*x) for x in O], fig=PF(P, segs=[('A', 'B'), ('B', 'C'), ('C', 'A')], alt='Equilateral triangle ABC'),
                ee='Put the two vectors at a common start: the angle is \\(180^\\circ-60^\\circ=120^\\circ\\), result \\(%d\\).' % (-a * a // 2), ev='Đặt hai vectơ chung điểm đầu: góc là \\(180^\\circ-60^\\circ=120^\\circ\\), kết quả \\(%d\\).' % (-a * a // 2))

def d11_d_acute(r, lv, ctx):
    p, q = r.choice([(1, 2), (2, 1), (1, 3), (3, 1), (2, 3)]); lo, hi = -5, 5
    good = [m for m in range(lo, hi + 1) if p * m + q > 0 and not (p * 1 == q * m)]
    n = len(good)
    qe = V(lv, ['\\(\\vec a=(%d;\\,%d)\\), \\(\\vec b=(m;\\,1)\\). How many integers \\(m\\in[%d;\\,%d]\\) make the angle between \\(\\vec a\\) and \\(\\vec b\\) acute?', 'For \\(\\vec a=(%d;\\,%d)\\) and \\(\\vec b=(m;\\,1)\\), count the integers \\(m\\) in \\([%d;\\,%d]\\) such that \\((\\vec a,\\vec b)\\lt90^\\circ\\).', 'Count the integers \\(m\\) from \\(%d\\) to \\(%d\\) with \\((\\vec a,\\vec b)\\) acute, where \\(\\vec a=(%d;\\,%d)\\), \\(\\vec b=(m;\\,1)\\).'])
    qv = V(lv, ['\\(\\vec a=(%d;\\,%d)\\), \\(\\vec b=(m;\\,1)\\). Có bao nhiêu số nguyên \\(m\\in[%d;\\,%d]\\) để góc giữa \\(\\vec a\\) và \\(\\vec b\\) là góc nhọn?', 'Với \\(\\vec a=(%d;\\,%d)\\), \\(\\vec b=(m;\\,1)\\), đếm các số nguyên \\(m\\) thuộc \\([%d;\\,%d]\\) sao cho \\((\\vec a,\\vec b)\\lt90^\\circ\\).', 'Đếm các số nguyên \\(m\\) từ \\(%d\\) đến \\(%d\\) để \\((\\vec a,\\vec b)\\) là góc nhọn, với \\(\\vec a=(%d;\\,%d)\\), \\(\\vec b=(m;\\,1)\\).'])
    args = (lo, hi, p, q) if lv == 3 else (p, q, lo, hi)
    excl = [m for m in range(lo, hi + 1) if p == q * m]
    return dict(en=qe % args, vi=qv % args, opts=nopts(r, n, [n + len(excl) if excl else n + 1, hi - lo + 1 - n, n - 1, n + 2]),
                ee='Need \\(\\vec a\\cdot\\vec b=%dm+%d\\gt0\\)%s: %d values.' % (p, q, (' and \\(\\vec b\\) not in the same direction as \\(\\vec a\\) (\\(m\\ne%s\\))' % frt(F(p, q))) if F(p, q).denominator == 1 else '', n),
                ev='Cần \\(\\vec a\\cdot\\vec b=%dm+%d\\gt0\\)%s: có %d giá trị.' % (p, q, (' và \\(\\vec b\\) không cùng hướng với \\(\\vec a\\) (\\(m\\ne%s\\))' % frt(F(p, q))) if F(p, q).denominator == 1 else '', n))

def d11_d_right(r, lv, ctx):
    for _ in range(500):
        V_ = gpt(r, -3, 3); u = r.choice([(1, 2), (2, 1), (1, -2), (2, -1), (1, 1), (3, 1)]); s1, s2 = r.choice([1, 2]), r.choice([1, 2, 3])
        P1 = vadd(V_, smul(s1, u)); P2_ = vadd(V_, smul(s2, (-u[1], u[0])))
        names = ['A', 'B', 'C']; r.shuffle(names); pts = {names[0]: V_, names[1]: P1, names[2]: P2_}
        xr, yr = box(*pts.values())
        if xr[1] - xr[0] <= 13 and yr[1] - yr[0] <= 13: break
    good = names[0]
    O = [tt('right-angled at \\(%s\\)' % x, 'vuông tại \\(%s\\)' % x) for x in [good] + [n for n in 'ABC' if n != good]] + [tt('not a right triangle', 'không phải tam giác vuông')]
    qe = V(lv, ['Triangle \\(ABC\\) is shown on the coordinate grid. Using the dot product, the triangle is…', 'Use dot products to classify triangle \\(ABC\\) on the grid. It is…', 'Read \\(A\\), \\(B\\), \\(C\\) from the grid. The triangle \\(ABC\\) is…'])
    qv = V(lv, ['Tam giác \\(ABC\\) được biểu diễn trên lưới tọa độ. Dùng tích vô hướng, tam giác đó…', 'Dùng tích vô hướng để xét tam giác \\(ABC\\) trên lưới. Tam giác đó…', 'Đọc tọa độ \\(A\\), \\(B\\), \\(C\\) trên lưới. Tam giác \\(ABC\\)…'])
    return dict(en=qe, vi=qv,
                opts=O[:1] + O[1:3] + O[3:], fig=GRID(xr, yr, pts={k: v for k, v in pts.items()}, alt='Triangle ABC on the coordinate grid'),
                ee='At \\(%s\\) the two side vectors have dot product \\(0\\).' % good, ev='Tại \\(%s\\) hai vectơ cạnh có tích vô hướng bằng \\(0\\).' % good)

def d11_d_norm(r, lv, ctx):
    a, b = r.choice([(3, 4), (2, 5), (4, 6), (5, 7), (3, 6)]); d = r.choice([-6, -4, 3, 5, 8, 10]); s2 = a * a + b * b + 2 * d
    if s2 <= 0 or not (abs(d) <= a * b): raise AssertionError
    k = (lv - 1) % 3
    if k == 1:
        s2m = a * a + b * b - 2 * d
        if s2m <= 0: raise AssertionError
        return dict(en='\\(|\\vec a|=%d\\), \\(|\\vec b|=%d\\) and \\(|\\vec a-\\vec b|^2=%d\\). Then \\(\\vec a\\cdot\\vec b=\\)…' % (a, b, s2m), vi='\\(|\\vec a|=%d\\), \\(|\\vec b|=%d\\) và \\(|\\vec a-\\vec b|^2=%d\\). Khi đó \\(\\vec a\\cdot\\vec b=\\)…' % (a, b, s2m),
                    opts=nopts(r, d, [-d, 2 * d, s2m - a * a - b * b, a * b]), ee='\\(|\\vec a-\\vec b|^2=%d+%d-2\\vec a\\cdot\\vec b\\Rightarrow\\vec a\\cdot\\vec b=%d\\).' % (a * a, b * b, d), ev='\\(|\\vec a-\\vec b|^2=%d+%d-2\\vec a\\cdot\\vec b\\Rightarrow\\vec a\\cdot\\vec b=%d\\).' % (a * a, b * b, d))
    return dict(en='\\(|\\vec a|=%d\\), \\(|\\vec b|=%d\\) and \\(|\\vec a+\\vec b|^2=%d\\). %s' % (a, b, s2, 'Then \\(\\vec a\\cdot\\vec b=\\)…' if k == 0 else 'Find the dot product \\(\\vec a\\cdot\\vec b\\).'),
                vi='\\(|\\vec a|=%d\\), \\(|\\vec b|=%d\\) và \\(|\\vec a+\\vec b|^2=%d\\). %s' % (a, b, s2, 'Khi đó \\(\\vec a\\cdot\\vec b=\\)…' if k == 0 else 'Tính tích vô hướng \\(\\vec a\\cdot\\vec b\\).'),
                opts=nopts(r, d, [-d, 2 * d, s2 - a * a - b * b, a * b]), ee='\\(|\\vec a+\\vec b|^2=%d+%d+2\\vec a\\cdot\\vec b\\Rightarrow\\vec a\\cdot\\vec b=%d\\).' % (a * a, b * b, d), ev='\\(|\\vec a+\\vec b|^2=%d+%d+2\\vec a\\cdot\\vec b\\Rightarrow\\vec a\\cdot\\vec b=%d\\).' % (a * a, b * b, d))

W11 = [(('A porter carries a box and walks along a level floor.', 'Một người khuân vác bê thùng hàng đi trên sàn nằm ngang.'), ('A horse pulls a cart forward along a level road.', 'Con ngựa kéo xe đi về phía trước trên đường nằm ngang.'), ('A person pushes a trolley up a slope.', 'Một người đẩy xe đẩy lên dốc.'), ('A crane lifts a load straight up.', 'Cần cẩu nâng vật thẳng lên.')),
       (('A satellite moves on a circle; gravity points to the center.', 'Vệ tinh chuyển động tròn; lực hấp dẫn hướng vào tâm.'), ('A ball falls vertically under gravity.', 'Quả bóng rơi thẳng đứng dưới tác dụng của trọng lực.'), ('A boy pulls a sled forward with a rope.', 'Cậu bé kéo xe trượt về phía trước bằng dây.'), ('A cyclist pedals forward.', 'Người đi xe đạp đạp xe về phía trước.')),
       (('A waiter holds a tray up while walking horizontally.', 'Người phục vụ nâng khay lên trong khi đi theo phương ngang.'), ('A worker pushes a box horizontally along the floor.', 'Công nhân đẩy thùng hàng theo phương ngang trên sàn.'), ('A lift carries people upward.', 'Thang máy chở người đi lên.'), ('Wind pushes a sailboat forward.', 'Gió đẩy thuyền buồm đi về phía trước.'))]
def d11_d_work(r, lv, ctx):
    S = W11[(lv - 1) % 3]
    qe = V(lv, ['The work of a force is \\(A=\\vec F\\cdot\\vec d\\). In which situation is the work of the named force equal to \\(0\\)? (The force is the one that holds or pulls.)', 'Work \\(A=\\vec F\\cdot\\vec d\\) equals \\(0\\) when \\(\\vec F\\perp\\vec d\\). Which situation gives zero work?', 'Choose the situation where the force does no work (\\(\\vec F\\cdot\\vec d=0\\)).'])
    qv = V(lv, ['Công của lực là \\(A=\\vec F\\cdot\\vec d\\). Trường hợp nào công của lực được nhắc tới bằng \\(0\\)? (Lực là lực nâng hoặc kéo.)', 'Công \\(A=\\vec F\\cdot\\vec d\\) bằng \\(0\\) khi \\(\\vec F\\perp\\vec d\\). Trường hợp nào cho công bằng không?', 'Chọn trường hợp lực không sinh công (\\(\\vec F\\cdot\\vec d=0\\)).'])
    return dict(en=qe, vi=qv, opts=[tt(*x) for x in S], ee='There the force is perpendicular to the displacement.', ev='Ở trường hợp đó lực vuông góc với độ dời.')

def d11_d_rect(r, lv, ctx):
    a, b = r.choice([(3, 5), (2, 4), (4, 7), (3, 6), (5, 8)]); good = b * b - a * a; k = (lv - 1) % 3
    if k == 1: good = -good; e = '\\overrightarrow{BD}\\cdot\\overrightarrow{CA}'
    else: e = '\\overrightarrow{AC}\\cdot\\overrightarrow{BD}'
    return dict(en='\\(ABCD\\) is a rectangle with \\(AB=%d\\), \\(AD=%d\\) (figure). Then \\(%s=\\)…' % (a, b, e), vi='Hình chữ nhật \\(ABCD\\) có \\(AB=%d\\), \\(AD=%d\\) (hình vẽ). Khi đó \\(%s=\\)…' % (a, b, e),
                opts=nopts(r, good, [-good, a * a + b * b, 0, a * b]), fig=PF({'A': (0, 0), 'B': (a, 0), 'C': (a, b), 'D': (0, b)}, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('A', 'C'), ('B', 'D')], right=[('B', 'A', 'D')], alt='Rectangle ABCD with its diagonals'),
                ee='\\(\\overrightarrow{AC}=\\overrightarrow{AB}+\\overrightarrow{AD}\\), \\(\\overrightarrow{BD}=\\overrightarrow{AD}-\\overrightarrow{AB}\\): \\(\\overrightarrow{AC}\\cdot\\overrightarrow{BD}=AD^2-AB^2=%d\\).' % (b * b - a * a),
                ev='\\(\\overrightarrow{AC}=\\overrightarrow{AB}+\\overrightarrow{AD}\\), \\(\\overrightarrow{BD}=\\overrightarrow{AD}-\\overrightarrow{AB}\\): \\(\\overrightarrow{AC}\\cdot\\overrightarrow{BD}=AD^2-AB^2=%d\\).' % (b * b - a * a))

B11 = dict(A=[d11_square, d11_righttri], B=[d11_tf_rect], C=[], D=[d11_d_proj, d11_d_diff, d11_d_error, d11_d_acute, d11_d_right, d11_d_norm, d11_d_work, d11_d_rect])
