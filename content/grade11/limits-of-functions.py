# -*- coding: utf-8 -*-
"""Nội dung bài g11-limits-02 (Giới hạn của hàm số) – CHỈ NỘI DUNG."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *

LID = 'g11-limits-02'
CAT = 'Limits'
TOPIC = (CAT, 'Giới hạn')
CV = 'Giới hạn'

ensure_vocab([
 ('g11-approaches', 'approaches', 'tiến tới', CV, 'x approaches 2.', r'\(x\to 2\)'),
 ('g11-left-limit', 'left-hand limit', 'giới hạn bên trái', CV, 'Find the left-hand limit at 1.', r'\(\lim_{x\to a^-}\)'),
 ('g11-right-limit', 'right-hand limit', 'giới hạn bên phải', CV, 'Find the right-hand limit at 1.', r'\(\lim_{x\to a^+}\)'),
 ('g11-one-sided', 'one-sided limit', 'giới hạn một bên', CV, 'A one-sided limit looks from one side only.', ''),
 ('g11-infinity', 'infinity', 'vô cực', CV, 'x tends to plus infinity.', r'\(\infty\)'),
 ('g11-direct-subst', 'substitution', 'thay trực tiếp', CV, 'Use direct substitution.', ''),
 ('g11-factor', 'factor', 'phân tích thành nhân tử', CV, 'Factor the numerator.', ''),
 ('g11-discontinuity', 'discontinuity', 'điểm gián đoạn', CV, 'The graph has a discontinuity at x = 1.', ''),
])
load_vocab()

# ---- kiểm tra số liệu bằng số ----
def lim(f, a, side=0):
    h = 1e-7
    xs = [a + h] if side > 0 else [a - h] if side < 0 else [a - h, a + h]
    return [f(x) for x in xs]
assert all(abs(v - 6) < 1e-5 for v in lim(lambda x: (x * x - 9) / (x - 3), 3))
assert all(abs(v - 4) < 1e-5 for v in lim(lambda x: (x * x - 4) / (x - 2), 2))
assert abs((3 * 1e8 ** 2 + 1) / (1e8 ** 2 - 2) - 3) < 1e-6
assert all(abs(v - 2) < 1e-5 for v in lim(lambda x: (x * x - 1) / (x - 1), 1)) and all(abs(v + 6) < 1e-5 for v in lim(lambda x: (x * x - 9) / (x + 3), -3))
assert all(abs(v + 4) < 1e-5 for v in lim(lambda x: (x * x - 4) / (x + 2), -2)) and all(abs(v - 10) < 1e-5 for v in lim(lambda x: (x * x - 25) / (x - 5), 5))
assert abs((2e9 + 1) / (1e9 + 3) - 2) < 1e-6 and abs((3 * 1e8 ** 2 + 1) / (1e8 ** 2 + 5) - 3) < 1e-6
assert lim(lambda x: (x + 1) / (x - 2), 2, +1)[0] > 1e6 and lim(lambda x: (x + 1) / (x - 2), 2, -1)[0] < -1e6
assert lim(lambda x: abs(x) / x, 0, +1)[0] == 1 and lim(lambda x: abs(x) / x, 0, -1)[0] == -1

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 55 minutes', 'khoảng 55 phút'),
            before=('functions and graphs, factoring, fractions (previous lessons)', 'hàm số và đồ thị, phân tích đa thức, phân thức (các bài trước)'))
goals = [
 (r'understand \(\lim_{x\to a}f(x)=L\) and one-sided limits from a graph;', r'hiểu \(\lim_{x\to a}f(x)=L\) và [[giới hạn một bên]] qua đồ thị;'),
 ('compute limits by substitution and by factoring;', 'tính giới hạn bằng cách [[thay trực tiếp]] và [[phân tích thành nhân tử]];'),
 ('find limits at infinity of rational functions;', 'tìm giới hạn tại [[vô cực]] của hàm phân thức;'),
 ('connect limits with vertical and horizontal asymptotes.', 'liên hệ giới hạn với [[tiệm cận đứng]] và [[tiệm cận ngang]].'),
]
vocab = [
 (r'<b>limit</b> – the value that \(f(x)\) gets close to when \(x\) gets close to \(a\).', r'[[Giới hạn]] – giá trị mà \(f(x)\) tiến sát khi \(x\) tiến sát \(a\).'),
 (r'<b>approaches</b> – gets closer and closer to: \(x\to a\).', r'[[Tiến tới]] – ngày càng gần: \(x\to a\).'),
 (r'<b>left-hand limit</b> – the limit when \(x\) approaches \(a\) from the left: \(x\to a^-\).', r'[[Giới hạn bên trái]] – giới hạn khi \(x\) tiến tới \(a\) từ phía bên trái: \(x\to a^-\).'),
 (r'<b>right-hand limit</b> – the limit when \(x\) approaches \(a\) from the right: \(x\to a^+\).', r'[[Giới hạn bên phải]] – giới hạn khi \(x\) tiến tới \(a\) từ phía bên phải: \(x\to a^+\).'),
 ('<b>infinity</b> – not a number; it means that the values grow without end.', '[[Vô cực]] – không phải một số; nghĩa là giá trị tăng mãi không dừng.'),
 ('<b>substitution</b> – replacing \\(x\\) by the number \\(a\\).', '[[Thay trực tiếp]] – thay \\(x\\) bằng số \\(a\\).'),
 ('<b>factor</b> – write an expression as a product.', '[[Phân tích thành nhân tử]] – viết biểu thức thành tích.'),
 ('<b>discontinuity</b> – a point where the graph has a hole, a jump or an asymptote.', '[[Điểm gián đoạn]] – điểm mà đồ thị có lỗ thủng, chỗ đứt hoặc tiệm cận.'),
]
phrases = [
 ('<b>Find the limit.</b>', 'Tìm giới hạn.'),
 ('<b>Evaluate \\(\\lim_{x\\to 3}\\dfrac{x^2-9}{x-3}\\).</b>', 'Tính \\(\\lim_{x\\to 3}\\dfrac{x^2-9}{x-3}\\).'),
 ('<b>Find the left-hand and the right-hand limits.</b>', 'Tìm giới hạn bên trái và giới hạn bên phải.'),
 ('<b>The limit does not exist.</b>', 'Giới hạn không tồn tại.'),
 ('<b>Find the limit as \\(x\\) tends to infinity.</b>', 'Tìm giới hạn khi \\(x\\) tiến tới vô cực.'),
 ('<b>Find the equations of the asymptotes.</b>', 'Tìm phương trình các đường tiệm cận.'),
]
review = (
 T(r'<b>Factoring.</b> \(x^2-9=(x-3)(x+3)\) and \(x^2-4=(x-2)(x+2)\) (difference of two squares).', r'<b>Phân tích đa thức.</b> \(x^2-9=(x-3)(x+3)\) và \(x^2-4=(x-2)(x+2)\) (hiệu hai bình phương).') +
 T(r'<b>Cancelling.</b> For \(x\ne 3\): \(\dfrac{(x-3)(x+3)}{x-3}=x+3\).', r'<b>Rút gọn.</b> Với \(x\ne 3\): \(\dfrac{(x-3)(x+3)}{x-3}=x+3\).') +
 T(r'<b>Big numbers.</b> If \(x\) is very large, then \(\dfrac1x\) is very close to 0.', r'<b>Số rất lớn.</b> Nếu \(x\) rất lớn thì \(\dfrac1x\) rất gần 0.'))

theory = '<h3>5.1 %s</h3>' % TI('The idea of a limit', 'Ý tưởng về giới hạn')
theory += BOX('mint', ('Definition (informal)', 'Định nghĩa (trực quan)'),
  T(r'We write \(\lim_{x\to a}f(x)=L\) if \(f(x)\) gets as close to \(L\) as we want when \(x\) gets close enough to \(a\) (\(x\ne a\)). The value \(f(a)\) is not needed.',
    r'Viết \(\lim_{x\to a}f(x)=L\) nếu \(f(x)\) tiến sát \(L\) tùy ý khi \(x\) đủ gần \(a\) (\(x\ne a\)). Không cần biết \(f(a)\).'),
  T(r'The limit exists exactly when the left-hand limit and the right-hand limit exist and are equal.', r'[[Giới hạn]] tồn tại đúng khi [[giới hạn bên trái]] và [[giới hạn bên phải]] tồn tại và bằng nhau.'))
theory += GRAPH({'view': [-2, 6, -2, 8], 'functions': [{'f': '(x^2-4)/(x-2)', 'label': 'f(x) = (x² − 4)/(x − 2)'}], 'holes': [[2, 4, '(2; 4)']], 'guides': [{'type': 'h', 'y': 4}]},
                cap=('f(2) is not defined (hole), but f(x) gets close to 4 on both sides: the limit is 4.', 'f(2) không xác định (lỗ thủng), nhưng f(x) tiến sát 4 ở cả hai phía: giới hạn bằng 4.'),
                alt=('Graph with a hole at the point (2; 4)', ''), height=320)
theory += GRAPH({'view': [-3, 6, -6, 6], 'functions': [{'f': '2x+1', 'domain': [-3, 1], 'open': [False, False], 'label': 'y = 2x + 1  (x ≤ 1)'}, {'f': '5-x', 'domain': [1, 6], 'open': [True, False], 'color': '#c2410c', 'label': 'y = 5 − x  (x > 1)'}]},
                cap=('The left-hand limit at 1 is 3 and the right-hand limit is 4. They are different, so the limit does not exist.', 'Giới hạn bên trái tại 1 là 3, bên phải là 4. Hai số khác nhau nên giới hạn không tồn tại.'),
                alt=('Piecewise graph with a jump at x = 1', ''), height=300)

theory += '<h3>5.2 %s</h3>' % TI('Computing limits', 'Cách tính giới hạn')
theory += BOX('mint', ('Limit laws', 'Quy tắc giới hạn'),
  M(r'\lim(f\pm g)=\lim f\pm\lim g,\quad \lim(f\cdot g)=\lim f\cdot\lim g,\quad \lim\dfrac{f}{g}=\dfrac{\lim f}{\lim g}\ \ (\lim g\ne 0)'),
  T(r'For polynomials, <b>substitution</b> gives the limit: \(\lim_{x\to a}P(x)=P(a)\).', r'Với đa thức, [[thay trực tiếp]] cho ra giới hạn: \(\lim_{x\to a}P(x)=P(a)\).'))
theory += BOX('blue', ('Form 0/0: factor and cancel', 'Dạng 0/0: phân tích và rút gọn'),
  T(r'If substitution gives \(\dfrac00\), factor the numerator and the denominator, cancel the common factor \((x-a)\), then substitute again.', r'Nếu thay trực tiếp được \(\dfrac00\), hãy [[phân tích thành nhân tử]] tử và mẫu, rút gọn thừa số chung \((x-a)\), rồi thay lại.'))

theory += '<h3>5.3 %s</h3>' % TI('Infinite limits and asymptotes', 'Giới hạn vô cực và tiệm cận')
theory += GRAPH({'view': [-6, 8, -8, 10], 'functions': [{'f': '(x+1)/(x-2)', 'label': 'y = (x + 1)/(x − 2)'}], 'asymptotes': [{'type': 'v', 'x': 2}, {'type': 'h', 'y': 1}]},
                cap=('Near x = 2 the values go to +∞ on the right and to −∞ on the left. Far away the graph approaches y = 1.', 'Gần x = 2, giá trị tiến tới +∞ bên phải và −∞ bên trái. Ở xa, đồ thị tiến sát y = 1.'),
                alt=('Hyperbola with vertical asymptote x = 2 and horizontal asymptote y = 1', ''), height=340)
theory += BOX('mint', ('Asymptotes from limits', 'Tiệm cận từ giới hạn'),
  T(r'If \(\lim_{x\to a^\pm}f(x)=\pm\infty\), the line \(x=a\) is a <b>vertical asymptote</b>. If \(\lim_{x\to\pm\infty}f(x)=b\), the line \(y=b\) is a <b>horizontal asymptote</b>.',
    r'Nếu \(\lim_{x\to a^\pm}f(x)=\pm\infty\) thì \(x=a\) là [[tiệm cận đứng]]. Nếu \(\lim_{x\to\pm\infty}f(x)=b\) thì \(y=b\) là [[tiệm cận ngang]].'))

theory += '<h3>5.4 %s</h3>' % TI('Limits at infinity of rational functions', 'Giới hạn tại vô cực của hàm phân thức')
theory += T(r'Divide the numerator and the denominator by the highest power of \(x\). Compare the degrees: if the degrees are equal, the limit is the ratio of the leading coefficients; if the numerator has the smaller degree, the limit is 0.',
            r'Chia tử và mẫu cho lũy thừa cao nhất của \(x\). So sánh bậc: nếu bậc bằng nhau, giới hạn bằng tỉ số hai hệ số cao nhất; nếu bậc tử nhỏ hơn bậc mẫu, giới hạn bằng 0.')
theory += GRAPH({'view': [-8, 8, -6, 12], 'functions': [{'f': '(3x^2+1)/(x^2-2)', 'label': 'y = (3x² + 1)/(x² − 2)'}],
                 'asymptotes': [{'type': 'h', 'y': 3}, {'type': 'v', 'x': math.sqrt(2)}, {'type': 'v', 'x': -math.sqrt(2)}]},
                cap=('The graph approaches y = 3 when x → ±∞.', 'Đồ thị tiến sát y = 3 khi x → ±∞.'), alt=('Rational function approaching the horizontal asymptote y = 3', ''), height=340)

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('The form 0/0', 'Dạng 0/0'),
  T(r'Find \(\lim_{x\to 3}\dfrac{x^2-9}{x-3}\).', r'Tìm \(\lim_{x\to 3}\dfrac{x^2-9}{x-3}\).'),
  (r'Substituting \(x=3\) gives \(\dfrac00\), so we factor.', r'Thay \(x=3\) được \(\dfrac00\) nên ta phân tích thành nhân tử.'),
  [T(r'\(x^2-9=(x-3)(x+3)\).', r'\(x^2-9=(x-3)(x+3)\).'), T(r'For \(x\ne 3\): \(\dfrac{x^2-9}{x-3}=x+3\).', r'Với \(x\ne 3\): \(\dfrac{x^2-9}{x-3}=x+3\).'), T(r'\(\lim_{x\to 3}(x+3)=6\).', r'\(\lim_{x\to 3}(x+3)=6\).')], r'\(6\)')
examples += EXAMPLE(2, ('Intermediate', 'Trung bình'), ('Limit at infinity', 'Giới hạn tại vô cực'),
  T(r'Find \(\lim_{x\to+\infty}\dfrac{3x^2+1}{x^2-2}\).', r'Tìm \(\lim_{x\to+\infty}\dfrac{3x^2+1}{x^2-2}\).'),
  (r'The highest power is \(x^2\). Divide the numerator and the denominator by \(x^2\).', r'Lũy thừa cao nhất là \(x^2\). Chia tử và mẫu cho \(x^2\).'),
  [T(r'\(\dfrac{3x^2+1}{x^2-2}=\dfrac{3+\frac{1}{x^2}}{1-\frac{2}{x^2}}\).', r'\(\dfrac{3x^2+1}{x^2-2}=\dfrac{3+\frac{1}{x^2}}{1-\frac{2}{x^2}}\).'), T(r'When \(x\to+\infty\): \(\dfrac1{x^2}\to 0\), so the limit is \(\dfrac{3+0}{1-0}=3\).', r'Khi \(x\to+\infty\): \(\dfrac1{x^2}\to 0\) nên giới hạn là \(\dfrac{3+0}{1-0}=3\).')],
  TI(r'\(3\) (so \(y=3\) is a horizontal asymptote).', r'\(3\) (nên \(y=3\) là tiệm cận ngang).'))
examples += EXAMPLE(3, ('Advanced', 'Nâng cao'), ('One-sided limits and asymptotes', 'Giới hạn một bên và tiệm cận'),
  T(r'For \(f(x)=\dfrac{x+1}{x-2}\), find \(\lim_{x\to 2^+}f(x)\), \(\lim_{x\to 2^-}f(x)\), \(\lim_{x\to\pm\infty}f(x)\) and the asymptotes (see the figure in 5.3).', r'Với \(f(x)=\dfrac{x+1}{x-2}\), tìm \(\lim_{x\to 2^+}f(x)\), \(\lim_{x\to 2^-}f(x)\), \(\lim_{x\to\pm\infty}f(x)\) và các tiệm cận (xem hình ở mục 5.3).'),
  (r'Near \(x=2\) the numerator is close to 3 and the denominator is close to 0. Look at the sign of the denominator on each side.', r'Gần \(x=2\), tử gần 3 còn mẫu gần 0. Hãy xét dấu của mẫu ở mỗi phía.'),
  [T(r'\(x\to 2^+\): \(x-2\gt 0\) is tiny, \(x+1\approx 3\), so \(f(x)\to+\infty\).', r'\(x\to 2^+\): \(x-2\gt 0\) rất nhỏ, \(x+1\approx 3\) nên \(f(x)\to+\infty\).'),
   T(r'\(x\to 2^-\): \(x-2\lt 0\) is tiny, so \(f(x)\to-\infty\). The two one-sided limits are different.', r'\(x\to 2^-\): \(x-2\lt 0\) rất nhỏ nên \(f(x)\to-\infty\). Hai giới hạn một bên khác nhau.'),
   T(r'Divide by \(x\): \(f(x)=\dfrac{1+1/x}{1-2/x}\to 1\) when \(x\to\pm\infty\).', r'Chia cho \(x\): \(f(x)=\dfrac{1+1/x}{1-2/x}\to 1\) khi \(x\to\pm\infty\).')],
  TI(r'\(+\infty\), \(-\infty\), \(1\); vertical asymptote \(x=2\), horizontal asymptote \(y=1\).', r'\(+\infty\), \(-\infty\), \(1\); tiệm cận đứng \(x=2\), tiệm cận ngang \(y=1\).'))

# A1 thay trực tiếp; A2 dạng 0/0; A3 giới hạn tại vô cực; B nhận định; C5 thay trực tiếp; C6 dạng 0/0
S1 = [
  [MCQ(1, (r'Find \(\lim_{x\to 2}(x^2+3x)\).', r'Tìm \(\lim_{x\to 2}(x^2+3x)\).'), ['10', '6', '8', '12'], 'a', (r'Answer: a. Substitute: \(4+6=10\).', r'Đáp án a. Thay trực tiếp: \(4+6=10\).')),
   MCQ(2, (r'Find \(\lim_{x\to 1}\dfrac{x^2-1}{x-1}\).', r'Tìm \(\lim_{x\to 1}\dfrac{x^2-1}{x-1}\).'), [r'\(0\)', r'\(1\)', r'\(2\)', TI('does not exist', 'không tồn tại')], 'c', (r'Answer: c. \(\dfrac{x^2-1}{x-1}=x+1\to 2\).', r'Đáp án c. \(\dfrac{x^2-1}{x-1}=x+1\to 2\).'), raw=True),
   MCQ(3, (r'Find \(\lim_{x\to+\infty}\dfrac1x\).', r'Tìm \(\lim_{x\to+\infty}\dfrac1x\).'), ['0', '1', r'+\infty', r'-\infty'], 'a', (r'Answer: a. For very large \(x\), \(\dfrac1x\) is close to 0.', r'Đáp án a. Với \(x\) rất lớn, \(\dfrac1x\) rất gần 0.'))],
  [TF(4, (r'\(\lim_{x\to 0}\dfrac1x=+\infty\).', r'\(\lim_{x\to 0}\dfrac1x=+\infty\).'), 'false', (r'False. On the right the values go to \(+\infty\), on the left to \(-\infty\). The limit does not exist.', r'Sai. Bên phải giá trị tiến tới \(+\infty\), bên trái tiến tới \(-\infty\). Giới hạn không tồn tại.'))],
  [SHORT(5, (r'Find \(\lim_{x\to -1}(2x+5)\).', r'Tìm \(\lim_{x\to -1}(2x+5)\).'), '3', 'number', ('Enter a number.', 'Nhập một số.'), (r'Answer: 3. \(2\cdot(-1)+5=3\).', r'Đáp số: 3. \(2\cdot(-1)+5=3\).')),
   SHORT(6, (r'Find \(\lim_{x\to 3}\dfrac{x^2-9}{x-3}\).', r'Tìm \(\lim_{x\to 3}\dfrac{x^2-9}{x-3}\).'), '6', 'number', ('Enter a number.', 'Nhập một số.'), (r'Answer: 6. \(x+3\to 6\).', r'Đáp số: 6. \(x+3\to 6\).'))]]
S2 = [
  [MCQ(1, (r'Find \(\lim_{x\to -1}(x^2-4x)\).', r'Tìm \(\lim_{x\to -1}(x^2-4x)\).'), ['3', '5', '-5', '-3'], 'b', (r'Answer: b. \(1+4=5\).', r'Đáp án b. \(1+4=5\).')),
   MCQ(2, (r'Find \(\lim_{x\to 2}\dfrac{x^2-4}{x-2}\).', r'Tìm \(\lim_{x\to 2}\dfrac{x^2-4}{x-2}\).'), [r'\(0\)', r'\(2\)', r'\(4\)', TI('does not exist', 'không tồn tại')], 'c', (r'Answer: c. \(x+2\to 4\).', r'Đáp án c. \(x+2\to 4\).'), raw=True),
   MCQ(3, (r'Find \(\lim_{x\to+\infty}\dfrac{2x+1}{x+3}\).', r'Tìm \(\lim_{x\to+\infty}\dfrac{2x+1}{x+3}\).'), ['1', '2', '3', r'+\infty'], 'b', (r'Answer: b. Divide by \(x\): \(\dfrac{2+1/x}{1+3/x}\to 2\).', r'Đáp án b. Chia cho \(x\): \(\dfrac{2+1/x}{1+3/x}\to 2\).'))],
  [TF(4, (r'\(\lim_{x\to 0}\dfrac{|x|}{x}=1\).', r'\(\lim_{x\to 0}\dfrac{|x|}{x}=1\).'), 'false', (r'False. On the right the quotient is 1, on the left it is \(-1\). The limit does not exist.', r'Sai. Bên phải thương bằng 1, bên trái bằng \(-1\). Giới hạn không tồn tại.'))],
  [SHORT(5, (r'Find \(\lim_{x\to 4}(3x-2)\).', r'Tìm \(\lim_{x\to 4}(3x-2)\).'), '10', 'number', ('Enter a number.', 'Nhập một số.'), (r'Answer: 10. \(12-2=10\).', r'Đáp số: 10. \(12-2=10\).')),
   SHORT(6, (r'Find \(\lim_{x\to -2}\dfrac{x^2-4}{x+2}\).', r'Tìm \(\lim_{x\to -2}\dfrac{x^2-4}{x+2}\).'), '-4', 'number', ('Enter a number.', 'Nhập một số.'), (r'Answer: \(-4\). \(x-2\to -4\).', r'Đáp số: \(-4\). \(x-2\to -4\).'))]]
S3 = [
  [MCQ(1, (r'Find \(\lim_{x\to 3}(x^2-2x)\).', r'Tìm \(\lim_{x\to 3}(x^2-2x)\).'), ['3', '0', '15', '-3'], 'a', (r'Answer: a. \(9-6=3\).', r'Đáp án a. \(9-6=3\).')),
   MCQ(2, (r'Find \(\lim_{x\to -3}\dfrac{x^2-9}{x+3}\).', r'Tìm \(\lim_{x\to -3}\dfrac{x^2-9}{x+3}\).'), [r'\(-6\)', r'\(6\)', r'\(0\)', TI('does not exist', 'không tồn tại')], 'a', (r'Answer: a. \(x-3\to -6\).', r'Đáp án a. \(x-3\to -6\).'), raw=True),
   MCQ(3, (r'Find \(\lim_{x\to-\infty}\dfrac{3x^2+1}{x^2+5}\).', r'Tìm \(\lim_{x\to-\infty}\dfrac{3x^2+1}{x^2+5}\).'), ['0', '1', '3', r'+\infty'], 'c', (r'Answer: c. The degrees are equal: \(\dfrac31=3\).', r'Đáp án c. Hai bậc bằng nhau: \(\dfrac31=3\).'))],
  [TF(4, (r'If \(f(a)\) is not defined, then \(\lim_{x\to a}f(x)\) cannot exist.', r'Nếu \(f(a)\) không xác định thì \(\lim_{x\to a}f(x)\) không thể tồn tại.'), 'false', (r'False. Example: \(\dfrac{x^2-4}{x-2}\) is not defined at 2 but its limit there is 4.', r'Sai. Ví dụ \(\dfrac{x^2-4}{x-2}\) không xác định tại 2 nhưng giới hạn tại đó bằng 4.'))],
  [SHORT(5, (r'Find \(\lim_{x\to -2}(5-2x)\).', r'Tìm \(\lim_{x\to -2}(5-2x)\).'), '9', 'number', ('Enter a number.', 'Nhập một số.'), (r'Answer: 9. \(5+4=9\).', r'Đáp số: 9. \(5+4=9\).')),
   SHORT(6, (r'Find \(\lim_{x\to 5}\dfrac{x^2-25}{x-5}\).', r'Tìm \(\lim_{x\to 5}\dfrac{x^2-25}{x-5}\).'), '10', 'number', ('Enter a number.', 'Nhập một số.'), (r'Answer: 10. \(x+5\to 10\).', r'Đáp số: 10. \(x+5\to 10\).'))]]
practice = LEVEL_PRACTICE([('A. Multiple Choice', 'A. Trắc nghiệm'), ('B. True or False', 'B. Đúng hoặc sai'), ('C. Short Answer', 'C. Trả lời ngắn')], {1: S1, 2: S2, 3: S3})

mistakes = [
 (r'<b>Math knowledge.</b> Thinking that \(\lim_{x\to a}f(x)=f(a)\) always. If \(f\) has a hole or a jump at \(a\), the two numbers may differ.', r'<b>Kiến thức Toán.</b> Cho rằng \(\lim_{x\to a}f(x)=f(a)\) luôn đúng. Nếu \(f\) có lỗ thủng hoặc chỗ đứt tại \(a\) thì hai số này có thể khác nhau.'),
 (r'<b>Using formulas.</b> Writing \(\dfrac00=0\) or \(\dfrac00=1\). It is an undefined form: factor first.', r'<b>Dùng công thức.</b> Viết \(\dfrac00=0\) hoặc \(\dfrac00=1\). Đây là dạng chưa xác định: phải phân tích trước.'),
 (r'<b>Infinity.</b> Treating \(\infty\) as a number, for example \(\infty-\infty=0\).', r'<b>Vô cực.</b> Coi \(\infty\) là một số, chẳng hạn \(\infty-\infty=0\).'),
 (r'<b>One-sided limits.</b> Saying \(\lim_{x\to 0}\dfrac1x=+\infty\) by looking at the right side only.', r'<b>Giới hạn một bên.</b> Kết luận \(\lim_{x\to 0}\dfrac1x=+\infty\) chỉ vì nhìn phía bên phải.'),
]
summary = [
 (r'\(\lim_{x\to a}f(x)=L\) means \(f(x)\) is close to \(L\) when \(x\) is close to \(a\); \(f(a)\) is not needed.', r'\(\lim_{x\to a}f(x)=L\) nghĩa là \(f(x)\) gần \(L\) khi \(x\) gần \(a\); không cần \(f(a)\).'),
 ('The limit exists when the left-hand and the right-hand limits are equal.', 'Giới hạn tồn tại khi giới hạn bên trái và bên phải bằng nhau.'),
 (r'For \(\dfrac00\): factor, cancel the common factor, substitute again.', r'Với dạng \(\dfrac00\): phân tích, rút gọn thừa số chung, rồi thay lại.'),
 (r'At infinity divide by the highest power of \(x\); equal degrees give the ratio of the leading coefficients.', r'Tại vô cực chia cho lũy thừa cao nhất của \(x\); bậc bằng nhau thì giới hạn là tỉ số hai hệ số cao nhất.'),
 ('Key English phrases: find the limit; left-hand and right-hand limits; the limit does not exist; asymptote.', 'Cụm tiếng Anh cần nhớ: find the limit (tìm giới hạn); left-hand and right-hand limits (giới hạn bên trái và bên phải); the limit does not exist (giới hạn không tồn tại); asymptote (tiệm cận).'),
]
checks = [
 ('I can read a limit and one-sided limits from a graph.', 'Tôi đọc được giới hạn và giới hạn một bên từ đồ thị.'),
 ('I can compute a limit by substitution or by factoring.', 'Tôi tính được giới hạn bằng thay trực tiếp hoặc phân tích thành nhân tử.'),
 ('I can find the limit at infinity of a rational function.', 'Tôi tìm được giới hạn tại vô cực của hàm phân thức.'),
 ('I can find vertical and horizontal asymptotes from limits.', 'Tôi tìm được tiệm cận đứng và tiệm cận ngang từ giới hạn.'),
 STD_SUMMARY_CHECK_EN(),
]

lesson(id=LID, title_en='Limits of Functions', title_vi='Giới hạn của hàm số', topic=TOPIC,
       folder='limits', file='limits-of-functions',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Limits of functions: one-sided limits, factoring, limits at infinity and asymptotes.', level='Intermediate', minutes=55,
       description_vi='Giới hạn của hàm số: giới hạn một bên, phân tích nhân tử, giới hạn tại vô cực và tiệm cận.',
       tags_vi=['giới hạn', 'giới hạn một bên', 'vô cực', 'tiệm cận', 'dạng 0/0'],
       prerequisites=['g11-functions-01'], tags=['limit', 'one-sided limit', 'infinity', 'asymptote'], order=40)
