# -*- coding: utf-8 -*-
"""Nội dung bài g8-quadrilaterals-02 = Toán 8 KNTT, Bài 11: Hình thang cân – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 8 (2026), Chapter 3 – Lesson 11, tr. 40–42 (trapezoid, isosceles trapezoid, base, leg, height, base angle)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g8b
from sp_g8b import FIGT

LID = 'g8-quadrilaterals-02'
CH = 'Tứ giác'
TOPIC = ('Quadrilaterals', CH)
ensure_vocab([
 ('g8-iso-trap', 'isosceles trapezoid', 'hình thang cân (lớp 8)', CH, 'An isosceles trapezoid is a trapezoid with two equal angles adjacent to one base.', ''),
 ('g8-base', 'base (of a trapezoid)', 'đáy (lớp 8)', CH, 'AB and CD are the bases of trapezoid ABCD.', ''),
 ('g8-leg', 'leg (of a trapezoid)', 'cạnh bên (hình thang)', CH, 'AD and BC are the legs of trapezoid ABCD.', ''),
 ('g8-height', 'height', 'đường cao (lớp 8)', CH, 'AH is a height of trapezoid ABCD.', ''),
 ('g8-base-angle', 'base angle', 'góc kề một đáy', CH, 'An isosceles trapezoid has equal base angles.', ''),
 ('g8-right-trap', 'right trapezoid', 'hình thang vuông', CH, 'A right trapezoid has a right angle.', ''),
])
load_vocab()

T1 = FIGT({'D': (0, 0), 'C': (4.8, 0), 'B': (3.6, 2.2), 'A': (1.1, 2.2), 'H': (1.1, 0)}, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')], dash=[('A', 'H')], right=[('A', 'H', 'C')],
          cap=('Trapezoid \\(ABCD\\) (\\(AB\\parallel CD\\)), height \\(AH\\).', 'Hình thang \\(ABCD\\) (\\(AB\\parallel CD\\)), đường cao \\(AH\\).'))
T2 = FIGT({'D': (0, 0), 'C': (4.6, 0), 'B': (3.5, 2.1), 'A': (1.1, 2.1)}, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('A', 'C'), ('B', 'D')],
          cap=('Isosceles trapezoid \\(ABCD\\): \\(AD=BC\\), \\(AC=BD\\).', 'Hình thang cân \\(ABCD\\): \\(AD=BC\\), \\(AC=BD\\).'))

# ---------- kiểm tra số liệu ----------
assert 180 - 110 == 70 and 180 - 60 == 120                    # Ví dụ 2
assert 180 - 68 == 112                                         # Ví dụ 3
assert 180 - 70 == 110                                         # Ví dụ 4
assert 6 + 11 + 2 * 5 == 27                                    # Ví dụ 5

meta = dict(level=('Beginner', 'Cơ bản'), time=('about 45 minutes', '45 phút'),
            before=('quadrilaterals (Lesson 10); parallel lines (grade 7)', 'tứ giác (Bài 10); hai đường thẳng song song (lớp 7)'))
goals = [
 (r'recognize a trapezoid, its bases, legs and height; recognize an isosceles trapezoid;', r'nhận biết được [[hình thang]], [[đáy|đáy (lớp 8)]], [[cạnh bên|cạnh bên (hình thang)]], [[đường cao|đường cao (lớp 8)]]; nhận biết [[hình thang cân|hình thang cân (lớp 8)]];'),
 (r'use the properties of an isosceles trapezoid (equal legs, equal diagonals, equal base angles);', r'sử dụng được tính chất của hình thang cân (hai cạnh bên bằng nhau, hai đường chéo bằng nhau, hai [[góc kề một đáy]] bằng nhau);'),
 (r'use the tests to show that a trapezoid is isosceles.', r'dùng được dấu hiệu để chứng minh một hình thang là hình thang cân.')]
vocab = [
 (r'<b>trapezoid</b> – a quadrilateral with two parallel opposite sides.', r'[[Hình thang]] – tứ giác có hai cạnh đối song song.'),
 (r'<b>base / leg</b> – the parallel sides are the bases; the other two sides are the legs.', r'[[Đáy|đáy (lớp 8)]] / [[cạnh bên|cạnh bên (hình thang)]] – hai cạnh song song là hai đáy; hai cạnh còn lại là hai cạnh bên.'),
 (r'<b>height</b> – a segment from a point of one base perpendicular to the other base.', r'[[Đường cao|đường cao (lớp 8)]] – đoạn thẳng kẻ từ một điểm của đáy này vuông góc với đáy kia.'),
 (r'<b>isosceles trapezoid</b> – a trapezoid with two equal base angles.', r'[[Hình thang cân|hình thang cân (lớp 8)]] – hình thang có hai góc kề một đáy bằng nhau.'),
 (r'<b>base angle</b> – an angle adjacent to a base.', r'[[Góc kề một đáy]] – góc tạo bởi một đáy và một cạnh bên.'),
 (r'<b>right trapezoid</b> – a trapezoid with a right angle.', r'[[Hình thang vuông]] – hình thang có một góc vuông.')]
phrases = [
 (r'<b>Use the figure to identify the bases and legs of trapezoid \(ABCD\).</b>', r'Dựa vào hình, chỉ ra hai đáy và hai cạnh bên của hình thang \(ABCD\).'),
 (r'<b>Name the two pairs of base angles of trapezoid \(PQRS\).</b>', r'Kể tên hai cặp góc kề một đáy của hình thang \(PQRS\).'),
 (r'<b>Determine whether trapezoid \(JKLM\) is isosceles.</b>', r'Xác định hình thang \(JKLM\) có phải hình thang cân không.'),
 (r'<b>The legs \(AD\) and \(BC\) have equal lengths. The diagonals \(AC\) and \(BD\) have equal lengths.</b>', r'Hai cạnh bên \(AD\), \(BC\) bằng nhau. Hai đường chéo \(AC\), \(BD\) bằng nhau.'),
 (r'<b>\(AB\parallel CD\)</b> is read "line \(AB\) is parallel to line \(CD\)"; <b>\(AH\perp CD\)</b> "line \(AH\) is perpendicular to line \(CD\)".', r'Cách đọc: \(AB\parallel CD\) – \(AB\) song song với \(CD\); \(AH\perp CD\) – \(AH\) vuông góc với \(CD\).')]
review = (T(r'<b>Parallel lines (grade 7).</b> If \(AB\parallel CD\), the two angles along a transversal on the same side add up to \(180^\circ\).', r'<b>Hai đường thẳng song song (lớp 7).</b> Nếu \(AB\parallel CD\) thì hai góc trong cùng phía tạo bởi một cát tuyến có tổng \(180^\circ\).'))

theory = '<h3>11.1 %s</h3>' % TI('Trapezoids', 'Hình thang')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'A <b>trapezoid</b> is a quadrilateral with two parallel opposite sides (the <b>bases</b>). The other two sides are the <b>legs</b>. A segment perpendicular to both bases is a <b>height</b>.', r'[[Hình thang]] là tứ giác có hai cạnh đối song song (gọi là hai [[đáy|đáy (lớp 8)]]); hai cạnh còn lại là hai [[cạnh bên|cạnh bên (hình thang)]]; đoạn vuông góc với hai đáy là [[đường cao|đường cao (lớp 8)]].'),
  T(r'In trapezoid \(ABCD\) (\(AB\parallel CD\)), the two angles along a leg are supplementary: \(\widehat{A}+\widehat{D}=180^\circ\), \(\widehat{B}+\widehat{C}=180^\circ\).', r'Trong hình thang \(ABCD\) (\(AB\parallel CD\)), hai góc kề một cạnh bên bù nhau: \(\widehat{A}+\widehat{D}=180^\circ\), \(\widehat{B}+\widehat{C}=180^\circ\).'),
  T1)
theory += '<h3>11.2 %s</h3>' % TI('Isosceles trapezoids', 'Hình thang cân')
theory += BOX('mint', ('Definition and properties', 'Định nghĩa và tính chất'),
  T(r'An <b>isosceles trapezoid</b> is a trapezoid with two equal angles adjacent to one base: \(\widehat{C}=\widehat{D}\) (then also \(\widehat{A}=\widehat{B}\)).', r'[[Hình thang cân|hình thang cân (lớp 8)]] là hình thang có hai góc kề một đáy bằng nhau: \(\widehat{C}=\widehat{D}\) (khi đó cũng có \(\widehat{A}=\widehat{B}\)).'),
  T(r'Properties: the two legs are equal (\(AD=BC\)); the two diagonals are equal (\(AC=BD\)).', r'Tính chất: hai cạnh bên bằng nhau (\(AD=BC\)); hai đường chéo bằng nhau (\(AC=BD\)).'),
  T2)
theory += BOX('blue', ('Tests', 'Dấu hiệu nhận biết'),
  T(r'A trapezoid is isosceles if it has two equal angles adjacent to one base, or if its diagonals are equal.', r'Hình thang có hai góc kề một đáy bằng nhau, hoặc có hai đường chéo bằng nhau, là hình thang cân.'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'),
  T(r'A trapezoid with two equal legs is not always isosceles: a parallelogram also has equal "legs".', r'Hình thang có hai cạnh bên bằng nhau chưa chắc là hình thang cân: hình bình hành cũng có hai cạnh bên bằng nhau.'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Bases, legs, height', 'Đáy, cạnh bên, đường cao'),
  T(r'In the figure of trapezoid \(ABCD\) above (\(AB\parallel CD\), \(AH\perp CD\)), name the bases, the legs and a height.', r'Trong hình thang \(ABCD\) ở hình trên (\(AB\parallel CD\), \(AH\perp CD\)), hãy chỉ ra hai đáy, hai cạnh bên và một đường cao.'),
  ('Bases are the parallel sides.', 'Hai đáy là hai cạnh song song.'),
  [T(r'Bases: \(AB\), \(CD\). Legs: \(AD\), \(BC\). Height: \(AH\).', r'Hai đáy: \(AB\), \(CD\). Hai cạnh bên: \(AD\), \(BC\). Đường cao: \(AH\).')],
  T(r'Bases \(AB, CD\); legs \(AD, BC\); height \(AH\).', r'Đáy \(AB, CD\); cạnh bên \(AD, BC\); đường cao \(AH\).'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Angles of a trapezoid', 'Góc của hình thang'),
  T(r'Trapezoid \(ABCD\) has \(AB\parallel CD\), \(\widehat{A}=110^\circ\), \(\widehat{B}=60^\circ\). Find \(\widehat{C}\) and \(\widehat{D}\).', r'Hình thang \(ABCD\) có \(AB\parallel CD\), \(\widehat{A}=110^\circ\), \(\widehat{B}=60^\circ\). Tính \(\widehat{C}\) và \(\widehat{D}\).'),
  ('Angles along a leg are supplementary.', 'Hai góc kề một cạnh bên bù nhau.'),
  [T(r'\(\widehat{D}=180^\circ-110^\circ=70^\circ\); \(\widehat{C}=180^\circ-60^\circ=120^\circ\).', r'\(\widehat{D}=180^\circ-110^\circ=70^\circ\); \(\widehat{C}=180^\circ-60^\circ=120^\circ\).')],
  T(r'\(\widehat{C}=120^\circ,\ \widehat{D}=70^\circ\).', r'\(\widehat{C}=120^\circ,\ \widehat{D}=70^\circ\).'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('Angles of an isosceles trapezoid', 'Góc của hình thang cân'),
  T(r'Isosceles trapezoid \(EFGH\) has bases \(EF\) and \(GH\), and \(\widehat{EHG}=68^\circ\). Find the other angles.', r'Hình thang cân \(EFGH\) có hai đáy \(EF\), \(GH\) và \(\widehat{EHG}=68^\circ\). Tính các góc còn lại.'),
  ('Equal base angles, supplementary angles along a leg.', 'Hai góc kề một đáy bằng nhau, hai góc kề một cạnh bên bù nhau.'),
  [T(r'\(\widehat{G}=\widehat{H}=68^\circ\).', r'\(\widehat{G}=\widehat{H}=68^\circ\).'),
   T(r'\(\widehat{E}=\widehat{F}=180^\circ-68^\circ=112^\circ\).', r'\(\widehat{E}=\widehat{F}=180^\circ-68^\circ=112^\circ\).')],
  T(r'\(\widehat{G}=68^\circ,\ \widehat{E}=\widehat{F}=112^\circ\).', r'\(\widehat{G}=68^\circ,\ \widehat{E}=\widehat{F}=112^\circ\).'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Cutting an isosceles triangle', 'Cắt tam giác cân'),
  T(r'Triangle \(RST\) has \(RS=RT\) and \(\widehat{S}=70^\circ\). Points \(U\in RS\), \(V\in RT\) with \(UV\parallel ST\). Show that \(UVTS\) is an isosceles trapezoid and find its angles.', r'Tam giác \(RST\) có \(RS=RT\), \(\widehat{S}=70^\circ\). Lấy \(U\in RS\), \(V\in RT\) sao cho \(UV\parallel ST\). Chứng minh \(UVTS\) là hình thang cân và tính các góc của nó.'),
  ('A trapezoid with equal base angles is isosceles.', 'Hình thang có hai góc kề một đáy bằng nhau là hình thang cân.'),
  [T(r'\(UV\parallel ST\), so \(UVTS\) is a trapezoid; \(\widehat{S}=\widehat{T}=70^\circ\) (isosceles triangle), so it is an isosceles trapezoid.', r'\(UV\parallel ST\) nên \(UVTS\) là hình thang; \(\widehat{S}=\widehat{T}=70^\circ\) (tam giác cân) nên nó là hình thang cân.'),
   T(r'\(\widehat{SUV}=\widehat{TVU}=180^\circ-70^\circ=110^\circ\).', r'\(\widehat{SUV}=\widehat{TVU}=180^\circ-70^\circ=110^\circ\).')],
  T(r'\(70^\circ,\ 70^\circ,\ 110^\circ,\ 110^\circ\).', r'Các góc: \(70^\circ,\ 70^\circ,\ 110^\circ,\ 110^\circ\).'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('A bridge frame', 'Khung cầu đi bộ'),
  T(r'The side frame of a pedestrian bridge is trapezoid \(ABCD\) with upper base \(AB=6\) m, lower base \(CD=11\) m, \(\widehat{C}=\widehat{D}=60^\circ\) and \(AD=5\) m. Find \(\widehat{A}\) and the total length of steel for the four sides.', r'Khung một mặt bên của cầu đi bộ là hình thang \(ABCD\) với đáy trên \(AB=6\) m, đáy dưới \(CD=11\) m, \(\widehat{C}=\widehat{D}=60^\circ\), \(AD=5\) m. Tính \(\widehat{A}\) và tổng chiều dài thép làm bốn cạnh của khung.'),
  ('Equal angles at the lower base → isosceles trapezoid.', 'Hai góc kề đáy dưới bằng nhau → hình thang cân.'),
  [T(r'\(\widehat{A}=180^\circ-60^\circ=120^\circ\); the trapezoid is isosceles, so \(BC=AD=5\) m.', r'\(\widehat{A}=180^\circ-60^\circ=120^\circ\); hình thang cân nên \(BC=AD=5\) m.'),
   T(r'Total length: \(6+11+5+5=27\) m.', r'Tổng chiều dài: \(6+11+5+5=27\) m.')],
  T(r'\(\widehat{A}=120^\circ\); 27 m of steel.', r'\(\widehat{A}=120^\circ\); cần 27 m thép.'))

_SETS = sp_g8b.BANK(sp_g8b.L11_GROUPS, start=1, seeds=(8111, 8112, 8113))
practice = LEVEL_PRACTICE(sp_g8b.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Pairing the wrong angles.</b> In trapezoid \(ABCD\) (\(AB\parallel CD\)), \(\widehat{A}+\widehat{D}=180^\circ\), not \(\widehat{A}+\widehat{C}\).', r'<b>Ghép sai cặp góc.</b> Trong hình thang \(ABCD\) (\(AB\parallel CD\)), \(\widehat{A}+\widehat{D}=180^\circ\), không phải \(\widehat{A}+\widehat{C}\).'),
 (r'<b>Equal legs ⇒ isosceles?</b> Not always (parallelograms).', r'<b>Hai cạnh bên bằng nhau ⇒ hình thang cân?</b> Chưa chắc (hình bình hành).'),
 (r'<b>Equal diagonals in any trapezoid.</b> Only isosceles trapezoids have equal diagonals.', r'<b>Cho rằng mọi hình thang có hai đường chéo bằng nhau.</b> Chỉ hình thang cân mới có.'),
 (r'<b>Forgetting the right-angle mark on a height.</b> A height is perpendicular to the bases.', r'<b>Quên kí hiệu góc vuông ở đường cao.</b> Đường cao vuông góc với hai đáy.')]
summary = [
 (r'Trapezoid: two parallel opposite sides (bases); angles along a leg are supplementary.', r'Hình thang: hai cạnh đối song song (hai đáy); hai góc kề một cạnh bên bù nhau.'),
 (r'Isosceles trapezoid: equal base angles; equal legs; equal diagonals.', r'Hình thang cân: hai góc kề một đáy bằng nhau; hai cạnh bên bằng nhau; hai đường chéo bằng nhau.'),
 (r'Tests: equal base angles, or equal diagonals.', r'Dấu hiệu: hai góc kề một đáy bằng nhau, hoặc hai đường chéo bằng nhau.'),
 (r'Key English: trapezoid, isosceles trapezoid, base, leg, height, base angle.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[hình thang]], [[hình thang cân|hình thang cân (lớp 8)]], [[đáy|đáy (lớp 8)]], [[cạnh bên|cạnh bên (hình thang)]], [[đường cao|đường cao (lớp 8)]], [[góc kề một đáy]].')]
checks = [
 (r'I can name the bases, legs and a height of a trapezoid.', r'Em chỉ ra được đáy, cạnh bên, đường cao của hình thang.'),
 (r'I can find angles in trapezoids and isosceles trapezoids.', r'Em tính được góc của hình thang, hình thang cân.'),
 (r'I can show that a trapezoid is isosceles.', r'Em chứng minh được một hình thang là hình thang cân.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Isosceles Trapezoids', title_vi='Hình thang cân', topic=TOPIC,
       folder='quadrilaterals', file='isosceles-trapezoids', catalog_title_vi='Hình thang cân',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Trapezoids, isosceles trapezoids: properties and tests.', level='Beginner', minutes=45,
       description_vi='Bài 11 – Hình thang, hình thang cân: định nghĩa, tính chất (cạnh bên, đường chéo, góc kề một đáy), dấu hiệu nhận biết.',
       tags_vi=['hình thang', 'hình thang cân', 'đường cao'],
       prerequisites=['g8-quadrilaterals-01'], tags=['trapezoid', 'isosceles trapezoid', 'base angle'], order=110)
