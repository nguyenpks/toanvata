# -*- coding: utf-8 -*-
"""Ngân hàng câu hỏi Toán 9 (KNTT) – Bài 28–30 (đường tròn ngoại tiếp, nội tiếp; tứ giác nội tiếp; đa giác đều),
Bài 31–32 (hình trụ, hình nón, hình cầu). Dùng chung BANK/ABCD_TITLES của sp_g9; hình tĩnh TikZ → SVG.
Mọi đáp án tính bằng số nguyên/Fraction từ chính dữ liệu sinh ra. Phần D dùng dạng câu khác phần A–C."""
import math, random
from fractions import Fraction as F
from sp_g9 import tx, dm, pick_opts
from sp_g9p import img, cfig, CFIG, A, deg, degv, dopts, pe, pv, _unit
from sp_g9s import iopts
from mb_pgf import texsvg, col
from fig2d import Canvas

PYT = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15), (12, 16, 20), (7, 24, 25), (20, 21, 29)]
SQ = lambda n: '\\sqrt%d' % n if n < 10 else '\\sqrt{%d}' % n


def surd(k, n, unit='cm'):
    """k√n (n = 1 ⇒ k); k có thể là phân số."""
    k = F(k); u = '\\text{ %s}' % unit if unit else ''
    if n == 1: return '%s%s' % (frac(k), u)
    if k == 1: return '%s%s' % (SQ(n), u)
    if k.denominator == 1: return '%d%s%s' % (k.numerator, SQ(n), u)
    return '\\dfrac{%s%s}{%d}%s' % ('' if k.numerator == 1 else k.numerator, SQ(n), k.denominator, u)


def frac(x):
    x = F(x)
    if x.denominator == 1: return str(x.numerator)
    return '\\dfrac{%d}{%d}' % (x.numerator, x.denominator)


def pi(k, unit='cm', p=1):
    """kπ (đơn vị mũ p)."""
    k = F(k); u = ('\\text{ %s}' % unit if p == 1 else '\\text{ %s}^%d' % (unit, p)) if unit else ''
    if k == 1: s = '\\pi'
    elif k.denominator == 1: s = '%d\\pi' % k.numerator
    else: s = '\\dfrac{%d\\pi}{%d}' % (k.numerator, k.denominator)
    return s + u


def piopts(r, good, bads, unit='cm', p=2):
    good = F(good)
    o = pick_opts(r, pi(good, unit, p), [pi(b, unit, p) for b in bads if F(b) > 0 and F(b) != good], fill=lambda k: pi(good + k, unit, p))
    return o


def sopts(r, good, bads, unit='cm'):
    """good, bads: (k, n) dạng k√n."""
    return pick_opts(r, surd(*good, unit=unit), [surd(*b, unit=unit) for b in bads if b != good and F(b[0]) > 0],
                     fill=lambda j: surd(F(good[0]) + j, good[1], unit=unit))


def cm(v, unit='cm'): return '%s\\text{ %s}' % (pe(v), unit)


def nopts(r, good, bads, unit='cm'):
    return pick_opts(r, tx('\\(%s\\)' % cm(good, unit), '\\(%s\\)' % dm(cm(good, unit))),
                     [tx('\\(%s\\)' % cm(b, unit), '\\(%s\\)' % dm(cm(b, unit))) for b in bads if F(b) != F(good) and F(b) > 0],
                     fill=lambda j: tx('\\(%s\\)' % cm(F(good) + j, unit), '\\(%s\\)' % dm(cm(F(good) + j, unit))))


# =====================================================================================================
# HÌNH TAM GIÁC VÀ ĐƯỜNG TRÒN (tĩnh): nhãn đặt ra ngoài, tránh nét; góc vuông bằng ô vuông
# =====================================================================================================
def tfig(P, circles=(), segs=(), dash=(), right=(), dots=(), px=300):
    """P: {tên: (x, y)}; circles: [(cx, cy, r)]; segs/dash: [(A, B)]; right: [(A, V, B)]; dots: tên các điểm vẽ chấm."""
    c = Canvas(); G = sum(p[0] for p in P.values()) / len(P), sum(p[1] for p in P.values()) / len(P)
    for cx, cy, rr in circles:
        ring = [(cx + rr * math.cos(2 * math.pi * i / 160), cy + rr * math.sin(2 * math.pi * i / 160)) for i in range(161)]
        c.seg_only(ring); c.o.append('\\draw[color=%s, line width=1.1pt] (%.3f,%.3f) circle (%.3f);' % (col('046b4d'), cx, cy, rr))
    for a, b in segs: c.poly([P[a], P[b]], 'ink, line width=0.85pt')
    for a, b in dash: c.poly([P[a], P[b]], 'ink, line width=0.7pt, dash pattern=on 3.5pt off 2.5pt')
    for a, v, b in right:
        V = P[v]; u1 = _unit(V, P[a]); u2 = _unit(V, P[b]); s = 0.22
        q1 = (V[0] + s * u1[0], V[1] + s * u1[1]); q2 = (V[0] + s * u2[0], V[1] + s * u2[1]); q3 = (q1[0] + s * u2[0], q1[1] + s * u2[1])
        c.poly([q1, q3, q2], 'ink, line width=0.7pt')
    for k in (dots or P.keys()): c.dot(*P[k], color='1f2937')
    for k, (x, y) in P.items():
        dx, dy = x - G[0], y - G[1]; L = math.hypot(dx, dy) or 1; base = math.atan2(dy, dx)
        cands = [(0.34 * math.cos(base + da), 0.34 * math.sin(base + da)) for da in (0, .35, -.35, .8, -.8, 1.3, -1.3, 2.0, -2.0, math.pi)]
        c.label(x, y, '$%s$' % k.replace("1", "'"), 0.3, 0.36, cands)
    return c.svg()


def TFIG(**kw):
    fn = tfig(**kw); return (img(fn, 'Figure', 280), img(fn, 'Hình vẽ', 280))


def circum(A_, B_, C_):
    ax, ay = A_; bx, by = B_; cx, cy = C_
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
    uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
    return ux, uy, math.hypot(ax - ux, ay - uy)


def incircle(A_, B_, C_):
    a = math.dist(B_, C_); b = math.dist(A_, C_); c = math.dist(A_, B_); p = a + b + c
    ix = (a * A_[0] + b * B_[0] + c * C_[0]) / p; iy = (a * A_[1] + b * B_[1] + c * C_[1]) / p
    s = p / 2; area = math.sqrt(s * (s - a) * (s - b) * (s - c)); return ix, iy, area / s


TRI = ['ABC', 'MNP', 'DEF', 'HIK']


# =====================================================================================================
# BÀI 28. Đường tròn ngoại tiếp và đường tròn nội tiếp của một tam giác
# =====================================================================================================
def b28_center(r, lv):
    k = r.choice(['out', 'in']); T = r.choice(TRI)
    if k == 'out':
        o = [tx('the three perpendicular bisectors of the sides', 'ba đường trung trực của ba cạnh'), tx('the three angle bisectors', 'ba đường phân giác'),
             tx('the three medians', 'ba đường trung tuyến'), tx('the three altitudes', 'ba đường cao')]
        return dict(en='The center of the circumcircle of triangle \\(%s\\) is the point where … meet.' % T, vi='Tâm đường tròn ngoại tiếp tam giác \\(%s\\) là giao điểm của …' % T, opts=o, ans=0,
                    ee='The circumcenter is equidistant from the three vertices, so it lies on the three perpendicular bisectors.', ev='Tâm đường tròn ngoại tiếp cách đều ba đỉnh nên nằm trên ba đường trung trực.')
    o = [tx('the three angle bisectors', 'ba đường phân giác trong'), tx('the three perpendicular bisectors of the sides', 'ba đường trung trực của ba cạnh'),
         tx('the three medians', 'ba đường trung tuyến'), tx('the three altitudes', 'ba đường cao')]
    return dict(en='The center of the incircle of triangle \\(%s\\) is the point where … meet.' % T, vi='Tâm đường tròn nội tiếp tam giác \\(%s\\) là giao điểm của …' % T, opts=o, ans=0,
                ee='The incenter is equidistant from the three sides, so it lies on the three angle bisectors.', ev='Tâm đường tròn nội tiếp cách đều ba cạnh nên nằm trên ba đường phân giác trong.')


def b28_right(r, lv):
    a, b, c = r.choice(PYT); k = r.choice([1, 1, 2]); a, b, c = a * k, b * k, c * k
    if c > 40: raise AssertionError
    R = F(c, 2)
    return dict(en='Triangle \\(ABC\\) is right-angled at \\(A\\), \\(AB=%d\\) cm, \\(AC=%d\\) cm. Find the radius of its circumcircle.' % (a, b),
                vi='Tam giác \\(ABC\\) vuông tại \\(A\\) có \\(AB=%d\\) cm, \\(AC=%d\\) cm. Tính bán kính đường tròn ngoại tiếp tam giác đó.' % (a, b),
                opts=nopts(r, R, [c, F(a + b, 2), F(a * b, c), F(a + b - c, 2)]), ans=0,
                ee='\\(BC=\\sqrt{%d^2+%d^2}=%d\\); the center is the midpoint of the hypotenuse, \\(R=\\dfrac{BC}{2}=%s\\) cm.' % (a, b, c, pe(R)),
                ev='\\(BC=\\sqrt{%d^2+%d^2}=%d\\); tâm là trung điểm cạnh huyền, \\(R=\\dfrac{BC}{2}=%s\\) cm.' % (a, b, c, dm(pe(R))))


def b28_equil(r, lv):
    k = r.randint(1, 8); a = 3 * k; which = r.choice(['R', 'r'])
    good = (k, 3) if which == 'R' else (F(k, 2), 3)
    return dict(en='An equilateral triangle has side %d cm. Find the radius of its %s.' % (a, 'circumcircle' if which == 'R' else 'incircle'),
                vi='Tam giác đều có cạnh %d cm. Tính bán kính đường tròn %s của tam giác.' % (a, 'ngoại tiếp' if which == 'R' else 'nội tiếp'),
                opts=sopts(r, good, [(F(k, 2), 3) if which == 'R' else (k, 3), (F(3 * k, 2), 3), (k, 2), (F(3 * k, 2), 1)]), ans=0,
                ee='\\(R=\\dfrac{a\\sqrt3}{3}\\), \\(r=\\dfrac{a\\sqrt3}{6}\\) with \\(a=%d\\): \\(%s=%s\\).' % (a, which, surd(*good)),
                ev='\\(R=\\dfrac{a\\sqrt3}{3}\\), \\(r=\\dfrac{a\\sqrt3}{6}\\) với \\(a=%d\\): \\(%s=%s\\).' % (a, which, surd(*good)))


def b28_tf_equi(r, lv):
    T = r.choice(TRI); k = r.choice(['out', 'in', 'both']); truth = r.random() < 0.5
    if k == 'out':
        claim = ('vertices', 'ba đỉnh') if truth else ('sides', 'ba cạnh')
        return dict(en='The center \\(O\\) of the circumcircle of triangle \\(%s\\) is equidistant from its three %s.' % (T, claim[0]),
                    vi='Tâm \\(O\\) của đường tròn ngoại tiếp tam giác \\(%s\\) cách đều %s của tam giác.' % (T, claim[1]), ans=truth,
                    ee='\\(O\\) is equidistant from the three vertices (\\(OA=OB=OC=R\\)), not in general from the sides.', ev='\\(O\\) cách đều ba đỉnh (\\(OA=OB=OC=R\\)); nói chung không cách đều ba cạnh.')
    if k == 'in':
        claim = ('sides', 'ba cạnh') if truth else ('vertices', 'ba đỉnh')
        return dict(en='The center \\(I\\) of the incircle of triangle \\(%s\\) is equidistant from its three %s.' % (T, claim[0]),
                    vi='Tâm \\(I\\) của đường tròn nội tiếp tam giác \\(%s\\) cách đều %s của tam giác.' % (T, claim[1]), ans=truth,
                    ee='\\(I\\) is equidistant from the three sides (the distance is \\(r\\)), not in general from the vertices.', ev='\\(I\\) cách đều ba cạnh (khoảng cách bằng \\(r\\)); nói chung không cách đều ba đỉnh.')
    claim = 2 if truth else r.choice([3, F(3, 2), F(1, 2)])
    return dict(en='In an equilateral triangle \\(%s\\), the circumradius is %s times the inradius.' % (T, pe(claim)),
                vi='Trong tam giác đều \\(%s\\), bán kính đường tròn ngoại tiếp gấp %s lần bán kính đường tròn nội tiếp.' % (T, pv(claim)), ans=truth,
                ee='\\(R=\\dfrac{a\\sqrt3}{3}=2\\cdot\\dfrac{a\\sqrt3}{6}=2r\\).', ev='\\(R=\\dfrac{a\\sqrt3}{3}=2\\cdot\\dfrac{a\\sqrt3}{6}=2r\\).')


def b28_tf_mid(r, lv):
    a, b, c = r.choice(PYT); truth = r.random() < 0.5; claim = F(c, 2) if truth else r.choice([F(a, 2), F(b, 2), F(c)])
    if claim == F(c, 2): truth = True
    return dict(en='A right triangle has legs %d cm and %d cm. The radius of its circumcircle is \\(%s\\) cm.' % (a, b, pe(claim)),
                vi='Một tam giác vuông có hai cạnh góc vuông %d cm và %d cm. Bán kính đường tròn ngoại tiếp tam giác đó là \\(%s\\) cm.' % (a, b, dm(pe(claim))), ans=truth,
                ee='Hypotenuse \\(%d\\) cm; \\(R=%s\\) cm.' % (c, pe(F(c, 2))), ev='Cạnh huyền \\(%d\\) cm; \\(R=%s\\) cm.' % (c, dm(pe(F(c, 2)))))


def b28_short_hyp(r, lv):
    a, b, c = r.choice(PYT)
    return dict(en='Triangle \\(MNP\\) is right-angled at \\(M\\) with \\(MN=%d\\) cm and \\(MP=%d\\) cm. Find the radius (cm) of its circumcircle.' % (a, b),
                vi='Tam giác \\(MNP\\) vuông tại \\(M\\) có \\(MN=%d\\) cm, \\(MP=%d\\) cm. Tính bán kính (cm) đường tròn ngoại tiếp tam giác.' % (a, b), key=pe(F(c, 2)),
                hint=('Enter a number (e.g. 6.5).', 'Nhập một số (ví dụ 6,5).'),
                ee='\\(NP=%d\\), \\(R=\\dfrac{NP}{2}=%s\\).' % (c, pe(F(c, 2))), ev='\\(NP=%d\\), \\(R=\\dfrac{NP}{2}=%s\\).' % (c, dm(pe(F(c, 2)))))


def b28_short_rR(r, lv):
    k = r.randint(2, 15); which = r.choice(['r2R', 'R2r'])
    if which == 'r2R':
        return dict(en='An equilateral triangle has inradius %d cm. Find its circumradius (cm).' % k, vi='Một tam giác đều có bán kính đường tròn nội tiếp %d cm. Tính bán kính đường tròn ngoại tiếp (cm).' % k,
                    key=str(2 * k), ee='\\(R=2r=%d\\).' % (2 * k), ev='\\(R=2r=%d\\).' % (2 * k))
    return dict(en='An equilateral triangle has circumradius %d cm. Find its inradius (cm).' % (2 * k), vi='Một tam giác đều có bán kính đường tròn ngoại tiếp %d cm. Tính bán kính đường tròn nội tiếp (cm).' % (2 * k),
                key=str(k), ee='\\(r=\\dfrac{R}{2}=%d\\).' % k, ev='\\(r=\\dfrac{R}{2}=%d\\).' % k)


def b28_d1_inscribed(r, lv):
    T = r.choice(TRI); k = r.choice(['circ', 'inc'])
    if k == 'circ':
        o = [tx('its three vertices lie on the circle', 'ba đỉnh của tam giác nằm trên đường tròn'), tx('its three sides touch the circle', 'ba cạnh của tam giác tiếp xúc với đường tròn'),
             tx('the circle lies inside the triangle', 'đường tròn nằm trong tam giác'), tx('its center is a vertex', 'tâm là một đỉnh của tam giác')]
        return dict(en='Triangle \\(%s\\) is inscribed in a circle (the circle is its circumcircle) when…' % T, vi='Tam giác \\(%s\\) nội tiếp đường tròn (đường tròn ngoại tiếp tam giác) khi…' % T, opts=o, ans=0,
                    ee='The circumcircle passes through the three vertices.', ev='Đường tròn ngoại tiếp đi qua ba đỉnh của tam giác.')
    o = [tx('it touches all three sides', 'tiếp xúc với cả ba cạnh'), tx('it passes through the three vertices', 'đi qua ba đỉnh'), tx('its center is the midpoint of a side', 'có tâm là trung điểm một cạnh'), tx('it passes through the midpoints of the sides', 'đi qua trung điểm ba cạnh')]
    return dict(en='The incircle of triangle \\(%s\\) is the circle that…' % T, vi='Đường tròn nội tiếp tam giác \\(%s\\) là đường tròn…' % T, opts=o, ans=0,
                ee='The incircle lies inside the triangle and touches all three sides.', ev='Đường tròn nội tiếp nằm trong tam giác và tiếp xúc với ba cạnh.')


def b28_d1_rightc(r, lv):
    T = r.choice(['ABC', 'DEF', 'MNP']); v = T[0]; h = T[1:]
    o = [tx('the midpoint of \\(%s\\)' % h, 'trung điểm của \\(%s\\)' % h), tx('the vertex \\(%s\\)' % v, 'đỉnh \\(%s\\)' % v), tx('the midpoint of \\(%s%s\\)' % (v, h[0]), 'trung điểm của \\(%s%s\\)' % (v, h[0])), tx('a point outside the triangle', 'một điểm nằm ngoài tam giác')]
    return dict(en='Triangle \\(%s\\) is right-angled at \\(%s\\). The center of its circumcircle is…' % (T, v), vi='Tam giác \\(%s\\) vuông tại \\(%s\\). Tâm đường tròn ngoại tiếp tam giác là…' % (T, v), opts=o, ans=0,
                ee='The right angle subtends a semicircle, so \\(%s\\) is a diameter.' % h, ev='Góc vuông chắn nửa đường tròn nên \\(%s\\) là đường kính.' % h)


def b28_d1_formula(r, lv):
    a = r.choice([4, 6, 8, 10, 12])
    k = r.choice(['R', 'r', 'h'])
    if k == 'R': o = ['R=\\dfrac{a\\sqrt3}{3}', 'R=\\dfrac{a\\sqrt3}{6}', 'R=\\dfrac{a\\sqrt3}{2}', 'R=a\\sqrt3']; en, vi = 'circumradius \\(R\\)', 'bán kính đường tròn ngoại tiếp \\(R\\)'
    elif k == 'r': o = ['r=\\dfrac{a\\sqrt3}{6}', 'r=\\dfrac{a\\sqrt3}{3}', 'r=\\dfrac{a\\sqrt3}{2}', 'r=\\dfrac{a}{2}']; en, vi = 'inradius \\(r\\)', 'bán kính đường tròn nội tiếp \\(r\\)'
    else: o = ['h=\\dfrac{a\\sqrt3}{2}', 'h=\\dfrac{a\\sqrt3}{3}', 'h=\\dfrac{a\\sqrt2}{2}', 'h=a\\sqrt3']; en, vi = 'height \\(h\\)', 'đường cao \\(h\\)'
    return dict(en='For an equilateral triangle with side \\(a\\), the %s is…' % en, vi='Với tam giác đều cạnh \\(a\\), %s là…' % vi, opts=o, ans=0,
                ee='\\(h=\\dfrac{a\\sqrt3}{2}\\), \\(R=\\dfrac23h=\\dfrac{a\\sqrt3}{3}\\), \\(r=\\dfrac13h=\\dfrac{a\\sqrt3}{6}\\).', ev='\\(h=\\dfrac{a\\sqrt3}{2}\\), \\(R=\\dfrac23h=\\dfrac{a\\sqrt3}{3}\\), \\(r=\\dfrac13h=\\dfrac{a\\sqrt3}{6}\\).')


def b28_d2_where(r, lv):
    a = r.randint(30, 80); b = r.randint(20, 80); c = 180 - a - b
    if c <= 10 or 90 in (a, b, c): raise AssertionError
    k = r.choice(['acute', 'obtuse', 'right'])
    if k == 'right': a, b, c = 90, r.randint(25, 65), 0; c = 180 - a - b
    elif k == 'obtuse': a = r.randint(100, 140); b = r.randint(15, 180 - a - 15); c = 180 - a - b
    else:
        if max(a, b, c) >= 90: raise AssertionError
    mx = max(a, b, c)
    good = ('inside the triangle', 'nằm bên trong tam giác') if mx < 90 else ('at the midpoint of the longest side', 'là trung điểm của cạnh lớn nhất') if mx == 90 else ('outside the triangle', 'nằm bên ngoài tam giác')
    alls = [('inside the triangle', 'nằm bên trong tam giác'), ('at the midpoint of the longest side', 'là trung điểm của cạnh lớn nhất'), ('outside the triangle', 'nằm bên ngoài tam giác'), ('at a vertex of the triangle', 'trùng với một đỉnh của tam giác')]
    o = [tx(*good)] + [tx(*x) for x in alls if x != good]
    return dict(en='Triangle \\(ABC\\) has angles \\(%d^\\circ\\), \\(%d^\\circ\\), \\(%d^\\circ\\). The center of its circumcircle is…' % (a, b, c),
                vi='Tam giác \\(ABC\\) có ba góc \\(%d^\\circ\\), \\(%d^\\circ\\), \\(%d^\\circ\\). Tâm đường tròn ngoại tiếp tam giác…' % (a, b, c), opts=o, ans=0,
                ee='Acute triangle: inside; right triangle: midpoint of the hypotenuse; obtuse triangle: outside.', ev='Tam giác nhọn: tâm ở trong; tam giác vuông: trung điểm cạnh huyền; tam giác tù: tâm ở ngoài.')


def b28_d2_area(r, lv):
    a, b, c = r.choice(PYT[:6]); k = r.choice(['area', 'len'])
    if k == 'area':
        g = F(c * c, 4)
        return dict(en='A right triangle has legs %d cm and %d cm. Find the area of the disk bounded by its circumcircle.' % (a, b), vi='Tam giác vuông có hai cạnh góc vuông %d cm và %d cm. Tính diện tích hình tròn ngoại tiếp tam giác.' % (a, b),
                    opts=piopts(r, g, [c * c, F(c, 2), F(a * b, 2), F(c * c, 2)]), ans=0, ee='\\(R=\\dfrac{%d}{2}\\); \\(S=\\pi R^2=%s\\).' % (c, pi(g, 'cm', 2)), ev='\\(R=\\dfrac{%d}{2}\\); \\(S=\\pi R^2=%s\\).' % (c, pi(g, 'cm', 2)))
    return dict(en='A right triangle has legs %d cm and %d cm. Find the length (circumference) of its circumcircle.' % (a, b), vi='Tam giác vuông có hai cạnh góc vuông %d cm và %d cm. Tính độ dài đường tròn ngoại tiếp tam giác.' % (a, b),
                opts=piopts(r, c, [2 * c, F(c, 2), a + b], p=1), ans=0, ee='\\(C=2\\pi R=\\pi\\cdot%d=%s\\).' % (c, pi(c)), ev='\\(C=2\\pi R=\\pi\\cdot%d=%s\\).' % (c, pi(c)))


def b28_d2_height(r, lv):
    k = r.randint(1, 10); h = 3 * k; which = r.choice(['R', 'r'])
    good = 2 * k if which == 'R' else k
    return dict(en='An equilateral triangle has height %d cm. Find the radius of its %s.' % (h, 'circumcircle' if which == 'R' else 'incircle'),
                vi='Tam giác đều có đường cao %d cm. Tính bán kính đường tròn %s của tam giác.' % (h, 'ngoại tiếp' if which == 'R' else 'nội tiếp'),
                opts=nopts(r, good, [k if which == 'R' else 2 * k, h, F(h, 2)]), ans=0,
                ee='The center divides the height in the ratio \\(2:1\\): \\(R=\\dfrac23h=%d\\), \\(r=\\dfrac13h=%d\\).' % (2 * k, k), ev='Tâm chia đường cao theo tỉ số \\(2:1\\): \\(R=\\dfrac23h=%d\\), \\(r=\\dfrac13h=%d\\).' % (2 * k, k))


def b28_d3_iso(r, lv):
    a = r.randint(2, 12)
    return dict(en='Triangle \\(ABC\\) is right-angled and isosceles at \\(A\\) with \\(AB=AC=%d\\) cm. Find the radius of its circumcircle.' % a,
                vi='Tam giác \\(ABC\\) vuông cân tại \\(A\\) có \\(AB=AC=%d\\) cm. Tính bán kính đường tròn ngoại tiếp tam giác.' % a,
                opts=sopts(r, (F(a, 2), 2), [(a, 2), (F(a, 2), 1), (F(a, 2), 3)]), ans=0,
                ee='\\(BC=%d\\sqrt2\\), \\(R=\\dfrac{BC}{2}=%s\\).' % (a, surd(F(a, 2), 2)), ev='\\(BC=%d\\sqrt2\\), \\(R=\\dfrac{BC}{2}=%s\\).' % (a, surd(F(a, 2), 2)),
                fig=TFIG(P={'A': (0, 0), 'B': (2, 0), 'C': (0, 2), 'O': (1, 1)}, circles=[(1, 1, math.sqrt(2))], segs=[('A', 'B'), ('B', 'C'), ('C', 'A')], dash=[('O', 'A')], right=[('B', 'A', 'C')]))


def b28_d3_side(r, lv):
    k = r.randint(1, 9); which = r.choice(['R', 'r'])
    if which == 'R':
        a = (k, 3); en, vi = 'circumradius \\(R=%d\\) cm' % k, 'bán kính đường tròn ngoại tiếp \\(R=%d\\) cm' % k
        ee = '\\(a=R\\sqrt3=%s\\).' % surd(k, 3)
    else:
        a = (2 * k, 3); en, vi = 'inradius \\(r=%d\\) cm' % k, 'bán kính đường tròn nội tiếp \\(r=%d\\) cm' % k
        ee = '\\(a=2r\\sqrt3=%s\\).' % surd(2 * k, 3)
    return dict(en='An equilateral triangle has %s. Find its side.' % en, vi='Tam giác đều có %s. Tính độ dài cạnh.' % vi,
                opts=sopts(r, a, [(k, 2), (3 * k, 1), (F(k, 3), 3), (2 * a[0], 3)]), ans=0, ee=ee, ev=ee)


def b28_d3_obtuse(r, lv):
    """Tam giác cân ABC (AB = AC), góc ở đỉnh A; tâm O đường tròn ngoại tiếp: góc BOC = 2A (A nhọn)."""
    x = r.choice(range(30, 81, 2))
    return dict(en='Triangle \\(ABC\\) is inscribed in \\((O)\\) and \\(%s=%d^\\circ\\). Find \\(%s\\).' % (A('BAC'), x, A('BOC')),
                vi='Tam giác \\(ABC\\) nội tiếp đường tròn \\((O)\\) và \\(%s=%d^\\circ\\). Tính \\(%s\\).' % (A('BAC'), x, A('BOC')),
                opts=dopts(r, 2 * x, [x, 180 - x, 90 + x // 2, 180 - 2 * x]), ans=0,
                ee='\\(%s\\) is the central angle intercepting the same arc \\(BC\\) as the inscribed angle \\(%s\\): \\(2\\cdot%d^\\circ=%d^\\circ\\).' % (A('BOC'), A('BAC'), x, 2 * x),
                ev='\\(%s\\) là góc ở tâm chắn cùng cung \\(BC\\) với góc nội tiếp \\(%s\\): \\(2\\cdot%d^\\circ=%d^\\circ\\).' % (A('BOC'), A('BAC'), x, 2 * x))


def b28_d4_lamp(r, lv):
    a, b, c = r.choice(PYT[:7]); u = r.choice([1, 2]) if c <= 15 else 1; a, b, c = a * u, b * u, c * u
    return dict(en='A garden has the shape of a right triangle \\(ABC\\) (right angle at \\(A\\)), \\(AB=%d\\) m, \\(AC=%d\\) m. A lamp must be equally far from \\(A\\), \\(B\\), \\(C\\). Where is it, and how far from each corner?' % (a, b),
                vi='Một khu vườn có dạng tam giác vuông \\(ABC\\) (vuông tại \\(A\\)), \\(AB=%d\\) m, \\(AC=%d\\) m. Cần đặt một đèn chiếu cách đều ba góc vườn \\(A\\), \\(B\\), \\(C\\). Đặt đèn ở đâu và cách mỗi góc bao xa?' % (a, b),
                opts=[tx('at the midpoint of \\(BC\\), \\(%s\\) m' % pe(F(c, 2)), 'tại trung điểm \\(BC\\), cách \\(%s\\) m' % dm(pe(F(c, 2)))), tx('at the midpoint of \\(BC\\), \\(%d\\) m' % c, 'tại trung điểm \\(BC\\), cách \\(%d\\) m' % c),
                      tx('at the incenter, \\(%s\\) m' % pe(F(a + b - c, 2)), 'tại tâm đường tròn nội tiếp, cách \\(%s\\) m' % dm(pe(F(a + b - c, 2)))), tx('at the vertex \\(A\\), \\(%s\\) m' % pe(F(c, 2)), 'tại góc \\(A\\), cách \\(%s\\) m' % dm(pe(F(c, 2))))], ans=0,
                ee='Equally far from the three vertices: the circumcenter = midpoint of the hypotenuse \\(BC=%d\\); distance \\(R=%s\\) m.' % (c, pe(F(c, 2))),
                ev='Cách đều ba đỉnh: tâm đường tròn ngoại tiếp = trung điểm cạnh huyền \\(BC=%d\\); khoảng cách \\(R=%s\\) m.' % (c, dm(pe(F(c, 2)))))


def b28_d4_bed(r, lv):
    k = r.randint(1, 6); a = 6 * k; rr = (k, 3); area = 3 * k * k
    return dict(en='A yard has the shape of an equilateral triangle with side %d m. What is the area of the largest round flower bed that fits inside the yard?' % a,
                vi='Một sân có dạng tam giác đều cạnh %d m. Tính diện tích bồn hoa hình tròn lớn nhất đặt được trong sân.' % a,
                opts=piopts(r, area, [12 * k * k, 9 * k * k, 6 * k * k], unit='m'), ans=0,
                ee='The largest circle is the incircle: \\(r=\\dfrac{%d\\sqrt3}{6}=%s\\); \\(S=\\pi r^2=%s\\).' % (a, surd(k, 3, 'm'), pi(area, 'm', 2)),
                ev='Hình tròn lớn nhất là hình tròn nội tiếp: \\(r=\\dfrac{%d\\sqrt3}{6}=%s\\); \\(S=\\pi r^2=%s\\).' % (a, surd(k, 3, 'm'), pi(area, 'm', 2)))


def b28_d4_perim(r, lv):
    R = r.randint(2, 12)
    return dict(en='An equilateral triangle is inscribed in a circle of radius %d cm. Find its perimeter.' % R, vi='Một tam giác đều nội tiếp đường tròn bán kính %d cm. Tính chu vi tam giác.' % R,
                opts=sopts(r, (3 * R, 3), [(R, 3), (3 * R, 1), (6 * R, 1), (3 * R, 2)]), ans=0,
                ee='\\(a=R\\sqrt3=%s\\); perimeter \\(3a=%s\\).' % (surd(R, 3), surd(3 * R, 3)), ev='\\(a=R\\sqrt3=%s\\); chu vi \\(3a=%s\\).' % (surd(R, 3), surd(3 * R, 3)))


L28_GROUPS = [[('mcq', b28_center), ('mcq', b28_right), ('mcq', b28_equil)], [('tf', b28_tf_equi), ('tf', b28_tf_mid)], [('short', b28_short_hyp), ('short', b28_short_rR)],
              [('mcq', b28_d1_inscribed), ('mcq', b28_d1_rightc), ('mcq', b28_d1_formula)], [('mcq', b28_d2_where), ('mcq', b28_d2_area), ('mcq', b28_d2_height)],
              [('mcq', b28_d3_iso), ('mcq', b28_d3_side), ('mcq', b28_d3_obtuse)], [('mcq', b28_d4_lamp), ('mcq', b28_d4_bed), ('mcq', b28_d4_perim)]]


# =====================================================================================================
# BÀI 29. Tứ giác nội tiếp
# =====================================================================================================
QN = ['ABCD', 'MNPQ', 'EFGH']


def _quad(r):
    a = r.randint(95, 135); b = r.randint(195, 235); c = r.randint(290, 330); d = r.randint(20, 70); return a, b, c, d


def b29_opp(r, lv):
    Q = r.choice(QN); x = r.randint(50, 130); i = r.randrange(2)
    v, w = (Q[0], Q[2]) if i == 0 else (Q[1], Q[3])
    pa = _quad(r); pts = dict(zip(Q, pa))
    return dict(en='\\(%s\\) is a cyclic quadrilateral and \\(\\widehat{%s}=%d^\\circ\\). Find \\(\\widehat{%s}\\).' % (Q, v, x, w),
                vi='\\(%s\\) là tứ giác nội tiếp và \\(\\widehat{%s}=%d^\\circ\\). Tính \\(\\widehat{%s}\\).' % (Q, v, x, w),
                opts=dopts(r, 180 - x, [x, 360 - x, 90 - x // 2 if x < 90 else x - 90, 180 - x + 10]), ans=0,
                ee='Opposite angles of a cyclic quadrilateral add up to \\(180^\\circ\\): \\(180^\\circ-%d^\\circ=%d^\\circ\\).' % (x, 180 - x),
                ev='Trong tứ giác nội tiếp, tổng hai góc đối bằng \\(180^\\circ\\): \\(180^\\circ-%d^\\circ=%d^\\circ\\).' % (x, 180 - x),
                fig=CFIG(pts=pts, segs=[(Q[0], Q[1]), (Q[1], Q[2]), (Q[2], Q[3]), (Q[3], Q[0])], O=False))


def b29_which(r, lv):
    k = r.choice(['always', 'not'])
    yes = [('a rectangle', 'hình chữ nhật'), ('a square', 'hình vuông'), ('an isosceles trapezoid', 'hình thang cân')]
    no = [('a rhombus that is not a square', 'hình thoi không phải hình vuông'), ('a parallelogram that is not a rectangle', 'hình bình hành không phải hình chữ nhật'), ('a right trapezoid', 'hình thang vuông')]
    if k == 'always':
        g = r.choice(yes); o = [tx(*g)] + [tx(*x) for x in no]
        st = r.choice([('Which quadrilateral is always cyclic (inscribed in a circle)?', 'Tứ giác nào sau đây luôn nội tiếp được một đường tròn?'),
                       ('Which of these quadrilaterals can always be inscribed in a circle?', 'Trong các tứ giác sau, tứ giác nào luôn nội tiếp được đường tròn?')])
        return dict(en=st[0], vi=st[1], opts=o, ans=0,
                    ee='%s has two pairs of opposite angles adding up to \\(180^\\circ\\).' % g[0].capitalize(), ev='%s có tổng hai góc đối bằng \\(180^\\circ\\).' % (g[1][0].upper() + g[1][1:]))
    g = r.choice(no); o = [tx(*g)] + [tx(*x) for x in yes]
    return dict(en='Which quadrilateral is NOT always cyclic?', vi='Tứ giác nào sau đây KHÔNG phải lúc nào cũng nội tiếp được đường tròn?', opts=o, ans=0,
                ee='In %s two opposite angles need not add up to \\(180^\\circ\\).' % g[0], ev='Ở %s, tổng hai góc đối không nhất thiết bằng \\(180^\\circ\\).' % g[1])


def b29_rect(r, lv):
    a, b, c = r.choice(PYT[:7])
    return dict(en='A rectangle has sides %d cm and %d cm. Find the radius of its circumcircle.' % (a, b), vi='Hình chữ nhật có hai cạnh %d cm và %d cm. Tính bán kính đường tròn ngoại tiếp hình chữ nhật.' % (a, b),
                opts=nopts(r, F(c, 2), [c, F(a + b, 2), F(a, 2), F(b, 2)]), ans=0,
                ee='The center is the intersection of the diagonals; diagonal \\(=\\sqrt{%d^2+%d^2}=%d\\), \\(R=%s\\) cm.' % (a, b, c, pe(F(c, 2))),
                ev='Tâm là giao điểm hai đường chéo; đường chéo \\(=\\sqrt{%d^2+%d^2}=%d\\), \\(R=%s\\) cm.' % (a, b, c, dm(pe(F(c, 2)))))


def b29_tf_cyc(r, lv):
    Q = r.choice(QN); x = r.randint(60, 120); truth = r.random() < 0.5; y = 180 - x if truth else 180 - x + r.choice([-10, 10, 20])
    return dict(en='Quadrilateral \\(%s\\) has \\(\\widehat{%s}=%d^\\circ\\) and \\(\\widehat{%s}=%d^\\circ\\). Then \\(%s\\) is a cyclic quadrilateral.' % (Q, Q[1], x, Q[3], y, Q),
                vi='Tứ giác \\(%s\\) có \\(\\widehat{%s}=%d^\\circ\\) và \\(\\widehat{%s}=%d^\\circ\\). Khi đó \\(%s\\) là tứ giác nội tiếp.' % (Q, Q[1], x, Q[3], y, Q), ans=truth,
                ee='A quadrilateral with two opposite angles adding up to \\(180^\\circ\\) is cyclic. Here \\(%d+%d=%d\\).' % (x, y, x + y),
                ev='Tứ giác có tổng hai góc đối bằng \\(180^\\circ\\) thì nội tiếp được. Ở đây \\(%d+%d=%d\\).' % (x, y, x + y))


def b29_tf_square(r, lv):
    a = r.randint(2, 14); truth = r.random() < 0.5; claim = (F(a, 2), 2) if truth else r.choice([(a, 2), (F(a, 2), 1), (F(a, 2), 3)])
    return dict(en='A square with side %d cm has circumradius \\(%s\\).' % (a, surd(*claim)), vi='Hình vuông cạnh %d cm có bán kính đường tròn ngoại tiếp là \\(%s\\).' % (a, surd(*claim)), ans=truth,
                ee='Diagonal \\(%d\\sqrt2\\); \\(R=%s\\).' % (a, surd(F(a, 2), 2)), ev='Đường chéo \\(%d\\sqrt2\\); \\(R=%s\\).' % (a, surd(F(a, 2), 2)))


def b29_short_angle(r, lv):
    Q = r.choice(QN); x = r.randint(40, 140)
    return dict(en='\\(%s\\) is inscribed in a circle and \\(\\widehat{%s}=%d^\\circ\\). Find \\(\\widehat{%s}\\) (in degrees).' % (Q, Q[1], x, Q[3]),
                vi='Tứ giác \\(%s\\) nội tiếp một đường tròn và \\(\\widehat{%s}=%d^\\circ\\). Tính số đo \\(\\widehat{%s}\\) (độ).' % (Q, Q[1], x, Q[3]), key=str(180 - x),
                ee='\\(180-%d=%d\\).' % (x, 180 - x), ev='\\(180-%d=%d\\).' % (x, 180 - x))


def b29_short_rect(r, lv):
    a, b, c = r.choice(PYT); k = r.choice([1, 2])
    if c * k > 60: k = 1
    return dict(en='A rectangular photo frame measures %d cm by %d cm. Find the diameter (cm) of the circle through its four corners.' % (a * k, b * k),
                vi='Một khung ảnh hình chữ nhật có kích thước %d cm × %d cm. Tính đường kính (cm) của đường tròn đi qua bốn góc khung.' % (a * k, b * k), key=str(c * k),
                ee='The diameter is the diagonal: \\(\\sqrt{%d^2+%d^2}=%d\\).' % (a * k, b * k, c * k), ev='Đường kính là đường chéo: \\(\\sqrt{%d^2+%d^2}=%d\\).' % (a * k, b * k, c * k))


def b29_d1_def(r, lv):
    Q = r.choice(QN)
    o = [tx('its four vertices lie on one circle', 'bốn đỉnh của nó cùng nằm trên một đường tròn'), tx('its four sides touch one circle', 'bốn cạnh của nó cùng tiếp xúc với một đường tròn'),
         tx('its diagonals are equal', 'hai đường chéo bằng nhau'), tx('it has a right angle', 'nó có một góc vuông')]
    return dict(en='Quadrilateral \\(%s\\) is called cyclic (inscribed in a circle) when…' % Q, vi='Tứ giác \\(%s\\) được gọi là tứ giác nội tiếp đường tròn khi…' % Q, opts=o, ans=0,
                ee='Definition: the four vertices lie on a circle.', ev='Định nghĩa: bốn đỉnh cùng nằm trên một đường tròn.')


def b29_d1_sum(r, lv):
    Q = r.choice(QN)
    o = ['\\widehat{%s}+\\widehat{%s}=180^\\circ' % (Q[0], Q[2]), '\\widehat{%s}+\\widehat{%s}=180^\\circ' % (Q[0], Q[1]), '\\widehat{%s}=\\widehat{%s}' % (Q[0], Q[2]), '\\widehat{%s}+\\widehat{%s}=360^\\circ' % (Q[0], Q[2])]
    return dict(en='\\(%s\\) is a cyclic quadrilateral. Which relation is always true?' % Q, vi='\\(%s\\) là tứ giác nội tiếp. Hệ thức nào luôn đúng?' % Q, opts=o, ans=0,
                ee='Opposite angles are supplementary.', ev='Hai góc đối diện có tổng bằng \\(180^\\circ\\).')


def b29_d1_set(r, lv):
    for _ in range(200):
        a, b = r.randint(60, 120), r.randint(60, 120)
        good = (a, b, 180 - a, 180 - b)
        bads = [(a, b, 180 - a + 10, 170 - b), (a, 180 - a, b, 180 - b), (a, b, 180 - b, 180 - a)]
        if len({good} | set(bads)) == 4 and all(sum(x) == 360 for x in bads[:1]) and a != b and a + b != 180: break
    else: raise AssertionError
    def f(t): return '\\(\\widehat{A}=%d^\\circ,\\ \\widehat{B}=%d^\\circ,\\ \\widehat{C}=%d^\\circ,\\ \\widehat{D}=%d^\\circ\\)' % t
    o = [tx(f(good), f(good))] + [tx(f(x), f(x)) for x in bads]
    st = r.choice([('Which quadrilateral \\(ABCD\\) (angles in this order) is cyclic?', 'Tứ giác \\(ABCD\\) nào sau đây (các góc theo thứ tự) là tứ giác nội tiếp?'),
                   ('The angles of quadrilateral \\(ABCD\\) are given below. In which case is \\(ABCD\\) inscribed in a circle?', 'Các góc của tứ giác \\(ABCD\\) được cho dưới đây. Trường hợp nào \\(ABCD\\) nội tiếp được đường tròn?'),
                   ('For which of the following quadrilaterals \\(ABCD\\) can we draw a circle through the four vertices?', 'Với tứ giác \\(ABCD\\) nào sau đây, ta vẽ được một đường tròn đi qua bốn đỉnh?')])
    return dict(en=st[0], vi=st[1], opts=o, ans=0,
                ee='We need \\(\\widehat{A}+\\widehat{C}=\\widehat{B}+\\widehat{D}=180^\\circ\\).', ev='Cần có \\(\\widehat{A}+\\widehat{C}=\\widehat{B}+\\widehat{D}=180^\\circ\\).')


def b29_d2_ext(r, lv):
    x = r.randint(55, 125); pa = _quad(r); pts = {'A': pa[0], 'B': pa[1], 'C': pa[2], 'D': pa[3]}
    return dict(en='\\(ABCD\\) is a cyclic quadrilateral with \\(%s=%d^\\circ\\). The side \\(BC\\) is extended beyond \\(C\\) to a point \\(E\\). Find \\(%s\\).' % (A('BAD'), x, A('DCE')),
                vi='\\(ABCD\\) là tứ giác nội tiếp có \\(%s=%d^\\circ\\). Kéo dài cạnh \\(BC\\) về phía \\(C\\) đến điểm \\(E\\). Tính \\(%s\\).' % (A('BAD'), x, A('DCE')),
                opts=dopts(r, x, [180 - x, 90 - x // 2 if x < 90 else x - 45, 2 * x if 2 * x < 360 else x + 20]), ans=0,
                ee='\\(%s=180^\\circ-%s=180^\\circ-(180^\\circ-%d^\\circ)=%d^\\circ\\): the exterior angle equals the opposite interior angle.' % (A('DCE'), A('BCD'), x, x),
                ev='\\(%s=180^\\circ-%s=180^\\circ-(180^\\circ-%d^\\circ)=%d^\\circ\\): góc ngoài bằng góc trong ở đỉnh đối diện.' % (A('DCE'), A('BCD'), x, x))


def b29_d2_two(r, lv):
    a, b = r.randint(60, 120), r.randint(60, 120); ask = r.choice(['C', 'D'])
    g = 180 - a if ask == 'C' else 180 - b
    return dict(en='Cyclic quadrilateral \\(ABCD\\) has \\(\\widehat{A}=%d^\\circ\\) and \\(\\widehat{B}=%d^\\circ\\). Find \\(\\widehat{%s}\\).' % (a, b, ask),
                vi='Tứ giác nội tiếp \\(ABCD\\) có \\(\\widehat{A}=%d^\\circ\\), \\(\\widehat{B}=%d^\\circ\\). Tính \\(\\widehat{%s}\\).' % (a, b, ask),
                opts=dopts(r, g, [180 - b if ask == 'C' else 180 - a, 360 - a - b, a if ask == 'C' else b]), ans=0,
                ee='\\(\\widehat{C}=180^\\circ-\\widehat{A}=%d^\\circ\\), \\(\\widehat{D}=180^\\circ-\\widehat{B}=%d^\\circ\\).' % (180 - a, 180 - b),
                ev='\\(\\widehat{C}=180^\\circ-\\widehat{A}=%d^\\circ\\), \\(\\widehat{D}=180^\\circ-\\widehat{B}=%d^\\circ\\).' % (180 - a, 180 - b))


def b29_d2_square(r, lv):
    R = r.randint(2, 15); k = r.choice(['side', 'area'])
    if k == 'side':
        return dict(en='A square is inscribed in a circle of radius %d cm. Find its side.' % R, vi='Một hình vuông nội tiếp đường tròn bán kính %d cm. Tính độ dài cạnh hình vuông.' % R,
                    opts=sopts(r, (R, 2), [(2 * R, 1), (R, 1), (R, 3), (2 * R, 2)]), ans=0, ee='Diagonal \\(=2R\\); side \\(=\\dfrac{2R}{\\sqrt2}=%s\\).' % surd(R, 2), ev='Đường chéo \\(=2R\\); cạnh \\(=\\dfrac{2R}{\\sqrt2}=%s\\).' % surd(R, 2))
    return dict(en='A square is inscribed in a circle of radius %d cm. Find its area.' % R, vi='Một hình vuông nội tiếp đường tròn bán kính %d cm. Tính diện tích hình vuông.' % R,
                opts=['%d\\text{ cm}^2' % (2 * R * R), '%d\\text{ cm}^2' % (R * R), '%d\\text{ cm}^2' % (4 * R * R), '%d\\text{ cm}^2' % (3 * R * R)], ans=0,
                ee='Side \\(R\\sqrt2\\); area \\(2R^2=%d\\) cm².' % (2 * R * R), ev='Cạnh \\(R\\sqrt2\\); diện tích \\(2R^2=%d\\) cm².' % (2 * R * R))


def b29_d3_trap(r, lv):
    x = r.randint(50, 85)
    return dict(en='\\(ABCD\\) is an isosceles trapezoid (\\(AB\\parallel CD\\), \\(AD=BC\\)) inscribed in a circle, \\(\\widehat{A}=%d^\\circ\\). Find \\(\\widehat{C}\\).' % x,
                vi='Hình thang cân \\(ABCD\\) (\\(AB\\parallel CD\\), \\(AD=BC\\)) nội tiếp đường tròn, \\(\\widehat{A}=%d^\\circ\\). Tính \\(\\widehat{C}\\).' % x,
                opts=dopts(r, 180 - x, [x, 90 - x // 2 + 45, 360 - 2 * x]), ans=0,
                ee='\\(\\widehat{A}\\) and \\(\\widehat{C}\\) are opposite angles: \\(\\widehat{C}=180^\\circ-%d^\\circ=%d^\\circ\\).' % (x, 180 - x), ev='\\(\\widehat{A}\\), \\(\\widehat{C}\\) là hai góc đối: \\(\\widehat{C}=180^\\circ-%d^\\circ=%d^\\circ\\).' % (x, 180 - x))


def b29_d3_chase(r, lv):
    x, y = r.randint(25, 60), r.randint(25, 60); pa = _quad(r)
    return dict(en='In the cyclic quadrilateral \\(ABCD\\), \\(%s=%d^\\circ\\) and \\(%s=%d^\\circ\\). Find \\(%s\\).' % (A('ABD'), x, A('ADB'), y, A('BCD')),
                vi='Trong tứ giác nội tiếp \\(ABCD\\), \\(%s=%d^\\circ\\) và \\(%s=%d^\\circ\\). Tính \\(%s\\).' % (A('ABD'), x, A('ADB'), y, A('BCD')),
                opts=dopts(r, x + y, [180 - x - y, x, y, 2 * (x + y) if 2 * (x + y) < 180 else x + y + 20]), ans=0,
                ee='In triangle \\(ABD\\): \\(%s=180^\\circ-%d^\\circ-%d^\\circ=%d^\\circ\\); \\(%s=180^\\circ-%d^\\circ=%d^\\circ\\).' % (A('BAD'), x, y, 180 - x - y, A('BCD'), 180 - x - y, x + y),
                ev='Trong tam giác \\(ABD\\): \\(%s=180^\\circ-%d^\\circ-%d^\\circ=%d^\\circ\\); \\(%s=180^\\circ-%d^\\circ=%d^\\circ\\).' % (A('BAD'), x, y, 180 - x - y, A('BCD'), 180 - x - y, x + y),
                fig=CFIG(pts=dict(zip('ABCD', pa)), segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('B', 'D')], O=False))


def b29_d3_rectpi(r, lv):
    a, b, c = r.choice(PYT[:6]); k = r.choice(['area', 'len'])
    if k == 'area':
        g = F(c * c, 4)
        return dict(en='A rectangle with sides %d cm and %d cm is inscribed in a circle. Find the area of the disk.' % (a, b), vi='Một hình chữ nhật có các cạnh %d cm và %d cm nội tiếp một đường tròn. Tính diện tích hình tròn đó.' % (a, b),
                    opts=piopts(r, g, [c * c, F(c * c, 2), a * b]), ans=0, ee='\\(R=\\dfrac{%d}{2}\\), \\(S=%s\\).' % (c, pi(g, 'cm', 2)), ev='\\(R=\\dfrac{%d}{2}\\), \\(S=%s\\).' % (c, pi(g, 'cm', 2)))
    return dict(en='A rectangle with sides %d cm and %d cm is inscribed in a circle. Find the circumference of the circle.' % (a, b), vi='Một hình chữ nhật có các cạnh %d cm và %d cm nội tiếp một đường tròn. Tính độ dài đường tròn đó.' % (a, b),
                opts=piopts(r, c, [2 * c, F(c, 2), a + b], p=1), ans=0, ee='\\(C=\\pi d=%s\\).' % pi(c), ev='\\(C=\\pi d=%s\\).' % pi(c))


def b29_d4_right(r, lv):
    a, b, c = r.choice(PYT[:6])
    return dict(en='Quadrilateral \\(ABCD\\) has \\(\\widehat{B}=\\widehat{D}=90^\\circ\\), \\(AB=%d\\) cm, \\(BC=%d\\) cm. Which statement is correct?' % (a, b),
                vi='Tứ giác \\(ABCD\\) có \\(\\widehat{B}=\\widehat{D}=90^\\circ\\), \\(AB=%d\\) cm, \\(BC=%d\\) cm. Khẳng định nào đúng?' % (a, b),
                opts=[tx('\\(ABCD\\) is cyclic, with circumradius \\(%s\\) cm' % pe(F(c, 2)), '\\(ABCD\\) nội tiếp đường tròn bán kính \\(%s\\) cm' % dm(pe(F(c, 2)))),
                      tx('\\(ABCD\\) is cyclic, with circumradius \\(%d\\) cm' % c, '\\(ABCD\\) nội tiếp đường tròn bán kính \\(%d\\) cm' % c),
                      tx('\\(ABCD\\) is not cyclic', '\\(ABCD\\) không nội tiếp được đường tròn'), tx('\\(ABCD\\) is cyclic, with circumradius \\(%s\\) cm' % pe(F(a + b, 2)), '\\(ABCD\\) nội tiếp đường tròn bán kính \\(%s\\) cm' % dm(pe(F(a + b, 2))))], ans=0,
                ee='\\(\\widehat{B}+\\widehat{D}=180^\\circ\\): cyclic. \\(B\\), \\(D\\) see \\(AC\\) under right angles, so \\(AC=%d\\) is a diameter, \\(R=%s\\).' % (c, pe(F(c, 2))),
                ev='\\(\\widehat{B}+\\widehat{D}=180^\\circ\\) nên nội tiếp. \\(B\\), \\(D\\) nhìn \\(AC\\) dưới góc vuông nên \\(AC=%d\\) là đường kính, \\(R=%s\\).' % (c, dm(pe(F(c, 2)))))


def b29_d4_ratio(r, lv):
    for _ in range(100):
        p, q = r.sample(range(1, 8), 2)
        if (180 * p) % (p + q) == 0: break
    else: raise AssertionError
    A_ = 180 * p // (p + q)
    return dict(en='Cyclic quadrilateral \\(ABCD\\) has \\(\\widehat{A}:\\widehat{C}=%d:%d\\). Find \\(\\widehat{A}\\).' % (p, q), vi='Tứ giác nội tiếp \\(ABCD\\) có \\(\\widehat{A}:\\widehat{C}=%d:%d\\). Tính \\(\\widehat{A}\\).' % (p, q),
                opts=dopts(r, A_, [180 - A_, 360 * p // (p + q) if (360 * p) % (p + q) == 0 else A_ + 15, 90]), ans=0,
                ee='\\(\\widehat{A}+\\widehat{C}=180^\\circ\\), so \\(\\widehat{A}=\\dfrac{%d}{%d}\\cdot180^\\circ=%d^\\circ\\).' % (p, p + q, A_), ev='\\(\\widehat{A}+\\widehat{C}=180^\\circ\\) nên \\(\\widehat{A}=\\dfrac{%d}{%d}\\cdot180^\\circ=%d^\\circ\\).' % (p, p + q, A_))


def b29_d4_stage(r, lv):
    a, b, c = r.choice(PYT[:7]); u = r.choice([1, 2])
    a, b, c = a * u, b * u, c * u
    g = F(c * c, 4)
    return dict(en='A circular theater garden is designed so that a rectangular stage %d m × %d m has its four corners on the boundary circle. What is the area of the garden?' % (a, b),
                vi='Một khu vườn – sân khấu hình tròn được thiết kế sao cho bốn góc của sân khấu hình chữ nhật %d m × %d m nằm trên đường tròn biên. Tính diện tích khu vườn.' % (a, b),
                opts=piopts(r, g, [c * c, F(c * c, 2), F(a * b, 1)], unit='m'), ans=0,
                ee='The stage is inscribed: diameter = diagonal \\(=%d\\) m, \\(S=\\pi\\left(\\dfrac{%d}{2}\\right)^2=%s\\).' % (c, c, pi(g, 'm', 2)),
                ev='Sân khấu nội tiếp đường tròn: đường kính = đường chéo \\(=%d\\) m, \\(S=\\pi\\left(\\dfrac{%d}{2}\\right)^2=%s\\).' % (c, c, pi(g, 'm', 2)))


L29_GROUPS = [[('mcq', b29_opp), ('mcq', b29_which), ('mcq', b29_rect)], [('tf', b29_tf_cyc), ('tf', b29_tf_square)], [('short', b29_short_angle), ('short', b29_short_rect)],
              [('mcq', b29_d1_def), ('mcq', b29_d1_sum), ('mcq', b29_d1_set)], [('mcq', b29_d2_ext), ('mcq', b29_d2_two), ('mcq', b29_d2_square)],
              [('mcq', b29_d3_trap), ('mcq', b29_d3_chase), ('mcq', b29_d3_rectpi)], [('mcq', b29_d4_right), ('mcq', b29_d4_ratio), ('mcq', b29_d4_stage)]]


# =====================================================================================================
# BÀI 30. Đa giác đều
# =====================================================================================================
PNAME = {3: ('equilateral triangle', 'tam giác đều'), 4: ('square', 'hình vuông'), 5: ('regular pentagon', 'ngũ giác đều'), 6: ('regular hexagon', 'lục giác đều'),
         8: ('regular octagon', 'bát giác đều'), 9: ('regular nonagon', 'cửu giác đều'), 10: ('regular decagon', 'thập giác đều'), 12: ('regular 12-gon', 'đa giác đều 12 cạnh')}
LET = 'ABCDEFGHIKLM'


def polyfig(n, central=True):
    pts = {LET[i]: 90 + 360 * i / n for i in range(n)}
    segs = [(LET[i], LET[(i + 1) % n]) for i in range(n)]
    return CFIG(pts=pts, segs=segs, dash=[('O', 'A'), ('O', 'B')] if central else [], arcs=[('A', 'O', 'B', '')] if central else [])


def b30_central(r, lv):
    n = r.choice([3, 4, 5, 6, 8, 9, 10, 12]); c = 360 // n
    q = dict(en='What is the central angle of a %s (the angle subtended at the center by one side)?' % PNAME[n][0], vi='Góc ở tâm của %s (góc ở tâm chắn một cạnh) bằng bao nhiêu?' % PNAME[n][1],
             opts=dopts(r, c, [F(180 * (n - 2), n), F(180, n), 2 * c]), ans=0,
             ee='\\(\\dfrac{360^\\circ}{%d}=%d^\\circ\\).' % (n, c), ev='\\(\\dfrac{360^\\circ}{%d}=%d^\\circ\\).' % (n, c))
    if n <= 8: q['fig'] = polyfig(n)
    return q


def b30_interior(r, lv):
    n = r.choice([3, 4, 5, 6, 8, 9, 10, 12]); g = F(180 * (n - 2), n)
    return dict(en='Find each interior angle of a %s.' % PNAME[n][0], vi='Tính số đo mỗi góc trong của %s.' % PNAME[n][1],
                opts=dopts(r, g, [F(360, n), 180 * (n - 2), F(180 * (n - 1), n), 180 - F(180, n)]), ans=0,
                ee='Sum of interior angles \\((%d-2)\\cdot180^\\circ=%d^\\circ\\); each angle \\(\\dfrac{%d^\\circ}{%d}=%s\\).' % (n, 180 * (n - 2), 180 * (n - 2), n, deg(g)),
                ev='Tổng các góc trong \\((%d-2)\\cdot180^\\circ=%d^\\circ\\); mỗi góc \\(\\dfrac{%d^\\circ}{%d}=%s\\).' % (n, 180 * (n - 2), 180 * (n - 2), n, degv(g)))


def b30_which(r, lv):
    k = r.choice(['is', 'not', 'is2'])
    yes = [('an equilateral triangle', 'tam giác đều'), ('a square', 'hình vuông'), ('a regular hexagon', 'lục giác đều')]
    no = [('a rhombus with a \\(60^\\circ\\) angle', 'hình thoi có một góc \\(60^\\circ\\)'), ('a rectangle 3 cm × 5 cm', 'hình chữ nhật 3 cm × 5 cm'), ('an isosceles right triangle', 'tam giác vuông cân'), ('an isosceles trapezoid', 'hình thang cân')]
    if k in ('is', 'is2'):
        g = r.choice(yes); o = [tx(*g)] + [tx(*x) for x in r.sample(no, 3)]
        st = ('Which figure is a regular polygon?', 'Hình nào sau đây là đa giác đều?') if k == 'is' else ('Which of these polygons has all sides equal AND all angles equal?', 'Đa giác nào sau đây có tất cả các cạnh bằng nhau VÀ tất cả các góc bằng nhau?')
    else:
        g = r.choice(no); o = [tx(*g)] + [tx(*x) for x in yes]
        st = ('Which figure is NOT a regular polygon?', 'Hình nào sau đây KHÔNG phải là đa giác đều?')
    return dict(en=st[0], vi=st[1], opts=o, ans=0, ee='A regular polygon has all sides equal and all angles equal.', ev='Đa giác đều là đa giác có tất cả các cạnh bằng nhau và tất cả các góc bằng nhau.')


def b30_tf_rot(r, lv):
    n = r.choice([3, 4, 5, 6, 8, 10, 12]); c = 360 // n
    truth = r.random() < 0.5
    a = c * r.randint(1, n - 1) if truth else r.choice([x for x in range(10, 360, 10) if x % c != 0] or [c + 1])
    return dict(en='The rotation about the center \\(O\\) through \\(%d^\\circ\\) maps the %s onto itself.' % (a, PNAME[n][0]),
                vi='Phép quay tâm \\(O\\) góc \\(%d^\\circ\\) biến %s thành chính nó.' % (a, PNAME[n][1]), ans=a % c == 0,
                ee='It works exactly for multiples of \\(\\dfrac{360^\\circ}{%d}=%d^\\circ\\). %s' % (n, c, '%d is a multiple of %d.' % (a, c) if a % c == 0 else '%d is not a multiple of %d.' % (a, c)),
                ev='Chỉ đúng khi góc quay là bội của \\(\\dfrac{360^\\circ}{%d}=%d^\\circ\\). %s' % (n, c, '%d là bội của %d.' % (a, c) if a % c == 0 else '%d không là bội của %d.' % (a, c)))


def b30_tf_hex(r, lv):
    R = r.randint(2, 20); truth = r.random() < 0.5; claim = R if truth else r.choice([2 * R, F(R, 2)])
    return dict(en='A regular hexagon is inscribed in a circle of radius %d cm. Each side of the hexagon is \\(%s\\) cm long.' % (R, pe(claim)),
                vi='Một lục giác đều nội tiếp đường tròn bán kính %d cm. Mỗi cạnh của lục giác dài \\(%s\\) cm.' % (R, dm(pe(claim))), ans=truth,
                ee='The central angle is \\(60^\\circ\\), so each triangle \\(OAB\\) is equilateral: side \\(=R=%d\\) cm.' % R, ev='Góc ở tâm bằng \\(60^\\circ\\) nên mỗi tam giác \\(OAB\\) đều: cạnh \\(=R=%d\\) cm.' % R)


def b30_short_count(r, lv):
    n = r.choice([3, 4, 5, 6, 8, 9, 10, 12])
    return dict(en='How many rotations about its center with angle \\(\\alpha\\), \\(0^\\circ\\lt\\alpha\\le360^\\circ\\), map a %s onto itself?' % PNAME[n][0],
                vi='Có bao nhiêu phép quay tâm \\(O\\) góc \\(\\alpha\\) (\\(0^\\circ\\lt\\alpha\\le360^\\circ\\)) biến %s tâm \\(O\\) thành chính nó?' % PNAME[n][1], key=str(n),
                ee='The angles \\(%d^\\circ, %d^\\circ, \\dots, 360^\\circ\\): %d rotations.' % (360 // n, 720 // n, n), ev='Các góc \\(%d^\\circ, %d^\\circ, \\dots, 360^\\circ\\): có %d phép quay.' % (360 // n, 720 // n, n))


def b30_short_n(r, lv):
    n = r.choice([5, 6, 8, 9, 10, 12, 15, 18, 20]); g = F(180 * (n - 2), n); k = r.choice(['int', 'cen'])
    if k == 'int' and g.denominator == 1:
        return dict(en='Each interior angle of a regular polygon is \\(%d^\\circ\\). How many sides does it have?' % g, vi='Mỗi góc trong của một đa giác đều bằng \\(%d^\\circ\\). Đa giác đó có bao nhiêu cạnh?' % g, key=str(n),
                    ee='Each exterior angle is \\(180^\\circ-%d^\\circ=%d^\\circ\\); \\(n=\\dfrac{360}{%d}=%d\\).' % (g, 180 - g, 180 - g, n), ev='Mỗi góc ngoài bằng \\(180^\\circ-%d^\\circ=%d^\\circ\\); \\(n=\\dfrac{360}{%d}=%d\\).' % (g, 180 - g, 180 - g, n))
    return dict(en='The central angle of a regular polygon is \\(%d^\\circ\\). How many sides does it have?' % (360 // n), vi='Góc ở tâm của một đa giác đều bằng \\(%d^\\circ\\). Đa giác đó có bao nhiêu cạnh?' % (360 // n), key=str(n),
                ee='\\(n=\\dfrac{360}{%d}=%d\\).' % (360 // n, n), ev='\\(n=\\dfrac{360}{%d}=%d\\).' % (360 // n, n))


def b30_d1_def(r, lv):
    k = r.choice(['def', 'rhombus', 'rect'])
    if k == 'def':
        o = [tx('all its sides are equal and all its angles are equal', 'tất cả các cạnh bằng nhau và tất cả các góc bằng nhau'), tx('all its sides are equal', 'tất cả các cạnh bằng nhau'),
             tx('all its angles are equal', 'tất cả các góc bằng nhau'), tx('it is inscribed in a circle', 'nội tiếp được một đường tròn')]
        return dict(en='A polygon is called regular when…', vi='Một đa giác được gọi là đa giác đều khi…', opts=o, ans=0, ee='Both conditions are needed.', ev='Cần cả hai điều kiện.')
    if k == 'rhombus':
        o = [tx('the sides are equal but the angles are not all equal', 'các cạnh bằng nhau nhưng các góc không bằng nhau'), tx('the angles are equal but the sides are not', 'các góc bằng nhau nhưng các cạnh không bằng nhau'),
             tx('it has only 4 sides', 'nó chỉ có 4 cạnh'), tx('it is not convex', 'nó không lồi')]
        return dict(en='Why is a rhombus with a \\(70^\\circ\\) angle NOT a regular polygon?', vi='Vì sao hình thoi có một góc \\(70^\\circ\\) KHÔNG phải là đa giác đều?', opts=o, ans=0, ee='Its angles are \\(70^\\circ\\) and \\(110^\\circ\\).', ev='Các góc của nó là \\(70^\\circ\\) và \\(110^\\circ\\).')
    o = [tx('the angles are equal but the sides are not all equal', 'các góc bằng nhau nhưng các cạnh không bằng nhau'), tx('the sides are equal but the angles are not', 'các cạnh bằng nhau nhưng các góc không bằng nhau'),
         tx('it has no center', 'nó không có tâm'), tx('it is not convex', 'nó không lồi')]
    return dict(en='Why is a 4 cm × 6 cm rectangle NOT a regular polygon?', vi='Vì sao hình chữ nhật 4 cm × 6 cm KHÔNG phải là đa giác đều?', opts=o, ans=0, ee='All angles are \\(90^\\circ\\), but the sides are 4 cm and 6 cm.', ev='Các góc đều bằng \\(90^\\circ\\) nhưng các cạnh là 4 cm và 6 cm.')


def b30_d1_center(r, lv):
    n = r.choice([3, 4, 6])
    o = [tx('the center \\(O\\) of the polygon', 'tâm \\(O\\) của đa giác'), tx('the vertex \\(A\\)', 'đỉnh \\(A\\)'), tx('the midpoint of \\(AB\\)', 'trung điểm của \\(AB\\)'), tx('any point inside the polygon', 'một điểm bất kì trong đa giác')]
    return dict(en='The rotations that map the %s \\(%s\\) onto itself have their center at…' % (PNAME[n][0], LET[:n]), vi='Các phép quay biến %s \\(%s\\) thành chính nó có tâm quay là…' % (PNAME[n][1], LET[:n]), opts=o, ans=0,
                ee='The center of the circumcircle (center of the polygon).', ev='Tâm của đường tròn ngoại tiếp (tâm của đa giác).', fig=polyfig(n, central=False))


def b30_d1_small(r, lv):
    n = r.choice([3, 4, 5, 6, 8, 10, 12]); c = 360 // n
    return dict(en='What is the smallest positive angle of a rotation about the center that maps a %s onto itself?' % PNAME[n][0], vi='Góc quay dương nhỏ nhất của phép quay quanh tâm biến %s thành chính nó là bao nhiêu?' % PNAME[n][1],
                opts=dopts(r, c, [360, 180, 2 * c, F(c, 2)]), ans=0, ee='\\(\\dfrac{360^\\circ}{%d}=%d^\\circ\\).' % (n, c), ev='\\(\\dfrac{360^\\circ}{%d}=%d^\\circ\\).' % (n, c))


def b30_d2_list(r, lv):
    n = r.choice([3, 4, 5, 6, 8]); c = 360 // n; good = c * r.randint(1, n - 1)
    bads = [x for x in (c // 2 * 3 if (c // 2 * 3) % c else c + 15, 90 if 90 % c else 100, 100, 45 if 45 % c else 50, c + 10) if x % c]
    return dict(en='Which rotation about its center maps a %s onto itself?' % PNAME[n][0], vi='Phép quay nào quanh tâm biến %s thành chính nó?' % PNAME[n][1],
                opts=pick_opts(r, tx('rotation through \\(%d^\\circ\\)' % good, 'phép quay góc \\(%d^\\circ\\)' % good), [tx('rotation through \\(%d^\\circ\\)' % b, 'phép quay góc \\(%d^\\circ\\)' % b) for b in bads]), ans=0,
                ee='Multiples of \\(%d^\\circ\\) work: \\(%d=%d\\cdot%d\\).' % (c, good, good // c, c), ev='Các bội của \\(%d^\\circ\\) đều thỏa mãn: \\(%d=%d\\cdot%d\\).' % (c, good, good // c, c))


def b30_d2_sum(r, lv):
    n = r.choice([5, 6, 7, 8, 9, 10, 12]); s = 180 * (n - 2)
    return dict(en='What is the sum of the interior angles of a regular polygon with %d sides?' % n, vi='Tổng các góc trong của một đa giác đều %d cạnh bằng bao nhiêu?' % n,
                opts=dopts(r, s, [180 * n, 360, 180 * (n - 1)], step=180) if s < 360 else dopts(r, s, [180 * n, 360, 180 * (n - 1)], step=180), ans=0,
                ee='\\((n-2)\\cdot180^\\circ=%d\\cdot180^\\circ=%d^\\circ\\).' % (n - 2, s), ev='\\((n-2)\\cdot180^\\circ=%d\\cdot180^\\circ=%d^\\circ\\).' % (n - 2, s))


def b30_d2_ext(r, lv):
    n = r.choice([5, 6, 8, 9, 10, 12, 15, 18]); e = 360 // n; i = 180 - e
    return dict(en='Each interior angle of a regular %d-gon is \\(%d^\\circ\\). What is each exterior angle?' % (n, i), vi='Mỗi góc trong của đa giác đều %d cạnh bằng \\(%d^\\circ\\). Mỗi góc ngoài bằng bao nhiêu?' % (n, i),
                opts=dopts(r, e, [i, 360 - i, 90 - e // 2 if 90 - e // 2 != e else e + 5]), ans=0,
                ee='\\(180^\\circ-%d^\\circ=%d^\\circ\\) (also \\(\\dfrac{360^\\circ}{%d}\\)).' % (i, e, n), ev='\\(180^\\circ-%d^\\circ=%d^\\circ\\) (cũng bằng \\(\\dfrac{360^\\circ}{%d}\\)).' % (i, e, n))


def b30_d3_hexper(r, lv):
    R = r.randint(2, 15)
    return dict(en='A regular hexagon is inscribed in a circle of radius %d cm. Find its perimeter.' % R, vi='Một lục giác đều nội tiếp đường tròn bán kính %d cm. Tính chu vi lục giác.' % R,
                opts=nopts(r, 6 * R, [3 * R, 12 * R, 6 * R + 6]), ans=0, ee='Side \\(=R=%d\\); perimeter \\(6\\cdot%d=%d\\) cm.' % (R, R, 6 * R), ev='Cạnh \\(=R=%d\\); chu vi \\(6\\cdot%d=%d\\) cm.' % (R, R, 6 * R),
                fig=polyfig(6))


def b30_d3_sqarea(r, lv):
    R = r.randint(2, 15)
    return dict(en='A square \\(ABCD\\) is inscribed in a circle of radius %d cm. Find its area.' % R, vi='Hình vuông \\(ABCD\\) nội tiếp đường tròn bán kính %d cm. Tính diện tích hình vuông.' % R,
                opts=pick_opts(r, '%d\\text{ cm}^2' % (2 * R * R), ['%d\\text{ cm}^2' % v for v in (R * R, 4 * R * R, 3 * R * R)]), ans=0,
                ee='The diagonals are diameters \\(2R\\); area \\(=\\dfrac{(2R)^2}{2}=2R^2=%d\\) cm².' % (2 * R * R), ev='Hai đường chéo là đường kính \\(2R\\); diện tích \\(=\\dfrac{(2R)^2}{2}=2R^2=%d\\) cm².' % (2 * R * R),
                fig=CFIG(pts={'A': 90, 'B': 180, 'C': 270, 'D': 0}, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')], dash=[('A', 'C'), ('B', 'D')], ocand=(-45, -135, 45, 135)))


def b30_d3_tri(r, lv):
    R = r.randint(2, 12)
    return dict(en='An equilateral triangle is inscribed in a circle of radius %d cm. Find its side.' % R, vi='Tam giác đều nội tiếp đường tròn bán kính %d cm. Tính độ dài cạnh tam giác.' % R,
                opts=sopts(r, (R, 3), [(R, 2), (2 * R, 1), (F(R, 2), 3)]), ans=0,
                ee='Central angle \\(120^\\circ\\): side \\(=2R\\sin60^\\circ=R\\sqrt3=%s\\).' % surd(R, 3), ev='Góc ở tâm \\(120^\\circ\\): cạnh \\(=2R\\sin60^\\circ=R\\sqrt3=%s\\).' % surd(R, 3))


def b30_d4_hexarea(r, lv):
    a = r.choice([2, 4, 6, 8, 10])
    g = F(3 * a * a, 2)
    return dict(en='A hexagonal floor tile is a regular hexagon with side %d cm. Find its area.' % a, vi='Một viên gạch lát nền hình lục giác đều cạnh %d cm. Tính diện tích viên gạch.' % a,
                opts=pick_opts(r, '%s\\sqrt3\\text{ cm}^2' % pe(g), ['%s\\sqrt3\\text{ cm}^2' % pe(x) for x in (F(a * a, 4), 3 * a * a, 6 * a * a)]), ans=0,
                ee='Six equilateral triangles of side %d: \\(6\\cdot\\dfrac{%d^2\\sqrt3}{4}=%s\\sqrt3\\) cm².' % (a, a, pe(g)), ev='Sáu tam giác đều cạnh %d: \\(6\\cdot\\dfrac{%d^2\\sqrt3}{4}=%s\\sqrt3\\) cm².' % (a, a, pe(g)))


def b30_d4_tile(r, lv):
    k = r.choice(['yes', 'no', 'yes2'])
    if k in ('yes', 'yes2'):
        g = r.choice([3, 4, 6]); bad = [5, 8, 10, 12]; o = [tx(PNAME[g][0], PNAME[g][1])] + [tx(PNAME[b][0], PNAME[b][1]) for b in r.sample(bad, 3)]
        st = ('Tiles of one kind of regular polygon must cover a floor without gaps or overlaps (the angles at each vertex add up to \\(360^\\circ\\)). Which shape works?',
              'Lát kín mặt sàn bằng các viên gạch cùng một loại đa giác đều (tổng các góc tại mỗi đỉnh chung bằng \\(360^\\circ\\)). Dùng loại nào được?') if k == 'yes' else \
             ('Which regular polygon can tile a plane by itself (its interior angle divides \\(360^\\circ\\))?', 'Đa giác đều nào tự lát kín được mặt phẳng (góc trong của nó là ước của \\(360^\\circ\\))?')
        e = F(180 * (g - 2), g)
        return dict(en=st[0], vi=st[1], opts=o, ans=0, ee='Interior angle \\(%s\\) divides \\(360^\\circ\\).' % deg(e), ev='Góc trong \\(%s\\) là ước của \\(360^\\circ\\).' % degv(e))
    g = r.choice([5, 8, 10]); o = [tx(PNAME[g][0], PNAME[g][1])] + [tx(PNAME[b][0], PNAME[b][1]) for b in (3, 4, 6)]
    e = F(180 * (g - 2), g)
    return dict(en='Which regular polygon CANNOT tile a floor by itself?', vi='Đa giác đều nào KHÔNG tự lát kín được mặt sàn?', opts=o, ans=0,
                ee='Its interior angle \\(%s\\) does not divide \\(360^\\circ\\).' % deg(e), ev='Góc trong \\(%s\\) không là ước của \\(360^\\circ\\).' % degv(e))


def b30_d4_gear(r, lv):
    n = r.choice([8, 10, 12, 15, 18, 20, 24, 30, 36]); k = r.randint(2, 5)
    a = F(360 * k, n)
    if a >= 360: raise AssertionError
    return dict(en='A gear wheel has %d equally spaced teeth (its outline is symmetric like a regular %d-gon). It turns so that each tooth moves %d places forward. Through what angle has it turned?' % (n, n, k),
                vi='Một bánh răng có %d răng cách đều nhau (đường viền đối xứng như đa giác đều %d cạnh). Bánh răng quay sao cho mỗi răng tiến lên %d vị trí. Bánh răng đã quay một góc bao nhiêu?' % (n, n, k),
                opts=dopts(r, a, [F(360, n), F(360 * (k + 1), n), F(180 * k, n), k * 10]), ans=0,
                ee='One place = \\(\\dfrac{360^\\circ}{%d}=%s\\); \\(%d\\) places = \\(%s\\).' % (n, deg(F(360, n)), k, deg(a)), ev='Một vị trí ứng với \\(\\dfrac{360^\\circ}{%d}=%s\\); \\(%d\\) vị trí ứng với \\(%s\\).' % (n, degv(F(360, n)), k, degv(a)))


L30_GROUPS = [[('mcq', b30_central), ('mcq', b30_interior), ('mcq', b30_which)], [('tf', b30_tf_rot), ('tf', b30_tf_hex)], [('short', b30_short_count), ('short', b30_short_n)],
              [('mcq', b30_d1_def), ('mcq', b30_d1_center), ('mcq', b30_d1_small)], [('mcq', b30_d2_list), ('mcq', b30_d2_sum), ('mcq', b30_d2_ext)],
              [('mcq', b30_d3_hexper), ('mcq', b30_d3_sqarea), ('mcq', b30_d3_tri)], [('mcq', b30_d4_hexarea), ('mcq', b30_d4_tile), ('mcq', b30_d4_gear)]]


# =====================================================================================================
# HÌNH KHỐI TRÒN XOAY (tĩnh): hình trụ, hình nón, hình cầu – nét khuất vẽ nét đứt
# =====================================================================================================
DASH = 'dash pattern=on 3pt off 2.5pt'


def solid_svg(kind, labs=('r', 'h', 'l')):
    G = col('046b4d'); O_ = col('c2410c')
    o = ['\\begin{tikzpicture}[line join=round]']
    if kind == 'cyl':
        R, ry, H = 1.3, 0.38, 2.6
        o += ['\\draw[color=%s, line width=1pt] (-%s,0) arc[start angle=180, end angle=360, x radius=%scm, y radius=%scm];' % (G, R, R, ry),
              '\\draw[color=%s, line width=0.8pt, %s] (%s,0) arc[start angle=0, end angle=180, x radius=%scm, y radius=%scm];' % (G, DASH, R, R, ry),
              '\\draw[color=%s, line width=1pt, fill=%s, fill opacity=0.15] (0,%s) ellipse (%scm and %scm);' % (G, col('86e0bd'), H, R, ry),
              '\\draw[color=%s, line width=1pt] (-%s,0) -- (-%s,%s) (%s,0) -- (%s,%s);' % (G, R, R, H, R, R, H),
              '\\draw[ink, line width=0.7pt, %s] (0,0) -- (0,%s);' % (DASH, H), '\\draw[color=%s, line width=1pt] (0,0) -- (%s,0);' % (O_, R),
              '\\fill[ink] (0,0) circle (1.4pt); \\fill[ink] (0,%s) circle (1.4pt);' % H,
              '\\node[font=\\small, text=ink, below] at (%s,0) {$%s$};' % (R / 2, labs[0]), '\\node[font=\\small, text=ink, left] at (0,%s) {$%s$};' % (H / 2 + 0.25, labs[1])]
    elif kind == 'cone':
        R, ry, H = 1.4, 0.4, 2.8
        o += ['\\draw[color=%s, line width=1pt, fill=%s, fill opacity=0.12] (-%s,0) arc[start angle=180, end angle=360, x radius=%scm, y radius=%scm] -- (0,%s) -- cycle;' % (G, col('86e0bd'), R, R, ry, H),
              '\\draw[color=%s, line width=0.8pt, %s] (%s,0) arc[start angle=0, end angle=180, x radius=%scm, y radius=%scm];' % (G, DASH, R, R, ry),
              '\\draw[ink, line width=0.7pt, %s] (0,0) -- (0,%s);' % (DASH, H), '\\draw[color=%s, line width=1pt] (0,0) -- (%s,0);' % (O_, R),
              '\\draw[ink, line width=0.6pt] (0,0.2) -- (0.2,0.2) -- (0.2,0);',
              '\\fill[ink] (0,0) circle (1.4pt); \\fill[ink] (0,%s) circle (1.4pt);' % H,
              '\\node[font=\\small, text=ink, below] at (%s,-0.02) {$%s$};' % (R / 2 + 0.1, labs[0]), '\\node[font=\\small, text=ink, left] at (0,%s) {$%s$};' % (H / 2, labs[1]),
              '\\node[font=\\small, text=ink, right] at (%s,%s) {$%s$};' % (R / 2 + 0.12, H / 2 + 0.1, labs[2])]
    else:
        R, ry = 1.6, 0.42
        o += ['\\shade[ball color=%s, opacity=0.25] (0,0) circle (%s);' % ('white', R), '\\draw[color=%s, line width=1pt] (0,0) circle (%s);' % (G, R),
              '\\draw[color=%s, line width=0.9pt] (-%s,0) arc[start angle=180, end angle=360, x radius=%scm, y radius=%scm];' % (G, R, R, ry),
              '\\draw[color=%s, line width=0.7pt, %s] (%s,0) arc[start angle=0, end angle=180, x radius=%scm, y radius=%scm];' % (G, DASH, R, R, ry),
              '\\draw[color=%s, line width=1pt] (0,0) -- (%s,%s);' % (O_, R * math.cos(math.radians(40)), R * math.sin(math.radians(40))),
              '\\fill[ink] (0,0) circle (1.4pt);', '\\node[font=\\small, text=ink, above left] at (0,0) {$O$};',
              '\\node[font=\\small, text=ink, above left] at (%s,%s) {$%s$};' % (R * 0.45, R * 0.35, labs[0])]
    o.append('\\end{tikzpicture}')
    return texsvg('\n'.join(o))


def SOLID(kind, labs=('r', 'h', 'l'), px=200):
    fn = solid_svg(kind, labs); return (img(fn, 'Figure', px), img(fn, 'Hình vẽ', px))


# =====================================================================================================
# BÀI 31. Hình trụ và hình nón
# =====================================================================================================
def b31_cyl_lat(r, lv):
    rr, h = r.randint(2, 9), r.randint(3, 15)
    return dict(en='A cylinder has base radius %d cm and height %d cm. Find its lateral area.' % (rr, h), vi='Một hình trụ có bán kính đáy %d cm và chiều cao %d cm. Tính diện tích xung quanh của hình trụ.' % (rr, h),
                opts=piopts(r, 2 * rr * h, [rr * h, rr * rr * h, 2 * rr * h + 2 * rr * rr, 4 * rr * h]), ans=0,
                ee='\\(S_{xq}=2\\pi rh=2\\pi\\cdot%d\\cdot%d=%s\\).' % (rr, h, pi(2 * rr * h, 'cm', 2)), ev='\\(S_{xq}=2\\pi rh=2\\pi\\cdot%d\\cdot%d=%s\\).' % (rr, h, pi(2 * rr * h, 'cm', 2)), fig=SOLID('cyl'))


def b31_cone_vol(r, lv):
    rr = r.randint(2, 9); h = 3 * r.randint(1, 5)
    return dict(en='A cone has base radius %d cm and height %d cm. Find its volume.' % (rr, h), vi='Một hình nón có bán kính đáy %d cm và chiều cao %d cm. Tính thể tích hình nón.' % (rr, h),
                opts=piopts(r, F(rr * rr * h, 3), [rr * rr * h, F(rr * h, 3), F(rr * rr * h, 2)], p=3), ans=0,
                ee='\\(V=\\dfrac13\\pi r^2h=\\dfrac13\\pi\\cdot%d^2\\cdot%d=%s\\).' % (rr, h, pi(F(rr * rr * h, 3), 'cm', 3)), ev='\\(V=\\dfrac13\\pi r^2h=\\dfrac13\\pi\\cdot%d^2\\cdot%d=%s\\).' % (rr, h, pi(F(rr * rr * h, 3), 'cm', 3)), fig=SOLID('cone'))


def b31_slant(r, lv):
    a, b, c = r.choice(PYT[:7]); rr, h = (a, b) if r.random() < 0.5 else (b, a)
    return dict(en='A cone has base radius %d cm and height %d cm. Find its slant height \\(l\\).' % (rr, h), vi='Một hình nón có bán kính đáy %d cm và chiều cao %d cm. Tính độ dài đường sinh \\(l\\).' % (rr, h),
                opts=nopts(r, c, [rr + h, abs(h - rr) or c + 1, c + 2, F(rr + h, 2)]), ans=0,
                ee='\\(l=\\sqrt{r^2+h^2}=\\sqrt{%d^2+%d^2}=%d\\) cm.' % (rr, h, c), ev='\\(l=\\sqrt{r^2+h^2}=\\sqrt{%d^2+%d^2}=%d\\) cm.' % (rr, h, c), fig=SOLID('cone'))


def b31_tf_cylv(r, lv):
    rr, h = r.randint(2, 8), r.randint(2, 12); g = rr * rr * h; truth = r.random() < 0.5; claim = g if truth else r.choice([2 * rr * h, rr * h * 2 * rr, F(g, 3)])
    if claim == g: truth = True
    return dict(en='A cylinder with base radius %d cm and height %d cm has volume \\(%s\\).' % (rr, h, pi(claim, 'cm', 3)), vi='Hình trụ có bán kính đáy %d cm, chiều cao %d cm có thể tích \\(%s\\).' % (rr, h, pi(claim, 'cm', 3)), ans=truth,
                ee='\\(V=\\pi r^2h=%s\\).' % pi(g, 'cm', 3), ev='\\(V=\\pi r^2h=%s\\).' % pi(g, 'cm', 3))


def b31_tf_conel(r, lv):
    rr, l = r.randint(2, 8), r.randint(9, 20); g = rr * l; truth = r.random() < 0.5; claim = g if truth else r.choice([2 * rr * l, rr * l + rr * rr, F(rr * l, 2)])
    if claim == g: truth = True
    return dict(en='A cone with base radius %d cm and slant height %d cm has lateral area \\(%s\\).' % (rr, l, pi(claim, 'cm', 2)), vi='Hình nón có bán kính đáy %d cm, đường sinh %d cm có diện tích xung quanh \\(%s\\).' % (rr, l, pi(claim, 'cm', 2)), ans=truth,
                ee='\\(S_{xq}=\\pi rl=%s\\).' % pi(g, 'cm', 2), ev='\\(S_{xq}=\\pi rl=%s\\).' % pi(g, 'cm', 2))


def b31_short_cylv(r, lv):
    rr, h = r.randint(2, 7), r.randint(2, 12); g = rr * rr * h
    return dict(en='A cylindrical can has base radius %d cm and height %d cm. Its volume is \\(k\\pi\\) cm³. Find \\(k\\).' % (rr, h), vi='Một lon hình trụ có bán kính đáy %d cm, chiều cao %d cm. Thể tích của lon là \\(k\\pi\\) cm³. Tìm \\(k\\).' % (rr, h), key=str(g),
                ee='\\(V=\\pi r^2h=\\pi\\cdot%d\\cdot%d=%d\\pi\\).' % (rr * rr, h, g), ev='\\(V=\\pi r^2h=\\pi\\cdot%d\\cdot%d=%d\\pi\\).' % (rr * rr, h, g))


def b31_short_conetot(r, lv):
    a, b, c = r.choice(PYT[:5]); rr, h = (a, b) if r.random() < 0.5 else (b, a); g = rr * c + rr * rr
    return dict(en='A cone has base radius %d cm and height %d cm. Its total surface area (lateral surface and base) is \\(k\\pi\\) cm². Find \\(k\\).' % (rr, h),
                vi='Hình nón có bán kính đáy %d cm, chiều cao %d cm. Diện tích toàn phần (xung quanh và đáy) là \\(k\\pi\\) cm². Tìm \\(k\\).' % (rr, h), key=str(g),
                ee='\\(l=\\sqrt{%d^2+%d^2}=%d\\); \\(S=\\pi rl+\\pi r^2=%d\\pi+%d\\pi=%d\\pi\\).' % (rr, h, c, rr * c, rr * rr, g),
                ev='\\(l=\\sqrt{%d^2+%d^2}=%d\\); \\(S=\\pi rl+\\pi r^2=%d\\pi+%d\\pi=%d\\pi\\).' % (rr, h, c, rr * c, rr * rr, g))


def b31_d1_names(r, lv):
    k = r.choice(['gen', 'cylh', 'base'])
    if k == 'gen':
        o = [tx('a slant height (generatrix)', 'đường sinh'), tx('the height', 'đường cao'), tx('a radius of the base', 'bán kính đáy'), tx('a diameter of the base', 'đường kính đáy')]
        return dict(en='In a cone with vertex \\(S\\), the segment joining \\(S\\) to a point \\(A\\) on the circle of the base is…', vi='Trong hình nón đỉnh \\(S\\), đoạn thẳng nối \\(S\\) với một điểm \\(A\\) trên đường tròn đáy là…', opts=o, ans=0,
                    ee='\\(SA\\) is a slant height (generatrix) \\(l\\).', ev='\\(SA\\) là một đường sinh \\(l\\).', fig=SOLID('cone', ('r', 'h', 'SA')))
    if k == 'cylh':
        o = [tx('the height of the cylinder', 'chiều cao của hình trụ'), tx('the radius of the base', 'bán kính đáy'), tx('the diameter of the base', 'đường kính đáy'), tx('half the height', 'một nửa chiều cao')]
        return dict(en='For a cylinder, the length of each generatrix equals…', vi='Ở hình trụ, độ dài mỗi đường sinh bằng…', opts=o, ans=0, ee='The generatrices of a cylinder are parallel to the axis and equal to the height.', ev='Các đường sinh của hình trụ song song với trục và bằng chiều cao.')
    o = [tx('two equal circles (disks) in parallel planes', 'hai hình tròn bằng nhau nằm trong hai mặt phẳng song song'), tx('one circle', 'một hình tròn'), tx('two squares', 'hai hình vuông'), tx('two circles of different sizes', 'hai hình tròn khác nhau')]
    return dict(en='The two bases of a cylinder are…', vi='Hai đáy của hình trụ là…', opts=o, ans=0, ee='A cylinder has two equal circular bases in parallel planes.', ev='Hình trụ có hai đáy là hai hình tròn bằng nhau nằm trong hai mặt phẳng song song.')


def b31_d1_formula(r, lv):
    k = r.choice(['cylV', 'coneS', 'cylS', 'coneV'])
    F_ = {'cylV': (['V=\\pi r^2h', 'V=\\dfrac13\\pi r^2h', 'V=2\\pi rh', 'V=\\pi rh'], 'the volume of a cylinder', 'thể tích hình trụ'),
          'coneS': (['S_{xq}=\\pi rl', 'S_{xq}=2\\pi rl', 'S_{xq}=\\pi r^2l', 'S_{xq}=\\dfrac13\\pi rl'], 'the lateral area of a cone', 'diện tích xung quanh hình nón'),
          'cylS': (['S_{xq}=2\\pi rh', 'S_{xq}=\\pi rh', 'S_{xq}=\\pi r^2h', 'S_{xq}=2\\pi r^2'], 'the lateral area of a cylinder', 'diện tích xung quanh hình trụ'),
          'coneV': (['V=\\dfrac13\\pi r^2h', 'V=\\pi r^2h', 'V=\\dfrac12\\pi r^2h', 'V=\\pi rl'], 'the volume of a cone', 'thể tích hình nón')}[k]
    return dict(en='Which formula gives %s?' % F_[1], vi='Công thức nào cho %s?' % F_[2], opts=F_[0], ans=0, ee='\\(%s\\).' % F_[0][0], ev='\\(%s\\).' % F_[0][0])


def b31_d1_rotate(r, lv):
    a, b = r.sample(range(2, 10), 2); k = r.choice(['rect', 'tri'])
    if k == 'rect':
        o = [tx('a cylinder with radius %d cm and height %d cm' % (b, a), 'hình trụ có bán kính đáy %d cm và chiều cao %d cm' % (b, a)), tx('a cylinder with radius %d cm and height %d cm' % (a, b), 'hình trụ có bán kính đáy %d cm và chiều cao %d cm' % (a, b)),
             tx('a cone with radius %d cm and height %d cm' % (b, a), 'hình nón có bán kính đáy %d cm và chiều cao %d cm' % (b, a)), tx('a sphere of radius %d cm' % a, 'hình cầu bán kính %d cm' % a)]
        return dict(en='Rectangle \\(ABCD\\) with \\(AB=%d\\) cm, \\(BC=%d\\) cm is rotated one full turn about the side \\(AB\\). We get…' % (a, b), vi='Quay hình chữ nhật \\(ABCD\\) có \\(AB=%d\\) cm, \\(BC=%d\\) cm một vòng quanh cạnh \\(AB\\), ta được…' % (a, b), opts=o, ans=0,
                    ee='\\(AB\\) is the axis (height \\(%d\\)); \\(BC\\perp AB\\) sweeps the base (radius \\(%d\\)).' % (a, b), ev='\\(AB\\) là trục (chiều cao \\(%d\\)); \\(BC\\perp AB\\) quét thành đáy (bán kính \\(%d\\)).' % (a, b))
    o = [tx('a cone with radius %d cm and height %d cm' % (b, a), 'hình nón có bán kính đáy %d cm và chiều cao %d cm' % (b, a)), tx('a cone with radius %d cm and height %d cm' % (a, b), 'hình nón có bán kính đáy %d cm và chiều cao %d cm' % (a, b)),
         tx('a cylinder with radius %d cm and height %d cm' % (b, a), 'hình trụ có bán kính đáy %d cm và chiều cao %d cm' % (b, a)), tx('a sphere of radius %d cm' % b, 'hình cầu bán kính %d cm' % b)]
    return dict(en='Triangle \\(ABC\\), right-angled at \\(A\\), with \\(AB=%d\\) cm, \\(AC=%d\\) cm, is rotated one full turn about \\(AB\\). We get…' % (a, b), vi='Quay tam giác \\(ABC\\) vuông tại \\(A\\) có \\(AB=%d\\) cm, \\(AC=%d\\) cm một vòng quanh cạnh \\(AB\\), ta được…' % (a, b), opts=o, ans=0,
                ee='\\(AB\\) is the height (\\(%d\\)), \\(AC\\) is the base radius (\\(%d\\)).' % (a, b), ev='\\(AB\\) là đường cao (\\(%d\\)), \\(AC\\) là bán kính đáy (\\(%d\\)).' % (a, b))


def b31_d2_total(r, lv):
    rr, h = r.randint(2, 8), r.randint(3, 12); g = 2 * rr * h + 2 * rr * rr
    return dict(en='A closed cylindrical box has base radius %d cm and height %d cm. Find its total surface area.' % (rr, h), vi='Một hộp hình trụ có nắp, bán kính đáy %d cm, chiều cao %d cm. Tính diện tích toàn phần của hộp.' % (rr, h),
                opts=piopts(r, g, [2 * rr * h, 2 * rr * h + rr * rr, rr * rr * h]), ans=0,
                ee='\\(S=2\\pi rh+2\\pi r^2=%d\\pi+%d\\pi=%s\\).' % (2 * rr * h, 2 * rr * rr, pi(g, 'cm', 2)), ev='\\(S=2\\pi rh+2\\pi r^2=%d\\pi+%d\\pi=%s\\).' % (2 * rr * h, 2 * rr * rr, pi(g, 'cm', 2)))


def b31_d2_rotv(r, lv):
    a = 3 * r.randint(1, 4); b = r.randint(2, 7)
    g = F(b * b * a, 3)
    return dict(en='Right triangle \\(ABC\\) (right angle at \\(A\\)), \\(AB=%d\\) cm, \\(AC=%d\\) cm, is rotated about \\(AB\\). Find the volume of the solid obtained.' % (a, b),
                vi='Quay tam giác \\(ABC\\) vuông tại \\(A\\) có \\(AB=%d\\) cm, \\(AC=%d\\) cm quanh cạnh \\(AB\\). Tính thể tích hình nhận được.' % (a, b),
                opts=piopts(r, g, [b * b * a, F(a * a * b, 3), F(b * b * a, 2)], p=3), ans=0,
                ee='A cone with \\(r=%d\\), \\(h=%d\\): \\(V=\\dfrac13\\pi\\cdot%d^2\\cdot%d=%s\\).' % (b, a, b, a, pi(g, 'cm', 3)), ev='Hình nón có \\(r=%d\\), \\(h=%d\\): \\(V=\\dfrac13\\pi\\cdot%d^2\\cdot%d=%s\\).' % (b, a, b, a, pi(g, 'cm', 3)))


def b31_d2_compare(r, lv):
    rr, h = r.randint(2, 9), r.randint(3, 12); k = r.choice(['cyl', 'cone'])
    if k == 'cyl':
        return dict(en='A cone and a cylinder have the same base (radius %d cm) and the same height (%d cm). The volume of the cylinder is how many times that of the cone?' % (rr, h),
                    vi='Một hình nón và một hình trụ có cùng đáy (bán kính %d cm) và cùng chiều cao (%d cm). Thể tích hình trụ gấp bao nhiêu lần thể tích hình nón?' % (rr, h),
                    opts=['3', '2', '\\dfrac13', '%d' % rr if rr not in (2, 3) else '4'], ans=0, ee='\\(\\pi r^2h=3\\cdot\\dfrac13\\pi r^2h\\).', ev='\\(\\pi r^2h=3\\cdot\\dfrac13\\pi r^2h\\).')
    V = rr * rr * h
    return dict(en='A cylindrical glass (radius %d cm, height %d cm) is full of water. The water is poured into conical cups with the same radius and the same height. How many cups can be filled?' % (rr, h),
                vi='Một cốc hình trụ (bán kính %d cm, cao %d cm) đầy nước. Rót nước sang các cốc hình nón có cùng bán kính đáy và cùng chiều cao. Rót đầy được bao nhiêu cốc hình nón?' % (rr, h),
                opts=['3', '2', '4', '6'], ans=0, ee='\\(\\dfrac{\\pi r^2h}{\\frac13\\pi r^2h}=3\\).', ev='\\(\\dfrac{\\pi r^2h}{\\frac13\\pi r^2h}=3\\).')


def b31_d3_tank(r, lv):
    d = r.choice([1, 2]); rr = F(r.choice([5, 6, 8, 10]), 10) if d == 1 else r.choice([1, 2]); h = r.choice([1, 2, 3])
    rr = F(rr); V = rr * rr * h; L = V * 1000
    return dict(en='A cylindrical water tank has base radius %s m and height %d m. How many liters does it hold? (\\(1\\text{ m}^3=1000\\) liters; use \\(\\pi\\approx3.14\\); round to the nearest liter.)' % (pe(rr), h),
                vi='Một bồn nước hình trụ có bán kính đáy %s m, chiều cao %d m. Bồn chứa được bao nhiêu lít nước? (\\(1\\text{ m}^3=1000\\) lít; lấy \\(\\pi\\approx3{,}14\\); làm tròn đến lít.)' % (pv(rr), h),
                opts=pick_opts(r, tx('\\(%d\\) liters' % round(3.14 * float(L)), '\\(%d\\) lít' % round(3.14 * float(L))),
                               [tx('\\(%d\\) liters' % round(x), '\\(%d\\) lít' % round(x)) for x in (3.14 * float(L) * 2, 3.14 * float(L) / 3, 3.14 * float(rr) * h * 1000 * 2)]), ans=0,
                ee='\\(V=\\pi r^2h\\approx3.14\\cdot%s^2\\cdot%d=%s\\) m³ \\(=%d\\) liters.' % (pe(rr), h, pe(F(314, 100) * V), round(3.14 * float(L))),
                ev='\\(V=\\pi r^2h\\approx3{,}14\\cdot%s^2\\cdot%d=%s\\) m³ \\(=%d\\) lít.' % (dm(pe(rr)), h, dm(pe(F(314, 100) * V)), round(3.14 * float(L))))


def b31_d3_hat(r, lv):
    rr, l = r.choice([(20, 30), (18, 30), (24, 30), (21, 35), (20, 25), (15, 25)])
    return dict(en='A conical palm-leaf hat has base radius %d cm and slant height %d cm. Find the area of leaves needed to cover its lateral surface.' % (rr, l), vi='Một chiếc nón lá hình nón có bán kính đáy %d cm, đường sinh %d cm. Tính diện tích lá cần để phủ mặt xung quanh của nón.' % (rr, l),
                opts=piopts(r, rr * l, [2 * rr * l, rr * l + rr * rr, F(rr * l, 2)]), ans=0,
                ee='\\(S_{xq}=\\pi rl=\\pi\\cdot%d\\cdot%d=%s\\).' % (rr, l, pi(rr * l, 'cm', 2)), ev='\\(S_{xq}=\\pi rl=\\pi\\cdot%d\\cdot%d=%s\\).' % (rr, l, pi(rr * l, 'cm', 2)))


def b31_d3_sector(r, lv):
    rr, l = r.choice([(3, 9), (4, 12), (5, 10), (6, 9), (2, 8), (5, 15), (3, 12), (4, 6)])
    a = F(360 * rr, l)
    return dict(en='The lateral surface of a cone (base radius %d cm, slant height %d cm) is cut open into a sector. Find the central angle of the sector.' % (rr, l),
                vi='Cắt mặt xung quanh của hình nón (bán kính đáy %d cm, đường sinh %d cm) rồi trải phẳng thành một hình quạt. Tính số đo cung (góc ở tâm) của hình quạt.' % (rr, l),
                opts=dopts(r, a, [F(180 * rr, l), F(360 * l, rr) if F(360 * l, rr) < 360 else a + 30, 360 - a]), ans=0,
                ee='Arc length = base circumference: \\(\\dfrac{\\pi l\\alpha}{180}=2\\pi r\\Rightarrow\\alpha=\\dfrac{360r}{l}=%s\\).' % deg(a), ev='Độ dài cung = chu vi đáy: \\(\\dfrac{\\pi l\\alpha}{180}=2\\pi r\\Rightarrow\\alpha=\\dfrac{360r}{l}=%s\\).' % degv(a))


def b31_d4_party(r, lv):
    L, ang = r.choice([(10, 216), (10, 288), (15, 216), (15, 288), (20, 216), (20, 288), (25, 216), (25, 288), (30, 216)])
    rr = F(L * ang, 360); h2 = L * L - rr * rr
    ok = h2.denominator == 1 and int(math.isqrt(int(h2))) ** 2 == h2
    if not ok: raise AssertionError
    h = math.isqrt(int(h2))
    return dict(en='A party hat is made by rolling a sector of radius %d cm and central angle \\(%d^\\circ\\) into a cone (no overlap). Find the height of the hat.' % (L, ang),
                vi='Một chiếc mũ sinh nhật được làm bằng cách cuộn một hình quạt bán kính %d cm, số đo cung \\(%d^\\circ\\) thành hình nón (không chồng mép). Tính chiều cao của mũ.' % (L, ang),
                opts=nopts(r, h, [L, int(rr), L - int(rr), h + 3]), ans=0,
                ee='\\(l=%d\\); \\(2\\pi r=\\dfrac{\\pi\\cdot%d\\cdot%d}{180}\\Rightarrow r=%s\\); \\(h=\\sqrt{%d^2-%s^2}=%d\\) cm.' % (L, L, ang, pe(rr), L, pe(rr), h),
                ev='\\(l=%d\\); \\(2\\pi r=\\dfrac{\\pi\\cdot%d\\cdot%d}{180}\\Rightarrow r=%s\\); \\(h=\\sqrt{%d^2-%s^2}=%d\\) cm.' % (L, L, ang, dm(pe(rr)), L, dm(pe(rr)), h))


def b31_d4_paint(r, lv):
    d, h, cost = r.choice([(2, 5, 50), (4, 3, 25), (3, 2, 50), (2, 3, 50), (1, 4, 25), (2, 2, 25)])
    rr = F(d, 2); S = 2 * rr * h; money = S * F(314, 100) * cost
    if money.denominator != 1: raise AssertionError
    return dict(en='A cylindrical column has diameter %d m and height %d m. Painting costs %d thousand VND per m². How much does it cost to paint its lateral surface? (\\(\\pi\\approx3.14\\))' % (d, h, cost),
                vi='Một cột trụ hình trụ có đường kính %d m, chiều cao %d m. Sơn mỗi mét vuông tốn %d nghìn đồng. Chi phí sơn mặt xung quanh cột là bao nhiêu? (\\(\\pi\\approx3{,}14\\))' % (d, h, cost),
                opts=pick_opts(r, tx('%s thousand VND' % pe(money), '%s nghìn đồng' % pv(money)), [tx('%s thousand VND' % pe(x), '%s nghìn đồng' % pv(x)) for x in (money * 2, money / 2, money * 3 / 2)]), ans=0,
                ee='\\(S_{xq}=2\\pi rh=\\pi dh\\approx3.14\\cdot%d\\cdot%d=%s\\) m²; cost \\(%s\\cdot%d=%s\\) thousand VND.' % (d, h, pe(S * F(314, 100)), pe(S * F(314, 100)), cost, pe(money)),
                ev='\\(S_{xq}=2\\pi rh=\\pi dh\\approx3{,}14\\cdot%d\\cdot%d=%s\\) m²; chi phí \\(%s\\cdot%d=%s\\) nghìn đồng.' % (d, h, dm(pe(S * F(314, 100))), dm(pe(S * F(314, 100))), cost, dm(pe(money))))


def b31_d4_melt(r, lv):
    R, H = r.choice([(6, 10), (4, 9), (3, 8), (5, 6), (6, 5)]); rc, hc = r.choice([(2, 3), (3, 2), (1, 3), (2, 5)])
    Vc = F(R * R * H); Vk = F(rc * rc * hc, 3); n = Vc / Vk
    if n.denominator != 1: raise AssertionError
    return dict(en='A metal cylinder (radius %d cm, height %d cm) is melted and recast into small cones of radius %d cm and height %d cm. How many cones are made?' % (R, H, rc, hc),
                vi='Nấu chảy một khối kim loại hình trụ (bán kính %d cm, cao %d cm) để đúc thành các khối hình nón bán kính đáy %d cm, cao %d cm. Đúc được bao nhiêu khối nón?' % (R, H, rc, hc),
                opts=iopts(r, int(n), [int(n) // 3, int(F(R * R * H, rc * rc * hc)), int(n) + 3]), ans=0,
                ee='\\(\\dfrac{\\pi\\cdot%d^2\\cdot%d}{\\frac13\\pi\\cdot%d^2\\cdot%d}=%d\\).' % (R, H, rc, hc, n), ev='\\(\\dfrac{\\pi\\cdot%d^2\\cdot%d}{\\frac13\\pi\\cdot%d^2\\cdot%d}=%d\\).' % (R, H, rc, hc, n))


L31_GROUPS = [[('mcq', b31_cyl_lat), ('mcq', b31_cone_vol), ('mcq', b31_slant)], [('tf', b31_tf_cylv), ('tf', b31_tf_conel)], [('short', b31_short_cylv), ('short', b31_short_conetot)],
              [('mcq', b31_d1_names), ('mcq', b31_d1_formula), ('mcq', b31_d1_rotate)], [('mcq', b31_d2_total), ('mcq', b31_d2_rotv), ('mcq', b31_d2_compare)],
              [('mcq', b31_d3_tank), ('mcq', b31_d3_hat), ('mcq', b31_d3_sector)], [('mcq', b31_d4_party), ('mcq', b31_d4_paint), ('mcq', b31_d4_melt)]]


# =====================================================================================================
# BÀI 32. Hình cầu
# =====================================================================================================
def b32_area(r, lv):
    R = r.randint(2, 12); dia = r.random() < 0.4; t = ('diameter %d cm' % (2 * R), 'đường kính %d cm' % (2 * R)) if dia else ('radius %d cm' % R, 'bán kính %d cm' % R)
    return dict(en='A sphere has %s. Find the area of its surface.' % t[0], vi='Một hình cầu có %s. Tính diện tích mặt cầu.' % t[1],
                opts=piopts(r, 4 * R * R, [R * R, 2 * R * R, F(4 * R ** 3, 3), 16 * R * R if dia else 4 * R]), ans=0,
                ee='\\(S=4\\pi R^2=4\\pi\\cdot%d^2=%s\\).' % (R, pi(4 * R * R, 'cm', 2)), ev='\\(S=4\\pi R^2=4\\pi\\cdot%d^2=%s\\).' % (R, pi(4 * R * R, 'cm', 2)), fig=SOLID('sph', ('R',)))


def b32_vol(r, lv):
    R = 3 * r.randint(1, 4)
    return dict(en='Find the volume of a ball of radius %d cm.' % R, vi='Tính thể tích hình cầu bán kính %d cm.' % R,
                opts=piopts(r, F(4 * R ** 3, 3), [4 * R * R, R ** 3, F(4 * R * R, 3), 4 * R ** 3], p=3), ans=0,
                ee='\\(V=\\dfrac43\\pi R^3=\\dfrac43\\pi\\cdot%d^3=%s\\).' % (R, pi(F(4 * R ** 3, 3), 'cm', 3)), ev='\\(V=\\dfrac43\\pi R^3=\\dfrac43\\pi\\cdot%d^3=%s\\).' % (R, pi(F(4 * R ** 3, 3), 'cm', 3)))


def b32_section(r, lv):
    a, b, c = r.choice(PYT[:7]); d, rr = (a, b) if r.random() < 0.5 else (b, a)
    return dict(en='A plane at distance %d cm from the center of a sphere of radius %d cm cuts the sphere. Find the radius of the cross-section.' % (d, c),
                vi='Một mặt phẳng cách tâm hình cầu bán kính %d cm một khoảng %d cm cắt hình cầu. Tính bán kính của mặt cắt.' % (c, d),
                opts=nopts(r, rr, [c - d, c + d, d, F(c, 2)]), ans=0,
                ee='The cross-section is a circle of radius \\(\\sqrt{R^2-d^2}=\\sqrt{%d^2-%d^2}=%d\\) cm.' % (c, d, rr), ev='Mặt cắt là hình tròn bán kính \\(\\sqrt{R^2-d^2}=\\sqrt{%d^2-%d^2}=%d\\) cm.' % (c, d, rr))


def b32_tf_area(r, lv):
    R = r.randint(2, 10); truth = r.random() < 0.5; claim = 4 * R * R if truth else r.choice([2 * R * R, R * R, 8 * R * R])
    return dict(en='A ball of radius %d cm has surface area \\(%s\\).' % (R, pi(claim, 'cm', 2)), vi='Hình cầu bán kính %d cm có diện tích mặt cầu là \\(%s\\).' % (R, pi(claim, 'cm', 2)), ans=truth,
                ee='\\(4\\pi R^2=%s\\).' % pi(4 * R * R, 'cm', 2), ev='\\(4\\pi R^2=%s\\).' % pi(4 * R * R, 'cm', 2))


def b32_tf_half(r, lv):
    R = 3 * r.randint(1, 4); g = F(2 * R ** 3, 3); truth = r.random() < 0.5; claim = g if truth else r.choice([F(4 * R ** 3, 3), 2 * R ** 3, F(R ** 3, 3)])
    return dict(en='A hemisphere of radius %d cm has volume \\(%s\\).' % (R, pi(claim, 'cm', 3)), vi='Nửa hình cầu bán kính %d cm có thể tích \\(%s\\).' % (R, pi(claim, 'cm', 3)), ans=truth,
                ee='\\(\\dfrac12\\cdot\\dfrac43\\pi R^3=\\dfrac23\\pi\\cdot%d^3=%s\\).' % (R, pi(g, 'cm', 3)), ev='\\(\\dfrac12\\cdot\\dfrac43\\pi R^3=\\dfrac23\\pi\\cdot%d^3=%s\\).' % (R, pi(g, 'cm', 3)))


def b32_short_s(r, lv):
    d = 2 * r.randint(1, 10); R = d // 2
    return dict(en='A ball has diameter %d cm. Its surface area is \\(k\\pi\\) cm². Find \\(k\\).' % d, vi='Một quả bóng có đường kính %d cm. Diện tích mặt cầu là \\(k\\pi\\) cm². Tìm \\(k\\).' % d, key=str(4 * R * R),
                ee='\\(R=%d\\); \\(S=4\\pi\\cdot%d^2=%d\\pi\\).' % (R, R, 4 * R * R), ev='\\(R=%d\\); \\(S=4\\pi\\cdot%d^2=%d\\pi\\).' % (R, R, 4 * R * R))


def b32_short_v(r, lv):
    R = 3 * r.randint(1, 3); k = F(4 * R ** 3, 3)
    return dict(en='A ball has radius %d cm. Its volume is \\(k\\pi\\) cm³. Find \\(k\\).' % R, vi='Hình cầu có bán kính %d cm. Thể tích là \\(k\\pi\\) cm³. Tìm \\(k\\).' % R, key=pe(k),
                ee='\\(V=\\dfrac43\\pi\\cdot%d^3=%s\\pi\\).' % (R, pe(k)), ev='\\(V=\\dfrac43\\pi\\cdot%d^3=%s\\pi\\).' % (R, pe(k)))


def b32_d1_terms(r, lv):
    k = r.choice(['great', 'section', 'surface'])
    if k == 'great':
        o = [tx('a great circle (radius equal to the radius of the sphere)', 'đường tròn lớn (bán kính bằng bán kính hình cầu)'), tx('a point', 'một điểm'), tx('an ellipse', 'một hình elip'), tx('a small circle of half the radius', 'đường tròn có bán kính bằng một nửa')]
        return dict(en='A plane through the center of a sphere cuts its surface in…', vi='Mặt phẳng đi qua tâm cắt mặt cầu theo…', opts=o, ans=0, ee='The cross-section through the center is a great circle.', ev='Mặt cắt qua tâm là đường tròn lớn.')
    if k == 'section':
        o = [tx('a circle (disk)', 'một hình tròn'), tx('a square', 'một hình vuông'), tx('a triangle', 'một tam giác'), tx('an ellipse that is not a circle', 'một hình elip không phải hình tròn')]
        return dict(en='Every plane cutting a ball (and not just touching it) gives a cross-section that is…', vi='Mọi mặt phẳng cắt hình cầu (không chỉ tiếp xúc) đều cho mặt cắt là…', opts=o, ans=0, ee='The cross-section of a ball is always a disk.', ev='Mặt cắt của hình cầu luôn là một hình tròn.')
    o = [tx('a surface of a sphere', 'mặt cầu'), tx('a solid ball', 'hình cầu (khối)'), tx('a great circle', 'đường tròn lớn'), tx('a hemisphere', 'nửa hình cầu')]
    return dict(en='The set of all points in space at distance \\(R\\) from a point \\(O\\) is…', vi='Tập hợp tất cả các điểm trong không gian cách điểm \\(O\\) một khoảng \\(R\\) là…', opts=o, ans=0,
                ee='Points at distance exactly \\(R\\) form the surface of the sphere; the solid ball also contains the inside points.', ev='Các điểm cách \\(O\\) đúng \\(R\\) tạo thành mặt cầu; hình cầu (khối) gồm cả các điểm bên trong.')


def b32_d1_formula(r, lv):
    k = r.choice(['S', 'V', 'Sh'])
    if k == 'S': o = ['S=4\\pi R^2', 'S=\\pi R^2', 'S=2\\pi R^2', 'S=\\dfrac43\\pi R^2']; en, vi = 'the area of the surface of a sphere', 'diện tích mặt cầu'
    elif k == 'V': o = ['V=\\dfrac43\\pi R^3', 'V=4\\pi R^3', 'V=\\dfrac13\\pi R^3', 'V=\\pi R^3']; en, vi = 'the volume of a ball', 'thể tích hình cầu'
    else: o = ['V=\\dfrac23\\pi R^3', 'V=\\dfrac43\\pi R^3', 'V=\\dfrac13\\pi R^3', 'V=2\\pi R^3']; en, vi = 'the volume of a hemisphere', 'thể tích nửa hình cầu'
    return dict(en='Which formula gives %s of radius \\(R\\)?' % en, vi='Công thức nào cho %s bán kính \\(R\\)?' % vi, opts=o, ans=0, ee='\\(%s\\).' % o[0], ev='\\(%s\\).' % o[0])


def b32_d1_dia(r, lv):
    d = 2 * r.randint(2, 20)
    return dict(en='A ball has diameter %d cm. What is its radius?' % d, vi='Một hình cầu có đường kính %d cm. Bán kính của nó là bao nhiêu?' % d,
                opts=nopts(r, d // 2, [d, 2 * d, d // 4 if d % 4 == 0 else d // 2 + 1]), ans=0, ee='\\(R=\\dfrac{d}{2}=%d\\) cm.' % (d // 2), ev='\\(R=\\dfrac{d}{2}=%d\\) cm.' % (d // 2))


def b32_d2_scale(r, lv):
    k = r.choice([2, 3]); what = r.choice(['S', 'V'])
    g = k * k if what == 'S' else k ** 3
    return dict(en='The radius of a ball is multiplied by %d. Its %s is multiplied by…' % (k, 'surface area' if what == 'S' else 'volume'), vi='Bán kính hình cầu tăng gấp %d lần. %s tăng gấp bao nhiêu lần?' % (k, 'Diện tích mặt cầu' if what == 'S' else 'Thể tích hình cầu'),
                opts=iopts(r, g, [k, k * k if what == 'V' else k ** 3, 2 * k]), ans=0,
                ee='\\(S\\) is proportional to \\(R^2\\), \\(V\\) to \\(R^3\\): factor \\(%d\\).' % g, ev='\\(S\\) tỉ lệ với \\(R^2\\), \\(V\\) tỉ lệ với \\(R^3\\): gấp \\(%d\\) lần.' % g)


def b32_d2_fromS(r, lv):
    R = r.randint(2, 12); S = 4 * R * R
    return dict(en='The surface of a sphere has area \\(%s\\). Find the radius.' % pi(S, 'cm', 2), vi='Mặt cầu có diện tích \\(%s\\). Tính bán kính hình cầu.' % pi(S, 'cm', 2),
                opts=nopts(r, R, [2 * R, R * R, S // 4 + 1 if S // 4 + 1 != R else R + 1, F(R, 2)]), ans=0, ee='\\(4\\pi R^2=%d\\pi\\Rightarrow R^2=%d\\Rightarrow R=%d\\) cm.' % (S, R * R, R), ev='\\(4\\pi R^2=%d\\pi\\Rightarrow R^2=%d\\Rightarrow R=%d\\) cm.' % (S, R * R, R))


def b32_d2_hemi(r, lv):
    R = r.randint(2, 10)
    return dict(en='A solid hemisphere of radius %d cm (curved surface and flat base). Find its total surface area.' % R, vi='Một khối nửa hình cầu bán kính %d cm (gồm mặt cong và mặt đáy phẳng). Tính diện tích toàn phần.' % R,
                opts=piopts(r, 3 * R * R, [2 * R * R, 4 * R * R, R * R]), ans=0, ee='Curved part \\(2\\pi R^2\\), base \\(\\pi R^2\\): total \\(3\\pi R^2=%s\\).' % pi(3 * R * R, 'cm', 2), ev='Mặt cong \\(2\\pi R^2\\), mặt đáy \\(\\pi R^2\\): tổng \\(3\\pi R^2=%s\\).' % pi(3 * R * R, 'cm', 2))


def b32_d3_box(r, lv):
    R = r.randint(2, 9)
    return dict(en='A ball of radius %d cm fits exactly in a cylindrical box (it touches the two bases and the side). What fraction of the box does the ball fill?' % R,
                vi='Một quả bóng bán kính %d cm đặt vừa khít trong một hộp hình trụ (tiếp xúc với hai đáy và mặt xung quanh). Quả bóng chiếm bao nhiêu phần thể tích hộp?' % R,
                opts=['\\dfrac23', '\\dfrac12', '\\dfrac34', '\\dfrac13'], ans=0,
                ee='Box: \\(\\pi R^2\\cdot2R=2\\pi R^3\\); ball: \\(\\dfrac43\\pi R^3\\); ratio \\(\\dfrac23\\).', ev='Hộp: \\(\\pi R^2\\cdot2R=2\\pi R^3\\); bóng: \\(\\dfrac43\\pi R^3\\); tỉ số \\(\\dfrac23\\).')


def b32_d3_tank(r, lv):
    R = 3 * r.randint(1, 3); H = r.randint(4, 12)
    g = R * R * H + F(4 * R ** 3, 3)
    return dict(en='A gas tank is a cylinder (radius %d dm, length %d dm) with a hemisphere of the same radius at each end. Find its volume.' % (R, H),
                vi='Một bồn chứa gồm một hình trụ (bán kính %d dm, dài %d dm) và hai nửa hình cầu cùng bán kính ở hai đầu. Tính thể tích bồn.' % (R, H),
                opts=piopts(r, g, [R * R * H + F(2 * R ** 3, 3), R * R * H, R * R * H + 4 * R * R], unit='dm', p=3), ans=0,
                ee='Cylinder \\(\\pi\\cdot%d^2\\cdot%d=%d\\pi\\); two hemispheres = one ball \\(\\dfrac43\\pi\\cdot%d^3=%s\\pi\\); total \\(%s\\).' % (R, H, R * R * H, R, pe(F(4 * R ** 3, 3)), pi(g, 'dm', 3)),
                ev='Hình trụ \\(\\pi\\cdot%d^2\\cdot%d=%d\\pi\\); hai nửa hình cầu = một hình cầu \\(\\dfrac43\\pi\\cdot%d^3=%s\\pi\\); tổng \\(%s\\).' % (R, H, R * R * H, R, pe(F(4 * R ** 3, 3)), pi(g, 'dm', 3)))


def b32_d3_great(r, lv):
    R = r.randint(2, 15); S = 4 * R * R
    return dict(en='A sphere has surface area \\(%s\\). Find the length of a great circle.' % pi(S, 'cm', 2), vi='Mặt cầu có diện tích \\(%s\\). Tính độ dài một đường tròn lớn.' % pi(S, 'cm', 2),
                opts=piopts(r, 2 * R, [R, 4 * R, R * R], p=1), ans=0, ee='\\(R=%d\\); great circle \\(2\\pi R=%s\\).' % (R, pi(2 * R)), ev='\\(R=%d\\); đường tròn lớn \\(2\\pi R=%s\\).' % (R, pi(2 * R)))


def b32_d4_tube(r, lv):
    R = r.randint(2, 5); n = 3
    cyl = R * R * (2 * R * n); balls = n * F(4 * R ** 3, 3); g = cyl - balls
    return dict(en='Three tennis balls of radius %d cm fit exactly in a cylindrical tube (they touch the side, each other and the two ends). Find the empty volume in the tube.' % R,
                vi='Ba quả bóng tennis bán kính %d cm đặt vừa khít trong một hộp hình trụ (tiếp xúc mặt xung quanh, tiếp xúc nhau và tiếp xúc hai đáy). Tính thể tích phần không gian trống trong hộp.' % R,
                opts=piopts(r, g, [cyl, balls, cyl - F(4 * R ** 3, 3)], p=3), ans=0,
                ee='Tube: \\(\\pi\\cdot%d^2\\cdot%d=%d\\pi\\); balls: \\(3\\cdot\\dfrac43\\pi\\cdot%d^3=%d\\pi\\); empty \\(%s\\).' % (R, 6 * R, cyl, R, balls, pi(g, 'cm', 3)),
                ev='Hộp: \\(\\pi\\cdot%d^2\\cdot%d=%d\\pi\\); ba quả bóng: \\(3\\cdot\\dfrac43\\pi\\cdot%d^3=%d\\pi\\); phần trống \\(%s\\).' % (R, 6 * R, cyl, R, balls, pi(g, 'cm', 3)))


def b32_d4_recast(r, lv):
    R, s = r.choice([(6, 2), (6, 3), (4, 2), (9, 3), (10, 5), (8, 2), (12, 4)]); n = (R // s) ** 3
    return dict(en='A metal ball of radius %d cm is melted and recast into small balls of radius %d cm. How many small balls are made?' % (R, s), vi='Nấu chảy một quả cầu kim loại bán kính %d cm để đúc thành các viên bi bán kính %d cm. Đúc được bao nhiêu viên bi?' % (R, s),
                opts=iopts(r, n, [R // s, (R // s) ** 2, 2 * n]), ans=0, ee='\\(\\dfrac{\\frac43\\pi\\cdot%d^3}{\\frac43\\pi\\cdot%d^3}=\\left(\\dfrac{%d}{%d}\\right)^3=%d\\).' % (R, s, R, s, n),
                ev='\\(\\dfrac{\\frac43\\pi\\cdot%d^3}{\\frac43\\pi\\cdot%d^3}=\\left(\\dfrac{%d}{%d}\\right)^3=%d\\).' % (R, s, R, s, n))


def b32_d4_dome(r, lv):
    d, cost = r.choice([(10, 100), (6, 150), (8, 50), (20, 20), (4, 250)]); R = F(d, 2)
    S = 2 * R * R * F(314, 100); money = S * cost
    if money.denominator != 1: raise AssertionError
    return dict(en='The roof of a planetarium is a hemisphere with diameter %d m. Painting costs %d thousand VND per m². How much does it cost to paint the outside of the roof? (\\(\\pi\\approx3.14\\))' % (d, cost),
                vi='Mái vòm của một nhà chiếu hình vũ trụ có dạng nửa mặt cầu đường kính %d m. Sơn mỗi mét vuông tốn %d nghìn đồng. Chi phí sơn mặt ngoài mái vòm là bao nhiêu? (\\(\\pi\\approx3{,}14\\))' % (d, cost),
                opts=pick_opts(r, tx('%s thousand VND' % pe(money), '%s nghìn đồng' % pv(money)), [tx('%s thousand VND' % pe(x), '%s nghìn đồng' % pv(x)) for x in (2 * money, money / 2, money * 3 / 2)]), ans=0,
                ee='\\(S=2\\pi R^2\\approx2\\cdot3.14\\cdot%s^2=%s\\) m²; cost \\(%s\\) thousand VND.' % (pe(R), pe(S), pe(money)), ev='\\(S=2\\pi R^2\\approx2\\cdot3{,}14\\cdot%s^2=%s\\) m²; chi phí \\(%s\\) nghìn đồng.' % (dm(pe(R)), dm(pe(S)), dm(pe(money))))


L32_GROUPS = [[('mcq', b32_area), ('mcq', b32_vol), ('mcq', b32_section)], [('tf', b32_tf_area), ('tf', b32_tf_half)], [('short', b32_short_s), ('short', b32_short_v)],
              [('mcq', b32_d1_terms), ('mcq', b32_d1_formula), ('mcq', b32_d1_dia)], [('mcq', b32_d2_scale), ('mcq', b32_d2_fromS), ('mcq', b32_d2_hemi)],
              [('mcq', b32_d3_box), ('mcq', b32_d3_tank), ('mcq', b32_d3_great)], [('mcq', b32_d4_tube), ('mcq', b32_d4_recast), ('mcq', b32_d4_dome)]]
