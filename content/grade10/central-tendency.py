# -*- coding: utf-8 -*-
"""g10-stats-02 = Toán 10 KNTT, Bài 13: Các số đặc trưng đo xu thế trung tâm. Mã ngân hàng câu hỏi: TOAN10-C5-B13."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g10e as S
from sp_g10e import mean, median, quartiles, modes, L, D, DE

def HT(r1, r2):
    """Bảng ngang 2 hàng, kẻ đủ đường (chuẩn trình bày bảng tần số của SGK)."""
    return TBL([TI(*r1[0])] + [str(x) for x in r1[1]], [[TI(*r2[0])] + [str(x) for x in r2[1]]])
CV = 'Các số đặc trưng đo xu thế trung tâm'
vocab = defs(CV, [
 ('mean10', 'mean (average)', 'số trung bình', 'the sum of all values divided by the number of values: \\(\\bar x=\\dfrac{x_1+\\dots+x_n}{n}\\).', 'tổng các giá trị chia cho số giá trị: \\(\\bar x=\\dfrac{x_1+\\dots+x_n}{n}\\).', 'The mean mark is 7.5.', '\\(\\bar x\\)'),
 ('med10', 'median', 'trung vị', 'the middle value of the sorted data (or the average of the two middle values).', 'giá trị đứng giữa của mẫu đã sắp xếp (hoặc trung bình cộng của hai giá trị đứng giữa).', 'The median is not affected by one extreme value.', '\\(M_e\\)'),
 ('quart10', 'quartiles', 'tứ phân vị', 'three values \\(Q_1, Q_2, Q_3\\) that split the sorted data into four parts of about the same size.', 'ba giá trị \\(Q_1, Q_2, Q_3\\) chia mẫu đã sắp xếp thành bốn phần có số giá trị xấp xỉ nhau.', 'The first quartile is 12.', '\\(Q_1,Q_2,Q_3\\)'),
 ('mode10', 'mode', 'mốt', 'the value with the largest frequency.', 'giá trị có tần số lớn nhất.', 'The mode of the shoe sizes is 39.', '\\(M_o\\)'),
 ('freq10', 'frequency', 'tần số', 'the number of times a value appears.', 'số lần một giá trị xuất hiện.', 'The value 8 has frequency 5.', '\\(n_i\\)'),
 ('extreme', 'extreme value (outlier)', 'giá trị bất thường', 'a value much larger or much smaller than the others.', 'giá trị quá lớn hoặc quá nhỏ so với các giá trị khác.', 'The extreme value pulls the mean up.', '')])
goals = [('compute the mean (also from a frequency table);', 'tính [[số trung bình]] (cả khi cho bảng [[tần số]]);'),
         ('find the median and the quartiles by the method of the textbook;', 'tìm [[trung vị]] và [[tứ phân vị]] theo đúng cách của SGK;'),
         ('find the mode;', 'tìm [[mốt]];'),
         ('choose a suitable measure when the data have extreme values.', 'chọn số đặc trưng phù hợp khi mẫu có [[giá trị bất thường]].')]
phrases = [('<b>Find the mean of the data.</b>', 'Tìm số trung bình của mẫu số liệu.'), ('<b>Sort the data in increasing order.</b>', 'Sắp xếp số liệu theo thứ tự tăng dần.'), ('<b>Find the median and the quartiles.</b>', 'Tìm trung vị và các tứ phân vị.'),
           ('<b>Which value appears most often?</b>', 'Giá trị nào xuất hiện nhiều nhất?'), ('<b>The median describes the data better.</b>', 'Trung vị mô tả mẫu số liệu tốt hơn.')]
review = T('From lower grades: a data sample is a list of values \\(x_1,\\dots,x_n\\); \\(n\\) is the sample size. A frequency table lists each value \\(x_i\\) and its frequency \\(n_i\\), with \\(n_1+\\dots+n_k=n\\).', 'Từ lớp dưới: mẫu số liệu là dãy giá trị \\(x_1,\\dots,x_n\\); \\(n\\) là cỡ mẫu. Bảng tần số ghi mỗi giá trị \\(x_i\\) và tần số \\(n_i\\), với \\(n_1+\\dots+n_k=n\\).')
theory = '<h3>13.1 %s</h3>' % TI('The mean', 'Số trung bình')
theory += BOX('blue', ('Formulas', 'Công thức'), M('\\bar x=\\dfrac{x_1+x_2+\\dots+x_n}{n},\\qquad \\bar x=\\dfrac{n_1x_1+n_2x_2+\\dots+n_kx_k}{n}\\ \\text{(bảng tần số)}'),
  T('The mean uses every value, so it is a good "centre" when the data have no extreme values.', 'Số trung bình dùng mọi giá trị nên là đại diện tốt khi mẫu không có giá trị bất thường.'))
theory += '<h3>13.2 %s</h3>' % TI('Median and quartiles', 'Trung vị và tứ phân vị')
theory += BOX('mint', ('Median \\(M_e\\)', 'Trung vị \\(M_e\\)'), UL([T('Sort the data. If \\(n\\) is odd, \\(M_e\\) is the middle value (position \\(\\frac{n+1}{2}\\)).', 'Sắp xếp mẫu theo thứ tự không giảm. Nếu \\(n\\) lẻ, \\(M_e\\) là giá trị đứng giữa (vị trí \\(\\frac{n+1}{2}\\)).'),
  T('If \\(n\\) is even, \\(M_e\\) is the mean of the two middle values (positions \\(\\frac n2\\) and \\(\\frac n2+1\\)).', 'Nếu \\(n\\) chẵn, \\(M_e\\) là trung bình cộng của hai giá trị đứng giữa (vị trí \\(\\frac n2\\) và \\(\\frac n2+1\\)).')]))
theory += BOX('blue', ('Quartiles \\(Q_1, Q_2, Q_3\\)', 'Tứ phân vị \\(Q_1, Q_2, Q_3\\)'), UL([T('\\(Q_2=M_e\\).', '\\(Q_2=M_e\\).'),
  T('\\(Q_1\\) is the median of the lower half, \\(Q_3\\) the median of the upper half. When \\(n\\) is odd, <b>do not include</b> \\(M_e\\) in the two halves.', '\\(Q_1\\) là trung vị của nửa số liệu bên trái, \\(Q_3\\) là trung vị của nửa bên phải. Khi \\(n\\) lẻ, <b>không tính</b> \\(M_e\\) vào hai nửa.')]))
X1 = [3, 5, 6, 7, 8, 9, 10, 12, 13, 15, 20]; assert quartiles(X1) == (6, 9, 13)
theory += TBL([TI('Position', 'Vị trí')] + [str(i + 1) for i in range(11)], [[TI('Value', 'Giá trị')] + ['<b>%d</b>' % x if x in (6, 9, 13) else str(x) for x in X1]])
theory += '<p class="mbl-note">%s</p>' % TI('\\(n=11\\): \\(Q_2=9\\) (6th value); lower half \\(3,5,6,7,8\\) gives \\(Q_1=6\\); upper half \\(10,12,13,15,20\\) gives \\(Q_3=13\\).', '\\(n=11\\): \\(Q_2=9\\) (giá trị thứ 6); nửa trái \\(3,5,6,7,8\\) cho \\(Q_1=6\\); nửa phải \\(10,12,13,15,20\\) cho \\(Q_3=13\\).')
theory += '<h3>13.3 %s</h3>' % TI('The mode', 'Mốt')
theory += BOX('mint', ('Mode \\(M_o\\)', 'Mốt \\(M_o\\)'), T('The value with the largest frequency. A sample may have more than one mode. The mode is useful for "most common" questions (shoe sizes, favourite colours).', 'Giá trị có tần số lớn nhất. Một mẫu có thể có nhiều mốt. Mốt hữu ích khi hỏi "phổ biến nhất" (cỡ giày, màu sắc ưa thích).'))
theory += BOX('yellow', ('Which measure?', 'Chọn số đặc trưng nào?'), T('Extreme values pull the mean but hardly change the median. With extreme values, prefer the median (and quartiles); otherwise the mean is fine.', 'Giá trị bất thường kéo lệch số trung bình nhưng hầu như không ảnh hưởng trung vị. Khi mẫu có giá trị bất thường, nên dùng trung vị (và tứ phân vị); nếu không, dùng số trung bình.'))

E1 = [2, 3, 3, 4, 5, 5, 5, 6]; assert (mean(E1), median(E1), modes(E1)[0]) == (F(33, 8), F(9, 2), [5])
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Self-study hours', 'Giờ tự học'), T('Hours of self-study per day of 8 students: \\(%s\\). Find the mean, the median and the mode.' % L(E1, False), 'Số giờ tự học mỗi ngày của 8 bạn: \\(%s\\). Tìm số trung bình, trung vị và mốt.' % L(E1)),
  T('The data are already sorted; \\(n=8\\) is even.', 'Mẫu đã sắp xếp; \\(n=8\\) chẵn.'),
  [T('\\(\\bar x=\\dfrac{33}{8}=4.125\\).', '\\(\\bar x=\\dfrac{33}{8}=4{,}125\\).'), T('\\(M_e=\\dfrac{4+5}{2}=4.5\\) (4th and 5th values).', '\\(M_e=\\dfrac{4+5}{2}=4{,}5\\) (giá trị thứ 4 và 5).'), T('5 appears 3 times: \\(M_o=5\\).', 'Giá trị 5 xuất hiện 3 lần: \\(M_o=5\\).')],
  T('\\(\\bar x=4.125\\) h, \\(M_e=4.5\\) h, \\(M_o=5\\) h.', '\\(\\bar x=4{,}125\\) giờ, \\(M_e=4{,}5\\) giờ, \\(M_o=5\\) giờ.'))
V2, N2 = [36, 37, 38, 39, 40, 41], [3, 7, 12, 15, 9, 4]; n2 = sum(N2); m2 = F(sum(v * f for v, f in zip(V2, N2)), n2); assert n2 == 50 and m2 == F(1932, 50)
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Shoe sizes', 'Cỡ giày'), T('A shop sold 50 pairs of sport shoes: %s Find the mean size and the mode. Which size should the shop order the most?' % HT((('Size', 'Cỡ giày'), V2), (('Pairs sold', 'Số đôi bán'), N2)), 'Một cửa hàng bán 50 đôi giày thể thao: %s Tìm cỡ giày trung bình và mốt. Cửa hàng nên nhập nhiều nhất cỡ nào?' % HT((('Size', 'Cỡ giày'), V2), (('Pairs sold', 'Số đôi bán'), N2))),
  T('Use \\(\\bar x=\\dfrac{\\sum n_ix_i}{n}\\).', 'Dùng \\(\\bar x=\\dfrac{\\sum n_ix_i}{n}\\).'),
  [T('\\(\\sum n_ix_i=36\\cdot3+37\\cdot7+38\\cdot12+39\\cdot15+40\\cdot9+41\\cdot4=1932\\); \\(\\bar x=\\dfrac{1932}{50}=38.64\\).', '\\(\\sum n_ix_i=36\\cdot3+37\\cdot7+38\\cdot12+39\\cdot15+40\\cdot9+41\\cdot4=1932\\); \\(\\bar x=\\dfrac{1932}{50}=38{,}64\\).'), T('Largest frequency 15: \\(M_o=39\\).', 'Tần số lớn nhất là 15: \\(M_o=39\\).')],
  T('\\(\\bar x=38.64\\), \\(M_o=39\\). Order size 39 the most: a "size 38.64" does not exist, so the mode is the useful measure here.', '\\(\\bar x=38{,}64\\), \\(M_o=39\\). Nên nhập nhiều nhất cỡ 39: không có giày "cỡ 38,64" nên mốt mới là số đặc trưng có ích ở đây.'))
E3 = [24, 18, 30, 21, 27, 15, 33, 20, 26, 22]; s3 = sorted(E3); q3 = quartiles(E3); assert q3 == (20, 23, 27)
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Quartiles with an even \\(n\\)', 'Tứ phân vị khi \\(n\\) chẵn'), T('Minutes 10 students spend travelling to school: \\(%s\\). Find \\(Q_1, Q_2, Q_3\\).' % L(E3, False), 'Thời gian (phút) đến trường của 10 bạn: \\(%s\\). Tìm \\(Q_1, Q_2, Q_3\\).' % L(E3)),
  T('Sort first; with \\(n=10\\) each half has 5 values.', 'Sắp xếp trước; với \\(n=10\\) mỗi nửa có 5 giá trị.'),
  [T('Sorted: \\(%s\\).' % L(s3, False), 'Sắp xếp: \\(%s\\).' % L(s3)), T('\\(Q_2=\\dfrac{%d+%d}{2}=%s\\) (5th and 6th values).' % (s3[4], s3[5], DE(q3[1])), '\\(Q_2=\\dfrac{%d+%d}{2}=%s\\) (giá trị thứ 5 và 6).' % (s3[4], s3[5], D(q3[1]))),
   T('Lower half \\(%s\\): \\(Q_1=%d\\). Upper half \\(%s\\): \\(Q_3=%d\\).' % (L(s3[:5], False), q3[0], L(s3[5:], False), q3[2]), 'Nửa trái \\(%s\\): \\(Q_1=%d\\). Nửa phải \\(%s\\): \\(Q_3=%d\\).' % (L(s3[:5]), q3[0], L(s3[5:]), q3[2]))],
  T('\\(Q_1=20\\), \\(Q_2=23\\), \\(Q_3=27\\) (minutes).', '\\(Q_1=20\\), \\(Q_2=23\\), \\(Q_3=27\\) (phút).'))
E4 = [8, 9, 9, 10, 10, 11, 12, 12, 13, 106]; assert (mean(E4), median(E4)) == (20, F(21, 2))
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Mean or median?', 'Số trung bình hay trung vị?'), T('Monthly salaries (million VND) at a small company: \\(%s\\) (the last one is the director). The company says: "The average salary is 20 million". Is this a fair description?' % L(E4, False), 'Lương hằng tháng (triệu đồng) ở một công ty nhỏ: \\(%s\\) (người cuối là giám đốc). Công ty nói: "Lương trung bình là 20 triệu". Mô tả này có hợp lí không?' % L(E4)),
  T('Compare the mean with the median.', 'So sánh số trung bình với trung vị.'),
  [T('\\(\\bar x=\\dfrac{200}{10}=20\\), but 9 out of 10 people earn at most 13 million.', '\\(\\bar x=\\dfrac{200}{10}=20\\), nhưng 9 trên 10 người có lương không quá 13 triệu.'), T('\\(M_e=\\dfrac{10+11}{2}=10.5\\).', '\\(M_e=\\dfrac{10+11}{2}=10{,}5\\).')],
  T('Not fair: the extreme value 106 pulls the mean up. The median 10.5 million describes a typical salary better.', 'Không hợp lí: giá trị bất thường 106 kéo số trung bình lên cao. Trung vị 10,5 triệu đại diện tốt hơn cho mức lương điển hình.'))
assert sum(E4) == 200
E5a, E5b = [6, 7, 7, 8, 8, 8, 9, 9], [5, 6, 6, 8, 9, 9, 9, 10]
assert mean(E5a) == mean(E5b) == F(31, 4) and (median(E5a), median(E5b)) == (8, F(17, 2)) and quartiles(E5a)[0] == 7 and quartiles(E5b)[0] == 6
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Two teams', 'Hai đội tuyển'), T('Scores of two teams in a quiz. Team A: \\(%s\\). Team B: \\(%s\\). Compare the two teams with the mean, the median and \\(Q_1\\).' % (L(E5a, False), L(E5b, False)), 'Điểm thi đấu của hai đội. Đội A: \\(%s\\). Đội B: \\(%s\\). So sánh hai đội qua số trung bình, trung vị và \\(Q_1\\).' % (L(E5a), L(E5b))),
  T('Same mean does not mean the same distribution.', 'Cùng số trung bình chưa chắc phân bố giống nhau.'),
  [T('Both means are \\(\\dfrac{62}{8}=7.75\\).', 'Cả hai số trung bình đều bằng \\(\\dfrac{62}{8}=7{,}75\\).'), T('A: \\(M_e=8\\), \\(Q_1=7\\). B: \\(M_e=8.5\\), \\(Q_1=6\\).', 'A: \\(M_e=8\\), \\(Q_1=7\\). B: \\(M_e=8{,}5\\), \\(Q_1=6\\).')],
  T('Team B has a higher median (its stronger half is better) but a lower \\(Q_1\\) (its weaker members are weaker): team B is less even. Team A is more uniform.', 'Đội B có trung vị cao hơn (nửa trên mạnh hơn) nhưng \\(Q_1\\) thấp hơn (các thành viên yếu hơn yếu hơn): đội B kém đồng đều; đội A đồng đều hơn.'))

def lvl(P):
    ctx, xs = P['d']; m = mean(xs); me = median(xs); q1, q2, q3 = quartiles(xs); s = sorted(xs)
    o1 = M4(1, '%s: \\(%s\\). The mean is…' % (ctx[0], L(xs, False)), '%s: \\(%s\\). Số trung bình là…' % (ctx[1], L(xs)), D(m), [D(me), D(F(sum(xs), len(xs) - 1)), D(m + 1), D(F(max(xs) + min(xs), 2))],
            '\\(\\bar x=\\dfrac{%d}{%d}=%s\\).' % (sum(xs), len(xs), DE(m)), '\\(\\bar x=\\dfrac{%d}{%d}=%s\\).' % (sum(xs), len(xs), D(m)))
    o2 = M4(2, '%s: \\(%s\\). The median is…' % (ctx[0], L(xs, False)), '%s: \\(%s\\). Trung vị là…' % (ctx[1], L(xs)), D(me), [D(xs[len(xs) // 2]), D(m), D(s[len(s) // 2 - 1]), D(me + 1)],
            'Sorted \\(%s\\): \\(M_e=%s\\).' % (L(s, False), DE(me)), 'Sắp xếp \\(%s\\): \\(M_e=%s\\).' % (L(s), D(me)))
    o3 = M4(3, '%s: \\(%s\\). The first quartile \\(Q_1\\) is…' % (ctx[0], L(xs, False)), '%s: \\(%s\\). Tứ phân vị thứ nhất \\(Q_1\\) là…' % (ctx[1], L(xs)), D(q1), [D(q3), D(q2), D(q1 + 1), D(s[len(s) // 4])],
            '\\(Q_1\\) is the median of the lower half: \\(Q_1=%s\\) (\\(Q_3=%s\\)).' % (DE(q1), DE(q3)), '\\(Q_1\\) là trung vị của nửa trái: \\(Q_1=%s\\) (\\(Q_3=%s\\)).' % (D(q1), D(q3)))
    ys, claim = P['mode']; mo, k = modes(ys); ok = [claim] == mo
    t4 = tf(4, 'Votes for favourite fruit (coded): \\(%s\\). The mode is %d.' % (L(ys, False), claim), 'Kết quả bình chọn loại quả yêu thích (đã mã hóa): \\(%s\\). Mốt của mẫu là %d.' % (L(ys), claim), ok,
            'The mode is %s (frequency %d).' % (' and '.join(map(str, mo)), k), 'Mốt là %s (tần số %d).' % (' và '.join(map(str, mo)), k))
    zs, extra = P['ext']; t5ok = abs(median(zs + [extra]) - median(zs)) < abs(mean(zs + [extra]) - mean(zs))
    t5 = tf(5, 'Data \\(%s\\). Adding the value %d changes the median less than it changes the mean.' % (L(zs, False), extra), 'Mẫu \\(%s\\). Thêm giá trị %d vào mẫu thì trung vị thay đổi ít hơn số trung bình.' % (L(zs), extra), t5ok,
            'Mean: \\(%s\\to%s\\); median: \\(%s\\to%s\\).' % (DE(mean(zs)), DE(mean(zs + [extra])), DE(median(zs)), DE(median(zs + [extra]))), 'Trung bình: \\(%s\\to%s\\); trung vị: \\(%s\\to%s\\).' % (D(mean(zs)), D(mean(zs + [extra])), D(median(zs)), D(median(zs + [extra]))))
    vals, fs = P['ft']; n = sum(fs); mf = F(sum(v * f for v, f in zip(vals, fs)), n); assert (100 * mf).denominator == 1
    s6 = sh(6, 'Number of books read in a month by students: %s Find the mean.' % HT((('Books', 'Số sách'), vals), (('Students', 'Số học sinh'), fs)), 'Số sách đọc trong một tháng của các học sinh: %s Tính số sách trung bình.' % HT((('Books', 'Số sách'), vals), (('Students', 'Số học sinh'), fs)), DE(mf),
            '\\(\\bar x=\\dfrac{%d}{%d}=%s\\).' % (sum(v * f for v, f in zip(vals, fs)), n, DE(mf)), '\\(\\bar x=\\dfrac{%d}{%d}=%s\\).' % (sum(v * f for v, f in zip(vals, fs)), n, D(mf)))
    n7, m7, known = P['miss']; x = n7 * m7 - sum(known); assert x > 0
    s7 = sh(7, 'A runner\'s times (s) in %d races have mean %d. Times of %d races are \\(%s\\). Find the time of the last race.' % (n7, m7, n7 - 1, L(known, False)), 'Thành tích (giây) của một vận động viên trong %d lần chạy có trung bình %d. %d lần đầu là \\(%s\\). Tìm thành tích lần cuối.' % (n7, m7, n7 - 1, L(known)), x,
            'Total \\(=%d\\cdot%d=%d\\); last \\(=%d-%d=%d\\).' % (n7, m7, n7 * m7, n7 * m7, sum(known), x), 'Tổng \\(=%d\\cdot%d=%d\\); lần cuối \\(=%d-%d=%d\\).' % (n7, m7, n7 * m7, n7 * m7, sum(known), x))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
PP = [dict(d=(('Marks of 9 students', 'Điểm của 9 học sinh'), [7, 5, 8, 9, 6, 8, 10, 7, 8]), mode=([1, 3, 2, 3, 4, 3, 2, 1, 3, 2], 3), ext=([5, 6, 7, 8, 9], 40), ft=([1, 2, 3, 4], [6, 10, 3, 1]), miss=(5, 13, [12, 14, 13, 12])),
      dict(d=(('Daily step counts (thousands) in 10 days', 'Số bước chân (nghìn bước) trong 10 ngày'), [8, 12, 6, 10, 9, 15, 7, 11, 9, 13]), mode=([2, 4, 4, 1, 2, 5, 2, 4, 3, 1], 4), ext=([20, 22, 23, 25], 21), ft=([0, 1, 2, 3, 4], [2, 5, 8, 3, 2]), miss=(6, 15, [14, 16, 15, 13, 17])),
      dict(d=(('Heights (cm) of 12 seedlings', 'Chiều cao (cm) của 12 cây giống'), [14, 18, 11, 16, 20, 13, 17, 15, 19, 12, 22, 15]), mode=([5, 5, 6, 7, 7, 8, 6, 5, 7, 5], 5), ext=([30, 32, 35, 36, 38, 41], 120), ft=([2, 3, 4, 5], [4, 9, 5, 2]), miss=(8, 12, [11, 13, 12, 10, 14, 12, 11]))]
practice = three(lvl, PP)
practice = with_self(practice, S.M13S10, start=8)
mistakes = [('<b>Not sorting.</b> The median and quartiles are found on the <b>sorted</b> data.', '<b>Quên sắp xếp.</b> Trung vị và tứ phân vị phải tìm trên mẫu <b>đã sắp xếp</b>.'),
            ('<b>Including \\(M_e\\) in the halves when \\(n\\) is odd.</b> The textbook leaves it out.', '<b>Tính cả \\(M_e\\) vào hai nửa khi \\(n\\) lẻ.</b> Theo SGK, không tính trung vị vào hai nửa.'),
            ('<b>Mode = largest frequency.</b> The mode is the <b>value</b>, not its frequency.', '<b>Mốt = tần số lớn nhất.</b> Mốt là <b>giá trị</b> có tần số lớn nhất, không phải tần số đó.'),
            ('<b>Using the mean with extreme values.</b> It can be far from most of the data; use the median.', '<b>Dùng số trung bình khi có giá trị bất thường.</b> Nó có thể xa phần lớn số liệu; nên dùng trung vị.')]
summary = [('\\(\\bar x=\\dfrac{\\sum x_i}{n}=\\dfrac{\\sum n_ix_i}{n}\\).', '\\(\\bar x=\\dfrac{\\sum x_i}{n}=\\dfrac{\\sum n_ix_i}{n}\\).'),
           ('\\(M_e\\): middle value(s) of the sorted data. \\(Q_1,Q_3\\): medians of the two halves (without \\(M_e\\) when \\(n\\) is odd).', '\\(M_e\\): giá trị (hai giá trị) đứng giữa của mẫu đã sắp xếp. \\(Q_1,Q_3\\): trung vị của hai nửa (không tính \\(M_e\\) khi \\(n\\) lẻ).'),
           ('\\(M_o\\): the value with the largest frequency.', '\\(M_o\\): giá trị có tần số lớn nhất.'),
           ('With extreme values prefer the median. Key words: mean, median, quartile, mode.', 'Khi có giá trị bất thường, ưu tiên trung vị. Từ cần nhớ: mean, median, quartile, mode.')]
checks = [('I can compute the mean, also from a frequency table.', 'Em tính được số trung bình, kể cả từ bảng tần số.'), ('I can find the median and the quartiles.', 'Em tìm được trung vị và tứ phân vị.'),
          ('I can find the mode.', 'Em tìm được mốt.'), ('I can choose a suitable measure for real data.', 'Em chọn được số đặc trưng phù hợp với số liệu thực tế.')]
LL('g10-stats-02', 'Measures of Central Tendency', CV, ('Statistics', 'Các số đặc trưng của mẫu số liệu không ghép nhóm'), 'statistics', 'central-tendency', 130, 'Beginner', 60, ('data samples, frequency tables', 'mẫu số liệu, bảng tần số'),
   'Mean, median, quartiles and mode of ungrouped data; choosing a measure when there are extreme values.', 'Bài 13 – Số trung bình, trung vị, tứ phân vị, mốt của mẫu số liệu không ghép nhóm; chọn số đặc trưng phù hợp.',
   ['mean', 'median', 'quartile', 'mode'], ['số trung bình', 'trung vị', 'tứ phân vị', 'mốt'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g10-stats-01'])
