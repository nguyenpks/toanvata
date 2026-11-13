# -*- coding: utf-8 -*-
"""Nội dung bài g9-quadratic-03 = Toán 9 KNTT, Bài 20: Định lí Viète và ứng dụng – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 6 – Lesson 20."""
import os, sys, math
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9

LID = 'g9-quadratic-03'
CH = 'Hàm số y = ax² (a ≠ 0). Phương trình bậc hai một ẩn'
TOPIC = ('Quadratic Function and Quadratic Equation', CH)
ensure_vocab([
 ('g9-viete', "Viète's theorem (Vieta's formulas)", 'định lí Viète', CH, "By Viète's theorem, x₁ + x₂ = −b/a and x₁x₂ = c/a.", ''),
 ('g9-sum-roots', 'sum of the roots', 'tổng hai nghiệm', CH, 'The sum of the roots is −b/a.', r'\(S\)'),
 ('g9-prod-roots', 'product of the roots', 'tích hai nghiệm', CH, 'The product of the roots is c/a.', r'\(P\)'),
 ('g9-inspection', 'solve by inspection', 'nhẩm nghiệm', CH, 'If a + b + c = 0, we can solve the equation by inspection.', ''),
 ('g9-remaining-root', 'the remaining root', 'nghiệm còn lại', CH, 'Find the remaining root, given that one root is 3.', ''),
 ('g9-without-solving', 'without solving the equation', 'không giải phương trình', CH, 'Without solving the equation, find the sum of its roots.', ''),
 ('g9-factorise', 'factorise', 'phân tích thành nhân tử', CH, 'Factorise x² + 11x + 18.', ''),
])
load_vocab()

# ---------- kiểm tra số liệu ----------
assert 7 * 7 - 4 * 2 * 3 == 25 and (F(7, 2), F(3, 2)) == (F(-(-7), 2), F(3, 2))
assert 1 - 6 + 5 == 0 and 5 - 14 + 9 == 0 and F(-9, 5) == F(-9, 5)
assert sorted([4, 5]) == [4, 5] and 4 + 5 == 9 and 4 * 5 == 20
assert 2 + 9 == 11 and 2 * 9 == 18 and 3 * (F(1, 3)) * (-2) == -2   # x²+11x+18 = (x+2)(x+9); 3x²+5x−2 = 3(x−1/3)(x+2)
L = [x for x in range(1, 20) if x * (20 - x) == 96]; assert L == [8, 12]

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 75 minutes', '75 phút'), before=('Lesson 19: quadratic equations', 'Bài 19: phương trình bậc hai một ẩn'))
goals = [
 (r"state Viète's theorem;", r'phát biểu được định lí Viète;'),
 (r'find the sum and the product of the roots without solving (when \(\Delta\ge0\));', r'tính được tổng, tích các nghiệm mà không giải phương trình (khi \(\Delta\ge0\));'),
 (r'solve equations by inspection when \(a+b+c=0\) or \(a-b+c=0\);', r'nhẩm được nghiệm khi \(a+b+c=0\) hoặc \(a-b+c=0\);'),
 (r'find two numbers from their sum and product; solve real-life problems.', r'tìm được hai số khi biết tổng và tích; giải bài toán thực tế.')]
vocab = [
 (r"<b>Viète's theorem</b> – \(x_1+x_2=-\dfrac ba\), \(x_1x_2=\dfrac ca\).", r'[[Định lí Viète]] – \(x_1+x_2=-\dfrac ba\), \(x_1x_2=\dfrac ca\).'),
 (r'<b>sum / product of the roots</b> – \(S=x_1+x_2\), \(P=x_1x_2\).', r'[[Tổng hai nghiệm]] / [[tích hai nghiệm]] – \(S=x_1+x_2\), \(P=x_1x_2\).'),
 (r'<b>solve by inspection</b> – find the roots mentally, e.g. when \(a+b+c=0\).', r'[[Nhẩm nghiệm]] – tìm nghiệm không cần công thức, ví dụ khi \(a+b+c=0\).'),
 (r'<b>the remaining root</b> – the other root when one root is known.', r'[[Nghiệm còn lại]] – nghiệm kia khi đã biết một nghiệm.'),
 (r'<b>without solving the equation</b> – using only \(a\), \(b\), \(c\).', r'[[Không giải phương trình]] – chỉ dùng các hệ số \(a\), \(b\), \(c\).')]
phrases = [
 (r"<b>By Viète's theorem, the sum of the roots is \(-\dfrac ba\).</b>", r'Theo định lí Viète, tổng hai nghiệm bằng \(-\dfrac ba\).'),
 (r'<b>First check that \(\Delta\ge0\).</b>', r'Trước hết kiểm tra \(\Delta\ge0\).'),
 (r'<b>Since \(a+b+c=0\), the equation has the roots \(1\) and \(\dfrac ca\).</b>', r'Vì \(a+b+c=0\) nên phương trình có hai nghiệm \(1\) và \(\dfrac ca\).'),
 (r'<b>The two numbers are the roots of \(x^2-Sx+P=0\).</b>', r'Hai số đó là nghiệm của phương trình \(x^2-Sx+P=0\).'),
 (r'<b>Find the remaining root.</b>', r'Tìm nghiệm còn lại.')]
review = (T(r'<b>Lesson 19.</b> If \(\Delta\ge0\): \(x_{1,2}=\dfrac{-b\pm\sqrt\Delta}{2a}\).', r'<b>Bài 19.</b> Nếu \(\Delta\ge0\): \(x_{1,2}=\dfrac{-b\pm\sqrt\Delta}{2a}\).') +
          T(r'<b>Identity.</b> \(x_1^2+x_2^2=(x_1+x_2)^2-2x_1x_2\).', r'<b>Hằng đẳng thức.</b> \(x_1^2+x_2^2=(x_1+x_2)^2-2x_1x_2\).'))

theory = '<h3>5.1 %s</h3>' % TI("Viète's theorem", 'Định lí Viète')
theory += BOX('blue', ('Theorem', 'Định lí'),
  T(r'If \(x_1\), \(x_2\) are the roots of \(ax^2+bx+c=0\ (a\ne0)\), then', r'Nếu \(x_1\), \(x_2\) là hai nghiệm của phương trình \(ax^2+bx+c=0\ (a\ne0)\) thì'),
  M(r'x_1+x_2=-\dfrac ba,\qquad x_1x_2=\dfrac ca'),
  T(r'The theorem is used only when the equation has roots, that is \(\Delta\ge0\). Proof: add and multiply the two roots \(\dfrac{-b\pm\sqrt\Delta}{2a}\).', r'Chỉ áp dụng khi phương trình có nghiệm, tức \(\Delta\ge0\). Chứng minh: cộng và nhân hai nghiệm \(\dfrac{-b\pm\sqrt\Delta}{2a}\).'))
theory += '<h3>5.2 %s</h3>' % TI('Applications', 'Ứng dụng')
theory += BOX('mint', ('Solving by inspection', 'Nhẩm nghiệm'),
  T(r'If \(a+b+c=0\): roots \(x_1=1\), \(x_2=\dfrac ca\). If \(a-b+c=0\): roots \(x_1=-1\), \(x_2=-\dfrac ca\).', r'Nếu \(a+b+c=0\): \(x_1=1\), \(x_2=\dfrac ca\). Nếu \(a-b+c=0\): \(x_1=-1\), \(x_2=-\dfrac ca\).'))
theory += BOX('yellow', ('Two numbers from their sum and product', 'Tìm hai số biết tổng và tích'),
  T(r'If two numbers have sum \(S\) and product \(P\), they are the roots of \(x^2-Sx+P=0\) (this requires \(S^2-4P\ge0\)).', r'Nếu hai số có tổng \(S\) và tích \(P\) thì chúng là nghiệm của phương trình \(x^2-Sx+P=0\) (điều kiện \(S^2-4P\ge0\)).'),
  T(r'Factorisation: if \(x_1\), \(x_2\) are the roots, then \(ax^2+bx+c=a(x-x_1)(x-x_2)\).', r'Phân tích thành nhân tử: nếu \(x_1\), \(x_2\) là hai nghiệm thì \(ax^2+bx+c=a(x-x_1)(x-x_2)\).'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Sum and product', 'Tổng và tích hai nghiệm'),
  T(r'Without solving, find the sum and the product of the roots of a) \(2x^2-7x+3=0\); b) \(x^2-x+3=0\).', r'Không giải phương trình, tính tổng và tích các nghiệm (nếu có) của a) \(2x^2-7x+3=0\); b) \(x^2-x+3=0\).'),
  ('Check \\(\\Delta\\) first.', 'Kiểm tra \\(\\Delta\\) trước.'),
  [T(r'a) \(\Delta=49-24=25\ge0\): \(x_1+x_2=\dfrac72\), \(x_1x_2=\dfrac32\).', r'a) \(\Delta=49-24=25\ge0\): \(x_1+x_2=\dfrac72\), \(x_1x_2=\dfrac32\).'),
   T(r'b) \(\Delta=1-12=-11\lt0\): no real roots, so there is no sum or product of roots.', r'b) \(\Delta=1-12=-11\lt0\): phương trình vô nghiệm nên không có tổng, tích các nghiệm.')],
  T(r'a) \(\dfrac72\) and \(\dfrac32\); b) the equation has no real roots.', r'a) \(\dfrac72\) và \(\dfrac32\); b) phương trình vô nghiệm.'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Solving by inspection', 'Nhẩm nghiệm'),
  T(r'Solve by inspection: a) \(x^2-6x+5=0\); b) \(5x^2+14x+9=0\).', r'Nhẩm nghiệm các phương trình: a) \(x^2-6x+5=0\); b) \(5x^2+14x+9=0\).'),
  ('Compute \\(a+b+c\\) and \\(a-b+c\\).', 'Tính \\(a+b+c\\) và \\(a-b+c\\).'),
  [T(r'a) \(1-6+5=0\): \(x_1=1\), \(x_2=5\).', r'a) \(1-6+5=0\): \(x_1=1\), \(x_2=5\).'),
   T(r'b) \(5-14+9=0\): \(x_1=-1\), \(x_2=-\dfrac95\).', r'b) \(5-14+9=0\): \(x_1=-1\), \(x_2=-\dfrac95\).')],
  T(r'a) \(1;\ 5\); b) \(-1;\ -\dfrac95\).', r'a) \(1;\ 5\); b) \(-1;\ -\dfrac95\).'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('Two numbers', 'Tìm hai số'),
  T(r'Find two numbers whose sum is 9 and whose product is 20.', r'Tìm hai số biết tổng của chúng bằng 9 và tích bằng 20.'),
  ('Solve \\(x^2-9x+20=0\\).', 'Giải phương trình \\(x^2-9x+20=0\\).'),
  [T(r'The numbers are the roots of \(x^2-9x+20=0\); \(\Delta=81-80=1\).', r'Hai số là nghiệm của \(x^2-9x+20=0\); \(\Delta=81-80=1\).'),
   T(r'\(x_1=\dfrac{9+1}{2}=5\), \(x_2=\dfrac{9-1}{2}=4\).', r'\(x_1=\dfrac{9+1}{2}=5\), \(x_2=\dfrac{9-1}{2}=4\).')],
  T(r'4 and 5.', r'4 và 5.'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Factorising', 'Phân tích thành nhân tử'),
  T(r'Factorise a) \(x^2+11x+18\); b) \(3x^2+5x-2\).', r'Phân tích thành nhân tử: a) \(x^2+11x+18\); b) \(3x^2+5x-2\).'),
  ('Find the roots, then use \\(a(x-x_1)(x-x_2)\\).', 'Tìm nghiệm rồi dùng \\(a(x-x_1)(x-x_2)\\).'),
  [T(r'a) Roots with sum \(-11\) and product 18: \(-2\), \(-9\). So \(x^2+11x+18=(x+2)(x+9)\).', r'a) Hai nghiệm có tổng \(-11\), tích 18: \(-2\), \(-9\). Vậy \(x^2+11x+18=(x+2)(x+9)\).'),
   T(r'b) \(\Delta=25+24=49\): roots \(\dfrac13\), \(-2\). So \(3x^2+5x-2=3\left(x-\dfrac13\right)(x+2)=(3x-1)(x+2)\).', r'b) \(\Delta=25+24=49\): hai nghiệm \(\dfrac13\), \(-2\). Vậy \(3x^2+5x-2=3\left(x-\dfrac13\right)(x+2)=(3x-1)(x+2)\).')],
  T(r'\((x+2)(x+9)\); \((3x-1)(x+2)\).', r'\((x+2)(x+9)\); \((3x-1)(x+2)\).'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Fencing a garden', 'Rào vườn'),
  T(r'Mr An uses all 40 m of wire netting to fence the four sides of a rectangular garden of area 96 m². Find the dimensions of the garden.', r'Ông An dùng hết 40 m lưới để rào bốn cạnh một mảnh vườn hình chữ nhật có diện tích 96 m². Tìm kích thước mảnh vườn.'),
  ('Length + width \\(=20\\), length × width \\(=96\\).', 'Dài + rộng \\(=20\\), dài × rộng \\(=96\\).'),
  [T(r'The length and width are the roots of \(x^2-20x+96=0\); \(\Delta^{\prime}=100-96=4\).', r'Chiều dài và chiều rộng là nghiệm của \(x^2-20x+96=0\); \(\Delta^{\prime}=100-96=4\).'),
   T(r'\(x_1=10+2=12\), \(x_2=10-2=8\).', r'\(x_1=10+2=12\), \(x_2=10-2=8\).')],
  T(r'12 m by 8 m.', r'12 m × 8 m.'))

_SETS = sp_g9.BANK(sp_g9.L20_GROUPS, start=1, seeds=(3001, 3002, 3003))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Sign of the sum.</b> \(x_1+x_2=-\dfrac ba\), not \(\dfrac ba\).', r'<b>Sai dấu của tổng.</b> \(x_1+x_2=-\dfrac ba\), không phải \(\dfrac ba\).'),
 (r'<b>Forgetting \(\Delta\ge0\).</b> \(x^2-x+1=0\) has no roots, so “sum = 1, product = 1” is wrong.', r'<b>Quên điều kiện \(\Delta\ge0\).</b> \(x^2-x+1=0\) vô nghiệm nên không thể nói tổng bằng 1, tích bằng 1.'),
 (r'<b>Wrong equation for two numbers.</b> Use \(x^2-Sx+P=0\), not \(x^2+Sx+P=0\).', r'<b>Sai phương trình tìm hai số.</b> Dùng \(x^2-Sx+P=0\), không phải \(x^2+Sx+P=0\).'),
 (r'<b>Dropping \(a\).</b> \(3x^2+5x-2=3(x-x_1)(x-x_2)\), not \((x-x_1)(x-x_2)\).', r'<b>Bỏ quên hệ số \(a\).</b> \(3x^2+5x-2=3(x-x_1)(x-x_2)\), không phải \((x-x_1)(x-x_2)\).')]
summary = [
 (r'\(\Delta\ge0\): \(x_1+x_2=-\dfrac ba\), \(x_1x_2=\dfrac ca\).', r'\(\Delta\ge0\): \(x_1+x_2=-\dfrac ba\), \(x_1x_2=\dfrac ca\).'),
 (r'\(a+b+c=0\Rightarrow 1;\ \dfrac ca\); \(a-b+c=0\Rightarrow -1;\ -\dfrac ca\).', r'\(a+b+c=0\Rightarrow 1;\ \dfrac ca\); \(a-b+c=0\Rightarrow -1;\ -\dfrac ca\).'),
 (r'Sum \(S\), product \(P\): roots of \(x^2-Sx+P=0\); \(ax^2+bx+c=a(x-x_1)(x-x_2)\).', r'Tổng \(S\), tích \(P\): là nghiệm của \(x^2-Sx+P=0\); \(ax^2+bx+c=a(x-x_1)(x-x_2)\).'),
 (r"Key English: Viète's theorem, sum / product of the roots, solve by inspection, the remaining root, without solving the equation, factorise.", r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[định lí Viète]], [[tổng hai nghiệm]], [[tích hai nghiệm]], [[nhẩm nghiệm]], [[nghiệm còn lại]], [[không giải phương trình]], [[phân tích thành nhân tử]].')]
checks = [
 (r"I can state Viète's theorem.", r'Em phát biểu được định lí Viète.'),
 (r'I can find the sum and the product of the roots without solving.', r'Em tính được tổng, tích các nghiệm mà không giải phương trình.'),
 (r'I can solve equations by inspection.', r'Em nhẩm được nghiệm của phương trình.'),
 (r'I can find two numbers from their sum and product.', r'Em tìm được hai số khi biết tổng và tích.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en="Viète's Theorem and Its Applications", title_vi='Định lí Viète và ứng dụng', topic=TOPIC,
       folder='quadratic-functions-equations', file='vietes-theorem', catalog_title_vi='Định lí Viète và ứng dụng',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description="Viète's theorem: sum and product of the roots, solving by inspection, finding two numbers.", level='Intermediate', minutes=75,
       description_vi='Bài 20 – Định lí Viète; tổng và tích hai nghiệm; nhẩm nghiệm; tìm hai số biết tổng và tích.',
       tags_vi=['định lí Viète', 'tổng tích nghiệm', 'nhẩm nghiệm'], prerequisites=['g9-quadratic-02'], tags=["Viete's theorem", 'sum of roots', 'product of roots'], order=200)
