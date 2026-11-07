# -*- coding: utf-8 -*-
"""g10-coord-03 = Toán 10 KNTT, Bài 21: Đường tròn trong mặt phẳng tọa độ. Mã ngân hàng câu hỏi: TOAN10-C7-B21."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g10h as S
from sp_g10h import ceq, cgen, rt
from sp_g10g import leq, V2

CV = 'Đường tròn trong mặt phẳng tọa độ'
vocab = defs(CV, [
 ('circeq', 'equation of a circle', 'phương trình đường tròn', '\\((x-a)^2+(y-b)^2=R^2\\): centre \\(I(a;b)\\), radius \\(R\\).', '\\((x-a)^2+(y-b)^2=R^2\\): tâm \\(I(a;b)\\), bán kính \\(R\\).', 'Write the equation of the circle.', ''),
 ('tancirc', 'tangent line to a circle', 'tiếp tuyến của đường tròn', 'a line with exactly one common point with the circle; it is perpendicular to the radius at that point.', 'đường thẳng có đúng một điểm chung với đường tròn; vuông góc với bán kính tại tiếp điểm.', 'Write the tangent at M.', ''),
 ('chord', 'chord', 'dây cung', 'a segment joining two points of a circle.', 'đoạn thẳng nối hai điểm của đường tròn.', 'The chord has length 8.', '')])
goals = [('recognise the equation of a circle and read its centre and radius;', 'nhận biết [[phương trình đường tròn]], xác định tâm và bán kính;'),
         ('write the equation of a circle from given data (centre and point, diameter, three points);', 'viết phương trình đường tròn khi biết tâm và một điểm, đường kính, ba điểm;'),
         ('write a [[tiếp tuyến của đường tròn|tiếp tuyến của đường tròn]] and decide the position of a line and a circle;', 'viết [[tiếp tuyến của đường tròn]] và xét vị trí tương đối giữa đường thẳng và đường tròn;'),
         ('solve real problems on coverage areas and chords.', 'giải bài toán thực tế về vùng phủ sóng, [[dây cung]].')]
goals[2] = ('write a tangent line to a circle and decide the position of a line and a circle;', goals[2][1])
phrases = [('<b>The centre is \\(I(2;-1)\\) and the radius is three.</b>', 'Tâm là \\(I(2;-1)\\), bán kính bằng 3.'), ('<b>The tangent is perpendicular to the radius.</b>', 'Tiếp tuyến vuông góc với bán kính tại tiếp điểm.'),
           ('<b>The line is tangent to the circle.</b>', 'Đường thẳng tiếp xúc với đường tròn.'), ('<b>Compare the distance with the radius.</b>', 'So sánh khoảng cách với bán kính.'), ('<b>The line cuts the circle at two points.</b>', 'Đường thẳng cắt đường tròn tại hai điểm.')]
review = T('From Bài 10: \\(AB=\\sqrt{(x_B-x_A)^2+(y_B-y_A)^2}\\). From Bài 20: \\(d(M,\\Delta)=\\dfrac{|ax_0+by_0+c|}{\\sqrt{a^2+b^2}}\\). Grade 9: a circle is the set of points at distance \\(R\\) from the centre.',
           'Từ Bài 10: \\(AB=\\sqrt{(x_B-x_A)^2+(y_B-y_A)^2}\\). Từ Bài 20: \\(d(M,\\Delta)=\\dfrac{|ax_0+by_0+c|}{\\sqrt{a^2+b^2}}\\). Lớp 9: đường tròn là tập hợp các điểm cách tâm một khoảng \\(R\\).')
theory = '<h3>21.1 %s</h3>' % TI('Equation of a circle', 'Phương trình đường tròn')
theory += BOX('blue', ('Two forms', 'Hai dạng'), UL([T('\\(M(x;y)\\) lies on the circle with centre \\(I(a;b)\\), radius \\(R\\) \\(\\iff IM=R\\iff(x-a)^2+(y-b)^2=R^2\\).', '\\(M(x;y)\\) thuộc đường tròn tâm \\(I(a;b)\\), bán kính \\(R\\) \\(\\iff IM=R\\iff(x-a)^2+(y-b)^2=R^2\\).'),
  T('Expanding: \\(x^2+y^2-2ax-2by+c=0\\) with \\(c=a^2+b^2-R^2\\). Conversely, this equation is a circle <b>only if</b> \\(a^2+b^2-c\\gt0\\); then \\(I(a;b)\\), \\(R=\\sqrt{a^2+b^2-c}\\).', 'Khai triển: \\(x^2+y^2-2ax-2by+c=0\\) với \\(c=a^2+b^2-R^2\\). Ngược lại, phương trình này là đường tròn <b>khi và chỉ khi</b> \\(a^2+b^2-c\\gt0\\); khi đó \\(I(a;b)\\), \\(R=\\sqrt{a^2+b^2-c}\\).')]))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('Read the centre with the opposite signs: \\((x+1)^2+(y-3)^2=16\\) has \\(I(-1;3)\\). A circle equation has the same coefficient for \\(x^2\\) and \\(y^2\\) and no \\(xy\\) term.', 'Đọc tâm với dấu ngược lại: \\((x+1)^2+(y-3)^2=16\\) có \\(I(-1;3)\\). Phương trình đường tròn có hệ số của \\(x^2\\), \\(y^2\\) bằng nhau và không có hạng tử \\(xy\\).'))
theory += '<h3>21.2 %s</h3>' % TI('Tangent lines; a line and a circle', 'Tiếp tuyến; đường thẳng và đường tròn')
theory += BOX('blue', ('Rules', 'Quy tắc'), UL([T('The tangent at \\(M_0(x_0;y_0)\\) of the circle with centre \\(I(a;b)\\) passes through \\(M_0\\) with normal vector \\(\\overrightarrow{IM_0}\\): \\((x_0-a)(x-x_0)+(y_0-b)(y-y_0)=0\\).', 'Tiếp tuyến tại \\(M_0(x_0;y_0)\\) của đường tròn tâm \\(I(a;b)\\) đi qua \\(M_0\\), nhận \\(\\overrightarrow{IM_0}\\) làm vectơ pháp tuyến: \\((x_0-a)(x-x_0)+(y_0-b)(y-y_0)=0\\).'),
  T('Let \\(d=d(I,\\Delta)\\). \\(d\\lt R\\): \\(\\Delta\\) cuts the circle at two points (chord length \\(2\\sqrt{R^2-d^2}\\)); \\(d=R\\): \\(\\Delta\\) is tangent; \\(d\\gt R\\): no common point.', 'Đặt \\(d=d(I,\\Delta)\\). \\(d\\lt R\\): \\(\\Delta\\) cắt đường tròn tại hai điểm (dây cung dài \\(2\\sqrt{R^2-d^2}\\)); \\(d=R\\): \\(\\Delta\\) tiếp xúc; \\(d\\gt R\\): không có điểm chung.')]))
theory += GEO({'view': [-4.5, 9, -5, 8.5], 'axes': True, 'steps': [
  {'type': 'point', 'id': 'I', 'at': [2, 1], 'name': 'I(2; 1)'}, {'type': 'point', 'id': 'M', 'at': [5, 5], 'name': 'M(5; 5)', 'off': [10, 6]},
  {'type': 'circle', 'id': 'c', 'center': 'I', 'through': 'M'}, {'type': 'tangent', 'center': 'I', 'at': 'M', 'showRadius': True},
  {'type': 'text', 'at': [5.6, 7.6], 'text': '3x + 4y − 35 = 0'}]},
  cap=('Circle \\((x-2)^2+(y-1)^2=25\\). The tangent at \\(M(5;5)\\) has normal vector \\(\\overrightarrow{IM}=(3;4)\\): \\(3x+4y-35=0\\).', 'Đường tròn \\((x-2)^2+(y-1)^2=25\\). Tiếp tuyến tại \\(M(5;5)\\) nhận \\(\\overrightarrow{IM}=(3;4)\\) làm vectơ pháp tuyến: \\(3x+4y-35=0\\).'),
  alt=('Circle with centre I and the tangent line at M', ''), height=340)
assert 3 * 5 + 4 * 5 - 35 == 0

assert 4 + 9 + 3 == 16
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Centre and radius', 'Tâm và bán kính'), T('Find the centre and radius: a) \\((x+1)^2+(y-3)^2=16\\); b) \\(x^2+y^2-4x+6y-3=0\\).', 'Tìm tâm và bán kính: a) \\((x+1)^2+(y-3)^2=16\\); b) \\(x^2+y^2-4x+6y-3=0\\).'),
  T('b) \\(-2a=-4\\), \\(-2b=6\\), \\(c=-3\\).', 'b) \\(-2a=-4\\), \\(-2b=6\\), \\(c=-3\\).'),
  [T('a) \\(I(-1;3)\\), \\(R=4\\).', 'a) \\(I(-1;3)\\), \\(R=4\\).'), T('b) \\(a=2\\), \\(b=-3\\); \\(a^2+b^2-c=4+9+3=16\\gt0\\): \\(I(2;-3)\\), \\(R=4\\).', 'b) \\(a=2\\), \\(b=-3\\); \\(a^2+b^2-c=4+9+3=16\\gt0\\): \\(I(2;-3)\\), \\(R=4\\).')],
  T('a) \\(I(-1;3)\\), \\(R=4\\); b) \\(I(2;-3)\\), \\(R=4\\).', 'a) \\(I(-1;3)\\), \\(R=4\\); b) \\(I(2;-3)\\), \\(R=4\\).'))
assert 3 ** 2 + 4 ** 2 == 25
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Centre and a point', 'Biết tâm và một điểm'), T('Write the equation of the circle with centre \\(I(1;-2)\\) passing through \\(A(4;2)\\).', 'Viết phương trình đường tròn tâm \\(I(1;-2)\\) và đi qua \\(A(4;2)\\).'),
  T('\\(R=IA\\).', '\\(R=IA\\).'), [T('\\(\\overrightarrow{IA}=(3;4)\\), \\(R^2=9+16=25\\).', '\\(\\overrightarrow{IA}=(3;4)\\), \\(R^2=9+16=25\\).')],
  T('\\((x-1)^2+(y+2)^2=25\\).', '\\((x-1)^2+(y+2)^2=25\\).'))
for X, Y in ((1, 2), (5, 2), (1, -2)): assert X * X + Y * Y - 6 * X + 1 == 0
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Circle through three points', 'Đường tròn qua ba điểm'), T('Write the equation of the circle through \\(A(1;2)\\), \\(B(5;2)\\), \\(C(1;-2)\\).', 'Viết phương trình đường tròn đi qua ba điểm \\(A(1;2)\\), \\(B(5;2)\\), \\(C(1;-2)\\).'),
  T('Use \\(x^2+y^2-2ax-2by+c=0\\) and substitute the three points.', 'Dùng dạng \\(x^2+y^2-2ax-2by+c=0\\), thay tọa độ ba điểm.'),
  [T('\\(A\\): \\(5-2a-4b+c=0\\); \\(B\\): \\(29-10a-4b+c=0\\); \\(C\\): \\(5-2a+4b+c=0\\).', '\\(A\\): \\(5-2a-4b+c=0\\); \\(B\\): \\(29-10a-4b+c=0\\); \\(C\\): \\(5-2a+4b+c=0\\).'),
   T('\\(A-C\\): \\(b=0\\); \\(B-A\\): \\(24-8a=0\\Rightarrow a=3\\); then \\(c=1\\).', 'Trừ \\(A\\) cho \\(C\\): \\(b=0\\); trừ \\(B\\) cho \\(A\\): \\(24-8a=0\\Rightarrow a=3\\); suy ra \\(c=1\\).'),
   T('\\(I(3;0)\\), \\(R^2=9-1=8\\). (Here \\(\\widehat{BAC}=90^\\circ\\), so \\(BC\\) is a diameter.)', '\\(I(3;0)\\), \\(R^2=9-1=8\\). (Ở đây \\(\\widehat{BAC}=90^\\circ\\) nên \\(BC\\) là đường kính.)')],
  T('\\(x^2+y^2-6x+1=0\\), i.e. \\((x-3)^2+y^2=8\\).', '\\(x^2+y^2-6x+1=0\\), tức \\((x-3)^2+y^2=8\\).'))
assert abs(3 * 2 - 4 * 1 + 23) == 25
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Tangent lines', 'Tiếp tuyến'), T('For \\((C): (x-2)^2+(y-1)^2=25\\): a) write the tangent at \\(M(5;5)\\); b) show that \\(\\Delta: 3x-4y+23=0\\) is tangent to \\((C)\\).', 'Cho \\((C): (x-2)^2+(y-1)^2=25\\). a) Viết tiếp tuyến tại \\(M(5;5)\\). b) Chứng minh \\(\\Delta: 3x-4y+23=0\\) tiếp xúc với \\((C)\\).'),
  T('a) normal vector \\(\\overrightarrow{IM}\\); b) compare \\(d(I,\\Delta)\\) with \\(R=5\\).', 'a) vectơ pháp tuyến \\(\\overrightarrow{IM}\\); b) so sánh \\(d(I,\\Delta)\\) với \\(R=5\\).'),
  [T('a) \\((5-2)^2+(5-1)^2=25\\) ✓; \\(3(x-5)+4(y-5)=0\\iff3x+4y-35=0\\).', 'a) \\((5-2)^2+(5-1)^2=25\\) ✓; \\(3(x-5)+4(y-5)=0\\iff3x+4y-35=0\\).'), T('b) \\(d(I,\\Delta)=\\dfrac{|6-4+23|}{5}=5=R\\).', 'b) \\(d(I,\\Delta)=\\dfrac{|6-4+23|}{5}=5=R\\).')],
  T('a) \\(3x+4y-35=0\\); b) \\(d=R\\), so \\(\\Delta\\) is tangent.', 'a) \\(3x+4y-35=0\\); b) \\(d=R\\) nên \\(\\Delta\\) tiếp xúc với \\((C)\\).'))
d5 = F(abs(2 - 3 + 6) ** 2, 2); assert d5 == F(25, 2) and 25 - d5 == F(25, 2)
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Signal along a road', 'Sóng điện thoại dọc con đường'), T('A mobile mast at \\(I(2;3)\\) (unit 1 km) covers a disc of radius 5 km. A straight road runs along \\(d: x-y+6=0\\). How long is the part of the road with signal?', 'Một trạm phát sóng đặt tại \\(I(2;3)\\) (đơn vị 1 km) phủ sóng một hình tròn bán kính 5 km. Một con đường thẳng chạy theo \\(d: x-y+6=0\\). Đoạn đường có sóng dài bao nhiêu?'),
  T('The covered part is the chord cut by \\(d\\): length \\(2\\sqrt{R^2-h^2}\\), \\(h=d(I,d)\\).', 'Đoạn có sóng là dây cung do \\(d\\) cắt: dài \\(2\\sqrt{R^2-h^2}\\) với \\(h=d(I,d)\\).'),
  [T('\\(h=\\dfrac{|2-3+6|}{\\sqrt2}=\\dfrac5{\\sqrt2}\\lt5\\): the road enters the area.', '\\(h=\\dfrac{|2-3+6|}{\\sqrt2}=\\dfrac5{\\sqrt2}\\lt5\\): con đường đi vào vùng phủ sóng.'), T('Length \\(=2\\sqrt{25-\\frac{25}2}=2\\cdot\\dfrac5{\\sqrt2}=5\\sqrt2\\approx7{,}07\\) km.', 'Độ dài \\(=2\\sqrt{25-\\frac{25}2}=2\\cdot\\dfrac5{\\sqrt2}=5\\sqrt2\\approx7{,}07\\) km.')],
  T('\\(5\\sqrt2\\approx7{,}07\\) km.', '\\(5\\sqrt2\\approx7{,}07\\) km.'))


def lvl(P):
    a, b, R = P['std']
    o = lambda A, B, RR: ('centre \\((%d;%d)\\), radius \\(%s\\)' % (A, B, RR), 'tâm \\((%d;%d)\\), bán kính \\(%s\\)' % (A, B, RR))
    o1 = M4(1, 'The circle \\(%s\\) has…' % ceq(a, b, R * R), 'Đường tròn \\(%s\\) có…' % ceq(a, b, R * R), TI(*o(a, b, R)), [TI(*o(-a, -b, R)), TI(*o(a, b, R * R)), TI(*o(-a, -b, R * R))],
            'Centre \\((a;b)\\), radius \\(R=\\sqrt{%d}\\).' % (R * R), 'Tâm \\((a;b)=(%d;%d)\\), bán kính \\(R=\\sqrt{%d}=%d\\).' % (a, b, R * R, R))
    a2, b2, R2 = P['gen']; c2 = a2 * a2 + b2 * b2 - R2 * R2
    o2 = M4(2, 'The circle \\(%s\\) has…' % cgen(a2, b2, c2), 'Đường tròn \\(%s\\) có…' % cgen(a2, b2, c2), TI(*o(a2, b2, R2)), [TI(*o(-a2, -b2, R2)), TI(*o(2 * a2, 2 * b2, R2)), TI(*o(a2, b2, rt(abs(c2))))],
            '\\(a=%d\\), \\(b=%d\\), \\(R=\\sqrt{a^2+b^2-c}\\).' % (a2, b2), '\\(a=%d\\), \\(b=%d\\), \\(R=\\sqrt{a^2+b^2-c}=\\sqrt{%d}=%d\\).' % (a2, b2, R2 * R2, R2))
    I, A = P['circ']; RR = (A[0] - I[0]) ** 2 + (A[1] - I[1]) ** 2
    o3 = M4(3, 'The circle with centre \\(I%s\\) through \\(A%s\\) is…' % (V2(I), V2(A)), 'Đường tròn tâm \\(I%s\\) đi qua \\(A%s\\) là…' % (V2(I), V2(A)), '\\(%s\\)' % ceq(*I, RR),
            ['\\(%s\\)' % ceq(-I[0], -I[1], RR), '\\(%s\\)' % ceq(*I, math.isqrt(RR)), '\\(%s\\)' % ceq(*A, RR)], '\\(R^2=IA^2=%d\\).' % RR, '\\(R^2=IA^2=%d\\).' % RR)
    (p, q, cc) = P['isc']; val = p * p + q * q - cc
    t4 = tf(4, '\\(%s\\) is the equation of a circle.' % cgen(p, q, cc), '\\(%s\\) là phương trình của một đường tròn.' % cgen(p, q, cc), val > 0,
            '\\(a^2+b^2-c=%d\\).' % val, '\\(a^2+b^2-c=%d\\)%s.' % (val, '\\(\\gt0\\)' if val > 0 else '\\(\\le0\\)'))
    J, RJ, (u, v, w) = P['tan']; dist = F(abs(u * J[0] + v * J[1] + w), math.isqrt(u * u + v * v))
    t5 = tf(5, 'The line \\(%s\\) is tangent to \\(%s\\).' % (leq(u, v, w), ceq(*J, RJ * RJ)), 'Đường thẳng \\(%s\\) tiếp xúc với đường tròn \\(%s\\).' % (leq(u, v, w), ceq(*J, RJ * RJ)), dist == RJ,
            '\\(d(I,\\Delta)=%s\\), \\(R=%d\\).' % (fr(dist), RJ), '\\(d(I,\\Delta)=%s\\), \\(R=%d\\).' % (fr(dist), RJ))
    (e, f, g) = P['rad']; R6 = math.isqrt(e * e + f * f - g); assert R6 * R6 == e * e + f * f - g
    s6 = sh(6, 'Find the radius of the circle \\(%s\\).' % cgen(e, f, g), 'Tìm bán kính của đường tròn \\(%s\\).' % cgen(e, f, g), R6,
            '\\(R=\\sqrt{a^2+b^2-c}\\).', '\\(R=\\sqrt{%d+%d-(%d)}=%d\\).' % (e * e, f * f, g, R6))
    K, RK, (h, i, j) = P['chord']; dd = F(abs(h * K[0] + i * K[1] + j), math.isqrt(h * h + i * i)); L = 2 * math.isqrt(int(RK * RK - dd * dd)); assert dd.denominator == 1 and (L // 2) ** 2 == RK * RK - dd * dd
    s7 = sh(7, 'A mast at \\(I%s\\) (unit 1 km) covers a disc of radius %d km. How many kilometres of the road \\(%s\\) have signal?' % (V2(K), RK, leq(h, i, j)), 'Một trạm phát sóng tại \\(I%s\\) (đơn vị 1 km) phủ sóng hình tròn bán kính %d km. Con đường \\(%s\\) có bao nhiêu kilômét được phủ sóng?' % (V2(K), RK, leq(h, i, j)), L,
            '\\(d=%d\\), chord \\(2\\sqrt{R^2-d^2}\\).' % int(dd), '\\(d(I,\\Delta)=%d\\), dây cung dài \\(2\\sqrt{%d-%d}=%d\\).' % (int(dd), RK * RK, int(dd) ** 2, L))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]


PP = [dict(std=(2, -3, 4), gen=(1, 2, 3), circ=((1, 2), (4, 6)), isc=(1, -2, 6), tan=((1, 2), 5, (3, 4, 14)), rad=(-3, 4, 0), chord=((2, 1), 5, (3, 4, 5))),
      dict(std=(-1, 4, 3), gen=(-2, 3, 5), circ=((-2, 1), (3, -11)), isc=(2, -1, 1), tan=((0, 3), 4, (4, -3, 10)), rad=(5, -12, 0), chord=((1, 1), 13, (5, 12, 48))),
      dict(std=(3, 0, 5), gen=(4, -1, 2), circ=((0, -3), (6, 5)), isc=(-1, 3, 15), tan=((-1, 2), 2, (0, 1, -4)), rad=(3, -4, -11), chord=((3, -1), 10, (3, -4, 17)))]
practice = three(lvl, PP)
practice = with_self(practice, S.M21S10, start=8)
mistakes = [('<b>Reading the centre with the wrong signs.</b> \\((x-2)^2+(y+5)^2=9\\) has centre \\((2;-5)\\), not \\((-2;5)\\).', '<b>Đọc sai dấu tọa độ tâm.</b> \\((x-2)^2+(y+5)^2=9\\) có tâm \\((2;-5)\\), không phải \\((-2;5)\\).'),
            ('<b>Taking \\(R=R^2\\).</b> In \\((x-1)^2+y^2=9\\) the radius is 3, not 9.', '<b>Lấy \\(R\\) bằng \\(R^2\\).</b> Trong \\((x-1)^2+y^2=9\\) bán kính là 3, không phải 9.'),
            ('<b>Forgetting the condition \\(a^2+b^2-c\\gt0\\).</b> \\(x^2+y^2-2x+4y+6=0\\) is not a circle (\\(1+4-6\\lt0\\)).', '<b>Quên điều kiện \\(a^2+b^2-c\\gt0\\).</b> \\(x^2+y^2-2x+4y+6=0\\) không phải đường tròn (\\(1+4-6\\lt0\\)).'),
            ('<b>Using \\(\\overrightarrow{IM}\\) as a direction vector of the tangent.</b> It is the <i>normal</i> vector of the tangent.', '<b>Dùng \\(\\overrightarrow{IM}\\) làm vectơ chỉ phương của tiếp tuyến.</b> Đó là vectơ <i>pháp tuyến</i> của tiếp tuyến.')]
summary = [('\\((x-a)^2+(y-b)^2=R^2\\); \\(x^2+y^2-2ax-2by+c=0\\) with \\(R=\\sqrt{a^2+b^2-c}\\) (need \\(\\gt0\\)).', '\\((x-a)^2+(y-b)^2=R^2\\); \\(x^2+y^2-2ax-2by+c=0\\) với \\(R=\\sqrt{a^2+b^2-c}\\) (cần \\(\\gt0\\)).'),
           ('Tangent at \\(M_0\\): \\((x_0-a)(x-x_0)+(y_0-b)(y-y_0)=0\\).', 'Tiếp tuyến tại \\(M_0\\): \\((x_0-a)(x-x_0)+(y_0-b)(y-y_0)=0\\).'),
           ('Line and circle: compare \\(d(I,\\Delta)\\) with \\(R\\); chord \\(2\\sqrt{R^2-d^2}\\).', 'Đường thẳng và đường tròn: so sánh \\(d(I,\\Delta)\\) với \\(R\\); dây cung \\(2\\sqrt{R^2-d^2}\\).'),
           ('Key words: centre, radius, tangent, chord.', 'Từ cần nhớ: centre, radius, tangent, chord.')]
checks = [('I can read the centre and radius of a circle.', 'Em đọc được tâm và bán kính của đường tròn.'), ('I can write the equation of a circle from given data.', 'Em viết được phương trình đường tròn từ dữ kiện.'),
          ('I can write a tangent at a point of the circle.', 'Em viết được tiếp tuyến tại một điểm của đường tròn.'), ('I can decide the position of a line and a circle.', 'Em xét được vị trí tương đối của đường thẳng và đường tròn.')]
LL('g10-coord-03', 'Circles in the Coordinate Plane', CV, ('Coordinate Geometry in the Plane', 'Phương pháp tọa độ trong mặt phẳng'), 'plane-coordinates', 'circles', 210, 'Intermediate', 70, ('distance, equations of a line', 'khoảng cách, phương trình đường thẳng'),
   'Equation of a circle, centre and radius, tangent lines, a line and a circle, chords.', 'Bài 21 – Phương trình đường tròn, tâm và bán kính, tiếp tuyến, vị trí tương đối giữa đường thẳng và đường tròn.',
   ['circle', 'centre', 'radius', 'tangent'], ['đường tròn', 'tâm', 'bán kính', 'tiếp tuyến'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g10-coord-02'])
