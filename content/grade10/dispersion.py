# -*- coding: utf-8 -*-
"""g10-stats-03 = Toán 10 KNTT, Bài 14: Các số đặc trưng đo độ phân tán. Mã ngân hàng câu hỏi: TOAN10-C5-B14."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g10e as S
from sp_g10e import mean, median, quartiles, var, outliers, L, D, DE

def HT(r1, r2): return TBL([TI(*r1[0])] + [str(x) for x in r1[1]], [[TI(*r2[0])] + [str(x) for x in r2[1]]])
CV = 'Các số đặc trưng đo độ phân tán'
vocab = defs(CV, [
 ('rng10', 'range', 'khoảng biến thiên', 'the difference between the largest and the smallest value: \\(R=x_{\\max}-x_{\\min}\\).', 'hiệu giữa giá trị lớn nhất và giá trị nhỏ nhất: \\(R=x_{\\max}-x_{\\min}\\).', 'The range of the temperatures is 9 degrees.', '\\(R\\)'),
 ('iqr10', 'interquartile range', 'khoảng tứ phân vị', '\\(\\Delta_Q=Q_3-Q_1\\): the spread of the middle half of the data.', '\\(\\Delta_Q=Q_3-Q_1\\): độ phân tán của nửa giữa mẫu số liệu.', 'The interquartile range is 6.', '\\(\\Delta_Q\\)'),
 ('var10', 'variance', 'phương sai', '\\(s^2=\\dfrac1n\\sum(x_i-\\bar x)^2\\), the mean of the squared deviations.', '\\(s^2=\\dfrac1n\\sum(x_i-\\bar x)^2\\), trung bình cộng bình phương các độ lệch.', 'The variance of the marks is 2.25.', '\\(s^2\\)'),
 ('sd10', 'standard deviation', 'độ lệch chuẩn', '\\(s=\\sqrt{s^2}\\); it has the same unit as the data.', '\\(s=\\sqrt{s^2}\\); cùng đơn vị với số liệu.', 'The standard deviation is 1.5 points.', '\\(s\\)'),
 ('spread', 'spread (dispersion)', 'độ phân tán', 'how far the values are scattered.', 'mức độ các giá trị nằm rải rác, cách xa nhau.', 'Sample A has a larger spread.', ''),
 ('outl10', 'outlier', 'giá trị ngoại lai', 'a value greater than \\(Q_3+1.5\\Delta_Q\\) or less than \\(Q_1-1.5\\Delta_Q\\).', 'giá trị lớn hơn \\(Q_3+1{,}5\\Delta_Q\\) hoặc nhỏ hơn \\(Q_1-1{,}5\\Delta_Q\\).', '95 is an outlier in this sample.', '')])
goals = [('find the range and the interquartile range;', 'tìm [[khoảng biến thiên]] và [[khoảng tứ phân vị]];'),
         ('detect outliers with the \\(1.5\\Delta_Q\\) rule;', 'phát hiện [[giá trị ngoại lai]] bằng quy tắc \\(1{,}5\\Delta_Q\\);'),
         ('compute the variance and the standard deviation;', 'tính [[phương sai]] và [[độ lệch chuẩn]];'),
         ('compare the spread (stability) of two samples.', 'so sánh [[độ phân tán]] (mức độ ổn định) của hai mẫu số liệu.')]
phrases = [('<b>Find the range of the data.</b>', 'Tìm khoảng biến thiên của mẫu số liệu.'), ('<b>Is there an outlier?</b>', 'Mẫu có giá trị ngoại lai không?'), ('<b>Compute the variance and the standard deviation.</b>', 'Tính phương sai và độ lệch chuẩn.'),
           ('<b>Which player is more consistent?</b>', 'Cầu thủ nào thi đấu ổn định hơn?'), ('<b>The data are more spread out.</b>', 'Số liệu phân tán hơn.')]
review = T('From Bài 13: the mean \\(\\bar x\\), the median \\(M_e=Q_2\\), the quartiles \\(Q_1\\), \\(Q_3\\) (medians of the two halves of the sorted data; without \\(M_e\\) when \\(n\\) is odd). Two samples can have the same mean but very different spread.', 'Từ Bài 13: số trung bình \\(\\bar x\\), trung vị \\(M_e=Q_2\\), tứ phân vị \\(Q_1\\), \\(Q_3\\) (trung vị của hai nửa mẫu đã sắp xếp; không tính \\(M_e\\) khi \\(n\\) lẻ). Hai mẫu có thể cùng số trung bình nhưng độ phân tán rất khác nhau.')
theory = '<h3>14.1 %s</h3>' % TI('Range and interquartile range', 'Khoảng biến thiên và khoảng tứ phân vị')
theory += BOX('blue', ('Definitions', 'Định nghĩa'), M('R=x_{\\max}-x_{\\min},\\qquad \\Delta_Q=Q_3-Q_1'),
  T('\\(R\\) is easy to compute but depends only on two values (it is very sensitive to outliers). \\(\\Delta_Q\\) describes the middle 50% of the data and is not affected by extreme values.', '\\(R\\) dễ tính nhưng chỉ phụ thuộc hai giá trị (rất nhạy với giá trị bất thường). \\(\\Delta_Q\\) mô tả 50% số liệu ở giữa và không bị ảnh hưởng bởi giá trị quá lớn, quá nhỏ.'))
theory += BOX('mint', ('Outliers', 'Giá trị ngoại lai'), T('\\(x\\) is an outlier if \\(x\\gt Q_3+1.5\\Delta_Q\\) or \\(x\\lt Q_1-1.5\\Delta_Q\\). Outliers may be mistakes in measuring, or really special cases – check before deleting them.', '\\(x\\) là giá trị ngoại lai nếu \\(x\\gt Q_3+1{,}5\\Delta_Q\\) hoặc \\(x\\lt Q_1-1{,}5\\Delta_Q\\). Giá trị ngoại lai có thể do đo sai, hoặc là trường hợp đặc biệt thật – cần kiểm tra trước khi loại bỏ.'))
theory += '<h3>14.2 %s</h3>' % TI('Variance and standard deviation', 'Phương sai và độ lệch chuẩn')
theory += BOX('blue', ('Formulas', 'Công thức'), M('s^2=\\dfrac{(x_1-\\bar x)^2+\\dots+(x_n-\\bar x)^2}{n}=\\dfrac{x_1^2+\\dots+x_n^2}{n}-\\bar x^2,\\qquad s=\\sqrt{s^2}'),
  UL([T('With a frequency table: \\(s^2=\\dfrac1n\\sum n_i(x_i-\\bar x)^2=\\dfrac1n\\sum n_ix_i^2-\\bar x^2\\).', 'Với bảng tần số: \\(s^2=\\dfrac1n\\sum n_i(x_i-\\bar x)^2=\\dfrac1n\\sum n_ix_i^2-\\bar x^2\\).'),
      T('The larger \\(s\\), the more the data are spread around the mean; \\(s\\) has the unit of the data.', '\\(s\\) càng lớn thì số liệu càng phân tán quanh số trung bình; \\(s\\) có cùng đơn vị với số liệu.'),
      T('Statistics also uses \\(\\hat s^2=\\dfrac{1}{n-1}\\sum(x_i-\\bar x)^2\\) (corrected variance) to estimate a population.', 'Trong thống kê còn dùng \\(\\hat s^2=\\dfrac{1}{n-1}\\sum(x_i-\\bar x)^2\\) (phương sai hiệu chỉnh) để ước lượng cho tổng thể.')]))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('Compare spreads only for data in the same unit. \\(s\\) and \\(R\\) are both affected by outliers; \\(\\Delta_Q\\) is not.', 'Chỉ so sánh độ phân tán của các mẫu cùng đơn vị đo. \\(s\\) và \\(R\\) đều bị ảnh hưởng bởi giá trị ngoại lai; \\(\\Delta_Q\\) thì không.'))

T1 = [24, 27, 22, 29, 31, 26, 25, 30, 28]; q = quartiles(T1); assert max(T1) - min(T1) == 9 and q == (F(49, 2), 27, F(59, 2)) and q[2] - q[0] == 5
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Temperatures', 'Nhiệt độ'), T('Highest temperatures (°C) in 9 days: \\(%s\\). Find \\(R\\) and \\(\\Delta_Q\\).' % L(T1, False), 'Nhiệt độ cao nhất (°C) trong 9 ngày: \\(%s\\). Tìm \\(R\\) và \\(\\Delta_Q\\).' % L(T1)),
  T('Sort; \\(n=9\\) is odd, so leave out the median for the halves.', 'Sắp xếp; \\(n=9\\) lẻ nên bỏ trung vị khi chia đôi.'),
  [T('Sorted: \\(%s\\); \\(R=31-22=9\\).' % L(sorted(T1), False), 'Sắp xếp: \\(%s\\); \\(R=31-22=9\\).' % L(sorted(T1))), T('\\(Q_2=27\\); lower half \\(22;24;25;26\\): \\(Q_1=24.5\\); upper half \\(28;29;30;31\\): \\(Q_3=29.5\\).', '\\(Q_2=27\\); nửa trái \\(22;24;25;26\\): \\(Q_1=24{,}5\\); nửa phải \\(28;29;30;31\\): \\(Q_3=29{,}5\\).')],
  T('\\(R=9\\) °C, \\(\\Delta_Q=5\\) °C.', '\\(R=9\\) °C, \\(\\Delta_Q=5\\) °C.'))
EA, EB = [8, 9, 7, 8, 8], [10, 6, 9, 5, 10]; assert mean(EA) == mean(EB) == 8 and var(EA) == F(2, 5) and var(EB) == F(22, 5)
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Two shooters', 'Hai xạ thủ'), T('Scores of two shooters in 5 shots. A: \\(%s\\). B: \\(%s\\). Compute the variances and say who is more consistent.' % (L(EA, False), L(EB, False)), 'Điểm 5 lần bắn của hai xạ thủ. A: \\(%s\\). B: \\(%s\\). Tính phương sai và cho biết ai bắn ổn định hơn.' % (L(EA), L(EB))),
  T('Both have mean 8; compare the squared deviations.', 'Cả hai có trung bình 8; so sánh các bình phương độ lệch.'),
  [T('A: deviations \\(0;1;-1;0;0\\), \\(s_A^2=\\dfrac{2}{5}=0.4\\), \\(s_A\\approx0.63\\).', 'A: độ lệch \\(0;1;-1;0;0\\), \\(s_A^2=\\dfrac{2}{5}=0{,}4\\), \\(s_A\\approx0{,}63\\).'), T('B: deviations \\(2;-2;1;-3;2\\), \\(s_B^2=\\dfrac{22}{5}=4.4\\), \\(s_B\\approx2.10\\).', 'B: độ lệch \\(2;-2;1;-3;2\\), \\(s_B^2=\\dfrac{22}{5}=4{,}4\\), \\(s_B\\approx2{,}10\\).')],
  T('Same mean, but \\(s_A\\lt s_B\\): shooter A is more consistent.', 'Cùng trung bình nhưng \\(s_A\\lt s_B\\): xạ thủ A ổn định hơn.'))
O3 = [12, 15, 14, 13, 16, 15, 14, 45, 13, 14]; o, lo, hi = outliers(O3); q3_ = quartiles(O3); assert o == [45] and q3_ == (13, 14, 15) and hi == 18 and lo == 10
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('An odd value', 'Một giá trị lạ'), T('Waiting times (minutes) at a clinic: \\(%s\\). Is there an outlier?' % L(O3, False), 'Thời gian chờ khám (phút) tại một phòng khám: \\(%s\\). Mẫu có giá trị ngoại lai không?' % L(O3)),
  T('Find \\(Q_1\\), \\(Q_3\\), \\(\\Delta_Q\\) and the two fences.', 'Tìm \\(Q_1\\), \\(Q_3\\), \\(\\Delta_Q\\) và hai ngưỡng.'),
  [T('Sorted: \\(%s\\); \\(Q_1=13\\), \\(Q_3=15\\), \\(\\Delta_Q=2\\).' % L(sorted(O3), False), 'Sắp xếp: \\(%s\\); \\(Q_1=13\\), \\(Q_3=15\\), \\(\\Delta_Q=2\\).' % L(sorted(O3))), T('Fences: \\(13-1.5\\cdot2=10\\) and \\(15+1.5\\cdot2=18\\).', 'Ngưỡng: \\(13-1{,}5\\cdot2=10\\) và \\(15+1{,}5\\cdot2=18\\).')],
  T('\\(45\\gt18\\): 45 minutes is an outlier (maybe a patient who came very early, or a recording error).', '\\(45\\gt18\\): 45 phút là giá trị ngoại lai (có thể bệnh nhân đến rất sớm, hoặc ghi sai).'))
V4, N4 = [5, 6, 7, 8, 9], [2, 3, 8, 5, 2]; n4 = sum(N4); m4 = F(sum(v * f for v, f in zip(V4, N4)), n4); s24 = F(sum(f * v * v for v, f in zip(V4, N4)), n4) - m4 * m4
assert n4 == 20 and m4 == F(142, 20) and s24 == F(119, 100)
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('From a frequency table', 'Từ bảng tần số'), T('Marks of 20 students: %s Find the variance and the standard deviation (to the hundredths).' % HT((('Mark', 'Điểm'), V4), (('Frequency', 'Tần số'), N4)), 'Điểm của 20 học sinh: %s Tính phương sai và độ lệch chuẩn (làm tròn đến hàng phần trăm).' % HT((('Mark', 'Điểm'), V4), (('Frequency', 'Tần số'), N4))),
  T('\\(s^2=\\dfrac1n\\sum n_ix_i^2-\\bar x^2\\).', '\\(s^2=\\dfrac1n\\sum n_ix_i^2-\\bar x^2\\).'),
  [T('\\(\\bar x=\\dfrac{%d}{20}=%s\\).' % (sum(v * f for v, f in zip(V4, N4)), DE(m4)), '\\(\\bar x=\\dfrac{%d}{20}=%s\\).' % (sum(v * f for v, f in zip(V4, N4)), D(m4))),
   T('\\(\\dfrac1n\\sum n_ix_i^2=\\dfrac{%d}{20}=%s\\); \\(s^2=%s-%s^2=%s\\).' % (sum(f * v * v for v, f in zip(V4, N4)), DE(F(sum(f * v * v for v, f in zip(V4, N4)), 20)), DE(F(sum(f * v * v for v, f in zip(V4, N4)), 20)), DE(m4), DE(s24)),
     '\\(\\dfrac1n\\sum n_ix_i^2=\\dfrac{%d}{20}=%s\\); \\(s^2=%s-%s^2=%s\\).' % (sum(f * v * v for v, f in zip(V4, N4)), D(F(sum(f * v * v for v, f in zip(V4, N4)), 20)), D(F(sum(f * v * v for v, f in zip(V4, N4)), 20)), D(m4), D(s24)))],
  T('\\(s^2=%s\\), \\(s\\approx%s\\).' % (DE(s24), DE(F(round(math.sqrt(s24) * 100), 100))), '\\(s^2=%s\\), \\(s\\approx%s\\).' % (D(s24), D(F(round(math.sqrt(s24) * 100), 100)))))
assert (s24 * 10000).denominator == 1
P5a, P5b = [52, 48, 50, 51, 49, 50], [56, 44, 50, 58, 42, 50]; assert mean(P5a) == mean(P5b) == 50 and var(P5a) == F(5, 3) and var(P5b) == F(100, 3)
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Choosing a supplier', 'Chọn nhà cung cấp'), T('A bakery needs bags of flour of 50 kg. It weighs 6 bags from each supplier. A: \\(%s\\); B: \\(%s\\). Both have mean 50 kg. Which supplier should it choose? Use \\(R\\), \\(\\Delta_Q\\) and \\(s\\).' % (L(P5a, False), L(P5b, False)), 'Một tiệm bánh cần các bao bột 50 kg. Cân thử 6 bao của mỗi nhà cung cấp. A: \\(%s\\); B: \\(%s\\). Cả hai đều có trung bình 50 kg. Nên chọn nhà cung cấp nào? Dùng \\(R\\), \\(\\Delta_Q\\) và \\(s\\).' % (L(P5a), L(P5b))),
  T('Same mean: the decision depends on the spread.', 'Cùng trung bình: quyết định dựa vào độ phân tán.'),
  [T('A: \\(R=4\\), \\(Q_1=49\\), \\(Q_3=51\\), \\(\\Delta_Q=2\\), \\(s^2=\\dfrac{10}{6}\\approx1.67\\), \\(s\\approx1.29\\) kg.', 'A: \\(R=4\\), \\(Q_1=49\\), \\(Q_3=51\\), \\(\\Delta_Q=2\\), \\(s^2=\\dfrac{10}{6}\\approx1{,}67\\), \\(s\\approx1{,}29\\) kg.'),
   T('B: \\(R=16\\), \\(Q_1=44\\), \\(Q_3=56\\), \\(\\Delta_Q=12\\), \\(s^2=\\dfrac{200}{6}\\approx33.33\\), \\(s\\approx5.77\\) kg.', 'B: \\(R=16\\), \\(Q_1=44\\), \\(Q_3=56\\), \\(\\Delta_Q=12\\), \\(s^2=\\dfrac{200}{6}\\approx33{,}33\\), \\(s\\approx5{,}77\\) kg.')],
  T('All three measures are much smaller for A: choose supplier A (the bags are more even).', 'Cả ba số đều nhỏ hơn hẳn ở A: nên chọn nhà cung cấp A (các bao đều nhau hơn).'))
assert quartiles(P5a) == (49, 50, 51) and quartiles(P5b) == (44, 50, 56) and round(math.sqrt(F(5, 3)), 2) == 1.29 and round(math.sqrt(F(100, 3)), 2) == 5.77

def lvl(P):
    ctx, xs = P['d']; R = max(xs) - min(xs); q1, q2, q3 = quartiles(xs); dq = q3 - q1
    o1 = M4(1, '%s: \\(%s\\). The range is…' % (ctx[0], L(xs, False)), '%s: \\(%s\\). Khoảng biến thiên là…' % (ctx[1], L(xs)), str(R), [str(max(xs)), D(dq), str(R + 1), str(xs[-1] - xs[0]) if xs[-1] - xs[0] != R else str(R - 1)],
            '\\(R=%d-%d=%d\\).' % (max(xs), min(xs), R), '\\(R=%d-%d=%d\\).' % (max(xs), min(xs), R))
    o2 = M4(2, '%s: \\(%s\\). The interquartile range \\(\\Delta_Q\\) is…' % (ctx[0], L(xs, False)), '%s: \\(%s\\). Khoảng tứ phân vị \\(\\Delta_Q\\) là…' % (ctx[1], L(xs)), D(dq), [str(R), D(q3 - q2), D(dq + 1), D(q2 - q1) if q2 - q1 != dq else D(dq + 2)],
            '\\(Q_1=%s\\), \\(Q_3=%s\\), \\(\\Delta_Q=%s\\).' % (DE(q1), DE(q3), DE(dq)), '\\(Q_1=%s\\), \\(Q_3=%s\\), \\(\\Delta_Q=%s\\).' % (D(q1), D(q3), D(dq)))
    ys = P['v']; v = var(ys); m = mean(ys)
    o3 = M4(3, 'Sleeping hours of a student on 8 nights: \\(%s\\). The variance is…' % L(ys, False), 'Số giờ ngủ của một học sinh trong 8 đêm: \\(%s\\). Phương sai là…' % L(ys), D(v),
            [D(v * len(ys) / (len(ys) - 1)), D(F(sum(y * y for y in ys), len(ys))), D(v + 1), D(2 * v)], '\\(\\bar x=%s\\), \\(s^2=\\dfrac{\\sum(x_i-\\bar x)^2}{n}=%s\\).' % (DE(m), DE(v)), '\\(\\bar x=%s\\), \\(s^2=\\dfrac{\\sum(x_i-\\bar x)^2}{n}=%s\\).' % (D(m), D(v)))
    zs, claim = P['out']; o, lo, hi = outliers(zs); ok = claim in o
    t4 = tf(4, 'Prices (thousand VND) of a dish at several restaurants: \\(%s\\). The value %d is an outlier.' % (L(zs, False), claim), 'Giá (nghìn đồng) một món ăn ở một số quán: \\(%s\\). Giá trị %d là giá trị ngoại lai.' % (L(zs), claim), ok,
            'Fences: \\(%s\\) and \\(%s\\).' % (DE(lo), DE(hi)), 'Hai ngưỡng: \\(%s\\) và \\(%s\\).' % (D(lo), D(hi)))
    a, b = P['cmp']; ok5 = var(a) < var(b)
    t5 = tf(5, 'Goals per match of two strikers. P: \\(%s\\). Q: \\(%s\\). Striker P is more consistent (smaller variance).' % (L(a, False), L(b, False)), 'Số bàn thắng mỗi trận của hai tiền đạo. P: \\(%s\\). Q: \\(%s\\). Tiền đạo P thi đấu ổn định hơn (phương sai nhỏ hơn).' % (L(a), L(b)), ok5,
            '\\(s_P^2=%s\\), \\(s_Q^2=%s\\).' % (DE(var(a)), DE(var(b))), '\\(s_P^2=%s\\), \\(s_Q^2=%s\\).' % (D(var(a)), D(var(b))))
    ws = P['s6']; v6 = var(ws); assert (100 * v6).denominator == 1
    s6 = sh(6, 'Find the variance of the data \\(%s\\).' % L(ws, False), 'Tính phương sai của mẫu số liệu \\(%s\\).' % L(ws), DE(v6), '\\(\\bar x=%s\\), \\(s^2=%s\\).' % (DE(mean(ws)), DE(v6)), '\\(\\bar x=%s\\), \\(s^2=%s\\).' % (D(mean(ws)), D(v6)))
    us = P['s7']; v7 = var(us); sd = math.isqrt(v7.numerator); assert v7.denominator == 1 and sd * sd == v7
    s7 = sh(7, 'Masses (kg) of some watermelons: \\(%s\\). Find the standard deviation.' % L(us, False), 'Khối lượng (kg) của một số quả dưa hấu: \\(%s\\). Tính độ lệch chuẩn.' % L(us), sd,
            '\\(\\bar x=%s\\), \\(s^2=%s\\), \\(s=%d\\).' % (DE(mean(us)), DE(v7), sd), '\\(\\bar x=%s\\), \\(s^2=%s\\), \\(s=%d\\).' % (D(mean(us)), D(v7), sd))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
PP = [dict(d=(('Points scored by a team in 8 games', 'Số điểm của một đội trong 8 trận'), [65, 72, 58, 80, 69, 75, 61, 70]), v=[7, 8, 6, 9, 8, 7, 8, 7], out=([30, 32, 35, 33, 31, 34, 60, 32, 33], 60), cmp=([1, 2, 1, 2, 1, 2], [0, 3, 0, 4, 1, 1]), s6=[4, 6, 8, 10, 12], s7=[4, 12, 12, 6, 10, 10]),
      dict(d=(('Minutes of daily exercise in 9 days', 'Số phút tập thể dục mỗi ngày trong 9 ngày'), [30, 45, 20, 35, 40, 25, 50, 30, 45]), v=[6, 7, 7, 8, 6, 5, 9, 8], out=([25, 28, 30, 27, 26, 29, 31, 40], 25), cmp=([0, 3, 1, 2, 0, 3], [1, 2, 2, 1, 2, 1]), s6=[3, 5, 6, 9, 12], s7=[2, 16, 16, 7, 8, 11]),
      dict(d=(('Weekly pocket money (thousand VND) of 10 students', 'Tiền tiêu vặt mỗi tuần (nghìn đồng) của 10 học sinh'), [50, 80, 40, 100, 60, 70, 90, 60, 120, 30]), v=[7, 6, 8, 7, 9, 5, 7, 7], out=([45, 50, 48, 52, 47, 49, 51, 20, 50, 46], 20), cmp=([2, 2, 3, 1, 2, 2], [4, 0, 2, 3, 1, 2]), s6=[10, 12, 15, 17, 21], s7=[17, 10, 5, 16, 11, 13])]
practice = three(lvl, PP)
practice = with_self(practice, S.M14S10, start=8)
mistakes = [('<b>\\(R\\) from the first and last values listed.</b> Use the largest and smallest values.', '<b>Lấy giá trị đầu và cuối dãy để tính \\(R\\).</b> Phải dùng giá trị lớn nhất và nhỏ nhất.'),
            ('<b>Forgetting to subtract \\(\\bar x^2\\).</b> \\(s^2=\\dfrac1n\\sum x_i^2-\\bar x^2\\).', '<b>Quên trừ \\(\\bar x^2\\).</b> \\(s^2=\\dfrac1n\\sum x_i^2-\\bar x^2\\).'),
            ('<b>Mixing up \\(s\\) and \\(s^2\\).</b> \\(s\\) is the square root, in the unit of the data.', '<b>Nhầm \\(s\\) với \\(s^2\\).</b> \\(s\\) là căn bậc hai, cùng đơn vị với số liệu.'),
            ('<b>Deleting outliers automatically.</b> First check whether they are errors or real special cases.', '<b>Tự động xóa giá trị ngoại lai.</b> Trước hết phải kiểm tra đó là sai sót hay trường hợp đặc biệt có thật.')]
summary = [('\\(R=x_{\\max}-x_{\\min}\\); \\(\\Delta_Q=Q_3-Q_1\\).', '\\(R=x_{\\max}-x_{\\min}\\); \\(\\Delta_Q=Q_3-Q_1\\).'),
           ('Outlier: \\(x\\gt Q_3+1.5\\Delta_Q\\) or \\(x\\lt Q_1-1.5\\Delta_Q\\).', 'Giá trị ngoại lai: \\(x\\gt Q_3+1{,}5\\Delta_Q\\) hoặc \\(x\\lt Q_1-1{,}5\\Delta_Q\\).'),
           ('\\(s^2=\\dfrac1n\\sum(x_i-\\bar x)^2=\\dfrac1n\\sum x_i^2-\\bar x^2\\); \\(s=\\sqrt{s^2}\\).', '\\(s^2=\\dfrac1n\\sum(x_i-\\bar x)^2=\\dfrac1n\\sum x_i^2-\\bar x^2\\); \\(s=\\sqrt{s^2}\\).'),
           ('Smaller spread = more stable. Key words: range, interquartile range, variance, standard deviation, outlier.', 'Độ phân tán nhỏ hơn thì ổn định hơn. Từ cần nhớ: range, interquartile range, variance, standard deviation, outlier.')]
checks = [('I can find \\(R\\) and \\(\\Delta_Q\\).', 'Em tìm được \\(R\\) và \\(\\Delta_Q\\).'), ('I can detect outliers.', 'Em phát hiện được giá trị ngoại lai.'),
          ('I can compute the variance and the standard deviation.', 'Em tính được phương sai và độ lệch chuẩn.'), ('I can compare the stability of two samples.', 'Em so sánh được độ ổn định của hai mẫu.')]
LL('g10-stats-03', 'Measures of Dispersion', CV, ('Statistics', 'Các số đặc trưng của mẫu số liệu không ghép nhóm'), 'statistics', 'dispersion', 140, 'Intermediate', 65, ('mean, median, quartiles', 'số trung bình, trung vị, tứ phân vị'),
   'Range, interquartile range, outliers, variance and standard deviation of ungrouped data; comparing stability.', 'Bài 14 – Khoảng biến thiên, khoảng tứ phân vị, giá trị ngoại lai, phương sai, độ lệch chuẩn của mẫu số liệu không ghép nhóm.',
   ['range', 'interquartile range', 'variance', 'standard deviation', 'outlier'], ['khoảng biến thiên', 'khoảng tứ phân vị', 'phương sai', 'độ lệch chuẩn', 'giá trị ngoại lai'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g10-stats-02'])
