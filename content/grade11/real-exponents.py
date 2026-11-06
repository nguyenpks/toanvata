# -*- coding: utf-8 -*-
"""g11-exp-03 = Toán 11 KNTT, Bài 18: Lũy thừa với số mũ thực. Mã ngân hàng câu hỏi: TOAN11-C6-B18.
(Bài cũ g11-exp-02 – Hàm số mũ và phương trình mũ – vẫn mở, học sau bài này.)"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g11f as S
from sp_g11f import ex, xp

CV = 'Lũy thừa với số mũ thực'
vocab = defs(CV, [
 ('nroot', 'n-th root', 'căn bậc n', '\\(b\\) is an n-th root of \\(a\\) when \\(b^n=a\\); for \\(a\\gt0\\), \\(\\sqrt[n]{a}\\) denotes the positive one.', '\\(b\\) là căn bậc \\(n\\) của \\(a\\) nếu \\(b^n=a\\); với \\(a\\gt0\\), \\(\\sqrt[n]{a}\\) là căn dương.', 'The cube root of 8 is 2.', '\\(\\sqrt[n]{a}\\)'),
 ('ratexp', 'rational exponent', 'số mũ hữu tỉ', 'for \\(a\\gt0\\) and \\(r=\\frac mn\\) (\\(n\\ge2\\)): \\(a^{\\frac mn}=\\sqrt[n]{a^m}\\).', 'với \\(a\\gt0\\), \\(r=\\frac mn\\) (\\(n\\ge2\\)): \\(a^{\\frac mn}=\\sqrt[n]{a^m}\\).', 'Eight to the power two thirds equals four.', '\\(a^{\\frac mn}\\)'),
 ('realexp', 'real exponent', 'số mũ thực', 'for \\(a\\gt0\\) and real \\(\\alpha=\\lim r_n\\) (\\(r_n\\) rational): \\(a^{\\alpha}=\\lim a^{r_n}\\).', 'với \\(a\\gt0\\), \\(\\alpha=\\lim r_n\\) (\\(r_n\\) hữu tỉ): \\(a^{\\alpha}=\\lim a^{r_n}\\).', 'Three to the power root two is about 4.73.', '\\(a^{\\alpha}\\)'),
 ('halflife', 'half-life', 'chu kì bán rã', 'the time after which half of a radioactive substance remains: \\(m(t)=m_0\\left(\\frac12\\right)^{t/T}\\).', 'khoảng thời gian để lượng chất phóng xạ còn một nửa: \\(m(t)=m_0\\left(\\frac12\\right)^{t/T}\\).', 'Carbon-14 has a half-life of 5730 years.', '\\(T\\)')])
goals = [('compute powers with integer, rational and real exponents and use n-th roots;', 'tính lũy thừa với số mũ nguyên, [[số mũ hữu tỉ]], [[số mũ thực]] và dùng [[căn bậc n]];'),
         ('use the rules of exponents to simplify expressions;', 'dùng tính chất của lũy thừa để rút gọn biểu thức;'),
         ('compare two powers with the same base;', 'so sánh hai lũy thừa cùng cơ số;'),
         ('solve problems on compound interest and radioactive decay.', 'giải bài toán lãi kép và phân rã phóng xạ ([[chu kì bán rã]]).')]
phrases = [('<b>Eight to the power two thirds equals four.</b>', '\\(8^{\\frac23}=4\\).'), ('<b>The cube root of twenty-seven is three.</b>', 'Căn bậc ba của 27 bằng 3.'), ('<b>When we multiply, we add the exponents.</b>', 'Khi nhân, ta cộng các số mũ.'),
           ('<b>The base is greater than one.</b>', 'Cơ số lớn hơn 1.'), ('<b>After two half-lives a quarter remains.</b>', 'Sau hai chu kì bán rã còn lại một phần tư.')]
review = T('Grade 10 and earlier: \\(a^n=a\\cdot a\\cdots a\\) (\\(n\\) factors), \\(a^0=1\\), \\(a^{-n}=\\dfrac1{a^n}\\) (\\(a\\ne0\\)); \\(a^m a^n=a^{m+n}\\), \\((a^m)^n=a^{mn}\\). Bài 15: \\(\\lim\\) of a sequence. Compound interest \\(A=P(1+r)^n\\) (Bài 7, geometric progressions).',
           'Đã học: \\(a^n=a\\cdot a\\cdots a\\) (\\(n\\) thừa số), \\(a^0=1\\), \\(a^{-n}=\\dfrac1{a^n}\\) (\\(a\\ne0\\)); \\(a^m a^n=a^{m+n}\\), \\((a^m)^n=a^{mn}\\). Bài 15: giới hạn của dãy số. Lãi kép \\(A=P(1+r)^n\\) (Bài 7, cấp số nhân).')
theory = '<h3>18.1 %s</h3>' % TI('Integer exponents and n-th roots', 'Lũy thừa với số mũ nguyên. Căn bậc n')
theory += BOX('blue', ('Definitions', 'Định nghĩa'), UL([T('For \\(a\\ne0\\), \\(n\\in\\mathbb N^*\\): \\(a^0=1\\), \\(a^{-n}=\\dfrac1{a^n}\\). (\\(0^0\\) and \\(0^{-n}\\) are meaningless.)', 'Với \\(a\\ne0\\), \\(n\\in\\mathbb N^*\\): \\(a^0=1\\), \\(a^{-n}=\\dfrac1{a^n}\\). (\\(0^0\\), \\(0^{-n}\\) không có nghĩa.)'),
  T('\\(b\\) is an n-th root of \\(a\\) if \\(b^n=a\\). \\(n\\) odd: exactly one root \\(\\sqrt[n]{a}\\). \\(n\\) even: \\(a\\lt0\\) – none; \\(a=0\\) – one (0); \\(a\\gt0\\) – two opposite roots \\(\\pm\\sqrt[n]{a}\\).', '\\(b\\) là căn bậc \\(n\\) của \\(a\\) nếu \\(b^n=a\\). \\(n\\) lẻ: có đúng một căn \\(\\sqrt[n]{a}\\). \\(n\\) chẵn: \\(a\\lt0\\) – không có; \\(a=0\\) – một căn là 0; \\(a\\gt0\\) – hai căn đối nhau \\(\\pm\\sqrt[n]{a}\\).')]))
theory += BOX('mint', ('Rules for roots (when defined)', 'Tính chất của căn bậc n (khi các biểu thức có nghĩa)'), T('\\(\\sqrt[n]{a}\\sqrt[n]{b}=\\sqrt[n]{ab}\\); \\(\\dfrac{\\sqrt[n]{a}}{\\sqrt[n]{b}}=\\sqrt[n]{\\dfrac ab}\\); \\((\\sqrt[n]{a})^m=\\sqrt[n]{a^m}\\); \\(\\sqrt[n]{\\sqrt[k]{a}}=\\sqrt[nk]{a}\\); \\(\\sqrt[n]{a^n}=a\\) if \\(n\\) odd, \\(=|a|\\) if \\(n\\) even.',
  '\\(\\sqrt[n]{a}\\sqrt[n]{b}=\\sqrt[n]{ab}\\); \\(\\dfrac{\\sqrt[n]{a}}{\\sqrt[n]{b}}=\\sqrt[n]{\\dfrac ab}\\); \\((\\sqrt[n]{a})^m=\\sqrt[n]{a^m}\\); \\(\\sqrt[n]{\\sqrt[k]{a}}=\\sqrt[nk]{a}\\); \\(\\sqrt[n]{a^n}=a\\) nếu \\(n\\) lẻ, \\(=|a|\\) nếu \\(n\\) chẵn.'))
theory += '<h3>18.2 %s</h3>' % TI('Rational and real exponents', 'Lũy thừa với số mũ hữu tỉ và số mũ thực')
theory += BOX('blue', ('Definitions (base \\(a\\gt0\\))', 'Định nghĩa (cơ số \\(a\\gt0\\))'), UL([T('\\(r=\\dfrac mn\\) (\\(m\\in\\mathbb Z\\), \\(n\\in\\mathbb N\\), \\(n\\ge2\\)): \\(a^{r}=a^{\\frac mn}=\\sqrt[n]{a^m}\\). Example: \\(8^{\\frac23}=\\sqrt[3]{64}=4\\).', '\\(r=\\dfrac mn\\) (\\(m\\in\\mathbb Z\\), \\(n\\in\\mathbb N\\), \\(n\\ge2\\)): \\(a^{r}=a^{\\frac mn}=\\sqrt[n]{a^m}\\). Ví dụ: \\(8^{\\frac23}=\\sqrt[3]{64}=4\\).'),
  T('\\(\\alpha\\) real, \\((r_n)\\) rational with \\(\\lim r_n=\\alpha\\): \\(a^{\\alpha}=\\lim a^{r_n}\\).', '\\(\\alpha\\) là số thực, \\((r_n)\\) là dãy số hữu tỉ có \\(\\lim r_n=\\alpha\\): \\(a^{\\alpha}=\\lim a^{r_n}\\).')]))
vals = [(r, 3 ** r) for r in (1.4, 1.41, 1.414, 1.4142)]
assert abs(3 ** math.sqrt(2) - 4.7288) < 1e-4
theory += TBL([TI('\\(r_n\\)', '\\(r_n\\)')] + ['\\(%s\\)' % ('%g' % r).replace('.', '{,}') for r, _ in vals] + ['\\(\\sqrt2\\)'],
              [[TI('\\(3^{r_n}\\)', '\\(3^{r_n}\\)')] + ['\\(%s\\)' % ('%.4f' % v).replace('.', '{,}') for _, v in vals] + ['\\(\\approx4{,}7288\\)']])
theory += T('<i>The rational numbers \\(r_n\\) get closer to \\(\\sqrt2\\), and \\(3^{r_n}\\) get closer to \\(3^{\\sqrt2}\\approx4{,}7288\\).</i>', '<i>Các số hữu tỉ \\(r_n\\) dần tới \\(\\sqrt2\\) thì \\(3^{r_n}\\) dần tới \\(3^{\\sqrt2}\\approx4{,}7288\\).</i>')
theory += '<h3>18.3 %s</h3>' % TI('Rules of exponents and comparison', 'Tính chất của lũy thừa và so sánh')
theory += BOX('mint', ('For \\(a,b\\gt0\\) and real \\(\\alpha,\\beta\\)', 'Với \\(a,b\\gt0\\) và \\(\\alpha,\\beta\\) thực'), T('\\(a^{\\alpha}a^{\\beta}=a^{\\alpha+\\beta}\\); \\(\\dfrac{a^{\\alpha}}{a^{\\beta}}=a^{\\alpha-\\beta}\\); \\((a^{\\alpha})^{\\beta}=a^{\\alpha\\beta}\\); \\((ab)^{\\alpha}=a^{\\alpha}b^{\\alpha}\\); \\(\\left(\\dfrac ab\\right)^{\\alpha}=\\dfrac{a^{\\alpha}}{b^{\\alpha}}\\).',
  '\\(a^{\\alpha}a^{\\beta}=a^{\\alpha+\\beta}\\); \\(\\dfrac{a^{\\alpha}}{a^{\\beta}}=a^{\\alpha-\\beta}\\); \\((a^{\\alpha})^{\\beta}=a^{\\alpha\\beta}\\); \\((ab)^{\\alpha}=a^{\\alpha}b^{\\alpha}\\); \\(\\left(\\dfrac ab\\right)^{\\alpha}=\\dfrac{a^{\\alpha}}{b^{\\alpha}}\\).'))
theory += BOX('blue', ('Comparing powers with the same base', 'So sánh hai lũy thừa cùng cơ số'), UL([T('\\(a\\gt1\\): \\(a^{\\alpha}\\gt a^{\\beta}\\iff\\alpha\\gt\\beta\\) (bigger exponent, bigger power).', '\\(a\\gt1\\): \\(a^{\\alpha}\\gt a^{\\beta}\\iff\\alpha\\gt\\beta\\) (số mũ lớn hơn thì lũy thừa lớn hơn).'),
  T('\\(0\\lt a\\lt1\\): \\(a^{\\alpha}\\gt a^{\\beta}\\iff\\alpha\\lt\\beta\\) (the order is reversed).', '\\(0\\lt a\\lt1\\): \\(a^{\\alpha}\\gt a^{\\beta}\\iff\\alpha\\lt\\beta\\) (đổi chiều).')]))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('Non-integer exponents need a <b>positive</b> base: \\((-8)^{\\frac13}\\) is not defined, although \\(\\sqrt[3]{-8}=-2\\). Also \\((a^m)^n\\ne a^{m+n}\\) and \\(a^m+a^n\\ne a^{m+n}\\).', 'Số mũ không nguyên cần cơ số <b>dương</b>: \\((-8)^{\\frac13}\\) không có nghĩa, dù \\(\\sqrt[3]{-8}=-2\\). Chú ý \\((a^m)^n\\ne a^{m+n}\\) và \\(a^m+a^n\\ne a^{m+n}\\).'))

assert 8 ** 2 == 64 and 4 ** 3 == 64 and F(1, 8) == F(1, 2 ** 3) and 3 * F(1, 3) == 1
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Computing powers', 'Tính giá trị'), T('Compute \\(A=8^{\\frac23}\\), \\(B=16^{-\\frac34}\\), \\(C=27^{\\frac13}\\cdot81^{-\\frac14}\\).', 'Tính \\(A=8^{\\frac23}\\), \\(B=16^{-\\frac34}\\), \\(C=27^{\\frac13}\\cdot81^{-\\frac14}\\).'),
  T('Write each base as a power of a prime.', 'Viết mỗi cơ số thành lũy thừa của số nguyên tố.'),
  [T('\\(A=(2^3)^{\\frac23}=2^2=4\\).', '\\(A=(2^3)^{\\frac23}=2^2=4\\).'), T('\\(B=(2^4)^{-\\frac34}=2^{-3}=\\dfrac18\\).', '\\(B=(2^4)^{-\\frac34}=2^{-3}=\\dfrac18\\).'), T('\\(C=(3^3)^{\\frac13}\\cdot(3^4)^{-\\frac14}=3\\cdot3^{-1}=1\\).', '\\(C=(3^3)^{\\frac13}\\cdot(3^4)^{-\\frac14}=3\\cdot3^{-1}=1\\).')],
  T('\\(A=4\\), \\(B=\\dfrac18\\), \\(C=1\\).', '\\(A=4\\), \\(B=\\dfrac18\\), \\(C=1\\).'))
assert (math.sqrt(2) + 1) + (2 - math.sqrt(2)) - (math.sqrt(3) - 1) * (math.sqrt(3) + 1) - 1 < 1e-12
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Simplifying', 'Rút gọn'), T('For \\(a\\gt0\\), simplify \\(P=\\dfrac{a^{\\sqrt2+1}\\cdot a^{2-\\sqrt2}}{\\left(a^{\\sqrt3-1}\\right)^{\\sqrt3+1}}\\).', 'Với \\(a\\gt0\\), rút gọn \\(P=\\dfrac{a^{\\sqrt2+1}\\cdot a^{2-\\sqrt2}}{\\left(a^{\\sqrt3-1}\\right)^{\\sqrt3+1}}\\).'),
  T('Add exponents in the numerator; multiply exponents in the denominator.', 'Tử: cộng số mũ; mẫu: nhân số mũ.'),
  [T('Numerator: \\(a^{(\\sqrt2+1)+(2-\\sqrt2)}=a^3\\).', 'Tử: \\(a^{(\\sqrt2+1)+(2-\\sqrt2)}=a^3\\).'), T('Denominator: \\(a^{(\\sqrt3-1)(\\sqrt3+1)}=a^{3-1}=a^2\\).', 'Mẫu: \\(a^{(\\sqrt3-1)(\\sqrt3+1)}=a^{3-1}=a^2\\).')], T('\\(P=\\dfrac{a^3}{a^2}=a\\).', '\\(P=\\dfrac{a^3}{a^2}=a\\).'))
assert F(1, 3) + F(1, 2) == F(5, 6) and (1 + F(1, 2)) / 3 == F(1, 2)
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Roots as powers', 'Viết căn thức dưới dạng lũy thừa'), T('For \\(x\\gt0\\), write as a power of \\(x\\): \\(Q=x^{\\frac13}\\sqrt{x}\\) and \\(R=\\sqrt[3]{x\\sqrt x}\\).', 'Với \\(x\\gt0\\), viết dưới dạng lũy thừa của \\(x\\): \\(Q=x^{\\frac13}\\sqrt{x}\\) và \\(R=\\sqrt[3]{x\\sqrt x}\\).'),
  T('\\(\\sqrt[n]{x^m}=x^{\\frac mn}\\).', '\\(\\sqrt[n]{x^m}=x^{\\frac mn}\\).'),
  [T('\\(Q=x^{\\frac13}x^{\\frac12}=x^{\\frac13+\\frac12}=x^{\\frac56}\\).', '\\(Q=x^{\\frac13}x^{\\frac12}=x^{\\frac13+\\frac12}=x^{\\frac56}\\).'), T('\\(x\\sqrt x=x^{\\frac32}\\), so \\(R=\\left(x^{\\frac32}\\right)^{\\frac13}=x^{\\frac12}\\).', '\\(x\\sqrt x=x^{\\frac32}\\) nên \\(R=\\left(x^{\\frac32}\\right)^{\\frac13}=x^{\\frac12}\\).')],
  T('\\(Q=x^{\\frac56}\\), \\(R=x^{\\frac12}=\\sqrt x\\).', '\\(Q=x^{\\frac56}\\), \\(R=x^{\\frac12}=\\sqrt x\\).'))
assert math.sqrt(3) > 1.7 and math.sqrt(5) > 2.2 and 0.7 ** math.sqrt(3) < 0.7 ** 1.7 and 2 ** math.sqrt(5) > 4 ** 1.1
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Comparing', 'So sánh'), T('Compare: a) \\(0{,}7^{\\sqrt3}\\) and \\(0{,}7^{1{,}7}\\); b) \\(2^{\\sqrt5}\\) and \\(4^{1{,}1}\\).', 'So sánh: a) \\(0{,}7^{\\sqrt3}\\) và \\(0{,}7^{1{,}7}\\); b) \\(2^{\\sqrt5}\\) và \\(4^{1{,}1}\\).'),
  T('Bring to the same base, then compare the exponents.', 'Đưa về cùng cơ số rồi so sánh số mũ.'),
  [T('a) \\(\\sqrt3\\approx1{,}732\\gt1{,}7\\) and \\(0\\lt0{,}7\\lt1\\): the order reverses, \\(0{,}7^{\\sqrt3}\\lt0{,}7^{1{,}7}\\).', 'a) \\(\\sqrt3\\approx1{,}732\\gt1{,}7\\) và \\(0\\lt0{,}7\\lt1\\): đổi chiều, \\(0{,}7^{\\sqrt3}\\lt0{,}7^{1{,}7}\\).'),
   T('b) \\(4^{1{,}1}=2^{2{,}2}\\); \\(\\sqrt5\\approx2{,}236\\gt2{,}2\\) and \\(2\\gt1\\): \\(2^{\\sqrt5}\\gt4^{1{,}1}\\).', 'b) \\(4^{1{,}1}=2^{2{,}2}\\); \\(\\sqrt5\\approx2{,}236\\gt2{,}2\\) và \\(2\\gt1\\): \\(2^{\\sqrt5}\\gt4^{1{,}1}\\).')],
  T('a) \\(0{,}7^{\\sqrt3}\\lt0{,}7^{1{,}7}\\); b) \\(2^{\\sqrt5}\\gt4^{1{,}1}\\).', 'a) \\(0{,}7^{\\sqrt3}\\lt0{,}7^{1{,}7}\\); b) \\(2^{\\sqrt5}\\gt4^{1{,}1}\\).'))
assert F(100) * F(106, 100) ** 3 == F(1191016, 10000) and abs(0.5 ** 0.5 - 0.7071) < 1e-4
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Savings and carbon dating', 'Tiết kiệm và định tuổi bằng carbon'), T('a) 100 million VND is saved at 6%/year compound interest. How much is there after 3 years? b) Carbon-14 has a half-life of 5730 years: \\(m(t)=m_0\\left(\\frac12\\right)^{\\frac t{5730}}\\). What percentage remains after 2865 years?', 'a) Gửi 100 triệu đồng, lãi kép 6%/năm. Sau 3 năm có bao nhiêu tiền? b) Carbon-14 có chu kì bán rã 5730 năm: \\(m(t)=m_0\\left(\\frac12\\right)^{\\frac t{5730}}\\). Sau 2865 năm còn lại bao nhiêu phần trăm?'),
  T('a) \\(A=P(1+r)^n\\). b) The exponent is \\(\\frac{2865}{5730}\\).', 'a) \\(A=P(1+r)^n\\). b) Số mũ là \\(\\frac{2865}{5730}\\).'),
  [T('a) \\(A=100\\cdot1{,}06^3=119{,}1016\\) (million VND).', 'a) \\(A=100\\cdot1{,}06^3=119{,}1016\\) (triệu đồng).'), T('b) \\(\\frac{2865}{5730}=\\frac12\\): \\(\\dfrac{m}{m_0}=\\left(\\frac12\\right)^{\\frac12}=\\dfrac{1}{\\sqrt2}\\approx0{,}7071\\).', 'b) \\(\\frac{2865}{5730}=\\frac12\\): \\(\\dfrac{m}{m_0}=\\left(\\frac12\\right)^{\\frac12}=\\dfrac{1}{\\sqrt2}\\approx0{,}7071\\).')],
  T('a) About 119.1 million VND. b) About 70.71% remains – not 75%: decay is not linear.', 'a) Khoảng 119,1 triệu đồng. b) Còn khoảng 70,71% – không phải 75%: phân rã không tuyến tính.'))

def lvl(P):
    N, b, k, m, n = P['val']; v = F(b) ** (k * m // n); assert k * m % n == 0 and F(N) == F(b) ** k
    o1 = M4(1, '\\(%d^{%s}=\\)…' % (N, ex(F(m, n))), '\\(%d^{%s}=\\)…' % (N, ex(F(m, n))), '\\(%s\\)' % fr(v), ['\\(%s\\)' % fr(1 / v), '\\(%s\\)' % fr(-v), '\\(%s\\)' % fr(F(N * m, n)), '\\(%s\\)' % fr(v + 1)],
            '\\(%d^{%s}=%d^{%d\\cdot%s}=%s\\).' % (N, ex(F(m, n)), b, k, ex(F(m, n)), fr(v)), '\\(%d^{%s}=%d^{%d\\cdot%s}=%s\\).' % (N, ex(F(m, n)), b, k, ex(F(m, n)), fr(v)))
    p, q, s = (F(t) for t in P['rule']); t2 = p * q - s
    o2 = M4(2, 'For \\(a\\gt0\\): \\(\\dfrac{\\left(a^{%s}\\right)^{%s}}{a^{%s}}=\\)…' % (ex(p), ex(q), ex(s)), 'Với \\(a\\gt0\\): \\(\\dfrac{\\left(a^{%s}\\right)^{%s}}{a^{%s}}=\\)…' % (ex(p), ex(q), ex(s)),
            '\\(%s\\)' % xp('a', t2), ['\\(%s\\)' % xp('a', p + q - s), '\\(%s\\)' % xp('a', p * q * s), '\\(%s\\)' % xp('a', p * q + s), '\\(%s\\)' % xp('a', p * q / s)],
            '\\(%s\\cdot%s-%s=%s\\).' % (ex(p), ex(q), ex(s), ex(t2)), '\\(%s\\cdot%s-%s=%s\\).' % (ex(p), ex(q), ex(s), ex(t2)))
    a3, x3, y3, gt = P['cmp']
    rel = lambda g: '\\(%s^{%s}%s%s^{%s}\\)' % (a3, x3, '\\gt' if g else '\\lt', a3, y3)
    cq = '\\(%s^{%s}\\) và \\(%s^{%s}\\)' % (a3, x3, a3, y3)
    o3 = M4(3, 'Compare ' + cq.replace(' và ', ' and ') + '.', 'So sánh ' + cq + '.', rel(gt), [rel(not gt), '\\(%s^{%s}=%s^{%s}\\)' % (a3, x3, a3, y3), '\\(%s^{%s}\\lt0\\)' % (a3, x3)],
            'Compare the exponents \\(%s\\) and \\(%s\\), then look at the base \\(%s\\).' % (x3, y3, a3), 'So sánh số mũ \\(%s\\) và \\(%s\\), rồi xét cơ số \\(%s\\).' % (x3, y3, a3))
    (e4, v4_), (e5, v5_) = P['tf']
    t4 = tf(4, e4[0], e4[1], v4_, e4[2], e4[3])
    t5 = tf(5, e5[0], e5[1], v5_, e5[2], e5[3])
    A, e1, B, e2, key6 = P['sum']
    s6 = sh(6, 'Compute \\(%d^{%s}+%d^{%s}\\).' % (A, ex(e1), B, ex(e2)), 'Tính \\(%d^{%s}+%d^{%s}\\).' % (A, ex(e1), B, ex(e2)), key6,
            'Write each base as a power of a prime; the sum is \\(%d\\).' % key6, 'Viết mỗi cơ số thành lũy thừa của số nguyên tố; tổng bằng \\(%d\\).' % key6)
    m0, T7, t7 = P['half']; k7 = t7 // T7; r7 = F(m0, 2 ** k7); assert r7.denominator == 1 and t7 % T7 == 0
    s7 = sh(7, 'A substance has a half-life of \\(%d\\) days. Starting with \\(%d\\) g, how many grams remain after \\(%d\\) days?' % (T7, m0, t7), 'Một chất có chu kì bán rã \\(%d\\) ngày. Ban đầu có \\(%d\\) g, sau \\(%d\\) ngày còn lại bao nhiêu gam?' % (T7, m0, t7), r7.numerator,
            '\\(%d\\left(\\frac12\\right)^{%d}=%d\\).' % (m0, k7, r7), '\\(%d\\left(\\frac12\\right)^{%d}=%d\\).' % (m0, k7, r7))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]

TFA = [('\\((a^{m})^{n}=a^{m+n}\\) for every \\(a\\gt0\\).', '\\((a^{m})^{n}=a^{m+n}\\) với mọi \\(a\\gt0\\).', 'In general \\((a^m)^n=a^{mn}\\).', 'Đúng là \\((a^m)^n=a^{mn}\\).'), False]
TFB = [('\\(\\sqrt[4]{(-3)^4}=-3\\).', '\\(\\sqrt[4]{(-3)^4}=-3\\).', 'Even root: \\(\\sqrt[4]{a^4}=|a|=3\\).', 'Căn bậc chẵn: \\(\\sqrt[4]{a^4}=|a|=3\\).'), False]
TFC = [('\\(\\sqrt[3]{-27}=-3\\).', '\\(\\sqrt[3]{-27}=-3\\).', '\\((-3)^3=-27\\) and odd roots are unique.', '\\((-3)^3=-27\\) và căn bậc lẻ là duy nhất.'), True]
TFD = [('After 3 half-lives, \\(\\frac18\\) of the substance remains.', 'Sau 3 chu kì bán rã, còn lại \\(\\frac18\\) lượng chất ban đầu.', '\\(\\left(\\frac12\\right)^3=\\frac18\\).', '\\(\\left(\\frac12\\right)^3=\\frac18\\).'), True]
TFE = [('\\((-8)^{\\frac13}=-2\\).', '\\((-8)^{\\frac13}=-2\\).', 'Rational exponents need a positive base: \\((-8)^{\\frac13}\\) is not defined.', 'Số mũ hữu tỉ cần cơ số dương: \\((-8)^{\\frac13}\\) không có nghĩa.'), False]
TFF = [('\\(5^{\\sqrt2}\\cdot5^{\\sqrt8}=5^{3\\sqrt2}\\).', '\\(5^{\\sqrt2}\\cdot5^{\\sqrt8}=5^{3\\sqrt2}\\).', '\\(\\sqrt2+2\\sqrt2=3\\sqrt2\\).', '\\(\\sqrt2+2\\sqrt2=3\\sqrt2\\).'), True]
assert 32 ** 0.6 + 27 ** (2 / 3) - 17 < 1e-9 and abs(16 ** 0.75 + 125 ** (1 / 3) - 13) < 1e-9 and abs(81 ** 0.25 + 64 ** (5 / 6) - 35) < 1e-9
PP = [dict(val=(8, 2, 3, 2, 3), rule=(F(1, 2), 4, 1), cmp=('3', '\\sqrt2', '1{,}4', True), tf=(TFA, TFC), sum=(32, F(3, 5), 27, F(2, 3), 17), half=(800, 10, 30)),
      dict(val=(16, 2, 4, -3, 4), rule=(F(2, 3), F(3, 2), F(1, 2)), cmp=('0{,}5', '\\sqrt3', '1{,}8', True), tf=(TFB, TFD), sum=(16, F(3, 4), 125, F(1, 3), 13), half=(640, 8, 32)),
      dict(val=(27, 3, 3, -2, 3), rule=(F(3, 4), 2, F(5, 2)), cmp=('\\left(\\dfrac43\\right)', '\\pi', '3{,}15', False), tf=(TFE, TFF), sum=(81, F(1, 4), 64, F(5, 6), 35), half=(1200, 5, 15))]
practice = three(lvl, PP)
practice = with_self(practice, S.M18S11, start=8)
mistakes = [('<b>\\(a^{-n}=-a^n\\).</b> A negative exponent means a reciprocal: \\(2^{-3}=\\frac18\\).', '<b>\\(a^{-n}=-a^n\\).</b> Số mũ âm là nghịch đảo: \\(2^{-3}=\\frac18\\).'),
            ('<b>\\(a^{\\frac mn}=\\sqrt[m]{a^n}\\).</b> The denominator is the root index: \\(a^{\\frac mn}=\\sqrt[n]{a^m}\\).', '<b>\\(a^{\\frac mn}=\\sqrt[m]{a^n}\\).</b> Mẫu số là chỉ số căn: \\(a^{\\frac mn}=\\sqrt[n]{a^m}\\).'),
            ('<b>Forgetting to reverse the order when \\(0\\lt a\\lt1\\).</b>', '<b>Quên đổi chiều khi \\(0\\lt a\\lt1\\).</b>'),
            ('<b>Thinking half of a half-life leaves 75%.</b> \\(\\left(\\frac12\\right)^{\\frac12}\\approx70{,}7\\%\\).', '<b>Nghĩ rằng sau nửa chu kì bán rã còn 75%.</b> Thực ra \\(\\left(\\frac12\\right)^{\\frac12}\\approx70{,}7\\%\\).')]
summary = [('\\(a^0=1\\), \\(a^{-n}=\\dfrac1{a^n}\\); \\(a^{\\frac mn}=\\sqrt[n]{a^m}\\) (\\(a\\gt0\\)); \\(a^{\\alpha}=\\lim a^{r_n}\\).', '\\(a^0=1\\), \\(a^{-n}=\\dfrac1{a^n}\\); \\(a^{\\frac mn}=\\sqrt[n]{a^m}\\) (\\(a\\gt0\\)); \\(a^{\\alpha}=\\lim a^{r_n}\\).'),
           ('Multiply: add exponents; divide: subtract; power of a power: multiply.', 'Nhân: cộng số mũ; chia: trừ số mũ; lũy thừa của lũy thừa: nhân số mũ.'),
           ('\\(a\\gt1\\): same order as the exponents; \\(0\\lt a\\lt1\\): reversed order.', '\\(a\\gt1\\): cùng chiều với số mũ; \\(0\\lt a\\lt1\\): ngược chiều.'),
           ('\\(A=P(1+r)^n\\); \\(m=m_0\\left(\\frac12\\right)^{t/T}\\). Key words: exponent, base, n-th root, half-life.', '\\(A=P(1+r)^n\\); \\(m=m_0\\left(\\frac12\\right)^{t/T}\\). Từ cần nhớ: exponent, base, n-th root, half-life.')]
checks = [('I can compute powers with rational exponents.', 'Em tính được lũy thừa với số mũ hữu tỉ.'), ('I can simplify expressions with the rules of exponents.', 'Em rút gọn được biểu thức bằng tính chất lũy thừa.'),
          ('I can compare powers with the same base.', 'Em so sánh được hai lũy thừa cùng cơ số.'), ('I can solve compound interest and half-life problems.', 'Em giải được bài toán lãi kép, chu kì bán rã.')]
LL('g11-exp-03', 'Powers with Real Exponents', CV, ('Exponential and Logarithmic Functions', 'Hàm số mũ và hàm số lôgarit'), 'exponential-functions', 'real-exponents', 190, 'Intermediate', 70, ('integer powers, square roots, limits of sequences', 'lũy thừa với số mũ nguyên, căn bậc hai, giới hạn của dãy số'),
   'Integer, rational and real exponents, n-th roots, rules of exponents, comparison, compound interest and half-life.', 'Bài 18 – Lũy thừa với số mũ nguyên, hữu tỉ, thực; căn bậc n; tính chất; so sánh; lãi kép và chu kì bán rã.',
   ['exponent', 'n-th root', 'rational exponent', 'half-life'], ['lũy thừa', 'căn bậc n', 'số mũ thực', 'chu kì bán rã'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g11-limits-05'])
