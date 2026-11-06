# -*- coding: utf-8 -*-
"""g12-int-02 = Toán 12 KNTT, Bài 12: Tích phân. Mã ngân hàng câu hỏi: TOAN12-C4-B12."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g12c as S
from sp_g12c import ptex, integ, ev, defint, D, DE

CV = 'Tích phân'
vocab = defs(CV, [
 ('defint', 'definite integral', 'tích phân', 'the number \\(\\int_a^bf(x)\\,dx=F(b)-F(a)\\), where \\(F\\) is an antiderivative of \\(f\\).', 'số \\(\\int_a^bf(x)\\,dx=F(b)-F(a)\\), trong đó \\(F\\) là một nguyên hàm của \\(f\\).', 'The definite integral from 0 to 2 equals 4.', '\\(\\int_a^b\\)'),
 ('limits', 'lower and upper limits', 'cận dưới và cận trên', 'the numbers \\(a\\) and \\(b\\) in \\(\\int_a^b\\).', 'các số \\(a\\) và \\(b\\) trong \\(\\int_a^b\\).', 'The lower limit is 0 and the upper limit is 2.', '\\(a,\\ b\\)'),
 ('nl', 'Newton–Leibniz formula', 'công thức Newton – Leibniz', '\\(\\int_a^bf(x)\\,dx=F(x)\\Big|_a^b=F(b)-F(a)\\).', '\\(\\int_a^bf(x)\\,dx=F(x)\\Big|_a^b=F(b)-F(a)\\).', 'Use the Newton–Leibniz formula.', ''),
 ('ctrap', 'region under a curve (curvilinear trapezoid)', 'hình thang cong', 'the region bounded by \\(y=f(x)\\ge0\\), the \\(x\\)-axis and the lines \\(x=a\\), \\(x=b\\); its area is \\(\\int_a^bf(x)\\,dx\\).', 'hình giới hạn bởi đồ thị \\(y=f(x)\\ge0\\), trục hoành và hai đường thẳng \\(x=a\\), \\(x=b\\); diện tích là \\(\\int_a^bf(x)\\,dx\\).', 'Find the area of the region under the curve.', ''),
 ('netch', 'total change', 'tổng lượng biến thiên', '\\(\\int_a^bF′(x)\\,dx=F(b)-F(a)\\): integrating a rate of change gives the total change.', '\\(\\int_a^bF′(x)\\,dx=F(b)-F(a)\\): tích phân của tốc độ thay đổi cho tổng lượng thay đổi.', 'The integral of the flow rate is the total volume.', ''),
 ('displ', 'distance travelled', 'quãng đường đi được', 'for \\(v(t)\\ge0\\), \\(\\int_a^bv(t)\\,dt\\) is the distance travelled from \\(t=a\\) to \\(t=b\\).', 'với \\(v(t)\\ge0\\), \\(\\int_a^bv(t)\\,dt\\) là quãng đường đi được từ \\(t=a\\) đến \\(t=b\\).', 'The car travels 40 m before stopping.', '')])
goals = [('compute a definite integral with the Newton–Leibniz formula;', 'tính [[tích phân]] bằng [[công thức Newton – Leibniz]];'),
         ('use the properties (linearity, splitting the interval, swapping the limits);', 'dùng các tính chất (tuyến tính, tách cận, đổi cận);'),
         ('integrate functions with absolute values by splitting the interval;', 'tính tích phân của hàm có dấu giá trị tuyệt đối bằng cách tách khoảng;'),
         ('interpret an integral as an area, a distance or a total change.', 'hiểu tích phân là diện tích [[hình thang cong]], [[quãng đường đi được]] hay [[tổng lượng biến thiên]].')]
phrases = [('<b>Evaluate the definite integral.</b>', 'Tính tích phân.'), ('<b>Split the integral at \\(x=1\\).</b>', 'Tách tích phân tại \\(x=1\\).'), ('<b>Find the area of the region under the curve.</b>', 'Tính diện tích hình thang cong.'),
           ('<b>How far does the car travel before it stops?</b>', 'Ô tô đi thêm được bao xa thì dừng?'), ('<b>The integral of the rate gives the total change.</b>', 'Tích phân của tốc độ cho tổng lượng thay đổi.')]
review = T('From Bài 11: \\(\\int x^\\alpha dx=\\dfrac{x^{\\alpha+1}}{\\alpha+1}+C\\), \\(\\int\\dfrac1xdx=\\ln|x|+C\\), \\(\\int\\sin x\\,dx=-\\cos x+C\\), \\(\\int\\cos x\\,dx=\\sin x+C\\), \\(\\int e^xdx=e^x+C\\), \\(\\int a^xdx=\\dfrac{a^x}{\\ln a}+C\\); if \\(v(t)=s′(t)\\), then \\(s\\) is an antiderivative of \\(v\\).',
           'Từ Bài 11: \\(\\int x^\\alpha dx=\\dfrac{x^{\\alpha+1}}{\\alpha+1}+C\\), \\(\\int\\dfrac1xdx=\\ln|x|+C\\), \\(\\int\\sin x\\,dx=-\\cos x+C\\), \\(\\int\\cos x\\,dx=\\sin x+C\\), \\(\\int e^xdx=e^x+C\\), \\(\\int a^xdx=\\dfrac{a^x}{\\ln a}+C\\); nếu \\(v(t)=s′(t)\\) thì \\(s\\) là một nguyên hàm của \\(v\\).')
FA = {2: F(1, 2), 0: 1}; area = defint(FA, 1, 3); assert area == F(19, 3)
pts = [[1, 0]] + [[round(1 + 2 * i / 40, 4), round(float(ev(FA, F(1) + F(2 * i, 40))), 4)] for i in range(41)] + [[3, 0]]
theory = '<h3>12.1 %s</h3>' % TI('Definition', 'Khái niệm tích phân')
theory += BOX('blue', ('Area under a curve', 'Diện tích hình thang cong'), T('Let \\(f\\) be continuous and non-negative on \\([a;b]\\), and \\(F\\) an antiderivative of \\(f\\). The area of the region bounded by \\(y=f(x)\\), the \\(x\\)-axis, \\(x=a\\), \\(x=b\\) is \\(S=F(b)-F(a)\\).', 'Cho \\(f\\) liên tục, không âm trên \\([a;b]\\) và \\(F\\) là một nguyên hàm của \\(f\\). Diện tích [[hình thang cong]] giới hạn bởi đồ thị \\(y=f(x)\\), trục hoành và hai đường thẳng \\(x=a\\), \\(x=b\\) là \\(S=F(b)-F(a)\\).'))
theory += GEO({'view': [-0.5, 4, -0.8, 6.5], 'axes': True, 'equal': False, 'steps': [{'type': 'polygon', 'through': pts, 'style': {'borders': {'visible': False}, 'fillOpacity': 0.4}}, {'type': 'curve', 'f': '0.5*x^2+1'},
  {'type': 'point', 'id': 'a', 'name': 'x = 1', 'at': [1, 0], 'fixed': True, 'off': [-8, -18]}, {'type': 'point', 'id': 'b', 'name': 'x = 3', 'at': [3, 0], 'fixed': True, 'off': [-8, -18]}]},
  cap=('The shaded region under \\(y=\\frac12x^2+1\\) on \\([1;3]\\) has area \\(\\int_1^3\\left(\\frac12x^2+1\\right)dx=\\left(\\frac{x^3}6+x\\right)\\Big|_1^3=\\frac{19}3\\).', 'Phần tô đậm dưới đồ thị \\(y=\\frac12x^2+1\\) trên \\([1;3]\\) có diện tích \\(\\int_1^3\\left(\\frac12x^2+1\\right)dx=\\left(\\frac{x^3}6+x\\right)\\Big|_1^3=\\frac{19}3\\).'),
  alt=('Region under a parabola between x = 1 and x = 3', ''), height=320)
theory += BOX('mint', ('Definition (Newton–Leibniz)', 'Định nghĩa (công thức Newton – Leibniz)'), M('\\int_a^bf(x)\\,dx=F(x)\\Big|_a^b=F(b)-F(a)'),
  UL([T('\\(f\\) continuous on an interval containing \\(a\\), \\(b\\); \\(F\\) any antiderivative (the constant \\(C\\) cancels).', '\\(f\\) liên tục trên một khoảng chứa \\(a\\), \\(b\\); \\(F\\) là một nguyên hàm bất kì (hằng số \\(C\\) bị triệt tiêu).'),
      T('Conventions: \\(\\int_a^af(x)\\,dx=0\\), \\(\\int_b^af(x)\\,dx=-\\int_a^bf(x)\\,dx\\). The variable name does not matter: \\(\\int_a^bf(x)\\,dx=\\int_a^bf(t)\\,dt\\).', 'Quy ước: \\(\\int_a^af(x)\\,dx=0\\), \\(\\int_b^af(x)\\,dx=-\\int_a^bf(x)\\,dx\\). Tích phân không phụ thuộc tên biến: \\(\\int_a^bf(x)\\,dx=\\int_a^bf(t)\\,dt\\).'),
      T('Meaning: \\(\\int_a^bF′(x)\\,dx=F(b)-F(a)\\) is the total change of \\(F\\); \\(\\int_a^bv(t)\\,dt\\) is the distance travelled when \\(v\\ge0\\).', 'Ý nghĩa: \\(\\int_a^bF′(x)\\,dx=F(b)-F(a)\\) là tổng lượng biến thiên của \\(F\\); \\(\\int_a^bv(t)\\,dt\\) là quãng đường đi được khi \\(v\\ge0\\).')]))
theory += '<h3>12.2 %s</h3>' % TI('Properties', 'Tính chất của tích phân')
theory += BOX('blue', ('For continuous \\(f\\), \\(g\\)', 'Với \\(f\\), \\(g\\) liên tục'), UL([T('\\(\\int_a^bkf(x)\\,dx=k\\int_a^bf(x)\\,dx\\).', '\\(\\int_a^bkf(x)\\,dx=k\\int_a^bf(x)\\,dx\\).'), T('\\(\\int_a^b[f(x)\\pm g(x)]\\,dx=\\int_a^bf(x)\\,dx\\pm\\int_a^bg(x)\\,dx\\).', '\\(\\int_a^b[f(x)\\pm g(x)]\\,dx=\\int_a^bf(x)\\,dx\\pm\\int_a^bg(x)\\,dx\\).'),
  T('\\(\\int_a^bf(x)\\,dx=\\int_a^cf(x)\\,dx+\\int_c^bf(x)\\,dx\\) (splitting at \\(c\\)).', '\\(\\int_a^bf(x)\\,dx=\\int_a^cf(x)\\,dx+\\int_c^bf(x)\\,dx\\) (tách cận tại \\(c\\)).')]))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('For \\(\\int|f(x)|\\,dx\\), split the interval where \\(f\\) changes sign and remove the absolute value on each part. A negative integral is possible; it is an area only when \\(f\\ge0\\).', 'Với \\(\\int|f(x)|\\,dx\\), tách khoảng tại các điểm \\(f\\) đổi dấu rồi bỏ dấu giá trị tuyệt đối trên từng khoảng. Tích phân có thể âm; nó chỉ là diện tích khi \\(f\\ge0\\).'))

assert defint({2: 3, 1: -2}, 1, 2) == 4
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('A polynomial', 'Hàm đa thức'), T('Compute \\(\\displaystyle\\int_1^2(3x^2-2x)\\,dx\\).', 'Tính \\(\\displaystyle\\int_1^2(3x^2-2x)\\,dx\\).'), T('Find an antiderivative, then \\(F(2)-F(1)\\).', 'Tìm một nguyên hàm rồi tính \\(F(2)-F(1)\\).'),
  [T('\\(F(x)=x^3-x^2\\).', '\\(F(x)=x^3-x^2\\).'), T('\\((8-4)-(1-1)=4\\).', '\\((8-4)-(1-1)=4\\).')], T('\\(4\\).', '\\(4\\).'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Trigonometric and logarithmic', 'Lượng giác và lôgarit'), T('Compute \\(\\displaystyle\\int_0^{\\frac\\pi2}(2\\cos x-\\sin x)\\,dx\\) and \\(\\displaystyle\\int_1^e\\dfrac2x\\,dx\\).', 'Tính \\(\\displaystyle\\int_0^{\\frac\\pi2}(2\\cos x-\\sin x)\\,dx\\) và \\(\\displaystyle\\int_1^e\\dfrac2x\\,dx\\).'),
  T('Antiderivatives: \\(2\\sin x+\\cos x\\) and \\(2\\ln|x|\\).', 'Nguyên hàm: \\(2\\sin x+\\cos x\\) và \\(2\\ln|x|\\).'),
  [T('\\((2\\sin x+\\cos x)\\Big|_0^{\\pi/2}=(2+0)-(0+1)=1\\).', '\\((2\\sin x+\\cos x)\\Big|_0^{\\pi/2}=(2+0)-(0+1)=1\\).'), T('\\(2\\ln x\\Big|_1^e=2(1-0)=2\\).', '\\(2\\ln x\\Big|_1^e=2(1-0)=2\\).')], T('\\(1\\) and \\(2\\).', '\\(1\\) và \\(2\\).'))
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Using the properties', 'Dùng tính chất'), T('\\(\\int_0^3f(x)\\,dx=5\\), \\(\\int_0^3g(x)\\,dx=-2\\), \\(\\int_0^1f(x)\\,dx=2\\). Compute \\(\\int_0^3[2f(x)-3g(x)]\\,dx\\), \\(\\int_1^3f(x)\\,dx\\) and \\(\\int_3^0g(x)\\,dx\\).', 'Cho \\(\\int_0^3f(x)\\,dx=5\\), \\(\\int_0^3g(x)\\,dx=-2\\), \\(\\int_0^1f(x)\\,dx=2\\). Tính \\(\\int_0^3[2f(x)-3g(x)]\\,dx\\), \\(\\int_1^3f(x)\\,dx\\) và \\(\\int_3^0g(x)\\,dx\\).'),
  T('Linearity, splitting and swapping the limits.', 'Tính chất tuyến tính, tách cận và đổi cận.'),
  [T('\\(2\\cdot5-3\\cdot(-2)=16\\).', '\\(2\\cdot5-3\\cdot(-2)=16\\).'), T('\\(\\int_1^3f=\\int_0^3f-\\int_0^1f=5-2=3\\).', '\\(\\int_1^3f=\\int_0^3f-\\int_0^1f=5-2=3\\).'), T('\\(\\int_3^0g=-\\int_0^3g=2\\).', '\\(\\int_3^0g=-\\int_0^3g=2\\).')], T('\\(16\\), \\(3\\), \\(2\\).', '\\(16\\), \\(3\\), \\(2\\).'))
assert F(1, 2) + F(4, 2) == F(5, 2)
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('An absolute value', 'Dấu giá trị tuyệt đối'), T('Compute \\(\\displaystyle\\int_0^3|x-1|\\,dx\\).', 'Tính \\(\\displaystyle\\int_0^3|x-1|\\,dx\\).'), T('\\(x-1\\) changes sign at \\(x=1\\).', '\\(x-1\\) đổi dấu tại \\(x=1\\).'),
  [T('\\(\\int_0^1(1-x)\\,dx=\\left(x-\\dfrac{x^2}2\\right)\\Big|_0^1=\\dfrac12\\).', '\\(\\int_0^1(1-x)\\,dx=\\left(x-\\dfrac{x^2}2\\right)\\Big|_0^1=\\dfrac12\\).'), T('\\(\\int_1^3(x-1)\\,dx=\\left(\\dfrac{x^2}2-x\\right)\\Big|_1^3=\\dfrac32-\\left(-\\dfrac12\\right)=2\\).', '\\(\\int_1^3(x-1)\\,dx=\\left(\\dfrac{x^2}2-x\\right)\\Big|_1^3=\\dfrac32-\\left(-\\dfrac12\\right)=2\\).')],
  T('\\(\\dfrac12+2=\\dfrac52\\).', '\\(\\dfrac12+2=\\dfrac52\\).'))
v0, a = 20, 5; T0 = F(v0, a); dist = v0 * T0 - F(a) * T0 * T0 / 2; assert (T0, dist) == (4, 40)
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Will the car stop in time?', 'Ô tô có dừng kịp không?'), T('A car moving at \\(20\\ \\text{m/s}\\) sees an obstacle 35 m ahead and brakes at once; its velocity is \\(v(t)=20-5t\\) (m/s). Does the car stop before the obstacle?', 'Một ô tô đang chạy \\(20\\ \\text{m/s}\\) thì thấy chướng ngại vật cách 35 m và hãm phanh ngay; vận tốc \\(v(t)=20-5t\\) (m/s). Ô tô có dừng trước chướng ngại vật không?'),
  T('Find when \\(v=0\\), then the distance \\(\\int_0^Tv(t)\\,dt\\).', 'Tìm thời điểm \\(v=0\\), rồi tính quãng đường \\(\\int_0^Tv(t)\\,dt\\).'),
  [T('\\(20-5t=0\\Rightarrow t=4\\) s.', '\\(20-5t=0\\Rightarrow t=4\\) s.'), T('\\(s=\\int_0^4(20-5t)\\,dt=\\left(20t-\\dfrac52t^2\\right)\\Big|_0^4=80-40=40\\) m.', '\\(s=\\int_0^4(20-5t)\\,dt=\\left(20t-\\dfrac52t^2\\right)\\Big|_0^4=80-40=40\\) m.')],
  T('No: it needs 40 m but has only 35 m, so it hits the obstacle (unless the driver also steers away).', 'Không: ô tô cần 40 m nhưng chỉ còn 35 m nên sẽ va vào chướng ngại vật (nếu không đánh lái tránh).'))

PROPS = [(False, '\\(\\int_a^bf(x)g(x)\\,dx=\\int_a^bf(x)\\,dx\\cdot\\int_a^bg(x)\\,dx\\) for all continuous \\(f\\), \\(g\\).', '\\(\\int_a^bf(x)g(x)\\,dx=\\int_a^bf(x)\\,dx\\cdot\\int_a^bg(x)\\,dx\\) với mọi hàm liên tục \\(f\\), \\(g\\).'),
         (True, '\\(\\int_b^af(x)\\,dx=-\\int_a^bf(x)\\,dx\\).', '\\(\\int_b^af(x)\\,dx=-\\int_a^bf(x)\\,dx\\).'),
         (True, 'If \\(f\\) is continuous and \\(f(x)\\ge0\\) on \\([a;b]\\) (\\(a\\lt b\\)), then \\(\\int_a^bf(x)\\,dx\\ge0\\).', 'Nếu \\(f\\) liên tục và \\(f(x)\\ge0\\) trên \\([a;b]\\) (\\(a\\lt b\\)) thì \\(\\int_a^bf(x)\\,dx\\ge0\\).')]
def lvl(P):
    A, (a, b) = P['poly']; v = defint(A, a, b); I = integ(A)
    o1 = M4(1, '\\(\\displaystyle\\int_{%d}^{%d}(%s)\\,dx=\\)…' % (a, b, ptex(A)), '\\(\\displaystyle\\int_{%d}^{%d}(%s)\\,dx=\\)…' % (a, b, ptex(A)), fr(v), [fr(ev(I, b)), fr(ev(A, b) - ev(A, a)), fr(-v) if v else '1', fr(v + 1), fr(v + 2)],
            '\\(F(x)=%s\\), \\(F(%d)-F(%d)=%s\\).' % (ptex(I), b, a, fr(v)), '\\(F(x)=%s\\), \\(F(%d)-F(%d)=%s\\).' % (ptex(I), b, a, fr(v)))
    e, ok, wr, ex = S.BASIC[P['basic']]
    o2 = M4(2, '\\(\\displaystyle%s=\\)…' % e, '\\(\\displaystyle%s=\\)…' % e, ok, wr, ex, ex)
    (A0, A1, X), (p, q) = P['prop']; val = p * X + q * (A1 - A0)
    ex3 = '%sf(x)%s%sg(x)' % ({1: '', -1: '-'}.get(q, str(q)), '+' if p > 0 else '-', '' if abs(p) == 1 else str(abs(p)))
    o3 = M4(3, '\\(\\int_0^4f(x)\\,dx=%d\\), \\(\\int_0^1f(x)\\,dx=%d\\), \\(\\int_1^4g(x)\\,dx=%d\\). Then \\(\\int_1^4[%s]\\,dx=\\)…' % (A1, A0, X, ex3),
            'Cho \\(\\int_0^4f(x)\\,dx=%d\\), \\(\\int_0^1f(x)\\,dx=%d\\), \\(\\int_1^4g(x)\\,dx=%d\\). Khi đó \\(\\int_1^4[%s]\\,dx=\\)…' % (A1, A0, X, ex3),
            str(val), [str(q * (A1 + A0) + p * X), str(q * A1 + p * X), str(val + 2), str(-val) if val else '1'], '\\(\\int_1^4f=%d-%d=%d\\); result \\(%d\\cdot%d+(%d)\\cdot%d=%d\\).' % (A1, A0, A1 - A0, q, A1 - A0, p, X, val), '\\(\\int_1^4f=%d-%d=%d\\); kết quả \\(%d\\cdot%d+(%d)\\cdot%d=%d\\).' % (A1, A0, A1 - A0, q, A1 - A0, p, X, val))
    pr = PROPS[P['t4']]; t4 = tf(4, pr[1], pr[2], pr[0], 'Swapping the limits changes the sign; a non-negative integrand on \\([a;b]\\) gives a non-negative integral; there is no product rule.', 'Đổi cận thì đổi dấu; hàm không âm trên \\([a;b]\\) có tích phân không âm; không có quy tắc tích phân của tích như vậy.')
    (m, c), ok5 = P['abs']; real = F(m * m + (c - m) ** 2, 2); claim = real if ok5 else defint({1: 1, 0: -m}, 0, c)
    assert (claim == real) == ok5
    t5 = tf(5, '\\(\\displaystyle\\int_0^{%d}|x-%d|\\,dx=%s\\).' % (c, m, fr(claim)), '\\(\\displaystyle\\int_0^{%d}|x-%d|\\,dx=%s\\).' % (c, m, fr(claim)), ok5,
            'Split at \\(x=%d\\): \\(%s+%s=%s\\).' % (m, fr(F(m * m, 2)), fr(F((c - m) ** 2, 2)), fr(real)), 'Tách tại \\(x=%d\\): \\(%s+%s=%s\\).' % (m, fr(F(m * m, 2)), fr(F((c - m) ** 2, 2)), fr(real)))
    v0, aa = P['brake']; T_ = F(v0, aa); s6v = v0 * T_ - F(aa) * T_ * T_ / 2
    s6 = sh(6, 'A train moving at \\(%d\\ \\text{m/s}\\) brakes with velocity \\(v(t)=%d-%dt\\) (m/s). How many metres does it travel until it stops?' % (v0, v0, aa), 'Một đoàn tàu đang chạy \\(%d\\ \\text{m/s}\\) thì hãm phanh, vận tốc \\(v(t)=%d-%dt\\) (m/s). Tàu đi thêm bao nhiêu mét thì dừng?' % (v0, v0, aa), DE(s6v),
            'Stops at \\(t=%s\\); \\(\\int_0^{%s}(%d-%dt)\\,dt=%s\\).' % (DE(T_), DE(T_), v0, aa, DE(s6v)), 'Dừng tại \\(t=%s\\); \\(\\int_0^{%s}(%d-%dt)\\,dt=%s\\).' % (D(T_), D(T_), v0, aa, D(s6v)))
    r0, r1, Tm = P['tank']; V = r0 * Tm + F(r1) * Tm * Tm / 2
    s7 = sh(7, 'Rain fills a tank at the rate \\(r(t)=%d+%st\\) (litres per hour), \\(0\\le t\\le%d\\). How many litres are collected in these %d hours?' % (r0, DE(r1), Tm, Tm), 'Nước mưa chảy vào bể với tốc độ \\(r(t)=%d+%st\\) (lít/giờ), \\(0\\le t\\le%d\\). Trong %d giờ đó bể hứng được bao nhiêu lít?' % (r0, D(r1), Tm, Tm), DE(V),
            '\\(\\int_0^{%d}r(t)\\,dt=%d\\cdot%d+\\dfrac{%s}{2}\\cdot%d^2=%s\\).' % (Tm, r0, Tm, DE(r1), Tm, DE(V)), '\\(\\int_0^{%d}r(t)\\,dt=%d\\cdot%d+\\dfrac{%s}{2}\\cdot%d^2=%s\\).' % (Tm, r0, Tm, D(r1), Tm, D(V)))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
PP = [dict(poly=({2: 3, 0: -1}, (0, 2)), basic=0, prop=((2, 7, 3), (-1, 2)), t4=0, abs=((1, 3), True), brake=(15, 3), tank=(40, 10, 6)),
      dict(poly=({2: 6, 1: -4, 0: 1}, (1, 3)), basic=4, prop=((-1, 5, 2), (3, 2)), t4=1, abs=((2, 5), False), brake=(24, 4), tank=(30, F(5, 2), 8)),
      dict(poly=({3: 4, 1: -6}, (-1, 2)), basic=5, prop=((4, 10, -3), (2, 3)), t4=2, abs=((3, 4), True), brake=(18, 6), tank=(25, 6, 5))]
practice = three(lvl, PP)
practice = with_self(practice, S.M12S12, start=8)
mistakes = [('<b>\\(F(a)-F(b)\\).</b> The order is upper limit minus lower limit: \\(F(b)-F(a)\\).', '<b>Tính \\(F(a)-F(b)\\).</b> Thứ tự đúng là cận trên trừ cận dưới: \\(F(b)-F(a)\\).'),
            ('<b>Keeping \\(+C\\).</b> In a definite integral the constant cancels; the answer is a number.', '<b>Giữ lại \\(+C\\).</b> Trong tích phân hằng số bị triệt tiêu; kết quả là một số.'),
            ('<b>Dropping the absolute value.</b> \\(\\int_0^3|x-1|dx\\ne\\int_0^3(x-1)dx\\): split where the sign changes.', '<b>Bỏ dấu giá trị tuyệt đối.</b> \\(\\int_0^3|x-1|dx\\ne\\int_0^3(x-1)dx\\): phải tách tại điểm đổi dấu.'),
            ('<b>Plugging into \\(f\\) instead of \\(F\\).</b> Use the antiderivative at the limits, not the integrand.', '<b>Thay cận vào \\(f\\) thay vì \\(F\\).</b> Thay cận vào nguyên hàm, không thay vào hàm dưới dấu tích phân.')]
summary = [('\\(\\int_a^bf(x)\\,dx=F(b)-F(a)\\) (\\(F′=f\\)); \\(\\int_a^a=0\\), \\(\\int_b^a=-\\int_a^b\\).', '\\(\\int_a^bf(x)\\,dx=F(b)-F(a)\\) (\\(F′=f\\)); \\(\\int_a^a=0\\), \\(\\int_b^a=-\\int_a^b\\).'),
           ('Linearity and splitting: \\(\\int_a^b=\\int_a^c+\\int_c^b\\).', 'Tính tuyến tính và tách cận: \\(\\int_a^b=\\int_a^c+\\int_c^b\\).'),
           ('\\(f\\ge0\\): the integral is the area under the curve; \\(\\int_a^bv(t)\\,dt\\): distance; \\(\\int_a^bF′\\): total change.', '\\(f\\ge0\\): tích phân là diện tích hình thang cong; \\(\\int_a^bv(t)\\,dt\\): quãng đường; \\(\\int_a^bF′\\): tổng lượng biến thiên.'),
           ('Key words: definite integral, limits, area, total change.', 'Từ cần nhớ: definite integral, limits, area, total change.')]
checks = [('I can compute a definite integral with the Newton–Leibniz formula.', 'Em tính được tích phân bằng công thức Newton – Leibniz.'), ('I can use the properties of integrals.', 'Em dùng được các tính chất của tích phân.'),
          ('I can handle an absolute value by splitting the interval.', 'Em tính được tích phân có dấu giá trị tuyệt đối.'), ('I can interpret an integral as an area, a distance or a total change.', 'Em hiểu tích phân là diện tích, quãng đường hay tổng lượng biến thiên.')]
LL('g12-int-02', 'Definite Integrals', CV, ('Antiderivatives and Integrals', 'Nguyên hàm và tích phân'), 'integrals', 'definite-integrals', 120, 'Intermediate', 75, ('antiderivatives, table of basic antiderivatives', 'nguyên hàm, bảng nguyên hàm cơ bản'),
   'Definite integrals: Newton–Leibniz formula, properties, absolute values, area under a curve, distance and total change.', 'Bài 12 – Tích phân: công thức Newton – Leibniz, tính chất, hàm chứa dấu giá trị tuyệt đối, diện tích, quãng đường, tổng lượng biến thiên.',
   ['definite integral', 'Newton–Leibniz', 'area', 'total change'], ['tích phân', 'Newton – Leibniz', 'diện tích', 'tổng lượng biến thiên'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g12-int-01'])
