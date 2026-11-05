# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 11 – Bài 10, 11 (quan hệ song song trong không gian). Số cặp cạnh được đếm bằng tọa độ nguyên (chính xác)."""
import itertools
from fractions import Fraction as F
from mb_selfpractice import *

def _cross(a, b): return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
def _dot(a, b): return sum(x * y for x, y in zip(a, b))
def _sub(a, b): return tuple(x - y for x, y in zip(a, b))
SOL = {
 'cube': ({'A': (0, 0, 0), 'B': (1, 0, 0), 'C': (1, 1, 0), 'D': (0, 1, 0), 'A′': (0, 0, 1), 'B′': (1, 0, 1), 'C′': (1, 1, 1), 'D′': (0, 1, 1)}, lambda a, b: sum(x != y for x, y in zip(a, b)) == 1),
 'box': ({'A': (0, 0, 0), 'B': (2, 0, 0), 'C': (2, 3, 0), 'D': (0, 3, 0), 'A′': (0, 0, 4), 'B′': (2, 0, 4), 'C′': (2, 3, 4), 'D′': (0, 3, 4)}, lambda a, b: sum(x != y for x, y in zip(a, b)) == 1),
 'tetra': ({'A': (0, 0, 0), 'B': (1, 0, 0), 'C': (0, 1, 0), 'D': (0, 0, 1)}, lambda a, b: True),
 'pyr': ({'A': (0, 0, 0), 'B': (2, 0, 0), 'C': (2, 2, 0), 'D': (0, 2, 0), 'S': (1, 1, 2)}, None),
 'prism': ({'A': (0, 0, 0), 'B': (2, 0, 0), 'C': (0, 2, 0), 'A′': (0, 0, 3), 'B′': (2, 0, 3), 'C′': (0, 2, 3)}, None),
}
def edges(name):
    P = SOL[name][0]
    if name == 'pyr': return [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('S', 'A'), ('S', 'B'), ('S', 'C'), ('S', 'D')]
    if name == 'prism': return [('A', 'B'), ('B', 'C'), ('C', 'A'), ('A′', 'B′'), ('B′', 'C′'), ('C′', 'A′'), ('A', 'A′'), ('B', 'B′'), ('C', 'C′')]
    f = SOL[name][1]; ks = list(P); return [(a, b) for a, b in itertools.combinations(ks, 2) if f(P[a], P[b])]
def rel(name, e1, e2):
    P = SOL[name][0]; d1, d2 = _sub(P[e1[1]], P[e1[0]]), _sub(P[e2[1]], P[e2[0]]); c = _cross(d1, d2)
    if c == (0, 0, 0): return 'par'
    return 'int' if _dot(_sub(P[e2[0]], P[e1[0]]), c) == 0 else 'skew'
def count(name, kind): return sum(1 for a, b in itertools.combinations(edges(name), 2) if rel(name, a, b) == kind)
NM = {'cube': ('a cube', 'hình lập phương'), 'box': ('a rectangular box ABCD.A′B′C′D′', 'hình hộp chữ nhật ABCD.A′B′C′D′'), 'tetra': ('a tetrahedron', 'tứ diện'), 'pyr': ('the pyramid S.ABCD with a square base', 'hình chóp S.ABCD đáy hình vuông'), 'prism': ('a triangular prism ABC.A′B′C′', 'lăng trụ tam giác ABC.A′B′C′')}
KN = {'par': ('parallel', 'song song với nhau'), 'skew': ('skew (not coplanar)', 'chéo nhau'), 'int': ('intersecting', 'cắt nhau')}
def pr_count(r, lv):
    name = r.choice(['cube', 'box', 'tetra', 'pyr', 'prism']); kind = r.choice(['par', 'skew', 'int']); c = count(name, kind)
    if c == 0: raise AssertionError
    return dict(en='How many pairs of edges of %s are %s?' % (NM[name][0], KN[kind][0]), vi='Có bao nhiêu cặp cạnh của %s %s?' % (NM[name][1], KN[kind][1]),
      opts=pick_opts(r, str(c), [str(c + 1), str(c - 1), str(c * 2), str(c + 6)], fill=lambda k: str(c + 3 * k)), ans=0, ee='Check every pair of edges: %d pair(s).' % c, ev='Xét mọi cặp cạnh: có %d cặp.' % c)
def pr_mid(r, lv):
    x = r.choice([6, 8, 10, 12, 14, 16, 18, 20]); a = r.choice(['MN', 'IJ', 'EF', 'PQ']); s = r.choice(['SA', 'SB', 'SC']); tri = r.choice(['SAB', 'SBC', 'SAC'])
    P = tri[0]; Q, R = tri[1], tri[2]
    return dict(en='In the pyramid, M and N are the midpoints of %s%s and %s%s. If %s%s = %d, then MN = …' % (P, Q, P, R, Q, R, x), vi='Trong hình chóp, M, N lần lượt là trung điểm của %s%s và %s%s. Nếu %s%s = %d thì MN = …' % (P, Q, P, R, Q, R, x),
      opts=pick_opts(r, str(x // 2), [str(x), str(2 * x), str(x // 2 + 1), str(x - 2)], fill=lambda k: str(x // 2 + 2 * k)), ans=0, ee='MN is a midline of the triangle: \\(MN\\parallel %s%s\\), \\(MN=\\dfrac12%s%s\\).' % (Q, R, Q, R), ev='MN là đường trung bình của tam giác: \\(MN\\parallel %s%s\\), \\(MN=\\dfrac12%s%s\\).' % (Q, R, Q, R))
def pr_perim(r, lv):
    a, b = r.choice([(6, 8), (10, 12), (8, 14), (12, 16), (6, 10), (14, 18), (4, 10), (16, 20), (18, 24), (20, 30), (12, 18), (10, 16)])
    return dict(en='In the tetrahedron ABCD, M, N, P, Q are the midpoints of AB, BC, CD, DA. If AC = %d and BD = %d, the perimeter of MNPQ is…' % (a, b), vi='Cho tứ diện ABCD, M, N, P, Q lần lượt là trung điểm của AB, BC, CD, DA. Biết AC = %d, BD = %d. Chu vi tứ giác MNPQ bằng…' % (a, b),
      opts=pick_opts(r, str(a + b), [str((a + b) // 2), str(2 * (a + b)), str(a * b // 2), str(a + b + 2)], fill=lambda k: str(a + b + 3 * k)), ans=0, ee='\\(MN=PQ=\\dfrac12AC\\) and \\(NP=MQ=\\dfrac12BD\\): perimeter \\(=AC+BD\\).', ev='\\(MN=PQ=\\dfrac12AC\\) và \\(NP=MQ=\\dfrac12BD\\): chu vi \\(=AC+BD\\).')
def pr_area(r, lv):
    a, b = r.choice([(6, 8), (10, 12), (8, 14), (12, 16), (6, 10), (14, 18), (4, 10), (20, 6), (16, 20), (18, 24), (20, 30), (12, 18), (8, 18), (10, 18)])
    return dict(en='In the tetrahedron ABCD, AC ⊥ BD, AC = %d, BD = %d, and M, N, P, Q are the midpoints of AB, BC, CD, DA. The area of MNPQ is…' % (a, b), vi='Cho tứ diện ABCD có AC ⊥ BD, AC = %d, BD = %d; M, N, P, Q là trung điểm của AB, BC, CD, DA. Diện tích tứ giác MNPQ bằng…' % (a, b),
      opts=pick_opts(r, str(a * b // 4), [str(a * b // 2), str(a * b), str((a + b) // 2), str(a * b // 4 + 2)], fill=lambda k: str(a * b // 4 + 3 * k)), ans=0, ee='MNPQ is a rectangle with sides \\(\\frac{AC}2\\) and \\(\\frac{BD}2\\): area \\(\\frac{AC\\cdot BD}4\\).', ev='MNPQ là hình chữ nhật có hai cạnh \\(\\frac{AC}2\\), \\(\\frac{BD}2\\): diện tích \\(\\frac{AC\\cdot BD}4\\).')
M11G = [pr_count, pr_mid, pr_perim, pr_area, pr_count, pr_mid, pr_area, pr_perim]

def sc_planes(r, lv):
    n = r.choice([4, 5, 6, 7, 8, 9, 10, 11, 12]); c = n * (n - 1) * (n - 2) // 6
    return dict(en='There are %d points in space, no four of them in one plane. How many planes pass through three of them?' % n, vi='Cho %d điểm trong không gian, không có bốn điểm nào đồng phẳng. Có bao nhiêu mặt phẳng đi qua ba trong số các điểm đó?' % n,
      opts=pick_opts(r, str(c), [str(n * (n - 1) // 2), str(c * 2), str(n * (n - 1) * (n - 2)), str(c + n)], fill=lambda k: str(c + 2 * k)), ans=0, ee='Choose 3 points out of %d: \\(\\binom{%d}{3}=%d\\).' % (n, n, c), ev='Chọn 3 điểm trong %d điểm: \\(\\binom{%d}{3}=%d\\).' % (n, n, c))
def sc_lines(r, lv):
    n = r.choice([4, 5, 6, 7, 8, 9, 10, 11, 12]); c = n * (n - 1) // 2
    return dict(en='There are %d points, no three on a line. How many lines pass through two of them?' % n, vi='Cho %d điểm, không có ba điểm nào thẳng hàng. Có bao nhiêu đường thẳng đi qua hai trong số các điểm đó?' % n,
      opts=pick_opts(r, str(c), [str(n * (n - 1)), str(c + n), str(c - 1), str(n)], fill=lambda k: str(c + 2 * k)), ans=0, ee='\\(\\binom{%d}{2}=%d\\).' % (n, c), ev='\\(\\binom{%d}{2}=%d\\).' % (n, c))
def sc_pyr(r, lv):
    n = r.choice([3, 4, 5, 6, 7, 8]); kind = r.choice(['faces', 'edges', 'verts'])
    ans = {'faces': n + 1, 'edges': 2 * n, 'verts': n + 1}[kind]
    nmv = {'faces': ('faces', 'mặt'), 'edges': ('edges', 'cạnh'), 'verts': ('vertices', 'đỉnh')}[kind]
    return dict(en='A pyramid has a base with %d sides. How many %s does it have?' % (n, nmv[0]), vi='Hình chóp có đáy là đa giác %d cạnh. Hình chóp đó có bao nhiêu %s?' % (n, nmv[1]),
      opts=pick_opts(r, str(ans), [str(ans + 1), str(ans - 1), str(n), str(3 * n)], fill=lambda k: str(ans + 2 * k)), ans=0, ee='Base: %d sides. Count: %d.' % (n, ans), ev='Đáy có %d cạnh. Đáp số: %d.' % (n, ans))
def sc_prism(r, lv):
    n = r.choice([3, 4, 5, 6, 7]); kind = r.choice(['faces', 'edges', 'verts'])
    ans = {'faces': n + 2, 'edges': 3 * n, 'verts': 2 * n}[kind]; nmv = {'faces': ('faces', 'mặt'), 'edges': ('edges', 'cạnh'), 'verts': ('vertices', 'đỉnh')}[kind]
    return dict(en='A prism has a base with %d sides. How many %s does it have?' % (n, nmv[0]), vi='Hình lăng trụ có đáy là đa giác %d cạnh. Hình lăng trụ đó có bao nhiêu %s?' % (n, nmv[1]),
      opts=pick_opts(r, str(ans), [str(ans + 1), str(ans - 1), str(2 * n + 1), str(n + 1)], fill=lambda k: str(ans + 2 * k)), ans=0, ee='Two bases with %d sides each, and %d lateral edges. Count: %d.' % (n, n, ans), ev='Hai đáy mỗi đáy %d cạnh, %d cạnh bên. Đáp số: %d.' % (n, n, ans))
def sc_diag(r, lv):
    n = r.choice([5, 6, 7, 8, 9, 10]); c = n * (n - 3) // 2
    return dict(en='A convex polygon has %d sides. How many diagonals does it have?' % n, vi='Một đa giác lồi có %d cạnh. Có bao nhiêu đường chéo?' % n,
      opts=pick_opts(r, str(c), [str(n * (n - 1) // 2), str(c + n), str(n * (n - 3)), str(c - 1)], fill=lambda k: str(c + 2 * k)), ans=0, ee='\\(\\dfrac{n(n-3)}2=%d\\).' % c, ev='\\(\\dfrac{n(n-3)}2=%d\\).' % c)
M10G = [sc_planes, sc_lines, sc_pyr, sc_prism, sc_diag, sc_planes, sc_pyr, sc_prism]
