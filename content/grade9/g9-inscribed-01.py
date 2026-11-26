# -*- coding: utf-8 -*-
"""Nội dung bài g9-inscribed-01 = Toán 9 KNTT, Bài 27: Góc nội tiếp – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 9 – Lesson 27."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9, sp_g9p

LID = 'g9-inscribed-01'
CH = 'Đường tròn ngoại tiếp và đường tròn nội tiếp'
TOPIC = ('Circumcircle and Incircle', CH)
ensure_vocab([
 ('g9-inscribed-angle', 'inscribed angle', 'góc nội tiếp', CH, 'The inscribed angle BAC intercepts the arc BC.', r'\(\widehat{BAC}\)'),
 ('g9-subtend', 'subtend (an arc)', 'chắn (cung)', CH, 'Two inscribed angles that subtend the same arc are equal.', ''),
])
load_vocab()

def FIGC(cap, px=300, **kw):
    fn = sp_g9p.cfig(**kw)
    return '<figure class="mbl-fig mbl-figtex">%s<figcaption>%s</figcaption></figure>' % (sp_g9p.img(fn, cap[0], px), TI(*cap))

# ---------- số liệu (kiểm tra bằng máy) ----------
def ins(P, V, Q):
    """Góc PVQ (độ) với các điểm cho bằng góc cực trên đường tròn đơn vị."""
    p = [(math.cos(math.radians(a)), math.sin(math.radians(a))) for a in (P, V, Q)]
    u = (p[0][0] - p[1][0], p[0][1] - p[1][1]); v = (p[2][0] - p[1][0], p[2][1] - p[1][1])
    return math.degrees(math.acos((u[0] * v[0] + u[1] * v[1]) / math.hypot(*u) / math.hypot(*v)))
assert abs(ins(230, 70, 310) - 40) < 1e-9 and abs(ins(230, 120, 310) - 40) < 1e-9 and abs(ins(230, 20, 310) - 40) < 1e-9
assert abs(ins(180, 110, 0) - 90) < 1e-9 and abs(ins(220, 90, 320) - 50) < 1e-9
assert 90 - 35 == 55 and abs(ins(180, 70, 0) - 90) < 1e-9 and abs(ins(70, 180, 0) - 35) < 1e-9       # Ví dụ 3: C tại 70°
R5 = 8 / math.sqrt(3); assert abs(2 * R5 * math.sin(math.radians(60)) - 8) < 1e-9 and round(R5, 1) == 4.6

F_DEF = FIGC(('\\(\\widehat{BAC}\\) is an inscribed angle; it intercepts the arc \\(BC\\) (orange).', '\\(\\widehat{BAC}\\) là góc nội tiếp; nó chắn cung \\(BC\\) (màu cam).'),
             pts={'A': 120, 'B': 230, 'C': 330}, segs=[('A', 'B'), ('A', 'C')], hl_arc=('B', 'C'), arcs=[('B', 'A', 'C', '')])
F_SAME = FIGC(('\\(\\widehat{ACB}=\\widehat{ADB}=\\widehat{AEB}=40^\\circ\\): the vertex moves on the arc, the angle does not change.', '\\(\\widehat{ACB}=\\widehat{ADB}=\\widehat{AEB}=40^\\circ\\): đỉnh di chuyển trên cung, số đo góc không đổi.'),
              px=330, pts={'A': 230, 'B': 310, 'C': 20, 'D': 70, 'E': 120}, segs=[('C', 'A'), ('C', 'B'), ('D', 'A'), ('D', 'B'), ('E', 'A'), ('E', 'B'), ('O', 'A'), ('O', 'B')],
              arcs=[('A', 'O', 'B', '80^\\circ')], hl_arc=('A', 'B'))
F_SEMI = FIGC(('\\(AB\\) is a diameter: \\(\\widehat{ACB}=90^\\circ\\).', '\\(AB\\) là đường kính: \\(\\widehat{ACB}=90^\\circ\\).'),
              pts={'A': 180, 'B': 0, 'C': 110}, segs=[('A', 'B'), ('C', 'A'), ('C', 'B')], right=[('A', 'C', 'B')])
F_EX2 = FIGC(('Example 2', 'Ví dụ 2'), pts={'A': 220, 'B': 320, 'C': 90}, segs=[('C', 'A'), ('C', 'B'), ('O', 'A'), ('O', 'B')], arcs=[('A', 'O', 'B', '100^\\circ')])
F_EX3 = FIGC(('Example 3', 'Ví dụ 3'), pts={'A': 180, 'B': 0, 'C': 70, 'D': 230}, segs=[('A', 'B'), ('C', 'A'), ('C', 'B'), ('D', 'A'), ('D', 'C')], right=[('A', 'C', 'B')])

# giao điểm M của AB và CD (Ví dụ 4)
def _pt(a, R=1.9): return (R * math.cos(math.radians(a)), R * math.sin(math.radians(a)))
def _inter(P1, P2, P3, P4):
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = P1, P2, P3, P4
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / d
    return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))
MX = _inter(_pt(160), _pt(340), _pt(60), _pt(250))
F_EX4 = FIGC(('Example 4: the chords \\(AB\\) and \\(CD\\) meet at \\(M\\).', 'Ví dụ 4: hai dây \\(AB\\) và \\(CD\\) cắt nhau tại \\(M\\).'), O=False,
             pts={'A': 160, 'B': 340, 'C': 60, 'D': 250}, inner={'M': MX}, segs=[('A', 'B'), ('C', 'D'), ('A', 'C'), ('D', 'B')])
d = lambda P, Q: math.hypot(P[0] - Q[0], P[1] - Q[1])
assert abs(d(MX, _pt(160)) * d(MX, _pt(340)) - d(MX, _pt(60)) * d(MX, _pt(250))) < 1e-9

meta = dict(level=('Basic', 'Cơ bản'), time=('about 90 minutes', '90 phút'), before=('Lesson 14: arcs, central angles', 'Bài 14: cung, góc ở tâm'))
goals = [
 (r'recognize an inscribed angle and the arc it intercepts;', r'nhận biết được góc nội tiếp và cung bị chắn;'),
 (r'know that an inscribed angle is half its intercepted arc, and the corollaries;', r'biết số đo góc nội tiếp bằng nửa số đo cung bị chắn và các hệ quả;'),
 (r'compute angles and prove that two angles are equal;', r'tính được số đo góc, chứng minh được hai góc bằng nhau;'),
 (r'solve multi-step problems and real situations (viewing angles).', r'giải được bài toán nhiều bước và tình huống thực tế (góc nhìn).')]
vocab = [
 (r'<b>inscribed angle</b> – an angle whose vertex is on the circle and whose sides contain two chords.', r'[[Góc nội tiếp]] – góc có đỉnh nằm trên đường tròn và hai cạnh chứa hai dây của đường tròn đó.'),
 (r'<b>intercepted arc</b> – the arc inside the angle (its endpoints are on the sides).', r'[[Cung bị chắn]] – cung nằm bên trong góc (hai đầu mút nằm trên hai cạnh của góc).'),
 (r'<b>subtend</b> – an angle subtends (intercepts) an arc.', r'[[Chắn|chắn (cung)]] – góc chắn một cung.'),
 (r'<b>central angle</b> – an angle with its vertex at the center.', r'[[Góc ở tâm]] – góc có đỉnh trùng với tâm đường tròn.'),
 (r'<b>semicircle</b> – the arc cut off by a diameter (\(180^\circ\)).', r'[[Nửa đường tròn]] – cung bị chia bởi một đường kính (\(180^\circ\)).')]
phrases = [
 (r'<b>\(\widehat{BAC}\) is an inscribed angle subtending the arc \(BC\).</b>', r'\(\widehat{BAC}\) là góc nội tiếp chắn cung \(BC\).'),
 (r'<b>An inscribed angle is half of its intercepted arc.</b>', r'Số đo góc nội tiếp bằng nửa số đo cung bị chắn.'),
 (r'<b>Angles subtended by the same arc are equal.</b>', r'Các góc nội tiếp cùng chắn một cung thì bằng nhau.'),
 (r'<b>The angle in a semicircle is a right angle.</b>', r'Góc nội tiếp chắn nửa đường tròn là góc vuông.'),
 (r'<b>Prove that \(\widehat{MAC}=\widehat{MDB}\).</b>', r'Chứng minh rằng \(\widehat{MAC}=\widehat{MDB}\).')]
review = (T(r'<b>Lesson 14.</b> The minor arc \(AB\) has the same measure as the central angle \(\widehat{AOB}\); the major arc measures \(360^\circ\) minus it. Notation: \(m\overset{\frown}{AB}\).', r'<b>Bài 14.</b> Số đo cung nhỏ \(AB\) bằng số đo góc ở tâm \(\widehat{AOB}\); số đo cung lớn bằng \(360^\circ\) trừ số đo cung nhỏ. Kí hiệu: \(\text{sđ}\,\overset{\frown}{AB}\).') +
          T(r'<b>Triangles.</b> The angles of a triangle add up to \(180^\circ\); in an isosceles triangle the base angles are equal.', r'<b>Tam giác.</b> Tổng ba góc của tam giác bằng \(180^\circ\); tam giác cân có hai góc ở đáy bằng nhau.'))

theory = '<h3>5.1 %s</h3>' % TI('Inscribed angles', 'Góc nội tiếp')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'An <b>inscribed angle</b> is an angle whose vertex lies on the circle and whose two sides contain two chords of the circle. The arc inside the angle is the <b>intercepted arc</b>.',
    r'[[Góc nội tiếp]] là góc có đỉnh nằm trên đường tròn và hai cạnh chứa hai dây cung của đường tròn đó. Cung nằm bên trong góc gọi là [[cung bị chắn]].'))
theory += F_DEF
theory += '<h3>5.2 %s</h3>' % TI('The inscribed angle theorem', 'Định lí về góc nội tiếp')
theory += BOX('mint', ('Theorem', 'Định lí'),
  T(r'The measure of an inscribed angle is <b>half</b> the measure of its intercepted arc.', r'Trong một đường tròn, số đo của góc nội tiếp bằng <b>nửa</b> số đo của cung bị chắn.'),
  M(r'\widehat{BAC}=\tfrac{1}{2}\,m\overset{\frown}{BC}'))
theory += T(r'In the figure below the arc \(AB\) (not containing \(C\), \(D\), \(E\)) measures \(80^\circ\); the three inscribed angles with vertices \(C\), \(D\), \(E\) all measure \(40^\circ\).',
            r'Trong hình dưới, cung \(AB\) (không chứa \(C\), \(D\), \(E\)) có số đo \(80^\circ\); ba góc nội tiếp có đỉnh \(C\), \(D\), \(E\) đều bằng \(40^\circ\).')
theory += F_SAME
theory += '<h3>5.3 %s</h3>' % TI('Corollaries', 'Hệ quả')
theory += BOX('yellow', ('In a circle', 'Trong một đường tròn'),
  OL([T(r'Inscribed angles subtending the same arc (or equal arcs) are equal.', r'Các góc nội tiếp cùng chắn một cung hoặc chắn các cung bằng nhau thì bằng nhau.'),
      T(r'An inscribed angle (at most \(90^\circ\)) is half the central angle subtending the same arc: \(\widehat{ACB}=\tfrac12\widehat{AOB}\).', r'Góc nội tiếp (không quá \(90^\circ\)) có số đo bằng nửa số đo góc ở tâm cùng chắn một cung: \(\widehat{ACB}=\tfrac12\widehat{AOB}\).'),
      T(r'An inscribed angle subtending a semicircle is a right angle.', r'Góc nội tiếp chắn nửa đường tròn là góc vuông.')]))
theory += F_SEMI

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Recognizing inscribed angles', 'Nhận biết góc nội tiếp'),
  T(r'In the figure of 5.2, name three inscribed angles and the arc they intercept. Is \(\widehat{AOB}\) an inscribed angle?', r'Trong hình ở mục 5.2, hãy kể tên ba góc nội tiếp và cung bị chắn bởi chúng. Góc \(\widehat{AOB}\) có phải góc nội tiếp không?'),
  ('Check: is the vertex on the circle? Are the sides chords?', 'Kiểm tra: đỉnh có nằm trên đường tròn không? Hai cạnh có chứa hai dây không?'),
  [T(r'\(\widehat{ACB}\), \(\widehat{ADB}\), \(\widehat{AEB}\): the vertices are on the circle and the sides are chords; they intercept the arc \(AB\).', r'\(\widehat{ACB}\), \(\widehat{ADB}\), \(\widehat{AEB}\): đỉnh nằm trên đường tròn, hai cạnh là dây; chúng cùng chắn cung \(AB\).'),
   T(r'\(\widehat{AOB}\) has its vertex at the center: it is a central angle, not an inscribed angle.', r'\(\widehat{AOB}\) có đỉnh là tâm: đó là góc ở tâm, không phải góc nội tiếp.')],
  T(r'\(\widehat{ACB}\), \(\widehat{ADB}\), \(\widehat{AEB}\) (arc \(AB\)); no.', r'\(\widehat{ACB}\), \(\widehat{ADB}\), \(\widehat{AEB}\) (chắn cung \(AB\)); không.'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Using the theorem', 'Áp dụng định lí'),
  T(r'In the figure, \(\widehat{AOB}=100^\circ\) and \(C\) lies on the major arc \(AB\). Find \(\widehat{ACB}\) and the measure of the major arc \(AB\).', r'Trong hình, \(\widehat{AOB}=100^\circ\) và \(C\) nằm trên cung lớn \(AB\). Tính \(\widehat{ACB}\) và số đo cung lớn \(AB\).') + F_EX2,
  ('The minor arc \\(AB\\) has the same measure as the central angle.', 'Số đo cung nhỏ \\(AB\\) bằng số đo góc ở tâm.'),
  [T(r'\(m\overset{\frown}{AB}=100^\circ\) (minor arc), so \(\widehat{ACB}=\dfrac{100^\circ}{2}=50^\circ\).', r'\(\text{sđ}\,\overset{\frown}{AB}=100^\circ\) (cung nhỏ), nên \(\widehat{ACB}=\dfrac{100^\circ}{2}=50^\circ\).'),
   T(r'Major arc \(AB\): \(360^\circ-100^\circ=260^\circ\).', r'Cung lớn \(AB\): \(360^\circ-100^\circ=260^\circ\).')],
  T(r'\(50^\circ\); \(260^\circ\).', r'\(50^\circ\); \(260^\circ\).'))
examples += EXAMPLE(3, ('Basic application', 'Vận dụng thấp'), ('A diameter', 'Đường kính'),
  T(r'\(AB\) is a diameter of \((O)\); \(C\), \(D\) are points of the circle on different sides of \(AB\); \(\widehat{ABC}=35^\circ\). Find \(\widehat{ACB}\), \(\widehat{BAC}\) and \(\widehat{ADC}\).', r'\(AB\) là đường kính của \((O)\); \(C\), \(D\) là hai điểm của đường tròn nằm khác phía đối với \(AB\); \(\widehat{ABC}=35^\circ\). Tính \(\widehat{ACB}\), \(\widehat{BAC}\) và \(\widehat{ADC}\).') + F_EX3,
  ('\\(\\widehat{ACB}\\) subtends a semicircle; \\(\\widehat{ADC}\\) and \\(\\widehat{ABC}\\) subtend the same arc \\(AC\\).', '\\(\\widehat{ACB}\\) chắn nửa đường tròn; \\(\\widehat{ADC}\\) và \\(\\widehat{ABC}\\) cùng chắn cung \\(AC\\).'),
  [T(r'\(\widehat{ACB}=90^\circ\) (angle in a semicircle).', r'\(\widehat{ACB}=90^\circ\) (góc nội tiếp chắn nửa đường tròn).'),
   T(r'In the right triangle \(ABC\): \(\widehat{BAC}=90^\circ-35^\circ=55^\circ\).', r'Trong tam giác vuông \(ABC\): \(\widehat{BAC}=90^\circ-35^\circ=55^\circ\).'),
   T(r'\(\widehat{ADC}=\widehat{ABC}=35^\circ\) (same arc \(AC\)).', r'\(\widehat{ADC}=\widehat{ABC}=35^\circ\) (cùng chắn cung \(AC\)).')],
  T(r'\(90^\circ\), \(55^\circ\), \(35^\circ\).', r'\(90^\circ\), \(55^\circ\), \(35^\circ\).'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Two chords', 'Hai dây cắt nhau'),
  T(r'The chords \(AB\) and \(CD\) of a circle meet at \(M\). Prove that \(\widehat{MAC}=\widehat{MDB}\) and \(MA\cdot MB=MC\cdot MD\).', r'Hai dây \(AB\) và \(CD\) của một đường tròn cắt nhau tại \(M\). Chứng minh rằng \(\widehat{MAC}=\widehat{MDB}\) và \(MA\cdot MB=MC\cdot MD\).') + F_EX4,
  ('Find two inscribed angles that subtend the same arc, then use similar triangles.', 'Tìm hai góc nội tiếp cùng chắn một cung rồi dùng tam giác đồng dạng.'),
  [T(r'\(\widehat{BAC}\) and \(\widehat{BDC}\) both subtend the arc \(BC\), so \(\widehat{MAC}=\widehat{MDB}\).', r'\(\widehat{BAC}\) và \(\widehat{BDC}\) cùng chắn cung \(BC\) nên \(\widehat{MAC}=\widehat{MDB}\).'),
   T(r'Also \(\widehat{AMC}=\widehat{DMB}\) (vertical angles). Hence \(\triangle MAC\backsim\triangle MDB\) and \(\dfrac{MA}{MD}=\dfrac{MC}{MB}\), that is \(MA\cdot MB=MC\cdot MD\).', r'Lại có \(\widehat{AMC}=\widehat{DMB}\) (đối đỉnh). Do đó \(\triangle MAC\backsim\triangle MDB\), suy ra \(\dfrac{MA}{MD}=\dfrac{MC}{MB}\), tức là \(MA\cdot MB=MC\cdot MD\).')],
  T(r'Proved.', r'Đã chứng minh.'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Placing a camera', 'Đặt máy quay'),
  T(r'The front edge \(AB=8\) m of a stage is a chord of a circle \((O)\) with \(\widehat{AOB}=120^\circ\). A camera must see \(AB\) under an angle of \(60^\circ\). (a) Where on the audience side can it be placed? (b) Find the radius of the circle (to one decimal place).',
    r'Mép sân khấu \(AB=8\) m là một dây của đường tròn \((O)\) với \(\widehat{AOB}=120^\circ\). Máy quay cần nhìn \(AB\) dưới góc \(60^\circ\). a) Có thể đặt máy quay ở đâu (phía khán giả)? b) Tính bán kính đường tròn (làm tròn đến hàng phần mười).'),
  ('Every inscribed angle on the major arc \\(AB\\) is half of \\(120^\\circ\\).', 'Mọi góc nội tiếp có đỉnh trên cung lớn \\(AB\\) đều bằng nửa của \\(120^\\circ\\).'),
  [T(r'(a) At any point \(C\) of the major arc \(AB\): \(\widehat{ACB}=\dfrac{120^\circ}{2}=60^\circ\).', r'a) Tại bất kì điểm \(C\) nào trên cung lớn \(AB\): \(\widehat{ACB}=\dfrac{120^\circ}{2}=60^\circ\).'),
   T(r'(b) Let \(H\) be the midpoint of \(AB\): \(OH\perp AB\), \(\widehat{AOH}=60^\circ\), \(AH=4\) m. So \(R=OA=\dfrac{AH}{\sin60^\circ}=\dfrac{8}{\sqrt3}\approx4.6\) m.', r'b) Gọi \(H\) là trung điểm \(AB\): \(OH\perp AB\), \(\widehat{AOH}=60^\circ\), \(AH=4\) m. Do đó \(R=OA=\dfrac{AH}{\sin60^\circ}=\dfrac{8}{\sqrt3}\approx4{,}6\) m.')],
  T(r'(a) On the major arc \(AB\); (b) about 4.6 m.', r'a) Trên cung lớn \(AB\); b) khoảng 4,6 m.'))

_SETS = sp_g9.BANK(sp_g9p.L27_GROUPS, start=1, seeds=(2701, 2702, 2703))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Calling a central angle “inscribed”.</b> The vertex of an inscribed angle is on the circle, not at the center.', r'<b>Nhầm góc ở tâm là góc nội tiếp.</b> Đỉnh của góc nội tiếp nằm trên đường tròn, không phải ở tâm.'),
 (r'<b>Doubling instead of halving.</b> Inscribed angle \(=\tfrac12\) arc; arc \(=2\cdot\) inscribed angle.', r'<b>Nhân đôi thay vì chia đôi.</b> Góc nội tiếp \(=\tfrac12\) số đo cung; số đo cung \(=2\cdot\) góc nội tiếp.'),
 (r'<b>Using the wrong arc.</b> If the vertex is on the minor arc \(AB\), the angle intercepts the major arc.', r'<b>Dùng nhầm cung.</b> Nếu đỉnh nằm trên cung nhỏ \(AB\) thì góc chắn cung lớn \(AB\).'),
 (r'<b>Forgetting the right angle.</b> If \(AB\) is a diameter, every \(\widehat{ACB}\) is \(90^\circ\).', r'<b>Quên góc vuông.</b> Nếu \(AB\) là đường kính thì mọi góc \(\widehat{ACB}\) đều bằng \(90^\circ\).')]
summary = [
 (r'Inscribed angle: vertex on the circle, sides containing two chords; it intercepts the arc inside it.', r'Góc nội tiếp: đỉnh nằm trên đường tròn, hai cạnh chứa hai dây; nó chắn cung nằm bên trong góc.'),
 (r'Inscribed angle \(=\tfrac12\) intercepted arc.', r'Số đo góc nội tiếp bằng nửa số đo cung bị chắn.'),
 (r'Same arc ⇒ equal angles; inscribed angle \(=\tfrac12\) central angle; angle in a semicircle \(=90^\circ\).', r'Cùng chắn một cung ⇒ bằng nhau; góc nội tiếp \(=\tfrac12\) góc ở tâm cùng chắn cung; góc nội tiếp chắn nửa đường tròn là góc vuông.'),
 (r'Key English: inscribed angle, intercepted arc, subtend, central angle, semicircle.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[góc nội tiếp]], [[cung bị chắn]], [[chắn|chắn (cung)]], [[góc ở tâm]], [[nửa đường tròn]].')]
checks = [
 (r'I can recognize inscribed angles and their intercepted arcs.', r'Em nhận biết được góc nội tiếp và cung bị chắn.'),
 (r'I can find an inscribed angle from its arc or from the central angle.', r'Em tính được góc nội tiếp từ số đo cung hoặc góc ở tâm.'),
 (r'I can use the corollaries to compute angles and prove equal angles.', r'Em dùng được các hệ quả để tính góc và chứng minh hai góc bằng nhau.'),
 (r'I can solve viewing-angle problems.', r'Em giải được bài toán về góc nhìn.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Inscribed Angles', title_vi='Góc nội tiếp', topic=TOPIC,
       folder='circumcircle-incircle', file='inscribed-angles', catalog_title_vi='Góc nội tiếp',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Inscribed angles and intercepted arcs; the inscribed angle theorem and its corollaries; angle in a semicircle; viewing angles.', level='Basic', minutes=90,
       description_vi='Bài 27 – Góc nội tiếp, cung bị chắn; số đo góc nội tiếp bằng nửa số đo cung bị chắn; các hệ quả; góc nội tiếp chắn nửa đường tròn.',
       tags_vi=['góc nội tiếp', 'cung bị chắn', 'đường tròn'], prerequisites=['g9-circles-02'], tags=['inscribed angle', 'intercepted arc', 'circle'], order=270)
