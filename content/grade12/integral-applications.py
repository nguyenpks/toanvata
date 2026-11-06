# -*- coding: utf-8 -*-
"""g12-int-03 = Toán 12 KNTT, Bài 13: Ứng dụng hình học của tích phân. Mã ngân hàng câu hỏi: TOAN12-C4-B13."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g12c as SC
import sp_g12d as S
from sp_g12d import pi
from sp_g12c import defint, ptex

CV = 'Ứng dụng hình học của tích phân'
vocab = defs(CV, [
 ('parea', 'area of a plane region', 'diện tích hình phẳng', '\\(S=\\int_a^b|f(x)-g(x)|\\,dx\\) for the region between \\(y=f(x)\\), \\(y=g(x)\\), \\(x=a\\), \\(x=b\\).', '\\(S=\\int_a^b|f(x)-g(x)|\\,dx\\) với hình phẳng giới hạn bởi \\(y=f(x)\\), \\(y=g(x)\\), \\(x=a\\), \\(x=b\\).', 'Find the area between the two curves.', '\\(S\\)'),
 ('xsec', 'cross-section', 'thiết diện (mặt cắt)', 'the plane figure obtained by cutting a solid with the plane \\(x=t\\); its area is \\(S(t)\\).', 'hình phẳng nhận được khi cắt vật thể bởi mặt phẳng \\(x=t\\); diện tích là \\(S(t)\\).', 'Each cross-section is a square.', '\\(S(x)\\)'),
 ('solrev', 'solid of revolution', 'khối tròn xoay', 'the solid formed by rotating a plane region about an axis.', 'khối tạo thành khi quay một hình phẳng quanh một trục.', 'Rotating the region gives a solid of revolution.', ''),
 ('rotax', 'rotate about the x-axis', 'quay quanh trục hoành', 'turn the region around \\(Ox\\); \\(V=\\pi\\int_a^bf^2(x)\\,dx\\).', 'quay hình phẳng quanh \\(Ox\\); \\(V=\\pi\\int_a^bf^2(x)\\,dx\\).', 'Rotate the region about the x-axis.', ''),
 ('intpt', 'intersection point', 'giao điểm', 'a common point of two graphs; its \\(x\\) solves \\(f(x)=g(x)\\).', 'điểm chung của hai đồ thị; hoành độ là nghiệm của \\(f(x)=g(x)\\).', 'Find the intersection points first.', ''),
 ('parch', 'parabolic arch', 'vòm (cổng) parabol', 'an arch shaped like a parabola; its area is \\(\\frac23\\) of the surrounding rectangle.', 'vòm có dạng parabol; diện tích bằng \\(\\frac23\\) hình chữ nhật bao quanh.', 'The gate is a parabolic arch.', '')])
goals = [('compute the area between a graph and the \\(x\\)-axis, splitting where the sign changes;', 'tính [[diện tích hình phẳng]] giới hạn bởi đồ thị và trục hoành, tách tại điểm đổi dấu;'),
         ('compute the area between two graphs using their intersection points;', 'tính diện tích giữa hai đồ thị nhờ các [[giao điểm]];'),
         ('compute volumes from cross-sections and volumes of solids of revolution;', 'tính thể tích vật thể theo [[thiết diện (mặt cắt)]] và thể tích [[khối tròn xoay]];'),
         ('solve real problems: arches, tanks, vases.', 'giải bài toán thực tế: [[vòm (cổng) parabol]], bồn chứa, lọ hoa.')]
phrases = [('<b>Find the area of the shaded region.</b>', 'Tính diện tích phần tô màu.'), ('<b>Find the intersection points of the two graphs.</b>', 'Tìm giao điểm của hai đồ thị.'), ('<b>Rotate the region about the x-axis.</b>', 'Quay hình phẳng quanh trục hoành.'),
           ('<b>Find the volume of the solid of revolution.</b>', 'Tính thể tích khối tròn xoay.'), ('<b>Split the integral where the function changes sign.</b>', 'Tách tích phân tại điểm hàm số đổi dấu.')]
review = T('From Bài 12: \\(\\int_a^bf(x)\\,dx=F(b)-F(a)\\); \\(\\int_a^b=\\int_a^c+\\int_c^b\\); \\(\\int|f|\\): split at the points where \\(f\\) changes sign. If \\(f\\ge0\\), \\(\\int_a^bf\\) is the area under the graph.', 'Từ Bài 12: \\(\\int_a^bf(x)\\,dx=F(b)-F(a)\\); \\(\\int_a^b=\\int_a^c+\\int_c^b\\); \\(\\int|f|\\): tách tại các điểm \\(f\\) đổi dấu. Nếu \\(f\\ge0\\) thì \\(\\int_a^bf\\) là diện tích dưới đồ thị.')
N = 40; xs = [-1 + 3 * i / N for i in range(N + 1)]
reg = [[round(x, 4), round(x + 2, 4)] for x in xs] + [[round(x, 4), round(x * x, 4)] for x in reversed(xs)]
assert defint({0: 2, 1: 1, 2: -1}, -1, 2) == F(9, 2)
theory = '<h3>13.1 %s</h3>' % TI('Area of a plane region', 'Tính diện tích hình phẳng')
theory += BOX('blue', ('Formulas', 'Công thức'), M('S=\\int_a^b|f(x)|\\,dx,\\qquad S=\\int_a^b|f(x)-g(x)|\\,dx'),
  UL([T('The first: region between \\(y=f(x)\\), the \\(x\\)-axis, \\(x=a\\), \\(x=b\\). The second: region between two graphs and \\(x=a\\), \\(x=b\\).', 'Công thức đầu: hình phẳng giới hạn bởi \\(y=f(x)\\), trục hoành, \\(x=a\\), \\(x=b\\). Công thức sau: giữa hai đồ thị và \\(x=a\\), \\(x=b\\).'),
      T('Steps: (1) solve \\(f(x)=g(x)\\) on \\([a;b]\\); (2) on each piece \\(f-g\\) keeps its sign, so remove \\(|\\ |\\); (3) add the pieces.', 'Các bước: (1) giải \\(f(x)=g(x)\\) trên \\([a;b]\\); (2) trên mỗi khoảng con \\(f-g\\) không đổi dấu nên bỏ được \\(|\\ |\\); (3) cộng các phần.')]))
theory += GEO({'view': [-2, 3, -1, 5], 'axes': True, 'equal': False, 'steps': [{'type': 'polygon', 'through': reg, 'style': {'borders': {'visible': False}, 'fillOpacity': 0.4}}, {'type': 'curve', 'f': 'x^2'}, {'type': 'curve', 'f': 'x+2', 'style': {'strokeColor': '#c2410c'}},
  {'type': 'point', 'id': 'P', 'name': '(−1; 1)', 'at': [-1, 1], 'fixed': True}, {'type': 'point', 'id': 'Q', 'name': '(2; 4)', 'at': [2, 4], 'fixed': True}]},
  cap=('Region between \\(y=x+2\\) (orange) and \\(y=x^2\\): they meet at \\(x=-1\\) and \\(x=2\\); \\(S=\\int_{-1}^2(x+2-x^2)\\,dx=\\frac92\\).', 'Hình phẳng giữa \\(y=x+2\\) (cam) và \\(y=x^2\\): hai đồ thị cắt nhau tại \\(x=-1\\), \\(x=2\\); \\(S=\\int_{-1}^2(x+2-x^2)\\,dx=\\frac92\\).'), alt=('Region between a line and a parabola', ''), height=320)
theory += '<h3>13.2 %s</h3>' % TI('Volume of a solid', 'Tính thể tích vật thể')
theory += BOX('mint', ('By cross-sections', 'Theo diện tích thiết diện'), M('V=\\int_a^bS(x)\\,dx'), T('The solid lies between the planes \\(x=a\\), \\(x=b\\); the plane \\(x\\) (\\(a\\le x\\le b\\)) cuts it in a figure of area \\(S(x)\\) (continuous).', 'Vật thể nằm giữa hai mặt phẳng \\(x=a\\), \\(x=b\\); mặt phẳng vuông góc với \\(Ox\\) tại \\(x\\) (\\(a\\le x\\le b\\)) cắt vật thể theo thiết diện có diện tích \\(S(x)\\) (liên tục).'))
theory += BOX('blue', ('Solid of revolution', 'Khối tròn xoay'), M('V=\\pi\\int_a^bf^2(x)\\,dx'), T('Rotating the region under \\(y=f(x)\\) (\\(a\\le x\\le b\\)) about \\(Ox\\): each cross-section is a disc of radius \\(|f(x)|\\), area \\(\\pi f^2(x)\\). This gives the cone \\(V=\\frac13\\pi r^2h\\) and the sphere \\(V=\\frac43\\pi R^3\\).', 'Quay hình phẳng giới hạn bởi \\(y=f(x)\\), trục hoành, \\(x=a\\), \\(x=b\\) quanh \\(Ox\\): mỗi thiết diện là hình tròn bán kính \\(|f(x)|\\), diện tích \\(\\pi f^2(x)\\). Từ đó có thể tích khối nón \\(V=\\frac13\\pi r^2h\\) và khối cầu \\(V=\\frac43\\pi R^3\\).'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('Area needs \\(|\\ |\\): \\(\\int_{-1}^1(x^3-x)\\,dx=0\\), but the area is \\(\\frac12\\). In the volume formula, square first: \\(\\pi\\int f^2\\), not \\(\\pi\\left(\\int f\\right)^2\\).', 'Diện tích phải có \\(|\\ |\\): \\(\\int_{-1}^1(x^3-x)\\,dx=0\\) nhưng diện tích bằng \\(\\frac12\\). Công thức thể tích bình phương trước: \\(\\pi\\int f^2\\), không phải \\(\\pi\\left(\\int f\\right)^2\\).'))

assert 2 * defint({0: 4, 2: -1}, 0, 2) == F(32, 3)
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Under the \\(x\\)-axis', 'Phần nằm dưới trục hoành'), T('Find the area bounded by \\(y=x^2-4\\), the \\(x\\)-axis, \\(x=-2\\) and \\(x=2\\).', 'Tính diện tích hình phẳng giới hạn bởi \\(y=x^2-4\\), trục hoành, \\(x=-2\\), \\(x=2\\).'),
  T('On \\([-2;2]\\), \\(x^2-4\\le0\\).', 'Trên \\([-2;2]\\), \\(x^2-4\\le0\\).'), [T('\\(S=\\int_{-2}^2(4-x^2)\\,dx=\\left(4x-\\dfrac{x^3}3\\right)\\Big|_{-2}^2=\\dfrac{16}3-\\left(-\\dfrac{16}3\\right)\\).', '\\(S=\\int_{-2}^2(4-x^2)\\,dx=\\left(4x-\\dfrac{x^3}3\\right)\\Big|_{-2}^2=\\dfrac{16}3-\\left(-\\dfrac{16}3\\right)\\).')],
  T('\\(S=\\dfrac{32}{3}\\).', '\\(S=\\dfrac{32}{3}\\).'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Between a line and a parabola', 'Giữa đường thẳng và parabol'), T('Find the area between \\(y=x^2\\) and \\(y=x+2\\) (see the figure).', 'Tính diện tích hình phẳng giới hạn bởi \\(y=x^2\\) và \\(y=x+2\\) (xem hình).'), T('Solve \\(x^2=x+2\\).', 'Giải \\(x^2=x+2\\).'),
  [T('\\(x^2-x-2=0\\iff x=-1\\) or \\(x=2\\); on \\([-1;2]\\), \\(x+2\\ge x^2\\).', '\\(x^2-x-2=0\\iff x=-1\\) hoặc \\(x=2\\); trên \\([-1;2]\\), \\(x+2\\ge x^2\\).'), T('\\(S=\\int_{-1}^2(x+2-x^2)\\,dx=\\left(\\dfrac{x^2}2+2x-\\dfrac{x^3}3\\right)\\Big|_{-1}^2=\\dfrac{10}3-\\left(-\\dfrac76\\right)\\).', '\\(S=\\int_{-1}^2(x+2-x^2)\\,dx=\\left(\\dfrac{x^2}2+2x-\\dfrac{x^3}3\\right)\\Big|_{-1}^2=\\dfrac{10}3-\\left(-\\dfrac76\\right)\\).')],
  T('\\(S=\\dfrac92\\).', '\\(S=\\dfrac92\\).'))
assert defint({0: 2, 1: 1, 2: -1}, 0, 2) == F(10, 3) and defint({0: 2, 1: 1, 2: -1}, 0, -1) == F(-7, 6)
assert 2 * defint({1: 1, 3: -1}, 0, 1) == F(1, 2)
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('A curve that crosses the axis', 'Đồ thị cắt trục hoành'), T('Find the area bounded by \\(y=x^3-x\\) and the \\(x\\)-axis.', 'Tính diện tích hình phẳng giới hạn bởi \\(y=x^3-x\\) và trục hoành.'), T('Roots \\(-1,0,1\\); the sign changes at 0.', 'Nghiệm \\(-1,0,1\\); hàm đổi dấu tại 0.'),
  [T('On \\([-1;0]\\): \\(x^3-x\\ge0\\); on \\([0;1]\\): \\(x^3-x\\le0\\).', 'Trên \\([-1;0]\\): \\(x^3-x\\ge0\\); trên \\([0;1]\\): \\(x^3-x\\le0\\).'), T('\\(S=\\int_{-1}^0(x^3-x)\\,dx+\\int_0^1(x-x^3)\\,dx=\\dfrac14+\\dfrac14\\).', '\\(S=\\int_{-1}^0(x^3-x)\\,dx+\\int_0^1(x-x^3)\\,dx=\\dfrac14+\\dfrac14\\).')],
  T('\\(S=\\dfrac12\\) (while \\(\\int_{-1}^1(x^3-x)\\,dx=0\\)).', '\\(S=\\dfrac12\\) (trong khi \\(\\int_{-1}^1(x^3-x)\\,dx=0\\)).'))
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Volumes of revolution', 'Thể tích khối tròn xoay'), T('(a) Rotate the region under \\(y=\\sqrt x\\), \\(0\\le x\\le4\\), about \\(Ox\\). (b) Prove the cone formula by rotating \\(y=\\dfrac rhx\\), \\(0\\le x\\le h\\).', '(a) Quay hình phẳng giới hạn bởi \\(y=\\sqrt x\\), trục hoành, \\(x=4\\) quanh \\(Ox\\). (b) Chứng minh công thức thể tích khối nón bằng cách quay \\(y=\\dfrac rhx\\), \\(0\\le x\\le h\\).'),
  T('\\(V=\\pi\\int_a^bf^2(x)\\,dx\\).', '\\(V=\\pi\\int_a^bf^2(x)\\,dx\\).'), [T('(a) \\(V=\\pi\\int_0^4x\\,dx=\\pi\\dfrac{x^2}2\\Big|_0^4=8\\pi\\).', '(a) \\(V=\\pi\\int_0^4x\\,dx=\\pi\\dfrac{x^2}2\\Big|_0^4=8\\pi\\).'), T('(b) \\(V=\\pi\\int_0^h\\dfrac{r^2}{h^2}x^2dx=\\pi\\dfrac{r^2}{h^2}\\cdot\\dfrac{h^3}3\\).', '(b) \\(V=\\pi\\int_0^h\\dfrac{r^2}{h^2}x^2dx=\\pi\\dfrac{r^2}{h^2}\\cdot\\dfrac{h^3}3\\).')],
  T('(a) \\(8\\pi\\); (b) \\(V=\\dfrac13\\pi r^2h\\).', '(a) \\(8\\pi\\); (b) \\(V=\\dfrac13\\pi r^2h\\).'))
assert F(2, 3) * 8 * 6 == 32 and 32 * 150 == 4800
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Painting a parabolic gate', 'Sơn cổng parabol'), T('A school gate is a parabolic arch 8 m wide at the ground and 6 m high. Paint costs 150 thousand VND per m² (one side). Find the area of the gate and the cost.', 'Cổng trường có dạng vòm parabol, chân cổng rộng 8 m, cao 6 m. Tiền sơn là 150 nghìn đồng/m² (sơn một mặt). Tính diện tích cổng và chi phí.'),
  T('Put the axis of symmetry on \\(Oy\\): \\(y=6-ax^2\\) passes through \\((4;0)\\).', 'Đặt trục đối xứng trùng \\(Oy\\): \\(y=6-ax^2\\) đi qua \\((4;0)\\).'),
  [T('\\(6-16a=0\\Rightarrow a=\\dfrac38\\), \\(y=6-\\dfrac38x^2\\).', '\\(6-16a=0\\Rightarrow a=\\dfrac38\\), \\(y=6-\\dfrac38x^2\\).'), T('\\(S=\\int_{-4}^4\\left(6-\\dfrac38x^2\\right)dx=\\left(6x-\\dfrac{x^3}8\\right)\\Big|_{-4}^4=16-(-16)=32\\).', '\\(S=\\int_{-4}^4\\left(6-\\dfrac38x^2\\right)dx=\\left(6x-\\dfrac{x^3}8\\right)\\Big|_{-4}^4=16-(-16)=32\\).'),
   T('Check: \\(\\frac23\\cdot8\\cdot6=32\\). Cost \\(32\\cdot150\\).', 'Kiểm tra: \\(\\frac23\\cdot8\\cdot6=32\\). Chi phí \\(32\\cdot150\\).')],
  T('\\(S=32\\ \\text{m}^2\\); cost 4\\,800 thousand VND (4.8 million).', '\\(S=32\\ \\text{m}^2\\); chi phí 4\\,800 nghìn đồng (4,8 triệu đồng).'))
assert defint({0: 6, 2: F(-3, 8)}, -4, 4) == 32

def lvl(P):
    k = P['par']; v1 = F(k ** 3, 6)
    o1 = M4(1, 'The area bounded by \\(y=-x^2+%dx\\) and the \\(x\\)-axis is…' % k, 'Diện tích hình phẳng giới hạn bởi \\(y=-x^2+%dx\\) và trục hoành là…' % k, fr(v1), [fr(F(k ** 3, 3)), fr(F(k ** 2, 2)), fr(-v1), fr(F(k ** 3, 2))],
            'Roots \\(0\\), \\(%d\\): \\(\\int_0^{%d}(-x^2+%dx)\\,dx=%s\\).' % (k, k, k, fr(v1)), 'Nghiệm \\(0\\), \\(%d\\): \\(\\int_0^{%d}(-x^2+%dx)\\,dx=%s\\).' % (k, k, k, fr(v1)))
    m = P['two']; v2 = F(m ** 3, 6)
    o2 = M4(2, 'The area between \\(y=x^2\\) and \\(y=%dx\\) is…' % m, 'Diện tích hình phẳng giới hạn bởi \\(y=x^2\\) và \\(y=%dx\\) là…' % m, fr(v2), [fr(F(m ** 3, 3)), fr(F(m ** 3, 2)), fr(F(m ** 2, 2)), fr(F(m ** 3, 12)), fr(F(m ** 3))],
            '\\(x^2=%dx\\iff x=0\\vee x=%d\\); \\(\\int_0^{%d}(%dx-x^2)\\,dx=%s\\).' % (m, m, m, m, fr(v2)), '\\(x^2=%dx\\iff x=0\\) hoặc \\(x=%d\\); \\(\\int_0^{%d}(%dx-x^2)\\,dx=%s\\).' % (m, m, m, m, fr(v2)))
    r_, h = P['cone']; v3 = F(r_ * r_ * h, 3)
    o3 = M4(3, 'A funnel is the solid made by rotating \\(y=%sx\\), \\(0\\le x\\le%d\\) (dm), about \\(Ox\\). Its volume is…' % (fr(F(r_, h)) if F(r_, h) != 1 else '', h), 'Một cái phễu là khối tạo thành khi quay \\(y=%sx\\), \\(0\\le x\\le%d\\) (dm) quanh \\(Ox\\). Thể tích của phễu là…' % (fr(F(r_, h)) if F(r_, h) != 1 else '', h),
            pi(v3) + '\\ \\text{dm}^3', [pi(3 * v3) + '\\ \\text{dm}^3', pi(v3 * 3 / 2) + '\\ \\text{dm}^3', fr(v3) + '\\ \\text{dm}^3'], '\\(V=\\pi\\int_0^{%d}\\left(%sx\\right)^2dx=%s\\) (a cone with \\(r=%d\\), \\(h=%d\\)).' % (h, fr(F(r_, h)), pi(v3), r_, h), '\\(V=\\pi\\int_0^{%d}\\left(%sx\\right)^2dx=%s\\) (khối nón \\(r=%d\\), \\(h=%d\\)).' % (h, fr(F(r_, h)), pi(v3), r_, h))
    a4, ok4 = P['cub']; real = F(a4 ** 4, 2); claim = real if ok4 else F(0)
    t4 = tf(4, 'The area bounded by \\(y=x^3-%dx\\) and the \\(x\\)-axis is \\(%s\\).' % (a4 * a4, fr(claim)), 'Diện tích hình phẳng giới hạn bởi \\(y=x^3-%dx\\) và trục hoành bằng \\(%s\\).' % (a4 * a4, fr(claim)), ok4,
            'Split at 0: \\(S=2\\int_0^{%d}(%dx-x^3)\\,dx=%s\\).' % (a4, a4 * a4, fr(real)), 'Tách tại 0: \\(S=2\\int_0^{%d}(%dx-x^3)\\,dx=%s\\).' % (a4, a4 * a4, fr(real)))
    a5, ok5 = P['sq']; real5 = F(a5 * a5, 2); claim5 = real5 if ok5 else F(2 * a5 ** 3, 3)
    t5 = tf(5, 'Rotating the region under \\(y=\\sqrt x\\), \\(0\\le x\\le%d\\), about \\(Ox\\) gives volume \\(%s\\).' % (a5, pi(claim5)), 'Quay hình phẳng giới hạn bởi \\(y=\\sqrt x\\), trục hoành, \\(x=%d\\) quanh \\(Ox\\) được khối có thể tích \\(%s\\).' % (a5, pi(claim5)), ok5,
            '\\(V=\\pi\\int_0^{%d}x\\,dx=%s\\).' % (a5, pi(real5)), '\\(V=\\pi\\int_0^{%d}x\\,dx=%s\\).' % (a5, pi(real5)))
    w, hh = P['gate']; v6 = F(2 * w * hh, 3); assert v6.denominator == 1
    s6 = sh(6, 'A tunnel entrance is a parabolic arch %d m wide at the ground and %d m high. Find its area (m²).' % (w, hh), 'Cửa một đường hầm có dạng vòm parabol, rộng %d m ở chân, cao %d m. Tính diện tích cửa hầm (m²).' % (w, hh), v6.numerator,
            '\\(\\frac23\\cdot%d\\cdot%d=%d\\) (integrate \\(y=%d-\\frac{%d}{%s}x^2\\)).' % (w, hh, v6, hh, hh, fr(F(w * w, 4))), '\\(\\frac23\\cdot%d\\cdot%d=%d\\) (tích phân của \\(y=%d-\\frac{%d}{%s}x^2\\)).' % (w, hh, v6, hh, hh, fr(F(w * w, 4))))
    L, kind = P['xs']
    if kind == 'sq': v7 = F(L ** 3, 3); en7, vi7 = 'a square of side \\(x\\)', 'hình vuông cạnh \\(x\\)'
    else: v7 = F(L ** 3, 6); en7, vi7 = 'a right isosceles triangle with legs \\(x\\)', 'tam giác vuông cân có cạnh góc vuông bằng \\(x\\)'
    assert v7.denominator == 1
    s7 = sh(7, 'A solid lies between \\(x=0\\) and \\(x=%d\\). The cross-section at \\(x\\) is %s. Find the volume.' % (L, en7), 'Một vật thể nằm giữa hai mặt phẳng \\(x=0\\) và \\(x=%d\\); thiết diện tại \\(x\\) là %s. Tính thể tích vật thể.' % (L, vi7), v7.numerator,
            '\\(V=\\int_0^{%d}S(x)\\,dx=%d\\).' % (L, v7), '\\(V=\\int_0^{%d}S(x)\\,dx=%d\\).' % (L, v7))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
PP = [dict(par=2, two=3, cone=(2, 3), cub=(1, True), sq=(2, True), gate=(6, 3), xs=(3, 'sq')),
      dict(par=4, two=2, cone=(3, 6), cub=(2, False), sq=(3, False), gate=(9, 4), xs=(6, 'tri')),
      dict(par=6, two=5, cone=(1, 2), cub=(3, True), sq=(5, True), gate=(12, 5), xs=(6, 'sq'))]
practice = three(lvl, PP)
practice = with_self(practice, S.M13S12, start=8)
mistakes = [('<b>Forgetting \\(|\\ |\\).</b> When the graph crosses the axis, split the integral; otherwise parts cancel.', '<b>Quên dấu \\(|\\ |\\).</b> Khi đồ thị cắt trục hoành phải tách tích phân, nếu không các phần sẽ triệt tiêu.'),
            ('<b>Wrong limits.</b> For the area between two graphs, the limits are the intersection points.', '<b>Sai cận.</b> Với diện tích giữa hai đồ thị, cận là hoành độ giao điểm.'),
            ('<b>\\(\\pi\\left(\\int f\\right)^2\\).</b> The volume is \\(\\pi\\int f^2\\): square the function, then integrate.', '<b>\\(\\pi\\left(\\int f\\right)^2\\).</b> Thể tích là \\(\\pi\\int f^2\\): bình phương hàm số rồi mới lấy tích phân.'),
            ('<b>Forgetting \\(\\pi\\).</b> Volumes of revolution contain \\(\\pi\\); cross-section volumes contain it only if \\(S(x)\\) does.', '<b>Quên \\(\\pi\\).</b> Thể tích khối tròn xoay có \\(\\pi\\); thể tích theo thiết diện chỉ có \\(\\pi\\) khi \\(S(x)\\) có \\(\\pi\\).')]
summary = [('\\(S=\\int_a^b|f(x)|\\,dx\\); \\(S=\\int_a^b|f(x)-g(x)|\\,dx\\).', '\\(S=\\int_a^b|f(x)|\\,dx\\); \\(S=\\int_a^b|f(x)-g(x)|\\,dx\\).'),
           ('Find intersection points, split where the sign changes.', 'Tìm giao điểm, tách tại điểm đổi dấu.'),
           ('\\(V=\\int_a^bS(x)\\,dx\\); \\(V=\\pi\\int_a^bf^2(x)\\,dx\\) (rotation about \\(Ox\\)).', '\\(V=\\int_a^bS(x)\\,dx\\); \\(V=\\pi\\int_a^bf^2(x)\\,dx\\) (quay quanh \\(Ox\\)).'),
           ('Parabolic arch: \\(\\frac23\\cdot\\text{width}\\cdot\\text{height}\\). Key words: area, volume, cross-section, solid of revolution.', 'Vòm parabol: \\(\\frac23\\cdot\\text{rộng}\\cdot\\text{cao}\\). Từ cần nhớ: area, volume, cross-section, solid of revolution.')]
checks = [('I can find the area between a graph and the \\(x\\)-axis.', 'Em tính được diện tích giữa đồ thị và trục hoành.'), ('I can find the area between two graphs.', 'Em tính được diện tích giữa hai đồ thị.'),
          ('I can find a volume from cross-sections.', 'Em tính được thể tích theo thiết diện.'), ('I can find the volume of a solid of revolution.', 'Em tính được thể tích khối tròn xoay.')]
LL('g12-int-03', 'Geometric Applications of Integrals', CV, ('Antiderivatives and Integrals', 'Nguyên hàm và tích phân'), 'integrals', 'integral-applications', 130, 'Intermediate', 75, ('definite integrals, absolute values', 'tích phân, dấu giá trị tuyệt đối'),
   'Areas of plane regions, volumes from cross-sections and volumes of solids of revolution; real-life arches and containers.', 'Bài 13 – Diện tích hình phẳng, thể tích vật thể theo thiết diện, thể tích khối tròn xoay; bài toán thực tế.',
   ['area', 'volume', 'cross-section', 'solid of revolution'], ['diện tích hình phẳng', 'thể tích', 'thiết diện', 'khối tròn xoay'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g12-int-02'])
