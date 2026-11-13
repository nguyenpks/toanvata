# -*- coding: utf-8 -*-
"""g11-limits-04 = Toán 11 KNTT, Bài 16: Giới hạn của hàm số. Mã ngân hàng câu hỏi: TOAN11-C5-B16.
(Bài cũ g11-limits-02 được giữ nhưng tạm khóa: đã soạn lại thành bài này.)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g11e as S
from sp_g11e import LX, poly

CV = 'Giới hạn của hàm số'
vocab = defs(CV, [
 ('flim', 'limit of a function', 'giới hạn của hàm số', '\\(\\lim\\limits_{x\\to x_0}f(x)=L\\): \\(f(x)\\) gets as close to \\(L\\) as we like when \\(x\\) is close enough to \\(x_0\\) (\\(x\\ne x_0\\)).', '\\(\\lim\\limits_{x\\to x_0}f(x)=L\\): \\(f(x)\\) gần \\(L\\) tùy ý khi \\(x\\) đủ gần \\(x_0\\) (\\(x\\ne x_0\\)).', 'The limit of \\(f\\) at 1 is 2.', ''),
 ('oneside', 'one-sided limit', 'giới hạn một phía', 'the limit when \\(x\\) approaches \\(x_0\\) only from the right (\\(x_0^+\\)) or only from the left (\\(x_0^-\\)).', 'giới hạn khi \\(x\\) dần tới \\(x_0\\) chỉ từ bên phải (\\(x_0^+\\)) hoặc chỉ từ bên trái (\\(x_0^-\\)).', 'The right-hand limit at 2 is \\(+\\infty\\).', '\\(x_0^\\pm\\)'),
 ('indet', 'indeterminate form', 'dạng vô định', 'an expression like \\(\\frac00\\) or \\(\\frac\\infty\\infty\\) whose limit cannot be read off directly.', 'biểu thức dạng \\(\\frac00\\), \\(\\frac\\infty\\infty\\)… chưa thể kết luận ngay giới hạn.', 'The limit has the form 0 over 0.', ''),
 ('factor', 'factorise', 'phân tích thành nhân tử', 'write a polynomial as a product, e.g. \\(x^2-1=(x-1)(x+1)\\).', 'viết đa thức thành tích, ví dụ \\(x^2-1=(x-1)(x+1)\\).', 'Factorise and cancel \\(x-1\\).', ''),
 ('approach', 'approach (tend to)', 'dần tới', '\\(x\\to x_0\\): \\(x\\) takes values closer and closer to \\(x_0\\).', '\\(x\\to x_0\\): \\(x\\) nhận các giá trị ngày càng gần \\(x_0\\).', 'As \\(x\\) approaches 2…', '\\(\\to\\)'),
 ('concen', 'concentration', 'nồng độ', 'amount of substance per unit volume, e.g. grams per litre.', 'lượng chất trong một đơn vị thể tích, ví dụ gam trên lít.', 'The concentration tends to 7.5 g/l.', '')])
goals = [('find the limit of a function at a point and at infinity;', 'tìm [[giới hạn của hàm số]] tại một điểm và tại vô cực;'),
         ('remove the indeterminate form \\(\\frac00\\) by factorising or using the conjugate;', 'khử [[dạng vô định]] \\(\\frac00\\) bằng cách [[phân tích thành nhân tử]] hoặc nhân liên hợp;'),
         ('use one-sided limits and decide whether a limit exists;', 'dùng [[giới hạn một phía]] và xét sự tồn tại của giới hạn;'),
         ('recognise infinite limits and use limits in real models.', 'nhận biết giới hạn vô cực và vận dụng vào mô hình thực tế.')]
phrases = [('<b>Find the limit of the function as \\(x\\) tends to 1.</b>', 'Tìm giới hạn của hàm số khi \\(x\\) dần tới 1.'), ('<b>The limit has the form zero over zero.</b>', 'Giới hạn có dạng 0 chia 0.'), ('<b>Factorise and simplify.</b>', 'Phân tích thành nhân tử và rút gọn.'),
           ('<b>The left-hand and right-hand limits are different.</b>', 'Giới hạn bên trái và bên phải khác nhau.'), ('<b>The limit does not exist.</b>', 'Giới hạn không tồn tại.')]
review = T('From Lesson 15: \\(\\lim\\frac1{n^k}=0\\); limits respect \\(+,-,\\times,:\\); \\(\\frac{\\text{number}\\ne0}{\\to0^+}\\to\\pm\\infty\\). Algebra: \\(a^2-b^2=(a-b)(a+b)\\), \\(a^3-b^3=(a-b)(a^2+ab+b^2)\\), \\(\\sqrt A-B=\\dfrac{A-B^2}{\\sqrt A+B}\\).', 'Từ Bài 15: \\(\\lim\\frac1{n^k}=0\\); giới hạn tương thích với \\(+,-,\\times,:\\); số khác 0 chia cho đại lượng dần tới 0 thì dần tới \\(\\pm\\infty\\). Đại số: \\(a^2-b^2=(a-b)(a+b)\\), \\(a^3-b^3=(a-b)(a^2+ab+b^2)\\), \\(\\sqrt A-B=\\dfrac{A-B^2}{\\sqrt A+B}\\).')
theory = '<h3>16.1 %s</h3>' % TI('Limit at a point', 'Giới hạn hữu hạn tại một điểm')
theory += BOX('blue', ('Definition', 'Định nghĩa'), T('Let \\(f\\) be defined near \\(x_0\\) (maybe not at \\(x_0\\)). \\(\\lim\\limits_{x\\to x_0}f(x)=L\\) if for every sequence \\(x_n\\to x_0\\) (\\(x_n\\ne x_0\\)) we have \\(f(x_n)\\to L\\).', 'Cho \\(f\\) xác định trên một khoảng chứa \\(x_0\\) (có thể trừ \\(x_0\\)). \\(\\lim\\limits_{x\\to x_0}f(x)=L\\) nếu với mọi dãy \\(x_n\\to x_0\\) (\\(x_n\\ne x_0\\)) ta có \\(f(x_n)\\to L\\).'))
theory += GRAPH({'view': [-3, 4, -2, 5], 'functions': [{'f': '(x^2-1)/(x-1)', 'label': 'y = (x² − 1)/(x − 1)'}], 'holes': [[1, 2, '(1; 2)']]},
  cap=('\\(f(x)=\\dfrac{x^2-1}{x-1}\\) is not defined at 1 (open circle), but \\(f(x)=x+1\\) for \\(x\\ne1\\), so \\(\\lim\\limits_{x\\to1}f(x)=2\\).', '\\(f(x)=\\dfrac{x^2-1}{x-1}\\) không xác định tại 1 (chấm rỗng), nhưng \\(f(x)=x+1\\) với \\(x\\ne1\\) nên \\(\\lim\\limits_{x\\to1}f(x)=2\\).'), alt=('A line with a hole at x = 1', ''), height=300)
theory += BOX('mint', ('Rules', 'Quy tắc'), UL([T('\\(\\lim\\limits_{x\\to x_0}c=c\\), \\(\\lim\\limits_{x\\to x_0}x=x_0\\); limits respect \\(+,-,\\times,:\\) (denominator limit \\(\\ne0\\)) and \\(\\sqrt{\\ }\\).', '\\(\\lim\\limits_{x\\to x_0}c=c\\), \\(\\lim\\limits_{x\\to x_0}x=x_0\\); giới hạn tương thích với \\(+,-,\\times,:\\) (giới hạn của mẫu khác 0) và \\(\\sqrt{\\ }\\).'),
  T('Polynomials and rational functions defined at \\(x_0\\): just substitute \\(x=x_0\\).', 'Đa thức, phân thức xác định tại \\(x_0\\): thay trực tiếp \\(x=x_0\\).'),
  T('Form \\(\\frac00\\): factorise \\((x-x_0)\\) and cancel, or multiply by the conjugate.', 'Dạng \\(\\frac00\\): phân tích để xuất hiện \\((x-x_0)\\) rồi rút gọn, hoặc nhân liên hợp.')]))
theory += BOX('blue', ('One-sided limits', 'Giới hạn một phía'), T('\\(\\lim\\limits_{x\\to x_0^+}f(x)\\) uses only \\(x\\gt x_0\\); \\(\\lim\\limits_{x\\to x_0^-}f(x)\\) only \\(x\\lt x_0\\). \\(\\lim\\limits_{x\\to x_0}f(x)=L\\iff\\) both one-sided limits equal \\(L\\).', '\\(\\lim\\limits_{x\\to x_0^+}f(x)\\) chỉ xét \\(x\\gt x_0\\); \\(\\lim\\limits_{x\\to x_0^-}f(x)\\) chỉ xét \\(x\\lt x_0\\). \\(\\lim\\limits_{x\\to x_0}f(x)=L\\iff\\) cả hai giới hạn một phía đều bằng \\(L\\).'))
theory += '<h3>16.2 %s</h3>' % TI('Limits at infinity and infinite limits', 'Giới hạn tại vô cực và giới hạn vô cực')
theory += BOX('mint', ('Basic facts', 'Kết quả cơ bản'), UL([T('\\(\\lim\\limits_{x\\to\\pm\\infty}\\dfrac{c}{x^k}=0\\); for a rational function divide by the highest power of \\(x\\) in the denominator.', '\\(\\lim\\limits_{x\\to\\pm\\infty}\\dfrac{c}{x^k}=0\\); với phân thức, chia tử và mẫu cho lũy thừa bậc cao nhất của \\(x\\) ở mẫu.'),
  T('\\(\\lim\\limits_{x\\to+\\infty}x^k=+\\infty\\); \\(\\lim\\limits_{x\\to a^+}\\dfrac1{x-a}=+\\infty\\), \\(\\lim\\limits_{x\\to a^-}\\dfrac1{x-a}=-\\infty\\).', '\\(\\lim\\limits_{x\\to+\\infty}x^k=+\\infty\\); \\(\\lim\\limits_{x\\to a^+}\\dfrac1{x-a}=+\\infty\\), \\(\\lim\\limits_{x\\to a^-}\\dfrac1{x-a}=-\\infty\\).'),
  T('If \\(f\\to L\\ne0\\) and \\(g\\to0\\) with a constant sign, then \\(\\dfrac fg\\to\\pm\\infty\\) (sign rule).', 'Nếu \\(f\\to L\\ne0\\) và \\(g\\to0\\) với dấu không đổi thì \\(\\dfrac fg\\to\\pm\\infty\\) (theo quy tắc dấu).')]))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('Never "cancel" before checking the form. \\(\\frac00\\) is not 0 and not 1. A limit at \\(x_0\\) does not care about the value \\(f(x_0)\\).', 'Không rút gọn trước khi xét dạng. \\(\\frac00\\) không bằng 0 cũng không bằng 1. Giới hạn tại \\(x_0\\) không phụ thuộc giá trị \\(f(x_0)\\).'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Substitution', 'Thay trực tiếp'), T('Find \\(%s(x^2+3x-1)\\) and \\(%s\\dfrac{2x+1}{x+2}\\).' % (LX(2), LX(1)), 'Tính \\(%s(x^2+3x-1)\\) và \\(%s\\dfrac{2x+1}{x+2}\\).' % (LX(2), LX(1))),
  T('Both functions are defined at the point.', 'Cả hai hàm số đều xác định tại điểm đang xét.'), [T('\\(4+6-1=9\\).', '\\(4+6-1=9\\).'), T('\\(\\dfrac{2+1}{1+2}=1\\).', '\\(\\dfrac{2+1}{1+2}=1\\).')], T('\\(9\\) and \\(1\\).', '\\(9\\) và \\(1\\).'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Form \\(\\frac00\\)', 'Dạng \\(\\frac00\\)'), T('Find \\(%s\\dfrac{x^2-5x+6}{x-3}\\) and \\(%s\\dfrac{\\sqrt{x+4}-2}{x}\\).' % (LX(3), LX(0)), 'Tính \\(%s\\dfrac{x^2-5x+6}{x-3}\\) và \\(%s\\dfrac{\\sqrt{x+4}-2}{x}\\).' % (LX(3), LX(0))),
  T('Substituting gives \\(\\frac00\\): factorise / use the conjugate.', 'Thay vào được \\(\\frac00\\): phân tích nhân tử / nhân liên hợp.'),
  [T('\\(\\dfrac{(x-2)(x-3)}{x-3}=x-2\\to1\\).', '\\(\\dfrac{(x-2)(x-3)}{x-3}=x-2\\to1\\).'), T('\\(\\dfrac{(x+4)-4}{x(\\sqrt{x+4}+2)}=\\dfrac{1}{\\sqrt{x+4}+2}\\to\\dfrac14\\).', '\\(\\dfrac{(x+4)-4}{x(\\sqrt{x+4}+2)}=\\dfrac{1}{\\sqrt{x+4}+2}\\to\\dfrac14\\).')],
  T('\\(1\\) and \\(\\dfrac14\\).', '\\(1\\) và \\(\\dfrac14\\).'))
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Does the limit exist?', 'Giới hạn có tồn tại không?'), T('\\(f(x)=x^2\\) for \\(x\\lt1\\), \\(f(x)=2x-3\\) for \\(x\\ge1\\). Find the one-sided limits at 1. Does \\(\\lim\\limits_{x\\to1}f(x)\\) exist? What value of the constant term (instead of \\(-3\\)) would make it exist?', 'Cho \\(f(x)=x^2\\) khi \\(x\\lt1\\), \\(f(x)=2x-3\\) khi \\(x\\ge1\\). Tìm các giới hạn một phía tại 1. \\(\\lim\\limits_{x\\to1}f(x)\\) có tồn tại không? Thay \\(-3\\) bằng số nào thì giới hạn tồn tại?'),
  T('Use the formula of each side.', 'Dùng công thức của từng phía.'),
  [T('\\(\\lim\\limits_{x\\to1^-}x^2=1\\); \\(\\lim\\limits_{x\\to1^+}(2x-3)=-1\\).', '\\(\\lim\\limits_{x\\to1^-}x^2=1\\); \\(\\lim\\limits_{x\\to1^+}(2x-3)=-1\\).'), T('\\(1\\ne-1\\): no limit. With \\(2x+c\\): \\(2+c=1\\iff c=-1\\).', '\\(1\\ne-1\\): không có giới hạn. Với \\(2x+c\\): \\(2+c=1\\iff c=-1\\).')],
  T('The limit does not exist; it exists if the term is \\(-1\\) (i.e. \\(f(x)=2x-1\\) for \\(x\\ge1\\)).', 'Giới hạn không tồn tại; nó tồn tại nếu thay bằng \\(-1\\) (tức \\(f(x)=2x-1\\) khi \\(x\\ge1\\)).'))
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('At infinity and near a vertical line', 'Tại vô cực và gần đường thẳng đứng'), T('Find \\(%s\\dfrac{3x^2-x}{x^2+2}\\), \\(\\lim\\limits_{x\\to2^+}\\dfrac{1}{x-2}\\) and \\(\\lim\\limits_{x\\to2^-}\\dfrac{1}{x-2}\\).' % LX('+\\infty'), 'Tính \\(%s\\dfrac{3x^2-x}{x^2+2}\\), \\(\\lim\\limits_{x\\to2^+}\\dfrac{1}{x-2}\\) và \\(\\lim\\limits_{x\\to2^-}\\dfrac{1}{x-2}\\).' % LX('+\\infty')),
  T('Divide by \\(x^2\\); look at the sign of \\(x-2\\).', 'Chia cho \\(x^2\\); xét dấu của \\(x-2\\).'), [T('\\(\\dfrac{3-\\frac1x}{1+\\frac2{x^2}}\\to3\\).', '\\(\\dfrac{3-\\frac1x}{1+\\frac2{x^2}}\\to3\\).'), T('\\(x\\to2^+\\): \\(x-2\\to0^+\\), so \\(+\\infty\\); \\(x\\to2^-\\): \\(x-2\\to0^-\\), so \\(-\\infty\\).', '\\(x\\to2^+\\): \\(x-2\\to0^+\\) nên \\(+\\infty\\); \\(x\\to2^-\\): \\(x-2\\to0^-\\) nên \\(-\\infty\\).')],
  T('\\(3\\); \\(+\\infty\\); \\(-\\infty\\).', '\\(3\\); \\(+\\infty\\); \\(-\\infty\\).'))
assert F(30, 4) == F(15, 2)
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Salt water in a tank', 'Nước muối trong bể'), T('A tank holds 200 l of pure water. Salt water with 30 g of salt per litre is pumped in at 4 l/min. After \\(t\\) minutes the concentration is \\(C(t)=\\dfrac{30\\cdot4t}{200+4t}\\) (g/l). What happens to \\(C(t)\\) after a very long time?', 'Một bể chứa 200 lít nước tinh khiết. Bơm vào bể nước muối nồng độ 30 g/l với tốc độ 4 lít/phút. Sau \\(t\\) phút, nồng độ muối trong bể là \\(C(t)=\\dfrac{30\\cdot4t}{200+4t}\\) (g/l). Nồng độ thay đổi thế nào sau rất lâu?'),
  T('Find \\(\\lim\\limits_{t\\to+\\infty}C(t)\\).', 'Tìm \\(\\lim\\limits_{t\\to+\\infty}C(t)\\).'), [T('\\(C(t)=\\dfrac{120t}{200+4t}=\\dfrac{120}{\\frac{200}t+4}\\).', '\\(C(t)=\\dfrac{120t}{200+4t}=\\dfrac{120}{\\frac{200}t+4}\\).'), T('\\(\\dfrac{200}{t}\\to0\\), so \\(C(t)\\to\\dfrac{120}{4}=30\\).', '\\(\\dfrac{200}{t}\\to0\\) nên \\(C(t)\\to\\dfrac{120}{4}=30\\).')],
  T('\\(C(t)\\to30\\) g/l: the water in the tank becomes almost as salty as the water pumped in, but never more.', '\\(C(t)\\to30\\) g/l: nước trong bể ngày càng mặn gần bằng nước bơm vào, nhưng không bao giờ mặn hơn.'))

def lvl(P):
    a, b = P['fac']; v1 = a - b
    o1 = M4(1, '\\(%s\\dfrac{%s}{x%+d}=\\)…' % (LX(a), poly([1, -(a + b), a * b], 'x'), -a), '\\(%s\\dfrac{%s}{x%+d}=\\)…' % (LX(a), poly([1, -(a + b), a * b], 'x'), -a), str(v1), [str(a + b), str(b - a), '0', str(v1 + 2)],
            '\\(\\dfrac{(x%+d)(x%+d)}{x%+d}=x%+d\\to%d\\).' % (-a, -b, -a, -b, v1), '\\(\\dfrac{(x%+d)(x%+d)}{x%+d}=x%+d\\to%d\\).' % (-a, -b, -a, -b, v1))
    k = P['conj']; v2 = F(1, 2 * k)
    o2 = M4(2, '\\(%s\\dfrac{\\sqrt{x+%d}-%d}{x}=\\)…' % (LX(0), k * k, k), '\\(%s\\dfrac{\\sqrt{x+%d}-%d}{x}=\\)…' % (LX(0), k * k, k), fr(v2), ['0', fr(F(1, k)), '+\\infty'],
            'Conjugate: \\(\\dfrac{1}{\\sqrt{x+%d}+%d}\\to%s\\).' % (k * k, k, fr(v2)), 'Nhân liên hợp: \\(\\dfrac{1}{\\sqrt{x+%d}+%d}\\to%s\\).' % (k * k, k, fr(v2)))
    nu, de, side = P['inf']; v3 = F(nu[0], de[0])
    o3 = M4(3, '\\(%s\\dfrac{%s}{%s}=\\)…' % (LX(side), poly(nu, 'x'), poly(de, 'x')), '\\(%s\\dfrac{%s}{%s}=\\)…' % (LX(side), poly(nu, 'x'), poly(de, 'x')), fr(v3), [fr(F(nu[-1], de[-1])), side, '0', fr(-v3)],
            'Divide by \\(x^{%d}\\): the ratio of leading coefficients.' % (len(de) - 1), 'Chia tử và mẫu cho \\(x^{%d}\\): tỉ số các hệ số bậc cao nhất.' % (len(de) - 1))
    a4, c4, sd, claim = P['side']; real = '+\\infty' if (c4 > 0) == (sd == '+') else '-\\infty'
    t4 = tf(4, '\\(\\lim\\limits_{x\\to%d^{%s}}\\dfrac{%d}{x%+d}=%s\\).' % (a4, sd, c4, -a4, claim), '\\(\\lim\\limits_{x\\to%d^{%s}}\\dfrac{%d}{x%+d}=%s\\).' % (a4, sd, c4, -a4, claim), claim == real,
            '\\(x%+d\\to0^{%s}\\) and the numerator is \\(%d\\): the limit is \\(%s\\).' % (-a4, sd, c4, real), '\\(x%+d\\to0^{%s}\\), tử bằng \\(%d\\): giới hạn là \\(%s\\).' % (-a4, sd, c4, real))
    (m, p_), (q, c), x0 = P['pw']; L_, R_ = m * x0 + p_, q * x0 + c
    t5 = tf(5, '\\(f(x)=%s\\) for \\(x\\lt%d\\), \\(f(x)=%s\\) for \\(x\\ge%d\\). \\(\\lim\\limits_{x\\to%d}f(x)\\) exists.' % (poly([m, p_], 'x'), x0, poly([q, c], 'x'), x0, x0), 'Cho \\(f(x)=%s\\) khi \\(x\\lt%d\\), \\(f(x)=%s\\) khi \\(x\\ge%d\\). Tồn tại \\(\\lim\\limits_{x\\to%d}f(x)\\).' % (poly([m, p_], 'x'), x0, poly([q, c], 'x'), x0, x0), L_ == R_,
            'Left limit \\(%d\\), right limit \\(%d\\).' % (L_, R_), 'Giới hạn trái \\(%d\\), giới hạn phải \\(%d\\).' % (L_, R_))
    a6 = P['cube']
    s6 = sh(6, 'Find \\(%s\\dfrac{x^3%+d}{x%+d}\\).' % (LX(a6), -a6 ** 3, -a6), 'Tính \\(%s\\dfrac{x^3%+d}{x%+d}\\).' % (LX(a6), -a6 ** 3, -a6), 3 * a6 * a6, '\\(x^2%+dx%+d\\to3\\cdot%d=%d\\).' % (a6, a6 * a6, a6 * a6, 3 * a6 * a6), '\\(x^2%+dx%+d\\to3\\cdot%d=%d\\).' % (a6, a6 * a6, a6 * a6, 3 * a6 * a6))
    V0, conc, rate = P['tank']
    s7 = sh(7, 'A tank has \\(%d\\) l of pure water. Salt water of \\(%d\\) g/l is added at \\(%d\\) l/min, so \\(C(t)=\\dfrac{%d\\cdot%d t}{%d+%dt}\\) (g/l). Find \\(\\lim\\limits_{t\\to+\\infty}C(t)\\).' % (V0, conc, rate, conc, rate, V0, rate),
            'Bể chứa \\(%d\\) l nước tinh khiết. Bơm vào nước muối \\(%d\\) g/l với tốc độ \\(%d\\) l/phút, nồng độ \\(C(t)=\\dfrac{%d\\cdot%d t}{%d+%dt}\\) (g/l). Tính \\(\\lim\\limits_{t\\to+\\infty}C(t)\\).' % (V0, conc, rate, conc, rate, V0, rate), conc,
            'Divide by \\(t\\): \\(\\dfrac{%d}{\\frac{%d}t+%d}\\to%d\\).' % (conc * rate, V0, rate, conc), 'Chia tử và mẫu cho \\(t\\): \\(\\dfrac{%d}{\\frac{%d}t+%d}\\to%d\\).' % (conc * rate, V0, rate, conc))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
PP = [dict(fac=(2, 5), conj=3, inf=([4, -1], [2, 3], '+\\infty'), side=(1, 3, '-', '+\\infty'), pw=((2, 1), (1, 3), 2), cube=2, tank=(100, 20, 5)),
      dict(fac=(-1, 3), conj=5, inf=([-6, 0, 1], [3, 2, -1], '-\\infty'), side=(-2, 5, '+', '+\\infty'), pw=((3, -2), (1, 2), 1), cube=-1, tank=(500, 40, 10)),
      dict(fac=(4, -2), conj=2, inf=([5, 2, 0], [2, 0, 7], '+\\infty'), side=(3, -2, '+', '+\\infty'), pw=((1, 4), (2, 1), 3), cube=3, tank=(300, 15, 6))]
practice = three(lvl, PP)
import sp_g11r as RR, sp_g11r2 as R2
# Hiệu chỉnh 13/11/2026: phần D cũ lặp lại các dạng của A–C → 8 dạng mới.
practice = RR.with_d(practice, R2.D16, seeds=(1161, 1162, 1163))
mistakes = [('<b>"\\(\\frac00=0\\)".</b> It is an indeterminate form: factorise or use the conjugate first.', '<b>"\\(\\frac00=0\\)".</b> Đây là dạng vô định: phải phân tích nhân tử hoặc nhân liên hợp trước.'),
            ('<b>Using \\(f(x_0)\\) as the limit.</b> The limit depends on values near \\(x_0\\), not at \\(x_0\\).', '<b>Lấy \\(f(x_0)\\) làm giới hạn.</b> Giới hạn phụ thuộc các giá trị gần \\(x_0\\), không phải tại \\(x_0\\).'),
            ('<b>Ignoring the side.</b> \\(\\dfrac1{x-2}\\) tends to \\(+\\infty\\) from the right but \\(-\\infty\\) from the left.', '<b>Bỏ qua phía.</b> \\(\\dfrac1{x-2}\\) dần tới \\(+\\infty\\) bên phải nhưng \\(-\\infty\\) bên trái.'),
            ('<b>Piecewise functions.</b> Use the left formula for \\(x\\to x_0^-\\) and the right formula for \\(x\\to x_0^+\\).', '<b>Hàm cho nhiều công thức.</b> Dùng công thức bên trái cho \\(x\\to x_0^-\\), công thức bên phải cho \\(x\\to x_0^+\\).')]
summary = [('Defined at \\(x_0\\) (polynomial, rational): substitute.', 'Hàm đa thức, phân thức xác định tại \\(x_0\\): thay trực tiếp.'),
           ('Form \\(\\frac00\\): factorise \\((x-x_0)\\) or multiply by the conjugate.', 'Dạng \\(\\frac00\\): phân tích ra \\((x-x_0)\\) hoặc nhân liên hợp.'),
           ('\\(\\lim\\limits_{x\\to x_0}f=L\\iff\\lim\\limits_{x\\to x_0^-}f=\\lim\\limits_{x\\to x_0^+}f=L\\).', '\\(\\lim\\limits_{x\\to x_0}f=L\\iff\\lim\\limits_{x\\to x_0^-}f=\\lim\\limits_{x\\to x_0^+}f=L\\).'),
           ('At \\(\\pm\\infty\\): divide by the highest power; \\(\\dfrac{L\\ne0}{\\to0^\\pm}\\to\\pm\\infty\\). Key words: limit, one-sided, indeterminate form.', 'Tại \\(\\pm\\infty\\): chia cho lũy thừa cao nhất; số khác 0 chia cho đại lượng dần tới \\(0^\\pm\\) thì dần tới \\(\\pm\\infty\\). Từ cần nhớ (chạm vào để xem tiếng Anh): <b class="mbl-term" tabindex="0" data-en="limit">giới hạn</b>, <b class="mbl-term" tabindex="0" data-en="one-sided limit">giới hạn một phía</b>, <b class="mbl-term" tabindex="0" data-en="indeterminate form">dạng vô định</b>.')]
checks = [('I can find a limit by substitution.', 'Em tính được giới hạn bằng cách thay trực tiếp.'), ('I can remove the form \\(\\frac00\\).', 'Em khử được dạng \\(\\frac00\\).'),
          ('I can use one-sided limits.', 'Em dùng được giới hạn một phía.'), ('I can find limits at infinity and infinite limits.', 'Em tìm được giới hạn tại vô cực và giới hạn vô cực.')]
LL('g11-limits-04', 'Limits of Functions', CV, ('Limits and Continuity', 'Giới hạn. Hàm số liên tục'), 'limits', 'function-limits', 170, 'Intermediate', 75, ('limits of sequences, factorising, conjugates', 'giới hạn của dãy số, phân tích nhân tử, nhân liên hợp'),
   'Limits of functions at a point and at infinity, the form 0/0, one-sided limits and infinite limits.', 'Bài 16 – Giới hạn hữu hạn tại một điểm, giới hạn một phía, giới hạn tại vô cực, giới hạn vô cực; khử dạng 0/0.',
   ['limit', 'one-sided limit', 'indeterminate form', 'infinity'], ['giới hạn hàm số', 'giới hạn một phía', 'dạng vô định', 'vô cực'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g11-limits-03'])
