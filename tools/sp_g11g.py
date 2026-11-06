# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 11 – Bài 19 (lôgarit), Bài 20 (hàm số mũ và hàm số lôgarit), Bài 21 (phương trình, bất phương trình mũ và lôgarit).
Đáp án tính chính xác bằng số nguyên / Fraction (lôgarit chỉ lấy các giá trị đúng)."""
import math
from fractions import Fraction as F
from mb_selfpractice import pick_opts, fr
from sp_g11f import TT, ex, D, DE
from sp_g10f import poly
def fac(p): return 'x' if p == 0 else 'x%+d' % -p

def lg(b, x): return '\\log_{%s}%s' % (fr(F(b)) if F(b).denominator == 1 else '\\frac{%d}{%d}' % (F(b).numerator, F(b).denominator), x)
def frn(q):
    q = F(q); return str(q.numerator) if q.denominator == 1 else ('-' if q < 0 else '') + '\\dfrac{%d}{%d}' % (abs(q.numerator), q.denominator)
BASES = [2, 3, 5, 10, 4, 9]
# ================= Bài 19. Lôgarit =================
def lg_val(r, lv):
    b = r.choice([2, 3, 5, 10]); k = r.choice([-3, -2, -1, 2, 3, 4, F(1, 2), F(3, 2), F(-1, 2)])
    if k.denominator if isinstance(k, F) else 1: pass
    k = F(k)
    if k.denominator == 1: N = frn(F(b) ** int(k))
    else: N = '\\sqrt{%d}' % b if k == F(1, 2) else '%d\\sqrt{%d}' % (b, b) if k == F(3, 2) else '\\dfrac{1}{\\sqrt{%d}}' % b
    return dict(en='\\(%s=\\)…' % lg(b, N if len(N) == 1 or N.isdigit() else '{%s}' % N), vi='\\(%s=\\)…' % lg(b, N if len(N) == 1 or N.isdigit() else '{%s}' % N),
      opts=pick_opts(r, frn(k), [frn(-k), frn(k + 1), frn(1 / k), frn(k * 2)]), ans=0,
      ee='\\(%d^{%s}=%s\\).' % (b, ex(k), N), ev='Vì \\(%d^{%s}=%s\\).' % (b, ex(k), N))
def lg_def(r, lv):
    b = r.choice([2, 3, 4, 5]); c = r.choice([2, 3, 4, -1, -2]); x = F(b) ** c
    return dict(en='If \\(%s=%d\\) then \\(x=\\)…' % (lg(b, 'x'), c), vi='Nếu \\(%s=%d\\) thì \\(x=\\)…' % (lg(b, 'x'), c), opts=pick_opts(r, frn(x), [frn(b * c), frn(F(c) ** b) if c > 0 else frn(-x), frn(x * b), frn(F(b, c) if c else 1)]), ans=0,
      ee='\\(x=%d^{%d}\\).' % (b, c), ev='\\(\\log_a x=c\\iff x=a^c\\): \\(x=%d^{%d}\\).' % (b, c))
def lg_sum(r, lv):
    b = r.choice([2, 3, 6, 10, 5]); k = r.choice([1, 2, 3]); T = b ** k
    ds = [d for d in range(2, T) if T % d == 0 and d != T // d]
    if not ds: raise AssertionError
    m = r.choice(ds); n = T // m; op = r.choice(['+', '-'])
    if op == '+': q = '%s+%s' % (lg(b, m), lg(b, n)); w = [frn(F(m + n)), str(k + 1), str(k - 1) if k > 1 else '0', frn(F(m * n))]
    else:
        m2 = T * n; q = '%s-%s' % (lg(b, m2), lg(b, n)); w = [str(k + 1), frn(F(m2 - n)), str(k - 1) if k > 1 else '0', frn(F(m2, n) + 1)]
    return dict(en='\\(%s=\\)…' % q, vi='\\(%s=\\)…' % q, opts=pick_opts(r, str(k), w), ans=0,
      ee='Use \\(\\log_a M\\pm\\log_a N=\\log_a(MN)\\) / \\(\\log_a\\frac MN\\): \\(\\log_{%d}%d=%d\\).' % (b, T, k), ev='\\(\\log_a M+\\log_a N=\\log_a(MN)\\), \\(\\log_a M-\\log_a N=\\log_a\\frac MN\\): được \\(\\log_{%d}%d=%d\\).' % (b, T, k))
def lg_expr(r, lv):
    p, q = r.choice([(2, 3), (2, 5), (3, 2), (3, 5)]); i, j = r.randint(1, 3), r.randint(1, 3); N = p ** i * q ** j
    ok = '%d+%da' % (i, j) if j > 1 else '%d+a' % i
    return dict(en='Given \\(%s=a\\). Then \\(%s=\\)…' % (lg(p, q), lg(p, N)), vi='Cho \\(%s=a\\). Khi đó \\(%s=\\)…' % (lg(p, q), lg(p, N)),
      opts=pick_opts(r, ok, ['%d+%da' % (j, i) if (i, j) != (j, i) else '%da' % (i + j), '%da' % (i * j), '%d+%da' % (i + 1, j), '%d\\cdot%da' % (i, j)]), ans=0,
      ee='\\(%d=%d^{%d}\\cdot%d^{%d}\\Rightarrow%s=%d+%d%s\\).' % (N, p, i, q, j, lg(p, N), i, j, lg(p, q)), ev='\\(%d=%d^{%d}\\cdot%d^{%d}\\Rightarrow%s=%d+%d%s\\).' % (N, p, i, q, j, lg(p, N), i, j, lg(p, q)))
def lg_change(r, lv):
    p = r.choice([2, 3]); i, j = r.sample([1, 2, 3, 4, 5], 2); v = F(j, i)
    return dict(en='\\(%s=\\)…' % lg(p ** i, p ** j), vi='\\(%s=\\)…' % lg(p ** i, p ** j), opts=pick_opts(r, frn(v), [frn(1 / v), frn(F(p ** j, p ** i)), frn(v + 1), frn(F(j - i))]), ans=0,
      ee='\\(%s=\\dfrac{%s}{%s}=\\dfrac{%d}{%d}\\).' % (lg(p ** i, p ** j), lg(p, p ** j), lg(p, p ** i), j, i), ev='Đổi cơ số: \\(%s=\\dfrac{%s}{%s}=\\dfrac{%d}{%d}\\).' % (lg(p ** i, p ** j), lg(p, p ** j), lg(p, p ** i), j, i))
def lg_ab(r, lv):
    a = r.choice([2, 3, 5]); b = r.choice([3, 5, 7, 6]); k = r.choice([1, 2, 3])
    if a == b: raise AssertionError
    v = b ** k; e = '%s' % lg(a, b) if k == 1 else '%d%s' % (k, lg(a, b))
    return dict(en='\\(%d^{%s}=\\)…' % (a, e), vi='\\(%d^{%s}=\\)…' % (a, e), opts=pick_opts(r, str(v), [str(k * b), str(a * k), str(b), str(a ** k)]), ans=0,
      ee='\\(a^{\\log_a b}=b\\): \\(%d^{%s}=%d^{%d}=%d\\).' % (a, e, b, k, v), ev='\\(a^{\\log_a b}=b\\): \\(%d^{%s}=%d^{%d}=%d\\).' % (a, e, b, k, v))
def lg_ph(r, lv):
    k = r.randint(2, 12); kind = r.choice(['ph', 'db'])
    if kind == 'ph':
        return dict(en='\\(\\mathrm{pH}=-\\log[\\mathrm{H^+}]\\). A solution has \\([\\mathrm{H^+}]=10^{-%d}\\) mol/L. Its pH is…' % k, vi='\\(\\mathrm{pH}=-\\log[\\mathrm{H^+}]\\). Một dung dịch có \\([\\mathrm{H^+}]=10^{-%d}\\) mol/L. Độ pH là…' % k,
          opts=pick_opts(r, str(k), [str(-k), str(14 - k) if 14 - k != k else str(k + 2), str(k + 1), str(10 * k)]), ans=0, ee='\\(-\\log10^{-%d}=%d\\).' % (k, k), ev='\\(-\\log10^{-%d}=%d\\).' % (k, k))
    return dict(en='Sound level \\(L=10\\log\\dfrac{I}{I_0}\\) (dB). A sound with \\(I=10^{%d}I_0\\) has level…' % k, vi='Mức cường độ âm \\(L=10\\log\\dfrac{I}{I_0}\\) (dB). Âm có \\(I=10^{%d}I_0\\) có mức cường độ…' % k,
      opts=pick_opts(r, '%d\\text{ dB}' % (10 * k), ['%d\\text{ dB}' % k, '%d\\text{ dB}' % (10 * k + 10), '%d\\text{ dB}' % (10 ** min(k, 3)), '%d\\text{ dB}' % (100 * k)]), ans=0, ee='\\(10\\cdot%d=%d\\).' % (k, 10 * k), ev='\\(L=10\\log10^{%d}=%d\\) dB.' % (k, 10 * k))
def lg_dom(r, lv):
    a = r.randint(-5, 5); kind = r.choice(['lin', 'sq'])
    if kind == 'lin':
        e = 'x%+d' % -a if a else 'x'; ok = 'x\\gt%d' % a; w = ['x\\ge%d' % a, 'x\\lt%d' % a, 'x\\ne%d' % a, 'x\\gt%d' % -a if a else 'x\\gt1']
    else:
        e = '(x%+d)^2' % -a if a else 'x^2'; ok = 'x\\ne%d' % a; w = ['x\\gt%d' % a, 'x\\in\\mathbb R', 'x\\ge%d' % a, 'x\\ne%d' % -a if a else 'x\\gt0']
    return dict(en='\\(%s\\) is defined when…' % lg(r.choice([2, 3, 5]), '(%s)' % e), vi='\\(%s\\) có nghĩa khi…' % lg(r.choice([2, 3, 5]), '(%s)' % e), opts=pick_opts(r, ok, w), ans=0,
      ee='Need \\(%s\\gt0\\).' % e, ev='Cần \\(%s\\gt0\\).' % e)
M19S11 = [lg_val, lg_def, lg_sum, lg_expr, lg_change, lg_ab, lg_ph, lg_dom]
# ================= Bài 20. Hàm số mũ và hàm số lôgarit =================
def f_dom(r, lv):
    p, q = sorted(r.sample(range(-4, 6), 2)); b = r.choice([2, 3, '\\frac12'])
    e = poly([1, -(p + q), p * q])
    ok = '(-\\infty;\\,%d)\\cup(%d;\\,+\\infty)' % (p, q)
    return dict(en='The domain of \\(y=\\log_{%s}(%s)\\) is…' % (b, e), vi='Tập xác định của hàm số \\(y=\\log_{%s}(%s)\\) là…' % (b, e),
      opts=pick_opts(r, ok, ['(%d;\\,%d)' % (p, q), '[%d;\\,%d]' % (p, q), '\\mathbb R', '(-\\infty;\\,%d]\\cup[%d;\\,+\\infty)' % (p, q)]), ans=0,
      ee='Need \\((%s)(%s)\\gt0\\).' % (fac(p), fac(q)), ev='Cần \\((%s)(%s)\\gt0\\).' % (fac(p), fac(q)))
FUN = [('y=2^x', True), ('y=\\left(\\frac12\\right)^x', False), ('y=\\log_3x', True), ('y=\\log_{\\frac13}x', False), ('y=\\left(\\frac{\\pi}{3}\\right)^x', True), ('y=\\left(\\frac{\\sqrt2}{2}\\right)^x', False),
       ('y=\\log_{0{,}5}x', False), ('y=\\ln x', True), ('y=e^x', True), ('y=\\left(\\frac{2}{e}\\right)^x', False), ('y=\\log_{\\sqrt3}x', True), ('y=\\left(\\frac{3}{4}\\right)^x', False)]
def f_mono(r, lv):
    f, inc = r.choice(FUN)
    opts = [TT('increasing', 'đồng biến'), TT('decreasing', 'nghịch biến')]
    if not inc: opts.reverse()
    return dict(en='On its domain, the function \\(%s\\) is…' % f, vi='Trên tập xác định, hàm số \\(%s\\)…' % f,
      opts=opts + [TT('constant', 'không đổi'), TT('increasing, then decreasing', 'đồng biến rồi nghịch biến')], ans=0,
      ee='Base \\(\\gt1\\): increasing; base in \\((0;1)\\): decreasing.', ev='Cơ số lớn hơn 1: đồng biến; cơ số thuộc \\((0;1)\\): nghịch biến.')
def f_base(r, lv):
    a = r.choice([2, 3, 4, 5, F(1, 2), F(1, 3)]); k = r.choice([2, 3, -1, -2]); x = F(a) ** k
    kind = r.choice(['log', 'exp'])
    if kind == 'log':
        q = 'The graph of \\(y=\\log_a x\\) passes through \\(M(%s;\\,%d)\\). Then \\(a=\\)…' % (frn(x), k); qv = 'Đồ thị hàm số \\(y=\\log_a x\\) đi qua \\(M(%s;\\,%d)\\). Khi đó \\(a=\\)…' % (frn(x), k)
        e = '\\(a^{%d}=%s\\).' % (k, frn(x))
    else:
        q = 'The graph of \\(y=a^x\\) passes through \\(M(%d;\\,%s)\\). Then \\(a=\\)…' % (k, frn(x)); qv = 'Đồ thị hàm số \\(y=a^x\\) đi qua \\(M(%d;\\,%s)\\). Khi đó \\(a=\\)…' % (k, frn(x)); e = '\\(a^{%d}=%s\\).' % (k, frn(x))
    return dict(en=q, vi=qv, opts=pick_opts(r, frn(a), [frn(1 / F(a)), frn(x / k), frn(F(a) + 1), frn(F(a) * 2)]), ans=0, ee=e, ev=e)
def f_point(r, lv):
    kind = r.choice(['exp', 'log']); a = r.choice([2, 3, 5, '\\frac12', '\\pi'])
    if kind == 'exp': ok, w = '(0;\\,1)', ['(1;\\,0)', '(1;\\,1)', '(0;\\,0)', '(1;\\,%s)' % a if a not in ('\\frac12',) else '(-1;\\,0)']
    else: ok, w = '(1;\\,0)', ['(0;\\,1)', '(1;\\,1)', '(0;\\,0)', '(%s;\\,0)' % a if a != '\\pi' else '(-1;\\,0)']
    f = 'y=%s^x' % ('\\left(\\frac12\\right)' if a == '\\frac12' else a) if kind == 'exp' else 'y=\\log_{%s}x' % a
    return dict(en='The graph of \\(%s\\) always passes through…' % f, vi='Đồ thị hàm số \\(%s\\) luôn đi qua điểm…' % f, opts=pick_opts(r, ok, w), ans=0,
      ee='\\(a^0=1\\), \\(\\log_a1=0\\).', ev='\\(a^0=1\\), \\(\\log_a1=0\\).')
def f_bact(r, lv):
    N0 = r.choice([100, 200, 500, 1000]); T = r.choice([20, 30, 15]); k = r.choice([2, 3, 4, 5]); N = N0 * 2 ** k
    return dict(en='A bacteria colony doubles every %d minutes: \\(N(t)=%d\\cdot2^{t/%d}\\). After %d minutes there are…' % (T, N0, T, k * T), vi='Một đàn vi khuẩn tăng gấp đôi sau mỗi %d phút: \\(N(t)=%d\\cdot2^{t/%d}\\). Sau %d phút có…' % (T, N0, T, k * T),
      opts=pick_opts(r, D(N), [D(N0 * 2 * k), D(N // 2), D(N * 2), D(N0 * k)]), ans=0, ee='\\(%d\\cdot2^{%d}=%s\\).' % (N0, k, DE(N)), ev='\\(%d\\cdot2^{%d}=%s\\).' % (N0, k, D(N)))
def f_car(r, lv):
    V0 = r.choice([500, 600, 800, 1000]); p = r.choice([10, 20]); n = r.choice([2, 3]); V = F(V0) * F(100 - p, 100) ** n
    return dict(en='A car worth %d million VND loses %d%% of its value each year: \\(V(n)=%d(1-0{,}%02d)^n\\). After %d years it is worth… (million VND)' % (V0, p, V0, p, n), vi='Một ô tô giá %d triệu đồng, mỗi năm mất %d%% giá trị: \\(V(n)=%d(1-0{,}%02d)^n\\). Sau %d năm còn… (triệu đồng)' % (V0, p, V0, p, n),
      opts=pick_opts(r, D(V), [D(V0 * (1 - F(p * n, 100))), D(V * F(100 - p, 100)), D(V0 - p * n), D(V / F(100 - p, 100) if n > 1 else V0)]), ans=0,
      ee='\\(%d\\cdot%s^{%d}=%s\\).' % (V0, DE(F(100 - p, 100)), n, DE(V)), ev='\\(%d\\cdot%s^{%d}=%s\\).' % (V0, D(F(100 - p, 100)), n, D(V)))
def f_cmp(r, lv):
    b = r.choice([2, 3, '\\frac12', '0{,}3']); x, y = r.sample([3, 5, 7, '\\sqrt2', '\\pi'], 2)
    val = {3: 3, 5: 5, 7: 7, '\\sqrt2': 1.414, '\\pi': 3.1416}; inc = b in (2, 3)
    g = (val[x] > val[y]) == inc
    rel = lambda gg: '\\log_{%s}%s%s\\log_{%s}%s' % (b, x, '\\gt' if gg else '\\lt', b, y)
    return dict(en='Which is true?  (compare \\(\\log_{%s}%s\\), \\(\\log_{%s}%s\\))' % (b, x, b, y), vi='Khẳng định nào đúng? (so sánh \\(\\log_{%s}%s\\) và \\(\\log_{%s}%s\\))' % (b, x, b, y),
      opts=pick_opts(r, rel(g), [rel(not g), '\\log_{%s}%s=\\log_{%s}%s' % (b, x, b, y), '\\log_{%s}%s\\lt0' % (b, x) if inc else '\\log_{%s}%s\\gt0' % (b, x)]), ans=0,
      ee='\\(y=\\log_{%s}x\\) is %s.' % (b, 'increasing' if inc else 'decreasing'), ev='Hàm \\(y=\\log_{%s}x\\) %s.' % (b, 'đồng biến' if inc else 'nghịch biến'))
def f_range(r, lv):
    k = r.randint(-3, 4); a = r.choice([2, 3, 5]); kind = r.choice(['exp', 'log'])
    if kind == 'exp': f = 'y=%d^x%+d' % (a, k) if k else 'y=%d^x' % a; ok = '(%d;\\,+\\infty)' % k; w = ['[%d;\\,+\\infty)' % k, '\\mathbb R', '(0;\\,+\\infty)' if k else '(1;\\,+\\infty)', '(%d;\\,+\\infty)' % (k + 1)]
    else: f = 'y=\\log_{%d}x%+d' % (a, k) if k else 'y=\\log_{%d}x' % a; ok = '\\mathbb R'; w = ['(0;\\,+\\infty)', '(%d;\\,+\\infty)' % k if k else '(1;\\,+\\infty)', '[%d;\\,+\\infty)' % k, '\\mathbb R\\setminus\\{0\\}']
    return dict(en='The range of \\(%s\\) is…' % f, vi='Tập giá trị của hàm số \\(%s\\) là…' % f, opts=pick_opts(r, ok, w), ans=0,
      ee='\\(a^x\\) takes all values in \\((0;+\\infty)\\); \\(\\log_a x\\) takes all real values.', ev='\\(a^x\\) nhận mọi giá trị thuộc \\((0;+\\infty)\\); \\(\\log_a x\\) nhận mọi giá trị thực.')
M20S11 = [f_dom, f_mono, f_base, f_point, f_bact, f_car, f_cmp, f_range]
# ================= Bài 21. Phương trình, bất phương trình mũ và lôgarit =================
def eq_exp1(r, lv):
    a = r.choice([2, 3, 5]); m = r.choice([1, 2, 3]); n = r.randint(-3, 3); k = r.choice([-2, -1, 2, 3, 4])
    if (k - n) % m: raise AssertionError
    x = (k - n) // m; R = frn(F(a) ** k)
    return dict(en='Solve \\(%d^{%s}=%s\\).' % (a, ('%dx' % m if m > 1 else 'x') + ('%+d' % n if n else ''), R), vi='Giải phương trình \\(%d^{%s}=%s\\).' % (a, ('%dx' % m if m > 1 else 'x') + ('%+d' % n if n else ''), R),
      opts=pick_opts(r, 'x=%d' % x, ['x=%d' % (x + 1), 'x=%d' % (-x) if x else 'x=1', 'x=%s' % frn(F(k + n, m)) if F(k + n, m) != x else 'x=%d' % (x - 1), 'x=%d' % k]), ans=0,
      ee='\\(%s=%d^{%d}\\Rightarrow %s=%d\\).' % (R, a, k, ('%dx' % m if m > 1 else 'x') + ('%+d' % n if n else ''), k), ev='\\(%s=%d^{%d}\\) nên \\(%s=%d\\).' % (R, a, k, ('%dx' % m if m > 1 else 'x') + ('%+d' % n if n else ''), k))
def eq_exp2(r, lv):
    p, q = sorted(r.sample(range(-3, 5), 2)); a = r.choice([2, 3]); k = r.choice([0, 1, 2, -1])
    # a^{x^2-(p+q)x} = a^{-pq}  với  hằng số dịch k: a^{x^2-(p+q)x+k} = a^{k-pq}
    e = poly([1, -(p + q), k])
    R = frn(F(a) ** (k - p * q))
    return dict(en='Solve \\(%d^{%s}=%s\\).' % (a, e, R), vi='Giải phương trình \\(%d^{%s}=%s\\).' % (a, e, R),
      opts=pick_opts(r, 'S=\\{%d;\\,%d\\}' % (p, q), ['S=\\{%d;\\,%d\\}' % (-q, -p), 'S=\\{%d\\}' % q, 'S=\\varnothing', 'S=\\{%d;\\,%d\\}' % (p - 1, q + 1)]), ans=0,
      ee='Exponents: \\(%s=%d\\iff(%s)(%s)=0\\).' % (e, k - p * q, fac(p), fac(q)), ev='So sánh số mũ: \\(%s=%d\\iff(%s)(%s)=0\\).' % (e, k - p * q, fac(p), fac(q)))
def eq_log1(r, lv):
    a = r.choice([2, 3, 5]); c = r.choice([1, 2, 3]); b = r.randint(-4, 4); m = r.choice([1, 2]); v = a ** c - b
    if v % m: raise AssertionError
    x = v // m; inside = ('%dx' % m if m > 1 else 'x') + ('%+d' % b if b else '')
    return dict(en='Solve \\(\\log_{%d}(%s)=%d\\).' % (a, inside, c), vi='Giải phương trình \\(\\log_{%d}(%s)=%d\\).' % (a, inside, c),
      opts=pick_opts(r, 'x=%d' % x, ['x=%s' % frn(F(a * c - b, m)), 'x=%s' % frn(F(c ** a - b, m)), 'x=%d' % (x + 1), 'x=%s' % frn(F(a ** c + b, m))]), ans=0,
      ee='\\(%s=%d^{%d}=%d\\).' % (inside, a, c, a ** c), ev='\\(%s=%d^{%d}=%d\\Rightarrow x=%d\\) (thỏa \\(%s\\gt0\\)).' % (inside, a, c, a ** c, x, inside))
def eq_log2(r, lv):
    # log_a(x^2 + px) = log_a(qx + s): x^2 + (p-q)x - s = 0 nghiệm u, v; loại nghiệm làm qx+s ≤ 0
    u, v = sorted(r.sample(range(-4, 6), 2)); q = r.choice([1, 2, 3]); s = r.randint(-3, 6); p = q - (u + v); s0 = -u * v
    if s != s0: s = s0
    ok_roots = [x for x in (u, v) if q * x + s > 0]
    if not ok_roots or len(ok_roots) == 2: raise AssertionError
    lhs = poly([1, p, 0]); rhs = ('%dx' % q if q > 1 else 'x') + ('%+d' % s if s else '')
    return dict(en='Solve \\(\\log_2(%s)=\\log_2(%s)\\).' % (lhs, rhs), vi='Giải phương trình \\(\\log_2(%s)=\\log_2(%s)\\).' % (lhs, rhs),
      opts=pick_opts(r, 'S=\\{%d\\}' % ok_roots[0], ['S=\\{%d;\\,%d\\}' % (u, v), 'S=\\{%d\\}' % ([x for x in (u, v) if x != ok_roots[0]][0]), 'S=\\varnothing', 'S=\\{%d\\}' % (ok_roots[0] + 1)]), ans=0,
      ee='\\(%s=%s\\): roots %d, %d; need \\(%s\\gt0\\).' % (lhs, rhs, u, v, rhs), ev='\\(%s=%s\\): nghiệm %d, %d; cần \\(%s\\gt0\\).' % (lhs, rhs, u, v, rhs))
def in_exp(r, lv):
    a = r.choice([2, 3, F(1, 2), F(1, 3)]); k = r.choice([-2, -1, 2, 3]); R = frn(F(a) ** k); rel = r.choice(['\\gt', '\\ge', '\\lt', '\\le'])
    inc = a > 1; flip = {'\\gt': '\\lt', '\\lt': '\\gt', '\\ge': '\\le', '\\le': '\\ge'}; rr = rel if inc else flip[rel]
    base = str(a) if F(a).denominator == 1 else '\\left(%s\\right)' % frn(a)
    return dict(en='Solve \\(%s^x%s%s\\).' % (base, rel, R), vi='Giải bất phương trình \\(%s^x%s%s\\).' % (base, rel, R),
      opts=pick_opts(r, 'x%s%d' % (rr, k), ['x%s%d' % (flip[rr], k), 'x%s%d' % (rr, -k), 'x%s%s' % (rr, R) if R != str(k) else 'x%s%d' % (rr, k + 1)]), ans=0,
      ee='\\(%s=%s^{%d}\\); the base is %s 1.' % (R, base, k, 'greater than' if inc else 'less than'), ev='\\(%s=%s^{%d}\\); cơ số %s 1 %s.' % (R, base, k, 'lớn hơn' if inc else 'nhỏ hơn', 'nên giữ chiều' if inc else 'nên đổi chiều'))
def in_log(r, lv):
    a = r.choice([2, 3, F(1, 2), F(1, 3)]); c = r.choice([1, 2, 3, -1]); b = r.randint(-3, 3)
    inside = 'x' + ('%+d' % b if b else ''); T = F(a) ** c; lo = -b
    if a > 1: ok = '%d\\lt x\\lt%s' % (lo, frn(T - b)) ; w = ['x\\lt%s' % frn(T - b), 'x\\gt%s' % frn(T - b), '%d\\lt x\\lt%s' % (lo, frn(c - b))]
    else: ok = 'x\\gt%s' % frn(T - b); w = ['%d\\lt x\\lt%s' % (lo, frn(T - b)), 'x\\lt%s' % frn(T - b), 'x\\gt%s' % frn(c - b)]
    if T - b <= lo: raise AssertionError
    return dict(en='Solve \\(%s\\lt%d\\).' % (lg(a, '(%s)' % inside), c), vi='Giải bất phương trình \\(%s\\lt%d\\).' % (lg(a, '(%s)' % inside), c),
      opts=pick_opts(r, ok, w), ans=0,
      ee='Domain \\(x\\gt%d\\); \\(%d=%s\\).' % (lo, c, lg(a, frn(T))), ev='Điều kiện \\(x\\gt%d\\); \\(%d=%s\\); cơ số %s 1.' % (lo, c, lg(a, frn(T)), 'lớn hơn' if a > 1 else 'nhỏ hơn'))
def eq_sub(r, lv):
    a = r.choice([2, 3]); i, j = r.sample([0, 1, 2], 2); u, v = a ** i, a ** j
    e = '%d^x-%d\\cdot%d^x+%d=0' % (a * a, u + v, a, u * v)
    return dict(en='The sum of the solutions of \\(%s\\) is…' % e, vi='Tổng các nghiệm của phương trình \\(%s\\) là…' % e,
      opts=pick_opts(r, str(i + j), [str(u + v), str(u * v), str(i * j) if i * j != i + j else str(i + j + 2), str(i + j + 1)]), ans=0,
      ee='\\(t=%d^x\\gt0\\): \\(t^2-%dt+%d=0\\Rightarrow t=%d,\\ t=%d\\Rightarrow x=%d,\\ x=%d\\).' % (a, u + v, u * v, u, v, i, j), ev='Đặt \\(t=%d^x\\gt0\\): \\(t^2-%dt+%d=0\\Rightarrow t=%d,\\ t=%d\\Rightarrow x=%d,\\ x=%d\\).' % (a, u + v, u * v, u, v, i, j))
def eq_time(r, lv):
    rate = r.choice([5, 6, 7, 8, 10, 12]); k = r.choice([2, 3])
    n = 0; v = F(1)
    while v < k: n += 1; v *= F(100 + rate, 100)
    return dict(en='Money is saved at %d%%/year compound interest. After at least how many full years is it at least %d times the deposit?' % (rate, k), vi='Gửi tiết kiệm lãi kép %d%%/năm. Sau ít nhất bao nhiêu năm (tròn năm) số tiền ít nhất gấp %d lần số tiền gửi?' % (rate, k),
      opts=pick_opts(r, str(n), [str(n - 1), str(n + 1), str(math.ceil(100 * (k - 1) / rate)) if math.ceil(100 * (k - 1) / rate) not in (n, n - 1, n + 1) else str(n + 2), str(n + 3)]), ans=0,
      ee='\\(n\\ge\\log_{%s}%d\\approx%s\\).' % (DE(F(100 + rate, 100)), k, ('%.2f' % (math.log(k) / math.log(1 + rate / 100)))), ev='\\((1+%s)^n\\ge%d\\iff n\\ge\\log_{%s}%d\\approx%s\\).' % (D(F(rate, 100)), k, D(F(100 + rate, 100)), k, ('%.2f' % (math.log(k) / math.log(1 + rate / 100))).replace('.', '{,}')))
M21S11 = [eq_exp1, eq_exp2, eq_log1, eq_log2, in_exp, in_log, eq_sub, eq_time]
