# -*- coding: utf-8 -*-
"""Nội dung bài g9-lineq-01 = Toán 9 KNTT, Bài 4: Phương trình quy về phương trình bậc nhất một ẩn – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 2 – Lesson 4, tr. 15–17 (product equation, denominator, restriction, Zero-Product Property)."""
import os, sys
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9

LID = 'g9-lineq-01'
CH = 'Phương trình và bất phương trình bậc nhất một ẩn'
TOPIC = ('Linear Equations and Linear Inequalities in One Variable', CH)
ensure_vocab([
 ('g9-lin1', 'linear equation in one variable', 'phương trình bậc nhất một ẩn', CH, 'A linear equation in one variable has the form ax + b = 0 (a ≠ 0).', r'\(ax+b=0\)'),
 ('g9-product-eq', 'product equation', 'phương trình tích', CH, '(x + 1)(x − 1) = 0 is a product equation.', r'\(A\cdot B=0\)'),
 ('g9-zero-product', 'Zero-Product Property', 'tính chất tích bằng 0', CH, 'By the Zero-Product Property, if A · B = 0 then A = 0 or B = 0.', ''),
 ('g9-common-factor', 'common factor', 'nhân tử chung', CH, 'Take out the common factor x + 1.', ''),
 ('g9-denom-alg', 'denominator', 'mẫu thức', CH, 'In (x + 1)/(x − 1), x − 1 is the denominator.', ''),
 ('g9-common-denom', 'common denominator', 'mẫu thức chung', CH, 'The common denominator of 1/(x − 1) and 1/(x + 1) is (x + 1)(x − 1).', ''),
 ('g9-frac-eq', 'equation with the variable in the denominator', 'phương trình chứa ẩn ở mẫu', CH, '1/(x − 2) + 3 = (x − 3)/(2 − x) has the variable in the denominator.', ''),
 ('g9-restriction', 'condition for the equation to be defined (restriction)', 'điều kiện xác định', CH, 'The restriction of (x + 1)/(x − 1) is x ≠ 1.', ''),
 ('g9-clear-denom', 'clear the denominators', 'khử mẫu', CH, 'Multiply both sides by the common denominator to clear the denominators.', ''),
 ('g9-downstream', 'downstream', 'xuôi dòng', CH, 'The boat goes 36 km downstream.', ''),
 ('g9-upstream', 'upstream', 'ngược dòng', CH, 'Going upstream, the boat is slower.', ''),
 ('g9-still-water', 'speed in still water', 'vận tốc riêng', CH, 'Find the speed of the boat in still water.', ''),
])
load_vocab()

# ---------- kiểm tra số liệu ----------
def roots(f, cand): return [x for x in cand if f(x) == 0]
C = sorted({F(n, d) for n in range(-40, 41) for d in (1, 2, 3, 4)})
assert sorted(set(roots(lambda x: (2 * x + 1) * (3 * x - 6), C))) == [F(-1, 2), 2]                     # Ví dụ 1
assert sorted(set(roots(lambda x: (x * x - 1) + (x + 1) * (x - 2), C))) == [-1, F(3, 2)]               # Ví dụ 2
assert [x for x in C if x not in (0, 2) and (x + 3) / x == (x + 2) / (x - 2)] == [-6]                   # Ví dụ 3
assert [x for x in C if x != 2 and 1 / (x - 2) + 3 == (x - 3) / (2 - x)] == []                          # Ví dụ 4: vô nghiệm
assert F(36, 15 + 3) == F(24, 15 - 3) == 2                                                             # Ví dụ 5

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 60 minutes', '60 phút'),
            before=('factoring polynomials; algebraic fractions (grade 8); linear equations in one variable', 'phân tích đa thức thành nhân tử; phân thức đại số (lớp 8); phương trình bậc nhất một ẩn'))
goals = [
 (r'solve a product equation \((ax+b)(cx+d)=0\), and turn an equation into a product by factoring;', r'giải được [[phương trình tích]] \((ax+b)(cx+d)=0\) và đưa phương trình về dạng tích bằng cách [[phân tích thành nhân tử]];'),
 (r'find the condition for an equation with the variable in the denominator to be defined;', r'tìm được [[điều kiện xác định]] của [[phương trình chứa ẩn ở mẫu]];'),
 (r'solve such an equation in four steps and reject values that break the condition;', r'giải được phương trình chứa ẩn ở mẫu theo bốn bước và loại các giá trị không thỏa mãn điều kiện;'),
 (r'solve simple real-world problems that lead to these equations.', r'giải được một số bài toán thực tế dẫn đến các phương trình này.')]
vocab = [
 (r'<b>linear equation in one variable</b> – \(ax+b=0\) with \(a\ne0\).', r'[[Phương trình bậc nhất một ẩn]] – phương trình dạng \(ax+b=0\) với \(a\ne0\).'),
 (r'<b>product equation</b> – an equation of the form \(A\cdot B=0\).', r'[[Phương trình tích]] – phương trình có dạng \(A\cdot B=0\).'),
 (r'<b>Zero-Product Property</b> – if \(A\cdot B=0\) then \(A=0\) or \(B=0\).', r'[[Tính chất tích bằng 0]] – nếu \(A\cdot B=0\) thì \(A=0\) hoặc \(B=0\).'),
 (r'<b>factor (v)</b> – write as a product: \(x^2-1=(x+1)(x-1)\).', r'[[Phân tích thành nhân tử]] – viết thành một tích: \(x^2-1=(x+1)(x-1)\).'),
 (r'<b>common factor</b> – a factor that appears in every term, like \(x+1\) in \((x+1)(x-2)+3(x+1)\).', r'[[Nhân tử chung]] – nhân tử có mặt trong mọi hạng tử, như \(x+1\) trong \((x+1)(x-2)+3(x+1)\).'),
 (r'<b>denominator / common denominator</b> – the bottom of a fraction / an expression divisible by all denominators.', r'[[Mẫu thức]] / [[mẫu thức chung]] – phần ở dưới dấu gạch phân số / biểu thức chia hết cho mọi mẫu thức.'),
 (r'<b>restriction</b> – the condition for the equation to be defined: every denominator is different from 0.', r'[[Điều kiện xác định]] – điều kiện để mọi mẫu thức của phương trình khác 0.'),
 (r'<b>clear the denominators</b> – multiply both sides by the common denominator.', r'[[Khử mẫu]] – nhân hai vế với mẫu thức chung để mất mẫu.')]
phrases = [
 (r'<b>Solve the equation / product equation.</b>', r'Giải phương trình / phương trình tích.'),
 (r'<b>Factor the left-hand side.</b>', r'Phân tích vế trái thành nhân tử.'),
 (r'<b>By the Zero-Product Property, \(x+1=0\) or \(x-1=0\).</b>', r'Theo tính chất tích bằng 0, \(x+1=0\) hoặc \(x-1=0\).'),
 (r'<b>Find the restriction (the condition for the equation to be defined).</b>', r'Tìm điều kiện xác định của phương trình.'),
 (r'<b>Multiply both sides by the common denominator.</b>', r'Nhân hai vế với mẫu thức chung.'),
 (r'<b>\(x=2\) does not satisfy the restriction, so it is rejected.</b>', r'\(x=2\) không thỏa mãn điều kiện xác định nên bị loại.')]
review = (T(r'<b>Linear equation in one variable.</b> \(ax+b=0\ (a\ne0)\Leftrightarrow x=-\dfrac{b}{a}\).', r'<b>Phương trình bậc nhất một ẩn.</b> \(ax+b=0\ (a\ne0)\Leftrightarrow x=-\dfrac{b}{a}\).') +
          T(r'<b>Factoring (grade 8).</b> Common factor: \(ax+ay=a(x+y)\). Difference of two squares: \(A^2-B^2=(A-B)(A+B)\).', r'<b>Phân tích đa thức thành nhân tử (lớp 8).</b> Đặt nhân tử chung: \(ax+ay=a(x+y)\). Hiệu hai bình phương: \(A^2-B^2=(A-B)(A+B)\).'))

theory = '<h3>5.1 %s</h3>' % TI('Product equations', 'Phương trình tích')
theory += BOX('blue', ('How to solve', 'Cách giải'),
  T(r'By the <b>Zero-Product Property</b>, \((a_1x+b_1)(a_2x+b_2)=0\) means \(a_1x+b_1=0\) <b>or</b> \(a_2x+b_2=0\).', r'Theo [[tính chất tích bằng 0]], \((a_1x+b_1)(a_2x+b_2)=0\) khi và chỉ khi \(a_1x+b_1=0\) <b>hoặc</b> \(a_2x+b_2=0\).'),
  T(r'Solve the two linear equations and take <b>all</b> the solutions found.', r'Giải hai phương trình bậc nhất rồi lấy <b>tất cả</b> các nghiệm tìm được.'))
theory += BOX('mint', ('Turning an equation into a product', 'Đưa phương trình về dạng tích'),
  T(r'Move all terms to the left-hand side so that the right-hand side is 0, then factor the left-hand side (common factor, identities…).', r'Chuyển mọi hạng tử sang vế trái để vế phải bằng 0, rồi [[phân tích thành nhân tử]] vế trái (đặt [[nhân tử chung]], dùng hằng đẳng thức…).'),
  T(r'Example: \(x^2-4x=0\Leftrightarrow x(x-4)=0\Leftrightarrow x=0\) or \(x=4\).', r'Ví dụ: \(x^2-4x=0\Leftrightarrow x(x-4)=0\Leftrightarrow x=0\) hoặc \(x=4\).'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'),
  T(r'Do not divide both sides by an expression containing \(x\) (for example by \(x\)): you may lose a solution.', r'Không chia hai vế cho một biểu thức chứa ẩn (chẳng hạn chia cho \(x\)) vì có thể làm mất nghiệm.'))
theory += '<h3>5.2 %s</h3>' % TI('Equations with the variable in the denominator', 'Phương trình chứa ẩn ở mẫu')
theory += BOX('blue', ('Restriction', 'Điều kiện xác định'),
  T(r'The <b>condition for the equation to be defined</b> (restriction) is that <b>every denominator is different from 0</b>. Example: \(\dfrac{x+1}{x-1}=\dfrac{2}{x+3}\) needs \(x\ne1\) and \(x\ne-3\).', r'[[Điều kiện xác định]] của phương trình là <b>mọi mẫu thức đều khác 0</b>. Ví dụ: phương trình \(\dfrac{x+1}{x-1}=\dfrac{2}{x+3}\) có điều kiện xác định \(x\ne1\) và \(x\ne-3\).'))
theory += BOX('mint', ('Four steps', 'Bốn bước giải'),
  UL([T(r'<b>Step 1.</b> Find the restriction.', r'<b>Bước 1.</b> Tìm điều kiện xác định của phương trình.'),
      T(r'<b>Step 2.</b> Rewrite both sides with the common denominator, then clear the denominators.', r'<b>Bước 2.</b> Quy đồng mẫu hai vế rồi [[khử mẫu]].'),
      T(r'<b>Step 3.</b> Solve the new equation.', r'<b>Bước 3.</b> Giải phương trình vừa nhận được.'),
      T(r'<b>Step 4.</b> Conclude: only the values that satisfy the restriction are solutions.', r'<b>Bước 4.</b> Kết luận: trong các giá trị tìm được, chỉ những giá trị thỏa mãn điều kiện xác định mới là nghiệm.')]))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('A product equation', 'Giải phương trình tích'),
  T(r'Solve \((2x+1)(3x-6)=0\).', r'Giải phương trình \((2x+1)(3x-6)=0\).'),
  ('Use the Zero-Product Property.', 'Dùng tính chất tích bằng 0.'),
  [T(r'\(2x+1=0\Rightarrow x=-\dfrac{1}{2}\).', r'\(2x+1=0\Rightarrow x=-\dfrac{1}{2}\).'),
   T(r'\(3x-6=0\Rightarrow x=2\).', r'\(3x-6=0\Rightarrow x=2\).')],
  T(r'\(x=-\dfrac{1}{2}\) or \(x=2\).', r'Phương trình có hai nghiệm \(x=-\dfrac{1}{2}\) và \(x=2\).'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Factor first', 'Đưa về phương trình tích'),
  T(r'Solve \((x^2-1)+(x+1)(x-2)=0\).', r'Giải phương trình \((x^2-1)+(x+1)(x-2)=0\).'),
  ('\\(x^2-1=(x+1)(x-1)\\), so \\(x+1\\) is a common factor.', '\\(x^2-1=(x+1)(x-1)\\) nên \\(x+1\\) là nhân tử chung.'),
  [T(r'\((x+1)(x-1)+(x+1)(x-2)=0\Leftrightarrow(x+1)(x-1+x-2)=0\Leftrightarrow(x+1)(2x-3)=0\).', r'\((x+1)(x-1)+(x+1)(x-2)=0\Leftrightarrow(x+1)(x-1+x-2)=0\Leftrightarrow(x+1)(2x-3)=0\).'),
   T(r'\(x+1=0\Rightarrow x=-1\); \(2x-3=0\Rightarrow x=\dfrac{3}{2}\).', r'\(x+1=0\Rightarrow x=-1\); \(2x-3=0\Rightarrow x=\dfrac{3}{2}\).')],
  T(r'\(x=-1\) or \(x=\dfrac{3}{2}\).', r'Phương trình có hai nghiệm \(x=-1\) và \(x=\dfrac{3}{2}\).'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('Four steps', 'Giải phương trình chứa ẩn ở mẫu'),
  T(r'Solve \(\dfrac{x+3}{x}=\dfrac{x+2}{x-2}\).', r'Giải phương trình \(\dfrac{x+3}{x}=\dfrac{x+2}{x-2}\).'),
  ('The denominators are \\(x\\) and \\(x-2\\).', 'Các mẫu thức là \\(x\\) và \\(x-2\\).'),
  [T(r'Restriction: \(x\ne0\) and \(x\ne2\).', r'Điều kiện xác định: \(x\ne0\) và \(x\ne2\).'),
   T(r'Common denominator \(x(x-2)\): \((x+3)(x-2)=x(x+2)\).', r'Mẫu thức chung \(x(x-2)\). Quy đồng và khử mẫu: \((x+3)(x-2)=x(x+2)\).'),
   T(r'\(x^2+x-6=x^2+2x\Leftrightarrow -x=6\Leftrightarrow x=-6\).', r'\(x^2+x-6=x^2+2x\Leftrightarrow -x=6\Leftrightarrow x=-6\).'),
   T(r'\(x=-6\) satisfies the restriction.', r'\(x=-6\) thỏa mãn điều kiện xác định.')],
  T(r'\(x=-6\).', r'Phương trình có nghiệm \(x=-6\).'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('A value that must be rejected', 'Giá trị bị loại'),
  T(r'Solve \(\dfrac{1}{x-2}+3=\dfrac{x-3}{2-x}\).', r'Giải phương trình \(\dfrac{1}{x-2}+3=\dfrac{x-3}{2-x}\).'),
  ('Note that \\(2-x=-(x-2)\\), so the common denominator is \\(x-2\\).', 'Chú ý \\(2-x=-(x-2)\\) nên mẫu thức chung là \\(x-2\\).'),
  [T(r'Restriction: \(x\ne2\).', r'Điều kiện xác định: \(x\ne2\).'),
   T(r'Rewrite: \(\dfrac{1}{x-2}+3=\dfrac{-(x-3)}{x-2}\). Clear the denominators: \(1+3(x-2)=-(x-3)\).', r'Viết lại: \(\dfrac{1}{x-2}+3=\dfrac{-(x-3)}{x-2}\). Khử mẫu: \(1+3(x-2)=-(x-3)\).'),
   T(r'\(3x-5=-x+3\Leftrightarrow 4x=8\Leftrightarrow x=2\).', r'\(3x-5=-x+3\Leftrightarrow 4x=8\Leftrightarrow x=2\).'),
   T(r'\(x=2\) does <b>not</b> satisfy the restriction, so it is rejected.', r'\(x=2\) <b>không</b> thỏa mãn điều kiện xác định nên bị loại.')],
  T(r'The equation has no solution.', r'Phương trình vô nghiệm.'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('A boat on a river', 'Ca nô trên sông'),
  T(r'A boat goes 36 km downstream and then 24 km upstream. The two trips take the same time. The current flows at 3 km/h. Find the speed of the boat in still water.', r'Một ca nô xuôi dòng 36 km rồi ngược dòng 24 km; thời gian xuôi dòng bằng thời gian ngược dòng. Vận tốc dòng nước là 3 km/h. Tính vận tốc riêng của ca nô (vận tốc khi nước yên lặng).'),
  ('Downstream speed \\(x+3\\), upstream speed \\(x-3\\); time = distance : speed.', 'Vận tốc xuôi dòng \\(x+3\\), ngược dòng \\(x-3\\); thời gian = quãng đường : vận tốc.'),
  [T(r'Let \(x\) (km/h) be the speed in still water, \(x\gt3\). Times: \(\dfrac{36}{x+3}\) h and \(\dfrac{24}{x-3}\) h.', r'Gọi \(x\) (km/h) là vận tốc riêng của ca nô, \(x\gt3\). Thời gian xuôi dòng \(\dfrac{36}{x+3}\) giờ, ngược dòng \(\dfrac{24}{x-3}\) giờ.'),
   T(r'\(\dfrac{36}{x+3}=\dfrac{24}{x-3}\Rightarrow 36(x-3)=24(x+3)\Rightarrow 12x=180\Rightarrow x=15\).', r'\(\dfrac{36}{x+3}=\dfrac{24}{x-3}\Rightarrow 36(x-3)=24(x+3)\Rightarrow 12x=180\Rightarrow x=15\).'),
   T(r'\(15\gt3\) ✓. Check: \(36:18=2\) h and \(24:12=2\) h.', r'\(15\gt3\) ✓. Thử lại: \(36:18=2\) giờ, \(24:12=2\) giờ.')],
  T(r'The speed in still water is 15 km/h.', r'Vận tốc riêng của ca nô là 15 km/h.'))

_SETS = sp_g9.BANK(sp_g9.L4_GROUPS, start=1, seeds=(1401, 1402, 1403))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Dividing by \(x\).</b> \(x^2=3x\Rightarrow x=3\) loses \(x=0\). Factor instead: \(x(x-3)=0\).', r'<b>Chia hai vế cho \(x\).</b> \(x^2=3x\Rightarrow x=3\) làm mất nghiệm \(x=0\). Hãy phân tích: \(x(x-3)=0\).'),
 (r'<b>Using “and” instead of “or”.</b> \(A\cdot B=0\) means \(A=0\) <b>or</b> \(B=0\).', r'<b>Dùng “và” thay cho “hoặc”.</b> \(A\cdot B=0\) khi \(A=0\) <b>hoặc</b> \(B=0\).'),
 (r'<b>Wrong sign of a root.</b> \(x+5=0\Rightarrow x=-5\), not \(x=5\).', r'<b>Sai dấu nghiệm.</b> \(x+5=0\Rightarrow x=-5\), không phải \(x=5\).'),
 (r'<b>Forgetting the restriction.</b> After solving, check every value: \(x=2\) in Example 4 must be rejected.', r'<b>Quên điều kiện xác định.</b> Giải xong phải đối chiếu từng giá trị: \(x=2\) ở Ví dụ 4 bị loại.'),
 (r'<b>Clearing only one side.</b> Multiply <b>every</b> term of both sides by the common denominator.', r'<b>Chỉ khử mẫu một vế.</b> Phải nhân <b>mọi</b> hạng tử của cả hai vế với mẫu thức chung.')]
summary = [
 (r'\(A\cdot B=0\Leftrightarrow A=0\) or \(B=0\). Move everything to one side and factor.', r'\(A\cdot B=0\Leftrightarrow A=0\) hoặc \(B=0\). Chuyển hết sang một vế rồi phân tích thành nhân tử.'),
 (r'Equation with the variable in the denominator: restriction → common denominator, clear → solve → keep only values that satisfy the restriction.', r'Phương trình chứa ẩn ở mẫu: điều kiện xác định → quy đồng, khử mẫu → giải → chỉ nhận giá trị thỏa mãn điều kiện.'),
 (r'In word problems, time = distance : speed; downstream speed = \(x+v\), upstream speed = \(x-v\).', r'Trong bài toán thực tế: thời gian = quãng đường : vận tốc; vận tốc xuôi dòng \(x+v\), ngược dòng \(x-v\).'),
 (r'Key English: product equation, Zero-Product Property, restriction, common denominator.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[phương trình tích]], [[tính chất tích bằng 0]], [[điều kiện xác định]], [[mẫu thức chung]].')]
checks = [
 (r'I can solve a product equation.', r'Em giải được phương trình tích.'),
 (r'I can factor an equation to get a product equation.', r'Em đưa được phương trình về dạng tích bằng cách phân tích thành nhân tử.'),
 (r'I can find the restriction of an equation with the variable in the denominator.', r'Em tìm được điều kiện xác định của phương trình chứa ẩn ở mẫu.'),
 (r'I can solve such equations and reject the values that break the restriction.', r'Em giải được phương trình chứa ẩn ở mẫu và loại được giá trị không thỏa mãn điều kiện.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Equations Reducible to Linear Equations in One Variable', title_vi='Phương trình quy về phương trình bậc nhất một ẩn', topic=TOPIC,
       folder='equations-and-inequalities', file='equations-reducible-to-linear', catalog_title_vi='Phương trình quy về phương trình bậc nhất một ẩn',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Product equations and equations with the variable in the denominator.', level='Intermediate', minutes=60,
       description_vi='Bài 4 – Phương trình tích và phương trình chứa ẩn ở mẫu; điều kiện xác định và bốn bước giải.',
       tags_vi=['phương trình tích', 'phương trình chứa ẩn ở mẫu', 'điều kiện xác định', 'phân tích thành nhân tử'],
       prerequisites=[], tags=['product equation', 'rational equation', 'restriction'], order=40)
