# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 10 – Bài 10 (vectơ trong mặt phẳng tọa độ), Bài 11 (tích vô hướng), Bài 12 (số gần đúng và sai số).
Mỗi builder(r, lv) trả dict(en, vi, opts[4], ans=0, ee, ev); đáp án do máy tính tính (Fraction / số nguyên), không nhập tay."""
import math
from fractions import Fraction as F
from mb_selfpractice import pick_opts, fr
from freqtable import num
from mb_lib import TI
def TT(en, vi): return '§' + TI(en, vi)

def P2(p): return '(%s;\\,%s)' % (fr(p[0]), fr(p[1]))
def V2(p): return '(%s;\\,%s)' % (fr(p[0]), fr(p[1]))
def ov(a, b): return '\\overrightarrow{%s%s}' % (a, b)
def _pt(r, lo=-6, hi=6): return (r.randint(lo, hi), r.randint(lo, hi))
def add(p, q, s=1, t=1): return (s * p[0] + t * q[0], s * p[1] + t * q[1])
def dot(p, q): return p[0] * q[0] + p[1] * q[1]
TRIPLES = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 6, 10), (4, 3, 5), (12, 5, 13), (9, 12, 15), (8, 15, 17), (0, 7, 7), (6, 0, 6)]

# ================= Bài 10. Vectơ trong mặt phẳng tọa độ =================
def c_ab(r, lv):
    A, B = _pt(r), _pt(r); assert A != B; v = add(B, A, 1, -1)
    return dict(en='\\(A%s\\), \\(B%s\\). The coordinates of \\(%s\\) are…' % (P2(A), P2(B), ov('A', 'B')), vi='Cho \\(A%s\\), \\(B%s\\). Tọa độ của \\(%s\\) là…' % (P2(A), P2(B), ov('A', 'B')),
      opts=pick_opts(r, V2(v), [V2(add(A, B, 1, -1)), V2(add(A, B)), V2((v[1], v[0])), V2((v[0], -v[1]))], fill=lambda k: V2((v[0] + k, v[1]))), ans=0,
      ee='End minus start: \\(%s=(x_B-x_A;\\,y_B-y_A)=%s\\).' % (ov('A', 'B'), V2(v)), ev='Lấy điểm cuối trừ điểm đầu: \\(%s=(x_B-x_A;\\,y_B-y_A)=%s\\).' % (ov('A', 'B'), V2(v)))
def c_comb(r, lv):
    a, b = _pt(r, -5, 5), _pt(r, -5, 5); s, t = r.choice([(2, 1), (2, -1), (3, -2), (1, -3), (-1, 2), (2, 3)]); res = add(a, b, s, t)
    ex = '%s\\vec a%s\\vec b' % ({1: '', -1: '-'}.get(s, str(s)), ('+' if t > 0 else '-') + ('' if abs(t) == 1 else str(abs(t))))
    return dict(en='\\(\\vec a=%s\\), \\(\\vec b=%s\\). Then \\(%s=\\)…' % (V2(a), V2(b), ex), vi='Cho \\(\\vec a=%s\\), \\(\\vec b=%s\\). Khi đó \\(%s=\\)…' % (V2(a), V2(b), ex),
      opts=pick_opts(r, V2(res), [V2(add(a, b, s, -t)), V2(add(a, b, t, s)), V2(add(a, b)), V2((res[0], -res[1]))], fill=lambda k: V2((res[0] + k, res[1] - k))), ans=0,
      ee='Multiply first, then add coordinate by coordinate: \\(%s\\).' % V2(res), ev='Nhân trước rồi cộng theo từng tọa độ: \\(%s\\).' % V2(res))
def c_len(r, lv):
    a, b, c = r.choice(TRIPLES); u = (r.choice([-1, 1]) * a, r.choice([-1, 1]) * b)
    return dict(en='The length of \\(\\vec u=%s\\) is…' % V2(u), vi='Độ dài của vectơ \\(\\vec u=%s\\) bằng…' % V2(u),
      opts=pick_opts(r, str(c), [str(a + b), str(c * c), str(abs(u[0] + u[1])), str(c + 1)], fill=lambda k: str(c + 2 * k)), ans=0,
      ee='\\(|\\vec u|=\\sqrt{%d^2+%d^2}=\\sqrt{%d}=%d\\).' % (a, b, c * c, c), ev='\\(|\\vec u|=\\sqrt{%d^2+%d^2}=\\sqrt{%d}=%d\\).' % (a, b, c * c, c))
def c_mid(r, lv):
    A = _pt(r); B = (A[0] + 2 * r.randint(-4, 4), A[1] + 2 * r.randint(-4, 4)); assert A != B; I = (F(A[0] + B[0], 2), F(A[1] + B[1], 2))
    return dict(en='\\(A%s\\), \\(B%s\\). The midpoint \\(I\\) of \\(AB\\) is…' % (P2(A), P2(B)), vi='Cho \\(A%s\\), \\(B%s\\). Trung điểm \\(I\\) của \\(AB\\) là…' % (P2(A), P2(B)),
      opts=pick_opts(r, P2(I), [P2(add(A, B)), P2((F(B[0] - A[0], 2), F(B[1] - A[1], 2))), P2(add(B, A, 1, -1)), P2((I[1], I[0]))], fill=lambda k: P2((I[0] + k, I[1]))), ans=0,
      ee='\\(I=\\left(\\dfrac{x_A+x_B}2;\\dfrac{y_A+y_B}2\\right)=%s\\).' % P2(I), ev='\\(I=\\left(\\dfrac{x_A+x_B}2;\\dfrac{y_A+y_B}2\\right)=%s\\).' % P2(I))
def c_cent(r, lv):
    A, B = _pt(r), _pt(r); G = _pt(r, -3, 3); C = (3 * G[0] - A[0] - B[0], 3 * G[1] - A[1] - B[1]); assert len({A, B, C}) == 3 and (B[0] - A[0]) * (C[1] - A[1]) != (B[1] - A[1]) * (C[0] - A[0])
    return dict(en='\\(A%s\\), \\(B%s\\), \\(C%s\\). The centroid \\(G\\) of triangle \\(ABC\\) is…' % (P2(A), P2(B), P2(C)), vi='Cho \\(A%s\\), \\(B%s\\), \\(C%s\\). Trọng tâm \\(G\\) của tam giác \\(ABC\\) là…' % (P2(A), P2(B), P2(C)),
      opts=pick_opts(r, P2(G), [P2((3 * G[0], 3 * G[1])), P2((F(3 * G[0], 2), F(3 * G[1], 2))), P2((G[1], G[0])), P2((G[0] + 1, G[1] - 1))], fill=lambda k: P2((G[0] + k, G[1] + k))), ans=0,
      ee='\\(G=\\left(\\dfrac{x_A+x_B+x_C}3;\\dfrac{y_A+y_B+y_C}3\\right)=%s\\).' % P2(G), ev='\\(G=\\left(\\dfrac{x_A+x_B+x_C}3;\\dfrac{y_A+y_B+y_C}3\\right)=%s\\).' % P2(G))
def c_pgm(r, lv):
    A, B, C = _pt(r), _pt(r), _pt(r); assert (B[0] - A[0]) * (C[1] - A[1]) != (B[1] - A[1]) * (C[0] - A[0]); D = (A[0] + C[0] - B[0], A[1] + C[1] - B[1])
    return dict(en='\\(ABCD\\) is a parallelogram with \\(A%s\\), \\(B%s\\), \\(C%s\\). Then \\(D\\) is…' % (P2(A), P2(B), P2(C)), vi='Cho hình bình hành \\(ABCD\\) có \\(A%s\\), \\(B%s\\), \\(C%s\\). Tọa độ đỉnh \\(D\\) là…' % (P2(A), P2(B), P2(C)),
      opts=pick_opts(r, P2(D), [P2((B[0] + C[0] - A[0], B[1] + C[1] - A[1])), P2((A[0] + B[0] - C[0], A[1] + B[1] - C[1])), P2((A[0] + B[0] + C[0], A[1] + B[1] + C[1]))], fill=lambda k: P2((D[0] + k, D[1]))), ans=0,
      ee='\\(%s=%s\\) gives \\(D=A+C-B=%s\\).' % (ov('A', 'D'), ov('B', 'C'), P2(D)), ev='\\(%s=%s\\) nên \\(D=A+C-B=%s\\).' % (ov('A', 'D'), ov('B', 'C'), P2(D)))
def c_colm(r, lv):
    a = r.choice([1, 2, 3, -2]); b = r.choice([2, 3, -1, 4, -3]); k = r.choice([2, 3, -2, -1, F(1, 2)]); m = a * k; c = b * k
    assert F(m).denominator == 1 and F(c).denominator == 1; m, c = int(m), int(c)
    return dict(en='\\(\\vec u=%s\\) and \\(\\vec v=(m;\\,%d)\\). The vectors are collinear when \\(m=\\)…' % (V2((a, b)), c), vi='Cho \\(\\vec u=%s\\), \\(\\vec v=(m;\\,%d)\\). Hai vectơ cùng phương khi \\(m=\\)…' % (V2((a, b)), c),
      opts=pick_opts(r, str(m), [str(-m), fr(F(b * c, a)) if a else '0', str(m + 1), fr(F(c, b) / a) if a else '1'], fill=lambda k: str(m + 2 * k)), ans=0,
      ee='Collinear: \\(\\dfrac{m}{%d}=\\dfrac{%d}{%d}\\), so \\(m=%d\\).' % (a, c, b, m), ev='Cùng phương: \\(\\dfrac{m}{%d}=\\dfrac{%d}{%d}\\) nên \\(m=%d\\).' % (a, c, b, m))
def c_robot(r, lv):
    A = _pt(r, -3, 3); u, w = _pt(r, -4, 4), _pt(r, -4, 4); assert u != (0, 0) and w != (0, 0); E = add(add(A, u), w)
    return dict(en='On a game map, a robot starts at \\(A%s\\). It moves by \\(\\vec u=%s\\), then by \\(\\vec w=%s\\). Where does it stop?' % (P2(A), V2(u), V2(w)),
      vi='Trên bản đồ một trò chơi, rô-bốt xuất phát tại \\(A%s\\), di chuyển theo \\(\\vec u=%s\\) rồi theo \\(\\vec w=%s\\). Rô-bốt dừng ở điểm nào?' % (P2(A), V2(u), V2(w)),
      opts=pick_opts(r, P2(E), [P2(add(u, w)), P2(add(A, u)), P2(add(add(A, u), w, 1, -1)), P2((E[1], E[0]))], fill=lambda k: P2((E[0] + k, E[1]))), ans=0,
      ee='Final point \\(=A+\\vec u+\\vec w=%s\\).' % P2(E), ev='Điểm dừng \\(=A+\\vec u+\\vec w=%s\\).' % P2(E))
M10S10 = [c_ab, c_comb, c_len, c_mid, c_cent, c_pgm, c_colm, c_robot]

# ================= Bài 11. Tích vô hướng của hai vectơ =================
COS = {0: F(1), 60: F(1, 2), 90: F(0), 120: F(-1, 2), 180: F(-1)}
def d_def(r, lv):
    a, b = r.choice([(2, 3), (4, 5), (3, 6), (2, 7), (6, 4), (5, 8)]); th = r.choice([60, 120, 90, 180, 0]); v = a * b * COS[th]
    return dict(en='\\(|\\vec a|=%d\\), \\(|\\vec b|=%d\\) and \\((\\vec a,\\vec b)=%d^\\circ\\). Then \\(\\vec a\\cdot\\vec b=\\)…' % (a, b, th), vi='Cho \\(|\\vec a|=%d\\), \\(|\\vec b|=%d\\), \\((\\vec a,\\vec b)=%d^\\circ\\). Khi đó \\(\\vec a\\cdot\\vec b=\\)…' % (a, b, th),
      opts=pick_opts(r, fr(v), [fr(a * b), fr(-v) if v else str(a + b), fr(F(a * b, 2)) if v != F(a * b, 2) else fr(2 * a * b), str(a + b)], fill=lambda k: fr(v + k)), ans=0,
      ee='\\(\\vec a\\cdot\\vec b=|\\vec a|\\,|\\vec b|\\cos%d^\\circ=%d\\cdot%d\\cdot%s=%s\\).' % (th, a, b, fr(COS[th]), fr(v)), ev='\\(\\vec a\\cdot\\vec b=|\\vec a|\\,|\\vec b|\\cos%d^\\circ=%d\\cdot%d\\cdot%s=%s\\).' % (th, a, b, fr(COS[th]), fr(v)))
def d_coord(r, lv):
    a, b = _pt(r, -5, 5), _pt(r, -5, 5); v = dot(a, b)
    return dict(en='\\(\\vec a=%s\\), \\(\\vec b=%s\\). Then \\(\\vec a\\cdot\\vec b=\\)…' % (V2(a), V2(b)), vi='Cho \\(\\vec a=%s\\), \\(\\vec b=%s\\). Khi đó \\(\\vec a\\cdot\\vec b=\\)…' % (V2(a), V2(b)),
      opts=pick_opts(r, str(v), [str(a[0] * b[1] + a[1] * b[0]), str(a[0] * b[0] - a[1] * b[1]), str(-v), str(v + 2)], fill=lambda k: str(v + 3 * k)), ans=0,
      ee='\\(x_1x_2+y_1y_2=%d\\cdot%s+%s\\cdot%s=%d\\).' % (a[0], '(%d)' % b[0] if b[0] < 0 else b[0], '(%d)' % a[1] if a[1] < 0 else a[1], '(%d)' % b[1] if b[1] < 0 else b[1], v), ev='\\(x_1x_2+y_1y_2=%d\\).' % v)
def _angle_pairs():
    out = []
    for x1 in range(-4, 5):
        for y1 in range(-4, 5):
            for x2 in range(-4, 5):
                for y2 in range(-4, 5):
                    if (x1, y1) == (0, 0) or (x2, y2) == (0, 0): continue
                    d = x1 * x2 + y1 * y2; n2 = (x1 * x1 + y1 * y1) * (x2 * x2 + y2 * y2)
                    c2 = F(d * d, n2)
                    if c2 == F(1, 2): out.append(((x1, y1), (x2, y2), 45 if d > 0 else 135))
                    elif d == 0: out.append(((x1, y1), (x2, y2), 90))
    return out
ANG = _angle_pairs()
def d_angle(r, lv):
    a, b, th = r.choice(ANG); assert a[0] * b[1] != a[1] * b[0] or th == 90
    return dict(en='The angle between \\(\\vec a=%s\\) and \\(\\vec b=%s\\) is…' % (V2(a), V2(b)), vi='Góc giữa hai vectơ \\(\\vec a=%s\\) và \\(\\vec b=%s\\) bằng…' % (V2(a), V2(b)),
      opts=pick_opts(r, '%d^\\circ' % th, ['%d^\\circ' % x for x in (45, 135, 90, 60, 30, 120) if x != th]), ans=0,
      ee='\\(\\cos(\\vec a,\\vec b)=\\dfrac{\\vec a\\cdot\\vec b}{|\\vec a|\\,|\\vec b|}=\\dfrac{%d}{\\sqrt{%d}\\cdot\\sqrt{%d}}\\), so the angle is \\(%d^\\circ\\).' % (dot(a, b), dot(a, a), dot(b, b), th),
      ev='\\(\\cos(\\vec a,\\vec b)=\\dfrac{\\vec a\\cdot\\vec b}{|\\vec a|\\,|\\vec b|}=\\dfrac{%d}{\\sqrt{%d}\\cdot\\sqrt{%d}}\\) nên góc bằng \\(%d^\\circ\\).' % (dot(a, b), dot(a, a), dot(b, b), th))
def d_perp(r, lv):
    a = r.choice([(1, 2), (2, -1), (3, 1), (2, 3), (-1, 4), (4, -2)]); p = r.randint(-4, 4); assert a[1] != 0; t = -a[0] * p
    assert t % a[1] == 0; m = t // a[1]
    return dict(en='\\(\\vec a=%s\\) and \\(\\vec b=(%d;\\,m)\\). The vectors are perpendicular when \\(m=\\)…' % (V2(a), p), vi='Cho \\(\\vec a=%s\\), \\(\\vec b=(%d;\\,m)\\). Hai vectơ vuông góc khi \\(m=\\)…' % (V2(a), p),
      opts=pick_opts(r, str(m), [str(-m) if m else '1', fr(F(a[1] * p, a[0])) if a[0] else '2', str(m + 1), str(m - 2)], fill=lambda k: str(m + 3 * k)), ans=0,
      ee='\\(\\vec a\\cdot\\vec b=%d\\cdot%d+%d\\,m=0\\Rightarrow m=%d\\).' % (a[0], p, a[1], m), ev='\\(\\vec a\\cdot\\vec b=%d\\cdot%d+%d\\,m=0\\Rightarrow m=%d\\).' % (a[0], p, a[1], m))
def d_work(r, lv):
    Fv = r.choice([20, 40, 50, 60, 80, 100]); d = r.choice([5, 10, 12, 15, 20]); th = r.choice([0, 60, 90, 120]); W = Fv * d * COS[th]
    return dict(en='A force of \\(%d\\ \\text{N}\\) pulls a box \\(%d\\ \\text{m}\\). The angle between the force and the motion is \\(%d^\\circ\\). The work \\(A=\\vec F\\cdot\\vec d\\) is…' % (Fv, d, th),
      vi='Một lực \\(%d\\ \\text{N}\\) kéo thùng hàng đi \\(%d\\ \\text{m}\\); góc giữa lực và hướng chuyển động là \\(%d^\\circ\\). Công \\(A=\\vec F\\cdot\\vec d\\) bằng…' % (Fv, d, th),
      opts=pick_opts(r, fr(W) + '\\ \\text{J}', [str(Fv * d) + '\\ \\text{J}', fr(-W if W else F(Fv * d, 2)) + '\\ \\text{J}', str(Fv + d) + '\\ \\text{J}', fr(F(Fv * d, 4)) + '\\ \\text{J}'], fill=lambda k: fr(W + 10 * k) + '\\ \\text{J}'), ans=0,
      ee='\\(A=%d\\cdot%d\\cdot\\cos%d^\\circ=%s\\ \\text{J}\\).' % (Fv, d, th, fr(W)), ev='\\(A=%d\\cdot%d\\cdot\\cos%d^\\circ=%s\\ \\text{J}\\).' % (Fv, d, th, fr(W)))
def d_equi(r, lv):
    a = r.choice([2, 4, 6, 8, 10]); which = r.choice(['AB,AC', 'AB,BC'])
    v = F(a * a, 2) if which == 'AB,AC' else F(-a * a, 2); p, q = which.split(',')
    return dict(en='Triangle \\(ABC\\) is equilateral with side \\(%d\\). Then \\(%s\\cdot%s=\\)…' % (a, ov(*p), ov(*q)), vi='Tam giác \\(ABC\\) đều cạnh \\(%d\\). Khi đó \\(%s\\cdot%s=\\)…' % (a, ov(*p), ov(*q)),
      opts=pick_opts(r, fr(v), [fr(-v), str(a * a), fr(F(a * a, 4)), str(-a * a)]), ans=0,
      ee='The angle between \\(%s\\) and \\(%s\\) is \\(%d^\\circ\\), so the product is \\(%d\\cdot%d\\cdot%s=%s\\).' % (ov(*p), ov(*q), 60 if v > 0 else 120, a, a, '\\frac12' if v > 0 else '\\left(-\\frac12\\right)', fr(v)),
      ev='Góc giữa \\(%s\\) và \\(%s\\) là \\(%d^\\circ\\) nên tích bằng \\(%d\\cdot%d\\cdot%s=%s\\).' % (ov(*p), ov(*q), 60 if v > 0 else 120, a, a, '\\frac12' if v > 0 else '\\left(-\\frac12\\right)', fr(v)))
SUMLEN = [(3, 5, 60, 7), (5, 3, 60, 7), (7, 8, 60, 13), (6, 10, 60, 14), (3, 4, 90, 5), (8, 15, 90, 17), (5, 8, 120, 7), (3, 8, 120, 7), (5, 16, 120, 14)]
def d_sumlen(r, lv):
    a, b, th, c = r.choice(SUMLEN); assert a * a + b * b + 2 * a * b * COS[th] == c * c
    return dict(en='\\(|\\vec a|=%d\\), \\(|\\vec b|=%d\\), \\((\\vec a,\\vec b)=%d^\\circ\\). Then \\(|\\vec a+\\vec b|=\\)…' % (a, b, th), vi='Cho \\(|\\vec a|=%d\\), \\(|\\vec b|=%d\\), \\((\\vec a,\\vec b)=%d^\\circ\\). Khi đó \\(|\\vec a+\\vec b|=\\)…' % (a, b, th),
      opts=pick_opts(r, str(c), [str(a + b), str(c * c), str(abs(a - b)), str(c + 1)], fill=lambda k: str(c + 2 * k)), ans=0,
      ee='\\(|\\vec a+\\vec b|^2=|\\vec a|^2+|\\vec b|^2+2\\vec a\\cdot\\vec b=%d\\), so \\(|\\vec a+\\vec b|=%d\\).' % (c * c, c), ev='\\(|\\vec a+\\vec b|^2=|\\vec a|^2+|\\vec b|^2+2\\vec a\\cdot\\vec b=%d\\) nên \\(|\\vec a+\\vec b|=%d\\).' % (c * c, c))
def d_tri(r, lv):
    A = _pt(r, -3, 3); u = r.choice([(2, 1), (3, 0), (1, 3), (2, -2), (4, 1)]); k = r.choice([1, 2, -1]); w = (-u[1] * k, u[0] * k)
    B, C = add(A, u), add(A, w); kind = r.choice(['right', 'other'])
    if kind == 'other': C = (C[0] + r.choice([1, -1, 2]), C[1])
    d = dot(add(B, A, 1, -1), add(C, A, 1, -1)); ang = 'right' if d == 0 else ('acute' if d > 0 else 'obtuse')
    ma = {'right': ('\\(\\widehat{BAC}=90^\\circ\\)', 'right'), 'acute': ('\\(\\widehat{BAC}\\lt90^\\circ\\)', 'acute'), 'obtuse': ('\\(\\widehat{BAC}\\gt90^\\circ\\)', 'obtuse')}
    T_ = {'right': TT('\\(\\widehat{BAC}\\) is a right angle', '\\(\\widehat{BAC}\\) là góc vuông'), 'acute': TT('\\(\\widehat{BAC}\\) is acute', '\\(\\widehat{BAC}\\) là góc nhọn'), 'obtuse': TT('\\(\\widehat{BAC}\\) is obtuse', '\\(\\widehat{BAC}\\) là góc tù'), 'eq': TT('Triangle \\(ABC\\) is equilateral', 'Tam giác \\(ABC\\) đều')}
    return dict(en='\\(A%s\\), \\(B%s\\), \\(C%s\\). Which statement is true?' % (P2(A), P2(B), P2(C)), vi='Cho \\(A%s\\), \\(B%s\\), \\(C%s\\). Khẳng định nào đúng?' % (P2(A), P2(B), P2(C)),
      opts=[T_[ang]] + [T_[x] for x in ('right', 'acute', 'obtuse', 'eq') if x != ang][:3], ans=0,
      ee='\\(%s\\cdot%s=%d\\): %s.' % (ov('A', 'B'), ov('A', 'C'), d, {'right': 'zero, so a right angle', 'acute': 'positive, so acute', 'obtuse': 'negative, so obtuse'}[ang]),
      ev='\\(%s\\cdot%s=%d\\): %s.' % (ov('A', 'B'), ov('A', 'C'), d, {'right': 'bằng 0 nên góc vuông', 'acute': 'dương nên góc nhọn', 'obtuse': 'âm nên góc tù'}[ang]))
M11S10 = [d_def, d_coord, d_angle, d_perp, d_work, d_equi, d_sumlen, d_tri]

# ================= Bài 12. Số gần đúng và sai số =================
def D(x):
    """Số trong công thức: dấu phẩy thập phân (chuẩn Việt Nam); số nguyên từ 10 000 tách nhóm ba chữ số bằng khoảng trắng hẹp."""
    x = F(x)
    if x.denominator == 1 and abs(x) >= 10000:
        t = '{:,}'.format(abs(x.numerator)).replace(',', '\\,'); return ('-' if x < 0 else '') + t
    return num(x)
def DE(x): return num(F(x), comma=False)
UNIT = [(F(1, 1000), 'thousandths', 'phần nghìn'), (F(1, 100), 'hundredths', 'phần trăm'), (F(1, 10), 'tenths', 'phần mười'), (F(1), 'units', 'đơn vị'), (F(10), 'tens', 'chục'), (F(100), 'hundreds', 'trăm'), (F(1000), 'thousands', 'nghìn')]
def rnd(x, u):
    """Làm tròn x đến bội của u (nửa lên)."""
    q = F(x) / u; n = math.floor(q + F(1, 2)); return n * u
def target_unit(d):
    """Quy tắc SGK: làm tròn đến hàng thấp nhất mà d nhỏ hơn 1 đơn vị của hàng đó."""
    for u, en, vi in UNIT:
        if d < u: return u, en, vi
    raise AssertionError
def e_abs(r, lv):
    t = F(r.randint(10000, 99999), 1000); u = r.choice([F(1, 10), F(1, 100)]); a = rnd(t, u); dlt = abs(t - a); assert dlt != 0
    return dict(en='The exact length is \\(%s\\ \\text{m}\\) and it is written as \\(%s\\ \\text{m}\\). The absolute error is…' % (D(t), D(a)), vi='Độ dài đúng là \\(%s\\ \\text{m}\\), được ghi gọn là \\(%s\\ \\text{m}\\). Sai số tuyệt đối là…' % (D(t), D(a)),
      opts=pick_opts(r, D(dlt), [D(dlt * 10), D(u), D(dlt / 10), D(u / 2)], fill=lambda k: D(dlt + k * F(1, 1000))), ans=0,
      ee='\\(\\Delta_a=|\\bar a-a|=|%s-%s|=%s\\).' % (D(t), D(a), D(dlt)), ev='\\(\\Delta_a=|\\bar a-a|=|%s-%s|=%s\\).' % (D(t), D(a), D(dlt)))
def e_interval(r, lv):
    a = F(r.randint(100, 999), 10); d = r.choice([F(1, 10), F(2, 10), F(5, 100), F(3, 10)])
    return dict(en='A rope is measured as \\(%s\\pm%s\\) (cm). The true length \\(\\bar a\\) lies in…' % (D(a), D(d)), vi='Một sợi dây đo được \\(%s\\pm%s\\) (cm). Độ dài đúng \\(\\bar a\\) nằm trong đoạn…' % (D(a), D(d)),
      opts=pick_opts(r, '[%s;\\,%s]' % (D(a - d), D(a + d)), ['[%s;\\,%s]' % (D(a), D(a + d)), '[%s;\\,%s]' % (D(a - 2 * d), D(a + 2 * d)), '[%s;\\,%s]' % (D(a - d), D(a)), '[%s;\\,%s]' % (D(a - d / 2), D(a + d / 2))]), ans=0,
      ee='\\(a-d\\le\\bar a\\le a+d\\).', ev='\\(a-d\\le\\bar a\\le a+d\\).')
def e_rel(r, lv):
    a, d = r.choice([(F(250), F(1, 2)), (F(80), F(2, 10)), (F(125), F(1, 4)), (F(40), F(1, 10)), (F(500), F(2)), (F(320), F(8, 10)), (F(160), F(4, 10))]); p = d / a * 100
    return dict(en='A length is measured as \\(%s\\pm%s\\) (cm). An upper bound for the relative error is…' % (D(a), D(d)), vi='Một độ dài đo được \\(%s\\pm%s\\) (cm). Sai số tương đối không vượt quá…' % (D(a), D(d)),
      opts=pick_opts(r, D(p) + '\\%', [D(p * 10) + '\\%', D(p / 10) + '\\%', D(d) + '\\%', D(p * 2) + '\\%'], fill=lambda k: D(p + k) + '\\%'), ans=0,
      ee='\\(\\delta_a\\le\\dfrac{d}{|a|}=\\dfrac{%s}{%s}=%s\\%%\\).' % (D(d), D(a), D(p)), ev='\\(\\delta_a\\le\\dfrac{d}{|a|}=\\dfrac{%s}{%s}=%s\\%%\\).' % (D(d), D(a), D(p)))
def e_compare(r, lv):
    a1, d1, a2, d2 = r.choice([(F(152), F(1, 2), F(4000), F(5)), (F(25), F(1, 10), F(1200), F(2)), (F(380), F(1), F(12), F(1, 10)), (F(56), F(2, 10), F(2500), F(10))])
    p1, p2 = d1 / a1, d2 / a2; assert p1 != p2
    better = 'A' if p1 < p2 else 'B'
    o = {x: TT('Measurement %s, because its relative error is smaller' % x, 'Phép đo %s, vì sai số tương đối nhỏ hơn' % x) for x in 'AB'}
    o.update({x + 'd': TT('Measurement %s, because its accuracy \\(d\\) is smaller' % x, 'Phép đo %s, vì độ chính xác \\(d\\) nhỏ hơn' % x) for x in 'AB'}); o['eq'] = TT('They are equally precise', 'Hai phép đo chính xác như nhau')
    small_d = 'Ad' if d1 < d2 else 'Bd'
    wrong = [x for x in ('A', 'B') if x != better] + ([small_d] if small_d[0] != better else [x for x in ('Ad', 'Bd') if x != small_d]) + ['eq']
    return dict(en='Measurement A: a desk is \\(%s\\pm%s\\) cm long. Measurement B: a road is \\(%s\\pm%s\\) cm long. Which measurement is more precise?' % (D(a1), D(d1), D(a2), D(d2)),
      vi='Phép đo A: chiếc bàn dài \\(%s\\pm%s\\) cm. Phép đo B: con đường dài \\(%s\\pm%s\\) cm. Phép đo nào chính xác hơn?' % (D(a1), D(d1), D(a2), D(d2)),
      opts=[o[better]] + [o[x] for x in wrong][:3], ans=0,
      ee='Compare \\(\\dfrac{%s}{%s}\\approx%s\\%%\\) and \\(\\dfrac{%s}{%s}\\approx%s\\%%\\).' % (D(d1), D(a1), D(rnd(p1 * 100, F(1, 1000))), D(d2), D(a2), D(rnd(p2 * 100, F(1, 1000)))),
      ev='So sánh \\(\\dfrac{%s}{%s}\\approx%s\\%%\\) và \\(\\dfrac{%s}{%s}\\approx%s\\%%\\).' % (D(d1), D(a1), D(rnd(p1 * 100, F(1, 1000))), D(d2), D(a2), D(rnd(p2 * 100, F(1, 1000)))))
def e_round_d(r, lv):
    case = r.choice(['dec', 'big'])
    if case == 'dec':
        a = F(r.randint(100000, 999999), 10000); d = r.choice([F(2, 1000), F(4, 1000), F(3, 100), F(6, 100), F(2, 10)])
    else:
        a = F(r.randint(1000000, 9999999)); d = r.choice([F(50), F(300), F(200), F(4000), F(30)])
    u, en, vi = target_unit(d); res = rnd(a, u)
    wrong = [rnd(a, x[0]) for x in UNIT if x[0] != u and x[0] < a]
    return dict(en='The approximate number \\(a=%s\\) has accuracy \\(d=%s\\). Round \\(a\\) correctly.' % (D(a), D(d)), vi='Số gần đúng \\(a=%s\\) có độ chính xác \\(d=%s\\). Hãy quy tròn \\(a\\).' % (D(a), D(d)),
      opts=pick_opts(r, D(res), [D(w) for w in sorted(wrong, key=lambda w: abs(w - res)) if w != res]), ans=0,
      ee='\\(d=%s\\lt1\\) unit of the %s, so round to the %s: \\(%s\\).' % (D(d), en, en, D(res)), ev='\\(d=%s\\) nhỏ hơn 1 đơn vị hàng %s nên quy tròn đến hàng %s: \\(%s\\).' % (D(d), vi, vi, D(res)))
def e_round_err(r, lv):
    u, en, vi = r.choice(UNIT[:6]); x = F(r.randint(10 ** 5, 10 ** 6 - 1), 1000) if u < 1 else F(r.randint(10 ** 4, 10 ** 6))
    return dict(en='The number \\(%s\\) is rounded to the %s. The absolute error of the rounded number is at most…' % (D(x), en), vi='Quy tròn số \\(%s\\) đến hàng %s. Sai số tuyệt đối của số quy tròn không vượt quá…' % (D(x), vi),
      opts=pick_opts(r, D(u / 2), [D(u), D(u / 10), D(u * 5), D(u / 5)]), ans=0,
      ee='Half a unit of the rounding place: \\(\\dfrac{%s}{2}=%s\\).' % (D(u), D(u / 2)), ev='Nửa đơn vị của hàng quy tròn: \\(\\dfrac{%s}{2}=%s\\).' % (D(u), D(u / 2)))
def e_sqrt(r, lv):
    n = r.choice([2, 3, 5, 7, 10, 11]); x = math.sqrt(n); lo = F(math.floor(x * 100), 100); hi = lo + F(1, 100); a = r.choice([lo, hi])
    d = F(1, 100)
    return dict(en='Given \\(%s\\lt\\sqrt{%d}\\lt%s\\). If we take \\(\\sqrt{%d}\\approx%s\\), the absolute error is less than…' % (D(lo), n, D(hi), n, D(a)), vi='Biết \\(%s\\lt\\sqrt{%d}\\lt%s\\). Nếu lấy \\(\\sqrt{%d}\\approx%s\\) thì sai số tuyệt đối nhỏ hơn…' % (D(lo), n, D(hi), n, D(a)),
      opts=pick_opts(r, D(d), [D(d / 2), D(d / 10), D(F(1, 10)), D(lo)]), ans=0,
      ee='\\(\\sqrt{%d}\\) and \\(%s\\) both lie in \\((%s;\\,%s)\\), whose length is \\(%s\\).' % (n, D(a), D(lo), D(hi), D(d)), ev='\\(\\sqrt{%d}\\) và \\(%s\\) cùng thuộc \\((%s;\\,%s)\\) có độ dài \\(%s\\).' % (n, D(a), D(lo), D(hi), D(d)))
def e_area(r, lv):
    a = r.choice([10, 20, 25, 30, 40]); d = r.choice([F(1, 10), F(2, 10), F(1, 2)]); S = a * a; dS = (a + d) ** 2 - S
    return dict(en='A square tile has side \\(%d\\pm%s\\) (cm). The area is \\(S=%d\\ \\text{cm}^2\\) with absolute error at most…' % (a, D(d), S), vi='Một viên gạch hình vuông có cạnh \\(%d\\pm%s\\) (cm). Diện tích \\(S=%d\\ \\text{cm}^2\\) với sai số tuyệt đối không vượt quá…' % (a, D(d), S),
      opts=pick_opts(r, D(dS), [D(d * d), D(2 * a * d), D(4 * d), D(d)]), ans=0,
      ee='The largest area is \\((%d+%s)^2=%s\\), so the error is at most \\(%s\\ \\text{cm}^2\\).' % (a, D(d), D((a + d) ** 2), D(dS)), ev='Diện tích lớn nhất là \\((%d+%s)^2=%s\\) nên sai số không vượt quá \\(%s\\ \\text{cm}^2\\).' % (a, D(d), D((a + d) ** 2), D(dS)))
M12S10 = [e_abs, e_interval, e_rel, e_compare, e_round_d, e_round_err, e_sqrt, e_area]
