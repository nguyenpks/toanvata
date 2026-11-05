# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 10 – Bài 4 (hệ BPT), Bài 5 (GTLG 0°–180°), Bài 6 (hệ thức lượng). Đáp án do máy tính."""
import math
from fractions import Fraction as F
from mb_selfpractice import *
from mb_quick import vertices

def _sys(r, lv, ge=False):
    while True:
        s = r.randint(4, 6 + lv); a = r.choice([2, 3, 4]); b = r.choice([1, 2]); x0 = r.randint(1, s - 1); y0 = s - x0
        c = a * x0 + b * y0
        if c > a * s or c <= b * s - 0 and False: continue
        if a * s >= c >= b * s and a != b: return s, a, b, c
def _tex(a, b, op, c): return '%s%s%s' % (lin(a, 0, 'x') + ('+%sy' % ('' if b == 1 else b)), op, c)

def sy_point(r, lv):
    s, a, b, c = _sys(r, lv); cons = [(-1, 0, 0), (0, -1, 0), (1, 1, s), (a, b, c)]
    ok = lambda p: all(u * p[0] + v * p[1] <= w for u, v, w in cons)
    pts = [(x, y) for x in range(-1, s + 3) for y in range(-1, s + 3)]
    good = [p for p in pts if ok(p) and p[0] > 0 and p[1] > 0]; bad = [p for p in pts if not ok(p) and p[0] >= 0 and p[1] >= 0]
    g = r.choice(good); w = r.sample(bad, 3)
    f = lambda p: '(%d;%d)' % p
    sysx = '\\begin{cases}x\\ge0,\\ y\\ge0\\\\ x+y\\le%d\\\\ %s\\le%d\\end{cases}' % (s, lin(a, 0, 'x') + '+' + ('' if b == 1 else str(b)) + 'y', c)
    return dict(en='Which pair is a solution of the system \\(%s\\)?' % sysx, vi='Cặp số nào là nghiệm của hệ \\(%s\\)?' % sysx, opts=[f(g)] + [f(p) for p in w], ans=0,
      ee='Substitute into every inequality; only %s satisfies all of them.' % f(g), ev='Thay vào từng bất phương trình; chỉ %s thỏa mãn cả hệ.' % f(g))

def sy_vertex(r, lv):
    s, a, b, c = _sys(r, lv)
    x = F(c - b * s, a - b); y = s - x
    t = lambda p, q: '(%s;%s)' % (fr(p), fr(q))
    return dict(en='The lines \\(x+y=%d\\) and \\(%s=%d\\) meet at which point?' % (s, lin(a, 0, 'x') + '+' + ('' if b == 1 else str(b)) + 'y', c),
      vi='Hai đường thẳng \\(x+y=%d\\) và \\(%s=%d\\) cắt nhau tại điểm nào?' % (s, lin(a, 0, 'x') + '+' + ('' if b == 1 else str(b)) + 'y', c),
      opts=pick_opts(r, t(x, y), [t(y, x), t(x + 1, y - 1), t(x - 1, y + 1), t(s - x + 1, x)], fill=lambda k: t(x + k, y + 2 * k)), ans=0,
      ee='Subtract the equations and solve: \\(x=%s\\), \\(y=%s\\).' % (fr(x), fr(y)), ev='Giải hệ hai phương trình: \\(x=%s\\), \\(y=%s\\).' % (fr(x), fr(y)))

def sy_opt(r, lv, mx=True):
    while True:
        s, a, b, c = _sys(r, lv); p = r.randint(1, 5); q = r.randint(1, 5)
        cons = [(-1, 0, 0), (0, -1, 0), (1, 1, s), (a, b, c)]; V = vertices(cons); vals = sorted({p * x + q * y for x, y in V})
        if len(vals) >= 4: break
    best = vals[-1]; others = vals[:-1]
    f = lambda t: str(t)
    return dict(en='On the region of \\(\\begin{cases}x\\ge0,\\ y\\ge0\\\\ x+y\\le%d\\\\ %s\\le%d\\end{cases}\\), what is the largest value of \\(F=%s\\)?' % (s, lin(a, 0, 'x') + '+' + ('' if b == 1 else str(b)) + 'y', c, lin(p, 0, 'x') + '+' + ('' if q == 1 else str(q)) + 'y'),
      vi='Trên miền nghiệm của hệ \\(\\begin{cases}x\\ge0,\\ y\\ge0\\\\ x+y\\le%d\\\\ %s\\le%d\\end{cases}\\), giá trị lớn nhất của \\(F=%s\\) là bao nhiêu?' % (s, lin(a, 0, 'x') + '+' + ('' if b == 1 else str(b)) + 'y', c, lin(p, 0, 'x') + '+' + ('' if q == 1 else str(q)) + 'y'),
      opts=[f(best)] + [f(v) for v in others[-3:]], ans=0, ee='Compute \\(F\\) at the vertices; the largest value is %d.' % best, ev='Tính \\(F\\) tại các đỉnh; giá trị lớn nhất là %d.' % best)

def sy_min(r, lv):
    while True:
        a = r.choice([2, 3, 4]); b = r.choice([1, 2, 3]); c = r.choice([12, 18, 24]); u = r.choice([1, 2]); v = r.choice([3, 4, 6]); w = r.choice([12, 18, 24])
        p = r.randint(2, 5); q = r.randint(2, 5)
        cons = [(-1, 0, 0), (0, -1, 0), (-a, -b, -c), (-u, -v, -w)]     # ax+by>=c, ux+vy>=w
        V = vertices(cons)
        if len(V) >= 3: break
    vals = sorted({p * x + q * y for x, y in V}); mn = vals[0]
    t = lambda a_, b_: lin(a_, 0, 'x') + '+' + ('' if b_ == 1 else str(b_)) + 'y'
    return dict(en='Find the smallest value of \\(F=%s\\) on the region \\(x\\ge0,\\ y\\ge0,\\ %s\\ge%d,\\ %s\\ge%d\\).' % (t(p, q), t(a, b), c, t(u, v), w),
      vi='Tìm giá trị nhỏ nhất của \\(F=%s\\) trên miền \\(x\\ge0,\\ y\\ge0,\\ %s\\ge%d,\\ %s\\ge%d\\).' % (t(p, q), t(a, b), c, t(u, v), w),
      opts=pick_opts(r, fr(mn), [fr(x) for x in vals[1:]] + [fr(mn + 1), fr(mn + 2)], fill=lambda k: fr(mn + 3 + k)), ans=0, ee='The smallest value is at a vertex: %s.' % fr(mn), ev='Giá trị nhỏ nhất đạt tại một đỉnh: %s.' % fr(mn))

def sy_count(r, lv):
    s, a, b, c = _sys(r, lv)
    n = sum(1 for x in range(0, s + 1) for y in range(0, s + 1) if x + y <= s and a * x + b * y <= c)
    return dict(en='How many pairs of natural numbers \\((x;y)\\) satisfy \\(x+y\\le%d\\) and \\(%s\\le%d\\)?' % (s, lin(a, 0, 'x') + '+' + ('' if b == 1 else str(b)) + 'y', c),
      vi='Có bao nhiêu cặp số tự nhiên \\((x;y)\\) thỏa \\(x+y\\le%d\\) và \\(%s\\le%d\\)?' % (s, lin(a, 0, 'x') + '+' + ('' if b == 1 else str(b)) + 'y', c),
      opts=pick_opts(r, str(n), [str(n + 1), str(n - 1), str(n + 2), str(n - 2)]), ans=0, ee='List the pairs for each \\(x\\) and add: %d pairs.' % n, ev='Liệt kê theo từng \\(x\\) rồi cộng lại: %d cặp.' % n)

def sy_model(r, lv):
    a = r.choice([2, 3, 4]); b = r.choice([1, 2, 5]); c = r.choice([40, 60, 80]); m = r.choice([6, 8, 10])
    right = '\\begin{cases}x\\ge0,\\ y\\ge0\\\\ %dx+%dy\\le%d\\\\ x+y\\le%d\\end{cases}' % (a, b, c, m)
    wrong = ['\\begin{cases}x\\ge0,\\ y\\ge0\\\\ %dx+%dy\\ge%d\\\\ x+y\\le%d\\end{cases}' % (a, b, c, m), '\\begin{cases}x\\ge0,\\ y\\ge0\\\\ %dx+%dy\\le%d\\\\ x+y\\ge%d\\end{cases}' % (a, b, c, m), '\\begin{cases}x\\ge0,\\ y\\ge0\\\\ %dx+%dy\\le%d\\\\ x+y\\le%d\\end{cases}' % (b, a, c, m)]
    return dict(en='A workshop makes \\(x\\) chairs and \\(y\\) tables. A chair needs %d hours and a table needs %d hours. There are at most %d hours, and at most %d items can be made. Which system describes this?' % (a, b, c, m),
      vi='Một xưởng làm \\(x\\) cái ghế và \\(y\\) cái bàn. Mỗi ghế cần %d giờ, mỗi bàn cần %d giờ. Xưởng có nhiều nhất %d giờ và làm nhiều nhất %d sản phẩm. Hệ bất phương trình nào mô tả điều đó?' % (a, b, c, m),
      opts=[right] + wrong, ans=0, ee='Time: \\(%dx+%dy\\le%d\\). Items: \\(x+y\\le%d\\). Also \\(x,y\\ge0\\).' % (a, b, c, m), ev='Thời gian: \\(%dx+%dy\\le%d\\). Số sản phẩm: \\(x+y\\le%d\\). Và \\(x,y\\ge0\\).' % (a, b, c, m))

B4 = [sy_point, sy_vertex, sy_opt, sy_min, sy_count, sy_model, sy_opt, sy_point]

# ---------- Bài 5: giá trị lượng giác của góc từ 0° đến 180° ----------
import trigval as TV
FN = {'sin': '\\sin', 'cos': '\\cos', 'tan': '\\tan', 'cot': '\\cot'}
def tg_special(r, lv):
    while True:
        fn = r.choice(['sin', 'cos', 'tan', 'cot']); a = r.choice([30, 45, 60, 120, 135, 150])
        v = TV.val(fn, a)
        if v: break
    pool = list(dict.fromkeys(TV.val(f, b) for f in FN for b in (30, 45, 60, 120, 135, 150) if TV.val(f, b) and TV.val(f, b) != v))
    r.shuffle(pool)
    return dict(en='What is \\(%s %d^\\circ\\)?' % (FN[fn], a), vi='Giá trị của \\(%s %d^\\circ\\) là bao nhiêu?' % (FN[fn], a), opts=[v] + pool[:3], ans=0,
      ee='From the table of special values: \\(%s %d^\\circ=%s\\).' % (FN[fn], a, v), ev='Theo bảng giá trị đặc biệt: \\(%s %d^\\circ=%s\\).' % (FN[fn], a, v))

TRI = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29)]
def tg_cos_obtuse(r, lv):
    a, b, c = r.choice(TRI); a, b = (a, b) if r.random() < .5 else (b, a)
    t = lambda p, q: '%s' % fr(F(p, q))
    return dict(en='Angle \\(\\alpha\\) is obtuse and \\(\\sin\\alpha=\\dfrac{%d}{%d}\\). Find \\(\\cos\\alpha\\).' % (a, c), vi='Góc \\(\\alpha\\) tù và \\(\\sin\\alpha=\\dfrac{%d}{%d}\\). Tính \\(\\cos\\alpha\\).' % (a, c),
      opts=[fr(F(-b, c)), fr(F(b, c)), fr(F(-a, c)), fr(F(-b, a))], ans=0, ee='\\(\\cos^2\\alpha=1-\\sin^2\\alpha=\\dfrac{%d}{%d}\\), and \\(\\cos\\alpha\\lt0\\) for an obtuse angle: \\(\\cos\\alpha=-\\dfrac{%d}{%d}\\).' % (b * b, c * c, b, c),
      ev='\\(\\cos^2\\alpha=1-\\sin^2\\alpha=\\dfrac{%d}{%d}\\), góc tù nên \\(\\cos\\alpha\\lt0\\): \\(\\cos\\alpha=-\\dfrac{%d}{%d}\\).' % (b * b, c * c, b, c))

def tg_tan_expr(r, lv):
    t = r.randint(2, 7); p = r.choice([1, 2, 3]); q = r.choice([1, 2]); 
    while t * q == p: t += 1
    v = F(t * p + q, t * q - p) if False else F(p * t + 1, t - 1) if False else None
    # (sin + cos)/(sin - cos) với p,q: (t + 1)/(t - 1) chỉ khi hệ số 1; dùng dạng (a sin + b cos)/(c sin + d cos)
    a, b, c, d = r.choice([1, 2, 3]), r.choice([1, 2, 3]), 1, r.choice([-1, -2, 1, 2])
    if c * t + d == 0: t += 1
    v = F(a * t + b, c * t + d)
    den = '\\sin\\alpha%s' % ('%+d\\cos\\alpha' % d if abs(d) != 1 else ('+' if d > 0 else '-') + '\\cos\\alpha')
    num_ = '%s\\sin\\alpha+%s\\cos\\alpha' % ('' if a == 1 else a, '' if b == 1 else b)
    return dict(en='Given \\(\\tan\\alpha=%d\\), find \\(\\dfrac{%s}{%s}\\).' % (t, num_, den), vi='Cho \\(\\tan\\alpha=%d\\). Tính \\(\\dfrac{%s}{%s}\\).' % (t, num_, den),
      opts=pick_opts(r, fr(v), [fr(F(a * t - b, c * t + d)), fr(F(a * t + b, c * t - d)), fr(v + 1), fr(-v)], fill=lambda k: fr(v + k + 1)), ans=0,
      ee='Divide the numerator and the denominator by \\(\\cos\\alpha\\): \\(\\dfrac{%d\\cdot%d+%d}{%d+(%d)}=%s\\).' % (a, t, b, t, d, fr(v)), ev='Chia tử và mẫu cho \\(\\cos\\alpha\\): \\(\\dfrac{%d\\cdot%d+%d}{%d+(%d)}=%s\\).' % (a, t, b, t, d, fr(v)))

def tg_supp(r, lv):
    fn = r.choice(['sin', 'cos', 'tan', 'cot']); a = r.choice([20, 35, 40, 55, 65, 70, 80]); sign = {'sin': 1, 'cos': -1, 'tan': -1, 'cot': -1}[fn]
    target = TV.num(fn, 180 - a)
    show = lambda sg, g, x: '%s%s %d^\\circ' % ('-' if sg < 0 else '', FN[g], x)
    right = show(sign, fn, a); assert abs(sign * TV.num(fn, a) - target) < 1e-9
    wrong = []
    for sg in (1, -1):
        for g in FN:
            for x in (a, 180 - a):
                if abs(sg * TV.num(g, x) - target) > 1e-9: wrong.append(show(sg, g, x))
    wrong = list(dict.fromkeys(wrong)); r.shuffle(wrong)
    return dict(en='Simplify \\(%s(180^\\circ-%d^\\circ)\\).' % (FN[fn], a), vi='Rút gọn \\(%s(180^\\circ-%d^\\circ)\\).' % (FN[fn], a), opts=[right] + wrong[:3], ans=0,
      ee='For supplementary angles: \\(\\sin\\) is the same, \\(\\cos,\\tan,\\cot\\) change sign.', ev='Hai góc bù nhau: \\(\\sin\\) bằng nhau, \\(\\cos,\\tan,\\cot\\) đổi dấu.')

def tg_angle(r, lv):
    fn, a = r.choice([('sin', 30), ('sin', 45), ('sin', 60), ('cos', 120), ('cos', 135), ('cos', 150), ('tan', 135), ('tan', 150), ('tan', 120)])
    if fn == 'sin': ans = 180 - a; vtex = TV.val('sin', a)
    else: ans = a; vtex = TV.val(fn, a)
    cond = ' (obtuse angle)' if fn == 'sin' else ''
    condv = ' (góc tù)' if fn == 'sin' else ''
    opts = [ans] + [x for x in (30, 45, 60, 90, 120, 135, 150) if x != ans]
    r.shuffle(opts[1:]); o = [str(ans)] + [str(x) for x in opts[1:4]]
    return dict(en='Find the angle \\(\\alpha\\) with \\(\\%s\\alpha=%s\\)%s.' % (fn, vtex, cond), vi='Tìm góc \\(\\alpha\\) biết \\(\\%s\\alpha=%s\\)%s.' % (fn, vtex, condv),
      opts=[x + '^\\circ' for x in o], ans=0, ee='Use the table of special values: \\(\\alpha=%d^\\circ\\).' % ans, ev='Dùng bảng giá trị đặc biệt: \\(\\alpha=%d^\\circ\\).' % ans)

def tg_height(r, lv):
    L = r.choice([6, 8, 10, 12, 14, 16, 18, 20]); a = r.choice([30, 45, 60]); h = {30: F(L, 2), 45: F(L) * 0, 60: F(0)}[a] if a == 30 else None
    val = {30: '%s' % fr(F(L, 2)), 45: '\\dfrac{%d\\sqrt2}{2}' % L, 60: '%d\\sqrt3\\over 2' % L}[a]
    val = {30: fr(F(L, 2)), 45: '\\dfrac{%d\\sqrt2}{2}' % L, 60: '\\dfrac{%d\\sqrt3}{2}' % L}[a]
    wr = {30: [fr(F(L, 2)) for _ in range(0)]}
    wrong = ['%d\\cos %d^\\circ' % (L, 90 - a) if False else (fr(F(L * 3, 2)) if a == 30 else '%d\\sqrt3' % L), '%d' % L, '%d\\sqrt2' % L, '%s' % fr(F(L, 3)), '\\dfrac{%d\\sqrt3}{3}' % L]
    other = {30: ['\\dfrac{%d\\sqrt3}{2}' % L, '\\dfrac{%d\\sqrt2}{2}' % L], 45: ['\\dfrac{%d\\sqrt3}{2}' % L, fr(F(L, 2))], 60: [fr(F(L, 2)), '\\dfrac{%d\\sqrt2}{2}' % L]}[a]
    return dict(en='A ladder %d m long leans on a wall and makes an angle of \\(%d^\\circ\\) with the ground. How high does it reach (in metres)?' % (L, a), vi='Một chiếc thang dài %d m dựa vào tường, tạo với mặt đất góc \\(%d^\\circ\\). Thang chạm tường ở độ cao bao nhiêu mét?' % (L, a),
      opts=[val] + other + ['%d' % L], ans=0, ee='Height \\(=%d\\sin %d^\\circ=%s\\) m.' % (L, a, val), ev='Độ cao \\(=%d\\sin %d^\\circ=%s\\) m.' % (L, a, val))

B5 = [tg_special, tg_cos_obtuse, tg_tan_expr, tg_supp, tg_angle, tg_height, tg_special, tg_cos_obtuse]

# ---------- Bài 6: hệ thức lượng trong tam giác ----------
SIDE_CASES = [(5, 8, 60, 7), (8, 15, 60, 13), (3, 8, 60, 7), (3, 5, 120, 7), (5, 3, 120, 7), (7, 8, 120, 13), (5, 16, 120, 19), (6, 10, 120, 14)]
for a_, b_, g_, c_ in SIDE_CASES: assert abs(a_ * a_ + b_ * b_ - 2 * a_ * b_ * math.cos(math.radians(g_)) - c_ * c_) < 1e-9, (a_, b_, g_)
def tri_side(r, lv):
    a, b, g, c = r.choice(SIDE_CASES)
    return dict(en='In triangle \\(ABC\\), \\(AB=%d\\), \\(AC=%d\\) and \\(\\widehat{A}=%d^\\circ\\). Find \\(BC\\).' % (a, b, g), vi='Cho tam giác \\(ABC\\) có \\(AB=%d\\), \\(AC=%d\\), \\(\\widehat{A}=%d^\\circ\\). Tính \\(BC\\).' % (a, b, g),
      opts=pick_opts(r, str(c), [str(c + 1), str(c - 1), str(a + b), str(abs(a - b) + 1)], fill=lambda k: str(c + 2 + k)), ans=0, ee='\\(BC^2=%d^2+%d^2-2\\cdot%d\\cdot%d\\cos%d^\\circ=%d\\), so \\(BC=%d\\).' % (a, b, a, b, g, c * c, c),
      ev='\\(BC^2=%d^2+%d^2-2\\cdot%d\\cdot%d\\cos%d^\\circ=%d\\) nên \\(BC=%d\\).' % (a, b, a, b, g, c * c, c))
ANG_CASES = [(5, 7, 8, 60), (3, 7, 5, 120), (3, 5, 4, 90), (7, 13, 8, 120), (5, 5, 5, 60), (6, 10, 8, 90), (8, 7, 5, 60)]
for a_, b_, c_, A_ in ANG_CASES: assert abs((a_ * a_ + c_ * c_ - b_ * b_) / (2 * a_ * c_) - math.cos(math.radians(A_))) < 1e-9, (a_, b_, c_)
def tri_angle(r, lv):
    a, b, c, A = r.choice([x for x in ANG_CASES if x[3]])
    # góc đối cạnh b (cạnh thứ hai)
    cosv = F(a * a + c * c - b * b, 2 * a * c); ang = {F(1, 2): 60, F(-1, 2): 120, F(0): 90}[cosv]
    return dict(en='A triangle has sides \\(%d,\\ %d,\\ %d\\). Find the angle opposite the side of length \\(%d\\).' % (a, b, c, b), vi='Tam giác có ba cạnh \\(%d,\\ %d,\\ %d\\). Tính góc đối diện với cạnh dài \\(%d\\).' % (a, b, c, b),
      opts=['%d^\\circ' % x for x in [ang] + [y for y in (30, 45, 60, 90, 120, 150) if y != ang][:3]], ans=0, ee='\\(\\cos=\\dfrac{%d^2+%d^2-%d^2}{2\\cdot%d\\cdot%d}=%s\\), so the angle is \\(%d^\\circ\\).' % (a, c, b, a, c, fr(cosv), ang),
      ev='\\(\\cos=\\dfrac{%d^2+%d^2-%d^2}{2\\cdot%d\\cdot%d}=%s\\) nên góc bằng \\(%d^\\circ\\).' % (a, c, b, a, c, fr(cosv), ang))
def tri_area(r, lv):
    a = r.choice([6, 8, 10, 12, 14]); b = r.choice([5, 7, 9, 11, 13]); g = r.choice([30, 150])
    v = F(a * b, 4)
    return dict(en='In triangle \\(ABC\\), \\(AB=%d\\), \\(AC=%d\\) and \\(\\widehat{A}=%d^\\circ\\). Find the area.' % (a, b, g), vi='Tam giác \\(ABC\\) có \\(AB=%d\\), \\(AC=%d\\), \\(\\widehat{A}=%d^\\circ\\). Tính diện tích.' % (a, b, g),
      opts=pick_opts(r, fr(v), [fr(2 * v), fr(F(a * b, 2) * 3 / 2 if False else F(a * b, 8)), fr(v + 1), fr(v - 1)], fill=lambda k: fr(v + k + 1)), ans=0, ee='\\(S=\\dfrac12\\cdot%d\\cdot%d\\cdot\\sin%d^\\circ=%s\\).' % (a, b, g, fr(v)), ev='\\(S=\\dfrac12\\cdot%d\\cdot%d\\cdot\\sin%d^\\circ=%s\\).' % (a, b, g, fr(v)))
HERON = [(3, 4, 5, 6), (5, 5, 6, 12), (13, 14, 15, 84), (5, 12, 13, 30), (6, 25, 29, 60), (9, 10, 17, 36), (7, 15, 20, 42), (8, 15, 17, 60), (10, 13, 13, 60)]
for a_, b_, c_, S_ in HERON:
    p_ = (a_ + b_ + c_) / 2; assert abs(math.sqrt(p_ * (p_ - a_) * (p_ - b_) * (p_ - c_)) - S_) < 1e-9, (a_, b_, c_)
def tri_heron(r, lv):
    a, b, c, S = r.choice(HERON)
    return dict(en='Find the area of the triangle with sides \\(%d,\\ %d,\\ %d\\).' % (a, b, c), vi='Tính diện tích tam giác có ba cạnh \\(%d,\\ %d,\\ %d\\).' % (a, b, c),
      opts=pick_opts(r, str(S), [str(S + 2), str(S - 2), str(S * 2), str(S + 6)], fill=lambda k: str(S + 10 + k)), ans=0, ee='Heron: \\(p=%s\\), \\(S=\\sqrt{p(p-a)(p-b)(p-c)}=%d\\).' % (fr(F(a + b + c, 2)), S), ev='Công thức Heron: \\(p=%s\\), \\(S=\\sqrt{p(p-a)(p-b)(p-c)}=%d\\).' % (fr(F(a + b + c, 2)), S))
def tri_sine(r, lv):
    a = r.choice([6, 8, 10, 12, 14, 16, 18, 20, 22]); A, B = r.choice([(30, 90), (90, 30)])
    b = a * 2 if (A, B) == (30, 90) else a // 2
    return dict(en='In triangle \\(ABC\\), \\(a=BC=%d\\), \\(\\widehat{A}=%d^\\circ\\) and \\(\\widehat{B}=%d^\\circ\\). Find \\(b=CA\\).' % (a, A, B), vi='Tam giác \\(ABC\\) có \\(a=BC=%d\\), \\(\\widehat{A}=%d^\\circ\\), \\(\\widehat{B}=%d^\\circ\\). Tính \\(b=CA\\).' % (a, A, B),
      opts=pick_opts(r, str(b), [str(a), str(a + b), str(b + 2), str(abs(a - b))], fill=lambda k: str(b + 3 + k)), ans=0, ee='\\(\\dfrac{b}{\\sin B}=\\dfrac{a}{\\sin A}\\Rightarrow b=\\dfrac{%d\\sin%d^\\circ}{\\sin%d^\\circ}=%d\\).' % (a, B, A, b), ev='\\(\\dfrac{b}{\\sin B}=\\dfrac{a}{\\sin A}\\Rightarrow b=\\dfrac{%d\\sin%d^\\circ}{\\sin%d^\\circ}=%d\\).' % (a, B, A, b))
def tri_circum(r, lv):
    a = r.choice([5, 6, 7, 8, 9, 10, 11, 12]); A = 30; R = a
    return dict(en='In triangle \\(ABC\\), \\(BC=%d\\) and \\(\\widehat{A}=30^\\circ\\). Find the circumradius \\(R\\).' % a, vi='Tam giác \\(ABC\\) có \\(BC=%d\\), \\(\\widehat{A}=30^\\circ\\). Tính bán kính đường tròn ngoại tiếp \\(R\\).' % a,
      opts=pick_opts(r, str(R), [str(2 * R), str(R + 1), str(R * 3), '%s' % fr(F(R, 2))], fill=lambda k: str(R + 3 + k)), ans=0, ee='\\(2R=\\dfrac{a}{\\sin A}=\\dfrac{%d}{1/2}=%d\\), so \\(R=%d\\).' % (a, 2 * a, R), ev='\\(2R=\\dfrac{a}{\\sin A}=\\dfrac{%d}{1/2}=%d\\) nên \\(R=%d\\).' % (a, 2 * a, R))
B6 = [tri_side, tri_angle, tri_area, tri_heron, tri_sine, tri_circum, tri_side, tri_heron]
