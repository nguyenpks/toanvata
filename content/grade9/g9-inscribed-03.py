# -*- coding: utf-8 -*-
"""Nội dung bài g9-inscribed-03 = Toán 9 KNTT, Bài 29: Tứ giác nội tiếp – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 9 – Lesson 29; Mini project Ch.9 (Smart Circular Theater & Garden)."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9, sp_g9p, sp_g9q as Q

LID = 'g9-inscribed-03'
CH = 'Đường tròn ngoại tiếp và đường tròn nội tiếp'
TOPIC = ('Circumcircle and Incircle', CH)
ensure_vocab([
 ('g9-cyclic-quad', 'cyclic quadrilateral', 'tứ giác nội tiếp (đường tròn)', CH, 'ABCD is a cyclic quadrilateral: its four vertices lie on a circle.', ''),
 ('g9-opposite-angles', 'opposite angles', 'hai góc đối (của tứ giác)', CH, 'The opposite angles of a cyclic quadrilateral are supplementary.', ''),
])
load_vocab()

def FIGC(cap, px=300, **kw):
    fn = sp_g9p.cfig(**kw); return '<figure class="mbl-fig mbl-figtex">%s<figcaption>%s</figcaption></figure>' % (sp_g9p.img(fn, cap[0], px), TI(*cap))
def ang(P, V, Q_):
    p = [(math.cos(math.radians(a)), math.sin(math.radians(a))) for a in (P, V, Q_)]
    u = (p[0][0] - p[1][0], p[0][1] - p[1][1]); v = (p[2][0] - p[1][0], p[2][1] - p[1][1])
    return math.degrees(math.acos((u[0] * v[0] + u[1] * v[1]) / math.hypot(*u) / math.hypot(*v)))

# ---------- số liệu (kiểm tra bằng máy) ----------
QA, QB, QC, QD = 110, 215, 300, 30
assert abs(ang(QD, QA, QB) + ang(QB, QC, QD) - 180) < 1e-9 and abs(ang(QA, QB, QC) + ang(QC, QD, QA) - 180) < 1e-9
F_DEF = FIGC(('\\(ABCD\\) is inscribed in \\((O)\\): \\(\\widehat{A}+\\widehat{C}=\\widehat{B}+\\widehat{D}=180^\\circ\\).', '\\(ABCD\\) nội tiếp \\((O)\\): \\(\\widehat{A}+\\widehat{C}=\\widehat{B}+\\widehat{D}=180^\\circ\\).'),
             pts={'A': QA, 'B': QB, 'C': QC, 'D': QD}, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')], arcs=[('D', 'A', 'B', ''), ('B', 'C', 'D', '')])
F_RECT = FIGC(('Rectangle \\(ABCD\\): the center is the intersection of the diagonals.', 'Hình chữ nhật \\(ABCD\\): tâm là giao điểm hai đường chéo.'),
              pts={'A': 143.13, 'B': 216.87, 'C': 323.13, 'D': 36.87}, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')], dash=[('A', 'C'), ('B', 'D')])
assert abs(ang(36.87, 143.13, 216.87) - 90) < 1e-3
assert 105 + 75 == 180 and 180 - 105 == 75 and 6 ** 2 + 8 ** 2 == 100 and 180 - (40 + 35) == 105

meta = dict(level=('Basic', 'Cơ bản'), time=('about 90 minutes', '90 phút'), before=('Lesson 27: inscribed angles', 'Bài 27: góc nội tiếp'))
goals = [
 (r'recognize a cyclic quadrilateral;', r'nhận biết được tứ giác nội tiếp;'),
 (r'know that the opposite angles of a cyclic quadrilateral add up to \(180^\circ\) (and the converse);', r'biết trong tứ giác nội tiếp tổng hai góc đối bằng \(180^\circ\) (và điều ngược lại);'),
 (r'find the circumcenter and circumradius of a rectangle and a square;', r'xác định được tâm, bán kính đường tròn ngoại tiếp hình chữ nhật, hình vuông;'),
 (r'compute angles and prove that a quadrilateral is cyclic.', r'tính được góc và chứng minh được một tứ giác là tứ giác nội tiếp.')]
vocab = [
 (r'<b>cyclic quadrilateral</b> – a quadrilateral whose four vertices lie on a circle.', r'[[Tứ giác nội tiếp|tứ giác nội tiếp (đường tròn)]] – tứ giác có bốn đỉnh cùng nằm trên một đường tròn.'),
 (r'<b>opposite angles</b> – two angles of a quadrilateral that are not next to each other (\(\widehat{A}\) and \(\widehat{C}\)).', r'[[Hai góc đối|hai góc đối (của tứ giác)]] – hai góc không kề nhau của tứ giác (\(\widehat{A}\) và \(\widehat{C}\)).'),
 (r'<b>supplementary angles</b> – two angles adding up to \(180^\circ\).', r'[[Hai góc bù nhau]] – hai góc có tổng bằng \(180^\circ\).'),
 (r'<b>circumcircle / circumradius</b> – the circle through the four vertices; its radius.', r'[[Đường tròn ngoại tiếp|đường tròn ngoại tiếp (tam giác, đa giác)]] tứ giác – đường tròn đi qua bốn đỉnh; bán kính của nó.'),
 (r'<b>converse</b> – the theorem with the condition and the conclusion swapped.', r'Định lí đảo – định lí có giả thiết và kết luận đổi chỗ cho nhau.')]
phrases = [
 (r'<b>\(ABCD\) is a cyclic quadrilateral.</b>', r'\(ABCD\) là tứ giác nội tiếp.'),
 (r'<b>The opposite angles are supplementary.</b>', r'Hai góc đối bù nhau.'),
 (r'<b>Prove that \(ABCD\) is cyclic.</b>', r'Chứng minh rằng \(ABCD\) là tứ giác nội tiếp.'),
 (r'<b>Every rectangle can be inscribed in a circle.</b>', r'Mọi hình chữ nhật đều nội tiếp được đường tròn.'),
 (r'<b>The center is the intersection of the diagonals.</b>', r'Tâm là giao điểm của hai đường chéo.')]
review = (T(r'<b>Lesson 27.</b> An inscribed angle is half its intercepted arc; the two arcs cut off by two points add up to \(360^\circ\).', r'<b>Bài 27.</b> Số đo góc nội tiếp bằng nửa số đo cung bị chắn; hai cung có chung hai mút có tổng số đo \(360^\circ\).') +
          T(r'<b>Grade 8.</b> The angles of a quadrilateral add up to \(360^\circ\).', r'<b>Lớp 8.</b> Tổng các góc của một tứ giác bằng \(360^\circ\).'))

theory = '<h3>5.1 %s</h3>' % TI('Cyclic quadrilaterals', 'Tứ giác nội tiếp')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'A quadrilateral whose four vertices lie on a circle is called a <b>cyclic quadrilateral</b> (inscribed in the circle).', r'Tứ giác có bốn đỉnh nằm trên một đường tròn được gọi là [[tứ giác nội tiếp|tứ giác nội tiếp (đường tròn)]] đường tròn (gọi tắt là tứ giác nội tiếp).'))
theory += F_DEF
theory += BOX('mint', ('Theorem', 'Định lí'),
  T(r'In a cyclic quadrilateral, the sum of two opposite angles is \(180^\circ\): \(\widehat{A}+\widehat{C}=\widehat{B}+\widehat{D}=180^\circ\).', r'Trong một tứ giác nội tiếp, tổng số đo hai góc đối bằng \(180^\circ\): \(\widehat{A}+\widehat{C}=\widehat{B}+\widehat{D}=180^\circ\).'),
  T(r'<i>Reason:</i> \(\widehat{A}\) and \(\widehat{C}\) intercept the two arcs \(BD\), whose measures add up to \(360^\circ\); so \(\widehat{A}+\widehat{C}=\dfrac{360^\circ}{2}=180^\circ\).', r'<i>Giải thích:</i> \(\widehat{A}\) và \(\widehat{C}\) chắn hai cung \(BD\) có tổng số đo \(360^\circ\) nên \(\widehat{A}+\widehat{C}=\dfrac{360^\circ}{2}=180^\circ\).'))
theory += BOX('yellow', ('Converse', 'Định lí đảo'),
  T(r'If a quadrilateral has two opposite angles adding up to \(180^\circ\), then it is cyclic.', r'Nếu một tứ giác có tổng số đo hai góc đối bằng \(180^\circ\) thì tứ giác đó nội tiếp được đường tròn.'))
theory += '<h3>5.2 %s</h3>' % TI('Rectangles and squares', 'Hình chữ nhật, hình vuông')
theory += BOX('mint', ('Circumcircle', 'Đường tròn ngoại tiếp'),
  UL([T(r'Every rectangle (and every square) is cyclic: its angles are \(90^\circ\), so opposite angles add up to \(180^\circ\).', r'Mọi hình chữ nhật (và hình vuông) đều nội tiếp được đường tròn: các góc bằng \(90^\circ\) nên tổng hai góc đối bằng \(180^\circ\).'),
      T(r'The center is the intersection of the diagonals; the radius is half a diagonal: \(R=\dfrac{\sqrt{a^2+b^2}}{2}\).', r'Tâm là giao điểm hai đường chéo; bán kính bằng nửa đường chéo: \(R=\dfrac{\sqrt{a^2+b^2}}{2}\).'),
      T(r'A square with side \(a\): \(R=\dfrac{a\sqrt2}{2}\).', r'Hình vuông cạnh \(a\): \(R=\dfrac{a\sqrt2}{2}\).')]))
theory += F_RECT

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Is it cyclic?', 'Có nội tiếp không?'),
  T(r'Which of these are cyclic quadrilaterals? (a) a square; (b) a rhombus with angles \(60^\circ\) and \(120^\circ\); (c) a quadrilateral with \(\widehat{A}=70^\circ\), \(\widehat{C}=110^\circ\).', r'Tứ giác nào sau đây nội tiếp được đường tròn? a) hình vuông; b) hình thoi có các góc \(60^\circ\) và \(120^\circ\); c) tứ giác có \(\widehat{A}=70^\circ\), \(\widehat{C}=110^\circ\).'),
  ('Check the sum of two opposite angles.', 'Kiểm tra tổng hai góc đối.'),
  [T(r'(a) Yes: \(90^\circ+90^\circ=180^\circ\). (b) No: opposite angles are equal, \(60^\circ+60^\circ\ne180^\circ\). (c) Yes: \(70^\circ+110^\circ=180^\circ\).', r'a) Có: \(90^\circ+90^\circ=180^\circ\). b) Không: hai góc đối bằng nhau, \(60^\circ+60^\circ\ne180^\circ\). c) Có: \(70^\circ+110^\circ=180^\circ\).')],
  T(r'(a) and (c).', r'a) và c).'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Finding angles', 'Tính góc'),
  T(r'\(ABCD\) is a cyclic quadrilateral with \(\widehat{A}=105^\circ\), \(\widehat{B}=80^\circ\). Find \(\widehat{C}\) and \(\widehat{D}\).', r'Tứ giác nội tiếp \(ABCD\) có \(\widehat{A}=105^\circ\), \(\widehat{B}=80^\circ\). Tính \(\widehat{C}\) và \(\widehat{D}\).'),
  ('Use \\(\\widehat{A}+\\widehat{C}=\\widehat{B}+\\widehat{D}=180^\\circ\\).', 'Dùng \\(\\widehat{A}+\\widehat{C}=\\widehat{B}+\\widehat{D}=180^\\circ\\).'),
  [T(r'\(\widehat{C}=180^\circ-105^\circ=75^\circ\); \(\widehat{D}=180^\circ-80^\circ=100^\circ\).', r'\(\widehat{C}=180^\circ-105^\circ=75^\circ\); \(\widehat{D}=180^\circ-80^\circ=100^\circ\).')],
  T(r'\(75^\circ\), \(100^\circ\).', r'\(75^\circ\), \(100^\circ\).'))
examples += EXAMPLE(3, ('Basic application', 'Vận dụng thấp'), ('A rectangle', 'Hình chữ nhật'),
  T(r'A rectangle \(ABCD\) has \(AB=8\) cm and \(BC=6\) cm. Find the center and the radius of its circumcircle, and the area of the disk.', r'Hình chữ nhật \(ABCD\) có \(AB=8\) cm, \(BC=6\) cm. Xác định tâm, tính bán kính đường tròn ngoại tiếp và diện tích hình tròn đó.'),
  ('The diagonal is a diameter.', 'Đường chéo là đường kính.'),
  [T(r'\(AC=\sqrt{8^2+6^2}=10\) cm; the center is the intersection \(O\) of \(AC\) and \(BD\); \(R=5\) cm.', r'\(AC=\sqrt{8^2+6^2}=10\) cm; tâm là giao điểm \(O\) của \(AC\) và \(BD\); \(R=5\) cm.'),
   T(r'\(S=\pi\cdot5^2=25\pi\approx78.5\) cm².', r'\(S=\pi\cdot5^2=25\pi\approx78{,}5\) cm².')],
  T(r'\(R=5\) cm; \(25\pi\) cm².', r'\(R=5\) cm; \(25\pi\) cm².'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Using inscribed angles', 'Dùng góc nội tiếp'),
  T(r'In the cyclic quadrilateral \(ABCD\), \(\widehat{ABD}=40^\circ\), \(\widehat{ADB}=35^\circ\). Find \(\widehat{BAD}\) and \(\widehat{BCD}\).', r'Trong tứ giác nội tiếp \(ABCD\), \(\widehat{ABD}=40^\circ\), \(\widehat{ADB}=35^\circ\). Tính \(\widehat{BAD}\) và \(\widehat{BCD}\).'),
  ('Triangle \\(ABD\\) first, then opposite angles.', 'Xét tam giác \\(ABD\\) trước, sau đó dùng tổng hai góc đối.'),
  [T(r'\(\widehat{BAD}=180^\circ-40^\circ-35^\circ=105^\circ\).', r'\(\widehat{BAD}=180^\circ-40^\circ-35^\circ=105^\circ\).'), T(r'\(\widehat{BCD}=180^\circ-105^\circ=75^\circ\).', r'\(\widehat{BCD}=180^\circ-105^\circ=75^\circ\).')],
  T(r'\(105^\circ\), \(75^\circ\).', r'\(105^\circ\), \(75^\circ\).'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Proving a quadrilateral is cyclic', 'Chứng minh tứ giác nội tiếp'),
  T(r'Triangle \(ABC\) has the altitudes \(BE\) and \(CF\) (\(E\in AC\), \(F\in AB\)) meeting at \(H\). Prove that \(AEHF\) is a cyclic quadrilateral and find the center of its circumcircle. (In the theater-garden project, this idea helps to place four lamps on one circular path.)',
    r'Tam giác \(ABC\) có hai đường cao \(BE\) và \(CF\) (\(E\in AC\), \(F\in AB\)) cắt nhau tại \(H\). Chứng minh \(AEHF\) là tứ giác nội tiếp và xác định tâm đường tròn ngoại tiếp tứ giác đó. (Trong dự án sân khấu – vườn tròn, ý này giúp đặt bốn đèn trên cùng một lối đi hình tròn.)'),
  ('Look at the angles at \\(E\\) and \\(F\\).', 'Xét các góc tại \\(E\\) và \\(F\\).'),
  [T(r'\(\widehat{AEH}=90^\circ\), \(\widehat{AFH}=90^\circ\), so \(\widehat{AEH}+\widehat{AFH}=180^\circ\): \(AEHF\) is cyclic.', r'\(\widehat{AEH}=90^\circ\), \(\widehat{AFH}=90^\circ\) nên \(\widehat{AEH}+\widehat{AFH}=180^\circ\): \(AEHF\) là tứ giác nội tiếp.'),
   T(r'\(E\) and \(F\) see \(AH\) under right angles, so \(AH\) is a diameter: the center is the midpoint of \(AH\).', r'\(E\), \(F\) nhìn \(AH\) dưới góc vuông nên \(AH\) là đường kính: tâm là trung điểm của \(AH\).')],
  T(r'Cyclic; center = midpoint of \(AH\).', r'Nội tiếp; tâm là trung điểm \(AH\).'))

_SETS = sp_g9.BANK(Q.L29_GROUPS, start=1, seeds=(2901, 2902, 2903))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Adding two neighboring angles.</b> Only OPPOSITE angles add up to \(180^\circ\).', r'<b>Cộng hai góc kề nhau.</b> Chỉ hai góc ĐỐI mới có tổng \(180^\circ\).'),
 (r'<b>Thinking every parallelogram is cyclic.</b> Only rectangles (and squares) among parallelograms are cyclic.', r'<b>Nghĩ mọi hình bình hành đều nội tiếp.</b> Trong các hình bình hành, chỉ hình chữ nhật (và hình vuông) nội tiếp được.'),
 (r'<b>Taking \(R\) equal to the diagonal.</b> \(R\) is half the diagonal.', r'<b>Lấy \(R\) bằng đường chéo.</b> \(R\) bằng nửa đường chéo.'),
 (r'<b>Checking only one pair.</b> To use the converse, one pair of opposite angles adding to \(180^\circ\) is enough; but you must show it.', r'<b>Không chứng minh.</b> Dùng định lí đảo cần chỉ ra một cặp góc đối có tổng \(180^\circ\).')]
summary = [
 (r'Cyclic quadrilateral: four vertices on one circle.', r'Tứ giác nội tiếp: bốn đỉnh cùng nằm trên một đường tròn.'),
 (r'Cyclic ⇔ a pair of opposite angles adds up to \(180^\circ\).', r'Tứ giác nội tiếp ⇔ có một cặp góc đối có tổng \(180^\circ\).'),
 (r'Rectangle: center = intersection of the diagonals, \(R=\dfrac{\text{diagonal}}{2}\); square: \(R=\dfrac{a\sqrt2}{2}\).', r'Hình chữ nhật: tâm là giao điểm hai đường chéo, \(R=\dfrac{\text{đường chéo}}{2}\); hình vuông: \(R=\dfrac{a\sqrt2}{2}\).'),
 (r'Key English: cyclic quadrilateral, opposite angles, supplementary angles, circumcircle, converse.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[tứ giác nội tiếp|tứ giác nội tiếp (đường tròn)]], [[hai góc đối|hai góc đối (của tứ giác)]], [[hai góc bù nhau]], [[đường tròn ngoại tiếp|đường tròn ngoại tiếp (tam giác, đa giác)]].')]
checks = [
 (r'I can recognize cyclic quadrilaterals.', r'Em nhận biết được tứ giác nội tiếp.'),
 (r'I can use the sum of opposite angles to find angles.', r'Em dùng được tính chất tổng hai góc đối để tính góc.'),
 (r'I can find the circumradius of a rectangle and a square.', r'Em tính được bán kính đường tròn ngoại tiếp hình chữ nhật, hình vuông.'),
 (r'I can prove that a quadrilateral is cyclic.', r'Em chứng minh được một tứ giác là tứ giác nội tiếp.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Cyclic Quadrilaterals', title_vi='Tứ giác nội tiếp', topic=TOPIC,
       folder='circumcircle-incircle', file='cyclic-quadrilaterals', catalog_title_vi='Tứ giác nội tiếp',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Cyclic quadrilaterals; opposite angles are supplementary (and the converse); circumcircles of rectangles and squares.', level='Basic', minutes=90,
       description_vi='Bài 29 – Tứ giác nội tiếp; tổng hai góc đối bằng 180° và định lí đảo; đường tròn ngoại tiếp hình chữ nhật, hình vuông.',
       tags_vi=['tứ giác nội tiếp', 'góc đối', 'hình chữ nhật'], prerequisites=['g9-inscribed-02'], tags=['cyclic quadrilateral', 'opposite angles', 'rectangle'], order=290)
