# -*- coding: utf-8 -*-
"""Nội dung bài g8-polynomials-01 = Toán 8 KNTT, Bài 1: Đơn thức – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 8 (2026), Chapter 1 – Lesson 1, tr. 7–9; Part 2 – Lesson plan (tr. 149); Part 3 – Monomials (tr. 161)."""
import os, sys
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g8
from sp_g8 import Poly, M

LID = 'g8-polynomials-01'
CH = 'Đa thức'
TOPIC = ('Polynomials', CH)
ensure_vocab([
 ('g8-monomial', 'monomial', 'đơn thức (lớp 8)', CH, 'The expression xy is a two-variable monomial.', ''),
 ('g8-literal-part', 'literal part', 'phần biến', CH, 'The literal part of 5x²y³ is x²y³.', ''),
 ('g8-simplified-monomial', 'simplified monomial', 'đơn thức thu gọn', CH, '5x²y³ is a simplified monomial.', ''),
 ('g8-like-monomials', 'like terms (like monomials)', 'đơn thức đồng dạng', CH, '4x² and −7x² are like terms as they have the same literal part.', ''),
 ('g8-degree-monomial', 'degree of a monomial', 'bậc của đơn thức', CH, 'The degree of the monomial 5x²y³ is 2 + 3 = 5.', ''),
 ('g8-one-var', 'one-variable', 'một biến (lớp 8)', CH, '−2x² is a one-variable monomial.', ''),
 ('g8-multi-var', 'multi-variable', 'nhiều biến (lớp 8)', CH, '3xy is a multi-variable monomial.', ''),
 ('g8-variable', 'variable', 'biến (lớp 8)', CH, 'The variables of 5x²y³ are x and y.', ''),
])
load_vocab()

# ---------- kiểm tra số liệu ----------
assert M(F(3, 4), (2, 1, 0)) * M(-8, (1, 3, 0)) == M(-6, (3, 4, 0))                                         # Ví dụ 2
A3 = Poly.of([(2, (1, 2, 0)), (-5, (1, 2, 0)), (F(1, 2), (1, 2, 0))])
assert A3 == M(F(-5, 2), (1, 2, 0)) and A3.at(2, -1) == -5                                                   # Ví dụ 4
assert M(4, (1, 0, 0)) * M(3, (1, 0, 0)) - M(1, (2, 0, 0)) == M(11, (2, 0, 0)) and 11 * 5 ** 2 == 275           # Ví dụ 5

meta = dict(level=('Beginner', 'Cơ bản'), time=('about 45 minutes', '45 phút'),
            before=('algebraic expressions; powers with natural exponents (grade 7)', 'biểu thức đại số; lũy thừa với số mũ tự nhiên (lớp 7)'))
goals = [
 (r'recognize a monomial, a simplified monomial, its coefficient, literal part and degree;', r'nhận biết được [[đơn thức|đơn thức (lớp 8)]], [[đơn thức thu gọn]], [[hệ số]], [[phần biến]] và [[bậc của đơn thức]];'),
 (r'simplify a monomial by multiplying the coefficients and adding the exponents;', r'thu gọn được đơn thức bằng cách nhân các hệ số và cộng số mũ của từng biến;'),
 (r'recognize like terms and add or subtract them;', r'nhận biết được [[đơn thức đồng dạng]] và thực hiện được phép cộng, trừ các đơn thức đồng dạng;'),
 (r'evaluate a monomial for given values of the variables.', r'tính được giá trị của đơn thức tại giá trị cho trước của các biến.')]
vocab = [
 (r'<b>monomial</b> – a number, a variable, or a product of numbers and variables: \(5\), \(x\), \(-3x^2y\).', r'[[Đơn thức|đơn thức (lớp 8)]] – một số, một biến hoặc một tích giữa các số và các biến: \(5\), \(x\), \(-3x^2y\).'),
 (r'<b>algebraic expression</b> – an expression made of numbers, variables and operations.', r'[[Biểu thức đại số]] – biểu thức gồm các số, các biến và các phép toán.'),
 (r'<b>coefficient / literal part</b> – in \(5x^2y^3\) the coefficient is \(5\), the literal part is \(x^2y^3\).', r'[[Hệ số]] / [[phần biến]] – trong \(5x^2y^3\), hệ số là \(5\), phần biến là \(x^2y^3\).'),
 (r'<b>exponent</b> – the exponent of \(x\) in \(5x^2y^3\) is \(2\).', r'[[Số mũ]] – số mũ của \(x\) trong \(5x^2y^3\) là \(2\).'),
 (r'<b>degree of a monomial</b> – the sum of the exponents of all variables: \(5x^2y^3\) has degree \(2+3=5\).', r'[[Bậc của đơn thức]] – tổng số mũ của tất cả các biến: \(5x^2y^3\) có bậc \(2+3=5\).'),
 (r'<b>like terms</b> – monomials with nonzero coefficients and the same literal part: \(4x^2\) and \(-7x^2\).', r'[[Đơn thức đồng dạng]] – các đơn thức có hệ số khác 0 và có cùng phần biến: \(4x^2\) và \(-7x^2\).'),
 (r'<b>one-variable / multi-variable</b> – \(-2x^2\) is a one-variable monomial; \(3xy\) is a multi-variable monomial.', r'[[Một biến|một biến (lớp 8)]] / [[nhiều biến|nhiều biến (lớp 8)]] – \(-2x^2\) là đơn thức một biến; \(3xy\) là đơn thức nhiều biến.')]
phrases = [
 (r'<b>Determine whether the expressions are monomials.</b>', r'Xác định các biểu thức nào là đơn thức.'),
 (r'<b>Simplify the monomial.</b>', r'Thu gọn đơn thức.'),
 (r'<b>Find the coefficient, the literal part and the degree of the monomial.</b>', r'Tìm hệ số, phần biến và bậc của đơn thức.'),
 (r'<b>Identify / combine like terms.</b>', r'Nhận biết / cộng các đơn thức đồng dạng.'),
 (r'<b>Evaluate the monomial for \(x=2,\ y=-3\).</b>', r'Tính giá trị của đơn thức tại \(x=2,\ y=-3\).'),
 (r'<b>We combine like terms by adding the coefficients and keeping the literal part.</b>', r'Cộng các đơn thức đồng dạng bằng cách cộng các hệ số và giữ nguyên phần biến.'),
 (r'<b>Is this expression a monomial? Why or why not?</b>', r'Biểu thức này có phải là đơn thức không? Vì sao?')]
review = (T(r'<b>Powers.</b> \(a^m\cdot a^n=a^{m+n}\); for example \(x^2\cdot x^3=x^5\).', r'<b>Lũy thừa.</b> \(a^m\cdot a^n=a^{m+n}\); ví dụ \(x^2\cdot x^3=x^5\).') +
          T(r'<b>Algebraic expressions (grade 7).</b> To evaluate an expression, substitute the values of the variables and calculate.', r'<b>Biểu thức đại số (lớp 7).</b> Muốn tính giá trị của biểu thức, thay giá trị của các biến vào rồi thực hiện phép tính.'))

theory = '<h3>1.1 %s</h3>' % TI('Monomials', 'Đơn thức')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'A <b>monomial</b> is an algebraic expression consisting of a number, a variable, or a product of numbers and variables.', r'[[Đơn thức|đơn thức (lớp 8)]] là biểu thức đại số chỉ gồm một số, hoặc một biến, hoặc một tích giữa các số và các biến.'),
  T(r'Monomials: \(-4\), \(y\), \(3x^3y\), \(\dfrac{7}{9}x\), \(\dfrac{xy}{2}\). Not monomials: \(2x+y\) (a sum), \(\dfrac{5}{x}\) (a variable in the denominator), \(\sqrt{x}\).', r'Là đơn thức: \(-4\), \(y\), \(3x^3y\), \(\dfrac{7}{9}x\), \(\dfrac{xy}{2}\). Không là đơn thức: \(2x+y\) (có phép cộng), \(\dfrac{5}{x}\) (có biến ở mẫu), \(\sqrt{x}\).'))
theory += BOX('mint', ('Simplified monomial', 'Đơn thức thu gọn'),
  T(r'A <b>simplified monomial</b> has one coefficient written first, and each variable appears only once (raised to a positive integer power). Example: \(5x^2y^3\) is simplified; \(2x\cdot 3xy\) is not.', r'[[Đơn thức thu gọn]] là đơn thức chỉ gồm một số (viết trước) hoặc tích của một số với các biến, mỗi biến chỉ xuất hiện một lần và đã được nâng lên lũy thừa với số mũ nguyên dương. Ví dụ: \(5x^2y^3\) là đơn thức thu gọn; \(2x\cdot 3xy\) chưa thu gọn.'),
  T(r'In a simplified monomial, the number is the <b>coefficient</b> and the product of the variables is the <b>literal part</b>.', r'Trong đơn thức thu gọn, phần số gọi là [[hệ số]], phần còn lại gọi là [[phần biến]].'),
  T(r'To simplify, <b>multiply the coefficients</b> and <b>add the exponents</b> of each variable: \(2x\cdot 3xy=6x^2y\).', r'Muốn thu gọn, ta <b>nhân các hệ số</b> với nhau và <b>cộng số mũ</b> của từng biến: \(2x\cdot 3xy=6x^2y\).'))
theory += BOX('blue', ('Degree', 'Bậc của đơn thức'),
  T(r'The <b>degree</b> of a monomial with a nonzero coefficient is the sum of the exponents of all its variables. A nonzero number has degree \(0\); the number \(0\) has no degree.', r'[[Bậc của đơn thức]] có hệ số khác 0 là tổng số mũ của tất cả các biến có trong đơn thức đó. Số thực khác 0 là đơn thức bậc 0; số 0 là đơn thức không có bậc.'),
  T(r'Example: \(-\dfrac{1}{2}x^3yz^2\) has degree \(3+1+2=6\). Careful: in \(2^3x^2\) the factor \(2^3\) belongs to the coefficient, so the degree is \(2\).', r'Ví dụ: \(-\dfrac{1}{2}x^3yz^2\) có bậc \(3+1+2=6\). Chú ý: trong \(2^3x^2\), \(2^3\) thuộc hệ số nên bậc là \(2\).'))
theory += '<h3>1.2 %s</h3>' % TI('Like terms', 'Đơn thức đồng dạng')
theory += BOX('mint', ('Like terms', 'Đơn thức đồng dạng'),
  T(r'<b>Like terms</b> are monomials with nonzero coefficients and the <b>same literal part</b>: \(4x^2y\), \(-x^2y\), \(\dfrac{2}{3}x^2y\).', r'Hai [[đơn thức đồng dạng]] là hai đơn thức có hệ số khác 0 và có <b>cùng phần biến</b>: \(4x^2y\), \(-x^2y\), \(\dfrac{2}{3}x^2y\).'),
  T(r'To add or subtract like terms, add or subtract the coefficients and keep the literal part: \(5xy^2-8xy^2=-3xy^2\).', r'Để cộng (hay trừ) các đơn thức đồng dạng, ta cộng (hay trừ) các hệ số với nhau và giữ nguyên phần biến: \(5xy^2-8xy^2=-3xy^2\).'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'),
  T(r'\(x^2y\) and \(xy^2\) are <b>not</b> like terms: the exponents of \(x\) and \(y\) are different.', r'\(x^2y\) và \(xy^2\) <b>không</b> đồng dạng vì số mũ của \(x\), của \(y\) khác nhau.'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Is it a monomial?', 'Nhận biết đơn thức'),
  T(r'Which of the following expressions are monomials? \(4x^3y;\ -7;\ 3x-y;\ \dfrac{2}{y};\ \dfrac{x^2y}{5};\ \sqrt{x}\).', r'Trong các biểu thức sau, biểu thức nào là đơn thức? \(4x^3y;\ -7;\ 3x-y;\ \dfrac{2}{y};\ \dfrac{x^2y}{5};\ \sqrt{x}\).'),
  ('Check each expression: is it a number, a variable, or a product of numbers and variables?', 'Xét từng biểu thức: có phải là một số, một biến hoặc một tích giữa các số và các biến không?'),
  [T(r'\(4x^3y\), \(-7\) and \(\dfrac{x^2y}{5}=\dfrac{1}{5}x^2y\) are monomials.', r'\(4x^3y\), \(-7\) và \(\dfrac{x^2y}{5}=\dfrac{1}{5}x^2y\) là đơn thức.'),
   T(r'\(3x-y\) contains a subtraction; \(\dfrac{2}{y}\) has a variable in the denominator; \(\sqrt{x}\) is a root of a variable.', r'\(3x-y\) có phép trừ; \(\dfrac{2}{y}\) có biến ở mẫu; \(\sqrt{x}\) là căn của biến.')],
  T(r'The monomials are \(4x^3y\), \(-7\), \(\dfrac{x^2y}{5}\).', r'Các đơn thức là \(4x^3y\), \(-7\), \(\dfrac{x^2y}{5}\).'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Simplify a monomial', 'Thu gọn đơn thức'),
  T(r'Simplify \(\dfrac{3}{4}x^2y\cdot(-8)xy^3\). Then give its coefficient, literal part and degree.', r'Thu gọn đơn thức \(\dfrac{3}{4}x^2y\cdot(-8)xy^3\) rồi chỉ ra hệ số, phần biến và bậc của nó.'),
  ('Multiply the coefficients and add the exponents of like bases.', 'Nhân các hệ số và cộng số mũ của cùng một biến.'),
  [T(r'\(\dfrac{3}{4}x^2y\cdot(-8)xy^3=\left(\dfrac{3}{4}\cdot(-8)\right)(x^2\cdot x)(y\cdot y^3)=-6x^3y^4\).', r'\(\dfrac{3}{4}x^2y\cdot(-8)xy^3=\left(\dfrac{3}{4}\cdot(-8)\right)(x^2\cdot x)(y\cdot y^3)=-6x^3y^4\).'),
   T(r'Coefficient \(-6\), literal part \(x^3y^4\), degree \(3+4=7\).', r'Hệ số \(-6\), phần biến \(x^3y^4\), bậc \(3+4=7\).')],
  T(r'\(-6x^3y^4\); coefficient \(-6\), literal part \(x^3y^4\), degree \(7\).', r'\(-6x^3y^4\); hệ số \(-6\), phần biến \(x^3y^4\), bậc \(7\).'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('Group like terms', 'Nhóm các đơn thức đồng dạng'),
  T(r'Group the like terms: \(2x^2y;\ -xy^2;\ 0.5x^2y;\ \dfrac{3}{2}xy^2;\ -4x^2y;\ 7xy\).', r'Sắp xếp các đơn thức sau thành từng nhóm đơn thức đồng dạng: \(2x^2y;\ -xy^2;\ 0{,}5x^2y;\ \dfrac{3}{2}xy^2;\ -4x^2y;\ 7xy\).'),
  ('Compare the literal parts.', 'So sánh phần biến của các đơn thức.'),
  [T(r'Literal part \(x^2y\): \(2x^2y,\ 0.5x^2y,\ -4x^2y\).', r'Phần biến \(x^2y\): \(2x^2y,\ 0{,}5x^2y,\ -4x^2y\).'),
   T(r'Literal part \(xy^2\): \(-xy^2,\ \dfrac{3}{2}xy^2\). The monomial \(7xy\) has no like term in the list.', r'Phần biến \(xy^2\): \(-xy^2,\ \dfrac{3}{2}xy^2\). Đơn thức \(7xy\) không đồng dạng với đơn thức nào khác.')],
  T(r'Two groups: \(\{2x^2y;\ 0.5x^2y;\ -4x^2y\}\) and \(\left\{-xy^2;\ \dfrac{3}{2}xy^2\right\}\).', r'Hai nhóm: \(\{2x^2y;\ 0{,}5x^2y;\ -4x^2y\}\) và \(\left\{-xy^2;\ \dfrac{3}{2}xy^2\right\}\).'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Combine, then evaluate', 'Thu gọn rồi tính giá trị'),
  T(r'Find the value of \(A=2xy^2-5xy^2+\dfrac{1}{2}xy^2\) at \(x=2,\ y=-1\).', r'Tính giá trị của biểu thức \(A=2xy^2-5xy^2+\dfrac{1}{2}xy^2\) tại \(x=2,\ y=-1\).'),
  ('The three terms are like terms: combine them first.', 'Ba đơn thức đồng dạng: nên cộng chúng trước khi thay số.'),
  [T(r'\(A=\left(2-5+\dfrac{1}{2}\right)xy^2=-\dfrac{5}{2}xy^2\).', r'\(A=\left(2-5+\dfrac{1}{2}\right)xy^2=-\dfrac{5}{2}xy^2\).'),
   T(r'Substitute: \(A=-\dfrac{5}{2}\cdot 2\cdot(-1)^2=-5\).', r'Thay số: \(A=-\dfrac{5}{2}\cdot 2\cdot(-1)^2=-5\).')],
  T(r'\(A=-5\).', r'\(A=-5\).'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('A garden with a pond', 'Mảnh vườn có ao'),
  T(r'A rectangular garden is \(4x\) m long and \(3x\) m wide. A square pond with side \(x\) m is dug in the garden. Write a monomial for the area of the remaining land, then find this area when \(x=5\).', r'Một mảnh vườn hình chữ nhật dài \(4x\) m, rộng \(3x\) m. Người ta đào một cái ao hình vuông cạnh \(x\) m trong vườn. Viết đơn thức biểu thị diện tích phần đất còn lại rồi tính diện tích đó khi \(x=5\).'),
  ('Area of the garden minus area of the pond; both are like terms.', 'Lấy diện tích vườn trừ diện tích ao; hai đơn thức này đồng dạng.'),
  [T(r'Garden: \(4x\cdot 3x=12x^2\) (m²). Pond: \(x\cdot x=x^2\) (m²).', r'Diện tích vườn: \(4x\cdot 3x=12x^2\) (m²). Diện tích ao: \(x\cdot x=x^2\) (m²).'),
   T(r'Remaining land: \(12x^2-x^2=11x^2\) (m²).', r'Diện tích còn lại: \(12x^2-x^2=11x^2\) (m²).'),
   T(r'When \(x=5\): \(11\cdot 5^2=275\) (m²).', r'Khi \(x=5\): \(11\cdot 5^2=275\) (m²).')],
  T(r'\(11x^2\) m²; \(275\) m² when \(x=5\).', r'\(11x^2\) m²; bằng \(275\) m² khi \(x=5\).'))

_SETS = sp_g8.BANK(sp_g8.L1_GROUPS, start=1, seeds=(801, 802, 803))
practice = LEVEL_PRACTICE(sp_g8.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Calling a sum a monomial.</b> \(3x+y\) is not a monomial (it has two terms).', r'<b>Coi một tổng là đơn thức.</b> \(3x+y\) không là đơn thức (có phép cộng).'),
 (r'<b>Multiplying the exponents.</b> \(x^2\cdot x^3=x^5\), not \(x^6\).', r'<b>Nhân các số mũ.</b> \(x^2\cdot x^3=x^5\), không phải \(x^6\).'),
 (r'<b>Counting the coefficient in the degree.</b> \(2^3x^2y\) has degree \(3\), not \(6\).', r'<b>Tính cả số mũ của hệ số vào bậc.</b> \(2^3x^2y\) có bậc \(3\), không phải \(6\).'),
 (r'<b>Mixing up \(x^2y\) and \(xy^2\).</b> They are not like terms and cannot be combined.', r'<b>Nhầm \(x^2y\) với \(xy^2\).</b> Hai đơn thức này không đồng dạng, không cộng được.'),
 (r'<b>Adding the literal parts.</b> \(3x^2+5x^2=8x^2\), not \(8x^4\).', r'<b>Cộng cả phần biến.</b> \(3x^2+5x^2=8x^2\), không phải \(8x^4\).')]
summary = [
 (r'A monomial is a number, a variable, or a product of numbers and variables.', r'Đơn thức là một số, một biến hoặc một tích giữa các số và các biến.'),
 (r'Simplified monomial = coefficient × literal part; degree = sum of the exponents of the variables.', r'Đơn thức thu gọn = hệ số × phần biến; bậc = tổng số mũ của các biến.'),
 (r'Like terms have the same literal part; add them by adding the coefficients.', r'Đơn thức đồng dạng có cùng phần biến; cộng chúng bằng cách cộng các hệ số.'),
 (r'Key English: monomial, coefficient, literal part, degree, like terms.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[đơn thức|đơn thức (lớp 8)]], [[hệ số]], [[phần biến]], [[bậc của đơn thức]], [[đơn thức đồng dạng]].')]
checks = [
 (r'I can tell whether an expression is a monomial.', r'Em nhận biết được một biểu thức có phải là đơn thức không.'),
 (r'I can simplify a monomial and give its coefficient, literal part and degree.', r'Em thu gọn được đơn thức và chỉ ra hệ số, phần biến, bậc.'),
 (r'I can recognize like terms and add or subtract them.', r'Em nhận biết và cộng, trừ được các đơn thức đồng dạng.'),
 (r'I can evaluate a monomial.', r'Em tính được giá trị của đơn thức.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Monomials', title_vi='Đơn thức', topic=TOPIC,
       folder='polynomials', file='monomials', catalog_title_vi='Đơn thức',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Monomials, simplified monomials, degree, like terms.', level='Beginner', minutes=45,
       description_vi='Bài 1 – Đơn thức, đơn thức thu gọn, hệ số, phần biến, bậc; đơn thức đồng dạng và cộng, trừ đơn thức đồng dạng.',
       tags_vi=['đơn thức', 'đơn thức thu gọn', 'bậc của đơn thức', 'đơn thức đồng dạng'],
       prerequisites=[], tags=['monomial', 'degree', 'like terms'], order=10)
