# -*- coding: utf-8 -*-
"""g11-perp-01 = Toán 11 KNTT, Bài 22: Hai đường thẳng vuông góc. Mã ngân hàng câu hỏi: TOAN11-C7-B22."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
from mb_solids import fig, FILL, HL, BL, GR
import sp_g11h as S

CV = 'Hai đường thẳng vuông góc'
vocab = defs(CV, [
 ('anglsp', 'angle between two lines in space', 'góc giữa hai đường thẳng trong không gian', 'the angle between two intersecting lines through any point \\(O\\), parallel to the given lines; from \\(0^\\circ\\) to \\(90^\\circ\\).', 'góc giữa hai đường thẳng cùng đi qua một điểm \\(O\\) và lần lượt song song (hoặc trùng) với hai đường thẳng đã cho; từ \\(0^\\circ\\) đến \\(90^\\circ\\).', 'The angle between AB and B′C′ is 90°.', '\\((a,b)\\)'),
 ('perpl', 'perpendicular lines (in space)', 'hai đường thẳng vuông góc (trong không gian)', 'two lines whose angle is \\(90^\\circ\\); they may not intersect.', 'hai đường thẳng tạo với nhau góc \\(90^\\circ\\); chúng có thể không cắt nhau.', 'AB and B′C′ are perpendicular.', '\\(a\\perp b\\)')])
goals = [('define the angle between two lines in space and recognise perpendicular lines;', 'nêu được định nghĩa [[góc giữa hai đường thẳng trong không gian]] và nhận biết [[hai đường thẳng vuông góc (trong không gian)|hai đường thẳng vuông góc (trong không gian)]];'),
         ('compute that angle by translating one line to meet the other;', 'tính góc đó bằng cách dựng đường thẳng song song để đưa về hai đường cắt nhau;'),
         ('prove that two lines are perpendicular in cubes, pyramids and tetrahedra;', 'chứng minh hai đường thẳng vuông góc trong hình lập phương, hình chóp, tứ diện;'),
         ('use right angles of real structures (beams, frames, rooms).', 'nhận ra và vận dụng góc vuông trong các kết cấu thực tế (dầm, khung, phòng).')]
phrases = [('<b>The two lines are perpendicular although they do not meet.</b>', 'Hai đường thẳng vuông góc dù không cắt nhau.'), ('<b>Draw a line through \\(B\\) parallel to \\(CD\\).</b>', 'Qua \\(B\\) kẻ đường thẳng song song với \\(CD\\).'),
           ('<b>The angle between the lines is sixty degrees.</b>', 'Góc giữa hai đường thẳng bằng 60°.'), ('<b>The triangle is equilateral.</b>', 'Tam giác đó là tam giác đều.'), ('<b>An angle between two lines is never obtuse.</b>', 'Góc giữa hai đường thẳng không bao giờ là góc tù.')]
review = T('From Bài 11: two lines in space can intersect, be parallel, coincide or be skew. Plane geometry: the angle between two intersecting lines is the smaller of the angles they form (\\(\\le90^\\circ\\)).',
           'Từ Bài 11: hai đường thẳng trong không gian có thể cắt nhau, song song, trùng nhau hoặc chéo nhau. Hình học phẳng: góc giữa hai đường thẳng cắt nhau là góc nhỏ hơn trong các góc chúng tạo thành (\\(\\le90^\\circ\\)).')
theory = '<h3>22.1 %s</h3>' % TI('The angle between two lines in space', 'Góc giữa hai đường thẳng trong không gian')
theory += BOX('blue', ('Definition', 'Định nghĩa'), UL([T('The angle between \\(a\\) and \\(b\\), written \\((a,b)\\), is the angle between two lines \\(a\'\\), \\(b\'\\) through one point \\(O\\) with \\(a\'\\parallel a\\) (or \\(a\'\\equiv a\\)) and \\(b\'\\parallel b\\) (or \\(b\'\\equiv b\\)). It does not depend on \\(O\\).',
   'Góc giữa hai đường thẳng \\(a\\) và \\(b\\), kí hiệu \\((a,b)\\), là góc giữa hai đường thẳng \\(a\'\\), \\(b\'\\) cùng đi qua một điểm \\(O\\) và lần lượt song song (hoặc trùng) với \\(a\\), \\(b\\). Góc này không phụ thuộc vào cách chọn \\(O\\).'),
  T('\\(0^\\circ\\le(a,b)\\le90^\\circ\\); parallel or coincident lines make \\(0^\\circ\\).', '\\(0^\\circ\\le(a,b)\\le90^\\circ\\); hai đường thẳng song song hoặc trùng nhau tạo góc \\(0^\\circ\\).'),
  T('In practice choose \\(O\\) on one of the lines and draw through it a parallel to the other line; then solve a triangle.', 'Thực hành: chọn \\(O\\) nằm trên một trong hai đường thẳng, qua \\(O\\) kẻ đường song song với đường còn lại, rồi giải tam giác.')]))
theory += '<h3>22.2 %s</h3>' % TI('Perpendicular lines', 'Hai đường thẳng vuông góc')
theory += BOX('blue', ('Definition and properties', 'Định nghĩa và tính chất'), UL([T('\\(a\\perp b\\iff(a,b)=90^\\circ\\). Perpendicular lines in space may intersect or be <b>skew</b>.', '\\(a\\perp b\\iff(a,b)=90^\\circ\\). Hai đường thẳng vuông góc trong không gian có thể cắt nhau hoặc <b>chéo nhau</b>.'),
  T('If \\(a\\parallel b\\) and \\(c\\perp a\\) then \\(c\\perp b\\).', 'Nếu \\(a\\parallel b\\) và \\(c\\perp a\\) thì \\(c\\perp b\\).'),
  T('Unlike in the plane, two lines perpendicular to a third line need <i>not</i> be parallel (the three edges at a corner of a cube).', 'Khác với trong mặt phẳng, hai đường thẳng cùng vuông góc với một đường thẳng thứ ba <i>chưa chắc</i> song song (ba cạnh xuất phát từ một đỉnh hình lập phương).')]))
theory += GEO3D(fig('cube', hl={('A', 'B'): HL, ('B′', 'C′'): BL, ('B', 'C'): GR}, right=[['A', 'B', 'C']]),
  cap=('\\(AB\\) and \\(B\'C\'\\) are skew. Since \\(B\'C\'\\parallel BC\\) and \\(AB\\perp BC\\): \\((AB,B\'C\')=(AB,BC)=90^\\circ\\).', '\\(AB\\) và \\(B\'C\'\\) chéo nhau. Vì \\(B\'C\'\\parallel BC\\) và \\(AB\\perp BC\\) nên \\((AB,B\'C\')=(AB,BC)=90^\\circ\\).'),
  alt=('Cube with the skew perpendicular edges AB and B′C′', ''), height=340)
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('If the triangle you build has an obtuse angle \\(\\alpha\\), the angle between the lines is \\(180^\\circ-\\alpha\\).', 'Nếu tam giác dựng được có góc tù \\(\\alpha\\) thì góc giữa hai đường thẳng là \\(180^\\circ-\\alpha\\).'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Angles in a cube', 'Góc trong hình lập phương'), T('In the cube \\(ABCD.A\'B\'C\'D\'\\), find \\((AB,C\'D\')\\), \\((AB,B\'C\')\\) and \\((AC,A\'D\')\\).', 'Cho hình lập phương \\(ABCD.A\'B\'C\'D\'\\). Tính \\((AB,C\'D\')\\), \\((AB,B\'C\')\\) và \\((AC,A\'D\')\\).'),
  T('Replace the second line by a parallel line through a point of the first.', 'Thay đường thứ hai bằng đường song song đi qua một điểm của đường thứ nhất.'),
  [T('\\(C\'D\'\\parallel CD\\parallel AB\\): \\((AB,C\'D\')=0^\\circ\\).', '\\(C\'D\'\\parallel CD\\parallel AB\\): \\((AB,C\'D\')=0^\\circ\\).'), T('\\(B\'C\'\\parallel BC\\): \\((AB,B\'C\')=\\widehat{ABC}=90^\\circ\\).', '\\(B\'C\'\\parallel BC\\): \\((AB,B\'C\')=\\widehat{ABC}=90^\\circ\\).'),
   T('\\(A\'D\'\\parallel AD\\): \\((AC,A\'D\')=\\widehat{CAD}=45^\\circ\\).', '\\(A\'D\'\\parallel AD\\): \\((AC,A\'D\')=\\widehat{CAD}=45^\\circ\\).')],
  T('\\(0^\\circ\\), \\(90^\\circ\\), \\(45^\\circ\\).', '\\(0^\\circ\\), \\(90^\\circ\\), \\(45^\\circ\\).'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Two face diagonals', 'Hai đường chéo mặt'), T('In the cube \\(ABCD.A\'B\'C\'D\'\\), find the angle between \\(A\'B\\) and \\(B\'C\\).', 'Cho hình lập phương \\(ABCD.A\'B\'C\'D\'\\). Tính góc giữa \\(A\'B\\) và \\(B\'C\\).'),
  T('\\(A\'D\'CB\\) is a rectangle, so \\(A\'B\\parallel D\'C\\).', '\\(A\'D\'CB\\) là hình chữ nhật nên \\(A\'B\\parallel D\'C\\).'),
  [T('\\((A\'B,B\'C)=(D\'C,B\'C)\\).', '\\((A\'B,B\'C)=(D\'C,B\'C)\\).'), T('\\(B\'C\\), \\(CD\'\\), \\(D\'B\'\\) are face diagonals, all equal to \\(a\\sqrt2\\): triangle \\(B\'CD\'\\) is equilateral, \\(\\widehat{B\'CD\'}=60^\\circ\\).', '\\(B\'C\\), \\(CD\'\\), \\(D\'B\'\\) là các đường chéo mặt, cùng bằng \\(a\\sqrt2\\): tam giác \\(B\'CD\'\\) đều, \\(\\widehat{B\'CD\'}=60^\\circ\\).')],
  T('\\((A\'B,B\'C)=60^\\circ\\).', '\\((A\'B,B\'C)=60^\\circ\\).'))
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('A pyramid with equal edges', 'Hình chóp có các cạnh bằng nhau'), T('\\(S.ABCD\\) has a square base of side \\(a\\) and \\(SA=SB=SC=SD=a\\). Find \\((SA,BC)\\) and \\((SA,SC)\\).', 'Hình chóp \\(S.ABCD\\) có đáy là hình vuông cạnh \\(a\\) và \\(SA=SB=SC=SD=a\\). Tính \\((SA,BC)\\) và \\((SA,SC)\\).'),
  T('\\(BC\\parallel AD\\); compare \\(SA^2+SC^2\\) with \\(AC^2\\).', '\\(BC\\parallel AD\\); so sánh \\(SA^2+SC^2\\) với \\(AC^2\\).'),
  [T('Triangle \\(SAD\\) is equilateral: \\((SA,BC)=(SA,AD)=\\widehat{SAD}=60^\\circ\\).', 'Tam giác \\(SAD\\) đều: \\((SA,BC)=(SA,AD)=\\widehat{SAD}=60^\\circ\\).'), T('\\(SA^2+SC^2=2a^2=AC^2\\): by the converse of Pythagoras \\(\\widehat{ASC}=90^\\circ\\).', '\\(SA^2+SC^2=2a^2=AC^2\\): theo định lí Pythagore đảo, \\(\\widehat{ASC}=90^\\circ\\).')],
  T('\\(60^\\circ\\) and \\(90^\\circ\\).', '\\(60^\\circ\\) và \\(90^\\circ\\).'))
assert F(1 + 1 - 3, 2) == F(-1, 2)
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Using midpoints', 'Dùng trung điểm'), T('Tetrahedron \\(ABCD\\): \\(AB=CD=2a\\); \\(M\\), \\(N\\) are the midpoints of \\(BC\\), \\(AD\\) and \\(MN=a\\sqrt3\\). Find \\((AB,CD)\\).', 'Tứ diện \\(ABCD\\) có \\(AB=CD=2a\\); \\(M\\), \\(N\\) lần lượt là trung điểm của \\(BC\\), \\(AD\\) và \\(MN=a\\sqrt3\\). Tính \\((AB,CD)\\).'),
  T('Take \\(P\\), the midpoint of \\(AC\\): \\(PM\\parallel AB\\), \\(PN\\parallel CD\\) (midlines).', 'Lấy \\(P\\) là trung điểm \\(AC\\): \\(PM\\parallel AB\\), \\(PN\\parallel CD\\) (đường trung bình).'),
  [T('\\(PM=\\frac12AB=a\\), \\(PN=\\frac12CD=a\\).', '\\(PM=\\frac12AB=a\\), \\(PN=\\frac12CD=a\\).'), T('\\(\\cos\\widehat{MPN}=\\dfrac{a^2+a^2-3a^2}{2a^2}=-\\dfrac12\\Rightarrow\\widehat{MPN}=120^\\circ\\).', '\\(\\cos\\widehat{MPN}=\\dfrac{a^2+a^2-3a^2}{2a^2}=-\\dfrac12\\Rightarrow\\widehat{MPN}=120^\\circ\\).'),
   T('The angle between lines is not obtuse: \\((AB,CD)=180^\\circ-120^\\circ\\).', 'Góc giữa hai đường thẳng không tù: \\((AB,CD)=180^\\circ-120^\\circ\\).')],
  T('\\((AB,CD)=60^\\circ\\).', '\\((AB,CD)=60^\\circ\\).'))
examples = EXFIG(examples, 4, GEO3D(fig('tet', pts={'M': 'mid:B,C', 'N': 'mid:A,D', 'P': 'mid:A,C'}, seg=[['P', 'M', {'color': HL}], ['P', 'N', {'color': BL}], ['M', 'N', {'dash': True}]]), alt=('Tetrahedron with the midpoints M, N, P', '')))
assert math.isclose(math.degrees(math.acos(3 / 5)), 53.13, abs_tol=0.01)
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('A cable in a warehouse', 'Sợi cáp trong nhà kho'), T('A warehouse is a box 4 m long, 3 m wide and 5 m high. A cable runs along a diagonal of the floor. Find the angle between the cable and a 3 m beam of the roof frame.', 'Một nhà kho dạng hình hộp chữ nhật dài 4 m, rộng 3 m, cao 5 m. Một sợi cáp chạy theo đường chéo sàn. Tính góc giữa sợi cáp và một thanh dầm dài 3 m của khung mái.'),
  T('The roof beam is parallel to a 3 m edge of the floor at the cable\'s end.', 'Thanh dầm song song với cạnh 3 m của sàn xuất phát từ đầu sợi cáp.'),
  [T('Floor diagonal \\(=\\sqrt{4^2+3^2}=5\\) m; the angle is the angle between the diagonal and the 3 m edge.', 'Đường chéo sàn \\(=\\sqrt{4^2+3^2}=5\\) m; góc cần tìm là góc giữa đường chéo và cạnh 3 m.'), T('\\(\\cos\\varphi=\\dfrac35\\Rightarrow\\varphi\\approx53{,}13^\\circ\\). The height 5 m plays no role.', '\\(\\cos\\varphi=\\dfrac35\\Rightarrow\\varphi\\approx53{,}13^\\circ\\). Chiều cao 5 m không ảnh hưởng.')],
  T('About \\(53{,}13^\\circ\\).', 'Khoảng \\(53{,}13^\\circ\\).'))
examples = EXFIG(examples, 2, GEO3D(fig('cube', seg=[['A′', 'B', {'color': HL}], ['B′', 'C', {'color': BL}], ['D′', 'C', {'color': HL}], ['B′', 'D′']], poly=[FILL(['B′', 'C', 'D′'], '#fde68a', .45)]), alt=('Cube with the equilateral triangle B′CD′', '')))


def lvl(P):
    p, q, d, ee, ev = P['cube']
    o1 = M4(1, 'In the cube \\(ABCD.A\'B\'C\'D\'\\), the angle between \\(%s\\) and \\(%s\\) is…' % (p, q), 'Trong hình lập phương \\(ABCD.A\'B\'C\'D\'\\), góc giữa \\(%s\\) và \\(%s\\) bằng…' % (p, q), '\\(%d^\\circ\\)' % d,
            ['\\(%d^\\circ\\)' % x for x in (0, 45, 60, 90, 30) if x != d][:3], ee + '.', ev + '.')
    a, b, d2, why, ang = P['pyr']
    o2 = M4(2, '\\(S.ABCD\\): square base, all edges equal. The angle between \\(%s\\) and \\(%s\\) is…' % (a, b), 'Hình chóp \\(S.ABCD\\) có đáy hình vuông và tất cả các cạnh bằng nhau. Góc giữa \\(%s\\) và \\(%s\\) bằng…' % (a, b), '\\(%d^\\circ\\)' % d2,
            ['\\(%d^\\circ\\)' % x for x in (45, 30, 60, 90) if x != d2], '\\(%s\\); angle \\(%s\\).' % (why, ang), '\\(%s\\); xét góc \\(%s\\).' % (why, ang))
    x, y, z = P['box']
    o3 = M4(3, 'Box \\(ABCD.A\'B\'C\'D\'\\): \\(AB=%d\\), \\(AD=%d\\). The cosine of the angle between \\(AB\\) and \\(A\'C\'\\) is…' % (x, y), 'Hình hộp chữ nhật \\(ABCD.A\'B\'C\'D\'\\) có \\(AB=%d\\), \\(AD=%d\\). Côsin của góc giữa \\(AB\\) và \\(A\'C\'\\) bằng…' % (x, y), '\\(%s\\)' % fr(F(x, z)),
            ['\\(%s\\)' % fr(F(y, z)), '\\(%s\\)' % fr(F(x, y)), '\\(%s\\)' % fr(F(y, x))], '\\(A\'C\'\\parallel AC=%d\\).' % z, '\\(A\'C\'\\parallel AC\\), \\(AC=%d\\): \\(\\cos\\widehat{BAC}=\\dfrac{%d}{%d}\\).' % (z, x, z))
    (se, sv), val = P['stmt']
    t4 = tf(4, se, sv, val, 'Think of the edges of a cube.', 'Hãy nghĩ đến các cạnh của hình lập phương.')
    (l1, l2), v5 = P['cstmt']
    t5 = tf(5, 'In the cube \\(ABCD.A\'B\'C\'D\'\\): \\(%s\\perp %s\\).' % (l1, l2), 'Trong hình lập phương \\(ABCD.A\'B\'C\'D\'\\): \\(%s\\perp %s\\).' % (l1, l2), v5,
            'Translate one line to meet the other.', 'Dời một đường thẳng để cắt đường kia rồi xét tam giác.')
    k, rad, ans6 = P['tet']; MN = ('%d\\sqrt{%d}' % (k, rad) if rad > 1 else str(k))
    s6 = sh(6, 'Tetrahedron \\(ABCD\\): \\(AB=CD=%d\\), \\(M\\), \\(N\\) midpoints of \\(BC\\), \\(AD\\), \\(MN=%s\\). Find \\((AB,CD)\\) in degrees.' % (2 * k, MN), 'Tứ diện \\(ABCD\\) có \\(AB=CD=%d\\), \\(M\\), \\(N\\) là trung điểm \\(BC\\), \\(AD\\), \\(MN=%s\\). Tính \\((AB,CD)\\) (độ).' % (2 * k, MN), ans6,
            '\\(P\\) midpoint of \\(AC\\): \\(\\cos\\widehat{MPN}=%s\\).' % fr(F(2 - rad, 2)), '\\(P\\) là trung điểm \\(AC\\): \\(PM=PN=%d\\), \\(\\cos\\widehat{MPN}=%s\\).' % (k, fr(F(2 - rad, 2))))
    ab, ad, ans7 = P['box2']
    s7 = sh(7, 'Box \\(ABCD.A\'B\'C\'D\'\\) with \\(AB=%s\\), \\(AD=%s\\). Find the angle (degrees) between \\(AB\\) and \\(A\'C\'\\).' % (ab, ad), 'Hình hộp chữ nhật \\(ABCD.A\'B\'C\'D\'\\) có \\(AB=%s\\), \\(AD=%s\\). Tính góc (độ) giữa \\(AB\\) và \\(A\'C\'\\).' % (ab, ad), ans7,
            '\\(\\tan\\widehat{BAC}=\\dfrac{BC}{AB}\\).', '\\(A\'C\'\\parallel AC\\), \\(\\tan\\widehat{BAC}=\\dfrac{BC}{AB}=\\dfrac{%s}{%s}\\).' % (ad, ab))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]


ST = [(('In space, two lines perpendicular to a third line are parallel.', 'Trong không gian, hai đường thẳng cùng vuông góc với một đường thẳng thứ ba thì song song với nhau.'), False),
      (('If \\(a\\parallel b\\) and \\(c\\perp a\\), then \\(c\\perp b\\).', 'Nếu \\(a\\parallel b\\) và \\(c\\perp a\\) thì \\(c\\perp b\\).'), True),
      (('Two perpendicular lines in space always intersect.', 'Hai đường thẳng vuông góc trong không gian luôn cắt nhau.'), False)]
PP = [dict(cube=S.CUBE_ANG[1], pyr=S.PYR_ANG[0], box=(3, 4, 5), stmt=ST[0], cstmt=(('AC', "B'D'"), True), tet=(3, 2, 90), box2=('4', '4\\sqrt3', 60)),
      dict(cube=S.CUBE_ANG[3], pyr=S.PYR_ANG[4], box=(5, 12, 13), stmt=ST[1], cstmt=(("A'B", "AD'"), False), tet=(2, 3, 60), box2=('5', '5', 45)),
      dict(cube=S.CUBE_ANG[2], pyr=S.PYR_ANG[1], box=(8, 6, 10), stmt=ST[2], cstmt=(('BD', "A'C'"), True), tet=(5, 1, 60), box2=('6', '2\\sqrt3', 30))]
practice = three(lvl, PP)
practice = with_self(practice, S.M22S11, start=8)
mistakes = [('<b>Taking an obtuse angle as the angle between two lines.</b> If the triangle gives \\(120^\\circ\\), the answer is \\(60^\\circ\\).', '<b>Lấy góc tù làm góc giữa hai đường thẳng.</b> Nếu tam giác cho góc \\(120^\\circ\\) thì đáp số là \\(60^\\circ\\).'),
            ('<b>Thinking perpendicular lines must meet.</b> \\(AB\\) and \\(B\'C\'\\) in a cube are skew and perpendicular.', '<b>Nghĩ rằng hai đường vuông góc phải cắt nhau.</b> \\(AB\\) và \\(B\'C\'\\) trong hình lập phương chéo nhau mà vẫn vuông góc.'),
            ('<b>Carrying plane rules into space.</b> Two lines perpendicular to a third are not necessarily parallel.', '<b>Áp dụng máy móc quy tắc hình phẳng.</b> Hai đường cùng vuông góc với đường thứ ba chưa chắc song song.'),
            ('<b>Reading an angle from the picture.</b> A drawn right angle may not look right (and conversely): always justify by parallels and triangles.', '<b>Đoán góc theo hình vẽ.</b> Hình vẽ phối cảnh làm méo góc: luôn lập luận bằng đường song song và tam giác.')]
summary = [('\\((a,b)\\): through a point \\(O\\) draw \\(a\'\\parallel a\\), \\(b\'\\parallel b\\); \\(0^\\circ\\le(a,b)\\le90^\\circ\\).', '\\((a,b)\\): qua điểm \\(O\\) kẻ \\(a\'\\parallel a\\), \\(b\'\\parallel b\\); \\(0^\\circ\\le(a,b)\\le90^\\circ\\).'),
           ('\\(a\\perp b\\iff(a,b)=90^\\circ\\) (the lines may be skew); \\(a\\parallel b,\\ c\\perp a\\Rightarrow c\\perp b\\).', '\\(a\\perp b\\iff(a,b)=90^\\circ\\) (có thể chéo nhau); \\(a\\parallel b,\\ c\\perp a\\Rightarrow c\\perp b\\).'),
           ('Method: translate, build a triangle, use the law of cosines; take \\(180^\\circ-\\alpha\\) if obtuse.', 'Phương pháp: dời song song, lập tam giác, dùng định lí côsin; lấy \\(180^\\circ-\\alpha\\) nếu góc tù.'),
           ('Key words: angle between lines, perpendicular, skew, translate.', 'Từ cần nhớ: angle between lines, perpendicular, skew, translate.')]
checks = [('I can define the angle between two lines in space.', 'Em nêu được định nghĩa góc giữa hai đường thẳng trong không gian.'), ('I can compute it by translating a line.', 'Em tính được góc bằng cách dời song song.'),
          ('I can prove two lines are perpendicular.', 'Em chứng minh được hai đường thẳng vuông góc.'), ('I know perpendicular lines may be skew.', 'Em biết hai đường vuông góc có thể chéo nhau.')]
LL('g11-perp-01', 'Perpendicular Lines', CV, ('Perpendicularity in Space', 'Quan hệ vuông góc trong không gian'), 'perpendicularity-in-space', 'perpendicular-lines', 230, 'Intermediate', 70, ('lines and planes in space, parallel lines', 'đường thẳng và mặt phẳng trong không gian, hai đường thẳng song song'),
   'The angle between two lines in space; perpendicular lines (intersecting or skew).', 'Bài 22 – Góc giữa hai đường thẳng trong không gian; hai đường thẳng vuông góc (cắt nhau hoặc chéo nhau).',
   ['angle between lines', 'perpendicular', 'skew'], ['góc giữa hai đường thẳng', 'vuông góc', 'chéo nhau'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g11-space-05'])
