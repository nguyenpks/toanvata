# -*- coding: utf-8 -*-
"""Nội dung bài g8-quadrilaterals-04 = Toán 8 KNTT, Bài 13: Hình chữ nhật – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 8 (2026), Chapter 3 – Lesson 13, tr. 46–48; Part 3 – Recognizing Rectangles Using Diagonals (tr. 165)."""
import os, sys
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g8b
from sp_g8b import FIGT

LID = 'g8-quadrilaterals-04'
CH = 'Tứ giác'
TOPIC = ('Quadrilaterals', CH)
ensure_vocab([
 ('g8-rectangle', 'rectangle', 'hình chữ nhật (lớp 8)', CH, 'A rectangle is a quadrilateral with four right angles.', ''),
 ('g8-right-angle', 'right angle', 'góc vuông (lớp 8)', CH, 'Each angle of a rectangle is a right angle.', ''),
 ('g8-median', 'median', 'đường trung tuyến (lớp 8)', CH, 'In a right triangle, the median to the hypotenuse is half the hypotenuse.', ''),
])
load_vocab()

R1 = FIGT({'A': (0, 0), 'B': (4.2, 0), 'C': (4.2, 2.4), 'D': (0, 2.4), 'O': (2.1, 1.2)}, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('A', 'C'), ('B', 'D')], right=[('D', 'A', 'B')],
          cap=('Rectangle \\(ABCD\\): \\(AC=BD\\), \\(OA=OB=OC=OD\\).', 'Hình chữ nhật \\(ABCD\\): \\(AC=BD\\), \\(OA=OB=OC=OD\\).'))
R2 = FIGT({'A': (0, 0), 'B': (4.0, 0), 'C': (0, 2.6), 'M': (2.0, 1.3)}, segs=[('A', 'B'), ('B', 'C'), ('C', 'A')], dash=[('A', 'M')], right=[('B', 'A', 'C')], px=230,
          cap=('Right triangle \\(ABC\\), \\(M\\) the midpoint of \\(BC\\): \\(AM=\\dfrac{BC}{2}\\).', 'Tam giác \\(ABC\\) vuông tại \\(A\\), \\(M\\) là trung điểm \\(BC\\): \\(AM=\\dfrac{BC}{2}\\).'))

# ---------- kiểm tra số liệu ----------
assert 10 // 2 == 5                                                   # Ví dụ 1
assert F(13, 2) == F('6.5')                                           # Ví dụ 3
x = 3; assert 2 * x + 1 == x + 4 == 7 and 2 * 7 == 14                 # Ví dụ 4

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 45 minutes', '45 phút'),
            before=('parallelograms (Lesson 12)', 'hình bình hành (Bài 12)'))
goals = [
 (r'recognize a rectangle and use its properties (equal diagonals that bisect each other);', r'nhận biết được [[hình chữ nhật|hình chữ nhật (lớp 8)]] và sử dụng tính chất: hai đường chéo bằng nhau và cắt nhau tại trung điểm mỗi đường;'),
 (r'use the tests for a rectangle;', r'dùng được các dấu hiệu nhận biết hình chữ nhật;'),
 (r'use the fact that the median to the hypotenuse of a right triangle is half the hypotenuse.', r'vận dụng được tính chất [[đường trung tuyến|đường trung tuyến (lớp 8)]] ứng với cạnh huyền của tam giác vuông bằng nửa cạnh huyền.')]
vocab = [
 (r'<b>rectangle</b> – a quadrilateral with four right angles.', r'[[Hình chữ nhật|hình chữ nhật (lớp 8)]] – tứ giác có bốn [[góc vuông|góc vuông (lớp 8)]].'),
 (r'<b>congruent diagonals</b> – diagonals of equal length.', r'Hai [[đường chéo]] bằng nhau.'),
 (r'<b>median / hypotenuse</b> – the segment from a vertex to the midpoint of the opposite side / the side opposite the right angle.', r'[[Đường trung tuyến|đường trung tuyến (lớp 8)]] / [[cạnh huyền]] – đoạn nối một đỉnh với trung điểm cạnh đối diện / cạnh đối diện với góc vuông.')]
phrases = [
 (r'<b>Use the diagram to identify the four right angles of rectangle \(ABCD\).</b>', r'Dựa vào hình, chỉ ra bốn góc vuông của hình chữ nhật \(ABCD\).'),
 (r'<b>Determine whether parallelogram \(EFGH\) is a rectangle.</b>', r'Xác định hình bình hành \(EFGH\) có phải hình chữ nhật không.'),
 (r'<b>A parallelogram with one right angle is a rectangle. A parallelogram with congruent diagonals is a rectangle.</b>', r'Hình bình hành có một góc vuông là hình chữ nhật. Hình bình hành có hai đường chéo bằng nhau là hình chữ nhật.'),
 (r'<b>Since \(M\) is the midpoint of hypotenuse \(BC\) in right triangle \(ABC\), \(M\) is equidistant from \(A\), \(B\) and \(C\).</b>', r'Vì \(M\) là trung điểm cạnh huyền \(BC\) của tam giác vuông \(ABC\) nên \(M\) cách đều \(A\), \(B\), \(C\).')]
review = (T(r'<b>Parallelogram (Lesson 12).</b> Its diagonals bisect each other; consecutive angles are supplementary.', r'<b>Hình bình hành (Bài 12).</b> Hai đường chéo cắt nhau tại trung điểm mỗi đường; hai góc kề một cạnh bù nhau.'))

theory = '<h3>13.1 %s</h3>' % TI('Definition and properties', 'Định nghĩa và tính chất')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'A <b>rectangle</b> is a quadrilateral with four right angles. A rectangle is both a parallelogram and an isosceles trapezoid.', r'[[Hình chữ nhật|hình chữ nhật (lớp 8)]] là tứ giác có bốn góc vuông. Hình chữ nhật vừa là hình bình hành, vừa là hình thang cân.'),
  T(r'Property: the diagonals of a rectangle are <b>equal</b> and bisect each other: \(AC=BD\), \(OA=OB=OC=OD\).', r'Tính chất: hai đường chéo của hình chữ nhật <b>bằng nhau</b> và cắt nhau tại trung điểm của mỗi đường: \(AC=BD\), \(OA=OB=OC=OD\).'),
  R1)
theory += '<h3>13.2 %s</h3>' % TI('Tests for a rectangle', 'Dấu hiệu nhận biết hình chữ nhật')
theory += BOX('mint', ('A quadrilateral is a rectangle if…', 'Tứ giác là hình chữ nhật nếu…'),
  T(r'1) it has three right angles; 2) it is an isosceles trapezoid with a right angle; 3) it is a parallelogram with a right angle; 4) it is a parallelogram with equal diagonals.', r'1) có ba góc vuông; 2) là hình thang cân có một góc vuông; 3) là hình bình hành có một góc vuông; 4) là hình bình hành có hai đường chéo bằng nhau.'))
theory += '<h3>13.3 %s</h3>' % TI('Application to right triangles', 'Áp dụng vào tam giác vuông')
theory += BOX('blue', ('Median to the hypotenuse', 'Đường trung tuyến ứng với cạnh huyền'),
  T(r'In a right triangle, the median to the hypotenuse is half the hypotenuse. Conversely, if the median from \(A\) is half of \(BC\), then triangle \(ABC\) is right-angled at \(A\).', r'Trong tam giác vuông, đường trung tuyến ứng với cạnh huyền bằng nửa cạnh huyền. Ngược lại, nếu đường trung tuyến kẻ từ \(A\) bằng nửa cạnh \(BC\) thì tam giác \(ABC\) vuông tại \(A\).'),
  R2)
theory += BOX('yellow', ('Watch out!', 'Lưu ý'),
  T(r'A quadrilateral with equal diagonals is not always a rectangle: it must first be a parallelogram (diagonals bisect each other).', r'Tứ giác có hai đường chéo bằng nhau chưa chắc là hình chữ nhật: trước hết nó phải là hình bình hành (hai đường chéo cắt nhau tại trung điểm mỗi đường).'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Diagonals of a rectangle', 'Đường chéo hình chữ nhật'),
  T(r'Rectangle \(ABCD\) has diagonals meeting at \(O\) and \(AC=10\) cm. Find \(BD\), \(OA\), \(OB\).', r'Hình chữ nhật \(ABCD\) có hai đường chéo cắt nhau tại \(O\), \(AC=10\) cm. Tính \(BD\), \(OA\), \(OB\).'),
  ('Equal diagonals that bisect each other.', 'Hai đường chéo bằng nhau và cắt nhau tại trung điểm mỗi đường.'),
  [T(r'\(BD=AC=10\) cm; \(OA=OB=10:2=5\) cm.', r'\(BD=AC=10\) cm; \(OA=OB=10:2=5\) cm.')],
  T(r'\(BD=10\) cm, \(OA=OB=5\) cm.', r'\(BD=10\) cm, \(OA=OB=5\) cm.'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Which is a rectangle?', 'Hình nào là hình chữ nhật?'),
  T(r'a) Parallelogram \(EFGH\) has \(\widehat{E}=90^\circ\). b) Quadrilateral \(KLMN\) has \(\widehat{K}=\widehat{L}=\widehat{M}=90^\circ\). c) Quadrilateral \(PQRS\) has \(PR=QS\). Which are surely rectangles?', r'a) Hình bình hành \(EFGH\) có \(\widehat{E}=90^\circ\). b) Tứ giác \(KLMN\) có \(\widehat{K}=\widehat{L}=\widehat{M}=90^\circ\). c) Tứ giác \(PQRS\) có \(PR=QS\). Hình nào chắc chắn là hình chữ nhật?'),
  ('Compare with the tests.', 'Đối chiếu với các dấu hiệu.'),
  [T(r'a) Yes (parallelogram with a right angle). b) Yes (three right angles).', r'a) Đúng (hình bình hành có một góc vuông). b) Đúng (tứ giác có ba góc vuông).'),
   T(r'c) Not necessarily: an isosceles trapezoid also has equal diagonals.', r'c) Chưa chắc: hình thang cân cũng có hai đường chéo bằng nhau.')],
  T(r'a) and b).', r'a) và b).'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('Median to the hypotenuse', 'Trung tuyến ứng với cạnh huyền'),
  T(r'Triangle \(ABC\) is right-angled at \(A\), \(BC=13\) cm, \(M\) is the midpoint of \(BC\). Find \(AM\).', r'Tam giác \(ABC\) vuông tại \(A\), \(BC=13\) cm, \(M\) là trung điểm của \(BC\). Tính \(AM\).'),
  ('Draw the rectangle \\(ABDC\\) with \\(M\\) the meeting point of the diagonals.', 'Vẽ hình chữ nhật \\(ABDC\\) có \\(M\\) là giao điểm hai đường chéo.'),
  [T(r'\(AM=\dfrac{BC}{2}=6.5\) cm.', r'\(AM=\dfrac{BC}{2}=6{,}5\) cm.')],
  T(r'\(AM=6.5\) cm.', r'\(AM=6{,}5\) cm.'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Diagonals with x', 'Đường chéo có ẩn x'),
  T(r'The diagonals of quadrilateral \(PQRS\) meet at \(T\); \(PT=TR=2x+1\), \(QT=TS=x+4\) (cm). Find \(x\) so that \(PQRS\) is a rectangle; then find its diagonals.', r'Hai đường chéo của tứ giác \(PQRS\) cắt nhau tại \(T\); \(PT=TR=2x+1\), \(QT=TS=x+4\) (cm). Tìm \(x\) để \(PQRS\) là hình chữ nhật; tính độ dài hai đường chéo.'),
  ('Diagonals bisect each other → parallelogram; equal diagonals → rectangle.', 'Hai đường chéo cắt nhau tại trung điểm → hình bình hành; hai đường chéo bằng nhau → hình chữ nhật.'),
  [T(r'Need \(PR=QS\), i.e. \(2x+1=x+4\Rightarrow x=3\).', r'Cần \(PR=QS\), tức là \(2x+1=x+4\Rightarrow x=3\).'),
   T(r'Then \(PR=QS=2\cdot7=14\) cm.', r'Khi đó \(PR=QS=2\cdot7=14\) cm.')],
  T(r'\(x=3\); diagonals 14 cm.', r'\(x=3\); hai đường chéo dài 14 cm.'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Checking a door frame', 'Kiểm tra khung cửa'),
  T(r'A carpenter makes a door frame with opposite sides \(2\) m and \(0.9\) m. How can he check that the corners are right angles using only a tape measure?', r'Người thợ làm khung cửa có các cạnh đối dài \(2\) m và \(0{,}9\) m. Chỉ dùng thước dây, làm sao kiểm tra các góc của khung đều vuông?'),
  ('Opposite sides equal → parallelogram.', 'Các cạnh đối bằng nhau → hình bình hành.'),
  [T(r'With equal opposite sides, the frame is a parallelogram.', r'Các cạnh đối bằng nhau nên khung là hình bình hành.'),
   T(r'Measure the two diagonals: if they are equal, the parallelogram is a rectangle, so all corners are right angles.', r'Đo hai đường chéo: nếu bằng nhau thì hình bình hành đó là hình chữ nhật, mọi góc đều vuông.')],
  T(r'Check that the two diagonals are equal.', r'Kiểm tra hai đường chéo có bằng nhau không.'))

_SETS = sp_g8b.BANK(sp_g8b.L13_GROUPS, start=1, seeds=(8131, 8132, 8133))
practice = LEVEL_PRACTICE(sp_g8b.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Equal diagonals ⇒ rectangle.</b> Only for a parallelogram.', r'<b>Hai đường chéo bằng nhau ⇒ hình chữ nhật.</b> Chỉ đúng với hình bình hành.'),
 (r'<b>Two right angles are enough.</b> No: a right trapezoid has two right angles.', r'<b>Hai góc vuông là đủ.</b> Sai: hình thang vuông có hai góc vuông.'),
 (r'<b>Median = hypotenuse.</b> The median to the hypotenuse is half of it.', r'<b>Trung tuyến bằng cạnh huyền.</b> Trung tuyến ứng với cạnh huyền chỉ bằng nửa cạnh huyền.'),
 (r'<b>Perpendicular diagonals.</b> A rectangle does not have perpendicular diagonals in general (that is a rhombus).', r'<b>Hai đường chéo vuông góc.</b> Hình chữ nhật nói chung không có tính chất này (đó là tính chất của hình thoi).')]
summary = [
 (r'Rectangle: four right angles; diagonals are equal and bisect each other.', r'Hình chữ nhật: bốn góc vuông; hai đường chéo bằng nhau và cắt nhau tại trung điểm mỗi đường.'),
 (r'Tests: three right angles; parallelogram with a right angle or equal diagonals; isosceles trapezoid with a right angle.', r'Dấu hiệu: ba góc vuông; hình bình hành có một góc vuông hoặc hai đường chéo bằng nhau; hình thang cân có một góc vuông.'),
 (r'Right triangle: median to the hypotenuse \(=\) half the hypotenuse.', r'Tam giác vuông: trung tuyến ứng với cạnh huyền bằng nửa cạnh huyền.'),
 (r'Key English: rectangle, right angle, median, hypotenuse.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[hình chữ nhật|hình chữ nhật (lớp 8)]], [[góc vuông|góc vuông (lớp 8)]], [[đường trung tuyến|đường trung tuyến (lớp 8)]], [[cạnh huyền]].')]
checks = [
 (r'I can use the properties of a rectangle.', r'Em dùng được tính chất của hình chữ nhật.'),
 (r'I can prove that a quadrilateral is a rectangle.', r'Em chứng minh được tứ giác là hình chữ nhật.'),
 (r'I can use the median to the hypotenuse.', r'Em vận dụng được tính chất trung tuyến ứng với cạnh huyền.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Rectangles', title_vi='Hình chữ nhật', topic=TOPIC,
       folder='quadrilaterals', file='rectangles', catalog_title_vi='Hình chữ nhật',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Rectangles: properties, tests, median to the hypotenuse.', level='Intermediate', minutes=45,
       description_vi='Bài 13 – Hình chữ nhật: định nghĩa, tính chất, dấu hiệu nhận biết; đường trung tuyến ứng với cạnh huyền.',
       tags_vi=['hình chữ nhật', 'dấu hiệu nhận biết', 'trung tuyến'],
       prerequisites=['g8-quadrilaterals-03'], tags=['rectangle', 'median', 'hypotenuse'], order=130)
