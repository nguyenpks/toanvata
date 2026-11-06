# -*- coding: utf-8 -*-
"""g12-coord-06 = Toán 12 KNTT, Bài 17: Phương trình mặt cầu. Mã ngân hàng câu hỏi: TOAN12-C5-B17.
Mỗi mức 22 câu: 7 câu soạn sẵn + 15 câu tự luyện (bài lớp 12 khối lượng lớn)."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g12f as S
from sp_g12f import sph, gen
from sp_g12d import eq, V3, dot, sub

CV = 'Phương trình mặt cầu'
vocab = defs(CV, [
 ('sphere', 'sphere', 'mặt cầu', 'the set of points \\(M\\) in space with \\(IM=R\\) (centre \\(I\\), radius \\(R\\gt0\\)).', 'tập hợp các điểm \\(M\\) trong không gian có \\(IM=R\\) (tâm \\(I\\), bán kính \\(R\\gt0\\)).', 'The sphere has centre I and radius 3.', '\\((S)\\)'),
 ('sphgen', 'general equation of a sphere', 'phương trình tổng quát của mặt cầu', '\\(x^2+y^2+z^2-2ax-2by-2cz+d=0\\) with \\(a^2+b^2+c^2-d\\gt0\\).', '\\(x^2+y^2+z^2-2ax-2by-2cz+d=0\\) với \\(a^2+b^2+c^2-d\\gt0\\).', 'Find the centre from the general equation.', ''),
 ('tanplane', 'tangent plane', 'tiếp diện', 'a plane with exactly one common point with the sphere; then \\(d(I,(P))=R\\).', 'mặt phẳng có đúng một điểm chung với mặt cầu; khi đó \\(d(I,(P))=R\\).', 'The plane is tangent to the sphere.', ''),
 ('secircle', 'cross-section circle', 'đường tròn giao tuyến', 'the circle where a plane cuts a sphere; radius \\(r=\\sqrt{R^2-d^2}\\).', 'đường tròn là giao của mặt phẳng và mặt cầu; bán kính \\(r=\\sqrt{R^2-d^2}\\).', 'The plane cuts the sphere along a circle of radius 4.', '')])
goals = [('recognise the equation of a sphere and read its centre and radius;', 'nhận biết phương trình [[mặt cầu]], xác định tâm và bán kính;'),
         ('write the equation of a sphere from given conditions (centre and point, diameter, tangent plane);', 'viết phương trình mặt cầu khi biết tâm và một điểm, đường kính, tiếp diện;'),
         ('decide the position of a point, a plane or a line relative to a sphere;', 'xét vị trí tương đối của điểm, mặt phẳng, đường thẳng với mặt cầu;'),
         ('solve problems on tangency and cross-sections, including real situations.', 'giải bài toán về [[tiếp diện]], [[đường tròn giao tuyến]], kể cả tình huống thực tế.')]
phrases = [('<b>The sphere has centre \\(I\\) and radius three.</b>', 'Mặt cầu có tâm \\(I\\), bán kính 3.'), ('<b>The distance from the centre to the plane equals the radius.</b>', 'Khoảng cách từ tâm đến mặt phẳng bằng bán kính.'),
           ('<b>The plane cuts the sphere along a circle.</b>', 'Mặt phẳng cắt mặt cầu theo một đường tròn.'), ('<b>The point lies inside the sphere.</b>', 'Điểm nằm trong mặt cầu.'), ('<b>Complete the squares.</b>', 'Đưa về tổng các bình phương.')]
review = T('From Bài 14–15: \\(d(M,(P))=\\dfrac{|Ax_0+By_0+Cz_0+D|}{\\sqrt{A^2+B^2+C^2}}\\); \\(AB=\\sqrt{(x_B-x_A)^2+(y_B-y_A)^2+(z_B-z_A)^2}\\); midpoint \\(\\left(\\frac{x_A+x_B}2;\\frac{y_A+y_B}2;\\frac{z_A+z_B}2\\right)\\); the foot of the perpendicular from \\(I\\) to \\((P)\\) is \\(I+t\\vec n\\).',
           'Từ Bài 14–15: \\(d(M,(P))=\\dfrac{|Ax_0+By_0+Cz_0+D|}{\\sqrt{A^2+B^2+C^2}}\\); \\(AB=\\sqrt{(x_B-x_A)^2+(y_B-y_A)^2+(z_B-z_A)^2}\\); trung điểm \\(\\left(\\frac{x_A+x_B}2;\\frac{y_A+y_B}2;\\frac{z_A+z_B}2\\right)\\); hình chiếu của \\(I\\) trên \\((P)\\) có dạng \\(I+t\\vec n\\).')
theory = '<h3>17.1 %s</h3>' % TI('Equation of a sphere', 'Phương trình mặt cầu')
theory += BOX('blue', ('Two forms', 'Hai dạng phương trình'), UL([T('Centre \\(I(a;b;c)\\), radius \\(R\\): \\[(x-a)^2+(y-b)^2+(z-c)^2=R^2.\\]', 'Tâm \\(I(a;b;c)\\), bán kính \\(R\\): \\[(x-a)^2+(y-b)^2+(z-c)^2=R^2.\\]'),
  T('\\(x^2+y^2+z^2-2ax-2by-2cz+d=0\\) is a sphere \\(\\iff a^2+b^2+c^2-d\\gt0\\); then \\(I(a;b;c)\\), \\(R=\\sqrt{a^2+b^2+c^2-d}\\). (The coefficients of \\(x^2,y^2,z^2\\) must be equal and there are no \\(xy,yz,zx\\) terms.)', '\\(x^2+y^2+z^2-2ax-2by-2cz+d=0\\) là mặt cầu \\(\\iff a^2+b^2+c^2-d\\gt0\\); khi đó \\(I(a;b;c)\\), \\(R=\\sqrt{a^2+b^2+c^2-d}\\). (Hệ số của \\(x^2,y^2,z^2\\) bằng nhau và không có số hạng \\(xy,yz,zx\\).)')]))
theory += BOX('mint', ('Point and sphere', 'Vị trí của điểm và mặt cầu'), T('\\(IM\\lt R\\): \\(M\\) is inside; \\(IM=R\\): \\(M\\) is on the sphere; \\(IM\\gt R\\): \\(M\\) is outside.', '\\(IM\\lt R\\): \\(M\\) nằm trong; \\(IM=R\\): \\(M\\) nằm trên mặt cầu; \\(IM\\gt R\\): \\(M\\) nằm ngoài.'))
theory += '<h3>17.2 %s</h3>' % TI('Planes, lines and spheres', 'Vị trí tương đối của mặt phẳng, đường thẳng với mặt cầu')
theory += TBL([TI('\\(d=d(I,(P))\\)', '\\(d=d(I,(P))\\)'), TI('Position', 'Vị trí'), TI('Common points', 'Điểm chung')], [
  ['\\(d\\gt R\\)', TI('no common point', 'không cắt nhau'), TI('none', 'không có')],
  ['\\(d=R\\)', TI('tangent (\\((P)\\) is a tangent plane)', 'tiếp xúc (\\((P)\\) là tiếp diện)'), TI('one point: the foot \\(H\\) of the perpendicular from \\(I\\)', 'một điểm: hình chiếu \\(H\\) của \\(I\\) trên \\((P)\\)')],
  ['\\(d\\lt R\\)', TI('cut along a circle', 'cắt theo một đường tròn'), TI('circle with centre \\(H\\), radius \\(r=\\sqrt{R^2-d^2}\\)', 'đường tròn tâm \\(H\\), bán kính \\(r=\\sqrt{R^2-d^2}\\)')]])
theory += BOX('mint', ('Line and sphere', 'Đường thẳng và mặt cầu'), T('Substitute the parametric equations into the sphere: a quadratic in \\(t\\) with 2, 1 or 0 roots \\(\\iff\\) the line cuts the sphere at 2 points, is tangent, or misses it (equivalently \\(d(I,\\Delta)\\lt R\\), \\(=R\\), \\(\\gt R\\)).', 'Thay phương trình tham số vào phương trình mặt cầu: được phương trình bậc hai theo \\(t\\) có 2, 1 hoặc 0 nghiệm \\(\\iff\\) đường thẳng cắt mặt cầu tại 2 điểm, tiếp xúc hoặc không cắt (tương đương \\(d(I,\\Delta)\\lt R\\), \\(=R\\), \\(\\gt R\\)).'))
FIGS = {'points': {'I': (0, 0, 0), 'H': (0, 0, 3), 'M': (4, 0, 3), '_p1': (-6.5, -5, 3), '_p2': (6.5, -5, 3), '_p3': (6.5, 5, 3), '_p4': (-6.5, 5, 3)}, 'oblique': (0.5, 35),
        'spheres': [{'c': 'I', 'R': 5}], 'hcircles': [{'c': 'I', 'R': 5, 'color': '#64748b'}, {'c': 'H', 'R': 4, 'color': '#c2410c'}],
        'polygons': [{'points': ['_p1', '_p2', '_p3', '_p4'], 'fill': '#93c5fd', 'opacity': .25, 'outline': True}],
        'segments': [['I', 'H', {'color': '#1d4ed8', 'width': 3, 'dash': True, 'force': True}], ['H', 'M', {'color': '#c2410c', 'width': 3}], ['I', 'M', {'color': '#0f766e', 'width': 3, 'dash': True, 'force': True}]],
        'right': [['I', 'H', 'M']], 'rsize': 0.5, 'labelpos': {'I': 'left', 'H': 'above left', 'M': 'right'}, 'px': 400}
theory += GEO3D(FIGS, cap=('Sphere of radius \\(R=IM=5\\) cut by a plane at distance \\(d=IH=3\\) from the centre: the cross-section is a circle with centre \\(H\\) and radius \\(r=HM=\\sqrt{5^2-3^2}=4\\).', 'Mặt cầu bán kính \\(R=IM=5\\) bị cắt bởi mặt phẳng cách tâm \\(d=IH=3\\): giao tuyến là đường tròn tâm \\(H\\), bán kính \\(r=HM=\\sqrt{5^2-3^2}=4\\).'), alt=('A sphere cut by a horizontal plane along a circle', ''))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('In \\(x^2+y^2+z^2-4x+\\ldots\\) the centre has \\(a=2\\) (half the coefficient, opposite sign). The right side of the standard form is \\(R^2\\), not \\(R\\). Always check \\(a^2+b^2+c^2-d\\gt0\\) before calling an equation a sphere.', 'Trong \\(x^2+y^2+z^2-4x+\\ldots\\) tâm có \\(a=2\\) (một nửa hệ số, đổi dấu). Vế phải của dạng chính tắc là \\(R^2\\), không phải \\(R\\). Luôn kiểm tra \\(a^2+b^2+c^2-d\\gt0\\) trước khi kết luận là mặt cầu.'))

assert 4 + 1 + 9 - 5 == 9
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Centre and radius', 'Tâm và bán kính'), T('Find the centre and radius of a) \\((x-1)^2+(y+2)^2+z^2=9\\); b) \\(x^2+y^2+z^2-4x+2y-6z+5=0\\).', 'Tìm tâm và bán kính của mặt cầu a) \\((x-1)^2+(y+2)^2+z^2=9\\); b) \\(x^2+y^2+z^2-4x+2y-6z+5=0\\).'),
  T('a) Read directly. b) \\(a,b,c\\) are minus half the coefficients.', 'a) Đọc trực tiếp. b) \\(a,b,c\\) bằng âm một nửa các hệ số.'),
  [T('a) \\(I(1;-2;0)\\), \\(R=\\sqrt9=3\\).', 'a) \\(I(1;-2;0)\\), \\(R=\\sqrt9=3\\).'), T('b) \\(a=2\\), \\(b=-1\\), \\(c=3\\), \\(d=5\\); \\(R^2=4+1+9-5=9\\).', 'b) \\(a=2\\), \\(b=-1\\), \\(c=3\\), \\(d=5\\); \\(R^2=4+1+9-5=9\\).')],
  T('a) \\(I(1;-2;0)\\), \\(R=3\\); b) \\(I(2;-1;3)\\), \\(R=3\\).', 'a) \\(I(1;-2;0)\\), \\(R=3\\); b) \\(I(2;-1;3)\\), \\(R=3\\).'))
assert dot(sub((3, 0, 0), (1, 2, -1)), sub((3, 0, 0), (1, 2, -1))) == 9 and dot(sub((2, -1, 3), (1, 1, 1)), sub((2, -1, 3), (1, 1, 1))) == 9
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Writing equations', 'Viết phương trình'), T('a) Centre \\(I(1;2;-1)\\), through \\(A(3;0;0)\\). b) Diameter \\(AB\\) with \\(A(2;-1;3)\\), \\(B(0;3;-1)\\).', 'Viết phương trình mặt cầu: a) tâm \\(I(1;2;-1)\\), đi qua \\(A(3;0;0)\\); b) đường kính \\(AB\\) với \\(A(2;-1;3)\\), \\(B(0;3;-1)\\).'),
  T('\\(R=IA\\); for a diameter the centre is the midpoint.', '\\(R=IA\\); với đường kính, tâm là trung điểm.'),
  [T('a) \\(R^2=IA^2=4+4+1=9\\): \\(%s\\).' % sph((1, 2, -1), 9), 'a) \\(R^2=IA^2=4+4+1=9\\): \\(%s\\).' % sph((1, 2, -1), 9)), T('b) \\(I(1;1;1)\\), \\(R^2=IA^2=1+4+4=9\\): \\(%s\\).' % sph((1, 1, 1), 9), 'b) \\(I(1;1;1)\\), \\(R^2=IA^2=1+4+4=9\\): \\(%s\\).' % sph((1, 1, 1), 9))],
  T('a) \\(%s\\); b) \\(%s\\).' % (sph((1, 2, -1), 9), sph((1, 1, 1), 9)), 'a) \\(%s\\); b) \\(%s\\).' % (sph((1, 2, -1), 9), sph((1, 1, 1), 9))))
I3, n3, D3 = (1, -2, 3), (2, -1, 2), -1; d3 = F(abs(dot(n3, I3) + D3), 3); H3 = tuple(i - c for i, c in zip(I3, n3)); assert d3 == 3 and dot(n3, H3) + D3 == 0
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('A tangent plane', 'Mặt cầu tiếp xúc mặt phẳng'), T('Write the sphere with centre \\(I(1;-2;3)\\) tangent to \\((P): 2x-y+2z-1=0\\) and find the point of contact.', 'Viết phương trình mặt cầu tâm \\(I(1;-2;3)\\) tiếp xúc với \\((P): 2x-y+2z-1=0\\) và tìm tiếp điểm.'),
  T('\\(R=d(I,(P))\\); the contact point is the foot of the perpendicular.', '\\(R=d(I,(P))\\); tiếp điểm là hình chiếu của \\(I\\) trên \\((P)\\).'),
  [T('\\(R=\\dfrac{|2+2+6-1|}{3}=3\\): \\(%s\\).' % sph(I3, 9), '\\(R=\\dfrac{|2+2+6-1|}{3}=3\\): \\(%s\\).' % sph(I3, 9)), T('\\(H=I+t\\vec n\\): \\(2(1+2t)-(-2-t)+2(3+2t)-1=0\\iff9+9t=0\\iff t=-1\\), \\(H(-1;-1;1)\\).', '\\(H=I+t\\vec n\\): \\(2(1+2t)-(-2-t)+2(3+2t)-1=0\\iff9+9t=0\\iff t=-1\\), \\(H(-1;-1;1)\\).')],
  T('\\(%s\\); contact point \\(H(-1;-1;1)\\).' % sph(I3, 9), '\\(%s\\); tiếp điểm \\(H(-1;-1;1)\\).' % sph(I3, 9)))
I4, n4, D4 = (1, 1, 2), (1, 2, 2), 2; assert abs(dot(n4, I4) + D4) == 9 and tuple(i - c for i, c in zip(I4, n4)) == (0, -1, 0) and 25 - 9 == 16
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('A cross-section', 'Đường tròn giao tuyến'), T('Show that \\((P): x+2y+2z+2=0\\) cuts \\((S): %s\\) along a circle; find its centre and radius.' % sph(I4, 25), 'Chứng minh \\((P): x+2y+2z+2=0\\) cắt \\((S): %s\\) theo một đường tròn; tìm tâm và bán kính đường tròn đó.' % sph(I4, 25)),
  T('Compare \\(d(I,(P))\\) with \\(R\\).', 'So sánh \\(d(I,(P))\\) với \\(R\\).'), [T('\\(I(1;1;2)\\), \\(R=5\\); \\(d=\\dfrac{|1+2+4+2|}{3}=3\\lt5\\): they cut.', '\\(I(1;1;2)\\), \\(R=5\\); \\(d=\\dfrac{|1+2+4+2|}{3}=3\\lt5\\): cắt nhau.'),
  T('\\(r=\\sqrt{25-9}=4\\); centre \\(H=I-\\vec n=(0;-1;0)\\) (check: \\(0-2+0+2=0\\)).', '\\(r=\\sqrt{25-9}=4\\); tâm \\(H=I-\\vec n=(0;-1;0)\\) (kiểm tra: \\(0-2+0+2=0\\)).')],
  T('Circle with centre \\(H(0;-1;0)\\) and radius 4.', 'Đường tròn tâm \\(H(0;-1;0)\\), bán kính 4.'))
assert 9 + 4 + 1 == 14 < 25 and abs(math.sqrt(21) - 4.58) < 0.01
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Wi-Fi coverage', 'Vùng phủ sóng Wi-Fi'), T('In a room (unit: m, floor \\((Oxy)\\)), a router at \\(I(4;3;2)\\) covers points at most 5 m away. a) Write the boundary sphere. b) Is the desk point \\(D(1;1;1)\\) covered? c) On the floor, the covered region is a disc: find its radius.', 'Trong một phòng (đơn vị mét, sàn là \\((Oxy)\\)), bộ phát Wi-Fi đặt tại \\(I(4;3;2)\\) phủ sóng các điểm cách nó không quá 5 m. a) Viết phương trình mặt cầu biên. b) Điểm \\(D(1;1;1)\\) trên bàn có được phủ sóng không? c) Trên sàn, vùng phủ sóng là một hình tròn: tìm bán kính.'),
  T('b) Compare \\(ID\\) with 5. c) The floor is the plane \\(z=0\\).', 'b) So sánh \\(ID\\) với 5. c) Sàn là mặt phẳng \\(z=0\\).'),
  [T('a) \\(%s\\).' % sph((4, 3, 2), 25), 'a) \\(%s\\).' % sph((4, 3, 2), 25)), T('b) \\(ID^2=9+4+1=14\\lt25\\): covered.', 'b) \\(ID^2=9+4+1=14\\lt25\\): được phủ sóng.'), T('c) \\(d(I,(Oxy))=2\\), \\(r=\\sqrt{25-4}=\\sqrt{21}\\approx4{,}58\\) m.', 'c) \\(d(I,(Oxy))=2\\), \\(r=\\sqrt{25-4}=\\sqrt{21}\\approx4{,}58\\) m.')],
  T('a) \\(%s\\); b) yes; c) about 4.58 m.' % sph((4, 3, 2), 25), 'a) \\(%s\\); b) có; c) khoảng 4,58 m.' % sph((4, 3, 2), 25)))

def lvl(P):
    I1, R1 = P['gen']; d1 = dot(I1, I1) - R1 * R1; nI = tuple(-x for x in I1)
    o1 = M4(1, 'Centre and radius of \\(%s\\):' % gen(I1, d1), 'Tâm và bán kính của mặt cầu \\(%s\\) là…' % gen(I1, d1), '\\(I%s,\\ R=%d\\)' % (V3(I1), R1),
            ['\\(I%s,\\ R=%d\\)' % (V3(nI), R1), '\\(I%s,\\ R=%d\\)' % (V3(I1), R1 * R1), '\\(I%s,\\ R=%d\\)' % (V3(tuple(2 * x for x in I1)), R1)], '\\(R^2=%d\\).' % (R1 * R1), '\\(R^2=a^2+b^2+c^2-d=%d\\).' % (R1 * R1))
    I2, A2 = P['thr']; R2 = dot(sub(A2, I2), sub(A2, I2))
    o2 = M4(2, 'The sphere with centre \\(I%s\\) through \\(A%s\\):' % (V3(I2), V3(A2)), 'Mặt cầu tâm \\(I%s\\) đi qua \\(A%s\\) là…' % (V3(I2), V3(A2)), '\\(%s\\)' % sph(I2, R2), ['\\(%s\\)' % sph(A2, R2), '\\(%s\\)' % sph(I2, R2 + 1), '\\(%s\\)' % sph(tuple(-x for x in I2), R2)],
            '\\(R^2=IA^2=%d\\).' % R2, '\\(R^2=IA^2=%d\\).' % R2)
    I3_, R3, n3_, dd = P['pl']; L3 = int(math.isqrt(dot(n3_, n3_))); D3_ = -dot(n3_, I3_) + dd * L3; pos = 0 if dd < R3 else 1 if dd == R3 else 2
    L = [TI('cut along a circle', 'cắt theo một đường tròn'), TI('tangent', 'tiếp xúc'), TI('no common point', 'không có điểm chung')]
    o3 = M4(3, 'Position of \\((S): %s\\) and \\((P): %s\\):' % (sph(I3_, R3 * R3), eq(*n3_, D3_)), 'Vị trí tương đối của \\((S): %s\\) và \\((P): %s\\):' % (sph(I3_, R3 * R3), eq(*n3_, D3_)), L[pos], [L[j] for j in range(3) if j != pos] + [TI('the plane passes through \\(I\\)', 'mặt phẳng đi qua tâm')],
            '\\(d(I,(P))=%d\\), \\(R=%d\\).' % (dd, R3), '\\(d(I,(P))=%d\\), \\(R=%d\\).' % (dd, R3))
    I4_, m4 = P['cond']; k4 = dot(I4_, I4_); truth4 = m4 < k4
    t4 = tf(4, '\\(%s\\) is the equation of a sphere.' % gen(I4_, m4), '\\(%s\\) là phương trình của một mặt cầu.' % gen(I4_, m4), truth4, '\\(a^2+b^2+c^2-d=%d\\).' % (k4 - m4), '\\(a^2+b^2+c^2-d=%d\\).' % (k4 - m4))
    I5, R5, A5 = P['on']; truth5 = dot(sub(A5, I5), sub(A5, I5)) == R5 * R5
    t5 = tf(5, 'The point \\(A%s\\) lies on \\(%s\\).' % (V3(A5), sph(I5, R5 * R5)), 'Điểm \\(A%s\\) thuộc mặt cầu \\(%s\\).' % (V3(A5), sph(I5, R5 * R5)), truth5,
            '\\(IA^2=%d\\).' % dot(sub(A5, I5), sub(A5, I5)), '\\(IA^2=%d\\), \\(R^2=%d\\).' % (dot(sub(A5, I5), sub(A5, I5)), R5 * R5))
    I6, n6, D6 = P['tan']; L6 = int(math.isqrt(dot(n6, n6))); R6 = F(abs(dot(n6, I6) + D6), L6); assert R6.denominator == 1
    s6 = sh(6, 'Find the radius of the sphere with centre \\(I%s\\) tangent to \\((P): %s\\).' % (V3(I6), eq(*n6, D6)), 'Tìm bán kính mặt cầu tâm \\(I%s\\) tiếp xúc với \\((P): %s\\).' % (V3(I6), eq(*n6, D6)), int(R6),
            '\\(R=\\dfrac{|%d|}{%d}=%d\\).' % (dot(n6, I6) + D6, L6, R6), '\\(R=d(I,(P))=\\dfrac{|%d|}{%d}=%d\\).' % (dot(n6, I6) + D6, L6, R6))
    R7, d7, h7 = P['sec']; r7 = int(math.isqrt(R7 * R7 - d7 * d7)); assert r7 * r7 == R7 * R7 - d7 * d7
    s7 = sh(7, 'A ball of radius %d cm is cut by a plane %d cm from its centre. Find the radius of the cut (cm).' % (R7, d7), 'Một quả cầu bán kính %d cm bị cắt bởi mặt phẳng cách tâm %d cm. Tính bán kính của mặt cắt (cm).' % (R7, d7), r7,
            '\\(r=\\sqrt{%d-%d}=%d\\).' % (R7 * R7, d7 * d7, r7), '\\(r=\\sqrt{R^2-d^2}=\\sqrt{%d-%d}=%d\\).' % (R7 * R7, d7 * d7, r7))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
PP = [dict(gen=((1, -2, 2), 2), thr=((0, 1, -1), (2, 3, 0)), pl=((1, 0, 2), 3, (1, 2, 2), 2), cond=((1, 2, -1), 7), on=((1, 0, -2), 3, (2, 2, 0)), tan=((1, 1, 1), (2, 1, 2), 4), sec=(10, 6, 0)),
      dict(gen=((2, 1, -3), 3), thr=((1, -1, 2), (3, 1, 3)), pl=((0, 2, -1), 4, (2, -1, 2), 4), cond=((2, -1, 0), 6), on=((0, 1, 1), 5, (3, 5, 2)), tan=((2, -1, 0), (1, -2, 2), 5), sec=(13, 5, 0)),
      dict(gen=((-1, 3, 1), 4), thr=((2, 0, 1), (0, 1, 3)), pl=((1, 1, 1), 2, (2, 1, -2), 3), cond=((3, 0, -1), 9), on=((2, -1, 1), 3, (4, 0, 3)), tan=((0, 2, -1), (2, 2, -1), 13), sec=(17, 8, 0))]
practice = three(lvl, PP)
practice = with_self(practice, S.M17S12, start=8)
mistakes = [('<b>Sign of the centre.</b> \\((x+2)^2\\) means \\(a=-2\\); \\(-4x\\) in the general form means \\(a=2\\).', '<b>Sai dấu tọa độ tâm.</b> \\((x+2)^2\\) ứng với \\(a=-2\\); \\(-4x\\) trong dạng tổng quát ứng với \\(a=2\\).'),
            ('<b>Writing \\(R\\) instead of \\(R^2\\) on the right side.</b>', '<b>Viết \\(R\\) thay cho \\(R^2\\) ở vế phải.</b>'),
            ('<b>Forgetting the condition \\(a^2+b^2+c^2-d\\gt0\\).</b> \\(x^2+y^2+z^2+1=0\\) is not a sphere.', '<b>Quên điều kiện \\(a^2+b^2+c^2-d\\gt0\\).</b> \\(x^2+y^2+z^2+1=0\\) không phải mặt cầu.'),
            ('<b>Using \\(r=R-d\\) for a cross-section.</b> Pythagoras: \\(r=\\sqrt{R^2-d^2}\\).', '<b>Tính bán kính giao tuyến \\(r=R-d\\).</b> Theo Pythagore: \\(r=\\sqrt{R^2-d^2}\\).')]
summary = [('\\((x-a)^2+(y-b)^2+(z-c)^2=R^2\\): centre \\(I(a;b;c)\\), radius \\(R\\).', '\\((x-a)^2+(y-b)^2+(z-c)^2=R^2\\): tâm \\(I(a;b;c)\\), bán kính \\(R\\).'),
           ('\\(x^2+y^2+z^2-2ax-2by-2cz+d=0\\): sphere iff \\(a^2+b^2+c^2-d\\gt0\\), \\(R=\\sqrt{a^2+b^2+c^2-d}\\).', '\\(x^2+y^2+z^2-2ax-2by-2cz+d=0\\): là mặt cầu khi \\(a^2+b^2+c^2-d\\gt0\\), \\(R=\\sqrt{a^2+b^2+c^2-d}\\).'),
           ('Plane: \\(d\\gt R\\) no common point; \\(d=R\\) tangent; \\(d\\lt R\\) circle of radius \\(\\sqrt{R^2-d^2}\\).', 'Mặt phẳng: \\(d\\gt R\\) không cắt; \\(d=R\\) tiếp xúc; \\(d\\lt R\\) cắt theo đường tròn bán kính \\(\\sqrt{R^2-d^2}\\).'),
           ('Key words: sphere, centre, radius, tangent plane, cross-section.', 'Từ cần nhớ: sphere, centre, radius, tangent plane, cross-section.')]
checks = [('I can read the centre and radius of a sphere.', 'Em xác định được tâm và bán kính mặt cầu.'), ('I can write the equation of a sphere from given conditions.', 'Em viết được phương trình mặt cầu theo điều kiện cho trước.'),
          ('I can decide the position of a plane and a sphere.', 'Em xét được vị trí tương đối của mặt phẳng và mặt cầu.'), ('I can find a tangent point and a cross-section circle.', 'Em tìm được tiếp điểm và đường tròn giao tuyến.')]
LL('g12-coord-06', 'Equations of a Sphere', CV, ('Coordinate Geometry in Space', 'Phương pháp tọa độ trong không gian'), 'space-coordinates', 'sphere-equations', 170, 'Intermediate', 80, ('equations of planes and lines, distance', 'phương trình mặt phẳng, đường thẳng, khoảng cách'),
   'Standard and general equations of a sphere; positions of points, planes and lines; tangent planes and cross-sections.', 'Bài 17 – Phương trình mặt cầu (chính tắc, tổng quát); vị trí của điểm, mặt phẳng, đường thẳng với mặt cầu; tiếp diện, đường tròn giao tuyến.',
   ['sphere', 'centre', 'radius', 'tangent plane'], ['mặt cầu', 'tâm', 'bán kính', 'tiếp diện'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g12-coord-05'])
