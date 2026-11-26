# -*- coding: utf-8 -*-
"""Nội dung bài g8-polynomials-05 = Toán 8 KNTT, Bài 5: Phép chia đa thức cho đơn thức – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 8 (2026), Chapter 1 – Lesson 5, tr. 18–19 (base, quotient, be divisible by).
Dấu chia: Mức 1 viết "A : B" như SGK; Mức 2, 3 viết "A ÷ B" như TLTA (đề xuất Q10 trong DAN-Y-LOP-8.md)."""
import os, sys
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g8
from sp_g8 import Poly, M

LID = 'g8-polynomials-05'
CH = 'Đa thức'
TOPIC = ('Polynomials', CH)
ensure_vocab([
 ('g8-divisible', 'be divisible by', 'chia hết cho (lớp 8)', CH, 'The monomial 2x²y³ is divisible by the monomial 2xy.', ''),
 ('g8-exact-div', 'exact division', 'phép chia hết', CH, '12x⁴y² ÷ 3x² is an exact division.', ''),
 ('g8-dividend', 'dividend', 'đa thức bị chia', CH, 'In (6x² + 3x) ÷ 3x, the dividend is 6x² + 3x.', ''),
 ('g8-divisor', 'divisor', 'đơn thức chia', CH, 'In (6x² + 3x) ÷ 3x, the divisor is 3x.', ''),
])
load_vocab()

# ---------- kiểm tra số liệu ----------
X = lambda c, a, b, z=0: (c, (a, b, z))
from sp_g8 import divisible, mdiv
assert not divisible((3, 2, 1), (2, 3, 0)) and divisible((3, 2, 1), (2, 1, 1)) and mdiv(6, (3, 2, 1), -3, (2, 1, 1)) == (-2, (1, 1, 0))   # Ví dụ 1
assert mdiv(12, (4, 3, 0), -4, (2, 1, 0)) == (-3, (2, 2, 0))                                                    # Ví dụ 2
assert M(2, (2, 2, 0)) * Poly.of([X(4, 2, 1), X(-3, 1, 0), X(1, 0, 0)]) == Poly.of([X(8, 4, 3), X(-6, 3, 2), X(2, 2, 2)])   # Ví dụ 3
Q4 = Poly.of([X(-3, 2, 1), X(2, 1, 2), X(-1, 0, 3)])
assert Q4 * M(-3, (1, 2, 0)) == Poly.of([X(9, 3, 3), X(-6, 2, 4), X(3, 1, 5)])                                   # Ví dụ 4
L5 = Poly.of([X(2, 1, 0), X(3, 0, 1)])
assert L5 * M(3, (2, 1, 0)) == Poly.of([X(6, 3, 1), X(9, 2, 2)]) and L5.at(2, 1) == 7                          # Ví dụ 5

def DV(en, vi): return T(en.replace(':', '\\div '), vi)

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 45 minutes', '45 phút'),
            before=('monomials; multiplying polynomials (Lessons 1, 4)', 'đơn thức; phép nhân đa thức (Bài 1, 4)'))
goals = [
 (r'state when a monomial is divisible by a monomial and when a polynomial is divisible by a monomial;', r'nêu được điều kiện để đơn thức [[chia hết cho|chia hết cho (lớp 8)]] đơn thức, đa thức chia hết cho đơn thức;'),
 (r'divide a monomial by a monomial;', r'thực hiện được phép chia đơn thức cho đơn thức;'),
 (r'divide a polynomial by a monomial (exact division);', r'thực hiện được phép chia đa thức cho đơn thức trong trường hợp [[phép chia hết]];'),
 (r'find an unknown factor and solve simple problems with division.', r'tìm được thừa số chưa biết và giải bài toán thực tế có phép chia.')]
vocab = [
 (r'<b>quotient</b> – the result of a division: \(6x^3\div 2x=3x^2\).', r'[[Thương]] – kết quả của phép chia: \(6x^3:2x=3x^2\).'),
 (r'<b>be divisible by</b> – \(2x^2y^3\) is divisible by \(2xy\) because the quotient \(xy^2\) is a monomial.', r'[[Chia hết cho|chia hết cho (lớp 8)]] – \(2x^2y^3\) chia hết cho \(2xy\) vì thương \(xy^2\) là một đơn thức.'),
 (r'<b>exact division</b> – a division in which the quotient is a polynomial.', r'[[Phép chia hết]] – phép chia có thương là một đa thức.'),
 (r'<b>dividend / divisor</b> – in \(A\div B\), \(A\) is the dividend and \(B\) is the divisor.', r'[[Đa thức bị chia]] / [[đơn thức chia]] – trong phép chia \(A:B\), \(A\) là đa thức bị chia, \(B\) là đơn thức chia.'),
 (r'<b>base / exponent</b> – \(x^m\div x^n=x^{m-n}\) (same base \(x\), \(m\ge n\)).', r'[[Cơ số]] / [[số mũ]] – \(x^m:x^n=x^{m-n}\) (cùng cơ số \(x\), \(m\ge n\)).')]
phrases = [
 (r'<b>Find the quotient of the division.</b>', r'Tìm thương của phép chia.'),
 (r'<b>Is the polynomial divisible by the monomial?</b>', r'Đa thức có chia hết cho đơn thức không?'),
 (r'<b>Which of the following divisions are not exact?</b>', r'Phép chia nào sau đây không phải là phép chia hết?'),
 (r'<b>To divide two monomials, we divide the coefficients and subtract the exponents of like bases.</b>', r'Muốn chia hai đơn thức, ta chia hệ số cho hệ số và trừ số mũ của cùng một biến.'),
 (r'<b>To divide a polynomial by a monomial, divide each term of the polynomial by the monomial.</b>', r'Muốn chia đa thức cho đơn thức, ta chia từng hạng tử của đa thức cho đơn thức.')]
review = (T(r'<b>Dividing powers.</b> \(x^m\div x^n=x^{m-n}\ (m\ge n)\); \(x^n\div x^n=1\).', r'<b>Chia hai lũy thừa cùng cơ số.</b> \(x^m:x^n=x^{m-n}\ (m\ge n)\); \(x^n:x^n=1\).') +
          T(r'<b>Multiplying (Lesson 4).</b> \(A\cdot B=C\) means \(C\div B=A\).', r'<b>Liên hệ với phép nhân (Bài 4).</b> \(A\cdot B=C\) thì \(C:B=A\).'))

theory = '<h3>5.1 %s</h3>' % TI('Dividing a monomial by a monomial', 'Chia đơn thức cho đơn thức')
theory += BOX('blue', ('When is it exact?', 'Khi nào chia hết?'),
  T(r'Monomial \(A\) is <b>divisible by</b> monomial \(B\ne0\) when every variable of \(B\) is a variable of \(A\) with an exponent <b>not greater than</b> its exponent in \(A\).', r'Đơn thức \(A\) [[chia hết cho|chia hết cho (lớp 8)]] đơn thức \(B\) (\(B\ne0\)) khi mỗi biến của \(B\) đều là biến của \(A\) với số mũ <b>không lớn hơn</b> số mũ của nó trong \(A\).'),
  T(r'Example: \(5x^2yz^3\) is divisible by \(-2x^2z^2\) but not by \(x^2y^2z^2\) (the exponent of \(y\) is \(2>1\)).', r'Ví dụ: \(5x^2yz^3\) chia hết cho \(-2x^2z^2\) nhưng không chia hết cho \(x^2y^2z^2\) (số mũ của \(y\) là \(2>1\)).'))
theory += BOX('mint', ('Rule', 'Quy tắc'),
  DV(r'Divide the coefficient of \(A\) by that of \(B\); for each variable, subtract the exponents. \(5x^2yz^3:(-2x^2z^2)=-\dfrac{5}{2}yz\).', r'Chia hệ số của \(A\) cho hệ số của \(B\); chia lũy thừa của từng biến trong \(A\) cho lũy thừa của cùng biến đó trong \(B\) (trừ số mũ); rồi nhân các kết quả. \(5x^2yz^3:(-2x^2z^2)=-\dfrac{5}{2}yz\).'))
theory += '<h3>5.2 %s</h3>' % TI('Dividing a polynomial by a monomial', 'Chia đa thức cho đơn thức')
theory += BOX('blue', ('Rule', 'Quy tắc'),
  T(r'A polynomial is divisible by a monomial when <b>every term</b> is divisible by it. Then divide each term by the monomial and add the results: \((A+B)\div C=A\div C+B\div C\).', r'Đa thức \(A\) chia hết cho đơn thức \(B\) khi <b>mọi hạng tử</b> của \(A\) đều chia hết cho \(B\). Khi đó ta chia từng hạng tử của \(A\) cho \(B\) rồi cộng các kết quả: \((A+B):C=A:C+B:C\).'),
  DV(r'\((6x^4y^2-5x^3y^4+xy^3):3xy^2=2x^3-\dfrac{5}{3}x^2y^2+\dfrac{1}{3}y\).', r'\((6x^4y^2-5x^3y^4+xy^3):3xy^2=2x^3-\dfrac{5}{3}x^2y^2+\dfrac{1}{3}y\).'))
theory += BOX('yellow', ('Notation', 'Kí hiệu'),
  T(r'In English, division is written with \(\div\); Vietnamese textbooks write \(A:B\). Check: quotient × divisor = dividend.', r'Sách giáo khoa viết phép chia là \(A:B\) (tiếng Anh thường viết \(A\div B\)). Kiểm tra: thương × đơn thức chia = đa thức bị chia.'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Divisible or not?', 'Có chia hết không?'),
  T(r'Let \(A=6x^3y^2z\). Is \(A\) divisible by \(B=2x^2y^3\)? By \(C=-3x^2yz\)? If so, find the quotient.', r'Cho \(A=6x^3y^2z\). \(A\) có chia hết cho \(B=2x^2y^3\) không? Có chia hết cho \(C=-3x^2yz\) không? Nếu có, tìm thương.'),
  ('Compare the exponents variable by variable.', 'So sánh số mũ của từng biến.'),
  [T(r'In \(B\), \(y\) has exponent \(3>2\): \(A\) is <b>not</b> divisible by \(B\).', r'Trong \(B\), biến \(y\) có số mũ \(3>2\) nên \(A\) <b>không</b> chia hết cho \(B\).'),
   T(r'Every exponent in \(C\) is at most that in \(A\): \(A\) is divisible by \(C\).', r'Mọi biến của \(C\) có số mũ không lớn hơn trong \(A\) nên \(A\) chia hết cho \(C\).'),
   DV(r'\(6x^3y^2z:(-3x^2yz)=-2xy\).', r'\(6x^3y^2z:(-3x^2yz)=-2xy\).')],
  T(r'Not divisible by \(B\); \(A\div C=-2xy\).', r'\(A\) không chia hết cho \(B\); \(A:C=-2xy\).'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Monomial ÷ monomial', 'Chia đơn thức cho đơn thức'),
  DV(r'Find the quotient \(12x^4y^3:(-4x^2y)\).', r'Tìm thương của phép chia \(12x^4y^3:(-4x^2y)\).'),
  ('Divide the coefficients, subtract the exponents.', 'Chia hệ số cho hệ số, trừ số mũ của từng biến.'),
  [DV(r'\(12:(-4)=-3\); \(x^4:x^2=x^2\); \(y^3:y=y^2\).', r'\(12:(-4)=-3\); \(x^4:x^2=x^2\); \(y^3:y=y^2\).')],
  T(r'\(-3x^2y^2\).', r'\(-3x^2y^2\).'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('Polynomial ÷ monomial', 'Chia đa thức cho đơn thức'),
  DV(r'Find \((8x^4y^3-6x^3y^2+2x^2y^2):2x^2y^2\).', r'Thực hiện phép chia \((8x^4y^3-6x^3y^2+2x^2y^2):2x^2y^2\).'),
  ('Every term is divisible by \\(2x^2y^2\\).', 'Mọi hạng tử đều chia hết cho \\(2x^2y^2\\).'),
  [DV(r'\(8x^4y^3:2x^2y^2=4x^2y\); \(-6x^3y^2:2x^2y^2=-3x\); \(2x^2y^2:2x^2y^2=1\).', r'\(8x^4y^3:2x^2y^2=4x^2y\); \(-6x^3y^2:2x^2y^2=-3x\); \(2x^2y^2:2x^2y^2=1\).')],
  T(r'\(4x^2y-3x+1\).', r'\(4x^2y-3x+1\).'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Find an unknown factor', 'Tìm thừa số chưa biết'),
  T(r'Find the polynomial \(A\) such that \(A\cdot(-3xy^2)=9x^3y^3-6x^2y^4+3xy^5\).', r'Tìm đa thức \(A\), biết \(A\cdot(-3xy^2)=9x^3y^3-6x^2y^4+3xy^5\).'),
  ('A missing factor = product ÷ known factor.', 'Thừa số chưa biết = tích : thừa số đã biết.'),
  [DV(r'\(A=(9x^3y^3-6x^2y^4+3xy^5):(-3xy^2)\).', r'\(A=(9x^3y^3-6x^2y^4+3xy^5):(-3xy^2)\).'),
   T(r'\(A=-3x^2y+2xy^2-y^3\). Check: \((-3x^2y+2xy^2-y^3)(-3xy^2)=9x^3y^3-6x^2y^4+3xy^5\) ✓.', r'\(A=-3x^2y+2xy^2-y^3\). Thử lại: \((-3x^2y+2xy^2-y^3)(-3xy^2)=9x^3y^3-6x^2y^4+3xy^5\) ✓.')],
  T(r'\(A=-3x^2y+2xy^2-y^3\).', r'\(A=-3x^2y+2xy^2-y^3\).'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Length of a rectangle', 'Chiều dài hình chữ nhật'),
  T(r'A rectangle has area \(6x^3y+9x^2y^2\) (cm²) and width \(3x^2y\) (cm). Find its length as a polynomial, then for \(x=2,\ y=1\).', r'Một hình chữ nhật có diện tích \(6x^3y+9x^2y^2\) (cm²) và chiều rộng \(3x^2y\) (cm). Tìm đa thức biểu thị chiều dài, rồi tính chiều dài khi \(x=2,\ y=1\).'),
  ('Length = area ÷ width.', 'Chiều dài = diện tích : chiều rộng.'),
  [DV(r'\((6x^3y+9x^2y^2):3x^2y=2x+3y\).', r'\((6x^3y+9x^2y^2):3x^2y=2x+3y\).'),
   T(r'\(x=2,\ y=1\): \(2\cdot2+3\cdot1=7\) (cm).', r'\(x=2,\ y=1\): \(2\cdot2+3\cdot1=7\) (cm).')],
  T(r'Length \(2x+3y\) cm; 7 cm.', r'Chiều dài \(2x+3y\) (cm); bằng 7 cm.'))

_SETS = sp_g8.BANK(sp_g8.L5_GROUPS, start=1, seeds=(851, 852, 853))
practice = LEVEL_PRACTICE(sp_g8.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Dividing the exponents.</b> \(x^6\div x^2=x^4\), not \(x^3\).', r'<b>Chia các số mũ.</b> \(x^6:x^2=x^4\), không phải \(x^3\).'),
 (r'<b>Forgetting a term.</b> \((x^2y+xy)\div xy=x+1\): the last term gives \(1\), not \(0\).', r'<b>Bỏ sót hạng tử.</b> \((x^2y+xy):xy=x+1\): hạng tử cuối cho thương \(1\), không phải \(0\).'),
 (r'<b>Sign errors.</b> \(-6x^3\div(-2x)=3x^2\).', r'<b>Sai dấu.</b> \(-6x^3:(-2x)=3x^2\).'),
 (r'<b>Calling a division exact too quickly.</b> \(8x^2y^2\div 6xz\) is not exact: \(z\) is not in the dividend.', r'<b>Vội cho là chia hết.</b> \(8x^2y^2:6xz\) không phải phép chia hết vì \(z\) không có trong đơn thức bị chia.')]
summary = [
 (r'\(A\) is divisible by \(B\) when each variable of \(B\) appears in \(A\) with an exponent not greater than in \(A\).', r'\(A\) chia hết cho \(B\) khi mỗi biến của \(B\) đều có trong \(A\) với số mũ không lớn hơn số mũ trong \(A\).'),
 (r'Monomial ÷ monomial: divide the coefficients, subtract the exponents.', r'Chia đơn thức cho đơn thức: chia hệ số, trừ số mũ.'),
 (r'Polynomial ÷ monomial: divide each term, then add.', r'Chia đa thức cho đơn thức: chia từng hạng tử rồi cộng các kết quả.'),
 (r'Key English: quotient, be divisible by, exact division, dividend, divisor.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[thương]], [[chia hết cho|chia hết cho (lớp 8)]], [[phép chia hết]], [[đa thức bị chia]], [[đơn thức chia]].')]
checks = [
 (r'I can tell whether a monomial or a polynomial is divisible by a monomial.', r'Em nhận biết được đơn thức, đa thức có chia hết cho đơn thức hay không.'),
 (r'I can divide a monomial by a monomial.', r'Em chia được đơn thức cho đơn thức.'),
 (r'I can divide a polynomial by a monomial.', r'Em chia được đa thức cho đơn thức.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Dividing Polynomials by Monomials', title_vi='Phép chia đa thức cho đơn thức', topic=TOPIC,
       folder='polynomials', file='dividing-polynomials-by-monomials', catalog_title_vi='Phép chia đa thức cho đơn thức',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Dividing a monomial by a monomial and a polynomial by a monomial.', level='Intermediate', minutes=45,
       description_vi='Bài 5 – Chia đơn thức cho đơn thức, chia đa thức cho đơn thức (trường hợp chia hết).',
       tags_vi=['chia đơn thức', 'chia đa thức cho đơn thức', 'chia hết'],
       prerequisites=['g8-polynomials-04'], tags=['quotient', 'divisible', 'division'], order=50)
