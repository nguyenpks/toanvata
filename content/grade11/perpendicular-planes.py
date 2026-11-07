# -*- coding: utf-8 -*-
"""g11-perp-04 = Toán 11 KNTT, Bài 25: Hai mặt phẳng vuông góc. Mã ngân hàng câu hỏi: TOAN11-C7-B25."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
from mb_solids import fig, FILL, HL, BL, GR
import sp_g11i as S
from sp_g11h import rq

CV = 'Hai mặt phẳng vuông góc'
vocab = defs(CV, [
 ('angpp2', 'angle between two planes', 'góc giữa hai mặt phẳng (không gian)', 'the angle between two lines perpendicular to the two planes; equivalently, for intersecting planes, between two lines in them perpendicular to the common line at one point.', 'góc giữa hai đường thẳng lần lượt vuông góc với hai mặt phẳng; với hai mặt phẳng cắt nhau, đó là góc giữa hai đường thẳng nằm trong hai mặt và cùng vuông góc với giao tuyến tại một điểm.', 'The angle between (SBC) and (ABCD) is SBA.', ''),
 ('dihed', 'dihedral angle', 'góc nhị diện', 'the figure formed by two half-planes with a common edge; it is measured by a plane angle perpendicular to the edge.', 'hình tạo bởi hai nửa mặt phẳng có chung bờ; số đo của nó là số đo một góc phẳng nhị diện (vuông góc với cạnh).', 'The dihedral angle [S, BC, A] measures 60°.', ''),
 ('perpplanes', 'perpendicular planes', 'hai mặt phẳng vuông góc', 'two planes whose angle is \\(90^\\circ\\); this holds when one contains a line perpendicular to the other.', 'hai mặt phẳng tạo với nhau góc \\(90^\\circ\\); điều đó xảy ra khi mặt này chứa một đường thẳng vuông góc với mặt kia.', 'The plane (SAB) is perpendicular to the base.', '\\((P)\\perp(Q)\\)'),
 ('regpyr', 'regular pyramid', 'hình chóp đều', 'a pyramid whose base is a regular polygon and whose apex projects onto the centre of the base.', 'hình chóp có đáy là đa giác đều và hình chiếu của đỉnh trên đáy là tâm của đáy.', 'In a regular pyramid all lateral edges are equal.', '')])
goals = [('define and compute the angle between two planes and the dihedral angle;', 'nêu định nghĩa và tính [[góc giữa hai mặt phẳng (không gian)|góc giữa hai mặt phẳng (không gian)]], [[góc nhị diện]];'),
         ('prove that two planes are perpendicular;', 'chứng minh [[hai mặt phẳng vuông góc]];'),
         ('recognise right prisms, boxes, cubes, [[hình chóp đều]] and regular frustums;', 'nhận biết hình lăng trụ đứng, lăng trụ đều, hình hộp chữ nhật, hình lập phương, [[hình chóp đều]], hình chóp cụt đều;'),
         ('compute roof pitches and lateral faces of real pyramids.', 'tính độ dốc mái nhà và mặt bên của các khối chóp thực tế.')]
goals[2] = ('recognise right prisms, boxes, cubes, regular pyramids and regular frustums;', goals[2][1])
phrases = [('<b>The two planes meet along the line \\(BC\\).</b>', 'Hai mặt phẳng cắt nhau theo giao tuyến \\(BC\\).'), ('<b>Both lines are perpendicular to the common line.</b>', 'Cả hai đường thẳng đều vuông góc với giao tuyến.'),
           ('<b>The plane contains a line perpendicular to the base.</b>', 'Mặt phẳng chứa một đường thẳng vuông góc với đáy.'), ('<b>The lateral faces make sixty degrees with the base.</b>', 'Các mặt bên tạo với đáy góc 60°.'), ('<b>The roof is pitched at about thirty-seven degrees.</b>', 'Mái nhà dốc khoảng 37°.')]
review = T('From Bài 23–24: \\(d\\perp(P)\\) via two intersecting lines; the angle between a line and a plane uses the projection. Grade 9: tangent ratio in a right triangle.', 'Từ Bài 23–24: chứng minh \\(d\\perp(P)\\) qua hai đường thẳng cắt nhau; góc giữa đường thẳng và mặt phẳng dùng hình chiếu. Lớp 9: tỉ số tan trong tam giác vuông.')
theory = '<h3>25.1 %s</h3>' % TI('Angle between two planes; dihedral angles', 'Góc giữa hai mặt phẳng; góc nhị diện')
theory += BOX('blue', ('Definition and method', 'Định nghĩa và cách xác định'), UL([T('The angle between \\((P)\\) and \\((Q)\\) is the angle between two lines \\(a\\perp(P)\\), \\(b\\perp(Q)\\). It lies in \\([0^\\circ;90^\\circ]\\); parallel or equal planes make \\(0^\\circ\\).', 'Góc giữa \\((P)\\) và \\((Q)\\) là góc giữa hai đường thẳng \\(a\\perp(P)\\), \\(b\\perp(Q)\\). Góc này thuộc \\([0^\\circ;90^\\circ]\\); hai mặt song song hoặc trùng nhau tạo góc \\(0^\\circ\\).'),
  T('Practical method for \\((P)\\cap(Q)=c\\): at a point \\(I\\in c\\) draw \\(a\\subset(P)\\), \\(b\\subset(Q)\\), both perpendicular to \\(c\\); then \\(((P),(Q))=(a,b)\\).', 'Cách xác định khi \\((P)\\cap(Q)=c\\): tại \\(I\\in c\\), dựng \\(a\\subset(P)\\), \\(b\\subset(Q)\\) cùng vuông góc với \\(c\\); khi đó \\(((P),(Q))=(a,b)\\).'),
  T('A <b>dihedral angle</b> \\([P,c,Q]\\) is formed by two half-planes with edge \\(c\\); its plane angle is built the same way, but can be obtuse (from \\(0^\\circ\\) to \\(180^\\circ\\)).', '<b>Góc nhị diện</b> \\([P,c,Q]\\) tạo bởi hai nửa mặt phẳng có chung bờ \\(c\\); góc phẳng nhị diện dựng tương tự nhưng có thể tù (từ \\(0^\\circ\\) đến \\(180^\\circ\\)).')]))
theory += GEO3D(fig('pyrsq', hl={('S', 'B'): HL, ('A', 'B'): BL, ('B', 'C'): GR}, angles=[['S', 'B', 'A']], right=[['S', 'B', 'C'], ['A', 'B', 'C']]),
  cap=('\\((SBC)\\cap(ABCD)=BC\\); \\(AB\\perp BC\\) and \\(SB\\perp BC\\) (three perpendiculars), so the angle between the planes is \\(\\widehat{SBA}\\).', '\\((SBC)\\cap(ABCD)=BC\\); \\(AB\\perp BC\\) và \\(SB\\perp BC\\) (ba đường vuông góc), nên góc giữa hai mặt phẳng là \\(\\widehat{SBA}\\).'), alt=('The angle SBA between the face SBC and the base', ''), height=360)
theory += '<h3>25.2 %s</h3>' % TI('Perpendicular planes', 'Hai mặt phẳng vuông góc')
theory += BOX('mint', ('Criterion and properties', 'Điều kiện và tính chất'), UL([T('If \\((P)\\) contains a line \\(a\\perp(Q)\\) then \\((P)\\perp(Q)\\).', 'Nếu \\((P)\\) chứa một đường thẳng \\(a\\perp(Q)\\) thì \\((P)\\perp(Q)\\).'),
  T('If \\((P)\\perp(Q)\\), every line of \\((P)\\) perpendicular to the common line is perpendicular to \\((Q)\\).', 'Nếu \\((P)\\perp(Q)\\) thì mọi đường thẳng nằm trong \\((P)\\) và vuông góc với giao tuyến đều vuông góc với \\((Q)\\).'),
  T('Two intersecting planes both perpendicular to \\((R)\\) meet along a line perpendicular to \\((R)\\).', 'Hai mặt phẳng cắt nhau cùng vuông góc với \\((R)\\) thì giao tuyến của chúng vuông góc với \\((R)\\).')]))
theory += '<h3>25.3 %s</h3>' % TI('Special prisms and pyramids', 'Một số hình lăng trụ, hình chóp đặc biệt')
theory += BOX('blue', ('Definitions', 'Định nghĩa'), UL([T('<b>Right prism</b>: lateral edges perpendicular to the bases (lateral faces are rectangles); <b>regular prism</b>: right prism with regular-polygon bases; <b>right box</b>: right prism with parallelogram bases; <b>rectangular box</b>: right box with rectangle bases; <b>cube</b>: all faces squares.', '<b>Lăng trụ đứng</b>: cạnh bên vuông góc với đáy (mặt bên là hình chữ nhật); <b>lăng trụ đều</b>: lăng trụ đứng có đáy là đa giác đều; <b>hình hộp đứng</b>: lăng trụ đứng có đáy là hình bình hành; <b>hình hộp chữ nhật</b>: hình hộp đứng có đáy là hình chữ nhật; <b>hình lập phương</b>: mọi mặt là hình vuông.'),
  T('<b>Regular pyramid</b>: regular base, apex projecting to the centre \\(O\\); lateral edges equal, lateral faces congruent isosceles triangles, all make the same angle with the base. A plane parallel to the base cuts off a <b>regular frustum</b>.', '<b>Hình chóp đều</b>: đáy là đa giác đều, hình chiếu của đỉnh là tâm \\(O\\) của đáy; các cạnh bên bằng nhau, các mặt bên là các tam giác cân bằng nhau và tạo với đáy các góc bằng nhau. Mặt phẳng song song với đáy cắt ra <b>hình chóp cụt đều</b>.')]))
cfg_reg = fig('pyrsq', pts={'O': (0, 0, 0), 'M': (0, 2, 0)}, seg=[['S', 'O', {'dash': True}], ['O', 'M', {'color': BL}], ['S', 'M', {'color': HL}]], angles=[['S', 'M', 'O']], right=[['S', 'O', 'M']])
cfg_reg['points']['S'] = (0.0, 0.0, 3.4)
theory += GEO3D(cfg_reg, cap=('Regular pyramid: \\(M\\) is the midpoint of \\(CD\\); \\(OM\\perp CD\\), \\(SM\\perp CD\\), so the angle between a lateral face and the base is \\(\\widehat{SMO}\\).', 'Hình chóp đều: \\(M\\) là trung điểm \\(CD\\); \\(OM\\perp CD\\), \\(SM\\perp CD\\) nên góc giữa mặt bên và đáy là \\(\\widehat{SMO}\\).'), alt=('Regular pyramid with the angle SMO', ''), height=360)

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Proving perpendicular planes', 'Chứng minh hai mặt phẳng vuông góc'), T('\\(S.ABCD\\): square base, \\(SA\\perp(ABCD)\\). Prove \\((SAB)\\perp(ABCD)\\), \\((SAB)\\perp(SBC)\\) and \\((SAC)\\perp(SBD)\\).', 'Hình chóp \\(S.ABCD\\) có đáy là hình vuông, \\(SA\\perp(ABCD)\\). Chứng minh \\((SAB)\\perp(ABCD)\\), \\((SAB)\\perp(SBC)\\) và \\((SAC)\\perp(SBD)\\).'),
  T('Find in one plane a line perpendicular to the other.', 'Tìm trong một mặt phẳng một đường thẳng vuông góc với mặt kia.'),
  [T('\\(SA\\subset(SAB)\\), \\(SA\\perp(ABCD)\\): \\((SAB)\\perp(ABCD)\\).', '\\(SA\\subset(SAB)\\), \\(SA\\perp(ABCD)\\): \\((SAB)\\perp(ABCD)\\).'), T('\\(BC\\perp(SAB)\\) (Bài 23), \\(BC\\subset(SBC)\\): \\((SBC)\\perp(SAB)\\).', '\\(BC\\perp(SAB)\\) (Bài 23), \\(BC\\subset(SBC)\\): \\((SBC)\\perp(SAB)\\).'),
   T('\\(BD\\perp(SAC)\\), \\(BD\\subset(SBD)\\): \\((SBD)\\perp(SAC)\\).', '\\(BD\\perp(SAC)\\), \\(BD\\subset(SBD)\\): \\((SBD)\\perp(SAC)\\).')], T('All three pairs are perpendicular.', 'Cả ba cặp mặt phẳng đều vuông góc.'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Angle between a face and the base', 'Góc giữa mặt bên và đáy'), T('\\(S.ABCD\\): square base of side \\(a\\), \\(SA\\perp(ABCD)\\), \\(SA=a\\sqrt3\\). Find the angle between \\((SBC)\\) and \\((ABCD)\\).', 'Hình chóp \\(S.ABCD\\) có đáy là hình vuông cạnh \\(a\\), \\(SA\\perp(ABCD)\\), \\(SA=a\\sqrt3\\). Tính góc giữa \\((SBC)\\) và \\((ABCD)\\).'),
  T('Common line \\(BC\\); \\(AB\\perp BC\\), \\(SB\\perp BC\\).', 'Giao tuyến \\(BC\\); \\(AB\\perp BC\\), \\(SB\\perp BC\\).'), [T('The angle is \\(\\widehat{SBA}\\): \\(\\tan\\widehat{SBA}=\\dfrac{a\\sqrt3}{a}=\\sqrt3\\).', 'Góc cần tìm là \\(\\widehat{SBA}\\): \\(\\tan\\widehat{SBA}=\\dfrac{a\\sqrt3}{a}=\\sqrt3\\).')], T('\\(60^\\circ\\).', '\\(60^\\circ\\).'))
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('A regular pyramid', 'Hình chóp đều'), T('Regular pyramid \\(S.ABCD\\) with base side \\(a\\) and height \\(SO=\\dfrac{a\\sqrt3}2\\). Find the angle between a lateral face and the base, and the slant height \\(SM\\).', 'Hình chóp tứ giác đều \\(S.ABCD\\) có cạnh đáy \\(a\\), chiều cao \\(SO=\\dfrac{a\\sqrt3}2\\). Tính góc giữa mặt bên và mặt đáy và trung đoạn \\(SM\\).'),
  T('\\(M\\) the midpoint of \\(CD\\), \\(OM=\\frac a2\\).', '\\(M\\) là trung điểm \\(CD\\), \\(OM=\\frac a2\\).'), [T('\\(\\tan\\widehat{SMO}=\\dfrac{a\\sqrt3/2}{a/2}=\\sqrt3\\Rightarrow60^\\circ\\).', '\\(\\tan\\widehat{SMO}=\\dfrac{a\\sqrt3/2}{a/2}=\\sqrt3\\Rightarrow60^\\circ\\).'), T('\\(SM=\\sqrt{SO^2+OM^2}=\\sqrt{\\frac{3a^2}4+\\frac{a^2}4}=a\\).', '\\(SM=\\sqrt{SO^2+OM^2}=\\sqrt{\\frac{3a^2}4+\\frac{a^2}4}=a\\).')],
  T('\\(60^\\circ\\); \\(SM=a\\).', '\\(60^\\circ\\); \\(SM=a\\).'))
assert math.isclose(math.degrees(math.atan(math.sqrt(2))), 54.74, abs_tol=0.01)
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('A plane through a cube', 'Mặt phẳng cắt hình lập phương'), T('Cube \\(ABCD.A\'B\'C\'D\'\\) with edge \\(a\\). Find the angle between \\((A\'BD)\\) and \\((ABCD)\\).', 'Hình lập phương \\(ABCD.A\'B\'C\'D\'\\) cạnh \\(a\\). Tính góc giữa \\((A\'BD)\\) và \\((ABCD)\\).'),
  T('Common line \\(BD\\); \\(O\\) the centre of \\(ABCD\\).', 'Giao tuyến \\(BD\\); \\(O\\) là tâm hình vuông \\(ABCD\\).'), [T('\\(AO\\perp BD\\), \\(A\'O\\perp BD\\) (\\(BD\\perp(AA\'O)\\)): the angle is \\(\\widehat{A\'OA}\\).', '\\(AO\\perp BD\\), \\(A\'O\\perp BD\\) (vì \\(BD\\perp(AA\'O)\\)): góc cần tìm là \\(\\widehat{A\'OA}\\).'), T('\\(\\tan\\widehat{A\'OA}=\\dfrac{a}{a\\sqrt2/2}=\\sqrt2\\).', '\\(\\tan\\widehat{A\'OA}=\\dfrac{a}{a\\sqrt2/2}=\\sqrt2\\).')],
  T('\\(\\tan\\varphi=\\sqrt2\\), \\(\\varphi\\approx54{,}74^\\circ\\).', '\\(\\tan\\varphi=\\sqrt2\\), \\(\\varphi\\approx54{,}74^\\circ\\).'))
examples = EXFIG(examples, 4, GEO3D(fig('cube', pts={'O': 'mid:A,C'}, seg=[['A′', 'B'], ['A′', 'D'], ['B', 'D', {'color': GR}], ['A', 'O', {'color': BL}], ['A′', 'O', {'color': HL}]], poly=[FILL(['A′', 'B', 'D'], '#fde68a', .45)], angles=[['A′', 'O', 'A']]), alt=('Plane A′BD in a cube and the angle A′OA', '')))
assert math.isclose(math.degrees(math.acos(0.8)), 36.87, abs_tol=0.01) and 2 * 5 * 10 == 100 and 100 * 0.8 == 80
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Roof pitch and roof area', 'Độ dốc và diện tích mái'), T('A house is 8 m wide and 10 m long. Its gable roof rises 3 m from the eaves to the ridge. Find the angle between each roof plane and the ceiling, and the area of roofing sheets needed.', 'Một ngôi nhà rộng 8 m, dài 10 m, mái hai mái có nóc cao hơn mép mái 3 m. Tính góc giữa mỗi mặt mái và mặt trần, và diện tích tôn lợp cần dùng.'),
  T('Cut perpendicular to the ridge: a right triangle with legs 4 m and 3 m.', 'Cắt vuông góc với nóc: tam giác vuông có hai cạnh góc vuông 4 m và 3 m.'),
  [T('Roof slope length \\(=\\sqrt{4^2+3^2}=5\\) m; \\(\\cos\\varphi=\\dfrac45\\Rightarrow\\varphi\\approx36{,}87^\\circ\\).', 'Chiều dài dốc mái \\(=\\sqrt{4^2+3^2}=5\\) m; \\(\\cos\\varphi=\\dfrac45\\Rightarrow\\varphi\\approx36{,}87^\\circ\\).'),
   T('Area \\(=2\\cdot5\\cdot10=100\\) m². Check: its projection on the ceiling is \\(8\\cdot10=80=100\\cos\\varphi\\) m².', 'Diện tích \\(=2\\cdot5\\cdot10=100\\) m². Kiểm tra: hình chiếu trên trần có diện tích \\(8\\cdot10=80=100\\cos\\varphi\\) m².')],
  T('About \\(36{,}87^\\circ\\); 100 m² of sheets.', 'Khoảng \\(36{,}87^\\circ\\); 100 m² tôn.'))


def lvl(P):
    k, sa, d = P['dih']
    o1 = M4(1, '\\(S.ABCD\\): square base of side %d, \\(SA\\perp(ABCD)\\), \\(SA=%s\\). The angle between \\((SBC)\\) and \\((ABCD)\\) is…' % (k, sa), 'Hình chóp \\(S.ABCD\\) có đáy là hình vuông cạnh %d, \\(SA\\perp(ABCD)\\), \\(SA=%s\\). Góc giữa \\((SBC)\\) và \\((ABCD)\\) bằng…' % (k, sa), '\\(%d^\\circ\\)' % d,
            ['\\(%d^\\circ\\)' % x for x in (30, 45, 60, 90) if x != d], 'The angle is \\(\\widehat{SBA}\\).', 'Góc cần tìm là \\(\\widehat{SBA}\\), \\(\\tan\\widehat{SBA}=\\dfrac{SA}{AB}\\).')
    k2, so, d2 = P['reg']
    o2 = M4(2, 'Regular pyramid \\(S.ABCD\\): base side %d, height \\(%s\\). The angle between a lateral face and the base is…' % (k2, so), 'Hình chóp tứ giác đều \\(S.ABCD\\) có cạnh đáy %d, chiều cao \\(%s\\). Góc giữa mặt bên và mặt đáy bằng…' % (k2, so), '\\(%d^\\circ\\)' % d2,
            ['\\(%d^\\circ\\)' % x for x in (30, 45, 60, 90) if x != d2], '\\(\\tan\\widehat{SMO}=\\dfrac{SO}{OM}\\), \\(OM=%d\\).' % (k2 // 2), '\\(\\tan\\widehat{SMO}=\\dfrac{SO}{OM}\\) với \\(OM=%d\\).' % (k2 // 2))
    p, q, bad = P['which']
    o3 = M4(3, '\\(S.ABCD\\): square base, \\(SA\\perp(ABCD)\\). Which plane is perpendicular to \\(%s\\)?' % q, 'Hình chóp \\(S.ABCD\\) có đáy hình vuông, \\(SA\\perp(ABCD)\\). Mặt phẳng nào vuông góc với \\(%s\\)?' % q, '\\(%s\\)' % p, ['\\(%s\\)' % b for b in bad],
            'It contains a line perpendicular to \\(%s\\).' % q, 'Mặt phẳng đó chứa một đường thẳng vuông góc với \\(%s\\).' % q)
    (se, sv), val = P['stmt']
    t4 = tf(4, se, sv, val, 'Recall the criterion.', 'Nhớ lại điều kiện hai mặt phẳng vuông góc.')
    (de, dv), v5 = P['defn']
    t5 = tf(5, de, dv, v5, 'Recall the definitions.', 'Nhớ lại định nghĩa các hình đặc biệt.')
    h, half, sm = P['apo']
    s6 = sh(6, 'Regular pyramid \\(S.ABCD\\): base side %d, height %d. Find the slant height \\(SM\\).' % (2 * half, h), 'Hình chóp tứ giác đều \\(S.ABCD\\) có cạnh đáy %d, chiều cao %d. Tính trung đoạn \\(SM\\).' % (2 * half, h), sm,
            '\\(SM=\\sqrt{SO^2+OM^2}\\).', '\\(SM=\\sqrt{%d+%d}=%d\\).' % (h * h, half * half, sm))
    w, rise, L, sl = P['roof']
    s7 = sh(7, 'A house %d m wide and %d m long has a gable roof whose ridge is %d m above the eaves. How many square metres of roofing are needed?' % (w, L, rise), 'Ngôi nhà rộng %d m, dài %d m, mái hai mái có nóc cao hơn mép mái %d m. Cần bao nhiêu mét vuông tôn lợp?' % (w, L, rise), 2 * sl * L,
            'Slope length \\(\\sqrt{%d^2+%d^2}=%d\\).' % (w // 2, rise, sl), 'Dốc mái dài \\(\\sqrt{%d^2+%d^2}=%d\\) m; diện tích \\(2\\cdot%d\\cdot%d=%d\\) m².' % (w // 2, rise, sl, sl, L, 2 * sl * L))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]


STM = [(('If \\((P)\\) contains a line perpendicular to \\((Q)\\), then \\((P)\\perp(Q)\\).', 'Nếu \\((P)\\) chứa một đường thẳng vuông góc với \\((Q)\\) thì \\((P)\\perp(Q)\\).'), True),
       (('If \\((P)\\perp(Q)\\), every line of \\((P)\\) is perpendicular to \\((Q)\\).', 'Nếu \\((P)\\perp(Q)\\) thì mọi đường thẳng nằm trong \\((P)\\) đều vuông góc với \\((Q)\\).'), False),
       (('Two planes perpendicular to the same plane are always parallel.', 'Hai mặt phẳng cùng vuông góc với một mặt phẳng thì luôn song song với nhau.'), False)]
DEF = [(('The lateral faces of a right prism are rectangles.', 'Các mặt bên của hình lăng trụ đứng là hình chữ nhật.'), True),
       (('The bases of a right box are always rectangles.', 'Hai đáy của hình hộp đứng luôn là hình chữ nhật.'), False),
       (('All lateral edges of a regular pyramid are equal.', 'Các cạnh bên của hình chóp đều bằng nhau.'), True)]
PP = [dict(dih=(3, '3\\sqrt3', 60), reg=(4, '2', 45), which=S.PERP_PL[0], stmt=STM[0], defn=DEF[0], apo=(3, 4, 5), roof=(8, 3, 12, 5)),
      dict(dih=(4, '4', 45), reg=(6, '3\\sqrt3', 60), which=S.PERP_PL[2], stmt=STM[1], defn=DEF[1], apo=(12, 5, 13), roof=(12, 8, 15, 10)),
      dict(dih=(6, '2\\sqrt3', 30), reg=(6, '\\sqrt3', 30), which=S.PERP_PL[3], stmt=STM[2], defn=DEF[2], apo=(8, 6, 10), roof=(16, 6, 20, 10))]
for pp in PP:
    k, sa, d = pp['dih']; v = {'3\\sqrt3': 3 * 3 ** .5, '4': 4, '2\\sqrt3': 2 * 3 ** .5}[sa]; assert round(math.degrees(math.atan(v / k))) == d
    k2, so, d2 = pp['reg']; v2 = {'2': 2, '3\\sqrt3': 3 * 3 ** .5, '\\sqrt3': 3 ** .5}[so]; assert round(math.degrees(math.atan(v2 / (k2 / 2)))) == d2
    w, rise, L, sl = pp['roof']; assert (w // 2) ** 2 + rise ** 2 == sl ** 2
practice = three(lvl, PP)
practice = with_self(practice, S.M25S11, start=8)
mistakes = [('<b>Taking the angle between two arbitrary lines of the planes.</b> Both lines must be perpendicular to the common line at the same point.', '<b>Lấy góc giữa hai đường bất kì trong hai mặt phẳng.</b> Hai đường phải cùng vuông góc với giao tuyến tại cùng một điểm.'),
            ('<b>Using \\(SC\\) for the angle between \\((SBC)\\) and the base.</b> \\(SC\\) is not perpendicular to \\(BC\\); use \\(SB\\).', '<b>Dùng \\(SC\\) cho góc giữa \\((SBC)\\) và đáy.</b> \\(SC\\) không vuông góc với \\(BC\\); phải dùng \\(SB\\).'),
            ('<b>In a regular pyramid, joining \\(S\\) to a vertex.</b> For the face angle use the midpoint \\(M\\) of a base edge.', '<b>Với hình chóp đều, nối \\(S\\) với một đỉnh.</b> Góc mặt bên – đáy dùng trung điểm \\(M\\) của cạnh đáy.'),
            ('<b>"Perpendicular planes" means every line is perpendicular.</b> Only lines perpendicular to the common line are.', '<b>Nghĩ rằng hai mặt vuông góc thì mọi đường đều vuông góc.</b> Chỉ những đường vuông góc với giao tuyến mới vuông góc với mặt kia.')]
summary = [('Angle between planes: at a point of the common line, take a line in each plane perpendicular to it.', 'Góc giữa hai mặt phẳng: tại một điểm của giao tuyến, lấy trong mỗi mặt một đường vuông góc với giao tuyến.'),
           ('\\((P)\\perp(Q)\\iff(P)\\) contains a line \\(\\perp(Q)\\).', '\\((P)\\perp(Q)\\iff(P)\\) chứa một đường thẳng vuông góc với \\((Q)\\).'),
           ('Regular pyramid: apex above the centre; face angle \\(\\widehat{SMO}\\), \\(SM=\\sqrt{SO^2+OM^2}\\).', 'Hình chóp đều: đỉnh chiếu xuống tâm đáy; góc mặt bên \\(\\widehat{SMO}\\), \\(SM=\\sqrt{SO^2+OM^2}\\).'),
           ('Key words: angle between planes, dihedral angle, perpendicular planes, regular pyramid, right prism.', 'Từ cần nhớ: angle between planes, dihedral angle, perpendicular planes, regular pyramid, right prism.')]
checks = [('I can find the angle between two planes.', 'Em xác định được góc giữa hai mặt phẳng.'), ('I can prove two planes are perpendicular.', 'Em chứng minh được hai mặt phẳng vuông góc.'),
          ('I know the special prisms and pyramids.', 'Em nhận biết được các hình lăng trụ, hình chóp đặc biệt.'), ('I can compute a roof pitch.', 'Em tính được độ dốc mái nhà.')]
LL('g11-perp-04', 'Perpendicular Planes', CV, ('Perpendicularity in Space', 'Quan hệ vuông góc trong không gian'), 'perpendicularity-in-space', 'perpendicular-planes', 260, 'Intermediate', 75, ('projection, angle between a line and a plane', 'phép chiếu vuông góc, góc giữa đường thẳng và mặt phẳng'),
   'Angle between two planes, dihedral angles, perpendicular planes; right prisms, boxes, regular pyramids and frustums.', 'Bài 25 – Góc giữa hai mặt phẳng, góc nhị diện, hai mặt phẳng vuông góc; lăng trụ đứng, hình hộp, hình chóp đều, chóp cụt đều.',
   ['angle between planes', 'dihedral angle', 'perpendicular planes'], ['góc giữa hai mặt phẳng', 'góc nhị diện', 'hai mặt phẳng vuông góc'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g11-perp-03'])
