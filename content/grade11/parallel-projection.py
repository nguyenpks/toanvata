# -*- coding: utf-8 -*-
"""g11-space-08 = Toán 11 KNTT, Bài 14: Phép chiếu song song. Mã ngân hàng câu hỏi: TOAN11-C4-B14."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g11d as S

CV = 'Phép chiếu song song'
vocab = defs(CV, [
 ('pproj', 'parallel projection', 'phép chiếu song song', 'the rule that sends each point \\(M\\) to the point \\(M′\\) where the line through \\(M\\) parallel to \\(l\\) meets the plane \\((P)\\).', 'quy tắc đặt mỗi điểm \\(M\\) với điểm \\(M′\\) là giao của đường thẳng qua \\(M\\) song song (hoặc trùng) với \\(l\\) và mặt phẳng \\((P)\\).', 'Sunlight gives a parallel projection onto the ground.', ''),
 ('pplane', 'plane of projection', 'mặt phẳng chiếu', 'the plane \\((P)\\) that receives the images.', 'mặt phẳng \\((P)\\) chứa các hình chiếu.', 'The ground is the plane of projection.', '\\((P)\\)'),
 ('pdir', 'direction of projection', 'phương chiếu', 'a line \\(l\\) cutting \\((P)\\); all projecting lines are parallel to \\(l\\).', 'đường thẳng \\(l\\) cắt \\((P)\\); mọi đường chiếu đều song song với \\(l\\).', 'The sun\'s rays give the direction of projection.', '\\(l\\)'),
 ('pimg', 'image (of a point or a figure)', 'hình chiếu song song', 'the point \\(M′\\), or the set of images of all points of a figure.', 'điểm \\(M′\\), hoặc tập hợp hình chiếu của mọi điểm của một hình.', 'The image of segment \\(AB\\) is segment \\(A′B′\\).', ''),
 ('prep', 'drawing of a solid (representation)', 'hình biểu diễn', 'the parallel projection of a solid onto a plane, drawn so that it looks like the solid.', 'hình chiếu song song của hình không gian lên một mặt phẳng, vẽ sao cho dễ hình dung.', 'A cube is drawn with parallelogram faces.', ''),
 ('ellip', 'ellipse', 'đường elip', 'the image of a circle under a parallel projection (in general).', 'hình chiếu song song của đường tròn (trong trường hợp tổng quát).', 'A round table top looks like an ellipse in the drawing.', ''),
 ('shadow', 'shadow', 'bóng (của vật)', 'in sunlight, the parallel projection of an object on the ground.', 'dưới ánh nắng, hình chiếu song song của vật lên mặt đất.', 'The shadow of the pole is 4 m long.', '')])
goals = [('describe a parallel projection: plane of projection, direction, image;', 'mô tả [[phép chiếu song song]]: [[mặt phẳng chiếu]], [[phương chiếu]], [[hình chiếu song song]];'),
         ('state what a parallel projection keeps (collinearity, parallelism, ratios) and what it changes (lengths, angles);', 'nêu được phép chiếu song song giữ những gì (thẳng hàng, song song, tỉ số) và làm thay đổi những gì (độ dài, góc);'),
         ('draw correct pictures of plane figures and solids;', 'vẽ đúng [[hình biểu diễn]] của hình phẳng và hình không gian;'),
         ('solve shadow problems in sunlight.', 'giải bài toán về [[bóng (của vật)]] dưới ánh nắng.')]
phrases = [('<b>Find the image of the point under the parallel projection.</b>', 'Tìm hình chiếu của điểm qua phép chiếu song song.'), ('<b>The projection keeps the ratio of the two segments.</b>', 'Phép chiếu giữ nguyên tỉ số hai đoạn thẳng.'),
           ('<b>Draw the representation of the cube.</b>', 'Vẽ hình biểu diễn của hình lập phương.'), ('<b>The image of a circle is an ellipse.</b>', 'Hình chiếu của đường tròn là đường elip.'), ('<b>How long is the shadow of the tree?</b>', 'Bóng của cái cây dài bao nhiêu?')]
review = T('From Bài 11–13: through a point there is exactly one line parallel to a given line; a plane cutting two parallel planes cuts them along parallel lines; Thales: a line parallel to one side of a triangle cuts the other sides proportionally.',
           'Từ Bài 11–13: qua một điểm có đúng một đường thẳng song song với đường thẳng cho trước; mặt phẳng cắt hai mặt phẳng song song theo hai giao tuyến song song; Thalès: đường thẳng song song với một cạnh tam giác chia hai cạnh kia theo cùng tỉ số.')
# hình vẽ: tam giác ABC phía trên mặt phẳng z = 0, chiếu theo phương l
l = (0.9, 0.6, -2.0)
def proj(P): t = -P[2] / l[2]; return tuple(round(p + t * d, 6) for p, d in zip(P, l))
Ap, Bp, Cp = (-2.5, -1, 2.6), (1, -2, 3.2), (0.5, 1.8, 2.2)
A1, B1, C1 = proj(Ap), proj(Bp), proj(Cp)
assert all(abs(q[2]) < 1e-9 for q in (A1, B1, C1))
FIG = {'solid': True, 'box': [[-4, 5], [-3.5, 4], [-0.5, 4]], 'points': {'A': Ap, 'B': Bp, 'C': Cp, 'A′': A1, 'B′': B1, 'C′': C1},
       'polygons': [{'points': ['A', 'B', 'C'], 'fill': '#fde68a', 'opacity': .55}, {'points': ['A′', 'B′', 'C′'], 'fill': '#86e0bd', 'opacity': .5}],
       'segments': [['A', 'A′', {'dash': True, 'color': '#c2410c', 'width': 1.6}], ['B', 'B′', {'dash': True, 'color': '#c2410c', 'width': 1.6}], ['C', 'C′', {'dash': True, 'color': '#c2410c', 'width': 1.6}]]}
theory = '<h3>14.1 %s</h3>' % TI('Definition', 'Định nghĩa')
theory += BOX('blue', ('Parallel projection', 'Phép chiếu song song'), T('Given a plane \\((P)\\) and a line \\(l\\) cutting \\((P)\\). For each point \\(M\\), the line through \\(M\\) parallel to (or equal to) \\(l\\) meets \\((P)\\) at \\(M′\\). The rule \\(M\\mapsto M′\\) is the parallel projection onto \\((P)\\) in the direction \\(l\\); \\(M′\\) is the image of \\(M\\).',
  'Cho mặt phẳng \\((P)\\) và đường thẳng \\(l\\) cắt \\((P)\\). Với mỗi điểm \\(M\\), đường thẳng qua \\(M\\) song song (hoặc trùng) với \\(l\\) cắt \\((P)\\) tại \\(M′\\). Quy tắc \\(M\\mapsto M′\\) là [[phép chiếu song song]] lên [[mặt phẳng chiếu]] \\((P)\\) theo [[phương chiếu]] \\(l\\); \\(M′\\) là hình chiếu song song của \\(M\\).'))
theory += GEO3D(FIG, cap=('Triangle \\(ABC\\) (yellow) and its image \\(A′B′C′\\) (green) on the plane \\(z=0\\); the dashed projecting lines \\(AA′, BB′, CC′\\) are all parallel to \\(l\\). Drag to rotate.', 'Tam giác \\(ABC\\) (vàng) và hình chiếu \\(A′B′C′\\) (xanh) trên mặt phẳng chiếu; các đường chiếu \\(AA′, BB′, CC′\\) (nét đứt) đều song song với \\(l\\). Kéo để xoay hình.'), alt=('A triangle and its parallel projection on a plane', ''), height=380)
theory += '<h3>14.2 %s</h3>' % TI('Properties', 'Tính chất')
theory += BOX('mint', ('For segments and lines not parallel to \\(l\\)', 'Với các đoạn thẳng, đường thẳng không song song với \\(l\\)'), UL([
  T('Three collinear points go to three collinear points, in the same order.', 'Ba điểm thẳng hàng biến thành ba điểm thẳng hàng và không làm thay đổi thứ tự.'),
  T('A line goes to a line, a ray to a ray, a segment to a segment.', 'Đường thẳng biến thành đường thẳng, tia thành tia, đoạn thẳng thành đoạn thẳng.'),
  T('Two parallel lines go to two parallel lines (or to the same line).', 'Hai đường thẳng song song biến thành hai đường thẳng song song hoặc trùng nhau.'),
  T('The ratio of two segments on one line or on two parallel lines is kept. In particular, a midpoint goes to a midpoint.', 'Tỉ số độ dài của hai đoạn thẳng nằm trên một đường thẳng hoặc trên hai đường thẳng song song được giữ nguyên. Đặc biệt, trung điểm biến thành trung điểm.')]))
theory += BOX('yellow', ('Not kept!', 'Không được giữ!'), T('Lengths, angles (even right angles) and the ratio of segments on <b>non-parallel</b> lines can change. A square may look like any parallelogram.', 'Độ dài, số đo góc (kể cả góc vuông) và tỉ số hai đoạn thẳng nằm trên hai đường thẳng <b>không song song</b> có thể thay đổi. Hình vuông có thể được vẽ thành một hình bình hành bất kì.'))
theory += '<h3>14.3 %s</h3>' % TI('Drawing solids', 'Hình biểu diễn của một hình không gian')
theory += TBL([TI('Real figure', 'Hình thật'), TI('Drawn as', 'Hình biểu diễn')], [
  [TI('any triangle (also right, isosceles, equilateral)', 'tam giác bất kì (cả vuông, cân, đều)'), TI('any triangle', 'một tam giác bất kì')],
  [TI('parallelogram, rectangle, rhombus, square', 'hình bình hành, chữ nhật, thoi, vuông'), TI('a parallelogram', 'một hình bình hành')],
  [TI('trapezoid with \\(AB=k\\,CD\\)', 'hình thang có \\(AB=k\\,CD\\)'), TI('a trapezoid with the same ratio \\(k\\) of the bases', 'một hình thang có tỉ số hai đáy bằng \\(k\\)')],
  [TI('circle', 'đường tròn'), TI('an ellipse (or a circle)', 'một đường elip (hoặc đường tròn)')],
  [TI('regular hexagon', 'lục giác đều'), TI('a hexagon whose opposite sides are parallel and equal', 'lục giác có các cạnh đối song song và bằng nhau')]])
theory += BOX('blue', ('How to draw', 'Cách vẽ'), T('Keep: parallel lines parallel, midpoints, ratios on one line. Hidden edges are dashed. Equal or perpendicular segments need not look equal or perpendicular.', 'Giữ: song song vẫn song song, trung điểm, tỉ số trên một đường thẳng. Cạnh khuất vẽ nét đứt. Các đoạn bằng nhau hay vuông góc không nhất thiết được vẽ bằng nhau hay vuông góc.'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Which picture is possible?', 'Hình nào có thể là hình chiếu?'), T('Can the image of a square \\(ABCD\\) (plane not parallel to \\(l\\)) be (a) a parallelogram that is not a rectangle; (b) a trapezoid with unequal bases; (c) a rectangle?', 'Hình chiếu song song của hình vuông \\(ABCD\\) (mặt phẳng chứa nó không song song với \\(l\\)) có thể là (a) hình bình hành không phải hình chữ nhật; (b) hình thang có hai đáy không bằng nhau; (c) hình chữ nhật không?'),
  T('\\(AB\\parallel CD\\), \\(AD\\parallel BC\\) and \\(AB=CD\\) must be kept.', 'Phải giữ \\(AB\\parallel CD\\), \\(AD\\parallel BC\\) và tỉ số \\(AB=CD\\) (hai đoạn song song).'),
  [T('Both pairs of opposite sides stay parallel, so the image is a parallelogram.', 'Hai cặp cạnh đối vẫn song song nên hình chiếu là hình bình hành.'), T('Angles can change: (a) and (c) are possible. (b) is impossible: equal parallel sides stay equal.', 'Góc có thể thay đổi: (a), (c) đều có thể. (b) không thể: hai đoạn song song bằng nhau vẫn bằng nhau.')],
  T('(a) yes; (b) no; (c) yes.', '(a) có; (b) không; (c) có.'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Shadow of a tree', 'Bóng của cái cây'), T('At the same moment, a vertical stick 1.5 m high casts a 2 m shadow on flat ground, and a vertical tree casts a 12 m shadow. How tall is the tree?', 'Cùng một thời điểm, chiếc cọc thẳng đứng cao 1,5 m có bóng dài 2 m trên mặt đất phẳng; một cái cây thẳng đứng có bóng dài 12 m. Cây cao bao nhiêu?'),
  T('Sunlight is a parallel projection; the stick and the tree are parallel, and so are their shadows.', 'Ánh nắng là phép chiếu song song; cọc và cây song song với nhau, bóng của chúng cũng song song.'),
  [T('The ratio height : shadow is the same: \\(\\dfrac{h}{12}=\\dfrac{1.5}{2}\\).', 'Tỉ số chiều cao : bóng như nhau: \\(\\dfrac{h}{12}=\\dfrac{1{,}5}{2}\\).')], T('\\(h=9\\) m.', '\\(h=9\\) m.'))
assert F(3, 2) / 2 * 12 == 9
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Ratio on a segment', 'Tỉ số trên một đoạn thẳng'), T('\\(M\\) lies on segment \\(AB\\) with \\(AM:MB=1:2\\). Under a parallel projection the image \\(A′B′\\) has length 9. Find \\(A′M′\\). Is \\(M′\\) between \\(A′\\) and \\(B′\\)?', 'Điểm \\(M\\) thuộc đoạn \\(AB\\) với \\(AM:MB=1:2\\). Qua một phép chiếu song song, \\(A′B′=9\\). Tính \\(A′M′\\). \\(M′\\) có nằm giữa \\(A′\\) và \\(B′\\) không?'),
  T('Ratios and order on one line are kept.', 'Tỉ số và thứ tự trên một đường thẳng được giữ nguyên.'),
  [T('\\(\\dfrac{A′M′}{A′B′}=\\dfrac{AM}{AB}=\\dfrac13\\).', '\\(\\dfrac{A′M′}{A′B′}=\\dfrac{AM}{AB}=\\dfrac13\\).'), T('Order is kept, so \\(M′\\) is between \\(A′\\) and \\(B′\\).', 'Thứ tự được giữ nên \\(M′\\) nằm giữa \\(A′\\) và \\(B′\\).')],
  T('\\(A′M′=3\\); yes.', '\\(A′M′=3\\); có.'))
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('A trapezoid and its centre lines', 'Hình thang và trung điểm'), T('\\(ABCD\\) is a trapezoid with \\(AB\\parallel CD\\), \\(AB=2CD\\). \\(I\\) is the midpoint of \\(AB\\). In the drawing \\(A′B′C′D′\\), \\(C′D′=3\\) cm. Find \\(A′B′\\) and show that \\(I′\\) is the midpoint of \\(A′B′\\) and \\(A′I′C′D′\\) is a parallelogram.', 'Hình thang \\(ABCD\\) có \\(AB\\parallel CD\\), \\(AB=2CD\\), \\(I\\) là trung điểm \\(AB\\). Trên hình biểu diễn \\(A′B′C′D′\\) có \\(C′D′=3\\) cm. Tính \\(A′B′\\); chứng tỏ \\(I′\\) là trung điểm \\(A′B′\\) và \\(A′I′C′D′\\) là hình bình hành.'),
  T('\\(AB\\parallel CD\\): their ratio is kept. Midpoints go to midpoints.', '\\(AB\\parallel CD\\): tỉ số được giữ. Trung điểm biến thành trung điểm.'),
  [T('\\(A′B′=2C′D′=6\\) cm; \\(I′\\) is the midpoint of \\(A′B′\\).', '\\(A′B′=2C′D′=6\\) cm; \\(I′\\) là trung điểm \\(A′B′\\).'), T('\\(AI\\parallel DC\\) and \\(AI=DC\\): \\(AICD\\) is a parallelogram, so its image \\(A′I′C′D′\\) is a parallelogram too.', '\\(AI\\parallel DC\\), \\(AI=DC\\): \\(AICD\\) là hình bình hành nên hình chiếu \\(A′I′C′D′\\) cũng là hình bình hành.')],
  T('\\(A′B′=6\\) cm.', '\\(A′B′=6\\) cm.'))
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Drawing an equilateral triangle and its centre', 'Vẽ tam giác đều và tâm của nó'), T('Explain how to draw an equilateral triangle \\(ABC\\), its centre \\(O\\) and the altitude \\(AH\\). Does the drawn altitude look perpendicular to \\(B′C′\\)?', 'Nêu cách vẽ hình biểu diễn của tam giác đều \\(ABC\\), tâm \\(O\\) và đường cao \\(AH\\). Đường cao vẽ ra có trông vuông góc với \\(B′C′\\) không?'),
  T('In an equilateral triangle, the altitude is also a median, and \\(O\\) is the centroid. Use only kept properties.', 'Trong tam giác đều, đường cao cũng là trung tuyến, \\(O\\) là trọng tâm. Chỉ dùng các tính chất được giữ.'),
  [T('Draw any triangle \\(A′B′C′\\). \\(H\\) is the midpoint of \\(BC\\): draw \\(H′\\) the midpoint of \\(B′C′\\).', 'Vẽ một tam giác bất kì \\(A′B′C′\\). \\(H\\) là trung điểm \\(BC\\): vẽ \\(H′\\) là trung điểm \\(B′C′\\).'), T('\\(O\\) divides \\(AH\\) with \\(AO=\\dfrac23AH\\): mark \\(O′\\) on \\(A′H′\\) with \\(A′O′=\\dfrac23A′H′\\).', '\\(O\\) chia \\(AH\\) với \\(AO=\\dfrac23AH\\): lấy \\(O′\\) trên \\(A′H′\\) sao cho \\(A′O′=\\dfrac23A′H′\\).')],
  T('\\(A′H′\\) is a median of \\(A′B′C′\\); in general it is <b>not</b> drawn perpendicular to \\(B′C′\\), because right angles are not kept.', '\\(A′H′\\) là trung tuyến của \\(A′B′C′\\); nói chung nó <b>không</b> được vẽ vuông góc với \\(B′C′\\) vì góc vuông không được bảo toàn.'))

PRS = [(True, 'A parallel projection keeps the midpoint of a segment.', 'Phép chiếu song song biến trung điểm của đoạn thẳng thành trung điểm của hình chiếu.'),
       (False, 'A parallel projection keeps the length of every segment.', 'Phép chiếu song song giữ nguyên độ dài mọi đoạn thẳng.'),
       (False, 'A parallel projection keeps right angles.', 'Phép chiếu song song biến góc vuông thành góc vuông.'),
       (True, 'Two parallel lines (not parallel to \\(l\\)) have parallel or equal images.', 'Hai đường thẳng song song (không song song với \\(l\\)) có hình chiếu song song hoặc trùng nhau.')]
SHP = [(True, 'The image of a square can be a rectangle that is not a square.', 'Hình chiếu song song của hình vuông có thể là hình chữ nhật không phải hình vuông.'),
       (False, 'The image of a parallelogram can be a trapezoid with unequal bases.', 'Hình chiếu song song của hình bình hành có thể là hình thang có hai đáy không bằng nhau.'),
       (True, 'The image of a circle (in a plane not parallel to \\(l\\)) can be an ellipse.', 'Hình chiếu song song của đường tròn (mặt phẳng chứa nó không song song với \\(l\\)) có thể là đường elip.')]
def lvl(P):
    (p, q), L = P['rat']; x = F(p * L, p + q)
    o1 = M4(1, '\\(M\\) is on segment \\(AB\\) with \\(AM:MB=%d:%d\\). The image of \\(AB\\) under a parallel projection has length \\(A′B′=%d\\). Then \\(A′M′=\\)…' % (p, q, L), 'Điểm \\(M\\) thuộc đoạn \\(AB\\), \\(AM:MB=%d:%d\\). Hình chiếu song song của \\(AB\\) có độ dài \\(A′B′=%d\\). Khi đó \\(A′M′=\\)…' % (p, q, L),
            fr(x), [fr(F(q * L, p + q)), fr(F(p * L, q)), fr(F(L, 2)) if x != F(L, 2) else fr(F(L, 3)), fr(x + 1), str(L)], '\\(\\dfrac{A′M′}{A′B′}=\\dfrac{AM}{AB}=\\dfrac{%d}{%d}\\).' % (p, p + q), '\\(\\dfrac{A′M′}{A′B′}=\\dfrac{AM}{AB}=\\dfrac{%d}{%d}\\).' % (p, p + q))
    (h1, s1), s2 = P['sh']; h2 = F(h1) * F(s2) / F(s1)
    o2 = M4(2, 'A vertical post \\(%s\\) m high casts a \\(%s\\) m shadow on flat ground. At the same time a vertical tower casts a \\(%s\\) m shadow. The tower is…' % (S.fd(h1, False), S.fd(s1, False), S.fd(s2, False)),
            'Một cột mốc thẳng đứng cao \\(%s\\) m có bóng dài \\(%s\\) m trên mặt đất phẳng. Cùng lúc đó, một tòa tháp thẳng đứng có bóng dài \\(%s\\) m. Tháp cao…' % (S.fd(h1), S.fd(s1), S.fd(s2)),
            '%s\\ \\text{m}' % S.fd(h2), ['%s\\ \\text{m}' % S.fd(v) for v in (F(s2) * F(s1) / F(h1), F(s2) - F(s1) + F(h1), F(s2), h2 + 2)],
            '\\(\\dfrac{h}{%s}=\\dfrac{%s}{%s}\\Rightarrow h=%s\\).' % (S.fd(s2, False), S.fd(h1, False), S.fd(s1, False), S.fd(h2, False)), '\\(\\dfrac{h}{%s}=\\dfrac{%s}{%s}\\Rightarrow h=%s\\).' % (S.fd(s2), S.fd(h1), S.fd(s1), S.fd(h2)))
    k, c3 = P['trap']; y = F(k) * c3
    o3 = M4(3, 'Trapezoid \\(ABCD\\): \\(AB\\parallel CD\\), \\(AB=%s\\,CD\\). In its drawing \\(A′B′C′D′\\), \\(C′D′=%d\\) cm. Then \\(A′B′=\\)…' % (fr(k), c3), 'Hình thang \\(ABCD\\): \\(AB\\parallel CD\\), \\(AB=%s\\,CD\\). Trên hình biểu diễn \\(A′B′C′D′\\) có \\(C′D′=%d\\) cm. Khi đó \\(A′B′=\\)…' % (fr(k), c3),
            '%s\\ \\text{cm}' % fr(y), ['%s\\ \\text{cm}' % fr(v) for v in (F(c3), F(c3) / F(k), y + c3, y + 1)], 'Parallel segments keep their ratio: \\(A′B′=%s\\cdot%d=%s\\).' % (fr(k), c3, fr(y)), 'Hai đoạn song song giữ nguyên tỉ số: \\(A′B′=%s\\cdot%d=%s\\).' % (fr(k), c3, fr(y)))
    e4 = PRS[P['t4']]; t4 = tf(4, e4[1], e4[2], e4[0], 'Kept: collinearity, order, parallelism, ratios on parallel lines (so midpoints). Not kept: lengths, angles.', 'Được giữ: thẳng hàng, thứ tự, song song, tỉ số trên các đường thẳng song song (nên giữ trung điểm). Không giữ: độ dài, góc.')
    e5 = SHP[P['t5']]; t5 = tf(5, e5[1], e5[2], e5[0], 'A parallelogram always goes to a parallelogram; angles may change; a circle usually goes to an ellipse.', 'Hình bình hành luôn biến thành hình bình hành; góc có thể đổi; đường tròn thường biến thành đường elip.')
    (a, b), c = P['poles']; v = F(c) * F(a) / F(b); assert (10 * v).denominator == 1
    s6 = sh(6, 'Two vertical poles stand on flat ground. The first is \\(%s\\) m high with a \\(%s\\) m shadow. The second has a \\(%s\\) m shadow at the same moment. How tall is the second pole (m)?' % (S.fd(a, False), S.fd(b, False), S.fd(c, False)), 'Hai cột thẳng đứng trên mặt đất phẳng. Cột thứ nhất cao \\(%s\\) m, bóng dài \\(%s\\) m. Cùng lúc đó, cột thứ hai có bóng dài \\(%s\\) m. Cột thứ hai cao bao nhiêu mét?' % (S.fd(a), S.fd(b), S.fd(c)),
            S.fd(F(c) * F(a) / F(b), False), 'Same ratio height : shadow: \\(h=%s\\cdot\\dfrac{%s}{%s}=%s\\).' % (S.fd(c, False), S.fd(a, False), S.fd(b, False), S.fd(F(c) * F(a) / F(b), False)), 'Cùng tỉ số chiều cao : bóng: \\(h=%s\\cdot\\dfrac{%s}{%s}=%s\\).' % (S.fd(c), S.fd(a), S.fd(b), S.fd(F(c) * F(a) / F(b))))
    (p7, q7), am = P['rat2']; ab = F(am) * (p7 + q7) / p7; assert ab.denominator == 1
    s7 = sh(7, '\\(M\\) is on segment \\(AB\\) with \\(AM:MB=%d:%d\\). Under a parallel projection, \\(A′M′=%d\\). Find \\(A′B′\\).' % (p7, q7, am), 'Điểm \\(M\\) thuộc đoạn \\(AB\\), \\(AM:MB=%d:%d\\). Qua một phép chiếu song song, \\(A′M′=%d\\). Tính \\(A′B′\\).' % (p7, q7, am), ab.numerator,
            '\\(A′B′=A′M′\\cdot\\dfrac{%d}{%d}=%d\\).' % (p7 + q7, p7, ab), '\\(A′B′=A′M′\\cdot\\dfrac{%d}{%d}=%d\\).' % (p7 + q7, p7, ab))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
PP = [dict(rat=((1, 2), 12), sh=((2, F(5, 2)), 30), trap=(2, 4), t4=0, t5=0, poles=((F(3, 2), 2), 10), rat2=((1, 3), 5)),
      dict(rat=((2, 3), 20), sh=((F(16, 10), 2), 25), trap=(3, 5), t4=1, t5=1, poles=((F(18, 10), F(24, 10)), 14), rat2=((2, 3), 8)),
      dict(rat=((3, 1), 16), sh=((F(12, 10), F(15, 10)), 40), trap=(F(3, 2), 6), t4=2, t5=2, poles=((2, 5), 18), rat2=((3, 4), 9))]
practice = three(lvl, PP)
practice = with_self(practice, S.M14S11, start=8)
mistakes = [('<b>Keeping lengths.</b> Only ratios on one line or on parallel lines are kept, not lengths.', '<b>Giữ độ dài.</b> Chỉ tỉ số trên một đường thẳng hoặc trên các đường thẳng song song được giữ, độ dài thì không.'),
            ('<b>Drawing right angles.</b> A right angle may be drawn acute or obtuse; a drawing of a solid does not have to keep right angles.', '<b>Cố vẽ góc vuông.</b> Góc vuông có thể được vẽ thành góc nhọn hay góc tù; hình biểu diễn không bắt buộc giữ góc vuông.'),
            ('<b>Ratio of non-parallel segments.</b> \\(\\dfrac{AB}{AC}\\) for non-parallel \\(AB\\), \\(AC\\) can change.', '<b>Tỉ số hai đoạn không song song.</b> \\(\\dfrac{AB}{AC}\\) với \\(AB\\), \\(AC\\) không song song có thể thay đổi.'),
            ('<b>Shadow ratios.</b> Compare height with shadow of objects at the <b>same moment</b>, both vertical.', '<b>Tỉ số bóng.</b> Chỉ so sánh chiều cao với bóng của các vật cùng thẳng đứng, ở <b>cùng một thời điểm</b>.')]
summary = [('Parallel projection onto \\((P)\\) along \\(l\\): \\(M′\\) is where the line through \\(M\\) parallel to \\(l\\) meets \\((P)\\).', 'Phép chiếu song song lên \\((P)\\) theo phương \\(l\\): \\(M′\\) là giao của đường thẳng qua \\(M\\) song song với \\(l\\) và \\((P)\\).'),
           ('Kept: collinearity and order, parallelism, ratios on one line or parallel lines (midpoints, centroids).', 'Được giữ: thẳng hàng và thứ tự, song song, tỉ số trên một đường thẳng hoặc trên các đường thẳng song song (trung điểm, trọng tâm).'),
           ('Not kept: lengths, angles. Square → parallelogram; circle → ellipse.', 'Không giữ: độ dài, góc. Hình vuông → hình bình hành; đường tròn → elip.'),
           ('Sunlight is a parallel projection. Key words: projection, image, direction, shadow.', 'Ánh nắng là một phép chiếu song song. Từ cần nhớ: projection, image, direction, shadow.')]
checks = [('I can find the image of a point under a parallel projection.', 'Em xác định được hình chiếu song song của một điểm.'), ('I know what a parallel projection keeps and changes.', 'Em biết phép chiếu song song giữ và làm thay đổi những gì.'),
          ('I can draw a correct picture of a figure in space.', 'Em vẽ đúng hình biểu diễn của một hình trong không gian.'), ('I can solve shadow problems.', 'Em giải được bài toán về bóng của vật.')]
LL('g11-space-08', 'Parallel Projection', CV, ('Parallelism in Space', 'Quan hệ song song trong không gian'), 'lines-and-planes-in-space', 'parallel-projection', 150, 'Intermediate', 60, ('parallel lines and planes, Thales\' theorem', 'đường thẳng và mặt phẳng song song, định lí Thalès'),
   'Parallel projection: definition, properties, drawing solids and shadows in sunlight.', 'Bài 14 – Phép chiếu song song: định nghĩa, tính chất, hình biểu diễn của hình không gian, bóng dưới ánh nắng.',
   ['parallel projection', 'image', 'representation', 'shadow'], ['phép chiếu song song', 'hình chiếu', 'hình biểu diễn', 'bóng'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g11-space-07'])
