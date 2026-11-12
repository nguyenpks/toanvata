# -*- coding: utf-8 -*-
"""Nội dung bài g9-trig-01 = Toán 9 KNTT, Bài 11: Tỉ số lượng giác của góc nhọn – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 4 – Lesson 11."""
import os, sys, math
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9

LID = 'g9-trig-01'
CH = 'Hệ thức lượng trong tam giác vuông'
TOPIC = ('Trigonometric Ratios in Right Triangles', CH)
ensure_vocab([
 ('g9-trig-ratio', 'trigonometric ratio', 'tỉ số lượng giác', CH, 'Sine, cosine, tangent and cotangent are the trigonometric ratios of an acute angle.', ''),
 ('g9-opp-side', 'opposite side', 'cạnh đối', CH, 'For angle B, the opposite side is AC.', ''),
 ('g9-adj-side', 'adjacent side', 'cạnh kề', CH, 'For angle B, the adjacent side is AB.', ''),
 ('g9-hypotenuse', 'hypotenuse', 'cạnh huyền', CH, 'The hypotenuse is the side opposite the right angle.', ''),
 ('g9-right-tri', 'right triangle', 'tam giác vuông', CH, 'Triangle ABC is a right triangle with the right angle at A.', ''),
 ('g9-elevation', 'angle of elevation', 'góc nâng', CH, 'The angle of elevation of the sun is 40°.', ''),
 ('g9-depression', 'angle of depression', 'góc hạ', CH, 'From the top of the tower, the angle of depression to the boat is 30°.', ''),
])
load_vocab()

# ---------- kiểm tra số liệu ----------
AB, AC, BC = 8, 6, 10; assert AB ** 2 + AC ** 2 == BC ** 2
assert (F(AC, BC), F(AB, BC), F(AC, AB), F(AB, AC)) == (F(3, 5), F(4, 5), F(3, 4), F(4, 3))
s = lambda d: math.sin(math.radians(d)); c = lambda d: math.cos(math.radians(d)); t = lambda d: math.tan(math.radians(d))
assert abs(s(30) + c(60) - t(45)) < 1e-12
assert abs(s(72) - c(18)) < 1e-12 and abs(c(68) - s(22)) < 1e-12 and abs(t(80) - 1 / t(10)) < 1e-12 and abs(1 / t(55) - t(35)) < 1e-12
assert '%.3f' % s(35) == '0.574' and '%.3f' % c(47.25) == '0.679' and round(math.degrees(math.atan(0.7))) == 35
h = 12 * t(40); assert '%.2f' % h == '10.07'

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 90 minutes', '90 phút'),
            before=('Grade 8: right triangles, the Pythagorean theorem, similar triangles', 'Lớp 8: tam giác vuông, định lí Pythagore, tam giác đồng dạng'))
goals = [
 (r'name the opposite side, the adjacent side and the hypotenuse for an acute angle;', r'xác định được cạnh đối, cạnh kề, cạnh huyền đối với một góc nhọn;'),
 (r'state and compute \(\sin\), \(\cos\), \(\tan\), \(\cot\) of an acute angle;', r'nêu được và tính được \(\sin\), \(\cos\), \(\tan\), \(\cot\) của góc nhọn;'),
 (r'know the values for \(30^\circ\), \(45^\circ\), \(60^\circ\) and the relation between complementary angles;', r'biết giá trị lượng giác của các góc \(30^\circ\), \(45^\circ\), \(60^\circ\) và quan hệ giữa hai góc phụ nhau;'),
 (r'use a calculator and solve simple real-life problems (angle of elevation).', r'dùng máy tính cầm tay và giải bài toán thực tế đơn giản (góc nâng).')]
vocab = [
 (r'<b>hypotenuse</b> – the side opposite the right angle (\(BC\)).', r'[[Cạnh huyền]] – cạnh đối diện góc vuông (\(BC\)).'),
 (r'<b>opposite side / adjacent side</b> – for angle \(B\): \(AC\) is opposite, \(AB\) is adjacent.', r'[[Cạnh đối]] / [[cạnh kề]] – với góc \(B\): \(AC\) là cạnh đối, \(AB\) là cạnh kề.'),
 (r'<b>trigonometric ratio</b> – \(\sin\alpha\), \(\cos\alpha\), \(\tan\alpha\), \(\cot\alpha\).', r'[[Tỉ số lượng giác]] – \(\sin\alpha\), \(\cos\alpha\), \(\tan\alpha\), \(\cot\alpha\).'),
 (r'<b>complementary angles</b> – two angles whose sum is \(90^\circ\).', r'[[Hai góc phụ nhau|góc phụ]] – hai góc có tổng bằng \(90^\circ\).'),
 (r'<b>angle of elevation / angle of depression</b> – the angle between the line of sight and the horizontal, looking up / looking down.', r'[[Góc nâng]] / [[góc hạ]] – góc giữa tia nhìn và phương nằm ngang khi nhìn lên / nhìn xuống.')]
phrases = [
 (r'<b>\(\sin\alpha\)</b>: “sine alpha”; <b>\(\cos\alpha\)</b>: “cosine alpha”.', r'\(\sin\alpha\): sin anpha; \(\cos\alpha\): côsin anpha.'),
 (r'<b>The sine of angle B equals the opposite side over the hypotenuse.</b>', r'Sin của góc \(B\) bằng cạnh đối chia cạnh huyền.'),
 (r'<b>\(30^\circ\) and \(60^\circ\) are complementary angles.</b>', r'\(30^\circ\) và \(60^\circ\) là hai góc phụ nhau.'),
 (r'<b>Set the calculator to degree mode.</b>', r'Để máy tính ở chế độ độ.'),
 (r'<b>Round to three decimal places.</b>', r'Làm tròn đến chữ số thập phân thứ ba.')]
review = (T(r'<b>Pythagorean theorem.</b> In triangle \(ABC\) right-angled at \(A\): \(BC^2=AB^2+AC^2\).', r'<b>Định lí Pythagore.</b> Tam giác \(ABC\) vuông tại \(A\): \(BC^2=AB^2+AC^2\).') +
          T(r'<b>Similar right triangles</b> with an equal acute angle have equal ratios of corresponding sides.', r'<b>Hai tam giác vuông đồng dạng</b> (có một góc nhọn bằng nhau) thì tỉ số các cạnh tương ứng bằng nhau.'))

G = lambda cfg, en, vi, hgt=300: GEO(sp_g9.auto_labels(cfg), cap=(en, vi), alt=(en, ''), height=hgt)
def pt(i, x, y): return {'type': 'point', 'id': i, 'at': [x, y], 'name': i}
FIG = G({'view': [-1, 6, -1, 4.4], 'steps': [pt('A', 0, 0), pt('B', 5, 0), pt('C', 0, 3.6),
          {'type': 'polygon', 'through': ['A', 'B', 'C']},
          {'type': 'angle', 'points': ['C', 'A', 'B']}, {'type': 'angle', 'points': ['A', 'B', 'C'], 'radius': 0.9, 'label': '\\alpha'}]},
        'Triangle ABC right-angled at A, with angle B = α: AC is the opposite side, AB the adjacent side, BC the hypotenuse.',
        'Tam giác ABC vuông tại A, góc B = α: AC là cạnh đối, AB là cạnh kề, BC là cạnh huyền.')

theory = '<h3>5.1 %s</h3>' % TI('Trigonometric ratios of an acute angle', 'Khái niệm tỉ số lượng giác của góc nhọn')
theory += FIG
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'Triangle \(ABC\) is right-angled at \(A\) and \(\widehat{B}=\alpha\). With respect to \(\alpha\): \(AC\) is the <b>opposite side</b>, \(AB\) is the <b>adjacent side</b>, \(BC\) is the <b>hypotenuse</b>.', r'Tam giác \(ABC\) vuông tại \(A\), \(\widehat{B}=\alpha\). Đối với góc \(\alpha\): \(AC\) là [[cạnh đối]], \(AB\) là [[cạnh kề]], \(BC\) là [[cạnh huyền]].'),
  M(r'\sin\alpha=\dfrac{AC}{BC},\quad \cos\alpha=\dfrac{AB}{BC},\quad \tan\alpha=\dfrac{AC}{AB},\quad \cot\alpha=\dfrac{AB}{AC}'),
  T(r'In words: sine = opposite/hypotenuse, cosine = adjacent/hypotenuse, tangent = opposite/adjacent, cotangent = adjacent/opposite. For an acute angle: \(0\lt\sin\alpha\lt1\), \(0\lt\cos\alpha\lt1\), \(\tan\alpha\cdot\cot\alpha=1\).', r'Nói gọn: sin = đối/huyền, cos = kề/huyền, tan = đối/kề, cot = kề/đối. Với góc nhọn: \(0\lt\sin\alpha\lt1\), \(0\lt\cos\alpha\lt1\), \(\tan\alpha\cdot\cot\alpha=1\).'))
theory += '<h3>5.2 %s</h3>' % TI('Special angles', 'Tỉ số lượng giác của các góc đặc biệt')
theory += TABLE([('Angle', 'Góc')] + [('\\(%d^\\circ\\)' % a, '\\(%d^\\circ\\)' % a) for a in (30, 45, 60)],
  [['\\(\\sin\\)', '\\(\\dfrac12\\)', '\\(\\dfrac{\\sqrt2}{2}\\)', '\\(\\dfrac{\\sqrt3}{2}\\)'],
   ['\\(\\cos\\)', '\\(\\dfrac{\\sqrt3}{2}\\)', '\\(\\dfrac{\\sqrt2}{2}\\)', '\\(\\dfrac12\\)'],
   ['\\(\\tan\\)', '\\(\\dfrac{\\sqrt3}{3}\\)', '\\(1\\)', '\\(\\sqrt3\\)'],
   ['\\(\\cot\\)', '\\(\\sqrt3\\)', '\\(1\\)', '\\(\\dfrac{\\sqrt3}{3}\\)']])
for (f, a), v in sp_g9.SPECIAL.items(): assert abs(sp_g9.SPVAL[v] - sp_g9._trig(f, a)) < 1e-12
theory += BOX('mint', ('Where do they come from?', 'Nguồn gốc'),
  T(r'\(45^\circ\): half of a square with side 1 (legs 1 and 1, hypotenuse \(\sqrt2\)). \(30^\circ\) and \(60^\circ\): half of an equilateral triangle with side 2 (legs 1 and \(\sqrt3\), hypotenuse 2).', r'\(45^\circ\): nửa hình vuông cạnh 1 (hai cạnh góc vuông bằng 1, cạnh huyền \(\sqrt2\)). \(30^\circ\) và \(60^\circ\): nửa tam giác đều cạnh 2 (hai cạnh góc vuông 1 và \(\sqrt3\), cạnh huyền 2).'))
theory += '<h3>5.3 %s</h3>' % TI('Complementary angles', 'Tỉ số lượng giác của hai góc phụ nhau')
theory += BOX('yellow', ('Rule', 'Định lí'),
  M(r'\sin\alpha=\cos\left(90^\circ-\alpha\right),\quad \cos\alpha=\sin\left(90^\circ-\alpha\right),\quad \tan\alpha=\cot\left(90^\circ-\alpha\right),\quad \cot\alpha=\tan\left(90^\circ-\alpha\right)'),
  T(r'Reason: in the figure, \(\widehat B+\widehat C=90^\circ\), and the side opposite \(B\) is the side adjacent to \(C\).', r'Lí do: trong hình, \(\widehat B+\widehat C=90^\circ\), cạnh đối của góc \(B\) chính là cạnh kề của góc \(C\).'),
  T(r'Calculator: set it to degree mode (D). Example: \(\sin35^\circ\approx0.574\); for an angle given in degrees and minutes, use the \(^\circ\,{}^{\prime}\,{}^{\prime\prime}\) key: \(\cos47^\circ15^{\prime}\approx0.679\). To find the angle from a ratio, use SHIFT + sin/cos/tan.', r'Máy tính cầm tay: để ở chế độ độ (D). Ví dụ: \(\sin35^\circ\approx0{,}574\); góc cho bằng độ và phút thì dùng phím \(^\circ\,{}^{\prime}\,{}^{\prime\prime}\): \(\cos47^\circ15^{\prime}\approx0{,}679\). Tìm góc khi biết tỉ số: dùng SHIFT + sin/cos/tan.'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('The four ratios', 'Bốn tỉ số lượng giác'),
  T(r'Triangle \(ABC\) is right-angled at \(A\) with \(AB=8\) cm, \(AC=6\) cm, \(BC=10\) cm. Compute the trigonometric ratios of angle \(B\).', r'Tam giác \(ABC\) vuông tại \(A\) có \(AB=8\) cm, \(AC=6\) cm, \(BC=10\) cm. Tính các tỉ số lượng giác của góc \(B\).'),
  ('For angle \\(B\\): opposite \\(AC\\), adjacent \\(AB\\), hypotenuse \\(BC\\).', 'Với góc \\(B\\): cạnh đối \\(AC\\), cạnh kề \\(AB\\), cạnh huyền \\(BC\\).'),
  [T(r'\(\sin B=\dfrac{6}{10}=\dfrac35\), \(\cos B=\dfrac{8}{10}=\dfrac45\).', r'\(\sin B=\dfrac{6}{10}=\dfrac35\), \(\cos B=\dfrac{8}{10}=\dfrac45\).'),
   T(r'\(\tan B=\dfrac68=\dfrac34\), \(\cot B=\dfrac86=\dfrac43\).', r'\(\tan B=\dfrac68=\dfrac34\), \(\cot B=\dfrac86=\dfrac43\).')],
  T(r'\(\sin B=\dfrac35\), \(\cos B=\dfrac45\), \(\tan B=\dfrac34\), \(\cot B=\dfrac43\).', r'\(\sin B=\dfrac35\), \(\cos B=\dfrac45\), \(\tan B=\dfrac34\), \(\cot B=\dfrac43\).'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Special angles', 'Góc đặc biệt'),
  T(r'Compute \(P=\sin30^\circ+\cos60^\circ-\tan45^\circ\).', r'Tính \(P=\sin30^\circ+\cos60^\circ-\tan45^\circ\).'),
  ('Use the table of special angles.', 'Dùng bảng giá trị lượng giác của các góc đặc biệt.'),
  [T(r'\(P=\dfrac12+\dfrac12-1=0\).', r'\(P=\dfrac12+\dfrac12-1=0\).')],
  T(r'\(P=0\).', r'\(P=0\).'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('Complementary angles', 'Hai góc phụ nhau'),
  T(r'Write as trigonometric ratios of angles less than \(45^\circ\): \(\sin72^\circ\), \(\cos68^\circ\), \(\tan80^\circ\), \(\cot55^\circ\).', r'Viết thành tỉ số lượng giác của góc nhỏ hơn \(45^\circ\): \(\sin72^\circ\), \(\cos68^\circ\), \(\tan80^\circ\), \(\cot55^\circ\).'),
  ('Replace \\(\\alpha\\) by \\(90^\\circ-\\alpha\\) and switch sin ↔ cos, tan ↔ cot.', 'Thay \\(\\alpha\\) bởi \\(90^\\circ-\\alpha\\) và đổi sin ↔ cos, tan ↔ cot.'),
  [T(r'\(\sin72^\circ=\cos18^\circ\), \(\cos68^\circ=\sin22^\circ\).', r'\(\sin72^\circ=\cos18^\circ\), \(\cos68^\circ=\sin22^\circ\).'),
   T(r'\(\tan80^\circ=\cot10^\circ\), \(\cot55^\circ=\tan35^\circ\).', r'\(\tan80^\circ=\cot10^\circ\), \(\cot55^\circ=\tan35^\circ\).')],
  T(r'\(\cos18^\circ\); \(\sin22^\circ\); \(\cot10^\circ\); \(\tan35^\circ\).', r'\(\cos18^\circ\); \(\sin22^\circ\); \(\cot10^\circ\); \(\tan35^\circ\).'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Using a calculator', 'Dùng máy tính cầm tay'),
  T(r'a) Compute \(\sin35^\circ\) and \(\cos47^\circ15^{\prime}\) (three decimal places). b) Find the acute angle \(\alpha\) with \(\tan\alpha=0.7\) (to the nearest degree).', r'a) Tính \(\sin35^\circ\) và \(\cos47^\circ15^{\prime}\) (làm tròn đến chữ số thập phân thứ ba). b) Tìm góc nhọn \(\alpha\) biết \(\tan\alpha=0{,}7\) (làm tròn đến độ).'),
  ('Check that the calculator is in degree mode.', 'Kiểm tra máy tính đang ở chế độ độ.'),
  [T(r'a) \(\sin35^\circ\approx0.574\); \(\cos47^\circ15^{\prime}\approx0.679\).', r'a) \(\sin35^\circ\approx0{,}574\); \(\cos47^\circ15^{\prime}\approx0{,}679\).'),
   T(r'b) SHIFT, tan, 0.7, = gives \(34.99\ldots^\circ\), so \(\alpha\approx35^\circ\).', r'b) Bấm SHIFT, tan, 0,7, = được \(34{,}99\ldots^\circ\), nên \(\alpha\approx35^\circ\).')],
  T(r'a) \(0.574\); \(0.679\). b) \(\alpha\approx35^\circ\).', r'a) \(0{,}574\); \(0{,}679\). b) \(\alpha\approx35^\circ\).'))
FIG2 = G({'view': [-1, 7, -0.8, 6], 'steps': [pt('A', 0, 0), pt('B', 6, 0), pt('C', 0, 5.03),
          {'type': 'polygon', 'through': ['A', 'B', 'C'], 'style': {'fillOpacity': 0.18}},
          {'type': 'angle', 'points': ['C', 'A', 'B']}, {'type': 'angle', 'points': ['A', 'B', 'C'], 'radius': 1.0, 'label': '40^\\circ'}]},
         'AC is the tree, AB = 12 m is its shadow, and the angle of elevation of the sun is 40°.', 'AC là cây, AB = 12 m là bóng cây, góc nâng của tia nắng là 40°.', 280)
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Height of a tree', 'Chiều cao của cây'),
  T(r'A tree casts a shadow \(12\) m long on flat ground. The angle of elevation of the sun is \(40^\circ\). How tall is the tree (two decimal places)?', r'Một cái cây có bóng trên mặt đất phẳng dài \(12\) m. Góc nâng của tia nắng mặt trời là \(40^\circ\). Tính chiều cao của cây (làm tròn đến chữ số thập phân thứ hai).') + FIG2,
  ('The height is opposite the \\(40^\\circ\\) angle, the shadow is adjacent: use \\(\\tan\\).', 'Chiều cao là cạnh đối của góc \\(40^\\circ\\), bóng là cạnh kề: dùng \\(\\tan\\).'),
  [T(r'\(\tan40^\circ=\dfrac{AC}{AB}\Rightarrow AC=12\cdot\tan40^\circ\).', r'\(\tan40^\circ=\dfrac{AC}{AB}\Rightarrow AC=12\cdot\tan40^\circ\).'),
   T(r'\(AC\approx12\cdot0.8391\approx10.07\) m.', r'\(AC\approx12\cdot0{,}8391\approx10{,}07\) m.')],
  T(r'About \(10.07\) m.', r'Khoảng \(10{,}07\) m.'))
assert '%.4f' % t(40) == '0.8391'

_SETS = sp_g9.BANK(sp_g9.L11_GROUPS, start=1, seeds=(2101, 2102, 2103))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Mixing up opposite and adjacent.</b> They depend on the angle: for \(B\) the opposite side is \(AC\), for \(C\) it is \(AB\).', r'<b>Nhầm cạnh đối và cạnh kề.</b> Chúng phụ thuộc vào góc đang xét: với góc \(B\) cạnh đối là \(AC\), với góc \(C\) là \(AB\).'),
 (r'<b>Inverting tan and cot.</b> \(\tan\) = opposite/adjacent, \(\cot\) = adjacent/opposite.', r'<b>Đảo ngược tan và cot.</b> \(\tan\) = đối/kề, \(\cot\) = kề/đối.'),
 (r'<b>Calculator in the wrong mode.</b> In radian mode \(\sin30\ne0.5\); switch to degrees (D).', r'<b>Để sai chế độ máy tính.</b> Ở chế độ radian \(\sin30\ne0{,}5\); phải chuyển sang chế độ độ (D).'),
 (r'<b>Wrong complementary angle.</b> \(\sin35^\circ=\cos55^\circ\), not \(\cos35^\circ\).', r'<b>Sai góc phụ.</b> \(\sin35^\circ=\cos55^\circ\), không phải \(\cos35^\circ\).')]
summary = [
 (r'sin = opposite/hypotenuse, cos = adjacent/hypotenuse, tan = opposite/adjacent, cot = adjacent/opposite.', r'sin = đối/huyền, cos = kề/huyền, tan = đối/kề, cot = kề/đối.'),
 (r'Special angles: \(\sin30^\circ=\cos60^\circ=\dfrac12\), \(\sin45^\circ=\cos45^\circ=\dfrac{\sqrt2}{2}\), \(\tan45^\circ=1\), \(\tan60^\circ=\sqrt3\).', r'Góc đặc biệt: \(\sin30^\circ=\cos60^\circ=\dfrac12\), \(\sin45^\circ=\cos45^\circ=\dfrac{\sqrt2}{2}\), \(\tan45^\circ=1\), \(\tan60^\circ=\sqrt3\).'),
 (r'Complementary angles: \(\sin\alpha=\cos(90^\circ-\alpha)\), \(\tan\alpha=\cot(90^\circ-\alpha)\).', r'Hai góc phụ nhau: \(\sin\alpha=\cos(90^\circ-\alpha)\), \(\tan\alpha=\cot(90^\circ-\alpha)\).'),
 (r'Key English: opposite side, adjacent side, hypotenuse, trigonometric ratio, angle of elevation, angle of depression.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[cạnh đối]], [[cạnh kề]], [[cạnh huyền]], [[tỉ số lượng giác]], [[góc nâng]], [[góc hạ]].')]
checks = [
 (r'I can name the opposite side, the adjacent side and the hypotenuse.', r'Em xác định được cạnh đối, cạnh kề, cạnh huyền.'),
 (r'I can compute the four trigonometric ratios of an acute angle.', r'Em tính được bốn tỉ số lượng giác của góc nhọn.'),
 (r'I know the values for \(30^\circ\), \(45^\circ\), \(60^\circ\) and use complementary angles.', r'Em nhớ giá trị của các góc \(30^\circ\), \(45^\circ\), \(60^\circ\) và dùng được quan hệ hai góc phụ nhau.'),
 (r'I can use a calculator and solve a problem with an angle of elevation.', r'Em dùng được máy tính cầm tay và giải được bài toán có góc nâng.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Trigonometric Ratios of an Acute Angle', title_vi='Tỉ số lượng giác của góc nhọn', topic=TOPIC,
       folder='right-triangle-trigonometry', file='trigonometric-ratios', catalog_title_vi='Tỉ số lượng giác của góc nhọn',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Sine, cosine, tangent and cotangent of an acute angle, special angles, complementary angles and calculator use.', level='Intermediate', minutes=90,
       description_vi='Bài 11 – Tỉ số lượng giác của góc nhọn; giá trị của các góc 30°, 45°, 60°; hai góc phụ nhau; dùng máy tính cầm tay.',
       tags_vi=['tỉ số lượng giác', 'tam giác vuông', 'góc nhọn'],
       prerequisites=[], tags=['sine', 'cosine', 'tangent', 'right triangle'], order=110)
