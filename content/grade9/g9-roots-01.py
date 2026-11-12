# -*- coding: utf-8 -*-
"""Nội dung bài g9-roots-01 = Toán 9 KNTT, Bài 7: Căn bậc hai và căn thức bậc hai – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 3 – Lesson 7, tr. 25–28."""
import os, sys, math
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9

LID = 'g9-roots-01'
CH = 'Căn bậc hai và căn bậc ba'
TOPIC = ('Square Roots and Cube Roots', CH)
ensure_vocab([
 ('g9-principal-root', 'principal square root', 'căn bậc hai số học', CH, 'The principal square root of 81 is 9, written √81 = 9.', r'\(\sqrt{a}\)'),
 ('g9-root-expr', 'square root expression', 'căn thức bậc hai', CH, '√(2x + 1) is a square root expression.', r'\(\sqrt{A}\)'),
 ('g9-radicand', 'radicand', 'biểu thức lấy căn', CH, 'The radicand of √(5 − 2x) is 5 − 2x.', ''),
 ('g9-nonneg', 'non-negative', 'không âm', CH, '√A is defined only when A is non-negative.', r'\(\ge 0\)'),
 ('g9-identity', 'identity', 'hằng đẳng thức', CH, 'Apply the identity √(A²) = |A|.', ''),
 ('g9-round2', 'round to two decimal places', 'làm tròn đến chữ số thập phân thứ hai', CH, 'Rounding to two decimal places, √11.1 ≈ 3.33.', ''),
 ('g9-perfect-sq', 'perfect square', 'số chính phương', CH, '49 is a perfect square: 49 = 7².', ''),
])
load_vocab()

# ---------- kiểm tra số liệu ----------
assert 9 * 9 == 81 and F(2, 3) ** 2 == F(4, 9)
assert abs(math.sqrt(11.1) - 3.33) < 0.005 and abs(math.sqrt(5) - 2) == math.sqrt(5) - 2
assert all(math.sqrt((1 - x) ** 2) == x - 1 for x in range(3, 30)) and math.sqrt((1 - 5) ** 2) == 4

meta = dict(level=('Beginner', 'Cơ bản'), time=('about 60 minutes', '60 phút'),
            before=('square roots and irrational numbers (grade 7); absolute value', 'căn bậc hai số học và số vô tỉ (lớp 7); giá trị tuyệt đối'))
goals = [
 (r'find the square roots of a number and the principal square root \(\sqrt{a}\);', r'tìm được [[căn bậc hai]] của một số và [[căn bậc hai số học]] \(\sqrt{a}\);'),
 (r'use a calculator and round square roots;', r'dùng máy tính cầm tay tính và làm tròn căn bậc hai;'),
 (r'find the condition for \(\sqrt{A}\) to be defined;', r'tìm được [[điều kiện xác định]] của [[căn thức bậc hai]] \(\sqrt{A}\);'),
 (r'apply the identity \(\sqrt{A^2}=|A|\) to compute and simplify.', r'vận dụng [[hằng đẳng thức]] \(\sqrt{A^2}=|A|\) để tính và rút gọn.')]
vocab = [
 (r'<b>square root of \(a\)</b> – a number \(x\) such that \(x^2=a\).', r'[[Căn bậc hai]] của \(a\) – số \(x\) sao cho \(x^2=a\).'),
 (r'<b>principal square root</b> \(\sqrt{a}\) – the non-negative square root of \(a\ge0\).', r'[[Căn bậc hai số học]] \(\sqrt{a}\) – căn bậc hai không âm của số \(a\ge0\).'),
 (r'<b>square root expression</b> \(\sqrt{A}\) – \(A\) is an algebraic expression.', r'[[Căn thức bậc hai]] \(\sqrt{A}\) – \(A\) là một biểu thức đại số.'),
 (r'<b>radicand</b> – the expression under the root sign.', r'[[Biểu thức lấy căn]] – biểu thức nằm dưới dấu căn.'),
 (r'<b>non-negative</b> – greater than or equal to 0.', r'[[Không âm]] – lớn hơn hoặc bằng 0.'),
 (r'<b>absolute value</b> \(|A|\) – \(A\) if \(A\ge0\), \(-A\) if \(A\lt0\).', r'[[Giá trị tuyệt đối]] \(|A|\) – bằng \(A\) nếu \(A\ge0\), bằng \(-A\) nếu \(A\lt0\).'),
 (r'<b>perfect square</b> – a number like \(49=7^2\).', r'[[Số chính phương]] – số như \(49=7^2\).')]
phrases = [
 (r'<b>\(\sqrt{81}=9\)</b>: “the square root of eighty-one equals nine”.', r'\(\sqrt{81}=9\): căn bậc hai số học của 81 bằng 9.'),
 (r'<b>How many square roots does 49 have?</b>', r'Số 49 có mấy căn bậc hai?'),
 (r'<b>For which values of \(x\) is \(\sqrt{A}\) defined?</b>', r'\(\sqrt{A}\) xác định với những giá trị nào của \(x\)?'),
 (r'<b>Applying the identity \(\sqrt{A^2}=|A|\), we obtain …</b>', r'Áp dụng hằng đẳng thức \(\sqrt{A^2}=|A|\), ta được …'),
 (r'<b>\(\sqrt{11.1}\approx 3.33\)</b>: “is approximately equal to”.', r'\(\sqrt{11{,}1}\approx 3{,}33\): xấp xỉ bằng.')]
review = (T(r'<b>Grade 7.</b> \(\sqrt{a}\) (for \(a\ge0\)) is the non-negative number whose square is \(a\): \(\sqrt{25}=5\). Numbers such as \(\sqrt{2}\) are irrational.', r'<b>Lớp 7.</b> \(\sqrt{a}\) (với \(a\ge0\)) là số không âm có bình phương bằng \(a\): \(\sqrt{25}=5\). Các số như \(\sqrt{2}\) là số vô tỉ.') +
          T(r'<b>Absolute value.</b> \(|3|=3\), \(|-3|=3\), \(|0|=0\).', r'<b>Giá trị tuyệt đối.</b> \(|3|=3\), \(|-3|=3\), \(|0|=0\).'))

theory = '<h3>5.1 %s</h3>' % TI('Square roots', 'Căn bậc hai')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'A <b>square root</b> of a number \(a\) is a number \(x\) such that \(x^2=a\).', r'[[Căn bậc hai]] của số thực \(a\) là số thực \(x\) sao cho \(x^2=a\).'),
  UL([T(r'A positive number \(a\) has exactly two square roots, which are opposite numbers: \(\sqrt{a}\) and \(-\sqrt{a}\).', r'Số dương \(a\) có đúng hai căn bậc hai là hai số đối nhau: \(\sqrt{a}\) và \(-\sqrt{a}\).'),
      T(r'The number 0 has exactly one square root: \(\sqrt{0}=0\).', r'Số 0 có đúng một căn bậc hai là \(\sqrt{0}=0\).'),
      T(r'A negative number has no square root.', r'Số âm không có căn bậc hai.')]),
  T(r'\(\sqrt{a}\) (with \(a\ge0\)) is the <b>principal square root</b> of \(a\). Example: the square roots of 81 are 9 and \(-9\); \(\sqrt{81}=9\).', r'\(\sqrt{a}\) (với \(a\ge0\)) là [[căn bậc hai số học]] của \(a\). Ví dụ: 81 có hai căn bậc hai là 9 và \(-9\); \(\sqrt{81}=9\).'))
theory += BOX('yellow', ('Calculator', 'Máy tính cầm tay'),
  T(r'Press the root key, then the number, then “=”. Example: \(\sqrt{11.1}\approx 3.33\) (rounded to two decimal places).', r'Bấm phím căn, nhập số rồi bấm “=”. Ví dụ: \(\sqrt{11{,}1}\approx 3{,}33\) (làm tròn đến chữ số thập phân thứ hai).'))
theory += '<h3>5.2 %s</h3>' % TI('Square root expressions', 'Căn thức bậc hai')
theory += BOX('mint', ('Definition', 'Định nghĩa'),
  T(r'If \(A\) is an algebraic expression, \(\sqrt{A}\) is a <b>square root expression</b> and \(A\) is its <b>radicand</b>.', r'Với \(A\) là một biểu thức đại số, ta gọi \(\sqrt{A}\) là [[căn thức bậc hai]] của \(A\); \(A\) là [[biểu thức lấy căn]].'),
  T(r'\(\sqrt{A}\) is defined only when \(A\ge0\). Example: \(\sqrt{2x+1}\) is defined when \(2x+1\ge0\), i.e. \(x\ge-\dfrac12\).', r'\(\sqrt{A}\) xác định khi và chỉ khi \(A\ge0\). Ví dụ: \(\sqrt{2x+1}\) xác định khi \(2x+1\ge0\), tức là \(x\ge-\dfrac12\).'))
theory += '<h3>5.3 %s</h3>' % TI('The identity √(A²) = |A|', 'Hằng đẳng thức √(A²) = |A|')
theory += BOX('blue', ('Identity', 'Hằng đẳng thức'),
  M(r'\sqrt{A^2}=|A|=\begin{cases}A & \text{if } A\ge0\\ -A & \text{if } A\lt0\end{cases}'.replace('\\text{if }', '')),
  T(r'Examples: \(\sqrt{7^2}=7\); \(\sqrt{(-7)^2}=|-7|=7\); \(\sqrt{(2-\sqrt5)^2}=|2-\sqrt5|=\sqrt5-2\) because \(2\lt\sqrt5\).', r'Ví dụ: \(\sqrt{7^2}=7\); \(\sqrt{(-7)^2}=|-7|=7\); \(\sqrt{(2-\sqrt5)^2}=|2-\sqrt5|=\sqrt5-2\) vì \(2\lt\sqrt5\).'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'),
  T(r'\(\sqrt{A^2}=A\) is true only when \(A\ge0\). For \(A\lt0\), \(\sqrt{A^2}=-A\).', r'\(\sqrt{A^2}=A\) chỉ đúng khi \(A\ge0\). Khi \(A\lt0\) thì \(\sqrt{A^2}=-A\).'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Square roots of a number', 'Căn bậc hai của một số'),
  T(r'Find the square roots of \(81\), \(\dfrac{4}{9}\), \(0\) and \(-16\).', r'Tìm các căn bậc hai của \(81\), \(\dfrac{4}{9}\), \(0\) và \(-16\).'),
  ('Positive: two opposite roots; 0: one root; negative: none.', 'Số dương: hai căn đối nhau; số 0: một căn; số âm: không có.'),
  [T(r'\(81\): \(9\) and \(-9\). \(\dfrac49\): \(\dfrac23\) and \(-\dfrac23\).', r'\(81\): \(9\) và \(-9\). \(\dfrac49\): \(\dfrac23\) và \(-\dfrac23\).'),
   T(r'\(0\): only \(0\). \(-16\): no square root.', r'\(0\): chỉ có \(0\). \(-16\): không có căn bậc hai.')],
  T(r'\(\pm9\); \(\pm\dfrac23\); \(0\); none.', r'\(\pm9\); \(\pm\dfrac23\); \(0\); không có.'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('When is it defined?', 'Điều kiện xác định'),
  T(r'Find the condition for each expression to be defined: a) \(\sqrt{2x+1}\); b) \(\sqrt{5-2x}\).', r'Tìm điều kiện xác định của mỗi căn thức: a) \(\sqrt{2x+1}\); b) \(\sqrt{5-2x}\).'),
  ('The radicand must be non-negative.', 'Biểu thức lấy căn phải không âm.'),
  [T(r'a) \(2x+1\ge0\Leftrightarrow x\ge-\dfrac12\).', r'a) \(2x+1\ge0\Leftrightarrow x\ge-\dfrac12\).'),
   T(r'b) \(5-2x\ge0\Leftrightarrow -2x\ge-5\Leftrightarrow x\le\dfrac52\) (dividing by \(-2\) reverses the sign).', r'b) \(5-2x\ge0\Leftrightarrow -2x\ge-5\Leftrightarrow x\le\dfrac52\) (chia cho \(-2\) thì đổi chiều).')],
  T(r'a) \(x\ge-\dfrac12\); b) \(x\le\dfrac52\).', r'a) \(x\ge-\dfrac12\); b) \(x\le\dfrac52\).'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('Using √(A²) = |A|', 'Áp dụng √(A²) = |A|'),
  T(r'Compute a) \(\sqrt{(-7)^2}\); b) \(\sqrt{(2-\sqrt5)^2}\).', r'Tính a) \(\sqrt{(-7)^2}\); b) \(\sqrt{(2-\sqrt5)^2}\).'),
  ('Decide the sign of the expression inside the square.', 'Xét dấu biểu thức bên trong bình phương.'),
  [T(r'a) \(\sqrt{(-7)^2}=|-7|=7\).', r'a) \(\sqrt{(-7)^2}=|-7|=7\).'),
   T(r'b) \(2=\sqrt4\lt\sqrt5\), so \(2-\sqrt5\lt0\) and \(\sqrt{(2-\sqrt5)^2}=\sqrt5-2\).', r'b) \(2=\sqrt4\lt\sqrt5\) nên \(2-\sqrt5\lt0\); do đó \(\sqrt{(2-\sqrt5)^2}=\sqrt5-2\).')],
  T(r'a) \(7\); b) \(\sqrt5-2\).', r'a) \(7\); b) \(\sqrt5-2\).'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Simplify an expression', 'Rút gọn căn thức'),
  T(r'Consider \(A=\sqrt{1-2x+x^2}\). a) Find the condition for \(A\) to be defined. b) Simplify \(A\) for \(x\gt2\). c) Find \(A\) at \(x=5\).', r'Cho \(A=\sqrt{1-2x+x^2}\). a) Tìm điều kiện xác định của \(A\). b) Rút gọn \(A\) với \(x\gt2\). c) Tính giá trị của \(A\) tại \(x=5\).'),
  ('\\(1-2x+x^2=(1-x)^2\\).', '\\(1-2x+x^2=(1-x)^2\\).'),
  [T(r'a) \((1-x)^2\ge0\) for every \(x\), so \(A\) is defined for all real \(x\).', r'a) \((1-x)^2\ge0\) với mọi \(x\) nên \(A\) xác định với mọi số thực \(x\).'),
   T(r'b) \(A=|1-x|\). For \(x\gt2\), \(1-x\lt0\), so \(A=x-1\).', r'b) \(A=|1-x|\). Với \(x\gt2\) thì \(1-x\lt0\) nên \(A=x-1\).'),
   T(r'c) At \(x=5\): \(A=5-1=4\).', r'c) Tại \(x=5\): \(A=5-1=4\).')],
  T(r'a) all \(x\); b) \(A=x-1\); c) \(4\).', r'a) mọi \(x\); b) \(A=x-1\); c) \(4\).'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('A square carpet', 'Tấm thảm hình vuông'),
  T(r'A square carpet has an area of \(11.1\) m². Find the length of its side, rounded to two decimal places.', r'Một tấm thảm hình vuông có diện tích \(11{,}1\) m². Tính độ dài cạnh tấm thảm (làm tròn đến chữ số thập phân thứ hai).'),
  ('The side \\(x\\gt0\\) satisfies \\(x^2=11.1\\).', 'Cạnh \\(x\\gt0\\) thỏa mãn \\(x^2=11{,}1\\).'),
  [T(r'\(x^2=11.1\) and \(x\gt0\), so \(x=\sqrt{11.1}\).', r'\(x^2=11{,}1\) và \(x\gt0\) nên \(x=\sqrt{11{,}1}\).'),
   T(r'With a calculator: \(\sqrt{11.1}=3.3316\ldots\approx3.33\).', r'Dùng máy tính: \(\sqrt{11{,}1}=3{,}3316\ldots\approx3{,}33\).')],
  T(r'The side is about \(3.33\) m.', r'Cạnh tấm thảm khoảng \(3{,}33\) m.'))

_SETS = sp_g9.BANK(sp_g9.L7_GROUPS, start=1, seeds=(1701, 1702, 1703))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Writing \(\sqrt{81}=\pm9\).</b> \(\sqrt{81}=9\) only; the square roots of 81 are \(\pm9\).', r'<b>Viết \(\sqrt{81}=\pm9\).</b> \(\sqrt{81}=9\); còn các căn bậc hai của 81 là \(\pm9\).'),
 (r'<b>Taking the square root of a negative number.</b> \(\sqrt{-16}\) has no meaning.', r'<b>Lấy căn của số âm.</b> \(\sqrt{-16}\) không có nghĩa.'),
 (r'<b>Writing \(\sqrt{A^2}=A\) without checking the sign.</b> \(\sqrt{(-5)^2}=5\), not \(-5\).', r'<b>Viết \(\sqrt{A^2}=A\) mà không xét dấu.</b> \(\sqrt{(-5)^2}=5\), không phải \(-5\).'),
 (r'<b>Forgetting to reverse the sign</b> when solving \(5-2x\ge0\): the answer is \(x\le\dfrac52\).', r'<b>Quên đổi chiều</b> khi giải \(5-2x\ge0\): kết quả là \(x\le\dfrac52\).'),
 (r'<b>Rounding too early.</b> Round only the final answer.', r'<b>Làm tròn quá sớm.</b> Chỉ làm tròn ở kết quả cuối cùng.')]
summary = [
 (r'\(a\gt0\): two square roots \(\pm\sqrt a\); \(a=0\): one; \(a\lt0\): none. \(\sqrt a\) is the principal (non-negative) root.', r'\(a\gt0\): hai căn bậc hai \(\pm\sqrt a\); \(a=0\): một căn; \(a\lt0\): không có. \(\sqrt a\) là căn bậc hai số học (không âm).'),
 (r'\(\sqrt{A}\) is defined when \(A\ge0\).', r'\(\sqrt{A}\) xác định khi \(A\ge0\).'),
 (r'\(\sqrt{A^2}=|A|\).', r'\(\sqrt{A^2}=|A|\).'),
 (r'Key English: square root, principal square root, radicand, non-negative.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[căn bậc hai]], [[căn bậc hai số học]], [[biểu thức lấy căn]], [[không âm]].')]
checks = [
 (r'I can find the square roots of a number.', r'Em tìm được căn bậc hai của một số.'),
 (r'I can find the condition for \(\sqrt{A}\) to be defined.', r'Em tìm được điều kiện xác định của \(\sqrt{A}\).'),
 (r'I can use \(\sqrt{A^2}=|A|\) to compute and simplify.', r'Em vận dụng được \(\sqrt{A^2}=|A|\) để tính và rút gọn.'),
 (r'I can use a calculator and round correctly.', r'Em dùng được máy tính cầm tay và làm tròn đúng.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Square Roots and Square Root Expressions', title_vi='Căn bậc hai và căn thức bậc hai', topic=TOPIC,
       folder='square-and-cube-roots', file='square-roots', catalog_title_vi='Căn bậc hai và căn thức bậc hai',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Square roots, principal square roots, square root expressions and the identity √(A²) = |A|.', level='Beginner', minutes=60,
       description_vi='Bài 7 – Căn bậc hai, căn bậc hai số học, căn thức bậc hai, điều kiện xác định và hằng đẳng thức √(A²) = |A|.',
       tags_vi=['căn bậc hai', 'căn thức', 'điều kiện xác định', 'giá trị tuyệt đối'],
       prerequisites=[], tags=['square root', 'radicand', 'absolute value'], order=70)
