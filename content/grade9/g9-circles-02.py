# -*- coding: utf-8 -*-
"""Nội dung bài g9-circles-02 = Toán 9 KNTT, Bài 14: Cung và dây của một đường tròn – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 5 – Lesson 14."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9

LID = 'g9-circles-02'
CH = 'Đường tròn'
TOPIC = ('Circles', CH)
ensure_vocab([
 ('g9-chord', 'chord', 'dây (của đường tròn)', CH, 'AB is a chord of the circle with center O.', ''),
 ('g9-arc', 'arc', 'cung (tròn)', CH, 'Two points on a circle divide it into two arcs.', r'\(\overset{\frown}{AB}\)'),
 ('g9-minor-arc', 'minor arc', 'cung nhỏ', CH, 'The minor arc AB measures the same as the central angle AOB.', ''),
 ('g9-major-arc', 'major arc', 'cung lớn', CH, 'The major arc AB measures 360° minus the minor arc AB.', ''),
 ('g9-semicircle', 'semicircle', 'nửa đường tròn', CH, 'Each arc cut off by a diameter is a semicircle (180°).', ''),
 ('g9-arc-measure', 'measure of an arc', 'số đo cung', CH, 'The measure of the minor arc AB is 60°.', ''),
 ('g9-intercepted-arc', 'intercepted arc', 'cung bị chắn', CH, 'The central angle AOB intercepts the arc AB.', ''),
])
load_vocab()

# ---------- kiểm tra số liệu ----------
assert 360 - 125 == 235 and 360 - 60 == 300
assert 8 ** 2 + 8 ** 2 == 128 and abs(8 * 2 ** .5 - math.sqrt(128)) < 1e-12 and 8 * 2 ** .5 < 16
assert 11 > 2 * 5

meta = dict(level=('Basic', 'Cơ bản'), time=('about 60 minutes', '60 phút'),
            before=('Lesson 13: circles; grade 7: triangle inequality', 'Bài 13: đường tròn; lớp 7: bất đẳng thức tam giác'))
goals = [
 (r'recognize chords, diameters, central angles, minor arcs, major arcs and semicircles;', r'nhận biết được dây, đường kính, góc ở tâm, cung nhỏ, cung lớn, nửa đường tròn;'),
 (r'know that a diameter is the longest chord;', r'biết đường kính là dây lớn nhất;'),
 (r'find the measure of an arc from its central angle;', r'tính được số đo cung theo góc ở tâm;'),
 (r'solve problems with chords and arcs (clock faces, wheels).', r'giải bài toán về dây và cung (mặt đồng hồ, bánh xe).')]
vocab = [
 (r'<b>chord</b> – a segment joining two points of the circle.', r'[[Dây|dây (của đường tròn)]] – đoạn thẳng nối hai điểm của đường tròn.'),
 (r'<b>central angle</b> – an angle with its vertex at the center.', r'[[Góc ở tâm]] – góc có đỉnh trùng với tâm đường tròn.'),
 (r'<b>minor arc / major arc</b> – the arc inside / outside the central angle (less / more than \(180^\circ\)).', r'[[Cung nhỏ]] / [[cung lớn]] – cung nằm bên trong / bên ngoài góc ở tâm (nhỏ hơn / lớn hơn \(180^\circ\)).'),
 (r'<b>semicircle</b> – each of the two arcs cut off by a diameter (\(180^\circ\)).', r'[[Nửa đường tròn]] – mỗi cung bị chia bởi một đường kính (\(180^\circ\)).'),
 (r'<b>measure of an arc / intercepted arc</b> – written \(m\overset{\frown}{AB}\); the arc cut off by an angle.', r'[[Số đo cung]] / [[cung bị chắn]] – kí hiệu \(\text{sđ}\,\overset{\frown}{AB}\); cung nằm trong góc.')]
phrases = [
 (r'<b>\(AB\) is a chord of the circle with center \(O\).</b>', r'\(AB\) là một dây của đường tròn tâm \(O\).'),
 (r'<b>A chord passing through the center is a diameter.</b>', r'Dây đi qua tâm là đường kính.'),
 (r'<b>\(\widehat{AOB}\) is a central angle intercepting arc \(AB\).</b>', r'\(\widehat{AOB}\) là góc ở tâm chắn cung \(AB\).'),
 (r'<b>The measure of the minor arc \(AB\) is equal to the measure of \(\widehat{AOB}\).</b>', r'Số đo cung nhỏ \(AB\) bằng số đo góc \(AOB\).'),
 (r'<b>In a circle of radius \(R\), every chord has length at most \(2R\).</b>', r'Trong đường tròn bán kính \(R\), mọi dây đều có độ dài không quá \(2R\).')]
review = (T(r'<b>Triangle inequality.</b> In triangle \(OAB\): \(AB\lt OA+OB\).', r'<b>Bất đẳng thức tam giác.</b> Trong tam giác \(OAB\): \(AB\lt OA+OB\).') +
          T(r'<b>Lesson 13.</b> \(OA=OB=R\) for every \(A\), \(B\) on \((O;\,R)\).', r'<b>Bài 13.</b> \(OA=OB=R\) với mọi \(A\), \(B\) thuộc \((O;\,R)\).'))

G = lambda cfg, en, vi, hgt=290: GEO(sp_g9.auto_labels(cfg), cap=(en, vi), alt=(en, ''), height=hgt)
def pt(i, x, y, name=None, size=3): return {'type': 'point', 'id': i, 'at': [round(x, 4), round(y, 4)], 'name': i if name is None else name, 'style': {'size': size}}
def seg(a, b, **st): return {'type': 'segment', 'through': [a, b], 'style': st}
def on(R, deg): return (R * math.cos(math.radians(deg)), R * math.sin(math.radians(deg)))
R = 2.4
FIG1 = G({'view': [-3.3, 3.3, -3.0, 3.0], 'steps': [pt('O', 0, 0), pt('A', -R, 0), pt('B', R, 0), pt('C', *on(R, 120)), pt('D', *on(R, 50)),
          {'type': 'circle', 'center': 'O', 'radius': R}, {'type': 'arc', 'points': ['O', 'D', 'C']}, seg('A', 'B'), seg('C', 'D'), seg('O', 'C', dash=True), seg('O', 'D', dash=True),
          {'type': 'angle', 'points': ['D', 'O', 'C'], 'radius': 0.55, 'label': False}]},
         'AB is a diameter, CD is a chord; the central angle COD intercepts the minor arc CD (orange).', 'AB là đường kính, CD là dây; góc ở tâm COD chắn cung nhỏ CD (màu cam).')
FIG2 = G({'view': [-3.3, 3.3, -3.0, 3.0], 'steps': [pt('O', 0, 0), pt('A', *on(R, 200)), pt('B', *on(R, 260)), {'type': 'circle', 'center': 'O', 'radius': R},
          {'type': 'polygon', 'through': ['O', 'A', 'B']}, {'type': 'arc', 'points': ['O', 'A', 'B']}, {'type': 'angle', 'points': ['A', 'O', 'B'], 'radius': 0.6, 'label': '60^\\circ'}]},
         'Chord AB equals the radius: triangle OAB is equilateral and the minor arc AB measures 60°.', 'Dây AB bằng bán kính: tam giác OAB đều, cung nhỏ AB có số đo 60°.')

theory = '<h3>5.1 %s</h3>' % TI('Chords and diameters', 'Dây và đường kính')
theory += BOX('blue', ('Definitions and theorem', 'Khái niệm và định lí'),
  T(r'A <b>chord</b> is a segment joining two points of a circle. A chord through the center is a <b>diameter</b>.', r'Đoạn thẳng nối hai điểm của đường tròn là một [[dây|dây (của đường tròn)]]. Dây đi qua tâm là [[đường kính]].'),
  T(r'<b>Theorem.</b> In a circle of radius \(R\), every chord \(AB\) satisfies \(AB\le2R\); equality holds only for a diameter. So the diameter is the longest chord.', r'<b>Định lí.</b> Trong đường tròn bán kính \(R\), mọi dây \(AB\) đều có \(AB\le2R\); dấu bằng xảy ra khi và chỉ khi \(AB\) là đường kính. Vậy đường kính là dây lớn nhất.'),
  T(r'Reason: if \(AB\) does not pass through \(O\), then in triangle \(OAB\): \(AB\lt OA+OB=2R\).', r'Lí do: nếu \(AB\) không đi qua \(O\) thì trong tam giác \(OAB\): \(AB\lt OA+OB=2R\).'))
theory += FIG1
theory += '<h3>5.2 %s</h3>' % TI('Arcs and central angles', 'Cung, góc ở tâm và số đo cung')
theory += BOX('mint', ('Rules', 'Quy tắc'),
  T(r'An angle with its vertex at the center is a <b>central angle</b>. Two points \(A\), \(B\) divide the circle into two arcs; the arc inside \(\widehat{AOB}\) is the <b>minor arc</b>, the other is the <b>major arc</b>.', r'Góc có đỉnh trùng với tâm là [[góc ở tâm]]. Hai điểm \(A\), \(B\) chia đường tròn thành hai cung; cung nằm bên trong góc \(AOB\) là [[cung nhỏ]], cung còn lại là [[cung lớn]].'),
  T(r'The minor arc \(AB\) measures \(\widehat{AOB}\); the major arc \(AB\) measures \(360^\circ-\widehat{AOB}\).', r'Số đo cung nhỏ: \(\text{sđ}\,\overset{\frown}{AB}=\widehat{AOB}\); số đo cung lớn: \(\text{sđ}\,\overset{\frown}{AB}=360^\circ-\widehat{AOB}\).'),
  T(r'A semicircle measures \(180^\circ\); the whole circle measures \(360^\circ\).', r'Nửa đường tròn có số đo \(180^\circ\); cả đường tròn có số đo \(360^\circ\).'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Parts of a circle', 'Các yếu tố của đường tròn'),
  T(r'In the figure above, name a diameter, a chord that is not a diameter, a central angle and the arc it intercepts.', r'Trong hình trên, hãy chỉ ra một đường kính, một dây không phải đường kính, một góc ở tâm và cung bị chắn bởi góc đó.'),
  ('A diameter passes through \\(O\\).', 'Đường kính đi qua \\(O\\).'),
  [T(r'Diameter: \(AB\). Chord (not a diameter): \(CD\).', r'Đường kính: \(AB\). Dây không phải đường kính: \(CD\).'),
   T(r'Central angle: \(\widehat{COD}\); it intercepts the minor arc \(CD\).', r'Góc ở tâm: \(\widehat{COD}\); góc này chắn cung nhỏ \(CD\).')],
  T(r'\(AB\); \(CD\); \(\widehat{COD}\) and arc \(CD\).', r'\(AB\); \(CD\); \(\widehat{COD}\) và cung \(CD\).'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Measures of arcs', 'Số đo cung'),
  T(r'In circle \((O)\), \(\widehat{AOB}=125^\circ\). Find the measures of the minor and the major arc \(AB\).', r'Trong đường tròn \((O)\), \(\widehat{AOB}=125^\circ\). Tính số đo cung nhỏ và cung lớn \(AB\).'),
  ('Minor arc = central angle.', 'Cung nhỏ = góc ở tâm.'),
  [T(r'The minor arc \(AB\) measures \(125^\circ\).', r'Cung nhỏ \(AB\) có số đo \(125^\circ\).'), T(r'The major arc \(AB\) measures \(360^\circ-125^\circ=235^\circ\).', r'Cung lớn \(AB\) có số đo \(360^\circ-125^\circ=235^\circ\).')],
  T(r'\(125^\circ\) and \(235^\circ\).', r'\(125^\circ\) và \(235^\circ\).'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('A chord equal to the radius', 'Dây bằng bán kính'),
  T(r'A circle has center \(O\) and radius 6 cm; chord \(AB=6\) cm. Find the measures of the minor and the major arc \(AB\).', r'Đường tròn tâm \(O\) bán kính 6 cm có dây \(AB=6\) cm. Tính số đo cung nhỏ và cung lớn \(AB\).') + FIG2,
  ('Compare \\(OA\\), \\(OB\\), \\(AB\\).', 'So sánh \\(OA\\), \\(OB\\), \\(AB\\).'),
  [T(r'Since \(OA=OB=AB=6\) cm, triangle \(OAB\) is equilateral. Therefore, \(\widehat{AOB}=60^\circ\).', r'Vì \(OA=OB=AB=6\) cm nên tam giác \(OAB\) đều. Do đó \(\widehat{AOB}=60^\circ\).'),
   T(r'Minor arc: \(60^\circ\); major arc: \(360^\circ-60^\circ=300^\circ\).', r'Cung nhỏ: \(60^\circ\); cung lớn: \(360^\circ-60^\circ=300^\circ\).')],
  T(r'\(60^\circ\) and \(300^\circ\).', r'\(60^\circ\) và \(300^\circ\).'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('A right central angle', 'Góc ở tâm vuông'),
  T(r'Circle \((O;\,8\text{ cm})\) has a chord \(AB=8\sqrt2\) cm. Show that \(\widehat{AOB}=90^\circ\), find the arcs \(AB\) and compare \(AB\) with the diameter.', r'Đường tròn \((O;\,8\text{ cm})\) có dây \(AB=8\sqrt2\) cm. Chứng minh \(\widehat{AOB}=90^\circ\), tính số đo các cung \(AB\) và so sánh \(AB\) với đường kính.'),
  ('Use the converse of the Pythagorean theorem.', 'Dùng định lí Pythagore đảo.'),
  [T(r'\(OA^2+OB^2=64+64=128=\left(8\sqrt2\right)^2=AB^2\), so triangle \(OAB\) is right-angled at \(O\): \(\widehat{AOB}=90^\circ\).', r'\(OA^2+OB^2=64+64=128=\left(8\sqrt2\right)^2=AB^2\) nên tam giác \(OAB\) vuông tại \(O\): \(\widehat{AOB}=90^\circ\).'),
   T(r'Minor arc \(90^\circ\), major arc \(270^\circ\). \(AB=8\sqrt2\approx11.3\lt16=2R\), as expected for a chord that is not a diameter.', r'Cung nhỏ \(90^\circ\), cung lớn \(270^\circ\). \(AB=8\sqrt2\approx11{,}3\lt16=2R\), đúng với định lí vì \(AB\) không phải đường kính.')],
  T(r'\(90^\circ\), \(270^\circ\); \(AB\lt2R\).', r'\(90^\circ\), \(270^\circ\); \(AB\lt2R\).'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Clock face', 'Mặt đồng hồ'),
  T(r'The 12 numbers on a clock face divide the rim into equal arcs. a) Find the measure of each small arc. b) At 4 o’clock, find the central angle between the hands. c) The clock has radius 10 cm. Could the distance between the tips of the hands (both reaching the rim) be 21 cm?', r'12 số trên mặt đồng hồ chia vành đồng hồ thành các cung bằng nhau. a) Tính số đo mỗi cung nhỏ. b) Lúc 4 giờ, tính góc ở tâm tạo bởi hai kim. c) Đồng hồ có bán kính 10 cm. Khoảng cách giữa hai đầu kim (cùng chạm vành) có thể bằng 21 cm không?'),
  ('Each arc is \\(\\dfrac{360^\\circ}{12}\\).', 'Mỗi cung bằng \\(\\dfrac{360^\\circ}{12}\\).'),
  [T(r'a) \(\dfrac{360^\circ}{12}=30^\circ\). b) At 4 o’clock the hands are 4 arcs apart: \(4\cdot30^\circ=120^\circ\).', r'a) \(\dfrac{360^\circ}{12}=30^\circ\). b) Lúc 4 giờ hai kim cách nhau 4 cung: \(4\cdot30^\circ=120^\circ\).'),
   T(r'c) The tips are the ends of a chord, and every chord is at most \(2R=20\) cm \(\lt21\) cm. So it is impossible.', r'c) Hai đầu kim là hai đầu mút của một dây, mà mọi dây đều không quá \(2R=20\) cm \(\lt21\) cm. Vậy không thể.')],
  T(r'a) \(30^\circ\); b) \(120^\circ\); c) no.', r'a) \(30^\circ\); b) \(120^\circ\); c) không thể.'))

_SETS = sp_g9.BANK(sp_g9.L14_GROUPS, start=1, seeds=(2401, 2402, 2403))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Major arc = central angle.</b> Only the minor arc equals the central angle; the major arc is \(360^\circ\) minus it.', r'<b>Cho cung lớn bằng góc ở tâm.</b> Chỉ cung nhỏ bằng góc ở tâm; cung lớn bằng \(360^\circ\) trừ góc đó.'),
 (r'<b>Chord longer than \(2R\).</b> No chord can be longer than the diameter.', r'<b>Dây dài hơn \(2R\).</b> Không dây nào dài hơn đường kính.'),
 (r'<b>Every chord is a diameter.</b> Only chords through the center are diameters.', r'<b>Cho mọi dây là đường kính.</b> Chỉ dây đi qua tâm mới là đường kính.'),
 (r'<b>Using \(180^\circ\) instead of \(360^\circ\).</b> The whole circle measures \(360^\circ\).', r'<b>Dùng \(180^\circ\) thay cho \(360^\circ\).</b> Cả đường tròn có số đo \(360^\circ\).')]
summary = [
 (r'Chord: joins two points of the circle; diameter: chord through \(O\); \(AB\le2R\).', r'Dây nối hai điểm của đường tròn; đường kính là dây đi qua tâm; \(AB\le2R\).'),
 (r'Minor arc \(AB\) = \(\widehat{AOB}\); major arc \(AB\) = \(360^\circ-\widehat{AOB}\); semicircle = \(180^\circ\).', r'Cung nhỏ \(AB\) = \(\widehat{AOB}\); cung lớn \(AB\) = \(360^\circ-\widehat{AOB}\); nửa đường tròn = \(180^\circ\).'),
 (r'Chord equal to \(R\) ⟹ equilateral triangle ⟹ arc \(60^\circ\).', r'Dây bằng \(R\) ⟹ tam giác đều ⟹ cung \(60^\circ\).'),
 (r'Key English: chord, central angle, minor arc, major arc, semicircle, measure of an arc, intercepted arc.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[dây (của đường tròn)]], [[góc ở tâm]], [[cung nhỏ]], [[cung lớn]], [[nửa đường tròn]], [[số đo cung]], [[cung bị chắn]].')]
checks = [
 (r'I can recognize chords, diameters, central angles and arcs.', r'Em nhận biết được dây, đường kính, góc ở tâm, cung.'),
 (r'I know that the diameter is the longest chord.', r'Em biết đường kính là dây lớn nhất.'),
 (r'I can find the measure of an arc.', r'Em tính được số đo cung.'),
 (r'I can solve problems with clocks and wheels.', r'Em giải được bài toán về đồng hồ, bánh xe.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Arcs and Chords of a Circle', title_vi='Cung và dây của một đường tròn', topic=TOPIC,
       folder='circles', file='arcs-and-chords', catalog_title_vi='Cung và dây của một đường tròn',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Chords and diameters, central angles, minor and major arcs and their measures.', level='Basic', minutes=60,
       description_vi='Bài 14 – Dây và đường kính; góc ở tâm; cung nhỏ, cung lớn và số đo cung.',
       tags_vi=['dây', 'cung', 'góc ở tâm'], prerequisites=['g9-circles-01'], tags=['chord', 'arc', 'central angle'], order=140)
