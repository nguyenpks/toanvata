# -*- coding: utf-8 -*-
"""g11-space-07 = Toán 11 KNTT, Bài 13: Hai mặt phẳng song song. Mã ngân hàng câu hỏi: TOAN11-C4-B13."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g11d as S
from sp_g11c import SOL, _cross, _dot, _sub

CV = 'Hai mặt phẳng song song'
vocab = defs(CV, [
 ('ppar', 'parallel planes', 'hai mặt phẳng song song', 'two planes with no common point; \\((P)\\parallel(Q)\\).', 'hai mặt phẳng không có điểm chung; \\((P)\\parallel(Q)\\).', 'The floor and the ceiling are parallel planes.', '\\((P)\\parallel(Q)\\)'),
 ('prism', 'prism', 'hình lăng trụ', 'a solid with two equal parallel bases and lateral faces that are parallelograms.', 'hình có hai đáy là hai đa giác bằng nhau nằm trên hai mặt phẳng song song, các mặt bên là hình bình hành.', 'A triangular prism has 5 faces.', ''),
 ('latedge', 'lateral edge', 'cạnh bên', 'an edge that joins the two bases; in a prism all lateral edges are parallel and equal.', 'cạnh nối hai đáy; trong hình lăng trụ các cạnh bên song song và bằng nhau.', '\\(AA′\\) is a lateral edge.', ''),
 ('pped', 'parallelepiped', 'hình hộp', 'a prism whose base is a parallelogram; all six faces are parallelograms.', 'hình lăng trụ có đáy là hình bình hành; cả sáu mặt đều là hình bình hành.', 'The four diagonals of a parallelepiped meet at one point.', ''),
 ('frust', 'frustum (truncated pyramid)', 'hình chóp cụt', 'the part of a pyramid between the base and a plane parallel to the base.', 'phần của hình chóp nằm giữa đáy và một mặt phẳng song song với đáy.', 'A lampshade has the shape of a frustum.', ''),
 ('thsp', 'Thales\' theorem in space', 'định lí Thalès trong không gian', 'three parallel planes cut any two lines in proportional segments.', 'ba mặt phẳng song song chắn trên hai cát tuyến bất kì những đoạn thẳng tương ứng tỉ lệ.', '\\(\\frac{AB}{A′B′}=\\frac{BC}{B′C′}\\).', '')])
goals = [('recognise parallel planes and prove that two planes are parallel;', 'nhận biết [[hai mặt phẳng song song]] và chứng minh hai mặt phẳng song song;'),
         ('use the properties of parallel planes to find lines of intersection;', 'dùng tính chất của hai mặt phẳng song song để tìm giao tuyến;'),
         ('apply Thales\' theorem in space;', 'vận dụng [[định lí Thalès trong không gian]];'),
         ('describe prisms, parallelepipeds and frustums and compute with them.', 'mô tả [[hình lăng trụ]], [[hình hộp]], [[hình chóp cụt]] và tính toán trên các hình đó.')]
phrases = [('<b>Prove that the two planes are parallel.</b>', 'Chứng minh hai mặt phẳng song song.'), ('<b>The plane cuts the two parallel planes along parallel lines.</b>', 'Mặt phẳng cắt hai mặt phẳng song song theo hai giao tuyến song song.'),
           ('<b>Find the length of the segment by Thales\' theorem.</b>', 'Tính độ dài đoạn thẳng bằng định lí Thalès.'), ('<b>The lateral edges of the prism are parallel and equal.</b>', 'Các cạnh bên của hình lăng trụ song song và bằng nhau.'), ('<b>How many faces does the prism have?</b>', 'Hình lăng trụ có bao nhiêu mặt?')]
review = T('From Bài 12: \\(a\\not\\subset(P)\\), \\(a\\parallel b\\subset(P)\\Rightarrow a\\parallel(P)\\); if \\(a\\parallel(P)\\) and a plane through \\(a\\) cuts \\((P)\\) along \\(b\\), then \\(b\\parallel a\\). Thales in a triangle: \\(MN\\parallel BC\\iff\\dfrac{AM}{AB}=\\dfrac{AN}{AC}\\).',
           'Từ Bài 12: \\(a\\not\\subset(P)\\), \\(a\\parallel b\\subset(P)\\Rightarrow a\\parallel(P)\\); nếu \\(a\\parallel(P)\\) và mặt phẳng chứa \\(a\\) cắt \\((P)\\) theo \\(b\\) thì \\(b\\parallel a\\). Thalès trong tam giác: \\(MN\\parallel BC\\iff\\dfrac{AM}{AB}=\\dfrac{AN}{AC}\\).')
# hình hộp (tọa độ cho hình vẽ): đáy ABCD là hình bình hành, AA′ không vuông góc với đáy
Ab, Bb, Cb, Db = (-3, -2, 0), (1, -2, 0), (3, 1.5, 0), (-1, 1.5, 0); sh_ = (0.8, 0.6, 3)
up = lambda P: tuple(p + s for p, s in zip(P, sh_))
A1, B1, C1, D1 = up(Ab), up(Bb), up(Cb), up(Db)
assert all(abs((Bb[i] - Ab[i]) - (Cb[i] - Db[i])) < 1e-12 for i in range(3))
BOXF = {'solid': True, 'box': [[-4, 5], [-3, 3], [-1, 4]], 'points': {'A': Ab, 'B': Bb, 'C': Cb, 'D': Db, 'A′': A1, 'B′': B1, 'C′': C1, 'D′': D1},
        'polygons': [{'points': ['A', 'B', 'C', 'D'], 'fill': '#86e0bd', 'opacity': .35}, {'points': ['A′', 'B′', 'C′', 'D′'], 'fill': '#fde68a', 'opacity': .35}]}
theory = '<h3>13.1 %s</h3>' % TI('Parallel planes and the criterion', 'Hai mặt phẳng song song và điều kiện song song')
theory += BOX('blue', ('Definition', 'Định nghĩa'), T('Two planes are parallel when they have no common point: \\((P)\\parallel(Q)\\). Then every line of \\((P)\\) is parallel to \\((Q)\\).', 'Hai mặt phẳng gọi là song song nếu chúng không có điểm chung: \\((P)\\parallel(Q)\\). Khi đó mọi đường thẳng nằm trong \\((P)\\) đều song song với \\((Q)\\).'))
theory += BOX('mint', ('Theorem 1 (criterion)', 'Định lí 1 (điều kiện)'), M('\\left.\\begin{array}{l}a,b\\subset(P),\\ a\\cap b=\\{O\\}\\\\ a\\parallel(Q),\\ b\\parallel(Q)\\end{array}\\right\\}\\Rightarrow(P)\\parallel(Q)'),
  T('Find in \\((P)\\) <b>two intersecting</b> lines, each parallel to \\((Q)\\) (usually each parallel to a line of \\((Q)\\)).', 'Tìm trong \\((P)\\) <b>hai đường thẳng cắt nhau</b> cùng song song với \\((Q)\\) (thường là mỗi đường song song với một đường thẳng của \\((Q)\\)).'))
theory += '<h3>13.2 %s</h3>' % TI('Properties', 'Tính chất')
theory += BOX('blue', ('Theorems', 'Các định lí'), UL([
  T('Through a point outside \\((Q)\\) there is exactly one plane parallel to \\((Q)\\).', 'Qua một điểm nằm ngoài mặt phẳng \\((Q)\\) có một và chỉ một mặt phẳng song song với \\((Q)\\).'),
  T('If \\((P)\\parallel(Q)\\) and a plane \\((R)\\) cuts \\((P)\\), then \\((R)\\) also cuts \\((Q)\\) and the two lines of intersection are parallel.', 'Nếu \\((P)\\parallel(Q)\\) và mặt phẳng \\((R)\\) cắt \\((P)\\) thì \\((R)\\) cũng cắt \\((Q)\\) và hai giao tuyến song song với nhau.'),
  T('<b>Thales\' theorem in space</b>: three parallel planes cut two lines at \\(A,B,C\\) and \\(A′,B′,C′\\) with \\(\\dfrac{AB}{A′B′}=\\dfrac{BC}{B′C′}=\\dfrac{CA}{C′A′}\\).', '<b>Định lí Thalès trong không gian</b>: ba mặt phẳng đôi một song song chắn trên hai cát tuyến bất kì các đoạn thẳng tương ứng tỉ lệ: \\(\\dfrac{AB}{A′B′}=\\dfrac{BC}{B′C′}=\\dfrac{CA}{C′A′}\\).')]))
theory += '<h3>13.3 %s</h3>' % TI('Prisms, parallelepipeds and frustums', 'Hình lăng trụ, hình hộp, hình chóp cụt')
theory += BOX('mint', ('Facts', 'Tính chất'), UL([
  T('<b>Prism</b>: two equal bases in parallel planes; lateral edges parallel and equal; lateral faces are parallelograms. An \\(n\\)-gonal prism has \\(n+2\\) faces, \\(3n\\) edges, \\(2n\\) vertices.', '<b>Hình lăng trụ</b>: hai đáy bằng nhau nằm trên hai mặt phẳng song song; các cạnh bên song song và bằng nhau; các mặt bên là hình bình hành. Lăng trụ \\(n\\)-giác có \\(n+2\\) mặt, \\(3n\\) cạnh, \\(2n\\) đỉnh.'),
  T('<b>Parallelepiped</b>: a prism with a parallelogram base; its 6 faces are parallelograms, opposite faces are parallel, and the 4 space diagonals meet at their common midpoint.', '<b>Hình hộp</b>: lăng trụ có đáy là hình bình hành; 6 mặt đều là hình bình hành, hai mặt đối diện song song, 4 đường chéo cắt nhau tại trung điểm của mỗi đường.'),
  T('<b>Frustum</b>: cut a pyramid by a plane parallel to the base. The two bases are similar polygons with parallel sides; the lateral edges, extended, meet at the apex.', '<b>Hình chóp cụt</b>: cắt hình chóp bởi mặt phẳng song song với đáy. Hai đáy là hai đa giác đồng dạng có các cạnh tương ứng song song; các cạnh bên kéo dài đồng quy tại đỉnh hình chóp.')]))
theory += GEO3D(BOXF, cap=('A parallelepiped \\(ABCD.A′B′C′D′\\): the bases \\((ABCD)\\) (green) and \\((A′B′C′D′)\\) (yellow) are parallel; hidden edges are dashed. Drag to rotate.', 'Hình hộp \\(ABCD.A′B′C′D′\\): hai đáy \\((ABCD)\\) (xanh) và \\((A′B′C′D′)\\) (vàng) song song; cạnh khuất vẽ nét đứt. Kéo để xoay hình.'), alt=('A parallelepiped with its two parallel bases', ''), height=380)
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('Two lines of \\((P)\\) parallel to \\((Q)\\) are enough only if they <b>intersect</b>; two parallel lines are not enough. Lines lying in two parallel planes may be skew.', 'Hai đường thẳng của \\((P)\\) song song với \\((Q)\\) chỉ đủ khi chúng <b>cắt nhau</b>; hai đường thẳng song song thì chưa đủ. Hai đường thẳng nằm trên hai mặt phẳng song song có thể chéo nhau.'))

CB = SOL['cube'][0]
def normal(pl):
    p = S.pts_of(pl); A_, B_, C_ = CB[p[0]], CB[p[1]], CB[p[2]]; return _cross(_sub(B_, A_), _sub(C_, A_)), A_
def planes_parallel(p1, p2):
    n1, P1 = normal(p1); n2, P2 = normal(p2); return _cross(n1, n2) == (0, 0, 0) and _dot(_sub(P2, P1), n1) != 0
assert planes_parallel('A′BD', 'CB′D′') and planes_parallel('ACD′', 'BA′C′') and not planes_parallel('ABC′', 'A′B′C')
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Parallel faces of a box', 'Các mặt song song của hình hộp'), T('In the parallelepiped \\(ABCD.A′B′C′D′\\), name the three pairs of parallel planes containing faces. Why is \\((ABB′A′)\\parallel(DCC′D′)\\)?', 'Trong hình hộp \\(ABCD.A′B′C′D′\\), kể tên ba cặp mặt phẳng song song chứa các mặt. Vì sao \\((ABB′A′)\\parallel(DCC′D′)\\)?'),
  T('Use the criterion with two intersecting lines \\(AB\\), \\(AA′\\).', 'Dùng điều kiện với hai đường thẳng cắt nhau \\(AB\\), \\(AA′\\).'),
  [T('\\((ABCD)\\parallel(A′B′C′D′)\\), \\((ABB′A′)\\parallel(DCC′D′)\\), \\((ADD′A′)\\parallel(BCC′B′)\\).', '\\((ABCD)\\parallel(A′B′C′D′)\\), \\((ABB′A′)\\parallel(DCC′D′)\\), \\((ADD′A′)\\parallel(BCC′B′)\\).'),
   T('\\(AB\\parallel DC\\subset(DCC′D′)\\) and \\(AA′\\parallel DD′\\subset(DCC′D′)\\); \\(AB\\), \\(AA′\\) meet at \\(A\\).', '\\(AB\\parallel DC\\subset(DCC′D′)\\) và \\(AA′\\parallel DD′\\subset(DCC′D′)\\); \\(AB\\), \\(AA′\\) cắt nhau tại \\(A\\).')],
  T('Three pairs; \\((ABB′A′)\\parallel(DCC′D′)\\) by Theorem 1.', 'Ba cặp; \\((ABB′A′)\\parallel(DCC′D′)\\) theo Định lí 1.'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Midpoints in a pyramid', 'Trung điểm trong hình chóp'), T('\\(S.ABCD\\) has a parallelogram base. \\(M,N,P\\) are the midpoints of \\(SA,SB,SC\\). Prove \\((MNP)\\parallel(ABCD)\\).', 'Cho hình chóp \\(S.ABCD\\) đáy là hình bình hành; \\(M,N,P\\) là trung điểm \\(SA,SB,SC\\). Chứng minh \\((MNP)\\parallel(ABCD)\\).'),
  T('Two intersecting lines of \\((MNP)\\): \\(MN\\) and \\(NP\\).', 'Hai đường thẳng cắt nhau trong \\((MNP)\\): \\(MN\\) và \\(NP\\).'),
  [T('Midlines: \\(MN\\parallel AB\\), \\(NP\\parallel BC\\), so \\(MN\\parallel(ABCD)\\), \\(NP\\parallel(ABCD)\\).', 'Đường trung bình: \\(MN\\parallel AB\\), \\(NP\\parallel BC\\) nên \\(MN\\parallel(ABCD)\\), \\(NP\\parallel(ABCD)\\).'), T('\\(MN\\) and \\(NP\\) meet at \\(N\\).', '\\(MN\\) và \\(NP\\) cắt nhau tại \\(N\\).')],
  T('\\((MNP)\\parallel(ABCD)\\).', '\\((MNP)\\parallel(ABCD)\\).'))
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Two diagonal planes', 'Hai mặt phẳng chéo'), T('In the parallelepiped \\(ABCD.A′B′C′D′\\), prove that \\((BA′C′)\\parallel(ACD′)\\).', 'Cho hình hộp \\(ABCD.A′B′C′D′\\). Chứng minh \\((BA′C′)\\parallel(ACD′)\\).'),
  T('Find two intersecting lines of \\((BA′C′)\\) parallel to lines of \\((ACD′)\\).', 'Tìm hai đường thẳng cắt nhau của \\((BA′C′)\\) lần lượt song song với hai đường thẳng của \\((ACD′)\\).'),
  [T('\\(ACC′A′\\) is a parallelogram, so \\(A′C′\\parallel AC\\).', '\\(ACC′A′\\) là hình bình hành nên \\(A′C′\\parallel AC\\).'), T('\\(A′BCD′\\) is a parallelogram (\\(A′D′\\parallel BC\\), \\(A′D′=BC\\)), so \\(BA′\\parallel CD′\\).', '\\(A′BCD′\\) là hình bình hành (\\(A′D′\\parallel BC\\), \\(A′D′=BC\\)) nên \\(BA′\\parallel CD′\\).'),
   T('\\(A′C′\\), \\(BA′\\) meet at \\(A′\\) and are parallel to \\((ACD′)\\).', '\\(A′C′\\), \\(BA′\\) cắt nhau tại \\(A′\\) và cùng song song với \\((ACD′)\\).')],
  T('\\((BA′C′)\\parallel(ACD′)\\).', '\\((BA′C′)\\parallel(ACD′)\\).'))
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Thales between floors', 'Thalès giữa các tầng nhà'), T('Three floors of a building lie in parallel planes. A straight cable crosses them at \\(A,B,C\\) and a straight rope at \\(A′,B′,C′\\). \\(AB=3\\) m, \\(BC=5\\) m, \\(A′B′=4.5\\) m. Find \\(B′C′\\) and \\(A′C′\\).', 'Ba sàn của một tòa nhà nằm trên ba mặt phẳng song song. Một dây cáp thẳng cắt ba sàn tại \\(A,B,C\\), một sợi dây thẳng cắt tại \\(A′,B′,C′\\). Biết \\(AB=3\\) m, \\(BC=5\\) m, \\(A′B′=4{,}5\\) m. Tính \\(B′C′\\) và \\(A′C′\\).'),
  T('Thales\' theorem in space.', 'Định lí Thalès trong không gian.'),
  [T('\\(\\dfrac{AB}{A′B′}=\\dfrac{BC}{B′C′}\\Rightarrow B′C′=\\dfrac{5\\cdot4.5}{3}=7.5\\) m.', '\\(\\dfrac{AB}{A′B′}=\\dfrac{BC}{B′C′}\\Rightarrow B′C′=\\dfrac{5\\cdot4{,}5}{3}=7{,}5\\) m.'), T('\\(A′C′=4.5+7.5\\).', '\\(A′C′=4{,}5+7{,}5\\).')],
  T('\\(B′C′=7.5\\) m, \\(A′C′=12\\) m.', '\\(B′C′=7{,}5\\) m, \\(A′C′=12\\) m.'))
assert F(5) * F(9, 2) / 3 == F(15, 2)
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('A lampshade', 'Chao đèn'), T('A lampshade is a frustum of a square pyramid. The bottom square has side 30 cm, the top square 12 cm. Extended, the lateral edges meet at the apex \\(S\\), and each edge of the whole pyramid is 50 cm. Find the length of a lateral edge of the lampshade.', 'Một chao đèn có dạng hình chóp cụt tứ giác đều: đáy lớn là hình vuông cạnh 30 cm, đáy nhỏ cạnh 12 cm. Kéo dài các cạnh bên cắt nhau tại đỉnh \\(S\\); mỗi cạnh bên của hình chóp đầy đủ dài 50 cm. Tính độ dài cạnh bên của chao đèn.'),
  T('The top base is cut by a plane parallel to the bottom base: use Thales in a lateral face.', 'Đáy nhỏ là thiết diện song song với đáy lớn: dùng Thalès trong một mặt bên.'),
  [T('In face \\(SAB\\): \\(A′B′\\parallel AB\\), so \\(\\dfrac{SA′}{SA}=\\dfrac{A′B′}{AB}=\\dfrac{12}{30}=\\dfrac25\\).', 'Trong mặt \\(SAB\\): \\(A′B′\\parallel AB\\) nên \\(\\dfrac{SA′}{SA}=\\dfrac{A′B′}{AB}=\\dfrac{12}{30}=\\dfrac25\\).'), T('\\(SA′=\\dfrac25\\cdot50=20\\) cm, so \\(AA′=50-20\\).', '\\(SA′=\\dfrac25\\cdot50=20\\) cm nên \\(AA′=50-20\\).')],
  T('Each lateral edge of the lampshade is 30 cm.', 'Mỗi cạnh bên của chao đèn dài 30 cm.'))
assert F(12, 30) * 50 == 20

ST5 = [('In the cube \\(ABCD.A′B′C′D′\\), \\((A′BD)\\parallel(CB′D′)\\).', 'Trong hình lập phương \\(ABCD.A′B′C′D′\\), \\((A′BD)\\parallel(CB′D′)\\).', 'A′BD', 'CB′D′'),
       ('In the cube \\(ABCD.A′B′C′D′\\), \\((ABC′)\\parallel(A′B′C)\\).', 'Trong hình lập phương \\(ABCD.A′B′C′D′\\), \\((ABC′)\\parallel(A′B′C)\\).', 'ABC′', 'A′B′C'),
       ('In the cube \\(ABCD.A′B′C′D′\\), \\((ACD′)\\parallel(BA′C′)\\).', 'Trong hình lập phương \\(ABCD.A′B′C′D′\\), \\((ACD′)\\parallel(BA′C′)\\).', 'ACD′', 'BA′C′')]
# ---- Hình vẽ cho ví dụ (TikZ -> SVG, tĩnh) ----
from mb_solids import fig, FILL, HL, BL
examples = EXFIG(examples, 1, GEO3D(fig('box', poly=[FILL(['A', 'B', 'B′', 'A′'], '#86e0bd', .35), FILL(['D', 'C', 'C′', 'D′'], '#fde68a', .45)]), alt=('Parallelepiped with two parallel faces shaded', '')))
examples = EXFIG(examples, 2, GEO3D(fig('pyr', pts={'M': 'mid:S,A', 'N': 'mid:S,B', 'P': 'mid:S,C'}, poly=[FILL('MNP', '#fca5a5', .45), FILL('ABCD', '#86e0bd', .3)]), alt=('Pyramid with the plane MNP parallel to the base', '')))
examples = EXFIG(examples, 3, GEO3D(fig('box', poly=[FILL(['B', 'A′', 'C′'], '#86e0bd', .4), FILL(['A', 'C', 'D′'], '#fde68a', .5)]), alt=('Parallelepiped with the planes BA′C′ and ACD′', '')))
examples = EXFIG(examples, 5, GEO3D(fig('pyr', pts={'A′': 'on:S,A,2/5', 'B′': 'on:S,B,2/5', 'C′': 'on:S,C,2/5', 'D′': 'on:S,D,2/5'}, seg=[['A′', 'B′'], ['B′', 'C′'], ['C′', 'D′'], ['D′', 'A′']], poly=[FILL(['A′', 'B′', 'C′', 'D′'], '#fde68a', .5)]), alt=('Pyramid cut by a plane parallel to the base: the frustum is the lampshade', '')))

def lvl(P):
    a, b, c = P['th']; x = F(b) * F(c) / a
    o1 = M4(1, 'Three parallel floors cut a straight cable at \\(A,B,C\\) and a straight rope at \\(A′,B′,C′\\). \\(AB=%s\\), \\(BC=%s\\), \\(A′B′=%s\\) (m). Then \\(B′C′=\\)…' % (fr(a), fr(b), fr(c)),
            'Ba sàn nhà song song cắt một dây cáp thẳng tại \\(A,B,C\\) và một sợi dây thẳng tại \\(A′,B′,C′\\). \\(AB=%s\\), \\(BC=%s\\), \\(A′B′=%s\\) (m). Khi đó \\(B′C′=\\)…' % (fr(a), fr(b), fr(c)),
            fr(x), [fr(F(a) * b / c), fr(F(b) + c - a), fr(F(c) * a / b), fr(x + 1)], '\\(B′C′=\\dfrac{BC\\cdot A′B′}{AB}=%s\\).' % fr(x), '\\(B′C′=\\dfrac{BC\\cdot A′B′}{AB}=%s\\).' % fr(x))
    n, kind = P['pr']; v = {'faces': n + 2, 'edges': 3 * n, 'verts': 2 * n}[kind]; w = {'faces': ('faces', 'mặt'), 'edges': ('edges', 'cạnh'), 'verts': ('vertices', 'đỉnh')}[kind]
    o2 = M4(2, 'A pencil has the shape of a prism with a regular %d-gon base. How many %s does this prism have?' % (n, w[0]), 'Một cây bút chì có dạng hình lăng trụ đáy là %d-giác đều. Hình lăng trụ đó có bao nhiêu %s?' % (n, w[1]),
            str(v), [str(t) for t in (n + 2, 3 * n, 2 * n, n, n + 1, 2 * n + 2) if t != v], '\\(n\\)-gonal prism: \\(n+2\\) faces, \\(3n\\) edges, \\(2n\\) vertices.', 'Lăng trụ \\(n\\)-giác: \\(n+2\\) mặt, \\(3n\\) cạnh, \\(2n\\) đỉnh.')
    big, small, full = P['fr']; k = F(small, big); top = k * full; lat = full - top; assert lat.denominator == 1
    o3 = M4(3, 'A planter is a frustum of a square pyramid with base edges %d cm and %d cm. The lateral edges, extended, meet at \\(S\\); a lateral edge of the full pyramid is %d cm. A lateral edge of the planter is…' % (big, small, full),
            'Một chậu cây có dạng hình chóp cụt tứ giác đều với cạnh hai đáy %d cm và %d cm. Kéo dài các cạnh bên cắt nhau tại \\(S\\); cạnh bên của hình chóp đầy đủ dài %d cm. Cạnh bên của chậu dài…' % (big, small, full),
            '%s\\ \\text{cm}' % fr(lat), ['%s\\ \\text{cm}' % fr(t) for t in (top, F(full - (big - small)), F(full, 2) if lat != F(full, 2) else F(full, 3), lat + 5)],
            '\\(\\dfrac{SA′}{SA}=\\dfrac{%d}{%d}\\), so \\(SA′=%s\\) and \\(AA′=%d-%s=%s\\).' % (small, big, fr(top), full, fr(top), fr(lat)), '\\(\\dfrac{SA′}{SA}=\\dfrac{%d}{%d}\\) nên \\(SA′=%s\\) và \\(AA′=%d-%s=%s\\).' % (small, big, fr(top), full, fr(top), fr(lat)))
    st = S.ST13[P['t4']]
    t4 = tf(4, st[1], st[2], st[0], 'Theorem 1 needs two <b>intersecting</b> lines; through a point there is exactly one parallel plane; lines in parallel planes may be skew.', 'Định lí 1 cần hai đường thẳng <b>cắt nhau</b>; qua một điểm có đúng một mặt phẳng song song; hai đường thẳng trên hai mặt phẳng song song có thể chéo nhau.')
    e = ST5[P['t5']]; truth = planes_parallel(e[2], e[3])
    t5 = tf(5, e[0], e[1], truth, 'Check two intersecting lines of one plane against the other (or use coordinates of the cube).', 'Kiểm tra hai đường thẳng cắt nhau của mặt phẳng này có song song với mặt phẳng kia không (hoặc dùng tọa độ hình lập phương).')
    a6, b6, c6 = P['th2']; x6 = F(c6) * F(a6 + b6) / a6; assert x6.denominator == 1
    s6 = sh(6, 'Three parallel planes cut line \\(d\\) at \\(A,B,C\\) and line \\(d′\\) at \\(A′,B′,C′\\). \\(AB=%d\\), \\(BC=%d\\), \\(A′B′=%d\\). Find \\(A′C′\\).' % (a6, b6, c6), 'Ba mặt phẳng song song cắt đường thẳng \\(d\\) tại \\(A,B,C\\) và cắt \\(d′\\) tại \\(A′,B′,C′\\). \\(AB=%d\\), \\(BC=%d\\), \\(A′B′=%d\\). Tính \\(A′C′\\).' % (a6, b6, c6), x6.numerator,
            '\\(\\dfrac{A′C′}{AC}=\\dfrac{A′B′}{AB}\\Rightarrow A′C′=\\dfrac{%d\\cdot%d}{%d}=%d\\).' % (c6, a6 + b6, a6, x6), '\\(\\dfrac{A′C′}{AC}=\\dfrac{A′B′}{AB}\\Rightarrow A′C′=\\dfrac{%d\\cdot%d}{%d}=%d\\).' % (c6, a6 + b6, a6, x6))
    (p7, q7), per = P['sec']; v7 = F(p7, q7) * per; assert v7.denominator == 1
    s7 = sh(7, 'A plane parallel to the base of the pyramid \\(S.ABC\\) cuts \\(SA\\) at \\(A′\\) with \\(\\dfrac{SA′}{SA}=\\dfrac{%d}{%d}\\). The perimeter of triangle \\(ABC\\) is %d. Find the perimeter of the cross-section \\(A′B′C′\\).' % (p7, q7, per),
            'Mặt phẳng song song với đáy của hình chóp \\(S.ABC\\) cắt \\(SA\\) tại \\(A′\\) với \\(\\dfrac{SA′}{SA}=\\dfrac{%d}{%d}\\). Chu vi tam giác \\(ABC\\) bằng %d. Tính chu vi thiết diện \\(A′B′C′\\).' % (p7, q7, per), v7.numerator,
            'Each side of \\(A′B′C′\\) is \\(\\dfrac{%d}{%d}\\) of the matching side: \\(%d\\).' % (p7, q7, v7), 'Mỗi cạnh của \\(A′B′C′\\) bằng \\(\\dfrac{%d}{%d}\\) cạnh tương ứng: \\(%d\\).' % (p7, q7, v7))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
PP = [dict(th=(2, 3, 4), pr=(6, 'faces'), fr=(20, 8, 40), t4=0, t5=0, th2=(2, 4, 3), sec=((1, 2), 36)),
      dict(th=(4, 6, 6), pr=(5, 'edges'), fr=(24, 9, 48), t4=3, t5=1, th2=(3, 6, 4), sec=((2, 3), 27)),
      dict(th=(5, 2, F(15, 2)), pr=(8, 'verts'), fr=(36, 15, 60), t4=4, t5=2, th2=(4, 6, 6), sec=((3, 5), 40))]
practice = three(lvl, PP)
practice = with_self(practice, S.M13S11, start=8)
mistakes = [('<b>Using two parallel lines.</b> The criterion needs two <b>intersecting</b> lines of \\((P)\\) parallel to \\((Q)\\).', '<b>Dùng hai đường thẳng song song.</b> Điều kiện cần hai đường thẳng <b>cắt nhau</b> của \\((P)\\) cùng song song với \\((Q)\\).'),
            ('<b>"Lines in parallel planes are parallel".</b> They may be skew.', '<b>"Hai đường thẳng nằm trên hai mặt phẳng song song thì song song".</b> Chúng có thể chéo nhau.'),
            ('<b>Mixing up segments in Thales.</b> Match the segments between the <b>same</b> two planes: \\(AB\\)–\\(A′B′\\).', '<b>Ghép sai đoạn trong Thalès.</b> Ghép các đoạn nằm giữa <b>cùng</b> hai mặt phẳng: \\(AB\\)–\\(A′B′\\).'),
            ('<b>Frustum edge = whole edge.</b> The lateral edge of a frustum is the whole edge minus the small top part.', '<b>Nhầm cạnh bên chóp cụt với cạnh bên hình chóp.</b> Cạnh bên chóp cụt bằng cạnh bên hình chóp trừ phần hình chóp nhỏ phía trên.')]
summary = [('\\((P)\\parallel(Q)\\): no common point. Criterion: two intersecting lines of \\((P)\\) parallel to \\((Q)\\).', '\\((P)\\parallel(Q)\\): không có điểm chung. Dấu hiệu: hai đường thẳng cắt nhau của \\((P)\\) cùng song song với \\((Q)\\).'),
           ('A plane cutting two parallel planes cuts them along parallel lines.', 'Mặt phẳng cắt hai mặt phẳng song song theo hai giao tuyến song song.'),
           ('Thales in space: \\(\\dfrac{AB}{A′B′}=\\dfrac{BC}{B′C′}=\\dfrac{CA}{C′A′}\\).', 'Thalès trong không gian: \\(\\dfrac{AB}{A′B′}=\\dfrac{BC}{B′C′}=\\dfrac{CA}{C′A′}\\).'),
           ('Prism: \\(n+2\\) faces, \\(3n\\) edges, \\(2n\\) vertices; parallelepiped: 3 pairs of parallel faces; frustum: bases similar and parallel. Key words: parallel planes, prism, frustum.', 'Lăng trụ: \\(n+2\\) mặt, \\(3n\\) cạnh, \\(2n\\) đỉnh; hình hộp: 3 cặp mặt song song; chóp cụt: hai đáy đồng dạng, song song. Từ cần nhớ: parallel planes, prism, frustum.')]
checks = [('I can prove that two planes are parallel.', 'Em chứng minh được hai mặt phẳng song song.'), ('I can use parallel planes to find parallel lines of intersection.', 'Em dùng được tính chất giao tuyến của mặt phẳng với hai mặt phẳng song song.'),
          ('I can apply Thales\' theorem in space.', 'Em vận dụng được định lí Thalès trong không gian.'), ('I can describe prisms, parallelepipeds and frustums.', 'Em mô tả được hình lăng trụ, hình hộp, hình chóp cụt.')]
LL('g11-space-07', 'Parallel Planes', CV, ('Parallelism in Space', 'Quan hệ song song trong không gian'), 'lines-and-planes-in-space', 'parallel-planes', 140, 'Intermediate', 70, ('a line parallel to a plane, Thales\' theorem in a triangle', 'đường thẳng song song với mặt phẳng, định lí Thalès trong tam giác'),
   'Parallel planes: criterion, properties, Thales\' theorem in space; prisms, parallelepipeds and frustums.', 'Bài 13 – Hai mặt phẳng song song: điều kiện, tính chất, định lí Thalès; hình lăng trụ, hình hộp, hình chóp cụt.',
   ['parallel planes', 'Thales', 'prism', 'parallelepiped', 'frustum'], ['hai mặt phẳng song song', 'Thalès', 'lăng trụ', 'hình hộp', 'chóp cụt'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g11-space-06'])
