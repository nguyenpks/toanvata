# -*- coding: utf-8 -*-
"""g12-coord-04 = Toán 12 KNTT, Bài 15: Phương trình đường thẳng trong không gian. Mã ngân hàng câu hỏi: TOAN12-C5-B15."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g12e as S
from sp_g12d import eq, V3, cross, dot, sub
from sp_g12e import par, canon, add, mul, neg

CV = 'Phương trình đường thẳng trong không gian'
vocab = defs(CV, [
 ('dirvec', 'direction vector', 'vectơ chỉ phương', 'a non-zero vector parallel to (or lying on) the line.', 'vectơ khác \\(\\vec0\\) có giá song song hoặc trùng với đường thẳng.', '\\(\\vec u=(2;1;-1)\\) is a direction vector of the line.', '\\(\\vec u\\)'),
 ('parameq', 'parametric equations', 'phương trình tham số', '\\(x=x_0+at\\), \\(y=y_0+bt\\), \\(z=z_0+ct\\) (\\(t\\in\\mathbb R\\)); each value of \\(t\\) gives one point of the line.', '\\(x=x_0+at\\), \\(y=y_0+bt\\), \\(z=z_0+ct\\) (\\(t\\in\\mathbb R\\)); mỗi giá trị \\(t\\) cho một điểm của đường thẳng.', 'Write the parametric equations of the line.', '\\(t\\)'),
 ('caneq', 'canonical equation', 'phương trình chính tắc', '\\(\\dfrac{x-x_0}{a}=\\dfrac{y-y_0}{b}=\\dfrac{z-z_0}{c}\\) (\\(abc\\ne0\\)).', '\\(\\dfrac{x-x_0}{a}=\\dfrac{y-y_0}{b}=\\dfrac{z-z_0}{c}\\) (\\(abc\\ne0\\)).', 'The canonical equation of the line.', ''),
 ('mixprod', 'mixed product', 'tích hỗn tạp', 'the number \\([\\vec u,\\vec v]\\cdot\\vec w\\); it is 0 exactly when the three vectors are coplanar.', 'số \\([\\vec u,\\vec v]\\cdot\\vec w\\); bằng 0 khi và chỉ khi ba vectơ đồng phẳng.', 'The mixed product is zero, so the lines are coplanar.', '')])
goals = [('find a direction vector and write parametric and canonical equations of a line;', 'tìm [[vectơ chỉ phương]], viết [[phương trình tham số]] và [[phương trình chính tắc]] của đường thẳng;'),
         ('write the line through two points or through a point perpendicular to a plane;', 'viết phương trình đường thẳng qua hai điểm, qua một điểm và vuông góc với mặt phẳng;'),
         ('decide whether two lines are parallel, coincident, intersecting or skew;', 'xét vị trí tương đối của hai đường thẳng (song song, trùng nhau, cắt nhau, chéo nhau);'),
         ('describe straight-line motion (drones, planes) with equations.', 'mô tả chuyển động thẳng (drone, máy bay) bằng phương trình đường thẳng.')]
phrases = [('<b>The line passes through \\(M\\) and has direction vector \\(\\vec u\\).</b>', 'Đường thẳng đi qua \\(M\\) và có vectơ chỉ phương \\(\\vec u\\).'), ('<b>Substitute the parametric equations into the plane.</b>', 'Thay phương trình tham số vào phương trình mặt phẳng.'),
           ('<b>The two direction vectors are collinear.</b>', 'Hai vectơ chỉ phương cùng phương.'), ('<b>The lines are skew.</b>', 'Hai đường thẳng chéo nhau.'), ('<b>For \\(t=2\\) we get the point \\(A\\).</b>', 'Với \\(t=2\\) ta được điểm \\(A\\).')]
review = T('From Bài 14: plane \\(Ax+By+Cz+D=0\\) with normal \\(\\vec n=(A;B;C)\\); cross product \\([\\vec u,\\vec v]\\perp\\vec u,\\vec v\\); \\(\\vec u,\\vec v\\) collinear \\(\\iff[\\vec u,\\vec v]=\\vec0\\). Grade 10: parametric equations of a line in the plane.',
           'Từ Bài 14: mặt phẳng \\(Ax+By+Cz+D=0\\) có vectơ pháp tuyến \\(\\vec n=(A;B;C)\\); \\([\\vec u,\\vec v]\\) vuông góc với \\(\\vec u\\), \\(\\vec v\\); \\(\\vec u,\\vec v\\) cùng phương \\(\\iff[\\vec u,\\vec v]=\\vec0\\). Lớp 10: phương trình tham số của đường thẳng trong mặt phẳng.')
# Hình: mặt phẳng x+y+z=4 và đường thẳng qua M vuông góc với nó
Mf = (3, 3, 3); tH = F(5, 3); Hf = tuple(F(c) - tH for c in Mf); assert sum(Hf) == 4
FIG = {'proj': 'oxyz', 'axes': True, 'solid': ['O', 'A', 'B', 'C'], 'box': [[-0.5, 4.5], [-0.5, 4.5], [-0.5, 4.5]], 'points': {'O': (0, 0, 0), 'A': (4, 0, 0), 'B': (0, 4, 0), 'C': (0, 0, 4), 'M': Mf, 'H': tuple(float(c) for c in Hf)},
       'polygons': [{'points': ['A', 'B', 'C'], 'fill': '#86e0bd', 'opacity': .45}], 'segments': [['M', 'H', {'color': '#c2410c', 'width': 3}]]}
theory = '<h3>15.1 %s</h3>' % TI('Direction vector. Equations of a line', 'Vectơ chỉ phương. Phương trình đường thẳng')
theory += BOX('blue', ('Definitions', 'Định nghĩa'), UL([T('\\(\\vec u\\ne\\vec0\\) is a direction vector of \\(\\Delta\\) if it is parallel to \\(\\Delta\\) (or lies on it). Then \\(k\\vec u\\) (\\(k\\ne0\\)) is also a direction vector.', '\\(\\vec u\\ne\\vec0\\) là vectơ chỉ phương của \\(\\Delta\\) nếu giá của nó song song hoặc trùng với \\(\\Delta\\). Khi đó \\(k\\vec u\\) (\\(k\\ne0\\)) cũng là vectơ chỉ phương.'),
  T('Through \\(M_0(x_0;y_0;z_0)\\) with \\(\\vec u=(a;b;c)\\): parametric equations \\(\\begin{cases}x=x_0+at\\\\y=y_0+bt\\\\z=z_0+ct\\end{cases}\\) (\\(t\\in\\mathbb R\\)).', 'Qua \\(M_0(x_0;y_0;z_0)\\), có \\(\\vec u=(a;b;c)\\): phương trình tham số \\(\\begin{cases}x=x_0+at\\\\y=y_0+bt\\\\z=z_0+ct\\end{cases}\\) (\\(t\\in\\mathbb R\\)).'),
  T('If \\(abc\\ne0\\): canonical equation \\(\\dfrac{x-x_0}{a}=\\dfrac{y-y_0}{b}=\\dfrac{z-z_0}{c}\\).', 'Nếu \\(abc\\ne0\\): phương trình chính tắc \\(\\dfrac{x-x_0}{a}=\\dfrac{y-y_0}{b}=\\dfrac{z-z_0}{c}\\).')]))
theory += BOX('mint', ('Useful cases', 'Các trường hợp thường gặp'), UL([T('Through \\(A\\), \\(B\\): \\(\\vec u=\\overrightarrow{AB}\\).', 'Qua hai điểm \\(A\\), \\(B\\): \\(\\vec u=\\overrightarrow{AB}\\).'),
  T('Through \\(M\\), perpendicular to \\((P)\\): \\(\\vec u=\\vec n_P\\).', 'Qua \\(M\\), vuông góc với \\((P)\\): \\(\\vec u=\\vec n_P\\).'), T('Through \\(M\\), parallel to \\(d\\): \\(\\vec u=\\vec u_d\\). Perpendicular to two non-collinear vectors \\(\\vec a,\\vec b\\): \\(\\vec u=[\\vec a,\\vec b]\\).', 'Qua \\(M\\), song song với \\(d\\): \\(\\vec u=\\vec u_d\\). Vuông góc với hai vectơ không cùng phương \\(\\vec a,\\vec b\\): \\(\\vec u=[\\vec a,\\vec b]\\).')]))
theory += GEO3D(FIG, cap=('The line through \\(M(3;3;3)\\) perpendicular to \\((P): x+y+z-4=0\\) has direction \\(\\vec n=(1;1;1)\\) and meets \\((P)\\) at \\(H\\left(\\frac43;\\frac43;\\frac43\\right)\\). Drag to rotate.', 'Đường thẳng qua \\(M(3;3;3)\\) vuông góc với \\((P): x+y+z-4=0\\) có vectơ chỉ phương \\(\\vec n=(1;1;1)\\), cắt \\((P)\\) tại \\(H\\left(\\frac43;\\frac43;\\frac43\\right)\\). Kéo để xoay hình.'), alt=('A plane and a line perpendicular to it', ''), height=380)
theory += '<h3>15.2 %s</h3>' % TI('Relative position of two lines', 'Vị trí tương đối của hai đường thẳng')
theory += BOX('blue', ('\\(d_1\\) through \\(M_1\\), direction \\(\\vec u_1\\); \\(d_2\\) through \\(M_2\\), direction \\(\\vec u_2\\)', '\\(d_1\\) qua \\(M_1\\), có \\(\\vec u_1\\); \\(d_2\\) qua \\(M_2\\), có \\(\\vec u_2\\)'), TBL([TI('Position', 'Vị trí'), TI('Condition', 'Điều kiện')], [
  [TI('coincident', 'trùng nhau'), TI('\\([\\vec u_1,\\vec u_2]=\\vec0\\) and \\([\\vec u_1,\\overrightarrow{M_1M_2}]=\\vec0\\)', '\\([\\vec u_1,\\vec u_2]=\\vec0\\) và \\([\\vec u_1,\\overrightarrow{M_1M_2}]=\\vec0\\)')],
  [TI('parallel', 'song song'), TI('\\([\\vec u_1,\\vec u_2]=\\vec0\\) and \\([\\vec u_1,\\overrightarrow{M_1M_2}]\\ne\\vec0\\)', '\\([\\vec u_1,\\vec u_2]=\\vec0\\) và \\([\\vec u_1,\\overrightarrow{M_1M_2}]\\ne\\vec0\\)')],
  [TI('intersecting', 'cắt nhau'), TI('\\([\\vec u_1,\\vec u_2]\\ne\\vec0\\) and \\([\\vec u_1,\\vec u_2]\\cdot\\overrightarrow{M_1M_2}=0\\)', '\\([\\vec u_1,\\vec u_2]\\ne\\vec0\\) và \\([\\vec u_1,\\vec u_2]\\cdot\\overrightarrow{M_1M_2}=0\\)')],
  [TI('skew', 'chéo nhau'), TI('\\([\\vec u_1,\\vec u_2]\\cdot\\overrightarrow{M_1M_2}\\ne0\\)', '\\([\\vec u_1,\\vec u_2]\\cdot\\overrightarrow{M_1M_2}\\ne0\\)')]]))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('A line has many equations: another point or another (proportional) direction vector gives a different-looking but equal line. In space, two lines that do not meet need not be parallel – they can be skew.', 'Một đường thẳng có nhiều phương trình: đổi điểm hoặc đổi vectơ chỉ phương (cùng phương) cho phương trình khác nhưng cùng một đường thẳng. Trong không gian, hai đường thẳng không cắt nhau chưa chắc song song – có thể chéo nhau.'))

M1, u1 = (1, -2, 3), (2, 1, -1); assert add(M1, mul(2, u1)) == (5, 0, 1)
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Writing equations', 'Viết phương trình'), T('Write the parametric and canonical equations of the line \\(\\Delta\\) through \\(M(1;-2;3)\\) with direction vector \\(\\vec u=(2;1;-1)\\). Does \\(A(5;0;1)\\) lie on \\(\\Delta\\)?', 'Viết phương trình tham số và chính tắc của đường thẳng \\(\\Delta\\) qua \\(M(1;-2;3)\\), có vectơ chỉ phương \\(\\vec u=(2;1;-1)\\). Điểm \\(A(5;0;1)\\) có thuộc \\(\\Delta\\) không?'),
  T('Use the formulas; for \\(A\\) look for one value of \\(t\\).', 'Dùng công thức; với \\(A\\), tìm một giá trị \\(t\\) chung.'),
  [T('\\(%s\\); \\(%s\\).' % (par(M1, u1), canon(M1, u1)), '\\(%s\\); \\(%s\\).' % (par(M1, u1), canon(M1, u1))), T('\\(5=1+2t\\Rightarrow t=2\\); then \\(y=-2+2=0\\), \\(z=3-2=1\\) ✓.', '\\(5=1+2t\\Rightarrow t=2\\); khi đó \\(y=-2+2=0\\), \\(z=3-2=1\\) ✓.')],
  T('Yes, \\(A\\in\\Delta\\) (it corresponds to \\(t=2\\)).', 'Có, \\(A\\in\\Delta\\) (ứng với \\(t=2\\)).'))
A2, B2 = (1, 0, 2), (3, -1, 4); u2 = sub(B2, A2); assert u2 == (2, -1, 2)
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Line through two points', 'Đường thẳng qua hai điểm'), T('Write the canonical equation of the line \\(AB\\) with \\(A(1;0;2)\\), \\(B(3;-1;4)\\).', 'Viết phương trình chính tắc của đường thẳng \\(AB\\) với \\(A(1;0;2)\\), \\(B(3;-1;4)\\).'),
  T('\\(\\vec u=\\overrightarrow{AB}\\).', '\\(\\vec u=\\overrightarrow{AB}\\).'), [T('\\(\\overrightarrow{AB}=(2;-1;2)\\).', '\\(\\overrightarrow{AB}=(2;-1;2)\\).'), T('Through \\(A\\): \\(%s\\).' % canon(A2, u2), 'Qua \\(A\\): \\(%s\\).' % canon(A2, u2))],
  T('\\(%s\\).' % canon(A2, u2), '\\(%s\\).' % canon(A2, u2)))
M3, n3 = (2, -1, 1), (1, -2, 2); t3 = F(-(dot(n3, M3) - 15), dot(n3, n3)); H3 = tuple(F(m) + t3 * c for m, c in zip(M3, n3)); assert t3 == 1 and H3 == (3, -3, 3) and dot(n3, H3) == 15
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Perpendicular to a plane', 'Vuông góc với mặt phẳng'), T('Write the equation of the line \\(d\\) through \\(M(2;-1;1)\\) perpendicular to \\((P): x-2y+2z-15=0\\). Find the foot \\(H\\) of the perpendicular and the distance \\(MH\\).', 'Viết phương trình đường thẳng \\(d\\) qua \\(M(2;-1;1)\\) và vuông góc với \\((P): x-2y+2z-15=0\\). Tìm hình chiếu vuông góc \\(H\\) của \\(M\\) trên \\((P)\\) và độ dài \\(MH\\).'),
  T('\\(\\vec u_d=\\vec n_P\\); substitute \\(d\\) into \\((P)\\).', '\\(\\vec u_d=\\vec n_P\\); thay \\(d\\) vào \\((P)\\).'),
  [T('\\(d: %s\\).' % par(M3, n3), '\\(d: %s\\).' % par(M3, n3)), T('\\((2+t)-2(-1-2t)+2(1+2t)-15=0\\iff9t-9=0\\iff t=1\\), so \\(H(3;-3;3)\\).', '\\((2+t)-2(-1-2t)+2(1+2t)-15=0\\iff9t-9=0\\iff t=1\\), nên \\(H(3;-3;3)\\).'),
   T('\\(MH=|\\overrightarrow{MH}|=|(1;-2;2)|=3\\) (equal to \\(d(M,(P))=\\frac{|2+2+2-15|}{3}=3\\)).', '\\(MH=|\\overrightarrow{MH}|=|(1;-2;2)|=3\\) (bằng \\(d(M,(P))=\\frac{|2+2+2-15|}{3}=3\\)).')],
  T('\\(H(3;-3;3)\\), \\(MH=3\\).', '\\(H(3;-3;3)\\), \\(MH=3\\).'))
P1, v1 = (1, 2, 3), (1, -1, 2)
P2, v2 = (3, 0, 6), (-2, 2, -4)
P3, v3 = (1, 1, 4), (1, 0, 1)
P4, v4 = (0, 0, 1), (1, 1, 0)
assert cross(v1, v2) == (0, 0, 0) and cross(v1, sub(P2, P1)) != (0, 0, 0)
c13 = cross(v1, v3); assert c13 != (0, 0, 0) and dot(c13, sub(P3, P1)) == 0
c14 = cross(v1, v4); m14 = dot(c14, sub(P4, P1)); assert m14 != 0
assert add(P1, v1) == add(P3, v3) == (2, 1, 5)
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Relative positions', 'Vị trí tương đối'), T('\\(d: %s\\). Find the position of \\(d\\) relative to \\(d_2: %s\\), \\(d_3: %s\\), \\(d_4: %s\\) (parameter \\(s\\)).' % (par(P1, v1), par(P2, v2).replace('t', 's'), par(P3, v3).replace('t', 's'), par(P4, v4).replace('t', 's')),
  'Cho \\(d: %s\\). Xét vị trí tương đối của \\(d\\) với \\(d_2: %s\\), \\(d_3: %s\\), \\(d_4: %s\\) (tham số \\(s\\)).' % (par(P1, v1), par(P2, v2).replace('t', 's'), par(P3, v3).replace('t', 's'), par(P4, v4).replace('t', 's'))),
  T('\\(\\vec u=(1;-1;2)\\), \\(M(1;2;3)\\). Compute cross products and mixed products.', '\\(\\vec u=(1;-1;2)\\), \\(M(1;2;3)\\). Tính tích có hướng và tích hỗn tạp.'),
  [T('\\(d_2\\): \\(\\vec u_2=(-2;2;-4)=-2\\vec u\\); \\(\\overrightarrow{MM_2}=(2;-2;3)\\) is not collinear with \\(\\vec u\\): <b>parallel</b>.', '\\(d_2\\): \\(\\vec u_2=(-2;2;-4)=-2\\vec u\\); \\(\\overrightarrow{MM_2}=(2;-2;3)\\) không cùng phương với \\(\\vec u\\): <b>song song</b>.'),
   T('\\(d_3\\): \\([\\vec u,\\vec u_3]=%s\\ne\\vec0\\), \\(\\overrightarrow{MM_3}=%s\\), mixed product \\(=0\\): <b>intersecting</b> at \\((2;1;5)\\) (\\(t=s=1\\)).' % (V3(c13), V3(sub(P3, P1))), '\\(d_3\\): \\([\\vec u,\\vec u_3]=%s\\ne\\vec0\\), \\(\\overrightarrow{MM_3}=%s\\), tích hỗn tạp \\(=0\\): <b>cắt nhau</b> tại \\((2;1;5)\\) (\\(t=s=1\\)).' % (V3(c13), V3(sub(P3, P1)))),
   T('\\(d_4\\): \\([\\vec u,\\vec u_4]=%s\\), \\(\\overrightarrow{MM_4}=%s\\), mixed product \\(=%d\\ne0\\): <b>skew</b>.' % (V3(c14), V3(sub(P4, P1)), m14), '\\(d_4\\): \\([\\vec u,\\vec u_4]=%s\\), \\(\\overrightarrow{MM_4}=%s\\), tích hỗn tạp \\(=%d\\ne0\\): <b>chéo nhau</b>.' % (V3(c14), V3(sub(P4, P1)), m14))],
  T('\\(d\\parallel d_2\\); \\(d\\) cuts \\(d_3\\) at \\((2;1;5)\\); \\(d\\) and \\(d_4\\) are skew.', '\\(d\\parallel d_2\\); \\(d\\) cắt \\(d_3\\) tại \\((2;1;5)\\); \\(d\\) và \\(d_4\\) chéo nhau.'))
Mp, up = (0, 0, 1), (4, 3, 1); tp = 4; Pp = add(Mp, mul(tp, up)); assert Pp == (16, 12, 5) and math.hypot(16, 12) == 20
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('A climbing aircraft', 'Máy bay lấy độ cao'), T('In a coordinate system in kilometres (\\(Oxy\\) is the ground), an aircraft passes \\(A(0;0;1)\\) and climbs in a straight line; after each minute its position changes by \\(\\vec v=(4;3;1)\\). When does it reach an altitude of 5 km, where is it, and how far is it (horizontally) from the point above which it passed \\(A\\)?', 'Trong hệ tọa độ đơn vị kilômét (\\((Oxy)\\) là mặt đất), một máy bay đi qua \\(A(0;0;1)\\) và bay thẳng lên; mỗi phút vị trí thay đổi một vectơ \\(\\vec v=(4;3;1)\\). Khi nào máy bay đạt độ cao 5 km, khi đó ở đâu và cách điểm xuất phát bao xa theo phương ngang?'),
  T('Path: \\(%s\\) (\\(t\\) in minutes).' % par(Mp, up), 'Quỹ đạo: \\(%s\\) (\\(t\\) tính bằng phút).' % par(Mp, up)),
  [T('\\(z=1+t=5\\iff t=4\\).', '\\(z=1+t=5\\iff t=4\\).'), T('Position \\((16;12;5)\\); horizontal distance \\(\\sqrt{16^2+12^2}=20\\) km.', 'Vị trí \\((16;12;5)\\); khoảng cách ngang \\(\\sqrt{16^2+12^2}=20\\) km.')],
  T('After 4 minutes, at \\((16;12;5)\\), 20 km away horizontally.', 'Sau 4 phút, tại \\((16;12;5)\\), cách 20 km theo phương ngang.'))

def lvl(P):
    M, u, k = P['read']
    o1 = M4(1, 'A direction vector of \\(%s\\) is…' % canon(M, u), 'Một vectơ chỉ phương của đường thẳng \\(%s\\) là…' % canon(M, u), '\\(%s\\)' % V3(mul(k, u)), ['\\(%s\\)' % V3(M), '\\(%s\\)' % V3(neg(M)), '\\(%s\\)' % V3((u[0], -u[1], u[2]))],
            'The denominators give \\(%s\\); multiply by \\(%d\\).' % (V3(u), k), 'Các mẫu số cho \\(%s\\); nhân với \\(%d\\).' % (V3(u), k))
    A, B = P['two']; w = sub(B, A)
    o2 = M4(2, 'The line through \\(A%s\\) and \\(B%s\\) is…' % (V3(A), V3(B)), 'Đường thẳng qua \\(A%s\\) và \\(B%s\\) có phương trình…' % (V3(A), V3(B)), '\\(%s\\)' % canon(A, w),
            ['\\(%s\\)' % canon(neg(A), w), '\\(%s\\)' % canon(A, (w[0], w[1], -w[2])), '\\(%s\\)' % canon(B, add(A, B)) if all(add(A, B)) else '\\(%s\\)' % canon(A, (-w[0], w[1], w[2]))],
            '\\(\\overrightarrow{AB}=%s\\), through \\(A\\).' % V3(w), '\\(\\overrightarrow{AB}=%s\\), qua \\(A\\).' % V3(w))
    Mq, n, Dq, t = P['meet']; Pq = add(Mq, mul(t, n)); Dd = -dot(n, Pq)
    o3 = M4(3, 'The line through \\(M%s\\) perpendicular to \\((P): %s\\) meets \\((P)\\) at…' % (V3(Mq), eq(*n, Dd)), 'Đường thẳng qua \\(M%s\\) vuông góc với \\((P): %s\\) cắt \\((P)\\) tại…' % (V3(Mq), eq(*n, Dd)), '\\(%s\\)' % V3(Pq),
            ['\\(%s\\)' % V3(add(Mq, mul(-t, n))), '\\(%s\\)' % V3(add(Mq, mul(t + 1, n))), '\\(%s\\)' % V3(n)], 'Substitute \\(M+t\\vec n\\): \\(t=%d\\).' % t, 'Thay \\(M+t\\vec n\\) vào: \\(t=%d\\).' % t)
    (M4a, u4a, M4b, u4b, claim_en, claim_vi, truth) = P['rel']
    c = cross(u4a, u4b); mx = dot(c, sub(M4b, M4a))
    real = 'parallel' if c == (0, 0, 0) and cross(u4a, sub(M4b, M4a)) != (0, 0, 0) else 'coincident' if c == (0, 0, 0) else 'intersecting' if mx == 0 else 'skew'
    assert (real == claim_en) == truth
    t4 = tf(4, 'The lines \\(%s\\) and \\(%s\\) are %s.' % (par(M4a, u4a), par(M4b, u4b).replace('t', 's'), claim_en), 'Hai đường thẳng \\(%s\\) và \\(%s\\) %s.' % (par(M4a, u4a), par(M4b, u4b).replace('t', 's'), claim_vi), truth,
            '\\([\\vec u_1,\\vec u_2]=%s\\), mixed product \\(%d\\): they are %s.' % (V3(c), mx, real), '\\([\\vec u_1,\\vec u_2]=%s\\), tích hỗn tạp \\(%d\\): %s.' % (V3(c), mx, dict(parallel='song song', coincident='trùng nhau', intersecting='cắt nhau', skew='chéo nhau')[real]))
    M5, u5, Q5, truth5 = P['on']; tt = [F(q - m, a) for q, m, a in zip(Q5, M5, u5)]
    assert (tt[0] == tt[1] == tt[2]) == truth5
    t5 = tf(5, 'The point \\(%s\\) lies on \\(%s\\).' % (V3(Q5), canon(M5, u5)), 'Điểm \\(%s\\) thuộc đường thẳng \\(%s\\).' % (V3(Q5), canon(M5, u5)), truth5,
            'The three ratios are \\(%s\\).' % ', '.join(fr(x) for x in tt), 'Ba tỉ số lần lượt là \\(%s\\).' % ', '.join(fr(x) for x in tt))
    M6, u6, n6, D6 = P['par_t']; tv = F(-(dot(n6, M6) + D6), dot(n6, u6)); assert tv.denominator == 1
    s6 = sh(6, '\\(d: %s\\) meets \\((P): %s\\) at the point with parameter \\(t=\\)?' % (par(M6, u6), eq(*n6, D6)), 'Đường thẳng \\(d: %s\\) cắt \\((P): %s\\) tại điểm ứng với \\(t=\\)?' % (par(M6, u6), eq(*n6, D6)), int(tv),
            '\\(%dt%+d=0\\Rightarrow t=%d\\).' % (dot(n6, u6), dot(n6, M6) + D6, tv), '\\(%dt%+d=0\\Rightarrow t=%d\\).' % (dot(n6, u6), dot(n6, M6) + D6, tv))
    M7, v7, h7 = P['plane']; t7 = F(h7 - M7[2], v7[2]); assert t7.denominator == 1
    s7 = sh(7, 'An aircraft at \\(%s\\) (km) moves by \\(\\vec v=%s\\) each minute. After how many minutes is its altitude \\(%d\\) km?' % (V3(M7), V3(v7), h7), 'Máy bay ở \\(%s\\) (km), mỗi phút dịch chuyển \\(\\vec v=%s\\). Sau bao nhiêu phút máy bay ở độ cao \\(%d\\) km?' % (V3(M7), V3(v7), h7), int(t7),
            '\\(z=%d+%dt=%d\\Rightarrow t=%d\\).' % (M7[2], v7[2], h7, t7), '\\(z=%d+%dt=%d\\Rightarrow t=%d\\).' % (M7[2], v7[2], h7, t7))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
PP = [dict(read=((1, -2, 0), (2, 3, -1), -2), two=((1, 2, 3), (3, 1, 5)), meet=((1, 1, 1), (1, 2, 2), 0, 1), rel=((1, 0, 2), (1, 2, -1), (3, 4, 0), (-2, -4, 2), 'parallel', 'song song', False),
           on=((1, -1, 2), (2, 1, 3), (5, 1, 8), True), par_t=((1, 0, -2), (1, 2, 1), (1, 1, 1), -7), plane=((0, 0, 1), (3, 4, 1), 6)),
      dict(read=((-1, 3, 2), (1, -2, 4), 3), two=((0, -1, 2), (2, 3, 1)), meet=((2, 0, -1), (2, -1, 2), 0, -1), rel=((0, 1, 1), (1, 1, 0), (1, 0, 2), (0, 1, 1), 'skew', 'chéo nhau', True),
           on=((2, 0, -1), (1, -3, 2), (4, -6, 2), False), par_t=((2, 1, 0), (1, -1, 2), (2, 1, -1), 1), plane=((5, 2, 2), (2, 2, 1), 9)),
      dict(read=((3, 0, -4), (-3, 1, 2), 2), two=((-2, 1, 0), (1, 3, -2)), meet=((-1, 2, 3), (1, -2, 1), 0, 2), rel=((1, 1, 0), (2, -1, 1), (3, 0, 1), (1, 1, 2), 'intersecting', 'cắt nhau', True),
           on=((0, 2, -1), (-1, 2, 3), (-2, 6, 5), True), par_t=((-1, 3, 2), (2, 1, -1), (1, -1, 3), 20), plane=((4, -3, 0), (1, 2, 2), 10))]
practice = three(lvl, PP)
practice = with_self(practice, S.M15S12, start=8)
mistakes = [('<b>Using the normal vector of a plane as a direction vector of a line in it.</b> \\(\\vec n_P\\) is the direction of lines <i>perpendicular</i> to \\((P)\\).', '<b>Lấy vectơ pháp tuyến của mặt phẳng làm vectơ chỉ phương của đường thẳng nằm trong nó.</b> \\(\\vec n_P\\) là phương của đường thẳng <i>vuông góc</i> với \\((P)\\).'),
            ('<b>Sign errors in the canonical form.</b> Through \\(M(1;-2;3)\\): \\(\\dfrac{x-1}{a}=\\dfrac{y+2}{b}=\\dfrac{z-3}{c}\\).', '<b>Sai dấu trong phương trình chính tắc.</b> Qua \\(M(1;-2;3)\\): \\(\\dfrac{x-1}{a}=\\dfrac{y+2}{b}=\\dfrac{z-3}{c}\\).'),
            ('<b>"Not intersecting, so parallel".</b> In space the lines may be skew: check \\([\\vec u_1,\\vec u_2]\\) first.', '<b>"Không cắt nhau nên song song".</b> Trong không gian có thể chéo nhau: kiểm tra \\([\\vec u_1,\\vec u_2]\\) trước.'),
            ('<b>Using the same parameter for two lines.</b> Give the second line its own parameter \\(s\\) when looking for a common point.', '<b>Dùng chung một tham số cho hai đường thẳng.</b> Khi tìm giao điểm, đặt tham số \\(s\\) riêng cho đường thứ hai.')]
summary = [('\\(\\Delta\\): \\(x=x_0+at\\), \\(y=y_0+bt\\), \\(z=z_0+ct\\); if \\(abc\\ne0\\): \\(\\dfrac{x-x_0}{a}=\\dfrac{y-y_0}{b}=\\dfrac{z-z_0}{c}\\).', '\\(\\Delta\\): \\(x=x_0+at\\), \\(y=y_0+bt\\), \\(z=z_0+ct\\); nếu \\(abc\\ne0\\): \\(\\dfrac{x-x_0}{a}=\\dfrac{y-y_0}{b}=\\dfrac{z-z_0}{c}\\).'),
           ('Through \\(A,B\\): \\(\\vec u=\\overrightarrow{AB}\\); perpendicular to \\((P)\\): \\(\\vec u=\\vec n_P\\).', 'Qua \\(A,B\\): \\(\\vec u=\\overrightarrow{AB}\\); vuông góc với \\((P)\\): \\(\\vec u=\\vec n_P\\).'),
           ('\\([\\vec u_1,\\vec u_2]=\\vec0\\): parallel or coincident; otherwise mixed product \\(=0\\): intersecting, \\(\\ne0\\): skew.', '\\([\\vec u_1,\\vec u_2]=\\vec0\\): song song hoặc trùng nhau; ngược lại tích hỗn tạp \\(=0\\): cắt nhau, \\(\\ne0\\): chéo nhau.'),
           ('Line ∩ plane: substitute the parametric equations and solve for \\(t\\). Key words: direction vector, parametric, canonical, skew.', 'Giao của đường thẳng và mặt phẳng: thay phương trình tham số, giải \\(t\\). Từ cần nhớ: direction vector, parametric, canonical, skew.')]
checks = [('I can write parametric and canonical equations of a line.', 'Em viết được phương trình tham số, chính tắc của đường thẳng.'), ('I can write the line through two points or perpendicular to a plane.', 'Em viết được đường thẳng qua hai điểm, vuông góc với mặt phẳng.'),
          ('I can decide the relative position of two lines.', 'Em xét được vị trí tương đối của hai đường thẳng.'), ('I can find where a line meets a plane.', 'Em tìm được giao điểm của đường thẳng và mặt phẳng.')]
LL('g12-coord-04', 'Equations of Lines in Space', CV, ('Coordinate Geometry in Space', 'Phương pháp tọa độ trong không gian'), 'space-coordinates', 'line-equations', 150, 'Intermediate', 75, ('equations of planes, cross product', 'phương trình mặt phẳng, tích có hướng'),
   'Direction vectors, parametric and canonical equations, lines through two points or perpendicular to a plane, relative positions of two lines.', 'Bài 15 – Vectơ chỉ phương, phương trình tham số, phương trình chính tắc, vị trí tương đối của hai đường thẳng, giao điểm với mặt phẳng.',
   ['line', 'direction vector', 'parametric equations', 'skew lines'], ['đường thẳng', 'vectơ chỉ phương', 'phương trình tham số', 'chéo nhau'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g12-coord-03'])
