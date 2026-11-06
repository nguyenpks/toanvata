# -*- coding: utf-8 -*-
"""g12-stats-02 = Toán 12 KNTT, Bài 10: Phương sai và độ lệch chuẩn. Mã ngân hàng câu hỏi: TOAN12-C3-B10."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g12c as S
from sp_g12c import VT, D, DE, r2
from gdata import GT

CV = 'Phương sai và độ lệch chuẩn'
vocab = defs(CV, [
 ('varc', 'variance', 'phương sai', 'the mean of the squared deviations from the mean: \\(s^2=\\dfrac1n\\sum n_i(x_i-\\bar x)^2\\).', 'trung bình cộng của bình phương các độ lệch so với số trung bình: \\(s^2=\\dfrac1n\\sum n_i(x_i-\\bar x)^2\\).', 'The variance is 86.', '\\(s^2\\)'),
 ('stdv', 'standard deviation', 'độ lệch chuẩn', 'the square root of the variance, \\(s=\\sqrt{s^2}\\); it has the same unit as the data.', 'căn bậc hai của phương sai, \\(s=\\sqrt{s^2}\\); cùng đơn vị với số liệu.', 'The standard deviation is about 9.27 points.', '\\(s\\)'),
 ('devi', 'deviation from the mean', 'độ lệch so với số trung bình', 'the difference \\(x_i-\\bar x\\).', 'hiệu \\(x_i-\\bar x\\).', 'A large deviation means a value far from the mean.', ''),
 ('midv', 'midpoint (class mark)', 'giá trị đại diện', 'the middle of a group, \\(x_i=\\dfrac{u_i+u_{i+1}}2\\).', 'giá trị chính giữa của nhóm, \\(x_i=\\dfrac{u_i+u_{i+1}}2\\).', 'The midpoint of \\([60;70)\\) is 65.', '\\(x_i\\)'),
 ('stab', 'stable (consistent)', 'ổn định (đồng đều)', 'having a small spread around the mean.', 'ít phân tán quanh số trung bình.', 'Machine B is more stable.', '')])
goals = [('compute the variance of grouped data with the two formulas;', 'tính [[phương sai]] của mẫu số liệu ghép nhóm bằng hai công thức;'),
         ('find the standard deviation and state its unit;', 'tìm [[độ lệch chuẩn]] và nêu đơn vị;'),
         ('explain what a large or small standard deviation means;', 'giải thích ý nghĩa của độ lệch chuẩn lớn hay nhỏ;'),
         ('compare the stability of two samples in real situations.', 'so sánh mức độ [[ổn định (đồng đều)]] của hai mẫu số liệu trong thực tế.')]
phrases = [('<b>Compute the variance of the grouped data.</b>', 'Tính phương sai của mẫu số liệu ghép nhóm.'), ('<b>Find the standard deviation, rounded to the hundredths.</b>', 'Tìm độ lệch chuẩn, làm tròn đến hàng phần trăm.'),
           ('<b>Which machine is more stable?</b>', 'Máy nào hoạt động ổn định hơn?'), ('<b>The data are more spread out.</b>', 'Số liệu phân tán hơn.'), ('<b>Use the midpoints of the groups.</b>', 'Dùng giá trị đại diện của các nhóm.')]
review = T('From Bài 9 and Grade 11: for grouped data with groups \\([u_i;u_{i+1})\\), the midpoint is \\(x_i=\\dfrac{u_i+u_{i+1}}2\\) and the mean is \\(\\bar x=\\dfrac{n_1x_1+\\dots+n_kx_k}{n}\\). The range and the interquartile range measure spread but use only a few values.',
           'Từ Bài 9 và lớp 11: với mẫu ghép nhóm có các nhóm \\([u_i;u_{i+1})\\), [[giá trị đại diện]] là \\(x_i=\\dfrac{u_i+u_{i+1}}2\\) và số trung bình \\(\\bar x=\\dfrac{n_1x_1+\\dots+n_kx_k}{n}\\). Khoảng biến thiên và khoảng tứ phân vị đo độ phân tán nhưng chỉ dùng một vài giá trị.')
LB = lambda g, f: {'group': g, 'freq': f}
theory = '<h3>10.1 %s</h3>' % TI('Variance and standard deviation of grouped data', 'Phương sai và độ lệch chuẩn của mẫu số liệu ghép nhóm')
theory += BOX('blue', ('Definition', 'Định nghĩa'), T('A grouped sample has \\(k\\) groups with midpoints \\(x_1,\\dots,x_k\\), frequencies \\(n_1,\\dots,n_k\\), size \\(n=n_1+\\dots+n_k\\) and mean \\(\\bar x\\).', 'Mẫu số liệu ghép nhóm có \\(k\\) nhóm với giá trị đại diện \\(x_1,\\dots,x_k\\), tần số \\(n_1,\\dots,n_k\\), cỡ mẫu \\(n=n_1+\\dots+n_k\\) và số trung bình \\(\\bar x\\).'),
  M('s^2=\\dfrac1n\\left[n_1(x_1-\\bar x)^2+\\dots+n_k(x_k-\\bar x)^2\\right]=\\dfrac1n\\left(n_1x_1^2+\\dots+n_kx_k^2\\right)-\\bar x^2'),
  T('\\(s^2\\) is the variance, \\(s=\\sqrt{s^2}\\) the standard deviation.', '\\(s^2\\) là [[phương sai]], \\(s=\\sqrt{s^2}\\) là [[độ lệch chuẩn]] của mẫu số liệu ghép nhóm.'))
theory += BOX('mint', ('Steps', 'Các bước tính'), UL([T('Write the midpoints \\(x_i\\) (add a row to the table).', 'Ghi giá trị đại diện \\(x_i\\) (thêm một hàng vào bảng).'), T('Compute \\(\\bar x=\\dfrac1n\\sum n_ix_i\\).', 'Tính \\(\\bar x=\\dfrac1n\\sum n_ix_i\\).'),
  T('Compute \\(\\dfrac1n\\sum n_ix_i^2\\), then subtract \\(\\bar x^2\\). Take the square root for \\(s\\).', 'Tính \\(\\dfrac1n\\sum n_ix_i^2\\) rồi trừ \\(\\bar x^2\\). Khai căn được \\(s\\).')]))
theory += '<h3>10.2 %s</h3>' % TI('Meaning', 'Ý nghĩa')
theory += BOX('blue', ('Interpreting \\(s\\)', 'Ý nghĩa của \\(s\\)'), UL([T('\\(s\\) measures how far the data are from the mean on average. A larger \\(s\\) means more spread; a smaller \\(s\\) means the data are more concentrated (more stable, more consistent).', '\\(s\\) đo mức độ các giá trị lệch khỏi số trung bình. \\(s\\) càng lớn thì số liệu càng phân tán; \\(s\\) càng nhỏ thì số liệu càng tập trung (ổn định, đồng đều hơn).'),
  T('\\(s\\) has the unit of the data; \\(s^2\\) has the unit squared. Compare \\(s\\) of samples measured in the same unit.', '\\(s\\) cùng đơn vị với số liệu; \\(s^2\\) có đơn vị là bình phương. So sánh \\(s\\) của các mẫu cùng đơn vị đo.'),
  T('Adding a constant to all data does not change \\(s\\); multiplying all data by \\(k\\gt0\\) multiplies \\(s\\) by \\(k\\).', 'Cộng cùng một số vào mọi giá trị thì \\(s\\) không đổi; nhân mọi giá trị với \\(k\\gt0\\) thì \\(s\\) nhân với \\(k\\).')]))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('For grouped data the values inside a group are replaced by the midpoint, so \\(s\\) is only an <b>estimate</b>. Like the mean, \\(s\\) is affected by extreme values; then \\(\\Delta_Q\\) may describe the spread better.', 'Với số liệu ghép nhóm, các giá trị trong nhóm được thay bằng giá trị đại diện nên \\(s\\) chỉ là giá trị <b>xấp xỉ</b>. Giống số trung bình, \\(s\\) bị ảnh hưởng bởi giá trị bất thường; khi đó \\(\\Delta_Q\\) có thể mô tả độ phân tán tốt hơn.'))

t1 = VT(33); assert (t1.u0, t1.h, t1.fs, t1.mean(), t1.var()) == (60, 10, [5, 8, 5, 2], 77, 86)
L1 = LB('Điểm / Score', 'Số học sinh / Students')
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Variance step by step', 'Tính phương sai từng bước'), T('The scores of 20 students in a test (out of 100): %s Find the mean, the variance and the standard deviation (to the hundredths).' % t1.html(rows=('group', 'mid', 'freq'), labels=L1), 'Điểm kiểm tra (thang 100) của 20 học sinh: %s Tìm số trung bình, phương sai và độ lệch chuẩn (làm tròn đến hàng phần trăm).' % t1.html(rows=('group', 'mid', 'freq'), labels=L1)),
  T('Use the midpoints 65, 75, 85, 95.', 'Dùng các giá trị đại diện 65, 75, 85, 95.'),
  [T('\\(\\bar x=\\dfrac{5\\cdot65+8\\cdot75+5\\cdot85+2\\cdot95}{20}=\\dfrac{1540}{20}=77\\).', '\\(\\bar x=\\dfrac{5\\cdot65+8\\cdot75+5\\cdot85+2\\cdot95}{20}=\\dfrac{1540}{20}=77\\).'),
   T('\\(\\dfrac1n\\sum n_ix_i^2=\\dfrac{5\\cdot65^2+8\\cdot75^2+5\\cdot85^2+2\\cdot95^2}{20}=\\dfrac{120\\,300}{20}=6015\\).', '\\(\\dfrac1n\\sum n_ix_i^2=\\dfrac{5\\cdot65^2+8\\cdot75^2+5\\cdot85^2+2\\cdot95^2}{20}=\\dfrac{120\\,300}{20}=6015\\).'),
   T('\\(s^2=6015-77^2=6015-5929=86\\); \\(s=\\sqrt{86}\\approx9.27\\).', '\\(s^2=6015-77^2=6015-5929=86\\); \\(s=\\sqrt{86}\\approx9{,}27\\).')],
  T('\\(\\bar x=77\\), \\(s^2=86\\), \\(s\\approx9.27\\) points.', '\\(\\bar x=77\\), \\(s^2=86\\), \\(s\\approx9{,}27\\) điểm.'))
assert 5 * 65 + 8 * 75 + 5 * 85 + 2 * 95 == 1540 and 5 * 65 ** 2 + 8 * 75 ** 2 + 5 * 85 ** 2 + 2 * 95 ** 2 == 120300 and r2(math.sqrt(86)) == F(927, 100)
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Units of \\(s^2\\) and \\(s\\)', 'Đơn vị của \\(s^2\\) và \\(s\\)'), T('The heights of a group of seedlings have variance \\(s^2=6.25\\ \\text{cm}^2\\). Find the standard deviation and its unit.', 'Chiều cao một nhóm cây giống có phương sai \\(s^2=6{,}25\\ \\text{cm}^2\\). Tìm độ lệch chuẩn và đơn vị.'),
  T('\\(s=\\sqrt{s^2}\\).', '\\(s=\\sqrt{s^2}\\).'), [T('\\(s=\\sqrt{6.25}=2.5\\).', '\\(s=\\sqrt{6{,}25}=2{,}5\\).')], T('\\(s=2.5\\) cm (same unit as the heights).', '\\(s=2{,}5\\) cm (cùng đơn vị với chiều cao).'))
ta, tb = VT(7), VT(28); assert (ta.mean(), ta.var(), tb.mean(), tb.var()) == (21, 144, 27, 196)
L2 = LB('Thời gian (phút) / Time (min)', 'Số học sinh / Students')
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Which group is more uniform?', 'Nhóm nào đồng đều hơn?'), T('Daily self-study time of two groups of students. Group A: %s Group B: %s Which group studies more uniformly?' % (ta.html(labels=L2), tb.html(labels=L2)), 'Thời gian tự học mỗi ngày của hai nhóm học sinh. Nhóm A: %s Nhóm B: %s Nhóm nào có thời gian tự học đồng đều hơn?' % (ta.html(labels=L2), tb.html(labels=L2))),
  T('Compute \\(s\\) for each group and compare.', 'Tính \\(s\\) của mỗi nhóm rồi so sánh.'),
  [T('A: \\(\\bar x_A=21\\), \\(s_A^2=585-21^2=144\\), \\(s_A=12\\).', 'A: \\(\\bar x_A=21\\), \\(s_A^2=585-21^2=144\\), \\(s_A=12\\).'), T('B: \\(\\bar x_B=27\\), \\(s_B^2=925-27^2=196\\), \\(s_B=14\\).', 'B: \\(\\bar x_B=27\\), \\(s_B^2=925-27^2=196\\), \\(s_B=14\\).')],
  T('\\(s_A=12\\lt s_B=14\\): group A is more uniform (group B studies longer on average).', '\\(s_A=12\\lt s_B=14\\): nhóm A đồng đều hơn (nhóm B học lâu hơn tính trung bình).'))
assert sum(f * ta.mid(i) ** 2 for i, f in enumerate(ta.fs)) / ta.n == 585 and sum(f * tb.mid(i) ** 2 for i, f in enumerate(tb.fs)) / tb.n == 925
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('From sums', 'Tính từ các tổng'), T('A sample of \\(n=40\\) grouped values has \\(\\sum n_ix_i=2600\\) and \\(\\sum n_ix_i^2=172\\,000\\). Find \\(\\bar x\\), \\(s^2\\) and \\(s\\).', 'Một mẫu ghép nhóm cỡ \\(n=40\\) có \\(\\sum n_ix_i=2600\\) và \\(\\sum n_ix_i^2=172\\,000\\). Tìm \\(\\bar x\\), \\(s^2\\) và \\(s\\).'),
  T('Use the short formula \\(s^2=\\dfrac1n\\sum n_ix_i^2-\\bar x^2\\).', 'Dùng công thức \\(s^2=\\dfrac1n\\sum n_ix_i^2-\\bar x^2\\).'), [T('\\(\\bar x=\\dfrac{2600}{40}=65\\).', '\\(\\bar x=\\dfrac{2600}{40}=65\\).'), T('\\(s^2=\\dfrac{172\\,000}{40}-65^2=4300-4225=75\\).', '\\(s^2=\\dfrac{172\\,000}{40}-65^2=4300-4225=75\\).')],
  T('\\(\\bar x=65\\), \\(s^2=75\\), \\(s=\\sqrt{75}\\approx8.66\\).', '\\(\\bar x=65\\), \\(s^2=75\\), \\(s=\\sqrt{75}\\approx8{,}66\\).'))
assert F(172000, 40) - 65 ** 2 == 75 and r2(math.sqrt(75)) == F(866, 100)
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Changing the unit', 'Đổi đơn vị đo'), T('Noon temperatures in a month have \\(\\bar x=30^\\circ\\text{C}\\) and \\(s=2.5^\\circ\\text{C}\\). Convert to Fahrenheit by \\(F=1.8C+32\\). Find the new mean and standard deviation. Is the weather "more variable" in °F?', 'Nhiệt độ buổi trưa trong một tháng có \\(\\bar x=30^\\circ\\text{C}\\), \\(s=2{,}5^\\circ\\text{C}\\). Đổi sang độ F theo \\(F=1{,}8C+32\\). Tìm số trung bình và độ lệch chuẩn mới. Thời tiết có "biến động hơn" khi đo bằng °F không?'),
  T('Multiplying by 1.8 multiplies \\(s\\) by 1.8; adding 32 changes the mean only.', 'Nhân với 1,8 làm \\(s\\) nhân 1,8; cộng 32 chỉ làm thay đổi số trung bình.'),
  [T('\\(\\bar x_F=1.8\\cdot30+32=86\\ ^\\circ\\text{F}\\).', '\\(\\bar x_F=1{,}8\\cdot30+32=86\\ ^\\circ\\text{F}\\).'), T('\\(s_F=1.8\\cdot2.5=4.5\\ ^\\circ\\text{F}\\).', '\\(s_F=1{,}8\\cdot2{,}5=4{,}5\\ ^\\circ\\text{F}\\).')],
  T('\\(86^\\circ\\text{F}\\) and \\(4.5^\\circ\\text{F}\\). No: the spread is the same, only the unit changed – compare \\(s\\) only in the same unit.', '\\(86^\\circ\\text{F}\\) và \\(4{,}5^\\circ\\text{F}\\). Không: mức biến động như cũ, chỉ đổi đơn vị – chỉ so sánh \\(s\\) khi cùng đơn vị.'))
assert F(18, 10) * 30 + 32 == 86 and F(18, 10) * F(25, 10) == F(45, 10)

CT = [('Điểm / Score', 'Số học sinh / Students', ('test scores', 'điểm kiểm tra')), ('Chiều cao (cm) / Height (cm)', 'Số cây / Plants', ('heights of seedlings', 'chiều cao cây giống')), ('Thời gian (phút) / Time (min)', 'Số khách / Customers', ('waiting times', 'thời gian chờ'))]
def lvl(P):
    t = VT(P['t']); c = CT[P['c']]; L = LB(c[0], c[1]); v, m = t.var(), t.mean(); ex2 = v + m * m
    o1 = M4(1, 'The table shows %s: %s The variance \\(s^2\\) is…' % (c[2][0], t.html(labels=L)), 'Bảng sau cho biết %s: %s Phương sai \\(s^2\\) bằng…' % (c[2][1], t.html(labels=L)),
            D(v), [D(ex2), D(r2(math.sqrt(v))), D(2 * v), D(v + 1)], '\\(\\bar x=%s\\), \\(s^2=%s-%s^2=%s\\).' % (DE(m), DE(ex2), DE(m), DE(v)), '\\(\\bar x=%s\\), \\(s^2=%s-%s^2=%s\\).' % (D(m), D(ex2), D(m), D(v)))
    n, mm, vv = P['sum']; S1, S2 = n * mm, n * (vv + mm * mm)
    o2 = M4(2, 'A grouped sample has \\(n=%d\\), \\(\\sum n_ix_i=%s\\), \\(\\sum n_ix_i^2=%s\\). Its standard deviation is…' % (n, D(S1), D(S2)), 'Một mẫu ghép nhóm có \\(n=%d\\), \\(\\sum n_ix_i=%s\\), \\(\\sum n_ix_i^2=%s\\). Độ lệch chuẩn của mẫu là…' % (n, D(S1), D(S2)),
            str(math.isqrt(vv)), [str(vv), D(F(S2, n)), str(math.isqrt(vv) + 1), str(mm)], '\\(\\bar x=%d\\), \\(s^2=%s-%d^2=%d\\), \\(s=%d\\).' % (mm, DE(F(S2, n)), mm, vv, math.isqrt(vv)), '\\(\\bar x=%d\\), \\(s^2=%s-%d^2=%d\\), \\(s=%d\\).' % (mm, D(F(S2, n)), mm, vv, math.isqrt(vv)))
    assert math.isqrt(vv) ** 2 == vv
    (ma, sa), (mb, sb), ctx = P['cmp']; better = 'A' if sa < sb else 'B'; worse = 'B' if better == 'A' else 'A'
    o3 = M4(3, '%s A: mean \\(%s\\), \\(s=%s\\). B: mean \\(%s\\), \\(s=%s\\). Which conclusion is right?' % (ctx[0], DE(ma), DE(sa), DE(mb), DE(sb)), '%s A: trung bình \\(%s\\), \\(s=%s\\). B: trung bình \\(%s\\), \\(s=%s\\). Kết luận nào đúng?' % (ctx[1], D(ma), D(sa), D(mb), D(sb)),
            S.TT('%s is more stable' % better, '%s ổn định hơn' % better), [S.TT('%s is more stable' % worse, '%s ổn định hơn' % worse), S.TT('Both are equally stable', 'Hai đối tượng ổn định như nhau'), S.TT('%s is more stable because its mean is larger' % ('A' if ma > mb else 'B'), '%s ổn định hơn vì có trung bình lớn hơn' % ('A' if ma > mb else 'B'))],
            'The smaller standard deviation means the more stable.', 'Độ lệch chuẩn nhỏ hơn thì ổn định hơn.')
    t4v = VT(P['t4']); claim = t4v.var() if P['t4ok'] else t4v.var() + t4v.mean() ** 2           # sai thường gặp: quên trừ \bar x^2
    t4 = tf(4, 'For the table %s the variance is \\(s^2=%s\\).' % (t4v.html(), DE(claim)), 'Với mẫu số liệu %s phương sai là \\(s^2=%s\\).' % (t4v.html(), D(claim)), P['t4ok'],
            '\\(\\bar x=%s\\), \\(s^2=%s\\).' % (DE(t4v.mean()), DE(t4v.var())), '\\(\\bar x=%s\\), \\(s^2=%s\\).' % (D(t4v.mean()), D(t4v.var())))
    st = [('If every value of a sample increases by 5, the standard deviation does not change.', 'Nếu cộng thêm 5 vào mọi giá trị của mẫu thì độ lệch chuẩn không đổi.', True),
          ('If every value of a sample is doubled, the variance is doubled.', 'Nếu nhân đôi mọi giá trị của mẫu thì phương sai cũng tăng gấp đôi.', False),
          ('The standard deviation has the same unit as the data.', 'Độ lệch chuẩn có cùng đơn vị với số liệu.', True)][P['t5']]
    t5 = tf(5, st[0], st[1], st[2], 'Adding \\(c\\): \\(s\\) unchanged. Multiplying by \\(k\\gt0\\): \\(s\\) times \\(k\\), \\(s^2\\) times \\(k^2\\). \\(s\\) has the data unit.', 'Cộng \\(c\\): \\(s\\) không đổi. Nhân \\(k\\gt0\\): \\(s\\) nhân \\(k\\), \\(s^2\\) nhân \\(k^2\\). \\(s\\) cùng đơn vị với số liệu.')
    t6 = VT(P['t6']); v6 = t6.var()
    s6 = sh(6, 'Find the variance of the grouped data %s' % t6.html(), 'Tính phương sai của mẫu số liệu ghép nhóm %s' % t6.html(), DE(v6), '\\(\\bar x=%s\\), \\(s^2=%s\\).' % (DE(t6.mean()), DE(v6)), '\\(\\bar x=%s\\), \\(s^2=%s\\).' % (D(t6.mean()), D(v6)))
    t7 = VT(P['t7']); s7v = r2(math.sqrt(t7.var()))
    s7 = sh(7, 'Find the standard deviation of the grouped data %s (round to the hundredths).' % t7.html(), 'Tính độ lệch chuẩn của mẫu số liệu ghép nhóm %s (làm tròn đến hàng phần trăm).' % t7.html(), DE(s7v),
            '\\(s^2=%s\\), \\(s=\\sqrt{%s}\\approx%s\\).' % (DE(t7.var()), DE(t7.var()), DE(s7v)), '\\(s^2=%s\\), \\(s=\\sqrt{%s}\\approx%s\\).' % (D(t7.var()), D(t7.var()), D(s7v)), hint=('Enter a decimal number, e.g. 3.25.', 'Nhập số thập phân, ví dụ 3,25.'))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
PP = [dict(t=16, c=0, sum=(20, 50, 16), cmp=((F(52), F(12, 10)), (F(54), F(25, 10)), ('Rice yield (quintals/ha) of two fields.', 'Năng suất lúa (tạ/ha) của hai ruộng.')), t4=38, t4ok=True, t5=0, t6=9, t7=12),
      dict(t=4, c=1, sum=(25, 40, 9), cmp=((F(500), F(42, 10)), (F(498), F(31, 10)), ('Volume (ml) of bottles filled by two machines.', 'Thể tích (ml) chai do hai máy chiết rót.')), t4=11, t4ok=False, t5=1, t6=13, t7=25),
      dict(t=2, c=2, sum=(40, 75, 49), cmp=((F(8), F(9, 10)), (F(85, 10), F(15, 10)), ('Scores of two shooters.', 'Điểm bắn của hai xạ thủ.')), t4=29, t4ok=True, t5=2, t6=24, t7=22)]
practice = three(lvl, PP)
practice = with_self(practice, S.M10S12, start=8)
mistakes = [('<b>Using the group ends instead of the midpoints.</b> \\(x_i\\) is the midpoint of the group.', '<b>Dùng đầu mút nhóm thay cho giá trị đại diện.</b> \\(x_i\\) là giá trị chính giữa của nhóm.'),
            ('<b>Forgetting to subtract \\(\\bar x^2\\).</b> \\(s^2=\\dfrac1n\\sum n_ix_i^2-\\bar x^2\\), not \\(\\dfrac1n\\sum n_ix_i^2\\).', '<b>Quên trừ \\(\\bar x^2\\).</b> \\(s^2=\\dfrac1n\\sum n_ix_i^2-\\bar x^2\\), không phải \\(\\dfrac1n\\sum n_ix_i^2\\).'),
            ('<b>Mixing up \\(s\\) and \\(s^2\\).</b> \\(s\\) is the square root; it has the unit of the data.', '<b>Nhầm \\(s\\) và \\(s^2\\).</b> \\(s\\) là căn bậc hai của \\(s^2\\) và cùng đơn vị với số liệu.'),
            ('<b>"Larger mean = more stable".</b> Stability depends on \\(s\\), not on the mean.', '<b>"Trung bình lớn hơn thì ổn định hơn".</b> Độ ổn định phụ thuộc vào \\(s\\), không phụ thuộc số trung bình.')]
summary = [('\\(s^2=\\dfrac1n\\sum n_i(x_i-\\bar x)^2=\\dfrac1n\\sum n_ix_i^2-\\bar x^2\\); \\(s=\\sqrt{s^2}\\).', '\\(s^2=\\dfrac1n\\sum n_i(x_i-\\bar x)^2=\\dfrac1n\\sum n_ix_i^2-\\bar x^2\\); \\(s=\\sqrt{s^2}\\).'),
           ('\\(x_i\\) are the midpoints of the groups; the result is an estimate.', '\\(x_i\\) là giá trị đại diện của các nhóm; kết quả là giá trị xấp xỉ.'),
           ('Smaller \\(s\\): data more concentrated, more stable.', '\\(s\\) nhỏ hơn: số liệu tập trung hơn, ổn định hơn.'),
           ('Key words: variance, standard deviation, spread, stable.', 'Từ cần nhớ: variance, standard deviation, spread, stable.')]
checks = [('I can compute the variance of grouped data.', 'Em tính được phương sai của mẫu số liệu ghép nhóm.'), ('I can find the standard deviation and its unit.', 'Em tìm được độ lệch chuẩn và đơn vị của nó.'),
          ('I can compare the stability of two samples.', 'Em so sánh được độ ổn định của hai mẫu.'), ('I know how \\(s\\) changes when the data are shifted or scaled.', 'Em biết \\(s\\) thay đổi thế nào khi cộng hay nhân số liệu với một số.')]
LL('g12-stats-02', 'Variance and Standard Deviation', CV, ('Statistics', 'Các số đặc trưng đo mức độ phân tán'), 'statistics', 'variance-standard-deviation', 100, 'Intermediate', 65, ('grouped data, mean, range and interquartile range', 'số liệu ghép nhóm, số trung bình, khoảng biến thiên và khoảng tứ phân vị'),
   'Variance and standard deviation of grouped data, their meaning and the comparison of the stability of two samples.', 'Bài 10 – Phương sai, độ lệch chuẩn của mẫu số liệu ghép nhóm; ý nghĩa và so sánh độ ổn định.',
   ['variance', 'standard deviation', 'spread', 'stability'], ['phương sai', 'độ lệch chuẩn', 'độ phân tán', 'ổn định'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g12-stats-01'])
