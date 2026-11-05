# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 10 – Chương IV (vectơ). Tọa độ nguyên/hữu tỉ trong cơ sở của hình, nên đáp án chính xác."""
import math
from fractions import Fraction as F
from mb_selfpractice import *

def ov(p, q): return '\\overrightarrow{%s%s}' % (p, q)
def sub(P, a, b): return tuple(y - x for x, y in zip(P[a], P[b]))
PGM = {'A': (0, 0), 'B': (1, 0), 'C': (1, 1), 'D': (0, 1), 'O': (F(1, 2), F(1, 2))}          # hình bình hành, cơ sở (AB, AD)
HEX = {'A': (1, 0), 'B': (0, 1), 'C': (-1, 1), 'D': (-1, 0), 'E': (0, -1), 'F': (1, -1), 'O': (0, 0)}   # lục giác đều tâm O, cơ sở (OA, OB)
PY = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (6, 8, 10), (9, 12, 15), (7, 24, 25), (20, 21, 29)]

def _eqvec(r, P, pairs):
    p = r.choice(pairs); v = sub(P, *p)
    eq = [x for x in pairs if x != p and sub(P, *x) == v]
    return p, v, eq
def v7_count(r, lv):
    n = r.choice([3, 4, 5, 6, 7, 8]); c = n * (n - 1)
    return dict(en='There are %d points, no three on a line. How many non-zero vectors have both endpoints among them?' % n, vi='Cho %d điểm phân biệt, không có ba điểm nào thẳng hàng. Có bao nhiêu vectơ khác vectơ-không với điểm đầu, điểm cuối thuộc tập điểm đó?' % n,
      opts=pick_opts(r, str(c), [str(c // 2), str(n * n), str(c + n), str(c - 1)], fill=lambda k: str(c + 2 * k)), ans=0, ee='Choose the start (%d ways) and the end (%d ways): %d.' % (n, n - 1, c), ev='Chọn điểm đầu (%d cách), điểm cuối (%d cách): %d vectơ.' % (n, n - 1, c))
def v7_eq(r, lv):
    P = r.choice([PGM, HEX]); names = [k for k in P if k != 'O' or P is HEX]
    pairs = [(a, b) for a in P for b in P if a != b]
    while True:
        p, v, eq = _eqvec(r, P, pairs)
        if eq: break
    c = r.choice(eq); wr = [x for x in pairs if sub(P, *x) != v and (sub(P, *x) == tuple(-t for t in v) or x[0] == p[0] or x[1] == p[1] or x[0] == c[0])]
    r.shuffle(wr); fig = 'parallelogram \\(ABCD\\) with centre \\(O\\)' if P is PGM else 'regular hexagon \\(ABCDEF\\) with centre \\(O\\)'; figv = 'hình bình hành \\(ABCD\\) tâm \\(O\\)' if P is PGM else 'lục giác đều \\(ABCDEF\\) tâm \\(O\\)'
    f = lambda x: ov(*x)
    return dict(en='In the %s, which vector equals \\(%s\\)?' % (fig, ov(*p)), vi='Cho %s. Vectơ nào bằng \\(%s\\)?' % (figv, ov(*p)), opts=pick_opts(r, f(c), [f(x) for x in wr]), ans=0,
      ee='Equal vectors have the same direction and the same length: \\(%s=%s\\).' % (ov(*p), ov(*c)), ev='Hai vectơ bằng nhau khi cùng hướng và cùng độ dài: \\(%s=%s\\).' % (ov(*p), ov(*c)))
def v7_len(r, lv):
    kind = r.choice(['sq', 'rect', 'hexAD', 'hexAC']); a = r.randint(2, 9)
    if kind == 'sq':
        en = 'ABCD is a square with side %d. Then \\(|%s|^2=\\)…' % (a, ov('A', 'C')); vi = 'ABCD là hình vuông cạnh %d. Khi đó \\(|%s|^2=\\)…' % (a, ov('A', 'C')); c = 2 * a * a; wr = [a * a, 4 * a * a, 2 * a, 3 * a * a]; e = 'The diagonal is \\(a\\sqrt2\\), so its square is \\(2a^2\\).'; ev = 'Đường chéo dài \\(a\\sqrt2\\) nên bình phương bằng \\(2a^2\\).'
    elif kind == 'rect':
        p, q, h = r.choice(PY); en = 'ABCD is a rectangle with AB = %d and AD = %d. Then \\(|%s|=\\)…' % (p, q, ov('A', 'C')); vi = 'ABCD là hình chữ nhật có AB = %d, AD = %d. Khi đó \\(|%s|=\\)…' % (p, q, ov('A', 'C')); c = h; wr = [p + q, q, h + 1, h - 1]; e = 'Pythagoras: \\(\\sqrt{%d^2+%d^2}=%d\\).' % (p, q, h); ev = 'Định lí Pi-ta-go: \\(\\sqrt{%d^2+%d^2}=%d\\).' % (p, q, h)
    elif kind == 'hexAD':
        en = 'ABCDEF is a regular hexagon with side %d. Then \\(|%s|=\\)…' % (a, ov('A', 'D')); vi = 'ABCDEF là lục giác đều cạnh %d. Khi đó \\(|%s|=\\)…' % (a, ov('A', 'D')); c = 2 * a; wr = [a, 3 * a, 4 * a, a * a]; e = 'AD passes through the centre: AD = 2·side.'; ev = 'AD đi qua tâm: AD bằng hai lần cạnh.'
    else:
        en = 'ABCDEF is a regular hexagon with side %d. Then \\(|%s|^2=\\)…' % (a, ov('A', 'C')); vi = 'ABCDEF là lục giác đều cạnh %d. Khi đó \\(|%s|^2=\\)…' % (a, ov('A', 'C')); c = 3 * a * a; wr = [a * a, 2 * a * a, 4 * a * a, 6 * a]; e = '\\(AC=a\\sqrt3\\) (law of cosines with \\(120^\\circ\\)).'; ev = '\\(AC=a\\sqrt3\\) (định lí cô-sin với góc \\(120^\\circ\\)).'
    return dict(en=en, vi=vi, opts=pick_opts(r, str(c), [str(x) for x in wr], fill=lambda k: str(c + 3 * k)), ans=0, ee=e, ev=ev)
def v7_dir(r, lv):
    P = HEX; pairs = [(a, b) for a in P for b in P if a != b]
    while True:
        p, q = r.sample(pairs, 2); u, v = sub(P, *p), sub(P, *q)
        cr = u[0] * v[1] - u[1] * v[0]
        if cr == 0: break
    same = (u[0] * v[0] + u[1] * v[1]) > 0 and any(u[i] * v[i] > 0 for i in range(2)) if False else None
    k = next((v[i] / u[i]) for i in range(2) if u[i] != 0); ans = 0 if k > 0 else 1
    return dict(en='In the regular hexagon \\(ABCDEF\\) with centre \\(O\\), the vectors \\(%s\\) and \\(%s\\) are…' % (ov(*p), ov(*q)), vi='Trong lục giác đều \\(ABCDEF\\) tâm \\(O\\), hai vectơ \\(%s\\) và \\(%s\\)…' % (ov(*p), ov(*q)),
      opts=['\\text{in the same direction}', '\\text{in opposite directions}', '\\text{not collinear}', '\\text{equal}'] if False else ['cùng hướng', 'ngược hướng', 'không cùng phương', 'bằng nhau'], ans=ans, ee='They are collinear; compare the directions along the line.', ev='Hai vectơ cùng phương; xét hướng dọc theo đường thẳng.') if k != 1 else None
M7S = [v7_count, v7_eq, v7_len, v7_eq, v7_count, v7_len, v7_eq, v7_len]

def v8_chasles(r, lv):
    a, b, c, d = r.sample('MNPQRSTUVW', 4); kind = r.choice([0, 1, 2])
    if kind == 0: ex = '%s+%s+%s' % (ov(a, b), ov(b, c), ov(c, d)); ans = ov(a, d); wr = [ov(a, c), ov(d, a), ov(b, d)]
    elif kind == 1: ex = '%s+%s-%s' % (ov(a, b), ov(b, c), ov(d, c)); ans = ov(a, d); wr = [ov(a, c), ov(d, a), ov(c, d)]
    else: ex = '%s-%s' % (ov(a, c), ov(a, b)); ans = ov(b, c); wr = [ov(c, b), ov(a, b), ov(b, a)]
    f = lambda x: x
    return dict(en='Simplify \\(%s\\).' % ex, vi='Rút gọn \\(%s\\).' % ex, opts=pick_opts(r, f(ans), [f(x) for x in wr]), ans=0, ee='Use the triangle rule and \\(\\overrightarrow{XY}-\\overrightarrow{XZ}=\\overrightarrow{ZY}\\).', ev='Dùng quy tắc ba điểm và \\(\\overrightarrow{XY}-\\overrightarrow{XZ}=\\overrightarrow{ZY}\\).')
def v8_par(r, lv):
    P = PGM; pairs = [(a, b) for a in 'ABCD' for b in 'ABCD' if a != b]
    ops = [((p1, 1), (q1, s)) for p1 in pairs for q1 in pairs for s in (1, -1) if p1 != q1 and p1[0] == q1[0] and any(sub(P, *x) == tuple(a + s * b for a, b in zip(sub(P, *p1), sub(P, *q1))) for x in pairs)]
    (p, s1), (q, s2) = r.choice(ops); v = tuple(s1 * x + s2 * y for x, y in zip(sub(P, *p), sub(P, *q)))
    sg = lambda s: '+' if s > 0 else '-'; ex = ov(*p) + ' %s ' % sg(s2) + ov(*q)
    cand = [x for x in pairs if sub(P, *x) == v]
    if not cand: return None
    c = cand[0]; wr = [x for x in pairs if sub(P, *x) != v]; r.shuffle(wr); f = lambda x: ov(*x)
    return dict(en='ABCD is a parallelogram. \\(%s=\\)…' % ex, vi='ABCD là hình bình hành. \\(%s=\\)…' % ex, opts=pick_opts(r, f(c), [f(x) for x in wr[:6]]), ans=0, ee='Use the parallelogram rule \\(\\overrightarrow{AB}+\\overrightarrow{AD}=\\overrightarrow{AC}\\) and equal opposite sides.', ev='Dùng quy tắc hình bình hành \\(\\overrightarrow{AB}+\\overrightarrow{AD}=\\overrightarrow{AC}\\) và các cạnh đối bằng nhau.')
def v8_rect(r, lv):
    p, q, h = r.choice(PY); op = r.choice(['+', '-']); ex = ov('A', 'B') + ' ' + op + ' ' + ov('A', 'D')
    return dict(en='ABCD is a rectangle with AB = %d and AD = %d. Find \\(|%s|\\).' % (p, q, ex), vi='ABCD là hình chữ nhật có AB = %d, AD = %d. Tính \\(|%s|\\).' % (p, q, ex),
      opts=pick_opts(r, str(h), [str(p + q), str(abs(p - q)), str(h + 1), str(q)], fill=lambda k: str(h + 2 * k)), ans=0, ee='\\(\\overrightarrow{AB}%s\\overrightarrow{AD}\\) has the length of a diagonal: \\(\\sqrt{%d^2+%d^2}=%d\\).' % (op, p, q, h), ev='\\(\\overrightarrow{AB}%s\\overrightarrow{AD}\\) có độ dài bằng đường chéo: \\(\\sqrt{%d^2+%d^2}=%d\\).' % (op, p, q, h))
def v8_hex(r, lv):
    P = HEX; names = 'ABCDEF'
    while True:
        a, b = r.sample(names, 2); v = tuple(x + y for x, y in zip(sub(P, 'O', a), sub(P, 'O', b)))
        tgt = [x for x in names if sub(P, 'O', x) == v]
        if tgt and abs(names.index(a) - names.index(b)) in (2, 4): break
    t = tgt[0]; f = lambda x: x; wr = [ov('O', x) for x in names if x != t] + [ov(t, 'O')]; r.shuffle(wr)
    return dict(en='\\(ABCDEF\\) is a regular hexagon with centre \\(O\\). \\(%s+%s=\\)…' % (ov('O', a), ov('O', b)), vi='\\(ABCDEF\\) là lục giác đều tâm \\(O\\). \\(%s+%s=\\)…' % (ov('O', a), ov('O', b)), opts=pick_opts(r, f(ov('O', t)), [f(x) for x in wr]), ans=0, ee='The sum is the diagonal of the rhombus built on \\(O%s\\) and \\(O%s\\).' % (a, b), ev='Tổng là vectơ đường chéo của hình thoi dựng trên hai vectơ \\(O%s\\), \\(O%s\\).' % (a, b))
def v8_force(r, lv):
    p, q, h = r.choice(PY); k = r.choice([1, 2, 5, 10]) if lv < 3 else r.choice([10, 20])
    return dict(en='Two forces of %d N and %d N act at one point at a right angle. The resultant force is…' % (p * k, q * k), vi='Hai lực %d N và %d N cùng tác dụng lên một vật tại một điểm, vuông góc với nhau. Hợp lực có độ lớn…' % (p * k, q * k),
      opts=pick_opts(r, '%d\\ \\text{N}' % (h * k), ['%d\\ \\text{N}' % ((p + q) * k), '%d\\ \\text{N}' % (abs(q - p) * k), '%d\\ \\text{N}' % (q * k), '%d\\ \\text{N}' % (h * k + 5)], fill=lambda j: '%d\\ \\text{N}' % (h * k + 7 * j)), ans=0, ee='The resultant is the diagonal of the rectangle: \\(\\sqrt{%d^2+%d^2}=%d\\).' % (p * k, q * k, h * k), ev='Hợp lực là đường chéo của hình chữ nhật: \\(\\sqrt{%d^2+%d^2}=%d\\).' % (p * k, q * k, h * k))
M8S = [v8_chasles, v8_par, v8_rect, v8_hex, v8_force, v8_chasles, v8_par, v8_hex]

def v9_mid(r, lv):
    A, B, C, I = r.sample('ABCDEFMNPQ', 4); k = r.choice([1, 2, 3])
    return dict(en='\\(%s\\) is the midpoint of \\(%s%s\\). Then \\(%s+%s=k\\,%s\\) with \\(k=\\)…' % (I, B, C, ov(A, B), ov(A, C), ov(A, I)), vi='\\(%s\\) là trung điểm của \\(%s%s\\). Khi đó \\(%s+%s=k\\,%s\\) với \\(k=\\)…' % (I, B, C, ov(A, B), ov(A, C), ov(A, I)),
      opts=['2', '1', '\\dfrac12', '3'], ans=0, ee='\\(\\overrightarrow{AB}+\\overrightarrow{AC}=2\\overrightarrow{AI}\\) for the midpoint \\(I\\) of \\(BC\\).', ev='\\(\\overrightarrow{AB}+\\overrightarrow{AC}=2\\overrightarrow{AI}\\) với \\(I\\) là trung điểm \\(BC\\).')
def v9_cent(r, lv):
    num, den = r.choice([(1, 3), (2, 3), (1, 2), (1, 6), (1, 4), (3, 4), (2, 5)]); kind = r.choice(['G', 'M'])
    if kind == 'G':
        x = F(1, 3); en = 'G is the centroid of triangle ABC. \\(%s=x\\,%s+x\\,%s\\) with \\(x=\\)…' % (ov('A', 'G'), ov('A', 'B'), ov('A', 'C')); vi = 'G là trọng tâm tam giác ABC. \\(%s=x\\,%s+x\\,%s\\) với \\(x=\\)…' % (ov('A', 'G'), ov('A', 'B'), ov('A', 'C'))
        e = '\\(\\overrightarrow{AG}=\\dfrac23\\overrightarrow{AI}\\) and \\(\\overrightarrow{AI}=\\dfrac12(\\overrightarrow{AB}+\\overrightarrow{AC})\\).'; v = '\\(\\overrightarrow{AG}=\\dfrac23\\overrightarrow{AI}\\) và \\(\\overrightarrow{AI}=\\dfrac12(\\overrightarrow{AB}+\\overrightarrow{AC})\\).'
    else:
        x = F(num, den); en = 'M is on segment BC with \\(%s=%s\\,%s\\). Then \\(%s=y\\,%s+%s\\,%s\\) with \\(y=\\)…' % (ov('B', 'M'), fr(x), ov('B', 'C'), ov('A', 'M'), ov('A', 'B'), fr(x), ov('A', 'C')) if False else ('M is on BC with \\(%s=%s\\,%s\\). Then the coefficient of \\(%s\\) in \\(%s=y\\,%s+z\\,%s\\) is \\(z=\\)…' % (ov('B', 'M'), fr(x), ov('B', 'C'), ov('A', 'C'), ov('A', 'M'), ov('A', 'B'), ov('A', 'C')))
        vi = 'M thuộc BC sao cho \\(%s=%s\\,%s\\). Khi đó trong \\(%s=y\\,%s+z\\,%s\\), hệ số \\(z=\\)…' % (ov('B', 'M'), fr(x), ov('B', 'C'), ov('A', 'M'), ov('A', 'B'), ov('A', 'C'))
        e = '\\(\\overrightarrow{AM}=\\overrightarrow{AB}+x\\overrightarrow{BC}=(1-x)\\overrightarrow{AB}+x\\overrightarrow{AC}\\).'; v = '\\(\\overrightarrow{AM}=\\overrightarrow{AB}+x\\overrightarrow{BC}=(1-x)\\overrightarrow{AB}+x\\overrightarrow{AC}\\).'
    f = lambda t: fr(t)
    return dict(en=en, vi=vi, opts=pick_opts(r, f(x), [f(1 - x), f(2 * x), f(x / 2), f(x + F(1, 2))], fill=lambda k: f(x + F(k, 7))), ans=0, ee=e, ev=v)
def v9_col(r, lv):
    k = r.choice([2, 3, -2, -3, 4, -1, 5]); A, B, C = r.sample('ABCDMNPQ', 3)
    return dict(en='Points %s, %s, %s satisfy \\(%s=%d\\,%s\\). Then the points are collinear and \\(%s=k\\,%s\\) with \\(k=\\)…' % (A, B, C, ov(A, B), k, ov(A, C), ov(A, C), ov(A, B)), vi='Ba điểm %s, %s, %s thỏa \\(%s=%d\\,%s\\). Khi đó ba điểm thẳng hàng và \\(%s=k\\,%s\\) với \\(k=\\)…' % (A, B, C, ov(A, B), k, ov(A, C), ov(A, C), ov(A, B)),
      opts=pick_opts(r, fr(F(1, k)), [str(k), str(-k), fr(F(-1, k)), '1'], fill=lambda j: str(k + 10 * j)), ans=0, ee='From \\(\\overrightarrow{AB}=%d\\overrightarrow{AC}\\) we get \\(\\overrightarrow{AC}=\\dfrac1{%d}\\overrightarrow{AB}\\).' % (k, k), ev='Từ \\(\\overrightarrow{AB}=%d\\overrightarrow{AC}\\) suy ra \\(\\overrightarrow{AC}=\\dfrac1{%d}\\overrightarrow{AB}\\).' % (k, k))
def v9_len(r, lv):
    a = r.randint(2, 12); k = r.choice([2, 3, -2, -3, 4, -5, F(1, 2), F(-3, 2)]); v = abs(k) * a
    return dict(en='\\(|\\vec a|=%d\\). Then \\(|%s\\vec a|=\\)…' % (a, fr(k)), vi='\\(|\\vec a|=%d\\). Khi đó \\(|%s\\vec a|=\\)…' % (a, fr(k)),
      opts=pick_opts(r, fr(v), [fr(k * a), fr(v + a), fr(a), fr(abs(k))], fill=lambda j: fr(v + 3 * j)), ans=0, ee='\\(|k\\vec a|=|k|\\,|\\vec a|\\), a length is never negative.', ev='\\(|k\\vec a|=|k|\\,|\\vec a|\\), độ dài không âm.')
def v9_ratio(r, lv):
    m, n = r.choice([(2, 5), (1, 3), (3, 4), (2, 7), (1, 4), (3, 8)]); A, B, M = r.sample('ABCDMNPQ', 3) if False else ('A', 'B', 'M')
    x = F(n - m, m)
    return dict(en='M is on segment AB with \\(AM=\\dfrac{%d}{%d}AB\\). Then \\(%s=k\\,%s\\) with \\(k=\\)…' % (m, n, ov('M', 'B'), ov('A', 'M')), vi='M thuộc đoạn AB sao cho \\(AM=\\dfrac{%d}{%d}AB\\). Khi đó \\(%s=k\\,%s\\) với \\(k=\\)…' % (m, n, ov('M', 'B'), ov('A', 'M')),
      opts=pick_opts(r, fr(x), [fr(F(m, n)), fr(F(n - m, n)), fr(-x), fr(F(n, m))], fill=lambda j: fr(x + j)), ans=0, ee='\\(MB=AB-AM=\\dfrac{%d}{%d}AB\\) and the vectors have the same direction.' % (n - m, n), ev='\\(MB=AB-AM=\\dfrac{%d}{%d}AB\\) và hai vectơ cùng hướng.' % (n - m, n))
M9S = [v9_mid, v9_cent, v9_col, v9_len, v9_ratio, v9_cent, v9_col, v9_len]
