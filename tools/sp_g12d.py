# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 12 – Bài 13 (ứng dụng hình học của tích phân), Bài 14 (phương trình mặt phẳng). Đáp án tính chính xác (Fraction, số nguyên)."""
import math
from fractions import Fraction as F
from mb_selfpractice import pick_opts, fr
from mb_lib import TI

def TT(en, vi): return '§' + TI(en, vi)
def pi(c):
    """c·π dưới dạng TeX."""
    c = F(c)
    if c == 0: return '0'
    if c == 1: return '\\pi'
    if c.denominator == 1: return '%d\\pi' % c.numerator
    return '\\dfrac{%s\\pi}{%d}' % ('' if c.numerator == 1 else c.numerator, c.denominator)
# ================= Bài 13 =================
def ap_par(r, lv):
    k = r.choice([1, 2, 3, 4, 6]); v = F(k ** 3, 6)
    f = '-x^2+%sx' % ('' if k == 1 else k)
    return dict(en='The area of the region bounded by \\(y=%s\\) and the \\(x\\)-axis is…' % f, vi='Diện tích hình phẳng giới hạn bởi \\(y=%s\\) và trục hoành là…' % f,
      opts=pick_opts(r, fr(v), [fr(F(k ** 3, 3)), fr(F(k ** 2, 2)), fr(-v), fr(F(k ** 3, 2))]), ans=0,
      ee='Roots \\(0\\), \\(%d\\); \\(S=\\int_0^{%d}(-x^2+%dx)\\,dx=\\dfrac{%d^3}{6}=%s\\).' % (k, k, k, k, fr(v)), ev='Nghiệm \\(0\\), \\(%d\\); \\(S=\\int_0^{%d}(-x^2+%dx)\\,dx=\\dfrac{%d^3}{6}=%s\\).' % (k, k, k, k, fr(v)))
def ap_two(r, lv):
    m = r.choice([1, 2, 3, 4, 6]); v = F(m ** 3, 6); g = 'x' if m == 1 else '%dx' % m
    return dict(en='The area between \\(y=x^2\\) and \\(y=%s\\) is…' % g, vi='Diện tích hình phẳng giới hạn bởi \\(y=x^2\\) và \\(y=%s\\) là…' % g,
      opts=pick_opts(r, fr(v), [fr(F(m ** 3, 3)), fr(F(m ** 3, 2)), fr(F(m ** 2, 2)), fr(F(m ** 3, 12))]), ans=0,
      ee='Intersections \\(x=0\\), \\(x=%d\\); \\(S=\\int_0^{%d}(%s-x^2)\\,dx=%s\\).' % (m, m, g, fr(v)), ev='Giao điểm \\(x=0\\), \\(x=%d\\); \\(S=\\int_0^{%d}(%s-x^2)\\,dx=%s\\).' % (m, m, g, fr(v)))
def ap_abs(r, lv):
    a = r.choice([1, 2, 3]); v = F(4 * a ** 3, 3)
    return dict(en='The area bounded by \\(y=x^2-%d\\), the \\(x\\)-axis, \\(x=-%d\\) and \\(x=%d\\) is…' % (a * a, a, a), vi='Diện tích hình phẳng giới hạn bởi \\(y=x^2-%d\\), trục hoành, \\(x=-%d\\), \\(x=%d\\) là…' % (a * a, a, a),
      opts=pick_opts(r, fr(v), [fr(-v), fr(F(2 * a ** 3, 3)), fr(F(8 * a ** 3, 3)), fr(2 * a ** 3)]), ans=0,
      ee='\\(x^2-%d\\le0\\) on \\([-%d;%d]\\): \\(S=\\int_{-%d}^{%d}(%d-x^2)\\,dx=%s\\).' % (a * a, a, a, a, a, a * a, fr(v)), ev='\\(x^2-%d\\le0\\) trên \\([-%d;%d]\\): \\(S=\\int_{-%d}^{%d}(%d-x^2)\\,dx=%s\\).' % (a * a, a, a, a, a, a * a, fr(v)))
def ap_cubic(r, lv):
    a = r.choice([1, 2, 3]); v = F(a ** 4, 2)    # y = x^3 - a^2 x trên [-a;a]
    return dict(en='The area bounded by \\(y=x^3-%sx\\) and the \\(x\\)-axis is…' % ('' if a == 1 else a * a), vi='Diện tích hình phẳng giới hạn bởi \\(y=x^3-%sx\\) và trục hoành là…' % ('' if a == 1 else a * a),
      opts=pick_opts(r, fr(v), ['0', fr(F(a ** 4, 4)), fr(a ** 4), fr(2 * a ** 4)]), ans=0,
      ee='Roots \\(-%d,0,%d\\); the function changes sign at 0, so \\(S=2\\int_0^{%d}(%dx-x^3)\\,dx=%s\\) (not \\(\\int_{-%d}^{%d}=0\\)).' % (a, a, a, a * a, fr(v), a, a), ev='Nghiệm \\(-%d,0,%d\\); hàm đổi dấu tại 0 nên \\(S=2\\int_0^{%d}(%dx-x^3)\\,dx=%s\\) (không phải \\(\\int_{-%d}^{%d}=0\\)).' % (a, a, a, a * a, fr(v), a, a))
def vr_lin(r, lv):
    k = r.choice([1, 2, 3, F(1, 2)]); h = r.choice([1, 2, 3, 4]); v = F(k) ** 2 * h ** 3 / 3
    f = 'x' if k == 1 else ('%sx' % fr(F(k)) if F(k).denominator == 1 else '\\frac12x')
    return dict(en='Rotating the region under \\(y=%s\\), \\(0\\le x\\le%d\\), about the \\(x\\)-axis gives a cone of volume…' % (f, h), vi='Quay hình phẳng giới hạn bởi \\(y=%s\\), trục hoành, \\(x=%d\\) quanh trục \\(Ox\\) được khối nón có thể tích…' % (f, h),
      opts=pick_opts(r, pi(v), [pi(3 * v), pi(v * 3 / 2), fr(v), pi(v / 2)]), ans=0,
      ee='\\(V=\\pi\\int_0^{%d}(%s)^2dx=%s\\).' % (h, f, pi(v)), ev='\\(V=\\pi\\int_0^{%d}(%s)^2dx=%s\\).' % (h, f, pi(v)))
def vr_sqrt(r, lv):
    a = r.choice([1, 2, 3, 4, 6]); v = F(a * a, 2)
    return dict(en='The volume obtained by rotating the region under \\(y=\\sqrt x\\), \\(0\\le x\\le%d\\), about \\(Ox\\) is…' % a, vi='Thể tích khối tròn xoay khi quay hình phẳng giới hạn bởi \\(y=\\sqrt x\\), trục hoành, \\(x=%d\\) quanh \\(Ox\\) là…' % a,
      opts=pick_opts(r, pi(v), [pi(F(2 * a ** 3, 3) if a else 1), fr(v), pi(a * a), pi(F(2, 3) * a)]), ans=0,
      ee='\\(V=\\pi\\int_0^{%d}x\\,dx=%s\\).' % (a, pi(v)), ev='\\(V=\\pi\\int_0^{%d}x\\,dx=%s\\).' % (a, pi(v)))
def vr_par(r, lv):
    a = r.choice([1, 2, 3]); v = F(a ** 5, 5)
    return dict(en='Rotating the region under \\(y=x^2\\), \\(0\\le x\\le%d\\), about \\(Ox\\) gives the volume…' % a, vi='Quay hình phẳng giới hạn bởi \\(y=x^2\\), trục hoành, \\(x=%d\\) quanh \\(Ox\\), thể tích khối tròn xoay là…' % a,
      opts=pick_opts(r, pi(v), [pi(F(a ** 3, 3)), fr(F(a ** 3, 3)), pi(F(a ** 4, 4)), fr(v)]), ans=0,
      ee='\\(V=\\pi\\int_0^{%d}x^4dx=%s\\).' % (a, pi(v)), ev='\\(V=\\pi\\int_0^{%d}x^4dx=%s\\).' % (a, pi(v)))
def vs_cross(r, lv):
    a, b = r.choice([(2, 1), (3, 0), (1, 2), (4, 1)]); L = r.choice([2, 3, 4]); v = F(a * L * L, 2) + b * L
    return dict(en='A solid lies between the planes \\(x=0\\) and \\(x=%d\\). Its cross-section at \\(x\\) has area \\(S(x)=%s\\). Its volume is…' % (L, ('%dx' % a if a != 1 else 'x') + ('+%d' % b if b else '')),
      vi='Một vật thể nằm giữa hai mặt phẳng \\(x=0\\) và \\(x=%d\\); thiết diện tại \\(x\\) có diện tích \\(S(x)=%s\\). Thể tích vật thể là…' % (L, ('%dx' % a if a != 1 else 'x') + ('+%d' % b if b else '')),
      opts=pick_opts(r, fr(v), [fr(a * L + b), fr(a * L * L + b * L), pi(v), fr(v + L)]), ans=0, ee='\\(V=\\int_0^{%d}S(x)\\,dx=%s\\).' % (L, fr(v)), ev='\\(V=\\int_0^{%d}S(x)\\,dx=%s\\).' % (L, fr(v)))
def ap_gate(r, lv):
    w, h = r.choice([(4, 3), (6, 4), (3, 2), (8, 6), (5, 3)]); v = F(2 * w * h, 3)
    return dict(en='A gate has the shape of a parabola arch, width \\(%d\\) m at the ground and height \\(%d\\) m. Its area is…' % (w, h), vi='Một cổng có dạng parabol, bề rộng chân cổng \\(%d\\) m, chiều cao \\(%d\\) m. Diện tích cổng là…' % (w, h),
      opts=pick_opts(r, fr(v) + '\\ \\text{m}^2', [fr(w * h) + '\\ \\text{m}^2', fr(F(w * h, 2)) + '\\ \\text{m}^2', fr(F(w * h, 3)) + '\\ \\text{m}^2', fr(F(4 * w * h, 3)) + '\\ \\text{m}^2']), ans=0,
      ee='Put the arch as \\(y=%d-\\dfrac{%d}{%s}x^2\\) on \\(\\left[-%s;%s\\right]\\); the integral gives \\(\\dfrac23\\cdot%d\\cdot%d=%s\\).' % (h, h, fr(F(w * w, 4)), fr(F(w, 2)), fr(F(w, 2)), w, h, fr(v)),
      ev='Đặt cổng là \\(y=%d-\\dfrac{%d}{%s}x^2\\) trên \\(\\left[-%s;%s\\right]\\); tích phân cho \\(\\dfrac23\\cdot%d\\cdot%d=%s\\).' % (h, h, fr(F(w * w, 4)), fr(F(w, 2)), fr(F(w, 2)), w, h, fr(v)))
M13S12 = [ap_par, ap_two, ap_abs, ap_cubic, vr_lin, vr_sqrt, vs_cross, ap_gate]
# ================= Bài 14 =================
def eq(A, B, C, Dd):
    s = ''
    for c, v in ((A, 'x'), (B, 'y'), (C, 'z')):
        if c == 0: continue
        sg = '-' if c < 0 else ('+' if s else ''); a = abs(c); s += sg + ('' if a == 1 else str(a)) + v
    if Dd: s += ('+' if Dd > 0 else '-') + str(abs(Dd))
    return s + '=0'
def V3(v): return '(%s)' % ';\\,'.join(fr(F(x)) for x in v)
def cross(u, v): return (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])
def dot(u, v): return sum(a * b for a, b in zip(u, v))
def sub(u, v): return tuple(a - b for a, b in zip(u, v))
def _n(r):
    n = (r.randint(-4, 4), r.randint(-4, 4), r.randint(-4, 4))
    if n == (0, 0, 0): raise AssertionError
    return n
def _p(r): return (r.randint(-3, 4), r.randint(-3, 4), r.randint(-3, 4))
def pl_pn(r, lv):
    n, M = _n(r), _p(r); Dd = -dot(n, M)
    return dict(en='The plane through \\(M%s\\) with normal vector \\(\\vec n=%s\\) is…' % (V3(M), V3(n)), vi='Mặt phẳng đi qua \\(M%s\\) và có vectơ pháp tuyến \\(\\vec n=%s\\) có phương trình…' % (V3(M), V3(n)),
      opts=pick_opts(r, eq(*n, Dd), [eq(*n, -Dd) if Dd else eq(*n, 1), eq(*M, -dot(n, M)) if M != n and any(M) else eq(n[0], n[1], -n[2] if n[2] else 1, Dd), eq(n[0], n[1], n[2], Dd + 1)]), ans=0,
      ee='\\(%d(x%+d)%+d(y%+d)%+d(z%+d)=0\\iff %s\\).' % (n[0], -M[0], n[1], -M[1], n[2], -M[2], eq(*n, Dd)), ev='\\(%d(x%+d)%+d(y%+d)%+d(z%+d)=0\\iff %s\\).' % (n[0], -M[0], n[1], -M[1], n[2], -M[2], eq(*n, Dd)))
def pl_read(r, lv):
    n = _n(r); Dd = r.randint(-6, 6); k = r.choice([2, -1, 3])
    return dict(en='A normal vector of the plane \\(%s\\) is…' % eq(*n, Dd), vi='Một vectơ pháp tuyến của mặt phẳng \\(%s\\) là…' % eq(*n, Dd),
      opts=pick_opts(r, V3(tuple(k * x for x in n)), [V3((n[0], n[1], Dd)), V3((n[1], n[0], n[2])) if n[0] != n[1] else V3((n[0], -n[1] if n[1] else 1, n[2])), V3((n[0], n[1], -n[2])) if n[2] else V3((n[0], n[1], 1)), V3((Dd, n[1], n[2]))]), ans=0,
      ee='\\(\\vec n=(A;B;C)=%s\\); any non-zero multiple, e.g. \\(%s\\), is also a normal vector.' % (V3(n), V3(tuple(k * x for x in n))), ev='\\(\\vec n=(A;B;C)=%s\\); mọi vectơ \\(k\\vec n\\) (\\(k\\ne0\\)), ví dụ \\(%s\\), cũng là vectơ pháp tuyến.' % (V3(n), V3(tuple(k * x for x in n))))
def pl_cross(r, lv):
    u, v = _n(r), _n(r); w = cross(u, v)
    if w == (0, 0, 0): raise AssertionError
    return dict(en='\\(\\vec u=%s\\), \\(\\vec v=%s\\). The vector \\([\\vec u,\\vec v]\\) is…' % (V3(u), V3(v)), vi='Cho \\(\\vec u=%s\\), \\(\\vec v=%s\\). Tích có hướng \\([\\vec u,\\vec v]\\) là…' % (V3(u), V3(v)),
      opts=pick_opts(r, V3(w), [V3(tuple(-x for x in w)), V3((w[0], -w[1], w[2])) if w[1] else V3((w[0], 1, w[2])), V3(tuple(a * b for a, b in zip(u, v)))]), ans=0,
      ee='\\([\\vec u,\\vec v]=\\left(\\begin{vmatrix}%d&%d\\\\%d&%d\\end{vmatrix};\\begin{vmatrix}%d&%d\\\\%d&%d\\end{vmatrix};\\begin{vmatrix}%d&%d\\\\%d&%d\\end{vmatrix}\\right)=%s\\).' % (u[1], u[2], v[1], v[2], u[2], u[0], v[2], v[0], u[0], u[1], v[0], v[1], V3(w)),
      ev='\\([\\vec u,\\vec v]=\\left(\\begin{vmatrix}%d&%d\\\\%d&%d\\end{vmatrix};\\begin{vmatrix}%d&%d\\\\%d&%d\\end{vmatrix};\\begin{vmatrix}%d&%d\\\\%d&%d\\end{vmatrix}\\right)=%s\\).' % (u[1], u[2], v[1], v[2], u[2], u[0], v[2], v[0], u[0], u[1], v[0], v[1], V3(w)))
def pl_int(r, lv):
    a, b, c = (r.choice([1, 2, 3, -2, 4, -1]) for _ in range(3))
    A, B, C, Dd = b * c, a * c, a * b, -a * b * c; g = math.gcd(math.gcd(abs(A), abs(B)), math.gcd(abs(C), abs(Dd)))
    A, B, C, Dd = A // g, B // g, C // g, Dd // g
    return dict(en='The plane through \\(A(%d;0;0)\\), \\(B(0;%d;0)\\), \\(C(0;0;%d)\\) is…' % (a, b, c), vi='Mặt phẳng đi qua \\(A(%d;0;0)\\), \\(B(0;%d;0)\\), \\(C(0;0;%d)\\) có phương trình…' % (a, b, c),
      opts=pick_opts(r, '\\dfrac{x}{%d}+\\dfrac{y}{%d}+\\dfrac{z}{%d}=1' % (a, b, c), ['%dx+%dy+%dz=1' % (a, b, c), '\\dfrac{x}{%d}+\\dfrac{y}{%d}+\\dfrac{z}{%d}=0' % (a, b, c), '\\dfrac{x}{%d}+\\dfrac{y}{%d}+\\dfrac{z}{%d}=1' % (-a, b, c)]), ans=0,
      ee='Intercept form: \\(\\dfrac xa+\\dfrac yb+\\dfrac zc=1\\), i.e. \\(%s\\).' % eq(A, B, C, Dd), ev='Phương trình theo đoạn chắn: \\(\\dfrac xa+\\dfrac yb+\\dfrac zc=1\\), tức \\(%s\\).' % eq(A, B, C, Dd))
TRIP = [(1, 2, 2, 3), (2, 1, 2, 3), (2, 2, 1, 3), (1, 4, 8, 9), (2, 3, 6, 7), (4, 4, 2, 6), (0, 3, 4, 5), (6, 2, 3, 7)]
def pl_dist(r, lv):
    A, B, C, Ln = r.choice(TRIP); s = [r.choice([1, -1]) for _ in range(3)]; A, B, C = A * s[0], B * s[1], C * s[2]
    M = _p(r); k = r.randint(1, 4) * r.choice([1, -1]); Dd = k * Ln - (A * M[0] + B * M[1] + C * M[2]); d = abs(k)
    return dict(en='The distance from \\(M%s\\) to the plane \\(%s\\) is…' % (V3(M), eq(A, B, C, Dd)), vi='Khoảng cách từ \\(M%s\\) đến mặt phẳng \\(%s\\) bằng…' % (V3(M), eq(A, B, C, Dd)),
      opts=pick_opts(r, str(d), [str(abs(k * Ln)), fr(F(abs(k * Ln), Ln * Ln)), str(d + 1), str(abs(Dd)) if abs(Dd) != d else str(d + 2)]), ans=0,
      ee='\\(d=\\dfrac{|%d|}{\\sqrt{%d}}=\\dfrac{%d}{%d}=%d\\).' % (k * Ln, Ln * Ln, abs(k * Ln), Ln, d), ev='\\(d=\\dfrac{|%d|}{\\sqrt{%d}}=\\dfrac{%d}{%d}=%d\\).' % (k * Ln, Ln * Ln, abs(k * Ln), Ln, d))
def pl_par(r, lv):
    n = (r.choice([1, 2, 3]), r.choice([-1, 2, -3]), r.choice([1, 2, 4])); k = r.choice([2, 3, -1, -2]); i = r.randrange(3)
    m = n[i] * k; shown = list(k * x for x in n); lab = ['A', 'B', 'C'][i]; shown_s = ['m' if j == i else str(shown[j]) for j in range(3)]
    q = ''
    for j, v in enumerate('xyz'):
        if j == i: q += ('+' if q else '') + 'm' + v; continue
        c = shown[j]; q += ('-' if c < 0 else ('+' if q else '')) + ('' if abs(c) == 1 else str(abs(c))) + v
    q += '+5=0'
    return dict(en='\\((P): %s\\) and \\((Q): %s\\). \\((P)\\parallel(Q)\\) when \\(m=\\)…' % (eq(*n, 1), q), vi='Cho \\((P): %s\\) và \\((Q): %s\\). \\((P)\\parallel(Q)\\) khi \\(m=\\)…' % (eq(*n, 1), q),
      opts=pick_opts(r, str(m), [str(-m), str(n[i]), str(m + 1), str(k)]), ans=0,
      ee='The normal vectors must be proportional with ratio \\(%d\\): \\(m=%d\\cdot%d=%d\\) (and \\(5\\ne%d\\cdot1\\)).' % (k, k, n[i], m, k), ev='Hai vectơ pháp tuyến phải cùng phương với tỉ số \\(%d\\): \\(m=%d\\cdot%d=%d\\) (và \\(5\\ne%d\\cdot1\\)).' % (k, k, n[i], m, k))
def pl_perp(r, lv):
    n1 = (r.choice([1, 2, 3]), r.choice([-1, 2, 1]), r.choice([1, -2, 3])); b, c = r.randint(-3, 3), r.randint(-3, 3); t = -(n1[1] * b + n1[2] * c)
    if t % n1[0]: raise AssertionError
    m = t // n1[0]
    tm = lambda k, v: '' if k == 0 else ('+' if k > 0 else '-') + ('' if abs(k) == 1 else str(abs(k))) + v
    q = 'mx' + tm(b, 'y') + tm(c, 'z') + '-1=0'
    return dict(en='\\((P): %s\\), \\((Q): %s\\). \\((P)\\perp(Q)\\) when \\(m=\\)…' % (eq(*n1, -2), q), vi='Cho \\((P): %s\\), \\((Q): %s\\). \\((P)\\perp(Q)\\) khi \\(m=\\)…' % (eq(*n1, -2), q),
      opts=pick_opts(r, str(m), [str(-m) if m else '1', str(m + 1), str(m - 2), str(n1[0])]), ans=0,
      ee='\\(\\vec n_1\\cdot\\vec n_2=%dm%+d=0\\Rightarrow m=%d\\).' % (n1[0], -t, m), ev='\\(\\vec n_1\\cdot\\vec n_2=%dm%+d=0\\Rightarrow m=%d\\).' % (n1[0], -t, m))
def pl_on(r, lv):
    n = _n(r); M = _p(r); Dd = -dot(n, M); others = []
    for _ in range(20):
        P = _p(r)
        if dot(n, P) + Dd != 0 and V3(P) not in others: others.append(V3(P))
    return dict(en='Which point lies on the plane \\(%s\\)?' % eq(*n, Dd), vi='Điểm nào thuộc mặt phẳng \\(%s\\)?' % eq(*n, Dd), opts=pick_opts(r, V3(M), others[:3]), ans=0,
      ee='Substitute: \\(%d\\cdot%d%+d\\cdot%d%+d\\cdot%d%+d=0\\).' % (n[0], M[0], n[1], M[1], n[2], M[2], Dd), ev='Thay tọa độ: \\(%d\\cdot%d%+d\\cdot%d%+d\\cdot%d%+d=0\\).' % (n[0], M[0], n[1], M[1], n[2], M[2], Dd))
M14S12 = [pl_pn, pl_read, pl_cross, pl_int, pl_dist, pl_par, pl_perp, pl_on]
