# -*- coding: utf-8 -*-
"""Ngân hàng câu hỏi Toán 8 (KNTT) – Chương III. Tứ giác (Bài 10–14).
Khung BANK / ABCD_TITLES của sp_g9; hình tĩnh vẽ bằng tfig (tên điểm tự tránh nét vẽ, góc vuông vẽ ô vuông)."""
import random, math
from fractions import Fraction as F
from sp_g9 import tx, nz, pick_opts, BANK, ABCD_TITLES
from sp_g9q import tfig
from sp_g9p import img

PICK = lambda r, L: L[r.randrange(len(L))]
NAMES = ['ABCD', 'MNPQ', 'EFGH', 'PQRS', 'KLMN', 'WXYZ', 'DEFG', 'IJKL']
def dg(v): return '%s^\\circ' % (v if isinstance(v, int) or float(v).is_integer() and int(v) == v else v)
def D(v): return '%d^\\circ' % v
def hat(s): return '\\widehat{%s}' % s

def dopt(r, good, bads, step=5):
    """Phương án số đo góc (độ)."""
    bads = [b for b in dict.fromkeys(bads) if b != good and 0 < b < 360]
    return pick_opts(r, D(good), [D(b) for b in bads], fill=lambda t: D(good + step * (t + 1) * (1 if t % 2 else -1)))

def nopt(r, good, bads, step=1, unit=''):
    f = lambda v: ('%s' % v) + unit
    bads = [b for b in dict.fromkeys(bads) if b != good and b > 0]
    return pick_opts(r, f(good), [f(b) for b in bads], fill=lambda t: f(good + step * (t + 1)))

def num(v):
    v = F(v)
    if v.denominator == 1: return str(v.numerator)
    s = '%g' % float(v); assert F(s) == v; return s
def vn(v): return num(v).replace('.', '{,}')

# ------------------------------------------------------------------ hình
def QF(P, segs=(), dash=(), right=(), px=260):
    fn = tfig(P=P, segs=segs, dash=dash, right=right)
    return (img(fn, 'Figure', px), img(fn, 'Hình vẽ', px))

def cyc(n):
    return [(n[i], n[(i + 1) % 4]) for i in range(4)]

def shape(kind, r):
    """Tọa độ 4 đỉnh (ngược chiều kim đồng hồ, bắt đầu từ góc dưới trái)."""
    if kind == 'quad':
        return [(0, 0), (r.uniform(3.6, 4.4), r.uniform(-0.3, 0.4)), (r.uniform(3.0, 4.2), r.uniform(2.2, 2.9)), (r.uniform(0.3, 1.1), r.uniform(1.8, 2.6))]
    if kind == 'trap':
        a = r.uniform(0.7, 1.4); b = r.uniform(0.7, 1.4); h = r.uniform(1.9, 2.4); W = r.uniform(4.2, 4.8)
        return [(0, 0), (W, 0), (W - b, h), (a, h)]
    if kind == 'itrap':
        a = r.uniform(0.8, 1.3); h = r.uniform(1.9, 2.3); W = r.uniform(4.2, 4.8)
        return [(0, 0), (W, 0), (W - a, h), (a, h)]
    if kind == 'para':
        s = r.uniform(0.9, 1.4); h = r.uniform(2.0, 2.4); W = r.uniform(3.6, 4.2)
        return [(0, 0), (W, 0), (W + s, h), (s, h)]
    if kind == 'rect':
        W, h = r.uniform(3.8, 4.4), r.uniform(2.1, 2.5); return [(0, 0), (W, 0), (W, h), (0, h)]
    if kind == 'rhom':
        a, b = r.uniform(2.0, 2.4), r.uniform(1.3, 1.6); return [(0, 0), (a, -b), (2 * a, 0), (a, b)]
    if kind == 'sq':
        return [(0, 0), (3, 0), (3, 3), (0, 3)]

def pts(names, coords): return {n: c for n, c in zip(names, coords)}

# =====================================================================================================
# BÀI 10. TỨ GIÁC
# =====================================================================================================
def _angles(r, lo=50, hi=140):
    while True:
        a, b, c = [r.randrange(lo, hi, 5) for _ in range(3)]; d = 360 - a - b - c
        if 40 <= d <= 160 and len({a, b, c, d}) >= 3: return a, b, c, d

def b10_fourth(r, lv):
    n = PICK(r, NAMES); a, b, c, d = _angles(r)
    t = '%s=%s,\\ %s=%s,\\ %s=%s' % (hat(n[0]), D(a), hat(n[1]), D(b), hat(n[2]), D(c))
    return dict(en='Quadrilateral \\(%s\\) has \\(%s\\). Find \\(%s\\).' % (n, t, hat(n[3])), vi='Tứ giác \\(%s\\) có \\(%s\\). Tính \\(%s\\).' % (n, t, hat(n[3])),
                opts=dopt(r, d, [180 - d if d != 90 else d + 10, 360 - a - b, 180 - c]), ans=0,
                ee='\\(%s=360^\\circ-%d^\\circ-%d^\\circ-%d^\\circ=%s\\).' % (hat(n[3]), a, b, c, D(d)), ev='\\(%s=360^\\circ-%d^\\circ-%d^\\circ-%d^\\circ=%s\\).' % (hat(n[3]), a, b, c, D(d)))

def b10_sum(r, lv):
    Q = PICK(r, [('The sum of the interior angles of a quadrilateral is…', 'Tổng các góc của một tứ giác bằng'), ('In every quadrilateral, the four angles add up to…', 'Trong mọi tứ giác, tổng bốn góc bằng'),
                 ('A diagonal divides a quadrilateral into two triangles, so the angle sum of the quadrilateral is…', 'Một đường chéo chia tứ giác thành hai tam giác nên tổng các góc của tứ giác bằng'),
                 ('Which number is the angle sum of any quadrilateral?', 'Tổng các góc của một tứ giác bất kì là')])
    return dict(en=Q[0], vi=Q[1], opts=[D(360), D(180), D(540), D(270)], ans=0, ee='\\(2\\cdot180^\\circ=360^\\circ\\).', ev='\\(2\\cdot180^\\circ=360^\\circ\\).')

def b10_diag(r, lv):
    n = PICK(r, NAMES); P = pts(n, shape('quad', r)); fig = QF(P, segs=cyc(n))
    good = '%s%s,\\ %s%s' % (n[0], n[2], n[1], n[3]); bads = ['%s%s,\\ %s%s' % (n[0], n[1], n[2], n[3]), '%s%s,\\ %s%s' % (n[0], n[3], n[1], n[2]), '%s%s,\\ %s%s' % (n[0], n[2], n[2], n[3])]
    return dict(en='What are the diagonals of quadrilateral \\(%s\\)?' % n, vi='Các đường chéo của tứ giác \\(%s\\) là' % n, opts=[good] + bads, ans=0, fig=fig,
                ee='A diagonal joins two opposite vertices: \\(%s\\).' % good, ev='Đường chéo nối hai đỉnh đối nhau: \\(%s\\).' % good)

TF10 = [('A convex quadrilateral can have four acute angles.', 'Một tứ giác lồi có thể có bốn góc nhọn.', False, 'Four acute angles add up to less than \\(360^\\circ\\).', 'Bốn góc nhọn có tổng nhỏ hơn \\(360^\\circ\\).'),
        ('A convex quadrilateral can have four obtuse angles.', 'Một tứ giác lồi có thể có bốn góc tù.', False, 'Four obtuse angles add up to more than \\(360^\\circ\\).', 'Bốn góc tù có tổng lớn hơn \\(360^\\circ\\).'),
        ('A quadrilateral can have four right angles.', 'Một tứ giác có thể có bốn góc vuông.', True, '\\(4\\cdot90^\\circ=360^\\circ\\), e.g. a rectangle.', '\\(4\\cdot90^\\circ=360^\\circ\\), chẳng hạn hình chữ nhật.'),
        ('A quadrilateral has exactly two diagonals.', 'Một tứ giác có đúng hai đường chéo.', True, 'Each diagonal joins a pair of opposite vertices; there are two such pairs.', 'Mỗi đường chéo nối một cặp đỉnh đối nhau; có hai cặp như vậy.'),
        ('A quadrilateral can have three obtuse angles.', 'Một tứ giác có thể có ba góc tù.', True, 'For example \\(100^\\circ,100^\\circ,100^\\circ,60^\\circ\\).', 'Ví dụ \\(100^\\circ,100^\\circ,100^\\circ,60^\\circ\\).'),
        ('Two opposite sides of a quadrilateral share a vertex.', 'Hai cạnh đối nhau của tứ giác có chung một đỉnh.', False, 'Opposite sides do not share a vertex.', 'Hai cạnh đối nhau không có đỉnh chung.')]
def b10_tf_claim(r, lv):
    en, vi, t, ee, ev = PICK(r, TF10); return dict(en=en, vi=vi, ans=t, ee=ee, ev=ev)

def b10_tf_num(r, lv):
    n = PICK(r, NAMES); a, b, c, d = _angles(r); truth = r.random() < .5; claim = d if truth else 360 - a - b - c + r.choice([-10, 10, 20])
    t = '%s=%s,\\ %s=%s,\\ %s=%s' % (hat(n[0]), D(a), hat(n[1]), D(b), hat(n[2]), D(c))
    return dict(en='In quadrilateral \\(%s\\), \\(%s\\). Then \\(%s=%s\\).' % (n, t, hat(n[3]), D(claim)), vi='Tứ giác \\(%s\\) có \\(%s\\). Khi đó \\(%s=%s\\).' % (n, t, hat(n[3]), D(claim)),
                ans=(claim == d), ee='\\(%s=%s\\).' % (hat(n[3]), D(d)), ev='\\(%s=%s\\).' % (hat(n[3]), D(d)))

def _xangles(r):
    while True:
        k = [r.randint(1, 3) for _ in range(4)]; c = [r.randrange(-30, 45, 5) for _ in range(3)]
        S = sum(k); c4 = None
        x = r.randrange(20, 70, 5); c.append(360 - sum(c) - S * x)
        angs = [k[i] * x + c[i] for i in range(4)]
        if all(30 <= a <= 170 for a in angs) and -40 <= c[3] <= 60: return k, c, x, angs

def _xe(k, c):
    if c == 0: return '%s^\\circ' % ('x' if k == 1 else '%dx' % k)
    return '(%s%s)^\\circ' % ('x' if k == 1 else '%dx' % k, '+%d' % c if c > 0 else '%d' % c)

def b10_short_x(r, lv):
    n = PICK(r, NAMES); k, c, x, angs = _xangles(r)
    t = ',\\ '.join('%s=%s' % (hat(n[i]), _xe(k[i], c[i])) for i in range(4))
    return dict(en='Quadrilateral \\(%s\\) has \\(%s\\). Find \\(x\\).' % (n, t), vi='Tứ giác \\(%s\\) có \\(%s\\). Tìm \\(x\\).' % (n, t), key=str(x),
                ee='\\(%dx%+d=360\\Rightarrow x=%d\\).' % (sum(k), sum(c), x), ev='\\(%dx%+d=360\\Rightarrow x=%d\\).' % (sum(k), sum(c), x))

RATIOS = [(1, 2, 3, 4), (2, 3, 4, 6), (3, 4, 5, 6), (1, 3, 5, 6), (2, 3, 5, 8), (1, 2, 2, 3), (3, 5, 5, 7), (4, 5, 6, 9), (2, 4, 5, 9), (1, 4, 5, 8)]
def b10_short_ratio(r, lv):
    n = PICK(r, NAMES); q = PICK(r, RATIOS); S = sum(q)
    if 360 % S: raise AssertionError
    u = 360 // S; big = q[-1] * u
    return dict(en='The angles \\(%s\\) of quadrilateral \\(%s\\) are in the ratio \\(%s\\). Find the largest angle (in degrees).' % (',\\ '.join(hat(c) for c in n), n, ':'.join(map(str, q))),
                vi='Các góc \\(%s\\) của tứ giác \\(%s\\) tỉ lệ với \\(%s\\). Tìm số đo góc lớn nhất (theo độ).' % (',\\ '.join(hat(c) for c in n), n, ':'.join(map(str, q))),
                key=str(big), ee='One part \\(=360^\\circ:%d=%d^\\circ\\); largest angle \\(=%d\\cdot%d^\\circ=%s\\).' % (S, u, q[-1], u, D(big)), ev='Mỗi phần \\(=360^\\circ:%d=%d^\\circ\\); góc lớn nhất \\(=%d\\cdot%d^\\circ=%s\\).' % (S, u, q[-1], u, D(big)))

def b10_d1_opp(r, lv):
    n = PICK(r, NAMES); i = r.randrange(4)
    good = n[(i + 2) % 4]; o = [good, n[(i + 1) % 4], n[(i + 3) % 4], n[i]]
    return dict(en='In quadrilateral \\(%s\\), which vertex is opposite to vertex \\(%s\\)?' % (n, n[i]), vi='Trong tứ giác \\(%s\\), đỉnh đối với đỉnh \\(%s\\) là' % (n, n[i]), opts=o, ans=0,
                ee='Vertices \\(%s\\) and \\(%s\\) are not consecutive.' % (n[i], good), ev='Hai đỉnh \\(%s\\) và \\(%s\\) không kề nhau.' % (n[i], good))

def b10_d1_side(r, lv):
    n = PICK(r, NAMES); i = r.randrange(4); s = n[i] + n[(i + 1) % 4]; good = n[(i + 2) % 4] + n[(i + 3) % 4]
    o = [good, n[(i + 1) % 4] + n[(i + 2) % 4], n[(i + 3) % 4] + n[i], n[i] + n[(i + 2) % 4]]
    P = pts(n, shape('quad', r)); fig = QF(P, segs=cyc(n))
    return dict(en='Which side of quadrilateral \\(%s\\) is opposite to side \\(%s\\)?' % (n, s), vi='Cạnh đối của cạnh \\(%s\\) trong tứ giác \\(%s\\) là' % (s, n), opts=o, ans=0, fig=fig,
                ee='Opposite sides have no common vertex.', ev='Hai cạnh đối nhau không có đỉnh chung.')

def b10_d1_pair(r, lv):
    n = PICK(r, NAMES)
    good = '%s\\text{ and }%s' % (hat(n[0]), hat(n[2])) if r.random() < .5 else '%s\\text{ and }%s' % (hat(n[1]), hat(n[3]))
    o_en = [good, '%s\\text{ and }%s' % (hat(n[0]), hat(n[1])), '%s\\text{ and }%s' % (hat(n[1]), hat(n[2])), '%s\\text{ and }%s' % (hat(n[3]), hat(n[0]))]
    o = [tx('\\(%s\\)' % x, '\\(%s\\)' % x.replace('\\text{ and }', '\\text{ và }')) for x in o_en]
    return dict(en='Which is a pair of opposite angles of quadrilateral \\(%s\\)?' % n, vi='Cặp góc nào là hai góc đối nhau của tứ giác \\(%s\\)?' % n, opts=o, ans=0,
                ee='Opposite angles are at opposite vertices.', ev='Hai góc đối nhau ở hai đỉnh đối nhau.')

def b10_d2_ext(r, lv):
    n = PICK(r, NAMES); a, b, c, d = _angles(r)
    t = '%s=%s,\\ %s=%s,\\ %s=%s' % (hat(n[0]), D(a), hat(n[1]), D(b), hat(n[2]), D(c))
    return dict(en='Quadrilateral \\(%s\\) has \\(%s\\). Find the exterior angle at vertex \\(%s\\) (the angle adjacent and supplementary to \\(%s\\)).' % (n, t, n[3], hat(n[3])),
                vi='Tứ giác \\(%s\\) có \\(%s\\). Tính góc ngoài tại đỉnh \\(%s\\) (góc kề bù với \\(%s\\)).' % (n, t, n[3], hat(n[3])),
                opts=dopt(r, 180 - d, [d, 360 - d, 180 - c]), ans=0, ee='\\(%s=%s\\), exterior angle \\(=180^\\circ-%d^\\circ=%s\\).' % (hat(n[3]), D(d), d, D(180 - d)),
                ev='\\(%s=%s\\), góc ngoài \\(=180^\\circ-%d^\\circ=%s\\).' % (hat(n[3]), D(d), d, D(180 - d)))

def b10_d2_eq(r, lv):
    n = PICK(r, NAMES)
    while True:
        a = r.randrange(50, 100, 5); k = r.choice([2, 3]); c = r.randrange(40, 120, 5); d = 360 - a - a - c
        if 40 < d < 170 and d != c: break
    t = '%s=%s=%s,\\ %s=%s' % (hat(n[0]), hat(n[1]), D(a), hat(n[2]), D(c))
    return dict(en='Quadrilateral \\(%s\\) has \\(%s\\). Find \\(%s\\).' % (n, t, hat(n[3])), vi='Tứ giác \\(%s\\) có \\(%s\\). Tính \\(%s\\).' % (n, t, hat(n[3])),
                opts=dopt(r, d, [360 - a - c, 180 - c, 2 * a]), ans=0, ee='\\(360^\\circ-2\\cdot%d^\\circ-%d^\\circ=%s\\).' % (a, c, D(d)), ev='\\(360^\\circ-2\\cdot%d^\\circ-%d^\\circ=%s\\).' % (a, c, D(d)))

def b10_d2_small(r, lv):
    n = PICK(r, NAMES); q = PICK(r, RATIOS); S = sum(q)
    if 360 % S: raise AssertionError
    u = 360 // S
    return dict(en='The angles of quadrilateral \\(%s\\) are in the ratio \\(%s\\). Find the smallest angle.' % (n, ':'.join(map(str, q))), vi='Các góc của tứ giác \\(%s\\) tỉ lệ với \\(%s\\). Góc nhỏ nhất bằng' % (n, ':'.join(map(str, q))),
                opts=dopt(r, q[0] * u, [q[-1] * u, u * q[1], 360 // 4]), ans=0, ee='One part \\(=%d^\\circ\\); smallest \\(=%s\\).' % (u, D(q[0] * u)), ev='Mỗi phần \\(=%d^\\circ\\); góc nhỏ nhất \\(=%s\\).' % (u, D(q[0] * u)))

def b10_d3_x(r, lv):
    n = PICK(r, NAMES); k, c, x, angs = _xangles(r); i = r.randrange(4)
    t = ',\\ '.join('%s=%s' % (hat(n[j]), _xe(k[j], c[j])) for j in range(4))
    return dict(en='Quadrilateral \\(%s\\) has \\(%s\\). Find \\(%s\\).' % (n, t, hat(n[i])), vi='Tứ giác \\(%s\\) có \\(%s\\). Tính \\(%s\\).' % (n, t, hat(n[i])),
                opts=dopt(r, angs[i], [x, angs[(i + 1) % 4], 180 - angs[i]]), ans=0, ee='\\(%dx%+d=360\\Rightarrow x=%d\\Rightarrow %s=%s\\).' % (sum(k), sum(c), x, hat(n[i]), D(angs[i])),
                ev='\\(%dx%+d=360\\Rightarrow x=%d\\Rightarrow %s=%s\\).' % (sum(k), sum(c), x, hat(n[i]), D(angs[i])))

def b10_d3_kite(r, lv):
    n = PICK(r, NAMES)
    while True:
        b, d = r.randrange(60, 150, 2), r.randrange(50, 140, 2)
        if (360 - b - d) % 2 == 0 and b != d and 30 < (360 - b - d) // 2 < 150: break
    a = (360 - b - d) // 2
    t = '%s%s=%s%s,\\ %s%s=%s%s,\\ %s=%s,\\ %s=%s' % (n[0], n[1], n[1], n[2], n[0], n[3], n[2], n[3], hat(n[0] + n[1] + n[2]), D(b), hat(n[2] + n[3] + n[0]), D(d))
    return dict(en='Quadrilateral \\(%s\\) has \\(%s\\). Find \\(%s\\).' % (n, t, hat(n[3] + n[0] + n[1])), vi='Tứ giác \\(%s\\) có \\(%s\\). Tính \\(%s\\).' % (n, t, hat(n[3] + n[0] + n[1])),
                opts=dopt(r, a, [360 - b - d, 180 - b, 180 - d]), ans=0,
                ee='\\(\\triangle %s%s%s=\\triangle %s%s%s\\) (s.s.s.), so \\(%s=%s=(360^\\circ-%d^\\circ-%d^\\circ):2=%s\\).' % (n[1], n[0], n[3], n[1], n[2], n[3], hat(n[0]), hat(n[2]), b, d, D(a)),
                ev='\\(\\triangle %s%s%s=\\triangle %s%s%s\\) (c.c.c) nên \\(%s=%s=(360^\\circ-%d^\\circ-%d^\\circ):2=%s\\).' % (n[1], n[0], n[3], n[1], n[2], n[3], hat(n[0]), hat(n[2]), b, d, D(a)))

def b10_d3_bis(r, lv):
    n = PICK(r, NAMES)
    while True:
        c, d = r.randrange(60, 140, 2), r.randrange(50, 130, 2)
        if 60 < 360 - c - d < 250: break
    v = (c + d) // 2 if (c + d) % 2 == 0 else None
    if v is None: raise AssertionError
    I = [q for q in 'OTUV' if q not in n][0]
    t = '%s=%s,\\ %s=%s' % (hat(n[2]), D(c), hat(n[3]), D(d))
    return dict(en='In convex quadrilateral \\(%s\\), \\(%s\\). The bisectors of \\(%s\\) and \\(%s\\) meet at \\(%s\\). Find \\(%s\\).' % (n, t, hat(n[0]), hat(n[1]), I, hat(n[0] + I + n[1])),
                vi='Tứ giác lồi \\(%s\\) có \\(%s\\). Các tia phân giác của \\(%s\\) và \\(%s\\) cắt nhau tại \\(%s\\). Tính \\(%s\\).' % (n, t, hat(n[0]), hat(n[1]), I, hat(n[0] + I + n[1])),
                opts=dopt(r, v, [360 - c - d, 180 - v, (360 - c - d) // 2]), ans=0,
                ee='\\(%s+%s=360^\\circ-%d^\\circ-%d^\\circ=%d^\\circ\\), so \\(%s=180^\\circ-%d^\\circ:2=%s\\).' % (hat(n[0]), hat(n[1]), c, d, 360 - c - d, hat(n[0] + I + n[1]), 360 - c - d, D(v)),
                ev='\\(%s+%s=360^\\circ-%d^\\circ-%d^\\circ=%d^\\circ\\) nên \\(%s=180^\\circ-%d^\\circ:2=%s\\).' % (hat(n[0]), hat(n[1]), c, d, 360 - c - d, hat(n[0] + I + n[1]), 360 - c - d, D(v)))

def b10_d4_garden(r, lv):
    a, b, c, d = _angles(r, 60, 130)
    return dict(en='A surveyor measures three corners of a quadrilateral garden: \\(%s\\), \\(%s\\) and \\(%s\\). What is the fourth corner angle?' % (D(a), D(b), D(c)),
                vi='Một người đo ba góc của một mảnh vườn hình tứ giác được \\(%s\\), \\(%s\\) và \\(%s\\). Góc còn lại của mảnh vườn bằng bao nhiêu?' % (D(a), D(b), D(c)),
                opts=dopt(r, d, [180 - d, 360 - a - b, (a + b + c) // 3]), ans=0, ee='\\(360^\\circ-(%d^\\circ+%d^\\circ+%d^\\circ)=%s\\).' % (a, b, c, D(d)), ev='\\(360^\\circ-(%d^\\circ+%d^\\circ+%d^\\circ)=%s\\).' % (a, b, c, D(d)))

def b10_d4_kite(r, lv):
    while True:
        top, bot = r.randrange(50, 110, 2), r.randrange(40, 100, 2)
        if (360 - top - bot) % 2 == 0 and top != bot: break
    s = (360 - top - bot) // 2
    return dict(en='A kite frame \\(ABCD\\) has \\(AB=AD\\) and \\(CB=CD\\). The angle at the top \\(A\\) is \\(%s\\) and the angle at the bottom \\(C\\) is \\(%s\\). Find the angle at \\(B\\).' % (D(top), D(bot)),
                vi='Khung một chiếc diều là tứ giác \\(ABCD\\) có \\(AB=AD\\), \\(CB=CD\\). Góc ở đỉnh \\(A\\) bằng \\(%s\\), góc ở đỉnh \\(C\\) bằng \\(%s\\). Tính góc ở đỉnh \\(B\\).' % (D(top), D(bot)),
                opts=dopt(r, s, [360 - top - bot, 180 - top, 180 - bot]), ans=0, ee='\\(\\widehat{B}=\\widehat{D}=(360^\\circ-%d^\\circ-%d^\\circ):2=%s\\).' % (top, bot, D(s)),
                ev='\\(\\widehat{B}=\\widehat{D}=(360^\\circ-%d^\\circ-%d^\\circ):2=%s\\).' % (top, bot, D(s)))

def b10_d4_acute(r, lv):
    k = r.choice(['acute', 'obtuse', 'right'])
    if k == 'acute': q, good, bads, e = ('What is the greatest number of acute angles a quadrilateral can have?', 'Một tứ giác có nhiều nhất bao nhiêu góc nhọn?'), 3, [4, 2, 1], 'Four acute angles would add up to less than \\(360^\\circ\\); three is possible, e.g. \\(80^\\circ,80^\\circ,80^\\circ,120^\\circ\\).'
    elif k == 'obtuse': q, good, bads, e = ('What is the greatest number of obtuse angles a quadrilateral can have?', 'Một tứ giác có nhiều nhất bao nhiêu góc tù?'), 3, [4, 2, 1], 'Four obtuse angles would add up to more than \\(360^\\circ\\); three is possible, e.g. \\(100^\\circ,100^\\circ,100^\\circ,60^\\circ\\).'
    else: q, good, bads, e = ('A quadrilateral has three right angles. How many right angles does it have in total?', 'Một tứ giác có ba góc vuông. Tứ giác đó có tất cả bao nhiêu góc vuông?'), 4, [3, 2, 1], 'The fourth angle is \\(360^\\circ-270^\\circ=90^\\circ\\).'
    ev = e.replace('Four acute angles would add up to less than', 'Bốn góc nhọn có tổng nhỏ hơn').replace('; three is possible, e.g.', '; có thể có ba góc, ví dụ').replace('Four obtuse angles would add up to more than', 'Bốn góc tù có tổng lớn hơn').replace('The fourth angle is', 'Góc thứ tư bằng')
    return dict(en=q[0], vi=q[1], opts=nopt(r, good, bads), ans=0, ee=e, ev=ev)

L10_GROUPS = [[('mcq', b10_fourth), ('mcq', b10_sum), ('mcq', b10_diag)], [('tf', b10_tf_claim), ('tf', b10_tf_num)], [('short', b10_short_x), ('short', b10_short_ratio)],
              [('mcq', b10_d1_opp), ('mcq', b10_d1_side), ('mcq', b10_d1_pair)], [('mcq', b10_d2_ext), ('mcq', b10_d2_eq), ('mcq', b10_d2_small)],
              [('mcq', b10_d3_x), ('mcq', b10_d3_kite), ('mcq', b10_d3_bis)], [('mcq', b10_d4_garden), ('mcq', b10_d4_kite), ('mcq', b10_d4_acute)]]

# =====================================================================================================
# BÀI 11. HÌNH THANG CÂN    (hình thang n với n0n1 ∥ n2n3; cạnh bên n0n3 và n1n2)
# =====================================================================================================
def par(a, b): return '%s\\parallel %s' % (a, b)

def b11_iso_angles(r, lv):
    n = PICK(r, NAMES); a = r.randrange(40, 86, 2) if r.random() < .5 else r.randrange(96, 140, 2); b = 180 - a
    good = '%s=%s,\\ %s=%s=%s' % (hat(n[1]), D(a), hat(n[2]), hat(n[3]), D(b))
    bads = ['%s=%s,\\ %s=%s=%s' % (hat(n[1]), D(b), hat(n[2]), hat(n[3]), D(a)), '%s=%s,\\ %s=%s=%s' % (hat(n[1]), D(a), hat(n[2]), hat(n[3]), D(a)), '%s=%s,\\ %s=%s=%s' % (hat(n[1]), D(b), hat(n[2]), hat(n[3]), D(b))]
    return dict(en='Isosceles trapezoid \\(%s\\) has bases \\(%s%s\\) and \\(%s%s\\), and \\(%s=%s\\). Find the other angles.' % (n, n[0], n[1], n[2], n[3], hat(n[0]), D(a)),
                vi='Hình thang cân \\(%s\\) có hai đáy \\(%s%s\\), \\(%s%s\\) và \\(%s=%s\\). Tính các góc còn lại.' % (n, n[0], n[1], n[2], n[3], hat(n[0]), D(a)), opts=[good] + bads, ans=0,
                ee='Base angles are equal: \\(%s=%s\\); angles along a leg are supplementary: \\(%s=180^\\circ-%d^\\circ=%s\\).' % (hat(n[1]), hat(n[0]), hat(n[3]), a, D(b)),
                ev='Hai góc kề một đáy bằng nhau: \\(%s=%s\\); hai góc kề một cạnh bên bù nhau: \\(%s=180^\\circ-%d^\\circ=%s\\).' % (hat(n[1]), hat(n[0]), hat(n[3]), a, D(b)))

def b11_leg(r, lv):
    n = PICK(r, NAMES); a = r.randrange(40, 140, 5)
    return dict(en='Trapezoid \\(%s\\) has \\(%s\\) and \\(%s=%s\\). Find \\(%s\\).' % (n, par(n[0] + n[1], n[2] + n[3]), hat(n[0]), D(a), hat(n[3])),
                vi='Hình thang \\(%s\\) có \\(%s\\) và \\(%s=%s\\). Tính \\(%s\\).' % (n, par(n[0] + n[1], n[2] + n[3]), hat(n[0]), D(a), hat(n[3])),
                opts=dopt(r, 180 - a, [a, 360 - a, 90 - a // 2 if a < 180 else 45]), ans=0,
                ee='\\(%s\\) and \\(%s\\) are angles along leg \\(%s%s\\), so they are supplementary.' % (hat(n[0]), hat(n[3]), n[0], n[3]),
                ev='\\(%s\\) và \\(%s\\) là hai góc kề cạnh bên \\(%s%s\\) nên bù nhau.' % (hat(n[0]), hat(n[3]), n[0], n[3]))

PROP11 = [('two legs are equal', 'hai cạnh bên bằng nhau', True), ('two diagonals are equal', 'hai đường chéo bằng nhau', True), ('two base angles at the same base are equal', 'hai góc kề một đáy bằng nhau', True),
          ('two diagonals are perpendicular', 'hai đường chéo vuông góc với nhau', False), ('two bases are equal', 'hai đáy bằng nhau', False), ('two diagonals bisect each other', 'hai đường chéo cắt nhau tại trung điểm mỗi đường', False),
          ('four angles are all equal', 'bốn góc bằng nhau', False)]
def b11_prop(r, lv):
    t = [p for p in PROP11 if p[2]]; f = [p for p in PROP11 if not p[2]]
    if r.random() < .5:
        g = PICK(r, t); bads = r.sample(f, 3); q = PICK(r, [('Which statement is true for every isosceles trapezoid?', 'Khẳng định nào đúng với mọi hình thang cân?'), ('Which property does every isosceles trapezoid have?', 'Mọi hình thang cân đều có tính chất nào sau đây?')])
    else:
        g = PICK(r, f); bads = r.sample(t, 3); q = PICK(r, [('Which statement is NOT true for every isosceles trapezoid?', 'Khẳng định nào KHÔNG đúng với mọi hình thang cân?'), ('Which property does an isosceles trapezoid NOT always have?', 'Hình thang cân không nhất thiết có tính chất nào sau đây?')])
    o = [tx('Its ' + g[0] + '.', 'Có ' + g[1] + '.')] + [tx('Its ' + b[0] + '.', 'Có ' + b[1] + '.') for b in bads]
    return dict(en=q[0], vi=q[1], opts=o, ans=0, ee='An isosceles trapezoid has equal legs, equal diagonals and equal base angles.', ev='Hình thang cân có hai cạnh bên bằng nhau, hai đường chéo bằng nhau, hai góc kề một đáy bằng nhau.')

def b11_tf_prop(r, lv):
    g = PICK(r, PROP11); return dict(en='In every isosceles trapezoid, its %s.' % g[0], vi='Trong mọi hình thang cân, %s.' % g[1], ans=g[2],
                                    ee='Properties: equal legs, equal diagonals, equal base angles.', ev='Tính chất: hai cạnh bên bằng nhau, hai đường chéo bằng nhau, hai góc kề một đáy bằng nhau.')

def b11_tf_test(r, lv):
    n = PICK(r, NAMES); k = r.choice(['diag', 'angle', 'leg'])
    if k == 'diag': en, vi, t = 'Trapezoid \\(%s\\) (\\(%s\\)) has \\(%s%s=%s%s\\). Then it is an isosceles trapezoid.' % (n, par(n[0] + n[1], n[2] + n[3]), n[0], n[2], n[1], n[3]), 'Hình thang \\(%s\\) (\\(%s\\)) có \\(%s%s=%s%s\\). Khi đó nó là hình thang cân.' % (n, par(n[0] + n[1], n[2] + n[3]), n[0], n[2], n[1], n[3]), True
    elif k == 'angle': en, vi, t = 'Trapezoid \\(%s\\) (\\(%s\\)) has \\(%s=%s\\). Then it is an isosceles trapezoid.' % (n, par(n[0] + n[1], n[2] + n[3]), hat(n[2]), hat(n[3])), 'Hình thang \\(%s\\) (\\(%s\\)) có \\(%s=%s\\). Khi đó nó là hình thang cân.' % (n, par(n[0] + n[1], n[2] + n[3]), hat(n[2]), hat(n[3])), True
    else: en, vi, t = 'Trapezoid \\(%s\\) (\\(%s\\)) has \\(%s%s=%s%s\\). Then it must be an isosceles trapezoid.' % (n, par(n[0] + n[1], n[2] + n[3]), n[0], n[3], n[1], n[2]), 'Hình thang \\(%s\\) (\\(%s\\)) có \\(%s%s=%s%s\\). Khi đó nó chắc chắn là hình thang cân.' % (n, par(n[0] + n[1], n[2] + n[3]), n[0], n[3], n[1], n[2]), False
    return dict(en=en, vi=vi, ans=t, ee='Tests: equal diagonals, or equal angles at one base. Equal legs are not enough (a parallelogram also has equal legs).',
                ev='Dấu hiệu: hai đường chéo bằng nhau, hoặc hai góc kề một đáy bằng nhau. Hai cạnh bên bằng nhau thì chưa đủ (hình bình hành cũng có).')

def b11_short_angle(r, lv):
    n = PICK(r, NAMES); a = r.randrange(50, 85, 1); b = 180 - a
    return dict(en='Isosceles trapezoid \\(%s\\) (\\(%s\\)) has \\(%s=%s\\). Find \\(%s\\) in degrees.' % (n, par(n[0] + n[1], n[2] + n[3]), hat(n[1]), D(a), hat(n[3])),
                vi='Hình thang cân \\(%s\\) (\\(%s\\)) có \\(%s=%s\\). Tính số đo \\(%s\\) (theo độ).' % (n, par(n[0] + n[1], n[2] + n[3]), hat(n[1]), D(a), hat(n[3])), key=str(b),
                ee='\\(%s=%s=%s\\), so \\(%s=180^\\circ-%d^\\circ=%s\\).' % (hat(n[0]), hat(n[1]), D(a), hat(n[3]), a, D(b)), ev='\\(%s=%s=%s\\) nên \\(%s=180^\\circ-%d^\\circ=%s\\).' % (hat(n[0]), hat(n[1]), D(a), hat(n[3]), a, D(b)))

def b11_short_per(r, lv):
    n = PICK(r, NAMES); B, b, l = r.randint(8, 20), r.randint(3, 7), r.randint(4, 9)
    if b >= B: raise AssertionError
    p = B + b + 2 * l
    return dict(en='Isosceles trapezoid \\(%s\\) has bases \\(%s%s=%d\\) cm, \\(%s%s=%d\\) cm and leg \\(%s%s=%d\\) cm. Find its perimeter (cm).' % (n, n[0], n[1], B, n[2], n[3], b, n[0], n[3], l),
                vi='Hình thang cân \\(%s\\) có hai đáy \\(%s%s=%d\\) cm, \\(%s%s=%d\\) cm và cạnh bên \\(%s%s=%d\\) cm. Tính chu vi của hình thang (cm).' % (n, n[0], n[1], B, n[2], n[3], b, n[0], n[3], l), key=str(p),
                ee='\\(%s%s=%s%s=%d\\), perimeter \\(=%d+%d+2\\cdot%d=%d\\).' % (n[1], n[2], n[0], n[3], l, B, b, l, p), ev='\\(%s%s=%s%s=%d\\), chu vi \\(=%d+%d+2\\cdot%d=%d\\).' % (n[1], n[2], n[0], n[3], l, B, b, l, p))

def _trapfig(r, n, iso=True, diag=False, height=False):
    P = pts(n, shape('itrap' if iso else 'trap', r)); segs = cyc(n); dash = []; right = []
    if diag: segs = segs + [(n[0], n[2]), (n[1], n[3])]
    if height:
        H = 'H'; P[H] = (P[n[3]][0], 0); dash = [(n[3], H)]; right = [(n[3], H, n[1])]
    return QF(P, segs=segs, dash=dash, right=right)

def b11_d1_bases(r, lv):
    n = PICK(r, [x for x in NAMES if 'H' not in x]); fig = _trapfig(r, n, iso=False, height=True)
    good = '%s%s\\text{ and }%s%s' % (n[0], n[1], n[2], n[3]); bads = ['%s%s\\text{ and }%s%s' % (n[0], n[3], n[1], n[2]), '%s%s\\text{ and }%s%s' % (n[0], n[2], n[1], n[3]), '%sH\\text{ and }%s%s' % (n[3], n[0], n[1])]
    o = [tx('\\(%s\\)' % x, '\\(%s\\)' % x.replace('\\text{ and }', '\\text{ và }')) for x in [good] + bads]
    return dict(en='In trapezoid \\(%s\\) (\\(%s\\)), which segments are the bases?' % (n, par(n[0] + n[1], n[2] + n[3])), vi='Trong hình thang \\(%s\\) (\\(%s\\)), hai đáy là' % (n, par(n[0] + n[1], n[2] + n[3])), opts=o, ans=0, fig=fig,
                ee='The bases are the two parallel sides.', ev='Hai đáy là hai cạnh song song.')

def b11_d1_height(r, lv):
    n = PICK(r, [x for x in NAMES if 'H' not in x]); fig = _trapfig(r, n, iso=False, height=True)
    o = ['%sH' % n[3], '%s%s' % (n[0], n[3]), '%s%s' % (n[1], n[2]), '%s%s' % (n[0], n[2])]
    return dict(en='In trapezoid \\(%s\\) (\\(%s\\)), which segment is a height?' % (n, par(n[0] + n[1], n[2] + n[3])), vi='Trong hình thang \\(%s\\) (\\(%s\\)), đoạn thẳng nào là một đường cao?' % (n, par(n[0] + n[1], n[2] + n[3])), opts=o, ans=0, fig=fig,
                ee='\\(%sH\\perp %s%s\\).' % (n[3], n[0], n[1]), ev='\\(%sH\\perp %s%s\\).' % (n[3], n[0], n[1]))

def b11_d1_diag(r, lv):
    n = PICK(r, NAMES); fig = _trapfig(r, n, iso=True, diag=True); d = r.randint(5, 15)
    return dict(en='Isosceles trapezoid \\(%s\\) (\\(%s\\)) has \\(%s%s=%d\\) cm. Find \\(%s%s\\).' % (n, par(n[0] + n[1], n[2] + n[3]), n[0], n[2], d, n[1], n[3]),
                vi='Hình thang cân \\(%s\\) (\\(%s\\)) có \\(%s%s=%d\\) cm. Tính \\(%s%s\\).' % (n, par(n[0] + n[1], n[2] + n[3]), n[0], n[2], d, n[1], n[3]),
                opts=nopt(r, d, [2 * d, d + 2, d - 3], unit='\\text{ cm}'), ans=0, fig=fig, ee='The diagonals of an isosceles trapezoid are equal.', ev='Hình thang cân có hai đường chéo bằng nhau.')

def b11_d2_x(r, lv):
    n = PICK(r, NAMES)
    while True:
        k1, k2 = r.randint(2, 4), r.randint(5, 7); x = r.randint(8, 25); c1 = r.randrange(-20, 40, 5); c2 = (k1 - k2) * x + c1
        a = k1 * x + c1
        if 40 < a < 140 and -60 <= c2 <= 60: break
    def e(k, c): return '(%dx%s)^\\circ' % (k, '' if c == 0 else ('+%d' % c if c > 0 else '%d' % c))
    return dict(en='Isosceles trapezoid \\(%s\\) (\\(%s\\)) has \\(%s=%s\\) and \\(%s=%s\\). Find \\(%s\\).' % (n, par(n[0] + n[1], n[2] + n[3]), hat(n[0]), e(k1, c1), hat(n[1]), e(k2, c2), hat(n[0])),
                vi='Hình thang cân \\(%s\\) (\\(%s\\)) có \\(%s=%s\\) và \\(%s=%s\\). Tính \\(%s\\).' % (n, par(n[0] + n[1], n[2] + n[3]), hat(n[0]), e(k1, c1), hat(n[1]), e(k2, c2), hat(n[0])),
                opts=dopt(r, a, [x, 180 - a, k2 * x]), ans=0, ee='Equal base angles: \\(%dx%+d=%dx%+d\\Rightarrow x=%d\\), so \\(%s=%s\\).' % (k1, c1, k2, c2, x, hat(n[0]), D(a)),
                ev='Hai góc kề một đáy bằng nhau: \\(%dx%+d=%dx%+d\\Rightarrow x=%d\\), nên \\(%s=%s\\).' % (k1, c1, k2, c2, x, hat(n[0]), D(a)))

def b11_d2_diff(r, lv):
    n = PICK(r, NAMES); dlt = r.randrange(10, 80, 10); a = (180 + dlt) // 2; d = 180 - a
    return dict(en='Trapezoid \\(%s\\) (\\(%s\\)) has \\(%s-%s=%s\\). Find \\(%s\\).' % (n, par(n[0] + n[1], n[2] + n[3]), hat(n[3]), hat(n[0]), D(dlt), hat(n[3])),
                vi='Hình thang \\(%s\\) (\\(%s\\)) có \\(%s-%s=%s\\). Tính \\(%s\\).' % (n, par(n[0] + n[1], n[2] + n[3]), hat(n[3]), hat(n[0]), D(dlt), hat(n[3])),
                opts=dopt(r, a, [d, 180 - dlt, a + dlt]), ans=0, ee='\\(%s+%s=180^\\circ\\) and their difference is \\(%d^\\circ\\): \\(%s=(180^\\circ+%d^\\circ):2=%s\\).' % (hat(n[3]), hat(n[0]), dlt, hat(n[3]), dlt, D(a)),
                ev='\\(%s+%s=180^\\circ\\), hiệu bằng \\(%d^\\circ\\) nên \\(%s=(180^\\circ+%d^\\circ):2=%s\\).' % (hat(n[3]), hat(n[0]), dlt, hat(n[3]), dlt, D(a)))

def b11_d2_per(r, lv):
    n = PICK(r, NAMES); B, b, l = r.randint(10, 24), r.randint(4, 9), r.randint(5, 10); p = B + b + 2 * l
    return dict(en='Isosceles trapezoid \\(%s\\) has perimeter %d cm and bases %d cm and %d cm. Find the length of each leg.' % (n, p, B, b),
                vi='Hình thang cân \\(%s\\) có chu vi %d cm, hai đáy dài %d cm và %d cm. Tính độ dài mỗi cạnh bên.' % (n, p, B, b),
                opts=nopt(r, l, [2 * l, p - B - b, l + 2], unit='\\text{ cm}'), ans=0, ee='\\((%d-%d-%d):2=%d\\) cm.' % (p, B, b, l), ev='\\((%d-%d-%d):2=%d\\) cm.' % (p, B, b, l))

def b11_d3_tri(r, lv):
    s = r.randrange(40, 86, 2); U = 180 - s
    return dict(en='Triangle \\(RST\\) has \\(RS=RT\\) and \\(\\widehat{S}=%s\\). Points \\(U\\in RS\\), \\(V\\in RT\\) with \\(UV\\parallel ST\\). Quadrilateral \\(UVTS\\) is an isosceles trapezoid. Find \\(\\widehat{SUV}\\).' % D(s),
                vi='Tam giác \\(RST\\) có \\(RS=RT\\) và \\(\\widehat{S}=%s\\). Lấy \\(U\\in RS\\), \\(V\\in RT\\) sao cho \\(UV\\parallel ST\\). Tứ giác \\(UVTS\\) là hình thang cân. Tính \\(\\widehat{SUV}\\).' % D(s),
                opts=dopt(r, U, [s, 180 - 2 * s if 180 - 2 * s > 0 else 90 - s, 90 + s // 2]), ans=0, ee='\\(UV\\parallel ST\\): \\(\\widehat{SUV}+\\widehat{S}=180^\\circ\\Rightarrow\\widehat{SUV}=%s\\).' % D(U),
                ev='\\(UV\\parallel ST\\) nên \\(\\widehat{SUV}+\\widehat{S}=180^\\circ\\Rightarrow\\widehat{SUV}=%s\\).' % D(U))

def b11_d3_bis(r, lv):
    n = PICK(r, NAMES); a = r.randint(4, 12); c = r.randint(a + 3, 2 * a + 8)
    return dict(en='Trapezoid \\(%s\\) (\\(%s\\)) has \\(%s%s=%d\\) cm. Diagonal \\(%s%s\\) bisects \\(%s\\). Find \\(%s%s\\).' % (n, par(n[0] + n[1], n[2] + n[3]), n[2], n[3], a, n[0], n[2], hat(n[3] + n[0] + n[1]), n[3], n[0]),
                vi='Hình thang \\(%s\\) (\\(%s\\)) có \\(%s%s=%d\\) cm, đường chéo \\(%s%s\\) là tia phân giác của \\(%s\\). Tính \\(%s%s\\).' % (n, par(n[0] + n[1], n[2] + n[3]), n[2], n[3], a, n[0], n[2], hat(n[3] + n[0] + n[1]), n[3], n[0]),
                opts=nopt(r, a, [2 * a, a + 3, c], unit='\\text{ cm}'), ans=0,
                ee='\\(%s=%s\\) (alternate angles) \\(=%s\\), so \\(\\triangle %s%s%s\\) is isosceles: \\(%s%s=%s%s=%d\\) cm.' % (hat(n[3] + n[2] + n[0]), hat(n[2] + n[0] + n[1]), hat(n[3] + n[0] + n[2]), n[0], n[3], n[2], n[3], n[0], n[2], n[3], a),
                ev='\\(%s=%s\\) (so le trong) \\(=%s\\) nên \\(\\triangle %s%s%s\\) cân tại \\(%s\\): \\(%s%s=%s%s=%d\\) cm.' % (hat(n[3] + n[2] + n[0]), hat(n[2] + n[0] + n[1]), hat(n[3] + n[0] + n[2]), n[0], n[3], n[2], n[3], n[3], n[0], n[2], n[3], a))

def b11_d3_x(r, lv):
    n = PICK(r, NAMES)
    while True:
        k1, k2 = r.randint(1, 3), r.randint(1, 3); c1 = r.randrange(0, 50, 5); x = r.randrange(20, 60, 5); c2 = 180 - (k1 + k2) * x - c1
        if -40 <= c2 <= 60 and 30 < k1 * x + c1 < 150: break
    def e(k, c): return '(%sx%s)^\\circ' % ('' if k == 1 else k, '' if c == 0 else ('+%d' % c if c > 0 else '%d' % c)) if c else ('%sx^\\circ' % ('' if k == 1 else k))
    a = k1 * x + c1
    return dict(en='Trapezoid \\(%s\\) (\\(%s\\)) has \\(%s=%s\\) and \\(%s=%s\\). Find \\(%s\\).' % (n, par(n[0] + n[1], n[2] + n[3]), hat(n[0]), e(k1, c1), hat(n[3]), e(k2, c2), hat(n[0])),
                vi='Hình thang \\(%s\\) (\\(%s\\)) có \\(%s=%s\\) và \\(%s=%s\\). Tính \\(%s\\).' % (n, par(n[0] + n[1], n[2] + n[3]), hat(n[0]), e(k1, c1), hat(n[3]), e(k2, c2), hat(n[0])),
                opts=dopt(r, a, [x, 180 - a, a + 10]), ans=0, ee='\\(%s+%s=180^\\circ\\Rightarrow %dx%+d=180\\Rightarrow x=%d\\); \\(%s=%s\\).' % (hat(n[0]), hat(n[3]), k1 + k2, c1 + c2, x, hat(n[0]), D(a)),
                ev='\\(%s+%s=180^\\circ\\Rightarrow %dx%+d=180\\Rightarrow x=%d\\); \\(%s=%s\\).' % (hat(n[0]), hat(n[3]), k1 + k2, c1 + c2, x, hat(n[0]), D(a)))

def b11_d4_bridge(r, lv):
    a = r.randrange(50, 76, 5); AB, CD, l = r.randint(6, 12), r.randint(14, 24), r.randint(4, 8)
    q = r.choice(['angle', 'per'])
    if q == 'angle':
        return dict(en='The side frame of a pedestrian bridge is trapezoid \\(ABCD\\) with \\(AB\\parallel CD\\) and \\(\\widehat{C}=\\widehat{D}=%s\\). Find the angle \\(\\widehat{DAB}\\) at the upper base.' % D(a),
                    vi='Khung một mặt bên của cầu đi bộ là hình thang \\(ABCD\\) (\\(AB\\parallel CD\\)) có \\(\\widehat{C}=\\widehat{D}=%s\\). Tính góc \\(\\widehat{DAB}\\) ở đáy trên.' % D(a),
                    opts=dopt(r, 180 - a, [a, 90 + a // 2, 2 * a]), ans=0, ee='\\(\\widehat{DAB}=180^\\circ-%d^\\circ=%s\\).' % (a, D(180 - a)), ev='\\(\\widehat{DAB}=180^\\circ-%d^\\circ=%s\\).' % (a, D(180 - a)))
    a = 60; CD = AB + l                     # góc đáy 60°: hình chiếu mỗi cạnh bên = l/2 nên CD = AB + l
    p = AB + CD + 2 * l
    return dict(en='The side frame of a pedestrian bridge is trapezoid \\(ABCD\\) (\\(AB\\parallel CD\\)) with \\(\\widehat{C}=\\widehat{D}=%s\\), \\(AB=%d\\) m, \\(CD=%d\\) m, \\(AD=%d\\) m. How many meters of steel are needed for its four sides?' % (D(a), AB, CD, l),
                vi='Khung một mặt bên của cầu đi bộ là hình thang \\(ABCD\\) (\\(AB\\parallel CD\\)) có \\(\\widehat{C}=\\widehat{D}=%s\\), \\(AB=%d\\) m, \\(CD=%d\\) m, \\(AD=%d\\) m. Cần bao nhiêu mét thép để làm bốn cạnh của khung?' % (D(a), AB, CD, l),
                opts=nopt(r, p, [AB + CD + l, AB + CD + 2 * l + 2, 2 * (AB + CD)], unit='\\text{ m}'), ans=0, ee='Isosceles trapezoid, so \\(BC=AD=%d\\) m; total \\(%d\\) m.' % (l, p), ev='Hình thang cân nên \\(BC=AD=%d\\) m; tổng \\(%d\\) m.' % (l, p))

def b11_d4_field(r, lv):
    a, b, h = r.randrange(20, 60, 2), r.randrange(10, 40, 2), r.randint(8, 30)
    if b >= a: a, b = b + 10, a
    S = (a + b) * h // 2
    if (a + b) * h % 2: raise AssertionError
    return dict(en='A field has the shape of a trapezoid with bases %d m and %d m and height %d m. Find its area.' % (a, b, h), vi='Một thửa ruộng có dạng hình thang với hai đáy dài %d m, %d m và chiều cao %d m. Tính diện tích thửa ruộng.' % (a, b, h),
                opts=nopt(r, S, [(a + b) * h, a * h, S + h], unit='\\text{ m}^2'), ans=0, ee='\\(S=\\dfrac{(%d+%d)\\cdot%d}{2}=%d\\) m².' % (a, b, h, S), ev='\\(S=\\dfrac{(%d+%d)\\cdot%d}{2}=%d\\) m².' % (a, b, h, S))

def b11_d4_roof(r, lv):
    a = r.randrange(30, 61, 5); top = 180 - a
    return dict(en='The front of a roof is an isosceles trapezoid. Each lower corner is \\(%s\\). What is each upper corner?' % D(a), vi='Mặt trước của một mái nhà có dạng hình thang cân, mỗi góc ở đáy dưới bằng \\(%s\\). Mỗi góc ở đáy trên bằng bao nhiêu?' % D(a),
                opts=dopt(r, top, [a, 90 + a, 2 * a]), ans=0, ee='\\(180^\\circ-%d^\\circ=%s\\).' % (a, D(top)), ev='\\(180^\\circ-%d^\\circ=%s\\).' % (a, D(top)))

L11_GROUPS = [[('mcq', b11_iso_angles), ('mcq', b11_leg), ('mcq', b11_prop)], [('tf', b11_tf_prop), ('tf', b11_tf_test)], [('short', b11_short_angle), ('short', b11_short_per)],
              [('mcq', b11_d1_bases), ('mcq', b11_d1_height), ('mcq', b11_d1_diag)], [('mcq', b11_d2_x), ('mcq', b11_d2_diff), ('mcq', b11_d2_per)],
              [('mcq', b11_d3_tri), ('mcq', b11_d3_bis), ('mcq', b11_d3_x)], [('mcq', b11_d4_bridge), ('mcq', b11_d4_field), ('mcq', b11_d4_roof)]]

# =====================================================================================================
# BÀI 12. HÌNH BÌNH HÀNH
# =====================================================================================================
def _cname(n): return [q for q in 'OIT' if q not in n][0]

def b12_angles(r, lv):
    n = PICK(r, NAMES); a = r.randrange(40, 140, 2)
    if a == 90: a = 72
    good = '%s=%s,\\ %s=%s=%s' % (hat(n[2]), D(a), hat(n[1]), hat(n[3]), D(180 - a))
    bads = ['%s=%s,\\ %s=%s=%s' % (hat(n[2]), D(180 - a), hat(n[1]), hat(n[3]), D(a)), '%s=%s,\\ %s=%s=%s' % (hat(n[2]), D(a), hat(n[1]), hat(n[3]), D(a)), '%s=%s,\\ %s=%s=%s' % (hat(n[2]), D(90), hat(n[1]), hat(n[3]), D(90))]
    return dict(en='Parallelogram \\(%s\\) has \\(%s=%s\\). Find the other angles.' % (n, hat(n[0]), D(a)), vi='Hình bình hành \\(%s\\) có \\(%s=%s\\). Tính các góc còn lại.' % (n, hat(n[0]), D(a)),
                opts=[good] + bads, ans=0, ee='Opposite angles are equal; consecutive angles are supplementary.', ev='Hai góc đối bằng nhau; hai góc kề một cạnh bù nhau.')

def b12_diag(r, lv):
    n = PICK(r, NAMES); O = _cname(n); a, b = r.randint(2, 9), r.randint(2, 9)
    if a == b: b += 1
    P = pts(n, shape('para', r)); P[O] = ((P[n[0]][0] + P[n[2]][0]) / 2, (P[n[0]][1] + P[n[2]][1]) / 2)
    fig = QF(P, segs=cyc(n) + [(n[0], n[2]), (n[1], n[3])])
    good = '%s%s=%d\\text{ cm},\\ %s%s=%d\\text{ cm}' % (n[0], n[2], 2 * a, n[1], n[3], 2 * b)
    bads = ['%s%s=%d\\text{ cm},\\ %s%s=%d\\text{ cm}' % (n[0], n[2], a, n[1], n[3], b), '%s%s=%d\\text{ cm},\\ %s%s=%d\\text{ cm}' % (n[0], n[2], 2 * a, n[1], n[3], 2 * a), '%s%s=%d\\text{ cm},\\ %s%s=%d\\text{ cm}' % (n[0], n[2], a + b, n[1], n[3], a + b)]
    return dict(en='The diagonals of parallelogram \\(%s\\) meet at \\(%s\\), with \\(%s%s=%d\\) cm and \\(%s%s=%d\\) cm. Find the diagonals.' % (n, O, O, n[0], a, O, n[1], b),
                vi='Hai đường chéo của hình bình hành \\(%s\\) cắt nhau tại \\(%s\\), biết \\(%s%s=%d\\) cm, \\(%s%s=%d\\) cm. Tính độ dài hai đường chéo.' % (n, O, O, n[0], a, O, n[1], b),
                opts=pick_opts(r, good, bads), ans=0, fig=fig, ee='\\(%s\\) is the midpoint of both diagonals.' % O, ev='\\(%s\\) là trung điểm của mỗi đường chéo.' % O)

TEST12 = [('both pairs of opposite sides are parallel', 'các cạnh đối song song', True), ('both pairs of opposite sides are equal', 'các cạnh đối bằng nhau', True),
          ('one pair of opposite sides is parallel and equal', 'hai cạnh đối song song và bằng nhau', True), ('both pairs of opposite angles are equal', 'các góc đối bằng nhau', True),
          ('the diagonals bisect each other', 'hai đường chéo cắt nhau tại trung điểm của mỗi đường', True),
          ('the diagonals are equal', 'hai đường chéo bằng nhau', False), ('one pair of opposite sides is parallel', 'có một cặp cạnh đối song song', False),
          ('the diagonals are perpendicular', 'hai đường chéo vuông góc', False), ('two adjacent sides are equal', 'hai cạnh kề bằng nhau', False), ('one pair of opposite sides is parallel and the other pair is equal', 'một cặp cạnh đối song song, cặp còn lại bằng nhau', False)]
def b12_test(r, lv):
    g = PICK(r, [t for t in TEST12 if t[2]]); bads = r.sample([t for t in TEST12 if not t[2]], 3)
    q = PICK(r, [('A quadrilateral is a parallelogram if…', 'Một tứ giác là hình bình hành nếu'), ('Which condition guarantees that a quadrilateral is a parallelogram?', 'Điều kiện nào đảm bảo một tứ giác là hình bình hành?'),
                 ('Which of these is a test for a parallelogram?', 'Đâu là một dấu hiệu nhận biết hình bình hành?'), ('Choose the condition that makes quadrilateral \\(ABCD\\) a parallelogram.', 'Chọn điều kiện để tứ giác \\(ABCD\\) là hình bình hành.')])
    o = [tx(g[0], g[1])] + [tx(b[0], b[1]) for b in bads]
    return dict(en=q[0], vi=q[1], opts=o, ans=0, ee='Tests: opposite sides parallel / equal; one pair parallel and equal; opposite angles equal; diagonals bisect each other.',
                ev='Dấu hiệu: các cạnh đối song song / bằng nhau; hai cạnh đối song song và bằng nhau; các góc đối bằng nhau; hai đường chéo cắt nhau tại trung điểm mỗi đường.')

PROP12 = [('the opposite sides are equal', 'các cạnh đối bằng nhau', True), ('the opposite angles are equal', 'các góc đối bằng nhau', True), ('the diagonals bisect each other', 'hai đường chéo cắt nhau tại trung điểm của mỗi đường', True),
          ('two consecutive angles are supplementary', 'hai góc kề một cạnh bù nhau', True), ('the diagonals are equal', 'hai đường chéo bằng nhau', False), ('the diagonals are perpendicular', 'hai đường chéo vuông góc với nhau', False),
          ('all sides are equal', 'tất cả các cạnh bằng nhau', False), ('each diagonal bisects two angles', 'mỗi đường chéo là phân giác của hai góc', False)]
def b12_tf_prop(r, lv):
    g = PICK(r, PROP12); return dict(en='In every parallelogram, %s.' % g[0], vi='Trong mọi hình bình hành, %s.' % g[1], ans=g[2],
                                    ee='Properties: opposite sides equal, opposite angles equal, diagonals bisect each other.', ev='Tính chất: các cạnh đối bằng nhau, các góc đối bằng nhau, hai đường chéo cắt nhau tại trung điểm mỗi đường.')

def b12_tf_num(r, lv):
    n = PICK(r, NAMES); a = r.randrange(40, 140, 5); truth = r.random() < .5; claim = 180 - a if truth else a
    if a == 90: claim = 90; truth = True
    return dict(en='Parallelogram \\(%s\\) has \\(%s=%s\\). Then \\(%s=%s\\).' % (n, hat(n[0]), D(a), hat(n[1]), D(claim)), vi='Hình bình hành \\(%s\\) có \\(%s=%s\\). Khi đó \\(%s=%s\\).' % (n, hat(n[0]), D(a), hat(n[1]), D(claim)),
                ans=(claim == 180 - a), ee='\\(%s=180^\\circ-%s=%s\\).' % (hat(n[1]), D(a), D(180 - a)), ev='\\(%s=180^\\circ-%s=%s\\).' % (hat(n[1]), D(a), D(180 - a)))

def b12_short_x(r, lv):
    n = PICK(r, NAMES)
    while True:
        k1, k2 = r.randint(1, 3), r.randint(4, 6); x = r.randint(2, 9); c1 = r.randint(1, 12); c2 = (k1 - k2) * x + c1
        if c2 < 0: break
    def e(k, c): return '%sx%s' % ('' if k == 1 else k, '' if c == 0 else ('+%d' % c if c > 0 else '%d' % c))
    return dict(en='Parallelogram \\(%s\\) has \\(%s%s=%s\\) and \\(%s%s=%s\\) (cm). Find \\(x\\).' % (n, n[0], n[1], e(k1, c1), n[2], n[3], e(k2, c2)),
                vi='Hình bình hành \\(%s\\) có \\(%s%s=%s\\) và \\(%s%s=%s\\) (cm). Tìm \\(x\\).' % (n, n[0], n[1], e(k1, c1), n[2], n[3], e(k2, c2)), key=str(x),
                ee='Opposite sides are equal: \\(%s=%s\\Rightarrow x=%d\\).' % (e(k1, c1), e(k2, c2), x), ev='Hai cạnh đối bằng nhau: \\(%s=%s\\Rightarrow x=%d\\).' % (e(k1, c1), e(k2, c2), x))

def b12_short_ang(r, lv):
    n = PICK(r, NAMES); a = r.randrange(41, 139); i = r.choice([1, 2, 3]); v = a if i == 2 else 180 - a
    return dict(en='Parallelogram \\(%s\\) has \\(%s=%s\\). Find \\(%s\\) in degrees.' % (n, hat(n[0]), D(a), hat(n[i])), vi='Hình bình hành \\(%s\\) có \\(%s=%s\\). Tính số đo \\(%s\\) (theo độ).' % (n, hat(n[0]), D(a), hat(n[i])), key=str(v),
                ee='\\(%s=%s\\).' % (hat(n[i]), D(v)), ev='\\(%s=%s\\).' % (hat(n[i]), D(v)))

def b12_d1_opp(r, lv):
    n = PICK(r, NAMES); i = r.randrange(4); good = hat(n[(i + 2) % 4]); o = [good, hat(n[(i + 1) % 4]), hat(n[(i + 3) % 4]), hat(n[(i + 1) % 4] + n[(i + 2) % 4] + n[i])]   # góc giữa cạnh và đường chéo tại đỉnh đối, chỉ là một phần của góc đúng
    return dict(en='In parallelogram \\(%s\\), which angle is equal to \\(%s\\)?' % (n, hat(n[i])), vi='Trong hình bình hành \\(%s\\), góc nào bằng \\(%s\\)?' % (n, hat(n[i])), opts=o, ans=0,
                ee='Opposite angles of a parallelogram are equal.', ev='Hình bình hành có các góc đối bằng nhau.')

def b12_d1_side(r, lv):
    n = PICK(r, NAMES); i = r.randrange(4); s = n[i] + n[(i + 1) % 4]; good = n[(i + 2) % 4] + n[(i + 3) % 4]
    P = pts(n, shape('para', r)); fig = QF(P, segs=cyc(n))
    o = [good, n[(i + 1) % 4] + n[(i + 2) % 4], n[(i + 3) % 4] + n[i], n[i] + n[(i + 2) % 4]]
    return dict(en='In parallelogram \\(%s\\), which side is equal and parallel to \\(%s\\)?' % (n, s), vi='Trong hình bình hành \\(%s\\), cạnh nào song song và bằng \\(%s\\)?' % (n, s), opts=o, ans=0, fig=fig,
                ee='Opposite sides are parallel and equal.', ev='Hai cạnh đối song song và bằng nhau.')

def b12_d1_mid(r, lv):
    n = PICK(r, NAMES); O = _cname(n); P = pts(n, shape('para', r)); P[O] = ((P[n[0]][0] + P[n[2]][0]) / 2, (P[n[0]][1] + P[n[2]][1]) / 2)
    fig = QF(P, segs=cyc(n) + [(n[0], n[2]), (n[1], n[3])])
    good = '%s%s=%s%s,\\ %s%s=%s%s' % (O, n[0], O, n[2], O, n[1], O, n[3]); bads = ['%s%s=%s%s,\\ %s%s=%s%s' % (O, n[0], O, n[1], O, n[2], O, n[3]), '%s%s=%s%s' % (n[0], n[2], n[1], n[3]), '%s%s\\perp %s%s' % (n[0], n[2], n[1], n[3])]
    return dict(en='The diagonals of parallelogram \\(%s\\) meet at \\(%s\\). Which statement is always true?' % (n, O), vi='Hai đường chéo của hình bình hành \\(%s\\) cắt nhau tại \\(%s\\). Khẳng định nào luôn đúng?' % (n, O),
                opts=[good] + bads, ans=0, fig=fig, ee='The diagonals bisect each other.', ev='Hai đường chéo cắt nhau tại trung điểm của mỗi đường.')

def b12_d2_cons(r, lv):
    n = PICK(r, NAMES)
    while True:
        k1, k2 = r.randint(2, 4), r.randint(3, 6); x = r.randint(10, 25); c1 = r.randrange(-20, 30, 2); c2 = 180 - (k1 + k2) * x - c1
        a = k1 * x + c1
        if -40 <= c2 <= 40 and 30 < a < 150 and a != 90: break
    def e(k, c): return '(%dx%s)^\\circ' % (k, '' if c == 0 else ('+%d' % c if c > 0 else '%d' % c)) if c else '%dx^\\circ' % k
    return dict(en='Parallelogram \\(%s\\) has \\(%s=%s\\) and \\(%s=%s\\). Find \\(%s\\).' % (n, hat(n[0]), e(k1, c1), hat(n[1]), e(k2, c2), hat(n[2])),
                vi='Hình bình hành \\(%s\\) có \\(%s=%s\\) và \\(%s=%s\\). Tính \\(%s\\).' % (n, hat(n[0]), e(k1, c1), hat(n[1]), e(k2, c2), hat(n[2])),
                opts=dopt(r, a, [180 - a, x, 90]), ans=0, ee='\\(%s+%s=180^\\circ\\Rightarrow x=%d\\); \\(%s=%s=%s\\).' % (hat(n[0]), hat(n[1]), x, hat(n[2]), hat(n[0]), D(a)),
                ev='\\(%s+%s=180^\\circ\\Rightarrow x=%d\\); \\(%s=%s=%s\\).' % (hat(n[0]), hat(n[1]), x, hat(n[2]), hat(n[0]), D(a)))

def b12_d2_per(r, lv):
    n = PICK(r, NAMES); a, b = r.randint(4, 15), r.randint(3, 12); k = r.choice(['per', 'side'])
    if k == 'per':
        return dict(en='Parallelogram \\(%s\\) has \\(%s%s=%d\\) cm and \\(%s%s=%d\\) cm. Find its perimeter.' % (n, n[0], n[1], a, n[1], n[2], b), vi='Hình bình hành \\(%s\\) có \\(%s%s=%d\\) cm, \\(%s%s=%d\\) cm. Tính chu vi của nó.' % (n, n[0], n[1], a, n[1], n[2], b),
                    opts=nopt(r, 2 * (a + b), [a + b, a * b, 2 * a + b], unit='\\text{ cm}'), ans=0, ee='\\(2(%d+%d)=%d\\) cm.' % (a, b, 2 * (a + b)), ev='\\(2(%d+%d)=%d\\) cm.' % (a, b, 2 * (a + b)))
    return dict(en='Parallelogram \\(%s\\) has perimeter %d cm and \\(%s%s=%d\\) cm. Find \\(%s%s\\).' % (n, 2 * (a + b), n[0], n[1], a, n[0], n[3]), vi='Hình bình hành \\(%s\\) có chu vi %d cm và \\(%s%s=%d\\) cm. Tính \\(%s%s\\).' % (n, 2 * (a + b), n[0], n[1], a, n[0], n[3]),
                opts=nopt(r, b, [2 * (a + b) - a, 2 * (a + b) - 2 * a, a], unit='\\text{ cm}'), ans=0, ee='\\(%s%s=%d:2-%d=%d\\) cm.' % (n[0], n[3], 2 * (a + b), a, b), ev='\\(%s%s=%d:2-%d=%d\\) cm.' % (n[0], n[3], 2 * (a + b), a, b))

def b12_d2_halves(r, lv):
    n = PICK(r, NAMES); O = _cname(n)
    while True:
        k1, k2 = r.randint(1, 3), r.randint(2, 5); x = r.randint(2, 8); c1 = r.randint(1, 9); c2 = (k1 - k2) * x + c1
        if k1 != k2 and c2 != 0 and k2 * x + c2 > 0: break
    def e(k, c): return '%sx%s' % ('' if k == 1 else k, '' if c == 0 else ('+%d' % c if c > 0 else '%d' % c))
    v = 2 * (k1 * x + c1)
    return dict(en='The diagonals of parallelogram \\(%s\\) meet at \\(%s\\), with \\(%s%s=%s\\) and \\(%s%s=%s\\) (cm). Find \\(%s%s\\).' % (n, O, O, n[0], e(k1, c1), O, n[2], e(k2, c2), n[0], n[2]),
                vi='Hai đường chéo của hình bình hành \\(%s\\) cắt nhau tại \\(%s\\), biết \\(%s%s=%s\\), \\(%s%s=%s\\) (cm). Tính \\(%s%s\\).' % (n, O, O, n[0], e(k1, c1), O, n[2], e(k2, c2), n[0], n[2]),
                opts=nopt(r, v, [v // 2, x, v + 2], unit='\\text{ cm}'), ans=0, ee='\\(%s=%s\\Rightarrow x=%d\\); \\(%s%s=2\\cdot%d=%d\\) cm.' % (e(k1, c1), e(k2, c2), x, n[0], n[2], v // 2, v),
                ev='\\(%s=%s\\Rightarrow x=%d\\); \\(%s%s=2\\cdot%d=%d\\) cm.' % (e(k1, c1), e(k2, c2), x, n[0], n[2], v // 2, v))

def b12_d3_diff(r, lv):
    n = PICK(r, NAMES); dlt = r.randrange(10, 100, 10); a = (180 + dlt) // 2
    return dict(en='Parallelogram \\(%s\\) has \\(%s-%s=%s\\). Find \\(%s\\).' % (n, hat(n[0]), hat(n[1]), D(dlt), hat(n[2])), vi='Hình bình hành \\(%s\\) có \\(%s-%s=%s\\). Tính \\(%s\\).' % (n, hat(n[0]), hat(n[1]), D(dlt), hat(n[2])),
                opts=dopt(r, a, [180 - a, dlt, a + dlt]), ans=0, ee='\\(%s+%s=180^\\circ\\Rightarrow %s=%s\\), and \\(%s=%s\\).' % (hat(n[0]), hat(n[1]), hat(n[0]), D(a), hat(n[2]), hat(n[0])),
                ev='\\(%s+%s=180^\\circ\\Rightarrow %s=%s\\), mà \\(%s=%s\\).' % (hat(n[0]), hat(n[1]), hat(n[0]), D(a), hat(n[2]), hat(n[0])))

def b12_d3_ratio(r, lv):
    n = PICK(r, NAMES); k = r.choice([2, 3]); b = r.randint(3, 10); a = k * b; p = 2 * (a + b)
    return dict(en='Parallelogram \\(%s\\) has \\(%s%s=%d\\,%s%s\\) and perimeter %d cm. Find \\(%s%s\\).' % (n, n[0], n[1], k, n[1], n[2], p, n[0], n[1]),
                vi='Hình bình hành \\(%s\\) có \\(%s%s=%d\\,%s%s\\) và chu vi %d cm. Tính \\(%s%s\\).' % (n, n[0], n[1], k, n[1], n[2], p, n[0], n[1]),
                opts=nopt(r, a, [b, p // 2, p // (k + 1)], unit='\\text{ cm}'), ans=0, ee='\\(%s%s+%s%s=%d\\); \\(%d\\) parts → one part \\(%d\\) cm; \\(%s%s=%d\\) cm.' % (n[0], n[1], n[1], n[2], p // 2, k + 1, b, n[0], n[1], a),
                ev='\\(%s%s+%s%s=%d\\); chia thành \\(%d\\) phần, mỗi phần \\(%d\\) cm; \\(%s%s=%d\\) cm.' % (n[0], n[1], n[1], n[2], p // 2, k + 1, b, n[0], n[1], a))

def b12_d3_which(r, lv):
    n = PICK(r, NAMES); O = _cname(n); a, b = r.randint(3, 9), r.randint(3, 9)
    good = '%s%s\\parallel %s%s,\\ %s%s=%s%s=%d\\text{ cm}' % (n[0], n[1], n[2], n[3], n[0], n[1], n[2], n[3], a)
    bads = ['%s%s\\parallel %s%s,\\ %s%s=%s%s=%d\\text{ cm}' % (n[0], n[1], n[2], n[3], n[1], n[2], n[3], n[0], b),
            '%s%s=%s%s=%d\\text{ cm},\\ %s%s=%s%s' % (n[0], n[1], n[1], n[2], a, n[2], n[3], n[3], n[0]),
            '%s%s=%s%s,\\ %s=%s' % (n[0], n[2], n[1], n[3], hat(n[0]), hat(n[1]))]
    return dict(en='Which data guarantee that quadrilateral \\(%s\\) is a parallelogram?' % n, vi='Với dữ kiện nào thì tứ giác \\(%s\\) chắc chắn là hình bình hành?' % n, opts=[good] + bads, ans=0,
                ee='One pair of opposite sides that is both parallel and equal is enough.', ev='Một cặp cạnh đối vừa song song vừa bằng nhau là đủ.')

def b12_d4_lift(r, lv):
    Q = PICK(r, [('A vehicle lift has two equal arms that stay parallel, attached to the ground and to the platform. Why does the platform stay parallel to the ground?', 'Bệ nâng ô tô có hai tay nâng bằng nhau và luôn song song, gắn với mặt đất và sàn nâng. Vì sao sàn nâng luôn song song với mặt đất?'),
                 ('In a folding lamp arm, two equal bars stay parallel. Why is the lamp head always kept at the same direction?', 'Cánh tay đèn bàn gấp có hai thanh bằng nhau luôn song song. Vì sao đầu đèn luôn giữ nguyên hướng?'),
                 ('A balance with two equal parallel rods keeps both pans level. Which shape explains this?', 'Một chiếc cân có hai thanh bằng nhau, song song giữ cho hai đĩa cân luôn nằm ngang. Hình nào giải thích điều này?')])
    o = [tx('The four joints form a parallelogram (one pair of opposite sides parallel and equal).', 'Bốn điểm khớp tạo thành hình bình hành (một cặp cạnh đối song song và bằng nhau).'),
         tx('The four joints form a trapezoid.', 'Bốn điểm khớp tạo thành hình thang.'), tx('The arms are perpendicular to the ground.', 'Các tay nâng vuông góc với mặt đất.'), tx('The diagonals are equal.', 'Hai đường chéo bằng nhau.')]
    return dict(en=Q[0], vi=Q[1], opts=o, ans=0, ee='Then the other pair of opposite sides is also parallel.', ev='Khi đó cặp cạnh đối còn lại cũng song song.')

def b12_d4_fence(r, lv):
    a, b, c = r.randint(15, 40), r.randint(10, 30), r.choice([50, 60, 80, 120]); p = 2 * (a + b); cost = p * c
    return dict(en='A parallelogram-shaped plot has sides %d m and %d m. Fencing costs %d thousand VND per meter. How much does it cost to fence the plot?' % (a, b, c),
                vi='Một mảnh đất hình bình hành có hai cạnh dài %d m và %d m. Mỗi mét hàng rào giá %d nghìn đồng. Làm hàng rào quanh mảnh đất hết bao nhiêu tiền?' % (a, b, c),
                opts=[tx('%s thousand VND' % '{:,}'.format(cost), '%s nghìn đồng' % '{:,}'.format(cost).replace(',', ' ')), tx('%s thousand VND' % '{:,}'.format((a + b) * c), '%s nghìn đồng' % '{:,}'.format((a + b) * c).replace(',', ' ')),
                      tx('%s thousand VND' % '{:,}'.format(a * b * c), '%s nghìn đồng' % '{:,}'.format(a * b * c).replace(',', ' ')), tx('%s thousand VND' % '{:,}'.format((2 * a + b) * c), '%s nghìn đồng' % '{:,}'.format((2 * a + b) * c).replace(',', ' '))], ans=0,
                ee='Perimeter \\(2(%d+%d)=%d\\) m; cost \\(%d\\cdot%d\\) = %s thousand VND.' % (a, b, p, p, c, '{:,}'.format(cost)), ev='Chu vi \\(2(%d+%d)=%d\\) m; số tiền \\(%d\\cdot%d\\) = %s nghìn đồng.' % (a, b, p, p, c, '{:,}'.format(cost).replace(',', ' ')))

def b12_d4_gate(r, lv):
    a = r.randrange(40, 80, 5)
    return dict(en='A folding gate is made of parallelograms. In one parallelogram an angle is \\(%s\\). What is the angle next to it (on the same side)?' % D(a),
                vi='Một cửa xếp được ghép từ các hình bình hành. Một hình bình hành có một góc bằng \\(%s\\). Góc kề với nó (chung một cạnh) bằng bao nhiêu?' % D(a),
                opts=dopt(r, 180 - a, [a, 90 - a // 2, 360 - a]), ans=0, ee='Consecutive angles are supplementary: \\(180^\\circ-%d^\\circ=%s\\).' % (a, D(180 - a)), ev='Hai góc kề một cạnh bù nhau: \\(180^\\circ-%d^\\circ=%s\\).' % (a, D(180 - a)))

L12_GROUPS = [[('mcq', b12_angles), ('mcq', b12_diag), ('mcq', b12_test)], [('tf', b12_tf_prop), ('tf', b12_tf_num)], [('short', b12_short_x), ('short', b12_short_ang)],
              [('mcq', b12_d1_opp), ('mcq', b12_d1_side), ('mcq', b12_d1_mid)], [('mcq', b12_d2_cons), ('mcq', b12_d2_per), ('mcq', b12_d2_halves)],
              [('mcq', b12_d3_diff), ('mcq', b12_d3_ratio), ('mcq', b12_d3_which)], [('mcq', b12_d4_lift), ('mcq', b12_d4_fence), ('mcq', b12_d4_gate)]]

# =====================================================================================================
# BÀI 13. HÌNH CHỮ NHẬT
# =====================================================================================================
def _rectfig(r, n, diag=True):
    O = _cname(n); P = pts(n, shape('rect', r)); P[O] = ((P[n[0]][0] + P[n[2]][0]) / 2, (P[n[0]][1] + P[n[2]][1]) / 2)
    segs = cyc(n) + ([(n[0], n[2]), (n[1], n[3])] if diag else [])
    return O, QF(P, segs=segs, right=[(n[3], n[0], n[1])])

def b13_diag(r, lv):
    n = PICK(r, NAMES); O, fig = _rectfig(r, n); d = r.randint(3, 12) * 2
    good = '%s%s=%d\\text{ cm},\\ %s%s=%d\\text{ cm}' % (n[1], n[3], d, O, n[0], d // 2)
    bads = ['%s%s=%d\\text{ cm},\\ %s%s=%d\\text{ cm}' % (n[1], n[3], d // 2, O, n[0], d // 2), '%s%s=%d\\text{ cm},\\ %s%s=%d\\text{ cm}' % (n[1], n[3], d, O, n[0], d), '%s%s=%d\\text{ cm},\\ %s%s=%d\\text{ cm}' % (n[1], n[3], 2 * d, O, n[0], d)]
    return dict(en='Rectangle \\(%s\\) has diagonals meeting at \\(%s\\) and \\(%s%s=%d\\) cm. Find \\(%s%s\\) and \\(%s%s\\).' % (n, O, n[0], n[2], d, n[1], n[3], O, n[0]),
                vi='Hình chữ nhật \\(%s\\) có hai đường chéo cắt nhau tại \\(%s\\) và \\(%s%s=%d\\) cm. Tính \\(%s%s\\) và \\(%s%s\\).' % (n, O, n[0], n[2], d, n[1], n[3], O, n[0]),
                opts=pick_opts(r, good, bads), ans=0, fig=fig, ee='The diagonals of a rectangle are equal and bisect each other.', ev='Hai đường chéo của hình chữ nhật bằng nhau và cắt nhau tại trung điểm mỗi đường.')

def b13_median(r, lv):
    t = PICK(r, ['ABC', 'DEF', 'MNP', 'PQR']); h = r.randint(5, 30)
    return dict(en='Triangle \\(%s\\) is right-angled at \\(%s\\), with hypotenuse \\(%s%s=%d\\) cm. \\(M\\) is the midpoint of \\(%s%s\\). Find \\(%sM\\).' % (t, t[0], t[1], t[2], h, t[1], t[2], t[0]) if 'M' not in t else
                'Triangle \\(%s\\) is right-angled at \\(%s\\), with hypotenuse \\(%s%s=%d\\) cm. \\(I\\) is the midpoint of \\(%s%s\\). Find \\(%sI\\).' % (t, t[0], t[1], t[2], h, t[1], t[2], t[0]),
                vi=('Tam giác \\(%s\\) vuông tại \\(%s\\), cạnh huyền \\(%s%s=%d\\) cm. \\(M\\) là trung điểm của \\(%s%s\\). Tính \\(%sM\\).' % (t, t[0], t[1], t[2], h, t[1], t[2], t[0])) if 'M' not in t else
                ('Tam giác \\(%s\\) vuông tại \\(%s\\), cạnh huyền \\(%s%s=%d\\) cm. \\(I\\) là trung điểm của \\(%s%s\\). Tính \\(%sI\\).' % (t, t[0], t[1], t[2], h, t[1], t[2], t[0])),
                opts=pick_opts(r, '%s\\text{ cm}' % vn(F(h, 2)) if lv == 1 else '%s\\text{ cm}' % num(F(h, 2)), ['%d\\text{ cm}' % h, '%d\\text{ cm}' % (2 * h), '%s\\text{ cm}' % (vn(F(h, 3)) if lv == 1 else num(F(h, 3))) if h % 3 == 0 else '%d\\text{ cm}' % (h + 1)]), ans=0,
                ee='The median to the hypotenuse is half the hypotenuse: \\(%d:2=%s\\) cm.' % (h, num(F(h, 2))), ev='Đường trung tuyến ứng với cạnh huyền bằng nửa cạnh huyền: \\(%d:2=%s\\) cm.' % (h, vn(F(h, 2))))

TEST13 = [('a quadrilateral with three right angles', 'tứ giác có ba góc vuông', True), ('a parallelogram with one right angle', 'hình bình hành có một góc vuông', True),
          ('a parallelogram with equal diagonals', 'hình bình hành có hai đường chéo bằng nhau', True), ('an isosceles trapezoid with one right angle', 'hình thang cân có một góc vuông', True),
          ('a quadrilateral with equal diagonals', 'tứ giác có hai đường chéo bằng nhau', False), ('a quadrilateral with perpendicular diagonals', 'tứ giác có hai đường chéo vuông góc', False),
          ('a trapezoid with one right angle', 'hình thang có một góc vuông', False), ('a quadrilateral with two right angles', 'tứ giác có hai góc vuông', False)]
def b13_test(r, lv):
    g = PICK(r, [t for t in TEST13 if t[2]]); bads = r.sample([t for t in TEST13 if not t[2]], 3)
    q = PICK(r, [('Which figure is always a rectangle?', 'Hình nào chắc chắn là hình chữ nhật?'), ('Which of these is a test for a rectangle?', 'Đâu là một dấu hiệu nhận biết hình chữ nhật?'),
                 ('Choose the figure that must be a rectangle.', 'Chọn hình chắc chắn là hình chữ nhật.'), ('Which condition is enough to conclude that a figure is a rectangle?', 'Điều kiện nào đủ để kết luận một hình là hình chữ nhật?')])
    o = [tx(g[0][0].upper() + g[0][1:], g[1][0].upper() + g[1][1:])] + [tx(b[0][0].upper() + b[0][1:], b[1][0].upper() + b[1][1:]) for b in bads]
    return dict(en=q[0], vi=q[1], opts=o, ans=0, ee='Tests: three right angles; a parallelogram with a right angle or equal diagonals; an isosceles trapezoid with a right angle.',
                ev='Dấu hiệu: tứ giác có ba góc vuông; hình bình hành có một góc vuông hoặc hai đường chéo bằng nhau; hình thang cân có một góc vuông.')

def b13_tf_claim(r, lv):
    g = PICK(r, TEST13); return dict(en='%s is always a rectangle.' % (g[0][0].upper() + g[0][1:]), vi='%s luôn là hình chữ nhật.' % (g[1][0].upper() + g[1][1:]), ans=g[2],
                                    ee='Check the tests for a rectangle.', ev='Đối chiếu với các dấu hiệu nhận biết hình chữ nhật.')

def b13_tf_num(r, lv):
    n = PICK(r, NAMES); O = _cname(n); d = r.randint(3, 15); truth = r.random() < .5; claim = d if truth else 2 * d
    return dict(en='Rectangle \\(%s\\) has diagonals meeting at \\(%s\\), and \\(%s%s=%d\\) cm. Then \\(%s%s=%d\\) cm.' % (n, O, O, n[0], d, O, n[1], claim),
                vi='Hình chữ nhật \\(%s\\) có hai đường chéo cắt nhau tại \\(%s\\), \\(%s%s=%d\\) cm. Khi đó \\(%s%s=%d\\) cm.' % (n, O, O, n[0], d, O, n[1], claim), ans=truth,
                ee='\\(%s%s=%s%s=%s%s=%s%s=%d\\) cm.' % (O, n[0], O, n[1], O, n[2], O, n[3], d), ev='\\(%s%s=%s%s=%s%s=%s%s=%d\\) cm.' % (O, n[0], O, n[1], O, n[2], O, n[3], d))

def b13_short_hyp(r, lv):
    t = PICK(r, ['ABC', 'DEF', 'PQR']); m = r.randint(3, 25)
    return dict(en='Triangle \\(%s\\) is right-angled at \\(%s\\); the median from \\(%s\\) has length %d cm. Find the hypotenuse \\(%s%s\\) (cm).' % (t, t[0], t[0], m, t[1], t[2]),
                vi='Tam giác \\(%s\\) vuông tại \\(%s\\), đường trung tuyến kẻ từ \\(%s\\) dài %d cm. Tính cạnh huyền \\(%s%s\\) (cm).' % (t, t[0], t[0], m, t[1], t[2]), key=str(2 * m),
                ee='Hypotenuse \\(=2\\cdot%d=%d\\) cm.' % (m, 2 * m), ev='Cạnh huyền \\(=2\\cdot%d=%d\\) cm.' % (m, 2 * m))

def b13_short_x(r, lv):
    n = PICK(r, NAMES)
    while True:
        k1, k2 = r.randint(1, 3), r.randint(3, 5); x = r.randint(2, 9); c1 = r.randint(1, 12); c2 = (k1 - k2) * x + c1
        if k1 != k2 and c2 < 0: break
    def e(k, c): return '%sx%s' % ('' if k == 1 else k, '' if c == 0 else ('+%d' % c if c > 0 else '%d' % c))
    return dict(en='Rectangle \\(%s\\) has diagonals \\(%s%s=%s\\) and \\(%s%s=%s\\) (cm). Find \\(x\\).' % (n, n[0], n[2], e(k1, c1), n[1], n[3], e(k2, c2)),
                vi='Hình chữ nhật \\(%s\\) có hai đường chéo \\(%s%s=%s\\), \\(%s%s=%s\\) (cm). Tìm \\(x\\).' % (n, n[0], n[2], e(k1, c1), n[1], n[3], e(k2, c2)), key=str(x),
                ee='Equal diagonals: \\(%s=%s\\Rightarrow x=%d\\).' % (e(k1, c1), e(k2, c2), x), ev='Hai đường chéo bằng nhau: \\(%s=%s\\Rightarrow x=%d\\).' % (e(k1, c1), e(k2, c2), x))

def b13_d1_def(r, lv):
    Q = PICK(r, [('A rectangle is a quadrilateral with…', 'Hình chữ nhật là tứ giác có'), ('Which definition describes a rectangle?', 'Định nghĩa nào mô tả hình chữ nhật?'),
                 ('Complete: a rectangle is a quadrilateral that has…', 'Hoàn thành: hình chữ nhật là tứ giác có…'), ('What makes a quadrilateral a rectangle by definition?', 'Theo định nghĩa, tứ giác là hình chữ nhật khi nào?')])
    o = [tx('four right angles', 'bốn góc vuông'), tx('four equal sides', 'bốn cạnh bằng nhau'), tx('two pairs of equal adjacent sides', 'hai cặp cạnh kề bằng nhau'), tx('perpendicular diagonals', 'hai đường chéo vuông góc')]
    return dict(en=Q[0], vi=Q[1], opts=o, ans=0, ee='Definition: four right angles.', ev='Định nghĩa: tứ giác có bốn góc vuông.')

def b13_d1_fig(r, lv):
    n = PICK(r, NAMES); O, fig = _rectfig(r, n)
    good = '%s%s=%s%s=%s%s=%s%s' % (O, n[0], O, n[1], O, n[2], O, n[3])
    bads = ['%s%s\\perp %s%s' % (n[0], n[2], n[1], n[3]), '%s%s=%s%s' % (n[0], n[1], n[1], n[2]), '%s=%s' % (hat(n[0] + n[2] + n[1]), hat(n[1] + n[3] + n[2]) if False else hat(n[0] + n[2] + n[3]))]
    return dict(en='In rectangle \\(%s\\), the diagonals meet at \\(%s\\). Which equality is always true?' % (n, O), vi='Hình chữ nhật \\(%s\\) có hai đường chéo cắt nhau tại \\(%s\\). Đẳng thức nào luôn đúng?' % (n, O),
                opts=[good] + bads, ans=0, fig=fig, ee='Equal diagonals bisecting each other.', ev='Hai đường chéo bằng nhau và cắt nhau tại trung điểm mỗi đường.')

def b13_d1_prop(r, lv):
    Q = PICK(r, [('Complete: the diagonals of any rectangle always…', 'Hoàn thành: hai đường chéo của mọi hình chữ nhật luôn'), ('The diagonals of a rectangle…', 'Hai đường chéo của hình chữ nhật'),
                 ('In every rectangle, the two diagonals…', 'Trong mọi hình chữ nhật, hai đường chéo')])
    o = [tx('are equal and bisect each other', 'bằng nhau và cắt nhau tại trung điểm mỗi đường'), tx('are perpendicular', 'vuông góc với nhau'), tx('bisect the angles', 'là phân giác của các góc'), tx('are parallel', 'song song với nhau')]
    return dict(en=Q[0], vi=Q[1], opts=o, ans=0, ee='Rectangle: equal diagonals that bisect each other.', ev='Hình chữ nhật: hai đường chéo bằng nhau và cắt nhau tại trung điểm mỗi đường.')

def b13_d2_angle(r, lv):
    n = PICK(r, NAMES); O = _cname(n); a = r.randrange(20, 71, 2)
    return dict(en='Rectangle \\(%s\\) has diagonals meeting at \\(%s\\) and \\(%s=%s\\). Find \\(%s\\).' % (n, O, hat(n[1] + n[0] + n[2]), D(a), hat(n[0] + n[1] + n[3])),
                vi='Hình chữ nhật \\(%s\\) có hai đường chéo cắt nhau tại \\(%s\\) và \\(%s=%s\\). Tính \\(%s\\).' % (n, O, hat(n[1] + n[0] + n[2]), D(a), hat(n[0] + n[1] + n[3])),
                opts=dopt(r, a, [90 - a, 180 - 2 * a, 2 * a]), ans=0, ee='\\(%s%s=%s%s\\) so \\(\\triangle %s%s%s\\) is isosceles: \\(%s=%s=%s\\).' % (O, n[0], O, n[1], O, n[0], n[1], hat(n[0] + n[1] + n[3]), hat(n[1] + n[0] + n[2]), D(a)),
                ev='\\(%s%s=%s%s\\) nên \\(\\triangle %s%s%s\\) cân tại \\(%s\\): \\(%s=%s=%s\\).' % (O, n[0], O, n[1], O, n[0], n[1], O, hat(n[0] + n[1] + n[3]), hat(n[1] + n[0] + n[2]), D(a)))

def b13_d2_med(r, lv):
    t = PICK(r, ['ABC', 'DEF', 'PQR']); h = r.randint(3, 16) * 2; ang = r.randrange(20, 71, 2)
    return dict(en='Triangle \\(%s\\) is right-angled at \\(%s\\), \\(%s%s=%d\\) cm, and \\(M\\) is the midpoint of \\(%s%s\\). Find the perimeter of triangle \\(%s%sM\\) if \\(%s%s=%d\\) cm.' % (t, t[0], t[1], t[2], h, t[1], t[2], t[0], t[1], t[0], t[1], h // 2 + 1),
                vi='Tam giác \\(%s\\) vuông tại \\(%s\\), \\(%s%s=%d\\) cm, \\(M\\) là trung điểm của \\(%s%s\\). Tính chu vi tam giác \\(%s%sM\\), biết \\(%s%s=%d\\) cm.' % (t, t[0], t[1], t[2], h, t[1], t[2], t[0], t[1], t[0], t[1], h // 2 + 1),
                opts=nopt(r, h + h // 2 + 1, [h + 1 + h, h // 2 * 3, h + h // 2], unit='\\text{ cm}'), ans=0,
                ee='\\(%sM=%sM=%d\\) cm, so the perimeter is \\(%d+%d+%d=%d\\) cm.' % (t[0], t[1], h // 2, h // 2, h // 2, h // 2 + 1, h + h // 2 + 1), ev='\\(%sM=%sM=%d\\) cm nên chu vi \\(=%d+%d+%d=%d\\) cm.' % (t[0], t[1], h // 2, h // 2, h // 2, h // 2 + 1, h + h // 2 + 1))

def b13_d2_per(r, lv):
    n = PICK(r, NAMES); a, b = r.randint(5, 20), r.randint(3, 12); k = r.choice(['S', 'P'])
    if a == b: a += 1
    v = a * b if k == 'S' else 2 * (a + b)
    return dict(en='Rectangle \\(%s\\) has \\(%s%s=%d\\) cm and \\(%s%s=%d\\) cm. Find its %s.' % (n, n[0], n[1], a, n[1], n[2], b, 'area' if k == 'S' else 'perimeter'),
                vi='Hình chữ nhật \\(%s\\) có \\(%s%s=%d\\) cm, \\(%s%s=%d\\) cm. Tính %s của nó.' % (n, n[0], n[1], a, n[1], n[2], b, 'diện tích' if k == 'S' else 'chu vi'),
                opts=nopt(r, v, [2 * (a + b) if k == 'S' else a * b, a + b, v * 2], unit='\\text{ cm}^2' if k == 'S' else '\\text{ cm}'), ans=0,
                ee='\\(%s\\).' % ('%d\\cdot%d=%d' % (a, b, v) if k == 'S' else '2(%d+%d)=%d' % (a, b, v)), ev='\\(%s\\).' % ('%d\\cdot%d=%d' % (a, b, v) if k == 'S' else '2(%d+%d)=%d' % (a, b, v)))

def b13_d3_x(r, lv):
    n = PICK(r, NAMES); T = _cname(n)
    while True:
        x = r.randint(2, 8); a1, c1 = r.randint(1, 3), r.randint(1, 9); a2 = r.randint(1, 3); c2 = a1 * x + c1 - a2 * x
        if a2 != a1 and c2 > 0: break
    d = 2 * (a1 * x + c1)
    def e(k, c): return '%sx+%d' % ('' if k == 1 else k, c)
    return dict(en='The diagonals \\(%s%s\\) and \\(%s%s\\) of quadrilateral \\(%s\\) meet at \\(%s\\), with \\(%s%s=%s%s=%s\\), \\(%s%s=%s%s=%s\\) (cm). Find \\(x\\) so that \\(%s\\) is a rectangle.' % (n[0], n[2], n[1], n[3], n, T, T, n[0], T, n[2], e(a1, c1), T, n[1], T, n[3], e(a2, c2), n),
                vi='Hai đường chéo \\(%s%s\\), \\(%s%s\\) của tứ giác \\(%s\\) cắt nhau tại \\(%s\\), \\(%s%s=%s%s=%s\\), \\(%s%s=%s%s=%s\\) (cm). Tìm \\(x\\) để \\(%s\\) là hình chữ nhật.' % (n[0], n[2], n[1], n[3], n, T, T, n[0], T, n[2], e(a1, c1), T, n[1], T, n[3], e(a2, c2), n),
                opts=nopt(r, x, [d, x + 1, a1 * x + c1]), ans=0, ee='It is a parallelogram (diagonals bisect each other); it is a rectangle when the diagonals are equal: \\(%s=%s\\Rightarrow x=%d\\).' % (e(a1, c1), e(a2, c2), x),
                ev='Tứ giác là hình bình hành (hai đường chéo cắt nhau tại trung điểm mỗi đường); là hình chữ nhật khi hai đường chéo bằng nhau: \\(%s=%s\\Rightarrow x=%d\\).' % (e(a1, c1), e(a2, c2), x))

def b13_d3_kind(r, lv):
    n = PICK(r, NAMES); k = r.randrange(3)
    if k == 0: cond_en, cond_vi = '\\(%s\\) and \\(%s=90^\\circ\\)' % (par(n[0] + n[1], n[2] + n[3]) + ',\\ ' + par(n[1] + n[2], n[3] + n[0]), hat(n[0])), '\\(%s\\) và \\(%s=90^\\circ\\)' % (par(n[0] + n[1], n[2] + n[3]) + ',\\ ' + par(n[1] + n[2], n[3] + n[0]), hat(n[0]))
    elif k == 1: cond_en, cond_vi = '\\(%s=%s=%s=90^\\circ\\)' % (hat(n[0]), hat(n[1]), hat(n[2])), '\\(%s=%s=%s=90^\\circ\\)' % (hat(n[0]), hat(n[1]), hat(n[2]))
    else: cond_en, cond_vi = '\\(%s%s=%s%s,\\ %s%s=%s%s\\) and \\(%s%s=%s%s\\)' % (n[0], n[1], n[2], n[3], n[1], n[2], n[3], n[0], n[0], n[2], n[1], n[3]), '\\(%s%s=%s%s,\\ %s%s=%s%s\\) và \\(%s%s=%s%s\\)' % (n[0], n[1], n[2], n[3], n[1], n[2], n[3], n[0], n[0], n[2], n[1], n[3])
    o = [tx('a rectangle', 'hình chữ nhật'), tx('a rhombus that is not a square', 'hình thoi (không phải hình vuông)'), tx('a trapezoid that is not a parallelogram', 'hình thang (không phải hình bình hành)'), tx('a kite', 'tứ giác có hai cặp cạnh kề bằng nhau')]
    return dict(en='Quadrilateral \\(%s\\) has %s. What kind of quadrilateral is it?' % (n, cond_en), vi='Tứ giác \\(%s\\) có %s. Tứ giác đó là hình gì?' % (n, cond_vi), opts=o, ans=0,
                ee=['A parallelogram with a right angle is a rectangle.', 'Three right angles give a rectangle.', 'Opposite sides equal → parallelogram; equal diagonals → rectangle.'][k],
                ev=['Hình bình hành có một góc vuông là hình chữ nhật.', 'Tứ giác có ba góc vuông là hình chữ nhật.', 'Các cạnh đối bằng nhau → hình bình hành; hai đường chéo bằng nhau → hình chữ nhật.'][k])

def b13_d3_mid(r, lv):
    a = r.randrange(20, 71, 2)
    return dict(en='Triangle \\(ABC\\) is right-angled at \\(A\\) with \\(\\widehat{B}=%s\\). \\(M\\) is the midpoint of \\(BC\\). Find \\(\\widehat{AMC}\\).' % D(a),
                vi='Tam giác \\(ABC\\) vuông tại \\(A\\) có \\(\\widehat{B}=%s\\), \\(M\\) là trung điểm của \\(BC\\). Tính \\(\\widehat{AMC}\\).' % D(a),
                opts=dopt(r, 2 * a, [a, 180 - 2 * a, 90 - a]), ans=0, ee='\\(MA=MB\\), so \\(\\widehat{MAB}=\\widehat{B}=%s\\) and the exterior angle \\(\\widehat{AMC}=2\\cdot%d^\\circ=%s\\).' % (D(a), a, D(2 * a)),
                ev='\\(MA=MB\\) nên \\(\\widehat{MAB}=\\widehat{B}=%s\\); góc ngoài \\(\\widehat{AMC}=2\\cdot%d^\\circ=%s\\).' % (D(a), a, D(2 * a)))

def b13_d4_door(r, lv):
    d1 = r.randint(200, 240); dd = r.choice([0, 0, 2, 3, 5]); d2 = d1 + dd
    good = tx('Yes, it is a rectangle.', 'Có, khung cửa là hình chữ nhật.') if dd == 0 else tx('No, it is not a rectangle.', 'Không, khung cửa không phải hình chữ nhật.')
    bad = tx('No, it is not a rectangle.', 'Không, khung cửa không phải hình chữ nhật.') if dd == 0 else tx('Yes, it is a rectangle.', 'Có, khung cửa là hình chữ nhật.')
    return dict(en='A door frame has opposite sides of equal length. A carpenter measures its two diagonals: %d cm and %d cm. Is the frame a rectangle?' % (d1, d2),
                vi='Một khung cửa có các cạnh đối bằng nhau. Người thợ đo hai đường chéo được %d cm và %d cm. Khung cửa có phải hình chữ nhật không?' % (d1, d2),
                opts=[good, bad, tx('We cannot tell without measuring the angles.', 'Không thể biết nếu không đo góc.'), tx('Only if the diagonals are perpendicular.', 'Chỉ khi hai đường chéo vuông góc.')], ans=0,
                ee='Equal opposite sides → parallelogram; it is a rectangle exactly when the diagonals are equal.', ev='Các cạnh đối bằng nhau → hình bình hành; nó là hình chữ nhật khi và chỉ khi hai đường chéo bằng nhau.')

def b13_d4_lamp(r, lv):
    a, b = r.choice([(6, 8), (9, 12), (12, 16), (15, 20), (5, 12), (8, 15), (12, 9)]); c = int(round(math.hypot(a, b))); assert c * c == a * a + b * b
    return dict(en='A garden has the shape of a right triangle whose hypotenuse is %d m long. A lamp is placed so that it is equally far from the three corners. How far is it from each corner?' % c,
                vi='Một khu vườn có dạng tam giác vuông với cạnh huyền dài %d m. Người ta đặt một bóng đèn cách đều ba góc vườn. Bóng đèn cách mỗi góc bao xa?' % c,
                opts=pick_opts(r, ('%s\\text{ m}' % num(F(c, 2))) if lv > 1 else ('%s\\text{ m}' % vn(F(c, 2))), ['%d\\text{ m}' % c, ('%s\\text{ m}' % num(F(c, 3))) if c % 3 == 0 else '%d\\text{ m}' % (c + 2), '%d\\text{ m}' % (a)]), ans=0,
                ee='The midpoint of the hypotenuse is equally far from the three vertices: \\(%d:2=%s\\) m.' % (c, num(F(c, 2))), ev='Trung điểm cạnh huyền cách đều ba đỉnh: \\(%d:2=%s\\) m.' % (c, vn(F(c, 2))))

def b13_d4_field(r, lv):
    a, b = r.randint(40, 100), r.randint(20, 70)
    return dict(en='Students mark a rectangular football field with ropes: two pairs of opposite sides of %d m and %d m. Which extra check ensures that the corners are right angles?' % (a, b),
                vi='Học sinh căng dây để kẻ một sân bóng hình chữ nhật: hai cặp cạnh đối dài %d m và %d m. Cần kiểm tra thêm điều gì để chắc chắn các góc sân đều vuông?' % (a, b),
                opts=[tx('The two diagonals are equal.', 'Hai đường chéo bằng nhau.'), tx('The two diagonals are perpendicular.', 'Hai đường chéo vuông góc với nhau.'), tx('One diagonal is %d m.' % (a + b), 'Một đường chéo dài %d m.' % (a + b)), tx('Nothing more is needed.', 'Không cần kiểm tra thêm.')], ans=0,
                ee='Equal opposite sides give a parallelogram; equal diagonals make it a rectangle.', ev='Các cạnh đối bằng nhau cho ta hình bình hành; hai đường chéo bằng nhau thì nó là hình chữ nhật.')

L13_GROUPS = [[('mcq', b13_diag), ('mcq', b13_median), ('mcq', b13_test)], [('tf', b13_tf_claim), ('tf', b13_tf_num)], [('short', b13_short_hyp), ('short', b13_short_x)],
              [('mcq', b13_d1_def), ('mcq', b13_d1_fig), ('mcq', b13_d1_prop)], [('mcq', b13_d2_angle), ('mcq', b13_d2_med), ('mcq', b13_d2_per)],
              [('mcq', b13_d3_x), ('mcq', b13_d3_kind), ('mcq', b13_d3_mid)], [('mcq', b13_d4_door), ('mcq', b13_d4_lamp), ('mcq', b13_d4_field)]]

# =====================================================================================================
# BÀI 14. HÌNH THOI VÀ HÌNH VUÔNG
# =====================================================================================================
def _rhfig(r, n):
    O = _cname(n); P = pts(n, shape('rhom', r)); P[O] = ((P[n[0]][0] + P[n[2]][0]) / 2, (P[n[0]][1] + P[n[2]][1]) / 2)
    return O, QF(P, segs=cyc(n) + [(n[0], n[2]), (n[1], n[3])], right=[(n[0], O, n[1])])

def b14_per(r, lv):
    n = PICK(r, NAMES); a = r.randint(3, 25); k = r.choice(['side', 'per'])
    if k == 'per':
        return dict(en='Rhombus \\(%s\\) has side \\(%s%s=%d\\) cm. Find its perimeter.' % (n, n[0], n[1], a), vi='Hình thoi \\(%s\\) có cạnh \\(%s%s=%d\\) cm. Tính chu vi của hình thoi.' % (n, n[0], n[1], a),
                    opts=nopt(r, 4 * a, [2 * a, a * a, 4 * a + 4], unit='\\text{ cm}'), ans=0, ee='Four equal sides: \\(4\\cdot%d=%d\\) cm.' % (a, 4 * a), ev='Bốn cạnh bằng nhau: \\(4\\cdot%d=%d\\) cm.' % (a, 4 * a))
    return dict(en='Rhombus \\(%s\\) has perimeter %d cm. Find \\(%s%s\\).' % (n, 4 * a, n[1], n[2]), vi='Hình thoi \\(%s\\) có chu vi %d cm. Tính \\(%s%s\\).' % (n, 4 * a, n[1], n[2]),
                opts=nopt(r, a, [2 * a, 4 * a, a + 2], unit='\\text{ cm}'), ans=0, ee='\\(%d:4=%d\\) cm.' % (4 * a, a), ev='\\(%d:4=%d\\) cm.' % (4 * a, a))

def b14_angle(r, lv):
    n = PICK(r, NAMES); O, fig = _rhfig(r, n); a = r.randrange(30, 151, 2)
    if a == 90: a = 64
    good = a // 2; q = r.choice([0, 1])
    if q == 0:
        return dict(en='Rhombus \\(%s\\) has \\(%s=%s\\). Find \\(%s\\).' % (n, hat(n[3] + n[0] + n[1]), D(a), hat(n[1] + n[0] + n[2])), vi='Hình thoi \\(%s\\) có \\(%s=%s\\). Tính \\(%s\\).' % (n, hat(n[3] + n[0] + n[1]), D(a), hat(n[1] + n[0] + n[2])),
                    opts=dopt(r, good, [a, 180 - a, 90 - good]), ans=0, fig=fig, ee='Diagonal \\(%s%s\\) bisects \\(%s\\): \\(%d^\\circ:2=%s\\).' % (n[0], n[2], hat(n[3] + n[0] + n[1]), a, D(good)),
                    ev='Đường chéo \\(%s%s\\) là phân giác của \\(%s\\): \\(%d^\\circ:2=%s\\).' % (n[0], n[2], hat(n[3] + n[0] + n[1]), a, D(good)))
    return dict(en='Rhombus \\(%s\\) has \\(%s=%s\\). Find \\(%s\\).' % (n, hat(n[3] + n[0] + n[1]), D(a), hat(n[0] + n[1] + n[2])), vi='Hình thoi \\(%s\\) có \\(%s=%s\\). Tính \\(%s\\).' % (n, hat(n[3] + n[0] + n[1]), D(a), hat(n[0] + n[1] + n[2])),
                opts=dopt(r, 180 - a, [a, good, 90]), ans=0, fig=fig, ee='Consecutive angles are supplementary.', ev='Hai góc kề một cạnh bù nhau.')

TEST14 = [('a parallelogram with two equal adjacent sides', 'hình bình hành có hai cạnh kề bằng nhau', 'rh'), ('a parallelogram with perpendicular diagonals', 'hình bình hành có hai đường chéo vuông góc', 'rh'),
          ('a quadrilateral with four equal sides', 'tứ giác có bốn cạnh bằng nhau', 'rh'), ('a parallelogram in which a diagonal bisects an angle', 'hình bình hành có một đường chéo là phân giác của một góc', 'rh'),
          ('a rectangle with two equal adjacent sides', 'hình chữ nhật có hai cạnh kề bằng nhau', 'sq'), ('a rectangle with perpendicular diagonals', 'hình chữ nhật có hai đường chéo vuông góc', 'sq'),
          ('a rhombus with a right angle', 'hình thoi có một góc vuông', 'sq'), ('a rhombus with equal diagonals', 'hình thoi có hai đường chéo bằng nhau', 'sq'),
          ('a quadrilateral with perpendicular diagonals', 'tứ giác có hai đường chéo vuông góc', 'no'), ('a quadrilateral with equal diagonals', 'tứ giác có hai đường chéo bằng nhau', 'no'),
          ('a parallelogram with equal diagonals', 'hình bình hành có hai đường chéo bằng nhau', 'rect'), ('a quadrilateral with two pairs of equal adjacent sides', 'tứ giác có hai cặp cạnh kề bằng nhau', 'no')]
def cap(s): return s[0].upper() + s[1:]
def b14_test(r, lv):
    kind = r.choice(['rh', 'sq']); g = PICK(r, [t for t in TEST14 if t[2] == kind]); bads = r.sample([t for t in TEST14 if t[2] != kind and not (kind == 'rh' and t[2] == 'sq')], 3)
    q = {'rh': PICK(r, [('Which figure is always a rhombus?', 'Hình nào chắc chắn là hình thoi?'), ('Which of these is a test for a rhombus?', 'Đâu là một dấu hiệu nhận biết hình thoi?')]),
         'sq': PICK(r, [('Which figure is always a square?', 'Hình nào chắc chắn là hình vuông?'), ('Which of these is a test for a square?', 'Đâu là một dấu hiệu nhận biết hình vuông?')])}[kind]
    o = [tx(cap(g[0]), cap(g[1]))] + [tx(cap(b[0]), cap(b[1])) for b in bads]
    return dict(en=q[0], vi=q[1], opts=o, ans=0, ee='Compare with the tests for a rhombus and for a square.', ev='Đối chiếu với các dấu hiệu nhận biết hình thoi, hình vuông.')

PROP14 = [('the diagonals of a rhombus are perpendicular', 'hai đường chéo của hình thoi vuông góc với nhau', True), ('the diagonals of a rhombus are equal', 'hai đường chéo của hình thoi bằng nhau', False),
          ('each diagonal of a rhombus bisects two angles', 'mỗi đường chéo của hình thoi là phân giác của hai góc', True), ('the diagonals of a square are equal and perpendicular', 'hai đường chéo của hình vuông bằng nhau và vuông góc', True),
          ('every rhombus is a square', 'mọi hình thoi đều là hình vuông', False), ('every square is a rhombus', 'mọi hình vuông đều là hình thoi', True), ('every square is a rectangle', 'mọi hình vuông đều là hình chữ nhật', True),
          ('every rectangle is a square', 'mọi hình chữ nhật đều là hình vuông', False)]
def b14_tf_prop(r, lv):
    g = PICK(r, PROP14); return dict(en=cap(g[0]) + '.', vi=cap(g[1]) + '.', ans=g[2], ee='Recall the properties of rhombi and squares.', ev='Nhớ lại tính chất của hình thoi, hình vuông.')

def b14_tf_num(r, lv):
    n = PICK(r, NAMES); O = _cname(n); a = r.randint(2, 12); truth = r.random() < .5; claim = a if truth else 2 * a
    return dict(en='Square \\(%s\\) has diagonals meeting at \\(%s\\) and \\(%s%s=%d\\) cm. Then \\(%s%s=%d\\) cm.' % (n, O, O, n[0], a, O, n[1], claim),
                vi='Hình vuông \\(%s\\) có hai đường chéo cắt nhau tại \\(%s\\), \\(%s%s=%d\\) cm. Khi đó \\(%s%s=%d\\) cm.' % (n, O, O, n[0], a, O, n[1], claim), ans=truth,
                ee='The diagonals of a square are equal and bisect each other: \\(%s%s=%s%s=%d\\) cm.' % (O, n[1], O, n[0], a), ev='Hai đường chéo của hình vuông bằng nhau và cắt nhau tại trung điểm mỗi đường: \\(%s%s=%s%s=%d\\) cm.' % (O, n[1], O, n[0], a))

def b14_short_x(r, lv):
    n = PICK(r, NAMES)
    while True:
        k1, k2 = r.randint(2, 4), r.randint(4, 7); x = r.randint(3, 10); c1 = r.randint(1, 12); c2 = (k1 - k2) * x + c1
        if k1 != k2 and c2 < 0: break
    side = k1 * x + c1
    return dict(en='Rhombus \\(%s\\) has \\(%s%s=%dx+%d\\) and \\(%s%s=%dx%d\\) (cm). Find the length of a side (cm).' % (n, n[0], n[1], k1, c1, n[1], n[2], k2, c2),
                vi='Hình thoi \\(%s\\) có \\(%s%s=%dx+%d\\) và \\(%s%s=%dx%d\\) (cm). Tính độ dài cạnh hình thoi (cm).' % (n, n[0], n[1], k1, c1, n[1], n[2], k2, c2), key=str(side),
                ee='\\(%dx+%d=%dx%d\\Rightarrow x=%d\\); side \\(=%d\\) cm.' % (k1, c1, k2, c2, x, side), ev='\\(%dx+%d=%dx%d\\Rightarrow x=%d\\); cạnh \\(=%d\\) cm.' % (k1, c1, k2, c2, x, side))

def b14_short_sq(r, lv):
    n = PICK(r, NAMES); O = _cname(n); a = r.randint(2, 15)
    return dict(en='Square \\(%s\\) has diagonals meeting at \\(%s\\), and \\(%s%s=%d\\) cm. Find \\(%s%s\\) (cm).' % (n, O, O, n[0], a, n[1], n[3]),
                vi='Hình vuông \\(%s\\) có hai đường chéo cắt nhau tại \\(%s\\), \\(%s%s=%d\\) cm. Tính \\(%s%s\\) (cm).' % (n, O, O, n[0], a, n[1], n[3]), key=str(2 * a),
                ee='\\(%s%s=%s%s=2\\cdot%d=%d\\) cm.' % (n[1], n[3], n[0], n[2], a, 2 * a), ev='\\(%s%s=%s%s=2\\cdot%d=%d\\) cm.' % (n[1], n[3], n[0], n[2], a, 2 * a))

def b14_d1_def(r, lv):
    k = r.choice(['rh', 'sq'])
    if k == 'rh': Q = PICK(r, [('A rhombus is a quadrilateral with…', 'Hình thoi là tứ giác có'), ('By definition, a rhombus is a quadrilateral that has…', 'Theo định nghĩa, hình thoi là tứ giác có')]); g = tx('four equal sides', 'bốn cạnh bằng nhau'); b = [tx('four right angles', 'bốn góc vuông'), tx('four right angles and four equal sides', 'bốn góc vuông và bốn cạnh bằng nhau'), tx('two equal diagonals', 'hai đường chéo bằng nhau')]
    else: Q = PICK(r, [('A square is a quadrilateral with…', 'Hình vuông là tứ giác có'), ('By definition, a square is a quadrilateral that has…', 'Theo định nghĩa, hình vuông là tứ giác có')]); g = tx('four right angles and four equal sides', 'bốn góc vuông và bốn cạnh bằng nhau'); b = [tx('four equal sides', 'bốn cạnh bằng nhau'), tx('four right angles', 'bốn góc vuông'), tx('perpendicular diagonals', 'hai đường chéo vuông góc')]
    return dict(en=Q[0], vi=Q[1], opts=[g] + b, ans=0, ee='Recall the definitions.', ev='Nhớ lại định nghĩa.')

def b14_d1_fig(r, lv):
    n = PICK(r, NAMES); O, fig = _rhfig(r, n)
    good = '%s%s\\perp %s%s' % (n[0], n[2], n[1], n[3]); bads = ['%s%s=%s%s' % (n[0], n[2], n[1], n[3]), '%s=90^\\circ' % hat(n[0]), '%s%s=%s%s' % (O, n[0], O, n[1])]
    return dict(en='In rhombus \\(%s\\), the diagonals meet at \\(%s\\). Which statement is always true?' % (n, O), vi='Hình thoi \\(%s\\) có hai đường chéo cắt nhau tại \\(%s\\). Khẳng định nào luôn đúng?' % (n, O),
                opts=[good] + bads, ans=0, fig=fig, ee='The diagonals of a rhombus are perpendicular.', ev='Hai đường chéo của hình thoi vuông góc với nhau.')

def b14_d1_sqang(r, lv):
    n = PICK(r, NAMES); O = _cname(n); k = r.choice([0, 1, 2])
    a = [(hat(n[1] + n[0] + n[2]), 45), (hat(n[0] + O + n[1]), 90), (hat(n[0] + n[1] + n[2]), 90)][k]
    return dict(en='Square \\(%s\\) has diagonals meeting at \\(%s\\). Find \\(%s\\).' % (n, O, a[0]), vi='Hình vuông \\(%s\\) có hai đường chéo cắt nhau tại \\(%s\\). Tính \\(%s\\).' % (n, O, a[0]),
                opts=dopt(r, a[1], [45 if a[1] == 90 else 90, 60, 30]), ans=0, ee='\\(%s=%s\\).' % (a[0], D(a[1])), ev='\\(%s=%s\\).' % (a[0], D(a[1])))

def b14_d2_x(r, lv):
    n = PICK(r, NAMES)
    while True:
        k1, k2 = r.randint(2, 4), r.randint(4, 7); x = r.randint(3, 10); c1 = r.randint(1, 12); c2 = (k1 - k2) * x + c1
        if k1 != k2 and c2 < 0: break
    side = k1 * x + c1
    return dict(en='Rhombus \\(%s\\) has \\(%s%s=%dx+%d\\) and \\(%s%s=%dx%d\\) (cm). Find its perimeter.' % (n, n[0], n[1], k1, c1, n[2], n[3], k2, c2),
                vi='Hình thoi \\(%s\\) có \\(%s%s=%dx+%d\\) và \\(%s%s=%dx%d\\) (cm). Tính chu vi hình thoi.' % (n, n[0], n[1], k1, c1, n[2], n[3], k2, c2),
                opts=nopt(r, 4 * side, [side, 2 * side, 4 * x], unit='\\text{ cm}'), ans=0, ee='\\(x=%d\\), side \\(%d\\) cm, perimeter \\(%d\\) cm.' % (x, side, 4 * side), ev='\\(x=%d\\), cạnh \\(%d\\) cm, chu vi \\(%d\\) cm.' % (x, side, 4 * side))

def b14_d2_ang(r, lv):
    n = PICK(r, NAMES); a = r.randrange(30, 151, 2)
    if a == 90: a = 70
    return dict(en='Rhombus \\(%s\\) has \\(%s=%s\\). Find \\(%s\\).' % (n, hat(n[3] + n[0] + n[1]), D(a), hat(n[0] + n[1] + n[3])), vi='Hình thoi \\(%s\\) có \\(%s=%s\\). Tính \\(%s\\).' % (n, hat(n[3] + n[0] + n[1]), D(a), hat(n[0] + n[1] + n[3])),
                opts=dopt(r, (180 - a) // 2, [a // 2, 180 - a, a]), ans=0, ee='\\(%s=180^\\circ-%d^\\circ=%s\\), and \\(%s%s\\) bisects it: \\(%s\\).' % (hat(n[0] + n[1] + n[2]), a, D(180 - a), n[1], n[3], D((180 - a) // 2)),
                ev='\\(%s=180^\\circ-%d^\\circ=%s\\), mà \\(%s%s\\) là phân giác nên bằng \\(%s\\).' % (hat(n[0] + n[1] + n[2]), a, D(180 - a), n[1], n[3], D((180 - a) // 2)))

def b14_d2_area(r, lv):
    n = PICK(r, NAMES); d1, d2 = r.randint(3, 15) * 2, r.randint(2, 14)
    return dict(en='Rhombus \\(%s\\) has diagonals %d cm and %d cm. Find its area.' % (n, d1, d2), vi='Hình thoi \\(%s\\) có hai đường chéo dài %d cm và %d cm. Tính diện tích hình thoi.' % (n, d1, d2),
                opts=nopt(r, d1 * d2 // 2, [d1 * d2, d1 + d2, 2 * (d1 + d2)], unit='\\text{ cm}^2'), ans=0, ee='\\(S=\\dfrac{%d\\cdot%d}{2}=%d\\) cm².' % (d1, d2, d1 * d2 // 2), ev='\\(S=\\dfrac{%d\\cdot%d}{2}=%d\\) cm².' % (d1, d2, d1 * d2 // 2))

def b14_d3_kind(r, lv):
    n = PICK(r, NAMES); O = _cname(n); k = r.randrange(4)
    conds = [('\\(%s%s\\) and \\(%s%s\\) bisect each other and \\(%s%s\\perp %s%s\\)' % (n[0], n[2], n[1], n[3], n[0], n[2], n[1], n[3]), '\\(%s%s\\), \\(%s%s\\) cắt nhau tại trung điểm mỗi đường và \\(%s%s\\perp %s%s\\)' % (n[0], n[2], n[1], n[3], n[0], n[2], n[1], n[3]), 0),
             ('\\(%s%s\\) and \\(%s%s\\) bisect each other, are equal and perpendicular' % (n[0], n[2], n[1], n[3]), '\\(%s%s\\), \\(%s%s\\) cắt nhau tại trung điểm mỗi đường, bằng nhau và vuông góc' % (n[0], n[2], n[1], n[3]), 1),
             ('\\(%s%s=%s%s=%s%s=%s%s\\) and \\(%s=90^\\circ\\)' % (n[0], n[1], n[1], n[2], n[2], n[3], n[3], n[0], hat(n[0])), '\\(%s%s=%s%s=%s%s=%s%s\\) và \\(%s=90^\\circ\\)' % (n[0], n[1], n[1], n[2], n[2], n[3], n[3], n[0], hat(n[0])), 1),
             ('\\(%s%s=%s%s=%s%s=%s%s\\)' % (n[0], n[1], n[1], n[2], n[2], n[3], n[3], n[0]), '\\(%s%s=%s%s=%s%s=%s%s\\)' % (n[0], n[1], n[1], n[2], n[2], n[3], n[3], n[0]), 0)]
    ce, cv, ans = conds[k]
    o = [tx('a rhombus (not necessarily a square)', 'hình thoi (chưa chắc là hình vuông)'), tx('a square', 'hình vuông'), tx('a rectangle (not necessarily a square)', 'hình chữ nhật (chưa chắc là hình vuông)'), tx('an isosceles trapezoid', 'hình thang cân')]
    o = [o[ans]] + [x for i, x in enumerate(o) if i != ans]
    return dict(en='Quadrilateral \\(%s\\) satisfies: %s. What is the most precise name for it?' % (n, ce), vi='Tứ giác \\(%s\\) thỏa mãn: %s. Tên gọi chính xác nhất của nó là' % (n, cv), opts=o, ans=0,
                ee='Use the tests for rhombi and squares.', ev='Dùng các dấu hiệu nhận biết hình thoi, hình vuông.')

def b14_d3_ang(r, lv):
    n = PICK(r, NAMES); a = r.randrange(30, 151, 2)
    if a == 90: a = 116
    return dict(en='Rhombus \\(%s\\) has \\(%s=%s\\). Find the angle between diagonal \\(%s%s\\) and side \\(%s%s\\).' % (n, hat(n[0]), D(a), n[0], n[2], n[0], n[1]),
                vi='Hình thoi \\(%s\\) có \\(%s=%s\\). Tính góc tạo bởi đường chéo \\(%s%s\\) và cạnh \\(%s%s\\).' % (n, hat(n[0]), D(a), n[0], n[2], n[0], n[1]),
                opts=dopt(r, a // 2, [a, 180 - a, 90 - a // 2]), ans=0,
                ee='The diagonal bisects \\(%s\\): \\(%s\\).' % (hat(n[0]), D(a // 2)), ev='Đường chéo là phân giác của \\(%s\\): \\(%s\\).' % (hat(n[0]), D(a // 2)))

def b14_d3_sq(r, lv):
    a = r.randint(2, 9) * 2; s = a
    return dict(en='Square \\(ABCD\\) has side %d cm. \\(M\\) and \\(N\\) are the midpoints of \\(AB\\) and \\(CD\\). What kind of quadrilateral is \\(AMND\\) and what is its perimeter?' % a,
                vi='Hình vuông \\(ABCD\\) có cạnh %d cm; \\(M\\), \\(N\\) lần lượt là trung điểm của \\(AB\\), \\(CD\\). Tứ giác \\(AMND\\) là hình gì và có chu vi bằng bao nhiêu?' % a,
                opts=[tx('A rectangle; %d cm' % (3 * a), 'Hình chữ nhật; %d cm' % (3 * a)), tx('A square; %d cm' % (2 * a), 'Hình vuông; %d cm' % (2 * a)), tx('A rectangle; %d cm' % (4 * a), 'Hình chữ nhật; %d cm' % (4 * a)), tx('A rhombus; %d cm' % (3 * a), 'Hình thoi; %d cm' % (3 * a))], ans=0,
                ee='Three right angles → rectangle with sides %d cm and %d cm: perimeter \\(2(%d+%d)=%d\\) cm.' % (a // 2, a, a // 2, a, 3 * a), ev='Có ba góc vuông → hình chữ nhật với hai cạnh %d cm và %d cm: chu vi \\(2(%d+%d)=%d\\) cm.' % (a // 2, a, a // 2, a, 3 * a))

def b14_d4_tile(r, lv):
    d1, d2 = r.choice([(20, 30), (24, 32), (30, 40), (16, 30), (18, 24), (40, 30)]); k = r.randint(10, 60)
    S = d1 * d2 // 2
    return dict(en='A floor is decorated with %d rhombus-shaped tiles; each tile has diagonals %d cm and %d cm. What area do the tiles cover?' % (k, d1, d2),
                vi='Một nền nhà được lát %d viên gạch hình thoi, mỗi viên có hai đường chéo dài %d cm và %d cm. Diện tích phần nền được lát là bao nhiêu?' % (k, d1, d2),
                opts=nopt(r, k * S, [k * d1 * d2, S, k * (d1 + d2)], unit='\\text{ cm}^2'), ans=0, ee='One tile: \\(%d\\cdot%d:2=%d\\) cm²; total \\(%d\\cdot%d=%d\\) cm².' % (d1, d2, S, k, S, k * S),
                ev='Một viên: \\(%d\\cdot%d:2=%d\\) cm²; tổng \\(%d\\cdot%d=%d\\) cm².' % (d1, d2, S, k, S, k * S))

def b14_d4_frame(r, lv):
    a = r.randint(20, 60); n = r.randint(4, 12)
    return dict(en='A decorative frame is made of %d rhombi with side %d cm, built from separate wooden bars (no bars shared). How many centimeters of wood are needed?' % (n, a),
                vi='Một khung trang trí gồm %d hình thoi cạnh %d cm, mỗi hình làm từ các thanh gỗ riêng (không dùng chung thanh). Cần tất cả bao nhiêu xăng-ti-mét thanh gỗ?' % (n, a),
                opts=nopt(r, 4 * a * n, [a * n, 2 * a * n, 4 * a], unit='\\text{ cm}'), ans=0, ee='\\(%d\\cdot4\\cdot%d=%d\\) cm.' % (n, a, 4 * a * n), ev='\\(%d\\cdot4\\cdot%d=%d\\) cm.' % (n, a, 4 * a * n))

def b14_d4_check(r, lv):
    Q = PICK(r, [('A tile-maker checks a tile: its four sides are equal. What else must she check to be sure it is a square?', 'Người thợ kiểm tra một viên gạch có bốn cạnh bằng nhau. Cần kiểm tra thêm điều gì để chắc chắn viên gạch là hình vuông?'),
                 ('A window frame has four equal sides. Which extra measurement shows that it is a square?', 'Một khung cửa sổ có bốn cạnh bằng nhau. Đo thêm điều gì để biết nó là hình vuông?'),
                 ('A garden bed has four equal sides. What extra condition makes it a square?', 'Một bồn hoa có bốn cạnh bằng nhau. Cần thêm điều kiện gì để nó là hình vuông?')])
    o = [tx('The two diagonals are equal.', 'Hai đường chéo bằng nhau.'), tx('The two diagonals are perpendicular.', 'Hai đường chéo vuông góc.'), tx('Opposite sides are parallel.', 'Các cạnh đối song song.'), tx('Each diagonal bisects two angles.', 'Mỗi đường chéo là phân giác của hai góc.')]
    return dict(en=Q[0], vi=Q[1], opts=o, ans=0, ee='Four equal sides → rhombus (already with perpendicular diagonals); a rhombus with equal diagonals is a square.',
                ev='Bốn cạnh bằng nhau → hình thoi (đã có hai đường chéo vuông góc); hình thoi có hai đường chéo bằng nhau là hình vuông.')

L14_GROUPS = [[('mcq', b14_per), ('mcq', b14_angle), ('mcq', b14_test)], [('tf', b14_tf_prop), ('tf', b14_tf_num)], [('short', b14_short_x), ('short', b14_short_sq)],
              [('mcq', b14_d1_def), ('mcq', b14_d1_fig), ('mcq', b14_d1_sqang)], [('mcq', b14_d2_x), ('mcq', b14_d2_ang), ('mcq', b14_d2_area)],
              [('mcq', b14_d3_kind), ('mcq', b14_d3_ang), ('mcq', b14_d3_sq)], [('mcq', b14_d4_tile), ('mcq', b14_d4_frame), ('mcq', b14_d4_check)]]

# ------------------------------------------------------------------ hình cho lý thuyết / ví dụ
def FIGT(P, segs=(), dash=(), right=(), px=260, cap=None):
    """Hình tĩnh có chú thích song ngữ (dùng trong lý thuyết, ví dụ)."""
    import mb_pgf
    from mb_lib import TI
    fn = tfig(P=P, segs=segs, dash=dash, right=right)
    return mb_pgf.img(fn, 'Figure', px, TI(*cap) if cap else None)
