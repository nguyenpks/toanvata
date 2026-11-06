# -*- coding: utf-8 -*-
"""g12-coord-03 = Toán 12 KNTT, Bài 14: Phương trình mặt phẳng. Mã ngân hàng câu hỏi: TOAN12-C5-B14."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g12d as S
from sp_g12d import eq, V3, cross, dot, sub

CV = 'Phương trình mặt phẳng'
vocab = defs(CV, [
 ('nvec', 'normal vector', 'vectơ pháp tuyến', 'a non-zero vector whose direction is perpendicular to the plane.', 'vectơ khác \\(\\vec 0\\) có giá vuông góc với mặt phẳng.', '\\(\\vec n=(2;-1;3)\\) is a normal vector.', '\\(\\vec n\\)'),
 ('dpair', 'pair of direction vectors', 'cặp vectơ chỉ phương', 'two non-collinear vectors parallel to (or lying in) the plane.', 'hai vectơ không cùng phương, có giá song song hoặc nằm trong mặt phẳng.', '\\(\\overrightarrow{AB}\\), \\(\\overrightarrow{AC}\\) are a pair of direction vectors.', '\\(\\vec u,\\vec v\\)'),
 ('xprod', 'cross product', 'tích có hướng', '\\([\\vec u,\\vec v]\\): a vector perpendicular to both \\(\\vec u\\) and \\(\\vec v\\).', '\\([\\vec u,\\vec v]\\): vectơ vuông góc với cả \\(\\vec u\\) và \\(\\vec v\\).', 'The cross product gives a normal vector.', '\\([\\vec u,\\vec v]\\)'),
 ('geneq', 'general equation of a plane', 'phương trình tổng quát của mặt phẳng', '\\(Ax+By+Cz+D=0\\) with \\(A^2+B^2+C^2\\gt0\\); \\(\\vec n=(A;B;C)\\).', '\\(Ax+By+Cz+D=0\\) với \\(A^2+B^2+C^2\\gt0\\); \\(\\vec n=(A;B;C)\\).', 'Write the general equation of the plane.', ''),
 ('intform', 'intercept form', 'phương trình theo đoạn chắn', '\\(\\dfrac xa+\\dfrac yb+\\dfrac zc=1\\): the plane through \\((a;0;0)\\), \\((0;b;0)\\), \\((0;0;c)\\).', '\\(\\dfrac xa+\\dfrac yb+\\dfrac zc=1\\): mặt phẳng qua \\((a;0;0)\\), \\((0;b;0)\\), \\((0;0;c)\\).', 'Use the intercept form.', ''),
 ('dpp', 'distance from a point to a plane', 'khoảng cách từ một điểm đến mặt phẳng', '\\(d=\\dfrac{|Ax_0+By_0+Cz_0+D|}{\\sqrt{A^2+B^2+C^2}}\\).', '\\(d=\\dfrac{|Ax_0+By_0+Cz_0+D|}{\\sqrt{A^2+B^2+C^2}}\\).', 'The distance from the lamp to the roof is 2.85 m.', '\\(d\\)')])
goals = [('recognise a normal vector and a pair of direction vectors; find a normal vector with the cross product;', 'nhận biết [[vectơ pháp tuyến]], [[cặp vectơ chỉ phương]]; tìm vectơ pháp tuyến bằng [[tích có hướng]];'),
         ('write the equation of a plane (point + normal, three points, intercepts);', 'viết [[phương trình tổng quát của mặt phẳng]] (qua điểm và có pháp tuyến, qua ba điểm, [[phương trình theo đoạn chắn]]);'),
         ('decide when two planes are parallel or perpendicular;', 'xét hai mặt phẳng song song, vuông góc;'),
         ('compute the distance from a point to a plane in real situations.', 'tính [[khoảng cách từ một điểm đến mặt phẳng]] trong tình huống thực tế.')]
phrases = [('<b>Find a normal vector of the plane.</b>', 'Tìm một vectơ pháp tuyến của mặt phẳng.'), ('<b>Write the equation of the plane through three points.</b>', 'Viết phương trình mặt phẳng đi qua ba điểm.'), ('<b>The two planes are parallel.</b>', 'Hai mặt phẳng song song.'),
           ('<b>Compute the distance from the point to the plane.</b>', 'Tính khoảng cách từ điểm đến mặt phẳng.'), ('<b>Substitute the coordinates of the point.</b>', 'Thay tọa độ của điểm vào phương trình.')]
review = T('From Bài 7–8: in \\(Oxyz\\), \\(\\overrightarrow{AB}=(x_B-x_A;y_B-y_A;z_B-z_A)\\), \\(\\vec u\\cdot\\vec v=xx′+yy′+zz′\\), \\(\\vec u\\perp\\vec v\\iff\\vec u\\cdot\\vec v=0\\), \\(|\\vec u|=\\sqrt{x^2+y^2+z^2}\\). From Grade 10: a line in \\(Oxy\\) is \\(ax+by+c=0\\) with normal \\((a;b)\\).', 'Từ Bài 7–8: trong \\(Oxyz\\), \\(\\overrightarrow{AB}=(x_B-x_A;y_B-y_A;z_B-z_A)\\), \\(\\vec u\\cdot\\vec v=xx′+yy′+zz′\\), \\(\\vec u\\perp\\vec v\\iff\\vec u\\cdot\\vec v=0\\), \\(|\\vec u|=\\sqrt{x^2+y^2+z^2}\\). Từ lớp 10: đường thẳng trong \\(Oxy\\) có dạng \\(ax+by+c=0\\) với pháp tuyến \\((a;b)\\).')
A0, B0, C0 = (3, 0, 0), (0, 2, 0), (0, 0, 4); n0 = cross(sub(B0, A0), sub(C0, A0)); assert n0 == (8, 12, 6)
G0 = (1, F(2, 3), F(4, 3)); assert dot((4, 6, 3), A0) == 12 and 4 * G0[0] + 6 * G0[1] + 3 * G0[2] == 12
Nt = tuple(float(g) + 0.18 * c for g, c in zip(G0, (4, 6, 3)))
FIG = {'solid': ['O', 'A', 'B', 'C'], 'box': [[-0.5, 4], [-0.5, 3.5], [-0.5, 5]], 'points': {'O': (0, 0, 0), 'A': A0, 'B': B0, 'C': C0, 'G': tuple(float(g) for g in G0), 'N': Nt},
       'polygons': [{'points': ['A', 'B', 'C'], 'fill': '#86e0bd', 'opacity': .45}], 'segments': [['G', 'N', {'color': '#c2410c', 'width': 4}]]}
theory = '<h3>14.1 %s</h3>' % TI('Normal vector and direction vectors', 'Vectơ pháp tuyến và cặp vectơ chỉ phương')
theory += BOX('blue', ('Definitions', 'Định nghĩa'), UL([T('\\(\\vec n\\ne\\vec0\\) is a normal vector of \\((P)\\) if it is perpendicular to \\((P)\\). Then \\(k\\vec n\\) (\\(k\\ne0\\)) is also a normal vector.', '\\(\\vec n\\ne\\vec0\\) là vectơ pháp tuyến của \\((P)\\) nếu giá của \\(\\vec n\\) vuông góc với \\((P)\\). Khi đó \\(k\\vec n\\) (\\(k\\ne0\\)) cũng là vectơ pháp tuyến.'),
  T('Two non-collinear vectors \\(\\vec u\\), \\(\\vec v\\) parallel to (or in) \\((P)\\) form a pair of direction vectors.', 'Hai vectơ không cùng phương \\(\\vec u\\), \\(\\vec v\\) có giá song song hoặc nằm trong \\((P)\\) là một cặp vectơ chỉ phương của \\((P)\\).')]))
theory += BOX('mint', ('Cross product', 'Tích có hướng'), M('[\\vec u,\\vec v]=\\left(\\begin{vmatrix}y&z\\\\y′&z′\\end{vmatrix};\\begin{vmatrix}z&x\\\\z′&x′\\end{vmatrix};\\begin{vmatrix}x&y\\\\x′&y′\\end{vmatrix}\\right)=(yz′-y′z;\\ zx′-z′x;\\ xy′-x′y)'),
  T('For \\(\\vec u=(x;y;z)\\), \\(\\vec v=(x′;y′;z′)\\) not collinear, \\(\\vec n=[\\vec u,\\vec v]\\) is perpendicular to both, so it is a normal vector of the plane with direction vectors \\(\\vec u\\), \\(\\vec v\\).', 'Với \\(\\vec u=(x;y;z)\\), \\(\\vec v=(x′;y′;z′)\\) không cùng phương, \\(\\vec n=[\\vec u,\\vec v]\\) vuông góc với cả hai nên là vectơ pháp tuyến của mặt phẳng nhận \\(\\vec u\\), \\(\\vec v\\) làm cặp vectơ chỉ phương.'))
theory += '<h3>14.2 %s</h3>' % TI('Equation of a plane', 'Phương trình tổng quát của mặt phẳng')
theory += BOX('blue', ('Forms', 'Các dạng'), UL([T('General: \\(Ax+By+Cz+D=0\\) (\\(A^2+B^2+C^2\\gt0\\)), normal vector \\(\\vec n=(A;B;C)\\).', 'Tổng quát: \\(Ax+By+Cz+D=0\\) (\\(A^2+B^2+C^2\\gt0\\)), vectơ pháp tuyến \\(\\vec n=(A;B;C)\\).'),
  T('Through \\(M_0(x_0;y_0;z_0)\\) with normal \\(\\vec n=(A;B;C)\\): \\(A(x-x_0)+B(y-y_0)+C(z-z_0)=0\\).', 'Qua \\(M_0(x_0;y_0;z_0)\\), có vectơ pháp tuyến \\(\\vec n=(A;B;C)\\): \\(A(x-x_0)+B(y-y_0)+C(z-z_0)=0\\).'),
  T('Through three non-collinear points \\(A,B,C\\): \\(\\vec n=[\\overrightarrow{AB},\\overrightarrow{AC}]\\), then use the point \\(A\\).', 'Qua ba điểm không thẳng hàng \\(A,B,C\\): \\(\\vec n=[\\overrightarrow{AB},\\overrightarrow{AC}]\\), rồi dùng điểm \\(A\\).'),
  T('Intercept form (\\(abc\\ne0\\)): \\(\\dfrac xa+\\dfrac yb+\\dfrac zc=1\\).', 'Theo đoạn chắn (\\(abc\\ne0\\)): \\(\\dfrac xa+\\dfrac yb+\\dfrac zc=1\\).')]))
theory += GEO3D(FIG, cap=('The plane \\(\\dfrac x3+\\dfrac y2+\\dfrac z4=1\\), i.e. \\(4x+6y+3z-12=0\\), cuts the axes at \\(A\\), \\(B\\), \\(C\\). The orange segment shows the direction of \\(\\vec n=(4;6;3)\\). Drag to rotate.', 'Mặt phẳng \\(\\dfrac x3+\\dfrac y2+\\dfrac z4=1\\), tức \\(4x+6y+3z-12=0\\), cắt các trục tại \\(A\\), \\(B\\), \\(C\\). Đoạn màu cam chỉ phương của \\(\\vec n=(4;6;3)\\). Kéo để xoay hình.'), alt=('A plane cutting the three axes with its normal vector', ''), height=380)
theory += '<h3>14.3 %s</h3>' % TI('Parallel and perpendicular planes; distance', 'Điều kiện song song, vuông góc; khoảng cách')
theory += BOX('mint', ('For \\((P): A x+By+Cz+D=0\\), \\((P′): A′x+B′y+C′z+D′=0\\)', 'Với \\((P): Ax+By+Cz+D=0\\), \\((P′): A′x+B′y+C′z+D′=0\\)'), UL([
  T('\\((P)\\parallel(P′)\\iff\\vec n′=k\\vec n\\) and \\(D′\\ne kD\\). If also \\(D′=kD\\), the planes coincide.', '\\((P)\\parallel(P′)\\iff\\vec n′=k\\vec n\\) và \\(D′\\ne kD\\). Nếu thêm \\(D′=kD\\) thì hai mặt phẳng trùng nhau.'),
  T('\\((P)\\perp(P′)\\iff\\vec n\\cdot\\vec n′=0\\iff AA′+BB′+CC′=0\\).', '\\((P)\\perp(P′)\\iff\\vec n\\cdot\\vec n′=0\\iff AA′+BB′+CC′=0\\).'),
  T('Distance: \\(d(M_0,(P))=\\dfrac{|Ax_0+By_0+Cz_0+D|}{\\sqrt{A^2+B^2+C^2}}\\). For parallel planes take any point of one plane.', 'Khoảng cách: \\(d(M_0,(P))=\\dfrac{|Ax_0+By_0+Cz_0+D|}{\\sqrt{A^2+B^2+C^2}}\\). Với hai mặt phẳng song song, lấy một điểm bất kì trên mặt phẳng này.')]))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('The normal vector is \\((A;B;C)\\), not \\((A;B;D)\\). A missing variable means a zero coefficient: \\(y-2z=0\\) has \\(\\vec n=(0;1;-2)\\) and passes through \\(O\\).', 'Vectơ pháp tuyến là \\((A;B;C)\\), không phải \\((A;B;D)\\). Thiếu biến nào thì hệ số đó bằng 0: \\(y-2z=0\\) có \\(\\vec n=(0;1;-2)\\) và đi qua \\(O\\).'))
# kiểm tra số liệu của các ví dụ
assert 2 * 1 - 0 + 3 * 1 - 5 == 0
assert eq(2, 1, -1, -dot((2, 1, -1), (1, -2, 3))) == '2x+y-z+3=0'
A3, B3, C3 = (1, 0, 1), (2, 1, 0), (0, 2, 3); n3 = cross(sub(B3, A3), sub(C3, A3)); D3 = -dot(n3, A3); assert n3 == (4, -1, 3) and D3 == -7 and dot(n3, B3) + D3 == 0 and dot(n3, C3) + D3 == 0
assert -dot((1, -2, 2), (1, 2, 3)) == -3 and F(abs(5 - (-3)), 3) == F(8, 3)
R1, R2, R3 = (0, 0, 3), (6, 0, 5), (0, 8, 3); nr = cross(sub(R2, R1), sub(R3, R1)); assert nr == (-16, 0, 48)
Lp = (3, 4, 1); dl = F(abs(3 - 3 * 1 + 9)) ; assert dl == 9 and round(9 / math.sqrt(10), 2) == 2.85 and 0 * 1 == 0
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Read the equation', 'Đọc phương trình'), T('\\((P): 2x-y+3z-5=0\\). Give two normal vectors of \\((P)\\). Does \\(M(1;0;1)\\) lie on \\((P)\\)? Does \\(N(0;1;2)\\)?', 'Cho \\((P): 2x-y+3z-5=0\\). Chỉ ra hai vectơ pháp tuyến của \\((P)\\). Điểm \\(M(1;0;1)\\), \\(N(0;1;2)\\) có thuộc \\((P)\\) không?'),
  T('\\(\\vec n=(A;B;C)\\); substitute the coordinates.', '\\(\\vec n=(A;B;C)\\); thay tọa độ điểm vào phương trình.'), [T('\\(\\vec n=(2;-1;3)\\), and also \\(-\\vec n=(-2;1;-3)\\).', '\\(\\vec n=(2;-1;3)\\), và cả \\(-\\vec n=(-2;1;-3)\\).'), T('\\(M\\): \\(2-0+3-5=0\\) ✓. \\(N\\): \\(0-1+6-5=0\\) ✓.', '\\(M\\): \\(2-0+3-5=0\\) ✓. \\(N\\): \\(0-1+6-5=0\\) ✓.')],
  T('Both points lie on \\((P)\\).', 'Cả hai điểm đều thuộc \\((P)\\).'))
assert -1 + 6 - 5 == 0
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Point and normal', 'Qua một điểm, biết pháp tuyến'), T('Write the plane through \\(M(1;-2;3)\\) with normal vector \\(\\vec n=(2;1;-1)\\).', 'Viết phương trình mặt phẳng đi qua \\(M(1;-2;3)\\) và có vectơ pháp tuyến \\(\\vec n=(2;1;-1)\\).'),
  T('\\(A(x-x_0)+B(y-y_0)+C(z-z_0)=0\\).', '\\(A(x-x_0)+B(y-y_0)+C(z-z_0)=0\\).'), [T('\\(2(x-1)+1(y+2)-1(z-3)=0\\).', '\\(2(x-1)+1(y+2)-1(z-3)=0\\).'), T('\\(2x-2+y+2-z+3=0\\).', '\\(2x-2+y+2-z+3=0\\).')], T('\\(2x+y-z+3=0\\).', '\\(2x+y-z+3=0\\).'))
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Through three points', 'Qua ba điểm'), T('Write the plane through \\(A(1;0;1)\\), \\(B(2;1;0)\\), \\(C(0;2;3)\\).', 'Viết phương trình mặt phẳng \\((ABC)\\) với \\(A(1;0;1)\\), \\(B(2;1;0)\\), \\(C(0;2;3)\\).'),
  T('\\(\\vec n=[\\overrightarrow{AB},\\overrightarrow{AC}]\\).', '\\(\\vec n=[\\overrightarrow{AB},\\overrightarrow{AC}]\\).'),
  [T('\\(\\overrightarrow{AB}=(1;1;-1)\\), \\(\\overrightarrow{AC}=(-1;2;2)\\).', '\\(\\overrightarrow{AB}=(1;1;-1)\\), \\(\\overrightarrow{AC}=(-1;2;2)\\).'), T('\\(\\vec n=(1\\cdot2-(-1)\\cdot2;\\ (-1)(-1)-1\\cdot2;\\ 1\\cdot2-1\\cdot(-1))=(4;-1;3)\\).', '\\(\\vec n=(1\\cdot2-(-1)\\cdot2;\\ (-1)(-1)-1\\cdot2;\\ 1\\cdot2-1\\cdot(-1))=(4;-1;3)\\).'),
   T('\\(4(x-1)-(y-0)+3(z-1)=0\\). Check \\(B\\): \\(8-1+0-7=0\\); \\(C\\): \\(0-2+9-7=0\\).', '\\(4(x-1)-(y-0)+3(z-1)=0\\). Kiểm tra \\(B\\): \\(8-1+0-7=0\\); \\(C\\): \\(0-2+9-7=0\\).')],
  T('\\((ABC): 4x-y+3z-7=0\\).', '\\((ABC): 4x-y+3z-7=0\\).'))
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('A parallel plane and its distance', 'Mặt phẳng song song và khoảng cách'), T('\\((Q): x-2y+2z+5=0\\). Write the plane \\((P)\\) through \\(M(1;2;3)\\) parallel to \\((Q)\\), and find the distance between \\((P)\\) and \\((Q)\\).', 'Cho \\((Q): x-2y+2z+5=0\\). Viết phương trình mặt phẳng \\((P)\\) qua \\(M(1;2;3)\\) và song song với \\((Q)\\); tính khoảng cách giữa \\((P)\\) và \\((Q)\\).'),
  T('\\((P)\\) keeps the normal vector \\((1;-2;2)\\).', '\\((P)\\) có cùng vectơ pháp tuyến \\((1;-2;2)\\).'),
  [T('\\((P): x-2y+2z+D=0\\), \\(1-4+6+D=0\\Rightarrow D=-3\\) (and \\(-3\\ne5\\)).', '\\((P): x-2y+2z+D=0\\), \\(1-4+6+D=0\\Rightarrow D=-3\\) (và \\(-3\\ne5\\)).'), T('\\(d=d(M,(Q))=\\dfrac{|1-4+6+5|}{\\sqrt{1+4+4}}=\\dfrac83\\).', '\\(d=d(M,(Q))=\\dfrac{|1-4+6+5|}{\\sqrt{1+4+4}}=\\dfrac83\\).')],
  T('\\((P): x-2y+2z-3=0\\); distance \\(\\dfrac83\\).', '\\((P): x-2y+2z-3=0\\); khoảng cách \\(\\dfrac83\\).'))
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('A lamp under a sloping roof', 'Đèn dưới mái dốc'), T('In a room (unit: metre), a sloping roof passes through \\(A(0;0;3)\\), \\(B(6;0;5)\\), \\(C(0;8;3)\\). A lamp hangs at \\(L(3;4;1)\\). Find the equation of the roof plane and the distance from the lamp to the roof.', 'Trong một căn phòng (đơn vị mét), mái dốc đi qua \\(A(0;0;3)\\), \\(B(6;0;5)\\), \\(C(0;8;3)\\). Một chiếc đèn treo tại \\(L(3;4;1)\\). Viết phương trình mặt phẳng mái và tính khoảng cách từ đèn đến mái.'),
  T('Normal \\(=[\\overrightarrow{AB},\\overrightarrow{AC}]\\), then the distance formula.', 'Pháp tuyến \\(=[\\overrightarrow{AB},\\overrightarrow{AC}]\\), rồi dùng công thức khoảng cách.'),
  [T('\\(\\overrightarrow{AB}=(6;0;2)\\), \\(\\overrightarrow{AC}=(0;8;0)\\), \\([\\overrightarrow{AB},\\overrightarrow{AC}]=(-16;0;48)=-16(1;0;-3)\\).', '\\(\\overrightarrow{AB}=(6;0;2)\\), \\(\\overrightarrow{AC}=(0;8;0)\\), \\([\\overrightarrow{AB},\\overrightarrow{AC}]=(-16;0;48)=-16(1;0;-3)\\).'),
   T('Roof: \\(1(x-0)-3(z-3)=0\\iff x-3z+9=0\\).', 'Mái: \\(1(x-0)-3(z-3)=0\\iff x-3z+9=0\\).'), T('\\(d=\\dfrac{|3-3+9|}{\\sqrt{1+9}}=\\dfrac{9}{\\sqrt{10}}\\approx2.85\\).', '\\(d=\\dfrac{|3-3+9|}{\\sqrt{1+9}}=\\dfrac{9}{\\sqrt{10}}\\approx2{,}85\\).')],
  T('\\(x-3z+9=0\\); about 2.85 m (the roof does not depend on \\(y\\): it slopes only in the \\(x\\)-direction).', '\\(x-3z+9=0\\); khoảng 2,85 m (phương trình mái không chứa \\(y\\): mái chỉ dốc theo hướng \\(Ox\\)).'))

def lvl(P):
    M, n = P['pn']; Dd = -dot(n, M)
    o1 = M4(1, 'The plane through \\(M%s\\) with normal vector \\(\\vec n=%s\\) is…' % (V3(M), V3(n)), 'Mặt phẳng qua \\(M%s\\), có vectơ pháp tuyến \\(\\vec n=%s\\) có phương trình…' % (V3(M), V3(n)), eq(*n, Dd), [eq(*n, -Dd), eq(*M, -dot(n, M)), eq(n[0], n[1], n[2], Dd + 2)],
            '\\(%d(x%+d)%+d(y%+d)%+d(z%+d)=0\\).' % (n[0], -M[0], n[1], -M[1], n[2], -M[2]), '\\(%d(x%+d)%+d(y%+d)%+d(z%+d)=0\\).' % (n[0], -M[0], n[1], -M[1], n[2], -M[2]))
    A, B, C = P['three']; nn = cross(sub(B, A), sub(C, A)); g = math.gcd(math.gcd(abs(nn[0]), abs(nn[1])), abs(nn[2])); nn = tuple(x // g for x in nn); D2 = -dot(nn, A)
    assert dot(nn, B) + D2 == 0 and dot(nn, C) + D2 == 0
    o2 = M4(2, 'A solar panel is a flat plate through the corners \\(A%s\\), \\(B%s\\), \\(C%s\\). The equation of its plane is…' % (V3(A), V3(B), V3(C)), 'Một tấm pin mặt trời phẳng đi qua ba góc \\(A%s\\), \\(B%s\\), \\(C%s\\). Phương trình mặt phẳng chứa tấm pin là…' % (V3(A), V3(B), V3(C)),
            eq(*nn, D2), [eq(*nn, -D2) if D2 else eq(*nn, 1), eq(nn[0], -nn[1], nn[2], D2) if nn[1] else eq(nn[0], 1, nn[2], D2), eq(nn[0], nn[1], nn[2], D2 + 1)],
            '\\(\\vec n=[\\overrightarrow{AB},\\overrightarrow{AC}]\\) gives \\(%s\\) (simplified).' % V3(nn), '\\(\\vec n=[\\overrightarrow{AB},\\overrightarrow{AC}]\\) cho \\(%s\\) (đã rút gọn).' % V3(nn))
    (a, b, c, Ln), M3, k = P['dist']; D3 = k * Ln - (a * M3[0] + b * M3[1] + c * M3[2])
    o3 = M4(3, 'The distance from \\(M%s\\) to the plane \\(%s\\) is…' % (V3(M3), eq(a, b, c, D3)), 'Khoảng cách từ \\(M%s\\) đến mặt phẳng \\(%s\\) bằng…' % (V3(M3), eq(a, b, c, D3)), str(abs(k)), [str(abs(k * Ln)), str(abs(k) + 1), fr(F(abs(k), Ln))],
            '\\(\\dfrac{|%d|}{\\sqrt{%d}}=%d\\).' % (k * Ln, Ln * Ln, abs(k)), '\\(\\dfrac{|%d|}{\\sqrt{%d}}=%d\\).' % (k * Ln, Ln * Ln, abs(k)))
    p1, p2 = P['par']; (n1, d1), (n2, d2) = p1, p2
    kk = [F(y, x) for x, y in zip(n1, n2) if x] ; prop = len(set(kk)) == 1 and all((x == 0) == (y == 0) for x, y in zip(n1, n2)); ok4 = prop and F(d2) != kk[0] * d1
    t4 = tf(4, '\\((P): %s\\) and \\((Q): %s\\) are parallel.' % (eq(*n1, d1), eq(*n2, d2)), 'Hai mặt phẳng \\((P): %s\\) và \\((Q): %s\\) song song.' % (eq(*n1, d1), eq(*n2, d2)), ok4,
            '\\(\\vec n_Q=%s\\vec n_P\\)? %s' % (fr(kk[0]) if prop else '\\,k', 'yes, and \\(D_Q\\ne kD_P\\).' if ok4 else ('yes, but \\(D_Q=kD_P\\): the planes coincide.' if prop else 'no.')),
            '\\(\\vec n_Q=%s\\vec n_P\\)? %s' % (fr(kk[0]) if prop else '\\,k', 'có, và \\(D_Q\\ne kD_P\\).' if ok4 else ('có, nhưng \\(D_Q=kD_P\\): hai mặt phẳng trùng nhau.' if prop else 'không.')))
    (m1, e1), (m2, e2) = P['perp']; ok5 = dot(m1, m2) == 0
    t5 = tf(5, 'A wall \\((P): %s\\) and a floor \\((Q): %s\\) are perpendicular.' % (eq(*m1, e1), eq(*m2, e2)), 'Bức tường \\((P): %s\\) và mặt sàn \\((Q): %s\\) vuông góc với nhau.' % (eq(*m1, e1), eq(*m2, e2)), ok5,
            '\\(\\vec n_P\\cdot\\vec n_Q=%d\\).' % dot(m1, m2), '\\(\\vec n_P\\cdot\\vec n_Q=%d\\).' % dot(m1, m2))
    n6, b6, c6 = P['m']; t = -(n6[1] * b6 + n6[2] * c6); assert t % n6[0] == 0; m6 = t // n6[0]
    tm = lambda k_, v: '' if k_ == 0 else ('+' if k_ > 0 else '-') + ('' if abs(k_) == 1 else str(abs(k_))) + v
    s6 = sh(6, '\\((P): %s\\), \\((Q): mx%s%s+4=0\\). Find \\(m\\) so that \\((P)\\perp(Q)\\).' % (eq(*n6, -1), tm(b6, 'y'), tm(c6, 'z')), 'Cho \\((P): %s\\), \\((Q): mx%s%s+4=0\\). Tìm \\(m\\) để \\((P)\\perp(Q)\\).' % (eq(*n6, -1), tm(b6, 'y'), tm(c6, 'z')), m6,
            '\\(%dm%+d=0\\Rightarrow m=%d\\).' % (n6[0], -t, m6), '\\(%dm%+d=0\\Rightarrow m=%d\\).' % (n6[0], -t, m6))
    (a7, b7, c7, L7), dA, dB = P['pp']; dist = F(abs(dA - dB), L7); assert (10 * dist).denominator == 1
    s7 = sh(7, 'Two parallel shelves lie in the planes \\(%s\\) and \\(%s\\) (unit: dm). Find the distance between them.' % (eq(a7, b7, c7, dA), eq(a7, b7, c7, dB)), 'Hai tấm kệ song song nằm trên hai mặt phẳng \\(%s\\) và \\(%s\\) (đơn vị dm). Tính khoảng cách giữa hai tấm kệ.' % (eq(a7, b7, c7, dA), eq(a7, b7, c7, dB)),
            fr(dist) if dist.denominator == 1 else ('%.1f' % float(dist)), '\\(d=\\dfrac{|%d-(%d)|}{\\sqrt{%d}}=%s\\).' % (dA, dB, L7 * L7, fr(dist)), '\\(d=\\dfrac{|%d-(%d)|}{\\sqrt{%d}}=%s\\).' % (dA, dB, L7 * L7, fr(dist)))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
PP = [dict(pn=((1, 2, -1), (3, -1, 2)), three=((1, 0, 0), (0, 2, 0), (0, 0, 2)), dist=((1, 2, 2, 3), (1, 1, 1), 2), par=(((1, -2, 3), 4), ((2, -4, 6), 1)), perp=(((1, 1, 0), -3), ((0, 0, 1), 0)), m=((2, -1, 3), 4, 2), pp=((2, 1, 2, 3), 5, -7)),
      dict(pn=((0, -3, 2), (1, 4, -2)), three=((2, 1, 0), (0, 3, 1), (1, 0, 2)), dist=((2, 3, 6, 7), (0, 1, -1), -3), par=(((1, 1, -1), 2), ((-3, -3, 3), -6)), perp=(((2, -1, 1), 0), ((1, 2, 1), 5)), m=((3, 2, -1), 1, 5), pp=((1, 2, 2, 3), 4, -5)),
      dict(pn=((2, -1, 4), (-2, 5, 1)), three=((1, 1, 1), (3, 2, 0), (0, 2, 3)), dist=((6, 2, 3, 7), (2, -1, 0), 3), par=(((1, -1, 2), 3), ((2, -1, 4), 1)), perp=(((1, 0, 2), -4), ((2, 3, -1), 0)), m=((1, -2, 2), 3, 4), pp=((4, 4, 2, 6), 9, -6))]
practice = three(lvl, PP)
practice = with_self(practice, S.M14S12, start=8)
mistakes = [('<b>\\(\\vec n=(A;B;D)\\).</b> The normal vector uses the coefficients of \\(x,y,z\\) only.', '<b>\\(\\vec n=(A;B;D)\\).</b> Vectơ pháp tuyến chỉ gồm hệ số của \\(x,y,z\\).'),
            ('<b>Sign errors.</b> Through \\(M(1;-2;3)\\): \\(A(x-1)+B(y+2)+C(z-3)=0\\).', '<b>Sai dấu.</b> Qua \\(M(1;-2;3)\\): \\(A(x-1)+B(y+2)+C(z-3)=0\\).'),
            ('<b>"Proportional normals ⇒ parallel".</b> Also check \\(D′\\ne kD\\); otherwise the planes coincide.', '<b>"Pháp tuyến cùng phương ⇒ song song".</b> Còn phải kiểm tra \\(D′\\ne kD\\); nếu không hai mặt phẳng trùng nhau.'),
            ('<b>Forgetting the absolute value or the root.</b> \\(d=\\dfrac{|\\dots|}{\\sqrt{A^2+B^2+C^2}}\\).', '<b>Quên giá trị tuyệt đối hoặc căn.</b> \\(d=\\dfrac{|\\dots|}{\\sqrt{A^2+B^2+C^2}}\\).')]
summary = [('\\(Ax+By+Cz+D=0\\) has \\(\\vec n=(A;B;C)\\); through \\(M_0\\): \\(A(x-x_0)+B(y-y_0)+C(z-z_0)=0\\).', '\\(Ax+By+Cz+D=0\\) có \\(\\vec n=(A;B;C)\\); qua \\(M_0\\): \\(A(x-x_0)+B(y-y_0)+C(z-z_0)=0\\).'),
           ('Three points: \\(\\vec n=[\\overrightarrow{AB},\\overrightarrow{AC}]\\); intercepts: \\(\\frac xa+\\frac yb+\\frac zc=1\\).', 'Ba điểm: \\(\\vec n=[\\overrightarrow{AB},\\overrightarrow{AC}]\\); đoạn chắn: \\(\\frac xa+\\frac yb+\\frac zc=1\\).'),
           ('Parallel: \\(\\vec n′=k\\vec n\\), \\(D′\\ne kD\\); perpendicular: \\(\\vec n\\cdot\\vec n′=0\\).', 'Song song: \\(\\vec n′=k\\vec n\\), \\(D′\\ne kD\\); vuông góc: \\(\\vec n\\cdot\\vec n′=0\\).'),
           ('\\(d=\\dfrac{|Ax_0+By_0+Cz_0+D|}{\\sqrt{A^2+B^2+C^2}}\\). Key words: normal vector, cross product, plane, distance.', '\\(d=\\dfrac{|Ax_0+By_0+Cz_0+D|}{\\sqrt{A^2+B^2+C^2}}\\). Từ cần nhớ: normal vector, cross product, plane, distance.')]
checks = [('I can read a normal vector from an equation.', 'Em đọc được vectơ pháp tuyến từ phương trình.'), ('I can write the equation of a plane in the usual cases.', 'Em viết được phương trình mặt phẳng trong các trường hợp thường gặp.'),
          ('I can decide whether two planes are parallel or perpendicular.', 'Em xét được hai mặt phẳng song song, vuông góc.'), ('I can compute the distance from a point to a plane.', 'Em tính được khoảng cách từ một điểm đến mặt phẳng.')]
LL('g12-coord-03', 'Equations of Planes', CV, ('Coordinate Geometry in Space', 'Phương pháp tọa độ trong không gian'), 'space-coordinates', 'plane-equations', 140, 'Intermediate', 75, ('coordinates in Oxyz, dot product', 'tọa độ trong không gian, tích vô hướng'),
   'Normal vectors, cross product, equations of planes, parallel and perpendicular planes, distance from a point to a plane.', 'Bài 14 – Vectơ pháp tuyến, tích có hướng, phương trình mặt phẳng, điều kiện song song, vuông góc, khoảng cách từ điểm đến mặt phẳng.',
   ['plane', 'normal vector', 'cross product', 'distance'], ['mặt phẳng', 'vectơ pháp tuyến', 'tích có hướng', 'khoảng cách'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g12-int-03'])
