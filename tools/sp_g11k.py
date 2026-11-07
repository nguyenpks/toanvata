# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 11 – Bài 31 (định nghĩa, ý nghĩa đạo hàm), Bài 32 (quy tắc tính đạo hàm), Bài 33 (đạo hàm cấp hai).
Đáp án tính chính xác bằng số nguyên/Fraction."""
import math
from fractions import Fraction as F
from mb_selfpractice import pick_opts, fr
from mb_selfpractice import poly
from sp_g11f import TT


def nz(r, lo, hi):
    while True:
        v = r.randint(lo, hi)
        if v: return v
def fx(c): return 'f(x)=' + poly(c)
def lin(m, b):
    return 'y=' + poly([m, b]) if m else 'y=%d' % b
def ev(c, x): return sum(a * x ** (len(c) - 1 - i) for i, a in enumerate(c))
def der(c):
    n = len(c) - 1
    return [a * (n - i) for i, a in enumerate(c[:-1])] or [0]


# ================= Bài 31 =================
def d_def(r, lv):
    a, b, c = nz(r, -3, 3), r.randint(-5, 5), r.randint(-5, 5); x0 = nz(r, -3, 3)
    v = 2 * a * x0 + b
    return dict(en='For \\(%s\\), using the definition, \\(f\'(%d)=\\)…' % (fx([a, b, c]), x0), vi='Cho \\(%s\\). Theo định nghĩa, \\(f\'(%d)=\\)…' % (fx([a, b, c]), x0),
      opts=pick_opts(r, str(v), [str(a * x0 + b), str(ev([a, b, c], x0)), str(2 * a * x0), str(-v), str(v + 2 * a)]), ans=0,
      ee='\\(\\lim\\limits_{h\\to0}\\dfrac{f(%d+h)-f(%d)}{h}=2a x_0+b\\).' % (x0, x0), ev='\\(\\dfrac{f(x_0+h)-f(x_0)}{h}=2ax_0+b+ah\\to 2\\cdot%d\\cdot%d+%d\\) khi \\(h\\to0\\).' % (a, x0, b))


def d_slope(r, lv):
    k = r.choice([2, 3]); x0 = nz(r, -3, 3); s = k * x0 ** (k - 1)
    return dict(en='The slope of the tangent to \\(y=x^%d\\) at the point with abscissa \\(%d\\) is…' % (k, x0), vi='Hệ số góc của tiếp tuyến của đồ thị \\(y=x^%d\\) tại điểm có hoành độ \\(%d\\) là…' % (k, x0),
      opts=pick_opts(r, str(s), [str(x0 ** k), str(k * x0), str(-s), str(s + 1), str(x0 ** (k - 1))]), ans=0, ee='\\((x^%d)\'=%dx^{%d}\\).' % (k, k, k - 1), ev='Hệ số góc bằng \\(f\'(x_0)\\) với \\((x^%d)\'=%s\\).' % (k, '2x' if k == 2 else '3x^2'))


def d_tan(r, lv):
    x0 = nz(r, -3, 3); m, b = 2 * x0, -x0 * x0
    return dict(en='The tangent to the parabola \\(y=x^2\\) at the point \\((%d;%d)\\) is…' % (x0, x0 * x0), vi='Tiếp tuyến của parabol \\(y=x^2\\) tại điểm \\((%d;%d)\\) có phương trình là…' % (x0, x0 * x0),
      opts=pick_opts(r, lin(m, b), [lin(m, -b), lin(x0, 0), lin(m, x0 * x0), lin(-m, b)]), ans=0,
      ee='\\(y=f\'(x_0)(x-x_0)+f(x_0)\\).', ev='\\(y=%d(x-(%d))+%d\\).' % (m, x0, x0 * x0))


def d_vel(r, lv):
    a = r.choice([2, 3, 4, 5]); b = r.randint(1, 10); t0 = r.randint(1, 6)
    return dict(en='A car moves with \\(s(t)=%s\\) (metres, seconds). Its instantaneous velocity at \\(t=%d\\) is… (m/s)' % (poly([a, b, 0], 't'), t0), vi='Một ô tô chuyển động theo phương trình \\(s(t)=%s\\) (\\(s\\) tính bằng mét, \\(t\\) bằng giây). Vận tốc tức thời tại \\(t=%d\\) là… (m/s)' % (poly([a, b, 0], 't'), t0),
      opts=pick_opts(r, str(2 * a * t0 + b), [str(a * t0 * t0 + b * t0), str(a * t0 + b), str(2 * a * t0), str(a * t0 + b * t0)]), ans=0,
      ee='\\(v(t)=s\'(t)\\).', ev='\\(v(t)=s\'(t)=%s\\), thay \\(t=%d\\).' % (poly([2 * a, b], 't'), t0))


def d_avg(r, lv):
    x1 = r.randint(-3, 2); x2 = x1 + r.randint(1, 4)
    return dict(en='The average rate of change of \\(f(x)=x^2\\) on \\([%d;%d]\\) is…' % (x1, x2), vi='Tốc độ thay đổi trung bình của \\(f(x)=x^2\\) trên đoạn \\([%d;%d]\\) là…' % (x1, x2),
      opts=pick_opts(r, str(x1 + x2), [str(x2 * x2 - x1 * x1), str(2 * x2), str(2 * x1), str(x2 - x1), str(x1 + x2 + 1)]), ans=0,
      ee='\\(\\dfrac{f(x_2)-f(x_1)}{x_2-x_1}\\).', ev='\\(\\dfrac{%d-%d}{%d-(%d)}\\) (hệ số góc của cát tuyến).' % (x2 * x2, x1 * x1, x2, x1))


def d_inv(r, lv):
    x0 = r.choice([2, 3, 4, -2, -3]); v = F(-1, x0 * x0)
    return dict(en='For \\(f(x)=\\dfrac1x\\), \\(f\'(%d)=\\)…' % x0, vi='Cho \\(f(x)=\\dfrac1x\\). Khi đó \\(f\'(%d)=\\)…' % x0,
      opts=pick_opts(r, fr(v), [fr(-v), fr(F(1, x0)), fr(F(-1, x0)), fr(F(-2, x0 ** 3))]), ans=0,
      ee='\\(\\dfrac{f(x_0+h)-f(x_0)}{h}=\\dfrac{-1}{x_0(x_0+h)}\\).', ev='\\(\\dfrac{f(x_0+h)-f(x_0)}{h}=\\dfrac{-1}{x_0(x_0+h)}\\to-\\dfrac1{x_0^2}\\).')


def d_cost(r, lv):
    a = r.choice([F(1, 10), F(1, 5), F(1, 2)]); b = r.choice([20, 30, 50]); x0 = r.choice([10, 20, 50])
    v = 2 * a * x0 + b
    return dict(en='The cost of producing \\(x\\) items is \\(C(x)=%s\\,x^2+%dx+500\\) (thousand đồng). The marginal cost \\(C\'(%d)\\) is…' % (fr(a), b, x0), vi='Chi phí sản xuất \\(x\\) sản phẩm là \\(C(x)=%s\\,x^2+%dx+500\\) (nghìn đồng). Chi phí biên \\(C\'(%d)\\) bằng…' % (fr(a), b, x0),
      opts=pick_opts(r, fr(v), [fr(a * x0 * x0 + b * x0 + 500), fr(a * x0 + b), fr(2 * a * x0), fr(v + 500)]), ans=0,
      ee='\\(C\'(x)=2ax+b\\).', ev='\\(C\'(x)=%s x+%d\\); chi phí biên xấp xỉ chi phí làm thêm sản phẩm tiếp theo.' % (fr(2 * a), b))


M31S11 = [d_def, d_slope, d_tan, d_vel, d_avg, d_inv, d_cost, d_def]

# ================= Bài 32 =================
def r_poly(r, lv):
    n = r.randint(3, 5); a, b, c = nz(r, -4, 4), nz(r, -5, 5), r.randint(-6, 6)
    cs = [a] + [0] * (n - 2) + [b, c]; d = der(cs)
    wrong = [poly(der(cs)[:-1] + [d[-1] + c]) if c else poly([a * n] + [0] * (n - 2) + [b + 1]), poly([a] + [0] * (n - 3) + [b, 0]) if n > 3 else poly([a * n, 0]), poly([a * (n - 1)] + [0] * (n - 2) + [b]), poly([a * n] + [0] * (n - 2) + [-b])]
    return dict(en='The derivative of \\(y=%s\\) is…' % poly(cs), vi='Đạo hàm của hàm số \\(y=%s\\) là…' % poly(cs),
      opts=pick_opts(r, "y'=" + poly(d), ["y'=" + w for w in wrong]), ans=0, ee='\\((x^n)\'=nx^{n-1}\\), constants vanish.', ev='\\((x^n)\'=nx^{n-1}\\); đạo hàm của hằng số bằng 0.')


def r_prod(r, lv):
    a, b = nz(r, -4, 4), nz(r, -4, 4); x0 = nz(r, -2, 3)
    f = [1, b, a, a * b]  # (x^2+a)(x+b)
    v = ev(der(f), x0)
    return dict(en='\\(f(x)=(x^2%+d)(x%+d)\\). Then \\(f\'(%d)=\\)…' % (a, b, x0), vi='Cho \\(f(x)=(x^2%+d)(x%+d)\\). Khi đó \\(f\'(%d)=\\)…' % (a, b, x0),
      opts=pick_opts(r, str(v), [str(2 * x0 * 1), str(2 * x0 * (x0 + b)), str(ev(f, x0)), str(v + a), str(-v)]), ans=0,
      ee='\\((uv)\'=u\'v+uv\'\\).', ev='\\(f\'(x)=2x(x%+d)+(x^2%+d)\\), thay \\(x=%d\\).' % (b, a, x0))


def r_quot(r, lv):
    a, b, c = nz(r, -3, 3), r.randint(-5, 5), nz(r, -4, 4)
    if a * c - b == 0: raise AssertionError
    k = a * c - b
    q = lambda n: "y'=\\dfrac{%d}{(x%+d)^2}" % (n, c)
    return dict(en='The derivative of \\(y=\\dfrac{%s}{x%+d}\\) is…' % (poly([a, b]), c), vi='Đạo hàm của hàm số \\(y=\\dfrac{%s}{x%+d}\\) là…' % (poly([a, b]), c),
      opts=pick_opts(r, q(k), [q(b - a * c), q(a * c + b), "y'=\\dfrac{%d}{x%+d}" % (k, c), q(a)]), ans=0,
      ee='\\(\\left(\\dfrac{ax+b}{cx+d}\\right)\'=\\dfrac{ad-bc}{(cx+d)^2}\\).', ev='\\(\\left(\\dfrac uv\\right)\'=\\dfrac{u\'v-uv\'}{v^2}\\): tử số \\(%d(x%+d)-(%s)=%d\\).' % (a, c, poly([a, b]), k))


def r_chain(r, lv):
    a, b = nz(r, -3, 3), nz(r, -5, 5); n = r.randint(2, 5)
    base = '(%s)' % poly([a, b])
    return dict(en='The derivative of \\(y=%s^{%d}\\) is…' % (base, n), vi='Đạo hàm của hàm số \\(y=%s^{%d}\\) là…' % (base, n),
      opts=pick_opts(r, "y'=%d%s^{%d}" % (n * a, base, n - 1) if n > 2 else "y'=%d%s" % (n * a, base), ["y'=%d%s^{%d}" % (n, base, n - 1) if n > 2 else "y'=%d%s" % (n, base), "y'=%d%s^{%d}" % (a, base, n - 1) if n > 2 else "y'=%d%s" % (a, base), "y'=%d%s^{%d}" % (n * a, base, n) , "y'=%d%s^{%d}" % (n * a * a, base, n - 1) if n > 2 else "y'=%d%s" % (n * a * a, base)]), ans=0,
      ee='\\((u^n)\'=nu^{n-1}u\'\\).', ev='Hàm hợp: \\((u^n)\'=n\\,u^{n-1}\\cdot u\'\\) với \\(u=%s\\), \\(u\'=%d\\).' % (poly([a, b]), a))


def r_sqrt(r, lv):
    a = r.randint(1, 4); m = r.randint(2, 5); x0 = r.randint(0, 4); b = m * m - a * x0
    v = F(a, 2 * m)
    return dict(en='\\(f(x)=\\sqrt{%s}\\). Then \\(f\'(%d)=\\)…' % (poly([a, b]), x0), vi='Cho \\(f(x)=\\sqrt{%s}\\). Khi đó \\(f\'(%d)=\\)…' % (poly([a, b]), x0),
      opts=pick_opts(r, fr(v), [fr(F(1, 2 * m)), fr(F(a, m)), fr(F(a, m * m)), fr(2 * v + 1)]), ans=0,
      ee='\\((\\sqrt u)\'=\\dfrac{u\'}{2\\sqrt u}\\).', ev='\\(f\'(x)=\\dfrac{%d}{2\\sqrt{%s}}\\); tại \\(x=%d\\): \\(\\sqrt{%d}=%d\\).' % (a, poly([a, b]), x0, m * m, m))


def r_trig(r, lv):
    k = r.randint(2, 5); kind = r.choice(['sin', 'cos', 'tan'])
    if kind == 'sin': c, w = "y'=%d\\cos %dx" % (k, k), ["y'=\\cos %dx" % k, "y'=-%d\\cos %dx" % (k, k), "y'=%d\\sin %dx" % (k, k)]
    elif kind == 'cos': c, w = "y'=-%d\\sin %dx" % (k, k), ["y'=%d\\sin %dx" % (k, k), "y'=-\\sin %dx" % k, "y'=-%d\\cos %dx" % (k, k)]
    else: c, w = "y'=\\dfrac{%d}{\\cos^2 %dx}" % (k, k), ["y'=\\dfrac{1}{\\cos^2 %dx}" % k, "y'=-\\dfrac{%d}{\\sin^2 %dx}" % (k, k), "y'=%d\\tan %dx" % (k, k)]
    return dict(en='The derivative of \\(y=\\%s %dx\\) is…' % (kind, k), vi='Đạo hàm của hàm số \\(y=\\%s %dx\\) là…' % (kind, k), opts=pick_opts(r, c, w), ans=0,
      ee='Chain rule with \\(u=%dx\\).' % k, ev='Hàm hợp với \\(u=%dx\\), \\(u\'=%d\\).' % (k, k))


def r_explog(r, lv):
    k = r.randint(2, 5); kind = r.choice(['e', 'ln', 'a'])
    if kind == 'e': f, c, w = 'e^{%dx}' % k, "y'=%de^{%dx}" % (k, k), ["y'=e^{%dx}" % k, "y'=%dxe^{%dx-1}" % (k, k), "y'=e^{%d}" % k]
    elif kind == 'ln': f, c, w = '\\ln(%dx)' % k, "y'=\\dfrac1x", ["y'=\\dfrac{%d}{x}" % k, "y'=\\dfrac{1}{%dx^2}" % k, "y'=\\ln %d" % k]
    else: f, c, w = '%d^x' % k, "y'=%d^x\\ln %d" % (k, k), ["y'=x\\cdot %d^{x-1}" % k, "y'=%d^x" % k, "y'=\\dfrac{%d^x}{\\ln %d}" % (k, k)]
    return dict(en='The derivative of \\(y=%s\\) is…' % f, vi='Đạo hàm của hàm số \\(y=%s\\) là…' % f, opts=pick_opts(r, c, w), ans=0,
      ee='\\((e^u)\'=u\'e^u\\), \\((\\ln u)\'=\\dfrac{u\'}{u}\\), \\((a^x)\'=a^x\\ln a\\).', ev='\\((e^u)\'=u\'e^u\\), \\((\\ln u)\'=\\dfrac{u\'}{u}\\), \\((a^x)\'=a^x\\ln a\\).')


def r_tangent(r, lv):
    b = r.randint(-3, 3); x0 = nz(r, -2, 2); cs = [1, 0, b, 0]
    m = ev(der(cs), x0); y0 = ev(cs, x0); c = y0 - m * x0
    return dict(en='The tangent to \\(y=%s\\) at the point with abscissa \\(%d\\) is…' % (poly(cs), x0), vi='Tiếp tuyến của đồ thị \\(y=%s\\) tại điểm có hoành độ \\(%d\\) là…' % (poly(cs), x0),
      opts=pick_opts(r, lin(m, c), [lin(m, y0), lin(m, -c), lin(y0, c), lin(-m, c), lin(m, c + 1)]), ans=0,
      ee='\\(y=f\'(x_0)(x-x_0)+f(x_0)\\).', ev='\\(f\'(%d)=%d\\), \\(f(%d)=%d\\): \\(y=%d(x-(%d))+(%d)\\).' % (x0, m, x0, y0, m, x0, y0))


M32S11 = [r_poly, r_prod, r_quot, r_chain, r_sqrt, r_trig, r_explog, r_tangent]

# ================= Bài 33 =================
def s_poly(r, lv):
    a, b, c = nz(r, -3, 3), r.randint(-5, 5), r.randint(-5, 5); x0 = r.randint(-2, 3)
    cs = [a, b, c, r.randint(-5, 5)]; v = 6 * a * x0 + 2 * b
    return dict(en='For \\(%s\\), \\(f\'\'(%d)=\\)…' % (fx(cs), x0), vi='Cho \\(%s\\). Khi đó \\(f\'\'(%d)=\\)…' % (fx(cs), x0),
      opts=pick_opts(r, str(v), [str(ev(der(cs), x0)), str(3 * a * x0 + 2 * b), str(6 * a * x0 + b), str(-v), str(v + 2)]), ans=0,
      ee='Differentiate twice.', ev='\\(f\'(x)=%s\\), \\(f\'\'(x)=%s\\).' % (poly(der(cs)), poly(der(der(cs)))))


def s_acc(r, lv):
    p = r.choice([3, 6, 9]); q = r.randint(1, 12); t0 = r.randint(1, 5)
    cs = [1, -p, q, 0]; acc = 6 * t0 - 2 * p
    return dict(en='\\(s(t)=%s\\) (m, s). The acceleration at \\(t=%d\\) is… (m/s²)' % (poly(cs, 't'), t0), vi='Một vật chuyển động theo phương trình \\(s(t)=%s\\) (\\(s\\): mét, \\(t\\): giây). Gia tốc tại \\(t=%d\\) là… (m/s²)' % (poly(cs, 't'), t0),
      opts=pick_opts(r, str(acc), [str(ev(der(cs), t0)), str(3 * t0 - 2 * p), str(6 * t0 - p), str(-acc), str(acc + 6)]), ans=0,
      ee='\\(a(t)=s\'\'(t)\\).', ev='\\(v(t)=%s\\), \\(a(t)=%s\\).' % (poly(der(cs), 't'), poly(der(der(cs)), 't')))


def s_trig(r, lv):
    k = r.randint(2, 5); kind = r.choice(['sin', 'cos'])
    c = "y''=-%d\\%s %dx" % (k * k, kind, k)
    w = ["y''=%d\\%s %dx" % (k * k, kind, k), "y''=-%d\\%s %dx" % (k, kind, k), "y''=-%d\\%s %dx" % (k * k, 'cos' if kind == 'sin' else 'sin', k)]
    return dict(en='For \\(y=\\%s %dx\\), \\(y\'\'=\\)…' % (kind, k), vi='Cho \\(y=\\%s %dx\\). Khi đó…' % (kind, k), opts=pick_opts(r, c, w), ans=0,
      ee='\\(y\'\'=-%d^2y\\).' % k, ev='Đạo hàm hai lần, mỗi lần nhân thêm \\(%d\\): \\(y\'\'=-%d\\,y\\).' % (k, k * k))


def s_exp(r, lv):
    k = r.randint(2, 5)
    return dict(en='For \\(y=e^{%dx}\\), \\(y\'\'=\\)…' % k, vi='Cho \\(y=e^{%dx}\\). Khi đó…' % k,
      opts=pick_opts(r, "y''=%de^{%dx}" % (k * k, k), ["y''=%de^{%dx}" % (2 * k, k), "y''=%de^{%dx}" % (k, k), "y''=e^{%dx}" % k]), ans=0, ee='Each derivative multiplies by \\(%d\\).' % k, ev='Mỗi lần lấy đạo hàm nhân thêm \\(%d\\).' % k)


def s_xn(r, lv):
    n = r.randint(3, 7)
    return dict(en='\\((x^%d)\'\'=\\)…' % n, vi='Đạo hàm cấp hai của \\(y=x^%d\\) là…' % n,
      opts=pick_opts(r, "%dx^{%d}" % (n * (n - 1), n - 2) if n > 3 else "%dx" % (n * (n - 1)), ["%dx^{%d}" % (n, n - 1), "%dx^{%d}" % (n * n, n - 2) if n > 3 else "%dx" % (n * n), "%dx^{%d}" % (n * (n - 1), n - 1), "%dx^{%d}" % (2 * n, n - 2) if n > 3 else "%dx" % (2 * n)]), ans=0,
      ee='\\(n(n-1)x^{n-2}\\).', ev='\\((x^n)\'\'=n(n-1)x^{n-2}\\).')


def s_inflect(r, lv):
    p = 3 * nz(r, -3, 3); q = r.randint(-5, 5)
    cs = [1, -p, q, 1]; t = F(p, 3)
    return dict(en='For \\(%s\\), the equation \\(f\'\'(x)=0\\) has the solution…' % fx(cs), vi='Cho \\(%s\\). Phương trình \\(f\'\'(x)=0\\) có nghiệm là…' % fx(cs),
      opts=pick_opts(r, 'x=' + fr(t), ['x=' + fr(-t), 'x=' + fr(F(p, 6)), 'x=' + fr(2 * t), 'x=' + fr(F(p, 2))]), ans=0, ee='\\(f\'\'(x)=6x-%d\\).' % (2 * p) if p > 0 else '\\(f\'\'(x)=6x+%d\\).' % (-2 * p),
      ev='\\(f\'\'(x)=%s=0\\).' % poly([6, -2 * p]))


def s_ln(r, lv):
    k = r.randint(2, 5)
    return dict(en='For \\(y=\\ln(%dx)\\) (\\(x>0\\)), \\(y\'\'=\\)…' % k, vi='Cho \\(y=\\ln(%dx)\\) với \\(x>0\\). Khi đó \\(y\'\'=\\)…' % k,
      opts=pick_opts(r, '-\\dfrac{1}{x^2}', ['\\dfrac{1}{x^2}', '-\\dfrac{%d}{x^2}' % k, '-\\dfrac{%d}{x^2}' % (k * k), '\\dfrac1x']), ans=0, ee='\\(y\'=\\dfrac1x\\).', ev='\\(y\'=\\dfrac{%d}{%dx}=\\dfrac1x\\), \\(y\'\'=-\\dfrac1{x^2}\\).' % (k, k))


def s_vmin(r, lv):
    p = r.choice([3, 6, 9, 12]); q = r.randint(30, 60); cs = [1, -p, q, 0]; t = p // 3
    return dict(en='\\(s(t)=%s\\). At which time is the acceleration zero?' % poly(cs, 't'), vi='Một vật chuyển động theo \\(s(t)=%s\\) (\\(t\\) giây). Gia tốc bằng 0 tại thời điểm…' % poly(cs, 't'),
      opts=pick_opts(r, 't=%d' % t, ['t=%d' % (2 * t), 't=%d' % p, 't=%d' % (t + 1), 't=%d' % (p // 2) if p // 2 != t else 't=%d' % (t + 2)]), ans=0,
      ee='\\(a(t)=6t-%d=0\\).' % (2 * p), ev='\\(a(t)=s\'\'(t)=6t-%d=0\\).' % (2 * p))


M33S11 = [s_poly, s_acc, s_trig, s_exp, s_xn, s_inflect, s_ln, s_vmin]


def _primes(b):
    def w(r, lv):
        d = b(r, lv)
        fix = lambda s: s.replace("''", '″').replace("'", '′') if isinstance(s, str) else s
        return {k: ([fix(o) for o in v] if k == 'opts' else fix(v)) for k, v in d.items()}
    w.__name__ = b.__name__
    return w
M31S11, M32S11, M33S11 = [[_primes(b) for b in L] for L in (M31S11, M32S11, M33S11)]
