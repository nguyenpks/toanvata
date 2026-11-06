# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 11 – Bài 17 (hàm số liên tục), Bài 18 (lũy thừa với số mũ thực). Đáp án tính chính xác."""
import math
from fractions import Fraction as F
from mb_selfpractice import pick_opts, fr
from mb_lib import TI
from freqtable import num
from sp_g11e import poly

def TT(en, vi): return '§' + TI(en, vi)
def D(x): return num(F(x))
def DE(x): return num(F(x), comma=False)
def pw(cs): return poly(cs, 'x')
def ex(q):
    q = F(q)
    if q.denominator == 1: return str(q.numerator)
    return ('-' if q < 0 else '') + '\\frac{%d}{%d}' % (abs(q.numerator), q.denominator)
def xp(base, q):
    return base if F(q) == 1 else '%s^{%s}' % (base, ex(q))
# ================= Bài 17. Hàm số liên tục =================
def c_rem(r, lv):
    a, b = r.randint(-4, 5), r.randint(-4, 5)
    if a == b: raise AssertionError
    v = a - b
    return dict(en='\\(f(x)=\\dfrac{%s}{x%+d}\\) for \\(x\\ne%d\\) and \\(f(%d)=m\\). \\(f\\) is continuous at \\(x=%d\\) when \\(m=\\)…' % (pw([1, -(a + b), a * b]), -a, a, a, a),
      vi='Cho \\(f(x)=\\dfrac{%s}{x%+d}\\) khi \\(x\\ne%d\\) và \\(f(%d)=m\\). Hàm số liên tục tại \\(x=%d\\) khi \\(m=\\)…' % (pw([1, -(a + b), a * b]), -a, a, a, a),
      opts=pick_opts(r, str(v), [str(a + b), str(b - a), '0', str(a), str(v + 1)]), ans=0,
      ee='Need \\(m=\\lim\\limits_{x\\to%d}(x%+d)=%d\\).' % (a, -b, v), ev='Cần \\(m=\\lim\\limits_{x\\to%d}(x%+d)=%d\\).' % (a, -b, v))
def c_piece(r, lv):
    x0 = r.randint(-2, 3); k = r.choice([1, 2, 3, -1]); p = r.randint(-4, 5); q = r.choice([1, 2, -1, 3])
    L = k * x0 * x0 + p; m = L - q * x0
    return dict(en='\\(f(x)=%s\\) for \\(x\\lt%d\\), \\(f(x)=%s+m\\) for \\(x\\ge%d\\). \\(f\\) is continuous on \\(\\mathbb R\\) when \\(m=\\)…' % (pw([k, 0, p]), x0, pw([q, 0]), x0),
      vi='Cho \\(f(x)=%s\\) khi \\(x\\lt%d\\), \\(f(x)=%s+m\\) khi \\(x\\ge%d\\). Hàm số liên tục trên \\(\\mathbb R\\) khi \\(m=\\)…' % (pw([k, 0, p]), x0, pw([q, 0]), x0),
      opts=pick_opts(r, str(m), [str(L), str(L + q * x0), str(-m) if m else '1', str(m + 1)]), ans=0,
      ee='Left limit \\(%d\\), right value \\(%d+m\\): \\(m=%d\\).' % (L, q * x0, m), ev='Giới hạn trái \\(%d\\), giá trị bên phải \\(%d+m\\): \\(m=%d\\).' % (L, q * x0, m))
def c_dom(r, lv):
    a, b = sorted(r.sample(range(-4, 6), 2)); kind = r.choice(['two', 'one'])
    if kind == 'two':
        f = '\\dfrac{x+%d}{%s}' % (r.randint(1, 5), pw([1, -(a + b), a * b])); ok = '(-\\infty;%d),\\ (%d;%d),\\ (%d;+\\infty)' % (a, a, b, b)
        wr = ['\\mathbb R', '(%d;%d)' % (a, b), '\\mathbb R\\setminus\\{%d\\}' % b, '(-\\infty;%d),\\ (%d;+\\infty)' % (-a, -b)]
    else:
        f = '\\sqrt{x%+d}' % -a if a else '\\sqrt x'; ok = '[%d;+\\infty)' % a; wr = ['\\mathbb R', '(%d;+\\infty)' % a, '(-\\infty;%d]' % a, '\\mathbb R\\setminus\\{%d\\}' % a]
    return dict(en='The function \\(y=%s\\) is continuous on…' % f, vi='Hàm số \\(y=%s\\) liên tục trên…' % f, opts=pick_opts(r, ok, wr), ans=0,
      ee='Elementary functions are continuous on each interval of their domain.', ev='Hàm số sơ cấp liên tục trên từng khoảng (nửa khoảng) của tập xác định.')
def c_ivt(r, lv):
    for _ in range(200):
        cs = [1, 0, r.choice([-3, -2, -1, 1, 2]), r.choice([-3, -1, 1, 2, 3])]
        f = lambda x: cs[0] * x ** 3 + cs[2] * x + cs[3]
        ints = [(i, i + 1) for i in range(-3, 3)]
        good = [iv for iv in ints if f(iv[0]) * f(iv[1]) < 0]; bad = [iv for iv in ints if f(iv[0]) * f(iv[1]) > 0]
        if good and len(bad) >= 3: break
    else: raise AssertionError
    g = r.choice(good)
    return dict(en='The equation \\(%s=0\\) surely has a root in the interval…' % pw(cs), vi='Phương trình \\(%s=0\\) chắc chắn có nghiệm thuộc khoảng…' % pw(cs),
      opts=pick_opts(r, '(%d;%d)' % g, ['(%d;%d)' % b for b in r.sample(bad, 3)]), ans=0,
      ee='\\(f(%d)=%d\\), \\(f(%d)=%d\\) have opposite signs and \\(f\\) is continuous.' % (g[0], f(g[0]), g[1], f(g[1])), ev='\\(f(%d)=%d\\), \\(f(%d)=%d\\) trái dấu và \\(f\\) liên tục.' % (g[0], f(g[0]), g[1], f(g[1])))
def c_count(r, lv):
    roots = sorted(r.sample(range(-4, 5), 3)); cs = [1, -sum(roots), roots[0] * roots[1] + roots[0] * roots[2] + roots[1] * roots[2], -roots[0] * roots[1] * roots[2]]
    f = lambda x: x ** 3 + cs[1] * x * x + cs[2] * x + cs[3]
    pts = sorted(set([roots[0] - 1, roots[2] + 1] + [F(roots[i] + roots[i + 1], 2) for i in range(2)]))
    if any(f(p) == 0 for p in pts): raise AssertionError
    return dict(en='\\(f(x)=%s\\). Using \\(f(%s)\\), \\(f(%s)\\), \\(f(%s)\\), \\(f(%s)\\), how many roots does \\(f(x)=0\\) have on \\(\\mathbb R\\)?' % ((pw(cs),) + tuple(fr(F(p)) for p in pts)),
      vi='Cho \\(f(x)=%s\\). Dựa vào \\(f(%s)\\), \\(f(%s)\\), \\(f(%s)\\), \\(f(%s)\\), phương trình \\(f(x)=0\\) có bao nhiêu nghiệm thực?' % ((pw(cs),) + tuple(fr(F(p)) for p in pts)),
      opts=pick_opts(r, '3', ['1', '2', '0']), ans=0, ee='Three sign changes give at least 3 roots; a cubic has at most 3.', ev='Ba lần đổi dấu cho ít nhất 3 nghiệm; phương trình bậc ba có không quá 3 nghiệm.')
def c_temp(r, lv):
    t1, t2 = r.choice([(6, 14), (5, 12), (7, 15)]); T1, T2 = r.choice([(18, 31), (20, 34), (16, 29)]); c = r.randint(T1 + 1, T2 - 1)
    return dict(en='At %d h the temperature was %d °C and at %d h it was %d °C. Temperature changes continuously. Which statement is surely true?' % (t1, T1, t2, T2), vi='Lúc %d giờ nhiệt độ là %d °C, lúc %d giờ là %d °C. Nhiệt độ thay đổi liên tục. Khẳng định nào chắc chắn đúng?' % (t1, T1, t2, T2),
      opts=[TT('At some moment between %d h and %d h it was exactly %d °C' % (t1, t2, c), 'Có thời điểm giữa %d giờ và %d giờ nhiệt độ đúng bằng %d °C' % (t1, t2, c)), TT('At %d h it was %d °C' % ((t1 + t2) // 2, (T1 + T2) // 2), 'Lúc %d giờ nhiệt độ là %d °C' % ((t1 + t2) // 2, (T1 + T2) // 2)),
            TT('The temperature never went above %d °C' % T2, 'Nhiệt độ không bao giờ vượt quá %d °C' % T2), TT('The temperature always increased', 'Nhiệt độ luôn tăng')], ans=0,
      ee='Intermediate value theorem: a continuous function takes every value between \\(%d\\) and \\(%d\\).' % (T1, T2), ev='Định lí giá trị trung gian: hàm liên tục nhận mọi giá trị nằm giữa \\(%d\\) và \\(%d\\).' % (T1, T2))
M17S11 = [c_rem, c_piece, c_dom, c_ivt, c_count, c_temp, c_rem, c_piece]
# ================= Bài 18. Lũy thừa với số mũ thực =================
BASES = [(4, 2), (8, 2), (9, 3), (27, 3), (16, 2), (25, 5), (32, 2), (64, 2), (81, 3), (125, 5)]
def e_rat(r, lv):
    N, b = r.choice(BASES); k = round(math.log(N, b)); n = r.choice([d for d in (2, 3, 4, 5) if k % d == 0] or [1]); m = r.choice([1, 2, 3, -1, -2]); v = F(b) ** (k * m // n)
    if n == 1: raise AssertionError
    e = ex(F(m, n))
    return dict(en='\\(%d^{%s}=\\)…' % (N, e), vi='\\(%d^{%s}=\\)…' % (N, e), opts=pick_opts(r, fr(v), [fr(F(N * m, n)) if F(N * m, n).denominator == 1 else fr(v * b), fr(1 / v), fr(F(b) ** (k * abs(m) // n) + 1), fr(-v)]), ans=0,
      ee='\\(%d=%d^{%d}\\), so \\(%d^{%s}=%d^{%d\\cdot%s}=%s\\).' % (N, b, k, N, e, b, k, e, fr(v)), ev='\\(%d=%d^{%d}\\) nên \\(%d^{%s}=%d^{%d\\cdot%s}=%s\\).' % (N, b, k, N, e, b, k, e, fr(v)))
def e_rule(r, lv):
    p, q, s = (F(r.choice([1, 2, 3, 5, 7]), r.choice([2, 3, 4, 6])) for _ in range(3)); t = p + q - s
    if t <= 0 or t.denominator > 12: raise AssertionError
    return dict(en='For \\(a\\gt0\\): \\(\\dfrac{a^{%s}\\cdot a^{%s}}{a^{%s}}=\\)…' % (ex(p), ex(q), ex(s)), vi='Với \\(a\\gt0\\): \\(\\dfrac{a^{%s}\\cdot a^{%s}}{a^{%s}}=\\)…' % (ex(p), ex(q), ex(s)),
      opts=pick_opts(r, xp('a', t), [xp('a', p * q / s), xp('a', p + q + s), xp('a', p * q - s), xp('a', t + 1)]), ans=0,
      ee='Add exponents when multiplying, subtract when dividing: \\(%s+%s-%s=%s\\).' % (ex(p), ex(q), ex(s), ex(t)), ev='Nhân thì cộng số mũ, chia thì trừ số mũ: \\(%s+%s-%s=%s\\).' % (ex(p), ex(q), ex(s), ex(t)))
def e_root(r, lv):
    n = r.choice([3, 4, 5, 6]); m = r.choice([1, 2, 3, 5]); k = r.choice([1, 2])
    if math.gcd(m, n) != 1: raise AssertionError
    e = F(m, n) + k
    return dict(en='For \\(x\\gt0\\): \\(%s\\cdot\\sqrt[%d]{x^{%d}}=\\)…' % (xp('x', k), n, m), vi='Với \\(x\\gt0\\): \\(%s\\cdot\\sqrt[%d]{x^{%d}}=\\)…' % (xp('x', k), n, m),
      opts=pick_opts(r, xp('x', e), [xp('x', F(n, m) + k), xp('x', F(m * k, n)), xp('x', F(m + k, n)), xp('x', F(m, n))]), ans=0,
      ee='\\(\\sqrt[%d]{x^{%d}}=x^{\\frac{%d}{%d}}\\); \\(%d+\\frac{%d}{%d}=%s\\).' % (n, m, m, n, k, m, n, ex(e)), ev='\\(\\sqrt[%d]{x^{%d}}=x^{\\frac{%d}{%d}}\\); \\(%d+\\frac{%d}{%d}=%s\\).' % (n, m, m, n, k, m, n, ex(e)))
CMP = {'\\sqrt3': ('1{,}7', True), '\\sqrt2': ('1{,}5', False), '\\pi': ('3{,}14', True), '\\sqrt5': ('2{,}3', False)}
def e_cmp(r, lv):
    a = r.choice([F(2), F(3), F(1, 2), F(2, 3), F(5, 4), F(3, 5)]); x = r.choice(list(CMP)); y, first_big = CMP[x]
    big = (a > 1) == first_big
    P = lambda rel: '\\left(%s\\right)^{%s}%s\\left(%s\\right)^{%s}' % (fr(a), x, rel, fr(a), y)
    q = '\\(\\left(%s\\right)^{%s}\\) và \\(\\left(%s\\right)^{%s}\\)' % (fr(a), x, fr(a), y)
    return dict(en='Compare ' + q.replace(' và ', ' and '), vi='So sánh ' + q,
      opts=pick_opts(r, P('\\gt' if big else '\\lt'), [P('\\lt' if big else '\\gt'), P('='), TT('Cannot compare', 'Không so sánh được')]), ans=0,
      ee='\\(%s %s %s\\) and the base is %s 1.' % (x, '\\gt' if first_big else '\\lt', y, 'greater than' if a > 1 else 'less than'),
      ev='\\(%s %s %s\\) và cơ số %s 1.' % (x, '\\gt' if first_big else '\\lt', y, 'lớn hơn' if a > 1 else 'nhỏ hơn'))
def e_interest(r, lv):
    P = r.choice([10, 20, 50, 100]); rate = r.choice([5, 6, 8, 10]); n = r.choice([2, 3])
    A = F(P) * F(100 + rate, 100) ** n
    return dict(en='You deposit %d million VND at %d%% per year, compound interest. After %d years the balance is… (million VND)' % (P, rate, n), vi='Gửi tiết kiệm %d triệu đồng, lãi suất %d%%/năm, lãi kép. Sau %d năm số tiền là… (triệu đồng)' % (P, rate, n),
      opts=pick_opts(r, D(A), [D(P * (1 + F(rate * n, 100))), D(F(P) * F(100 + rate, 100) ** (n + 1)), D(A + 1), D(P + F(P * rate, 100))]), ans=0,
      ee='\\(A=%d\\left(1+\\frac{%d}{100}\\right)^{%d}=%s\\).' % (P, rate, n, DE(A)), ev='\\(A=%d\\left(1+\\frac{%d}{100}\\right)^{%d}=%s\\).' % (P, rate, n, D(A)))
def e_half(r, lv):
    m0 = r.choice([80, 160, 200, 320, 640]); T = r.choice([5, 8, 30, 12]); k = r.choice([2, 3, 4]); m = F(m0, 2 ** k)
    return dict(en='A radioactive substance has a half-life of %d years. From %d g, how much remains after %d years?' % (T, m0, k * T), vi='Một chất phóng xạ có chu kì bán rã %d năm. Từ %d g, sau %d năm còn lại bao nhiêu gam?' % (T, m0, k * T),
      opts=pick_opts(r, D(m) + '\\ \\text{g}', [D(F(m0, 2 * k)) + '\\ \\text{g}', D(m * 2) + '\\ \\text{g}', D(m / 2) + '\\ \\text{g}', D(F(m0, k)) + '\\ \\text{g}']), ans=0,
      ee='\\(m=%d\\left(\\frac12\\right)^{%d}=%s\\).' % (m0, k, DE(m)), ev='\\(m=%d\\left(\\frac12\\right)^{%d}=%s\\).' % (m0, k, D(m)))
def e_neg(r, lv):
    b = r.choice([2, 3, 5, 10]); n = r.choice([1, 2, 3]); v = F(1, b ** n); c = r.choice([0, 1])
    e = '%d^{-%d}' % (b, n) if not c else '\\left(\\dfrac1{%d}\\right)^{%d}' % (b, n)
    return dict(en='\\(%s=\\)…' % e, vi='\\(%s=\\)…' % e, opts=pick_opts(r, fr(v), [str(-b ** n), fr(F(-1, b ** n)), str(b ** n), fr(F(1, b * n))]), ans=0,
      ee='\\(a^{-n}=\\dfrac1{a^n}\\).', ev='\\(a^{-n}=\\dfrac1{a^n}\\).')
M18S11 = [e_rat, e_rule, e_root, e_cmp, e_interest, e_half, e_neg, e_rat]
