# -*- coding: utf-8 -*-
"""Ngân hàng câu hỏi sinh tự động cho Toán 9 (KNTT) – Bài 1 đến Bài 4.
Mỗi hàm builder(r, lv) trả về một câu hỏi; mọi đáp án do máy tính tính bằng phân số (Fraction) và tự kiểm lại
(thay nghiệm vào phương trình, duyệt điều kiện xác định…). Câu hỏi ở mỗi mức ngôn ngữ dùng số liệu khác nhau.

Ba loại câu hỏi:
  mcq   -> dict(en, vi, opts[4], ans, ee, ev)       (opts[ans] là phương án đúng; phương án văn bản viết '§' + TI(en, vi))
  tf    -> dict(en, vi, ans=True/False, ee, ev)
  short -> dict(en, vi, key, ee, ev)                (key là đáp số; ô trả lời nhận số nguyên hoặc thập phân)
BANK(groups, start) -> {1: [[mục nhóm 1], [mục nhóm 2], ...], 2: [...], 3: [...]} dùng thẳng cho LEVEL_PRACTICE."""
import random
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
    t += [('D1. Self-practice – Remembering', 'D1. Tự luyện – Mức Biết'), ('D2. Self-practice – Understanding', 'D2. Tự luyện – Mức Hiểu'),
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
