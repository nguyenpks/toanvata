# -*- coding: utf-8 -*-
"""Hiệu chỉnh lớp 12 – đợt 3 (13/11/2026): phần D (8 dạng mới, khác A–C) cho Bài 13 (ứng dụng hình học của tích phân),
Bài 14 (phương trình mặt phẳng), Bài 15 (phương trình đường thẳng), Bài 16 (công thức tính góc). Câu cũ vẫn giữ trong thư viện câu hỏi.
Mỗi hàm (r, lv) → dict(en, vi, opts (opts[0] đúng), ee, ev[, fig]). Kiểm tra độc lập: scripts/audit13.py."""
import math, random
from fractions import Fraction as F
from functools import reduce
from sp_g11r import tx, ne, nv, nopt, nopts, Q3D
from sp_g11r2 import frt, fo, V
from sp_g12r import V3, sq, ksq, dot, sub, add, mul, n2, isq, nz, boxcfg, poly_tex
import fig2d as G

def pv(s, k): return '%d\\pi' % k if False else s
def pifrac(x):
    """x·π (x Fraction) → TeX."""
    x = F(x)
    if x == 0: return '0'
    if x.denominator == 1: return ('%d\\pi' % x.numerator) if abs(x.numerator) != 1 else ('\\pi' if x > 0 else '-\\pi')
    return ('-' if x < 0 else '') + '\\dfrac{%s\\pi}{%d}' % ('' if abs(x.numerator) == 1 else abs(x.numerator), x.denominator)
def cross(u, w): return (u[1] * w[2] - u[2] * w[1], u[2] * w[0] - u[0] * w[2], u[0] * w[1] - u[1] * w[0])
def red(v):
    g = reduce(math.gcd, [abs(int(x)) for x in v if x]) or 1
    v = tuple(int(x) // g for x in v)
    for x in v:
        if x: return v if x > 0 else tuple(-y for y in v)
    return v
def lin3(c, names=('x', 'y', 'z'), const=0):
    out = ''
    for k, nm in zip(c, names):
        if k == 0: continue
        t = nm if abs(k) == 1 else '%d%s' % (abs(k), nm)
        out += ('-' if k < 0 else ('+' if out else '')) + t
    if const: out += ('+%d' % const) if const > 0 else str(const)
    return out or '0'
def plane(n, d): return lin3(n, const=d) + '=0'
def surd(num, N):
    """num/√N (num, N nguyên dương) → TeX rút gọn, khử căn ở mẫu."""
    a, b = 1, N; k = 2
    while k * k <= b:
        while b % (k * k) == 0: b //= k * k; a *= k
        k += 1
    # num/(a√b) = num√b/(a b)
    if b == 1: return frt(F(num, a))
    fr = F(num, a * b)
    if fr.numerator == 1: top = '\\sqrt{%d}' % b
    else: top = '%d\\sqrt{%d}' % (fr.numerator, b)
    return top if fr.denominator == 1 else '\\dfrac{%s}{%d}' % (top, fr.denominator)
def par(P, u, t='t'):
    rows = []
    for p, k, nm in zip(P, u, 'xyz'):
        s = str(p) if p or not k else ''
        if k: s += (('+' if s else '') if k > 0 else '-') + ('' if abs(k) == 1 else str(abs(k))) + t
        rows.append('%s=%s' % (nm, s or '0'))
    return '\\begin{cases}%s\\end{cases}' % '\\\\'.join(rows)
def can(P, u):
    parts = []
    for p, k, nm in zip(P, u, 'xyz'):
        num = nm if p == 0 else '%s%s%d' % (nm, '-' if p > 0 else '+', abs(p))
        parts.append('\\dfrac{%s}{%d}' % (num, k))
    return '='.join(parts)

# =============================================================== Bài 13 – Ứng dụng hình học của tích phân
def a13_two(r, lv):
    for _ in range(300):
        x1 = r.randint(-2, 1); x2 = x1 + r.choice([2, 3]); a = r.choice([1, -1]); m = r.randint(-2, 2); n = r.randint(-1, 3)
        L = lambda x: m * x + n; P = lambda x: L(x) + a * (x - x1) * (x - x2)
        ys = [P(F(i, 10) + x1 - 1) for i in range(0, (x2 - x1 + 2) * 10 + 1)] + [L(x1 - 1), L(x2 + 1)]
        if max(ys) - min(ys) <= 10: break
    else: raise AssertionError
    A = F(abs(a) * (x2 - x1) ** 3, 6)
    pt = poly_tex(a, a * (-(x1 + x2)) + m, a * x1 * x2 + n); lt = poly_tex(0, m, n)
    top, bot = (L, P) if a > 0 else (P, L)
    lo, hi = float(min(ys)) - .5, float(max(ys)) + .5
    img = G.graph_svg([(lambda x: float(P(F(x).limit_denominator(1000))), G.GREEN), (lambda x: float(L(F(x).limit_denominator(1000))), G.ORANGE)], (min(x1 - 1.2, -.8), max(x2 + 1.2, .8)), (min(lo, -.6), max(hi, .6)),
                      [(x1, str(x1)), (x2, str(x2))] if 0 not in (x1, x2) else [(v, str(v)) for v in (x1, x2) if v], [], dots=[(x1, L(x1), False), (x2, L(x2), False)],
                      fills=[(lambda x: float(top(F(x).limit_denominator(1000))), lambda x: float(bot(F(x).limit_denominator(1000))), x1, x2)], W=5.6, H=4.2)
    return dict(en='The shaded region is bounded by the parabola \\(y=%s\\) and the line \\(y=%s\\) (see the figure). Its area is…' % (pt, lt),
                vi='Miền tô đậm giới hạn bởi parabol \\(y=%s\\) và đường thẳng \\(y=%s\\) (xem hình). Diện tích miền đó là' % (pt, lt),
                opts=nopts(r, A, [2 * A, A / 2 if A / 2 != A else A + 1, F((x2 - x1) ** 2, 2), A + 1]), fig=G.FIG(img, 'Region between a parabola and a line', 'Miền giữa parabol và đường thẳng', 300),
                ee='The curves meet at \\(x=%d\\), \\(x=%d\\): \\(S=\\displaystyle\\int_{%d}^{%d}\\left|(%s)-(%s)\\right|dx=%s\\).' % (x1, x2, x1, x2, pt, lt, ne(A)),
                ev='Hai đường cắt nhau tại \\(x=%d\\), \\(x=%d\\): \\(S=\\displaystyle\\int_{%d}^{%d}\\left|(%s)-(%s)\\right|dx=%s\\).' % (x1, x2, x1, x2, pt, lt, nv(A)))

def a13_abs(r, lv):
    c = r.choice([1, 2]); k = c + r.choice([1, 2]) if c == 1 else c + 1
    f = lambda x: x * x - c * c
    A = F(2 * c ** 3, 3) + F(k ** 3 - c ** 3, 3) - c * c * (k - c); signed = F(k ** 3, 3) - c * c * k
    img = G.graph_svg([(lambda x: x * x - c * c, G.GREEN)], (-1, k + .8), (-c * c - .8, k * k - c * c + .8), [(c, str(c)), (k, str(k))], [(-c * c, str(-c * c))],
                      fills=[(lambda x: 0.0, lambda x: x * x - c * c, 0, c), (lambda x: x * x - c * c, lambda x: 0.0, c, k)], vlines=[(k, None)], W=4.8, H=4.4)
    return dict(en='The shaded region is bounded by \\(y=x^2-%d\\), the axis \\(Ox\\) and the lines \\(x=0\\), \\(x=%d\\) (see the figure). Its area is…' % (c * c, k),
                vi='Miền tô đậm giới hạn bởi \\(y=x^2-%d\\), trục \\(Ox\\) và các đường thẳng \\(x=0\\), \\(x=%d\\) (xem hình). Diện tích miền đó là' % (c * c, k),
                opts=nopts(r, A, [abs(signed), signed if signed != abs(signed) else signed + 2, F(2 * c ** 3, 3), A + 1]), fig=G.FIG(img, 'Region crossing the axis', 'Miền cắt trục hoành', 260),
                ee='The graph crosses \\(Ox\\) at \\(x=%d\\), so split: \\(S=\\displaystyle\\int_0^{%d}(%d-x^2)dx+\\int_{%d}^{%d}(x^2-%d)dx=%s\\) (not \\(\\left|\\int_0^{%d}\\right|\\)).' % (c, c, c * c, c, k, c * c, ne(A), k),
                ev='Đồ thị cắt \\(Ox\\) tại \\(x=%d\\) nên tách: \\(S=\\displaystyle\\int_0^{%d}(%d-x^2)dx+\\int_{%d}^{%d}(x^2-%d)dx=%s\\) (không phải \\(\\left|\\int_0^{%d}\\right|\\)).' % (c, c, c * c, c, k, c * c, nv(A), k))

VOL = [('y=\\dfrac1x', '[1;\\,2]', '\\dfrac{\\pi}{2}', ['\\pi\\ln2', '\\dfrac12', '2\\pi']), ('y=\\dfrac1x', '[1;\\,3]', '\\dfrac{2\\pi}{3}', ['\\pi\\ln3', '\\dfrac23', '\\dfrac{\\pi}{3}']),
       ('y=\\sin x', '[0;\\,\\pi]', '\\dfrac{\\pi^2}{2}', ['2\\pi', '\\pi^2', '\\dfrac{\\pi}{2}']), ('y=e^x', '[0;\\,1]', '\\dfrac{\\pi(e^2-1)}{2}', ['\\pi(e-1)', '\\dfrac{e^2-1}{2}', '\\pi(e^2-1)']),
       ('y=x^2', '[0;\\,1]', '\\dfrac{\\pi}{5}', ['\\dfrac{\\pi}{3}', '\\dfrac15', '\\dfrac{\\pi}{2}']), ('y=x^2', '[0;\\,2]', '\\dfrac{32\\pi}{5}', ['\\dfrac{8\\pi}{3}', '\\dfrac{32}{5}', '\\dfrac{16\\pi}{5}']),
       ('y=\\sqrt{4-x^2}', '[-2;\\,2]', '\\dfrac{32\\pi}{3}', ['2\\pi', '\\dfrac{16\\pi}{3}', '8\\pi']), ('y=\\cos x', '\\left[0;\\,\\dfrac{\\pi}{2}\\right]', '\\dfrac{\\pi^2}{4}', ['\\pi', '\\dfrac{\\pi}{2}', '\\dfrac{\\pi^2}{2}'])]
def a13_vol(r, lv):
    fx, I, g, b = r.choice(VOL)
    return dict(en='The region under \\(%s\\) over \\(%s\\) (and above \\(Ox\\)) is rotated about \\(Ox\\). The volume of the solid is…' % (fx, I),
                vi='Miền nằm dưới đồ thị \\(%s\\) trên đoạn \\(%s\\) (và phía trên \\(Ox\\)) quay quanh trục \\(Ox\\). Thể tích khối tròn xoay là' % (fx, I),
                opts=[g] + b, ee='\\(V=\\pi\\displaystyle\\int_a^b f^2(x)\\,dx=%s\\) (do not forget \\(\\pi\\) and the square).' % g, ev='\\(V=\\pi\\displaystyle\\int_a^b f^2(x)\\,dx=%s\\) (đừng quên \\(\\pi\\) và bình phương).' % g)

WASH = [('y=x', 'y=x^2', 0, 1, F(2, 15), [F(1, 6), F(1, 30), F(1, 3)]), ('y=2x', 'y=x^2', 0, 2, F(64, 15), [F(4, 3), F(16, 15), F(8, 3)]), ('y=x', 'y=x^3', 0, 1, F(4, 21), [F(1, 4), F(1, 12), F(2, 7)]),
        ('y=\\sqrt x', 'y=x', 0, 1, F(1, 6), [F(1, 30), F(1, 2), F(1, 3)]), ('y=4', 'y=x^2', 0, 2, F(128, 5), [F(16, 3), F(32, 5), F(64, 5)])]
def a13_washer(r, lv):
    f, g, a, b, Vv, bad = r.choice(WASH)
    return dict(en='The region between \\(%s\\) and \\(%s\\) for \\(%d\\le x\\le%d\\) is rotated about \\(Ox\\). The volume of the solid is…' % (f, g, a, b),
                vi='Miền giữa hai đồ thị \\(%s\\) và \\(%s\\) với \\(%d\\le x\\le%d\\) quay quanh trục \\(Ox\\). Thể tích khối tròn xoay là' % (f, g, a, b),
                opts=[pifrac(Vv)] + [pifrac(x) for x in bad],
                ee='Washer: \\(V=\\pi\\displaystyle\\int_{%d}^{%d}\\left(f^2-g^2\\right)dx\\) with the upper curve \\(f\\); this is not \\(\\pi\\displaystyle\\int(f-g)^2dx\\). Answer: \\(%s\\).' % (a, b, pifrac(Vv)),
                ev='Khối có lỗ: \\(V=\\pi\\displaystyle\\int_{%d}^{%d}\\left(f^2-g^2\\right)dx\\) với \\(f\\) là đường phía trên; không phải \\(\\pi\\displaystyle\\int(f-g)^2dx\\). Đáp số: \\(%s\\).' % (a, b, pifrac(Vv)))

def a13_bowl(r, lv):
    R = r.choice([3, 6, 9, 10, 12]); h = r.choice([x for x in (1, 2, 3, 4, 5, 6) if x < R])
    Vv = F(h * h * (3 * R - h), 3)
    return dict(en='A hemispherical bowl has radius \\(%d\\) cm. Water in it is \\(%d\\) cm deep. Using \\(V=\\pi\\displaystyle\\int_{%d}^{%d}\\left(%d-x^2\\right)dx\\) (rotating a circle about \\(Ox\\)), the volume of water (cm³) is…' % (R, h, R - h, R, R * R),
                vi='Một cái bát hình bán cầu bán kính \\(%d\\) cm chứa nước sâu \\(%d\\) cm. Dùng \\(V=\\pi\\displaystyle\\int_{%d}^{%d}\\left(%d-x^2\\right)dx\\) (quay đường tròn quanh \\(Ox\\)), thể tích nước (cm³) là' % (R, h, R - h, R, R * R),
                opts=[pifrac(Vv), pifrac(F(h * h * R)), pifrac(F(2 * R ** 3, 3) - Vv) if F(2 * R ** 3, 3) - Vv != Vv else pifrac(Vv * 2), pifrac(F(h * h * (3 * R - h), 6))],
                ee='\\(V=\\pi\\left[%dx-\\dfrac{x^3}{3}\\right]_{%d}^{%d}=\\pi h^2\\left(R-\\dfrac h3\\right)=%s\\).' % (R * R, R - h, R, pifrac(Vv)),
                ev='\\(V=\\pi\\left[%dx-\\dfrac{x^3}{3}\\right]_{%d}^{%d}=\\pi h^2\\left(R-\\dfrac h3\\right)=%s\\).' % (R * R, R - h, R, pifrac(Vv)))

def a13_param(r, lv):
    m = r.choice([1, 4, 9, 16]); A = F(4, 3) * math.isqrt(m) ** 3
    return dict(en='The region between \\(y=x^2\\) and the line \\(y=m\\) (\\(m\\gt0\\)) has area \\(%s\\). Then \\(m=\\)…' % frt(A), vi='Miền giới hạn bởi \\(y=x^2\\) và đường thẳng \\(y=m\\) (\\(m\\gt0\\)) có diện tích \\(%s\\). Khi đó \\(m=\\)' % frt(A),
                opts=nopts(r, m, [math.isqrt(m), m * m if m * m != m else 2, m + 1, 2 * m if 2 * m != m else 3]),
                ee='The curves meet at \\(x=\\pm\\sqrt m\\): \\(S=\\displaystyle\\int_{-\\sqrt m}^{\\sqrt m}(m-x^2)dx=\\dfrac43m\\sqrt m=%s\\Rightarrow m=%d\\).' % (frt(A), m),
                ev='Hai đường cắt nhau tại \\(x=\\pm\\sqrt m\\): \\(S=\\displaystyle\\int_{-\\sqrt m}^{\\sqrt m}(m-x^2)dx=\\dfrac43m\\sqrt m=%s\\Rightarrow m=%d\\).' % (frt(A), m))

def a13_cross(r, lv):
    b = r.choice([2, 3, 4, 6]); kind = r.choice(['tri', 'semi'])
    if kind == 'tri':
        Vv = F(b ** 3, 12); g = ksq(Vv, 3); bad = [frt(Vv * 4), ksq(Vv * 2, 3), ksq(Vv * 4, 3)]
        de, dv = 'an equilateral triangle with side \\(x\\)', 'một tam giác đều cạnh \\(x\\)'; Se = '\\dfrac{\\sqrt3}{4}x^2'
    else:
        Vv = F(b ** 3, 24); g = pifrac(Vv); bad = [pifrac(Vv * 4), pifrac(Vv * 2), pifrac(Vv * 8)]
        de, dv = 'a semicircle with diameter \\(x\\)', 'một nửa hình tròn đường kính \\(x\\)'; Se = '\\dfrac{\\pi}{8}x^2'
    return dict(en='A solid lies between the planes \\(x=0\\) and \\(x=%d\\). Its cross-section perpendicular to \\(Ox\\) at \\(x\\) is %s. Its volume is…' % (b, de),
                vi='Một vật thể nằm giữa hai mặt phẳng \\(x=0\\) và \\(x=%d\\). Thiết diện vuông góc với \\(Ox\\) tại \\(x\\) là %s. Thể tích vật thể là' % (b, dv),
                opts=[g] + bad, ee='\\(S(x)=%s\\), \\(V=\\displaystyle\\int_0^{%d}S(x)\\,dx=%s\\).' % (Se, b, g), ev='\\(S(x)=%s\\), \\(V=\\displaystyle\\int_0^{%d}S(x)\\,dx=%s\\).' % (Se, b, g))

WI = [('x', 'x^2', lambda x: x, lambda x: x * x, 0, 1, 2), ('2x', 'x^2', lambda x: 2 * x, lambda x: x * x, 0, 2, 3), ('1', 'x^2', lambda x: 1.0, lambda x: x * x, 0, 1, 2), ('4', 'x^2', lambda x: 4.0, lambda x: x * x, 0, 2, 3)]
def a13_which(r, lv):
    ft, gt, f, g, a, c, b = r.choice(WI)
    img = G.graph_svg([(f, G.ORANGE), (g, G.GREEN)], (-.6, b + .6), (-.6, max(g(b), f(b)) + .6), [(c, str(c)), (b, str(b))], [],
                      fills=[(f, g, a, c), (g, f, c, b)], vlines=[(b, None)], W=4.6, H=4.4)
    I = lambda p, q, u, v: '\\displaystyle\\int_{%d}^{%d}\\left(%s-%s\\right)dx' % (u, v, p, q)
    good = I(ft, gt, a, c) + '+' + I(gt, ft, c, b)
    bads = [I(ft, gt, a, b), I(gt, ft, a, b), I(ft, gt, a, c) + '+' + I(ft, gt, c, b)]
    q = V(lv, [('Which integral gives the area of the shaded region bounded by \\(y=%s\\), \\(y=%s\\) and \\(x=%d\\)?', 'Diện tích miền tô đậm giới hạn bởi \\(y=%s\\), \\(y=%s\\) và \\(x=%d\\) được tính bởi công thức nào?'),
                   ('The shaded region lies between \\(y=%s\\) and \\(y=%s\\), from the origin to \\(x=%d\\). Its area equals…', 'Miền tô đậm nằm giữa \\(y=%s\\) và \\(y=%s\\), từ gốc tọa độ đến \\(x=%d\\). Diện tích miền đó bằng'),
                   ('Choose the correct formula for the area of the shaded region (curves \\(y=%s\\), \\(y=%s\\), line \\(x=%d\\)).', 'Chọn công thức đúng tính diện tích miền tô đậm (các đường \\(y=%s\\), \\(y=%s\\), \\(x=%d\\)).')])
    return dict(en=q[0] % (ft, gt, b), vi=q[1] % (ft, gt, b), opts=[good] + bads, fig=G.FIG(img, 'Shaded region', 'Miền tô đậm', 260),
                ee='The curves cross at \\(x=%d\\); on each piece subtract the lower curve from the upper one.' % c, ev='Hai đường cắt nhau tại \\(x=%d\\); trên mỗi đoạn lấy đường trên trừ đường dưới.' % c)

D13 = [a13_two, a13_abs, a13_vol, a13_washer, a13_bowl, a13_param, a13_cross, a13_which]

# =============================================================== Bài 14 – Phương trình mặt phẳng
def rpt(r, lo=-4, hi=4): return tuple(r.randint(lo, hi) for _ in range(3))
def p14_three(r, lv):
    for _ in range(300):
        A, B, C = rpt(r), rpt(r), rpt(r); n = cross(sub(B, A), sub(C, A))
        if n2(n) and all(abs(x) <= 12 for x in n): break
    n = red(n); d = -dot(n, A)
    assert dot(n, B) + d == 0 and dot(n, C) + d == 0
    bads = [plane((n[0], -n[1], n[2]), d), plane(n, -d) if d else plane(n, 1), plane(red(sub(B, A)), -dot(red(sub(B, A)), A))]
    return dict(en='The plane through \\(A%s\\), \\(B%s\\), \\(C%s\\) is…' % (V3(A), V3(B), V3(C)), vi='Mặt phẳng đi qua ba điểm \\(A%s\\), \\(B%s\\), \\(C%s\\) là' % (V3(A), V3(B), V3(C)),
                opts=fo(plane(n, d), bads),
                ee='\\(\\vec n=[\\overrightarrow{AB},\\overrightarrow{AC}]\\parallel%s\\); through \\(A\\): \\(%s\\).' % (V3(n), plane(n, d)), ev='\\(\\vec n=[\\overrightarrow{AB},\\overrightarrow{AC}]\\parallel%s\\); qua \\(A\\): \\(%s\\).' % (V3(n), plane(n, d)))

def p14_parallel(r, lv):
    n = red(tuple(nz(r, -3, 3) if i == 0 else r.randint(-3, 3) for i in range(3))); M = rpt(r); dq = nz(r, -6, 6)
    d = -dot(n, M)
    if d == dq: raise AssertionError
    return dict(en='The plane through \\(M%s\\) parallel to \\((Q): %s\\) is…' % (V3(M), plane(n, dq)), vi='Mặt phẳng đi qua \\(M%s\\) và song song với \\((Q): %s\\) là' % (V3(M), plane(n, dq)),
                opts=fo(plane(n, d), [plane(n, -d) if d else plane(n, 3), plane(n, dq + d) if dq + d not in (d, -d) else plane(n, d + 1), plane(tuple(-x if i == 2 else x for i, x in enumerate(n)), d) if n[2] else plane(n, d - 2)]),
                ee='Same normal \\(%s\\): \\(%s+D=0\\) through \\(M\\) gives \\(D=%d\\).' % (V3(n), lin3(n), d), ev='Cùng vectơ pháp tuyến \\(%s\\): \\(%s+D=0\\) đi qua \\(M\\) nên \\(D=%d\\).' % (V3(n), lin3(n), d))

def p14_bisector(r, lv):
    for _ in range(300):
        A, B = rpt(r), rpt(r)
        if A != B and all((a + b) % 2 == 0 for a, b in zip(A, B)): break
    n0 = sub(B, A); I = tuple((a + b) // 2 for a, b in zip(A, B)); g = reduce(math.gcd, [abs(x) for x in n0]); n = tuple(x // g for x in n0); d = -dot(n, I)
    return dict(en='The perpendicular bisector plane of the segment \\(AB\\) with \\(A%s\\), \\(B%s\\) is…' % (V3(A), V3(B)), vi='Mặt phẳng trung trực của đoạn \\(AB\\) với \\(A%s\\), \\(B%s\\) là' % (V3(A), V3(B)),
                opts=fo(plane(n, d), [plane(n, -dot(n, A)), plane(n, -dot(n, B)), plane(n, -d) if d else plane(n, 2)]),
                ee='It passes through the midpoint \\(I%s\\) with normal \\(\\overrightarrow{AB}\\parallel%s\\): \\(%s\\).' % (V3(I), V3(n), plane(n, d)), ev='Mặt phẳng đi qua trung điểm \\(I%s\\), nhận \\(\\overrightarrow{AB}\\parallel%s\\) làm pháp tuyến: \\(%s\\).' % (V3(I), V3(n), plane(n, d)))

def p14_box(r, lv):
    a, b, c = r.sample([2, 3, 4, 6], 3); kind = r.choice(['ACO', 'OAB'])
    if kind == 'ACO': pts = ['A', 'C', 'O′']; n = red((b * c, a * c, a * b)); P = (a, 0, 0)
    else: pts = ['O′', 'A', 'B']; n = red((c, 0, a)); P = (a, 0, 0)
    d = -dot(n, P); cfg = boxcfg(a, b, c)
    cfg['polygons'] = [{'points': pts, 'fill': '#86e0bd', 'opacity': .45, 'outline': True}]
    bads = [plane(red((a, b, c)) if kind == 'ACO' else red((a, 0, c)), -dot(red((a, b, c)) if kind == 'ACO' else red((a, 0, c)), P)), plane(n, -d), plane(red((n[0], n[1] if n[1] == 0 else -n[1], n[2])) if kind == 'ACO' else (n[0], 1, n[2]), d)]
    names = '(%s)' % ''.join(pts)
    return dict(en='The rectangular box \\(OABC.O′A′B′C′\\) has \\(O\\) at the origin and \\(B′%s\\) (see the figure). The equation of the plane \\(%s\\) is…' % (V3((a, b, c)), names),
                vi='Hình hộp chữ nhật \\(OABC.O′A′B′C′\\) có \\(O\\) là gốc tọa độ và \\(B′%s\\) (xem hình). Phương trình mặt phẳng \\(%s\\) là' % (V3((a, b, c)), names),
                opts=fo(plane(n, d), bads), fig=Q3D(cfg, 'Box'),
                ee='Read the coordinates of the three vertices from the box, then \\(\\vec n\\parallel%s\\): \\(%s\\).' % (V3(n), plane(n, d)), ev='Đọc tọa độ ba đỉnh từ hình hộp, rồi \\(\\vec n\\parallel%s\\): \\(%s\\).' % (V3(n), plane(n, d)))

QD = [(1, 2, 2), (2, 1, 2), (2, 2, 1), (1, -2, 2), (2, -1, -2), (2, 3, 6), (3, 6, 2), (6, 2, 3), (1, 4, 8), (4, 4, 7)]
def p14_foot(r, lv):
    n = tuple(x * r.choice([1, -1]) for x in r.choice(QD)); H = rpt(r, -3, 3); t = nz(r, -2, 2); M = add(H, mul(t, n)); d = -dot(n, H)
    M = tuple(int(x) for x in M)
    return dict(en='The orthogonal projection of \\(M%s\\) onto \\((P): %s\\) is…' % (V3(M), plane(n, d)), vi='Hình chiếu vuông góc của \\(M%s\\) lên mặt phẳng \\((P): %s\\) là' % (V3(M), plane(n, d)),
                opts=fo(V3(H), [V3(tuple(int(x) for x in add(M, mul(t, n)))), V3(tuple(int(x) for x in sub(H, mul(t, n)))), V3(tuple(int(x) for x in add(H, n))) if t != 1 else V3(tuple(int(x) for x in add(H, mul(2, n))))]),
                ee='\\(H=M+s\\vec n\\) with \\(H\\in(P)\\): \\(s=%d\\), \\(H%s\\).' % (-t, V3(H)), ev='\\(H=M+s\\vec n\\) với \\(H\\in(P)\\): \\(s=%d\\), \\(H%s\\).' % (-t, V3(H)))

def p14_sym(r, lv):
    n = tuple(x * r.choice([1, -1]) for x in r.choice(QD[:5])); H = rpt(r, -3, 3); t = nz(r, -1, 1); M = tuple(int(x) for x in add(H, mul(t, n))); d = -dot(n, H)
    Ms = tuple(int(x) for x in sub(H, mul(t, n)))
    return dict(en='The point symmetric to \\(M%s\\) with respect to \\((P): %s\\) is…' % (V3(M), plane(n, d)), vi='Điểm đối xứng với \\(M%s\\) qua mặt phẳng \\((P): %s\\) là' % (V3(M), plane(n, d)),
                opts=fo(V3(Ms), [V3(H), V3(tuple(-x for x in M)), V3(tuple(int(x) for x in add(M, mul(2 * t, n))))]),
                ee='The foot is \\(H%s\\) (midpoint of \\(MM′\\)), so \\(M′=2H-M=%s\\).' % (V3(H), V3(Ms)), ev='Hình chiếu \\(H%s\\) là trung điểm của \\(MM′\\), nên \\(M′=2H-M=%s\\).' % (V3(H), V3(Ms)))

def p14_dist_m(r, lv):
    for _ in range(300):
        n = tuple(x * r.choice([1, -1]) for x in r.choice(QD)); L = math.isqrt(n2(n)); M = rpt(r, -3, 3); dd = r.randint(1, 3); s = dot(n, M)
        m1, m2 = dd * L - s, -dd * L - s
        if m1 > 0 > m2: break
    else: raise AssertionError
    return dict(en='\\((P): %s+m=0\\). Find \\(m\\gt0\\) such that the distance from \\(M%s\\) to \\((P)\\) equals \\(%d\\).' % (lin3(n), V3(M), dd), vi='Cho \\((P): %s+m=0\\). Tìm \\(m\\gt0\\) để khoảng cách từ \\(M%s\\) đến \\((P)\\) bằng \\(%d\\).' % (lin3(n), V3(M), dd),
                opts=nopts(r, m1, [m2, -m2, dd * L, abs(dd - s)]),
                ee='\\(\\dfrac{|%d+m|}{%d}=%d\\Leftrightarrow m=%d\\) or \\(m=%d\\); the positive one is \\(%d\\).' % (s, L, dd, m1, m2, m1), ev='\\(\\dfrac{|%d+m|}{%d}=%d\\Leftrightarrow m=%d\\) hoặc \\(m=%d\\); giá trị dương là \\(%d\\).' % (s, L, dd, m1, m2, m1))

def p14_tetra(r, lv):
    p, q, s = [x * r.choice([1, 1, -1]) for x in r.sample([1, 2, 3, 4, 6], 3)]
    L = abs(p * q * s) // math.gcd(math.gcd(abs(p * q), abs(q * s)), abs(p * s)); L = reduce(lambda u, w: u * w // math.gcd(u, w), [abs(p), abs(q), abs(s)])
    n = (L // p, L // q, L // s); Vv = F(abs(p * q * s), 6)
    return dict(en='The plane \\((P): %s\\) meets \\(Ox\\), \\(Oy\\), \\(Oz\\) at \\(A\\), \\(B\\), \\(C\\). The volume of the tetrahedron \\(OABC\\) is…' % plane(n, -L),
                vi='Mặt phẳng \\((P): %s\\) cắt \\(Ox\\), \\(Oy\\), \\(Oz\\) lần lượt tại \\(A\\), \\(B\\), \\(C\\). Thể tích tứ diện \\(OABC\\) là' % plane(n, -L),
                opts=nopts(r, Vv, [Vv * 3, Vv * 2, F(L, 6), Vv + 1]),
                ee='Intercepts \\(%d\\), \\(%d\\), \\(%d\\): \\(V=\\dfrac16|%d\\cdot%d\\cdot%d|=%s\\).' % (p, q, s, p, q, s, ne(Vv)), ev='Các giao điểm có hoành/tung/cao độ \\(%d\\), \\(%d\\), \\(%d\\): \\(V=\\dfrac16|%d\\cdot%d\\cdot%d|=%s\\).' % (p, q, s, p, q, s, nv(Vv)))

D14 = [p14_three, p14_parallel, p14_bisector, p14_box, p14_foot, p14_sym, p14_dist_m, p14_tetra]

# =============================================================== Bài 15 – Phương trình đường thẳng
def nzv(r, lo=-3, hi=3): return tuple(nz(r, lo, hi) for _ in range(3))
REL = [('parallel', 'song song'), ('intersecting', 'cắt nhau'), ('skew', 'chéo nhau'), ('coincident', 'trùng nhau')]
def l15_relpos(r, lv):
    kind = r.choice(['parallel', 'intersecting', 'skew'] if lv > 1 else ['parallel', 'intersecting', 'skew', 'coincident'])
    for _ in range(500):
        P1 = rpt(r, -3, 3); u1 = nzv(r)
        if kind in ('parallel', 'coincident'):
            k = r.choice([2, -1, -2]); u2 = mul(k, u1)
            P2 = add(P1, mul(r.choice([1, -1, 2]), u1)) if kind == 'coincident' else add(P1, rpt(r, -2, 2))
        elif kind == 'intersecting':
            Q = add(P1, mul(r.choice([1, -1]), u1)); u2 = nzv(r); P2 = add(Q, mul(r.choice([1, -1]), u2))
        else: u2 = nzv(r); P2 = add(P1, rpt(r, -3, 3))
        P2 = tuple(int(x) for x in P2); u2 = tuple(int(x) for x in u2)
        cr = cross(u1, u2); w = sub(P2, P1)
        if not any(cr): got = 'coincident' if not any(cross(w, u1)) else 'parallel'
        else: got = 'intersecting' if dot(w, cr) == 0 else 'skew'
        if got == kind: break
    else: raise AssertionError
    good = [x for x in REL if x[0] == kind][0]
    return dict(en='The relative position of \\(d_1: %s\\) and \\(d_2: %s\\) is…' % (par(P1, u1), par(P2, u2, 's')), vi='Vị trí tương đối của \\(d_1: %s\\) và \\(d_2: %s\\) là' % (par(P1, u1), par(P2, u2, 's')),
                opts=[tx(*good)] + [tx(*x) for x in REL if x != good],
                ee='\\([\\vec u_1,\\vec u_2]=%s\\)%s.' % (V3(cr), '' if not any(cr) else ', \\(\\overrightarrow{M_1M_2}\\cdot[\\vec u_1,\\vec u_2]=%d\\)' % dot(sub(P2, P1), cr)) + ' So the lines are %s.' % kind,
                ev='\\([\\vec u_1,\\vec u_2]=%s\\)%s.' % (V3(cr), '' if not any(cr) else ', \\(\\overrightarrow{M_1M_2}\\cdot[\\vec u_1,\\vec u_2]=%d\\)' % dot(sub(P2, P1), cr)) + ' Vậy hai đường thẳng %s.' % good[1])

def l15_par(r, lv):
    M = rpt(r, -4, 4); P = rpt(r, -4, 4); u = nzv(r)
    if M == P: raise AssertionError
    return dict(en='The line through \\(M%s\\) parallel to \\(d: %s\\) is…' % (V3(M), can(P, u)), vi='Đường thẳng đi qua \\(M%s\\) và song song với \\(d: %s\\) là' % (V3(M), can(P, u)),
                opts=fo(can(M, u), [can(P, u), can(M, tuple(-x if i == 0 else x for i, x in enumerate(u))), can(tuple(-x for x in M), u)]),
                ee='Same direction vector \\(%s\\), through \\(M\\): \\(%s\\).' % (V3(u), can(M, u)), ev='Cùng vectơ chỉ phương \\(%s\\), đi qua \\(M\\): \\(%s\\).' % (V3(u), can(M, u)))

def l15_perp2(r, lv):
    for _ in range(300):
        u1, u2 = nzv(r, -2, 2), nzv(r, -2, 2); w = cross(u1, u2)
        if all(w): w = red(w); break
    else: raise AssertionError
    M = rpt(r, -3, 3)
    bad = [red(add(u1, u2)) if all(add(u1, u2)) else (1, 1, 1), tuple(-x if i == 1 else x for i, x in enumerate(w)), red(cross(u1, (u2[0], u2[1], -u2[2]))) if all(cross(u1, (u2[0], u2[1], -u2[2]))) else (w[0], w[1], w[2] + 1)]
    return dict(en='The line through \\(M%s\\) perpendicular to both directions \\(\\vec u_1=%s\\) and \\(\\vec u_2=%s\\) is…' % (V3(M), V3(u1), V3(u2)),
                vi='Đường thẳng đi qua \\(M%s\\) và vuông góc với cả hai vectơ \\(\\vec u_1=%s\\), \\(\\vec u_2=%s\\) là' % (V3(M), V3(u1), V3(u2)),
                opts=fo(can(M, w), [can(M, b) for b in bad if all(b)] + [can(M, (w[0] + 1, w[1], w[2])) if w[0] + 1 else can(M, (2, w[1], w[2]))]),
                ee='Direction \\([\\vec u_1,\\vec u_2]\\parallel%s\\).' % V3(w), ev='Vectơ chỉ phương \\([\\vec u_1,\\vec u_2]\\parallel%s\\).' % V3(w))

def l15_foot(r, lv):
    for _ in range(500):
        P = rpt(r, -3, 3); u = nzv(r, -2, 2); t0 = r.randint(-2, 2); H = add(P, mul(t0, u)); w = rpt(r, -3, 3)
        if dot(w, u) == 0 and n2(w): break
    else: raise AssertionError
    M = tuple(int(x) for x in add(H, w)); H = tuple(int(x) for x in H)
    return dict(en='The foot of the perpendicular from \\(M%s\\) to the line \\(d: %s\\) is…' % (V3(M), par(P, u)), vi='Hình chiếu vuông góc của \\(M%s\\) lên đường thẳng \\(d: %s\\) là' % (V3(M), par(P, u)),
                opts=fo(V3(H), [V3(P) if P != H else V3(tuple(int(x) for x in add(H, u))), V3(tuple(int(x) for x in add(H, u))) if P != tuple(int(x) for x in add(H, u)) else V3(tuple(int(x) for x in sub(H, u))), V3(tuple(int(x) for x in sub(H, w)))]),
                ee='\\(H=(%s)+t%s\\); \\(\\overrightarrow{MH}\\cdot\\vec u=0\\) gives \\(t=%d\\), \\(H%s\\).' % (';'.join(map(str, P)), V3(u), t0, V3(H)),
                ev='\\(H=(%s)+t%s\\); \\(\\overrightarrow{MH}\\cdot\\vec u=0\\) cho \\(t=%d\\), \\(H%s\\).' % (';'.join(map(str, P)), V3(u), t0, V3(H)))

def l15_dist(r, lv):
    for _ in range(3000):
        P = rpt(r, -3, 3); u = nzv(r, -2, 2); t0 = r.randint(-2, 2); w = rpt(r, -4, 4)
        if dot(w, u) == 0 and n2(w) and isq(n2(w)): break
    else: raise AssertionError
    M = tuple(int(x) for x in add(add(P, mul(t0, u)), w)); dd = math.isqrt(n2(w))
    return dict(en='The distance from \\(M%s\\) to the line \\(d: %s\\) is…' % (V3(M), can(P, u)), vi='Khoảng cách từ \\(M%s\\) đến đường thẳng \\(d: %s\\) bằng' % (V3(M), can(P, u)),
                opts=fo(str(dd), [sq(n2(sub(M, P))), str(dd + 1), sq(dd * dd + n2(u)), str(dd * 2)]),
                ee='\\(d(M,d)=\\dfrac{\\left|[\\overrightarrow{PM},\\vec u]\\right|}{|\\vec u|}=%d\\).' % dd, ev='\\(d(M,d)=\\dfrac{\\left|[\\overrightarrow{PM},\\vec u]\\right|}{|\\vec u|}=%d\\).' % dd)

def l15_box(r, lv):
    a, b, c = r.sample([2, 3, 4], 3); kind = r.choice(['OB′', 'AC′', 'CA′'])
    if kind == 'OB′': P, u = (0, 0, 0), (a, b, c)
    elif kind == 'AC′': P, u = (a, 0, 0), (-a, b, c)
    else: P, u = (0, b, 0), (a, -b, c)
    cfg = boxcfg(a, b, c, segs=[(kind[0], kind[1:], {'color': '#c2410c', 'width': 3})])
    bads = [par(P, (u[0], u[1], -u[2])), par(P, (b, a, c) if kind == 'OB′' else (u[1], u[0], u[2])), par((a, b, c), u) if kind != 'OB′' else par(P, (a, b, 0))]
    return dict(en='The rectangular box \\(OABC.O′A′B′C′\\) has \\(O\\) at the origin and \\(B′%s\\) (see the figure). Parametric equations of the line \\(%s\\) are…' % (V3((a, b, c)), kind),
                vi='Hình hộp chữ nhật \\(OABC.O′A′B′C′\\) có \\(O\\) là gốc tọa độ và \\(B′%s\\) (xem hình). Phương trình tham số của đường thẳng \\(%s\\) là' % (V3((a, b, c)), kind),
                opts=fo(par(P, u), bads), fig=Q3D(cfg, 'Box'),
                ee='Through \\(%s%s\\) with direction \\(\\overrightarrow{%s}=%s\\).' % (kind[0], V3(P), kind, V3(u)), ev='Đi qua \\(%s%s\\), vectơ chỉ phương \\(\\overrightarrow{%s}=%s\\).' % (kind[0], V3(P), kind, V3(u)))

def l15_parm(r, lv):
    for _ in range(500):
        n = nzv(r, -3, 3); u0, u2 = nz(r, -3, 3), nz(r, -3, 3); num = -(n[0] * u0 + n[2] * u2)
        if num % n[1] == 0 and num // n[1] != 0:
            m = num // n[1]; P = rpt(r, -3, 3); e = nz(r, -6, 6)
            if dot(n, P) + e != 0: break
    else: raise AssertionError
    return dict(en='For which \\(m\\) is \\(d: %s\\) parallel to \\((P): %s\\)?' % (can(P, (u0, 'M', u2)).replace('{M}', '{m}'), plane(n, e)) if False else
                   'For which \\(m\\) is the line through \\(M%s\\) with direction \\(\\vec u=(%d;m;%d)\\) parallel to \\((P): %s\\)?' % (V3(P), u0, u2, plane(n, e)),
                vi='Với giá trị nào của \\(m\\) thì đường thẳng đi qua \\(M%s\\) có vectơ chỉ phương \\(\\vec u=(%d;m;%d)\\) song song với \\((P): %s\\)?' % (V3(P), u0, u2, plane(n, e)),
                opts=nopts(r, m, [-m, m + 1, n[1], m - 2 if m - 2 not in (-m, m + 1) else m + 3]),
                ee='\\(d\\parallel(P)\\Leftrightarrow\\vec u\\cdot\\vec n=0\\) and \\(M\\notin(P)\\): \\(%d%+dm%+d=0\\Rightarrow m=%d\\).' % (n[0] * u0, n[1], n[2] * u2, m),
                ev='\\(d\\parallel(P)\\Leftrightarrow\\vec u\\cdot\\vec n=0\\) và \\(M\\notin(P)\\): \\(%d%+dm%+d=0\\Rightarrow m=%d\\).' % (n[0] * u0, n[1], n[2] * u2, m))

def l15_laser(r, lv):
    t0 = r.choice([1, 2, 3]); u = (nz(r, -3, 3), nz(r, -3, 3), -r.choice([1, 2])); h = -u[2] * t0
    A = (r.randint(-2, 4), r.randint(-2, 4), h); Hh = tuple(int(x) for x in add(A, mul(t0, u)))
    assert Hh[2] == 0
    return dict(en='A laser beam starts at \\(A%s\\) (m) and travels in the direction \\(\\vec u=%s\\). Where does it hit the floor \\((Oxy)\\)?' % (V3(A), V3(u)),
                vi='Một tia laser xuất phát từ \\(A%s\\) (m) và đi theo hướng \\(\\vec u=%s\\). Tia laser chạm sàn \\((Oxy)\\) tại điểm nào?' % (V3(A), V3(u)),
                opts=fo(V3(Hh), [V3((A[0], A[1], 0)), V3(tuple(int(x) for x in sub(A, mul(t0, u))))[:-1] + ')' if False else V3(tuple(int(x) for x in sub(A, mul(t0, u)))), V3((Hh[0] + u[0], Hh[1] + u[1], 0))]),
                ee='\\(z=%d%+dt=0\\Leftrightarrow t=%d\\): the point \\(%s\\).' % (h, u[2], t0, V3(Hh)), ev='\\(z=%d%+dt=0\\Leftrightarrow t=%d\\): điểm \\(%s\\).' % (h, u[2], t0, V3(Hh)))

D15 = [l15_relpos, l15_par, l15_perp2, l15_foot, l15_dist, l15_box, l15_parm, l15_laser]

# =============================================================== Bài 16 – Công thức tính góc
def g16_box_lines(r, lv):
    a, b, c = r.sample([2, 3, 4], 3)
    P = {'O': (0, 0, 0), 'A': (a, 0, 0), 'C': (0, b, 0), 'B': (a, b, 0), 'O′': (0, 0, c), 'A′': (a, 0, c), 'C′': (0, b, c), 'B′': (a, b, c)}
    pairs = [('O', 'B′', 'A', 'C′'), ('O', 'B′', 'A', 'C'), ('A′', 'C', 'O', 'B'), ('O′', 'B', 'A', 'C′'), ('O', 'A′', 'O', 'C′'), ('O', 'B′', 'C', 'A′')]
    p, q, s, t = r.choice(pairs); u, w = sub(P[q], P[p]), sub(P[t], P[s]); d = abs(dot(u, w))
    if d == 0: raise AssertionError
    good = surd(d, n2(u) * n2(w))
    bads = [surd(d + 1, n2(u) * n2(w)), surd(d, n2(u) * n2(w) + 1) if True else '', frt(F(d, n2(u))), surd(max(1, d - 1), n2(u) * n2(w))]
    cfg = boxcfg(a, b, c, segs=[(p, q, {'color': '#c2410c', 'width': 3}), (s, t, {'color': '#1d4ed8', 'width': 3})])
    return dict(en='The rectangular box \\(OABC.O′A′B′C′\\) has \\(O\\) at the origin and \\(B′%s\\) (see the figure). The cosine of the angle between the lines \\(%s\\) and \\(%s\\) is…' % (V3((a, b, c)), p + q, s + t),
                vi='Hình hộp chữ nhật \\(OABC.O′A′B′C′\\) có \\(O\\) là gốc tọa độ và \\(B′%s\\) (xem hình). Côsin của góc giữa hai đường thẳng \\(%s\\) và \\(%s\\) bằng' % (V3((a, b, c)), p + q, s + t),
                opts=fo(good, bads), fig=Q3D(cfg, 'Box'),
                ee='\\(\\overrightarrow{%s}=%s\\), \\(\\overrightarrow{%s}=%s\\): \\(\\cos=\\dfrac{|%d|}{\\sqrt{%d}\\cdot\\sqrt{%d}}=%s\\).' % (p + q, V3(u), s + t, V3(w), dot(u, w), n2(u), n2(w), good),
                ev='\\(\\overrightarrow{%s}=%s\\), \\(\\overrightarrow{%s}=%s\\): \\(\\cos=\\dfrac{|%d|}{\\sqrt{%d}\\cdot\\sqrt{%d}}=%s\\).' % (p + q, V3(u), s + t, V3(w), dot(u, w), n2(u), n2(w), good))

DIAG = [(3, 4, 5), (6, 8, 10), (6, 8, 5), (2, 2, 2), (4, 3, 5), (4, 3, 2), (3, 4, 3)]
def g16_diag(r, lv):
    a, b, c = r.choice(DIAG); base2 = a * a + b * b
    tan = surd(c, base2)
    cfg = boxcfg(a, b, c, segs=[('O', 'B′', {'color': '#c2410c', 'width': 3}), ('O', 'B', {'dash': True, 'color': '#1d4ed8', 'width': 2})])
    return dict(en='The rectangular box \\(OABC.O′A′B′C′\\) has \\(O\\) at the origin and \\(B′%s\\) (see the figure). Let \\(\\varphi\\) be the angle between the line \\(OB′\\) and the plane \\((Oxy)\\). Then \\(\\tan\\varphi=\\)…' % V3((a, b, c)),
                vi='Hình hộp chữ nhật \\(OABC.O′A′B′C′\\) có \\(O\\) là gốc tọa độ và \\(B′%s\\) (xem hình). Gọi \\(\\varphi\\) là góc giữa đường thẳng \\(OB′\\) và mặt phẳng \\((Oxy)\\). Khi đó \\(\\tan\\varphi=\\)' % V3((a, b, c)),
                opts=fo(tan, [surd(int(math.isqrt(base2)) if isq(base2) else 1, c * c) if isq(base2) else surd(1, c * c * base2), surd(c, a * a + b * b + c * c), frt(F(c, a + b)), frt(F(c, a))]), fig=Q3D(cfg, 'Box'),
                ee='The projection of \\(OB′\\) on \\((Oxy)\\) is \\(OB=\\sqrt{%d}\\), and \\(BB′=%d\\): \\(\\tan\\varphi=\\dfrac{%d}{\\sqrt{%d}}=%s\\).' % (base2, c, c, base2, tan),
                ev='Hình chiếu của \\(OB′\\) lên \\((Oxy)\\) là \\(OB=\\sqrt{%d}\\), và \\(BB′=%d\\): \\(\\tan\\varphi=\\dfrac{%d}{\\sqrt{%d}}=%s\\).' % (base2, c, c, base2, tan))

def g16_dihedral(r, lv):
    a, b, c = r.sample([1, 2, 3, 4, 6], 3); nn = (b * c, a * c, a * b); N = n2(nn)
    good = surd(a * b, N)
    cfg = boxcfg(a, b, c); cfg['polygons'] = [{'points': ['A', 'C', 'O′'], 'fill': '#86e0bd', 'opacity': .45, 'outline': True}]
    return dict(en='The rectangular box \\(OABC.O′A′B′C′\\) has \\(O\\) at the origin and \\(B′%s\\) (see the figure). The cosine of the angle between the planes \\((ACO′)\\) and \\((Oxy)\\) is…' % V3((a, b, c)),
                vi='Hình hộp chữ nhật \\(OABC.O′A′B′C′\\) có \\(O\\) là gốc tọa độ và \\(B′%s\\) (xem hình). Côsin của góc giữa hai mặt phẳng \\((ACO′)\\) và \\((Oxy)\\) bằng' % V3((a, b, c)),
                opts=fo(good, [surd(b * c, N), surd(a * c, N), surd(c, a * a + b * b + c * c), surd(a * b, N + 1)]), fig=Q3D(cfg, 'Box'),
                ee='\\((ACO′): \\dfrac x{%d}+\\dfrac y{%d}+\\dfrac z{%d}=1\\), normal \\(%s\\); \\((Oxy)\\) has normal \\((0;0;1)\\): \\(\\cos=\\dfrac{%d}{\\sqrt{%d}}=%s\\).' % (a, b, c, V3(nn), a * b, N, good),
                ev='\\((ACO′): \\dfrac x{%d}+\\dfrac y{%d}+\\dfrac z{%d}=1\\), pháp tuyến \\(%s\\); \\((Oxy)\\) có pháp tuyến \\((0;0;1)\\): \\(\\cos=\\dfrac{%d}{\\sqrt{%d}}=%s\\).' % (a, b, c, V3(nn), a * b, N, good))

TANS = [(30, '\\dfrac{\\sqrt3}{3}'), (45, '1'), (60, '\\sqrt3')]
def g16_m(r, lv):
    ang, t = r.choice(TANS); comp = r.choice(['(1;0;m)', '(0;1;m)'])
    return dict(en='The line with direction vector \\(\\vec u=%s\\) (\\(m\\gt0\\)) makes an angle of \\(%d^\\circ\\) with the plane \\((Oxy)\\). Then \\(m=\\)…' % (comp, ang),
                vi='Đường thẳng có vectơ chỉ phương \\(\\vec u=%s\\) (\\(m\\gt0\\)) tạo với mặt phẳng \\((Oxy)\\) góc \\(%d^\\circ\\). Khi đó \\(m=\\)' % (comp, ang),
                opts=[t] + [x for a, x in TANS if a != ang] + ['\\dfrac12' if ang != 30 else '2'],
                ee='\\(\\sin\\varphi=\\dfrac{m}{\\sqrt{1+m^2}}\\Leftrightarrow m=\\tan\\varphi=\\tan%d^\\circ=%s\\).' % (ang, t), ev='\\(\\sin\\varphi=\\dfrac{m}{\\sqrt{1+m^2}}\\Leftrightarrow m=\\tan\\varphi=\\tan%d^\\circ=%s\\).' % (ang, t))

def g16_ramp(r, lv):
    for _ in range(3000):
        A = (r.randint(0, 3), r.randint(0, 3), 0); B = add(A, (r.randint(1, 6), r.randint(-2, 2), 0)); C = add(A, (r.randint(-2, 2), r.randint(1, 6), r.randint(1, 4)))
        n = cross(sub(B, A), sub(C, A))
        if n2(n) and isq(n2(n)) and n[2] and len(set(map(abs, n))) > 1: break
    else: raise AssertionError
    L = math.isqrt(n2(n)); cs = F(abs(n[2]), L)
    return dict(en='A ramp is a flat plane through \\(A%s\\), \\(B%s\\), \\(C%s\\) (m); the ground is \\((Oxy)\\). The cosine of the angle between the ramp and the ground is…' % (V3(A), V3(B), V3(C)),
                vi='Một con dốc là mặt phẳng đi qua \\(A%s\\), \\(B%s\\), \\(C%s\\) (m); mặt đất là \\((Oxy)\\). Côsin của góc giữa mặt dốc và mặt đất là' % (V3(A), V3(B), V3(C)),
                opts=fo(cs, [1 - cs if 1 - cs != cs else cs / 2, F(abs(n[0]), L) if F(abs(n[0]), L) != cs else F(abs(n[1]), L), F(abs(n[2]) + 1, L + 1), cs / 2]),
                ee='\\(\\vec n=[\\overrightarrow{AB},\\overrightarrow{AC}]=%s\\), \\(|\\vec n|=%d\\): \\(\\cos=\\dfrac{%d}{%d}=%s\\).' % (V3(n), L, abs(n[2]), L, frt(cs)),
                ev='\\(\\vec n=[\\overrightarrow{AB},\\overrightarrow{AC}]=%s\\), \\(|\\vec n|=%d\\): \\(\\cos=\\dfrac{%d}{%d}=%s\\).' % (V3(n), L, abs(n[2]), L, frt(cs)))

AX = [('(1;1;\\sqrt6)', 'Oz', 30), ('(1;1;0)', 'Ox', 45), ('(1;\\sqrt3;0)', 'Ox', 60), ('(0;1;1)', 'Oz', 45), ('(1;1;\\sqrt2)', 'Ox', 60), ('(1;1;\\sqrt2)', 'Oz', 45), ('(\\sqrt3;0;1)', 'Ox', 30), ('(2;0;0)', 'Oy', 90)]
def g16_axis(r, lv):
    u, ax, ang = r.choice(AX)
    return dict(en='The angle between the line with direction vector \\(\\vec u=%s\\) and the axis \\(%s\\) is…' % (u, ax), vi='Góc giữa đường thẳng có vectơ chỉ phương \\(\\vec u=%s\\) và trục \\(%s\\) bằng' % (u, ax),
                opts=['%d^\\circ' % ang] + ['%d^\\circ' % x for x in (30, 45, 60, 90) if x != ang],
                ee='\\(\\cos\\varphi=\\dfrac{|u_%s|}{|\\vec u|}\\), giving \\(%d^\\circ\\).' % (ax[1].lower(), ang), ev='\\(\\cos\\varphi=\\dfrac{|u_%s|}{|\\vec u|}\\), suy ra \\(%d^\\circ\\).' % (ax[1].lower(), ang))

SUN = [(2, 1, -2), (1, 2, -2), (2, -2, -1), (4, 4, -7), (6, 2, -3), (3, 6, -2), (2, 3, -6), (1, -4, -8)]
def g16_sun(r, lv):
    u = r.choice(SUN); L = math.isqrt(n2(u)); s = F(abs(u[2]), L); cs = None
    return dict(en='Sunlight travels in the direction \\(\\vec u=%s\\). Let \\(\\varphi\\) be the angle between the sun rays and the ground \\((Oxy)\\). Then \\(\\sin\\varphi=\\)…' % V3(u),
                vi='Ánh nắng chiếu theo hướng \\(\\vec u=%s\\). Gọi \\(\\varphi\\) là góc giữa tia nắng và mặt đất \\((Oxy)\\). Khi đó \\(\\sin\\varphi=\\)' % V3(u),
                opts=fo(s, [F(abs(u[0]), L) if F(abs(u[0]), L) != s else F(abs(u[1]), L), 1 - s, F(abs(u[2]), L + 1), s / 2]),
                ee='\\(\\sin\\varphi=\\dfrac{|\\vec u\\cdot\\vec k|}{|\\vec u|}=\\dfrac{%d}{%d}\\).' % (abs(u[2]), L), ev='\\(\\sin\\varphi=\\dfrac{|\\vec u\\cdot\\vec k|}{|\\vec u|}=\\dfrac{%d}{%d}\\).' % (abs(u[2]), L))

NICE2 = {F(1, 4): 30, F(1, 2): 45, F(3, 4): 60, F(1): 90}
def g16_lp(r, lv):
    for _ in range(5000):
        u = nzv(r, -2, 2); n = tuple(r.randint(-2, 2) for _ in range(3))
        if not n2(n): continue
        s2 = F(dot(u, n) ** 2, n2(u) * n2(n))
        if s2 in NICE2 and (s2 != 1 or r.random() < .2): break
    else: raise AssertionError
    ang = NICE2[s2]; P = rpt(r, -3, 3); e = r.randint(-5, 5)
    return dict(en='The angle between the line \\(d: %s\\) and the plane \\((P): %s\\) is…' % (can(P, u), plane(n, e)), vi='Góc giữa đường thẳng \\(d: %s\\) và mặt phẳng \\((P): %s\\) bằng' % (can(P, u), plane(n, e)),
                opts=['%d^\\circ' % ang] + ['%d^\\circ' % x for x in (30, 45, 60, 90) if x != ang],
                ee='\\(\\sin\\varphi=\\dfrac{|\\vec u\\cdot\\vec n|}{|\\vec u||\\vec n|}=\\dfrac{%d}{\\sqrt{%d}\\cdot\\sqrt{%d}}\\), so \\(\\varphi=%d^\\circ\\) (sine, not cosine, for a line and a plane).' % (abs(dot(u, n)), n2(u), n2(n), ang),
                ev='\\(\\sin\\varphi=\\dfrac{|\\vec u\\cdot\\vec n|}{|\\vec u||\\vec n|}=\\dfrac{%d}{\\sqrt{%d}\\cdot\\sqrt{%d}}\\), nên \\(\\varphi=%d^\\circ\\) (với đường thẳng và mặt phẳng dùng sin, không phải côsin).' % (abs(dot(u, n)), n2(u), n2(n), ang))

D16 = [g16_box_lines, g16_diag, g16_dihedral, g16_m, g16_ramp, g16_axis, g16_sun, g16_lp]
