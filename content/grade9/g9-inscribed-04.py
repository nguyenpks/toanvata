# -*- coding: utf-8 -*-
"""Nội dung bài g9-inscribed-04 = Toán 9 KNTT, Bài 30: Đa giác đều – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 9 – Lesson 30. Diễn đạt phép quay theo SGK (không dùng “bậc đối xứng quay”, xem D10)."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9, sp_g9p, sp_g9q as Q

LID = 'g9-inscribed-04'
CH = 'Đường tròn ngoại tiếp và đường tròn nội tiếp'
TOPIC = ('Circumcircle and Incircle', CH)
ensure_vocab([
 ('g9-regular-polygon', 'regular polygon', 'đa giác đều (lớp 9)', CH, 'A regular hexagon has six equal sides and six equal angles.', ''),
 ('g9-rotation', 'rotation', 'phép quay (lớp 9)', CH, 'The rotation about O through 60° maps the regular hexagon onto itself.', ''),
 ('g9-center-rotation', 'center of rotation', 'tâm quay (phép quay)', CH, 'The center of rotation is the center of the polygon.', ''),
 ('g9-angle-rotation', 'angle of rotation', 'góc quay (phép quay)', CH, 'The angle of rotation is 120°.', ''),
])
load_vocab()

def FIGC(cap, px=280, **kw):
    fn = sp_g9p.cfig(**kw); return '<figure class="mbl-fig mbl-figtex">%s<figcaption>%s</figcaption></figure>' % (sp_g9p.img(fn, cap[0], px), TI(*cap))
def poly(n, dash=True, mark=True):
    L = 'ABCDEFGH'; pts = {L[i]: 90 + 360 * i / n for i in range(n)}
    return dict(pts=pts, segs=[(L[i], L[(i + 1) % n]) for i in range(n)], dash=[('O', 'A'), ('O', 'B')] if dash else [], arcs=[('A', 'O', 'B', '%d^\\circ' % (360 // n))] if mark else [])

F_TRI = FIGC(('Equilateral triangle: central angle \\(120^\\circ\\).', 'Tam giác đều: góc ở tâm \\(120^\\circ\\).'), **poly(3))
F_SQ = FIGC(('Square: central angle \\(90^\\circ\\).', 'Hình vuông: góc ở tâm \\(90^\\circ\\).'), **poly(4))
F_HEX = FIGC(('Regular hexagon: central angle \\(60^\\circ\\); \\(OAB\\) is equilateral.', 'Lục giác đều: góc ở tâm \\(60^\\circ\\); tam giác \\(OAB\\) đều.'), **poly(6))
# ---------- số liệu (kiểm tra bằng máy) ----------
for n in (3, 4, 5, 6, 8): assert 360 % n == 0
assert 180 * (8 - 2) / 8 == 135 and 360 / 8 == 45 and [60 * k for k in range(1, 7)] == [60, 120, 180, 240, 300, 360]
assert abs(6 * 4 ** 2 * math.sqrt(3) / 4 - 24 * math.sqrt(3)) < 1e-12

meta = dict(level=('Basic', 'Cơ bản'), time=('about 90 minutes', '90 phút'), before=('Lesson 28: circumcircle and incircle', 'Bài 28: đường tròn ngoại tiếp, nội tiếp'))
goals = [
 (r'recognize regular polygons and real objects shaped like them;', r'nhận biết được đa giác đều và các hình dạng đa giác đều trong thực tế;'),
 (r'understand rotations and find the rotations that map a regular polygon onto itself;', r'hiểu phép quay và xác định được các phép quay giữ nguyên đa giác đều;'),
 (r'compute the central angle \(\dfrac{360^\circ}{n}\) and the interior angle;', r'tính được góc ở tâm \(\dfrac{360^\circ}{n}\) và góc trong của đa giác đều;'),
 (r'compute sides, perimeters and areas of inscribed regular polygons (hexagon, square, triangle).', r'tính được cạnh, chu vi, diện tích của đa giác đều nội tiếp (lục giác đều, hình vuông, tam giác đều).')]
vocab = [
 (r'<b>regular polygon</b> – a convex polygon with all sides equal and all angles equal.', r'[[Đa giác đều|đa giác đều (lớp 9)]] – đa giác lồi có tất cả các cạnh bằng nhau và tất cả các góc bằng nhau.'),
 (r'<b>center of a regular polygon</b> – the common center of its circumcircle and incircle.', r'Tâm của đa giác đều – tâm chung của đường tròn ngoại tiếp và đường tròn nội tiếp đa giác.'),
 (r'<b>rotation</b> – turning every point about a fixed point \(O\) through the same angle in the same direction.', r'[[Phép quay|phép quay (lớp 9)]] – biến mỗi điểm quay quanh một điểm cố định \(O\) một góc như nhau, theo cùng một chiều.'),
 (r'<b>center / angle of rotation</b> – the fixed point \(O\) / the angle \(\alpha\).', r'[[Tâm quay|tâm quay (phép quay)]] / [[góc quay|góc quay (phép quay)]] – điểm cố định \(O\) / góc \(\alpha\).'),
 (r'<b>map … onto itself</b> – after the rotation the figure covers its old position.', r'Biến hình … thành chính nó – sau phép quay, hình trùng với vị trí cũ.')]
phrases = [
 (r'<b>\(ABCDEF\) is a regular hexagon with center \(O\).</b>', r'\(ABCDEF\) là lục giác đều tâm \(O\).'),
 (r'<b>The rotation about \(O\) through \(60^\circ\) maps \(A\) onto \(B\).</b>', r'Phép quay tâm \(O\) góc \(60^\circ\) biến \(A\) thành \(B\).'),
 (r'<b>The rotation maps the hexagon onto itself.</b>', r'Phép quay biến lục giác thành chính nó.'),
 (r'<b>Each interior angle measures \(120^\circ\).</b>', r'Mỗi góc trong có số đo \(120^\circ\).'),
 (r'<b>Find the perimeter of the inscribed regular hexagon.</b>', r'Tính chu vi lục giác đều nội tiếp.')]
review = (T(r'<b>Lesson 28.</b> An equilateral triangle has a circumcircle and an incircle with the same center.', r'<b>Bài 28.</b> Tam giác đều có đường tròn ngoại tiếp và nội tiếp cùng tâm.') +
          T(r'<b>Grade 8.</b> The interior angles of an \(n\)-gon add up to \((n-2)\cdot180^\circ\).', r'<b>Lớp 8.</b> Tổng các góc trong của đa giác \(n\) cạnh bằng \((n-2)\cdot180^\circ\).'))

theory = '<h3>5.1 %s</h3>' % TI('Regular polygons', 'Đa giác đều')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'A <b>regular polygon</b> is a convex polygon whose sides are all equal and whose angles are all equal. Examples: equilateral triangle, square, regular pentagon, regular hexagon.', r'[[Đa giác đều|đa giác đều (lớp 9)]] là đa giác lồi có tất cả các cạnh bằng nhau và tất cả các góc bằng nhau. Ví dụ: tam giác đều, hình vuông, ngũ giác đều, lục giác đều.'),
  T(r'Every regular polygon has a circumcircle and an incircle with the same center \(O\) (the <b>center</b> of the polygon).', r'Mỗi đa giác đều có một đường tròn ngoại tiếp và một đường tròn nội tiếp cùng tâm \(O\) (gọi là <b>tâm</b> của đa giác đều).'))
theory += BOX('mint', ('Angles of a regular \\(n\\)-gon', 'Các góc của đa giác đều \\(n\\) cạnh'),
  UL([T(r'Central angle (subtended by one side): \(\dfrac{360^\circ}{n}\).', r'Góc ở tâm (chắn một cạnh): \(\dfrac{360^\circ}{n}\).'),
      T(r'Interior angle: \(\dfrac{(n-2)\cdot180^\circ}{n}\). Example: regular hexagon \(\dfrac{4\cdot180^\circ}{6}=120^\circ\).', r'Góc trong: \(\dfrac{(n-2)\cdot180^\circ}{n}\). Ví dụ: lục giác đều \(\dfrac{4\cdot180^\circ}{6}=120^\circ\).')]))
theory += '<div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center">%s%s%s</div>' % (F_TRI, F_SQ, F_HEX)
theory += T(r'Real objects: honeycomb cells (hexagons), floor tiles, the pentagon on a football, the octagonal STOP sign.', r'Trong thực tế: ô tổ ong (lục giác đều), gạch lát nền, các ngũ giác trên quả bóng đá, biển báo STOP hình bát giác.')
theory += '<h3>5.2 %s</h3>' % TI('Rotations', 'Phép quay')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'The <b>rotation</b> about \(O\) through \(\alpha^\circ\) (\(0^\circ\lt\alpha^\circ\lt360^\circ\)) moves each point \(A\ne O\) to the point \(A^{\prime}) on the circle \((O;\,OA)\) such that the arc from \(A\) to \(A^{\prime}\) measures \(\alpha^\circ\) in the given direction (clockwise or counterclockwise). \(O\) stays fixed.',
    r'[[Phép quay|phép quay (lớp 9)]] [[tâm|tâm quay (phép quay)]] \(O\), [[góc|góc quay (phép quay)]] \(\alpha^\circ\) (\(0^\circ\lt\alpha^\circ\lt360^\circ\)) biến mỗi điểm \(A\ne O\) thành điểm \(A^{\prime}\) thuộc đường tròn \((O;\,OA)\) sao cho cung từ \(A\) đến \(A^{\prime}\) theo chiều quay có số đo \(\alpha^\circ\); điểm \(O\) giữ nguyên.'),
  T(r'The rotation through \(360^\circ\) keeps every point in place.', r'Phép quay \(360^\circ\) giữ nguyên mọi điểm.'))
theory += BOX('yellow', ('Rotations keeping a regular polygon', 'Phép quay giữ nguyên đa giác đều'),
  T(r'The rotations about the center \(O\) through \(\dfrac{360^\circ}{n},\ 2\cdot\dfrac{360^\circ}{n},\ \dots,\ n\cdot\dfrac{360^\circ}{n}=360^\circ\) map a regular \(n\)-gon onto itself (in either direction). Example: the equilateral triangle – \(120^\circ, 240^\circ, 360^\circ\); the square – \(90^\circ, 180^\circ, 270^\circ, 360^\circ\).',
    r'Các phép quay tâm \(O\) góc \(\dfrac{360^\circ}{n},\ 2\cdot\dfrac{360^\circ}{n},\ \dots,\ n\cdot\dfrac{360^\circ}{n}=360^\circ\) (theo chiều nào cũng được) biến đa giác đều \(n\) cạnh thành chính nó. Ví dụ: tam giác đều – \(120^\circ, 240^\circ, 360^\circ\); hình vuông – \(90^\circ, 180^\circ, 270^\circ, 360^\circ\).'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Regular or not?', 'Có phải đa giác đều?'),
  T(r'Which are regular polygons? (a) a rhombus with a \(60^\circ\) angle; (b) a square; (c) a rectangle 2 cm × 3 cm; (d) a hexagonal honeycomb cell with equal sides and \(120^\circ\) angles.', r'Hình nào là đa giác đều? a) hình thoi có một góc \(60^\circ\); b) hình vuông; c) hình chữ nhật 2 cm × 3 cm; d) ô tổ ong hình lục giác có các cạnh bằng nhau và các góc bằng \(120^\circ\).'),
  ('Both conditions: equal sides AND equal angles.', 'Cần cả hai điều kiện: các cạnh bằng nhau VÀ các góc bằng nhau.'),
  [T(r'(a) No (angles \(60^\circ\), \(120^\circ\)). (b) Yes. (c) No (sides 2 and 3). (d) Yes.', r'a) Không (các góc \(60^\circ\), \(120^\circ\)). b) Có. c) Không (các cạnh 2 và 3). d) Có.')],
  T(r'(b) and (d).', r'b) và d).'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Angles of a regular octagon', 'Các góc của bát giác đều'),
  T(r'Find the central angle and each interior angle of a regular octagon.', r'Tính góc ở tâm và mỗi góc trong của bát giác đều.'),
  ('\\(n=8\\).', '\\(n=8\\).'),
  [T(r'Central angle \(\dfrac{360^\circ}{8}=45^\circ\).', r'Góc ở tâm \(\dfrac{360^\circ}{8}=45^\circ\).'), T(r'Interior angle \(\dfrac{6\cdot180^\circ}{8}=135^\circ\).', r'Góc trong \(\dfrac{6\cdot180^\circ}{8}=135^\circ\).')],
  T(r'\(45^\circ\); \(135^\circ\).', r'\(45^\circ\); \(135^\circ\).'))
examples += EXAMPLE(3, ('Basic application', 'Vận dụng thấp'), ('Rotations of a hexagon', 'Phép quay giữ nguyên lục giác đều'),
  T(r'\(ABCDEF\) is a regular hexagon with center \(O\). (a) List the rotations about \(O\) (counterclockwise, \(0^\circ\lt\alpha\le360^\circ\)) that map it onto itself. (b) The rotation through \(120^\circ\) maps \(A\) onto which vertex?', r'\(ABCDEF\) là lục giác đều tâm \(O\). a) Liệt kê các phép quay tâm \(O\) (ngược chiều kim đồng hồ, \(0^\circ\lt\alpha\le360^\circ\)) biến lục giác thành chính nó. b) Phép quay góc \(120^\circ\) biến \(A\) thành đỉnh nào?'),
  ('Multiples of \\(60^\\circ\\); each \\(60^\\circ\\) moves a vertex to the next one.', 'Các bội của \\(60^\\circ\\); mỗi lần quay \\(60^\\circ\\) đưa một đỉnh tới đỉnh kế tiếp.'),
  [F_HEX, T(r'(a) \(60^\circ, 120^\circ, 180^\circ, 240^\circ, 300^\circ, 360^\circ\) (6 rotations). (b) \(120^\circ=2\cdot60^\circ\): \(A\to C\) (vertices named counterclockwise).', r'a) \(60^\circ, 120^\circ, 180^\circ, 240^\circ, 300^\circ, 360^\circ\) (6 phép quay). b) \(120^\circ=2\cdot60^\circ\): \(A\) biến thành \(C\) (các đỉnh đặt tên ngược chiều kim đồng hồ).')],
  T(r'(a) 6 rotations; (b) \(C\).', r'a) 6 phép quay; b) \(C\).'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Inscribed regular polygons', 'Đa giác đều nội tiếp'),
  T(r'A circle has radius 4 cm. Find the side of the inscribed regular hexagon, of the inscribed square and of the inscribed equilateral triangle.', r'Đường tròn có bán kính 4 cm. Tính cạnh của lục giác đều, hình vuông và tam giác đều nội tiếp đường tròn đó.'),
  ('Hexagon: \\(a=R\\); square: \\(a=R\\sqrt2\\); triangle: \\(a=R\\sqrt3\\).', 'Lục giác đều: \\(a=R\\); hình vuông: \\(a=R\\sqrt2\\); tam giác đều: \\(a=R\\sqrt3\\).'),
  [T(r'Hexagon: \(OAB\) is equilateral, \(a=4\) cm. Square: diagonal \(8\), \(a=4\sqrt2\) cm. Triangle: \(a=4\sqrt3\) cm.', r'Lục giác: tam giác \(OAB\) đều, \(a=4\) cm. Hình vuông: đường chéo \(8\), \(a=4\sqrt2\) cm. Tam giác đều: \(a=4\sqrt3\) cm.')],
  T(r'4 cm; \(4\sqrt2\) cm; \(4\sqrt3\) cm.', r'4 cm; \(4\sqrt2\) cm; \(4\sqrt3\) cm.'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('A hexagonal tile', 'Viên gạch lục giác'),
  T(r'A floor tile is a regular hexagon with side 4 cm. (a) Find its perimeter and area. (b) Explain why regular hexagons can cover a floor without gaps.', r'Một viên gạch lát nền là lục giác đều cạnh 4 cm. a) Tính chu vi và diện tích viên gạch. b) Giải thích vì sao các viên gạch lục giác đều lát kín được mặt sàn.'),
  ('Split the hexagon into 6 equilateral triangles.', 'Chia lục giác thành 6 tam giác đều.'),
  [T(r'(a) Perimeter \(6\cdot4=24\) cm; area \(6\cdot\dfrac{4^2\sqrt3}{4}=24\sqrt3\approx41.6\) cm².', r'a) Chu vi \(6\cdot4=24\) cm; diện tích \(6\cdot\dfrac{4^2\sqrt3}{4}=24\sqrt3\approx41{,}6\) cm².'),
   T(r'(b) Each interior angle is \(120^\circ\) and \(3\cdot120^\circ=360^\circ\): three tiles fit exactly around each vertex.', r'b) Mỗi góc trong bằng \(120^\circ\) và \(3\cdot120^\circ=360^\circ\): ba viên gạch khít nhau quanh mỗi đỉnh.')],
  T(r'(a) 24 cm; \(24\sqrt3\) cm²; (b) \(3\cdot120^\circ=360^\circ\).', r'a) 24 cm; \(24\sqrt3\) cm²; b) \(3\cdot120^\circ=360^\circ\).'))
assert abs(24 * math.sqrt(3) - 41.569) < 1e-3

_SETS = sp_g9.BANK(Q.L30_GROUPS, start=1, seeds=(3001, 3002, 3003))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Checking only the sides.</b> A rhombus has equal sides but is not regular (unless it is a square).', r'<b>Chỉ kiểm tra các cạnh.</b> Hình thoi có các cạnh bằng nhau nhưng không phải đa giác đều (trừ hình vuông).'),
 (r'<b>Confusing the central angle and the interior angle.</b> Hexagon: central angle \(60^\circ\), interior angle \(120^\circ\).', r'<b>Nhầm góc ở tâm với góc trong.</b> Lục giác đều: góc ở tâm \(60^\circ\), góc trong \(120^\circ\).'),
 (r'<b>Wrong rotation angles.</b> Only multiples of \(\dfrac{360^\circ}{n}\) keep a regular \(n\)-gon.', r'<b>Sai góc quay.</b> Chỉ các bội của \(\dfrac{360^\circ}{n}\) mới giữ nguyên đa giác đều \(n\) cạnh.'),
 (r'<b>Forgetting \(a=R\) for the hexagon.</b> In a regular hexagon each triangle \(OAB\) is equilateral.', r'<b>Quên \(a=R\) ở lục giác đều.</b> Trong lục giác đều, mỗi tam giác \(OAB\) là tam giác đều.')]
summary = [
 (r'Regular polygon: all sides equal and all angles equal; it has a center \(O\).', r'Đa giác đều: các cạnh bằng nhau, các góc bằng nhau; có tâm \(O\).'),
 (r'Central angle \(\dfrac{360^\circ}{n}\); interior angle \(\dfrac{(n-2)\cdot180^\circ}{n}\).', r'Góc ở tâm \(\dfrac{360^\circ}{n}\); góc trong \(\dfrac{(n-2)\cdot180^\circ}{n}\).'),
 (r'The rotations about \(O\) through \(k\cdot\dfrac{360^\circ}{n}\) map the polygon onto itself. Inscribed: hexagon \(a=R\), square \(a=R\sqrt2\), triangle \(a=R\sqrt3\).', r'Các phép quay tâm \(O\) góc \(k\cdot\dfrac{360^\circ}{n}\) biến đa giác thành chính nó. Nội tiếp: lục giác \(a=R\), hình vuông \(a=R\sqrt2\), tam giác đều \(a=R\sqrt3\).'),
 (r'Key English: regular polygon, rotation, center of rotation, angle of rotation.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[đa giác đều|đa giác đều (lớp 9)]], [[phép quay|phép quay (lớp 9)]], [[tâm quay|tâm quay (phép quay)]], [[góc quay|góc quay (phép quay)]].')]
checks = [
 (r'I can recognize regular polygons.', r'Em nhận biết được đa giác đều.'),
 (r'I can find the central and interior angles of a regular polygon.', r'Em tính được góc ở tâm, góc trong của đa giác đều.'),
 (r'I can list the rotations that map a regular polygon onto itself.', r'Em liệt kê được các phép quay giữ nguyên đa giác đều.'),
 (r'I can compute sides, perimeters and areas of inscribed regular polygons.', r'Em tính được cạnh, chu vi, diện tích của đa giác đều nội tiếp.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Regular Polygons', title_vi='Đa giác đều', topic=TOPIC,
       folder='circumcircle-incircle', file='regular-polygons', catalog_title_vi='Đa giác đều',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Regular polygons, central and interior angles, rotations mapping a regular polygon onto itself, inscribed hexagon, square and triangle.', level='Basic', minutes=90,
       description_vi='Bài 30 – Đa giác đều; góc ở tâm, góc trong; phép quay giữ nguyên đa giác đều; lục giác đều, hình vuông, tam giác đều nội tiếp.',
       tags_vi=['đa giác đều', 'phép quay', 'lục giác đều'], prerequisites=['g9-inscribed-03'], tags=['regular polygon', 'rotation', 'hexagon'], order=300)
