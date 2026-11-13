# -*- coding: utf-8 -*-
"""Nội dung bài g9-quadratic-02 = Toán 9 KNTT, Bài 19: Phương trình bậc hai một ẩn – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 6 – Lesson 19."""
import os, sys, math
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9

LID = 'g9-quadratic-02'
CH = 'Hàm số y = ax² (a ≠ 0). Phương trình bậc hai một ẩn'
TOPIC = ('Quadratic Function and Quadratic Equation', CH)
ensure_vocab([
 ('g9-quad-eq', 'quadratic equation in one unknown', 'phương trình bậc hai một ẩn', CH, '2x² + 3x − 1 = 0 is a quadratic equation in one unknown.', ''),
 ('g9-discriminant', 'discriminant', 'biệt thức', CH, 'The discriminant is Δ = b² − 4ac.', r'\(\Delta\)'),
 ('g9-reduced-disc', 'reduced discriminant', 'biệt thức thu gọn', CH, "If b = 2b', the reduced discriminant is Δ' = b'² − ac.", r"\(\Delta'\)"),
 ('g9-double-root', 'double root (repeated root)', 'nghiệm kép', CH, 'If Δ = 0, the equation has a double root.', ''),
 ('g9-two-roots', 'two distinct roots', 'hai nghiệm phân biệt', CH, 'If Δ > 0, the equation has two distinct roots.', ''),
 ('g9-no-real-roots', 'no real roots', 'vô nghiệm', CH, 'If Δ < 0, the equation has no real roots.', ''),
 ('g9-incomplete-eq', 'incomplete quadratic equation', 'phương trình khuyết', CH, '5x² + 11x = 0 is an incomplete quadratic equation (c = 0).', ''),
 ('g9-quad-formula', 'quadratic formula', 'công thức nghiệm', CH, 'Use the quadratic formula to solve the equation.', ''),
])
load_vocab()

# ---------- kiểm tra số liệu ----------
assert (3 - 1, 2 + 1, -1) == (2, 3, -1)            # 3x²+2x−1 = x²−x  ⇒ 2x²+3x−1 = 0
assert 7 * 7 - 4 * 3 * (-1) == 61 and 21 * 21 - 9 * 49 == 0 and F(-21, 9) == F(-7, 3)
assert 5 - 2 == 3
D = 2.5 ** 2 - 4 * 0.1 * (-0.2); x1, x2 = (-2.5 - math.sqrt(D)) / 0.2, (-2.5 + math.sqrt(D)) / 0.2
assert ('%.2f' % x1, '%.2f' % x2) == ('-25.08', '0.08')
assert [x for x in (2, 20) if (28 - 2 * x) * (16 - 2 * x) == 288] == [2, 20] and 16 - 2 * 20 < 0

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 90 minutes', '90 phút'), before=('Lesson 4; grade 8: algebraic identities', 'Bài 4; lớp 8: hằng đẳng thức'))
goals = [
 (r'recognize a quadratic equation and its coefficients \(a\), \(b\), \(c\);', r'nhận biết được phương trình bậc hai một ẩn và các hệ số \(a\), \(b\), \(c\);'),
 (r'solve incomplete equations without the formula;', r'giải được phương trình khuyết mà không cần công thức nghiệm;'),
 (r'use the discriminant \(\Delta\) (or \(\Delta^{\prime})\) to solve and to count the roots;', r'dùng biệt thức \(\Delta\) (hoặc \(\Delta^{\prime})\) để giải và xác định số nghiệm;'),
 (r'use a calculator and solve real-life problems leading to quadratic equations.', r'dùng máy tính cầm tay và giải bài toán thực tế dẫn tới phương trình bậc hai.')]
vocab = [
 (r'<b>quadratic equation in one unknown</b> – \(ax^2+bx+c=0\) with \(a\ne0\).', r'[[Phương trình bậc hai một ẩn]] – \(ax^2+bx+c=0\) với \(a\ne0\).'),
 (r'<b>incomplete equation</b> – \(b=0\) or \(c=0\).', r'[[Phương trình khuyết]] – \(b=0\) hoặc \(c=0\).'),
 (r'<b>discriminant / reduced discriminant</b> – \(\Delta=b^2-4ac\); \(\Delta^{\prime}=b^{\prime}^2-ac\) when \(b=2b^{\prime}\).', r'[[Biệt thức]] / [[biệt thức thu gọn]] – \(\Delta=b^2-4ac\); \(\Delta^{\prime}=b^{\prime}^2-ac\) khi \(b=2b^{\prime}\).'),
 (r'<b>two distinct roots / double root / no real roots</b> – \(\Delta\gt0\) / \(\Delta=0\) / \(\Delta\lt0\).', r'[[Hai nghiệm phân biệt]] / [[nghiệm kép]] / [[vô nghiệm]] – \(\Delta\gt0\) / \(\Delta=0\) / \(\Delta\lt0\).'),
 (r'<b>quadratic formula</b> – \(x_{1,2}=\dfrac{-b\pm\sqrt\Delta}{2a}\).', r'[[Công thức nghiệm]] – \(x_{1,2}=\dfrac{-b\pm\sqrt\Delta}{2a}\).')]
phrases = [
 (r'<b>State the coefficients \(a\), \(b\) and \(c\).</b>', r'Xác định các hệ số \(a\), \(b\), \(c\).'),
 (r'<b>Calculate the discriminant.</b>', r'Tính biệt thức.'),
 (r'<b>Since \(\Delta\gt0\), the equation has two distinct roots.</b>', r'Vì \(\Delta\gt0\) nên phương trình có hai nghiệm phân biệt.'),
 (r'<b>The equation has a double root \(x_1=x_2=-\dfrac{b}{2a}\).</b>', r'Phương trình có nghiệm kép \(x_1=x_2=-\dfrac{b}{2a}\).'),
 (r'<b>Reject the root that does not satisfy the condition.</b>', r'Loại nghiệm không thỏa mãn điều kiện.')]
review = (T(r'<b>Lesson 4.</b> \(A\cdot B=0\iff A=0\) or \(B=0\).', r'<b>Bài 4.</b> \(A\cdot B=0\iff A=0\) hoặc \(B=0\).') +
          T(r'<b>Identities.</b> \((A\pm B)^2=A^2\pm2AB+B^2\).', r'<b>Hằng đẳng thức.</b> \((A\pm B)^2=A^2\pm2AB+B^2\).'))

theory = '<h3>5.1 %s</h3>' % TI('Definition', 'Định nghĩa phương trình bậc hai một ẩn')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'A <b>quadratic equation in one unknown</b> \(x\) has the form \(ax^2+bx+c=0\), where \(a\), \(b\), \(c\) are given numbers and \(a\ne0\).', r'[[Phương trình bậc hai một ẩn]] (ẩn \(x\)) là phương trình có dạng \(ax^2+bx+c=0\), trong đó \(a\), \(b\), \(c\) là các số cho trước, \(a\ne0\).'),
  T(r'Incomplete equations: \(ax^2+bx=0\Leftrightarrow x(ax+b)=0\); \(ax^2+c=0\Leftrightarrow x^2=-\dfrac ca\).', r'Phương trình khuyết: \(ax^2+bx=0\Leftrightarrow x(ax+b)=0\); \(ax^2+c=0\Leftrightarrow x^2=-\dfrac ca\).'))
theory += '<h3>5.2 %s</h3>' % TI('The quadratic formula', 'Công thức nghiệm')
theory += TABLE([('\\(\\Delta=b^2-4ac\\)', '\\(\\Delta=b^2-4ac\\)'), ('Roots', 'Nghiệm')],
  [[TI('\\(\\Delta\\gt0\\)', '\\(\\Delta\\gt0\\)'), TI('two distinct roots \\(x_{1,2}=\\dfrac{-b\\pm\\sqrt\\Delta}{2a}\\)', 'hai nghiệm phân biệt \\(x_{1,2}=\\dfrac{-b\\pm\\sqrt\\Delta}{2a}\\)')],
   [TI('\\(\\Delta=0\\)', '\\(\\Delta=0\\)'), TI('a double root \\(x_1=x_2=-\\dfrac{b}{2a}\\)', 'nghiệm kép \\(x_1=x_2=-\\dfrac{b}{2a}\\)')],
   [TI('\\(\\Delta\\lt0\\)', '\\(\\Delta\\lt0\\)'), TI('no real roots', 'vô nghiệm')]])
theory += BOX('mint', ('Reduced formula', 'Công thức nghiệm thu gọn'),
  T(r'If \(b=2b^{\prime}\), let \(\Delta^{\prime}=b^{\prime}^2-ac\). If \(\Delta^{\prime}\gt0\): \(x_{1,2}=\dfrac{-b^{\prime}\pm\sqrt{\Delta^{\prime}}}{a}\); if \(\Delta^{\prime}=0\): \(x_1=x_2=-\dfrac{b^{\prime}}{a}\); if \(\Delta^{\prime}\lt0\): no real roots.', r'Nếu \(b=2b^{\prime}\), đặt \(\Delta^{\prime}=b^{\prime}^2-ac\). Nếu \(\Delta^{\prime}\gt0\): \(x_{1,2}=\dfrac{-b^{\prime}\pm\sqrt{\Delta^{\prime}}}{a}\); nếu \(\Delta^{\prime}=0\): \(x_1=x_2=-\dfrac{b^{\prime}}{a}\); nếu \(\Delta^{\prime}\lt0\): vô nghiệm.'),
  T(r'Note: if \(a\) and \(c\) have opposite signs, then \(ac\lt0\), \(\Delta\gt0\) and the equation has two distinct roots.', r'Chú ý: nếu \(a\), \(c\) trái dấu thì \(ac\lt0\), \(\Delta\gt0\) và phương trình có hai nghiệm phân biệt.'))
theory += BOX('yellow', ('Calculator', 'Dùng máy tính cầm tay'),
  T(r'Choose the equation mode \(ax^2+bx+c=0\), enter \(a\), \(b\), \(c\) and read \(x_1\), \(x_2\).', r'Chọn chế độ giải phương trình \(ax^2+bx+c=0\), nhập \(a\), \(b\), \(c\) rồi đọc \(x_1\), \(x_2\).'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Recognizing the equation', 'Nhận biết phương trình bậc hai'),
  T(r'Write each equation in the form \(ax^2+bx+c=0\) and state \(a\), \(b\), \(c\): a) \(3x^2+2x-1=x^2-x\); b) \((2x+1)^2=x+1\).', r'Đưa mỗi phương trình về dạng \(ax^2+bx+c=0\) và chỉ ra \(a\), \(b\), \(c\): a) \(3x^2+2x-1=x^2-x\); b) \((2x+1)^2=x+1\).'),
  ('Move every term to the left-hand side.', 'Chuyển mọi hạng tử sang vế trái.'),
  [T(r'a) \(2x^2+3x-1=0\): \(a=2\), \(b=3\), \(c=-1\).', r'a) \(2x^2+3x-1=0\): \(a=2\), \(b=3\), \(c=-1\).'),
   T(r'b) \(4x^2+4x+1=x+1\Leftrightarrow 4x^2+3x=0\): \(a=4\), \(b=3\), \(c=0\).', r'b) \(4x^2+4x+1=x+1\Leftrightarrow 4x^2+3x=0\): \(a=4\), \(b=3\), \(c=0\).')],
  T(r'a) \(2;\ 3;\ -1\); b) \(4;\ 3;\ 0\).', r'a) \(2;\ 3;\ -1\); b) \(4;\ 3;\ 0\).'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Incomplete equations', 'Phương trình khuyết'),
  T(r'Solve a) \(5x^2+11x=0\); b) \(x^2-25=0\); c) \((3x+2)^2=5\).', r'Giải các phương trình a) \(5x^2+11x=0\); b) \(x^2-25=0\); c) \((3x+2)^2=5\).'),
  ('Factorise or take square roots.', 'Đặt nhân tử chung hoặc khai căn.'),
  [T(r'a) \(x(5x+11)=0\Rightarrow x=0\) or \(x=-\dfrac{11}{5}\). b) \(x^2=25\Rightarrow x=\pm5\).', r'a) \(x(5x+11)=0\Rightarrow x=0\) hoặc \(x=-\dfrac{11}{5}\). b) \(x^2=25\Rightarrow x=\pm5\).'),
   T(r'c) \(3x+2=\pm\sqrt5\Rightarrow x=\dfrac{-2\pm\sqrt5}{3}\).', r'c) \(3x+2=\pm\sqrt5\Rightarrow x=\dfrac{-2\pm\sqrt5}{3}\).')],
  T(r'a) \(S=\left\{-\dfrac{11}{5};\ 0\right\}\); b) \(S=\{-5;\ 5\}\); c) \(S=\left\{\dfrac{-2-\sqrt5}{3};\ \dfrac{-2+\sqrt5}{3}\right\}\).', r'a) \(S=\left\{-\dfrac{11}{5};\ 0\right\}\); b) \(S=\{-5;\ 5\}\); c) \(S=\left\{\dfrac{-2-\sqrt5}{3};\ \dfrac{-2+\sqrt5}{3}\right\}\).'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('The quadratic formula', 'Dùng công thức nghiệm'),
  T(r'a) Solve \(3x^2+7x-1=0\). b) Without solving, give the number of roots of \(9x^2+42x+49=0\) and \(x^2-x+1=0\).', r'a) Giải phương trình \(3x^2+7x-1=0\). b) Không giải, cho biết số nghiệm của \(9x^2+42x+49=0\) và \(x^2-x+1=0\).'),
  ('\\(a=3\\), \\(b=7\\), \\(c=-1\\).', '\\(a=3\\), \\(b=7\\), \\(c=-1\\).'),
  [T(r'a) \(\Delta=49+12=61\gt0\): \(x_{1,2}=\dfrac{-7\pm\sqrt{61}}{6}\).', r'a) \(\Delta=49+12=61\gt0\): \(x_{1,2}=\dfrac{-7\pm\sqrt{61}}{6}\).'),
   T(r'b) \(\Delta^{\prime}=21^2-9\cdot49=0\): a double root \(x=-\dfrac73\). \(\Delta=1-4=-3\lt0\): no real roots.', r'b) \(\Delta^{\prime}=21^2-9\cdot49=0\): nghiệm kép \(x=-\dfrac73\). \(\Delta=1-4=-3\lt0\): vô nghiệm.')],
  T(r'a) \(\dfrac{-7\pm\sqrt{61}}{6}\); b) a double root; no real roots.', r'a) \(\dfrac{-7\pm\sqrt{61}}{6}\); b) nghiệm kép; vô nghiệm.'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Reduced formula and calculator', 'Công thức thu gọn và máy tính'),
  T(r'a) Solve \(x^2-2\sqrt5x+2=0\). b) Use a calculator to solve \(0.1x^2+2.5x-0.2=0\) (two decimal places).', r'a) Giải phương trình \(x^2-2\sqrt5x+2=0\). b) Dùng máy tính cầm tay giải \(0{,}1x^2+2{,}5x-0{,}2=0\) (làm tròn đến chữ số thập phân thứ hai).'),
  ("\\(b'=-\\sqrt5\\).", "\\(b'=-\\sqrt5\\)."),
  [T(r'a) \(\Delta^{\prime}=5-2=3\gt0\): \(x_{1,2}=\sqrt5\pm\sqrt3\).', r'a) \(\Delta^{\prime}=5-2=3\gt0\): \(x_{1,2}=\sqrt5\pm\sqrt3\).'),
   T(r'b) The calculator gives \(x_1\approx-25.08\), \(x_2\approx0.08\).', r'b) Máy tính cho \(x_1\approx-25{,}08\), \(x_2\approx0{,}08\).')],
  T(r'a) \(\sqrt5\pm\sqrt3\); b) \(-25.08\); \(0.08\).', r'a) \(\sqrt5\pm\sqrt3\); b) \(-25{,}08\); \(0{,}08\).'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('A pool with a path', 'Bể bơi và lối đi'),
  T(r'A rectangular plot 28 m by 16 m contains a swimming pool with a path of constant width \(x\) m around it. Find \(x\) so that the pool has area 288 m².', r'Một khu đất hình chữ nhật 28 m × 16 m có bể bơi ở giữa, xung quanh là lối đi rộng đều \(x\) m. Tìm \(x\) để diện tích bể bơi là 288 m².'),
  ('The pool is \\((28-2x)\\) m by \\((16-2x)\\) m, with \\(0\\lt x\\lt8\\).', 'Bể bơi có kích thước \\((28-2x)\\) m × \\((16-2x)\\) m, với \\(0\\lt x\\lt8\\).'),
  [T(r'\((28-2x)(16-2x)=288\Leftrightarrow 4x^2-88x+160=0\Leftrightarrow x^2-22x+40=0\).', r'\((28-2x)(16-2x)=288\Leftrightarrow 4x^2-88x+160=0\Leftrightarrow x^2-22x+40=0\).'),
   T(r'\(\Delta^{\prime}=121-40=81\): \(x=11\pm9\), i.e. \(x=2\) or \(x=20\). Only \(x=2\) satisfies \(0\lt x\lt8\).', r'\(\Delta^{\prime}=121-40=81\): \(x=11\pm9\), tức \(x=2\) hoặc \(x=20\). Chỉ \(x=2\) thỏa mãn \(0\lt x\lt8\).')],
  T(r'\(x=2\) m.', r'\(x=2\) m.'))

_SETS = sp_g9.BANK(sp_g9.L19_GROUPS, start=1, seeds=(2901, 2902, 2903))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Wrong signs of \(b\), \(c\).</b> In \(x^2-5x-6=0\), \(b=-5\) and \(c=-6\).', r'<b>Sai dấu \(b\), \(c\).</b> Trong \(x^2-5x-6=0\) thì \(b=-5\), \(c=-6\).'),
 (r'<b>Losing a root.</b> \(5x^2+11x=0\) has the root \(x=0\) too; never divide both sides by \(x\).', r'<b>Mất nghiệm.</b> \(5x^2+11x=0\) còn có nghiệm \(x=0\); không chia hai vế cho \(x\).'),
 (r'<b>\(2a\) vs \(a\).</b> Full formula: denominator \(2a\); reduced formula: denominator \(a\).', r'<b>Nhầm \(2a\) với \(a\).</b> Công thức nghiệm: mẫu \(2a\); công thức thu gọn: mẫu \(a\).'),
 (r'<b>Not checking conditions.</b> In word problems reject roots that make a length negative.', r'<b>Không đối chiếu điều kiện.</b> Trong bài toán thực tế phải loại nghiệm làm độ dài âm.')]
summary = [
 (r'\(ax^2+bx+c=0\ (a\ne0)\); \(\Delta=b^2-4ac\).', r'\(ax^2+bx+c=0\ (a\ne0)\); \(\Delta=b^2-4ac\).'),
 (r'\(\Delta\gt0\): \(x_{1,2}=\dfrac{-b\pm\sqrt\Delta}{2a}\); \(\Delta=0\): \(x=-\dfrac b{2a}\); \(\Delta\lt0\): no real roots.', r'\(\Delta\gt0\): \(x_{1,2}=\dfrac{-b\pm\sqrt\Delta}{2a}\); \(\Delta=0\): \(x=-\dfrac b{2a}\); \(\Delta\lt0\): vô nghiệm.'),
 (r'\(b=2b^{\prime}\): \(\Delta^{\prime}=b^{\prime}^2-ac\), \(x_{1,2}=\dfrac{-b^{\prime}\pm\sqrt{\Delta^{\prime}}}{a}\); \(ac\lt0\Rightarrow\) two distinct roots.', r'\(b=2b^{\prime}\): \(\Delta^{\prime}=b^{\prime}^2-ac\), \(x_{1,2}=\dfrac{-b^{\prime}\pm\sqrt{\Delta^{\prime}}}{a}\); \(ac\lt0\Rightarrow\) có hai nghiệm phân biệt.'),
 (r'Key English: quadratic equation in one unknown, incomplete equation, discriminant, reduced discriminant, two distinct roots, double root, no real roots, quadratic formula.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[phương trình bậc hai một ẩn]], [[phương trình khuyết]], [[biệt thức]], [[biệt thức thu gọn]], [[hai nghiệm phân biệt]], [[nghiệm kép]], [[vô nghiệm]], [[công thức nghiệm]].')]
checks = [
 (r'I can recognize a quadratic equation and its coefficients.', r'Em nhận biết được phương trình bậc hai và các hệ số.'),
 (r'I can solve incomplete equations.', r'Em giải được phương trình khuyết.'),
 (r'I can use \(\Delta\) and \(\Delta^{\prime}\) to solve equations.', r'Em dùng được \(\Delta\), \(\Delta^{\prime}\) để giải phương trình.'),
 (r'I can solve real-life problems leading to quadratic equations.', r'Em giải được bài toán thực tế dẫn tới phương trình bậc hai.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Quadratic Equations in One Unknown', title_vi='Phương trình bậc hai một ẩn', topic=TOPIC,
       folder='quadratic-functions-equations', file='quadratic-equations', catalog_title_vi='Phương trình bậc hai một ẩn',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Quadratic equations, incomplete equations, the discriminant and the quadratic formula.', level='Intermediate', minutes=90,
       description_vi="Bài 19 – Phương trình bậc hai một ẩn; phương trình khuyết; biệt thức Δ, Δ'; công thức nghiệm; máy tính cầm tay.",
       tags_vi=['phương trình bậc hai', 'biệt thức', 'công thức nghiệm'], prerequisites=['g9-lineq-01'], tags=['quadratic equation', 'discriminant', 'quadratic formula'], order=190)
