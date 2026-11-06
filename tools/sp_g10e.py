# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 10 – Bài 13 (số đặc trưng đo xu thế trung tâm), Bài 14 (số đặc trưng đo độ phân tán) – mẫu số liệu KHÔNG ghép nhóm.
Tứ phân vị theo SGK Kết nối tri thức: Q2 là trung vị; n lẻ thì bỏ trung vị khi chia đôi mẫu; Q1, Q3 là trung vị của nửa dưới, nửa trên."""
import math
from fractions import Fraction as F
from mb_selfpractice import pick_opts, fr
from mb_lib import TI
from freqtable import num

def TT(en, vi): return '§' + TI(en, vi)
def D(x): return num(F(x))
def DE(x): return num(F(x), comma=False)
def median(xs):
    s = sorted(xs); n = len(s); return F(s[n // 2]) if n % 2 else F(s[n // 2 - 1] + s[n // 2], 2)
def quartiles(xs):
    s = sorted(xs); n = len(s); lo, hi = s[:n // 2], s[(n + 1) // 2:]
    return median(lo), median(s), median(hi)
def mean(xs): return F(sum(xs), len(xs))
def var(xs): m = mean(xs); return sum((F(x) - m) ** 2 for x in xs) / len(xs)
def modes(xs):
    c = {x: xs.count(x) for x in xs}; k = max(c.values()); return sorted(x for x in c if c[x] == k), k
def outliers(xs):
    q1, q2, q3 = quartiles(xs); d = q3 - q1; return [x for x in xs if x < q1 - F(3, 2) * d or x > q3 + F(3, 2) * d], q1 - F(3, 2) * d, q3 + F(3, 2) * d
def L(xs, comma=True): return ';\\ '.join(D(x) if comma else DE(x) for x in xs)
CTX = [(('marks (out of 10) of a group', 'điểm kiểm tra (thang 10) của một nhóm học sinh'), 0, 10), (('daily sales (cups of tea) of a shop', 'số cốc trà sữa bán được mỗi ngày của một quán'), 20, 60),
       (('heights (cm) of a basketball team', 'chiều cao (cm) của một đội bóng rổ'), 165, 195), (('times (minutes) to get to school', 'thời gian (phút) đi đến trường'), 5, 40), (('ages of a club', 'tuổi các thành viên một câu lạc bộ'), 14, 30)]
def data(r, n=None, nice_mean=False, nice_var=False):
    for _ in range(200000):
        c = r.choice(CTX); n_ = n or r.choice([7, 8, 9, 10, 11, 12]); xs = [r.randint(c[1], c[2]) for _ in range(n_)]
        if len(set(xs)) < 4: continue
        if nice_mean and (2 * mean(xs)).denominator != 1: continue
        if nice_var and not ((var(xs) * 100).denominator == 1 and mean(xs).denominator == 1): continue
        return c, xs
    raise RuntimeError
# ---------------- Bài 13 ----------------
def m_mean(r, lv):
    c, xs = data(r, nice_mean=True); m = mean(xs)
    return dict(en='The %s: \\(%s\\). The mean is…' % (c[0][0], L(xs, False)), vi='Có %s: \\(%s\\). Số trung bình là…' % (c[0][1], L(xs)),
      opts=pick_opts(r, D(m), [D(median(xs)), D(F(sum(xs), len(xs) - 1)), D(F(max(xs) + min(xs), 2)), D(m + 1)], fill=lambda k: D(m + F(k, 2))), ans=0,
      ee='\\(\\bar x=\\dfrac{%d}{%d}=%s\\).' % (sum(xs), len(xs), DE(m)), ev='\\(\\bar x=\\dfrac{%d}{%d}=%s\\).' % (sum(xs), len(xs), D(m)))
def m_median(r, lv):
    c, xs = data(r); me = median(xs); s = sorted(xs)
    return dict(en='The %s: \\(%s\\). The median is…' % (c[0][0], L(xs, False)), vi='Có %s: \\(%s\\). Trung vị là…' % (c[0][1], L(xs)),
      opts=pick_opts(r, D(me), [D(xs[len(xs) // 2]), D(mean(xs)) if mean(xs).denominator <= 2 else D(me + 1), D(s[len(s) // 2 - 1]), D(me + 2)], fill=lambda k: D(me + F(k, 2))), ans=0,
      ee='Sorted: \\(%s\\); \\(n=%d\\), so \\(M_e=%s\\).' % (L(s, False), len(s), DE(me)), ev='Sắp xếp: \\(%s\\); \\(n=%d\\) nên \\(M_e=%s\\).' % (L(s), len(s), D(me)))
def m_mode(r, lv):
    for _ in range(1000):
        c, xs = data(r); mo, k = modes(xs)
        if len(mo) == 1 and k >= 2: break
    else: raise AssertionError
    mo = mo[0]; others = [x for x in sorted(set(xs), key=lambda v: -xs.count(v)) if x != mo]
    return dict(en='The %s: \\(%s\\). The mode is…' % (c[0][0], L(xs, False)), vi='Có %s: \\(%s\\). Mốt của mẫu là…' % (c[0][1], L(xs)),
      opts=pick_opts(r, str(mo), [str(o) for o in others] + [str(k)]), ans=0, ee='\\(%d\\) appears most often (%d times).' % (mo, k), ev='\\(%d\\) xuất hiện nhiều nhất (%d lần).' % (mo, k))
def m_q(r, lv):
    c, xs = data(r); q1, q2, q3 = quartiles(xs); s = sorted(xs); w = r.choice(['Q_1', 'Q_3']); v = q1 if w == 'Q_1' else q3; o = q3 if w == 'Q_1' else q1
    return dict(en='The %s: \\(%s\\). The quartile \\(%s\\) is…' % (c[0][0], L(xs, False), w), vi='Có %s: \\(%s\\). Tứ phân vị \\(%s\\) là…' % (c[0][1], L(xs), w),
      opts=pick_opts(r, D(v), [D(o), D(q2), D(v + 1), D(v - 1)], fill=lambda k: D(v + F(k, 2))), ans=0,
      ee='Sorted \\(%s\\); \\(Q_2=%s\\); \\(Q_1=%s\\), \\(Q_3=%s\\) (medians of the two halves).' % (L(s, False), DE(q2), DE(q1), DE(q3)), ev='Sắp xếp \\(%s\\); \\(Q_2=%s\\); \\(Q_1=%s\\), \\(Q_3=%s\\) (trung vị của hai nửa).' % (L(s), D(q2), D(q1), D(q3)))
def m_freq(r, lv):
    vals = sorted(r.sample(range(5, 11), 4)); fs = [r.randint(1, 8) for _ in vals]; n = sum(fs); m = F(sum(v * f for v, f in zip(vals, fs)), n)
    if (100 * m).denominator != 1: raise AssertionError
    tb = '\\begin{array}{|c|%s}\\hline \\text{%s}&%s\\\\\\hline \\text{%s}&%s\\\\\\hline\\end{array}'
    t_en = tb % ('c|' * 4, 'Mark', '&'.join(map(str, vals)), 'Frequency', '&'.join(map(str, fs))); t_vi = tb % ('c|' * 4, 'Điểm', '&'.join(map(str, vals)), 'Tần số', '&'.join(map(str, fs)))
    return dict(en='A class test: \\(%s\\) The mean mark is…' % t_en, vi='Kết quả bài kiểm tra của một lớp: \\(%s\\) Điểm trung bình là…' % t_vi,
      opts=pick_opts(r, D(m), [D(mean(vals)), D(F(n, len(vals))), D(m + F(1, 2)), D(m - F(1, 2))]), ans=0,
      ee='\\(\\bar x=\\dfrac{\\sum n_ix_i}{n}=\\dfrac{%d}{%d}=%s\\).' % (sum(v * f for v, f in zip(vals, fs)), n, DE(m)), ev='\\(\\bar x=\\dfrac{\\sum n_ix_i}{n}=\\dfrac{%d}{%d}=%s\\).' % (sum(v * f for v, f in zip(vals, fs)), n, D(m)))
def m_choose(r, lv):
    base = r.choice([(12, 13, 13, 14, 15, 15, 16), (8, 9, 9, 10, 11, 12, 12), (20, 21, 22, 22, 23, 24, 25)]); big = base[-1] * r.choice([8, 10, 12]); xs = list(base) + [big]
    return dict(en='Monthly incomes (million VND) of 8 workers: \\(%s\\). Which number describes a "typical" income best?' % L(xs, False), vi='Thu nhập hằng tháng (triệu đồng) của 8 người: \\(%s\\). Số đặc trưng nào đại diện tốt nhất cho mức thu nhập "điển hình"?' % L(xs),
      opts=[TT('The median, because there is an extreme value', 'Trung vị, vì mẫu có giá trị bất thường'), TT('The mean, because it uses all values', 'Số trung bình, vì dùng mọi giá trị'), TT('The largest value', 'Giá trị lớn nhất'), TT('The range', 'Khoảng biến thiên')], ans=0,
      ee='The value %d pulls the mean up to \\(%s\\); the median \\(%s\\) is not affected.' % (big, DE(mean(xs)), DE(median(xs))), ev='Giá trị %d kéo số trung bình lên \\(%s\\); trung vị \\(%s\\) không bị ảnh hưởng.' % (big, D(mean(xs)), D(median(xs))))
def m_missing(r, lv):
    n = r.choice([5, 6, 8]); xs = [r.randint(4, 12) for _ in range(n - 1)]; m = r.randint(6, 10); x = m * n - sum(xs)
    if not (0 <= x <= 20): raise AssertionError
    return dict(en='The mean of %d numbers is %d. %d of them are \\(%s\\). The remaining number is…' % (n, m, n - 1, L(xs, False)),
      vi='Số trung bình của %d số là %d. %d số trong đó là \\(%s\\). Số còn lại là…' % (n, m, n - 1, L(xs)),
      opts=pick_opts(r, str(x), [str(m), str(x + n), str(abs(x - n)) if abs(x - n) != x else str(x + 1), str(x + 1)]), ans=0,
      ee='Total \\(=%d\\cdot%d=%d\\); missing \\(=%d-%d=%d\\).' % (n, m, n * m, n * m, sum(xs), x), ev='Tổng \\(=%d\\cdot%d=%d\\); số còn lại \\(=%d-%d=%d\\).' % (n, m, n * m, n * m, sum(xs), x))
M13S10 = [m_mean, m_median, m_mode, m_q, m_freq, m_choose, m_missing, m_q]
# ---------------- Bài 14 ----------------
def d_range(r, lv):
    c, xs = data(r); R = max(xs) - min(xs)
    return dict(en='The %s: \\(%s\\). The range is…' % (c[0][0], L(xs, False)), vi='Có %s: \\(%s\\). Khoảng biến thiên là…' % (c[0][1], L(xs)),
      opts=pick_opts(r, str(R), [str(max(xs)), str(xs[-1] - xs[0]) if xs[-1] - xs[0] != R else str(R + 1), str(quartiles(xs)[2] - quartiles(xs)[0]) if quartiles(xs)[2] - quartiles(xs)[0] != R else str(R - 1), str(R + 2)]), ans=0,
      ee='\\(R=x_{\\max}-x_{\\min}=%d-%d=%d\\).' % (max(xs), min(xs), R), ev='\\(R=x_{\\max}-x_{\\min}=%d-%d=%d\\).' % (max(xs), min(xs), R))
def d_iqr(r, lv):
    c, xs = data(r); q1, q2, q3 = quartiles(xs); d = q3 - q1
    return dict(en='The %s: \\(%s\\). The interquartile range \\(\\Delta_Q\\) is…' % (c[0][0], L(xs, False)), vi='Có %s: \\(%s\\). Khoảng tứ phân vị \\(\\Delta_Q\\) là…' % (c[0][1], L(xs)),
      opts=pick_opts(r, D(d), [D(max(xs) - min(xs)), D(q3 - q2), D(d + 1), D(q2 - q1) if q2 - q1 != d else D(d + 2)], fill=lambda k: D(d + F(k, 2))), ans=0,
      ee='\\(Q_1=%s\\), \\(Q_3=%s\\), \\(\\Delta_Q=%s\\).' % (DE(q1), DE(q3), DE(d)), ev='\\(Q_1=%s\\), \\(Q_3=%s\\), \\(\\Delta_Q=%s\\).' % (D(q1), D(q3), D(d)))
def d_var(r, lv):
    c, xs = data(r, n=r.choice([5, 6, 8]), nice_var=True); v = var(xs); m = mean(xs)
    return dict(en='The %s: \\(%s\\). The variance \\(s^2\\) is…' % (c[0][0], L(xs, False)), vi='Có %s: \\(%s\\). Phương sai \\(s^2\\) là…' % (c[0][1], L(xs)),
      opts=pick_opts(r, D(v), [D(v * len(xs) / (len(xs) - 1)) if (v * len(xs) / (len(xs) - 1) * 100).denominator == 1 else D(v + 1), D(F(round(math.sqrt(v) * 100), 100)), D(v + m), D(2 * v)], fill=lambda k: D(v + k)), ans=0,
      ee='\\(\\bar x=%s\\); \\(s^2=\\dfrac1n\\sum(x_i-\\bar x)^2=%s\\).' % (DE(m), DE(v)), ev='\\(\\bar x=%s\\); \\(s^2=\\dfrac1n\\sum(x_i-\\bar x)^2=%s\\).' % (D(m), D(v)))
def d_out(r, lv):
    for _ in range(5000):
        c, xs = data(r, n=r.choice([9, 10, 11]))
        xs = xs[:-1] + [max(xs) + r.choice([25, 30, 40, 60])]
        o, lo, hi = outliers(xs)
        if len(o) == 1: break
    else: raise AssertionError
    o = o[0]; cand = [x for x in sorted(set(xs)) if x != o]
    return dict(en='The %s: \\(%s\\). Which value is an outlier?' % (c[0][0], L(xs, False)), vi='Có %s: \\(%s\\). Giá trị nào là giá trị bất thường?' % (c[0][1], L(xs)),
      opts=pick_opts(r, str(o), [str(cand[0]), str(cand[-1]), str(cand[len(cand) // 2])]), ans=0,
      ee='\\(Q_1=%s\\), \\(Q_3=%s\\), \\(\\Delta_Q=%s\\); values above \\(Q_3+1.5\\Delta_Q=%s\\) are outliers.' % (DE(quartiles(xs)[0]), DE(quartiles(xs)[2]), DE(quartiles(xs)[2] - quartiles(xs)[0]), DE(hi)),
      ev='\\(Q_1=%s\\), \\(Q_3=%s\\), \\(\\Delta_Q=%s\\); giá trị lớn hơn \\(Q_3+1{,}5\\Delta_Q=%s\\) là bất thường.' % (D(quartiles(xs)[0]), D(quartiles(xs)[2]), D(quartiles(xs)[2] - quartiles(xs)[0]), D(hi)))
def d_sd(r, lv):
    s = r.choice([2, 3, 4, 5, F(3, 2), F(5, 2), F(12, 10)]); v = s * s; u = r.choice([('cm', 'cm'), ('kg', 'kg'), ('points', 'điểm')])
    return dict(en='A sample has variance \\(%s\\). Its standard deviation is…' % DE(v), vi='Một mẫu có phương sai \\(%s\\). Độ lệch chuẩn của mẫu là…' % D(v),
      opts=pick_opts(r, D(s), [D(v / 2), D(v), D(s * 2), D(s + 1)]), ans=0, ee='\\(s=\\sqrt{s^2}=%s\\).' % DE(s), ev='\\(s=\\sqrt{s^2}=%s\\).' % D(s))
def d_compare(r, lv):
    a = [r.randint(6, 9) for _ in range(6)]; b = [r.choice([4, 5, 9, 10]) for _ in range(6)]
    if var(a) == var(b) or mean(a).denominator > 2 or mean(b).denominator > 2: raise AssertionError
    better = 'An' if var(a) < var(b) else 'Bình'
    return dict(en='Marks of An: \\(%s\\). Marks of Bình: \\(%s\\). Who has more stable results?' % (L(a, False), L(b, False)), vi='Điểm của An: \\(%s\\). Điểm của Bình: \\(%s\\). Bạn nào có kết quả ổn định hơn?' % (L(a), L(b)),
      opts=[TT('%s (smaller variance)' % better, '%s (phương sai nhỏ hơn)' % better), TT('%s (larger variance)' % ('Bình' if better == 'An' else 'An'), '%s (phương sai lớn hơn)' % ('Bình' if better == 'An' else 'An')), TT('Equally stable', 'Ổn định như nhau'), TT('The one with the higher maximum', 'Bạn có điểm cao nhất lớn hơn')], ans=0,
      ee='\\(s^2_{An}=%s\\), \\(s^2_{Binh}=%s\\).' % (DE(var(a)), DE(var(b))), ev='\\(s^2_{An}=%s\\), \\(s^2_{Bình}=%s\\).' % (D(var(a)), D(var(b))))
def d_shift(r, lv):
    c, xs = data(r); R = max(xs) - min(xs); k = r.choice([2, 3]); add = r.choice([5, 10])
    kind = r.choice(['add', 'mul'])
    ans = R if kind == 'add' else k * R
    return dict(en='A sample has range %d. Every value is %s. The new range is…' % (R, 'increased by %d' % add if kind == 'add' else 'multiplied by %d' % k), vi='Một mẫu có khoảng biến thiên %d. Mọi giá trị đều được %s. Khoảng biến thiên mới là…' % (R, 'cộng thêm %d' % add if kind == 'add' else 'nhân với %d' % k),
      opts=pick_opts(r, str(ans), [str(R + add), str(k * R) if kind == 'add' else str(R), str(k * k * R), str(ans + 1)]), ans=0,
      ee='Adding moves all values equally (spread unchanged); multiplying by \\(k\\) multiplies distances by \\(k\\).', ev='Cộng thêm thì mọi giá trị dời như nhau (độ phân tán không đổi); nhân với \\(k\\) thì mọi khoảng cách nhân \\(k\\).')
M14S10 = [d_range, d_iqr, d_var, d_out, d_sd, d_compare, d_shift, d_iqr]
