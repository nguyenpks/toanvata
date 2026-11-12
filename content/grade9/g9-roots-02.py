# -*- coding: utf-8 -*-
"""Nội dung bài g9-roots-02 = Toán 9 KNTT, Bài 8: Khai căn bậc hai với phép nhân và phép chia – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 3 – Lesson 8, tr. 29–32."""
import os, sys, math
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9

LID = 'g9-roots-02'
CH = 'Căn bậc hai và căn bậc ba'
TOPIC = ('Square Roots and Cube Roots', CH)
ensure_vocab([
 ('g9-take-root', 'take the square root', 'khai căn bậc hai', CH, 'Take the square root of each factor.', ''),
 ('g9-product', 'product', 'tích', CH, 'The square root of a product equals the product of the square roots.', ''),
 ('g9-holds', 'the rule holds when …', 'quy tắc đúng khi', CH, 'The rule √(AB) = √A·√B holds when A ≥ 0 and B ≥ 0.', ''),
 ('g9-strict-pos', 'strictly positive', 'dương', CH, 'The denominator B must be strictly positive: B > 0.', r'\(\gt 0\)'),
 ('g9-take-out', 'take out of the root sign', 'đưa ra ngoài dấu căn', CH, '√(25a²b²) = 5|ab|: take 5|ab| out of the root sign.', ''),
])
load_vocab()

# ---------- kiểm tra số liệu ----------
assert math.isqrt(4 * 9 * 25) ** 2 == 900 and F(5, 7) ** 2 == F(25, 49)
assert math.isqrt(5 * 125) == 25 and 25 + 5 == 30 and math.isqrt(50 // 2) == 5
assert math.isqrt(60 * 15) == 30 and 30 * 30 == 900

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 60 minutes', '60 phút'),
            before=('Lesson 7: square roots and the identity √(A²) = |A|', 'Bài 7: căn bậc hai và hằng đẳng thức √(A²) = |A|'))
goals = [
 (r'use \(\sqrt{AB}=\sqrt A\cdot\sqrt B\) (\(A, B\ge0\)) in both directions;', r'vận dụng được \(\sqrt{AB}=\sqrt A\cdot\sqrt B\) (\(A, B\ge0\)) theo cả hai chiều;'),
 (r'use \(\sqrt{\dfrac AB}=\dfrac{\sqrt A}{\sqrt B}\) (\(A\ge0,\ B\gt0\)) in both directions;', r'vận dụng được \(\sqrt{\dfrac AB}=\dfrac{\sqrt A}{\sqrt B}\) (\(A\ge0,\ B\gt0\)) theo cả hai chiều;'),
 (r'compute and simplify expressions with square roots, paying attention to signs;', r'tính và rút gọn biểu thức chứa căn, chú ý dấu của biểu thức;'),
 (r'use these rules in formulas from physics and geometry.', r'vận dụng trong công thức vật lí và hình học.')]
vocab = [
 (r'<b>take the square root</b> – find \(\sqrt{\ }\) of a number or an expression.', r'[[Khai căn bậc hai]] – tìm căn bậc hai số học của một số hay một biểu thức.'),
 (r'<b>product / quotient</b> – the result of a multiplication / a division.', r'[[Tích]] / [[thương]] – kết quả của phép nhân / phép chia.'),
 (r'<b>the rule holds when …</b> – the conditions for the rule to be true.', r'[[Quy tắc đúng khi]] … – các điều kiện để quy tắc đúng.'),
 (r'<b>strictly positive</b> – greater than 0 (not equal to 0).', r'[[Dương]] – lớn hơn 0 (khác 0).'),
 (r'<b>take out of the root sign</b> – write \(\sqrt{9a^2}=3|a|\).', r'[[Đưa ra ngoài dấu căn]] – viết \(\sqrt{9a^2}=3|a|\).')]
phrases = [
 (r'<b>\(\sqrt{A}\cdot\sqrt{B}=\sqrt{AB}\)</b>: “root A times root B equals root of A B”.', r'\(\sqrt{A}\cdot\sqrt{B}=\sqrt{AB}\).'),
 (r'<b>The rule holds when \(A\ge0\) and \(B\gt0\).</b>', r'Quy tắc đúng khi \(A\ge0\) và \(B\gt0\).'),
 (r'<b>Write 125 as \(25\cdot5\).</b>', r'Viết 125 thành \(25\cdot5\).'),
 (r'<b>Simplify the expression.</b>', r'Rút gọn biểu thức.'),
 (r'<b>Since \(a\lt0\), \(|a|=-a\).</b>', r'Vì \(a\lt0\) nên \(|a|=-a\).')]
review = (T(r'<b>Lesson 7.</b> \(\sqrt{A}\) is defined for \(A\ge0\); \(\sqrt{A^2}=|A|\).', r'<b>Bài 7.</b> \(\sqrt{A}\) xác định khi \(A\ge0\); \(\sqrt{A^2}=|A|\).') +
          T(r'<b>Perfect squares.</b> \(16, 25, 36, 49, 64, 81, 100, 121, 144\).', r'<b>Số chính phương.</b> \(16, 25, 36, 49, 64, 81, 100, 121, 144\).'))

theory = '<h3>5.1 %s</h3>' % TI('Square root of a product', 'Khai căn bậc hai và phép nhân')
theory += BOX('blue', ('Rule', 'Quy tắc'),
  M(r'\sqrt{AB}=\sqrt{A}\cdot\sqrt{B}\qquad (A\ge0,\ B\ge0)'),
  T(r'From left to right: take the square root of each factor. From right to left: multiply the radicands.', r'Chiều từ trái sang phải: [[khai căn bậc hai]] từng thừa số. Chiều từ phải sang trái: nhân các biểu thức lấy căn.'),
  T(r'Examples: \(\sqrt{4\cdot9\cdot25}=2\cdot3\cdot5=30\); \(\sqrt5\cdot\sqrt{125}=\sqrt{625}=25\).', r'Ví dụ: \(\sqrt{4\cdot9\cdot25}=2\cdot3\cdot5=30\); \(\sqrt5\cdot\sqrt{125}=\sqrt{625}=25\).'))
theory += '<h3>5.2 %s</h3>' % TI('Square root of a quotient', 'Khai căn bậc hai và phép chia')
theory += BOX('mint', ('Rule', 'Quy tắc'),
  M(r'\sqrt{\dfrac{A}{B}}=\dfrac{\sqrt{A}}{\sqrt{B}}\qquad (A\ge0,\ B\gt0)'),
  T(r'Examples: \(\sqrt{\dfrac{25}{49}}=\dfrac57\); \(\dfrac{\sqrt{50}}{\sqrt2}=\sqrt{25}=5\).', r'Ví dụ: \(\sqrt{\dfrac{25}{49}}=\dfrac57\); \(\dfrac{\sqrt{50}}{\sqrt2}=\sqrt{25}=5\).'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'),
  T(r'With letters, keep the sign: \(\sqrt{9a^2}=3|a|\). It equals \(3a\) if \(a\ge0\) and \(-3a\) if \(a\lt0\). Also \(\sqrt{a+b}\ne\sqrt a+\sqrt b\) in general: \(\sqrt{9+16}=5\ne7\).', r'Với biểu thức chứa chữ phải giữ dấu: \(\sqrt{9a^2}=3|a|\), bằng \(3a\) nếu \(a\ge0\) và bằng \(-3a\) nếu \(a\lt0\). Ngoài ra, nói chung \(\sqrt{a+b}\ne\sqrt a+\sqrt b\): \(\sqrt{9+16}=5\ne7\).'))

examples = EXAMPLE(1, ('Remembering', 'Biết'), ('Apply the rules', 'Áp dụng quy tắc'),
  T(r'Compute a) \(\sqrt{2^2\cdot3^2\cdot5^2}\); b) \(\sqrt{\dfrac{25}{49}}\).', r'Tính a) \(\sqrt{2^2\cdot3^2\cdot5^2}\); b) \(\sqrt{\dfrac{25}{49}}\).'),
  ('Take the square root of each factor / of the numerator and the denominator.', 'Khai căn từng thừa số / khai căn tử và mẫu.'),
  [T(r'a) \(\sqrt{2^2}\cdot\sqrt{3^2}\cdot\sqrt{5^2}=2\cdot3\cdot5=30\).', r'a) \(\sqrt{2^2}\cdot\sqrt{3^2}\cdot\sqrt{5^2}=2\cdot3\cdot5=30\).'),
   T(r'b) \(\dfrac{\sqrt{25}}{\sqrt{49}}=\dfrac57\).', r'b) \(\dfrac{\sqrt{25}}{\sqrt{49}}=\dfrac57\).')],
  T(r'a) \(30\); b) \(\dfrac57\).', r'a) \(30\); b) \(\dfrac57\).'))
examples += EXAMPLE(2, ('Understanding', 'Hiểu'), ('Multiply the radicands', 'Nhân các căn thức'),
  T(r'Compute \(\sqrt5\left(\sqrt{125}+\sqrt5\right)\).', r'Tính \(\sqrt5\left(\sqrt{125}+\sqrt5\right)\).'),
  ('Distribute, then use \\(\\sqrt A\\cdot\\sqrt B=\\sqrt{AB}\\).', 'Nhân phân phối rồi dùng \\(\\sqrt A\\cdot\\sqrt B=\\sqrt{AB}\\).'),
  [T(r'\(\sqrt5\cdot\sqrt{125}+\sqrt5\cdot\sqrt5=\sqrt{625}+\sqrt{25}\).', r'\(\sqrt5\cdot\sqrt{125}+\sqrt5\cdot\sqrt5=\sqrt{625}+\sqrt{25}\).'),
   T(r'\(=25+5=30\).', r'\(=25+5=30\).')],
  T(r'\(30\).', r'\(30\).'))
examples += EXAMPLE(3, ('Understanding', 'Hiểu'), ('Divide the radicands', 'Chia hai căn thức'),
  T(r'Compute a) \(\dfrac{\sqrt{50}}{\sqrt2}\); b) \(\dfrac{\sqrt{45}}{\sqrt{80}}\).', r'Tính a) \(\dfrac{\sqrt{50}}{\sqrt2}\); b) \(\dfrac{\sqrt{45}}{\sqrt{80}}\).'),
  ('Use \\(\\dfrac{\\sqrt A}{\\sqrt B}=\\sqrt{\\dfrac AB}\\) and simplify the fraction first.', 'Dùng \\(\\dfrac{\\sqrt A}{\\sqrt B}=\\sqrt{\\dfrac AB}\\) và rút gọn phân số trước.'),
  [T(r'a) \(\sqrt{\dfrac{50}{2}}=\sqrt{25}=5\).', r'a) \(\sqrt{\dfrac{50}{2}}=\sqrt{25}=5\).'),
   T(r'b) \(\sqrt{\dfrac{45}{80}}=\sqrt{\dfrac{9}{16}}=\dfrac34\).', r'b) \(\sqrt{\dfrac{45}{80}}=\sqrt{\dfrac{9}{16}}=\dfrac34\).')],
  T(r'a) \(5\); b) \(\dfrac34\).', r'a) \(5\); b) \(\dfrac34\).'))
assert F(45, 80) == F(9, 16)
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Expressions with letters', 'Biểu thức chứa chữ'),
  T(r'Simplify a) \(\sqrt{25a^2b^2}\) with \(a\lt0,\ b\gt0\); b) \(\dfrac{\sqrt{12a^3}}{\sqrt{3a}}\) with \(a\gt0\).', r'Rút gọn a) \(\sqrt{25a^2b^2}\) với \(a\lt0,\ b\gt0\); b) \(\dfrac{\sqrt{12a^3}}{\sqrt{3a}}\) với \(a\gt0\).'),
  ('Keep absolute values, then use the sign conditions.', 'Giữ dấu giá trị tuyệt đối rồi dùng điều kiện về dấu.'),
  [T(r'a) \(\sqrt{25}\cdot\sqrt{a^2}\cdot\sqrt{b^2}=5|a||b|=5(-a)b=-5ab\).', r'a) \(\sqrt{25}\cdot\sqrt{a^2}\cdot\sqrt{b^2}=5|a||b|=5(-a)b=-5ab\).'),
   T(r'b) \(\sqrt{\dfrac{12a^3}{3a}}=\sqrt{4a^2}=2|a|=2a\) (because \(a\gt0\)).', r'b) \(\sqrt{\dfrac{12a^3}{3a}}=\sqrt{4a^2}=2|a|=2a\) (vì \(a\gt0\)).')],
  T(r'a) \(-5ab\); b) \(2a\).', r'a) \(-5ab\); b) \(2a\).'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Electric power', 'Công suất điện'),
  T(r'The power of a device is \(P=\dfrac{U^2}{R}\) (\(P\) in watts, \(U\) in volts, \(R\) in ohms), so \(U=\sqrt{P\cdot R}\). Find \(U\) when \(P=60\) W and \(R=15\ \Omega\).', r'Công suất của một thiết bị điện là \(P=\dfrac{U^2}{R}\) (\(P\): oát, \(U\): vôn, \(R\): ôm), suy ra \(U=\sqrt{P\cdot R}\). Tính \(U\) khi \(P=60\) W và \(R=15\ \Omega\).'),
  ('Multiply under the root sign, then take the square root.', 'Nhân dưới dấu căn rồi khai căn.'),
  [T(r'\(U=\sqrt{60\cdot15}=\sqrt{900}=30\).', r'\(U=\sqrt{60\cdot15}=\sqrt{900}=30\).')],
  T(r'\(U=30\) V.', r'\(U=30\) V.'))

_SETS = sp_g9.BANK(sp_g9.L8_GROUPS, start=1, seeds=(1801, 1802, 1803))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Splitting a sum.</b> \(\sqrt{9+16}\ne\sqrt9+\sqrt{16}\): the rules are only for products and quotients.', r'<b>Tách căn của một tổng.</b> \(\sqrt{9+16}\ne\sqrt9+\sqrt{16}\): quy tắc chỉ dùng cho tích và thương.'),
 (r'<b>Losing the absolute value.</b> \(\sqrt{9a^2}=3|a|\), which is \(-3a\) when \(a\lt0\).', r'<b>Bỏ mất giá trị tuyệt đối.</b> \(\sqrt{9a^2}=3|a|\), bằng \(-3a\) khi \(a\lt0\).'),
 (r'<b>Ignoring the conditions.</b> \(\sqrt{(-4)(-9)}=6\), but \(\sqrt{-4}\cdot\sqrt{-9}\) is not defined.', r'<b>Bỏ qua điều kiện.</b> \(\sqrt{(-4)(-9)}=6\), nhưng \(\sqrt{-4}\cdot\sqrt{-9}\) không xác định.'),
 (r'<b>Allowing \(B=0\) in a quotient.</b> The denominator must be strictly positive.', r'<b>Cho phép \(B=0\) ở phép chia.</b> Mẫu phải dương.')]
summary = [
 (r'\(\sqrt{AB}=\sqrt A\cdot\sqrt B\) for \(A, B\ge0\).', r'\(\sqrt{AB}=\sqrt A\cdot\sqrt B\) với \(A, B\ge0\).'),
 (r'\(\sqrt{\dfrac AB}=\dfrac{\sqrt A}{\sqrt B}\) for \(A\ge0,\ B\gt0\).', r'\(\sqrt{\dfrac AB}=\dfrac{\sqrt A}{\sqrt B}\) với \(A\ge0,\ B\gt0\).'),
 (r'With letters, \(\sqrt{A^2B}=|A|\sqrt B\): check the sign of \(A\).', r'Với biểu thức chứa chữ, \(\sqrt{A^2B}=|A|\sqrt B\): xét dấu của \(A\).'),
 (r'Key English: take the square root, product, quotient, the rule holds when …', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[khai căn bậc hai]], [[tích]], [[thương]], [[quy tắc đúng khi]].')]
checks = [
 (r'I can use \(\sqrt{AB}=\sqrt A\cdot\sqrt B\) in both directions.', r'Em vận dụng được \(\sqrt{AB}=\sqrt A\cdot\sqrt B\) theo cả hai chiều.'),
 (r'I can use \(\sqrt{\dfrac AB}=\dfrac{\sqrt A}{\sqrt B}\) in both directions.', r'Em vận dụng được \(\sqrt{\dfrac AB}=\dfrac{\sqrt A}{\sqrt B}\) theo cả hai chiều.'),
 (r'I can simplify expressions with letters, keeping the correct sign.', r'Em rút gọn được biểu thức chứa chữ, giữ đúng dấu.'),
 (r'I can use the rules in a physics formula.', r'Em vận dụng được các quy tắc trong công thức vật lí.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Square Roots of Products and Quotients', title_vi='Khai căn bậc hai với phép nhân và phép chia', topic=TOPIC,
       folder='square-and-cube-roots', file='roots-products-quotients', catalog_title_vi='Khai căn bậc hai với phép nhân và phép chia',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='The rules √(AB) = √A·√B and √(A/B) = √A/√B, with computations and simplifications.', level='Intermediate', minutes=60,
       description_vi='Bài 8 – Khai căn bậc hai một tích, một thương; nhân, chia các căn thức bậc hai; rút gọn biểu thức chứa chữ.',
       tags_vi=['căn bậc hai', 'tích', 'thương', 'rút gọn'],
       prerequisites=['g9-roots-01'], tags=['square root', 'product', 'quotient'], order=80)
