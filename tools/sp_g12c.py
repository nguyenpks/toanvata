# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 12 – Bài 10 (phương sai, độ lệch chuẩn), Bài 11 (nguyên hàm), Bài 12 (tích phân).
Mọi đáp án do máy tính tính: bảng ghép nhóm bằng GT (Fraction), đa thức/nguyên hàm bằng hệ số Fraction, tích phân bằng công thức Newton–Leibniz chính xác."""
import functools, math, random
from fractions import Fraction as F
from mb_selfpractice import pick_opts, fr
from mb_lib import TI
from gdata import GT
from freqtable import num

def TT(en, vi): return '§' + TI(en, vi)
def D(x): return num(F(x))                     # dấu phẩy thập phân
def DE(x): return num(F(x), comma=False)       # dấu chấm (tiếng Anh)
def r2(x): return F(round(float(x) * 100)) / 100    # làm tròn 2 chữ số thập phân (để hiển thị)

# ================= Bài 10. Phương sai và độ lệch chuẩn (mẫu ghép nhóm) =================
def vtable(seed, sq=False):
    """Bảng ghép nhóm có trung bình là bội của 0,5 và phương sai có tối đa 2 chữ số thập phân; sq=True: phương sai là số chính phương."""
    r = random.Random(seed)
    for _ in range(300000):
        h = r.choice([2, 4, 5, 10]); k = r.choice([4, 5]); fs = [r.randint(1, 12) for _ in range(k)]; n = sum(fs)
        if n < 15 or n > 50 or max(fs) > 4 * min(fs): continue
        t = GT(r.choice([0, 10, 20, 40, 50, 60, 100, 150]), h, fs); m, v = t.mean(), t.var()
        if (2 * m).denominator != 1 or (100 * v).denominator != 1 or v == 0: continue
        if sq and not (v.denominator == 1 and math.isqrt(v.numerator) ** 2 == v.numerator): continue
        return t
    raise RuntimeError('vtable')
@functools.lru_cache(maxsize=None)
def VT(seed, sq=False): return vtable(seed, sq)
def _vt(r, sq=False): return VT(r.randint(1, 400), sq)
def mids(t): return ', '.join(D(t.mid(i)) for i in range(t.k))
def v_var(r, lv):
    t = _vt(r); m, v = t.mean(), t.var(); ex2 = sum(f * t.mid(i) ** 2 for i, f in enumerate(t.fs)) / t.n
    return dict(en='A grouped frequency table: %s. The variance \\(s^2\\) of the sample is…' % t.html(rows=('group', 'freq')), vi='Cho mẫu số liệu ghép nhóm: %s. Phương sai \\(s^2\\) của mẫu là…' % t.html(rows=('group', 'freq')),
      opts=pick_opts(r, D(v), [D(ex2), D(v * t.n / (t.n - 1)) if (v * t.n / (t.n - 1) * 100).denominator == 1 else D(v + 1), D(r2(math.sqrt(v))), D(v * 2)], fill=lambda k: D(v + k)), ans=0,
      ee='Midpoints \\(%s\\); \\(\\bar x=%s\\); \\(s^2=\\dfrac1n\\sum n_ix_i^2-\\bar x^2=%s-%s=%s\\).' % (mids(t).replace('{,}', '.'), DE(m), DE(ex2), DE(m * m), DE(v)),
      ev='Giá trị đại diện \\(%s\\); \\(\\bar x=%s\\); \\(s^2=\\dfrac1n\\sum n_ix_i^2-\\bar x^2=%s-%s=%s\\).' % (mids(t), D(m), D(ex2), D(m * m), D(v)))
def v_std(r, lv):
    t = _vt(r, sq=True); v = t.var(); s = math.isqrt(v.numerator)
    return dict(en='A grouped frequency table: %s. The standard deviation \\(s\\) is…' % t.html(), vi='Cho mẫu số liệu ghép nhóm: %s. Độ lệch chuẩn \\(s\\) của mẫu là…' % t.html(),
      opts=pick_opts(r, str(s), [D(v), str(s + 1), D(t.mean()), str(max(s - 1, 1)) if s > 1 else '0{,}5'], fill=lambda k: str(s + 2 * k)), ans=0,
      ee='\\(s^2=%s\\), so \\(s=\\sqrt{%s}=%d\\).' % (DE(v), DE(v), s), ev='\\(s^2=%s\\) nên \\(s=\\sqrt{%s}=%d\\).' % (D(v), D(v), s))
def v_formula(r, lv):
    n = r.choice([20, 25, 40, 50]); m = F(r.randint(20, 80)); v = F(r.choice([4, 9, 16, 25, 36, 6, 12, 2]) * r.choice([1, 1, 2])); S2 = n * (v + m * m)
    return dict(en='For a sample of size \\(n=%d\\), the midpoints give \\(\\sum n_ix_i=%s\\) and \\(\\sum n_ix_i^2=%s\\). The variance is…' % (n, D(n * m), D(S2)), vi='Một mẫu có cỡ \\(n=%d\\); theo các giá trị đại diện, \\(\\sum n_ix_i=%s\\) và \\(\\sum n_ix_i^2=%s\\). Phương sai bằng…' % (n, D(n * m), D(S2)),
      opts=pick_opts(r, D(v), [D(S2 / n), D(v * n / (n - 1)) if (v * n / (n - 1) * 100).denominator == 1 else D(v + 2), D(m), D(v + m)], fill=lambda k: D(v + 3 * k)), ans=0,
      ee='\\(\\bar x=%s\\); \\(s^2=\\dfrac{%s}{%d}-%s^2=%s\\).' % (DE(m), DE(S2), n, DE(m), DE(v)), ev='\\(\\bar x=%s\\); \\(s^2=\\dfrac{%s}{%d}-%s^2=%s\\).' % (D(m), D(S2), n, D(m), D(v)))
CTX = [(('two rice fields', 'hai ruộng lúa'), ('yield (quintals per hectare)', 'năng suất (tạ/ha)'), ('more stable yield', 'năng suất ổn định hơn')),
       (('two shooters', 'hai xạ thủ'), ('score', 'điểm bắn'), ('more consistent', 'bắn ổn định hơn')),
       (('two machines filling bottles', 'hai máy chiết rót'), ('volume (ml)', 'thể tích (ml)'), ('more uniform', 'đồng đều hơn')),
       (('two classes', 'hai lớp học'), ('test score', 'điểm kiểm tra'), ('more even', 'đồng đều hơn'))]
def v_compare(r, lv):
    c = r.choice(CTX); s1, s2 = r.sample([F(x, 10) for x in (8, 12, 15, 21, 25, 31, 36, 42)], 2); m1, m2 = r.choice([(F(52), F(53)), (F(75), F(74)), (F(8), F(8)), (F(500), F(501))])
    a_better = s1 < s2; nm = ('A', 'B')
    o = {x: TT('%s: smaller standard deviation' % x, '%s: độ lệch chuẩn nhỏ hơn' % x) for x in nm}
    o2 = {x: TT('%s: larger mean' % x, '%s: số trung bình lớn hơn' % x) for x in nm}
    win = 'A' if a_better else 'B'; lose = 'B' if a_better else 'A'
    big_mean = 'A' if m1 > m2 else 'B'
    wrong = [o[lose], o2[big_mean] if big_mean != win else o2[lose], TT('Both are equally stable', 'Hai mẫu ổn định như nhau')]
    return dict(en='%s: A has mean \\(%s\\) and \\(s=%s\\); B has mean \\(%s\\) and \\(s=%s\\) (%s). Which is %s?' % (c[0][0].capitalize(), DE(m1), DE(s1), DE(m2), DE(s2), c[1][0], c[2][0]),
      vi='%s: A có trung bình \\(%s\\), \\(s=%s\\); B có trung bình \\(%s\\), \\(s=%s\\) (%s). Đối tượng nào %s?' % (c[0][1].capitalize(), D(m1), D(s1), D(m2), D(s2), c[1][1], c[2][1]),
      opts=[o[win]] + wrong, ans=0, ee='Stability is measured by the spread: the smaller \\(s\\) wins.', ev='Độ ổn định đo bằng độ phân tán: \\(s\\) nhỏ hơn thì ổn định hơn.')
def v_shift(r, lv):
    s = F(r.choice([12, 15, 24, 32, 18, 25]), 10); kind = r.choice(['add', 'mul', 'mul2'])
    if kind == 'add':
        c = r.choice([2, 5, 10]); ans = s
        en, vi = 'Every value of a sample with \\(s=%s\\) is increased by %d. The new standard deviation is…' % (DE(s), c), 'Mọi giá trị của một mẫu có \\(s=%s\\) đều được cộng thêm %d. Độ lệch chuẩn mới là…' % (D(s), c); wr = [s + c, s * c, s - 1 if s > 1 else s + 2]
        ee, ev = 'Adding a constant moves all data but does not change the spread.', 'Cộng thêm một hằng số làm dữ liệu dịch chuyển nhưng không đổi độ phân tán.'
    else:
        k = 2 if kind == 'mul' else 3; ans = s * k
        en, vi = 'Every value of a sample with \\(s=%s\\) is multiplied by %d. The new standard deviation is…' % (DE(s), k), 'Mọi giá trị của một mẫu có \\(s=%s\\) đều được nhân với %d. Độ lệch chuẩn mới là…' % (D(s), k); wr = [s, s * k * k, s + k]
        ee, ev = 'Multiplying by \\(k\\gt0\\) multiplies \\(s\\) by \\(k\\) and \\(s^2\\) by \\(k^2\\).', 'Nhân với \\(k\\gt0\\) thì \\(s\\) nhân \\(k\\), còn \\(s^2\\) nhân \\(k^2\\).'
    return dict(en=en, vi=vi, opts=pick_opts(r, D(ans), [D(w) for w in wr], fill=lambda q: D(ans + q)), ans=0, ee=ee, ev=ev)
def v_root(r, lv):
    s = r.choice([F(x, 10) for x in (12, 15, 25, 35, 45, 7, 9, 11, 13)] + [F(x) for x in (3, 4, 6, 7, 8)]); v = s * s
    unit = r.choice([('cm', 'cm'), ('kg', 'kg'), ('min', 'phút')])
    return dict(en='The variance of a sample is \\(s^2=%s\\) (%s\\(^2\\)). The standard deviation is…' % (DE(v), unit[0]), vi='Phương sai của một mẫu là \\(s^2=%s\\) (%s\\(^2\\)). Độ lệch chuẩn là…' % (D(v), unit[1]),
      opts=pick_opts(r, '%s\\ \\text{%s}' % (D(s), unit[0]), ['%s\\ \\text{%s}' % (D(w), unit[0]) for w in (v / 2, v, s * 2, s + 1)]), ans=0,
      ee='\\(s=\\sqrt{s^2}=%s\\), in the same unit as the data.' % DE(s), ev='\\(s=\\sqrt{s^2}=%s\\), cùng đơn vị với số liệu.' % D(s))
M10S12 = [v_var, v_std, v_formula, v_compare, v_shift, v_root, v_var, v_formula]

# ================= Bài 11. Nguyên hàm =================
def term(c, p, var='x', first=False):
    """c·x^p dưới dạng TeX (c Fraction, p int hoặc Fraction)."""
    c = F(c)
    if c == 0: return ''
    sgn = '-' if c < 0 else ('' if first else '+'); a = abs(c)
    if p == 0: return sgn + fr(a)
    xs = var if p == 1 else (var + '^{%s}' % (fr(F(p)) if F(p).denominator == 1 else '\\frac{%d}{%d}' % (F(p).numerator, F(p).denominator)))
    if a == 1: return sgn + xs
    if a.denominator == 1: return sgn + '%d%s' % (a.numerator, xs)
    return sgn + '\\dfrac{%d}{%d}%s' % (a.numerator, a.denominator, xs)
def ptex(P, var='x'):
    s = ''
    for p in sorted(P, key=lambda q: -F(q)):
        t = term(P[p], p, var, first=(s == ''))
        s += t
    return s or '0'
def integ(P): return {F(p) + 1: F(c) / (F(p) + 1) for p, c in P.items() if c != 0}
def deriv(P): return {F(p) - 1: F(c) * F(p) for p, c in P.items() if F(p) != 0 and c != 0}
def ev(P, x): return sum(F(c) * F(x) ** int(p) for p, c in P.items())
def a_poly(r, lv):
    P = {2: r.choice([3, 6, -3, 9, 1]), 1: r.choice([2, -4, 4, 6, -2]), 0: r.choice([1, -5, 3, 7, -1])}; I = integ(P)
    w1 = {p: c for p, c in deriv(P).items()}; w2 = {F(p) + 1: F(c) for p, c in P.items()}; w3 = {F(p) + 1: F(c) * (F(p) + 1) for p, c in P.items()}
    return dict(en='\\(\\displaystyle\\int(%s)\\,dx=\\)…' % ptex(P), vi='\\(\\displaystyle\\int(%s)\\,dx=\\)…' % ptex(P),
      opts=pick_opts(r, ptex(I) + '+C', [ptex(w1) + '+C', ptex(w2) + '+C', ptex(w3) + '+C', ptex(I)]), ans=0,
      ee='\\(\\int x^\\alpha dx=\\dfrac{x^{\\alpha+1}}{\\alpha+1}+C\\), term by term.', ev='\\(\\int x^\\alpha dx=\\dfrac{x^{\\alpha+1}}{\\alpha+1}+C\\), lấy từng hạng tử.')
def a_power(r, lv):
    kind = r.choice(['neg', 'sqrt', 'cube']); a = r.choice([1, 2, 3, 4, 6])
    if kind == 'neg':
        f = '\\dfrac{%s}{x^2}' % a; ok = '-\\dfrac{%s}{x}' % a if a != 1 else '-\\dfrac{1}{x}'; wr = ['\\dfrac{%s}{x}' % a, '-\\dfrac{%d}{x^3}' % (2 * a), '%s\\ln|x|' % ('' if a == 1 else a)]
        ee = '\\(\\int x^{-2}dx=\\dfrac{x^{-1}}{-1}+C=-\\dfrac1x+C\\).'
    elif kind == 'sqrt':
        f = '%s\\sqrt{x}' % ('' if a == 1 else a); ok = '%sx\\sqrt{x}' % fr(F(2 * a, 3)) if F(2 * a, 3) != 1 else 'x\\sqrt{x}'; wr = ['\\dfrac{%s}{2\\sqrt x}' % a, '%sx\\sqrt{x}' % fr(F(3 * a, 2)), '%sx^2' % fr(F(a, 2))]
        ee = '\\(\\int x^{\\frac12}dx=\\dfrac{x^{\\frac32}}{\\frac32}+C=\\dfrac23x\\sqrt x+C\\).'
    else:
        f = '%sx^3' % ('' if a == 1 else a); ok = ptex({4: F(a, 4)}); wr = [ptex({2: 3 * a}), ptex({4: a}), ptex({4: F(a, 3)})]
        ee = '\\(\\int x^3dx=\\dfrac{x^4}{4}+C\\).'
    return dict(en='On \\((0;+\\infty)\\), \\(\\displaystyle\\int %s\\,dx=\\)…' % f, vi='Trên \\((0;+\\infty)\\), \\(\\displaystyle\\int %s\\,dx=\\)…' % f, opts=pick_opts(r, ok + '+C', [w + '+C' for w in wr]), ans=0, ee=ee, ev=ee)
def a_trig(r, lv):
    a, b = r.choice([1, 2, 3, -2]), r.choice([1, 2, 4, -3])
    f = '%s\\sin x%s\\cos x' % ({1: '', -1: '-'}.get(a, str(a)), ('+' if b > 0 else '-') + ('' if abs(b) == 1 else str(abs(b))))
    def comb(c1, s1, c2, s2):
        t1 = ({1: '', -1: '-'}.get(c1, str(c1))) + s1; t2 = ('+' if c2 > 0 else '-') + ('' if abs(c2) == 1 else str(abs(c2))) + s2; return t1 + t2 + '+C'
    ok = comb(-a, '\\cos x', b, '\\sin x')
    return dict(en='\\(\\displaystyle\\int(%s)\\,dx=\\)…' % f, vi='\\(\\displaystyle\\int(%s)\\,dx=\\)…' % f,
      opts=pick_opts(r, ok, [comb(a, '\\cos x', b, '\\sin x'), comb(a, '\\cos x', -b, '\\sin x'), comb(-a, '\\cos x', -b, '\\sin x')]), ans=0,
      ee='\\(\\int\\sin x\\,dx=-\\cos x+C\\), \\(\\int\\cos x\\,dx=\\sin x+C\\).', ev='\\(\\int\\sin x\\,dx=-\\cos x+C\\), \\(\\int\\cos x\\,dx=\\sin x+C\\).')
def a_exp(r, lv):
    a = r.choice([2, 3, 5, 10]); k = r.choice([1, 2, 3])
    f = '%se^x+%d^x' % ('' if k == 1 else k, a); ok = '%se^x+\\dfrac{%d^x}{\\ln %d}+C' % ('' if k == 1 else k, a, a)
    wr = ['%se^x+%d^x\\ln %d+C' % ('' if k == 1 else k, a, a), '%se^x+x\\cdot%d^{x-1}+C' % ('' if k == 1 else k, a), '%se^{x+1}+\\dfrac{%d^{x+1}}{x+1}+C' % ('' if k == 1 else k, a)]
    return dict(en='\\(\\displaystyle\\int(%s)\\,dx=\\)…' % f, vi='\\(\\displaystyle\\int(%s)\\,dx=\\)…' % f, opts=pick_opts(r, ok, wr), ans=0,
      ee='\\(\\int e^xdx=e^x+C\\), \\(\\int a^xdx=\\dfrac{a^x}{\\ln a}+C\\).', ev='\\(\\int e^xdx=e^x+C\\), \\(\\int a^xdx=\\dfrac{a^x}{\\ln a}+C\\).')
def a_init(r, lv):
    P = {1: r.choice([2, 4, 6, -2]), 0: r.choice([1, -3, 5, 2])}; x0, y0, x1 = r.choice([0, 1]), r.randint(-3, 5), r.choice([2, 3, -1])
    I = integ(P); C = y0 - ev(I, x0); val = ev(I, x1) + C
    return dict(en='\\(F(x)\\) is an antiderivative of \\(f(x)=%s\\) with \\(F(%d)=%d\\). Then \\(F(%d)=\\)…' % (ptex(P), x0, y0, x1), vi='Biết \\(F(x)\\) là một nguyên hàm của \\(f(x)=%s\\) và \\(F(%d)=%d\\). Khi đó \\(F(%d)=\\)…' % (ptex(P), x0, y0, x1),
      opts=pick_opts(r, fr(val), [fr(ev(I, x1)), fr(ev(P, x1) + y0), fr(val + 1), fr(-val) if val else '1'], fill=lambda k: fr(val + 2 * k)), ans=0,
      ee='\\(F(x)=%s+C\\), \\(F(%d)=%d\\Rightarrow C=%s\\); \\(F(%d)=%s\\).' % (ptex(I), x0, y0, fr(C), x1, fr(val)), ev='\\(F(x)=%s+C\\), \\(F(%d)=%d\\Rightarrow C=%s\\); \\(F(%d)=%s\\).' % (ptex(I), x0, y0, fr(C), x1, fr(val)))
def a_check(r, lv):
    I = {3: r.choice([1, 2, -1]), 1: r.choice([-2, 3, 5]), 0: r.choice([4, -7, 1])}; f = deriv(I)
    return dict(en='Which function is an antiderivative of \\(f(x)=%s\\)?' % ptex(f), vi='Hàm số nào là một nguyên hàm của \\(f(x)=%s\\)?' % ptex(f),
      opts=pick_opts(r, 'F(x)=' + ptex(I), ['F(x)=' + ptex(deriv(f)), 'F(x)=' + ptex({F(p) + 1: c for p, c in f.items()}), 'F(x)=' + ptex({3: I[3], 1: -I[1], 0: I[0]})]), ans=0,
      ee='Check \\(F′(x)=f(x)\\): \\((%s)′=%s\\).' % (ptex(I), ptex(f)), ev='Kiểm tra \\(F′(x)=f(x)\\): \\((%s)′=%s\\).' % (ptex(I), ptex(f)))
def a_motion(r, lv):
    a = r.choice([2, 3, 4, F(1, 2), F(3, 2)]); v0 = r.choice([0, 2, 5, 10]); T = r.choice([4, 6, 8, 10]); s = v0 * T + a * T * T / 2
    return dict(en='A car starts with velocity \\(%s\\ \\text{m/s}\\) and accelerates with \\(a=%s\\ \\text{m/s}^2\\). How far does it travel in the first \\(%d\\) s?' % (v0, DE(a), T), vi='Một ô tô có vận tốc ban đầu \\(%s\\ \\text{m/s}\\), tăng tốc với gia tốc \\(a=%s\\ \\text{m/s}^2\\). Quãng đường đi được trong \\(%d\\) giây đầu là…' % (v0, D(a), T),
      opts=pick_opts(r, '%s\\ \\text{m}' % D(s), ['%s\\ \\text{m}' % D(w) for w in (v0 * T + a * T * T, v0 + a * T, a * T * T / 2, s + T)]), ans=0,
      ee='\\(v(t)=%s+%st\\), \\(s(t)=\\int v\\,dt=%st+\\dfrac{%s}{2}t^2\\) (\\(s(0)=0\\)); \\(s(%d)=%s\\).' % (v0, DE(a), v0, DE(a), T, DE(s)), ev='\\(v(t)=%s+%st\\), \\(s(t)=\\int v\\,dt=%st+\\dfrac{%s}{2}t^2\\) (\\(s(0)=0\\)); \\(s(%d)=%s\\).' % (v0, D(a), v0, D(a), T, D(s)))
def a_cost(r, lv):
    a, b = r.choice([(10, F(1, 5)), (20, F(1, 10)), (5, F(2, 5)), (8, F(1, 2))]); C0 = r.choice([100, 200, 500]); X = r.choice([10, 20, 50])
    val = C0 + a * X + b * X * X / 2
    return dict(en='The marginal cost of a workshop is \\(C′(x)=%d+%sx\\) (thousand VND per product) and the fixed cost is \\(C(0)=%d\\) thousand VND. The cost of making \\(%d\\) products is…' % (a, DE(b), C0, X),
      vi='Chi phí biên của một xưởng là \\(C′(x)=%d+%sx\\) (nghìn đồng/sản phẩm), chi phí cố định \\(C(0)=%d\\) nghìn đồng. Chi phí sản xuất \\(%d\\) sản phẩm là…' % (a, D(b), C0, X),
      opts=pick_opts(r, D(val), [D(a * X + b * X * X / 2), D(C0 + a * X + b * X * X), D(C0 + a + b * X), D(val + C0)]), ans=0,
      ee='\\(C(x)=%d+%dx+%sx^2\\); \\(C(%d)=%s\\).' % (C0, a, DE(b / 2), X, DE(val)), ev='\\(C(x)=%d+%dx+%sx^2\\); \\(C(%d)=%s\\).' % (C0, a, D(b / 2), X, D(val)))
M11S12 = [a_poly, a_power, a_trig, a_exp, a_init, a_check, a_motion, a_cost]

# ================= Bài 12. Tích phân =================
def defint(P, a, b): I = integ(P); return ev(I, b) - ev(I, a)
def i_poly(r, lv):
    P = {2: r.choice([3, -3, 6, 1]), 1: r.choice([2, -4, 4, 1]), 0: r.choice([1, -2, 3, 0])}; a, b = r.choice([(0, 1), (0, 2), (1, 2), (-1, 1), (1, 3), (-1, 2)]); v = defint(P, a, b)
    I = integ(P)
    return dict(en='\\(\\displaystyle\\int_{%d}^{%d}(%s)\\,dx=\\)…' % (a, b, ptex(P)), vi='\\(\\displaystyle\\int_{%d}^{%d}(%s)\\,dx=\\)…' % (a, b, ptex(P)),
      opts=pick_opts(r, fr(v), [fr(ev(I, b)), fr(ev(P, b) - ev(P, a)), fr(-v) if v else '1', fr(v + 1)], fill=lambda k: fr(v + 2 * k)), ans=0,
      ee='\\(F(x)=%s\\); \\(F(%d)-F(%d)=%s\\).' % (ptex(I), b, a, fr(v)), ev='\\(F(x)=%s\\); \\(F(%d)-F(%d)=%s\\).' % (ptex(I), b, a, fr(v)))
BASIC = [('\\int_0^{\\frac{\\pi}{2}}\\cos x\\,dx', '1', ['0', '-1', '\\dfrac{\\pi}{2}'], '\\(\\sin x\\Big|_0^{\\pi/2}=1\\).'), ('\\int_0^{\\pi}\\sin x\\,dx', '2', ['0', '-2', '1'], '\\(-\\cos x\\Big|_0^{\\pi}=1+1=2\\).'),
         ('\\int_1^{e}\\dfrac{1}{x}\\,dx', '1', ['e-1', '\\dfrac{1}{e}-1', '0'], '\\(\\ln|x|\\Big|_1^{e}=1\\).'), ('\\int_0^{1}e^x\\,dx', 'e-1', ['e', '1', 'e+1'], '\\(e^x\\Big|_0^1=e-1\\).'),
         ('\\int_0^{\\ln 3}e^x\\,dx', '2', ['3', '\\ln 3', '1'], '\\(e^{\\ln3}-e^0=3-1=2\\).'), ('\\int_1^{2}\\dfrac{1}{x^2}\\,dx', '\\dfrac12', ['-\\dfrac12', '\\dfrac74', '\\ln2'], '\\(-\\dfrac1x\\Big|_1^2=-\\dfrac12+1=\\dfrac12\\).'),
         ('\\int_0^{\\frac{\\pi}{4}}\\dfrac{1}{\\cos^2x}\\,dx', '1', ['0', '\\dfrac{\\pi}{4}', '-1'], '\\(\\tan x\\Big|_0^{\\pi/4}=1\\).'), ('\\int_0^{1}2^x\\,dx', '\\dfrac{1}{\\ln 2}', ['\\ln 2', '1', '2\\ln2'], '\\(\\dfrac{2^x}{\\ln2}\\Big|_0^1=\\dfrac{2-1}{\\ln2}\\).')]
assert abs(math.exp(math.log(3)) - 1 - 2) < 1e-12
def i_basic(r, lv):
    e, ok, wr, ex = r.choice(BASIC)
    return dict(en='\\(\\displaystyle%s=\\)…' % e, vi='\\(\\displaystyle%s=\\)…' % e, opts=pick_opts(r, ok, wr), ans=0, ee=ex, ev=ex)
def i_lin(r, lv):
    A, B = r.randint(-4, 6), r.randint(-5, 5); p, q = r.choice([(2, 3), (3, -1), (1, 2), (2, -3), (4, 1)]); v = p * A + q * B; a, b = r.choice([(0, 2), (1, 4), (-1, 3)])
    ex = '%s f(x)%s g(x)' % ({1: ''}.get(p, str(p)), ('+' if q > 0 else '-') + ('' if abs(q) == 1 else str(abs(q))))
    return dict(en='\\(\\int_{%d}^{%d}f(x)\\,dx=%d\\), \\(\\int_{%d}^{%d}g(x)\\,dx=%d\\). Then \\(\\displaystyle\\int_{%d}^{%d}[%s]\\,dx=\\)…' % (a, b, A, a, b, B, a, b, ex), vi='Cho \\(\\int_{%d}^{%d}f(x)\\,dx=%d\\), \\(\\int_{%d}^{%d}g(x)\\,dx=%d\\). Khi đó \\(\\displaystyle\\int_{%d}^{%d}[%s]\\,dx=\\)…' % (a, b, A, a, b, B, a, b, ex),
      opts=pick_opts(r, str(v), [str(A + B), str(p * A - q * B), str(q * A + p * B), str(v + 1)], fill=lambda k: str(v + 2 * k)), ans=0, ee='Linearity: \\(%d\\cdot%d+(%d)\\cdot(%d)=%d\\).' % (p, A, q, B, v), ev='Tính chất tuyến tính: \\(%d\\cdot%d+(%d)\\cdot(%d)=%d\\).' % (p, A, q, B, v))
def i_split(r, lv):
    a, c, b = r.choice([(0, 2, 5), (1, 3, 6), (-2, 0, 4), (0, 1, 3)]); X, Y = r.randint(-3, 8), r.randint(-5, 9); total = X + Y
    return dict(en='\\(\\int_{%d}^{%d}f(x)\\,dx=%d\\) and \\(\\int_{%d}^{%d}f(x)\\,dx=%d\\). Then \\(\\int_{%d}^{%d}f(x)\\,dx=\\)…' % (a, b, total, a, c, X, c, b), vi='Cho \\(\\int_{%d}^{%d}f(x)\\,dx=%d\\) và \\(\\int_{%d}^{%d}f(x)\\,dx=%d\\). Khi đó \\(\\int_{%d}^{%d}f(x)\\,dx=\\)…' % (a, b, total, a, c, X, c, b),
      opts=pick_opts(r, str(Y), [str(total + X), str(-Y), str(X - total), str(Y + 1)], fill=lambda k: str(Y + 2 * k)), ans=0,
      ee='\\(\\int_{%d}^{%d}=\\int_{%d}^{%d}+\\int_{%d}^{%d}\\Rightarrow %d-%d=%d\\).' % (a, b, a, c, c, b, total, X, Y), ev='\\(\\int_{%d}^{%d}=\\int_{%d}^{%d}+\\int_{%d}^{%d}\\Rightarrow %d-%d=%d\\).' % (a, b, a, c, c, b, total, X, Y))
def i_abs(r, lv):
    m, c = r.choice([(1, 3), (2, 3), (2, 5), (1, 4), (3, 4), (2, 4)]); v = F(m * m + (c - m) ** 2, 2)
    return dict(en='\\(\\displaystyle\\int_0^{%d}|x-%d|\\,dx=\\)…' % (c, m), vi='\\(\\displaystyle\\int_0^{%d}|x-%d|\\,dx=\\)…' % (c, m),
      opts=pick_opts(r, fr(v), [fr(defint({1: 1, 0: -m}, 0, c)), fr(abs(defint({1: 1, 0: -m}, 0, c))) if abs(defint({1: 1, 0: -m}, 0, c)) != v else fr(v + 1), fr(F(c * c, 2)), fr(v + F(1, 2))], fill=lambda k: fr(v + k)), ans=0,
      ee='Split at \\(x=%d\\): \\(\\int_0^{%d}(%d-x)dx+\\int_{%d}^{%d}(x-%d)dx=%s+%s=%s\\).' % (m, m, m, m, c, m, fr(F(m * m, 2)), fr(F((c - m) ** 2, 2)), fr(v)), ev='Tách tại \\(x=%d\\): \\(\\int_0^{%d}(%d-x)dx+\\int_{%d}^{%d}(x-%d)dx=%s+%s=%s\\).' % (m, m, m, m, c, m, fr(F(m * m, 2)), fr(F((c - m) ** 2, 2)), fr(v)))
def i_brake(r, lv):
    v0, a = r.choice([(20, 4), (15, 5), (12, 3), (24, 6), (30, 5), (18, 6)]); T = F(v0, a); s = v0 * T - a * T * T / 2
    return dict(en='A car moving at \\(%d\\ \\text{m/s}\\) brakes; its velocity is \\(v(t)=%d-%dt\\ (\\text{m/s})\\). How far does it go from braking until it stops?' % (v0, v0, a), vi='Ô tô đang chạy \\(%d\\ \\text{m/s}\\) thì hãm phanh; vận tốc \\(v(t)=%d-%dt\\ (\\text{m/s})\\). Từ lúc hãm phanh đến khi dừng, ô tô đi được…' % (v0, v0, a),
      opts=pick_opts(r, '%s\\ \\text{m}' % D(s), ['%s\\ \\text{m}' % D(w) for w in (v0 * T, 2 * s, T, s + v0)]), ans=0,
      ee='Stops when \\(v=0\\): \\(t=%s\\). \\(s=\\int_0^{%s}(%d-%dt)\\,dt=%s\\).' % (DE(T), DE(T), v0, a, DE(s)), ev='Dừng khi \\(v=0\\): \\(t=%s\\). \\(s=\\int_0^{%s}(%d-%dt)\\,dt=%s\\).' % (D(T), D(T), v0, a, D(s)))
def i_tank(r, lv):
    a, b, T = r.choice([(20, 2, 10), (30, 4, 5), (10, 1, 20), (50, 6, 10), (12, 3, 8)]); V = a * T + b * T * T / 2
    return dict(en='Water flows into a tank at the rate \\(r(t)=%d+%dt\\) (litres per minute). How much water flows in during the first \\(%d\\) minutes?' % (a, b, T), vi='Nước chảy vào bể với tốc độ \\(r(t)=%d+%dt\\) (lít/phút). Trong \\(%d\\) phút đầu, lượng nước chảy vào bể là…' % (a, b, T),
      opts=pick_opts(r, '%s\\ \\text{l}' % D(V), ['%s\\ \\text{l}' % D(w) for w in (a + b * T, (a + b * T) * T, a * T + b * T * T, V - a * T)]), ans=0,
      ee='Total change \\(=\\int_0^{%d}r(t)\\,dt=%d\\cdot%d+\\dfrac{%d}{2}\\cdot%d^2=%s\\).' % (T, a, T, b, T, DE(V)), ev='Tổng lượng biến thiên \\(=\\int_0^{%d}r(t)\\,dt=%d\\cdot%d+\\dfrac{%d}{2}\\cdot%d^2=%s\\).' % (T, a, T, b, T, D(V)))
def i_swap(r, lv):
    a, b = r.choice([(1, 4), (0, 3), (-2, 2), (2, 5)]); X = r.choice([-6, -3, 2, 5, 7, 9]); k = r.choice([1, 2, 3])
    v = -k * X
    return dict(en='\\(\\int_{%d}^{%d}f(x)\\,dx=%d\\). Then \\(\\int_{%d}^{%d}%sf(x)\\,dx=\\)…' % (a, b, X, b, a, '' if k == 1 else str(k)), vi='Cho \\(\\int_{%d}^{%d}f(x)\\,dx=%d\\). Khi đó \\(\\int_{%d}^{%d}%sf(x)\\,dx=\\)…' % (a, b, X, b, a, '' if k == 1 else str(k)),
      opts=pick_opts(r, str(v), [str(-v), str(X), str(-X) if -X != v else str(X + k), str(v + 1)], fill=lambda q: str(v + 2 * q)), ans=0,
      ee='\\(\\int_b^a=-\\int_a^b\\), so the result is \\(%d\\cdot(-%s)=%d\\).' % (k, X if X >= 0 else '(%d)' % X, v), ev='\\(\\int_b^a=-\\int_a^b\\) nên kết quả là \\(%d\\cdot(-%s)=%d\\).' % (k, X if X >= 0 else '(%d)' % X, v))
M12S12 = [i_poly, i_basic, i_lin, i_split, i_abs, i_brake, i_tank, i_swap]
