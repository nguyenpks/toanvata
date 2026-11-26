# -*- coding: utf-8 -*-
"""Nội dung bài g8-polynomials-02 = Toán 8 KNTT, Bài 2: Đa thức – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 8 (2026), Chapter 1 – Lesson 2, tr. 10–12 (polynomial, constant term, zero polynomial, binomial, trinomial)."""
import os, sys
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g8
from sp_g8 import Poly, M

LID = 'g8-polynomials-02'
CH = 'Đa thức'
TOPIC = ('Polynomials', CH)
ensure_vocab([
 ('g8-polynomial', 'polynomial', 'đa thức (lớp 8)', CH, 'The expression x + y is a polynomial.', ''),
 ('g8-simplified-poly', 'simplified polynomial', 'đa thức thu gọn', CH, '−xy² − 4xy is a simplified polynomial: it has no like terms.', ''),
 ('g8-degree-poly', 'degree of a polynomial', 'bậc của đa thức', CH, 'The degree of the polynomial equals the degree of the term with the highest degree.', ''),
 ('g8-constant-term', 'constant term', 'hệ số tự do (lớp 8)', CH, 'In the polynomial x² + 3x − 5, −5 is the constant term.', ''),
 ('g8-zero-poly', 'zero polynomial', 'đa thức không (lớp 8)', CH, 'The number 0 is called the zero polynomial.', ''),
 ('g8-binomial', 'binomial', 'nhị thức (lớp 8)', CH, 'The expression 3x + 2y is called a binomial.', ''),
 ('g8-trinomial', 'trinomial', 'tam thức (lớp 8)', CH, 'The expression 3x + 2y − 1 is called a trinomial.', ''),
])
load_vocab()

# ---------- kiểm tra số liệu ----------
X = lambda c, a, b: (c, (a, b, 0))
P2 = Poly.of([X(6, 2, 3), X(-3, 1, 2), X(1, 1, 1), X(-4, 2, 3), X(2, 1, 2), X(-2, 2, 3), X(-5, 1, 1)])
assert P2 == Poly.of([X(-1, 1, 2), X(-4, 1, 1)]) and P2.deg() == 3                                            # Ví dụ 2
Q3 = Poly.of([X(3, 4, 0), X(2, 2, 2), X(-3, 4, 0), X(1, 1, 1), X(-5, 0, 0)])
assert Q3.deg() == 4 and len(Q3) == 3                                                                          # Ví dụ 3
A4 = Poly.of([(4, (2, 1, 0)), (F(-1, 3), (1, 1, 0)), (3, (1, 0, 1)), (-4, (2, 1, 0)), (F(4, 3), (1, 1, 0))])
assert A4 == Poly.of([(1, (1, 1, 0)), (3, (1, 0, 1))]) and A4.at(3, -2, F(1, 3)) == -3                        # Ví dụ 4
assert 2 * (5 * 4 + 4 * 3 + 3 * 5) == 94                                                                       # Ví dụ 5

meta = dict(level=('Beginner', 'Cơ bản'), time=('about 45 minutes', '45 phút'),
            before=('monomials (Lesson 1)', 'đơn thức (Bài 1)'))
goals = [
 (r'recognize a polynomial and its terms;', r'nhận biết được [[đa thức|đa thức (lớp 8)]] và các [[hạng tử]] của nó;'),
 (r'simplify a polynomial by combining like terms;', r'thu gọn được đa thức bằng cách cộng các hạng tử đồng dạng;'),
 (r'find the degree of a polynomial;', r'tìm được [[bậc của đa thức]];'),
 (r'evaluate a polynomial for given values of the variables.', r'tính được giá trị của đa thức tại giá trị cho trước của các biến.')]
vocab = [
 (r'<b>polynomial</b> – a sum of monomials: \(3xy^2-1\), \(x^2+2xy+y^2\).', r'[[Đa thức|đa thức (lớp 8)]] – một tổng của những đơn thức: \(3xy^2-1\), \(x^2+2xy+y^2\).'),
 (r'<b>term</b> – each monomial in the sum: \(3xy^2-1\) has the terms \(3xy^2\) and \(-1\).', r'[[Hạng tử]] – mỗi đơn thức trong tổng: \(3xy^2-1\) có các hạng tử \(3xy^2\) và \(-1\).'),
 (r'<b>constant term</b> – the term without variables: \(-1\) in \(3xy^2-1\).', r'[[Hệ số tự do|hệ số tự do (lớp 8)]] – hạng tử không chứa biến: \(-1\) trong \(3xy^2-1\).'),
 (r'<b>simplified polynomial</b> – a polynomial with no like terms.', r'[[Đa thức thu gọn]] – đa thức không còn hai hạng tử nào đồng dạng.'),
 (r'<b>degree of a polynomial</b> – the degree of its term of highest degree (after simplifying).', r'[[Bậc của đa thức]] – bậc của hạng tử có bậc cao nhất trong dạng thu gọn.'),
 (r'<b>zero polynomial</b> – the number \(0\); it has no degree.', r'[[Đa thức không|đa thức không (lớp 8)]] – số \(0\); đa thức không không có bậc.'),
 (r'<b>binomial / trinomial</b> – a polynomial with two / three terms: \(3x+2y\), \(3x+2y-1\).', r'[[Nhị thức|nhị thức (lớp 8)]] / [[tam thức|tam thức (lớp 8)]] – đa thức có hai / ba hạng tử: \(3x+2y\), \(3x+2y-1\).')]
phrases = [
 (r'<b>Determine whether the expressions are polynomials.</b>', r'Xác định các biểu thức nào là đa thức.'),
 (r'<b>Specify the terms of each polynomial.</b>', r'Chỉ ra các hạng tử của mỗi đa thức.'),
 (r'<b>Simplify the polynomial and find its degree.</b>', r'Thu gọn đa thức và tìm bậc của nó.'),
 (r'<b>The degree of the polynomial equals the degree of the term with the highest degree.</b>', r'Bậc của đa thức bằng bậc của hạng tử có bậc cao nhất.'),
 (r'<b>We simplify the polynomial by combining like terms.</b>', r'Thu gọn đa thức bằng cách cộng các hạng tử đồng dạng.'),
 (r'<b>Find the value of the polynomial for \(x=2,\ y=-3\).</b>', r'Tính giá trị của đa thức tại \(x=2,\ y=-3\).')]
review = (T(r'<b>Monomials (Lesson 1).</b> The degree of \(5x^2y^3\) is \(5\); like terms such as \(4xy\) and \(-7xy\) add up to \(-3xy\).', r'<b>Đơn thức (Bài 1).</b> \(5x^2y^3\) có bậc \(5\); các đơn thức đồng dạng như \(4xy\) và \(-7xy\) có tổng \(-3xy\).'))

theory = '<h3>2.1 %s</h3>' % TI('Polynomials', 'Đa thức')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'A <b>polynomial</b> is a sum of monomials. Each monomial in the sum is a <b>term</b> of the polynomial.', r'[[Đa thức|đa thức (lớp 8)]] là một tổng của những đơn thức; mỗi đơn thức trong tổng gọi là một [[hạng tử]] của đa thức đó.'),
  T(r'Every monomial is also a polynomial (with one term). The number \(0\) is the <b>zero polynomial</b>.', r'Mỗi đơn thức cũng được coi là một đa thức (chỉ có một hạng tử). Số \(0\) cũng là một đa thức, gọi là [[đa thức không|đa thức không (lớp 8)]].'),
  T(r'Example: \(2x^2-\dfrac{1}{3}y+5\) is a polynomial with the terms \(2x^2\), \(-\dfrac{1}{3}y\), \(5\). The term \(5\) has no variable: it is the <b>constant term</b>.', r'Ví dụ: \(2x^2-\dfrac{1}{3}y+5\) là đa thức có ba hạng tử \(2x^2\), \(-\dfrac{1}{3}y\), \(5\). Hạng tử \(5\) không chứa biến, gọi là [[hệ số tự do|hệ số tự do (lớp 8)]].'),
  T(r'\(x+\dfrac{1}{x}\) and \(x+\sqrt{xy}\) are <b>not</b> polynomials: \(\dfrac{1}{x}\) and \(\sqrt{xy}\) are not monomials.', r'\(x+\dfrac{1}{x}\) và \(x+\sqrt{xy}\) <b>không</b> là đa thức vì \(\dfrac{1}{x}\) và \(\sqrt{xy}\) không phải là đơn thức.'))
theory += '<h3>2.2 %s</h3>' % TI('Simplified polynomials and degree', 'Đa thức thu gọn. Bậc của đa thức')
theory += BOX('mint', ('Simplify', 'Thu gọn đa thức'),
  T(r'A <b>simplified polynomial</b> has no like terms. To simplify, group the like terms and add them.', r'[[Đa thức thu gọn]] là đa thức không có hai hạng tử nào đồng dạng. Muốn thu gọn, ta nhóm các hạng tử đồng dạng rồi cộng chúng.'),
  T(r'Example: \(3x^2y-xy+5-x^2y+4xy=(3x^2y-x^2y)+(-xy+4xy)+5=2x^2y+3xy+5\).', r'Ví dụ: \(3x^2y-xy+5-x^2y+4xy=(3x^2y-x^2y)+(-xy+4xy)+5=2x^2y+3xy+5\).'))
theory += BOX('blue', ('Degree of a polynomial', 'Bậc của đa thức'),
  T(r'The <b>degree</b> of a polynomial is the degree of its term of highest degree <b>in the simplified form</b>.', r'[[Bậc của đa thức]] là bậc của hạng tử có bậc cao nhất trong <b>dạng thu gọn</b> của đa thức đó.'),
  T(r'Example: \(2x^2y+3xy+5\) has terms of degree \(3,\ 2,\ 0\), so its degree is \(3\). A nonzero number has degree \(0\); the zero polynomial has no degree.', r'Ví dụ: \(2x^2y+3xy+5\) có các hạng tử bậc \(3,\ 2,\ 0\) nên có bậc \(3\). Một số khác 0 là đa thức bậc 0; đa thức không không có bậc.'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'),
  T(r'Always simplify before finding the degree: in \(x^4+2xy-x^4\) the terms \(x^4\) and \(-x^4\) cancel, so the degree is \(2\), not \(4\).', r'Luôn thu gọn trước khi tìm bậc: trong \(x^4+2xy-x^4\), hai hạng tử \(x^4\) và \(-x^4\) triệt tiêu nên đa thức có bậc \(2\), không phải \(4\).'))
theory += '<h3>2.3 %s</h3>' % TI('Value of a polynomial', 'Giá trị của đa thức')
theory += BOX('mint', ('Evaluate', 'Tính giá trị'),
  T(r'Simplify the polynomial first, then substitute the values of the variables and calculate.', r'Nên thu gọn đa thức trước, sau đó thay giá trị của các biến vào và thực hiện phép tính.'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Is it a polynomial?', 'Nhận biết đa thức'),
  T(r'Which expressions are polynomials? Give the terms of each polynomial. \(3xy^2-1;\ x+\dfrac{1}{x};\ 2x^2-\dfrac{1}{3}y+5;\ x+\sqrt{xy}\).', r'Biểu thức nào là đa thức? Chỉ ra các hạng tử của mỗi đa thức. \(3xy^2-1;\ x+\dfrac{1}{x};\ 2x^2-\dfrac{1}{3}y+5;\ x+\sqrt{xy}\).'),
  ('A polynomial is a sum of monomials.', 'Đa thức là tổng của những đơn thức.'),
  [T(r'\(3xy^2-1\) is a polynomial with terms \(3xy^2\) and \(-1\).', r'\(3xy^2-1\) là đa thức có hai hạng tử \(3xy^2\) và \(-1\).'),
   T(r'\(2x^2-\dfrac{1}{3}y+5\) is a polynomial with terms \(2x^2\), \(-\dfrac{1}{3}y\) and \(5\).', r'\(2x^2-\dfrac{1}{3}y+5\) là đa thức có ba hạng tử \(2x^2\), \(-\dfrac{1}{3}y\) và \(5\).'),
   T(r'\(x+\dfrac{1}{x}\) and \(x+\sqrt{xy}\) are not polynomials.', r'\(x+\dfrac{1}{x}\) và \(x+\sqrt{xy}\) không là đa thức.')],
  T(r'Polynomials: \(3xy^2-1\) and \(2x^2-\dfrac{1}{3}y+5\).', r'Các đa thức: \(3xy^2-1\) và \(2x^2-\dfrac{1}{3}y+5\).'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Simplify, then find the degree', 'Thu gọn và tìm bậc'),
  T(r'Simplify and find the degree of \(P=6x^2y^3-3xy^2+xy-4x^2y^3+2xy^2-2x^2y^3-5xy\).', r'Thu gọn và tìm bậc của đa thức \(P=6x^2y^3-3xy^2+xy-4x^2y^3+2xy^2-2x^2y^3-5xy\).'),
  ('Group the like terms.', 'Nhóm các hạng tử đồng dạng.'),
  [T(r'\(P=(6x^2y^3-4x^2y^3-2x^2y^3)+(-3xy^2+2xy^2)+(xy-5xy)=-xy^2-4xy\).', r'\(P=(6x^2y^3-4x^2y^3-2x^2y^3)+(-3xy^2+2xy^2)+(xy-5xy)=-xy^2-4xy\).'),
   T(r'The term of highest degree is \(-xy^2\) (degree \(1+2=3\)).', r'Hạng tử có bậc cao nhất là \(-xy^2\) (bậc \(1+2=3\)).')],
  T(r'\(P=-xy^2-4xy\); degree \(3\).', r'\(P=-xy^2-4xy\); \(P\) có bậc \(3\).'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('A trap with the degree', 'Cẩn thận khi tìm bậc'),
  T(r'Find the degree of \(Q=3x^4+2x^2y^2-3x^4+xy-5\).', r'Tìm bậc của đa thức \(Q=3x^4+2x^2y^2-3x^4+xy-5\).'),
  ('\\(Q\\) is not simplified yet.', '\\(Q\\) chưa ở dạng thu gọn.'),
  [T(r'\(3x^4-3x^4=0\), so \(Q=2x^2y^2+xy-5\).', r'\(3x^4-3x^4=0\) nên \(Q=2x^2y^2+xy-5\).'),
   T(r'The terms have degrees \(4,\ 2,\ 0\).', r'Các hạng tử có bậc lần lượt là \(4,\ 2,\ 0\).')],
  T(r'\(Q\) has degree \(4\) (because of \(2x^2y^2\), not \(3x^4\)).', r'\(Q\) có bậc \(4\) (do hạng tử \(2x^2y^2\), không phải \(3x^4\)).'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Value of a polynomial', 'Tính giá trị của đa thức'),
  T(r'Find the value of \(A=4x^2y-\dfrac{1}{3}xy+3xz-4x^2y+\dfrac{4}{3}xy\) at \(x=3,\ y=-2,\ z=\dfrac{1}{3}\).', r'Tính giá trị của đa thức \(A=4x^2y-\dfrac{1}{3}xy+3xz-4x^2y+\dfrac{4}{3}xy\) tại \(x=3,\ y=-2,\ z=\dfrac{1}{3}\).'),
  ('Simplify first: several terms cancel.', 'Thu gọn trước, nhiều hạng tử sẽ triệt tiêu.'),
  [T(r'\(A=(4x^2y-4x^2y)+\left(-\dfrac{1}{3}xy+\dfrac{4}{3}xy\right)+3xz=xy+3xz\).', r'\(A=(4x^2y-4x^2y)+\left(-\dfrac{1}{3}xy+\dfrac{4}{3}xy\right)+3xz=xy+3xz\).'),
   T(r'\(A=3\cdot(-2)+3\cdot 3\cdot\dfrac{1}{3}=-6+3=-3\).', r'\(A=3\cdot(-2)+3\cdot 3\cdot\dfrac{1}{3}=-6+3=-3\).')],
  T(r'\(A=-3\).', r'\(A=-3\).'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Surface area of a box', 'Diện tích các mặt của chiếc hộp'),
  T(r'A box is \(x\) cm long, \(y\) cm wide and \(z\) cm high. Write a polynomial \(S\) for the total area of its six faces. What is the degree of \(S\)? Find \(S\) when \(x=5,\ y=4,\ z=3\).', r'Một chiếc hộp hình hộp chữ nhật dài \(x\) cm, rộng \(y\) cm, cao \(z\) cm. Viết đa thức \(S\) biểu thị tổng diện tích sáu mặt của hộp. \(S\) có bậc bao nhiêu? Tính \(S\) khi \(x=5,\ y=4,\ z=3\).'),
  ('There are three pairs of equal faces: \\(xy\\), \\(yz\\), \\(zx\\).', 'Hộp có ba cặp mặt bằng nhau, diện tích \\(xy\\), \\(yz\\), \\(zx\\).'),
  [T(r'\(S=2xy+2yz+2zx\); every term has degree \(2\), so \(S\) has degree \(2\).', r'\(S=2xy+2yz+2zx\); mọi hạng tử đều có bậc \(2\) nên \(S\) có bậc \(2\).'),
   T(r'\(S=2(5\cdot4+4\cdot3+3\cdot5)=2\cdot47=94\) (cm²).', r'\(S=2(5\cdot4+4\cdot3+3\cdot5)=2\cdot47=94\) (cm²).')],
  T(r'\(S=2xy+2yz+2zx\), degree \(2\); \(S=94\) cm².', r'\(S=2xy+2yz+2zx\), bậc \(2\); \(S=94\) cm².'))

_SETS = sp_g8.BANK(sp_g8.L2_GROUPS, start=1, seeds=(821, 822, 823))
practice = LEVEL_PRACTICE(sp_g8.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Finding the degree before simplifying.</b> Terms that cancel do not count.', r'<b>Tìm bậc khi chưa thu gọn.</b> Các hạng tử triệt tiêu nhau không được tính.'),
 (r'<b>Taking the largest exponent as the degree.</b> The degree of \(x^2y^3\) is \(5\), not \(3\).', r'<b>Lấy số mũ lớn nhất làm bậc.</b> Bậc của \(x^2y^3\) là \(5\), không phải \(3\).'),
 (r'<b>Losing the sign of a term.</b> The terms of \(3x-2y\) are \(3x\) and \(-2y\).', r'<b>Bỏ quên dấu của hạng tử.</b> Các hạng tử của \(3x-2y\) là \(3x\) và \(-2y\).'),
 (r'<b>Combining unlike terms.</b> \(2x^2y+3xy\) cannot be simplified further.', r'<b>Cộng các hạng tử không đồng dạng.</b> \(2x^2y+3xy\) không thu gọn thêm được.')]
summary = [
 (r'A polynomial is a sum of monomials (its terms).', r'Đa thức là tổng của những đơn thức; mỗi đơn thức là một hạng tử.'),
 (r'Simplify by combining like terms; the degree is the highest degree of a term in the simplified form.', r'Thu gọn bằng cách cộng các hạng tử đồng dạng; bậc của đa thức là bậc cao nhất của các hạng tử trong dạng thu gọn.'),
 (r'To evaluate: simplify, substitute, calculate.', r'Tính giá trị: thu gọn → thay số → tính.'),
 (r'Key English: polynomial, term, constant term, degree of a polynomial, binomial, trinomial.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[đa thức|đa thức (lớp 8)]], [[hạng tử]], [[hệ số tự do|hệ số tự do (lớp 8)]], [[bậc của đa thức]], [[nhị thức|nhị thức (lớp 8)]], [[tam thức|tam thức (lớp 8)]].')]
checks = [
 (r'I can tell whether an expression is a polynomial and list its terms.', r'Em nhận biết được đa thức và chỉ ra các hạng tử của nó.'),
 (r'I can simplify a polynomial.', r'Em thu gọn được đa thức.'),
 (r'I can find the degree of a polynomial.', r'Em tìm được bậc của đa thức.'),
 (r'I can evaluate a polynomial.', r'Em tính được giá trị của đa thức.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Polynomials', title_vi='Đa thức', topic=TOPIC,
       folder='polynomials', file='polynomials', catalog_title_vi='Đa thức',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Polynomials, terms, simplified form, degree and value.', level='Beginner', minutes=45,
       description_vi='Bài 2 – Đa thức, hạng tử, đa thức thu gọn, bậc của đa thức, giá trị của đa thức.',
       tags_vi=['đa thức', 'hạng tử', 'đa thức thu gọn', 'bậc của đa thức'],
       prerequisites=['g8-polynomials-01'], tags=['polynomial', 'term', 'degree'], order=20)
