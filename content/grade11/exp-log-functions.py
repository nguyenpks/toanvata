# -*- coding: utf-8 -*-
"""g11-exp-05 = Toán 11 KNTT, Bài 20: Hàm số mũ và hàm số lôgarit. Mã ngân hàng câu hỏi: TOAN11-C6-B20."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g11g as S
from sp_g11g import lg, frn, fac
from sp_g10f import poly

CV = 'Hàm số mũ và hàm số lôgarit'
vocab = defs(CV, [
 ('expfn', 'exponential function', 'hàm số mũ', '\\(y=a^x\\) (\\(a\\gt0\\), \\(a\\ne1\\)); domain \\(\\mathbb R\\), range \\((0;+\\infty)\\).', '\\(y=a^x\\) (\\(a\\gt0\\), \\(a\\ne1\\)); tập xác định \\(\\mathbb R\\), tập giá trị \\((0;+\\infty)\\).', 'The exponential function grows very fast.', '\\(a^x\\)'),
 ('logfn', 'logarithmic function', 'hàm số lôgarit', '\\(y=\\log_a x\\) (\\(a\\gt0\\), \\(a\\ne1\\)); domain \\((0;+\\infty)\\), range \\(\\mathbb R\\).', '\\(y=\\log_a x\\) (\\(a\\gt0\\), \\(a\\ne1\\)); tập xác định \\((0;+\\infty)\\), tập giá trị \\(\\mathbb R\\).', 'The logarithmic function grows slowly.', '\\(\\log_a x\\)'),
 ('asym0', 'horizontal / vertical asymptote', 'tiệm cận ngang / tiệm cận đứng (đồ thị mũ, lôgarit)', '\\(y=a^x\\) approaches the line \\(y=0\\); \\(y=\\log_a x\\) approaches the line \\(x=0\\).', 'đồ thị \\(y=a^x\\) tiến sát đường \\(y=0\\); đồ thị \\(y=\\log_a x\\) tiến sát đường \\(x=0\\).', 'The x-axis is an asymptote of y = 2^x.', ''),
 ('expgrow', 'exponential growth / decay', 'tăng trưởng / suy giảm theo hàm mũ', 'a quantity multiplied by the same factor in equal time steps: \\(N=N_0a^{t}\\).', 'đại lượng được nhân với cùng một hệ số sau mỗi khoảng thời gian bằng nhau: \\(N=N_0a^{t}\\).', 'Bacteria show exponential growth.', '')])
goals = [('recognise exponential and logarithmic functions and their key features;', 'nhận biết [[hàm số mũ]], [[hàm số lôgarit]] và các đặc trưng cơ bản;'),
         ('find domains, decide monotonicity and sketch the graphs;', 'tìm tập xác định, xét tính đơn điệu và vẽ đồ thị;'),
         ('compare numbers using monotonicity;', 'so sánh các số dựa vào tính đơn điệu;'),
         ('model growth and decay with exponential and logarithmic functions.', 'mô hình hóa bài toán [[tăng trưởng / suy giảm theo hàm mũ|tăng trưởng / suy giảm theo hàm mũ]].')]
phrases = [('<b>The base is greater than one, so the function is increasing.</b>', 'Cơ số lớn hơn 1 nên hàm số đồng biến.'), ('<b>The graph always passes through the point zero, one.</b>', 'Đồ thị luôn đi qua điểm \\((0;1)\\).'),
           ('<b>The domain is the positive real numbers.</b>', 'Tập xác định là \\((0;+\\infty)\\).'), ('<b>The two graphs are symmetric about the line \\(y=x\\).</b>', 'Hai đồ thị đối xứng nhau qua đường thẳng \\(y=x\\).'), ('<b>The population doubles every twenty minutes.</b>', 'Số lượng tăng gấp đôi sau mỗi 20 phút.')]
review = T('From Bài 18–19: \\(a^x\\) is defined for every real \\(x\\) when \\(a\\gt0\\); \\(\\log_a x\\) needs \\(x\\gt0\\); \\(\\log_a a^x=x\\), \\(a^{\\log_a x}=x\\). Comparing powers: for \\(a\\gt1\\) a larger exponent gives a larger power.',
           'Từ Bài 18–19: \\(a^x\\) xác định với mọi \\(x\\) khi \\(a\\gt0\\); \\(\\log_a x\\) cần \\(x\\gt0\\); \\(\\log_a a^x=x\\), \\(a^{\\log_a x}=x\\). So sánh lũy thừa: với \\(a\\gt1\\), số mũ lớn hơn thì lũy thừa lớn hơn.')
theory = '<h3>20.1 %s</h3>' % TI('The exponential function', 'Hàm số mũ')
theory += TBL(['', TI('\\(y=a^x\\), \\(a\\gt1\\)', '\\(y=a^x\\), \\(a\\gt1\\)'), TI('\\(y=a^x\\), \\(0\\lt a\\lt1\\)', '\\(y=a^x\\), \\(0\\lt a\\lt1\\)')], [
  [TI('Domain / range', 'Tập xác định / giá trị'), '\\(\\mathbb R\\) / \\((0;+\\infty)\\)', '\\(\\mathbb R\\) / \\((0;+\\infty)\\)'],
  [TI('Monotonicity', 'Tính đơn điệu'), TI('increasing', 'đồng biến'), TI('decreasing', 'nghịch biến')],
  [TI('Special points', 'Điểm đặc biệt'), '\\((0;1)\\), \\((1;a)\\)', '\\((0;1)\\), \\((1;a)\\)'],
  [TI('Asymptote', 'Tiệm cận'), TI('\\(y=0\\) (as \\(x\\to-\\infty\\))', '\\(y=0\\) (khi \\(x\\to-\\infty\\))'), TI('\\(y=0\\) (as \\(x\\to+\\infty\\))', '\\(y=0\\) (khi \\(x\\to+\\infty\\))')]])
theory += '<h3>20.2 %s</h3>' % TI('The logarithmic function', 'Hàm số lôgarit')
theory += TBL(['', TI('\\(y=\\log_a x\\), \\(a\\gt1\\)', '\\(y=\\log_a x\\), \\(a\\gt1\\)'), TI('\\(y=\\log_a x\\), \\(0\\lt a\\lt1\\)', '\\(y=\\log_a x\\), \\(0\\lt a\\lt1\\)')], [
  [TI('Domain / range', 'Tập xác định / giá trị'), '\\((0;+\\infty)\\) / \\(\\mathbb R\\)', '\\((0;+\\infty)\\) / \\(\\mathbb R\\)'],
  [TI('Monotonicity', 'Tính đơn điệu'), TI('increasing', 'đồng biến'), TI('decreasing', 'nghịch biến')],
  [TI('Special points', 'Điểm đặc biệt'), '\\((1;0)\\), \\((a;1)\\)', '\\((1;0)\\), \\((a;1)\\)'],
  [TI('Asymptote', 'Tiệm cận'), TI('\\(x=0\\) (as \\(x\\to0^+\\))', '\\(x=0\\) (khi \\(x\\to0^+\\))'), TI('\\(x=0\\) (as \\(x\\to0^+\\))', '\\(x=0\\) (khi \\(x\\to0^+\\))')]])
theory += GRAPH({'view': [-4, 6, -4, 6], 'functions': [{'f': 'a^x', 'label': 'y = aˣ'}, {'f': 'log(a,x)', 'label': 'y = logₐx'}, {'f': 'x', 'label': 'y = x'}],
  'params': [{'name': 'a', 'min': 0.2, 'max': 4, 'value': 2, 'step': 0.1}], 'family': [{'a': 2, '_labels': {'0': 'y = 2ˣ', '1': 'y = log₂x'}, '_colors': {'0': '#046b4d', '1': '#0e7490'}}, {'a': 0.5, '_labels': {'0': 'y = (1/2)ˣ', '1': 'y = log_{1/2}x'}, '_colors': {'0': '#c2410c', '1': '#be185d'}}], 'points': [{'x': 0, 'y': 1, 'label': '(0; 1)'}, {'x': 1, 'y': 0, 'label': '(1; 0)'}]},
  cap=('Solid colours: \\(a=2\\) (green, teal) and \\(a=\\frac12\\) (orange, pink); for each \\(a\\) the exponential curve passes through \\((0;1)\\) and the logarithmic curve through \\((1;0)\\). Both graphs rise when \\(a\\gt1\\) and fall when \\(0\\lt a\\lt1\\); they are symmetric about \\(y=x\\) because \\(y=\\log_a x\\iff x=a^y\\). (\\(a=1\\) is not allowed.)', 'Màu xanh lá, xanh lơ: \\(a=2\\); màu cam, hồng: \\(a=\\frac12\\); với mỗi \\(a\\), đường mũ đi qua \\((0;1)\\), đường lôgarit đi qua \\((1;0)\\). Hai đồ thị cùng đi lên khi \\(a\\gt1\\), cùng đi xuống khi \\(0\\lt a\\lt1\\); chúng đối xứng qua \\(y=x\\) vì \\(y=\\log_a x\\iff x=a^y\\). (Không xét \\(a=1\\).)'),
  alt=('Graphs of y = a^x and y = log_a x for a = 2 and a = 1/2', 'Đồ thị y = aˣ và y = logₐx với a = 2 và a = 1/2'), height=320)
theory += BOX('mint', ('Comparing', 'So sánh'), T('\\(a\\gt1\\): \\(a^{u}\\lt a^{v}\\iff u\\lt v\\); \\(\\log_a u\\lt\\log_a v\\iff0\\lt u\\lt v\\). \\(0\\lt a\\lt1\\): both inequalities reverse.', '\\(a\\gt1\\): \\(a^{u}\\lt a^{v}\\iff u\\lt v\\); \\(\\log_a u\\lt\\log_a v\\iff0\\lt u\\lt v\\). \\(0\\lt a\\lt1\\): cả hai đổi chiều.'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('\\(y=x^2\\) is a power function, not an exponential one (the variable is in the base). \\(y=a^x\\) never touches \\(Ox\\): \\(a^x\\gt0\\) for all \\(x\\).', '\\(y=x^2\\) là hàm lũy thừa, không phải hàm mũ (biến nằm ở cơ số). Đồ thị \\(y=a^x\\) không bao giờ chạm \\(Ox\\): \\(a^x\\gt0\\) với mọi \\(x\\).'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Domains', 'Tập xác định'), T('Find the domain of \\(y=\\log_3(x^2-4x+3)\\) and of \\(y=\\ln(2-x)+\\sqrt{x+1}\\).', 'Tìm tập xác định của \\(y=\\log_3(x^2-4x+3)\\) và \\(y=\\ln(2-x)+\\sqrt{x+1}\\).'), T('The expression inside a log must be positive.', 'Biểu thức dưới dấu lôgarit phải dương.'),
  [T('\\(x^2-4x+3\\gt0\\iff(x-1)(x-3)\\gt0\\iff x\\lt1\\) or \\(x\\gt3\\).', '\\(x^2-4x+3\\gt0\\iff(x-1)(x-3)\\gt0\\iff x\\lt1\\) hoặc \\(x\\gt3\\).'), T('\\(2-x\\gt0\\) and \\(x+1\\ge0\\iff-1\\le x\\lt2\\).', '\\(2-x\\gt0\\) và \\(x+1\\ge0\\iff-1\\le x\\lt2\\).')],
  T('\\(D=(-\\infty;1)\\cup(3;+\\infty)\\); \\(D=[-1;2)\\).', '\\(D=(-\\infty;1)\\cup(3;+\\infty)\\); \\(D=[-1;2)\\).'))
assert math.pi / 4 < 1 < math.sqrt(2) and 0.7 ** 2.5 > 0.7 ** 3 and math.log(3, 0.5) < math.log(2, 0.5)
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Monotonicity and comparison', 'Tính đơn điệu và so sánh'), T('a) Which are increasing: \\(y=\\left(\\frac{\\pi}{4}\\right)^x\\), \\(y=\\log_{\\sqrt2}x\\), \\(y=e^{-x}\\)? b) Compare \\(0{,}7^{2{,}5}\\) and \\(0{,}7^{3}\\); \\(\\log_{0{,}5}3\\) and \\(\\log_{0{,}5}2\\).', 'a) Hàm số nào đồng biến: \\(y=\\left(\\frac{\\pi}{4}\\right)^x\\), \\(y=\\log_{\\sqrt2}x\\), \\(y=e^{-x}\\)? b) So sánh \\(0{,}7^{2{,}5}\\) và \\(0{,}7^{3}\\); \\(\\log_{0{,}5}3\\) và \\(\\log_{0{,}5}2\\).'),
  T('Look at the base.', 'Xét cơ số.'), [T('a) \\(\\frac\\pi4\\lt1\\): decreasing; \\(\\sqrt2\\gt1\\): increasing; \\(e^{-x}=\\left(\\frac1e\\right)^x\\): decreasing.', 'a) \\(\\frac\\pi4\\lt1\\): nghịch biến; \\(\\sqrt2\\gt1\\): đồng biến; \\(e^{-x}=\\left(\\frac1e\\right)^x\\): nghịch biến.'),
  T('b) Base \\(0{,}7\\lt1\\), \\(2{,}5\\lt3\\Rightarrow0{,}7^{2{,}5}\\gt0{,}7^3\\); base \\(0{,}5\\lt1\\), \\(3\\gt2\\Rightarrow\\log_{0{,}5}3\\lt\\log_{0{,}5}2\\).', 'b) Cơ số \\(0{,}7\\lt1\\), \\(2{,}5\\lt3\\Rightarrow0{,}7^{2{,}5}\\gt0{,}7^3\\); cơ số \\(0{,}5\\lt1\\), \\(3\\gt2\\Rightarrow\\log_{0{,}5}3\\lt\\log_{0{,}5}2\\).')],
  T('Only \\(y=\\log_{\\sqrt2}x\\) is increasing; \\(0{,}7^{2{,}5}\\gt0{,}7^3\\); \\(\\log_{0{,}5}3\\lt\\log_{0{,}5}2\\).', 'Chỉ \\(y=\\log_{\\sqrt2}x\\) đồng biến; \\(0{,}7^{2{,}5}\\gt0{,}7^3\\); \\(\\log_{0{,}5}3\\lt\\log_{0{,}5}2\\).'))
assert 3 ** 2 == 9 and F(1, 2) ** -2 == 4
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Finding the base', 'Tìm cơ số'), T('a) The graph of \\(y=\\log_a x\\) passes through \\(A(9;2)\\). Find \\(a\\). b) The graph of \\(y=a^x\\) passes through \\(B(-2;4)\\). Find \\(a\\) and say whether the function increases.', 'a) Đồ thị \\(y=\\log_a x\\) đi qua \\(A(9;2)\\). Tìm \\(a\\). b) Đồ thị \\(y=a^x\\) đi qua \\(B(-2;4)\\). Tìm \\(a\\) và cho biết hàm số đồng biến hay nghịch biến.'),
  T('Substitute the point; remember \\(a\\gt0\\), \\(a\\ne1\\).', 'Thay tọa độ điểm; nhớ \\(a\\gt0\\), \\(a\\ne1\\).'), [T('a) \\(\\log_a 9=2\\iff a^2=9\\Rightarrow a=3\\) (\\(a\\gt0\\)).', 'a) \\(\\log_a 9=2\\iff a^2=9\\Rightarrow a=3\\) (vì \\(a\\gt0\\)).'), T('b) \\(a^{-2}=4\\iff a^2=\\frac14\\Rightarrow a=\\frac12\\lt1\\): decreasing.', 'b) \\(a^{-2}=4\\iff a^2=\\frac14\\Rightarrow a=\\frac12\\lt1\\): nghịch biến.')],
  T('a) \\(a=3\\); b) \\(a=\\frac12\\), decreasing.', 'a) \\(a=3\\); b) \\(a=\\frac12\\), nghịch biến.'))
assert [math.log2(x + 1) for x in (0, 1, 3, 7)] == [0, 1, 2, 3]
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Shifted graphs', 'Đồ thị tịnh tiến'), T('Find the range and the asymptote of \\(y=2^x-3\\). For \\(f(x)=\\log_2(x+1)\\), find the domain, \\(f(0)\\), \\(f(3)\\), \\(f(7)\\) and the asymptote.', 'Tìm tập giá trị và tiệm cận của đồ thị \\(y=2^x-3\\). Với \\(f(x)=\\log_2(x+1)\\), tìm tập xác định, \\(f(0)\\), \\(f(3)\\), \\(f(7)\\) và tiệm cận.'),
  T('Shift the basic graphs.', 'Tịnh tiến đồ thị cơ bản.'), [T('\\(2^x\\gt0\\Rightarrow2^x-3\\gt-3\\): range \\((-3;+\\infty)\\), asymptote \\(y=-3\\).', '\\(2^x\\gt0\\Rightarrow2^x-3\\gt-3\\): tập giá trị \\((-3;+\\infty)\\), tiệm cận \\(y=-3\\).'),
  T('\\(x+1\\gt0\\iff x\\gt-1\\); \\(f(0)=0\\), \\(f(3)=2\\), \\(f(7)=3\\); asymptote \\(x=-1\\).', '\\(x+1\\gt0\\iff x\\gt-1\\); \\(f(0)=0\\), \\(f(3)=2\\), \\(f(7)=3\\); tiệm cận \\(x=-1\\).')],
  T('\\((-3;+\\infty)\\), \\(y=-3\\); \\(D=(-1;+\\infty)\\), \\(0;2;3\\), \\(x=-1\\).', '\\((-3;+\\infty)\\), \\(y=-3\\); \\(D=(-1;+\\infty)\\), \\(0;2;3\\), \\(x=-1\\).'))
t50 = 20 * math.log2(50); assert abs(t50 - 112.88) < 0.01 and 1000 * 2 ** 3 == 8000
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Bacteria growth', 'Sự sinh trưởng của vi khuẩn'), T('A culture starts with 1000 bacteria and doubles every 20 minutes: \\(N(t)=1000\\cdot2^{t/20}\\) (\\(t\\) in minutes). How many are there after 1 hour? After how long are there 50 000?', 'Một mẻ nuôi cấy có 1000 vi khuẩn, cứ 20 phút tăng gấp đôi: \\(N(t)=1000\\cdot2^{t/20}\\) (\\(t\\) tính bằng phút). Sau 1 giờ có bao nhiêu vi khuẩn? Sau bao lâu có 50 000 vi khuẩn?'),
  T('Use the inverse function \\(t=20\\log_2\\dfrac{N}{1000}\\).', 'Dùng hàm ngược \\(t=20\\log_2\\dfrac{N}{1000}\\).'), [T('\\(N(60)=1000\\cdot2^3=8000\\).', '\\(N(60)=1000\\cdot2^3=8000\\).'), T('\\(2^{t/20}=50\\iff t=20\\log_2 50\\approx112{,}9\\) minutes.', '\\(2^{t/20}=50\\iff t=20\\log_2 50\\approx112{,}9\\) phút.')],
  T('8000 bacteria; about 113 minutes (1 h 53 min).', '8000 vi khuẩn; khoảng 113 phút (1 giờ 53 phút).'))

def lvl(P):
    p, q = P['dom']
    o1 = M4(1, 'The domain of \\(y=\\log_2(%s)\\) is…' % poly([1, -(p + q), p * q]), 'Tập xác định của hàm số \\(y=\\log_2(%s)\\) là…' % poly([1, -(p + q), p * q]), '\\((-\\infty;%d)\\cup(%d;+\\infty)\\)' % (p, q),
            ['\\((%d;%d)\\)' % (p, q), '\\([%d;%d]\\)' % (p, q), '\\(\\mathbb R\\)'], 'Need \\((%s)(%s)\\gt0\\).' % (fac(p), fac(q)), 'Cần \\((%s)(%s)\\gt0\\).' % (fac(p), fac(q)))
    good, bads, want, wen, wvi = P['mono']
    o2 = M4(2, 'Which function is %s %s?' % ('increasing' if want else 'decreasing', wen), 'Hàm số nào %s %s?' % ('đồng biến' if want else 'nghịch biến', wvi), '\\(%s\\)' % good, ['\\(%s\\)' % b for b in bads],
            'Look at the base.', 'Xét cơ số: lớn hơn 1 thì đồng biến, thuộc \\((0;1)\\) thì nghịch biến.')
    kind, xx, k, a = P['base']
    q3 = ('The graph of \\(y=\\log_a x\\) passes through \\((%s;\\,%d)\\). Then \\(a=\\)…' % (frn(xx), k), 'Đồ thị \\(y=\\log_a x\\) đi qua \\((%s;\\,%d)\\). Khi đó \\(a=\\)…' % (frn(xx), k)) if kind == 'log' else \
         ('The graph of \\(y=a^x\\) passes through \\((%d;\\,%s)\\). Then \\(a=\\)…' % (k, frn(xx)), 'Đồ thị \\(y=a^x\\) đi qua \\((%d;\\,%s)\\). Khi đó \\(a=\\)…' % (k, frn(xx)))
    assert F(a) ** k == F(xx)
    o3 = M4(3, q3[0], q3[1], '\\(%s\\)' % frn(a), ['\\(%s\\)' % frn(1 / F(a)), '\\(%s\\)' % frn(F(xx) / k), '\\(%s\\)' % frn(F(a) + 1)], '\\(a^{%d}=%s\\).' % (k, frn(xx)), '\\(a^{%d}=%s\\).' % (k, frn(xx)))
    (e4, v4_), (e5, v5_) = P['tf']
    t4 = tf(4, e4[0], e4[1], v4_, e4[2], e4[3]); t5 = tf(5, e5[0], e5[1], v5_, e5[2], e5[3])
    b6, s6_, x6 = P['val']; v6 = math.log(x6 + s6_, b6); v6 = round(v6); assert b6 ** v6 == x6 + s6_
    s6 = sh(6, '\\(f(x)=\\log_{%d}(x%+d)\\). Compute \\(f(%d)\\).' % (b6, s6_, x6), 'Cho \\(f(x)=\\log_{%d}(x%+d)\\). Tính \\(f(%d)\\).' % (b6, s6_, x6), v6, '\\(\\log_{%d}%d=%d\\).' % (b6, x6 + s6_, v6), '\\(f(%d)=\\log_{%d}%d=%d\\).' % (x6, b6, x6 + s6_, v6))
    N0, T7, t7 = P['bact']; N7 = N0 * 2 ** (t7 // T7); assert t7 % T7 == 0
    s7 = sh(7, 'Bacteria: \\(N(t)=%d\\cdot2^{t/%d}\\) (\\(t\\) in minutes). Find \\(N(%d)\\).' % (N0, T7, t7), 'Vi khuẩn: \\(N(t)=%d\\cdot2^{t/%d}\\) (\\(t\\) tính bằng phút). Tính \\(N(%d)\\).' % (N0, T7, t7), N7,
            '\\(%d\\cdot2^{%d}=%d\\).' % (N0, t7 // T7, N7), '\\(%d\\cdot2^{%d}=%d\\).' % (N0, t7 // T7, N7))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
UA = (('The graph of \\(y=a^x\\) (\\(a\\gt0\\), \\(a\\ne1\\)) lies above the \\(x\\)-axis.', 'Đồ thị hàm số \\(y=a^x\\) (\\(a\\gt0\\), \\(a\\ne1\\)) nằm phía trên trục hoành.', '\\(a^x\\gt0\\) for all \\(x\\).', '\\(a^x\\gt0\\) với mọi \\(x\\).'), True)
UB = (('\\(y=\\log_{\\frac13}x\\) is increasing on \\((0;+\\infty)\\).', 'Hàm số \\(y=\\log_{\\frac13}x\\) đồng biến trên \\((0;+\\infty)\\).', 'Base \\(\\frac13\\lt1\\): decreasing.', 'Cơ số \\(\\frac13\\lt1\\): nghịch biến.'), False)
UC = (('\\(2^{\\sqrt3}\\gt2^{1{,}7}\\).', '\\(2^{\\sqrt3}\\gt2^{1{,}7}\\).', '\\(\\sqrt3\\approx1{,}732\\gt1{,}7\\), base \\(2\\gt1\\).', '\\(\\sqrt3\\approx1{,}732\\gt1{,}7\\), cơ số \\(2\\gt1\\).'), True)
UD = (('The graph of \\(y=\\log_2 x\\) passes through \\((0;1)\\).', 'Đồ thị hàm số \\(y=\\log_2 x\\) đi qua điểm \\((0;1)\\).', '\\(x=0\\) is not in the domain; it passes through \\((1;0)\\).', '\\(x=0\\) không thuộc tập xác định; đồ thị đi qua \\((1;0)\\).'), False)
UE = (('\\(\\log_{0{,}2}5\\lt\\log_{0{,}2}3\\).', '\\(\\log_{0{,}2}5\\lt\\log_{0{,}2}3\\).', 'Base \\(0{,}2\\lt1\\): decreasing, \\(5\\gt3\\).', 'Cơ số \\(0{,}2\\lt1\\): nghịch biến, \\(5\\gt3\\).'), True)
UF = (('The domain of \\(y=\\ln(x-2)\\) is \\([2;+\\infty)\\).', 'Tập xác định của \\(y=\\ln(x-2)\\) là \\([2;+\\infty)\\).', 'Need \\(x-2\\gt0\\): \\((2;+\\infty)\\).', 'Cần \\(x-2\\gt0\\): \\((2;+\\infty)\\).'), False)
PP = [dict(dom=(1, 4), mono=('y=3^x', ['y=\\left(\\frac12\\right)^x', 'y=\\log_{0{,}5}x', 'y=e^{-x}'], True, 'on its domain', 'trên tập xác định của nó'), base=('log', 8, 3, 2), tf=(UA, UB), val=(2, 1, 7), bact=(500, 30, 90)),
      dict(dom=(-2, 3), mono=('y=\\log_{\\frac25}x', ['y=\\ln x', 'y=\\left(\\frac43\\right)^x', 'y=\\log_{\\sqrt5}x'], False, 'on its domain', 'trên tập xác định của nó'), base=('exp', 27, 3, 3), tf=(UC, UD), val=(3, -2, 11), bact=(200, 20, 80)),
      dict(dom=(-4, 0), mono=('y=\\left(\\frac{e}{2}\\right)^x', ['y=\\left(\\frac{2}{e}\\right)^x', 'y=\\left(\\frac{\\pi}{4}\\right)^x', 'y=0{,}9^x'], True, 'on \\(\\mathbb R\\)', 'trên \\(\\mathbb R\\)'), base=('exp', F(1, 4), -2, 2), tf=(UE, UF), val=(5, 4, 21), bact=(1000, 15, 60))]
practice = three(lvl, PP)
practice = with_self(practice, S.M20S11, start=8)
mistakes = [('<b>Treating \\(y=x^3\\) as exponential.</b> In an exponential function the <i>variable is the exponent</i>.', '<b>Coi \\(y=x^3\\) là hàm số mũ.</b> Ở hàm số mũ, <i>biến nằm ở số mũ</i>.'),
            ('<b>Forgetting the domain of \\(\\log_a x\\).</b> The argument must be strictly positive.', '<b>Quên điều kiện của \\(\\log_a x\\).</b> Biểu thức dưới dấu lôgarit phải dương.'),
            ('<b>Not reversing the inequality when \\(0\\lt a\\lt1\\).</b>', '<b>Không đổi chiều khi \\(0\\lt a\\lt1\\).</b>'),
            ('<b>Taking a negative base from \\(a^2=9\\).</b> The base must be positive: \\(a=3\\), not \\(\\pm3\\).', '<b>Nhận cơ số âm từ \\(a^2=9\\).</b> Cơ số phải dương: \\(a=3\\), không phải \\(\\pm3\\).')]
summary = [('\\(y=a^x\\): \\(D=\\mathbb R\\), \\(T=(0;+\\infty)\\), through \\((0;1)\\), asymptote \\(y=0\\).', '\\(y=a^x\\): \\(D=\\mathbb R\\), \\(T=(0;+\\infty)\\), qua \\((0;1)\\), tiệm cận \\(y=0\\).'),
           ('\\(y=\\log_a x\\): \\(D=(0;+\\infty)\\), \\(T=\\mathbb R\\), through \\((1;0)\\), asymptote \\(x=0\\).', '\\(y=\\log_a x\\): \\(D=(0;+\\infty)\\), \\(T=\\mathbb R\\), qua \\((1;0)\\), tiệm cận \\(x=0\\).'),
           ('\\(a\\gt1\\): increasing; \\(0\\lt a\\lt1\\): decreasing. The two graphs are symmetric about \\(y=x\\).', '\\(a\\gt1\\): đồng biến; \\(0\\lt a\\lt1\\): nghịch biến. Hai đồ thị đối xứng qua \\(y=x\\).'),
           ('Key words: exponential function, logarithmic function, asymptote, growth, decay.', 'Từ cần nhớ: exponential function, logarithmic function, asymptote, growth, decay.')]
checks = [('I can find the domain of an exponential or logarithmic function.', 'Em tìm được tập xác định của hàm số mũ, lôgarit.'), ('I can decide whether it increases or decreases.', 'Em xét được tính đồng biến, nghịch biến.'),
          ('I can sketch and read the graphs.', 'Em vẽ và đọc được đồ thị.'), ('I can model growth and decay.', 'Em mô hình hóa được bài toán tăng trưởng, suy giảm.')]
LL('g11-exp-05', 'Exponential and Logarithmic Functions', CV, ('Exponential and Logarithmic Functions', 'Hàm số mũ và hàm số lôgarit'), 'exponential-functions', 'exp-log-functions', 210, 'Intermediate', 70, ('logarithms, powers with real exponents', 'lôgarit, lũy thừa với số mũ thực'),
   'Exponential and logarithmic functions: domains, monotonicity, graphs, comparison and growth models.', 'Bài 20 – Hàm số mũ và hàm số lôgarit: tập xác định, tính đơn điệu, đồ thị, so sánh, mô hình tăng trưởng.',
   ['exponential function', 'logarithmic function', 'graph', 'growth'], ['hàm số mũ', 'hàm số lôgarit', 'đồ thị', 'tăng trưởng'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g11-exp-04'])
