# -*- coding: utf-8 -*-
"""Nội dung bài g11-trigf-01 = Toán 11 KNTT, Chương I, Bài 1: Giá trị lượng giác của góc lượng giác – CHỈ NỘI DUNG.
Bố cục do config/model.json quyết định. Bài tập: mỗi mức một bộ riêng, cùng dạng, khác số liệu (LEVEL_PRACTICE).
Mã ngân hàng câu hỏi: TOAN11-C1-B01."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *

LID = 'g11-trigf-01'
CAT = 'Trigonometric Functions'
TOPIC = (CAT, 'Hàm số lượng giác')
CV = 'Hàm số lượng giác'
PI = math.pi

ensure_vocab([
 ('g11-oriented-angle', 'oriented angle', 'góc lượng giác', CV, 'An oriented angle has a direction of rotation.', r'\((Ou,Ov)\)'),
 ('g11-initial-side', 'initial side', 'tia đầu', CV, 'The ray Ou is the initial side.', ''),
 ('g11-terminal-side', 'terminal side', 'tia cuối', CV, 'The ray Ov is the terminal side.', ''),
 ('g11-radian', 'radian', 'radian', CV, 'Convert 180 degrees to radians.', r'\(\text{rad}\)'),
 ('g11-degree', 'degree', 'độ', CV, 'A full turn is 360 degrees.', r'\(^\circ\)'),
 ('g11-unit-circle', 'unit circle', 'đường tròn đơn vị', CV, 'The unit circle has radius 1.', ''),
 ('g11-trig-circle', 'trigonometric circle', 'đường tròn lượng giác', CV, 'Points on the trigonometric circle are given by angles.', ''),
 ('g11-arc-length', 'arc length', 'độ dài cung', CV, 'Find the arc length.', ''),
 ('g11-central-angle', 'central angle', 'góc ở tâm', CV, 'The central angle is 2 radians.', ''),
 ('g11-sine', 'sine', 'sin', CV, 'The sine of the angle is the y-coordinate.', r'\(\sin\alpha\)'),
 ('g11-cosine', 'cosine', 'cos', CV, 'The cosine of the angle is the x-coordinate.', r'\(\cos\alpha\)'),
 ('g11-tangent-trig', 'tangent', 'tan', CV, 'The tangent is sine divided by cosine.', r'\(\tan\alpha\)'),
 ('g11-cotangent', 'cotangent', 'cot', CV, 'The cotangent is cosine divided by sine.', r'\(\cot\alpha\)'),
 ('g11-trig-value', 'trigonometric value', 'giá trị lượng giác', CV, 'Find the trigonometric values of the angle.', ''),
 ('g11-quadrant', 'quadrant', 'góc phần tư', CV, 'The angle is in the second quadrant.', ''),
 ('g11-opposite-angles', 'opposite angles', 'góc đối', CV, 'The angles alpha and minus alpha are opposite angles.', ''),
 ('g11-supplementary', 'supplementary angles', 'góc bù', CV, 'Supplementary angles add up to pi.', ''),
 ('g11-complementary', 'complementary angles', 'góc phụ', CV, 'Complementary angles add up to pi over 2.', ''),
])
load_vocab()

# ---- kiểm tra số liệu ----
assert abs(135 * PI / 180 - 3 * PI / 4) < 1e-12 and abs(5 * PI / 6 * 180 / PI - 150) < 1e-9
assert abs(6 * (120 * PI / 180) - 4 * PI) < 1e-9 and abs(4 * PI - 12.566370614) < 1e-8
a = 2 * PI - math.acos(0.6)        # góc phần tư IV có cos = 3/5
assert abs(math.cos(a) - 0.6) < 1e-12 and abs(math.sin(a) + 0.8) < 1e-12 and abs(math.tan(a) + 4 / 3) < 1e-12
assert abs((-11 * PI / 6 + 2 * PI) - PI / 6) < 1e-12 and abs((-11 * PI / 6) - (PI / 6) + 2 * PI) < 1e-12
assert abs(math.cos(5 * PI / 6) + math.sqrt(3) / 2) < 1e-12 and abs(math.sin(7 * PI / 6) + 0.5) < 1e-12 and abs(math.tan(-PI / 3) + math.sqrt(3)) < 1e-12
assert abs(math.cos(2 * PI / 3) + 0.5) < 1e-12 and abs(math.sin(-PI / 6) + 0.5) < 1e-12
# các câu của bài tập: (cos, góc phần tư) -> sin
for c, s, lo, hi in ((0.6, -0.8, 3 * PI / 2, 2 * PI), (-0.6, -0.8, PI, 3 * PI / 2)):
    x = math.acos(c) if s > 0 else 2 * PI - math.acos(c); assert lo < x < hi and abs(math.sin(x) - s) < 1e-12
x = math.asin(0.6); x = PI - x; assert PI / 2 < x < PI and abs(math.cos(x) + 0.8) < 1e-12
assert abs((-PI / 3) - (5 * PI / 3) + 2 * PI) < 1e-12 and abs((7 * PI / 6) - (-5 * PI / 6) - 2 * PI) < 1e-12

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 60 minutes', 'khoảng 60 phút'),
            before=('trigonometric ratios of acute angles, the circle (grades 9–10)', 'tỉ số lượng giác của góc nhọn, đường tròn (lớp 9–10)'))
goals = [
 ('describe an oriented angle and its measure in degrees and in radians;', 'mô tả [[góc lượng giác]] và số đo của nó bằng [[độ]] và [[radian]];'),
 ('convert between degrees and radians and compute arc length;', 'đổi giữa độ và radian, tính [[độ dài cung]];'),
 ('define sin, cos, tan and cot with the trigonometric circle;', 'định nghĩa [[sin]], [[cos]], [[tan]], [[cot]] bằng [[đường tròn lượng giác]];'),
 ('use the values of special angles and the sign in each quadrant;', 'dùng giá trị của các góc đặc biệt và dấu trong từng [[góc phần tư]];'),
 (r'use the basic identities and the values of related angles (opposite, supplementary, complementary).', r'dùng các hệ thức cơ bản và giá trị của các góc liên quan đặc biệt ([[góc đối]], [[góc bù]], [[góc phụ]]).'),
]
vocab = [
 ('<b>oriented angle</b> – an angle with a direction of rotation from the initial side to the terminal side.', '[[Góc lượng giác]] – góc có kèm chiều quay từ [[tia đầu]] đến [[tia cuối]].'),
 ('<b>initial side, terminal side</b> – the starting ray and the ending ray of the rotation.', '[[Tia đầu]], [[tia cuối]] – tia bắt đầu và tia kết thúc của phép quay.'),
 ('<b>radian</b> – the angle at the centre of a circle that cuts an arc as long as the radius.', '[[Radian]] – góc ở tâm của đường tròn chắn cung có độ dài bằng bán kính.'),
 (r'<b>degree</b> – one 360th of a full turn: \(1^\circ=\dfrac{\pi}{180}\) rad.', r'[[Độ]] – một phần 360 của vòng tròn: \(1^\circ=\dfrac{\pi}{180}\) rad.'),
 ('<b>trigonometric circle</b> – the circle of radius 1, centre at the origin, with a chosen direction of rotation.', '[[Đường tròn lượng giác]] – đường tròn bán kính 1, tâm ở gốc tọa độ, có chọn chiều quay.'),
 ('<b>arc length</b> – the length of part of a circle.', '[[Độ dài cung]] – độ dài một phần của đường tròn.'),
 ('<b>sine, cosine, tangent, cotangent</b> – the four trigonometric functions of an angle.', '[[sin]], [[cos]], [[tan]], [[cot]] – bốn giá trị lượng giác của một góc.'),
 ('<b>quadrant</b> – one of the four parts of the coordinate plane.', '[[Góc phần tư]] – một trong bốn phần của mặt phẳng tọa độ.'),
 (r'<b>opposite, supplementary, complementary angles</b> – pairs with sum \(0\), \(\pi\), \(\dfrac{\pi}{2}\).', r'[[Góc đối]], [[góc bù]], [[góc phụ]] – các cặp góc có tổng bằng \(0\), \(\pi\), \(\dfrac{\pi}{2}\).'),
]
phrases = [
 ('<b>Convert the angle to radians.</b>', 'Đổi số đo góc sang radian.'),
 ('<b>Find the length of the arc.</b>', 'Tìm độ dài cung.'),
 (r'<b>Find the exact value of \(\sin\dfrac{\pi}{3}\).</b>', r'Tìm giá trị chính xác của \(\sin\dfrac{\pi}{3}\).'),
 ('<b>In which quadrant is the angle?</b>', 'Góc nằm ở góc phần tư nào?'),
 (r'<b>Use the identity to find \(\sin\alpha\).</b>', r'Dùng đẳng thức để tìm \(\sin\alpha\).'),
 (r'<b>Give your answer in terms of \(\pi\).</b>', r'Viết đáp số theo \(\pi\).'),
]
review = (
 T(r'<b>Right triangle.</b> For an acute angle \(\alpha\): \(\sin\alpha=\dfrac{\text{opposite}}{\text{hypotenuse}}\), \(\cos\alpha=\dfrac{\text{adjacent}}{\text{hypotenuse}}\), \(\tan\alpha=\dfrac{\text{opposite}}{\text{adjacent}}\).',
   r'<b>Tam giác vuông.</b> Với góc nhọn \(\alpha\): \(\sin\alpha=\dfrac{\text{đối}}{\text{huyền}}\), \(\cos\alpha=\dfrac{\text{kề}}{\text{huyền}}\), \(\tan\alpha=\dfrac{\text{đối}}{\text{kề}}\).') +
 T(r'<b>Circle.</b> The circumference of a circle of radius \(R\) is \(2\pi R\).', r'<b>Đường tròn.</b> Chu vi đường tròn bán kính \(R\) là \(2\pi R\).'))

theory = '<h3>5.1 %s</h3>' % TI('Oriented angles', 'Góc lượng giác và số đo')
theory += BOX('mint', ('Definition', 'Định nghĩa'),
  T(r'Rotate a ray \(Ou\) about \(O\) until it reaches the ray \(Ov\). The rotation has a <b>direction</b>: anticlockwise is positive, clockwise is negative. The result is an <b>oriented angle</b> with initial side \(Ou\) and terminal side \(Ov\), written \((Ou,Ov)\).',
    r'Quay tia \(Ou\) quanh \(O\) đến khi trùng tia \(Ov\). Phép quay có <b>chiều</b>: ngược chiều kim đồng hồ là chiều dương, cùng chiều kim đồng hồ là chiều âm. Kết quả là một <b>[[góc lượng giác]]</b> có [[tia đầu]] \(Ou\), [[tia cuối]] \(Ov\), kí hiệu \((Ou,Ov)\).'),
  T(r'If one measure of \((Ou,Ov)\) is \(\alpha\), every measure has the form', r'Nếu một số đo của \((Ou,Ov)\) là \(\alpha\) thì mọi số đo của nó có dạng'),
  M(r'\alpha+k\cdot 360^\circ\quad\text{or}\quad \alpha+k\cdot 2\pi\ \ (k\in\mathbb{Z}).'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'),
  T(r'Different angles such as \(\dfrac{\pi}{3}\) and \(\dfrac{7\pi}{3}\) have the same terminal side, but they are different oriented angles. Two angles have the same terminal side exactly when they differ by a multiple of \(2\pi\).',
    r'Các góc như \(\dfrac{\pi}{3}\) và \(\dfrac{7\pi}{3}\) có cùng tia cuối nhưng là những góc lượng giác khác nhau. Hai góc có cùng tia cuối khi và chỉ khi hiệu của chúng là bội của \(2\pi\).'))

theory += '<h3>5.2 %s</h3>' % TI('Radians and arc length', 'Radian và độ dài cung')
theory += BOX('mint', ('Definition', 'Định nghĩa'),
  T(r'An angle of <b>1 radian</b> is the central angle that subtends an arc as long as the radius. A half turn is \(\pi\) radians.', r'Góc <b>1 [[radian]]</b> là [[góc ở tâm]] chắn cung có độ dài bằng bán kính. Nửa vòng tròn là \(\pi\) radian.'),
  M(r'180^\circ=\pi\ \text{rad},\qquad \alpha^\circ=\alpha\cdot\dfrac{\pi}{180}\ \text{rad},\qquad x\ \text{rad}=x\cdot\dfrac{180^\circ}{\pi}'),
  T(r'<b>Arc length:</b> on a circle of radius \(R\), a central angle \(\alpha\) (in radians) subtends an arc of length \(\ell=R\alpha\).', r'<b>[[Độ dài cung]]:</b> trên đường tròn bán kính \(R\), góc ở tâm \(\alpha\) (radian) chắn cung dài \(\ell=R\alpha\).'))
theory += TABLE([('Degrees', 'Độ'), ('Radians', 'Radian')], [
  [r'\(0^\circ\)', r'\(0\)'], [r'\(30^\circ\)', r'\(\dfrac{\pi}{6}\)'], [r'\(45^\circ\)', r'\(\dfrac{\pi}{4}\)'], [r'\(60^\circ\)', r'\(\dfrac{\pi}{3}\)'],
  [r'\(90^\circ\)', r'\(\dfrac{\pi}{2}\)'], [r'\(180^\circ\)', r'\(\pi\)'], [r'\(270^\circ\)', r'\(\dfrac{3\pi}{2}\)'], [r'\(360^\circ\)', r'\(2\pi\)']])

theory += '<h3>5.3 %s</h3>' % TI('The trigonometric circle and trigonometric values', 'Đường tròn lượng giác và giá trị lượng giác')
theory += BOX('mint', ('Definition', 'Định nghĩa'),
  T(r'On the trigonometric circle, let \(P\) be the point reached after turning by the angle \(\alpha\) from \(I(1;0)\). Then', r'Trên [[đường tròn lượng giác]], gọi \(P\) là điểm có được sau khi quay góc \(\alpha\) từ \(I(1;0)\). Khi đó'),
  M(r'P(\cos\alpha;\ \sin\alpha),\qquad \tan\alpha=\dfrac{\sin\alpha}{\cos\alpha}\ (\cos\alpha\ne 0),\qquad \cot\alpha=\dfrac{\cos\alpha}{\sin\alpha}\ (\sin\alpha\ne 0).'))
theory += GEO({'view': [-1.8, 1.8, -1.4, 1.4], 'axes': True, 'equal': True, 'steps': [
    {'type': 'point', 'id': 'O', 'at': [0, 0], 'fixed': True}, {'type': 'point', 'id': 'I', 'at': [1, 0], 'fixed': True, 'off': [6, -16]},
    {'type': 'circle', 'id': 'c', 'center': 'O', 'through': 'I'}, {'type': 'line', 'id': 'Ox', 'through': ['O', 'I'], 'style': {'visible': False}},
    {'type': 'glider', 'id': 'P', 'at': [0.5, math.sqrt(3) / 2], 'on': 'c'}, {'type': 'segment', 'through': ['O', 'P']},
    {'type': 'altitude', 'from': 'P', 'to': 'Ox', 'foot': 'H', 'footName': 'H', 'style': {'strokeColor': '#c2410c', 'strokeWidth': 3, 'dash': 0}},
    {'type': 'segment', 'through': ['O', 'H'], 'style': {'strokeColor': '#1d4ed8', 'strokeWidth': 3}},
    {'type': 'arc', 'points': ['O', 'I', 'P']}, {'type': 'angle', 'points': ['I', 'O', 'P'], 'radius': 0.3}]},
  cap=('P is the point of angle α on the circle. OH = cos α (blue) and PH = sin α (orange); PH is a true perpendicular to the x-axis.', 'P là điểm biểu diễn góc α trên đường tròn. OH = cos α (xanh), PH = sin α (cam); PH là đường vuông góc thật với trục hoành.'),
  alt=('Trigonometric circle with a point P and its projection H on the x-axis', ''), height=380)
theory += TABLE([('Quadrant', 'Góc phần tư'), (r'sin', 'sin'), ('cos', 'cos'), ('tan, cot', 'tan, cot')], [
  [r'I \((0;\frac{\pi}{2})\)', '+', '+', '+'], [r'II \((\frac{\pi}{2};\pi)\)', '+', '−', '−'],
  [r'III \((\pi;\frac{3\pi}{2})\)', '−', '−', '+'], [r'IV \((\frac{3\pi}{2};2\pi)\)', '−', '+', '−']])
theory += TABLE([(r'\(\alpha\)', r'\(\alpha\)'), ('sin', 'sin'), ('cos', 'cos'), ('tan', 'tan'), ('cot', 'cot')], [
  [r'\(0\)', r'\(0\)', r'\(1\)', r'\(0\)', TI('undefined', 'không xác định')],
  [r'\(\dfrac{\pi}{6}\)', r'\(\dfrac12\)', r'\(\dfrac{\sqrt3}{2}\)', r'\(\dfrac{\sqrt3}{3}\)', r'\(\sqrt3\)'],
  [r'\(\dfrac{\pi}{4}\)', r'\(\dfrac{\sqrt2}{2}\)', r'\(\dfrac{\sqrt2}{2}\)', r'\(1\)', r'\(1\)'],
  [r'\(\dfrac{\pi}{3}\)', r'\(\dfrac{\sqrt3}{2}\)', r'\(\dfrac12\)', r'\(\sqrt3\)', r'\(\dfrac{\sqrt3}{3}\)'],
  [r'\(\dfrac{\pi}{2}\)', r'\(1\)', r'\(0\)', TI('undefined', 'không xác định'), r'\(0\)']])

theory += '<h3>5.4 %s</h3>' % TI('Basic identities', 'Các hệ thức lượng giác cơ bản')
theory += BOX('blue', ('Basic identities', 'Hệ thức cơ bản'),
  M(r'\sin^2\alpha+\cos^2\alpha=1,\qquad \tan\alpha\cdot\cot\alpha=1,'),
  M(r'1+\tan^2\alpha=\dfrac{1}{\cos^2\alpha}\ (\cos\alpha\ne0),\qquad 1+\cot^2\alpha=\dfrac{1}{\sin^2\alpha}\ (\sin\alpha\ne0).'),
  T(r'The first one follows from \(P(\cos\alpha;\sin\alpha)\) lying on the circle \(x^2+y^2=1\); the others follow by dividing by \(\cos^2\alpha\) or \(\sin^2\alpha\).', r'Hệ thức đầu suy ra từ việc \(P(\cos\alpha;\sin\alpha)\) nằm trên đường tròn \(x^2+y^2=1\); các hệ thức còn lại có được khi chia cho \(\cos^2\alpha\) hoặc \(\sin^2\alpha\).'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'),
  T(r'Write \(\sin^2\alpha\) for \((\sin\alpha)^2\). When the angle has no unit, it is in radians.', r'Viết \(\sin^2\alpha\) cho \((\sin\alpha)^2\). Góc không ghi đơn vị được hiểu là radian.'))

theory += '<h3>5.5 %s</h3>' % TI('Values of related angles', 'Giá trị lượng giác của các góc liên quan đặc biệt')
theory += TABLE([('Relation', 'Quan hệ'), ('sin', 'sin'), ('cos', 'cos'), ('tan', 'tan'), ('cot', 'cot')], [
  [TI('Opposite angles: \\(-\\alpha\\)', '[[Góc đối]]: \\(-\\alpha\\)'), r'\(-\sin\alpha\)', r'\(\cos\alpha\)', r'\(-\tan\alpha\)', r'\(-\cot\alpha\)'],
  [TI('Supplementary angles: \\(\\pi-\\alpha\\)', '[[Góc bù]]: \\(\\pi-\\alpha\\)'), r'\(\sin\alpha\)', r'\(-\cos\alpha\)', r'\(-\tan\alpha\)', r'\(-\cot\alpha\)'],
  [TI('Differ by \\(\\pi\\): \\(\\alpha+\\pi\\)', 'Hơn kém \\(\\pi\\): \\(\\alpha+\\pi\\)'), r'\(-\sin\alpha\)', r'\(-\cos\alpha\)', r'\(\tan\alpha\)', r'\(\cot\alpha\)'],
  [TI('Complementary angles: \\(\\frac{\\pi}{2}-\\alpha\\)', '[[Góc phụ]]: \\(\\frac{\\pi}{2}-\\alpha\\)'), r'\(\cos\alpha\)', r'\(\sin\alpha\)', r'\(\cot\alpha\)', r'\(\tan\alpha\)']])
theory += T(r'<b>Tip:</b> to find a value, first add or subtract a multiple of \(2\pi\) to reach an angle in \([0;2\pi)\), then use the table above.', r'<b>Mẹo:</b> muốn tính một giá trị, trước hết cộng hoặc trừ bội của \(2\pi\) để đưa góc về \([0;2\pi)\), rồi dùng bảng trên.')

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Converting angles', 'Đổi số đo góc'),
  T(r'(a) Convert \(135^\circ\) to radians. (b) Convert \(\dfrac{5\pi}{6}\) rad to degrees.', r'(a) Đổi \(135^\circ\) sang radian. (b) Đổi \(\dfrac{5\pi}{6}\) rad sang độ.'),
  (r'Use \(180^\circ=\pi\) rad: multiply by \(\dfrac{\pi}{180}\) to go to radians, by \(\dfrac{180}{\pi}\) to go to degrees.', r'Dùng \(180^\circ=\pi\) rad: nhân với \(\dfrac{\pi}{180}\) để sang radian, nhân với \(\dfrac{180}{\pi}\) để sang độ.'),
  [T(r'(a) \(135\cdot\dfrac{\pi}{180}=\dfrac{3\pi}{4}\).', r'(a) \(135\cdot\dfrac{\pi}{180}=\dfrac{3\pi}{4}\).'), T(r'(b) \(\dfrac{5\pi}{6}\cdot\dfrac{180}{\pi}=150\), so \(150^\circ\).', r'(b) \(\dfrac{5\pi}{6}\cdot\dfrac{180}{\pi}=150\) nên \(150^\circ\).')],
  r'(a) \(\dfrac{3\pi}{4}\); (b) \(150^\circ\).')
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Oriented angles', 'Góc lượng giác'),
  T(r'Find the measure in \([0;2\pi)\) of the oriented angle whose measure is \(-\dfrac{11\pi}{6}\), and write all its measures.', r'Tìm số đo thuộc \([0;2\pi)\) của góc lượng giác có số đo \(-\dfrac{11\pi}{6}\) và viết mọi số đo của nó.'),
  (r'Add a multiple of \(2\pi\) until the result lies in \([0;2\pi)\).', r'Cộng thêm bội của \(2\pi\) cho đến khi kết quả thuộc \([0;2\pi)\).'),
  [T(r'\(-\dfrac{11\pi}{6}+2\pi=\dfrac{\pi}{6}\in[0;2\pi)\).', r'\(-\dfrac{11\pi}{6}+2\pi=\dfrac{\pi}{6}\in[0;2\pi)\).'),
   T(r'All measures: \(\dfrac{\pi}{6}+k2\pi\), \(k\in\mathbb{Z}\).', r'Mọi số đo: \(\dfrac{\pi}{6}+k2\pi\), \(k\in\mathbb{Z}\).')],
  r'\(\dfrac{\pi}{6}\); all measures \(\dfrac{\pi}{6}+k2\pi\).')
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Arc length', 'Độ dài cung'),
  T(r'A circle has radius \(6\) cm. Find the length of the arc subtended by a central angle of \(120^\circ\).', r'Một đường tròn có bán kính \(6\) cm. Tính độ dài cung chắn bởi góc ở tâm \(120^\circ\).'),
  (r'First change the angle to radians, then use \(\ell=R\alpha\).', r'Đổi góc sang radian trước, rồi dùng \(\ell=R\alpha\).'),
  [T(r'\(120^\circ=\dfrac{2\pi}{3}\) rad.', r'\(120^\circ=\dfrac{2\pi}{3}\) rad.'), T(r'\(\ell=6\cdot\dfrac{2\pi}{3}=4\pi\approx 12.57\) cm.', r'\(\ell=6\cdot\dfrac{2\pi}{3}=4\pi\approx 12{,}57\) cm.')],
  r'\(\ell=4\pi\approx 12.57\) cm.')
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Related angles', 'Góc liên quan đặc biệt'),
  T(r'Find \(\cos\dfrac{5\pi}{6}\), \(\sin\dfrac{7\pi}{6}\) and \(\tan\left(-\dfrac{\pi}{3}\right)\).', r'Tính \(\cos\dfrac{5\pi}{6}\), \(\sin\dfrac{7\pi}{6}\) và \(\tan\left(-\dfrac{\pi}{3}\right)\).'),
  (r'Write each angle as \(\pi-\alpha\), \(\pi+\alpha\) or \(-\alpha\) with a special angle \(\alpha\).', r'Viết mỗi góc dưới dạng \(\pi-\alpha\), \(\pi+\alpha\) hoặc \(-\alpha\) với \(\alpha\) là góc đặc biệt.'),
  [T(r'\(\cos\dfrac{5\pi}{6}=\cos\left(\pi-\dfrac{\pi}{6}\right)=-\cos\dfrac{\pi}{6}=-\dfrac{\sqrt3}{2}\).', r'\(\cos\dfrac{5\pi}{6}=\cos\left(\pi-\dfrac{\pi}{6}\right)=-\cos\dfrac{\pi}{6}=-\dfrac{\sqrt3}{2}\).'),
   T(r'\(\sin\dfrac{7\pi}{6}=\sin\left(\pi+\dfrac{\pi}{6}\right)=-\sin\dfrac{\pi}{6}=-\dfrac12\).', r'\(\sin\dfrac{7\pi}{6}=\sin\left(\pi+\dfrac{\pi}{6}\right)=-\sin\dfrac{\pi}{6}=-\dfrac12\).'),
   T(r'\(\tan\left(-\dfrac{\pi}{3}\right)=-\tan\dfrac{\pi}{3}=-\sqrt3\).', r'\(\tan\left(-\dfrac{\pi}{3}\right)=-\tan\dfrac{\pi}{3}=-\sqrt3\).')],
  r'\(-\dfrac{\sqrt3}{2}\); \(-\dfrac12\); \(-\sqrt3\).')
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Using the identity', 'Dùng hệ thức cơ bản'),
  T(r'Given \(\cos\alpha=\dfrac35\) and \(\dfrac{3\pi}{2}\lt\alpha\lt 2\pi\), find \(\sin\alpha\), \(\tan\alpha\) and \(\cot\alpha\).', r'Cho \(\cos\alpha=\dfrac35\) và \(\dfrac{3\pi}{2}\lt\alpha\lt 2\pi\). Tính \(\sin\alpha\), \(\tan\alpha\) và \(\cot\alpha\).'),
  (r'Use \(\sin^2\alpha=1-\cos^2\alpha\), then choose the sign from the quadrant.', r'Dùng \(\sin^2\alpha=1-\cos^2\alpha\), rồi chọn dấu theo góc phần tư.'),
  [T(r'\(\sin^2\alpha=1-\dfrac{9}{25}=\dfrac{16}{25}\), so \(\sin\alpha=\pm\dfrac45\).', r'\(\sin^2\alpha=1-\dfrac{9}{25}=\dfrac{16}{25}\) nên \(\sin\alpha=\pm\dfrac45\).'),
   T(r'\(\alpha\) is in quadrant IV, where sine is negative: \(\sin\alpha=-\dfrac45\).', r'\(\alpha\) thuộc góc phần tư IV, nơi sin âm: \(\sin\alpha=-\dfrac45\).'),
   T(r'\(\tan\alpha=\dfrac{-4/5}{3/5}=-\dfrac43\), \(\cot\alpha=-\dfrac34\).', r'\(\tan\alpha=\dfrac{-4/5}{3/5}=-\dfrac43\), \(\cot\alpha=-\dfrac34\).')],
  r'\(\sin\alpha=-\dfrac45\), \(\tan\alpha=-\dfrac43\), \(\cot\alpha=-\dfrac34\).')

# ----- Bài tập từng mức: cùng dạng (A1 đổi góc, A2 giá trị đặc biệt, A3 góc liên quan; B4 hệ thức, B5 cùng tia cuối; C6 độ dài cung, C7 dùng hệ thức) -----
def _mcq(n, qe, qv, opts, ans, ee, ev): return MCQ(n, (qe, qv), opts, ans, (ee, ev))
S1 = [
  [_mcq(1, r'Convert \(60^\circ\) to radians.', r'Đổi \(60^\circ\) sang radian.', [r'\dfrac{\pi}{6}', r'\dfrac{\pi}{3}', r'\dfrac{\pi}{2}', r'\dfrac{2\pi}{3}'], 'b', r'Answer: b. \(60\cdot\dfrac{\pi}{180}=\dfrac{\pi}{3}\).', r'Đáp án b. \(60\cdot\dfrac{\pi}{180}=\dfrac{\pi}{3}\).'),
   _mcq(2, r'What is \(\sin\dfrac{\pi}{6}\)?', r'\(\sin\dfrac{\pi}{6}\) bằng bao nhiêu?', [r'\dfrac{\sqrt3}{2}', r'\dfrac12', r'1', r'\dfrac{\sqrt2}{2}'], 'b', r'Answer: b. \(\sin 30^\circ=\dfrac12\).', r'Đáp án b. \(\sin 30^\circ=\dfrac12\).'),
   _mcq(3, r'What is \(\cos\pi\)?', r'\(\cos\pi\) bằng bao nhiêu?', ['0', '1', '-1', r'\dfrac12'], 'c', r'Answer: c. At angle \(\pi\) the point is \((-1;0)\).', r'Đáp án c. Tại góc \(\pi\), điểm trên đường tròn là \((-1;0)\).')],
  [TF(4, (r'\(\sin^2\alpha+\cos^2\alpha=1\) for every angle \(\alpha\).', r'\(\sin^2\alpha+\cos^2\alpha=1\) với mọi góc \(\alpha\).'), 'true', (r'True. The point \(P(\cos\alpha;\sin\alpha)\) is on the trigonometric circle.', r'Đúng. Điểm \(P(\cos\alpha;\sin\alpha)\) nằm trên đường tròn lượng giác.')),
   TF(5, (r'The angles \(\dfrac{\pi}{3}\) and \(\dfrac{7\pi}{3}\) have the same terminal side.', r'Hai góc \(\dfrac{\pi}{3}\) và \(\dfrac{7\pi}{3}\) có cùng tia cuối.'), 'true', (r'True. \(\dfrac{7\pi}{3}-\dfrac{\pi}{3}=2\pi\).', r'Đúng. \(\dfrac{7\pi}{3}-\dfrac{\pi}{3}=2\pi\).'))],
  [SHORT(6, (r'On a circle of radius 3 cm, a central angle is 2 rad. Find the arc length in cm.', r'Trên đường tròn bán kính 3 cm, góc ở tâm là 2 rad. Tính độ dài cung (cm).'), '6', 'number', ('Enter a number.', 'Nhập một số.'), (r'Answer: 6. \(\ell=R\alpha=3\cdot 2=6\).', r'Đáp số: 6. \(\ell=R\alpha=3\cdot 2=6\).')),
   SHORT(7, (r'Given \(\cos\alpha=0.6\) and \(\dfrac{3\pi}{2}\lt\alpha\lt2\pi\). Find \(\sin\alpha\).', r'Cho \(\cos\alpha=0{,}6\) và \(\dfrac{3\pi}{2}\lt\alpha\lt2\pi\). Tính \(\sin\alpha\).'), '-0.8|-4/5', 'number', ('Enter a number.', 'Nhập một số.'), (r'Answer: \(-0.8\). \(\sin^2\alpha=0.64\) and sine is negative in quadrant IV.', r'Đáp số: \(-0{,}8\). \(\sin^2\alpha=0{,}64\) và sin âm ở góc phần tư IV.'))]]
S2 = [
  [_mcq(1, r'Convert \(150^\circ\) to radians.', r'Đổi \(150^\circ\) sang radian.', [r'\dfrac{2\pi}{3}', r'\dfrac{3\pi}{4}', r'\dfrac{5\pi}{6}', r'\dfrac{\pi}{6}'], 'c', r'Answer: c. \(150\cdot\dfrac{\pi}{180}=\dfrac{5\pi}{6}\).', r'Đáp án c. \(150\cdot\dfrac{\pi}{180}=\dfrac{5\pi}{6}\).'),
   _mcq(2, r'What is \(\sin\dfrac{\pi}{3}\)?', r'\(\sin\dfrac{\pi}{3}\) bằng bao nhiêu?', [r'\dfrac12', r'\dfrac{\sqrt2}{2}', r'\dfrac{\sqrt3}{2}', r'\sqrt3'], 'c', r'Answer: c. \(\sin 60^\circ=\dfrac{\sqrt3}{2}\).', r'Đáp án c. \(\sin 60^\circ=\dfrac{\sqrt3}{2}\).'),
   _mcq(3, r'What is \(\cos\dfrac{2\pi}{3}\)?', r'\(\cos\dfrac{2\pi}{3}\) bằng bao nhiêu?', [r'\dfrac12', r'-\dfrac12', r'-\dfrac{\sqrt3}{2}', r'\dfrac{\sqrt3}{2}'], 'b', r'Answer: b. \(\cos\dfrac{2\pi}{3}=\cos\left(\pi-\dfrac{\pi}{3}\right)=-\dfrac12\).', r'Đáp án b. \(\cos\dfrac{2\pi}{3}=\cos\left(\pi-\dfrac{\pi}{3}\right)=-\dfrac12\).')],
  [TF(4, (r'If \(\cos\alpha=0.8\) then \(\sin\alpha=0.2\).', r'Nếu \(\cos\alpha=0{,}8\) thì \(\sin\alpha=0{,}2\).'), 'false', (r'False. \(\sin^2\alpha=1-0.64=0.36\), so \(\sin\alpha=\pm 0.6\).', r'Sai. \(\sin^2\alpha=1-0{,}64=0{,}36\) nên \(\sin\alpha=\pm 0{,}6\).')),
   TF(5, (r'The angles \(-\dfrac{\pi}{3}\) and \(\dfrac{5\pi}{3}\) have the same terminal side.', r'Hai góc \(-\dfrac{\pi}{3}\) và \(\dfrac{5\pi}{3}\) có cùng tia cuối.'), 'true', (r'True. \(\dfrac{5\pi}{3}-\left(-\dfrac{\pi}{3}\right)=2\pi\).', r'Đúng. \(\dfrac{5\pi}{3}-\left(-\dfrac{\pi}{3}\right)=2\pi\).'))],
  [SHORT(6, (r'On a circle of radius 5 cm, a central angle is 1.2 rad. Find the arc length in cm.', r'Trên đường tròn bán kính 5 cm, góc ở tâm là 1,2 rad. Tính độ dài cung (cm).'), '6', 'number', ('Enter a number.', 'Nhập một số.'), (r'Answer: 6. \(\ell=5\cdot 1.2=6\).', r'Đáp số: 6. \(\ell=5\cdot 1{,}2=6\).')),
   SHORT(7, (r'Given \(\sin\alpha=0.6\) and \(\dfrac{\pi}{2}\lt\alpha\lt\pi\). Find \(\cos\alpha\).', r'Cho \(\sin\alpha=0{,}6\) và \(\dfrac{\pi}{2}\lt\alpha\lt\pi\). Tính \(\cos\alpha\).'), '-0.8|-4/5', 'number', ('Enter a number.', 'Nhập một số.'), (r'Answer: \(-0.8\). \(\cos^2\alpha=0.64\) and cosine is negative in quadrant II.', r'Đáp số: \(-0{,}8\). \(\cos^2\alpha=0{,}64\) và cos âm ở góc phần tư II.'))]]
S3 = [
  [_mcq(1, r'Convert \(\dfrac{3\pi}{4}\) rad to degrees.', r'Đổi \(\dfrac{3\pi}{4}\) rad sang độ.', [r'120^\circ', r'135^\circ', r'150^\circ', r'45^\circ'], 'b', r'Answer: b. \(\dfrac{3\pi}{4}\cdot\dfrac{180}{\pi}=135\).', r'Đáp án b. \(\dfrac{3\pi}{4}\cdot\dfrac{180}{\pi}=135\).'),
   _mcq(2, r'What is \(\tan\dfrac{\pi}{4}\)?', r'\(\tan\dfrac{\pi}{4}\) bằng bao nhiêu?', ['0', '1', r'\sqrt3', r'\dfrac{\sqrt3}{3}'], 'b', r'Answer: b. \(\sin\dfrac{\pi}{4}=\cos\dfrac{\pi}{4}\), so the quotient is 1.', r'Đáp án b. \(\sin\dfrac{\pi}{4}=\cos\dfrac{\pi}{4}\) nên thương bằng 1.'),
   _mcq(3, r'What is \(\sin\left(-\dfrac{\pi}{6}\right)\)?', r'\(\sin\left(-\dfrac{\pi}{6}\right)\) bằng bao nhiêu?', [r'\dfrac12', r'-\dfrac12', r'-\dfrac{\sqrt3}{2}', r'0'], 'b', r'Answer: b. \(\sin(-\alpha)=-\sin\alpha\), so the value is \(-\dfrac12\).', r'Đáp án b. \(\sin(-\alpha)=-\sin\alpha\) nên giá trị là \(-\dfrac12\).')],
  [TF(4, (r'If \(\cos\alpha=0.6\), then \(\sin\alpha=\pm 0.8\).', r'Nếu \(\cos\alpha=0{,}6\) thì \(\sin\alpha=\pm 0{,}8\).'), 'true', (r'True. \(\sin^2\alpha=1-0.36=0.64\).', r'Đúng. \(\sin^2\alpha=1-0{,}36=0{,}64\).')),
   TF(5, (r'The angles \(\dfrac{\pi}{6}\) and \(\dfrac{7\pi}{6}\) have the same terminal side.', r'Hai góc \(\dfrac{\pi}{6}\) và \(\dfrac{7\pi}{6}\) có cùng tia cuối.'), 'false', (r'False. Their difference is \(\pi\), not a multiple of \(2\pi\).', r'Sai. Hiệu của chúng là \(\pi\), không phải bội của \(2\pi\).'))],
  [SHORT(6, (r'On a circle of radius 2.5 cm, a central angle is 4 rad. Find the arc length in cm.', r'Trên đường tròn bán kính 2,5 cm, góc ở tâm là 4 rad. Tính độ dài cung (cm).'), '10', 'number', ('Enter a number.', 'Nhập một số.'), (r'Answer: 10. \(\ell=2.5\cdot 4=10\).', r'Đáp số: 10. \(\ell=2{,}5\cdot 4=10\).')),
   SHORT(7, (r'Given \(\cos\alpha=-0.6\) and \(\pi\lt\alpha\lt\dfrac{3\pi}{2}\). Find \(\sin\alpha\).', r'Cho \(\cos\alpha=-0{,}6\) và \(\pi\lt\alpha\lt\dfrac{3\pi}{2}\). Tính \(\sin\alpha\).'), '-0.8|-4/5', 'number', ('Enter a number.', 'Nhập một số.'), (r'Answer: \(-0.8\). \(\sin^2\alpha=0.64\) and sine is negative in quadrant III.', r'Đáp số: \(-0{,}8\). \(\sin^2\alpha=0{,}64\) và sin âm ở góc phần tư III.'))]]
practice = LEVEL_PRACTICE([('A. Multiple Choice', 'A. Trắc nghiệm'), ('B. True or False', 'B. Đúng hoặc sai'), ('C. Short Answer', 'C. Trả lời ngắn')], {1: S1, 2: S2, 3: S3})

mistakes = [
 (r'<b>Math knowledge.</b> Using \(\pi=180\) instead of \(\pi\) rad \(=180^\circ\). Check: \(\dfrac{\pi}{2}\) rad is \(90^\circ\).', r'<b>Kiến thức Toán.</b> Viết \(\pi=180\) thay vì \(\pi\) rad \(=180^\circ\). Kiểm tra: \(\dfrac{\pi}{2}\) rad là \(90^\circ\).'),
 (r'<b>Using formulas.</b> Using \(\ell=R\alpha\) with \(\alpha\) in degrees. The formula needs radians.', r'<b>Dùng công thức.</b> Dùng \(\ell=R\alpha\) khi \(\alpha\) tính bằng độ. Công thức này cần radian.'),
 (r'<b>Oriented angles.</b> Saying \(\dfrac{\pi}{6}\) and \(\dfrac{7\pi}{6}\) have the same terminal side. They differ by \(\pi\), not by \(2\pi\).', r'<b>Góc lượng giác.</b> Cho rằng \(\dfrac{\pi}{6}\) và \(\dfrac{7\pi}{6}\) cùng tia cuối. Hai góc này hơn kém \(\pi\), không phải \(2\pi\).'),
 (r'<b>Signs.</b> Forgetting the sign in the quadrant, for example \(\cos\dfrac{2\pi}{3}=+\dfrac12\). It is negative in quadrant II.', r'<b>Dấu.</b> Quên dấu theo góc phần tư, chẳng hạn viết \(\cos\dfrac{2\pi}{3}=+\dfrac12\). Ở góc phần tư II giá trị này âm.'),
 (r'<b>Identity.</b> From \(\sin^2\alpha=\dfrac{16}{25}\) writing only \(\sin\alpha=\dfrac45\). Always decide the sign.', r'<b>Hệ thức.</b> Từ \(\sin^2\alpha=\dfrac{16}{25}\) chỉ viết \(\sin\alpha=\dfrac45\). Luôn phải xác định dấu.'),
]
summary = [
 (r'An oriented angle has measures \(\alpha+k2\pi\); two angles have the same terminal side when they differ by a multiple of \(2\pi\).', r'Góc lượng giác có số đo \(\alpha+k2\pi\); hai góc cùng tia cuối khi hiệu của chúng là bội của \(2\pi\).'),
 (r'\(180^\circ=\pi\) rad; the arc length is \(\ell=R\alpha\) when \(\alpha\) is in radians.', r'\(180^\circ=\pi\) rad; độ dài cung \(\ell=R\alpha\) khi \(\alpha\) tính bằng radian.'),
 (r'On the trigonometric circle, \(P(\cos\alpha;\sin\alpha)\), \(\tan\alpha=\dfrac{\sin\alpha}{\cos\alpha}\), \(\cot\alpha=\dfrac{\cos\alpha}{\sin\alpha}\).', r'Trên đường tròn lượng giác, \(P(\cos\alpha;\sin\alpha)\), \(\tan\alpha=\dfrac{\sin\alpha}{\cos\alpha}\), \(\cot\alpha=\dfrac{\cos\alpha}{\sin\alpha}\).'),
 (r'Signs: sin is positive in quadrants I, II; cos in I, IV; tan and cot in I, III.', r'Dấu: sin dương ở góc phần tư I, II; cos dương ở I, IV; tan và cot dương ở I, III.'),
 (r'\(\sin^2\alpha+\cos^2\alpha=1\), \(1+\tan^2\alpha=\dfrac{1}{\cos^2\alpha}\), \(1+\cot^2\alpha=\dfrac{1}{\sin^2\alpha}\).', r'\(\sin^2\alpha+\cos^2\alpha=1\), \(1+\tan^2\alpha=\dfrac{1}{\cos^2\alpha}\), \(1+\cot^2\alpha=\dfrac{1}{\sin^2\alpha}\).'),
 ('Key English phrases: convert to radians; find the arc length; find the exact value; in which quadrant.', 'Cụm tiếng Anh cần nhớ: convert to radians (đổi sang radian); find the arc length (tìm độ dài cung); find the exact value (tìm giá trị chính xác); in which quadrant (ở góc phần tư nào).'),
]
checks = [
 ('I can find all measures of an oriented angle.', 'Tôi tìm được mọi số đo của một góc lượng giác.'),
 ('I can convert between degrees and radians and compute an arc length.', 'Tôi đổi được giữa độ và radian và tính được độ dài cung.'),
 ('I can find sin, cos, tan and cot of special angles.', 'Tôi tìm được sin, cos, tan, cot của các góc đặc biệt.'),
 ('I can use the identities and the values of related angles.', 'Tôi dùng được các hệ thức cơ bản và giá trị của các góc liên quan đặc biệt.'),
 STD_SUMMARY_CHECK_EN(),
]

lesson(id=LID, title_en='Trigonometric Values of Oriented Angles', title_vi='Giá trị lượng giác của góc lượng giác', topic=TOPIC,
       folder='trigonometric-functions', file='radians-and-trigonometric-functions',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Oriented angles, radians, arc length, and the sine, cosine, tangent and cotangent of an angle.', level='Intermediate', minutes=60,
       description_vi='Bài 1 – Góc lượng giác, radian, độ dài cung; sin, cos, tan, cot, các hệ thức cơ bản và góc liên quan đặc biệt.',
       tags_vi=['góc lượng giác', 'radian', 'đường tròn lượng giác', 'sin', 'cos', 'tan', 'cot', 'độ dài cung'],
       prerequisites=['g11-functions-01'], tags=['oriented angle', 'radian', 'trigonometric circle', 'sine', 'cosine', 'tangent', 'cotangent'], order=20)
