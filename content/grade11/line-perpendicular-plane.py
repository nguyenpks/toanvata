# -*- coding: utf-8 -*-
"""g11-perp-02 = Toán 11 KNTT, Bài 23: Đường thẳng vuông góc với mặt phẳng. Mã ngân hàng câu hỏi: TOAN11-C7-B23."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
from mb_solids import fig, FILL, HL, BL, GR
import sp_g11h as S

CV = 'Đường thẳng vuông góc với mặt phẳng'
vocab = defs(CV, [
 ('lperpp', 'line perpendicular to a plane', 'đường thẳng vuông góc với mặt phẳng', 'a line perpendicular to every line of the plane.', 'đường thẳng vuông góc với mọi đường thẳng nằm trong mặt phẳng.', 'SA is perpendicular to the plane (ABCD).', '\\(d\\perp(P)\\)'),
 ('perpbis', 'perpendicular bisector plane', 'mặt phẳng trung trực', 'the plane through the midpoint of a segment and perpendicular to it; the set of points equidistant from its endpoints.', 'mặt phẳng đi qua trung điểm của đoạn thẳng và vuông góc với đoạn thẳng đó; là tập hợp các điểm cách đều hai đầu mút.', 'M lies on the perpendicular bisector plane of AB.', ''),
 ('critp', 'criterion for perpendicularity', 'điều kiện vuông góc', 'a line perpendicular to two intersecting lines of a plane is perpendicular to the plane.', 'đường thẳng vuông góc với hai đường thẳng cắt nhau nằm trong mặt phẳng thì vuông góc với mặt phẳng đó.', 'Use the criterion with AB and AD.', '')])
goals = [('define a [[đường thẳng vuông góc với mặt phẳng|đường thẳng vuông góc với mặt phẳng]] and state the criterion;', 'nêu được định nghĩa [[đường thẳng vuông góc với mặt phẳng]] và [[điều kiện vuông góc]];'),
         ('prove that a line is perpendicular to a plane, and deduce perpendicular lines;', 'chứng minh đường thẳng vuông góc với mặt phẳng, từ đó suy ra hai đường thẳng vuông góc;'),
         ('use the links between parallelism and perpendicularity, and the [[mặt phẳng trung trực]];', 'vận dụng mối liên hệ giữa quan hệ song song và quan hệ vuông góc, [[mặt phẳng trung trực]];'),
         ('check verticality in real life (poles, walls, columns).', 'kiểm tra tính thẳng đứng trong thực tế (cột, tường, trụ).')]
goals = [(e.replace('[[đường thẳng vuông góc với mặt phẳng|đường thẳng vuông góc với mặt phẳng]]', 'line perpendicular to a plane').replace('[[mặt phẳng trung trực]]', 'perpendicular bisector plane'), v) for e, v in goals]
phrases = [('<b>The line is perpendicular to two intersecting lines of the plane.</b>', 'Đường thẳng vuông góc với hai đường thẳng cắt nhau nằm trong mặt phẳng.'), ('<b>Therefore it is perpendicular to the plane.</b>', 'Do đó nó vuông góc với mặt phẳng.'),
           ('<b>A line perpendicular to a plane is perpendicular to every line in it.</b>', 'Đường thẳng vuông góc với mặt phẳng thì vuông góc với mọi đường thẳng nằm trong mặt phẳng đó.'), ('<b>The two lines are both perpendicular to the base, so they are parallel.</b>', 'Hai đường thẳng cùng vuông góc với đáy nên song song.'), ('<b>The pole stands vertically.</b>', 'Cái cột đứng thẳng.')]
review = T('From Bài 22: \\(a\\perp b\\iff(a,b)=90^\\circ\\), and \\(a\\parallel b,\\ c\\perp a\\Rightarrow c\\perp b\\). Grade 9: in a square the diagonals are perpendicular; in an isosceles triangle the median is also an altitude.',
           'Từ Bài 22: \\(a\\perp b\\iff(a,b)=90^\\circ\\), và \\(a\\parallel b,\\ c\\perp a\\Rightarrow c\\perp b\\). Lớp 9: hai đường chéo hình vuông vuông góc; trong tam giác cân, đường trung tuyến cũng là đường cao.')
theory = '<h3>23.1 %s</h3>' % TI('Definition and criterion', 'Định nghĩa và điều kiện')
theory += BOX('blue', ('Definition', 'Định nghĩa'), T('\\(d\\perp(P)\\) when \\(d\\) is perpendicular to every line lying in \\((P)\\). Then \\(d\\) meets \\((P)\\) at exactly one point.', '\\(d\\perp(P)\\) khi \\(d\\) vuông góc với mọi đường thẳng nằm trong \\((P)\\). Khi đó \\(d\\) cắt \\((P)\\) tại đúng một điểm.'))
theory += BOX('mint', ('Criterion', 'Điều kiện'), T('If \\(d\\perp a\\), \\(d\\perp b\\), with \\(a\\), \\(b\\subset(P)\\) <b>intersecting</b>, then \\(d\\perp(P)\\). Two parallel lines are not enough.', 'Nếu \\(d\\perp a\\), \\(d\\perp b\\) với \\(a\\), \\(b\\) nằm trong \\((P)\\) và <b>cắt nhau</b> thì \\(d\\perp(P)\\). Hai đường song song thì chưa đủ.'))
theory += GEO3D(fig('pyrsq', hl={('S', 'A'): HL, ('A', 'B'): BL, ('A', 'D'): BL}, right=[['S', 'A', 'B'], ['S', 'A', 'D']]),
  cap=('\\(SA\\perp AB\\) and \\(SA\\perp AD\\), and \\(AB\\), \\(AD\\) meet at \\(A\\): so \\(SA\\perp(ABCD)\\), hence \\(SA\\perp AC\\), \\(SA\\perp BD\\), …', '\\(SA\\perp AB\\), \\(SA\\perp AD\\), và \\(AB\\), \\(AD\\) cắt nhau tại \\(A\\): nên \\(SA\\perp(ABCD)\\), suy ra \\(SA\\perp AC\\), \\(SA\\perp BD\\), …'),
  alt=('Pyramid with SA perpendicular to two edges of the base', ''), height=360)
theory += '<h3>23.2 %s</h3>' % TI('Properties', 'Tính chất')
theory += BOX('blue', ('Existence and uniqueness', 'Sự tồn tại và duy nhất'), UL([T('Through a point there is exactly one plane perpendicular to a given line, and exactly one line perpendicular to a given plane.', 'Qua một điểm có duy nhất một mặt phẳng vuông góc với một đường thẳng cho trước, và duy nhất một đường thẳng vuông góc với một mặt phẳng cho trước.'),
  T('The perpendicular bisector plane of \\(AB\\) passes through its midpoint and is perpendicular to \\(AB\\); it is the set of points \\(M\\) with \\(MA=MB\\).', 'Mặt phẳng trung trực của \\(AB\\) đi qua trung điểm và vuông góc với \\(AB\\); đó là tập hợp các điểm \\(M\\) có \\(MA=MB\\).')]))
theory += BOX('blue', ('Parallel and perpendicular', 'Liên hệ song song – vuông góc'), UL([T('\\(a\\parallel b\\), \\((P)\\perp a\\Rightarrow(P)\\perp b\\); two distinct lines perpendicular to one plane are parallel.', '\\(a\\parallel b\\), \\((P)\\perp a\\Rightarrow(P)\\perp b\\); hai đường thẳng phân biệt cùng vuông góc với một mặt phẳng thì song song.'),
  T('\\((P)\\parallel(Q)\\), \\(a\\perp(P)\\Rightarrow a\\perp(Q)\\); two distinct planes perpendicular to one line are parallel.', '\\((P)\\parallel(Q)\\), \\(a\\perp(P)\\Rightarrow a\\perp(Q)\\); hai mặt phẳng phân biệt cùng vuông góc với một đường thẳng thì song song.'),
  T('\\(a\\parallel(P)\\), \\(b\\perp(P)\\Rightarrow b\\perp a\\).', '\\(a\\parallel(P)\\), \\(b\\perp(P)\\Rightarrow b\\perp a\\).')]))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('To prove \\(a\\perp b\\) in space, a common strategy is: find a plane containing \\(b\\) that is perpendicular to \\(a\\).', 'Để chứng minh \\(a\\perp b\\) trong không gian, cách thường dùng: tìm một mặt phẳng chứa \\(b\\) và vuông góc với \\(a\\).'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Using the criterion', 'Dùng điều kiện vuông góc'), T('\\(S.ABCD\\) has a square base and \\(SA\\perp(ABCD)\\). Prove \\(BC\\perp(SAB)\\) and \\(CD\\perp(SAD)\\).', 'Hình chóp \\(S.ABCD\\) có đáy là hình vuông, \\(SA\\perp(ABCD)\\). Chứng minh \\(BC\\perp(SAB)\\) và \\(CD\\perp(SAD)\\).'),
  T('Find two intersecting lines of \\((SAB)\\) perpendicular to \\(BC\\).', 'Tìm hai đường thẳng cắt nhau trong \\((SAB)\\) cùng vuông góc với \\(BC\\).'),
  [T('\\(BC\\perp AB\\) (square) and \\(BC\\perp SA\\) (\\(SA\\perp(ABCD)\\)); \\(AB\\), \\(SA\\) meet at \\(A\\): \\(BC\\perp(SAB)\\).', '\\(BC\\perp AB\\) (hình vuông) và \\(BC\\perp SA\\) (vì \\(SA\\perp(ABCD)\\)); \\(AB\\), \\(SA\\) cắt nhau tại \\(A\\): \\(BC\\perp(SAB)\\).'),
   T('Similarly \\(CD\\perp AD\\), \\(CD\\perp SA\\): \\(CD\\perp(SAD)\\). Consequence: \\(BC\\perp SB\\), \\(CD\\perp SD\\) – all four lateral faces are right triangles.', 'Tương tự \\(CD\\perp AD\\), \\(CD\\perp SA\\): \\(CD\\perp(SAD)\\). Hệ quả: \\(BC\\perp SB\\), \\(CD\\perp SD\\) – bốn mặt bên đều là tam giác vuông.')],
  T('Proved; the lateral faces are right triangles at \\(A\\), \\(A\\), \\(B\\), \\(D\\).', 'Đã chứng minh; các mặt bên vuông lần lượt tại \\(A\\), \\(A\\), \\(B\\), \\(D\\).'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Three perpendicular edges', 'Ba cạnh đôi một vuông góc'), T('\\(OA\\), \\(OB\\), \\(OC\\) are pairwise perpendicular and \\(OA=OB=OC=a\\). Prove \\(OA\\perp(OBC)\\) and find the sides of triangle \\(ABC\\).', 'Cho \\(OA\\), \\(OB\\), \\(OC\\) đôi một vuông góc và \\(OA=OB=OC=a\\). Chứng minh \\(OA\\perp(OBC)\\) và tính các cạnh của tam giác \\(ABC\\).'),
  T('\\(OB\\), \\(OC\\) meet at \\(O\\).', '\\(OB\\), \\(OC\\) cắt nhau tại \\(O\\).'),
  [T('\\(OA\\perp OB\\), \\(OA\\perp OC\\): \\(OA\\perp(OBC)\\).', '\\(OA\\perp OB\\), \\(OA\\perp OC\\): \\(OA\\perp(OBC)\\).'), T('Each of \\(AB\\), \\(BC\\), \\(CA\\) is the hypotenuse of an isosceles right triangle with legs \\(a\\): equal to \\(a\\sqrt2\\).', 'Mỗi cạnh \\(AB\\), \\(BC\\), \\(CA\\) là cạnh huyền của tam giác vuông cân có cạnh góc vuông \\(a\\): bằng \\(a\\sqrt2\\).')],
  T('\\(ABC\\) is equilateral with side \\(a\\sqrt2\\).', 'Tam giác \\(ABC\\) đều cạnh \\(a\\sqrt2\\).'))
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('A diagonal perpendicular to an edge', 'Đường chéo vuông góc với cạnh bên'), T('\\(S.ABCD\\): square base with centre \\(O\\), \\(SA\\perp(ABCD)\\). Prove \\(BD\\perp(SAC)\\) and \\(BD\\perp SC\\).', 'Hình chóp \\(S.ABCD\\) có đáy là hình vuông tâm \\(O\\), \\(SA\\perp(ABCD)\\). Chứng minh \\(BD\\perp(SAC)\\) và \\(BD\\perp SC\\).'),
  T('Strategy: a plane containing \\(SC\\) and perpendicular to \\(BD\\).', 'Chiến lược: tìm mặt phẳng chứa \\(SC\\) và vuông góc với \\(BD\\).'),
  [T('\\(BD\\perp AC\\) (diagonals of a square), \\(BD\\perp SA\\); \\(AC\\cap SA=A\\): \\(BD\\perp(SAC)\\).', '\\(BD\\perp AC\\) (hai đường chéo hình vuông), \\(BD\\perp SA\\); \\(AC\\cap SA=A\\): \\(BD\\perp(SAC)\\).'), T('\\(SC\\subset(SAC)\\Rightarrow BD\\perp SC\\).', '\\(SC\\subset(SAC)\\Rightarrow BD\\perp SC\\).')],
  T('\\(BD\\perp(SAC)\\), so \\(BD\\perp SC\\) (they are skew!).', '\\(BD\\perp(SAC)\\) nên \\(BD\\perp SC\\) (hai đường này chéo nhau!).'))
examples = EXFIG(examples, 3, GEO3D(fig('pyrsq', pts={'O': 'mid:A,C'}, seg=[['A', 'C'], ['B', 'D', {'color': HL}], ['S', 'C', {'color': BL}]], poly=[FILL('SAC', '#fde68a', .45)]), alt=('Plane SAC and the diagonal BD', '')))
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Opposite edges of a tetrahedron', 'Hai cạnh đối của tứ diện'), T('Tetrahedron \\(ABCD\\) has \\(AB=AC\\) and \\(DB=DC\\). Prove \\(BC\\perp AD\\).', 'Tứ diện \\(ABCD\\) có \\(AB=AC\\) và \\(DB=DC\\). Chứng minh \\(BC\\perp AD\\).'),
  T('Let \\(M\\) be the midpoint of \\(BC\\).', 'Gọi \\(M\\) là trung điểm của \\(BC\\).'),
  [T('Triangles \\(ABC\\), \\(DBC\\) are isosceles: \\(AM\\perp BC\\), \\(DM\\perp BC\\).', 'Tam giác \\(ABC\\), \\(DBC\\) cân: \\(AM\\perp BC\\), \\(DM\\perp BC\\).'), T('\\(AM\\), \\(DM\\) meet at \\(M\\): \\(BC\\perp(ADM)\\supset AD\\). (\\((ADM)\\) is the perpendicular bisector plane of \\(BC\\).)', '\\(AM\\), \\(DM\\) cắt nhau tại \\(M\\): \\(BC\\perp(ADM)\\supset AD\\). (\\((ADM)\\) chính là mặt phẳng trung trực của \\(BC\\).)')],
  T('\\(BC\\perp AD\\).', '\\(BC\\perp AD\\).'))
examples = EXFIG(examples, 4, GEO3D(fig('tet', pts={'M': 'mid:B,C'}, seg=[['A', 'M', {'color': BL}], ['D', 'M', {'color': BL}], ['B', 'C', {'color': HL}]], poly=[FILL('ADM', '#86e0bd', .4)]), alt=('Tetrahedron with the plane ADM', '')))
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Is the pole vertical?', 'Cột có thẳng đứng không?'), T('A worker sets up a 6 m flagpole on flat ground. a) Why must she check the right angle with the ground in two different directions? b) A guy rope goes from the top to a peg 8 m from the foot. How long is it?', 'Một công nhân dựng cột cờ cao 6 m trên mặt đất phẳng. a) Vì sao phải kiểm tra góc vuông với mặt đất theo hai hướng khác nhau? b) Một sợi dây néo nối đỉnh cột với cọc cách chân cột 8 m. Sợi dây dài bao nhiêu?'),
  T('Criterion: two intersecting lines of the ground.', 'Điều kiện: hai đường thẳng cắt nhau của mặt đất.'),
  [T('a) One right angle only shows the pole lies in a plane perpendicular to one ground line – it may still lean sideways. Right angles with two intersecting ground lines give pole \\(\\perp\\) ground.', 'a) Một góc vuông chỉ cho biết cột vuông góc với một đường thẳng của mặt đất – cột vẫn có thể nghiêng sang bên. Vuông góc với hai đường cắt nhau của mặt đất thì cột vuông góc với mặt đất.'),
   T('b) The pole is then perpendicular to the line from its foot to the peg: rope \\(=\\sqrt{6^2+8^2}=10\\) m.', 'b) Khi đó cột vuông góc với đường nối chân cột với cọc: dây dài \\(\\sqrt{6^2+8^2}=10\\) m.')],
  T('a) To use the criterion; b) 10 m.', 'a) Để dùng điều kiện vuông góc; b) 10 m.'))


def lvl(P):
    pl, ok, bad = P['sq']
    o1 = M4(1, '\\(S.ABCD\\): square base, \\(SA\\perp(ABCD)\\). Which line is perpendicular to \\(%s\\)?' % pl, 'Hình chóp \\(S.ABCD\\) có đáy hình vuông, \\(SA\\perp(ABCD)\\). Đường thẳng nào vuông góc với mặt phẳng \\(%s\\)?' % pl, '\\(%s\\)' % ok, ['\\(%s\\)' % b for b in bad],
            '\\(%s\\perp SA\\) and a second line of \\(%s\\).' % (ok, pl), '\\(%s\\) vuông góc với \\(SA\\) và với một đường thẳng khác của \\(%s\\) cắt \\(SA\\).' % (ok, pl))
    v, line, okp, badp = P['tri']
    o2 = M4(2, '\\(S.ABC\\): \\(SA\\perp(ABC)\\), triangle \\(ABC\\) right-angled at \\(%s\\). Then \\(%s\\) is perpendicular to…' % (v, line), 'Hình chóp \\(S.ABC\\) có \\(SA\\perp(ABC)\\), tam giác \\(ABC\\) vuông tại \\(%s\\). Khi đó \\(%s\\) vuông góc với mặt phẳng…' % (v, line), '\\(%s\\)' % okp, ['\\(%s\\)' % b for b in badp],
            '\\(%s\\perp SA\\) and \\(%s\\) is perpendicular to the other leg.' % (line, line), '\\(%s\\perp SA\\) và \\(%s\\) vuông góc với cạnh góc vuông còn lại.' % (line, line))
    h, a, d = P['sc']
    o3 = M4(3, '\\(S.ABCD\\): square base of side %d, \\(SA\\perp(ABCD)\\), \\(SA=%d\\). Then \\(SC=\\)…' % (a, h), 'Hình chóp \\(S.ABCD\\) có đáy là hình vuông cạnh %d, \\(SA\\perp(ABCD)\\), \\(SA=%d\\). Độ dài \\(SC\\) bằng…' % (a, h), '\\(%d\\)' % d,
            ['\\(%s\\)' % w for w in [S.rt(h * h + a * a), str(h + a), S.rt(2 * a * a), S.rt(h * h + 4 * a * a)] if w != str(d)][:3], '\\(SA\\perp AC\\), \\(AC=%d\\sqrt2\\).' % a, '\\(SA\\perp AC\\), \\(AC=%d\\sqrt2\\): \\(SC=\\sqrt{%d+%d}=%d\\).' % (a, h * h, 2 * a * a, d))
    (se, sv), val = P['stmt']
    t4 = tf(4, se, sv, val, 'Recall the criterion and the properties.', 'Nhớ lại điều kiện vuông góc và các tính chất.')
    (l1, l2), v5, why = P['st5']
    t5 = tf(5, '\\(S.ABCD\\): square base, \\(SA\\perp(ABCD)\\). Then \\(%s\\perp %s\\).' % (l1, l2), 'Hình chóp \\(S.ABCD\\) có đáy hình vuông, \\(SA\\perp(ABCD)\\). Khi đó \\(%s\\perp %s\\).' % (l1, l2), v5, why[0], why[1])
    x, y, z, w = P['diag']
    s6 = sh(6, 'Box \\(ABCD.A\'B\'C\'D\'\\): \\(AB=%d\\), \\(AD=%d\\), \\(AA\'=%d\\). Find \\(A\'C\\).' % (x, y, z), 'Hình hộp chữ nhật \\(ABCD.A\'B\'C\'D\'\\) có \\(AB=%d\\), \\(AD=%d\\), \\(AA\'=%d\\). Tính \\(A\'C\\).' % (x, y, z), w,
            '\\(AA\'\\perp AC\\).', '\\(AA\'\\perp(ABCD)\\) nên \\(AA\'\\perp AC\\): \\(A\'C=\\sqrt{%d+%d+%d}=%d\\).' % (x * x, y * y, z * z, w))
    p, q, c = P['pole']
    s7 = sh(7, 'A %d m pole stands perpendicular to flat ground. A rope joins its top to a peg %d m from its foot. Find the length of the rope (m).' % (p, q), 'Một cột cao %d m dựng vuông góc với mặt đất phẳng. Sợi dây nối đỉnh cột với cọc cách chân cột %d m. Tính chiều dài sợi dây (m).' % (p, q), c,
            'The pole is perpendicular to the ground line through its foot.', 'Cột vuông góc với đường thẳng qua chân cột nằm trên mặt đất: \\(\\sqrt{%d+%d}=%d\\).' % (p * p, q * q, c))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]


STM = [(('A line perpendicular to two lines of a plane is perpendicular to the plane.', 'Đường thẳng vuông góc với hai đường thẳng nằm trong một mặt phẳng thì vuông góc với mặt phẳng đó.'), False),
       (('Two distinct lines perpendicular to the same plane are parallel.', 'Hai đường thẳng phân biệt cùng vuông góc với một mặt phẳng thì song song với nhau.'), True),
       (('Through a point there are infinitely many planes perpendicular to a given line.', 'Qua một điểm có vô số mặt phẳng vuông góc với một đường thẳng cho trước.'), False)]
PP = [dict(sq=S.SQ_PERP[0], tri=S.TRI[0], sc=(2, 4, 6), stmt=STM[0], st5=(('BD', 'SC'), True, ('\\(BD\\perp(SAC)\\).', '\\(BD\\perp(SAC)\\supset SC\\).')), diag=(2, 3, 6, 7), pole=(6, 8, 10)),
      dict(sq=S.SQ_PERP[2], tri=S.TRI[1], sc=(7, 6, 11), stmt=STM[1], st5=(('BC', 'SD'), False, ('\\(BC\\parallel AD\\) and \\((SD,AD)=\\widehat{SDA}\\ne90^\\circ\\).', '\\(BC\\parallel AD\\) nên \\((BC,SD)=\\widehat{SDA}\\ne90^\\circ\\) (tam giác \\(SAD\\) vuông tại \\(A\\)).')), diag=(1, 4, 8, 9), pole=(5, 12, 13)),
      dict(sq=S.SQ_PERP[4], tri=S.TRI[2], sc=(3, 6, 9), stmt=STM[2], st5=(('CD', 'SD'), True, ('\\(CD\\perp(SAD)\\).', '\\(CD\\perp AD\\), \\(CD\\perp SA\\) nên \\(CD\\perp(SAD)\\supset SD\\).')), diag=(4, 4, 7, 9), pole=(9, 12, 15))]
practice = three(lvl, PP)
practice = with_self(practice, S.M23S11, start=8)
mistakes = [('<b>Using two parallel lines in the criterion.</b> The two lines of the plane must <i>intersect</i>.', '<b>Dùng hai đường song song trong điều kiện vuông góc.</b> Hai đường thẳng trong mặt phẳng phải <i>cắt nhau</i>.'),
            ('<b>Proving \\(d\\perp(P)\\) from \\(d\\perp\\) one line only.</b> One right angle is never enough.', '<b>Kết luận \\(d\\perp(P)\\) khi \\(d\\) chỉ vuông góc với một đường.</b> Một góc vuông không bao giờ đủ.'),
            ('<b>Forgetting the consequence.</b> Once \\(d\\perp(P)\\), \\(d\\) is perpendicular to <i>every</i> line of \\((P)\\) – use it to get new right angles.', '<b>Quên hệ quả.</b> Khi \\(d\\perp(P)\\), \\(d\\) vuông góc với <i>mọi</i> đường thẳng của \\((P)\\) – dùng để có thêm góc vuông.'),
            ('<b>Assuming \\(SB\\perp BC\\) only from the picture.</b> Prove \\(BC\\perp(SAB)\\) first.', '<b>Thấy \\(SB\\perp BC\\) qua hình vẽ.</b> Phải chứng minh \\(BC\\perp(SAB)\\) trước.')]
summary = [('\\(d\\perp(P)\\iff d\\) is perpendicular to every line of \\((P)\\).', '\\(d\\perp(P)\\iff d\\) vuông góc với mọi đường thẳng của \\((P)\\).'),
           ('Criterion: \\(d\\perp a\\), \\(d\\perp b\\), \\(a\\), \\(b\\subset(P)\\) intersecting \\(\\Rightarrow d\\perp(P)\\).', 'Điều kiện: \\(d\\perp a\\), \\(d\\perp b\\), \\(a\\), \\(b\\subset(P)\\) cắt nhau \\(\\Rightarrow d\\perp(P)\\).'),
           ('Links: parallel lines/planes keep perpendicularity; two lines \\(\\perp\\) one plane are parallel.', 'Liên hệ: song song bảo toàn quan hệ vuông góc; hai đường cùng vuông góc với một mặt phẳng thì song song.'),
           ('Key words: perpendicular to a plane, criterion, perpendicular bisector plane.', 'Từ cần nhớ: perpendicular to a plane, criterion, perpendicular bisector plane.')]
checks = [('I can state the definition and the criterion.', 'Em nêu được định nghĩa và điều kiện vuông góc.'), ('I can prove a line is perpendicular to a plane.', 'Em chứng minh được đường thẳng vuông góc với mặt phẳng.'),
          ('I can deduce perpendicular lines from it.', 'Em suy ra được hai đường thẳng vuông góc.'), ('I can explain how to check that a pole is vertical.', 'Em giải thích được cách kiểm tra cột thẳng đứng.')]
LL('g11-perp-02', 'A Line Perpendicular to a Plane', CV, ('Perpendicularity in Space', 'Quan hệ vuông góc trong không gian'), 'perpendicularity-in-space', 'line-perpendicular-plane', 240, 'Intermediate', 75, ('perpendicular lines', 'hai đường thẳng vuông góc'),
   'Definition and criterion; existence and uniqueness; perpendicular bisector plane; links between parallelism and perpendicularity.', 'Bài 23 – Định nghĩa, điều kiện đường thẳng vuông góc với mặt phẳng; tính chất; mặt phẳng trung trực; liên hệ song song – vuông góc.',
   ['perpendicular to a plane', 'criterion', 'perpendicular bisector plane'], ['vuông góc với mặt phẳng', 'điều kiện vuông góc', 'mặt phẳng trung trực'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g11-perp-01'])
