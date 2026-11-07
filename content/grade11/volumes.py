# -*- coding: utf-8 -*-
"""g11-perp-06 = Toán 11 KNTT, Bài 27: Thể tích. Mã ngân hàng câu hỏi: TOAN11-C7-B27."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
from mb_solids import fig, FILL, HL, BL, GR
import sp_g11i as S
from sp_g11h import rq, co

CV = 'Thể tích khối chóp, khối lăng trụ'
vocab = defs(CV, [
 ('vpyr', 'volume of a pyramid', 'thể tích khối chóp', '\\(V=\\frac13Bh\\), \\(B\\) the base area, \\(h\\) the height.', '\\(V=\\frac13Bh\\), \\(B\\) là diện tích đáy, \\(h\\) là chiều cao.', 'The volume of the pyramid is 48.', '\\(V\\)'),
 ('vprism', 'volume of a prism', 'thể tích khối lăng trụ', '\\(V=Bh\\).', '\\(V=Bh\\).', 'The volume of the prism is 60.', ''),
 ('frustumv', 'volume of a frustum', 'thể tích khối chóp cụt đều', '\\(V=\\frac h3\\left(S+S\'+\\sqrt{SS\'}\\right)\\), \\(S\\), \\(S\'\\) the areas of the two bases.', '\\(V=\\frac h3\\left(S+S\'+\\sqrt{SS\'}\\right)\\), \\(S\\), \\(S\'\\) là diện tích hai đáy.', 'A bucket shaped like a frustum holds 28 litres.', '')])
goals = [('recall the volume formulas of pyramids, frustums, prisms, boxes and cubes;', 'nhớ công thức [[thể tích khối chóp]], [[thể tích khối chóp cụt đều]], [[thể tích khối lăng trụ]], khối hộp chữ nhật, khối lập phương;'),
         ('find the height and the base area needed in a given solid;', 'xác định chiều cao và diện tích đáy cần thiết của khối đã cho;'),
         ('compare volumes by ratios;', 'so sánh thể tích bằng tỉ số;'),
         ('compute capacities of tanks, buckets and famous buildings.', 'tính sức chứa của bể, xô và thể tích các công trình nổi tiếng.')]
phrases = [('<b>The volume equals one third of the base area times the height.</b>', 'Thể tích bằng một phần ba diện tích đáy nhân chiều cao.'), ('<b>The height is the edge perpendicular to the base.</b>', 'Chiều cao là cạnh vuông góc với đáy.'),
           ('<b>One cubic decimetre is one litre.</b>', 'Một đề-xi-mét khối bằng một lít.'), ('<b>The ratio of the volumes is one sixth.</b>', 'Tỉ số thể tích bằng một phần sáu.'), ('<b>Compute the area of the base first.</b>', 'Tính diện tích đáy trước.')]
review = T('From Bài 23–26: heights are perpendicular segments; regular pyramids project onto the centre. Areas: square \\(a^2\\), right triangle \\(\\frac12pq\\), equilateral triangle \\(\\frac{a^2\\sqrt3}4\\).', 'Từ Bài 23–26: chiều cao là đoạn vuông góc; hình chóp đều có đỉnh chiếu xuống tâm đáy. Diện tích: hình vuông \\(a^2\\), tam giác vuông \\(\\frac12pq\\), tam giác đều \\(\\frac{a^2\\sqrt3}4\\).')
theory = '<h3>27.1 %s</h3>' % TI('Pyramids and frustums', 'Khối chóp và khối chóp cụt đều')
theory += BOX('blue', ('Formulas', 'Công thức'), UL([T('Pyramid: \\(V=\\dfrac13Bh\\) (\\(h\\) = distance from the apex to the base plane).', 'Khối chóp: \\(V=\\dfrac13Bh\\) (\\(h\\) là khoảng cách từ đỉnh đến mặt phẳng đáy).'),
  T('Regular frustum with base areas \\(S\\), \\(S\'\\) and height \\(h\\): \\(V=\\dfrac h3\\left(S+S\'+\\sqrt{SS\'}\\right)\\) (the big pyramid minus the small one).', 'Khối chóp cụt đều có diện tích hai đáy \\(S\\), \\(S\'\\), chiều cao \\(h\\): \\(V=\\dfrac h3\\left(S+S\'+\\sqrt{SS\'}\\right)\\) (khối chóp lớn trừ khối chóp nhỏ).')]))
cfg = fig('pyrsq', pts={'O': (0, 0, 0)}, seg=[['S', 'O', {'color': HL, 'dash': True}], ['A', 'C'], ['B', 'D']], right=[['S', 'O', 'B']], poly=[FILL('ABCD', '#86e0bd', .35)])
cfg['points']['S'] = (0.0, 0.0, 3.4)
theory += GEO3D(cfg, cap=('Regular pyramid: base \\(B=AB^2\\), height \\(h=SO\\); \\(V=\\frac13AB^2\\cdot SO\\).', 'Hình chóp đều: đáy \\(B=AB^2\\), chiều cao \\(h=SO\\); \\(V=\\frac13AB^2\\cdot SO\\).'), alt=('Regular pyramid with its height SO', ''), height=340)
theory += '<h3>27.2 %s</h3>' % TI('Prisms, boxes, cubes', 'Khối lăng trụ, khối hộp, khối lập phương')
theory += BOX('blue', ('Formulas', 'Công thức'), UL([T('Prism: \\(V=Bh\\) (for a right prism \\(h\\) is the lateral edge).', 'Khối lăng trụ: \\(V=Bh\\) (với lăng trụ đứng, \\(h\\) là cạnh bên).'), T('Box: \\(V=abc\\); cube: \\(V=a^3\\).', 'Khối hộp chữ nhật: \\(V=abc\\); khối lập phương: \\(V=a^3\\).'),
  T('Ratio rule: for \\(M\\in SA\\), \\(N\\in SB\\), \\(P\\in SC\\): \\(\\dfrac{V_{S.MNP}}{V_{S.ABC}}=\\dfrac{SM}{SA}\\cdot\\dfrac{SN}{SB}\\cdot\\dfrac{SP}{SC}\\).', 'Tỉ số thể tích: với \\(M\\in SA\\), \\(N\\in SB\\), \\(P\\in SC\\): \\(\\dfrac{V_{S.MNP}}{V_{S.ABC}}=\\dfrac{SM}{SA}\\cdot\\dfrac{SN}{SB}\\cdot\\dfrac{SP}{SC}\\).')]))
frust = {'solid': ['A', 'B', 'C', 'D', 'A′', 'B′', 'C′', 'D′'], 'points': {'A': (-2.2, -2.2, 0.0), 'B': (2.2, -2.2, 0.0), 'C': (2.2, 2.2, 0.0), 'D': (-2.2, 2.2, 0.0), 'A′': (-1.1, -1.1, 2.6), 'B′': (1.1, -1.1, 2.6), 'C′': (1.1, 1.1, 2.6), 'D′': (-1.1, 1.1, 2.6), 'O': (0.0, 0.0, 0.0), 'O′': (0.0, 0.0, 2.6)},
         'segments': [['O', 'O′', {'color': HL, 'dash': True}]], 'polygons': [FILL(['A′', 'B′', 'C′', 'D′'], '#fde68a', .5)], 'px': 340}
theory += GEO3D(frust, cap=('A regular square frustum: bases of areas \\(S\\), \\(S\'\\), height \\(h=OO\'\\).', 'Khối chóp cụt tứ giác đều: hai đáy có diện tích \\(S\\), \\(S\'\\), chiều cao \\(h=OO\'\\).'), alt=('Regular square frustum with its height', ''), height=300)
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('Do not forget the factor \\(\\frac13\\) for pyramids, and use the <i>height</i>, not a lateral edge (except for right prisms).', 'Đừng quên hệ số \\(\\frac13\\) của khối chóp, và dùng <i>chiều cao</i>, không dùng cạnh bên (trừ lăng trụ đứng).'))

assert 36 * 4 // 3 == 48 and 16 + 18 == 34
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('A regular pyramid', 'Khối chóp đều'), T('A regular pyramid \\(S.ABCD\\) has base side 6 and height 4. Find its volume and its lateral edge.', 'Khối chóp tứ giác đều \\(S.ABCD\\) có cạnh đáy 6, chiều cao 4. Tính thể tích và độ dài cạnh bên.'),
  T('\\(B=36\\), \\(h=4\\); \\(AO=3\\sqrt2\\).', '\\(B=36\\), \\(h=4\\); \\(AO=3\\sqrt2\\).'), [T('\\(V=\\frac13\\cdot36\\cdot4=48\\).', '\\(V=\\frac13\\cdot36\\cdot4=48\\).'), T('\\(SA=\\sqrt{SO^2+AO^2}=\\sqrt{16+18}=\\sqrt{34}\\).', '\\(SA=\\sqrt{SO^2+AO^2}=\\sqrt{16+18}=\\sqrt{34}\\).')], T('\\(V=48\\), \\(SA=\\sqrt{34}\\).', '\\(V=48\\), \\(SA=\\sqrt{34}\\).'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('A right prism', 'Khối lăng trụ đứng'), T('A right prism has a right-triangle base with legs 3 and 4 and lateral edge 10. Find its volume.', 'Khối lăng trụ đứng có đáy là tam giác vuông với hai cạnh góc vuông 3 và 4, cạnh bên 10. Tính thể tích.'),
  T('\\(V=Bh\\), \\(h\\) = lateral edge.', '\\(V=Bh\\), \\(h\\) là cạnh bên.'), [T('\\(B=\\frac12\\cdot3\\cdot4=6\\); \\(V=6\\cdot10\\).', '\\(B=\\frac12\\cdot3\\cdot4=6\\); \\(V=6\\cdot10\\).')], T('60.', '60.'))
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Height from an angle', 'Chiều cao qua góc'), T('\\(S.ABCD\\): square base of side \\(a\\), \\(SA\\perp(ABCD)\\), \\(SC\\) makes \\(45^\\circ\\) with the base. Find the volume.', 'Hình chóp \\(S.ABCD\\) có đáy là hình vuông cạnh \\(a\\), \\(SA\\perp(ABCD)\\), \\(SC\\) tạo với đáy góc \\(45^\\circ\\). Tính thể tích khối chóp.'),
  T('\\((SC,(ABCD))=\\widehat{SCA}=45^\\circ\\).', '\\((SC,(ABCD))=\\widehat{SCA}=45^\\circ\\).'), [T('Triangle \\(SAC\\) is right isosceles: \\(SA=AC=a\\sqrt2\\).', 'Tam giác \\(SAC\\) vuông cân: \\(SA=AC=a\\sqrt2\\).'), T('\\(V=\\frac13a^2\\cdot a\\sqrt2\\).', '\\(V=\\frac13a^2\\cdot a\\sqrt2\\).')],
  T('\\(V=\\dfrac{a^3\\sqrt2}3\\).', '\\(V=\\dfrac{a^3\\sqrt2}3\\).'))
assert 1 * (16 + 4 + 8) == 28 and F(3 * 4 * 5, 6) == 10
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('A bucket', 'Cái xô'), T('A bucket is a regular square frustum: bottom side 2 dm, top side 4 dm, height 3 dm. How many litres does it hold?', 'Một cái xô có dạng khối chóp cụt tứ giác đều: cạnh đáy dưới 2 dm, cạnh miệng 4 dm, cao 3 dm. Xô chứa được bao nhiêu lít?'),
  T('\\(S=16\\), \\(S\'=4\\), \\(h=3\\).', '\\(S=16\\), \\(S\'=4\\), \\(h=3\\).'), [T('\\(V=\\frac33(16+4+\\sqrt{64})=28\\ \\text{dm}^3\\).', '\\(V=\\frac33(16+4+\\sqrt{64})=28\\ \\text{dm}^3\\).')], T('28 litres.', '28 lít.'))
VG = F(230 * 230 * 146, 3); assert int(VG) == 2574466
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('The Great Pyramid', 'Kim tự tháp Kê-ốp'), T('The Great Pyramid of Giza was a regular square pyramid with base side about 230 m and height about 146 m. Estimate its volume. If the stone blocks average 1,1 m³, roughly how many blocks were used?', 'Kim tự tháp Kê-ốp (Ai Cập) ban đầu là khối chóp tứ giác đều có cạnh đáy khoảng 230 m, chiều cao khoảng 146 m. Ước tính thể tích. Nếu mỗi khối đá trung bình 1,1 m³ thì cần khoảng bao nhiêu khối?'),
  T('\\(V=\\frac13Bh\\).', '\\(V=\\frac13Bh\\).'), [T('\\(V=\\frac13\\cdot230^2\\cdot146\\approx2\\,574\\,467\\) m³.', '\\(V=\\frac13\\cdot230^2\\cdot146\\approx2\\,574\\,467\\) m³.'), T('Blocks \\(\\approx\\dfrac{2\\,574\\,467}{1{,}1}\\approx2{,}3\\) million (a little less in reality: the inner chambers are empty).', 'Số khối \\(\\approx\\dfrac{2\\,574\\,467}{1{,}1}\\approx2{,}3\\) triệu (thực tế ít hơn một chút vì có các phòng rỗng bên trong).')],
  T('About 2,57 million m³, about 2,3 million blocks.', 'Khoảng 2,57 triệu m³, khoảng 2,3 triệu khối đá.'))


def lvl(P):
    a, h = P['pyr']; V1 = F(a * a * h, 3)
    o1 = M4(1, 'A pyramid with square base of side %d and height %d has volume…' % (a, h), 'Khối chóp có đáy là hình vuông cạnh %d, chiều cao %d có thể tích…' % (a, h), '\\(%s\\)' % fr(V1),
            ['\\(%d\\)' % (a * a * h), '\\(%s\\)' % fr(F(a * a * h, 6)), '\\(%s\\)' % fr(F(a * h, 3))], '\\(V=\\frac13Bh\\).', '\\(V=\\frac13\\cdot%d\\cdot%d=%s\\).' % (a * a, h, fr(V1)))
    p, q, hh = P['prism']; V2 = F(p * q * hh, 2)
    o2 = M4(2, 'A right prism with right-triangle base (legs %d, %d) and lateral edge %d has volume…' % (p, q, hh), 'Khối lăng trụ đứng có đáy là tam giác vuông (hai cạnh góc vuông %d, %d), cạnh bên %d có thể tích…' % (p, q, hh), '\\(%s\\)' % fr(V2),
            ['\\(%d\\)' % (p * q * hh), '\\(%s\\)' % fr(F(p * q * hh, 6)), '\\(%s\\)' % fr(F(p * q * hh, 3))], '\\(V=Bh\\).', '\\(V=\\frac12\\cdot%d\\cdot%d\\cdot%d=%s\\).' % (p, q, hh, fr(V2)))
    x, y, z = P['oabc']; V3 = F(x * y * z, 6)
    o3 = M4(3, '\\(OA\\), \\(OB\\), \\(OC\\) pairwise perpendicular, \\(OA=%d\\), \\(OB=%d\\), \\(OC=%d\\). \\(V_{OABC}=\\)…' % (x, y, z), 'Tứ diện \\(OABC\\) có \\(OA\\), \\(OB\\), \\(OC\\) đôi một vuông góc, \\(OA=%d\\), \\(OB=%d\\), \\(OC=%d\\). Thể tích bằng…' % (x, y, z), '\\(%s\\)' % fr(V3),
            ['\\(%d\\)' % (x * y * z), '\\(%s\\)' % fr(F(x * y * z, 3)), '\\(%s\\)' % fr(F(x * y * z, 2))], '\\(V=\\frac16OA\\cdot OB\\cdot OC\\).', '\\(V=\\frac16\\cdot%d\\cdot%d\\cdot%d=%s\\).' % (x, y, z, fr(V3)))
    (b1, b2, h4), claim = P['frus']; V4 = F(h4, 3) * (b1 * b1 + b2 * b2 + b1 * b2)
    t4 = tf(4, 'A regular square frustum with base sides %d and %d and height %d has volume %s.' % (b1, b2, h4, fr(claim)), 'Khối chóp cụt tứ giác đều có cạnh hai đáy %d và %d, chiều cao %d có thể tích bằng %s.' % (b1, b2, h4, fr(claim)), V4 == claim,
            '\\(V=\\frac{%d}3(%d+%d+%d)=%s\\).' % (h4, b1 * b1, b2 * b2, b1 * b2, fr(V4)), '\\(V=\\frac{%d}3(%d+%d+%d)=%s\\).' % (h4, b1 * b1, b2 * b2, b1 * b2, fr(V4)))
    (m, n), claim5 = P['ratio']; k = F(*m) * F(*n)
    t5 = tf(5, 'In \\(S.ABC\\), \\(M\\in SA\\), \\(N\\in SB\\) with \\(SM=%s\\,SA\\), \\(SN=%s\\,SB\\). Then \\(V_{S.MNC}=%s\\,V_{S.ABC}\\).' % (fr(F(*m)), fr(F(*n)), fr(claim5)), 'Trong khối chóp \\(S.ABC\\), \\(M\\in SA\\), \\(N\\in SB\\) với \\(SM=%s\\,SA\\), \\(SN=%s\\,SB\\). Khi đó \\(V_{S.MNC}=%s\\,V_{S.ABC}\\).' % (fr(F(*m)), fr(F(*n)), fr(claim5)), k == claim5,
            'Ratio \\(=%s\\cdot%s=%s\\).' % (fr(F(*m)), fr(F(*n)), fr(k)), 'Tỉ số \\(=%s\\cdot%s\\cdot1=%s\\).' % (fr(F(*m)), fr(F(*n)), fr(k)))
    a6 = P['cube']
    s6 = sh(6, 'A cube has diagonal \\(%s\\). Find its volume.' % co(a6, 3), 'Hình lập phương có đường chéo \\(%s\\). Tính thể tích khối lập phương.' % co(a6, 3), a6 ** 3,
            'Edge \\(%d\\).' % a6, 'Đường chéo \\(a\\sqrt3\\Rightarrow a=%d\\), \\(V=%d\\).' % (a6, a6 ** 3))
    (L, W, H) = P['tank']
    s7 = sh(7, 'A rectangular tank is %d dm long, %d dm wide and %d dm deep. How many litres of water does it hold when full?' % (L, W, H), 'Một bể hình hộp chữ nhật dài %d dm, rộng %d dm, sâu %d dm. Khi đầy, bể chứa bao nhiêu lít nước?' % (L, W, H), L * W * H,
            '\\(1\\text{ dm}^3=1\\) L.', '\\(V=%d\\cdot%d\\cdot%d=%d\\text{ dm}^3=%d\\) lít.' % (L, W, H, L * W * H, L * W * H))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]


PP = [dict(pyr=(6, 5), prism=(3, 4, 7), oabc=(2, 3, 4), frus=((6, 3, 4), 84), ratio=(((1, 2), (1, 3)), F(1, 6)), cube=3, tank=(12, 8, 6)),
      dict(pyr=(4, 9), prism=(5, 6, 3), oabc=(3, 5, 6), frus=((5, 2, 6), 80), ratio=(((2, 3), (1, 2)), F(1, 6)), cube=4, tank=(15, 10, 8)),
      dict(pyr=(5, 6), prism=(6, 8, 5), oabc=(4, 4, 9), frus=((4, 2, 3), 28), ratio=(((3, 4), (2, 3)), F(1, 2)), cube=5, tank=(20, 12, 9))]
practice = three(lvl, PP)
practice = with_self(practice, S.M27S11, start=8)
mistakes = [('<b>Forgetting \\(\\frac13\\) for a pyramid.</b> \\(V=\\frac13Bh\\), not \\(Bh\\).', '<b>Quên \\(\\frac13\\) với khối chóp.</b> \\(V=\\frac13Bh\\), không phải \\(Bh\\).'), ('<b>Using a lateral edge as the height of a pyramid.</b> The height is perpendicular to the base.', '<b>Dùng cạnh bên làm chiều cao khối chóp.</b> Chiều cao phải vuông góc với đáy.'),
            ('<b>Frustum: averaging the two areas.</b> Use \\(\\frac h3(S+S\'+\\sqrt{SS\'})\\), not \\(h\\cdot\\frac{S+S\'}2\\).', '<b>Chóp cụt: lấy trung bình hai đáy.</b> Phải dùng \\(\\frac h3(S+S\'+\\sqrt{SS\'})\\), không phải \\(h\\cdot\\frac{S+S\'}2\\).'), ('<b>Mixing units.</b> 1 m³ = 1000 L, 1 dm³ = 1 L.', '<b>Nhầm đơn vị.</b> 1 m³ = 1000 lít, 1 dm³ = 1 lít.')]
summary = [('Pyramid \\(V=\\frac13Bh\\); frustum \\(V=\\frac h3(S+S\'+\\sqrt{SS\'})\\).', 'Khối chóp \\(V=\\frac13Bh\\); chóp cụt \\(V=\\frac h3(S+S\'+\\sqrt{SS\'})\\).'), ('Prism \\(V=Bh\\); box \\(abc\\); cube \\(a^3\\).', 'Lăng trụ \\(V=Bh\\); hộp chữ nhật \\(abc\\); lập phương \\(a^3\\).'),
           ('Ratios: \\(\\dfrac{V_{S.MNP}}{V_{S.ABC}}=\\dfrac{SM}{SA}\\cdot\\dfrac{SN}{SB}\\cdot\\dfrac{SP}{SC}\\).', 'Tỉ số: \\(\\dfrac{V_{S.MNP}}{V_{S.ABC}}=\\dfrac{SM}{SA}\\cdot\\dfrac{SN}{SB}\\cdot\\dfrac{SP}{SC}\\).'), ('Key words: volume, base area, height, frustum, capacity.', 'Từ cần nhớ: volume, base area, height, frustum, capacity.')]
checks = [('I can compute volumes of pyramids and prisms.', 'Em tính được thể tích khối chóp, khối lăng trụ.'), ('I can find the height from angles or distances.', 'Em tìm được chiều cao từ góc hoặc khoảng cách.'),
          ('I can use the frustum formula.', 'Em dùng được công thức khối chóp cụt.'), ('I can convert volumes to litres.', 'Em đổi được thể tích ra lít.')]
LL('g11-perp-06', 'Volumes', CV, ('Perpendicularity in Space', 'Quan hệ vuông góc trong không gian'), 'perpendicularity-in-space', 'volumes', 280, 'Intermediate', 70, ('distances, regular pyramids', 'khoảng cách, hình chóp đều'),
   'Volumes of pyramids, regular frustums, prisms, boxes and cubes; volume ratios; capacities.', 'Bài 27 – Thể tích khối chóp, khối chóp cụt đều, khối lăng trụ, khối hộp, khối lập phương; tỉ số thể tích; sức chứa.',
   ['volume', 'pyramid', 'prism', 'frustum'], ['thể tích', 'khối chóp', 'khối lăng trụ', 'chóp cụt'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g11-perp-05'])
