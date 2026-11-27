# -*- coding: utf-8 -*-
"""Nội dung bài g8-identities-01 = Toán 8 KNTT, Bài 6: Hiệu hai bình phương. Bình phương của một tổng hay một hiệu – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 8 (2026), Chapter 2 – Lesson 6, tr. 23–25; Part 3 – Difference of Two Squares (tr. 163)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
from mb_pgf import texsvg, img
import sp_g8
from sp_g8 import Poly, M, L

LID = 'g8-identities-01'
CH = 'Hằng đẳng thức đáng nhớ và ứng dụng'
TOPIC = ('Algebraic Identities and Applications', CH)
ensure_vocab([
 ('g8-square', 'square', 'bình phương (lớp 8)', CH, 'The square of 3x is 9x².', ''),
 ('g8-diff-squares', 'difference of two squares', 'hiệu hai bình phương (lớp 8)', CH, 'A² − B² is the difference of two squares.', ''),
 ('g8-square-sum', 'square of a sum', 'bình phương của một tổng', CH, '(A + B)² is the square of a sum.', ''),
 ('g8-square-diff', 'square of a difference', 'bình phương của một hiệu (lớp 8)', CH, '(A − B)² is the square of a difference.', ''),
])
load_vocab()

SQ = texsvg('\n'.join([
 '\\begin{tikzpicture}[x=1cm,y=1cm,font=\\small]',
 '\\fill[blue!8] (0,0) rectangle (2.6,2.6); \\fill[green!10] (2.6,0) rectangle (3.8,2.6); \\fill[green!10] (0,2.6) rectangle (2.6,3.8); \\fill[orange!14] (2.6,2.6) rectangle (3.8,3.8);',
 '\\draw[thick] (0,0) rectangle (3.8,3.8); \\draw (2.6,0)--(2.6,3.8); \\draw (0,2.6)--(3.8,2.6);',
 '\\node at (1.3,1.3) {$a^2$}; \\node at (3.2,1.3) {$ab$}; \\node at (1.3,3.2) {$ab$}; \\node at (3.2,3.2) {$b^2$};',
 '\\draw[<->] (0,-0.35)--(2.6,-0.35) node[midway,below] {$a$}; \\draw[<->] (2.6,-0.35)--(3.8,-0.35) node[midway,below] {$b$};',
 '\\draw[<->] (-0.35,0)--(-0.35,2.6) node[midway,left] {$a$}; \\draw[<->] (-0.35,2.6)--(-0.35,3.8) node[midway,left] {$b$};',
 '\\end{tikzpicture}']))

# ---------- kiểm tra số liệu ----------
X = lambda c, a, b: (c, (a, b, 0))
from fractions import Fraction as F
P = Poly.of([X(2, 1, 0), X(3, 0, 1)]); assert P * P == Poly.of([X(4, 2, 0), X(12, 1, 1), X(9, 0, 2)])          # Ví dụ 2
Q = L(1, F(-1, 2)); assert Q * Q == Poly.of([X(1, 2, 0), X(-1, 1, 0), X(F(1, 4), 0, 0)])
assert L(3, -1, (1, 0, 0), (0, 1, 0)) * L(3, 1, (1, 0, 0), (0, 1, 0)) == Poly.of([X(9, 2, 0), X(-1, 0, 2)])
assert L(1, -3) * L(1, -3) == Poly.of([X(1, 2, 0), X(-6, 1, 0), X(9, 0, 0)])                                   # Ví dụ 3
assert 103 ** 2 == 10609 and 98 * 102 == 9996 and 49 ** 2 == 2401                                                # Ví dụ 4
assert (10 + 3) ** 2 - 10 ** 2 == 69                                                                              # Ví dụ 5

meta = dict(level=('Beginner', 'Cơ bản'), time=('about 60 minutes', '60 phút'),
            before=('multiplying polynomials (Lesson 4)', 'phép nhân đa thức (Bài 4)'))
goals = [
 (r'recognize an identity;', r'nhận biết được [[hằng đẳng thức]];'),
 (r'state and use the identities \(A^2-B^2\), \((A+B)^2\), \((A-B)^2\);', r'phát biểu và sử dụng được các hằng đẳng thức [[hiệu hai bình phương|hiệu hai bình phương (lớp 8)]], [[bình phương của một tổng]], [[bình phương của một hiệu|bình phương của một hiệu (lớp 8)]];'),
 (r'expand expressions and write expressions as products or squares;', r'[[khai triển]] biểu thức và viết biểu thức dưới dạng tích hoặc bình phương;'),
 (r'calculate quickly and solve simple problems with these identities.', r'tính nhanh và giải bài toán đơn giản bằng các hằng đẳng thức.')]
vocab = [
 (r'<b>identity</b> – an equality \(A=B\) that is true for all values of the variables.', r'[[Hằng đẳng thức]] – đẳng thức \(A=B\) đúng với mọi giá trị của các biến.'),
 (r'<b>left-hand side (LHS) / right-hand side (RHS)</b> – the expressions on the left and on the right of "=".', r'[[Vế trái]] / [[vế phải]] – biểu thức ở bên trái và bên phải dấu "=".'),
 (r'<b>square</b> – \(A^2\); for example, the square of \(3x\) is \(9x^2\).', r'[[Bình phương|bình phương (lớp 8)]] – \(A^2\); ví dụ bình phương của \(3x\) là \(9x^2\).'),
 (r'<b>difference of two squares</b> – \(A^2-B^2=(A-B)(A+B)\).', r'[[Hiệu hai bình phương|hiệu hai bình phương (lớp 8)]] – \(A^2-B^2=(A-B)(A+B)\).'),
 (r'<b>square of a sum</b> – \((A+B)^2=A^2+2AB+B^2\).', r'[[Bình phương của một tổng]] – \((A+B)^2=A^2+2AB+B^2\).'),
 (r'<b>square of a difference</b> – \((A-B)^2=A^2-2AB+B^2\).', r'[[Bình phương của một hiệu|bình phương của một hiệu (lớp 8)]] – \((A-B)^2=A^2-2AB+B^2\).'),
 (r'<b>expand</b> – write a product or a power as a sum.', r'[[Khai triển]] – viết một tích hay một lũy thừa thành tổng.')]
phrases = [
 (r'<b>Which of the following equations are identities?</b>', r'Đẳng thức nào là hằng đẳng thức?'),
 (r'<b>Calculate using identities.</b>', r'Tính bằng cách dùng hằng đẳng thức.'),
 (r'<b>Expand the expressions.</b>', r'Khai triển các biểu thức.'),
 (r'<b>Write the expressions as products / squares.</b>', r'Viết các biểu thức dưới dạng tích / bình phương.'),
 (r'<b>Prove that the equation is true for every value of the variables.</b>', r'Chứng minh đẳng thức đúng với mọi giá trị của các biến.'),
 (r'<b>\(A^2-B^2\)</b> is read "the difference of two squares"; <b>\((A+B)^2\)</b> "the square of a sum"; <b>\((A-B)^2\)</b> "the square of a difference".', r'Cách đọc: \(A^2-B^2\) – hiệu hai bình phương; \((A+B)^2\) – bình phương của một tổng; \((A-B)^2\) – bình phương của một hiệu.')]
review = (T(r'<b>Multiplying polynomials (Lesson 4).</b> \((a+b)(c+d)=ac+ad+bc+bd\).', r'<b>Nhân hai đa thức (Bài 4).</b> \((a+b)(c+d)=ac+ad+bc+bd\).') +
          T(r'<b>Squares.</b> \((3x)^2=9x^2\), \((-2y)^2=4y^2\).', r'<b>Bình phương.</b> \((3x)^2=9x^2\), \((-2y)^2=4y^2\).'))

theory = '<h3>6.1 %s</h3>' % TI('Identities', 'Hằng đẳng thức')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'An <b>identity</b> is an equality \(A=B\) whose two sides always take the same value for every value of the variables.', r'[[Hằng đẳng thức]] là đẳng thức có dạng \(A=B\), trong đó hai vế luôn nhận cùng một giá trị với mọi giá trị của biến.'),
  T(r'\(x(x+2)=x^2+2x\) is an identity; \(2x+1=3x\) is not (it is true only for \(x=1\)).', r'\(x(x+2)=x^2+2x\) là hằng đẳng thức; \(2x+1=3x\) không phải (chỉ đúng khi \(x=1\)).'))
theory += '<h3>6.2 %s</h3>' % TI('Three identities', 'Ba hằng đẳng thức')
theory += BOX('mint', ('Identities', 'Hằng đẳng thức đáng nhớ'),
  T(r'<b>Difference of two squares:</b> \(A^2-B^2=(A-B)(A+B)\).', r'<b>[[Hiệu hai bình phương|hiệu hai bình phương (lớp 8)]]:</b> \(A^2-B^2=(A-B)(A+B)\).'),
  T(r'<b>Square of a sum:</b> \((A+B)^2=A^2+2AB+B^2\).', r'<b>[[Bình phương của một tổng]]:</b> \((A+B)^2=A^2+2AB+B^2\).'),
  T(r'<b>Square of a difference:</b> \((A-B)^2=A^2-2AB+B^2\).', r'<b>[[Bình phương của một hiệu|bình phương của một hiệu (lớp 8)]]:</b> \((A-B)^2=A^2-2AB+B^2\).'),
  T(r'\(A\) and \(B\) may be numbers, variables or expressions: \((2x+3y)^2=(2x)^2+2\cdot2x\cdot3y+(3y)^2\).', r'\(A\), \(B\) có thể là số, biến hoặc biểu thức: \((2x+3y)^2=(2x)^2+2\cdot2x\cdot3y+(3y)^2\).'),
  img(SQ, 'Area model of (a+b)^2', 230, TI('A square of side \\(a+b\\) is made of \\(a^2\\), two rectangles \\(ab\\) and \\(b^2\\).', 'Hình vuông cạnh \\(a+b\\) gồm \\(a^2\\), hai hình chữ nhật \\(ab\\) và \\(b^2\\).')))
theory += BOX('blue', ('Two directions', 'Hai chiều sử dụng'),
  T(r'Left to right: <b>expand</b>, e.g. \((x-5)^2=x^2-10x+25\). Right to left: <b>write as a product or a square</b>, e.g. \(x^2-10x+25=(x-5)^2\), \(9-y^2=(3-y)(3+y)\).', r'Từ trái sang phải: <b>khai triển</b>, chẳng hạn \((x-5)^2=x^2-10x+25\). Từ phải sang trái: <b>viết thành tích hoặc bình phương</b>, chẳng hạn \(x^2-10x+25=(x-5)^2\), \(9-y^2=(3-y)(3+y)\).'),
  T(r'Quick calculation: \(51^2=(50+1)^2=2601\); \(29\cdot31=30^2-1^2=899\).', r'Tính nhanh: \(51^2=(50+1)^2=2601\); \(29\cdot31=30^2-1^2=899\).'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'),
  T(r'\((A+B)^2\ne A^2+B^2\): never forget the middle term \(2AB\). Also \((A-B)^2=(B-A)^2\).', r'\((A+B)^2\ne A^2+B^2\): không được quên hạng tử \(2AB\). Ngoài ra \((A-B)^2=(B-A)^2\).'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Identity or not?', 'Có phải hằng đẳng thức?'),
  T(r'Which equalities are identities? a) \(x(x+2)=x^2+2x\); b) \(2x+1=3x\); c) \((x+1)^2=x^2+2x+1\); d) \(x^2-4=0\).', r'Đẳng thức nào là hằng đẳng thức? a) \(x(x+2)=x^2+2x\); b) \(2x+1=3x\); c) \((x+1)^2=x^2+2x+1\); d) \(x^2-4=0\).'),
  ('Check whether both sides are equal for every \\(x\\).', 'Kiểm tra hai vế có bằng nhau với mọi \\(x\\) hay không.'),
  [T(r'a) and c): expanding the left side gives the right side for every \(x\).', r'a) và c): khai triển vế trái được đúng vế phải với mọi \(x\).'),
   T(r'b) is true only for \(x=1\); d) only for \(x=\pm2\).', r'b) chỉ đúng khi \(x=1\); d) chỉ đúng khi \(x=\pm2\).')],
  T(r'a) and c) are identities.', r'a) và c) là hằng đẳng thức.'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Expand', 'Khai triển'),
  T(r'Expand: a) \((2x+3y)^2\); b) \(\left(x-\dfrac{1}{2}\right)^2\); c) \((3x-y)(3x+y)\).', r'Khai triển: a) \((2x+3y)^2\); b) \(\left(x-\dfrac{1}{2}\right)^2\); c) \((3x-y)(3x+y)\).'),
  ('Identify \\(A\\) and \\(B\\) first.', 'Xác định \\(A\\) và \\(B\\) trước.'),
  [T(r'a) \(A=2x,\ B=3y\): \(4x^2+12xy+9y^2\).', r'a) \(A=2x,\ B=3y\): \(4x^2+12xy+9y^2\).'),
   T(r'b) \(A=x,\ B=\dfrac{1}{2}\): \(x^2-x+\dfrac{1}{4}\).', r'b) \(A=x,\ B=\dfrac{1}{2}\): \(x^2-x+\dfrac{1}{4}\).'),
   T(r'c) \((A-B)(A+B)=A^2-B^2\): \(9x^2-y^2\).', r'c) \((A-B)(A+B)=A^2-B^2\): \(9x^2-y^2\).')],
  T(r'\(4x^2+12xy+9y^2\); \(x^2-x+\dfrac{1}{4}\); \(9x^2-y^2\).', r'\(4x^2+12xy+9y^2\); \(x^2-x+\dfrac{1}{4}\); \(9x^2-y^2\).'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('Write as a square or a product', 'Viết thành bình phương hoặc tích'),
  T(r'Write as a square or a product: a) \(x^2-6x+9\); b) \(4x^2+4xy+y^2\); c) \(25-16y^2\).', r'Viết dưới dạng bình phương hoặc tích: a) \(x^2-6x+9\); b) \(4x^2+4xy+y^2\); c) \(25-16y^2\).'),
  ('Look for \\(A^2\\), \\(B^2\\) and the middle term \\(2AB\\).', 'Tìm \\(A^2\\), \\(B^2\\) và hạng tử \\(2AB\\).'),
  [T(r'a) \(x^2-2\cdot x\cdot3+3^2=(x-3)^2\).', r'a) \(x^2-2\cdot x\cdot3+3^2=(x-3)^2\).'),
   T(r'b) \((2x)^2+2\cdot2x\cdot y+y^2=(2x+y)^2\).', r'b) \((2x)^2+2\cdot2x\cdot y+y^2=(2x+y)^2\).'),
   T(r'c) \(5^2-(4y)^2=(5-4y)(5+4y)\).', r'c) \(5^2-(4y)^2=(5-4y)(5+4y)\).')],
  T(r'\((x-3)^2\); \((2x+y)^2\); \((5-4y)(5+4y)\).', r'\((x-3)^2\); \((2x+y)^2\); \((5-4y)(5+4y)\).'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Calculate quickly', 'Tính nhanh'),
  T(r'Calculate quickly: a) \(103^2\); b) \(98\cdot102\); c) \(49^2\).', r'Tính nhanh: a) \(103^2\); b) \(98\cdot102\); c) \(49^2\).'),
  ('Write each number using a round number.', 'Viết mỗi số qua một số tròn trăm, tròn chục.'),
  [T(r'a) \((100+3)^2=10000+600+9=10609\).', r'a) \((100+3)^2=10000+600+9=10609\).'),
   T(r'b) \((100-2)(100+2)=10000-4=9996\).', r'b) \((100-2)(100+2)=10000-4=9996\).'),
   T(r'c) \((50-1)^2=2500-100+1=2401\).', r'c) \((50-1)^2=2500-100+1=2401\).')],
  T(r'\(10609\); \(9996\); \(2401\).', r'\(10609\); \(9996\); \(2401\).'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Enlarging a square garden', 'Mở rộng vườn hình vuông'),
  T(r'A square garden has side \(x\) m. Each side is increased by 3 m and the area increases by 69 m². Find \(x\).', r'Một mảnh vườn hình vuông cạnh \(x\) m. Mở rộng mỗi cạnh thêm 3 m thì diện tích tăng thêm 69 m². Tìm \(x\).'),
  ('Increase = new area − old area.', 'Phần tăng thêm = diện tích mới − diện tích cũ.'),
  [T(r'\((x+3)^2-x^2=x^2+6x+9-x^2=6x+9\).', r'\((x+3)^2-x^2=x^2+6x+9-x^2=6x+9\).'),
   T(r'\(6x+9=69\Rightarrow 6x=60\Rightarrow x=10\).', r'\(6x+9=69\Rightarrow 6x=60\Rightarrow x=10\).')],
  T(r'\(x=10\) m.', r'Cạnh vườn ban đầu là \(10\) m.'))

_SETS = sp_g8.BANK(sp_g8.L6_GROUPS, start=1, seeds=(861, 862, 863))
practice = LEVEL_PRACTICE(sp_g8.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Forgetting \(2AB\).</b> \((x+5)^2=x^2+10x+25\), not \(x^2+25\).', r'<b>Quên hạng tử \(2AB\).</b> \((x+5)^2=x^2+10x+25\), không phải \(x^2+25\).'),
 (r'<b>Squaring only the variable.</b> \((3x)^2=9x^2\), not \(3x^2\).', r'<b>Chỉ bình phương biến.</b> \((3x)^2=9x^2\), không phải \(3x^2\).'),
 (r'<b>Confusing \((A-B)^2\) with \(A^2-B^2\).</b> \((x-2)^2=x^2-4x+4\), while \(x^2-4=(x-2)(x+2)\).', r'<b>Nhầm \((A-B)^2\) với \(A^2-B^2\).</b> \((x-2)^2=x^2-4x+4\), còn \(x^2-4=(x-2)(x+2)\).'),
 (r'<b>Wrong sign of \(2AB\).</b> In \((A-B)^2\) the middle term is \(-2AB\).', r'<b>Sai dấu của \(2AB\).</b> Trong \((A-B)^2\), hạng tử giữa là \(-2AB\).')]
summary = [
 (r'\(A^2-B^2=(A-B)(A+B)\).', r'\(A^2-B^2=(A-B)(A+B)\).'),
 (r'\((A+B)^2=A^2+2AB+B^2\); \((A-B)^2=A^2-2AB+B^2\).', r'\((A+B)^2=A^2+2AB+B^2\); \((A-B)^2=A^2-2AB+B^2\).'),
 (r'Use them both ways: to expand and to write as a product / square; also for quick calculation.', r'Dùng theo hai chiều: khai triển và viết thành tích / bình phương; dùng để tính nhanh.'),
 (r'Key English: identity, difference of two squares, square of a sum, square of a difference, expand.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[hằng đẳng thức]], [[hiệu hai bình phương|hiệu hai bình phương (lớp 8)]], [[bình phương của một tổng]], [[bình phương của một hiệu|bình phương của một hiệu (lớp 8)]], [[khai triển]].')]
checks = [
 (r'I can recognize an identity.', r'Em nhận biết được hằng đẳng thức.'),
 (r'I can expand \((A\pm B)^2\) and \((A-B)(A+B)\).', r'Em khai triển được \((A\pm B)^2\) và \((A-B)(A+B)\).'),
 (r'I can write a polynomial as a square or as a product.', r'Em viết được đa thức dưới dạng bình phương hoặc tích.'),
 (r'I can calculate quickly using identities.', r'Em tính nhanh được bằng hằng đẳng thức.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Difference of Two Squares. Square of a Sum or a Difference', title_vi='Hiệu hai bình phương. Bình phương của một tổng hay một hiệu', topic=TOPIC,
       folder='identities', file='squares-identities', catalog_title_vi='Hiệu hai bình phương. Bình phương của một tổng hay một hiệu',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Identities: difference of two squares, square of a sum, square of a difference.', level='Beginner', minutes=60,
       description_vi='Bài 6 – Hằng đẳng thức; hiệu hai bình phương; bình phương của một tổng, một hiệu; tính nhanh.',
       tags_vi=['hằng đẳng thức', 'hiệu hai bình phương', 'bình phương của một tổng'],
       prerequisites=['g8-polynomials-04'], tags=['identity', 'difference of two squares', 'square of a sum'], order=60)
