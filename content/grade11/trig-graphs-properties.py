# -*- coding: utf-8 -*-
"""Nội dung bài g11-trigf-02 = Toán 11 KNTT, Chương I, Bài 3: Hàm số lượng giác – CHỈ NỘI DUNG.
Mã ngân hàng câu hỏi: TOAN11-C1-B03. Bài tập: mỗi mức một bộ riêng, cùng dạng, khác số liệu (LEVEL_PRACTICE)."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *

LID = 'g11-trigf-02'
CAT = 'Trigonometric Functions'
TOPIC = (CAT, 'Hàm số lượng giác')
CV = 'Hàm số lượng giác'
PI = math.pi

ensure_vocab([
 ('g11-periodic', 'periodic function', 'hàm số tuần hoàn', CV, 'The sine function is periodic.', ''),
 ('g11-period', 'period', 'chu kì', CV, 'The period of sine is 2 pi.', ''),
 ('g11-amplitude', 'amplitude', 'biên độ', CV, 'The amplitude of 3 sin x is 3.', ''),
 ('g11-even-function', 'even function', 'hàm số chẵn', CV, 'Cosine is an even function.', ''),
 ('g11-odd-function', 'odd function', 'hàm số lẻ', CV, 'Sine is an odd function.', ''),
 ('g11-max-value', 'maximum value', 'giá trị lớn nhất', CV, 'Find the maximum value of the function.', ''),
 ('g11-min-value', 'minimum value', 'giá trị nhỏ nhất', CV, 'Find the minimum value of the function.', ''),
 ('g11-graph-trig', 'sinusoidal curve', 'đường hình sin', CV, 'The graph of sine is a sinusoidal curve.', ''),
 ('g11-trig-function', 'trigonometric function', 'hàm số lượng giác', CV, 'Sine and cosine are trigonometric functions.', r'\(y=\sin x\)'),
 ('g11-increasing', 'increasing', 'đồng biến', CV, 'The sine function is increasing on this interval.', ''),
 ('g11-decreasing', 'decreasing', 'nghịch biến', CV, 'The cosine function is decreasing on this interval.', ''),
 ('g11-domain', 'domain', 'tập xác định', CV, 'State the domain of the function.', ''),
 ('g11-range', 'range', 'tập giá trị', CV, 'State the range of the function.', ''),
])
load_vocab()

# ---- kiểm tra số liệu (mọi công thức, ví dụ và đáp án bài tập) ----
ok = lambda x, y: abs(x - y) < 1e-9
# tính chẵn lẻ
for x in (0.3, 1.1, 2.0):
    assert ok(math.cos(-x), math.cos(x)) and ok(math.sin(-x), -math.sin(x)) and ok(math.tan(-x), -math.tan(x)) and ok(1 / math.tan(-x), -1 / math.tan(x))
    assert ok(math.sin(x + 2 * PI), math.sin(x)) and ok(math.cos(x + 2 * PI), math.cos(x)) and ok(math.tan(x + PI), math.tan(x)) and ok(1 / math.tan(x + PI), 1 / math.tan(x))
    assert ok((-x) * math.sin(-x), x * math.sin(x))                                           # VD2: x sin x chẵn
f2 = lambda x: math.sin(x) + math.cos(x)
assert not ok(f2(1), f2(-1)) and not ok(f2(1), -f2(-1))                                       # VD2: sin x + cos x không chẵn không lẻ
# VD1: tập xác định
assert abs(math.cos(5 * PI / 6 - PI / 3)) < 1e-12 and abs(math.sin(2 * (PI / 2))) < 1e-12
# VD3: giá trị lớn nhất, nhỏ nhất của y = 2 − 3cos x
ys = [2 - 3 * math.cos(i * 2 * PI / 20000) for i in range(20001)]
assert ok(max(ys), 5) and ok(min(ys), -1)
# VD4: chu kì của y = sin 2x + cos 3x là 2π
f4 = lambda x: math.sin(2 * x) + math.cos(3 * x)
assert all(ok(f4(x + 2 * PI), f4(x)) for x in (0.3, 1.2, 2.5))
assert not ok(f4(0.3 + PI), f4(0.3)) and not ok(f4(0.3 + 2 * PI / 3), f4(0.3)) and not ok(f4(0.3 + PI / 2), f4(0.3))
# VD5: thủy triều h(t) = 4 + 1,5 sin(πt/6)
h = lambda t: 4 + 1.5 * math.sin(PI * t / 6)
assert ok(h(3), 5.5) and ok(h(9), 2.5) and ok(h(0.5 + 12), h(0.5)) and ok(h(1), 4.75) and ok(h(5), 4.75)
assert all((h(t / 1000) >= 4.75) == (1 <= t / 1000 <= 5) for t in range(0, 12000, 7) if abs(t / 1000 - 1) > 1e-2 and abs(t / 1000 - 5) > 1e-2)
# Bài tập
assert ok(math.sin(2 * (0.3 + PI)), math.sin(2 * 0.3)) and ok(math.cos((0.3 + 4 * PI) / 2), math.cos(0.3 / 2)) and ok(math.tan(3 * (0.2 + PI / 3)), math.tan(3 * 0.2))
assert ok(2 * 1 + 1, 3) and ok(3 * (-1) - 2, -5) and ok(5 - 2 * (-1), 7) and ok(2 - (-1), 3) and ok(3 - 2 * (-1), 5) and ok(4 - 2 * 1, 2) and ok(3 * 1, 3)
assert ok(math.sin(PI / 6), 0.5) and ok(math.sin(5 * PI / 6), 0.5) and ok(math.cos(PI), -1)    # số nghiệm trên [0; 2π]
assert 2 * math.sin(0.3) + 1 < 3 + 1e-12

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 65 minutes', 'khoảng 65 phút'),
            before=('trigonometric values of an angle, radians and the unit circle (Lesson 1)', 'giá trị lượng giác của góc, radian và đường tròn đơn vị (Bài 1)'))
goals = [
 (r'state the domain and range of \(\sin x\), \(\cos x\), \(\tan x\) and \(\cot x\);', r'nêu [[tập xác định]], [[tập giá trị]] của \(\sin x\), \(\cos x\), \(\tan x\), \(\cot x\);'),
 ('find the period and decide whether a function is even or odd;', 'tìm [[chu kì]] và xét tính chẵn lẻ của hàm số;'),
 ('read the graphs and the intervals where each function is increasing or decreasing;', 'đọc [[đồ thị]] và các khoảng [[đồng biến]], [[nghịch biến]] của từng hàm số;'),
 ('find maximum and minimum values and model a periodic phenomenon.', 'tìm [[giá trị lớn nhất]], [[giá trị nhỏ nhất]] và mô hình hóa một hiện tượng tuần hoàn.'),
]
vocab = [
 (r'<b>trigonometric function</b> – a function such as \(y=\sin x\), \(y=\cos x\), \(y=\tan x\), \(y=\cot x\) whose variable is an angle in radians.', r'[[Hàm số lượng giác]] – hàm số như \(y=\sin x\), \(y=\cos x\), \(y=\tan x\), \(y=\cot x\) có biến là số đo góc (radian).'),
 ('<b>periodic function</b> – a function whose graph repeats after a fixed distance.', '[[Hàm số tuần hoàn]] – hàm số có đồ thị lặp lại sau một khoảng cố định.'),
 (r'<b>period</b> – the smallest positive \(T\) with \(f(x+T)=f(x)\).', r'[[Chu kì]] – số dương nhỏ nhất \(T\) sao cho \(f(x+T)=f(x)\).'),
 (r'<b>amplitude</b> – half of the difference between the maximum and minimum values; for \(a\sin x\) it is \(|a|\).', r'[[Biên độ]] – một nửa hiệu giữa giá trị lớn nhất và nhỏ nhất; với \(a\sin x\) là \(|a|\).'),
 (r'<b>even function</b> – \(f(-x)=f(x)\); the graph is symmetric about the y-axis.', r'[[Hàm số chẵn]] – \(f(-x)=f(x)\); đồ thị đối xứng qua trục tung.'),
 (r'<b>odd function</b> – \(f(-x)=-f(x)\); the graph is symmetric about the origin.', r'[[Hàm số lẻ]] – \(f(-x)=-f(x)\); đồ thị đối xứng qua gốc tọa độ.'),
 ('<b>increasing</b> – the values go up as x goes up.', '[[Đồng biến]] – giá trị hàm số tăng khi x tăng.'),
 ('<b>decreasing</b> – the values go down as x goes up.', '[[Nghịch biến]] – giá trị hàm số giảm khi x tăng.'),
 ('<b>domain</b> – the set of all x for which the function is defined.', '[[Tập xác định]] – tập các giá trị x mà hàm số xác định.'),
 ('<b>range</b> – the set of all values that the function takes.', '[[Tập giá trị]] – tập các giá trị mà hàm số nhận được.'),
 ('<b>maximum value</b> – the greatest value of the function.', '[[Giá trị lớn nhất]] – giá trị lớn nhất mà hàm số đạt được.'),
 ('<b>minimum value</b> – the smallest value of the function.', '[[Giá trị nhỏ nhất]] – giá trị nhỏ nhất mà hàm số đạt được.'),
 ('<b>sinusoidal curve</b> – the wave-shaped graph of sine or cosine.', '[[Đường hình sin]] – đồ thị hình sóng của sin hoặc cos.'),
]
phrases = [
 ('<b>Find the period of the function.</b>', 'Tìm chu kì của hàm số.'),
 ('<b>State the domain and the range.</b>', 'Nêu tập xác định và tập giá trị.'),
 ('<b>Find the maximum and minimum values.</b>', 'Tìm giá trị lớn nhất và giá trị nhỏ nhất.'),
 ('<b>Is the function even, odd or neither?</b>', 'Hàm số chẵn, lẻ hay không chẵn không lẻ?'),
 ('<b>On which intervals is the function increasing?</b>', 'Hàm số đồng biến trên những khoảng nào?'),
 ('<b>Use the graph to solve the equation.</b>', 'Dùng đồ thị để giải phương trình.'),
]
review = (
 T(r'<b>Special values.</b> \(\sin 0=0\), \(\sin\dfrac{\pi}{2}=1\), \(\sin\pi=0\), \(\cos 0=1\), \(\cos\dfrac{\pi}{2}=0\), \(\cos\pi=-1\).', r'<b>Giá trị đặc biệt.</b> \(\sin 0=0\), \(\sin\dfrac{\pi}{2}=1\), \(\sin\pi=0\), \(\cos 0=1\), \(\cos\dfrac{\pi}{2}=0\), \(\cos\pi=-1\).') +
 T(r'<b>Definitions.</b> \(\tan x=\dfrac{\sin x}{\cos x}\) (\(\cos x\ne 0\)) and \(\cot x=\dfrac{\cos x}{\sin x}\) (\(\sin x\ne 0\)).', r'<b>Định nghĩa.</b> \(\tan x=\dfrac{\sin x}{\cos x}\) (\(\cos x\ne 0\)) và \(\cot x=\dfrac{\cos x}{\sin x}\) (\(\sin x\ne 0\)).') +
 T(r'<b>Parity.</b> \(f\) is even if \(f(-x)=f(x)\) and odd if \(f(-x)=-f(x)\). Example: \(x^2\) is even, \(x^3\) is odd.', r'<b>Tính chẵn lẻ.</b> \(f\) chẵn nếu \(f(-x)=f(x)\), lẻ nếu \(f(-x)=-f(x)\). Ví dụ: \(x^2\) chẵn, \(x^3\) lẻ.'))

theory = '<h3>5.1 %s</h3>' % TI('Trigonometric functions', 'Hàm số lượng giác')
theory += T(r'For every real number \(x\) (an angle in radians) there is exactly one value \(\sin x\) and exactly one value \(\cos x\). So \(y=\sin x\) and \(y=\cos x\) are functions defined on \(\mathbb{R}\). The functions \(y=\tan x\) and \(y=\cot x\) are defined by the quotients, so they are not defined everywhere.',
            r'Với mỗi số thực \(x\) (số đo góc theo radian) có đúng một giá trị \(\sin x\) và đúng một giá trị \(\cos x\). Vậy \(y=\sin x\) và \(y=\cos x\) là các hàm số xác định trên \(\mathbb{R}\). Các hàm số \(y=\tan x\) và \(y=\cot x\) được định nghĩa bằng thương nên không xác định ở mọi nơi.')
theory += BOX('blue', ('Domains', 'Tập xác định'),
  T(r'\(y=\sin x\) and \(y=\cos x\): \(D=\mathbb{R}\).', r'\(y=\sin x\) và \(y=\cos x\): \(D=\mathbb{R}\).'),
  T(r'\(y=\tan x\): \(D=\mathbb{R}\setminus\left\{\dfrac{\pi}{2}+k\pi,\ k\in\mathbb{Z}\right\}\) (where \(\cos x=0\) is excluded).', r'\(y=\tan x\): \(D=\mathbb{R}\setminus\left\{\dfrac{\pi}{2}+k\pi,\ k\in\mathbb{Z}\right\}\) (loại các điểm \(\cos x=0\)).'),
  T(r'\(y=\cot x\): \(D=\mathbb{R}\setminus\left\{k\pi,\ k\in\mathbb{Z}\right\}\) (where \(\sin x=0\) is excluded).', r'\(y=\cot x\): \(D=\mathbb{R}\setminus\left\{k\pi,\ k\in\mathbb{Z}\right\}\) (loại các điểm \(\sin x=0\)).'))

theory += '<h3>5.2 %s</h3>' % TI('Periodic functions and parity', 'Hàm số tuần hoàn. Hàm số chẵn, hàm số lẻ')
theory += BOX('mint', ('Periodic function', 'Hàm số tuần hoàn'),
  T(r'A function \(f\) is <b>periodic</b> if there is a number \(T\ne 0\) such that \(x\pm T\) is in the domain whenever \(x\) is, and \(f(x+T)=f(x)\). The smallest positive such \(T\) is the <b>period</b>.',
    r'Hàm số \(f\) gọi là [[hàm số tuần hoàn]] nếu có số \(T\ne 0\) sao cho với mọi \(x\) thuộc tập xác định thì \(x\pm T\) cũng thuộc tập xác định và \(f(x+T)=f(x)\). Số \(T\) dương nhỏ nhất như vậy gọi là [[chu kì]].'),
  T(r'\(\sin x\) and \(\cos x\) have period \(2\pi\); \(\tan x\) and \(\cot x\) have period \(\pi\).', r'\(\sin x\) và \(\cos x\) có chu kì \(2\pi\); \(\tan x\) và \(\cot x\) có chu kì \(\pi\).'),
  T(r'For \(y=\sin(bx+c)\) or \(y=\cos(bx+c)\) the period is \(\dfrac{2\pi}{|b|}\); for \(y=\tan(bx+c)\) or \(y=\cot(bx+c)\) it is \(\dfrac{\pi}{|b|}\).', r'Với \(y=\sin(bx+c)\) hoặc \(y=\cos(bx+c)\) chu kì là \(\dfrac{2\pi}{|b|}\); với \(y=\tan(bx+c)\) hoặc \(y=\cot(bx+c)\) chu kì là \(\dfrac{\pi}{|b|}\).'))
theory += BOX('mint', ('Even and odd functions', 'Hàm số chẵn, hàm số lẻ'),
  T(r'\(\cos x\) is <b>even</b>: \(\cos(-x)=\cos x\), so its graph is symmetric about the y-axis. \(\sin x\), \(\tan x\) and \(\cot x\) are <b>odd</b>: \(f(-x)=-f(x)\), so their graphs are symmetric about the origin.',
    r'\(\cos x\) là [[hàm số chẵn]]: \(\cos(-x)=\cos x\), đồ thị đối xứng qua trục tung. \(\sin x\), \(\tan x\), \(\cot x\) là [[hàm số lẻ]]: \(f(-x)=-f(x)\), đồ thị đối xứng qua gốc tọa độ.'),
  T(r'To test parity, the domain must also be symmetric about \(0\) (if \(x\) is in the domain, so is \(-x\)).', r'Khi xét tính chẵn lẻ, tập xác định phải đối xứng qua \(0\) (nếu \(x\) thuộc tập xác định thì \(-x\) cũng thuộc).'))

theory += '<h3>5.3 %s</h3>' % TI('The functions y = sin x and y = cos x', 'Hàm số y = sin x và y = cos x')
theory += GRAPH({'view': [-7, 7, -2, 2], 'pi': True, 'functions': [{'f': 'sin(x)', 'label': 'y = sin x'}, {'f': 'cos(x)', 'label': 'y = cos x'}], 'mark': {'intersections': [[0, 1]]}},
                cap=('The graphs of sin x and cos x are the same wave shifted by π/2. Two full periods are shown.', 'Đồ thị sin x và cos x là cùng một đường hình sin, lệch nhau π/2. Hình vẽ thể hiện hai chu kì.'),
                alt=('Graphs of sine and cosine with intersection points', ''), height=340)
theory += TABLE([('Property', 'Tính chất'), (r'\(y=\sin x\)', r'\(y=\sin x\)'), (r'\(y=\cos x\)', r'\(y=\cos x\)')], [
  [TI('domain', 'tập xác định'), r'\(\mathbb{R}\)', r'\(\mathbb{R}\)'], [TI('range', 'tập giá trị'), r'\([-1;1]\)', r'\([-1;1]\)'],
  [TI('period', 'chu kì'), r'\(2\pi\)', r'\(2\pi\)'], [TI('parity', 'tính chẵn lẻ'), TI('odd', 'lẻ'), TI('even', 'chẵn')],
  [TI('increasing on', 'đồng biến trên'), r'\(\left(-\dfrac{\pi}{2}+k2\pi;\ \dfrac{\pi}{2}+k2\pi\right)\)', r'\((-\pi+k2\pi;\ k2\pi)\)'],
  [TI('decreasing on', 'nghịch biến trên'), r'\(\left(\dfrac{\pi}{2}+k2\pi;\ \dfrac{3\pi}{2}+k2\pi\right)\)', r'\((k2\pi;\ \pi+k2\pi)\)']])
theory += GRAPH({'view': [-4.2, 4.2, -1.6, 1.6], 'pi': True, 'functions': [{'f': 'sin(x)', 'label': 'y = sin x'}], 'mark': {'extrema': [0]}, 'monotone': {'f': 0}},
                cap=('Green parts: sin x is increasing. Orange parts: sin x is decreasing. The turning points are the maximum and minimum values.', 'Phần xanh: sin x đồng biến. Phần cam: sin x nghịch biến. Các điểm đổi chiều là điểm có giá trị lớn nhất, nhỏ nhất.'),
                alt=('Sine curve coloured by increasing and decreasing parts', ''), height=320)
theory += BOX('mint', ('Effect of the numbers a, b, c, d', 'Ảnh hưởng của các số a, b, c, d'),
  M(r'y=a\sin(bx+c)+d'),
  T(r'The amplitude is \(|a|\); the period is \(\dfrac{2\pi}{|b|}\); \(c\) shifts the wave horizontally; \(d\) shifts it vertically. The maximum value is \(|a|+d\) and the minimum value is \(-|a|+d\).',
    r'[[Biên độ]] là \(|a|\); [[chu kì]] là \(\dfrac{2\pi}{|b|}\); \(c\) dời đồ thị theo chiều ngang; \(d\) dời theo chiều dọc. [[Giá trị lớn nhất]] là \(|a|+d\), [[giá trị nhỏ nhất]] là \(-|a|+d\).'))
theory += GRAPH({'view': [-7, 7, -3, 3], 'pi': True, 'params': [{'name': 'a', 'min': 0.5, 'max': 3, 'value': 2, 'step': 0.1}, {'name': 'b', 'min': 0.5, 'max': 3, 'value': 1, 'step': 0.1}, {'name': 'c', 'min': -3, 'max': 3, 'value': 0, 'step': 0.1}, {'name': 'd', 'min': -2, 'max': 2, 'value': 0, 'step': 0.1}], 'family': [{'a': 1, 'b': 1, 'c': 0, 'd': 0, '_label': 'y = sin x'}, {'a': 2, 'b': 1, 'c': 0, 'd': 0, '_label': 'y = 2 sin x'}, {'a': 1, 'b': 2, 'c': 0, 'd': 0, '_label': 'y = sin 2x'}],
                 'functions': [{'f': 'a*sin(b*x+c)+d', 'label': 'y = a·sin(bx + c) + d'}]},
                cap=('y = 2 sin x has amplitude 2 (period 2π); y = sin 2x keeps amplitude 1 but its period is π.', 'y = 2 sin x có biên độ 2 (chu kì 2π); y = sin 2x vẫn có biên độ 1 nhưng chu kì là π.'), alt=('Graphs of sin x, 2 sin x and sin 2x', ''), height=360)

theory += '<h3>5.4 %s</h3>' % TI('The functions y = tan x and y = cot x', 'Hàm số y = tan x và y = cot x')
theory += GRAPH({'view': [-5, 5, -6, 6], 'pi': True, 'functions': [{'f': 'tan(x)', 'label': 'y = tan x'}, {'f': '1/tan(x)', 'label': 'y = cot x'}],
                 'asymptotes': [{'type': 'v', 'x': PI / 2}, {'type': 'v', 'x': -PI / 2}, {'type': 'v', 'x': 3 * PI / 2}, {'type': 'v', 'x': -3 * PI / 2}, {'type': 'v', 'x': 0, 'color': '#c2410c'}, {'type': 'v', 'x': PI, 'color': '#c2410c'}, {'type': 'v', 'x': -PI, 'color': '#c2410c'}]},
                cap=('tan x is cut at π/2 + kπ; cot x is cut at kπ. The dashed lines are vertical asymptotes. Neither graph is joined across them.', 'tan x bị cắt tại π/2 + kπ; cot x bị cắt tại kπ. Các đường nét đứt là tiệm cận đứng; hai đồ thị không nối qua chúng.'),
                alt=('Graphs of tangent and cotangent with vertical asymptotes', ''), height=360)
theory += TABLE([('Property', 'Tính chất'), (r'\(y=\tan x\)', r'\(y=\tan x\)'), (r'\(y=\cot x\)', r'\(y=\cot x\)')], [
  [TI('domain', 'tập xác định'), r'\(\mathbb{R}\setminus\left\{\dfrac{\pi}{2}+k\pi\right\}\)', r'\(\mathbb{R}\setminus\{k\pi\}\)'],
  [TI('range', 'tập giá trị'), r'\(\mathbb{R}\)', r'\(\mathbb{R}\)'], [TI('period', 'chu kì'), r'\(\pi\)', r'\(\pi\)'], [TI('parity', 'tính chẵn lẻ'), TI('odd', 'lẻ'), TI('odd', 'lẻ')],
  [TI('monotonic on', 'tính đơn điệu'), TI(r'increasing on \(\left(-\dfrac{\pi}{2}+k\pi;\ \dfrac{\pi}{2}+k\pi\right)\)', r'đồng biến trên \(\left(-\dfrac{\pi}{2}+k\pi;\ \dfrac{\pi}{2}+k\pi\right)\)'),
   TI(r'decreasing on \((k\pi;\ \pi+k\pi)\)', r'nghịch biến trên \((k\pi;\ \pi+k\pi)\)')]])
theory += BOX('yellow', ('Watch out!', 'Lưu ý'),
  T(r'For \(y=\tan(bx)\) the period is \(\dfrac{\pi}{|b|}\), not \(\dfrac{2\pi}{|b|}\). The function \(\tan x\) is increasing on each interval where it is defined, but it is not increasing on the whole domain.',
    r'Với \(y=\tan(bx)\) chu kì là \(\dfrac{\pi}{|b|}\), không phải \(\dfrac{2\pi}{|b|}\). Hàm \(\tan x\) đồng biến trên từng khoảng mà nó xác định, nhưng không đồng biến trên cả tập xác định.'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Domain of tangent and cotangent', 'Tập xác định của hàm tan và cot'),
  T(r'Find the domain of (a) \(y=\tan\left(x-\dfrac{\pi}{3}\right)\); (b) \(y=\cot 2x\).', r'Tìm tập xác định của (a) \(y=\tan\left(x-\dfrac{\pi}{3}\right)\); (b) \(y=\cot 2x\).'),
  (r'\(\tan u\) needs \(u\ne\dfrac{\pi}{2}+k\pi\); \(\cot u\) needs \(u\ne k\pi\).', r'\(\tan u\) cần \(u\ne\dfrac{\pi}{2}+k\pi\); \(\cot u\) cần \(u\ne k\pi\).'),
  [T(r'(a) \(x-\dfrac{\pi}{3}\ne\dfrac{\pi}{2}+k\pi\Rightarrow x\ne\dfrac{5\pi}{6}+k\pi\).', r'(a) \(x-\dfrac{\pi}{3}\ne\dfrac{\pi}{2}+k\pi\Rightarrow x\ne\dfrac{5\pi}{6}+k\pi\).'),
   T(r'(b) \(2x\ne k\pi\Rightarrow x\ne\dfrac{k\pi}{2}\).', r'(b) \(2x\ne k\pi\Rightarrow x\ne\dfrac{k\pi}{2}\).')],
  r'(a) \(D=\mathbb{R}\setminus\left\{\dfrac{5\pi}{6}+k\pi\right\}\); (b) \(D=\mathbb{R}\setminus\left\{\dfrac{k\pi}{2}\right\}\).')
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Even, odd or neither', 'Chẵn, lẻ hay không chẵn không lẻ'),
  T(r'Decide whether each function is even, odd or neither: (a) \(y=x\sin x\); (b) \(y=\sin x+\cos x\).', r'Xét tính chẵn lẻ của mỗi hàm số: (a) \(y=x\sin x\); (b) \(y=\sin x+\cos x\).'),
  (r'The domain is \(\mathbb{R}\) (symmetric). Compare \(f(-x)\) with \(f(x)\) and \(-f(x)\).', r'Tập xác định là \(\mathbb{R}\) (đối xứng). So sánh \(f(-x)\) với \(f(x)\) và \(-f(x)\).'),
  [T(r'(a) \(f(-x)=(-x)\sin(-x)=(-x)(-\sin x)=x\sin x=f(x)\): even.', r'(a) \(f(-x)=(-x)\sin(-x)=(-x)(-\sin x)=x\sin x=f(x)\): hàm số chẵn.'),
   T(r'(b) \(f(-x)=-\sin x+\cos x\). At \(x=\dfrac{\pi}{4}\): \(f\left(\dfrac{\pi}{4}\right)=\sqrt2\) but \(f\left(-\dfrac{\pi}{4}\right)=0\), which is neither \(\sqrt2\) nor \(-\sqrt2\). So \(f(-x)\ne f(x)\) and \(f(-x)\ne -f(x)\).',
     r'(b) \(f(-x)=-\sin x+\cos x\). Tại \(x=\dfrac{\pi}{4}\): \(f\left(\dfrac{\pi}{4}\right)=\sqrt2\) còn \(f\left(-\dfrac{\pi}{4}\right)=0\), khác cả \(\sqrt2\) lẫn \(-\sqrt2\). Vậy \(f(-x)\ne f(x)\) và \(f(-x)\ne -f(x)\).')],
  r'(a) even; (b) neither even nor odd.')
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Maximum and minimum values', 'Giá trị lớn nhất, nhỏ nhất'),
  T(r'Find the maximum and minimum values of \(y=2-3\cos x\) and say for which \(x\) they occur.', r'Tìm giá trị lớn nhất và nhỏ nhất của \(y=2-3\cos x\) và cho biết đạt tại những \(x\) nào.'),
  (r'Start from \(-1\le\cos x\le 1\) and multiply by \(-3\) (the inequality turns around).', r'Xuất phát từ \(-1\le\cos x\le 1\) rồi nhân với \(-3\) (bất đẳng thức đổi chiều).'),
  [T(r'\(-3\le -3\cos x\le 3\), so \(-1\le 2-3\cos x\le 5\).', r'\(-3\le -3\cos x\le 3\) nên \(-1\le 2-3\cos x\le 5\).'),
   T(r'Maximum \(5\) when \(\cos x=-1\), i.e. \(x=\pi+k2\pi\).', r'Giá trị lớn nhất \(5\) khi \(\cos x=-1\), tức \(x=\pi+k2\pi\).'),
   T(r'Minimum \(-1\) when \(\cos x=1\), i.e. \(x=k2\pi\).', r'Giá trị nhỏ nhất \(-1\) khi \(\cos x=1\), tức \(x=k2\pi\).')],
  r'\(\max y=5\), \(\min y=-1\).')
examples += EXAMPLE(4, ('Advanced', 'Nâng cao'), ('Period of a sum', 'Chu kì của một tổng'),
  T(r'Show that \(2\pi\) is the period of \(y=\sin 2x+\cos 3x\).', r'Chứng tỏ \(2\pi\) là chu kì của \(y=\sin 2x+\cos 3x\).'),
  (r'\(\sin 2x\) has period \(\pi\); \(\cos 3x\) has period \(\dfrac{2\pi}{3}\). A common period must be a multiple of both.', r'\(\sin 2x\) có chu kì \(\pi\); \(\cos 3x\) có chu kì \(\dfrac{2\pi}{3}\). Chu kì chung phải là bội của cả hai.'),
  [T(r'The common multiples of \(\pi\) and \(\dfrac{2\pi}{3}\) are \(2\pi,4\pi,\dots\); the smallest is \(2\pi\) (\(2\pi=2\cdot\pi=3\cdot\dfrac{2\pi}{3}\)).', r'Các bội chung của \(\pi\) và \(\dfrac{2\pi}{3}\) là \(2\pi,4\pi,\dots\); nhỏ nhất là \(2\pi\) (\(2\pi=2\cdot\pi=3\cdot\dfrac{2\pi}{3}\)).'),
   T(r'Check: \(\sin(2x+4\pi)=\sin 2x\) and \(\cos(3x+6\pi)=\cos 3x\), so \(f(x+2\pi)=f(x)\).', r'Kiểm tra: \(\sin(2x+4\pi)=\sin 2x\) và \(\cos(3x+6\pi)=\cos 3x\) nên \(f(x+2\pi)=f(x)\).'),
   T(r'A smaller candidate fails: for \(T=\pi\), \(\cos(3x+3\pi)=-\cos 3x\), so \(f(x+\pi)\ne f(x)\).', r'Ứng viên nhỏ hơn không đúng: với \(T=\pi\), \(\cos(3x+3\pi)=-\cos 3x\) nên \(f(x+\pi)\ne f(x)\).')],
  r'The period is \(2\pi\).')
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Modelling the tide', 'Mô hình hóa thủy triều'),
  T(r'At a harbour the water depth (in metres) \(t\) hours after midnight is \(h(t)=4+1.5\sin\dfrac{\pi t}{6}\). Find the period, the highest and lowest depth, and the times in \([0;12]\) when \(h=4.75\).', r'Ở một bến cảng, độ sâu của nước (mét) sau \(t\) giờ kể từ nửa đêm là \(h(t)=4+1{,}5\sin\dfrac{\pi t}{6}\). Tìm chu kì, độ sâu lớn nhất và nhỏ nhất, và các thời điểm trong \([0;12]\) mà \(h=4{,}75\).') +
  GRAPH({'view': [-0.5, 13, 1, 7], 'functions': [{'f': '4+1.5*sin(pi*x/6)', 'label': 'h(t) = 4 + 1.5 sin(πt/6)'}, {'f': '4.75', 'label': 'h = 4.75', 'color': '#c2410c', 'width': 1.8}], 'mark': {'extrema': [0], 'intersections': [[0, 1]]}, 'xname': 't', 'yname': 'h'},
        alt=('Tide curve crossing the level 4.75', ''), height=300),
  (r'It has the form \(a\sin(bt)+d\) with \(a=1.5\), \(b=\dfrac{\pi}{6}\), \(d=4\).', r'Hàm có dạng \(a\sin(bt)+d\) với \(a=1{,}5\), \(b=\dfrac{\pi}{6}\), \(d=4\).'),
  [T(r'Period: \(\dfrac{2\pi}{\pi/6}=12\) hours.', r'Chu kì: \(\dfrac{2\pi}{\pi/6}=12\) giờ.'),
   T(r'Highest: \(4+1.5=5.5\) m (at \(t=3\)); lowest: \(4-1.5=2.5\) m (at \(t=9\)).', r'Lớn nhất: \(4+1{,}5=5{,}5\) m (tại \(t=3\)); nhỏ nhất: \(4-1{,}5=2{,}5\) m (tại \(t=9\)).'),
   T(r'\(h=4.75\) means \(\sin\dfrac{\pi t}{6}=0.5\), so \(\dfrac{\pi t}{6}=\dfrac{\pi}{6}\) or \(\dfrac{5\pi}{6}\) (in \([0;2\pi]\)).', r'\(h=4{,}75\) nghĩa là \(\sin\dfrac{\pi t}{6}=0{,}5\), nên \(\dfrac{\pi t}{6}=\dfrac{\pi}{6}\) hoặc \(\dfrac{5\pi}{6}\) (trong \([0;2\pi]\)).'),
   T(r'So \(t=1\) or \(t=5\): the depth is 4.75 m at 1:00 and at 5:00.', r'Vậy \(t=1\) hoặc \(t=5\): độ sâu là 4,75 m lúc 1 giờ và lúc 5 giờ.')],
  r'Period 12 h; highest 5.5 m, lowest 2.5 m; \(h=4.75\) at \(t=1\) and \(t=5\).')

# A1 chu kì; A2 tập xác định / tập giá trị; A3 giá trị lớn nhất; B4 tính chẵn lẻ; B5 tính đơn điệu; C6 giá trị lớn nhất/nhỏ nhất; C7 số nghiệm trên [0; 2π]
HN = ('Enter a whole number.', 'Nhập một số nguyên.'); HNUM = ('Enter a number.', 'Nhập một số.')
S1 = [
  [MCQ(1, (r'What is the period of \(y=\sin 2x\)?', r'Chu kì của \(y=\sin 2x\) là bao nhiêu?'), [r'\dfrac{\pi}{2}', r'\pi', r'2\pi', r'4\pi'], 'b', (r'Answer: b. \(\dfrac{2\pi}{2}=\pi\).', r'Đáp án b. \(\dfrac{2\pi}{2}=\pi\).')),
   MCQ(2, (r'What is the domain of \(y=\cot x\)?', r'Tập xác định của \(y=\cot x\) là gì?'), [r'\mathbb{R}', r'\mathbb{R}\setminus\{k\pi\}', r'\mathbb{R}\setminus\left\{\dfrac{\pi}{2}+k\pi\right\}', r'[-1;1]'], 'b', (r'Answer: b. \(\cot x\) is not defined where \(\sin x=0\), i.e. \(x=k\pi\).', r'Đáp án b. \(\cot x\) không xác định khi \(\sin x=0\), tức \(x=k\pi\).')),
   MCQ(3, (r'What is the maximum value of \(y=3\sin x\)?', r'Giá trị lớn nhất của \(y=3\sin x\) là bao nhiêu?'), ['1', '3', '-3', '6'], 'b', (r'Answer: b. \(\sin x\le 1\), so \(3\sin x\le 3\).', r'Đáp án b. \(\sin x\le 1\) nên \(3\sin x\le 3\).'))],
  [TF(4, (r'\(y=\cos x\) is an even function.', r'\(y=\cos x\) là hàm số chẵn.'), 'true', (r'True. \(\cos(-x)=\cos x\).', r'Đúng. \(\cos(-x)=\cos x\).')),
   TF(5, (r'\(y=\sin x\) is increasing on \(\left(0;\dfrac{\pi}{2}\right)\).', r'\(y=\sin x\) đồng biến trên \(\left(0;\dfrac{\pi}{2}\right)\).'), 'true', (r'True. \(\sin x\) is increasing on \(\left(-\dfrac{\pi}{2};\dfrac{\pi}{2}\right)\).', r'Đúng. \(\sin x\) đồng biến trên \(\left(-\dfrac{\pi}{2};\dfrac{\pi}{2}\right)\).'))],
  [SHORT(6, (r'Find the maximum value of \(y=2\sin x+1\).', r'Tìm giá trị lớn nhất của \(y=2\sin x+1\).'), '3', 'number', HNUM, (r'Answer: 3. \(2\cdot 1+1=3\).', r'Đáp số: 3. \(2\cdot 1+1=3\).')),
   SHORT(7, (r'How many solutions does \(\sin x=\dfrac12\) have in \([0;2\pi]\)?', r'Phương trình \(\sin x=\dfrac12\) có bao nhiêu nghiệm trong \([0;2\pi]\)?'), '2', 'number', HN, (r'Answer: 2. They are \(\dfrac{\pi}{6}\) and \(\dfrac{5\pi}{6}\).', r'Đáp số: 2. Đó là \(\dfrac{\pi}{6}\) và \(\dfrac{5\pi}{6}\).'))]]
S2 = [
  [MCQ(1, (r'What is the period of \(y=\cos\dfrac{x}{2}\)?', r'Chu kì của \(y=\cos\dfrac{x}{2}\) là bao nhiêu?'), [r'\pi', r'2\pi', r'4\pi', r'8\pi'], 'c', (r'Answer: c. \(\dfrac{2\pi}{1/2}=4\pi\).', r'Đáp án c. \(\dfrac{2\pi}{1/2}=4\pi\).')),
   MCQ(2, (r'What is the range of \(y=4\cos x\)?', r'Tập giá trị của \(y=4\cos x\) là gì?'), [r'[-1;1]', r'[0;4]', r'[-4;4]', r'\mathbb{R}'], 'c', (r'Answer: c. \(-4\le 4\cos x\le 4\).', r'Đáp án c. \(-4\le 4\cos x\le 4\).')),
   MCQ(3, (r'What is the maximum value of \(y=2-\cos x\)?', r'Giá trị lớn nhất của \(y=2-\cos x\) là bao nhiêu?'), ['1', '2', '3', '-1'], 'c', (r'Answer: c. The greatest value happens when \(\cos x=-1\): \(2-(-1)=3\).', r'Đáp án c. Giá trị lớn nhất đạt khi \(\cos x=-1\): \(2-(-1)=3\).'))],
  [TF(4, (r'\(y=\sin x\) is an even function.', r'\(y=\sin x\) là hàm số chẵn.'), 'false', (r'False. \(\sin(-x)=-\sin x\): it is odd.', r'Sai. \(\sin(-x)=-\sin x\): đây là hàm số lẻ.')),
   TF(5, (r'\(y=\cos x\) is increasing on \(\left(0;\dfrac{\pi}{2}\right)\).', r'\(y=\cos x\) đồng biến trên \(\left(0;\dfrac{\pi}{2}\right)\).'), 'false', (r'False. \(\cos x\) is decreasing on \((0;\pi)\).', r'Sai. \(\cos x\) nghịch biến trên \((0;\pi)\).'))],
  [SHORT(6, (r'Find the minimum value of \(y=3\cos x-2\).', r'Tìm giá trị nhỏ nhất của \(y=3\cos x-2\).'), '-5', 'number', HNUM, (r'Answer: \(-5\). \(3\cdot(-1)-2=-5\).', r'Đáp số: \(-5\). \(3\cdot(-1)-2=-5\).')),
   SHORT(7, (r'How many solutions does \(\cos x=-1\) have in \([0;2\pi]\)?', r'Phương trình \(\cos x=-1\) có bao nhiêu nghiệm trong \([0;2\pi]\)?'), '1', 'number', HN, (r'Answer: 1. Only \(x=\pi\).', r'Đáp số: 1. Chỉ có \(x=\pi\).'))]]
S3 = [
  [MCQ(1, (r'What is the period of \(y=\tan 3x\)?', r'Chu kì của \(y=\tan 3x\) là bao nhiêu?'), [r'\dfrac{\pi}{3}', r'\dfrac{2\pi}{3}', r'\pi', r'3\pi'], 'a', (r'Answer: a. \(\dfrac{\pi}{3}\), because the period of tangent is \(\pi\).', r'Đáp án a. \(\dfrac{\pi}{3}\), vì chu kì của hàm tan là \(\pi\).')),
   MCQ(2, (r'What is the domain of \(y=\tan 2x\)?', r'Tập xác định của \(y=\tan 2x\) là gì?'), [r'\mathbb{R}', r'\mathbb{R}\setminus\left\{\dfrac{\pi}{2}+k\pi\right\}', r'\mathbb{R}\setminus\{k\pi\}', r'\mathbb{R}\setminus\left\{\dfrac{\pi}{4}+\dfrac{k\pi}{2}\right\}'], 'd', (r'Answer: d. \(2x\ne\dfrac{\pi}{2}+k\pi\Rightarrow x\ne\dfrac{\pi}{4}+\dfrac{k\pi}{2}\).', r'Đáp án d. \(2x\ne\dfrac{\pi}{2}+k\pi\Rightarrow x\ne\dfrac{\pi}{4}+\dfrac{k\pi}{2}\).')),
   MCQ(3, (r'What is the maximum value of \(y=3-2\sin x\)?', r'Giá trị lớn nhất của \(y=3-2\sin x\) là bao nhiêu?'), ['1', '3', '5', '-1'], 'c', (r'Answer: c. The greatest value happens when \(\sin x=-1\): \(3+2=5\).', r'Đáp án c. Giá trị lớn nhất đạt khi \(\sin x=-1\): \(3+2=5\).'))],
  [TF(4, (r'\(y=\tan x\) is an odd function.', r'\(y=\tan x\) là hàm số lẻ.'), 'true', (r'True. \(\tan(-x)=-\tan x\) and the domain is symmetric.', r'Đúng. \(\tan(-x)=-\tan x\) và tập xác định đối xứng.')),
   TF(5, (r'\(y=\cot x\) is decreasing on \((0;\pi)\).', r'\(y=\cot x\) nghịch biến trên \((0;\pi)\).'), 'true', (r'True. \(\cot x\) is decreasing on every interval \((k\pi;\pi+k\pi)\).', r'Đúng. \(\cot x\) nghịch biến trên mỗi khoảng \((k\pi;\pi+k\pi)\).'))],
  [SHORT(6, (r'Find the maximum value of \(y=5-2\cos x\).', r'Tìm giá trị lớn nhất của \(y=5-2\cos x\).'), '7', 'number', HNUM, (r'Answer: 7. The greatest value is at \(\cos x=-1\): \(5+2=7\).', r'Đáp số: 7. Giá trị lớn nhất đạt khi \(\cos x=-1\): \(5+2=7\).')),
   SHORT(7, (r'How many solutions does \(\cos x=1.2\) have in \([0;2\pi]\)?', r'Phương trình \(\cos x=1{,}2\) có bao nhiêu nghiệm trong \([0;2\pi]\)?'), '0', 'number', HN, (r'Answer: 0, because \(\cos x\le 1\).', r'Đáp số: 0, vì \(\cos x\le 1\).'))]]
practice = LEVEL_PRACTICE([('A. Multiple Choice', 'A. Trắc nghiệm'), ('B. True or False', 'B. Đúng hoặc sai'), ('C. Short Answer', 'C. Trả lời ngắn')], {1: S1, 2: S2, 3: S3})

mistakes = [
 (r'<b>Periods.</b> Giving \(2\pi\) as the period of \(\tan x\). The period of \(\tan x\) is \(\pi\).', r'<b>Chu kì.</b> Cho rằng chu kì của \(\tan x\) là \(2\pi\). Chu kì của \(\tan x\) là \(\pi\).'),
 (r'<b>Using formulas.</b> Writing the period of \(y=\sin 2x\) as \(2\pi\cdot 2\). Correct: \(\dfrac{2\pi}{2}=\pi\).', r'<b>Dùng công thức.</b> Viết chu kì của \(y=\sin 2x\) là \(2\pi\cdot 2\). Đúng: \(\dfrac{2\pi}{2}=\pi\).'),
 (r'<b>Extreme values.</b> Forgetting that \(a\) can be negative: for \(y=3-2\sin x\), the maximum comes from \(\sin x=-1\).', r'<b>Giá trị lớn nhất, nhỏ nhất.</b> Quên rằng \(a\) có thể âm: với \(y=3-2\sin x\), giá trị lớn nhất đạt khi \(\sin x=-1\).'),
 (r'<b>Parity.</b> Deciding even or odd without checking that the domain is symmetric, or saying \(\sin x+\cos x\) is even because \(\cos x\) is.', r'<b>Chẵn lẻ.</b> Kết luận chẵn lẻ mà không kiểm tra tập xác định đối xứng, hoặc cho rằng \(\sin x+\cos x\) chẵn vì \(\cos x\) chẵn.'),
 (r'<b>Reading graphs.</b> Joining the branches of \(\tan x\) across its vertical asymptotes, or saying \(\tan x\) is increasing on its whole domain.', r'<b>Đọc đồ thị.</b> Nối các nhánh của \(\tan x\) qua các [[tiệm cận đứng]], hoặc nói \(\tan x\) đồng biến trên cả tập xác định.'),
]
summary = [
 (r'\(\sin x\) and \(\cos x\): domain \(\mathbb{R}\), range \([-1;1]\), period \(2\pi\); sine is odd, cosine is even.', r'\(\sin x\) và \(\cos x\): tập xác định \(\mathbb{R}\), tập giá trị \([-1;1]\), chu kì \(2\pi\); sin lẻ, cos chẵn.'),
 (r'\(\tan x\): period \(\pi\), undefined at \(\dfrac{\pi}{2}+k\pi\); \(\cot x\): period \(\pi\), undefined at \(k\pi\); both have range \(\mathbb{R}\) and are odd.', r'\(\tan x\): chu kì \(\pi\), không xác định tại \(\dfrac{\pi}{2}+k\pi\); \(\cot x\): chu kì \(\pi\), không xác định tại \(k\pi\); cả hai có tập giá trị \(\mathbb{R}\) và là hàm số lẻ.'),
 (r'For \(y=a\sin(bx+c)+d\): amplitude \(|a|\), period \(\dfrac{2\pi}{|b|}\), maximum \(|a|+d\), minimum \(-|a|+d\).', r'Với \(y=a\sin(bx+c)+d\): biên độ \(|a|\), chu kì \(\dfrac{2\pi}{|b|}\), lớn nhất \(|a|+d\), nhỏ nhất \(-|a|+d\).'),
 ('Sine increases on (−π/2; π/2) and decreases on (π/2; 3π/2); cosine decreases on (0; π) and increases on (π; 2π); tan increases and cot decreases on every interval of their domain.', 'sin đồng biến trên (−π/2; π/2), nghịch biến trên (π/2; 3π/2); cos nghịch biến trên (0; π), đồng biến trên (π; 2π); tan đồng biến, cot nghịch biến trên từng khoảng thuộc tập xác định.'),
 ('Key English phrases: find the period; state the domain and range; find the maximum value; on which intervals is the function increasing.', 'Cụm tiếng Anh cần nhớ: find the period (tìm chu kì); state the domain and range (nêu tập xác định và tập giá trị); find the maximum value (tìm giá trị lớn nhất); on which intervals is the function increasing (đồng biến trên những khoảng nào).'),
]
checks = [
 ('I can state the domain, range, period and parity of sine, cosine, tangent and cotangent.', 'Tôi nêu được tập xác định, tập giá trị, chu kì và tính chẵn lẻ của sin, cos, tan, cot.'),
 ('I can find the amplitude and the period of y = a sin(bx + c) + d.', 'Tôi tìm được biên độ và chu kì của y = a sin(bx + c) + d.'),
 ('I can say where sine, cosine, tangent and cotangent are increasing or decreasing.', 'Tôi nói được các khoảng đồng biến, nghịch biến của sin, cos, tan, cot.'),
 ('I can find maximum and minimum values and use a sine model for a periodic situation.', 'Tôi tìm được giá trị lớn nhất, nhỏ nhất và dùng hàm sin để mô hình hóa tình huống tuần hoàn.'),
 STD_SUMMARY_CHECK_EN(),
]

lesson(id=LID, title_en='Trigonometric Functions', title_vi='Hàm số lượng giác', topic=TOPIC,
       folder='trigonometric-functions', file='graphs-and-properties',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Domain, range, period, parity, graphs and monotonicity of sine, cosine, tangent and cotangent; periodic models.', level='Intermediate', minutes=65,
       description_vi='Bài 3 – Tập xác định, tập giá trị, chu kì, tính chẵn lẻ, đồ thị và tính đơn điệu của sin, cos, tan, cot; mô hình hóa hiện tượng tuần hoàn.',
       tags_vi=['hàm số lượng giác', 'chu kì', 'đồ thị', 'sin', 'cos', 'tan', 'cot', 'đồng biến', 'nghịch biến', 'thủy triều'],
       prerequisites=['g11-trigf-03'], tags=['trigonometric functions', 'period', 'graph', 'sine', 'cosine', 'tangent', 'cotangent', 'monotonic'], order=30)
