# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 12 – Bài 9 (khoảng biến thiên, khoảng tứ phân vị) và Bài 7–8 (tọa độ trong không gian) sẽ thêm ở cuối file."""
import functools, math
from fractions import Fraction as F
from mb_selfpractice import *
from gdata import GT, nice, dec

@functools.lru_cache(maxsize=None)
def T12(seed): return nice(seed, need=('q1', 'q3', 'median'))
def _t(r): return T12(r.randint(300, 460))
def gd_range(r, lv):
    t = _t(r); v = t.rng()
    return dict(en='A frequency table: %s. The range is…' % t.html(), vi='Bảng tần số ghép nhóm: %s. Khoảng biến thiên là…' % t.html(),
      opts=pick_opts(r, dec(v), [dec(t.edge(t.k)), dec(v - t.h), dec(v + t.h), dec(t.edge(t.k - 1) - t.edge(0))], fill=lambda k: dec(v + 3 * k)), ans=0, ee='\\(R=\\)(right end of the last group)\\(-\\)(left end of the first group)\\(=%s\\).' % dec(v), ev='\\(R=\\)(đầu mút phải nhóm cuối)\\(-\\)(đầu mút trái nhóm đầu)\\(=%s\\).' % dec(v))
def gd_q1(r, lv):
    t = _t(r); i, v = t.quant(1, 4)
    return dict(en='A frequency table: %s. The first quartile \\(Q_1\\) is…' % t.html(), vi='Bảng tần số ghép nhóm: %s. Tứ phân vị thứ nhất \\(Q_1\\) là…' % t.html(),
      opts=pick_opts(r, dec(v), [dec(t.edge(i)), dec(t.mid(i)), dec(v + 1), dec(t.median())], fill=lambda k: dec(v + 2 * k)), ans=0, ee='\\(\\frac n4=%s\\) lies in %s; \\(Q_1=u+\\dfrac{n/4-C}{n_m}h=%s\\).' % (dec(F(t.n, 4)), t.label(i), dec(v)), ev='\\(\\frac n4=%s\\) thuộc nhóm %s; \\(Q_1=u+\\dfrac{n/4-C}{n_m}h=%s\\).' % (dec(F(t.n, 4)), t.label(i), dec(v)))
def gd_q3(r, lv):
    t = _t(r); i, v = t.quant(3, 4)
    return dict(en='A frequency table: %s. The third quartile \\(Q_3\\) is…' % t.html(), vi='Bảng tần số ghép nhóm: %s. Tứ phân vị thứ ba \\(Q_3\\) là…' % t.html(),
      opts=pick_opts(r, dec(v), [dec(t.edge(i)), dec(t.mid(i)), dec(v + 1), dec(t.median())], fill=lambda k: dec(v + 2 * k)), ans=0, ee='\\(\\frac{3n}4=%s\\) lies in %s; \\(Q_3=u+\\dfrac{3n/4-C}{n_m}h=%s\\).' % (dec(F(3 * t.n, 4)), t.label(i), dec(v)), ev='\\(\\frac{3n}4=%s\\) thuộc nhóm %s; \\(Q_3=u+\\dfrac{3n/4-C}{n_m}h=%s\\).' % (dec(F(3 * t.n, 4)), t.label(i), dec(v)))
def gd_iqr(r, lv):
    t = _t(r); v = t.iqr()
    return dict(en='A frequency table: %s. The interquartile range \\(\\Delta_Q\\) is…' % t.html(), vi='Bảng tần số ghép nhóm: %s. Khoảng tứ phân vị \\(\\Delta_Q\\) là…' % t.html(),
      opts=pick_opts(r, dec(v), [dec(t.q3()), dec(t.q3() + t.q1()), dec(t.rng()), dec(v + 1)], fill=lambda k: dec(v + 2 * k)), ans=0, ee='\\(\\Delta_Q=Q_3-Q_1=%s-%s=%s\\).' % (dec(t.q3()), dec(t.q1()), dec(v)), ev='\\(\\Delta_Q=Q_3-Q_1=%s-%s=%s\\).' % (dec(t.q3()), dec(t.q1()), dec(v)))
def gd_group(r, lv):
    t = _t(r); i, _ = t.quant(r.choice([1, 3]), 4) if False else t.quant(1, 4)
    return dict(en='A frequency table: %s. Which group contains \\(Q_1\\)?' % t.html(), vi='Bảng tần số ghép nhóm: %s. Nhóm nào chứa \\(Q_1\\)?' % t.html(),
      opts=pick_opts(r, t.label(i), [t.label(j) for j in range(t.k) if j != i]), ans=0, ee='\\(\\frac n4=%s\\); the cumulative frequency first reaches it in %s.' % (dec(F(t.n, 4)), t.label(i)), ev='\\(\\frac n4=%s\\); tần số tích lũy lần đầu đạt giá trị này ở nhóm %s.' % (dec(F(t.n, 4)), t.label(i)))
def gd_more(r, lv):
    a, b = _t(r), _t(r)
    if a is b or a.iqr() == b.iqr(): raise AssertionError
    return dict(en='Sample A has \\(\\Delta_Q=%s\\) and sample B has \\(\\Delta_Q=%s\\). Which sample is more spread out in the middle?' % (dec(a.iqr()), dec(b.iqr())), vi='Mẫu A có \\(\\Delta_Q=%s\\), mẫu B có \\(\\Delta_Q=%s\\). Mẫu nào phân tán nhiều hơn ở phần giữa?' % (dec(a.iqr()), dec(b.iqr())),
      opts=['Sample A' if a.iqr() > b.iqr() else 'Sample B', 'Sample B' if a.iqr() > b.iqr() else 'Sample A', 'Both are the same', 'We cannot compare'], ans=0, ee='A larger \\(\\Delta_Q\\) means a larger spread of the middle half of the data.', ev='\\(\\Delta_Q\\) lớn hơn nghĩa là một nửa số liệu ở giữa phân tán nhiều hơn.')
M9S12 = [gd_range, gd_q1, gd_q3, gd_iqr, gd_group, gd_more, gd_q1, gd_iqr]

# ---------- Bài 7, 8: tọa độ trong không gian ----------
QD = [(1, 2, 2, 3), (2, 3, 6, 7), (1, 4, 8, 9), (4, 4, 7, 9), (2, 6, 9, 11), (6, 6, 7, 11), (3, 4, 12, 13), (2, 10, 11, 15), (1, 12, 12, 17), (8, 9, 12, 17), (4, 5, 20, 21), (6, 10, 15, 19)]
def P3(p): return '(%s;%s;%s)' % tuple(fr(F(x)) for x in p)
def V3(p): return '(%s;%s;%s)' % tuple(fr(F(x)) for x in p)
def _pt(r, lo=-6, hi=6): return tuple(r.randint(lo, hi) for _ in range(3))
def _nz(r): 
    while True:
        p = _pt(r)
        if all(x != 0 for x in p): return p
def ox_proj(r, lv):
    M = _nz(r); kind = r.choice(['Oxy', 'Oyz', 'Oxz', 'Ox', 'Oy', 'Oz'])
    out = {'Oxy': (M[0], M[1], 0), 'Oyz': (0, M[1], M[2]), 'Oxz': (M[0], 0, M[2]), 'Ox': (M[0], 0, 0), 'Oy': (0, M[1], 0), 'Oz': (0, 0, M[2])}[kind]
    what = ('plane \\((%s)\\)' % kind) if len(kind) == 3 else ('axis \\(%s\\)' % kind); wvi = ('mặt phẳng \\((%s)\\)' % kind) if len(kind) == 3 else ('trục \\(%s\\)' % kind)
    return dict(en='The projection of \\(M%s\\) onto the %s is…' % (P3(M), what), vi='Hình chiếu vuông góc của \\(M%s\\) lên %s là…' % (P3(M), wvi),
      opts=pick_opts(r, P3(out), [P3((M[0], M[1], -M[2])), P3((-M[0], -M[1], 0)), P3(M), P3((M[1], M[0], 0))], fill=lambda k: P3((out[0] + k, out[1], out[2]))), ans=0, ee='Keep the coordinates that stay in the %s and set the others to 0.' % what, ev='Giữ các tọa độ ở lại trong %s, các tọa độ còn lại bằng 0.' % wvi)
def ox_sym(r, lv):
    M = _nz(r); kind = r.choice(['Oxy', 'Oyz', 'Oxz', 'Ox', 'Oy', 'Oz', 'O'])
    sg = {'Oxy': (1, 1, -1), 'Oyz': (-1, 1, 1), 'Oxz': (1, -1, 1), 'Ox': (1, -1, -1), 'Oy': (-1, 1, -1), 'Oz': (-1, -1, 1), 'O': (-1, -1, -1)}[kind]
    out = tuple(a * b for a, b in zip(M, sg)); what = {'O': 'the origin \\(O\\)'}.get(kind, ('the plane \\((%s)\\)' % kind) if len(kind) == 3 else ('the axis \\(%s\\)' % kind)); wvi = {'O': 'gốc tọa độ \\(O\\)'}.get(kind, ('mặt phẳng \\((%s)\\)' % kind) if len(kind) == 3 else ('trục \\(%s\\)' % kind))
    wr = [P3(tuple(a * b for a, b in zip(M, s))) for s in [(1, 1, -1), (-1, 1, 1), (1, -1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)] if s != sg]
    return dict(en='The point symmetric to \\(M%s\\) about %s is…' % (P3(M), what), vi='Điểm đối xứng với \\(M%s\\) qua %s là…' % (P3(M), wvi), opts=pick_opts(r, P3(out), wr), ans=0,
      ee='Change the sign of the coordinates that are not in the mirror.', ev='Đổi dấu các tọa độ không nằm trong “gương” đối xứng.')
def ox_dist(r, lv):
    a, b, c, d = r.choice(QD); A = _pt(r, -4, 4); sg = [r.choice([-1, 1]) for _ in range(3)]; v = [a, b, c]; r.shuffle(v); B = tuple(A[i] + sg[i] * v[i] for i in range(3))
    return dict(en='\\(A%s\\) and \\(B%s\\). The length \\(AB\\) is…' % (P3(A), P3(B)), vi='Cho \\(A%s\\), \\(B%s\\). Độ dài \\(AB\\) bằng…' % (P3(A), P3(B)), opts=pick_opts(r, str(d), [str(a + b + c), str(d + 1), str(d - 1), str(a * a + b * b + c * c)], fill=lambda k: str(d + 2 * k)), ans=0,
      ee='\\(AB=\\sqrt{(x_B-x_A)^2+(y_B-y_A)^2+(z_B-z_A)^2}=\\sqrt{%d}=%d\\).' % (d * d, d), ev='\\(AB=\\sqrt{(x_B-x_A)^2+(y_B-y_A)^2+(z_B-z_A)^2}=\\sqrt{%d}=%d\\).' % (d * d, d))
def ox_mid(r, lv):
    A = _pt(r); B = tuple(a + 2 * r.randint(-4, 4) for a in A); m = tuple(F(a + b, 2) for a, b in zip(A, B))
    return dict(en='\\(A%s\\), \\(B%s\\). The midpoint \\(I\\) of \\(AB\\) is…' % (P3(A), P3(B)), vi='Cho \\(A%s\\), \\(B%s\\). Trung điểm \\(I\\) của \\(AB\\) là…' % (P3(A), P3(B)), opts=pick_opts(r, P3(m), [P3(tuple(a + b for a, b in zip(A, B))), P3(tuple(F(b - a, 2) for a, b in zip(A, B))), P3(tuple(b - a for a, b in zip(A, B))), P3(tuple(m_ + 1 for m_ in m))], fill=lambda k: P3(tuple(m_ + k for m_ in m))), ans=0, ee='\\(I=\\left(\\dfrac{x_A+x_B}2;\\dfrac{y_A+y_B}2;\\dfrac{z_A+z_B}2\\right)\\).', ev='\\(I=\\left(\\dfrac{x_A+x_B}2;\\dfrac{y_A+y_B}2;\\dfrac{z_A+z_B}2\\right)\\).')
def ox_cent(r, lv):
    A, B = _pt(r), _pt(r); G = _pt(r, -3, 3); C = tuple(3 * g - a - b for g, a, b in zip(G, A, B))
    return dict(en='\\(A%s\\), \\(B%s\\), \\(C%s\\). The centroid \\(G\\) of triangle \\(ABC\\) is…' % (P3(A), P3(B), P3(C)), vi='Cho \\(A%s\\), \\(B%s\\), \\(C%s\\). Trọng tâm \\(G\\) của tam giác \\(ABC\\) là…' % (P3(A), P3(B), P3(C)),
      opts=pick_opts(r, P3(G), [P3(tuple(a + b + c for a, b, c in zip(A, B, C))), P3(tuple(F(a + b + c, 2) for a, b, c in zip(A, B, C))), P3(tuple(g + 1 for g in G))], fill=lambda k: P3(tuple(g + k for g in G))), ans=0, ee='\\(G=\\left(\\dfrac{x_A+x_B+x_C}3;\\dfrac{y_A+y_B+y_C}3;\\dfrac{z_A+z_B+z_C}3\\right)\\).', ev='\\(G=\\left(\\dfrac{x_A+x_B+x_C}3;\\dfrac{y_A+y_B+y_C}3;\\dfrac{z_A+z_B+z_C}3\\right)\\).')
def ox_pgm(r, lv):
    A, B, C = _pt(r), _pt(r), _pt(r); D = tuple(a + c - b for a, b, c in zip(A, B, C))
    return dict(en='\\(ABCD\\) is a parallelogram with \\(A%s\\), \\(B%s\\), \\(C%s\\). Then \\(D\\) is…' % (P3(A), P3(B), P3(C)), vi='Cho hình bình hành \\(ABCD\\) có \\(A%s\\), \\(B%s\\), \\(C%s\\). Khi đó \\(D\\) là…' % (P3(A), P3(B), P3(C)),
      opts=pick_opts(r, P3(D), [P3(tuple(b + c - a for a, b, c in zip(A, B, C))), P3(tuple(a + b - c for a, b, c in zip(A, B, C))), P3(tuple(a + b + c for a, b, c in zip(A, B, C)))], fill=lambda k: P3(tuple(d + k for d in D))), ans=0, ee='\\(\\overrightarrow{AB}=\\overrightarrow{DC}\\), so \\(D=A+C-B\\).', ev='\\(\\overrightarrow{AB}=\\overrightarrow{DC}\\) nên \\(D=A+C-B\\).')
def ox_daxis(r, lv):
    a, b, c, d = r.choice(QD); M = (r.choice([-3, 2, 5]), r.choice([-1, 1]) * b, r.choice([-1, 1]) * c) ; M = (M[0], M[1], M[2]); ax = r.choice(['Ox', 'Oy', 'Oz'])
    xs = {'Ox': (M[0], M[1], M[2]), 'Oy': (M[1], M[0], M[2]), 'Oz': (M[1], M[2], M[0])}[ax]; Mx = {'Ox': xs, 'Oy': (xs[1], xs[0], xs[2]), 'Oz': (xs[2], xs[0], xs[1])}[ax]
    if ax == 'Ox': h = (b, c)
    elif ax == 'Oy': Mx = (M[1], M[0], M[2]); h = (M[1], M[2])
    else: Mx = (M[1], M[2], M[0]); h = (M[1], M[2])
    dd = math.hypot(*h); assert abs(dd - round(dd)) < 1e-9; dd = round(dd)
    return dict(en='The distance from \\(M%s\\) to the axis \\(%s\\) is…' % (P3(Mx), ax), vi='Khoảng cách từ \\(M%s\\) đến trục \\(%s\\) bằng…' % (P3(Mx), ax),
      opts=pick_opts(r, str(dd), [str(abs(h[0]) + abs(h[1])), str(abs(h[0])), str(abs(h[1])), str(dd + 1)], fill=lambda k: str(dd + 2 * k)), ans=0, ee='The distance is \\(\\sqrt{}\\) of the sum of squares of the other two coordinates: %d.' % dd, ev='Khoảng cách bằng căn của tổng bình phương hai tọa độ còn lại: %d.' % dd)
M7S12 = [ox_proj, ox_sym, ox_dist, ox_mid, ox_cent, ox_pgm, ox_proj, ox_dist]

def _vec(r, lo=-5, hi=5): return tuple(r.randint(lo, hi) for _ in range(3))
def ob_sum(r, lv):
    a, b = _vec(r), _vec(r); s1, s2 = r.choice([(1, 1), (1, -1), (2, 1), (2, -3), (3, -1), (-1, 2)]); res = tuple(s1 * x + s2 * y for x, y in zip(a, b))
    ex = '%s\\vec a%s\\vec b' % ('' if s1 == 1 else str(s1), ('+' if s2 > 0 else '-') + ('' if abs(s2) == 1 else str(abs(s2))))
    return dict(en='\\(\\vec a=%s\\), \\(\\vec b=%s\\). Then \\(%s=\\)…' % (V3(a), V3(b), ex), vi='Cho \\(\\vec a=%s\\), \\(\\vec b=%s\\). Khi đó \\(%s=\\)…' % (V3(a), V3(b), ex), opts=pick_opts(r, V3(res), [V3(tuple(s1 * x - s2 * y for x, y in zip(a, b))), V3(tuple(x + y for x, y in zip(a, b))), V3(tuple(x - y for x, y in zip(a, b))), V3(tuple(s2 * x + s1 * y for x, y in zip(a, b)))], fill=lambda k: V3(tuple(z + k for z in res))), ans=0, ee='Do each coordinate separately.', ev='Tính từng tọa độ riêng.')
def ob_dot(r, lv):
    a, b = _vec(r), _vec(r); d = sum(x * y for x, y in zip(a, b))
    return dict(en='\\(\\vec a=%s\\), \\(\\vec b=%s\\). Then \\(\\vec a\\cdot\\vec b=\\)…' % (V3(a), V3(b)), vi='Cho \\(\\vec a=%s\\), \\(\\vec b=%s\\). Khi đó \\(\\vec a\\cdot\\vec b=\\)…' % (V3(a), V3(b)), opts=pick_opts(r, str(d), [str(-d), str(d + 2), str(d - 2), str(a[0] * b[0] + a[1] * b[1])], fill=lambda k: str(d + 3 * k)), ans=0, ee='\\(\\vec a\\cdot\\vec b=x_1x_2+y_1y_2+z_1z_2=%d\\).' % d, ev='\\(\\vec a\\cdot\\vec b=x_1x_2+y_1y_2+z_1z_2=%d\\).' % d)
def ob_len(r, lv):
    a, b, c, d = r.choice(QD); v = [r.choice([-1, 1]) * x for x in (a, b, c)]; r.shuffle(v)
    return dict(en='\\(\\vec a=%s\\). Then \\(|\\vec a|=\\)…' % V3(v), vi='Cho \\(\\vec a=%s\\). Khi đó \\(|\\vec a|=\\)…' % V3(v), opts=pick_opts(r, str(d), [str(a + b + c), str(d * d), str(d + 1), str(d - 1)], fill=lambda k: str(d + 2 * k)), ans=0, ee='\\(|\\vec a|=\\sqrt{x^2+y^2+z^2}=\\sqrt{%d}=%d\\).' % (d * d, d), ev='\\(|\\vec a|=\\sqrt{x^2+y^2+z^2}=\\sqrt{%d}=%d\\).' % (d * d, d))
def ob_perp(r, lv):
    while True:
        a = _vec(r, -4, 4); m = r.randint(-5, 5); b0 = (r.randint(-4, 4), r.randint(-4, 4)); b = (b0[0], b0[1], 0)
        if a[2] != 0: 
            # a·b = a0 b0 + a1 b1 + a2 * t = 0 với t = m
            t = F(-(a[0] * b0[0] + a[1] * b0[1]), a[2])
            if t.denominator == 1: break
    m = int(t)
    return dict(en='\\(\\vec a=%s\\), \\(\\vec b=(%d;%d;m)\\). Find \\(m\\) so that \\(\\vec a\\perp\\vec b\\).' % (V3(a), b0[0], b0[1]), vi='Cho \\(\\vec a=%s\\), \\(\\vec b=(%d;%d;m)\\). Tìm \\(m\\) để \\(\\vec a\\perp\\vec b\\).' % (V3(a), b0[0], b0[1]),
      opts=pick_opts(r, str(m), [str(-m), str(m + 1), str(m - 1), '0'], fill=lambda k: str(m + 3 * k)), ans=0, ee='\\(\\vec a\\cdot\\vec b=0\\) gives a linear equation in \\(m\\): \\(m=%d\\).' % m, ev='\\(\\vec a\\cdot\\vec b=0\\) cho phương trình bậc nhất theo \\(m\\): \\(m=%d\\).' % m)
def ob_col(r, lv):
    a = _vec(r, 1, 4); k = r.choice([2, 3, -2, -1, F(1, 2)]); b = tuple(x * k for x in a)
    if any(F(x).denominator != 1 for x in b): raise AssertionError
    m = b[2]
    return dict(en='\\(\\vec a=%s\\), \\(\\vec b=(%d;%d;m)\\) are collinear. Find \\(m\\).' % (V3(a), b[0], b[1]), vi='Cho \\(\\vec a=%s\\), \\(\\vec b=(%d;%d;m)\\) cùng phương. Tìm \\(m\\).' % (V3(a), b[0], b[1]),
      opts=pick_opts(r, str(m), [str(-m), str(m + 1), str(a[2]), str(m - 1)], fill=lambda j: str(m + 2 * j)), ans=0, ee='\\(\\vec b=k\\vec a\\) with \\(k=%s\\); so \\(m=%d\\).' % (fr(F(k)), m), ev='\\(\\vec b=k\\vec a\\) với \\(k=%s\\); suy ra \\(m=%d\\).' % (fr(F(k)), m))
def ob_cos(r, lv):
    tab = {F(1, 2): '\\dfrac12', F(-1, 2): '-\\dfrac12', F(0): '0', F(1, 3): '\\dfrac13', F(-1, 3): '-\\dfrac13', F(2, 3): '\\dfrac23', F(-2, 3): '-\\dfrac23', F(1): '1', F(-1): '-1'}
    for _ in range(4000):
        a, b = _vec(r, -3, 3), _vec(r, -3, 3); na, nb = sum(x * x for x in a), sum(x * x for x in b)
        if na == 0 or nb == 0: continue
        sa, sb = math.isqrt(na), math.isqrt(nb)
        if sa * sa != na or sb * sb != nb: continue
        c = F(sum(x * y for x, y in zip(a, b)), sa * sb)
        if c in tab and c not in (1, -1): break
    else: raise AssertionError
    opts = ['\\dfrac12', '-\\dfrac12', '0', '\\dfrac13', '-\\dfrac13', '\\dfrac23', '-\\dfrac23']; cc = tab[c]
    return dict(en='\\(\\vec a=%s\\), \\(\\vec b=%s\\). Then \\(\\cos(\\vec a,\\vec b)=\\)…' % (V3(a), V3(b)), vi='Cho \\(\\vec a=%s\\), \\(\\vec b=%s\\). Khi đó \\(\\cos(\\vec a,\\vec b)=\\)…' % (V3(a), V3(b)), opts=pick_opts(r, cc, [o for o in opts if o != cc]), ans=0, ee='\\(\\cos=\\dfrac{\\vec a\\cdot\\vec b}{|\\vec a||\\vec b|}\\).', ev='\\(\\cos=\\dfrac{\\vec a\\cdot\\vec b}{|\\vec a||\\vec b|}\\).')
M8S12 = [ob_sum, ob_dot, ob_len, ob_perp, ob_col, ob_cos, ob_sum, ob_dot]
