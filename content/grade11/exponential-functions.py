# -*- coding: utf-8 -*-
"""Nội dung bài g11-exp-02 (Hàm số mũ và phương trình mũ) – CHỈ NỘI DUNG."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *

LID = 'g11-exp-02'
CAT = 'Exponential Functions'
TOPIC = (CAT, 'Hàm số mũ')
CV = 'Hàm số mũ'

ensure_vocab([
 ('g11-exp-function', 'exponential function', 'hàm số mũ', CV, 'The graph of an exponential function passes through (0, 1).', r'\(y=a^x\)'),
 ('g11-exponent', 'exponent', 'số mũ', CV, 'In 2^5, the exponent is 5.', ''),
 ('g11-power', 'power', 'lũy thừa', CV, 'Write the number as a power of 2.', ''),
 ('g11-exp-equation', 'exponential equation', 'phương trình mũ', CV, 'Solve the exponential equation.', ''),
 ('g11-substitution-var', 'substitution', 'đặt ẩn phụ', CV, 'Use the substitution t = 2^x.', ''),
 ('g11-positive-only', 'positive', 'dương', CV, 'The base must be positive.', ''),
])
load_vocab()

# ---- kiểm tra số liệu ----
assert 2 ** 3 * 2 ** 2 == 32 and 3 ** 4 // 3 ** 2 == 9 and 2 ** 5 * 2 ** -2 == 8
assert 2 ** (4 + 1) == 32 and 3 ** (2 * 2) == 81 and 3 ** (2 * 2 - 1) == 27 and 4 ** 3 == 64 and 5 ** 3 == 125 and 2 ** 4 == 16 and 3 ** 4 == 81
assert abs(5 ** -2 - 0.04) < 1e-12 and abs(2 ** -3 - 0.125) < 1e-12 and abs(10 ** -2 - 0.01) < 1e-12
assert 4 ** 2 - 3 * 2 ** 2 - 4 == 0 and (2 ** 3) / (2 ** 0) == 8

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 50 minutes', 'khoảng 50 phút'),
            before=('powers with integer exponents, functions and graphs', 'lũy thừa với số mũ nguyên, hàm số và đồ thị'))
goals = [
 (r'state the properties of \(y=a^x\) and sketch its graph;', r'nêu tính chất của \(y=a^x\) và phác họa đồ thị;'),
 ('decide when an exponential function is increasing or decreasing;', 'xác định khi nào [[hàm số mũ]] đồng biến hay nghịch biến;'),
 ('solve exponential equations with the same base;', 'giải [[phương trình mũ]] cùng cơ số;'),
 ('solve simple equations by a substitution.', 'giải phương trình đơn giản bằng cách [[đặt ẩn phụ]].'),
]
vocab = [
 (r'<b>exponential function</b> – a function \(y=a^x\) with \(a\gt 0\) and \(a\ne 1\).', r'[[Hàm số mũ]] – hàm số \(y=a^x\) với \(a\gt 0\) và \(a\ne 1\).'),
 (r'<b>base</b> – the number \(a\) in \(a^x\).', r'[[Cơ số]] – số \(a\) trong \(a^x\).'),
 (r'<b>exponent</b> – the number \(x\) in \(a^x\): it tells how many times we multiply.', r'[[Số mũ]] – số \(x\) trong \(a^x\): cho biết nhân bao nhiêu lần.'),
 ('<b>power</b> – a number written as \\(a^n\\).', '[[Lũy thừa]] – số được viết dưới dạng \\(a^n\\).'),
 ('<b>exponential equation</b> – an equation with the unknown in the exponent.', '[[Phương trình mũ]] – phương trình có ẩn ở số mũ.'),
 ('<b>substitution</b> – replacing an expression by a new letter to simplify an equation.', '[[Đặt ẩn phụ]] – thay một biểu thức bằng chữ mới để đơn giản hóa phương trình.'),
 ('<b>horizontal asymptote</b> – the line \\(y=0\\) that the graph of \\(a^x\\) approaches.', '[[Tiệm cận ngang]] – đường \\(y=0\\) mà đồ thị \\(a^x\\) tiến sát.'),
]
phrases = [
 ('<b>Solve the equation.</b>', 'Giải phương trình.'),
 ('<b>Write both sides as powers of the same base.</b>', 'Viết hai vế thành lũy thừa cùng cơ số.'),
 ('<b>Is the function increasing or decreasing?</b>', 'Hàm số đồng biến hay nghịch biến?'),
 ('<b>Simplify the expression.</b>', 'Rút gọn biểu thức.'),
 ('<b>Use the substitution \\(t=2^x\\).</b>', 'Đặt ẩn phụ \\(t=2^x\\).'),
 ('<b>Find the value of \\(2^{-3}\\).</b>', 'Tìm giá trị của \\(2^{-3}\\).'),
]
review = (
 T(r'<b>Laws of exponents.</b> \(a^m\cdot a^n=a^{m+n}\), \(\dfrac{a^m}{a^n}=a^{m-n}\), \((a^m)^n=a^{mn}\), \(a^{-n}=\dfrac{1}{a^n}\), \(a^0=1\).', r'<b>Quy tắc lũy thừa.</b> \(a^m\cdot a^n=a^{m+n}\), \(\dfrac{a^m}{a^n}=a^{m-n}\), \((a^m)^n=a^{mn}\), \(a^{-n}=\dfrac{1}{a^n}\), \(a^0=1\).') +
 T(r'<b>Quadratic equations.</b> \(t^2-3t-4=0\Leftrightarrow (t-4)(t+1)=0\).', r'<b>Phương trình bậc hai.</b> \(t^2-3t-4=0\Leftrightarrow (t-4)(t+1)=0\).'))

theory = '<h3>5.1 %s</h3>' % TI(r'The function \(y=a^x\)', r'Hàm số \(y=a^x\)')
theory += BOX('mint', ('Definition', 'Định nghĩa'),
  T(r'An <b>exponential function</b> is \(y=a^x\) with base \(a\gt 0\), \(a\ne 1\), defined for every real \(x\).', r'[[Hàm số mũ]] là \(y=a^x\) với [[cơ số]] \(a\gt 0\), \(a\ne 1\), xác định với mọi số thực \(x\).'))
theory += GRAPH({'view': [-4, 4, -1, 9], 'functions': [{'f': '2^x', 'label': 'y = 2ˣ  (a > 1: tăng)'}, {'f': '0.5^x', 'label': 'y = (1/2)ˣ  (0 < a < 1: giảm)'}],
                 'asymptotes': [{'type': 'h', 'y': 0, 'color': '#475569'}], 'mark': {'yint': [0]}},
                cap=('Both graphs pass through (0; 1) and approach the x-axis. They are mirror images in the y-axis.', 'Cả hai đồ thị đều qua (0; 1) và tiến sát trục hoành. Chúng đối xứng với nhau qua trục tung.'),
                alt=('Graphs of 2 to the x and one half to the x', ''), height=340)
theory += TABLE([('Property', 'Tính chất'), (r'\(a\gt 1\)', r'\(a\gt 1\)'), (r'\(0\lt a\lt 1\)', r'\(0\lt a\lt 1\)')], [
  [TI('domain', 'tập xác định'), r'\(\mathbb{R}\)', r'\(\mathbb{R}\)'], [TI('range', 'tập giá trị'), r'\((0;+\infty)\)', r'\((0;+\infty)\)'],
  [TI('monotonicity', 'tính đơn điệu'), TI('increasing', 'đồng biến'), TI('decreasing', 'nghịch biến')],
  [TI('special points', 'điểm đặc biệt'), r'\((0;1)\), \((1;a)\)', r'\((0;1)\), \((1;a)\)'], [TI('asymptote', 'tiệm cận'), r'\(y=0\)', r'\(y=0\)']])
theory += T(r'Try the slider: change the base \(a\) and watch the graph. At \(a=1\) the function is constant, which is why \(a=1\) is not allowed.', r'Thử kéo thanh trượt: đổi cơ số \(a\) và quan sát đồ thị. Tại \(a=1\) hàm số là hằng số, vì thế không cho phép \(a=1\).')
theory += GRAPH({'view': [-4, 4, -1, 9], 'params': [{'name': 'a', 'min': 0.2, 'max': 4, 'value': 2, 'step': 0.05}], 'functions': [{'f': 'a^x', 'label': 'y = aˣ'}]}, alt=('Exponential graph controlled by the base a', ''), height=320)
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T(r'\(a^x\gt 0\) for every \(x\). So an equation such as \(2^x=-4\) has no solution.', r'\(a^x\gt 0\) với mọi \(x\). Vì vậy phương trình như \(2^x=-4\) vô nghiệm.'))

theory += '<h3>5.2 %s</h3>' % TI('Exponential equations', 'Phương trình mũ')
theory += BOX('mint', ('Same base', 'Cùng cơ số'),
  M(r'a^{f(x)}=a^{g(x)}\ \Longleftrightarrow\ f(x)=g(x)\qquad (a\gt 0,\ a\ne 1)'),
  T(r'Write both sides as powers of the same base, then compare the exponents. Because \(a^x\) is one-to-one (either always increasing or always decreasing), no solution is lost.', r'Viết hai vế thành lũy thừa cùng cơ số rồi so sánh số mũ. Vì \(a^x\) luôn đồng biến hoặc luôn nghịch biến nên không mất nghiệm.'))
theory += GRAPH({'view': [-2, 5, -1, 12], 'markRange': [-2, 5], 'functions': [{'f': '2^x', 'label': 'y = 2ˣ'}, {'f': '8', 'label': 'y = 8', 'color': '#c2410c', 'width': 1.8}], 'mark': {'intersections': [[0, 1]]}},
                cap=('The solution of 2ˣ = 8 is the x-coordinate of the intersection point: x = 3.', 'Nghiệm của 2ˣ = 8 là hoành độ giao điểm: x = 3.'), alt=('Graph of 2 to the x meeting the line y = 8', ''), height=320)
theory += BOX('blue', ('Substitution', 'Đặt ẩn phụ'),
  T(r'For \(4^x-3\cdot 2^x-4=0\) put \(t=2^x\gt 0\). Then \(4^x=(2^x)^2=t^2\) and we get an ordinary quadratic equation. Reject any \(t\le 0\).', r'Với \(4^x-3\cdot 2^x-4=0\), đặt \(t=2^x\gt 0\). Khi đó \(4^x=(2^x)^2=t^2\) và ta được phương trình bậc hai. Loại mọi nghiệm \(t\le 0\).'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Simplifying powers', 'Rút gọn lũy thừa'),
  T(r'Simplify \(\dfrac{2^{x+1}}{2^{x-2}}\).', r'Rút gọn \(\dfrac{2^{x+1}}{2^{x-2}}\).'),
  (r'Same base: subtract the exponents.', r'Cùng cơ số: trừ các số mũ.'),
  [T(r'\(\dfrac{2^{x+1}}{2^{x-2}}=2^{(x+1)-(x-2)}\).', r'\(\dfrac{2^{x+1}}{2^{x-2}}=2^{(x+1)-(x-2)}\).'), T(r'\(=2^3=8\).', r'\(=2^3=8\).')], r'\(8\)')
examples += EXAMPLE(2, ('Intermediate', 'Trung bình'), ('Same base', 'Phương trình cùng cơ số'),
  T(r'Solve \(3^{2x-1}=27\).', r'Giải phương trình \(3^{2x-1}=27\).'),
  (r'Write 27 as a power of 3, then compare the exponents.', r'Viết 27 thành lũy thừa của 3 rồi so sánh số mũ.'),
  [T(r'\(27=3^3\), so \(3^{2x-1}=3^3\).', r'\(27=3^3\) nên \(3^{2x-1}=3^3\).'), T(r'\(2x-1=3\Rightarrow x=2\).', r'\(2x-1=3\Rightarrow x=2\).'), T(r'Check: \(3^{2\cdot 2-1}=3^3=27\). ✓', r'Kiểm tra: \(3^{2\cdot 2-1}=3^3=27\). ✓')], r'\(x=2\)')
examples += EXAMPLE(3, ('Advanced', 'Nâng cao'), ('A substitution', 'Dùng ẩn phụ'),
  T(r'Solve \(4^x-3\cdot 2^x-4=0\).', r'Giải phương trình \(4^x-3\cdot 2^x-4=0\).'),
  (r'Notice that \(4^x=(2^x)^2\). Put \(t=2^x\) with \(t\gt 0\).', r'Chú ý \(4^x=(2^x)^2\). Đặt \(t=2^x\) với \(t\gt 0\).'),
  [T(r'The equation becomes \(t^2-3t-4=0\), that is \((t-4)(t+1)=0\).', r'Phương trình thành \(t^2-3t-4=0\), tức là \((t-4)(t+1)=0\).'),
   T(r'\(t=4\) or \(t=-1\). Reject \(t=-1\) because \(t\gt 0\).', r'\(t=4\) hoặc \(t=-1\). Loại \(t=-1\) vì \(t\gt 0\).'),
   T(r'\(2^x=4\Rightarrow x=2\). Check: \(16-12-4=0\). ✓', r'\(2^x=4\Rightarrow x=2\). Kiểm tra: \(16-12-4=0\). ✓')], r'\(x=2\)')

INC = TI('increasing', 'đồng biến'); DEC = TI('decreasing', 'nghịch biến'); CON = TI('constant', 'không đổi'); NEI = TI('neither', 'không đơn điệu')
# A1 tính lũy thừa; A2 đồng biến/nghịch biến; A3 phương trình cùng cơ số; B nhận định về đồ thị; C5 phương trình mũ; C6 lũy thừa số mũ âm
S1 = [
  [MCQ(1, (r'Calculate \(2^3\cdot 2^2\).', r'Tính \(2^3\cdot 2^2\).'), ['10', '32', '64', '25'], 'b', (r'Answer: b. \(2^{3+2}=2^5=32\).', r'Đáp án b. \(2^{3+2}=2^5=32\).')),
   MCQ(2, (r'Is \(y=2^x\) increasing or decreasing?', r'Hàm số \(y=2^x\) đồng biến hay nghịch biến?'), [INC, DEC, CON, NEI], 'a', (r'Answer: a. The base \(2\gt 1\).', r'Đáp án a. Cơ số \(2\gt 1\).'), raw=True),
   MCQ(3, (r'Solve \(2^x=16\).', r'Giải phương trình \(2^x=16\).'), ['x=2', 'x=3', 'x=4', 'x=8'], 'c', (r'Answer: c. \(16=2^4\).', r'Đáp án c. \(16=2^4\).'))],
  [TF(4, (r'The range of \(y=3^x\) is \(\mathbb{R}\).', r'Tập giá trị của \(y=3^x\) là \(\mathbb{R}\).'), 'false', (r'False. \(3^x\gt 0\), so the range is \((0;+\infty)\).', r'Sai. \(3^x\gt 0\) nên tập giá trị là \((0;+\infty)\).'))],
  [SHORT(5, (r'Solve \(3^x=81\).', r'Giải phương trình \(3^x=81\).'), '4', 'number', ('Enter a number.', 'Nhập một số.'), (r'Answer: 4. \(81=3^4\).', r'Đáp số: 4. \(81=3^4\).')),
   SHORT(6, (r'Find the value of \(5^{-2}\).', r'Tìm giá trị của \(5^{-2}\).'), '1/25|0.04', 'number', ('Enter a fraction or a decimal.', 'Nhập phân số hoặc số thập phân.'), (r'Answer: \(\dfrac1{25}=0.04\).', r'Đáp số: \(\dfrac1{25}=0{,}04\).'))]]
S2 = [
  [MCQ(1, (r'Calculate \(\dfrac{3^4}{3^2}\).', r'Tính \(\dfrac{3^4}{3^2}\).'), ['3', '6', '9', '27'], 'c', (r'Answer: c. \(3^{4-2}=3^2=9\).', r'Đáp án c. \(3^{4-2}=3^2=9\).')),
   MCQ(2, (r'Is \(y=\left(\dfrac13\right)^x\) increasing or decreasing?', r'Hàm số \(y=\left(\dfrac13\right)^x\) đồng biến hay nghịch biến?'), [INC, DEC, CON, NEI], 'b', (r'Answer: b. The base \(\dfrac13\) is between 0 and 1.', r'Đáp án b. Cơ số \(\dfrac13\) nằm giữa 0 và 1.'), raw=True),
   MCQ(3, (r'Solve \(5^x=125\).', r'Giải phương trình \(5^x=125\).'), ['x=2', 'x=3', 'x=5', 'x=25'], 'b', (r'Answer: b. \(125=5^3\).', r'Đáp án b. \(125=5^3\).'))],
  [TF(4, (r'The graph of \(y=\left(\dfrac12\right)^x\) has the horizontal asymptote \(y=0\).', r'Đồ thị \(y=\left(\dfrac12\right)^x\) có tiệm cận ngang \(y=0\).'), 'true', (r'True. When \(x\to+\infty\) the values approach 0.', r'Đúng. Khi \(x\to+\infty\) giá trị tiến sát 0.'))],
  [SHORT(5, (r'Solve \(2^{x+1}=32\).', r'Giải phương trình \(2^{x+1}=32\).'), '4', 'number', ('Enter a number.', 'Nhập một số.'), (r'Answer: 4. \(x+1=5\).', r'Đáp số: 4. \(x+1=5\).')),
   SHORT(6, (r'Find the value of \(2^{-3}\).', r'Tìm giá trị của \(2^{-3}\).'), '1/8|0.125', 'number', ('Enter a fraction or a decimal.', 'Nhập phân số hoặc số thập phân.'), (r'Answer: \(\dfrac18=0.125\).', r'Đáp số: \(\dfrac18=0{,}125\).'))]]
S3 = [
  [MCQ(1, (r'Calculate \(2^5\cdot 2^{-2}\).', r'Tính \(2^5\cdot 2^{-2}\).'), ['8', '32', '16', '4'], 'a', (r'Answer: a. \(2^{5-2}=2^3=8\).', r'Đáp án a. \(2^{5-2}=2^3=8\).')),
   MCQ(2, (r'Is \(y=0.5^x\) increasing or decreasing?', r'Hàm số \(y=0.5^x\) đồng biến hay nghịch biến?'), [INC, DEC, CON, NEI], 'b', (r'Answer: b. The base 0.5 is between 0 and 1.', r'Đáp án b. Cơ số 0,5 nằm giữa 0 và 1.'), raw=True),
   MCQ(3, (r'Solve \(4^x=64\).', r'Giải phương trình \(4^x=64\).'), ['x=3', 'x=4', 'x=6', 'x=16'], 'a', (r'Answer: a. \(64=4^3\).', r'Đáp án a. \(64=4^3\).'))],
  [TF(4, (r'The graph of \(y=3^x\) meets the x-axis.', r'Đồ thị \(y=3^x\) cắt trục hoành.'), 'false', (r'False. \(3^x\gt 0\) for every \(x\), so the graph stays above the axis.', r'Sai. \(3^x\gt 0\) với mọi \(x\) nên đồ thị luôn nằm trên trục hoành.'))],
  [SHORT(5, (r'Solve \(3^{2x}=81\).', r'Giải phương trình \(3^{2x}=81\).'), '2', 'number', ('Enter a number.', 'Nhập một số.'), (r'Answer: 2. \(81=3^4\), so \(2x=4\).', r'Đáp số: 2. \(81=3^4\) nên \(2x=4\).')),
   SHORT(6, (r'Find the value of \(10^{-2}\).', r'Tìm giá trị của \(10^{-2}\).'), '0.01|1/100', 'number', ('Enter a fraction or a decimal.', 'Nhập phân số hoặc số thập phân.'), (r'Answer: \(\dfrac1{100}=0.01\).', r'Đáp số: \(\dfrac1{100}=0{,}01\).'))]]
practice = LEVEL_PRACTICE([('A. Multiple Choice', 'A. Trắc nghiệm'), ('B. True or False', 'B. Đúng hoặc sai'), ('C. Short Answer', 'C. Trả lời ngắn')], {1: S1, 2: S2, 3: S3})

mistakes = [
 (r'<b>Math knowledge.</b> Thinking that \(a^x\) can be negative or 0. Always \(a^x\gt 0\).', r'<b>Kiến thức Toán.</b> Cho rằng \(a^x\) có thể âm hoặc bằng 0. Luôn có \(a^x\gt 0\).'),
 (r'<b>Using formulas.</b> Writing \(2^3\cdot 2^2=4^5\) or \(2^3\cdot 2^2=2^6\). Correct: add the exponents: \(2^5\).', r'<b>Dùng công thức.</b> Viết \(2^3\cdot 2^2=4^5\) hoặc \(2^6\). Đúng: cộng số mũ: \(2^5\).'),
 (r'<b>Monotonicity.</b> Saying \(y=\left(\dfrac12\right)^x\) is increasing because \(x\) increases. The base is less than 1, so it decreases.', r'<b>Tính đơn điệu.</b> Cho rằng \(y=\left(\dfrac12\right)^x\) đồng biến vì \(x\) tăng. Cơ số nhỏ hơn 1 nên hàm nghịch biến.'),
 (r'<b>Substitution.</b> Keeping \(t=-1\) as a solution. Since \(t=2^x\gt 0\), it must be rejected.', r'<b>Đặt ẩn phụ.</b> Giữ nghiệm \(t=-1\). Vì \(t=2^x\gt 0\) nên phải loại.'),
]
summary = [
 (r'\(y=a^x\) (\(a\gt 0\), \(a\ne 1\)): domain \(\mathbb{R}\), range \((0;+\infty)\), passes through \((0;1)\), asymptote \(y=0\).', r'\(y=a^x\) (\(a\gt 0\), \(a\ne 1\)): tập xác định \(\mathbb{R}\), tập giá trị \((0;+\infty)\), đi qua \((0;1)\), tiệm cận \(y=0\).'),
 (r'Increasing if \(a\gt 1\); decreasing if \(0\lt a\lt 1\).', r'Đồng biến nếu \(a\gt 1\); nghịch biến nếu \(0\lt a\lt 1\).'),
 (r'\(a^{f(x)}=a^{g(x)}\Leftrightarrow f(x)=g(x)\).', r'\(a^{f(x)}=a^{g(x)}\Leftrightarrow f(x)=g(x)\).'),
 (r'For \(4^x-3\cdot 2^x-4=0\) substitute \(t=2^x\gt 0\).', r'Với \(4^x-3\cdot 2^x-4=0\) đặt \(t=2^x\gt 0\).'),
 ('Key English phrases: solve the equation; same base; increasing or decreasing; use the substitution.', 'Cụm tiếng Anh cần nhớ: solve the equation (giải phương trình); same base (cùng cơ số); increasing or decreasing (đồng biến hay nghịch biến); use the substitution (đặt ẩn phụ).'),
]
checks = [
 ('I can state the properties of an exponential function.', 'Tôi nêu được tính chất của hàm số mũ.'),
 ('I can decide if y = a^x is increasing or decreasing.', 'Tôi xác định được y = a^x đồng biến hay nghịch biến.'),
 ('I can solve an exponential equation with the same base.', 'Tôi giải được phương trình mũ cùng cơ số.'),
 ('I can solve an equation by a substitution and reject t ≤ 0.', 'Tôi giải được phương trình bằng ẩn phụ và loại t ≤ 0.'),
 STD_SUMMARY_CHECK_EN(),
]

lesson(id=LID, title_en='Exponential Functions and Equations', title_vi='Hàm số mũ và phương trình mũ', topic=TOPIC,
       folder='exponential-functions', file='exponential-functions-and-equations',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Graphs and properties of y = a^x and solving exponential equations.', level='Intermediate', minutes=50,
       description_vi='Đồ thị và tính chất của hàm số y = a^x, giải phương trình mũ.',
       tags_vi=['hàm số mũ', 'phương trình mũ', 'lũy thừa', 'cơ số', 'đồng biến', 'nghịch biến'],
       prerequisites=['g11-functions-01'], tags=['exponential function', 'exponential equation', 'power', 'base'], order=60)
