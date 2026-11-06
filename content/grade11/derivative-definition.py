# -*- coding: utf-8 -*-
"""Nội dung bài g11-derivatives-01 (Đạo hàm: định nghĩa) – CHỈ NỘI DUNG."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *

LID = 'g11-derivatives-01'
CAT = 'Derivatives'
TOPIC = (CAT, 'Đạo hàm')
CV = 'Đạo hàm'

ensure_vocab([
 ('g11-tangent-line', 'tangent line', 'tiếp tuyến', CV, 'Find the equation of the tangent line.', ''),
 ('g11-slope', 'slope', 'hệ số góc', CV, 'The slope of the line is 2.', ''),
 ('g11-secant-line', 'secant line', 'cát tuyến', CV, 'A secant line meets the curve at two points.', ''),
 ('g11-difference-quotient', 'difference quotient', 'tỉ số biến thiên', CV, 'The difference quotient is the slope of a secant line.', r'\(\dfrac{f(x_0+h)-f(x_0)}{h}\)'),
 ('g11-tangent-point', 'point of tangency', 'tiếp điểm', CV, 'The point of tangency is (1; 1).', ''),
 ('g11-differentiable', 'differentiable', 'có đạo hàm', CV, 'The function is differentiable at x = 2.', ''),
 ('g11-rate-of-change', 'rate of change', 'tốc độ thay đổi', CV, 'The derivative is an instantaneous rate of change.', ''),
])
load_vocab()

# ---- kiểm tra số liệu ----
def D(f, x, h=1e-6): return (f(x + h) - f(x - h)) / (2 * h)
assert abs(D(lambda x: x * x, 3) - 6) < 1e-6 and abs(D(lambda x: x ** 3, 1) - 3) < 1e-6
g = lambda x: x * x - 4 * x + 3
assert abs(D(g, 2)) < 1e-6 and g(2) == -1 and abs(D(g, 3) - 2) < 1e-6 and g(3) == 0 and 2 * 3 - 6 == 0
assert abs(D(lambda x: x * x - 3 * x, 4) - 5) < 1e-5 and abs(D(lambda x: x ** 3, -1) - 3) < 1e-5
assert abs(D(lambda x: x * x + 5 * x, 1) - 7) < 1e-5 and abs(D(lambda x: x ** 3 - x, 2) - 11) < 1e-4
assert abs(D(lambda x: x * x - 6 * x, 5) - 4) < 1e-5 and abs(D(lambda x: x ** 3 + 2 * x, 1) - 5) < 1e-5
assert abs(D(lambda x: x * x, -3) + 6) < 1e-6 and abs(D(lambda x: x ** 3, -2) - 12) < 1e-4 and abs(D(lambda x: x * x, 5) - 10) < 1e-6
assert abs(D(lambda x: abs(x), 1e-3) - 1) < 1e-6 and abs(D(lambda x: abs(x), -1e-3) + 1) < 1e-6   # |x| có "góc nhọn" tại 0

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 55 minutes', 'khoảng 55 phút'),
            before=('limits of functions, equations of lines (previous lessons and grade 10)', 'giới hạn của hàm số, phương trình đường thẳng (bài trước và lớp 10)'))
goals = [
 (r'define \(f′(x_0)\) as a limit of difference quotients;', r'định nghĩa \(f′(x_0)\) là giới hạn của [[tỉ số biến thiên]];'),
 ('explain the derivative as the slope of the tangent line;', 'giải thích đạo hàm là [[hệ số góc]] của [[tiếp tuyến]];'),
 ('write the equation of a tangent line at a given point;', 'viết phương trình tiếp tuyến tại một điểm cho trước;'),
 ('recognize points where a function has no derivative.', 'nhận ra những điểm mà hàm số không [[có đạo hàm]].'),
]
vocab = [
 (r'<b>derivative</b> – the number \(f′(x_0)\) that tells how fast \(f\) changes at \(x_0\).', r'[[Đạo hàm]] – số \(f′(x_0)\) cho biết \(f\) thay đổi nhanh thế nào tại \(x_0\).'),
 ('<b>difference quotient</b> – the slope of the secant line through two points of the graph.', '[[Tỉ số biến thiên]] – hệ số góc của cát tuyến đi qua hai điểm của đồ thị.'),
 ('<b>secant line</b> – a line that meets a curve at two points.', '[[Cát tuyến]] – đường thẳng cắt đường cong tại hai điểm.'),
 ('<b>tangent line</b> – the line that just touches the curve at a point and has the same direction there.', '[[Tiếp tuyến]] – đường thẳng chỉ chạm đường cong tại một điểm và cùng hướng với đường cong ở đó.'),
 ('<b>point of tangency</b> – the point where the tangent line touches the curve.', '[[Tiếp điểm]] – điểm mà tiếp tuyến chạm đường cong.'),
 ('<b>slope</b> – how steep a line is: the rise divided by the run.', '[[Hệ số góc]] – độ dốc của đường thẳng: độ tăng chia cho độ rộng.'),
 (r'<b>differentiable</b> – having a derivative at that point.', '[[Có đạo hàm]] – tồn tại đạo hàm tại điểm đó.'),
 ('<b>rate of change</b> – how quickly a quantity changes.', '[[Tốc độ thay đổi]] – đại lượng thay đổi nhanh hay chậm.'),
]
phrases = [
 ('<b>Find the derivative of \\(f\\) at \\(x=2\\).</b>', 'Tìm đạo hàm của \\(f\\) tại \\(x=2\\).'),
 ('<b>Use the definition of the derivative.</b>', 'Dùng định nghĩa của đạo hàm.'),
 ('<b>Find the slope of the tangent line at the point.</b>', 'Tìm hệ số góc của tiếp tuyến tại điểm đó.'),
 ('<b>Write the equation of the tangent line.</b>', 'Viết phương trình tiếp tuyến.'),
 ('<b>Is the function differentiable at this point?</b>', 'Hàm số có đạo hàm tại điểm này không?'),
 ('<b>Find the point where the tangent line is horizontal.</b>', 'Tìm điểm mà tại đó tiếp tuyến nằm ngang.'),
]
review = (
 T(r'<b>Slope of a line.</b> The line through \((x_1;y_1)\) and \((x_2;y_2)\) has slope \(k=\dfrac{y_2-y_1}{x_2-x_1}\).', r'<b>Hệ số góc.</b> Đường thẳng qua \((x_1;y_1)\) và \((x_2;y_2)\) có hệ số góc \(k=\dfrac{y_2-y_1}{x_2-x_1}\).') +
 T(r'<b>Line through a point.</b> The line with slope \(k\) through \((x_0;y_0)\) is \(y=k(x-x_0)+y_0\).', r'<b>Đường thẳng qua một điểm.</b> Đường thẳng có hệ số góc \(k\) đi qua \((x_0;y_0)\) là \(y=k(x-x_0)+y_0\).') +
 T(r'<b>Limits.</b> You will use \(\lim_{h\to 0}\) and the factoring technique from the previous lesson.', r'<b>Giới hạn.</b> Bài này dùng \(\lim_{h\to 0}\) và kĩ thuật phân tích của bài trước.'))

theory = '<h3>5.1 %s</h3>' % TI('Definition of the derivative', 'Định nghĩa đạo hàm')
theory += BOX('mint', ('Definition', 'Định nghĩa'),
  M(r"f'(x_0)=\lim_{h\to 0}\dfrac{f(x_0+h)-f(x_0)}{h}"),
  T(r'The fraction is the <b>difference quotient</b>: the slope of the <b>secant line</b> through \((x_0;f(x_0))\) and \((x_0+h;f(x_0+h))\). When \(h\to 0\) the secant line turns into the <b>tangent line</b>.',
    r'Phân số là [[tỉ số biến thiên]]: hệ số góc của [[cát tuyến]] qua \((x_0;f(x_0))\) và \((x_0+h;f(x_0+h))\). Khi \(h\to 0\), cát tuyến trở thành [[tiếp tuyến]].'))
theory += BOX('mint', ('Tangent line', 'Phương trình tiếp tuyến'),
  T(r'The slope of the tangent line at the point of tangency \((x_0;f(x_0))\) is \(f′(x_0)\). The tangent line is', r'[[Hệ số góc]] của tiếp tuyến tại [[tiếp điểm]] \((x_0;f(x_0))\) là \(f′(x_0)\). Phương trình tiếp tuyến là'),
  M(r"y=f'(x_0)\,(x-x_0)+f(x_0)."))
theory += GRAPH({'view': [-4, 4, -2, 10], 'functions': [{'f': 'x^2', 'label': 'f(x) = x²'}], 'tangent': {'f': 0, 'at': 1, 'min': -3, 'max': 3}},
                cap=('The orange line is the tangent line at M(1; 1). Its slope is f′(1) = 2; in general the slope at x₀ is f′(x₀) = 2x₀.', 'Đường màu cam là tiếp tuyến tại M(1; 1). Hệ số góc của nó là f′(1) = 2; tổng quát, hệ số góc tại x₀ là f′(x₀) = 2x₀.'),
                alt=('Parabola with its tangent line at M(1; 1)', ''), height=340)

theory += '<h3>5.2 %s</h3>' % TI('Quick rules', 'Một số quy tắc nhanh')
theory += TABLE([('Function', 'Hàm số'), ('Derivative', 'Đạo hàm')], [
  [r'\(c\) (a constant)', r'\(0\)'], [r'\(x\)', r'\(1\)'], [r'\(x^2\)', r'\(2x\)'], [r'\(x^3\)', r'\(3x^2\)'], [r'\(x^n\)', r'\(n\,x^{n-1}\)'], [r'\(u+v\)', r"\(u'+v'\)"], [r'\(c\cdot u\)', r"\(c\cdot u'\)"]])
theory += T('These rules follow from the definition; the next lesson explains them in detail.', 'Các quy tắc này suy ra từ định nghĩa; bài sau sẽ giải thích chi tiết.')

theory += '<h3>5.3 %s</h3>' % TI('When there is no derivative', 'Khi nào không có đạo hàm')
theory += GRAPH({'view': [-3, 3, -1, 3], 'functions': [{'f': 'abs(x)', 'label': 'y = |x|'}], 'mark': {'extrema': [0]}},
                cap=('At x = 0 the graph has a sharp corner. The slopes of the secant lines are −1 on the left and +1 on the right, so there is no derivative at 0.', 'Tại x = 0 đồ thị có góc nhọn. Hệ số góc các cát tuyến là −1 ở bên trái và +1 ở bên phải, nên không có đạo hàm tại 0.'),
                alt=('Graph of the absolute value with a corner at the origin', ''), height=300)
theory += BOX('yellow', ('Watch out!', 'Lưu ý'),
  T(r'A function has no derivative at a corner, at a jump, at a vertical tangent, or where it is not defined.', r'Hàm số không có đạo hàm tại điểm góc nhọn, chỗ đứt, nơi tiếp tuyến thẳng đứng hoặc nơi hàm không xác định.'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Derivative from the definition', 'Đạo hàm theo định nghĩa'),
  T(r'Use the definition to find \(f′(3)\) for \(f(x)=x^2\).', r'Dùng định nghĩa để tìm \(f′(3)\) với \(f(x)=x^2\).'),
  (r'Write the difference quotient with \(x_0=3\), simplify, then let \(h\to 0\).', r'Viết tỉ số biến thiên với \(x_0=3\), rút gọn rồi cho \(h\to 0\).'),
  [T(r'\(\dfrac{f(3+h)-f(3)}{h}=\dfrac{(3+h)^2-9}{h}=\dfrac{6h+h^2}{h}\).', r'\(\dfrac{f(3+h)-f(3)}{h}=\dfrac{(3+h)^2-9}{h}=\dfrac{6h+h^2}{h}\).'),
   T(r'For \(h\ne 0\) this equals \(6+h\).', r'Với \(h\ne 0\) biểu thức bằng \(6+h\).'), T(r'\(\lim_{h\to 0}(6+h)=6\).', r'\(\lim_{h\to 0}(6+h)=6\).')], r"\(f'(3)=6\)")
examples += EXAMPLE(2, ('Intermediate', 'Trung bình'), ('A tangent line', 'Viết phương trình tiếp tuyến'),
  T(r'Find the equation of the tangent line to \(y=x^3\) at the point \((1;1)\).', r'Viết phương trình tiếp tuyến của \(y=x^3\) tại điểm \((1;1)\).'),
  (r'We need the slope \(f′(1)\), then we use \(y=f′(x_0)(x-x_0)+f(x_0)\).', r'Cần hệ số góc \(f′(1)\), rồi dùng \(y=f′(x_0)(x-x_0)+f(x_0)\).'),
  [T(r'\(f′(x)=3x^2\), so \(f′(1)=3\).', r'\(f′(x)=3x^2\) nên \(f′(1)=3\).'), T(r'\(y=3(x-1)+1=3x-2\).', r'\(y=3(x-1)+1=3x-2\).')], r'\(y=3x-2\)')
examples += EXAMPLE(3, ('Advanced', 'Nâng cao'), ('Special tangent lines', 'Tiếp tuyến đặc biệt'),
  T(r'For \(f(x)=x^2-4x+3\): (a) find the point where the tangent line is horizontal; (b) find the tangent line parallel to \(y=2x+1\).', r'Cho \(f(x)=x^2-4x+3\): (a) tìm điểm mà tiếp tuyến nằm ngang; (b) viết tiếp tuyến song song với \(y=2x+1\).') +
  GRAPH({'view': [-1, 5, -3, 5], 'functions': [{'f': 'x^2-4x+3', 'label': 'f(x) = x² − 4x + 3'}], 'mark': {'extrema': [0], 'roots': [0]}, 'tangent': {'f': 0, 'at': [2, 3], 'min': -0.5, 'max': 4.5, 'step': 0.1}},
        cap=('The two tangent lines found in the solution: the horizontal one at (2; −1) and the one at (3; 0) with slope 2.', 'Hai tiếp tuyến tìm được trong lời giải: tiếp tuyến nằm ngang tại (2; −1) và tiếp tuyến tại (3; 0) có hệ số góc 2.'),
        alt=('Parabola with two tangent lines', ''), height=320),
  (r'Here \(f′(x)=2x-4\). A horizontal line has slope 0, and parallel lines have the same slope.', r'Ở đây \(f′(x)=2x-4\). Đường nằm ngang có hệ số góc 0, hai đường song song có cùng hệ số góc.'),
  [T(r'(a) \(2x-4=0\Rightarrow x=2\), \(f(2)=-1\): the point is \((2;-1)\).', r'(a) \(2x-4=0\Rightarrow x=2\), \(f(2)=-1\): điểm cần tìm là \((2;-1)\).'),
   T(r'(b) The slope is 2: \(2x-4=2\Rightarrow x=3\), \(f(3)=0\).', r'(b) Hệ số góc bằng 2: \(2x-4=2\Rightarrow x=3\), \(f(3)=0\).'),
   T(r'The tangent line: \(y=2(x-3)+0=2x-6\). It is parallel to \(y=2x+1\) and different from it.', r'Tiếp tuyến: \(y=2(x-3)+0=2x-6\). Nó song song với \(y=2x+1\) và khác đường này.')],
  TI(r'(a) \((2;-1)\); (b) \(y=2x-6\).', r'(a) \((2;-1)\); (b) \(y=2x-6\).'))

# A1 f'(x0) của x²; A2 f'(x0) của x³; A3 phương trình tiếp tuyến; B nhận định; C5 f'(x0); C6 hệ số góc tiếp tuyến
S1 = [
  [MCQ(1, (r"If \(f(x)=x^2\), what is \(f'(1)\)?", r"Nếu \(f(x)=x^2\) thì \(f'(1)\) bằng bao nhiêu?"), ['1', '2', '3', '0'], 'b', (r"Answer: b. \(f'(x)=2x\), so \(f'(1)=2\).", r"Đáp án b. \(f'(x)=2x\) nên \(f'(1)=2\).")),
   MCQ(2, (r"If \(f(x)=x^3\), what is \(f'(2)\)?", r"Nếu \(f(x)=x^3\) thì \(f'(2)\) bằng bao nhiêu?"), ['6', '8', '12', '3'], 'c', (r"Answer: c. \(f'(x)=3x^2\), so \(f'(2)=12\).", r"Đáp án c. \(f'(x)=3x^2\) nên \(f'(2)=12\).")),
   MCQ(3, (r'What is the tangent line to \(y=x^2\) at \((1;1)\)?', r'Tiếp tuyến của \(y=x^2\) tại \((1;1)\) là đường nào?'), ['y=2x-1', 'y=x', 'y=2x+1', 'y=x-1'], 'a', (r'Answer: a. \(y=2(x-1)+1=2x-1\).', r'Đáp án a. \(y=2(x-1)+1=2x-1\).'))],
  [TF(4, (r"If \(f'(x_0)=0\), the tangent line at \(x_0\) is horizontal.", r"Nếu \(f'(x_0)=0\) thì tiếp tuyến tại \(x_0\) nằm ngang."), 'true', (r'True. A line with slope 0 is horizontal.', r'Đúng. Đường thẳng có hệ số góc 0 thì nằm ngang.'))],
  [SHORT(5, (r"If \(f(x)=x^2-3x\), find \(f'(4)\).", r"Cho \(f(x)=x^2-3x\). Tìm \(f'(4)\)."), '5', 'number', ('Enter a number.', 'Nhập một số.'), (r"Answer: 5. \(f'(x)=2x-3\), \(f'(4)=5\).", r"Đáp số: 5. \(f'(x)=2x-3\), \(f'(4)=5\).")),
   SHORT(6, (r'Find the slope of the tangent line to \(y=x^3\) at \(x=-1\).', r'Tìm hệ số góc của tiếp tuyến của \(y=x^3\) tại \(x=-1\).'), '3', 'number', ('Enter a number.', 'Nhập một số.'), (r'Answer: 3. \(3\cdot(-1)^2=3\).', r'Đáp số: 3. \(3\cdot(-1)^2=3\).'))]]
S2 = [
  [MCQ(1, (r"If \(f(x)=x^2\), what is \(f'(-3)\)?", r"Nếu \(f(x)=x^2\) thì \(f'(-3)\) bằng bao nhiêu?"), ['6', '-6', '-3', '9'], 'b', (r"Answer: b. \(f'(x)=2x\), so \(f'(-3)=-6\).", r"Đáp án b. \(f'(x)=2x\) nên \(f'(-3)=-6\).")),
   MCQ(2, (r"If \(f(x)=x^3\), what is \(f'(1)\)?", r"Nếu \(f(x)=x^3\) thì \(f'(1)\) bằng bao nhiêu?"), ['1', '2', '3', '0'], 'c', (r"Answer: c. \(3\cdot 1^2=3\).", r"Đáp án c. \(3\cdot 1^2=3\).")),
   MCQ(3, (r'What is the tangent line to \(y=x^3\) at \((1;1)\)?', r'Tiếp tuyến của \(y=x^3\) tại \((1;1)\) là đường nào?'), ['y=3x+2', 'y=3x-2', 'y=x', 'y=3x-1'], 'b', (r'Answer: b. \(y=3(x-1)+1=3x-2\).', r'Đáp án b. \(y=3(x-1)+1=3x-2\).'))],
  [TF(4, (r"If \(f'(x_0)\gt 0\), the tangent line goes down from left to right.", r"Nếu \(f'(x_0)\gt 0\) thì tiếp tuyến đi xuống từ trái sang phải."), 'false', (r'False. A positive slope means the line goes up.', r'Sai. Hệ số góc dương nghĩa là đường thẳng đi lên.'))],
  [SHORT(5, (r"If \(f(x)=x^2+5x\), find \(f'(1)\).", r"Cho \(f(x)=x^2+5x\). Tìm \(f'(1)\)."), '7', 'number', ('Enter a number.', 'Nhập một số.'), (r"Answer: 7. \(f'(x)=2x+5\).", r"Đáp số: 7. \(f'(x)=2x+5\).")),
   SHORT(6, (r'Find the slope of the tangent line to \(y=x^3-x\) at \(x=2\).', r'Tìm hệ số góc của tiếp tuyến của \(y=x^3-x\) tại \(x=2\).'), '11', 'number', ('Enter a number.', 'Nhập một số.'), (r"Answer: 11. \(y'=3x^2-1=11\).", r"Đáp số: 11. \(y'=3x^2-1=11\)."))]]
S3 = [
  [MCQ(1, (r"If \(f(x)=x^2\), what is \(f'(5)\)?", r"Nếu \(f(x)=x^2\) thì \(f'(5)\) bằng bao nhiêu?"), ['5', '10', '25', '2'], 'b', (r"Answer: b. \(2\cdot 5=10\).", r"Đáp án b. \(2\cdot 5=10\).")),
   MCQ(2, (r"If \(f(x)=x^3\), what is \(f'(-2)\)?", r"Nếu \(f(x)=x^3\) thì \(f'(-2)\) bằng bao nhiêu?"), ['-12', '12', '-8', '8'], 'b', (r"Answer: b. \(3\cdot(-2)^2=12\).", r"Đáp án b. \(3\cdot(-2)^2=12\).")),
   MCQ(3, (r'What is the tangent line to \(y=x^2\) at \((-1;1)\)?', r'Tiếp tuyến của \(y=x^2\) tại \((-1;1)\) là đường nào?'), ['y=2x+1', 'y=-2x+1', 'y=-2x-1', 'y=2x-1'], 'c', (r'Answer: c. The slope is \(2\cdot(-1)=-2\): \(y=-2(x+1)+1=-2x-1\).', r'Đáp án c. Hệ số góc là \(2\cdot(-1)=-2\): \(y=-2(x+1)+1=-2x-1\).'))],
  [TF(4, (r'The function \(y=|x|\) has a derivative at \(x=0\).', r'Hàm số \(y=|x|\) có đạo hàm tại \(x=0\).'), 'false', (r'False. The graph has a sharp corner at 0.', r'Sai. Đồ thị có góc nhọn tại 0.'))],
  [SHORT(5, (r"If \(f(x)=x^2-6x\), find \(f'(5)\).", r"Cho \(f(x)=x^2-6x\). Tìm \(f'(5)\)."), '4', 'number', ('Enter a number.', 'Nhập một số.'), (r"Answer: 4. \(f'(x)=2x-6\).", r"Đáp số: 4. \(f'(x)=2x-6\).")),
   SHORT(6, (r'Find the slope of the tangent line to \(y=x^3+2x\) at \(x=1\).', r'Tìm hệ số góc của tiếp tuyến của \(y=x^3+2x\) tại \(x=1\).'), '5', 'number', ('Enter a number.', 'Nhập một số.'), (r"Answer: 5. \(y'=3x^2+2=5\).", r"Đáp số: 5. \(y'=3x^2+2=5\)."))]]
practice = LEVEL_PRACTICE([('A. Multiple Choice', 'A. Trắc nghiệm'), ('B. True or False', 'B. Đúng hoặc sai'), ('C. Short Answer', 'C. Trả lời ngắn')], {1: S1, 2: S2, 3: S3})

mistakes = [
 (r"<b>Math knowledge.</b> Mixing up \(f'(x_0)\) (a number) with \(f(x_0)\) (the height of the graph).", r"<b>Kiến thức Toán.</b> Nhầm \(f'(x_0)\) (một số, độ dốc) với \(f(x_0)\) (độ cao của đồ thị)."),
 (r"<b>Tangent lines.</b> Writing \(y=f'(x_0)(x-x_0)\) and forgetting \(+f(x_0)\).", r"<b>Tiếp tuyến.</b> Viết \(y=f'(x_0)(x-x_0)\) và quên \(+f(x_0)\)."),
 (r'<b>Differentiability.</b> Assuming every continuous function has a derivative everywhere. The graph of \(|x|\) is continuous but has a corner at 0.', r'<b>Có đạo hàm.</b> Cho rằng mọi hàm liên tục đều có đạo hàm ở mọi điểm. Đồ thị \(|x|\) liên tục nhưng có góc nhọn tại 0.'),
 (r'<b>Using the definition.</b> Substituting \(h=0\) too early, which gives \(\dfrac00\). Simplify first.', r'<b>Dùng định nghĩa.</b> Thay \(h=0\) quá sớm nên được \(\dfrac00\). Hãy rút gọn trước.'),
]
summary = [
 (r"\(f'(x_0)=\lim_{h\to 0}\dfrac{f(x_0+h)-f(x_0)}{h}\): the limit of the slopes of secant lines.", r"\(f'(x_0)=\lim_{h\to 0}\dfrac{f(x_0+h)-f(x_0)}{h}\): giới hạn của hệ số góc các cát tuyến."),
 (r"\(f'(x_0)\) is the slope of the tangent line at \((x_0;f(x_0))\).", r"\(f'(x_0)\) là hệ số góc của tiếp tuyến tại \((x_0;f(x_0))\)."),
 (r"Tangent line: \(y=f'(x_0)(x-x_0)+f(x_0)\). Horizontal tangent: \(f'(x_0)=0\).", r"Tiếp tuyến: \(y=f'(x_0)(x-x_0)+f(x_0)\). Tiếp tuyến nằm ngang: \(f'(x_0)=0\)."),
 (r"\((x^n)'=nx^{n-1}\), \((c)'=0\), \((u+v)'=u'+v'\).", r"\((x^n)'=nx^{n-1}\), \((c)'=0\), \((u+v)'=u'+v'\)."),
 ('Key English phrases: use the definition; slope of the tangent line; equation of the tangent line; differentiable.', 'Cụm tiếng Anh cần nhớ: use the definition (dùng định nghĩa); slope of the tangent line (hệ số góc của tiếp tuyến); equation of the tangent line (phương trình tiếp tuyến); differentiable (có đạo hàm).'),
]
checks = [
 ('I can compute a derivative from the definition.', 'Tôi tính được đạo hàm theo định nghĩa.'),
 ('I can explain the derivative as the slope of the tangent line.', 'Tôi giải thích được đạo hàm là hệ số góc của tiếp tuyến.'),
 ('I can write the equation of a tangent line.', 'Tôi viết được phương trình tiếp tuyến.'),
 ('I can find where the tangent line is horizontal or parallel to a given line.', 'Tôi tìm được điểm có tiếp tuyến nằm ngang hoặc song song với đường cho trước.'),
 STD_SUMMARY_CHECK_EN(),
]

lesson(id=LID, title_en='The Derivative: Definition', title_vi='Đạo hàm: định nghĩa và tiếp tuyến', topic=TOPIC,
       folder='derivatives', file='derivative-definition',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='The derivative as a limit and as the slope of the tangent line.', level='Intermediate', minutes=55,
       description_vi='Đạo hàm là giới hạn của tỉ số biến thiên và là hệ số góc của tiếp tuyến.',
       tags_vi=['đạo hàm', 'tiếp tuyến', 'hệ số góc', 'định nghĩa', 'cát tuyến'],
       prerequisites=['g11-limits-02'], tags=['derivative', 'tangent line', 'slope', 'definition'], order=50)
