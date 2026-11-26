# -*- coding: utf-8 -*-
"""Nội dung bài g8-polynomials-04 = Toán 8 KNTT, Bài 4: Phép nhân đa thức – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 8 (2026), Chapter 1 – Lesson 4, tr. 15–17 (product, distributive property, independent of the variables).
Tình huống lãi kép: SGK Toán 8 KNTT, Hoạt động thực hành trải nghiệm "Công thức lãi kép"."""
import os, sys
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
from mb_pgf import texsvg, img
import sp_g8
from sp_g8 import Poly, M

LID = 'g8-polynomials-04'
CH = 'Đa thức'
TOPIC = ('Polynomials', CH)
ensure_vocab([
 ('g8-comm-mul', 'commutative property of multiplication', 'tính chất giao hoán của phép nhân', CH, 'According to the commutative property of multiplication, A · B = B · A.', ''),
 ('g8-assoc-mul', 'associative property of multiplication', 'tính chất kết hợp của phép nhân', CH, 'According to the associative property of multiplication, (A · B) · C = A · (B · C).', ''),
 ('g8-indep-var', 'independent of the variables', 'không phụ thuộc vào giá trị của biến', CH, 'Show that the value of the expression is independent of the variables.', ''),
])
load_vocab()

# ---------- hình: mô hình diện tích (a+b)(c+d) ----------
AREA = texsvg('\n'.join([
 '\\begin{tikzpicture}[x=1cm,y=1cm,font=\\small]',
 '\\fill[blue!8] (0,0) rectangle (3,2); \\fill[green!10] (3,0) rectangle (4.6,2); \\fill[orange!12] (0,2) rectangle (3,3.2); \\fill[red!8] (3,2) rectangle (4.6,3.2);',
 '\\draw[thick] (0,0) rectangle (4.6,3.2); \\draw (3,0)--(3,3.2); \\draw (0,2)--(4.6,2);',
 '\\node at (1.5,1) {$ac$}; \\node at (3.8,1) {$bc$}; \\node at (1.5,2.6) {$ad$}; \\node at (3.8,2.6) {$bd$};',
 '\\draw[<->] (0,-0.35)--(3,-0.35) node[midway,below] {$a$}; \\draw[<->] (3,-0.35)--(4.6,-0.35) node[midway,below] {$b$};',
 '\\draw[<->] (-0.35,0)--(-0.35,2) node[midway,left] {$c$}; \\draw[<->] (-0.35,2)--(-0.35,3.2) node[midway,left] {$d$};',
 '\\end{tikzpicture}']))

# ---------- kiểm tra số liệu ----------
X = lambda c, a, b: (c, (a, b, 0))
m1 = M(2, (2, 1, 0)); P1 = Poly.of([X(3, 1, 1), X(-5, 0, 2), X(1, 0, 0)])
assert m1 * P1 == Poly.of([X(6, 3, 2), X(-10, 2, 3), X(2, 2, 1)])                                                # Ví dụ 1
A2, B2 = Poly.of([X(1, 1, 0), X(-2, 0, 1)]), Poly.of([X(1, 2, 0), X(3, 1, 1), X(-1, 0, 2)])
assert A2 * B2 == Poly.of([X(1, 3, 0), X(1, 2, 1), X(-7, 1, 2), X(2, 0, 3)])                                     # Ví dụ 2
x_, y_ = M(1, (1, 0, 0)), M(1, (0, 1, 0))
A3 = x_ * Poly.of([X(1, 2, 0), X(-3, 0, 1)]) - M(1, (2, 0, 0)) * Poly.of([X(1, 1, 0), X(1, 0, 1)]) + M(3, (1, 1, 0))
assert A3 == M(-1, (2, 1, 0)) and A3.at(-2, 3) == -12                                                            # Ví dụ 3
P4 = Poly.of([X(1, 2, 0), X(1, 0, 1)]) * Poly.of([X(1, 1, 0), X(-1, 0, 0)]) - Poly.of([X(1, 2, 0), X(-1, 0, 1)]) * Poly.of([X(1, 1, 0), X(1, 0, 0)]) + Poly.of([X(2, 2, 0), X(-2, 1, 1), X(7, 0, 0)])
assert P4 == M(7, (0, 0, 0))                                                                                      # Ví dụ 4
V5 = x_ * Poly.of([X(1, 1, 0), X(4, 0, 0)]) * Poly.of([X(1, 1, 0), X(1, 0, 0)])
assert V5 == Poly.of([X(1, 3, 0), X(5, 2, 0), X(4, 1, 0)]) and V5.at(5) == 270                                  # Ví dụ 5

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 60 minutes', '60 phút'),
            before=('monomials; adding polynomials (Lessons 1–3)', 'đơn thức; cộng, trừ đa thức (Bài 1–3)'))
goals = [
 (r'multiply a monomial by a polynomial;', r'thực hiện được phép nhân đơn thức với đa thức;'),
 (r'multiply a polynomial by a polynomial;', r'thực hiện được phép nhân đa thức với đa thức;'),
 (r'simplify expressions and evaluate them; show that an expression does not depend on the variables;', r'rút gọn và tính giá trị biểu thức; chứng tỏ một biểu thức [[không phụ thuộc vào giá trị của biến]];'),
 (r'write areas, volumes and amounts of money as polynomials.', r'viết được diện tích, thể tích, số tiền dưới dạng đa thức.')]
vocab = [
 (r'<b>product</b> – the result of a multiplication: \(A\cdot B\).', r'[[Tích]] – kết quả của phép nhân: \(A\cdot B\).'),
 (r'<b>distributive property</b> – \(A(B+C)=AB+AC\).', r'[[Tính chất phân phối]] – \(A(B+C)=AB+AC\).'),
 (r'<b>commutative property of multiplication</b> – \(A\cdot B=B\cdot A\).', r'[[Tính chất giao hoán của phép nhân]] – \(A\cdot B=B\cdot A\).'),
 (r'<b>associative property of multiplication</b> – \((A\cdot B)\cdot C=A\cdot(B\cdot C)\).', r'[[Tính chất kết hợp của phép nhân]] – \((A\cdot B)\cdot C=A\cdot(B\cdot C)\).'),
 (r'<b>expand</b> – write a product as a sum of terms.', r'[[Khai triển]] – viết một tích thành tổng các hạng tử.'),
 (r'<b>independent of the variables</b> – the value is the same for all values of the variables.', r'[[Không phụ thuộc vào giá trị của biến]] – biểu thức có cùng một giá trị với mọi giá trị của biến.')]
phrases = [
 (r'<b>Multiply the polynomial by the monomial.</b>', r'Nhân đơn thức với đa thức.'),
 (r'<b>To multiply a polynomial by a monomial, we multiply each term of the polynomial by the monomial.</b>', r'Muốn nhân một đơn thức với một đa thức, ta nhân đơn thức với từng hạng tử của đa thức rồi cộng các tích.'),
 (r'<b>To multiply two polynomials, we multiply each term of the first polynomial by each term of the second polynomial.</b>', r'Muốn nhân hai đa thức, ta nhân mỗi hạng tử của đa thức này với từng hạng tử của đa thức kia rồi cộng các tích.'),
 (r'<b>Simplify the expression and evaluate it for \(x=-2,\ y=3\).</b>', r'Rút gọn biểu thức rồi tính giá trị tại \(x=-2,\ y=3\).'),
 (r'<b>Show that the value of the expression is independent of the variables.</b>', r'Chứng tỏ giá trị của biểu thức không phụ thuộc vào giá trị của biến.')]
review = (T(r'<b>Multiplying monomials (Lesson 1).</b> \(2x^2y\cdot 3xy^3=6x^3y^4\): multiply the coefficients, add the exponents.', r'<b>Nhân hai đơn thức (Bài 1).</b> \(2x^2y\cdot 3xy^3=6x^3y^4\): nhân các hệ số, cộng số mũ.') +
          T(r'<b>Distributive property (grade 7).</b> \(a(b+c)=ab+ac\).', r'<b>Tính chất phân phối (lớp 7).</b> \(a(b+c)=ab+ac\).'))

theory = '<h3>4.1 %s</h3>' % TI('Multiplying a monomial by a polynomial', 'Nhân đơn thức với đa thức')
theory += BOX('blue', ('Rule', 'Quy tắc'),
  T(r'Multiply the monomial by <b>each</b> term of the polynomial, then add the products: \(A(B+C)=AB+AC\).', r'Muốn nhân một đơn thức với một đa thức, ta nhân đơn thức đó với <b>từng</b> hạng tử của đa thức rồi cộng các tích với nhau: \(A(B+C)=AB+AC\).'),
  T(r'\(-3x^2y(2x-y+4)=-6x^3y+3x^2y^2-12x^2y\).', r'\(-3x^2y(2x-y+4)=-6x^3y+3x^2y^2-12x^2y\).'))
theory += '<h3>4.2 %s</h3>' % TI('Multiplying two polynomials', 'Nhân đa thức với đa thức')
theory += BOX('mint', ('Rule', 'Quy tắc'),
  T(r'Multiply <b>each term</b> of the first polynomial by <b>each term</b> of the second, then add the products and combine like terms.', r'Muốn nhân một đa thức với một đa thức, ta nhân <b>mỗi hạng tử</b> của đa thức này với <b>từng hạng tử</b> của đa thức kia rồi cộng các tích với nhau (và thu gọn).'),
  T(r'\((a+b)(c+d)=ac+ad+bc+bd\). Example: \((x+2)(x-5)=x^2-5x+2x-10=x^2-3x-10\).', r'\((a+b)(c+d)=ac+ad+bc+bd\). Ví dụ: \((x+2)(x-5)=x^2-5x+2x-10=x^2-3x-10\).'),
  img(AREA, 'Area model of (a+b)(c+d)', 260, TI('Area model: the big rectangle \\((a+b)(c+d)\\) is made of four parts \\(ac+ad+bc+bd\\).', 'Mô hình diện tích: hình chữ nhật lớn \\((a+b)(c+d)\\) gồm bốn phần \\(ac+ad+bc+bd\\).')))
theory += BOX('blue', ('Properties and counting', 'Tính chất'),
  T(r'Multiplication of polynomials is commutative and associative, and it distributes over addition.', r'Phép nhân đa thức có [[tính chất giao hoán của phép nhân]], [[tính chất kết hợp của phép nhân]] và [[tính chất phân phối]] đối với phép cộng.'),
  T(r'A polynomial with \(m\) terms times a polynomial with \(n\) terms gives \(m\cdot n\) products before combining. The degree of the product is the sum of the degrees.', r'Nhân đa thức có \(m\) hạng tử với đa thức có \(n\) hạng tử, trước khi thu gọn ta được \(m\cdot n\) tích. Bậc của tích bằng tổng bậc của hai đa thức.'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'),
  T(r'Do not forget the middle terms: \((x+3)(x+4)=x^2+7x+12\), not \(x^2+12\).', r'Không bỏ sót các tích ở giữa: \((x+3)(x+4)=x^2+7x+12\), không phải \(x^2+12\).'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Monomial × polynomial', 'Nhân đơn thức với đa thức'),
  T(r'Find the product \(2x^2y(3xy-5y^2+1)\).', r'Thực hiện phép nhân \(2x^2y(3xy-5y^2+1)\).'),
  ('Multiply \\(2x^2y\\) by each of the three terms.', 'Nhân \\(2x^2y\\) với từng hạng tử trong ngoặc.'),
  [T(r'\(2x^2y\cdot3xy=6x^3y^2\); \(2x^2y\cdot(-5y^2)=-10x^2y^3\); \(2x^2y\cdot1=2x^2y\).', r'\(2x^2y\cdot3xy=6x^3y^2\); \(2x^2y\cdot(-5y^2)=-10x^2y^3\); \(2x^2y\cdot1=2x^2y\).')],
  T(r'\(6x^3y^2-10x^2y^3+2x^2y\).', r'\(6x^3y^2-10x^2y^3+2x^2y\).'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Polynomial × polynomial', 'Nhân hai đa thức'),
  T(r'Expand \((x-2y)(x^2+3xy-y^2)\).', r'Thực hiện phép nhân \((x-2y)(x^2+3xy-y^2)\).'),
  ('Multiply \\(x\\), then \\(-2y\\), by each term of the second bracket.', 'Lần lượt nhân \\(x\\) và \\(-2y\\) với từng hạng tử của ngoặc thứ hai.'),
  [T(r'\(x(x^2+3xy-y^2)=x^3+3x^2y-xy^2\).', r'\(x(x^2+3xy-y^2)=x^3+3x^2y-xy^2\).'),
   T(r'\(-2y(x^2+3xy-y^2)=-2x^2y-6xy^2+2y^3\).', r'\(-2y(x^2+3xy-y^2)=-2x^2y-6xy^2+2y^3\).'),
   T(r'Add: \(x^3+x^2y-7xy^2+2y^3\).', r'Cộng lại và thu gọn: \(x^3+x^2y-7xy^2+2y^3\).')],
  T(r'\(x^3+x^2y-7xy^2+2y^3\).', r'\(x^3+x^2y-7xy^2+2y^3\).'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('Simplify, then evaluate', 'Rút gọn rồi tính giá trị'),
  T(r'Simplify \(A=x(x^2-3y)-x^2(x+y)+3xy\), then evaluate it at \(x=-2,\ y=3\).', r'Rút gọn biểu thức \(A=x(x^2-3y)-x^2(x+y)+3xy\) rồi tính giá trị tại \(x=-2,\ y=3\).'),
  ('Expand each product, then combine.', 'Khai triển từng tích rồi thu gọn.'),
  [T(r'\(A=x^3-3xy-x^3-x^2y+3xy=-x^2y\).', r'\(A=x^3-3xy-x^3-x^2y+3xy=-x^2y\).'),
   T(r'\(A=-(-2)^2\cdot3=-12\).', r'\(A=-(-2)^2\cdot3=-12\).')],
  T(r'\(A=-x^2y=-12\).', r'\(A=-x^2y\); giá trị bằng \(-12\).'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Independent of the variables', 'Giá trị không phụ thuộc vào biến'),
  T(r'Show that \(P=(x^2+y)(x-1)-(x^2-y)(x+1)+2x^2-2xy+7\) does not depend on \(x\) and \(y\).', r'Chứng tỏ giá trị của biểu thức \(P=(x^2+y)(x-1)-(x^2-y)(x+1)+2x^2-2xy+7\) không phụ thuộc vào giá trị của \(x\) và \(y\).'),
  ('Expand and show that all terms with variables cancel.', 'Khai triển và chứng tỏ mọi hạng tử chứa biến đều triệt tiêu.'),
  [T(r'\((x^2+y)(x-1)=x^3-x^2+xy-y\); \((x^2-y)(x+1)=x^3+x^2-xy-y\).', r'\((x^2+y)(x-1)=x^3-x^2+xy-y\); \((x^2-y)(x+1)=x^3+x^2-xy-y\).'),
   T(r'\(P=x^3-x^2+xy-y-x^3-x^2+xy+y+2x^2-2xy+7=7\).', r'\(P=x^3-x^2+xy-y-x^3-x^2+xy+y+2x^2-2xy+7=7\).')],
  T(r'\(P=7\) for all \(x\), \(y\).', r'\(P=7\) với mọi \(x\), \(y\): giá trị của \(P\) không phụ thuộc vào biến.'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Volume of a tank', 'Thể tích bể nước'),
  T(r'A tank has a rectangular base \((x+4)\) dm by \((x+1)\) dm and height \(x\) dm. Write its volume as a polynomial. How many liters does it hold when \(x=5\)?', r'Một bể nước có đáy là hình chữ nhật kích thước \((x+4)\) dm và \((x+1)\) dm, chiều cao \(x\) dm. Viết đa thức biểu thị thể tích của bể. Khi \(x=5\), bể chứa được bao nhiêu lít nước?'),
  ('Volume = length × width × height; 1 dm³ = 1 liter.', 'Thể tích = dài × rộng × cao; 1 dm³ = 1 lít.'),
  [T(r'\(V=x(x+4)(x+1)=x(x^2+5x+4)=x^3+5x^2+4x\) (dm³).', r'\(V=x(x+4)(x+1)=x(x^2+5x+4)=x^3+5x^2+4x\) (dm³).'),
   T(r'\(x=5\): \(V=125+125+20=270\) (dm³).', r'\(x=5\): \(V=125+125+20=270\) (dm³).')],
  T(r'\(V=x^3+5x^2+4x\); the tank holds 270 liters.', r'\(V=x^3+5x^2+4x\); bể chứa được 270 lít nước.'))

_SETS = sp_g8.BANK(sp_g8.L4_GROUPS, start=1, seeds=(841, 842, 843))
practice = LEVEL_PRACTICE(sp_g8.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Multiplying only the first term.</b> \(2x(x+3)=2x^2+6x\), not \(2x^2+3\).', r'<b>Chỉ nhân với hạng tử đầu.</b> \(2x(x+3)=2x^2+6x\), không phải \(2x^2+3\).'),
 (r'<b>Sign errors with a negative factor.</b> \(-y(x-2)=-xy+2y\).', r'<b>Sai dấu khi nhân với số âm.</b> \(-y(x-2)=-xy+2y\).'),
 (r'<b>Missing middle terms.</b> \((x+a)(x+b)=x^2+(a+b)x+ab\).', r'<b>Thiếu các tích ở giữa.</b> \((x+a)(x+b)=x^2+(a+b)x+ab\).'),
 (r'<b>Multiplying exponents.</b> \(x^2\cdot x^3=x^5\).', r'<b>Nhân các số mũ.</b> \(x^2\cdot x^3=x^5\).')]
summary = [
 (r'Monomial × polynomial: multiply by each term, then add.', r'Đơn thức × đa thức: nhân với từng hạng tử rồi cộng.'),
 (r'Polynomial × polynomial: each term × each term, then combine like terms.', r'Đa thức × đa thức: mỗi hạng tử nhân với từng hạng tử rồi thu gọn.'),
 (r'To show an expression does not depend on the variables, simplify it to a number.', r'Muốn chứng tỏ biểu thức không phụ thuộc vào biến, rút gọn nó thành một hằng số.'),
 (r'Key English: product, expand, distributive property, independent of the variables.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[tích]], [[khai triển]], [[tính chất phân phối]], [[không phụ thuộc vào giá trị của biến]].')]
checks = [
 (r'I can multiply a monomial by a polynomial.', r'Em nhân được đơn thức với đa thức.'),
 (r'I can multiply two polynomials and combine like terms.', r'Em nhân được hai đa thức và thu gọn kết quả.'),
 (r'I can show that an expression does not depend on the variables.', r'Em chứng tỏ được một biểu thức không phụ thuộc vào biến.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Multiplying Polynomials', title_vi='Phép nhân đa thức', topic=TOPIC,
       folder='polynomials', file='multiplying-polynomials', catalog_title_vi='Phép nhân đa thức',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Multiplying a monomial by a polynomial and two polynomials.', level='Intermediate', minutes=60,
       description_vi='Bài 4 – Nhân đơn thức với đa thức, nhân đa thức với đa thức; rút gọn, tính giá trị biểu thức.',
       tags_vi=['nhân đa thức', 'tính chất phân phối', 'khai triển'],
       prerequisites=['g8-polynomials-03'], tags=['product', 'distributive property', 'expand'], order=40)
