# -*- coding: utf-8 -*-
"""Nội dung bài g11-space-02 (Đường thẳng và mặt phẳng song song) – CHỈ NỘI DUNG."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *

LID = 'g11-space-02'
CAT = 'Lines and Planes in Space'
TOPIC = (CAT, 'Đường thẳng và mặt phẳng trong không gian')
CV = 'Hình học không gian'

ensure_vocab([
 ('g11-plane', 'plane', 'mặt phẳng', CV, 'A plane has no thickness.', ''),
 ('g11-parallel', 'parallel', 'song song', CV, 'The two lines are parallel.', r'\(a\parallel b\)'),
 ('g11-skew-lines', 'skew lines', 'hai đường thẳng chéo nhau', CV, 'Skew lines do not meet and are not parallel.', ''),
 ('g11-intersecting-lines', 'intersecting lines', 'hai đường thẳng cắt nhau', CV, 'Intersecting lines have one common point.', ''),
 ('g11-edge', 'edge', 'cạnh', CV, 'A cube has 12 edges.', ''),
 ('g11-face', 'face', 'mặt', CV, 'A cube has 6 faces.', ''),
 ('g11-midline', 'midline', 'đường trung bình', CV, 'The midline is parallel to the third side.', ''),
 ('g11-pyramid', 'pyramid', 'hình chóp', CV, 'The pyramid has a square base.', ''),
 ('g11-prism', 'prism', 'hình lăng trụ', CV, 'A triangular prism has 9 edges.', ''),
 ('g11-cube', 'cube', 'hình lập phương', CV, 'A cube has equal edges.', ''),
 ('g11-common-point', 'common point', 'điểm chung', CV, 'The line and the plane have no common point.', ''),
])
load_vocab()

# ---- kiểm tra hình học bằng vectơ tọa độ (các hình trong bài) ----
def sub(p, q): return tuple(a - b for a, b in zip(p, q))
def par(u, v): return all(abs(u[i] * v[j] - u[j] * v[i]) < 1e-9 for i in range(3) for j in range(3))
mid = lambda p, q: tuple((a + b) / 2 for a, b in zip(p, q))
A, B, C, D, S = (-3, -2, 0), (2, -2, 0), (3, 2, 0), (-2, 2, 0), (0, 0, 3.2)
assert sub(B, A) == sub(C, D) and mid(A, C) == (0, 0, 0)            # ABCD là hình bình hành tâm O
O = (0, 0, 0); M = mid(S, C); assert par(sub(M, O), sub(S, A))     # OM // SA (đường trung bình tam giác SAC)
cA, cB, cC, cD = (-2, -2, -2), (2, -2, -2), (2, 2, -2), (-2, 2, -2); cA1, cB1, cC1, cD1 = (-2, -2, 2), (2, -2, 2), (2, 2, 2), (-2, 2, 2)
assert par(sub(cB, cA1), sub(cC, cD1)) and par(sub(cD, cA1), sub(cC, cB1))   # A'B // D'C và A'D // B'C
assert not par(sub(cB, cA), sub(cC1, cB1)) and par(sub(cB, cA), sub(cC, cD))  # AB không // B'C' ; AB // CD

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 55 minutes', 'khoảng 55 phút'),
            before=('points, lines and planes in space (previous lesson), midlines in a triangle', 'điểm, đường thẳng, mặt phẳng trong không gian (bài trước), đường trung bình của tam giác'))
goals = [
 ('describe the positions of two lines in space: parallel, intersecting or skew;', 'mô tả vị trí của hai đường thẳng trong không gian: [[song song]], cắt nhau hoặc chéo nhau;'),
 ('prove that a line is parallel to a plane;', 'chứng minh đường thẳng song song với [[mặt phẳng]];'),
 ('prove that two planes are parallel;', 'chứng minh hai mặt phẳng song song;'),
 ('read a 3D figure: find its edges, faces and hidden (dashed) lines.', 'đọc hình không gian: tìm [[cạnh]], [[mặt]] và các nét khuất (nét đứt).'),
]
vocab = [
 ('<b>plane</b> – a flat surface that goes on without end.', '[[Mặt phẳng]] – bề mặt phẳng kéo dài vô hạn.'),
 (r'<b>parallel</b> – lines in the same plane that never meet: \(a\parallel b\).', r'[[Song song]] – hai đường thẳng cùng nằm trong một mặt phẳng và không bao giờ gặp nhau: \(a\parallel b\).'),
 ('<b>skew lines</b> – two lines that are not in the same plane: they do not meet and are not parallel.', '[[Hai đường thẳng chéo nhau]] – hai đường thẳng không cùng nằm trong một mặt phẳng: không gặp nhau và không song song.'),
 ('<b>intersecting lines</b> – two lines with exactly one common point.', '[[Hai đường thẳng cắt nhau]] – hai đường thẳng có đúng một điểm chung.'),
 ('<b>common point</b> – a point that belongs to both objects.', '[[Điểm chung]] – điểm thuộc cả hai đối tượng.'),
 ('<b>edge</b> – a segment where two faces of a solid meet.', '[[Cạnh]] – đoạn thẳng nơi hai mặt của khối gặp nhau.'),
 ('<b>face</b> – a flat surface of a solid.', '[[Mặt]] – một mặt phẳng của khối.'),
 ('<b>midline</b> – the segment joining the midpoints of two sides of a triangle.', '[[Đường trung bình]] – đoạn nối trung điểm hai cạnh của tam giác.'),
 ('<b>pyramid</b>, <b>prism</b>, <b>cube</b> – common solids.', '[[Hình chóp]], [[hình lăng trụ]], [[hình lập phương]] – các khối thường gặp.'),
]
phrases = [
 ('<b>Prove that the line is parallel to the plane.</b>', 'Chứng minh đường thẳng song song với mặt phẳng.'),
 ('<b>Are the lines parallel, intersecting or skew?</b>', 'Hai đường thẳng song song, cắt nhau hay chéo nhau?'),
 ('<b>Name the edges parallel to \\(AB\\).</b>', 'Kể tên các cạnh song song với \\(AB\\).'),
 ('<b>\\(M\\) is the midpoint of \\(SC\\).</b>', '\\(M\\) là trung điểm của \\(SC\\).'),
 ('<b>The line lies in the plane.</b>', 'Đường thẳng nằm trong mặt phẳng.'),
 ('<b>Show that the two planes are parallel.</b>', 'Chứng tỏ hai mặt phẳng song song.'),
]
review = (
 T(r'<b>Midline of a triangle.</b> If \(M\) and \(N\) are the midpoints of \(SA\) and \(SB\), then \(MN\parallel AB\) and \(MN=\dfrac12AB\).', r'<b>Đường trung bình của tam giác.</b> Nếu \(M\), \(N\) là trung điểm của \(SA\), \(SB\) thì \(MN\parallel AB\) và \(MN=\dfrac12AB\).') +
 T(r'<b>Parallelogram.</b> Opposite sides are parallel and equal; the diagonals bisect each other.', r'<b>Hình bình hành.</b> Các cạnh đối song song và bằng nhau; hai đường chéo cắt nhau tại trung điểm mỗi đường.'))

CUBE = {'solid': True, 'box': [[-3, 3], [-3, 3], [-3, 3]], 'points': {'A': cA, 'B': cB, 'C': cC, 'D': cD, 'A′': cA1, 'B′': cB1, 'C′': cC1, 'D′': cD1}}
def cube(extra=None, color_edges=None):
    edges = [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A'], ['A′', 'B′'], ['B′', 'C′'], ['C′', 'D′'], ['D′', 'A′'], ['A', 'A′'], ['B', 'B′'], ['C', 'C′'], ['D', 'D′']]
    cfg = dict(CUBE); cfg['segments'] = [e for e in edges if not (color_edges and tuple(e) in color_edges)] + [[e[0], e[1], color_edges[tuple(e)]] for e in edges if color_edges and tuple(e) in color_edges]
    cfg.update(extra or {}); return cfg

theory = '<h3>5.1 %s</h3>' % TI('Two lines in space', 'Hai đường thẳng trong không gian')
theory += T(r'Two lines in space are in exactly one of three positions: <b>parallel</b> (same plane, no common point), <b>intersecting</b> (one common point), or <b>skew</b> (not in the same plane).',
            r'Hai đường thẳng trong không gian ở đúng một trong ba vị trí: [[song song]] (cùng mặt phẳng, không có [[điểm chung]]), cắt nhau (có một điểm chung) hoặc chéo nhau (không cùng mặt phẳng).')
HL, BL = {'color': '#c2410c', 'width': 4.5}, {'color': '#1d4ed8', 'width': 4.5}
theory += GEO3D(cube(color_edges={('A', 'B'): HL, ('C', 'D'): HL, ('A', 'D'): BL, ('B′', 'C′'): {'color': '#7c3aed', 'width': 4.5}}),
                cap=('Edge AB (orange). CD is parallel to AB; AD (blue) meets AB at A; B′C′ (purple) is skew to AB.', 'Cạnh AB (cam). CD song song với AB; AD (xanh) cắt AB tại A; B′C′ (tím) chéo nhau với AB.'),
                alt=('A cube with four highlighted edges', ''), height=380)
theory += BOX('blue', ('A way to test', 'Cách kiểm tra'),
  T('Lines that are in the same plane are parallel or intersecting. If you cannot find a plane that contains both, they are skew.', 'Hai đường thẳng cùng nằm trong một mặt phẳng thì song song hoặc cắt nhau. Nếu không tìm được mặt phẳng chứa cả hai thì chúng chéo nhau.'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'),
  T(r'In space, two lines with no common point are <b>not</b> always parallel: they may be skew. Parallel lines must also lie in one plane.', r'Trong không gian, hai đường thẳng không có điểm chung <b>chưa chắc</b> song song: chúng có thể chéo nhau. Hai đường thẳng song song phải cùng nằm trong một mặt phẳng.'))

theory += '<h3>5.2 %s</h3>' % TI('A line parallel to a plane', 'Đường thẳng song song với mặt phẳng')
theory += BOX('mint', ('Theorem', 'Định lí'),
  T(r'If a line \(a\) is not in the plane \((P)\) and \(a\parallel b\) for some line \(b\) in \((P)\), then \(a\parallel(P)\), that is, \(a\) and \((P)\) have no common point.', r'Nếu đường thẳng \(a\) không nằm trong mặt phẳng \((P)\) và \(a\parallel b\) với một đường thẳng \(b\) nào đó nằm trong \((P)\) thì \(a\parallel(P)\), tức là \(a\) và \((P)\) không có điểm chung.'),
  T(r'If \(a\parallel(P)\) and a plane \((Q)\) contains \(a\) and meets \((P)\) along \(b\), then \(a\parallel b\).', r'Nếu \(a\parallel(P)\) và mặt phẳng \((Q)\) chứa \(a\), cắt \((P)\) theo giao tuyến \(b\) thì \(a\parallel b\).'))
PYR = {'solid': ['S', 'A', 'B', 'C', 'D'], 'box': [[-4, 4], [-3, 3], [-1, 4]], 'points': {'A': A, 'B': B, 'C': C, 'D': D, 'S': S, 'O': O, 'M': tuple(M)},
       'polygons': [['A', 'B', 'C', 'D']], 'segments': [['S', 'A'], ['S', 'B'], ['S', 'C'], ['S', 'D'], ['A', 'C', {'dash': True, 'color': '#64748b', 'width': 1.6}], ['B', 'D', {'dash': True, 'color': '#64748b', 'width': 1.6}], ['O', 'M', {'color': '#c2410c', 'width': 4}]]}
theory += GEO3D(PYR, cap=('Pyramid S.ABCD: ABCD is a parallelogram with centre O; M is the midpoint of SC. OM is a midline of triangle SAC.', 'Hình chóp S.ABCD: ABCD là hình bình hành tâm O; M là trung điểm của SC. OM là đường trung bình của tam giác SAC.'), alt=('Pyramid with the segment OM', ''), height=380)

theory += '<h3>5.3 %s</h3>' % TI('Parallel planes', 'Hai mặt phẳng song song')
theory += BOX('mint', ('Theorem', 'Định lí'),
  T(r'If a plane \((P)\) contains two <b>intersecting</b> lines that are both parallel to another plane \((Q)\), then \((P)\parallel(Q)\).', r'Nếu mặt phẳng \((P)\) chứa hai đường thẳng <b>cắt nhau</b> cùng song song với mặt phẳng \((Q)\) thì \((P)\parallel(Q)\).'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('A line parallel to the base', 'Đường thẳng song song với mặt đáy'),
  T(r'In the pyramid \(S.ABCD\) with a parallelogram base, \(M\) and \(N\) are the midpoints of \(SA\) and \(SB\). Prove that \(MN\parallel(ABCD)\) and \(MN\parallel CD\).', r'Cho hình chóp \(S.ABCD\) có đáy là hình bình hành; \(M\), \(N\) là trung điểm của \(SA\), \(SB\). Chứng minh \(MN\parallel(ABCD)\) và \(MN\parallel CD\).'),
  (r'Use the midline of triangle \(SAB\), then the theorem of 5.2.', r'Dùng [[đường trung bình]] của tam giác \(SAB\), rồi định lí ở mục 5.2.'),
  [T(r'\(MN\) is the midline of triangle \(SAB\), so \(MN\parallel AB\).', r'\(MN\) là đường trung bình của tam giác \(SAB\) nên \(MN\parallel AB\).'),
   T(r'\(AB\subset(ABCD)\) and \(MN\not\subset(ABCD)\), so \(MN\parallel(ABCD)\).', r'\(AB\subset(ABCD)\) và \(MN\not\subset(ABCD)\) nên \(MN\parallel(ABCD)\).'),
   T(r'\(ABCD\) is a parallelogram: \(AB\parallel CD\). Hence \(MN\parallel CD\).', r'\(ABCD\) là hình bình hành: \(AB\parallel CD\). Suy ra \(MN\parallel CD\).')],
  TI('Proved.', 'Đã chứng minh.'))
examples += EXAMPLE(2, ('Intermediate', 'Trung bình'), ('The centre and a midpoint', 'Tâm đáy và một trung điểm'),
  T(r'In the pyramid of the figure in 5.2, prove that \(OM\parallel(SAB)\) and \(OM\parallel(SAD)\).', r'Trong hình chóp ở hình mục 5.2, chứng minh \(OM\parallel(SAB)\) và \(OM\parallel(SAD)\).'),
  (r'First show \(OM\parallel SA\).', r'Trước hết chứng minh \(OM\parallel SA\).'),
  [T(r'\(O\) is the midpoint of \(AC\) (centre of the parallelogram) and \(M\) is the midpoint of \(SC\). So \(OM\) is the midline of triangle \(SAC\): \(OM\parallel SA\).', r'\(O\) là trung điểm \(AC\) (tâm hình bình hành), \(M\) là trung điểm \(SC\). Vậy \(OM\) là đường trung bình của tam giác \(SAC\): \(OM\parallel SA\).'),
   T(r'\(SA\subset(SAB)\) and \(OM\not\subset(SAB)\), so \(OM\parallel(SAB)\).', r'\(SA\subset(SAB)\) và \(OM\not\subset(SAB)\) nên \(OM\parallel(SAB)\).'),
   T(r'\(SA\subset(SAD)\) and \(OM\not\subset(SAD)\), so \(OM\parallel(SAD)\).', r'\(SA\subset(SAD)\) và \(OM\not\subset(SAD)\) nên \(OM\parallel(SAD)\).')],
  TI('Proved.', 'Đã chứng minh.'))
examples += EXAMPLE(3, ('Advanced', 'Nâng cao'), ('Two parallel planes in a cube', 'Hai mặt phẳng song song trong hình lập phương'),
  T(r'In the cube \(ABCD.A′B′C′D′\) prove that \((A′BD)\parallel(CB′D′)\).', r'Trong hình lập phương \(ABCD.A′B′C′D′\) chứng minh \((A′BD)\parallel(CB′D′)\).') +
  GEO3D(cube(extra={'polygons': [{'points': ['A′', 'B', 'D'], 'fill': '#86e0bd', 'opacity': 0.35}, {'points': ['C', 'B′', 'D′'], 'fill': '#fdba74', 'opacity': 0.35}]}), alt=('A cube with two triangular sections', ''), height=360),
  (r'Find two intersecting lines of \((A′BD)\) that are parallel to lines of \((CB′D′)\).', r'Tìm hai đường thẳng cắt nhau của \((A′BD)\) lần lượt song song với hai đường thẳng của \((CB′D′)\).'),
  [T(r'\(A′BCD′\) is a rectangle (a face section), so \(A′B\parallel D′C\) with \(D′C\subset(CB′D′)\); hence \(A′B\parallel(CB′D′)\).', r'\(A′BCD′\) là hình chữ nhật nên \(A′B\parallel D′C\), \(D′C\subset(CB′D′)\); suy ra \(A′B\parallel(CB′D′)\).'),
   T(r'Similarly \(A′DCB′\) is a rectangle: \(A′D\parallel B′C\), so \(A′D\parallel(CB′D′)\).', r'Tương tự \(A′DCB′\) là hình chữ nhật: \(A′D\parallel B′C\) nên \(A′D\parallel(CB′D′)\).'),
   T(r'\(A′B\) and \(A′D\) intersect at \(A′\) and lie in \((A′BD)\). By the theorem of 5.3, \((A′BD)\parallel(CB′D′)\).', r'\(A′B\) và \(A′D\) cắt nhau tại \(A′\) và nằm trong \((A′BD)\). Theo định lí ở mục 5.3, \((A′BD)\parallel(CB′D′)\).')],
  TI('Proved.', 'Đã chứng minh.'))

REL = lambda *a: [TI(*x) for x in a]
PAR, INT, SKW, IDN = ('parallel', 'song song'), ('intersecting', 'cắt nhau'), ('skew', 'chéo nhau'), ('identical', 'trùng nhau')
# A1 vị trí hai đường; A2 mệnh đề; A3 số cạnh song song; B nhận định; C5 số cạnh chéo nhau; C6 số mặt song song với cạnh
S1 = [
  [MCQ(1, (r'In a cube \(ABCD.A′B′C′D′\), what is the position of the edges \(AB\) and \(CD\)?', r'Trong hình lập phương \(ABCD.A′B′C′D′\), hai cạnh \(AB\) và \(CD\) có vị trí nào?'), REL(PAR, INT, SKW, IDN), 'a', ('Answer: a. They are opposite sides of the face ABCD, which is a square.', 'Đáp án a. Chúng là hai cạnh đối của mặt ABCD, là hình vuông.'), raw=True),
   MCQ(2, (r'The line \(a\) and the plane \((P)\) have no common point. Then:', r'Đường thẳng \(a\) và mặt phẳng \((P)\) không có điểm chung. Khi đó:'), [r'a\parallel(P)', r'a\subset(P)', r'a\ \text{cắt}\ (P)', r'a=(P)'], 'a', ('Answer: a. This is the definition of a line parallel to a plane.', 'Đáp án a. Đây chính là định nghĩa đường thẳng song song với mặt phẳng.')),
   MCQ(3, (r'How many other edges of a cube are parallel to a given edge?', r'Hình lập phương có bao nhiêu cạnh khác song song với một cạnh cho trước?'), ['1', '2', '3', '4'], 'c', ('Answer: c. The other three edges in the same direction.', 'Đáp án c. Ba cạnh còn lại cùng phương.'))],
  [TF(4, (r'Two lines with no common point are parallel.', r'Hai đường thẳng không có điểm chung thì song song.'), 'false', ('False. They may be skew.', 'Sai. Chúng có thể chéo nhau.'))],
  [SHORT(5, (r'How many edges of a cube are skew to a given edge?', r'Có bao nhiêu cạnh của hình lập phương chéo nhau với một cạnh cho trước?'), '4', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'), ('Answer: 4. Total 12 = 1 (itself) + 3 parallel + 4 intersecting + 4 skew.', 'Đáp số: 4. Tổng 12 = 1 (chính nó) + 3 song song + 4 cắt nhau + 4 chéo nhau.')),
   SHORT(6, (r'For an edge \(AB\) of a cube, how many faces are parallel to the line \(AB\)?', r'Với cạnh \(AB\) của hình lập phương, có bao nhiêu mặt song song với đường thẳng \(AB\)?'), '2', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'), ('Answer: 2. The faces CDD′C′ and A′B′C′D′ (they contain edges parallel to AB).', 'Đáp số: 2. Các mặt CDD′C′ và A′B′C′D′ (chứa các cạnh song song với AB).'))]]
S2 = [
  [MCQ(1, (r'In a triangular prism \(ABC.A′B′C′\), what is the position of the edges \(AB\) and \(B′C′\)?', r'Trong hình lăng trụ tam giác \(ABC.A′B′C′\), hai cạnh \(AB\) và \(B′C′\) có vị trí nào?'), REL(SKW, PAR, INT, IDN), 'a', (r'Answer: a. \(B′C′\parallel BC\), which meets \(AB\). The lines \(AB\) and \(B′C′\) have no common point and are not in one plane.', r'Đáp án a. \(B′C′\parallel BC\) mà \(BC\) cắt \(AB\). Hai đường \(AB\) và \(B′C′\) không có điểm chung và không cùng mặt phẳng.'), raw=True),
   MCQ(2, (r'\(a\parallel b\), \(b\subset(P)\) and \(a\not\subset(P)\). Then:', r'\(a\parallel b\), \(b\subset(P)\) và \(a\not\subset(P)\). Khi đó:'), [r'a\subset(P)', r'a\parallel(P)', r'a\perp(P)', r'a=b'], 'b', ('Answer: b. This is the theorem of 5.2.', 'Đáp án b. Đây là định lí ở mục 5.2.')),
   MCQ(3, (r'How many other edges of a triangular prism are parallel to the edge \(AB\)?', r'Hình lăng trụ tam giác có bao nhiêu cạnh khác song song với cạnh \(AB\)?'), ['1', '2', '3', '0'], 'a', (r'Answer: a. Only \(A′B′\).', r'Đáp án a. Chỉ có \(A′B′\).'))],
  [TF(4, (r'Two lines parallel to the same plane are parallel to each other.', r'Hai đường thẳng cùng song song với một mặt phẳng thì song song với nhau.'), 'false', ('False. They can intersect or be skew.', 'Sai. Chúng có thể cắt nhau hoặc chéo nhau.'))],
  [SHORT(5, (r'How many edges of a triangular prism are skew to the edge \(AB\)?', r'Có bao nhiêu cạnh của hình lăng trụ tam giác chéo nhau với cạnh \(AB\)?'), '3', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'), (r'Answer: 3. The edges \(B′C′\), \(C′A′\), \(CC′\).', r'Đáp số: 3. Đó là các cạnh \(B′C′\), \(C′A′\), \(CC′\).')),
   SHORT(6, (r'For the edge \(AB\) of a triangular prism, how many faces are parallel to the line \(AB\)?', r'Với cạnh \(AB\) của hình lăng trụ tam giác, có bao nhiêu mặt song song với đường thẳng \(AB\)?'), '1', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'), (r'Answer: 1. Only the face \(A′B′C′\).', r'Đáp số: 1. Chỉ có mặt \(A′B′C′\).'))]]
S3 = [
  [MCQ(1, (r'In the pyramid \(S.ABCD\) (\(ABCD\) is a parallelogram), what is the position of \(SC\) and \(AB\)?', r'Trong hình chóp \(S.ABCD\) (\(ABCD\) là hình bình hành), hai đường \(SC\) và \(AB\) có vị trí nào?'), REL(INT, PAR, IDN, SKW), 'd', (r'Answer: d. \(SC\) meets the base only at \(C\), which is not on \(AB\); and \(SC\) is not in the base plane.', r'Đáp án d. \(SC\) chỉ gặp mặt đáy tại \(C\) không thuộc \(AB\); và \(SC\) không nằm trong mặt đáy.'), raw=True),
   MCQ(2, (r'The plane \((Q)\) contains \(a\), \(a\parallel(P)\) and \((Q)\cap(P)=b\). Then:', r'Mặt phẳng \((Q)\) chứa \(a\), \(a\parallel(P)\) và \((Q)\cap(P)=b\). Khi đó:'), [r'a\perp b', r'a\ \text{cắt}\ b', r'a=b', r'a\parallel b'], 'd', ('Answer: d. This is the second theorem of 5.2.', 'Đáp án d. Đây là định lí thứ hai ở mục 5.2.')),
   MCQ(3, (r'How many other edges of the pyramid \(S.ABCD\) are parallel to the edge \(AB\)?', r'Hình chóp \(S.ABCD\) có bao nhiêu cạnh khác song song với cạnh \(AB\)?'), ['0', '1', '2', '3'], 'b', (r'Answer: b. Only \(CD\).', r'Đáp án b. Chỉ có \(CD\).'))],
  [TF(4, (r'If \(a\parallel b\) and \(b\parallel c\) (three different lines), then \(a\parallel c\).', r'Nếu \(a\parallel b\) và \(b\parallel c\) (ba đường thẳng phân biệt) thì \(a\parallel c\).'), 'true', ('True. Parallelism of lines in space is transitive.', 'Đúng. Quan hệ song song giữa các đường thẳng trong không gian có tính bắc cầu.'))],
  [SHORT(5, (r'How many edges of the pyramid \(S.ABCD\) are skew to the edge \(AB\)?', r'Có bao nhiêu cạnh của hình chóp \(S.ABCD\) chéo nhau với cạnh \(AB\)?'), '2', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'), (r'Answer: 2. The edges \(SC\) and \(SD\).', r'Đáp số: 2. Đó là các cạnh \(SC\) và \(SD\).')),
   SHORT(6, (r'For the edge \(AB\) of the pyramid \(S.ABCD\), how many faces are parallel to the line \(AB\)?', r'Với cạnh \(AB\) của hình chóp \(S.ABCD\), có bao nhiêu mặt song song với đường thẳng \(AB\)?'), '1', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'), (r'Answer: 1. The face \(SCD\), since \(AB\parallel CD\).', r'Đáp số: 1. Mặt \(SCD\), vì \(AB\parallel CD\).'))]]
practice = LEVEL_PRACTICE([('A. Multiple Choice', 'A. Trắc nghiệm'), ('B. True or False', 'B. Đúng hoặc sai'), ('C. Short Answer', 'C. Trả lời ngắn')], {1: S1, 2: S2, 3: S3})

mistakes = [
 (r'<b>Math knowledge.</b> Saying that two lines with no common point are parallel. They may be skew.', r'<b>Kiến thức Toán.</b> Cho rằng hai đường thẳng không có điểm chung thì song song. Chúng có thể chéo nhau.'),
 (r'<b>Theorems.</b> Forgetting the condition \(a\not\subset(P)\) when proving \(a\parallel(P)\).', r'<b>Định lí.</b> Quên điều kiện \(a\not\subset(P)\) khi chứng minh \(a\parallel(P)\).'),
 (r'<b>Parallel planes.</b> Using two <b>parallel</b> lines of \((P)\) instead of two <b>intersecting</b> lines.', r'<b>Hai mặt phẳng song song.</b> Dùng hai đường thẳng <b>song song</b> của \((P)\) thay vì hai đường thẳng <b>cắt nhau</b>.'),
 (r'<b>Reading figures.</b> Trusting that lines that look parallel in a drawing are parallel. Prove it from the data.', r'<b>Đọc hình.</b> Tin rằng hai đường trông song song trên hình vẽ thì song song. Phải chứng minh từ dữ kiện.'),
]
summary = [
 ('Two lines in space: parallel, intersecting or skew.', 'Hai đường thẳng trong không gian: song song, cắt nhau hoặc chéo nhau.'),
 (r'\(a\not\subset(P)\), \(a\parallel b\), \(b\subset(P)\) \(\Rightarrow\) \(a\parallel(P)\).', r'\(a\not\subset(P)\), \(a\parallel b\), \(b\subset(P)\) \(\Rightarrow\) \(a\parallel(P)\).'),
 (r'\((P)\) has two intersecting lines parallel to \((Q)\) \(\Rightarrow\) \((P)\parallel(Q)\).', r'\((P)\) có hai đường thẳng cắt nhau cùng song song với \((Q)\) \(\Rightarrow\) \((P)\parallel(Q)\).'),
 ('A midline of a triangle is parallel to the third side: it often gives the parallel line.', 'Đường trung bình của tam giác song song với cạnh thứ ba: thường dùng để tìm đường song song.'),
 ('Key English phrases: parallel, intersecting, skew; prove that the line is parallel to the plane.', 'Cụm tiếng Anh cần nhớ: parallel (song song), intersecting (cắt nhau), skew (chéo nhau); prove that the line is parallel to the plane (chứng minh đường thẳng song song với mặt phẳng).'),
]
checks = [
 ('I can tell if two lines in space are parallel, intersecting or skew.', 'Tôi nhận biết được hai đường thẳng trong không gian song song, cắt nhau hay chéo nhau.'),
 ('I can prove that a line is parallel to a plane.', 'Tôi chứng minh được đường thẳng song song với mặt phẳng.'),
 ('I can prove that two planes are parallel.', 'Tôi chứng minh được hai mặt phẳng song song.'),
 ('I can read a 3D figure and name its edges and faces.', 'Tôi đọc được hình không gian và gọi tên các cạnh, mặt.'),
 STD_SUMMARY_CHECK_EN(),
]

lesson(id=LID, title_en='Parallel Lines and Planes', title_vi='Đường thẳng và mặt phẳng song song', topic=TOPIC,
       folder='lines-and-planes-in-space', file='parallel-lines-and-planes',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Parallel lines, parallel line and plane, and parallel planes in space, with 3D figures.', level='Intermediate', minutes=55,
       description_vi='Hai đường thẳng song song, đường thẳng song song với mặt phẳng và hai mặt phẳng song song, kèm hình vẽ không gian.',
       tags_vi=['song song', 'chéo nhau', 'mặt phẳng', 'hình chóp', 'hình lập phương', 'đường trung bình'],
       prerequisites=[], tags=['parallel', 'skew lines', 'plane', 'pyramid', 'cube'], order=70)
