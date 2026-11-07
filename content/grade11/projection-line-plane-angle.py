# -*- coding: utf-8 -*-
"""g11-perp-03 = Toán 11 KNTT, Bài 24: Phép chiếu vuông góc. Góc giữa đường thẳng và mặt phẳng. Mã ngân hàng câu hỏi: TOAN11-C7-B24."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
from mb_solids import fig, FILL, HL, BL, GR
import sp_g11h as S

CV = 'Phép chiếu vuông góc. Góc giữa đường thẳng và mặt phẳng'
vocab = defs(CV, [
 ('orthproj', 'orthogonal projection', 'phép chiếu vuông góc', 'the parallel projection onto a plane in the direction perpendicular to that plane.', 'phép chiếu song song lên một mặt phẳng theo phương vuông góc với mặt phẳng đó.', 'The orthogonal projection of S is A.', ''),
 ('threeperp', 'three perpendiculars theorem', 'định lí ba đường vuông góc', '\\(a\\subset(P)\\), \\(b\'\\) the projection of \\(b\\) on \\((P)\\): \\(a\\perp b\\iff a\\perp b\'\\).', '\\(a\\subset(P)\\), \\(b\'\\) là hình chiếu của \\(b\\) lên \\((P)\\): \\(a\\perp b\\iff a\\perp b\'\\).', 'By the three perpendiculars theorem, SB ⊥ BC.', ''),
 ('anglp2', 'angle between a line and a plane', 'góc giữa đường thẳng và mặt phẳng (hình học)', 'the angle between the line and its orthogonal projection on the plane (\\(90^\\circ\\) if the line is perpendicular to the plane).', 'góc giữa đường thẳng và hình chiếu vuông góc của nó trên mặt phẳng (bằng \\(90^\\circ\\) nếu đường thẳng vuông góc với mặt phẳng).', 'The angle between SC and the base is 60°.', '\\((d,(P))\\)')])
goals = [('find orthogonal projections of points and lines on a plane;', 'xác định hình chiếu vuông góc của điểm, đường thẳng lên mặt phẳng ([[phép chiếu vuông góc]]);'),
         ('use the three perpendiculars theorem to prove right angles;', 'vận dụng [[định lí ba đường vuông góc]] để chứng minh góc vuông;'),
         ('find and compute the angle between a line and a plane;', 'xác định và tính [[góc giữa đường thẳng và mặt phẳng (hình học)|góc giữa đường thẳng và mặt phẳng (hình học)]];'),
         ('apply slopes of ramps, ladders and roofs.', 'vận dụng vào độ dốc của đường dốc, thang, mái nhà.')]
goals[2] = (goals[2][0], 'xác định và tính [[góc giữa đường thẳng và mặt phẳng|góc giữa đường thẳng và mặt phẳng (hình học)]];')
phrases = [('<b>The projection of \\(S\\) on the base is \\(A\\).</b>', 'Hình chiếu của \\(S\\) lên đáy là \\(A\\).'), ('<b>The projection of \\(SC\\) is \\(AC\\).</b>', 'Hình chiếu của \\(SC\\) là \\(AC\\).'),
           ('<b>The angle between \\(SC\\) and the base is the angle \\(SCA\\).</b>', 'Góc giữa \\(SC\\) và đáy là góc \\(SCA\\).'), ('<b>By the three perpendiculars theorem, \\(SB\\) is perpendicular to \\(BC\\).</b>', 'Theo định lí ba đường vuông góc, \\(SB\\) vuông góc với \\(BC\\).'), ('<b>The ramp makes an angle of about five degrees with the ground.</b>', 'Đường dốc tạo với mặt đất góc khoảng 5°.')]
review = T('From Bài 23: \\(d\\perp(P)\\) when \\(d\\) is perpendicular to two intersecting lines of \\((P)\\). From Bài 14: parallel projection. Grade 9: \\(\\tan\\alpha=\\dfrac{\\text{opposite}}{\\text{adjacent}}\\) in a right triangle.',
           'Từ Bài 23: \\(d\\perp(P)\\) khi \\(d\\) vuông góc với hai đường thẳng cắt nhau của \\((P)\\). Từ Bài 14: phép chiếu song song. Lớp 9: trong tam giác vuông \\(\\tan\\alpha=\\dfrac{\\text{đối}}{\\text{kề}}\\).')
theory = '<h3>24.1 %s</h3>' % TI('Orthogonal projection', 'Phép chiếu vuông góc')
theory += BOX('blue', ('Definition', 'Định nghĩa'), UL([T('The projection of \\(M\\) on \\((P)\\) is the foot \\(H\\) of the perpendicular from \\(M\\) to \\((P)\\). It is the parallel projection along a direction perpendicular to \\((P)\\).', 'Hình chiếu của \\(M\\) lên \\((P)\\) là chân \\(H\\) của đường vuông góc kẻ từ \\(M\\) đến \\((P)\\). Đó là phép chiếu song song theo phương vuông góc với \\((P)\\).'),
  T('The projection of a line not perpendicular to \\((P)\\) is a line; it is enough to project two of its points. A point of \\((P)\\) is its own projection.', 'Hình chiếu của đường thẳng không vuông góc với \\((P)\\) là một đường thẳng; chỉ cần chiếu hai điểm của nó. Điểm nằm trên \\((P)\\) có hình chiếu là chính nó.')]))
theory += BOX('mint', ('Three perpendiculars theorem', 'Định lí ba đường vuông góc'), T('Let \\(a\\subset(P)\\) and let \\(b\\) be a line not perpendicular to \\((P)\\) with projection \\(b\'\\). Then \\(a\\perp b\\iff a\\perp b\'\\).', 'Cho \\(a\\subset(P)\\) và đường thẳng \\(b\\) không vuông góc với \\((P)\\), có hình chiếu \\(b\'\\) trên \\((P)\\). Khi đó \\(a\\perp b\\iff a\\perp b\'\\).'))
theory += '<h3>24.2 %s</h3>' % TI('The angle between a line and a plane', 'Góc giữa đường thẳng và mặt phẳng')
theory += BOX('blue', ('Definition', 'Định nghĩa'), UL([T('If \\(d\\perp(P)\\): \\((d,(P))=90^\\circ\\). Otherwise \\((d,(P))\\) is the angle between \\(d\\) and its projection \\(d\'\\) on \\((P)\\). So \\(0^\\circ\\le(d,(P))\\le90^\\circ\\); it is \\(0^\\circ\\) when \\(d\\parallel(P)\\) or \\(d\\subset(P)\\).', 'Nếu \\(d\\perp(P)\\): \\((d,(P))=90^\\circ\\). Ngược lại, \\((d,(P))\\) là góc giữa \\(d\\) và hình chiếu \\(d\'\\) của nó trên \\((P)\\). Vậy \\(0^\\circ\\le(d,(P))\\le90^\\circ\\); bằng \\(0^\\circ\\) khi \\(d\\parallel(P)\\) hoặc \\(d\\subset(P)\\).'),
  T('Method for a slant segment \\(SM\\) (\\(M\\in(P)\\)): find the projection \\(H\\) of \\(S\\); then \\((SM,(P))=\\widehat{SMH}\\) and \\(\\tan\\widehat{SMH}=\\dfrac{SH}{HM}\\).', 'Cách làm với đoạn xiên \\(SM\\) (\\(M\\in(P)\\)): tìm hình chiếu \\(H\\) của \\(S\\); khi đó \\((SM,(P))=\\widehat{SMH}\\) và \\(\\tan\\widehat{SMH}=\\dfrac{SH}{HM}\\).')]))
theory += GEO3D(fig('pyrsq', seg=[['A', 'C', {'color': BL}], ['S', 'C', {'color': HL}]], angles=[['S', 'C', 'A']], right=[['S', 'A', 'C']]),
  cap=('\\(SA\\perp(ABCD)\\): the projection of \\(S\\) is \\(A\\), of \\(SC\\) is \\(AC\\), so \\((SC,(ABCD))=\\widehat{SCA}\\).', '\\(SA\\perp(ABCD)\\): hình chiếu của \\(S\\) là \\(A\\), của \\(SC\\) là \\(AC\\), nên \\((SC,(ABCD))=\\widehat{SCA}\\).'),
  alt=('The angle SCA between SC and the base', ''), height=360)
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('Do not take the angle with any line of the plane: \\((SC,(ABCD))\\) is the angle with the <i>projection</i> \\(AC\\), not with \\(BC\\) or \\(CD\\). It is the smallest angle between \\(SC\\) and the lines of the plane.', 'Không lấy góc với một đường bất kì của mặt phẳng: \\((SC,(ABCD))\\) là góc với <i>hình chiếu</i> \\(AC\\), không phải với \\(BC\\) hay \\(CD\\). Đó là góc nhỏ nhất giữa \\(SC\\) và các đường thẳng của mặt phẳng.'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Projection and angle', 'Hình chiếu và góc'), T('\\(S.ABCD\\): square base of side \\(a\\), \\(SA\\perp(ABCD)\\), \\(SA=a\\sqrt3\\). Find the angles between \\(SB\\), \\(SD\\) and the base.', 'Hình chóp \\(S.ABCD\\) có đáy là hình vuông cạnh \\(a\\), \\(SA\\perp(ABCD)\\), \\(SA=a\\sqrt3\\). Tính góc giữa \\(SB\\), \\(SD\\) và mặt đáy.'),
  T('Projections: \\(S\\to A\\), \\(B\\to B\\).', 'Hình chiếu: \\(S\\to A\\), \\(B\\to B\\).'),
  [T('\\((SB,(ABCD))=\\widehat{SBA}\\), \\(\\tan\\widehat{SBA}=\\dfrac{SA}{AB}=\\sqrt3\\Rightarrow60^\\circ\\).', '\\((SB,(ABCD))=\\widehat{SBA}\\), \\(\\tan\\widehat{SBA}=\\dfrac{SA}{AB}=\\sqrt3\\Rightarrow60^\\circ\\).'), T('Likewise \\((SD,(ABCD))=\\widehat{SDA}=60^\\circ\\) (\\(AD=AB\\)).', 'Tương tự \\((SD,(ABCD))=\\widehat{SDA}=60^\\circ\\) (vì \\(AD=AB\\)).')],
  T('Both angles equal \\(60^\\circ\\).', 'Cả hai góc bằng \\(60^\\circ\\).'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Three perpendiculars', 'Ba đường vuông góc'), T('\\(S.ABCD\\): \\(ABCD\\) is a rectangle and \\(SA\\perp(ABCD)\\). Prove \\(SB\\perp BC\\) and \\(SD\\perp CD\\).', 'Hình chóp \\(S.ABCD\\) có \\(ABCD\\) là hình chữ nhật, \\(SA\\perp(ABCD)\\). Chứng minh \\(SB\\perp BC\\) và \\(SD\\perp CD\\).'),
  T('The projection of \\(SB\\) on the base is \\(AB\\).', 'Hình chiếu của \\(SB\\) lên đáy là \\(AB\\).'),
  [T('\\(BC\\subset(ABCD)\\), \\(BC\\perp AB\\) = projection of \\(SB\\): by the theorem \\(BC\\perp SB\\).', '\\(BC\\subset(ABCD)\\), \\(BC\\perp AB\\) là hình chiếu của \\(SB\\): theo định lí, \\(BC\\perp SB\\).'), T('\\(CD\\perp AD\\) = projection of \\(SD\\): \\(CD\\perp SD\\).', '\\(CD\\perp AD\\) là hình chiếu của \\(SD\\): \\(CD\\perp SD\\).')],
  T('Triangles \\(SBC\\), \\(SDC\\) are right-angled at \\(B\\), \\(D\\).', 'Tam giác \\(SBC\\), \\(SDC\\) vuông tại \\(B\\), \\(D\\).'))
assert math.isclose(math.degrees(math.atan(1 / math.sqrt(2))), 35.26, abs_tol=0.01)
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('A diagonal of a cube', 'Đường chéo hình lập phương'), T('Find the angle between the diagonal \\(A\'C\\) of the cube \\(ABCD.A\'B\'C\'D\'\\) (edge \\(a\\)) and the base \\((ABCD)\\).', 'Tính góc giữa đường chéo \\(A\'C\\) của hình lập phương \\(ABCD.A\'B\'C\'D\'\\) (cạnh \\(a\\)) và mặt đáy \\((ABCD)\\).'),
  T('\\(AA\'\\perp(ABCD)\\): the projection of \\(A\'C\\) is \\(AC\\).', '\\(AA\'\\perp(ABCD)\\): hình chiếu của \\(A\'C\\) là \\(AC\\).'),
  [T('\\(\\varphi=\\widehat{A\'CA}\\), \\(\\tan\\varphi=\\dfrac{AA\'}{AC}=\\dfrac{a}{a\\sqrt2}=\\dfrac{\\sqrt2}2\\).', '\\(\\varphi=\\widehat{A\'CA}\\), \\(\\tan\\varphi=\\dfrac{AA\'}{AC}=\\dfrac{a}{a\\sqrt2}=\\dfrac{\\sqrt2}2\\).')],
  T('\\(\\tan\\varphi=\\dfrac{\\sqrt2}2\\), \\(\\varphi\\approx35{,}26^\\circ\\).', '\\(\\tan\\varphi=\\dfrac{\\sqrt2}2\\), \\(\\varphi\\approx35{,}26^\\circ\\).'))
examples = EXFIG(examples, 3, GEO3D(fig('cube', seg=[['A', 'C', {'color': BL}], ['A′', 'C', {'color': HL}]], angles=[['A′', 'C', 'A']], right=[['A′', 'A', 'C']]), alt=('Cube with the angle between A′C and the base', '')))
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('A regular pyramid', 'Hình chóp đều'), T('Regular pyramid \\(S.ABCD\\) with base side \\(a\\) and lateral edge \\(a\\sqrt2\\). Find the angle between \\(SA\\) and the base, and the height.', 'Hình chóp tứ giác đều \\(S.ABCD\\) có cạnh đáy \\(a\\), cạnh bên \\(a\\sqrt2\\). Tính góc giữa \\(SA\\) và đáy, và chiều cao của hình chóp.'),
  T('In a regular pyramid the projection of \\(S\\) is the centre \\(O\\).', 'Trong hình chóp đều, hình chiếu của \\(S\\) là tâm \\(O\\) của đáy.'),
  [T('\\(AO=\\dfrac{a\\sqrt2}2\\); \\(\\cos\\widehat{SAO}=\\dfrac{AO}{SA}=\\dfrac12\\Rightarrow\\widehat{SAO}=60^\\circ\\).', '\\(AO=\\dfrac{a\\sqrt2}2\\); \\(\\cos\\widehat{SAO}=\\dfrac{AO}{SA}=\\dfrac12\\Rightarrow\\widehat{SAO}=60^\\circ\\).'), T('\\(SO=\\sqrt{2a^2-\\frac{a^2}2}=\\dfrac{a\\sqrt6}2\\).', '\\(SO=\\sqrt{2a^2-\\frac{a^2}2}=\\dfrac{a\\sqrt6}2\\).')],
  T('\\(60^\\circ\\); \\(SO=\\dfrac{a\\sqrt6}2\\).', '\\(60^\\circ\\); \\(SO=\\dfrac{a\\sqrt6}2\\).'))
assert math.isclose(math.degrees(math.atan(0.6 / 7.2)), 4.76, abs_tol=0.01)
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('A wheelchair ramp', 'Đường dốc cho xe lăn'), T('Building guides require a wheelchair ramp to rise at most 1 m for every 12 m of horizontal length. A ramp rises 0,6 m over a horizontal length of 7,2 m. Find the angle between the ramp and the ground. Does it meet the guide?', 'Hướng dẫn xây dựng yêu cầu đường dốc cho xe lăn cao không quá 1 m trên mỗi 12 m chiều dài nằm ngang. Một đường dốc cao 0,6 m trên chiều dài nằm ngang 7,2 m. Tính góc giữa mặt dốc và mặt đất. Đường dốc có đạt yêu cầu không?'),
  T('The projection of the ramp line on the ground is its horizontal length.', 'Hình chiếu của đường dốc lên mặt đất là chiều dài nằm ngang.'),
  [T('\\(\\tan\\varphi=\\dfrac{0{,}6}{7{,}2}=\\dfrac1{12}\\Rightarrow\\varphi\\approx4{,}76^\\circ\\).', '\\(\\tan\\varphi=\\dfrac{0{,}6}{7{,}2}=\\dfrac1{12}\\Rightarrow\\varphi\\approx4{,}76^\\circ\\).'), T('The ratio is exactly \\(1:12\\): it just meets the guide.', 'Tỉ số đúng bằng \\(1:12\\): vừa đạt yêu cầu.')],
  T('About \\(4{,}76^\\circ\\); acceptable (limit case).', 'Khoảng \\(4{,}76^\\circ\\); đạt yêu cầu (trường hợp giới hạn).'))


def lvl(P):
    side, sa, d1 = P['sb']
    o1 = M4(1, '\\(S.ABCD\\): square base of side %d, \\(SA\\perp(ABCD)\\), \\(SA=%s\\). The angle between \\(SB\\) and the base is…' % (side, sa), 'Hình chóp \\(S.ABCD\\) có đáy là hình vuông cạnh %d, \\(SA\\perp(ABCD)\\), \\(SA=%s\\). Góc giữa \\(SB\\) và mặt đáy bằng…' % (side, sa), '\\(%d^\\circ\\)' % d1,
            ['\\(%d^\\circ\\)' % x for x in (30, 45, 60, 90) if x != d1], '\\(\\tan\\widehat{SBA}=\\dfrac{SA}{AB}\\).', '\\(\\tan\\widehat{SBA}=\\dfrac{SA}{AB}\\).')
    side2, sa2, d2 = P['sc']
    o2 = M4(2, '\\(S.ABCD\\): square base of side %d, \\(SA\\perp(ABCD)\\), \\(SA=%s\\). The angle between \\(SC\\) and the base is…' % (side2, sa2), 'Hình chóp \\(S.ABCD\\) có đáy là hình vuông cạnh %d, \\(SA\\perp(ABCD)\\), \\(SA=%s\\). Góc giữa \\(SC\\) và mặt đáy bằng…' % (side2, sa2), '\\(%d^\\circ\\)' % d2,
            ['\\(%d^\\circ\\)' % x for x in (30, 45, 60, 90) if x != d2], '\\(\\tan\\widehat{SCA}=\\dfrac{SA}{AC}\\), \\(AC=%d\\sqrt2\\).' % side2, '\\(\\tan\\widehat{SCA}=\\dfrac{SA}{AC}\\) với \\(AC=%d\\sqrt2\\).' % side2)
    s, p = P['proj']
    o3 = M4(3, '\\(S.ABCD\\) (square base, centre \\(O\\)), \\(SA\\perp(ABCD)\\). The projection of \\(%s\\) on \\((ABCD)\\) is…' % s, 'Hình chóp \\(S.ABCD\\) có đáy hình vuông tâm \\(O\\), \\(SA\\perp(ABCD)\\). Hình chiếu vuông góc của \\(%s\\) lên \\((ABCD)\\) là…' % s, '\\(%s\\)' % p,
            ['\\(%s\\)' % x for x in ('BC', 'BD', 'CD', 'AB', 'AC', 'AD') if x != p][:3], 'The projection of \\(S\\) is \\(A\\).', 'Hình chiếu của \\(S\\) là \\(A\\).')
    (se, sv), val = P['stmt']
    t4 = tf(4, se, sv, val, 'Recall the definition.', 'Nhớ lại định nghĩa góc giữa đường thẳng và mặt phẳng.')
    (l1, l2), v5, why = P['three']
    t5 = tf(5, '\\(S.ABCD\\): square base, \\(SA\\perp(ABCD)\\). Then \\(%s\\perp %s\\).' % (l1, l2), 'Hình chóp \\(S.ABCD\\) có đáy hình vuông, \\(SA\\perp(ABCD)\\). Khi đó \\(%s\\perp %s\\).' % (l1, l2), v5, why[0], why[1])
    side6, so6, d6 = P['reg']
    s6 = sh(6, 'Regular pyramid \\(S.ABCD\\): base side %d, height \\(SO=%s\\). Find the angle (degrees) between a lateral edge and the base.' % (side6, so6), 'Hình chóp tứ giác đều \\(S.ABCD\\) có cạnh đáy %d, chiều cao \\(SO=%s\\). Tính góc (độ) giữa cạnh bên và mặt đáy.' % (side6, so6), d6,
            '\\(\\tan\\widehat{SAO}=\\dfrac{SO}{AO}\\), \\(AO=\\dfrac{%d\\sqrt2}2\\).' % side6, '\\(\\tan\\widehat{SAO}=\\dfrac{SO}{AO}\\) với \\(AO=\\dfrac{%d\\sqrt2}2\\).' % side6)
    a, b, c = P['lad']
    s7 = sh(7, 'A %d m ladder leans on a vertical wall with its top %d m high. Find the length (m) of its orthogonal projection on the flat ground.' % (c, b), 'Một chiếc thang dài %d m dựa vào tường thẳng đứng, đỉnh thang cao %d m. Tính độ dài (m) hình chiếu vuông góc của thang trên mặt đất phẳng.' % (c, b), a,
            '\\(\\sqrt{%d-%d}\\).' % (c * c, b * b), 'Hình chiếu là đoạn nối chân thang với chân tường: \\(\\sqrt{%d-%d}=%d\\).' % (c * c, b * b, a))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]


STM = [(('The angle between a line and a plane can be obtuse.', 'Góc giữa đường thẳng và mặt phẳng có thể là góc tù.'), False),
       (('If \\(d\\perp(P)\\), the angle between \\(d\\) and \\((P)\\) is \\(90^\\circ\\).', 'Nếu \\(d\\perp(P)\\) thì góc giữa \\(d\\) và \\((P)\\) bằng \\(90^\\circ\\).'), True),
       (('If \\(d\\parallel(P)\\), the angle between \\(d\\) and \\((P)\\) is \\(90^\\circ\\).', 'Nếu \\(d\\parallel(P)\\) thì góc giữa \\(d\\) và \\((P)\\) bằng \\(90^\\circ\\).'), False)]
PP = [dict(sb=(2, '2\\sqrt3', 60), sc=(3, '3\\sqrt2', 45), proj=('SD', 'AD'), stmt=STM[0], three=(('SC', 'BD'), True, ('The projection \\(AC\\perp BD\\).', 'Hình chiếu của \\(SC\\) là \\(AC\\perp BD\\) nên \\(SC\\perp BD\\).')), reg=(4, '2\\sqrt2', 45), lad=(6, 8, 10)),
      dict(sb=(3, '3', 45), sc=(2, '2\\sqrt6', 60), proj=('SC', 'AC'), stmt=STM[1], three=(('SB', 'CD'), False, ('\\(CD\\parallel AB\\) and \\(\\widehat{SBA}\\ne90^\\circ\\).', '\\(CD\\parallel AB\\) mà \\(\\widehat{SBA}\\ne90^\\circ\\) nên \\(SB\\) không vuông góc với \\(CD\\).')), reg=(6, '3\\sqrt6', 60), lad=(5, 12, 13)),
      dict(sb=(3, '\\sqrt3', 30), sc=(3, '\\sqrt6', 30), proj=('SO', 'AO'), stmt=STM[2], three=(('SD', 'CD'), True, ('The projection \\(AD\\perp CD\\).', 'Hình chiếu của \\(SD\\) là \\(AD\\perp CD\\) nên \\(SD\\perp CD\\).')), reg=(6, '\\sqrt6', 30), lad=(9, 12, 15))]
for pp in PP:
    s_, a_, d_ = pp['reg']; so = {'2\\sqrt2': 2 * math.sqrt(2), '3\\sqrt6': 3 * math.sqrt(6), '\\sqrt6': math.sqrt(6)}[a_]
    assert round(math.degrees(math.atan(so / (s_ * math.sqrt(2) / 2)))) == d_
practice = three(lvl, PP)
practice = with_self(practice, S.M24S11, start=8)
mistakes = [('<b>Using an edge of the base instead of the projection.</b> \\((SC,(ABCD))=\\widehat{SCA}\\), not \\(\\widehat{SCB}\\).', '<b>Lấy cạnh đáy thay cho hình chiếu.</b> \\((SC,(ABCD))=\\widehat{SCA}\\), không phải \\(\\widehat{SCB}\\).'),
            ('<b>Putting the foot of the height at a vertex of a regular pyramid.</b> The projection of the apex is the centre \\(O\\).', '<b>Đặt chân đường cao của hình chóp đều tại một đỉnh.</b> Hình chiếu của đỉnh là tâm \\(O\\) của đáy.'),
            ('<b>Mixing \\(\\tan\\) and \\(\\sin\\).</b> \\(\\tan=\\dfrac{SH}{HM}\\) (height over projection); \\(\\sin=\\dfrac{SH}{SM}\\).', '<b>Nhầm \\(\\tan\\) và \\(\\sin\\).</b> \\(\\tan=\\dfrac{SH}{HM}\\) (chiều cao chia hình chiếu); \\(\\sin=\\dfrac{SH}{SM}\\).'),
            ('<b>Applying the three perpendiculars theorem to a line not in the plane.</b> The line \\(a\\) must lie in \\((P)\\).', '<b>Dùng định lí ba đường vuông góc khi \\(a\\) không nằm trong mặt phẳng.</b> Đường \\(a\\) phải nằm trong \\((P)\\).')]
summary = [('Projection of \\(M\\): foot of the perpendicular; of a line: project two points.', 'Hình chiếu của \\(M\\): chân đường vuông góc; của đường thẳng: chiếu hai điểm.'),
           ('Three perpendiculars: \\(a\\subset(P)\\): \\(a\\perp b\\iff a\\perp b\'\\).', 'Ba đường vuông góc: \\(a\\subset(P)\\): \\(a\\perp b\\iff a\\perp b\'\\).'),
           ('\\((d,(P))=(d,d\')\\in[0^\\circ;90^\\circ]\\); for \\(SM\\): \\(\\tan\\widehat{SMH}=\\dfrac{SH}{HM}\\).', '\\((d,(P))=(d,d\')\\in[0^\\circ;90^\\circ]\\); với \\(SM\\): \\(\\tan\\widehat{SMH}=\\dfrac{SH}{HM}\\).'),
           ('Key words: orthogonal projection, three perpendiculars, angle between a line and a plane.', 'Từ cần nhớ: orthogonal projection, three perpendiculars, angle between a line and a plane.')]
checks = [('I can find projections of points and lines.', 'Em xác định được hình chiếu của điểm, đường thẳng.'), ('I can use the three perpendiculars theorem.', 'Em vận dụng được định lí ba đường vuông góc.'),
          ('I can compute the angle between a line and a plane.', 'Em tính được góc giữa đường thẳng và mặt phẳng.'), ('I can compute slopes of ramps and ladders.', 'Em tính được độ dốc của đường dốc, thang.')]
LL('g11-perp-03', 'Orthogonal Projection; Angle between a Line and a Plane', CV, ('Perpendicularity in Space', 'Quan hệ vuông góc trong không gian'), 'perpendicularity-in-space', 'projection-line-plane-angle', 250, 'Intermediate', 75, ('a line perpendicular to a plane', 'đường thẳng vuông góc với mặt phẳng'),
   'Orthogonal projection, the three perpendiculars theorem, the angle between a line and a plane.', 'Bài 24 – Phép chiếu vuông góc, định lí ba đường vuông góc, góc giữa đường thẳng và mặt phẳng.',
   ['orthogonal projection', 'three perpendiculars', 'angle line–plane'], ['phép chiếu vuông góc', 'ba đường vuông góc', 'góc giữa đường thẳng và mặt phẳng'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g11-perp-02'])
