# -*- coding: utf-8 -*-
"""Nội dung bài g8-quadrilaterals-03 = Toán 8 KNTT, Bài 12: Hình bình hành – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 8 (2026), Chapter 3 – Lesson 12, tr. 43–45 (parallelogram, consecutive angles, bisect, test for a parallelogram)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g8b
from sp_g8b import FIGT

LID = 'g8-quadrilaterals-03'
CH = 'Tứ giác'
TOPIC = ('Quadrilaterals', CH)
ensure_vocab([
 ('g8-consec-angles', 'consecutive angles', 'hai góc kề một cạnh', CH, 'In a parallelogram, two consecutive angles are supplementary.', ''),
 ('g8-bisect', 'bisect each other', 'cắt nhau tại trung điểm của mỗi đường', CH, 'The diagonals of a parallelogram bisect each other.', ''),
 ('g8-test', 'test (for a figure)', 'dấu hiệu nhận biết (lớp 8)', CH, 'Use a test for a parallelogram to decide whether ABCD is a parallelogram.', ''),
])
load_vocab()

P1 = FIGT({'A': (0, 0), 'B': (3.9, 0), 'C': (5.1, 2.2), 'D': (1.2, 2.2), 'O': (2.55, 1.1)}, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('A', 'C'), ('B', 'D')],
          cap=('Parallelogram \\(ABCD\\); diagonals meet at \\(O\\).', 'Hình bình hành \\(ABCD\\); hai đường chéo cắt nhau tại \\(O\\).'))
EX4 = FIGT({'K': (0, 0), 'L': (4.0, 0), 'M': (5.2, 2.2), 'N': (1.2, 2.2), 'P': (2.0, 0), 'Q': (3.2, 2.2)}, segs=[('K', 'L'), ('L', 'M'), ('M', 'N'), ('N', 'K'), ('L', 'Q'), ('N', 'P')], px=250)

# ---------- kiểm tra số liệu ----------
x = (180 - 18 + 6) // 8; assert x == 21 and 3 * x + 18 == 81 and 5 * x - 6 == 99          # Ví dụ 2
assert 2 * 4 == 8 and 2 * 3 == 6                                                             # Ví dụ 3

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 60 minutes', '60 phút'),
            before=('trapezoids (Lesson 11); congruent triangles (grade 7)', 'hình thang (Bài 11); các trường hợp bằng nhau của tam giác (lớp 7)'))
goals = [
 (r'recognize a parallelogram;', r'nhận biết được [[hình bình hành]];'),
 (r'use its properties: opposite sides equal, opposite angles equal, diagonals bisect each other;', r'sử dụng được tính chất: các cạnh đối bằng nhau, các góc đối bằng nhau, hai đường chéo [[cắt nhau tại trung điểm của mỗi đường]];'),
 (r'use the tests to prove that a quadrilateral is a parallelogram.', r'dùng được các [[dấu hiệu nhận biết|dấu hiệu nhận biết (lớp 8)]] để chứng minh một tứ giác là hình bình hành.')]
vocab = [
 (r'<b>parallelogram</b> – a quadrilateral whose opposite sides are parallel.', r'[[Hình bình hành]] – tứ giác có các cạnh đối song song.'),
 (r'<b>consecutive angles</b> – two angles with a common side, e.g. \(\widehat{A}\) and \(\widehat{B}\).', r'[[Hai góc kề một cạnh]] – hai góc có chung một cạnh, chẳng hạn \(\widehat{A}\) và \(\widehat{B}\).'),
 (r'<b>midpoint / bisect each other</b> – the diagonals meet at the midpoint of each.', r'[[Trung điểm]] / [[cắt nhau tại trung điểm của mỗi đường]] – hai đường chéo cắt nhau tại trung điểm của mỗi đường.'),
 (r'<b>test for a parallelogram</b> – a condition that proves a quadrilateral is a parallelogram.', r'[[Dấu hiệu nhận biết|dấu hiệu nhận biết (lớp 8)]] hình bình hành – điều kiện đủ để kết luận tứ giác là hình bình hành.')]
phrases = [
 (r'<b>Identify the pairs of opposite sides in quadrilateral \(ABCD\).</b>', r'Chỉ ra các cặp cạnh đối của tứ giác \(ABCD\).'),
 (r'<b>Determine whether quadrilateral \(PQRS\) is a parallelogram.</b>', r'Xác định tứ giác \(PQRS\) có phải hình bình hành không.'),
 (r'<b>Since \(ABCD\) is a parallelogram, \(AB=CD\) and \(AD=BC\).</b>', r'Vì \(ABCD\) là hình bình hành nên \(AB=CD\) và \(AD=BC\).'),
 (r'<b>Point \(O\) is the midpoint of both diagonals.</b>', r'\(O\) là trung điểm của cả hai đường chéo.'),
 (r'<b>Segments \(EF\) and \(GH\) are parallel and have equal lengths, so \(EFGH\) is a parallelogram.</b>', r'\(EF\) và \(GH\) song song và bằng nhau nên \(EFGH\) là hình bình hành.')]
review = (T(r'<b>Trapezoid (Lesson 11).</b> Two angles along a leg are supplementary.', r'<b>Hình thang (Bài 11).</b> Hai góc kề một cạnh bên bù nhau.') +
          T(r'<b>Congruent triangles (grade 7).</b> s.s.s., s.a.s., a.s.a.', r'<b>Hai tam giác bằng nhau (lớp 7).</b> c.c.c, c.g.c, g.c.g.'))

theory = '<h3>12.1 %s</h3>' % TI('Definition and properties', 'Định nghĩa và tính chất')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'A <b>parallelogram</b> is a quadrilateral with both pairs of opposite sides parallel: \(AB\parallel CD\), \(AD\parallel BC\).', r'[[Hình bình hành]] là tứ giác có các cạnh đối song song: \(AB\parallel CD\), \(AD\parallel BC\).'),
  P1)
theory += BOX('mint', ('Properties', 'Tính chất'),
  T(r'In parallelogram \(ABCD\): opposite sides are equal (\(AB=CD,\ AD=BC\)); opposite angles are equal (\(\widehat{A}=\widehat{C},\ \widehat{B}=\widehat{D}\)); the diagonals bisect each other (\(OA=OC,\ OB=OD\)).', r'Trong hình bình hành \(ABCD\): các cạnh đối bằng nhau (\(AB=CD,\ AD=BC\)); các góc đối bằng nhau (\(\widehat{A}=\widehat{C},\ \widehat{B}=\widehat{D}\)); hai đường chéo cắt nhau tại trung điểm của mỗi đường (\(OA=OC,\ OB=OD\)).'),
  T(r'Consecutive angles are supplementary: \(\widehat{A}+\widehat{B}=180^\circ\).', r'Hai góc kề một cạnh bù nhau: \(\widehat{A}+\widehat{B}=180^\circ\).'))
theory += '<h3>12.2 %s</h3>' % TI('Tests for a parallelogram', 'Dấu hiệu nhận biết hình bình hành')
theory += BOX('blue', ('A quadrilateral is a parallelogram if…', 'Tứ giác là hình bình hành nếu…'),
  T(r'1) both pairs of opposite sides are parallel; 2) both pairs of opposite sides are equal; 3) one pair of opposite sides is parallel and equal; 4) both pairs of opposite angles are equal; 5) the diagonals bisect each other.', r'1) các cạnh đối song song; 2) các cạnh đối bằng nhau; 3) có hai cạnh đối song song và bằng nhau; 4) các góc đối bằng nhau; 5) hai đường chéo cắt nhau tại trung điểm của mỗi đường.'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'),
  T(r'"One pair of opposite sides parallel" and "the other pair equal" is <b>not</b> a test: an isosceles trapezoid satisfies it.', r'"Một cặp cạnh đối song song, cặp kia bằng nhau" <b>không</b> phải dấu hiệu: hình thang cân cũng thỏa mãn.'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Sides and angles', 'Cạnh và góc'),
  T(r'Parallelogram \(ABCD\) has \(AB=5\) cm, \(BC=3\) cm and \(\widehat{A}=65^\circ\). Find \(CD\), \(AD\), \(\widehat{C}\), \(\widehat{B}\).', r'Hình bình hành \(ABCD\) có \(AB=5\) cm, \(BC=3\) cm, \(\widehat{A}=65^\circ\). Tính \(CD\), \(AD\), \(\widehat{C}\), \(\widehat{B}\).'),
  ('Opposite sides and opposite angles are equal.', 'Các cạnh đối, các góc đối bằng nhau.'),
  [T(r'\(CD=AB=5\) cm, \(AD=BC=3\) cm.', r'\(CD=AB=5\) cm, \(AD=BC=3\) cm.'),
   T(r'\(\widehat{C}=\widehat{A}=65^\circ\), \(\widehat{B}=180^\circ-65^\circ=115^\circ\).', r'\(\widehat{C}=\widehat{A}=65^\circ\), \(\widehat{B}=180^\circ-65^\circ=115^\circ\).')],
  T(r'\(CD=5\) cm, \(AD=3\) cm, \(\widehat{C}=65^\circ\), \(\widehat{B}=115^\circ\).', r'\(CD=5\) cm, \(AD=3\) cm, \(\widehat{C}=65^\circ\), \(\widehat{B}=115^\circ\).'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Consecutive angles', 'Hai góc kề một cạnh'),
  T(r'In parallelogram \(ABCD\), \(\widehat{A}=(3x+18)^\circ\) and \(\widehat{B}=(5x-6)^\circ\). Find \(x\) and the angles.', r'Hình bình hành \(ABCD\) có \(\widehat{A}=(3x+18)^\circ\), \(\widehat{B}=(5x-6)^\circ\). Tìm \(x\) và các góc.'),
  ('\\(\\widehat{A}+\\widehat{B}=180^\\circ\\).', '\\(\\widehat{A}+\\widehat{B}=180^\\circ\\).'),
  [T(r'\(8x+12=180\Rightarrow x=21\).', r'\(8x+12=180\Rightarrow x=21\).'),
   T(r'\(\widehat{A}=\widehat{C}=81^\circ\), \(\widehat{B}=\widehat{D}=99^\circ\).', r'\(\widehat{A}=\widehat{C}=81^\circ\), \(\widehat{B}=\widehat{D}=99^\circ\).')],
  T(r'\(x=21\); \(81^\circ,\ 99^\circ,\ 81^\circ,\ 99^\circ\).', r'\(x=21\); \(81^\circ,\ 99^\circ,\ 81^\circ,\ 99^\circ\).'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('Is it a parallelogram?', 'Có phải hình bình hành?'),
  T(r'a) Quadrilateral \(JKLM\) has \(JK\parallel LM\) and \(JK=LM\). b) The diagonals of \(PQRS\) meet at \(T\) with \(PT=TR=4\) cm, \(QT=TS=3\) cm. Are they parallelograms? Find \(PR\), \(QS\).', r'a) Tứ giác \(JKLM\) có \(JK\parallel LM\) và \(JK=LM\). b) Hai đường chéo của \(PQRS\) cắt nhau tại \(T\), \(PT=TR=4\) cm, \(QT=TS=3\) cm. Chúng có phải hình bình hành không? Tính \(PR\), \(QS\).'),
  ('Compare with the tests.', 'Đối chiếu với các dấu hiệu.'),
  [T(r'a) One pair of opposite sides parallel and equal ⇒ parallelogram.', r'a) Có hai cạnh đối song song và bằng nhau ⇒ hình bình hành.'),
   T(r'b) The diagonals bisect each other ⇒ parallelogram; \(PR=8\) cm, \(QS=6\) cm.', r'b) Hai đường chéo cắt nhau tại trung điểm mỗi đường ⇒ hình bình hành; \(PR=8\) cm, \(QS=6\) cm.')],
  T(r'Both are parallelograms; \(PR=8\) cm, \(QS=6\) cm.', r'Cả hai đều là hình bình hành; \(PR=8\) cm, \(QS=6\) cm.'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('A proof with midpoints', 'Chứng minh với trung điểm'),
  T(r'In parallelogram \(KLMN\), \(P\) is the midpoint of \(KL\) and \(Q\) is the midpoint of \(MN\). Prove that \(LQ=NP\).', r'Cho hình bình hành \(KLMN\); \(P\) là trung điểm của \(KL\), \(Q\) là trung điểm của \(MN\). Chứng minh \(LQ=NP\).') + EX4,
  ('Show that \\(PLQN\\) is a parallelogram.', 'Chứng minh \\(PLQN\\) là hình bình hành.'),
  [T(r'\(PL=\dfrac{KL}{2}\), \(NQ=\dfrac{MN}{2}\) and \(KL=MN\), so \(PL=NQ\); also \(PL\parallel NQ\) (on \(KL\parallel MN\)).', r'\(PL=\dfrac{KL}{2}\), \(NQ=\dfrac{MN}{2}\) mà \(KL=MN\) nên \(PL=NQ\); lại có \(PL\parallel NQ\) (vì \(KL\parallel MN\)).'),
   T(r'So \(PLQN\) is a parallelogram (one pair of opposite sides parallel and equal), hence \(LQ=NP\).', r'Vậy \(PLQN\) là hình bình hành (hai cạnh đối song song và bằng nhau), suy ra \(LQ=NP\).')],
  T(r'\(LQ=NP\).', r'\(LQ=NP\).'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('A vehicle lift', 'Bệ nâng ô tô'),
  T(r'A vehicle lift has two equal arms \(AD\) and \(BC\) that always stay parallel; \(A, B\) are on the ground and \(C, D\) on the platform. Why does the platform \(DC\) stay parallel to the ground \(AB\)?', r'Bệ nâng ô tô có hai tay nâng \(AD\), \(BC\) bằng nhau và luôn song song; \(A, B\) gắn với mặt đất, \(C, D\) gắn với sàn nâng. Vì sao sàn nâng \(DC\) luôn song song với mặt đất \(AB\)?'),
  ('Look at quadrilateral \\(ABCD\\).', 'Xét tứ giác \\(ABCD\\).'),
  [T(r'\(AD\parallel BC\) and \(AD=BC\), so \(ABCD\) is a parallelogram.', r'\(AD\parallel BC\) và \(AD=BC\) nên \(ABCD\) là hình bình hành.'),
   T(r'Hence \(DC\parallel AB\) at every position of the arms.', r'Do đó \(DC\parallel AB\) ở mọi vị trí của tay nâng.')],
  T(r'\(ABCD\) is always a parallelogram, so \(DC\parallel AB\).', r'\(ABCD\) luôn là hình bình hành nên \(DC\parallel AB\).'))

_SETS = sp_g8b.BANK(sp_g8b.L12_GROUPS, start=1, seeds=(8121, 8122, 8123))
practice = LEVEL_PRACTICE(sp_g8b.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Equal diagonals in every parallelogram.</b> Not true; only rectangles have equal diagonals.', r'<b>Cho rằng hình bình hành có hai đường chéo bằng nhau.</b> Sai; chỉ hình chữ nhật mới có.'),
 (r'<b>Equal consecutive angles.</b> Consecutive angles are supplementary, opposite angles are equal.', r'<b>Cho hai góc kề bằng nhau.</b> Hai góc kề một cạnh bù nhau; hai góc đối mới bằng nhau.'),
 (r'<b>Using a non-test.</b> "One pair parallel, the other pair equal" does not prove a parallelogram.', r'<b>Dùng sai dấu hiệu.</b> "Một cặp song song, cặp kia bằng nhau" không đủ để kết luận hình bình hành.'),
 (r'<b>\(OA=OB\)?</b> In a parallelogram \(OA=OC\) and \(OB=OD\), but \(OA\) and \(OB\) need not be equal.', r'<b>\(OA=OB\)?</b> Trong hình bình hành \(OA=OC\), \(OB=OD\) nhưng \(OA\) chưa chắc bằng \(OB\).')]
summary = [
 (r'Parallelogram: opposite sides parallel.', r'Hình bình hành: tứ giác có các cạnh đối song song.'),
 (r'Properties: opposite sides equal; opposite angles equal; diagonals bisect each other.', r'Tính chất: các cạnh đối bằng nhau; các góc đối bằng nhau; hai đường chéo cắt nhau tại trung điểm mỗi đường.'),
 (r'Five tests (sides parallel / equal, one pair parallel and equal, angles, diagonals).', r'Năm dấu hiệu (cạnh đối song song / bằng nhau, hai cạnh đối song song và bằng nhau, góc đối, đường chéo).'),
 (r'Key English: parallelogram, consecutive angles, bisect each other, test.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[hình bình hành]], [[hai góc kề một cạnh]], [[cắt nhau tại trung điểm của mỗi đường]], [[dấu hiệu nhận biết|dấu hiệu nhận biết (lớp 8)]].')]
checks = [
 (r'I can use the properties of a parallelogram to find sides and angles.', r'Em dùng được tính chất hình bình hành để tính cạnh, góc.'),
 (r'I can choose a suitable test to prove a quadrilateral is a parallelogram.', r'Em chọn được dấu hiệu thích hợp để chứng minh tứ giác là hình bình hành.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Parallelograms', title_vi='Hình bình hành', topic=TOPIC,
       folder='quadrilaterals', file='parallelograms', catalog_title_vi='Hình bình hành',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Parallelograms: properties and tests.', level='Intermediate', minutes=60,
       description_vi='Bài 12 – Hình bình hành: định nghĩa, tính chất (cạnh, góc, đường chéo), dấu hiệu nhận biết.',
       tags_vi=['hình bình hành', 'dấu hiệu nhận biết', 'đường chéo'],
       prerequisites=['g8-quadrilaterals-02'], tags=['parallelogram', 'test', 'bisect'], order=120)
