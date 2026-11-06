# -*- coding: utf-8 -*-
"""Nội dung bài g11-space-03 (Quan hệ vuông góc) – CHỈ NỘI DUNG."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *

LID = 'g11-space-03'
CAT = 'Lines and Planes in Space'
TOPIC = (CAT, 'Đường thẳng và mặt phẳng trong không gian')
CV = 'Hình học không gian'

ensure_vocab([
 ('g11-perpendicular', 'perpendicular', 'vuông góc', CV, 'The line is perpendicular to the plane.', r'\(a\perp b\)'),
 ('g11-foot', 'foot of the perpendicular', 'chân đường vuông góc', CV, 'H is the foot of the perpendicular from P.', ''),
 ('g11-projection', 'projection', 'hình chiếu', CV, 'The projection of S on the base is A.', ''),
 ('g11-angle-line-plane', 'angle between a line and a plane', 'góc giữa đường thẳng và mặt phẳng', CV, 'Find the angle between the line and the plane.', ''),
 ('g11-perp-planes', 'perpendicular planes', 'hai mặt phẳng vuông góc', CV, 'The two planes are perpendicular.', ''),
 ('g11-diagonal', 'diagonal', 'đường chéo', CV, 'The diagonals of a square are perpendicular.', ''),
 ('g11-tangent-circle', 'tangent to a circle', 'tiếp tuyến của đường tròn', CV, 'A tangent is perpendicular to the radius.', ''),
 ('g11-height', 'height', 'chiều cao', CV, 'SA is the height of the pyramid.', ''),
])
load_vocab()

# ---- kiểm tra bằng vectơ: chóp S.ABCD, đáy hình vuông, SA ⊥ đáy ----
def dot(u, v): return sum(a * b for a, b in zip(u, v))
def sub(p, q): return tuple(a - b for a, b in zip(p, q))
a, h = 2, 2.0
pA, pB, pC, pD, pS = (0, 0, 0), (a, 0, 0), (a, a, 0), (0, a, 0), (0, 0, h)
assert dot(sub(pS, pA), sub(pB, pA)) == 0 and dot(sub(pS, pA), sub(pD, pA)) == 0           # SA ⊥ AB, AD
assert dot(sub(pC, pB), sub(pB, pA)) == 0 and dot(sub(pC, pB), sub(pS, pA)) == 0           # BC ⊥ (SAB)
assert dot(sub(pC, pD), sub(pD, pA)) == 0 and dot(sub(pC, pD), sub(pS, pA)) == 0           # CD ⊥ (SAD)
assert dot(sub(pD, pB), sub(pC, pA)) == 0 and dot(sub(pD, pB), sub(pS, pA)) == 0           # BD ⊥ (SAC)
assert dot(sub(pC, pA), sub(pS, pB)) != 0 and dot(sub(pD, pB), sub(pS, pC)) == 0           # AC không ⊥ SB ; SC ⊥ BD
assert abs(math.degrees(math.atan(h / (a * math.sqrt(2)))) - 35.2644) < 1e-3                # góc giữa SC và đáy
assert 3 ** 2 + 4 ** 2 == 5 ** 2 and 5 ** 2 + 12 ** 2 == 13 ** 2 and 8 ** 2 + 6 ** 2 == 10 ** 2
assert 1 ** 2 + 2 * 1 ** 2 == 3 and 1 ** 2 + 2 * 2 ** 2 == 9 and 2 ** 2 + 2 * 1 ** 2 == 6

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 60 minutes', 'khoảng 60 phút'),
            before=('parallel lines and planes (previous lesson), the Pythagorean theorem, tangent of an angle', 'đường thẳng và mặt phẳng song song (bài trước), định lí Pythagore, tang của góc'))
goals = [
 ('build perpendicular lines, altitudes and tangents in the plane;', 'dựng đường [[vuông góc]], đường cao và tiếp tuyến trong mặt phẳng;'),
 ('prove that a line is perpendicular to a plane;', 'chứng minh đường thẳng vuông góc với mặt phẳng;'),
 ('find the angle between a line and a plane;', 'tìm [[góc giữa đường thẳng và mặt phẳng]];'),
 ('prove that two planes are perpendicular.', 'chứng minh [[hai mặt phẳng vuông góc]].'),
]
vocab = [
 (r'<b>perpendicular</b> – meeting at a right angle: \(a\perp b\).', r'[[Vuông góc]] – gặp nhau tạo góc vuông: \(a\perp b\).'),
 ('<b>foot of the perpendicular</b> – the point where a perpendicular meets the line or the plane.', '[[Chân đường vuông góc]] – điểm mà đường vuông góc gặp đường thẳng hoặc mặt phẳng.'),
 ('<b>projection</b> – the shadow of a point or a line on a plane, along a perpendicular.', '[[Hình chiếu]] – “bóng” của điểm hoặc đường thẳng trên mặt phẳng, theo phương vuông góc.'),
 ('<b>angle between a line and a plane</b> – the angle between the line and its projection on the plane.', '[[Góc giữa đường thẳng và mặt phẳng]] – góc giữa đường thẳng và hình chiếu của nó trên mặt phẳng.'),
 ('<b>perpendicular planes</b> – two planes that make a right angle.', '[[Hai mặt phẳng vuông góc]] – hai mặt phẳng tạo thành góc vuông.'),
 ('<b>diagonal</b> – a segment joining two vertices that are not neighbours.', '[[Đường chéo]] – đoạn nối hai đỉnh không kề nhau.'),
 ('<b>tangent to a circle</b> – a line that touches the circle at exactly one point.', '[[Tiếp tuyến của đường tròn]] – đường thẳng chỉ có một điểm chung với đường tròn.'),
 ('<b>height</b> – the distance from the apex to the base.', '[[Chiều cao]] – khoảng cách từ đỉnh đến mặt đáy.'),
]
phrases = [
 ('<b>Prove that \\(BC\\) is perpendicular to the plane \\((SAB)\\).</b>', 'Chứng minh \\(BC\\) vuông góc với mặt phẳng \\((SAB)\\).'),
 ('<b>Find the angle between \\(SC\\) and the base.</b>', 'Tìm góc giữa \\(SC\\) và mặt đáy.'),
 ('<b>\\(SA\\) is perpendicular to the base.</b>', '\\(SA\\) vuông góc với mặt đáy.'),
 ('<b>The base is a square of side \\(a\\).</b>', 'Đáy là hình vuông cạnh \\(a\\).'),
 ('<b>Prove that the two planes are perpendicular.</b>', 'Chứng minh hai mặt phẳng vuông góc.'),
 ('<b>Draw the altitude from \\(C\\).</b>', 'Vẽ đường cao hạ từ \\(C\\).'),
]
review = (
 T(r'<b>Perpendicular in the plane.</b> From a point \(P\) not on a line \(AB\) there is exactly one perpendicular to \(AB\). Its foot is \(H\). The segment \(PH\) is the shortest segment from \(P\) to the line.', r'<b>Vuông góc trong mặt phẳng.</b> Từ điểm \(P\) không thuộc đường thẳng \(AB\) có đúng một đường vuông góc với \(AB\); chân của nó là \(H\). Đoạn \(PH\) là đoạn ngắn nhất từ \(P\) đến đường thẳng.') +
  GEO({'view': [-6, 6, -3, 5], 'steps': [
      {'type': 'point', 'id': 'A', 'at': [-4, 0]}, {'type': 'point', 'id': 'B', 'at': [4, 0]}, {'type': 'line', 'id': 'AB', 'through': ['A', 'B']},
      {'type': 'point', 'id': 'P', 'at': [1, 3.5]}, {'type': 'perpendicular', 'from': 'P', 'to': 'AB', 'foot': 'H', 'footName': 'H'},
      {'type': 'angle', 'points': ['B', 'H', 'P'], 'radius': 0.6}]},
      cap=('H is the foot of the perpendicular from P to AB; the square marks the right angle.', 'H là chân đường vuông góc hạ từ P xuống AB; ô vuông nhỏ kí hiệu góc vuông.'), alt=('A perpendicular from a point to a line', ''), height=320) +
 T(r'<b>Tangent to a circle.</b> The tangent at a point \(T\) of a circle with centre \(O\) is the line through \(T\) perpendicular to the radius \(OT\).', r'<b>Tiếp tuyến của đường tròn.</b> Tiếp tuyến tại điểm \(T\) của đường tròn tâm \(O\) là đường thẳng qua \(T\) vuông góc với bán kính \(OT\).') +
  GEO({'view': [-6, 6, -4, 5], 'steps': [
      {'type': 'point', 'id': 'O', 'at': [-1, 0]}, {'type': 'point', 'id': 'R', 'at': [2, 0]}, {'type': 'circle', 'id': 'c', 'center': 'O', 'through': 'R'},
      {'type': 'glider', 'id': 'T', 'at': [-1, 3], 'on': 'c'}, {'type': 'tangent', 'center': 'O', 'at': 'T', 'showRadius': True}]},
      cap=('The tangent is the perpendicular to OT at T.', 'Tiếp tuyến là đường vuông góc với OT tại T.'), alt=('A circle with a tangent line', ''), height=320))

PYR = {'solid': True, 'box': [[-3, 3], [-3, 3], [-1, 4]], 'points': {'A': (-2, -2, 0), 'B': (2, -2, 0), 'C': (2, 2, 0), 'D': (-2, 2, 0), 'S': (-2, -2, 3.5)},
       'polygons': [['A', 'B', 'C', 'D']]}
def pyr(hl=None):
    segs = {('S', 'A'): [], ('S', 'B'): [], ('S', 'C'): [], ('S', 'D'): [], ('A', 'C'): [{'dash': True, 'color': '#64748b', 'width': 1.6}], ('B', 'D'): [{'dash': True, 'color': '#64748b', 'width': 1.6}]}
    out = []
    for k, v in segs.items():
        opts = (hl or {}).get(k) or (v[0] if v else None)
        out.append([k[0], k[1]] + ([opts] if opts else []))
    c = dict(PYR); c['segments'] = out; return c

theory = '<h3>5.1 %s</h3>' % TI('A line perpendicular to a plane', 'Đường thẳng vuông góc với mặt phẳng')
theory += BOX('mint', ('Theorem', 'Định lí'),
  T(r'If a line is perpendicular to two <b>intersecting</b> lines of a plane, it is perpendicular to the plane (and so to every line of the plane).', r'Nếu một đường thẳng vuông góc với hai đường thẳng <b>cắt nhau</b> của một mặt phẳng thì nó vuông góc với mặt phẳng đó (và với mọi đường thẳng nằm trong mặt phẳng).'))
theory += GEO3D(pyr({('S', 'A'): {'color': '#c2410c', 'width': 4.5}}), cap=('Pyramid S.ABCD: ABCD is a square and SA is perpendicular to the base. SA ⟂ AB and SA ⟂ AD, so SA ⟂ (ABCD).', 'Hình chóp S.ABCD: ABCD là hình vuông và SA vuông góc với đáy. SA ⟂ AB và SA ⟂ AD nên SA ⟂ (ABCD).'), alt=('Pyramid with the edge SA perpendicular to the base', ''), height=380)

theory += '<h3>5.2 %s</h3>' % TI('The angle between a line and a plane', 'Góc giữa đường thẳng và mặt phẳng')
theory += BOX('mint', ('Definition', 'Định nghĩa'),
  T(r'If a line meets a plane at \(B\) and its <b>projection</b> on the plane is the line \(BA\), the angle between the line and the plane is the angle between the line and its projection.', r'Nếu đường thẳng cắt mặt phẳng tại \(B\) và [[hình chiếu]] của nó trên mặt phẳng là đường \(BA\) thì góc giữa đường thẳng và mặt phẳng là góc giữa đường thẳng với hình chiếu của nó.'))
theory += GEO3D(pyr({('S', 'B'): {'color': '#c2410c', 'width': 4.5}}), cap=('For SB: the projection of S on the base is A, so the projection of SB is AB. The angle is SBA and tan(SBA) = SA / AB.', 'Với SB: hình chiếu của S lên đáy là A nên hình chiếu của SB là AB. Góc cần tìm là SBA và tan(SBA) = SA / AB.'), alt=('The angle between SB and the base', ''), height=380)

theory += '<h3>5.3 %s</h3>' % TI('Perpendicular planes', 'Hai mặt phẳng vuông góc')
theory += BOX('mint', ('Theorem', 'Định lí'),
  T(r'If a plane contains a line perpendicular to another plane, then the two planes are perpendicular.', r'Nếu một mặt phẳng chứa một đường thẳng vuông góc với mặt phẳng kia thì hai mặt phẳng vuông góc với nhau.'),
  T(r'Example: \(SA\subset(SAB)\) and \(SA\perp(ABCD)\), so \((SAB)\perp(ABCD)\).', r'Ví dụ: \(SA\subset(SAB)\) và \(SA\perp(ABCD)\) nên \((SAB)\perp(ABCD)\).'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T(r'To prove \(a\perp(P)\), the two lines in \((P)\) must <b>intersect</b>. Two parallel lines are not enough.', r'Để chứng minh \(a\perp(P)\), hai đường thẳng trong \((P)\) phải <b>cắt nhau</b>. Hai đường song song là chưa đủ.'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('A line perpendicular to a plane', 'Đường thẳng vuông góc với mặt phẳng'),
  T(r'In \(S.ABCD\) the base is a square and \(SA\perp(ABCD)\). Prove that \(BC\perp(SAB)\).', r'Cho \(S.ABCD\) có đáy là hình vuông và \(SA\perp(ABCD)\). Chứng minh \(BC\perp(SAB)\).'),
  (r'Find two intersecting lines of \((SAB)\) that are perpendicular to \(BC\).', r'Tìm hai đường thẳng cắt nhau của \((SAB)\) cùng vuông góc với \(BC\).'),
  [T(r'\(ABCD\) is a square, so \(BC\perp AB\).', r'\(ABCD\) là hình vuông nên \(BC\perp AB\).'), T(r'\(SA\perp(ABCD)\) and \(BC\subset(ABCD)\), so \(BC\perp SA\).', r'\(SA\perp(ABCD)\) và \(BC\subset(ABCD)\) nên \(BC\perp SA\).'),
   T(r'\(AB\) and \(SA\) intersect at \(A\) and lie in \((SAB)\). Hence \(BC\perp(SAB)\).', r'\(AB\) và \(SA\) cắt nhau tại \(A\) và cùng nằm trong \((SAB)\). Vậy \(BC\perp(SAB)\).')], TI('Proved.', 'Đã chứng minh.'))
examples += EXAMPLE(2, ('Intermediate', 'Trung bình'), ('An angle with a plane', 'Góc giữa đường thẳng và mặt phẳng'),
  T(r'The base \(ABCD\) is a square of side 2 and \(SA=2\) with \(SA\perp(ABCD)\). Find the angle between \(SC\) and \((ABCD)\).', r'Đáy \(ABCD\) là hình vuông cạnh 2, \(SA=2\) và \(SA\perp(ABCD)\). Tìm góc giữa \(SC\) và \((ABCD)\).'),
  (r'The projection of \(S\) on the base is \(A\), so the projection of \(SC\) is \(AC\). The angle is \(\widehat{SCA}\), in the right triangle \(SAC\).', r'Hình chiếu của \(S\) lên đáy là \(A\) nên hình chiếu của \(SC\) là \(AC\). Góc cần tìm là \(\widehat{SCA}\) trong tam giác vuông \(SAC\).'),
  [T(r'\(AC=2\sqrt2\) (the diagonal of a square of side 2).', r'\(AC=2\sqrt2\) (đường chéo hình vuông cạnh 2).'), T(r'\(\tan\widehat{SCA}=\dfrac{SA}{AC}=\dfrac{2}{2\sqrt2}=\dfrac{1}{\sqrt2}\approx 0{,}7071\).', r'\(\tan\widehat{SCA}=\dfrac{SA}{AC}=\dfrac{2}{2\sqrt2}=\dfrac{1}{\sqrt2}\approx 0{,}7071\).'),
   T(r'So \(\widehat{SCA}\approx 35{,}26^\circ\).', r'Vậy \(\widehat{SCA}\approx 35{,}26^\circ\).')], TI(r'about \(35.26^\circ\).', r'khoảng \(35{,}26^\circ\).'))
examples += EXAMPLE(3, ('Advanced', 'Nâng cao'), ('Two perpendicular planes', 'Hai mặt phẳng vuông góc'),
  T(r'Same pyramid. Prove that \((SBD)\perp(SAC)\).', r'Cùng hình chóp. Chứng minh \((SBD)\perp(SAC)\).'),
  (r'Show that \(BD\perp(SAC)\), then use the theorem of 5.3 with the line \(BD\) of the plane \((SBD)\).', r'Chứng minh \(BD\perp(SAC)\), rồi dùng định lí ở mục 5.3 với đường thẳng \(BD\) của mặt phẳng \((SBD)\).'),
  [T(r'The diagonals of a square are perpendicular: \(BD\perp AC\).', r'Hai đường chéo của hình vuông vuông góc: \(BD\perp AC\).'), T(r'\(SA\perp(ABCD)\), so \(BD\perp SA\).', r'\(SA\perp(ABCD)\) nên \(BD\perp SA\).'),
   T(r'\(AC\) and \(SA\) intersect at \(A\) in \((SAC)\), so \(BD\perp(SAC)\).', r'\(AC\) và \(SA\) cắt nhau tại \(A\) trong \((SAC)\) nên \(BD\perp(SAC)\).'),
   T(r'The plane \((SBD)\) contains \(BD\perp(SAC)\), so \((SBD)\perp(SAC)\).', r'Mặt phẳng \((SBD)\) chứa \(BD\perp(SAC)\) nên \((SBD)\perp(SAC)\).')], TI('Proved.', 'Đã chứng minh.'))

# ---- Hình vẽ cho ví dụ (TikZ -> SVG, tĩnh) ----
from mb_solids import fig, FILL, HL, BL
examples = EXFIG(examples, 1, GEO3D(fig('pyrsq', hl={('B', 'C'): HL}, poly=[FILL('SAB', '#86e0bd', .4)], right=[['S', 'A', 'B'], ['C', 'B', 'A']]), alt=('Pyramid with SA perpendicular to the base and BC perpendicular to SAB', '')))
examples = EXFIG(examples, 2, GEO3D(fig('pyrsq', seg=[['A', 'C'], ['S', 'C', {'color': HL}]], angles=[['S', 'C', 'A']], right=[['S', 'A', 'C']]), alt=('The angle SCA between SC and the base', '')))
examples = EXFIG(examples, 3, GEO3D(fig('pyrsq', pts={'O': 'mid:A,C'}, seg=[['A', 'C'], ['B', 'D', {'color': HL}], ['S', 'O']], poly=[FILL('SAC', '#fde68a', .45), FILL('SBD', '#86e0bd', .35)]), alt=('Planes SAC and SBD in the pyramid', '')))


SQ = lambda a_, h_: r'In the pyramid \(S.ABCD\), \(ABCD\) is a square of side %s and \(SA\perp(ABCD)\), \(SA=%s\). ' % (a_, h_)
SQV = lambda a_, h_: r'Trong hình chóp \(S.ABCD\), đáy \(ABCD\) là hình vuông cạnh %s, \(SA\perp(ABCD)\), \(SA=%s\). ' % (a_, h_)
# A1 độ dài AC; A2 độ dài SB; A3 đường vuông góc với mặt phẳng; B nhận định; C5 tan của góc SB và đáy; C6 SC²
S1 = [
  [MCQ(1, (SQ(2, 2) + r'Find \(AC\).', SQV(2, 2) + r'Tính \(AC\).'), [r'2\sqrt2', '4', r'\sqrt2', '8'], 'a', (r'Answer: a. The diagonal of a square of side \(a\) is \(a\sqrt2\).', r'Đáp án a. Đường chéo hình vuông cạnh \(a\) bằng \(a\sqrt2\).')),
   MCQ(2, (SQ(3, 4) + r'Find \(SB\).', SQV(3, 4) + r'Tính \(SB\).'), ['7', '5', '12', r'\sqrt7'], 'b', (r'Answer: b. \(SB^2=SA^2+AB^2=16+9=25\).', r'Đáp án b. \(SB^2=SA^2+AB^2=16+9=25\).')),
   MCQ(3, (r'In the same kind of pyramid, which line is perpendicular to the plane \((SAB)\)?', r'Trong hình chóp trên, đường thẳng nào vuông góc với mặt phẳng \((SAB)\)?'), ['BC', 'CD', 'AC', 'BD'], 'a', (r'Answer: a. \(BC\perp AB\) and \(BC\perp SA\).', r'Đáp án a. \(BC\perp AB\) và \(BC\perp SA\).'))],
  [TF(4, (r'In such a pyramid, \(SA\perp AB\).', r'Trong hình chóp như trên, \(SA\perp AB\).'), 'true', (r'True. \(SA\perp(ABCD)\) and \(AB\) lies in \((ABCD)\).', r'Đúng. \(SA\perp(ABCD)\) và \(AB\) nằm trong \((ABCD)\).'))],
  [SHORT(5, (SQ(2, 2) + r'Find \(\tan\) of the angle between \(SB\) and \((ABCD)\).', SQV(2, 2) + r'Tính \(\tan\) của góc giữa \(SB\) và \((ABCD)\).'), '1', 'number', ('Enter a number.', 'Nhập một số.'), (r'Answer: 1. \(\tan\widehat{SBA}=\dfrac{SA}{AB}=\dfrac22\).', r'Đáp số: 1. \(\tan\widehat{SBA}=\dfrac{SA}{AB}=\dfrac22\).')),
   SHORT(6, (SQ(1, 1) + r'Find \(SC^2\).', SQV(1, 1) + r'Tính \(SC^2\).'), '3', 'number', ('Enter a number.', 'Nhập một số.'), (r'Answer: 3. \(SC^2=SA^2+AC^2=1+2\).', r'Đáp số: 3. \(SC^2=SA^2+AC^2=1+2\).'))]]
S2 = [
  [MCQ(1, (SQ(3, 3) + r'Find \(AC\).', SQV(3, 3) + r'Tính \(AC\).'), ['3', '6', r'3\sqrt2', '9'], 'c', (r'Answer: c. \(AC=3\sqrt2\).', r'Đáp án c. \(AC=3\sqrt2\).')),
   MCQ(2, (SQ(5, 12) + r'Find \(SB\).', SQV(5, 12) + r'Tính \(SB\).'), ['13', '17', '7', r'\sqrt{119}'], 'a', (r'Answer: a. \(SB^2=144+25=169\).', r'Đáp án a. \(SB^2=144+25=169\).')),
   MCQ(3, (r'In the same kind of pyramid, which line is perpendicular to the plane \((SAD)\)?', r'Trong hình chóp trên, đường thẳng nào vuông góc với mặt phẳng \((SAD)\)?'), ['BC', 'CD', 'AC', 'BD'], 'b', (r'Answer: b. \(CD\perp AD\) and \(CD\perp SA\).', r'Đáp án b. \(CD\perp AD\) và \(CD\perp SA\).'))],
  [TF(4, (r'In such a pyramid, \(AC\perp SB\).', r'Trong hình chóp như trên, \(AC\perp SB\).'), 'false', (r'False. With \(A\) as origin, \(\overrightarrow{AC}=(a;a;0)\) and \(\overrightarrow{SB}=(a;0;-h)\), whose dot product is \(a^2\ne 0\).', r'Sai. Với \(A\) là gốc, \(\overrightarrow{AC}=(a;a;0)\), \(\overrightarrow{SB}=(a;0;-h)\), tích vô hướng bằng \(a^2\ne 0\).'))],
  [SHORT(5, (SQ(4, 2) + r'Find \(\tan\) of the angle between \(SB\) and \((ABCD)\).', SQV(4, 2) + r'Tính \(\tan\) của góc giữa \(SB\) và \((ABCD)\).'), '0.5|1/2', 'number', ('Enter a number or a fraction.', 'Nhập một số hoặc phân số.'), (r'Answer: 0.5. \(\tan\widehat{SBA}=\dfrac{2}{4}\).', r'Đáp số: 0,5. \(\tan\widehat{SBA}=\dfrac{2}{4}\).')),
   SHORT(6, (SQ(2, 1) + r'Find \(SC^2\).', SQV(2, 1) + r'Tính \(SC^2\).'), '9', 'number', ('Enter a number.', 'Nhập một số.'), (r'Answer: 9. \(SC^2=1+2\cdot 4\).', r'Đáp số: 9. \(SC^2=1+2\cdot 4\).'))]]
S3 = [
  [MCQ(1, (SQ(5, 5) + r'Find \(AC\).', SQV(5, 5) + r'Tính \(AC\).'), ['10', r'5\sqrt2', '5', '25'], 'b', (r'Answer: b. \(AC=5\sqrt2\).', r'Đáp án b. \(AC=5\sqrt2\).')),
   MCQ(2, (SQ(8, 6) + r'Find \(SB\).', SQV(8, 6) + r'Tính \(SB\).'), ['14', '2', '10', '48'], 'c', (r'Answer: c. \(SB^2=36+64=100\).', r'Đáp án c. \(SB^2=36+64=100\).')),
   MCQ(3, (r'In the same kind of pyramid, which line is perpendicular to the plane \((SAC)\)?', r'Trong hình chóp trên, đường thẳng nào vuông góc với mặt phẳng \((SAC)\)?'), ['BC', 'CD', 'AB', 'BD'], 'd', (r'Answer: d. \(BD\perp AC\) and \(BD\perp SA\).', r'Đáp án d. \(BD\perp AC\) và \(BD\perp SA\).'))],
  [TF(4, (r'In such a pyramid, \(SC\perp BD\).', r'Trong hình chóp như trên, \(SC\perp BD\).'), 'true', (r'True. \(BD\perp(SAC)\) and \(SC\subset(SAC)\).', r'Đúng. \(BD\perp(SAC)\) và \(SC\subset(SAC)\).'))],
  [SHORT(5, (SQ(3, 6) + r'Find \(\tan\) of the angle between \(SB\) and \((ABCD)\).', SQV(3, 6) + r'Tính \(\tan\) của góc giữa \(SB\) và \((ABCD)\).'), '2', 'number', ('Enter a number.', 'Nhập một số.'), (r'Answer: 2. \(\tan\widehat{SBA}=\dfrac63\).', r'Đáp số: 2. \(\tan\widehat{SBA}=\dfrac63\).')),
   SHORT(6, (SQ(1, 2) + r'Find \(SC^2\).', SQV(1, 2) + r'Tính \(SC^2\).'), '6', 'number', ('Enter a number.', 'Nhập một số.'), (r'Answer: 6. \(SC^2=4+2\cdot 1\).', r'Đáp số: 6. \(SC^2=4+2\cdot 1\).'))]]
practice = LEVEL_PRACTICE([('A. Multiple Choice', 'A. Trắc nghiệm'), ('B. True or False', 'B. Đúng hoặc sai'), ('C. Short Answer', 'C. Trả lời ngắn')], {1: S1, 2: S2, 3: S3})

mistakes = [
 (r'<b>Math knowledge.</b> Thinking that \(a\perp b\) and \(b\perp c\) implies \(a\perp c\). In space \(a\) and \(c\) can even be parallel.', r'<b>Kiến thức Toán.</b> Cho rằng \(a\perp b\) và \(b\perp c\) thì \(a\perp c\). Trong không gian \(a\) và \(c\) thậm chí có thể song song.'),
 (r'<b>Theorems.</b> Using two <b>parallel</b> lines of the plane to prove \(a\perp(P)\). They must intersect.', r'<b>Định lí.</b> Dùng hai đường thẳng <b>song song</b> trong mặt phẳng để chứng minh \(a\perp(P)\). Hai đường đó phải cắt nhau.'),
 (r'<b>Angles.</b> Taking \(\widehat{SBC}\) as the angle between \(SB\) and the base. Use the projection: \(\widehat{SBA}\).', r'<b>Góc.</b> Lấy \(\widehat{SBC}\) làm góc giữa \(SB\) và đáy. Phải dùng hình chiếu: \(\widehat{SBA}\).'),
 (r'<b>Drawings.</b> Drawing a “right angle” by eye. Build it as a true perpendicular.', r'<b>Hình vẽ.</b> Vẽ “góc vuông” theo cảm tính. Phải dựng bằng quan hệ vuông góc thật.'),
]
summary = [
 (r'A line perpendicular to two intersecting lines of a plane is perpendicular to the plane.', r'Đường thẳng vuông góc với hai đường thẳng cắt nhau của một mặt phẳng thì vuông góc với mặt phẳng.'),
 ('The angle between a line and a plane is the angle between the line and its projection on the plane.', 'Góc giữa đường thẳng và mặt phẳng là góc giữa đường thẳng và hình chiếu của nó trên mặt phẳng.'),
 (r'A plane that contains a line perpendicular to another plane is perpendicular to it.', r'Mặt phẳng chứa một đường thẳng vuông góc với mặt phẳng khác thì vuông góc với mặt phẳng đó.'),
 ('In the plane: a tangent to a circle is perpendicular to the radius at the point of tangency.', 'Trong mặt phẳng: tiếp tuyến của đường tròn vuông góc với bán kính tại tiếp điểm.'),
 ('Key English phrases: perpendicular to the plane; the angle between the line and the plane; the projection; prove that the planes are perpendicular.', 'Cụm tiếng Anh cần nhớ: perpendicular to the plane (vuông góc với mặt phẳng); the angle between the line and the plane (góc giữa đường thẳng và mặt phẳng); the projection (hình chiếu); prove that the planes are perpendicular (chứng minh hai mặt phẳng vuông góc).'),
]
checks = [
 ('I can build a perpendicular, an altitude and a tangent in the plane.', 'Tôi dựng được đường vuông góc, đường cao và tiếp tuyến trong mặt phẳng.'),
 ('I can prove that a line is perpendicular to a plane.', 'Tôi chứng minh được đường thẳng vuông góc với mặt phẳng.'),
 ('I can find the angle between a line and a plane.', 'Tôi tìm được góc giữa đường thẳng và mặt phẳng.'),
 ('I can prove that two planes are perpendicular.', 'Tôi chứng minh được hai mặt phẳng vuông góc.'),
 STD_SUMMARY_CHECK_EN(),
]

lesson(id=LID, title_en='Perpendicularity', title_vi='Quan hệ vuông góc', topic=TOPIC,
       folder='lines-and-planes-in-space', file='perpendicularity',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Perpendicular lines and planes in space, the angle between a line and a plane, with true constructions and 3D figures.', level='Intermediate', minutes=60,
       description_vi='Đường thẳng và mặt phẳng vuông góc, góc giữa đường thẳng và mặt phẳng, kèm hình dựng chính xác và hình 3D.',
       tags_vi=['vuông góc', 'góc giữa đường thẳng và mặt phẳng', 'hình chiếu', 'tiếp tuyến', 'hình chóp'],
       prerequisites=['g11-space-02'], tags=['perpendicular', 'projection', 'angle between line and plane', 'tangent', 'pyramid'], order=80)
