# -*- coding: utf-8 -*-
"""Nội dung bài g9-circles-01 = Toán 9 KNTT, Bài 13: Mở đầu về đường tròn – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 5 – Lesson 13 (chỉ lấy phần đúng bài, xem D6)."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9

LID = 'g9-circles-01'
CH = 'Đường tròn'
TOPIC = ('Circles', CH)
ensure_vocab([
 ('g9-circle', 'circle', 'đường tròn', CH, 'The circle has center O and radius R.', r'\((O;\,R)\)'),
 ('g9-center', 'center (of a circle)', 'tâm (của đường tròn)', CH, 'The point O is the center of the circle.', ''),
 ('g9-radius', 'radius (pl. radii)', 'bán kính', CH, 'OA and OB are radii of the same circle, so OA = OB.', 'R'),
 ('g9-diameter', 'diameter', 'đường kính', CH, 'A diameter is a chord through the center; its length is 2R.', ''),
 ('g9-distance', 'distance', 'khoảng cách', CH, 'Compare the distance OM with the radius R.', ''),
 ('g9-concyclic', 'lie on the same circle', 'cùng nằm trên một đường tròn', CH, 'Points A, B, C and D lie on the same circle.', ''),
])
load_vocab()

# ---------- kiểm tra số liệu ----------
assert 2.5 < 3 and 5 == 5 and 7 > 5
assert math.hypot(6, 8) / 2 == 5 and math.hypot(5, 12) / 2 == 6.5
assert math.hypot(30, 40) == 50 and 50 < 60

meta = dict(level=('Basic', 'Cơ bản'), time=('about 60 minutes', '60 phút'),
            before=('Grade 7: isosceles triangles, perpendicular bisector; grade 8: Pythagorean theorem', 'Lớp 7: tam giác cân, đường trung trực; lớp 8: định lí Pythagore'))
goals = [
 (r'state the definition of a circle; use the words center, radius, diameter;', r'nêu được định nghĩa đường tròn; dùng đúng các từ tâm, bán kính, đường kính;'),
 (r'decide whether a point lies inside, on or outside a circle;', r'xác định được vị trí của một điểm đối với đường tròn;'),
 (r'know that a circle is symmetric about its center and about every line through its center;', r'biết đường tròn có tâm đối xứng là tâm và trục đối xứng là mọi đường thẳng đi qua tâm;'),
 (r'show that several points lie on the same circle and solve simple real-life problems.', r'chứng minh được nhiều điểm cùng nằm trên một đường tròn và giải bài toán thực tế đơn giản.')]
vocab = [
 (r'<b>circle</b> \((O;\,R)\) – all points at distance \(R\) from \(O\).', r'[[Đường tròn]] \((O;\,R)\) – gồm tất cả các điểm cách \(O\) đúng bằng \(R\).'),
 (r'<b>center / radius</b> – the point \(O\) / the distance \(R\) (also a segment \(OA\)).', r'[[Tâm|tâm (của đường tròn)]] / [[bán kính]] – điểm \(O\) / độ dài \(R\) (cũng chỉ đoạn \(OA\)).'),
 (r'<b>diameter</b> – a segment through \(O\) with both ends on the circle; length \(2R\).', r'[[Đường kính]] – đoạn thẳng đi qua \(O\), hai đầu nằm trên đường tròn; dài \(2R\).'),
 (r'<b>lie inside / on / outside the circle</b> – \(OM\lt R\) / \(OM=R\) / \(OM\gt R\).', r'Nằm trong / nằm trên / nằm ngoài đường tròn – \(OM\lt R\) / \(OM=R\) / \(OM\gt R\).'),
 (r'<b>center of symmetry / axis of symmetry</b> – the center \(O\) / every line through \(O\).', r'[[Tâm đối xứng]] / [[trục đối xứng]] – tâm \(O\) / mọi đường thẳng đi qua \(O\).')]
phrases = [
 (r'<b>The circle has center \(O\) and radius \(R\).</b>', r'Đường tròn có tâm \(O\), bán kính \(R\).'),
 (r'<b>Points \(A\), \(B\) and \(C\) lie on the circle.</b>', r'Các điểm \(A\), \(B\), \(C\) nằm trên đường tròn.'),
 (r'<b>Since \(OA\) and \(OB\) are radii of the same circle, \(OA=OB\).</b>', r'Vì \(OA\), \(OB\) là bán kính của cùng một đường tròn nên \(OA=OB\).'),
 (r'<b>Therefore, triangle \(OAB\) is isosceles.</b>', r'Do đó tam giác \(OAB\) cân tại \(O\).'),
 (r'<b>Hence, we can conclude that the four points lie on the same circle.</b>', r'Vậy ta kết luận bốn điểm cùng nằm trên một đường tròn.')]
review = (T(r'<b>Isosceles triangle.</b> If \(OA=OB\) then \(\widehat{OAB}=\widehat{OBA}\).', r'<b>Tam giác cân.</b> Nếu \(OA=OB\) thì \(\widehat{OAB}=\widehat{OBA}\).') +
          T(r'<b>Rectangle.</b> The two diagonals are equal and bisect each other.', r'<b>Hình chữ nhật.</b> Hai đường chéo bằng nhau và cắt nhau tại trung điểm mỗi đường.'))

G = lambda cfg, en, vi, hgt=290: GEO(sp_g9.auto_labels(cfg), cap=(en, vi), alt=(en, ''), height=hgt)
def pt(i, x, y, name=None, size=3): return {'type': 'point', 'id': i, 'at': [round(x, 4), round(y, 4)], 'name': i if name is None else name, 'style': {'size': size}}
def seg(a, b, **st): return {'type': 'segment', 'through': [a, b], 'style': st}
def txt(x, y, s): return {'type': 'text', 'at': [x, y], 'text': s}

R = 2.5; a = math.radians(40)
FIG1 = G({'view': [-3.4, 4.4, -2.9, 3.0], 'steps': [pt('O', 0, 0), pt('N', R * math.cos(a), R * math.sin(a)), pt('M', -1.1, -0.6), pt('P', 3.3, -2.0),
          {'type': 'circle', 'center': 'O', 'radius': R}, seg('O', 'N'), seg('O', 'M', dash=True), seg('O', 'P', dash=True), txt(0.62, 1.05, 'R')]},
         'Circle (O; R): M is inside (OM < R), N is on the circle (ON = R), P is outside (OP > R).', 'Đường tròn (O; R): M nằm trong (OM < R), N nằm trên (ON = R), P nằm ngoài (OP > R) đường tròn.')
u = (2 / 5 ** .5, 1 / 5 ** .5); A = (2.2 * math.cos(math.radians(105)), 2.2 * math.sin(math.radians(105))); k = A[0] * u[0] + A[1] * u[1]
A2 = (2 * k * u[0] - A[0], 2 * k * u[1] - A[1]); B = (2.2 * math.cos(math.radians(160)), 2.2 * math.sin(math.radians(160)))
assert abs(math.hypot(*A2) - 2.2) < 1e-9
FIG2 = G({'view': [-3.2, 3.6, -2.8, 2.8], 'steps': [pt('O', 0, 0), pt('A', *A), pt('A1', *A2, name="A'"), pt('B', *B), pt('B1', -B[0], -B[1], name="B'"),
          {'type': 'circle', 'center': 'O', 'radius': 2.2}, {'type': 'lineeq', 'a': 1, 'b': -2, 'c': 0}, seg('A', 'A1', dash=True), seg('B', 'B1', dash=True), txt(2.95, 1.2, 'd')]},
         "A' is symmetric to A with respect to the line d through O; B' is symmetric to B with respect to O. Both images lie on the circle.",
         "A' đối xứng với A qua đường thẳng d đi qua O; B' đối xứng với B qua O. Cả A' và B' đều nằm trên đường tròn.")

theory = '<h3>5.1 %s</h3>' % TI('Circle and the position of a point', 'Đường tròn. Vị trí tương đối của điểm và đường tròn')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'The <b>circle</b> with center \(O\) and radius \(R\) \((R\gt0)\), written \((O;\,R)\) or \((O)\), is the set of all points at distance \(R\) from \(O\).', r'[[Đường tròn]] tâm \(O\) bán kính \(R\) \((R\gt0)\), kí hiệu \((O;\,R)\) hoặc \((O)\), là hình gồm tất cả các điểm cách \(O\) đúng bằng \(R\).'),
  T(r'A <b>diameter</b> passes through \(O\) and has both endpoints on the circle; its length is \(2R\).', r'[[Đường kính]] đi qua \(O\), hai đầu mút nằm trên đường tròn; độ dài bằng \(2R\).'))
theory += FIG1
theory += TABLE([('Position of \\(M\\)', 'Vị trí của điểm \\(M\\)'), ('Condition', 'Hệ thức')],
  [[TI('\\(M\\) lies inside \\((O;\\,R)\\)', '\\(M\\) nằm trong \\((O;\\,R)\\)'), TI('\\(OM\\lt R\\)', '\\(OM\\lt R\\)')],
   [TI('\\(M\\) lies on \\((O;\\,R)\\)', '\\(M\\) nằm trên \\((O;\\,R)\\)'), TI('\\(OM=R\\)', '\\(OM=R\\)')],
   [TI('\\(M\\) lies outside \\((O;\\,R)\\)', '\\(M\\) nằm ngoài \\((O;\\,R)\\)'), TI('\\(OM\\gt R\\)', '\\(OM\\gt R\\)')]])
theory += '<h3>5.2 %s</h3>' % TI('Symmetry of a circle', 'Tính đối xứng của đường tròn')
theory += BOX('mint', ('Properties', 'Tính chất'),
  T(r'A circle is symmetric about its center: its center is its <b>center of symmetry</b>.', r'Đường tròn là hình có tâm đối xứng; [[tâm đối xứng]] là tâm của đường tròn.'),
  T(r'A circle is symmetric about every line through its center: each such line (each diameter) is an <b>axis of symmetry</b>, so a circle has infinitely many axes of symmetry.', r'Đường tròn là hình có trục đối xứng; mỗi đường thẳng đi qua tâm (mỗi đường kính) là một [[trục đối xứng]], nên đường tròn có vô số trục đối xứng.'))
theory += FIG2
theory += BOX('yellow', ('To show that points lie on one circle', 'Chứng minh nhiều điểm cùng nằm trên một đường tròn'),
  T(r'Find a point \(O\) whose distances to all the points are equal; then they lie on the circle with center \(O\). Examples: the four vertices of a rectangle (center = intersection of the diagonals); the three vertices of a right triangle (center = midpoint of the hypotenuse).', r'Tìm một điểm \(O\) cách đều tất cả các điểm đó; khi đó chúng [[cùng nằm trên một đường tròn]] tâm \(O\). Ví dụ: bốn đỉnh của hình chữ nhật (tâm là giao điểm hai đường chéo); ba đỉnh của tam giác vuông (tâm là trung điểm cạnh huyền).'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Position of points', 'Vị trí của điểm'),
  T(r'Given \((O;\,5\text{ cm})\) and points \(A\), \(B\), \(C\) with \(OA=3\) cm, \(OB=5\) cm, \(OC=7\) cm. Where does each point lie?', r'Cho \((O;\,5\text{ cm})\) và các điểm \(A\), \(B\), \(C\) với \(OA=3\) cm, \(OB=5\) cm, \(OC=7\) cm. Mỗi điểm nằm ở đâu so với đường tròn?'),
  ('Compare each distance with \\(R=5\\).', 'So sánh từng khoảng cách với \\(R=5\\).'),
  [T(r'\(OA=3\lt5\): \(A\) lies inside the circle.', r'\(OA=3\lt5\): \(A\) nằm trong đường tròn.'), T(r'\(OB=5=R\): \(B\) lies on the circle.', r'\(OB=5=R\): \(B\) nằm trên đường tròn.'),
   T(r'\(OC=7\gt5\): \(C\) lies outside the circle.', r'\(OC=7\gt5\): \(C\) nằm ngoài đường tròn.')],
  T(r'\(A\) inside, \(B\) on, \(C\) outside.', r'\(A\) nằm trong, \(B\) nằm trên, \(C\) nằm ngoài đường tròn.'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Symmetry', 'Tính đối xứng'),
  T(r'\(A\) lies on \((O;\,4\text{ cm})\). Let \(A^{\prime}\) be symmetric to \(A\) with respect to \(O\). Does \(A^{\prime}\) lie on the circle? Find \(AA^{\prime}\).', r'Điểm \(A\) nằm trên \((O;\,4\text{ cm})\). Gọi \(A^{\prime}\) là điểm đối xứng với \(A\) qua \(O\). \(A^{\prime}\) có nằm trên đường tròn không? Tính \(AA^{\prime}\).'),
  ('\\(O\\) is the midpoint of \\(AA^{\\prime}\\).', '\\(O\\) là trung điểm của \\(AA^{\\prime}\\).'),
  [T(r'\(O\) is the midpoint of \(AA^{\prime}\), so \(OA^{\prime}=OA=4\) cm: \(A^{\prime}\) lies on the circle.', r'\(O\) là trung điểm của \(AA^{\prime}\) nên \(OA^{\prime}=OA=4\) cm: \(A^{\prime}\) nằm trên đường tròn.'),
   T(r'\(AA^{\prime}\) is a diameter: \(AA^{\prime}=2\cdot4=8\) cm.', r'\(AA^{\prime}\) là một đường kính: \(AA^{\prime}=2\cdot4=8\) cm.')],
  T(r'Yes; \(AA^{\prime}=8\) cm.', r'Có; \(AA^{\prime}=8\) cm.'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('An isosceles triangle', 'Tam giác cân trong đường tròn'),
  T(r'\(A\), \(B\) lie on \((O)\) and \(\widehat{AOB}=100^\circ\). Find \(\widehat{OAB}\) and \(\widehat{OBA}\).', r'\(A\), \(B\) nằm trên \((O)\) và \(\widehat{AOB}=100^\circ\). Tính \(\widehat{OAB}\) và \(\widehat{OBA}\).'),
  ('\\(OA\\), \\(OB\\) are radii.', '\\(OA\\), \\(OB\\) là bán kính.'),
  [T(r'Since \(OA\) and \(OB\) are radii of the same circle, \(OA=OB\). Therefore, triangle \(OAB\) is isosceles at \(O\).', r'Vì \(OA\), \(OB\) là bán kính của cùng một đường tròn nên \(OA=OB\). Do đó tam giác \(OAB\) cân tại \(O\).'),
   T(r'\(\widehat{OAB}=\widehat{OBA}=\dfrac{180^\circ-100^\circ}{2}=40^\circ\).', r'\(\widehat{OAB}=\widehat{OBA}=\dfrac{180^\circ-100^\circ}{2}=40^\circ\).')],
  T(r'\(40^\circ\) and \(40^\circ\).', r'\(40^\circ\) và \(40^\circ\).'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Four points on a circle', 'Bốn điểm cùng nằm trên một đường tròn'),
  T(r'Rectangle \(ABCD\) has \(AB=6\) cm, \(BC=8\) cm. Show that \(A\), \(B\), \(C\), \(D\) lie on the same circle and find its radius.', r'Hình chữ nhật \(ABCD\) có \(AB=6\) cm, \(BC=8\) cm. Chứng minh bốn điểm \(A\), \(B\), \(C\), \(D\) cùng nằm trên một đường tròn và tính bán kính đường tròn đó.'),
  ('Let \\(O\\) be the intersection of the diagonals.', 'Gọi \\(O\\) là giao điểm hai đường chéo.'),
  [T(r'The diagonals of a rectangle are equal and bisect each other: \(OA=OB=OC=OD=\dfrac{AC}{2}\).', r'Hai đường chéo của hình chữ nhật bằng nhau và cắt nhau tại trung điểm mỗi đường: \(OA=OB=OC=OD=\dfrac{AC}{2}\).'),
   T(r'Hence the four points lie on the circle with center \(O\). \(AC=\sqrt{6^2+8^2}=10\), so \(R=5\) cm.', r'Vậy bốn điểm cùng nằm trên đường tròn tâm \(O\). \(AC=\sqrt{6^2+8^2}=10\) nên \(R=5\) cm.')],
  T(r'\(R=5\) cm.', r'\(R=5\) cm.'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Phone coverage', 'Vùng phủ sóng'),
  T(r'A phone tower covers a disk of radius 60 km. A village is 30 km east and 40 km north of the tower. Is the village covered? How much farther could it be (in the same direction) and still be covered?', r'Một trạm phát sóng điện thoại phủ sóng trong hình tròn bán kính 60 km. Một ngôi làng cách trạm 30 km về phía đông và 40 km về phía bắc. Làng có được phủ sóng không? Làng có thể ở xa thêm tối đa bao nhiêu (cùng hướng) mà vẫn được phủ sóng?'),
  ('The distance is the hypotenuse of a right triangle.', 'Khoảng cách là cạnh huyền của một tam giác vuông.'),
  [T(r'Distance \(=\sqrt{30^2+40^2}=50\) km \(\lt60\) km: the village lies inside the coverage circle.', r'Khoảng cách \(=\sqrt{30^2+40^2}=50\) km \(\lt60\) km: làng nằm trong đường tròn giới hạn vùng phủ sóng.'),
   T(r'It could be \(60-50=10\) km farther and still lie on (or inside) the circle.', r'Làng có thể xa thêm \(60-50=10\) km mà vẫn nằm trên (hoặc trong) đường tròn.')],
  T(r'Yes; up to 10 km farther.', r'Có; xa thêm tối đa 10 km.'))

_SETS = sp_g9.BANK(sp_g9.L13_GROUPS, start=1, seeds=(2301, 2302, 2303))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Radius vs diameter.</b> The diameter is \(2R\), not \(R\).', r'<b>Nhầm bán kính với đường kính.</b> Đường kính bằng \(2R\), không phải \(R\).'),
 (r'<b>Comparing with the diameter.</b> To decide the position of \(M\), compare \(OM\) with \(R\), not with \(2R\).', r'<b>So sánh với đường kính.</b> Để xét vị trí điểm \(M\) phải so sánh \(OM\) với \(R\), không phải với \(2R\).'),
 (r'<b>Only one axis of symmetry.</b> A circle has infinitely many axes of symmetry.', r'<b>Cho rằng chỉ có một trục đối xứng.</b> Đường tròn có vô số trục đối xứng.'),
 (r'<b>Not explaining \(OA=OB\).</b> Always say “since \(OA\) and \(OB\) are radii”.', r'<b>Không giải thích \(OA=OB\).</b> Luôn nêu lí do “vì \(OA\), \(OB\) là bán kính”.')]
summary = [
 (r'\((O;\,R)\) = all points at distance \(R\) from \(O\); diameter \(=2R\).', r'\((O;\,R)\) gồm các điểm cách \(O\) đúng bằng \(R\); đường kính \(=2R\).'),
 (r'\(OM\lt R\): inside; \(OM=R\): on; \(OM\gt R\): outside.', r'\(OM\lt R\): nằm trong; \(OM=R\): nằm trên; \(OM\gt R\): nằm ngoài.'),
 (r'Center of symmetry: \(O\); axes of symmetry: every line through \(O\).', r'Tâm đối xứng: \(O\); trục đối xứng: mọi đường thẳng đi qua \(O\).'),
 (r'Key English: circle, center, radius, diameter, distance, center / axis of symmetry, lie on the same circle.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[đường tròn]], [[tâm (của đường tròn)]], [[bán kính]], [[đường kính]], [[khoảng cách]], [[tâm đối xứng]], [[trục đối xứng]], [[cùng nằm trên một đường tròn]].')]
checks = [
 (r'I can state the definition of a circle.', r'Em nêu được định nghĩa đường tròn.'),
 (r'I can decide whether a point lies inside, on or outside a circle.', r'Em xác định được vị trí của điểm đối với đường tròn.'),
 (r'I know the symmetry of a circle.', r'Em biết tính đối xứng của đường tròn.'),
 (r'I can show that points lie on the same circle.', r'Em chứng minh được các điểm cùng nằm trên một đường tròn.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Introduction to Circles', title_vi='Mở đầu về đường tròn', topic=TOPIC,
       folder='circles', file='introduction-to-circles', catalog_title_vi='Mở đầu về đường tròn',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Circle, center, radius, diameter; position of a point and a circle; symmetry of a circle.', level='Basic', minutes=60,
       description_vi='Bài 13 – Đường tròn; vị trí tương đối của điểm và đường tròn; tính đối xứng của đường tròn.',
       tags_vi=['đường tròn', 'bán kính', 'đối xứng'], prerequisites=[], tags=['circle', 'radius', 'symmetry'], order=130)
