# -*- coding: utf-8 -*-
"""Hiệu chỉnh lớp 12 – đợt 2 (13/11/2026): phần D (8 dạng mới, khác A–C) cho Bài 1 (đơn điệu, cực trị), Bài 2 (GTLN–GTNN),
Bài 3 (tiệm cận), Bài 4 (khảo sát hàm số). Nhiều câu đọc từ đồ thị (của f hoặc f′) và bảng biến thiên.
Câu cũ của phần D vẫn được giữ trong thư viện câu hỏi (tools/question_bank.py). Kiểm tra độc lập: scripts/audit12.py."""
import math, random
from fractions import Fraction as F
from sp_g11r import tx, ne, nv, nopt, nopts
from sp_g11r2 import frt, fo, V
from sp_g12r import poly_tex, nz, sq, ksq
import fig2d as G
from mb_pgf import texsvg

# ---------------------------------------------------------------- bảng biến thiên (TikZ)
def _vis(t):
    import re as _re
    return len(_re.sub(r'\\[a-zA-Z]+', 'x', t).replace('{', '').replace('}', ''))
def vt_svg(pts, signs, fname="f'(x)", gname='f(x)'):
    """pts: danh sách điểm theo thứ tự; mỗi điểm dict(x=tex, v=(tex, 'top'|'bot') | None, z=True nếu f′=0,
    bar=((tex,pos),(tex,pos)) nếu hàm không xác định tại đó). signs: dấu f′ trên từng khoảng ('+'/'-')."""
    n = len(pts); W0 = 1.35; step = 1.9; X = [W0 + 0.75 + i * step for i in range(n)]; Wt = X[-1] + 0.75
    Y3, Y2, Y1 = 3.25, 2.55, 1.85; ytop, ybot = 1.5, 0.35
    o = ['\\draw[ink, line width=0.7pt] (0,0) rectangle (%.2f,%.2f);' % (Wt, Y3), '\\draw[ink, line width=0.6pt] (0,%.2f) -- (%.2f,%.2f);' % (Y2, Wt, Y2),
         '\\draw[ink, line width=0.6pt] (0,%.2f) -- (%.2f,%.2f);' % (Y1, Wt, Y1), '\\draw[ink, line width=0.6pt] (%.2f,0) -- (%.2f,%.2f);' % (W0, W0, Y3),
         '\\node[text=ink] at (%.2f,%.2f) {$x$};' % (W0 / 2, (Y2 + Y3) / 2), '\\node[text=ink] at (%.2f,%.2f) {$%s$};' % (W0 / 2, (Y1 + Y2) / 2, fname),
         '\\node[text=ink] at (%.2f,%.2f) {$%s$};' % (W0 / 2, Y1 / 2, gname)]
    ends = []          # (vị trí trái, vị trí phải) của giá trị tại mỗi điểm: (x, y)
    for i, p in enumerate(pts):
        o.append('\\node[text=ink] at (%.2f,%.2f) {$%s$};' % (X[i], (Y2 + Y3) / 2, p['x']))
        if p.get('z'): o.append('\\node[text=ink] at (%.2f,%.2f) {$0$};' % (X[i], (Y1 + Y2) / 2))
        if p.get('bar'):
            for d in (-0.045, 0.045): o.append('\\draw[ink, line width=0.6pt] (%.3f,0) -- (%.3f,%.2f);' % (X[i] + d, X[i] + d, Y2))
            (lt, lp), (rt, rp) = p['bar']; yl = ytop if lp == 'top' else ybot; yr = ytop if rp == 'top' else ybot
            o.append('\\node[text=ink, anchor=east] at (%.2f,%.2f) {$%s$};' % (X[i] - 0.1, yl, lt)); o.append('\\node[text=ink, anchor=west] at (%.2f,%.2f) {$%s$};' % (X[i] + 0.1, yr, rt))
            ends.append(((X[i] - 0.1 - 0.17 * _vis(lt) - 0.12, yl), (X[i] + 0.1 + 0.17 * _vis(rt) + 0.12, yr)))
        else:
            t, pos = p['v']; y = ytop if pos == 'top' else ybot
            o.append('\\node[text=ink] at (%.2f,%.2f) {$%s$};' % (X[i], y, t)); w = 0.09 * _vis(t) + 0.28
            ends.append(((X[i] - w, y), (X[i] + w, y)))
    for i, s in enumerate(signs):
        o.append('\\node[text=ink] at (%.2f,%.2f) {$%s$};' % ((X[i] + X[i + 1]) / 2, (Y1 + Y2) / 2, s))
        (x0, y0), (x1, y1) = ends[i][1], ends[i + 1][0]
        dy0 = -0.18 if y0 > 1 else 0.18; dy1 = -0.18 if y1 > 1 else 0.18
        o.append('\\draw[ink, line width=0.7pt, -{Stealth[length=2.2mm]}] (%.2f,%.2f) -- (%.2f,%.2f);' % (x0, y0 + dy0, x1, y1 + dy1))
    return texsvg('\\begin{tikzpicture}\n' + '\n'.join(o) + '\n\\end{tikzpicture}')
def VTFIG(pts, signs, px=None, **kw):
    fn = vt_svg(pts, signs, **kw); px = px or min(460, 120 + 95 * len(pts))
    return G.FIG(fn, 'Variation table', 'Bảng biến thiên', px)

def cub(a, b, c, d): return lambda x: ((a * x + b) * x + c) * x + d
def iv(a, b):
    A = '-\\infty' if a is None else frt(a); B = '+\\infty' if b is None else frt(b); return '(%s;\\,%s)' % (A, B)
def ticks_for(vals, lo, hi): return [(v, frt(v)) for v in sorted(set(vals)) if v != 0 and lo < v < hi]

# =============================================================== Bài 1 – Tính đơn điệu và cực trị
def m1_fp_dec(r, lv):
    """Đồ thị y = f′(x) (bậc ba có 3 nghiệm) → khoảng nghịch biến của f."""
    for _ in range(300):
        a, b, c = sorted(r.sample(range(-3, 4), 3))
        if b - a < 2 and c - b < 2: continue
        k0 = r.choice([1, -1]); bump = max(abs((F(x, 20) - a) * (F(x, 20) - b) * (F(x, 20) - c)) for x in range(20 * a, 20 * c + 1))
        b1 = max(abs((F(x, 20) - a) * (F(x, 20) - b) * (F(x, 20) - c)) for x in range(20 * a, 20 * b + 1)); b2 = max(abs((F(x, 20) - a) * (F(x, 20) - b) * (F(x, 20) - c)) for x in range(20 * b, 20 * c + 1))
        if max(b1, b2) > 3 * min(b1, b2): continue
        k = k0 * F(5, 2) / bump; k = F(k).limit_denominator(12)
        fp = lambda x: k * (x - a) * (x - b) * (x - c)
        ys = [fp(F(x, 10)) for x in range(10 * a, 10 * c + 1)]
        break
    else: raise AssertionError
    roots = [a, b, c]; segs = [(None, a), (a, b), (b, c), (c, None)]
    sgn = [1 if fp(F((p if p is not None else q - 1) + (q if q is not None else p + 1), 2)) > 0 else -1 for p, q in segs]
    neg = [s for s, g in zip(segs, sgn) if g < 0]; pos = [s for s, g in zip(segs, sgn) if g > 0]
    good = r.choice(neg); bad = pos + [(a, c), (None, b), (b, None)]
    bad = [x for x in bad if x != good]
    yr = 2.9
    img = G.graph_svg([(lambda x: float(fp(F(x).limit_denominator(1000))), G.GREEN)], (a - 1.2, c + 1.2), (-yr, yr), ticks_for(roots, a - 2, c + 2), [], dots=[(x, 0, False) for x in roots], W=6.4, H=3.8, names=('x', "y=f'(x)"))
    pe, pv = V(lv, [("The figure shows the graph of \\(y=f'(x)\\). On which interval is \\(f\\) decreasing?", "Hình vẽ là đồ thị của hàm số \\(y=f'(x)\\). Hàm số \\(f\\) nghịch biến trên khoảng nào?"),
                    ("Below is the graph of the derivative \\(f'\\). The function \\(f\\) decreases on which interval?", "Dưới đây là đồ thị của đạo hàm \\(f'\\). Hàm số \\(f\\) nghịch biến trên khoảng nào sau đây?"),
                    ("The curve in the figure is \\(y=f'(x)\\) (not \\(y=f(x)\\)). Which interval is an interval where \\(f\\) is decreasing?", "Đường cong trong hình là \\(y=f'(x)\\) (không phải \\(y=f(x)\\)). Khoảng nào là một khoảng nghịch biến của \\(f\\)?")])
    return dict(en=pe, vi=pv, opts=fo(iv(*good), [iv(*x) for x in bad]), fig=G.FIG(img, "Graph of f'", "Đồ thị của f'", 330),
                ee="\\(f\\) decreases where the graph of \\(f'\\) lies below \\(Ox\\): on \\(%s\\)." % ', '.join('\\(%s\\)' % iv(*x) for x in neg).replace('\\(\\(', '\\(').replace('\\)\\)', '\\)'),
                ev="\\(f\\) nghịch biến khi đồ thị \\(f'\\) nằm dưới \\(Ox\\): trên %s." % ', '.join('\\(%s\\)' % iv(*x) for x in neg))

def m1_fp_max(r, lv):
    """Đồ thị f′ có một nghiệm kép → điểm cực đại / số điểm cực trị."""
    for _ in range(300):
        a, b, c = sorted(r.sample(range(-3, 4), 3)); dbl = r.choice([a, b, c])
        if b - a < 2 or c - b < 2: continue
        others = [x for x in (a, b, c) if x != dbl]
        g = lambda x: (x - dbl) ** 2 * (x - others[0]) * (x - others[1])
        bs = [max(abs(g(F(x, 20))) for x in range(20 * lo, 20 * hi + 1)) for lo, hi in ((a, b), (b, c))]
        if max(bs) > 3 * min(bs): continue
        k = (r.choice([1, -1]) * F(5, 2) / max(bs)).limit_denominator(12)
        fp = lambda x: k * g(x)
        ys = [fp(F(x, 10)) for x in range(10 * a, 10 * c + 1)]
        break
    else: raise AssertionError
    ext = []
    for x0 in (a, b, c):
        L, R_ = fp(x0 - F(1, 100)), fp(x0 + F(1, 100))
        if L > 0 > R_: ext.append((x0, 'max'))
        if L < 0 < R_: ext.append((x0, 'min'))
    yr = max(abs(float(v)) for v in ys) * 1.15 + .2
    img = G.graph_svg([(lambda x: float(fp(F(x).limit_denominator(1000))), G.GREEN)], (a - 1.2, c + 1.2), (-yr, yr), ticks_for([a, b, c], a - 2, c + 2), [], dots=[(x, 0, False) for x in (a, b, c)], W=6.4, H=3.8, names=('x', "y=f'(x)"))
    fig = G.FIG(img, "Graph of f'", "Đồ thị của f'", 330)
    if lv == 1 or not [e for e in ext if e[1] == 'max']:
        n = len(ext)
        return dict(en="The figure shows the graph of \\(y=f'(x)\\). How many extreme points does \\(f\\) have?", vi="Hình vẽ là đồ thị của \\(y=f'(x)\\). Hàm số \\(f\\) có bao nhiêu điểm cực trị?",
                    opts=nopts(r, n, [3, 1, 0, 2]), fig=fig,
                    ee="\\(f'\\) changes sign only at %s; at the double root \\(x=%d\\) the graph of \\(f'\\) touches \\(Ox\\) without crossing, so it is not an extreme point. Answer: \\(%d\\)." % (', '.join('\\(x=%d\\)' % e[0] for e in ext), dbl, n),
                    ev="\\(f'\\) chỉ đổi dấu tại %s; tại nghiệm kép \\(x=%d\\) đồ thị \\(f'\\) chạm \\(Ox\\) mà không cắt nên không là điểm cực trị. Đáp số: \\(%d\\)." % (', '.join('\\(x=%d\\)' % e[0] for e in ext), dbl, n))
    mx = [e[0] for e in ext if e[1] == 'max'][0]
    return dict(en="The figure shows the graph of \\(y=f'(x)\\). At which point does \\(f\\) have a local maximum?", vi="Hình vẽ là đồ thị của \\(y=f'(x)\\). Hàm số \\(f\\) đạt cực đại tại điểm nào?",
                opts=fo('x=%d' % mx, ['x=%d' % x for x in (a, b, c) if x != mx] + ['x=0' if 0 not in (a, b, c) else 'x=4']), fig=fig,
                ee="Local maximum where \\(f'\\) changes from \\(+\\) to \\(-\\): \\(x=%d\\)." % mx, ev="Cực đại tại điểm \\(f'\\) đổi dấu từ \\(+\\) sang \\(-\\): \\(x=%d\\)." % mx)

def cubic_from(r, crit=None):
    """f = a x³ + b x² + c x + d có hai điểm tới hạn nguyên p < q, giá trị nguyên."""
    for _ in range(500):
        p = r.randint(-3, 1); q = p + 2; s = r.choice([1, -1])
        # f′ = 3 s (x−p)(x−q) → f = s(x³ − 3(p+q)/2 x² + 3pq x) + d
        if (p + q) % 2: continue
        d = r.randint(-4, 4)
        f = lambda x, p=p, q=q, s=s, d=d: s * (x ** 3 - F(3 * (p + q), 2) * x ** 2 + 3 * p * q * x) + d
        if abs(f(p) - f(q)) > 40 or f(p) == f(q): continue
        return dict(p=p, q=q, s=s, d=d, f=f, tex=poly_tex3(s, -s * F(3 * (p + q), 2), s * 3 * p * q, d))
    raise AssertionError
def poly_tex3(a, b, c, d):
    out = ''
    for co, pw in ((a, 3), (b, 2), (c, 1), (d, 0)):
        co = F(co)
        if co == 0: continue
        body = {3: 'x^3', 2: 'x^2', 1: 'x', 0: ''}[pw]; m = abs(co)
        t = (body if m == 1 and pw else frt(m) + body)
        out += ('-' if co < 0 else ('+' if out else '')) + t
    return out or '0'

def m1_vt(r, lv):
    C = cubic_from(r); p, q, s, f = C['p'], C['q'], C['s'], C['f']
    if s > 0: pts = [dict(x='-\\infty', v=('-\\infty', 'bot')), dict(x=frt(p), v=(frt(f(p)), 'top'), z=True), dict(x=frt(q), v=(frt(f(q)), 'bot'), z=True), dict(x='+\\infty', v=('+\\infty', 'top'))]; sg = ['+', '-', '+']; mx, mn = p, q
    else: pts = [dict(x='-\\infty', v=('+\\infty', 'top')), dict(x=frt(p), v=(frt(f(p)), 'bot'), z=True), dict(x=frt(q), v=(frt(f(q)), 'top'), z=True), dict(x='+\\infty', v=('-\\infty', 'bot'))]; sg = ['-', '+', '-']; mx, mn = q, p
    ask = V(lv, ['maxval', 'minpt', 'maxval'])
    if ask == 'maxval':
        good = f(mx)
        return dict(en='The variation table of \\(y=f(x)\\) is shown. What is the local maximum value of \\(f\\)?', vi='Cho bảng biến thiên của hàm số \\(y=f(x)\\). Giá trị cực đại của hàm số là',
                    opts=nopts(r, good, [f(mn), mx, mn, good + 1]), fig=VTFIG(pts, sg),
                    ee='The local maximum is the value at the top of the "peak": \\(f(%d)=%s\\) (not the point \\(x=%d\\)).' % (mx, frt(good), mx),
                    ev='Giá trị cực đại là giá trị ở "đỉnh": \\(f(%d)=%s\\) (không phải điểm \\(x=%d\\)).' % (mx, frt(good), mx))
    return dict(en='The variation table of \\(y=f(x)\\) is shown. The function has a local minimum at…', vi='Cho bảng biến thiên của hàm số \\(y=f(x)\\). Hàm số đạt cực tiểu tại',
                opts=fo('x=%d' % mn, ['x=%d' % mx, 'x=%s' % frt(f(mn)), 'x=%s' % frt(f(mx)) if f(mx) not in (mn, mx) else 'x=%d' % (mn + 5)]), fig=VTFIG(pts, sg),
                ee='\\(f\'\\) changes from \\(-\\) to \\(+\\) at \\(x=%d\\): local minimum there (value \\(%s\\)).' % (mn, frt(f(mn))), ev='\\(f\'\\) đổi dấu từ \\(-\\) sang \\(+\\) tại \\(x=%d\\): cực tiểu tại đó (giá trị \\(%s\\)).' % (mn, frt(f(mn))))

def m1_fgraph(r, lv):
    C = cubic_from(r); p, q, s, f = C['p'], C['q'], C['s'], C['f']
    ys = [f(p), f(q), f(p - F(11, 10)), f(q + F(11, 10))]; lo, hi = float(min(ys)) - .5, float(max(ys)) + .5
    if hi - lo > 14: raise AssertionError
    img = G.graph_svg([(lambda x: float(f(F(x).limit_denominator(1000))), G.GREEN)], (p - 1.2, q + 1.2), (min(lo, -.6), max(hi, .6)), ticks_for([p, q], p - 2, q + 2),
                      ticks_for([f(p), f(q)], -99, 99), dots=[(p, f(p), False), (q, f(q), False)], vlines=[(p, None), (q, None)] if False else [], W=6.0, H=4.2)
    inc = [(p, q)] if s < 0 else [(None, p), (q, None)]; dec = [(None, p), (q, None)] if s < 0 else [(p, q)]
    good = r.choice(inc); bad = dec + [(None, q), (p, None), (F(f(q)), F(f(p))) if f(q) < f(p) else (F(f(p)), F(f(q)))]
    return dict(en='The figure shows the graph of \\(y=f(x)\\). On which interval is \\(f\\) increasing?', vi='Hình vẽ là đồ thị của hàm số \\(y=f(x)\\). Hàm số đồng biến trên khoảng nào?',
                opts=fo(iv(*good), [iv(*x) for x in bad if x != good]), fig=G.FIG(img, 'Graph of f', 'Đồ thị của f', 320),
                ee='The graph goes up (from left to right) on \\(%s\\). Read intervals on \\(Ox\\), not values on \\(Oy\\).' % ', '.join(iv(*x) for x in inc),
                ev='Đồ thị đi lên (từ trái sang phải) trên \\(%s\\). Khoảng đọc trên trục \\(Ox\\), không phải giá trị trên \\(Oy\\).' % ', '.join(iv(*x) for x in inc))

INC = [('y=x^3+3x', True, "y'=3x^2+3\\gt0"), ('y=x^3-3x', False, "y'=3x^2-3"), ('y=x^4+1', False, "y'=4x^3"), ('y=\\dfrac{x-1}{x+1}', False, 'not defined at \\(-1\\)'),
       ('y=x-\\sin x', True, "y'=1-\\cos x\\ge0"), ('y=x^3+x^2+x', True, "y'=3x^2+2x+1\\gt0"), ('y=2x+\\cos x', True, "y'=2-\\sin x\\gt0"), ('y=\\sqrt{x^2+1}', False, "y'=\\dfrac{x}{\\sqrt{x^2+1}}"),
       ('y=x^2+2x', False, "y'=2x+2"), ('y=-x^3+x', False, "y'=-3x^2+1"), ('y=x+\\dfrac1x', False, 'not defined at 0'), ('y=e^{-x}', False, "y'=-e^{-x}\\lt0")]
def m1_which(r, lv):
    good = r.choice([x for x in INC if x[1]]); bad = r.sample([x for x in INC if not x[1]], 3)
    q = V(lv, [('Which function is increasing on \\(\\mathbb R\\)?', 'Hàm số nào đồng biến trên \\(\\mathbb R\\)?'), ('Exactly one function below is increasing on the whole of \\(\\mathbb R\\). Which one?', 'Chỉ có một hàm số dưới đây đồng biến trên cả \\(\\mathbb R\\). Đó là hàm số nào?'),
                   ('Which function has \\(y\'\\ge0\\) for every real \\(x\\) (and so increases on \\(\\mathbb R\\))?', 'Hàm số nào có \\(y\'\\ge0\\) với mọi số thực \\(x\\) (nên đồng biến trên \\(\\mathbb R\\))?')])
    return dict(en=q[0], vi=q[1], opts=[good[0]] + [b[0] for b in bad],
                ee='\\(%s\\): \\(%s\\) (equal to 0 only at isolated points). The others are not defined on all of \\(\\mathbb R\\) or have \\(y\'\\lt0\\) somewhere.' % (good[0], good[2]),
                ev='\\(%s\\): \\(%s\\) (chỉ bằng 0 tại các điểm rời rạc). Các hàm còn lại không xác định trên \\(\\mathbb R\\) hoặc có \\(y\'\\lt0\\) ở đâu đó.' % (good[0], good[2]))

def m1_param(r, lv):
    x0 = r.randint(-2, 4); typ = r.choice(['min', 'max']); m = x0 - 1 if typ == 'min' else x0 + 1
    # f = x³ − 3m x² + 3(m²−1)x ; f′ = 3(x−m+1)(x−m−1): cực đại tại m−1, cực tiểu tại m+1
    ft = poly_tex3(1, -3 * m, 3 * (m * m - 1), 0) if m * m != 1 else poly_tex3(1, -3 * m, 0, 0)
    ft_gen = 'x^3-3mx^2+3(m^2-1)x'
    other = x0 + 1 if typ == 'min' else x0 - 1
    return dict(en='Find \\(m\\) so that \\(f(x)=%s\\) has a local %s at \\(x=%d\\).' % (ft_gen, 'minimum' if typ == 'min' else 'maximum', x0),
                vi='Tìm \\(m\\) để hàm số \\(f(x)=%s\\) đạt cực %s tại \\(x=%d\\).' % (ft_gen, 'tiểu' if typ == 'min' else 'đại', x0),
                opts=nopts(r, m, [other, x0, -m if -m != m else m + 3, m + 2 if m + 2 != other else m - 2]),
                ee="\\(f'(x)=3(x-m+1)(x-m-1)\\): local maximum at \\(x=m-1\\), local minimum at \\(x=m+1\\). So \\(%s=%d\\Rightarrow m=%d\\) (check: \\(f''(%d)%s0\\))." % ('m+1' if typ == 'min' else 'm-1', x0, m, x0, '\\gt' if typ == 'min' else '\\lt'),
                ev="\\(f'(x)=3(x-m+1)(x-m-1)\\): cực đại tại \\(x=m-1\\), cực tiểu tại \\(x=m+1\\). Vậy \\(%s=%d\\Rightarrow m=%d\\) (thử lại: \\(f''(%d)%s0\\))." % ('m+1' if typ == 'min' else 'm-1', x0, m, x0, '\\gt' if typ == 'min' else '\\lt'))

def m1_sales(r, lv):
    a = r.choice([2, 3, 4, 5]); T = 2 * a + r.choice([2, 3, 4]); c = r.choice([10, 20, 50])
    # S(t) = −t³ + 3a t² + c, S′ = 3t(2a − t) > 0 trên (0; 2a)
    St = 'S(t)=-t^3+%dt^2+%d' % (3 * a, c)
    return dict(en='The number of products sold (hundreds) after \\(t\\) months is \\(%s\\), \\(0\\le t\\le%d\\). During which period are the sales increasing?' % (St, T),
                vi='Số sản phẩm bán được (trăm sản phẩm) sau \\(t\\) tháng là \\(%s\\), \\(0\\le t\\le%d\\). Trong khoảng thời gian nào số sản phẩm bán ra tăng?' % (St, T),
                opts=fo('(0;\\,%d)' % (2 * a), ['(%d;\\,%d)' % (2 * a, T), '(0;\\,%d)' % (3 * a) if 3 * a < T else '(0;\\,%d)' % a, '(0;\\,%d)' % T, '(%d;\\,%d)' % (a, T)]),
                ee="\\(S'(t)=-3t^2+%dt=3t(%d-t)\\gt0\\Leftrightarrow0\\lt t\\lt%d\\)." % (6 * a, 2 * a, 2 * a), ev="\\(S'(t)=-3t^2+%dt=3t(%d-t)\\gt0\\Leftrightarrow0\\lt t\\lt%d\\)." % (6 * a, 2 * a, 2 * a))

EXL = [('y=xe^x', 'min', '-1', ["1", "0", "e"], "y'=(x+1)e^x"), ('y=xe^{-x}', 'max', '1', ['-1', '0', 'e'], "y'=(1-x)e^{-x}"), ('y=x\\ln x', 'min', '\\dfrac1e', ['e', '1', '0'], "y'=\\ln x+1"),
       ('y=\\ln x-x', 'max', '1', ['e', '\\dfrac1e', '0'], "y'=\\dfrac1x-1"), ('y=x^2e^x', 'max', '-2', ['0', '2', '-1'], "y'=x(x+2)e^x"), ('y=e^x-x', 'min', '0', ['1', '-1', 'e'], "y'=e^x-1"),
       ('y=\\dfrac{\\ln x}{x}', 'max', 'e', ['1', '\\dfrac1e', 'e^2'], "y'=\\dfrac{1-\\ln x}{x^2}")]
def m1_explog(r, lv):
    fx, typ, g, b, d = r.choice(EXL)
    return dict(en='The function \\(%s\\) has a local %s at…' % (fx, 'maximum' if typ == 'max' else 'minimum'), vi='Hàm số \\(%s\\) đạt cực %s tại' % (fx, 'đại' if typ == 'max' else 'tiểu'),
                opts=['x=' + g] + ['x=' + x for x in b],
                ee="\\(%s\\); it changes sign %s at \\(x=%s\\)." % (d, 'from \\(+\\) to \\(-\\)' if typ == 'max' else 'from \\(-\\) to \\(+\\)', g),
                ev="\\(%s\\); đổi dấu %s tại \\(x=%s\\)." % (d, 'từ \\(+\\) sang \\(-\\)' if typ == 'max' else 'từ \\(-\\) sang \\(+\\)', g))

D1 = [m1_fp_dec, m1_fp_max, m1_vt, m1_fgraph, m1_which, m1_param, m1_sales, m1_explog]

# =============================================================== Bài 2 – Giá trị lớn nhất, nhỏ nhất
def m2_graph(r, lv):
    for _ in range(500):
        C = cubic_from(r); p, q, f = C['p'], C['q'], C['f']
        a = p - r.choice([0, 1]); b = q + r.choice([0, 1])
        if (a, b) == (p, q): continue
        vals = {x: f(x) for x in (a, p, q, b)}
        if max(vals.values()) - min(vals.values()) > 12: continue
        ask = V(lv, ['max', 'min', 'max'])
        M = max(vals.values()); m = min(vals.values())
        if lv == 3 and M not in (f(a), f(b)) and m not in (f(a), f(b)): continue      # mức 3: đáp án tại đầu mút (bẫy cực trị)
        break
    else: raise AssertionError
    lo, hi = float(m) - .6, float(M) + .6
    img = G.graph_svg([(lambda x: float(f(F(x).limit_denominator(1000))) if a <= x <= b else None, G.GREEN)], (a - .8, b + .8), (min(lo, -.6), max(hi, .6)),
                      ticks_for([a, p, q, b], a - 1, b + 1), ticks_for(list(vals.values()), -99, 99), dots=[(x, v, False) for x, v in vals.items()], W=6.0, H=4.2)
    good = M if ask == 'max' else m; loc = [f(p), f(q)]
    return dict(en='The figure shows the graph of \\(y=f(x)\\) on \\([%d;\\,%d]\\). The %s value of \\(f\\) on \\([%d;\\,%d]\\) is…' % (a, b, 'largest' if ask == 'max' else 'smallest', a, b),
                vi='Hình vẽ là đồ thị của hàm số \\(y=f(x)\\) trên đoạn \\([%d;\\,%d]\\). Giá trị %s của \\(f\\) trên đoạn \\([%d;\\,%d]\\) là' % (a, b, 'lớn nhất' if ask == 'max' else 'nhỏ nhất', a, b),
                opts=nopts(r, good, [x for x in loc + list(vals.values()) if x != good] + [good + 1]), fig=G.FIG(img, 'Graph on a closed interval', 'Đồ thị trên một đoạn', 320),
                ee='Compare the heights at the ends and at the turning points: \\(%s\\); the %s is \\(%s\\).' % (', '.join('f(%d)=%s' % (x, frt(v)) for x, v in vals.items()), 'largest' if ask == 'max' else 'smallest', frt(good)),
                ev='So sánh độ cao tại hai đầu mút và các điểm cực trị: \\(%s\\); giá trị %s là \\(%s\\).' % (', '.join('f(%d)=%s' % (x, frt(v)) for x, v in vals.items()), 'lớn nhất' if ask == 'max' else 'nhỏ nhất', frt(good)))

def m2_vt(r, lv):
    for _ in range(500):
        C = cubic_from(r); p, q, s, f = C['p'], C['q'], C['s'], C['f']; a, b = p - r.choice([1, 2]), q + r.choice([1, 2])
        vals = [f(a), f(p), f(q), f(b)]
        if len(set(vals)) == 4 and max(vals) - min(vals) <= 40: break
    else: raise AssertionError
    up = s > 0
    pts = [dict(x=frt(a), v=(frt(f(a)), 'bot' if up else 'top')), dict(x=frt(p), v=(frt(f(p)), 'top' if up else 'bot'), z=True), dict(x=frt(q), v=(frt(f(q)), 'bot' if up else 'top'), z=True), dict(x=frt(b), v=(frt(f(b)), 'top' if up else 'bot'))]
    sg = ['+', '-', '+'] if up else ['-', '+', '-']
    ask = r.choice(['max', 'min']); good = max(vals) if ask == 'max' else min(vals)
    return dict(en='The variation table of \\(y=f(x)\\) on \\([%d;\\,%d]\\) is shown. The %s value of \\(f\\) on this interval is…' % (a, b, 'largest' if ask == 'max' else 'smallest'),
                vi='Cho bảng biến thiên của hàm số \\(y=f(x)\\) trên đoạn \\([%d;\\,%d]\\). Giá trị %s của \\(f\\) trên đoạn này là' % (a, b, 'lớn nhất' if ask == 'max' else 'nhỏ nhất'),
                opts=nopts(r, good, [v for v in vals if v != good] + [a, b]), fig=VTFIG(pts, sg),
                ee='Compare all the values in the bottom row: \\(%s\\).' % ', '.join(frt(v) for v in vals), ev='So sánh mọi giá trị ở hàng cuối: \\(%s\\).' % ', '.join(frt(v) for v in vals))

TRG = [('y=3\\sin x+4\\cos x', 'max', '5', ['7', '1', '4']), ('y=3\\sin x+4\\cos x', 'min', '-5', ['-7', '-1', '-4']), ('y=\\sin x+\\sqrt3\\cos x', 'max', '2', ['1+\\sqrt3', '\\sqrt3', '1']),
       ('y=\\cos 2x+2\\sin x', 'max', '\\dfrac32', ['3', '1', '2']), ('y=\\sin^2x-4\\sin x+3', 'max', '8', ['3', '0', '4']), ('y=\\sin^2x-4\\sin x+3', 'min', '0', ['-1', '3', '2']),
       ('y=2\\sin^2x+\\cos 2x', 'max', '1', ['3', '2', '0']), ('y=\\sin x\\cos x', 'max', '\\dfrac12', ['1', '2', '\\dfrac14'])]
def m2_trig(r, lv):
    fx, typ, g, b = r.choice(TRG)
    return dict(en='The %s value of \\(%s\\) on \\(\\mathbb R\\) is…' % ('largest' if typ == 'max' else 'smallest', fx), vi='Giá trị %s của hàm số \\(%s\\) trên \\(\\mathbb R\\) là' % ('lớn nhất' if typ == 'max' else 'nhỏ nhất', fx),
                opts=[g] + b, ee='Write \\(y\\) in terms of one quantity (for example \\(t=\\sin x\\in[-1;1]\\), or \\(a\\sin x+b\\cos x=\\sqrt{a^2+b^2}\\sin(x+\\varphi)\\)) and study it on its range. Answer: \\(%s\\).' % g,
                ev='Đưa \\(y\\) về một đại lượng (chẳng hạn \\(t=\\sin x\\in[-1;1]\\), hoặc \\(a\\sin x+b\\cos x=\\sqrt{a^2+b^2}\\sin(x+\\varphi)\\)) rồi khảo sát trên miền giá trị của nó. Đáp số: \\(%s\\).' % g)

SQ = [('y=x+\\sqrt{4-x^2}', 'max', '2\\sqrt2', ['2', '4', '\\sqrt2']), ('y=x+\\sqrt{4-x^2}', 'min', '-2', ['0', '-2\\sqrt2', '2']), ('y=\\sqrt x+\\sqrt{4-x}', 'max', '2\\sqrt2', ['4', '2', '\\sqrt2']),
      ('y=\\sqrt x+\\sqrt{4-x}', 'min', '2', ['0', '\\sqrt2', '2\\sqrt2']), ('y=x\\sqrt{4-x^2}', 'max', '2', ['4', '\\sqrt2', '2\\sqrt2']), ('y=x+\\sqrt{2-x^2}', 'max', '2', ['\\sqrt2', '2\\sqrt2', '1'])]
def m2_sqrt(r, lv):
    fx, typ, g, b = r.choice(SQ)
    return dict(en='The %s value of \\(%s\\) (on its domain) is…' % ('largest' if typ == 'max' else 'smallest', fx), vi='Giá trị %s của hàm số \\(%s\\) (trên tập xác định) là' % ('lớn nhất' if typ == 'max' else 'nhỏ nhất', fx),
                opts=[g] + b, ee='Find the domain (a closed interval), solve \\(y\'=0\\) inside it, then compare the values at the critical points and at the ends: \\(%s\\).' % g,
                ev='Tìm tập xác định (một đoạn), giải \\(y\'=0\\) trên đó rồi so sánh giá trị tại điểm tới hạn và hai đầu mút: \\(%s\\).' % g)

def m2_param(r, lv):
    T = r.randint(-3, 9); a, b = 0, r.choice([3, 4]); c = r.choice([1, 2]) if b == 4 else 1
    # f = x² − 2c x + m trên [0; b], c ∈ (0;b): min = m − c², max = max(f(0), f(b)) = m + max(0, b² − 2cb)
    ask = r.choice(['min', 'max'])
    if ask == 'min': m = T + c * c
    else: m = T - max(0, b * b - 2 * c * b)
    return dict(en='Find \\(m\\) so that the %s value of \\(f(x)=x^2-%sx+m\\) on \\([0;\\,%d]\\) equals \\(%d\\).' % ('smallest' if ask == 'min' else 'largest', '' if c == 1 else '%d' % (2 * c), b, T) if c != 1 else
                   'Find \\(m\\) so that the %s value of \\(f(x)=x^2-2x+m\\) on \\([0;\\,%d]\\) equals \\(%d\\).' % ('smallest' if ask == 'min' else 'largest', b, T),
                vi='Tìm \\(m\\) để giá trị %s của hàm số \\(f(x)=x^2-%sx+m\\) trên đoạn \\([0;\\,%d]\\) bằng \\(%d\\).' % ('nhỏ nhất' if ask == 'min' else 'lớn nhất', '2' if c == 1 else '%d' % (2 * c), b, T),
                opts=nopts(r, m, [T, T - c * c if ask == 'min' else T + c * c, T + max(0, b * b - 2 * c * b) if ask == 'min' else T - c * c, m + 1]),
                ee='On \\([0;%d]\\): smallest \\(f(%d)=m-%d\\), largest \\(f(%d)=m+%d\\). Setting the %s equal to \\(%d\\) gives \\(m=%d\\).' % (b, c, c * c, b if b * b - 2 * c * b > 0 else 0, max(0, b * b - 2 * c * b), 'smallest' if ask == 'min' else 'largest', T, m),
                ev='Trên \\([0;%d]\\): nhỏ nhất \\(f(%d)=m-%d\\), lớn nhất \\(f(%d)=m+%d\\). Cho giá trị %s bằng \\(%d\\) được \\(m=%d\\).' % (b, c, c * c, b if b * b - 2 * c * b > 0 else 0, max(0, b * b - 2 * c * b), 'nhỏ nhất' if ask == 'min' else 'lớn nhất', T, m))

EXM = [('y=xe^{-x}', '[0;\\,2]', 'max', '\\dfrac1e', ['\\dfrac{2}{e^2}', '0', 'e']), ('y=x-\\ln x', '\\left[\\dfrac12;\\,e\\right]', 'min', '1', ['\\dfrac12+\\ln2', 'e-1', '0']),
       ('y=\\dfrac{\\ln x}{x}', '[1;\\,e^2]', 'max', '\\dfrac1e', ['\\dfrac{2}{e^2}', '0', 'e']), ('y=e^x-x', '[-1;\\,1]', 'min', '1', ['0', 'e-1', '\\dfrac1e+1']),
       ('y=e^x-x', '[-1;\\,1]', 'max', 'e-1', ['\\dfrac1e+1', '1', 'e']), ('y=x^2-2\\ln x', '\\left[\\dfrac1e;\\,e\\right]', 'min', '1', ['0', '\\dfrac1{e^2}+2', 'e^2-2'])]
def m2_explog(r, lv):
    fx, I, typ, g, b = r.choice(EXM)
    return dict(en='The %s value of \\(%s\\) on \\(%s\\) is…' % ('largest' if typ == 'max' else 'smallest', fx, I), vi='Giá trị %s của hàm số \\(%s\\) trên đoạn \\(%s\\) là' % ('lớn nhất' if typ == 'max' else 'nhỏ nhất', fx, I),
                opts=[g] + b, ee='Solve \\(y\'=0\\) in the interval, then compare the values at that point and at the two ends. Answer: \\(%s\\).' % g,
                ev='Giải \\(y\'=0\\) trên đoạn, rồi so sánh giá trị tại điểm đó và tại hai đầu mút. Đáp số: \\(%s\\).' % g)

def m2_visitors(r, lv):
    a = r.choice([2, 3, 4]); c = r.choice([5, 10, 20]); T = 2 * a + r.choice([1, 2, 3])
    N = lambda t: -t ** 3 + 3 * a * t * t + c
    vals = {t: N(t) for t in range(T + 1)}; best = max(vals.values()); assert best == N(2 * a) == 4 * a ** 3 + c
    ask = V(lv, ['val', 'time', 'val'])
    if ask == 'val':
        return dict(en='During a festival, the number of visitors (hundreds) \\(t\\) hours after opening is \\(N(t)=-t^3+%dt^2+%d\\), \\(0\\le t\\le%d\\). The largest number of visitors (hundreds) is…' % (3 * a, c, T),
                    vi='Trong một lễ hội, số khách (trăm người) sau \\(t\\) giờ kể từ khi mở cửa là \\(N(t)=-t^3+%dt^2+%d\\), \\(0\\le t\\le%d\\). Số khách lớn nhất (trăm người) là' % (3 * a, c, T),
                    opts=nopts(r, best, [N(a), N(T), c, best + a]),
                    ee="\\(N'(t)=-3t^2+%dt=0\\Leftrightarrow t=0\\) or \\(t=%d\\); \\(N(0)=%d\\), \\(N(%d)=%d\\), \\(N(%d)=%d\\). Largest: \\(%d\\)." % (6 * a, 2 * a, c, 2 * a, best, T, N(T), best),
                    ev="\\(N'(t)=-3t^2+%dt=0\\Leftrightarrow t=0\\) hoặc \\(t=%d\\); \\(N(0)=%d\\), \\(N(%d)=%d\\), \\(N(%d)=%d\\). Lớn nhất: \\(%d\\)." % (6 * a, 2 * a, c, 2 * a, best, T, N(T), best))
    return dict(en='During a festival, the number of visitors (hundreds) \\(t\\) hours after opening is \\(N(t)=-t^3+%dt^2+%d\\), \\(0\\le t\\le%d\\). After how many hours is the number of visitors largest?' % (3 * a, c, T),
                vi='Trong một lễ hội, số khách (trăm người) sau \\(t\\) giờ kể từ khi mở cửa là \\(N(t)=-t^3+%dt^2+%d\\), \\(0\\le t\\le%d\\). Sau bao nhiêu giờ thì số khách đông nhất?' % (3 * a, c, T),
                opts=nopts(r, 2 * a, [a, 3 * a if 3 * a != T else T + 1, T, 2 * a + 1 if 2 * a + 1 != T else 1]),
                ee="\\(N'(t)=3t(%d-t)\\): \\(N\\) increases on \\((0;%d)\\) and decreases on \\((%d;%d)\\), so the largest value is at \\(t=%d\\)." % (2 * a, 2 * a, 2 * a, T, 2 * a),
                ev="\\(N'(t)=3t(%d-t)\\): \\(N\\) tăng trên \\((0;%d)\\) và giảm trên \\((%d;%d)\\), nên lớn nhất tại \\(t=%d\\)." % (2 * a, 2 * a, 2 * a, T, 2 * a))

def m2_sum(r, lv):
    for _ in range(300):
        p = r.choice([1, 2]); lo = r.randint(-3, 0); hi = r.randint(1, 4)
        f = lambda x: x ** 3 - 3 * p * p * x
        cand = [lo, hi] + [x for x in (-p, p) if lo < x < hi]
        vals = [f(x) for x in cand]; M, m = max(vals), min(vals)
        if len(set(vals)) >= 3: break
    else: raise AssertionError
    ft = 'x^3-%dx' % (3 * p * p) if p > 1 else 'x^3-3x'
    return dict(en='Let \\(M\\), \\(m\\) be the largest and smallest values of \\(f(x)=%s\\) on \\([%d;\\,%d]\\). Then \\(M+m=\\)…' % (ft, lo, hi),
                vi='Gọi \\(M\\), \\(m\\) là giá trị lớn nhất và nhỏ nhất của hàm số \\(f(x)=%s\\) trên đoạn \\([%d;\\,%d]\\). Khi đó \\(M+m=\\)' % (ft, lo, hi),
                opts=nopts(r, M + m, [f(lo) + f(hi), 2 * p ** 3 - 2 * p ** 3, M - m, f(-p) + f(p) + 1]),
                ee='Critical points \\(x=\\pm%d\\); compare \\(%s\\): \\(M=%d\\), \\(m=%d\\), \\(M+m=%d\\).' % (p, ', '.join('f(%d)=%d' % (x, f(x)) for x in cand), M, m, M + m),
                ev='Điểm tới hạn \\(x=\\pm%d\\); so sánh \\(%s\\): \\(M=%d\\), \\(m=%d\\), \\(M+m=%d\\).' % (p, ', '.join('f(%d)=%d' % (x, f(x)) for x in cand), M, m, M + m))

D2 = [m2_graph, m2_vt, m2_trig, m2_sqrt, m2_param, m2_explog, m2_visitors, m2_sum]

# =============================================================== Bài 3 – Đường tiệm cận
def hom(a, b, c, d):
    """(ax+b)/(cx+d) → TeX."""
    def lin(p, q):
        if p == 0: return str(q)
        s = ('' if p == 1 else '-' if p == -1 else str(p)) + 'x'
        return s + ('' if q == 0 else ('+%d' % q if q > 0 else str(q)))
    return '\\dfrac{%s}{%s}' % (lin(a, b), lin(c, d))
def a3_graph(r, lv):
    for _ in range(300):
        c = r.choice([-2, -1, 1, 2]); k = r.choice([1, 2, -1, -2]); a = r.choice([1, 2, -1, -2]); b = k + a * c * 1
        # y = a + k/(x−c) = (a x + (k − a c))/(x − c)
        bb = k - a * c
        if a != 0 and k != 0 and abs(bb) <= 8: break
    f = lambda x: a + k / (x - c) if abs(x - c) > 1e-9 else None
    img = G.graph_svg([(f, G.GREEN)], (c - 4.2, c + 4.2), (a - 4.2, a + 4.2), [(c, str(c))] if c else [], [(a, str(a))] if a else [],
                      hlines=[(a, None)], vlines=[(c, None)], W=5.4, H=5.4)
    good = 'x=%d,\\ y=%d' % (c, a); bad = ['x=%d,\\ y=%d' % (a, c), 'x=%d,\\ y=%d' % (-c, a), 'x=%d,\\ y=%d' % (c, -a) if a != 0 else 'x=%d,\\ y=0' % c, 'x=%d,\\ y=%d' % (-c, -a)]
    return dict(en='The figure shows the graph of \\(y=f(x)\\) and its asymptotes (dashed). The asymptotes are…', vi='Hình vẽ là đồ thị của hàm số \\(y=f(x)\\) và các đường tiệm cận (nét đứt). Các đường tiệm cận là',
                opts=fo(good, bad), fig=G.FIG(img, 'Graph with asymptotes', 'Đồ thị và các đường tiệm cận', 300),
                ee='The vertical dashed line is \\(x=%d\\) (vertical asymptote), the horizontal one is \\(y=%d\\) (horizontal asymptote); here \\(f(x)=%s\\).' % (c, a, hom(a, bb, 1, -c)),
                ev='Đường nét đứt thẳng đứng là \\(x=%d\\) (tiệm cận đứng), đường nằm ngang là \\(y=%d\\) (tiệm cận ngang); ở đây \\(f(x)=%s\\).' % (c, a, hom(a, bb, 1, -c)))

def a3_vt(r, lv):
    kind = V(lv, ['std', 'two', 'half'])
    c = r.choice([-2, -1, 1, 2, 3]); L = r.choice([-2, -1, 1, 2, 3])
    if kind == 'std':
        pts = [dict(x='-\\infty', v=(str(L), 'top')), dict(x=str(c), bar=(('-\\infty', 'bot'), ('+\\infty', 'top'))), dict(x='+\\infty', v=(str(L), 'bot'))]; sg = ['-', '-']; n = 2
        ex_e, ex_v = 'vertical \\(x=%d\\) and horizontal \\(y=%d\\)' % (c, L), 'tiệm cận đứng \\(x=%d\\) và tiệm cận ngang \\(y=%d\\)' % (c, L)
    elif kind == 'two':
        L2 = L + r.choice([2, 3, -2]); pts = [dict(x='-\\infty', v=(str(L), 'bot')), dict(x=str(c), bar=(('+\\infty', 'top'), ('-\\infty', 'bot'))), dict(x='+\\infty', v=(str(L2), 'top'))]; sg = ['+', '+']; n = 3
        ex_e, ex_v = '\\(x=%d\\), \\(y=%d\\) and \\(y=%d\\)' % (c, L, L2), '\\(x=%d\\), \\(y=%d\\) và \\(y=%d\\)' % (c, L, L2)
    else:
        pts = [dict(x='-\\infty', v=(str(L), 'top')), dict(x=str(c), bar=(('-\\infty', 'bot'), ('-\\infty', 'bot'))), dict(x='+\\infty', v=('+\\infty', 'top'))]; sg = ['-', '+']; n = 2
        ex_e, ex_v = '\\(x=%d\\) and \\(y=%d\\) (only as \\(x\\to-\\infty\\))' % (c, L), '\\(x=%d\\) và \\(y=%d\\) (chỉ khi \\(x\\to-\\infty\\))' % (c, L)
    return dict(en='The variation table of \\(y=f(x)\\) is shown. How many asymptotes (vertical and horizontal) does its graph have?', vi='Cho bảng biến thiên của hàm số \\(y=f(x)\\). Đồ thị hàm số có tổng cộng bao nhiêu đường tiệm cận đứng và ngang?',
                opts=nopts(r, n, [1, 2, 3, 4, 0]), fig=VTFIG(pts, sg, fname="y'", gname='y'),
                ee='Read the limits: infinite limits at \\(x=%d\\) give a vertical asymptote; finite limits at \\(\\pm\\infty\\) give horizontal asymptotes. Here: %s.' % (c, ex_e),
                ev='Đọc các giới hạn: giới hạn vô cực tại \\(x=%d\\) cho tiệm cận đứng; giới hạn hữu hạn tại \\(\\pm\\infty\\) cho tiệm cận ngang. Ở đây: %s.' % (c, ex_v))

def a3_noVA(r, lv):
    for _ in range(200):
        p = r.choice([1, 2, 3, -1]); m = nz(r, -4, 4); q = p * m
        if q != 0: break
    # y = (p x + q)/(x + m) không có TCĐ khi tử triệt tiêu tại x = −m: −p m + q = 0
    return dict(en='For which \\(m\\) does the graph of \\(y=\\dfrac{%s}{x+m}\\) have no vertical asymptote?' % poly_tex(0, p, q), vi='Với giá trị nào của \\(m\\) thì đồ thị hàm số \\(y=\\dfrac{%s}{x+m}\\) không có tiệm cận đứng?' % poly_tex(0, p, q),
                opts=nopts(r, m, [-m, q, -q if -q != m else p, 0 if m != 0 else 1]),
                ee='No vertical asymptote when the numerator also vanishes at \\(x=-m\\): \\(%d(-m)%s=0\\Leftrightarrow m=%d\\) (then \\(y=%d\\) with \\(x\\ne%d\\)).' % (p, ('+%d' % q) if q > 0 else str(q), m, p, -m),
                ev='Không có tiệm cận đứng khi tử cũng bằng 0 tại \\(x=-m\\): \\(%d(-m)%s=0\\Leftrightarrow m=%d\\) (khi đó \\(y=%d\\) với \\(x\\ne%d\\)).' % (p, ('+%d' % q) if q > 0 else str(q), m, p, -m))

def a3_twoHA(r, lv):
    k = r.choice([1, 2, 3]); c = r.randint(-3, 3); s = r.choice([1, 4, 9])
    fx = '\\dfrac{%s}{\\sqrt{x^2+%d}}' % (poly_tex(0, k, c), s)
    return dict(en='The horizontal asymptotes of the graph of \\(y=%s\\) are…' % fx, vi='Các đường tiệm cận ngang của đồ thị hàm số \\(y=%s\\) là' % fx,
                opts=[tx('\\(y=%d\\) and \\(y=%d\\)' % (k, -k), '\\(y=%d\\) và \\(y=%d\\)' % (k, -k)), tx('only \\(y=%d\\)' % k, 'chỉ \\(y=%d\\)' % k), tx('only \\(y=0\\)', 'chỉ \\(y=0\\)'), tx('\\(y=%d\\) and \\(y=%d\\)' % (k * k, -k * k) if k > 1 else '\\(y=0\\) and \\(y=%d\\)' % k, '\\(y=%d\\) và \\(y=%d\\)' % (k * k, -k * k) if k > 1 else '\\(y=0\\) và \\(y=%d\\)' % k)],
                ee='\\(\\sqrt{x^2+%d}\\approx|x|\\): as \\(x\\to+\\infty\\), \\(y\\to%d\\); as \\(x\\to-\\infty\\), \\(|x|=-x\\) and \\(y\\to%d\\).' % (s, k, -k),
                ev='\\(\\sqrt{x^2+%d}\\approx|x|\\): khi \\(x\\to+\\infty\\), \\(y\\to%d\\); khi \\(x\\to-\\infty\\), \\(|x|=-x\\) nên \\(y\\to%d\\).' % (s, k, -k))

def a3_oblique(r, lv):
    for _ in range(200):
        s = nz(r, -4, 5); a = s - 1; b = r.randint(-5, 5)
        if a + b + 1 != 0: break
    return dict(en='The graph of \\(y=\\dfrac{x^2+ax%s}{x-1}\\) has the oblique asymptote \\(y=x%s\\). Then \\(a=\\)…' % (('+%d' % b) if b > 0 else (str(b) if b else ''), ('+%d' % s) if s > 0 else str(s)),
                vi='Đồ thị hàm số \\(y=\\dfrac{x^2+ax%s}{x-1}\\) có tiệm cận xiên \\(y=x%s\\). Khi đó \\(a=\\)' % (('+%d' % b) if b > 0 else (str(b) if b else ''), ('+%d' % s) if s > 0 else str(s)),
                opts=nopts(r, a, [s, s + 1, -a if -a != a else a + 2, s - b if s - b not in (a, s, s + 1) else a - 3]),
                ee='\\(\\dfrac{x^2+ax%s}{x-1}=x+(a+1)+\\dfrac{a%s}{x-1}\\), so the oblique asymptote is \\(y=x+a+1\\): \\(a+1=%d\\Rightarrow a=%d\\).' % (('+%d' % b) if b > 0 else (str(b) if b else ''), ('+%d' % (b + 1)) if b + 1 > 0 else (str(b + 1) if b + 1 else ''), s, a),
                ev='\\(\\dfrac{x^2+ax%s}{x-1}=x+(a+1)+\\dfrac{a%s}{x-1}\\), nên tiệm cận xiên là \\(y=x+a+1\\): \\(a+1=%d\\Rightarrow a=%d\\).' % (('+%d' % b) if b > 0 else (str(b) if b else ''), ('+%d' % (b + 1)) if b + 1 > 0 else (str(b + 1) if b + 1 else ''), s, a))

def a3_cost(r, lv):
    p = r.choice([15, 20, 25, 40, 50]); Q = r.choice([2000, 5000, 12000, 30000])
    return dict(en='A workshop\'s average cost per product (thousand VND) for \\(x\\) products is \\(C(x)=\\dfrac{%dx+%d}{x}\\). When \\(x\\) becomes very large, \\(C(x)\\) gets close to…' % (p, Q),
                vi='Chi phí trung bình (nghìn đồng) cho mỗi sản phẩm khi xưởng sản xuất \\(x\\) sản phẩm là \\(C(x)=\\dfrac{%dx+%d}{x}\\). Khi \\(x\\) rất lớn, \\(C(x)\\) dần tới' % (p, Q),
                opts=nopts(r, p, [Q, p + Q, 0, Q // p if Q % p == 0 else Q // 100]),
                ee='\\(\\displaystyle\\lim_{x\\to+\\infty}C(x)=%d\\): the line \\(y=%d\\) is the horizontal asymptote — the fixed cost is shared among more and more products.' % (p, p),
                ev='\\(\\displaystyle\\lim_{x\\to+\\infty}C(x)=%d\\): đường \\(y=%d\\) là tiệm cận ngang — chi phí cố định được chia cho ngày càng nhiều sản phẩm.' % (p, p))

def a3_rect(r, lv):
    for _ in range(300):
        a, c = nz(r, -4, 4), r.choice([1, 2, -1]); d = nz(r, -6, 6); b = r.randint(-5, 5)
        if a * d - b * c != 0 and F(d, c).denominator == 1 and F(a, c).denominator == 1 and abs(F(a, c)) > 0: break
    S = abs(F(d, c)) * abs(F(a, c))
    return dict(en='The two asymptotes of the graph of \\(y=%s\\) and the two coordinate axes bound a rectangle. Its area is…' % hom(a, b, c, d),
                vi='Hai đường tiệm cận của đồ thị hàm số \\(y=%s\\) cùng hai trục tọa độ tạo thành một hình chữ nhật. Diện tích hình chữ nhật đó là' % hom(a, b, c, d),
                opts=nopts(r, S, [abs(F(b, d)) * abs(F(a, c)) if b else S + 2, abs(F(d, c)) + abs(F(a, c)), 2 * (abs(F(d, c)) + abs(F(a, c))), S / 2]),
                ee='Asymptotes \\(x=%s\\), \\(y=%s\\); the rectangle has sides \\(%s\\) and \\(%s\\): area \\(%s\\).' % (frt(F(-d, c)), frt(F(a, c)), frt(abs(F(d, c))), frt(abs(F(a, c))), ne(S)),
                ev='Tiệm cận \\(x=%s\\), \\(y=%s\\); hình chữ nhật có hai cạnh \\(%s\\) và \\(%s\\): diện tích \\(%s\\).' % (frt(F(-d, c)), frt(F(a, c)), frt(abs(F(d, c))), frt(abs(F(a, c))), nv(S)))

CON3 = [(('If \\(\\displaystyle\\lim_{x\\to2^+}f(x)=+\\infty\\), the line \\(x=2\\) is a vertical asymptote of the graph of \\(f\\)', 'Nếu \\(\\displaystyle\\lim_{x\\to2^+}f(x)=+\\infty\\) thì đường thẳng \\(x=2\\) là tiệm cận đứng của đồ thị \\(f\\)'), True),
        (('If \\(\\displaystyle\\lim_{x\\to-\\infty}f(x)=3\\), the line \\(y=3\\) is a horizontal asymptote of the graph of \\(f\\)', 'Nếu \\(\\displaystyle\\lim_{x\\to-\\infty}f(x)=3\\) thì đường thẳng \\(y=3\\) là tiệm cận ngang của đồ thị \\(f\\)'), True),
        (('A graph can cross its horizontal asymptote', 'Đồ thị có thể cắt tiệm cận ngang của nó'), True),
        (('If \\(f(2)\\) is not defined, \\(x=2\\) is a vertical asymptote', 'Nếu \\(f(2)\\) không xác định thì \\(x=2\\) là tiệm cận đứng'), False),
        (('The graph of a polynomial of degree 3 has a horizontal asymptote', 'Đồ thị hàm đa thức bậc ba có tiệm cận ngang'), False),
        (('A graph has at most one horizontal asymptote', 'Đồ thị có nhiều nhất một tiệm cận ngang'), False),
        (('A graph can cross its vertical asymptote', 'Đồ thị có thể cắt tiệm cận đứng của nó'), False),
        (('\\(y=\\dfrac{x^2-1}{x-1}\\) has the vertical asymptote \\(x=1\\)', '\\(y=\\dfrac{x^2-1}{x-1}\\) có tiệm cận đứng \\(x=1\\)'), False)]
def a3_concept(r, lv):
    g = r.choice([c for c in CON3 if c[1]]); b = r.sample([c for c in CON3 if not c[1]], 3)
    W = lambda c: tx(c[0][0], c[0][1])
    q = V(lv, [('Which statement is true?', 'Khẳng định nào đúng?'), ('Which statement about asymptotes is correct?', 'Khẳng định nào về đường tiệm cận là đúng?'), ('Exactly one statement is true. Which one?', 'Chỉ có một khẳng định đúng. Đó là khẳng định nào?')])
    return dict(en=q[0], vi=q[1], opts=[W(g)] + [W(x) for x in b],
                ee='Asymptotes come from limits: a vertical one needs an infinite one-sided limit, a horizontal one a finite limit at \\(\\pm\\infty\\) (there can be two, and the graph may cross it). A hole is not an asymptote; polynomials have no asymptotes.',
                ev='Tiệm cận đến từ giới hạn: tiệm cận đứng cần một giới hạn một bên vô cực, tiệm cận ngang cần giới hạn hữu hạn tại \\(\\pm\\infty\\) (có thể có hai, và đồ thị có thể cắt nó). Điểm hổng không phải tiệm cận; đa thức không có tiệm cận.')

D3 = [a3_graph, a3_vt, a3_noVA, a3_twoHA, a3_oblique, a3_cost, a3_rect, a3_concept]

# =============================================================== Bài 4 – Khảo sát và vẽ đồ thị
def cub_graph(C, extra_ticks=()):
    p, q, f = C['p'], C['q'], C['f']
    lo_x, hi_x = p - 1.15, q + 1.15
    ys = [float(f(F(x).limit_denominator(100))) for x in (lo_x, hi_x, p, q, 0)]
    lo, hi = min(ys + [0]) - .4, max(ys + [0]) + .4
    if hi - lo > 16: raise AssertionError
    yt = ticks_for([f(p), f(q), f(0)] + list(extra_ticks), lo, hi)
    return G.graph_svg([(lambda x: float(f(F(x).limit_denominator(1000))), G.GREEN)], (min(lo_x, -1.2), max(hi_x, 1.2)), (lo, hi), ticks_for([p, q], -9, 9), yt,
                       dots=[(p, f(p), False), (q, f(q), False)] + ([(0, f(0), False)] if 0 not in (p, q) else []), W=6.0, H=4.4)
def s4_identify(r, lv):
    C = cubic_from(r); s, p, q, d = C['s'], C['p'], C['q'], C['d']
    b, c = -s * F(3 * (p + q), 2), s * 3 * p * q
    good = 'y=' + poly_tex3(s, b, c, d)
    bads = ['y=' + poly_tex3(-s, -b, -c, d), 'y=' + poly_tex3(s, b, c, -d) if d else 'y=' + poly_tex3(s, b, c, 2), 'y=' + poly_tex3(s, -b, c, d) if b else 'y=' + poly_tex3(s, b, -c, d)]
    return dict(en='Which function has the graph shown in the figure?', vi='Đồ thị trong hình là của hàm số nào?',
                opts=fo(good, bads), fig=G.FIG(cub_graph(C), 'Graph of a cubic', 'Đồ thị hàm bậc ba', 320),
                ee='Check the shape (\\(a%s0\\)), the point on \\(Oy\\) \\((0;%s)\\) and the turning points \\(x=%d\\), \\(x=%d\\): only \\(%s\\) fits.' % ('\\gt' if s > 0 else '\\lt', frt(d), p, q, good),
                ev='Xét dáng đồ thị (\\(a%s0\\)), giao điểm với \\(Oy\\) là \\((0;%s)\\) và các điểm cực trị \\(x=%d\\), \\(x=%d\\): chỉ \\(%s\\) phù hợp.' % ('\\gt' if s > 0 else '\\lt', frt(d), p, q, good))

def s4_rational(r, lv):
    for _ in range(300):
        c = r.choice([-2, -1, 1, 2]); a = r.choice([-2, -1, 1, 2]); k = r.choice([1, 2, 3, -1, -2, -3]); bb = k - a * c
        if abs(bb) <= 8 and a != -c: break
    good = 'y=' + hom(a, bb, 1, -c)
    f = lambda x: a + k / (x - c) if abs(x - c) > 1e-9 else None
    x0 = F(-bb, a); y0 = F(bb, -c)
    img = G.graph_svg([(f, G.GREEN)], (c - 4.2, c + 4.2), (a - 4.2, a + 4.2), [(c, str(c))] + ([(x0, frt(x0))] if x0 != 0 and abs(x0 - c) > .6 and abs(x0 - c) < 4 else []),
                      [(a, str(a))] + ([(y0, frt(y0))] if y0 != 0 and abs(y0 - a) > .6 and abs(y0 - a) < 4 else []), hlines=[(a, None)], vlines=[(c, None)],
                      dots=[(x0, 0, False)] if abs(x0 - c) < 4 else [], W=5.4, H=5.4)
    bads = ['y=' + hom(a, bb, 1, c), 'y=' + hom(-c, bb, 1, -a) if (-c, -a) != (a, c) else 'y=' + hom(a, -bb, 1, -c), 'y=' + hom(a, a * c - k, 1, -c)]
    return dict(en='The figure shows the graph of a function and its asymptotes (dashed). Which function is it?', vi='Hình vẽ là đồ thị của một hàm số và các đường tiệm cận (nét đứt). Đó là hàm số nào?',
                opts=fo(good, bads), fig=G.FIG(img, 'Graph of a rational function', 'Đồ thị hàm phân thức', 300),
                ee='Asymptotes \\(x=%d\\), \\(y=%d\\) and the branches %s: \\(%s\\).' % (c, a, 'lie top-right and bottom-left' if k > 0 else 'lie top-left and bottom-right', good),
                ev='Tiệm cận \\(x=%d\\), \\(y=%d\\) và hai nhánh %s: \\(%s\\).' % (c, a, 'nằm ở góc trên phải và dưới trái' if k > 0 else 'nằm ở góc trên trái và dưới phải', good))

def s4_signs(r, lv):
    C = cubic_from(r); s, d = C['s'], C['d']
    if d == 0: raise AssertionError
    combos = [(sa, sd) for sa in ('\\gt', '\\lt') for sd in ('\\gt', '\\lt')]; g = ('\\gt' if s > 0 else '\\lt', '\\gt' if d > 0 else '\\lt')
    opts = ['a%s0,\\ d%s0' % g] + ['a%s0,\\ d%s0' % c for c in combos if c != g]
    return dict(en='The figure shows the graph of \\(y=ax^3+bx^2+cx+d\\). Which is true?', vi='Hình vẽ là đồ thị hàm số \\(y=ax^3+bx^2+cx+d\\). Khẳng định nào đúng?',
                opts=opts, fig=G.FIG(cub_graph(C), 'Graph of a cubic', 'Đồ thị hàm bậc ba', 320),
                ee='The right-hand branch goes %s, so \\(a%s0\\); the graph meets \\(Oy\\) at \\((0;d)\\) %s \\(Ox\\), so \\(d%s0\\).' % ('up' if s > 0 else 'down', g[0], 'above' if d > 0 else 'below', g[1]),
                ev='Nhánh bên phải đi %s nên \\(a%s0\\); đồ thị cắt \\(Oy\\) tại \\((0;d)\\) nằm %s \\(Ox\\) nên \\(d%s0\\).' % ('lên' if s > 0 else 'xuống', g[0], 'trên' if d > 0 else 'dưới', g[1]))

def s4_mrange(r, lv):
    C = cubic_from(r); f, p, q = C['f'], C['p'], C['q']; lo, hi = sorted([f(p), f(q)])
    good = '(%s;\\,%s)' % (frt(lo), frt(hi)); bads = ['[%s;\\,%s]' % (frt(lo), frt(hi)), '(%d;\\,%d)' % (p, q), '(%s;\\,+\\infty)' % frt(lo)]
    return dict(en='The figure shows the graph of \\(y=f(x)\\). For which values of \\(m\\) does \\(f(x)=m\\) have three distinct solutions?', vi='Hình vẽ là đồ thị hàm số \\(y=f(x)\\). Với những giá trị nào của \\(m\\) thì phương trình \\(f(x)=m\\) có ba nghiệm phân biệt?',
                opts=fo(good, bads), fig=G.FIG(cub_graph(C), 'Graph of a cubic', 'Đồ thị hàm bậc ba', 320),
                ee='The line \\(y=m\\) cuts the graph three times exactly when it lies strictly between the extreme values \\(%s\\) and \\(%s\\).' % (frt(lo), frt(hi)),
                ev='Đường thẳng \\(y=m\\) cắt đồ thị tại ba điểm khi và chỉ khi nó nằm giữa (không trùng) hai giá trị cực trị \\(%s\\) và \\(%s\\).' % (frt(lo), frt(hi)))

def s4_count(r, lv):
    C = cubic_from(r); f, p, q = C['f'], C['p'], C['q']; lo, hi = sorted([f(p), f(q)])
    k = r.choice([2, 3]); t = r.choice([lo - 1, lo, (lo + hi) / 2, hi, hi + 1]); c = -k * t
    n = 3 if lo < t < hi else 2 if t in (lo, hi) else 1
    eq = '%df(x)%s=0' % (k, ('+%s' % frt(c)) if c > 0 else ('-%s' % frt(-c)) if c else '')
    return dict(en='The figure shows the graph of \\(y=f(x)\\). How many real solutions does \\(%s\\) have?' % eq, vi='Hình vẽ là đồ thị hàm số \\(y=f(x)\\). Phương trình \\(%s\\) có bao nhiêu nghiệm thực?' % eq,
                opts=nopts(r, n, [1, 2, 3, 0]), fig=G.FIG(cub_graph(C), 'Graph of a cubic', 'Đồ thị hàm bậc ba', 320),
                ee='\\(%s\\Leftrightarrow f(x)=%s\\); the line \\(y=%s\\) meets the graph at \\(%d\\) point(s).' % (eq, frt(t), frt(t), n),
                ev='\\(%s\\Leftrightarrow f(x)=%s\\); đường thẳng \\(y=%s\\) cắt đồ thị tại \\(%d\\) điểm.' % (eq, frt(t), frt(t), n))

def s4_quartic(r, lv):
    a = r.choice([1, 2, 3]); c = r.randint(-3, 4)
    fx = 'y=x^4-%dx^2%s' % (2 * a * a, ('+%d' % c) if c > 0 else (str(c) if c else ''))
    S = a ** 5
    return dict(en='The three extreme points of the graph of \\(%s\\) form a triangle. Its area is…' % fx, vi='Ba điểm cực trị của đồ thị hàm số \\(%s\\) tạo thành một tam giác. Diện tích tam giác đó là' % fx,
                opts=nopts(r, S, [2 * S, a ** 4, a ** 3, S + a * a]),
                ee="\\(y'=4x(x^2-%d)\\): points \\((0;%d)\\), \\((\\pm%d;%d)\\). Base \\(%d\\), height \\(%d\\): area \\(\\dfrac12\\cdot%d\\cdot%d=%d\\)." % (a * a, c, a, c - a ** 4, 2 * a, a ** 4, 2 * a, a ** 4, S),
                ev="\\(y'=4x(x^2-%d)\\): các điểm \\((0;%d)\\), \\((\\pm%d;%d)\\). Đáy \\(%d\\), chiều cao \\(%d\\): diện tích \\(\\dfrac12\\cdot%d\\cdot%d=%d\\)." % (a * a, c, a, c - a ** 4, 2 * a, a ** 4, 2 * a, a ** 4, S))

def s4_vt_identify(r, lv):
    C = cubic_from(r); p, q, s, f, d = C['p'], C['q'], C['s'], C['f'], C['d']
    up = s > 0
    pts = [dict(x='-\\infty', v=('-\\infty' if up else '+\\infty', 'bot' if up else 'top')), dict(x=frt(p), v=(frt(f(p)), 'top' if up else 'bot'), z=True),
           dict(x=frt(q), v=(frt(f(q)), 'bot' if up else 'top'), z=True), dict(x='+\\infty', v=('+\\infty' if up else '-\\infty', 'top' if up else 'bot'))]
    b, c = -s * F(3 * (p + q), 2), s * 3 * p * q
    good = 'y=' + poly_tex3(s, b, c, d)
    alt = cubic_from(r)
    bads = ['y=' + poly_tex3(-s, -b, -c, d), 'y=' + poly_tex3(s, b, c, d + 2), 'y=' + poly_tex3(s, b, -c if c else 3, d)]
    return dict(en='Which function has the variation table shown?', vi='Bảng biến thiên trong hình là của hàm số nào?',
                opts=fo(good, bads), fig=VTFIG(pts, ['+', '-', '+'] if up else ['-', '+', '-'], fname="y'", gname='y'),
                ee='The table needs \\(y\'=0\\) at \\(x=%d\\), \\(x=%d\\), the right sign of \\(a\\) and the values \\(%s\\), \\(%s\\): only \\(%s\\) fits.' % (p, q, frt(f(p)), frt(f(q)), good),
                ev='Bảng cần \\(y\'=0\\) tại \\(x=%d\\), \\(x=%d\\), dấu của \\(a\\) phù hợp và các giá trị \\(%s\\), \\(%s\\): chỉ \\(%s\\) phù hợp.' % (p, q, frt(f(p)), frt(f(q)), good))

def s4_intersect(r, lv):
    for _ in range(300):
        rr = r.sample(range(-3, 4), 2); dbl = r.random() < .4
        roots = [rr[0], rr[0], rr[1]] if dbl else sorted(r.sample(range(-3, 4), 3))
        S = sum(roots); P2 = roots[0] * roots[1] + roots[0] * roots[2] + roots[1] * roots[2]; P3 = roots[0] * roots[1] * roots[2]
        # x³ − S x² + P2 x − P3 = 0  ⇔  x³ − S x² = −P2 x + P3
        if S != 0 and (P2 != 0 or P3 != 0): break
    n = len(set(roots))
    curve = 'y=' + poly_tex3(1, -S, 0, 0); line = 'y=' + poly_tex(0, -P2, P3)
    return dict(en='How many points do the graphs of \\(%s\\) and \\(%s\\) have in common?' % (curve, line), vi='Đồ thị hàm số \\(%s\\) và đường thẳng \\(%s\\) có bao nhiêu điểm chung?' % (curve, line),
                opts=nopts(r, n, [3, 2, 1, 0]),
                ee='Solve \\(%s=%s\\Leftrightarrow %s=0\\), whose roots are \\(%s\\): \\(%d\\) common point(s).' % (poly_tex3(1, -S, 0, 0), poly_tex(0, -P2, P3), poly_tex3(1, -S, P2, -P3), ', '.join(str(x) for x in sorted(set(roots))), n),
                ev='Giải \\(%s=%s\\Leftrightarrow %s=0\\), có nghiệm \\(%s\\): \\(%d\\) điểm chung.' % (poly_tex3(1, -S, 0, 0), poly_tex(0, -P2, P3), poly_tex3(1, -S, P2, -P3), ', '.join(str(x) for x in sorted(set(roots))), n))

D4 = [s4_identify, s4_rational, s4_signs, s4_mrange, s4_count, s4_quartic, s4_vt_identify, s4_intersect]

# ---------------------------------------------------------------- dùng trong bài (đánh số tiếp, giữ chữ cái mục)
def adapt(b):
    """Hàm sinh (r, lv) → (r, lv, ctx) cho with_d."""
    def w(r, lv, ctx): return b(r, lv)
    w.__name__ = b.__name__; return w
REPH = [('en', r'^The figure shows', {2: 'The figure below shows', 3: 'Look at the figure. It shows'}),
        ('en', r'^The variation table of (.*?) is shown\.', {2: r'Here is the variation table of \1.', 3: r'Use the variation table of \1 below.'}),
        ('en', r'^Which function has the graph shown in the figure\?', {2: 'The figure shows the graph of which function?', 3: 'Which of the following functions is drawn in the figure?'}),
        ('en', r'^Which function has the variation table shown\?', {2: 'The variation table belongs to which function?', 3: 'Which of the following functions has this variation table?'}),
        ('vi', r'^Hình vẽ là', {2: 'Hình vẽ dưới đây là', 3: 'Quan sát hình vẽ: đây là'}),
        ('vi', r'^Cho bảng biến thiên của', {2: 'Dưới đây là bảng biến thiên của', 3: 'Dựa vào bảng biến thiên của'}),
        ('vi', r'^Đồ thị trong hình là của hàm số nào\?', {2: 'Hình vẽ là đồ thị của hàm số nào?', 3: 'Hàm số nào sau đây có đồ thị như hình vẽ?'}),
        ('vi', r'^Bảng biến thiên trong hình là của hàm số nào\?', {2: 'Hàm số nào có bảng biến thiên như hình?', 3: 'Bảng biến thiên đã cho là của hàm số nào sau đây?'})]
def rephrase(q, lv):
    """Lời dẫn câu đọc hình/bảng đổi theo mức để đề các mức không trùng nhau."""
    import re as _re
    q = dict(q)
    for k, pat, rep in REPH:
        if lv in rep: q[k] = _re.sub(pat, rep[lv], q[k], count=1)
    return q
def dset(practice, D, seeds):
    """Phần D theo mức (dict lv → danh sách câu) để gắn vào bài có cách ghép mục riêng.
    Hai câu được coi là trùng khi trùng cả đề lẫn hình (câu đọc hình có thể cùng lời dẫn nhưng khác hình)."""
    import html as _h
    from sp_g11r import _fig
    from mb_lib import MCQ
    old = ''.join(''.join(g[1]) for g in practice); used = set(); out = {}
    for lv, seed in zip((1, 2, 3), seeds):
        r = random.Random(seed); n = 1 + sum(len(g[1]) for g in practice if g[2] == [lv]); items = []
        for b in D:
            for _ in range(500):
                try: q = b(r, lv)
                except AssertionError: continue
                q = rephrase(q, lv); k = q['en']
                if k in used or ('fig' not in q and _h.escape(q['en'], quote=False) in old) or len(set(q['opts'])) != 4: continue
                break
            else: raise RuntimeError('không sinh được câu: ' + b.__name__)
            used.add(k); en, vi = _fig(q)
            opts = list(q['opts']); good = opts[0]; idx = list(range(4)); r.shuffle(idx); shf = [opts[i] for i in idx]; L = 'abcd'[shf.index(good)]
            items.append(MCQ(n, (en, vi), shf, L, ('Answer: %s. %s' % (L, q['ee']), 'Đáp án %s. %s' % (L, q['ev'])))); n += 1
        out[lv] = items
    return out
