# -*- coding: utf-8 -*-
"""g10-func-01 = Toán 10 KNTT, Bài 15: Hàm số. Mã ngân hàng câu hỏi: TOAN10-C6-B15."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g10f as S
from sp_g10f import poly, D

def HT(r1, r2): return TBL([TI(*r1[0])] + [str(x) for x in r1[1]], [[TI(*r2[0])] + [str(x) for x in r2[1]]])
CV = 'Hàm số'
vocab = defs(CV, [
 ('func10', 'function', 'hàm số', 'a rule that gives each \\(x\\) in a set \\(D\\) exactly one number \\(y\\); we write \\(y=f(x)\\).', 'quy tắc cho tương ứng mỗi \\(x\\) thuộc tập \\(D\\) với một và chỉ một số \\(y\\); viết \\(y=f(x)\\).', 'The fare is a function of the distance.', '\\(y=f(x)\\)'),
 ('dom10', 'domain', 'tập xác định', 'the set \\(D\\) of all \\(x\\) for which \\(f(x)\\) is defined.', 'tập hợp \\(D\\) gồm mọi \\(x\\) làm cho \\(f(x)\\) có nghĩa.', 'The domain is \\([1;+\\infty)\\).', '\\(D\\)'),
 ('rng10f', 'range (set of values)', 'tập giá trị', 'the set of all values \\(f(x)\\) when \\(x\\) runs through \\(D\\).', 'tập hợp mọi giá trị \\(f(x)\\) khi \\(x\\) chạy khắp \\(D\\).', 'The range of \\(x^2\\) is \\([0;+\\infty)\\).', ''),
 ('graph10', 'graph of a function', 'đồ thị hàm số', 'the set of points \\((x;f(x))\\) with \\(x\\in D\\).', 'tập hợp các điểm \\((x;f(x))\\) với \\(x\\in D\\).', 'The point \\((2;3)\\) is on the graph.', ''),
 ('incr10', 'increasing function', 'hàm số đồng biến', '\\(x_1\\lt x_2\\Rightarrow f(x_1)\\lt f(x_2)\\): the graph goes up from left to right.', '\\(x_1\\lt x_2\\Rightarrow f(x_1)\\lt f(x_2)\\): đồ thị đi lên từ trái sang phải.', 'The function is increasing on \\((0;+\\infty)\\).', ''),
 ('decr10', 'decreasing function', 'hàm số nghịch biến', '\\(x_1\\lt x_2\\Rightarrow f(x_1)\\gt f(x_2)\\): the graph goes down from left to right.', '\\(x_1\\lt x_2\\Rightarrow f(x_1)\\gt f(x_2)\\): đồ thị đi xuống từ trái sang phải.', 'The function is decreasing on \\(\\mathbb R\\).', ''),
 ('piece10', 'piecewise-defined function', 'hàm số cho bởi nhiều công thức', 'a function given by different formulas on different parts of the domain.', 'hàm số có công thức khác nhau trên các phần khác nhau của tập xác định.', 'The electricity bill is a piecewise function.', '')])
goals = [('recognise a function given by a table, a graph or a formula;', 'nhận biết [[hàm số]] cho bằng bảng, biểu đồ, công thức;'),
         ('find the domain and compute values, also for piecewise functions;', 'tìm [[tập xác định]], tính giá trị hàm số, kể cả [[hàm số cho bởi nhiều công thức]];'),
         ('read a graph: points on the graph, range, increasing and decreasing intervals;', 'đọc [[đồ thị hàm số]]: điểm thuộc đồ thị, [[tập giá trị]], khoảng [[đồng biến|hàm số đồng biến]], [[nghịch biến|hàm số nghịch biến]];'),
         ('build simple functions from real situations.', 'thiết lập hàm số mô tả tình huống thực tế đơn giản.')]
phrases = [('<b>Find the domain of the function.</b>', 'Tìm tập xác định của hàm số.'), ('<b>Does the point lie on the graph?</b>', 'Điểm có thuộc đồ thị không?'), ('<b>The function is increasing on this interval.</b>', 'Hàm số đồng biến trên khoảng này.'),
           ('<b>Write the cost as a function of the distance.</b>', 'Biểu diễn chi phí theo quãng đường.'), ('<b>Read the value from the graph.</b>', 'Đọc giá trị từ đồ thị.')]
review = T('From lower grades: the functions \\(y=ax+b\\) (a line) and \\(y=ax^2\\) (a parabola through \\(O\\)); \\(\\sqrt A\\) needs \\(A\\ge0\\), \\(\\dfrac1A\\) needs \\(A\\ne0\\); intervals \\([a;b]\\), \\((a;+\\infty)\\)…', 'Từ lớp dưới: hàm số \\(y=ax+b\\) (đường thẳng) và \\(y=ax^2\\) (parabol qua \\(O\\)); \\(\\sqrt A\\) có nghĩa khi \\(A\\ge0\\), \\(\\dfrac1A\\) có nghĩa khi \\(A\\ne0\\); các khoảng, đoạn \\([a;b]\\), \\((a;+\\infty)\\)…')
theory = '<h3>15.1 %s</h3>' % TI('Functions and domains', 'Khái niệm hàm số, tập xác định')
theory += BOX('blue', ('Definition', 'Định nghĩa'), T('If for each \\(x\\) in a set \\(D\\subset\\mathbb R\\) there is <b>one and only one</b> number \\(y\\), we have a function \\(y=f(x)\\); \\(x\\) is the variable, \\(D\\) the domain. A function can be given by a table, a chart, a graph or a formula.', 'Nếu với mỗi \\(x\\) thuộc tập \\(D\\subset\\mathbb R\\) có <b>một và chỉ một</b> số \\(y\\) tương ứng thì ta có hàm số \\(y=f(x)\\); \\(x\\) là biến số, \\(D\\) là [[tập xác định]]. Hàm số có thể cho bằng bảng, biểu đồ, đồ thị hoặc công thức.'))
theory += BOX('mint', ('Domain of a formula', 'Tập xác định của hàm cho bằng công thức'), T('When only a formula is given, the domain is the set of \\(x\\) for which the formula makes sense: denominators \\(\\ne0\\), expressions under a square root \\(\\ge0\\). The range is the set of all values \\(f(x)\\).', 'Khi chỉ cho công thức, tập xác định là tập các \\(x\\) làm biểu thức có nghĩa: mẫu khác 0, biểu thức dưới dấu căn bậc hai không âm. [[Tập giá trị]] là tập mọi giá trị \\(f(x)\\).'))
theory += '<h3>15.2 %s</h3>' % TI('Graph of a function', 'Đồ thị của hàm số')
theory += BOX('blue', ('Definition', 'Định nghĩa'), T('The graph is the set of points \\(M(x;f(x))\\), \\(x\\in D\\). \\(M(x_0;y_0)\\) lies on the graph \\(\\iff x_0\\in D\\) and \\(y_0=f(x_0)\\).', 'Đồ thị hàm số là tập hợp các điểm \\(M(x;f(x))\\) với \\(x\\in D\\). \\(M(x_0;y_0)\\) thuộc đồ thị \\(\\iff x_0\\in D\\) và \\(y_0=f(x_0)\\).'))
theory += GRAPH({'view': [-2, 4, -2, 5], 'functions': [{'f': 'x^2-2*x', 'label': 'y = x² − 2x'}], 'points': [{'x': 1, 'y': -1, 'label': '(1; −1)'}, {'x': 3, 'y': 3, 'label': '(3; 3)'}, {'x': -1, 'y': 3, 'label': '(−1; 3)'}]},
  cap=('\\(y=x^2-2x\\): the graph goes down on \\((-\\infty;1)\\) and up on \\((1;+\\infty)\\); the lowest point is \\((1;-1)\\), so the range is \\([-1;+\\infty)\\).', '\\(y=x^2-2x\\): đồ thị đi xuống trên \\((-\\infty;1)\\), đi lên trên \\((1;+\\infty)\\); điểm thấp nhất là \\((1;-1)\\) nên tập giá trị là \\([-1;+\\infty)\\).'), alt=('Graph of a parabola with vertex (1; -1)', ''), height=300)
theory += '<h3>15.3 %s</h3>' % TI('Increasing and decreasing functions', 'Sự đồng biến, nghịch biến của hàm số')
theory += BOX('mint', ('Definitions (on an interval \\(K\\))', 'Định nghĩa (trên khoảng \\(K\\))'), UL([T('Increasing: \\(x_1\\lt x_2\\Rightarrow f(x_1)\\lt f(x_2)\\) for all \\(x_1,x_2\\in K\\) – the graph rises.', 'Đồng biến: \\(x_1\\lt x_2\\Rightarrow f(x_1)\\lt f(x_2)\\) với mọi \\(x_1,x_2\\in K\\) – đồ thị đi lên.'),
  T('Decreasing: \\(x_1\\lt x_2\\Rightarrow f(x_1)\\gt f(x_2)\\) – the graph falls.', 'Nghịch biến: \\(x_1\\lt x_2\\Rightarrow f(x_1)\\gt f(x_2)\\) – đồ thị đi xuống.'),
  T('\\(y=ax+b\\) is increasing on \\(\\mathbb R\\) if \\(a\\gt0\\), decreasing if \\(a\\lt0\\).', '\\(y=ax+b\\) đồng biến trên \\(\\mathbb R\\) nếu \\(a\\gt0\\), nghịch biến nếu \\(a\\lt0\\).')]))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('"Increasing on \\(K\\)" is about an interval, not about a single point. One \\(x\\) with two values of \\(y\\) (e.g. a circle) is <b>not</b> a function.', '"Đồng biến trên \\(K\\)" nói về cả một khoảng, không phải tại một điểm. Một giá trị \\(x\\) ứng với hai giá trị \\(y\\) (như đường tròn) thì <b>không</b> phải hàm số.'))

H1, T1 = [6, 9, 12, 15, 18], [24, 27, 33, 31, 28]
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('A function given by a table', 'Hàm số cho bằng bảng'), T('Temperature in Hà Nội on one day: %s Explain why the temperature \\(T\\) is a function of the time \\(t\\). Give the domain, \\(T(12)\\) and the range.' % HT((('Time (h)', 'Giờ'), H1), (('T (°C)', 'T (°C)'), T1)), 'Nhiệt độ ở Hà Nội trong một ngày: %s Giải thích vì sao nhiệt độ \\(T\\) là hàm số của thời điểm \\(t\\). Nêu tập xác định, \\(T(12)\\) và tập giá trị.' % HT((('Time (h)', 'Giờ'), H1), (('T (°C)', 'T (°C)'), T1))),
  T('Each time has exactly one temperature.', 'Mỗi thời điểm có đúng một nhiệt độ.'), [T('Each \\(t\\) in the table gives one \\(T\\): a function.', 'Mỗi \\(t\\) trong bảng cho một giá trị \\(T\\): đó là hàm số.'), T('\\(D=\\{6;9;12;15;18\\}\\), \\(T(12)=33\\).', '\\(D=\\{6;9;12;15;18\\}\\), \\(T(12)=33\\).')],
  T('Range \\(\\{24;27;28;31;33\\}\\).', 'Tập giá trị \\(\\{24;27;28;31;33\\}\\).'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Domain', 'Tập xác định'), T('Find the domain of \\(y=\\sqrt{x-1}+\\dfrac{2}{x-3}\\).', 'Tìm tập xác định của hàm số \\(y=\\sqrt{x-1}+\\dfrac{2}{x-3}\\).'), T('Root: \\(\\ge0\\); denominator: \\(\\ne0\\).', 'Căn: không âm; mẫu: khác 0.'),
  [T('\\(x-1\\ge0\\iff x\\ge1\\); \\(x-3\\ne0\\iff x\\ne3\\).', '\\(x-1\\ge0\\iff x\\ge1\\); \\(x-3\\ne0\\iff x\\ne3\\).')], T('\\(D=[1;+\\infty)\\setminus\\{3\\}\\).', '\\(D=[1;+\\infty)\\setminus\\{3\\}\\).'))
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Points on a graph', 'Điểm thuộc đồ thị'), T('Which of \\(A(3;3)\\), \\(B(2;1)\\), \\(C(-1;3)\\) lie on the graph of \\(y=x^2-2x\\) (see the figure)? Find the points of the graph with \\(y=0\\).', 'Trong các điểm \\(A(3;3)\\), \\(B(2;1)\\), \\(C(-1;3)\\), điểm nào thuộc đồ thị \\(y=x^2-2x\\) (xem hình)? Tìm các điểm của đồ thị có tung độ bằng 0.'),
  T('Substitute \\(x\\) and compare with \\(y\\).', 'Thay hoành độ, so sánh với tung độ.'), [T('\\(f(3)=3\\) ✓; \\(f(2)=0\\ne1\\) ✗; \\(f(-1)=3\\) ✓.', '\\(f(3)=3\\) ✓; \\(f(2)=0\\ne1\\) ✗; \\(f(-1)=3\\) ✓.'), T('\\(x^2-2x=0\\iff x=0\\) or \\(x=2\\).', '\\(x^2-2x=0\\iff x=0\\) hoặc \\(x=2\\).')],
  T('\\(A\\), \\(C\\) lie on the graph; the points with \\(y=0\\) are \\((0;0)\\), \\((2;0)\\).', '\\(A\\), \\(C\\) thuộc đồ thị; các điểm có tung độ 0 là \\((0;0)\\), \\((2;0)\\).'))
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Increasing or decreasing?', 'Đồng biến hay nghịch biến?'), T('Use the definition to study \\(y=-2x+3\\) on \\(\\mathbb R\\) and \\(y=\\dfrac1x\\) on \\((0;+\\infty)\\).', 'Dùng định nghĩa xét tính đồng biến, nghịch biến của \\(y=-2x+3\\) trên \\(\\mathbb R\\) và \\(y=\\dfrac1x\\) trên \\((0;+\\infty)\\).'),
  T('Take \\(x_1\\lt x_2\\) and compare \\(f(x_1)\\), \\(f(x_2)\\).', 'Lấy \\(x_1\\lt x_2\\), so sánh \\(f(x_1)\\), \\(f(x_2)\\).'),
  [T('\\(f(x_1)-f(x_2)=-2(x_1-x_2)\\gt0\\): decreasing.', '\\(f(x_1)-f(x_2)=-2(x_1-x_2)\\gt0\\): nghịch biến.'), T('\\(\\dfrac1{x_1}-\\dfrac1{x_2}=\\dfrac{x_2-x_1}{x_1x_2}\\gt0\\) for \\(0\\lt x_1\\lt x_2\\): decreasing.', '\\(\\dfrac1{x_1}-\\dfrac1{x_2}=\\dfrac{x_2-x_1}{x_1x_2}\\gt0\\) với \\(0\\lt x_1\\lt x_2\\): nghịch biến.')],
  T('Both functions are decreasing on the given intervals.', 'Cả hai hàm số đều nghịch biến trên các khoảng đã cho.'))
f5 = F(50) * F(18, 10) + F(50) * F(19, 10) + F(50) * F(22, 10); assert f5 == 295
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('An electricity bill', 'Hóa đơn tiền điện'), T('Electricity prices (thousand VND/kWh): first 50 kWh: 1.8; from 51 to 100: 1.9; from 101 to 200: 2.2. Write the bill \\(y=f(x)\\) for \\(0\\le x\\le200\\) kWh and compute \\(f(150)\\).', 'Giá điện (nghìn đồng/kWh): 50 kWh đầu: 1,8; từ 51 đến 100: 1,9; từ 101 đến 200: 2,2. Viết tiền điện \\(y=f(x)\\) với \\(0\\le x\\le200\\) kWh và tính \\(f(150)\\).'),
  T('A piecewise function: each tier has its own price.', 'Hàm số cho bởi nhiều công thức: mỗi bậc một giá.'),
  [T('\\(0\\le x\\le50\\): \\(f(x)=1.8x\\); \\(50\\lt x\\le100\\): \\(f(x)=90+1.9(x-50)\\); \\(100\\lt x\\le200\\): \\(f(x)=185+2.2(x-100)\\).', '\\(0\\le x\\le50\\): \\(f(x)=1{,}8x\\); \\(50\\lt x\\le100\\): \\(f(x)=90+1{,}9(x-50)\\); \\(100\\lt x\\le200\\): \\(f(x)=185+2{,}2(x-100)\\).'),
   T('\\(f(150)=185+2.2\\cdot50=295\\).', '\\(f(150)=185+2{,}2\\cdot50=295\\).')],
  T('\\(f(150)=295\\) thousand VND; \\(f\\) is increasing (using more always costs more).', '\\(f(150)=295\\) nghìn đồng; \\(f\\) đồng biến (dùng nhiều điện hơn thì trả nhiều tiền hơn).'))

def lvl(P):
    k, a, b = P['dom']
    if k == 'sqrt': f, ok, wr = '\\sqrt{%s}' % poly([a, b]), '[%s;\\,+\\infty)' % fr(F(-b, a)), ['(%s;\\,+\\infty)' % fr(F(-b, a)), '(-\\infty;\\,%s]' % fr(F(-b, a)), '\\mathbb R']
    else: f, ok, wr = '\\dfrac{\\sqrt{x%+d}}{x-%d}' % (-a, b), '[%d;\\,+\\infty)\\setminus\\{%d\\}' % (a, b), ['[%d;\\,+\\infty)' % a, '\\mathbb R\\setminus\\{%d\\}' % b, '(%d;\\,+\\infty)' % a]
    o1 = M4(1, 'The domain of \\(y=%s\\) is…' % f, 'Tập xác định của hàm số \\(y=%s\\) là…' % f, ok, wr, 'Square root \\(\\ge0\\), denominator \\(\\ne0\\).', 'Biểu thức dưới căn không âm, mẫu khác 0.')
    (base, km1, p, d) = P['fare']; cost = base + max(0, d - km1) * p
    o2 = M4(2, 'A delivery service charges %d thousand VND for the first %d km and %d thousand VND for each further km. The charge for %d km is…' % (base, km1, p, d), 'Một dịch vụ giao hàng thu %d nghìn đồng cho %d km đầu và %d nghìn đồng cho mỗi km tiếp theo. Giao hàng %d km phải trả…' % (base, km1, p, d),
            '%d\\ \\text{(nghìn đồng)}' % cost, ['%d\\ \\text{(nghìn đồng)}' % x for x in (base + d * p, d * p, cost + p, cost - p, cost + 2 * p)], '\\(f(x)=%d+%d(x-%d)\\) for \\(x\\gt%d\\): \\(f(%d)=%d\\).' % (base, p, km1, km1, d, cost), '\\(f(x)=%d+%d(x-%d)\\) khi \\(x\\gt%d\\): \\(f(%d)=%d\\).' % (base, p, km1, km1, d, cost))
    a3, b3 = P['lin']; inc = a3 > 0
    o3 = M4(3, 'The function \\(y=%s\\) on \\(\\mathbb R\\) is…' % poly([a3, b3]), 'Trên \\(\\mathbb R\\), hàm số \\(y=%s\\)…' % poly([a3, b3]), S.TT('increasing' if inc else 'decreasing', 'đồng biến' if inc else 'nghịch biến'),
            [S.TT('decreasing' if inc else 'increasing', 'nghịch biến' if inc else 'đồng biến'), S.TT('constant', 'là hàm hằng'), S.TT('increasing then decreasing', 'đồng biến rồi nghịch biến')], 'The coefficient \\(a=%s\\) is %s.' % (fr(F(a3)), 'positive' if inc else 'negative'), 'Hệ số \\(a=%s\\) %s.' % (fr(F(a3)), 'dương' if inc else 'âm'))
    cs, pt = P['pt']; ok4 = pt[1] == cs[0] * pt[0] ** 2 + cs[1] * pt[0] + cs[2]
    t4 = tf(4, 'The point \\((%d;\\,%d)\\) lies on the graph of \\(y=%s\\).' % (pt[0], pt[1], poly(cs)), 'Điểm \\((%d;\\,%d)\\) thuộc đồ thị hàm số \\(y=%s\\).' % (pt[0], pt[1], poly(cs)), ok4,
            '\\(f(%d)=%d\\).' % (pt[0], cs[0] * pt[0] ** 2 + cs[1] * pt[0] + cs[2]), '\\(f(%d)=%d\\).' % (pt[0], cs[0] * pt[0] ** 2 + cs[1] * pt[0] + cs[2]))
    c5, ok5 = P['rng']; claim = '[%d;\\,+\\infty)' % c5 if ok5 else '(%d;\\,+\\infty)' % c5
    t5 = tf(5, 'The range of \\(y=x^2%+d\\) is \\(%s\\).' % (c5, claim), 'Tập giá trị của hàm số \\(y=x^2%+d\\) là \\(%s\\).' % (c5, claim), ok5, '\\(x^2\\ge0\\) with equality at \\(x=0\\), so \\(y\\ge%d\\) and \\(y=%d\\) is reached.' % (c5, c5), '\\(x^2\\ge0\\), dấu bằng tại \\(x=0\\) nên \\(y\\ge%d\\) và đạt \\(y=%d\\).' % (c5, c5))
    (x1, f1, x2, f2), xq = P['pw']; v6 = f1(xq) if xq < x1 else f2(xq)
    s6 = sh(6, '\\(f(x)=%s\\) if \\(x\\lt%d\\) and \\(f(x)=%s\\) if \\(x\\ge%d\\). Find \\(f(%d)+f(%d)\\).' % (P['pwt'][0], x1, P['pwt'][1], x1, xq, x2), 'Cho \\(f(x)=%s\\) khi \\(x\\lt%d\\), \\(f(x)=%s\\) khi \\(x\\ge%d\\). Tính \\(f(%d)+f(%d)\\).' % (P['pwt'][0], x1, P['pwt'][1], x1, xq, x2),
            v6 + (f1(x2) if x2 < x1 else f2(x2)), '\\(f(%d)=%d\\), \\(f(%d)=%d\\).' % (xq, v6, x2, f1(x2) if x2 < x1 else f2(x2)), '\\(f(%d)=%d\\), \\(f(%d)=%d\\).' % (xq, v6, x2, f1(x2) if x2 < x1 else f2(x2)))
    kwh = P['kwh']; tiers = [(50, F('1.8')), (50, F('1.9')), (100, F('2.2'))]; left = kwh; bill = F(0)
    for lim, pr in tiers: u = min(left, lim); bill += u * pr; left -= u
    assert left == 0
    s7 = sh(7, 'With the prices of Example 5, how much (thousand VND) does a family using %d kWh pay?' % kwh, 'Với giá điện ở Ví dụ 5, gia đình dùng %d kWh phải trả bao nhiêu nghìn đồng?' % kwh, D(bill).replace('{,}', '.'), 'Add the tiers: \\(%s\\).' % D(bill).replace('{,}', '.'), 'Cộng từng bậc: \\(%s\\).' % D(bill))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
PP = [dict(dom=('sqrt', 2, -6), fare=(15, 2, 5, 9), lin=(-3, 1), pt=([1, -3, 2], (3, 2)), rng=(2, True), pw=((0, lambda x: 2 * x + 1, 3, lambda x: x * x), -2), pwt=('2x+1', 'x^2'), kwh=80),
      dict(dom=('frac', 2, 5), fare=(20, 3, 4, 10), lin=(F(1, 2), -4), pt=([2, 1, -3], (-2, 3)), rng=(-1, False), pw=((1, lambda x: 3 - x, 4, lambda x: 2 * x - 1), -1), pwt=('3-x', '2x-1'), kwh=130),
      dict(dom=('frac', -1, 3), fare=(12, 1, 6, 15), lin=(2, 7), pt=([-1, 4, 0], (5, -6)), rng=(-3, True), pw=((2, lambda x: x * x - 1, 5, lambda x: 4 - x), 0), pwt=('x^2-1', '4-x'), kwh=45)]
practice = three(lvl, PP)
practice = with_self(practice, S.M15S10, start=8)
mistakes = [('<b>Forgetting a condition.</b> \\(\\dfrac{\\sqrt{x-1}}{x-3}\\) needs both \\(x\\ge1\\) and \\(x\\ne3\\).', '<b>Thiếu điều kiện.</b> \\(\\dfrac{\\sqrt{x-1}}{x-3}\\) cần cả \\(x\\ge1\\) và \\(x\\ne3\\).'),
            ('<b>Using the wrong piece.</b> In a piecewise function, first decide which formula the value of \\(x\\) uses.', '<b>Dùng sai công thức.</b> Với hàm cho bởi nhiều công thức, phải xét \\(x\\) thuộc phần nào trước.'),
            ('<b>Strict or not.</b> \\(\\sqrt{x-1}\\) is defined at \\(x=1\\): write \\([1;+\\infty)\\), not \\((1;+\\infty)\\).', '<b>Nhầm dấu ngoặc.</b> \\(\\sqrt{x-1}\\) xác định tại \\(x=1\\): viết \\([1;+\\infty)\\), không phải \\((1;+\\infty)\\).'),
            ('<b>Monotonic on \\(\\mathbb R\\).</b> \\(\\dfrac1x\\) is decreasing on \\((-\\infty;0)\\) and on \\((0;+\\infty)\\), but not on \\(\\mathbb R\\setminus\\{0\\}\\).', '<b>Đơn điệu trên cả tập.</b> \\(\\dfrac1x\\) nghịch biến trên \\((-\\infty;0)\\) và trên \\((0;+\\infty)\\), nhưng không nghịch biến trên \\(\\mathbb R\\setminus\\{0\\}\\).')]
summary = [('A function gives each \\(x\\in D\\) exactly one \\(y=f(x)\\).', 'Hàm số cho mỗi \\(x\\in D\\) đúng một giá trị \\(y=f(x)\\).'),
           ('Domain: denominators \\(\\ne0\\), square roots of \\(\\ge0\\).', 'Tập xác định: mẫu khác 0, biểu thức dưới căn không âm.'),
           ('\\(M(x_0;y_0)\\) on the graph \\(\\iff y_0=f(x_0)\\).', '\\(M(x_0;y_0)\\) thuộc đồ thị \\(\\iff y_0=f(x_0)\\).'),
           ('Increasing: graph rises; decreasing: graph falls. Key words: function, domain, range, graph, increasing, decreasing.', 'Đồng biến: đồ thị đi lên; nghịch biến: đồ thị đi xuống. Từ cần nhớ: function, domain, range, graph, increasing, decreasing.')]
checks = [('I can tell whether a rule is a function.', 'Em nhận biết được một quy tắc có là hàm số hay không.'), ('I can find the domain of a function.', 'Em tìm được tập xác định của hàm số.'),
          ('I can read a graph.', 'Em đọc được đồ thị hàm số.'), ('I can write a piecewise function for a real situation.', 'Em lập được hàm số nhiều công thức cho tình huống thực tế.')]
LL('g10-func-01', 'Functions', CV, ('Functions and Graphs', 'Hàm số, đồ thị và ứng dụng'), 'functions', 'functions', 150, 'Beginner', 60, ('linear functions, intervals', 'hàm số bậc nhất, khoảng và đoạn'),
   'Functions given by tables, graphs and formulas; domain, range, graph, increasing and decreasing functions; piecewise functions.', 'Bài 15 – Hàm số, tập xác định, tập giá trị, đồ thị, hàm số đồng biến, nghịch biến; hàm số cho bởi nhiều công thức.',
   ['function', 'domain', 'range', 'graph', 'increasing'], ['hàm số', 'tập xác định', 'tập giá trị', 'đồ thị', 'đồng biến'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g10-stats-03'])
