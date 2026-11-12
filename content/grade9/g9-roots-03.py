# -*- coding: utf-8 -*-
"""Nội dung bài g9-roots-03 = Toán 9 KNTT, Bài 9: Biến đổi đơn giản và rút gọn biểu thức chứa căn thức bậc hai – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 3 – Lesson 9."""
import os, sys, math
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9

LID = 'g9-roots-03'
CH = 'Căn bậc hai và căn bậc ba'
TOPIC = ('Square Roots and Cube Roots', CH)
ensure_vocab([
 ('g9-take-in', 'bring into the root sign', 'đưa vào trong dấu căn', CH, '4√3 = √(16·3) = √48: bring 4 into the root sign.', ''),
 ('g9-rationalize', 'rationalize the denominator', 'trục căn thức ở mẫu', CH, 'Rationalize the denominator of 1/√5: 1/√5 = √5/5.', ''),
 ('g9-conjugate', 'conjugate expression', 'biểu thức liên hợp', CH, 'The conjugate of √5 − 2 is √5 + 2.', ''),
 ('g9-like-roots', 'like radicals', 'căn thức đồng dạng', CH, '2√3 and −5√3 are like radicals.', ''),
 ('g9-simplify-expr', 'simplify an expression', 'rút gọn biểu thức', CH, 'Simplify the expression 2√3 − √75.', ''),
])
load_vocab()

# ---------- kiểm tra số liệu ----------
assert 4 * 13 == 52 and 16 * 3 == 48 and 4 * 7 == 28 and 9 * 2 == 18 and 4 * 3 == 12 and 18 > 12
assert (5 ** 0.5 + 2) * (5 ** 0.5 - 2) - 1 < 1e-12
r3 = 3 ** 0.5
A = 2 * r3 - 75 ** 0.5 + math.sqrt((1 - r3) ** 2); assert abs(A - (-2 * r3 - 1)) < 1e-12
assert abs(math.sqrt(1 - 0.6 ** 2) - 0.8) < 1e-12 and abs(80 / 0.8 - 100) < 1e-9

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 75 minutes', '75 phút'),
            before=('Lesson 8: square roots of products and quotients', 'Bài 8: khai căn bậc hai với phép nhân và phép chia'))
goals = [
 (r'take a factor out of the root sign and bring a factor into the root sign;', r'đưa được thừa số ra ngoài dấu căn và đưa thừa số vào trong dấu căn;'),
 (r'remove a denominator under the root sign and rationalize a denominator;', r'khử được mẫu của biểu thức lấy căn và trục căn thức ở mẫu;'),
 (r'combine like radicals and simplify expressions containing square roots;', r'cộng, trừ các căn thức đồng dạng và rút gọn biểu thức chứa căn thức bậc hai;'),
 (r'use these transformations in a formula from physics.', r'vận dụng các phép biến đổi trong một công thức vật lí.')]
vocab = [
 (r'<b>take out of the root sign</b> – \(\sqrt{A^2B}=|A|\sqrt B\) (\(B\ge0\)).', r'[[Đưa ra ngoài dấu căn]] – \(\sqrt{A^2B}=|A|\sqrt B\) (\(B\ge0\)).'),
 (r'<b>bring into the root sign</b> – \(A\sqrt B=\sqrt{A^2B}\) if \(A\ge0\).', r'[[Đưa vào trong dấu căn]] – \(A\sqrt B=\sqrt{A^2B}\) nếu \(A\ge0\).'),
 (r'<b>rationalize the denominator</b> – rewrite a fraction so that no root is left in the denominator.', r'[[Trục căn thức ở mẫu]] – biến đổi để mẫu không còn chứa căn.'),
 (r'<b>conjugate expression</b> – \(\sqrt A+B\) and \(\sqrt A-B\) are conjugates.', r'[[Biểu thức liên hợp]] – \(\sqrt A+B\) và \(\sqrt A-B\) là hai biểu thức liên hợp.'),
 (r'<b>like radicals</b> – radicals with the same radicand, such as \(2\sqrt3\) and \(-5\sqrt3\).', r'[[Căn thức đồng dạng]] – các căn thức có cùng biểu thức dưới dấu căn, như \(2\sqrt3\) và \(-5\sqrt3\).')]
phrases = [
 (r'<b>Write 52 as \(4\cdot13\).</b>', r'Viết 52 thành \(4\cdot13\).'),
 (r'<b>Take 2 out of the root sign.</b>', r'Đưa 2 ra ngoài dấu căn.'),
 (r'<b>Multiply the numerator and the denominator by the conjugate.</b>', r'Nhân cả tử và mẫu với biểu thức liên hợp.'),
 (r'<b>Combine like radicals.</b>', r'Cộng, trừ các căn thức đồng dạng.'),
 (r'<b>Simplify the expression.</b>', r'Rút gọn biểu thức.')]
review = (T(r'<b>Lesson 8.</b> \(\sqrt{AB}=\sqrt A\cdot\sqrt B\) (\(A,B\ge0\)); \(\sqrt{\dfrac AB}=\dfrac{\sqrt A}{\sqrt B}\) (\(A\ge0,\ B\gt0\)).', r'<b>Bài 8.</b> \(\sqrt{AB}=\sqrt A\cdot\sqrt B\) (\(A,B\ge0\)); \(\sqrt{\dfrac AB}=\dfrac{\sqrt A}{\sqrt B}\) (\(A\ge0,\ B\gt0\)).') +
          T(r'<b>Identity.</b> \((a+b)(a-b)=a^2-b^2\).', r'<b>Hằng đẳng thức.</b> \((a+b)(a-b)=a^2-b^2\).'))

theory = '<h3>5.1 %s</h3>' % TI('Taking a factor out of / into the root sign', 'Đưa thừa số ra ngoài, vào trong dấu căn')
theory += BOX('blue', ('Rules', 'Quy tắc'),
  M(r'\sqrt{A^2B}=|A|\sqrt{B}\qquad (B\ge0)'),
  M(r'A\sqrt{B}=\sqrt{A^2B}\ \ (A\ge0,\ B\ge0);\qquad A\sqrt{B}=-\sqrt{A^2B}\ \ (A\lt0,\ B\ge0)'),
  T(r'Examples: \(\sqrt{52}=\sqrt{4\cdot13}=2\sqrt{13}\); \(4\sqrt3=\sqrt{48}\); \(-2\sqrt7=-\sqrt{28}\).', r'Ví dụ: \(\sqrt{52}=\sqrt{4\cdot13}=2\sqrt{13}\); \(4\sqrt3=\sqrt{48}\); \(-2\sqrt7=-\sqrt{28}\).'))
theory += '<h3>5.2 %s</h3>' % TI('Removing a denominator and rationalizing', 'Khử mẫu và trục căn thức ở mẫu')
theory += BOX('mint', ('Rules', 'Quy tắc'),
  M(r'\sqrt{\dfrac{A}{B}}=\dfrac{\sqrt{AB}}{|B|}\ \ (AB\ge0,\ B\ne0);\qquad \dfrac{A}{\sqrt B}=\dfrac{A\sqrt B}{B}\ \ (B\gt0)'),
  M(r'\dfrac{C}{\sqrt A-B}=\dfrac{C\left(\sqrt A+B\right)}{A-B^2}\qquad (A\ge0,\ A\ne B^2)'),
  T(r'The second rule uses the conjugate: \(\left(\sqrt A-B\right)\left(\sqrt A+B\right)=A-B^2\). The same idea works for \(\sqrt A+B\) and for \(\sqrt A\pm\sqrt B\).', r'Quy tắc thứ hai dùng [[biểu thức liên hợp]]: \(\left(\sqrt A-B\right)\left(\sqrt A+B\right)=A-B^2\). Làm tương tự với \(\sqrt A+B\) và \(\sqrt A\pm\sqrt B\).'))
theory += '<h3>5.3 %s</h3>' % TI('Simplifying expressions', 'Rút gọn biểu thức chứa căn thức bậc hai')
theory += BOX('yellow', ('Method', 'Cách làm'),
  UL([T(r'Take factors out of the root sign to get like radicals.', r'Đưa thừa số ra ngoài dấu căn để được các căn thức đồng dạng.'),
     T(r'Remove denominators, rationalize denominators.', r'Khử mẫu, trục căn thức ở mẫu.'),
     T(r'Combine like radicals: \(a\sqrt c+b\sqrt c=(a+b)\sqrt c\).', r'Cộng, trừ các căn thức đồng dạng: \(a\sqrt c+b\sqrt c=(a+b)\sqrt c\).')]),
  T(r'Comparing: bring the factors into the root sign, then compare the radicands. Example: \(3\sqrt2=\sqrt{18}\gt\sqrt{12}=2\sqrt3\).', r'So sánh: đưa thừa số vào trong dấu căn rồi so sánh các biểu thức dưới dấu căn. Ví dụ: \(3\sqrt2=\sqrt{18}\gt\sqrt{12}=2\sqrt3\).'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Take a factor out', 'Đưa thừa số ra ngoài dấu căn'),
  T(r'Take the factor out of the root sign: a) \(\sqrt{52}\); b) \(\sqrt{27a}\) with \(a\ge0\).', r'Đưa thừa số ra ngoài dấu căn: a) \(\sqrt{52}\); b) \(\sqrt{27a}\) với \(a\ge0\).'),
  ('Find a perfect-square factor.', 'Tìm thừa số là số chính phương.'),
  [T(r'a) \(\sqrt{52}=\sqrt{2^2\cdot13}=2\sqrt{13}\).', r'a) \(\sqrt{52}=\sqrt{2^2\cdot13}=2\sqrt{13}\).'),
   T(r'b) \(\sqrt{27a}=\sqrt{3^2\cdot3a}=3\sqrt{3a}\).', r'b) \(\sqrt{27a}=\sqrt{3^2\cdot3a}=3\sqrt{3a}\).')],
  T(r'a) \(2\sqrt{13}\); b) \(3\sqrt{3a}\).', r'a) \(2\sqrt{13}\); b) \(3\sqrt{3a}\).'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Bring a factor in and compare', 'Đưa thừa số vào trong dấu căn và so sánh'),
  T(r'a) Bring the factor into the root sign: \(4\sqrt3\); \(-2\sqrt7\). b) Compare \(3\sqrt2\) and \(2\sqrt3\).', r'a) Đưa thừa số vào trong dấu căn: \(4\sqrt3\); \(-2\sqrt7\). b) So sánh \(3\sqrt2\) và \(2\sqrt3\).'),
  ('A negative factor stays outside as a minus sign.', 'Thừa số âm thì giữ dấu trừ ở ngoài.'),
  [T(r'a) \(4\sqrt3=\sqrt{4^2\cdot3}=\sqrt{48}\); \(-2\sqrt7=-\sqrt{2^2\cdot7}=-\sqrt{28}\).', r'a) \(4\sqrt3=\sqrt{4^2\cdot3}=\sqrt{48}\); \(-2\sqrt7=-\sqrt{2^2\cdot7}=-\sqrt{28}\).'),
   T(r'b) \(3\sqrt2=\sqrt{18}\), \(2\sqrt3=\sqrt{12}\). Since \(18\gt12\), \(3\sqrt2\gt2\sqrt3\).', r'b) \(3\sqrt2=\sqrt{18}\), \(2\sqrt3=\sqrt{12}\). Vì \(18\gt12\) nên \(3\sqrt2\gt2\sqrt3\).')],
  T(r'a) \(\sqrt{48}\); \(-\sqrt{28}\). b) \(3\sqrt2\gt2\sqrt3\).', r'a) \(\sqrt{48}\); \(-\sqrt{28}\). b) \(3\sqrt2\gt2\sqrt3\).'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('Remove the denominator, rationalize', 'Khử mẫu, trục căn thức ở mẫu'),
  T(r'a) Remove the denominator: \(\sqrt{\dfrac35}\). b) Rationalize the denominator: \(\dfrac{1}{\sqrt5-2}\).', r'a) Khử mẫu của biểu thức lấy căn: \(\sqrt{\dfrac35}\). b) Trục căn thức ở mẫu: \(\dfrac{1}{\sqrt5-2}\).'),
  ('For b), multiply by the conjugate \\(\\sqrt5+2\\).', 'Ở câu b), nhân tử và mẫu với biểu thức liên hợp \\(\\sqrt5+2\\).'),
  [T(r'a) \(\sqrt{\dfrac35}=\sqrt{\dfrac{3\cdot5}{5^2}}=\dfrac{\sqrt{15}}{5}\).', r'a) \(\sqrt{\dfrac35}=\sqrt{\dfrac{3\cdot5}{5^2}}=\dfrac{\sqrt{15}}{5}\).'),
   T(r'b) \(\dfrac{\sqrt5+2}{\left(\sqrt5-2\right)\left(\sqrt5+2\right)}=\dfrac{\sqrt5+2}{5-4}=\sqrt5+2\).', r'b) \(\dfrac{\sqrt5+2}{\left(\sqrt5-2\right)\left(\sqrt5+2\right)}=\dfrac{\sqrt5+2}{5-4}=\sqrt5+2\).')],
  T(r'a) \(\dfrac{\sqrt{15}}{5}\); b) \(\sqrt5+2\).', r'a) \(\dfrac{\sqrt{15}}{5}\); b) \(\sqrt5+2\).'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Simplify an expression', 'Rút gọn biểu thức'),
  T(r'Simplify \(A=2\sqrt3-\sqrt{75}+\sqrt{\left(1-\sqrt3\right)^2}\).', r'Rút gọn \(A=2\sqrt3-\sqrt{75}+\sqrt{\left(1-\sqrt3\right)^2}\).'),
  ('Use \\(\\sqrt{A^2}=|A|\\) and check the sign of \\(1-\\sqrt3\\).', 'Dùng \\(\\sqrt{A^2}=|A|\\) và xét dấu của \\(1-\\sqrt3\\).'),
  [T(r'\(\sqrt{75}=\sqrt{25\cdot3}=5\sqrt3\).', r'\(\sqrt{75}=\sqrt{25\cdot3}=5\sqrt3\).'),
   T(r'\(1\lt\sqrt3\), so \(\sqrt{\left(1-\sqrt3\right)^2}=\left|1-\sqrt3\right|=\sqrt3-1\).', r'\(1\lt\sqrt3\) nên \(\sqrt{\left(1-\sqrt3\right)^2}=\left|1-\sqrt3\right|=\sqrt3-1\).'),
   T(r'\(A=2\sqrt3-5\sqrt3+\sqrt3-1=-2\sqrt3-1\).', r'\(A=2\sqrt3-5\sqrt3+\sqrt3-1=-2\sqrt3-1\).')],
  T(r'\(A=-2\sqrt3-1\).', r'\(A=-2\sqrt3-1\).'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Mass at high speed', 'Khối lượng khi chuyển động rất nhanh'),
  T(r'In the theory of relativity, a body with rest mass \(m_0\) moving at speed \(v\) has mass \(m=\dfrac{m_0}{\sqrt{1-\dfrac{v^2}{c^2}}}\), where \(c\) is the speed of light (the mass grows only when \(v\) is very close to \(c\)). Find \(m\) when \(m_0=80\) kg and \(v=0.6c\).', r'Theo thuyết tương đối, một vật có khối lượng nghỉ \(m_0\) chuyển động với tốc độ \(v\) thì có khối lượng \(m=\dfrac{m_0}{\sqrt{1-\dfrac{v^2}{c^2}}}\), trong đó \(c\) là tốc độ ánh sáng (khối lượng chỉ tăng rõ khi \(v\) rất gần \(c\)). Tính \(m\) khi \(m_0=80\) kg và \(v=0{,}6c\).'),
  ('Simplify \\(\\dfrac{v^2}{c^2}\\) first.', 'Rút gọn \\(\\dfrac{v^2}{c^2}\\) trước.'),
  [T(r'\(\dfrac{v^2}{c^2}=\dfrac{(0.6c)^2}{c^2}=0.36\), so \(\sqrt{1-0.36}=\sqrt{0.64}=0.8\).', r'\(\dfrac{v^2}{c^2}=\dfrac{(0{,}6c)^2}{c^2}=0{,}36\), nên \(\sqrt{1-0{,}36}=\sqrt{0{,}64}=0{,}8\).'),
   T(r'\(m=\dfrac{80}{0.8}=100\) kg (that is \(1.25\,m_0\)).', r'\(m=\dfrac{80}{0{,}8}=100\) kg (tức là \(1{,}25\,m_0\)).')],
  T(r'\(m=100\) kg.', r'\(m=100\) kg.'))

_SETS = sp_g9.BANK(sp_g9.L9_GROUPS, start=1, seeds=(1901, 1902, 1903))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Losing the minus sign.</b> \(-2\sqrt7=-\sqrt{28}\), not \(\sqrt{28}\) and not \(\sqrt{-28}\).', r'<b>Làm mất dấu trừ.</b> \(-2\sqrt7=-\sqrt{28}\), không phải \(\sqrt{28}\) hay \(\sqrt{-28}\).'),
 (r'<b>Adding unlike radicals.</b> \(\sqrt2+\sqrt3\ne\sqrt5\); only like radicals can be combined.', r'<b>Cộng các căn không đồng dạng.</b> \(\sqrt2+\sqrt3\ne\sqrt5\); chỉ cộng, trừ được các căn thức đồng dạng.'),
 (r'<b>Wrong conjugate.</b> For \(\sqrt5-2\), multiply by \(\sqrt5+2\), not by \(\sqrt5-2\).', r'<b>Nhầm biểu thức liên hợp.</b> Với \(\sqrt5-2\) phải nhân với \(\sqrt5+2\), không nhân với \(\sqrt5-2\).'),
 (r'<b>Forgetting \(|A|\).</b> \(\sqrt{\left(1-\sqrt3\right)^2}=\sqrt3-1\), not \(1-\sqrt3\).', r'<b>Quên \(|A|\).</b> \(\sqrt{\left(1-\sqrt3\right)^2}=\sqrt3-1\), không phải \(1-\sqrt3\).')]
summary = [
 (r'\(\sqrt{A^2B}=|A|\sqrt B\); \(A\sqrt B=\sqrt{A^2B}\) if \(A\ge0\), \(A\sqrt B=-\sqrt{A^2B}\) if \(A\lt0\).', r'\(\sqrt{A^2B}=|A|\sqrt B\); \(A\sqrt B=\sqrt{A^2B}\) nếu \(A\ge0\), \(A\sqrt B=-\sqrt{A^2B}\) nếu \(A\lt0\).'),
 (r'\(\dfrac{A}{\sqrt B}=\dfrac{A\sqrt B}{B}\); \(\dfrac{C}{\sqrt A-B}=\dfrac{C\left(\sqrt A+B\right)}{A-B^2}\).', r'\(\dfrac{A}{\sqrt B}=\dfrac{A\sqrt B}{B}\); \(\dfrac{C}{\sqrt A-B}=\dfrac{C\left(\sqrt A+B\right)}{A-B^2}\).'),
 (r'To simplify: take factors out, get like radicals, then combine them.', r'Rút gọn: đưa thừa số ra ngoài, tạo căn thức đồng dạng rồi cộng, trừ.'),
 (r'Key English: take out of / bring into the root sign, rationalize the denominator, conjugate expression, like radicals.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[đưa ra ngoài dấu căn]], [[đưa vào trong dấu căn]], [[trục căn thức ở mẫu]], [[biểu thức liên hợp]], [[căn thức đồng dạng]].')]
checks = [
 (r'I can take a factor out of / into the root sign.', r'Em đưa được thừa số ra ngoài, vào trong dấu căn.'),
 (r'I can remove a denominator and rationalize a denominator.', r'Em khử được mẫu và trục được căn thức ở mẫu.'),
 (r'I can simplify an expression containing square roots.', r'Em rút gọn được biểu thức chứa căn thức bậc hai.'),
 (r'I can use these transformations in a physics formula.', r'Em vận dụng được các phép biến đổi trong công thức vật lí.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Simplifying Expressions Containing Square Roots', title_vi='Biến đổi đơn giản và rút gọn biểu thức chứa căn thức bậc hai', topic=TOPIC,
       folder='square-and-cube-roots', file='simplifying-square-roots', catalog_title_vi='Biến đổi đơn giản và rút gọn biểu thức chứa căn thức bậc hai',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Taking factors out of / into the root sign, rationalizing denominators and simplifying expressions with square roots.', level='Intermediate', minutes=75,
       description_vi='Bài 9 – Đưa thừa số ra ngoài, vào trong dấu căn; khử mẫu, trục căn thức ở mẫu; rút gọn biểu thức chứa căn thức bậc hai.',
       tags_vi=['căn bậc hai', 'trục căn thức', 'rút gọn'],
       prerequisites=['g9-roots-02'], tags=['square root', 'rationalize', 'simplify'], order=90)
