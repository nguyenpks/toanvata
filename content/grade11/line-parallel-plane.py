# -*- coding: utf-8 -*-
"""g11-space-06 = Toán 11 KNTT, Bài 12: Đường thẳng và mặt phẳng song song. Mã ngân hàng câu hỏi: TOAN11-C4-B12."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g11d as S

CV = 'Đường thẳng và mặt phẳng song song'
vocab = defs(CV, [
 ('lpar', 'a line parallel to a plane', 'đường thẳng song song với mặt phẳng', 'a line and a plane with no common point; we write \\(a\\parallel(P)\\).', 'đường thẳng và mặt phẳng không có điểm chung; kí hiệu \\(a\\parallel(P)\\).', 'The edge \\(A′B′\\) is parallel to the plane \\((ABCD)\\).', '\\(a\\parallel(P)\\)'),
 ('lcut', 'a line cutting a plane', 'đường thẳng cắt mặt phẳng', 'a line and a plane with exactly one common point.', 'đường thẳng và mặt phẳng có đúng một điểm chung.', 'The line \\(SA\\) cuts \\((ABCD)\\) at \\(A\\).', ''),
 ('lin', 'a line lying in a plane', 'đường thẳng nằm trong mặt phẳng', 'every point of the line belongs to the plane; \\(a\\subset(P)\\).', 'mọi điểm của đường thẳng đều thuộc mặt phẳng; \\(a\\subset(P)\\).', '\\(AB\\subset(ABCD)\\).', '\\(a\\subset(P)\\)'),
 ('crit', 'condition (criterion)', 'điều kiện (dấu hiệu nhận biết)', 'a fact that is enough to conclude something.', 'điều đủ để kết luận một tính chất.', 'Use the criterion for a line parallel to a plane.', ''),
 ('thales', 'Thales\' theorem', 'định lí Thalès', 'a line parallel to one side of a triangle cuts the other two sides in equal ratios.', 'đường thẳng song song với một cạnh của tam giác chắn trên hai cạnh kia những đoạn tương ứng tỉ lệ.', 'By Thales\' theorem, \\(\\frac{AM}{AB}=\\frac{AN}{AC}\\).', ''),
 ('trapz', 'trapezoid', 'hình thang', 'a quadrilateral with (at least) one pair of parallel sides.', 'tứ giác có (ít nhất) một cặp cạnh đối song song.', 'The cross-section \\(ABMN\\) is a trapezoid.', '')])
goals = [('name the three positions of a line and a plane;', 'nêu ba vị trí tương đối của đường thẳng và mặt phẳng: [[đường thẳng song song với mặt phẳng]], [[đường thẳng cắt mặt phẳng]], [[đường thẳng nằm trong mặt phẳng]];'),
         ('prove that a line is parallel to a plane with the criterion;', 'chứng minh đường thẳng song song với mặt phẳng bằng [[điều kiện (dấu hiệu nhận biết)]];'),
         ('use the properties to find lines of intersection and cross-sections;', 'dùng tính chất để tìm [[giao tuyến]] và [[thiết diện]];'),
         ('compute lengths in a cross-section with Thales\' theorem.', 'tính độ dài trong thiết diện bằng [[định lí Thalès]].')]
phrases = [('<b>Prove that the line \\(MN\\) is parallel to the plane \\((ABCD)\\).</b>', 'Chứng minh đường thẳng \\(MN\\) song song với mặt phẳng \\((ABCD)\\).'), ('<b>The line lies in the plane.</b>', 'Đường thẳng nằm trong mặt phẳng.'),
           ('<b>Find the line of intersection of the two planes.</b>', 'Tìm giao tuyến của hai mặt phẳng.'), ('<b>Determine the cross-section of the pyramid.</b>', 'Xác định thiết diện của hình chóp.'), ('<b>The cross-section is a parallelogram.</b>', 'Thiết diện là hình bình hành.')]
review = T('From Bài 10–11: two planes with a common point meet along a line; two lines are parallel when they lie in one plane and have no common point; a midline of a triangle is parallel to the third side and half of it; if two planes contain two parallel lines and meet, their line of intersection is parallel to both.',
           'Từ Bài 10–11: hai mặt phẳng có một điểm chung thì cắt nhau theo một giao tuyến; hai đường thẳng song song là hai đường thẳng cùng nằm trong một mặt phẳng và không có điểm chung; đường trung bình của tam giác song song với cạnh thứ ba và bằng nửa cạnh đó; hai mặt phẳng cắt nhau lần lượt chứa hai đường thẳng song song thì giao tuyến song song với hai đường thẳng đó.')
A, B, C, D, Sp = (-3, -2, 0), (2, -2, 0), (3, 2, 0), (-2, 2, 0), (0, 0, 3.2)
mid = lambda P, Q: tuple((p + q) / 2 for p, q in zip(P, Q))
M_, N_, Mc, Nd = mid(Sp, A), mid(Sp, B), mid(Sp, C), mid(Sp, D)
assert all(abs((N_[i] - M_[i]) - (B[i] - A[i]) / 2) < 1e-12 for i in range(3)) and all(abs((Nd[i] - Mc[i]) - (D[i] - C[i]) / 2) < 1e-12 for i in range(3))
PYR = {'solid': ['S', 'A', 'B', 'C', 'D'], 'box': [[-4, 4], [-3, 3], [-1, 4]], 'points': {'A': A, 'B': B, 'C': C, 'D': D, 'S': Sp, 'M': M_, 'N': N_},
       'polygons': [{'points': ['A', 'B', 'C', 'D'], 'fill': '#86e0bd', 'opacity': .3}], 'segments': [['M', 'N', {'color': '#c2410c', 'width': 4}], ['A', 'B', {'color': '#1d4ed8', 'width': 4}]]}
theory = '<h3>12.1 %s</h3>' % TI('Positions of a line and a plane', 'Vị trí tương đối của đường thẳng và mặt phẳng')
theory += BOX('blue', ('Three cases (by the number of common points)', 'Ba trường hợp (theo số điểm chung)'), UL([
  T('<b>The line lies in the plane</b>: infinitely many common points, \\(a\\subset(P)\\).', '<b>Đường thẳng nằm trong mặt phẳng</b>: vô số điểm chung, \\(a\\subset(P)\\).'),
  T('<b>The line cuts the plane</b>: exactly one common point, \\(a\\cap(P)=\\{M\\}\\).', '<b>Đường thẳng cắt mặt phẳng</b>: đúng một điểm chung, \\(a\\cap(P)=\\{M\\}\\).'),
  T('<b>The line is parallel to the plane</b>: no common point, \\(a\\parallel(P)\\).', '<b>Đường thẳng song song với mặt phẳng</b>: không có điểm chung, \\(a\\parallel(P)\\).')]))
theory += '<h3>12.2 %s</h3>' % TI('Criterion for a line parallel to a plane', 'Điều kiện để đường thẳng song song với mặt phẳng')
theory += BOX('mint', ('Theorem 1', 'Định lí 1'), M('\\left.\\begin{array}{l}a\\not\\subset(P)\\\\ a\\parallel b\\\\ b\\subset(P)\\end{array}\\right\\}\\Rightarrow a\\parallel(P)'),
  T('To prove \\(a\\parallel(P)\\), find a line \\(b\\) <b>in</b> \\((P)\\) with \\(a\\parallel b\\), and check that \\(a\\) is not in \\((P)\\).', 'Muốn chứng minh \\(a\\parallel(P)\\), ta tìm một đường thẳng \\(b\\) <b>nằm trong</b> \\((P)\\) mà \\(a\\parallel b\\), và kiểm tra \\(a\\) không nằm trong \\((P)\\).'))
theory += GEO3D(PYR, cap=('\\(M\\), \\(N\\) are the midpoints of \\(SA\\), \\(SB\\): \\(MN\\parallel AB\\subset(ABCD)\\), so \\(MN\\parallel(ABCD)\\). Drag to rotate.', '\\(M\\), \\(N\\) là trung điểm \\(SA\\), \\(SB\\): \\(MN\\parallel AB\\subset(ABCD)\\) nên \\(MN\\parallel(ABCD)\\). Kéo để xoay hình.'), alt=('A pyramid with the midline MN parallel to the base edge AB', ''), height=380)
theory += '<h3>12.3 %s</h3>' % TI('Properties', 'Tính chất')
theory += BOX('blue', ('Theorem 2 and corollaries', 'Định lí 2 và hệ quả'), UL([
  T('If \\(a\\parallel(P)\\) and a plane \\((Q)\\) containing \\(a\\) cuts \\((P)\\) along \\(b\\), then \\(b\\parallel a\\).', 'Nếu \\(a\\parallel(P)\\) và mặt phẳng \\((Q)\\) chứa \\(a\\) cắt \\((P)\\) theo giao tuyến \\(b\\) thì \\(b\\parallel a\\).'),
  T('If two intersecting planes are both parallel to a line \\(d\\), then their line of intersection is parallel to \\(d\\).', 'Nếu hai mặt phẳng cắt nhau cùng song song với một đường thẳng \\(d\\) thì giao tuyến của chúng song song với \\(d\\).'),
  T('For two skew lines \\(a\\), \\(b\\), there is exactly one plane containing \\(a\\) and parallel to \\(b\\).', 'Cho hai đường thẳng chéo nhau \\(a\\), \\(b\\). Có đúng một mặt phẳng chứa \\(a\\) và song song với \\(b\\).')]))
theory += BOX('mint', ('How to use Theorem 2 for cross-sections', 'Dùng Định lí 2 để tìm thiết diện'), T('If the cutting plane \\((\\alpha)\\) is parallel to a line \\(d\\) and meets a face that contains \\(d\\) at a point \\(M\\), then the cut on that face is the line through \\(M\\) parallel to \\(d\\).', 'Nếu mặt phẳng cắt \\((\\alpha)\\) song song với đường thẳng \\(d\\) và có điểm chung \\(M\\) với một mặt chứa \\(d\\), thì giao tuyến trên mặt đó là đường thẳng qua \\(M\\) song song với \\(d\\).'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('\\(a\\parallel(P)\\) does <b>not</b> mean \\(a\\) is parallel to every line of \\((P)\\): it can be skew to many of them. Two lines parallel to the same plane may meet or be skew.', '\\(a\\parallel(P)\\) <b>không</b> có nghĩa \\(a\\) song song với mọi đường thẳng của \\((P)\\): \\(a\\) có thể chéo nhau với nhiều đường thẳng trong đó. Hai đường thẳng cùng song song với một mặt phẳng có thể cắt nhau hoặc chéo nhau.'))
assert S.plane_rel('cube', 'ABCD') == (4, 4, 4)
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Edges and a face of a cube', 'Cạnh và mặt của hình lập phương'), T('In the cube \\(ABCD.A′B′C′D′\\), which edges are parallel to the plane \\((ABCD)\\)? What is the position of \\(AC′\\) and \\((ABCD)\\)?', 'Trong hình lập phương \\(ABCD.A′B′C′D′\\), những cạnh nào song song với mặt phẳng \\((ABCD)\\)? Đường thẳng \\(AC′\\) và \\((ABCD)\\) có vị trí thế nào?'),
  T('An upper edge is parallel to a lower edge, which lies in \\((ABCD)\\).', 'Mỗi cạnh của mặt trên song song với một cạnh của mặt dưới, mà cạnh đó nằm trong \\((ABCD)\\).'),
  [T('\\(A′B′\\parallel AB\\subset(ABCD)\\) and \\(A′B′\\not\\subset(ABCD)\\), so \\(A′B′\\parallel(ABCD)\\); similarly \\(B′C′\\), \\(C′D′\\), \\(D′A′\\).', '\\(A′B′\\parallel AB\\subset(ABCD)\\) và \\(A′B′\\not\\subset(ABCD)\\) nên \\(A′B′\\parallel(ABCD)\\); tương tự với \\(B′C′\\), \\(C′D′\\), \\(D′A′\\).'), T('\\(A\\in AC′\\cap(ABCD)\\) and \\(C′\\notin(ABCD)\\).', '\\(A\\in AC′\\cap(ABCD)\\) và \\(C′\\notin(ABCD)\\).')],
  T('Four edges \\(A′B′, B′C′, C′D′, D′A′\\); \\(AC′\\) cuts \\((ABCD)\\) at \\(A\\).', 'Bốn cạnh \\(A′B′, B′C′, C′D′, D′A′\\); \\(AC′\\) cắt \\((ABCD)\\) tại \\(A\\).'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('A midline in a pyramid', 'Đường trung bình trong hình chóp'), T('\\(S.ABCD\\) has a parallelogram base; \\(M\\), \\(N\\) are the midpoints of \\(SA\\), \\(SB\\). Prove that \\(MN\\parallel(ABCD)\\) and \\(MN\\parallel(SCD)\\).', 'Cho hình chóp \\(S.ABCD\\) đáy là hình bình hành; \\(M\\), \\(N\\) là trung điểm \\(SA\\), \\(SB\\). Chứng minh \\(MN\\parallel(ABCD)\\) và \\(MN\\parallel(SCD)\\).'),
  T('Find in each plane a line parallel to \\(MN\\).', 'Trong mỗi mặt phẳng, tìm một đường thẳng song song với \\(MN\\).'),
  [T('\\(MN\\) is a midline of \\(\\triangle SAB\\): \\(MN\\parallel AB\\). \\(AB\\subset(ABCD)\\), \\(MN\\not\\subset(ABCD)\\) so \\(MN\\parallel(ABCD)\\).', '\\(MN\\) là đường trung bình của \\(\\triangle SAB\\): \\(MN\\parallel AB\\). Mà \\(AB\\subset(ABCD)\\), \\(MN\\not\\subset(ABCD)\\) nên \\(MN\\parallel(ABCD)\\).'),
   T('\\(AB\\parallel CD\\) so \\(MN\\parallel CD\\subset(SCD)\\); \\(M\\notin(SCD)\\).', '\\(AB\\parallel CD\\) nên \\(MN\\parallel CD\\subset(SCD)\\); \\(M\\notin(SCD)\\).')],
  T('\\(MN\\parallel(ABCD)\\) and \\(MN\\parallel(SCD)\\).', '\\(MN\\parallel(ABCD)\\) và \\(MN\\parallel(SCD)\\).'))
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Two centroids', 'Hai trọng tâm'), T('In the tetrahedron \\(ABCD\\), \\(G_1\\), \\(G_2\\) are the centroids of triangles \\(ABC\\) and \\(ABD\\). Prove that \\(G_1G_2\\parallel(BCD)\\).', 'Cho tứ diện \\(ABCD\\); \\(G_1\\), \\(G_2\\) là trọng tâm các tam giác \\(ABC\\), \\(ABD\\). Chứng minh \\(G_1G_2\\parallel(BCD)\\).'),
  T('Let \\(M\\), \\(N\\) be the midpoints of \\(BC\\), \\(BD\\) and use \\(\\dfrac{AG_1}{AM}=\\dfrac{AG_2}{AN}=\\dfrac23\\).', 'Gọi \\(M\\), \\(N\\) là trung điểm \\(BC\\), \\(BD\\) và dùng \\(\\dfrac{AG_1}{AM}=\\dfrac{AG_2}{AN}=\\dfrac23\\).'),
  [T('In \\(\\triangle AMN\\): \\(\\dfrac{AG_1}{AM}=\\dfrac{AG_2}{AN}\\), so \\(G_1G_2\\parallel MN\\) (Thales).', 'Trong \\(\\triangle AMN\\): \\(\\dfrac{AG_1}{AM}=\\dfrac{AG_2}{AN}\\) nên \\(G_1G_2\\parallel MN\\) (Thalès đảo).'), T('\\(MN\\subset(BCD)\\) and \\(G_1\\notin(BCD)\\).', '\\(MN\\subset(BCD)\\) và \\(G_1\\notin(BCD)\\).')],
  T('\\(G_1G_2\\parallel MN\\subset(BCD)\\), hence \\(G_1G_2\\parallel(BCD)\\) (and \\(G_1G_2=\\dfrac23MN=\\dfrac13CD\\)).', '\\(G_1G_2\\parallel MN\\subset(BCD)\\) nên \\(G_1G_2\\parallel(BCD)\\) (và \\(G_1G_2=\\dfrac23MN=\\dfrac13CD\\)).'))
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('A cross-section parallel to two edges', 'Thiết diện song song với hai cạnh'), T('Tetrahedron \\(ABCD\\) with \\(BC=AD=6\\). \\(M\\in AB\\), \\(AM=\\dfrac13AB\\). The plane \\((\\alpha)\\) through \\(M\\) is parallel to \\(BC\\) and \\(AD\\). Find the cross-section and its perimeter.', 'Cho tứ diện \\(ABCD\\) có \\(BC=AD=6\\). Điểm \\(M\\in AB\\) với \\(AM=\\dfrac13AB\\). Mặt phẳng \\((\\alpha)\\) qua \\(M\\), song song với \\(BC\\) và \\(AD\\). Xác định thiết diện và tính chu vi.'),
  T('On each face, draw through a known point a line parallel to \\(BC\\) or \\(AD\\) (Theorem 2).', 'Trên mỗi mặt, qua điểm đã biết kẻ đường thẳng song song với \\(BC\\) hoặc \\(AD\\) (Định lí 2).'),
  [T('In \\((ABC)\\): \\(MN\\parallel BC\\), \\(N\\in AC\\). In \\((ACD)\\): \\(NP\\parallel AD\\), \\(P\\in CD\\). In \\((BCD)\\): \\(PQ\\parallel BC\\), \\(Q\\in BD\\). Then \\(QM\\parallel AD\\).', 'Trong \\((ABC)\\): \\(MN\\parallel BC\\), \\(N\\in AC\\). Trong \\((ACD)\\): \\(NP\\parallel AD\\), \\(P\\in CD\\). Trong \\((BCD)\\): \\(PQ\\parallel BC\\), \\(Q\\in BD\\). Khi đó \\(QM\\parallel AD\\).'),
   T('\\(MN\\parallel PQ\\), \\(NP\\parallel QM\\): \\(MNPQ\\) is a parallelogram. Thales: \\(MN=\\dfrac13BC=2\\), \\(MQ=\\dfrac{BM}{BA}AD=\\dfrac23\\cdot6=4\\).', '\\(MN\\parallel PQ\\), \\(NP\\parallel QM\\): \\(MNPQ\\) là hình bình hành. Theo Thalès: \\(MN=\\dfrac13BC=2\\), \\(MQ=\\dfrac{BM}{BA}AD=\\dfrac23\\cdot6=4\\).')],
  T('Parallelogram \\(MNPQ\\), perimeter \\(2(2+4)=12\\).', 'Hình bình hành \\(MNPQ\\), chu vi \\(2(2+4)=12\\).'))
assert F(1, 3) * 6 == 2 and F(2, 3) * 6 == 4
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('A plane through a base edge', 'Mặt phẳng chứa một cạnh đáy'), T('\\(S.ABCD\\) has a parallelogram base, \\(AB=8\\). \\(M\\) is the midpoint of \\(SC\\). The plane \\((ABM)\\) cuts \\(SD\\) at \\(N\\). Find \\(N\\), the shape of the cross-section and \\(MN\\).', 'Cho hình chóp \\(S.ABCD\\) đáy là hình bình hành, \\(AB=8\\); \\(M\\) là trung điểm \\(SC\\). Mặt phẳng \\((ABM)\\) cắt \\(SD\\) tại \\(N\\). Xác định \\(N\\), hình dạng thiết diện và tính \\(MN\\).'),
  T('\\(AB\\parallel CD\\subset(SCD)\\), so \\(AB\\parallel(SCD)\\). Use Theorem 2 with the plane \\((ABM)\\) through \\(AB\\).', '\\(AB\\parallel CD\\subset(SCD)\\) nên \\(AB\\parallel(SCD)\\). Dùng Định lí 2 cho mặt phẳng \\((ABM)\\) chứa \\(AB\\).'),
  [T('\\((ABM)\\) and \\((SCD)\\) share \\(M\\); their line of intersection is the line through \\(M\\) parallel to \\(AB\\) (and \\(CD\\)), meeting \\(SD\\) at \\(N\\).', '\\((ABM)\\) và \\((SCD)\\) có điểm chung \\(M\\); giao tuyến là đường thẳng qua \\(M\\) song song với \\(AB\\) (và \\(CD\\)), cắt \\(SD\\) tại \\(N\\).'),
   T('\\(MN\\parallel CD\\) and \\(M\\) is the midpoint of \\(SC\\), so \\(N\\) is the midpoint of \\(SD\\) and \\(MN=\\dfrac12CD=4\\).', '\\(MN\\parallel CD\\), \\(M\\) là trung điểm \\(SC\\) nên \\(N\\) là trung điểm \\(SD\\) và \\(MN=\\dfrac12CD=4\\).')],
  T('\\(N\\) is the midpoint of \\(SD\\); the cross-section \\(ABMN\\) is a trapezoid (\\(MN\\parallel AB\\), \\(MN=4\\ne AB\\)); \\(MN=4\\).', '\\(N\\) là trung điểm \\(SD\\); thiết diện \\(ABMN\\) là hình thang (\\(MN\\parallel AB\\), \\(MN=4\\ne AB\\)); \\(MN=4\\).'))
assert all(abs((Nd[i] - Mc[i]) - (D[i] - C[i]) / 2) < 1e-12 for i in range(3))

SOLNAME = S.NM
# ---- Hình vẽ cho ví dụ (TikZ -> SVG, tĩnh) ----
from mb_solids import fig, FILL, HL, BL
examples = EXFIG(examples, 1, GEO3D(fig('cube', seg=[['A', 'C′', {'color': HL}]], poly=[FILL('ABCD', '#86e0bd', .3)], hl={('A′', 'B′'): BL, ('B′', 'C′'): BL, ('C′', 'D′'): BL, ('D′', 'A′'): BL}), alt=('Cube: the top edges are parallel to the base; AC′ cuts the base at A', '')))
examples = EXFIG(examples, 2, GEO3D(fig('pyr', pts={'M': 'mid:S,A', 'N': 'mid:S,B'}, seg=[['M', 'N', {'color': HL}]], hl={('A', 'B'): BL, ('C', 'D'): BL}), alt=('Pyramid with MN parallel to AB and CD', '')))
examples = EXFIG(examples, 3, GEO3D(fig('tet', pts={'I': 'mid:A,B', 'G_1': 'cen:A,B,C', 'G_2': 'cen:A,B,D'}, seg=[['C', 'I', {'color': '#64748b', 'width': 1.6}], ['D', 'I', {'color': '#64748b', 'width': 1.6}], ['G_1', 'G_2', {'color': HL}]]), alt=('Tetrahedron with the centroids G1 and G2', '')))
examples = EXFIG(examples, 4, GEO3D(fig('tet', pts={'M': 'on:A,B,1/3', 'N': 'on:A,C,1/3', 'P': 'on:D,C,1/3', 'Q': 'on:D,B,1/3'}, poly=[FILL('MNPQ', '#fca5a5', .45)]), alt=('Tetrahedron with the cross-section MNPQ', '')))
examples = EXFIG(examples, 5, GEO3D(fig('pyr', pts={'M': 'mid:S,C', 'N': 'mid:S,D'}, poly=[FILL(['A', 'B', 'M', 'N'], '#fca5a5', .45)]), alt=('Pyramid with the cross-section ABMN', '')))

def lvl(P):
    sol, pl = P['cnt']; par, inn, cut = S.plane_rel(sol, pl)
    o1 = M4(1, 'How many edges of %s are parallel to the plane \\((%s)\\)?' % (SOLNAME[sol][0], pl), 'Có bao nhiêu cạnh của %s song song với mặt phẳng \\((%s)\\)?' % (SOLNAME[sol][1], pl), str(par), [str(par + inn), str(inn), str(cut + par), str(par + 1), str(par + 2)],
            'Parallel edges: not in the plane and parallel to a line in it: %d.' % par, 'Cạnh song song: không nằm trong mặt phẳng và song song với một đường thẳng của nó: %d.' % par)
    (p, q), L = P['th']; x = F(p * L, q)
    o2 = M4(2, 'Tetrahedron \\(ABCD\\), \\(BC=%d\\). \\(M\\in AB\\) with \\(AM=\\dfrac{%d}{%d}AB\\). The plane through \\(M\\) parallel to \\(BC\\) cuts \\(AC\\) at \\(N\\). Then \\(MN=\\)…' % (L, p, q), 'Tứ diện \\(ABCD\\) có \\(BC=%d\\). Điểm \\(M\\in AB\\), \\(AM=\\dfrac{%d}{%d}AB\\). Mặt phẳng qua \\(M\\) song song với \\(BC\\) cắt \\(AC\\) tại \\(N\\). Khi đó \\(MN=\\)…' % (L, p, q),
            fr(x), [fr(F((q - p) * L, q)), str(L), fr(F(q * L, p)), fr(x + 1), fr(2 * x + 1)], '\\(MN\\parallel BC\\) (Theorem 2), Thales: \\(MN=\\dfrac{%d}{%d}\\cdot%d=%s\\).' % (p, q, L, fr(x)), '\\(MN\\parallel BC\\) (Định lí 2), Thalès: \\(MN=\\dfrac{%d}{%d}\\cdot%d=%s\\).' % (p, q, L, fr(x)))
    (p3, q3), L3 = P['pyr']; x3 = F(p3 * L3, q3)
    o3 = M4(3, 'A tent has the shape of a pyramid \\(S.ABCD\\) with a rectangular floor, \\(AB=%d\\) dm. A straight pole \\(MN\\) joins \\(M\\in SC\\) and \\(N\\in SD\\) with \\(MN\\parallel(ABCD)\\) and \\(\\dfrac{SM}{SC}=\\dfrac{%d}{%d}\\). The pole is…' % (L3, p3, q3),
            'Một chiếc lều có dạng hình chóp \\(S.ABCD\\), đáy hình chữ nhật, \\(AB=%d\\) dm. Thanh nẹp thẳng \\(MN\\) nối \\(M\\in SC\\), \\(N\\in SD\\), \\(MN\\parallel(ABCD)\\) và \\(\\dfrac{SM}{SC}=\\dfrac{%d}{%d}\\). Thanh nẹp dài…' % (L3, p3, q3),
            '%s\\ \\text{dm}' % fr(x3), ['%s\\ \\text{dm}' % fr(v) for v in (F((q3 - p3) * L3, q3), F(L3), F(L3, 2) if x3 != F(L3, 2) else F(L3, 4), x3 + 5, 2 * x3 + 5)],
            '\\((SCD)\\) contains \\(MN\\) and cuts \\((ABCD)\\) along \\(CD\\), so \\(MN\\parallel CD\\); \\(MN=\\dfrac{%d}{%d}CD=%s\\).' % (p3, q3, fr(x3)), '\\((SCD)\\) chứa \\(MN\\), cắt \\((ABCD)\\) theo \\(CD\\) nên \\(MN\\parallel CD\\); \\(MN=\\dfrac{%d}{%d}CD=%s\\).' % (p3, q3, fr(x3)))
    st = S.ST12[P['t4']]
    t4 = tf(4, st[1], st[2], st[0], 'Recall Theorem 1, Theorem 2 and the corollary; a line parallel to \\((P)\\) may be skew to lines of \\((P)\\).', 'Nhớ lại Định lí 1, Định lí 2 và hệ quả; đường thẳng song song với \\((P)\\) có thể chéo nhau với đường thẳng nằm trong \\((P)\\).')
    st5 = [('In the cube \\(ABCD.A′B′C′D′\\), \\(A′C′\\parallel(ABCD)\\).', 'Trong hình lập phương \\(ABCD.A′B′C′D′\\), \\(A′C′\\parallel(ABCD)\\).', True, '\\(A′C′\\parallel AC\\subset(ABCD)\\).', '\\(A′C′\\parallel AC\\subset(ABCD)\\).'),
           ('In the cube \\(ABCD.A′B′C′D′\\), \\(AC′\\parallel(A′B′C′D′)\\).', 'Trong hình lập phương \\(ABCD.A′B′C′D′\\), \\(AC′\\parallel(A′B′C′D′)\\).', False, '\\(AC′\\) meets \\((A′B′C′D′)\\) at \\(C′\\).', '\\(AC′\\) cắt \\((A′B′C′D′)\\) tại \\(C′\\).'),
           ('In the cube \\(ABCD.A′B′C′D′\\), \\(BD\\parallel(CB′D′)\\).', 'Trong hình lập phương \\(ABCD.A′B′C′D′\\), \\(BD\\parallel(CB′D′)\\).', True, '\\(BD\\parallel B′D′\\subset(CB′D′)\\) and \\(B\\notin(CB′D′)\\).', '\\(BD\\parallel B′D′\\subset(CB′D′)\\) và \\(B\\notin(CB′D′)\\).')][P['t5']]
    t5 = tf(5, st5[0], st5[1], st5[2], st5[3], st5[4])
    (p6, q6), bc, ad = P['sec']; mn, mq = F(p6 * bc, q6), F((q6 - p6) * ad, q6); per = 2 * (mn + mq); assert per.denominator == 1
    s6 = sh(6, 'Tetrahedron \\(ABCD\\), \\(BC=%d\\), \\(AD=%d\\). \\(M\\in AB\\), \\(AM=\\dfrac{%d}{%d}AB\\). The plane through \\(M\\) parallel to \\(BC\\) and \\(AD\\) cuts the tetrahedron in a parallelogram. Find its perimeter.' % (bc, ad, p6, q6),
            'Tứ diện \\(ABCD\\) có \\(BC=%d\\), \\(AD=%d\\). Điểm \\(M\\in AB\\), \\(AM=\\dfrac{%d}{%d}AB\\). Mặt phẳng qua \\(M\\) song song với \\(BC\\) và \\(AD\\) cắt tứ diện theo một hình bình hành. Tính chu vi hình bình hành đó.' % (bc, ad, p6, q6), per.numerator,
            '\\(MN=\\dfrac{%d}{%d}BC=%s\\), \\(MQ=\\dfrac{%d}{%d}AD=%s\\); perimeter \\(=%d\\).' % (p6, q6, fr(mn), q6 - p6, q6, fr(mq), per), '\\(MN=\\dfrac{%d}{%d}BC=%s\\), \\(MQ=\\dfrac{%d}{%d}AD=%s\\); chu vi \\(=%d\\).' % (p6, q6, fr(mn), q6 - p6, q6, fr(mq), per))
    sol7, pl7 = P['cut']; par7, inn7, cut7 = S.plane_rel(sol7, pl7)
    s7 = sh(7, 'How many lines containing an edge of %s cut the plane \\((%s)\\) (exactly one common point)?' % (SOLNAME[sol7][0], pl7), 'Có bao nhiêu đường thẳng chứa cạnh của %s cắt mặt phẳng \\((%s)\\) (có đúng một điểm chung)?' % (SOLNAME[sol7][1], pl7), cut7,
            '%d edges are parallel, %d lie in the plane, the other %d cut it.' % (par7, inn7, cut7), '%d cạnh song song, %d cạnh nằm trong mặt phẳng, %d cạnh còn lại cắt mặt phẳng.' % (par7, inn7, cut7))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
PP = [dict(cnt=('cube', 'ABCD'), th=((1, 2), 10), pyr=((1, 2), 30), t4=0, t5=0, sec=((1, 2), 8, 6), cut=('cube', 'ABB′A′')),
      dict(cnt=('prism', 'ABB′A′'), th=((2, 3), 12), pyr=((2, 5), 25), t4=3, t5=1, sec=((1, 3), 9, 12), cut=('pyr', 'SAC')),
      dict(cnt=('cube', 'ACC′A′'), th=((3, 4), 16), pyr=((3, 5), 40), t4=4, t5=2, sec=((2, 5), 10, 15), cut=('box', 'ACC′A′'))]
practice = three(lvl, PP)
practice = with_self(practice, S.M12S11, start=8)
mistakes = [('<b>Forgetting \\(a\\not\\subset(P)\\).</b> If \\(a\\parallel b\\subset(P)\\), \\(a\\) may lie in \\((P)\\); check one point of \\(a\\) is outside \\((P)\\).', '<b>Quên điều kiện \\(a\\not\\subset(P)\\).</b> Nếu \\(a\\parallel b\\subset(P)\\) thì \\(a\\) có thể nằm trong \\((P)\\); phải chỉ ra một điểm của \\(a\\) ở ngoài \\((P)\\).'),
            ('<b>"Parallel to every line".</b> \\(a\\parallel(P)\\) does not make \\(a\\) parallel to all lines of \\((P)\\).', '<b>"Song song với mọi đường thẳng".</b> \\(a\\parallel(P)\\) không suy ra \\(a\\) song song với mọi đường thẳng của \\((P)\\).'),
            ('<b>Drawing the cut line freely.</b> On a face containing \\(d\\parallel(\\alpha)\\), the cut must be parallel to \\(d\\).', '<b>Vẽ giao tuyến tùy ý.</b> Trên mặt chứa \\(d\\parallel(\\alpha)\\), giao tuyến phải song song với \\(d\\).'),
            ('<b>Wrong ratio in Thales.</b> \\(MN=\\dfrac{AM}{AB}BC\\) but \\(MQ=\\dfrac{BM}{BA}AD\\): use the vertex of each triangle.', '<b>Dùng sai tỉ số Thalès.</b> \\(MN=\\dfrac{AM}{AB}BC\\) nhưng \\(MQ=\\dfrac{BM}{BA}AD\\): tỉ số tính từ đỉnh của từng tam giác.')]
summary = [('Line and plane: in it, cutting it (one point), or parallel (no point).', 'Đường thẳng và mặt phẳng: nằm trong, cắt (một điểm chung) hoặc song song (không có điểm chung).'),
           ('Criterion: \\(a\\not\\subset(P)\\), \\(a\\parallel b\\subset(P)\\Rightarrow a\\parallel(P)\\).', 'Dấu hiệu: \\(a\\not\\subset(P)\\), \\(a\\parallel b\\subset(P)\\Rightarrow a\\parallel(P)\\).'),
           ('\\(a\\parallel(P)\\), \\(a\\subset(Q)\\), \\((Q)\\cap(P)=b\\Rightarrow b\\parallel a\\): the key to cross-sections.', '\\(a\\parallel(P)\\), \\(a\\subset(Q)\\), \\((Q)\\cap(P)=b\\Rightarrow b\\parallel a\\): chìa khóa tìm thiết diện.'),
           ('Key words: parallel to a plane, line of intersection, cross-section.', 'Từ cần nhớ: parallel to a plane, line of intersection, cross-section.')]
checks = [('I can name the position of a line and a plane.', 'Em nêu được vị trí tương đối của đường thẳng và mặt phẳng.'), ('I can prove that a line is parallel to a plane.', 'Em chứng minh được đường thẳng song song với mặt phẳng.'),
          ('I can find a cross-section parallel to a line.', 'Em xác định được thiết diện song song với một đường thẳng.'), ('I can compute lengths with Thales\' theorem.', 'Em tính được độ dài nhờ định lí Thalès.')]
LL('g11-space-06', 'Lines Parallel to Planes', CV, ('Parallelism in Space', 'Quan hệ song song trong không gian'), 'lines-and-planes-in-space', 'line-parallel-plane', 130, 'Intermediate', 70, ('lines and planes in space, parallel lines, midline of a triangle', 'đường thẳng và mặt phẳng trong không gian, hai đường thẳng song song, đường trung bình'),
   'Positions of a line and a plane, the criterion and properties of a line parallel to a plane, cross-sections.', 'Bài 12 – Vị trí tương đối, điều kiện và tính chất của đường thẳng song song với mặt phẳng; thiết diện.',
   ['line parallel to a plane', 'cross-section', 'line of intersection'], ['đường thẳng song song mặt phẳng', 'thiết diện', 'giao tuyến'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g11-space-05'])
