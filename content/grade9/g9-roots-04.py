# -*- coding: utf-8 -*-
"""Nội dung bài g9-roots-04 = Toán 9 KNTT, Bài 10: Căn bậc ba và căn thức bậc ba – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 3 – Lesson 10."""
import os, sys, math
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9

LID = 'g9-roots-04'
CH = 'Căn bậc hai và căn bậc ba'
TOPIC = ('Square Roots and Cube Roots', CH)
ensure_vocab([
 ('g9-cube-root', 'cube root', 'căn bậc ba', CH, 'The cube root of −27 is −3, because (−3)³ = −27.', r'\(\sqrt[3]{a}\)'),
 ('g9-root-index', 'index (of a root)', 'chỉ số của căn', CH, 'In ∛a, the number 3 is the index of the root.', ''),
 ('g9-cube-root-expr', 'cube root expression', 'căn thức bậc ba', CH, '∛(2x + 5) is a cube root expression.', ''),
 ('g9-cube-of', 'cube (of a number)', 'lập phương (của một số)', CH, 'The cube of 4 is 4³ = 64.', r'\(a^3\)'),
 ('g9-volume', 'volume', 'thể tích', CH, 'The volume of a cube with edge a is a³.', r'\(V\)'),
])
load_vocab()

# ---------- kiểm tra số liệu ----------
assert 4 ** 3 == 64 and (-3) ** 3 == -27 and F(-2, 3) ** 3 == F(-8, 27)
assert abs(12 ** (1 / 3) - 2.29) < 0.005 and 2 * 11 + 5 == 27 and 3 ** 3 == 27 > 26
v = 730 ** (1 / 3); assert abs(v - 9.00) < 0.005 and round(v, 2) == 9.0

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 60 minutes', '60 phút'),
            before=('Lesson 7: square roots; powers \\(a^3\\)', 'Bài 7: căn bậc hai; lũy thừa \\(a^3\\)'))
goals = [
 (r'state the definition of the cube root of a real number;', r'nêu được định nghĩa căn bậc ba của một số thực;'),
 (r'compute cube roots of cubes and use \(\left(\sqrt[3]{a}\right)^3=\sqrt[3]{a^3}=a\);', r'tính được căn bậc ba của các lập phương và dùng \(\left(\sqrt[3]{a}\right)^3=\sqrt[3]{a^3}=a\);'),
 (r'use a calculator to approximate cube roots and evaluate cube root expressions;', r'dùng máy tính cầm tay tính gần đúng căn bậc ba; tính giá trị căn thức bậc ba;'),
 (r'solve problems about the edge and the volume of a cube.', r'giải bài toán về cạnh và thể tích hình lập phương.')]
vocab = [
 (r'<b>cube root</b> – \(\sqrt[3]{a}\) is the number \(x\) with \(x^3=a\).', r'[[Căn bậc ba]] – \(\sqrt[3]{a}\) là số \(x\) sao cho \(x^3=a\).'),
 (r'<b>index (of a root)</b> – the small 3 in \(\sqrt[3]{\ }\).', r'[[Chỉ số của căn]] – số 3 nhỏ trong \(\sqrt[3]{\ }\).'),
 (r'<b>cube (of a number)</b> – \(a^3=a\cdot a\cdot a\).', r'[[Lập phương (của một số)|lập phương (của một số)]] – \(a^3=a\cdot a\cdot a\).'),
 (r'<b>cube root expression</b> – \(\sqrt[3]{A}\), where \(A\) is an algebraic expression.', r'[[Căn thức bậc ba]] – \(\sqrt[3]{A}\) với \(A\) là một biểu thức đại số.'),
 (r'<b>volume</b> – the volume of a cube with edge \(a\) is \(V=a^3\).', r'[[Thể tích]] – hình lập phương cạnh \(a\) có thể tích \(V=a^3\).')]
phrases = [
 (r'<b>\(\sqrt[3]{64}\)</b>: “the cube root of sixty-four”.', r'\(\sqrt[3]{64}\): căn bậc ba của 64.'),
 (r'<b>Every real number has exactly one cube root.</b>', r'Mọi số thực đều có đúng một căn bậc ba.'),
 (r'<b>Cube both sides.</b>', r'Lập phương hai vế.'),
 (r'<b>The edge is about 9.00 dm.</b>', r'Cạnh dài khoảng 9,00 dm.'),
 (r'<b>The expression is defined for every value of \(x\).</b>', r'Biểu thức xác định với mọi giá trị của \(x\).')]
review = (T(r'<b>Cubes.</b> \(1, 8, 27, 64, 125, 216, 343, 512, 729, 1000\); and \((-a)^3=-a^3\).', r'<b>Các lập phương.</b> \(1, 8, 27, 64, 125, 216, 343, 512, 729, 1000\); và \((-a)^3=-a^3\).') +
          T(r'<b>Lesson 7.</b> \(\sqrt{a}\) is defined only for \(a\ge0\).', r'<b>Bài 7.</b> \(\sqrt{a}\) chỉ xác định khi \(a\ge0\).'))

theory = '<h3>5.1 %s</h3>' % TI('Cube root', 'Căn bậc ba')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'The <b>cube root</b> of a real number \(a\) is the number \(x\) such that \(x^3=a\). It is written \(\sqrt[3]{a}\); the number 3 is the index of the root.', r'[[Căn bậc ba]] của số thực \(a\) là số \(x\) sao cho \(x^3=a\). Kí hiệu \(\sqrt[3]{a}\); số 3 là [[chỉ số của căn]].'),
  M(r'\left(\sqrt[3]{a}\right)^3=\sqrt[3]{a^3}=a\qquad\text{for every } a'),
  T(r'Every real number has <b>exactly one</b> cube root: positive numbers have positive cube roots, negative numbers have negative cube roots, \(\sqrt[3]{0}=0\). Examples: \(\sqrt[3]{64}=4\), \(\sqrt[3]{-27}=-3\).', r'Mọi số thực đều có <b>đúng một</b> căn bậc ba: số dương có căn bậc ba dương, số âm có căn bậc ba âm, \(\sqrt[3]{0}=0\). Ví dụ: \(\sqrt[3]{64}=4\), \(\sqrt[3]{-27}=-3\).'))
theory += '<h3>5.2 %s</h3>' % TI('Cube root expressions', 'Căn thức bậc ba')
theory += BOX('mint', ('Notes', 'Ghi nhớ'),
  T(r'\(\sqrt[3]{A}\) is defined for <b>every</b> value of the variable for which \(A\) is defined (no condition \(A\ge0\)).', r'\(\sqrt[3]{A}\) xác định với <b>mọi</b> giá trị của biến làm cho \(A\) xác định (không cần điều kiện \(A\ge0\)).'),
  T(r'Comparing: if \(a\lt b\) then \(\sqrt[3]{a}\lt\sqrt[3]{b}\). Example: \(3=\sqrt[3]{27}\gt\sqrt[3]{26}\).', r'So sánh: nếu \(a\lt b\) thì \(\sqrt[3]{a}\lt\sqrt[3]{b}\). Ví dụ: \(3=\sqrt[3]{27}\gt\sqrt[3]{26}\).'),
  T(r'Calculator: use the \(\sqrt[3]{\ }\) key (often SHIFT + \(\sqrt{\ }\)). Example: \(\sqrt[3]{12}\approx2.29\).', r'Máy tính cầm tay: dùng phím \(\sqrt[3]{\ }\) (thường là SHIFT + \(\sqrt{\ }\)). Ví dụ: \(\sqrt[3]{12}\approx2{,}29\).'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Compute cube roots', 'Tính căn bậc ba'),
  T(r'Compute a) \(\sqrt[3]{64}\); b) \(\sqrt[3]{-27}\); c) \(\sqrt[3]{-\dfrac{8}{27}}\).', r'Tính a) \(\sqrt[3]{64}\); b) \(\sqrt[3]{-27}\); c) \(\sqrt[3]{-\dfrac{8}{27}}\).'),
  ('Write each number as a cube.', 'Viết mỗi số dưới dạng lập phương của một số.'),
  [T(r'a) \(64=4^3\Rightarrow\sqrt[3]{64}=4\). b) \(-27=(-3)^3\Rightarrow\sqrt[3]{-27}=-3\).', r'a) \(64=4^3\Rightarrow\sqrt[3]{64}=4\). b) \(-27=(-3)^3\Rightarrow\sqrt[3]{-27}=-3\).'),
   T(r'c) \(-\dfrac{8}{27}=\left(-\dfrac23\right)^3\Rightarrow\sqrt[3]{-\dfrac{8}{27}}=-\dfrac23\).', r'c) \(-\dfrac{8}{27}=\left(-\dfrac23\right)^3\Rightarrow\sqrt[3]{-\dfrac{8}{27}}=-\dfrac23\).')],
  T(r'a) \(4\); b) \(-3\); c) \(-\dfrac23\).', r'a) \(4\); b) \(-3\); c) \(-\dfrac23\).'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Use the identity', 'Dùng đẳng thức'),
  T(r'Compute a) \(\left(\sqrt[3]{5}\right)^3\); b) \(\sqrt[3]{(-7)^3}+\sqrt[3]{1000}\).', r'Tính a) \(\left(\sqrt[3]{5}\right)^3\); b) \(\sqrt[3]{(-7)^3}+\sqrt[3]{1000}\).'),
  ('\\(\\left(\\sqrt[3]{a}\\right)^3=\\sqrt[3]{a^3}=a\\) for every \\(a\\) – no absolute value!', '\\(\\left(\\sqrt[3]{a}\\right)^3=\\sqrt[3]{a^3}=a\\) với mọi \\(a\\) – không có giá trị tuyệt đối!'),
  [T(r'a) \(\left(\sqrt[3]{5}\right)^3=5\).', r'a) \(\left(\sqrt[3]{5}\right)^3=5\).'),
   T(r'b) \(-7+10=3\).', r'b) \(-7+10=3\).')],
  T(r'a) \(5\); b) \(3\).', r'a) \(5\); b) \(3\).'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('Calculator', 'Dùng máy tính cầm tay'),
  T(r'Use a calculator to find \(\sqrt[3]{12}\), rounded to two decimal places. Check your answer by cubing.', r'Dùng máy tính cầm tay tính \(\sqrt[3]{12}\), làm tròn đến chữ số thập phân thứ hai. Kiểm tra lại bằng cách lập phương.'),
  ('Press SHIFT, \\(\\sqrt{\\ }\\) (or the \\(\\sqrt[3]{\\ }\\) key), 12, =.', 'Bấm SHIFT, \\(\\sqrt{\\ }\\) (hoặc phím \\(\\sqrt[3]{\\ }\\)), 12, =.'),
  [T(r'The screen shows \(2.289428\ldots\), so \(\sqrt[3]{12}\approx2.29\).', r'Màn hình hiện \(2{,}289428\ldots\), nên \(\sqrt[3]{12}\approx2{,}29\).'),
   T(r'Check: \(2.29^3\approx12.01\), close to 12.', r'Kiểm tra: \(2{,}29^3\approx12{,}01\), gần bằng 12.')],
  T(r'\(\sqrt[3]{12}\approx2.29\).', r'\(\sqrt[3]{12}\approx2{,}29\).'))
assert abs(2.29 ** 3 - 12.01) < 0.005
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Cube root expression', 'Căn thức bậc ba'),
  T(r'Given \(A=\sqrt[3]{2x+5}\). a) For which \(x\) is \(A\) defined? b) Compute \(A\) at \(x=11\). c) Compare that value with \(\sqrt[3]{26}\).', r'Cho \(A=\sqrt[3]{2x+5}\). a) \(A\) xác định khi nào? b) Tính giá trị của \(A\) tại \(x=11\). c) So sánh giá trị đó với \(\sqrt[3]{26}\).'),
  ('A cube root is defined for every real radicand.', 'Căn bậc ba xác định với mọi biểu thức dưới dấu căn.'),
  [T(r'a) \(2x+5\) is defined for every \(x\), so \(A\) is defined for every \(x\).', r'a) \(2x+5\) xác định với mọi \(x\) nên \(A\) xác định với mọi \(x\).'),
   T(r'b) \(A=\sqrt[3]{2\cdot11+5}=\sqrt[3]{27}=3\).', r'b) \(A=\sqrt[3]{2\cdot11+5}=\sqrt[3]{27}=3\).'),
   T(r'c) \(3=\sqrt[3]{27}\) and \(27\gt26\), so \(3\gt\sqrt[3]{26}\).', r'c) \(3=\sqrt[3]{27}\) và \(27\gt26\) nên \(3\gt\sqrt[3]{26}\).')],
  T(r'a) every \(x\); b) \(3\); c) \(3\gt\sqrt[3]{26}\).', r'a) mọi \(x\); b) \(3\); c) \(3\gt\sqrt[3]{26}\).'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('A cubic tank', 'Bể nước hình lập phương'),
  T(r'A water tank in the shape of a cube holds \(730\) dm³ of water. Find the length of its edge, rounded to two decimal places.', r'Một bể nước hình lập phương chứa được \(730\) dm³ nước. Tính độ dài cạnh bể (làm tròn đến chữ số thập phân thứ hai).'),
  ('\\(V=a^3\\Rightarrow a=\\sqrt[3]{V}\\).', '\\(V=a^3\\Rightarrow a=\\sqrt[3]{V}\\).'),
  [T(r'\(a=\sqrt[3]{730}\approx9.0041\ldots\)', r'\(a=\sqrt[3]{730}\approx9{,}0041\ldots\)'),
   T(r'\(a\approx9.00\) dm (check: \(9^3=729\), very close to 730).', r'\(a\approx9{,}00\) dm (kiểm tra: \(9^3=729\), rất gần 730).')],
  T(r'About \(9.00\) dm.', r'Khoảng \(9{,}00\) dm.'))
assert abs(730 ** (1 / 3) - 9.0041) < 0.0001

_SETS = sp_g9.BANK(sp_g9.L10_GROUPS, start=1, seeds=(2001, 2002, 2003))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Saying a negative number has no cube root.</b> \(\sqrt[3]{-8}=-2\); only square roots of negative numbers are not defined.', r'<b>Cho rằng số âm không có căn bậc ba.</b> \(\sqrt[3]{-8}=-2\); chỉ căn bậc hai của số âm mới không xác định.'),
 (r'<b>Writing \(\pm\).</b> Every number has exactly one cube root: \(\sqrt[3]{27}=3\), not \(\pm3\).', r'<b>Viết \(\pm\).</b> Mỗi số có đúng một căn bậc ba: \(\sqrt[3]{27}=3\), không phải \(\pm3\).'),
 (r'<b>Dividing by 3.</b> \(\sqrt[3]{27}\ne\dfrac{27}{3}\).', r'<b>Chia cho 3.</b> \(\sqrt[3]{27}\ne\dfrac{27}{3}\).'),
 (r'<b>Adding a condition \(A\ge0\).</b> \(\sqrt[3]{A}\) needs no such condition.', r'<b>Thêm điều kiện \(A\ge0\).</b> \(\sqrt[3]{A}\) không cần điều kiện này.')]
summary = [
 (r'\(x=\sqrt[3]{a}\iff x^3=a\); every real number has exactly one cube root.', r'\(x=\sqrt[3]{a}\iff x^3=a\); mọi số thực có đúng một căn bậc ba.'),
 (r'\(\left(\sqrt[3]{a}\right)^3=\sqrt[3]{a^3}=a\) for every \(a\).', r'\(\left(\sqrt[3]{a}\right)^3=\sqrt[3]{a^3}=a\) với mọi \(a\).'),
 (r'\(\sqrt[3]{A}\) is defined whenever \(A\) is defined; \(a\lt b\iff\sqrt[3]{a}\lt\sqrt[3]{b}\).', r'\(\sqrt[3]{A}\) xác định khi \(A\) xác định; \(a\lt b\iff\sqrt[3]{a}\lt\sqrt[3]{b}\).'),
 (r'Key English: cube root, index of a root, cube of a number, cube root expression, volume.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[căn bậc ba]], [[chỉ số của căn]], [[lập phương (của một số)]], [[căn thức bậc ba]], [[thể tích]].')]
checks = [
 (r'I can state the definition of a cube root.', r'Em nêu được định nghĩa căn bậc ba.'),
 (r'I can compute cube roots, also of negative numbers and fractions.', r'Em tính được căn bậc ba, kể cả của số âm và phân số.'),
 (r'I can use a calculator to approximate cube roots.', r'Em dùng được máy tính cầm tay để tính gần đúng căn bậc ba.'),
 (r'I can find the edge of a cube from its volume.', r'Em tính được cạnh hình lập phương khi biết thể tích.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Cube Roots and Cube Root Expressions', title_vi='Căn bậc ba và căn thức bậc ba', topic=TOPIC,
       folder='square-and-cube-roots', file='cube-roots', catalog_title_vi='Căn bậc ba và căn thức bậc ba',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='The cube root of a real number, cube root expressions, calculator use and the edge of a cube.', level='Intermediate', minutes=60,
       description_vi='Bài 10 – Căn bậc ba của một số thực; căn thức bậc ba; dùng máy tính cầm tay; cạnh và thể tích hình lập phương.',
       tags_vi=['căn bậc ba', 'lập phương', 'thể tích'],
       prerequisites=['g9-roots-01'], tags=['cube root', 'cube', 'volume'], order=100)
