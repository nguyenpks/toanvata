# -*- coding: utf-8 -*-
"""Nội dung bài g11-functions-01 (Đồ thị hàm số) – CHỈ NỘI DUNG. Bố cục, số mục, tên mục, số lớp do config/model.json quyết định.
Bài tập: mỗi mức học một bộ riêng, cùng dạng nhưng khác số liệu (LEVEL_PRACTICE)."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *

LID = 'g11-functions-01'
CAT = 'Functions and Graphs'
TOPIC = (CAT, 'Hàm số và đồ thị')
CV = 'Hàm số và đồ thị'

ensure_vocab([
 ('v-range', 'range', 'tập giá trị', CV, 'The range of f is [-4, +infinity).', ''),
 ('v-zero', 'zero (root)', 'nghiệm', CV, 'The zeros of f are x = -1 and x = 3.', ''),
 ('v-x-intercept', 'x-intercept', 'giao điểm với trục hoành', CV, 'Find the x-intercepts of the graph.', ''),
 ('v-y-intercept', 'y-intercept', 'giao điểm với trục tung', CV, 'The y-intercept is (0, f(0)).', ''),
   ('v-piecewise', 'piecewise function', 'hàm số từng đoạn', CV, 'A piecewise function has different rules on different intervals.', ''),
 ('v-absolute-value', 'absolute value', 'giá trị tuyệt đối', CV, 'The absolute value of -3 is 3.', r'\(|x|\)'),
  ('v-vertical-line-test', 'vertical line test', 'phép thử đường thẳng đứng', CV, 'Use the vertical line test.', ''),
])
load_vocab()

# kiểm tra số liệu bằng tính toán trước khi viết đáp án
f1 = lambda x: x * x - 2 * x - 3
assert f1(-1) == 0 and f1(3) == 0 and f1(0) == -3 and f1(1) == -4
assert 2 * 2 ** 2 - 3 * 2 + 1 == 3 and 2 * (-1) ** 2 - 3 * (-1) + 1 == 6
pw = lambda x: 2 * x + 1 if x <= 1 else 5 - x
assert pw(1) == 3 and pw(3) == 2 and pw(0) == 1 and 5 - 1 == 4

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 50 minutes', 'khoảng 50 phút'),
            before=('functions, equations and inequalities (grades 9–10)', 'hàm số, phương trình, bất phương trình (lớp 9–10)'))
goals = [
 ('find the domain of a function and evaluate it at a number;', 'tìm [[tập xác định]] của [[hàm số]] và tính giá trị hàm số tại một số;'),
 ('read intercepts, increasing and decreasing intervals and the range from a graph;', 'đọc giao điểm với các trục, khoảng [[đồng biến|hàm số đồng biến]], [[nghịch biến|hàm số nghịch biến]] và [[tập giá trị]] từ [[đồ thị]];'),
 ('recognize graphs of polynomial, rational, radical, absolute value and piecewise functions;', 'nhận ra đồ thị hàm đa thức, phân thức, căn thức, [[giá trị tuyệt đối]] và [[hàm số từng đoạn]];'),
 ('use the graph tool: zoom, move the axes and read asymptotes.', 'dùng công cụ vẽ đồ thị: thu phóng, di chuyển trục và đọc [[tiệm cận|đường tiệm cận]].'),
]
vocab = [
 ('<b>function</b> – a rule that gives exactly one output \\(y\\) for each input \\(x\\).', '[[Hàm số]] – quy tắc cho đúng một giá trị \\(y\\) ứng với mỗi giá trị \\(x\\).'),
 ('<b>domain</b> – the set of all inputs \\(x\\) for which \\(f(x)\\) is defined.', '[[Tập xác định]] – tập các giá trị \\(x\\) để \\(f(x)\\) có nghĩa.'),
 ('<b>range</b> – the set of all outputs \\(y=f(x)\\).', '[[Tập giá trị]] – tập các giá trị \\(y=f(x)\\) nhận được.'),
 ('<b>graph</b> – the set of all points \\((x;f(x))\\) in the plane.', '[[Đồ thị]] – tập các điểm \\((x;f(x))\\) trong mặt phẳng tọa độ.'),
 ('<b>zero (root)</b> – a number \\(x\\) with \\(f(x)=0\\).', '[[Nghiệm]] – số \\(x\\) thỏa \\(f(x)=0\\).'),
 ('<b>x-intercept</b> – a point where the graph meets the x-axis.', '[[Giao điểm với trục hoành]] – điểm đồ thị cắt trục \\(Ox\\).'),
 ('<b>y-intercept</b> – the point \\((0;f(0))\\) where the graph meets the y-axis.', '[[Giao điểm với trục tung]] – điểm \\((0;f(0))\\) đồ thị cắt trục \\(Oy\\).'),
 ('<b>increasing</b> – the graph goes up from left to right.', '[[Đồng biến|hàm số đồng biến]] – đồ thị đi lên khi \\(x\\) tăng.'),
 ('<b>decreasing</b> – the graph goes down from left to right.', '[[Nghịch biến|hàm số nghịch biến]] – đồ thị đi xuống khi \\(x\\) tăng.'),
 ('<b>piecewise function</b> – a function with different rules on different intervals.', '[[Hàm số từng đoạn]] – hàm số có công thức khác nhau trên các khoảng khác nhau.'),
 ('<b>absolute value</b> – the distance from \\(x\\) to 0: \\(|x|\\).', '[[Giá trị tuyệt đối]] – khoảng cách từ \\(x\\) đến 0: \\(|x|\\).'),
 ('<b>asymptote</b> – a line that the graph gets closer and closer to.', '[[Tiệm cận|đường tiệm cận]] – đường thẳng mà đồ thị tiến sát dần.'),
]
phrases = [
 ('<b>State the domain of \\(f\\).</b>', 'Nêu tập xác định của \\(f\\).'),
 ('<b>Evaluate \\(f(2)\\).</b> Substitute \\(x=2\\).', 'Tính \\(f(2)\\). Thay \\(x=2\\).'),
 ('<b>Find the x-intercepts and the y-intercept.</b>', 'Tìm các giao điểm với trục hoành và với trục tung.'),
 ('<b>On which intervals is \\(f\\) increasing?</b>', 'Hàm số \\(f\\) đồng biến trên những khoảng nào?'),
 ('<b>Find the range of \\(f\\).</b>', 'Tìm tập giá trị của \\(f\\).'),
 ('<b>Sketch the graph of \\(f\\).</b>', 'Phác họa đồ thị của \\(f\\).'),
 ('<b>Does the graph have an asymptote?</b>', 'Đồ thị có đường tiệm cận không?'),
 ('<b>Is this the graph of a function?</b> Use the vertical line test.', 'Đây có phải đồ thị của một hàm số không? Dùng phép thử đường thẳng đứng.'),
]
review = (
 T(r'<b>Evaluating.</b> If \(f(x)=2x+1\), then \(f(3)=2\cdot 3+1=7\).', r'<b>Tính giá trị.</b> Nếu \(f(x)=2x+1\) thì \(f(3)=2\cdot 3+1=7\).') +
 T(r'<b>Inequalities.</b> \(x-2\ge 0\) means \(x\ge 2\). We write the solution as the interval \([2,+\infty)\).', r'<b>Bất phương trình.</b> \(x-2\ge 0\) nghĩa là \(x\ge 2\); viết nghiệm là khoảng \([2,+\infty)\).') +
 T(r'<b>Coordinates.</b> The point \((a;b)\) is on the graph of \(y=f(x)\) exactly when \(b=f(a)\).', r'<b>Tọa độ.</b> Điểm \((a;b)\) thuộc đồ thị \(y=f(x)\) đúng khi \(b=f(a)\).')
)

theory = '<h3>5.1 %s</h3>' % TI('Function and graph', 'Hàm số và đồ thị')
theory += BOX('mint', ('Definition', 'Định nghĩa'),
  T(r'A <b>function</b> \(f\) assigns to each \(x\) in its <b>domain</b> exactly one number \(y=f(x)\). The <b>graph</b> of \(f\) is the set of points \((x;f(x))\).',
    r'[[Hàm số]] \(f\) cho mỗi \(x\) thuộc [[tập xác định]] đúng một số \(y=f(x)\). [[Đồ thị]] của \(f\) là tập các điểm \((x;f(x))\).'),
  T(r'<b>Vertical line test:</b> a curve is the graph of a function if every vertical line meets it at most once.', r'<b>Phép thử đường thẳng đứng:</b> một đường cong là đồ thị hàm số nếu mọi đường thẳng đứng cắt nó tại nhiều nhất một điểm.'))
theory += GRAPH({'view': [-3, 5, -5, 6], 'functions': [{'f': 'x^2-2x-3', 'label': 'y = x² − 2x − 3'}],
                 'mark': {'roots': [0], 'yint': [0], 'extrema': [0]}, 'monotone': {'f': 0}},
                cap=('Graph of y = x² − 2x − 3: intercepts, minimum, increasing and decreasing parts.', 'Đồ thị y = x² − 2x − 3: giao điểm với các trục, điểm thấp nhất, phần đồng biến và nghịch biến.'),
                alt=('Parabola y = x squared minus 2x minus 3 with intercepts and minimum point', ''), height=340)
theory += T(r'<b>How to read a graph.</b> Zeros: where the graph meets the x-axis. Increasing: the graph rises from left to right. Range: all heights the graph reaches.',
            r'<b>Cách đọc đồ thị.</b> Nghiệm: nơi đồ thị cắt trục hoành. Đồng biến: đồ thị đi lên từ trái sang phải. Tập giá trị: mọi độ cao mà đồ thị đạt tới.')

theory += '<h3>5.2 %s</h3>' % TI('Domain of a function', 'Tập xác định của hàm số')
theory += TABLE([('Form of f(x)', 'Dạng của f(x)'), ('Condition', 'Điều kiện'), ('Example', 'Ví dụ')], [
  [TI('polynomial', 'đa thức'), TI('no condition', 'không có điều kiện'), r'\(x^2-3x\): \(\mathbb{R}\)'],
  [TI('fraction', 'phân thức'), TI('denominator is not 0', 'mẫu khác 0'), r'\(\dfrac{1}{x-2}\): \(x\ne 2\)'],
  [TI('square root', 'căn bậc hai'), TI('radicand is at least 0', 'biểu thức dưới căn không âm'), r'\(\sqrt{x-1}\): \(x\ge 1\)'],
  [TI('logarithm', 'logarit'), TI('argument is positive', 'biểu thức trong logarit dương'), r'\(\ln x\): \(x\gt 0\)']])
theory += GRAPH({'view': [-8, 10, -12, 14], 'functions': [{'f': '(x^2-1)/(x-2)', 'label': 'y = (x² − 1)/(x − 2)'}],
                 'asymptotes': [{'type': 'v', 'x': 2}, {'type': 'oblique', 'm': 1, 'b': 2}], 'mark': {'roots': [0], 'yint': [0]}},
                cap=('The graph is cut at x = 2, so the domain is R without 2. The dashed lines are asymptotes.', 'Đồ thị bị cắt tại x = 2 nên tập xác định là R trừ 2. Các đường nét đứt là tiệm cận.'),
                alt=('Graph of a rational function with a vertical and an oblique asymptote', ''), height=360)
theory += T(r'The domain is \(\mathbb{R}\setminus\{2\}\). Notice that the graph does <b>not</b> join the two branches across \(x=2\).', r'Tập xác định là \(\mathbb{R}\setminus\{2\}\). Chú ý đồ thị <b>không</b> nối hai nhánh qua \(x=2\).')

theory += '<h3>5.3 %s</h3>' % TI('Families of graphs', 'Các họ đồ thị thường gặp')
theory += TABLE([('Function', 'Hàm số'), ('Shape of the graph', 'Dạng đồ thị')], [
  [r'\(y=ax^2+bx+c\)', TI('parabola, opens up if \\(a\\gt 0\\)', 'parabol, bề lõm hướng lên nếu \\(a\\gt 0\\)')],
  [r'\(y=\dfrac{ax+b}{cx+d}\)', TI('hyperbola with vertical and horizontal asymptotes', 'hypebol có tiệm cận đứng và tiệm cận ngang')],
  [r'\(y=\sqrt{x+k}\)', TI('half of a parabola, starts at \\(x=-k\\)', 'nửa parabol, bắt đầu tại \\(x=-k\\)')],
  [r'\(y=|x-h|\)', TI('V-shape with corner at \\(x=h\\)', 'hình chữ V, có điểm nhọn tại \\(x=h\\)')],
  [TI('piecewise', 'từng đoạn'), TI('pieces joined or broken at the endpoints', 'các đoạn nối liền hoặc bị đứt tại đầu mút')]])
theory += GRAPH({'view': [-5, 7, -3, 6],
                 'functions': [{'f': 'sqrt(x+1)', 'label': 'y = √(x + 1)'}, {'f': 'abs(x-2)', 'label': 'y = |x − 2|'}], 'mark': {'extrema': [1]}},
                cap=('A radical function and an absolute value function on the same axes.', 'Hàm căn thức và hàm giá trị tuyệt đối trên cùng một hệ trục.'),
                alt=('Graphs of square root and absolute value functions', ''), height=340)
theory += BOX('blue', ('Compare the graphs', 'So sánh các đồ thị'),
  T(r'In \(y=a(x-h)^2+k\), the number \(a\) changes the opening, \(h\) moves the graph left or right, and \(k\) moves it up or down.', r'Trong \(y=a(x-h)^2+k\), số \(a\) đổi độ mở, \(h\) dời đồ thị sang trái/phải, \(k\) dời lên/xuống.'))
theory += GRAPH({'view': [-6, 6, -6, 8], 'params': [{'name': 'a', 'min': -3, 'max': 3, 'value': 1, 'step': 0.1}, {'name': 'h', 'min': -4, 'max': 4, 'value': 0, 'step': 0.1}, {'name': 'k', 'min': -4, 'max': 4, 'value': -2, 'step': 0.1}], 'family': [{'a': 1, 'h': 0, 'k': 0, '_label': 'y = x²'}, {'a': 1, 'h': 2, 'k': -2, '_label': 'y = (x − 2)² − 2'}, {'a': -0.5, 'h': -2, 'k': 4, '_label': 'y = −0.5(x + 2)² + 4'}],
                 'functions': [{'f': 'a*(x-h)^2+k', 'label': 'y = a(x − h)² + k'}]},
                cap=('From y = x²: h = 2, k = −2 moves the graph 2 units right and 2 units down; a = −0.5 turns it upside down and makes it wider.', 'Từ y = x²: h = 2, k = −2 dời đồ thị sang phải 2 đơn vị và xuống dưới 2 đơn vị; a = −0,5 làm đồ thị quay xuống và mở rộng hơn.'), alt=('Three parabolas of the form y = a(x − h)² + k', ''), height=340)
theory += BOX('yellow', ('Reading the figures', 'Đọc hình vẽ'),
  T(r'All graphs are drawn with LaTeX (PGFPlots). Asymptotes are dashed lines; open dots are points that do not belong to the graph.', r'Mọi đồ thị được vẽ bằng LaTeX (PGFPlots). Đường tiệm cận vẽ nét đứt; chấm rỗng là điểm không thuộc đồ thị.'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Reading a graph', 'Đọc đồ thị'),
  T(r'Use the graph of \(y=x^2-2x-3\) in section 5.1. Find the x-intercepts, the y-intercept, the intervals where the function increases and decreases, and the range.',
    r'Dùng đồ thị \(y=x^2-2x-3\) ở mục 5.1. Tìm giao điểm với hai trục, các khoảng đồng biến, nghịch biến và tập giá trị.'),
  (r'Read the points where the graph meets the axes, then find the lowest point (the vertex) to decide where the graph falls and rises.', r'Đọc các điểm đồ thị cắt hai trục, rồi tìm điểm thấp nhất (đỉnh) để biết đồ thị đi xuống, đi lên ở đâu.'),
  [T(r'x-intercepts: \(f(x)=0\Leftrightarrow (x+1)(x-3)=0\), so \(x=-1\) and \(x=3\). The graph meets \(Ox\) at \((-1;0)\) and \((3;0)\).', r'Giao điểm với \(Ox\): \(f(x)=0\Leftrightarrow (x+1)(x-3)=0\) nên \(x=-1\) và \(x=3\): các điểm \((-1;0)\), \((3;0)\).'),
   T(r'y-intercept: \(f(0)=-3\), the point \((0;-3)\).', r'Giao điểm với \(Oy\): \(f(0)=-3\), điểm \((0;-3)\).'),
   T(r'The lowest point is the vertex \((1;-4)\). The function decreases on \((-\infty;1)\) and increases on \((1;+\infty)\).', r'Điểm thấp nhất là đỉnh \((1;-4)\). Hàm số nghịch biến trên \((-\infty;1)\) và đồng biến trên \((1;+\infty)\).'),
   T(r'Every height is at least \(-4\), so the range is \([-4;+\infty)\).', r'Mọi độ cao đều không nhỏ hơn \(-4\) nên tập giá trị là \([-4;+\infty)\).')],
  TI(r'\((-1;0)\), \((3;0)\), \((0;-3)\); decreasing on \((-\infty;1)\), increasing on \((1;+\infty)\); range \([-4;+\infty)\).', r'\((-1;0)\), \((3;0)\), \((0;-3)\); nghịch biến trên \((-\infty;1)\), đồng biến trên \((1;+\infty)\); tập giá trị \([-4;+\infty)\).'))
examples += EXAMPLE(2, ('Intermediate', 'Trung bình'), ('Finding the domain', 'Tìm tập xác định'),
  T(r'Find the domain of \(f(x)=\dfrac{\sqrt{x-1}}{x-3}\).', r'Tìm tập xác định của \(f(x)=\dfrac{\sqrt{x-1}}{x-3}\).'),
  (r'The expression has a square root and a fraction. We need both conditions at the same time.', r'Biểu thức có căn bậc hai và phân thức, nên cần đồng thời cả hai điều kiện.'),
  [T(r'Square root: \(x-1\ge 0\Leftrightarrow x\ge 1\).', r'Căn bậc hai: \(x-1\ge 0\Leftrightarrow x\ge 1\).'),
   T(r'Fraction: \(x-3\ne 0\Leftrightarrow x\ne 3\).', r'Phân thức: \(x-3\ne 0\Leftrightarrow x\ne 3\).'),
   T(r'Take \(x\ge 1\) and remove \(x=3\): the domain is \([1;3)\cup(3;+\infty)\).', r'Lấy \(x\ge 1\) rồi bỏ \(x=3\): tập xác định là \([1;3)\cup(3;+\infty)\).')],
  r'\(D=[1;3)\cup(3;+\infty)\).')
examples += EXAMPLE(3, ('Advanced', 'Nâng cao'), ('A piecewise function', 'Hàm số từng đoạn'),
  T(r'Let \(f(x)=2x+1\) if \(x\le 1\) and \(f(x)=5-x\) if \(x\gt 1\). Find \(f(0)\), \(f(1)\), \(f(3)\). Does the graph have a break at \(x=1\)?', r'Cho \(f(x)=2x+1\) nếu \(x\le 1\) và \(f(x)=5-x\) nếu \(x\gt 1\). Tính \(f(0)\), \(f(1)\), \(f(3)\). Đồ thị có bị đứt tại \(x=1\) không?') +
  GRAPH({'view': [-3, 6, -6, 6], 'functions': [{'f': '2x+1', 'domain': [-3, 1], 'open': [False, False], 'color': '#046b4d', 'label': 'y = 2x + 1  (x ≤ 1)'},
                                               {'f': '5-x', 'domain': [1, 6], 'open': [True, False], 'color': '#c2410c', 'label': 'y = 5 − x  (x > 1)'}]},
        alt=('Piecewise graph with a jump at x = 1', ''), height=320),
  (r'First decide which rule to use: compare each \(x\) with 1.', r'Trước hết chọn công thức phù hợp: so sánh từng giá trị \(x\) với 1.'),
  [T(r'\(0\le 1\), so \(f(0)=2\cdot 0+1=1\).', r'\(0\le 1\) nên \(f(0)=2\cdot 0+1=1\).'),
   T(r'\(1\le 1\), so \(f(1)=2\cdot 1+1=3\).', r'\(1\le 1\) nên \(f(1)=2\cdot 1+1=3\).'),
   T(r'\(3\gt 1\), so \(f(3)=5-3=2\).', r'\(3\gt 1\) nên \(f(3)=5-3=2\).'),
   T(r'Just to the right of 1 the second rule gives values close to \(5-1=4\), but \(f(1)=3\). The pieces do not meet: the graph has a jump at \(x=1\) (filled dot at \((1;3)\), empty dot at \((1;4)\)).', r'Ngay bên phải 1, công thức thứ hai cho giá trị gần \(5-1=4\), còn \(f(1)=3\). Hai đoạn không gặp nhau: đồ thị bị đứt tại \(x=1\) (chấm đặc \((1;3)\), chấm rỗng \((1;4)\)).')],
  TI(r'\(f(0)=1\), \(f(1)=3\), \(f(3)=2\); the graph has a jump at \(x=1\).', r'\(f(0)=1\), \(f(1)=3\), \(f(3)=2\); đồ thị bị đứt tại \(x=1\).'))

# ----- Bài tập: mỗi mức một bộ riêng, cùng dạng -----
R = r'\mathbb{R}'
S1 = [
  [MCQ(1, (r'What is the domain of \(f(x)=\sqrt{x-2}\)?', r'Tập xác định của \(f(x)=\sqrt{x-2}\) là gì?'), [r'[2,+\infty)', r'(2,+\infty)', r'(-\infty,2]', R], 'a',
        (r'Answer: a. We need \(x-2\ge 0\), so \(x\ge 2\).', r'Đáp án a. Cần \(x-2\ge 0\) nên \(x\ge 2\).')),
   MCQ(2, (r'If \(f(x)=x^2-4x+3\), what is \(f(-1)\)?', r'Nếu \(f(x)=x^2-4x+3\) thì \(f(-1)\) bằng bao nhiêu?'), ['8', '0', '2', '-6'], 'a',
        (r'Answer: a. \(f(-1)=1+4+3=8\).', r'Đáp án a. \(f(-1)=1+4+3=8\).')),
   MCQ(3, (r'What are the zeros of \(y=x^2-9\)?', r'Các nghiệm của \(y=x^2-9\) là gì?'), [r'\{3\}', r'\{-3,3\}', r'\{9\}', r'\{0\}'], 'b',
        (r'Answer: b. \(x^2=9\Leftrightarrow x=\pm 3\).', r'Đáp án b. \(x^2=9\Leftrightarrow x=\pm 3\).'))],
  [TF(4, (r'The point \((-2;4)\) is on the graph of \(y=x^2\).', r'Điểm \((-2;4)\) thuộc đồ thị \(y=x^2\).'), 'true', (r'True. \((-2)^2=4\).', r'Đúng. \((-2)^2=4\).'))],
  [SHORT(5, (r'If \(f(x)=3x-5\), find \(f(4)\).', r'Cho \(f(x)=3x-5\). Tính \(f(4)\).'), '7', 'number', ('Enter a number.', 'Nhập một số.'), (r'Answer: 7. \(3\cdot 4-5=7\).', r'Đáp số: 7. \(3\cdot 4-5=7\).')),
   SHORT(6, (r'How many times does the graph of \(y=x^2-4x+4\) meet the x-axis?', r'Đồ thị \(y=x^2-4x+4\) cắt hoặc chạm trục hoành tại bao nhiêu điểm?'), '1', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'),
         (r'Answer: 1. \(y=(x-2)^2\) is 0 only at \(x=2\); the graph touches the axis.', r'Đáp số: 1. \(y=(x-2)^2\) chỉ bằng 0 tại \(x=2\); đồ thị chạm trục hoành.'))]]
S2 = [
  [MCQ(1, (r'What is the domain of \(f(x)=\sqrt{x+3}\)?', r'Tập xác định của \(f(x)=\sqrt{x+3}\) là gì?'), [r'[-3,+\infty)', r'(-3,+\infty)', r'(-\infty,-3]', r'[3,+\infty)'], 'a',
        (r'Answer: a. We need \(x+3\ge 0\), so \(x\ge -3\).', r'Đáp án a. Cần \(x+3\ge 0\) nên \(x\ge -3\).')),
   MCQ(2, (r'If \(f(x)=x^2-2x-5\), what is \(f(-2)\)?', r'Nếu \(f(x)=x^2-2x-5\) thì \(f(-2)\) bằng bao nhiêu?'), ['-5', '3', '13', '-3'], 'b',
        (r'Answer: b. \(f(-2)=4+4-5=3\).', r'Đáp án b. \(f(-2)=4+4-5=3\).')),
   MCQ(3, (r'What are the zeros of \(y=(x-1)(x+5)\)?', r'Các nghiệm của \(y=(x-1)(x+5)\) là gì?'), [r'\{1,5\}', r'\{-1,5\}', r'\{1,-5\}', r'\{-1,-5\}'], 'c',
        (r'Answer: c. A product is 0 when a factor is 0: \(x=1\) or \(x=-5\).', r'Đáp án c. Tích bằng 0 khi một thừa số bằng 0: \(x=1\) hoặc \(x=-5\).'))],
  [TF(4, (r'The point \((-1;2)\) is on the graph of \(y=x^2\).', r'Điểm \((-1;2)\) thuộc đồ thị \(y=x^2\).'), 'false', (r'False. \((-1)^2=1\), not 2.', r'Sai. \((-1)^2=1\), không phải 2.'))],
  [SHORT(5, (r'If \(g(x)=2x^2-3\), find \(g(-3)\).', r'Cho \(g(x)=2x^2-3\). Tính \(g(-3)\).'), '15', 'number', ('Enter a number.', 'Nhập một số.'), (r'Answer: 15. \(2\cdot 9-3=15\).', r'Đáp số: 15. \(2\cdot 9-3=15\).')),
   SHORT(6, (r'How many times does the graph of \(y=x^2+1\) meet the x-axis?', r'Đồ thị \(y=x^2+1\) cắt hoặc chạm trục hoành tại bao nhiêu điểm?'), '0', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'),
         (r'Answer: 0. \(x^2+1\ge 1\), so the graph is always above the axis.', r'Đáp số: 0. \(x^2+1\ge 1\) nên đồ thị luôn nằm trên trục hoành.'))]]
S3 = [
  [MCQ(1, (r'What is the domain of \(f(x)=\dfrac{1}{x-4}\)?', r'Tập xác định của \(f(x)=\dfrac{1}{x-4}\) là gì?'), [r'\mathbb{R}\setminus\{4\}', r'\mathbb{R}\setminus\{-4\}', R, r'(4,+\infty)'], 'a',
        (r'Answer: a. The denominator must not be 0: \(x\ne 4\).', r'Đáp án a. Mẫu phải khác 0: \(x\ne 4\).')),
   MCQ(2, (r'If \(f(x)=-x^2+3x\), what is \(f(-2)\)?', r'Nếu \(f(x)=-x^2+3x\) thì \(f(-2)\) bằng bao nhiêu?'), ['-10', '2', '10', '-2'], 'a',
        (r'Answer: a. \(f(-2)=-4-6=-10\).', r'Đáp án a. \(f(-2)=-4-6=-10\).')),
   MCQ(3, (r'What is the y-coordinate of the y-intercept of \(y=2x^2-5x+7\)?', r'Tung độ giao điểm của \(y=2x^2-5x+7\) với trục tung là bao nhiêu?'), ['7', '-5', '2', '0'], 'a',
        (r'Answer: a. The y-intercept is \((0;f(0))=(0;7)\).', r'Đáp án a. Giao điểm với trục tung là \((0;f(0))=(0;7)\).'))],
  [TF(4, (r'The graph of \(y=|x|\) is symmetric about the y-axis.', r'Đồ thị \(y=|x|\) đối xứng qua trục tung.'), 'true', (r'True. \(|-x|=|x|\), so the point \((-a;b)\) is on the graph whenever \((a;b)\) is.', r'Đúng. \(|-x|=|x|\) nên nếu \((a;b)\) thuộc đồ thị thì \((-a;b)\) cũng thuộc.'))],
  [SHORT(5, (r'If \(h(x)=x^3-2x\), find \(h(2)\).', r'Cho \(h(x)=x^3-2x\). Tính \(h(2)\).'), '4', 'number', ('Enter a number.', 'Nhập một số.'), (r'Answer: 4. \(8-4=4\).', r'Đáp số: 4. \(8-4=4\).')),
   SHORT(6, (r'How many times does the graph of \(y=x^2-2x-3\) meet the x-axis?', r'Đồ thị \(y=x^2-2x-3\) cắt hoặc chạm trục hoành tại bao nhiêu điểm?'), '2', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'),
         (r'Answer: 2. \(x^2-2x-3=(x+1)(x-3)\) has two zeros.', r'Đáp số: 2. \(x^2-2x-3=(x+1)(x-3)\) có hai nghiệm.'))]]
practice = QUIZ_GROUPS = LEVEL_PRACTICE([('A. Multiple Choice', 'A. Trắc nghiệm'), ('B. True or False', 'B. Đúng hoặc sai'), ('C. Short Answer', 'C. Trả lời ngắn')],
                                         {1: S1, 2: S2, 3: S3})

mistakes = [
 (r'<b>Math knowledge.</b> Forgetting a condition when finding the domain, for example writing \(\mathbb{R}\) for \(\dfrac{\sqrt{x-1}}{x-3}\). Check every root and every denominator.', r'<b>Kiến thức Toán.</b> Quên một điều kiện khi tìm [[tập xác định]], chẳng hạn viết \(\mathbb{R}\) cho \(\dfrac{\sqrt{x-1}}{x-3}\). Hãy kiểm tra từng căn và từng mẫu.'),
 (r'<b>Reading graphs.</b> Mixing up the zeros (where \(y=0\)) with the y-intercept (where \(x=0\)).', r'<b>Đọc đồ thị.</b> Nhầm [[nghiệm]] (nơi \(y=0\)) với giao điểm với trục tung (nơi \(x=0\)).'),
 (r'<b>Monotonicity.</b> Writing “increasing on \((-\infty;1)\cup(1;+\infty)\)” when the function falls first and then rises. State each interval separately.', r'<b>Tính đơn điệu.</b> Viết “đồng biến trên \((-\infty;1)\cup(1;+\infty)\)” trong khi hàm giảm rồi mới tăng. Phải nêu riêng từng khoảng.'),
 (r'<b>Drawing.</b> Joining the two branches of a fraction across an asymptote, or the two pieces of a piecewise function across a jump.', r'<b>Vẽ đồ thị.</b> Nối hai nhánh của phân thức qua [[tiệm cận|đường tiệm cận]], hoặc nối hai đoạn của hàm từng đoạn qua chỗ đứt.'),
]
summary = [
 (r'A function gives exactly one \(y\) for each \(x\) in its domain; its graph is the set of points \((x;f(x))\).', r'[[Hàm số]] cho đúng một \(y\) ứng với mỗi \(x\) trong [[tập xác định]]; [[đồ thị]] là tập các điểm \((x;f(x))\).'),
 ('Domain: no zero denominators, no negative numbers under a square root, positive numbers inside a logarithm.', 'Tập xác định: mẫu khác 0, biểu thức dưới căn bậc hai không âm, biểu thức trong logarit dương.'),
 (r'Zeros: \(f(x)=0\). y-intercept: \(f(0)\). Increasing: the graph rises; decreasing: the graph falls.', r'Nghiệm: \(f(x)=0\). Giao điểm với \(Oy\): \(f(0)\). Đồng biến: đồ thị đi lên; nghịch biến: đồ thị đi xuống.'),
 ('A graph never crosses a vertical asymptote and is broken where a piecewise function jumps.', 'Đồ thị không bao giờ cắt tiệm cận đứng và bị đứt tại chỗ hàm từng đoạn nhảy.'),
 ('Key English phrases: state the domain; find the zeros; on which intervals is f increasing; find the range.', 'Cụm tiếng Anh cần nhớ: state the domain (nêu tập xác định); find the zeros (tìm nghiệm); on which intervals is f increasing (đồng biến trên những khoảng nào); find the range (tìm tập giá trị).'),
]
checks = [
 ('I can find the domain of a function with a fraction or a square root.', 'Tôi tìm được tập xác định của hàm có phân thức hoặc căn bậc hai.'),
 ('I can evaluate a function, including a piecewise function.', 'Tôi tính được giá trị hàm số, kể cả hàm từng đoạn.'),
 ('I can read zeros, intercepts, increasing intervals and range from a graph.', 'Tôi đọc được nghiệm, giao điểm, khoảng đồng biến và tập giá trị từ đồ thị.'),
 ('I can use the graph tool to zoom, stretch an axis and move the picture.', 'Tôi dùng được công cụ đồ thị để phóng, giãn trục và di chuyển hình.'),
 STD_SUMMARY_CHECK_EN(),
]

lesson(id=LID, title_en='Graphs of Functions', title_vi='Đồ thị hàm số', topic=TOPIC,
       folder='functions-and-graphs', file='graphs-of-functions',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Read and sketch graphs of functions: domain, intercepts, monotonicity, asymptotes.', level='Intermediate', minutes=50,
       description_vi='Đọc và vẽ đồ thị hàm số: tập xác định, giao điểm với trục, đồng biến – nghịch biến, tiệm cận.',
       tags_vi=['hàm số', 'đồ thị', 'tập xác định', 'giao điểm', 'đồng biến', 'nghịch biến', 'tiệm cận'],
       prerequisites=[], tags=['function', 'graph', 'domain', 'intercept', 'asymptote'], order=10)
