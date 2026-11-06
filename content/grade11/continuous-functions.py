# -*- coding: utf-8 -*-
"""g11-limits-05 = Toán 11 KNTT, Bài 17: Hàm số liên tục. Mã ngân hàng câu hỏi: TOAN11-C5-B17."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g11f as S
from sp_g11e import LX, poly

CV = 'Hàm số liên tục'
vocab = defs(CV, [
 ('contpt', 'continuous at a point', 'liên tục tại một điểm', '\\(f\\) is continuous at \\(x_0\\) when \\(\\lim\\limits_{x\\to x_0}f(x)=f(x_0)\\).', '\\(f\\) liên tục tại \\(x_0\\) khi \\(\\lim\\limits_{x\\to x_0}f(x)=f(x_0)\\).', 'The function is continuous at 2.', ''),
 ('discont', 'discontinuous', 'gián đoạn', 'not continuous at a point: the graph is broken there.', 'không liên tục tại một điểm: đồ thị bị đứt tại đó.', 'The function is discontinuous at 1.', ''),
 ('contint', 'continuous on an interval', 'liên tục trên một khoảng', 'continuous at every point of the interval (on \\([a;b]\\): also \\(\\lim\\limits_{x\\to a^+}f=f(a)\\), \\(\\lim\\limits_{x\\to b^-}f=f(b)\\)); the graph is one unbroken curve.', 'liên tục tại mọi điểm của khoảng (trên \\([a;b]\\): thêm \\(\\lim\\limits_{x\\to a^+}f=f(a)\\), \\(\\lim\\limits_{x\\to b^-}f=f(b)\\)); đồ thị là một đường liền.', 'A polynomial is continuous on the whole real line.', ''),
 ('ivt', 'intermediate value theorem', 'định lí giá trị trung gian', 'if \\(f\\) is continuous on \\([a;b]\\) and \\(f(a)f(b)\\lt0\\), then \\(f(c)=0\\) for some \\(c\\in(a;b)\\).', 'nếu \\(f\\) liên tục trên \\([a;b]\\) và \\(f(a)f(b)\\lt0\\) thì có \\(c\\in(a;b)\\) với \\(f(c)=0\\).', 'By the intermediate value theorem the equation has a root.', ''),
 ('elemf', 'elementary function', 'hàm số sơ cấp', 'a function built from polynomials, fractions, roots and trigonometric functions; it is continuous on each interval of its domain.', 'hàm số tạo từ đa thức, phân thức, căn thức, hàm lượng giác; liên tục trên từng khoảng của tập xác định.', 'Rational functions are elementary functions.', '')])
goals = [('decide whether a function is continuous at a point and find a parameter that makes it continuous;', 'xét tính [[liên tục tại một điểm]] của hàm số và tìm tham số để hàm số liên tục;'),
         ('state the intervals on which elementary functions are continuous;', 'chỉ ra các khoảng mà [[hàm số sơ cấp]] [[liên tục trên một khoảng]];'),
         ('use the intermediate value theorem to show that an equation has roots;', 'dùng [[định lí giá trị trung gian]] để chứng minh phương trình có nghiệm;'),
         ('recognise continuous processes in real life.', 'nhận biết các quá trình biến đổi liên tục trong thực tế.')]
phrases = [('<b>The function is continuous at \\(x\\) equals two.</b>', 'Hàm số liên tục tại \\(x=2\\).'), ('<b>The graph is an unbroken curve.</b>', 'Đồ thị là một đường liền nét.'), ('<b>The function is discontinuous at one.</b>', 'Hàm số gián đoạn tại 1.'),
           ('<b>\\(f(0)\\) and \\(f(1)\\) have opposite signs.</b>', '\\(f(0)\\) và \\(f(1)\\) trái dấu.'), ('<b>The equation has at least one root in the interval.</b>', 'Phương trình có ít nhất một nghiệm trong khoảng đó.')]
review = T('From Bài 16: \\(\\lim\\limits_{x\\to x_0}f(x)=L\\iff\\lim\\limits_{x\\to x_0^-}f(x)=\\lim\\limits_{x\\to x_0^+}f(x)=L\\); the form \\(\\frac00\\) is removed by factorising. Domain: denominators \\(\\ne0\\), expressions under \\(\\sqrt{\\ }\\) \\(\\ge0\\).',
           'Từ Bài 16: \\(\\lim\\limits_{x\\to x_0}f(x)=L\\iff\\lim\\limits_{x\\to x_0^-}f(x)=\\lim\\limits_{x\\to x_0^+}f(x)=L\\); khử dạng \\(\\frac00\\) bằng phân tích nhân tử. Tập xác định: mẫu khác 0, biểu thức dưới căn bậc hai không âm.')
theory = '<h3>17.1 %s</h3>' % TI('Continuity at a point', 'Hàm số liên tục tại một điểm')
theory += BOX('blue', ('Definition', 'Định nghĩa'), T('Let \\(f\\) be defined on an interval \\(K\\) containing \\(x_0\\). \\(f\\) is continuous at \\(x_0\\) if \\[\\lim\\limits_{x\\to x_0}f(x)=f(x_0).\\] Three things are needed: \\(f(x_0)\\) exists, the limit exists, and they are equal. Otherwise \\(f\\) is discontinuous at \\(x_0\\).',
  'Cho \\(f\\) xác định trên khoảng \\(K\\) chứa \\(x_0\\). \\(f\\) liên tục tại \\(x_0\\) nếu \\[\\lim\\limits_{x\\to x_0}f(x)=f(x_0).\\] Cần đủ ba điều: \\(f(x_0)\\) xác định, giới hạn tồn tại, và hai số đó bằng nhau. Ngược lại, \\(f\\) gián đoạn tại \\(x_0\\).'))
theory += GRAPH({'view': [-3, 4, -3, 5], 'functions': [{'f': 'x^2', 'label': 'y = x² (x < 1)', 'domain': [-3, 1]}, {'f': '2*x-3', 'label': 'y = 2x − 3 (x ≥ 1)', 'domain': [1, 4]}],
  'points': [{'x': 1, 'y': 1, 'label': '(1; 1)', 'open': True}, {'x': 1, 'y': -1, 'label': '(1; −1)'}]},
  cap=('\\(f(x)=x^2\\) for \\(x\\lt1\\), \\(f(x)=2x-3\\) for \\(x\\ge1\\): the left limit is 1, the right limit is \\(-1\\). The graph "jumps" – \\(f\\) is discontinuous at 1.', '\\(f(x)=x^2\\) khi \\(x\\lt1\\), \\(f(x)=2x-3\\) khi \\(x\\ge1\\): giới hạn trái bằng 1, giới hạn phải bằng \\(-1\\). Đồ thị bị "nhảy" – \\(f\\) gián đoạn tại 1.'),
  alt=('A broken graph: a parabola up to x = 1 and a line starting lower at x = 1', 'Đồ thị bị đứt tại x = 1'), height=300)
theory += BOX('mint', ('Piecewise functions', 'Hàm số cho bởi nhiều công thức'), T('For \\(f(x)=g(x)\\) when \\(x\\lt x_0\\) and \\(f(x)=h(x)\\) when \\(x\\ge x_0\\): \\(f\\) is continuous at \\(x_0\\iff\\lim\\limits_{x\\to x_0^-}g(x)=h(x_0)\\) (and \\(\\lim\\limits_{x\\to x_0^+}h(x)=h(x_0)\\), automatic when \\(h\\) is a polynomial).',
  'Với \\(f(x)=g(x)\\) khi \\(x\\lt x_0\\), \\(f(x)=h(x)\\) khi \\(x\\ge x_0\\): \\(f\\) liên tục tại \\(x_0\\iff\\lim\\limits_{x\\to x_0^-}g(x)=h(x_0)\\) (và \\(\\lim\\limits_{x\\to x_0^+}h(x)=h(x_0)\\), luôn đúng khi \\(h\\) là đa thức).'))
theory += '<h3>17.2 %s</h3>' % TI('Continuity on an interval. Elementary functions', 'Hàm số liên tục trên một khoảng. Các hàm số sơ cấp')
theory += BOX('mint', ('Facts', 'Kết quả'), UL([T('Polynomials, \\(\\sin x\\), \\(\\cos x\\) are continuous on \\(\\mathbb R\\).', 'Đa thức, \\(\\sin x\\), \\(\\cos x\\) liên tục trên \\(\\mathbb R\\).'),
  T('Rational functions, \\(\\sqrt{x}\\), \\(\\tan x\\), \\(\\cot x\\) are continuous on each interval of their domain.', 'Phân thức hữu tỉ, \\(\\sqrt{x}\\), \\(\\tan x\\), \\(\\cot x\\) liên tục trên từng khoảng của tập xác định.'),
  T('If \\(f,g\\) are continuous at \\(x_0\\) then so are \\(f\\pm g\\), \\(fg\\) and \\(\\dfrac fg\\) (when \\(g(x_0)\\ne0\\)).', 'Nếu \\(f,g\\) liên tục tại \\(x_0\\) thì \\(f\\pm g\\), \\(fg\\), \\(\\dfrac fg\\) (khi \\(g(x_0)\\ne0\\)) cũng liên tục tại \\(x_0\\).')]))
theory += BOX('blue', ('Intermediate value theorem', 'Định lí giá trị trung gian'), T('If \\(f\\) is continuous on \\([a;b]\\) and \\(f(a)\\cdot f(b)\\lt0\\), then there is at least one \\(c\\in(a;b)\\) with \\(f(c)=0\\). More generally, \\(f\\) takes every value between \\(f(a)\\) and \\(f(b)\\).',
  'Nếu \\(f\\) liên tục trên \\([a;b]\\) và \\(f(a)\\cdot f(b)\\lt0\\) thì có ít nhất một \\(c\\in(a;b)\\) sao cho \\(f(c)=0\\). Tổng quát, \\(f\\) nhận mọi giá trị nằm giữa \\(f(a)\\) và \\(f(b)\\).'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('The theorem needs continuity on the <b>closed</b> interval. \\(f(x)=\\dfrac1x\\) has \\(f(-1)\\lt0\\lt f(1)\\) but no root: it is not continuous at 0. The theorem says "at least one" root – it does not count roots.',
  'Định lí cần liên tục trên <b>đoạn</b>. \\(f(x)=\\dfrac1x\\) có \\(f(-1)\\lt0\\lt f(1)\\) nhưng không có nghiệm vì không liên tục tại 0. Định lí chỉ khẳng định "ít nhất một" nghiệm, không cho biết số nghiệm.'))

assert all(((x * x - 4) / (x - 2)) == x + 2 for x in (F(1), F(3), F(5, 2)))
assert 2 * 4 - 2 == 2 * 2 + 2 and 4 + 2 == 6
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Continuity at a point', 'Xét tính liên tục tại một điểm'), T('\\(f(x)=\\dfrac{x^2-4}{x-2}\\) for \\(x\\ne2\\) and \\(f(2)=4\\). Is \\(f\\) continuous at \\(x=2\\)? What if \\(f(2)=3\\)?', 'Cho \\(f(x)=\\dfrac{x^2-4}{x-2}\\) khi \\(x\\ne2\\) và \\(f(2)=4\\). Hàm số có liên tục tại \\(x=2\\) không? Nếu \\(f(2)=3\\) thì sao?'),
  T('Compare \\(\\lim\\limits_{x\\to2}f(x)\\) with \\(f(2)\\).', 'So sánh \\(\\lim\\limits_{x\\to2}f(x)\\) với \\(f(2)\\).'),
  [T('\\(\\lim\\limits_{x\\to2}\\dfrac{(x-2)(x+2)}{x-2}=\\lim\\limits_{x\\to2}(x+2)=4\\).', '\\(\\lim\\limits_{x\\to2}\\dfrac{(x-2)(x+2)}{x-2}=\\lim\\limits_{x\\to2}(x+2)=4\\).'), T('\\(4=f(2)\\): continuous. If \\(f(2)=3\\ne4\\): discontinuous.', '\\(4=f(2)\\): liên tục. Nếu \\(f(2)=3\\ne4\\): gián đoạn.')],
  T('Continuous when \\(f(2)=4\\); discontinuous when \\(f(2)=3\\).', 'Liên tục khi \\(f(2)=4\\); gián đoạn khi \\(f(2)=3\\).'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Find the parameter', 'Tìm tham số'), T('\\(f(x)=x^2+x\\) for \\(x\\lt2\\), \\(f(x)=mx-2\\) for \\(x\\ge2\\). Find \\(m\\) so that \\(f\\) is continuous on \\(\\mathbb R\\).', 'Cho \\(f(x)=x^2+x\\) khi \\(x\\lt2\\), \\(f(x)=mx-2\\) khi \\(x\\ge2\\). Tìm \\(m\\) để hàm số liên tục trên \\(\\mathbb R\\).'),
  T('Each piece is a polynomial; only \\(x=2\\) needs checking.', 'Mỗi phần là đa thức; chỉ cần xét tại \\(x=2\\).'),
  [T('\\(\\lim\\limits_{x\\to2^-}(x^2+x)=6\\); \\(f(2)=\\lim\\limits_{x\\to2^+}(mx-2)=2m-2\\).', '\\(\\lim\\limits_{x\\to2^-}(x^2+x)=6\\); \\(f(2)=\\lim\\limits_{x\\to2^+}(mx-2)=2m-2\\).'), T('\\(2m-2=6\\iff m=4\\).', '\\(2m-2=6\\iff m=4\\).')], T('\\(m=4\\).', '\\(m=4\\).'))
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Intervals of continuity', 'Khoảng liên tục'), T('Find the intervals on which \\(y=\\dfrac{x+1}{x^2-5x+6}\\) and \\(y=\\sqrt{4-x}\\) are continuous.', 'Tìm các khoảng mà hàm số \\(y=\\dfrac{x+1}{x^2-5x+6}\\) và \\(y=\\sqrt{4-x}\\) liên tục.'),
  T('Elementary functions are continuous on their domain.', 'Hàm số sơ cấp liên tục trên tập xác định của nó.'),
  [T('\\(x^2-5x+6=(x-2)(x-3)\\ne0\\iff x\\ne2,\\ x\\ne3\\).', '\\(x^2-5x+6=(x-2)(x-3)\\ne0\\iff x\\ne2,\\ x\\ne3\\).'), T('\\(4-x\\ge0\\iff x\\le4\\).', '\\(4-x\\ge0\\iff x\\le4\\).')],
  T('The first on \\((-\\infty;2)\\), \\((2;3)\\), \\((3;+\\infty)\\); the second on \\((-\\infty;4]\\).', 'Hàm thứ nhất liên tục trên \\((-\\infty;2)\\), \\((2;3)\\), \\((3;+\\infty)\\); hàm thứ hai liên tục trên \\((-\\infty;4]\\).'))
g = lambda x: x ** 3 - 3 * x + 1
assert (g(-2), g(0), g(1), g(2)) == (-1, 1, -1, 3)
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Proving that roots exist', 'Chứng minh phương trình có nghiệm'), T('Prove that \\(x^3-3x+1=0\\) has exactly three real roots in \\((-2;2)\\).', 'Chứng minh phương trình \\(x^3-3x+1=0\\) có đúng ba nghiệm thực thuộc \\((-2;2)\\).'),
  T('Find sign changes of \\(f(x)=x^3-3x+1\\) (continuous on \\(\\mathbb R\\)).', 'Tìm các lần đổi dấu của \\(f(x)=x^3-3x+1\\) (liên tục trên \\(\\mathbb R\\)).'),
  [T('\\(f(-2)=-1\\), \\(f(0)=1\\), \\(f(1)=-1\\), \\(f(2)=3\\).', '\\(f(-2)=-1\\), \\(f(0)=1\\), \\(f(1)=-1\\), \\(f(2)=3\\).'), T('Sign changes on \\((-2;0)\\), \\((0;1)\\), \\((1;2)\\): at least one root in each.', 'Đổi dấu trên \\((-2;0)\\), \\((0;1)\\), \\((1;2)\\): mỗi khoảng có ít nhất một nghiệm.'), T('A cubic equation has at most 3 roots.', 'Phương trình bậc ba có không quá 3 nghiệm.')],
  T('Exactly three roots, one in each of \\((-2;0)\\), \\((0;1)\\), \\((1;2)\\).', 'Đúng ba nghiệm, mỗi khoảng \\((-2;0)\\), \\((0;1)\\), \\((1;2)\\) có một nghiệm.'))
assert 20 + 8 * 10 == 100
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Boiling water', 'Đun nước'), T('A kettle heats water: \\(T(t)=20+8t\\) (°C) for \\(0\\le t\\le10\\) (minutes) and then keeps it at \\(T(t)=a\\) for \\(10\\lt t\\le15\\). Temperature changes continuously. Find \\(a\\), and explain why at some moment the water was exactly 61 °C.', 'Ấm đun nước: \\(T(t)=20+8t\\) (°C) với \\(0\\le t\\le10\\) (phút), sau đó giữ ở \\(T(t)=a\\) với \\(10\\lt t\\le15\\). Nhiệt độ thay đổi liên tục. Tìm \\(a\\) và giải thích vì sao có thời điểm nước đúng 61 °C.'),
  T('Continuity at \\(t=10\\); then the intermediate value theorem on \\([0;10]\\).', 'Liên tục tại \\(t=10\\); rồi dùng định lí giá trị trung gian trên \\([0;10]\\).'),
  [T('\\(\\lim\\limits_{t\\to10^+}T=a\\) must equal \\(T(10)=20+80=100\\), so \\(a=100\\).', '\\(\\lim\\limits_{t\\to10^+}T=a\\) phải bằng \\(T(10)=20+80=100\\) nên \\(a=100\\).'), T('\\(T\\) is continuous on \\([0;10]\\) with \\(T(0)=20\\lt61\\lt100=T(10)\\): some \\(t\\) gives \\(T(t)=61\\) (here \\(t=5{,}125\\) min).', '\\(T\\) liên tục trên \\([0;10]\\), \\(T(0)=20\\lt61\\lt100=T(10)\\) nên có \\(t\\) với \\(T(t)=61\\) (cụ thể \\(t=5{,}125\\) phút).')],
  T('\\(a=100\\) °C (boiling point); the water passes through every temperature between 20 °C and 100 °C.', '\\(a=100\\) °C (nhiệt độ sôi); nước đi qua mọi nhiệt độ từ 20 °C đến 100 °C.'))
assert F(61 - 20, 8) == F(41, 8) == F(5125, 1000)

def lvl(P):
    a, b = P['rem']; v1 = a - b
    o1 = M4(1, '\\(f(x)=\\dfrac{%s}{x%+d}\\) (\\(x\\ne%d\\)), \\(f(%d)=m\\). \\(f\\) is continuous at \\(%d\\) when \\(m=\\)…' % (poly([1, -(a + b), a * b], 'x'), -a, a, a, a), 'Cho \\(f(x)=\\dfrac{%s}{x%+d}\\) (\\(x\\ne%d\\)), \\(f(%d)=m\\). Hàm số liên tục tại \\(%d\\) khi \\(m=\\)…' % (poly([1, -(a + b), a * b], 'x'), -a, a, a, a),
            str(v1), [str(a + b), str(b - a), '0', str(v1 + 2)], '\\(m=\\lim\\limits_{x\\to%d}(x%+d)=%d\\).' % (a, -b, v1), '\\(m=\\lim\\limits_{x\\to%d}(x%+d)=%d\\).' % (a, -b, v1))
    x0, k, p, q = P['pw']; L = k * x0 * x0 + p; m2 = L - q * x0
    o2 = M4(2, '\\(f(x)=%s\\) for \\(x\\lt%d\\), \\(f(x)=%s+m\\) for \\(x\\ge%d\\). \\(f\\) is continuous on \\(\\mathbb R\\) when \\(m=\\)…' % (poly([k, 0, p], 'x'), x0, poly([q, 0], 'x'), x0), 'Cho \\(f(x)=%s\\) khi \\(x\\lt%d\\), \\(f(x)=%s+m\\) khi \\(x\\ge%d\\). Hàm số liên tục trên \\(\\mathbb R\\) khi \\(m=\\)…' % (poly([k, 0, p], 'x'), x0, poly([q, 0], 'x'), x0),
            str(m2), [str(L), str(L + q * x0), str(m2 + 1), str(-m2 - 1)], '\\(%d=%d+m\\iff m=%d\\).' % (L, q * x0, m2), '\\(%d=%d+m\\iff m=%d\\).' % (L, q * x0, m2))
    r1, r2 = P['dom']
    o3 = M4(3, '\\(y=\\dfrac{2x-1}{%s}\\) is continuous on…' % poly([1, -(r1 + r2), r1 * r2], 'x'), 'Hàm số \\(y=\\dfrac{2x-1}{%s}\\) liên tục trên…' % poly([1, -(r1 + r2), r1 * r2], 'x'),
            '\\((-\\infty;%d)\\), \\((%d;%d)\\), \\((%d;+\\infty)\\)' % (r1, r1, r2, r2), ['\\(\\mathbb R\\)', '\\((%d;%d)\\)' % (r1, r2), '\\(\\mathbb R\\setminus\\{\\tfrac12\\}\\)', '\\((-\\infty;%d)\\), \\((%d;+\\infty)\\)' % (-r2, -r1)],
            'Denominator \\((x%+d)(x%+d)\\ne0\\).' % (-r1, -r2), 'Mẫu \\((x%+d)(x%+d)\\ne0\\).' % (-r1, -r2))
    cs, (u, w), truth = P['ivt']; f4 = lambda x: sum(c * x ** (len(cs) - 1 - i) for i, c in enumerate(cs))
    assert (f4(u) * f4(w) < 0) == truth
    t4 = tf(4, 'Since \\(f(%d)\\cdot f(%d)\\lt0\\) for \\(f(x)=%s\\), the equation \\(f(x)=0\\) has a root in \\((%d;%d)\\).' % (u, w, poly(cs, 'x'), u, w) if truth else 'For \\(f(x)=%s\\), \\(f(%d)\\cdot f(%d)\\lt0\\).' % (poly(cs, 'x'), u, w),
            'Vì \\(f(%d)\\cdot f(%d)\\lt0\\) với \\(f(x)=%s\\) nên phương trình \\(f(x)=0\\) có nghiệm thuộc \\((%d;%d)\\).' % (u, w, poly(cs, 'x'), u, w) if truth else 'Với \\(f(x)=%s\\) thì \\(f(%d)\\cdot f(%d)\\lt0\\).' % (poly(cs, 'x'), u, w), truth,
            '\\(f(%d)=%d\\), \\(f(%d)=%d\\).' % (u, f4(u), w, f4(w)), '\\(f(%d)=%d\\), \\(f(%d)=%d\\).' % (u, f4(u), w, f4(w)))
    c5, v5 = P['jump']
    t5 = tf(5, '\\(f(x)=\\dfrac{x^2-%d}{x-%d}\\) for \\(x\\ne%d\\), \\(f(%d)=%d\\) is continuous at \\(%d\\).' % (c5 * c5, c5, c5, c5, v5, c5), 'Hàm số \\(f(x)=\\dfrac{x^2-%d}{x-%d}\\) khi \\(x\\ne%d\\), \\(f(%d)=%d\\) liên tục tại \\(%d\\).' % (c5 * c5, c5, c5, c5, v5, c5), v5 == 2 * c5,
            'The limit is \\(%d+%d=%d\\); \\(f(%d)=%d\\).' % (c5, c5, 2 * c5, c5, v5), 'Giới hạn bằng \\(%d+%d=%d\\); \\(f(%d)=%d\\).' % (c5, c5, 2 * c5, c5, v5))
    x6, s6v = P['sq']; m6 = s6v
    s6 = sh(6, '\\(f(x)=\\dfrac{\\sqrt{x%+d}-%d}{x%+d}\\) for \\(x\\ne%d\\), \\(f(%d)=\\dfrac{1}{m}\\). Find \\(m\\) for continuity at \\(%d\\).' % (s6v * s6v - x6, s6v, -x6, x6, x6, x6), 'Cho \\(f(x)=\\dfrac{\\sqrt{x%+d}-%d}{x%+d}\\) khi \\(x\\ne%d\\), \\(f(%d)=\\dfrac{1}{m}\\). Tìm \\(m\\) để hàm số liên tục tại \\(%d\\).' % (s6v * s6v - x6, s6v, -x6, x6, x6, x6),
            2 * m6, 'Conjugate: limit \\(=\\dfrac1{\\sqrt{%d}+%d}=\\dfrac1{%d}\\), so \\(m=%d\\).' % (s6v * s6v, s6v, 2 * s6v, 2 * s6v), 'Nhân liên hợp: giới hạn \\(=\\dfrac1{\\sqrt{%d}+%d}=\\dfrac1{%d}\\) nên \\(m=%d\\).' % (s6v * s6v, s6v, 2 * s6v, 2 * s6v))
    T0, r7, t7 = P['heat']; a7 = T0 + r7 * t7
    s7 = sh(7, 'Water is heated: \\(T(t)=%d+%dt\\) (°C) for \\(0\\le t\\le%d\\) min, then \\(T(t)=a\\) for \\(t\\gt%d\\). \\(T\\) is continuous. Find \\(a\\).' % (T0, r7, t7, t7), 'Đun nước: \\(T(t)=%d+%dt\\) (°C) với \\(0\\le t\\le%d\\) phút, sau đó \\(T(t)=a\\) với \\(t\\gt%d\\). \\(T\\) liên tục. Tìm \\(a\\).' % (T0, r7, t7, t7),
            a7, '\\(a=T(%d)=%d+%d\\cdot%d=%d\\).' % (t7, T0, r7, t7, a7), '\\(a=T(%d)=%d+%d\\cdot%d=%d\\).' % (t7, T0, r7, t7, a7))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
PP = [dict(rem=(3, 1), pw=(1, 1, 2, 3), dom=(1, 4), ivt=([1, 0, -4, 1], (0, 1), True), jump=(3, 6), sq=(1, 2), heat=(25, 15, 5)),
      dict(rem=(-2, 4), pw=(2, 2, -1, 1), dom=(-1, 3), ivt=([1, 0, 1, 3], (0, 1), False), jump=(2, 3), sq=(5, 3), heat=(18, 10, 8)),
      dict(rem=(5, -1), pw=(-1, 3, 1, -2), dom=(-3, 2), ivt=([2, 0, -3, -1], (1, 2), True), jump=(4, 7), sq=(-3, 1), heat=(22, 6, 12))]
practice = three(lvl, PP)
practice = with_self(practice, S.M17S11, start=8)
mistakes = [('<b>Only checking that the limit exists.</b> Continuity also needs \\(\\lim f=f(x_0)\\).', '<b>Chỉ kiểm tra giới hạn tồn tại.</b> Liên tục còn cần \\(\\lim f=f(x_0)\\).'),
            ('<b>Using the wrong piece.</b> For \\(x\\to x_0^-\\) use the formula for \\(x\\lt x_0\\).', '<b>Dùng nhầm công thức.</b> Với \\(x\\to x_0^-\\) dùng công thức ứng với \\(x\\lt x_0\\).'),
            ('<b>Writing "continuous on \\((-\\infty;2)\\cup(2;+\\infty)\\)".</b> State the separate intervals: the function is continuous on each of them.', '<b>Viết "liên tục trên \\((-\\infty;2)\\cup(2;+\\infty)\\)".</b> Hãy nêu từng khoảng: hàm số liên tục trên mỗi khoảng đó.'),
            ('<b>Using the theorem without continuity, or to count roots.</b> \\(f(a)f(b)\\lt0\\) gives at least one root only for a continuous \\(f\\) on \\([a;b]\\).', '<b>Dùng định lí khi hàm không liên tục, hoặc để đếm nghiệm.</b> \\(f(a)f(b)\\lt0\\) chỉ cho ít nhất một nghiệm khi \\(f\\) liên tục trên \\([a;b]\\).')]
summary = [('\\(f\\) continuous at \\(x_0\\iff\\lim\\limits_{x\\to x_0}f(x)=f(x_0)\\).', '\\(f\\) liên tục tại \\(x_0\\iff\\lim\\limits_{x\\to x_0}f(x)=f(x_0)\\).'),
           ('Piecewise: left limit = right limit = value at the joining point.', 'Hàm nhiều công thức: giới hạn trái = giới hạn phải = giá trị tại điểm nối.'),
           ('Elementary functions are continuous on each interval of their domain.', 'Hàm số sơ cấp liên tục trên từng khoảng của tập xác định.'),
           ('\\(f\\) continuous on \\([a;b]\\), \\(f(a)f(b)\\lt0\\Rightarrow\\) a root in \\((a;b)\\). Key words: continuous, discontinuous, intermediate value theorem.', '\\(f\\) liên tục trên \\([a;b]\\), \\(f(a)f(b)\\lt0\\Rightarrow\\) có nghiệm thuộc \\((a;b)\\). Từ cần nhớ: continuous, discontinuous, intermediate value theorem.')]
checks = [('I can check continuity at a point.', 'Em xét được tính liên tục tại một điểm.'), ('I can find a parameter that makes a function continuous.', 'Em tìm được tham số để hàm số liên tục.'),
          ('I can state where an elementary function is continuous.', 'Em chỉ ra được khoảng liên tục của hàm số sơ cấp.'), ('I can prove that an equation has a root.', 'Em chứng minh được phương trình có nghiệm.')]
LL('g11-limits-05', 'Continuous Functions', CV, ('Limits and Continuity', 'Giới hạn. Hàm số liên tục'), 'limits', 'continuous-functions', 180, 'Intermediate', 70, ('limits of functions, one-sided limits', 'giới hạn của hàm số, giới hạn một phía'),
   'Continuity at a point and on an interval, parameters for continuity, the intermediate value theorem.', 'Bài 17 – Hàm số liên tục tại một điểm, trên một khoảng; tìm tham số; định lí giá trị trung gian và chứng minh phương trình có nghiệm.',
   ['continuity', 'discontinuous', 'intermediate value theorem', 'piecewise'], ['hàm số liên tục', 'gián đoạn', 'định lí giá trị trung gian', 'hàm nhiều công thức'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g11-limits-04'])
