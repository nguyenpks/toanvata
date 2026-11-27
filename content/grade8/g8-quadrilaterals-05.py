# -*- coding: utf-8 -*-
"""Nội dung bài g8-quadrilaterals-05 = Toán 8 KNTT, Bài 14: Hình thoi và hình vuông – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 8 (2026), Chapter 3 – Lesson 14, tr. 49–52; Mini project "Designing a Quadrilateral Tiling for the School Courtyard" (tr. 181)."""
import os, sys
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g8b
from sp_g8b import FIGT

LID = 'g8-quadrilaterals-05'
CH = 'Tứ giác'
TOPIC = ('Quadrilaterals', CH)
ensure_vocab([
 ('g8-rhombus', 'rhombus (pl. rhombi)', 'hình thoi (lớp 8)', CH, 'A rhombus is a quadrilateral with four equal sides.', ''),
 ('g8-square-shape', 'square', 'hình vuông (lớp 8)', CH, 'A square is a quadrilateral with four right angles and four equal sides.', ''),
 ('g8-angle-bisector', 'angle bisector', 'tia phân giác (lớp 8)', CH, 'Diagonal AC is the angle bisector of angle A.', ''),
 ('g8-adjacent-sides', 'adjacent sides', 'hai cạnh kề', CH, 'A parallelogram with two equal adjacent sides is a rhombus.', ''),
])
load_vocab()

H1 = FIGT({'A': (0, 0), 'B': (2.2, -1.45), 'C': (4.4, 0), 'D': (2.2, 1.45), 'O': (2.2, 0)}, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('A', 'C'), ('B', 'D')], right=[('C', 'O', 'D')],
          cap=('Rhombus \\(ABCD\\): \\(AC\\perp BD\\); \\(AC\\) bisects \\(\\widehat{A}\\) and \\(\\widehat{C}\\).', 'Hình thoi \\(ABCD\\): \\(AC\\perp BD\\); \\(AC\\) là phân giác của \\(\\widehat{A}\\), \\(\\widehat{C}\\).'))
S1 = FIGT({'A': (0, 0), 'B': (3, 0), 'C': (3, 3), 'D': (0, 3), 'O': (1.5, 1.5)}, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('A', 'C'), ('B', 'D')], right=[('D', 'A', 'B'), ('B', 'O', 'C')], px=220,
          cap=('Square \\(ABCD\\): equal, perpendicular diagonals.', 'Hình vuông \\(ABCD\\): hai đường chéo bằng nhau và vuông góc.'))

# ---------- kiểm tra số liệu ----------
x = 7; assert 3 * x + 5 == 5 * x - 9 == 26 and 4 * 26 == 104 and 68 // 2 == 34 and 180 - 68 == 112      # Ví dụ 2
assert F('4.5') * 2 == 9                                                                                     # Ví dụ 3
assert 30 * 40 // 2 == 600 and 50 * 600 == 30000                                                             # Ví dụ 5

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 60 minutes', '60 phút'),
            before=('parallelograms, rectangles (Lessons 12–13)', 'hình bình hành, hình chữ nhật (Bài 12, 13)'))
goals = [
 (r'recognize a rhombus and a square;', r'nhận biết được [[hình thoi|hình thoi (lớp 8)]] và [[hình vuông|hình vuông (lớp 8)]];'),
 (r'use their properties: perpendicular diagonals that bisect the angles (rhombus); equal and perpendicular diagonals (square);', r'sử dụng được tính chất: hai đường chéo vuông góc và là [[tia phân giác|tia phân giác (lớp 8)]] của các góc (hình thoi); hai đường chéo bằng nhau và vuông góc (hình vuông);'),
 (r'use the tests for a rhombus and a square.', r'dùng được các dấu hiệu nhận biết hình thoi, hình vuông.')]
vocab = [
 (r'<b>rhombus</b> (plural <b>rhombi</b>) – a quadrilateral with four equal sides.', r'[[Hình thoi|hình thoi (lớp 8)]] – tứ giác có bốn cạnh bằng nhau.'),
 (r'<b>square</b> – a quadrilateral with four right angles and four equal sides.', r'[[Hình vuông|hình vuông (lớp 8)]] – tứ giác có bốn góc vuông và bốn cạnh bằng nhau.'),
 (r'<b>adjacent sides</b> – two sides with a common vertex.', r'[[Hai cạnh kề]] – hai cạnh có chung một đỉnh.'),
 (r'<b>angle bisector</b> – a ray dividing an angle into two equal angles.', r'[[Tia phân giác|tia phân giác (lớp 8)]] – tia chia một góc thành hai góc bằng nhau.'),
 (r'<b>perpendicular</b> – meeting at a right angle: \(AC\perp BD\).', r'[[Vuông góc]] – cắt nhau tạo thành góc vuông: \(AC\perp BD\).')]
phrases = [
 (r'<b>Use the figure to identify the perpendicular diagonals of rhombus \(ABCD\).</b>', r'Dựa vào hình, chỉ ra hai đường chéo vuông góc của hình thoi \(ABCD\).'),
 (r'<b>Since \(ABCD\) is a rhombus, \(AC\perp BD\). Diagonal \(AC\) bisects \(\widehat{DAB}\).</b>', r'Vì \(ABCD\) là hình thoi nên \(AC\perp BD\); đường chéo \(AC\) là phân giác của \(\widehat{DAB}\).'),
 (r'<b>Because \(AB=BC\) and \(ABCD\) is a parallelogram, it is also a rhombus.</b>', r'Vì \(AB=BC\) và \(ABCD\) là hình bình hành nên nó là hình thoi.'),
 (r'<b>A rectangle with two congruent adjacent sides is a square.</b>', r'Hình chữ nhật có hai cạnh kề bằng nhau là hình vuông.'),
 (r'<b>Since \(KLMN\) is both a rectangle and a rhombus, it is a square.</b>', r'Vì \(KLMN\) vừa là hình chữ nhật vừa là hình thoi nên nó là hình vuông.')]
review = (T(r'<b>Parallelogram, rectangle (Lessons 12–13).</b> Diagonals bisect each other; a rectangle has equal diagonals.', r'<b>Hình bình hành, hình chữ nhật (Bài 12, 13).</b> Hai đường chéo cắt nhau tại trung điểm mỗi đường; hình chữ nhật có hai đường chéo bằng nhau.') +
          T(r'<b>Area of a rhombus (grade 6).</b> \(S=\dfrac{d_1d_2}{2}\).', r'<b>Diện tích hình thoi (lớp 6).</b> \(S=\dfrac{d_1d_2}{2}\).'))

theory = '<h3>14.1 %s</h3>' % TI('Rhombi', 'Hình thoi')
theory += BOX('blue', ('Definition and properties', 'Định nghĩa và tính chất'),
  T(r'A <b>rhombus</b> is a quadrilateral with four equal sides. It is a parallelogram, so it has all the properties of a parallelogram.', r'[[Hình thoi|hình thoi (lớp 8)]] là tứ giác có bốn cạnh bằng nhau. Hình thoi là một hình bình hành nên có mọi tính chất của hình bình hành.'),
  T(r'In addition: the diagonals are perpendicular, and each diagonal bisects two angles of the rhombus.', r'Ngoài ra: hai đường chéo vuông góc với nhau; mỗi đường chéo là đường phân giác của hai góc của hình thoi.'),
  H1)
theory += BOX('mint', ('Tests for a rhombus', 'Dấu hiệu nhận biết hình thoi'),
  T(r'1) a quadrilateral with four equal sides; 2) a parallelogram with two equal adjacent sides; 3) a parallelogram with perpendicular diagonals; 4) a parallelogram in which a diagonal bisects an angle.', r'1) tứ giác có bốn cạnh bằng nhau; 2) hình bình hành có hai cạnh kề bằng nhau; 3) hình bình hành có hai đường chéo vuông góc; 4) hình bình hành có một đường chéo là đường phân giác của một góc.'))
theory += '<h3>14.2 %s</h3>' % TI('Squares', 'Hình vuông')
theory += BOX('blue', ('Definition and properties', 'Định nghĩa và tính chất'),
  T(r'A <b>square</b> is a quadrilateral with four right angles and four equal sides. A square is both a rectangle and a rhombus: its diagonals are equal, perpendicular, bisect each other and bisect the angles.', r'[[Hình vuông|hình vuông (lớp 8)]] là tứ giác có bốn góc vuông và bốn cạnh bằng nhau. Hình vuông vừa là hình chữ nhật vừa là hình thoi: hai đường chéo bằng nhau, vuông góc, cắt nhau tại trung điểm mỗi đường và là phân giác các góc.'),
  S1)
theory += BOX('mint', ('Tests for a square', 'Dấu hiệu nhận biết hình vuông'),
  T(r'1) a rectangle with two equal adjacent sides; 2) a rectangle with perpendicular diagonals; 3) a rhombus with a right angle; 4) a rhombus with equal diagonals.', r'1) hình chữ nhật có hai cạnh kề bằng nhau; 2) hình chữ nhật có hai đường chéo vuông góc; 3) hình thoi có một góc vuông; 4) hình thoi có hai đường chéo bằng nhau.'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'),
  T(r'A quadrilateral with perpendicular diagonals is not always a rhombus: it must first be a parallelogram.', r'Tứ giác có hai đường chéo vuông góc chưa chắc là hình thoi: trước hết nó phải là hình bình hành.'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Sides of a rhombus', 'Cạnh của hình thoi'),
  T(r'Rhombus \(ABCD\) has \(AB=5\) cm. Find its perimeter and the angle between its diagonals.', r'Hình thoi \(ABCD\) có \(AB=5\) cm. Tính chu vi và góc giữa hai đường chéo.'),
  ('Four equal sides; perpendicular diagonals.', 'Bốn cạnh bằng nhau; hai đường chéo vuông góc.'),
  [T(r'Perimeter \(4\cdot5=20\) cm; the diagonals meet at \(90^\circ\).', r'Chu vi \(4\cdot5=20\) cm; hai đường chéo vuông góc (\(90^\circ\)).')],
  T(r'20 cm; \(90^\circ\).', r'20 cm; \(90^\circ\).'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Rhombus with x', 'Hình thoi có ẩn x'),
  T(r'Rhombus \(WXYZ\) has \(WX=3x+5\), \(XY=5x-9\) (cm) and \(\widehat{XWZ}=68^\circ\). Find \(x\), the side, \(\widehat{XWY}\) and \(\widehat{WZY}\).', r'Hình thoi \(WXYZ\) có \(WX=3x+5\), \(XY=5x-9\) (cm) và \(\widehat{XWZ}=68^\circ\). Tìm \(x\), độ dài cạnh, \(\widehat{XWY}\) và \(\widehat{WZY}\).'),
  ('Equal sides; the diagonal bisects the angle; consecutive angles are supplementary.', 'Các cạnh bằng nhau; đường chéo là phân giác; hai góc kề một cạnh bù nhau.'),
  [T(r'\(3x+5=5x-9\Rightarrow x=7\); side \(26\) cm.', r'\(3x+5=5x-9\Rightarrow x=7\); cạnh dài \(26\) cm.'),
   T(r'\(\widehat{XWY}=68^\circ:2=34^\circ\); \(\widehat{WZY}=180^\circ-68^\circ=112^\circ\).', r'\(\widehat{XWY}=68^\circ:2=34^\circ\); \(\widehat{WZY}=180^\circ-68^\circ=112^\circ\).')],
  T(r'\(x=7\); 26 cm; \(34^\circ\); \(112^\circ\).', r'\(x=7\); 26 cm; \(34^\circ\); \(112^\circ\).'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('Diagonals of a square', 'Đường chéo hình vuông'),
  T(r'In square \(JKLM\), the diagonals meet at \(P\) and \(JP=4.5\) cm. Find \(KP\), \(LP\), \(MP\), \(JL\), \(KM\) and \(\widehat{KJL}\).', r'Hình vuông \(JKLM\) có hai đường chéo cắt nhau tại \(P\), \(JP=4{,}5\) cm. Tính \(KP\), \(LP\), \(MP\), \(JL\), \(KM\) và \(\widehat{KJL}\).'),
  ('Equal diagonals bisecting each other and the angles.', 'Hai đường chéo bằng nhau, cắt nhau tại trung điểm, là phân giác các góc.'),
  [T(r'\(KP=LP=MP=4.5\) cm; \(JL=KM=9\) cm.', r'\(KP=LP=MP=4{,}5\) cm; \(JL=KM=9\) cm.'),
   T(r'\(\widehat{KJL}=90^\circ:2=45^\circ\).', r'\(\widehat{KJL}=90^\circ:2=45^\circ\).')],
  T(r'\(4.5\) cm; \(9\) cm; \(45^\circ\).', r'\(4{,}5\) cm; \(9\) cm; \(45^\circ\).'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Proving a square', 'Chứng minh hình vuông'),
  T(r'The diagonals \(PR\), \(QS\) of quadrilateral \(PQRS\) meet at \(T\) with \(PT=TR\), \(QT=TS\), \(PR=QS\) and \(PR\perp QS\). Prove that \(PQRS\) is a square.', r'Hai đường chéo \(PR\), \(QS\) của tứ giác \(PQRS\) cắt nhau tại \(T\), \(PT=TR\), \(QT=TS\), \(PR=QS\) và \(PR\perp QS\). Chứng minh \(PQRS\) là hình vuông.'),
  ('Go step by step: parallelogram → rectangle → square.', 'Lần lượt: hình bình hành → hình chữ nhật → hình vuông.'),
  [T(r'Diagonals bisect each other ⇒ parallelogram; equal diagonals ⇒ rectangle.', r'Hai đường chéo cắt nhau tại trung điểm ⇒ hình bình hành; hai đường chéo bằng nhau ⇒ hình chữ nhật.'),
   T(r'A rectangle with perpendicular diagonals ⇒ square.', r'Hình chữ nhật có hai đường chéo vuông góc ⇒ hình vuông.')],
  T(r'\(PQRS\) is a square.', r'\(PQRS\) là hình vuông.'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Tiling the courtyard', 'Lát gạch sân trường'),
  T(r'The class designs a tiling for the school courtyard with rhombus tiles whose diagonals are 30 cm and 40 cm. What area do 50 tiles cover?', r'Lớp thiết kế mẫu lát sân trường bằng gạch hình thoi có hai đường chéo 30 cm và 40 cm. 50 viên gạch lát được diện tích bao nhiêu?'),
  ('Area of a rhombus \\(=\\dfrac{d_1d_2}{2}\\).', 'Diện tích hình thoi \\(=\\dfrac{d_1d_2}{2}\\).'),
  [T(r'One tile: \(\dfrac{30\cdot40}{2}=600\) cm².', r'Một viên: \(\dfrac{30\cdot40}{2}=600\) cm².'),
   T(r'50 tiles: \(50\cdot600=30000\) cm² \(=3\) m².', r'50 viên: \(50\cdot600=30000\) cm² \(=3\) m².')],
  T(r'\(30000\) cm² (3 m²).', r'\(30000\) cm² (3 m²).'))

_SETS = sp_g8b.BANK(sp_g8b.L14_GROUPS, start=1, seeds=(8141, 8142, 8143))
practice = LEVEL_PRACTICE(sp_g8b.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Equal diagonals in a rhombus.</b> In general they are not equal (only in a square).', r'<b>Cho rằng hình thoi có hai đường chéo bằng nhau.</b> Nói chung không (chỉ hình vuông mới có).'),
 (r'<b>Perpendicular diagonals ⇒ rhombus.</b> Only for a parallelogram.', r'<b>Hai đường chéo vuông góc ⇒ hình thoi.</b> Chỉ đúng với hình bình hành.'),
 (r'<b>Every rectangle is a square.</b> No: every square is a rectangle, not conversely.', r'<b>Mọi hình chữ nhật là hình vuông.</b> Sai: mọi hình vuông là hình chữ nhật, không có chiều ngược lại.'),
 (r'<b>Forgetting to halve the angle.</b> The diagonal of a rhombus makes half of the vertex angle with a side.', r'<b>Quên chia đôi góc.</b> Đường chéo hình thoi tạo với cạnh một góc bằng nửa góc ở đỉnh.')]
summary = [
 (r'Rhombus: four equal sides; diagonals perpendicular and bisect the angles.', r'Hình thoi: bốn cạnh bằng nhau; hai đường chéo vuông góc và là phân giác các góc.'),
 (r'Square: rectangle + rhombus; diagonals equal, perpendicular, bisecting each other.', r'Hình vuông: vừa là hình chữ nhật vừa là hình thoi; hai đường chéo bằng nhau, vuông góc, cắt nhau tại trung điểm mỗi đường.'),
 (r'Use the tests in the right order: parallelogram → rectangle / rhombus → square.', r'Dùng dấu hiệu theo thứ tự: hình bình hành → hình chữ nhật / hình thoi → hình vuông.'),
 (r'Key English: rhombus, square, adjacent sides, angle bisector, perpendicular.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[hình thoi|hình thoi (lớp 8)]], [[hình vuông|hình vuông (lớp 8)]], [[hai cạnh kề]], [[tia phân giác|tia phân giác (lớp 8)]], [[vuông góc]].')]
checks = [
 (r'I can use the properties of rhombi and squares.', r'Em dùng được tính chất của hình thoi, hình vuông.'),
 (r'I can prove that a quadrilateral is a rhombus or a square.', r'Em chứng minh được tứ giác là hình thoi, hình vuông.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Rhombi and Squares', title_vi='Hình thoi và hình vuông', topic=TOPIC,
       folder='quadrilaterals', file='rhombi-squares', catalog_title_vi='Hình thoi và hình vuông',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Rhombi and squares: properties and tests.', level='Intermediate', minutes=60,
       description_vi='Bài 14 – Hình thoi, hình vuông: định nghĩa, tính chất, dấu hiệu nhận biết.',
       tags_vi=['hình thoi', 'hình vuông', 'dấu hiệu nhận biết'],
       prerequisites=['g8-quadrilaterals-04'], tags=['rhombus', 'square', 'angle bisector'], order=140)
