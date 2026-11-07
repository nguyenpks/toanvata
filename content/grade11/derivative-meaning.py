# -*- coding: utf-8 -*-
"""g11-deriv-01 = Toán 11 KNTT, Bài 31: Định nghĩa và ý nghĩa của đạo hàm. Mã ngân hàng câu hỏi: TOAN11-C9-B31.
Soạn lại thay cho g11-derivatives-01 (bài cũ được khóa)."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g11k as S

CV = 'Định nghĩa và ý nghĩa của đạo hàm'
vocab = defs(CV, [
 ('deriv31', 'derivative at a point', 'đạo hàm tại một điểm', 'the limit \\(f′(x_0)=\\lim\\limits_{x\\to x_0}\\dfrac{f(x)-f(x_0)}{x-x_0}\\), if it is finite.', 'giới hạn hữu hạn \\(f′(x_0)=\\lim\\limits_{x\\to x_0}\\dfrac{f(x)-f(x_0)}{x-x_0}\\) (nếu có).', 'The derivative at 3 is 6.', '\\(f′(x_0)\\)'),
 ('instvel', 'instantaneous velocity', 'vận tốc tức thời', 'the derivative of the position function: \\(v(t_0)=s′(t_0)\\).', 'đạo hàm của hàm quãng đường: \\(v(t_0)=s′(t_0)\\).', 'The instantaneous velocity at t = 2 s is 19.6 m/s.', '\\(s′(t_0)\\)'),
 ('avgvel', 'average velocity', 'vận tốc trung bình', 'distance travelled divided by time: \\(\\dfrac{s(t)-s(t_0)}{t-t_0}\\).', 'quãng đường chia cho thời gian: \\(\\dfrac{s(t)-s(t_0)}{t-t_0}\\).', 'The average velocity on [2; 3] is 24.5 m/s.', ''),
 ('margcost', 'marginal cost', 'chi phí biên', 'the derivative \\(C′(x)\\) of the cost function; approximately the cost of one more item.', 'đạo hàm \\(C′(x)\\) của hàm chi phí; xấp xỉ chi phí làm thêm một sản phẩm.', 'The marginal cost at 100 items is 40 thousand đồng.', '\\(C′(x)\\)')])
goals = [('define the derivative at a point as a limit and compute it from the definition;', 'phát biểu định nghĩa [[đạo hàm tại một điểm]] và tính đạo hàm bằng định nghĩa;'),
         ('interpret \\(f′(x_0)\\) as the slope of the tangent and write the tangent equation;', 'hiểu \\(f′(x_0)\\) là [[hệ số góc]] của [[tiếp tuyến]] và viết phương trình tiếp tuyến;'),
         ('interpret the derivative as an instantaneous rate of change (velocity, marginal cost);', 'hiểu đạo hàm là tốc độ thay đổi tức thời ([[vận tốc tức thời]], [[chi phí biên]]);'),
         ('recognise points where a function has no derivative.', 'nhận biết điểm mà hàm số không [[có đạo hàm]].')]
phrases = [('<b>The secant line turns into the tangent line.</b>', 'Cát tuyến dần trở thành tiếp tuyến.'), ('<b>The derivative is the slope of the tangent.</b>', 'Đạo hàm là hệ số góc của tiếp tuyến.'),
           ('<b>The instantaneous velocity at two seconds is twenty metres per second.</b>', 'Vận tốc tức thời tại giây thứ hai là 20 m/s.'), ('<b>Let h tend to zero.</b>', 'Cho h dần tới 0.'), ('<b>The graph has a corner, so there is no derivative there.</b>', 'Đồ thị có góc nhọn nên tại đó không có đạo hàm.')]
review = T('From Chapter V: \\(\\lim\\limits_{x\\to x_0}\\), removing the factor \\(x-x_0\\) in \\(\\frac00\\) limits. From Grade 10: a line with slope \\(k\\) through \\((x_0;y_0)\\) is \\(y=k(x-x_0)+y_0\\).',
           'Từ Chương V: giới hạn \\(\\lim\\limits_{x\\to x_0}\\), khử dạng \\(\\frac00\\) bằng cách rút gọn nhân tử \\(x-x_0\\). Từ lớp 10: đường thẳng hệ số góc \\(k\\) qua \\((x_0;y_0)\\) là \\(y=k(x-x_0)+y_0\\).')

theory = '<h3>31.1 %s</h3>' % TI('Two problems that lead to the derivative', 'Hai bài toán dẫn đến khái niệm đạo hàm')
theory += BOX('blue', ('Velocity and slope', 'Vận tốc và hệ số góc'), UL([
  T('<b>Velocity.</b> A stone falls with \\(s(t)=4{,}9t^2\\) (m). On \\([2;t]\\) its average velocity is \\(\\dfrac{s(t)-s(2)}{t-2}=4{,}9(t+2)\\). As \\(t\\to2\\) this tends to \\(19{,}6\\) m/s: the instantaneous velocity at \\(t=2\\).',
    '<b>Vận tốc.</b> Một hòn đá rơi tự do với \\(s(t)=4{,}9t^2\\) (m). Trên \\([2;t]\\), [[vận tốc trung bình]] là \\(\\dfrac{s(t)-s(2)}{t-2}=4{,}9(t+2)\\). Khi \\(t\\to2\\), giá trị này dần tới \\(19{,}6\\) m/s: [[vận tốc tức thời]] tại \\(t=2\\).'),
  T('<b>Slope.</b> The secant line through \\(M(x_0;f(x_0))\\) and \\(N(x;f(x))\\) has slope \\(\\dfrac{f(x)-f(x_0)}{x-x_0}\\). As \\(N\\to M\\) the secant turns into the tangent at \\(M\\).',
    '<b>Hệ số góc.</b> [[cát tuyến|cát tuyến]] qua \\(M(x_0;f(x_0))\\) và \\(N(x;f(x))\\) có hệ số góc \\(\\dfrac{f(x)-f(x_0)}{x-x_0}\\). Khi \\(N\\to M\\), cát tuyến dần tới tiếp tuyến tại \\(M\\).')]))
theory += GRAPH({'view': [-1, 3.2, -1.5, 6], 'functions': [{'f': 'x^2', 'label': 'y = x²'}, {'f': '3*x-2', 'label': 'y = 3x − 2', 'color': '#7c3aed'}],
                 'tangent': {'f': 0, 'at': 1, 'min': -0.5, 'max': 3}, 'points': [{'x': 1, 'y': 1, 'label': 'M(1; 1)', 'off': [8, -10]}, {'x': 2, 'y': 4, 'label': 'N(2; 4)', 'off': [-10, 8]}]},
                cap=('Secant MN: y = 3x − 2 (slope 3) and the tangent at M(1; 1) (slope 2). As N slides towards M, the slope of MN tends to f′(1) = 2.', 'Cát tuyến MN: y = 3x − 2 (hệ số góc 3) và tiếp tuyến tại M(1; 1) (hệ số góc 2). Khi N trượt dần về M, hệ số góc của MN dần tới f′(1) = 2.'),
                alt=('Parabola y = x squared with a secant line through M and N and the tangent line at M', ''), height=330)
theory += '<h3>31.2 %s</h3>' % TI('Definition', 'Định nghĩa đạo hàm tại một điểm')
theory += BOX('mint', ('Definition', 'Định nghĩa'), T('Let \\(y=f(x)\\) be defined on \\((a;b)\\) containing \\(x_0\\). If the limit \\[f′(x_0)=\\lim_{x\\to x_0}\\dfrac{f(x)-f(x_0)}{x-x_0}=\\lim_{h\\to0}\\dfrac{f(x_0+h)-f(x_0)}{h}\\] exists and is finite, it is the <b>derivative</b> of \\(f\\) at \\(x_0\\). \\(h=\\Delta x\\) is the increment of \\(x\\), \\(\\Delta y=f(x_0+h)-f(x_0)\\) the increment of \\(y\\).',
  'Cho hàm \\(y=f(x)\\) xác định trên \\((a;b)\\) chứa \\(x_0\\). Nếu tồn tại giới hạn hữu hạn \\[f′(x_0)=\\lim_{x\\to x_0}\\dfrac{f(x)-f(x_0)}{x-x_0}=\\lim_{h\\to0}\\dfrac{f(x_0+h)-f(x_0)}{h}\\] thì giới hạn đó là [[đạo hàm tại một điểm|đạo hàm]] của \\(f\\) tại \\(x_0\\). \\(h=\\Delta x\\) là số gia của biến, \\(\\Delta y=f(x_0+h)-f(x_0)\\) là số gia của hàm số.'))
theory += BOX('blue', ('Three steps', 'Ba bước tính đạo hàm bằng định nghĩa'), UL([T('Compute \\(\\Delta y=f(x_0+h)-f(x_0)\\).', 'Tính \\(\\Delta y=f(x_0+h)-f(x_0)\\).'), T('Simplify \\(\\dfrac{\\Delta y}{h}\\) (cancel \\(h\\)).', 'Rút gọn [[tỉ số biến thiên]] \\(\\dfrac{\\Delta y}{h}\\) (triệt tiêu \\(h\\)).'), T('Let \\(h\\to0\\).', 'Cho \\(h\\to0\\).')]))
theory += BOX('mint', ('Results to remember', 'Kết quả cần nhớ'), T('From the definition: \\((c)′=0\\), \\((x)′=1\\), \\((x^2)′=2x\\), \\((x^3)′=3x^2\\), \\(\\left(\\dfrac1x\\right)′=-\\dfrac1{x^2}\\), \\((\\sqrt x)′=\\dfrac1{2\\sqrt x}\\). The function \\(x\\mapsto f′(x)\\) is the <b>derivative function</b>.',
  'Từ định nghĩa: \\((c)′=0\\), \\((x)′=1\\), \\((x^2)′=2x\\), \\((x^3)′=3x^2\\), \\(\\left(\\dfrac1x\\right)′=-\\dfrac1{x^2}\\), \\((\\sqrt x)′=\\dfrac1{2\\sqrt x}\\). Hàm số \\(x\\mapsto f′(x)\\) gọi là <b>hàm đạo hàm</b> (gọi tắt là đạo hàm) của \\(f\\).'))
theory += '<h3>31.3 %s</h3>' % TI('Meaning of the derivative', 'Ý nghĩa của đạo hàm')
theory += BOX('blue', ('Geometric and physical meaning', 'Ý nghĩa hình học và vật lí'), UL([
  T('<b>Geometry:</b> \\(f′(x_0)\\) is the slope of the tangent at \\(M(x_0;f(x_0))\\); the tangent is \\(y=f′(x_0)(x-x_0)+f(x_0)\\).', '<b>Hình học:</b> \\(f′(x_0)\\) là hệ số góc của tiếp tuyến tại [[tiếp điểm]] \\(M(x_0;f(x_0))\\); phương trình tiếp tuyến: \\(y=f′(x_0)(x-x_0)+f(x_0)\\).'),
  T('<b>Physics:</b> \\(v(t_0)=s′(t_0)\\) (velocity); the current \\(I(t_0)=Q′(t_0)\\) where \\(Q\\) is the charge.', '<b>Vật lí:</b> \\(v(t_0)=s′(t_0)\\) (vận tốc tức thời); cường độ dòng điện tức thời \\(I(t_0)=Q′(t_0)\\) với \\(Q\\) là điện lượng.'),
  T('<b>Economics:</b> the marginal cost \\(C′(x_0)\\) approximates the cost of producing item number \\(x_0+1\\).', '<b>Kinh tế:</b> [[chi phí biên]] \\(C′(x_0)\\) xấp xỉ chi phí sản xuất thêm sản phẩm thứ \\(x_0+1\\).')]))
theory += GRAPH({'view': [-3, 3, -1, 3], 'functions': [{'f': 'abs(x)', 'label': 'y = |x|'}]},
                cap=('y = |x| has a corner at 0: secant slopes are −1 on the left, +1 on the right, so f′(0) does not exist (although the function is continuous).', 'y = |x| có góc nhọn tại 0: hệ số góc cát tuyến bằng −1 ở bên trái và +1 ở bên phải, nên không tồn tại f′(0) (dù hàm số liên tục).'),
                alt=('Graph of the absolute value function with a corner at the origin', ''), height=260)
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('If \\(f\\) has a derivative at \\(x_0\\) then \\(f\\) is continuous at \\(x_0\\). The converse is false (example \\(|x|\\) at 0).', 'Nếu \\(f\\) có đạo hàm tại \\(x_0\\) thì \\(f\\) liên tục tại \\(x_0\\). Điều ngược lại không đúng (ví dụ \\(|x|\\) tại 0).'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Using the definition', 'Tính đạo hàm bằng định nghĩa'), T('Use the definition to compute \\(f′(2)\\) for \\(f(x)=x^2+3x\\).', 'Dùng định nghĩa tính \\(f′(2)\\) với \\(f(x)=x^2+3x\\).'),
  T('Follow the three steps.', 'Làm theo ba bước.'), [T('\\(\\Delta y=(2+h)^2+3(2+h)-10=7h+h^2\\).', '\\(\\Delta y=(2+h)^2+3(2+h)-10=7h+h^2\\).'), T('\\(\\dfrac{\\Delta y}{h}=7+h\\to7\\).', '\\(\\dfrac{\\Delta y}{h}=7+h\\to7\\) khi \\(h\\to0\\).')], T('\\(f′(2)=7\\).', '\\(f′(2)=7\\).'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('A tangent line', 'Phương trình tiếp tuyến'), T('Write the tangent to \\(y=x^3\\) at the point with abscissa \\(-1\\).', 'Viết phương trình tiếp tuyến của đồ thị \\(y=x^3\\) tại điểm có hoành độ \\(-1\\).'),
  T('\\((x^3)′=3x^2\\).', '\\((x^3)′=3x^2\\).'), [T('\\(x_0=-1\\), \\(y_0=-1\\), \\(f′(-1)=3\\).', '\\(x_0=-1\\), \\(y_0=-1\\), \\(f′(-1)=3\\).'), T('\\(y=3(x+1)-1\\).', '\\(y=3(x+1)-1\\).')], T('\\(y=3x+2\\).', '\\(y=3x+2\\).'))
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Free fall', 'Rơi tự do'), T('A ball is dropped from a 45 m tower; \\(s(t)=5t^2\\) (m, s; \\(g\\approx10\\)). Find its velocity when it hits the ground.', 'Thả một quả bóng từ đỉnh tháp cao 45 m; quãng đường rơi \\(s(t)=5t^2\\) (m, s; lấy \\(g\\approx10\\)). Tính vận tốc của bóng lúc chạm đất.'),
  T('Find the time first, then \\(v=s′(t)\\).', 'Tìm thời điểm chạm đất, rồi tính \\(v=s′(t)\\).'), [T('\\(5t^2=45\\Rightarrow t=3\\) s.', '\\(5t^2=45\\Rightarrow t=3\\) giây.'), T('\\(s′(t)=10t\\) (by the definition, as for \\(x^2\\)); \\(v(3)=30\\) m/s.', '\\(s′(t)=10t\\) (theo định nghĩa, như với \\(x^2\\)); \\(v(3)=30\\) m/s.')], T('\\(30\\) m/s (\\(108\\) km/h).', '\\(30\\) m/s (khoảng \\(108\\) km/h).'))
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Marginal cost', 'Chi phí biên'), T('A workshop makes \\(x\\) chairs at cost \\(C(x)=0{,}1x^2+40x+800\\) (thousand đồng). Compute \\(C′(50)\\) and compare with \\(C(51)-C(50)\\).', 'Một xưởng sản xuất \\(x\\) chiếc ghế với chi phí \\(C(x)=0{,}1x^2+40x+800\\) (nghìn đồng). Tính \\(C′(50)\\) và so sánh với \\(C(51)-C(50)\\).'),
  T('\\(C′(x)=0{,}2x+40\\).', '\\(C′(x)=0{,}2x+40\\).'), [T('\\(C′(50)=50\\) thousand đồng.', '\\(C′(50)=50\\) nghìn đồng.'), T('\\(C(51)-C(50)=0{,}1(51^2-50^2)+40=50{,}1\\).', '\\(C(51)-C(50)=0{,}1(51^2-50^2)+40=50{,}1\\).')],
  T('\\(C′(50)=50\\): the 51st chair costs about 50 thousand đồng.', '\\(C′(50)=50\\): chiếc ghế thứ 51 tốn khoảng 50 nghìn đồng.'))
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Tangent with a given slope', 'Tiếp tuyến có hệ số góc cho trước'), T('Find the tangents to \\(y=x^2-4x+3\\) that are parallel to \\(y=2x+1\\), and the point where the tangent is horizontal.', 'Viết phương trình tiếp tuyến của \\(y=x^2-4x+3\\) song song với đường thẳng \\(y=2x+1\\), và tìm điểm mà tại đó tiếp tuyến nằm ngang.'),
  T('\\(f′(x)=2x-4\\); parallel lines have equal slopes.', '\\(f′(x)=2x-4\\); hai đường song song có cùng hệ số góc.'),
  [T('\\(2x_0-4=2\\Rightarrow x_0=3\\), \\(f(3)=0\\): \\(y=2(x-3)=2x-6\\) (different from \\(y=2x+1\\)).', '\\(2x_0-4=2\\Rightarrow x_0=3\\), \\(f(3)=0\\): \\(y=2(x-3)=2x-6\\) (khác đường \\(y=2x+1\\)).'), T('Horizontal: \\(2x_0-4=0\\Rightarrow x_0=2\\), point \\((2;-1)\\), the vertex.', 'Nằm ngang: \\(2x_0-4=0\\Rightarrow x_0=2\\), điểm \\((2;-1)\\) là đỉnh parabol.')],
  T('\\(y=2x-6\\); \\((2;-1)\\).', '\\(y=2x-6\\); \\((2;-1)\\).'))
examples = EXFIG(examples, 5, GRAPH({'view': [-1, 5, -3, 5], 'functions': [{'f': 'x^2-4x+3', 'label': 'y = x² − 4x + 3'}], 'tangent': {'f': 0, 'at': [2, 3], 'min': -0.5, 'max': 4.5}},
  cap=('The horizontal tangent at (2; −1) and the tangent y = 2x − 6 at (3; 0).', 'Tiếp tuyến nằm ngang tại (2; −1) và tiếp tuyến y = 2x − 6 tại (3; 0).'), alt=('Parabola with two tangent lines', ''), height=300))


def lvl(P):
    a, b, x0 = P['df']
    v = 2 * a * x0 + b
    o1 = M4(1, 'By definition, for \\(f(x)=%s\\), \\(f′(%d)=\\)…' % (poly_tex([a, b, 0]), x0), 'Dùng định nghĩa, với \\(f(x)=%s\\) thì \\(f′(%d)=\\)…' % (poly_tex([a, b, 0]), x0), '\\(%d\\)' % v,
            ['\\(%d\\)' % (a * x0 * x0 + b * x0), '\\(%d\\)' % (a * x0 + b), '\\(%d\\)' % (2 * a * x0), '\\(%d\\)' % (-v)], '\\(\\dfrac{\\Delta y}{h}=2ax_0+b+ah\\).', '\\(\\dfrac{\\Delta y}{h}=%d+%sh\\to%d\\).' % (v, '' if a == 1 else str(a), v))
    x1 = P['tan']; m, c = 3 * x1 * x1, -2 * x1 ** 3
    L = lambda m_, c_: '\\(y=%s\\)' % poly_tex([m_, c_])
    o2 = M4(2, 'The tangent to \\(y=x^3\\) at the point with abscissa \\(%d\\) is…' % x1, 'Tiếp tuyến của đồ thị \\(y=x^3\\) tại điểm có hoành độ \\(%d\\) là…' % x1, L(m, c),
            [L(m, -c), L(m, x1 ** 3), L(3 * x1, c), L(-m, c)], '\\(y=3x_0^2(x-x_0)+x_0^3\\).', '\\(f′(%d)=%d\\), \\(f(%d)=%d\\): \\(y=%d(x-(%d))+(%d)\\).' % (x1, m, x1, x1 ** 3, m, x1, x1 ** 3))
    k, t0 = P['vel']
    o3 = M4(3, 'An object moves with \\(s(t)=%dt^2\\) (m, s). Its instantaneous velocity at \\(t=%d\\) is…' % (k, t0), 'Một vật chuyển động theo \\(s(t)=%dt^2\\) (m, s). Vận tốc tức thời tại \\(t=%d\\) là…' % (k, t0), '\\(%d\\) m/s' % (2 * k * t0),
            ['\\(%d\\) m/s' % (k * t0 * t0), '\\(%d\\) m/s' % (k * t0), '\\(%d\\) m/s' % (k * (2 * t0 + 1)), '\\(%d\\) m/s' % (4 * k * t0)], '\\(v=s′(t)=%dt\\).' % (2 * k), '\\(v(t)=s′(t)=%dt\\); vận tốc trung bình trên \\([%d;%d]\\) là \\(%d\\) m/s, khác vận tốc tức thời.' % (2 * k, t0, t0 + 1, k * (2 * t0 + 1)))
    (se, sv), v4 = P['t4']
    t4 = tf(4, se, sv, v4, 'Recall the geometric meaning.', 'Nhớ lại ý nghĩa hình học, mối liên hệ với tính liên tục.')
    (te, tv), v5 = P['t5']
    t5 = tf(5, te, tv, v5, 'Average vs instantaneous.', 'Phân biệt tốc độ trung bình và tức thời.')
    p, q, x2 = P['slope']
    s6 = sh(6, 'Find the slope of the tangent to \\(y=%s\\) at \\(x=%d\\).' % (poly_tex([1, 0, p, q]), x2), 'Tìm hệ số góc của tiếp tuyến của đồ thị \\(y=%s\\) tại điểm có hoành độ \\(x=%d\\).' % (poly_tex([1, 0, p, q]), x2),
            3 * x2 * x2 + p, '\\(f′(x)=3x^2%+d\\).' % p, '\\(f′(x)=3x^2%+d\\), \\(f′(%d)=%d\\).' % (p, x2, 3 * x2 * x2 + p))
    a7, b7, n7 = P['cost']
    s7 = sh(7, 'Cost \\(C(x)=%s\\,x^2+%dx+1000\\) (thousand đồng). Find the marginal cost \\(C′(%d)\\).' % (fr(a7), b7, n7), 'Chi phí \\(C(x)=%s\\,x^2+%dx+1000\\) (nghìn đồng) khi sản xuất \\(x\\) sản phẩm. Tính chi phí biên \\(C′(%d)\\).' % (fr(a7), b7, n7),
            int(2 * a7 * n7 + b7), '\\(C′(x)=2ax+b\\).', '\\(C′(x)=%s x+%d\\), \\(C′(%d)=%d\\).' % (fr(2 * a7), b7, n7, int(2 * a7 * n7 + b7)))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]


def poly_tex(c):
    return S.poly(c)


PP = [dict(df=(1, -3, 4), tan=1, vel=(5, 2),
           t4=(('If \\(f′(x_0)=0\\), the tangent at \\(x_0\\) is horizontal.', 'Nếu \\(f′(x_0)=0\\) thì tiếp tuyến tại điểm có hoành độ \\(x_0\\) song song hoặc trùng với trục \\(Ox\\).'), True),
           t5=(('The average velocity on \\([2;3]\\) always equals the instantaneous velocity at \\(t=2\\).', 'Vận tốc trung bình trên \\([2;3]\\) luôn bằng vận tốc tức thời tại \\(t=2\\).'), False), slope=(-2, 1, 2), cost=(F(1, 10), 30, 100)),
      dict(df=(2, 1, -1), tan=-1, vel=(4, 3),
           t4=(('If \\(f\\) is continuous at \\(x_0\\) then \\(f\\) has a derivative at \\(x_0\\).', 'Nếu \\(f\\) liên tục tại \\(x_0\\) thì \\(f\\) có đạo hàm tại \\(x_0\\).'), False),
           t5=(('If \\(f′(x_0)\\gt0\\), the tangent at \\(x_0\\) goes up from left to right.', 'Nếu \\(f′(x_0)\\gt0\\) thì tiếp tuyến tại \\(x_0\\) đi lên từ trái sang phải.'), True), slope=(1, -4, -1), cost=(F(1, 5), 50, 40)),
      dict(df=(-1, 4, 3), tan=2, vel=(3, 4),
           t4=(('\\(y=|x-1|\\) has no derivative at \\(x=1\\).', 'Hàm số \\(y=|x-1|\\) không có đạo hàm tại \\(x=1\\).'), True),
           t5=(('If \\(s(t)\\) is the position, \\(s′(t_0)\\) is the average velocity on \\([0;t_0]\\).', 'Nếu \\(s(t)\\) là quãng đường thì \\(s′(t_0)\\) là vận tốc trung bình trên \\([0;t_0]\\).'), False), slope=(-5, 2, -2), cost=(F(1, 2), 20, 30))]
practice = three(lvl, PP)
practice = with_self(practice, S.M31S11, start=8)
mistakes = [('<b>Forgetting that \\(h\\to0\\) only at the end.</b> Cancel \\(h\\) first, then take the limit.', '<b>Cho \\(h=0\\) quá sớm.</b> Phải rút gọn \\(h\\) trước rồi mới lấy giới hạn.'),
            ('<b>Using \\(f(x_0)\\) as the slope.</b> The slope is \\(f′(x_0)\\); \\(f(x_0)\\) is the ordinate of the point.', '<b>Lấy \\(f(x_0)\\) làm hệ số góc.</b> Hệ số góc là \\(f′(x_0)\\); \\(f(x_0)\\) là tung độ tiếp điểm.'),
            ('<b>Confusing average and instantaneous velocity.</b>', '<b>Nhầm vận tốc trung bình với vận tốc tức thời.</b>'),
            ('<b>Thinking continuous implies differentiable.</b> \\(|x|\\) is a counterexample.', '<b>Cho rằng liên tục thì có đạo hàm.</b> Hàm \\(|x|\\) là phản ví dụ.')]
summary = [('\\(f′(x_0)=\\lim\\limits_{h\\to0}\\dfrac{f(x_0+h)-f(x_0)}{h}\\).', '\\(f′(x_0)=\\lim\\limits_{h\\to0}\\dfrac{f(x_0+h)-f(x_0)}{h}\\).'), ('Tangent: \\(y=f′(x_0)(x-x_0)+f(x_0)\\).', 'Tiếp tuyến: \\(y=f′(x_0)(x-x_0)+f(x_0)\\).'),
           ('\\(v(t)=s′(t)\\); marginal cost \\(C′(x)\\); differentiable \\(\\Rightarrow\\) continuous.', '\\(v(t)=s′(t)\\); chi phí biên \\(C′(x)\\); có đạo hàm \\(\\Rightarrow\\) liên tục.'), ('Key words: derivative, tangent, slope, instantaneous velocity, marginal cost.', 'Từ cần nhớ: derivative, tangent, slope, instantaneous velocity, marginal cost.')]
checks = [('I can compute a derivative from the definition.', 'Em tính được đạo hàm bằng định nghĩa.'), ('I can write a tangent equation.', 'Em viết được phương trình tiếp tuyến.'), ('I can explain velocity as a derivative.', 'Em giải thích được vận tốc tức thời là đạo hàm.'), ('I can spot points without a derivative.', 'Em nhận ra điểm hàm số không có đạo hàm.')]
LL('g11-deriv-01', 'Definition and Meaning of the Derivative', CV, ('Derivatives', 'Đạo hàm'), 'derivatives', 'derivative-meaning', 320, 'Intermediate', 60, ('limits of functions', 'giới hạn của hàm số'),
   'The derivative at a point, tangent lines, instantaneous velocity and marginal cost, points without a derivative.', 'Bài 31 – Định nghĩa đạo hàm tại một điểm; ý nghĩa hình học (tiếp tuyến), vật lí (vận tốc tức thời) và kinh tế (chi phí biên).',
   ['derivative', 'tangent line', 'instantaneous velocity'], ['đạo hàm', 'tiếp tuyến', 'vận tốc tức thời'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g11-limits-05'])
