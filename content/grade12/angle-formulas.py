# -*- coding: utf-8 -*-
"""g12-coord-05 = Toán 12 KNTT, Bài 16: Công thức tính góc trong không gian. Mã ngân hàng câu hỏi: TOAN12-C5-B16."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g12e as S
from sp_g12d import eq, V3, cross, dot, sub
from sp_g12e import par, canon, n2

CV = 'Công thức tính góc trong không gian'
vocab = defs(CV, [
 ('angll', 'angle between two lines', 'góc giữa hai đường thẳng (tọa độ)', 'in \\([0^\\circ;90^\\circ]\\): \\(\\cos(d_1,d_2)=\\dfrac{|\\vec u_1\\cdot\\vec u_2|}{|\\vec u_1|\\,|\\vec u_2|}\\).', 'thuộc \\([0^\\circ;90^\\circ]\\): \\(\\cos(d_1,d_2)=\\dfrac{|\\vec u_1\\cdot\\vec u_2|}{|\\vec u_1|\\,|\\vec u_2|}\\).', 'The angle between the two lines is 60 degrees.', ''),
 ('anglp', 'angle between a line and a plane', 'góc giữa đường thẳng và mặt phẳng (tọa độ)', '\\(\\sin(d,(P))=\\dfrac{|\\vec u\\cdot\\vec n|}{|\\vec u|\\,|\\vec n|}\\) – sine, because \\(\\vec n\\) is perpendicular to the plane.', '\\(\\sin(d,(P))=\\dfrac{|\\vec u\\cdot\\vec n|}{|\\vec u|\\,|\\vec n|}\\) – dùng sin vì \\(\\vec n\\) vuông góc với mặt phẳng.', 'The angle between the line and the plane is 30 degrees.', ''),
 ('angpp', 'angle between two planes', 'góc giữa hai mặt phẳng', 'in \\([0^\\circ;90^\\circ]\\): \\(\\cos((P),(Q))=\\dfrac{|\\vec n_1\\cdot\\vec n_2|}{|\\vec n_1|\\,|\\vec n_2|}\\).', 'thuộc \\([0^\\circ;90^\\circ]\\): \\(\\cos((P),(Q))=\\dfrac{|\\vec n_1\\cdot\\vec n_2|}{|\\vec n_1|\\,|\\vec n_2|}\\).', 'The angle between the roof and the ground.', ''),
 ('incl', 'angle of inclination', 'góc nghiêng', 'the angle between a surface (or a line) and the horizontal ground.', 'góc giữa một mặt (hoặc một đường) với mặt đất nằm ngang.', 'The panel has an angle of inclination of about 37 degrees.', '')])
goals = [('compute the angle between two lines from their direction vectors;', 'tính [[góc giữa hai đường thẳng|góc giữa hai đường thẳng (tọa độ)]] theo vectơ chỉ phương;'),
         ('compute the angle between a line and a plane (with sine) and between two planes;', 'tính [[góc giữa đường thẳng và mặt phẳng|góc giữa đường thẳng và mặt phẳng (tọa độ)]] (dùng sin) và [[góc giữa hai mặt phẳng]];'),
         ('put a cube or box in coordinates to compute angles;', 'gắn hệ tọa độ vào hình lập phương, hình hộp để tính góc;'),
         ('find angles of inclination in real situations (roofs, ramps, solar panels).', 'tính [[góc nghiêng]] trong thực tế (mái nhà, dốc, tấm pin mặt trời).')]
phrases = [('<b>The angle between the two lines is sixty degrees.</b>', 'Góc giữa hai đường thẳng bằng \\(60^\\circ\\).'), ('<b>Take the absolute value of the dot product.</b>', 'Lấy giá trị tuyệt đối của tích vô hướng.'), ('<b>For a line and a plane we use the sine.</b>', 'Với đường thẳng và mặt phẳng ta dùng sin.'),
           ('<b>Place the cube in a coordinate system.</b>', 'Gắn hình lập phương vào hệ tọa độ.'), ('<b>The panel is tilted at about thirty-seven degrees.</b>', 'Tấm pin nghiêng khoảng \\(37^\\circ\\).')]
review = T('Grade 12, Bài 7: \\(\\cos(\\vec u,\\vec v)=\\dfrac{\\vec u\\cdot\\vec v}{|\\vec u||\\vec v|}\\) (can be negative). Bài 14–15: normal vector of a plane, direction vector of a line. Grade 11: the angle between two lines lies in \\([0^\\circ;90^\\circ]\\).',
           'Lớp 12, Bài 7: \\(\\cos(\\vec u,\\vec v)=\\dfrac{\\vec u\\cdot\\vec v}{|\\vec u||\\vec v|}\\) (có thể âm). Bài 14–15: vectơ pháp tuyến của mặt phẳng, vectơ chỉ phương của đường thẳng. Lớp 11: góc giữa hai đường thẳng thuộc \\([0^\\circ;90^\\circ]\\).')
CUBE = {'solid': True, 'box': [[-0.3, 1.4], [-0.3, 1.4], [-0.3, 1.4]], 'points': {'A': (0, 0, 0), 'B': (1, 0, 0), 'C': (1, 1, 0), 'D': (0, 1, 0), 'A′': (0, 0, 1), 'B′': (1, 0, 1), 'C′': (1, 1, 1), 'D′': (0, 1, 1)},
        'polygons': [{'points': ['A′', 'B', 'D'], 'fill': '#fde68a', 'opacity': .5}], 'segments': [['A′', 'C', {'color': '#c2410c', 'width': 3, 'dash': True}]]}
theory = '<h3>16.1 %s</h3>' % TI('Angle between two lines', 'Góc giữa hai đường thẳng')
theory += BOX('blue', ('Formula', 'Công thức'), T('If \\(d_1\\), \\(d_2\\) have direction vectors \\(\\vec u_1=(a_1;b_1;c_1)\\), \\(\\vec u_2=(a_2;b_2;c_2)\\), then \\[\\cos(d_1,d_2)=\\dfrac{|\\vec u_1\\cdot\\vec u_2|}{|\\vec u_1|\\,|\\vec u_2|}=\\dfrac{|a_1a_2+b_1b_2+c_1c_2|}{\\sqrt{a_1^2+b_1^2+c_1^2}\\,\\sqrt{a_2^2+b_2^2+c_2^2}}.\\] The absolute value makes the angle lie in \\([0^\\circ;90^\\circ]\\). \\(d_1\\perp d_2\\iff\\vec u_1\\cdot\\vec u_2=0\\).',
  'Nếu \\(d_1\\), \\(d_2\\) có vectơ chỉ phương \\(\\vec u_1=(a_1;b_1;c_1)\\), \\(\\vec u_2=(a_2;b_2;c_2)\\) thì \\[\\cos(d_1,d_2)=\\dfrac{|\\vec u_1\\cdot\\vec u_2|}{|\\vec u_1|\\,|\\vec u_2|}=\\dfrac{|a_1a_2+b_1b_2+c_1c_2|}{\\sqrt{a_1^2+b_1^2+c_1^2}\\,\\sqrt{a_2^2+b_2^2+c_2^2}}.\\] Dấu giá trị tuyệt đối bảo đảm góc thuộc \\([0^\\circ;90^\\circ]\\). \\(d_1\\perp d_2\\iff\\vec u_1\\cdot\\vec u_2=0\\).'))
theory += '<h3>16.2 %s</h3>' % TI('Angle between a line and a plane', 'Góc giữa đường thẳng và mặt phẳng')
theory += BOX('blue', ('Formula', 'Công thức'), T('If \\(d\\) has direction vector \\(\\vec u\\) and \\((P)\\) has normal vector \\(\\vec n\\), then \\[\\sin(d,(P))=\\dfrac{|\\vec u\\cdot\\vec n|}{|\\vec u|\\,|\\vec n|}.\\] Reason: the angle between \\(d\\) and \\(\\vec n\\) is \\(90^\\circ-(d,(P))\\).',
  'Nếu \\(d\\) có vectơ chỉ phương \\(\\vec u\\), \\((P)\\) có vectơ pháp tuyến \\(\\vec n\\) thì \\[\\sin(d,(P))=\\dfrac{|\\vec u\\cdot\\vec n|}{|\\vec u|\\,|\\vec n|}.\\] Lí do: góc giữa \\(d\\) và giá của \\(\\vec n\\) bằng \\(90^\\circ-(d,(P))\\).'))
theory += '<h3>16.3 %s</h3>' % TI('Angle between two planes', 'Góc giữa hai mặt phẳng')
theory += BOX('blue', ('Formula', 'Công thức'), T('If \\((P)\\), \\((Q)\\) have normal vectors \\(\\vec n_1\\), \\(\\vec n_2\\), then \\[\\cos((P),(Q))=\\dfrac{|\\vec n_1\\cdot\\vec n_2|}{|\\vec n_1|\\,|\\vec n_2|}.\\] \\((P)\\perp(Q)\\iff\\vec n_1\\cdot\\vec n_2=0\\). The angle with the ground \\((Oxy)\\) uses \\(\\vec k=(0;0;1)\\).',
  'Nếu \\((P)\\), \\((Q)\\) có vectơ pháp tuyến \\(\\vec n_1\\), \\(\\vec n_2\\) thì \\[\\cos((P),(Q))=\\dfrac{|\\vec n_1\\cdot\\vec n_2|}{|\\vec n_1|\\,|\\vec n_2|}.\\] \\((P)\\perp(Q)\\iff\\vec n_1\\cdot\\vec n_2=0\\). Góc với mặt đất \\((Oxy)\\) dùng \\(\\vec k=(0;0;1)\\).'))
theory += TBL([TI('Angle', 'Góc'), TI('Vectors used', 'Vectơ dùng'), TI('Function', 'Hàm')], [[TI('line – line', 'đường – đường'), '\\(\\vec u_1,\\vec u_2\\)', '\\(\\cos\\)'], [TI('line – plane', 'đường – mặt'), '\\(\\vec u,\\vec n\\)', '\\(\\sin\\)'], [TI('plane – plane', 'mặt – mặt'), '\\(\\vec n_1,\\vec n_2\\)', '\\(\\cos\\)']])
theory += GEO3D(CUBE, cap=('Cube \\(ABCD.A\'B\'C\'D\'\\) of side 1 with \\(A\\) at the origin: the diagonal \\(A\'C\\) (orange, dashed because it runs inside the cube) and the plane \\((A\'BD)\\) (yellow) are used in Example 4. Drag to rotate.', 'Hình lập phương \\(ABCD.A\'B\'C\'D\'\\) cạnh 1, \\(A\\) là gốc tọa độ: đường chéo \\(A\'C\\) (cam, nét đứt vì nằm trong khối) và mặt phẳng \\((A\'BD)\\) (vàng) dùng trong Ví dụ 4. Kéo để xoay hình.'), alt=('A unit cube with a diagonal and a triangular section', ''), height=380)
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('Do not forget the absolute value: the angle between lines or planes is never obtuse. For a line and a plane the formula gives the <b>sine</b>. If \\(\\cos\\) is not a "nice" value, give the angle approximately (e.g. \\(\\approx54{,}74^\\circ\\)).', 'Đừng quên dấu giá trị tuyệt đối: góc giữa hai đường thẳng, hai mặt phẳng không bao giờ tù. Với đường thẳng và mặt phẳng, công thức cho <b>sin</b>. Nếu côsin không phải giá trị "đẹp", ghi góc gần đúng (ví dụ \\(\\approx54{,}74^\\circ\\)).'))

u1, u2 = (1, 1, 0), (0, 1, 1); assert F(dot(u1, u2) ** 2, n2(u1) * n2(u2)) == F(1, 4)
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Two lines', 'Hai đường thẳng'), T('Find the angle between \\(d_1: %s\\) and \\(d_2: %s\\) (parameter \\(s\\)).' % (par((1, 2, 3), u1), par((2, 1, -1), u2).replace('t', 's')), 'Tính góc giữa \\(d_1: %s\\) và \\(d_2: %s\\) (tham số \\(s\\)).' % (par((1, 2, 3), u1), par((2, 1, -1), u2).replace('t', 's'))),
  T('Read the coefficients of \\(t\\) and \\(s\\).', 'Đọc hệ số của \\(t\\) và \\(s\\).'), [T('\\(\\vec u_1=(1;1;0)\\), \\(\\vec u_2=(0;1;1)\\), \\(\\vec u_1\\cdot\\vec u_2=1\\).', '\\(\\vec u_1=(1;1;0)\\), \\(\\vec u_2=(0;1;1)\\), \\(\\vec u_1\\cdot\\vec u_2=1\\).'), T('\\(\\cos=\\dfrac{1}{\\sqrt2\\cdot\\sqrt2}=\\dfrac12\\).', '\\(\\cos=\\dfrac{1}{\\sqrt2\\cdot\\sqrt2}=\\dfrac12\\).')],
  T('\\((d_1,d_2)=60^\\circ\\).', '\\((d_1,d_2)=60^\\circ\\).'))
u, n = (1, 0, 1), (1, 1, 0); assert F(dot(u, n) ** 2, n2(u) * n2(n)) == F(1, 4)
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Line and plane', 'Đường thẳng và mặt phẳng'), T('Find the angle between \\(d: %s\\) and \\((P): x+y-3=0\\).' % par((1, 2, 0), u), 'Tính góc giữa \\(d: %s\\) và \\((P): x+y-3=0\\).' % par((1, 2, 0), u)),
  T('Use the sine formula.', 'Dùng công thức sin.'), [T('\\(\\vec u=(1;0;1)\\), \\(\\vec n=(1;1;0)\\), \\(|\\vec u\\cdot\\vec n|=1\\).', '\\(\\vec u=(1;0;1)\\), \\(\\vec n=(1;1;0)\\), \\(|\\vec u\\cdot\\vec n|=1\\).'), T('\\(\\sin\\varphi=\\dfrac{1}{\\sqrt2\\cdot\\sqrt2}=\\dfrac12\\).', '\\(\\sin\\varphi=\\dfrac{1}{\\sqrt2\\cdot\\sqrt2}=\\dfrac12\\).')],
  T('\\(\\varphi=30^\\circ\\) (not \\(60^\\circ\\)!).', '\\(\\varphi=30^\\circ\\) (không phải \\(60^\\circ\\)!).'))
na, nb = (1, 0, -1), (0, 1, -1); assert F(dot(na, nb) ** 2, n2(na) * n2(nb)) == F(1, 4)
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Two planes', 'Hai mặt phẳng'), T('Find the angle between \\((P): %s\\) and \\((Q): %s\\).' % (eq(*na, 1), eq(*nb, -2)), 'Tính góc giữa hai mặt phẳng \\((P): %s\\) và \\((Q): %s\\).' % (eq(*na, 1), eq(*nb, -2))),
  T('Use the normal vectors.', 'Dùng hai vectơ pháp tuyến.'), [T('\\(\\vec n_1=(1;0;-1)\\), \\(\\vec n_2=(0;1;-1)\\), \\(\\vec n_1\\cdot\\vec n_2=1\\).', '\\(\\vec n_1=(1;0;-1)\\), \\(\\vec n_2=(0;1;-1)\\), \\(\\vec n_1\\cdot\\vec n_2=1\\).'), T('\\(\\cos=\\dfrac{1}{\\sqrt2\\cdot\\sqrt2}=\\dfrac12\\).', '\\(\\cos=\\dfrac{1}{\\sqrt2\\cdot\\sqrt2}=\\dfrac12\\).')],
  T('\\(((P),(Q))=60^\\circ\\).', '\\(((P),(Q))=60^\\circ\\).'))
a1 = math.degrees(math.asin(1 / math.sqrt(3))); a2 = math.degrees(math.acos(1 / math.sqrt(3))); assert abs(a1 - 35.26) < 0.01 and abs(a2 - 54.74) < 0.01 and abs(a1 + a2 - 90) < 1e-9
assert dot((1, 0, 1), (0, 1, 1)) == 1
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Angles in a cube', 'Góc trong hình lập phương'), T('Cube \\(ABCD.A\'B\'C\'D\'\\) with side 1. Find a) the angle between \\(A\'C\\) and \\((ABCD)\\); b) the angle between \\((A\'BD)\\) and \\((ABCD)\\); c) the angle between \\(AB\'\\) and \\(BC\'\\).', 'Cho hình lập phương \\(ABCD.A\'B\'C\'D\'\\) cạnh 1. Tính a) góc giữa \\(A\'C\\) và \\((ABCD)\\); b) góc giữa \\((A\'BD)\\) và \\((ABCD)\\); c) góc giữa \\(AB\'\\) và \\(BC\'\\).'),
  T('\\(A(0;0;0)\\), \\(B(1;0;0)\\), \\(D(0;1;0)\\), \\(A\'(0;0;1)\\); then \\(C(1;1;0)\\), \\(B\'(1;0;1)\\), \\(C\'(1;1;1)\\); \\((ABCD)\\) is \\(z=0\\) with \\(\\vec k=(0;0;1)\\).', '\\(A(0;0;0)\\), \\(B(1;0;0)\\), \\(D(0;1;0)\\), \\(A\'(0;0;1)\\); khi đó \\(C(1;1;0)\\), \\(B\'(1;0;1)\\), \\(C\'(1;1;1)\\); \\((ABCD)\\) là \\(z=0\\), có \\(\\vec k=(0;0;1)\\).'),
  [T('a) \\(\\overrightarrow{A\'C}=(1;1;-1)\\): \\(\\sin\\varphi=\\dfrac{1}{\\sqrt3}\\Rightarrow\\varphi\\approx35{,}26^\\circ\\).', 'a) \\(\\overrightarrow{A\'C}=(1;1;-1)\\): \\(\\sin\\varphi=\\dfrac{1}{\\sqrt3}\\Rightarrow\\varphi\\approx35{,}26^\\circ\\).'),
   T('b) \\((A\'BD): x+y+z-1=0\\), \\(\\vec n=(1;1;1)\\): \\(\\cos=\\dfrac{1}{\\sqrt3}\\Rightarrow\\approx54{,}74^\\circ\\).', 'b) \\((A\'BD): x+y+z-1=0\\), \\(\\vec n=(1;1;1)\\): \\(\\cos=\\dfrac{1}{\\sqrt3}\\Rightarrow\\approx54{,}74^\\circ\\).'),
   T('c) \\(\\overrightarrow{AB\'}=(1;0;1)\\), \\(\\overrightarrow{BC\'}=(0;1;1)\\): \\(\\cos=\\dfrac12\\Rightarrow60^\\circ\\).', 'c) \\(\\overrightarrow{AB\'}=(1;0;1)\\), \\(\\overrightarrow{BC\'}=(0;1;1)\\): \\(\\cos=\\dfrac12\\Rightarrow60^\\circ\\).')],
  T('a) \\(\\approx35{,}26^\\circ\\); b) \\(\\approx54{,}74^\\circ\\); c) \\(60^\\circ\\).', 'a) \\(\\approx35{,}26^\\circ\\); b) \\(\\approx54{,}74^\\circ\\); c) \\(60^\\circ\\).'))
g1 = math.degrees(math.acos(F(4, 5))); g2 = math.degrees(math.asin(7 / (5 * math.sqrt(2)))); assert abs(g1 - 36.87) < 0.01 and abs(g2 - 81.87) < 0.01
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Solar panel', 'Tấm pin mặt trời'), T('A solar panel lies in the plane \\((P): 3y+4z-12=0\\) (unit: m, the ground is \\((Oxy)\\)). At noon the sun rays have direction \\(\\vec u=(0;-1;-1)\\). Find the angle of inclination of the panel and the angle between the rays and the panel.', 'Một tấm pin mặt trời nằm trong mặt phẳng \\((P): 3y+4z-12=0\\) (đơn vị mét, mặt đất là \\((Oxy)\\)). Buổi trưa tia nắng có vectơ chỉ phương \\(\\vec u=(0;-1;-1)\\). Tính góc nghiêng của tấm pin và góc giữa tia nắng với tấm pin.'),
  T('Plane – plane with \\(\\vec k\\); line – plane with sine.', 'Mặt – mặt dùng \\(\\vec k\\); đường – mặt dùng sin.'),
  [T('\\(\\vec n=(0;3;4)\\), \\(|\\vec n|=5\\): \\(\\cos=\\dfrac{|4|}{5}=0{,}8\\Rightarrow\\approx36{,}87^\\circ\\).', '\\(\\vec n=(0;3;4)\\), \\(|\\vec n|=5\\): \\(\\cos=\\dfrac{|4|}{5}=0{,}8\\Rightarrow\\approx36{,}87^\\circ\\).'),
   T('\\(\\sin\\varphi=\\dfrac{|0-3-4|}{\\sqrt2\\cdot5}=\\dfrac{7}{5\\sqrt2}\\approx0{,}99\\Rightarrow\\varphi\\approx81{,}87^\\circ\\).', '\\(\\sin\\varphi=\\dfrac{|0-3-4|}{\\sqrt2\\cdot5}=\\dfrac{7}{5\\sqrt2}\\approx0{,}99\\Rightarrow\\varphi\\approx81{,}87^\\circ\\).')],
  T('The panel is tilted about \\(36{,}87^\\circ\\); the rays hit it at about \\(81{,}87^\\circ\\) – almost perpendicular, which is good for collecting energy.', 'Tấm pin nghiêng khoảng \\(36{,}87^\\circ\\); tia nắng tạo với tấm pin góc khoảng \\(81{,}87^\\circ\\) – gần vuông góc, thuận lợi để thu năng lượng.'))

def ang(a, b):
    c2 = F(dot(a, b) ** 2, n2(a) * n2(b)); return {F(0): 90, F(1, 4): 60, F(1, 2): 45, F(3, 4): 30}[c2]
def lvl(P):
    deg = lambda x: '\\(%d^\\circ\\)' % x
    (Ma, ua), (Mb, ub) = P['ll']; g1 = ang(ua, ub)
    o1 = M4(1, 'The angle between \\(%s\\) and \\(%s\\) is…' % (par(Ma, ua), par(Mb, ub).replace('t', 's')), 'Góc giữa hai đường thẳng \\(%s\\) và \\(%s\\) bằng…' % (par(Ma, ua), par(Mb, ub).replace('t', 's')), deg(g1), [deg(x) for x in (30, 45, 60, 90, 120) if x != g1],
            '\\(\\cos=\\dfrac{%d}{\\sqrt{%d}\\sqrt{%d}}\\).' % (abs(dot(ua, ub)), n2(ua), n2(ub)), '\\(\\cos=\\dfrac{%d}{\\sqrt{%d}\\sqrt{%d}}\\).' % (abs(dot(ua, ub)), n2(ua), n2(ub)))
    Mc, uc, nc, Dc = P['lp']; g2 = 90 - ang(uc, nc)
    o2 = M4(2, 'The angle between \\(%s\\) and \\((P): %s\\) is…' % (par(Mc, uc), eq(*nc, Dc)), 'Góc giữa đường thẳng \\(%s\\) và \\((P): %s\\) bằng…' % (par(Mc, uc), eq(*nc, Dc)), deg(g2), [deg(90 - g2)] + [deg(x) for x in (30, 45, 60, 90) if x not in (g2, 90 - g2)],
            '\\(\\sin\\varphi=\\dfrac{%d}{\\sqrt{%d}\\sqrt{%d}}\\).' % (abs(dot(uc, nc)), n2(uc), n2(nc)), '\\(\\sin\\varphi=\\dfrac{%d}{\\sqrt{%d}\\sqrt{%d}}\\).' % (abs(dot(uc, nc)), n2(uc), n2(nc)))
    (n1, D1), (n2_, D2) = P['pp']; g3 = ang(n1, n2_)
    o3 = M4(3, 'The angle between \\(%s\\) and \\(%s\\) is…' % (eq(*n1, D1), eq(*n2_, D2)), 'Góc giữa hai mặt phẳng \\(%s\\) và \\(%s\\) bằng…' % (eq(*n1, D1), eq(*n2_, D2)), deg(g3), [deg(x) for x in (30, 45, 60, 90, 135) if x != g3],
            '\\(\\cos=\\dfrac{%d}{\\sqrt{%d}\\sqrt{%d}}\\).' % (abs(dot(n1, n2_)), n2(n1), n2(n2_)), '\\(\\cos=\\dfrac{%d}{\\sqrt{%d}\\sqrt{%d}}\\).' % (abs(dot(n1, n2_)), n2(n1), n2(n2_)))
    a4, b4, c4, truth4 = P['cos']; real = F(abs(dot(a4, b4)), 9); assert (real == c4) == truth4 and n2(a4) == n2(b4) == 9
    t4 = tf(4, 'Lines with direction vectors \\(%s\\) and \\(%s\\) make an angle with cosine \\(%s\\).' % (V3(a4), V3(b4), fr(c4)), 'Hai đường thẳng có vectơ chỉ phương \\(%s\\) và \\(%s\\) tạo với nhau góc có côsin bằng \\(%s\\).' % (V3(a4), V3(b4), fr(c4)), truth4,
            '\\(\\cos=\\dfrac{|%d|}{3\\cdot3}=%s\\).' % (dot(a4, b4), fr(real)), '\\(\\cos=\\dfrac{|%d|}{3\\cdot3}=%s\\).' % (dot(a4, b4), fr(real)))
    s5, truth5 = P['stmt']
    t5 = tf(5, s5[0], s5[1], truth5, s5[2], s5[3])
    u6, b6, c6 = P['m']; t6 = -(u6[1] * b6 + u6[2] * c6); assert t6 % u6[0] == 0; m6 = t6 // u6[0]
    s6 = sh(6, '\\(d_1\\) has direction \\(%s\\), \\(d_2\\) has direction \\((m;%d;%d)\\). Find \\(m\\) so that \\(d_1\\perp d_2\\).' % (V3(u6), b6, c6), '\\(d_1\\) có vectơ chỉ phương \\(%s\\), \\(d_2\\) có vectơ chỉ phương \\((m;%d;%d)\\). Tìm \\(m\\) để \\(d_1\\perp d_2\\).' % (V3(u6), b6, c6), m6,
            '\\(%dm%+d=0\\Rightarrow m=%d\\).' % (u6[0], -t6, m6), '\\(%dm%+d=0\\Rightarrow m=%d\\).' % (u6[0], -t6, m6))
    n7, H7 = P['roof']; g7 = ang(n7, (0, 0, 1))
    s7 = sh(7, 'A roof lies in the plane \\(%s\\) (ground \\((Oxy)\\)). Find its angle of inclination in degrees.' % eq(*n7, -H7), 'Mái nhà nằm trong mặt phẳng \\(%s\\) (mặt đất là \\((Oxy)\\)). Tính góc nghiêng của mái theo độ.' % eq(*n7, -H7), g7,
            '\\(\\cos=\\dfrac{%d}{\\sqrt{%d}}\\Rightarrow%d^\\circ\\).' % (abs(n7[2]), n2(n7), g7), '\\(\\cos=\\dfrac{%d}{\\sqrt{%d}}\\Rightarrow%d^\\circ\\).' % (abs(n7[2]), n2(n7), g7))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
SA = (('The angle between two lines can be \\(120^\\circ\\).', 'Góc giữa hai đường thẳng có thể bằng \\(120^\\circ\\).', 'It always lies in \\([0^\\circ;90^\\circ]\\).', 'Góc giữa hai đường thẳng luôn thuộc \\([0^\\circ;90^\\circ]\\).'), False)
SB = (('If \\(\\vec u\\cdot\\vec n=0\\) then the line is parallel to the plane or lies in it.', 'Nếu \\(\\vec u\\cdot\\vec n=0\\) thì đường thẳng song song hoặc nằm trong mặt phẳng.', 'Then \\(\\sin\\varphi=0\\), so \\(\\varphi=0^\\circ\\).', 'Khi đó \\(\\sin\\varphi=0\\) nên \\(\\varphi=0^\\circ\\).'), True)
SC = (('The angle between a line and a plane is computed with \\(\\cos=\\dfrac{|\\vec u\\cdot\\vec n|}{|\\vec u||\\vec n|}\\).', 'Góc giữa đường thẳng và mặt phẳng tính bởi \\(\\cos=\\dfrac{|\\vec u\\cdot\\vec n|}{|\\vec u||\\vec n|}\\).', 'That expression is the <b>sine</b> of the angle.', 'Biểu thức đó là <b>sin</b> của góc.'), False)
PP = [dict(ll=(((1, 2, 0), (1, 1, 0)), ((0, 1, 3), (1, 0, 0))), lp=((1, 0, 2), (0, 1, 1), (0, 1, 0), -3), pp=(((1, 1, 0), 2), ((0, 1, 1), -1)), cos=((1, 2, 2), (2, 1, 2), F(8, 9), True), stmt=SA, m=((1, 2, -1), 1, 3), roof=((0, 1, 1), 4)),
      dict(ll=(((0, 1, -2), (1, -1, 0)), ((3, 0, 1), (0, 1, 1))), lp=((2, -1, 0), (1, 1, 0), (1, 0, 0), 1), pp=(((1, 0, 0), -2), ((1, 0, 1), 3)), cos=((1, -2, 2), (2, 2, 1), F(4, 9), False), stmt=SB, m=((2, -1, 1), 3, -1), roof=((1, 0, 1), 3)),
      dict(ll=(((1, 1, 1), (1, 0, 1)), ((2, -1, 0), (1, 1, 0))), lp=((0, 2, 1), (1, 1, 0), (0, 1, 1), 4), pp=(((1, 1, 0), -1), ((1, -1, 0), 5)), cos=((2, -1, -2), (1, 2, 2), F(4, 9), True), stmt=SC, m=((3, 1, -2), 2, 4), roof=((0, -1, 1), 6))]
practice = three(lvl, PP)
practice = with_self(practice, S.M16S12, start=8)
mistakes = [('<b>Forgetting the absolute value</b> and getting an obtuse angle between lines or planes.', '<b>Quên dấu giá trị tuyệt đối</b> nên ra góc tù giữa hai đường thẳng hoặc hai mặt phẳng.'),
            ('<b>Using cosine for a line and a plane.</b> \\(\\dfrac{|\\vec u\\cdot\\vec n|}{|\\vec u||\\vec n|}\\) is the sine of that angle.', '<b>Dùng cos cho góc giữa đường thẳng và mặt phẳng.</b> \\(\\dfrac{|\\vec u\\cdot\\vec n|}{|\\vec u||\\vec n|}\\) là sin của góc đó.'),
            ('<b>Taking a point instead of a direction vector.</b> From \\(\\dfrac{x-1}{2}=\\ldots\\) the direction is the denominators, not \\((1;\\ldots)\\).', '<b>Lấy tọa độ điểm thay cho vectơ chỉ phương.</b> Từ \\(\\dfrac{x-1}{2}=\\ldots\\) vectơ chỉ phương là các mẫu số, không phải \\((1;\\ldots)\\).'),
            ('<b>Wrong coordinates in a cube.</b> Fix \\(A\\) at the origin and the three edges from \\(A\\) on the axes before writing other points.', '<b>Sai tọa độ trong hình lập phương.</b> Đặt \\(A\\) là gốc, ba cạnh xuất phát từ \\(A\\) nằm trên ba trục rồi mới ghi các điểm khác.')]
summary = [('Line–line: \\(\\cos=\\dfrac{|\\vec u_1\\cdot\\vec u_2|}{|\\vec u_1||\\vec u_2|}\\).', 'Đường – đường: \\(\\cos=\\dfrac{|\\vec u_1\\cdot\\vec u_2|}{|\\vec u_1||\\vec u_2|}\\).'),
           ('Line–plane: \\(\\sin=\\dfrac{|\\vec u\\cdot\\vec n|}{|\\vec u||\\vec n|}\\).', 'Đường – mặt: \\(\\sin=\\dfrac{|\\vec u\\cdot\\vec n|}{|\\vec u||\\vec n|}\\).'),
           ('Plane–plane: \\(\\cos=\\dfrac{|\\vec n_1\\cdot\\vec n_2|}{|\\vec n_1||\\vec n_2|}\\); all angles in \\([0^\\circ;90^\\circ]\\).', 'Mặt – mặt: \\(\\cos=\\dfrac{|\\vec n_1\\cdot\\vec n_2|}{|\\vec n_1||\\vec n_2|}\\); mọi góc thuộc \\([0^\\circ;90^\\circ]\\).'),
           ('Cubes and boxes: put a vertex at \\(O\\), edges on the axes. Key words: angle, direction vector, normal vector, inclination.', 'Hình lập phương, hình hộp: đặt một đỉnh tại \\(O\\), các cạnh trên trục tọa độ. Từ cần nhớ: angle, direction vector, normal vector, inclination.')]
checks = [('I can compute the angle between two lines.', 'Em tính được góc giữa hai đường thẳng.'), ('I can compute the angle between a line and a plane.', 'Em tính được góc giữa đường thẳng và mặt phẳng.'),
          ('I can compute the angle between two planes.', 'Em tính được góc giữa hai mặt phẳng.'), ('I can use coordinates to find angles in a cube.', 'Em dùng tọa độ để tính góc trong hình lập phương.')]
LL('g12-coord-05', 'Angle Formulas in Space', CV, ('Coordinate Geometry in Space', 'Phương pháp tọa độ trong không gian'), 'space-coordinates', 'angle-formulas', 160, 'Intermediate', 70, ('equations of lines and planes, dot product', 'phương trình đường thẳng, mặt phẳng, tích vô hướng'),
   'Angles between two lines, a line and a plane, two planes by coordinates; angles in cubes; inclination of roofs and solar panels.', 'Bài 16 – Công thức tính góc giữa hai đường thẳng, giữa đường thẳng và mặt phẳng, giữa hai mặt phẳng; góc trong hình lập phương; góc nghiêng thực tế.',
   ['angle', 'line', 'plane', 'inclination'], ['góc', 'đường thẳng', 'mặt phẳng', 'góc nghiêng'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g12-coord-04'])
