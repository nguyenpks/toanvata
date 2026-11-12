# -*- coding: utf-8 -*-
"""Ngân hàng câu hỏi sinh tự động cho Toán 9 (KNTT) – Bài 1 đến Bài 4.
Mỗi hàm builder(r, lv) trả về một câu hỏi; mọi đáp án do máy tính tính bằng phân số (Fraction) và tự kiểm lại
(thay nghiệm vào phương trình, duyệt điều kiện xác định…). Câu hỏi ở mỗi mức ngôn ngữ dùng số liệu khác nhau.

Ba loại câu hỏi:
  mcq   -> dict(en, vi, opts[4], ans, ee, ev)       (opts[ans] là phương án đúng; phương án văn bản viết '§' + TI(en, vi))
  tf    -> dict(en, vi, ans=True/False, ee, ev)
  short -> dict(en, vi, key, ee, ev)                (key là đáp số; ô trả lời nhận số nguyên hoặc thập phân)
BANK(groups, start) -> {1: [[mục nhóm 1], [mục nhóm 2], ...], 2: [...], 3: [...]} dùng thẳng cho LEVEL_PRACTICE."""
import random, math
from fractions import Fraction as F
from mb_selfpractice import fr, pick_opts
from mb_lib import MCQ, TF, SHORT, TI

# ---------------------------------------------------------------- tiện ích viết công thức
def P(x, y):
    """Cặp số (x; y) theo SGK (dấu chấm phẩy)."""
    return '(%s;\\ %s)' % (fr(x), fr(y))

def mono(a, v, first):
    """Hạng tử a·v (a là Fraction/int) có dấu, dùng khi ghép biểu thức."""
    a = F(a)
    if a == 0: return ''
    s = fr(abs(a)) if abs(a) != 1 or not v else ''
    if abs(a) != 1 and v and a.denominator != 1: s = fr(abs(a))
    body = s + v
    if first: return ('-' if a < 0 else '') + body
    return ('-' if a < 0 else '+') + body

def lin(*terms):
    """lin((a,'x'), (b,'y'), (c,'')) -> 'ax+by+c' (bỏ hạng tử 0)."""
    s = ''
    for a, v in terms:
        if F(a) == 0: continue
        s += mono(a, v, s == '')
    return s or '0'

def eq2(a, b, c, x='x', y='y'):
    return '%s=%s' % (lin((a, x), (b, y)), fr(c))

def cases(*rows):
    return '\\begin{cases}%s\\end{cases}' % '\\\\ '.join(rows)

def solve2(a, b, c, a2, b2, c2):
    """Giải hệ bằng định thức. Trả về ('one', x, y) | ('none',) | ('inf',)."""
    a, b, c, a2, b2, c2 = map(F, (a, b, c, a2, b2, c2))
    D = a * b2 - a2 * b
    if D != 0:
        x = (c * b2 - c2 * b) / D; y = (a * c2 - a2 * c) / D
        assert a * x + b * y == c and a2 * x + b2 * y == c2
        return ('one', x, y)
    if a * c2 == a2 * c and b * c2 == b2 * c: return ('inf',)
    return ('none',)

def nz(r, lo, hi):
    while True:
        v = r.randint(lo, hi)
        if v: return v

def tx(en, vi):
    """Phương án dạng văn bản song ngữ (không bọc công thức)."""
    return '§' + TI(en, vi)

def vnum(x):
    """Số thập phân viết kiểu Việt Nam trong công thức: 2{,}5."""
    s = ('%g' % float(x))
    return s.replace('.', '{,}')

def enum(x):
    return '%g' % float(x)

# ---------------------------------------------------------------- dựng ba bộ câu hỏi
HINT_NUM = ('Enter a number.', 'Nhập một số.')

def _render(kind, q, n, r):
    if kind == 'mcq':
        opts = list(q['opts']); correct = opts[q['ans']]
        assert len(set(opts)) == 4, opts
        idx = list(range(4)); r.shuffle(idx); sh = [opts[i] for i in idx]; L = 'abcd'[sh.index(correct)]
        return MCQ(n, (q['en'], q['vi']), sh, L, ('Answer: %s. %s' % (L, q['ee']), 'Đáp án %s. %s' % (L, q['ev'])))
    if kind == 'tf':
        a = bool(q['ans'])
        return TF(n, (q['en'], q['vi']), 'true' if a else 'false',
                  (('True. ' if a else 'False. ') + q['ee'], ('Đúng. ' if a else 'Sai. ') + q['ev']))
    if kind == 'short':
        return SHORT(n, (q['en'], q['vi']), q['key'], 'number', q.get('hint', HINT_NUM),
                     ('Answer: %s. %s' % (q['key'], q['ee']), 'Đáp số: %s. %s' % (q['key'].replace('.', ','), q['ev'])))
    raise ValueError(kind)

def BANK(groups, start=1, seeds=(911, 922, 933)):
    """groups: [[(kind, builder), ...], ...]. Không câu nào trùng nhau (kể cả giữa các mức)."""
    used = set(); out = {}
    for lv, seed in zip((1, 2, 3), seeds):
        r = random.Random(seed); n = start; sets = []
        for g in groups:
            items = []
            for kind, b in g:
                for _ in range(400):
                    try: q = b(r, lv)
                    except AssertionError: continue
                    if q['en'] not in used and (kind != 'mcq' or len(set(q['opts'])) == 4): break
                else: raise RuntimeError('không sinh được câu không trùng: ' + b.__name__)
                assert '<' not in q['en'].replace('<b>', '').replace('</b>', '') and '<' not in q['vi'].replace('<b>', '').replace('</b>', ''), q['en']
                # Từ "nghiệm" đứng riêng được gắn tự động với mục từ chung "zero (root)" (dùng cho hàm số lớp 11–12);
                # ở lớp 9 đó là nghiệm của phương trình/hệ, nên chú thích tiếng Anh là "solution".
                used.add(q['en']); items.append(_render(kind, q, n, r).replace('data-en="zero (root)">', 'data-en="solution">').replace('data-en="velocity">', 'data-en="speed">')); n += 1
            sets.append(items)
        out[lv] = sets
    return out

def ABCD_TITLES(nd=4):
    t = [('A. Multiple Choice', 'A. Trắc nghiệm nhiều lựa chọn'), ('B. True or False', 'B. Đúng hoặc sai'), ('C. Short Answer', 'C. Trả lời ngắn')]
    t += [('D1. Self-practice – Remembering', 'D1. Tự luyện – Mức Nhận biết'), ('D2. Self-practice – Understanding', 'D2. Tự luyện – Mức Thông hiểu'),
          ('D3. Self-practice – Basic application', 'D3. Tự luyện – Mức Vận dụng thấp'), ('D4. Self-practice – Advanced application', 'D4. Tự luyện – Mức Vận dụng')]
    return t

# =====================================================================================================
# BÀI 1. Khái niệm phương trình và hệ hai phương trình bậc nhất hai ẩn
# =====================================================================================================
def _sol_eq(r, lo=-4, hi=4, coef=5):
    """Phương trình ax+by=c (a, b ≠ 0) có nghiệm (x0; y0) cho trước."""
    a, b = nz(r, -coef, coef), nz(r, -coef, coef); x0, y0 = r.randint(lo, hi), r.randint(lo, hi)
    return a, b, a * x0 + b * y0, x0, y0

def b1_linear(r, lv):
    a, b, c = nz(r, -6, 6), nz(r, -6, 6), nz(r, -9, 9)
    good = eq2(a, b, c)
    bad = ['%sx^2%s=%d' % ('' if a == 1 else '-' if a == -1 else a, mono(b, 'y', False), c),
           '%sxy%s=%d' % ('' if a == 1 else '-' if a == -1 else a, mono(b, 'y', False), c),
           '0x+0y=%d' % c,
           '\\dfrac{%d}{x}%s=%d' % (abs(a), mono(b, 'y', False), c) if a > 0 else '-\\dfrac{%d}{x}%s=%d' % (abs(a), mono(b, 'y', False), c),
           '%s%s^2=%d' % (lin((a, 'x')), mono(b, 'y', False), c)]
    r.shuffle(bad)
    en, vi = r.choice([('Which equation is a linear equation in two variables \\(x\\) and \\(y\\)?', 'Phương trình nào là phương trình bậc nhất hai ẩn \\(x\\) và \\(y\\)?'),
                       ('Choose the linear equation in two variables.', 'Chọn phương trình bậc nhất hai ẩn.'),
                       ('Only one of these equations is a linear equation in two variables. Which one?', 'Chỉ có một phương trình là phương trình bậc nhất hai ẩn. Đó là phương trình nào?'),
                       ('Which of the following is a linear equation in \\(x\\) and \\(y\\)?', 'Phương trình nào sau đây là phương trình bậc nhất hai ẩn \\(x, y\\)?'),
                       ('Pick the equation of the form \\(ax+by=c\\) (\\(a, b\\) not both zero).', 'Chọn phương trình có dạng \\(ax+by=c\\) (\\(a, b\\) không đồng thời bằng 0).')])
    return dict(en=en, vi=vi, opts=[good] + bad[:3], ans=0,
                ee='It has the form \\(ax+by=c\\) with \\(a, b\\) not both zero. The others contain \\(x^2\\), \\(y^2\\), \\(xy\\), \\(\\frac{1}{x}\\) or have \\(a=b=0\\).',
                ev='Phương trình có dạng \\(ax+by=c\\) với \\(a, b\\) không đồng thời bằng 0. Các phương trình còn lại chứa \\(x^2\\), \\(y^2\\), \\(xy\\), \\(\\frac{1}{x}\\) hoặc có \\(a=b=0\\).')

def b1_pair(r, lv):
    a, b, c, x0, y0 = _sol_eq(r)
    cand = [(y0, x0), (x0, -y0), (-x0, y0), (x0 + 1, y0), (x0, y0 + 1), (-x0, -y0)]
    bad = [P(*p) for p in cand if a * p[0] + b * p[1] != c]
    assert len(set(bad)) >= 3
    e = eq2(a, b, c)
    return dict(en='Which ordered pair is a solution of the equation \\(%s\\)?' % e, vi='Cặp số nào là nghiệm của phương trình \\(%s\\)?' % e,
                opts=pick_opts(r, P(x0, y0), bad), ans=0,
                ee='Substitute: \\(%s\\cdot(%s)+(%s)\\cdot(%s)=%s\\). The other pairs do not satisfy the equation.' % (a, x0, b, y0, fr(c)),
                ev='Thay vào: \\(%s\\cdot(%s)+(%s)\\cdot(%s)=%s\\). Các cặp còn lại không thỏa mãn phương trình.' % (a, x0, b, y0, fr(c)))

def b1_find_m(r, lv):
    m, b = nz(r, -6, 6), nz(r, -5, 5); p, q = nz(r, -4, 4), r.randint(-4, 4)
    c = m * p + b * q
    others = [-m, m + 1, m - 1, F(c + b * q, p), F(c, p)]
    e = 'mx%s=%d' % (mono(b, 'y', False), c)
    return dict(en='Find \\(m\\) so that \\(%s\\) is a solution of the equation \\(%s\\).' % (P(p, q), e),
                vi='Tìm \\(m\\) để \\(%s\\) là nghiệm của phương trình \\(%s\\).' % (P(p, q), e),
                opts=pick_opts(r, 'm=' + fr(m), ['m=' + fr(o) for o in others if o != m]), ans=0,
                ee='Substitute \\(x=%s,\\ y=%s\\): \\(%s=%d\\), so \\(m=%s\\).' % (p, q, lin((p, 'm'), (b * q, '')), c, fr(m)),
                ev='Thay \\(x=%s,\\ y=%s\\): \\(%s=%d\\), suy ra \\(m=%s\\).' % (p, q, lin((p, 'm'), (b * q, '')), c, fr(m)))

def b1_tf_system(r, lv):
    a, b, c, x0, y0 = _sol_eq(r, coef=4); a2, b2 = nz(r, -4, 4), nz(r, -4, 4)
    assert a * b2 - a2 * b != 0
    c2 = a2 * x0 + b2 * y0
    truth = r.random() < 0.5
    if truth: p = (x0, y0)
    else:                                   # cặp chỉ thỏa phương trình thứ nhất
        p = (x0 + b, y0 - a); assert a * p[0] + b * p[1] == c and a2 * p[0] + b2 * p[1] != c2
    s = cases(eq2(a, b, c), eq2(a2, b2, c2))
    ok1, ok2 = a * p[0] + b * p[1] == c, a2 * p[0] + b2 * p[1] == c2
    return dict(en='The pair \\(%s\\) is a solution of the system \\(%s\\).' % (P(*p), s), vi='Cặp số \\(%s\\) là nghiệm của hệ \\(%s\\).' % (P(*p), s), ans=ok1 and ok2,
                ee='The first equation gives \\(%s\\) and the second gives \\(%s\\)%s.' % (fr(a * p[0] + b * p[1]), fr(a2 * p[0] + b2 * p[1]), '' if ok1 and ok2 else ' (not %d)' % c2),
                ev='Phương trình thứ nhất cho \\(%s\\), phương trình thứ hai cho \\(%s\\)%s.' % (fr(a * p[0] + b * p[1]), fr(a2 * p[0] + b2 * p[1]), '' if ok1 and ok2 else ' (khác %d)' % c2))

def b1_tf_general(r, lv):
    a, b = nz(r, -5, 5), r.choice([1, -1]); c = r.randint(-8, 8)
    k, m = F(-a, b), F(c, b)               # y = kx + m
    truth = r.random() < 0.5
    kk = k if truth else -k
    g = '(x;\\ %s)' % lin((kk, 'x'), (m, ''))
    e = eq2(a, b, c)
    return dict(en='The general solution of \\(%s\\) is \\(%s\\) with \\(x\\in\\mathbb{R}\\).' % (e, g), vi='Nghiệm tổng quát của phương trình \\(%s\\) là \\(%s\\) với \\(x\\in\\mathbb{R}\\).' % (e, g), ans=truth,
                ee='From the equation, \\(y=%s\\).' % lin((k, 'x'), (m, '')), ev='Từ phương trình suy ra \\(y=%s\\).' % lin((k, 'x'), (m, '')))

def b1_short_yint(r, lv):
    a, b = nz(r, -6, 6), nz(r, -5, 5); y0 = nz(r, -6, 6); c = b * y0
    e = eq2(a, b, c)
    return dict(en='The line that represents the solutions of \\(%s\\) meets the \\(y\\)-axis at \\((0;\\ y_0)\\). Find \\(y_0\\).' % e,
                vi='Đường thẳng biểu diễn tập nghiệm của phương trình \\(%s\\) cắt trục tung tại điểm \\((0;\\ y_0)\\). Tìm \\(y_0\\).' % e,
                key=str(y0), ee='Put \\(x=0\\): \\(%dy_0=%d\\), so \\(y_0=%d\\).' % (b, c, y0), ev='Thay \\(x=0\\): \\(%dy_0=%d\\) nên \\(y_0=%d\\).' % (b, c, y0))

NAMES = [('Lan', 'Lan'), ('Minh', 'Minh'), ('Hoa', 'Hoa'), ('Nam', 'Nam'), ('An', 'An'), ('Mai', 'Mai')]
def b1_short_shop(r, lv):
    p, q = r.choice([8, 10, 12, 15]), r.choice([3, 4, 5, 6]); k, y = r.randint(2, 6), r.randint(2, 8); T = p * k + q * y
    nm = r.choice(NAMES)
    return dict(en='A notebook costs %d thousand dong and a pen costs %d thousand dong. %s spends exactly %d thousand dong on \\(x\\) notebooks and \\(y\\) pens, so \\(%dx+%dy=%d\\). If %s buys %d notebooks, how many pens does %s buy?' % (p, q, nm[0], T, p, q, T, nm[0], k, 'she' if nm[0] in ('Lan', 'Hoa', 'Mai') else 'he'),
                vi='Một quyển vở giá %d nghìn đồng, một cây bút giá %d nghìn đồng. Bạn %s mua \\(x\\) quyển vở và \\(y\\) cây bút hết đúng %d nghìn đồng, nên \\(%dx+%dy=%d\\). Nếu bạn %s mua %d quyển vở thì bạn mua bao nhiêu cây bút?' % (p, q, nm[1], T, p, q, T, nm[1], k),
                key=str(y), ee='\\(%d\\cdot%d+%dy=%d\\Rightarrow %dy=%d\\Rightarrow y=%d\\).' % (p, k, q, T, q, T - p * k, y),
                ev='\\(%d\\cdot%d+%dy=%d\\Rightarrow %dy=%d\\Rightarrow y=%d\\).' % (p, k, q, T, q, T - p * k, y), hint=('Enter a whole number.', 'Nhập một số nguyên.'))

# ---- tự luyện Bài 1
def b1_d1_coef(r, lv):
    a, b, c = nz(r, -9, 9), nz(r, -9, 9), nz(r, -9, 9)
    assert len({a, b, c, -b}) == 4
    which = r.choice(['x', 'y'])
    ans = a if which == 'x' else b
    others = [b if which == 'x' else a, c, -ans]
    e = eq2(a, b, c)
    return dict(en='In the equation \\(%s\\), what is the coefficient of \\(%s\\)?' % (e, which), vi='Trong phương trình \\(%s\\), hệ số của \\(%s\\) là bao nhiêu?' % (e, which),
                opts=pick_opts(r, str(ans), [str(o) for o in others]), ans=0,
                ee='Compare with \\(ax+by=c\\): \\(a=%d,\\ b=%d,\\ c=%d\\).' % (a, b, c), ev='So sánh với \\(ax+by=c\\): \\(a=%d,\\ b=%d,\\ c=%d\\).' % (a, b, c))

def b1_d1_system(r, lv):
    a, b, c, a2, b2, c2 = nz(r, -5, 5), nz(r, -5, 5), r.randint(-9, 9), nz(r, -5, 5), nz(r, -5, 5), r.randint(-9, 9)
    good = cases(eq2(a, b, c), eq2(a2, b2, c2))
    bads = [cases('%s%s=%d' % (lin((a, 'x')), mono(b, 'y^2', False), c), eq2(a2, b2, c2)),
            cases(eq2(a, b, c), '%s%s=%d' % (lin((a2, 'xy')), mono(b2, 'y', False), c2)),
            cases(eq2(a, b, c), '0x+0y=%d' % (c2 or 5)),
            cases('%s%s=%d' % (lin((a, 'x^2')), mono(b, 'y', False), c), eq2(a2, b2, c2))]
    r.shuffle(bads)
    v = r.randint(0, 3)
    st = [('Which of these is a system of two linear equations in two variables?', 'Hệ nào sau đây là hệ hai phương trình bậc nhất hai ẩn?'),
          ('Choose the system of two linear equations in two variables.', 'Chọn hệ hai phương trình bậc nhất hai ẩn.'),
          ('Only one option is a system of two linear equations in two variables. Which one?', 'Chỉ có một phương án là hệ hai phương trình bậc nhất hai ẩn. Đó là phương án nào?'),
          ('Which system is made of two linear equations in \\(x\\) and \\(y\\)?', 'Hệ nào gồm hai phương trình bậc nhất hai ẩn \\(x, y\\)?')][v]
    return dict(en=st[0], vi=st[1], opts=[good] + bads[:3], ans=0,
                ee='Both equations must have the form \\(ax+by=c\\) with \\(a, b\\) not both zero.', ev='Cả hai phương trình phải có dạng \\(ax+by=c\\) với \\(a, b\\) không đồng thời bằng 0.')

def b1_d1_count(r, lv):
    a, b, c = nz(r, -9, 9), nz(r, -9, 9), r.randint(-12, 12)
    e = eq2(a, b, c)
    o = [tx('infinitely many', 'vô số nghiệm'), tx('exactly one', 'đúng một nghiệm'), tx('no solution', 'vô nghiệm'), tx('exactly two', 'đúng hai nghiệm')]
    return dict(en='How many solutions does the equation \\(%s\\) have?' % e, vi='Phương trình \\(%s\\) có bao nhiêu nghiệm?' % e, opts=o, ans=0,
                ee='A linear equation in two variables always has infinitely many solutions (all points of a line).', ev='Phương trình bậc nhất hai ẩn luôn có vô số nghiệm (mọi điểm của một đường thẳng).')

def b1_d2_find_y(r, lv):
    a, b, c, x0, y0 = _sol_eq(r, coef=6)
    others = [-y0, y0 + 1, F(c + a * x0, b), F(c, b), x0]
    e = eq2(a, b, c)
    return dict(en='The pair \\(%s\\) is a solution of \\(%s\\). Find \\(y_0\\).' % ('(%s;\\ y_0)' % fr(x0), e), vi='Cặp số \\(%s\\) là nghiệm của phương trình \\(%s\\). Tìm \\(y_0\\).' % ('(%s;\\ y_0)' % fr(x0), e),
                opts=pick_opts(r, fr(y0), [fr(o) for o in others if o != y0]), ans=0,
                ee='Substitute \\(x=%s\\): \\(%dy_0=%s\\), so \\(y_0=%s\\).' % (x0, b, fr(c - a * x0), fr(y0)), ev='Thay \\(x=%s\\): \\(%dy_0=%s\\) nên \\(y_0=%s\\).' % (x0, b, fr(c - a * x0), fr(y0)))

def b1_d2_special(r, lv):
    k = nz(r, -6, 6); v = nz(r, -5, 5); which = r.choice(['x', 'y'])
    if which == 'y': e = '0x%s=%d' % (mono(k, 'y', False), k * v); good = 'y=%d' % v; bads = ['x=%d' % v, 'y=%d' % (k * v) if k * v != v else 'y=%d' % (-v), 'y=%d' % (-v) if -v != k * v else 'x=%d' % (-v)]
    else: e = '%s+0y=%d' % (lin((k, 'x')), k * v); good = 'x=%d' % v; bads = ['y=%d' % v, 'x=%d' % (k * v) if k * v != v else 'x=%d' % (-v), 'x=%d' % (-v) if -v != k * v else 'y=%d' % (-v)]
    par = ('parallel to (or on) the \\(x\\)-axis', 'song song hoặc trùng với trục hoành') if which == 'y' else ('parallel to (or on) the \\(y\\)-axis', 'song song hoặc trùng với trục tung')
    return dict(en='The solutions of \\(%s\\) are represented by which line?' % e, vi='Tập nghiệm của phương trình \\(%s\\) được biểu diễn bởi đường thẳng nào?' % e,
                opts=pick_opts(r, good, bads, fill=lambda t: '%s=%d' % (which, v + 10 * t)), ans=0,
                ee='The equation means \\(%s\\); this line is %s.' % (good, par[0]), ev='Phương trình tương đương \\(%s\\); đường thẳng này %s.' % (good, par[1]))

def b1_d2_point(r, lv):
    a, b, c, x0, y0 = _sol_eq(r, coef=5)
    cand = [(y0, x0), (x0, -y0), (-x0, -y0), (x0 - 1, y0), (x0, y0 - 1), (-x0, y0)]
    bad = ['%s(%s;\\ %s)' % (L, fr(p[0]), fr(p[1])) for L, p in zip('NPQRST', cand) if a * p[0] + b * p[1] != c]
    assert len(bad) >= 3
    e = eq2(a, b, c)
    return dict(en='Which point lies on the line \\(%s\\)?' % e, vi='Điểm nào thuộc đường thẳng \\(%s\\)?' % e,
                opts=pick_opts(r, 'M(%s;\\ %s)' % (fr(x0), fr(y0)), bad[:3]), ans=0,
                ee='A point lies on the line when its coordinates satisfy the equation: \\(%d\\cdot(%d)+(%d)\\cdot(%d)=%d\\).' % (a, x0, b, y0, c),
                ev='Điểm thuộc đường thẳng khi tọa độ của nó thỏa mãn phương trình: \\(%d\\cdot(%d)+(%d)\\cdot(%d)=%d\\).' % (a, x0, b, y0, c))

def b1_d3_find_m_y(r, lv):
    a, m = nz(r, -6, 6), nz(r, -6, 6); p, q = r.randint(-4, 4), nz(r, -4, 4); c = a * p + m * q
    others = [-m, m + 1, F(c + a * p, q), F(c, q)]
    e = '%smy=%d' % (lin((a, 'x')) + '+', c)
    return dict(en='Find \\(m\\) so that \\(%s\\) is a solution of \\(%s\\).' % (P(p, q), e), vi='Tìm \\(m\\) để \\(%s\\) là nghiệm của phương trình \\(%s\\).' % (P(p, q), e),
                opts=pick_opts(r, 'm=' + fr(m), ['m=' + fr(o) for o in others if o != m], fill=lambda t: 'm=%d' % (m + 2 * t + 1)), ans=0,
                ee='\\(%s=%d\\Rightarrow %s=%d\\Rightarrow m=%d\\).' % (lin((a * p, ''), (q, 'm')), c, lin((q, 'm')), c - a * p, m),
                ev='\\(%s=%d\\Rightarrow %s=%d\\Rightarrow m=%d\\).' % (lin((a * p, ''), (q, 'm')), c, lin((q, 'm')), c - a * p, m))

def b1_d3_syspair(r, lv):
    a, b, c, x0, y0 = _sol_eq(r, coef=4); a2, b2 = nz(r, -4, 4), nz(r, -4, 4)
    assert a * b2 - a2 * b != 0; c2 = a2 * x0 + b2 * y0
    only1 = (x0 + b, y0 - a); only2 = (x0 + b2, y0 - a2)
    cand = [only1, only2, (y0, x0), (-x0, -y0)]
    bad = [P(*p) for p in cand if not (a * p[0] + b * p[1] == c and a2 * p[0] + b2 * p[1] == c2)]
    s = cases(eq2(a, b, c), eq2(a2, b2, c2))
    return dict(en='Which pair is a solution of the system \\(%s\\)?' % s, vi='Cặp số nào là nghiệm của hệ \\(%s\\)?' % s,
                opts=pick_opts(r, P(x0, y0), bad), ans=0,
                ee='The pair must satisfy <b>both</b> equations. Some options satisfy only one of them.', ev='Cặp số phải thỏa mãn <b>cả hai</b> phương trình. Có phương án chỉ thỏa mãn một phương trình.')

def b1_d3_find_c(r, lv):
    a, b = nz(r, -6, 6), nz(r, -6, 6); p, q = r.randint(-5, 5), r.randint(-5, 5); c = a * p + b * q
    others = [-c, a * p - b * q, a * q + b * p, c + 1]
    e = '%s=c' % lin((a, 'x'), (b, 'y'))
    return dict(en='Find \\(c\\) so that the line \\(%s\\) passes through the point \\(M%s\\).' % (e, P(p, q)), vi='Tìm \\(c\\) để đường thẳng \\(%s\\) đi qua điểm \\(M%s\\).' % (e, P(p, q)),
                opts=pick_opts(r, 'c=%d' % c, ['c=%d' % o for o in others if o != c], fill=lambda t: 'c=%d' % (c + 2 * t + 1)), ans=0,
                ee='\\(c=%d\\cdot(%d)+(%d)\\cdot(%d)=%d\\).' % (a, p, b, q, c), ev='\\(c=%d\\cdot(%d)+(%d)\\cdot(%d)=%d\\).' % (a, p, b, q, c))

def b1_d4_garden(r, lv):
    w = r.randint(4, 15); d = r.randint(2, 8); L = w + d; Pm = 2 * (L + w)
    good = cases('2x+2y=%d' % Pm, 'x-y=%d' % d)
    bads = [cases('x+y=%d' % Pm, 'x-y=%d' % d), cases('2x+2y=%d' % Pm, 'y-x=%d' % d), cases('xy=%d' % Pm, 'x-y=%d' % d), cases('x+y=%d' % Pm, 'x+y=%d' % d)]
    return dict(en='A rectangular garden has a perimeter of %d m. Its length is %d m longer than its width. Let \\(x\\) be the length and \\(y\\) the width (in meters). Which system describes the situation?' % (Pm, d),
                vi='Một mảnh vườn hình chữ nhật có chu vi %d m, chiều dài hơn chiều rộng %d m. Gọi \\(x\\) là chiều dài, \\(y\\) là chiều rộng (mét). Hệ phương trình nào mô tả tình huống?' % (Pm, d),
                opts=[good] + bads[:3], ans=0, ee='Perimeter: \\(2x+2y=%d\\); length minus width: \\(x-y=%d\\).' % (Pm, d), ev='Chu vi: \\(2x+2y=%d\\); chiều dài trừ chiều rộng: \\(x-y=%d\\).' % (Pm, d))

def b1_d4_tickets(r, lv):
    a, b = r.choice([(50, 30), (60, 40), (80, 50), (70, 45), (90, 60)]); x, y = r.randint(3, 12), r.randint(5, 20); n, T = x + y, a * x + b * y
    good = cases('x+y=%d' % n, '%dx+%dy=%d' % (a, b, T))
    bads = [cases('x+y=%d' % n, '%dx+%dy=%d' % (b, a, T)), cases('x+y=%d' % T, '%dx+%dy=%d' % (a, b, n)), cases('%dx+%dy=%d' % (a, b, n), 'x+y=%d' % (a + b)), cases('x-y=%d' % n, '%dx+%dy=%d' % (a, b, T))]
    r.shuffle(bads)
    return dict(en='A class buys %d museum tickets for %d thousand dong in total. An adult ticket costs %d thousand dong and a student ticket costs %d thousand dong. Let \\(x\\) be the number of adult tickets and \\(y\\) the number of student tickets. Which system is correct?' % (n, T, a, b),
                vi='Một lớp mua %d vé tham quan bảo tàng hết %d nghìn đồng. Vé người lớn giá %d nghìn đồng, vé học sinh giá %d nghìn đồng. Gọi \\(x\\) là số vé người lớn, \\(y\\) là số vé học sinh. Hệ phương trình nào đúng?' % (n, T, a, b),
                opts=[good] + bads[:3], ans=0, ee='Number of tickets: \\(x+y=%d\\). Money: \\(%dx+%dy=%d\\).' % (n, a, b, T), ev='Số vé: \\(x+y=%d\\). Số tiền: \\(%dx+%dy=%d\\).' % (n, a, b, T))

def b1_d4_mn(r, lv):
    m, n = nz(r, -5, 5), nz(r, -5, 5); p, q = nz(r, -4, 4), nz(r, -4, 4); b, a2 = nz(r, -3, 3), nz(r, -3, 3)
    c1, c2 = m * p + b * q, a2 * p + n * q
    s = cases('mx%s=%d' % (mono(b, 'y', False), c1), '%sny=%d' % (lin((a2, 'x')) + '+', c2))
    good = 'm=%d,\\ n=%d' % (m, n)
    alts = [(-m, n), (m, -n), (n, m), (m + 1, n), (m, n + 1)]
    return dict(en='Find \\(m\\) and \\(n\\) so that \\(%s\\) is a solution of the system \\(%s\\).' % (P(p, q), s), vi='Tìm \\(m\\) và \\(n\\) để \\(%s\\) là nghiệm của hệ \\(%s\\).' % (P(p, q), s),
                opts=pick_opts(r, good, ['m=%d,\\ n=%d' % t for t in alts if t != (m, n)]), ans=0,
                ee='First equation: \\(%s=%d\\Rightarrow m=%d\\). Second: \\(%s=%d\\Rightarrow n=%d\\).' % (lin((p, 'm'), (b * q, '')), c1, m, lin((q, 'n'), (a2 * p, '')), c2, n),
                ev='Phương trình thứ nhất: \\(%s=%d\\Rightarrow m=%d\\). Phương trình thứ hai: \\(%s=%d\\Rightarrow n=%d\\).' % (lin((p, 'm'), (b * q, '')), c1, m, lin((q, 'n'), (a2 * p, '')), c2, n))

L1_GROUPS = [[('mcq', b1_linear), ('mcq', b1_pair), ('mcq', b1_find_m)], [('tf', b1_tf_system), ('tf', b1_tf_general)], [('short', b1_short_yint), ('short', b1_short_shop)],
             [('mcq', b1_d1_coef), ('mcq', b1_d1_system), ('mcq', b1_d1_count)], [('mcq', b1_d2_find_y), ('mcq', b1_d2_special), ('mcq', b1_d2_point)],
             [('mcq', b1_d3_find_m_y), ('mcq', b1_d3_syspair), ('mcq', b1_d3_find_c)], [('mcq', b1_d4_garden), ('mcq', b1_d4_tickets), ('mcq', b1_d4_mn)]]

# =====================================================================================================
# BÀI 2. Giải hệ hai phương trình bậc nhất hai ẩn
# =====================================================================================================
def _sys(r, coef=5, lo=-5, hi=5, unit=False):
    """Hệ có nghiệm duy nhất (x0; y0) nguyên. unit=True: phương trình đầu có hệ số của x bằng 1 (dễ thế)."""
    while True:
        a = 1 if unit else nz(r, -coef, coef); b, a2, b2 = nz(r, -coef, coef), nz(r, -coef, coef), nz(r, -coef, coef)
        if a * b2 - a2 * b != 0 and not (a == a2 and b == b2): break
    x0, y0 = r.randint(lo, hi), r.randint(lo, hi)
    c, c2 = a * x0 + b * y0, a2 * x0 + b2 * y0
    k = solve2(a, b, c, a2, b2, c2); assert k == ('one', x0, y0)
    return a, b, c, a2, b2, c2, x0, y0

def _bad_pairs(sysc, x0, y0):
    a, b, c, a2, b2, c2 = sysc
    cand = [(y0, x0), (-x0, y0), (x0, -y0), (-x0, -y0), (x0 + 1, y0), (x0, y0 - 1)]
    return [P(*p) for p in cand if not (a * p[0] + b * p[1] == c and a2 * p[0] + b2 * p[1] == c2)]

def b2_solve(r, lv):
    a, b, c, a2, b2, c2, x0, y0 = _sys(r)
    s = cases(eq2(a, b, c), eq2(a2, b2, c2))
    return dict(en='Solve the system \\(%s\\).' % s, vi='Giải hệ phương trình \\(%s\\).' % s, opts=pick_opts(r, P(x0, y0), _bad_pairs((a, b, c, a2, b2, c2), x0, y0)), ans=0,
                ee='The solution is \\(%s\\). Check: both equations are true.' % P(x0, y0), ev='Nghiệm của hệ là \\(%s\\). Thử lại: cả hai phương trình đều đúng.' % P(x0, y0))

def b2_express(r, lv):
    b, c = nz(r, -7, 7), nz(r, -12, 12); a2, b2 = nz(r, -5, 5), nz(r, -5, 5)
    c2 = nz(r, -9, 9); good = 'x=%s' % lin((c, ''), (-b, 'y')); bads = ['x=%s' % lin((c, ''), (b, 'y')), 'x=%s' % lin((-c, ''), (b, 'y')), 'x=%s' % lin((-c, ''), (-b, 'y'))]
    e = eq2(1, b, c)
    return dict(en='To solve the system \\(%s\\) by substitution, we first express \\(x\\) from the first equation. Which expression is correct?' % cases(e, eq2(a2, b2, c2)),
                vi='Để giải hệ \\(%s\\) bằng phương pháp thế, ta rút \\(x\\) từ phương trình thứ nhất. Cách rút nào đúng?' % cases(e, eq2(a2, b2, c2)),
                opts=[good] + bads, ans=0, ee='Move \\(%s\\) to the right-hand side and change its sign.' % lin((b, 'y')), ev='Chuyển \\(%s\\) sang vế phải và đổi dấu.' % lin((b, 'y')))

TXT_COUNT = [tx('exactly one solution', 'có nghiệm duy nhất'), tx('no solution', 'vô nghiệm'), tx('infinitely many solutions', 'có vô số nghiệm'), tx('exactly two solutions', 'có đúng hai nghiệm')]
def _kind_sys(r, kind):
    a, b = nz(r, -5, 5), nz(r, -5, 5); k = r.choice([2, 3, -2, -1, 4])
    if kind == 'one':
        a2, b2 = nz(r, -5, 5), nz(r, -5, 5); assert a * b2 != a2 * b
        c, c2 = r.randint(-9, 9), r.randint(-9, 9)
    else:
        c = r.randint(-6, 6); a2, b2 = k * a, k * b; c2 = k * c if kind == 'inf' else k * c + nz(r, -4, 4)
    assert solve2(a, b, c, a2, b2, c2)[0] == kind
    return a, b, c, a2, b2, c2

def b2_count(r, lv):
    kind = r.choice(['one', 'none', 'inf']); a, b, c, a2, b2, c2 = _kind_sys(r, kind)
    s = cases(eq2(a, b, c), eq2(a2, b2, c2)); i = ['one', 'none', 'inf'].index(kind)
    why = {'one': ('The two lines have different slopes, so they intersect at one point.', 'Hai đường thẳng cắt nhau tại một điểm.'),
           'none': ('The second equation is the first one multiplied by %d on the left side but not on the right side: the lines are parallel.' % (a2 // a), 'Vế trái phương trình thứ hai bằng %d lần vế trái phương trình thứ nhất nhưng vế phải thì không: hai đường thẳng song song.' % (a2 // a)),
           'inf': ('The second equation is the first one multiplied by %d: the lines coincide.' % (a2 // a), 'Phương trình thứ hai bằng %d lần phương trình thứ nhất: hai đường thẳng trùng nhau.' % (a2 // a))}[kind]
    return dict(en='How many solutions does the system \\(%s\\) have?' % s, vi='Hệ phương trình \\(%s\\) có bao nhiêu nghiệm?' % s, opts=TXT_COUNT, ans=i, ee=why[0], ev=why[1])

def b2_tf_pair(r, lv):
    a, b, c, a2, b2, c2, x0, y0 = _sys(r, coef=4)
    truth = r.random() < 0.5; p = (x0, y0) if truth else r.choice([(y0, x0), (x0, -y0), (-x0, y0)])
    ok = a * p[0] + b * p[1] == c and a2 * p[0] + b2 * p[1] == c2
    s = cases(eq2(a, b, c), eq2(a2, b2, c2))
    return dict(en='The system \\(%s\\) has the solution \\(%s\\).' % (s, P(*p)), vi='Hệ phương trình \\(%s\\) có nghiệm là \\(%s\\).' % (s, P(*p)), ans=ok,
                ee='Solving gives \\(%s\\).' % P(x0, y0), ev='Giải hệ được nghiệm \\(%s\\).' % P(x0, y0))

def b2_tf_none(r, lv):
    kind = r.choice(['one', 'none', 'none', 'inf']); a, b, c, a2, b2, c2 = _kind_sys(r, kind)
    s = cases(eq2(a, b, c), eq2(a2, b2, c2))
    return dict(en='The system \\(%s\\) has no solution.' % s, vi='Hệ phương trình \\(%s\\) vô nghiệm.' % s, ans=(kind == 'none'),
                ee={'one': 'It has exactly one solution.', 'none': 'The lines are parallel.', 'inf': 'It has infinitely many solutions (the lines coincide).'}[kind],
                ev={'one': 'Hệ có nghiệm duy nhất.', 'none': 'Hai đường thẳng song song.', 'inf': 'Hệ có vô số nghiệm (hai đường thẳng trùng nhau).'}[kind])

def b2_short_sum(r, lv):
    a, b, c, a2, b2, c2, x0, y0 = _sys(r)
    s = cases(eq2(a, b, c), eq2(a2, b2, c2))
    return dict(en='Solve the system \\(%s\\). Write the value of \\(x+y\\).' % s, vi='Giải hệ phương trình \\(%s\\). Ghi giá trị của \\(x+y\\).' % s,
                key=str(x0 + y0), ee='The solution is \\(%s\\), so \\(x+y=%d\\).' % (P(x0, y0), x0 + y0), ev='Nghiệm của hệ là \\(%s\\) nên \\(x+y=%d\\).' % (P(x0, y0), x0 + y0))

def b2_short_line(r, lv):
    a, b = nz(r, -4, 4), r.randint(-6, 6); x1 = r.randint(-4, 3); x2 = x1 + r.randint(1, 4)
    A, B = (x1, a * x1 + b), (x2, a * x2 + b)
    assert solve2(x1, 1, A[1], x2, 1, B[1]) == ('one', a, b)
    return dict(en='The line \\(y=ax+b\\) passes through \\(A%s\\) and \\(B%s\\). Find \\(a+b\\).' % (P(*A), P(*B)), vi='Đường thẳng \\(y=ax+b\\) đi qua \\(A%s\\) và \\(B%s\\). Tìm \\(a+b\\).' % (P(*A), P(*B)),
                key=str(a + b), ee='Solve \\(%s\\): \\(a=%d,\\ b=%d\\), so \\(a+b=%d\\).' % (cases('%s=%d' % (lin((x1, 'a'), (1, 'b')), A[1]), '%s=%d' % (lin((x2, 'a'), (1, 'b')), B[1])), a, b, a + b),
                ev='Giải hệ \\(%s\\): \\(a=%d,\\ b=%d\\) nên \\(a+b=%d\\).' % (cases('%s=%d' % (lin((x1, 'a'), (1, 'b')), A[1]), '%s=%d' % (lin((x2, 'a'), (1, 'b')), B[1])), a, b, a + b))

# ---- tự luyện Bài 2
def b2_d1_express_y(r, lv):
    k, c = nz(r, -7, 7), nz(r, -12, 12)
    e = eq2(k, 1, c); good = 'y=%s' % lin((c, ''), (-k, 'x'))
    bads = ['y=%s' % lin((c, ''), (k, 'x')), 'y=%s' % lin((-c, ''), (k, 'x')), 'y=%s' % lin((-c, ''), (-k, 'x'))]
    return dict(en='From the equation \\(%s\\), express \\(y\\) in terms of \\(x\\).' % e, vi='Từ phương trình \\(%s\\), hãy biểu diễn \\(y\\) theo \\(x\\).' % e, opts=[good] + bads, ans=0,
                ee='\\(y=%s\\).' % lin((c, ''), (-k, 'x')), ev='\\(y=%s\\).' % lin((c, ''), (-k, 'x')))

def b2_d1_eliminate(r, lv):
    a, a2, b = nz(r, -6, 6), nz(r, -6, 6), r.randint(2, 7); opp = r.random() < 0.5
    assert abs(a) != abs(a2)
    b2 = -b if opp else b; c, c2 = r.randint(-12, 12), r.randint(-12, 12)
    s = cases(eq2(a, b, c), eq2(a2, b2, c2))
    o = [tx('add the two equations side by side', 'cộng từng vế hai phương trình'), tx('subtract the two equations side by side', 'trừ từng vế hai phương trình'),
         tx('multiply both equations by \\(%d\\)' % b, 'nhân cả hai phương trình với \\(%d\\)' % b), tx('add \\(%d\\) to both sides of the first equation' % b, 'cộng \\(%d\\) vào hai vế của phương trình thứ nhất' % b)]
    return dict(en='To eliminate \\(y\\) in the system \\(%s\\), we should…' % s, vi='Để khử ẩn \\(y\\) trong hệ \\(%s\\), ta nên…' % s, opts=o, ans=0 if opp else 1,
                ee='The coefficients of \\(y\\) are %s, so we %s.' % ('opposite numbers' if opp else 'equal', 'add' if opp else 'subtract'),
                ev='Hệ số của \\(y\\) %s nên ta %s từng vế.' % ('là hai số đối nhau' if opp else 'bằng nhau', 'cộng' if opp else 'trừ'))

def b2_d1_zero(r, lv):
    k = r.randint(-9, 9); v = r.choice(['x', 'y'])
    i = 2 if k == 0 else 1
    return dict(en='While solving a system by elimination, we get \\(0%s=%d\\). What can we say about the system?' % (v, k),
                vi='Khi giải một hệ bằng phương pháp cộng đại số, ta được \\(0%s=%d\\). Kết luận gì về hệ?' % (v, k), opts=TXT_COUNT, ans=i,
                ee='\\(0%s=%d\\) is %s.' % (v, k, 'true for every value, so the system has infinitely many solutions' if k == 0 else 'never true, so the system has no solution'),
                ev='\\(0%s=%d\\) %s.' % (v, k, 'đúng với mọi giá trị nên hệ có vô số nghiệm' if k == 0 else 'không bao giờ đúng nên hệ vô nghiệm'))

def b2_d2_subst(r, lv):
    k, m = nz(r, -4, 4), r.randint(-6, 6); a, b = nz(r, -5, 5), nz(r, -5, 5); assert a + b * k != 0
    x0 = r.randint(-4, 4); y0 = k * x0 + m; c = a * x0 + b * y0
    sysc = (-k, 1, m, a, b, c); assert solve2(*sysc) == ('one', x0, y0)
    s = cases('y=%s' % lin((k, 'x'), (m, '')), eq2(a, b, c))
    return dict(en='Solve the system \\(%s\\).' % s, vi='Giải hệ phương trình \\(%s\\).' % s, opts=pick_opts(r, P(x0, y0), _bad_pairs(sysc, x0, y0)), ans=0,
                ee='Substitute \\(y=%s\\) into the second equation: \\(%s=%d\\Rightarrow x=%d\\), then \\(y=%d\\).' % (lin((k, 'x'), (m, '')), lin((a + b * k, 'x'), (b * m, '')), c, x0, y0),
                ev='Thế \\(y=%s\\) vào phương trình thứ hai: \\(%s=%d\\Rightarrow x=%d\\), suy ra \\(y=%d\\).' % (lin((k, 'x'), (m, '')), lin((a + b * k, 'x'), (b * m, '')), c, x0, y0))

def b2_d2_elim(r, lv):
    a = nz(r, -5, 5); b, b2 = nz(r, -5, 5), nz(r, -5, 5); assert b != b2
    x0, y0 = r.randint(-5, 5), r.randint(-5, 5); c, c2 = a * x0 + b * y0, a * x0 + b2 * y0
    sysc = (a, b, c, a, b2, c2); assert solve2(*sysc) == ('one', x0, y0)
    s = cases(eq2(a, b, c), eq2(a, b2, c2))
    return dict(en='Solve the system \\(%s\\).' % s, vi='Giải hệ phương trình \\(%s\\).' % s, opts=pick_opts(r, P(x0, y0), _bad_pairs(sysc, x0, y0)), ans=0,
                ee='Subtract the equations: \\(%s=%d\\Rightarrow y=%d\\); then \\(x=%d\\).' % (lin((b - b2, 'y')), c - c2, y0, x0),
                ev='Trừ từng vế: \\(%s=%d\\Rightarrow y=%d\\); suy ra \\(x=%d\\).' % (lin((b - b2, 'y')), c - c2, y0, x0))

def b2_d2_which(r, lv):
    want = r.choice(['inf', 'none'])
    good = cases(*[eq2(*t) for t in (lambda s: (s[:3], s[3:]))(_kind_sys(r, want))])
    other = 'none' if want == 'inf' else 'inf'
    bads = [cases(*[eq2(*t) for t in (lambda s: (s[:3], s[3:]))(_kind_sys(r, k))]) for k in (other, 'one', 'one')]
    st = {'inf': [('Which system has infinitely many solutions?', 'Hệ nào sau đây có vô số nghiệm?'), ('Choose the system whose two lines coincide.', 'Chọn hệ có hai đường thẳng trùng nhau.'),
                  ('Only one system has infinitely many solutions. Which one?', 'Chỉ có một hệ có vô số nghiệm. Đó là hệ nào?')],
          'none': [('Which system has no solution?', 'Hệ nào sau đây vô nghiệm?'), ('Choose the system whose two lines are parallel.', 'Chọn hệ có hai đường thẳng song song.'),
                   ('Only one system has no solution. Which one?', 'Chỉ có một hệ vô nghiệm. Đó là hệ nào?')]}[want]
    q = r.choice(st)
    return dict(en=q[0], vi=q[1], opts=[good] + bads, ans=0,
                ee='In the correct system, the second equation is a multiple of the first %s.' % ('(both sides)' if want == 'inf' else 'on the left side only'),
                ev='Ở hệ đúng, phương trình thứ hai %s.' % ('bằng một số lần phương trình thứ nhất (cả hai vế)' if want == 'inf' else 'có vế trái bằng một số lần vế trái phương trình thứ nhất nhưng vế phải thì không'))

def b2_d3_mult(r, lv):
    while True:
        a, b, c, a2, b2, c2, x0, y0 = _sys(r, coef=6)
        if abs(a) not in (1, abs(a2)) and abs(b) not in (1, abs(b2)) and abs(a2) != 1 and abs(b2) != 1: break
    sysc = (a, b, c, a2, b2, c2); s = cases(eq2(a, b, c), eq2(a2, b2, c2))
    return dict(en='Solve the system \\(%s\\).' % s, vi='Giải hệ phương trình \\(%s\\).' % s, opts=pick_opts(r, P(x0, y0), _bad_pairs(sysc, x0, y0)), ans=0,
                ee='Multiply the equations by \\(%d\\) and \\(%d\\) so that the coefficients of \\(x\\) are equal, then subtract: \\(y=%d\\), \\(x=%d\\).' % (a2, a, y0, x0),
                ev='Nhân hai phương trình lần lượt với \\(%d\\) và \\(%d\\) để hệ số của \\(x\\) bằng nhau, rồi trừ từng vế: \\(y=%d\\), \\(x=%d\\).' % (a2, a, y0, x0))

def b2_d3_line(r, lv):
    a, b = nz(r, -4, 4), r.randint(-6, 6); x1 = r.randint(-4, 3); x2 = x1 + r.randint(1, 4); A, B = (x1, a * x1 + b), (x2, a * x2 + b)
    good = 'y=%s' % lin((a, 'x'), (b, '')); bads = ['y=%s' % lin((-a, 'x'), (b, '')), 'y=%s' % lin((a, 'x'), (-b, '')) if b else 'y=%s' % lin((a, 'x'), (1, '')), 'y=%s' % lin((b, 'x'), (a, '')) if b not in (0, a) else 'y=%s' % lin((a + 1, 'x'), (b, ''))]
    return dict(en='Find the line \\(y=ax+b\\) through \\(A%s\\) and \\(B%s\\).' % (P(*A), P(*B)), vi='Tìm đường thẳng \\(y=ax+b\\) đi qua \\(A%s\\) và \\(B%s\\).' % (P(*A), P(*B)),
                opts=pick_opts(r, good, bads, fill=lambda t: 'y=%s' % lin((a + t + 1, 'x'), (b, ''))), ans=0,
                ee='Solve \\(%s\\): \\(a=%d,\\ b=%d\\).' % (cases('%s=%d' % (lin((x1, 'a'), (1, 'b')), A[1]), '%s=%d' % (lin((x2, 'a'), (1, 'b')), B[1])), a, b),
                ev='Giải hệ \\(%s\\): \\(a=%d,\\ b=%d\\).' % (cases('%s=%d' % (lin((x1, 'a'), (1, 'b')), A[1]), '%s=%d' % (lin((x2, 'a'), (1, 'b')), B[1])), a, b))

def b2_d3_frac(r, lv):
    p, q = r.choice([(2, 3), (3, 2), (2, 5), (4, 3), (3, 4)]); x0, y0 = p * r.randint(-3, 3), q * r.randint(-3, 3); k = r.choice([1, 2, -1])
    c1 = F(x0, p) + F(y0, q); c2 = x0 + k * y0; assert c1.denominator == 1
    sysc = (F(1, p), F(1, q), c1, 1, k, c2); assert solve2(*sysc) == ('one', x0, y0)
    s = cases('\\dfrac{x}{%d}+\\dfrac{y}{%d}=%s' % (p, q, fr(c1)), eq2(1, k, c2))
    return dict(en='Solve the system \\(%s\\).' % s, vi='Giải hệ phương trình \\(%s\\).' % s, opts=pick_opts(r, P(x0, y0), _bad_pairs(sysc, x0, y0)), ans=0,
                ee='Multiply the first equation by \\(%d\\): \\(%s=%s\\). Then solve: \\(%s\\).' % (p * q, lin((q, 'x'), (p, 'y')), fr(c1 * p * q), P(x0, y0)),
                ev='Nhân hai vế phương trình thứ nhất với \\(%d\\): \\(%s=%s\\). Giải hệ được \\(%s\\).' % (p * q, lin((q, 'x'), (p, 'y')), fr(c1 * p * q), P(x0, y0)))

def b2_d4_m_none(r, lv):
    a, b = nz(r, -4, 4), nz(r, -4, 4); k = r.choice([2, 3, -2]); c = r.randint(-6, 6); c2 = k * c + nz(r, -3, 3); m = k * a
    assert solve2(a, b, c, m, k * b, c2)[0] == 'none' and solve2(a, b, c, m + 1, k * b, c2)[0] == 'one'
    s = cases(eq2(a, b, c), 'mx%s=%d' % (mono(k * b, 'y', False), c2))
    return dict(en='Find \\(m\\) so that the system \\(%s\\) has no solution.' % s, vi='Tìm \\(m\\) để hệ \\(%s\\) vô nghiệm.' % s,
                opts=pick_opts(r, 'm=%d' % m, ['m=%d' % o for o in (a, -m, k, m + k) if o != m], fill=lambda t: 'm=%d' % (m + t + 5)), ans=0,
                ee='No solution means the two lines are parallel: the left side of the second equation is \\(%d\\) times the left side of the first one, so \\(m=%d\\); the right sides do not match (\\(%d\\ne %d\\cdot(%d)\\)).' % (k, m, c2, k, c),
                ev='Hệ vô nghiệm khi hai đường thẳng song song: vế trái phương trình thứ hai bằng \\(%d\\) lần vế trái phương trình thứ nhất nên \\(m=%d\\); vế phải không tương ứng (\\(%d\\ne %d\\cdot(%d)\\)).' % (k, m, c2, k, c))

def b2_d4_ab(r, lv):
    a, b = nz(r, -5, 5), nz(r, -5, 5); p, q = nz(r, -3, 3), nz(r, -3, 3); assert p * p + q * q != 0
    c1, c2 = a * p + b * q, b * p - a * q
    assert solve2(p, q, c1, -q, p, c2) == ('one', a, b)
    s = cases('ax+by=%d' % c1, 'bx-ay=%d' % c2)
    good = 'a=%d,\\ b=%d' % (a, b)
    return dict(en='Find \\(a, b\\) so that the system \\(%s\\) has the solution \\(%s\\).' % (s, P(p, q)), vi='Tìm \\(a, b\\) để hệ \\(%s\\) có nghiệm \\(%s\\).' % (s, P(p, q)),
                opts=pick_opts(r, good, ['a=%d,\\ b=%d' % t for t in ((b, a), (-a, b), (a, -b), (-a, -b)) if t != (a, b)]), ans=0,
                ee='Substitute \\(x=%d,\\ y=%d\\): \\(%s\\). Solving gives \\(a=%d,\\ b=%d\\).' % (p, q, cases('%s=%d' % (lin((p, 'a'), (q, 'b')), c1), '%s=%d' % (lin((-q, 'a'), (p, 'b')), c2)), a, b),
                ev='Thay \\(x=%d,\\ y=%d\\): \\(%s\\). Giải hệ được \\(a=%d,\\ b=%d\\).' % (p, q, cases('%s=%d' % (lin((p, 'a'), (q, 'b')), c1), '%s=%d' % (lin((-q, 'a'), (p, 'b')), c2)), a, b))

def b2_d4_bracket(r, lv):
    k1, k2 = r.randint(2, 4), r.randint(2, 4); x0, y0 = r.randint(-4, 4), r.randint(-4, 4)
    c1 = k1 * (x0 + 1) - y0; c2 = x0 + k2 * (y0 - 1)
    sysc = (k1, -1, c1 - k1, 1, k2, c2 + k2); assert solve2(*sysc) == ('one', x0, y0)
    s = cases('%d(x+1)-y=%d' % (k1, c1), 'x+%d(y-1)=%d' % (k2, c2))
    return dict(en='Solve the system \\(%s\\).' % s, vi='Giải hệ phương trình \\(%s\\).' % s, opts=pick_opts(r, P(x0, y0), _bad_pairs(sysc, x0, y0)), ans=0,
                ee='Expand: \\(%s\\). Solving gives \\(%s\\).' % (cases(eq2(k1, -1, c1 - k1), eq2(1, k2, c2 + k2)), P(x0, y0)),
                ev='Khai triển: \\(%s\\). Giải hệ được \\(%s\\).' % (cases(eq2(k1, -1, c1 - k1), eq2(1, k2, c2 + k2)), P(x0, y0)))

L2_GROUPS = [[('mcq', b2_solve), ('mcq', b2_express), ('mcq', b2_count)], [('tf', b2_tf_pair), ('tf', b2_tf_none)], [('short', b2_short_sum), ('short', b2_short_line)],
             [('mcq', b2_d1_express_y), ('mcq', b2_d1_eliminate), ('mcq', b2_d1_zero)], [('mcq', b2_d2_subst), ('mcq', b2_d2_elim), ('mcq', b2_d2_which)],
             [('mcq', b2_d3_mult), ('mcq', b2_d3_line), ('mcq', b2_d3_frac)], [('mcq', b2_d4_m_none), ('mcq', b2_d4_ab), ('mcq', b2_d4_bracket)]]

# =====================================================================================================
# BÀI 3. Giải bài toán bằng cách lập hệ phương trình
# =====================================================================================================
CTX_SUM = [  # (en: hai đại lượng, vi) – tổng S, đại lượng thứ nhất hơn đại lượng thứ hai d
    ('Class 9A and class 9B have %d students in total. Class 9A has %d more students than class 9B.', 'Hai lớp 9A và 9B có tổng cộng %d học sinh. Lớp 9A nhiều hơn lớp 9B %d học sinh.', 'the number of students of 9A', 'số học sinh lớp 9A', 'the number of students of 9B', 'số học sinh lớp 9B'),
    ('Two bookshelves hold %d books in total. The first shelf holds %d more books than the second one.', 'Hai giá sách có tổng cộng %d quyển sách. Giá thứ nhất nhiều hơn giá thứ hai %d quyển.', 'the number of books on the first shelf', 'số sách ở giá thứ nhất', 'the number of books on the second shelf', 'số sách ở giá thứ hai'),
    ('Two teams planted %d trees in total. Team A planted %d more trees than team B.', 'Hai đội trồng được tổng cộng %d cây. Đội A trồng nhiều hơn đội B %d cây.', 'the number of trees of team A', 'số cây đội A trồng', 'the number of trees of team B', 'số cây đội B trồng'),
    ('Two boxes contain %d apples in total. The first box has %d more apples than the second one.', 'Hai thùng có tổng cộng %d quả táo. Thùng thứ nhất nhiều hơn thùng thứ hai %d quả.', 'the number of apples in the first box', 'số táo ở thùng thứ nhất', 'the number of apples in the second box', 'số táo ở thùng thứ hai')]

def _sumdiff(r):
    y = r.randint(12, 45); d = r.randint(2, 12); x = y + d; return x, y, x + y, d

def b3_model(r, lv):
    x, y, S, d = _sumdiff(r); c = r.choice(CTX_SUM)
    good = cases('x+y=%d' % S, 'x-y=%d' % d)
    bads = [cases('x+y=%d' % S, 'y-x=%d' % d), cases('x-y=%d' % S, 'x+y=%d' % d), cases('x+y=%d' % S, 'x=%dy' % d)]
    return dict(en=(c[0] % (S, d)) + ' Let \\(x\\) be %s and \\(y\\) be %s. Which system is correct?' % (c[2], c[4]),
                vi=(c[1] % (S, d)) + ' Gọi \\(x\\) là %s, \\(y\\) là %s. Hệ phương trình nào đúng?' % (c[3], c[5]),
                opts=[good] + bads, ans=0, ee='Total: \\(x+y=%d\\). Difference: \\(x-y=%d\\).' % (S, d), ev='Tổng: \\(x+y=%d\\). Hiệu: \\(x-y=%d\\).' % (S, d))

SHOP = [('bread roll', 'ổ bánh mì', 'box of milk', 'hộp sữa'), ('notebook', 'quyển vở', 'pen', 'cây bút'), ('kilogram of oranges', 'kilôgam cam', 'kilogram of apples', 'kilôgam táo'),
        ('cup of tea', 'cốc trà sữa', 'cake', 'cái bánh ngọt')]
def _shop(r):
    while True:
        x, y = r.randint(5, 30), r.randint(4, 25); a, b, a2, b2 = r.randint(1, 4), r.randint(1, 4), r.randint(1, 4), r.randint(1, 4)
        if x != y and a * b2 - a2 * b != 0: break
    return x, y, a, b, a2, b2, a * x + b * y, a2 * x + b2 * y

def b3_shop_price(r, lv):
    x, y, a, b, a2, b2, T1, T2 = _shop(r); it = r.choice(SHOP); ask = r.choice([0, 1])
    assert solve2(a, b, T1, a2, b2, T2) == ('one', x, y)
    v = [x, y][ask]; others = [[y, x][ask], v + 1, v - 1, T1 - T2]
    en = 'Buying %d %s(s) and %d %s(es) costs %d thousand dong. Buying %d %s(s) and %d %s(es) costs %d thousand dong. What is the price of one %s?' % (a, it[0], b, it[2], T1, a2, it[0], b2, it[2], T2, [it[0], it[2]][ask])
    vi = 'Mua %d %s và %d %s hết %d nghìn đồng. Mua %d %s và %d %s hết %d nghìn đồng. Giá một %s là bao nhiêu?' % (a, it[1], b, it[3], T1, a2, it[1], b2, it[3], T2, [it[1], it[3]][ask])
    return dict(en=_plural(en), vi=vi, opts=pick_opts(r, '%d' % v, ['%d' % o for o in others if o != v and o > 0], fill=lambda t: '%d' % (v + 2 * t + 1)), ans=0,
                ee='Let \\(x, y\\) be the two prices: \\(%s\\Rightarrow x=%d,\\ y=%d\\) (thousand dong).' % (cases('%dx+%dy=%d' % (a, b, T1), '%dx+%dy=%d' % (a2, b2, T2)), x, y),
                ev='Gọi \\(x, y\\) là giá hai loại: \\(%s\\Rightarrow x=%d,\\ y=%d\\) (nghìn đồng).' % (cases('%dx+%dy=%d' % (a, b, T1), '%dx+%dy=%d' % (a2, b2, T2)), x, y))

import re
def _plural(s):
    """'1 notebook(s)' -> '1 notebook', '3 notebook(s)' -> '3 notebooks'; '(es)' tương tự."""
    def rep(m):
        n, w, suf = int(m.group(1)), m.group(2), m.group(3)
        if n == 1: return '%d %s' % (n, w)
        if w.startswith('box of'): return '%d boxes of %s' % (n, w[7:])
        if w.startswith('kilogram'): return '%d kilograms%s' % (n, w[8:])
        if w.startswith('cup of'): return '%d cups%s' % (n, w[3:])
        return '%d %s%s' % (n, w, 's')
    return re.sub(r'(\d+) ([a-z ]+?)\((e?s)\)', rep, s)

CTX_COND = [('the number of students in a class', 'số học sinh của một lớp', 'n'), ('the speed of a car (km/h)', 'vận tốc của một ô tô (km/h)', 'r'),
            ('the number of buses a school rents', 'số xe buýt nhà trường thuê', 'n'), ('the length of a rectangle (m)', 'chiều dài của một hình chữ nhật (m)', 'r'),
            ('the price of a book (thousand dong)', 'giá một quyển sách (nghìn đồng)', 'r'), ('the number of trees a team plants', 'số cây một đội trồng', 'n')]
def b3_condition(r, lv):
    c = r.choice(CTX_COND); nat = c[2] == 'n'
    o = [tx('\\(x\\) is a natural number and \\(x\\gt 0\\)', '\\(x\\) là số tự nhiên, \\(x\\gt 0\\)'), tx('\\(x\\gt 0\\) (not necessarily a whole number)', '\\(x\\gt 0\\) (không nhất thiết là số nguyên)'),
         tx('\\(x\\lt 0\\)', '\\(x\\lt 0\\)'), tx('\\(x\\) can be any real number', '\\(x\\) là số thực bất kì')]
    k = r.randint(2, 9)
    return dict(en='In a word problem, let \\(x\\) be %s. Problem number %d asks for it. What is the suitable condition for \\(x\\)?' % (c[0], k) if False else 'Let \\(x\\) be %s. What is the suitable condition for \\(x\\)?' % c[0],
                vi='Gọi \\(x\\) là %s. Điều kiện thích hợp của \\(x\\) là gì?' % c[1], opts=o, ans=0 if nat else 1,
                ee='%s' % ('A number of objects or people is a positive whole number.' if nat else 'A length, a speed or a price is a positive number, not always a whole number.'),
                ev='%s' % ('Số người, số đồ vật là số tự nhiên khác 0.' if nat else 'Độ dài, vận tốc, giá tiền là số dương, không nhất thiết là số nguyên.'))

def b3_tf_shop(r, lv):
    x, y, a, b, a2, b2, T1, T2 = _shop(r); it = r.choice(SHOP[:2]); truth = r.random() < 0.5; claim = x if truth else r.choice([y, x + 2, x - 1])
    en = _plural('%d %s(s) and %d %s(es) cost %d thousand dong; %d %s(s) and %d %s(es) cost %d thousand dong. Then one %s costs %d thousand dong.' % (a, it[0], b, it[2], T1, a2, it[0], b2, it[2], T2, it[0], claim))
    vi = '%d %s và %d %s giá %d nghìn đồng; %d %s và %d %s giá %d nghìn đồng. Khi đó một %s giá %d nghìn đồng.' % (a, it[1], b, it[3], T1, a2, it[1], b2, it[3], T2, it[1], claim)
    return dict(en=en, vi=vi, ans=(claim == x), ee='Solving the system gives %d and %d thousand dong.' % (x, y), ev='Giải hệ được giá hai loại là %d và %d nghìn đồng.' % (x, y))

def b3_tf_rect(r, lv):
    w = r.randint(3, 20); d = r.randint(1, 10); L = w + d; Pm = 2 * (L + w); S = L * w; truth = r.random() < 0.5; claim = S if truth else r.choice([S + L, S - w, (Pm // 2) ** 2 // 4 if (Pm // 2) ** 2 // 4 != S else S + 1])
    return dict(en='A rectangle has a perimeter of %d m and its length is %d m more than its width. Its area is %d m².' % (Pm, d, claim),
                vi='Một hình chữ nhật có chu vi %d m, chiều dài hơn chiều rộng %d m. Diện tích hình chữ nhật là %d m².' % (Pm, d, claim), ans=(claim == S),
                ee='\\(x+y=%d,\\ x-y=%d\\Rightarrow x=%d,\\ y=%d\\); area \\(=%d\\cdot%d=%d\\) m².' % (Pm // 2, d, L, w, L, w, S),
                ev='\\(x+y=%d,\\ x-y=%d\\Rightarrow x=%d,\\ y=%d\\); diện tích \\(=%d\\cdot%d=%d\\) m².' % (Pm // 2, d, L, w, L, w, S))

def b3_short_legs(r, lv):
    c, d = r.randint(8, 40), r.randint(5, 30); H, L = c + d, 2 * c + 4 * d
    assert solve2(1, 1, H, 2, 4, L) == ('one', c, d)
    return dict(en='A farm has chickens and dogs: %d heads and %d legs in total. How many dogs are there?' % (H, L),
                vi='Một trang trại nuôi gà và chó, có tổng cộng %d con và %d chân. Hỏi có bao nhiêu con chó?' % (H, L), key=str(d),
                ee='\\(%s\\Rightarrow x=%d,\\ y=%d\\) (\\(x\\) chickens, \\(y\\) dogs).' % (cases('x+y=%d' % H, '2x+4y=%d' % L), c, d),
                ev='\\(%s\\Rightarrow x=%d,\\ y=%d\\) (\\(x\\) con gà, \\(y\\) con chó).' % (cases('x+y=%d' % H, '2x+4y=%d' % L), c, d), hint=('Enter a whole number.', 'Nhập một số nguyên.'))

def _pct(r):
    while True:
        p, q = r.choice([10, 15, 20, 25]), r.choice([10, 12, 15, 20]); x, y = 20 * r.randint(5, 30), 20 * r.randint(5, 30)
        if p != q and x * p % 100 == 0 and y * q % 100 == 0: break
    return p, q, x, y, x + y, x + y + x * p // 100 + y * q // 100

def b3_short_percent(r, lv):
    p, q, x, y, T, T2 = _pct(r)
    assert solve2(1, 1, T, F(100 + p, 100), F(100 + q, 100), T2) == ('one', x, y)
    return dict(en='Two workshops planned to make %d products. Workshop A made %d%% more and workshop B made %d%% more than planned, so they made %d products. How many products did workshop A plan to make?' % (T, p, q, T2),
                vi='Theo kế hoạch, hai tổ sản xuất %d sản phẩm. Thực tế tổ A vượt mức %d%%, tổ B vượt mức %d%% nên cả hai tổ làm được %d sản phẩm. Theo kế hoạch, tổ A phải làm bao nhiêu sản phẩm?' % (T, p, q, T2),
                key=str(x), ee='\\(x+y=%d\\) and \\(%d\\%%x+%d\\%%y=%d\\) (the extra products). So \\(x=%d,\\ y=%d\\).' % (T, p, q, T2 - T, x, y),
                ev='\\(x+y=%d\\) và \\(%d\\%%x+%d\\%%y=%d\\) (số sản phẩm vượt mức). Suy ra \\(x=%d,\\ y=%d\\).' % (T, p, q, T2 - T, x, y), hint=('Enter a whole number.', 'Nhập một số nguyên.'))

# ---- tự luyện Bài 3
STEPS = [tx('Set up the system (choose unknowns, conditions, write two equations)', 'Lập hệ phương trình (chọn ẩn, đặt điều kiện, lập hai phương trình)'),
         tx('Solve the system', 'Giải hệ phương trình'), tx('Check the conditions and answer', 'Kiểm tra điều kiện và trả lời'), tx('Draw a graph of the two lines', 'Vẽ đồ thị hai đường thẳng')]
def b3_d1_steps(r, lv):
    k = r.choice([0, 1, 2])
    q = [('When we solve a word problem by setting up a system of equations, what is the first step?', 'Khi giải bài toán bằng cách lập hệ phương trình, bước đầu tiên là gì?'),
         ('After setting up the system for a word problem, what do we do next?', 'Sau khi lập được hệ phương trình cho bài toán, ta làm gì tiếp theo?'),
         ('After solving the system of a word problem, what is the last step?', 'Sau khi giải hệ phương trình của bài toán, bước cuối cùng là gì?')][k]
    return dict(en=q[0], vi=q[1], opts=STEPS, ans=k, ee='The three steps: set up the system – solve it – check and answer.', ev='Ba bước: lập hệ phương trình – giải hệ – kiểm tra điều kiện và trả lời.')

def b3_d1_sum(r, lv):
    S = r.randint(10, 99); kind = r.choice(['sum', 'diff'])
    if kind == 'sum':
        good, bads = 'x+y=%d' % S, ['x-y=%d' % S, 'xy=%d' % S, 'x=y+%d' % S]
        en, vi = 'The sum of two numbers \\(x\\) and \\(y\\) is %d. Which equation shows this?' % S, 'Tổng của hai số \\(x\\) và \\(y\\) là %d. Phương trình nào thể hiện điều đó?' % S
    else:
        good, bads = 'x-y=%d' % S, ['x+y=%d' % S, 'y-x=%d' % S, 'x=%dy' % S]
        en, vi = 'The number \\(x\\) is %d more than the number \\(y\\). Which equation shows this?' % S, 'Số \\(x\\) lớn hơn số \\(y\\) là %d đơn vị. Phương trình nào thể hiện điều đó?' % S
    return dict(en=en, vi=vi, opts=[good] + bads, ans=0, ee='\\(%s\\).' % good, ev='\\(%s\\).' % good)

def b3_d1_times(r, lv):
    k = r.randint(2, 9); c = r.choice([('The number of boys \\(x\\) is %d times the number of girls \\(y\\).', 'Số bạn nam \\(x\\) gấp %d lần số bạn nữ \\(y\\).'),
                                       ('The price of a bag \\(x\\) is %d times the price of a pen \\(y\\).', 'Giá một chiếc cặp \\(x\\) gấp %d lần giá một cây bút \\(y\\).'),
                                       ('The length \\(x\\) is %d times the width \\(y\\).', 'Chiều dài \\(x\\) gấp %d lần chiều rộng \\(y\\).')])
    return dict(en=(c[0] % k) + ' Which equation is correct?', vi=(c[1] % k) + ' Phương trình nào đúng?', opts=['x=%dy' % k, 'y=%dx' % k, 'x+y=%d' % k, 'x-y=%d' % k], ans=0,
                ee='“\\(x\\) is %d times \\(y\\)” means \\(x=%dy\\).' % (k, k), ev='“\\(x\\) gấp %d lần \\(y\\)” nghĩa là \\(x=%dy\\).' % (k, k))

def b3_d2_seats(r, lv):
    a, b = r.choice([(4, 7), (16, 29), (29, 45), (7, 16), (4, 16)])
    return dict(en='A company has \\(x\\) cars with %d seats and \\(y\\) cars with %d seats. What is the total number of seats?' % (a, b),
                vi='Một công ty có \\(x\\) xe %d chỗ và \\(y\\) xe %d chỗ. Tổng số chỗ ngồi là bao nhiêu?' % (a, b),
                opts=['%dx+%dy' % (a, b), '%dx+%dy' % (b, a), '%d(x+y)' % (a + b), 'x+y'], ans=0, ee='\\(%d\\) seats per car times \\(x\\) cars, plus \\(%d\\) times \\(y\\).' % (a, b), ev='Mỗi xe %d chỗ nhân với \\(x\\) xe, cộng %d nhân với \\(y\\).' % (a, b))

def b3_d2_distance(r, lv):
    t, s = r.randint(2, 5), r.randint(1, 4); assert t != s
    return dict(en='A car travels at \\(x\\) km/h for %d hours, then at \\(y\\) km/h for %d hour%s. What distance does it travel?' % (t, s, '' if s == 1 else 's'),
                vi='Một ô tô đi với vận tốc \\(x\\) km/h trong %d giờ, rồi với vận tốc \\(y\\) km/h trong %d giờ. Quãng đường ô tô đi được là bao nhiêu?' % (t, s),
                opts=['%dx+%dy' % (t, s), '%dx+%dy' % (s, t), '\\dfrac{x}{%d}+\\dfrac{y}{%d}' % (t, s), '%d(x+y)' % (t + s)], ans=0,
                ee='distance = speed × time.', ev='Quãng đường = vận tốc × thời gian.')

def b3_d2_digits(r, lv):
    v = r.choice([0, 1, 2]); k = r.randint(2, 9)
    q = [('A two-digit number has tens digit \\(x\\) and units digit \\(y\\). Which expression is the number?', 'Một số có hai chữ số, chữ số hàng chục là \\(x\\), chữ số hàng đơn vị là \\(y\\). Biểu thức nào là số đó?', ['10x+y', '10y+x', 'x+y', 'xy']),
         ('A two-digit number has tens digit \\(x\\) and units digit \\(y\\). Which expression is the number written in reverse order?', 'Một số có hai chữ số, chữ số hàng chục là \\(x\\), chữ số hàng đơn vị là \\(y\\). Biểu thức nào là số viết theo thứ tự ngược lại?', ['10y+x', '10x+y', 'x+y', 'yx']),
         ('A two-digit number has tens digit \\(x\\) and units digit \\(y\\). The sum of its digits is %d. Which equation is correct?' % k, 'Một số có hai chữ số, chữ số hàng chục là \\(x\\), chữ số hàng đơn vị là \\(y\\). Tổng các chữ số bằng %d. Phương trình nào đúng?' % k, ['x+y=%d' % k, '10x+y=%d' % k, '10y+x=%d' % k, 'xy=%d' % k])][v]
    return dict(en=q[0], vi=q[1], opts=q[2], ans=0, ee='\\(\\overline{xy}=10x+y\\).', ev='\\(\\overline{xy}=10x+y\\).')

def b3_d3_sumdiff(r, lv):
    x, y, S, d = _sumdiff(r); c = r.choice(CTX_SUM)
    return dict(en=(c[0] % (S, d)) + ' Find %s.' % c[2], vi=(c[1] % (S, d)) + ' Tìm %s.' % c[3],
                opts=pick_opts(r, str(x), [str(y), str(S - d), str(x + d), str(S // 2)]), ans=0,
                ee='\\(x+y=%d,\\ x-y=%d\\Rightarrow 2x=%d\\Rightarrow x=%d\\).' % (S, d, S + d, x), ev='\\(x+y=%d,\\ x-y=%d\\Rightarrow 2x=%d\\Rightarrow x=%d\\).' % (S, d, S + d, x))

def b3_d3_shop(r, lv):
    q = b3_shop_price(r, lv); q['en'] = re.sub(r'What is the price of one (.*)\?$', r'Find the price of one \1.', q['en']); q['vi'] = q['vi'].replace('Giá một', 'Hãy tìm giá một').replace(' là bao nhiêu?', '.')
    return q

def b3_d3_area(r, lv):
    w = r.randint(3, 25); d = r.randint(1, 12); L = w + d; Pm = 2 * (L + w); S = L * w
    return dict(en='A rectangular yard has a perimeter of %d m. Its length is %d m more than its width. Find its area.' % (Pm, d),
                vi='Một mảnh sân hình chữ nhật có chu vi %d m, chiều dài hơn chiều rộng %d m. Tính diện tích mảnh sân.' % (Pm, d),
                opts=pick_opts(r, '%d\\text{ m}^2' % S, ['%d\\text{ m}^2' % o for o in (Pm * d, (L + d) * w, L * L, w * w) if o != S]), ans=0,
                ee='\\(x+y=%d,\\ x-y=%d\\Rightarrow x=%d,\\ y=%d\\). Area \\(=%d\\) m².' % (Pm // 2, d, L, w, S), ev='\\(x+y=%d,\\ x-y=%d\\Rightarrow x=%d,\\ y=%d\\). Diện tích \\(=%d\\) m².' % (Pm // 2, d, L, w, S))

def b3_d4_legs(r, lv):
    c, d = r.randint(8, 40), r.randint(5, 30); H, L = c + d, 2 * c + 4 * d
    return dict(en='A yard has chickens and rabbits: %d animals and %d legs. How many chickens are there?' % (H, L),
                vi='Trong sân có gà và thỏ, tổng cộng %d con và %d chân. Có bao nhiêu con gà?' % (H, L),
                opts=pick_opts(r, str(c), [str(d), str(L // 4), str(H - L // 4) if H - L // 4 > 0 else str(c + 2), str(c + 1)], fill=lambda t: str(c + 2 * t + 2)), ans=0,
                ee='\\(%s\\Rightarrow x=%d\\) chickens, \\(y=%d\\) rabbits.' % (cases('x+y=%d' % H, '2x+4y=%d' % L), c, d), ev='\\(%s\\Rightarrow x=%d\\) con gà, \\(y=%d\\) con thỏ.' % (cases('x+y=%d' % H, '2x+4y=%d' % L), c, d))

def b3_d4_percent(r, lv):
    p, q, x, y, T, T2 = _pct(r)
    return dict(en='Two schools planned to collect %d kg of waste paper. School A collected %d%% more and school B %d%% more than planned, so they collected %d kg. How many kilograms did school B plan to collect?' % (T, p, q, T2),
                vi='Theo kế hoạch, hai trường thu gom %d kg giấy vụn. Thực tế trường A vượt %d%%, trường B vượt %d%% kế hoạch nên thu được %d kg. Theo kế hoạch, trường B phải thu gom bao nhiêu kilôgam?' % (T, p, q, T2),
                opts=pick_opts(r, str(y), [str(x), str(T2 - x), str(T - y + 20), str(y + 20)], fill=lambda t: str(y + 40 * t)), ans=0,
                ee='\\(x+y=%d\\), \\(%d\\%%x+%d\\%%y=%d\\Rightarrow x=%d,\\ y=%d\\).' % (T, p, q, T2 - T, x, y), ev='\\(x+y=%d\\), \\(%d\\%%x+%d\\%%y=%d\\Rightarrow x=%d,\\ y=%d\\).' % (T, p, q, T2 - T, x, y))

def b3_d4_speed(r, lv):
    while True:
        u, v = 5 * r.randint(8, 16), 5 * r.randint(4, 12); t1 = r.choice([1, 2, 3])
        if u - v >= 10 and t1 * (u + v) % (u - v) == 0 and t1 * (u + v) // (u - v) <= 8: break
    D = t1 * (u + v)
    t2 = F(D, u - v)
    assert t2.denominator == 1
    t2 = int(t2)
    assert solve2(t1, t1, D, t2, -t2, D) == ('one', u, v)
    return dict(en='Two cars start at the same time from two towns %d km apart. If they drive toward each other, they meet after %d hour%s. If they drive in the same direction, the faster car catches up with the other after %d hours. Find the speed of the faster car.' % (D, t1, '' if t1 == 1 else 's', t2),
                vi='Hai ô tô khởi hành cùng lúc từ hai thị trấn cách nhau %d km. Nếu đi ngược chiều thì sau %d giờ chúng gặp nhau. Nếu đi cùng chiều thì sau %d giờ xe nhanh đuổi kịp xe kia. Tính vận tốc của xe đi nhanh hơn.' % (D, t1, t2),
                opts=pick_opts(r, '%d\\text{ km/h}' % u, ['%d\\text{ km/h}' % o for o in (v, u + v, u - v, u + 5)]), ans=0,
                ee='\\(%s\\Rightarrow x=%d,\\ y=%d\\).' % (cases('%d(x+y)=%d' % (t1, D), '%d(x-y)=%d' % (t2, D)), u, v), ev='\\(%s\\Rightarrow x=%d,\\ y=%d\\).' % (cases('%d(x+y)=%d' % (t1, D), '%d(x-y)=%d' % (t2, D)), u, v))

L3_GROUPS = [[('mcq', b3_model), ('mcq', b3_shop_price), ('mcq', b3_condition)], [('tf', b3_tf_shop), ('tf', b3_tf_rect)], [('short', b3_short_legs), ('short', b3_short_percent)],
             [('mcq', b3_d1_steps), ('mcq', b3_d1_sum), ('mcq', b3_d1_times)], [('mcq', b3_d2_seats), ('mcq', b3_d2_distance), ('mcq', b3_d2_digits)],
             [('mcq', b3_d3_sumdiff), ('mcq', b3_d3_shop), ('mcq', b3_d3_area)], [('mcq', b3_d4_legs), ('mcq', b3_d4_percent), ('mcq', b3_d4_speed)]]

# =====================================================================================================
# BÀI 4. Phương trình quy về phương trình bậc nhất một ẩn
# =====================================================================================================
def S2(a, b):
    """Tập nghiệm hai phần tử theo SGK: S = {a; b} (sắp xếp tăng dần)."""
    a, b = sorted([F(a), F(b)])
    return 'S=\\{%s;\\ %s\\}' % (fr(a), fr(b)) if a != b else 'S=\\{%s\\}' % fr(a)

def factor(a, b):
    """(ax+b) dạng tex; a ≠ 0."""
    return '(%s)' % lin((a, 'x'), (b, '')) if b else lin((a, 'x')) if a not in (1, -1) else ('x' if a == 1 else '(-x)')

def _prod(r, frac=True):
    a, c = (r.choice([1, 2, 3, -2]), r.choice([1, 2, 3, 4, -3])) if frac else (1, 1)
    r1 = F(r.randint(-6, 6), 1); r2 = F(r.randint(-9, 9), c) if frac else F(r.randint(-7, 7))
    # (a x - a r1)(c x - c r2) với hệ số nguyên
    b = -a * r1; d = -c * r2; assert b.denominator == 1 and d.denominator == 1 and r1 != r2
    return a, int(b), c, int(d), r1, r2

def b4_prod_solve(r, lv):
    a, b, c, d, r1, r2 = _prod(r)
    e = '%s%s=0' % (factor(a, b), factor(c, d))
    good = S2(r1, r2); bads = [S2(-r1, -r2), S2(r1, -r2), S2(-r1, r2), S2(F(-b), F(-d)) if (F(-b), F(-d)) != (r1, r2) else S2(r1 + 1, r2)]
    return dict(en='Solve the equation \\(%s\\).' % e, vi='Giải phương trình \\(%s\\).' % e, opts=pick_opts(r, good, [x for x in bads if x != good], fill=lambda t: S2(r1 + t, r2 - t)), ans=0,
                ee='\\(%s=0\\) or \\(%s=0\\), so \\(x=%s\\) or \\(x=%s\\).' % (lin((a, 'x'), (b, '')), lin((c, 'x'), (d, '')), fr(r1), fr(r2)),
                ev='\\(%s=0\\) hoặc \\(%s=0\\), suy ra \\(x=%s\\) hoặc \\(x=%s\\).' % (lin((a, 'x'), (b, '')), lin((c, 'x'), (d, '')), fr(r1), fr(r2)))

def b4_dkxd(r, lv):
    p, q = nz(r, -7, 7), nz(r, -7, 7); assert p != -q
    m, k = nz(r, -5, 5), nz(r, -5, 5)
    e = '\\dfrac{%d}{x%s}+\\dfrac{x}{x%s}=%d' % (m, mono(-p, '', False), mono(q, '', False), k)
    good = 'x\\ne %d,\\ x\\ne %d' % (p, -q); bads = ['x\\ne %d,\\ x\\ne %d' % (-p, q), 'x\\ne %d' % p, 'x\\ne %d' % (-q), 'x\\ne 0']
    return dict(en='Find the condition for the equation \\(%s\\) to be defined.' % e, vi='Tìm điều kiện xác định của phương trình \\(%s\\).' % e, opts=pick_opts(r, good, bads), ans=0,
                ee='All denominators must be nonzero: \\(x%s\\ne0\\) and \\(x%s\\ne0\\).' % (mono(-p, '', False), mono(q, '', False)),
                ev='Mọi mẫu thức phải khác 0: \\(x%s\\ne0\\) và \\(x%s\\ne0\\).' % (mono(-p, '', False), mono(q, '', False)))

def b4_common(r, lv):
    t = r.choice(['kx2', 'sq'])
    if t == 'kx2':
        k, m = nz(r, -5, 5), nz(r, -12, 12); assert F(m, k) != 0
        e = '%s%s=0' % (lin((k, 'x^2')), mono(-m, 'x', False)); good = S2(0, F(m, k)); bads = [S2(0, F(-m, k)), 'S=\\{%s\\}' % fr(F(m, k)), S2(F(m, k), F(-m, k))]
        ee = ('Factor: \\(x(%s)=0\\), so \\(x=0\\) or \\(x=%s\\).' % (lin((k, 'x'), (-m, '')), fr(F(m, k))), 'Đặt nhân tử chung: \\(x(%s)=0\\), suy ra \\(x=0\\) hoặc \\(x=%s\\).' % (lin((k, 'x'), (-m, '')), fr(F(m, k))))
    else:
        n = r.randint(2, 12); e = 'x^2-%d=0' % (n * n); good = S2(-n, n); bads = ['S=\\{%d\\}' % n, 'S=\\{%d\\}' % (n * n), S2(-n * n, n * n)]
        ee = ('\\((x-%d)(x+%d)=0\\), so \\(x=%d\\) or \\(x=-%d\\).' % (n, n, n, n), '\\((x-%d)(x+%d)=0\\), suy ra \\(x=%d\\) hoặc \\(x=-%d\\).' % (n, n, n, n))
    return dict(en='Find the solution set of the equation \\(%s\\).' % e, vi='Tìm tập nghiệm của phương trình \\(%s\\).' % e, opts=[good] + bads, ans=0, ee=ee[0], ev=ee[1])

def _frac_eq(r):
    """\\dfrac{kx}{x-p} - \\dfrac{m}{x} = k  ->  x = mp/(m - kp): nghiệm nguyên, khác 0 và p."""
    while True:
        k, p, m = r.randint(1, 3), nz(r, -6, 6), r.randint(1, 9)
        if m - k * p == 0: continue
        x = F(m * p, m - k * p)
        if x.denominator == 1 and x not in (0, p): return k, p, m, int(x)

def _fe_tex(k, p, m):
    return '\\dfrac{%sx}{x%s}-\\dfrac{%d}{x}=%d' % ('' if k == 1 else '-' if k == -1 else k, mono(-p, '', False), m, k)

def b4_tf_root(r, lv):
    k, p, m, x = _frac_eq(r); truth = r.random() < 0.5
    claim = x if truth else r.choice([p, 0, -x if -x != x else x + 1])
    e = _fe_tex(k, p, m)
    why = ('Condition: \\(x\\ne0,\\ x\\ne%d\\). Clearing denominators gives \\(x=%d\\), which satisfies the condition.' % (p, x),
           'Điều kiện: \\(x\\ne0,\\ x\\ne%d\\). Khử mẫu được \\(x=%d\\), thỏa mãn điều kiện.' % (p, x))
    return dict(en='The equation \\(%s\\) has the solution \\(x=%d\\).' % (e, claim), vi='Phương trình \\(%s\\) có nghiệm \\(x=%d\\).' % (e, claim), ans=(claim == x), ee=why[0], ev=why[1])

def b4_tf_prod(r, lv):
    a, b = nz(r, -8, 8), nz(r, -8, 8); assert a != -b
    truth = r.random() < 0.5; s = (a, -b) if truth else r.choice([(a, b), (-a, -b), (-a, b)])
    assert truth or s != (a, -b)
    e = '(x%s)(x%s)=0' % (mono(-a, '', False), mono(b, '', False))
    return dict(en='The equation \\(%s\\) has two solutions \\(x=%d\\) and \\(x=%d\\).' % (e, s[0], s[1]), vi='Phương trình \\(%s\\) có hai nghiệm \\(x=%d\\) và \\(x=%d\\).' % (e, s[0], s[1]),
                ans=truth, ee='\\(x%s=0\\Rightarrow x=%d\\); \\(x%s=0\\Rightarrow x=%d\\).' % (mono(-a, '', False), a, mono(b, '', False), -b),
                ev='\\(x%s=0\\Rightarrow x=%d\\); \\(x%s=0\\Rightarrow x=%d\\).' % (mono(-a, '', False), a, mono(b, '', False), -b))

def b4_short_sum(r, lv):
    a, b, c, d, r1, r2 = _prod(r, frac=False); e = '%s%s=0' % (factor(a, b), factor(c, d))
    return dict(en='Find the sum of all solutions of the equation \\(%s\\).' % e, vi='Tính tổng các nghiệm của phương trình \\(%s\\).' % e, key=fr(r1 + r2),
                ee='The solutions are \\(%s\\) and \\(%s\\); their sum is \\(%s\\).' % (fr(r1), fr(r2), fr(r1 + r2)), ev='Hai nghiệm là \\(%s\\) và \\(%s\\); tổng bằng \\(%s\\).' % (fr(r1), fr(r2), fr(r1 + r2)))

def b4_short_frac(r, lv):
    k, p, m, x = _frac_eq(r); e = _fe_tex(k, p, m)
    return dict(en='Solve the equation \\(%s\\).' % e, vi='Giải phương trình \\(%s\\).' % e, key=str(x),
                ee='Condition \\(x\\ne0,\\ x\\ne%d\\). Multiply by \\(x(x%s)\\): \\(%s=%s\\Rightarrow x=%d\\) (accepted).' % (p, mono(-p, '', False), lin((k, 'x^2'), (-m, 'x'), (m * p, '')), lin((k, 'x^2'), (-k * p, 'x')), x),
                ev='Điều kiện \\(x\\ne0,\\ x\\ne%d\\). Nhân hai vế với \\(x(x%s)\\): \\(%s=%s\\Rightarrow x=%d\\) (thỏa mãn).' % (p, mono(-p, '', False), lin((k, 'x^2'), (-m, 'x'), (m * p, '')), lin((k, 'x^2'), (-k * p, 'x')), x))

# ---- tự luyện Bài 4
def b4_d1_zero(r, lv):
    a, b = nz(r, -9, 9), nz(r, -9, 9); assert a != b
    A, B = 'x%s' % mono(-a, '', False), 'x%s' % mono(-b, '', False)
    o = [tx('\\(%s=0\\) or \\(%s=0\\)' % (A, B), '\\(%s=0\\) hoặc \\(%s=0\\)' % (A, B)), tx('\\(%s=0\\) and \\(%s=0\\)' % (A, B), '\\(%s=0\\) và \\(%s=0\\)' % (A, B)),
         tx('\\(%s=%s\\)' % (A, B), '\\(%s=%s\\)' % (A, B)), tx('\\(%s=1\\) or \\(%s=1\\)' % (A, B), '\\(%s=1\\) hoặc \\(%s=1\\)' % (A, B))]
    e = '(%s)(%s)=0' % (A, B)
    return dict(en='The equation \\(%s\\) is equivalent to…' % e, vi='Phương trình \\(%s\\) tương đương với…' % e, opts=o, ans=0,
                ee='A product is zero when at least one factor is zero.', ev='Tích bằng 0 khi có ít nhất một thừa số bằng 0.')

def b4_d1_dk(r, lv):
    p, n = nz(r, -9, 9), r.choice([1, 2, 3, 5, 7])
    e = '\\dfrac{%d}{x%s}=%d' % (n, mono(-p, '', False), r.randint(1, 9))
    return dict(en='What is the condition for the equation \\(%s\\) to be defined?' % e, vi='Điều kiện xác định của phương trình \\(%s\\) là gì?' % e,
                opts=pick_opts(r, 'x\\ne %d' % p, ['x\\ne %d' % o for o in (-p, n, 0) if o != p], fill=lambda t: 'x\\ne %d' % (p + 10 * t)), ans=0,
                ee='The denominator \\(x%s\\) must be nonzero.' % mono(-p, '', False), ev='Mẫu thức \\(x%s\\) phải khác 0.' % mono(-p, '', False))

def b4_d1_which(r, lv):
    a, b, c = nz(r, -7, 7), nz(r, -7, 7), nz(r, 2, 9); assert a != -b
    A, B = 'x%s' % mono(-a, '', False), 'x%s' % mono(b, '', False)
    good = '(%s)(%s)=0' % (A, B); bads = ['(%s)+(%s)=0' % (A, B), '(%s)(%s)=%d' % (A, B, c), '\\dfrac{%s}{%s}=%d' % (A, B, c)]
    q = r.choice([('Which equation is a product equation?', 'Phương trình nào là phương trình tích?'), ('Choose the product equation.', 'Chọn phương trình tích.'),
                  ('Which of these equations has the form \\(A\\cdot B=0\\)?', 'Phương trình nào có dạng \\(A\\cdot B=0\\)?'), ('Only one equation is a product equation. Which one?', 'Chỉ có một phương trình tích. Đó là phương trình nào?')])
    return dict(en=q[0], vi=q[1], opts=[good] + bads, ans=0, ee='A product equation has the form \\(A\\cdot B=0\\) (the right-hand side is 0).', ev='Phương trình tích có dạng \\(A\\cdot B=0\\) (vế phải bằng 0).')

def b4_d2_prod(r, lv):
    q = b4_prod_solve(r, lv); q['en'] = q['en'].replace('Solve the equation', 'Find the solution set of'); q['vi'] = q['vi'].replace('Giải phương trình', 'Tìm tập nghiệm của phương trình')
    return q

def b4_d2_common(r, lv):
    a, b, k = nz(r, -6, 6), nz(r, -6, 6), nz(r, -5, 5); r1, r2 = -a, b - k; assert r1 != r2 and a != -b
    e = '(x%s)(x%s)%s=0' % (mono(a, '', False), mono(-b, '', False), mono(k, '(x%s)' % mono(a, '', False), False))
    return dict(en='Solve the equation \\(%s\\).' % e, vi='Giải phương trình \\(%s\\).' % e, opts=pick_opts(r, S2(r1, r2), [S2(-r1, r2), S2(r1, b), S2(r1, b + k), S2(-r1, -r2)]), ans=0,
                ee='Common factor \\(x%s\\): \\((x%s)(x%s)=0\\), so \\(x=%d\\) or \\(x=%d\\).' % (mono(a, '', False), mono(a, '', False), mono(k - b, '', False), r1, r2),
                ev='Nhân tử chung \\(x%s\\): \\((x%s)(x%s)=0\\), suy ra \\(x=%d\\) hoặc \\(x=%d\\).' % (mono(a, '', False), mono(a, '', False), mono(k - b, '', False), r1, r2))

def b4_d2_dk2(r, lv):
    p = nz(r, -9, 9); n = r.randint(1, 9)
    e = '\\dfrac{%d}{x(x%s)}=\\dfrac{1}{x}' % (n, mono(-p, '', False))
    good = 'x\\ne0,\\ x\\ne %d' % p
    return dict(en='Find the condition for the equation \\(%s\\) to be defined.' % e, vi='Tìm điều kiện xác định của phương trình \\(%s\\).' % e,
                opts=pick_opts(r, good, ['x\\ne0,\\ x\\ne %d' % (-p), 'x\\ne %d' % p, 'x\\ne0']), ans=0,
                ee='\\(x(x%s)\\ne0\\) means \\(x\\ne0\\) and \\(x\\ne%d\\).' % (mono(-p, '', False), p), ev='\\(x(x%s)\\ne0\\) khi \\(x\\ne0\\) và \\(x\\ne%d\\).' % (mono(-p, '', False), p))

def b4_d3_frac(r, lv):
    while True:
        a, b, p, q = r.randint(1, 7), r.randint(1, 7), nz(r, -6, 6), nz(r, -6, 6)
        if a != b and p != q:
            x = F(a * q - b * p, a - b)
            if x.denominator == 1 and x not in (p, q): break
    x = int(x); assert F(a, x - p) == F(b, x - q)
    e = '\\dfrac{%d}{x%s}=\\dfrac{%d}{x%s}' % (a, mono(-p, '', False), b, mono(-q, '', False))
    return dict(en='Solve the equation \\(%s\\).' % e, vi='Giải phương trình \\(%s\\).' % e,
                opts=pick_opts(r, 'x=%d' % x, ['x=%d' % o for o in (-x, p, q, x + 1) if o != x]), ans=0,
                ee='Condition \\(x\\ne%d,\\ x\\ne%d\\). Cross-multiply: \\(%d(x%s)=%d(x%s)\\Rightarrow x=%d\\).' % (p, q, a, mono(-q, '', False), b, mono(-p, '', False), x),
                ev='Điều kiện \\(x\\ne%d,\\ x\\ne%d\\). Khử mẫu: \\(%d(x%s)=%d(x%s)\\Rightarrow x=%d\\).' % (p, q, a, mono(-q, '', False), b, mono(-p, '', False), x))

def b4_d3_extra(r, lv):
    p, k = r.randint(1, 7), r.choice([2, 3, 4, 5])
    e = '\\dfrac{1}{x-%d}+%d=\\dfrac{x-%d}{%d-x}' % (p, k, p + 1, p)
    # 1 + k(x-p) = -(x-p-1)  <=>  (k+1)x = (k+1)p  <=>  x = p (bị loại)
    for xv in range(-20, 21):
        if xv == p: continue
        assert F(1, xv - p) + k != F(xv - p - 1, p - xv)
    o = [tx('no solution', 'vô nghiệm'), tx('\\(x=%d\\)' % p, '\\(x=%d\\)' % p), tx('\\(x=%d\\)' % (p + 1), '\\(x=%d\\)' % (p + 1)), tx('\\(x=%d\\)' % (-p), '\\(x=%d\\)' % (-p))]
    return dict(en='Solve the equation \\(%s\\).' % e, vi='Giải phương trình \\(%s\\).' % e, opts=o, ans=0,
                ee='Condition \\(x\\ne%d\\). Clearing denominators gives \\(%dx=%d\\), so \\(x=%d\\) – but this value is excluded. The equation has no solution.' % (p, k + 1, (k + 1) * p, p),
                ev='Điều kiện \\(x\\ne%d\\). Khử mẫu được \\(%dx=%d\\), suy ra \\(x=%d\\) – giá trị này không thỏa mãn điều kiện. Phương trình vô nghiệm.' % (p, k + 1, (k + 1) * p, p))

def b4_d3_diffsq(r, lv):
    while True:
        n, m = r.randint(1, 8), r.randint(-12, 12)
        if (n + m) % 3 == 0 and F(-(n + m), 3) != n: break
    r2 = F(-(n + m), 3)
    e = 'x^2-%d+(x-%d)(2x%s)=0' % (n * n, n, mono(m, '', False))
    return dict(en='Solve the equation \\(%s\\).' % e, vi='Giải phương trình \\(%s\\).' % e,
                opts=pick_opts(r, S2(n, r2), [S2(-n, r2), S2(n, -r2), 'S=\\{%d\\}' % n, S2(n, F(-m, 2))]), ans=0,
                ee='\\((x-%d)(x+%d)+(x-%d)(2x%s)=(x-%d)(3x%s)=0\\).' % (n, n, n, mono(m, '', False), n, mono(n + m, '', False)),
                ev='\\((x-%d)(x+%d)+(x-%d)(2x%s)=(x-%d)(3x%s)=0\\).' % (n, n, n, mono(m, '', False), n, mono(n + m, '', False)))

def b4_d4_canoe(r, lv):
    while True:
        v, x = r.choice([2, 3, 4]), r.randint(10, 30); D1 = r.randint(2, 6) * (x + v); t = F(D1, x + v); D2 = t * (x - v)
        if D2.denominator == 1 and D2 > 0: break
    D2 = int(D2); assert F(D1, x + v) == F(D2, x - v)
    return dict(en='A boat goes %d km downstream and %d km upstream; the two trips take the same time. The current flows at %d km/h. Find the speed of the boat in still water.' % (D1, D2, v),
                vi='Một ca nô xuôi dòng %d km và ngược dòng %d km, thời gian hai lần đi bằng nhau. Vận tốc dòng nước là %d km/h. Tính vận tốc của ca nô khi nước yên lặng.' % (D1, D2, v),
                opts=pick_opts(r, '%d\\text{ km/h}' % x, ['%d\\text{ km/h}' % o for o in (x + v, x - v, x + 2 * v, D1 - D2)]), ans=0,
                ee='\\(\\dfrac{%d}{x+%d}=\\dfrac{%d}{x-%d}\\) (\\(x\\gt %d\\)) \\(\\Rightarrow %d(x-%d)=%d(x+%d)\\Rightarrow x=%d\\).' % (D1, v, D2, v, v, D1, v, D2, v, x),
                ev='\\(\\dfrac{%d}{x+%d}=\\dfrac{%d}{x-%d}\\) (\\(x\\gt %d\\)) \\(\\Rightarrow %d(x-%d)=%d(x+%d)\\Rightarrow x=%d\\).' % (D1, v, D2, v, v, D1, v, D2, v, x))

def b4_d4_trucks(r, lv):
    while True:
        x, d, n = r.randint(3, 8), r.randint(2, 4), r.randint(10, 40); M2, M1 = n * x, n * (x + d)
        if M1 != M2: break
    assert F(M1, x + d) == F(M2, x)
    return dict(en='Truck A carries %d tonnes of goods and truck B carries %d tonnes, with the same number of trips. On each trip, truck A carries %d tonnes more than truck B. How many tonnes does truck B carry on each trip?' % (M1, M2, d),
                vi='Xe A chở %d tấn hàng, xe B chở %d tấn hàng, số chuyến của hai xe bằng nhau. Mỗi chuyến xe A chở nhiều hơn xe B %d tấn. Mỗi chuyến xe B chở bao nhiêu tấn?' % (M1, M2, d),
                opts=pick_opts(r, str(x), [str(x + d), str(n), str(M1 - M2), str(x + 1)], fill=lambda t: str(x + 2 * t + 2)), ans=0,
                ee='\\(\\dfrac{%d}{x+%d}=\\dfrac{%d}{x}\\Rightarrow %dx=%d(x+%d)\\Rightarrow x=%d\\).' % (M1, d, M2, M1, M2, d, x),
                ev='\\(\\dfrac{%d}{x+%d}=\\dfrac{%d}{x}\\Rightarrow %dx=%d(x+%d)\\Rightarrow x=%d\\).' % (M1, d, M2, M1, M2, d, x))

def b4_d4_gen(r, lv):
    while True:
        a, b, c, d = nz(r, -6, 6), nz(r, -6, 6), nz(r, -6, 6), nz(r, -6, 6)
        den = a + d - c + b
        if den == 0 or b == -d or a == c: continue
        x = F(-b * c - a * d, den)
        if x.denominator == 1 and x not in (b, -d): break
    x = int(x); assert F(x + a, x - b) == F(x + c, x + d)
    e = '\\dfrac{%s}{x%s}=\\dfrac{%s}{x%s}' % (lin((1, 'x'), (a, '')), mono(-b, '', False), lin((1, 'x'), (c, '')), mono(d, '', False))
    return dict(en='Solve the equation \\(%s\\).' % e, vi='Giải phương trình \\(%s\\).' % e,
                opts=pick_opts(r, 'x=%d' % x, ['x=%d' % o for o in (-x, b, -d, x + 1) if o != x], fill=lambda t: 'x=%d' % (x + 3 * t)), ans=0,
                ee='Condition \\(x\\ne%d,\\ x\\ne%d\\). Cross-multiply: \\((%s)(%s)=(%s)(%s)\\Rightarrow %s=%d\\Rightarrow x=%d\\).' % (b, -d, lin((1, 'x'), (a, '')), lin((1, 'x'), (d, '')), lin((1, 'x'), (c, '')), lin((1, 'x'), (-b, '')), lin((den, 'x')), -b * c - a * d, x),
                ev='Điều kiện \\(x\\ne%d,\\ x\\ne%d\\). Khử mẫu: \\((%s)(%s)=(%s)(%s)\\Rightarrow %s=%d\\Rightarrow x=%d\\).' % (b, -d, lin((1, 'x'), (a, '')), lin((1, 'x'), (d, '')), lin((1, 'x'), (c, '')), lin((1, 'x'), (-b, '')), lin((den, 'x')), -b * c - a * d, x))

L4_GROUPS = [[('mcq', b4_prod_solve), ('mcq', b4_dkxd), ('mcq', b4_common)], [('tf', b4_tf_root), ('tf', b4_tf_prod)], [('short', b4_short_sum), ('short', b4_short_frac)],
             [('mcq', b4_d1_zero), ('mcq', b4_d1_dk), ('mcq', b4_d1_which)], [('mcq', b4_d2_prod), ('mcq', b4_d2_common), ('mcq', b4_d2_dk2)],
             [('mcq', b4_d3_frac), ('mcq', b4_d3_extra), ('mcq', b4_d3_diffsq)], [('mcq', b4_d4_canoe), ('mcq', b4_d4_trucks), ('mcq', b4_d4_gen)]]

# =====================================================================================================
# Nhãn điểm trên hình: đặt vuông góc với các đường thẳng đi qua điểm, tránh trục tọa độ (không bị đè, không bị cắt)
# =====================================================================================================
import math as _m
def auto_labels(cfg, dist=11):
    """Tính 'off' cho mọi điểm có tên chưa đặt tay: chọn trong 8 hướng hướng xa nhất (theo góc) với các đường thẳng
    đi qua điểm (lineeq, đoạn/đường qua điểm), với trục tọa độ nếu điểm nằm trên trục, và với các điểm có tên ở gần."""
    cfg = dict(cfg); cfg['shiftLabels'] = True; steps = [dict(s) for s in cfg['steps']]
    pts = {s['id']: tuple(s['at']) for s in steps if s['type'] in ('point', 'glider')}
    for s in steps:
        if s['type'] not in ('point', 'glider') or s.get('off') is not None: continue
        X, Y = s['at']; dirs = []; rays = []
        poly = [t for t in steps if t['type'] == 'polygon' and s['id'] in t['through']]
        if poly:                                   # đỉnh đa giác: đặt nhãn theo phân giác ngoài (ra ngoài hình)
            th = poly[0]['through']; i = th.index(s['id']); Pp, Q = pts[th[i - 1]], pts[th[(i + 1) % len(th)]]
            u = (Pp[0] - X, Pp[1] - Y); v = (Q[0] - X, Q[1] - Y); nu, nv = _m.hypot(*u), _m.hypot(*v)
            w = (-(u[0] / nu + v[0] / nv), -(u[1] / nu + v[1] / nv)); nw = _m.hypot(*w) or 1
            s['off'] = [round(dist * w[0] / nw, 2), round(dist * w[1] / nw, 2)]; continue
        for t in steps:
            if t['type'] == 'lineeq' and abs(t['a'] * X + t['b'] * Y + t['c']) < 1e-9 * (abs(t['a']) + abs(t['b'])) + 1e-9:
                dirs.append(_m.atan2(-t['a'], t['b']))
            if t['type'] in ('segment', 'line') and s['id'] in [r for r in t['through'] if isinstance(r, str)]:
                o = [r for r in t['through'] if r != s['id']][0]; Q = pts[o] if isinstance(o, str) else o
                if t['type'] == 'segment': rays.append(_m.atan2(Q[1] - Y, Q[0] - X))   # đầu mút đoạn thẳng: chỉ một phía
                else: dirs.append(_m.atan2(Q[1] - Y, Q[0] - X))
        if cfg.get('axes'):
            if abs(Y) < 1e-9: dirs.append(0.0)
            if abs(X) < 1e-9: dirs.append(_m.pi / 2)
        near = [_m.atan2(q[1] - Y, q[0] - X) for i, q in pts.items() if i != s['id'] and _m.hypot(q[0] - X, q[1] - Y) < 1.6]
        def score(a):
            def ad(u, v, line=True):
                d = abs((u - v + _m.pi) % (2 * _m.pi) - _m.pi)
                return min(d, _m.pi - d) if line else d
            sc = min([ad(a, d) for d in dirs] + [ad(a, d, False) for d in rays] + [ad(a, d, False) * 0.8 for d in near] + [_m.pi])
            return sc + 0.01 * _m.cos(a - _m.pi / 4)      # hòa thì ưu tiên phía trên bên phải
        best = max((k * _m.pi / 8 for k in range(16)), key=score)
        s['off'] = [round(dist * _m.cos(best), 2), round(dist * _m.sin(best), 2)]
    cfg['steps'] = steps
    return cfg

def _gl(x):
    return x

REL = {'<': '\\lt ', '>': '\\gt ', '<=': '\\le ', '>=': '\\ge '}
FLIP = {'<': '>', '>': '<', '<=': '>=', '>=': '<='}
def holds(a, op, b):
    return {'<': a < b, '>': a > b, '<=': a <= b, '>=': a >= b}[op]

# =====================================================================================================
# BÀI 5. Bất đẳng thức và tính chất
# =====================================================================================================
SIT = [('The age \\(a\\) of a viewer must be at least %d years.', 'Tuổi \\(a\\) của người xem phải ít nhất là %d tuổi.', 'a', '>='),
       ('The load \\(m\\) (kg) of a lift must not exceed %d kg.', 'Khối lượng \\(m\\) (kg) chở trong thang máy không được vượt quá %d kg.', 'm', '<='),
       ('The number of students \\(s\\) in a class is at most %d.', 'Số học sinh \\(s\\) của một lớp nhiều nhất là %d.', 's', '<='),
       ('The height \\(h\\) (m) of a drone is greater than %d m.', 'Độ cao \\(h\\) (m) của một chiếc flycam lớn hơn %d m.', 'h', '>'),
       ('The speed \\(v\\) (km/h) on this road must be less than %d km/h.', 'Tốc độ \\(v\\) (km/h) trên đoạn đường này phải nhỏ hơn %d km/h.', 'v', '<'),
       ('The score \\(d\\) needed to pass is at least %d points.', 'Điểm \\(d\\) để đạt phải ít nhất là %d điểm.', 'd', '>=')]
def b5_translate(r, lv):
    en, vi, v, op = r.choice(SIT); n = r.randint(5, 900) if v in ('m', 'h') else r.randint(5, 60)
    opts = ['%s%s %d' % (v, REL[o], n) for o in (op, '<', '>', '<=', '>=') ]
    opts = [opts[0]] + [o for o in opts[1:] if o != opts[0]]
    return dict(en=(en % n) + ' Which inequality describes this?', vi=(vi % n) + ' Bất đẳng thức nào mô tả điều đó?', opts=opts[:4], ans=0,
                ee='“at least” → \\(\\ge\\); “at most”, “not exceed” → \\(\\le\\); “greater than” → \\(\\gt\\); “less than” → \\(\\lt\\).',
                ev='“ít nhất” → \\(\\ge\\); “nhiều nhất”, “không vượt quá” → \\(\\le\\); “lớn hơn” → \\(\\gt\\); “nhỏ hơn” → \\(\\lt\\).')

def b5_property(r, lv):
    op = r.choice(['<', '>']); k = -r.randint(2, 6); c = nz(r, -9, 9)
    good = '%da%s %s %db%s' % (k, mono(c, '', False), REL[FLIP[op]], k, mono(c, '', False))
    bads = ['%da%s %s %db%s' % (k, mono(c, '', False), REL[op], k, mono(c, '', False)),
            'a%s %s b%s' % (mono(c, '', False), REL[FLIP[op]], mono(c, '', False)),
            '%da %s %db' % (-k, REL[FLIP[op]], -k)]
    E1, E2 = lin((k, 'a'), (c, '')), lin((k, 'b'), (c, ''))
    return dict(en='Given \\(a%sb\\). Compare \\(%s\\) and \\(%s\\): which inequality is true?' % (REL[op], E1, E2), vi='Cho \\(a%sb\\). So sánh \\(%s\\) và \\(%s\\): bất đẳng thức nào đúng?' % (REL[op], E1, E2), opts=[good] + bads, ans=0,
                ee='Multiplying by the negative number \\(%d\\) reverses the sign; adding \\(%d\\) keeps it.' % (k, c),
                ev='Nhân với số âm \\(%d\\) thì đổi chiều; cộng \\(%d\\) thì giữ nguyên chiều.' % (k, c))

def b5_compare(r, lv):
    while True:
        a, b, c, d = r.randint(2, 40), r.randint(2, 40), r.randint(2, 40), r.randint(2, 40)
        x, y = F(a, b), F(c, d)
        if x.denominator == b and y.denominator == d and x != y and abs(x - y) < F(1, 3): break
    sym = '\\lt' if x < y else '\\gt'
    fx_, fy_ = '\\dfrac{%d}{%d}' % (a, b), '\\dfrac{%d}{%d}' % (c, d)
    opts = ['%s%s%s' % (fx_, s_, fy_) for s_ in (sym, '\\gt' if sym == '\\lt' else '\\lt', '=', '\\ge')]
    return dict(en='Compare \\(%s\\) and \\(%s\\).' % (fx_, fy_), vi='So sánh \\(%s\\) và \\(%s\\).' % (fx_, fy_), opts=opts, ans=0,
                ee='Write with a common denominator: \\(\\dfrac{%d}{%d}\\) and \\(\\dfrac{%d}{%d}\\).' % (a * d, b * d, c * b, b * d),
                ev='Quy đồng mẫu: \\(\\dfrac{%d}{%d}\\) và \\(\\dfrac{%d}{%d}\\).' % (a * d, b * d, c * b, b * d))

def b5_tf_rule(r, lv):
    op = r.choice(['<', '>']); k = nz(r, -6, 6); m = r.randint(-9, 9)
    claim = r.choice([op, FLIP[op]]); truth = (claim == op) == (k > 0)
    e = '%s%s %s %s%s' % (lin((k, 'a')), mono(m, '', False) if m else '', REL[claim], lin((k, 'b')), mono(m, '', False) if m else '')
    return dict(en='If \\(a%sb\\) then \\(%s\\).' % (REL[op], e), vi='Nếu \\(a%sb\\) thì \\(%s\\).' % (REL[op], e), ans=truth,
                ee='Multiplying by \\(%d\\) %s the sign.' % (k, 'keeps' if k > 0 else 'reverses'), ev='Nhân với \\(%d\\) thì %s chiều bất đẳng thức.' % (k, 'giữ nguyên' if k > 0 else 'đổi'))

def b5_tf_square(r, lv):
    k = r.randint(1, 9); strict = r.random() < 0.5
    e = 'x^2+%d%s %dx' % (k * k, '\\gt' if strict else '\\ge', 2 * k)
    return dict(en='\\(%s\\) for every real number \\(x\\).' % e, vi='\\(%s\\) với mọi số thực \\(x\\).' % e, ans=not strict,
                ee='\\(x^2+%d-%dx=(x-%d)^2\\ge0\\); equality when \\(x=%d\\).' % (k * k, 2 * k, k, k), ev='\\(x^2+%d-%dx=(x-%d)^2\\ge0\\); dấu bằng xảy ra khi \\(x=%d\\).' % (k * k, 2 * k, k, k))

def b5_short_min(r, lv):
    a, p, q = r.randint(-5, 8), r.randint(2, 6), r.randint(-9, 9)
    return dict(en='Given \\(x\\ge %d\\). What is the smallest possible value of \\(%s\\)?' % (a, lin((p, 'x'), (q, ''))), vi='Cho \\(x\\ge %d\\). Giá trị nhỏ nhất có thể của \\(%s\\) là bao nhiêu?' % (a, lin((p, 'x'), (q, ''))),
                key=str(p * a + q), ee='\\(x\\ge %d\\Rightarrow %dx\\ge %d\\Rightarrow %s\\ge %d\\), reached at \\(x=%d\\).' % (a, p, p * a, lin((p, 'x'), (q, '')), p * a + q, a),
                ev='\\(x\\ge %d\\Rightarrow %dx\\ge %d\\Rightarrow %s\\ge %d\\), đạt được khi \\(x=%d\\).' % (a, p, p * a, lin((p, 'x'), (q, '')), p * a + q, a))

def b5_short_count(r, lv):
    a = r.randint(-8, 10); b = a + r.randint(3, 12); sa, sb = r.choice([('\\le ', '\\le '), ('\\lt ', '\\le '), ('\\le ', '\\lt '), ('\\lt ', '\\lt ')])
    n = len([t for t in range(a - 1, b + 2) if (t >= a if sa == '\\le ' else t > a) and (t <= b if sb == '\\le ' else t < b)])
    return dict(en='The temperature \\(T\\) (°C) of a room satisfies \\(%d%sT%s%d\\). How many whole-number values can \\(T\\) take?' % (a, sa, sb, b),
                vi='Nhiệt độ \\(T\\) (°C) của một căn phòng thỏa mãn \\(%d%sT%s%d\\). \\(T\\) có thể nhận bao nhiêu giá trị nguyên?' % (a, sa, sb, b), key=str(n),
                ee='Count the integers in the range (watch the strict signs): %d values.' % n, ev='Đếm các số nguyên thỏa mãn (chú ý dấu không bằng): %d giá trị.' % n, hint=('Enter a whole number.', 'Nhập một số nguyên.'))

def b5_d1_read(r, lv):
    n = r.randint(-9, 20); op = r.choice(['<', '>', '<=', '>='])
    T = {'<': ('\\(x\\) is less than %d', '\\(x\\) nhỏ hơn %d'), '>': ('\\(x\\) is greater than %d', '\\(x\\) lớn hơn %d'),
         '<=': ('\\(x\\) is less than or equal to %d', '\\(x\\) nhỏ hơn hoặc bằng %d'), '>=': ('\\(x\\) is greater than or equal to %d', '\\(x\\) lớn hơn hoặc bằng %d')}
    order = [op] + [o for o in ('<', '>', '<=', '>=') if o != op]
    return dict(en='How do we read \\(x%s%d\\)?' % (REL[op], n), vi='Đọc \\(x%s%d\\) như thế nào?' % (REL[op], n), opts=[tx(T[o][0] % n, T[o][1] % n) for o in order], ans=0,
                ee='\\(%s\\) means “%s”.' % (REL[op], T[op][0] % n), ev='\\(%s\\): %s.' % (REL[op], T[op][1] % n))

def b5_d1_trans(r, lv):
    op = r.choice(['<', '<=']); v = r.choice([('x', 'y', 'z'), ('a', 'b', 'c'), ('m', 'n', 'p'), ('u', 'v', 'w')]); x_, y_, z_ = v
    good = '%s%s %s' % (x_, REL[op], z_)
    return dict(en='Given \\(%s%s%s\\) and \\(%s%s%s\\). Which conclusion follows?' % (x_, REL[op], y_, y_, REL[op], z_),
                vi='Cho \\(%s%s%s\\) và \\(%s%s%s\\). Kết luận nào đúng?' % (x_, REL[op], y_, y_, REL[op], z_),
                opts=[good, '%s%s %s' % (x_, REL[FLIP[op]], z_), '%s%s %s' % (z_, REL[op], x_), '%s=%s' % (x_, z_)], ans=0, ee='Transitive property.', ev='Tính chất bắc cầu.')

def b5_d1_side(r, lv):
    p, q, m = nz(r, -9, 9), r.randint(1, 9), r.randint(-9, 9); side = r.choice(['left', 'right'])
    L, R_ = lin((p, 'x'), (q, '')), lin((m, ''), (2, 'x'))
    good = L if side == 'left' else R_
    return dict(en='In the inequality \\(%s\\lt %s\\), what is the %s-hand side?' % (L, R_, side), vi='Trong bất đẳng thức \\(%s\\lt %s\\), vế %s là gì?' % (L, R_, 'trái' if side == 'left' else 'phải'),
                opts=[good, R_ if side == 'left' else L, '%s\\lt %s' % (L, R_), '\\lt'], ans=0, ee='LHS is before the sign, RHS is after it.', ev='Vế trái đứng trước dấu, vế phải đứng sau dấu.')

def b5_d2_add(r, lv):
    op = r.choice(['<', '>', '<=', '>=']); c = nz(r, -12, 12)
    return dict(en='Given \\(a%sb\\). Fill in: \\(a%s\\ \\square\\ b%s\\).' % (REL[op], mono(c, '', False), mono(c, '', False)), vi='Cho \\(a%sb\\). Điền dấu thích hợp: \\(a%s\\ \\square\\ b%s\\).' % (REL[op], mono(c, '', False), mono(c, '', False)),
                opts=[REL[op]] + [REL[o] for o in ('<', '>', '<=', '>=') if o != op][:3], ans=0, ee='Adding the same number to both sides keeps the sign.', ev='Cộng cùng một số vào hai vế thì giữ nguyên chiều.')

def b5_d2_mul(r, lv):
    op = r.choice(['<', '>', '<=', '>=']); k = nz(r, -9, 9); assert abs(k) > 1
    good = REL[op] if k > 0 else REL[FLIP[op]]
    return dict(en='Given \\(x%sy\\). Fill in: \\(%dx\\ \\square\\ %dy\\).' % (REL[op], k, k), vi='Cho \\(x%sy\\). Điền dấu thích hợp: \\(%dx\\ \\square\\ %dy\\).' % (REL[op], k, k),
                opts=[good] + [REL[o] for o in ('<', '>', '<=', '>=') if REL[o] != good][:3], ans=0,
                ee='Multiplying by \\(%d\\) %s the sign.' % (k, 'keeps' if k > 0 else 'reverses'), ev='Nhân với \\(%d\\) thì %s chiều.' % (k, 'giữ nguyên' if k > 0 else 'đổi'))

def b5_d2_diff(r, lv):
    p, q = r.sample(range(-9, 10), 2); assert p != q
    s = '\\lt ' if p < q else '\\gt '
    A, B = 'a%s' % mono(p, '', False) if p else 'a', 'a%s' % mono(q, '', False) if q else 'a'
    return dict(en='Compare \\(%s\\) and \\(%s\\) for any real number \\(a\\).' % (A, B), vi='So sánh \\(%s\\) và \\(%s\\) với mọi số thực \\(a\\).' % (A, B),
                opts=['%s%s%s' % (A, s, B), '%s%s%s' % (A, '\\gt ' if s == '\\lt ' else '\\lt ', B), '%s=%s' % (A, B), tx('it depends on \\(a\\)', 'phụ thuộc vào \\(a\\)')], ans=0,
                ee='Their difference is \\(%d\\), whatever \\(a\\) is.' % (p - q), ev='Hiệu của chúng bằng \\(%d\\) với mọi \\(a\\).' % (p - q))

def b5_d3_infer(r, lv):
    op = r.choice(['<', '>']); p = nz(r, -6, 6); q = nz(r, -9, 9); assert abs(p) > 1
    s = op if p > 0 else FLIP[op]
    L, R_ = lin((p, 'a'), (q, '')), lin((p, 'b'), (q, ''))
    opts = ['%s%s%s' % (L, REL[s], R_), '%s%s%s' % (L, REL[FLIP[s]], R_), '%s%s%s' % (lin((p, 'a'), (-q, '')), REL[s], R_), '%s%s%s' % (lin((-p, 'a'), (q, '')), REL[s], lin((-p, 'b'), (q, '')))]
    return dict(en='Given \\(a%sb\\). Which inequality about \\(%s\\) can we prove?' % (REL[op], L), vi='Cho \\(a%sb\\). Bất đẳng thức nào về \\(%s\\) chứng minh được?' % (REL[op], L), opts=opts, ans=0,
                ee='Multiply by \\(%d\\) (%s), then add \\(%d\\).' % (p, 'keep the sign' if p > 0 else 'reverse the sign', q), ev='Nhân với \\(%d\\) (%s), rồi cộng \\(%d\\).' % (p, 'giữ chiều' if p > 0 else 'đổi chiều', q))

def b5_d3_frac(r, lv):
    n = r.randint(150, 2100); m = r.randint(50, 900)
    a, b = 2 * n + r.randint(1, 9), n; c, d = 2 * m - r.randint(1, 9), m       # a/b > 2 > c/d
    assert F(a, b) > 2 > F(c, d)
    return dict(en='Compare \\(\\dfrac{%d}{%d}\\) and \\(\\dfrac{%d}{%d}\\) without a calculator.' % (a, b, c, d), vi='So sánh \\(\\dfrac{%d}{%d}\\) và \\(\\dfrac{%d}{%d}\\) mà không dùng máy tính.' % (a, b, c, d),
                opts=['\\dfrac{%d}{%d}\\gt\\dfrac{%d}{%d}' % (a, b, c, d), '\\dfrac{%d}{%d}\\lt\\dfrac{%d}{%d}' % (a, b, c, d), '\\dfrac{%d}{%d}=\\dfrac{%d}{%d}' % (a, b, c, d), '\\dfrac{%d}{%d}\\le\\dfrac{%d}{%d}' % (a, b, c, d)], ans=0,
                ee='\\(\\dfrac{%d}{%d}\\gt\\dfrac{%d}{%d}=2\\) and \\(\\dfrac{%d}{%d}\\lt\\dfrac{%d}{%d}=2\\); use 2 as a middle number.' % (a, b, 2 * b, b, c, d, 2 * d, d),
                ev='\\(\\dfrac{%d}{%d}\\gt\\dfrac{%d}{%d}=2\\) và \\(\\dfrac{%d}{%d}\\lt\\dfrac{%d}{%d}=2\\); dùng số 2 làm trung gian (tính chất bắc cầu).' % (a, b, 2 * b, b, c, d, 2 * d, d))

def b5_d3_double(r, lv):
    lo = r.randint(10, 60); hi = lo + r.randint(20, 120)
    c = r.choice([('The height \\(h\\) (m) of a drone must be greater than %d m and less than %d m.', 'Độ cao \\(h\\) (m) của flycam phải lớn hơn %d m và nhỏ hơn %d m.', 'h'),
                  ('The water temperature \\(t\\) (°C) must be at least %d °C and at most %d °C.', 'Nhiệt độ nước \\(t\\) (°C) phải ít nhất %d °C và nhiều nhất %d °C.', 't')])
    v = c[2]; strict = v == 'h'
    S1, S2 = ('\\lt ', '\\le ') if strict else ('\\le ', '\\lt ')
    good = '%d%s%s%s%d' % (lo, S1, v, S1, hi)
    bads = ['%d%s%s%s%d' % (lo, S2, v, S2, hi), '%s\\lt %d' % (v, lo), '%d%s%s%s%d' % (hi, S1, v, S1, lo)]
    return dict(en=(c[0] % (lo, hi)) + ' Which is correct?', vi=(c[1] % (lo, hi)) + ' Cách viết nào đúng?', opts=[good] + bads, ans=0,
                ee='“greater/less than” → strict signs; “at least/at most” → \\(\\le\\).', ev='“lớn hơn/nhỏ hơn” → dấu \\(\\lt\\); “ít nhất/nhiều nhất” → dấu \\(\\le\\).')

def b5_d4_equal(r, lv):
    k = nz(r, -9, 9)
    return dict(en='We have \\(a^2+%d\\ge %da\\) for every real \\(a\\). For which value of \\(a\\) does equality hold?' % (k * k, 2 * k), vi='Ta có \\(a^2+%d\\ge %da\\) với mọi số thực \\(a\\). Dấu bằng xảy ra khi \\(a\\) bằng bao nhiêu?' % (k * k, 2 * k),
                opts=pick_opts(r, 'a=%d' % k, ['a=%d' % o for o in (-k, k * k, 2 * k, 0) if o != k]), ans=0,
                ee='\\(a^2+%d-%da=(a%s)^2\\ge0\\); it is 0 when \\(a=%d\\).' % (k * k, 2 * k, mono(-k, '', False), k), ev='\\(a^2+%d-%da=(a%s)^2\\ge0\\); bằng 0 khi \\(a=%d\\).' % (k * k, 2 * k, mono(-k, '', False), k))

def b5_d4_notalways(r, lv):
    c, k = nz(r, -9, 9), r.randint(2, 7)
    good = 'a^2\\ge b^2'
    bads = ['a%s\\ge b%s' % (mono(c, '', False), mono(c, '', False)), '%da\\ge %db' % (k, k), '-%da\\le -%db' % (k, k)]
    q = r.choice([('Given \\(a\\ge b\\). Which inequality is NOT always true?', 'Cho \\(a\\ge b\\). Bất đẳng thức nào KHÔNG phải lúc nào cũng đúng?'),
                  ('Let \\(a\\ge b\\). Which statement can be false?', 'Cho \\(a\\ge b\\). Khẳng định nào có thể sai?'),
                  ('Suppose \\(a\\ge b\\). Which of these does not always follow?', 'Giả sử \\(a\\ge b\\). Điều nào sau đây không luôn suy ra được?')])
    return dict(en=q[0] + ' (\\(k=%d\\), \\(c=%d\\))' % (k, c), vi=q[1] + ' (\\(k=%d\\), \\(c=%d\\))' % (k, c), opts=[good] + bads, ans=0,
                ee='Counterexample: \\(a=1,\\ b=-2\\): \\(a\\ge b\\) but \\(1\\lt 4\\).', ev='Phản ví dụ: \\(a=1,\\ b=-2\\): \\(a\\ge b\\) nhưng \\(1\\lt 4\\).')

def b5_d4_consec(r, lv):
    n = r.randint(5, 99)
    return dict(en='For the three consecutive numbers %d, %d, %d, compute \\(%d^2-%d\\cdot%d\\).' % (n - 1, n, n + 1, n, n - 1, n + 1),
                vi='Với ba số tự nhiên liên tiếp %d, %d, %d, hãy tính \\(%d^2-%d\\cdot%d\\).' % (n - 1, n, n + 1, n, n - 1, n + 1),
                opts=['1', '0', '-1', str(2 * n)], ans=0, ee='\\(n^2-(n-1)(n+1)=n^2-(n^2-1)=1\\gt0\\): the middle number squared is always larger.', ev='\\(n^2-(n-1)(n+1)=n^2-(n^2-1)=1\\gt0\\): bình phương số ở giữa luôn lớn hơn tích hai số kia.')

L5_GROUPS = [[('mcq', b5_translate), ('mcq', b5_property), ('mcq', b5_compare)], [('tf', b5_tf_rule), ('tf', b5_tf_square)], [('short', b5_short_min), ('short', b5_short_count)],
             [('mcq', b5_d1_read), ('mcq', b5_d1_trans), ('mcq', b5_d1_side)], [('mcq', b5_d2_add), ('mcq', b5_d2_mul), ('mcq', b5_d2_diff)],
             [('mcq', b5_d3_infer), ('mcq', b5_d3_frac), ('mcq', b5_d3_double)], [('mcq', b5_d4_equal), ('mcq', b5_d4_notalways), ('mcq', b5_d4_consec)]]

# =====================================================================================================
# BÀI 6. Bất phương trình bậc nhất một ẩn
# =====================================================================================================
def solve_lin_ineq(a, b, op):
    """ax + b op 0  ->  (op', r): x op' r."""
    rt = F(-b, a); o = op if a > 0 else FLIP[op]
    return o, rt

def ineq_tex(o, r_, v='x'):
    return '%s%s%s' % (v, REL[o], fr(r_))

def b6_which(r, lv):
    a, b = nz(r, -9, 9), nz(r, -9, 9); op = r.choice(list(REL))
    good = '%s%s0' % (lin((a, 'x'), (b, '')), REL[op])
    bads = ['0x%s%s0' % (mono(b, '', False), REL[op]), '%s%s%s0' % (lin((1, 'x^2')), mono(-abs(b), '', False), REL[op]), '\\dfrac{%d}{x}%s%s0' % (abs(a), mono(b, '', False), REL[op]), 'xy%s%s0' % (mono(b, '', False), REL[op])]
    r.shuffle(bads)
    q = r.choice([('Which is a linear inequality in one variable?', 'Bất phương trình nào là bất phương trình bậc nhất một ẩn?'), ('Choose the linear inequality in one variable.', 'Chọn bất phương trình bậc nhất một ẩn.'),
                  ('Only one of these is a linear inequality in one variable. Which one?', 'Chỉ có một bất phương trình bậc nhất một ẩn. Đó là bất phương trình nào?'), ('Identify the linear inequality in \\(x\\).', 'Chỉ ra bất phương trình bậc nhất ẩn \\(x\\).')])
    return dict(en=q[0], vi=q[1], opts=[good] + bads[:3], ans=0, ee='It has the form \\(ax+b\\lt 0\\) (or \\(\\gt, \\le, \\ge\\)) with \\(a\\ne0\\).', ev='Bất phương trình có dạng \\(ax+b\\lt 0\\) (hoặc \\(\\gt, \\le, \\ge\\)) với \\(a\\ne0\\).')

def _ineq(r, neg=None):
    while True:
        a = nz(r, -9, 9); 
        if neg is not None and (a < 0) != neg: continue
        x0 = r.randint(-8, 8); den = r.choice([1, 1, 1, abs(a)]); b = -a * x0 if den == 1 else -(a * x0 + r.choice([1, -1])) 
        if a not in (1, -1): break
    return a, b, r.choice(list(REL))

def b6_solve(r, lv):
    a, b, op = _ineq(r); c = r.randint(-9, 9); o, rt = solve_lin_ineq(a, b - c, op)
    e = '%s%s%d' % (lin((a, 'x'), (b, '')), REL[op], c)
    good = ineq_tex(o, rt); bads = [ineq_tex(FLIP[o], rt), ineq_tex(o, -rt) if rt else ineq_tex(o, F(1)), ineq_tex(FLIP[o], -rt) if rt else ineq_tex(FLIP[o], F(-1))]
    return dict(en='Solve the inequality \\(%s\\).' % e, vi='Giải bất phương trình \\(%s\\).' % e, opts=pick_opts(r, good, bads, fill=lambda t: ineq_tex(o, rt + t)), ans=0,
                ee='\\(%s%s%s\\)%s, so \\(%s\\).' % (lin((a, 'x')), REL[op], fr(c - b), ' (divide by \\(%d\\) and reverse the sign)' % a if a < 0 else '', good),
                ev='\\(%s%s%s\\)%s, suy ra \\(%s\\).' % (lin((a, 'x')), REL[op], fr(c - b), ' (chia cho \\(%d\\) và đổi chiều)' % a if a < 0 else '', good))

def b6_check(r, lv):
    a, b, op = _ineq(r); c = r.randint(-9, 9)
    sat = [v for v in range(-12, 13) if holds(a * v + b, op, c)]; uns = [v for v in range(-12, 13) if not holds(a * v + b, op, c)]
    assert sat and len(uns) >= 3
    g = r.choice(sat); bads = r.sample(uns, 3); e = '%s%s%d' % (lin((a, 'x'), (b, '')), REL[op], c)
    return dict(en='Which value of \\(x\\) is a solution of \\(%s\\)?' % e, vi='Giá trị nào của \\(x\\) là nghiệm của bất phương trình \\(%s\\)?' % e,
                opts=['x=%d' % g] + ['x=%d' % v for v in bads], ans=0, ee='Substitute: \\(%s=%d%s%d\\) is true.' % (lin((a, '\\cdot(%d)' % g), (b, '')).replace('\\cdot', '\\cdot') if False else '%d\\cdot(%d)%s' % (a, g, mono(b, '', False)), a * g + b, REL[op], c),
                ev='Thay vào: \\(%d\\cdot(%d)%s=%d%s%d\\) đúng.' % (a, g, mono(b, '', False), a * g + b, REL[op], c))

def b6_tf_sol(r, lv):
    a, b, op = _ineq(r); c = r.randint(-9, 9); v = r.randint(-8, 8); truth = holds(a * v + b, op, c)
    e = '%s%s%d' % (lin((a, 'x'), (b, '')), REL[op], c)
    return dict(en='\\(x=%d\\) is a solution of the inequality \\(%s\\).' % (v, e), vi='\\(x=%d\\) là một nghiệm của bất phương trình \\(%s\\).' % (v, e), ans=truth,
                ee='\\(%d\\cdot(%d)%s=%d\\); the statement \\(%d%s%d\\) is %s.' % (a, v, mono(b, '', False), a * v + b, a * v + b, REL[op], c, 'true' if truth else 'false'),
                ev='\\(%d\\cdot(%d)%s=%d\\); mệnh đề \\(%d%s%d\\) %s.' % (a, v, mono(b, '', False), a * v + b, a * v + b, REL[op], c, 'đúng' if truth else 'sai'))

def b6_tf_neg(r, lv):
    k, m = r.randint(2, 9), r.randint(-20, 20); op = r.choice(['>=', '<=', '>', '<']); truth = r.random() < 0.5
    o, rt = solve_lin_ineq(-k, m, op); claim = o if truth else FLIP[o]
    e = '%s%s0' % (lin((-k, 'x'), (m, '')), REL[op])
    return dict(en='The solution of \\(%s\\) is \\(%s\\).' % (e, ineq_tex(claim, rt)), vi='Nghiệm của bất phương trình \\(%s\\) là \\(%s\\).' % (e, ineq_tex(claim, rt)), ans=truth,
                ee='Divide by \\(%d\\lt 0\\) and reverse the sign: \\(%s\\).' % (-k, ineq_tex(o, rt)), ev='Chia hai vế cho \\(%d\\lt 0\\) và đổi chiều: \\(%s\\).' % (-k, ineq_tex(o, rt)))

def b6_short_max(r, lv):
    while True:
        a, c = r.randint(2, 9), r.randint(-6, 6); assert a != c
        if a == c: continue
        b, d = r.randint(-15, 15), r.randint(-15, 15); op = r.choice(['<=', '<'])
        o, rt = solve_lin_ineq(a - c, b - d, op)
        if o in ('<=', '<'): break
    n = max(t for t in range(-60, 60) if holds(t, o, rt))
    e = '%s%s%s' % (lin((a, 'x'), (b, '')), REL[op], lin((c, 'x'), (d, '')))
    return dict(en='Find the largest integer \\(x\\) that satisfies \\(%s\\).' % e, vi='Tìm số nguyên \\(x\\) lớn nhất thỏa mãn \\(%s\\).' % e, key=str(n),
                ee='The solution is \\(%s\\); the largest integer is %d.' % (ineq_tex(o, rt), n), ev='Nghiệm của bất phương trình là \\(%s\\); số nguyên lớn nhất là %d.' % (ineq_tex(o, rt), n))

def b6_short_shop(r, lv):
    M = r.choice([100, 120, 150, 200]); p = r.choice([25, 30, 35, 40, 45]); n = r.randint(3, 6); x = (M - p) // n
    nm = r.choice(NAMES)
    return dict(en='%s has %d thousand dong. %s buys a book for %d thousand dong and %d notebooks of the same price \\(x\\) (thousand dong, a whole number). What is the highest possible price of one notebook?' % (nm[0], M, 'She' if nm[0] in ('Lan', 'Hoa', 'Mai') else 'He', p, n),
                vi='Bạn %s có %d nghìn đồng. Bạn mua một quyển sách giá %d nghìn đồng và %d quyển vở cùng giá \\(x\\) (nghìn đồng, là số nguyên). Giá mỗi quyển vở cao nhất có thể là bao nhiêu?' % (nm[1], M, p, n),
                key=str(x), ee='\\(%dx+%d\\le %d\\Rightarrow x\\le %s\\), so the largest whole number is %d.' % (n, p, M, fr(F(M - p, n)), x), ev='\\(%dx+%d\\le %d\\Rightarrow x\\le %s\\), nên số nguyên lớn nhất là %d.' % (n, p, M, fr(F(M - p, n)), x), hint=('Enter a whole number.', 'Nhập một số nguyên.'))

def b6_d1_rule(r, lv):
    k = r.randint(2, 15)
    o = [tx('reverse the inequality sign', 'đổi chiều bất phương trình'), tx('keep the inequality sign', 'giữ nguyên chiều bất phương trình'), tx('change it into an equation', 'đổi thành phương trình'), tx('add \\(%d\\) to the right-hand side only' % k, 'chỉ cộng \\(%d\\) vào vế phải' % k)]
    return dict(en='When we divide both sides of an inequality by \\(-%d\\), we must…' % k, vi='Khi chia hai vế của một bất phương trình cho \\(-%d\\), ta phải…' % k, opts=o, ans=0,
                ee='Multiplying or dividing by a negative number reverses the sign.', ev='Nhân hoặc chia hai vế cho số âm thì phải đổi chiều.')

def b6_d1_ab(r, lv):
    a, b = nz(r, -9, 9), nz(r, -9, 9); op = r.choice(list(REL)); assert a != b and a != -b
    e = '%s%s0' % (lin((a, 'x'), (b, '')), REL[op])
    return dict(en='In the inequality \\(%s\\), what are \\(a\\) and \\(b\\)?' % e, vi='Trong bất phương trình \\(%s\\), hệ số \\(a\\) và \\(b\\) là bao nhiêu?' % e,
                opts=['a=%d,\\ b=%d' % (a, b), 'a=%d,\\ b=%d' % (b, a), 'a=%d,\\ b=%d' % (a, -b), 'a=%d,\\ b=%d' % (-a, b)], ans=0, ee='Compare with \\(ax+b\\).', ev='So sánh với dạng \\(ax+b\\).')

def b6_d1_check(r, lv):
    q = b6_check(r, lv); q['en'] = q['en'].replace('Which value of \\(x\\) is a solution of', 'Which number satisfies'); q['vi'] = q['vi'].replace('Giá trị nào của \\(x\\) là nghiệm của bất phương trình', 'Số nào thỏa mãn bất phương trình')
    return q

def b6_d2_neg(r, lv):
    a, b, op = _ineq(r, neg=True); o, rt = solve_lin_ineq(a, b, op)
    e = '%s%s0' % (lin((a, 'x'), (b, '')), REL[op])
    return dict(en='Solve \\(%s\\).' % e, vi='Giải bất phương trình \\(%s\\).' % e, opts=pick_opts(r, ineq_tex(o, rt), [ineq_tex(FLIP[o], rt), ineq_tex(o, -rt) if rt else ineq_tex(o, F(2)), ineq_tex(FLIP[o], -rt) if rt else ineq_tex(FLIP[o], F(-2))]), ans=0,
                ee='\\(%s%s%s\\); divide by \\(%d\\lt0\\) and reverse: \\(%s\\).' % (lin((a, 'x')), REL[op], fr(-b), a, ineq_tex(o, rt)), ev='\\(%s%s%s\\); chia cho \\(%d\\lt0\\) và đổi chiều: \\(%s\\).' % (lin((a, 'x')), REL[op], fr(-b), a, ineq_tex(o, rt)))

def b6_d2_dot(r, lv):
    v = r.randint(-9, 9); op = r.choice(list(REL)); closed = op in ('<=', '>=')
    o = [tx('a filled (solid) dot', 'chấm tròn đặc (lấy điểm đó)'), tx('an open (hollow) dot', 'chấm tròn rỗng (bỏ điểm đó)'), tx('a dashed line', 'một đường nét đứt'), tx('nothing at that point', 'không đánh dấu gì')]
    return dict(en='On a number line, the solutions \\(x%s%d\\) are shown. What do we draw at the point \\(%d\\)?' % (REL[op], v, v), vi='Biểu diễn nghiệm \\(x%s%d\\) trên trục số. Tại điểm \\(%d\\) ta vẽ gì?' % (REL[op], v, v),
                opts=o, ans=0 if closed else 1, ee='%s' % ('The point belongs to the solutions (\\(\\le,\\ge\\)): filled dot.' if closed else 'The point is not a solution (\\(\\lt,\\gt\\)): open dot.'),
                ev='%s' % ('Điểm đó là nghiệm (dấu \\(\\le,\\ge\\)): chấm đặc.' if closed else 'Điểm đó không là nghiệm (dấu \\(\\lt,\\gt\\)): chấm rỗng.'))

def b6_d2_frac(r, lv):
    p = r.choice([2, 3, 4, 5]); q, c = r.randint(-9, 9), r.randint(-9, 9); op = r.choice(list(REL)); rt = (c - q) * p
    e = '\\dfrac{x}{%d}%s%s%d' % (p, mono(q, '', False) if q else '', REL[op], c)
    return dict(en='Solve \\(%s\\).' % e, vi='Giải bất phương trình \\(%s\\).' % e, opts=pick_opts(r, ineq_tex(op, F(rt)), [ineq_tex(op, F(c - q)), ineq_tex(FLIP[op], F(rt)), ineq_tex(op, F(c - q, p))], fill=lambda t: ineq_tex(op, F(rt + t))), ans=0,
                ee='\\(\\dfrac{x}{%d}%s%d\\); multiply by \\(%d\\gt0\\): \\(%s\\).' % (p, REL[op], c - q, p, ineq_tex(op, F(rt))), ev='\\(\\dfrac{x}{%d}%s%d\\); nhân hai vế với \\(%d\\gt0\\): \\(%s\\).' % (p, REL[op], c - q, p, ineq_tex(op, F(rt))))

def b6_d3_both(r, lv):
    while True:
        a, c = nz(r, -8, 8), nz(r, -8, 8)
        if a != c and abs(a - c) > 1: break
    b, d = r.randint(-15, 15), r.randint(-15, 15); op = r.choice(list(REL)); o, rt = solve_lin_ineq(a - c, b - d, op)
    e = '%s%s%s' % (lin((a, 'x'), (b, '')), REL[op], lin((c, 'x'), (d, '')))
    return dict(en='Solve \\(%s\\).' % e, vi='Giải bất phương trình \\(%s\\).' % e, opts=pick_opts(r, ineq_tex(o, rt), [ineq_tex(FLIP[o], rt), ineq_tex(o, -rt) if rt else ineq_tex(o, F(3)), ineq_tex(o, F(d - b, a + c)) if a + c else ineq_tex(o, rt + 1)], fill=lambda t: ineq_tex(o, rt + t)), ans=0,
                ee='Move terms: \\(%s%s%d\\Rightarrow %s\\).' % (lin((a - c, 'x')), REL[op], d - b, ineq_tex(o, rt)), ev='Chuyển vế: \\(%s%s%d\\Rightarrow %s\\).' % (lin((a - c, 'x')), REL[op], d - b, ineq_tex(o, rt)))

def b6_d3_expand(r, lv):
    a, b = nz(r, -6, 6), nz(r, -6, 6); c, d = r.randint(-8, 8), r.randint(-12, 12); op = r.choice(list(REL))
    # (x+a)(2x+b) = 2x^2 + (b+2a)x + ab ; vế phải 2x^2 + c x + d  ->  (b+2a-c)x + ab - d op 0
    k = b + 2 * a - c; assert k != 0 and abs(k) != 1
    o, rt = solve_lin_ineq(k, a * b - d, op)
    e = '(x%s)(2x%s)%s2x^2%s%s' % (mono(a, '', False), mono(b, '', False), REL[op], mono(c, 'x', False) if c else '', mono(d, '', False) if d else '')
    return dict(en='Solve \\(%s\\).' % e, vi='Giải bất phương trình \\(%s\\).' % e, opts=pick_opts(r, ineq_tex(o, rt), [ineq_tex(FLIP[o], rt), ineq_tex(o, -rt) if rt else ineq_tex(o, F(1)), ineq_tex(o, rt + 1)]), ans=0,
                ee='Expand: \\(2x^2%s%s\\); the \\(2x^2\\) terms cancel: \\(%s%s%d\\Rightarrow %s\\).' % (mono(b + 2 * a, 'x', False), mono(a * b, '', False), lin((k, 'x')), REL[op], d - a * b, ineq_tex(o, rt)),
                ev='Khai triển: \\(2x^2%s%s\\); hai hạng tử \\(2x^2\\) triệt tiêu: \\(%s%s%d\\Rightarrow %s\\).' % (mono(b + 2 * a, 'x', False), mono(a * b, '', False), lin((k, 'x')), REL[op], d - a * b, ineq_tex(o, rt)))

def b6_d3_min(r, lv):
    while True:
        a, b, op = _ineq(r); c = r.randint(-9, 9); o, rt = solve_lin_ineq(a, b - c, op)
        if o in ('>', '>='): break
    n = min(t for t in range(-60, 60) if holds(t, o, rt)); e = '%s%s%d' % (lin((a, 'x'), (b, '')), REL[op], c)
    return dict(en='What is the smallest integer that satisfies \\(%s\\)?' % e, vi='Số nguyên nhỏ nhất thỏa mãn \\(%s\\) là số nào?' % e, opts=pick_opts(r, str(n), [str(n - 1), str(n + 1), str(-n) if n else '2']), ans=0,
                ee='Solution: \\(%s\\); the smallest integer is %d.' % (ineq_tex(o, rt), n), ev='Nghiệm: \\(%s\\); số nguyên nhỏ nhất là %d.' % (ineq_tex(o, rt), n))

def b6_d4_shop(r, lv):
    M = r.choice([200, 250, 300, 500]); p = r.choice([15, 18, 20, 25]); f = r.choice([20, 30, 40, 50]); x = (M - f) // p
    return dict(en='A class has %d thousand dong. They pay %d thousand dong for transport and buy drinks at %d thousand dong each. What is the greatest number of drinks they can buy?' % (M, f, p),
                vi='Một lớp có %d nghìn đồng. Lớp trả %d nghìn đồng tiền xe và mua nước uống, mỗi chai %d nghìn đồng. Lớp mua được nhiều nhất bao nhiêu chai nước?' % (M, f, p),
                opts=pick_opts(r, str(x), [str(x + 1), str(M // p), str(x - 1)]), ans=0,
                ee='\\(%dx+%d\\le %d\\Rightarrow x\\le %s\\); \\(x\\) is a whole number, so \\(x=%d\\).' % (p, f, M, fr(F(M - f, p)), x), ev='\\(%dx+%d\\le %d\\Rightarrow x\\le %s\\); \\(x\\) là số tự nhiên nên \\(x=%d\\).' % (p, f, M, fr(F(M - f, p)), x))

def b6_d4_triangle(r, lv):
    while True:
        a, b, c, d = r.randint(2, 5), r.randint(-3, 6), r.randint(1, 3), r.randint(2, 12)
        if a > c: break
    rt = F(d - b, a - c)
    return dict(en='In triangle \\(DEF\\), \\(DF=%s\\) and \\(DE=%s\\) (cm), and \\(DF\\) is longer than \\(DE\\). Which condition on \\(x\\) is correct?' % (lin((a, 'x'), (b, '')), lin((c, 'x'), (d, ''))),
                vi='Tam giác \\(DEF\\) có \\(DF=%s\\) và \\(DE=%s\\) (cm), trong đó \\(DF\\) dài hơn \\(DE\\). Điều kiện nào của \\(x\\) đúng?' % (lin((a, 'x'), (b, '')), lin((c, 'x'), (d, ''))),
                opts=pick_opts(r, ineq_tex('>', rt), [ineq_tex('<', rt), ineq_tex('>', F(d + b, a + c)), ineq_tex('>=', rt)]), ans=0,
                ee='\\(%s\\gt %s\\Rightarrow %s\\gt %d\\Rightarrow %s\\).' % (lin((a, 'x'), (b, '')), lin((c, 'x'), (d, '')), lin((a - c, 'x')), d - b, ineq_tex('>', rt)),
                ev='\\(%s\\gt %s\\Rightarrow %s\\gt %d\\Rightarrow %s\\).' % (lin((a, 'x'), (b, '')), lin((c, 'x'), (d, '')), lin((a - c, 'x')), d - b, ineq_tex('>', rt)))

def b6_d4_plan(r, lv):
    while True:
        fa, pa = r.choice([50, 60, 70, 80, 100]), r.choice([300, 400, 500, 600])   # gói A: phí cố định (nghìn đồng) + giá mỗi phút (đồng)
        fb, pb = r.choice([0, 10, 20]), r.choice([800, 900, 1000, 1200])
        if pb > pa and fa > fb: break
    # chi phí (đồng): A = 1000fa + pa·t ; B = 1000fb + pb·t ; A rẻ hơn B  <=>  t > 1000(fa-fb)/(pb-pa)
    rt = F(1000 * (fa - fb), pb - pa); n = int(rt) + 1
    assert 1000 * fa + pa * n < 1000 * fb + pb * n and not (1000 * fa + pa * (n - 1) < 1000 * fb + pb * (n - 1))
    return dict(en='Phone plan A costs %d thousand dong per month plus %d dong per minute. Plan B costs %d thousand dong per month plus %d dong per minute. From how many whole minutes per month is plan A cheaper?' % (fa, pa, fb, pb),
                vi='Gói cước A: %d nghìn đồng mỗi tháng và %d đồng mỗi phút gọi. Gói B: %d nghìn đồng mỗi tháng và %d đồng mỗi phút gọi. Gọi từ bao nhiêu phút (số nguyên) trở lên trong tháng thì gói A rẻ hơn?' % (fa, pa, fb, pb),
                opts=pick_opts(r, str(n), [str(n - 1), str(n + 1), str(int(F(1000 * (fa + fb), pb - pa)))], fill=lambda t: str(n + 2 * t + 1)), ans=0,
                ee='\\(%d000+%dt\\lt %d+%dt\\Rightarrow t\\gt %s\\), so from %d minutes.' % (fa, pa, 1000 * fb, pb, fr(rt), n),
                ev='\\(%d000+%dt\\lt %d+%dt\\Rightarrow t\\gt %s\\), nên từ %d phút trở lên.' % (fa, pa, 1000 * fb, pb, fr(rt), n))

L6_GROUPS = [[('mcq', b6_which), ('mcq', b6_solve), ('mcq', b6_check)], [('tf', b6_tf_sol), ('tf', b6_tf_neg)], [('short', b6_short_max), ('short', b6_short_shop)],
             [('mcq', b6_d1_rule), ('mcq', b6_d1_ab), ('mcq', b6_d1_check)], [('mcq', b6_d2_neg), ('mcq', b6_d2_dot), ('mcq', b6_d2_frac)],
             [('mcq', b6_d3_both), ('mcq', b6_d3_expand), ('mcq', b6_d3_min)], [('mcq', b6_d4_shop), ('mcq', b6_d4_triangle), ('mcq', b6_d4_plan)]]

def ray_svg(a, op, lo=None, hi=None):
    """Trục số biểu diễn nghiệm x op a: tô phần nghiệm, chấm đặc (lấy a) / chấm rỗng (bỏ a); nhãn số đặt dưới, không đè lên đường tô."""
    from mb_pgf import texsvg, col
    a = F(a); lo = math.floor(a) - 4 if lo is None else lo; hi = math.floor(a) + 4 if hi is None else hi
    right = op in ('>', '>='); closed = op in ('<=', '>=')
    av = float(a); o = ['\\begin{tikzpicture}[x=0.9cm, y=1cm]',
         '\\draw[ink, line width=0.8pt, -{Stealth[length=2.6mm]}] (%s,0) -- (%s,0) node[right] {$x$};' % (lo - 0.4, hi + 0.5),
         '\\draw[%s, line width=5pt, opacity=0.75] (%s,0) -- (%s,0);' % ('mint', av, hi + 0.35 if right else lo - 0.35)]
    for v in range(lo, hi + 1):
        if abs(v - av) < 0.35: continue
        o.append('\\draw[ink, line width=0.7pt] (%s,0.12) -- (%s,-0.12) node[below=3pt, font=\\small] {$%s$};' % (v, v, v))
    o.append('\\node[circle, inner sep=0pt, minimum size=8pt, draw=%s, line width=1.2pt, fill=%s] at (%s,0) {};' % (col('046b4d'), col('046b4d') if closed else 'white', av))
    o.append('\\node[font=\\small, fill=white, inner sep=1pt] at (%s,-0.48) {$%s$};' % (av, fr(a)))
    o.append('\\end{tikzpicture}')
    return texsvg('\n'.join(o))

# =====================================================================================================
# BÀI 7. Căn bậc hai và căn thức bậc hai
# =====================================================================================================
def sq_frac(r):
    """Số chính phương (nguyên hoặc phân số) n và căn bậc hai số học s của nó."""
    if r.random() < 0.6:
        s = F(r.randint(2, 25)); return s * s, s
    p, q = r.randint(1, 12), r.randint(2, 15); s = F(p, q)
    assert s.denominator == q
    return s * s, s

def b7_roots(r, lv):
    n2, s = sq_frac(r)
    return dict(en='The square roots of \\(%s\\) are…' % fr(n2), vi='Các căn bậc hai của \\(%s\\) là…' % fr(n2),
                opts=['\\pm %s' % fr(s), fr(s), '-%s' % fr(s), fr(n2 / 2) if n2 / 2 != s else fr(n2 * 2)], ans=0,
                ee='Both \\(%s\\) and \\(-%s\\) squared give \\(%s\\): a positive number has two opposite square roots.' % (fr(s), fr(s), fr(n2)),
                ev='Cả \\(%s\\) và \\(-%s\\) bình phương đều bằng \\(%s\\): số dương có hai căn bậc hai là hai số đối nhau.' % (fr(s), fr(s), fr(n2)))

def b7_arith(r, lv):
    n2, s = sq_frac(r)
    return dict(en='Compute \\(\\sqrt{%s}\\).' % fr(n2), vi='Tính \\(\\sqrt{%s}\\).' % fr(n2), opts=pick_opts(r, fr(s), ['-%s' % fr(s), '\\pm %s' % fr(s), fr(n2 / 2)], fill=lambda t: fr(s + t)), ans=0,
                ee='\\(\\sqrt{%s}\\) is the non-negative number whose square is \\(%s\\): \\(%s\\).' % (fr(n2), fr(n2), fr(s)), ev='\\(\\sqrt{%s}\\) là số không âm có bình phương bằng \\(%s\\): \\(%s\\).' % (fr(n2), fr(n2), fr(s)))

def _dk(a, b):
    """√(ax+b) xác định ⇔ ax+b ≥ 0 ⇔ x ≥ -b/a (a>0) hoặc x ≤ -b/a (a<0)."""
    rt = F(-b, a); return ('>=' if a > 0 else '<='), rt

def b7_dk(r, lv):
    a, b = nz(r, -7, 7), nz(r, -12, 12); o, rt = _dk(a, b); E = lin((a, 'x'), (b, ''))
    good = ineq_tex(o, rt); bads = [ineq_tex(FLIP[o], rt), ineq_tex(o, -rt), ineq_tex({'>=': '>', '<=': '<'}[o], rt)]
    return dict(en='For which \\(x\\) is \\(\\sqrt{%s}\\) defined?' % E, vi='\\(\\sqrt{%s}\\) xác định khi nào?' % E, opts=pick_opts(r, good, bads), ans=0,
                ee='We need \\(%s\\ge0\\), i.e. \\(%s\\).' % (E, good), ev='Cần \\(%s\\ge0\\), tức là \\(%s\\).' % (E, good))

def b7_tf_abs(r, lv):
    k = r.randint(2, 15); truth = r.random() < 0.5; rhs = k if truth else -k
    return dict(en='\\(\\sqrt{(-%d)^2}=%d\\).' % (k, rhs), vi='\\(\\sqrt{(-%d)^2}=%d\\).' % (k, rhs), ans=truth,
                ee='\\(\\sqrt{A^2}=|A|\\), so \\(\\sqrt{(-%d)^2}=|-%d|=%d\\).' % (k, k, k), ev='\\(\\sqrt{A^2}=|A|\\) nên \\(\\sqrt{(-%d)^2}=|-%d|=%d\\).' % (k, k, k))

def b7_tf_def(r, lv):
    a, b = nz(r, -6, 6), r.randint(-15, 15); v = r.randint(-6, 6); val = a * v + b; E = lin((a, 'x'), (b, ''))
    return dict(en='The expression \\(\\sqrt{%s}\\) is defined at \\(x=%d\\).' % (E, v), vi='Biểu thức \\(\\sqrt{%s}\\) xác định tại \\(x=%d\\).' % (E, v), ans=val >= 0,
                ee='At \\(x=%d\\) the radicand is \\(%d\\), which is %s.' % (v, val, 'non-negative' if val >= 0 else 'negative'), ev='Tại \\(x=%d\\), biểu thức dưới dấu căn bằng \\(%d\\) %s.' % (v, val, '(không âm)' if val >= 0 else '(âm)'))

def b7_short_sum(r, lv):
    a, b = r.randint(2, 20), r.randint(2, 20); k = r.choice([1, 2, 3, -1])
    return dict(en='Compute \\(\\sqrt{%d}%s\\sqrt{%d}\\).' % (a * a, '+' if k == 1 else '-' if k == -1 else '+%d' % k, b * b), vi='Tính \\(\\sqrt{%d}%s\\sqrt{%d}\\).' % (a * a, '+' if k == 1 else '-' if k == -1 else '+%d' % k, b * b),
                key=str(a + k * b), ee='\\(%d%s=%d\\).' % (a, lin((k * b, '')) if k * b < 0 else '+%d' % (k * b), a + k * b), ev='\\(%d%s=%d\\).' % (a, lin((k * b, '')) if k * b < 0 else '+%d' % (k * b), a + k * b))

def b7_short_round(r, lv):
    while True:
        n = r.randint(2, 99)
        if int(n ** 0.5) ** 2 != n: break
    v = round(n ** 0.5 + 1e-12, 2); key = '%.2f' % v
    assert abs(v - n ** 0.5) <= 0.005
    return dict(en='Use a calculator to find \\(\\sqrt{%d}\\), rounded to two decimal places.' % n, vi='Dùng máy tính cầm tay tính \\(\\sqrt{%d}\\), làm tròn đến chữ số thập phân thứ hai.' % n,
                key=key, ee='\\(\\sqrt{%d}\\approx %s\\).' % (n, key), ev='\\(\\sqrt{%d}\\approx %s\\).' % (n, key.replace('.', '{,}')), hint=('Enter a decimal number (e.g. 3.33).', 'Nhập một số thập phân (ví dụ 3,33).'))

def b7_d1_none(r, lv):
    vals = r.sample(range(1, 50), 3); neg = -r.randint(1, 49)
    q = r.choice([('Which number has no square root?', 'Số nào không có căn bậc hai?'), ('Which of these numbers has no square root?', 'Số nào sau đây không có căn bậc hai?'), ('Choose the number that has no square root.', 'Chọn số không có căn bậc hai.'), ('Only one of these numbers has no square root. Which one?', 'Chỉ có một số không có căn bậc hai. Đó là số nào?')])
    return dict(en=q[0], vi=q[1], opts=[str(neg)] + [str(v) for v in vals[:2]] + ['0'], ans=0, ee='A negative number has no square root.', ev='Số âm không có căn bậc hai.')

def b7_d1_sq(r, lv):
    k = r.randint(2, 30)
    return dict(en='\\(\\sqrt{%d^2}\\) is equal to…' % k, vi='\\(\\sqrt{%d^2}\\) bằng…' % k, opts=[str(k), str(-k), '\\pm %d' % k, str(k * k)], ans=0,
                ee='\\(\\sqrt{a^2}=a\\) for \\(a\\ge0\\).', ev='\\(\\sqrt{a^2}=a\\) với \\(a\\ge0\\).')

def b7_d1_radicand(r, lv):
    a, b, c = nz(r, -7, 7), r.randint(-9, 9), r.randint(2, 9)
    E = lin((a, 'x'), (b, '')) if b else lin((a, 'x'))
    return dict(en='What is the radicand of \\(%d\\sqrt{%s}\\)?' % (c, E), vi='Biểu thức lấy căn của \\(%d\\sqrt{%s}\\) là gì?' % (c, E), opts=[E, str(c), '%d(%s)' % (c, E), '\\sqrt{%s}' % E], ans=0,
                ee='The radicand is the expression under the root sign.', ev='Biểu thức lấy căn là biểu thức nằm dưới dấu căn.')

def b7_d2_abs(r, lv):
    a, b = r.sample(range(1, 20), 2)
    return dict(en='Compute \\(\\sqrt{(%d-%d)^2}\\).' % (a, b), vi='Tính \\(\\sqrt{(%d-%d)^2}\\).' % (a, b), opts=pick_opts(r, str(abs(a - b)), [str(a - b) if a - b != abs(a - b) else str(-(a - b)), str(a + b), str((a - b) ** 2)]), ans=0,
                ee='\\(\\sqrt{(%d-%d)^2}=|%d|=%d\\).' % (a, b, a - b, abs(a - b)), ev='\\(\\sqrt{(%d-%d)^2}=|%d|=%d\\).' % (a, b, a - b, abs(a - b)))

def b7_d2_xsq(r, lv):
    n = r.choice([2, 3, 5, 6, 7, 10, 11, 13, 15, 17, 19, 21])
    return dict(en='Solve \\(x^2=%d\\).' % n, vi='Giải phương trình \\(x^2=%d\\).' % n, opts=['x=\\pm\\sqrt{%d}' % n, 'x=\\sqrt{%d}' % n, 'x=\\pm %d' % (n * n), 'x=\\dfrac{%d}{2}' % n], ans=0,
                ee='\\(x\\) is a square root of %d: \\(x=\\sqrt{%d}\\) or \\(x=-\\sqrt{%d}\\).' % (n, n, n), ev='\\(x\\) là căn bậc hai của %d: \\(x=\\sqrt{%d}\\) hoặc \\(x=-\\sqrt{%d}\\).' % (n, n, n))

def b7_d2_dk2(r, lv):
    k = r.randint(-9, 12)
    return dict(en='For which \\(x\\) is \\(\\sqrt{%d-x}\\) defined?' % k, vi='Biểu thức \\(\\sqrt{%d-x}\\) xác định khi nào?' % k, opts=['x\\le %d' % k, 'x\\ge %d' % k, 'x\\le %d' % (-k) if k else 'x\\lt 0', 'x\\lt %d' % k], ans=0,
                ee='\\(%d-x\\ge0\\Leftrightarrow x\\le %d\\).' % (k, k), ev='\\(%d-x\\ge0\\Leftrightarrow x\\le %d\\).' % (k, k))

def b7_d3_simpl(r, lv):
    a = r.randint(-6, 9); big = r.random() < 0.5
    cond = 'x\\gt %d' % a if big else 'x\\lt %d' % a
    good = lin((1, 'x'), (-a, '')) if big else lin((a, ''), (-1, 'x'))
    other = lin((a, ''), (-1, 'x')) if big else lin((1, 'x'), (-a, ''))
    return dict(en='Simplify \\(\\sqrt{(x%s)^2}\\) for \\(%s\\).' % (mono(-a, '', False) if a else '', cond), vi='Rút gọn \\(\\sqrt{(x%s)^2}\\) với \\(%s\\).' % (mono(-a, '', False) if a else '', cond),
                opts=pick_opts(r, good, [other, lin((1, 'x'), (a, '')) if a else '-x', '(x%s)^2' % (mono(-a, '', False) if a else '')]), ans=0,
                ee='\\(\\sqrt{A^2}=|A|\\); here \\(x%s\\) is %s.' % (mono(-a, '', False) if a else '', 'positive' if big else 'negative'), ev='\\(\\sqrt{A^2}=|A|\\); ở đây \\(x%s\\) %s.' % (mono(-a, '', False) if a else '', 'dương' if big else 'âm'))

def b7_d3_compare(r, lv):
    m = r.randint(2, 12); n = m * m + r.choice([-3, -2, -1, 1, 2, 3])
    s = '\\gt ' if n > m * m else '\\lt '
    return dict(en='Compare \\(%d\\) and \\(\\sqrt{%d}\\) without a calculator.' % (m, n), vi='So sánh \\(%d\\) và \\(\\sqrt{%d}\\) mà không dùng máy tính.' % (m, n),
                opts=['%d%s\\sqrt{%d}' % (m, '\\lt ' if s == '\\gt ' else '\\gt ', n), '%d%s\\sqrt{%d}' % (m, s, n), '%d=\\sqrt{%d}' % (m, n), '%d\\ge\\sqrt{%d}' % (m, n) if s == '\\gt ' else '%d\\le\\sqrt{%d}' % (m, n)], ans=0,
                ee='\\(%d=\\sqrt{%d}\\) and \\(%d%s%d\\).' % (m, m * m, m * m, '\\lt ' if s == '\\gt ' else '\\gt ', n), ev='\\(%d=\\sqrt{%d}\\) và \\(%d%s%d\\).' % (m, m * m, m * m, '\\lt ' if s == '\\gt ' else '\\gt ', n))

def b7_d3_value(r, lv):
    a, b = nz(r, -5, 6), r.randint(-10, 10); k = r.randint(1, 9); v = F(k * k - b, a)
    assert v.denominator == 1
    E = lin((a, 'x'), (b, ''))
    return dict(en='Find the value of \\(\\sqrt{%s}\\) at \\(x=%s\\).' % (E, fr(v)), vi='Tính giá trị của \\(\\sqrt{%s}\\) tại \\(x=%s\\).' % (E, fr(v)), opts=pick_opts(r, str(k), [str(-k), str(k * k), str(k + 1)]), ans=0,
                ee='The radicand equals \\(%d\\), so the value is \\(\\sqrt{%d}=%d\\).' % (k * k, k * k, k), ev='Biểu thức dưới dấu căn bằng \\(%d\\) nên giá trị là \\(\\sqrt{%d}=%d\\).' % (k * k, k * k, k))

def b7_d4_square(r, lv):
    s = r.randint(4, 40); S = s * s
    return dict(en='A square garden has an area of %d m². How many meters of fence are needed to go around it?' % S, vi='Một mảnh vườn hình vuông có diện tích %d m². Cần bao nhiêu mét hàng rào để rào quanh mảnh vườn?' % S,
                opts=pick_opts(r, '%d\\text{ m}' % (4 * s), ['%d\\text{ m}' % o for o in (s, 2 * s, S // 4 if S // 4 != 4 * s else S)]), ans=0,
                ee='Side \\(=\\sqrt{%d}=%d\\) m; perimeter \\(=4\\cdot%d=%d\\) m.' % (S, s, s, 4 * s), ev='Cạnh \\(=\\sqrt{%d}=%d\\) m; chu vi \\(=4\\cdot%d=%d\\) m.' % (S, s, s, 4 * s))

def b7_d4_poly(r, lv):
    a = r.randint(1, 6); v = a + r.randint(1, 9)
    E = 'x^2-%dx+%d' % (2 * a, a * a)
    return dict(en='Given \\(A=\\sqrt{%s}\\) with \\(x\\gt %d\\). Find \\(A\\) at \\(x=%d\\).' % (E, a, v), vi='Cho \\(A=\\sqrt{%s}\\) với \\(x\\gt %d\\). Tính \\(A\\) tại \\(x=%d\\).' % (E, a, v),
                opts=pick_opts(r, str(v - a), [str(a - v), str(v + a), str((v - a) ** 2)]), ans=0,
                ee='\\(A=\\sqrt{(x-%d)^2}=|x-%d|=x-%d\\) (because \\(x\\gt %d\\)); at \\(x=%d\\): \\(A=%d\\).' % (a, a, a, a, v, v - a),
                ev='\\(A=\\sqrt{(x-%d)^2}=|x-%d|=x-%d\\) (vì \\(x\\gt %d\\)); tại \\(x=%d\\): \\(A=%d\\).' % (a, a, a, a, v, v - a))

def b7_d4_int(r, lv):
    while True:
        a, b = r.randint(1, 4), r.choice([2, 3, 5, 6, 7, 10, 11, 13])
        if b > a * a: break
    E = '\\sqrt{(%d+\\sqrt{%d})^2}-\\sqrt{(%d-\\sqrt{%d})^2}' % (a, b, a, b)
    return dict(en='Compute \\(A=%s\\) without a calculator.' % E, vi='Tính \\(A=%s\\) mà không dùng máy tính.' % E, opts=[str(2 * a), '2\\sqrt{%d}' % b, '0', str(-2 * a)], ans=0,
                ee='\\(%d-\\sqrt{%d}\\lt0\\) because \\(%d\\lt %d\\); so \\(A=(%d+\\sqrt{%d})-(\\sqrt{%d}-%d)=%d\\).' % (a, b, a * a, b, a, b, b, a, 2 * a),
                ev='\\(%d-\\sqrt{%d}\\lt0\\) vì \\(%d\\lt %d\\); nên \\(A=(%d+\\sqrt{%d})-(\\sqrt{%d}-%d)=%d\\).' % (a, b, a * a, b, a, b, b, a, 2 * a))

L7_GROUPS = [[('mcq', b7_roots), ('mcq', b7_arith), ('mcq', b7_dk)], [('tf', b7_tf_abs), ('tf', b7_tf_def)], [('short', b7_short_sum), ('short', b7_short_round)],
             [('mcq', b7_d1_none), ('mcq', b7_d1_sq), ('mcq', b7_d1_radicand)], [('mcq', b7_d2_abs), ('mcq', b7_d2_xsq), ('mcq', b7_d2_dk2)],
             [('mcq', b7_d3_simpl), ('mcq', b7_d3_compare), ('mcq', b7_d3_value)], [('mcq', b7_d4_square), ('mcq', b7_d4_poly), ('mcq', b7_d4_int)]]

# =====================================================================================================
# BÀI 8. Khai căn bậc hai với phép nhân và phép chia
# =====================================================================================================
SQF = [2, 3, 5, 6, 7, 10]
def b8_mul(r, lv):
    m = r.choice(SQF); p, q = r.randint(1, 6), r.randint(1, 6); a, b = m * p * p, m * q * q
    assert a != b
    return dict(en='Compute \\(\\sqrt{%d}\\cdot\\sqrt{%d}\\).' % (a, b), vi='Tính \\(\\sqrt{%d}\\cdot\\sqrt{%d}\\).' % (a, b), opts=pick_opts(r, str(m * p * q), ['\\sqrt{%d}' % (a + b), str(a * b), str(m * p * q + 1)]), ans=0,
                ee='\\(\\sqrt{%d}\\cdot\\sqrt{%d}=\\sqrt{%d}=%d\\).' % (a, b, a * b, m * p * q), ev='\\(\\sqrt{%d}\\cdot\\sqrt{%d}=\\sqrt{%d}=%d\\).' % (a, b, a * b, m * p * q))

def b8_quot(r, lv):
    p, q = r.randint(1, 15), r.randint(2, 16); f = F(p, q); assert f.denominator == q and p != q
    return dict(en='Compute \\(\\sqrt{\\dfrac{%d}{%d}}\\).' % (p * p, q * q), vi='Tính \\(\\sqrt{\\dfrac{%d}{%d}}\\).' % (p * p, q * q), opts=pick_opts(r, fr(f), [fr(F(p * p, q)), fr(F(q, p)), '-' + fr(f)]), ans=0,
                ee='\\(\\sqrt{\\dfrac{%d}{%d}}=\\dfrac{\\sqrt{%d}}{\\sqrt{%d}}=%s\\).' % (p * p, q * q, p * p, q * q, fr(f)), ev='\\(\\sqrt{\\dfrac{%d}{%d}}=\\dfrac{\\sqrt{%d}}{\\sqrt{%d}}=%s\\).' % (p * p, q * q, p * p, q * q, fr(f)))

def b8_div(r, lv):
    m = r.choice(SQF); k = r.randint(2, 12); a = m * k * k
    return dict(en='Compute \\(\\dfrac{\\sqrt{%d}}{\\sqrt{%d}}\\).' % (a, m), vi='Tính \\(\\dfrac{\\sqrt{%d}}{\\sqrt{%d}}\\).' % (a, m), opts=pick_opts(r, str(k), [str(k * k), '\\sqrt{%d}' % (a - m), str(a // m // 2) if a // m // 2 != k else str(k + 1)]), ans=0,
                ee='\\(\\dfrac{\\sqrt{%d}}{\\sqrt{%d}}=\\sqrt{\\dfrac{%d}{%d}}=\\sqrt{%d}=%d\\).' % (a, m, a, m, k * k, k), ev='\\(\\dfrac{\\sqrt{%d}}{\\sqrt{%d}}=\\sqrt{\\dfrac{%d}{%d}}=\\sqrt{%d}=%d\\).' % (a, m, a, m, k * k, k))

def b8_tf_num(r, lv):
    p, q = r.randint(2, 12), r.randint(2, 12); truth = r.random() < 0.5; c = p * q if truth else r.choice([p + q, p * q + 1, p * q * 2])
    assert truth or c != p * q
    return dict(en='\\(\\sqrt{%d\\cdot%d}=%d\\).' % (p * p, q * q, c), vi='\\(\\sqrt{%d\\cdot%d}=%d\\).' % (p * p, q * q, c), ans=truth,
                ee='\\(\\sqrt{%d}\\cdot\\sqrt{%d}=%d\\cdot%d=%d\\).' % (p * p, q * q, p, q, p * q), ev='\\(\\sqrt{%d}\\cdot\\sqrt{%d}=%d\\cdot%d=%d\\).' % (p * p, q * q, p, q, p * q))

def b8_tf_abs(r, lv):
    k = r.randint(2, 9); v = r.choice(['x', 'a', 'm']); truth = r.random() < 0.5
    rhs = '%d|%s|y^2' % (k, v) if truth else '%d%sy^2' % (k, v)
    return dict(en='\\(\\sqrt{%d%s^2y^4}=%s\\) for all real numbers \\(%s, y\\).' % (k * k, v, rhs, v), vi='\\(\\sqrt{%d%s^2y^4}=%s\\) với mọi số thực \\(%s, y\\).' % (k * k, v, rhs, v), ans=truth,
                ee='\\(\\sqrt{%d}\\cdot\\sqrt{%s^2}\\cdot\\sqrt{y^4}=%d|%s|y^2\\) (\\(y^2\\ge0\\) but \\(%s\\) may be negative).' % (k * k, v, k, v, v),
                ev='\\(\\sqrt{%d}\\cdot\\sqrt{%s^2}\\cdot\\sqrt{y^4}=%d|%s|y^2\\) (\\(y^2\\ge0\\) nhưng \\(%s\\) có thể âm).' % (k * k, v, k, v, v))

def b8_short_mul(r, lv):
    m = r.choice(SQF); p, q = r.randint(1, 7), r.randint(2, 7); a, b = m * p * p, m * q * q; c = r.randint(1, 30)
    return dict(en='Compute \\(\\sqrt{%d}\\cdot\\sqrt{%d}+%d\\).' % (a, b, c), vi='Tính \\(\\sqrt{%d}\\cdot\\sqrt{%d}+%d\\).' % (a, b, c), key=str(m * p * q + c),
                ee='\\(\\sqrt{%d}=%d\\), so the result is \\(%d\\).' % (a * b, m * p * q, m * p * q + c), ev='\\(\\sqrt{%d}=%d\\), nên kết quả là \\(%d\\).' % (a * b, m * p * q, m * p * q + c))

def b8_short_volt(r, lv):
    U = r.choice([6, 9, 10, 12, 20, 24, 30, 40, 50]); R = r.choice([2, 3, 4, 5, 6, 8, 10, 12, 20]); P = F(U * U, R)
    assert P.denominator == 1
    return dict(en='The power of a device is \\(P=\\dfrac{U^2}{R}\\). With \\(P=%d\\) W and \\(R=%d\\ \\Omega\\), the voltage is \\(U=\\sqrt{P\\cdot R}\\). Find \\(U\\) (in volts).' % (P, R),
                vi='Công suất của một thiết bị là \\(P=\\dfrac{U^2}{R}\\). Với \\(P=%d\\) W và \\(R=%d\\ \\Omega\\), hiệu điện thế là \\(U=\\sqrt{P\\cdot R}\\). Tính \\(U\\) (vôn).' % (P, R),
                key=str(U), ee='\\(U=\\sqrt{%d\\cdot%d}=\\sqrt{%d}=%d\\) V.' % (P, R, U * U, U), ev='\\(U=\\sqrt{%d\\cdot%d}=\\sqrt{%d}=%d\\) V.' % (P, R, U * U, U))

def b8_d1_cond(r, lv):
    v1, v2 = r.choice([('A', 'B'), ('a', 'b'), ('M', 'N'), ('x', 'y')])
    o = [tx('\\(%s\\ge0\\) and \\(%s\\ge0\\)' % (v1, v2), '\\(%s\\ge0\\) và \\(%s\\ge0\\)' % (v1, v2)), tx('for all \\(%s, %s\\)' % (v1, v2), 'với mọi \\(%s, %s\\)' % (v1, v2)),
         tx('only \\(%s\\gt0\\)' % v1, 'chỉ cần \\(%s\\gt0\\)' % v1), tx('\\(%s\\ne0\\)' % v2, '\\(%s\\ne0\\)' % v2)]
    return dict(en='The rule \\(\\sqrt{%s%s}=\\sqrt{%s}\\cdot\\sqrt{%s}\\) holds when…' % (v1, v2, v1, v2), vi='Quy tắc \\(\\sqrt{%s%s}=\\sqrt{%s}\\cdot\\sqrt{%s}\\) đúng khi…' % (v1, v2, v1, v2), opts=o, ans=0,
                ee='Both factors must be non-negative.', ev='Cả hai thừa số phải không âm.')

def b8_d1_qcond(r, lv):
    v1, v2 = r.choice([('A', 'B'), ('a', 'b'), ('M', 'N'), ('x', 'y')])
    o = [tx('\\(%s\\ge0\\) and \\(%s\\gt0\\)' % (v1, v2), '\\(%s\\ge0\\) và \\(%s\\gt0\\)' % (v1, v2)), tx('\\(%s\\ge0\\) and \\(%s\\ge0\\)' % (v1, v2), '\\(%s\\ge0\\) và \\(%s\\ge0\\)' % (v1, v2)),
         tx('for all \\(%s, %s\\)' % (v1, v2), 'với mọi \\(%s, %s\\)' % (v1, v2)), tx('\\(%s\\gt0\\) and \\(%s\\ge0\\)' % (v1, v2), '\\(%s\\gt0\\) và \\(%s\\ge0\\)' % (v1, v2))]
    return dict(en='The rule \\(\\sqrt{\\dfrac{%s}{%s}}=\\dfrac{\\sqrt{%s}}{\\sqrt{%s}}\\) holds when…' % (v1, v2, v1, v2), vi='Quy tắc \\(\\sqrt{\\dfrac{%s}{%s}}=\\dfrac{\\sqrt{%s}}{\\sqrt{%s}}\\) đúng khi…' % (v1, v2, v1, v2), opts=o, ans=0,
                ee='The numerator must be non-negative and the denominator positive.', ev='Tử không âm và mẫu dương.')

def b8_d1_num(r, lv):
    p, q = r.randint(2, 15), r.randint(2, 15); assert p != q
    return dict(en='Compute \\(\\sqrt{%d\\cdot%d}\\).' % (p * p, q * q), vi='Tính \\(\\sqrt{%d\\cdot%d}\\).' % (p * p, q * q), opts=pick_opts(r, str(p * q), [str(p + q), str(p * p * q * q), str(p * q * 2)]), ans=0,
                ee='\\(\\sqrt{%d}\\cdot\\sqrt{%d}=%d\\cdot%d=%d\\).' % (p * p, q * q, p, q, p * q), ev='\\(\\sqrt{%d}\\cdot\\sqrt{%d}=%d\\cdot%d=%d\\).' % (p * p, q * q, p, q, p * q))

def b8_d2_three(r, lv):
    p, q, s = r.sample([2, 3, 5, 7, 11], 3)
    return dict(en='Compute \\(\\sqrt{%d^2\\cdot%d^2\\cdot%d^2}\\).' % (p, q, s), vi='Tính \\(\\sqrt{%d^2\\cdot%d^2\\cdot%d^2}\\).' % (p, q, s), opts=pick_opts(r, str(p * q * s), [str(p + q + s), str((p * q * s) ** 2), str(p * q * s * 2)]), ans=0,
                ee='\\(%d\\cdot%d\\cdot%d=%d\\).' % (p, q, s, p * q * s), ev='\\(%d\\cdot%d\\cdot%d=%d\\).' % (p, q, s, p * q * s))

def b8_d2_neg(r, lv):
    k = r.randint(2, 12); sign = r.choice(['\\lt ', '\\gt '])
    good = '%da' % (-k) if sign == '\\lt ' else '%da' % k
    return dict(en='Simplify \\(\\sqrt{%da^2}\\) for \\(a%s0\\).' % (k * k, sign), vi='Rút gọn \\(\\sqrt{%da^2}\\) với \\(a%s0\\).' % (k * k, sign),
                opts=[good, '%da' % k if good.startswith('-') else '%da' % (-k), '%da' % (k * k), '\\pm %da' % k], ans=0,
                ee='\\(\\sqrt{%da^2}=%d|a|=%s\\).' % (k * k, k, good), ev='\\(\\sqrt{%da^2}=%d|a|=%s\\).' % (k * k, k, good))

def b8_d2_bracket(r, lv):
    m = r.choice([2, 3, 5, 6, 7]); p = r.randint(2, 6); q = r.randint(1, 4); assert p != q
    a, b = m * p * p, m * q * q        # √m(√a + √b) = m(p + q)
    return dict(en='Compute \\(\\sqrt{%d}\\left(\\sqrt{%d}+\\sqrt{%d}\\right)\\).' % (m, a, b), vi='Tính \\(\\sqrt{%d}\\left(\\sqrt{%d}+\\sqrt{%d}\\right)\\).' % (m, a, b),
                opts=pick_opts(r, str(m * (p + q)), [str(m * p * q), str(p + q), '\\sqrt{%d}' % (m * (a + b))]), ans=0,
                ee='\\(\\sqrt{%d}+\\sqrt{%d}=%d+%d=%d\\).' % (m * a, m * b, m * p, m * q, m * (p + q)), ev='\\(\\sqrt{%d}+\\sqrt{%d}=%d+%d=%d\\).' % (m * a, m * b, m * p, m * q, m * (p + q)))

def b8_d3_var(r, lv):
    m = r.choice([2, 3, 5, 6, 7]); k = r.randint(2, 7)
    return dict(en='Simplify \\(\\dfrac{\\sqrt{%da^3}}{\\sqrt{%da}}\\) with \\(a\\gt0\\).' % (m * k * k, m), vi='Rút gọn \\(\\dfrac{\\sqrt{%da^3}}{\\sqrt{%da}}\\) với \\(a\\gt0\\).' % (m * k * k, m),
                opts=['%da' % k, '%da^2' % k, '%da' % (k * k), '%d\\sqrt{a}' % k], ans=0,
                ee='\\(\\sqrt{\\dfrac{%da^3}{%da}}=\\sqrt{%da^2}=%da\\) (\\(a\\gt0\\)).' % (m * k * k, m, k * k, k), ev='\\(\\sqrt{\\dfrac{%da^3}{%da}}=\\sqrt{%da^2}=%da\\) (\\(a\\gt0\\)).' % (m * k * k, m, k * k, k))

def b8_d3_four(r, lv):
    k = r.randint(2, 12)
    return dict(en='Simplify \\(\\sqrt{%da^4}\\).' % (k * k), vi='Rút gọn \\(\\sqrt{%da^4}\\).' % (k * k), opts=['%da^2' % k, '%d|a|' % k, '%da^4' % k, '%da^2' % (-k)], ans=0,
                ee='\\(\\sqrt{%d}\\cdot\\sqrt{(a^2)^2}=%da^2\\) because \\(a^2\\ge0\\).' % (k * k, k), ev='\\(\\sqrt{%d}\\cdot\\sqrt{(a^2)^2}=%da^2\\) vì \\(a^2\\ge0\\).' % (k * k, k))

def b8_d3_rect(r, lv):
    m = r.choice(SQF); p, q = r.randint(1, 6), r.randint(1, 6); a, b = m * p * p, m * q * q
    assert a != b
    return dict(en='A rectangle has sides \\(\\sqrt{%d}\\) cm and \\(\\sqrt{%d}\\) cm. Find its area.' % (a, b), vi='Một hình chữ nhật có hai cạnh \\(\\sqrt{%d}\\) cm và \\(\\sqrt{%d}\\) cm. Tính diện tích hình chữ nhật.' % (a, b),
                opts=pick_opts(r, '%d\\text{ cm}^2' % (m * p * q), ['\\sqrt{%d}\\text{ cm}^2' % (a + b), '%d\\text{ cm}^2' % (a * b), '%d\\text{ cm}^2' % (2 * m * p * q)]), ans=0,
                ee='\\(S=\\sqrt{%d}\\cdot\\sqrt{%d}=\\sqrt{%d}=%d\\) cm².' % (a, b, a * b, m * p * q), ev='\\(S=\\sqrt{%d}\\cdot\\sqrt{%d}=\\sqrt{%d}=%d\\) cm².' % (a, b, a * b, m * p * q))

def b8_d4_volt(r, lv):
    q = b8_short_volt(r, lv); U = int(q['key'])
    q = dict(q, opts=pick_opts(r, '%d\\text{ V}' % U, ['%d\\text{ V}' % o for o in (U * U, U // 2 if U // 2 else U + 1, U + 2)]), ans=0)
    q['en'] = q['en'].replace('Find \\(U\\) (in volts).', 'Which value is \\(U\\)?'); q['vi'] = q['vi'].replace('Tính \\(U\\) (vôn).', '\\(U\\) bằng bao nhiêu?')
    del q['key']; return q

def b8_d4_frac(r, lv):
    k = r.choice([2, 3, 5, 6, 7, 10]); c = r.randint(1, 6)
    return dict(en='Simplify \\((a-%d)\\sqrt{\\dfrac{%d}{(a-%d)^2}}\\) with \\(a\\gt %d\\).' % (c, k, c, c), vi='Rút gọn \\((a-%d)\\sqrt{\\dfrac{%d}{(a-%d)^2}}\\) với \\(a\\gt %d\\).' % (c, k, c, c),
                opts=['\\sqrt{%d}' % k, '-\\sqrt{%d}' % k, '(a-%d)\\sqrt{%d}' % (c, k), str(k)], ans=0,
                ee='\\(\\sqrt{\\dfrac{%d}{(a-%d)^2}}=\\dfrac{\\sqrt{%d}}{|a-%d|}=\\dfrac{\\sqrt{%d}}{a-%d}\\) since \\(a\\gt %d\\); multiply by \\(a-%d\\).' % (k, c, k, c, k, c, c, c),
                ev='\\(\\sqrt{\\dfrac{%d}{(a-%d)^2}}=\\dfrac{\\sqrt{%d}}{|a-%d|}=\\dfrac{\\sqrt{%d}}{a-%d}\\) vì \\(a\\gt %d\\); nhân với \\(a-%d\\).' % (k, c, k, c, k, c, c, c))

def b8_d4_combo(r, lv):
    m1, k1 = r.choice([2, 3, 5]), r.randint(2, 9); m2, k2 = r.choice([2, 3, 5]), r.randint(2, 6)
    v = k1 - m2 * k2
    A = '\\dfrac{\\sqrt{%d}}{\\sqrt{%d}}-\\sqrt{%d}\\cdot\\sqrt{%d}' % (m1 * k1 * k1, m1, m2, m2 * k2 * k2)
    return dict(en='Compute \\(%s\\).' % A, vi='Tính \\(%s\\).' % A, opts=pick_opts(r, str(v), [str(k1 + m2 * k2), str(k1 * k1 - m2 * k2), str(-v) if v else '1']), ans=0,
                ee='\\(\\sqrt{%d}=%d\\) and \\(\\sqrt{%d}=%d\\), so the result is \\(%d\\).' % (k1 * k1, k1, m2 * m2 * k2 * k2, m2 * k2, v),
                ev='\\(\\sqrt{%d}=%d\\) và \\(\\sqrt{%d}=%d\\), nên kết quả là \\(%d\\).' % (k1 * k1, k1, m2 * m2 * k2 * k2, m2 * k2, v))

def _isq(n):
    s = int(round(n ** 0.5)); assert s * s == n; return s

L8_GROUPS = [[('mcq', b8_mul), ('mcq', b8_quot), ('mcq', b8_div)], [('tf', b8_tf_num), ('tf', b8_tf_abs)], [('short', b8_short_mul), ('short', b8_short_volt)],
             [('mcq', b8_d1_cond), ('mcq', b8_d1_qcond), ('mcq', b8_d1_num)], [('mcq', b8_d2_three), ('mcq', b8_d2_neg), ('mcq', b8_d2_bracket)],
             [('mcq', b8_d3_var), ('mcq', b8_d3_four), ('mcq', b8_d3_rect)], [('mcq', b8_d4_volt), ('mcq', b8_d4_frac), ('mcq', b8_d4_combo)]]

# =====================================================================================================
# BÀI 9. Biến đổi đơn giản và rút gọn biểu thức chứa căn thức bậc hai
# =====================================================================================================
SQF2 = [2, 3, 5, 6, 7, 10, 11, 13, 14, 15]
def rad(k, m):
    """k√m dạng tex (k nguyên khác 0)."""
    return ('' if k == 1 else '-' if k == -1 else str(k)) + '\\sqrt{%d}' % m

def b9_out(r, lv):
    k, m = r.randint(2, 9), r.choice(SQF2)
    return dict(en='Take a factor out of the root sign: \\(\\sqrt{%d}\\).' % (k * k * m), vi='Đưa thừa số ra ngoài dấu căn: \\(\\sqrt{%d}\\).' % (k * k * m),
                opts=pick_opts(r, rad(k, m), [rad(m, k) if m != k else rad(k + 1, m), rad(k * k, m), '\\sqrt{%d}' % (k * m)]), ans=0,
                ee='\\(%d=%d^2\\cdot%d\\), so \\(\\sqrt{%d}=%s\\).' % (k * k * m, k, m, k * k * m, rad(k, m)), ev='\\(%d=%d^2\\cdot%d\\) nên \\(\\sqrt{%d}=%s\\).' % (k * k * m, k, m, k * k * m, rad(k, m)))

def b9_in(r, lv):
    k, m = nz(r, -9, 9), r.choice(SQF2); assert abs(k) > 1
    good = ('-' if k < 0 else '') + '\\sqrt{%d}' % (k * k * m)
    return dict(en='Take the factor into the root sign: \\(%s\\).' % rad(k, m), vi='Đưa thừa số vào trong dấu căn: \\(%s\\).' % rad(k, m),
                opts=pick_opts(r, good, [('' if k < 0 else '-') + '\\sqrt{%d}' % (k * k * m), '\\sqrt{%d}' % (abs(k) * m) if k > 0 else '-\\sqrt{%d}' % (abs(k) * m), '\\sqrt{%d}' % (k * k * m) if k < 0 else '\\sqrt{%d}' % (k * m * m)]), ans=0,
                ee='%s' % ('\\(%d\\gt0\\): \\(%s=\\sqrt{%d^2\\cdot%d}\\).' % (k, rad(k, m), k, m) if k > 0 else '\\(%d\\lt0\\): keep the minus sign outside: \\(%s=-\\sqrt{%d^2\\cdot%d}\\).' % (k, rad(k, m), -k, m)),
                ev='%s' % ('\\(%d\\gt0\\): \\(%s=\\sqrt{%d^2\\cdot%d}\\).' % (k, rad(k, m), k, m) if k > 0 else '\\(%d\\lt0\\): giữ dấu trừ ở ngoài: \\(%s=-\\sqrt{%d^2\\cdot%d}\\).' % (k, rad(k, m), -k, m)))

def b9_ratc(r, lv):
    m = r.choice(SQF2); c = m * r.randint(1, 6) if r.random() < 0.5 else r.randint(1, 9)
    f = F(c, m); num = ('' if f.numerator == 1 else str(f.numerator)) + '\\sqrt{%d}' % m
    good = num if f.denominator == 1 else '\\dfrac{%s}{%d}' % (num, f.denominator)
    bads = ['\\dfrac{%d}{%d}' % (c, m), '\\dfrac{%d\\sqrt{%d}}{%d}' % (c, m, m * m) if c != m else '\\dfrac{\\sqrt{%d}}{%d}' % (m, m), '%d\\sqrt{%d}' % (c * m, m)]
    return dict(en='Rationalize the denominator: \\(\\dfrac{%d}{\\sqrt{%d}}\\).' % (c, m), vi='Trục căn thức ở mẫu: \\(\\dfrac{%d}{\\sqrt{%d}}\\).' % (c, m), opts=pick_opts(r, good, bads), ans=0,
                ee='Multiply the numerator and the denominator by \\(\\sqrt{%d}\\): \\(\\dfrac{%d\\sqrt{%d}}{%d}\\), then simplify: \\(%s\\).' % (m, c, m, m, good), ev='Nhân cả tử và mẫu với \\(\\sqrt{%d}\\): \\(\\dfrac{%d\\sqrt{%d}}{%d}\\), rút gọn được \\(%s\\).' % (m, c, m, m, good))

def b9_tf_cmp(r, lv):
    a, b, c, d = r.randint(2, 7), r.choice(SQF2), r.randint(2, 7), r.choice(SQF2)
    x, y = a * a * b, c * c * d; assert x != y
    claim = r.choice(['\\gt ', '\\lt ']); truth = (x > y) == (claim == '\\gt ')
    return dict(en='\\(%s%s%s\\).' % (rad(a, b), claim, rad(c, d)), vi='\\(%s%s%s\\).' % (rad(a, b), claim, rad(c, d)), ans=truth,
                ee='\\(%s=\\sqrt{%d}\\), \\(%s=\\sqrt{%d}\\); compare \\(%d\\) and \\(%d\\).' % (rad(a, b), x, rad(c, d), y, x, y), ev='\\(%s=\\sqrt{%d}\\), \\(%s=\\sqrt{%d}\\); so sánh \\(%d\\) và \\(%d\\).' % (rad(a, b), x, rad(c, d), y, x, y))

def b9_tf_neg(r, lv):
    k, m = r.randint(2, 9), r.choice(SQF2); truth = r.random() < 0.5
    rhs = rad(k, m) if truth else rad(-k, m)
    return dict(en='\\(\\sqrt{(-%d)^2\\cdot%d}=%s\\).' % (k, m, rhs), vi='\\(\\sqrt{(-%d)^2\\cdot%d}=%s\\).' % (k, m, rhs), ans=truth,
                ee='\\(\\sqrt{A^2B}=|A|\\sqrt{B}\\): \\(|-%d|\\sqrt{%d}=%s\\).' % (k, m, rad(k, m)), ev='\\(\\sqrt{A^2B}=|A|\\sqrt{B}\\): \\(|-%d|\\sqrt{%d}=%s\\).' % (k, m, rad(k, m)))

def b9_short_comb(r, lv):
    m = r.choice([2, 3, 5, 6, 7]); p, q, s_ = r.sample(range(1, 7), 3); a, b = r.randint(1, 4), nz(r, -3, 3)
    t = a * p + b * q - s_
    E = '%d\\sqrt{%d}%s\\sqrt{%d}-\\sqrt{%d}' % (a, p * p * m, ('+%d' % b if b > 0 else '%d' % b) if abs(b) != 1 else ('+' if b > 0 else '-'), q * q * m, s_ * s_ * m)
    return dict(en='Write \\(%s\\) in the form \\(t\\sqrt{%d}\\). Find \\(t\\).' % (E, m), vi='Viết \\(%s\\) dưới dạng \\(t\\sqrt{%d}\\). Tìm \\(t\\).' % (E, m), key=str(t),
                ee='\\(%d\\cdot%d%s%s-%d=%d\\).' % (a, p, '+' if b > 0 else '-', '%d\\cdot%d' % (abs(b), q), s_, t), ev='\\(%d\\cdot%d%s%s-%d=%d\\).' % (a, p, '+' if b > 0 else '-', '%d\\cdot%d' % (abs(b), q), s_, t))

def b9_short_conj(r, lv):
    while True:
        k = r.randint(1, 5); n = r.choice(SQF2); d = n - k * k
        if d != 0 and abs(d) <= 4: break
    c = d * r.randint(1, 4); A, B = F(c * k, d), F(c, d)
    return dict(en='Rationalize the denominator of \\(\\dfrac{%d}{\\sqrt{%d}-%d}\\) and write it as \\(a+b\\sqrt{%d}\\). Find \\(a+b\\).' % (c, n, k, n),
                vi='Trục căn thức ở mẫu của \\(\\dfrac{%d}{\\sqrt{%d}-%d}\\) và viết dưới dạng \\(a+b\\sqrt{%d}\\). Tìm \\(a+b\\).' % (c, n, k, n), key=fr(A + B),
                ee='Multiply by the conjugate \\(\\sqrt{%d}+%d\\): \\(\\dfrac{%d(\\sqrt{%d}+%d)}{%d}=%s+%s\\sqrt{%d}\\).' % (n, k, c, n, k, d, fr(A), fr(B), n),
                ev='Nhân với biểu thức liên hợp \\(\\sqrt{%d}+%d\\): \\(\\dfrac{%d(\\sqrt{%d}+%d)}{%d}=%s+%s\\sqrt{%d}\\).' % (n, k, c, n, k, d, fr(A), fr(B), n))

def b9_d1_abs(r, lv):
    v = r.choice(['a', 'x', 'm']); m = r.choice(SQF2)
    return dict(en='For \\(%s\\lt0\\), \\(\\sqrt{%s^2\\cdot%d}\\) is equal to…' % (v, v, m), vi='Với \\(%s\\lt0\\), \\(\\sqrt{%s^2\\cdot%d}\\) bằng…' % (v, v, m),
                opts=['-%s\\sqrt{%d}' % (v, m), '%s\\sqrt{%d}' % (v, m), '%s^2\\sqrt{%d}' % (v, m), '\\sqrt{%d}%s' % (m, v)], ans=0,
                ee='\\(\\sqrt{%s^2\\cdot%d}=|%s|\\sqrt{%d}=-%s\\sqrt{%d}\\) because \\(%s\\lt0\\).' % (v, m, v, m, v, m, v), ev='\\(\\sqrt{%s^2\\cdot%d}=|%s|\\sqrt{%d}=-%s\\sqrt{%d}\\) vì \\(%s\\lt0\\).' % (v, m, v, m, v, m, v))

def b9_d1_conj(r, lv):
    m, k = r.choice(SQF2), r.randint(1, 9); sign = r.choice(['-', '+'])
    other = '+' if sign == '-' else '-'
    return dict(en='What is the conjugate expression of \\(\\sqrt{%d}%s%d\\)?' % (m, sign, k), vi='Biểu thức liên hợp của \\(\\sqrt{%d}%s%d\\) là gì?' % (m, sign, k),
                opts=['\\sqrt{%d}%s%d' % (m, other, k), '%d%s\\sqrt{%d}' % (k, sign, m), '\\sqrt{%d}%s%d' % (m, sign, k), '-\\sqrt{%d}%s%d' % (m, sign, k)], ans=0,
                ee='Change the sign between the two terms; the product is \\(%d-%d\\).' % (m, k * k), ev='Đổi dấu giữa hai hạng tử; tích của chúng là \\(%d-%d\\).' % (m, k * k))

def b9_d1_write(r, lv):
    k, m = r.randint(2, 12), r.choice(SQF2)
    return dict(en='Write \\(\\sqrt{%d}\\) in the form \\(a\\sqrt{b}\\) with \\(b=%d\\).' % (k * k * m, m), vi='Viết \\(\\sqrt{%d}\\) dưới dạng \\(a\\sqrt{b}\\) với \\(b=%d\\).' % (k * k * m, m),
                opts=pick_opts(r, rad(k, m), [rad(k * k, m), rad(k + 1, m), rad(k - 1, m) if k > 2 else rad(k + 2, m)]), ans=0, ee='\\(\\sqrt{%d^2\\cdot%d}=%s\\).' % (k, m, rad(k, m)), ev='\\(\\sqrt{%d^2\\cdot%d}=%s\\).' % (k, m, rad(k, m)))

def b9_d2_inneg(r, lv):
    k, m = r.randint(2, 9), r.choice(SQF2)
    return dict(en='Which expression equals \\(-%s\\)?' % rad(k, m), vi='Biểu thức nào bằng \\(-%s\\)?' % rad(k, m),
                opts=['-\\sqrt{%d}' % (k * k * m), '\\sqrt{%d}' % (k * k * m), '\\sqrt{-%d}' % (k * k * m), '-\\sqrt{%d}' % (k * m)], ans=0,
                ee='\\(%s=\\sqrt{%d}\\), so \\(-%s=-\\sqrt{%d}\\).' % (rad(k, m), k * k * m, rad(k, m), k * k * m), ev='\\(%s=\\sqrt{%d}\\) nên \\(-%s=-\\sqrt{%d}\\).' % (rad(k, m), k * k * m, rad(k, m), k * k * m))

def b9_d2_clear(r, lv):
    p, q = r.choice([(1, 2), (1, 3), (2, 3), (3, 5), (2, 5), (1, 5), (3, 7), (5, 6), (1, 6), (2, 7)])
    return dict(en='Clear the fraction inside the root: \\(\\sqrt{\\dfrac{%d}{%d}}\\).' % (p, q), vi='Khử mẫu của biểu thức lấy căn: \\(\\sqrt{\\dfrac{%d}{%d}}\\).' % (p, q),
                opts=['\\dfrac{\\sqrt{%d}}{%d}' % (p * q, q), '\\dfrac{\\sqrt{%d}}{%d}' % (p * q, q * q), '\\dfrac{\\sqrt{%d}}{%d}' % (p, q), '\\dfrac{%d\\sqrt{%d}}{%d}' % (p, q, q * q)], ans=0,
                ee='\\(\\sqrt{\\dfrac{%d}{%d}}=\\sqrt{\\dfrac{%d\\cdot%d}{%d^2}}=\\dfrac{\\sqrt{%d}}{%d}\\).' % (p, q, p, q, q, p * q, q), ev='\\(\\sqrt{\\dfrac{%d}{%d}}=\\sqrt{\\dfrac{%d\\cdot%d}{%d^2}}=\\dfrac{\\sqrt{%d}}{%d}\\).' % (p, q, p, q, q, p * q, q))

def b9_d2_like(r, lv):
    m = r.choice(SQF2); a, b, c = r.randint(2, 9), nz(r, -8, 8), r.randint(1, 6)
    t = a + b - c; E = '%d\\sqrt{%d}%s\\sqrt{%d}-%s' % (a, m, ('+%d' % b if b > 0 else '%d' % b) if abs(b) != 1 else ('+' if b > 0 else '-'), m, rad(c, m))
    good = rad(t, m) if t else '0'
    return dict(en='Simplify \\(%s\\).' % E, vi='Rút gọn \\(%s\\).' % E, opts=pick_opts(r, good, [rad(t + 2, m) if t + 2 else '0', rad(a + b + c, m) if a + b + c else '0', '\\sqrt{%d}' % (abs(t) * m) if t else rad(1, m)], fill=lambda u: rad(t + 3 * u, m) if t + 3 * u else '1'), ans=0,
                ee='Combine like radicals: \\((%d%s-%d)\\sqrt{%d}=%s\\).' % (a, mono(b, '', False), c, m, good), ev='Cộng các căn đồng dạng: \\((%d%s-%d)\\sqrt{%d}=%s\\).' % (a, mono(b, '', False), c, m, good))

def b9_d3_simpl(r, lv):
    m = r.choice([2, 3, 5, 6, 7]); p, q, s_ = r.sample(range(1, 7), 3); t = p + q - s_
    E = '\\sqrt{%d}+\\sqrt{%d}-\\sqrt{%d}' % (p * p * m, q * q * m, s_ * s_ * m); good = rad(t, m) if t else '0'
    return dict(en='Simplify \\(%s\\).' % E, vi='Rút gọn \\(%s\\).' % E, opts=pick_opts(r, good, ['\\sqrt{%d}' % ((p * p + q * q - s_ * s_) * m) if p * p + q * q - s_ * s_ > 0 else rad(t + 1, m) if t + 1 else '1', rad(p + q + s_, m), rad(t - 1, m) if t - 1 else '0'], fill=lambda u: rad(t + 2 * u, m) if t + 2 * u else '2'), ans=0,
                ee='\\(%s+%s-%s=%s\\).' % (rad(p, m), rad(q, m), rad(s_, m), good), ev='\\(%s+%s-%s=%s\\).' % (rad(p, m), rad(q, m), rad(s_, m), good))

def b9_d3_conj(r, lv):
    while True:
        k = r.randint(1, 4); n = r.choice(SQF2); d = n - k * k
        if 1 <= d <= 3: break
    c = d * r.randint(1, 3); B = c // d; A = c * k // d
    good = '%s\\sqrt{%d}-%d' % ('' if B == 1 else B, n, A)
    return dict(en='Rationalize the denominator: \\(\\dfrac{%d}{\\sqrt{%d}+%d}\\).' % (c, n, k), vi='Trục căn thức ở mẫu: \\(\\dfrac{%d}{\\sqrt{%d}+%d}\\).' % (c, n, k),
                opts=pick_opts(r, good, ['%s\\sqrt{%d}+%d' % ('' if B == 1 else B, n, A), '%d-%s\\sqrt{%d}' % (A, '' if B == 1 else B, n), '\\dfrac{%d\\sqrt{%d}}{%d}' % (c, n, n)]), ans=0,
                ee='Multiply by \\(\\sqrt{%d}-%d\\): the denominator becomes \\(%d-%d=%d\\).' % (n, k, n, k * k, d), ev='Nhân tử và mẫu với \\(\\sqrt{%d}-%d\\): mẫu trở thành \\(%d-%d=%d\\).' % (n, k, n, k * k, d))

def b9_d3_cmp(r, lv):
    while True:
        a, b, c, d = r.randint(2, 7), r.choice(SQF2[:6]), r.randint(2, 7), r.choice(SQF2[:6])
        if a * a * b != c * c * d and b != d: break
    s = '\\gt ' if a * a * b > c * c * d else '\\lt '; o = '\\lt ' if s == '\\gt ' else '\\gt '
    return dict(en='Compare \\(%s\\) and \\(%s\\) without a calculator.' % (rad(a, b), rad(c, d)), vi='So sánh \\(%s\\) và \\(%s\\) mà không dùng máy tính.' % (rad(a, b), rad(c, d)),
                opts=['%s%s%s' % (rad(a, b), s, rad(c, d)), '%s%s%s' % (rad(a, b), o, rad(c, d)), '%s=%s' % (rad(a, b), rad(c, d)), tx('cannot be compared', 'không so sánh được')], ans=0,
                ee='Take the factors into the root: \\(\\sqrt{%d}\\) and \\(\\sqrt{%d}\\).' % (a * a * b, c * c * d), ev='Đưa thừa số vào trong dấu căn: \\(\\sqrt{%d}\\) và \\(\\sqrt{%d}\\).' % (a * a * b, c * c * d))

def b9_d4_abs(r, lv):
    m = r.choice([2, 3, 5, 6, 7]); p, q = r.randint(2, 6), r.randint(2, 6); assert p != q
    E = '%d\\sqrt{%d}-\\sqrt{%d}+\\sqrt{(1-\\sqrt{%d})^2}' % (p, m, q * q * m, m); t = p - q + 1
    good = '%s-1' % (rad(t, m) if t else '0') if t else '-1'
    return dict(en='Simplify \\(A=%s\\).' % E, vi='Rút gọn \\(A=%s\\).' % E,
                opts=pick_opts(r, good, ['%s+1' % rad(p - q - 1, m) if p - q - 1 else '1', '%s+1' % rad(t, m) if t else '1', '%s-1' % rad(p - q - 1, m) if p - q - 1 else '-1']), ans=0,
                ee='\\(\\sqrt{%d}=%s\\); \\(1-\\sqrt{%d}\\lt0\\) so \\(\\sqrt{(1-\\sqrt{%d})^2}=\\sqrt{%d}-1\\).' % (q * q * m, rad(q, m), m, m, m),
                ev='\\(\\sqrt{%d}=%s\\); \\(1-\\sqrt{%d}\\lt0\\) nên \\(\\sqrt{(1-\\sqrt{%d})^2}=\\sqrt{%d}-1\\).' % (q * q * m, rad(q, m), m, m, m))

def b9_d4_rel(r, lv):
    fr_, k = r.choice([((3, 5), F(5, 4)), ((4, 5), F(5, 3)), ((5, 13), F(13, 12)), ((12, 13), F(13, 5))])
    m0 = (4 if k.denominator == 4 else 3 if k.denominator == 3 else 12 if k.denominator == 12 else 5) * r.randint(5, 20); m = m0 * k
    return dict(en='In relativity, a body with rest mass \\(m_0\\) moving at speed \\(v\\) has mass \\(m=\\dfrac{m_0}{\\sqrt{1-\\frac{v^2}{c^2}}}\\) (\\(c\\) is the speed of light). Find \\(m\\) when \\(m_0=%d\\) kg and \\(v=\\dfrac{%d}{%d}c\\).' % (m0, fr_[0], fr_[1]),
                vi='Theo thuyết tương đối, vật có khối lượng nghỉ \\(m_0\\) chuyển động với vận tốc \\(v\\) thì có khối lượng \\(m=\\dfrac{m_0}{\\sqrt{1-\\frac{v^2}{c^2}}}\\) (\\(c\\) là vận tốc ánh sáng). Tính \\(m\\) khi \\(m_0=%d\\) kg và \\(v=\\dfrac{%d}{%d}c\\).' % (m0, fr_[0], fr_[1]),
                opts=pick_opts(r, '%s\\text{ kg}' % fr(m), ['%s\\text{ kg}' % fr(o) for o in (m0 * F(fr_[1], fr_[0]), m0 * (1 - F(fr_[0] ** 2, fr_[1] ** 2)), m0 / k)]), ans=0,
                ee='\\(1-\\dfrac{v^2}{c^2}=1-\\dfrac{%d}{%d}=\\dfrac{%d}{%d}\\), whose square root is \\(%s\\); so \\(m=%d:%s=%s\\) kg.' % (fr_[0] ** 2, fr_[1] ** 2, fr_[1] ** 2 - fr_[0] ** 2, fr_[1] ** 2, fr(1 / k), m0, fr(1 / k), fr(m)),
                ev='\\(1-\\dfrac{v^2}{c^2}=1-\\dfrac{%d}{%d}=\\dfrac{%d}{%d}\\), căn bậc hai bằng \\(%s\\); nên \\(m=%d:%s=%s\\) kg.' % (fr_[0] ** 2, fr_[1] ** 2, fr_[1] ** 2 - fr_[0] ** 2, fr_[1] ** 2, fr(1 / k), m0, fr(1 / k), fr(m)))

def b9_d4_frac(r, lv):
    a = r.randint(2, 6); x = r.choice([t for t in range(1, 50) if t != a * a and int(t ** 0.5) ** 2 == t])
    val = F(2 * x, x - a * a); E = '\\sqrt{x}\\left(\\dfrac{1}{\\sqrt{x}+%d}-\\dfrac{1}{%d-\\sqrt{x}}\\right)' % (a, a)
    return dict(en='Given \\(A=%s\\) (\\(x\\ge0,\\ x\\ne%d\\)). Simplify \\(A\\), then find \\(A\\) at \\(x=%d\\).' % (E, a * a, x), vi='Cho \\(A=%s\\) (\\(x\\ge0,\\ x\\ne%d\\)). Rút gọn \\(A\\) rồi tính \\(A\\) tại \\(x=%d\\).' % (E, a * a, x),
                opts=pick_opts(r, fr(val), [fr(-val), fr(F(2 * x, x + a * a)), fr(F(x, x - a * a))]), ans=0,
                ee='\\(A=\\dfrac{2x}{x-%d}\\); at \\(x=%d\\): \\(A=%s\\).' % (a * a, x, fr(val)), ev='\\(A=\\dfrac{2x}{x-%d}\\); tại \\(x=%d\\): \\(A=%s\\).' % (a * a, x, fr(val)))

L9_GROUPS = [[('mcq', b9_out), ('mcq', b9_in), ('mcq', b9_ratc)], [('tf', b9_tf_cmp), ('tf', b9_tf_neg)], [('short', b9_short_comb), ('short', b9_short_conj)],
             [('mcq', b9_d1_abs), ('mcq', b9_d1_conj), ('mcq', b9_d1_write)], [('mcq', b9_d2_inneg), ('mcq', b9_d2_clear), ('mcq', b9_d2_like)],
             [('mcq', b9_d3_simpl), ('mcq', b9_d3_conj), ('mcq', b9_d3_cmp)], [('mcq', b9_d4_abs), ('mcq', b9_d4_rel), ('mcq', b9_d4_frac)]]

# =====================================================================================================
# BÀI 10. Căn bậc ba và căn thức bậc ba
# =====================================================================================================
def cube_frac(r):
    if r.random() < 0.65:
        s = F(nz(r, -12, 12)); return s ** 3, s
    p, q = nz(r, -5, 5), r.randint(2, 6); s = F(p, q); assert s.denominator == q
    return s ** 3, s

def b10_val(r, lv):
    c, s = cube_frac(r)
    return dict(en='Compute \\(\\sqrt[3]{%s}\\).' % fr(c), vi='Tính \\(\\sqrt[3]{%s}\\).' % fr(c), opts=pick_opts(r, fr(s), [fr(-s), '\\pm ' + fr(abs(s)), fr(c / 3) if c / 3 not in (s, -s) else fr(s * 2)]), ans=0,
                ee='\\((%s)^3=%s\\).' % (fr(s), fr(c)), ev='\\((%s)^3=%s\\).' % (fr(s), fr(c)))

def b10_eq(r, lv):
    s = nz(r, -10, 10); c = s ** 3
    return dict(en='Solve \\(x^3=%d\\).' % c, vi='Giải phương trình \\(x^3=%d\\).' % c, opts=pick_opts(r, 'x=%d' % s, ['x=%d' % (-s), 'x=\\pm %d' % abs(s), 'x=%s' % fr(F(c, 3))]), ans=0,
                ee='\\(x=\\sqrt[3]{%d}=%d\\).' % (c, s), ev='\\(x=\\sqrt[3]{%d}=%d\\).' % (c, s))

def b10_dom(r, lv):
    a, b = nz(r, -7, 7), r.randint(-9, 9); E = lin((a, 'x'), (b, '')) if b else lin((a, 'x'))
    o = [tx('for every real number \\(x\\)', 'với mọi số thực \\(x\\)'), tx('only for \\(%s\\ge0\\)' % E, 'chỉ khi \\(%s\\ge0\\)' % E), tx('only for \\(x\\ge0\\)', 'chỉ khi \\(x\\ge0\\)'), tx('only for \\(%s\\ne0\\)' % E, 'chỉ khi \\(%s\\ne0\\)' % E)]
    return dict(en='For which \\(x\\) is \\(\\sqrt[3]{%s}\\) defined?' % E, vi='\\(\\sqrt[3]{%s}\\) xác định khi nào?' % E, opts=o, ans=0,
                ee='A cube root is defined for every real number (also negative ones).', ev='Căn bậc ba xác định với mọi số thực (kể cả số âm).')

def b10_tf_neg(r, lv):
    n = r.randint(2, 12); truth = r.random() < 0.5; rhs = -n if truth else n
    return dict(en='\\(\\sqrt[3]{-%d}=%d\\).' % (n ** 3, rhs), vi='\\(\\sqrt[3]{-%d}=%d\\).' % (n ** 3, rhs), ans=truth, ee='\\((-%d)^3=-%d\\).' % (n, n ** 3), ev='\\((-%d)^3=-%d\\).' % (n, n ** 3))

def b10_tf_cube(r, lv):
    k = nz(r, -30, 30); truth = r.random() < 0.5; rhs = k if truth else k ** 3
    assert truth or rhs != k
    return dict(en='\\(\\left(\\sqrt[3]{%d}\\right)^3=%d\\).' % (k, rhs), vi='\\(\\left(\\sqrt[3]{%d}\\right)^3=%d\\).' % (k, rhs), ans=truth,
                ee='\\(\\left(\\sqrt[3]{a}\\right)^3=a\\) for every \\(a\\).', ev='\\(\\left(\\sqrt[3]{a}\\right)^3=a\\) với mọi \\(a\\).')

def b10_short_sum(r, lv):
    a, b = nz(r, -9, 9), nz(r, -9, 9); k = r.choice([1, 2, -1])
    E = '\\sqrt[3]{%d}%s\\sqrt[3]{%d}' % (a ** 3, '+' if k == 1 else '-' if k == -1 else '+2', b ** 3)
    return dict(en='Compute \\(%s\\).' % E, vi='Tính \\(%s\\).' % E, key=str(a + k * b), ee='\\(%d%s=%d\\).' % (a, mono(k * b, '', False), a + k * b), ev='\\(%d%s=%d\\).' % (a, mono(k * b, '', False), a + k * b))

def b10_short_calc(r, lv):
    while True:
        n = r.randint(2, 200)
        if round(n ** (1 / 3)) ** 3 != n: break
    v = n ** (1 / 3); key = '%.2f' % (math.floor(v * 100 + 0.5) / 100)
    return dict(en='Use a calculator to find \\(\\sqrt[3]{%d}\\), rounded to two decimal places.' % n, vi='Dùng máy tính cầm tay tính \\(\\sqrt[3]{%d}\\), làm tròn đến chữ số thập phân thứ hai.' % n,
                key=key, ee='\\(\\sqrt[3]{%d}\\approx %s\\).' % (n, key), ev='\\(\\sqrt[3]{%d}\\approx %s\\).' % (n, key.replace('.', '{,}')), hint=('Enter a decimal number (e.g. 2.29).', 'Nhập một số thập phân (ví dụ 2,29).'))

def b10_d1_count(r, lv):
    n = -r.randint(2, 99)
    o = [tx('exactly one', 'đúng một'), tx('none', 'không có'), tx('two (opposite numbers)', 'hai (là hai số đối nhau)'), tx('three', 'ba')]
    return dict(en='How many cube roots does the number \\(%d\\) have?' % n, vi='Số \\(%d\\) có bao nhiêu căn bậc ba?' % n, opts=o, ans=0, ee='Every real number has exactly one cube root.', ev='Mọi số thực đều có đúng một căn bậc ba.')

def b10_d1_index(r, lv):
    a = r.randint(2, 99)
    return dict(en='In \\(\\sqrt[3]{%d}\\), what is the index of the root?' % a, vi='Trong \\(\\sqrt[3]{%d}\\), chỉ số của căn là bao nhiêu?' % a, opts=['3', '2', str(a), '1'], ans=0,
                ee='The small number 3 is the index.', ev='Số 3 nhỏ phía trên là chỉ số của căn.')

def b10_d1_def(r, lv):
    s = nz(r, -15, 15)
    return dict(en='\\(\\sqrt[3]{(%d)^3}\\) is equal to…' % s, vi='\\(\\sqrt[3]{(%d)^3}\\) bằng…' % s, opts=pick_opts(r, str(s), [str(-s), str(abs(s)) if abs(s) != s else str(s * 3), str(s ** 3)]), ans=0,
                ee='\\(\\sqrt[3]{a^3}=a\\) for every \\(a\\).', ev='\\(\\sqrt[3]{a^3}=a\\) với mọi \\(a\\).')

def b10_d2_frac(r, lv):
    p, q = nz(r, -6, 6), r.randint(2, 7); s = F(p, q); assert s.denominator == q
    return dict(en='Compute \\(\\sqrt[3]{%s}\\).' % fr(s ** 3), vi='Tính \\(\\sqrt[3]{%s}\\).' % fr(s ** 3), opts=pick_opts(r, fr(s), [fr(-s), fr(F(p ** 3, q)), fr(F(p, q ** 3))]), ans=0,
                ee='\\(\\left(%s\\right)^3=%s\\).' % (fr(s), fr(s ** 3)), ev='\\(\\left(%s\\right)^3=%s\\).' % (fr(s), fr(s ** 3)))

def b10_d2_value(r, lv):
    a, b = nz(r, -5, 5), r.randint(-10, 10); s = nz(r, -5, 5); x = F(s ** 3 - b, a); assert x.denominator == 1
    E = lin((a, 'x'), (b, '')) if b else lin((a, 'x'))
    return dict(en='Find the value of \\(\\sqrt[3]{%s}\\) at \\(x=%s\\).' % (E, fr(x)), vi='Tính giá trị của \\(\\sqrt[3]{%s}\\) tại \\(x=%s\\).' % (E, fr(x)), opts=pick_opts(r, str(s), [str(-s), str(s ** 3), str(s + 1)]), ans=0,
                ee='The radicand equals \\(%d\\), and \\(\\sqrt[3]{%d}=%d\\).' % (s ** 3, s ** 3, s), ev='Biểu thức dưới dấu căn bằng \\(%d\\), và \\(\\sqrt[3]{%d}=%d\\).' % (s ** 3, s ** 3, s))

def b10_d2_cmp(r, lv):
    m = nz(r, -8, 8); n = m ** 3 + r.choice([-2, -1, 1, 2]); s = '\\gt ' if m ** 3 > n else '\\lt '; o = '\\lt ' if s == '\\gt ' else '\\gt '
    return dict(en='Compare \\(%d\\) and \\(\\sqrt[3]{%d}\\).' % (m, n), vi='So sánh \\(%d\\) và \\(\\sqrt[3]{%d}\\).' % (m, n),
                opts=['%d%s\\sqrt[3]{%d}' % (m, s, n), '%d%s\\sqrt[3]{%d}' % (m, o, n), '%d=\\sqrt[3]{%d}' % (m, n), tx('cannot be compared', 'không so sánh được')], ans=0,
                ee='\\(%d=\\sqrt[3]{%d}\\) and \\(%d%s%d\\).' % (m, m ** 3, m ** 3, s, n), ev='\\(%d=\\sqrt[3]{%d}\\) và \\(%d%s%d\\).' % (m, m ** 3, m ** 3, s, n))

def b10_d3_eq(r, lv):
    p, q = r.randint(-9, 9), nz(r, -5, 5)
    return dict(en='Solve \\(\\sqrt[3]{x%s}=%d\\).' % (mono(p, '', False) if p else '', q), vi='Giải phương trình \\(\\sqrt[3]{x%s}=%d\\).' % (mono(p, '', False) if p else '', q),
                opts=pick_opts(r, 'x=%d' % (q ** 3 - p), ['x=%d' % (q ** 3 + p), 'x=%d' % (q - p), 'x=%d' % (3 * q - p)]), ans=0,
                ee='Cube both sides: \\(x%s=%d\\Rightarrow x=%d\\).' % (mono(p, '', False) if p else '', q ** 3, q ** 3 - p), ev='Lập phương hai vế: \\(x%s=%d\\Rightarrow x=%d\\).' % (mono(p, '', False) if p else '', q ** 3, q ** 3 - p))

def b10_d3_edge(r, lv):
    a = r.randint(2, 15); V = a ** 3
    return dict(en='A cube has a volume of %d cm³. Find the length of its edge.' % V, vi='Một hình lập phương có thể tích %d cm³. Tính độ dài cạnh của nó.' % V,
                opts=pick_opts(r, '%d\\text{ cm}' % a, ['%d\\text{ cm}' % o for o in (V // 3, a * a, a + 1)]), ans=0, ee='\\(a=\\sqrt[3]{%d}=%d\\) cm.' % (V, a), ev='\\(a=\\sqrt[3]{%d}=%d\\) cm.' % (V, a))

def b10_d3_mix(r, lv):
    p, q = nz(r, -20, 20), nz(r, -6, 6)
    return dict(en='Compute \\(\\left(\\sqrt[3]{%d}\\right)^3+\\sqrt[3]{%d}\\).' % (p, q ** 3), vi='Tính \\(\\left(\\sqrt[3]{%d}\\right)^3+\\sqrt[3]{%d}\\).' % (p, q ** 3),
                opts=pick_opts(r, str(p + q), [str(p + q ** 3), str(p - q), str(p * q)]), ans=0, ee='\\(%d+(%d)=%d\\).' % (p, q, p + q), ev='\\(%d+(%d)=%d\\).' % (p, q, p + q))

def b10_d4_grow(r, lv):
    a, b = r.sample(range(2, 12), 2); a, b = min(a, b), max(a, b)
    return dict(en='A cubic tank is replaced by a bigger cubic tank. The volume increases from %d dm³ to %d dm³. By how many decimeters does the edge increase?' % (a ** 3, b ** 3),
                vi='Một bể hình lập phương được thay bằng bể hình lập phương lớn hơn. Thể tích tăng từ %d dm³ lên %d dm³. Cạnh bể tăng thêm bao nhiêu đề-xi-mét?' % (a ** 3, b ** 3),
                opts=pick_opts(r, str(b - a), [str(b ** 3 - a ** 3), str(b), str(b * b - a * a)]), ans=0, ee='\\(\\sqrt[3]{%d}-\\sqrt[3]{%d}=%d-%d=%d\\).' % (b ** 3, a ** 3, b, a, b - a), ev='\\(\\sqrt[3]{%d}-\\sqrt[3]{%d}=%d-%d=%d\\).' % (b ** 3, a ** 3, b, a, b - a))

def b10_d4_eq2(r, lv):
    k, s = r.choice([2, 3, 4, 5]), nz(r, -5, 5); m = r.randint(-20, 20); c = k * s ** 3 + m
    return dict(en='Solve \\(%dx^3%s=%d\\).' % (k, mono(m, '', False) if m else '', c), vi='Giải phương trình \\(%dx^3%s=%d\\).' % (k, mono(m, '', False) if m else '', c),
                opts=pick_opts(r, 'x=%d' % s, ['x=%d' % (-s), 'x=%d' % (s ** 3), 'x=%s' % fr(F(c - m, 3 * k))]), ans=0,
                ee='\\(x^3=%d\\Rightarrow x=%d\\).' % (s ** 3, s), ev='\\(x^3=%d\\Rightarrow x=%d\\).' % (s ** 3, s))

def b10_d4_box(r, lv):
    a = r.choice([2, 3, 4, 5, 6, 8, 10]); L = a ** 3
    return dict(en='A cube-shaped box holds exactly %d liters of water (1 liter = 1 dm³). What is the length of its edge in centimeters?' % L, vi='Một chiếc hộp hình lập phương chứa vừa đầy %d lít nước (1 lít = 1 dm³). Cạnh hộp dài bao nhiêu xăng-ti-mét?' % L,
                opts=pick_opts(r, '%d\\text{ cm}' % (10 * a), ['%d\\text{ cm}' % o for o in (a, 100 * a, 10 * L // 3 if 10 * L // 3 != 10 * a else L)]), ans=0,
                ee='Edge \\(=\\sqrt[3]{%d}=%d\\) dm \\(=%d\\) cm.' % (L, a, 10 * a), ev='Cạnh \\(=\\sqrt[3]{%d}=%d\\) dm \\(=%d\\) cm.' % (L, a, 10 * a))

L10_GROUPS = [[('mcq', b10_val), ('mcq', b10_eq), ('mcq', b10_dom)], [('tf', b10_tf_neg), ('tf', b10_tf_cube)], [('short', b10_short_sum), ('short', b10_short_calc)],
              [('mcq', b10_d1_count), ('mcq', b10_d1_index), ('mcq', b10_d1_def)], [('mcq', b10_d2_frac), ('mcq', b10_d2_value), ('mcq', b10_d2_cmp)],
              [('mcq', b10_d3_eq), ('mcq', b10_d3_edge), ('mcq', b10_d3_mix)], [('mcq', b10_d4_grow), ('mcq', b10_d4_eq2), ('mcq', b10_d4_box)]]

# =====================================================================================================
# BÀI 11. Tỉ số lượng giác của góc nhọn
# =====================================================================================================
TRIPLES = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (9, 40, 41)]
def _tri(r):
    a, b, c = r.choice(TRIPLES); k = r.choice([1, 1, 2, 3]); AB, AC = (a * k, b * k) if r.random() < 0.5 else (b * k, a * k)
    return AB, AC, c * k          # tam giác ABC vuông tại A: AB, AC cạnh góc vuông, BC cạnh huyền

RAT = {'sin': lambda AB, AC, BC: F(AC, BC), 'cos': lambda AB, AC, BC: F(AB, BC), 'tan': lambda AB, AC, BC: F(AC, AB), 'cot': lambda AB, AC, BC: F(AB, AC)}
RATEN = {'sin': ('opposite / hypotenuse', 'cạnh đối / cạnh huyền'), 'cos': ('adjacent / hypotenuse', 'cạnh kề / cạnh huyền'), 'tan': ('opposite / adjacent', 'cạnh đối / cạnh kề'), 'cot': ('adjacent / opposite', 'cạnh kề / cạnh đối')}

def b11_ratio(r, lv):
    AB, AC, BC = _tri(r); f = r.choice(list(RAT)); v = RAT[f](AB, AC, BC)
    others = [RAT[g](AB, AC, BC) for g in RAT if g != f]
    return dict(en='Triangle \\(ABC\\) is right-angled at \\(A\\) with \\(AB=%d\\), \\(AC=%d\\), \\(BC=%d\\). Find \\(\\%s B\\).' % (AB, AC, BC, f), vi='Tam giác \\(ABC\\) vuông tại \\(A\\) có \\(AB=%d\\), \\(AC=%d\\), \\(BC=%d\\). Tính \\(\\%s B\\).' % (AB, AC, BC, f),
                opts=pick_opts(r, fr(v), [fr(o) for o in others if o != v], fill=lambda t: fr(v + t)), ans=0,
                ee='For angle \\(B\\): opposite side \\(AC\\), adjacent side \\(AB\\), hypotenuse \\(BC\\). \\(\\%s B=\\) %s \\(=%s\\).' % (f, RATEN[f][0], fr(v)),
                ev='Với góc \\(B\\): cạnh đối \\(AC\\), cạnh kề \\(AB\\), cạnh huyền \\(BC\\). \\(\\%s B=\\) %s \\(=%s\\).' % (f, RATEN[f][1], fr(v)))

SPECIAL = {('sin', 30): '\\dfrac{1}{2}', ('sin', 45): '\\dfrac{\\sqrt{2}}{2}', ('sin', 60): '\\dfrac{\\sqrt{3}}{2}', ('cos', 30): '\\dfrac{\\sqrt{3}}{2}', ('cos', 45): '\\dfrac{\\sqrt{2}}{2}', ('cos', 60): '\\dfrac{1}{2}',
           ('tan', 30): '\\dfrac{\\sqrt{3}}{3}', ('tan', 45): '1', ('tan', 60): '\\sqrt{3}', ('cot', 30): '\\sqrt{3}', ('cot', 45): '1', ('cot', 60): '\\dfrac{\\sqrt{3}}{3}'}
SPVAL = {'\\dfrac{1}{2}': 0.5, '\\dfrac{\\sqrt{2}}{2}': 2 ** 0.5 / 2, '\\dfrac{\\sqrt{3}}{2}': 3 ** 0.5 / 2, '\\dfrac{\\sqrt{3}}{3}': 3 ** 0.5 / 3, '1': 1.0, '\\sqrt{3}': 3 ** 0.5}
def _trig(f, a):
    x = math.radians(a); return {'sin': math.sin(x), 'cos': math.cos(x), 'tan': math.tan(x), 'cot': 1 / math.tan(x)}[f]

def b11_special(r, lv):
    f, a = r.choice(list(SPECIAL)); good = SPECIAL[(f, a)]; assert abs(SPVAL[good] - _trig(f, a)) < 1e-12
    bads = [v for v in SPVAL if v != good]; r.shuffle(bads)
    return dict(en='What is the exact value of \\(\\%s %d^\\circ\\)?' % (f, a), vi='Giá trị đúng của \\(\\%s %d^\\circ\\) là bao nhiêu?' % (f, a), opts=[good] + bads[:3], ans=0,
                ee='From the table of special angles: \\(\\%s %d^\\circ=%s\\).' % (f, a, good), ev='Theo bảng giá trị lượng giác của các góc đặc biệt: \\(\\%s %d^\\circ=%s\\).' % (f, a, good))

def b11_comp(r, lv):
    a = r.randint(5, 85); assert a != 45; f = r.choice(['sin', 'cos', 'tan', 'cot']); g = {'sin': 'cos', 'cos': 'sin', 'tan': 'cot', 'cot': 'tan'}[f]
    return dict(en='Which value is equal to \\(\\%s %d^\\circ\\)?' % (f, a), vi='Giá trị nào bằng \\(\\%s %d^\\circ\\)?' % (f, a),
                opts=['\\%s %d^\\circ' % (g, 90 - a), '\\%s %d^\\circ' % (g, a), '\\%s %d^\\circ' % (f, 90 - a), '\\%s %d^\\circ' % (g, 180 - a)], ans=0,
                ee='\\(%d^\\circ\\) and \\(%d^\\circ\\) are complementary angles, so \\(\\%s %d^\\circ=\\%s %d^\\circ\\).' % (a, 90 - a, f, a, g, 90 - a), ev='\\(%d^\\circ\\) và \\(%d^\\circ\\) là hai góc phụ nhau nên \\(\\%s %d^\\circ=\\%s %d^\\circ\\).' % (a, 90 - a, f, a, g, 90 - a))

def b11_tf_def(r, lv):
    f = r.choice(list(RAT)); V = r.choice(['B', 'C']); truth = r.random() < 0.5
    # góc B: đối AC, kề AB; góc C: đối AB, kề AC
    opp, adj = ('AC', 'AB') if V == 'B' else ('AB', 'AC')
    cor = {'sin': (opp, 'BC'), 'cos': (adj, 'BC'), 'tan': (opp, adj), 'cot': (adj, opp)}[f]
    wrong = {'sin': (adj, 'BC'), 'cos': (opp, 'BC'), 'tan': (adj, opp), 'cot': (opp, adj)}[f]
    num, den = cor if truth else wrong; nm = r.choice(['ABC', 'ABC'])
    return dict(en='Triangle \\(ABC\\) is right-angled at \\(A\\). Then \\(\\%s %s=\\dfrac{%s}{%s}\\).' % (f, V, num, den), vi='Tam giác \\(ABC\\) vuông tại \\(A\\). Khi đó \\(\\%s %s=\\dfrac{%s}{%s}\\).' % (f, V, num, den), ans=truth,
                ee='For angle \\(%s\\), the opposite side is \\(%s\\) and the adjacent side is \\(%s\\): \\(\\%s %s=\\dfrac{%s}{%s}\\).' % (V, opp, adj, f, V, cor[0], cor[1]), ev='Với góc \\(%s\\), cạnh đối là \\(%s\\), cạnh kề là \\(%s\\): \\(\\%s %s=\\dfrac{%s}{%s}\\).' % (V, opp, adj, f, V, cor[0], cor[1]))

def b11_tf_comp(r, lv):
    a = r.randint(10, 80); truth = r.random() < 0.5; b = 90 - a if truth else 90 - a + r.choice([-10, -5, 5, 10])
    return dict(en='\\(\\sin %d^\\circ=\\cos %d^\\circ\\).' % (a, b), vi='\\(\\sin %d^\\circ=\\cos %d^\\circ\\).' % (a, b), ans=truth,
                ee='\\(\\sin\\alpha=\\cos(90^\\circ-\\alpha)\\); here \\(90^\\circ-%d^\\circ=%d^\\circ\\).' % (a, 90 - a), ev='\\(\\sin\\alpha=\\cos(90^\\circ-\\alpha)\\); ở đây \\(90^\\circ-%d^\\circ=%d^\\circ\\).' % (a, 90 - a))

def b11_short_calc(r, lv):
    f, a = r.choice(['sin', 'cos', 'tan']), r.randint(5, 85); v = _trig(f, a); key = '%.3f' % v
    assert abs(float(key) - v) <= 0.0005
    return dict(en='Use a calculator to find \\(\\%s %d^\\circ\\), rounded to three decimal places.' % (f, a), vi='Dùng máy tính cầm tay tính \\(\\%s %d^\\circ\\), làm tròn đến chữ số thập phân thứ ba.' % (f, a),
                key=key, ee='\\(\\%s %d^\\circ\\approx %s\\) (calculator in degree mode).' % (f, a, key), ev='\\(\\%s %d^\\circ\\approx %s\\) (máy tính để ở chế độ độ).' % (f, a, key.replace('.', '{,}')), hint=('Enter a decimal number (e.g. 0.454).', 'Nhập một số thập phân (ví dụ 0,454).'))

def b11_short_side(r, lv):
    AB, AC, BC = _tri(r); f = r.choice(['sin', 'cos'])
    v = RAT[f](AB, AC, BC); want, val = ('AC', AC) if f == 'sin' else ('AB', AB)
    return dict(en='Triangle \\(ABC\\) is right-angled at \\(A\\), \\(BC=%d\\) cm and \\(\\%s B=%s\\). Find \\(%s\\) (cm).' % (BC, f, fr(v), want), vi='Tam giác \\(ABC\\) vuông tại \\(A\\), \\(BC=%d\\) cm và \\(\\%s B=%s\\). Tính \\(%s\\) (cm).' % (BC, f, fr(v), want),
                key=str(val), ee='\\(%s=BC\\cdot\\%s B=%d\\cdot%s=%d\\) cm.' % (want, f, BC, fr(v), val), ev='\\(%s=BC\\cdot\\%s B=%d\\cdot%s=%d\\) cm.' % (want, f, BC, fr(v), val))

def b11_d1_side(r, lv):
    V = r.choice(['B', 'C']); kind = r.choice(['opposite', 'adjacent']); P_, Q_ = r.choice([('M', 'N'), ('D', 'E'), ('A', 'B')]) if False else ('', '')
    opp, adj = ('AC', 'AB') if V == 'B' else ('AB', 'AC'); good = opp if kind == 'opposite' else adj
    return dict(en='Triangle \\(ABC\\) is right-angled at \\(A\\). Which side is %s to angle \\(%s\\)?' % (kind, V), vi='Tam giác \\(ABC\\) vuông tại \\(A\\). Cạnh nào là cạnh %s của góc \\(%s\\)?' % ('đối' if kind == 'opposite' else 'kề', V),
                opts=[good, adj if good == opp else opp, 'BC', tx('none of these', 'không có cạnh nào')], ans=0,
                ee='The hypotenuse is \\(BC\\); for angle \\(%s\\) the opposite side is \\(%s\\) and the adjacent side is \\(%s\\).' % (V, opp, adj), ev='Cạnh huyền là \\(BC\\); với góc \\(%s\\), cạnh đối là \\(%s\\), cạnh kề là \\(%s\\).' % (V, opp, adj))

def b11_d1_defn(r, lv):
    f = r.choice(list(RAT)); al = r.choice(['\\alpha', '\\beta', 'B', 'C', 'x'])
    order = [f] + [g for g in RAT if g != f]
    return dict(en='\\(\\%s %s\\) of an acute angle \\(%s\\) in a right triangle is the ratio…' % (f, al, al), vi='\\(\\%s %s\\) của góc nhọn \\(%s\\) trong tam giác vuông là tỉ số…' % (f, al, al),
                opts=[tx(RATEN[g][0], RATEN[g][1]) for g in order], ans=0, ee='\\(\\%s\\) = %s.' % (f, RATEN[f][0]), ev='\\(\\%s\\) = %s.' % (f, RATEN[f][1]))

def b11_d1_tan45(r, lv):
    f, a = r.choice([k for k in SPECIAL if SPECIAL[k] in ('1', '\\dfrac{1}{2}')]); good = SPECIAL[(f, a)]
    return dict(en='\\(\\%s %d^\\circ\\) is equal to…' % (f, a), vi='\\(\\%s %d^\\circ\\) bằng…' % (f, a), opts=[good] + [v for v in ('\\dfrac{1}{2}', '1', '\\dfrac{\\sqrt{3}}{2}', '\\dfrac{\\sqrt{2}}{2}') if v != good][:3], ans=0,
                ee='Table of special angles.', ev='Bảng giá trị lượng giác của các góc đặc biệt.')

def b11_d2_cos(r, lv):
    q = b11_ratio(r, lv); q['en'] = q['en'].replace('Find', 'Calculate'); q['vi'] = q['vi'].replace('Tính', 'Hãy tính'); return q

def b11_d2_prod(r, lv):
    a = r.randint(5, 85)
    return dict(en='Compute \\(\\tan %d^\\circ\\cdot\\cot %d^\\circ\\).' % (a, a), vi='Tính \\(\\tan %d^\\circ\\cdot\\cot %d^\\circ\\).' % (a, a), opts=['1', '0', str(a), '\\tan^2 %d^\\circ' % a], ans=0,
                ee='\\(\\tan\\alpha\\cdot\\cot\\alpha=\\dfrac{\\text{opp}}{\\text{adj}}\\cdot\\dfrac{\\text{adj}}{\\text{opp}}=1\\).', ev='\\(\\tan\\alpha\\cdot\\cot\\alpha=1\\) (hai tỉ số nghịch đảo nhau).')

def b11_d2_cofn(r, lv):
    a = r.randint(10, 80); p, q = r.randint(1, 7), r.randint(8, 15)
    return dict(en='Given \\(\\sin %d^\\circ\\approx %s\\). What is \\(\\cos %d^\\circ\\)?' % (a, '%.4f' % math.sin(math.radians(a)), 90 - a), vi='Cho \\(\\sin %d^\\circ\\approx %s\\). Giá trị của \\(\\cos %d^\\circ\\) là bao nhiêu?' % (a, ('%.4f' % math.sin(math.radians(a))).replace('.', '{,}'), 90 - a),
                opts=[tx('the same value, about %s' % ('%.4f' % math.sin(math.radians(a))), 'bằng đúng giá trị đó, khoảng %s' % ('%.4f' % math.sin(math.radians(a))).replace('.', ',')), tx('\\(1-\\sin %d^\\circ\\)' % a, '\\(1-\\sin %d^\\circ\\)' % a),
                      tx('\\(\\dfrac{1}{\\sin %d^\\circ}\\)' % a, '\\(\\dfrac{1}{\\sin %d^\\circ}\\)' % a), tx('it cannot be found', 'không tính được')], ans=0,
                ee='\\(%d^\\circ\\) and \\(%d^\\circ\\) are complementary: \\(\\cos %d^\\circ=\\sin %d^\\circ\\).' % (a, 90 - a, 90 - a, a), ev='\\(%d^\\circ\\) và \\(%d^\\circ\\) phụ nhau: \\(\\cos %d^\\circ=\\sin %d^\\circ\\).' % (a, 90 - a, 90 - a, a))

def b11_d3_angle(r, lv):
    AB, AC, BC = _tri(r); B = math.degrees(math.atan2(AC, AB)); n = round(B)
    assert abs(B - n) < 0.45
    return dict(en='Triangle \\(ABC\\) is right-angled at \\(A\\) with \\(AB=%d\\) and \\(AC=%d\\). Find angle \\(B\\), rounded to the nearest degree.' % (AB, AC), vi='Tam giác \\(ABC\\) vuông tại \\(A\\) có \\(AB=%d\\), \\(AC=%d\\). Tính góc \\(B\\) (làm tròn đến độ).' % (AB, AC),
                opts=pick_opts(r, '%d^\\circ' % n, ['%d^\\circ' % (90 - n) if 90 - n != n else '%d^\\circ' % (n + 5), '%d^\\circ' % (n + 1), '%d^\\circ' % (n - 1)]), ans=0,
                ee='\\(\\tan B=\\dfrac{AC}{AB}=%s\\Rightarrow B\\approx %d^\\circ\\).' % (fr(F(AC, AB)), n), ev='\\(\\tan B=\\dfrac{AC}{AB}=%s\\Rightarrow B\\approx %d^\\circ\\).' % (fr(F(AC, AB)), n))

def b11_d3_spec(r, lv):
    k = r.randint(2, 12); B = r.choice([30, 60])
    AB = 'k' if False else None
    # BC = 2k; B = 60° => AB = BC cos60 = k, AC = k√3 ; B = 30° => AB = k√3, AC = k
    want = r.choice(['AB', 'AC']); val = {('AB', 60): str(k), ('AC', 60): '%d\\sqrt{3}' % k, ('AB', 30): '%d\\sqrt{3}' % k, ('AC', 30): str(k)}[(want, B)]
    other = {('AB', 60): '%d\\sqrt{3}' % k, ('AC', 60): str(k), ('AB', 30): str(k), ('AC', 30): '%d\\sqrt{3}' % k}[(want, B)]
    return dict(en='Triangle \\(ABC\\) is right-angled at \\(A\\), \\(BC=%d\\) cm and \\(\\widehat{B}=%d^\\circ\\). Find \\(%s\\).' % (2 * k, B, want), vi='Tam giác \\(ABC\\) vuông tại \\(A\\), \\(BC=%d\\) cm và \\(\\widehat{B}=%d^\\circ\\). Tính \\(%s\\).' % (2 * k, B, want),
                opts=['%s\\text{ cm}' % val, '%s\\text{ cm}' % other, '%d\\text{ cm}' % (2 * k), '%d\\sqrt{2}\\text{ cm}' % k], ans=0,
                ee='\\(%s=BC\\cdot\\%s %d^\\circ\\).' % (want, 'cos' if want == 'AB' else 'sin', B), ev='\\(%s=BC\\cdot\\%s %d^\\circ\\).' % (want, 'cos' if want == 'AB' else 'sin', B))

def b11_d3_expr(r, lv):
    c = r.choice([(30, 'sin', 'cos', '1'), (45, 'sin', 'cos', '1'), (60, 'sin', 'cos', '1')])
    a = c[0]; k = r.randint(2, 5)
    v = k * (math.sin(math.radians(a)) ** 2 + math.cos(math.radians(a)) ** 2); assert abs(v - k) < 1e-12
    return dict(en='Compute \\(%d\\left(\\sin^2 %d^\\circ+\\cos^2 %d^\\circ\\right)\\).' % (k, a, a), vi='Tính \\(%d\\left(\\sin^2 %d^\\circ+\\cos^2 %d^\\circ\\right)\\).' % (k, a, a),
                opts=[str(k), str(2 * k), '%d^2' % k, '0'], ans=0, ee='\\(\\sin^2 %d^\\circ+\\cos^2 %d^\\circ=1\\).' % (a, a), ev='\\(\\sin^2 %d^\\circ+\\cos^2 %d^\\circ=1\\).' % (a, a))

def b11_d4_tan(r, lv):
    a, b, c = r.choice(TRIPLES); f = r.choice(['tan', 'cot', 'cos'])
    v = {'tan': F(a, b), 'cot': F(b, a), 'cos': F(b, c)}[f]
    return dict(en='Given an acute angle \\(\\alpha\\) with \\(\\sin\\alpha=%s\\). Find \\(\\%s\\alpha\\).' % (fr(F(a, c)), f), vi='Cho góc nhọn \\(\\alpha\\) có \\(\\sin\\alpha=%s\\). Tính \\(\\%s\\alpha\\).' % (fr(F(a, c)), f),
                opts=pick_opts(r, fr(v), [fr(o) for o in (F(a, b), F(b, a), F(b, c), F(c, b)) if o != v]), ans=0,
                ee='Draw a right triangle with opposite side %d and hypotenuse %d; the adjacent side is \\(\\sqrt{%d^2-%d^2}=%d\\).' % (a, c, c, a, b), ev='Vẽ tam giác vuông có cạnh đối %d, cạnh huyền %d; cạnh kề bằng \\(\\sqrt{%d^2-%d^2}=%d\\).' % (a, c, c, a, b))

def b11_d4_ladder(r, lv):
    L = r.choice([4, 6, 8, 10]); ang = r.choice([30, 45, 60])
    h = {30: '%d' % (L // 2), 45: '%d\\sqrt{2}' % (L // 2) if L // 2 != 1 else '\\sqrt{2}', 60: '%d\\sqrt{3}' % (L // 2) if L // 2 != 1 else '\\sqrt{3}'}[ang]
    bad = [{30: '%d\\sqrt{3}' % (L // 2), 45: '%d' % (L // 2), 60: '%d' % (L // 2)}[ang], str(L), '%d\\sqrt{2}' % L]
    return dict(en='A ladder %d m long leans against a wall and makes an angle of \\(%d^\\circ\\) with the horizontal ground. How high up the wall does it reach?' % (L, ang), vi='Một chiếc thang dài %d m dựa vào tường, tạo với mặt đất nằm ngang một góc \\(%d^\\circ\\). Đầu thang chạm tường ở độ cao bao nhiêu?' % (L, ang),
                opts=pick_opts(r, '%s\\text{ m}' % h, ['%s\\text{ m}' % b for b in bad]), ans=0, ee='Height \\(=%d\\cdot\\sin %d^\\circ\\).' % (L, ang), ev='Độ cao \\(=%d\\cdot\\sin %d^\\circ\\).' % (L, ang))

def b11_d4_cmp(r, lv):
    a = r.randint(5, 85); assert a != 45
    s = '\\lt ' if a < 45 else '\\gt '; o = '\\gt ' if s == '\\lt ' else '\\lt '
    return dict(en='Compare \\(\\sin %d^\\circ\\) and \\(\\cos %d^\\circ\\) without a calculator.' % (a, a), vi='So sánh \\(\\sin %d^\\circ\\) và \\(\\cos %d^\\circ\\) mà không dùng máy tính.' % (a, a),
                opts=['\\sin %d^\\circ%s\\cos %d^\\circ' % (a, s, a), '\\sin %d^\\circ%s\\cos %d^\\circ' % (a, o, a), '\\sin %d^\\circ=\\cos %d^\\circ' % (a, a), tx('cannot be compared', 'không so sánh được')], ans=0,
                ee='\\(\\cos %d^\\circ=\\sin %d^\\circ\\), and the sine of an acute angle increases with the angle.' % (a, 90 - a), ev='\\(\\cos %d^\\circ=\\sin %d^\\circ\\); góc nhọn càng lớn thì sin càng lớn.' % (a, 90 - a))

L11_GROUPS = [[('mcq', b11_ratio), ('mcq', b11_special), ('mcq', b11_comp)], [('tf', b11_tf_def), ('tf', b11_tf_comp)], [('short', b11_short_calc), ('short', b11_short_side)],
              [('mcq', b11_d1_side), ('mcq', b11_d1_defn), ('mcq', b11_d1_tan45)], [('mcq', b11_d2_cos), ('mcq', b11_d2_prod), ('mcq', b11_d2_cofn)],
              [('mcq', b11_d3_angle), ('mcq', b11_d3_spec), ('mcq', b11_d3_expr)], [('mcq', b11_d4_tan), ('mcq', b11_d4_ladder), ('mcq', b11_d4_cmp)]]

# =====================================================================================================
# BÀI 12. Một số hệ thức giữa cạnh, góc trong tam giác vuông và ứng dụng
# =====================================================================================================
def _r1(v):
    """Làm tròn đến hàng phần mười; tránh giá trị sát ranh giới làm tròn (…,x5)."""
    f = v * 10 - math.floor(v * 10); assert abs(f - 0.5) > 0.03
    return '%.1f' % (math.floor(v * 10 + 0.5) / 10)

def dopt(s, unit=''):
    """Phương án số thập phân: dấu chấm (EN) / dấu phẩy (VI)."""
    u = '\\text{ %s}' % unit if unit else ''
    return tx('\\(%s%s\\)' % (s, u), '\\(%s%s\\)' % (s.replace('.', '{,}'), u))

def dm(s): return s.replace('.', '{,}')
HINT_D1 = ('Enter a decimal number (e.g. 7.7).', 'Nhập một số thập phân (ví dụ 7,7).')
TRI_NAMES = [('A', 'B', 'C'), ('D', 'E', 'F'), ('M', 'N', 'P'), ('H', 'I', 'K')]   # đỉnh góc vuông, hai đỉnh còn lại
def _ang(r): return r.choice([x for x in range(20, 71) if x != 45])
def _dec_opts(r, good, bads, unit):
    seen = [good]
    for b in bads:
        if b not in seen and float(b) > 0: seen.append(b)
    k = 1
    while len(seen) < 4:
        c = '%.1f' % (float(good) + k * 0.7); k += 1
        if c not in seen: seen.append(c)
    return [dopt(s, unit) for s in seen[:4]]

def b12_leg_sin(r, lv):
    a, B = r.randint(6, 30), _ang(r); s = math.sin(math.radians(B)); c = math.cos(math.radians(B))
    good = _r1(a * s); bads = []
    for v in (a * c, a * math.tan(math.radians(B)), a / s):
        try: bads.append(_r1(v))
        except AssertionError: bads.append('%.1f' % v)
    return dict(en='Triangle \\(ABC\\) is right-angled at \\(A\\), \\(BC=%d\\) cm and \\(\\widehat{B}=%d^\\circ\\). Find \\(AC\\), rounded to the nearest tenth of a centimeter.' % (a, B),
                vi='Tam giác \\(ABC\\) vuông tại \\(A\\), \\(BC=%d\\) cm và \\(\\widehat{B}=%d^\\circ\\). Tính \\(AC\\) (làm tròn đến hàng phần mười của xăng-ti-mét).' % (a, B),
                opts=_dec_opts(r, good, bads, 'cm'), ans=0,
                ee='\\(AC\\) is opposite angle \\(B\\): \\(AC=BC\\cdot\\sin B=%d\\cdot\\sin %d^\\circ\\approx %s\\) cm.' % (a, B, good),
                ev='\\(AC\\) là cạnh đối của góc \\(B\\): \\(AC=BC\\cdot\\sin B=%d\\cdot\\sin %d^\\circ\\approx %s\\) cm.' % (a, B, dm(good)))

def b12_leg_tan(r, lv):
    c, B = r.randint(4, 25), _ang(r); t = math.tan(math.radians(B))
    good = _r1(c * t); bads = []
    for v in (c / t, c * math.sin(math.radians(B)), c * math.cos(math.radians(B))):
        try: bads.append(_r1(v))
        except AssertionError: bads.append('%.1f' % v)
    return dict(en='Triangle \\(ABC\\) is right-angled at \\(A\\), \\(AB=%d\\) m and \\(\\widehat{B}=%d^\\circ\\). Find \\(AC\\), rounded to the nearest tenth of a meter.' % (c, B),
                vi='Tam giác \\(ABC\\) vuông tại \\(A\\), \\(AB=%d\\) m và \\(\\widehat{B}=%d^\\circ\\). Tính \\(AC\\) (làm tròn đến hàng phần mười của mét).' % (c, B),
                opts=_dec_opts(r, good, bads, 'm'), ans=0,
                ee='\\(AC\\) is opposite and \\(AB\\) is adjacent to angle \\(B\\): \\(AC=AB\\cdot\\tan B=%d\\cdot\\tan %d^\\circ\\approx %s\\) m.' % (c, B, good),
                ev='\\(AC\\) là cạnh đối, \\(AB\\) là cạnh kề của góc \\(B\\): \\(AC=AB\\cdot\\tan B=%d\\cdot\\tan %d^\\circ\\approx %s\\) m.' % (c, B, dm(good)))

def _rels(R, X, Y):
    """Tam giác vuông tại R; hai đỉnh nhọn X, Y; cạnh huyền XY. Trả về (hệ thức đúng, hệ thức sai)."""
    h = X + Y; lx = R + Y; ly = R + X   # lx: cạnh đối góc X; ly: cạnh đối góc Y
    good = ['%s=%s\\cdot\\sin %s' % (lx, h, X), '%s=%s\\cdot\\cos %s' % (lx, h, Y), '%s=%s\\cdot\\tan %s' % (lx, ly, X), '%s=%s\\cdot\\cot %s' % (lx, ly, Y),
            '%s=%s\\cdot\\sin %s' % (ly, h, Y), '%s=%s\\cdot\\cos %s' % (ly, h, X), '%s=%s\\cdot\\tan %s' % (ly, lx, Y), '%s=%s\\cdot\\cot %s' % (ly, lx, X)]
    bad = ['%s=%s\\cdot\\cos %s' % (lx, h, X), '%s=%s\\cdot\\sin %s' % (lx, h, Y), '%s=%s\\cdot\\cot %s' % (lx, ly, X), '%s=%s\\cdot\\tan %s' % (lx, ly, Y),
           '%s=%s\\cdot\\cos %s' % (ly, h, Y), '%s=%s\\cdot\\sin %s' % (ly, h, X), '%s=%s\\cdot\\cot %s' % (ly, lx, Y), '%s=%s\\cdot\\tan %s' % (ly, lx, X),
           '%s=%s\\cdot\\sin %s' % (h, lx, X), '%s=%s\\cdot\\tan %s' % (h, ly, X)]
    return good, bad

def b12_formula(r, lv):
    R, X, Y = r.choice(TRI_NAMES); g, b = _rels(R, X, Y); good = r.choice(g); bad = r.sample(b, 3)
    return dict(en='Triangle \\(%s%s%s\\) is right-angled at \\(%s\\). Which relation is correct?' % (R, X, Y, R), vi='Tam giác \\(%s%s%s\\) vuông tại \\(%s\\). Hệ thức nào đúng?' % (R, X, Y, R),
                opts=[good] + bad, ans=0,
                ee='Each leg = hypotenuse × sine of the opposite angle = hypotenuse × cosine of the adjacent angle = other leg × tangent of the opposite angle = other leg × cotangent of the adjacent angle.',
                ev='Mỗi cạnh góc vuông = cạnh huyền × sin góc đối = cạnh huyền × cos góc kề = cạnh góc vuông kia × tan góc đối = cạnh góc vuông kia × cot góc kề.')

def b12_tf_rel(r, lv):
    R, X, Y = r.choice(TRI_NAMES); g, b = _rels(R, X, Y); truth = r.random() < 0.5; s = r.choice(g if truth else b[:8])
    return dict(en='Triangle \\(%s%s%s\\) is right-angled at \\(%s\\). Then \\(%s\\).' % (R, X, Y, R, s), vi='Tam giác \\(%s%s%s\\) vuông tại \\(%s\\). Khi đó \\(%s\\).' % (R, X, Y, R, s), ans=truth,
                ee='The hypotenuse is \\(%s%s\\); \\(%s%s\\) is opposite angle \\(%s\\) and \\(%s%s\\) is opposite angle \\(%s\\).' % (X, Y, R, Y, X, R, X, Y),
                ev='Cạnh huyền là \\(%s%s\\); \\(%s%s\\) là cạnh đối của góc \\(%s\\), \\(%s%s\\) là cạnh đối của góc \\(%s\\).' % (X, Y, R, Y, X, R, X, Y))

def b12_tf_solve(r, lv):
    a, B = r.randint(5, 20), _ang(r); truth = r.random() < 0.5
    v = a * math.cos(math.radians(B)); good = _r1(v)
    shown = good if truth else _r1(a * math.sin(math.radians(B)))
    assert truth or shown != good
    return dict(en='Triangle \\(ABC\\) is right-angled at \\(A\\), \\(BC=%d\\) and \\(\\widehat{B}=%d^\\circ\\). Then \\(\\widehat{C}=%d^\\circ\\) and \\(AB\\approx %s\\) (nearest tenth).' % (a, B, 90 - B, shown),
                vi='Tam giác \\(ABC\\) vuông tại \\(A\\), \\(BC=%d\\) và \\(\\widehat{B}=%d^\\circ\\). Khi đó \\(\\widehat{C}=%d^\\circ\\) và \\(AB\\approx %s\\) (làm tròn đến hàng phần mười).' % (a, B, 90 - B, dm(shown)), ans=truth,
                ee='\\(AB\\) is adjacent to \\(B\\): \\(AB=BC\\cdot\\cos B\\approx %s\\).' % good, ev='\\(AB\\) là cạnh kề của góc \\(B\\): \\(AB=BC\\cdot\\cos B\\approx %s\\).' % dm(good))

def b12_short_hyp(r, lv):
    c, B = r.randint(4, 30), _ang(r); key = _r1(c / math.cos(math.radians(B)))
    return dict(en='Triangle \\(ABC\\) is right-angled at \\(A\\), \\(AB=%d\\) cm and \\(\\widehat{B}=%d^\\circ\\). Find \\(BC\\) in centimeters, rounded to the nearest tenth.' % (c, B),
                vi='Tam giác \\(ABC\\) vuông tại \\(A\\), \\(AB=%d\\) cm và \\(\\widehat{B}=%d^\\circ\\). Tính \\(BC\\) theo xăng-ti-mét (làm tròn đến hàng phần mười).' % (c, B), key=key, hint=HINT_D1,
                ee='\\(AB=BC\\cdot\\cos B\\Rightarrow BC=\\dfrac{%d}{\\cos %d^\\circ}\\approx %s\\) cm.' % (c, B, key), ev='\\(AB=BC\\cdot\\cos B\\Rightarrow BC=\\dfrac{%d}{\\cos %d^\\circ}\\approx %s\\) cm.' % (c, B, dm(key)))

def b12_short_angle(r, lv):
    while True:
        p, q = r.randint(3, 20), r.randint(3, 20); B = math.degrees(math.atan2(q, p))
        if p != q and abs(B - math.floor(B) - 0.5) > 0.05: break
    n = round(B)
    return dict(en='Triangle \\(ABC\\) is right-angled at \\(A\\), \\(AB=%d\\) cm and \\(AC=%d\\) cm. Find angle \\(B\\) in degrees, rounded to the nearest degree.' % (p, q),
                vi='Tam giác \\(ABC\\) vuông tại \\(A\\), \\(AB=%d\\) cm và \\(AC=%d\\) cm. Tính số đo góc \\(B\\) (làm tròn đến độ).' % (p, q), key=str(n), hint=('Enter a whole number of degrees.', 'Nhập số đo theo độ (số nguyên).'),
                ee='\\(\\tan B=\\dfrac{AC}{AB}=\\dfrac{%d}{%d}\\Rightarrow B\\approx %d^\\circ\\) (SHIFT tan).' % (q, p, n), ev='\\(\\tan B=\\dfrac{AC}{AB}=\\dfrac{%d}{%d}\\Rightarrow B\\approx %d^\\circ\\) (bấm SHIFT tan).' % (q, p, n))

def b12_d1_hyp(r, lv):
    R, X, Y = r.choice(TRI_NAMES)
    return dict(en='Triangle \\(%s%s%s\\) is right-angled at \\(%s\\). Which side is the hypotenuse?' % (R, X, Y, R), vi='Tam giác \\(%s%s%s\\) vuông tại \\(%s\\). Cạnh huyền là cạnh nào?' % (R, X, Y, R),
                opts=['%s%s' % (X, Y), '%s%s' % (R, X), '%s%s' % (R, Y), tx('none of them', 'không có cạnh nào')], ans=0,
                ee='The hypotenuse is opposite the right angle \\(%s\\).' % R, ev='Cạnh huyền là cạnh đối diện với góc vuông \\(%s\\).' % R)

def b12_d1_other(r, lv):
    R, X, Y = r.choice(TRI_NAMES); b = r.randint(10, 80)
    return dict(en='Triangle \\(%s%s%s\\) is right-angled at \\(%s\\) and \\(\\widehat{%s}=%d^\\circ\\). Find \\(\\widehat{%s}\\).' % (R, X, Y, R, X, b, Y), vi='Tam giác \\(%s%s%s\\) vuông tại \\(%s\\) và \\(\\widehat{%s}=%d^\\circ\\). Tính \\(\\widehat{%s}\\).' % (R, X, Y, R, X, b, Y),
                opts=pick_opts(r, '%d^\\circ' % (90 - b), ['%d^\\circ' % v for v in (180 - b, b, 90 + b) if v != 90 - b], fill=lambda k: '%d^\\circ' % (90 - b + 10 * k)), ans=0,
                ee='The two acute angles of a right triangle are complementary: \\(90^\\circ-%d^\\circ=%d^\\circ\\).' % (b, 90 - b), ev='Hai góc nhọn của tam giác vuông phụ nhau: \\(90^\\circ-%d^\\circ=%d^\\circ\\).' % (b, 90 - b))

def b12_d1_rule(r, lv):
    k = r.choice(['sin', 'cos', 'tan', 'cot'])
    stem = {'sin': ('hypotenuse × sine of …', 'cạnh huyền × sin của …'), 'cos': ('hypotenuse × cosine of …', 'cạnh huyền × cos của …'),
            'tan': ('the other leg × tangent of …', 'cạnh góc vuông kia × tan của …'), 'cot': ('the other leg × cotangent of …', 'cạnh góc vuông kia × cot của …')}[k]
    good = k in ('sin', 'tan')
    o = [tx('the opposite angle', 'góc đối'), tx('the adjacent angle', 'góc kề'), tx('the right angle', 'góc vuông'), tx('any angle of the triangle', 'góc bất kì của tam giác')]
    if not good: o[0], o[1] = o[1], o[0]
    return dict(en='In a right triangle, each leg equals %s' % stem[0], vi='Trong tam giác vuông, mỗi cạnh góc vuông bằng %s' % stem[1], opts=o, ans=0,
                ee='sin, tan go with the opposite angle; cos, cot go with the adjacent angle.', ev='sin, tan đi với góc đối; cos, cot đi với góc kề.')

def b12_d2_cos(r, lv):
    a, C = r.randint(6, 30), _ang(r); good = _r1(a * math.cos(math.radians(C))); bads = []
    for v in (a * math.sin(math.radians(C)), a / math.cos(math.radians(C)), a * math.tan(math.radians(C))):
        try: bads.append(_r1(v))
        except AssertionError: bads.append('%.1f' % v)
    return dict(en='Triangle \\(ABC\\) is right-angled at \\(A\\), \\(BC=%d\\) cm and \\(\\widehat{C}=%d^\\circ\\). Find \\(AC\\) (nearest tenth).' % (a, C),
                vi='Tam giác \\(ABC\\) vuông tại \\(A\\), \\(BC=%d\\) cm và \\(\\widehat{C}=%d^\\circ\\). Tính \\(AC\\) (làm tròn đến hàng phần mười).' % (a, C),
                opts=_dec_opts(r, good, bads, 'cm'), ans=0, ee='\\(AC\\) is adjacent to \\(C\\): \\(AC=BC\\cdot\\cos C\\approx %s\\) cm.' % good, ev='\\(AC\\) là cạnh kề của góc \\(C\\): \\(AC=BC\\cdot\\cos C\\approx %s\\) cm.' % dm(good))

def b12_d2_cot(r, lv):
    b, B = r.randint(4, 25), _ang(r); good = _r1(b / math.tan(math.radians(B))); bads = []
    for v in (b * math.tan(math.radians(B)), b * math.cos(math.radians(B)), b / math.sin(math.radians(B))):
        try: bads.append(_r1(v))
        except AssertionError: bads.append('%.1f' % v)
    return dict(en='Triangle \\(ABC\\) is right-angled at \\(A\\), \\(AC=%d\\) m and \\(\\widehat{B}=%d^\\circ\\). Find \\(AB\\) (nearest tenth).' % (b, B),
                vi='Tam giác \\(ABC\\) vuông tại \\(A\\), \\(AC=%d\\) m và \\(\\widehat{B}=%d^\\circ\\). Tính \\(AB\\) (làm tròn đến hàng phần mười).' % (b, B),
                opts=_dec_opts(r, good, bads, 'm'), ans=0, ee='\\(AB=AC\\cdot\\cot B=\\dfrac{%d}{\\tan %d^\\circ}\\approx %s\\) m.' % (b, B, good), ev='\\(AB=AC\\cdot\\cot B=\\dfrac{%d}{\\tan %d^\\circ}\\approx %s\\) m.' % (b, B, dm(good)))

def b12_d2_exact(r, lv):
    k = r.randint(2, 15); B = r.choice([30, 60]); kind = r.choice(['AC', 'BC'])
    # AB = k (cạnh kề góc B)
    if kind == 'AC': good, bad = ('%d\\sqrt{3}' % k, '\\dfrac{%d\\sqrt{3}}{3}' % k) if B == 60 else ('\\dfrac{%d\\sqrt{3}}{3}' % k, '%d\\sqrt{3}' % k)
    else: good, bad = ('%d' % (2 * k), '\\dfrac{%d\\sqrt{3}}{3}' % (2 * k)) if B == 60 else ('\\dfrac{%d\\sqrt{3}}{3}' % (2 * k), '%d' % (2 * k))
    o = [good, bad, '%d\\sqrt{2}' % k, '%d' % k if good != '%d' % k else '%d' % (3 * k)]
    return dict(en='Triangle \\(ABC\\) is right-angled at \\(A\\), \\(AB=%d\\) and \\(\\widehat{B}=%d^\\circ\\). Find the exact value of \\(%s\\).' % (k, B, kind),
                vi='Tam giác \\(ABC\\) vuông tại \\(A\\), \\(AB=%d\\) và \\(\\widehat{B}=%d^\\circ\\). Tính giá trị đúng của \\(%s\\).' % (k, B, kind), opts=o, ans=0,
                ee='\\(%s\\).' % ('AC=AB\\cdot\\tan %d^\\circ' % B if kind == 'AC' else 'BC=\\dfrac{AB}{\\cos %d^\\circ}' % B), ev='\\(%s\\).' % ('AC=AB\\cdot\\tan %d^\\circ' % B if kind == 'AC' else 'BC=\\dfrac{AB}{\\cos %d^\\circ}' % B))

def b12_d3_solve(r, lv):
    a, B = r.randint(6, 25), _ang(r); s, c = math.sin(math.radians(B)), math.cos(math.radians(B))
    AC, AB = _r1(a * s), _r1(a * c)
    trip = lambda C_, x, y: tx('\\(\\widehat{C}=%d^\\circ,\\ AB\\approx %s,\\ AC\\approx %s\\)' % (C_, x, y), '\\(\\widehat{C}=%d^\\circ,\\ AB\\approx %s,\\ AC\\approx %s\\)' % (C_, dm(x), dm(y)))
    assert AC != AB
    o = [trip(90 - B, AB, AC), trip(90 - B, AC, AB), trip(B, AB, AC), trip(180 - B, AB, AC)]
    return dict(en='Solve the right triangle \\(ABC\\) (right angle at \\(A\\)) given \\(BC=%d\\) and \\(\\widehat{B}=%d^\\circ\\) (sides to the nearest tenth).' % (a, B),
                vi='Giải tam giác \\(ABC\\) vuông tại \\(A\\), biết \\(BC=%d\\) và \\(\\widehat{B}=%d^\\circ\\) (cạnh làm tròn đến hàng phần mười).' % (a, B), opts=o, ans=0,
                ee='\\(\\widehat{C}=90^\\circ-%d^\\circ\\); \\(AB=BC\\cos B\\), \\(AC=BC\\sin B\\).' % B, ev='\\(\\widehat{C}=90^\\circ-%d^\\circ\\); \\(AB=BC\\cos B\\), \\(AC=BC\\sin B\\).' % B)

def b12_d3_ladder(r, lv):
    L, a = r.choice([3, 4, 5, 6, 7, 8]), r.randint(55, 80); good = _r1(L * math.sin(math.radians(a))); bads = []
    for v in (L * math.cos(math.radians(a)), L * math.tan(math.radians(a)) if L * math.tan(math.radians(a)) < 60 else L + 1.3, L / math.sin(math.radians(a))):
        try: bads.append(_r1(v))
        except AssertionError: bads.append('%.1f' % v)
    return dict(en='A %d m ladder leans against a vertical wall and makes a \\(%d^\\circ\\) angle with the ground. How high up the wall does it reach (nearest tenth)?' % (L, a),
                vi='Một chiếc thang dài %d m dựa vào bức tường thẳng đứng, tạo với mặt đất một góc \\(%d^\\circ\\). Đầu thang chạm tường ở độ cao bao nhiêu (làm tròn đến hàng phần mười)?' % (L, a),
                opts=_dec_opts(r, good, bads, 'm'), ans=0, ee='Height \\(=%d\\cdot\\sin %d^\\circ\\approx %s\\) m.' % (L, a, good), ev='Độ cao \\(=%d\\cdot\\sin %d^\\circ\\approx %s\\) m.' % (L, a, dm(good)))

def b12_d3_depr(r, lv):
    h, d = r.randint(12, 60), r.randint(20, 50); good = _r1(h / math.tan(math.radians(d))); bads = []
    for v in (h * math.tan(math.radians(d)), h * math.cos(math.radians(d)), h / math.sin(math.radians(d))):
        try: bads.append(_r1(v))
        except AssertionError: bads.append('%.1f' % v)
    return dict(en='From the top of a %d m tall building, the angle of depression to a car on the ground is \\(%d^\\circ\\). Find the horizontal distance from the car to the foot of the building (nearest tenth).' % (h, d),
                vi='Từ đỉnh một tòa nhà cao %d m, góc hạ nhìn xuống một chiếc ô tô trên mặt đất là \\(%d^\\circ\\). Tính khoảng cách từ ô tô đến chân tòa nhà (làm tròn đến hàng phần mười).' % (h, d),
                opts=_dec_opts(r, good, bads, 'm'), ans=0,
                ee='The angle of depression equals the angle of elevation from the car: distance \\(=\\dfrac{%d}{\\tan %d^\\circ}\\approx %s\\) m.' % (h, d, good),
                ev='Góc hạ bằng góc nâng nhìn từ ô tô (so le trong): khoảng cách \\(=\\dfrac{%d}{\\tan %d^\\circ}\\approx %s\\) m.' % (h, d, dm(good)))

def b12_d4_two(r, lv):
    a1, a2 = r.choice([(30, 45), (30, 60), (45, 60)]); d = r.choice(range(10, 61, 2))
    t1, t2 = math.tan(math.radians(a1)), math.tan(math.radians(a2)); h = d / (1 / t1 - 1 / t2); good = _r1(h); bads = []
    for v in (d * t1, d * t2, d / (1 / t1 + 1 / t2)):
        try: bads.append(_r1(v))
        except AssertionError: bads.append('%.1f' % v)
    return dict(en='From point \\(M\\) on level ground, the angle of elevation to the top of a tower is \\(%d^\\circ\\). After walking %d m straight towards the tower to point \\(N\\), the angle of elevation is \\(%d^\\circ\\). Find the height of the tower (nearest tenth).' % (a1, d, a2),
                vi='Từ điểm \\(M\\) trên mặt đất phẳng, góc nâng nhìn lên đỉnh một tháp là \\(%d^\\circ\\). Đi thẳng về phía tháp %d m đến điểm \\(N\\) thì góc nâng là \\(%d^\\circ\\). Tính chiều cao của tháp (làm tròn đến hàng phần mười).' % (a1, d, a2),
                opts=_dec_opts(r, good, bads, 'm'), ans=0,
                ee='Let \\(h\\) be the height: \\(h\\cot %d^\\circ-h\\cot %d^\\circ=%d\\Rightarrow h=\\dfrac{%d}{\\cot %d^\\circ-\\cot %d^\\circ}\\approx %s\\) m.' % (a1, a2, d, d, a1, a2, good),
                ev='Gọi \\(h\\) là chiều cao: \\(h\\cot %d^\\circ-h\\cot %d^\\circ=%d\\Rightarrow h=\\dfrac{%d}{\\cot %d^\\circ-\\cot %d^\\circ}\\approx %s\\) m.' % (a1, a2, d, d, a1, a2, dm(good)))

def b12_d4_eye(r, lv):
    e, d, a = r.choice([1.5, 1.6, 1.7]), r.randint(8, 40), r.randint(20, 60); good = _r1(e + d * math.tan(math.radians(a))); bads = []
    for v in (d * math.tan(math.radians(a)), e + d * math.sin(math.radians(a)), e + d / math.tan(math.radians(a))):
        try: bads.append(_r1(v))
        except AssertionError: bads.append('%.1f' % v)
    es = ('%g' % e)
    return dict(en='A student whose eyes are %s m above the ground stands %d m from a flagpole and sees its top at an angle of elevation of \\(%d^\\circ\\). How tall is the flagpole (nearest tenth)?' % (es, d, a),
                vi='Một bạn học sinh có mắt cách mặt đất %s m đứng cách cột cờ %d m, nhìn đỉnh cột cờ với góc nâng \\(%d^\\circ\\). Cột cờ cao bao nhiêu mét (làm tròn đến hàng phần mười)?' % (es.replace('.', ','), d, a),
                opts=_dec_opts(r, good, bads, 'm'), ans=0,
                ee='Height \\(=%s+%d\\cdot\\tan %d^\\circ\\approx %s\\) m (add the eye height).' % (es, d, a, good), ev='Chiều cao \\(=%s+%d\\cdot\\tan %d^\\circ\\approx %s\\) m (cộng thêm chiều cao tới mắt).' % (dm(es), d, a, dm(good)))

def b12_d4_plane(r, lv):
    v, a, t = r.choice([300, 360, 400, 450, 480, 500, 600]), r.choice([10, 12, 15, 20, 25, 30]), r.choice([1.2, 1.5, 2, 3])
    dist = v * t / 60; assert abs(dist * 10 - round(dist * 10)) < 1e-9; dist = round(dist, 1); h = dist * math.sin(math.radians(a)); good = _r1(h); bads = []
    for w in (dist * math.cos(math.radians(a)), dist * math.tan(math.radians(a)), dist):
        try: bads.append(_r1(w))
        except AssertionError: bads.append('%.1f' % w)
    ts = '%g' % t
    return dict(en='An airplane climbs at %d km/h along a path that makes a \\(%d^\\circ\\) angle with the horizontal. How many kilometers does it rise in %s minutes (nearest tenth)?' % (v, a, ts),
                vi='Một máy bay bay lên với vận tốc %d km/h theo đường tạo với phương nằm ngang một góc \\(%d^\\circ\\). Sau %s phút máy bay lên cao được bao nhiêu ki-lô-mét (làm tròn đến hàng phần mười)?' % (v, a, ts.replace('.', ',')),
                opts=_dec_opts(r, good, bads, 'km'), ans=0,
                ee='Distance flown \\(=%d\\cdot\\dfrac{%s}{60}=%g\\) km; height \\(=%g\\cdot\\sin %d^\\circ\\approx %s\\) km.' % (v, ts, dist, dist, a, good),
                ev='Quãng đường bay \\(=%d\\cdot\\dfrac{%s}{60}=%s\\) km; độ cao \\(=%s\\cdot\\sin %d^\\circ\\approx %s\\) km.' % (v, dm(ts), dm('%g' % dist), dm('%g' % dist), a, dm(good)))

L12_GROUPS = [[('mcq', b12_leg_sin), ('mcq', b12_leg_tan), ('mcq', b12_formula)], [('tf', b12_tf_rel), ('tf', b12_tf_solve)], [('short', b12_short_hyp), ('short', b12_short_angle)],
              [('mcq', b12_d1_hyp), ('mcq', b12_d1_other), ('mcq', b12_d1_rule)], [('mcq', b12_d2_cos), ('mcq', b12_d2_cot), ('mcq', b12_d2_exact)],
              [('mcq', b12_d3_solve), ('mcq', b12_d3_ladder), ('mcq', b12_d3_depr)], [('mcq', b12_d4_two), ('mcq', b12_d4_eye), ('mcq', b12_d4_plane)]]
