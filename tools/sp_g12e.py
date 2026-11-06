# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 12 – Bài 15 (phương trình đường thẳng trong không gian), Bài 16 (công thức tính góc trong không gian).
Đáp án tính chính xác bằng số nguyên/Fraction; góc chỉ lấy các giá trị "đẹp" kiểm tra bằng cos² hữu tỉ."""
import math, itertools
from fractions import Fraction as F
from mb_selfpractice import pick_opts, fr
from mb_lib import TI
from sp_g12d import eq, V3, cross, dot, sub

def TT(en, vi): return '§' + TI(en, vi)
def neg(v): return tuple(-x for x in v)
def mul(k, v): return tuple(k * x for x in v)
def add(u, v): return tuple(a + b for a, b in zip(u, v))
def _d(r):
    v = (r.randint(-3, 3), r.randint(-3, 3), r.randint(-3, 3))
    if v == (0, 0, 0): raise AssertionError
    return v
def _p(r): return (r.randint(-3, 4), r.randint(-3, 4), r.randint(-3, 4))
def term(c, x0):
    """'x-1', 'y+3', 'z' cho tử số của phương trình chính tắc."""
    return '%s%s' % (c, '' if x0 == 0 else '%+d' % -x0)
def par(M, u):
    """Hệ phương trình tham số dạng \\begin{cases}."""
    rows = []
    for v, m, a in zip('xyz', M, u):
        if a == 0: rhs = str(m)
        else:
            c = ('' if abs(a) == 1 else str(abs(a))) + 't'
            rhs = (('-' if a < 0 else '') + c) if m == 0 else '%d%s%s' % (m, '+' if a > 0 else '-', c)
        rows.append('%s=%s' % (v, rhs))
    return '\\begin{cases}%s\\end{cases}' % '\\\\'.join(rows)
def alts(u):
    """Các vectơ sai thường gặp (đổi dấu một thành phần, đổi chỗ)."""
    out = [(u[0], u[1], -u[2]), (-u[0], u[1], u[2]), (u[1], u[0], u[2]), (u[0], u[2], u[1]), (u[0], -u[1], u[2])]
    return [w for w in out if w != tuple(u)]
def canon(M, u):
    assert all(u)
    return '=' .join('\\dfrac{%s}{%d}' % (term(v, m), a) for v, m, a in zip('xyz', M, u))
# ================= Bài 15. Phương trình đường thẳng =================
def ln_par(r, lv):
    M, u = _p(r), _d(r)
    if not all(u): raise AssertionError
    return dict(en='The line through \\(M%s\\) with direction vector \\(\\vec u=%s\\) has parametric equations…' % (V3(M), V3(u)), vi='Đường thẳng đi qua \\(M%s\\) và có vectơ chỉ phương \\(\\vec u=%s\\) có phương trình tham số…' % (V3(M), V3(u)),
      opts=pick_opts(r, par(M, u), [par(u, M) if all(M) else par(neg(M), u), par(neg(M), u)] + [par(M, w) for w in alts(u)] + [par(w, u) for w in alts(M)]), ans=0,
      ee='\\(x=x_0+at\\), \\(y=y_0+bt\\), \\(z=z_0+ct\\) with \\(M(x_0;y_0;z_0)\\), \\(\\vec u=(a;b;c)\\).', ev='\\(x=x_0+at\\), \\(y=y_0+bt\\), \\(z=z_0+ct\\) với \\(M(x_0;y_0;z_0)\\), \\(\\vec u=(a;b;c)\\).')
def ln_read(r, lv):
    M, u = _p(r), _d(r)
    if not all(u) or M == u: raise AssertionError
    k = r.choice([2, -1, -2, 3])
    return dict(en='A direction vector of the line \\(%s\\) is…' % canon(M, u), vi='Một vectơ chỉ phương của đường thẳng \\(%s\\) là…' % canon(M, u),
      opts=pick_opts(r, V3(mul(k, u)), [V3(M)] + ([V3(neg(M))] if any(M) else []) + [V3(w) for w in alts(u)]), ans=0,
      ee='The denominators give \\(\\vec u=%s\\); \\(%s\\) is a non-zero multiple of it.' % (V3(u), V3(mul(k, u))), ev='Các mẫu số cho \\(\\vec u=%s\\); \\(%s\\) là một bội khác 0 của nó.' % (V3(u), V3(mul(k, u))))
def ln_two(r, lv):
    A, B = _p(r), _p(r); u = sub(B, A)
    if not all(u): raise AssertionError
    return dict(en='The line \\(AB\\) with \\(A%s\\), \\(B%s\\) has the canonical equation…' % (V3(A), V3(B)), vi='Đường thẳng \\(AB\\) với \\(A%s\\), \\(B%s\\) có phương trình chính tắc…' % (V3(A), V3(B)),
      opts=pick_opts(r, canon(A, u), ([canon(neg(A), u)] if any(A) else []) + ([canon(A, add(A, B))] if all(add(A, B)) else []) + [canon(A, w) for w in alts(u) if all(w)]), ans=0,
      ee='\\(\\overrightarrow{AB}=%s\\) and the line passes through \\(A\\).' % V3(u), ev='\\(\\overrightarrow{AB}=%s\\), đường thẳng đi qua \\(A\\).' % V3(u))
def ln_on(r, lv):
    M, u = _p(r), _d(r); t = r.choice([-2, -1, 1, 2, 3]); P = add(M, mul(t, u)); others = []
    for _ in range(40):
        Q = add(P, (r.randint(-1, 1), r.randint(-1, 1), r.randint(-1, 1)))
        if cross(sub(Q, M), u) != (0, 0, 0) and V3(Q) not in others: others.append(V3(Q))
    if len(others) < 3: raise AssertionError
    return dict(en='Which point lies on the line \\(%s\\)?' % par(M, u), vi='Điểm nào thuộc đường thẳng \\(%s\\)?' % par(M, u), opts=pick_opts(r, V3(P), others[:3]), ans=0,
      ee='Take \\(t=%d\\): \\(%s\\).' % (t, V3(P)), ev='Lấy \\(t=%d\\): được \\(%s\\).' % (t, V3(P)))
def ln_perp(r, lv):
    M = _p(r); n = _d(r)
    if not all(n): raise AssertionError
    Dd = r.randint(-5, 5)
    return dict(en='The line through \\(M%s\\) perpendicular to \\((P): %s\\) is…' % (V3(M), eq(*n, Dd)), vi='Đường thẳng đi qua \\(M%s\\) và vuông góc với \\((P): %s\\) là…' % (V3(M), eq(*n, Dd)),
      opts=pick_opts(r, canon(M, n), ([canon(neg(M), n)] if any(M) else []) + ([canon(n, M)] if all(M) and M != n else []) + [canon(M, w) for w in alts(n) if all(w)]), ans=0,
      ee='Its direction vector is the normal vector \\(\\vec n=%s\\).' % V3(n), ev='Vectơ chỉ phương là vectơ pháp tuyến \\(\\vec n=%s\\).' % V3(n))
def ln_meet(r, lv):
    M, u = _p(r), _d(r); n = _d(r); du = dot(n, u)
    if du == 0: raise AssertionError
    t = r.choice([-2, -1, 1, 2]); P = add(M, mul(t, u)); Dd = -dot(n, P)
    others = [V3(add(M, mul(s, u))) for s in (t + 1, -t, t - 1) if s != t] + [V3(M), V3(add(P, (1, 0, 0)))]
    others = [o for o in dict.fromkeys(others) if o != V3(P)]
    return dict(en='The line \\(%s\\) meets the plane \\(%s\\) at…' % (par(M, u), eq(*n, Dd)), vi='Giao điểm của đường thẳng \\(%s\\) và mặt phẳng \\(%s\\) là…' % (par(M, u), eq(*n, Dd)),
      opts=pick_opts(r, V3(P), others), ans=0,
      ee='Substitute: \\(%dt%+d=0\\Rightarrow t=%d\\).' % (du, dot(n, M) + Dd, t), ev='Thay vào: \\(%dt%+d=0\\Rightarrow t=%d\\).' % (du, dot(n, M) + Dd, t))
REL = [('parallel', 'song song'), ('intersecting', 'cắt nhau'), ('skew', 'chéo nhau'), ('coincident', 'trùng nhau')]
def ln_rel(r, lv):
    M1, u = _p(r), _d(r); kind = r.choice([0, 1, 2]); k = r.choice([2, -1, -2])
    if kind == 0:
        M2 = add(M1, (1, 0, 0)) if cross((1, 0, 0), u) != (0, 0, 0) else add(M1, (0, 1, 0)); v = mul(k, u)
    else:
        v = _d(r)
        if cross(u, v) == (0, 0, 0): raise AssertionError
        if kind == 1: M2 = add(M1, mul(r.choice([1, 2, -1]), u)); M2 = add(M2, mul(r.choice([1, -1]), v))
        else:
            w = cross(u, v); M2 = add(M1, w if r.random() < .5 else neg(w))
    # kiểm tra lại bằng tích hỗn tạp
    c = cross(u, v); mixed = dot(c, sub(M2, M1))
    real = 0 if c == (0, 0, 0) and cross(u, sub(M2, M1)) != (0, 0, 0) else 3 if c == (0, 0, 0) else 1 if mixed == 0 else 2
    assert real == kind
    return dict(en='The lines \\(d_1: %s\\) and \\(d_2: %s\\) (parameter \\(s\\)) are…' % (par(M1, u), par(M2, v).replace('t', 's')), vi='Hai đường thẳng \\(d_1: %s\\) và \\(d_2: %s\\) (tham số \\(s\\))…' % (par(M1, u), par(M2, v).replace('t', 's')),
      opts=[TT(*REL[kind])] + [TT(*REL[j]) for j in range(4) if j != kind], ans=0,
      ee='\\([\\vec u_1,\\vec u_2]=%s\\), \\([\\vec u_1,\\vec u_2]\\cdot\\overrightarrow{M_1M_2}=%d\\).' % (V3(c), mixed), ev='\\([\\vec u_1,\\vec u_2]=%s\\), \\([\\vec u_1,\\vec u_2]\\cdot\\overrightarrow{M_1M_2}=%d\\).' % (V3(c), mixed))
def ln_drone(r, lv):
    M = (r.randint(0, 5), r.randint(0, 5), r.randint(1, 3)); u = (r.choice([1, 2, -1]), r.choice([1, 2, 3]), r.choice([1, 2])); t = r.choice([2, 3, 4, 5]); P = add(M, mul(t, u))
    return dict(en='A drone starts at \\(%s\\) and flies in a straight line with velocity \\(\\vec v=%s\\) (m/s). Its position after %d s is…' % (V3(M), V3(u), t), vi='Một drone xuất phát tại \\(%s\\), bay thẳng với vectơ vận tốc \\(\\vec v=%s\\) (m/s). Vị trí sau %d giây là…' % (V3(M), V3(u), t),
      opts=pick_opts(r, V3(P), [V3(add(M, mul(t + 1, u))), V3(mul(t, u)), V3(add(M, u)), V3(add(M, mul(t - 1, u)))]), ans=0,
      ee='\\(M+t\\vec v=%s+%d\\cdot%s=%s\\).' % (V3(M), t, V3(u), V3(P)), ev='\\(M+t\\vec v=%s+%d\\cdot%s=%s\\).' % (V3(M), t, V3(u), V3(P)))
M15S12 = [ln_par, ln_read, ln_two, ln_on, ln_perp, ln_meet, ln_rel, ln_drone]
# ================= Bài 16. Góc =================
VEC = [v for v in itertools.product(range(-2, 3), repeat=3) if any(v)]
def n2(v): return dot(v, v)
COS2 = {F(0): 90, F(1, 4): 60, F(1, 2): 45, F(3, 4): 30, F(1): 0}
PAIRS = {}
for a, b in itertools.combinations(VEC, 2):
    c2 = F(dot(a, b) ** 2, n2(a) * n2(b))
    if c2 in COS2 and c2 != 1: PAIRS.setdefault(COS2[c2], []).append((a, b))
def deg(x): return '%d^\\circ' % x
def an_ll(r, lv):
    g = r.choice([30, 45, 60, 90]); a, b = r.choice(PAIRS[g])
    if not all(a) or not all(b): M1, M2 = _p(r), _p(r); s1, s2 = par(M1, a), par(M2, b).replace('t', 's')
    else: s1, s2 = canon(_p(r), a), canon(_p(r), b)
    return dict(en='The angle between \\(d_1: %s\\) and \\(d_2: %s\\) is…' % (s1, s2), vi='Góc giữa hai đường thẳng \\(d_1: %s\\) và \\(d_2: %s\\) bằng…' % (s1, s2),
      opts=pick_opts(r, deg(g), [deg(x) for x in (30, 45, 60, 90, 120, 135) if x != g]), ans=0,
      ee='\\(\\cos=\\dfrac{|\\vec u_1\\cdot\\vec u_2|}{|\\vec u_1||\\vec u_2|}=\\dfrac{%d}{\\sqrt{%d}\\cdot\\sqrt{%d}}\\Rightarrow %s\\).' % (abs(dot(a, b)), n2(a), n2(b), deg(g)), ev='\\(\\cos=\\dfrac{|\\vec u_1\\cdot\\vec u_2|}{|\\vec u_1||\\vec u_2|}=\\dfrac{%d}{\\sqrt{%d}\\cdot\\sqrt{%d}}\\Rightarrow %s\\).' % (abs(dot(a, b)), n2(a), n2(b), deg(g)))
def an_lp(r, lv):
    g = r.choice([30, 45, 60]); a, n = r.choice(PAIRS[90 - g]);
    if r.random() < .5: a, n = n, a
    M = _p(r); Dd = r.randint(-4, 4)
    return dict(en='The angle between the line \\(%s\\) and the plane \\(%s\\) is…' % (par(M, a), eq(*n, Dd)), vi='Góc giữa đường thẳng \\(%s\\) và mặt phẳng \\(%s\\) bằng…' % (par(M, a), eq(*n, Dd)),
      opts=pick_opts(r, deg(g), [deg(90 - g)] + [deg(x) for x in (30, 45, 60, 90) if x not in (g, 90 - g)]), ans=0,
      ee='\\(\\sin\\varphi=\\dfrac{|\\vec u\\cdot\\vec n|}{|\\vec u||\\vec n|}=\\dfrac{%d}{\\sqrt{%d}\\cdot\\sqrt{%d}}\\Rightarrow\\varphi=%s\\) (sine, not cosine!).' % (abs(dot(a, n)), n2(a), n2(n), deg(g)), ev='\\(\\sin\\varphi=\\dfrac{|\\vec u\\cdot\\vec n|}{|\\vec u||\\vec n|}=\\dfrac{%d}{\\sqrt{%d}\\cdot\\sqrt{%d}}\\Rightarrow\\varphi=%s\\) (sin, không phải cos!).' % (abs(dot(a, n)), n2(a), n2(n), deg(g)))
def an_pp(r, lv):
    g = r.choice([45, 60, 90, 30]); a, b = r.choice(PAIRS[g])
    return dict(en='The angle between the planes \\(%s\\) and \\(%s\\) is…' % (eq(*a, r.randint(-4, 4)), eq(*b, r.randint(-4, 4))), vi='Góc giữa hai mặt phẳng \\(%s\\) và \\(%s\\) bằng…' % (eq(*a, r.randint(-4, 4)), eq(*b, r.randint(-4, 4))),
      opts=pick_opts(r, deg(g), [deg(x) for x in (30, 45, 60, 90, 120, 150) if x != g]), ans=0,
      ee='\\(\\cos=\\dfrac{|\\vec n_1\\cdot\\vec n_2|}{|\\vec n_1||\\vec n_2|}=\\dfrac{%d}{\\sqrt{%d}\\cdot\\sqrt{%d}}\\).' % (abs(dot(a, b)), n2(a), n2(b)), ev='\\(\\cos=\\dfrac{|\\vec n_1\\cdot\\vec n_2|}{|\\vec n_1||\\vec n_2|}=\\dfrac{%d}{\\sqrt{%d}\\cdot\\sqrt{%d}}\\).' % (abs(dot(a, b)), n2(a), n2(b)))
L3 = [(1, 2, 2), (2, 1, 2), (2, 2, 1), (0, 0, 3), (3, 0, 0), (0, 3, 0), (1, -2, 2), (2, -1, -2), (-2, 2, 1)]
def an_cos(r, lv):
    a, b = r.sample(L3, 2); c = F(abs(dot(a, b)), 9)
    if c == 0: raise AssertionError
    return dict(en='\\(d_1\\), \\(d_2\\) have direction vectors \\(\\vec u_1=%s\\), \\(\\vec u_2=%s\\). \\(\\cos(d_1,d_2)=\\)…' % (V3(a), V3(b)), vi='\\(d_1\\), \\(d_2\\) có vectơ chỉ phương \\(\\vec u_1=%s\\), \\(\\vec u_2=%s\\). \\(\\cos(d_1,d_2)=\\)…' % (V3(a), V3(b)),
      opts=pick_opts(r, fr(c), [fr(-c) if dot(a, b) < 0 else fr(c / 3), fr(F(abs(dot(a, b)), 3)), fr(F(abs(dot(a, b)), 81)), fr(1 - c) if c != F(1, 2) else fr(c * 2)]), ans=0,
      ee='\\(|\\vec u_1|=|\\vec u_2|=3\\); \\(\\cos=\\dfrac{|%d|}{9}=%s\\) (always \\(\\ge0\\)).' % (dot(a, b), fr(c)), ev='\\(|\\vec u_1|=|\\vec u_2|=3\\); \\(\\cos=\\dfrac{|%d|}{9}=%s\\) (luôn \\(\\ge0\\)).' % (dot(a, b), fr(c)))
def an_m(r, lv):
    u = (r.choice([1, 2, 3]), r.choice([-1, 1, 2]), r.choice([1, -2, 3])); b, c = r.randint(-3, 3), r.randint(-3, 3); t = -(u[1] * b + u[2] * c)
    if t % u[0]: raise AssertionError
    m = t // u[0]
    return dict(en='\\(\\vec u_1=%s\\), \\(\\vec u_2=(m;%d;%d)\\) are direction vectors of \\(d_1\\), \\(d_2\\). \\(d_1\\perp d_2\\) when \\(m=\\)…' % (V3(u), b, c), vi='\\(\\vec u_1=%s\\), \\(\\vec u_2=(m;%d;%d)\\) là vectơ chỉ phương của \\(d_1\\), \\(d_2\\). \\(d_1\\perp d_2\\) khi \\(m=\\)…' % (V3(u), b, c),
      opts=pick_opts(r, str(m), [str(-m) if m else '1', str(m + 1), str(m - 2), str(u[0])]), ans=0,
      ee='\\(\\vec u_1\\cdot\\vec u_2=%dm%+d=0\\Rightarrow m=%d\\).' % (u[0], -t, m), ev='\\(\\vec u_1\\cdot\\vec u_2=%dm%+d=0\\Rightarrow m=%d\\).' % (u[0], -t, m))
SQN = [(1, 2, 2), (2, 1, 2), (2, 2, 1), (2, 3, 6), (3, 2, 6), (6, 2, 3), (1, 4, 8), (4, 1, 8), (4, 4, 7), (8, 4, 1), (2, 6, 3)]
def _sgn(r, v): return tuple(x * r.choice([1, -1]) for x in v)
def an_roof(r, lv):
    n = _sgn(r, r.choice(SQN)); L = int(math.isqrt(n2(n))); assert L * L == n2(n); c = F(abs(n[2]), L); H = r.choice([3, 4, 5, 6])
    return dict(en='A solar panel lies in the plane \\(%s\\) (the ground is \\((Oxy)\\)). The cosine of the angle between the panel and the ground is…' % eq(*n, -H), vi='Một tấm pin mặt trời nằm trong mặt phẳng \\(%s\\) (mặt đất là \\((Oxy)\\)). Côsin của góc giữa tấm pin và mặt đất bằng…' % eq(*n, -H),
      opts=pick_opts(r, fr(c), [fr(F(abs(n[0]), L)), fr(F(abs(n[1]), L)), fr(F(abs(n[2]), L * L)), fr(1 - c), fr(c / 2)]), ans=0,
      ee='\\(\\vec n=%s\\), \\(\\vec k=(0;0;1)\\): \\(\\cos=\\dfrac{|%d|}{\\sqrt{%d}}=%s\\).' % (V3(n), n[2], n2(n), fr(c)), ev='\\(\\vec n=%s\\), \\(\\vec k=(0;0;1)\\): \\(\\cos=\\dfrac{|%d|}{\\sqrt{%d}}=%s\\).' % (V3(n), n[2], n2(n), fr(c)))
def an_axis(r, lv):
    n = _sgn(r, r.choice(SQN)); L = int(math.isqrt(n2(n))); ax = r.randrange(3); c = F(abs(n[ax]), L); nm = ['Ox', 'Oy', 'Oz'][ax]
    return dict(en='\\(\\varphi\\) is the angle between the axis \\(%s\\) and the plane \\(%s\\). \\(\\sin\\varphi=\\)…' % (nm, eq(*n, r.randint(-3, 3))), vi='Gọi \\(\\varphi\\) là góc giữa trục \\(%s\\) và mặt phẳng \\(%s\\). \\(\\sin\\varphi=\\)…' % (nm, eq(*n, r.randint(-3, 3))),
      opts=pick_opts(r, fr(c), [fr(F(abs(n[i]), L)) for i in range(3) if i != ax] + [fr(F(abs(n[ax]), L * L)), fr(1 - c), fr(c / 2)]), ans=0,
      ee='\\(\\sin\\varphi=\\dfrac{|\\vec e\\cdot\\vec n|}{|\\vec e||\\vec n|}=\\dfrac{%d}{%d}\\).' % (abs(n[ax]), L), ev='\\(\\sin\\varphi=\\dfrac{|\\vec e\\cdot\\vec n|}{|\\vec e||\\vec n|}=\\dfrac{%d}{%d}\\).' % (abs(n[ax]), L))
M16S12 = [an_ll, an_lp, an_pp, an_cos, an_m, an_roof, an_axis, an_ll]
