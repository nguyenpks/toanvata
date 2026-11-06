# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 11 – Bài 15 (giới hạn của dãy số), Bài 16 (giới hạn của hàm số). Đáp án tính chính xác bằng Fraction."""
import math
from fractions import Fraction as F
from mb_selfpractice import pick_opts, fr
from mb_lib import TI
from freqtable import num

def TT(en, vi): return '§' + TI(en, vi)
def D(x): return num(F(x))
LN = '\\lim\\limits_{n\\to+\\infty}'
def LX(a): return '\\lim\\limits_{x\\to%s}' % a
def poly(cs, v='n'):
    """cs: hệ số từ bậc cao xuống bậc 0."""
    d = len(cs) - 1; s = ''
    for i, c in enumerate(cs):
        p = d - i
        if c == 0: continue
        sg = '-' if c < 0 else ('+' if s else ''); a = abs(c)
        body = (v if p == 1 else '%s^{%d}' % (v, p)) if p else ''
        coef = '' if (a == 1 and p) else fr(F(a))
        s += sg + coef + body
    return s or '0'
INF = ['+\\infty', '-\\infty', '0', '1']
# ================= Bài 15 =================
def ls_rat(r, lv):
    a, d = r.choice([1, 2, 3, -2, 4, 5]), r.choice([1, 2, 3, -1, 6]); b, c, e, f = (r.randint(-5, 5) for _ in range(4)); kind = r.choice(['same', 'lower'])
    num_ = [a, b, c] if kind == 'same' else [0, a, b]; den = [d, e, f]; v = F(a, d) if kind == 'same' else F(0)
    return dict(en='\\(%s\\dfrac{%s}{%s}=\\)…' % (LN, poly(num_), poly(den)), vi='\\(%s\\dfrac{%s}{%s}=\\)…' % (LN, poly(num_), poly(den)),
      opts=pick_opts(r, fr(v), [fr(F(c, f)) if f else '+\\infty', '+\\infty', fr(F(a, d)) if v == 0 else '0', fr(F(b, e)) if e else '1', fr(v + 1)]), ans=0,
      ee='Divide numerator and denominator by \\(n^2\\) (the highest power of the denominator).', ev='Chia cả tử và mẫu cho \\(n^2\\) (lũy thừa bậc cao nhất của mẫu).')
def ls_deg(r, lv):
    a = r.choice([1, 2, -1, -3, 3]); d = r.choice([1, 2, -1, 4]); b = r.randint(-4, 4); e = r.randint(1, 6)
    v = '+\\infty' if a * d > 0 else '-\\infty'
    return dict(en='\\(%s\\dfrac{%s}{%s}=\\)…' % (LN, poly([a, 0, b]), poly([d, e])), vi='\\(%s\\dfrac{%s}{%s}=\\)…' % (LN, poly([a, 0, b]), poly([d, e])),
      opts=pick_opts(r, v, [x for x in INF if x != v] + [fr(F(a, d))]), ans=0,
      ee='\\(\\dfrac{%s}{%s}=n\\cdot\\dfrac{%d+\\frac{%d}{n^2}}{%d+\\frac{%d}{n}}\\); the second factor tends to \\(%s\\).' % (poly([a, 0, b]), poly([d, e]), a, b, d, e, fr(F(a, d))),
      ev='\\(\\dfrac{%s}{%s}=n\\cdot\\dfrac{%d+\\frac{%d}{n^2}}{%d+\\frac{%d}{n}}\\); thừa số sau dần tới \\(%s\\).' % (poly([a, 0, b]), poly([d, e]), a, b, d, e, fr(F(a, d))))
def ls_geo(r, lv):
    u1 = r.choice([2, 3, 4, 6, 8, 9, 10, 12]); q = r.choice([F(1, 2), F(1, 3), F(-1, 2), F(2, 3), F(1, 4), F(-1, 3)]); S = u1 / (1 - q)
    return dict(en='The sum of the infinite geometric series \\(%s%s+%s+\\dots\\) is…' % (fr(F(u1)), ('+' if q > 0 else '') + fr(u1 * q), fr(u1 * q * q)), vi='Tổng của cấp số nhân lùi vô hạn \\(%s%s+%s+\\dots\\) bằng…' % (fr(F(u1)), ('+' if q > 0 else '') + fr(u1 * q), fr(u1 * q * q)),
      opts=pick_opts(r, fr(S), [fr(u1 / (1 + q)), fr(u1 * q / (1 - q)), fr(F(u1) / q), fr(S + 1)], fill=lambda k: fr(S + 2 * k)), ans=0,
      ee='\\(u_1=%s\\), \\(q=%s\\): \\(S=\\dfrac{u_1}{1-q}=%s\\).' % (u1, fr(q), fr(S)), ev='\\(u_1=%s\\), \\(q=%s\\): \\(S=\\dfrac{u_1}{1-q}=%s\\).' % (u1, fr(q), fr(S)))
def ls_dec(r, lv):
    k = r.choice([1, 2]); p = r.randint(1, 9) if k == 1 else r.randint(10, 98)
    if k == 2 and p % 11 == 0: raise AssertionError
    v = F(p, 10 ** k - 1); per = str(p).zfill(k)
    return dict(en='The repeating decimal \\(0.(%s)=0.%s%s\\dots\\) equals…' % (per, per, per), vi='Số thập phân vô hạn tuần hoàn \\(0{,}(%s)=0{,}%s%s\\dots\\) bằng phân số…' % (per, per, per),
      opts=pick_opts(r, fr(v), [fr(F(p, 10 ** k)), fr(F(p, 10 ** k + 1)), fr(F(p, 10 ** k - 2)) if 10 ** k - 2 else '1', fr(F(p + 1, 10 ** k - 1))]), ans=0,
      ee='\\(\\dfrac{%d}{10^{%d}}+\\dfrac{%d}{10^{%d}}+\\dots\\) is a geometric series with \\(q=10^{-%d}\\): sum \\(=\\dfrac{%d}{%d}=%s\\).' % (p, k, p, 2 * k, k, p, 10 ** k - 1, fr(v)),
      ev='Đây là tổng cấp số nhân lùi vô hạn với \\(u_1=\\dfrac{%d}{10^{%d}}\\), \\(q=10^{-%d}\\): tổng \\(=\\dfrac{%d}{%d}=%s\\).' % (p, k, k, p, 10 ** k - 1, fr(v)))
def ls_exp(r, lv):
    B, b = r.choice([(3, 2), (4, 3), (5, 2), (5, 3)]); a, c = r.choice([1, 2, 3, -1]), r.choice([1, 2, 5, -2]); x, y = r.choice([-3, -1, 1, 2, 4]), r.randint(1, 9)
    v = F(a, c); co = lambda k: {1: '', -1: '-'}.get(k, '%d\\cdot' % k)
    e = '%s\\dfrac{%s%d^n%s%d^n}{%s%d^n+%d}' % (LN, co(a), B, ('+' + co(x)) if x > 0 else co(x), b, co(c), B, y)
    return dict(en='\\(%s=\\)…' % e, vi='\\(%s=\\)…' % e,
      opts=pick_opts(r, fr(v), [fr(F(x, c)), '+\\infty', '0', fr(F(a + x, c)), fr(F(a, y))]), ans=0,
      ee='Divide by \\(%d^n\\); \\(\\left(\\frac{%d}{%d}\\right)^n\\to0\\) and \\(\\frac{%d}{%d^n}\\to0\\).' % (B, b, B, y, B), ev='Chia tử và mẫu cho \\(%d^n\\); \\(\\left(\\frac{%d}{%d}\\right)^n\\to0\\), \\(\\frac{%d}{%d^n}\\to0\\).' % (B, b, B, y, B))
def ls_sqrt(r, lv):
    a = r.choice([2, 4, 6, -2, 3, 5]); v = F(a, 2)
    return dict(en='\\(%s\\left(\\sqrt{n^2%s}-n\\right)=\\)…' % (LN, '+' + poly([a, 0]) if a > 0 else poly([a, 0])), vi='\\(%s\\left(\\sqrt{n^2%s}-n\\right)=\\)…' % (LN, '+' + poly([a, 0]) if a > 0 else poly([a, 0])),
      opts=pick_opts(r, fr(v), [str(a), '0', '+\\infty', fr(-v)]), ans=0,
      ee='Multiply by the conjugate: \\(\\dfrac{%dn}{\\sqrt{n^2%+dn}+n}\\to\\dfrac{%d}{2}\\).' % (a, a, a), ev='Nhân liên hợp: \\(\\dfrac{%dn}{\\sqrt{n^2%+dn}+n}\\to\\dfrac{%d}{2}\\).' % (a, a, a))
def ls_q(r, lv):
    q = r.choice([F(2, 3), F(-1, 2), F(5, 4), F(3, 2), F(1, 5), F(-3, 4)])
    v = '0' if abs(q) < 1 else '+\\infty'
    return dict(en='\\(%s\\left(%s\\right)^n=\\)…' % (LN, fr(q)), vi='\\(%s\\left(%s\\right)^n=\\)…' % (LN, fr(q)),
      opts=pick_opts(r, v, [x for x in ('0', '+\\infty', '1', '-\\infty') if x != v]), ans=0,
      ee='\\(\\lim q^n=0\\) if \\(|q|\\lt1\\); \\(\\lim q^n=+\\infty\\) if \\(q\\gt1\\).', ev='\\(\\lim q^n=0\\) nếu \\(|q|\\lt1\\); \\(\\lim q^n=+\\infty\\) nếu \\(q\\gt1\\).')
def ls_ball(r, lv):
    h = r.choice([2, 3, 4, 5, 6, 10]); q = r.choice([F(1, 2), F(1, 3), F(2, 3), F(3, 4)]); T = h + 2 * h * q / (1 - q)
    return dict(en='A ball is dropped from \\(%d\\) m. After each bounce it rises to \\(%s\\) of the previous height. The total distance it travels (until it stops) is…' % (h, fr(q)),
      vi='Thả một quả bóng từ độ cao \\(%d\\) m. Sau mỗi lần chạm đất, bóng nảy lên bằng \\(%s\\) độ cao trước đó. Tổng quãng đường bóng đi được đến khi dừng là…' % (h, fr(q)),
      opts=pick_opts(r, fr(T) + '\\ \\text{m}', [fr(h / (1 - q)) + '\\ \\text{m}', fr(2 * h / (1 - q)) + '\\ \\text{m}', fr(h * (1 + 2 * q)) + '\\ \\text{m}', fr(T + 1) + '\\ \\text{m}']), ans=0,
      ee='Down \\(%d\\) m, then up and down each bounce: \\(%d+2\\cdot\\dfrac{%d\\cdot%s}{1-%s}=%s\\).' % (h, h, h, fr(q), fr(q), fr(T)), ev='Rơi \\(%d\\) m, sau đó mỗi lần nảy đi lên rồi xuống: \\(%d+2\\cdot\\dfrac{%d\\cdot%s}{1-%s}=%s\\).' % (h, h, h, fr(q), fr(q), fr(T)))
M15S11 = [ls_rat, ls_deg, ls_geo, ls_dec, ls_exp, ls_sqrt, ls_q, ls_ball]
# ================= Bài 16 =================
def lf_sub(r, lv):
    a = r.randint(-3, 3); cs = [r.choice([1, 2, -1, 3]), r.randint(-5, 5), r.randint(-6, 6)]; v = cs[0] * a * a + cs[1] * a + cs[2]
    return dict(en='\\(%s(%s)=\\)…' % (LX(a), poly(cs, 'x')), vi='\\(%s(%s)=\\)…' % (LX(a), poly(cs, 'x')), opts=pick_opts(r, str(v), [str(v + 1), str(-v) if v else '1', str(cs[2]), str(v - 2)]), ans=0,
      ee='A polynomial is continuous: substitute \\(x=%d\\).' % a, ev='Hàm đa thức: thay trực tiếp \\(x=%d\\).' % a)
def lf_fac(r, lv):
    a, b = r.randint(-4, 5), r.randint(-4, 5)
    if a == b: raise AssertionError
    v = a - b
    return dict(en='\\(%s\\dfrac{%s}{x%s}=\\)…' % (LX(a), poly([1, -(a + b), a * b], 'x'), '%+d' % -a if a else ''), vi='\\(%s\\dfrac{%s}{x%s}=\\)…' % (LX(a), poly([1, -(a + b), a * b], 'x'), '%+d' % -a if a else ''),
      opts=pick_opts(r, str(v), [str(a + b), str(b - a), '0', str(a), str(v + 1)]), ans=0,
      ee='\\(\\dfrac{(x%s)(x%s)}{x%s}=x%s\\to%d\\).' % ('%+d' % -a, '%+d' % -b, '%+d' % -a, '%+d' % -b, v), ev='\\(\\dfrac{(x%s)(x%s)}{x%s}=x%s\\to%d\\).' % ('%+d' % -a, '%+d' % -b, '%+d' % -a, '%+d' % -b, v))
def lf_conj(r, lv):
    k = r.choice([1, 2, 3, 4, 5, 6]); c = r.choice([1, 2, 3, 4]); v = F(1, 2 * k * c); den = 'x' if c == 1 else '%dx' % c
    return dict(en='\\(%s\\dfrac{\\sqrt{x+%d}-%d}{%s}=\\)…' % (LX(0), k * k, k, den), vi='\\(%s\\dfrac{\\sqrt{x+%d}-%d}{%s}=\\)…' % (LX(0), k * k, k, den), opts=pick_opts(r, fr(v), [fr(F(1, k * c)), '0', fr(F(k, 2 * c)), '+\\infty']), ans=0,
      ee='Multiply by \\(\\sqrt{x+%d}+%d\\): \\(\\dfrac{1}{%s(\\sqrt{x+%d}+%d)}\\to%s\\).' % (k * k, k, '' if c == 1 else c, k * k, k, fr(v)), ev='Nhân liên hợp \\(\\sqrt{x+%d}+%d\\): \\(\\dfrac{1}{%s(\\sqrt{x+%d}+%d)}\\to%s\\).' % (k * k, k, '' if c == 1 else c, k * k, k, fr(v)))
def lf_inf(r, lv):
    a, d = r.choice([2, 3, -1, 4, 6]), r.choice([1, 2, -3, 5]); b, e = r.randint(-5, 5), r.randint(-5, 5); side = r.choice(['+\\infty', '-\\infty']); v = F(a, d)
    return dict(en='\\(%s\\dfrac{%s}{%s}=\\)…' % (LX(side), poly([a, b], 'x'), poly([d, e], 'x')), vi='\\(%s\\dfrac{%s}{%s}=\\)…' % (LX(side), poly([a, b], 'x'), poly([d, e], 'x')),
      opts=pick_opts(r, fr(v), [fr(F(b, e)) if e else '0', side, fr(-v), '0' if v else '1']), ans=0, ee='Divide by \\(x\\): the answer is the ratio of the leading coefficients.', ev='Chia tử và mẫu cho \\(x\\): kết quả là tỉ số hai hệ số bậc cao nhất.')
def lf_side(r, lv):
    a = r.randint(-3, 4); c = r.choice([1, 2, -1, -3]); side = r.choice(['+', '-'])
    pos = (c > 0) == (side == '+'); v = '+\\infty' if pos else '-\\infty'
    return dict(en='\\(\\lim\\limits_{x\\to%d^{%s}}\\dfrac{%d}{x%s}=\\)…' % (a, side, c, '%+d' % -a if a else ''), vi='\\(\\lim\\limits_{x\\to%d^{%s}}\\dfrac{%d}{x%s}=\\)…' % (a, side, c, '%+d' % -a if a else ''),
      opts=pick_opts(r, v, [x for x in ('+\\infty', '-\\infty', '0', str(c)) if x != v]), ans=0,
      ee='The numerator tends to \\(%d\\); \\(x%s\\to0\\) with sign \\(%s\\).' % (c, '%+d' % -a if a else '', side), ev='Tử dần tới \\(%d\\); \\(x%s\\to0\\) và mang dấu \\(%s\\).' % (c, '%+d' % -a if a else '', side))
def lf_piece(r, lv):
    a = r.randint(-2, 3); k = r.choice([1, 2, 3, -1]); p = r.randint(-4, 6); m = k * a + p
    q = r.randint(-3, 3); c = m - q * a
    return dict(en='\\(f(x)=%sx%s\\) for \\(x\\lt%d\\) and \\(f(x)=%s\\) for \\(x\\ge%d\\). The value of \\(c\\) making \\(\\lim\\limits_{x\\to%d}f(x)\\) exist is…' % ('' if k == 1 else ('-' if k == -1 else k), '%+d' % p, a, poly([q, 0], 'x') + '+c' if q else 'c', a, a),
      vi='Cho \\(f(x)=%sx%s\\) khi \\(x\\lt%d\\) và \\(f(x)=%s\\) khi \\(x\\ge%d\\). Giá trị \\(c\\) để tồn tại \\(\\lim\\limits_{x\\to%d}f(x)\\) là…' % ('' if k == 1 else ('-' if k == -1 else k), '%+d' % p, a, poly([q, 0], 'x') + '+c' if q else 'c', a, a),
      opts=pick_opts(r, str(c), [str(m), str(c + 1), str(-c) if c else '1', str(m + q * a)]), ans=0,
      ee='Left limit \\(=%d\\), right limit \\(=%d+c\\); equal when \\(c=%d\\).' % (m, q * a, c), ev='Giới hạn trái \\(=%d\\), giới hạn phải \\(=%d+c\\); bằng nhau khi \\(c=%d\\).' % (m, q * a, c))
def lf_cost(r, lv):
    C0 = r.choice([2000, 5000, 10000, 50000]); c = r.choice([15, 20, 25, 40, 120])
    return dict(en='A workshop spends \\(C(x)=%d+%dx\\) (thousand VND) to make \\(x\\) products. The average cost \\(\\dfrac{C(x)}{x}\\) when \\(x\\to+\\infty\\) tends to…' % (C0, c), vi='Một xưởng sản xuất \\(x\\) sản phẩm hết \\(C(x)=%d+%dx\\) (nghìn đồng). Chi phí trung bình mỗi sản phẩm \\(\\dfrac{C(x)}{x}\\) khi \\(x\\to+\\infty\\) dần tới…' % (C0, c),
      opts=pick_opts(r, str(c), [str(C0), '0', '+\\infty', str(C0 + c)]), ans=0, ee='\\(\\dfrac{%d}{x}+%d\\to%d\\): the fixed cost is shared by more and more products.' % (C0, c, c), ev='\\(\\dfrac{%d}{x}+%d\\to%d\\): chi phí cố định được chia cho ngày càng nhiều sản phẩm.' % (C0, c, c))
def lf_cube(r, lv):
    a = r.choice([1, 2, 3, 4, 5, -1, -2, -3]); v = 3 * a * a
    return dict(en='\\(%s\\dfrac{x^3%s}{x%s}=\\)…' % (LX(a), '%+d' % -(a ** 3), '%+d' % -a), vi='\\(%s\\dfrac{x^3%s}{x%s}=\\)…' % (LX(a), '%+d' % -(a ** 3), '%+d' % -a),
      opts=pick_opts(r, str(v), [str(a * a), str(2 * a * a), '0', str(3 * a)]), ans=0,
      ee='\\(x^3-a^3=(x-a)(x^2+ax+a^2)\\); limit \\(=3a^2=%d\\).' % v, ev='\\(x^3-a^3=(x-a)(x^2+ax+a^2)\\); giới hạn \\(=3a^2=%d\\).' % v)
M16S11 = [lf_sub, lf_fac, lf_conj, lf_inf, lf_side, lf_piece, lf_cost, lf_cube]
