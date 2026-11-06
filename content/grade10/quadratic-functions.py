# -*- coding: utf-8 -*-
"""g10-func-02 = Toán 10 KNTT, Bài 16: Hàm số bậc hai. Mã ngân hàng câu hỏi: TOAN10-C6-B16."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g10f as S
from sp_g10f import poly, D, iv

CV = 'Hàm số bậc hai'
vocab = defs(CV, [
 ('quadf', 'quadratic function', 'hàm số bậc hai', '\\(y=ax^2+bx+c\\) with \\(a\\ne0\\); its domain is \\(\\mathbb R\\).', '\\(y=ax^2+bx+c\\) với \\(a\\ne0\\); tập xác định là \\(\\mathbb R\\).', 'The area is a quadratic function of the width.', ''),
 ('parab', 'parabola', 'parabol', 'the graph of a quadratic function.', 'đồ thị của hàm số bậc hai.', 'The parabola opens downward.', ''),
 ('vertx', 'vertex', 'đỉnh (của parabol)', 'the turning point \\(I\\left(-\\dfrac b{2a};-\\dfrac\\Delta{4a}\\right)\\).', 'điểm \\(I\\left(-\\dfrac b{2a};-\\dfrac\\Delta{4a}\\right)\\) nơi đồ thị đổi chiều.', 'The vertex is the highest point.', '\\(I\\)'),
 ('axsym', 'axis of symmetry', 'trục đối xứng', 'the vertical line \\(x=-\\dfrac b{2a}\\) through the vertex.', 'đường thẳng \\(x=-\\dfrac b{2a}\\) đi qua đỉnh.', 'The axis of symmetry is \\(x=2\\).', ''),
 ('opensup', 'open upward / downward', 'bề lõm quay lên / quay xuống', '\\(a\\gt0\\): opens upward (lowest point); \\(a\\lt0\\): opens downward (highest point).', '\\(a\\gt0\\): bề lõm quay lên (có điểm thấp nhất); \\(a\\lt0\\): bề lõm quay xuống (có điểm cao nhất).', 'Since \\(a\\lt0\\), the parabola opens downward.', ''),
 ('varbl', 'table of variations', 'bảng biến thiên', 'a table showing where the function increases and decreases and its extreme value.', 'bảng cho biết các khoảng đồng biến, nghịch biến và giá trị cực đại hoặc cực tiểu.', 'Draw the table of variations.', '')])
goals = [('find the vertex, the axis of symmetry and the direction of a parabola;', 'tìm [[đỉnh|đỉnh (của parabol)]], [[trục đối xứng]] và chiều [[bề lõm|bề lõm quay lên / quay xuống]] của [[parabol]];'),
         ('draw the graph and the table of variations of \\(y=ax^2+bx+c\\);', 'vẽ đồ thị và lập [[bảng biến thiên]] của [[hàm số bậc hai]];'),
         ('find the largest or smallest value;', 'tìm giá trị lớn nhất, nhỏ nhất;'),
         ('solve optimisation problems (areas, prices, heights).', 'giải bài toán tối ưu thực tế (diện tích, giá bán, độ cao).')]
phrases = [('<b>Find the vertex of the parabola.</b>', 'Tìm đỉnh của parabol.'), ('<b>The parabola opens upward.</b>', 'Parabol có bề lõm quay lên.'), ('<b>Draw the table of variations.</b>', 'Lập bảng biến thiên.'),
           ('<b>Find the maximum height of the ball.</b>', 'Tìm độ cao lớn nhất của quả bóng.'), ('<b>Which width gives the largest area?</b>', 'Chiều rộng nào cho diện tích lớn nhất?')]
review = T('From Bài 15: domain, graph, increasing/decreasing. From Grade 9: \\(y=ax^2\\) is a parabola with vertex \\(O\\); \\(ax^2+bx+c=0\\) has \\(\\Delta=b^2-4ac\\). Completing the square: \\(ax^2+bx+c=a\\left(x+\\dfrac b{2a}\\right)^2-\\dfrac{\\Delta}{4a}\\).', 'Từ Bài 15: tập xác định, đồ thị, đồng biến/nghịch biến. Từ lớp 9: \\(y=ax^2\\) là parabol đỉnh \\(O\\); phương trình \\(ax^2+bx+c=0\\) có \\(\\Delta=b^2-4ac\\). Biến đổi: \\(ax^2+bx+c=a\\left(x+\\dfrac b{2a}\\right)^2-\\dfrac{\\Delta}{4a}\\).')
theory = '<h3>16.1 %s</h3>' % TI('Quadratic functions and their graphs', 'Hàm số bậc hai và đồ thị')
theory += BOX('blue', ('Definition and graph', 'Định nghĩa và đồ thị'), UL([T('\\(y=ax^2+bx+c\\) (\\(a\\ne0\\)), domain \\(\\mathbb R\\). Its graph is a parabola with vertex \\(I\\left(-\\dfrac b{2a};-\\dfrac\\Delta{4a}\\right)\\) and axis of symmetry \\(x=-\\dfrac b{2a}\\).', '\\(y=ax^2+bx+c\\) (\\(a\\ne0\\)), tập xác định \\(\\mathbb R\\). Đồ thị là một parabol có đỉnh \\(I\\left(-\\dfrac b{2a};-\\dfrac\\Delta{4a}\\right)\\), trục đối xứng \\(x=-\\dfrac b{2a}\\).'),
  T('\\(a\\gt0\\): opens upward; \\(a\\lt0\\): opens downward. The graph cuts \\(Oy\\) at \\((0;c)\\); it cuts \\(Ox\\) at the roots of \\(ax^2+bx+c=0\\) (if any).', '\\(a\\gt0\\): bề lõm quay lên; \\(a\\lt0\\): bề lõm quay xuống. Đồ thị cắt \\(Oy\\) tại \\((0;c)\\), cắt \\(Ox\\) tại các nghiệm của \\(ax^2+bx+c=0\\) (nếu có).')]))
theory += BOX('mint', ('Drawing steps', 'Các bước vẽ'), UL([T('Find the vertex and the axis.', 'Xác định đỉnh và trục đối xứng.'), T('Find a few points: intersections with the axes and points symmetric about the axis.', 'Tìm vài điểm: giao với các trục, các điểm đối xứng qua trục.'), T('Draw a smooth curve, opening as the sign of \\(a\\) says.', 'Vẽ đường cong trơn, bề lõm theo dấu của \\(a\\).')]))
theory += GRAPH({'view': [-5, 5, -5, 6], 'functions': [{'f': 'a*x^2+b*x+c', 'label': 'y = ax² + bx + c'}], 'params': [{'name': 'a', 'min': -3, 'max': 3, 'value': 1, 'step': 0.5}, {'name': 'b', 'min': -4, 'max': 4, 'value': -2, 'step': 1}, {'name': 'c', 'min': -4, 'max': 4, 'value': -1, 'step': 1}], 'family': [{'a': 1, 'b': -2, 'c': -1, '_label': 'y = x² − 2x − 1'}, {'a': -1, 'b': 2, 'c': 3, '_label': 'y = −x² + 2x + 3'}, {'a': 0.5, 'b': 0, 'c': -4, '_label': 'y = 0.5x² − 4'}]},
  cap=('Three parabolas: the sign of \\(a\\) decides the direction (\\(a\\gt0\\): opening up, \\(a\\lt0\\): opening down); the vertex is at \\(x=-\\frac b{2a}\\); \\(c\\) is where the graph meets \\(Oy\\). (When \\(a=0\\) the graph is a line, not a parabola.)', 'Ba parabol: dấu của \\(a\\) quyết định chiều bề lõm (\\(a\\gt0\\): quay lên, \\(a\\lt0\\): quay xuống); đỉnh có hoành độ \\(x=-\\frac b{2a}\\); \\(c\\) là tung độ giao điểm với \\(Oy\\). (Khi \\(a=0\\) đồ thị là đường thẳng, không phải parabol.)'), alt=('Three parabolas y = ax² + bx + c with different a, b, c', ''), height=330)
theory += '<h3>16.2 %s</h3>' % TI('Variations and extreme values', 'Sự biến thiên và giá trị lớn nhất, nhỏ nhất')
theory += TBL(['', TI('\\(a\\gt0\\)', '\\(a\\gt0\\)'), TI('\\(a\\lt0\\)', '\\(a\\lt0\\)')], [
  [TI('On \\(\\left(-\\infty;-\\frac b{2a}\\right)\\)', 'Trên \\(\\left(-\\infty;-\\frac b{2a}\\right)\\)'), TI('decreasing', 'nghịch biến'), TI('increasing', 'đồng biến')],
  [TI('On \\(\\left(-\\frac b{2a};+\\infty\\right)\\)', 'Trên \\(\\left(-\\frac b{2a};+\\infty\\right)\\)'), TI('increasing', 'đồng biến'), TI('decreasing', 'nghịch biến')],
  [TI('Extreme value', 'Giá trị đặc biệt'), TI('minimum \\(-\\frac\\Delta{4a}\\) at the vertex', 'nhỏ nhất bằng \\(-\\frac\\Delta{4a}\\) tại đỉnh'), TI('maximum \\(-\\frac\\Delta{4a}\\) at the vertex', 'lớn nhất bằng \\(-\\frac\\Delta{4a}\\) tại đỉnh')]])
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('\\(x_I=-\\dfrac{b}{2a}\\) (with the minus sign). It is often easier to get \\(y_I\\) by substituting \\(x_I\\) than by computing \\(-\\dfrac\\Delta{4a}\\). In real problems check that the best \\(x\\) is allowed (a length must be positive…).', '\\(x_I=-\\dfrac{b}{2a}\\) (có dấu trừ). Thường tính \\(y_I\\) bằng cách thay \\(x_I\\) vào hàm số nhanh hơn tính \\(-\\dfrac\\Delta{4a}\\). Trong bài toán thực tế, kiểm tra giá trị \\(x\\) tìm được có thỏa điều kiện (độ dài phải dương…).'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Key features', 'Các yếu tố của parabol'), T('For \\(y=x^2-4x+3\\), find the vertex, the axis, the direction and the intersections with the axes.', 'Với \\(y=x^2-4x+3\\), tìm đỉnh, trục đối xứng, chiều bề lõm và giao điểm với các trục.'), T('\\(a=1\\), \\(b=-4\\), \\(c=3\\).', '\\(a=1\\), \\(b=-4\\), \\(c=3\\).'),
  [T('\\(x_I=-\\dfrac{-4}{2}=2\\), \\(y_I=4-8+3=-1\\); axis \\(x=2\\); \\(a\\gt0\\): opens upward.', '\\(x_I=-\\dfrac{-4}{2}=2\\), \\(y_I=4-8+3=-1\\); trục \\(x=2\\); \\(a\\gt0\\): bề lõm quay lên.'), T('\\(Oy\\): \\((0;3)\\). \\(Ox\\): \\(x^2-4x+3=0\\iff x=1\\) or \\(x=3\\).', '\\(Oy\\): \\((0;3)\\). \\(Ox\\): \\(x^2-4x+3=0\\iff x=1\\) hoặc \\(x=3\\).')],
  T('\\(I(2;-1)\\), \\(x=2\\), opens upward, \\((0;3)\\), \\((1;0)\\), \\((3;0)\\).', '\\(I(2;-1)\\), \\(x=2\\), bề lõm quay lên, \\((0;3)\\), \\((1;0)\\), \\((3;0)\\).'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Table of variations', 'Bảng biến thiên'), T('Study the variations of \\(y=-2x^2+4x+1\\) and give its largest value.', 'Xét sự biến thiên của \\(y=-2x^2+4x+1\\) và tìm giá trị lớn nhất.'), T('\\(a=-2\\lt0\\): opens downward.', '\\(a=-2\\lt0\\): bề lõm quay xuống.'),
  [T('\\(x_I=-\\dfrac{4}{-4}=1\\), \\(y_I=-2+4+1=3\\).', '\\(x_I=-\\dfrac{4}{-4}=1\\), \\(y_I=-2+4+1=3\\).'), T('Increasing on \\((-\\infty;1)\\), decreasing on \\((1;+\\infty)\\).', 'Đồng biến trên \\((-\\infty;1)\\), nghịch biến trên \\((1;+\\infty)\\).')],
  T('Largest value 3 at \\(x=1\\); no smallest value.', 'Giá trị lớn nhất bằng 3 tại \\(x=1\\); không có giá trị nhỏ nhất.'))
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Find the parabola', 'Xác định parabol'), T('Find \\(y=ax^2+bx+c\\) whose vertex is \\(I(1;2)\\) and which passes through \\(A(0;3)\\).', 'Tìm parabol \\(y=ax^2+bx+c\\) có đỉnh \\(I(1;2)\\) và đi qua \\(A(0;3)\\).'), T('Vertex form \\(y=a(x-1)^2+2\\).', 'Dạng đỉnh \\(y=a(x-1)^2+2\\).'),
  [T('\\(A\\): \\(3=a(0-1)^2+2\\Rightarrow a=1\\).', '\\(A\\): \\(3=a(0-1)^2+2\\Rightarrow a=1\\).'), T('\\(y=(x-1)^2+2=x^2-2x+3\\).', '\\(y=(x-1)^2+2=x^2-2x+3\\).')], T('\\(y=x^2-2x+3\\).', '\\(y=x^2-2x+3\\).'))
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('A pen along a wall', 'Chuồng dựa vào tường'), T('With 40 m of fence, a farmer builds a rectangular pen along a long wall (the wall is one side). Find the dimensions with the largest area.', 'Với 40 m lưới, bác nông dân rào chuồng hình chữ nhật dựa vào một bức tường dài (tường là một cạnh). Tìm kích thước để diện tích lớn nhất.'),
  T('Let \\(x\\) be the two sides perpendicular to the wall.', 'Gọi \\(x\\) là hai cạnh vuông góc với tường.'), [T('Third side \\(40-2x\\) (\\(0\\lt x\\lt20\\)); \\(S(x)=x(40-2x)=-2x^2+40x\\).', 'Cạnh thứ ba \\(40-2x\\) (\\(0\\lt x\\lt20\\)); \\(S(x)=x(40-2x)=-2x^2+40x\\).'), T('Vertex \\(x=10\\), \\(S(10)=200\\).', 'Đỉnh tại \\(x=10\\), \\(S(10)=200\\).')],
  T('\\(10\\) m \\(\\times\\) \\(20\\) m, area \\(200\\ \\text{m}^2\\).', '\\(10\\) m \\(\\times\\) \\(20\\) m, diện tích \\(200\\ \\text{m}^2\\).'))
tg = (9.8 + math.sqrt(9.8 ** 2 + 4 * 4.9)) / 9.8; assert abs(tg - 2.097) < 0.001 and abs(-4.9 + 9.8 + 1 - 5.9) < 1e-9
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Flight of a ball', 'Quỹ đạo quả bóng'), T('A ball is kicked up from 1 m above the ground. Its height is \\(h(t)=-4.9t^2+9.8t+1\\) (m, \\(t\\) in s). Find the greatest height and when the ball reaches the ground (to 0.01 s).', 'Một quả bóng được đá lên từ độ cao 1 m. Độ cao \\(h(t)=-4{,}9t^2+9{,}8t+1\\) (m, \\(t\\) tính bằng giây). Tìm độ cao lớn nhất và thời điểm bóng chạm đất (làm tròn đến 0,01 s).'),
  T('Vertex for the maximum; solve \\(h(t)=0\\) with \\(t\\gt0\\).', 'Đỉnh cho độ cao lớn nhất; giải \\(h(t)=0\\) với \\(t\\gt0\\).'),
  [T('\\(t_I=\\dfrac{9.8}{9.8}=1\\), \\(h(1)=5.9\\) m.', '\\(t_I=\\dfrac{9{,}8}{9{,}8}=1\\), \\(h(1)=5{,}9\\) m.'), T('\\(-4.9t^2+9.8t+1=0\\Rightarrow t=\\dfrac{9.8+\\sqrt{115.64}}{9.8}\\approx2.10\\) s (the other root is negative).', '\\(-4{,}9t^2+9{,}8t+1=0\\Rightarrow t=\\dfrac{9{,}8+\\sqrt{115{,}64}}{9{,}8}\\approx2{,}10\\) s (nghiệm còn lại âm).')],
  T('Greatest height 5.9 m (at \\(t=1\\) s); it lands after about 2.10 s.', 'Độ cao lớn nhất 5,9 m (tại \\(t=1\\) s); bóng chạm đất sau khoảng 2,10 s.'))
assert abs(9.8 ** 2 + 4 * 4.9 - 115.64) < 1e-9 and round(tg, 2) == 2.10

def lvl(P):
    a, h, k = P['v']; b, c = -2 * a * h, a * h * h + k; cs = [a, b, c]
    o1 = M4(1, 'The vertex of \\(y=%s\\) is…' % poly(cs), 'Đỉnh của parabol \\(y=%s\\) là…' % poly(cs), '(%s;\\,%s)' % (fr(F(h)), fr(F(k))), ['(%s;\\,%s)' % (fr(F(-h)), fr(F(k))), '(%s;\\,%s)' % (fr(F(h)), fr(F(c))), '(%s;\\,%s)' % (fr(F(k)), fr(F(h)))],
            '\\(x_I=-\\dfrac b{2a}=%s\\), \\(y_I=%s\\).' % (fr(F(h)), fr(F(k))), '\\(x_I=-\\dfrac b{2a}=%s\\), \\(y_I=%s\\).' % (fr(F(h)), fr(F(k))))
    a2, h2, k2 = P['m']; b2, c2 = -2 * a2 * h2, a2 * h2 * h2 + k2; up = a2 > 0
    A_ = S.TT('decreasing on \\(%s\\), increasing on \\(%s\\)' % (iv(None, h2), iv(h2, None, lo='(')), 'nghịch biến trên \\(%s\\), đồng biến trên \\(%s\\)' % (iv(None, h2), iv(h2, None, lo='(')))
    B_ = S.TT('increasing on \\(%s\\), decreasing on \\(%s\\)' % (iv(None, h2), iv(h2, None, lo='(')), 'đồng biến trên \\(%s\\), nghịch biến trên \\(%s\\)' % (iv(None, h2), iv(h2, None, lo='(')))
    o2 = M4(2, 'The function \\(y=%s\\) is…' % poly([a2, b2, c2]), 'Hàm số \\(y=%s\\)…' % poly([a2, b2, c2]), A_ if up else B_, [B_ if up else A_, S.TT('increasing on \\(\\mathbb R\\)', 'đồng biến trên \\(\\mathbb R\\)'), S.TT('decreasing on \\(\\mathbb R\\)', 'nghịch biến trên \\(\\mathbb R\\)')],
            '\\(a%s0\\), vertex at \\(x=%s\\).' % ('\\gt' if up else '\\lt', fr(F(h2))), '\\(a%s0\\), đỉnh tại \\(x=%s\\).' % ('\\gt' if up else '\\lt', fr(F(h2))))
    L = P['fence']; A3 = F(L * L, 16)
    o3 = M4(3, 'A rectangular flower bed is edged with %d m of bricks (all four sides). Its largest possible area is…' % L, 'Một bồn hoa hình chữ nhật được viền bằng %d m gạch (cả bốn cạnh). Diện tích lớn nhất có thể của bồn hoa là…' % L,
            fr(A3) + '\\ \\text{m}^2', [fr(F(L * L, 8)) + '\\ \\text{m}^2', fr(F(L * L, 4)) + '\\ \\text{m}^2', fr(A3 + L) + '\\ \\text{m}^2'], '\\(S=x\\left(%s-x\\right)\\) is largest at \\(x=%s\\) (a square).' % (fr(F(L, 2)), fr(F(L, 4))), '\\(S=x\\left(%s-x\\right)\\) lớn nhất khi \\(x=%s\\) (hình vuông).' % (fr(F(L, 2)), fr(F(L, 4))))
    a4, h4, k4, claim = P['ax']; b4, c4 = -2 * a4 * h4, a4 * h4 * h4 + k4
    t4 = tf(4, 'The axis of symmetry of \\(y=%s\\) is \\(x=%s\\).' % (poly([a4, b4, c4]), fr(F(claim))), 'Trục đối xứng của parabol \\(y=%s\\) là \\(x=%s\\).' % (poly([a4, b4, c4]), fr(F(claim))), claim == h4,
            '\\(x=-\\dfrac{b}{2a}=%s\\).' % fr(F(h4)), '\\(x=-\\dfrac{b}{2a}=%s\\).' % fr(F(h4)))
    a5, h5, k5, kind = P['ext']; b5, c5 = -2 * a5 * h5, a5 * h5 * h5 + k5; real_kind = 'min' if a5 > 0 else 'max'
    t5 = tf(5, 'The function \\(y=%s\\) has a %s value equal to %s.' % (poly([a5, b5, c5]), 'smallest' if kind == 'min' else 'largest', fr(F(k5))), 'Hàm số \\(y=%s\\) có giá trị %s bằng %s.' % (poly([a5, b5, c5]), 'nhỏ nhất' if kind == 'min' else 'lớn nhất', fr(F(k5))), kind == real_kind,
            '\\(a%s0\\): the vertex value %s is the %s value.' % ('\\gt' if a5 > 0 else '\\lt', fr(F(k5)), 'smallest' if a5 > 0 else 'largest'), '\\(a%s0\\): tung độ đỉnh %s là giá trị %s.' % ('\\gt' if a5 > 0 else '\\lt', fr(F(k5)), 'nhỏ nhất' if a5 > 0 else 'lớn nhất'))
    (h6, k6), (x6, y6) = P['find']; a6 = F(y6 - k6, (x6 - h6) ** 2)
    s6 = sh(6, 'The parabola \\(y=ax^2+bx+c\\) has vertex \\(I(%d;\\,%d)\\) and passes through \\(M(%d;\\,%d)\\). Find \\(a\\).' % (h6, k6, x6, y6), 'Parabol \\(y=ax^2+bx+c\\) có đỉnh \\(I(%d;\\,%d)\\) và đi qua \\(M(%d;\\,%d)\\). Tìm \\(a\\).' % (h6, k6, x6, y6), str(a6.numerator) if a6.denominator == 1 else str(float(a6)),
            '\\(%d=a(%d-%d)^2+%d\\Rightarrow a=%s\\).' % (y6, x6, h6, k6, fr(a6)), '\\(%d=a(%d-%d)^2+%d\\Rightarrow a=%s\\).' % (y6, x6, h6, k6, fr(a6)))
    v0, h0 = P['ball']; t = F(v0, 10); H = -5 * t * t + v0 * t + h0
    s7 = sh(7, 'A ball is thrown up with height \\(h(t)=-5t^2+%dt+%d\\) (m). Find its greatest height (m).' % (v0, h0), 'Một quả bóng được ném lên với độ cao \\(h(t)=-5t^2+%dt+%d\\) (m). Tìm độ cao lớn nhất của bóng (m).' % (v0, h0), str(float(H)) if H.denominator != 1 else H.numerator,
            'Vertex \\(t=%s\\): \\(h=%s\\).' % (str(float(t)), str(float(H))), 'Đỉnh \\(t=%s\\): \\(h=%s\\).' % (D(t), D(H)))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
PP = [dict(v=(1, 3, -2), m=(2, -1, 1), fence=24, ax=(1, 2, 1, 2), ext=(-1, 1, 4, 'max'), find=((1, 2), (3, 10)), ball=(20, 1)),
      dict(v=(-1, 2, 5), m=(-1, 3, 2), fence=36, ax=(2, -1, 0, 1), ext=(2, -1, -3, 'max'), find=((-2, 1), (0, -7)), ball=(10, 2)),
      dict(v=(2, -1, 3), m=(3, 1, -2), fence=60, ax=(-3, 1, 2, 1), ext=(F(1, 2), 2, -1, 'min'), find=((2, -3), (4, 3)), ball=(15, 1))]
practice = three(lvl, PP)
practice = with_self(practice, S.M16S10, start=8)
mistakes = [('<b>Forgetting the minus sign.</b> \\(x_I=-\\dfrac{b}{2a}\\): for \\(y=x^2-4x+3\\), \\(x_I=2\\), not \\(-2\\).', '<b>Quên dấu trừ.</b> \\(x_I=-\\dfrac{b}{2a}\\): với \\(y=x^2-4x+3\\), \\(x_I=2\\), không phải \\(-2\\).'),
            ('<b>Mixing up the direction.</b> \\(a\\gt0\\): the vertex is the lowest point (minimum).', '<b>Nhầm chiều bề lõm.</b> \\(a\\gt0\\): đỉnh là điểm thấp nhất (giá trị nhỏ nhất).'),
            ('<b>Giving \\(x_I\\) as the extreme value.</b> The largest/smallest value is \\(y_I\\).', '<b>Lấy \\(x_I\\) làm giá trị lớn nhất/nhỏ nhất.</b> Giá trị đó là \\(y_I\\).'),
            ('<b>Ignoring real conditions.</b> In optimisation, the variable must stay in its allowed interval.', '<b>Bỏ qua điều kiện thực tế.</b> Trong bài toán tối ưu, biến phải thuộc khoảng cho phép.')]
summary = [('\\(y=ax^2+bx+c\\) (\\(a\\ne0\\)): parabola, vertex \\(I\\left(-\\frac b{2a};-\\frac\\Delta{4a}\\right)\\), axis \\(x=-\\frac b{2a}\\).', '\\(y=ax^2+bx+c\\) (\\(a\\ne0\\)): parabol, đỉnh \\(I\\left(-\\frac b{2a};-\\frac\\Delta{4a}\\right)\\), trục \\(x=-\\frac b{2a}\\).'),
           ('\\(a\\gt0\\): decreasing then increasing, minimum at \\(I\\); \\(a\\lt0\\): increasing then decreasing, maximum at \\(I\\).', '\\(a\\gt0\\): nghịch biến rồi đồng biến, nhỏ nhất tại \\(I\\); \\(a\\lt0\\): đồng biến rồi nghịch biến, lớn nhất tại \\(I\\).'),
           ('Vertex form: \\(y=a(x-x_I)^2+y_I\\).', 'Dạng đỉnh: \\(y=a(x-x_I)^2+y_I\\).'),
           ('Key words: quadratic function, parabola, vertex, axis of symmetry, maximum, minimum.', 'Từ cần nhớ: quadratic function, parabola, vertex, axis of symmetry, maximum, minimum.')]
checks = [('I can find the vertex and the axis of a parabola.', 'Em tìm được đỉnh và trục đối xứng của parabol.'), ('I can draw the graph and the table of variations.', 'Em vẽ được đồ thị và lập bảng biến thiên.'),
          ('I can find the largest or smallest value.', 'Em tìm được giá trị lớn nhất, nhỏ nhất.'), ('I can solve a simple optimisation problem.', 'Em giải được bài toán tối ưu đơn giản.')]
LL('g10-func-02', 'Quadratic Functions', CV, ('Functions and Graphs', 'Hàm số, đồ thị và ứng dụng'), 'functions', 'quadratic-functions', 160, 'Intermediate', 70, ('functions, quadratic equations', 'hàm số, phương trình bậc hai'),
   'Quadratic functions: parabola, vertex, axis, variations, largest and smallest values, optimisation problems.', 'Bài 16 – Hàm số bậc hai: parabol, đỉnh, trục đối xứng, sự biến thiên, giá trị lớn nhất, nhỏ nhất, bài toán tối ưu.',
   ['quadratic function', 'parabola', 'vertex', 'axis of symmetry'], ['hàm số bậc hai', 'parabol', 'đỉnh', 'trục đối xứng'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g10-func-01'])
