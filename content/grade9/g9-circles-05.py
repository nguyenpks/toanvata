# -*- coding: utf-8 -*-
"""Nội dung bài g9-circles-05 = Toán 9 KNTT, Bài 17: Vị trí tương đối của hai đường tròn – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 5 – Lesson 17."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9

LID = 'g9-circles-05'
CH = 'Đường tròn'
TOPIC = ('Circles', CH)
ensure_vocab([
 ('g9-dist-centers', 'distance between the centers', 'đoạn nối tâm', CH, 'Let d be the distance between the centers.', r'\(d=OO^{\prime}\)'),
 ('g9-intersecting-circles', 'intersecting circles', 'hai đường tròn cắt nhau', CH, 'Intersecting circles have two common points.', ''),
 ('g9-ext-tangent', 'externally tangent', 'tiếp xúc ngoài', CH, 'If d = R + r, the circles are externally tangent.', ''),
 ('g9-int-tangent', 'internally tangent', 'tiếp xúc trong', CH, 'If d = R − r, the circles are internally tangent.', ''),
 ('g9-disjoint-circles', 'outside each other', 'ở ngoài nhau', CH, 'If d > R + r, the circles lie outside each other.', ''),
 ('g9-nested', 'one inside the other', 'đựng nhau', CH, 'If d < R − r, one circle lies inside the other.', ''),
 ('g9-common-chord', 'common chord', 'dây chung', CH, 'The line of centers is the perpendicular bisector of the common chord.', ''),
 ('g9-collinear', 'collinear', 'thẳng hàng', CH, 'The two centers and the point of tangency are collinear.', ''),
])
load_vocab()

# ---------- kiểm tra số liệu ----------
assert [sp_g9.cpos(7, 3, d) for d in (12, 10, 6, 4, 2)] == ['out', 'ext', 'inter', 'int', 'in']
assert sp_g9.cpos(6, 4, 8) == 'inter' and 10 - 8 == 2 and 8 - 2 == 6
assert 13 - 8 == 5 and 13 + 8 == 21
x = (14 ** 2 + 15 ** 2 - 13 ** 2) / 28; assert x == 9 and math.sqrt(15 ** 2 - 81) == 12
for k in (1, 15): assert sp_g9.cpos(k + 2, 7, 10) in ('ext', 'int')
assert sp_g9.cpos(2 + 2, 7, 10) == 'inter' and sp_g9.cpos(0.5 + 2, 7, 10) == 'out' and sp_g9.cpos(16 + 2, 7, 10) == 'in'

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 75 minutes', '75 phút'), before=('Lesson 16: a line and a circle', 'Bài 16: vị trí tương đối của đường thẳng và đường tròn'))
goals = [
 (r'name the five relative positions of two circles;', r'nhận biết được các vị trí tương đối của hai đường tròn;'),
 (r'decide the position by comparing \(d\) with \(R+r\) and \(R-r\);', r'xác định được vị trí tương đối nhờ so sánh \(d\) với \(R+r\) và \(R-r\);'),
 (r'find a radius or a distance for given tangency;', r'tìm được bán kính hoặc khoảng cách để hai đường tròn tiếp xúc;'),
 (r'solve real-life problems (fountains, gears, flower beds).', r'giải được bài toán thực tế (đài phun nước, bánh răng, bồn hoa).')]
vocab = [
 (r'<b>distance between the centers</b> – \(d=OO^{\prime}\).', r'[[Đoạn nối tâm]] – \(d=OO^{\prime}\).'),
 (r'<b>intersecting circles</b> – two common points; <b>common chord</b> \(AB\).', r'[[Hai đường tròn cắt nhau]] – có hai điểm chung; [[dây chung]] \(AB\).'),
 (r'<b>externally / internally tangent</b> – one common point, \(d=R+r\) / \(d=R-r\).', r'[[Tiếp xúc ngoài]] / [[tiếp xúc trong]] – một điểm chung, \(d=R+r\) / \(d=R-r\).'),
 (r'<b>outside each other / one inside the other</b> – no common point.', r'[[Ở ngoài nhau]] / [[đựng nhau]] – không có điểm chung.'),
 (r'<b>collinear</b> – on one straight line (the centers and the point of tangency).', r'[[Thẳng hàng]] – cùng nằm trên một đường thẳng (hai tâm và tiếp điểm).')]
phrases = [
 (r'<b>Let \(d\) be the distance between their centers.</b>', r'Gọi \(d\) là khoảng cách giữa hai tâm.'),
 (r'<b>Compare \(d\) with \(R+r\) and \(R-r\) before drawing a conclusion.</b>', r'So sánh \(d\) với \(R+r\) và \(R-r\) trước khi kết luận.'),
 (r'<b>Since \(R-r\lt d\lt R+r\), the circles intersect at two points.</b>', r'Vì \(R-r\lt d\lt R+r\) nên hai đường tròn cắt nhau tại hai điểm.'),
 (r'<b>The two centers and the point of tangency are collinear.</b>', r'Hai tâm và tiếp điểm thẳng hàng.'),
 (r'<b>The line of centers is perpendicular to the common chord.</b>', r'Đường nối tâm vuông góc với dây chung.')]
review = (T(r'<b>Lesson 16.</b> A line and a circle: compare \(d\) with \(R\).', r'<b>Bài 16.</b> Đường thẳng và đường tròn: so sánh \(d\) với \(R\).') +
          T(r'<b>Perpendicular bisector.</b> Points equidistant from \(A\) and \(B\) lie on the perpendicular bisector of \(AB\).', r'<b>Đường trung trực.</b> Điểm cách đều \(A\) và \(B\) thì nằm trên đường trung trực của \(AB\).'))

G = lambda cfg, en, vi, hgt=260: GEO(sp_g9.auto_labels(cfg), cap=(en, vi), alt=(en, ''), height=hgt)
def pt(i, x, y, name=None, size=3): return {'type': 'point', 'id': i, 'at': [round(x, 4), round(y, 4)], 'name': i if name is None else name, 'style': {'size': size}}
def seg(a, b, **st): return {'type': 'segment', 'through': [a, b], 'style': st}
R1, r1, d1 = 2.5, 1.8, 3.0; xm = (d1 * d1 + R1 * R1 - r1 * r1) / (2 * d1); ym = math.sqrt(R1 * R1 - xm * xm)
FIG1 = G({'view': [-2.9, 5.2, -2.8, 2.8], 'steps': [pt('O', 0, 0), pt('O1', d1, 0, name="O'"), pt('A', xm, ym), pt('B', xm, -ym), dict(pt('M', xm, 0, size=2), off=[-8, -10]),
          {'type': 'circle', 'center': 'O', 'radius': R1}, {'type': 'circle', 'center': 'O1', 'radius': r1}, seg('O', 'O1', dash=True), seg('A', 'B'), {'type': 'angle', 'points': ['O1', 'M', 'A']}]},
         "Intersecting circles: OO' is perpendicular to the common chord AB at its midpoint M.", "Hai đường tròn cắt nhau: OO' vuông góc với dây chung AB tại trung điểm M.")
FIG2 = G({'view': [-1.9, 9.4, -2.1, 2.1], 'steps': [pt('O', 0, 0), pt('O1', 2.5, 0, name="O'"), pt('T', 1.5, 0), {'type': 'circle', 'center': 'O', 'radius': 1.5}, {'type': 'circle', 'center': 'O1', 'radius': 1.0},
          pt('I', 6.4, 0), pt('I1', 7.2, 0, name="I'"), pt('K', 8.2, 0), {'type': 'circle', 'center': 'I', 'radius': 1.8}, {'type': 'circle', 'center': 'I1', 'radius': 1.0},
          seg('O', 'O1', dash=True), seg('I', 'K', dash=True)]},
         "Left: externally tangent at T (OO' = R + r). Right: internally tangent at K (II' = R − r). The centers and the point of tangency are collinear.",
         "Trái: tiếp xúc ngoài tại T (OO' = R + r). Phải: tiếp xúc trong tại K (II' = R − r). Hai tâm và tiếp điểm thẳng hàng.", 270)

theory = '<h3>5.1 %s</h3>' % TI('Five relative positions', 'Các vị trí tương đối của hai đường tròn')
theory += T(r'Let \((O;\,R)\) and \((O^{\prime};\,r)\) with \(R\ge r\), and \(d=OO^{\prime}\).', r'Cho hai đường tròn \((O;\,R)\) và \((O^{\prime};\,r)\) với \(R\ge r\), \(d=OO^{\prime}\).')
theory += TABLE([('Position', 'Vị trí tương đối'), ('Common points', 'Số điểm chung'), ('Relation', 'Hệ thức')],
  [[TI('intersecting', 'cắt nhau'), '2', '\\(R-r\\lt d\\lt R+r\\)'],
   [TI('externally tangent', 'tiếp xúc ngoài'), '1', '\\(d=R+r\\)'],
   [TI('internally tangent', 'tiếp xúc trong'), '1', '\\(d=R-r\\gt0\\)'],
   [TI('outside each other', 'ở ngoài nhau'), '0', '\\(d\\gt R+r\\)'],
   [TI('one inside the other', 'đựng nhau'), '0', '\\(d\\lt R-r\\) (\\(d=0\\): concentric)' if False else '\\(d\\lt R-r\\)']])
theory += T(r'Concentric circles (\(d=0\)) are a special case of “one inside the other”.', r'Hai đường tròn đồng tâm (\(d=0\)) là trường hợp đặc biệt của hai đường tròn đựng nhau.')
theory += '<h3>5.2 %s</h3>' % TI('Line of centers', 'Tính chất đường nối tâm')
theory += FIG1
theory += BOX('blue', ('Properties', 'Tính chất'),
  T(r'If two circles intersect at \(A\), \(B\), the line of centers \(OO^{\prime}\) is the perpendicular bisector of the common chord \(AB\) (because \(OA=OB\) and \(O^{\prime}A=O^{\prime}B\)).', r'Nếu hai đường tròn cắt nhau tại \(A\), \(B\) thì đường nối tâm \(OO^{\prime}\) là đường trung trực của [[dây chung]] \(AB\) (vì \(OA=OB\), \(O^{\prime}A=O^{\prime}B\)).'),
  T(r'If two circles are tangent at \(T\), then \(O\), \(O^{\prime}\), \(T\) are collinear.', r'Nếu hai đường tròn tiếp xúc nhau tại \(T\) thì \(O\), \(O^{\prime}\), \(T\) [[thẳng hàng]].'))
theory += FIG2
theory += BOX('yellow', ('Strategy', 'Cách làm'), T(r'Compute \(R+r\) and \(R-r\) first, then place \(d\) relative to these two numbers.', r'Tính \(R+r\) và \(R-r\) trước, rồi xem \(d\) nằm ở đâu so với hai số đó.'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Five cases', 'Năm trường hợp'),
  T(r'Two circles have radii 7 cm and 3 cm. Give their relative position and the number of common points when \(d\) is a) 12 cm; b) 10 cm; c) 6 cm; d) 4 cm; e) 2 cm.', r'Hai đường tròn có bán kính 7 cm và 3 cm. Nêu vị trí tương đối và số điểm chung khi \(d\) bằng a) 12 cm; b) 10 cm; c) 6 cm; d) 4 cm; e) 2 cm.'),
  ('\\(R+r=10\\), \\(R-r=4\\).', '\\(R+r=10\\), \\(R-r=4\\).'),
  [T(r'a) \(12\gt10\): outside each other, 0 points. b) \(d=10\): externally tangent, 1 point.', r'a) \(12\gt10\): ở ngoài nhau, 0 điểm chung. b) \(d=10\): tiếp xúc ngoài, 1 điểm chung.'),
   T(r'c) \(4\lt6\lt10\): intersecting, 2 points. d) \(d=4\): internally tangent, 1 point. e) \(2\lt4\): one inside the other, 0 points.', r'c) \(4\lt6\lt10\): cắt nhau, 2 điểm chung. d) \(d=4\): tiếp xúc trong, 1 điểm chung. e) \(2\lt4\): đựng nhau, 0 điểm chung.')],
  T(r'0; 1; 2; 1; 0 common points.', r'Lần lượt 0; 1; 2; 1; 0 điểm chung.'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Two circular fountains', 'Hai đài phun nước'),
  T(r'Two circular fountains have radii 6 m and 4 m; their centers \(A\), \(B\) are 8 m apart. a) Give the relative position. b) How far must the smaller fountain move directly away from \(A\) to be externally tangent? c) From the original position, how far must it move directly towards \(A\) to be internally tangent?', r'Hai đài phun nước hình tròn có bán kính 6 m và 4 m, hai tâm \(A\), \(B\) cách nhau 8 m. a) Nêu vị trí tương đối. b) Phải dời đài nhỏ thẳng ra xa \(A\) bao nhiêu mét để hai đường tròn tiếp xúc ngoài? c) Từ vị trí ban đầu, phải dời đài nhỏ thẳng về phía \(A\) bao nhiêu mét để tiếp xúc trong?'),
  ('\\(R+r=10\\), \\(R-r=2\\).', '\\(R+r=10\\), \\(R-r=2\\).'),
  [T(r'a) \(2\lt8\lt10\): the circles intersect at two points.', r'a) \(2\lt8\lt10\): hai đường tròn cắt nhau tại hai điểm.'),
   T(r'b) External tangency needs \(d=10\): move \(10-8=2\) m. c) Internal tangency needs \(d=2\): move \(8-2=6\) m.', r'b) Tiếp xúc ngoài khi \(d=10\): dời \(10-8=2\) m. c) Tiếp xúc trong khi \(d=2\): dời \(8-2=6\) m.')],
  T(r'Intersecting; 2 m; 6 m.', r'Cắt nhau; 2 m; 6 m.'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('An unknown radius', 'Tìm bán kính'),
  T(r'Circle \(C_1\) has radius 8 cm, circle \(C_2\) has radius \(r\) cm, and the centers are 13 cm apart. Find \(r\) if the circles are a) externally tangent; b) internally tangent. c) For which \(r\) do they intersect?', r'Đường tròn \(C_1\) bán kính 8 cm, đường tròn \(C_2\) bán kính \(r\) cm, hai tâm cách nhau 13 cm. Tìm \(r\) để hai đường tròn a) tiếp xúc ngoài; b) tiếp xúc trong. c) Với \(r\) nào thì chúng cắt nhau?'),
  ('Internal tangency: \\(|8-r|=13\\).', 'Tiếp xúc trong: \\(|8-r|=13\\).'),
  [T(r'a) \(8+r=13\Rightarrow r=5\). b) \(|8-r|=13\Rightarrow r=21\) (\(r=-5\) is rejected).', r'a) \(8+r=13\Rightarrow r=5\). b) \(|8-r|=13\Rightarrow r=21\) (loại \(r=-5\)).'),
   T(r'c) \(|8-r|\lt13\lt8+r\Leftrightarrow 5\lt r\lt21\).', r'c) \(|8-r|\lt13\lt8+r\Leftrightarrow 5\lt r\lt21\).')],
  T(r'5 cm; 21 cm; \(5\lt r\lt21\).', r'5 cm; 21 cm; \(5\lt r\lt21\).'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Common chord', 'Dây chung'),
  T(r'\((O;\,15\text{ cm})\) and \((O^{\prime};\,13\text{ cm})\) intersect at \(A\), \(B\) and \(OO^{\prime}=14\) cm. Find the common chord \(AB\).', r'\((O;\,15\text{ cm})\) và \((O^{\prime};\,13\text{ cm})\) cắt nhau tại \(A\), \(B\), \(OO^{\prime}=14\) cm. Tính độ dài dây chung \(AB\).'),
  ('Let \\(M\\) be the midpoint of \\(AB\\) and \\(OM=x\\).', 'Gọi \\(M\\) là trung điểm \\(AB\\), \\(OM=x\\).'),
  [T(r'\(OO^{\prime}\perp AB\) at \(M\). \(AM^2=15^2-x^2=13^2-(14-x)^2\Rightarrow 225-x^2=169-196+28x-x^2\Rightarrow x=9\).', r'\(OO^{\prime}\perp AB\) tại \(M\). \(AM^2=15^2-x^2=13^2-(14-x)^2\Rightarrow 225-x^2=169-196+28x-x^2\Rightarrow x=9\).'),
   T(r'\(AM=\sqrt{225-81}=12\), so \(AB=24\) cm.', r'\(AM=\sqrt{225-81}=12\) nên \(AB=24\) cm.')],
  T(r'\(AB=24\) cm.', r'\(AB=24\) cm.'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('A parameter', 'Bài toán có tham số'),
  T(r'Two circles have radii \(k+2\) and 7 (\(k\gt0\)); their centers are 10 units apart. Find all \(k\) for which they a) are tangent; b) intersect; c) have no common point.', r'Hai đường tròn có bán kính \(k+2\) và 7 (\(k\gt0\)), hai tâm cách nhau 10 đơn vị. Tìm mọi \(k\) để chúng a) tiếp xúc nhau; b) cắt nhau; c) không có điểm chung.'),
  ('\\(R+r=k+9\\), \\(|R-r|=|k-5|\\).', '\\(R+r=k+9\\), \\(|R-r|=|k-5|\\).'),
  [T(r'a) External: \(k+9=10\Rightarrow k=1\). Internal: \(|k-5|=10\Rightarrow k=15\).', r'a) Tiếp xúc ngoài: \(k+9=10\Rightarrow k=1\). Tiếp xúc trong: \(|k-5|=10\Rightarrow k=15\).'),
   T(r'b) \(|k-5|\lt10\lt k+9\Leftrightarrow 1\lt k\lt15\). c) \(0\lt k\lt1\) (outside each other) or \(k\gt15\) (one inside the other).', r'b) \(|k-5|\lt10\lt k+9\Leftrightarrow 1\lt k\lt15\). c) \(0\lt k\lt1\) (ở ngoài nhau) hoặc \(k\gt15\) (đựng nhau).')],
  T(r'a) \(k=1\) or \(k=15\); b) \(1\lt k\lt15\); c) \(0\lt k\lt1\) or \(k\gt15\).', r'a) \(k=1\) hoặc \(k=15\); b) \(1\lt k\lt15\); c) \(0\lt k\lt1\) hoặc \(k\gt15\).'))

_SETS = sp_g9.BANK(sp_g9.L17_GROUPS, start=1, seeds=(2701, 2702, 2703))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Comparing \(d\) with only one number.</b> Always compare with both \(R+r\) and \(R-r\).', r'<b>Chỉ so sánh \(d\) với một số.</b> Luôn so sánh với cả \(R+r\) và \(R-r\).'),
 (r'<b>Mixing up external and internal tangency.</b> External: \(d=R+r\); internal: \(d=R-r\).', r'<b>Nhầm tiếp xúc ngoài và tiếp xúc trong.</b> Ngoài: \(d=R+r\); trong: \(d=R-r\).'),
 (r'<b>Forgetting the second value.</b> \(|R-r|=d\) can give two radii; reject only negative ones.', r'<b>Bỏ sót nghiệm.</b> \(|R-r|=d\) có thể cho hai giá trị bán kính; chỉ loại giá trị âm.'),
 (r'<b>“No common point” is not one case.</b> It can be “outside each other” or “one inside the other”.', r'<b>“Không có điểm chung” gồm hai trường hợp.</b> Ở ngoài nhau hoặc đựng nhau.')]
summary = [
 (r'Intersecting: \(R-r\lt d\lt R+r\); externally tangent: \(d=R+r\); internally tangent: \(d=R-r\).', r'Cắt nhau: \(R-r\lt d\lt R+r\); tiếp xúc ngoài: \(d=R+r\); tiếp xúc trong: \(d=R-r\).'),
 (r'Outside each other: \(d\gt R+r\); one inside the other: \(d\lt R-r\).', r'Ở ngoài nhau: \(d\gt R+r\); đựng nhau: \(d\lt R-r\).'),
 (r'The line of centers is the perpendicular bisector of the common chord; tangent circles: centers and point of tangency are collinear.', r'Đường nối tâm là trung trực của dây chung; hai đường tròn tiếp xúc: hai tâm và tiếp điểm thẳng hàng.'),
 (r'Key English: distance between the centers, intersecting, externally / internally tangent, outside each other, one inside the other, common chord, collinear.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[đoạn nối tâm]], [[hai đường tròn cắt nhau]], [[tiếp xúc ngoài]], [[tiếp xúc trong]], [[ở ngoài nhau]], [[đựng nhau]], [[dây chung]], [[thẳng hàng]].')]
checks = [
 (r'I can name the relative positions of two circles.', r'Em nêu được các vị trí tương đối của hai đường tròn.'),
 (r'I can decide the position from \(d\), \(R\), \(r\).', r'Em xác định được vị trí tương đối qua \(d\), \(R\), \(r\).'),
 (r'I can find a radius or a distance for tangency.', r'Em tìm được bán kính hoặc khoảng cách để hai đường tròn tiếp xúc.'),
 (r'I can find the common chord of two intersecting circles.', r'Em tính được dây chung của hai đường tròn cắt nhau.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Relative Positions of Two Circles', title_vi='Vị trí tương đối của hai đường tròn', topic=TOPIC,
       folder='circles', file='two-circles', catalog_title_vi='Vị trí tương đối của hai đường tròn',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Intersecting, tangent and non-intersecting circles; the line of centers and the common chord.', level='Intermediate', minutes=75,
       description_vi='Bài 17 – Hai đường tròn cắt nhau, tiếp xúc, không giao nhau; đường nối tâm và dây chung.',
       tags_vi=['hai đường tròn', 'tiếp xúc', 'dây chung'], prerequisites=['g9-circles-04'], tags=['two circles', 'tangent circles', 'common chord'], order=170)
