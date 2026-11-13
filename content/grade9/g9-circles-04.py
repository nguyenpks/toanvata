# -*- coding: utf-8 -*-
"""Nội dung bài g9-circles-04 = Toán 9 KNTT, Bài 16: Vị trí tương đối của đường thẳng và đường tròn – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 5 – Lesson 16; ví dụ tiếp tuyến của Lesson 13 chuyển về đây (D6)."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9

LID = 'g9-circles-04'
CH = 'Đường tròn'
TOPIC = ('Circles', CH)
ensure_vocab([
 ('g9-secant', 'secant', 'cát tuyến (của đường tròn)', CH, 'A secant cuts the circle at two points.', ''),
 ('g9-tangent', 'tangent (to a circle)', 'tiếp tuyến (của đường tròn)', CH, 'The line d is tangent to the circle at A.', ''),
 ('g9-tangent-segments', 'tangent segments from a point', 'hai tiếp tuyến cắt nhau', CH, 'The two tangent segments drawn from the same external point are equal.', ''),
 ('g9-perpendicular', 'perpendicular', 'vuông góc', CH, 'The radius is perpendicular to the tangent at the point of tangency.', r'\(\perp\)'),
 ('g9-no-common', 'have no common point', 'không giao nhau', CH, 'If d > R, the line and the circle have no common point.', ''),
])
load_vocab()

# ---------- kiểm tra số liệu ----------
assert math.sqrt(13 ** 2 - 5 ** 2) == 12 and 2 * math.sqrt(5 ** 2 - 3 ** 2) == 8
PA = math.sqrt(10 ** 2 - 5 ** 2); assert abs(PA - 5 * 3 ** .5) < 1e-12 and abs(math.degrees(math.acos(5 / 10)) - 60) < 1e-9
S = 5 * PA; Ssec = math.pi * 25 * 120 / 360; assert abs(S - 25 * 3 ** .5) < 1e-9 and '%.2f' % (S - Ssec) == '17.12'

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 90 minutes', '90 phút'),
            before=('Lessons 13–14; grade 8: Pythagorean theorem', 'Bài 13, 14; lớp 8: định lí Pythagore'))
goals = [
 (r'describe the three positions of a line and a circle using \(d\) and \(R\);', r'mô tả được ba vị trí tương đối của đường thẳng và đường tròn qua hệ thức giữa \(d\) và \(R\);'),
 (r'recognize a tangent and use the property “tangent ⟂ radius”;', r'nhận biết được tiếp tuyến và dùng tính chất “tiếp tuyến vuông góc với bán kính tại tiếp điểm”;'),
 (r'use the property of two tangents from one point;', r'vận dụng được tính chất của hai tiếp tuyến cắt nhau;'),
 (r'compute tangent lengths and chord lengths with the Pythagorean theorem.', r'tính được độ dài tiếp tuyến, độ dài dây bằng định lí Pythagore.')]
vocab = [
 (r'<b>secant</b> – a line with two common points with the circle.', r'[[Cát tuyến|cát tuyến (của đường tròn)]] – đường thẳng có hai điểm chung với đường tròn.'),
 (r'<b>tangent / point of tangency</b> – a line with exactly one common point / that point.', r'[[Tiếp tuyến|tiếp tuyến (của đường tròn)]] / [[tiếp điểm]] – đường thẳng có đúng một điểm chung / điểm chung đó.'),
 (r'<b>distance from a point to a line</b> – the length \(d=OH\) of the perpendicular from \(O\).', r'[[Khoảng cách từ một điểm đến một đường thẳng]] – độ dài \(d=OH\) của đoạn vuông góc kẻ từ \(O\).'),
 (r'<b>perpendicular</b> – \(OA\perp a\): the radius meets the tangent at a right angle.', r'[[Vuông góc]] – \(OA\perp a\): bán kính vuông góc với tiếp tuyến.'),
 (r'<b>tangent segments</b> – \(PA\), \(PB\) drawn from the same point \(P\); \(PA=PB\).', r'[[Hai tiếp tuyến cắt nhau]] – \(PA\), \(PB\) kẻ từ cùng một điểm \(P\); \(PA=PB\).')]
phrases = [
 (r'<b>The line \(d\) is tangent to the circle at \(A\).</b>', r'Đường thẳng \(d\) tiếp xúc với đường tròn tại \(A\).'),
 (r'<b>The radius is perpendicular to the tangent at the point of tangency.</b>', r'Bán kính vuông góc với tiếp tuyến tại tiếp điểm.'),
 (r'<b>Since \(PA\) is tangent to the circle at \(A\), \(OA\perp PA\).</b>', r'Vì \(PA\) là tiếp tuyến của đường tròn tại \(A\) nên \(OA\perp PA\).'),
 (r'<b>Therefore, triangle \(OAP\) is a right triangle.</b>', r'Do đó tam giác \(OAP\) vuông tại \(A\).'),
 (r'<b>The two tangent segments drawn from the same external point are equal.</b>', r'Hai tiếp tuyến cắt nhau tại một điểm thì điểm đó cách đều hai tiếp điểm.')]
review = (T(r'<b>Pythagorean theorem.</b> In a right triangle, (hypotenuse)\(^2\) = sum of the squares of the legs.', r'<b>Định lí Pythagore.</b> Trong tam giác vuông, bình phương cạnh huyền bằng tổng bình phương hai cạnh góc vuông.') +
          T(r'<b>Lesson 14.</b> The perpendicular from \(O\) to a chord bisects the chord.', r'<b>Bài 14.</b> Đường vuông góc kẻ từ \(O\) đến một dây đi qua trung điểm của dây đó.'))

G = lambda cfg, en, vi, hgt=290: GEO(sp_g9.auto_labels(cfg), cap=(en, vi), alt=(en, ''), height=hgt)
def pt(i, x, y, name=None, size=3): return {'type': 'point', 'id': i, 'at': [round(x, 4), round(y, 4)], 'name': i if name is None else name, 'style': {'size': size}}
def seg(a, b, **st): return {'type': 'segment', 'through': [a, b], 'style': st}
def txt(x, y, s): return {'type': 'text', 'at': [x, y], 'text': s}
R = 1.8; xa = math.sqrt(R * R - 0.9 ** 2)
FIG1 = G({'view': [-3.0, 3.6, -2.6, 2.4], 'steps': [pt('O', 0, 0), pt('A', -xa, 0.9), pt('B', xa, 0.9), pt('H', 0, -R), pt('K', 2.6, 0), pt('K2', 2.6, 1.0, name='', size=0),
          {'type': 'circle', 'center': 'O', 'radius': R}, {'type': 'lineeq', 'a': 0, 'b': 1, 'c': -0.9}, {'type': 'tangent', 'center': 'O', 'at': 'H', 'showRadius': True},
          {'type': 'lineeq', 'a': 1, 'b': 0, 'c': -2.6}, seg('O', 'K', dash=True), {'type': 'angle', 'points': ['O', 'K', 'K2']},
          txt(-2.75, 1.15, 'a'), txt(-2.75, -2.05, 'b'), txt(2.85, 2.1, 'c')]},
         'Line a cuts the circle at A and B (d < R); line b is tangent at H (d = R); line c has no common point with the circle (d = OK > R).',
         'Đường thẳng a cắt đường tròn tại A, B (d < R); b tiếp xúc với đường tròn tại H (d = R); c không giao với đường tròn (d = OK > R).')
P = (5.0, 0.0); c = 2 / 5; A = (2 * c, 2 * math.sqrt(1 - c * c)); B = (A[0], -A[1])
assert abs((P[0] - A[0]) * A[0] + (P[1] - A[1]) * A[1]) < 1e-9
FIG2 = G({'view': [-2.6, 5.8, -2.6, 2.6], 'steps': [pt('O', 0, 0), pt('P', *P), pt('A', *A), pt('B', *B), {'type': 'circle', 'center': 'O', 'radius': 2},
          seg('P', 'A'), seg('P', 'B'), seg('O', 'A'), seg('O', 'B'), seg('O', 'P', dash=True), {'type': 'angle', 'points': ['O', 'A', 'P']}, {'type': 'angle', 'points': ['O', 'B', 'P']}]},
         'PA and PB are tangent to (O) at A and B: OA ⊥ PA, OB ⊥ PB and PA = PB.', 'PA, PB là hai tiếp tuyến của (O) tại A, B: OA ⊥ PA, OB ⊥ PB và PA = PB.', 270)

theory = '<h3>5.1 %s</h3>' % TI('Three relative positions', 'Ba vị trí tương đối của đường thẳng và đường tròn')
theory += FIG1
theory += TABLE([('Position', 'Vị trí tương đối'), ('Common points', 'Số điểm chung'), ('Relation', 'Hệ thức')],
  [[TI('the line cuts the circle (secant)', 'cắt nhau (cát tuyến)'), '2', '\\(d\\lt R\\)'],
   [TI('the line is tangent to the circle', 'tiếp xúc nhau (tiếp tuyến)'), '1', '\\(d=R\\)'],
   [TI('they have no common point', 'không giao nhau'), '0', '\\(d\\gt R\\)']])
theory += BOX('blue', ('Notes', 'Ghi nhớ'),
  T(r'Here \(d=OH\) is the distance from the center \(O\) to the line (\(H\) is the foot of the perpendicular).', r'Ở đây \(d=OH\) là khoảng cách từ tâm \(O\) đến đường thẳng (\(H\) là chân đường vuông góc).'),
  T(r'When the line cuts the circle at \(A\), \(B\): \(H\) is the midpoint of \(AB\) and \(AH=\sqrt{R^2-d^2}\).', r'Khi đường thẳng cắt đường tròn tại \(A\), \(B\): \(H\) là trung điểm của \(AB\) và \(AH=\sqrt{R^2-d^2}\).'))
theory += '<h3>5.2 %s</h3>' % TI('Tangents', 'Tiếp tuyến của đường tròn')
theory += BOX('mint', ('Properties', 'Tính chất và dấu hiệu'),
  T(r'<b>Property.</b> If \(a\) is tangent to \((O)\) at \(A\), then \(a\perp OA\).', r'<b>Tính chất.</b> Nếu \(a\) là tiếp tuyến của \((O)\) tại \(A\) thì \(a\perp OA\).'),
  T(r'<b>Test.</b> If a line passes through a point \(A\) of the circle and is perpendicular to \(OA\), it is a tangent at \(A\).', r'<b>Dấu hiệu.</b> Nếu một đường thẳng đi qua điểm \(A\) của đường tròn và vuông góc với bán kính \(OA\) thì nó là tiếp tuyến của đường tròn tại \(A\).'))
theory += FIG2
theory += BOX('yellow', ('Two tangents from one point', 'Tính chất hai tiếp tuyến cắt nhau'),
  T(r'If the tangents at \(A\) and \(B\) meet at \(P\), then \(PA=PB\); \(PO\) bisects \(\widehat{APB}\); \(OP\) bisects \(\widehat{AOB}\).', r'Nếu hai tiếp tuyến tại \(A\), \(B\) của \((O)\) cắt nhau tại \(P\) thì \(PA=PB\); \(PO\) là tia phân giác của \(\widehat{APB}\); \(OP\) là tia phân giác của \(\widehat{AOB}\).'),
  T(r'Reason: right triangles \(OAP\) and \(OBP\) have \(OA=OB\) and the common hypotenuse \(OP\).', r'Lí do: hai tam giác vuông \(OAP\), \(OBP\) có \(OA=OB\) và chung cạnh huyền \(OP\).'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Relative positions', 'Xác định vị trí tương đối'),
  T(r'Circle \((O;\,6\text{ cm})\). Lines \(a\), \(b\), \(c\) are at distances 4 cm, 6 cm, 8 cm from \(O\). Give the relative position of each line and the circle.', r'Cho \((O;\,6\text{ cm})\) và các đường thẳng \(a\), \(b\), \(c\) cách \(O\) lần lượt 4 cm, 6 cm, 8 cm. Nêu vị trí tương đối của mỗi đường thẳng với đường tròn.'),
  ('Compare each \\(d\\) with \\(R=6\\).', 'So sánh mỗi \\(d\\) với \\(R=6\\).'),
  [T(r'\(4\lt6\): \(a\) cuts the circle (2 common points). \(6=6\): \(b\) is a tangent (1 common point).', r'\(4\lt6\): \(a\) cắt đường tròn (2 điểm chung). \(6=6\): \(b\) là tiếp tuyến (1 điểm chung).'),
   T(r'\(8\gt6\): \(c\) and the circle have no common point.', r'\(8\gt6\): \(c\) và đường tròn không giao nhau.')],
  T(r'\(a\): secant; \(b\): tangent; \(c\): no common point.', r'\(a\): cắt nhau; \(b\): tiếp xúc; \(c\): không giao nhau.'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Length of a tangent', 'Độ dài tiếp tuyến'),
  T(r'A circle has center \(O\) and radius 5 cm. \(PA\) is tangent to the circle at \(A\) and \(OP=13\) cm. a) Explain why \(\widehat{OAP}=90^\circ\). b) Find \(PA\).', r'Đường tròn tâm \(O\) bán kính 5 cm. \(PA\) là tiếp tuyến của đường tròn tại \(A\) và \(OP=13\) cm. a) Giải thích vì sao \(\widehat{OAP}=90^\circ\). b) Tính \(PA\).'),
  ('A tangent is perpendicular to the radius.', 'Tiếp tuyến vuông góc với bán kính tại tiếp điểm.'),
  [T(r'a) Since \(PA\) is tangent to the circle at \(A\), \(OA\perp PA\). Therefore, triangle \(OAP\) is a right triangle at \(A\).', r'a) Vì \(PA\) là tiếp tuyến tại \(A\) nên \(OA\perp PA\). Do đó tam giác \(OAP\) vuông tại \(A\).'),
   T(r'b) By the Pythagorean theorem, \(PA^2=OP^2-OA^2=169-25=144\), so \(PA=12\) cm.', r'b) Theo định lí Pythagore, \(PA^2=OP^2-OA^2=169-25=144\) nên \(PA=12\) cm.')],
  T(r'\(PA=12\) cm.', r'\(PA=12\) cm.'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('Two tangents', 'Hai tiếp tuyến cắt nhau'),
  T(r'In Example 2, a second tangent \(PB\) is drawn from \(P\) (\(B\) on the circle). Find \(PB\) and compare \(\widehat{APO}\) with \(\widehat{BPO}\).', r'Ở Ví dụ 2, kẻ thêm tiếp tuyến \(PB\) từ \(P\) (\(B\) thuộc đường tròn). Tính \(PB\) và so sánh \(\widehat{APO}\) với \(\widehat{BPO}\).'),
  ('Use the property of two tangents from one point.', 'Dùng tính chất hai tiếp tuyến cắt nhau.'),
  [T(r'The two tangent segments drawn from the same external point are equal: \(PB=PA=12\) cm.', r'Hai tiếp tuyến cắt nhau tại \(P\) nên \(PB=PA=12\) cm.'),
   T(r'\(PO\) bisects \(\widehat{APB}\), so \(\widehat{APO}=\widehat{BPO}\).', r'\(PO\) là tia phân giác của \(\widehat{APB}\) nên \(\widehat{APO}=\widehat{BPO}\).')],
  T(r'\(PB=12\) cm; the two angles are equal.', r'\(PB=12\) cm; hai góc bằng nhau.'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('A chord cut by a line', 'Dây cung tạo bởi cát tuyến'),
  T(r'Line \(a\) is 3 cm from the center of \((O;\,5\text{ cm})\). Show that \(a\) cuts the circle at two points \(A\), \(B\) and find \(AB\).', r'Đường thẳng \(a\) cách tâm của \((O;\,5\text{ cm})\) một đoạn 3 cm. Chứng minh \(a\) cắt đường tròn tại hai điểm \(A\), \(B\) và tính \(AB\).'),
  ('Draw \\(OH\\perp a\\).', 'Kẻ \\(OH\\perp a\\).'),
  [T(r'\(d=3\lt5=R\), so \(a\) is a secant. Let \(H\) be the foot of the perpendicular from \(O\); \(H\) is the midpoint of \(AB\).', r'\(d=3\lt5=R\) nên \(a\) cắt đường tròn tại hai điểm. Gọi \(H\) là chân đường vuông góc kẻ từ \(O\); \(H\) là trung điểm của \(AB\).'),
   T(r'\(AH=\sqrt{5^2-3^2}=4\) cm, so \(AB=8\) cm.', r'\(AH=\sqrt{5^2-3^2}=4\) cm nên \(AB=8\) cm.')],
  T(r'\(AB=8\) cm.', r'\(AB=8\) cm.'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Region between two tangents', 'Phần hình giữa hai tiếp tuyến'),
  T(r'From \(P\), tangents \(PA\), \(PB\) are drawn to \((O;\,5\text{ cm})\) with \(OP=10\) cm. a) Find \(PA\). b) Find \(\widehat{AOP}\) and \(\widehat{AOB}\). c) Find the area of \(OAPB\). d) Find the area enclosed by \(PA\), \(PB\) and the minor arc \(AB\) (two decimal places).', r'Từ \(P\) kẻ hai tiếp tuyến \(PA\), \(PB\) tới \((O;\,5\text{ cm})\) với \(OP=10\) cm. a) Tính \(PA\). b) Tính \(\widehat{AOP}\) và \(\widehat{AOB}\). c) Tính diện tích tứ giác \(OAPB\). d) Tính diện tích phần hình giới hạn bởi \(PA\), \(PB\) và cung nhỏ \(AB\) (làm tròn đến chữ số thập phân thứ hai).'),
  ('Use \\(\\cos\\widehat{AOP}=\\dfrac{OA}{OP}\\) and the sector area from Lesson 15.', 'Dùng \\(\\cos\\widehat{AOP}=\\dfrac{OA}{OP}\\) và diện tích hình quạt ở Bài 15.'),
  [T(r'a) \(PA=\sqrt{10^2-5^2}=5\sqrt3\) cm. b) \(\cos\widehat{AOP}=\dfrac{5}{10}=\dfrac12\Rightarrow\widehat{AOP}=60^\circ\); \(\widehat{AOB}=120^\circ\).', r'a) \(PA=\sqrt{10^2-5^2}=5\sqrt3\) cm. b) \(\cos\widehat{AOP}=\dfrac{5}{10}=\dfrac12\Rightarrow\widehat{AOP}=60^\circ\); \(\widehat{AOB}=120^\circ\).'),
   T(r'c) \(S_{OAPB}=2\cdot\dfrac12\cdot OA\cdot PA=5\cdot5\sqrt3=25\sqrt3\) cm².', r'c) \(S_{OAPB}=2\cdot\dfrac12\cdot OA\cdot PA=5\cdot5\sqrt3=25\sqrt3\) cm².'),
   T(r'd) Sector \(AOB\): \(\dfrac{\pi\cdot5^2\cdot120}{360}=\dfrac{25\pi}{3}\). Required area \(=25\sqrt3-\dfrac{25\pi}{3}\approx17.12\) cm².', r'd) Hình quạt \(AOB\): \(\dfrac{\pi\cdot5^2\cdot120}{360}=\dfrac{25\pi}{3}\). Diện tích cần tìm \(=25\sqrt3-\dfrac{25\pi}{3}\approx17{,}12\) cm².')],
  T(r'\(5\sqrt3\) cm; \(60^\circ\), \(120^\circ\); \(25\sqrt3\) cm²; about 17.12 cm².', r'\(5\sqrt3\) cm; \(60^\circ\), \(120^\circ\); \(25\sqrt3\) cm²; khoảng 17,12 cm².'))

_SETS = sp_g9.BANK(sp_g9.L16_GROUPS, start=1, seeds=(2601, 2602, 2603))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Comparing \(d\) with the diameter.</b> Compare the distance \(d\) with \(R\), not with \(2R\).', r'<b>So sánh \(d\) với đường kính.</b> Phải so sánh \(d\) với \(R\), không phải với \(2R\).'),
 (r'<b>Adding instead of subtracting.</b> \(PA=\sqrt{OP^2-R^2}\), not \(\sqrt{OP^2+R^2}\).', r'<b>Cộng thay vì trừ.</b> \(PA=\sqrt{OP^2-R^2}\), không phải \(\sqrt{OP^2+R^2}\).'),
 (r'<b>Half chord.</b> \(\sqrt{R^2-d^2}\) is half of the chord; double it.', r'<b>Quên nhân đôi.</b> \(\sqrt{R^2-d^2}\) chỉ là nửa dây; phải nhân 2.'),
 (r'<b>Distance along any segment.</b> \(d\) is measured along the perpendicular from \(O\).', r'<b>Đo khoảng cách sai.</b> \(d\) là độ dài đoạn vuông góc kẻ từ \(O\) đến đường thẳng.')]
summary = [
 (r'\(d\lt R\): 2 common points; \(d=R\): tangent; \(d\gt R\): no common point.', r'\(d\lt R\): cắt nhau; \(d=R\): tiếp xúc; \(d\gt R\): không giao nhau.'),
 (r'Tangent at \(A\) ⟺ the line passes through \(A\) and is perpendicular to \(OA\).', r'Tiếp tuyến tại \(A\) ⟺ đường thẳng đi qua \(A\) và vuông góc với \(OA\).'),
 (r'Two tangents from \(P\): \(PA=PB\), \(PO\) bisects \(\widehat{APB}\) and \(OP\) bisects \(\widehat{AOB}\).', r'Hai tiếp tuyến cắt nhau tại \(P\): \(PA=PB\), \(PO\) là phân giác \(\widehat{APB}\), \(OP\) là phân giác \(\widehat{AOB}\).'),
 (r'Key English: secant, tangent, point of tangency, distance from a point to a line, perpendicular, tangent segments, no common point.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[cát tuyến (của đường tròn)]], [[tiếp tuyến (của đường tròn)]], [[tiếp điểm]], [[khoảng cách từ một điểm đến một đường thẳng]], [[vuông góc]], [[hai tiếp tuyến cắt nhau]], [[không giao nhau]].')]
checks = [
 (r'I can give the relative position of a line and a circle from \(d\) and \(R\).', r'Em xác định được vị trí tương đối của đường thẳng và đường tròn qua \(d\) và \(R\).'),
 (r'I can recognize and prove a tangent.', r'Em nhận biết và chứng minh được tiếp tuyến.'),
 (r'I can use the property of two tangents from one point.', r'Em vận dụng được tính chất hai tiếp tuyến cắt nhau.'),
 (r'I can compute tangent lengths and chord lengths.', r'Em tính được độ dài tiếp tuyến và độ dài dây.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Relative Positions of a Line and a Circle', title_vi='Vị trí tương đối của đường thẳng và đường tròn', topic=TOPIC,
       folder='circles', file='line-and-circle', catalog_title_vi='Vị trí tương đối của đường thẳng và đường tròn',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Secants, tangents and lines missing a circle; tangent properties; two tangents from a point.', level='Intermediate', minutes=90,
       description_vi='Bài 16 – Ba vị trí tương đối của đường thẳng và đường tròn; tiếp tuyến; tính chất hai tiếp tuyến cắt nhau.',
       tags_vi=['tiếp tuyến', 'cát tuyến', 'vị trí tương đối'], prerequisites=['g9-circles-02'], tags=['tangent', 'secant', 'circle'], order=160)
