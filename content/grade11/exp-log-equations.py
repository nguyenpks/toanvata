# -*- coding: utf-8 -*-
"""g11-exp-06 = Toán 11 KNTT, Bài 21: Phương trình, bất phương trình mũ và lôgarit. Mã ngân hàng câu hỏi: TOAN11-C6-B21."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g11g as S
from sp_g11g import lg, frn
from sp_g10f import poly

CV = 'Phương trình, bất phương trình mũ và lôgarit'
vocab = defs(CV, [
 ('expeq', 'exponential equation', 'phương trình mũ', 'an equation with the unknown in the exponent, e.g. \\(a^x=b\\).', 'phương trình có ẩn ở số mũ, ví dụ \\(a^x=b\\).', 'Solve the exponential equation.', ''),
 ('logeq', 'logarithmic equation', 'phương trình lôgarit', 'an equation with the unknown inside a logarithm, e.g. \\(\\log_a x=b\\).', 'phương trình có ẩn nằm dưới dấu lôgarit, ví dụ \\(\\log_a x=b\\).', 'Check the domain of the logarithmic equation.', ''),
 ('expineq', 'exponential inequality', 'bất phương trình mũ', 'an inequality with the unknown in the exponent, e.g. \\(a^x\\gt b\\).', 'bất phương trình có ẩn ở số mũ, ví dụ \\(a^x\\gt b\\).', 'Solve the exponential inequality.', ''),
 ('logineq', 'logarithmic inequality', 'bất phương trình lôgarit', 'an inequality with the unknown inside a logarithm.', 'bất phương trình có ẩn nằm dưới dấu lôgarit.', 'Solve the logarithmic inequality.', '')])
goals = [('recognise basic exponential and logarithmic equations and inequalities;', 'nhận biết [[phương trình mũ]], [[phương trình lôgarit]], [[bất phương trình mũ]], [[bất phương trình lôgarit]] cơ bản;'),
         ('solve them by bringing both sides to the same base or by taking logarithms;', 'giải bằng cách đưa về cùng cơ số hoặc lấy lôgarit hai vế;'),
         ('use a new unknown \\(t=a^x\\) and always check the conditions;', 'đặt ẩn phụ \\(t=a^x\\) và luôn kiểm tra điều kiện;'),
         ('solve real problems (interest, growth, decay) with them.', 'giải bài toán thực tế (lãi suất, tăng trưởng, suy giảm).')]
phrases = [('<b>Bring both sides to the same base.</b>', 'Đưa hai vế về cùng cơ số.'), ('<b>Take the logarithm of both sides.</b>', 'Lấy lôgarit hai vế.'), ('<b>The base is less than one, so the inequality reverses.</b>', 'Cơ số nhỏ hơn 1 nên đổi chiều bất phương trình.'),
           ('<b>Check the domain first.</b>', 'Đặt điều kiện trước.'), ('<b>It takes at least six years.</b>', 'Cần ít nhất 6 năm.')]
review = T('From Lessons 19–20: \\(\\log_a b=\\alpha\\iff a^{\\alpha}=b\\); \\(y=a^x\\) and \\(y=\\log_a x\\) are increasing when \\(a\\gt1\\), decreasing when \\(0\\lt a\\lt1\\); \\(\\log_a x\\) needs \\(x\\gt0\\); \\(a^x\\gt0\\) for all \\(x\\).',
           'Từ Bài 19–20: \\(\\log_a b=\\alpha\\iff a^{\\alpha}=b\\); \\(y=a^x\\), \\(y=\\log_a x\\) đồng biến khi \\(a\\gt1\\), nghịch biến khi \\(0\\lt a\\lt1\\); \\(\\log_a x\\) cần \\(x\\gt0\\); \\(a^x\\gt0\\) với mọi \\(x\\).')
theory = '<h3>21.1 %s</h3>' % TI('Exponential equations', 'Phương trình mũ')
theory += BOX('blue', ('Basic forms (\\(a\\gt0\\), \\(a\\ne1\\))', 'Dạng cơ bản (\\(a\\gt0\\), \\(a\\ne1\\))'), UL([T('\\(a^x=b\\): if \\(b\\gt0\\), \\(x=\\log_a b\\); if \\(b\\le0\\), no solution.', '\\(a^x=b\\): nếu \\(b\\gt0\\) thì \\(x=\\log_a b\\); nếu \\(b\\le0\\) thì vô nghiệm.'),
  T('\\(a^{u(x)}=a^{v(x)}\\iff u(x)=v(x)\\) (same base).', '\\(a^{u(x)}=a^{v(x)}\\iff u(x)=v(x)\\) (cùng cơ số).'), T('Equations in \\(a^x\\): put \\(t=a^x\\) (\\(t\\gt0\\)).', 'Phương trình theo \\(a^x\\): đặt \\(t=a^x\\) (\\(t\\gt0\\)).')]))
theory += '<h3>21.2 %s</h3>' % TI('Logarithmic equations', 'Phương trình lôgarit')
theory += BOX('blue', ('Basic forms', 'Dạng cơ bản'), UL([T('\\(\\log_a x=b\\iff x=a^b\\) (always exactly one solution).', '\\(\\log_a x=b\\iff x=a^b\\) (luôn có đúng một nghiệm).'),
  T('\\(\\log_a u(x)=\\log_a v(x)\\iff u(x)=v(x)\\gt0\\).', '\\(\\log_a u(x)=\\log_a v(x)\\iff u(x)=v(x)\\gt0\\).'), T('Write the domain conditions first and check the roots at the end.', 'Đặt điều kiện xác định trước, cuối cùng đối chiếu nghiệm.')]))
theory += '<h3>21.3 %s</h3>' % TI('Inequalities', 'Bất phương trình mũ và lôgarit')
theory += TBL(['', TI('\\(a\\gt1\\)', '\\(a\\gt1\\)'), TI('\\(0\\lt a\\lt1\\)', '\\(0\\lt a\\lt1\\)')], [
  [TI('\\(a^x\\gt b\\) (\\(b\\gt0\\))', '\\(a^x\\gt b\\) (\\(b\\gt0\\))'), '\\(x\\gt\\log_a b\\)', '\\(x\\lt\\log_a b\\)'],
  [TI('\\(a^x\\gt b\\) (\\(b\\le0\\))', '\\(a^x\\gt b\\) (\\(b\\le0\\))'), TI('every \\(x\\)', 'mọi \\(x\\)'), TI('every \\(x\\)', 'mọi \\(x\\)')],
  [TI('\\(\\log_a x\\gt b\\)', '\\(\\log_a x\\gt b\\)'), '\\(x\\gt a^b\\)', '\\(0\\lt x\\lt a^b\\)']])
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('With base \\(0\\lt a\\lt1\\) the inequality sign <b>reverses</b>. For logarithmic inequalities never forget \\(x\\gt0\\) (the argument must be positive): \\(\\log_{\\frac12}x\\gt1\\iff0\\lt x\\lt\\frac12\\), not just \\(x\\lt\\frac12\\).', 'Với cơ số \\(0\\lt a\\lt1\\) phải <b>đổi chiều</b> bất phương trình. Với bất phương trình lôgarit đừng quên \\(x\\gt0\\): \\(\\log_{\\frac12}x\\gt1\\iff0\\lt x\\lt\\frac12\\), không chỉ là \\(x\\lt\\frac12\\).'))

assert F(2) ** (-3 + 1) == F(1, 4) and all(3 ** (x * x - x) == 9 for x in (-1, 2))
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Exponential equations', 'Phương trình mũ'), T('Solve a) \\(2^{x+1}=\\frac14\\); b) \\(3^{x^2-x}=9\\); c) \\(5^x=7\\).', 'Giải các phương trình a) \\(2^{x+1}=\\frac14\\); b) \\(3^{x^2-x}=9\\); c) \\(5^x=7\\).'), T('Same base, or take \\(\\log_5\\).', 'Đưa về cùng cơ số, hoặc lấy \\(\\log_5\\).'),
  [T('a) \\(\\frac14=2^{-2}\\Rightarrow x+1=-2\\Rightarrow x=-3\\).', 'a) \\(\\frac14=2^{-2}\\Rightarrow x+1=-2\\Rightarrow x=-3\\).'), T('b) \\(x^2-x=2\\iff x=-1\\) or \\(x=2\\).', 'b) \\(x^2-x=2\\iff x=-1\\) hoặc \\(x=2\\).'), T('c) \\(x=\\log_5 7\\approx1.209\\).', 'c) \\(x=\\log_5 7\\approx1{,}209\\).')],
  T('a) \\(x=-3\\); b) \\(S=\\{-1;2\\}\\); c) \\(x=\\log_5 7\\).', 'a) \\(x=-3\\); b) \\(S=\\{-1;2\\}\\); c) \\(x=\\log_5 7\\).'))
assert abs(math.log(7, 5) - 1.209) < 0.001 and (0 + 1) * (0 + 3) == 3 and (-4 + 1) < 0
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Logarithmic equations', 'Phương trình lôgarit'), T('Solve a) \\(\\log_2(x-1)=3\\); b) \\(\\log_3(x+1)+\\log_3(x+3)=1\\).', 'Giải các phương trình a) \\(\\log_2(x-1)=3\\); b) \\(\\log_3(x+1)+\\log_3(x+3)=1\\).'), T('Conditions first.', 'Đặt điều kiện trước.'),
  [T('a) \\(x\\gt1\\); \\(x-1=2^3\\Rightarrow x=9\\) ✓.', 'a) \\(x\\gt1\\); \\(x-1=2^3\\Rightarrow x=9\\) ✓.'), T('b) \\(x\\gt-1\\); \\(\\log_3[(x+1)(x+3)]=1\\iff x^2+4x+3=3\\iff x=0\\) or \\(x=-4\\); only \\(x=0\\) satisfies \\(x\\gt-1\\).', 'b) \\(x\\gt-1\\); \\(\\log_3[(x+1)(x+3)]=1\\iff x^2+4x+3=3\\iff x=0\\) hoặc \\(x=-4\\); chỉ \\(x=0\\) thỏa \\(x\\gt-1\\).')],
  T('a) \\(x=9\\); b) \\(x=0\\).', 'a) \\(x=9\\); b) \\(x=0\\).'))
assert all((F(1, 2) ** x > 8) == (x < -3) for x in range(-6, 3)) and all((math.log(x + 1, 0.5) >= -2 - 1e-12) == (-1 < x <= 3) for x in [F(k, 2) for k in range(-1, 12)])
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Inequalities', 'Bất phương trình'), T('Solve a) \\(\\left(\\frac12\\right)^x\\gt8\\); b) \\(\\log_{0.5}(x+1)\\ge-2\\).', 'Giải a) \\(\\left(\\frac12\\right)^x\\gt8\\); b) \\(\\log_{0{,}5}(x+1)\\ge-2\\).'), T('Base less than 1: reverse the sign.', 'Cơ số nhỏ hơn 1: đổi chiều.'),
  [T('a) \\(8=\\left(\\frac12\\right)^{-3}\\Rightarrow x\\lt-3\\).', 'a) \\(8=\\left(\\frac12\\right)^{-3}\\Rightarrow x\\lt-3\\).'), T('b) \\(x+1\\gt0\\) and \\(x+1\\le0.5^{-2}=4\\iff-1\\lt x\\le3\\).', 'b) \\(x+1\\gt0\\) và \\(x+1\\le0{,}5^{-2}=4\\iff-1\\lt x\\le3\\).')],
  T('a) \\(x\\lt-3\\); b) \\((-1;3]\\).', 'a) \\(x\\lt-3\\); b) \\((-1;3]\\).'))
assert all(4 ** x - 6 * 2 ** x + 8 == 0 for x in (1, 2))
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('A new unknown', 'Đặt ẩn phụ'), T('Solve \\(4^x-6\\cdot2^x+8=0\\).', 'Giải phương trình \\(4^x-6\\cdot2^x+8=0\\).'), T('\\(4^x=(2^x)^2\\); put \\(t=2^x\\gt0\\).', '\\(4^x=(2^x)^2\\); đặt \\(t=2^x\\gt0\\).'),
  [T('\\(t^2-6t+8=0\\iff t=2\\) or \\(t=4\\) (both positive).', '\\(t^2-6t+8=0\\iff t=2\\) hoặc \\(t=4\\) (đều dương).'), T('\\(2^x=2\\iff x=1\\); \\(2^x=4\\iff x=2\\).', '\\(2^x=2\\iff x=1\\); \\(2^x=4\\iff x=2\\).')], T('\\(S=\\{1;2\\}\\).', '\\(S=\\{1;2\\}\\).'))
n5 = math.log(1.5) / math.log(1.07); assert 5 < n5 < 6 and 1.07 ** 5 < 1.5 < 1.07 ** 6
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('How long to save?', 'Gửi tiết kiệm bao lâu?'), T('Ms Lan deposits 100 million VND at 7%/year compound interest. After how many full years will she have at least 150 million VND?', 'Cô Lan gửi 100 triệu đồng, lãi kép 7%/năm. Sau ít nhất bao nhiêu năm (tròn năm) cô có từ 150 triệu đồng trở lên?'),
  T('Solve \\(100\\cdot1.07^n\\ge150\\) by taking logarithms.', 'Giải \\(100\\cdot1{,}07^n\\ge150\\) bằng cách lấy lôgarit.'), [T('\\(1.07^n\\ge1.5\\iff n\\ge\\log_{1.07}1.5=\\dfrac{\\ln1.5}{\\ln1.07}\\approx5.99\\) (base \\(\\gt1\\)).', '\\(1{,}07^n\\ge1{,}5\\iff n\\ge\\log_{1{,}07}1{,}5=\\dfrac{\\ln1{,}5}{\\ln1{,}07}\\approx5{,}99\\) (cơ số \\(\\gt1\\)).'),
  T('Check: \\(1.07^5\\approx1.403\\lt1.5\\), \\(1.07^6\\approx1.501\\ge1.5\\).', 'Kiểm tra: \\(1{,}07^5\\approx1{,}403\\lt1{,}5\\), \\(1{,}07^6\\approx1{,}501\\ge1{,}5\\).')], T('6 years.', '6 năm.'))

def lvl(P):
    a1, m1, n1, k1 = P['e1']; x1 = F(k1 - n1, m1); assert x1.denominator == 1; ex1 = poly([m1, n1]); R1 = frn(F(a1) ** k1)
    o1 = M4(1, 'Solve \\(%d^{%s}=%s\\).' % (a1, ex1, R1), 'Giải phương trình \\(%d^{%s}=%s\\).' % (a1, ex1, R1), '\\(x=%d\\)' % x1, ['\\(x=%d\\)' % (x1 + 1), '\\(x=%d\\)' % (-x1 if x1 else 2), '\\(x=%d\\)' % k1, '\\(x=%d\\)' % (x1 - 1)],
            '\\(%s=%d\\).' % (ex1, k1), '\\(%s=%d^{%d}\\Rightarrow %s=%d\\).' % (R1, a1, k1, ex1, k1))  # T-002: thiếu dấu cách tạo \Rightarrowx
    a2, b2, c2 = P['l1']; x2 = a2 ** c2 - b2
    o2 = M4(2, 'Find \\(x\\) such that \\(\\log_{%d}(x%+d)=%d\\).' % (a2, b2, c2), 'Tìm \\(x\\) thỏa mãn \\(\\log_{%d}(x%+d)=%d\\).' % (a2, b2, c2), '\\(x=%d\\)' % x2, ['\\(x=%d\\)' % (a2 * c2 - b2), '\\(x=%d\\)' % (c2 ** a2 - b2), '\\(x=%d\\)' % (a2 ** c2 + b2), '\\(x=%d\\)' % (x2 + 1), '\\(x=%d\\)' % (x2 - 1), '\\(x=%d\\)' % (a2 ** (c2 + 1) - b2)],
            '\\(x%+d=%d^{%d}\\).' % (b2, a2, c2), '\\(x%+d=%d^{%d}=%d\\Rightarrow x=%d\\).' % (b2, a2, c2, a2 ** c2, x2))
    base3, k3, rel3 = P['i1']; inc = F(base3) > 1; flip = {'\\gt': '\\lt', '\\lt': '\\gt', '\\ge': '\\le', '\\le': '\\ge'}; rr = rel3 if inc else flip[rel3]
    B3 = str(base3) if F(base3).denominator == 1 else '\\left(%s\\right)' % frn(base3); R3 = frn(F(base3) ** k3)
    o3 = M4(3, 'The solution set of the inequality \\(%s^x%s%s\\) is described by…' % (B3, rel3, R3), 'Tập nghiệm của bất phương trình \\(%s^x%s%s\\) được mô tả bởi…' % (B3, rel3, R3), '\\(x%s%d\\)' % (rr, k3), ['\\(x%s%d\\)' % (flip[rr], k3), '\\(x%s%d\\)' % (rr, -k3), '\\(x%s%s\\)' % (rr, R3)],
            '\\(%s=%s^{%d}\\).' % (R3, B3, k3), '\\(%s=%s^{%d}\\); cơ số %s 1.' % (R3, B3, k3, 'lớn hơn' if inc else 'nhỏ hơn'))
    (e4, v4_), (e5, v5_) = P['tf']
    t4 = tf(4, e4[0], e4[1], v4_, e4[2], e4[3]); t5 = tf(5, e5[0], e5[1], v5_, e5[2], e5[3])
    a6, i6, j6 = P['sub']; u, v = a6 ** i6, a6 ** j6
    s6 = sh(6, 'Find the sum of the solutions of \\(%d^x-%d\\cdot%d^x+%d=0\\).' % (a6 * a6, u + v, a6, u * v), 'Tính tổng các nghiệm của phương trình \\(%d^x-%d\\cdot%d^x+%d=0\\).' % (a6 * a6, u + v, a6, u * v), i6 + j6,
            '\\(t=%d^x\\): \\(t=%d\\), \\(t=%d\\Rightarrow x=%d,\\ x=%d\\).' % (a6, u, v, i6, j6), 'Đặt \\(t=%d^x\\gt0\\): \\(t=%d\\), \\(t=%d\\Rightarrow x=%d,\\ x=%d\\).' % (a6, u, v, i6, j6))
    rate, k7 = P['save']; n = 0; val = F(1)
    while val < k7: n += 1; val *= F(100 + rate, 100)
    s7 = sh(7, 'Money at %d%%/year compound interest. After at least how many full years does it reach %s times the deposit?' % (rate, '%g' % float(k7)), 'Gửi tiết kiệm lãi kép %d%%/năm. Sau ít nhất bao nhiêu năm (tròn năm) số tiền đạt từ %s lần số tiền gửi trở lên?' % (rate, ('%g' % float(k7)).replace('.', ',')), n,
            '\\(n\\ge\\log_{%s}%s\\approx%.2f\\).' % (('%g' % (1 + rate / 100)), ('%g' % float(k7)), math.log(float(k7)) / math.log(1 + rate / 100)), '\\(n\\ge\\log_{%s}%s\\approx%s\\).' % (('%g' % (1 + rate / 100)).replace('.', '{,}'), ('%g' % float(k7)).replace('.', '{,}'), ('%.2f' % (math.log(float(k7)) / math.log(1 + rate / 100))).replace('.', '{,}')))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
VA = (('\\(\\log_2(x-1)+\\log_2(x+1)=3\\) has the solutions \\(x=\\pm3\\).', 'Phương trình \\(\\log_2(x-1)+\\log_2(x+1)=3\\) có hai nghiệm \\(x=\\pm3\\).', 'Need \\(x\\gt1\\): only \\(x=3\\).', 'Điều kiện \\(x\\gt1\\): chỉ có \\(x=3\\).'), False)
VB = (('\\(\\left(\\frac13\\right)^x\\lt9\\iff x\\gt-2\\).', '\\(\\left(\\frac13\\right)^x\\lt9\\iff x\\gt-2\\).', '\\(9=\\left(\\frac13\\right)^{-2}\\), base \\(\\lt1\\): reverse.', '\\(9=\\left(\\frac13\\right)^{-2}\\), cơ số nhỏ hơn 1: đổi chiều.'), True)
VC = (('The equation \\(3^x=-9\\) has the solution \\(x=-2\\).', 'Phương trình \\(3^x=-9\\) có nghiệm \\(x=-2\\).', '\\(3^x\\gt0\\): no solution.', '\\(3^x\\gt0\\) nên phương trình vô nghiệm.'), False)
VD = (('\\(\\log_3 x\\lt2\\iff0\\lt x\\lt9\\).', '\\(\\log_3 x\\lt2\\iff0\\lt x\\lt9\\).', '\\(x\\gt0\\) and \\(x\\lt3^2\\).', '\\(x\\gt0\\) và \\(x\\lt3^2\\).'), True)
VE = (('\\(\\log_{\\frac12}x\\gt1\\iff x\\lt\\frac12\\).', '\\(\\log_{\\frac12}x\\gt1\\iff x\\lt\\frac12\\).', 'Also need \\(x\\gt0\\): \\(0\\lt x\\lt\\frac12\\).', 'Còn cần \\(x\\gt0\\): \\(0\\lt x\\lt\\frac12\\).'), False)
VF = (('\\(5^x=7\\iff x=\\log_5 7\\).', '\\(5^x=7\\iff x=\\log_5 7\\).', 'Definition of the logarithm.', 'Theo định nghĩa lôgarit.'), True)
PP = [dict(e1=(2, 1, 1, 4), l1=(2, -1, 3), i1=(3, 2, '\\gt'), tf=(VA, VB), sub=(2, 0, 2), save=(8, 2)),
      dict(e1=(3, 2, -1, 3), l1=(3, 2, 2), i1=(F(1, 2), -3, '\\ge'), tf=(VC, VD), sub=(3, 0, 1), save=(6, F(3, 2))),
      dict(e1=(5, 1, 3, -1), l1=(5, -3, 1), i1=(F(1, 3), 2, '\\lt'), tf=(VE, VF), sub=(3, 1, 2), save=(10, 3))]
practice = three(lvl, PP)
# Hiệu chỉnh 13/11/2026: phần D gồm 8 dạng khác nhau, không lặp "Solve …" (tools/sp_g11r.py)
import sp_g11r as R
practice = R.with_d(practice, R.D21, seeds=(2101, 2102, 2103))
mistakes = [('<b>Not reversing the sign when the base is in \\((0;1)\\).</b>', '<b>Không đổi chiều khi cơ số thuộc \\((0;1)\\).</b>'),
            ('<b>Skipping the domain of logarithms.</b> Roots that make an argument \\(\\le0\\) must be rejected.', '<b>Bỏ qua điều kiện của lôgarit.</b> Nghiệm làm biểu thức dưới dấu lôgarit \\(\\le0\\) phải bị loại.'),
            ('<b>Keeping \\(t\\le0\\) after putting \\(t=a^x\\).</b> \\(a^x\\) is always positive.', '<b>Giữ \\(t\\le0\\) sau khi đặt \\(t=a^x\\).</b> \\(a^x\\) luôn dương.'),
            ('<b>Rounding \\(n\\) down in money problems.</b> If \\(n\\ge5.99\\), the answer is 6 years, not 5.', '<b>Làm tròn xuống \\(n\\) trong bài toán tiền gửi.</b> Nếu \\(n\\ge5{,}99\\) thì đáp số là 6 năm, không phải 5.')]
summary = [('\\(a^x=b\\ (b\\gt0)\\iff x=\\log_a b\\); \\(a^{u}=a^{v}\\iff u=v\\).', '\\(a^x=b\\ (b\\gt0)\\iff x=\\log_a b\\); \\(a^{u}=a^{v}\\iff u=v\\).'),
           ('\\(\\log_a x=b\\iff x=a^b\\); \\(\\log_a u=\\log_a v\\iff u=v\\gt0\\).', '\\(\\log_a x=b\\iff x=a^b\\); \\(\\log_a u=\\log_a v\\iff u=v\\gt0\\).'),
           ('Inequalities: keep the sign if \\(a\\gt1\\), reverse it if \\(0\\lt a\\lt1\\); logarithms also need the argument \\(\\gt0\\).', 'Bất phương trình: giữ chiều nếu \\(a\\gt1\\), đổi chiều nếu \\(0\\lt a\\lt1\\); với lôgarit còn cần biểu thức dưới dấu log dương.'),
           ('Key words: exponential equation, logarithmic equation, same base, take logarithms.', 'Từ cần nhớ: exponential equation, logarithmic equation, same base, take logarithms.')]
checks = [('I can solve basic exponential equations.', 'Em giải được phương trình mũ cơ bản.'), ('I can solve basic logarithmic equations with conditions.', 'Em giải được phương trình lôgarit cơ bản có điều kiện.'),
          ('I can solve exponential and logarithmic inequalities.', 'Em giải được bất phương trình mũ, lôgarit.'), ('I can solve interest and growth problems.', 'Em giải được bài toán lãi suất, tăng trưởng.')]
LL('g11-exp-06', 'Exponential and Logarithmic Equations and Inequalities', CV, ('Exponential and Logarithmic Functions', 'Hàm số mũ và hàm số lôgarit'), 'exponential-functions', 'exp-log-equations', 220, 'Intermediate', 75, ('exponential and logarithmic functions', 'hàm số mũ, hàm số lôgarit'),
   'Basic exponential and logarithmic equations and inequalities, same base, new unknown, real problems.', 'Bài 21 – Phương trình, bất phương trình mũ và lôgarit cơ bản; đưa về cùng cơ số, đặt ẩn phụ; bài toán thực tế.',
   ['exponential equation', 'logarithmic equation', 'inequality', 'compound interest'], ['phương trình mũ', 'phương trình lôgarit', 'bất phương trình', 'lãi kép'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g11-exp-05'])
