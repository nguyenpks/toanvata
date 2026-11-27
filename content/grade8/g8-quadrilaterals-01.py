# -*- coding: utf-8 -*-
"""Nội dung bài g8-quadrilaterals-01 = Toán 8 KNTT, Bài 10: Tứ giác – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 8 (2026), Chapter 3 – Lesson 10, tr. 37–39."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g8b
from sp_g8b import FIGT

LID = 'g8-quadrilaterals-01'
CH = 'Tứ giác'
TOPIC = ('Quadrilaterals', CH)
ensure_vocab([
 ('g8-quadrilateral', 'quadrilateral', 'tứ giác (lớp 8)', CH, 'ABCD is a quadrilateral with four sides AB, BC, CD and DA.', ''),
 ('g8-convex-quad', 'convex quadrilateral', 'tứ giác lồi', CH, 'A convex quadrilateral always lies in one half-plane determined by any line containing one of its sides.', ''),
 ('g8-vertex', 'vertex', 'đỉnh (lớp 8)', CH, 'A quadrilateral has four vertices.', ''),
 ('g8-side', 'side', 'cạnh (lớp 8)', CH, 'AB is a side of quadrilateral ABCD.', ''),
 ('g8-interior-angle', 'interior angle', 'góc trong (lớp 8)', CH, 'The interior angles of a quadrilateral add up to 360°.', ''),
 ('g8-opp-vertices', 'opposite vertices', 'hai đỉnh đối nhau', CH, 'A and C are opposite vertices of ABCD.', ''),
 ('g8-opp-sides', 'opposite sides', 'hai cạnh đối nhau (lớp 8)', CH, 'AB and CD are opposite sides of ABCD.', ''),
 ('g8-opp-angles', 'opposite angles', 'hai góc đối nhau (lớp 8)', CH, 'Angles A and C are opposite angles of ABCD.', ''),
 ('g8-consec-vertices', 'consecutive vertices', 'hai đỉnh kề nhau', CH, 'A and B are consecutive vertices of ABCD.', ''),
])
load_vocab()

Q1 = FIGT({'A': (0, 0), 'B': (4.2, 0.2), 'C': (3.6, 2.6), 'D': (0.7, 2.2)}, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')], dash=[('A', 'C'), ('B', 'D')],
          cap=('Convex quadrilateral \\(ABCD\\) with diagonals \\(AC\\), \\(BD\\).', 'Tứ giác lồi \\(ABCD\\) với hai đường chéo \\(AC\\), \\(BD\\).'))
Q2 = FIGT({'M': (0, 0), 'N': (4, 0), 'P': (1.8, 1.0), 'Q': (0.8, 2.8)}, segs=[('M', 'N'), ('N', 'P'), ('P', 'Q'), ('Q', 'M')], px=220,
          cap=('\\(MNPQ\\) is not convex: line \\(NP\\) cuts the quadrilateral.', '\\(MNPQ\\) không phải tứ giác lồi: đường thẳng \\(NP\\) cắt qua tứ giác.'))
EX1 = FIGT({'P': (0, 0), 'Q': (4.0, -0.3), 'R': (3.4, 2.4), 'S': (0.5, 2.0)}, segs=[('P', 'Q'), ('Q', 'R'), ('R', 'S'), ('S', 'P')], px=230)

# ---------- kiểm tra số liệu ----------
assert 360 - 70 - 110 - 95 == 85                                                          # Ví dụ 2
assert [k * 360 // 15 for k in (2, 3, 4, 6)] == [48, 72, 96, 144]                           # Ví dụ 3
x = (360 - 15 + 10 - 25 - 30) // 6; assert x == 50 and [x + 15, 2 * x - 10, x + 25, 2 * x + 30] == [65, 90, 75, 130]   # Ví dụ 4
assert (360 - 100 - 120) // 2 == 70                                                         # Ví dụ 5

meta = dict(level=('Beginner', 'Cơ bản'), time=('about 45 minutes', '45 phút'),
            before=('triangles, angle sum of a triangle (grade 7)', 'tam giác, tổng ba góc của tam giác (lớp 7)'))
goals = [
 (r'recognize a quadrilateral, a convex quadrilateral and their vertices, sides, angles and diagonals;', r'nhận biết được [[tứ giác|tứ giác (lớp 8)]], [[tứ giác lồi]] và các [[đỉnh|đỉnh (lớp 8)]], [[cạnh|cạnh (lớp 8)]], góc, [[đường chéo]] của nó;'),
 (r'explain and use the fact that the angles of a quadrilateral add up to \(360^\circ\);', r'giải thích và sử dụng được định lí tổng các góc của một tứ giác bằng \(360^\circ\);'),
 (r'find unknown angles in quadrilaterals, including problems with \(x\) and ratios.', r'tính được góc chưa biết của tứ giác, kể cả bài toán có ẩn \(x\) hoặc tỉ số.')]
vocab = [
 (r'<b>quadrilateral</b> – a figure \(ABCD\) made of four segments \(AB, BC, CD, DA\), no two of which lie on the same line.', r'[[Tứ giác|tứ giác (lớp 8)]] – hình \(ABCD\) gồm bốn đoạn thẳng \(AB, BC, CD, DA\), trong đó không có hai đoạn nào cùng nằm trên một đường thẳng.'),
 (r'<b>convex quadrilateral</b> – it always lies on one side of the line through any of its sides.', r'[[Tứ giác lồi]] – tứ giác luôn nằm về một phía của đường thẳng chứa bất kì cạnh nào của nó.'),
 (r'<b>vertex / side / diagonal</b> – \(A\) is a vertex, \(AB\) a side, \(AC\) a diagonal.', r'[[Đỉnh|đỉnh (lớp 8)]] / [[cạnh|cạnh (lớp 8)]] / [[đường chéo]] – \(A\) là đỉnh, \(AB\) là cạnh, \(AC\) là đường chéo.'),
 (r'<b>interior angle</b> – \(\widehat{A}=\widehat{DAB}\), \(\widehat{B}\), \(\widehat{C}\), \(\widehat{D}\).', r'[[Góc trong|góc trong (lớp 8)]] (góc của tứ giác) – \(\widehat{A}=\widehat{DAB}\), \(\widehat{B}\), \(\widehat{C}\), \(\widehat{D}\).'),
 (r'<b>consecutive / opposite vertices</b> – \(A, B\) are consecutive; \(A, C\) are opposite.', r'[[Hai đỉnh kề nhau]] / [[hai đỉnh đối nhau]] – \(A, B\) kề nhau; \(A, C\) đối nhau.'),
 (r'<b>opposite sides / opposite angles</b> – \(AB, CD\) are opposite sides; \(\widehat{A}, \widehat{C}\) are opposite angles.', r'[[Hai cạnh đối nhau|hai cạnh đối nhau (lớp 8)]] / [[hai góc đối nhau|hai góc đối nhau (lớp 8)]] – \(AB, CD\) là hai cạnh đối; \(\widehat{A}, \widehat{C}\) là hai góc đối.')]
phrases = [
 (r'<b>List the four sides and two diagonals of quadrilateral \(PQRS\).</b>', r'Kể tên bốn cạnh và hai đường chéo của tứ giác \(PQRS\).'),
 (r'<b>Identify each pair of opposite vertices in quadrilateral \(KLMN\).</b>', r'Chỉ ra các cặp đỉnh đối nhau của tứ giác \(KLMN\).'),
 (r'<b>Determine whether quadrilateral \(EFGH\) is convex.</b>', r'Xác định tứ giác \(EFGH\) có phải là tứ giác lồi không.'),
 (r'<b>Draw diagonal \(AC\) to divide quadrilateral \(ABCD\) into two triangles.</b>', r'Vẽ đường chéo \(AC\) để chia tứ giác \(ABCD\) thành hai tam giác.'),
 (r'<b>Since diagonal \(AC\) forms two triangles, the angle sum is \(2\times180^\circ=360^\circ\).</b>', r'Vì đường chéo \(AC\) tạo thành hai tam giác nên tổng các góc là \(2\cdot180^\circ=360^\circ\).'),
 (r'<b>Opposite sides \(AB\) and \(CD\) do not share a vertex.</b>', r'Hai cạnh đối \(AB\) và \(CD\) không có đỉnh chung.')]
review = (T(r'<b>Angle sum of a triangle (grade 7).</b> \(\widehat{A}+\widehat{B}+\widehat{C}=180^\circ\).', r'<b>Tổng ba góc của tam giác (lớp 7).</b> \(\widehat{A}+\widehat{B}+\widehat{C}=180^\circ\).') +
          T(r'<b>Supplementary angles.</b> Two adjacent angles on a line add up to \(180^\circ\).', r'<b>Hai góc kề bù</b> có tổng bằng \(180^\circ\).'))

theory = '<h3>10.1 %s</h3>' % TI('Quadrilaterals', 'Tứ giác')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'Quadrilateral \(ABCD\) is the figure formed by four segments \(AB, BC, CD, DA\), no two of which lie on the same line.', r'[[Tứ giác|tứ giác (lớp 8)]] \(ABCD\) là hình gồm bốn đoạn thẳng \(AB, BC, CD, DA\), trong đó không có hai đoạn thẳng nào cùng nằm trên một đường thẳng.'),
  T(r'Vertices: \(A, B, C, D\). Sides: \(AB, BC, CD, DA\). Diagonals: \(AC, BD\) (they join opposite vertices). Angles: \(\widehat{A}, \widehat{B}, \widehat{C}, \widehat{D}\).', r'Các đỉnh: \(A, B, C, D\). Các cạnh: \(AB, BC, CD, DA\). Các đường chéo: \(AC, BD\) (nối hai đỉnh đối nhau). Các góc: \(\widehat{A}, \widehat{B}, \widehat{C}, \widehat{D}\).'),
  Q1)
theory += BOX('mint', ('Convex quadrilateral', 'Tứ giác lồi'),
  T(r'A <b>convex quadrilateral</b> always lies on one side of the line through any of its sides. From now on, "quadrilateral" means a convex quadrilateral.', r'[[Tứ giác lồi]] là tứ giác luôn nằm về một phía của đường thẳng chứa bất kì cạnh nào của nó. Từ nay, khi nói tứ giác mà không chú thích gì thêm, ta hiểu đó là tứ giác lồi.'),
  Q2)
theory += '<h3>10.2 %s</h3>' % TI('Angle sum of a quadrilateral', 'Tổng các góc của một tứ giác')
theory += BOX('blue', ('Theorem', 'Định lí'),
  T(r'The four angles of a quadrilateral add up to \(360^\circ\): \(\widehat{A}+\widehat{B}+\widehat{C}+\widehat{D}=360^\circ\).', r'Tổng các góc của một tứ giác bằng \(360^\circ\): \(\widehat{A}+\widehat{B}+\widehat{C}+\widehat{D}=360^\circ\).'),
  T(r'Reason: diagonal \(AC\) divides \(ABCD\) into triangles \(ABC\) and \(ACD\); each has angle sum \(180^\circ\), so the total is \(2\cdot180^\circ=360^\circ\).', r'Giải thích: đường chéo \(AC\) chia tứ giác thành hai tam giác \(ABC\) và \(ACD\); mỗi tam giác có tổng ba góc \(180^\circ\) nên tổng là \(2\cdot180^\circ=360^\circ\).'))
theory += BOX('yellow', ('Consequences', 'Hệ quả'),
  T(r'A quadrilateral cannot have four acute angles (sum \(<360^\circ\)) nor four obtuse angles (sum \(>360^\circ\)). If it has three right angles, the fourth is also a right angle.', r'Một tứ giác không thể có bốn góc nhọn (tổng \(<360^\circ\)), cũng không thể có bốn góc tù (tổng \(>360^\circ\)). Nếu có ba góc vuông thì góc thứ tư cũng vuông.'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Name the parts', 'Gọi tên các yếu tố'),
  T(r'For quadrilateral \(PQRS\) in the figure, list the sides, the diagonals and the pairs of opposite vertices.', r'Với tứ giác \(PQRS\) trong hình, hãy kể tên các cạnh, các đường chéo và các cặp đỉnh đối nhau.') + EX1,
  ('Go around the quadrilateral in order \\(P\\to Q\\to R\\to S\\).', 'Đi theo thứ tự \\(P\\to Q\\to R\\to S\\).'),
  [T(r'Sides: \(PQ, QR, RS, SP\).', r'Các cạnh: \(PQ, QR, RS, SP\).'),
   T(r'Diagonals: \(PR, QS\). Opposite vertices: \(P\) and \(R\); \(Q\) and \(S\).', r'Các đường chéo: \(PR, QS\). Các cặp đỉnh đối nhau: \(P\) và \(R\); \(Q\) và \(S\).')],
  T(r'Sides \(PQ, QR, RS, SP\); diagonals \(PR, QS\); opposite vertices \(P, R\) and \(Q, S\).', r'Cạnh \(PQ, QR, RS, SP\); đường chéo \(PR, QS\); đỉnh đối: \(P, R\) và \(Q, S\).'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('The fourth angle', 'Góc thứ tư'),
  T(r'Quadrilateral \(ABCD\) has \(\widehat{A}=70^\circ\), \(\widehat{B}=110^\circ\), \(\widehat{C}=95^\circ\). Find \(\widehat{D}\).', r'Tứ giác \(ABCD\) có \(\widehat{A}=70^\circ\), \(\widehat{B}=110^\circ\), \(\widehat{C}=95^\circ\). Tính \(\widehat{D}\).'),
  ('Use the angle sum \\(360^\\circ\\).', 'Dùng tổng các góc bằng \\(360^\\circ\\).'),
  [T(r'\(\widehat{D}=360^\circ-(70^\circ+110^\circ+95^\circ)=85^\circ\).', r'\(\widehat{D}=360^\circ-(70^\circ+110^\circ+95^\circ)=85^\circ\).')],
  T(r'\(\widehat{D}=85^\circ\).', r'\(\widehat{D}=85^\circ\).'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('Angles in a ratio', 'Các góc tỉ lệ'),
  T(r'The angles \(\widehat{A}, \widehat{B}, \widehat{C}, \widehat{D}\) of a quadrilateral are in the ratio \(2:3:4:6\). Find them.', r'Các góc \(\widehat{A}, \widehat{B}, \widehat{C}, \widehat{D}\) của một tứ giác tỉ lệ với \(2:3:4:6\). Tính các góc đó.'),
  ('Divide \\(360^\\circ\\) into \\(2+3+4+6=15\\) equal parts.', 'Chia \\(360^\\circ\\) thành \\(2+3+4+6=15\\) phần bằng nhau.'),
  [T(r'One part: \(360^\circ:15=24^\circ\).', r'Mỗi phần: \(360^\circ:15=24^\circ\).'),
   T(r'\(\widehat{A}=48^\circ,\ \widehat{B}=72^\circ,\ \widehat{C}=96^\circ,\ \widehat{D}=144^\circ\).', r'\(\widehat{A}=48^\circ,\ \widehat{B}=72^\circ,\ \widehat{C}=96^\circ,\ \widehat{D}=144^\circ\).')],
  T(r'\(48^\circ,\ 72^\circ,\ 96^\circ,\ 144^\circ\).', r'\(48^\circ,\ 72^\circ,\ 96^\circ,\ 144^\circ\).'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Angles with x', 'Góc có ẩn x'),
  T(r'The angles of quadrilateral \(ABCD\) are \((x+15)^\circ,\ (2x-10)^\circ,\ (x+25)^\circ,\ (2x+30)^\circ\). Find \(x\) and each angle.', r'Các góc của tứ giác \(ABCD\) lần lượt là \((x+15)^\circ,\ (2x-10)^\circ,\ (x+25)^\circ,\ (2x+30)^\circ\). Tìm \(x\) và số đo mỗi góc.'),
  ('Add the four expressions and set the sum equal to 360.', 'Cộng bốn biểu thức và cho tổng bằng 360.'),
  [T(r'\(6x+60=360\Rightarrow x=50\).', r'\(6x+60=360\Rightarrow x=50\).'),
   T(r'Angles: \(65^\circ,\ 90^\circ,\ 75^\circ,\ 130^\circ\) (check: sum \(360^\circ\)).', r'Các góc: \(65^\circ,\ 90^\circ,\ 75^\circ,\ 130^\circ\) (thử lại: tổng \(360^\circ\)).')],
  T(r'\(x=50\); \(65^\circ,\ 90^\circ,\ 75^\circ,\ 130^\circ\).', r'\(x=50\); \(65^\circ,\ 90^\circ,\ 75^\circ,\ 130^\circ\).'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('A kite frame', 'Khung diều'),
  T(r'A kite frame \(ABCD\) has \(AB=BC\), \(AD=CD\), \(\widehat{ABC}=100^\circ\), \(\widehat{CDA}=120^\circ\). Find \(\widehat{DAB}\) and \(\widehat{BCD}\).', r'Khung diều \(ABCD\) có \(AB=BC\), \(AD=CD\), \(\widehat{ABC}=100^\circ\), \(\widehat{CDA}=120^\circ\). Tính \(\widehat{DAB}\) và \(\widehat{BCD}\).'),
  ('Compare triangles \\(ABD\\) and \\(CBD\\).', 'So sánh hai tam giác \\(ABD\\) và \\(CBD\\).'),
  [T(r'\(\triangle ABD=\triangle CBD\) (s.s.s.: \(AB=CB\), \(AD=CD\), \(BD\) common), so \(\widehat{DAB}=\widehat{BCD}\).', r'\(\triangle ABD=\triangle CBD\) (c.c.c: \(AB=CB\), \(AD=CD\), \(BD\) chung) nên \(\widehat{DAB}=\widehat{BCD}\).'),
   T(r'\(\widehat{DAB}+\widehat{BCD}=360^\circ-100^\circ-120^\circ=140^\circ\), so each is \(70^\circ\).', r'\(\widehat{DAB}+\widehat{BCD}=360^\circ-100^\circ-120^\circ=140^\circ\) nên mỗi góc bằng \(70^\circ\).')],
  T(r'\(\widehat{DAB}=\widehat{BCD}=70^\circ\).', r'\(\widehat{DAB}=\widehat{BCD}=70^\circ\).'))

_SETS = sp_g8b.BANK(sp_g8b.L10_GROUPS, start=1, seeds=(8101, 8102, 8103))
practice = LEVEL_PRACTICE(sp_g8b.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Joining consecutive vertices as a diagonal.</b> \(AB\) is a side; diagonals are \(AC\) and \(BD\).', r'<b>Nhầm cạnh với đường chéo.</b> \(AB\) là cạnh; đường chéo là \(AC\) và \(BD\).'),
 (r'<b>Using \(180^\circ\) instead of \(360^\circ\).</b> \(180^\circ\) is for a triangle.', r'<b>Dùng \(180^\circ\) thay cho \(360^\circ\).</b> \(180^\circ\) là tổng ba góc của tam giác.'),
 (r'<b>Naming the quadrilateral out of order.</b> \(ABCD\) means sides \(AB, BC, CD, DA\); \(ACBD\) is a different figure.', r'<b>Gọi tên không theo thứ tự.</b> \(ABCD\) có các cạnh \(AB, BC, CD, DA\); \(ACBD\) là hình khác.'),
 (r'<b>Forgetting to check the answer.</b> After finding \(x\), add the angles to make sure the sum is \(360^\circ\).', r'<b>Quên thử lại.</b> Sau khi tìm \(x\), cộng các góc để kiểm tra tổng bằng \(360^\circ\).')]
summary = [
 (r'Quadrilateral \(ABCD\): 4 vertices, 4 sides, 2 diagonals, 4 angles.', r'Tứ giác \(ABCD\): 4 đỉnh, 4 cạnh, 2 đường chéo, 4 góc.'),
 (r'\(\widehat{A}+\widehat{B}+\widehat{C}+\widehat{D}=360^\circ\).', r'\(\widehat{A}+\widehat{B}+\widehat{C}+\widehat{D}=360^\circ\).'),
 (r'Key English: quadrilateral, convex, vertex, side, diagonal, opposite angles.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[tứ giác|tứ giác (lớp 8)]], [[tứ giác lồi]], [[đỉnh|đỉnh (lớp 8)]], [[cạnh|cạnh (lớp 8)]], [[đường chéo]], [[hai góc đối nhau|hai góc đối nhau (lớp 8)]].')]
checks = [
 (r'I can name the vertices, sides, diagonals and angles of a quadrilateral.', r'Em gọi tên được đỉnh, cạnh, đường chéo, góc của tứ giác.'),
 (r'I can explain why the angles of a quadrilateral add up to \(360^\circ\).', r'Em giải thích được vì sao tổng các góc của tứ giác bằng \(360^\circ\).'),
 (r'I can find unknown angles of a quadrilateral.', r'Em tính được góc chưa biết của tứ giác.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Quadrilaterals', title_vi='Tứ giác', topic=TOPIC,
       folder='quadrilaterals', file='quadrilaterals', catalog_title_vi='Tứ giác',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Quadrilaterals, convex quadrilaterals, angle sum of a quadrilateral.', level='Beginner', minutes=45,
       description_vi='Bài 10 – Tứ giác, tứ giác lồi; đỉnh, cạnh, đường chéo, góc; định lí tổng các góc của tứ giác.',
       tags_vi=['tứ giác', 'tứ giác lồi', 'tổng các góc của tứ giác'],
       prerequisites=[], tags=['quadrilateral', 'convex', 'angle sum'], order=100)
