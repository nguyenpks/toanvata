# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 10 – Bài 20 (vị trí tương đối, góc, khoảng cách), Bài 21 (đường tròn trong mặt phẳng tọa độ),
Bài 22 (ba đường conic). Đáp án tính chính xác bằng số nguyên / Fraction / căn thức rút gọn."""
import math
from fractions import Fraction as F
from mb_selfpractice import pick_opts, fr
from sp_g10f import TT
from sp_g10g import leq, norm3, V2


def sq_split(s):
    """s = q²·m (m không chứa bình phương) → (q, m)."""
    q = 1
    for k in range(int(math.isqrt(s)), 1, -1):
        if s % (k * k) == 0: q = k; break
    return q, s // (q * q)


def surd(num, s):
    """num / √s (num ≥ 0, s > 0) viết gọn dạng p√m / d."""
    num = F(num); q, m = sq_split(s)
    v = num / (q * m) if m > 1 else num / q           # = (num·√m)/(q·m)
    if m == 1: return fr(v)
    if v == 0: return '0'
    p, d = v.numerator, v.denominator
    top = ('' if p == 1 else str(p)) + '\\sqrt{%d}' % m
    return top if d == 1 else '\\dfrac{%s}{%d}' % (top, d)


def rt(s):
    q, m = sq_split(s)
    return str(q) if m == 1 else ('' if q == 1 else str(q)) + '\\sqrt{%d}' % m


PYN = [(3, 4), (4, 3), (3, -4), (4, -3), (5, 12), (12, -5), (6, 8), (8, -6), (1, 0), (0, 1)]


def _pt(r): return (r.randint(-4, 5), r.randint(-4, 5))


def _n(r):
    while True:
        a, b = r.randint(-4, 4), r.randint(-4, 4)
        if (a, b) != (0, 0) and math.gcd(abs(a), abs(b)) == 1: return a, b


# ================= Bài 20. Vị trí tương đối, góc và khoảng cách =================
POS = [('parallel', 'song song'), ('coincident', 'trùng nhau'), ('intersecting but not perpendicular', 'cắt nhau nhưng không vuông góc'), ('perpendicular', 'vuông góc')]


def rp_pos(r, lv):
    a, b = _n(r); c = r.randint(-5, 5); kind = r.randrange(4); k = r.choice([2, -2, 3, -1])
    if kind == 0: a2, b2, c2 = k * a, k * b, k * c + r.choice([1, 2, -3])
    elif kind == 1: a2, b2, c2 = k * a, k * b, k * c
    elif kind == 3: a2, b2, c2 = -b, a, r.randint(-5, 5)
    else:
        a2, b2 = a + r.choice([1, -1]), b + r.choice([2, -1]); c2 = r.randint(-5, 5)
        if a * b2 - a2 * b == 0 or a * a2 + b * b2 == 0: raise AssertionError
    if (a2, b2) == (0, 0): raise AssertionError
    opts = [TT(*POS[kind])] + [TT(*POS[j]) for j in range(4) if j != kind]
    why = {0: ('\\(\\dfrac{a_1}{a_2}=\\dfrac{b_1}{b_2}\\ne\\dfrac{c_1}{c_2}\\).', '\\(\\dfrac{a_1}{a_2}=\\dfrac{b_1}{b_2}\\ne\\dfrac{c_1}{c_2}\\) nên hai đường thẳng song song.'),
           1: ('The coefficients are proportional (factor \\(%d\\)).' % k, 'Các hệ số tỉ lệ (hệ số tỉ lệ \\(%d\\)) nên hai đường thẳng trùng nhau.' % k),
           2: ('\\(a_1b_2-a_2b_1=%d\\ne0\\) and \\(\\vec n_1\\cdot\\vec n_2=%d\\ne0\\).' % (a * b2 - a2 * b, a * a2 + b * b2), '\\(a_1b_2-a_2b_1=%d\\ne0\\) và \\(\\vec n_1\\cdot\\vec n_2=%d\\ne0\\): cắt nhau, không vuông góc.' % (a * b2 - a2 * b, a * a2 + b * b2)),
           3: ('\\(\\vec n_1\\cdot\\vec n_2=%d\\cdot(%d)%+d\\cdot%d=0\\).' % (a, a2, b, b2), '\\(\\vec n_1\\cdot\\vec n_2=%d\\cdot(%d)%+d\\cdot%d=0\\) nên hai đường thẳng vuông góc.' % (a, a2, b, b2))}[kind]
    return dict(en='The lines \\(%s\\) and \\(%s\\) are…' % (leq(a, b, c), leq(a2, b2, c2)), vi='Hai đường thẳng \\(%s\\) và \\(%s\\)…' % (leq(a, b, c), leq(a2, b2, c2)), opts=opts, ans=0, ee=why[0], ev=why[1])


def rp_perp_m(r, lv):
    a, b = r.choice([(1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2), (1, -2), (2, -1), (1, -3), (3, -2)]); k = r.choice([1, 2, -1, 3, -2]); c = r.randint(-5, 5)
    m = F(-b * k, a)
    if m.denominator != 1: raise AssertionError
    m = int(m)
    return dict(en='The lines \\(%s\\) and \\(mx%+dy+1=0\\) are perpendicular when \\(m=\\)…' % (leq(a, b, c), k), vi='Hai đường thẳng \\(%s\\) và \\(mx%+dy+1=0\\) vuông góc khi \\(m=\\)…' % (leq(a, b, c), k),
      opts=pick_opts(r, str(m), [str(-m), fr(F(b * k, a) if a else 1) if F(b * k, a) != m else str(m + 1), fr(F(a * k, b)), str(m + 2), str(m - 1)]), ans=0,
      ee='\\(\\vec n_1\\cdot\\vec n_2=%d m%+d=0\\).' % (a, b * k), ev='\\(\\vec n_1\\cdot\\vec n_2=0\\iff %dm%+d=0\\iff m=%d\\).' % (a, b * k, m))


def rp_par_line(r, lv):
    a, b = _n(r); c = r.randint(-5, 5); M = _pt(r); c2 = -(a * M[0] + b * M[1])
    if c2 == c: raise AssertionError
    A, B, C = norm3(a, b, c2)
    return dict(en='The line through \\(M%s\\) parallel to \\(%s\\) is…' % (V2(M), leq(a, b, c)), vi='Đường thẳng đi qua \\(M%s\\) và song song với \\(%s\\) là…' % (V2(M), leq(a, b, c)),
      opts=pick_opts(r, leq(A, B, C), [leq(*norm3(b, -a, -(b * M[0] - a * M[1]))), leq(*norm3(a, b, -c2)) if c2 else leq(A, B, 1), leq(*norm3(a, b, c)), leq(*norm3(a, -b, c2)) if b and a else leq(A, B, C + 2)]), ans=0,
      ee='Same normal vector \\(%s\\): \\(%d(x%+d)%+d(y%+d)=0\\).' % (V2((a, b)), a, -M[0], b, -M[1]), ev='Cùng vectơ pháp tuyến \\(%s\\): \\(%d(x%+d)%+d(y%+d)=0\\).' % (V2((a, b)), a, -M[0], b, -M[1]))


def rp_dist(r, lv):
    a, b = r.choice(PYN); c = r.randint(-9, 9); M = _pt(r); N = abs(a * M[0] + b * M[1] + c); s = a * a + b * b
    if N == 0: raise AssertionError
    d = surd(N, s)
    return dict(en='The distance from \\(M%s\\) to \\(%s\\) is…' % (V2(M), leq(a, b, c)), vi='Khoảng cách từ \\(M%s\\) đến đường thẳng \\(%s\\) là…' % (V2(M), leq(a, b, c)),
      opts=pick_opts(r, d, [surd(abs(a * M[0] + b * M[1] - c), s) if c else surd(N + 1, s), surd(N, s * s) if s > 1 else str(N + 1), str(N), surd(abs(a * M[1] + b * M[0] + c), s), surd(N + 2, s)]), ans=0,
      ee='\\(d=\\dfrac{|%d\\cdot(%d)%+d\\cdot(%d)%+d|}{\\sqrt{%d}}\\).' % (a, M[0], b, M[1], c, s), ev='\\(d=\\dfrac{|ax_0+by_0+c|}{\\sqrt{a^2+b^2}}=\\dfrac{%d}{%s}\\).' % (N, rt(s)))


def rp_cos(r, lv):
    n1, n2 = _n(r), _n(r); p = abs(n1[0] * n2[0] + n1[1] * n2[1]); s = (n1[0] ** 2 + n1[1] ** 2) * (n2[0] ** 2 + n2[1] ** 2)
    if p == 0 or n1[0] * n2[1] == n1[1] * n2[0]: raise AssertionError
    c1, c2 = r.randint(-4, 4), r.randint(-4, 4)
    return dict(en='Let \\(\\varphi\\) be the angle between \\(%s\\) and \\(%s\\). Then \\(\\cos\\varphi=\\)…' % (leq(*n1, c1), leq(*n2, c2)), vi='Gọi \\(\\varphi\\) là góc giữa hai đường thẳng \\(%s\\) và \\(%s\\). Khi đó \\(\\cos\\varphi=\\)…' % (leq(*n1, c1), leq(*n2, c2)),
      opts=pick_opts(r, surd(p, s), [surd(abs(n1[0] * n2[1] - n1[1] * n2[0]), s), surd(p + 1, s), surd(p, s * 4), surd(abs(n1[0] * n2[0] - n1[1] * n2[1]) or p + 2, s), surd(p + 2, s)]), ans=0,
      ee='\\(\\cos\\varphi=\\dfrac{|\\vec n_1\\cdot\\vec n_2|}{|\\vec n_1|\\,|\\vec n_2|}=\\dfrac{%d}{\\sqrt{%d}}\\).' % (p, s), ev='\\(\\cos\\varphi=\\dfrac{|a_1a_2+b_1b_2|}{\\sqrt{a_1^2+b_1^2}\\sqrt{a_2^2+b_2^2}}=\\dfrac{%d}{\\sqrt{%d}}\\).' % (p, s))


def rp_angle(r, lv):
    a, b = _n(r); kind = r.choice([45, 90, 45])
    a2, b2 = (a - b, a + b) if kind == 45 else (-b, a)
    g = math.gcd(abs(a2), abs(b2)) or 1; a2, b2 = a2 // g, b2 // g
    c1, c2 = r.randint(-4, 4), r.randint(-4, 4)
    p = abs(a * a2 + b * b2)
    return dict(en='The angle between \\(%s\\) and \\(%s\\) is…' % (leq(a, b, c1), leq(a2, b2, c2)), vi='Góc giữa hai đường thẳng \\(%s\\) và \\(%s\\) bằng…' % (leq(a, b, c1), leq(a2, b2, c2)),
      opts=pick_opts(r, '%d^\\circ' % kind, ['%d^\\circ' % x for x in (30, 60, 135, 90, 45) if x != kind]), ans=0,
      ee='\\(\\cos\\varphi=\\dfrac{%d}{\\sqrt{%d}\\sqrt{%d}}\\).' % (p, a * a + b * b, a2 * a2 + b2 * b2), ev='\\(\\cos\\varphi=\\dfrac{%d}{\\sqrt{%d}\\cdot\\sqrt{%d}}=%s\\).' % (p, a * a + b * b, a2 * a2 + b2 * b2, '0' if kind == 90 else '\\dfrac{\\sqrt2}{2}'))


def rp_dpar(r, lv):
    a, b = r.choice(PYN[:8]); c1 = r.randint(-9, 9); c2 = c1 + r.choice([-15, -10, -5, 5, 10, 13, 7, -8])
    s = a * a + b * b; N = abs(c1 - c2)
    return dict(en='The distance between the parallel lines \\(%s\\) and \\(%s\\) is…' % (leq(a, b, c1), leq(a, b, c2)), vi='Khoảng cách giữa hai đường thẳng song song \\(%s\\) và \\(%s\\) là…' % (leq(a, b, c1), leq(a, b, c2)),
      opts=pick_opts(r, surd(N, s), [surd(abs(c1 + c2) or N + 1, s), str(N), surd(N, s * s), surd(N + 5, s)]), ans=0,
      ee='Take a point of one line and its distance to the other: \\(\\dfrac{|c_1-c_2|}{\\sqrt{a^2+b^2}}\\).', ev='Lấy một điểm trên đường này rồi tính khoảng cách đến đường kia: \\(\\dfrac{|c_1-c_2|}{\\sqrt{a^2+b^2}}=\\dfrac{%d}{%d}\\).' % (N, math.isqrt(s)))


def rp_meet(r, lv):
    P = _pt(r); n1, n2 = _n(r), _n(r)
    if n1[0] * n2[1] - n1[1] * n2[0] == 0: raise AssertionError
    c1, c2 = -(n1[0] * P[0] + n1[1] * P[1]), -(n2[0] * P[0] + n2[1] * P[1])
    return dict(en='The lines \\(%s\\) and \\(%s\\) meet at…' % (leq(*n1, c1), leq(*n2, c2)), vi='Giao điểm của hai đường thẳng \\(%s\\) và \\(%s\\) là…' % (leq(*n1, c1), leq(*n2, c2)),
      opts=pick_opts(r, V2(P), [V2((P[1], P[0])), V2((-P[0], P[1])), V2((P[0], -P[1])), V2((-P[0], -P[1])), V2((P[0] + 1, P[1]))]), ans=0,
      ee='Solve the system of the two equations.', ev='Giải hệ hai phương trình; kiểm tra: tọa độ \\(%s\\) thỏa mãn cả hai.' % V2(P))


def rp_pipe(r, lv):
    a, b = r.choice(PYN[:8]); c = r.choice([-20, -15, 10, 12, 25, -30]); H = (r.randint(1, 6), r.randint(1, 6)); N = abs(a * H[0] + b * H[1] + c); s = a * a + b * b
    if N == 0: raise AssertionError
    d = F(N, math.isqrt(s)) * 100
    return dict(en='On a map (unit 100 m) a house is at \\(H%s\\) and a straight water main runs along \\(%s\\). The shortest pipe from the house to the main is…' % (V2(H), leq(a, b, c)),
      vi='Trên bản đồ (đơn vị 100 m), một ngôi nhà ở \\(H%s\\), đường ống nước chính chạy theo đường thẳng \\(%s\\). Đoạn ống ngắn nhất nối nhà với đường ống chính dài…' % (V2(H), leq(a, b, c)),
      opts=pick_opts(r, '%s\\text{ m}' % fr(d), ['%s\\text{ m}' % fr(F(N) * 100), '%s\\text{ m}' % fr(F(N, s) * 100), '%s\\text{ m}' % fr(d + 100), '%s\\text{ m}' % fr(F(abs(a * H[0] + b * H[1] - c), math.isqrt(s)) * 100)]), ans=0,
      ee='The shortest pipe is perpendicular: \\(d=\\dfrac{%d}{%d}\\) units.' % (N, math.isqrt(s)), ev='Đoạn ngắn nhất là đoạn vuông góc: \\(d=\\dfrac{%d}{%d}\\) đơn vị \\(=%s\\) m.' % (N, math.isqrt(s), fr(d)))


M20S10 = [rp_pos, rp_perp_m, rp_par_line, rp_dist, rp_meet, rp_angle, rp_cos, rp_dpar, rp_pipe]


# ================= Bài 21. Đường tròn trong mặt phẳng tọa độ =================
def ceq(a, b, R2):
    f = lambda v, c: v if c == 0 else '(%s%s%d)' % (v, '-' if c > 0 else '+', abs(c))
    return '%s^2+%s^2=%d' % (f('x', a), f('y', b), R2)


def cgen(a, b, c):
    s = 'x^2+y^2'
    for k, v in ((-2 * a, 'x'), (-2 * b, 'y')):
        if k: s += ('-' if k < 0 else '+') + ('' if abs(k) == 1 else str(abs(k))) + v
    if c: s += '%+d' % c
    return s + '=0'


def c_center(r, lv):
    a, b = r.randint(-5, 5), r.randint(-5, 5); R = r.randint(1, 6)
    if a == 0 and b == 0: raise AssertionError
    o = lambda A, B, RR: TT('centre \\((%d;%d)\\), radius \\(%s\\)' % (A, B, RR), 'tâm \\((%d;%d)\\), bán kính \\(%s\\)' % (A, B, RR))
    return dict(en='The circle \\(%s\\) has…' % ceq(a, b, R * R), vi='Đường tròn \\(%s\\) có…' % ceq(a, b, R * R),
      opts=pick_opts(r, o(a, b, R), [o(-a, -b, R), o(a, b, R * R), o(-a, -b, R * R), o(b, a, R) if a != b else o(a, -b, R)]), ans=0,
      ee='\\((x-a)^2+(y-b)^2=R^2\\): centre \\((a;b)\\), radius \\(R\\).', ev='\\((x-a)^2+(y-b)^2=R^2\\) có tâm \\(I(a;b)\\), bán kính \\(R\\).')


def c_general(r, lv):
    a, b = r.randint(-4, 4), r.randint(-4, 4); R = r.randint(1, 6); c = a * a + b * b - R * R
    if a == 0 or b == 0: raise AssertionError
    o = lambda A, B, RR: TT('\\(I(%d;%d)\\), \\(R=%s\\)' % (A, B, RR), '\\(I(%d;%d)\\), \\(R=%s\\)' % (A, B, RR))
    w = [o(-a, -b, R), o(2 * a, 2 * b, R), o(a, b, rt(R * R + 2 * abs(c)) if c else R + 1), o(a, b, rt(abs(c)) if c and abs(c) != R * R else R + 2)]
    return dict(en='The circle \\(%s\\) has centre and radius…' % cgen(a, b, c), vi='Đường tròn \\(%s\\) có tâm và bán kính…' % cgen(a, b, c),
      opts=pick_opts(r, o(a, b, R), w), ans=0,
      ee='\\(a=%d\\), \\(b=%d\\), \\(R=\\sqrt{a^2+b^2-c}=\\sqrt{%d}\\).' % (a, b, R * R), ev='\\(-2a=%d\\Rightarrow a=%d\\); \\(-2b=%d\\Rightarrow b=%d\\); \\(R=\\sqrt{a^2+b^2-c}=\\sqrt{%d}=%d\\).' % (-2 * a, a, -2 * b, b, R * R, R))


def c_iscircle(r, lv):
    a, b = r.randint(-3, 3), r.randint(-3, 3); R = r.randint(1, 4); c = a * a + b * b - R * R
    good = cgen(a, b, c); bad1 = cgen(a, b, a * a + b * b + r.randint(1, 5))
    bad2 = good.replace('y^2', '2y^2', 1); bad3 = good.replace('x^2+y^2', 'x^2-y^2', 1); bad4 = good.replace('=0', '+xy=0')
    return dict(en='Which equation is the equation of a circle?', vi='Phương trình nào là phương trình đường tròn?', opts=pick_opts(r, '%s' % good, [bad1, bad2, bad3, bad4]), ans=0,
      ee='Need equal coefficients of \\(x^2\\), \\(y^2\\), no \\(xy\\) term and \\(a^2+b^2-c\\gt0\\).', ev='Cần hệ số của \\(x^2\\) và \\(y^2\\) bằng nhau, không có hạng tử \\(xy\\) và \\(a^2+b^2-c\\gt0\\).')


def c_write(r, lv):
    I, A = _pt(r), _pt(r); R2 = (A[0] - I[0]) ** 2 + (A[1] - I[1]) ** 2
    if R2 == 0 or I == (0, 0): raise AssertionError
    return dict(en='The circle with centre \\(I%s\\) through \\(A%s\\) is…' % (V2(I), V2(A)), vi='Đường tròn tâm \\(I%s\\) và đi qua \\(A%s\\) có phương trình…' % (V2(I), V2(A)),
      opts=pick_opts(r, ceq(*I, R2), [ceq(-I[0], -I[1], R2), ceq(*I, R2 + 1), ceq(*A, R2), ceq(*I, round(math.sqrt(R2) * 100) // 100 + 1)]), ans=0,
      ee='\\(R^2=IA^2=%d\\).' % R2, ev='\\(R^2=IA^2=(%d)^2+(%d)^2=%d\\).' % (A[0] - I[0], A[1] - I[1], R2))


def c_diam(r, lv):
    A = _pt(r); B = (A[0] + 2 * r.randint(-3, 3), A[1] + 2 * r.randint(-3, 3))
    if A == B: raise AssertionError
    I = ((A[0] + B[0]) // 2, (A[1] + B[1]) // 2); R2 = (A[0] - I[0]) ** 2 + (A[1] - I[1]) ** 2; AB2 = 4 * R2
    if I == (0, 0): raise AssertionError
    return dict(en='The circle with diameter \\(AB\\), \\(A%s\\), \\(B%s\\) is…' % (V2(A), V2(B)), vi='Đường tròn đường kính \\(AB\\) với \\(A%s\\), \\(B%s\\) có phương trình…' % (V2(A), V2(B)),
      opts=pick_opts(r, ceq(*I, R2), [ceq(*I, AB2), ceq(-I[0], -I[1], R2), ceq(*A, AB2), ceq(*I, R2 + 1)]), ans=0,
      ee='Centre = midpoint \\(I%s\\); \\(R^2=\\dfrac{AB^2}{4}=%d\\).' % (V2(I), R2), ev='Tâm là trung điểm \\(I%s\\); \\(R^2=\\dfrac{AB^2}{4}=%d\\).' % (V2(I), R2))


def c_tangent(r, lv):
    I = _pt(r); u = r.choice([(3, 4), (4, 3), (-3, 4), (0, 5), (5, 0), (-4, -3), (1, 2), (2, -1), (0, 3), (-2, 2)]); M = (I[0] + u[0], I[1] + u[1]); R2 = u[0] ** 2 + u[1] ** 2
    a, b, c = norm3(u[0], u[1], -(u[0] * M[0] + u[1] * M[1]))
    return dict(en='The tangent to \\(%s\\) at \\(M%s\\) is…' % (ceq(*I, R2), V2(M)), vi='Tiếp tuyến của đường tròn \\(%s\\) tại điểm \\(M%s\\) là…' % (ceq(*I, R2), V2(M)),
      opts=pick_opts(r, leq(a, b, c), [leq(*norm3(u[1], -u[0], -(u[1] * M[0] - u[0] * M[1]))), leq(*norm3(u[0], u[1], -(u[0] * I[0] + u[1] * I[1]))), leq(*norm3(u[0], u[1], -c)) if c else leq(a, b, 1), leq(*norm3(u[0], -u[1], c)) if u[1] and u[0] else leq(a, b, c + 3)]), ans=0,
      ee='Normal vector \\(\\overrightarrow{IM}=%s\\), through \\(M\\).' % V2(u), ev='Tiếp tuyến qua \\(M\\), nhận \\(\\overrightarrow{IM}=%s\\) làm vectơ pháp tuyến.' % V2(u))


def c_pos(r, lv):
    I = _pt(r); R = r.randint(2, 5); a, b = r.choice(PYN[:8]); s = math.isqrt(a * a + b * b); kind = r.randrange(3)
    D = {0: R * s - r.randint(1, R * s - 1), 1: R * s, 2: R * s + r.randint(1, 6)}[kind]
    c = r.choice([1, -1]) * D - (a * I[0] + b * I[1])
    opts = [TT('the line meets the circle at two points', 'cắt đường tròn tại hai điểm'), TT('the line is tangent to the circle', 'tiếp xúc với đường tròn'), TT('the line does not meet the circle', 'không cắt đường tròn'), TT('the line passes through the centre', 'đi qua tâm đường tròn')]
    if kind == 0 and D == 0: raise AssertionError
    order = [opts[kind]] + [opts[j] for j in range(4) if j != kind]
    return dict(en='The line \\(%s\\) and the circle \\(%s\\):' % (leq(a, b, c), ceq(*I, R * R)), vi='Đường thẳng \\(%s\\) và đường tròn \\(%s\\):' % (leq(a, b, c), ceq(*I, R * R)), opts=order, ans=0,
      ee='\\(d(I,\\Delta)=%s\\) compared with \\(R=%d\\).' % (fr(F(D, s)), R), ev='\\(d(I,\\Delta)=\\dfrac{%d}{%d}=%s\\) so với \\(R=%d\\).' % (D, s, fr(F(D, s)), R))


def c_tanR(r, lv):
    I = _pt(r); a, b = r.choice(PYN[:8]); s = math.isqrt(a * a + b * b); D = s * r.randint(1, 4) * r.choice([1, 1, 2]) + r.choice([0, 0, s]); c = D - (a * I[0] + b * I[1])
    R = F(D, s); R2 = R * R
    if R2.denominator != 1: raise AssertionError
    R2 = int(R2)
    return dict(en='The circle with centre \\(I%s\\) tangent to \\(%s\\) is…' % (V2(I), leq(a, b, c)), vi='Đường tròn tâm \\(I%s\\) tiếp xúc với đường thẳng \\(%s\\) có phương trình…' % (V2(I), leq(a, b, c)),
      opts=pick_opts(r, ceq(*I, R2), [ceq(*I, int(R)), ceq(-I[0], -I[1], R2), ceq(*I, D * D), ceq(*I, R2 + 1)]), ans=0,
      ee='\\(R=d(I,\\Delta)=%s\\).' % fr(R), ev='\\(R=d(I,\\Delta)=\\dfrac{%d}{%d}=%s\\Rightarrow R^2=%d\\).' % (D, s, fr(R), R2))


def c_wifi(r, lv):
    I = (r.randint(0, 4), r.randint(0, 4)); R = r.choice([3, 4, 5]); pts = []
    while len(pts) < 5:
        P = (r.randint(-2, 8), r.randint(-2, 8))
        if P not in pts and (P[0] - I[0]) ** 2 + (P[1] - I[1]) ** 2 != R * R: pts.append(P)
    n = sum((P[0] - I[0]) ** 2 + (P[1] - I[1]) ** 2 < R * R for P in pts)
    names = 'ABCDE'
    return dict(en='A Wi-Fi router at \\(I%s\\) covers the disc of radius %d (unit 10 m). Of the rooms \\(%s\\), how many are covered?' % (V2(I), R, ',\\ '.join('%s%s' % (names[i], V2(P)) for i, P in enumerate(pts))),
      vi='Bộ phát Wi-Fi đặt tại \\(I%s\\) phủ sóng hình tròn bán kính %d (đơn vị 10 m). Trong các phòng \\(%s\\), có bao nhiêu phòng được phủ sóng?' % (V2(I), R, ',\\ '.join('%s%s' % (names[i], V2(P)) for i, P in enumerate(pts))),
      opts=pick_opts(r, str(n), [str(k) for k in (n + 1, n - 1, n + 2, 5 - n, 0, 5) if 0 <= k <= 5]), ans=0,
      ee='A point is covered when \\(IP^2\\lt%d\\).' % (R * R), ev='Điểm \\(P\\) được phủ sóng khi \\(IP^2\\lt%d\\); các giá trị \\(IP^2\\): %s.' % (R * R, ', '.join(str((P[0] - I[0]) ** 2 + (P[1] - I[1]) ** 2) for P in pts)))


M21S10 = [c_center, c_general, c_write, c_diam, c_tangent, c_pos, c_tanR, c_wifi]


# ================= Bài 22. Ba đường conic =================
ELL = [(5, 4, 3), (5, 3, 4), (13, 12, 5), (13, 5, 12), (10, 8, 6), (10, 6, 8), (17, 15, 8), (17, 8, 15), (25, 24, 7), (15, 12, 9), (15, 9, 12)]
HYP = [(3, 4, 5), (4, 3, 5), (5, 12, 13), (12, 5, 13), (6, 8, 10), (8, 6, 10), (8, 15, 17), (15, 8, 17), (9, 12, 15), (12, 9, 15)]


def efrm(a2, b2): return '\\dfrac{x^2}{%d}+\\dfrac{y^2}{%d}=1' % (a2, b2)
def hfrm(a2, b2): return '\\dfrac{x^2}{%d}-\\dfrac{y^2}{%d}=1' % (a2, b2)


def e_axes(r, lv):
    a, b, c = r.choice(ELL)
    o = lambda p, q: TT('major axis \\(%d\\), minor axis \\(%d\\)' % (p, q), 'trục lớn \\(%d\\), trục nhỏ \\(%d\\)' % (p, q))
    return dict(en='The ellipse \\(%s\\) has…' % efrm(a * a, b * b), vi='Elip \\(%s\\) có độ dài…' % efrm(a * a, b * b),
      opts=pick_opts(r, o(2 * a, 2 * b), [o(a, b), o(2 * b, 2 * a), o(a * a, b * b), o(2 * a, 2 * c)]), ans=0,
      ee='\\(a=%d\\), \\(b=%d\\); axes \\(2a\\), \\(2b\\).' % (a, b), ev='\\(a=%d\\), \\(b=%d\\); trục lớn \\(2a=%d\\), trục nhỏ \\(2b=%d\\).' % (a, b, 2 * a, 2 * b))


def e_foci(r, lv):
    a, b, c = r.choice(ELL)
    return dict(en='The foci of the ellipse \\(%s\\) are…' % efrm(a * a, b * b), vi='Tiêu điểm của elip \\(%s\\) là…' % efrm(a * a, b * b),
      opts=pick_opts(r, 'F_{1,2}(\\pm%d;\\,0)' % c, ['F_{1,2}(\\pm%s;\\,0)' % rt(a * a + b * b), 'F_{1,2}(\\pm%d;\\,0)' % a, 'F_{1,2}(0;\\,\\pm%d)' % c, 'F_{1,2}(\\pm%d;\\,0)' % b]), ans=0,
      ee='\\(c^2=a^2-b^2=%d\\).' % (c * c), ev='Với elip: \\(c^2=a^2-b^2=%d-%d=%d\\Rightarrow c=%d\\).' % (a * a, b * b, c * c, c))


def e_write(r, lv):
    a, b, c = r.choice(ELL)
    return dict(en='An ellipse (standard form) has major axis \\(%d\\) and focal distance \\(F_1F_2=%d\\). Its equation is…' % (2 * a, 2 * c), vi='Elip (dạng chính tắc) có độ dài trục lớn \\(%d\\) và tiêu cự \\(%d\\). Phương trình của elip là…' % (2 * a, 2 * c),
      opts=pick_opts(r, efrm(a * a, b * b), [efrm(a * a, c * c), efrm(4 * a * a, 4 * b * b), hfrm(a * a, b * b), efrm(a * a, a * a + c * c)]), ans=0,
      ee='\\(a=%d\\), \\(c=%d\\), \\(b^2=a^2-c^2=%d\\).' % (a, c, b * b), ev='\\(a=%d\\), \\(c=%d\\), \\(b^2=a^2-c^2=%d\\).' % (a, c, b * b))


def e_sum(r, lv):
    a, b, c = r.choice(ELL)
    return dict(en='\\(M\\) lies on the ellipse \\(%s\\) with foci \\(F_1\\), \\(F_2\\). Then \\(MF_1+MF_2=\\)…' % efrm(a * a, b * b), vi='Điểm \\(M\\) thuộc elip \\(%s\\) có hai tiêu điểm \\(F_1\\), \\(F_2\\). Khi đó \\(MF_1+MF_2=\\)…' % efrm(a * a, b * b),
      opts=pick_opts(r, str(2 * a), [str(a), str(2 * b), str(2 * c), str(a * a)]), ans=0, ee='\\(MF_1+MF_2=2a\\).', ev='Theo định nghĩa elip: \\(MF_1+MF_2=2a=%d\\).' % (2 * a))


def h_foci(r, lv):
    a, b, c = r.choice(HYP)
    return dict(en='The foci of the hyperbola \\(%s\\) are…' % hfrm(a * a, b * b), vi='Tiêu điểm của hypebol \\(%s\\) là…' % hfrm(a * a, b * b),
      opts=pick_opts(r, 'F_{1,2}(\\pm%d;\\,0)' % c, ['F_{1,2}(\\pm%s;\\,0)' % rt(abs(a * a - b * b)), 'F_{1,2}(\\pm%d;\\,0)' % a, 'F_{1,2}(0;\\,\\pm%d)' % c, 'F_{1,2}(\\pm%d;\\,0)' % b]), ans=0,
      ee='For a hyperbola \\(c^2=a^2+b^2\\).', ev='Với hypebol: \\(c^2=a^2+b^2=%d\\Rightarrow c=%d\\).' % (c * c, c))


def h_asym(r, lv):
    a, b, c = r.choice(HYP); k = F(b, a)
    return dict(en='The asymptotes of the hyperbola \\(%s\\) are…' % hfrm(a * a, b * b), vi='Hai đường tiệm cận của hypebol \\(%s\\) là…' % hfrm(a * a, b * b),
      opts=pick_opts(r, 'y=\\pm%sx' % fr(k), ['y=\\pm%sx' % fr(1 / k), 'y=\\pm%sx' % fr(F(b * b, a * a)), 'y=\\pm%sx' % fr(F(c, a)), 'y=\\pm%sx' % fr(F(b, c))]), ans=0,
      ee='\\(y=\\pm\\dfrac bax\\).', ev='Tiệm cận của hypebol: \\(y=\\pm\\dfrac bax=\\pm%sx\\).' % fr(k))


def h_diff(r, lv):
    a, b, c = r.choice(HYP)
    return dict(en='\\(M\\) lies on the hyperbola \\(%s\\). Then \\(|MF_1-MF_2|=\\)…' % hfrm(a * a, b * b), vi='Điểm \\(M\\) thuộc hypebol \\(%s\\). Khi đó \\(|MF_1-MF_2|=\\)…' % hfrm(a * a, b * b),
      opts=pick_opts(r, str(2 * a), [str(a), str(2 * b), str(2 * c), str(a + b)]), ans=0, ee='\\(|MF_1-MF_2|=2a\\).', ev='Theo định nghĩa hypebol: \\(|MF_1-MF_2|=2a=%d\\).' % (2 * a))


def p_focus(r, lv):
    p = r.choice([1, 2, 3, 4, 6, 8, F(1, 2), F(3, 2), 5]); q = 2 * p
    return dict(en='The focus and directrix of the parabola \\(y^2=%sx\\) are…' % fr(q), vi='Tiêu điểm và đường chuẩn của parabol \\(y^2=%sx\\) là…' % fr(q),
      opts=pick_opts(r, 'F(%s;0),\\ \\Delta: x=-%s' % (fr(p / 2), fr(p / 2)), ['F(%s;0),\\ \\Delta: x=-%s' % (fr(p), fr(p)), 'F(%s;0),\\ \\Delta: x=-%s' % (fr(q), fr(q)), 'F(-%s;0),\\ \\Delta: x=%s' % (fr(p / 2), fr(p / 2)), 'F(0;%s),\\ \\Delta: y=-%s' % (fr(p / 2), fr(p / 2))]), ans=0,
      ee='\\(y^2=2px\\) with \\(p=%s\\): \\(F(\\tfrac p2;0)\\), \\(x=-\\tfrac p2\\).' % fr(p), ev='\\(y^2=2px\\) với \\(p=%s\\): tiêu điểm \\(F\\left(\\tfrac p2;0\\right)\\), đường chuẩn \\(x=-\\tfrac p2\\).' % fr(p))


def p_dist(r, lv):
    p = r.choice([2, 4, 6, 8, 1, 3]); x0 = r.choice([1, 2, 3, 4, 5, 8]); y2 = 2 * p * x0
    return dict(en='\\(M\\) on the parabola \\(y^2=%dx\\) has \\(x_M=%d\\). Its distance to the focus is…' % (2 * p, x0), vi='Điểm \\(M\\) thuộc parabol \\(y^2=%dx\\) có hoành độ \\(%d\\). Khoảng cách từ \\(M\\) đến tiêu điểm là…' % (2 * p, x0),
      opts=pick_opts(r, fr(x0 + F(p, 2)), [fr(x0 + p), fr(x0 - F(p, 2)) if x0 * 2 != p else fr(x0 + 2 * p), fr(F(p, 2)), rt(y2)]), ans=0,
      ee='\\(MF=d(M,\\Delta)=x_M+\\dfrac p2\\).', ev='\\(MF=d(M,\\Delta)=x_M+\\dfrac p2=%d+%s\\).' % (x0, fr(F(p, 2))))


def k_type(r, lv):
    kind = r.randrange(3); a, b, c = r.choice(ELL)
    eqs = [efrm(a * a, b * b), hfrm(a * a, b * b), 'y^2=%dx' % (2 * r.choice([1, 2, 3, 5]))]
    names = [('ellipse', 'đường elip'), ('hyperbola', 'đường hypebol'), ('parabola', 'đường parabol'), ('circle', 'đường tròn')]
    return dict(en='The curve \\(%s\\) is…' % eqs[kind], vi='Đường cong \\(%s\\) là…' % eqs[kind], opts=[TT(*names[kind])] + [TT(*names[j]) for j in range(4) if j != kind], ans=0,
      ee='Compare with the three standard forms.', ev='So sánh với ba dạng chính tắc: \\(\\frac{x^2}{a^2}+\\frac{y^2}{b^2}=1\\) (elip), \\(\\frac{x^2}{a^2}-\\frac{y^2}{b^2}=1\\) (hypebol), \\(y^2=2px\\) (parabol).')


def p_dish(r, lv):
    D, h = r.choice([(80, 10), (60, 5), (120, 15), (100, 20), (40, 4), (160, 20)])   # đường kính, độ sâu (cm)
    p2 = F((D // 2) ** 2, h)            # y² = 2p·x, qua (h; D/2)  → 2p = (D/2)²/h ; tiêu điểm x = p/2 = 2p/4
    f = p2 / 4
    return dict(en='A satellite dish has a parabolic cross-section: diameter %d cm, depth %d cm. Its receiver must be at the focus, at distance … from the vertex.' % (D, h), vi='Một chảo ăng-ten có thiết diện là parabol: đường kính miệng %d cm, độ sâu %d cm. Đầu thu đặt tại tiêu điểm, cách đỉnh chảo…' % (D, h),
      opts=pick_opts(r, '%s\\text{ cm}' % fr(f), ['%s\\text{ cm}' % fr(p2), '%s\\text{ cm}' % fr(p2 / 2), '%s\\text{ cm}' % fr(F(D, 2)), '%s\\text{ cm}' % fr(f + h)]), ans=0,
      ee='\\(y^2=2px\\) through \\((%d;%d)\\): \\(2p=%s\\); focus at \\(\\tfrac p2\\).' % (h, D // 2, fr(p2)), ev='\\(y^2=2px\\) đi qua \\((%d;%d)\\) nên \\(2p=\\dfrac{%d}{%d}=%s\\); tiêu điểm cách đỉnh \\(\\dfrac p2=%s\\) cm.' % (h, D // 2, (D // 2) ** 2, h, fr(p2), fr(f)))


M22S10 = [e_axes, e_foci, e_write, e_sum, h_foci, h_asym, h_diff, p_focus, p_dist, k_type, p_dish]
