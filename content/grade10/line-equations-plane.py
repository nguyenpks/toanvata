# -*- coding: utf-8 -*-
"""g10-coord-01 = Toán 10 KNTT, Bài 19: Phương trình đường thẳng. Mã ngân hàng câu hỏi: TOAN10-C7-B19."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g10g as S
from sp_g10g import leq, norm3, V2, pr2

CV = 'Phương trình đường thẳng'
vocab = defs(CV, [
 ('geneq2', 'general equation of a line', 'phương trình tổng quát của đường thẳng', '\\(ax+by+c=0\\) with \\(a^2+b^2\\ne0\\); \\(\\vec n=(a;b)\\) is a normal vector.', '\\(ax+by+c=0\\) với \\(a^2+b^2\\ne0\\); \\(\\vec n=(a;b)\\) là một vectơ pháp tuyến.', 'Write the general equation of the line.', ''),
 ('nvec2', 'normal vector of a line', 'vectơ pháp tuyến của đường thẳng', 'a non-zero vector perpendicular to the direction of the line.', 'vectơ khác \\(\\vec0\\) có giá vuông góc với đường thẳng.', 'The normal vector is (2; −3).', '\\(\\vec n\\)'),
 ('slopeform', 'slope–intercept form', 'phương trình theo hệ số góc', '\\(y=kx+m\\); \\(k\\) is the slope.', '\\(y=kx+m\\); \\(k\\) là hệ số góc.', 'The line y = 2x + 1 has slope 2.', '')])
goals = [('recognise direction vectors, normal vectors and the forms of the equation of a line;', 'nhận biết [[vectơ chỉ phương]], [[vectơ pháp tuyến của đường thẳng]] và các dạng phương trình đường thẳng;'),
         ('write parametric and general equations from given data (a point and a vector, two points, a slope);', 'viết [[phương trình tham số]] và [[phương trình tổng quát của đường thẳng]] khi biết một điểm và một vectơ, hai điểm, hệ số góc;'),
         ('solve coordinate problems on lines in a triangle (altitudes, medians);', 'giải bài toán tọa độ về đường cao, đường trung tuyến trong tam giác;'),
         ('model linear relations in real life with a line.', 'mô hình hóa quan hệ bậc nhất trong thực tế bằng đường thẳng.')]
phrases = [('<b>The line passes through \\(A\\) and has normal vector \\(\\vec n\\).</b>', 'Đường thẳng đi qua \\(A\\) và có vectơ pháp tuyến \\(\\vec n\\).'), ('<b>A direction vector is perpendicular to a normal vector.</b>', 'Vectơ chỉ phương vuông góc với vectơ pháp tuyến.'),
           ('<b>Substitute the coordinates of the point.</b>', 'Thay tọa độ của điểm vào phương trình.'), ('<b>The slope of the line is two.</b>', 'Hệ số góc của đường thẳng bằng 2.'), ('<b>Write the general equation.</b>', 'Viết phương trình tổng quát.')]
review = T('From Bài 10–11: coordinates of a vector \\(\\overrightarrow{AB}=(x_B-x_A;y_B-y_A)\\); \\(\\vec u\\perp\\vec v\\iff\\vec u\\cdot\\vec v=0\\). From Grade 9: the graph of \\(y=ax+b\\) is a line with slope \\(a\\).',
           'Từ Bài 10–11: tọa độ vectơ \\(\\overrightarrow{AB}=(x_B-x_A;y_B-y_A)\\); \\(\\vec u\\perp\\vec v\\iff\\vec u\\cdot\\vec v=0\\). Từ lớp 9: đồ thị \\(y=ax+b\\) là đường thẳng có hệ số góc \\(a\\).')
theory = '<h3>19.1 %s</h3>' % TI('Direction vector and parametric equations', 'Vectơ chỉ phương và phương trình tham số')
theory += BOX('blue', ('Definitions', 'Định nghĩa'), UL([T('\\(\\vec u\\ne\\vec0\\) is a direction vector of \\(\\Delta\\) if it is parallel to (or lies on) \\(\\Delta\\).', '\\(\\vec u\\ne\\vec0\\) là vectơ chỉ phương của \\(\\Delta\\) nếu giá của nó song song hoặc trùng với \\(\\Delta\\).'),
  T('Through \\(M_0(x_0;y_0)\\) with \\(\\vec u=(a;b)\\): \\(\\begin{cases}x=x_0+at\\\\y=y_0+bt\\end{cases}\\) (\\(t\\in\\mathbb R\\)). Each \\(t\\) gives one point of \\(\\Delta\\).', 'Qua \\(M_0(x_0;y_0)\\), có \\(\\vec u=(a;b)\\): \\(\\begin{cases}x=x_0+at\\\\y=y_0+bt\\end{cases}\\) (\\(t\\in\\mathbb R\\)). Mỗi \\(t\\) cho một điểm của \\(\\Delta\\).')]))
theory += '<h3>19.2 %s</h3>' % TI('Normal vector and general equation', 'Vectơ pháp tuyến và phương trình tổng quát')
theory += BOX('blue', ('Definitions', 'Định nghĩa'), UL([T('\\(\\vec n\\ne\\vec0\\) is a normal vector of \\(\\Delta\\) if it is perpendicular to a direction vector. If \\(\\vec u=(a;b)\\) then \\(\\vec n=(b;-a)\\) (and conversely).', '\\(\\vec n\\ne\\vec0\\) là vectơ pháp tuyến của \\(\\Delta\\) nếu nó vuông góc với vectơ chỉ phương. Nếu \\(\\vec u=(a;b)\\) thì \\(\\vec n=(b;-a)\\) (và ngược lại).'),
  T('Through \\(M_0(x_0;y_0)\\) with \\(\\vec n=(a;b)\\): \\(a(x-x_0)+b(y-y_0)=0\\), i.e. \\(ax+by+c=0\\) with \\(c=-ax_0-by_0\\).', 'Qua \\(M_0(x_0;y_0)\\), có \\(\\vec n=(a;b)\\): \\(a(x-x_0)+b(y-y_0)=0\\), tức \\(ax+by+c=0\\) với \\(c=-ax_0-by_0\\).'),
  T('Conversely, every equation \\(ax+by+c=0\\) (\\(a^2+b^2\\ne0\\)) is a line with \\(\\vec n=(a;b)\\), \\(\\vec u=(b;-a)\\).', 'Ngược lại, mọi phương trình \\(ax+by+c=0\\) (\\(a^2+b^2\\ne0\\)) là một đường thẳng có \\(\\vec n=(a;b)\\), \\(\\vec u=(b;-a)\\).')]))
theory += BOX('mint', ('Special cases', 'Các trường hợp đặc biệt'), UL([T('Through \\(A(a;0)\\), \\(B(0;b)\\) (\\(ab\\ne0\\)): \\(\\dfrac xa+\\dfrac yb=1\\) (intercept form).', 'Qua \\(A(a;0)\\), \\(B(0;b)\\) (\\(ab\\ne0\\)): \\(\\dfrac xa+\\dfrac yb=1\\) (phương trình đoạn chắn).'),
  T('If \\(b\\ne0\\): \\(ax+by+c=0\\iff y=kx+m\\) with slope \\(k=-\\dfrac ab\\). Through \\(A\\), \\(B\\) with \\(x_A\\ne x_B\\): \\(k=\\dfrac{y_B-y_A}{x_B-x_A}\\).', 'Nếu \\(b\\ne0\\): \\(ax+by+c=0\\iff y=kx+m\\) với hệ số góc \\(k=-\\dfrac ab\\). Qua \\(A\\), \\(B\\) với \\(x_A\\ne x_B\\): \\(k=\\dfrac{y_B-y_A}{x_B-x_A}\\).'),
  T('\\(a=0\\): \\(y=-\\frac cb\\) (parallel to \\(Ox\\)); \\(b=0\\): \\(x=-\\frac ca\\) (parallel to \\(Oy\\)).', '\\(a=0\\): \\(y=-\\frac cb\\) (song song với \\(Ox\\)); \\(b=0\\): \\(x=-\\frac ca\\) (song song với \\(Oy\\)).')]))
theory += GRAPH({'view': [-3, 6, -2, 5], 'functions': [{'f': '(x+1)/2', 'label': 'x − 2y + 1 = 0'}], 'points': [{'x': 1, 'y': 1, 'label': 'A(1; 1)'}, {'x': 3, 'y': 2, 'label': 'B(3; 2)'}]},
  cap=('The line \\(AB\\): \\(\\overrightarrow{AB}=(2;1)\\) is a direction vector, \\(\\vec n=(1;-2)\\) a normal vector, so \\(x-2y+1=0\\); slope \\(k=\\frac12\\).', 'Đường thẳng \\(AB\\): \\(\\overrightarrow{AB}=(2;1)\\) là vectơ chỉ phương, \\(\\vec n=(1;-2)\\) là vectơ pháp tuyến, nên \\(x-2y+1=0\\); hệ số góc \\(k=\\frac12\\).'),
  alt=('The line through A(1;1) and B(3;2)', 'Đường thẳng qua A(1;1) và B(3;2)'), height=280)
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('From \\(ax+by+c=0\\): \\(\\vec n=(a;b)\\) but \\(\\vec u=(b;-a)\\) – do not mix them up. A line has many equations: multiplying by \\(k\\ne0\\) gives the same line.', 'Từ \\(ax+by+c=0\\): \\(\\vec n=(a;b)\\) còn \\(\\vec u=(b;-a)\\) – đừng nhầm. Một đường thẳng có nhiều phương trình: nhân hai vế với \\(k\\ne0\\) vẫn được cùng đường thẳng.'))

assert 2 * 0 - 3 * 2 + 6 == 0 and 2 * (-3) + 6 == 0 and 2 * 3 + (-3) * 2 == 0
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Reading a general equation', 'Đọc phương trình tổng quát'), T('For \\(\\Delta: 2x-3y+6=0\\), give a normal vector, a direction vector and two points of \\(\\Delta\\).', 'Cho \\(\\Delta: 2x-3y+6=0\\). Chỉ ra một vectơ pháp tuyến, một vectơ chỉ phương và hai điểm thuộc \\(\\Delta\\).'),
  T('\\(\\vec n=(a;b)\\), \\(\\vec u=(b;-a)\\); points: put \\(x=0\\), then \\(y=0\\).', '\\(\\vec n=(a;b)\\), \\(\\vec u=(b;-a)\\); tìm điểm: cho \\(x=0\\), rồi \\(y=0\\).'),
  [T('\\(\\vec n=(2;-3)\\), \\(\\vec u=(3;2)\\) (check \\(\\vec n\\cdot\\vec u=6-6=0\\)).', '\\(\\vec n=(2;-3)\\), \\(\\vec u=(3;2)\\) (kiểm tra \\(\\vec n\\cdot\\vec u=6-6=0\\)).'), T('\\(x=0\\Rightarrow y=2\\); \\(y=0\\Rightarrow x=-3\\).', '\\(x=0\\Rightarrow y=2\\); \\(y=0\\Rightarrow x=-3\\).')],
  T('\\(\\vec n=(2;-3)\\), \\(\\vec u=(3;2)\\), points \\((0;2)\\), \\((-3;0)\\).', '\\(\\vec n=(2;-3)\\), \\(\\vec u=(3;2)\\), điểm \\((0;2)\\), \\((-3;0)\\).'))
assert (1 + 3 * 2, -2 + 4 * 2) == (7, 6)
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Parametric equations', 'Phương trình tham số'), T('Write parametric equations of the line \\(d\\) through \\(A(1;-2)\\) with direction vector \\(\\vec u=(3;4)\\). Does \\(M(7;6)\\) lie on \\(d\\)?', 'Viết phương trình tham số của đường thẳng \\(d\\) qua \\(A(1;-2)\\), có vectơ chỉ phương \\(\\vec u=(3;4)\\). Điểm \\(M(7;6)\\) có thuộc \\(d\\) không?'),
  T('Find one \\(t\\) for both coordinates.', 'Tìm một giá trị \\(t\\) chung cho cả hai tọa độ.'), [T('\\(d: %s\\).' % pr2((1, -2), (3, 4)), '\\(d: %s\\).' % pr2((1, -2), (3, 4))), T('\\(7=1+3t\\Rightarrow t=2\\); \\(y=-2+8=6\\) ✓.', '\\(7=1+3t\\Rightarrow t=2\\); \\(y=-2+8=6\\) ✓.')],
  T('\\(M\\in d\\) (with \\(t=2\\)).', '\\(M\\in d\\) (ứng với \\(t=2\\)).'))
assert norm3(3, -1, -5) == (3, -1, -5) and 3 * 2 - 1 - 5 == 0 and (1 + 2 - 3, 4 - 1 - 3) == (0, 0)
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('General equations', 'Viết phương trình tổng quát'), T('a) The line through \\(M(2;1)\\) with normal vector \\(\\vec n=(3;-1)\\). b) The line through \\(A(1;2)\\) and \\(B(4;-1)\\).', 'Viết phương trình tổng quát của: a) đường thẳng qua \\(M(2;1)\\), có vectơ pháp tuyến \\(\\vec n=(3;-1)\\); b) đường thẳng qua \\(A(1;2)\\) và \\(B(4;-1)\\).'),
  T('\\(a(x-x_0)+b(y-y_0)=0\\); for b), \\(\\vec n\\perp\\overrightarrow{AB}\\).', '\\(a(x-x_0)+b(y-y_0)=0\\); câu b), \\(\\vec n\\perp\\overrightarrow{AB}\\).'),
  [T('a) \\(3(x-2)-(y-1)=0\\iff3x-y-5=0\\).', 'a) \\(3(x-2)-(y-1)=0\\iff3x-y-5=0\\).'), T('b) \\(\\overrightarrow{AB}=(3;-3)\\), take \\(\\vec u=(1;-1)\\), \\(\\vec n=(1;1)\\): \\((x-1)+(y-2)=0\\iff x+y-3=0\\).', 'b) \\(\\overrightarrow{AB}=(3;-3)\\), chọn \\(\\vec u=(1;-1)\\), \\(\\vec n=(1;1)\\): \\((x-1)+(y-2)=0\\iff x+y-3=0\\).')],
  T('a) \\(3x-y-5=0\\); b) \\(x+y-3=0\\).', 'a) \\(3x-y-5=0\\); b) \\(x+y-3=0\\).'))
assert 2 * 1 + 4 - 6 == 0 and (4 * (1 - 1) + 2 * (4 - 4)) == 0 and ((-1 + 3) / 2, (0 + 2) / 2) == (1, 1)
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Altitude and median', 'Đường cao và đường trung tuyến'), T('Triangle \\(ABC\\): \\(A(1;4)\\), \\(B(-1;0)\\), \\(C(3;2)\\). Write the equations of the altitude \\(AH\\) and the median \\(AM\\).', 'Cho tam giác \\(ABC\\) với \\(A(1;4)\\), \\(B(-1;0)\\), \\(C(3;2)\\). Viết phương trình đường cao \\(AH\\) và đường trung tuyến \\(AM\\).'),
  T('The altitude has normal vector \\(\\overrightarrow{BC}\\); \\(M\\) is the midpoint of \\(BC\\).', 'Đường cao nhận \\(\\overrightarrow{BC}\\) làm vectơ pháp tuyến; \\(M\\) là trung điểm \\(BC\\).'),
  [T('\\(\\overrightarrow{BC}=(4;2)\\), take \\(\\vec n=(2;1)\\): \\(2(x-1)+(y-4)=0\\iff2x+y-6=0\\).', '\\(\\overrightarrow{BC}=(4;2)\\), chọn \\(\\vec n=(2;1)\\): \\(2(x-1)+(y-4)=0\\iff2x+y-6=0\\).'), T('\\(M(1;1)\\); \\(A\\) and \\(M\\) both have \\(x=1\\), so \\(AM: x-1=0\\).', '\\(M(1;1)\\); \\(A\\) và \\(M\\) cùng hoành độ 1 nên \\(AM: x-1=0\\).')],
  T('\\(AH: 2x+y-6=0\\); \\(AM: x-1=0\\).', '\\(AH: 2x+y-6=0\\); \\(AM: x-1=0\\).'))
k5 = F(54 - 30, 5 - 2); assert k5 == 8 and 30 - 8 * 2 == 14 and 8 * 10 + 14 == 94
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Taxi fares', 'Cước taxi'), T('A taxi fare \\(y\\) (thousand VND) depends linearly on the distance \\(x\\) (km). A 2 km trip costs 30 thousand and a 5 km trip costs 54 thousand. Write the equation of the line and find the fare for 10 km.', 'Giá cước taxi \\(y\\) (nghìn đồng) phụ thuộc bậc nhất vào quãng đường \\(x\\) (km). Đi 2 km hết 30 nghìn, đi 5 km hết 54 nghìn. Viết phương trình đường thẳng biểu diễn và tính tiền đi 10 km.'),
  T('The line passes through \\((2;30)\\) and \\((5;54)\\).', 'Đường thẳng đi qua \\((2;30)\\) và \\((5;54)\\).'), [T('\\(k=\\dfrac{54-30}{5-2}=8\\); \\(y=8x+m\\), \\(30=16+m\\Rightarrow m=14\\).', '\\(k=\\dfrac{54-30}{5-2}=8\\); \\(y=8x+m\\), \\(30=16+m\\Rightarrow m=14\\).'), T('General form \\(8x-y+14=0\\); \\(x=10\\Rightarrow y=94\\).', 'Dạng tổng quát \\(8x-y+14=0\\); \\(x=10\\Rightarrow y=94\\).')],
  T('\\(y=8x+14\\); 10 km costs 94 thousand VND (8 thousand per km plus 14 thousand opening fee).', '\\(y=8x+14\\); đi 10 km hết 94 nghìn đồng (8 nghìn/km cộng 14 nghìn phí mở cửa).'))

def lvl(P):
    (a1, b1, c1), k1 = P['nv']
    o1 = M4(1, 'A normal vector of \\(%s\\) is…' % leq(a1, b1, c1), 'Một vectơ pháp tuyến của đường thẳng \\(%s\\) là…' % leq(a1, b1, c1), '\\(\\vec n=%s\\)' % V2((k1 * a1, k1 * b1)),
            ['\\(\\vec n=%s\\)' % V2((b1, -a1)), '\\(\\vec n=%s\\)' % V2((a1, c1)), '\\(\\vec n=%s\\)' % V2((-b1, a1)), '\\(\\vec n=%s\\)' % V2((a1, -b1))], '\\(\\vec n=(a;b)=%s\\) or a multiple.' % V2((a1, b1)), '\\(\\vec n=(a;b)=%s\\) hoặc bội khác 0.' % V2((a1, b1)))
    A, B = P['two']; u = (B[0] - A[0], B[1] - A[1]); a2, b2, c2 = norm3(u[1], -u[0], -(u[1] * A[0] - u[0] * A[1]))
    o2 = M4(2, 'The line through \\(A%s\\) and \\(B%s\\) is…' % (V2(A), V2(B)), 'Đường thẳng qua \\(A%s\\) và \\(B%s\\) có phương trình…' % (V2(A), V2(B)), '\\(%s\\)' % leq(a2, b2, c2),
            ['\\(%s\\)' % leq(*norm3(u[0], u[1], -(u[0] * A[0] + u[1] * A[1]))), '\\(%s\\)' % leq(*norm3(a2, b2, -c2 if c2 else 1)), '\\(%s\\)' % leq(*norm3(b2, a2, c2 + 1))],
            '\\(\\overrightarrow{AB}=%s\\Rightarrow\\vec n=%s\\).' % (V2(u), V2((u[1], -u[0]))), '\\(\\overrightarrow{AB}=%s\\Rightarrow\\vec n=%s\\).' % (V2(u), V2((u[1], -u[0]))))
    A3, B3 = P['slope']; k = F(B3[1] - A3[1], B3[0] - A3[0])
    o3 = M4(3, 'The slope of the line through \\(A%s\\) and \\(B%s\\) is…' % (V2(A3), V2(B3)), 'Hệ số góc của đường thẳng qua \\(A%s\\) và \\(B%s\\) là…' % (V2(A3), V2(B3)), '\\(%s\\)' % fr(k),
            ['\\(%s\\)' % fr(1 / k), '\\(%s\\)' % fr(-k), '\\(%s\\)' % fr(-1 / k)], '\\(k=\\dfrac{y_B-y_A}{x_B-x_A}\\).', '\\(k=\\dfrac{y_B-y_A}{x_B-x_A}\\).')
    (a4, b4, c4), u4 = P['dir']; truth4 = a4 * u4[0] + b4 * u4[1] == 0
    t4 = tf(4, '\\(\\vec u=%s\\) is a direction vector of \\(%s\\).' % (V2(u4), leq(a4, b4, c4)), '\\(\\vec u=%s\\) là một vectơ chỉ phương của đường thẳng \\(%s\\).' % (V2(u4), leq(a4, b4, c4)), truth4,
            '\\(\\vec n\\cdot\\vec u=%d\\).' % (a4 * u4[0] + b4 * u4[1]), '\\(\\vec n\\cdot\\vec u=%d\\).' % (a4 * u4[0] + b4 * u4[1]))
    M5, u5, Q5 = P['on']; t = F(Q5[0] - M5[0], u5[0]); truth5 = M5[1] + t * u5[1] == Q5[1]
    t5 = tf(5, 'The point \\(%s\\) lies on \\(%s\\).' % (V2(Q5), pr2(M5, u5)), 'Điểm \\(%s\\) thuộc đường thẳng \\(%s\\).' % (V2(Q5), pr2(M5, u5)), truth5,
            'From \\(x\\): \\(t=%s\\); then \\(y=%s\\).' % (fr(t), fr(M5[1] + t * u5[1])), 'Từ \\(x\\): \\(t=%s\\); khi đó \\(y=%s\\).' % (fr(t), fr(M5[1] + t * u5[1])))
    M6, n6 = P['c']; c6 = -(n6[0] * M6[0] + n6[1] * M6[1])
    s6 = sh(6, 'The line through \\(M%s\\) with normal vector \\(\\vec n=%s\\) is \\(%dx%+dy+c=0\\). Find \\(c\\).' % (V2(M6), V2(n6), n6[0], n6[1]), 'Đường thẳng qua \\(M%s\\), có vectơ pháp tuyến \\(\\vec n=%s\\) có phương trình \\(%dx%+dy+c=0\\). Tìm \\(c\\).' % (V2(M6), V2(n6), n6[0], n6[1]), c6,
            '\\(c=-(%d\\cdot%d%+d\\cdot%d)=%d\\).' % (n6[0], M6[0], n6[1], M6[1], c6), '\\(c=-(%d\\cdot%d%+d\\cdot%d)=%d\\).' % (n6[0], M6[0], n6[1], M6[1], c6))
    (x1, y1), (x2, y2), x7 = P['taxi']; k7 = F(y2 - y1, x2 - x1); m7 = y1 - k7 * x1; y7 = k7 * x7 + m7; assert y7.denominator == 1
    s7 = sh(7, 'A fare \\(y\\) (thousand VND) is linear in the distance \\(x\\) (km): %d km costs %d, %d km costs %d. Find the fare for %d km.' % (x1, y1, x2, y2, x7), 'Cước \\(y\\) (nghìn đồng) phụ thuộc bậc nhất vào quãng đường \\(x\\) (km): đi %d km hết %d, đi %d km hết %d. Tính tiền đi %d km.' % (x1, y1, x2, y2, x7), int(y7),
            '\\(y=%sx%+d\\).' % (fr(k7), int(m7)), '\\(y=%sx%+d\\), \\(x=%d\\Rightarrow y=%d\\).' % (fr(k7), int(m7), x7, int(y7)))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
PP = [dict(nv=((3, -2, 5), 2), two=((1, 1), (3, 5)), slope=((0, 1), (2, 7)), dir=((2, -1, 3), (1, 2)), on=((1, 2), (2, -1), (5, 0)), c=((1, 2), (2, 3)), taxi=((2, 26), (6, 58), 10)),
      dict(nv=((1, 4, -3), -1), two=((-2, 3), (1, 0)), slope=((1, -2), (4, 4)), dir=((3, 1, -2), (3, 1)), on=((0, -1), (3, 2), (6, 4)), c=((-1, 3), (4, -1)), taxi=((3, 33), (7, 61), 12)),
      dict(nv=((5, 2, 1), 3), two=((0, -3), (4, 1)), slope=((-1, 3), (3, -5)), dir=((1, -3, 4), (3, 1)), on=((2, 0), (1, -2), (4, -5)), c=((2, -2), (-3, 5)), taxi=((1, 20), (5, 52), 8))]
practice = three(lvl, PP)
practice = with_self(practice, S.M19S10, start=8)
mistakes = [('<b>Using \\((a;b)\\) as a direction vector of \\(ax+by+c=0\\).</b> \\((a;b)\\) is the <i>normal</i> vector; \\(\\vec u=(b;-a)\\).', '<b>Lấy \\((a;b)\\) làm vectơ chỉ phương của \\(ax+by+c=0\\).</b> \\((a;b)\\) là vectơ <i>pháp tuyến</i>; \\(\\vec u=(b;-a)\\).'),
            ('<b>Writing the general equation with \\(\\overrightarrow{AB}\\) as normal vector.</b> \\(\\overrightarrow{AB}\\) is a direction vector; swap and change one sign.', '<b>Dùng \\(\\overrightarrow{AB}\\) làm vectơ pháp tuyến.</b> \\(\\overrightarrow{AB}\\) là vectơ chỉ phương; đổi chỗ hai tọa độ và đổi dấu một tọa độ.'),
            ('<b>Sign errors in \\(a(x-x_0)+b(y-y_0)=0\\).</b> For \\(M(2;-1)\\): \\(a(x-2)+b(y+1)=0\\).', '<b>Sai dấu trong \\(a(x-x_0)+b(y-y_0)=0\\).</b> Với \\(M(2;-1)\\): \\(a(x-2)+b(y+1)=0\\).'),
            ('<b>Slope of a vertical line.</b> \\(x=c\\) has no slope.', '<b>Hệ số góc của đường thẳng đứng.</b> Đường thẳng \\(x=c\\) không có hệ số góc.')]
summary = [('Parametric: \\(x=x_0+at\\), \\(y=y_0+bt\\) (\\(\\vec u=(a;b)\\)).', 'Tham số: \\(x=x_0+at\\), \\(y=y_0+bt\\) (\\(\\vec u=(a;b)\\)).'),
           ('General: \\(a(x-x_0)+b(y-y_0)=0\\) (\\(\\vec n=(a;b)\\)); \\(\\vec u=(b;-a)\\).', 'Tổng quát: \\(a(x-x_0)+b(y-y_0)=0\\) (\\(\\vec n=(a;b)\\)); \\(\\vec u=(b;-a)\\).'),
           ('Intercept form \\(\\frac xa+\\frac yb=1\\); slope form \\(y=kx+m\\), \\(k=\\frac{y_B-y_A}{x_B-x_A}\\).', 'Đoạn chắn \\(\\frac xa+\\frac yb=1\\); hệ số góc \\(y=kx+m\\), \\(k=\\frac{y_B-y_A}{x_B-x_A}\\).'),
           ('Key words: direction vector, normal vector, parametric, general equation, slope.', 'Từ cần nhớ: direction vector, normal vector, parametric, general equation, slope.')]
checks = [('I can read \\(\\vec n\\) and \\(\\vec u\\) from an equation.', 'Em đọc được \\(\\vec n\\), \\(\\vec u\\) từ phương trình.'), ('I can write parametric and general equations.', 'Em viết được phương trình tham số và tổng quát.'),
          ('I can write altitudes and medians of a triangle.', 'Em viết được phương trình đường cao, trung tuyến của tam giác.'), ('I can model a linear relation by a line.', 'Em mô hình hóa được quan hệ bậc nhất bằng đường thẳng.')]
LL('g10-coord-01', 'Equations of a Line', CV, ('Coordinate Geometry in the Plane', 'Phương pháp tọa độ trong mặt phẳng'), 'plane-coordinates', 'line-equations', 190, 'Intermediate', 70, ('vectors in the coordinate plane, dot product', 'vectơ trong mặt phẳng tọa độ, tích vô hướng'),
   'Direction and normal vectors; parametric, general, intercept and slope forms; altitudes and medians; linear models.', 'Bài 19 – Vectơ chỉ phương, vectơ pháp tuyến; phương trình tham số, tổng quát, đoạn chắn, hệ số góc; đường cao, trung tuyến; mô hình bậc nhất.',
   ['line', 'direction vector', 'normal vector', 'general equation'], ['đường thẳng', 'vectơ chỉ phương', 'vectơ pháp tuyến', 'phương trình tổng quát'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g10-vec-05'])
