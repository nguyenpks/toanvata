# -*- coding: utf-8 -*-
"""Nội dung bài g9-lineq-03 = Toán 9 KNTT, Bài 6: Bất phương trình bậc nhất một ẩn – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 2 – Lesson 6, tr. 20–21.
Sửa lỗi tài liệu: TLTA khai triển (x+1)(2x−1) = 2x² + x − 2 và ra x ≤ 9/4; đúng là 2x² + x − 1 và x ≤ 2 (Ví dụ 4).
Theo quyết định của GV (Q8): có biểu diễn tập nghiệm trên trục số (hình tĩnh, nhãn số không đè lên phần tô)."""
import os, sys
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
from mb_extra import FIGR
import mb_pgf
import sp_g9

LID = 'g9-lineq-03'
CH = 'Phương trình và bất phương trình bậc nhất một ẩn'
TOPIC = ('Linear Equations and Linear Inequalities in One Variable', CH)
ensure_vocab([
 ('g9-ineq-eq', 'inequality (with a variable)', 'bất phương trình', CH, '3x − 1 < 5 is an inequality in the variable x.', ''),
 ('g9-lin-ineq1', 'linear inequality in one variable', 'bất phương trình bậc nhất một ẩn', CH, '3x − 1 < 0 is a linear inequality in one variable.', r'\(ax+b\lt 0\)'),
 ('g9-sol-ineq', 'solution of an inequality', 'nghiệm của bất phương trình', CH, 'x = 0 is a solution of the inequality 3x − 6 < 0.', ''),
 ('g9-solve-ineq', 'solve an inequality', 'giải bất phương trình', CH, 'Solve the following inequalities.', ''),
 ('g9-transpose', 'move a term to the other side', 'chuyển vế', CH, 'Move −2 to the right-hand side and change its sign.', ''),
])
load_vocab()

# ---------- kiểm tra số liệu ----------
X = [F(n, 4) for n in range(-200, 201)]
assert [x for x in X if -2 * x + 10 >= 0] == [x for x in X if x <= 5]                                  # Ví dụ 2
assert [x for x in X if 5 * x - 2 > -3 * x + 14] == [x for x in X if x > 2]                             # Ví dụ 3
assert [x for x in X if (x + 1) * (2 * x - 1) <= 2 * x * x - 3 * x + 7] == [x for x in X if x <= 2]     # Ví dụ 4
assert max(x for x in range(0, 100) if 3 * x + 28 <= 100) == 24                                        # Ví dụ 5

def NL(a, op, en, vi, alt):
    return FIGR(mb_pgf.svg_img(sp_g9.ray_svg(a, op), alt, 460), en, vi)

meta = dict(level=('Beginner', 'Cơ bản'), time=('about 60 minutes', '60 phút'),
            before=('Lesson 5: properties of inequalities; linear equations in one variable', 'Bài 5: tính chất của bất đẳng thức; phương trình bậc nhất một ẩn'))
goals = [
 (r'recognize a linear inequality in one variable and check whether a number is a solution;', r'nhận biết [[bất phương trình bậc nhất một ẩn]] và kiểm tra một số có là [[nghiệm của bất phương trình]] hay không;'),
 (r'solve linear inequalities by moving terms and multiplying (or dividing) both sides;', r'[[giải bất phương trình]] bậc nhất một ẩn bằng quy tắc [[chuyển vế]] và quy tắc nhân (chia) hai vế;'),
 (r'show the solutions on a number line;', r'biểu diễn tập nghiệm trên [[trục số]];'),
 (r'solve simple real-world problems with inequalities.', r'giải được một số bài toán thực tế dẫn đến bất phương trình.')]
vocab = [
 (r'<b>linear inequality in one variable</b> – \(ax+b\lt 0\) (or \(\gt,\le,\ge\)) with \(a\ne0\).', r'[[Bất phương trình bậc nhất một ẩn]] – bất phương trình dạng \(ax+b\lt 0\) (hoặc \(\gt,\le,\ge\)) với \(a\ne0\).'),
 (r'<b>solution</b> – a value of \(x\) that makes the inequality true.', r'[[Nghiệm của bất phương trình]] – giá trị của \(x\) làm bất phương trình trở thành bất đẳng thức đúng.'),
 (r'<b>solve an inequality</b> – find all its solutions.', r'[[Giải bất phương trình]] – tìm tất cả các nghiệm của nó.'),
 (r'<b>move a term</b> – move it to the other side and change its sign.', r'[[Chuyển vế]] – chuyển một hạng tử sang vế kia và đổi dấu hạng tử đó.'),
 (r'<b>number line</b> – a line on which the solutions are shaded.', r'[[Trục số]] – đường thẳng dùng để biểu diễn tập nghiệm.')]
phrases = [
 (r'<b>Identify the linear inequality in one variable.</b>', r'Chỉ ra bất phương trình bậc nhất một ẩn.'),
 (r'<b>The statement is true, so \(x=0\) is a solution.</b>', r'Khẳng định đúng nên \(x=0\) là một nghiệm.'),
 (r'<b>Solve the following inequalities.</b>', r'Giải các bất phương trình sau.'),
 (r'<b>Divide both sides by \(-2\) and reverse the inequality sign.</b>', r'Chia hai vế cho \(-2\) và đổi chiều bất phương trình.'),
 (r'<b>The solutions are all real numbers \(x\) satisfying \(x\gt2\).</b>', r'Nghiệm của bất phương trình là mọi số thực \(x\) thỏa mãn \(x\gt2\).')]
review = (T(r'<b>Lesson 5.</b> Adding the same number keeps the direction; multiplying by a negative number reverses it.', r'<b>Bài 5.</b> Cộng cùng một số vào hai vế: giữ chiều; nhân hai vế với số âm: đổi chiều.') +
          T(r'<b>Equations.</b> Solving \(ax+b=0\) uses the same moves: \(3x-6=0\Leftrightarrow 3x=6\Leftrightarrow x=2\).', r'<b>Phương trình.</b> Giải \(ax+b=0\) cũng dùng các bước tương tự: \(3x-6=0\Leftrightarrow 3x=6\Leftrightarrow x=2\).'))

theory = '<h3>5.1 %s</h3>' % TI('Linear inequalities in one variable', 'Bất phương trình bậc nhất một ẩn')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'A <b>linear inequality in one variable</b> \(x\) has the form \(ax+b\lt0\), \(ax+b\gt0\), \(ax+b\le0\) or \(ax+b\ge0\), where \(a, b\) are given numbers and \(a\ne0\).', r'[[Bất phương trình bậc nhất một ẩn]] \(x\) là bất phương trình dạng \(ax+b\lt0\) (hoặc \(ax+b\gt0\), \(ax+b\le0\), \(ax+b\ge0\)), trong đó \(a, b\) là hai số đã cho, \(a\ne0\).'),
  T(r'A number \(x_0\) is a <b>solution</b> if replacing \(x\) by \(x_0\) gives a true inequality. Example: \(x=0\) is a solution of \(3x-6\lt0\) because \(-6\lt0\).', r'Số \(x_0\) là [[nghiệm của bất phương trình]] nếu thay \(x=x_0\) ta được một bất đẳng thức đúng. Ví dụ: \(x=0\) là nghiệm của \(3x-6\lt0\) vì \(-6\lt0\).'))
theory += '<h3>5.2 %s</h3>' % TI('How to solve', 'Cách giải')
theory += BOX('mint', ('Two rules', 'Hai quy tắc'),
  UL([T(r'<b>Moving a term:</b> move a term to the other side and change its sign. The direction does not change.', r'<b>Quy tắc chuyển vế:</b> chuyển một hạng tử sang vế kia và đổi dấu hạng tử đó; bất phương trình giữ nguyên chiều.'),
      T(r'<b>Multiplying (dividing):</b> multiply or divide both sides by the same number \(c\ne0\): keep the direction if \(c\gt0\), <b>reverse</b> it if \(c\lt0\).', r'<b>Quy tắc nhân (chia):</b> nhân hoặc chia hai vế cho cùng một số \(c\ne0\): giữ nguyên chiều nếu \(c\gt0\), <b>đổi chiều</b> nếu \(c\lt0\).')]),
  T(r'So \(ax+b\gt0\Leftrightarrow ax\gt-b\Leftrightarrow x\gt-\dfrac{b}{a}\) if \(a\gt0\), and \(x\lt-\dfrac{b}{a}\) if \(a\lt0\).', r'Như vậy \(ax+b\gt0\Leftrightarrow ax\gt-b\Leftrightarrow x\gt-\dfrac{b}{a}\) nếu \(a\gt0\); \(x\lt-\dfrac{b}{a}\) nếu \(a\lt0\).'))
theory += '<h3>5.3 %s</h3>' % TI('Showing solutions on a number line', 'Biểu diễn tập nghiệm trên trục số')
theory += T(r'Shade the part of the number line that contains the solutions. A <b>filled</b> dot means the endpoint is a solution (\(\le,\ \ge\)); an <b>open</b> dot means it is not (\(\lt,\ \gt\)).', r'Tô phần trục số chứa các nghiệm. Chấm <b>đặc</b> nghĩa là đầu mút là nghiệm (dấu \(\le,\ \ge\)); chấm <b>rỗng</b> nghĩa là đầu mút không là nghiệm (dấu \(\lt,\ \gt\)).')
theory += NL(2, '>', r'The solutions \(x\gt2\): open dot at 2, shading to the right.', r'Tập nghiệm \(x\gt2\): chấm rỗng tại 2, tô phần bên phải.', 'Number line: x greater than 2')
theory += NL(-1, '<=', r'The solutions \(x\le-1\): filled dot at \(-1\), shading to the left.', r'Tập nghiệm \(x\le-1\): chấm đặc tại \(-1\), tô phần bên trái.', 'Number line: x less than or equal to minus 1')

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Recognize and check', 'Nhận biết và kiểm tra nghiệm'),
  T(r'a) Which are linear inequalities in one variable: \(3x+10\ge0\); \(0x-4\lt0\); \(x^2-1\le0\); \(\dfrac{x}{3}+2\gt0\)? b) Is \(x=0\) a solution of \(3x-6\lt0\)?', r'a) Bất phương trình nào là bất phương trình bậc nhất một ẩn: \(3x+10\ge0\); \(0x-4\lt0\); \(x^2-1\le0\); \(\dfrac{x}{3}+2\gt0\)? b) \(x=0\) có là nghiệm của \(3x-6\lt0\) không?'),
  ('Check the form \\(ax+b\\) with \\(a\\ne0\\); then substitute.', 'Kiểm tra dạng \\(ax+b\\) với \\(a\\ne0\\); sau đó thay số.'),
  [T(r'a) \(3x+10\ge0\) (\(a=3\)) and \(\dfrac{x}{3}+2\gt0\) (\(a=\dfrac13\)) are. \(0x-4\lt0\) has \(a=0\); \(x^2-1\le0\) contains \(x^2\).', r'a) \(3x+10\ge0\) (\(a=3\)) và \(\dfrac{x}{3}+2\gt0\) (\(a=\dfrac13\)) là bất phương trình bậc nhất một ẩn. \(0x-4\lt0\) có \(a=0\); \(x^2-1\le0\) chứa \(x^2\).'),
   T(r'b) \(3\cdot0-6=-6\lt0\) is true, so \(x=0\) is a solution.', r'b) \(3\cdot0-6=-6\lt0\) đúng nên \(x=0\) là một nghiệm.')],
  T(r'a) \(3x+10\ge0\) and \(\dfrac{x}{3}+2\gt0\). b) Yes.', r'a) \(3x+10\ge0\) và \(\dfrac{x}{3}+2\gt0\). b) Có.'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('A negative coefficient', 'Hệ số âm'),
  T(r'Solve \(-2x+10\ge0\) and show the solutions on a number line.', r'Giải bất phương trình \(-2x+10\ge0\) và biểu diễn tập nghiệm trên trục số.'),
  ('After moving 10, divide by \\(-2\\): reverse the sign.', 'Sau khi chuyển vế, chia cho \\(-2\\) thì phải đổi chiều.'),
  [T(r'\(-2x\ge-10\).', r'\(-2x\ge-10\).'),
   T(r'Divide by \(-2\lt0\): \(x\le5\).', r'Chia hai vế cho \(-2\lt0\): \(x\le5\).'),
   NL(5, '<=', r'\(x\le5\): filled dot at 5.', r'\(x\le5\): chấm đặc tại 5.', 'Number line: x less than or equal to 5')],
  T(r'\(x\le5\).', r'Nghiệm của bất phương trình là \(x\le5\).'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('Variables on both sides', 'Ẩn ở hai vế'),
  T(r'Solve \(5x-2\gt -3x+14\).', r'Giải bất phương trình \(5x-2\gt -3x+14\).'),
  ('Move the \\(x\\)-terms to the left and the numbers to the right.', 'Chuyển các hạng tử chứa \\(x\\) sang vế trái, các số sang vế phải.'),
  [T(r'\(5x+3x\gt 14+2\Leftrightarrow 8x\gt16\Leftrightarrow x\gt2\).', r'\(5x+3x\gt 14+2\Leftrightarrow 8x\gt16\Leftrightarrow x\gt2\).'),
   NL(2, '>', r'\(x\gt2\): open dot at 2.', r'\(x\gt2\): chấm rỗng tại 2.', 'Number line: x greater than 2')],
  T(r'\(x\gt2\).', r'Nghiệm của bất phương trình là \(x\gt2\).'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Expand first', 'Khai triển rồi giải'),
  T(r'Solve \((x+1)(2x-1)\le 2x^2-3x+7\).', r'Giải bất phương trình \((x+1)(2x-1)\le 2x^2-3x+7\).'),
  ('Expand the left-hand side; the \\(2x^2\\) terms cancel.', 'Khai triển vế trái; các hạng tử \\(2x^2\\) triệt tiêu.'),
  [T(r'\((x+1)(2x-1)=2x^2+x-1\).', r'\((x+1)(2x-1)=2x^2+x-1\).'),
   T(r'\(2x^2+x-1\le 2x^2-3x+7\Leftrightarrow 4x\le 8\Leftrightarrow x\le2\).', r'\(2x^2+x-1\le 2x^2-3x+7\Leftrightarrow 4x\le 8\Leftrightarrow x\le2\).')],
  T(r'\(x\le2\).', r'Nghiệm của bất phương trình là \(x\le2\).'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Shopping with a budget', 'Mua sắm với số tiền có hạn'),
  T(r'Lan has 100 thousand dong. She buys a diary for 28 thousand dong and 3 pens of the same price \(x\) (thousand dong). Write an inequality and find the highest possible price of a pen.', r'Lan có 100 nghìn đồng. Lan mua một quyển sổ giá 28 nghìn đồng và 3 cây bút cùng giá \(x\) (nghìn đồng). Viết bất phương trình và tìm giá cao nhất có thể của một cây bút.'),
  ('Total cost cannot exceed the money she has.', 'Tổng số tiền mua không vượt quá số tiền Lan có.'),
  [T(r'Total cost: \(3x+28\). Inequality: \(3x+28\le100\).', r'Tổng số tiền: \(3x+28\). Bất phương trình: \(3x+28\le100\).'),
   T(r'\(3x\le72\Leftrightarrow x\le24\).', r'\(3x\le72\Leftrightarrow x\le24\).')],
  T(r'A pen costs at most 24 thousand dong.', r'Mỗi cây bút có giá nhiều nhất là 24 nghìn đồng.'))

_SETS = sp_g9.BANK(sp_g9.L6_GROUPS, start=1, seeds=(1601, 1602, 1603))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Not reversing when dividing by a negative number.</b> \(-2x\ge-10\Rightarrow x\le5\), not \(x\ge5\).', r'<b>Chia cho số âm mà không đổi chiều.</b> \(-2x\ge-10\Rightarrow x\le5\), không phải \(x\ge5\).'),
 (r'<b>Reversing when moving a term.</b> Moving a term changes its sign, not the direction of the inequality.', r'<b>Đổi chiều khi chuyển vế.</b> Chuyển vế chỉ đổi dấu hạng tử, không đổi chiều bất phương trình.'),
 (r'<b>Wrong dot on the number line.</b> \(\le,\ \ge\): filled dot; \(\lt,\ \gt\): open dot.', r'<b>Vẽ sai đầu mút trên trục số.</b> Dấu \(\le,\ \ge\): chấm đặc; dấu \(\lt,\ \gt\): chấm rỗng.'),
 (r'<b>Expanding carelessly.</b> \((x+1)(2x-1)=2x^2+x-1\); check each product.', r'<b>Khai triển sai.</b> \((x+1)(2x-1)=2x^2+x-1\); hãy kiểm tra từng tích.'),
 (r'<b>Forgetting whole numbers in word problems.</b> If \(x\) counts objects, take the largest whole number that works.', r'<b>Quên điều kiện số nguyên.</b> Nếu \(x\) là số đồ vật thì chọn số tự nhiên lớn nhất thỏa mãn.')]
summary = [
 (r'Linear inequality in one variable: \(ax+b\lt0\) (or \(\gt,\le,\ge\)), \(a\ne0\).', r'Bất phương trình bậc nhất một ẩn: \(ax+b\lt0\) (hoặc \(\gt,\le,\ge\)), \(a\ne0\).'),
 (r'Move terms (change the sign of the term); multiply or divide by a negative number → reverse the inequality.', r'Chuyển vế (đổi dấu hạng tử); nhân hoặc chia cho số âm → đổi chiều bất phương trình.'),
 (r'Number line: filled dot for \(\le,\ge\), open dot for \(\lt,\gt\).', r'Trục số: chấm đặc với \(\le,\ge\), chấm rỗng với \(\lt,\gt\).'),
 (r'Key English: linear inequality in one variable, solve an inequality, reverse the sign.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[bất phương trình bậc nhất một ẩn]], [[giải bất phương trình]], [[chuyển vế]], [[trục số]].')]
checks = [
 (r'I can recognize a linear inequality in one variable.', r'Em nhận biết được bất phương trình bậc nhất một ẩn.'),
 (r'I can solve linear inequalities, including those with negative coefficients.', r'Em giải được bất phương trình bậc nhất một ẩn, kể cả khi hệ số âm.'),
 (r'I can show the solutions on a number line.', r'Em biểu diễn được tập nghiệm trên trục số.'),
 (r'I can solve simple word problems with inequalities.', r'Em giải được bài toán thực tế đơn giản bằng bất phương trình.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Linear Inequalities in One Variable', title_vi='Bất phương trình bậc nhất một ẩn', topic=TOPIC,
       folder='equations-and-inequalities', file='linear-inequalities-one-variable', catalog_title_vi='Bất phương trình bậc nhất một ẩn',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Linear inequalities in one variable: solving them and showing the solutions on a number line.', level='Beginner', minutes=60,
       description_vi='Bài 6 – Bất phương trình bậc nhất một ẩn: cách giải, biểu diễn tập nghiệm trên trục số và bài toán thực tế.',
       tags_vi=['bất phương trình', 'bậc nhất một ẩn', 'trục số', 'đổi chiều'],
       prerequisites=['g9-lineq-02'], tags=['linear inequality', 'number line'], order=60)
