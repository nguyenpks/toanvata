# -*- coding: utf-8 -*-
"""Nội dung bài g9-inscribed-02 = Toán 9 KNTT, Bài 28: Đường tròn ngoại tiếp và đường tròn nội tiếp của một tam giác – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 9 – Lesson 28."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9, sp_g9p, sp_g9q as Q

LID = 'g9-inscribed-02'
CH = 'Đường tròn ngoại tiếp và đường tròn nội tiếp'
TOPIC = ('Circumcircle and Incircle', CH)
ensure_vocab([
 ('g9-circumcircle', 'circumcircle', 'đường tròn ngoại tiếp (tam giác, đa giác)', CH, 'The circumcircle of a triangle passes through its three vertices.', ''),
 ('g9-incircle', 'incircle', 'đường tròn nội tiếp (tam giác, đa giác)', CH, 'The incircle of a triangle touches its three sides.', ''),
 ('g9-circumcenter', 'circumcenter', 'tâm đường tròn ngoại tiếp (tam giác)', CH, 'The circumcenter is equidistant from the three vertices.', ''),
 ('g9-incenter', 'incenter', 'tâm đường tròn nội tiếp (tam giác)', CH, 'The incenter is equidistant from the three sides.', ''),
 ('g9-perp-bisector', 'perpendicular bisector', 'đường trung trực (của đoạn thẳng)', CH, 'The perpendicular bisectors of the sides meet at the circumcenter.', ''),
 ('g9-angle-bisector', 'angle bisector', 'đường phân giác (của góc)', CH, 'The angle bisectors meet at the incenter.', ''),
])
load_vocab()

def FIG(fn, cap, px=300): return '<figure class="mbl-fig mbl-figtex">%s<figcaption>%s</figcaption></figure>' % (sp_g9p.img(fn, cap[0], px), TI(*cap))

# ---------- số liệu (kiểm tra bằng máy) ----------
PA, PB, PC = (-1.6, -1.0), (2.2, -1.0), (0.4, 1.9)
ox, oy, R0 = Q.circum(PA, PB, PC); ix, iy, r0 = Q.incircle(PA, PB, PC)
assert abs(math.dist((ox, oy), PA) - math.dist((ox, oy), PC)) < 1e-9
F_CIRC = FIG(Q.tfig(P={'A': PA, 'B': PB, 'C': PC, 'O': (ox, oy)}, circles=[(ox, oy, R0)], segs=[('A', 'B'), ('B', 'C'), ('C', 'A')], dash=[('O', 'A'), ('O', 'B'), ('O', 'C')]),
             ('Circumcircle \\((O;\\,R)\\): \\(OA=OB=OC=R\\).', 'Đường tròn ngoại tiếp \\((O;\\,R)\\): \\(OA=OB=OC=R\\).'))
def foot(P, U, V):
    ux, uy = V[0] - U[0], V[1] - U[1]; t = ((P[0] - U[0]) * ux + (P[1] - U[1]) * uy) / (ux * ux + uy * uy); return (U[0] + t * ux, U[1] + t * uy)
HD, HE, HF = foot((ix, iy), PB, PC), foot((ix, iy), PC, PA), foot((ix, iy), PA, PB)
assert abs(math.dist((ix, iy), HD) - r0) < 1e-9 and abs(math.dist((ix, iy), HF) - r0) < 1e-9
F_INC = FIG(Q.tfig(P={'A': PA, 'B': PB, 'C': PC, 'I': (ix, iy), 'D': HD, 'E': HE, 'F': HF}, circles=[(ix, iy, r0)], segs=[('A', 'B'), ('B', 'C'), ('C', 'A')],
                   dash=[('I', 'D'), ('I', 'E'), ('I', 'F')], right=[('I', 'F', 'B')], dots=['A', 'B', 'C', 'I', 'D', 'E', 'F']),
            ('Incircle \\((I;\\,r)\\): \\(ID=IE=IF=r\\).', 'Đường tròn nội tiếp \\((I;\\,r)\\): \\(ID=IE=IF=r\\).'))
F_RIGHT = FIG(Q.tfig(P={'A': (0, 0), 'B': (3, 0), 'C': (0, 2.25), 'O': (1.5, 1.125)}, circles=[(1.5, 1.125, 1.875)], segs=[('A', 'B'), ('B', 'C'), ('C', 'A')], dash=[('O', 'A')], right=[('B', 'A', 'C')]),
              ('Right triangle: the circumcenter is the midpoint of the hypotenuse.', 'Tam giác vuông: tâm đường tròn ngoại tiếp là trung điểm cạnh huyền.'))
assert math.dist((1.5, 1.125), (0, 0)) == 1.875 == math.dist((1.5, 1.125), (3, 0))
s3 = math.sqrt(3); assert abs(6 * s3 / 3 - 2 * s3) < 1e-12 and abs(6 * s3 / 6 - s3) < 1e-12
assert (6, 8, 10) and 6 ** 2 + 8 ** 2 == 100

meta = dict(level=('Basic', 'Cơ bản'), time=('about 90 minutes', '90 phút'), before=('Grade 7: perpendicular bisectors, angle bisectors; Lesson 27', 'Lớp 7: đường trung trực, đường phân giác; Bài 27'))
goals = [
 (r'recognize the circumcircle and the incircle of a triangle and their centers;', r'nhận biết được đường tròn ngoại tiếp, đường tròn nội tiếp của tam giác và tâm của chúng;'),
 (r'know that the circumcenter of a right triangle is the midpoint of the hypotenuse;', r'biết tâm đường tròn ngoại tiếp tam giác vuông là trung điểm cạnh huyền;'),
 (r'compute \(R\) and \(r\) of right triangles and equilateral triangles;', r'tính được \(R\), \(r\) của tam giác vuông, tam giác đều;'),
 (r'solve real problems (a lamp equally far from three points, the largest round flower bed).', r'giải được bài toán thực tế (đèn cách đều ba điểm, bồn hoa tròn lớn nhất).')]
vocab = [
 (r'<b>circumcircle / circumcenter / circumradius</b> – the circle through the three vertices; its center \(O\); its radius \(R\).', r'[[Đường tròn ngoại tiếp|đường tròn ngoại tiếp (tam giác, đa giác)]] – đường tròn đi qua ba đỉnh; [[tâm|tâm đường tròn ngoại tiếp (tam giác)]] \(O\); bán kính \(R\).'),
 (r'<b>incircle / incenter / inradius</b> – the circle touching the three sides; its center \(I\); its radius \(r\).', r'[[Đường tròn nội tiếp|đường tròn nội tiếp (tam giác, đa giác)]] – đường tròn tiếp xúc với ba cạnh; [[tâm|tâm đường tròn nội tiếp (tam giác)]] \(I\); bán kính \(r\).'),
 (r'<b>perpendicular bisector</b> – the line perpendicular to a segment at its midpoint.', r'[[Đường trung trực|đường trung trực (của đoạn thẳng)]] – đường thẳng vuông góc với đoạn thẳng tại trung điểm.'),
 (r'<b>angle bisector</b> – the ray dividing an angle into two equal angles.', r'[[Đường phân giác|đường phân giác (của góc)]] – tia chia góc thành hai góc bằng nhau.'),
 (r'<b>equidistant</b> – at equal distances.', r'Cách đều – có khoảng cách bằng nhau.')]
phrases = [
 (r'<b>Triangle \(ABC\) is inscribed in the circle \((O)\).</b>', r'Tam giác \(ABC\) nội tiếp đường tròn \((O)\).'),
 (r'<b>The circle \((I)\) is inscribed in triangle \(ABC\).</b>', r'Đường tròn \((I)\) nội tiếp tam giác \(ABC\).'),
 (r'<b>The circumcenter is equidistant from the three vertices.</b>', r'Tâm đường tròn ngoại tiếp cách đều ba đỉnh.'),
 (r'<b>The incenter is equidistant from the three sides.</b>', r'Tâm đường tròn nội tiếp cách đều ba cạnh.'),
 (r'<b>Find the circumradius and the inradius.</b>', r'Tính bán kính đường tròn ngoại tiếp và bán kính đường tròn nội tiếp.')]
review = (T(r'<b>Grade 7.</b> The three perpendicular bisectors of a triangle meet at one point, equidistant from the vertices; the three angle bisectors meet at one point, equidistant from the sides.',
            r'<b>Lớp 7.</b> Ba đường trung trực của tam giác cùng đi qua một điểm, điểm này cách đều ba đỉnh; ba đường phân giác cùng đi qua một điểm, điểm này cách đều ba cạnh.') +
          T(r'<b>Lesson 27.</b> An inscribed angle subtending a semicircle is a right angle.', r'<b>Bài 27.</b> Góc nội tiếp chắn nửa đường tròn là góc vuông.'))

theory = '<h3>5.1 %s</h3>' % TI('The circumcircle of a triangle', 'Đường tròn ngoại tiếp tam giác')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'The circle passing through the three vertices of a triangle is its <b>circumcircle</b>; the triangle is <b>inscribed</b> in the circle.', r'Đường tròn đi qua ba đỉnh của một tam giác gọi là [[đường tròn ngoại tiếp|đường tròn ngoại tiếp (tam giác, đa giác)]] tam giác đó; khi đó tam giác được gọi là <b>nội tiếp</b> đường tròn.'),
  T(r'Its center \(O\) is the intersection of the three <b>perpendicular bisectors</b> of the sides; \(OA=OB=OC=R\).', r'Tâm \(O\) là giao điểm của ba [[đường trung trực|đường trung trực (của đoạn thẳng)]] của ba cạnh; \(OA=OB=OC=R\).'))
theory += F_CIRC
theory += BOX('mint', ('Special cases', 'Trường hợp đặc biệt'),
  UL([T(r'Right triangle: the circumcenter is the <b>midpoint of the hypotenuse</b>, \(R=\dfrac{\text{hypotenuse}}{2}\).', r'Tam giác vuông: tâm đường tròn ngoại tiếp là <b>trung điểm cạnh huyền</b>, \(R=\dfrac{\text{cạnh huyền}}{2}\).'),
      T(r'Equilateral triangle with side \(a\): \(R=\dfrac{a\sqrt3}{3}\) (the center is the centroid, \(R=\dfrac23h\), \(h=\dfrac{a\sqrt3}{2}\)).', r'Tam giác đều cạnh \(a\): \(R=\dfrac{a\sqrt3}{3}\) (tâm là trọng tâm, \(R=\dfrac23h\) với \(h=\dfrac{a\sqrt3}{2}\)).')]))
theory += F_RIGHT
theory += '<h3>5.2 %s</h3>' % TI('The incircle of a triangle', 'Đường tròn nội tiếp tam giác')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'The circle touching the three sides of a triangle is its <b>incircle</b>; the triangle is <b>circumscribed</b> about the circle.', r'Đường tròn tiếp xúc với ba cạnh của một tam giác gọi là [[đường tròn nội tiếp|đường tròn nội tiếp (tam giác, đa giác)]] tam giác đó; khi đó tam giác được gọi là <b>ngoại tiếp</b> đường tròn.'),
  T(r'Its center \(I\) is the intersection of the three <b>angle bisectors</b>; \(I\) is equidistant from the sides: \(ID=IE=IF=r\).', r'Tâm \(I\) là giao điểm của ba [[đường phân giác|đường phân giác (của góc)]] trong của tam giác; \(I\) cách đều ba cạnh: \(ID=IE=IF=r\).'),
  T(r'Equilateral triangle with side \(a\): \(I\equiv O\) and \(r=\dfrac{a\sqrt3}{6}=\dfrac{R}{2}\).', r'Tam giác đều cạnh \(a\): \(I\) trùng \(O\) và \(r=\dfrac{a\sqrt3}{6}=\dfrac{R}{2}\).'))
theory += F_INC

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Which center?', 'Tâm nào?'),
  T(r'(a) Which lines meet at the center of the circumcircle of a triangle? (b) Which point of a triangle is equidistant from its three sides?', r'a) Những đường nào đi qua tâm đường tròn ngoại tiếp tam giác? b) Điểm nào của tam giác cách đều ba cạnh?'),
  ('Circumcircle ↔ vertices ↔ perpendicular bisectors; incircle ↔ sides ↔ angle bisectors.', 'Đường tròn ngoại tiếp ↔ ba đỉnh ↔ đường trung trực; đường tròn nội tiếp ↔ ba cạnh ↔ đường phân giác.'),
  [T(r'(a) The three perpendicular bisectors of the sides.', r'a) Ba đường trung trực của ba cạnh.'), T(r'(b) The incenter, the intersection of the three angle bisectors.', r'b) Tâm đường tròn nội tiếp, giao điểm của ba đường phân giác.')],
  T(r'(a) Perpendicular bisectors; (b) the incenter.', r'a) Ba đường trung trực; b) tâm đường tròn nội tiếp.'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('A right triangle', 'Tam giác vuông'),
  T(r'Triangle \(ABC\) is right-angled at \(A\) with \(AB=6\) cm, \(AC=8\) cm. Find the center and the radius of its circumcircle.', r'Tam giác \(ABC\) vuông tại \(A\) có \(AB=6\) cm, \(AC=8\) cm. Xác định tâm và tính bán kính đường tròn ngoại tiếp tam giác.'),
  ('\\(\\widehat{BAC}=90^\\circ\\) subtends a semicircle, so \\(BC\\) is a diameter.', '\\(\\widehat{BAC}=90^\\circ\\) chắn nửa đường tròn nên \\(BC\\) là đường kính.'),
  [T(r'\(BC=\sqrt{6^2+8^2}=10\) cm.', r'\(BC=\sqrt{6^2+8^2}=10\) cm.'), T(r'The center is the midpoint \(O\) of \(BC\); \(R=\dfrac{10}{2}=5\) cm.', r'Tâm là trung điểm \(O\) của \(BC\); \(R=\dfrac{10}{2}=5\) cm.')],
  T(r'The midpoint of \(BC\); \(R=5\) cm.', r'Trung điểm \(BC\); \(R=5\) cm.'))
examples += EXAMPLE(3, ('Basic application', 'Vận dụng thấp'), ('An equilateral triangle', 'Tam giác đều'),
  T(r'An equilateral triangle has side 6 cm. Find its circumradius \(R\) and inradius \(r\).', r'Tam giác đều có cạnh 6 cm. Tính bán kính \(R\) của đường tròn ngoại tiếp và bán kính \(r\) của đường tròn nội tiếp.'),
  ('The center is the centroid: it divides each height in the ratio \\(2:1\\).', 'Tâm là trọng tâm: chia mỗi đường cao theo tỉ số \\(2:1\\).'),
  [T(r'Height \(h=\dfrac{6\sqrt3}{2}=3\sqrt3\) cm.', r'Đường cao \(h=\dfrac{6\sqrt3}{2}=3\sqrt3\) cm.'), T(r'\(R=\dfrac23h=2\sqrt3\) cm, \(r=\dfrac13h=\sqrt3\) cm.', r'\(R=\dfrac23h=2\sqrt3\) cm, \(r=\dfrac13h=\sqrt3\) cm.')],
  T(r'\(R=2\sqrt3\) cm, \(r=\sqrt3\) cm.', r'\(R=2\sqrt3\) cm, \(r=\sqrt3\) cm.'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('From \\(R\\) to the side', 'Từ \\(R\\) tính cạnh'),
  T(r'An equilateral triangle is inscribed in a circle of radius 4 cm. Find its side and its area.', r'Tam giác đều nội tiếp đường tròn bán kính 4 cm. Tính cạnh và diện tích của tam giác.'),
  ('\\(R=\\dfrac{a\\sqrt3}{3}\\Rightarrow a=R\\sqrt3\\).', '\\(R=\\dfrac{a\\sqrt3}{3}\\Rightarrow a=R\\sqrt3\\).'),
  [T(r'\(a=4\sqrt3\) cm; \(h=\dfrac{a\sqrt3}{2}=6\) cm.', r'\(a=4\sqrt3\) cm; \(h=\dfrac{a\sqrt3}{2}=6\) cm.'), T(r'\(S=\dfrac12\cdot4\sqrt3\cdot6=12\sqrt3\) cm².', r'\(S=\dfrac12\cdot4\sqrt3\cdot6=12\sqrt3\) cm².')],
  T(r'\(4\sqrt3\) cm; \(12\sqrt3\) cm².', r'\(4\sqrt3\) cm; \(12\sqrt3\) cm².'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('A lamp and a flower bed', 'Đèn chiếu và bồn hoa'),
  T(r'(a) A garden has the shape of a right triangle \(ABC\) (right angle at \(A\)), \(AB=9\) m, \(AC=12\) m. Where should a lamp be placed so that it is equally far from \(A\), \(B\), \(C\), and how far? (b) A yard is an equilateral triangle with side 12 m. Find the radius of the largest round flower bed inside it.',
    r'a) Một khu vườn có dạng tam giác vuông \(ABC\) (vuông tại \(A\)), \(AB=9\) m, \(AC=12\) m. Đặt đèn ở đâu để cách đều \(A\), \(B\), \(C\), và cách bao xa? b) Một sân có dạng tam giác đều cạnh 12 m. Tính bán kính của bồn hoa hình tròn lớn nhất đặt trong sân.'),
  ('(a) circumcenter; (b) the largest circle inside a triangle is its incircle.', 'a) tâm đường tròn ngoại tiếp; b) hình tròn lớn nhất nằm trong tam giác là hình tròn nội tiếp.'),
  [T(r'(a) \(BC=\sqrt{9^2+12^2}=15\) m; the lamp is at the midpoint of \(BC\), 7.5 m from each corner.', r'a) \(BC=\sqrt{9^2+12^2}=15\) m; đặt đèn tại trung điểm \(BC\), cách mỗi góc 7,5 m.'),
   T(r'(b) \(r=\dfrac{12\sqrt3}{6}=2\sqrt3\approx3.5\) m.', r'b) \(r=\dfrac{12\sqrt3}{6}=2\sqrt3\approx3{,}5\) m.')],
  T(r'(a) Midpoint of \(BC\), 7.5 m; (b) \(2\sqrt3\approx3.5\) m.', r'a) Trung điểm \(BC\), 7,5 m; b) \(2\sqrt3\approx3{,}5\) m.'))
assert 9 ** 2 + 12 ** 2 == 225 and abs(2 * math.sqrt(3) - 3.464) < 1e-3

_SETS = sp_g9.BANK(Q.L28_GROUPS, start=1, seeds=(2801, 2802, 2803))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Mixing up the two centers.</b> Circumcenter: perpendicular bisectors (equidistant from vertices). Incenter: angle bisectors (equidistant from sides).', r'<b>Nhầm hai tâm.</b> Tâm ngoại tiếp: giao ba đường trung trực (cách đều ba đỉnh). Tâm nội tiếp: giao ba đường phân giác (cách đều ba cạnh).'),
 (r'<b>Taking \(R\) equal to the hypotenuse.</b> \(R\) is half the hypotenuse.', r'<b>Lấy \(R\) bằng cạnh huyền.</b> \(R\) bằng nửa cạnh huyền.'),
 (r'<b>Swapping the formulas.</b> Equilateral triangle: \(R=\dfrac{a\sqrt3}{3}\), \(r=\dfrac{a\sqrt3}{6}\); \(R=2r\).', r'<b>Đổi chỗ hai công thức.</b> Tam giác đều: \(R=\dfrac{a\sqrt3}{3}\), \(r=\dfrac{a\sqrt3}{6}\); \(R=2r\).'),
 (r'<b>Thinking the circumcenter is always inside.</b> It is outside for an obtuse triangle.', r'<b>Nghĩ tâm ngoại tiếp luôn nằm trong tam giác.</b> Với tam giác tù, tâm nằm ngoài tam giác.')]
summary = [
 (r'Circumcircle: through the 3 vertices; center = intersection of the perpendicular bisectors.', r'Đường tròn ngoại tiếp: đi qua 3 đỉnh; tâm là giao điểm ba đường trung trực.'),
 (r'Incircle: touches the 3 sides; center = intersection of the angle bisectors.', r'Đường tròn nội tiếp: tiếp xúc 3 cạnh; tâm là giao điểm ba đường phân giác.'),
 (r'Right triangle: \(R=\dfrac{\text{hypotenuse}}{2}\). Equilateral triangle: \(R=\dfrac{a\sqrt3}{3}\), \(r=\dfrac{a\sqrt3}{6}\).', r'Tam giác vuông: \(R=\dfrac{\text{cạnh huyền}}{2}\). Tam giác đều: \(R=\dfrac{a\sqrt3}{3}\), \(r=\dfrac{a\sqrt3}{6}\).'),
 (r'Key English: circumcircle, circumcenter, incircle, incenter, perpendicular bisector, angle bisector.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[đường tròn ngoại tiếp|đường tròn ngoại tiếp (tam giác, đa giác)]], [[đường tròn nội tiếp|đường tròn nội tiếp (tam giác, đa giác)]], [[đường trung trực|đường trung trực (của đoạn thẳng)]], [[đường phân giác|đường phân giác (của góc)]].')]
checks = [
 (r'I can tell the circumcircle from the incircle and locate their centers.', r'Em phân biệt được đường tròn ngoại tiếp, nội tiếp và xác định được tâm của chúng.'),
 (r'I can find \(R\) of a right triangle.', r'Em tính được \(R\) của tam giác vuông.'),
 (r'I can find \(R\) and \(r\) of an equilateral triangle.', r'Em tính được \(R\), \(r\) của tam giác đều.'),
 (r'I can solve real problems with these circles.', r'Em giải được bài toán thực tế liên quan.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Circumcircle and Incircle of a Triangle', title_vi='Đường tròn ngoại tiếp và đường tròn nội tiếp của một tam giác', topic=TOPIC,
       folder='circumcircle-incircle', file='circumcircle-incircle-triangle', catalog_title_vi='Đường tròn ngoại tiếp và đường tròn nội tiếp của một tam giác',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Circumcircle and incircle of a triangle; circumcenter of a right triangle; R and r of an equilateral triangle.', level='Basic', minutes=90,
       description_vi='Bài 28 – Đường tròn ngoại tiếp, nội tiếp tam giác; tâm đường tròn ngoại tiếp tam giác vuông; bán kính của tam giác đều.',
       tags_vi=['đường tròn ngoại tiếp', 'đường tròn nội tiếp', 'tam giác đều'], prerequisites=['g9-inscribed-01'], tags=['circumcircle', 'incircle', 'equilateral triangle'], order=280)
