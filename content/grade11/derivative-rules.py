# -*- coding: utf-8 -*-
"""g11-deriv-02 = Toán 11 KNTT, Bài 32: Các quy tắc tính đạo hàm. Mã ngân hàng câu hỏi: TOAN11-C9-B32."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g11k as S

P_ = S.poly
CV = 'Các quy tắc tính đạo hàm'
vocab = defs(CV, [
 ('prodrule', 'product rule', 'quy tắc đạo hàm của tích', '\\((uv)′=u′v+uv′\\).', '\\((uv)′=u′v+uv′\\).', 'Use the product rule for (x² + 1)(x − 3).', '\\((uv)′\\)'),
 ('quotrule', 'quotient rule', 'quy tắc đạo hàm của thương', '\\(\\left(\\dfrac uv\\right)′=\\dfrac{u′v-uv′}{v^2}\\) where \\(v\\ne0\\).', '\\(\\left(\\dfrac uv\\right)′=\\dfrac{u′v-uv′}{v^2}\\) với \\(v\\ne0\\).', 'The quotient rule gives the derivative of (2x + 1)/(x − 1).', ''),
 ('compfn', 'composite function', 'hàm số hợp', 'a function of the form \\(y=f(u(x))\\).', 'hàm số dạng \\(y=f(u(x))\\).', 'y = sin 3x is a composite function.', '\\(f(u(x))\\)'),
 ('chainrule', 'chain rule', 'đạo hàm của hàm số hợp', '\\(y′_x=y′_u\\cdot u′_x\\).', 'quy tắc \\(y′_x=y′_u\\cdot u′_x\\).', 'By the chain rule, (sin 3x)′ = 3 cos 3x.', '\\(y′_u\\cdot u′_x\\)')])
goals = [('use the derivatives of \\(x^n\\), \\(\\sqrt x\\), trigonometric, exponential and logarithmic functions;', 'sử dụng đạo hàm của \\(x^n\\), \\(\\sqrt x\\), các hàm lượng giác, hàm mũ, hàm lôgarit;'),
         ('apply the sum, product and quotient rules;', 'vận dụng quy tắc đạo hàm của tổng, [[tích|quy tắc đạo hàm của tích]], [[thương|quy tắc đạo hàm của thương]];'),
         ('differentiate composite functions with the chain rule;', 'tính đạo hàm của [[hàm số hợp]] bằng quy tắc [[đạo hàm của hàm số hợp]];'),
         ('solve tangent and rate-of-change problems.', 'giải bài toán tiếp tuyến và tốc độ thay đổi.')]
phrases = [('<b>Differentiate the inside function too.</b>', 'Nhớ nhân thêm đạo hàm của hàm bên trong.'), ('<b>The derivative of a product is not the product of the derivatives.</b>', 'Đạo hàm của tích không bằng tích các đạo hàm.'),
           ('<b>Write the function as a power before differentiating.</b>', 'Viết hàm số dưới dạng lũy thừa trước khi lấy đạo hàm.'), ('<b>The tangent has slope four at this point.</b>', 'Tiếp tuyến tại điểm này có hệ số góc bằng 4.'), ('<b>Check the domain first.</b>', 'Kiểm tra tập xác định trước.')]
review = T('From Bài 31: \\(f′(x_0)\\) as a limit, \\((x^2)′=2x\\), \\((x^3)′=3x^2\\), \\(\\left(\\frac1x\\right)′=-\\frac1{x^2}\\), tangent \\(y=f′(x_0)(x-x_0)+f(x_0)\\). From Chapter I and VI: \\(\\sin\\), \\(\\cos\\), \\(e^x\\), \\(\\ln x\\).',
           'Từ Bài 31: định nghĩa \\(f′(x_0)\\), \\((x^2)′=2x\\), \\((x^3)′=3x^2\\), \\(\\left(\\frac1x\\right)′=-\\frac1{x^2}\\), tiếp tuyến \\(y=f′(x_0)(x-x_0)+f(x_0)\\). Từ Chương I và VI: hàm \\(\\sin\\), \\(\\cos\\), \\(e^x\\), \\(\\ln x\\).')

theory = '<h3>32.1 %s</h3>' % TI('Derivatives of basic functions', 'Đạo hàm của một số hàm số thường gặp')
rows = [('\\((c)′=0\\), \\((x)′=1\\)', '—'), ('\\((x^n)′=nx^{n-1}\\) \\((n\\in\\mathbb N^*)\\)', '\\((u^n)′=nu^{n-1}u′\\)'), ('\\((\\sqrt x)′=\\dfrac1{2\\sqrt x}\\) \\((x>0)\\)', '\\((\\sqrt u)′=\\dfrac{u′}{2\\sqrt u}\\)'),
        ('\\((\\sin x)′=\\cos x\\)', '\\((\\sin u)′=u′\\cos u\\)'), ('\\((\\cos x)′=-\\sin x\\)', '\\((\\cos u)′=-u′\\sin u\\)'), ('\\((\\tan x)′=\\dfrac1{\\cos^2x}\\)', '\\((\\tan u)′=\\dfrac{u′}{\\cos^2u}\\)'), ('\\((\\cot x)′=-\\dfrac1{\\sin^2x}\\)', '\\((\\cot u)′=-\\dfrac{u′}{\\sin^2u}\\)'),
        ('\\((e^x)′=e^x\\), \\((a^x)′=a^x\\ln a\\)', '\\((e^u)′=u′e^u\\), \\((a^u)′=u′a^u\\ln a\\)'), ('\\((\\ln x)′=\\dfrac1x\\), \\((\\log_ax)′=\\dfrac1{x\\ln a}\\)', '\\((\\ln u)′=\\dfrac{u′}{u}\\), \\((\\log_au)′=\\dfrac{u′}{u\\ln a}\\)')]
theory += TBL([TI('Basic function', 'Hàm số sơ cấp'), TI('Composite \\(u=u(x)\\)', 'Hàm hợp \\(u=u(x)\\)')], [list(r) for r in rows])
theory += '<h3>32.2 %s</h3>' % TI('Rules', 'Các quy tắc')
theory += BOX('blue', ('Sum, product, quotient', 'Tổng, hiệu, tích, thương'), UL([T('\\((u\\pm v)′=u′\\pm v′\\); \\((ku)′=ku′\\).', '\\((u\\pm v)′=u′\\pm v′\\); \\((ku)′=ku′\\).'), T('\\((uv)′=u′v+uv′\\).', '[[Đạo hàm của tích|quy tắc đạo hàm của tích]]: \\((uv)′=u′v+uv′\\).'),
  T('\\(\\left(\\dfrac uv\\right)′=\\dfrac{u′v-uv′}{v^2}\\) \\((v\\ne0)\\); in particular \\(\\left(\\dfrac{ax+b}{cx+d}\\right)′=\\dfrac{ad-bc}{(cx+d)^2}\\).', '[[Đạo hàm của thương|quy tắc đạo hàm của thương]]: \\(\\left(\\dfrac uv\\right)′=\\dfrac{u′v-uv′}{v^2}\\) \\((v\\ne0)\\); đặc biệt \\(\\left(\\dfrac{ax+b}{cx+d}\\right)′=\\dfrac{ad-bc}{(cx+d)^2}\\).')]))
theory += BOX('mint', ('Chain rule', 'Đạo hàm của hàm số hợp'), T('If \\(u=g(x)\\) has a derivative at \\(x\\) and \\(y=f(u)\\) has a derivative at \\(u\\), then \\(y=f(g(x))\\) has \\[y′_x=y′_u\\cdot u′_x.\\] Example: \\(y=(x^2+1)^5\\Rightarrow y′=5(x^2+1)^4\\cdot2x\\).',
  'Nếu \\(u=g(x)\\) có đạo hàm tại \\(x\\) và \\(y=f(u)\\) có đạo hàm tại \\(u\\) thì [[hàm số hợp]] \\(y=f(g(x))\\) có đạo hàm \\[y′_x=y′_u\\cdot u′_x.\\] Ví dụ: \\(y=(x^2+1)^5\\Rightarrow y′=5(x^2+1)^4\\cdot2x\\).'))
theory += GRAPH({'view': [-3.5, 6.5, -1.6, 1.8], 'functions': [{'f': 'sin(x)', 'label': 'y = sin x'}, {'f': 'cos(x)', 'label': 'y = cos x', 'color': '#7c3aed'}], 'tangent': {'f': 0, 'at': 0, 'min': -1.4, 'max': 1.4}},
                cap=('Where sin x rises, cos x > 0; at its peaks (x = π/2) cos x = 0. The tangent at O has slope cos 0 = 1.', 'Ở đoạn y = sin x đi lên thì cos x > 0; tại đỉnh (x = π/2) thì cos x = 0. Tiếp tuyến tại O có hệ số góc cos 0 = 1.'),
                alt=('Graphs of sine and cosine, the tangent to sine at the origin', ''), height=280)
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('\\((uv)′\\ne u′v′\\) and \\(\\left(\\dfrac uv\\right)′\\ne\\dfrac{u′}{v′}\\). For \\(\\sin 3x\\), \\(e^{2x}\\), \\((2x+1)^5\\) do not forget the factor \\(u′\\).', '\\((uv)′\\ne u′v′\\) và \\(\\left(\\dfrac uv\\right)′\\ne\\dfrac{u′}{v′}\\). Với \\(\\sin 3x\\), \\(e^{2x}\\), \\((2x+1)^5\\) đừng quên nhân thêm \\(u′\\).'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Polynomials and roots', 'Đa thức và căn thức'), T('Differentiate (a) \\(y=2x^4-3x^2+5x-1\\); (b) \\(y=x\\sqrt x\\) \\((x>0)\\).', 'Tính đạo hàm: a) \\(y=2x^4-3x^2+5x-1\\); b) \\(y=x\\sqrt x\\) \\((x>0)\\).'),
  T('Term by term; (b) product rule.', 'Từng hạng tử; câu b dùng đạo hàm của tích.'), [T('(a) \\(y′=8x^3-6x+5\\).', 'a) \\(y′=8x^3-6x+5\\).'), T('(b) \\(y′=\\sqrt x+x\\cdot\\dfrac1{2\\sqrt x}=\\dfrac32\\sqrt x\\).', 'b) \\(y′=\\sqrt x+x\\cdot\\dfrac1{2\\sqrt x}=\\dfrac32\\sqrt x\\).')], T('\\(8x^3-6x+5\\); \\(\\dfrac32\\sqrt x\\).', '\\(8x^3-6x+5\\); \\(\\dfrac32\\sqrt x\\).'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Quotient', 'Đạo hàm của thương'), T('Differentiate \\(y=\\dfrac{2x+1}{x-1}\\).', 'Tính đạo hàm của \\(y=\\dfrac{2x+1}{x-1}\\).'),
  T('Quotient rule.', 'Quy tắc thương.'), [T('\\(y′=\\dfrac{2(x-1)-(2x+1)\\cdot1}{(x-1)^2}=\\dfrac{-3}{(x-1)^2}\\).', '\\(y′=\\dfrac{2(x-1)-(2x+1)\\cdot1}{(x-1)^2}=\\dfrac{-3}{(x-1)^2}\\).')], T('\\(y′=-\\dfrac3{(x-1)^2}\\), \\(x\\ne1\\).', '\\(y′=-\\dfrac3{(x-1)^2}\\), \\(x\\ne1\\).'))
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Chain rule', 'Hàm số hợp'), T('Differentiate (a) \\(y=\\sin(3x-\\frac\\pi4)\\); (b) \\(y=e^{x^2}\\); (c) \\(y=\\ln(x^2+1)\\); (d) \\(y=\\sqrt{x^2+5}\\).', 'Tính đạo hàm: a) \\(y=\\sin(3x-\\frac\\pi4)\\); b) \\(y=e^{x^2}\\); c) \\(y=\\ln(x^2+1)\\); d) \\(y=\\sqrt{x^2+5}\\).'),
  T('Identify \\(u\\) each time.', 'Xác định \\(u\\) trong từng câu.'), [T('(a) \\(3\\cos(3x-\\frac\\pi4)\\); (b) \\(2xe^{x^2}\\).', 'a) \\(3\\cos(3x-\\frac\\pi4)\\); b) \\(2xe^{x^2}\\).'), T('(c) \\(\\dfrac{2x}{x^2+1}\\); (d) \\(\\dfrac{x}{\\sqrt{x^2+5}}\\).', 'c) \\(\\dfrac{2x}{x^2+1}\\); d) \\(\\dfrac{x}{\\sqrt{x^2+5}}\\).')],
  T('See the steps.', 'Như các bước trên.'))
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Tangent of a cubic', 'Tiếp tuyến của hàm bậc ba'), T('Write the tangent to \\(y=x^3-3x^2+2\\) at the point with abscissa 1, and the tangents with slope 9.', 'Viết phương trình tiếp tuyến của đồ thị \\(y=x^3-3x^2+2\\) tại điểm có hoành độ 1, và các tiếp tuyến có hệ số góc bằng 9.'),
  T('\\(y′=3x^2-6x\\).', '\\(y′=3x^2-6x\\).'), [T('At \\(x=1\\): \\(y=0\\), \\(y′=-3\\): \\(y=-3(x-1)=-3x+3\\).', 'Tại \\(x=1\\): \\(y=0\\), \\(y′=-3\\): \\(y=-3(x-1)=-3x+3\\).'),
   T('\\(3x^2-6x=9\\iff x=-1\\) or \\(x=3\\). Points \\((-1;-2)\\), \\((3;2)\\): \\(y=9x+7\\) and \\(y=9x-25\\).', '\\(3x^2-6x=9\\iff x=-1\\) hoặc \\(x=3\\). Tiếp điểm \\((-1;-2)\\), \\((3;2)\\): \\(y=9x+7\\) và \\(y=9x-25\\).')],
  T('\\(y=-3x+3\\); \\(y=9x+7\\), \\(y=9x-25\\).', '\\(y=-3x+3\\); \\(y=9x+7\\), \\(y=9x-25\\).'))
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Cooling coffee', 'Cốc cà phê nguội dần'), T('The temperature of a cup of coffee is \\(T(t)=25+65e^{-0{,}05t}\\) (°C, \\(t\\) in minutes). Find the rate of change of the temperature at \\(t=0\\) and \\(t=20\\).', 'Nhiệt độ của một cốc cà phê sau \\(t\\) phút là \\(T(t)=25+65e^{-0{,}05t}\\) (°C). Tính tốc độ thay đổi nhiệt độ tại \\(t=0\\) và \\(t=20\\).'),
  T('\\((e^u)′=u′e^u\\).', '\\((e^u)′=u′e^u\\).'), [T('\\(T′(t)=-3{,}25e^{-0{,}05t}\\).', '\\(T′(t)=65\\cdot(-0{,}05)e^{-0{,}05t}=-3{,}25e^{-0{,}05t}\\).'), T('\\(T′(0)=-3{,}25\\); \\(T′(20)=-3{,}25e^{-1}\\approx-1{,}2\\) °C/min.', '\\(T′(0)=-3{,}25\\); \\(T′(20)=-3{,}25e^{-1}\\approx-1{,}2\\) °C/phút.')],
  T('The coffee cools about 3,25 °C/min at first, then only about 1,2 °C/min.', 'Lúc đầu cà phê nguội khoảng 3,25 °C mỗi phút, sau 20 phút chỉ còn khoảng 1,2 °C mỗi phút.'))
assert abs(3.25 * math.exp(-1) - 1.2) < 0.01
examples = EXFIG(examples, 4, GRAPH({'view': [-2, 4, -6, 6], 'functions': [{'f': 'x^3-3x^2+2', 'label': 'y = x³ − 3x² + 2'}], 'tangent': {'f': 0, 'at': [1, 3], 'min': -1.5, 'max': 3.8}},
  cap=('Tangent y = −3x + 3 at (1; 0) and tangent y = 9x − 25 at (3; 2).', 'Tiếp tuyến y = −3x + 3 tại (1; 0) và tiếp tuyến y = 9x − 25 tại (3; 2).'), alt=('Cubic with two tangent lines', ''), height=320))


def lvl(P):
    a, b, c = P['quot']; k = a * c - b
    q = lambda n: "\\(y′=\\dfrac{%d}{(x%+d)^2}\\)" % (n, c)
    o1 = M4(1, 'The derivative of \\(y=\\dfrac{%s}{x%+d}\\) is…' % (P_([a, b]), c), 'Đạo hàm của hàm số \\(y=\\dfrac{%s}{x%+d}\\) là…' % (P_([a, b]), c), q(k), [q(-k), q(a * c + b), "\\(y′=\\dfrac{%d}{x%+d}\\)" % (k, c)],
            '\\(\\dfrac{ad-bc}{(cx+d)^2}\\).', 'Tử số: \\(%d\\cdot(%d)-(%d)\\cdot1=%d\\).' % (a, c, b, k))
    kind, kk = P['chain']
    if kind == 'sin': cor, wr, f = "\\(y′=%d\\cos(%dx+1)\\)" % (kk, kk), ["\\(y′=\\cos(%dx+1)\\)" % kk, "\\(y′=-%d\\cos(%dx+1)\\)" % (kk, kk), "\\(y′=%d\\sin(%dx+1)\\)" % (kk, kk)], '\\sin(%dx+1)' % kk
    elif kind == 'exp': cor, wr, f = "\\(y′=%de^{%dx-1}\\)" % (kk, kk), ["\\(y′=e^{%dx-1}\\)" % kk, "\\(y′=(%dx-1)e^{%dx-2}\\)" % (kk, kk), "\\(y′=%de^{%dx}\\)" % (kk, kk)], 'e^{%dx-1}' % kk
    else: cor, wr, f = "\\(y′=\\dfrac{%d}{%dx+1}\\)" % (kk, kk), ["\\(y′=\\dfrac{1}{%dx+1}\\)" % kk, "\\(y′=\\dfrac{%d}{x}\\)" % kk, "\\(y′=%d\\ln(%dx+1)\\)" % (kk, kk)], '\\ln(%dx+1)' % kk
    o2 = M4(2, 'The derivative of \\(y=%s\\) is…' % f, 'Đạo hàm của hàm số \\(y=%s\\) là…' % f, cor, wr, 'Chain rule, \\(u′=%d\\).' % kk, 'Hàm hợp với \\(u′=%d\\).' % kk)
    bb, x0 = P['tan']; cs = [1, 0, bb, 0]; m = 3 * x0 * x0 + bb; y0 = x0 ** 3 + bb * x0; cc = y0 - m * x0
    L = lambda m_, c_: '\\(y=%s\\)' % P_([m_, c_])
    o3 = M4(3, 'The tangent to \\(y=%s\\) at the point with abscissa \\(%d\\) is…' % (P_(cs), x0), 'Tiếp tuyến của đồ thị \\(y=%s\\) tại điểm có hoành độ \\(%d\\) là…' % (P_(cs), x0), L(m, cc),
            [L(m, y0), L(m, -cc), L(y0, cc), L(-m, cc)], '\\(y=f′(x_0)(x-x_0)+f(x_0)\\).', '\\(f′(%d)=%d\\), \\(f(%d)=%d\\).' % (x0, m, x0, y0))
    (se, sv), v4 = P['t4']
    t4 = tf(4, se, sv, v4, 'Check with the rules.', 'Đối chiếu với quy tắc tính đạo hàm.')
    (te, tv), v5 = P['t5']
    t5 = tf(5, te, tv, v5, 'Chain rule.', 'Quy tắc đạo hàm hàm hợp.')
    pa, pb, x6 = P['prod']; v6 = 2 * x6 * (x6 + pb) + (x6 * x6 + pa)
    s6 = sh(6, '\\(f(x)=(x^2%+d)(x%+d)\\). Find \\(f′(%d)\\).' % (pa, pb, x6), 'Cho \\(f(x)=(x^2%+d)(x%+d)\\). Tính \\(f′(%d)\\).' % (pa, pb, x6), v6, '\\((uv)′=u′v+uv′\\).', '\\(f′(x)=2x(x%+d)+(x^2%+d)\\).' % (pb, pa))
    n7, x7 = P['pow']; v7 = 2 * n7 * (2 * x7 - 1) ** (n7 - 1)
    s7 = sh(7, '\\(f(x)=(2x-1)^{%d}\\). Find \\(f′(%d)\\).' % (n7, x7), 'Cho \\(f(x)=(2x-1)^{%d}\\). Tính \\(f′(%d)\\).' % (n7, x7), v7, '\\((u^n)′=nu^{n-1}u′\\).', '\\(f′(x)=%d\\cdot2(2x-1)^{%d}\\).' % (n7, n7 - 1))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]


PP = [dict(quot=(2, 1, -1), chain=('sin', 3), tan=(-3, 2),
           t4=(('\\((x^2\\cdot x^3)′=2x\\cdot3x^2\\).', '\\((x^2\\cdot x^3)′=2x\\cdot3x^2\\).'), False), t5=(('\\((\\cos 2x)′=-2\\sin 2x\\).', '\\((\\cos 2x)′=-2\\sin 2x\\).'), True), prod=(1, -2, 2), pow=(3, 1)),
      dict(quot=(1, 3, 2), chain=('exp', 2), tan=(1, -1),
           t4=(('\\(\\left(\\dfrac1{x^2}\\right)′=-\\dfrac2{x^3}\\) for \\(x\\ne0\\).', '\\(\\left(\\dfrac1{x^2}\\right)′=-\\dfrac2{x^3}\\) với \\(x\\ne0\\).'), True), t5=(('\\((e^{3x})′=e^{3x}\\).', '\\((e^{3x})′=e^{3x}\\).'), False), prod=(3, 1, -1), pow=(4, 1)),
      dict(quot=(3, -2, -3), chain=('ln', 4), tan=(-2, -2),
           t4=(('\\((\\tan x)′=1+\\tan^2x\\) where \\(\\cos x\\ne0\\).', '\\((\\tan x)′=1+\\tan^2x\\) với \\(\\cos x\\ne0\\).'), True), t5=(('\\((\\sqrt{x^2+1})′=\\dfrac1{2\\sqrt{x^2+1}}\\).', '\\((\\sqrt{x^2+1})′=\\dfrac1{2\\sqrt{x^2+1}}\\).'), False), prod=(-4, 3, 1), pow=(3, 2))]
practice = three(lvl, PP)
practice = with_self(practice, S.M32S11, start=8)
mistakes = [('<b>\\((uv)′=u′v′\\).</b> Wrong: use \\(u′v+uv′\\).', '<b>Viết \\((uv)′=u′v′\\).</b> Sai: phải là \\(u′v+uv′\\).'),
            ('<b>Forgetting \\(u′\\) in the chain rule.</b> \\((\\sin 3x)′=3\\cos 3x\\), not \\(\\cos 3x\\).', '<b>Quên nhân \\(u′\\) khi tính đạo hàm hàm hợp.</b> \\((\\sin 3x)′=3\\cos 3x\\), không phải \\(\\cos 3x\\).'),
            ('<b>Sign errors in the quotient rule.</b> The numerator is \\(u′v-uv′\\), in this order.', '<b>Sai dấu ở quy tắc thương.</b> Tử số là \\(u′v-uv′\\), đúng thứ tự.'),
            ('<b>Treating \\(e^x\\) like \\(x^n\\).</b> \\((e^x)′=e^x\\), not \\(xe^{x-1}\\).', '<b>Coi \\(e^x\\) như lũy thừa \\(x^n\\).</b> \\((e^x)′=e^x\\), không phải \\(xe^{x-1}\\).')]
summary = [('Table of basic derivatives and their composite forms.', 'Bảng đạo hàm của các hàm sơ cấp và dạng hàm hợp.'), ('\\((u\\pm v)′=u′\\pm v′\\), \\((uv)′=u′v+uv′\\), \\(\\left(\\frac uv\\right)′=\\frac{u′v-uv′}{v^2}\\).', '\\((u\\pm v)′=u′\\pm v′\\), \\((uv)′=u′v+uv′\\), \\(\\left(\\frac uv\\right)′=\\frac{u′v-uv′}{v^2}\\).'),
           ('Chain rule: \\(y′_x=y′_u\\cdot u′_x\\).', 'Hàm hợp: \\(y′_x=y′_u\\cdot u′_x\\).'), ('Key words: product rule, quotient rule, chain rule, composite function.', 'Từ cần nhớ: product rule, quotient rule, chain rule, composite function.')]
checks = [('I know the table of basic derivatives.', 'Em thuộc bảng đạo hàm cơ bản.'), ('I can use the product and quotient rules.', 'Em dùng được quy tắc tích, thương.'), ('I can differentiate composite functions.', 'Em tính được đạo hàm hàm hợp.'), ('I can solve tangent and rate problems.', 'Em giải được bài toán tiếp tuyến, tốc độ thay đổi.')]
LL('g11-deriv-02', 'Rules of Differentiation', CV, ('Derivatives', 'Đạo hàm'), 'derivatives', 'derivative-rules', 330, 'Intermediate', 70, ('definition of the derivative', 'định nghĩa đạo hàm'),
   'Derivatives of basic functions, sum, product and quotient rules, the chain rule, tangents and rates of change.', 'Bài 32 – Đạo hàm của các hàm số thường gặp; quy tắc tổng, tích, thương; đạo hàm của hàm số hợp; tiếp tuyến và tốc độ thay đổi.',
   ['product rule', 'quotient rule', 'chain rule'], ['đạo hàm của tích', 'đạo hàm của thương', 'hàm số hợp'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g11-deriv-01'])
