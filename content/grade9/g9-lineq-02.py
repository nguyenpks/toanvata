# -*- coding: utf-8 -*-
"""Nội dung bài g9-lineq-02 = Toán 9 KNTT, Bài 5: Bất đẳng thức và tính chất – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 2 – Lesson 5, tr. 18–19."""
import os, sys
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9

LID = 'g9-lineq-02'
CH = 'Phương trình và bất phương trình bậc nhất một ẩn'
TOPIC = ('Linear Equations and Linear Inequalities in One Variable', CH)
ensure_vocab([
 ('g9-ineq', 'inequality', 'bất đẳng thức', CH, 'An inequality is a statement comparing two expressions, such as a < b.', r'\(a\lt b\)'),
 ('g9-lhs', 'left-hand side (LHS)', 'vế trái', CH, 'In the inequality a < b, a is the left-hand side.', ''),
 ('g9-rhs', 'right-hand side (RHS)', 'vế phải', CH, 'In the inequality a < b, b is the right-hand side.', ''),
 ('g9-same-dir', 'same direction', 'cùng chiều', CH, 'a < b and c < d are inequalities of the same direction.', ''),
 ('g9-opp-dir', 'opposite direction', 'ngược chiều', CH, 'a < b and c > d are inequalities of the opposite direction.', ''),
 ('g9-ineq-sign', 'inequality sign', 'dấu bất đẳng thức', CH, 'When multiplying by a negative number, reverse the inequality sign.', r'\(\lt,\ \gt,\ \le,\ \ge\)'),
 ('g9-reverse', 'reverse the inequality sign', 'đổi chiều bất đẳng thức', CH, 'Multiply by −2 and reverse the inequality sign.', ''),
])
load_vocab()

# ---------- kiểm tra số liệu ----------
assert F(2026, 1012) > 2 > F(199, 100)
assert all(a * a + b * b >= 2 * a * b for a in range(-20, 21) for b in range(-20, 21))
assert all(n * n - (n - 1) * (n + 1) == 1 for n in range(1, 200))

meta = dict(level=('Beginner', 'Cơ bản'), time=('about 45 minutes', '45 phút'),
            before=('comparing real numbers (grade 7); the identity (a − b)²', 'so sánh hai số thực (lớp 7); hằng đẳng thức bình phương của một hiệu'))
goals = [
 (r'read and write inequalities \(a\lt b,\ a\gt b,\ a\le b,\ a\ge b\) and recognize their two sides;', r'đọc, viết được [[bất đẳng thức]] \(a\lt b,\ a\gt b,\ a\le b,\ a\ge b\) và chỉ ra [[vế trái]], [[vế phải]];'),
 (r'use the transitive property;', r'vận dụng [[tính chất bắc cầu]];'),
 (r'use the link between order and addition, and between order and multiplication;', r'vận dụng liên hệ giữa thứ tự và phép cộng, giữa thứ tự và phép nhân;'),
 (r'prove simple inequalities and describe real situations with inequalities.', r'chứng minh bất đẳng thức đơn giản và mô tả tình huống thực tế bằng bất đẳng thức.')]
vocab = [
 (r'<b>inequality</b> – a statement \(a\lt b\), \(a\gt b\), \(a\le b\) or \(a\ge b\).', r'[[Bất đẳng thức]] – hệ thức dạng \(a\lt b\), \(a\gt b\), \(a\le b\) hoặc \(a\ge b\).'),
 (r'<b>left-hand side / right-hand side</b> – the expression before / after the sign.', r'[[Vế trái]] / [[vế phải]] – biểu thức đứng trước / sau dấu bất đẳng thức.'),
 (r'<b>transitive property</b> – if \(a\lt b\) and \(b\lt c\) then \(a\lt c\).', r'[[Tính chất bắc cầu]] – nếu \(a\lt b\) và \(b\lt c\) thì \(a\lt c\).'),
 (r'<b>same direction / opposite direction</b> – \(a\lt b\) and \(c\lt d\) / \(a\lt b\) and \(c\gt d\).', r'[[Cùng chiều]] / [[ngược chiều]] – \(a\lt b\) và \(c\lt d\) / \(a\lt b\) và \(c\gt d\).'),
 (r'<b>reverse the inequality sign</b> – change \(\lt\) into \(\gt\) (and \(\le\) into \(\ge\)).', r'[[Đổi chiều bất đẳng thức]] – đổi \(\lt\) thành \(\gt\) (và \(\le\) thành \(\ge\)).')]
phrases = [
 (r'<b>\(a\lt b\)</b>: “\(a\) is (strictly) less than \(b\)”; <b>\(a\le b\)</b>: “\(a\) is less than or equal to \(b\)”.', r'\(a\lt b\): \(a\) nhỏ hơn \(b\); \(a\le b\): \(a\) nhỏ hơn hoặc bằng \(b\).'),
 (r'<b>Compare the values of the two numbers.</b>', r'So sánh giá trị của hai số.'),
 (r'<b>Write an inequality to represent the following situation.</b>', r'Viết bất đẳng thức mô tả tình huống sau.'),
 (r'<b>Add 3 to both sides of the inequality.</b>', r'Cộng 3 vào hai vế của bất đẳng thức.'),
 (r'<b>Multiply both sides by −2 and reverse the inequality sign.</b>', r'Nhân hai vế với −2 và đổi chiều bất đẳng thức.'),
 (r'<b>Prove the following inequality for any real number.</b>', r'Chứng minh bất đẳng thức sau với mọi số thực.')]
review = (T(r'<b>Comparing numbers.</b> For two real numbers \(a, b\), exactly one is true: \(a\lt b\), \(a=b\) or \(a\gt b\). On the number line, the smaller number is on the left.', r'<b>So sánh hai số.</b> Với hai số thực \(a, b\), luôn xảy ra đúng một trong ba trường hợp: \(a\lt b\), \(a=b\) hoặc \(a\gt b\). Trên trục số, số nhỏ hơn nằm bên trái.') +
          T(r'<b>Identity.</b> \((a-b)^2=a^2-2ab+b^2\ge0\) for every \(a, b\).', r'<b>Hằng đẳng thức.</b> \((a-b)^2=a^2-2ab+b^2\ge0\) với mọi \(a, b\).'))

theory = '<h3>5.1 %s</h3>' % TI('Inequalities', 'Bất đẳng thức')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'We call \(a\lt b\) (or \(a\gt b\), \(a\le b\), \(a\ge b\)) an <b>inequality</b>; \(a\) is the left-hand side and \(b\) is the right-hand side.', r'Ta gọi hệ thức dạng \(a\lt b\) (hay \(a\gt b\), \(a\le b\), \(a\ge b\)) là [[bất đẳng thức]]; \(a\) là [[vế trái]], \(b\) là [[vế phải]].'),
  T(r'<b>Transitive property:</b> if \(a\lt b\) and \(b\lt c\) then \(a\lt c\). (The same holds for \(\gt,\ \le,\ \ge\).)', r'[[Tính chất bắc cầu]]: nếu \(a\lt b\) và \(b\lt c\) thì \(a\lt c\). (Tương tự với \(\gt,\ \le,\ \ge\).)'))
theory += '<h3>5.2 %s</h3>' % TI('Order and addition', 'Liên hệ giữa thứ tự và phép cộng')
theory += BOX('mint', ('Property', 'Tính chất'),
  T(r'If \(a\lt b\) then \(a+c\lt b+c\) for every number \(c\). Adding (or subtracting) the same number on both sides keeps the direction.', r'Nếu \(a\lt b\) thì \(a+c\lt b+c\) với mọi số \(c\). Cộng (hoặc trừ) cùng một số vào hai vế, bất đẳng thức giữ nguyên chiều.'))
theory += '<h3>5.3 %s</h3>' % TI('Order and multiplication', 'Liên hệ giữa thứ tự và phép nhân')
theory += BOX('mint', ('Property', 'Tính chất'),
  UL([T(r'If \(a\lt b\) and \(c\gt0\) then \(ac\lt bc\): multiplying by a <b>positive</b> number keeps the direction.', r'Nếu \(a\lt b\) và \(c\gt0\) thì \(ac\lt bc\): nhân với số <b>dương</b>, bất đẳng thức giữ nguyên chiều.'),
      T(r'If \(a\lt b\) and \(c\lt0\) then \(ac\gt bc\): multiplying by a <b>negative</b> number reverses the direction.', r'Nếu \(a\lt b\) và \(c\lt0\) thì \(ac\gt bc\): nhân với số <b>âm</b>, bất đẳng thức [[đổi chiều|đổi chiều bất đẳng thức]].')]))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'),
  T(r'Dividing by \(c\) is multiplying by \(\dfrac{1}{c}\): divide by a negative number → reverse the sign. Example: \(-2x\lt 6\Leftrightarrow x\gt -3\).', r'Chia cho \(c\) là nhân với \(\dfrac{1}{c}\): chia cho số âm thì đổi chiều. Ví dụ: \(-2x\lt 6\Leftrightarrow x\gt -3\).'))

examples = EXAMPLE(1, ('Remembering', 'Biết'), ('Describe a situation', 'Mô tả tình huống bằng bất đẳng thức'),
  T(r'Write an inequality for each statement. a) The age \(a\) of a viewer must be at least 18. b) The load \(m\) (kg) of a lift cannot exceed 800 kg. c) The number of students \(s\) in a class is at most 45.', r'Viết bất đẳng thức mô tả mỗi câu. a) Tuổi \(a\) của người xem phải ít nhất là 18. b) Khối lượng \(m\) (kg) trong thang máy không được vượt quá 800 kg. c) Số học sinh \(s\) của một lớp nhiều nhất là 45.'),
  ('“at least” → \\(\\ge\\); “not exceed”, “at most” → \\(\\le\\).', '“ít nhất” → \\(\\ge\\); “không vượt quá”, “nhiều nhất” → \\(\\le\\).'),
  [T(r'a) \(a\ge 18\). b) \(m\le 800\). c) \(s\le 45\).', r'a) \(a\ge 18\). b) \(m\le 800\). c) \(s\le 45\).')],
  T(r'\(a\ge18\); \(m\le800\); \(s\le45\).', r'\(a\ge18\); \(m\le800\); \(s\le45\).'))
examples += EXAMPLE(2, ('Understanding', 'Hiểu'), ('Compare using a middle number', 'So sánh nhờ số trung gian'),
  T(r'Compare \(\dfrac{2026}{1012}\) and \(\dfrac{199}{100}\).', r'So sánh \(\dfrac{2026}{1012}\) và \(\dfrac{199}{100}\).'),
  ('Both fractions are close to 2. Compare each of them with 2.', 'Hai phân số đều gần bằng 2. So sánh từng phân số với 2.'),
  [T(r'\(\dfrac{2026}{1012}\gt\dfrac{2024}{1012}=2\) and \(\dfrac{199}{100}\lt\dfrac{200}{100}=2\).', r'\(\dfrac{2026}{1012}\gt\dfrac{2024}{1012}=2\) và \(\dfrac{199}{100}\lt\dfrac{200}{100}=2\).'),
   T(r'By the transitive property, \(\dfrac{199}{100}\lt2\lt\dfrac{2026}{1012}\).', r'Theo tính chất bắc cầu, \(\dfrac{199}{100}\lt2\lt\dfrac{2026}{1012}\).')],
  T(r'\(\dfrac{2026}{1012}\gt\dfrac{199}{100}\).', r'\(\dfrac{2026}{1012}\gt\dfrac{199}{100}\).'))
examples += EXAMPLE(3, ('Understanding', 'Hiểu'), ('Use the properties', 'Vận dụng các tính chất'),
  T(r'Given \(a\lt b\). Prove that a) \(2a+3\lt 2b+3\); b) \(-2a-3b+1\gt -5b+1\).', r'Cho \(a\lt b\). Chứng minh: a) \(2a+3\lt 2b+3\); b) \(-2a-3b+1\gt -5b+1\).'),
  ('Multiply first, then add. Watch the sign of the number you multiply by.', 'Nhân trước rồi cộng. Chú ý dấu của số nhân vào.'),
  [T(r'a) \(a\lt b\) and \(2\gt0\): \(2a\lt 2b\). Add 3: \(2a+3\lt 2b+3\).', r'a) \(a\lt b\) và \(2\gt0\) nên \(2a\lt 2b\). Cộng 3 vào hai vế: \(2a+3\lt 2b+3\).'),
   T(r'b) \(a\lt b\) and \(-2\lt0\): \(-2a\gt -2b\). Add \(-3b+1\) to both sides: \(-2a-3b+1\gt -2b-3b+1=-5b+1\).', r'b) \(a\lt b\) và \(-2\lt0\) nên \(-2a\gt -2b\). Cộng \(-3b+1\) vào hai vế: \(-2a-3b+1\gt -2b-3b+1=-5b+1\).')],
  T(r'Both inequalities are proved.', r'Hai bất đẳng thức đã được chứng minh.'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('A classic inequality', 'Một bất đẳng thức quen thuộc'),
  T(r'Prove that \(a^2+b^2\ge 2ab\) for any real numbers \(a, b\). When does equality hold?', r'Chứng minh \(a^2+b^2\ge 2ab\) với mọi số thực \(a, b\). Khi nào xảy ra dấu bằng?'),
  ('Look at the difference LHS − RHS.', 'Xét hiệu vế trái trừ vế phải.'),
  [T(r'\(a^2+b^2-2ab=(a-b)^2\).', r'\(a^2+b^2-2ab=(a-b)^2\).'),
   T(r'\((a-b)^2\ge0\) for all \(a, b\), so \(a^2+b^2\ge 2ab\). Equality holds when \(a=b\).', r'\((a-b)^2\ge0\) với mọi \(a, b\) nên \(a^2+b^2\ge 2ab\). Dấu bằng xảy ra khi \(a=b\).')],
  T(r'\(a^2+b^2\ge2ab\); equality when \(a=b\).', r'\(a^2+b^2\ge2ab\); dấu bằng khi \(a=b\).'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Three consecutive numbers', 'Ba số tự nhiên liên tiếp'),
  T(r'Prove that for three consecutive natural numbers, the square of the middle number is greater than the product of the other two.', r'Chứng minh rằng trong ba số tự nhiên liên tiếp, bình phương số ở giữa lớn hơn tích của hai số còn lại.'),
  ('Call the numbers \\(n-1,\\ n,\\ n+1\\) and compare \\(n^2\\) with \\((n-1)(n+1)\\).', 'Gọi ba số là \\(n-1,\\ n,\\ n+1\\) rồi so sánh \\(n^2\\) với \\((n-1)(n+1)\\).'),
  [T(r'\((n-1)(n+1)=n^2-1\).', r'\((n-1)(n+1)=n^2-1\).'),
   T(r'\(n^2-(n^2-1)=1\gt0\), so \(n^2\gt (n-1)(n+1)\). Check: \(5^2=25\gt 4\cdot6=24\).', r'\(n^2-(n^2-1)=1\gt0\) nên \(n^2\gt (n-1)(n+1)\). Thử: \(5^2=25\gt 4\cdot6=24\).')],
  T(r'The square of the middle number is always 1 more than the product of the other two.', r'Bình phương số ở giữa luôn lớn hơn tích hai số còn lại đúng 1 đơn vị.'))

_SETS = sp_g9.BANK(sp_g9.L5_GROUPS, start=1, seeds=(1501, 1502, 1503))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Not reversing the sign.</b> From \(a\lt b\): \(-3a\gt -3b\), not \(-3a\lt -3b\).', r'<b>Quên đổi chiều.</b> Từ \(a\lt b\) suy ra \(-3a\gt -3b\), không phải \(-3a\lt -3b\).'),
 (r'<b>Reversing when adding a negative number.</b> \(a\lt b\Rightarrow a-5\lt b-5\): adding never changes the direction.', r'<b>Đổi chiều khi cộng số âm.</b> \(a\lt b\Rightarrow a-5\lt b-5\): phép cộng không làm đổi chiều.'),
 (r'<b>Mixing up “at least” and “at most”.</b> At least → \(\ge\); at most → \(\le\).', r'<b>Nhầm “ít nhất” với “nhiều nhất”.</b> Ít nhất → \(\ge\); nhiều nhất → \(\le\).'),
 (r'<b>Squaring both sides.</b> \(a\ge b\) does not always give \(a^2\ge b^2\): \(1\ge-2\) but \(1\lt4\).', r'<b>Bình phương hai vế.</b> \(a\ge b\) chưa chắc suy ra \(a^2\ge b^2\): \(1\ge-2\) nhưng \(1\lt4\).')]
summary = [
 (r'Inequality: \(a\lt b,\ a\gt b,\ a\le b,\ a\ge b\); LHS before the sign, RHS after it.', r'Bất đẳng thức: \(a\lt b,\ a\gt b,\ a\le b,\ a\ge b\); vế trái đứng trước dấu, vế phải đứng sau.'),
 (r'Transitive: \(a\lt b,\ b\lt c\Rightarrow a\lt c\).', r'Bắc cầu: \(a\lt b,\ b\lt c\Rightarrow a\lt c\).'),
 (r'Adding the same number keeps the direction; multiplying by a positive number keeps it; by a negative number reverses it.', r'Cộng cùng một số: giữ chiều; nhân với số dương: giữ chiều; nhân với số âm: đổi chiều.'),
 (r'To prove \(A\ge B\), show that \(A-B\ge0\) (often a square).', r'Để chứng minh \(A\ge B\), chứng minh \(A-B\ge0\) (thường là một bình phương).'),
 (r'Key English: inequality, left-hand side, right-hand side, reverse the inequality sign.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[bất đẳng thức]], [[vế trái]], [[vế phải]], [[đổi chiều bất đẳng thức]].')]
checks = [
 (r'I can read and write inequalities and name their two sides.', r'Em đọc, viết được bất đẳng thức và chỉ ra hai vế.'),
 (r'I can use the transitive property.', r'Em vận dụng được tính chất bắc cầu.'),
 (r'I know when to keep and when to reverse the sign.', r'Em biết khi nào giữ chiều, khi nào đổi chiều bất đẳng thức.'),
 (r'I can prove simple inequalities such as \(a^2+b^2\ge2ab\).', r'Em chứng minh được bất đẳng thức đơn giản như \(a^2+b^2\ge2ab\).'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Inequalities and Their Properties', title_vi='Bất đẳng thức và tính chất', topic=TOPIC,
       folder='equations-and-inequalities', file='inequalities-properties', catalog_title_vi='Bất đẳng thức và tính chất',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Inequalities, the transitive property, and the links between order and addition or multiplication.', level='Beginner', minutes=45,
       description_vi='Bài 5 – Bất đẳng thức, tính chất bắc cầu, liên hệ giữa thứ tự với phép cộng và phép nhân.',
       tags_vi=['bất đẳng thức', 'tính chất bắc cầu', 'đổi chiều'],
       prerequisites=[], tags=['inequality', 'order', 'transitive'], order=50)
