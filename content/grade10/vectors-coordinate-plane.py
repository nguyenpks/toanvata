# -*- coding: utf-8 -*-
"""g10-vec-04 = Toán 10 KNTT, Bài 10: Vectơ trong mặt phẳng tọa độ. Mã ngân hàng câu hỏi: TOAN10-C4-B10."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g10d as S
from sp_g10d import P2, V2, ov, add

CV = 'Vectơ trong mặt phẳng tọa độ'
vocab = defs(CV, [
 ('oxy', 'coordinate plane', 'hệ trục tọa độ', 'two perpendicular axes \\(Ox\\), \\(Oy\\) meeting at the origin \\(O\\), with unit vectors \\(\\vec i\\), \\(\\vec j\\).', 'hai trục \\(Ox\\), \\(Oy\\) vuông góc tại gốc \\(O\\), có vectơ đơn vị \\(\\vec i\\), \\(\\vec j\\).', 'Draw the coordinate plane \\(Oxy\\).', '\\(Oxy\\)'),
 ('unitv', 'unit vector', 'vectơ đơn vị', 'a vector of length 1; \\(\\vec i\\) on \\(Ox\\) and \\(\\vec j\\) on \\(Oy\\).', 'vectơ có độ dài bằng 1; \\(\\vec i\\) trên \\(Ox\\), \\(\\vec j\\) trên \\(Oy\\).', '\\(|\\vec i|=|\\vec j|=1\\).', '\\(\\vec i,\\ \\vec j\\)'),
 ('vcoord', 'coordinates of a vector', 'tọa độ của vectơ', 'the pair \\((x;y)\\) with \\(\\vec u=x\\vec i+y\\vec j\\).', 'cặp số \\((x;y)\\) sao cho \\(\\vec u=x\\vec i+y\\vec j\\).', '\\(\\vec u=3\\vec i-2\\vec j\\), so \\(\\vec u=(3;-2)\\).', '\\(\\vec u=(x;y)\\)'),
 ('pcoord', 'coordinates of a point', 'tọa độ của điểm', 'the coordinates of the vector \\(\\overrightarrow{OM}\\); \\(x\\) is the abscissa, \\(y\\) the ordinate.', 'tọa độ của vectơ \\(\\overrightarrow{OM}\\); \\(x\\) là hoành độ, \\(y\\) là tung độ.', '\\(M(2;5)\\) has abscissa 2.', '\\(M(x;y)\\)'),
 ('absc', 'abscissa', 'hoành độ', 'the first coordinate \\(x\\) of a point.', 'tọa độ thứ nhất \\(x\\) của một điểm.', 'The abscissa of \\(M(2;5)\\) is 2.', ''),
 ('ordi', 'ordinate', 'tung độ', 'the second coordinate \\(y\\) of a point.', 'tọa độ thứ hai \\(y\\) của một điểm.', 'The ordinate of \\(M(2;5)\\) is 5.', ''),
 ('collin', 'collinear points', 'ba điểm thẳng hàng', 'points that lie on one line; \\(A,B,C\\) are collinear when \\(\\overrightarrow{AB}\\) and \\(\\overrightarrow{AC}\\) are collinear vectors.', 'các điểm cùng nằm trên một đường thẳng; \\(A,B,C\\) thẳng hàng khi \\(\\overrightarrow{AB}\\), \\(\\overrightarrow{AC}\\) cùng phương.', 'Show that \\(A\\), \\(B\\), \\(C\\) are collinear.', '')])
goals = [('read and write the coordinates of points and vectors in \\(Oxy\\);', 'đọc, viết [[tọa độ của điểm]] và [[tọa độ của vectơ]] trong [[hệ trục tọa độ]] \\(Oxy\\);'),
         ('find \\(\\overrightarrow{AB}\\), the length \\(AB\\), a midpoint and a centroid;', 'tìm \\(\\overrightarrow{AB}\\), độ dài \\(AB\\), tọa độ trung điểm và trọng tâm;'),
         ('add, subtract and scale vectors by coordinates; test collinearity;', 'cộng, trừ, nhân vectơ với một số theo tọa độ; xét hai vectơ cùng phương;'),
         ('use coordinates in map and motion problems, and decide if three points are collinear.', 'dùng tọa độ trong bài toán bản đồ, chuyển động và xét [[ba điểm thẳng hàng]].')]
phrases = [('<b>Find the coordinates of the vector \\(\\overrightarrow{AB}\\).</b>', 'Tìm tọa độ của vectơ \\(\\overrightarrow{AB}\\).'), ('<b>Find the midpoint of the segment \\(AB\\).</b>', 'Tìm tọa độ trung điểm của đoạn thẳng \\(AB\\).'),
           ('<b>The two vectors are collinear.</b>', 'Hai vectơ cùng phương.'), ('<b>Are the three points collinear?</b>', 'Ba điểm có thẳng hàng không?'), ('<b>Find the fourth vertex of the parallelogram.</b>', 'Tìm đỉnh thứ tư của hình bình hành.')]
review = T('From Bài 7–9: two vectors are equal when they have the same direction and the same length; \\(I\\) is the midpoint of \\(AB\\iff\\overrightarrow{IA}+\\overrightarrow{IB}=\\vec 0\\); \\(G\\) is the centroid of \\(ABC\\iff\\overrightarrow{GA}+\\overrightarrow{GB}+\\overrightarrow{GC}=\\vec 0\\); \\(\\vec b\\) and \\(\\vec a\\ne\\vec 0\\) are collinear \\(\\iff\\vec b=k\\vec a\\).',
           'Từ Bài 7–9: hai vectơ bằng nhau khi cùng hướng và cùng độ dài; \\(I\\) là trung điểm \\(AB\\iff\\overrightarrow{IA}+\\overrightarrow{IB}=\\vec 0\\); \\(G\\) là trọng tâm tam giác \\(ABC\\iff\\overrightarrow{GA}+\\overrightarrow{GB}+\\overrightarrow{GC}=\\vec 0\\); \\(\\vec b\\) và \\(\\vec a\\ne\\vec 0\\) cùng phương \\(\\iff\\vec b=k\\vec a\\).')

FIGA, FIGB = (1, 1), (4, 5)
theory = '<h3>10.1 %s</h3>' % TI('Coordinates of a vector and of a point', 'Tọa độ của vectơ và của điểm')
theory += BOX('blue', ('Definitions', 'Định nghĩa'), UL([
  T('The coordinate plane \\(Oxy\\) has two perpendicular axes with unit vectors \\(\\vec i\\) (on \\(Ox\\)) and \\(\\vec j\\) (on \\(Oy\\)).', '[[Hệ trục tọa độ]] \\(Oxy\\) gồm hai trục vuông góc với hai [[vectơ đơn vị]] \\(\\vec i\\) (trên \\(Ox\\)) và \\(\\vec j\\) (trên \\(Oy\\)).'),
  T('Every vector \\(\\vec u\\) can be written in exactly one way as \\(\\vec u=x\\vec i+y\\vec j\\). We write \\(\\vec u=(x;y)\\).', 'Mọi vectơ \\(\\vec u\\) biểu diễn được duy nhất dưới dạng \\(\\vec u=x\\vec i+y\\vec j\\). Ta viết \\(\\vec u=(x;y)\\).'),
  T('The coordinates of a point \\(M\\) are the coordinates of \\(\\overrightarrow{OM}\\): \\(M(x;y)\\iff\\overrightarrow{OM}=x\\vec i+y\\vec j\\).', 'Tọa độ của điểm \\(M\\) là tọa độ của vectơ \\(\\overrightarrow{OM}\\): \\(M(x;y)\\iff\\overrightarrow{OM}=x\\vec i+y\\vec j\\).'),
  T('\\(\\vec u=(x;y)\\) and \\(\\vec u′=(x′;y′)\\) are equal \\(\\iff x=x′\\) and \\(y=y′\\).', '\\(\\vec u=(x;y)\\) và \\(\\vec u′=(x′;y′)\\) bằng nhau \\(\\iff x=x′\\) và \\(y=y′\\).')]))
theory += BOX('mint', ('Vector from two points', 'Vectơ nối hai điểm'), M('\\overrightarrow{AB}=(x_B-x_A;\\,y_B-y_A),\\qquad AB=|\\overrightarrow{AB}|=\\sqrt{(x_B-x_A)^2+(y_B-y_A)^2}'),
  T('Rule: <b>end point minus start point</b>. Also \\(|\\vec u|=\\sqrt{x^2+y^2}\\) for \\(\\vec u=(x;y)\\).', 'Quy tắc: <b>tọa độ điểm cuối trừ tọa độ điểm đầu</b>. Với \\(\\vec u=(x;y)\\) thì \\(|\\vec u|=\\sqrt{x^2+y^2}\\).'))
theory += GEO({'view': [-1, 7, -1, 7], 'axes': True, 'steps': [
  {'type': 'point', 'id': 'A', 'at': list(FIGA), 'fixed': True}, {'type': 'point', 'id': 'B', 'at': list(FIGB), 'fixed': True}, {'type': 'point', 'id': 'H', 'name': '', 'at': [FIGB[0], FIGA[1]], 'fixed': True, 'style': {'size': 1}},
  {'type': 'segment', 'through': ['A', 'B'], 'style': {'lastArrow': {'type': 2, 'size': 8}, 'strokeWidth': 3}},
  {'type': 'segment', 'through': ['A', 'H'], 'style': {'dash': 2, 'strokeColor': '#c2410c'}}, {'type': 'segment', 'through': ['H', 'B'], 'style': {'dash': 2, 'strokeColor': '#1d4ed8'}}]},
  cap=('\\(A(1;1)\\), \\(B(4;5)\\): \\(\\overrightarrow{AB}=(3;4)\\) – go 3 units right (orange) and 4 units up (blue); \\(AB=\\sqrt{3^2+4^2}=5\\).', '\\(A(1;1)\\), \\(B(4;5)\\): \\(\\overrightarrow{AB}=(3;4)\\) – sang phải 3 đơn vị (cam), lên trên 4 đơn vị (xanh); \\(AB=\\sqrt{3^2+4^2}=5\\).'),
  alt=('Vector AB on the coordinate plane with its horizontal and vertical parts', ''), height=320)
assert add(FIGB, FIGA, 1, -1) == (3, 4)
theory += '<h3>10.2 %s</h3>' % TI('Operations on vectors by coordinates', 'Biểu thức tọa độ của các phép toán vectơ')
theory += BOX('blue', ('With \\(\\vec u=(x;y)\\), \\(\\vec v=(x′;y′)\\) and a number \\(k\\)', 'Với \\(\\vec u=(x;y)\\), \\(\\vec v=(x′;y′)\\) và số thực \\(k\\)'), UL([
  T('\\(\\vec u+\\vec v=(x+x′;\\,y+y′)\\), \\(\\vec u-\\vec v=(x-x′;\\,y-y′)\\), \\(k\\vec u=(kx;\\,ky)\\).', '\\(\\vec u+\\vec v=(x+x′;\\,y+y′)\\), \\(\\vec u-\\vec v=(x-x′;\\,y-y′)\\), \\(k\\vec u=(kx;\\,ky)\\).'),
  T('\\(\\vec v\\) is collinear with \\(\\vec u\\ne\\vec 0\\) \\(\\iff\\) there is \\(k\\) with \\(x′=kx,\\ y′=ky\\) \\(\\iff xy′-x′y=0\\).', '\\(\\vec v\\) cùng phương với \\(\\vec u\\ne\\vec 0\\) \\(\\iff\\) có số \\(k\\) để \\(x′=kx,\\ y′=ky\\) \\(\\iff xy′-x′y=0\\).')]))
theory += BOX('mint', ('Midpoint and centroid', 'Trung điểm và trọng tâm'), M('I\\left(\\dfrac{x_A+x_B}{2};\\,\\dfrac{y_A+y_B}{2}\\right),\\qquad G\\left(\\dfrac{x_A+x_B+x_C}{3};\\,\\dfrac{y_A+y_B+y_C}{3}\\right)'),
  T('\\(I\\) is the midpoint of \\(AB\\); \\(G\\) is the centroid of triangle \\(ABC\\).', '\\(I\\) là trung điểm đoạn \\(AB\\); \\(G\\) là trọng tâm tam giác \\(ABC\\).'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('\\(\\overrightarrow{AB}\\) and \\(\\overrightarrow{BA}\\) have opposite coordinates. When the second vector has a zero coordinate, use \\(xy′-x′y=0\\) instead of dividing by zero. \\(A\\), \\(B\\), \\(C\\) are collinear \\(\\iff\\overrightarrow{AB}\\), \\(\\overrightarrow{AC}\\) are collinear.',
  '\\(\\overrightarrow{AB}\\) và \\(\\overrightarrow{BA}\\) có tọa độ đối nhau. Khi có tọa độ bằng 0, dùng điều kiện \\(xy′-x′y=0\\) thay vì chia cho 0. \\(A\\), \\(B\\), \\(C\\) thẳng hàng \\(\\iff\\overrightarrow{AB}\\), \\(\\overrightarrow{AC}\\) cùng phương.'))

# ----- Ví dụ (mọi số liệu được kiểm bằng assert) -----
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Read coordinates', 'Đọc tọa độ'), T('Write the coordinates of \\(\\vec u=3\\vec i-2\\vec j\\), \\(\\vec v=-\\vec j\\) and of the point \\(M\\) with \\(\\overrightarrow{OM}=-\\vec i+4\\vec j\\).', 'Viết tọa độ của \\(\\vec u=3\\vec i-2\\vec j\\), \\(\\vec v=-\\vec j\\) và của điểm \\(M\\) biết \\(\\overrightarrow{OM}=-\\vec i+4\\vec j\\).'),
  T('The number in front of \\(\\vec i\\) is \\(x\\); the number in front of \\(\\vec j\\) is \\(y\\). A missing term means 0.', 'Hệ số của \\(\\vec i\\) là \\(x\\), hệ số của \\(\\vec j\\) là \\(y\\); thiếu số hạng nào thì tọa độ đó bằng 0.'),
  [T('\\(\\vec u=3\\vec i+(-2)\\vec j\\Rightarrow\\vec u=(3;-2)\\).', '\\(\\vec u=3\\vec i+(-2)\\vec j\\Rightarrow\\vec u=(3;-2)\\).'), T('\\(\\vec v=0\\vec i+(-1)\\vec j\\Rightarrow\\vec v=(0;-1)\\).', '\\(\\vec v=0\\vec i+(-1)\\vec j\\Rightarrow\\vec v=(0;-1)\\).'), T('\\(M\\) has the coordinates of \\(\\overrightarrow{OM}\\).', 'Tọa độ \\(M\\) là tọa độ của \\(\\overrightarrow{OM}\\).')],
  T('\\(\\vec u=(3;-2)\\), \\(\\vec v=(0;-1)\\), \\(M(-1;4)\\).', '\\(\\vec u=(3;-2)\\), \\(\\vec v=(0;-1)\\), \\(M(-1;4)\\).'))
A, B = (-2, 1), (4, 9); AB = add(B, A, 1, -1); assert AB == (6, 8) and math.hypot(*AB) == 10
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Distance on a map', 'Khoảng cách trên bản đồ'), T('On a city map (1 unit = 100 m), the school is at \\(A(-2;1)\\) and the stadium at \\(B(4;9)\\). Find \\(\\overrightarrow{AB}\\) and the straight-line distance between them in metres.', 'Trên bản đồ thành phố (1 đơn vị ứng với 100 m), trường học ở \\(A(-2;1)\\), sân vận động ở \\(B(4;9)\\). Tìm \\(\\overrightarrow{AB}\\) và khoảng cách theo đường thẳng giữa hai nơi (mét).'),
  T('End minus start, then the length formula.', 'Lấy điểm cuối trừ điểm đầu, rồi dùng công thức độ dài.'),
  [T('\\(\\overrightarrow{AB}=(4-(-2);\\,9-1)=(6;8)\\).', '\\(\\overrightarrow{AB}=(4-(-2);\\,9-1)=(6;8)\\).'), T('\\(AB=\\sqrt{6^2+8^2}=\\sqrt{100}=10\\) units.', '\\(AB=\\sqrt{6^2+8^2}=\\sqrt{100}=10\\) đơn vị.')],
  T('\\(\\overrightarrow{AB}=(6;8)\\); the distance is \\(10\\cdot100=1000\\ \\text{m}\\).', '\\(\\overrightarrow{AB}=(6;8)\\); khoảng cách là \\(10\\cdot100=1000\\ \\text{m}\\).'))
a, b, c = (2, -1), (-3, 4), (-6, 3); s = add(a, b, 2, 1); assert s == (1, 2) and c == (-3 * a[0], -3 * a[1])
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Operations and collinearity', 'Phép toán và cùng phương'), T('\\(\\vec a=(2;-1)\\), \\(\\vec b=(-3;4)\\), \\(\\vec c=(-6;3)\\). Find \\(2\\vec a+\\vec b\\). Are \\(\\vec a\\) and \\(\\vec c\\) collinear? Are \\(\\vec a\\) and \\(\\vec b\\)?', 'Cho \\(\\vec a=(2;-1)\\), \\(\\vec b=(-3;4)\\), \\(\\vec c=(-6;3)\\). Tính \\(2\\vec a+\\vec b\\). Hai vectơ \\(\\vec a\\), \\(\\vec c\\) có cùng phương không? \\(\\vec a\\), \\(\\vec b\\) thì sao?'),
  T('Work coordinate by coordinate; for collinearity look for one number \\(k\\) for both coordinates.', 'Tính theo từng tọa độ; để xét cùng phương, tìm một số \\(k\\) dùng chung cho cả hai tọa độ.'),
  [T('\\(2\\vec a=(4;-2)\\), so \\(2\\vec a+\\vec b=(4-3;\\,-2+4)=(1;2)\\).', '\\(2\\vec a=(4;-2)\\) nên \\(2\\vec a+\\vec b=(4-3;\\,-2+4)=(1;2)\\).'), T('\\(\\vec c=(-6;3)=-3\\cdot(2;-1)=-3\\vec a\\): collinear (opposite directions).', '\\(\\vec c=(-6;3)=-3\\cdot(2;-1)=-3\\vec a\\): cùng phương (ngược hướng).'), T('\\(2\\cdot4-(-3)\\cdot(-1)=8-3=5\\ne0\\): \\(\\vec a\\), \\(\\vec b\\) are not collinear.', '\\(2\\cdot4-(-3)\\cdot(-1)=8-3=5\\ne0\\): \\(\\vec a\\), \\(\\vec b\\) không cùng phương.')],
  T('\\(2\\vec a+\\vec b=(1;2)\\); \\(\\vec a\\parallel\\vec c\\) (collinear); \\(\\vec a\\), \\(\\vec b\\) are not collinear.', '\\(2\\vec a+\\vec b=(1;2)\\); \\(\\vec a\\), \\(\\vec c\\) cùng phương; \\(\\vec a\\), \\(\\vec b\\) không cùng phương.'))
assert a[0] * b[1] - b[0] * a[1] == 5
A, B, C = (-1, 1), (3, 2), (1, -3); M_ = (F(B[0] + C[0], 2), F(B[1] + C[1], 2)); G = (F(A[0] + B[0] + C[0], 3), F(A[1] + B[1] + C[1], 3)); D = add(add(A, C), B, 1, -1)
assert M_ == (2, F(-1, 2)) and G == (1, 0) and D == (-3, -4)
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Midpoint, centroid, parallelogram', 'Trung điểm, trọng tâm, hình bình hành'), T('\\(A(-1;1)\\), \\(B(3;2)\\), \\(C(1;-3)\\). Find the midpoint \\(M\\) of \\(BC\\), the centroid \\(G\\) of triangle \\(ABC\\), and \\(D\\) so that \\(ABCD\\) is a parallelogram.', 'Cho \\(A(-1;1)\\), \\(B(3;2)\\), \\(C(1;-3)\\). Tìm trung điểm \\(M\\) của \\(BC\\), trọng tâm \\(G\\) của tam giác \\(ABC\\) và điểm \\(D\\) để \\(ABCD\\) là hình bình hành.'),
  T('For the parallelogram use \\(\\overrightarrow{AD}=\\overrightarrow{BC}\\) (careful with the order of the letters).', 'Với hình bình hành dùng \\(\\overrightarrow{AD}=\\overrightarrow{BC}\\) (chú ý thứ tự các đỉnh).'),
  [T('\\(M\\left(\\dfrac{3+1}2;\\dfrac{2-3}2\\right)=\\left(2;-\\dfrac12\\right)\\).', '\\(M\\left(\\dfrac{3+1}2;\\dfrac{2-3}2\\right)=\\left(2;-\\dfrac12\\right)\\).'), T('\\(G\\left(\\dfrac{-1+3+1}3;\\dfrac{1+2-3}3\\right)=(1;0)\\).', '\\(G\\left(\\dfrac{-1+3+1}3;\\dfrac{1+2-3}3\\right)=(1;0)\\).'),
   T('\\(\\overrightarrow{BC}=(-2;-5)\\). \\(\\overrightarrow{AD}=\\overrightarrow{BC}\\) gives \\(x_D+1=-2\\), \\(y_D-1=-5\\).', '\\(\\overrightarrow{BC}=(-2;-5)\\). \\(\\overrightarrow{AD}=\\overrightarrow{BC}\\) cho \\(x_D+1=-2\\), \\(y_D-1=-5\\).')],
  T('\\(M\\left(2;-\\dfrac12\\right)\\), \\(G(1;0)\\), \\(D(-3;-4)\\).', '\\(M\\left(2;-\\dfrac12\\right)\\), \\(G(1;0)\\), \\(D(-3;-4)\\).'))
P0, P1, P2_ = (1, 1), (3, 2), (9, 5); u1, u2 = add(P1, P0, 1, -1), add(P2_, P0, 1, -1); assert u2 == (4 * u1[0], 4 * u1[1])
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Will the drone pass the tower?', 'Flycam có bay qua tháp không?'), T('A drone flies in a straight line from \\(A(1;1)\\) through \\(B(3;2)\\) (unit: km). A radio tower stands at \\(C(9;5)\\). Will the drone fly over the tower? If yes, how far from \\(A\\) is the tower?', 'Một flycam bay theo đường thẳng từ \\(A(1;1)\\) qua \\(B(3;2)\\) (đơn vị km). Một trạm phát sóng đặt ở \\(C(9;5)\\). Flycam có bay qua trạm không? Nếu có, trạm cách \\(A\\) bao xa?'),
  T('The drone passes \\(C\\) exactly when \\(A\\), \\(B\\), \\(C\\) are collinear.', 'Flycam bay qua \\(C\\) khi và chỉ khi \\(A\\), \\(B\\), \\(C\\) thẳng hàng.'),
  [T('\\(\\overrightarrow{AB}=(2;1)\\), \\(\\overrightarrow{AC}=(8;4)=4\\overrightarrow{AB}\\).', '\\(\\overrightarrow{AB}=(2;1)\\), \\(\\overrightarrow{AC}=(8;4)=4\\overrightarrow{AB}\\).'), T('So \\(A\\), \\(B\\), \\(C\\) are collinear and \\(C\\) is on the same side as \\(B\\) (because \\(k=4\\gt0\\)).', 'Vậy \\(A\\), \\(B\\), \\(C\\) thẳng hàng và \\(C\\) cùng phía với \\(B\\) so với \\(A\\) (vì \\(k=4\\gt0\\)).'), T('\\(AC=\\sqrt{8^2+4^2}=\\sqrt{80}=4\\sqrt5\\approx8.94\\) km.', '\\(AC=\\sqrt{8^2+4^2}=\\sqrt{80}=4\\sqrt5\\approx8{,}94\\) km.')],
  T('Yes; the tower is \\(4\\sqrt5\\approx8.94\\) km from \\(A\\).', 'Có; trạm cách \\(A\\) khoảng \\(4\\sqrt5\\approx8{,}94\\) km.'))
assert abs(math.hypot(8, 4) - 8.94) < 0.005

# ----- Bài tập: mỗi mức một bộ cùng dạng, khác số liệu -----
def lvl(P):
    A, B, unit = P['map']; v = add(B, A, 1, -1); d = math.hypot(*v); assert d == int(d); d = int(d)
    o1 = M4(1, 'On a map (1 unit = %d m), a bus stop is at \\(A%s\\) and a market at \\(B%s\\). The vector \\(%s\\) is…' % (unit, P2(A), P2(B), ov('A', 'B')), 'Trên bản đồ (1 đơn vị ứng với %d m), trạm xe buýt ở \\(A%s\\), chợ ở \\(B%s\\). Vectơ \\(%s\\) có tọa độ…' % (unit, P2(A), P2(B), ov('A', 'B')),
            V2(v), [V2(add(A, B, 1, -1)), V2(add(A, B)), V2((v[1], v[0]))], 'End minus start: \\(%s\\).' % V2(v), 'Điểm cuối trừ điểm đầu: \\(%s\\).' % V2(v))
    a, b, (s, t) = P['comb']; res = add(a, b, s, t); ex = '%s\\vec a%s\\vec b' % ({1: '', -1: '-'}.get(s, str(s)), ('+' if t > 0 else '-') + ('' if abs(t) == 1 else str(abs(t))))
    o2 = M4(2, '\\(\\vec a=%s\\), \\(\\vec b=%s\\). The coordinates of \\(%s\\) are…' % (V2(a), V2(b), ex), 'Cho \\(\\vec a=%s\\), \\(\\vec b=%s\\). Tọa độ của \\(%s\\) là…' % (V2(a), V2(b), ex),
            V2(res), [V2(add(a, b, s, -t)), V2(add(a, b)), V2((res[0], -res[1]))], 'Scale, then add coordinate by coordinate.', 'Nhân với số trước, rồi cộng theo từng tọa độ.')
    A3, B3, C3 = P['pgm']; D3 = add(add(A3, C3), B3, 1, -1)
    o3 = M4(3, 'A garden \\(ABCD\\) is a parallelogram with \\(A%s\\), \\(B%s\\), \\(C%s\\). The corner \\(D\\) is at…' % (P2(A3), P2(B3), P2(C3)), 'Một mảnh vườn \\(ABCD\\) hình bình hành có \\(A%s\\), \\(B%s\\), \\(C%s\\). Góc vườn \\(D\\) có tọa độ…' % (P2(A3), P2(B3), P2(C3)),
            P2(D3), [P2(add(add(B3, C3), A3, 1, -1)), P2(add(add(A3, B3), C3, 1, -1)), P2(add(A3, C3))], '\\(\\overrightarrow{AD}=\\overrightarrow{BC}\\Rightarrow D=A+C-B=%s\\).' % P2(D3), '\\(\\overrightarrow{AD}=\\overrightarrow{BC}\\Rightarrow D=A+C-B=%s\\).' % P2(D3))
    u, w, truth = P['col']; real = u[0] * w[1] - u[1] * w[0] == 0; assert real == truth
    t4 = tf(4, '\\(\\vec u=%s\\) and \\(\\vec w=%s\\) are collinear.' % (V2(u), V2(w)), 'Hai vectơ \\(\\vec u=%s\\) và \\(\\vec w=%s\\) cùng phương.' % (V2(u), V2(w)), truth,
            '\\(xy′-x′y=%d\\cdot%d-%d\\cdot%d=%d\\).' % (u[0], w[1], w[0], u[1], u[0] * w[1] - u[1] * w[0]), '\\(xy′-x′y=%d\\cdot%d-%d\\cdot%d=%d\\).' % (u[0], w[1], w[0], u[1], u[0] * w[1] - u[1] * w[0]))
    E, F_, G_, gtruth = P['cent']; Gr = (F(E[0] + F_[0] + G_[0], 3), F(E[1] + F_[1] + G_[1], 3)); claim = Gr if gtruth else (Gr[0] + 1, Gr[1])
    t5 = tf(5, 'Three friends live at \\(E%s\\), \\(F%s\\), \\(H%s\\). They want to meet at the centroid of triangle \\(EFH\\). The meeting point is \\(%s\\).' % (P2(E), P2(F_), P2(G_), P2(claim)),
            'Ba bạn ở \\(E%s\\), \\(F%s\\), \\(H%s\\) hẹn gặp tại trọng tâm tam giác \\(EFH\\). Điểm hẹn là \\(%s\\).' % (P2(E), P2(F_), P2(G_), P2(claim)), gtruth,
            'The centroid is \\(%s\\).' % P2(Gr), 'Trọng tâm là \\(%s\\).' % P2(Gr))
    s6 = sh(6, 'On a map (1 unit = %d m), \\(A%s\\) and \\(B%s\\). Find the real distance \\(AB\\) in metres.' % (unit, P2(A), P2(B)),
            'Trên bản đồ (1 đơn vị ứng với %d m) cho \\(A%s\\), \\(B%s\\). Tính khoảng cách thực tế \\(AB\\) (mét).' % (unit, P2(A), P2(B)), d * unit, '\\(AB=\\sqrt{%d^2+%d^2}=%d\\) units \\(=%d\\) m.' % (abs(v[0]), abs(v[1]), d, d * unit), '\\(AB=\\sqrt{%d^2+%d^2}=%d\\) đơn vị \\(=%d\\) m.' % (abs(v[0]), abs(v[1]), d, d * unit))
    Q1, Q2, x3 = P['line']; dvec = add(Q2, Q1, 1, -1); tnum = (x3 - Q1[0]); assert tnum % dvec[0] == 0; m = Q1[1] + tnum // dvec[0] * dvec[1]
    s7 = sh(7, 'Points \\(A%s\\), \\(B%s\\) and \\(C(%d;\\,m)\\). Find \\(m\\) so that \\(A\\), \\(B\\), \\(C\\) are collinear.' % (P2(Q1), P2(Q2), x3), 'Cho \\(A%s\\), \\(B%s\\), \\(C(%d;\\,m)\\). Tìm \\(m\\) để ba điểm \\(A\\), \\(B\\), \\(C\\) thẳng hàng.' % (P2(Q1), P2(Q2), x3), m,
            '\\(\\overrightarrow{AB}=%s\\), \\(\\overrightarrow{AC}=(%d;\\,m%s%d)\\) collinear gives \\(m=%d\\).' % (V2(dvec), x3 - Q1[0], '-' if Q1[1] >= 0 else '+', abs(Q1[1]), m), '\\(\\overrightarrow{AB}=%s\\), \\(\\overrightarrow{AC}=(%d;\\,m%s%d)\\) cùng phương cho \\(m=%d\\).' % (V2(dvec), x3 - Q1[0], '-' if Q1[1] >= 0 else '+', abs(Q1[1]), m))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
PP = [dict(map=((1, 2), (4, 6), 100), comb=((1, 3), (2, -1), (2, 1)), pgm=((0, 0), (3, 1), (5, 4)), col=((2, -3), (-4, 6), True), cent=((0, 0), (6, 3), (3, 6), True), line=((0, 1), (2, 3), 4)),
      dict(map=((-2, 3), (4, -5), 50), comb=((-2, 4), (3, 1), (3, -2)), pgm=((1, -2), (4, 0), (6, 5)), col=((3, 1), (6, 3), False), cent=((-1, 2), (4, 5), (3, -1), False), line=((1, -1), (3, 3), 5)),
      dict(map=((5, -1), (-7, 4), 20), comb=((4, -1), (-2, 5), (-1, 3)), pgm=((-3, 1), (2, -1), (4, 3)), col=((-5, 2), (10, -4), True), cent=((2, -3), (-4, 1), (5, 8), True), line=((-2, 4), (1, -2), 4))]
practice = three(lvl, PP)
practice = with_self(practice, S.M10S10, start=8)
mistakes = [('<b>Start minus end.</b> \\(\\overrightarrow{AB}=B-A\\) (end minus start); \\(A-B\\) gives \\(\\overrightarrow{BA}\\).', '<b>Lấy điểm đầu trừ điểm cuối.</b> \\(\\overrightarrow{AB}=B-A\\) (cuối trừ đầu); \\(A-B\\) cho \\(\\overrightarrow{BA}\\).'),
            ('<b>Adding the coordinates in the length.</b> \\(|(3;4)|=\\sqrt{9+16}=5\\), not \\(3+4=7\\).', '<b>Cộng tọa độ khi tính độ dài.</b> \\(|(3;4)|=\\sqrt{9+16}=5\\), không phải \\(3+4=7\\).'),
            ('<b>Wrong order of the parallelogram.</b> For \\(ABCD\\) use \\(\\overrightarrow{AD}=\\overrightarrow{BC}\\) (or \\(\\overrightarrow{AB}=\\overrightarrow{DC}\\)), so \\(D=A+C-B\\).', '<b>Sai thứ tự đỉnh hình bình hành.</b> Với \\(ABCD\\) dùng \\(\\overrightarrow{AD}=\\overrightarrow{BC}\\) (hoặc \\(\\overrightarrow{AB}=\\overrightarrow{DC}\\)) nên \\(D=A+C-B\\).'),
            ('<b>Two different ratios.</b> Collinear vectors need the <b>same</b> \\(k\\) for both coordinates.', '<b>Hai tỉ số khác nhau.</b> Hai vectơ cùng phương cần <b>cùng một</b> số \\(k\\) cho cả hai tọa độ.')]
summary = [('\\(\\vec u=x\\vec i+y\\vec j\\iff\\vec u=(x;y)\\); \\(M(x;y)\\iff\\overrightarrow{OM}=(x;y)\\).', '\\(\\vec u=x\\vec i+y\\vec j\\iff\\vec u=(x;y)\\); \\(M(x;y)\\iff\\overrightarrow{OM}=(x;y)\\).'),
           ('\\(\\overrightarrow{AB}=(x_B-x_A;\\,y_B-y_A)\\), \\(AB=\\sqrt{(x_B-x_A)^2+(y_B-y_A)^2}\\).', '\\(\\overrightarrow{AB}=(x_B-x_A;\\,y_B-y_A)\\), \\(AB=\\sqrt{(x_B-x_A)^2+(y_B-y_A)^2}\\).'),
           ('Sum, difference and \\(k\\vec u\\) are done coordinate by coordinate; collinear \\(\\iff xy′-x′y=0\\).', 'Tổng, hiệu, \\(k\\vec u\\) tính theo từng tọa độ; cùng phương \\(\\iff xy′-x′y=0\\).'),
           ('Midpoint: average of 2 points; centroid: average of 3 points. Key words: coordinates, abscissa, ordinate, collinear.', 'Trung điểm: trung bình cộng 2 điểm; trọng tâm: trung bình cộng 3 điểm. Từ cần nhớ: coordinates, abscissa, ordinate, collinear.')]
checks = [('I can write the coordinates of points and vectors.', 'Em viết được tọa độ của điểm và của vectơ.'), ('I can find \\(\\overrightarrow{AB}\\), \\(AB\\), a midpoint and a centroid.', 'Em tìm được \\(\\overrightarrow{AB}\\), \\(AB\\), trung điểm và trọng tâm.'),
          ('I can decide whether two vectors (three points) are collinear.', 'Em xét được hai vectơ cùng phương, ba điểm thẳng hàng.'), ('I can solve a map problem with coordinates.', 'Em giải được bài toán bản đồ bằng tọa độ.')]
LL('g10-vec-04', 'Vectors in the Coordinate Plane', CV, ('Vectors', 'Vectơ'), 'vectors', 'vectors-coordinate-plane', 100, 'Intermediate', 70, ('vectors, sum and difference, multiplying a vector by a number', 'vectơ, tổng và hiệu, tích của vectơ với một số'),
   'Coordinates of points and vectors in Oxy; vector operations by coordinates; midpoint, centroid, collinear points.', 'Bài 10 – Tọa độ của điểm, vectơ; biểu thức tọa độ các phép toán vectơ; trung điểm, trọng tâm, ba điểm thẳng hàng.',
   ['coordinates', 'vector', 'midpoint', 'centroid', 'collinear'], ['tọa độ', 'vectơ', 'trung điểm', 'trọng tâm', 'thẳng hàng'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g10-vec-03'])
