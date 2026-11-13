# -*- coding: utf-8 -*-
"""Hiệu chỉnh đợt 2 (13/11/2026) – Toán 11 KNTT, Bài 1–5, 8, 15, 16, 19.
Mỗi hàm sinh câu (r, lv, ctx) → dict như sp_g11r (opts[0] là đáp án đúng; fig = (html_en, html_vi) nếu có hình/bảng).
Phần D (8 câu trắc nghiệm) của mỗi bài gồm 8 DẠNG KHÁC NHAU và khác các dạng ở phần A–C của chính bài đó.
Mọi đáp án được tính trong hàm sinh (Fraction, bảng giá trị đặc biệt, hoặc thử số); kiểm tra độc lập ở scripts/audit10.py."""
import math, random
from fractions import Fraction as F
from sp_g11r import tx, ne, nv, nopt, nopts, key, with_d, assemble, stats_ctx, take, lab, TD
import fig2d as G
from fig2d import pitex

def M(s): return '\\(%s\\)' % s
def V(lv, opts): return opts[(lv - 1) % len(opts)]      # cách hỏi đổi theo mức → đề không trùng giữa các mức
def pit(fr): return pitex(fr, '\\dfrac')           # bội của π, dạng hiển thị trong đề
def frt(x):
    """Phân số → TeX (dfrac)."""
    x = F(x)
    if x.denominator == 1: return str(x.numerator)
    return ('-' if x < 0 else '') + '\\dfrac{%d}{%d}' % (abs(x.numerator), x.denominator)
def fo(good, cands):
    """Phương án dạng phân số/biểu thức: đáp án đúng + 3 phương án nhiễu đầu tiên khác nhau."""
    S = lambda c: c if isinstance(c, str) else frt(c)
    out = [S(good)]
    for c in cands:
        if S(c) not in out: out.append(S(c))
        if len(out) == 4: return out
    raise AssertionError('thiếu phương án')
def cx(c, v='n', first=False):
    """Hệ số·biến kèm dấu: +n, -n, +3n, -2n (first=True: không có dấu + đầu)."""
    s = {1: v, -1: '-' + v}.get(c, '%d%s' % (c, v))
    return s if first or s.startswith('-') else '+' + s
def opt_m(s): return s                      # phương án là biểu thức toán (mb_lib tự bọc \( \))
def distinct4(opts):
    assert len(set(opts)) == 4, opts
    return opts

# ---------------------------------------------------------------- giá trị lượng giác đặc biệt (độ → TeX, số)
SIN = {0: '0', 30: '\\dfrac12', 45: '\\dfrac{\\sqrt2}{2}', 60: '\\dfrac{\\sqrt3}{2}', 90: '1'}
def sp_val(fn, a):
    """sin/cos của góc a (độ, bội 15° đặc biệt 30/45/60/90) → (tex, số)."""
    a %= 360
    x = math.cos(math.radians(a)) if fn == 'cos' else math.sin(math.radians(a))
    ref = {0: 0, 30: 30, 45: 45, 60: 60, 90: 90}
    b = a % 180; b = min(b, 180 - b)
    if fn == 'cos': b = 90 - b
    t = SIN[b]
    if x < -1e-9: t = '-' + t
    return t, x
def tex_num(v):
    """Số đặc biệt → TeX (dò bảng)."""
    tab = {0: '0', 0.5: '\\dfrac12', math.sqrt(2) / 2: '\\dfrac{\\sqrt2}{2}', math.sqrt(3) / 2: '\\dfrac{\\sqrt3}{2}', 1: '1', math.sqrt(3): '\\sqrt3', math.sqrt(3) / 3: '\\dfrac{\\sqrt3}{3}'}
    for k, t in tab.items():
        if abs(abs(v) - k) < 1e-9: return ('-' + t) if v < -1e-9 else t
    raise AssertionError(v)

ROM = ['I', 'II', 'III', 'IV']
def quad(a):
    a %= 360; assert a % 90
    return int(a // 90)

# =====================================================================================================
# BÀI 1. Giá trị lượng giác của góc lượng giác
# =====================================================================================================
NONAX = [30, 45, 60, 120, 135, 150, 210, 225, 240, 300, 315, 330]

def b1_quadrant(r, lv, ctx):
    a0 = r.choice(NONAX); k = r.choice([-3, -2, -1, 1, 2, 3]); m = F(a0 + 360 * k, 180)
    q = quad(a0)
    opts = [tx('Quadrant %s' % ROM[i], 'Góc phần tư %s' % ROM[i]) for i in [q] + [j for j in range(4) if j != q]]
    return dict(en='The terminal side of the angle \\(\\alpha=%s\\) lies in which quadrant?' % pit(m), vi='Tia cuối của góc lượng giác \\(\\alpha=%s\\) nằm ở góc phần tư nào?' % pit(m),
                opts=opts, ee='\\(%s=%s%+d\\cdot2\\pi\\), and \\(%s\\) is in quadrant %s.' % (pit(m), pit(F(a0, 180)), k, pit(F(a0, 180)), ROM[q]),
                ev='\\(%s=%s%+d\\cdot2\\pi\\), mà \\(%s\\) thuộc góc phần tư %s.' % (pit(m), pit(F(a0, 180)), k, pit(F(a0, 180)), ROM[q]))

def b1_point_fig(r, lv, ctx):
    a = r.choice(NONAX); cx, _ = sp_val('cos', a); sy, _ = sp_val('sin', a)
    fn = G.circle_svg([(a, 'M')], rays=[a], proj=(a, cx.replace('\\dfrac', '\\frac'), sy.replace('\\dfrac', '\\frac')))
    k = r.choice([-1, 1])
    good = F(a, 180) + 2 * k
    bads = [F(-a, 180), F(180 - a, 180), F(180 + a, 180)]
    bads = [b + 2 * r.choice([-1, 0, 0, 1]) for b in bads]
    opts = [pit(good)] + [pit(b) for b in bads]
    st = V(lv, [('In the figure, \\(M\\) is a point on the trigonometric circle. Which number is a measure of the oriented angle \\((OA,OM)\\)?', 'Trong hình vẽ, \\(M\\) là một điểm trên đường tròn lượng giác. Số nào là một số đo của góc lượng giác \\((OA,OM)\\)?'),
               ('The point \\(M\\) in the figure lies on the trigonometric circle. Which value can be a measure of the angle \\((OA,OM)\\)?', 'Điểm \\(M\\) trong hình nằm trên đường tròn lượng giác. Giá trị nào có thể là số đo của góc lượng giác \\((OA,OM)\\)?'),
               ('Look at the point \\(M\\) on the trigonometric circle in the figure. Choose a measure of the oriented angle \\((OA,OM)\\).', 'Quan sát điểm \\(M\\) trên đường tròn lượng giác trong hình. Chọn một số đo của góc lượng giác \\((OA,OM)\\).')])
    return dict(en=st[0], vi=st[1],
                opts=distinct4(opts), fig=G.FIG(fn, 'Point M on the trigonometric circle', 'Điểm M trên đường tròn lượng giác', 300),
                ee='\\(M\\) has coordinates \\(\\left(%s;\\,%s\\right)\\), so \\((OA,OM)=%s+k2\\pi\\); with \\(k=%d\\) we get \\(%s\\).' % (cx, sy, pit(F(a, 180)), k, pit(good)),
                ev='\\(M\\) có tọa độ \\(\\left(%s;\\,%s\\right)\\) nên \\((OA,OM)=%s+k2\\pi\\); với \\(k=%d\\) được \\(%s\\).' % (cx, sy, pit(F(a, 180)), k, pit(good)))

def b1_sign(r, lv, ctx):
    q = r.choice([1, 2, 3])
    rng = {1: ('\\dfrac{\\pi}{2}\\lt\\alpha\\lt\\pi'), 2: ('\\pi\\lt\\alpha\\lt\\dfrac{3\\pi}{2}'), 3: ('\\dfrac{3\\pi}{2}\\lt\\alpha\\lt2\\pi')}[q]
    a = {1: 125, 2: 230, 3: 310}[q]; t = math.radians(a)
    cand = {'\\sin\\alpha': math.sin(t), '\\cos\\alpha': math.cos(t), '\\tan\\alpha': math.tan(t), '\\cot\\alpha': 1 / math.tan(t), '\\sin\\alpha+\\cos\\alpha': math.sin(t) + math.cos(t), '\\sin\\alpha\\cos\\alpha': math.sin(t) * math.cos(t)}
    pos = [k for k, v in cand.items() if v > 0 and k in ('\\sin\\alpha', '\\cos\\alpha', '\\tan\\alpha')]
    good = pos[0]
    neg = [k for k, v in cand.items() if v < 0]
    r.shuffle(neg); opts = [good] + neg[:3]
    # kiểm tra: dấu không phụ thuộc góc cụ thể trong góc phần tư (thử nhiều góc)
    for aa in range(90 * q + 1, 90 * q + 90):
        tt = math.radians(aa)
        val = {'\\sin\\alpha': math.sin(tt), '\\cos\\alpha': math.cos(tt), '\\tan\\alpha': math.tan(tt), '\\cot\\alpha': 1 / math.tan(tt), '\\sin\\alpha\\cos\\alpha': math.sin(tt) * math.cos(tt), '\\sin\\alpha+\\cos\\alpha': math.sin(tt) + math.cos(tt)}
        assert val[good] > 0 and all(val[o] < 0 for o in opts[1:])
    st = V(lv, [('Given \\(%s\\). Which value is positive?', 'Cho \\(%s\\). Giá trị nào dương?'), ('Let \\(%s\\). Which expression is positive?', 'Cho góc \\(\\alpha\\) thỏa mãn \\(%s\\). Biểu thức nào dương?'), ('Suppose \\(%s\\). Which of these is greater than 0?', 'Giả sử \\(%s\\). Giá trị nào lớn hơn 0?')])
    return dict(en=st[0] % rng, vi=st[1] % rng, opts=opts,
                ee='\\(\\alpha\\) is in quadrant %s, so only \\(%s\\gt0\\) among the options.' % (ROM[q], good), ev='\\(\\alpha\\) thuộc góc phần tư %s nên trong các phương án chỉ có \\(%s\\gt0\\).' % (ROM[q], good))

def b1_clock(r, lv, ctx):
    R = r.choice([6, 8, 9, 10, 12, 15]); m = r.choice([5, 10, 15, 20, 25, 40, 45, 50])
    good = F(R * m, 30); opts = ['%s\\ \\text{cm}' % pit(x) for x in (good, good / 2, good * 2)] + ['%d\\ \\text{cm}' % (6 * m * R)]
    return dict(en='The minute hand of a clock is \\(%d\\) cm long. In \\(%d\\) minutes, how far does its tip travel?' % (R, m), vi='Kim phút của một chiếc đồng hồ dài \\(%d\\) cm. Trong \\(%d\\) phút, đầu kim đi được quãng đường bao nhiêu?' % (R, m),
                opts=distinct4(opts), ee='In \\(%d\\) minutes the hand turns \\(\\dfrac{%d}{60}\\cdot2\\pi=%s\\) rad, so \\(\\ell=%d\\cdot%s=%s\\) cm.' % (m, m, pit(F(m, 30)), R, pit(F(m, 30)), pit(good)),
                ev='Trong \\(%d\\) phút kim quay \\(\\dfrac{%d}{60}\\cdot2\\pi=%s\\) rad nên \\(\\ell=%d\\cdot%s=%s\\) cm.' % (m, m, pit(F(m, 30)), R, pit(F(m, 30)), pit(good)))

REL = {'\\sin(\\pi-\\alpha)': ('s', 1), '\\sin(\\pi+\\alpha)': ('s', -1), '\\sin(-\\alpha)': ('s', -1), '\\cos\\left(\\dfrac{\\pi}{2}-\\alpha\\right)': ('s', 1), '\\cos\\left(\\dfrac{\\pi}{2}+\\alpha\\right)': ('s', -1),
       '\\cos(\\pi-\\alpha)': ('c', -1), '\\cos(\\pi+\\alpha)': ('c', -1), '\\cos(-\\alpha)': ('c', 1), '\\sin\\left(\\dfrac{\\pi}{2}-\\alpha\\right)': ('c', 1), '\\sin\\left(\\dfrac{\\pi}{2}+\\alpha\\right)': ('c', 1)}
def _relnum(t, a):
    import re
    s = t.replace('\\left', '').replace('\\right', '').replace('\\dfrac{\\pi}{2}', '(pi/2)').replace('\\pi', 'pi').replace('\\alpha', 'a').replace('\\sin', 'sin').replace('\\cos', 'cos')
    return eval(s, {'sin': math.sin, 'cos': math.cos, 'pi': math.pi, 'a': a})
def b1_simplify(r, lv, ctx):
    kind = r.choice(['s', 'c']); ks = [k for k, v in REL.items() if v[0] == kind]
    t1, t2 = r.sample(ks, 2); sg = r.choice([1, -1])
    c = REL[t1][1] + sg * REL[t2][1]
    expr = '%s%s%s' % (t1, '+' if sg > 0 else '-', t2)
    base = '\\sin\\alpha' if kind == 's' else '\\cos\\alpha'; other = '\\cos\\alpha' if kind == 's' else '\\sin\\alpha'
    def fm(k, b): return '0' if k == 0 else ('%s%s' % ({1: '', -1: '-', 2: '2', -2: '-2'}[k], b))
    good = fm(c, base); pool = [fm(k, base) for k in (2, -2, 0) if k != c] + [fm(2, other), fm(-2, other)]
    opts = [good] + pool[:3]
    for a in (0.3, 1.1, 2.0):
        val = _relnum(t1, a) + sg * _relnum(t2, a); assert abs(val - c * (math.sin(a) if kind == 's' else math.cos(a))) < 1e-9
    return dict(en='Simplify \\(A=%s\\).' % expr, vi='Rút gọn biểu thức \\(A=%s\\).' % expr, opts=distinct4(opts),
                ee='\\(%s=%s\\), \\(%s=%s\\), so \\(A=%s\\).' % (t1, fm(REL[t1][1], base), t2, fm(REL[t2][1], base), good),
                ev='\\(%s=%s\\), \\(%s=%s\\) nên \\(A=%s\\).' % (t1, fm(REL[t1][1], base), t2, fm(REL[t2][1], base), good))

def b1_sumprod(r, lv, ctx):
    s = r.choice([F(1, 2), F(1, 3), F(1, 5), F(7, 5), F(2, 3), F(-1, 2), F(-1, 3), F(6, 5)])
    good = (s * s - 1) / 2
    return dict(en='Given \\(\\sin\\alpha+\\cos\\alpha=%s\\). Find \\(\\sin\\alpha\\cos\\alpha\\).' % frt(s), vi='Cho \\(\\sin\\alpha+\\cos\\alpha=%s\\). Tính \\(\\sin\\alpha\\cos\\alpha\\).' % frt(s),
                opts=distinct4([frt(good), frt(-good), frt(s * s - 1), frt(s * s / 2)]),
                ee='Square both sides: \\(1+2\\sin\\alpha\\cos\\alpha=%s\\), so \\(\\sin\\alpha\\cos\\alpha=%s\\).' % (frt(s * s), frt(good)),
                ev='Bình phương hai vế: \\(1+2\\sin\\alpha\\cos\\alpha=%s\\) nên \\(\\sin\\alpha\\cos\\alpha=%s\\).' % (frt(s * s), frt(good)))

def b1_points(r, lv, ctx):
    base = r.choice([F(1, 6), F(1, 4), F(1, 3), F(1, 12)])
    step = r.choice([F(1), F(1, 2), F(1, 3), F(2, 3), F(1, 4)])     # bước kπ·step
    n = int(2 / step)
    st = {F(1): 'k\\pi', F(1, 2): '\\dfrac{k\\pi}{2}', F(1, 3): '\\dfrac{k\\pi}{3}', F(2, 3): '\\dfrac{k2\\pi}{3}', F(1, 4): '\\dfrac{k\\pi}{4}'}[step]
    pts = {((base + k * step) % 2) for k in range(-40, 40)}; assert len(pts) == n
    return dict(en='How many points on the trigonometric circle represent the angles \\(\\alpha=%s+%s\\) \\((k\\in\\mathbb Z)\\)?' % (pit(base), st), vi='Có bao nhiêu điểm trên đường tròn lượng giác biểu diễn các góc \\(\\alpha=%s+%s\\) \\((k\\in\\mathbb Z)\\)?' % (pit(base), st),
                opts=nopts(r, n, [n // 2, 2 * n, n + 1, 1, 2, 4]),
                ee='Consecutive points differ by \\(%s\\); a full turn \\(2\\pi\\) contains \\(%d\\) such steps, so there are \\(%d\\) points.' % (pit(step), n, n),
                ev='Hai điểm liên tiếp cách nhau một cung \\(%s\\); một vòng \\(2\\pi\\) chứa \\(%d\\) bước như vậy nên có \\(%d\\) điểm.' % (pit(step), n, n))

def b1_sym_fig(r, lv, ctx):
    a = r.choice([20, 25, 35, 40, 50, 55, 65, 70]) + 90 * r.choice([0, 1, 2, 3])
    typ = r.choice(['x', 'y', 'o'])
    b = {'x': -a, 'y': 180 - a, 'o': 180 + a}[typ] % 360
    fn = G.circle_svg([(a, 'M'), (b, 'N')], dashed=[(a, b)] if typ != 'o' else [], showA=False)
    nm = {'x': ('the axis \\(Ox\\)', 'trục \\(Ox\\)'), 'y': ('the axis \\(Oy\\)', 'trục \\(Oy\\)'), 'o': ('the origin \\(O\\)', 'gốc tọa độ \\(O\\)')}[typ]
    good = {'x': '\\cos\\beta=\\cos\\alpha', 'y': '\\sin\\beta=\\sin\\alpha', 'o': '\\tan\\beta=\\tan\\alpha'}[typ]
    al = ['\\cos\\beta=\\cos\\alpha', '\\sin\\beta=\\sin\\alpha', '\\tan\\beta=\\tan\\alpha', '\\sin\\beta=\\cos\\alpha']
    opts = [good] + [o for o in al if o != good]
    A, B = math.radians(a), math.radians(b)
    val = {'\\cos\\beta=\\cos\\alpha': abs(math.cos(B) - math.cos(A)), '\\sin\\beta=\\sin\\alpha': abs(math.sin(B) - math.sin(A)), '\\tan\\beta=\\tan\\alpha': abs(math.tan(B) - math.tan(A)), '\\sin\\beta=\\cos\\alpha': abs(math.sin(B) - math.cos(A))}
    assert val[good] < 1e-9 and all(val[o] > 1e-3 for o in opts[1:])
    return dict(en='In the figure, the points \\(M\\) and \\(N\\) on the trigonometric circle represent the angles \\(\\alpha\\) and \\(\\beta\\); they are symmetric with respect to %s. Which equality is true?' % nm[0],
                vi='Trong hình vẽ, hai điểm \\(M\\), \\(N\\) trên đường tròn lượng giác biểu diễn các góc \\(\\alpha\\), \\(\\beta\\) và đối xứng nhau qua %s. Đẳng thức nào đúng?' % nm[1],
                opts=opts, fig=G.FIG(fn, 'Two symmetric points on the trigonometric circle', 'Hai điểm đối xứng trên đường tròn lượng giác', 300),
                ee={'x': '\\(\\beta=-\\alpha+k2\\pi\\), so the cosines are equal.', 'y': '\\(\\beta=\\pi-\\alpha+k2\\pi\\), so the sines are equal.', 'o': '\\(\\beta=\\pi+\\alpha+k2\\pi\\), so the tangents are equal.'}[typ],
                ev={'x': '\\(\\beta=-\\alpha+k2\\pi\\) nên hai giá trị cos bằng nhau.', 'y': '\\(\\beta=\\pi-\\alpha+k2\\pi\\) nên hai giá trị sin bằng nhau.', 'o': '\\(\\beta=\\pi+\\alpha+k2\\pi\\) nên hai giá trị tan bằng nhau.'}[typ])

D1 = [b1_quadrant, b1_point_fig, b1_sign, b1_clock, b1_simplify, b1_sumprod, b1_points, b1_sym_fig]

# =====================================================================================================
# BÀI 2. Công thức lượng giác
# =====================================================================================================
TRI = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25)]
def b2_add(r, lv, ctx):
    (p1, q1, c1), (p2, q2, c2) = TRI[0], r.choice(TRI[1:])
    if r.random() < .5: (p1, q1, c1), (p2, q2, c2) = (p2, q2, c2), (p1, q1, c1)
    if r.random() < .5: p1, q1 = q1, p1
    if r.random() < .5: p2, q2 = q2, p2
    sa, ca, sb, cb = F(p1, c1), F(q1, c1), F(p2, c2), F(q2, c2)
    V = {'\\sin(a+b)': sa * cb + ca * sb, '\\sin(a-b)': sa * cb - ca * sb, '\\cos(a+b)': ca * cb - sa * sb, '\\cos(a-b)': ca * cb + sa * sb}
    if len(set(V.values())) != 4: raise AssertionError
    ask = r.choice(list(V)); good = V[ask]
    A, B = math.atan2(p1, q1), math.atan2(p2, q2)
    num = {'\\sin(a+b)': math.sin(A + B), '\\sin(a-b)': math.sin(A - B), '\\cos(a+b)': math.cos(A + B), '\\cos(a-b)': math.cos(A - B)}
    assert abs(num[ask] - float(good)) < 1e-12
    rest = [V[k] for k in V if k != ask]
    return dict(en='Given \\(\\sin a=%s\\), \\(\\cos b=%s\\) with \\(0\\lt a,b\\lt\\dfrac{\\pi}{2}\\). Find \\(%s\\).' % (frt(sa), frt(cb), ask),
                vi='Cho \\(\\sin a=%s\\), \\(\\cos b=%s\\) với \\(0\\lt a,b\\lt\\dfrac{\\pi}{2}\\). Tính \\(%s\\).' % (frt(sa), frt(cb), ask),
                opts=distinct4([frt(good)] + [frt(x) for x in rest]),
                ee='\\(\\cos a=%s\\), \\(\\sin b=%s\\) (both positive). Then \\(%s=%s\\).' % (frt(ca), frt(sb), ask, frt(good)),
                ev='\\(\\cos a=%s\\), \\(\\sin b=%s\\) (đều dương). Khi đó \\(%s=%s\\).' % (frt(ca), frt(sb), ask, frt(good)))

def b2_tan(r, lv, ctx):
    p = F(r.choice([1, 2, 3, -1, -2, 1, 1]), r.choice([1, 2, 3])); q = F(r.choice([1, 2, 3, 4, -1, -3]), r.choice([1, 2, 3, 5]))
    sg = r.choice([1, -1])
    if 1 - sg * p * q == 0 or p == q: raise AssertionError
    good = (p + sg * q) / (1 - sg * p * q)
    bad = [(p + sg * q) / (1 + sg * p * q) if 1 + sg * p * q else p + q + 7, p + sg * q, (p - sg * q) / (1 + sg * p * q) if 1 + sg * p * q else 9]
    assert abs(math.tan(math.atan(p) + sg * math.atan(q)) - float(good)) < 1e-9
    op = '+' if sg > 0 else '-'
    opts = [frt(good)] + [frt(x) for x in bad]
    return dict(en='Given \\(\\tan a=%s\\) and \\(\\tan b=%s\\). Find \\(\\tan(a%sb)\\).' % (frt(p), frt(q), op), vi='Cho \\(\\tan a=%s\\) và \\(\\tan b=%s\\). Tính \\(\\tan(a%sb)\\).' % (frt(p), frt(q), op),
                opts=distinct4(opts), ee='\\(\\tan(a%sb)=\\dfrac{\\tan a%s\\tan b}{1%s\\tan a\\tan b}=%s\\).' % (op, op, '-' if sg > 0 else '+', frt(good)),
                ev='\\(\\tan(a%sb)=\\dfrac{\\tan a%s\\tan b}{1%s\\tan a\\tan b}=%s\\).' % (op, op, '-' if sg > 0 else '+', frt(good)))

def _kx(k): return 'x' if k == 1 else '%dx' % k
def b2_prod(r, lv, ctx):
    m, n = sorted(r.sample(range(1, 7), 2), reverse=True)
    S, D = _kx(m + n), _kx(m - n)
    forms = {'sc': ('2\\sin %s\\cos %s' % (_kx(m), _kx(n)), '\\sin %s+\\sin %s' % (S, D)),
             'cc': ('2\\cos %s\\cos %s' % (_kx(m), _kx(n)), '\\cos %s+\\cos %s' % (S, D)),
             'ss': ('2\\sin %s\\sin %s' % (_kx(m), _kx(n)), '\\cos %s-\\cos %s' % (D, S))}
    k = r.choice(list(forms)); lhs, good = forms[k]
    opts = [good] + [forms[j][1] for j in forms if j != k] + ['\\sin %s-\\sin %s' % (S, D)]
    f = {'sc': lambda x: 2 * math.sin(m * x) * math.cos(n * x), 'cc': lambda x: 2 * math.cos(m * x) * math.cos(n * x), 'ss': lambda x: 2 * math.sin(m * x) * math.sin(n * x)}[k]
    g = {'sc': lambda x: math.sin((m + n) * x) + math.sin((m - n) * x), 'cc': lambda x: math.cos((m + n) * x) + math.cos((m - n) * x), 'ss': lambda x: math.cos((m - n) * x) - math.cos((m + n) * x)}[k]
    assert all(abs(f(x) - g(x)) < 1e-9 for x in (0.3, 0.7, 1.9))
    return dict(en='Write \\(%s\\) as a sum.' % lhs, vi='Biến đổi \\(%s\\) thành tổng.' % lhs, opts=distinct4(opts),
                ee='Product-to-sum formula: \\(%s=%s\\).' % (lhs, good), ev='Công thức biến đổi tích thành tổng: \\(%s=%s\\).' % (lhs, good))

def b2_sum(r, lv, ctx):
    p, q = sorted(r.sample(range(1, 9), 2), reverse=True)
    if (p + q) % 2: raise AssertionError
    u, v = (p + q) // 2, (p - q) // 2; A, B = _kx(u), _kx(v)
    sn, cs = math.sin, math.cos
    cand = {'2\\cos %s\\cos %s' % (A, B): lambda x: 2 * cs(u * x) * cs(v * x), '-2\\sin %s\\sin %s' % (A, B): lambda x: -2 * sn(u * x) * sn(v * x),
            '2\\sin %s\\cos %s' % (A, B): lambda x: 2 * sn(u * x) * cs(v * x), '2\\cos %s\\sin %s' % (A, B): lambda x: 2 * cs(u * x) * sn(v * x),
            '2\\sin %s\\sin %s' % (A, B): lambda x: 2 * sn(u * x) * sn(v * x)}
    forms = [('\\cos %s+\\cos %s' % (_kx(p), _kx(q)), lambda x: cs(p * x) + cs(q * x)), ('\\cos %s-\\cos %s' % (_kx(p), _kx(q)), lambda x: cs(p * x) - cs(q * x)),
             ('\\sin %s+\\sin %s' % (_kx(p), _kx(q)), lambda x: sn(p * x) + sn(q * x)), ('\\sin %s-\\sin %s' % (_kx(p), _kx(q)), lambda x: sn(p * x) - sn(q * x))]
    lhs, f = r.choice(forms); X = (0.3, 0.8, 2.1)
    good = [t for t, g in cand.items() if all(abs(f(x) - g(x)) < 1e-9 for x in X)]; assert len(good) == 1; good = good[0]
    bad = [t for t, g in cand.items() if any(abs(f(x) - g(x)) > 1e-6 for x in X)]; r.shuffle(bad)
    return dict(en='Write \\(%s\\) as a product.' % lhs, vi='Biến đổi \\(%s\\) thành tích.' % lhs, opts=distinct4([good] + bad[:3]),
                ee='Sum-to-product formula: \\(%s=%s\\).' % (lhs, good), ev='Công thức biến đổi tổng thành tích: \\(%s=%s\\).' % (lhs, good))

TV = {('tan', 15): '2-\\sqrt3', ('tan', 75): '2+\\sqrt3', ('tan', 105): '-2-\\sqrt3', ('tan', 165): '\\sqrt3-2',
      ('sin', 15): '\\dfrac{\\sqrt6-\\sqrt2}{4}', ('sin', 75): '\\dfrac{\\sqrt6+\\sqrt2}{4}', ('sin', 105): '\\dfrac{\\sqrt6+\\sqrt2}{4}', ('sin', 165): '\\dfrac{\\sqrt6-\\sqrt2}{4}',
      ('cos', 15): '\\dfrac{\\sqrt6+\\sqrt2}{4}', ('cos', 75): '\\dfrac{\\sqrt6-\\sqrt2}{4}', ('cos', 105): '-\\dfrac{\\sqrt6-\\sqrt2}{4}', ('cos', 165): '-\\dfrac{\\sqrt6+\\sqrt2}{4}'}
POOL = {'2-\\sqrt3': 2 - 3 ** .5, '2+\\sqrt3': 2 + 3 ** .5, '-2-\\sqrt3': -2 - 3 ** .5, '\\sqrt3-2': 3 ** .5 - 2, '\\dfrac{\\sqrt6-\\sqrt2}{4}': (6 ** .5 - 2 ** .5) / 4, '\\dfrac{\\sqrt6+\\sqrt2}{4}': (6 ** .5 + 2 ** .5) / 4,
        '-\\dfrac{\\sqrt6-\\sqrt2}{4}': -(6 ** .5 - 2 ** .5) / 4, '-\\dfrac{\\sqrt6+\\sqrt2}{4}': -(6 ** .5 + 2 ** .5) / 4}
def b2_exact(r, lv, ctx):
    fn = r.choice(['sin', 'cos', 'tan']); a = r.choice([15, 75, 105, 165]); good = TV[(fn, a)]
    v = {'sin': math.sin, 'cos': math.cos, 'tan': math.tan}[fn](math.radians(a)); assert abs(POOL[good] - v) < 1e-12
    same_kind = [t for t in POOL if ('sqrt6' in t) == ('sqrt6' in good) and abs(POOL[t] - v) > 1e-9]
    r.shuffle(same_kind); opts = [good] + same_kind[:3]
    dec = {15: '45^\\circ-30^\\circ', 75: '45^\\circ+30^\\circ', 105: '60^\\circ+45^\\circ', 165: '120^\\circ+45^\\circ'}[a]
    return dict(en='Find the exact value of \\(\\%s %d^\\circ\\).' % (fn, a), vi='Tính giá trị đúng của \\(\\%s %d^\\circ\\).' % (fn, a), opts=distinct4(opts),
                ee='Write \\(%d^\\circ=%s\\) and use the addition formula: \\(\\%s %d^\\circ=%s\\).' % (a, dec, fn, a, good), ev='Viết \\(%d^\\circ=%s\\) rồi dùng công thức cộng: \\(\\%s %d^\\circ=%s\\).' % (a, dec, fn, a, good))

SIMP = [('\\dfrac{\\sin2\\alpha}{1+\\cos2\\alpha}', '\\tan\\alpha', lambda a: math.sin(2 * a) / (1 + math.cos(2 * a))),
        ('\\dfrac{1-\\cos2\\alpha}{\\sin2\\alpha}', '\\tan\\alpha', lambda a: (1 - math.cos(2 * a)) / math.sin(2 * a)),
        ('\\dfrac{\\sin2\\alpha}{1-\\cos2\\alpha}', '\\cot\\alpha', lambda a: math.sin(2 * a) / (1 - math.cos(2 * a))),
        ('\\dfrac{1+\\cos2\\alpha}{\\sin2\\alpha}', '\\cot\\alpha', lambda a: (1 + math.cos(2 * a)) / math.sin(2 * a)),
        ('\\dfrac{1-\\cos2\\alpha}{1+\\cos2\\alpha}', '\\tan^2\\alpha', lambda a: (1 - math.cos(2 * a)) / (1 + math.cos(2 * a))),
        ('\\dfrac{\\sin2\\alpha}{2\\cos\\alpha}', '\\sin\\alpha', lambda a: math.sin(2 * a) / (2 * math.cos(a))),
        ('\\dfrac{\\sin2\\alpha}{2\\sin\\alpha}', '\\cos\\alpha', lambda a: math.sin(2 * a) / (2 * math.sin(a))),
        ('\\dfrac{1-\\cos2\\alpha}{2\\sin\\alpha}', '\\sin\\alpha', lambda a: (1 - math.cos(2 * a)) / (2 * math.sin(a)))]
RES = {'\\tan\\alpha': lambda a: math.tan(a), '\\cot\\alpha': lambda a: 1 / math.tan(a), '\\tan^2\\alpha': lambda a: math.tan(a) ** 2, '\\sin\\alpha': math.sin, '\\cos\\alpha': math.cos, '2\\tan\\alpha': lambda a: 2 * math.tan(a)}
def b2_simplify(r, lv, ctx):
    e, good, f = r.choice(SIMP)
    assert all(abs(f(a) - RES[good](a)) < 1e-9 for a in (0.3, 0.9, 1.3))
    bad = [k for k in RES if k != good and any(abs(f(a) - RES[k](a)) > 1e-6 for a in (0.3, 0.9, 1.3))]; r.shuffle(bad)
    return dict(en='Simplify \\(%s\\) (where it is defined).' % e, vi='Rút gọn biểu thức \\(%s\\) (khi biểu thức có nghĩa).' % e, opts=distinct4([good] + bad[:3]),
                ee='Use \\(\\sin2\\alpha=2\\sin\\alpha\\cos\\alpha\\), \\(1+\\cos2\\alpha=2\\cos^2\\alpha\\), \\(1-\\cos2\\alpha=2\\sin^2\\alpha\\); the result is \\(%s\\).' % good,
                ev='Dùng \\(\\sin2\\alpha=2\\sin\\alpha\\cos\\alpha\\), \\(1+\\cos2\\alpha=2\\cos^2\\alpha\\), \\(1-\\cos2\\alpha=2\\sin^2\\alpha\\); kết quả là \\(%s\\).' % good)

AMP = [('\\sin x+\\sqrt3\\cos x', 2, F(1, 3)), ('\\sqrt3\\sin x+\\cos x', 2, F(1, 6)), ('\\sin x+\\cos x', '\\sqrt2', F(1, 4)), ('\\sin x-\\cos x', '\\sqrt2', F(-1, 4)),
       ('\\sin x-\\sqrt3\\cos x', 2, F(-1, 3)), ('\\sqrt3\\sin x-\\cos x', 2, F(-1, 6))]
def b2_amp(r, lv, ctx):
    e, R, phi = r.choice(AMP)
    Rn = 2 if R == 2 else 2 ** .5
    a = 3 ** .5 if e.startswith('\\sqrt3') else 1
    bb = 3 ** .5 if '+\\sqrt3\\cos' in e else -(3 ** .5) if '-\\sqrt3\\cos' in e else (1 if '+\\cos' in e else -1)
    assert all(abs(a * math.sin(x) + bb * math.cos(x) - Rn * math.sin(x + float(phi) * math.pi)) < 1e-9 for x in (0.2, 1.0, 2.5))
    cand = [F(1, 3), F(1, 6), F(1, 4), F(-1, 4), F(-1, 3), F(-1, 6)]
    bad = [c for c in cand if c != phi]; r.shuffle(bad)
    return dict(en='Write \\(%s=%s\\sin(x+\\varphi)\\) with \\(-\\pi\\lt\\varphi\\lt\\pi\\). Then \\(\\varphi=\\)…' % (e, R), vi='Viết \\(%s=%s\\sin(x+\\varphi)\\) với \\(-\\pi\\lt\\varphi\\lt\\pi\\). Khi đó \\(\\varphi=\\)…' % (e, R),
                opts=distinct4([pit(phi)] + [pit(c) for c in bad[:3]]),
                ee='\\(%s=%s\\left(\\cos\\varphi\\sin x+\\sin\\varphi\\cos x\\right)\\) with \\(\\cos\\varphi=%s\\), \\(\\sin\\varphi=%s\\), so \\(\\varphi=%s\\).' % (e, R, tex_num(math.cos(float(phi) * math.pi)), tex_num(math.sin(float(phi) * math.pi)), pit(phi)),
                ev='\\(%s=%s\\left(\\cos\\varphi\\sin x+\\sin\\varphi\\cos x\\right)\\) với \\(\\cos\\varphi=%s\\), \\(\\sin\\varphi=%s\\) nên \\(\\varphi=%s\\).' % (e, R, tex_num(math.cos(float(phi) * math.pi)), tex_num(math.sin(float(phi) * math.pi)), pit(phi)))

def statue_svg(a, b, c):
    """O, H trên mặt đất; A, B trên đường thẳng đứng qua H (HA = b, HB = c); góc vuông tại H."""
    s = 4.2 / max(a, c)
    O, H, A, B = (0, 0), (a * s, 0), (a * s, b * s), (a * s, c * s)
    cv = G.Canvas()
    cv.poly([(-0.4, 0), (a * s + 0.8, 0)], 'ink, line width=0.8pt')
    cv.poly([H, B], 'ink, line width=1.1pt')
    cv.poly([O, A], 'ink, line width=0.8pt'); cv.poly([O, B], 'ink, line width=0.8pt')
    q = 0.22
    cv.poly([(H[0] - q, 0), (H[0] - q, q), (H[0], q)], 'ink, line width=0.6pt')
    for P in (O, H, A, B): cv.dot(*P)
    cv.label(*O, '$O$', 0.3, 0.36, [(-0.1, -0.3), (-0.3, 0.05)])
    cv.label(*H, '$H$', 0.3, 0.36, [(0.25, -0.28), (0, -0.3)])
    cv.label(*A, '$A$', 0.3, 0.36, [(0.28, 0), (0.28, -0.2), (0.28, 0.2)])
    cv.label(*B, '$B$', 0.3, 0.36, [(0.28, 0), (0.28, 0.2), (0, 0.3)])
    return cv.svg()
def b2_statue(r, lv, ctx):
    for _ in range(200):
        a = r.choice([4, 5, 6, 8, 9, 10, 12]); b = r.choice([2, 3, 4, 5, 6]); c = b + r.choice([1, 2, 3, 4, 6])
        good = F(a * (c - b), a * a + b * c)
        bads = [F(c - b, a), F(a * (c - b), a * a - b * c) if a * a != b * c else F(c + b, a), F(c, a) - F(b, a) * F(c, a)]
        if len({good, *bads}) == 4 and good.denominator <= 40: break
    else: raise AssertionError
    tA, tB = math.atan2(b, a), math.atan2(c, a); assert abs(math.tan(tB - tA) - float(good)) < 1e-12
    fn = statue_svg(a, b, c)
    return dict(en='A statue \\(AB\\) stands on a pedestal \\(HA\\) (see the figure). From a point \\(O\\) on the ground, \\(OH=%d\\) m, \\(HA=%d\\) m, \\(HB=%d\\) m. Find \\(\\tan\\widehat{AOB}\\).' % (a, b, c),
                vi='Một bức tượng \\(AB\\) đặt trên bệ \\(HA\\) (xem hình). Từ điểm \\(O\\) trên mặt đất, \\(OH=%d\\) m, \\(HA=%d\\) m, \\(HB=%d\\) m. Tính \\(\\tan\\widehat{AOB}\\).' % (a, b, c),
                opts=distinct4([frt(good)] + [frt(x) for x in bads]), fig=G.FIG(fn, 'Statue on a pedestal', 'Tượng trên bệ', 300),
                ee='\\(\\tan\\widehat{HOB}=\\dfrac{%d}{%d}\\), \\(\\tan\\widehat{HOA}=\\dfrac{%d}{%d}\\); \\(\\tan\\widehat{AOB}=\\tan(\\widehat{HOB}-\\widehat{HOA})=%s\\).' % (c, a, b, a, frt(good)),
                ev='\\(\\tan\\widehat{HOB}=\\dfrac{%d}{%d}\\), \\(\\tan\\widehat{HOA}=\\dfrac{%d}{%d}\\); \\(\\tan\\widehat{AOB}=\\tan(\\widehat{HOB}-\\widehat{HOA})=%s\\).' % (c, a, b, a, frt(good)))

D2 = [b2_add, b2_tan, b2_prod, b2_sum, b2_exact, b2_simplify, b2_amp, b2_statue]

# =====================================================================================================
# BÀI 3. Hàm số lượng giác
# =====================================================================================================
TRIG = {'\\sin x': math.sin, '\\cos x': math.cos, '-\\sin x': lambda x: -math.sin(x), '-\\cos x': lambda x: -math.cos(x)}
def ivl(a, b): return '\\left(%s;\\,%s\\right)' % (pit(a), pit(b))
def tgr(fs, lo, hi, step, ymin, ymax, yt, **kw):
    return G.graph_svg(fs, (float(lo) * math.pi, float(hi) * math.pi), (ymin, ymax), G.pi_ticks(lo, hi, step), yt, **kw)
YT1 = [(1, '1'), (-1, '-1')]

def b3_odd(r, lv, ctx):
    X = [0.3, 0.7, 1.2, 2.3]
    pool = {'x\\cos x': lambda x: x * math.cos(x), '\\tan x+\\sin x': lambda x: math.tan(x) + math.sin(x), '\\sin 3x': lambda x: math.sin(3 * x), 'x^3+\\sin x': lambda x: x ** 3 + math.sin(x),
            '\\sin x-x': lambda x: math.sin(x) - x, 'x\\sin x': lambda x: x * math.sin(x), '\\cos x+x^2': lambda x: math.cos(x) + x * x, '|\\sin x|': lambda x: abs(math.sin(x)),
            '\\sin^2x': lambda x: math.sin(x) ** 2, '\\cos 3x': lambda x: math.cos(3 * x), 'x\\tan x': lambda x: x * math.tan(x), '\\sin x+\\cos x': lambda x: math.sin(x) + math.cos(x),
            '\\sin x+1': lambda x: math.sin(x) + 1, '\\cos x-\\sin x': lambda x: math.cos(x) - math.sin(x), 'x+\\cos x': lambda x: x + math.cos(x)}
    par = {}
    for k, f in pool.items():
        if all(abs(f(-x) + f(x)) < 1e-9 for x in X): par[k] = 'odd'
        elif all(abs(f(-x) - f(x)) < 1e-9 for x in X): par[k] = 'even'
        else: par[k] = 'none'
    want = r.choice(['odd', 'even'])
    good = r.choice([k for k in pool if par[k] == want]); bad = [k for k in pool if par[k] != want]; r.shuffle(bad)
    opts = ['y=' + good] + ['y=' + b for b in bad[:3]]
    w = ('odd', 'lẻ') if want == 'odd' else ('even', 'chẵn')
    st = V(lv, [('Which function is %s?', 'Hàm số nào là hàm số %s?'), ('Among the following functions, which one is %s?', 'Trong các hàm số sau, hàm số nào %s?'), ('Choose the %s function.', 'Chọn hàm số %s.')])
    return dict(en=st[0] % w[0], vi=st[1] % w[1], opts=opts,
                ee='For \\(f(x)=%s\\): \\(f(-x)=%sf(x)\\) for every \\(x\\) in the domain (symmetric about 0).' % (good, '-' if want == 'odd' else ''),
                ev='Với \\(f(x)=%s\\): \\(f(-x)=%sf(x)\\) với mọi \\(x\\) thuộc tập xác định (đối xứng qua 0).' % (good, '-' if want == 'odd' else ''))

def b3_inc_fig(r, lv, ctx):
    nm = r.choice(list(TRIG)); f = TRIG[nm]
    I = [(F(k, 2), F(k, 2) + 1) for k in range(-2, 3)]
    def inc(a, b):
        xs = [float(a) * math.pi + (float(b - a) * math.pi) * i / 40 for i in range(41)]
        return all(f(x2) > f(x1) for x1, x2 in zip(xs, xs[1:]))
    good = [p for p in I if inc(*p)]; bad = [p for p in I if not inc(*p)]
    g = r.choice(good); r.shuffle(bad)
    fn = tgr([(f, G.GREEN)], -1, 2, F(1, 2), -1.5, 1.5, YT1)
    st = V(lv, [('The figure shows the graph of a function \\(y=f(x)\\) on \\([-\\pi;\\,2\\pi]\\). On which interval is the function increasing?', 'Hình vẽ là đồ thị của hàm số \\(y=f(x)\\) trên \\([-\\pi;\\,2\\pi]\\). Hàm số đồng biến trên khoảng nào?'),
               ('Use the graph of \\(y=f(x)\\) on \\([-\\pi;\\,2\\pi]\\) in the figure. The function increases on which interval?', 'Dựa vào đồ thị hàm số \\(y=f(x)\\) trên \\([-\\pi;\\,2\\pi]\\) trong hình. Hàm số đồng biến trên khoảng nào?'),
               ('From the graph of \\(y=f(x)\\) in the figure, choose an interval on which \\(f\\) is increasing.', 'Từ đồ thị hàm số \\(y=f(x)\\) trong hình, chọn một khoảng mà trên đó \\(f\\) đồng biến.')])
    return dict(en=st[0], vi=st[1],
                opts=[ivl(*g)] + [ivl(*b) for b in bad[:3]], fig=G.FIG(fn, 'Graph of a trigonometric function', 'Đồ thị hàm số lượng giác', 440),
                ee='On \\(%s\\) the graph goes up from left to right; on each other interval it goes down at least partly.' % ivl(*g),
                ev='Trên \\(%s\\) đồ thị đi lên từ trái sang phải; trên mỗi khoảng còn lại đồ thị có đoạn đi xuống.' % ivl(*g))

def b3_period_fig(r, lv, ctx):
    b = r.choice([F(2), F(1, 2), F(3), F(4), F(2, 3)]); trig = r.choice(['sin', 'cos']); A = r.choice([1, 2])
    T = 2 / b
    f = (lambda x: A * math.sin(float(b) * x)) if trig == 'sin' else (lambda x: A * math.cos(float(b) * x))
    fn = tgr([(f, G.GREEN)], -T / 2, 2 * T, T / 4, -A - .5, A + .5, [(A, str(A)), (-A, str(-A))])
    cand = [T, T / 2, 2 * T, T * F(3, 2), T * 4]
    opts = []
    for c in cand:
        if pit(c) not in opts: opts.append(pit(c))
    st = V(lv, [('The figure shows the graph of a function \\(y=f(x)\\) of the form \\(y=a\\sin bx\\) or \\(y=a\\cos bx\\). What is its period?', 'Hình vẽ là đồ thị của hàm số \\(y=f(x)\\) có dạng \\(y=a\\sin bx\\) hoặc \\(y=a\\cos bx\\). Chu kì của hàm số là bao nhiêu?'),
               ('Based on the graph in the figure, find the period of the function \\(y=f(x)\\).', 'Dựa vào đồ thị trong hình, tìm chu kì của hàm số \\(y=f(x)\\).'),
               ('The graph of a periodic function \\(y=f(x)\\) is shown. Its period is…', 'Cho đồ thị của hàm số tuần hoàn \\(y=f(x)\\) như hình vẽ. Chu kì của hàm số là…')])
    return dict(en=st[0], vi=st[1],
                opts=distinct4(opts[:4]), fig=G.FIG(fn, 'Graph of a periodic function', 'Đồ thị hàm số tuần hoàn', 440),
                ee='The graph repeats after every \\(%s\\) (from one peak to the next).' % pit(T), ev='Đồ thị lặp lại sau mỗi đoạn dài \\(%s\\) (từ một đỉnh đến đỉnh kế tiếp).' % pit(T))

def b3_which_fig(r, lv, ctx):
    a = r.choice([-1, 1, 2]); b = r.choice([1, 2, 3]); trig = r.choice(['sin', 'cos'])
    def mk(a_, b_, t_): return ('y=%s%s\\%s x' % (('%d' % a_) if a_ else '', ('%+d' % b_).replace('+1', '+').replace('-1', '-') if a_ else ('%d' % b_).replace('-1', '-').replace('1', '') if abs(b_) == 1 else '%d' % b_, t_),
                                (lambda x: a_ + b_ * (math.sin(x) if t_ == 'sin' else math.cos(x))))
    good = mk(a, b, trig); other = 'cos' if trig == 'sin' else 'sin'
    cands = [mk(a, b, other), mk(a, -b, trig), mk(b, a, trig) if a != b and a > 0 else mk(-a, b, trig), mk(a, -b, other)]
    X = [i * 0.37 for i in range(-8, 18)]
    bad = []
    for t, g in cands:
        if t != good[0] and t not in bad and any(abs(g(x) - good[1](x)) > 1e-6 for x in X): bad.append(t)
    fn = tgr([(good[1], G.GREEN)], -1, 2, F(1, 2), a - b - .7, a + b + .7, [(v, str(v)) for v in sorted({a - b, a + b, a}) if v != 0])
    st = V(lv, [('The figure shows the graph of which function?', 'Hình vẽ là đồ thị của hàm số nào?'), ('Which function has the graph shown in the figure?', 'Hàm số nào có đồ thị như hình vẽ?'), ('The curve in the figure is the graph of…', 'Đường cong trong hình là đồ thị của hàm số…')])
    return dict(en=st[0], vi=st[1], opts=distinct4([good[0]] + bad[:3]),
                fig=G.FIG(fn, 'Graph of a trigonometric function', 'Đồ thị hàm số lượng giác', 440),
                ee='Maximum \\(%d\\), minimum \\(%d\\); at \\(x=0\\) the value is \\(%d\\). Only \\(%s\\) fits all three.' % (a + b, a - b, round(good[1](0)), good[0]),
                ev='Giá trị lớn nhất \\(%d\\), nhỏ nhất \\(%d\\); tại \\(x=0\\) giá trị là \\(%d\\). Chỉ \\(%s\\) thỏa mãn cả ba điều này.' % (a + b, a - b, round(good[1](0)), good[0]))

INTER = [('\\sin x', '\\cos x', math.sin, math.cos, (F(1, 4), F(5, 4))), ('\\sin x', '\\dfrac12', math.sin, lambda x: .5, (F(1, 6), F(5, 6))),
         ('\\cos x', '-\\dfrac12', math.cos, lambda x: -.5, (F(2, 3), F(4, 3))), ('\\sin x', '-\\dfrac{\\sqrt2}{2}', math.sin, lambda x: -(2 ** .5) / 2, (F(5, 4), F(7, 4))),
         ('\\cos x', '\\dfrac{\\sqrt3}{2}', math.cos, lambda x: 3 ** .5 / 2, (F(1, 6), F(11, 6))), ('\\sin x', '-\\dfrac12', math.sin, lambda x: -.5, (F(7, 6), F(11, 6)))]
def b3_inter_fig(r, lv, ctx):
    i = r.randrange(len(INTER)); a, b, f, g, sol = INTER[i]
    for s in sol: assert abs(f(float(s) * math.pi) - g(float(s) * math.pi)) < 1e-9
    xs = [0.000137 + k * (2 * math.pi - 0.0003) / 2400 for k in range(2401)]; cnt = sum(1 for x1, x2 in zip(xs, xs[1:]) if (f(x1) - g(x1)) * (f(x2) - g(x2)) < 0)
    assert cnt == 2
    fn = tgr([(f, G.GREEN), (g, G.ORANGE)], 0, 2, F(1, 4), -1.4, 1.4, YT1, dots=[(float(s) * math.pi, f(float(s) * math.pi), False) for s in sol])
    def st(p): return 'x=%s,\\ x=%s' % (pit(p[0]), pit(p[1]))
    bad = [INTER[j][4] for j in range(len(INTER)) if j != i and INTER[j][4] != sol]; r.shuffle(bad)
    return dict(en='The figure shows the graphs of \\(y=%s\\) and \\(y=%s\\) on \\([0;\\,2\\pi]\\). The \\(x\\)-coordinates of their common points are…' % (a, b),
                vi='Hình vẽ là đồ thị của \\(y=%s\\) và \\(y=%s\\) trên \\([0;\\,2\\pi]\\). Hoành độ các giao điểm là…' % (a, b),
                opts=distinct4([st(sol)] + [st(p) for p in bad[:3]]), fig=G.FIG(fn, 'Two graphs and their common points', 'Hai đồ thị và các giao điểm', 440),
                ee='Solve \\(%s=%s\\) on \\([0;\\,2\\pi]\\): \\(%s\\).' % (a, b, st(sol)), ev='Giải \\(%s=%s\\) trên \\([0;\\,2\\pi]\\): \\(%s\\).' % (a, b, st(sol)))

def b3_tide_fig(r, lv, ctx):
    c = r.choice([5, 6, 8, 10]); A = r.choice([2, 3]); trig = r.choice(['sin', 'cos', 'sin'])
    f = (lambda t: c + A * math.sin(math.pi * t / 6)) if trig == 'sin' else (lambda t: c + A * math.cos(math.pi * t / 6))
    ask = r.choice(['max', 'min']) if trig == 'sin' else 'min'
    ts = [k / 100 for k in range(0, 1201)]; vals = [f(t) for t in ts]
    ext = max(vals) if ask == 'max' else min(vals); sol = [t for t, v in zip(ts, vals) if abs(v - ext) < 1e-9]
    assert len(sol) == 1 and abs(sol[0] - round(sol[0])) < 1e-9; good = int(round(sol[0]))
    fn = G.graph_svg([(f, G.BLUE)], (0, 24), (0, c + A + 1.5), G.int_ticks(3, 24, 3), [(v, str(v)) for v in (c - A, c, c + A)], names=('t', 'h'), W=9, H=4.2)
    w = ('highest', 'cao nhất') if ask == 'max' else ('lowest', 'thấp nhất')
    return dict(en='The figure shows the water depth \\(h\\) (m) at a harbour \\(t\\) hours after midnight, \\(h=%d+%d\\%s\\dfrac{\\pi t}{6}\\). In the first 12 hours \\((0\\lt t\\lt12)\\), when is the water %s?' % (c, A, trig, w[0]),
                vi='Hình vẽ biểu diễn độ sâu \\(h\\) (m) của mực nước ở một cảng sau \\(t\\) giờ kể từ 0 giờ, \\(h=%d+%d\\%s\\dfrac{\\pi t}{6}\\). Trong 12 giờ đầu \\((0\\lt t\\lt12)\\), mực nước %s lúc mấy giờ?' % (c, A, trig, w[1]),
                opts=['%d' % x for x in [good] + [v for v in (3, 6, 9, 12) if v != good]], fig=G.FIG(fn, 'Water depth over time', 'Độ sâu mực nước theo thời gian', 440),
                ee='The %s value \\(%d\\) m is reached when \\(\\%s\\dfrac{\\pi t}{6}=%s1\\), i.e. \\(t=%d\\).' % (w[0], ext, trig, '' if ask == 'max' else '-', good),
                ev='Giá trị %s \\(%d\\) m đạt được khi \\(\\%s\\dfrac{\\pi t}{6}=%s1\\), tức \\(t=%d\\).' % (w[1], ext, trig, '' if ask == 'max' else '-', good))

def b3_compare(r, lv, ctx):
    den = r.choice([5, 7, 8, 9, 10])
    def stm(fn, a, b, rel):
        ft = {'sin': math.sin, 'cos': math.cos, 'tan': math.tan}[fn]
        va, vb = ft(float(a) * math.pi), ft(float(b) * math.pi)
        ar = lambda v: pit(v) if v > 0 else '\\left(%s\\right)' % pit(v)
        tex = '\\%s%s%s\\%s%s' % (fn, ar(a), '\\lt' if rel == '<' else '\\gt', fn, ar(b))
        return tex, (va < vb) if rel == '<' else (va > vb)
    S = []
    for _ in range(60):
        fn = r.choice(['sin', 'cos', 'tan'])
        if fn == 'cos': lo, hi = 1, den - 1
        else: lo, hi = -(den // 2 - (1 if den % 2 == 0 else 0)), den // 2 - (1 if den % 2 == 0 else 0)
        i, j = sorted(r.sample(range(lo, hi + 1), 2))
        if i == 0 or j == 0: continue
        S.append(stm(fn, F(i, den), F(j, den), r.choice('<>')))
    tr = [s for s in S if s[1]]; fa = [s for s in S if not s[1]]
    good = tr[0][0]; bads = []
    for s in fa:
        if s[0] not in bads: bads.append(s[0])
    st = V(lv, [('Which inequality is true?', 'Bất đẳng thức nào đúng?'), ('Which comparison is correct?', 'So sánh nào đúng?'), ('Choose the true statement.', 'Chọn khẳng định đúng.')])
    return dict(en=st[0], vi=st[1], opts=distinct4([good] + bads[:3]),
                ee='\\(\\sin\\) and \\(\\tan\\) increase on \\(\\left(-\\dfrac{\\pi}{2};\\dfrac{\\pi}{2}\\right)\\); \\(\\cos\\) decreases on \\((0;\\pi)\\). Hence \\(%s\\).' % good,
                ev='\\(\\sin\\) và \\(\\tan\\) đồng biến trên \\(\\left(-\\dfrac{\\pi}{2};\\dfrac{\\pi}{2}\\right)\\); \\(\\cos\\) nghịch biến trên \\((0;\\pi)\\). Do đó \\(%s\\).' % good)

def b3_ferris(r, lv, ctx):
    T = r.choice([12, 18, 24, 30]); R = r.choice([16, 18, 20]); c = R + 2
    t = r.choice([T // 6, T // 3, T // 2, 2 * T // 3])
    h = c - R * math.cos(2 * math.pi * t / T); good = round(h); assert abs(h - good) < 1e-9
    cand = [c + R // 2, c - R // 2, c, c + R, c - R]
    return dict(en='The height of a seat on a Ferris wheel is \\(h(t)=%d-%d\\cos\\dfrac{2\\pi t}{%d}\\) (m), \\(t\\) in minutes. Find the height at \\(t=%d\\).' % (c, R, T, t),
                vi='Độ cao của một ca bin vòng quay là \\(h(t)=%d-%d\\cos\\dfrac{2\\pi t}{%d}\\) (m), \\(t\\) tính bằng phút. Tính độ cao tại \\(t=%d\\).' % (c, R, T, t),
                opts=nopts(r, good, [x for x in cand if x != good], step=2),
                ee='\\(\\dfrac{2\\pi\\cdot%d}{%d}=%s\\), \\(\\cos%s=%s\\), so \\(h=%d\\) m.' % (t, T, pit(F(2 * t, T)), pit(F(2 * t, T)), tex_num(math.cos(2 * math.pi * t / T)), good),
                ev='\\(\\dfrac{2\\pi\\cdot%d}{%d}=%s\\), \\(\\cos%s=%s\\) nên \\(h=%d\\) m.' % (t, T, pit(F(2 * t, T)), pit(F(2 * t, T)), tex_num(math.cos(2 * math.pi * t / T)), good))

def b3_shift(r, lv, ctx):
    base = r.choice(['\\sin x', '\\cos x', '\\tan x']); kind = r.choice(['L', 'R', 'U', 'D'])
    if kind in 'LR':
        p = r.choice([F(1, 6), F(1, 4), F(1, 3), F(1, 2), F(2, 3)]); sp = pit(p)
        new = base.replace('x', '\\left(x%s%s\\right)' % ('+' if kind == 'L' else '-', sp))
        amt_e = amt_v = '\\(%s\\)' % sp
    else:
        p = r.choice([1, 2, 3]); new = 'y=%s%s%d' % (base, '+' if kind == 'U' else '-', p); amt_e = '\\(%d\\) units' % p; amt_v = '\\(%d\\) đơn vị' % p
    if kind in 'LR': new = 'y=' + new
    names = {'L': ('to the left by %s', 'sang trái %s'), 'R': ('to the right by %s', 'sang phải %s'), 'U': ('upward by %s', 'lên trên %s'), 'D': ('downward by %s', 'xuống dưới %s')}
    order = [kind] + [k for k in 'LRUD' if k != kind]
    opts = [tx('Translate %s' % (names[k][0] % amt_e), 'Tịnh tiến %s' % (names[k][1] % amt_v)) for k in order]
    return dict(en='The graph of \\(%s\\) is obtained from the graph of \\(y=%s\\) by which translation?' % (new, base), vi='Đồ thị hàm số \\(%s\\) nhận được từ đồ thị hàm số \\(y=%s\\) bằng phép tịnh tiến nào?' % (new, base),
                opts=opts, ee='\\(y=f(x+a)\\) moves the graph left by \\(a\\) \\((a\\gt0)\\), \\(y=f(x-a)\\) right; \\(y=f(x)\\pm b\\) moves it up/down.',
                ev='\\(y=f(x+a)\\) dời đồ thị sang trái \\(a\\) \\((a\\gt0)\\), \\(y=f(x-a)\\) sang phải; \\(y=f(x)\\pm b\\) dời lên/xuống.')

D3 = [b3_inc_fig, b3_period_fig, b3_which_fig, b3_inter_fig, b3_tide_fig, b3_compare, b3_ferris, b3_shift]

# =====================================================================================================
# BÀI 4. Phương trình lượng giác cơ bản
# =====================================================================================================
def norm(a, per=2):
    """Đưa bội của π về khoảng (-per/2; per/2]."""
    a = F(a) % per
    if a > F(per, 2): a -= per
    return a
def fam_set(fams):
    s = set()
    for off, per in fams:
        for k in range(-30, 31):
            v = F(off) + k * F(per)
            if -4 <= v <= 4: s.add(v)
    return s
def fam_tex(fams, deg=False):
    out = []
    for off, per in fams:
        if deg:
            out.append('x=%s^\\circ+k%d^\\circ' % (off, per))
        else:
            pt = {F(2): 'k2\\pi', F(1): 'k\\pi', F(1, 2): 'k\\dfrac{\\pi}{2}'}[F(per)]
            out.append(('x=%s+%s' % (pit(off), pt)) if off != 0 else 'x=%s' % pt)
    return ',\\ '.join(out)
def arg(c): return 'x%s%s' % ('+' if c > 0 else '-', pit(abs(c)))

def b4_shift(r, lv, ctx):
    fn = r.choice(['sin', 'cos']); c = r.choice([F(1, 6), F(1, 4), F(1, 3), F(-1, 6), F(-1, 4), F(-1, 3)])
    d = r.choice([F(1, 6), F(1, 4), F(1, 3), F(2, 3), F(3, 4), F(5, 6)])
    if fn == 'sin':
        good = [(norm(d - c), 2), (norm(1 - d - c), 2)]; bads = [[(norm(d + c), 2), (norm(1 - d + c), 2)], [(norm(d - c), 1)], [(norm(d - c), 2), (norm(-d - c), 2)]]
    else:
        good = [(norm(d - c), 2), (norm(-d - c), 2)]; bads = [[(norm(d + c), 2), (norm(-d + c), 2)], [(norm(d - c), 1)], [(norm(d - c), 2), (norm(1 - d - c), 2)]]
    f = math.sin if fn == 'sin' else math.cos
    gs = fam_set(good)
    for v in gs: assert abs(f(float(v + c) * math.pi) - f(float(d) * math.pi)) < 1e-9
    xs = [F(k, 24) for k in range(-96, 97)]
    truth = {x for x in xs if abs(f(float(x + c) * math.pi) - f(float(d) * math.pi)) < 1e-9}
    assert truth == {x for x in gs if -4 <= x <= 4 and x.denominator in (1, 2, 3, 4, 6, 8, 12, 24)}
    for b in bads: assert fam_set(b) != gs
    eq = '\\%s\\left(%s\\right)=\\%s%s' % (fn, arg(c), fn, pit(d))
    return dict(en='The solutions of \\(%s\\) are…' % eq, vi='Nghiệm của phương trình \\(%s\\) là…' % eq, opts=distinct4([fam_tex(good)] + [fam_tex(b) for b in bads]),
                ee='\\(%s\\iff %s\\) \\((k\\in\\mathbb Z)\\).' % (eq, fam_tex(good)), ev='\\(%s\\iff %s\\) \\((k\\in\\mathbb Z)\\).' % (eq, fam_tex(good)))

def b4_sum(r, lv, ctx):
    fn = r.choice(['sin', 'cos']); k2 = r.choice([2, 3])
    vals = {'\\dfrac12': .5, '\\dfrac{\\sqrt3}{2}': 3 ** .5 / 2, '\\dfrac{\\sqrt2}{2}': 2 ** .5 / 2, '-\\dfrac12': -.5, '-\\dfrac{\\sqrt2}{2}': -(2 ** .5) / 2}
    vt = r.choice(list(vals)); v = vals[vt]
    f = math.sin if fn == 'sin' else math.cos
    grid = [F(j, 72) for j in range(0, 73)]                     # x/π trên [0; π]
    sol = [x for x in grid if abs(f(k2 * float(x) * math.pi) - v) < 1e-9]
    if not 2 <= len(sol) <= 6: raise AssertionError
    S = sum(sol, F(0))
    cand = [S + F(1, 2), S - F(1, 2), sol[0], 2 * S, S + 1, S / 2]
    bad = []
    for c in cand:
        if c > 0 and c != S and c not in bad: bad.append(c)
    return dict(en='Find the sum of the solutions of \\(\\%s %dx=%s\\) on \\([0;\\,\\pi]\\).' % (fn, k2, vt), vi='Tính tổng các nghiệm của phương trình \\(\\%s %dx=%s\\) trên đoạn \\([0;\\,\\pi]\\).' % (fn, k2, vt),
                opts=distinct4([pit(S)] + [pit(b) for b in bad[:3]]),
                ee='The solutions in \\([0;\\,\\pi]\\) are \\(%s\\); their sum is \\(%s\\).' % (';\\ '.join(pit(x) for x in sol), pit(S)),
                ev='Các nghiệm thuộc \\([0;\\,\\pi]\\) là \\(%s\\); tổng bằng \\(%s\\).' % (';\\ '.join(pit(x) for x in sol), pit(S)))

TANV = {'1': 45, '\\sqrt3': 60, '\\dfrac{\\sqrt3}{3}': 30, '-1': -45, '-\\sqrt3': -60}
def b4_tandeg(r, lv, ctx):
    vt = r.choice(list(TANV)); b = TANV[vt]; a = r.choice([10, 15, 20, 25, 35, 40, 50])
    good = [(a + b, 180)]; bads = [[(a + b, 360)], [(b - a, 180)], [(a + b, 90)]]
    for k in range(-3, 4): assert abs(math.tan(math.radians(a + b + 180 * k - a)) - math.tan(math.radians(b))) < 1e-9
    return dict(en='Solve \\(\\tan(x-%d^\\circ)=%s\\).' % (a, vt), vi='Giải phương trình \\(\\tan(x-%d^\\circ)=%s\\).' % (a, vt),
                opts=distinct4([fam_tex(good, True)] + [fam_tex(x, True) for x in bads]),
                ee='\\(x-%d^\\circ=%d^\\circ+k180^\\circ\\), so \\(x=%d^\\circ+k180^\\circ\\).' % (a, b, a + b), ev='\\(x-%d^\\circ=%d^\\circ+k180^\\circ\\) nên \\(x=%d^\\circ+k180^\\circ\\).' % (a, b, a + b))

def b4_cond(r, lv, ctx):
    c = r.choice([1, 2, 3, -1, -2]); form = r.choice(['s', 'c'])
    if form == 's': eq = '\\sin x=m%+d' % c; lo, hi = -1 - c, 1 - c; wl, wh = -1 + c, 1 + c
    else: eq = '2\\cos x=m%+d' % c; lo, hi = -2 - c, 2 - c; wl, wh = -2 + c, 2 + c
    for m in range(lo - 3, hi + 4):
        val = (m + c) if form == 's' else F(m + c, 2)
        assert (lo <= m <= hi) == (-1 <= val <= 1)
    opts = ['%d\\le m\\le %d' % (lo, hi), '%d\\lt m\\lt %d' % (lo, hi), '%d\\le m\\le %d' % (wl, wh), '-1\\le m\\le 1']
    return dict(en='For which values of \\(m\\) does the equation \\(%s\\) have solutions?' % eq, vi='Với giá trị nào của \\(m\\) thì phương trình \\(%s\\) có nghiệm?' % eq, opts=distinct4(opts),
                ee='The equation has solutions iff \\(%s\\le m%+d\\le %s\\), i.e. \\(%d\\le m\\le %d\\).' % ('-1' if form == 's' else '-2', c, '1' if form == 's' else '2', lo, hi),
                ev='Phương trình có nghiệm khi và chỉ khi \\(%s\\le m%+d\\le %s\\), tức \\(%d\\le m\\le %d\\).' % ('-1' if form == 's' else '-2', c, '1' if form == 's' else '2', lo, hi))

CIRC = [('\\sin x=\\dfrac12', (30, 150)), ('\\sin x=-\\dfrac{\\sqrt3}{2}', (240, 300)), ('\\cos x=\\dfrac12', (60, 300)), ('\\cos x=-\\dfrac{\\sqrt2}{2}', (135, 225)),
        ('\\tan x=1', (45, 225)), ('\\tan x=-\\sqrt3', (120, 300)), ('\\cos x=\\dfrac{\\sqrt3}{2}', (30, 330)), ('\\sin x=\\dfrac{\\sqrt2}{2}', (45, 135))]
def _ev_eq(eq, a):
    fn, rhs = eq.split('=')
    t = {'\\sin x': math.sin, '\\cos x': math.cos, '\\tan x': math.tan}[fn](math.radians(a))
    v = {'\\dfrac12': .5, '-\\dfrac{\\sqrt3}{2}': -(3 ** .5) / 2, '-\\dfrac{\\sqrt2}{2}': -(2 ** .5) / 2, '1': 1, '-\\sqrt3': -(3 ** .5), '\\dfrac{\\sqrt3}{2}': 3 ** .5 / 2, '\\dfrac{\\sqrt2}{2}': 2 ** .5 / 2}[rhs]
    return abs(t - v) < 1e-9
def b4_circle_fig(r, lv, ctx):
    i = r.randrange(len(CIRC)); eq, pts = CIRC[i]
    assert {a for a in range(0, 360, 15) if _ev_eq(eq, a)} == set(pts)
    bad = [CIRC[j][0] for j in range(len(CIRC)) if set(CIRC[j][1]) != set(pts)]; r.shuffle(bad)
    fn = G.circle_svg([(a, None) for a in pts], showA=True, dashed=[pts])
    st = V(lv, [('The two marked points on the trigonometric circle represent all solutions of which equation?', 'Hai điểm được đánh dấu trên đường tròn lượng giác biểu diễn tất cả các nghiệm của phương trình nào?'),
               ('All solutions of an equation are shown by the two points on the trigonometric circle. Which equation is it?', 'Tất cả các nghiệm của một phương trình được biểu diễn bởi hai điểm trên đường tròn lượng giác. Đó là phương trình nào?'),
               ('Which equation has its solutions represented exactly by the two marked points on the trigonometric circle?', 'Phương trình nào có các nghiệm được biểu diễn đúng bởi hai điểm đánh dấu trên đường tròn lượng giác?')])
    return dict(en=st[0], vi=st[1],
                opts=[eq] + bad[:3], fig=G.FIG(fn, 'Two points on the trigonometric circle', 'Hai điểm trên đường tròn lượng giác', 280),
                ee='The points correspond to \\(%s\\) and \\(%s\\), which are exactly the solutions of \\(%s\\) on one turn.' % (pit(F(pts[0], 180)), pit(F(pts[1], 180)), eq),
                ev='Hai điểm ứng với các góc \\(%s\\) và \\(%s\\), đúng là các nghiệm của \\(%s\\) trên một vòng.' % (pit(F(pts[0], 180)), pit(F(pts[1], 180)), eq))

def b4_spring(r, lv, ctx):
    A = r.choice([4, 6, 8, 10]); w = r.choice([F(1, 2), F(1, 3), F(1, 4)])
    tg = {'h': (F(A, 2), F(1, 3)), 'mh': (F(-A, 2), F(2, 3)), 'z': (F(0), F(1, 2)), 'm': (F(-A), F(1))}
    k = r.choice(list(tg)); x0, th = tg[k]; t = th / w
    tt = [j / 1000 for j in range(1, 20001)]; first = next(s for s in tt if abs(A * math.cos(float(w) * math.pi * s) - float(x0)) < 2e-3 * A)
    assert abs(first - float(t)) < 0.01
    bad = [o / w for kk, (_, o) in tg.items() if kk != k] + [th, t * 2]
    wt = {F(1, 2): '\\dfrac{\\pi t}{2}', F(1, 3): '\\dfrac{\\pi t}{3}', F(1, 4): '\\dfrac{\\pi t}{4}'}[w]
    return dict(en='The position of a weight on a spring is \\(x(t)=%d\\cos%s\\) (cm), \\(t\\) in seconds. When does \\(x\\) first equal \\(%s\\) cm \\((t\\gt0)\\)?' % (A, wt, frt(x0)),
                vi='Li độ của một vật gắn với lò xo là \\(x(t)=%d\\cos%s\\) (cm), \\(t\\) tính bằng giây. Lần đầu tiên \\(x=%s\\) cm \\((t\\gt0)\\) là lúc nào?' % (A, wt, frt(x0)),
                opts=nopts(r, t, bad, step=F(1, 3)) if True else None,
                ee='\\(\\cos%s=%s\\); the smallest positive value of \\(%s\\) is \\(%s\\), so \\(t=%s\\) s.' % (wt, frt(x0 / A), wt, pit(th), ne(t)),
                ev='\\(\\cos%s=%s\\); giá trị dương nhỏ nhất của \\(%s\\) là \\(%s\\) nên \\(t=%s\\) s.' % (wt, frt(x0 / A), wt, pit(th), nv(t)))

COTV = {'1': F(1, 4), '\\sqrt3': F(1, 6), '-1': F(3, 4), '\\dfrac{\\sqrt3}{3}': F(1, 3), '-\\sqrt3': F(5, 6)}
def b4_cot(r, lv, ctx):
    vt = r.choice(list(COTV)); b = COTV[vt]; c = r.choice([F(1, 6), F(1, 4), F(1, 3), F(-1, 6), F(-1, 3)])
    N = lambda a: norm(a, 1)
    good = [(N(b - c), 1)]; bads = [[(N(b - c), 2)], [(N(b + c), 1)], [(N(-b - c), 1)]]
    gs = fam_set(good)
    for v in gs: assert abs(1 / math.tan(float(v + c) * math.pi) - 1 / math.tan(float(b) * math.pi)) < 1e-9
    for x in bads: assert fam_set(x) != gs
    eq = '\\cot\\left(%s\\right)=%s' % (arg(c), vt)
    return dict(en='Solve \\(%s\\).' % eq, vi='Giải phương trình \\(%s\\).' % eq, opts=distinct4([fam_tex(good)] + [fam_tex(x) for x in bads]),
                ee='\\(%s=%s+k\\pi\\), so \\(%s\\).' % (arg(c), pit(b), fam_tex(good)), ev='\\(%s=%s+k\\pi\\) nên \\(%s\\).' % (arg(c), pit(b), fam_tex(good)))

GRF = [('cos', '\\dfrac12', .5, F(-1), F(1), (F(-1, 3), F(1, 3))), ('cos', '-\\dfrac12', -.5, F(-1), F(1), (F(-2, 3), F(2, 3))), ('sin', '-\\dfrac12', -.5, F(-1), F(1), (F(-5, 6), F(-1, 6))),
       ('tan', '1', 1, F(-1, 2), F(3, 2), (F(1, 4), F(5, 4))), ('tan', '-1', -1, F(-1, 2), F(3, 2), (F(3, 4), F(-1, 4))), ('sin', '\\dfrac{\\sqrt3}{2}', 3 ** .5 / 2, F(-1), F(1), (F(1, 3), F(2, 3)))]
def b4_graph_fig(r, lv, ctx):
    i = r.randrange(len(GRF)); fn, mt, m, lo, hi, sol = GRF[i]; sol = tuple(sorted(sol))
    f = {'sin': math.sin, 'cos': math.cos, 'tan': math.tan}[fn]
    for s in sol: assert abs(f(float(s) * math.pi) - m) < 1e-9 and lo < s < hi
    xs = [float(lo) * math.pi + 1e-4 + j * (float(hi - lo) * math.pi - 2e-4) / 3000 for j in range(3001)]
    cnt = 0
    for x1, x2 in zip(xs, xs[1:]):
        if fn == 'tan' and math.cos(x1) * math.cos(x2) <= 0: continue
        if (f(x1) - m) * (f(x2) - m) < 0: cnt += 1
    assert cnt == 2
    def ff(x):
        if fn == 'tan' and abs(math.cos(x)) < 0.12: return None
        return f(x)
    vl = [(float(v) * math.pi, None) for v in (F(-1, 2), F(1, 2), F(3, 2)) if fn == 'tan' and lo <= v <= hi]
    yr = (-3.2, 3.2) if fn == 'tan' else (-1.5, 1.5)
    img = G.graph_svg([(ff, G.GREEN), (lambda x: m, G.ORANGE)], (float(lo) * math.pi, float(hi) * math.pi), yr, G.pi_ticks(lo, hi, F(1, 4) if fn == 'tan' else F(1, 3) if i < 2 or i == 5 else F(1, 6)),
                      [(1, '1'), (-1, '-1')], vlines=vl, dots=[(float(s) * math.pi, m, False) for s in sol])
    def st(p): return 'x=%s,\\ x=%s' % (pit(p[0]), pit(p[1]))
    bad = []
    for j, g in enumerate(GRF):
        p = tuple(sorted(g[5]))
        if p != sol and st(p) not in bad: bad.append(st(p))
    r.shuffle(bad)
    dom = '\\left(%s;\\,%s\\right)' % (pit(lo), pit(hi)) if fn == 'tan' else '[%s;\\,%s]' % (pit(lo), pit(hi))
    return dict(en='The figure shows the graph of \\(y=\\%s x\\) and the line \\(y=%s\\) on \\(%s\\). Which values of \\(x\\) in this interval satisfy \\(\\%s x=%s\\)?' % (fn, mt, dom, fn, mt),
                vi='Hình vẽ là đồ thị hàm số \\(y=\\%s x\\) và đường thẳng \\(y=%s\\) trên \\(%s\\). Những giá trị \\(x\\) nào thuộc khoảng này thỏa mãn \\(\\%s x=%s\\)?' % (fn, mt, dom, fn, mt),
                opts=distinct4([st(sol)] + bad[:3]), fig=G.FIG(img, 'Graph and a horizontal line', 'Đồ thị và một đường thẳng nằm ngang', 440),
                ee='The line meets the graph at two points with \\(%s\\).' % st(sol), ev='Đường thẳng cắt đồ thị tại hai điểm có \\(%s\\).' % st(sol))

D4 = [b4_shift, b4_sum, b4_tandeg, b4_cond, b4_circle_fig, b4_spring, b4_cot, b4_graph_fig]

# =====================================================================================================
# BÀI 5. Dãy số
# =====================================================================================================
SEQ = [('2n-1', lambda n: 2 * n - 1), ('3n-2', lambda n: 3 * n - 2), ('6-n', lambda n: 6 - n), ('(-1)^n n', lambda n: (-1) ** n * n), ('\\dfrac{12}{n}', lambda n: F(12, n)),
       ('2^{n-1}', lambda n: 2 ** (n - 1)), ('n^2-4n+5', lambda n: n * n - 4 * n + 5), ('7-2n', lambda n: 7 - 2 * n), ('(-1)^{n+1}\\cdot 2', lambda n: (-1) ** (n + 1) * 2), ('n^2-2', lambda n: n * n - 2)]
def b5_dots_fig(r, lv, ctx):
    i = r.randrange(len(SEQ)); t, f = SEQ[i]; vals = [f(n) for n in range(1, 6)]
    bad = [s for s, g in SEQ if s != t and [g(n) for n in range(1, 6)] != vals]; r.shuffle(bad)
    lo, hi = min(vals + [0]), max(vals + [0])
    step = 1 if hi - lo <= 12 else 2
    img = G.graph_svg([], (-0.4, 5.6), (lo - 1, hi + 1.2), G.int_ticks(1, 5), G.int_ticks(lo, hi, step), dots=[(n, float(v), False) for n, v in zip(range(1, 6), vals)], names=('n', 'u_n'), W=6.5, H=4.4)
    st = V(lv, [('The figure shows the points \\((n;\\,u_n)\\) for the first five terms of a sequence \\((u_n)\\). Which formula can be the general term?', 'Hình vẽ biểu diễn các điểm \\((n;\\,u_n)\\) ứng với năm số hạng đầu của dãy số \\((u_n)\\). Công thức nào có thể là số hạng tổng quát?'),
               ('The first five terms of \\((u_n)\\) are shown as points \\((n;\\,u_n)\\). Which general term fits?', 'Năm số hạng đầu của dãy \\((u_n)\\) được biểu diễn bởi các điểm \\((n;\\,u_n)\\). Số hạng tổng quát nào phù hợp?'),
               ('Read the first five terms from the figure. Which formula gives \\(u_n\\)?', 'Đọc năm số hạng đầu từ hình vẽ. Công thức nào cho \\(u_n\\)?')])
    return dict(en=st[0], vi=st[1],
                opts=['u_n=' + t] + ['u_n=' + b for b in bad[:3]], fig=G.FIG(img, 'Points of a sequence', 'Các điểm biểu diễn dãy số', 330),
                ee='The figure gives \\(%s\\); only \\(u_n=%s\\) gives these values.' % (';\\ '.join(ne(v) for v in vals), t), ev='Hình vẽ cho \\(%s\\); chỉ \\(u_n=%s\\) cho đúng các giá trị này.' % (';\\ '.join(nv(v) for v in vals), t))

def match_svg(kind):
    cv = G.Canvas(); s = 0.75; x0 = 0
    for n in (1, 2, 3):
        if kind == 'sq':
            for j in range(n):
                X = x0 + j * s
                cv.poly([(X, 0), (X + s, 0)], 'color={rgb,255:red,194;green,65;blue,12}, line width=1.6pt'); cv.poly([(X, s), (X + s, s)], 'color={rgb,255:red,194;green,65;blue,12}, line width=1.6pt')
                cv.poly([(X, 0), (X, s)], 'color={rgb,255:red,194;green,65;blue,12}, line width=1.6pt')
            cv.poly([(x0 + n * s, 0), (x0 + n * s, s)], 'color={rgb,255:red,194;green,65;blue,12}, line width=1.6pt')
            w = n * s
        else:
            h = s * 0.866
            for j in range(n):
                X = x0 + j * s / 2
                if j % 2 == 0: cv.poly([(X, 0), (X + s / 2, h), (X + s, 0)], 'color={rgb,255:red,194;green,65;blue,12}, line width=1.6pt')
                else: cv.poly([(X, h), (X + s / 2, 0), (X + s, h)], 'color={rgb,255:red,194;green,65;blue,12}, line width=1.6pt')
            bot = [(x0 + 2 * k * s / 2, 0) for k in range((n + 2) // 2 + 1)]
            cv.poly([(x0, 0), (x0 + ((n + 1) // 2) * s, 0)], 'color={rgb,255:red,194;green,65;blue,12}, line width=1.6pt')
            if n >= 2: cv.poly([(x0 + s / 2, h), (x0 + s / 2 + (n // 2) * s, h)], 'color={rgb,255:red,194;green,65;blue,12}, line width=1.6pt')
            w = (n + 1) / 2 * s
        cv.o.append('\\node[font=\\small, text=ink] at (%.3f,-0.45) {$n=%d$};' % (x0 + w / 2, n))
        x0 += w + 1.0
    return cv.svg()
def b5_match_fig(r, lv, ctx):
    kind = r.choice(['sq', 'tr']); k = r.randrange(10, 31)
    good = 3 * k + 1 if kind == 'sq' else 2 * k + 1
    assert [3 * n + 1 for n in (1, 2, 3)] == [4, 7, 10] and [2 * n + 1 for n in (1, 2, 3)] == [3, 5, 7]
    bad = [3 * k, 4 * k, 3 * k + 4] if kind == 'sq' else [2 * k, 3 * k, 2 * k + 3]
    shape = ('squares', 'hình vuông') if kind == 'sq' else ('triangles', 'tam giác')
    return dict(en='Matchsticks are used to make rows of %s as in the figure; \\(u_n\\) is the number of matchsticks in pattern \\(n\\). Find \\(u_{%d}\\).' % (shape[0], k),
                vi='Dùng que diêm xếp thành dãy các %s như hình vẽ; \\(u_n\\) là số que diêm ở hình thứ \\(n\\). Tính \\(u_{%d}\\).' % (shape[1], k),
                opts=nopts(r, good, bad), fig=G.FIG(match_svg(kind), 'Matchstick patterns', 'Các hình xếp bằng que diêm', 360),
                ee='\\(u_1=%d\\) and each new %s adds %d sticks: \\(u_n=%s\\), so \\(u_{%d}=%d\\).' % (4 if kind == 'sq' else 3, 'square' if kind == 'sq' else 'triangle', 3 if kind == 'sq' else 2, '3n+1' if kind == 'sq' else '2n+1', k, good),
                ev='\\(u_1=%d\\) và mỗi %s mới thêm %d que: \\(u_n=%s\\) nên \\(u_{%d}=%d\\).' % (4 if kind == 'sq' else 3, 'hình vuông' if kind == 'sq' else 'tam giác', 3 if kind == 'sq' else 2, '3n+1' if kind == 'sq' else '2n+1', k, good))

def b5_tele(r, lv, ctx):
    m = r.randrange(4, 12); typ = r.choice([0, 1])
    if typ == 0: t = '\\dfrac{1}{n(n+1)}'; S = sum(F(1, n * (n + 1)) for n in range(1, m + 1)); idea = ('\\dfrac1n-\\dfrac1{n+1}', '1-\\dfrac{1}{%d}' % (m + 1))
    else: t = '\\dfrac{1}{(n+1)(n+2)}'; S = sum(F(1, (n + 1) * (n + 2)) for n in range(1, m + 1)); idea = ('\\dfrac1{n+1}-\\dfrac1{n+2}', '\\dfrac12-\\dfrac{1}{%d}' % (m + 2))
    bad = [F(m, m + 2), 1 - F(1, m), S + F(1, (m + 1) * (m + 2)), S - F(1, m * (m + 1))]
    return dict(en='The sequence has \\(u_n=%s\\). Find \\(S=u_1+u_2+\\dots+u_{%d}\\).' % (t, m), vi='Cho dãy số \\(u_n=%s\\). Tính \\(S=u_1+u_2+\\dots+u_{%d}\\).' % (t, m),
                opts=distinct4([frt(S)] + [frt(x) for x in dict.fromkeys(b for b in bad if b != S)][:3]),
                ee='\\(u_n=%s\\), so the sum telescopes: \\(S=%s=%s\\).' % (idea[0], idea[1], frt(S)), ev='\\(u_n=%s\\) nên các số hạng triệt tiêu dần: \\(S=%s=%s\\).' % (idea[0], idea[1], frt(S)))

def b5_extreme(r, lv, ctx):
    a = r.randrange(5, 14); b = r.randrange(-5, 9); ask = r.choice(['max', 'min'])
    if ask == 'max': f = lambda n: -n * n + a * n + b; t = '-n^2%+dn%+d' % (a, b)
    else: f = lambda n: n * n - a * n + b; t = 'n^2-%dn%+d' % (a, b)
    t = t.replace('+0', '')
    vals = [f(n) for n in range(1, 200)]; ext = max(vals) if ask == 'max' else min(vals); n0 = vals.index(ext) + 1
    bad = [f(n0 + 1) if f(n0 + 1) != ext else f(n0 + 2), f(1), b, ext + (1 if ask == 'max' else -1)]
    w = ('largest', 'lớn nhất') if ask == 'max' else ('smallest', 'nhỏ nhất')
    return dict(en='Find the %s term of the sequence \\(u_n=%s\\).' % (w[0], t), vi='Tìm số hạng %s của dãy số \\(u_n=%s\\).' % (w[1], t), opts=nopts(r, ext, bad),
                ee='The parabola has its vertex at \\(n=%s\\); the nearest positive integer gives \\(u_{%d}=%d\\).' % (ne(F(a, 2)), n0, ext), ev='Parabol có đỉnh tại \\(n=%s\\); số nguyên dương gần nhất cho \\(u_{%d}=%d\\).' % (nv(F(a, 2)), n0, ext))

def b5_negcount(r, lv, ctx):
    p, q = sorted(r.sample(range(1, 16), 2))
    if q - p < 2: raise AssertionError
    a, b = p + q, p * q
    if r.random() < .5: b -= r.choice([1, 2])
    f = lambda n: n * n - a * n + b
    cnt = sum(1 for n in range(1, 300) if f(n) < 0)
    return dict(en='How many terms of the sequence \\(u_n=n^2-%dn+%d\\) are negative?' % (a, b), vi='Dãy số \\(u_n=n^2-%dn+%d\\) có bao nhiêu số hạng âm?' % (a, b),
                opts=nopts(r, cnt, [cnt + 1, cnt - 1, cnt + 2, q - p]),
                ee='\\(u_n\\lt0\\) for the integers \\(n\\) strictly between the roots of \\(x^2-%dx+%d\\); there are \\(%d\\) of them.' % (a, b, cnt), ev='\\(u_n\\lt0\\) với các số nguyên \\(n\\) nằm giữa hai nghiệm của \\(x^2-%dx+%d\\); có \\(%d\\) số như vậy.' % (a, b, cnt))

def b5_fish(r, lv, ctx):
    for _ in range(400):
        p = r.choice([F(3, 2), F(2), F(5, 4), F(6, 5)]); c = r.choice(range(20, 160, 10)); u1 = r.choice(range(100, 420, 20))
        u = [F(u1)]
        for _k in range(5): u.append(p * u[-1] - c)
        if all(x.denominator == 1 and x > 0 for x in u[:5]): break
    else: raise AssertionError
    k = r.choice([3, 4]); good = u[k - 1]
    bad = [u[k - 2], u[k], p ** (k - 1) * u1]
    pct = int((p - 1) * 100)
    return dict(en='A pond has \\(%d\\) fish at first. Each year the number of fish grows by \\(%d\\%%\\), then \\(%d\\) fish are caught. So \\(u_1=%d\\), \\(u_{n+1}=%s\\,u_n-%d\\). Find \\(u_{%d}\\).' % (u1, pct, c, u1, ne(p), c, k),
                vi='Một ao có \\(%d\\) con cá lúc đầu. Mỗi năm số cá tăng \\(%d\\%%\\), sau đó người ta bắt \\(%d\\) con. Khi đó \\(u_1=%d\\), \\(u_{n+1}=%s\\,u_n-%d\\). Tính \\(u_{%d}\\).' % (u1, pct, c, u1, nv(p), c, k),
                opts=nopts(r, good, bad, step=10), ee='\\(%s\\).' % ';\\ '.join('u_%d=%s' % (i + 1, ne(u[i])) for i in range(k)), ev='\\(%s\\).' % ';\\ '.join('u_%d=%s' % (i + 1, nv(u[i])) for i in range(k)))

def b5_param(r, lv, ctx):
    c = r.choice([1, 2, 3]); q = r.choice([1, 2, 3, 4, -1, -2]); b = c * q
    good = 'a\\gt %d' % q; bad = ['a\\lt %d' % q, 'a\\gt %d' % (-q), 'a\\gt 0' if q != 0 else 'a\\gt 1']
    if q == -0: raise AssertionError
    for a in (q - 1, q + 1):
        d = [F(a * (n + 1) + b, n + 1 + c) - F(a * n + b, n + c) for n in range(1, 30)]
        assert all(x > 0 for x in d) == (a > q) and all(x < 0 for x in d) == (a < q)
    if 'a\\gt %d' % (-q) == good: raise AssertionError
    return dict(en='For which values of \\(a\\) is the sequence \\(u_n=\\dfrac{an%+d}{n+%d}\\) increasing?' % (b, c), vi='Với giá trị nào của \\(a\\) thì dãy số \\(u_n=\\dfrac{an%+d}{n+%d}\\) là dãy số tăng?' % (b, c),
                opts=distinct4([good] + bad), ee='\\(u_{n+1}-u_n=\\dfrac{%da%+d}{(n+%d)(n+%d)}\\gt0\\iff a\\gt %d\\).' % (c, -b, c, c + 1, q),
                ev='\\(u_{n+1}-u_n=\\dfrac{%da%+d}{(n+%d)(n+%d)}\\gt0\\iff a\\gt %d\\).' % (c, -b, c, c + 1, q))

ISF = [('n^2+n', lambda n: n * n + n), ('n(n+2)', lambda n: n * (n + 2)), ('3n+2', lambda n: 3 * n + 2), ('2^n+1', lambda n: 2 ** n + 1), ('n^2-1', lambda n: n * n - 1), ('5n-3', lambda n: 5 * n - 3)]
def b5_isterm(r, lv, ctx):
    t, f = r.choice(ISF); k = r.randrange(6, 15) if '2^n' not in t else r.randrange(5, 10)
    good = f(k); S = {f(n) for n in range(1, 400)}
    bad = []
    for d in r.sample([-7, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 8, 10], 14):
        if good + d not in S and good + d > 0: bad.append(good + d)
    return dict(en='Which number is a term of the sequence \\(u_n=%s\\)?' % t, vi='Số nào là một số hạng của dãy số \\(u_n=%s\\)?' % t, opts=[str(good)] + [str(x) for x in bad[:3]],
                ee='\\(u_{%d}=%d\\); the other numbers do not equal \\(u_n\\) for any positive integer \\(n\\).' % (k, good), ev='\\(u_{%d}=%d\\); các số còn lại không bằng \\(u_n\\) với số nguyên dương \\(n\\) nào.' % (k, good))

D5 = [b5_dots_fig, b5_match_fig, b5_tele, b5_extreme, b5_negcount, b5_fish, b5_param, b5_isterm]

# =====================================================================================================
# BÀI 15. Giới hạn của dãy số
# =====================================================================================================
def lim_seq(f, n0=10 ** 6):
    return f(n0)
def b15_sumform(r, lv, ctx):
    a = r.choice([1, 2, 3, 4]); b = r.choice([1, 2, 3, 5, 7])
    forms = [('1+2+\\dots+n', lambda n: F(n * (n + 1), 2), 2, F(1, 2 * a)), ('1+3+5+\\dots+(2n-1)', lambda n: F(n * n), 2, F(1, a)),
             ('2+4+\\dots+2n', lambda n: F(n * (n + 1)), 2, F(1, a)), ('1^2+2^2+\\dots+n^2', lambda n: F(n * (n + 1) * (2 * n + 1), 6), 3, F(1, 3 * a))]
    t, S, deg, good = r.choice(forms)
    den = '%dn^%d+%d' % (a, deg, b) if a != 1 else 'n^%d+%d' % (deg, b)
    n = 10 ** 6; assert abs(float(S(n) / (a * n ** deg + b)) - float(good)) < 1e-5
    return dict(en='\\(\\lim\\dfrac{%s}{%s}=\\)…' % (t, den), vi='\\(\\lim\\dfrac{%s}{%s}=\\)…' % (t, den),
                opts=fo(good, [good * 2, '+\\infty', good / 2, F(1, a), 0]),
                ee='\\(%s=%s\\); divide numerator and denominator by \\(n^%d\\): the limit is \\(%s\\).' % (t, {'1+2+\\dots+n': '\\dfrac{n(n+1)}{2}', '1+3+5+\\dots+(2n-1)': 'n^2', '2+4+\\dots+2n': 'n(n+1)', '1^2+2^2+\\dots+n^2': '\\dfrac{n(n+1)(2n+1)}{6}'}[t], deg, frt(good)),
                ev='\\(%s=%s\\); chia cả tử và mẫu cho \\(n^%d\\): giới hạn bằng \\(%s\\).' % (t, {'1+2+\\dots+n': '\\dfrac{n(n+1)}{2}', '1+3+5+\\dots+(2n-1)': 'n^2', '2+4+\\dots+2n': 'n(n+1)', '1^2+2^2+\\dots+n^2': '\\dfrac{n(n+1)(2n+1)}{6}'}[t], deg, frt(good)))

def b15_param(r, lv, ctx):
    d = r.choice([1, 2, 3, 4]); L = r.choice([2, 3, 4, -1, -2, F(1, 2), F(3, 2)]); a = L * d
    if F(a).denominator != 1: raise AssertionError
    b = r.choice([-3, -1, 1, 2, 5]); e = r.choice([1, 3, 4, 7])
    num = 'an^2%s%+d' % (cx(b), r.choice([1, 2, -5])); den = ('%dn^2' % d if d != 1 else 'n^2') + '%+d' % e
    return dict(en='Given \\(\\lim\\dfrac{%s}{%s}=%s\\). Then \\(a=\\)…' % (num, den, frt(L)), vi='Biết \\(\\lim\\dfrac{%s}{%s}=%s\\). Khi đó \\(a=\\)…' % (num, den, frt(L)),
                opts=fo(a, [F(L, d), L, a + d, -a, a + 1]), ee='The limit equals \\(\\dfrac{a}{%d}\\), so \\(\\dfrac{a}{%d}=%s\\) and \\(a=%s\\).' % (d, d, frt(L), frt(a)),
                ev='Giới hạn bằng \\(\\dfrac{a}{%d}\\) nên \\(\\dfrac{a}{%d}=%s\\), suy ra \\(a=%s\\).' % (d, d, frt(L), frt(a)))

def b15_findq(r, lv, ctx):
    q = r.choice([F(1, 2), F(1, 3), F(2, 3), F(1, 4), F(3, 4), F(-1, 2), F(-1, 3), F(1, 5)]); u1 = r.choice([2, 3, 4, 6, 8, 9, 12])
    S = u1 / (1 - q)
    if S.denominator > 6: raise AssertionError
    tot = sum(u1 * q ** k for k in range(200)); assert abs(float(tot - S)) < 1e-9
    return dict(en='An infinite geometric series has first term \\(%d\\) and sum \\(%s\\). Find its common ratio.' % (u1, frt(S)), vi='Một cấp số nhân lùi vô hạn có số hạng đầu \\(%d\\) và tổng \\(%s\\). Tìm công bội của nó.' % (u1, frt(S)),
                opts=fo(q, [1 - q, -q, q / 2, 2 * q, q + F(1, 2)]),
                ee='\\(S=\\dfrac{u_1}{1-q}\\Rightarrow 1-q=\\dfrac{%d}{%s}=%s\\Rightarrow q=%s\\).' % (u1, frt(S), frt(1 - q), frt(q)),
                ev='\\(S=\\dfrac{u_1}{1-q}\\Rightarrow 1-q=\\dfrac{%d}{%s}=%s\\Rightarrow q=%s\\).' % (u1, frt(S), frt(1 - q), frt(q)))

def b15_root(r, lv, ctx):
    a = r.choice([2, 3, 4]); c = r.choice([1, 2, 3, 5]); b = r.choice([1, 3, 5, -2]); d = r.choice([1, 2, -3, 4])
    good = F(a, c)
    n = 10 ** 7; assert abs(math.sqrt(a * a * n * n + b * n) / (c * n + d) - float(good)) < 1e-5
    return dict(en='\\(\\lim\\dfrac{\\sqrt{%dn^2%+dn}}{%s}=\\)…' % (a * a, b, ('%dn' % c if c != 1 else 'n') + '%+d' % d), vi='\\(\\lim\\dfrac{\\sqrt{%dn^2%+dn}}{%s}=\\)…' % (a * a, b, ('%dn' % c if c != 1 else 'n') + '%+d' % d),
                opts=fo(good, [F(a * a, c), F(a, c * c), F(b, d), 0, good + 1]),
                ee='Divide by \\(n\\): \\(\\dfrac{\\sqrt{%d+\\frac{%d}{n}}}{%d+\\frac{%d}{n}}\\to\\dfrac{%d}{%d}=%s\\).' % (a * a, b, c, d, a, c, frt(good)),
                ev='Chia tử và mẫu cho \\(n\\): \\(\\dfrac{\\sqrt{%d+\\frac{%d}{n}}}{%d+\\frac{%d}{n}}\\to\\dfrac{%d}{%d}=%s\\).' % (a * a, b, c, d, a, c, frt(good)))

def b15_inf(r, lv, ctx):
    a = r.choice([-3, -2, -1, 1, 2, 3]); b = r.choice([2, 4, 5, -5]); c = r.choice([1, 3, -7])
    kind = r.choice(['poly', 'rat'])
    if kind == 'poly':
        t = '%sn^3%+dn^2%+d' % ({1: '', -1: '-'}.get(a, str(a)), b, c); f = lambda n: a * n ** 3 + b * n ** 2 + c
    else:
        e = r.choice([1, 2, 3]); t = '\\dfrac{%sn^3%+dn}{%dn^2%+d}' % ({1: '', -1: '-'}.get(a, str(a)), b, e, c); f = lambda n: F(a * n ** 3 + b * n, e * n * n + c)
    good = '+\\infty' if a > 0 else '-\\infty'; assert (f(10 ** 6) > 10 ** 5) == (a > 0) and abs(f(10 ** 6)) > 10 ** 5
    return dict(en='\\(\\lim\\left(%s\\right)=\\)…' % t if kind == 'poly' else '\\(\\lim%s=\\)…' % t, vi='\\(\\lim\\left(%s\\right)=\\)…' % t if kind == 'poly' else '\\(\\lim%s=\\)…' % t,
                opts=[good, '-\\infty' if a > 0 else '+\\infty', str(a), '0'],
                ee='The leading term \\(%sn^3\\) (or \\(\\dfrac{%s}{%s}n\\)) decides the limit: \\(%s\\).' % (a, a, 'e' if kind == 'rat' else '1', good) if False else 'Factor out the highest power of \\(n\\); the sign of the leading coefficient \\(%d\\) gives \\(%s\\).' % (a, good),
                ev='Đặt lũy thừa bậc cao nhất của \\(n\\) làm nhân tử chung; dấu của hệ số \\(%d\\) cho kết quả \\(%s\\).' % (a, good))

def b15_fig(r, lv, ctx):
    for _ in range(100):
        p = r.choice([1, 2, 3, -1]); q = r.choice([-3, -2, 1, 4, 5, 6]); c = r.choice([1, 2])
        if q != p * c and q != p and q != 2 * p and p != 0: break
    f = lambda n: F(p * n + q, n + c)
    vals = [f(n) for n in range(1, 13)]
    lo, hi = min([float(v) for v in vals] + [p, 0]) - 0.8, max([float(v) for v in vals] + [p, 0]) + 0.8
    img = G.graph_svg([], (-0.4, 12.8), (lo, hi), G.int_ticks(2, 12, 2), G.int_ticks(math.ceil(lo), math.floor(hi), 1), hlines=[(p, None)],
                      dots=[(n, float(v), False) for n, v in zip(range(1, 13), vals)], names=('n', 'u_n'), W=7.5, H=4.0)
    tf = lambda a, b_, cc: '\\dfrac{%s%+d}{%s%+d}' % ({1: 'n', -1: '-n'}.get(a, '%dn' % a), b_, 'n' if cc == 1 else '%dn' % cc, c)
    good = 'u_n=' + tf(p, q, 1)
    bad = ['u_n=\\dfrac{%s%+d}{n%+d}' % ({1: 'n', -1: '-n'}.get(q, '%dn' % q), p, c), 'u_n=' + tf(p, q, 2), 'u_n=\\dfrac{%s%+d}{n^2%+d}' % ({1: 'n', -1: '-n'}.get(p, '%dn' % p), q, c)]
    st = V(lv, [('The figure shows the points \\((n;\\,u_n)\\) of a sequence; the points get closer and closer to the dashed line. Which formula can be \\(u_n\\)?', 'Hình vẽ biểu diễn các điểm \\((n;\\,u_n)\\) của một dãy số; các điểm ngày càng gần đường nét đứt. Công thức nào có thể là \\(u_n\\)?'),
               ('As \\(n\\) grows, the points \\((n;\\,u_n)\\) in the figure approach the dashed line. Which sequence can it be?', 'Khi \\(n\\) tăng, các điểm \\((n;\\,u_n)\\) trong hình tiến dần tới đường nét đứt. Đó có thể là dãy số nào?'),
               ('The dashed line in the figure shows where the points \\((n;\\,u_n)\\) are heading. Choose a possible formula for \\(u_n\\).', 'Đường nét đứt trong hình cho biết các điểm \\((n;\\,u_n)\\) tiến dần tới đâu. Chọn một công thức có thể của \\(u_n\\).')])
    return dict(en=st[0], vi=st[1],
                opts=distinct4([good] + bad), fig=G.FIG(img, 'Points of a sequence and a dashed line', 'Các điểm của dãy số và đường nét đứt', 400),
                ee='The dashed line is \\(y=%d\\), so \\(\\lim u_n=%d\\). The other formulas have limits \\(%d\\), \\(%s\\) and \\(0\\).' % (p, p, q, frt(F(p, 2))),
                ev='Đường nét đứt là \\(y=%d\\) nên \\(\\lim u_n=%d\\). Các công thức còn lại có giới hạn \\(%d\\), \\(%s\\) và \\(0\\).' % (p, p, q, frt(F(p, 2))))

def b15_squeeze(r, lv, ctx):
    a = r.choice([1, 2, 3, 5]); b = r.choice([1, 2, 4])
    forms = [('\\dfrac{\\sin n}{n}', F(0)), ('\\dfrac{(-1)^n}{n+%d}' % b, F(0)), ('\\dfrac{%dn+\\cos n}{%dn}' % (a, b), F(a, b)), ('\\dfrac{%dn+(-1)^n}{%dn+1}' % (a, b), F(a, b))]
    t, good = r.choice(forms)
    return dict(en='\\(\\lim%s=\\)…' % t, vi='\\(\\lim%s=\\)…' % t, opts=fo(good, [1, F(a + 1, b), '+\\infty', 0, F(a, b + 1), 2]),
                ee='\\(|\\sin n|,\\ |\\cos n|,\\ |(-1)^n|\\le1\\), so these terms divided by \\(n\\) tend to \\(0\\); the limit is \\(%s\\).' % frt(good),
                ev='\\(|\\sin n|,\\ |\\cos n|,\\ |(-1)^n|\\le1\\) nên khi chia cho \\(n\\) chúng dần tới \\(0\\); giới hạn bằng \\(%s\\).' % frt(good))

def b15_rec(r, lv, ctx):
    typ = r.choice([0, 1, 2])
    if typ == 0:
        c = r.choice([1, 2, 3, 5]); t = 'u_{n+1}=\\dfrac{u_n}{2}+%d' % c; good = 2 * c; bad = [c, F(c, 2), 3 * c]; g = lambda u: u / 2 + c
    elif typ == 1:
        k = r.choice([2, 4, 6, 8]); t = 'u_{n+1}=\\dfrac{u_n+%d}{3}' % k; good = F(k, 2); bad = [k, F(k, 3), 2 * k]; g = lambda u: (u + k) / 3
    else:
        m = r.choice([2, 3, 4, 5]); t = 'u_{n+1}=\\sqrt{u_n+%d}' % (m * (m - 1)); good = m; bad = [-(m - 1), m - 1, m * (m - 1)]; g = lambda u: math.sqrt(u + m * (m - 1))
    u = 1.0
    for _ in range(200): u = g(u)
    assert abs(u - float(good)) < 1e-9
    return dict(en='The sequence \\(u_1=1\\), \\(%s\\) has a finite limit \\(L\\). Find \\(L\\).' % t, vi='Dãy số \\(u_1=1\\), \\(%s\\) có giới hạn hữu hạn \\(L\\). Tìm \\(L\\).' % t, opts=nopts(r, good, bad),
                ee='Let \\(n\\to+\\infty\\) in the recurrence: \\(L\\) satisfies the same equation; solving it (and keeping \\(L\\ge0\\)) gives \\(L=%s\\).' % ne(good),
                ev='Cho \\(n\\to+\\infty\\) trong hệ thức truy hồi: \\(L\\) thỏa mãn cùng phương trình; giải ra (và giữ \\(L\\ge0\\)) được \\(L=%s\\).' % nv(good))

D15 = [b15_sumform, b15_param, b15_findq, b15_root, b15_inf, b15_fig, b15_squeeze, b15_rec]

# =====================================================================================================
# BÀI 16. Giới hạn của hàm số
# =====================================================================================================
def b16_jump_fig(r, lv, ctx):
    for _ in range(200):
        x0 = r.choice([1, 2, 3, -1]); m1, m2 = r.choice([1, -1, 2, F(1, 2)]), r.choice([1, -1, -2, F(1, 2)])
        L1 = r.randint(-2, 3); L2 = r.randint(-2, 3)
        if L1 != L2 and abs(L1 - L2) >= 2: break
    f1 = lambda x: L1 + m1 * (x - x0); f2 = lambda x: L2 + m2 * (x - x0)
    xr = (x0 - 3.3, x0 + 3.3)
    ys = [float(f1(xr[0] + 0.01)), float(f2(xr[1] - 0.01)), L1, L2, 0]
    yr = (min(ys) - 0.8, max(ys) + 0.8)
    if yr[1] - yr[0] > 9: raise AssertionError
    img = G.graph_svg([(lambda x: float(f1(x)) if x < x0 else None, G.GREEN), (lambda x: float(f2(x)) if x >= x0 else None, G.GREEN)], xr, yr,
                      G.int_ticks(math.ceil(xr[0]), math.floor(xr[1])), G.int_ticks(math.ceil(yr[0]), math.floor(yr[1])), dots=[(x0, L1, True), (x0, L2, False)],
                      vlines=[(x0, None)] if False else [], W=6.5, H=4.6)
    side = r.choice(['-', '+'])
    good = L1 if side == '-' else L2; other = L2 if side == '-' else L1
    return dict(en='The figure shows the graph of \\(y=f(x)\\) (an open dot means the point is not on the graph). Find \\(\\lim\\limits_{x\\to%d^{%s}}f(x)\\).' % (x0, side),
                vi='Hình vẽ là đồ thị hàm số \\(y=f(x)\\) (chấm rỗng là điểm không thuộc đồ thị). Tìm \\(\\lim\\limits_{x\\to%d^{%s}}f(x)\\).' % (x0, side),
                opts=fo(good, [other, x0, 0, good + 1, good - 1]), fig=G.FIG(img, 'Graph with a jump', 'Đồ thị có bước nhảy', 330),
                ee='As \\(x\\) approaches \\(%d\\) from the %s, the graph approaches the height \\(%d\\).' % (x0, 'left' if side == '-' else 'right', good),
                ev='Khi \\(x\\) dần tới \\(%d\\) từ bên %s, đồ thị dần tới độ cao \\(%d\\).' % (x0, 'trái' if side == '-' else 'phải', good))

def b16_asym_fig(r, lv, ctx):
    for _ in range(100):
        a = r.choice([1, 2, -1]); c = r.choice([1, 2, -1]); b = r.choice([-3, -1, 1, 2, 3])
        if a * c + b != 0: break
    f = lambda x: (a * x + b) / (x - c)
    side = r.choice(['-', '+']); k = a * c + b
    good = '+\\infty' if (k > 0) == (side == '+') else '-\\infty'
    xs = [c + (1e-6 if side == '+' else -1e-6)]; assert (f(xs[0]) > 0) == (good == '+\\infty')
    img = G.graph_svg([(lambda x: f(x) if abs(x - c) > 0.12 else None, G.GREEN)], (c - 5, c + 5), (a - 6, a + 6), G.int_ticks(c - 4, c + 4, 2 if c % 2 == 0 else 1) if False else G.int_ticks(c - 4, c + 4),
                      G.int_ticks(a - 5, a + 5, 2), hlines=[(a, None)], vlines=[(c, None)], W=6.5, H=5)
    return dict(en='The figure shows the graph of \\(y=\\dfrac{%s%+d}{x%+d}\\) and its asymptotes (dashed). Find \\(\\lim\\limits_{x\\to%s^{%s}}y\\).' % (cx(a, 'x', True), b, -c, ('(%d)' % c) if c < 0 else c, side),
                vi='Hình vẽ là đồ thị hàm số \\(y=\\dfrac{%s%+d}{x%+d}\\) và các tiệm cận (nét đứt). Tìm \\(\\lim\\limits_{x\\to%s^{%s}}y\\).' % (cx(a, 'x', True), b, -c, ('(%d)' % c) if c < 0 else c, side),
                opts=[good, '-\\infty' if good == '+\\infty' else '+\\infty', str(a), str(c) if c != a else '0'],
                ee='Near \\(x=%d\\) the numerator tends to \\(%d\\) and the denominator to \\(0\\) with sign %s; the graph goes %s along the dashed line \\(x=%d\\).' % (c, k, '+' if side == '+' else '−', 'up' if good == '+\\infty' else 'down', c),
                ev='Gần \\(x=%d\\), tử dần tới \\(%d\\), mẫu dần tới \\(0\\) và mang dấu %s; đồ thị đi %s dọc theo đường nét đứt \\(x=%d\\).' % (c, k, '+' if side == '+' else '−', 'lên' if good == '+\\infty' else 'xuống', c))

def b16_sqrtinf(r, lv, ctx):
    a = r.choice([2, 4, 6, -2, -4, 3, 5]); b = r.choice([1, 3, -5, 7])
    good = F(a, 2); x = 1e7; assert abs(math.sqrt(x * x + a * x + b) - x - float(good)) < 1e-4
    return dict(en='\\(\\lim\\limits_{x\\to+\\infty}\\left(\\sqrt{x^2%s%+d}-x\\right)=\\)…' % (cx(a, 'x'), b), vi='\\(\\lim\\limits_{x\\to+\\infty}\\left(\\sqrt{x^2%s%+d}-x\\right)=\\)…' % (cx(a, 'x'), b),
                opts=fo(good, [a, 0, '+\\infty', -good, F(b, 2)]), ee='Multiply by the conjugate: \\(\\dfrac{%sx%+d}{\\sqrt{x^2%s%+d}+x}\\to\\dfrac{%d}{2}=%s\\).' % (a, b, cx(a, 'x'), b, a, frt(good)),
                ev='Nhân liên hợp: \\(\\dfrac{%dx%+d}{\\sqrt{x^2%s%+d}+x}\\to\\dfrac{%d}{2}=%s\\).' % (a, b, cx(a, 'x'), b, a, frt(good)))

def b16_neginf(r, lv, ctx):
    a = r.choice([2, 3, 4, 5]); c = r.choice([1, 2, 3]); b = r.choice([1, 3, 7]); d = r.choice([1, -2, 5])
    good = F(-a, c); x = -1e7; assert abs(math.sqrt(a * a * x * x + b) / (c * x + d) - float(good)) < 1e-5
    return dict(en='\\(\\lim\\limits_{x\\to-\\infty}\\dfrac{\\sqrt{%dx^2+%d}}{%s%+d}=\\)…' % (a * a, b, cx(c, 'x', True), d), vi='\\(\\lim\\limits_{x\\to-\\infty}\\dfrac{\\sqrt{%dx^2+%d}}{%s%+d}=\\)…' % (a * a, b, cx(c, 'x', True), d),
                opts=fo(good, [-good, F(a * a, c), F(-a * a, c), 0]), ee='For \\(x\\lt0\\), \\(\\sqrt{x^2}=|x|=-x\\): the limit is \\(\\dfrac{-%d}{%d}=%s\\).' % (a, c, frt(good)),
                ev='Với \\(x\\lt0\\), \\(\\sqrt{x^2}=|x|=-x\\): giới hạn bằng \\(\\dfrac{-%d}{%d}=%s\\).' % (a, c, frt(good)))

def b16_param(r, lv, ctx):
    x0 = r.choice([1, 2, -1, 3]); L = r.choice([1, 2, 3, 5, -1, -3])
    a = L - 2 * x0; b = -x0 * x0 - a * x0
    f = lambda x: (x * x + a * x + b) / (x - x0); assert abs(f(x0 + 1e-7) - L) < 1e-5
    ask = r.choice(['s', 'p']); good = a + b if ask == 's' else a * b
    return dict(en='Given \\(\\lim\\limits_{x\\to%s}\\dfrac{x^2+ax+b}{x%+d}=%d\\). Find \\(%s\\).' % (('(%d)' % x0) if x0 < 0 else x0, -x0, L, 'a+b' if ask == 's' else 'ab'),
                vi='Biết \\(\\lim\\limits_{x\\to%s}\\dfrac{x^2+ax+b}{x%+d}=%d\\). Tính \\(%s\\).' % (('(%d)' % x0) if x0 < 0 else x0, -x0, L, 'a+b' if ask == 's' else 'ab'),
                opts=nopts(r, good, [a - b, -(a + b), a, b, good + 2]),
                ee='The numerator must vanish at \\(x=%d\\) and \\(x^2+ax+b=(x%+d)(x%+d)\\); then the limit is \\(%d%+d=%d\\). So \\(a=%d\\), \\(b=%d\\).' % (x0, -x0, a + x0, x0, a + x0, L, a, b),
                ev='Tử phải bằng 0 tại \\(x=%d\\) và \\(x^2+ax+b=(x%+d)(x%+d)\\); khi đó giới hạn bằng \\(%d%+d=%d\\). Vậy \\(a=%d\\), \\(b=%d\\).' % (x0, -x0, a + x0, x0, a + x0, L, a, b))

def b16_polyinf(r, lv, ctx):
    a = r.choice([-3, -2, -1, 1, 2]); deg = r.choice([3, 4]); toward = r.choice(['+', '-'])
    b = r.choice([2, -5, 7]); c = r.choice([1, -4])
    t = '%sx^%d%sx^2%+d' % ({1: '', -1: '-'}.get(a, str(a)), deg, cx(b, '', False) if False else ('%+d' % b), c)
    f = lambda x: a * x ** deg + b * x * x + c
    big = f(1e5 if toward == '+' else -1e5); good = '+\\infty' if big > 0 else '-\\infty'
    return dict(en='\\(\\lim\\limits_{x\\to%s\\infty}\\left(%s\\right)=\\)…' % (toward, t), vi='\\(\\lim\\limits_{x\\to%s\\infty}\\left(%s\\right)=\\)…' % (toward, t),
                opts=[good, '-\\infty' if good == '+\\infty' else '+\\infty', str(a), '0'],
                ee='\\(%s=x^%d\\left(%d+\\dfrac{%d}{x^%d}+\\dfrac{%d}{x^%d}\\right)\\); \\(x^%d\\to%s\\infty\\) and the bracket tends to \\(%d\\), so the limit is \\(%s\\).' % (t, deg, a, b, deg - 2, c, deg, deg, '+' if toward == '+' or deg % 2 == 0 else '-', a, good),
                ev='\\(%s=x^%d\\left(%d+\\dfrac{%d}{x^%d}+\\dfrac{%d}{x^%d}\\right)\\); \\(x^%d\\to%s\\infty\\) và biểu thức trong ngoặc dần tới \\(%d\\) nên giới hạn là \\(%s\\).' % (t, deg, a, b, deg - 2, c, deg, deg, '+' if toward == '+' or deg % 2 == 0 else '-', a, good))

def vtab(xs, ys, lang):
    N = ne if lang == 'en' else nv
    row = lambda L, vs: '<tr><th scope="row">%s</th>%s</tr>' % (L, ''.join('<td>\\(%s\\)</td>' % N(v) for v in vs))
    return '<div class="mbl-tablewrap mbl-freqwrap"><table class="mbl-table mbl-freq"><tbody>%s%s</tbody></table></div>' % (row('\\(x\\)', xs), row('\\(f(x)\\)', ys))
def b16_table(r, lv, ctx):
    x0 = r.choice([1, 2, 3, -1]); k = r.choice([1, 2, 3, -2]); c = r.choice([2, 3, -1])
    # f(x) = (x - x0)(kx + c)/(x - x0) = kx + c (x ≠ x0)
    hs = [F(-1, 10), F(-1, 100), F(-1, 1000), F(1, 1000), F(1, 100), F(1, 10)]
    xs = [x0 + h for h in hs]; ys = [k * x + c for x in xs]; good = k * x0 + c
    for x, y in zip(xs, ys): assert ((x - x0) * (k * x + c)) / (x - x0) == y
    fig = (vtab(xs, ys, 'en'), vtab(xs, ys, 'vi'))
    return dict(en='The table gives some values of a function \\(f(x)\\) near \\(x=%d\\) (\\(f\\) is not defined at \\(%d\\)). Which is most likely \\(\\lim\\limits_{x\\to%s}f(x)\\)?' % (x0, x0, ('(%d)' % x0) if x0 < 0 else x0),
                vi='Bảng cho một số giá trị của hàm số \\(f(x)\\) gần \\(x=%d\\) (\\(f\\) không xác định tại \\(%d\\)). Giới hạn \\(\\lim\\limits_{x\\to%s}f(x)\\) có khả năng bằng bao nhiêu nhất?' % (x0, x0, ('(%d)' % x0) if x0 < 0 else x0),
                opts=nopts(r, good, [x0, 0, good + k * F(1, 10), good + 1]), fig=fig,
                ee='From both sides, \\(f(x)\\) gets closer and closer to \\(%d\\).' % good, ev='Từ cả hai phía, \\(f(x)\\) ngày càng gần \\(%d\\).' % good)

def b16_abs(r, lv, ctx):
    a = r.choice([2, 3, 4, 5, -2, -3]); side = r.choice(['-', '+'])
    good = a if side == '+' else -a
    f = lambda x: (x * x - a * x) / abs(x - a); x = a + (1e-7 if side == '+' else -1e-7); assert abs(f(x) - good) < 1e-5
    pa = ('(%d)' % a) if a < 0 else str(a)
    return dict(en='\\(\\lim\\limits_{x\\to%s^{%s}}\\dfrac{x^2%sx}{|x%+d|}=\\)…' % (pa, side, cx(-a, ''), -a), vi='\\(\\lim\\limits_{x\\to%s^{%s}}\\dfrac{x^2%sx}{|x%+d|}=\\)…' % (pa, side, cx(-a, ''), -a),
                opts=nopts(r, good, [-good, 0, 1, 2 * good]),
                ee='\\(x^2%sx=x(x%+d)\\). For \\(x\\to%s^{%s}\\), \\(|x%+d|=%s(x%+d)\\), so the quotient is \\(%sx\\to%d\\).' % (cx(-a, ''), -a, pa, side, -a, '' if side == '+' else '-', -a, '' if side == '+' else '-', good),
                ev='\\(x^2%sx=x(x%+d)\\). Khi \\(x\\to%s^{%s}\\), \\(|x%+d|=%s(x%+d)\\) nên thương bằng \\(%sx\\to%d\\).' % (cx(-a, ''), -a, pa, side, -a, '' if side == '+' else '-', -a, '' if side == '+' else '-', good))

D16 = [b16_jump_fig, b16_asym_fig, b16_sqrtinf, b16_neginf, b16_param, b16_polyinf, b16_table, b16_abs]

# =====================================================================================================
# BÀI 19. Lôgarit
# =====================================================================================================
def b19_chain(r, lv, ctx):
    a, b = r.sample([2, 3, 5, 7], 2); k = r.choice([2, 3, 4, 5]); c = a ** k
    if c > 700: raise AssertionError
    good = k; assert abs(math.log(b, a) * math.log(c, b) - k) < 1e-9
    return dict(en='\\(\\log_{%d}%d\\cdot\\log_{%d}%d=\\)…' % (a, b, b, c), vi='\\(\\log_{%d}%d\\cdot\\log_{%d}%d=\\)…' % (a, b, b, c),
                opts=nopts(r, good, [k + 1, k - 1, b, F(1, k)]), ee='\\(\\log_ab\\cdot\\log_bc=\\log_ac\\): \\(\\log_{%d}%d=%d\\).' % (a, c, k), ev='\\(\\log_ab\\cdot\\log_bc=\\log_ac\\): \\(\\log_{%d}%d=%d\\).' % (a, c, k))

def b19_sign(r, lv, ctx):
    def item(pos):
        base = r.choice([2, 3, 5, F(1, 2), F(1, 3), F(2, 3)]); big = r.choice([True, False])
        x = r.choice([3, 5, 7, F(3, 2)]) if big else r.choice([F(1, 2), F(2, 5), F(3, 4)])
        v = math.log(float(x)) / math.log(float(base))
        bt = frt(base).replace('\\dfrac', '\\frac'); xt = ne(x)
        return '\\log_{%s}%s' % (bt, xt) if '.' not in xt else '\\log_{%s}%s' % (bt, frt(x)), v
    for _ in range(200):
        items = [item(None) for _ in range(12)]
        pos = [t for t, v in items if v > 1e-9]; neg = [t for t, v in items if v < -1e-9]
        neg = list(dict.fromkeys(neg))
        if pos and len(neg) >= 3: break
    else: raise AssertionError
    good = pos[0]
    st = V(lv, [('Which number is positive?', 'Số nào dương?'), ('Which logarithm is greater than 0?', 'Lôgarit nào lớn hơn 0?'), ('Choose the positive number.', 'Chọn số dương.')])
    return dict(en=st[0], vi=st[1], opts=distinct4([good] + neg[:3]),
                ee='\\(\\log_ax\\gt0\\) when \\(a\\) and \\(x\\) are both greater than 1 or both less than 1; only \\(%s\\) is positive.' % good,
                ev='\\(\\log_ax\\gt0\\) khi \\(a\\), \\(x\\) cùng lớn hơn 1 hoặc cùng nhỏ hơn 1; chỉ có \\(%s\\) dương.' % good)

def b19_domain(r, lv, ctx):
    p = r.choice([-2, -1, 0, 1, 2]); q = p + r.choice([3, 4, 5, 6])
    base = 'x' if p == 0 else 'x%+d' % (-p)
    good = '%d\\lt x\\lt %d,\\ x\\ne %d' % (p, q, p + 1); bad = ['%d\\lt x\\lt %d' % (p, q), 'x\\gt %d,\\ x\\ne %d' % (p, p + 1), 'x\\lt %d,\\ x\\ne %d' % (q, p + 1)]
    for x in [p + F(k, 4) for k in range(-8, 4 * (q - p) + 9)]:
        ok = (x - p > 0) and (x - p != 1) and (q - x > 0)
        assert ok == (p < x < q and x != p + 1)
    return dict(en='The expression \\(\\log_{%s}(%d-x)\\) is defined when…' % (base, q), vi='Biểu thức \\(\\log_{%s}(%d-x)\\) có nghĩa khi…' % (base, q), opts=distinct4([good] + bad),
                ee='Need \\(%s\\gt0\\), \\(%s\\ne1\\) and \\(%d-x\\gt0\\): \\(%s\\).' % (base, base, q, good), ev='Cần \\(%s\\gt0\\), \\(%s\\ne1\\) và \\(%d-x\\gt0\\): \\(%s\\).' % (base, base, q, good))

def b19_double(r, lv, ctx):
    rate = r.choice([5, 6, 7, 8, 9, 10, 12]); mult = r.choice([2, 2, 3])
    n = 1
    while (1 + rate / 100) ** n < mult: n += 1
    assert abs((1 + rate / 100) ** n - mult) > 1e-6 and abs((1 + rate / 100) ** (n - 1) - mult) > 1e-6
    L = math.log(mult) / math.log(1 + rate / 100)
    w = {2: ('double', 'gấp đôi'), 3: ('triple', 'gấp ba')}[mult]
    return dict(en='Money is saved at \\(%d\\%%\\) per year, compounded yearly. After how many whole years does it first at least %s?' % (rate, w[0]),
                vi='Gửi tiết kiệm với lãi suất \\(%d\\%%\\)/năm, lãi nhập gốc hằng năm. Sau ít nhất bao nhiêu năm thì số tiền đạt ít nhất %s số tiền ban đầu?' % (rate, w[1]),
                opts=nopts(r, n, [n - 1, n + 1, n + 2, round(100 / rate)]),
                ee='\\(%s^n\\ge%d\\iff n\\ge\\log_{%s}%d\\approx%s\\), so \\(n=%d\\).' % (ne(1 + F(rate, 100)), mult, ne(1 + F(rate, 100)), mult, ('%.2f' % L), n),
                ev='\\(%s^n\\ge%d\\iff n\\ge\\log_{%s}%d\\approx%s\\) nên \\(n=%d\\).' % (nv(1 + F(rate, 100)), mult, nv(1 + F(rate, 100)), mult, ('%.2f' % L).replace('.', '{,}'), n))

LOGT = {2: F('0.3010'), 3: F('0.4771'), 5: F('0.6990'), 7: F('0.8451')}
def ltab(lang):
    N = ne if lang == 'en' else nv
    return ('<div class="mbl-tablewrap mbl-freqwrap"><table class="mbl-table mbl-freq"><tbody><tr><th scope="row">\\(x\\)</th>%s</tr><tr><th scope="row">\\(\\log x\\)</th>%s</tr></tbody></table></div>'
            % (''.join('<td>\\(%d\\)</td>' % k for k in LOGT), ''.join('<td>\\(\\approx%s\\)</td>' % ('%.4f' % float(v) if lang == 'en' else ('%.4f' % float(v)).replace('.', '{,}')) for v in LOGT.values())))
def b19_table(r, lv, ctx):
    for _ in range(200):
        e = {p: r.choice([0, 0, 1, 2]) for p in LOGT}; d = r.choice([0, 0, 1])
        if sum(e.values()) < 2: continue
        N = F(1)
        for p, k in e.items(): N *= p ** k
        N /= 10 ** d
        if N.denominator == 1 and 10 < N < 1000 or (N.denominator > 1 and N > F(1, 10)): break
    good = sum(k * LOGT[p] for p, k in e.items()) - d
    assert abs(float(good) - math.log10(float(N))) < 0.002
    alts = [good + 1, good - LOGT[2], good + LOGT[3] - LOGT[2], 1 - good]
    nt = ne(N) if N.denominator == 1 or '.' in ne(N) else frt(N); ntv = nv(N) if N.denominator == 1 or '.' in ne(N) else frt(N)
    pr = ' + '.join('%d\\log %d' % (k, p) if k > 1 else '\\log %d' % p for p, k in e.items() if k) + (' - 1' if d else '')
    return dict(en='Using the table, \\(\\log %s\\approx\\)…' % nt, vi='Dùng bảng giá trị, \\(\\log %s\\approx\\)…' % ntv,
                opts=nopts(r, good, alts, step=F(1, 10)), fig=(ltab('en'), ltab('vi')),
                ee='\\(\\log %s=%s\\approx%s\\).' % (nt, pr, ne(good)), ev='\\(\\log %s=%s\\approx%s\\).' % (ntv, pr, nv(good)))

def b19_pow(r, lv, ctx):
    a = r.choice([2, 3, 5]); k = r.choice([2, 3]); b = r.choice([3, 5, 6, 7] if a != 5 else [2, 3, 4, 6])
    if a ** k > 30 or b == a: raise AssertionError
    good = b ** k; assert abs((a ** k) ** math.log(b, a) - good) < 1e-6
    return dict(en='\\(%d^{\\log_{%d}%d}=\\)…' % (a ** k, a, b), vi='\\(%d^{\\log_{%d}%d}=\\)…' % (a ** k, a, b), opts=nopts(r, good, [b, k * b, b ** (k + 1), a * b]),
                ee='\\(%d^{\\log_{%d}%d}=\\left(%d^{\\log_{%d}%d}\\right)^{%d}=%d^{%d}=%d\\).' % (a ** k, a, b, a, a, b, k, b, k, good),
                ev='\\(%d^{\\log_{%d}%d}=\\left(%d^{\\log_{%d}%d}\\right)^{%d}=%d^{%d}=%d\\).' % (a ** k, a, b, a, a, b, k, b, k, good))

def b19_digits(r, lv, ctx):
    a = r.choice([2, 3, 7]); n = r.randrange(20, 90)
    L = n * math.log10(a); frac = L - math.floor(L)
    if frac < 0.02 or frac > 0.98: raise AssertionError
    good = math.floor(L) + 1; assert len(str(a ** n)) == good
    lt = {2: '0.3010', 3: '0.4771', 7: '0.8451'}[a]
    return dict(en='Given \\(\\log %d\\approx%s\\). How many digits does \\(%d^{%d}\\) have?' % (a, lt, a, n), vi='Biết \\(\\log %d\\approx%s\\). Số \\(%d^{%d}\\) có bao nhiêu chữ số?' % (a, lt.replace('.', '{,}'), a, n),
                opts=nopts(r, good, [good - 1, good + 1, n]), ee='\\(\\log %d^{%d}=%d\\log %d\\approx%s\\); the number of digits is \\(\\lfloor %s\\rfloor+1=%d\\).' % (a, n, n, a, '%.2f' % L, '%.2f' % L, good),
                ev='\\(\\log %d^{%d}=%d\\log %d\\approx%s\\); số chữ số là \\(\\lfloor %s\\rfloor+1=%d\\).' % (a, n, n, a, ('%.2f' % L).replace('.', '{,}'), ('%.2f' % L).replace('.', '{,}'), good))

def b19_ph(r, lv, ctx):
    m = r.choice([2, 3, 5]); e = r.choice([3, 4, 5, 6, 8])
    ph = e - math.log10(m); good = F(round(ph * 10), 10)
    lt = {2: '0.3010', 3: '0.4771', 5: '0.6990'}[m]
    alts = [F(round((e + math.log10(m)) * 10), 10), F(round((e - 1 + math.log10(m)) * 10), 10), F(e), F(round((ph - 1) * 10), 10)]
    return dict(en='\\(\\text{pH}=-\\log[\\text{H}^+]\\). A solution has \\([\\text{H}^+]=%d\\cdot10^{-%d}\\) mol/l. Given \\(\\log %d\\approx%s\\), its pH (to one decimal place) is…' % (m, e, m, lt),
                vi='\\(\\text{pH}=-\\log[\\text{H}^+]\\). Một dung dịch có \\([\\text{H}^+]=%d\\cdot10^{-%d}\\) mol/l. Biết \\(\\log %d\\approx%s\\), độ pH của dung dịch (làm tròn đến hàng phần mười) là…' % (m, e, m, lt.replace('.', '{,}')),
                opts=nopts(r, good, alts, step=F(1, 10)),
                ee='\\(\\text{pH}=-(\\log %d-%d)=%d-\\log %d\\approx%s\\).' % (m, e, e, m, ne(good)), ev='\\(\\text{pH}=-(\\log %d-%d)=%d-\\log %d\\approx%s\\).' % (m, e, e, m, nv(good)))

D19 = [b19_chain, b19_sign, b19_domain, b19_double, b19_table, b19_pow, b19_digits, b19_ph]

# =====================================================================================================
# BÀI 8. Mẫu số liệu ghép nhóm (viết lại toàn bộ: A3, B2, C2, D8 – mỗi mức 15 câu, 15 dạng)
# =====================================================================================================
import gq
from gq import mkt
from sp_g11r import gtab, TB, grp as _grp
NS = (20, 25, 40, 50)
def gl(sc, lang): return lab(sc['gl'])[0 if lang == 'en' else 1]
def fl(sc, lang): return lab(sc['fl'])[0 if lang == 'en' else 1]
def ltx(sc, x, lang): return sc['lt'][0 if lang == 'en' else 1].format(x=x)
def gtx(sc, x, lang): return sc['ge'][0 if lang == 'en' else 1].format(x=x)
def G8(t, i, lang='en'): return _grp(t, i, ne if lang == 'en' else nv)
def reltab(sc, t, lang, unknown):
    N = ne if lang == 'en' else nv
    cells = ['\\([%s;\\,%s)\\)' % (N(t.edge(i)), N(t.edge(i + 1))) for i in range(t.k)]
    rel = ['\\(x\\)' if i == unknown else '\\(%s\\%%\\)' % N(F(100 * t.fs[i], t.n)) for i in range(t.k)]
    L2 = 'Relative frequency' if lang == 'en' else 'Tần số tương đối'
    rows = '<tr><th scope="row">%s</th>%s<td class="mbl-freq-tot">%s</td></tr>' % (gl(sc, lang), ''.join('<td>%s</td>' % c for c in cells), 'Total' if lang == 'en' else 'Cộng')
    rows += '<tr><th scope="row">%s</th>%s<td class="mbl-freq-tot">\\(100\\%%\\)</td></tr>' % (L2, ''.join('<td>%s</td>' % c for c in rel))
    return '<div class="mbl-tablewrap mbl-freqwrap"><table class="mbl-table mbl-freq"><tbody>%s</tbody></table></div>' % rows

def s8_count_lt(r, lv, ctx):
    sc = take(ctx); t = mkt(r, sc); j = r.randint(1, t.k - 1); x = t.edge(j); good = t.cum(j)
    return dict(en='%s How many %s %s?' % (sc['intro'][0], sc['ent'][0], ltx(sc, ne(x), 'en')), vi='%s Có bao nhiêu %s %s?' % (sc['intro'][1], sc['ent'][1], ltx(sc, nv(x), 'vi')),
                opts=nopts(r, good, [good + t.fs[j], good - t.fs[j - 1], t.fs[j - 1], t.n - good]), fig=TB(sc, t),
                ee='Add the frequencies of the groups before %s: \\(%s=%d\\).' % (ne(x), '+'.join(str(f) for f in t.fs[:j]), good), ev='Cộng tần số các nhóm đứng trước mốc %s: \\(%s=%d\\).' % (nv(x), '+'.join(str(f) for f in t.fs[:j]), good))

def s8_modal(r, lv, ctx):
    sc = take(ctx); t = mkt(r, sc, need=('mode',)); g = t.mode_group()
    others = [i for i in range(t.k) if i != g]; r.shuffle(others)
    return dict(en='%s Which group has the highest frequency?' % sc['intro'][0], vi='%s Nhóm nào có tần số lớn nhất?' % sc['intro'][1], fig=TB(sc, t),
                opts=[tx(G8(t, i), G8(t, i, 'vi')) for i in [g] + others[:3]],
                ee='The largest frequency is \\(%d\\), in the group %s.' % (t.fs[g], G8(t, g)), ev='Tần số lớn nhất là \\(%d\\), ở nhóm %s.' % (t.fs[g], G8(t, g, 'vi')))

def s8_mid(r, lv, ctx):
    sc = take(ctx); t = mkt(r, sc); i = r.randrange(t.k); m = t.mid(i)
    return dict(en='%s What is the midpoint (representative value) of the group %s?' % (sc['intro'][0], G8(t, i)), vi='%s Giá trị đại diện của nhóm %s là bao nhiêu?' % (sc['intro'][1], G8(t, i, 'vi')),
                opts=nopts(r, m, [t.edge(i), t.edge(i + 1), F(t.h, 2), m + t.h]), fig=TB(sc, t),
                ee='\\(x=\\dfrac{%s+%s}{2}=%s\\).' % (ne(t.edge(i)), ne(t.edge(i + 1)), ne(m)), ev='\\(x=\\dfrac{%s+%s}{2}=%s\\).' % (nv(t.edge(i)), nv(t.edge(i + 1)), nv(m)))

def s8_tf_edge(r, lv, ctx):
    sc = take(ctx); t = mkt(r, sc); j = r.randint(1, t.k - 1); x = t.edge(j); good = r.random() < .5; gi = j if good else j - 1
    return dict(en='%s A %s with a %s of exactly %s %s is counted in the group %s.' % (sc['intro'][0], sc['ent1'][0], sc['var'][0], ne(x), sc['unit'], G8(t, gi)),
                vi='%s Một %s có %s đúng bằng %s %s được xếp vào nhóm %s.' % (sc['intro'][1], sc['ent1'][1], sc['var'][1], nv(x), sc['uv'], G8(t, gi, 'vi')), truth=good, fig=TB(sc, t),
                ee='In \\([a;\\,b)\\) the left end belongs to the group and the right end does not, so %s goes to %s.' % (ne(x), G8(t, j)),
                ev='Trong nhóm \\([a;\\,b)\\) đầu mút trái thuộc nhóm, đầu mút phải thì không; nên %s thuộc nhóm %s.' % (nv(x), G8(t, j, 'vi')))

def s8_tf_pct(r, lv, ctx):
    sc = take(ctx); t = mkt(r, sc, nset=NS); j = r.randint(1, t.k - 1); x = t.edge(j)
    p = F(100 * (t.n - t.cum(j)), t.n); q = F(100 * t.cum(j), t.n)
    good = r.random() < .5 or p == q; claim = p if good else q
    return dict(en='%s Exactly \\(%s\\%%\\) of the %s %s.' % (sc['intro'][0], ne(claim), sc['ent'][0], gtx(sc, ne(x), 'en')), vi='%s Có đúng \\(%s\\%%\\) số %s %s.' % (sc['intro'][1], nv(claim), sc['ent'][1], gtx(sc, nv(x), 'vi')),
                truth=good, fig=TB(sc, t), ee='\\(\\dfrac{%d}{%d}\\cdot100\\%%=%s\\%%\\).' % (t.n - t.cum(j), t.n, ne(p)), ev='\\(\\dfrac{%d}{%d}\\cdot100\\%%=%s\\%%\\).' % (t.n - t.cum(j), t.n, nv(p)))

def s8_sh_missing(r, lv, ctx):
    sc = take(ctx); t = mkt(r, sc); u = r.randrange(t.k)
    return dict(en='%s The total is \\(n=%d\\). Find the missing frequency \\(x\\).' % (sc['intro'][0], t.n), vi='%s Tổng số là \\(n=%d\\). Tìm tần số \\(x\\) còn thiếu.' % (sc['intro'][1], t.n),
                key=key(t.fs[u]), fig=TB(sc, t, unknown=u), ee='\\(x=%d-(%s)=%d\\).' % (t.n, '+'.join(str(f) for i, f in enumerate(t.fs) if i != u), t.fs[u]), ev='\\(x=%d-(%s)=%d\\).' % (t.n, '+'.join(str(f) for i, f in enumerate(t.fs) if i != u), t.fs[u]),
                hint=('Enter a whole number.', 'Nhập một số nguyên.'))

def s8_sh_pct(r, lv, ctx):
    sc = take(ctx); t = mkt(r, sc, nset=NS); j = r.randint(1, t.k - 1); x = t.edge(j); p = F(100 * t.cum(j), t.n)
    return dict(en='%s What percentage of the %s %s? (Enter the number without %%.)' % (sc['intro'][0], sc['ent'][0], ltx(sc, ne(x), 'en')), vi='%s Bao nhiêu phần trăm số %s %s? (Chỉ nhập số, không nhập dấu %%.)' % (sc['intro'][1], sc['ent'][1], ltx(sc, nv(x), 'vi')),
                key=key(p), fig=TB(sc, t), ee='\\(\\dfrac{%d}{%d}\\cdot100\\%%=%s\\%%\\).' % (t.cum(j), t.n, ne(p)), ev='\\(\\dfrac{%d}{%d}\\cdot100\\%%=%s\\%%\\).' % (t.cum(j), t.n, nv(p)))

def s8_raw(r, lv, ctx):
    sc = take(ctx)
    for _ in range(200):
        t = mkt(r, sc, kk=r.choice([3, 4])); k = t.k; fs = [r.randint(2, 4) for _ in range(k)]
        vals = [t.edge(g) + r.randrange(0, t.h) for g in range(k) for _q in range(fs[g])]
        i0 = r.randrange(1, k); vals[sum(fs[:i0])] = t.edge(i0)
        cnt = [sum(1 for v in vals if t.edge(g) <= v < t.edge(g + 1)) for g in range(k)]
        cntR = [sum(1 for v in vals if t.edge(g) < v <= t.edge(g + 1)) for g in range(k)]
        g = r.choice([i0 - 1, i0])
        if cnt[g] != cntR[g]: break
    else: raise AssertionError
    r.shuffle(vals); good = cnt[g]
    data = ';\\ '.join(map(str, vals)); groups = ',\\ '.join('[%d;\\,%d)' % (t.edge(i), t.edge(i + 1)) for i in range(k))
    return dict(en='The %s values (%s) of %d %s were recorded: \\(%s\\). The data are put into the groups \\(%s\\). What is the frequency of the group %s?' % (sc['var'][0], sc['unit'], len(vals), sc['ent'][0], data, groups, G8(t, g)),
                vi='Ghi lại %s (%s) của %d %s: \\(%s\\). Chia số liệu vào các nhóm \\(%s\\). Tần số của nhóm %s là bao nhiêu?' % (sc['var'][1], sc['uv'], len(vals), sc['ent'][1], data, groups, G8(t, g, 'vi')),
                opts=nopts(r, good, [cntR[g], good + 1, good - 1]), ee='Count the values \\(v\\) with \\(%d\\le v\\lt %d\\) (the value %d belongs to the group starting at %d): \\(%d\\).' % (t.edge(g), t.edge(g + 1), t.edge(i0), t.edge(i0), good),
                ev='Đếm các giá trị \\(v\\) với \\(%d\\le v\\lt %d\\) (giá trị %d thuộc nhóm bắt đầu từ %d): \\(%d\\).' % (t.edge(g), t.edge(g + 1), t.edge(i0), t.edge(i0), good))

def s8_ngroups(r, lv, ctx):
    sc = take(ctx); h = r.choice(sc['h']); a = r.choice(sc['u0']); lo = a + r.randrange(0, h); hi = lo + r.randint(3 * h, 6 * h) + r.randrange(1, h)
    k = (hi - a) // h + 1
    E = [a + i * h for i in range(k + 1)]; assert E[0] <= lo and E[-2] <= hi < E[-1]
    return dict(en='The smallest %s of some %s is %d %s and the largest is %d %s. The data are grouped as \\([%d;\\,%d),\\ [%d;\\,%d),\\dots\\) (all groups of width %d). How many groups are needed?' % (sc['var'][0], sc['ent'][0], lo, sc['unit'], hi, sc['unit'], a, a + h, a + h, a + 2 * h, h),
                vi='%s nhỏ nhất của một số %s là %d %s, lớn nhất là %d %s. Ghép nhóm số liệu thành \\([%d;\\,%d),\\ [%d;\\,%d),\\dots\\) (các nhóm cùng độ rộng %d). Cần bao nhiêu nhóm?' % (sc['var'][1][0].upper() + sc['var'][1][1:], sc['ent'][1], lo, sc['uv'], hi, sc['uv'], a, a + h, a + h, a + 2 * h, h),
                opts=nopts(r, k, [k - 1, k + 1, (hi - lo) // h]),
                ee='The groups start at %d; the last group must contain %d: \\([%d;\\,%d)\\). That is \\(%d\\) groups.' % (a, hi, E[-2], E[-1], k), ev='Các nhóm bắt đầu từ %d; nhóm cuối phải chứa %d: \\([%d;\\,%d)\\). Vậy cần \\(%d\\) nhóm.' % (a, hi, E[-2], E[-1], k))

def s8_relmiss(r, lv, ctx):
    sc = take(ctx); t = mkt(r, sc, nset=NS); u = r.randrange(t.k)
    p = F(100 * t.fs[u], t.n); good = t.fs[u]
    return dict(en='%s The table gives the relative frequencies of a sample of \\(%d\\) %s. How many %s are in the group %s?' % (sc['intro'][0], t.n, sc['ent'][0], sc['ent'][0], G8(t, u)),
                vi='%s Bảng cho tần số tương đối của một mẫu gồm \\(%d\\) %s. Nhóm %s có bao nhiêu %s?' % (sc['intro'][1], t.n, sc['ent'][1], G8(t, u, 'vi'), sc['ent'][1]),
                opts=nopts(r, good, [p, good + 1, 100 - sum(F(100 * f, t.n) for i, f in enumerate(t.fs) if i != u) + 1, t.n - good]),
                fig=(reltab(sc, t, 'en', u), reltab(sc, t, 'vi', u)),
                ee='\\(x=100\\%%-(\\text{other groups})=%s\\%%\\), so the frequency is \\(%s\\%%\\cdot%d=%d\\).' % (ne(p), ne(p), t.n, good),
                ev='\\(x=100\\%%-(\\text{các nhóm còn lại})=%s\\%%\\) nên tần số là \\(%s\\%%\\cdot%d=%d\\).' % (nv(p), nv(p), t.n, good))

def HIST(sc, t):
    e = [ne(t.edge(i)) for i in range(t.k + 1)]
    fe = G.hist_svg(e, t.fs, lab(sc['gl'])[0], lab(sc['fl'])[0]); fv = G.hist_svg(e, t.fs, lab(sc['gl'])[1], lab(sc['fl'])[1])
    return (G.img(fe, 'Histogram', 380), G.img(fv, 'Biểu đồ tần số', 380))
def s8_hist_n(r, lv, ctx):
    sc = take(ctx); t = mkt(r, sc)
    return dict(en='%s The histogram shows the grouped data. How many %s are there in total?' % (sc['intro'][0], sc['ent'][0]), vi='%s Biểu đồ tần số biểu diễn mẫu số liệu ghép nhóm. Có tất cả bao nhiêu %s?' % (sc['intro'][1], sc['ent'][1]),
                opts=nopts(r, t.n, [t.n - t.fs[0], t.n + t.fs[-1], max(t.fs) * t.k, t.k]), fig=HIST(sc, t),
                ee='Add the heights of all the bars: \\(%s=%d\\).' % ('+'.join(map(str, t.fs)), t.n), ev='Cộng chiều cao của tất cả các cột: \\(%s=%d\\).' % ('+'.join(map(str, t.fs)), t.n))

def s8_hist_rel(r, lv, ctx):
    sc = take(ctx); t = mkt(r, sc, nset=NS); i = r.randrange(t.k); p = F(100 * t.fs[i], t.n)
    return dict(en='%s Based on the histogram, the relative frequency of the group %s is…' % (sc['intro'][0], G8(t, i)), vi='%s Dựa vào biểu đồ tần số, tần số tương đối của nhóm %s là…' % (sc['intro'][1], G8(t, i, 'vi')),
                opts=[tx('\\(%s\\%%\\)' % ne(x), '\\(%s\\%%\\)' % nv(x)) for x in dict.fromkeys([p, F(t.fs[i]), F(100 * t.fs[i], t.n + t.fs[i]) if t.n else 1, p + 5, p + 10])][:4],
                fig=HIST(sc, t), ee='\\(\\dfrac{%d}{%d}\\cdot100\\%%=%s\\%%\\).' % (t.fs[i], t.n, ne(p)), ev='\\(\\dfrac{%d}{%d}\\cdot100\\%%=%s\\%%\\).' % (t.fs[i], t.n, nv(p)))

ERRS = {'overlap': ('The value %d belongs to two groups.', 'Giá trị %d thuộc hai nhóm.'), 'gap': ('Values between %d and %d belong to no group.', 'Các giá trị nằm giữa %d và %d không thuộc nhóm nào.'),
        'width': ('The groups do not all have the same width.', 'Các nhóm không cùng độ rộng.'), 'few': ('There are too few groups.', 'Số nhóm quá ít.')}
def s8_error(r, lv, ctx):
    sc = take(ctx); h = r.choice(sc['h']); a = r.choice(sc['u0']); typ = r.choice(['overlap', 'gap', 'width'])
    if typ == 'overlap': G_ = ['[%d;\\,%d]' % (a + i * h, a + (i + 1) * h) for i in range(4)]; v = (a + h,)
    elif typ == 'gap': G_ = ['[%d;\\,%d)' % (a + i * h, a + (i + 1) * h - 1) for i in range(4)]; v = (a + h - 1, a + h)
    else:
        w = [h, h, 2 * h, h]; e = [a]
        for x in w: e.append(e[-1] + x)
        G_ = ['[%d;\\,%d)' % (e[i], e[i + 1]) for i in range(4)]; v = ()
    def S(tp, lang):
        s = ERRS[tp][0 if lang == 'en' else 1]
        if tp == 'overlap': return s % (a + h)
        if tp == 'gap': return s % (a + h - 1, a + h)
        return s
    order = [typ] + [x for x in ERRS if x != typ]
    return dict(en='A student grouped the %s of some %s as \\(%s\\). What is wrong with this grouping?' % (sc['var'][0], sc['ent'][0], ',\\ '.join(G_)), vi='Một bạn ghép nhóm %s của một số %s thành \\(%s\\). Cách ghép nhóm này sai ở đâu?' % (sc['var'][1], sc['ent'][1], ',\\ '.join(G_)),
                opts=[tx(S(x, 'en'), S(x, 'vi')) for x in order],
                ee={'overlap': 'The closed groups share their ends, e.g. %d is in two groups.' % (a + h), 'gap': 'For example, a value of %s is in no group.' % ne(F(2 * (a + h) - 1, 2)), 'width': 'The third group is twice as wide as the others.'}[typ],
                ev={'overlap': 'Các nhóm đóng có chung đầu mút, chẳng hạn %d thuộc hai nhóm.' % (a + h), 'gap': 'Chẳng hạn giá trị %s không thuộc nhóm nào.' % nv(F(2 * (a + h) - 1, 2)), 'width': 'Nhóm thứ ba rộng gấp đôi các nhóm còn lại.'}[typ])

def s8_merge(r, lv, ctx):
    sc = take(ctx); t = mkt(r, sc, kk=4); j = r.choice([0, 1]); i = 2 * j; good = t.fs[i] + t.fs[i + 1]
    ng = '\\([%s;\\,%s)\\)'
    return dict(en='%s The data are grouped again with groups twice as wide, starting at %s. What is the frequency of the new group %s?' % (sc['intro'][0], ne(t.edge(0)), ng % (ne(t.edge(i)), ne(t.edge(i + 2)))),
                vi='%s Ghép nhóm lại với độ rộng gấp đôi, bắt đầu từ %s. Tần số của nhóm mới %s là bao nhiêu?' % (sc['intro'][1], nv(t.edge(0)), ng % (nv(t.edge(i)), nv(t.edge(i + 2)))),
                opts=nopts(r, good, [t.fs[i], t.fs[i + 1], good + t.fs[i + 2] if i + 2 < t.k else good + 2, t.fs[1] + t.fs[2]]), fig=TB(sc, t),
                ee='The new group joins %s and %s: \\(%d+%d=%d\\).' % (G8(t, i), G8(t, i + 1), t.fs[i], t.fs[i + 1], good), ev='Nhóm mới gộp %s và %s: \\(%d+%d=%d\\).' % (G8(t, i, 'vi'), G8(t, i + 1, 'vi'), t.fs[i], t.fs[i + 1], good))

def cmptab(t, fa, fb, lang, sc):
    N = ne if lang == 'en' else nv
    cells = ''.join('<td>\\([%s;\\,%s)\\)</td>' % (N(t.edge(i)), N(t.edge(i + 1))) for i in range(t.k))
    ra = ''.join('<td>\\(%d\\)</td>' % f for f in fa); rb = ''.join('<td>\\(%d\\)</td>' % f for f in fb)
    A, B = ('Class A', 'Class B') if lang == 'en' else ('Lớp A', 'Lớp B')
    return ('<div class="mbl-tablewrap mbl-freqwrap"><table class="mbl-table mbl-freq"><tbody><tr><th scope="row">%s</th>%s</tr><tr><th scope="row">%s</th>%s</tr><tr><th scope="row">%s</th>%s</tr></tbody></table></div>'
            % (gl(sc, lang), cells, A, ra, B, rb))
def s8_cmp(r, lv, ctx):
    sc = gq.SC[2] if r.random() < .5 else gq.SC[0]
    for _ in range(500):
        t = mkt(r, sc, kk=4); fa = [r.randint(2, 12) for _ in range(4)]; fb = [r.randint(2, 12) for _ in range(4)]
        j = r.randint(1, 3); na, nb = sum(fa), sum(fb); ca, cb = sum(fa[j:]), sum(fb[j:])
        pa, pb = F(ca, na), F(cb, nb)
        if pa != pb and (ca > cb) != (pa > pb) and abs(pa - pb) > F(3, 100): break
    else: raise AssertionError
    x = t.edge(j); win = 'A' if pa > pb else 'B'
    o = [win, 'B' if win == 'A' else 'A']
    opts = [tx('Class %s' % c, 'Lớp %s' % c) for c in o] + [tx('The two percentages are equal', 'Hai tỉ lệ bằng nhau'), tx('It cannot be determined', 'Không so sánh được')]
    return dict(en='The table shows the %s of the students of two classes. Which class has a larger percentage of students who %s?' % (sc['var'][0], gtx(sc, ne(x), 'en').replace('are at least', 'are at least')),
                vi='Bảng cho %s của học sinh hai lớp. Lớp nào có tỉ lệ học sinh %s cao hơn?' % (sc['var'][1], gtx(sc, nv(x), 'vi')), opts=opts, fig=(cmptab(t, fa, fb, 'en', sc), cmptab(t, fa, fb, 'vi', sc)),
                ee='Class A: \\(\\dfrac{%d}{%d}\\approx%s\\%%\\); class B: \\(\\dfrac{%d}{%d}\\approx%s\\%%\\). Compare percentages, not counts.' % (ca, na, '%.1f' % (100 * float(pa)), cb, nb, '%.1f' % (100 * float(pb))),
                ev='Lớp A: \\(\\dfrac{%d}{%d}\\approx%s\\%%\\); lớp B: \\(\\dfrac{%d}{%d}\\approx%s\\%%\\). Cần so sánh tỉ lệ, không so sánh số lượng.' % (ca, na, ('%.1f' % (100 * float(pa))).replace('.', '{,}'), cb, nb, ('%.1f' % (100 * float(pb))).replace('.', '{,}')))

A8 = [s8_count_lt, s8_modal, s8_mid]
B8 = [s8_tf_edge, s8_tf_pct]
C8 = [s8_sh_missing, s8_sh_pct]
D8 = [s8_raw, s8_ngroups, s8_relmiss, s8_hist_n, s8_hist_rel, s8_error, s8_merge, s8_cmp]

# ---------------------------------------------------------------- tiện ích nối vào bài
def mcq_one(b, n, seed, lv):
    """Một câu trắc nghiệm (đã trộn phương án) từ hàm sinh b – dùng thay một câu cũ ở phần A."""
    from mb_lib import MCQ
    from sp_g11r import _fig
    r = random.Random(seed)
    for _ in range(500):
        try: q = b(r, lv, {}); break
        except AssertionError: continue
    en, vi = _fig(q); opts = list(q['opts']); good = opts[0]; idx = list(range(4)); r.shuffle(idx); shf = [opts[i] for i in idx]; L = 'abcd'[shf.index(good)]
    return MCQ(n, (en, vi), shf, L, ('Answer: %s. %s' % (L, q['ee']), 'Đáp án %s. %s' % (L, q['ev'])))
