# -*- coding: utf-8 -*-
"""g11-exp-04 = Toán 11 KNTT, Bài 19: Lôgarit. Mã ngân hàng câu hỏi: TOAN11-C6-B19."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g11g as S
from sp_g11g import lg, frn

CV = 'Lôgarit'
vocab = defs(CV, [
 ('logar', 'logarithm', 'lôgarit', 'for \\(a\\gt0\\), \\(a\\ne1\\), \\(b\\gt0\\): \\(\\log_a b=\\alpha\\iff a^{\\alpha}=b\\).', 'với \\(a\\gt0\\), \\(a\\ne1\\), \\(b\\gt0\\): \\(\\log_a b=\\alpha\\iff a^{\\alpha}=b\\).', 'The logarithm of eight to base two is three.', '\\(\\log_a b\\)'),
 ('lg10', 'common logarithm', 'lôgarit thập phân', 'the logarithm to base 10, written \\(\\log b\\) (or \\(\\lg b\\)).', 'lôgarit cơ số 10, kí hiệu \\(\\log b\\) (hoặc \\(\\lg b\\)).', 'log 1000 = 3.', '\\(\\log\\)'),
 ('lnat', 'natural logarithm', 'lôgarit tự nhiên', 'the logarithm to base \\(e\\approx2.718\\), written \\(\\ln b\\).', 'lôgarit cơ số \\(e\\approx2{,}718\\), kí hiệu \\(\\ln b\\).', 'ln e = 1.', '\\(\\ln\\)'),
 ('chbase', 'change of base formula', 'công thức đổi cơ số', '\\(\\log_a b=\\dfrac{\\log_c b}{\\log_c a}\\).', '\\(\\log_a b=\\dfrac{\\log_c b}{\\log_c a}\\).', 'Use the change of base formula.', '')])
goals = [('state the definition of the logarithm and its basic properties;', 'phát biểu định nghĩa [[lôgarit]] và các tính chất cơ bản;'),
         ('compute logarithms and use the product, quotient and power rules;', 'tính lôgarit và dùng quy tắc tích, thương, lũy thừa;'),
         ('use the change of base formula, common and natural logarithms;', 'dùng [[công thức đổi cơ số]], [[lôgarit thập phân]] và [[lôgarit tự nhiên]];'),
         ('apply logarithms to scales (pH, decibel, Richter).', 'vận dụng lôgarit vào các thang đo (pH, đêxiben, Richter).')]
phrases = [('<b>The logarithm of eight to base two is three.</b>', '\\(\\log_2 8=3\\).'), ('<b>Two to the power three equals eight.</b>', '\\(2^3=8\\).'), ('<b>The log of a product is the sum of the logs.</b>', 'Lôgarit của một tích bằng tổng các lôgarit.'),
           ('<b>Change to base ten.</b>', 'Đổi sang cơ số 10.'), ('<b>An increase of one unit means ten times stronger.</b>', 'Tăng 1 đơn vị nghĩa là mạnh gấp 10 lần.')]
review = T('From Lesson 18: \\(a^{\\alpha}a^{\\beta}=a^{\\alpha+\\beta}\\), \\(\\dfrac{a^{\\alpha}}{a^{\\beta}}=a^{\\alpha-\\beta}\\), \\((a^{\\alpha})^{\\beta}=a^{\\alpha\\beta}\\), \\(a^{\\frac mn}=\\sqrt[n]{a^m}\\) (\\(a\\gt0\\)). The logarithm answers the question "to which power must I raise \\(a\\) to get \\(b\\)?".',
           'Từ Bài 18: \\(a^{\\alpha}a^{\\beta}=a^{\\alpha+\\beta}\\), \\(\\dfrac{a^{\\alpha}}{a^{\\beta}}=a^{\\alpha-\\beta}\\), \\((a^{\\alpha})^{\\beta}=a^{\\alpha\\beta}\\), \\(a^{\\frac mn}=\\sqrt[n]{a^m}\\) (\\(a\\gt0\\)). Lôgarit trả lời câu hỏi "phải nâng \\(a\\) lên lũy thừa bao nhiêu để được \\(b\\)?".')
theory = '<h3>19.1 %s</h3>' % TI('The logarithm', 'Khái niệm lôgarit')
theory += BOX('blue', ('Definition', 'Định nghĩa'), T('Let \\(a\\gt0\\), \\(a\\ne1\\), \\(b\\gt0\\). The number \\(\\alpha\\) with \\(a^{\\alpha}=b\\) is the logarithm of \\(b\\) to base \\(a\\): \\[\\log_a b=\\alpha\\iff a^{\\alpha}=b.\\] Base 10: \\(\\log b\\) (common logarithm); base \\(e\\approx2.718\\): \\(\\ln b\\) (natural logarithm).',
  'Cho \\(a\\gt0\\), \\(a\\ne1\\), \\(b\\gt0\\). Số \\(\\alpha\\) thỏa \\(a^{\\alpha}=b\\) là lôgarit cơ số \\(a\\) của \\(b\\): \\[\\log_a b=\\alpha\\iff a^{\\alpha}=b.\\] Cơ số 10: \\(\\log b\\) (lôgarit thập phân); cơ số \\(e\\approx2{,}718\\): \\(\\ln b\\) (lôgarit tự nhiên).'))
theory += BOX('mint', ('Immediate properties', 'Tính chất'), T('\\(\\log_a1=0\\); \\(\\log_a a=1\\); \\(\\log_a a^{\\alpha}=\\alpha\\); \\(a^{\\log_a b}=b\\). Examples: \\(\\log_2 8=3\\), \\(\\log_3\\frac19=-2\\), \\(\\log 1000=3\\), \\(\\ln e^2=2\\).',
  '\\(\\log_a1=0\\); \\(\\log_a a=1\\); \\(\\log_a a^{\\alpha}=\\alpha\\); \\(a^{\\log_a b}=b\\). Ví dụ: \\(\\log_2 8=3\\), \\(\\log_3\\frac19=-2\\), \\(\\log 1000=3\\), \\(\\ln e^2=2\\).'))
theory += '<h3>19.2 %s</h3>' % TI('Rules of logarithms', 'Tính chất của lôgarit')
theory += BOX('blue', ('For \\(a\\gt0\\), \\(a\\ne1\\), \\(M,N\\gt0\\)', 'Với \\(a\\gt0\\), \\(a\\ne1\\), \\(M,N\\gt0\\)'), UL([T('\\(\\log_a(MN)=\\log_a M+\\log_a N\\); \\(\\log_a\\dfrac MN=\\log_a M-\\log_a N\\).', '\\(\\log_a(MN)=\\log_a M+\\log_a N\\); \\(\\log_a\\dfrac MN=\\log_a M-\\log_a N\\).'),
  T('\\(\\log_a M^{\\alpha}=\\alpha\\log_a M\\); in particular \\(\\log_a\\dfrac1N=-\\log_a N\\), \\(\\log_a\\sqrt[n]{M}=\\dfrac1n\\log_a M\\).', '\\(\\log_a M^{\\alpha}=\\alpha\\log_a M\\); đặc biệt \\(\\log_a\\dfrac1N=-\\log_a N\\), \\(\\log_a\\sqrt[n]{M}=\\dfrac1n\\log_a M\\).'),
  T('Change of base (\\(c\\gt0\\), \\(c\\ne1\\)): \\(\\log_a b=\\dfrac{\\log_c b}{\\log_c a}\\); hence \\(\\log_a b=\\dfrac{1}{\\log_b a}\\) (\\(b\\ne1\\)) and \\(\\log_{a^{\\alpha}}b=\\dfrac1{\\alpha}\\log_a b\\).', 'Đổi cơ số (\\(c\\gt0\\), \\(c\\ne1\\)): \\(\\log_a b=\\dfrac{\\log_c b}{\\log_c a}\\); suy ra \\(\\log_a b=\\dfrac{1}{\\log_b a}\\) (\\(b\\ne1\\)) và \\(\\log_{a^{\\alpha}}b=\\dfrac1{\\alpha}\\log_a b\\).')]))
vals = [(2, math.log10(2)), (3, math.log10(3)), (5, math.log10(5)), (7, math.log10(7))]
theory += TBL([TI('\\(x\\)', '\\(x\\)')] + ['\\(%d\\)' % x for x, _ in vals], [[TI('\\(\\log x\\) (calculator)', '\\(\\log x\\) (máy tính)')] + [TI('\\(\\approx%s\\)' % ('%.4f' % v), '\\(\\approx%s\\)' % ('%.4f' % v).replace('.', '{,}')) for _, v in vals]])
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('There is <b>no</b> rule for \\(\\log_a(M+N)\\): \\(\\log_2(2+2)=2\\ne\\log_2 2+\\log_2 2=2\\) is only a coincidence; \\(\\log_2(4+4)=3\\ne4\\). Also \\(\\log_a M^2=2\\log_a|M|\\) when \\(M\\) may be negative.', '<b>Không có</b> quy tắc cho \\(\\log_a(M+N)\\): \\(\\log_2(4+4)=3\\ne\\log_2 4+\\log_2 4=4\\). Ngoài ra \\(\\log_a M^2=2\\log_a|M|\\) khi \\(M\\) có thể âm.'))

assert 2 ** 3 == 8 and F(1, 9) == F(3) ** -2 and F(1, 2) ** -2 == 4 and 10 ** 3 == 1000
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Computing logarithms', 'Tính lôgarit'), T('Compute \\(\\log_2 8\\), \\(\\log_3\\frac19\\), \\(\\log_{\\frac12}4\\), \\(\\log 1000\\), \\(\\ln e^3\\).', 'Tính \\(\\log_2 8\\), \\(\\log_3\\frac19\\), \\(\\log_{\\frac12}4\\), \\(\\log 1000\\), \\(\\ln e^3\\).'),
  T('Write each number as a power of the base.', 'Viết mỗi số thành lũy thừa của cơ số.'),
  [T('\\(8=2^3\\Rightarrow\\log_2 8=3\\); \\(\\frac19=3^{-2}\\Rightarrow\\log_3\\frac19=-2\\).', '\\(8=2^3\\Rightarrow\\log_2 8=3\\); \\(\\frac19=3^{-2}\\Rightarrow\\log_3\\frac19=-2\\).'), T('\\(4=\\left(\\frac12\\right)^{-2}\\Rightarrow\\log_{\\frac12}4=-2\\); \\(\\log10^3=3\\); \\(\\ln e^3=3\\).', '\\(4=\\left(\\frac12\\right)^{-2}\\Rightarrow\\log_{\\frac12}4=-2\\); \\(\\log10^3=3\\); \\(\\ln e^3=3\\).')],
  T('\\(3\\); \\(-2\\); \\(-2\\); \\(3\\); \\(3\\).', '\\(3\\); \\(-2\\); \\(-2\\); \\(3\\); \\(3\\).'))
assert 9 * 4 == 36 == 6 ** 2 and F(40, 5) == 8 and F(25) ** F(1, 3) and 25 == 5 ** 2
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Using the rules', 'Dùng tính chất'), T('Compute \\(A=\\log_6 9+\\log_6 4\\), \\(B=\\log_2 40-\\log_2 5\\), \\(C=\\log_5\\sqrt[3]{25}\\).', 'Tính \\(A=\\log_6 9+\\log_6 4\\), \\(B=\\log_2 40-\\log_2 5\\), \\(C=\\log_5\\sqrt[3]{25}\\).'),
  T('Product rule, quotient rule, power rule.', 'Quy tắc tích, thương, lũy thừa.'),
  [T('\\(A=\\log_6 36=2\\); \\(B=\\log_2 8=3\\).', '\\(A=\\log_6 36=2\\); \\(B=\\log_2 8=3\\).'), T('\\(\\sqrt[3]{25}=5^{\\frac23}\\Rightarrow C=\\frac23\\).', '\\(\\sqrt[3]{25}=5^{\\frac23}\\Rightarrow C=\\frac23\\).')], T('\\(A=2\\), \\(B=3\\), \\(C=\\frac23\\).', '\\(A=2\\), \\(B=3\\), \\(C=\\frac23\\).'))
assert 72 == 2 ** 3 * 3 ** 2 and F(3, 2) == F(math.log2(8)) / F(math.log2(4)) and F(3, 2) == F(3, 2)
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Changing the base', 'Đổi cơ số'), T('a) Given \\(a=\\log_2 3\\), express \\(\\log_2 72\\) and \\(\\log_3 2\\) in terms of \\(a\\). b) Compute \\(\\log_4 8\\) and \\(\\log_9 27\\).', 'a) Cho \\(a=\\log_2 3\\). Biểu diễn \\(\\log_2 72\\) và \\(\\log_3 2\\) theo \\(a\\). b) Tính \\(\\log_4 8\\) và \\(\\log_9 27\\).'),
  T('Factorise 72; use \\(\\log_a b=\\frac{1}{\\log_b a}\\) and change to a common base.', 'Phân tích 72 ra thừa số; dùng \\(\\log_a b=\\frac{1}{\\log_b a}\\) và đổi về cùng cơ số.'),
  [T('\\(72=2^3\\cdot3^2\\Rightarrow\\log_2 72=3+2a\\); \\(\\log_3 2=\\dfrac1a\\).', '\\(72=2^3\\cdot3^2\\Rightarrow\\log_2 72=3+2a\\); \\(\\log_3 2=\\dfrac1a\\).'), T('\\(\\log_4 8=\\dfrac{\\log_2 8}{\\log_2 4}=\\dfrac32\\); \\(\\log_9 27=\\dfrac{\\log_3 27}{\\log_3 9}=\\dfrac32\\).', '\\(\\log_4 8=\\dfrac{\\log_2 8}{\\log_2 4}=\\dfrac32\\); \\(\\log_9 27=\\dfrac{\\log_3 27}{\\log_3 9}=\\dfrac32\\).')],
  T('\\(3+2a\\); \\(\\frac1a\\); \\(\\frac32\\); \\(\\frac32\\).', '\\(3+2a\\); \\(\\frac1a\\); \\(\\frac32\\); \\(\\frac32\\).'))
assert 2 * 5 == 10 and (3 ** 2) ** 1 == 9 and 2 ** 2 == 4
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Powers with logarithmic exponents', 'Lũy thừa có số mũ là lôgarit'), T('Compute \\(P=2^{\\log_2 5+1}\\) and \\(Q=9^{\\log_3 2}\\).', 'Tính \\(P=2^{\\log_2 5+1}\\) và \\(Q=9^{\\log_3 2}\\).'), T('\\(a^{\\log_a b}=b\\); write \\(9=3^2\\).', '\\(a^{\\log_a b}=b\\); viết \\(9=3^2\\).'),
  [T('\\(P=2^{\\log_2 5}\\cdot2=5\\cdot2=10\\).', '\\(P=2^{\\log_2 5}\\cdot2=5\\cdot2=10\\).'), T('\\(Q=(3^2)^{\\log_3 2}=\\left(3^{\\log_3 2}\\right)^2=2^2=4\\).', '\\(Q=(3^2)^{\\log_3 2}=\\left(3^{\\log_3 2}\\right)^2=2^2=4\\).')], T('\\(P=10\\), \\(Q=4\\).', '\\(P=10\\), \\(Q=4\\).'))
assert 10 ** (F(72, 10) - F(52, 10)) == 100 and 10 ** ((90 - 60) // 10) == 1000
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Earthquakes and noise', 'Động đất và tiếng ồn'), T('a) The Richter magnitude is \\(M=\\log\\dfrac{A}{A_0}\\) (\\(A\\): amplitude). How many times larger is the amplitude of a 7.2 earthquake than that of a 5.2 one? b) Sound level \\(L=10\\log\\dfrac{I}{I_0}\\) (dB). A street is 60 dB, a concert 90 dB. Compare the intensities.', 'a) Độ lớn động đất theo Richter là \\(M=\\log\\dfrac{A}{A_0}\\) (\\(A\\): biên độ). Biên độ trận 7,2 độ lớn gấp bao nhiêu lần trận 5,2 độ? b) Mức cường độ âm \\(L=10\\log\\dfrac{I}{I_0}\\) (dB). Đường phố 60 dB, buổi hòa nhạc 90 dB. So sánh cường độ âm.'),
  T('Subtract the two equations: \\(\\log\\frac{A_1}{A_0}-\\log\\frac{A_2}{A_0}=\\log\\frac{A_1}{A_2}\\).', 'Trừ hai đẳng thức: \\(\\log\\frac{A_1}{A_0}-\\log\\frac{A_2}{A_0}=\\log\\frac{A_1}{A_2}\\).'),
  [T('a) \\(\\log\\dfrac{A_1}{A_2}=7.2-5.2=2\\Rightarrow\\dfrac{A_1}{A_2}=10^2=100\\).', 'a) \\(\\log\\dfrac{A_1}{A_2}=7{,}2-5{,}2=2\\Rightarrow\\dfrac{A_1}{A_2}=10^2=100\\).'), T('b) \\(10\\log\\dfrac{I_1}{I_2}=90-60=30\\Rightarrow\\dfrac{I_1}{I_2}=10^3=1000\\).', 'b) \\(10\\log\\dfrac{I_1}{I_2}=90-60=30\\Rightarrow\\dfrac{I_1}{I_2}=10^3=1000\\).')],
  T('a) 100 times; b) the concert is 1000 times more intense (although "only" 30 dB louder).', 'a) 100 lần; b) cường độ âm buổi hòa nhạc gấp 1000 lần (dù "chỉ" hơn 30 dB).'))

def lvl(P):
    b1, k1 = P['val']; N1 = F(b1) ** k1
    o1 = M4(1, '\\(%s=\\)…' % lg(b1, frn(N1) if N1.denominator == 1 else '{%s}' % frn(N1)), '\\(%s=\\)…' % lg(b1, frn(N1) if N1.denominator == 1 else '{%s}' % frn(N1)), '\\(%d\\)' % k1, ['\\(%d\\)' % -k1, '\\(%d\\)' % (k1 + 1), '\\(%s\\)' % frn(N1 / b1)],
            '\\(%d^{%d}=%s\\).' % (b1, k1, frn(N1)), '\\(%d^{%d}=%s\\).' % (b1, k1, frn(N1)))
    b2, m2, n2 = P['sum']; v2 = round(math.log(m2 * n2, b2)); assert b2 ** v2 == m2 * n2
    o2 = M4(2, '\\(%s+%s=\\)…' % (lg(b2, m2), lg(b2, n2)), '\\(%s+%s=\\)…' % (lg(b2, m2), lg(b2, n2)), '\\(%d\\)' % v2, ['\\(%s\\)' % lg(b2, m2 + n2), '\\(%d\\)' % (v2 + 1), '\\(%d\\)' % (m2 * n2)],
            '\\(\\log_{%d}%d=%d\\).' % (b2, m2 * n2, v2), '\\(\\log_{%d}%d=%d\\).' % (b2, m2 * n2, v2))
    p3, q3, i3, j3 = P['expr']; N3 = p3 ** i3 * q3 ** j3
    o3 = M4(3, 'Given \\(%s=a\\), \\(%s=\\)…' % (lg(p3, q3), lg(p3, N3)), 'Cho \\(%s=a\\). Khi đó \\(%s=\\)…' % (lg(p3, q3), lg(p3, N3)), '\\(%d+%da\\)' % (i3, j3),
            ['\\(%d+%da\\)' % (j3, i3), '\\(%da\\)' % (i3 * j3), '\\(%d\\cdot%da\\)' % (i3, j3)], '\\(%d=%d^{%d}\\cdot%d^{%d}\\).' % (N3, p3, i3, q3, j3), '\\(%d=%d^{%d}\\cdot%d^{%d}\\).' % (N3, p3, i3, q3, j3))
    (e4, v4_), (e5, v5_) = P['tf']
    t4 = tf(4, e4[0], e4[1], v4_, e4[2], e4[3]); t5 = tf(5, e5[0], e5[1], v5_, e5[2], e5[3])
    b6, M6, N6 = P['q']; v6 = round(math.log(M6 // N6, b6)); assert b6 ** v6 * N6 == M6
    s6 = sh(6, 'Compute \\(%s-%s\\).' % (lg(b6, M6), lg(b6, N6)), 'Tính \\(%s-%s\\).' % (lg(b6, M6), lg(b6, N6)), v6, '\\(\\log_{%d}%d=%d\\).' % (b6, M6 // N6, v6), '\\(\\log_{%d}\\dfrac{%d}{%d}=\\log_{%d}%d=%d\\).' % (b6, M6, N6, b6, M6 // N6, v6))
    L1, L2 = P['db']; k7 = (L2 - L1) // 10
    s7 = sh(7, 'Sound levels \\(L=10\\log\\frac{I}{I_0}\\): %d dB and %d dB. How many times more intense is the louder sound?' % (L1, L2), 'Hai âm có mức cường độ \\(L=10\\log\\frac{I}{I_0}\\) là %d dB và %d dB. Âm lớn hơn có cường độ gấp bao nhiêu lần?' % (L1, L2), 10 ** k7,
            '\\(\\frac{I_2}{I_1}=10^{(%d-%d)/10}=10^{%d}\\).' % (L2, L1, k7), '\\(\\frac{I_2}{I_1}=10^{(%d-%d)/10}=10^{%d}\\).' % (L2, L1, k7))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
TA = (('\\(\\log_2(4+4)=\\log_2 4+\\log_2 4\\).', '\\(\\log_2(4+4)=\\log_2 4+\\log_2 4\\).', 'Left: \\(\\log_2 8=3\\); right: \\(4\\).', 'Vế trái \\(\\log_2 8=3\\); vế phải \\(4\\).'), False)
TB = (('\\(\\log_4 8=\\dfrac32\\).', '\\(\\log_4 8=\\dfrac32\\).', '\\(4^{3/2}=8\\).', '\\(4^{3/2}=8\\).'), True)
TC = (('\\(\\log_3 x^2=2\\log_3 x\\) for every \\(x\\ne0\\).', '\\(\\log_3 x^2=2\\log_3 x\\) với mọi \\(x\\ne0\\).', 'Only for \\(x\\gt0\\); in general \\(2\\log_3|x|\\).', 'Chỉ đúng khi \\(x\\gt0\\); tổng quát là \\(2\\log_3|x|\\).'), False)
TD = (('\\(\\ln e^5=5\\).', '\\(\\ln e^5=5\\).', '\\(\\log_a a^{\\alpha}=\\alpha\\).', '\\(\\log_a a^{\\alpha}=\\alpha\\).'), True)
TE = (('\\(5^{\\log_5 7}=7\\).', '\\(5^{\\log_5 7}=7\\).', '\\(a^{\\log_a b}=b\\).', '\\(a^{\\log_a b}=b\\).'), True)
TF_ = (('\\(\\log_{\\frac12}8=3\\).', '\\(\\log_{\\frac12}8=3\\).', '\\(\\left(\\frac12\\right)^{-3}=8\\), so it is \\(-3\\).', '\\(\\left(\\frac12\\right)^{-3}=8\\) nên bằng \\(-3\\).'), False)
PP = [dict(val=(2, 5), sum=(6, 4, 9), expr=(2, 3, 1, 2), tf=(TA, TB), q=(2, 96, 3), db=(40, 70)),
      dict(val=(3, -3), sum=(10, 25, 40), expr=(3, 2, 2, 1), tf=(TC, TD), q=(3, 162, 2), db=(50, 80)),
      dict(val=(5, 3), sum=(2, 8, 16), expr=(2, 5, 3, 2), tf=(TE, TF_), q=(5, 375, 3), db=(20, 50))]
practice = three(lvl, PP)
import sp_g11r as RR, sp_g11r2 as R2
# Hiệu chỉnh 13/11/2026: phần D cũ lặp lại các dạng của A–C → 8 dạng mới.
practice = RR.with_d(practice, R2.D19, seeds=(1191, 1192, 1193))
mistakes = [('<b>\\(\\log_a(M+N)=\\log_a M+\\log_a N\\).</b> False – the sum rule is for products.', '<b>\\(\\log_a(M+N)=\\log_a M+\\log_a N\\).</b> Sai – quy tắc tổng chỉ dùng cho tích.'),
            ('<b>\\(\\dfrac{\\log_a M}{\\log_a N}=\\log_a\\dfrac MN\\).</b> False; \\(\\dfrac{\\log_a M}{\\log_a N}=\\log_N M\\).', '<b>\\(\\dfrac{\\log_a M}{\\log_a N}=\\log_a\\dfrac MN\\).</b> Sai; \\(\\dfrac{\\log_a M}{\\log_a N}=\\log_N M\\).'),
            ('<b>Ignoring the conditions.</b> \\(\\log_a b\\) needs \\(a\\gt0\\), \\(a\\ne1\\), \\(b\\gt0\\): \\(\\log_2(-4)\\) is meaningless.', '<b>Quên điều kiện.</b> \\(\\log_a b\\) cần \\(a\\gt0\\), \\(a\\ne1\\), \\(b\\gt0\\): \\(\\log_2(-4)\\) không có nghĩa.'),
            ('<b>Thinking 90 dB is 1.5 times 60 dB in intensity.</b> Each +10 dB multiplies the intensity by 10.', '<b>Nghĩ 90 dB có cường độ gấp 1,5 lần 60 dB.</b> Mỗi +10 dB là cường độ gấp 10 lần.')]
summary = [('\\(\\log_a b=\\alpha\\iff a^{\\alpha}=b\\) (\\(a\\gt0\\), \\(a\\ne1\\), \\(b\\gt0\\)); \\(\\log_a1=0\\), \\(\\log_a a=1\\), \\(a^{\\log_a b}=b\\).', '\\(\\log_a b=\\alpha\\iff a^{\\alpha}=b\\) (\\(a\\gt0\\), \\(a\\ne1\\), \\(b\\gt0\\)); \\(\\log_a1=0\\), \\(\\log_a a=1\\), \\(a^{\\log_a b}=b\\).'),
           ('\\(\\log_a(MN)=\\log_a M+\\log_a N\\), \\(\\log_a\\frac MN=\\log_a M-\\log_a N\\), \\(\\log_a M^{\\alpha}=\\alpha\\log_a M\\).', '\\(\\log_a(MN)=\\log_a M+\\log_a N\\), \\(\\log_a\\frac MN=\\log_a M-\\log_a N\\), \\(\\log_a M^{\\alpha}=\\alpha\\log_a M\\).'),
           ('\\(\\log_a b=\\dfrac{\\log_c b}{\\log_c a}\\); \\(\\log\\) = base 10, \\(\\ln\\) = base \\(e\\).', '\\(\\log_a b=\\dfrac{\\log_c b}{\\log_c a}\\); \\(\\log\\) là cơ số 10, \\(\\ln\\) là cơ số \\(e\\).'),
           ('Key words: logarithm, base, common logarithm, natural logarithm, change of base.', 'Từ cần nhớ (chạm vào để xem tiếng Anh): <b class="mbl-term" tabindex="0" data-en="logarithm">lôgarit</b>, <b class="mbl-term" tabindex="0" data-en="base">cơ số</b>, <b class="mbl-term" tabindex="0" data-en="common logarithm">lôgarit thập phân</b>, <b class="mbl-term" tabindex="0" data-en="natural logarithm">lôgarit tự nhiên</b>, <b class="mbl-term" tabindex="0" data-en="change of base">đổi cơ số</b>.')]
checks = [('I can compute simple logarithms.', 'Em tính được các lôgarit đơn giản.'), ('I can use the product, quotient and power rules.', 'Em dùng được quy tắc tích, thương, lũy thừa.'),
          ('I can change the base of a logarithm.', 'Em đổi được cơ số của lôgarit.'), ('I can use logarithmic scales (pH, dB, Richter).', 'Em vận dụng được các thang đo lôgarit (pH, dB, Richter).')]
LL('g11-exp-04', 'Logarithms', CV, ('Exponential and Logarithmic Functions', 'Hàm số mũ và hàm số lôgarit'), 'exponential-functions', 'logarithms', 200, 'Intermediate', 70, ('powers with real exponents', 'lũy thừa với số mũ thực'),
   'Definition of the logarithm, rules, change of base, common and natural logarithms, logarithmic scales.', 'Bài 19 – Định nghĩa lôgarit, tính chất, đổi cơ số, lôgarit thập phân và tự nhiên, các thang đo lôgarit.',
   ['logarithm', 'base', 'change of base', 'natural logarithm'], ['lôgarit', 'cơ số', 'đổi cơ số', 'lôgarit tự nhiên'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g11-exp-03'])
