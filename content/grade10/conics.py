# -*- coding: utf-8 -*-
"""g10-coord-04 = Toán 10 KNTT, Bài 22: Ba đường conic. Mã ngân hàng câu hỏi: TOAN10-C7-B22."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g10h as S
from sp_g10h import efrm, hfrm

CV = 'Ba đường conic'
vocab = defs(CV, [
 ('ellipse2', 'ellipse', 'đường elip', 'the set of points \\(M\\) with \\(MF_1+MF_2=2a\\) (\\(2a\\gt F_1F_2\\)).', 'tập hợp các điểm \\(M\\) có \\(MF_1+MF_2=2a\\) (\\(2a\\gt F_1F_2\\)).', 'The Earth moves on an ellipse around the Sun.', '\\((E)\\)'),
 ('hyperb', 'hyperbola', 'đường hypebol', 'the set of points \\(M\\) with \\(|MF_1-MF_2|=2a\\) (\\(0\\lt2a\\lt F_1F_2\\)).', 'tập hợp các điểm \\(M\\) có \\(|MF_1-MF_2|=2a\\) (\\(0\\lt2a\\lt F_1F_2\\)).', 'A cooling tower has hyperbolic sides.', '\\((H)\\)'),
 ('parabc', 'parabola (conic)', 'đường parabol (conic)', 'the set of points equidistant from a focus \\(F\\) and a directrix \\(\\Delta\\).', 'tập hợp các điểm cách đều tiêu điểm \\(F\\) và đường chuẩn \\(\\Delta\\).', 'A satellite dish has a parabolic section.', '\\((P)\\)'),
 ('focus', 'focus (plural foci)', 'tiêu điểm', 'a fixed point used to define a conic.', 'điểm cố định dùng để định nghĩa đường conic.', 'The foci are F1 and F2.', '\\(F\\)'),
 ('directrix', 'directrix', 'đường chuẩn', 'the fixed line in the definition of a parabola.', 'đường thẳng cố định trong định nghĩa parabol.', 'The directrix is x = −2.', '\\(\\Delta\\)')])
goals = [('recognise the ellipse, the hyperbola and the parabola from their definitions;', 'nhận biết [[đường elip]], [[đường hypebol]], đường parabol qua định nghĩa;'),
         ('read and write their standard equations, [[tiêu điểm]] and other features;', 'đọc và viết phương trình chính tắc, xác định [[tiêu điểm]], đỉnh, độ dài các trục, [[đường chuẩn]];'),
         ('use the focal properties \\(MF_1+MF_2=2a\\), \\(|MF_1-MF_2|=2a\\), \\(MF=d(M,\\Delta)\\);', 'vận dụng tính chất \\(MF_1+MF_2=2a\\), \\(|MF_1-MF_2|=2a\\), \\(MF=d(M,\\Delta)\\);'),
         ('model real objects: orbits, cooling towers, satellite dishes.', 'mô hình hóa các vật thể thực tế: quỹ đạo, tháp làm nguội, chảo ăng-ten.')]
goals[1] = ('read and write their standard equations, foci and other features;', goals[1][1])
phrases = [('<b>The sum of the distances to the two foci is constant.</b>', 'Tổng khoảng cách đến hai tiêu điểm không đổi.'), ('<b>The ellipse has major axis ten and minor axis six.</b>', 'Elip có trục lớn bằng 10 và trục nhỏ bằng 6.'),
           ('<b>Every point of a parabola is equidistant from the focus and the directrix.</b>', 'Mọi điểm của parabol cách đều tiêu điểm và đường chuẩn.'), ('<b>The asymptotes of the hyperbola are dashed lines.</b>', 'Các đường tiệm cận của hypebol vẽ bằng nét đứt.'), ('<b>Write the standard equation.</b>', 'Viết phương trình chính tắc.')]
review = T('From Bài 21: distance \\(MF=\\sqrt{(x-x_F)^2+(y-y_F)^2}\\). From Bài 20: \\(d(M,\\Delta)\\). From Bài 16: the graph of \\(y=ax^2\\) is a parabola.', 'Từ Bài 21: khoảng cách \\(MF=\\sqrt{(x-x_F)^2+(y-y_F)^2}\\). Từ Bài 20: \\(d(M,\\Delta)\\). Từ Bài 16: đồ thị \\(y=ax^2\\) là một parabol.')
theory = '<h3>22.1 %s</h3>' % TI('The ellipse', 'Đường elip')
theory += BOX('blue', ('Definition and standard equation', 'Định nghĩa và phương trình chính tắc'), UL([T('Given \\(F_1\\), \\(F_2\\) with \\(F_1F_2=2c\\) and \\(a\\gt c\\gt0\\): the ellipse is the set of points \\(M\\) with \\(MF_1+MF_2=2a\\).', 'Cho \\(F_1\\), \\(F_2\\) với \\(F_1F_2=2c\\) và \\(a\\gt c\\gt0\\): elip là tập hợp các điểm \\(M\\) sao cho \\(MF_1+MF_2=2a\\).'),
  T('With \\(F_1(-c;0)\\), \\(F_2(c;0)\\): \\(\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=1\\), \\(a\\gt b\\gt0\\), \\(b^2=a^2-c^2\\).', 'Với \\(F_1(-c;0)\\), \\(F_2(c;0)\\): \\(\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=1\\), \\(a\\gt b\\gt0\\), \\(b^2=a^2-c^2\\).'),
  T('Vertices \\((\\pm a;0)\\), \\((0;\\pm b)\\); major axis \\(2a\\), minor axis \\(2b\\), focal distance \\(2c\\).', 'Đỉnh \\((\\pm a;0)\\), \\((0;\\pm b)\\); trục lớn \\(2a\\), trục nhỏ \\(2b\\), tiêu cự \\(2c\\).')]))
theory += GRAPH({'view': [-6.5, 6.5, -4, 4], 'equal': True, 'functions': [], 'param': [{'x': '5*cos(t)', 'y': '3*sin(t)', 'label': 'x²/25 + y²/9 = 1'}],
  'points': [{'x': -4, 'y': 0, 'label': 'F₁(−4; 0)', 'off': [-6, 8]}, {'x': 4, 'y': 0, 'label': 'F₂(4; 0)', 'off': [6, 8]}, {'x': 3, 'y': 2.4, 'label': 'M', 'color': '#c2410c'}], 'guides': []},
  cap=('\\(a=5\\), \\(b=3\\), \\(c=4\\). For every point \\(M\\): \\(MF_1+MF_2=10\\) (e.g. \\(M(3;\\frac{12}5)\\): \\(MF_1=\\frac{37}5\\), \\(MF_2=\\frac{13}5\\)).', '\\(a=5\\), \\(b=3\\), \\(c=4\\). Với mọi điểm \\(M\\): \\(MF_1+MF_2=10\\) (ví dụ \\(M(3;\\frac{12}5)\\): \\(MF_1=\\frac{37}5\\), \\(MF_2=\\frac{13}5\\)).'),
  alt=('Ellipse with its two foci', ''), height=300)
assert F(9, 25) + F(144, 25) / 9 == 1 and (F(37, 5) ** 2 == 7 ** 2 + F(12, 5) ** 2) and (F(13, 5) ** 2 == 1 + F(12, 5) ** 2)
theory += '<h3>22.2 %s</h3>' % TI('The hyperbola', 'Đường hypebol')
theory += BOX('blue', ('Definition and standard equation', 'Định nghĩa và phương trình chính tắc'), UL([T('Given \\(F_1F_2=2c\\) and \\(0\\lt a\\lt c\\): the hyperbola is the set of points \\(M\\) with \\(|MF_1-MF_2|=2a\\).', 'Cho \\(F_1F_2=2c\\) và \\(0\\lt a\\lt c\\): hypebol là tập hợp các điểm \\(M\\) sao cho \\(|MF_1-MF_2|=2a\\).'),
  T('Standard equation \\(\\dfrac{x^2}{a^2}-\\dfrac{y^2}{b^2}=1\\) with \\(b^2=c^2-a^2\\); foci \\((\\pm c;0)\\), vertices \\((\\pm a;0)\\). It has two branches and two asymptotes \\(y=\\pm\\dfrac bax\\) (dashed in the figure).', 'Phương trình chính tắc \\(\\dfrac{x^2}{a^2}-\\dfrac{y^2}{b^2}=1\\) với \\(b^2=c^2-a^2\\); tiêu điểm \\((\\pm c;0)\\), đỉnh \\((\\pm a;0)\\). Hypebol có hai nhánh và hai đường tiệm cận \\(y=\\pm\\dfrac bax\\) (nét đứt trong hình).')]))
theory += GRAPH({'view': [-8, 8, -5, 5], 'equal': True, 'functions': [], 'param': [{'x': '4*cosh(t)', 'y': '3*sinh(t)', 'range': [-1.75, 1.75], 'label': 'x²/16 − y²/9 = 1'}, {'x': '-4*cosh(t)', 'y': '3*sinh(t)', 'range': [-1.75, 1.75], 'color': '#046b4d'}],
  'asymptotes': [{'type': 'o', 'm': 0.75, 'b': 0, 'label': 'y = 3x/4'}, {'type': 'o', 'm': -0.75, 'b': 0, 'label': 'y = −3x/4'}],
  'points': [{'x': -5, 'y': 0, 'label': 'F₁', 'off': [-4, 8]}, {'x': 5, 'y': 0, 'label': 'F₂', 'off': [4, 8]}]},
  cap=('\\(a=4\\), \\(b=3\\), \\(c=5\\). The two branches approach the dashed asymptotes \\(y=\\pm\\frac34x\\).', '\\(a=4\\), \\(b=3\\), \\(c=5\\). Hai nhánh tiến sát hai đường tiệm cận nét đứt \\(y=\\pm\\frac34x\\).'), alt=('Hyperbola with its two foci and dashed asymptotes', ''), height=320)
theory += '<h3>22.3 %s</h3>' % TI('The parabola', 'Đường parabol')
theory += BOX('blue', ('Definition and standard equation', 'Định nghĩa và phương trình chính tắc'), UL([T('Given a point \\(F\\) and a line \\(\\Delta\\) not through \\(F\\): the parabola is the set of points \\(M\\) with \\(MF=d(M,\\Delta)\\).', 'Cho điểm \\(F\\) và đường thẳng \\(\\Delta\\) không đi qua \\(F\\): parabol là tập hợp các điểm \\(M\\) sao cho \\(MF=d(M,\\Delta)\\).'),
  T('Standard equation \\(y^2=2px\\) (\\(p\\gt0\\)): focus \\(F\\left(\\frac p2;0\\right)\\), directrix \\(x=-\\frac p2\\), vertex \\(O\\). For \\(M(x;y)\\) on it: \\(MF=x+\\frac p2\\).', 'Phương trình chính tắc \\(y^2=2px\\) (\\(p\\gt0\\)): tiêu điểm \\(F\\left(\\frac p2;0\\right)\\), đường chuẩn \\(x=-\\frac p2\\), đỉnh \\(O\\). Với \\(M(x;y)\\) thuộc parabol: \\(MF=x+\\frac p2\\).')]))
theory += GRAPH({'view': [-3.5, 7, -6, 6], 'equal': True, 'functions': [], 'param': [{'x': 't*t/8', 'y': 't', 'range': [-6.5, 6.5], 'label': 'y² = 8x'}, {'x': '-2+0*t', 'y': 't', 'range': [-6, 6], 'color': '#7c3aed', 'samples': 2}], 'points': [{'x': 2, 'y': 0, 'label': 'F(2; 0)', 'off': [6, -12]}, {'x': 4.5, 'y': 6, 'label': 'M', 'color': '#c2410c'}],
  'texts': [{'x': -2.9, 'y': 4.5, 'text': 'x = −2'}]},
  cap=('\\(y^2=8x\\): \\(p=4\\), focus \\(F(2;0)\\), directrix \\(x=-2\\) (purple). For \\(M(4{,}5;6)\\): \\(MF=6{,}5=d(M,\\Delta)\\).', '\\(y^2=8x\\): \\(p=4\\), tiêu điểm \\(F(2;0)\\), đường chuẩn \\(x=-2\\) (màu tím). Với \\(M(4{,}5;6)\\): \\(MF=6{,}5=d(M,\\Delta)\\).'), alt=('Parabola with focus and directrix', ''), height=320)
assert 6 ** 2 == 8 * 4.5 and math.hypot(4.5 - 2, 6) == 6.5
theory += BOX('mint', ('Conics around us', 'Conic quanh ta'), UL([T('Planets and satellites move on ellipses with the Sun (or the Earth) at a focus.', 'Hành tinh, vệ tinh chuyển động trên quỹ đạo elip, Mặt Trời (hoặc Trái Đất) ở một tiêu điểm.'),
  T('Cooling towers of power plants have hyperbolic sides: strong and easy to build with straight beams.', 'Tháp làm nguội của nhà máy điện có mặt cắt là hypebol: chắc chắn và dựng được bằng các thanh thẳng.'),
  T('Rays parallel to the axis of a parabolic mirror are reflected to the focus: satellite dishes, solar cookers, car headlights.', 'Tia song song với trục của gương parabol phản xạ hội tụ tại tiêu điểm: chảo ăng-ten, bếp năng lượng mặt trời, đèn pha ô tô.')]))

assert 25 - 9 == 16
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Reading an ellipse', 'Đọc các yếu tố của elip'), T('For \\((E): \\dfrac{x^2}{25}+\\dfrac{y^2}{9}=1\\), find the foci, the vertices and the lengths of the axes.', 'Cho \\((E): \\dfrac{x^2}{25}+\\dfrac{y^2}{9}=1\\). Tìm tiêu điểm, các đỉnh, độ dài các trục.'),
  T('\\(a^2=25\\), \\(b^2=9\\), \\(c^2=a^2-b^2\\).', '\\(a^2=25\\), \\(b^2=9\\), \\(c^2=a^2-b^2\\).'),
  [T('\\(a=5\\), \\(b=3\\), \\(c=\\sqrt{25-9}=4\\).', '\\(a=5\\), \\(b=3\\), \\(c=\\sqrt{25-9}=4\\).'), T('Foci \\(F_1(-4;0)\\), \\(F_2(4;0)\\); vertices \\((\\pm5;0)\\), \\((0;\\pm3)\\).', 'Tiêu điểm \\(F_1(-4;0)\\), \\(F_2(4;0)\\); đỉnh \\((\\pm5;0)\\), \\((0;\\pm3)\\).')],
  T('Major axis 10, minor axis 6, focal distance 8.', 'Trục lớn 10, trục nhỏ 6, tiêu cự 8.'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Writing an ellipse', 'Viết phương trình elip'), T('Write the standard equation of the ellipse with major axis 10 and focal distance 6.', 'Viết phương trình chính tắc của elip có độ dài trục lớn 10 và tiêu cự 6.'),
  T('\\(2a=10\\), \\(2c=6\\).', '\\(2a=10\\), \\(2c=6\\).'), [T('\\(a=5\\), \\(c=3\\), \\(b^2=25-9=16\\).', '\\(a=5\\), \\(c=3\\), \\(b^2=25-9=16\\).')],
  T('\\(\\dfrac{x^2}{25}+\\dfrac{y^2}{16}=1\\).', '\\(\\dfrac{x^2}{25}+\\dfrac{y^2}{16}=1\\).'))
assert 16 + 9 == 25 and 5 + 4 == 9 and 9 + 8 == 17 and 9 - 8 == 1
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('A point on a hyperbola', 'Điểm trên hypebol'), T('For \\((H): \\dfrac{x^2}{16}-\\dfrac{y^2}{9}=1\\): find the foci. A point \\(M\\in(H)\\) has \\(MF_1=9\\). Find \\(MF_2\\).', 'Cho \\((H): \\dfrac{x^2}{16}-\\dfrac{y^2}{9}=1\\). Tìm tiêu điểm. Điểm \\(M\\in(H)\\) có \\(MF_1=9\\). Tính \\(MF_2\\).'),
  T('\\(c^2=a^2+b^2\\); \\(|MF_1-MF_2|=2a\\).', '\\(c^2=a^2+b^2\\); \\(|MF_1-MF_2|=2a\\).'),
  [T('\\(a=4\\), \\(b=3\\), \\(c=5\\): \\(F_1(-5;0)\\), \\(F_2(5;0)\\).', '\\(a=4\\), \\(b=3\\), \\(c=5\\): \\(F_1(-5;0)\\), \\(F_2(5;0)\\).'), T('\\(|9-MF_2|=8\\Rightarrow MF_2=1\\) or \\(MF_2=17\\).', '\\(|9-MF_2|=8\\Rightarrow MF_2=1\\) hoặc \\(MF_2=17\\).'),
   T('Both occur: \\(MF_2=1\\) at the vertex \\((4;0)\\); \\(MF_2=17\\) on the left branch.', 'Cả hai đều xảy ra: \\(MF_2=1\\) tại đỉnh \\((4;0)\\); \\(MF_2=17\\) trên nhánh trái.')],
  T('\\(MF_2=1\\) or \\(MF_2=17\\).', '\\(MF_2=1\\) hoặc \\(MF_2=17\\).'))
assert 2 * 4 == 8 and 3 + 2 == 5 and 8 * 3 == 24
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Focus and directrix', 'Tiêu điểm và đường chuẩn'), T('For \\((P): y^2=8x\\): find the focus and the directrix. A point \\(M\\in(P)\\) has \\(x_M=3\\); find \\(MF\\) and \\(y_M\\).', 'Cho \\((P): y^2=8x\\). Tìm tiêu điểm, đường chuẩn. Điểm \\(M\\in(P)\\) có hoành độ 3; tính \\(MF\\) và \\(y_M\\).'),
  T('\\(2p=8\\).', '\\(2p=8\\).'), [T('\\(p=4\\): \\(F(2;0)\\), \\(\\Delta: x=-2\\).', '\\(p=4\\): \\(F(2;0)\\), \\(\\Delta: x=-2\\).'), T('\\(MF=d(M,\\Delta)=3+2=5\\); \\(y_M^2=24\\Rightarrow y_M=\\pm2\\sqrt6\\).', '\\(MF=d(M,\\Delta)=3+2=5\\); \\(y_M^2=24\\Rightarrow y_M=\\pm2\\sqrt6\\).')],
  T('\\(F(2;0)\\), \\(x=-2\\), \\(MF=5\\), \\(y_M=\\pm2\\sqrt6\\).', '\\(F(2;0)\\), \\(x=-2\\), \\(MF=5\\), \\(y_M=\\pm2\\sqrt6\\).'))
assert 40 ** 2 == 160 * 10 and F(160, 4) == 40
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Where to put the receiver?', 'Đặt đầu thu ở đâu?'), T('A satellite dish has a parabolic cross-section, diameter 80 cm and depth 10 cm. How far from the vertex must the receiver be?', 'Một chảo ăng-ten có thiết diện là parabol, đường kính miệng 80 cm, độ sâu 10 cm. Đầu thu phải đặt cách đỉnh chảo bao xa?'),
  T('Put the vertex at \\(O\\), the axis along \\(Ox\\): \\(y^2=2px\\) passes through \\((10;40)\\).', 'Đặt đỉnh tại \\(O\\), trục chảo theo \\(Ox\\): \\(y^2=2px\\) đi qua \\((10;40)\\).'),
  [T('\\(1600=2p\\cdot10\\Rightarrow2p=160\\), \\(p=80\\).', '\\(1600=2p\\cdot10\\Rightarrow2p=160\\), \\(p=80\\).'), T('The focus is at \\(\\frac p2=40\\) cm: incoming parallel signals are reflected there.', 'Tiêu điểm cách đỉnh \\(\\frac p2=40\\) cm: tín hiệu song song với trục phản xạ hội tụ tại đó.')],
  T('40 cm from the vertex, on the axis.', 'Cách đỉnh 40 cm, trên trục của chảo.'))


def lvl(P):
    a, b, c = P['ell']
    o1 = M4(1, 'The foci of \\(%s\\) are…' % efrm(a * a, b * b), 'Tiêu điểm của elip \\(%s\\) là…' % efrm(a * a, b * b), '\\(F_{1,2}(\\pm%d;0)\\)' % c,
            ['\\(F_{1,2}(\\pm%d;0)\\)' % a, '\\(F_{1,2}(0;\\pm%d)\\)' % c, '\\(F_{1,2}(\\pm%d;0)\\)' % b], '\\(c^2=a^2-b^2\\).', '\\(c^2=a^2-b^2=%d\\Rightarrow c=%d\\).' % (c * c, c))
    ha, hc = P['hyp']; hb2 = hc * hc - ha * ha
    o2 = M4(2, 'The hyperbola with vertices \\((\\pm%d;0)\\) and foci \\((\\pm%d;0)\\) is…' % (ha, hc), 'Hypebol có đỉnh \\((\\pm%d;0)\\) và tiêu điểm \\((\\pm%d;0)\\) là…' % (ha, hc), '\\(%s\\)' % hfrm(ha * ha, hb2),
            ['\\(%s\\)' % hfrm(ha * ha, hc * hc + ha * ha), '\\(%s\\)' % efrm(hc * hc, hb2) if hc * hc != hb2 else '\\(%s\\)' % efrm(hc * hc, 1), '\\(%s\\)' % hfrm(hc * hc, ha * ha)], '\\(b^2=c^2-a^2\\).', '\\(b^2=c^2-a^2=%d\\).' % hb2)
    q = P['par']; p = F(q, 2)
    o3 = M4(3, 'The focus of the parabola \\(y^2=%dx\\) is…' % q, 'Tiêu điểm của parabol \\(y^2=%dx\\) là…' % q, '\\(F(%s;0)\\)' % fr(p / 2),
            ['\\(F(%s;0)\\)' % fr(p), '\\(F(%d;0)\\)' % q, '\\(F(0;%s)\\)' % fr(p / 2)], '\\(2p=%d\\), \\(F(\\frac p2;0)\\).' % q, '\\(2p=%d\\Rightarrow p=%s\\), \\(F\\left(\\frac p2;0\\right)\\).' % (q, fr(p)))
    (a4, b4), claim = P['sum']
    t4 = tf(4, 'For every \\(M\\) on \\(%s\\): \\(MF_1+MF_2=%d\\).' % (efrm(a4 * a4, b4), claim), 'Với mọi điểm \\(M\\) thuộc elip \\(%s\\): \\(MF_1+MF_2=%d\\).' % (efrm(a4 * a4, b4), claim), claim == 2 * a4,
            '\\(MF_1+MF_2=2a=%d\\).' % (2 * a4), '\\(MF_1+MF_2=2a=%d\\).' % (2 * a4))
    eq5, kind5, said5 = P['kind']; names = {'e': ('an ellipse', 'đường elip'), 'h': ('a hyperbola', 'đường hypebol'), 'p': ('a parabola', 'đường parabol')}
    t5 = tf(5, '\\(%s\\) is %s.' % (eq5, names[said5][0]), '\\(%s\\) là %s.' % (eq5, names[said5][1]), kind5 == said5, 'It is %s.' % names[kind5][0], 'Đó là %s.' % names[kind5][1])
    a6, b6, c6 = P['foc']
    s6 = sh(6, 'Find the focal distance \\(F_1F_2\\) of \\(%s\\).' % efrm(a6 * a6, b6 * b6), 'Tính tiêu cự \\(F_1F_2\\) của elip \\(%s\\).' % efrm(a6 * a6, b6 * b6), 2 * c6,
            '\\(c=\\sqrt{a^2-b^2}=%d\\).' % c6, '\\(c=\\sqrt{a^2-b^2}=%d\\Rightarrow F_1F_2=2c=%d\\).' % (c6, 2 * c6))
    D, h = P['dish']; two_p = F((D // 2) ** 2, h); f = two_p / 4; assert f.denominator == 1
    s7 = sh(7, 'A satellite dish (parabolic section) has diameter %d cm and depth %d cm. How many centimetres from the vertex is the focus?' % (D, h), 'Chảo ăng-ten (thiết diện parabol) có đường kính miệng %d cm và độ sâu %d cm. Tiêu điểm cách đỉnh chảo bao nhiêu xentimét?' % (D, h), int(f),
            '\\(y^2=2px\\) through \\((%d;%d)\\).' % (h, D // 2), '\\(y^2=2px\\) đi qua \\((%d;%d)\\): \\(2p=%s\\), tiêu điểm cách đỉnh \\(\\frac p2=%d\\) cm.' % (h, D // 2, fr(two_p), int(f)))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]


PP = [dict(ell=(5, 4, 3), hyp=(3, 5), par=12, sum=((6, 20), 12), kind=('\\dfrac{x^2}{16}-\\dfrac{y^2}{9}=1', 'h', 'e'), foc=(10, 8, 6), dish=(60, 5)),
      dict(ell=(13, 12, 5), hyp=(4, 5), par=6, sum=((7, 24), 7), kind=('y^2=10x', 'p', 'p'), foc=(13, 12, 5), dish=(120, 15)),
      dict(ell=(10, 6, 8), hyp=(12, 13), par=20, sum=((5, 9), 10), kind=('\\dfrac{x^2}{9}+\\dfrac{y^2}{4}=1', 'e', 'h'), foc=(17, 15, 8), dish=(40, 4))]
practice = three(lvl, PP)
practice = with_self(practice, S.M22S10, start=8)
mistakes = [('<b>Using \\(c^2=a^2+b^2\\) for an ellipse.</b> Ellipse: \\(c^2=a^2-b^2\\); hyperbola: \\(c^2=a^2+b^2\\).', '<b>Dùng \\(c^2=a^2+b^2\\) cho elip.</b> Elip: \\(c^2=a^2-b^2\\); hypebol: \\(c^2=a^2+b^2\\).'),
            ('<b>Reading \\(a\\) as \\(a^2\\).</b> In \\(\\frac{x^2}{25}+\\frac{y^2}{9}=1\\): \\(a=5\\), the major axis is 10, not 25.', '<b>Nhầm \\(a\\) với \\(a^2\\).</b> Trong \\(\\frac{x^2}{25}+\\frac{y^2}{9}=1\\): \\(a=5\\), trục lớn bằng 10, không phải 25.'),
            ('<b>Focus of \\(y^2=2px\\) at \\((p;0)\\).</b> The focus is \\(\\left(\\frac p2;0\\right)\\): for \\(y^2=8x\\), \\(p=4\\), \\(F(2;0)\\).', '<b>Tiêu điểm của \\(y^2=2px\\) là \\((p;0)\\).</b> Tiêu điểm là \\(\\left(\\frac p2;0\\right)\\): với \\(y^2=8x\\), \\(p=4\\), \\(F(2;0)\\).'),
            ('<b>Forgetting the absolute value for the hyperbola.</b> \\(|MF_1-MF_2|=2a\\) gives two cases.', '<b>Quên giá trị tuyệt đối ở hypebol.</b> \\(|MF_1-MF_2|=2a\\) cho hai trường hợp.')]
summary = [('Ellipse: \\(MF_1+MF_2=2a\\); \\(\\frac{x^2}{a^2}+\\frac{y^2}{b^2}=1\\), \\(b^2=a^2-c^2\\).', 'Elip: \\(MF_1+MF_2=2a\\); \\(\\frac{x^2}{a^2}+\\frac{y^2}{b^2}=1\\), \\(b^2=a^2-c^2\\).'),
           ('Hyperbola: \\(|MF_1-MF_2|=2a\\); \\(\\frac{x^2}{a^2}-\\frac{y^2}{b^2}=1\\), \\(b^2=c^2-a^2\\); asymptotes \\(y=\\pm\\frac bax\\).', 'Hypebol: \\(|MF_1-MF_2|=2a\\); \\(\\frac{x^2}{a^2}-\\frac{y^2}{b^2}=1\\), \\(b^2=c^2-a^2\\); tiệm cận \\(y=\\pm\\frac bax\\).'),
           ('Parabola: \\(MF=d(M,\\Delta)\\); \\(y^2=2px\\), \\(F(\\frac p2;0)\\), \\(\\Delta: x=-\\frac p2\\).', 'Parabol: \\(MF=d(M,\\Delta)\\); \\(y^2=2px\\), \\(F(\\frac p2;0)\\), \\(\\Delta: x=-\\frac p2\\).'),
           ('Key words: ellipse, hyperbola, parabola, focus, directrix, vertex, axis.', 'Từ cần nhớ: ellipse, hyperbola, parabola, focus, directrix, vertex, axis.')]
checks = [('I can tell the three conics from their equations.', 'Em phân biệt được ba đường conic qua phương trình.'), ('I can find foci, vertices and axes.', 'Em tìm được tiêu điểm, đỉnh, độ dài các trục.'),
          ('I can write a standard equation from given data.', 'Em viết được phương trình chính tắc từ dữ kiện.'), ('I can use conics in real models.', 'Em vận dụng được conic trong mô hình thực tế.')]
LL('g10-coord-04', 'The Three Conics', CV, ('Coordinate Geometry in the Plane', 'Phương pháp tọa độ trong mặt phẳng'), 'plane-coordinates', 'conics', 220, 'Intermediate', 75, ('circles, distance', 'đường tròn, khoảng cách'),
   'Ellipse, hyperbola and parabola: definitions, standard equations, foci, vertices, directrix; real models.', 'Bài 22 – Elip, hypebol, parabol: định nghĩa, phương trình chính tắc, tiêu điểm, đỉnh, đường chuẩn; mô hình thực tế.',
   ['ellipse', 'hyperbola', 'parabola', 'focus'], ['elip', 'hypebol', 'parabol', 'tiêu điểm'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g10-coord-03'])
