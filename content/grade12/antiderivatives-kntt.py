# -*- coding: utf-8 -*-
"""g12-int-01 = Toán 12 KNTT, Bài 11: Nguyên hàm. Mã ngân hàng câu hỏi: TOAN12-C4-B11.
(Bài cũ g12-antider-01/02 được giữ lại nhưng tạm khóa: đổi biến và nguyên hàm từng phần không thuộc danh mục SGK Kết nối tri thức.)"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g12c as S
from sp_g12c import ptex, integ, deriv, ev, D, DE

CV = 'Nguyên hàm'
vocab = defs(CV, [
 ('antid', 'antiderivative (primitive)', 'nguyên hàm', 'a function \\(F\\) with \\(F′(x)=f(x)\\) for every \\(x\\) in \\(K\\).', 'hàm số \\(F\\) thỏa mãn \\(F′(x)=f(x)\\) với mọi \\(x\\) thuộc \\(K\\).', '\\(x^2\\) is an antiderivative of \\(2x\\).', '\\(F(x)\\)'),
 ('indef', 'indefinite integral', 'họ nguyên hàm', 'the set of all antiderivatives \\(F(x)+C\\), written \\(\\int f(x)\\,dx\\).', 'tập hợp mọi nguyên hàm \\(F(x)+C\\), kí hiệu \\(\\int f(x)\\,dx\\).', '\\(\\int2x\\,dx=x^2+C\\).', '\\(\\int f(x)\\,dx\\)'),
 ('constC', 'constant of integration', 'hằng số tùy ý \\(C\\)', 'the arbitrary constant \\(C\\) in \\(F(x)+C\\).', 'hằng số \\(C\\) bất kì trong \\(F(x)+C\\).', 'Do not forget the constant \\(C\\).', '\\(C\\)'),
 ('integr', 'integrand', 'hàm số dưới dấu nguyên hàm', 'the function \\(f(x)\\) in \\(\\int f(x)\\,dx\\).', 'hàm số \\(f(x)\\) trong \\(\\int f(x)\\,dx\\).', 'The integrand is \\(3x^2\\).', ''),
 ('initc', 'initial condition', 'điều kiện ban đầu', 'a given value such as \\(F(0)=2\\) that fixes \\(C\\).', 'giá trị cho trước, ví dụ \\(F(0)=2\\), dùng để tìm \\(C\\).', 'Use the initial condition to find \\(C\\).', ''),
 ('veloc', 'velocity', 'vận tốc', 'the derivative of the position: \\(v(t)=s′(t)\\); so \\(s(t)\\) is an antiderivative of \\(v(t)\\).', 'đạo hàm của tọa độ (quãng đường): \\(v(t)=s′(t)\\); do đó \\(s(t)\\) là một nguyên hàm của \\(v(t)\\).', 'The velocity is \\(20-9.8t\\) m/s.', '\\(v(t)\\)')])
goals = [('explain what an antiderivative is and write \\(\\int f(x)\\,dx=F(x)+C\\);', 'hiểu khái niệm [[nguyên hàm]] và viết [[họ nguyên hàm]] \\(\\int f(x)\\,dx=F(x)+C\\);'),
         ('use the two properties and the table of basic antiderivatives;', 'dùng hai tính chất và bảng nguyên hàm cơ bản;'),
         ('find the antiderivative that satisfies an initial condition;', 'tìm nguyên hàm thỏa mãn [[điều kiện ban đầu]];'),
         ('solve motion and cost problems with antiderivatives.', 'giải bài toán chuyển động, chi phí bằng nguyên hàm.')]
phrases = [('<b>Find the antiderivative of the function.</b>', 'Tìm nguyên hàm của hàm số.'), ('<b>Check that \\(F′(x)=f(x)\\).</b>', 'Kiểm tra \\(F′(x)=f(x)\\).'),
           ('<b>Find \\(F(x)\\) such that \\(F(0)=2\\).</b>', 'Tìm \\(F(x)\\) sao cho \\(F(0)=2\\).'), ('<b>Do not forget the constant \\(C\\).</b>', 'Đừng quên hằng số \\(C\\).'), ('<b>Find the position of the object at time \\(t\\).</b>', 'Tìm vị trí của vật tại thời điểm \\(t\\).')]
review = T('From Grade 11: \\((x^n)′=nx^{n-1}\\), \\((\\ln x)′=\\dfrac1x\\), \\((e^x)′=e^x\\), \\((a^x)′=a^x\\ln a\\), \\((\\sin x)′=\\cos x\\), \\((\\cos x)′=-\\sin x\\), \\((\\tan x)′=\\dfrac1{\\cos^2x}\\), \\((\\cot x)′=-\\dfrac1{\\sin^2x}\\). Today we go backwards: from the derivative to the function.',
           'Từ lớp 11: \\((x^n)′=nx^{n-1}\\), \\((\\ln x)′=\\dfrac1x\\), \\((e^x)′=e^x\\), \\((a^x)′=a^x\\ln a\\), \\((\\sin x)′=\\cos x\\), \\((\\cos x)′=-\\sin x\\), \\((\\tan x)′=\\dfrac1{\\cos^2x}\\), \\((\\cot x)′=-\\dfrac1{\\sin^2x}\\). Hôm nay ta làm ngược lại: từ đạo hàm tìm hàm số.')
theory = '<h3>11.1 %s</h3>' % TI('The idea of an antiderivative', 'Khái niệm nguyên hàm')
theory += BOX('blue', ('Definition', 'Định nghĩa'), T('Let \\(f\\) be defined on an interval \\(K\\). A function \\(F\\) is an <b>antiderivative</b> of \\(f\\) on \\(K\\) if \\(F′(x)=f(x)\\) for all \\(x\\in K\\).', 'Cho hàm số \\(f\\) xác định trên khoảng (đoạn, nửa khoảng) \\(K\\). Hàm số \\(F\\) là một <b>[[nguyên hàm]]</b> của \\(f\\) trên \\(K\\) nếu \\(F′(x)=f(x)\\) với mọi \\(x\\in K\\).'))
theory += BOX('mint', ('Theorem', 'Định lí'), UL([T('If \\(F\\) is an antiderivative of \\(f\\) on \\(K\\), then all antiderivatives are \\(F(x)+C\\) (\\(C\\) a constant). We write \\(\\displaystyle\\int f(x)\\,dx=F(x)+C\\).', 'Nếu \\(F\\) là một nguyên hàm của \\(f\\) trên \\(K\\) thì mọi nguyên hàm của \\(f\\) có dạng \\(F(x)+C\\) (\\(C\\) là hằng số). Kí hiệu \\(\\displaystyle\\int f(x)\\,dx=F(x)+C\\).'),
  T('Every function continuous on \\(K\\) has an antiderivative on \\(K\\). Also \\(\\displaystyle\\int f′(x)\\,dx=f(x)+C\\).', 'Mọi hàm số liên tục trên \\(K\\) đều có nguyên hàm trên \\(K\\). Ngoài ra \\(\\displaystyle\\int f′(x)\\,dx=f(x)+C\\).')]))
theory += GRAPH({'view': [-3, 3, -3, 6], 'functions': [{'f': 'x^2-2', 'label': 'y = x² − 2', 'dash': 2}, {'f': 'x^2', 'label': 'y = x²'}, {'f': 'x^2+2', 'label': 'y = x² + 2', 'dash': 2}], 'legend': True},
  cap=('Three antiderivatives of \\(f(x)=2x\\): the graphs are vertical shifts of each other, and at the same \\(x\\) they have the same slope \\(2x\\).', 'Ba nguyên hàm của \\(f(x)=2x\\): các đồ thị là ảnh của nhau qua phép tịnh tiến theo trục tung, tại cùng một \\(x\\) có cùng hệ số góc tiếp tuyến \\(2x\\).'), alt=('Three parabolas shifted vertically', ''), height=320)
theory += '<h3>11.2 %s</h3>' % TI('Properties', 'Tính chất của nguyên hàm')
theory += BOX('blue', ('For continuous \\(f\\), \\(g\\) on \\(K\\)', 'Với \\(f\\), \\(g\\) liên tục trên \\(K\\)'), M('\\int kf(x)\\,dx=k\\int f(x)\\,dx\\ (k\\ne0),\\qquad\\int[f(x)\\pm g(x)]\\,dx=\\int f(x)\\,dx\\pm\\int g(x)\\,dx'))
theory += '<h3>11.3 %s</h3>' % TI('Table of basic antiderivatives', 'Nguyên hàm của một số hàm số sơ cấp')
theory += TBL([TI('Function \\(f(x)\\)', 'Hàm số \\(f(x)\\)'), '\\(\\int f(x)\\,dx\\)'], [
  ['\\(x^\\alpha\\ (\\alpha\\ne-1)\\)', '\\(\\dfrac{x^{\\alpha+1}}{\\alpha+1}+C\\)'], ['\\(\\dfrac1x\\)', '\\(\\ln|x|+C\\)'], ['\\(\\sin x\\)', '\\(-\\cos x+C\\)'], ['\\(\\cos x\\)', '\\(\\sin x+C\\)'],
  ['\\(\\dfrac1{\\cos^2x}\\)', '\\(\\tan x+C\\)'], ['\\(\\dfrac1{\\sin^2x}\\)', '\\(-\\cot x+C\\)'], ['\\(e^x\\)', '\\(e^x+C\\)'], ['\\(a^x\\ (0\\lt a\\ne1)\\)', '\\(\\dfrac{a^x}{\\ln a}+C\\)']])
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('Always add \\(+C\\). Check your answer by differentiating. There is no rule "\\(\\int f\\cdot g=\\int f\\cdot\\int g\\)": rewrite the product as a sum first. \\(\\int\\dfrac1x\\,dx=\\ln|x|+C\\) (absolute value!).', 'Luôn viết \\(+C\\). Kiểm tra kết quả bằng cách lấy đạo hàm. Không có quy tắc "\\(\\int f\\cdot g=\\int f\\cdot\\int g\\)": phải biến đổi tích thành tổng trước. \\(\\int\\dfrac1x\\,dx=\\ln|x|+C\\) (có dấu giá trị tuyệt đối!).'))

P1 = {2: 3, 1: -4, 0: 5}; assert ptex(integ(P1)) == 'x^{3}-2x^{2}+5x'
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('A polynomial', 'Hàm đa thức'), T('Find \\(\\displaystyle\\int(3x^2-4x+5)\\,dx\\).', 'Tìm \\(\\displaystyle\\int(3x^2-4x+5)\\,dx\\).'), T('Split into terms; use \\(\\int x^\\alpha dx=\\dfrac{x^{\\alpha+1}}{\\alpha+1}+C\\).', 'Tách thành từng hạng tử; dùng \\(\\int x^\\alpha dx=\\dfrac{x^{\\alpha+1}}{\\alpha+1}+C\\).'),
  [T('\\(3\\int x^2dx-4\\int x\\,dx+5\\int dx=3\\cdot\\dfrac{x^3}3-4\\cdot\\dfrac{x^2}2+5x+C\\).', '\\(3\\int x^2dx-4\\int x\\,dx+5\\int dx=3\\cdot\\dfrac{x^3}3-4\\cdot\\dfrac{x^2}2+5x+C\\).'), T('Check: \\((x^3-2x^2+5x)′=3x^2-4x+5\\).', 'Thử lại: \\((x^3-2x^2+5x)′=3x^2-4x+5\\).')],
  T('\\(x^3-2x^2+5x+C\\).', '\\(x^3-2x^2+5x+C\\).'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Trigonometric, logarithmic and exponential', 'Lượng giác, lôgarit, mũ'), T('On \\((0;+\\infty)\\), find \\(\\displaystyle\\int\\left(2\\sin x+\\dfrac3x\\right)dx\\) and \\(\\displaystyle\\int(e^x-2^x)\\,dx\\).', 'Trên \\((0;+\\infty)\\), tìm \\(\\displaystyle\\int\\left(2\\sin x+\\dfrac3x\\right)dx\\) và \\(\\displaystyle\\int(e^x-2^x)\\,dx\\).'),
  T('Use the table row by row.', 'Dùng bảng nguyên hàm từng dòng.'), [T('\\(2(-\\cos x)+3\\ln|x|+C=-2\\cos x+3\\ln x+C\\) (\\(x\\gt0\\)).', '\\(2(-\\cos x)+3\\ln|x|+C=-2\\cos x+3\\ln x+C\\) (vì \\(x\\gt0\\)).'), T('\\(\\int e^xdx-\\int2^xdx=e^x-\\dfrac{2^x}{\\ln2}+C\\).', '\\(\\int e^xdx-\\int2^xdx=e^x-\\dfrac{2^x}{\\ln2}+C\\).')],
  T('\\(-2\\cos x+3\\ln x+C\\); \\(e^x-\\dfrac{2^x}{\\ln2}+C\\).', '\\(-2\\cos x+3\\ln x+C\\); \\(e^x-\\dfrac{2^x}{\\ln2}+C\\).'))
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Rewrite first', 'Biến đổi trước khi tìm'), T('Find (a) \\(\\displaystyle\\int\\dfrac{x^2+1}{x}\\,dx\\) on \\((0;+\\infty)\\); (b) \\(\\displaystyle\\int\\tan^2x\\,dx\\) on \\(\\left(-\\dfrac\\pi2;\\dfrac\\pi2\\right)\\).', 'Tìm (a) \\(\\displaystyle\\int\\dfrac{x^2+1}{x}\\,dx\\) trên \\((0;+\\infty)\\); (b) \\(\\displaystyle\\int\\tan^2x\\,dx\\) trên \\(\\left(-\\dfrac\\pi2;\\dfrac\\pi2\\right)\\).'),
  T('Turn a quotient into a sum; use \\(\\tan^2x=\\dfrac1{\\cos^2x}-1\\).', 'Biến thương thành tổng; dùng \\(\\tan^2x=\\dfrac1{\\cos^2x}-1\\).'),
  [T('(a) \\(\\dfrac{x^2+1}x=x+\\dfrac1x\\), so the answer is \\(\\dfrac{x^2}2+\\ln x+C\\).', '(a) \\(\\dfrac{x^2+1}x=x+\\dfrac1x\\) nên kết quả là \\(\\dfrac{x^2}2+\\ln x+C\\).'), T('(b) \\(\\int\\left(\\dfrac1{\\cos^2x}-1\\right)dx=\\tan x-x+C\\).', '(b) \\(\\int\\left(\\dfrac1{\\cos^2x}-1\\right)dx=\\tan x-x+C\\).')],
  T('(a) \\(\\dfrac{x^2}2+\\ln x+C\\); (b) \\(\\tan x-x+C\\).', '(a) \\(\\dfrac{x^2}2+\\ln x+C\\); (b) \\(\\tan x-x+C\\).'))
P4 = {3: 4, 1: -2, 0: 1}; I4 = integ(P4); C4 = 3 - ev(I4, 1); assert ptex(I4) == 'x^{4}-x^{2}+x' and C4 == 2
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('An initial condition', 'Điều kiện ban đầu'), T('Find the antiderivative \\(F\\) of \\(f(x)=4x^3-2x+1\\) with \\(F(1)=3\\).', 'Tìm nguyên hàm \\(F\\) của \\(f(x)=4x^3-2x+1\\) thỏa mãn \\(F(1)=3\\).'), T('Find the family, then use \\(F(1)=3\\) to get \\(C\\).', 'Tìm họ nguyên hàm, rồi dùng \\(F(1)=3\\) để tìm \\(C\\).'),
  [T('\\(F(x)=x^4-x^2+x+C\\).', '\\(F(x)=x^4-x^2+x+C\\).'), T('\\(F(1)=1-1+1+C=1+C=3\\Rightarrow C=2\\).', '\\(F(1)=1-1+1+C=1+C=3\\Rightarrow C=2\\).')], T('\\(F(x)=x^4-x^2+x+2\\).', '\\(F(x)=x^4-x^2+x+2\\).'))
h2 = F(20) * 2 - F(49, 10) * 4 + F(3, 2); assert h2 == F(219, 10)
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('A ball thrown upward', 'Quả bóng ném lên'), T('A ball is thrown straight up from a height of 1.5 m. Its velocity is \\(v(t)=20-9.8t\\) (m/s). Find its height \\(h(t)\\), its height after 2 s, and the time it reaches the top.', 'Một quả bóng được ném thẳng đứng lên từ độ cao 1,5 m, vận tốc \\(v(t)=20-9{,}8t\\) (m/s). Tìm độ cao \\(h(t)\\), độ cao sau 2 giây và thời điểm bóng lên cao nhất.'),
  T('\\(h(t)\\) is the antiderivative of \\(v(t)\\) with \\(h(0)=1.5\\).', '\\(h(t)\\) là nguyên hàm của \\(v(t)\\) thỏa mãn \\(h(0)=1{,}5\\).'),
  [T('\\(h(t)=20t-4.9t^2+C\\), \\(h(0)=C=1.5\\).', '\\(h(t)=20t-4{,}9t^2+C\\), \\(h(0)=C=1{,}5\\).'), T('\\(h(2)=40-19.6+1.5=21.9\\) m.', '\\(h(2)=40-19{,}6+1{,}5=21{,}9\\) m.'), T('Top when \\(v(t)=0\\): \\(t=\\dfrac{20}{9.8}\\approx2.04\\) s.', 'Lên cao nhất khi \\(v(t)=0\\): \\(t=\\dfrac{20}{9{,}8}\\approx2{,}04\\) s.')],
  T('\\(h(t)=-4.9t^2+20t+1.5\\); \\(h(2)=21.9\\) m; top at \\(t\\approx2.04\\) s.', '\\(h(t)=-4{,}9t^2+20t+1{,}5\\); \\(h(2)=21{,}9\\) m; lên cao nhất tại \\(t\\approx2{,}04\\) s.'))
assert round(20 / 9.8, 2) == 2.04

RULES = [(True, '\\(\\displaystyle\\int\\dfrac1x\\,dx=\\ln|x|+C\\) on \\((-\\infty;0)\\).', '\\(\\displaystyle\\int\\dfrac1x\\,dx=\\ln|x|+C\\) trên \\((-\\infty;0)\\).'),
         (False, '\\(\\displaystyle\\int f(x)g(x)\\,dx=\\int f(x)\\,dx\\cdot\\int g(x)\\,dx\\) for all continuous \\(f\\), \\(g\\).', '\\(\\displaystyle\\int f(x)g(x)\\,dx=\\int f(x)\\,dx\\cdot\\int g(x)\\,dx\\) với mọi hàm liên tục \\(f\\), \\(g\\).'),
         (False, '\\(\\displaystyle\\int3^x\\,dx=3^x\\ln3+C\\).', '\\(\\displaystyle\\int3^x\\,dx=3^x\\ln3+C\\).')]
def lvl(P):
    A = P['poly']; I = integ(A)
    o1 = M4(1, '\\(\\displaystyle\\int(%s)\\,dx=\\)…' % ptex(A), '\\(\\displaystyle\\int(%s)\\,dx=\\)…' % ptex(A), ptex(I) + '+C', [ptex(deriv(A)) + '+C', ptex({F(p) + 1: F(c) for p, c in A.items()}) + '+C', ptex(I)],
            'Term by term: \\(%s+C\\). Check by differentiating.' % ptex(I), 'Lấy nguyên hàm từng hạng tử: \\(%s+C\\). Thử lại bằng đạo hàm.' % ptex(I))
    o2 = M4(2, P['mix'][0], P['mix'][0], P['mix'][1], P['mix'][2], P['mix'][3], P['mix'][3])
    B, (x0, y0), x1 = P['init']; IB = integ(B); C = y0 - ev(IB, x0); val = ev(IB, x1) + C
    o3 = M4(3, '\\(F\\) is an antiderivative of \\(f(x)=%s\\) with \\(F(%d)=%d\\). Then \\(F(%d)=\\)…' % (ptex(B), x0, y0, x1), '\\(F\\) là một nguyên hàm của \\(f(x)=%s\\) và \\(F(%d)=%d\\). Khi đó \\(F(%d)=\\)…' % (ptex(B), x0, y0, x1),
            fr(val), [fr(ev(IB, x1)), fr(ev(B, x1) + y0), fr(val + 2), fr(-val) if val else '3'], '\\(F(x)=%s+C\\), \\(C=%s\\), \\(F(%d)=%s\\).' % (ptex(IB), fr(C), x1, fr(val)), '\\(F(x)=%s+C\\), \\(C=%s\\), \\(F(%d)=%s\\).' % (ptex(IB), fr(C), x1, fr(val)))
    Fc, f, truth = P['chk']; real = ptex(deriv(Fc)) == f; assert real == truth
    t4 = tf(4, '\\(F(x)=%s\\) is an antiderivative of \\(f(x)=%s\\).' % (ptex(Fc), f), '\\(F(x)=%s\\) là một nguyên hàm của \\(f(x)=%s\\).' % (ptex(Fc), f), truth,
            '\\(F′(x)=%s\\).' % ptex(deriv(Fc)), '\\(F′(x)=%s\\).' % ptex(deriv(Fc)))
    rr = RULES[P['t5']]; t5 = tf(5, rr[1], rr[2], rr[0], 'Check by differentiating: \\((\\ln|x|)′=\\dfrac1x\\) for \\(x\\ne0\\); \\(\\left(\\dfrac{3^x}{\\ln3}\\right)′=3^x\\); there is no product rule for antiderivatives.', 'Kiểm tra bằng đạo hàm: \\((\\ln|x|)′=\\dfrac1x\\) với \\(x\\ne0\\); \\(\\left(\\dfrac{3^x}{\\ln3}\\right)′=3^x\\); không có quy tắc nguyên hàm của tích như vậy.')
    v0, a, T_ = P['mot']; s = v0 * T_ + F(a) * T_ * T_ / 2; assert s.denominator == 1
    s6 = sh(6, 'A motorbike has velocity \\(v(t)=%d+%st\\) (m/s) and \\(s(0)=0\\). How many metres does it travel in the first \\(%d\\) seconds?' % (v0, DE(a), T_), 'Một xe máy có vận tốc \\(v(t)=%d+%st\\) (m/s) và \\(s(0)=0\\). Trong \\(%d\\) giây đầu xe đi được bao nhiêu mét?' % (v0, D(a), T_), s.numerator,
            '\\(s(t)=%dt+%st^2\\); \\(s(%d)=%d\\).' % (v0, DE(F(a) / 2), T_, s), '\\(s(t)=%dt+%st^2\\); \\(s(%d)=%d\\).' % (v0, D(F(a) / 2), T_, s))
    G, (g0, gy), g1 = P['init2']; IG = integ(G); CG = gy - ev(IG, g0); vv = ev(IG, g1) + CG; assert vv.denominator == 1
    s7 = sh(7, '\\(F\\) is an antiderivative of \\(f(x)=%s\\) with \\(F(%d)=%d\\). Find \\(F(%d)\\).' % (ptex(G), g0, gy, g1), 'Cho \\(F\\) là một nguyên hàm của \\(f(x)=%s\\) thỏa mãn \\(F(%d)=%d\\). Tính \\(F(%d)\\).' % (ptex(G), g0, gy, g1), vv.numerator,
            '\\(F(x)=%s+C\\), \\(C=%s\\), \\(F(%d)=%d\\).' % (ptex(IG), fr(CG), g1, vv), '\\(F(x)=%s+C\\), \\(C=%s\\), \\(F(%d)=%d\\).' % (ptex(IG), fr(CG), g1, vv))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
MIX = [('\\(\\displaystyle\\int(3\\cos x-\\sin x)\\,dx=\\)…', '3\\sin x+\\cos x+C', ['3\\sin x-\\cos x+C', '-3\\sin x+\\cos x+C', '-3\\sin x-\\cos x+C'], '\\(\\int\\cos x\\,dx=\\sin x+C\\), \\(\\int\\sin x\\,dx=-\\cos x+C\\).'),
       ('On \\((0;+\\infty)\\): \\(\\displaystyle\\int\\left(e^x+\\dfrac2x\\right)dx=\\)…', 'e^x+2\\ln x+C', ['e^x-\\dfrac{2}{x^2}+C', 'xe^{x-1}+2\\ln x+C', 'e^x+\\dfrac{2}{\\ln x}+C'], '\\(\\int e^xdx=e^x+C\\), \\(\\int\\dfrac1xdx=\\ln|x|+C\\).'),
       ('\\(\\displaystyle\\int\\left(\\dfrac{1}{\\cos^2x}+5^x\\right)dx=\\)…', '\\tan x+\\dfrac{5^x}{\\ln5}+C', ['\\tan x+5^x\\ln5+C', '-\\cot x+\\dfrac{5^x}{\\ln5}+C', '\\tan x+\\dfrac{5^{x+1}}{x+1}+C'], '\\(\\int\\dfrac1{\\cos^2x}dx=\\tan x+C\\), \\(\\int a^xdx=\\dfrac{a^x}{\\ln a}+C\\).')]
PP = [dict(poly={2: 6, 1: -2, 0: 3}, mix=MIX[0], init=({1: 2, 0: 1}, (0, 3), 2), chk=({3: 1, 2: -1, 0: 7}, '3x^{2}-2x', True), t5=0, mot=(5, 2, 10), init2=({2: 3, 0: -2}, (1, 4), 2)),
      dict(poly={3: 4, 1: 6, 0: -1}, mix=MIX[1], init=({1: -4, 0: 3}, (1, 2), 3), chk=({4: 1, 1: 2}, '4x^{3}+2x', False), t5=1, mot=(10, 3, 8), init2=({1: 6, 0: 1}, (0, -3), 3)),
      dict(poly={2: -9, 1: 4, 0: 2}, mix=MIX[2], init=({2: 3, 1: -2}, (2, 1), -1), chk=({3: 2, 1: -5, 0: 1}, '6x^{2}-5', True), t5=2, mot=(12, 4, 5), init2=({3: 4, 1: -2}, (1, 0), 2))]
practice = three(lvl, PP)
practice = with_self(practice, S.M11S12, start=8)
mistakes = [('<b>Forgetting \\(+C\\).</b> \\(\\int f(x)\\,dx\\) is a family of functions.', '<b>Quên \\(+C\\).</b> \\(\\int f(x)\\,dx\\) là một họ hàm số.'),
            ('<b>Differentiating instead of integrating.</b> \\(\\int x^3dx=\\dfrac{x^4}4+C\\), not \\(3x^2\\).', '<b>Lấy đạo hàm thay vì nguyên hàm.</b> \\(\\int x^3dx=\\dfrac{x^4}4+C\\), không phải \\(3x^2\\).'),
            ('<b>Sign of \\(\\int\\sin x\\,dx\\).</b> It is \\(-\\cos x+C\\).', '<b>Sai dấu ở \\(\\int\\sin x\\,dx\\).</b> Kết quả là \\(-\\cos x+C\\).'),
            ('<b>\\(\\int a^xdx=a^x\\ln a\\).</b> That is the derivative; the antiderivative is \\(\\dfrac{a^x}{\\ln a}+C\\).', '<b>\\(\\int a^xdx=a^x\\ln a\\).</b> Đó là đạo hàm; nguyên hàm là \\(\\dfrac{a^x}{\\ln a}+C\\).')]
summary = [('\\(F\\) is an antiderivative of \\(f\\iff F′=f\\); \\(\\int f(x)\\,dx=F(x)+C\\).', '\\(F\\) là nguyên hàm của \\(f\\iff F′=f\\); \\(\\int f(x)\\,dx=F(x)+C\\).'),
           ('\\(\\int kf=k\\int f\\) (\\(k\\ne0\\)); \\(\\int(f\\pm g)=\\int f\\pm\\int g\\).', '\\(\\int kf=k\\int f\\) (\\(k\\ne0\\)); \\(\\int(f\\pm g)=\\int f\\pm\\int g\\).'),
           ('Table: \\(x^\\alpha\\to\\dfrac{x^{\\alpha+1}}{\\alpha+1}\\), \\(\\dfrac1x\\to\\ln|x|\\), \\(\\sin\\to-\\cos\\), \\(\\cos\\to\\sin\\), \\(e^x\\to e^x\\), \\(a^x\\to\\dfrac{a^x}{\\ln a}\\).', 'Bảng: \\(x^\\alpha\\to\\dfrac{x^{\\alpha+1}}{\\alpha+1}\\), \\(\\dfrac1x\\to\\ln|x|\\), \\(\\sin\\to-\\cos\\), \\(\\cos\\to\\sin\\), \\(e^x\\to e^x\\), \\(a^x\\to\\dfrac{a^x}{\\ln a}\\).'),
           ('An initial condition fixes \\(C\\). Key words: antiderivative, integral, constant of integration.', 'Điều kiện ban đầu xác định \\(C\\). Từ cần nhớ: antiderivative, integral, constant of integration.')]
checks = [('I can say what an antiderivative is and check one by differentiating.', 'Em nêu được khái niệm nguyên hàm và kiểm tra bằng đạo hàm.'), ('I can use the table and the two properties.', 'Em dùng được bảng nguyên hàm và hai tính chất.'),
          ('I can find \\(F\\) with an initial condition.', 'Em tìm được \\(F\\) thỏa mãn điều kiện ban đầu.'), ('I can solve a motion problem with antiderivatives.', 'Em giải được bài toán chuyển động bằng nguyên hàm.')]
LL('g12-int-01', 'Antiderivatives', CV, ('Antiderivatives and Integrals', 'Nguyên hàm và tích phân'), 'integrals', 'antiderivatives', 110, 'Intermediate', 70, ('derivatives of basic functions', 'đạo hàm của các hàm số sơ cấp'),
   'Antiderivatives: definition, properties, table of basic antiderivatives, initial conditions and motion problems.', 'Bài 11 – Khái niệm nguyên hàm, tính chất, bảng nguyên hàm cơ bản, điều kiện ban đầu và bài toán chuyển động.',
   ['antiderivative', 'indefinite integral', 'constant of integration'], ['nguyên hàm', 'họ nguyên hàm', 'hằng số C'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g12-stats-02'])
