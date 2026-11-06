# -*- coding: utf-8 -*-
"""Nội dung bài g11-trige-01 = Toán 11 KNTT, Chương I, Bài 4: Phương trình lượng giác cơ bản – CHỈ NỘI DUNG.
Mã ngân hàng câu hỏi: TOAN11-C1-B04. Bài tập: mỗi mức một bộ riêng, cùng dạng, khác số liệu (LEVEL_PRACTICE)."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *

LID = 'g11-trige-01'
CAT = 'Trigonometric Equations'
TOPIC = (CAT, 'Phương trình lượng giác')
CV = 'Phương trình lượng giác'
PI = math.pi
S3 = math.sqrt(3); S2 = math.sqrt(2)

ensure_vocab([
 ('g11-trig-equation', 'trigonometric equation', 'phương trình lượng giác', CV, 'Solve the trigonometric equation.', r'\(\sin x=\dfrac12\)'),
 ('g11-basic-trig-eq', 'basic trigonometric equation', 'phương trình lượng giác cơ bản', CV, 'This is a basic trigonometric equation.', r'\(\cos x=m\)'),
 ('g11-general-solution', 'general solution', 'họ nghiệm', CV, 'Write the general solution.', r'\(x=\alpha+k2\pi\)'),
 ('g11-solution', 'solution', 'nghiệm', CV, 'Find all solutions in the interval.', ''),
 ('g11-arcsine', 'arcsine', 'arcsin', CV, 'The arcsine of 1/2 is pi/6.', r'\(\arcsin m\)'),
 ('g11-interval', 'interval', 'khoảng', CV, 'List the solutions in the interval.', ''),
 ('g11-no-solution', 'no solution', 'vô nghiệm', CV, 'The equation has no solution.', ''),
 ('g11-integer-k', 'integer k', 'số nguyên k', CV, 'Here k is any integer.', r'\(k\in\mathbb{Z}\)'),
])
load_vocab()

# ---- kiểm tra số liệu ----
ok = lambda x, y: abs(x - y) < 1e-9
def holds(fn, m, xs): return all(ok(fn(x), m) for x in xs)
K = range(-4, 5)
# họ nghiệm tổng quát
for a in (0.3, 0.9, 1.3):
    assert holds(math.sin, math.sin(a), [a + 2 * k * PI for k in K] + [PI - a + 2 * k * PI for k in K])
    assert holds(math.cos, math.cos(a), [a + 2 * k * PI for k in K] + [-a + 2 * k * PI for k in K])
    assert holds(math.tan, math.tan(a), [a + k * PI for k in K])
    assert holds(lambda x: 1 / math.tan(x), 1 / math.tan(a), [a + k * PI for k in K])
assert holds(math.sin, 0, [k * PI for k in K]) and holds(math.sin, 1, [PI / 2 + 2 * k * PI for k in K]) and holds(math.sin, -1, [-PI / 2 + 2 * k * PI for k in K])
assert holds(math.cos, 0, [PI / 2 + k * PI for k in K]) and holds(math.cos, 1, [2 * k * PI for k in K]) and holds(math.cos, -1, [PI + 2 * k * PI for k in K])
# arcsin 0,3 (máy tính)
a03 = math.asin(0.3); assert abs(a03 - 0.30469) < 1e-5 and abs(PI - a03 - 2.83690) < 1e-5 and abs(math.degrees(a03) - 17.4576) < 1e-3
def roots_in(fn, lo, hi, n=200000):               # nghiệm bằng quét đổi dấu (đối chứng với đáp án đại số)
    out, px, pv = [], lo, fn(lo)
    for i in range(1, n + 1):
        x = lo + (hi - lo) * i / n; v = fn(x)
        if pv == 0 or pv * v < 0: out.append(x if pv != 0 else px)
        px, pv = x, v
    return out
# VD1, VD2, VD3
assert holds(math.sin, 0.5, [PI / 6 + 2 * k * PI for k in K] + [5 * PI / 6 + 2 * k * PI for k in K])
assert holds(math.cos, -S2 / 2, [3 * PI / 4 + 2 * k * PI for k in K] + [-3 * PI / 4 + 2 * k * PI for k in K])
assert holds(lambda x: math.tan(x + PI / 4), S3, [PI / 12 + k * PI for k in K])
# VD4: cos 2x = 1/2 trên [0; 2π] có 4 nghiệm π/6, 5π/6, 7π/6, 11π/6
r4 = roots_in(lambda x: math.cos(2 * x) - 0.5, 0, 2 * PI)
assert len(r4) == 4 and all(abs(a - b) < 1e-4 for a, b in zip(r4, [PI / 6, 5 * PI / 6, 7 * PI / 6, 11 * PI / 6]))
# VD5: cos x + cos 3x = 0  <=>  x = π/4 + kπ/2  hoặc  x = π/2 + kπ
assert holds(lambda x: math.cos(x) + math.cos(3 * x), 0, [PI / 4 + k * PI / 2 for k in K] + [PI / 2 + k * PI for k in K])
r5 = roots_in(lambda x: math.cos(x) + math.cos(3 * x), 0.01, 2 * PI - 0.01)
assert len(r5) == 6 and all(abs(a - b) < 1e-4 for a, b in zip(r5, [PI / 4, PI / 2, 3 * PI / 4, 5 * PI / 4, 3 * PI / 2, 7 * PI / 4]))
# Bài tập
assert holds(math.sin, math.sin(PI / 5), [PI / 5 + 2 * k * PI for k in K] + [4 * PI / 5 + 2 * k * PI for k in K])
assert holds(math.cos, 0.5, [PI / 3 + 2 * k * PI for k in K] + [-PI / 3 + 2 * k * PI for k in K])
assert holds(math.tan, math.tan(PI / 5), [PI / 5 + k * PI for k in K])
assert holds(math.sin, math.sin(PI / 7), [PI / 7 + 2 * k * PI for k in K] + [6 * PI / 7 + 2 * k * PI for k in K])
assert holds(math.cos, math.cos(PI / 5), [PI / 5 + 2 * k * PI for k in K] + [-PI / 5 + 2 * k * PI for k in K])
assert holds(math.tan, math.tan(PI / 7), [PI / 7 + k * PI for k in K])
assert holds(math.cos, math.cos(PI / 8), [PI / 8 + 2 * k * PI for k in K] + [-PI / 8 + 2 * k * PI for k in K])
assert holds(math.sin, math.sin(PI / 8), [PI / 8 + 2 * k * PI for k in K] + [7 * PI / 8 + 2 * k * PI for k in K])
assert holds(math.tan, math.tan(PI / 8), [PI / 8 + k * PI for k in K])
for m, cnt in ((0.3, 2), (-1, 1), (1.2, 0)):      # C7: số nghiệm trong [0; 2π]
    fn = (lambda x: math.sin(x) - m) if m == 0.3 else (lambda x: math.cos(x) - m)
    if m == -1: assert ok(math.cos(PI), -1) and all(math.cos(i * 2 * PI / 100000) + 1 > -1e-12 for i in range(100001)) and all(abs(math.cos(i * 2 * PI / 1000) + 1) > 1e-9 for i in range(1001) if i != 500)    # chạm tại x = π: đúng 1 nghiệm
    else: assert len(roots_in(fn, 0, 2 * PI)) == cnt
assert ok(math.degrees(math.asin(0.5)), 30) and ok(math.degrees(math.acos(0.5)), 60) and ok(math.degrees(math.atan(1)), 45)
assert ok(math.degrees(math.asin(S3 / 2)), 60) and ok(math.degrees(math.acos(S2 / 2)), 45) and ok(math.degrees(math.atan(S3)), 60)
assert max(math.sin(x / 1000) for x in range(0, 6284)) < 0.9 + 0.1 + 1e-9                  # |sin| <= 1: sin x = 0,9 có nghiệm, sin x = 1,5 vô nghiệm
assert all(abs(math.cos(x / 100)) <= 1 for x in range(0, 700)) and 1.01 > 1 and math.sqrt(2) > 1

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 65 minutes', 'khoảng 65 phút'),
            before=('trigonometric functions, their graphs and periods (Lesson 3) and the trigonometric formulas (Lesson 2)', 'hàm số lượng giác, đồ thị và chu kì (Bài 3), công thức lượng giác (Bài 2)'))
goals = [
 ('recognise the four basic trigonometric equations;', 'nhận biết bốn [[phương trình lượng giác cơ bản]];'),
 ('write the [[general solution]] of each basic equation.', 'viết [[họ nghiệm]] của từng phương trình cơ bản.'),
 ('pick the solutions in a given interval;', 'chọn các [[nghiệm]] thuộc một [[khoảng]] cho trước;'),
 ('combine the trigonometric formulas to solve simple equations.', 'kết hợp công thức lượng giác để giải các phương trình đơn giản.'),
]
goals[1] = ('write the general solution of each basic equation;', 'viết [[họ nghiệm]] của từng phương trình cơ bản;')
vocab = [
 (r'<b>trigonometric equation</b> – an equation with a trigonometric function of the unknown, such as \(\sin x=\dfrac12\).', r'[[Phương trình lượng giác]] – phương trình chứa hàm số lượng giác của ẩn, ví dụ \(\sin x=\dfrac12\).'),
 (r'<b>basic trigonometric equation</b> – one of \(\sin x=m\), \(\cos x=m\), \(\tan x=m\), \(\cot x=m\).', r'[[Phương trình lượng giác cơ bản]] – một trong các phương trình \(\sin x=m\), \(\cos x=m\), \(\tan x=m\), \(\cot x=m\).'),
 (r'<b>general solution</b> – a formula with \(k\in\mathbb{Z}\) that gives all the solutions.', r'[[Họ nghiệm]] – công thức có \(k\in\mathbb{Z}\) cho tất cả các nghiệm.'),
 ('<b>solution</b> – a value of the unknown that makes the equation true.', '[[Nghiệm]] – giá trị của ẩn làm cho phương trình đúng.'),
 (r'<b>arcsine</b> – \(\arcsin m\) is the angle in \(\left[-\dfrac{\pi}{2};\dfrac{\pi}{2}\right]\) whose sine is \(m\).', r'[[arcsin]] – \(\arcsin m\) là góc thuộc \(\left[-\dfrac{\pi}{2};\dfrac{\pi}{2}\right]\) có sin bằng \(m\).'),
 ('<b>interval</b> – all numbers between two endpoints.', '[[Khoảng]] – tập các số nằm giữa hai đầu mút.'),
 ('<b>no solution</b> – no value of x makes the equation true.', '[[Vô nghiệm]] – không có giá trị x nào làm phương trình đúng.'),
 (r'<b>integer k</b> – \(k\in\mathbb{Z}\): \(\dots,-2,-1,0,1,2,\dots\)', r'[[Số nguyên k]] – \(k\in\mathbb{Z}\): \(\dots,-2,-1,0,1,2,\dots\)'),
]
phrases = [
 ('<b>Solve the equation.</b>', 'Giải phương trình.'),
 ('<b>Write the general solution.</b>', 'Viết họ nghiệm.'),
 ('<b>Find the solutions in the interval.</b>', 'Tìm các nghiệm trong khoảng.'),
 ('<b>The equation has no solution.</b>', 'Phương trình vô nghiệm.'),
 ('<b>How many solutions are there?</b>', 'Có bao nhiêu nghiệm?'),
 ('<b>Where k is an integer.</b>', 'Với k là số nguyên.'),
]
review = (
 T(r'<b>Special values.</b> \(\sin\dfrac{\pi}{6}=\dfrac12\), \(\cos\dfrac{\pi}{3}=\dfrac12\), \(\sin\dfrac{\pi}{4}=\cos\dfrac{\pi}{4}=\dfrac{\sqrt2}{2}\), \(\tan\dfrac{\pi}{4}=1\), \(\tan\dfrac{\pi}{3}=\sqrt3\).', r'<b>Giá trị đặc biệt.</b> \(\sin\dfrac{\pi}{6}=\dfrac12\), \(\cos\dfrac{\pi}{3}=\dfrac12\), \(\sin\dfrac{\pi}{4}=\cos\dfrac{\pi}{4}=\dfrac{\sqrt2}{2}\), \(\tan\dfrac{\pi}{4}=1\), \(\tan\dfrac{\pi}{3}=\sqrt3\).') +
 T(r'<b>Periods.</b> \(\sin\) and \(\cos\) repeat every \(2\pi\); \(\tan\) and \(\cot\) repeat every \(\pi\).', r'<b>Chu kì.</b> \(\sin\), \(\cos\) lặp lại sau \(2\pi\); \(\tan\), \(\cot\) lặp lại sau \(\pi\).') +
 T(r'<b>Related angles.</b> \(\sin(\pi-\alpha)=\sin\alpha\) and \(\cos(-\alpha)=\cos\alpha\).', r'<b>Góc liên quan.</b> \(\sin(\pi-\alpha)=\sin\alpha\) và \(\cos(-\alpha)=\cos\alpha\).'))

theory = '<h3>5.1 %s</h3>' % TI('The equation sin x = m', 'Phương trình sin x = m')
theory += T(r'A <b>basic trigonometric equation</b> has one of the forms \(\sin x=m\), \(\cos x=m\), \(\tan x=m\), \(\cot x=m\). Solving it means finding <b>all</b> \(x\) that make it true; because the functions repeat, there are infinitely many solutions in general.',
            r'[[Phương trình lượng giác cơ bản]] có một trong các dạng \(\sin x=m\), \(\cos x=m\), \(\tan x=m\), \(\cot x=m\). Giải phương trình là tìm <b>tất cả</b> các \(x\) thỏa mãn; vì các hàm số lặp lại nên nói chung có vô số nghiệm.')
theory += GRAPH({'view': [-0.6, 6.9, -1.9, 1.9], 'pi': True, 'params': [{'name': 'm', 'min': -1.5, 'max': 1.5, 'value': 0.5, 'step': 0.05}], 'family': [{'m': 0.5, '_label': 'y = 0.5'}, {'m': 1.5, '_label': 'y = 1.5', '_color': '#7c3aed'}],
                 'functions': [{'f': 'sin(x)', 'label': 'y = sin x'}, {'f': 'm', 'label': 'y = m', 'color': '#c2410c', 'width': 1.8}], 'mark': {'intersections': [[0, 1]]}},
                cap=('The solutions of sin x = m are the x-coordinates of the intersection points. For m = 0.5 there are two solutions in [0; 2π]; the line y = 1.5 (|m| > 1) does not meet the curve.', 'Nghiệm của sin x = m là hoành độ các giao điểm. Với m = 0,5 có hai nghiệm trong [0; 2π]; đường y = 1,5 (|m| > 1) không cắt đồ thị.'),
                alt=('Sine curve and a horizontal line y = m', ''), height=340)
theory += BOX('blue', ('Solving sin x = m', 'Giải sin x = m'),
  T(r'If \(|m|>1\): no solution (because \(-1\le\sin x\le 1\)).', r'Nếu \(|m|>1\): [[vô nghiệm]] (vì \(-1\le\sin x\le 1\)).'),
  T(r'If \(|m|\le 1\): let \(\alpha\) be an angle with \(\sin\alpha=m\) (for example \(\alpha=\arcsin m\)). Then', r'Nếu \(|m|\le 1\): gọi \(\alpha\) là góc có \(\sin\alpha=m\) (chẳng hạn \(\alpha=\arcsin m\)). Khi đó'),
  M(r'\sin x=\sin\alpha\iff\begin{cases}x=\alpha+k2\pi\\ x=\pi-\alpha+k2\pi\end{cases}\qquad(k\in\mathbb{Z})'),
  T(r'In degrees: \(x=\alpha^\circ+k360^\circ\) or \(x=180^\circ-\alpha^\circ+k360^\circ\).', r'Theo độ: \(x=\alpha^\circ+k360^\circ\) hoặc \(x=180^\circ-\alpha^\circ+k360^\circ\).'),
  T(r'Special cases: \(\sin x=0\iff x=k\pi\); \(\sin x=1\iff x=\dfrac{\pi}{2}+k2\pi\); \(\sin x=-1\iff x=-\dfrac{\pi}{2}+k2\pi\).', r'Trường hợp đặc biệt: \(\sin x=0\iff x=k\pi\); \(\sin x=1\iff x=\dfrac{\pi}{2}+k2\pi\); \(\sin x=-1\iff x=-\dfrac{\pi}{2}+k2\pi\).'))

theory += '<h3>5.2 %s</h3>' % TI('The equation cos x = m', 'Phương trình cos x = m')
theory += BOX('blue', ('Solving cos x = m', 'Giải cos x = m'),
  T(r'If \(|m|>1\): no solution. If \(|m|\le 1\): let \(\cos\alpha=m\). Then', r'Nếu \(|m|>1\): vô nghiệm. Nếu \(|m|\le 1\): gọi \(\alpha\) là góc có \(\cos\alpha=m\). Khi đó'),
  M(r'\cos x=\cos\alpha\iff x=\pm\alpha+k2\pi\qquad(k\in\mathbb{Z})'),
  T(r'Special cases: \(\cos x=0\iff x=\dfrac{\pi}{2}+k\pi\); \(\cos x=1\iff x=k2\pi\); \(\cos x=-1\iff x=\pi+k2\pi\).', r'Trường hợp đặc biệt: \(\cos x=0\iff x=\dfrac{\pi}{2}+k\pi\); \(\cos x=1\iff x=k2\pi\); \(\cos x=-1\iff x=\pi+k2\pi\).'))

theory += '<h3>5.3 %s</h3>' % TI('The equations tan x = m and cot x = m', 'Phương trình tan x = m và cot x = m')
theory += GRAPH({'view': [-1.7, 4.9, -5, 5], 'pi': True, 'params': [{'name': 'm', 'min': -4, 'max': 4, 'value': 1, 'step': 0.1}],
                 'functions': [{'f': 'tan(x)', 'label': 'y = tan x'}, {'f': 'm', 'label': 'y = 1', 'color': '#c2410c', 'width': 1.8}], 'mark': {'intersections': [[0, 1]]},
                 'asymptotes': [{'type': 'v', 'x': PI / 2}, {'type': 'v', 'x': -PI / 2}, {'type': 'v', 'x': 3 * PI / 2}]},
                cap=('For every real m the line meets each branch of tan x exactly once, so tan x = m always has solutions, spaced π apart.', 'Với mọi số thực m, đường thẳng cắt mỗi nhánh của tan x đúng một lần nên tan x = m luôn có nghiệm, cách nhau π.'),
                alt=('Tangent curve and a horizontal line y = m', ''), height=340)
theory += BOX('blue', ('Solving tan x = m and cot x = m', 'Giải tan x = m và cot x = m'),
  T(r'The equation \(\tan x=m\) has solutions for every real \(m\). Let \(\tan\alpha=m\) (for example \(\alpha=\arctan m\)). Then', r'Phương trình \(\tan x=m\) có nghiệm với mọi số thực \(m\). Gọi \(\alpha\) là góc có \(\tan\alpha=m\) (chẳng hạn \(\alpha=\arctan m\)). Khi đó'),
  M(r'\tan x=\tan\alpha\iff x=\alpha+k\pi\qquad(k\in\mathbb{Z})'),
  T(r'The equation \(\cot x=m\) also has solutions for every real \(m\): with \(\cot\alpha=m\),', r'Phương trình \(\cot x=m\) cũng có nghiệm với mọi số thực \(m\): với \(\cot\alpha=m\),'),
  M(r'\cot x=\cot\alpha\iff x=\alpha+k\pi\qquad(k\in\mathbb{Z})'),
  T(r'Remember the conditions: \(\tan x\) needs \(\cos x\ne 0\) and \(\cot x\) needs \(\sin x\ne 0\).', r'Nhớ điều kiện: \(\tan x\) cần \(\cos x\ne 0\), \(\cot x\) cần \(\sin x\ne 0\).'))
theory += BOX('mint', ('When m is not a special value', 'Khi m không phải giá trị đặc biệt'),
  T(r'Use a calculator in radian mode. For example \(\sin x=0.3\): \(\alpha=\arcsin 0.3\approx 0.3047\), so \(x\approx 0.3047+k2\pi\) or \(x\approx\pi-0.3047\approx 2.8369+k2\pi\). In degrees, \(\alpha\approx 17.46^\circ\).',
    r'Dùng máy tính ở chế độ radian. Ví dụ \(\sin x=0{,}3\): \(\alpha=\arcsin 0{,}3\approx 0{,}3047\), nên \(x\approx 0{,}3047+k2\pi\) hoặc \(x\approx\pi-0{,}3047\approx 2{,}8369+k2\pi\). Theo độ, \(\alpha\approx 17{,}46^\circ\).'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'),
  T(r'Do not mix units: write \(k2\pi\) with radians and \(k360^\circ\) with degrees in the same answer. For \(\cos x=\cos\alpha\) write \(\pm\alpha\) (two families); for \(\tan x=\tan\alpha\) the period is \(\pi\), not \(2\pi\).',
    r'Không trộn đơn vị: dùng \(k2\pi\) với radian, \(k360^\circ\) với độ trong cùng một đáp án. Với \(\cos x=\cos\alpha\) viết \(\pm\alpha\) (hai họ nghiệm); với \(\tan x=\tan\alpha\) chu kì là \(\pi\), không phải \(2\pi\).'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Solve sin x = 1/2', 'Giải sin x = 1/2'),
  T(r'Solve \(\sin x=\dfrac12\).', r'Giải phương trình \(\sin x=\dfrac12\).'),
  (r'Find an angle \(\alpha\) with \(\sin\alpha=\dfrac12\), then use the two families.', r'Tìm góc \(\alpha\) có \(\sin\alpha=\dfrac12\), rồi dùng hai họ nghiệm.'),
  [T(r'\(\dfrac12=\sin\dfrac{\pi}{6}\), so \(\sin x=\sin\dfrac{\pi}{6}\).', r'\(\dfrac12=\sin\dfrac{\pi}{6}\) nên \(\sin x=\sin\dfrac{\pi}{6}\).'),
   T(r'\(x=\dfrac{\pi}{6}+k2\pi\) or \(x=\pi-\dfrac{\pi}{6}+k2\pi=\dfrac{5\pi}{6}+k2\pi\), \(k\in\mathbb{Z}\).', r'\(x=\dfrac{\pi}{6}+k2\pi\) hoặc \(x=\pi-\dfrac{\pi}{6}+k2\pi=\dfrac{5\pi}{6}+k2\pi\), \(k\in\mathbb{Z}\).')],
  r'\(x=\dfrac{\pi}{6}+k2\pi\) or \(x=\dfrac{5\pi}{6}+k2\pi\), \(k\in\mathbb{Z}\).')
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Solve cos x = −√2/2', 'Giải cos x = −√2/2'),
  T(r'Solve \(\cos x=-\dfrac{\sqrt2}{2}\).', r'Giải phương trình \(\cos x=-\dfrac{\sqrt2}{2}\).'),
  (r'Use \(\cos\dfrac{3\pi}{4}=-\dfrac{\sqrt2}{2}\) and the formula \(x=\pm\alpha+k2\pi\).', r'Dùng \(\cos\dfrac{3\pi}{4}=-\dfrac{\sqrt2}{2}\) và công thức \(x=\pm\alpha+k2\pi\).'),
  [T(r'\(\cos x=\cos\dfrac{3\pi}{4}\).', r'\(\cos x=\cos\dfrac{3\pi}{4}\).'), T(r'So \(x=\pm\dfrac{3\pi}{4}+k2\pi\), \(k\in\mathbb{Z}\).', r'Vậy \(x=\pm\dfrac{3\pi}{4}+k2\pi\), \(k\in\mathbb{Z}\).')],
  r'\(x=\pm\dfrac{3\pi}{4}+k2\pi\), \(k\in\mathbb{Z}\).')
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('An equation with tan', 'Phương trình có tan'),
  T(r'Solve \(\tan\left(x+\dfrac{\pi}{4}\right)=\sqrt3\).', r'Giải phương trình \(\tan\left(x+\dfrac{\pi}{4}\right)=\sqrt3\).'),
  (r'Treat \(x+\dfrac{\pi}{4}\) as one angle. \(\sqrt3=\tan\dfrac{\pi}{3}\).', r'Coi \(x+\dfrac{\pi}{4}\) là một góc. \(\sqrt3=\tan\dfrac{\pi}{3}\).'),
  [T(r'\(x+\dfrac{\pi}{4}=\dfrac{\pi}{3}+k\pi\).', r'\(x+\dfrac{\pi}{4}=\dfrac{\pi}{3}+k\pi\).'),
   T(r'\(x=\dfrac{\pi}{3}-\dfrac{\pi}{4}+k\pi=\dfrac{\pi}{12}+k\pi\), \(k\in\mathbb{Z}\).', r'\(x=\dfrac{\pi}{3}-\dfrac{\pi}{4}+k\pi=\dfrac{\pi}{12}+k\pi\), \(k\in\mathbb{Z}\).'),
   T(r'The condition \(\cos\left(x+\dfrac{\pi}{4}\right)\ne 0\) holds, since \(x+\dfrac{\pi}{4}=\dfrac{\pi}{3}+k\pi\).', r'Điều kiện \(\cos\left(x+\dfrac{\pi}{4}\right)\ne 0\) thỏa mãn vì \(x+\dfrac{\pi}{4}=\dfrac{\pi}{3}+k\pi\).')],
  r'\(x=\dfrac{\pi}{12}+k\pi\), \(k\in\mathbb{Z}\).')
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Solutions in an interval', 'Nghiệm trong một đoạn'),
  T(r'Find the solutions of \(\cos 2x=\dfrac12\) in \([0;2\pi]\).', r'Tìm các nghiệm của \(\cos 2x=\dfrac12\) trong \([0;2\pi]\).') +
  GRAPH({'view': [-0.4, 6.7, -1.6, 1.6], 'pi': True, 'markRange': [0, 2 * PI], 'functions': [{'f': 'cos(2x)', 'label': 'y = cos 2x'}, {'f': '0.5', 'label': 'y = 1/2', 'color': '#c2410c', 'width': 1.8}], 'mark': {'intersections': [[0, 1]]}},
        alt=('Curve y = cos 2x and the line y = 1/2 meeting four times', ''), height=300),
  (r'Solve in general first, then choose the integers \(k\) that put \(x\) in \([0;2\pi]\).', r'Giải tổng quát trước, rồi chọn các số nguyên \(k\) để \(x\) thuộc \([0;2\pi]\).'),
  [T(r'\(\cos 2x=\cos\dfrac{\pi}{3}\Rightarrow 2x=\pm\dfrac{\pi}{3}+k2\pi\Rightarrow x=\pm\dfrac{\pi}{6}+k\pi\).', r'\(\cos 2x=\cos\dfrac{\pi}{3}\Rightarrow 2x=\pm\dfrac{\pi}{3}+k2\pi\Rightarrow x=\pm\dfrac{\pi}{6}+k\pi\).'),
   T(r'For \(x=\dfrac{\pi}{6}+k\pi\): \(k=0\to\dfrac{\pi}{6}\); \(k=1\to\dfrac{7\pi}{6}\).', r'Với \(x=\dfrac{\pi}{6}+k\pi\): \(k=0\to\dfrac{\pi}{6}\); \(k=1\to\dfrac{7\pi}{6}\).'),
   T(r'For \(x=-\dfrac{\pi}{6}+k\pi\): \(k=1\to\dfrac{5\pi}{6}\); \(k=2\to\dfrac{11\pi}{6}\).', r'Với \(x=-\dfrac{\pi}{6}+k\pi\): \(k=1\to\dfrac{5\pi}{6}\); \(k=2\to\dfrac{11\pi}{6}\).'),
   T(r'Four solutions, matching the four intersection points in the figure.', r'Có bốn nghiệm, khớp với bốn giao điểm trên hình.')],
  r'\(x\in\left\{\dfrac{\pi}{6},\dfrac{5\pi}{6},\dfrac{7\pi}{6},\dfrac{11\pi}{6}\right\}\).')
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Using a formula first', 'Dùng công thức trước khi giải'),
  T(r'Solve \(\cos x+\cos 3x=0\).', r'Giải phương trình \(\cos x+\cos 3x=0\).'),
  (r'Turn the sum into a product (Lesson 2), then solve two basic equations.', r'Biến đổi tổng thành tích (Bài 2), rồi giải hai phương trình cơ bản.'),
  [T(r'\(\cos x+\cos 3x=2\cos 2x\cos x\), so the equation is \(\cos 2x\cos x=0\).', r'\(\cos x+\cos 3x=2\cos 2x\cos x\) nên phương trình trở thành \(\cos 2x\cos x=0\).'),
   T(r'\(\cos 2x=0\iff 2x=\dfrac{\pi}{2}+k\pi\iff x=\dfrac{\pi}{4}+\dfrac{k\pi}{2}\).', r'\(\cos 2x=0\iff 2x=\dfrac{\pi}{2}+k\pi\iff x=\dfrac{\pi}{4}+\dfrac{k\pi}{2}\).'),
   T(r'\(\cos x=0\iff x=\dfrac{\pi}{2}+k\pi\).', r'\(\cos x=0\iff x=\dfrac{\pi}{2}+k\pi\).'),
   T(r'These two families are different: the first never gives \(\dfrac{\pi}{2}\), so we keep both.', r'Hai họ nghiệm này khác nhau: họ thứ nhất không bao giờ cho \(\dfrac{\pi}{2}\), nên giữ cả hai.')],
  r'\(x=\dfrac{\pi}{4}+\dfrac{k\pi}{2}\) or \(x=\dfrac{\pi}{2}+k\pi\), \(k\in\mathbb{Z}\).')

# A1 họ nghiệm; A2 phương trình vô nghiệm / nghiệm đặc biệt; A3 nghiệm đặc biệt; B4 số nghiệm; B5 công thức; C6 nghiệm nhỏ nhất (độ); C7 số nghiệm trong [0; 2π]
HN = ('Enter a whole number.', 'Nhập một số nguyên.')
Q1 = [
  [MCQ(1, (r'Which gives all solutions of \(\sin x=\sin\dfrac{\pi}{5}\)?', r'Công thức nào cho tất cả nghiệm của \(\sin x=\sin\dfrac{\pi}{5}\)?'),
       [r'x=\dfrac{\pi}{5}+k\pi', r'x=\dfrac{\pi}{5}+k2\pi,\ x=\dfrac{4\pi}{5}+k2\pi', r'x=\pm\dfrac{\pi}{5}+k2\pi', r'x=\dfrac{\pi}{5}+k2\pi,\ x=-\dfrac{\pi}{5}+k2\pi'], 'b', (r'Answer: b. The second family is \(\pi-\dfrac{\pi}{5}=\dfrac{4\pi}{5}\).', r'Đáp án b. Họ thứ hai là \(\pi-\dfrac{\pi}{5}=\dfrac{4\pi}{5}\).')),
   MCQ(2, (r'Which of these equations has no solution?', r'Phương trình nào dưới đây vô nghiệm?'), [r'\sin x=0.9', r'\cos x=-1', r'\tan x=5', r'\sin x=1.5'], 'd', (r'Answer: d. \(\sin x\le 1\), so \(\sin x=1.5\) has no solution.', r'Đáp án d. \(\sin x\le 1\) nên \(\sin x=1{,}5\) vô nghiệm.')),
   MCQ(3, (r'Solve \(\sin x=0\).', r'Giải phương trình \(\sin x=0\).'), [r'x=k\pi', r'x=k2\pi', r'x=\dfrac{\pi}{2}+k\pi', r'x=\dfrac{\pi}{2}+k2\pi'], 'a', (r'Answer: a. \(\sin x=0\) at every multiple of \(\pi\).', r'Đáp án a. \(\sin x=0\) tại mọi bội của \(\pi\).'))],
  [TF(4, (r'The equation \(\sin x=\dfrac12\) has exactly two solutions in \([0;2\pi]\).', r'Phương trình \(\sin x=\dfrac12\) có đúng hai nghiệm trong \([0;2\pi]\).'), 'true', (r'True: \(\dfrac{\pi}{6}\) and \(\dfrac{5\pi}{6}\).', r'Đúng: \(\dfrac{\pi}{6}\) và \(\dfrac{5\pi}{6}\).')),
   TF(5, (r'\(\tan x=\tan\alpha\iff x=\alpha+k\pi\), \(k\in\mathbb{Z}\) (when both sides are defined).', r'\(\tan x=\tan\alpha\iff x=\alpha+k\pi\), \(k\in\mathbb{Z}\) (khi hai vế xác định).'), 'true', (r'True. The period of tangent is \(\pi\).', r'Đúng. Chu kì của hàm tan là \(\pi\).'))],
  [SHORT(6, (r'Solve \(\sin x=\dfrac12\). What is the smallest positive solution in degrees?', r'Giải \(\sin x=\dfrac12\). Nghiệm dương nhỏ nhất theo độ là bao nhiêu?'), '30', 'number', ('Enter a number of degrees.', 'Nhập số đo theo độ.'), (r'Answer: 30. \(\sin 30^\circ=\dfrac12\).', r'Đáp số: 30. \(\sin 30^\circ=\dfrac12\).')),
   SHORT(7, (r'How many solutions does \(\sin x=0.3\) have in \([0;2\pi]\)?', r'Phương trình \(\sin x=0{,}3\) có bao nhiêu nghiệm trong \([0;2\pi]\)?'), '2', 'number', HN, (r'Answer: 2: \(\alpha\) and \(\pi-\alpha\) with \(\alpha\approx 0.3047\).', r'Đáp số: 2: \(\alpha\) và \(\pi-\alpha\) với \(\alpha\approx 0{,}3047\).'))]]
Q2 = [
  [MCQ(1, (r'Which gives all solutions of \(\cos x=\cos\dfrac{\pi}{5}\)?', r'Công thức nào cho tất cả nghiệm của \(\cos x=\cos\dfrac{\pi}{5}\)?'),
       [r'x=\dfrac{\pi}{5}+k\pi', r'x=\dfrac{\pi}{5}+k2\pi,\ x=\dfrac{4\pi}{5}+k2\pi', r'x=\pm\dfrac{\pi}{5}+k2\pi', r'x=\dfrac{\pi}{5}+k2\pi'], 'c', (r'Answer: c. For cosine, the two families are \(\alpha+k2\pi\) and \(-\alpha+k2\pi\).', r'Đáp án c. Với cos, hai họ nghiệm là \(\alpha+k2\pi\) và \(-\alpha+k2\pi\).')),
   MCQ(2, (r'Choose the equation that has no solution.', r'Chọn phương trình vô nghiệm.'), [r'\sin x=-1', r'\cos x=\dfrac13', r'\tan x=-10', r'\cos x=-\sqrt2'], 'd', (r'Answer: d. \(-\sqrt2\approx -1.41\lt -1\), but \(\cos x\ge -1\).', r'Đáp án d. \(-\sqrt2\approx -1{,}41\lt -1\), mà \(\cos x\ge -1\).')),
   MCQ(3, (r'Solve \(\cos x=0\).', r'Giải phương trình \(\cos x=0\).'), [r'x=k\pi', r'x=k2\pi', r'x=\dfrac{\pi}{2}+k\pi', r'x=\pi+k2\pi'], 'c', (r'Answer: c. \(\cos x=0\) at \(\dfrac{\pi}{2}\), \(\dfrac{3\pi}{2}\), ... that is \(\dfrac{\pi}{2}+k\pi\).', r'Đáp án c. \(\cos x=0\) tại \(\dfrac{\pi}{2}\), \(\dfrac{3\pi}{2}\), ... tức \(\dfrac{\pi}{2}+k\pi\).'))],
  [TF(4, (r'The solutions of \(\cos x=\dfrac12\) are only \(x=\dfrac{\pi}{3}+k2\pi\).', r'Nghiệm của \(\cos x=\dfrac12\) chỉ là \(x=\dfrac{\pi}{3}+k2\pi\).'), 'false', (r'False. There is also \(x=-\dfrac{\pi}{3}+k2\pi\).', r'Sai. Còn có họ \(x=-\dfrac{\pi}{3}+k2\pi\).')),
   TF(5, (r'\(\sin x=\sin\alpha\iff x=\alpha+k\pi\).', r'\(\sin x=\sin\alpha\iff x=\alpha+k\pi\).'), 'false', (r'False. The correct families are \(\alpha+k2\pi\) and \(\pi-\alpha+k2\pi\).', r'Sai. Hai họ nghiệm đúng là \(\alpha+k2\pi\) và \(\pi-\alpha+k2\pi\).'))],
  [SHORT(6, (r'Solve \(\cos x=\dfrac12\). What is the smallest positive solution in degrees?', r'Giải \(\cos x=\dfrac12\). Nghiệm dương nhỏ nhất theo độ là bao nhiêu?'), '60', 'number', ('Enter a number of degrees.', 'Nhập số đo theo độ.'), (r'Answer: 60. \(\cos 60^\circ=\dfrac12\).', r'Đáp số: 60. \(\cos 60^\circ=\dfrac12\).')),
   SHORT(7, (r'How many solutions does \(\cos x=-1\) have in \([0;2\pi]\)?', r'Phương trình \(\cos x=-1\) có bao nhiêu nghiệm trong \([0;2\pi]\)?'), '1', 'number', HN, (r'Answer: 1: only \(x=\pi\).', r'Đáp số: 1: chỉ có \(x=\pi\).'))]]
Q3 = [
  [MCQ(1, (r'Which gives all solutions of \(\tan x=\tan\dfrac{\pi}{5}\)?', r'Công thức nào cho tất cả nghiệm của \(\tan x=\tan\dfrac{\pi}{5}\)?'),
       [r'x=\dfrac{\pi}{5}+k2\pi', r'x=\dfrac{\pi}{5}+k\pi', r'x=\pm\dfrac{\pi}{5}+k\pi', r'x=\dfrac{\pi}{5}+k2\pi,\ x=\dfrac{4\pi}{5}+k2\pi'], 'b', (r'Answer: b. Tangent has period \(\pi\).', r'Đáp án b. Hàm tan có chu kì \(\pi\).')),
   MCQ(2, (r'Which one cannot be solved because the value is out of range?', r'Phương trình nào vô nghiệm vì giá trị nằm ngoài miền giá trị?'), [r'\cot x=100', r'\sin x=-0.99', r'\cos x=1.01', r'\tan x=0'], 'c', (r'Answer: c. \(\cos x\le 1\), so \(\cos x=1.01\) has no solution.', r'Đáp án c. \(\cos x\le 1\) nên \(\cos x=1{,}01\) vô nghiệm.')),
   MCQ(3, (r'Solve \(\sin x=-1\).', r'Giải phương trình \(\sin x=-1\).'), [r'x=-\dfrac{\pi}{2}+k2\pi', r'x=\dfrac{\pi}{2}+k2\pi', r'x=-\dfrac{\pi}{2}+k\pi', r'x=\pi+k2\pi'], 'a', (r'Answer: a. \(\sin\left(-\dfrac{\pi}{2}\right)=-1\) and the period is \(2\pi\).', r'Đáp án a. \(\sin\left(-\dfrac{\pi}{2}\right)=-1\) và chu kì là \(2\pi\).'))],
  [TF(4, (r'The equation \(\tan x=1\) has infinitely many solutions.', r'Phương trình \(\tan x=1\) có vô số nghiệm.'), 'true', (r'True: \(x=\dfrac{\pi}{4}+k\pi\), \(k\in\mathbb{Z}\).', r'Đúng: \(x=\dfrac{\pi}{4}+k\pi\), \(k\in\mathbb{Z}\).')),
   TF(5, (r'\(\cos x=\cos\alpha\iff x=\pm\alpha+k2\pi\), \(k\in\mathbb{Z}\).', r'\(\cos x=\cos\alpha\iff x=\pm\alpha+k2\pi\), \(k\in\mathbb{Z}\).'), 'true', (r'True. This is the formula for cosine.', r'Đúng. Đây là công thức của phương trình cos.'))],
  [SHORT(6, (r'Solve \(\tan x=1\). What is the smallest positive solution in degrees?', r'Giải \(\tan x=1\). Nghiệm dương nhỏ nhất theo độ là bao nhiêu?'), '45', 'number', ('Enter a number of degrees.', 'Nhập số đo theo độ.'), (r'Answer: 45. \(\tan 45^\circ=1\).', r'Đáp số: 45. \(\tan 45^\circ=1\).')),
   SHORT(7, (r'How many solutions does \(\cos x=1.2\) have in \([0;2\pi]\)?', r'Phương trình \(\cos x=1{,}2\) có bao nhiêu nghiệm trong \([0;2\pi]\)?'), '0', 'number', HN, (r'Answer: 0, because \(\cos x\le 1\).', r'Đáp số: 0, vì \(\cos x\le 1\).'))]]
practice = LEVEL_PRACTICE([('A. Multiple Choice', 'A. Trắc nghiệm'), ('B. True or False', 'B. Đúng hoặc sai'), ('C. Short Answer', 'C. Trả lời ngắn')], {1: Q1, 2: Q2, 3: Q3})

mistakes = [
 (r'<b>Missing family.</b> For \(\sin x=\sin\alpha\) giving only \(x=\alpha+k2\pi\). The second family \(\pi-\alpha+k2\pi\) is also needed.', r'<b>Thiếu họ nghiệm.</b> Với \(\sin x=\sin\alpha\) chỉ viết \(x=\alpha+k2\pi\). Còn phải có họ \(\pi-\alpha+k2\pi\).'),
 (r'<b>Cosine sign.</b> For \(\cos x=\cos\alpha\) forgetting the minus: \(x=\pm\alpha+k2\pi\).', r'<b>Dấu của cos.</b> Với \(\cos x=\cos\alpha\) quên dấu trừ: \(x=\pm\alpha+k2\pi\).'),
 (r'<b>Wrong period.</b> Writing \(x=\alpha+k2\pi\) for \(\tan x=\tan\alpha\). The period of tangent is \(\pi\).', r'<b>Sai chu kì.</b> Viết \(x=\alpha+k2\pi\) cho \(\tan x=\tan\alpha\). Chu kì của hàm tan là \(\pi\).'),
 (r'<b>Out of range.</b> Trying to solve \(\sin x=1.5\) or \(\cos x=-2\). When \(|m|>1\) there is no solution.', r'<b>Ngoài miền giá trị.</b> Cố giải \(\sin x=1{,}5\) hoặc \(\cos x=-2\). Khi \(|m|>1\) phương trình vô nghiệm.'),
 (r'<b>Mixed units.</b> Writing \(x=30^\circ+k2\pi\). Use \(30^\circ+k360^\circ\) or \(\dfrac{\pi}{6}+k2\pi\).', r'<b>Trộn đơn vị.</b> Viết \(x=30^\circ+k2\pi\). Phải viết \(30^\circ+k360^\circ\) hoặc \(\dfrac{\pi}{6}+k2\pi\).'),
 (r'<b>Interval.</b> Listing the general solution as the answer when the problem asks for solutions in \([0;2\pi]\).', r'<b>Khoảng cho trước.</b> Ghi họ nghiệm tổng quát khi đề yêu cầu nghiệm trong \([0;2\pi]\).'),
]
summary = [
 (r'\(\sin x=\sin\alpha\iff x=\alpha+k2\pi\) or \(x=\pi-\alpha+k2\pi\); \(\cos x=\cos\alpha\iff x=\pm\alpha+k2\pi\); \(\tan x=\tan\alpha\) and \(\cot x=\cot\alpha\iff x=\alpha+k\pi\).', r'\(\sin x=\sin\alpha\iff x=\alpha+k2\pi\) hoặc \(x=\pi-\alpha+k2\pi\); \(\cos x=\cos\alpha\iff x=\pm\alpha+k2\pi\); \(\tan x=\tan\alpha\) và \(\cot x=\cot\alpha\iff x=\alpha+k\pi\).'),
 (r'\(\sin x=m\) and \(\cos x=m\) have no solution if \(|m|>1\); \(\tan x=m\) and \(\cot x=m\) have solutions for every \(m\).', r'\(\sin x=m\) và \(\cos x=m\) vô nghiệm nếu \(|m|>1\); \(\tan x=m\) và \(\cot x=m\) có nghiệm với mọi \(m\).'),
 ('To find solutions in an interval, solve in general first and then choose the integers k.', 'Để tìm nghiệm trong một khoảng, giải tổng quát trước rồi chọn các số nguyên k.'),
 ('Use the formulas of Lesson 2 to turn a sum into a product first; each factor gives a basic equation.', 'Dùng công thức ở Bài 2 để biến tổng thành tích; mỗi thừa số cho một phương trình cơ bản.'),
 ('Key English phrases: solve the equation; write the general solution; find the solutions in the interval; the equation has no solution.', 'Cụm tiếng Anh cần nhớ: solve the equation (giải phương trình); write the general solution (viết họ nghiệm); find the solutions in the interval (tìm nghiệm trong khoảng); the equation has no solution (phương trình vô nghiệm).'),
]
checks = [
 ('I can say when sin x = m and cos x = m have no solution.', 'Tôi nói được khi nào sin x = m và cos x = m vô nghiệm.'),
 ('I can write the general solution of the four basic equations.', 'Tôi viết được họ nghiệm của bốn phương trình cơ bản.'),
 ('I can find the solutions in a given interval.', 'Tôi tìm được các nghiệm thuộc một khoảng cho trước.'),
 ('I can use a formula to turn an equation into basic equations.', 'Tôi dùng được công thức để đưa phương trình về các phương trình cơ bản.'),
 STD_SUMMARY_CHECK_EN(),
]

lesson(id=LID, title_en='Basic Trigonometric Equations', title_vi='Phương trình lượng giác cơ bản', topic=TOPIC,
       folder='trigonometric-equations', file='basic-trigonometric-equations',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Solve sin x = m, cos x = m, tan x = m and cot x = m; general solutions and solutions in an interval.', level='Intermediate', minutes=65,
       description_vi='Bài 4 – Giải phương trình sin x = m, cos x = m, tan x = m, cot x = m; họ nghiệm và nghiệm trong một khoảng.',
       tags_vi=['phương trình lượng giác', 'họ nghiệm', 'nghiệm trong khoảng', 'sin x = m', 'cos x = m', 'tan x = m'],
       prerequisites=['g11-trigf-02'], tags=['trigonometric equation', 'general solution', 'basic equation', 'arcsin', 'interval'], order=35)
