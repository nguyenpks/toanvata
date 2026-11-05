# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 11 – Bài 6 (cấp số cộng), Bài 7 (cấp số nhân), Bài 8 (mẫu số liệu ghép nhóm)."""
import math
from fractions import Fraction as F
from mb_selfpractice import *

# ---------- Bài 6: cấp số cộng ----------
def ap_term(r, lv):
    u1 = r.randint(-8, 12); d = r.choice([-4, -3, -2, 2, 3, 4, 5]); k = r.randint(8, 20); v = u1 + (k - 1) * d
    return dict(en='An arithmetic sequence has \\(u_1=%d\\) and common difference \\(d=%d\\). Find \\(u_{%d}\\).' % (u1, d, k), vi='Cấp số cộng có \\(u_1=%d\\), công sai \\(d=%d\\). Tính \\(u_{%d}\\).' % (u1, d, k),
      opts=pick_opts(r, str(v), [str(v + d), str(v - d), str(u1 + k * d), str(u1 + d * (k - 2)), str(v + 1)], fill=lambda j: str(v + 5 + j)), ans=0, ee='\\(u_n=u_1+(n-1)d=%d+%d\\cdot%d=%d\\).' % (u1, k - 1, d, v), ev='\\(u_n=u_1+(n-1)d=%d+%d\\cdot%d=%d\\).' % (u1, k - 1, d, v))
def ap_d(r, lv):
    d = r.choice([-5, -3, -2, 2, 3, 4, 6]); u1 = r.randint(-10, 10); i, j = r.sample(range(2, 12), 2); i, j = min(i, j), max(i, j)
    ui, uj = u1 + (i - 1) * d, u1 + (j - 1) * d
    return dict(en='In an arithmetic sequence \\(u_{%d}=%d\\) and \\(u_{%d}=%d\\). Find the common difference \\(d\\).' % (i, ui, j, uj), vi='Cấp số cộng có \\(u_{%d}=%d\\) và \\(u_{%d}=%d\\). Tìm công sai \\(d\\).' % (i, ui, j, uj),
      opts=pick_opts(r, str(d), [str(-d), str(d + 1), str(d - 1), str(2 * d)], fill=lambda k: str(d + 3 + k)), ans=0, ee='\\(d=\\dfrac{u_{%d}-u_{%d}}{%d-%d}=\\dfrac{%d}{%d}=%d\\).' % (j, i, j, i, uj - ui, j - i, d), ev='\\(d=\\dfrac{u_{%d}-u_{%d}}{%d-%d}=\\dfrac{%d}{%d}=%d\\).' % (j, i, j, i, uj - ui, j - i, d))
def ap_sum(r, lv):
    u1 = r.randint(-6, 10); d = r.choice([-3, -2, 2, 3, 4, 5]); n = r.randint(8, 25); S = n * (2 * u1 + (n - 1) * d) // 2
    return dict(en='Find the sum of the first %d terms of the arithmetic sequence with \\(u_1=%d\\) and \\(d=%d\\).' % (n, u1, d), vi='Tính tổng %d số hạng đầu của cấp số cộng có \\(u_1=%d\\), \\(d=%d\\).' % (n, u1, d),
      opts=pick_opts(r, str(S), [str(S + n), str(S - n), str(n * (u1 + (n - 1) * d)), str(S + d)], fill=lambda k: str(S + 7 + k)), ans=0, ee='\\(S_n=\\dfrac{n[2u_1+(n-1)d]}{2}=\\dfrac{%d\\cdot%d}{2}=%d\\).' % (n, 2 * u1 + (n - 1) * d, S), ev='\\(S_n=\\dfrac{n[2u_1+(n-1)d]}{2}=\\dfrac{%d\\cdot%d}{2}=%d\\).' % (n, 2 * u1 + (n - 1) * d, S))
def ap_count(r, lv):
    u1 = r.randint(-5, 9); d = r.choice([2, 3, 4, 5, 6]); n = r.randint(12, 40); last = u1 + (n - 1) * d
    return dict(en='How many terms does the arithmetic sequence \\(%d,\\ %d,\\ %d,\\dots,\\ %d\\) have?' % (u1, u1 + d, u1 + 2 * d, last), vi='Cấp số cộng \\(%d,\\ %d,\\ %d,\\dots,\\ %d\\) có bao nhiêu số hạng?' % (u1, u1 + d, u1 + 2 * d, last),
      opts=pick_opts(r, str(n), [str(n + 1), str(n - 1), str(n + 2), str(2 * n)], fill=lambda k: str(n + 3 + k)), ans=0, ee='\\(%d=%d+(n-1)\\cdot%d\\Rightarrow n=%d\\).' % (last, u1, d, n), ev='\\(%d=%d+(n-1)\\cdot%d\\Rightarrow n=%d\\).' % (last, u1, d, n))
def ap_mid(r, lv):
    a = r.randint(-9, 9); d = r.choice([-4, -3, 2, 3, 5, 6]); b = a + 2 * d; x = a + d
    return dict(en='For which \\(x\\) are \\(%d,\\ x,\\ %d\\) three consecutive terms of an arithmetic sequence?' % (a, b), vi='Với giá trị nào của \\(x\\) thì \\(%d,\\ x,\\ %d\\) là ba số hạng liên tiếp của một cấp số cộng?' % (a, b),
      opts=pick_opts(r, str(x), [str(x + 1), str(x - 1), str(a * b), str(b - a)], fill=lambda k: str(x + 4 + k)), ans=0, ee='The middle term is the average: \\(x=\\dfrac{%d+%d}{2}=%d\\).' % (a, b, x), ev='Số hạng giữa là trung bình cộng: \\(x=\\dfrac{%d+%d}{2}=%d\\).' % (a, b, x))
def ap_seats(r, lv):
    f = r.randint(10, 20); d = r.choice([2, 3, 4]); n = r.randint(8, 15); S = n * (2 * f + (n - 1) * d) // 2
    return dict(en='A hall has %d rows. The first row has %d seats and each next row has %d more seats than the row before. How many seats are there in total?' % (n, f, d), vi='Một hội trường có %d hàng ghế. Hàng đầu có %d ghế, mỗi hàng sau nhiều hơn hàng trước %d ghế. Tổng số ghế là bao nhiêu?' % (n, f, d),
      opts=pick_opts(r, str(S), [str(S + n), str(S - f), str(n * (f + (n - 1) * d)), str(S + d)], fill=lambda k: str(S + 9 + k)), ans=0, ee='\\(S_{%d}=\\dfrac{%d[2\\cdot%d+%d\\cdot%d]}{2}=%d\\).' % (n, n, f, n - 1, d, S), ev='\\(S_{%d}=\\dfrac{%d[2\\cdot%d+%d\\cdot%d]}{2}=%d\\).' % (n, n, f, n - 1, d, S))
B6 = [ap_term, ap_d, ap_sum, ap_count, ap_mid, ap_seats, ap_term, ap_sum]

# ---------- Bài 7: cấp số nhân ----------
def gp_term(r, lv):
    u1 = r.choice([1, 2, 3, 4, 5]); q = r.choice([2, 3, -2, -3]); k = r.randint(4, 7) if abs(q) == 3 else r.randint(5, 9); v = u1 * q ** (k - 1)
    return dict(en='A geometric sequence has \\(u_1=%d\\) and common ratio \\(q=%d\\). Find \\(u_{%d}\\).' % (u1, q, k), vi='Cấp số nhân có \\(u_1=%d\\), công bội \\(q=%d\\). Tính \\(u_{%d}\\).' % (u1, q, k),
      opts=pick_opts(r, str(v), [str(u1 * q ** k), str(u1 * q ** (k - 2)), str(u1 + (k - 1) * q), str(-v)], fill=lambda j: str(v + 11 * j)), ans=0, ee='\\(u_n=u_1q^{n-1}=%d\\cdot(%d)^{%d}=%d\\).' % (u1, q, k - 1, v), ev='\\(u_n=u_1q^{n-1}=%d\\cdot(%d)^{%d}=%d\\).' % (u1, q, k - 1, v))
def gp_q(r, lv):
    q = r.choice([2, 3, -2, -3, 4, 5]); u1 = r.choice([1, 2, 3, -1, -2]); i = r.randint(1, 3); j = i + 2 if r.random() < .5 else i + 1
    ui, uj = u1 * q ** (i - 1), u1 * q ** (j - 1)
    if j == i + 2:
        cand = [q, -q] if q * q == uj // ui else [q]
        return dict(en='In a geometric sequence with positive ratio, \\(u_{%d}=%d\\) and \\(u_{%d}=%d\\). Find \\(q\\).' % (i, abs(ui), j, abs(uj)), vi='Cấp số nhân có công bội dương, \\(u_{%d}=%d\\) và \\(u_{%d}=%d\\). Tìm \\(q\\).' % (i, abs(ui), j, abs(uj)),
          opts=pick_opts(r, str(abs(q)), [str(-abs(q)), str(abs(q) * abs(q)), str(abs(q) + 1), str(abs(q) - 1)], fill=lambda k: str(abs(q) + 4 + k)), ans=0, ee='\\(q^2=\\dfrac{%d}{%d}=%d\\), and \\(q\\gt0\\), so \\(q=%d\\).' % (abs(uj), abs(ui), q * q, abs(q)), ev='\\(q^2=\\dfrac{%d}{%d}=%d\\), \\(q\\gt0\\) nên \\(q=%d\\).' % (abs(uj), abs(ui), q * q, abs(q)))
    return dict(en='In a geometric sequence \\(u_{%d}=%d\\) and \\(u_{%d}=%d\\). Find \\(q\\).' % (i, ui, j, uj), vi='Cấp số nhân có \\(u_{%d}=%d\\) và \\(u_{%d}=%d\\). Tìm \\(q\\).' % (i, ui, j, uj),
      opts=pick_opts(r, str(q), [str(-q), str(q + 1), str(q * q), str(q - 1)], fill=lambda k: str(q + 4 + k)), ans=0, ee='\\(q=\\dfrac{u_{%d}}{u_{%d}}=\\dfrac{%d}{%d}=%d\\).' % (j, i, uj, ui, q), ev='\\(q=\\dfrac{u_{%d}}{u_{%d}}=\\dfrac{%d}{%d}=%d\\).' % (j, i, uj, ui, q))
def gp_sum(r, lv):
    u1 = r.choice([1, 2, 3, 5]); q = r.choice([2, 3, -2]); n = r.randint(4, 8); S = u1 * (q ** n - 1) // (q - 1)
    return dict(en='Find the sum of the first %d terms of the geometric sequence with \\(u_1=%d\\) and \\(q=%d\\).' % (n, u1, q), vi='Tính tổng %d số hạng đầu của cấp số nhân có \\(u_1=%d\\), \\(q=%d\\).' % (n, u1, q),
      opts=pick_opts(r, str(S), [str(S + u1), str(S - u1), str(u1 * q ** n), str(u1 * (q ** n + 1) // (q + 1) if q != -1 else S + 2)], fill=lambda k: str(S + 7 * k)), ans=0, ee='\\(S_n=u_1\\dfrac{q^n-1}{q-1}=%d\\cdot\\dfrac{(%d)^{%d}-1}{%d-1}=%d\\).' % (u1, q, n, q, S), ev='\\(S_n=u_1\\dfrac{q^n-1}{q-1}=%d\\cdot\\dfrac{(%d)^{%d}-1}{%d-1}=%d\\).' % (u1, q, n, q, S))
def gp_mid(r, lv):
    q = r.choice([2, 3, 4, 5]); a = r.choice([1, 2, 3, 4]); x = a * q; b = a * q * q
    return dict(en='For which positive \\(x\\) are \\(%d,\\ x,\\ %d\\) three consecutive terms of a geometric sequence?' % (a, b), vi='Với \\(x\\gt0\\) nào thì \\(%d,\\ x,\\ %d\\) là ba số hạng liên tiếp của một cấp số nhân?' % (a, b),
      opts=pick_opts(r, str(x), [str(x + 1), str(x - 1), str((a + b) // 2 if (a + b) % 2 == 0 else x + 2), str(a * b)], fill=lambda k: str(x + 3 + k)), ans=0, ee='\\(x^2=%d\\cdot%d=%d\\), so \\(x=%d\\).' % (a, b, a * b, x), ev='\\(x^2=%d\\cdot%d=%d\\) nên \\(x=%d\\).' % (a, b, a * b, x))
def gp_money(r, lv):
    P = r.choice([100, 200, 300, 400, 500, 600]); rate = r.choice([10, 20, 5]); n = 2
    if rate == 5 and P % 400: P = 400
    A = P * (100 + rate) ** n // 100 ** n; assert A * 100 ** n == P * (100 + rate) ** n
    return dict(en='You deposit %d million dong at a compound interest of %d%% per year. How many million dong will you have after %d years?' % (P, rate, n), vi='Gửi %d triệu đồng với lãi kép %d%%/năm. Sau %d năm có bao nhiêu triệu đồng?' % (P, rate, n),
      opts=pick_opts(r, str(A), [str(P + n * P * rate // 100), str(A + 1), str(A - 1), str(P * rate)], fill=lambda k: str(A + 5 * k)), ans=0, ee='\\(A=P(1+r)^n=%d\\cdot(1.%02d)^{%d}=%d\\).' % (P, rate, n, A), ev='\\(A=P(1+r)^n=%d\\cdot(1{,}%02d)^{%d}=%d\\).' % (P, rate, n, A))
def gp_count(r, lv):
    u1 = r.choice([1, 2, 3]); q = r.choice([2, 3]); n = r.randint(5, 9) if q == 2 else r.randint(4, 6); last = u1 * q ** (n - 1)
    return dict(en='How many terms does the geometric sequence \\(%d,\\ %d,\\ %d,\\dots,\\ %d\\) have?' % (u1, u1 * q, u1 * q * q, last), vi='Cấp số nhân \\(%d,\\ %d,\\ %d,\\dots,\\ %d\\) có bao nhiêu số hạng?' % (u1, u1 * q, u1 * q * q, last),
      opts=pick_opts(r, str(n), [str(n + 1), str(n - 1), str(n + 2), str(2 * n)], fill=lambda k: str(n + 3 + k)), ans=0, ee='\\(%d\\cdot%d^{n-1}=%d\\Rightarrow n=%d\\).' % (u1, q, last, n), ev='\\(%d\\cdot%d^{n-1}=%d\\Rightarrow n=%d\\).' % (u1, q, last, n))
B7 = [gp_term, gp_q, gp_sum, gp_mid, gp_money, gp_count, gp_term, gp_sum]

# ---------- Bài 8: mẫu số liệu ghép nhóm ----------
def _tab(edges, fs):
    from freqtable import FREQ
    return FREQ(edges, fs)
def _mk(r):
    w = r.choice([2, 5, 10]); a = r.choice([0, w, 2 * w]); k = r.choice([4, 5]); edges = [a + i * w for i in range(k + 1)]; fs = [r.randint(2, 12) for _ in range(k)]
    return w, edges, fs
def st_width(r, lv):
    w, edges, fs = _mk(r); i = r.randrange(len(fs)); mid = F(edges[i] + edges[i + 1], 2)
    return dict(en='The data are grouped as \\([%d;%d)\\). What is the midpoint (representative value) of this group?' % (edges[i], edges[i + 1]), vi='Nhóm số liệu \\([%d;%d)\\) có giá trị đại diện là bao nhiêu?' % (edges[i], edges[i + 1]),
      opts=pick_opts(r, fr(mid), [str(edges[i]), str(edges[i + 1]), fr(mid + 1), str(w)], fill=lambda k: fr(mid + k + 2)), ans=0, ee='The midpoint is \\(\\dfrac{%d+%d}{2}=%s\\).' % (edges[i], edges[i + 1], fr(mid)), ev='Giá trị đại diện là \\(\\dfrac{%d+%d}{2}=%s\\).' % (edges[i], edges[i + 1], fr(mid)))
def st_total(r, lv):
    w, edges, fs = _mk(r); n = sum(fs)
    return dict(en='A frequency table: %s. How many data values are there in total?' % _tab(edges, fs), vi='Bảng tần số: %s. Mẫu số liệu có tất cả bao nhiêu giá trị?' % _tab(edges, fs),
      opts=pick_opts(r, str(n), [str(n + 1), str(n - 1), str(max(fs)), str(n + 3)], fill=lambda k: str(n + 5 + k)), ans=0, ee='Add all the frequencies: %s = %d.' % ('+'.join(map(str, fs)), n), ev='Cộng mọi tần số: %s = %d.' % ('+'.join(map(str, fs)), n))
def st_rel(r, lv):
    while True:
        w, edges, fs = _mk(r); n = sum(fs)
        if 100 % n == 0 or n in (8, 16, 20, 25, 40, 50): break
    i = r.randrange(len(fs)); v = F(100 * fs[i], n)
    return dict(en='A frequency table: %s. What is the relative frequency of the group \\([%d;%d)\\) (in %%)?' % (_tab(edges, fs), edges[i], edges[i + 1]), vi='Bảng tần số: %s. Tần suất của nhóm \\([%d;%d)\\) là bao nhiêu phần trăm?' % (_tab(edges, fs), edges[i], edges[i + 1]),
      opts=pick_opts(r, fr(v), [fr(v + 5), fr(v - 5), fr(v * 2), fr(F(fs[i]))], fill=lambda k: fr(v + 7 + k)), ans=0, ee='\\(\\dfrac{%d}{%d}\\cdot100\\%%=%s\\%%\\).' % (fs[i], n, fr(v)), ev='\\(\\dfrac{%d}{%d}\\cdot100\\%%=%s\\%%\\).' % (fs[i], n, fr(v)))
def st_cum(r, lv):
    w, edges, fs = _mk(r); j = r.randint(1, len(fs) - 1); c = sum(fs[:j])
    return dict(en='A frequency table: %s. How many values are less than \\(%d\\)?' % (_tab(edges, fs), edges[j]), vi='Bảng tần số: %s. Có bao nhiêu giá trị nhỏ hơn \\(%d\\)?' % (_tab(edges, fs), edges[j]),
      opts=pick_opts(r, str(c), [str(c + fs[j]), str(c - fs[0]) if c != fs[0] else str(c + 2), str(fs[j - 1]), str(c + 1)], fill=lambda k: str(c + 4 + k)), ans=0, ee='Add the frequencies of the groups before %d: %d.' % (edges[j], c), ev='Cộng tần số của các nhóm đứng trước %d: %d.' % (edges[j], c))
def st_mode(r, lv):
    while True:
        w, edges, fs = _mk(r)
        if fs.count(max(fs)) == 1: break
    i = fs.index(max(fs))
    return dict(en='A frequency table: %s. Which group has the highest frequency?' % _tab(edges, fs), vi='Bảng tần số: %s. Nhóm nào có tần số lớn nhất?' % _tab(edges, fs),
      opts=['[%d;%d)' % (edges[i], edges[i + 1])] + ['[%d;%d)' % (edges[k], edges[k + 1]) for k in range(len(fs)) if k != i][:3], ans=0, ee='The largest frequency is %d, in the group \\([%d;%d)\\).' % (fs[i], edges[i], edges[i + 1]), ev='Tần số lớn nhất là %d, thuộc nhóm \\([%d;%d)\\).' % (fs[i], edges[i], edges[i + 1]))
def st_mean(r, lv):
    w, edges, fs = _mk(r); n = sum(fs); mids = [F(edges[i] + edges[i + 1], 2) for i in range(len(fs))]; m = sum(mi * f for mi, f in zip(mids, fs)) / n
    return dict(en='A frequency table: %s. Estimate the mean using the midpoints of the groups.' % _tab(edges, fs), vi='Bảng tần số: %s. Ước tính số trung bình bằng giá trị đại diện của các nhóm.' % _tab(edges, fs),
      opts=pick_opts(r, fr(m), [fr(m + 1), fr(m - 1), fr(m + w), fr(sum(mids) / len(mids))], fill=lambda k: fr(m + k + 2)), ans=0, ee='\\(\\bar x=\\dfrac{\\sum f_ix_i}{n}=%s\\).' % fr(m), ev='\\(\\bar x=\\dfrac{\\sum f_ix_i}{n}=%s\\).' % fr(m))
B8 = [st_width, st_total, st_rel, st_cum, st_mode, st_mean, st_total, st_cum]
