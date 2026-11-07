# -*- coding: utf-8 -*-
"""g11-perp-05 = Toán 11 KNTT, Bài 26: Khoảng cách. Mã ngân hàng câu hỏi: TOAN11-C7-B26."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
from mb_solids import fig, FILL, HL, BL, GR
import sp_g11i as S
from sp_g10h import rt

CV = 'Khoảng cách trong không gian'
vocab = defs(CV, [
 ('dptp', 'distance from a point to a plane', 'khoảng cách từ một điểm đến một mặt phẳng', 'the length \\(MH\\), where \\(H\\) is the projection of \\(M\\) on the plane.', 'độ dài \\(MH\\), với \\(H\\) là hình chiếu vuông góc của \\(M\\) trên mặt phẳng.', 'The distance from A to (SBC) is AH.', '\\(d(M,(P))\\)'),
 ('commperp', 'common perpendicular', 'đường vuông góc chung', 'the line meeting two skew lines and perpendicular to both.', 'đường thẳng cắt cả hai đường thẳng chéo nhau và vuông góc với cả hai.', 'AO is the common perpendicular of AA′ and BD.', ''),
 ('dskew', 'distance between two skew lines', 'khoảng cách giữa hai đường thẳng chéo nhau', 'the length of the common perpendicular segment.', 'độ dài đoạn vuông góc chung của hai đường thẳng đó.', 'The distance between AB and CC′ is BC.', '')])
goals = [('define and compute the distance from a point to a line and to a plane;', 'nêu định nghĩa và tính khoảng cách từ một điểm đến một đường thẳng, [[khoảng cách từ một điểm đến một mặt phẳng]];'),
         ('compute distances between a line and a parallel plane, and between parallel planes;', 'tính khoảng cách giữa đường thẳng và mặt phẳng song song, giữa hai mặt phẳng song song;'),
         ('find the common perpendicular and the distance between two skew lines in simple cases;', 'xác định [[đường vuông góc chung]] và tính [[khoảng cách giữa hai đường thẳng chéo nhau]] trong trường hợp đơn giản;'),
         ('apply distances to rooms, roofs and supports.', 'vận dụng khoảng cách trong phòng ở, mái che, giá đỡ.')]
phrases = [('<b>Draw \\(AH\\) perpendicular to \\(SB\\).</b>', 'Kẻ \\(AH\\) vuông góc với \\(SB\\).'), ('<b>\\(AH\\) is perpendicular to the plane \\(SBC\\).</b>', '\\(AH\\) vuông góc với mặt phẳng \\((SBC)\\).'),
           ('<b>The distance equals the length of the common perpendicular.</b>', 'Khoảng cách bằng độ dài đoạn vuông góc chung.'), ('<b>One over the square of the height equals the sum of the reciprocals of the squares.</b>', 'Nghịch đảo bình phương đường cao bằng tổng nghịch đảo bình phương hai cạnh góc vuông.'), ('<b>The two planes are parallel, so take any point.</b>', 'Hai mặt phẳng song song nên lấy một điểm bất kì.')]
review = T('From Bài 23–25: perpendicular line and plane, perpendicular planes. Right triangle with altitude \\(AH\\): \\(AH=\\dfrac{AB\\cdot AC}{BC}\\), \\(\\dfrac1{AH^2}=\\dfrac1{AB^2}+\\dfrac1{AC^2}\\).', 'Từ Bài 23–25: đường thẳng vuông góc với mặt phẳng, hai mặt phẳng vuông góc. Tam giác vuông có đường cao \\(AH\\): \\(AH=\\dfrac{AB\\cdot AC}{BC}\\), \\(\\dfrac1{AH^2}=\\dfrac1{AB^2}+\\dfrac1{AC^2}\\).')
theory = '<h3>26.1 %s</h3>' % TI('Distance from a point to a line or a plane', 'Khoảng cách từ một điểm đến đường thẳng, mặt phẳng')
theory += BOX('blue', ('Definitions', 'Định nghĩa'), UL([T('\\(d(M,a)=MH\\), \\(H\\) the foot of the perpendicular from \\(M\\) to \\(a\\); \\(d(M,(P))=MH\\), \\(H\\) the projection of \\(M\\) on \\((P)\\). It is the shortest distance from \\(M\\) to points of \\(a\\) (of \\((P)\\)).', '\\(d(M,a)=MH\\), \\(H\\) là chân đường vuông góc kẻ từ \\(M\\) đến \\(a\\); \\(d(M,(P))=MH\\), \\(H\\) là hình chiếu của \\(M\\) trên \\((P)\\). Đó là khoảng cách ngắn nhất từ \\(M\\) đến các điểm của \\(a\\) (của \\((P)\\)).'),
  T('Typical construction: if \\(SA\\perp(ABCD)\\), to get \\(d(A,(SBC))\\) draw \\(AH\\perp SB\\); since \\(BC\\perp(SAB)\\), \\(AH\\perp BC\\), so \\(AH\\perp(SBC)\\) and \\(\\dfrac1{AH^2}=\\dfrac1{SA^2}+\\dfrac1{AB^2}\\).', 'Cách dựng thường gặp: nếu \\(SA\\perp(ABCD)\\), để tính \\(d(A,(SBC))\\) kẻ \\(AH\\perp SB\\); vì \\(BC\\perp(SAB)\\) nên \\(AH\\perp BC\\), do đó \\(AH\\perp(SBC)\\) và \\(\\dfrac1{AH^2}=\\dfrac1{SA^2}+\\dfrac1{AB^2}\\).')]))
t_h = F(1296, 1296 + 1600)
theory += GEO3D(fig('pyrsq', pts={'H': 'on:S,B,%s' % t_h}, seg=[['A', 'H', {'color': HL}]], hl={('B', 'C'): GR}, right=[['A', 'H', 'S'], ['S', 'A', 'B']], poly=[FILL('SBC', '#86e0bd', .3)]),
  cap=('\\(AH\\perp SB\\) and \\(AH\\perp BC\\) (because \\(BC\\perp(SAB)\\)), so \\(AH=d(A,(SBC))\\).', '\\(AH\\perp SB\\) và \\(AH\\perp BC\\) (vì \\(BC\\perp(SAB)\\)) nên \\(AH=d(A,(SBC))\\).'), alt=('Distance AH from A to the plane SBC', ''), height=360)
theory += '<h3>26.2 %s</h3>' % TI('Parallel line and plane; parallel planes', 'Đường thẳng song song với mặt phẳng; hai mặt phẳng song song')
theory += BOX('blue', ('Definitions', 'Định nghĩa'), UL([T('If \\(a\\parallel(P)\\): \\(d(a,(P))=d(M,(P))\\) for any \\(M\\in a\\).', 'Nếu \\(a\\parallel(P)\\): \\(d(a,(P))=d(M,(P))\\) với \\(M\\) bất kì thuộc \\(a\\).'),
  T('If \\((P)\\parallel(Q)\\): \\(d((P),(Q))=d(M,(Q))\\) for any \\(M\\in(P)\\). Example: in a box, the distance between opposite faces is the edge perpendicular to them.', 'Nếu \\((P)\\parallel(Q)\\): \\(d((P),(Q))=d(M,(Q))\\) với \\(M\\) bất kì thuộc \\((P)\\). Ví dụ: trong hình hộp chữ nhật, khoảng cách giữa hai mặt đối diện bằng cạnh vuông góc với chúng.')]))
theory += '<h3>26.3 %s</h3>' % TI('Distance between two skew lines', 'Khoảng cách giữa hai đường thẳng chéo nhau')
theory += BOX('mint', ('Common perpendicular', 'Đường vuông góc chung'), UL([T('Two skew lines \\(a\\), \\(b\\) have a unique common perpendicular \\(\\Delta\\), meeting them at \\(M\\), \\(N\\); \\(d(a,b)=MN\\), the smallest distance between a point of \\(a\\) and a point of \\(b\\).', 'Hai đường thẳng chéo nhau \\(a\\), \\(b\\) có duy nhất một đường vuông góc chung \\(\\Delta\\), cắt chúng tại \\(M\\), \\(N\\); \\(d(a,b)=MN\\), là khoảng cách nhỏ nhất giữa một điểm của \\(a\\) và một điểm của \\(b\\).'),
  T('Alternative: if \\((P)\\supset b\\) and \\((P)\\parallel a\\), then \\(d(a,b)=d(a,(P))\\).', 'Cách khác: nếu \\((P)\\supset b\\) và \\((P)\\parallel a\\) thì \\(d(a,b)=d(a,(P))\\).')]))
theory += GEO3D(fig('cube', pts={'O': 'mid:A,C'}, seg=[['B', 'D', {'color': BL}], ['A', 'O', {'color': HL}]], hl={('A', 'A′'): BL}, right=[['A′', 'A', 'O'], ['A', 'O', 'B']]),
  cap=('\\(AO\\perp AA\'\\) and \\(AO\\perp BD\\): \\(AO\\) is the common perpendicular, \\(d(AA\',BD)=AO=\\dfrac{a\\sqrt2}2\\).', '\\(AO\\perp AA\'\\) và \\(AO\\perp BD\\): \\(AO\\) là đoạn vuông góc chung, \\(d(AA\',BD)=AO=\\dfrac{a\\sqrt2}2\\).'), alt=('Common perpendicular AO of AA′ and BD in a cube', ''), height=340)
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('A slanted segment is longer than the perpendicular one: \\(d(A,(SBC))=AH\\), not \\(AB\\) or \\(AC\\).', 'Đoạn xiên luôn dài hơn đoạn vuông góc: \\(d(A,(SBC))=AH\\), không phải \\(AB\\) hay \\(AC\\).'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Easy distances', 'Các khoảng cách cơ bản'), T('\\(S.ABCD\\): square base of side \\(a\\), \\(SA\\perp(ABCD)\\), \\(SA=a\\). Find \\(d(S,(ABCD))\\), \\(d(B,(SAD))\\) and \\(d(S,BC)\\).', 'Hình chóp \\(S.ABCD\\) có đáy là hình vuông cạnh \\(a\\), \\(SA\\perp(ABCD)\\), \\(SA=a\\). Tính \\(d(S,(ABCD))\\), \\(d(B,(SAD))\\) và \\(d(S,BC)\\).'),
  T('Look for perpendiculars that already exist.', 'Tìm các đường vuông góc có sẵn.'),
  [T('\\(SA\\perp(ABCD)\\): \\(d(S,(ABCD))=SA=a\\).', '\\(SA\\perp(ABCD)\\): \\(d(S,(ABCD))=SA=a\\).'), T('\\(AB\\perp AD\\), \\(AB\\perp SA\\): \\(AB\\perp(SAD)\\), \\(d(B,(SAD))=BA=a\\).', '\\(AB\\perp AD\\), \\(AB\\perp SA\\): \\(AB\\perp(SAD)\\), \\(d(B,(SAD))=BA=a\\).'),
   T('\\(BC\\perp(SAB)\\Rightarrow SB\\perp BC\\): \\(d(S,BC)=SB=a\\sqrt2\\).', '\\(BC\\perp(SAB)\\Rightarrow SB\\perp BC\\): \\(d(S,BC)=SB=a\\sqrt2\\).')], T('\\(a\\); \\(a\\); \\(a\\sqrt2\\).', '\\(a\\); \\(a\\); \\(a\\sqrt2\\).'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Distances in a cube', 'Khoảng cách trong hình lập phương'), T('Cube \\(ABCD.A\'B\'C\'D\'\\) with edge \\(a\\). Find \\(d(AB,(A\'B\'C\'D\'))\\), \\(d((ABB\'A\'),(DCC\'D\'))\\) and \\(d(AB,CC\')\\).', 'Hình lập phương \\(ABCD.A\'B\'C\'D\'\\) cạnh \\(a\\). Tính \\(d(AB,(A\'B\'C\'D\'))\\), \\(d((ABB\'A\'),(DCC\'D\'))\\) và \\(d(AB,CC\')\\).'),
  T('Parallel line–plane and planes; common perpendicular for skew lines.', 'Đường song song mặt, hai mặt song song; đường vuông góc chung cho hai đường chéo nhau.'),
  [T('\\(AB\\parallel(A\'B\'C\'D\')\\): distance \\(AA\'=a\\).', '\\(AB\\parallel(A\'B\'C\'D\')\\): khoảng cách bằng \\(AA\'=a\\).'), T('Opposite faces: distance \\(AD=a\\).', 'Hai mặt đối diện: khoảng cách bằng \\(AD=a\\).'), T('\\(BC\\perp AB\\), \\(BC\\perp CC\'\\): \\(d(AB,CC\')=BC=a\\).', '\\(BC\\perp AB\\), \\(BC\\perp CC\'\\): \\(d(AB,CC\')=BC=a\\).')],
  T('All three equal \\(a\\).', 'Cả ba đều bằng \\(a\\).'))
assert F(3 * 4, 5) == F(12, 5) and F(1, 9) + F(1, 16) == F(25, 144)
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Point to a slanted plane', 'Từ một điểm đến mặt phẳng xiên'), T('\\(S.ABCD\\): square base of side 4, \\(SA\\perp(ABCD)\\), \\(SA=3\\). Find \\(d(A,(SBC))\\) and \\(d(D,(SBC))\\).', 'Hình chóp \\(S.ABCD\\) có đáy là hình vuông cạnh 4, \\(SA\\perp(ABCD)\\), \\(SA=3\\). Tính \\(d(A,(SBC))\\) và \\(d(D,(SBC))\\).'),
  T('\\(AH\\perp SB\\); \\(AD\\parallel BC\\Rightarrow AD\\parallel(SBC)\\).', '\\(AH\\perp SB\\); \\(AD\\parallel BC\\Rightarrow AD\\parallel(SBC)\\).'),
  [T('\\(SB=5\\); \\(AH=\\dfrac{SA\\cdot AB}{SB}=\\dfrac{12}5\\) (check: \\(\\frac19+\\frac1{16}=\\frac{25}{144}\\)).', '\\(SB=5\\); \\(AH=\\dfrac{SA\\cdot AB}{SB}=\\dfrac{12}5\\) (kiểm tra: \\(\\frac19+\\frac1{16}=\\frac{25}{144}\\)).'), T('\\(D\\) lies on \\(AD\\parallel(SBC)\\): \\(d(D,(SBC))=d(A,(SBC))\\).', '\\(D\\) thuộc \\(AD\\parallel(SBC)\\): \\(d(D,(SBC))=d(A,(SBC))\\).')],
  T('Both equal \\(\\dfrac{12}5\\).', 'Cả hai bằng \\(\\dfrac{12}5\\).'))
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Skew lines in a cube', 'Hai đường chéo nhau trong hình lập phương'), T('Cube \\(ABCD.A\'B\'C\'D\'\\) with edge \\(a\\). Find \\(d(AA\',BD)\\) and \\(d(BB\',AC)\\).', 'Hình lập phương \\(ABCD.A\'B\'C\'D\'\\) cạnh \\(a\\). Tính \\(d(AA\',BD)\\) và \\(d(BB\',AC)\\).'),
  T('\\(O\\) the centre of \\(ABCD\\).', 'Gọi \\(O\\) là tâm hình vuông \\(ABCD\\).'), [T('\\(AO\\perp BD\\) (square), \\(AO\\perp AA\'\\) (\\(AA\'\\perp\\) base): \\(d(AA\',BD)=AO=\\dfrac{a\\sqrt2}2\\).', '\\(AO\\perp BD\\) (hình vuông), \\(AO\\perp AA\'\\) (\\(AA\'\\perp\\) đáy): \\(d(AA\',BD)=AO=\\dfrac{a\\sqrt2}2\\).'), T('Likewise \\(BO\\) is the common perpendicular of \\(BB\'\\), \\(AC\\).', 'Tương tự \\(BO\\) là đoạn vuông góc chung của \\(BB\'\\) và \\(AC\\).')],
  T('Both equal \\(\\dfrac{a\\sqrt2}2\\).', 'Cả hai bằng \\(\\dfrac{a\\sqrt2}2\\).'))
assert abs(1.2 / math.sqrt(3) - 0.693) < 1e-3
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('A glass shelf in a corner', 'Tấm kính góc phòng'), T('In a room corner \\(O\\) the floor and two walls are pairwise perpendicular. A triangular glass shelf is fixed at \\(A\\), \\(B\\), \\(C\\) on the three edges with \\(OA=OB=OC=1{,}2\\) m. How far is the corner from the glass?', 'Tại góc phòng \\(O\\), sàn và hai bức tường đôi một vuông góc. Một tấm kính tam giác được gắn tại \\(A\\), \\(B\\), \\(C\\) trên ba cạnh góc phòng với \\(OA=OB=OC=1{,}2\\) m. Góc phòng cách tấm kính bao xa?'),
  T('\\(OA\\), \\(OB\\), \\(OC\\) pairwise perpendicular: \\(\\dfrac1{d^2}=\\dfrac1{OA^2}+\\dfrac1{OB^2}+\\dfrac1{OC^2}\\).', '\\(OA\\), \\(OB\\), \\(OC\\) đôi một vuông góc: \\(\\dfrac1{d^2}=\\dfrac1{OA^2}+\\dfrac1{OB^2}+\\dfrac1{OC^2}\\).'),
  [T('Let \\(M\\) be the midpoint of \\(BC\\), \\(OH\\perp AM\\): \\(OH\\perp(ABC)\\); applying the right-triangle rule twice gives the formula.', 'Gọi \\(M\\) là trung điểm \\(BC\\), kẻ \\(OH\\perp AM\\): \\(OH\\perp(ABC)\\); áp dụng hệ thức lượng trong tam giác vuông hai lần được công thức trên.'), T('\\(\\dfrac1{d^2}=\\dfrac3{1{,}44}\\Rightarrow d=\\dfrac{1{,}2}{\\sqrt3}\\approx0{,}69\\) m.', '\\(\\dfrac1{d^2}=\\dfrac3{1{,}44}\\Rightarrow d=\\dfrac{1{,}2}{\\sqrt3}\\approx0{,}69\\) m.')],
  T('About 0,69 m.', 'Khoảng 0,69 m.'))
examples = EXFIG(examples, 5, GEO3D({'solid': ['O', 'A', 'B', 'C'], 'points': {'O': (0.0, 0.0, 0.0), 'A': (3.2, 0.0, 0.0), 'B': (0.0, 3.2, 0.0), 'C': (0.0, 0.0, 3.2), 'M': (0.0, 1.6, 1.6), 'H': (1.0667, 1.0667, 1.0667)}, 'segments': [['A', 'M', {'color': '#1d4ed8'}], ['O', 'H', {'color': '#c2410c', 'width': 3.6}]], 'polygons': [FILL('ABC', '#bfdbfe', .45)], 'right': [['A', 'O', 'B'], ['B', 'O', 'C'], ['O', 'H', 'M']], 'px': 340, 'oblique': (0.65, 215)}, alt=('Corner O with three perpendicular edges and the plane ABC', '')))


def lvl(P):
    h, a, s = P['asbc']
    o1 = M4(1, '\\(S.ABCD\\): square base of side %d, \\(SA\\perp(ABCD)\\), \\(SA=%d\\). \\(d(A,(SBC))=\\)…' % (a, h), 'Hình chóp \\(S.ABCD\\) có đáy là hình vuông cạnh %d, \\(SA\\perp(ABCD)\\), \\(SA=%d\\). \\(d(A,(SBC))\\) bằng…' % (a, h), '\\(%s\\)' % fr(F(h * a, s)),
            ['\\(%d\\)' % h, '\\(%d\\)' % a, '\\(%s\\)' % fr(F(s, 2))], '\\(AH\\perp SB\\), \\(AH=\\dfrac{SA\\cdot AB}{SB}\\).', 'Kẻ \\(AH\\perp SB\\): \\(AH=\\dfrac{SA\\cdot AB}{SB}=\\dfrac{%d\\cdot%d}{%d}\\).' % (h, a, s))
    p, q, ok, ee, ev = P['cube']
    o2 = M4(2, 'Cube \\(ABCD.A\'B\'C\'D\'\\) with edge \\(a\\). The distance between \\(%s\\) and \\(%s\\) is…' % (p, q), 'Hình lập phương \\(ABCD.A\'B\'C\'D\'\\) cạnh \\(a\\). Khoảng cách giữa \\(%s\\) và \\(%s\\) bằng…' % (p, q), '\\(%s\\)' % ok,
            ['\\(%s\\)' % o for o in ['a', 'a\\sqrt2', '\\dfrac{a\\sqrt2}{2}', '\\dfrac{a\\sqrt3}{3}', 'a\\sqrt3'] if o != ok][:3], ee[0].upper() + ee[1:] + '.', ev[0].upper() + ev[1:] + '.')
    h3, a3, s3 = P['sbc']
    o3 = M4(3, '\\(S.ABCD\\): square base of side %d, \\(SA\\perp(ABCD)\\), \\(SA=%d\\). \\(d(S,BC)=\\)…' % (a3, h3), 'Hình chóp \\(S.ABCD\\) có đáy là hình vuông cạnh %d, \\(SA\\perp(ABCD)\\), \\(SA=%d\\). \\(d(S,BC)\\) bằng…' % (a3, h3), '\\(%d\\)' % s3,
            ['\\(%d\\)' % h3, '\\(%s\\)' % rt(h3 * h3 + 2 * a3 * a3), '\\(%s\\)' % fr(F(h3 * a3, s3))], '\\(SB\\perp BC\\).', '\\(BC\\perp(SAB)\\) nên \\(SB\\perp BC\\): \\(d=SB=%d\\).' % s3)
    (se, sv), val = P['stmt']
    t4 = tf(4, se, sv, val, 'Recall the definitions.', 'Nhớ lại các định nghĩa khoảng cách.')
    (le, lv_), v5 = P['ccheck']
    t5 = tf(5, le, lv_, v5, 'Find the perpendicular segment.', 'Tìm đoạn vuông góc tương ứng.')
    h6, a6, s6_ = P['int']; d6 = F(h6 * a6, s6_); assert d6.denominator == 1
    s6 = sh(6, '\\(S.ABCD\\): square base of side %d, \\(SA\\perp(ABCD)\\), \\(SA=%d\\). Find \\(d(A,(SBC))\\).' % (a6, h6), 'Hình chóp \\(S.ABCD\\) có đáy là hình vuông cạnh %d, \\(SA\\perp(ABCD)\\), \\(SA=%d\\). Tính \\(d(A,(SBC))\\).' % (a6, h6), int(d6),
            '\\(AH=\\dfrac{SA\\cdot AB}{SB}\\).', '\\(SB=%d\\), \\(AH=\\dfrac{%d\\cdot%d}{%d}=%d\\).' % (s6_, h6, a6, s6_, int(d6)))
    a7, h7, so7 = P['tent']
    s7 = sh(7, 'A square courtyard \\(ABCD\\) has side %d m; a pole \\(SA=%d\\) m stands vertically at \\(A\\). A rope runs from \\(S\\) to the diagonal \\(BD\\) along the shortest path. How long is it (m)?' % (a7, h7), 'Một sân hình vuông \\(ABCD\\) cạnh %d m; cột \\(SA=%d\\) m dựng thẳng đứng tại \\(A\\). Căng dây từ \\(S\\) đến đường chéo \\(BD\\) theo đường ngắn nhất. Sợi dây dài bao nhiêu mét?' % (a7, h7), so7,
            'Shortest to \\(BD\\): \\(SO\\), \\(O\\) the centre.', 'Đường ngắn nhất là \\(SO\\) (\\(BD\\perp(SAO)\\)): \\(SO=\\sqrt{%d+%d}=%d\\).' % (h7 * h7, a7 * a7 // 2, so7))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]


STM = [(('The distance between two skew lines is the length of their common perpendicular segment.', 'Khoảng cách giữa hai đường thẳng chéo nhau bằng độ dài đoạn vuông góc chung của chúng.'), True),
       (('The distance from a point to a plane is the length of any segment from the point to the plane.', 'Khoảng cách từ một điểm đến một mặt phẳng bằng độ dài một đoạn thẳng bất kì nối điểm đó với mặt phẳng.'), False),
       (('If \\((P)\\parallel(Q)\\), \\(d((P),(Q))=d(M,(Q))\\) for every \\(M\\in(P)\\).', 'Nếu \\((P)\\parallel(Q)\\) thì \\(d((P),(Q))=d(M,(Q))\\) với mọi \\(M\\in(P)\\).'), True)]
CC = [(('In a cube of edge \\(a\\): \\(d(A,(A\'BD))=\\dfrac{a\\sqrt3}{3}\\).', 'Trong hình lập phương cạnh \\(a\\): \\(d(A,(A\'BD))=\\dfrac{a\\sqrt3}{3}\\).'), True),
      (('In a cube of edge \\(a\\): \\(d(AB,C\'D\')=a\\).', 'Trong hình lập phương cạnh \\(a\\): \\(d(AB,C\'D\')=a\\).'), False),
      (('In a cube of edge \\(a\\): \\(d(AA\',BD)=\\dfrac{a\\sqrt2}{2}\\).', 'Trong hình lập phương cạnh \\(a\\): \\(d(AA\',BD)=\\dfrac{a\\sqrt2}{2}\\).'), True)]
PP = [dict(asbc=(3, 4, 5), cube=S.CUBE_D[0], sbc=(6, 8, 10), stmt=STM[0], ccheck=CC[0], int=(15, 20, 25), tent=(8, 2, 6)),
      dict(asbc=(5, 12, 13), cube=S.CUBE_D[4], sbc=(5, 12, 13), stmt=STM[1], ccheck=CC[1], int=(30, 40, 50), tent=(12, 3, 9)),
      dict(asbc=(8, 6, 10), cube=S.CUBE_D[5], sbc=(9, 12, 15), stmt=STM[2], ccheck=CC[2], int=(20, 15, 25), tent=(16, 4, 12))]
for pp in PP:
    a7, h7, so7 = pp['tent']; assert h7 * h7 + a7 * a7 // 2 == so7 * so7 and a7 % 2 == 0
practice = three(lvl, PP)
practice = with_self(practice, S.M26S11, start=8)
mistakes = [('<b>Taking a slanted segment as the distance.</b> \\(d(A,(SBC))\\) is not \\(AB\\): first construct the perpendicular \\(AH\\).', '<b>Lấy đoạn xiên làm khoảng cách.</b> \\(d(A,(SBC))\\) không phải \\(AB\\): phải dựng đoạn vuông góc \\(AH\\) trước.'),
            ('<b>Drawing \\(AH\\perp SC\\) instead of \\(AH\\perp SB\\).</b> \\(H\\) must lie on the line where \\((SAB)\\) (which is perpendicular to \\((SBC)\\)) meets \\((SBC)\\): that line is \\(SB\\).', '<b>Kẻ \\(AH\\perp SC\\) thay vì \\(AH\\perp SB\\).</b> \\(H\\) phải nằm trên giao tuyến của \\((SAB)\\) (mặt vuông góc với \\((SBC)\\)) với \\((SBC)\\), tức là \\(SB\\).'),
            ('<b>Forgetting to use parallelism.</b> \\(d(D,(SBC))=d(A,(SBC))\\) since \\(AD\\parallel(SBC)\\).', '<b>Quên dùng quan hệ song song.</b> \\(d(D,(SBC))=d(A,(SBC))\\) vì \\(AD\\parallel(SBC)\\).'),
            ('<b>For skew lines, using a segment perpendicular to only one line.</b> The common perpendicular is perpendicular to both.', '<b>Với hai đường chéo nhau, dùng đoạn chỉ vuông góc với một đường.</b> Đoạn vuông góc chung phải vuông góc với cả hai.')]
summary = [('\\(d(M,(P))=MH\\), \\(H\\) the projection; \\(SA\\perp\\) base: \\(\\dfrac1{AH^2}=\\dfrac1{SA^2}+\\dfrac1{AB^2}\\).', '\\(d(M,(P))=MH\\), \\(H\\) là hình chiếu; \\(SA\\perp\\) đáy: \\(\\dfrac1{AH^2}=\\dfrac1{SA^2}+\\dfrac1{AB^2}\\).'),
           ('Parallel objects: take any convenient point.', 'Các đối tượng song song: lấy một điểm thuận tiện bất kì.'), ('Skew lines: common perpendicular, or a plane through one line parallel to the other.', 'Hai đường chéo nhau: đoạn vuông góc chung, hoặc mặt phẳng chứa đường này và song song với đường kia.'),
           ('Key words: distance, projection, common perpendicular, skew lines.', 'Từ cần nhớ: distance, projection, common perpendicular, skew lines.')]
checks = [('I can compute distances from a point to a line and to a plane.', 'Em tính được khoảng cách từ điểm đến đường thẳng, mặt phẳng.'), ('I can use parallelism to move a point.', 'Em dùng quan hệ song song để đổi điểm.'),
          ('I can find simple common perpendiculars.', 'Em xác định được đoạn vuông góc chung trong trường hợp đơn giản.'), ('I can solve real distance problems.', 'Em giải được bài toán khoảng cách thực tế.')]
LL('g11-perp-05', 'Distances in Space', CV, ('Perpendicularity in Space', 'Quan hệ vuông góc trong không gian'), 'perpendicularity-in-space', 'distances-in-space', 270, 'Intermediate', 80, ('perpendicular planes, projections', 'hai mặt phẳng vuông góc, phép chiếu vuông góc'),
   'Distance from a point to a line and to a plane; parallel lines and planes; common perpendicular and distance between skew lines.', 'Bài 26 – Khoảng cách từ điểm đến đường thẳng, mặt phẳng; giữa các đối tượng song song; đường vuông góc chung, khoảng cách giữa hai đường thẳng chéo nhau.',
   ['distance', 'common perpendicular', 'skew lines'], ['khoảng cách', 'đường vuông góc chung', 'chéo nhau'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g11-perp-04'])
