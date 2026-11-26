# -*- coding: utf-8 -*-
"""Nội dung bài g8-polynomials-03 = Toán 8 KNTT, Bài 3: Phép cộng và phép trừ đa thức – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 8 (2026), Chapter 1 – Lesson 3, tr. 13–14 (sum, difference, commutative/associative property of addition)."""
import os, sys
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g8
from sp_g8 import Poly, M

LID = 'g8-polynomials-03'
CH = 'Đa thức'
TOPIC = ('Polynomials', CH)
ensure_vocab([
 ('g8-sum', 'sum', 'tổng (lớp 8)', CH, 'The sum of two polynomials A and B is the polynomial A + B.', ''),
 ('g8-comm-add', 'commutative property of addition', 'tính chất giao hoán của phép cộng', CH, 'According to the commutative property of addition, A + B = B + A.', ''),
 ('g8-assoc-add', 'associative property of addition', 'tính chất kết hợp của phép cộng', CH, 'According to the associative property of addition, (A + B) + C = A + (B + C).', ''),
 ('g8-remove-brackets', 'remove brackets', 'bỏ dấu ngoặc (lớp 8)', CH, 'Remove the brackets and combine like terms.', ''),
])
load_vocab()

# ---------- kiểm tra số liệu ----------
X = lambda c, a, b, z=0: (c, (a, b, z))
A1 = Poly.of([X(2, 2, 1), X(3, 1, 1), X(-4, 0, 0)]); B1 = Poly.of([X(-1, 1, 1), X(1, 2, 0), X(-2, 2, 1), X(5, 0, 0)])
assert A1 + B1 == Poly.of([X(2, 1, 1), X(1, 2, 0), X(1, 0, 0)])                                                # Ví dụ 1
A2 = Poly.of([X(3, 2, 2), X(-2, 1, 1), X(1, 0, 1)]); B2 = Poly.of([X(-1, 2, 2), X(4, 1, 1), X(-6, 0, 0)])
assert A2 - B2 == Poly.of([X(4, 2, 2), X(-6, 1, 1), X(1, 0, 1), X(6, 0, 0)])                                    # Ví dụ 2
C3 = Poly.of([X(6, 2, 1), X(4, 1, 0), X(-2, 0, 0, 1), X(3, 0, 0)]); B3 = Poly.of([X(1, 1, 1, 1), X(-3, 2, 1), X(4, 1, 0), X(-1, 0, 0)])
assert C3 - B3 == Poly.of([X(9, 2, 1), X(-1, 1, 1, 1), X(-2, 0, 0, 1), X(4, 0, 0)])                           # Ví dụ 3
A4 = Poly.of([X(2, 2, 1), X(-3, 1, 1, 1), X(5, 1, 0), X(-2, 0, 0)]); B4 = Poly.of([X(-2, 2, 1), X(4, 1, 1, 1), X(-1, 1, 0), X(3, 0, 0)])
S4, D4 = A4 + B4, A4 - B4
assert S4 == Poly.of([X(1, 1, 1, 1), X(4, 1, 0), X(1, 0, 0)]) and S4.deg() == 3 and S4.at(1, 2, -1) == 3     # Ví dụ 4
assert D4 == Poly.of([X(4, 2, 1), X(-7, 1, 1, 1), X(6, 1, 0), X(-5, 0, 0)]) and D4.at(1, 2, -1) == 23
Rv, Cv = Poly.of([X(-1, 2, 0), X(120, 1, 0)]), Poly.of([X(20, 1, 0), X(500, 0, 0)])
assert Rv - Cv == Poly.of([X(-1, 2, 0), X(100, 1, 0), X(-500, 0, 0)]) and (Rv - Cv).at(40) == 1900             # Ví dụ 5

meta = dict(level=('Beginner', 'Cơ bản'), time=('about 45 minutes', '45 phút'),
            before=('polynomials, like terms (Lessons 1–2)', 'đa thức, hạng tử đồng dạng (Bài 1, 2)'))
goals = [
 (r'add two polynomials;', r'thực hiện được phép cộng hai đa thức;'),
 (r'subtract two polynomials, changing the sign of every term in the brackets after a minus sign;', r'thực hiện được phép trừ hai đa thức, đổi dấu mọi hạng tử trong ngoặc đứng sau dấu trừ;'),
 (r'use addition and subtraction to find an unknown polynomial and to simplify expressions.', r'vận dụng phép cộng, trừ đa thức để tìm đa thức chưa biết và rút gọn biểu thức.')]
vocab = [
 (r'<b>sum</b> – the result of an addition: \(A+B\).', r'[[Tổng|tổng (lớp 8)]] – kết quả của phép cộng: \(A+B\).'),
 (r'<b>difference</b> – the result of a subtraction: \(A-B\).', r'[[Hiệu]] – kết quả của phép trừ: \(A-B\).'),
 (r'<b>like terms</b> – terms with the same literal part; they can be combined.', r'[[Các hạng tử đồng dạng]] – các hạng tử có cùng phần biến; cộng được với nhau.'),
 (r'<b>commutative property of addition</b> – \(A+B=B+A\).', r'[[Tính chất giao hoán của phép cộng]] – \(A+B=B+A\).'),
 (r'<b>associative property of addition</b> – \((A+B)+C=A+(B+C)\).', r'[[Tính chất kết hợp của phép cộng]] – \((A+B)+C=A+(B+C)\).'),
 (r'<b>remove brackets</b> – after a minus sign, change the sign of every term inside.', r'[[Bỏ dấu ngoặc|bỏ dấu ngoặc (lớp 8)]] – nếu trước ngoặc có dấu trừ thì đổi dấu mọi hạng tử trong ngoặc.')]
phrases = [
 (r'<b>Find the sum / difference of the polynomials.</b>', r'Tính tổng / hiệu của các đa thức.'),
 (r'<b>Remove the brackets and combine like terms.</b>', r'Bỏ dấu ngoặc rồi cộng các hạng tử đồng dạng.'),
 (r'<b>Find the polynomial \(M\) given that \(M+B=C\).</b>', r'Tìm đa thức \(M\), biết \(M+B=C\).'),
 (r'<b>Can these terms be combined?</b>', r'Các hạng tử này có cộng được với nhau không?'),
 (r'<b>Evaluate \(A+B\) for \(x=1,\ y=2\).</b>', r'Tính giá trị của \(A+B\) tại \(x=1,\ y=2\).')]
review = (T(r'<b>Removing brackets.</b> \(+(a-b)=a-b\); \(-(a-b+c)=-a+b-c\).', r'<b>Quy tắc dấu ngoặc.</b> \(+(a-b)=a-b\); \(-(a-b+c)=-a+b-c\).') +
          T(r'<b>Simplifying (Lesson 2).</b> Combine like terms by adding their coefficients.', r'<b>Thu gọn đa thức (Bài 2).</b> Cộng các hạng tử đồng dạng bằng cách cộng các hệ số.'))

theory = '<h3>3.1 %s</h3>' % TI('Adding polynomials', 'Cộng hai đa thức')
theory += BOX('blue', ('Rule', 'Quy tắc'),
  T(r'To add \(A\) and \(B\): write \(A+B\) with brackets, remove the brackets, then combine like terms.', r'Muốn cộng hai đa thức \(A\) và \(B\), ta viết \(A+B\) (mỗi đa thức để trong ngoặc), bỏ dấu ngoặc rồi thu gọn các hạng tử đồng dạng.'),
  T(r'\((3x^2y+xy-1)+(x^2y-4xy+2)=3x^2y+xy-1+x^2y-4xy+2=4x^2y-3xy+1\).', r'\((3x^2y+xy-1)+(x^2y-4xy+2)=3x^2y+xy-1+x^2y-4xy+2=4x^2y-3xy+1\).'))
theory += '<h3>3.2 %s</h3>' % TI('Subtracting polynomials', 'Trừ hai đa thức')
theory += BOX('mint', ('Rule', 'Quy tắc'),
  T(r'To subtract \(B\) from \(A\): write \(A-B\) with brackets, remove the brackets — <b>changing the sign of every term of \(B\)</b> — then combine like terms.', r'Muốn trừ đa thức \(A\) cho đa thức \(B\), ta viết \(A-B\) (mỗi đa thức để trong ngoặc), bỏ dấu ngoặc — <b>đổi dấu tất cả các hạng tử của \(B\)</b> — rồi thu gọn.'),
  T(r'\((3x^2y+xy-1)-(x^2y-4xy+2)=3x^2y+xy-1-x^2y+4xy-2=2x^2y+5xy-3\).', r'\((3x^2y+xy-1)-(x^2y-4xy+2)=3x^2y+xy-1-x^2y+4xy-2=2x^2y+5xy-3\).'))
theory += BOX('blue', ('Properties', 'Tính chất'),
  T(r'Addition of polynomials is <b>commutative</b> and <b>associative</b>: \(A+B=B+A\), \((A+B)+C=A+(B+C)\). So we may regroup terms freely.', r'Phép cộng đa thức có [[tính chất giao hoán của phép cộng|tính chất giao hoán của phép cộng]] và [[tính chất kết hợp của phép cộng]]: \(A+B=B+A\), \((A+B)+C=A+(B+C)\); nhờ đó có thể nhóm các hạng tử tùy ý.'),
  T(r'Finding an unknown polynomial: \(M+B=C\Rightarrow M=C-B\); \(M-B=C\Rightarrow M=C+B\).', r'Tìm đa thức chưa biết: \(M+B=C\Rightarrow M=C-B\); \(M-B=C\Rightarrow M=C+B\).'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'),
  T(r'The minus sign in front of a bracket applies to <b>all</b> terms: \(-(x^2y-4xy+2)=-x^2y+4xy-2\), not \(-x^2y-4xy+2\).', r'Dấu trừ trước ngoặc áp dụng cho <b>tất cả</b> các hạng tử: \(-(x^2y-4xy+2)=-x^2y+4xy-2\), không phải \(-x^2y-4xy+2\).'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Adding', 'Cộng hai đa thức'),
  T(r'Find \(A+B\), given \(A=2x^2y+3xy-4\) and \(B=-xy+x^2-2x^2y+5\).', r'Cho \(A=2x^2y+3xy-4\) và \(B=-xy+x^2-2x^2y+5\). Tính \(A+B\).'),
  ('Remove the brackets, then group like terms.', 'Bỏ dấu ngoặc rồi nhóm các hạng tử đồng dạng.'),
  [T(r'\(A+B=2x^2y+3xy-4-xy+x^2-2x^2y+5\).', r'\(A+B=2x^2y+3xy-4-xy+x^2-2x^2y+5\).'),
   T(r'\(=(2x^2y-2x^2y)+(3xy-xy)+x^2+(-4+5)=2xy+x^2+1\).', r'\(=(2x^2y-2x^2y)+(3xy-xy)+x^2+(-4+5)=2xy+x^2+1\).')],
  T(r'\(A+B=x^2+2xy+1\).', r'\(A+B=x^2+2xy+1\).'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Subtracting', 'Trừ hai đa thức'),
  T(r'Find \(A-B\), given \(A=3x^2y^2-2xy+y\) and \(B=-x^2y^2+4xy-6\).', r'Cho \(A=3x^2y^2-2xy+y\) và \(B=-x^2y^2+4xy-6\). Tính \(A-B\).'),
  ('Change the sign of every term of \\(B\\).', 'Đổi dấu tất cả các hạng tử của \\(B\\).'),
  [T(r'\(A-B=(3x^2y^2-2xy+y)-(-x^2y^2+4xy-6)=3x^2y^2-2xy+y+x^2y^2-4xy+6\).', r'\(A-B=(3x^2y^2-2xy+y)-(-x^2y^2+4xy-6)=3x^2y^2-2xy+y+x^2y^2-4xy+6\).'),
   T(r'\(=4x^2y^2-6xy+y+6\).', r'\(=4x^2y^2-6xy+y+6\).')],
  T(r'\(A-B=4x^2y^2-6xy+y+6\).', r'\(A-B=4x^2y^2-6xy+y+6\).'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('Find the unknown polynomial', 'Tìm đa thức chưa biết'),
  T(r'Find the polynomial \(M\) such that \(M+(xyz-3x^2y+4x-1)=6x^2y+4x-2z+3\).', r'Tìm đa thức \(M\), biết \(M+(xyz-3x^2y+4x-1)=6x^2y+4x-2z+3\).'),
  ('\\(M\\) is a difference of two polynomials.', '\\(M\\) là hiệu của hai đa thức.'),
  [T(r'\(M=(6x^2y+4x-2z+3)-(xyz-3x^2y+4x-1)=6x^2y+4x-2z+3-xyz+3x^2y-4x+1\).', r'\(M=(6x^2y+4x-2z+3)-(xyz-3x^2y+4x-1)=6x^2y+4x-2z+3-xyz+3x^2y-4x+1\).'),
   T(r'\(=9x^2y-xyz-2z+4\).', r'\(=9x^2y-xyz-2z+4\).')],
  T(r'\(M=9x^2y-xyz-2z+4\).', r'\(M=9x^2y-xyz-2z+4\).'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Sum, difference, degree and value', 'Tổng, hiệu, bậc và giá trị'),
  T(r'Given \(A=2x^2y-3xyz+5x-2\) and \(B=-2x^2y+4xyz-x+3\). a) Find \(A+B\) and \(A-B\). b) Give their degrees. c) Evaluate both at \(x=1,\ y=2,\ z=-1\).', r'Cho \(A=2x^2y-3xyz+5x-2\) và \(B=-2x^2y+4xyz-x+3\). a) Tính \(A+B\) và \(A-B\). b) Tìm bậc của mỗi đa thức vừa tìm được. c) Tính giá trị của chúng tại \(x=1,\ y=2,\ z=-1\).'),
  ('Simplify first, then substitute.', 'Thu gọn trước, thay số sau.'),
  [T(r'a) \(A+B=xyz+4x+1\); \(A-B=4x^2y-7xyz+6x-5\).', r'a) \(A+B=xyz+4x+1\); \(A-B=4x^2y-7xyz+6x-5\).'),
   T(r'b) Both have degree \(3\) (the term \(xyz\), and the terms \(4x^2y\), \(-7xyz\)).', r'b) Cả hai đa thức đều có bậc \(3\).'),
   T(r'c) \(A+B=1\cdot2\cdot(-1)+4+1=3\); \(A-B=4\cdot2-7\cdot(-2)+6-5=23\).', r'c) \(A+B=1\cdot2\cdot(-1)+4+1=3\); \(A-B=4\cdot2-7\cdot(-2)+6-5=23\).')],
  T(r'\(A+B=xyz+4x+1=3\); \(A-B=4x^2y-7xyz+6x-5=23\); both of degree \(3\).', r'\(A+B=xyz+4x+1\), giá trị \(3\); \(A-B=4x^2y-7xyz+6x-5\), giá trị \(23\); cả hai có bậc \(3\).'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Profit of a workshop', 'Lợi nhuận của xưởng'),
  T(r'A workshop makes and sells \(x\) bags a day. Its revenue is \(R=-x^2+120x\) and its cost is \(C=20x+500\) (thousand VND). Write the profit \(L=R-C\) as a polynomial and find the profit when \(x=40\).', r'Một xưởng mỗi ngày làm và bán \(x\) chiếc túi. Doanh thu là \(R=-x^2+120x\), chi phí là \(C=20x+500\) (nghìn đồng). Viết đa thức biểu thị lợi nhuận \(L=R-C\) và tính lợi nhuận khi \(x=40\).'),
  ('Profit = revenue − cost.', 'Lợi nhuận = doanh thu − chi phí.'),
  [T(r'\(L=(-x^2+120x)-(20x+500)=-x^2+100x-500\).', r'\(L=(-x^2+120x)-(20x+500)=-x^2+100x-500\).'),
   T(r'\(x=40\): \(L=-1600+4000-500=1900\).', r'\(x=40\): \(L=-1600+4000-500=1900\).')],
  T(r'\(L=-x^2+100x-500\); the profit is 1,900 thousand VND (1.9 million VND).', r'\(L=-x^2+100x-500\); lợi nhuận là 1 900 nghìn đồng (1,9 triệu đồng).'))

_SETS = sp_g8.BANK(sp_g8.L3_GROUPS, start=1, seeds=(831, 832, 833))
practice = LEVEL_PRACTICE(sp_g8.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Changing only the first sign.</b> \(A-(x-y+2)=A-x+y-2\): every sign changes.', r'<b>Chỉ đổi dấu hạng tử đầu.</b> \(A-(x-y+2)=A-x+y-2\): đổi dấu tất cả.'),
 (r'<b>Adding unlike terms.</b> \(x^2y\) and \(xy^2\) stay separate.', r'<b>Cộng các hạng tử không đồng dạng.</b> \(x^2y\) và \(xy^2\) phải để riêng.'),
 (r'<b>Wrong order in subtraction.</b> \(A-B\ne B-A\); in fact \(B-A=-(A-B)\).', r'<b>Nhầm thứ tự khi trừ.</b> \(A-B\ne B-A\); thực ra \(B-A=-(A-B)\).'),
 (r'<b>\(M+B=C\Rightarrow M=C+B\).</b> Wrong: \(M=C-B\).', r'<b>\(M+B=C\Rightarrow M=C+B\).</b> Sai: \(M=C-B\).')]
summary = [
 (r'\(A+B\): remove the brackets, combine like terms.', r'\(A+B\): bỏ ngoặc, cộng các hạng tử đồng dạng.'),
 (r'\(A-B\): change the sign of every term of \(B\), then combine.', r'\(A-B\): đổi dấu mọi hạng tử của \(B\) rồi thu gọn.'),
 (r'Unknown polynomial: \(M+B=C\Rightarrow M=C-B\); \(M-B=C\Rightarrow M=C+B\).', r'Đa thức chưa biết: \(M+B=C\Rightarrow M=C-B\); \(M-B=C\Rightarrow M=C+B\).'),
 (r'Key English: sum, difference, remove brackets, like terms.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[tổng|tổng (lớp 8)]], [[hiệu]], [[bỏ dấu ngoặc|bỏ dấu ngoặc (lớp 8)]], [[các hạng tử đồng dạng]].')]
checks = [
 (r'I can add two polynomials.', r'Em cộng được hai đa thức.'),
 (r'I can subtract two polynomials without sign mistakes.', r'Em trừ được hai đa thức, không sai dấu.'),
 (r'I can find an unknown polynomial \(M\).', r'Em tìm được đa thức \(M\) chưa biết.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Adding and Subtracting Polynomials', title_vi='Phép cộng và phép trừ đa thức', topic=TOPIC,
       folder='polynomials', file='adding-subtracting-polynomials', catalog_title_vi='Phép cộng và phép trừ đa thức',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Adding and subtracting polynomials; finding an unknown polynomial.', level='Beginner', minutes=45,
       description_vi='Bài 3 – Cộng, trừ hai đa thức; quy tắc bỏ dấu ngoặc; tìm đa thức chưa biết.',
       tags_vi=['cộng đa thức', 'trừ đa thức', 'bỏ dấu ngoặc'],
       prerequisites=['g8-polynomials-02'], tags=['sum', 'difference', 'polynomial'], order=30)
