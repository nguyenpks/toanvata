# -*- coding: utf-8 -*-
"""g10-func-03 = Toán 10 KNTT, Bài 17: Dấu của tam thức bậc hai. Mã ngân hàng câu hỏi: TOAN10-C6-B17."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g10g as S
from sp_g10f import poly
from sp_g10g import seg, union

CV = 'Dấu của tam thức bậc hai'
vocab = defs(CV, [
 ('qtri', 'quadratic trinomial', 'tam thức bậc hai', 'an expression \\(f(x)=ax^2+bx+c\\) with \\(a\\ne0\\).', 'biểu thức \\(f(x)=ax^2+bx+c\\) với \\(a\\ne0\\).', 'The quadratic trinomial has two roots.', '\\(f(x)\\)'),
 ('signtab', 'sign table', 'bảng xét dấu', 'a table showing on which intervals an expression is positive or negative.', 'bảng cho biết biểu thức dương, âm trên những khoảng nào.', 'Make a sign table for f(x).', ''),
 ('qineq', 'quadratic inequality', 'bất phương trình bậc hai', 'an inequality \\(ax^2+bx+c\\gt0\\) (or \\(\\lt\\), \\(\\ge\\), \\(\\le\\)) with \\(a\\ne0\\).', 'bất phương trình dạng \\(ax^2+bx+c\\gt0\\) (hoặc \\(\\lt\\), \\(\\ge\\), \\(\\le\\)) với \\(a\\ne0\\).', 'Solve the quadratic inequality.', ''),
 ('samesign', 'same sign as \\(a\\)', 'cùng dấu với hệ số a', 'having the same sign (+ or −) as the leading coefficient \\(a\\).', 'có cùng dấu (+ hoặc −) với hệ số \\(a\\).', 'Outside the roots, f(x) has the same sign as a.', '')])
goals = [('recognise a quadratic trinomial, its roots and its discriminant;', 'nhận biết [[tam thức bậc hai]], nghiệm và [[biệt thức]] của nó;'),
         ('find the sign of \\(f(x)=ax^2+bx+c\\) with the sign theorem and a sign table;', 'xét dấu tam thức bậc hai bằng định lí về dấu và [[bảng xét dấu]];'),
         ('solve quadratic inequalities;', 'giải [[bất phương trình bậc hai]];'),
         ('use the sign of a trinomial in real problems (profit, height, conditions for all \\(x\\)).', 'vận dụng dấu tam thức vào bài toán thực tế (lợi nhuận, độ cao, điều kiện đúng với mọi \\(x\\)).')]
phrases = [('<b>The trinomial has two distinct roots.</b>', 'Tam thức có hai nghiệm phân biệt.'), ('<b>Between the roots, \\(f(x)\\) has the opposite sign to \\(a\\).</b>', 'Giữa hai nghiệm, \\(f(x)\\) trái dấu với \\(a\\).'),
           ('<b>Make a sign table.</b>', 'Lập bảng xét dấu.'), ('<b>The solution set is the closed interval from one to four.</b>', 'Tập nghiệm là đoạn \\([1;4]\\).'), ('<b>The inequality holds for every real \\(x\\).</b>', 'Bất phương trình đúng với mọi \\(x\\) thực.')]
review = T('From Bài 16: the parabola \\(y=ax^2+bx+c\\) opens upward when \\(a\\gt0\\) and downward when \\(a\\lt0\\); it cuts \\(Ox\\) at the roots of \\(ax^2+bx+c=0\\). \\(\\Delta=b^2-4ac\\) (or \\(\\Delta\'=b\'^2-ac\\) with \\(b=2b\'\\)).',
           'Từ Bài 16: parabol \\(y=ax^2+bx+c\\) có bề lõm quay lên khi \\(a\\gt0\\), quay xuống khi \\(a\\lt0\\); cắt \\(Ox\\) tại các nghiệm của \\(ax^2+bx+c=0\\). \\(\\Delta=b^2-4ac\\) (hoặc \\(\\Delta\'=b\'^2-ac\\) với \\(b=2b\'\\)).')
theory = '<h3>17.1 %s</h3>' % TI('The sign of a quadratic trinomial', 'Dấu của tam thức bậc hai')
theory += BOX('blue', ('Sign theorem', 'Định lí về dấu của tam thức bậc hai'), T('Let \\(f(x)=ax^2+bx+c\\) (\\(a\\ne0\\)), \\(\\Delta=b^2-4ac\\).', 'Cho \\(f(x)=ax^2+bx+c\\) (\\(a\\ne0\\)), \\(\\Delta=b^2-4ac\\).') + UL([
  T('\\(\\Delta\\lt0\\): \\(f(x)\\) has the same sign as \\(a\\) for every \\(x\\in\\mathbb R\\).', '\\(\\Delta\\lt0\\): \\(f(x)\\) cùng dấu với \\(a\\) với mọi \\(x\\in\\mathbb R\\).'),
  T('\\(\\Delta=0\\): \\(f(x)\\) has the same sign as \\(a\\) for every \\(x\\ne-\\dfrac b{2a}\\); \\(f\\left(-\\dfrac b{2a}\\right)=0\\).', '\\(\\Delta=0\\): \\(f(x)\\) cùng dấu với \\(a\\) với mọi \\(x\\ne-\\dfrac b{2a}\\); \\(f\\left(-\\dfrac b{2a}\\right)=0\\).'),
  T('\\(\\Delta\\gt0\\), roots \\(x_1\\lt x_2\\): \\(f(x)\\) has the sign of \\(a\\) on \\((-\\infty;x_1)\\cup(x_2;+\\infty)\\) and the opposite sign on \\((x_1;x_2)\\). Memory aid: <i>"outside – same, inside – opposite"</i>.', '\\(\\Delta\\gt0\\), hai nghiệm \\(x_1\\lt x_2\\): \\(f(x)\\) cùng dấu \\(a\\) trên \\((-\\infty;x_1)\\cup(x_2;+\\infty)\\), trái dấu \\(a\\) trên \\((x_1;x_2)\\). Ghi nhớ: <i>"trong trái, ngoài cùng"</i>.')]))
theory += TBL(['\\(x\\)', '\\(-\\infty\\)', '', '\\(x_1\\)', '', '\\(x_2\\)', '', '\\(+\\infty\\)'], [['\\(f(x)\\)', '', TI('same sign as \\(a\\)', 'cùng dấu \\(a\\)'), '0', TI('opposite to \\(a\\)', 'trái dấu \\(a\\)'), '0', TI('same sign as \\(a\\)', 'cùng dấu \\(a\\)'), '']])
theory += GRAPH({'view': [-4, 6, -6, 6], 'functions': [{'f': 'x^2-2*x-3', 'label': 'y = x² − 2x − 3'}], 'points': [{'x': -1, 'y': 0, 'label': 'x₁ = −1'}, {'x': 3, 'y': 0, 'label': 'x₂ = 3'}]},
  cap=('\\(f(x)=x^2-2x-3\\) (\\(a=1\\gt0\\)): the graph is above \\(Ox\\) outside \\([-1;3]\\) (\\(f\\gt0\\)) and below \\(Ox\\) between the roots (\\(f\\lt0\\)).', '\\(f(x)=x^2-2x-3\\) (\\(a=1\\gt0\\)): đồ thị nằm trên \\(Ox\\) ngoài đoạn \\([-1;3]\\) (\\(f\\gt0\\)) và nằm dưới \\(Ox\\) giữa hai nghiệm (\\(f\\lt0\\)).'),
  alt=('Parabola cutting the x-axis at −1 and 3', 'Parabol cắt Ox tại −1 và 3'), height=300)
theory += '<h3>17.2 %s</h3>' % TI('Quadratic inequalities', 'Bất phương trình bậc hai một ẩn')
theory += BOX('mint', ('Method', 'Cách giải'), UL([T('Write the inequality as \\(f(x)\\gt0\\) (\\(\\lt0\\), \\(\\ge0\\), \\(\\le0\\)) with \\(f(x)=ax^2+bx+c\\).', 'Đưa về dạng \\(f(x)\\gt0\\) (\\(\\lt0\\), \\(\\ge0\\), \\(\\le0\\)) với \\(f(x)=ax^2+bx+c\\).'),
  T('Find \\(\\Delta\\) and the roots; make the sign table (or use the theorem).', 'Tính \\(\\Delta\\), tìm nghiệm; lập bảng xét dấu (hoặc dùng định lí).'), T('Read the solution set; include the roots for \\(\\ge\\), \\(\\le\\).', 'Đọc tập nghiệm; với \\(\\ge\\), \\(\\le\\) thì lấy cả các nghiệm.')]))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('\\(ax^2+bx+c\\gt0\\) for <b>every</b> \\(x\\) \\(\\iff a\\gt0\\) and \\(\\Delta\\lt0\\); \\(ax^2+bx+c\\lt0\\) for every \\(x\\iff a\\lt0\\) and \\(\\Delta\\lt0\\). Dividing by a negative number reverses the inequality sign.', '\\(ax^2+bx+c\\gt0\\) với <b>mọi</b> \\(x\\iff a\\gt0\\) và \\(\\Delta\\lt0\\); \\(ax^2+bx+c\\lt0\\) với mọi \\(x\\iff a\\lt0\\) và \\(\\Delta\\lt0\\). Chia hai vế cho số âm phải đổi chiều bất phương trình.'))

f1 = lambda x: x * x - x - 6; assert f1(-2) == f1(3) == 0 and f1(0) < 0 and f1(4) > 0
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('A sign table', 'Lập bảng xét dấu'), T('Find the sign of \\(f(x)=x^2-x-6\\).', 'Xét dấu tam thức \\(f(x)=x^2-x-6\\).'), T('Find the roots, then use "outside – same, inside – opposite".', 'Tìm nghiệm rồi dùng quy tắc "trong trái, ngoài cùng".'),
  [T('\\(\\Delta=1+24=25\\gt0\\); roots \\(x_1=-2\\), \\(x_2=3\\); \\(a=1\\gt0\\).', '\\(\\Delta=1+24=25\\gt0\\); nghiệm \\(x_1=-2\\), \\(x_2=3\\); \\(a=1\\gt0\\).'), T('\\(f(x)\\gt0\\) on \\((-\\infty;-2)\\cup(3;+\\infty)\\); \\(f(x)\\lt0\\) on \\((-2;3)\\).', '\\(f(x)\\gt0\\) trên \\((-\\infty;-2)\\cup(3;+\\infty)\\); \\(f(x)\\lt0\\) trên \\((-2;3)\\).')],
  T('Positive outside \\([-2;3]\\), negative on \\((-2;3)\\), zero at \\(-2\\) and \\(3\\).', 'Dương ngoài đoạn \\([-2;3]\\), âm trên \\((-2;3)\\), bằng 0 tại \\(-2\\) và \\(3\\).'))
assert 2 * 2 - 2 * 5 < 0 and 144 - 4 * 4 * 9 == 0
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('No roots or a double root', 'Vô nghiệm hoặc nghiệm kép'), T('Find the sign of \\(g(x)=-2x^2+4x-5\\) and \\(h(x)=4x^2-12x+9\\).', 'Xét dấu \\(g(x)=-2x^2+4x-5\\) và \\(h(x)=4x^2-12x+9\\).'), T('Compute \\(\\Delta\'\\) or \\(\\Delta\\).', 'Tính \\(\\Delta\'\\) hoặc \\(\\Delta\\).'),
  [T('\\(g\\): \\(\\Delta\'=4-10=-6\\lt0\\), \\(a=-2\\lt0\\Rightarrow g(x)\\lt0\\) for all \\(x\\).', '\\(g\\): \\(\\Delta\'=4-10=-6\\lt0\\), \\(a=-2\\lt0\\Rightarrow g(x)\\lt0\\) với mọi \\(x\\).'), T('\\(h\\): \\(\\Delta=144-144=0\\); \\(h(x)=(2x-3)^2\\).', '\\(h\\): \\(\\Delta=144-144=0\\); \\(h(x)=(2x-3)^2\\).')],
  T('\\(g(x)\\lt0\\) for all \\(x\\); \\(h(x)\\gt0\\) for all \\(x\\ne\\frac32\\), \\(h\\left(\\frac32\\right)=0\\).', '\\(g(x)\\lt0\\) với mọi \\(x\\); \\(h(x)\\gt0\\) với mọi \\(x\\ne\\frac32\\), \\(h\\left(\\frac32\\right)=0\\).'))
assert all(-x * x + 5 * x - 4 >= 0 for x in (1, 2, 4)) and 2 * F(-1, 2) ** 2 - 3 * F(-1, 2) - 2 == 0
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Quadratic inequalities', 'Giải bất phương trình bậc hai'), T('Solve a) \\(-x^2+5x-4\\ge0\\); b) \\(2x^2-3x-2\\gt0\\).', 'Giải các bất phương trình a) \\(-x^2+5x-4\\ge0\\); b) \\(2x^2-3x-2\\gt0\\).'), T('Roots first, then the sign of \\(a\\).', 'Tìm nghiệm trước, rồi xét dấu của \\(a\\).'),
  [T('a) Roots 1 and 4, \\(a=-1\\lt0\\): \\(f\\ge0\\) between the roots, \\(S=[1;4]\\).', 'a) Nghiệm 1 và 4, \\(a=-1\\lt0\\): \\(f\\ge0\\) giữa hai nghiệm, \\(S=[1;4]\\).'), T('b) Roots \\(-\\frac12\\) and 2, \\(a=2\\gt0\\): \\(f\\gt0\\) outside, \\(S=\\left(-\\infty;-\\frac12\\right)\\cup(2;+\\infty)\\).', 'b) Nghiệm \\(-\\frac12\\) và 2, \\(a=2\\gt0\\): \\(f\\gt0\\) ở ngoài, \\(S=\\left(-\\infty;-\\frac12\\right)\\cup(2;+\\infty)\\).')],
  T('a) \\([1;4]\\); b) \\(\\left(-\\infty;-\\frac12\\right)\\cup(2;+\\infty)\\).', 'a) \\([1;4]\\); b) \\(\\left(-\\infty;-\\frac12\\right)\\cup(2;+\\infty)\\).'))
assert all(((m + 1) ** 2 - (m + 7) < 0) == (-3 < m < 2) for m in [F(k, 2) for k in range(-10, 10)])
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('True for every x', 'Đúng với mọi x'), T('Find \\(m\\) so that \\(x^2-2(m+1)x+m+7\\gt0\\) for every \\(x\\in\\mathbb R\\).', 'Tìm \\(m\\) để \\(x^2-2(m+1)x+m+7\\gt0\\) với mọi \\(x\\in\\mathbb R\\).'), T('\\(a=1\\gt0\\): need \\(\\Delta\'\\lt0\\).', '\\(a=1\\gt0\\): cần \\(\\Delta\'\\lt0\\).'),
  [T('\\(\\Delta\'=(m+1)^2-(m+7)=m^2+m-6\\).', '\\(\\Delta\'=(m+1)^2-(m+7)=m^2+m-6\\).'), T('\\(m^2+m-6\\lt0\\iff-3\\lt m\\lt2\\) (roots \\(-3\\), \\(2\\)).', '\\(m^2+m-6\\lt0\\iff-3\\lt m\\lt2\\) (nghiệm \\(-3\\), \\(2\\)).')], T('\\(-3\\lt m\\lt2\\).', '\\(-3\\lt m\\lt2\\).'))
P5 = lambda x: -x * x + 100 * x - 1600; assert P5(30) == P5(70) == 500 and P5(50) == 900
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Choosing a price', 'Chọn giá bán'), T('A shop sells a T-shirt at \\(x\\) thousand VND. Its weekly profit is \\(P(x)=-x^2+100x-1600\\) (thousand VND). For which prices is the profit at least 500 thousand VND?', 'Một cửa hàng bán áo phông với giá \\(x\\) nghìn đồng. Lợi nhuận mỗi tuần là \\(P(x)=-x^2+100x-1600\\) (nghìn đồng). Với giá nào thì lợi nhuận ít nhất 500 nghìn đồng?'),
  T('Solve \\(P(x)\\ge500\\).', 'Giải \\(P(x)\\ge500\\).'), [T('\\(-x^2+100x-2100\\ge0\\iff x^2-100x+2100\\le0\\).', '\\(-x^2+100x-2100\\ge0\\iff x^2-100x+2100\\le0\\).'), T('Roots 30 and 70; \\(a=1\\gt0\\): \\(\\le0\\) between the roots.', 'Nghiệm 30 và 70; \\(a=1\\gt0\\): \\(\\le0\\) giữa hai nghiệm.')],
  T('Price from 30 to 70 thousand VND (the largest profit, 900 thousand, is at 50 thousand).', 'Giá từ 30 đến 70 nghìn đồng (lợi nhuận lớn nhất 900 nghìn đồng khi giá 50 nghìn).'))

def lvl(P):
    p, q, a = P['tab']; cs = [a, -a * (p + q), a * p * q]
    o1 = M4(1, '\\(f(x)=%s\\) is negative exactly on…' % poly(cs), 'Tam thức \\(f(x)=%s\\) âm khi và chỉ khi \\(x\\) thuộc…' % poly(cs), '\\(%s\\)' % (seg(p, q, False) if a > 0 else union(p, q, False)),
            ['\\(%s\\)' % (union(p, q, False) if a > 0 else seg(p, q, False)), '\\(%s\\)' % seg(p, q, True), '\\(%s\\)' % seg(-q, -p, False), '\\(\\mathbb R\\)'],
            'Roots \\(%d\\), \\(%d\\); \\(a=%d\\).' % (p, q, a), 'Hai nghiệm \\(%d\\), \\(%d\\); \\(a=%d\\): trong trái, ngoài cùng.' % (p, q, a))
    (u, v, a2), rel = P['ineq']; cs2 = [a2, -a2 * (u + v), a2 * u * v]; closed = rel in ('\\ge', '\\le'); pos = rel in ('\\gt', '\\ge'); inside = (pos and a2 < 0) or (not pos and a2 > 0)
    ok2 = seg(u, v, closed) if inside else union(u, v, closed)
    o2 = M4(2, 'Solve \\(%s%s0\\).' % (poly(cs2), rel), 'Giải bất phương trình \\(%s%s0\\).' % (poly(cs2), rel), '\\(%s\\)' % ok2,
            ['\\(%s\\)' % (union(u, v, closed) if inside else seg(u, v, closed)), '\\(%s\\)' % (seg(u, v, not closed) if inside else union(u, v, not closed)), '\\(\\varnothing\\)'],
            'Roots \\(%s\\), \\(%s\\); \\(a=%d\\).' % (fr(F(u)), fr(F(v)), a2), 'Nghiệm \\(%s\\), \\(%s\\); \\(a=%d\\).' % (fr(F(u)), fr(F(v)), a2))
    s3 = P['all']; k3 = s3 * s3
    o3 = M4(3, '\\(x^2+2mx+%d\\gt0\\) for all \\(x\\in\\mathbb R\\) when…' % k3, '\\(x^2+2mx+%d\\gt0\\) với mọi \\(x\\in\\mathbb R\\) khi…' % k3, '\\(-%d\\lt m\\lt%d\\)' % (s3, s3),
            ['\\(-%d\\le m\\le%d\\)' % (s3, s3), '\\(m\\gt%d\\)' % s3, '\\(m\\in(-\\infty;-%d)\\cup(%d;+\\infty)\\)' % (s3, s3)], '\\(\\Delta\'=m^2-%d\\lt0\\).' % k3, '\\(\\Delta\'=m^2-%d\\lt0\\iff-%d\\lt m\\lt%d\\).' % (k3, s3, s3))
    (a4, b4, c4), claim4 = P['tf4']; d4 = b4 * b4 - 4 * a4 * c4; truth4 = (d4 < 0 and ((a4 > 0) == (claim4 == 'pos')))
    t4 = tf(4, '\\(%s%s0\\) for every \\(x\\in\\mathbb R\\).' % (poly([a4, b4, c4]), '\\gt' if claim4 == 'pos' else '\\lt'), '\\(%s%s0\\) với mọi \\(x\\in\\mathbb R\\).' % (poly([a4, b4, c4]), '\\gt' if claim4 == 'pos' else '\\lt'), truth4,
            '\\(\\Delta=%d\\), \\(a=%d\\).' % (d4, a4), '\\(\\Delta=%d\\), \\(a=%d\\).' % (d4, a4))
    (p5, q5), x5, cl5 = P['tf5']; f5 = (x5 - p5) * (x5 - q5); truth5 = f5 < 0
    t5 = tf(5, '\\(x=%d\\) is a solution of \\(%s\\lt0\\).' % (x5, poly([1, -(p5 + q5), p5 * q5])), '\\(x=%d\\) là một nghiệm của bất phương trình \\(%s\\lt0\\).' % (x5, poly([1, -(p5 + q5), p5 * q5])), truth5,
            '\\(f(%d)=%d\\).' % (x5, f5), '\\(f(%d)=%d\\).' % (x5, f5))
    p6, q6, cl6 = P['cnt']; n6 = q6 - p6 + 1 if cl6 else q6 - p6 - 1
    s6 = sh(6, 'How many integers satisfy \\(%s%s0\\)?' % (poly([1, -(p6 + q6), p6 * q6]), '\\le' if cl6 else '\\lt'), 'Bất phương trình \\(%s%s0\\) có bao nhiêu nghiệm nguyên?' % (poly([1, -(p6 + q6), p6 * q6]), '\\le' if cl6 else '\\lt'), n6,
            'Solution set \\(%s\\).' % seg(p6, q6, cl6), 'Tập nghiệm \\(%s\\).' % seg(p6, q6, cl6))
    t1, t2, H = P['ball']; c7 = -5 * t1 * t2 + H; assert c7 >= 0
    s7 = sh(7, 'A ball\'s height is \\(h(t)=%s\\) (m). For how many seconds is it higher than %d m?' % (poly([-5, 5 * (t1 + t2), c7], 't'), H), 'Độ cao của quả bóng là \\(h(t)=%s\\) (m). Bóng ở cao hơn %d m trong bao nhiêu giây?' % (poly([-5, 5 * (t1 + t2), c7], 't'), H), t2 - t1,
            '\\(h(t)\\gt%d\\iff%d\\lt t\\lt%d\\): \\(%d\\) s.' % (H, t1, t2, t2 - t1), '\\(h(t)\\gt%d\\iff%d\\lt t\\lt%d\\): \\(%d\\) giây.' % (H, t1, t2, t2 - t1))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
PP = [dict(tab=(-1, 4, 1), ineq=((2, 5, -1), '\\ge'), all=2, tf4=((1, -2, 3), 'pos'), tf5=((1, 5), 3, 0), cnt=(-2, 3, True), ball=(1, 3, 20)),
      dict(tab=(-3, 2, -2), ineq=((-1, 3, 2), '\\gt'), all=3, tf4=((-1, 4, -5), 'pos'), tf5=((-2, 1), 1, 0), cnt=(1, 6, False), ball=(1, 2, 15)),
      dict(tab=(0, 5, -1), ineq=((-4, 1, 3), '\\le'), all=4, tf4=((2, 1, -3), 'pos'), tf5=((0, 4), 2, 0), cnt=(-3, 4, True), ball=(2, 4, 45))]
practice = three(lvl, PP)
practice = with_self(practice, S.M17S10, start=8)
mistakes = [('<b>Forgetting the sign of \\(a\\).</b> \\(-x^2+5x-4\\ge0\\) holds <i>between</i> the roots because \\(a\\lt0\\).', '<b>Quên xét dấu của \\(a\\).</b> \\(-x^2+5x-4\\ge0\\) đúng <i>giữa</i> hai nghiệm vì \\(a\\lt0\\).'),
            ('<b>Brackets for \\(\\ge\\), \\(\\le\\).</b> The roots belong to the solution set: use \\([\\ ]\\), not \\((\\ )\\).', '<b>Dùng sai ngoặc với \\(\\ge\\), \\(\\le\\).</b> Nghiệm của tam thức thuộc tập nghiệm: dùng \\([\\ ]\\), không dùng \\((\\ )\\).'),
            ('<b>\\(\\Delta\\lt0\\) means "no solution".</b> Not always: \\(x^2+1\\gt0\\) holds for <i>every</i> \\(x\\); only \\(x^2+1\\lt0\\) has no solution.', '<b>Nghĩ \\(\\Delta\\lt0\\) là "vô nghiệm".</b> Không phải lúc nào cũng vậy: \\(x^2+1\\gt0\\) đúng với <i>mọi</i> \\(x\\); chỉ \\(x^2+1\\lt0\\) mới vô nghiệm.'),
            ('<b>Writing \\(S=(3;-2)\\).</b> Write the smaller root first: \\((-2;3)\\).', '<b>Viết \\(S=(3;-2)\\).</b> Nghiệm nhỏ viết trước: \\((-2;3)\\).')]
summary = [('\\(\\Delta\\lt0\\): \\(f\\) has the sign of \\(a\\) everywhere; \\(\\Delta=0\\): sign of \\(a\\) except at the double root.', '\\(\\Delta\\lt0\\): \\(f\\) luôn cùng dấu \\(a\\); \\(\\Delta=0\\): cùng dấu \\(a\\) trừ tại nghiệm kép.'),
           ('\\(\\Delta\\gt0\\): "outside – same, inside – opposite" (to the sign of \\(a\\)).', '\\(\\Delta\\gt0\\): "trong trái, ngoài cùng" (so với dấu của \\(a\\)).'),
           ('\\(ax^2+bx+c\\gt0\\ \\forall x\\iff a\\gt0,\\ \\Delta\\lt0\\).', '\\(ax^2+bx+c\\gt0\\ \\forall x\\iff a\\gt0,\\ \\Delta\\lt0\\).'),
           ('Key words: quadratic trinomial, discriminant, sign table, quadratic inequality.', 'Từ cần nhớ: quadratic trinomial, discriminant, sign table, quadratic inequality.')]
checks = [('I can find the sign of a quadratic trinomial.', 'Em xét được dấu của tam thức bậc hai.'), ('I can solve a quadratic inequality.', 'Em giải được bất phương trình bậc hai.'),
          ('I can find \\(m\\) so that a trinomial keeps one sign.', 'Em tìm được \\(m\\) để tam thức không đổi dấu.'), ('I can use inequalities in real problems.', 'Em vận dụng được bất phương trình vào bài toán thực tế.')]
LL('g10-func-03', 'The Sign of a Quadratic Trinomial', CV, ('Functions and Graphs', 'Hàm số, đồ thị và ứng dụng'), 'functions', 'quadratic-sign', 170, 'Intermediate', 70, ('quadratic functions, quadratic equations', 'hàm số bậc hai, phương trình bậc hai'),
   'The sign theorem for \\(ax^2+bx+c\\), sign tables, quadratic inequalities and real applications.', 'Bài 17 – Định lí về dấu của tam thức bậc hai, bảng xét dấu, giải bất phương trình bậc hai và ứng dụng.',
   ['quadratic trinomial', 'sign table', 'quadratic inequality', 'discriminant'], ['tam thức bậc hai', 'bảng xét dấu', 'bất phương trình bậc hai', 'biệt thức'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g10-func-02'])
