# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 12 (mỗi bài 15 dạng → 22 câu/mức cùng 7 câu soạn sẵn):
Bài 17 (phương trình mặt cầu), Bài 18 (xác suất có điều kiện), Bài 19 (công thức xác suất toàn phần, công thức Bayes).
Mọi đáp án tính chính xác bằng số nguyên / Fraction; xác suất hiển thị dạng thập phân hữu hạn hoặc phân số tối giản."""
import math, itertools
from fractions import Fraction as F
from mb_selfpractice import pick_opts, fr
from mb_lib import TI
from freqtable import num
from sp_g12d import eq, V3, dot, sub

def TT(en, vi): return '§' + TI(en, vi)
def P(x): return num(F(x))
def PE(x): return num(F(x), comma=False)
def popts(r, c, cands):
    """Phương án xác suất: c đúng; cands các giá trị sai (lọc trùng, ngoài [0;1])."""
    c = F(c); seen, out = {c}, []
    for w in cands:
        w = F(w)
        if 0 <= w <= 1 and w not in seen: seen.add(w); out.append(P(w))
    if len(out) < 3: raise AssertionError
    return pick_opts(r, P(c), out)
def sq(v, c):
    """(x-a)^2 cho mặt cầu."""
    return '%s^2' % c if v == 0 else '(%s%+d)^2' % (c, -v)
def sph(I, R2): return '%s+%s+%s=%d' % (sq(I[0], 'x'), sq(I[1], 'y'), sq(I[2], 'z'), R2)
def gen(I, d):
    s = 'x^2+y^2+z^2'
    for v, c in zip(I, 'xyz'):
        if v: s += '%+d%s' % (-2 * v, c)
    if d: s += '%+d' % d
    return s + '=0'
def _I(r): return (r.randint(-3, 4), r.randint(-3, 4), r.randint(-3, 4))
N3 = [(1, 2, 2), (2, 1, 2), (2, 2, 1), (1, -2, 2), (2, -1, -2), (2, 2, -1), (2, 3, 6), (3, 6, 2), (6, 2, 3)]     # |n| là số nguyên
def _n(r):
    n = r.choice(N3); s = r.choice([1, -1]); n = tuple(s * x for x in n); return n, int(math.isqrt(dot(n, n)))
# ================= Bài 17. Phương trình mặt cầu =================
def sp_cr(r, lv):
    I = _I(r); R = r.randint(1, 6)
    return dict(en='The sphere \\(%s\\) has centre and radius…' % sph(I, R * R), vi='Mặt cầu \\(%s\\) có tâm và bán kính là…' % sph(I, R * R),
      opts=pick_opts(r, 'I%s,\\ R=%d' % (V3(I), R), ['I%s,\\ R=%d' % (V3(tuple(-x for x in I)), R) if any(I) else 'I(1;\\,1;\\,1),\\ R=%d' % R, 'I%s,\\ R=%d' % (V3(I), R * R), 'I%s,\\ R=%d' % (V3(tuple(-x for x in I)), R * R) if any(I) else 'I(0;\\,0;\\,0),\\ R=%d' % (R + 1), 'I%s,\\ R=%d' % (V3(I), R + 1)]), ans=0,
      ee='\\((x-a)^2+(y-b)^2+(z-c)^2=R^2\\): \\(I(a;b;c)\\), \\(R=\\sqrt{%d}=%d\\).' % (R * R, R), ev='\\((x-a)^2+(y-b)^2+(z-c)^2=R^2\\): tâm \\(I(a;b;c)\\), \\(R=\\sqrt{%d}=%d\\).' % (R * R, R))
def sp_gen(r, lv):
    I = _I(r); R = r.randint(1, 6); d = dot(I, I) - R * R
    if not any(I): raise AssertionError
    return dict(en='The sphere \\(%s\\) has centre and radius…' % gen(I, d), vi='Mặt cầu \\(%s\\) có tâm và bán kính là…' % gen(I, d),
      opts=pick_opts(r, 'I%s,\\ R=%d' % (V3(I), R), ['I%s,\\ R=%d' % (V3(tuple(-x for x in I)), R), 'I%s,\\ R=%d' % (V3(tuple(2 * x for x in I)), R), 'I%s,\\ R=\\sqrt{%d}' % (V3(I), dot(I, I) + d) if dot(I, I) + d > 0 else 'I%s,\\ R=%d' % (V3(I), R + 1), 'I%s,\\ R=%d' % (V3(I), R + 2)]), ans=0,
      ee='\\(a,b,c\\) are minus half the coefficients; \\(R^2=a^2+b^2+c^2-d=%d\\).' % (R * R), ev='\\(a,b,c\\) bằng âm một nửa các hệ số; \\(R^2=a^2+b^2+c^2-d=%d\\).' % (R * R))
def sp_write(r, lv):
    I = _I(r); R = r.randint(1, 5)
    return dict(en='The sphere with centre \\(I%s\\) and radius \\(%d\\) is…' % (V3(I), R), vi='Mặt cầu tâm \\(I%s\\), bán kính \\(%d\\) có phương trình…' % (V3(I), R),
      opts=pick_opts(r, sph(I, R * R), [sph(I, R), sph(tuple(-x for x in I), R * R) if any(I) else sph((1, 0, 0), R * R), sph(tuple(-x for x in I), R) if any(I) else sph(I, 2 * R), sph(I, 2 * R * R)]), ans=0,
      ee='Right side is \\(R^2=%d\\).' % (R * R), ev='Vế phải là \\(R^2=%d\\).' % (R * R))
def sp_through(r, lv):
    I = _I(r); A = _I(r); R2 = dot(sub(A, I), sub(A, I))
    if R2 == 0: raise AssertionError
    return dict(en='The sphere with centre \\(I%s\\) passing through \\(A%s\\) is…' % (V3(I), V3(A)), vi='Mặt cầu tâm \\(I%s\\) và đi qua \\(A%s\\) có phương trình…' % (V3(I), V3(A)),
      opts=pick_opts(r, sph(I, R2), [sph(A, R2), sph(I, R2 + 1), sph(I, dot(A, A)) if dot(A, A) != R2 else sph(I, R2 * 2), sph(tuple(-x for x in I), R2) if any(I) else sph(I, R2 + 2)]), ans=0,
      ee='\\(R^2=IA^2=%d\\).' % R2, ev='\\(R^2=IA^2=%d\\).' % R2)
def sp_diam(r, lv):
    I = _I(r); h = (r.randint(-2, 2), r.randint(-2, 2), r.randint(-2, 2))
    if not any(h): raise AssertionError
    A = sub(I, h); B = tuple(i + k for i, k in zip(I, h)); R2 = dot(h, h)
    return dict(en='The sphere with diameter \\(AB\\), \\(A%s\\), \\(B%s\\), is…' % (V3(A), V3(B)), vi='Mặt cầu đường kính \\(AB\\) với \\(A%s\\), \\(B%s\\) có phương trình…' % (V3(A), V3(B)),
      opts=pick_opts(r, sph(I, R2), [sph(I, 4 * R2), sph(A, R2), sph(I, 2 * R2), sph(B, 4 * R2)]), ans=0,
      ee='Centre = midpoint \\(I%s\\), \\(R=\\frac{AB}{2}\\), \\(R^2=%d\\).' % (V3(I), R2), ev='Tâm là trung điểm \\(I%s\\), \\(R=\\frac{AB}{2}\\), \\(R^2=%d\\).' % (V3(I), R2))
def sp_cond(r, lv):
    I = _I(r)
    if not any(I): raise AssertionError
    k = dot(I, I)
    return dict(en='\\(%s\\) is the equation of a sphere exactly when…' % gen(I, 0).replace('=0', '+m=0'), vi='\\(%s\\) là phương trình mặt cầu khi và chỉ khi…' % gen(I, 0).replace('=0', '+m=0'),
      opts=pick_opts(r, 'm\\lt%d' % k, ['m\\gt%d' % k, 'm\\le%d' % k, 'm\\lt%d' % (k * 2) if k else 'm\\lt1', 'm\\gt-%d' % k]), ans=0,
      ee='Need \\(a^2+b^2+c^2-d=%d-m\\gt0\\).' % k, ev='Cần \\(a^2+b^2+c^2-d=%d-m\\gt0\\).' % k)
def sp_pt(r, lv):
    I = _I(r); R = r.randint(2, 5); A = tuple(i + r.randint(-3, 3) for i in I); d2 = dot(sub(A, I), sub(A, I))
    pos = 0 if d2 < R * R else 1 if d2 == R * R else 2
    L = [TT('inside the sphere', 'nằm trong mặt cầu'), TT('on the sphere', 'nằm trên mặt cầu'), TT('outside the sphere', 'nằm ngoài mặt cầu'), TT('at the centre', 'trùng với tâm')]
    if d2 == 0: raise AssertionError
    return dict(en='Where is \\(A%s\\) relative to the sphere \\(%s\\)?' % (V3(A), sph(I, R * R)), vi='Điểm \\(A%s\\) có vị trí thế nào so với mặt cầu \\(%s\\)?' % (V3(A), sph(I, R * R)),
      opts=[L[pos]] + [L[j] for j in range(4) if j != pos], ans=0,
      ee='\\(IA^2=%d\\), \\(R^2=%d\\).' % (d2, R * R), ev='\\(IA^2=%d\\), \\(R^2=%d\\).' % (d2, R * R))
def sp_tan(r, lv):
    I = _I(r); n, L = _n(r); t = r.choice([1, 2, -1, -2]); Dd = -dot(n, I) + t * L
    d = abs(dot(n, I) + Dd) // L; assert d * L == abs(dot(n, I) + Dd)
    return dict(en='The sphere with centre \\(I%s\\) tangent to \\((P): %s\\) has radius…' % (V3(I), eq(*n, Dd)), vi='Mặt cầu tâm \\(I%s\\) tiếp xúc với \\((P): %s\\) có bán kính…' % (V3(I), eq(*n, Dd)),
      opts=pick_opts(r, str(d), [str(d * L), str(d * d), str(abs(Dd)) if abs(Dd) not in (d, d * L, d * d) else str(d + 1), str(d + L)]), ans=0,
      ee='\\(R=d(I,(P))=\\dfrac{|%d|}{%d}=%d\\).' % (dot(n, I) + Dd, L, d), ev='\\(R=d(I,(P))=\\dfrac{|%d|}{%d}=%d\\).' % (dot(n, I) + Dd, L, d))
def sp_plane(r, lv):
    I = _I(r); n, L = _n(r); d = r.randint(1, 5); R = r.randint(1, 6)
    if d == R and r.random() < .5: pass
    Dd = -dot(n, I) + d * L * r.choice([1, -1])
    pos = 0 if d < R else 1 if d == R else 2
    opts = [TT('they cut along a circle', 'cắt nhau theo một đường tròn'), TT('they are tangent', 'tiếp xúc nhau'), TT('they have no common point', 'không có điểm chung'), TT('the plane passes through the centre', 'mặt phẳng đi qua tâm')]
    return dict(en='Relative position of \\((S): %s\\) and \\((P): %s\\):' % (sph(I, R * R), eq(*n, Dd)), vi='Vị trí tương đối của \\((S): %s\\) và \\((P): %s\\) là…' % (sph(I, R * R), eq(*n, Dd)),
      opts=[opts[pos]] + [opts[j] for j in range(4) if j != pos], ans=0,
      ee='\\(d(I,(P))=%d\\), \\(R=%d\\).' % (d, R), ev='\\(d(I,(P))=%d\\), \\(R=%d\\).' % (d, R))
PYT = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (4, 3, 5), (8, 6, 10), (12, 5, 13)]
def sp_circ(r, lv):
    I = _I(r); n, L = _n(r); d, rr, R = r.choice(PYT); Dd = -dot(n, I) + d * L * r.choice([1, -1])
    return dict(en='\\((P): %s\\) cuts \\((S): %s\\) along a circle of radius…' % (eq(*n, Dd), sph(I, R * R)), vi='\\((P): %s\\) cắt \\((S): %s\\) theo đường tròn có bán kính…' % (eq(*n, Dd), sph(I, R * R)),
      opts=pick_opts(r, str(rr), [str(R - d), str(d), '\\sqrt{%d}' % (R * R + d * d), str(R)]), ans=0,
      ee='\\(r=\\sqrt{R^2-d^2}=\\sqrt{%d-%d}=%d\\).' % (R * R, d * d, rr), ev='\\(r=\\sqrt{R^2-d^2}=\\sqrt{%d-%d}=%d\\).' % (R * R, d * d, rr))
def sp_on(r, lv):
    I = _I(r); R = r.choice([3, 5, 7, 9]); vs = [v for v in itertools.product(range(-R, R + 1), repeat=3) if dot(v, v) == R * R]
    v = r.choice(vs); A = tuple(i + k for i, k in zip(I, v)); others = []
    for _ in range(60):
        w = tuple(a + r.randint(-1, 1) for a in A); dd = dot(sub(w, I), sub(w, I))
        if dd != R * R and V3(w) not in others: others.append(V3(w))
    return dict(en='Which point lies on \\((S): %s\\)?' % sph(I, R * R), vi='Điểm nào thuộc mặt cầu \\((S): %s\\)?' % sph(I, R * R), opts=pick_opts(r, V3(A), others[:3]), ans=0,
      ee='\\(IA^2=%d=R^2\\).' % (R * R), ev='\\(IA^2=%d=R^2\\).' % (R * R))
def sp_foot(r, lv):
    I = _I(r); n, L = _n(r); t = r.choice([1, -1, 2]); H = tuple(i - t * k for i, k in zip(I, n)); Dd = -dot(n, H)
    return dict(en='The sphere with centre \\(I%s\\) touches \\((P): %s\\) at…' % (V3(I), eq(*n, Dd)), vi='Mặt cầu tâm \\(I%s\\) tiếp xúc với \\((P): %s\\) tại điểm…' % (V3(I), eq(*n, Dd)),
      opts=pick_opts(r, V3(H), [V3(tuple(i + t * k for i, k in zip(I, n))), V3(n), V3(tuple(i - k for i, k in zip(I, n))) if t != 1 else V3(tuple(i - 2 * k for i, k in zip(I, n))), V3(I)]), ans=0,
      ee='Projection of \\(I\\) on \\((P)\\): \\(I-%d\\vec n=%s\\).' % (t, V3(H)), ev='Hình chiếu của \\(I\\) trên \\((P)\\): \\(H=I-%d\\vec n=%s\\).' % (t, V3(H)))
def sp_wifi(r, lv):
    I = (r.randint(0, 6), r.randint(0, 6), r.choice([2, 3])); R = r.choice([5, 7, 9, 10]); vs = [v for v in itertools.product(range(-R - 1, R + 2), repeat=3) if dot(v, v) in (R * R - 2, R * R + 2, R * R - 5, R * R + 5)]
    v = r.choice(vs); A = tuple(i + k for i, k in zip(I, v)); ok = dot(v, v) <= R * R
    o = [TT('yes, \\(IA^2=%d\\le%d\\)' % (dot(v, v), R * R), 'có, vì \\(IA^2=%d\\le%d\\)' % (dot(v, v), R * R)), TT('no, \\(IA^2=%d\\gt%d\\)' % (dot(v, v), R * R), 'không, vì \\(IA^2=%d\\gt%d\\)' % (dot(v, v), R * R)),
         TT('yes, \\(IA=%d\\)' % R, 'có, vì \\(IA=%d\\)' % R), TT('no, \\(IA=%d\\)' % (R + 1), 'không, vì \\(IA=%d\\)' % (R + 1))]
    if not ok: o = [o[1], o[0], o[2], o[3]]
    return dict(en='A Wi-Fi router at \\(I%s\\) (m) covers a ball of radius %d m. Is the phone at \\(A%s\\) covered?' % (V3(I), R, V3(A)), vi='Bộ phát Wi-Fi đặt tại \\(I%s\\) (m) phủ sóng trong khối cầu bán kính %d m. Điện thoại tại \\(A%s\\) có bắt được sóng không?' % (V3(I), R, V3(A)),
      opts=o, ans=0, ee='\\(IA^2=%d\\), \\(R^2=%d\\).' % (dot(v, v), R * R), ev='\\(IA^2=%d\\), \\(R^2=%d\\).' % (dot(v, v), R * R))
def sp_ground(r, lv):
    I = (r.randint(-3, 3), r.randint(-3, 3), r.randint(1, 6)); R = I[2]
    return dict(en='A ball with centre \\(I%s\\) rests on the floor \\((Oxy)\\). Its equation is…' % V3(I), vi='Quả bóng tâm \\(I%s\\) đặt trên sàn \\((Oxy)\\) (tiếp xúc với sàn). Phương trình mặt cầu là…' % V3(I),
      opts=pick_opts(r, sph(I, R * R), [sph(I, R), sph(I, dot(I, I)), sph(I, (R + 1) ** 2), sph(I, I[0] ** 2 + I[1] ** 2 if I[0] or I[1] else 1)]), ans=0,
      ee='\\(R=d(I,(Oxy))=|z_I|=%d\\).' % R, ev='\\(R=d(I,(Oxy))=|z_I|=%d\\).' % R)
def sp_line(r, lv):
    I = _I(r); R = r.choice([3, 5]); u = r.choice([(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 2, 2)]); w = r.choice([(0, 0, 1), (0, 1, 0), (1, 0, 0), (2, -2, 1), (2, 1, -2)])
    if dot(u, w): raise AssertionError
    k = r.choice([0, 1, 2]); dist = [0, R, R + 2][k] * 1
    # M = I + dist * w/|w|; dùng w có |w| nguyên
    Lw = int(math.isqrt(dot(w, w)))
    if Lw * Lw != dot(w, w) or dist % Lw and dist: raise AssertionError
    M = tuple(i + (dist // Lw) * c for i, c in zip(I, w)) if dist else I
    if dist and (dist // Lw) * Lw != dist: raise AssertionError
    n_pts = 2 if dist < R else 1 if dist == R else 0
    par = '\\begin{cases}%s\\end{cases}' % '\\\\'.join('%s=%s' % (c, ('%d' % m if m else '') + (('+' if a > 0 and m else '') + ('' if abs(a) == 1 else str(a)).replace('-1', '-') + 't' if a else '') or '0') for c, m, a in zip('xyz', M, u))
    return dict(en='How many common points do the line \\(%s\\) and the sphere \\(%s\\) have?' % (par, sph(I, R * R)), vi='Đường thẳng \\(%s\\) và mặt cầu \\(%s\\) có bao nhiêu điểm chung?' % (par, sph(I, R * R)),
      opts=pick_opts(r, str(n_pts), [str(x) for x in (0, 1, 2, 3) if x != n_pts]), ans=0,
      ee='Distance from \\(I\\) to the line \\(=%d\\), \\(R=%d\\).' % (dist, R), ev='Khoảng cách từ \\(I\\) đến đường thẳng bằng \\(%d\\), \\(R=%d\\).' % (dist, R))
M17S12 = [sp_cr, sp_gen, sp_write, sp_through, sp_diam, sp_cond, sp_pt, sp_tan, sp_plane, sp_circ, sp_on, sp_foot, sp_wifi, sp_ground, sp_line]
# ================= Bài 18. Xác suất có điều kiện =================
def cp_formula(r, lv):
    b = F(r.choice([2, 3, 4, 5, 6]), 10); a = b * F(r.choice([1, 2, 3]), r.choice([4, 5]))
    c = a / b
    return dict(en='\\(P(B)=%s\\), \\(P(A\\cap B)=%s\\). Then \\(P(A\\mid B)=\\)…' % (PE(b), PE(a)), vi='Cho \\(P(B)=%s\\), \\(P(A\\cap B)=%s\\). Khi đó \\(P(A\\mid B)=\\)…' % (P(b), P(a)),
      opts=popts(r, c, [a * b, b - a, a, 1 - c, b / 2]), ans=0, ee='\\(P(A\\mid B)=\\dfrac{P(A\\cap B)}{P(B)}\\).', ev='\\(P(A\\mid B)=\\dfrac{P(A\\cap B)}{P(B)}=%s\\).' % P(c))
def _tab(r):
    a, b, c, d = (r.randint(5, 30) for _ in range(4)); return a, b, c, d
def cp_table(r, lv):
    a, b, c, d = _tab(r)   # nam thích / nam không ; nữ thích / nữ không
    T = '\\begin{array}{c|cc}&\\text{Yes}&\\text{No}\\\\\\hline\\text{Boys}&%d&%d\\\\\\text{Girls}&%d&%d\\end{array}' % (a, b, c, d)
    Tv = T.replace('Yes', 'Thích').replace('No', 'Không').replace('Boys', 'Nam').replace('Girls', 'Nữ')
    q = r.choice(['g', 'y']); ans = F(c, c + d) if q == 'g' else F(c, a + c)
    en = 'Survey: \\(%s\\). A random student is %s. The probability that %s is…' % (T, 'a girl' if q == 'g' else 'one who answered "Yes"', 'she said "Yes"' if q == 'g' else 'it is a girl')
    vi = 'Khảo sát: \\(%s\\). Chọn ngẫu nhiên một học sinh, biết %s. Xác suất %s là…' % (Tv, 'đó là nữ' if q == 'g' else 'học sinh đó trả lời "Thích"', 'em đó trả lời "Thích"' if q == 'g' else 'đó là nữ')
    return dict(en=en, vi=vi, opts=popts(r, ans, [F(c, a + b + c + d), F(a, a + b) if q == 'g' else F(a, a + c), F(c + d, a + b + c + d), 1 - ans, F(d, c + d)]), ans=0,
      ee='Restrict to the given group: \\(%s\\).' % P(ans), ev='Chỉ xét trong nhóm đã biết: \\(%s\\).' % P(ans))
def cp_draw(r, lv):
    rd, bl = r.randint(3, 8), r.randint(2, 7); n = rd + bl; c = F(rd - 1, n - 1)
    return dict(en='A box has %d red and %d blue balls. Two balls are drawn one after another without replacement. Given that the first is red, the probability that the second is red is…' % (rd, bl), vi='Hộp có %d bi đỏ và %d bi xanh. Lấy lần lượt 2 bi không hoàn lại. Biết bi thứ nhất màu đỏ, xác suất bi thứ hai màu đỏ là…' % (rd, bl),
      opts=popts(r, c, [F(rd, n), F(rd - 1, n), F(rd, n - 1), F(bl, n - 1), F(rd * (rd - 1), n * (n - 1))]), ans=0,
      ee='After one red ball: %d red among %d.' % (rd - 1, n - 1), ev='Sau khi lấy 1 bi đỏ còn %d bi đỏ trong %d bi.' % (rd - 1, n - 1))
def cp_mult(r, lv):
    rd, bl = r.randint(3, 8), r.randint(2, 7); n = rd + bl; c = F(rd, n) * F(rd - 1, n - 1)
    return dict(en='A box has %d red and %d blue balls; draw 2 without replacement. \\(P(\\text{both red})=\\)…' % (rd, bl), vi='Hộp có %d bi đỏ và %d bi xanh; lấy lần lượt 2 bi không hoàn lại. Xác suất cả hai bi đều đỏ là…' % (rd, bl),
      opts=popts(r, c, [F(rd, n) ** 2, F(rd - 1, n - 1), F(rd, n) * F(rd - 1, n), F(2 * rd, n * (n - 1)), F(rd * bl, n * (n - 1))]), ans=0,
      ee='\\(P(A\\cap B)=P(A)P(B\\mid A)=\\frac{%d}{%d}\\cdot\\frac{%d}{%d}\\).' % (rd, n, rd - 1, n - 1), ev='Công thức nhân: \\(P(A\\cap B)=P(A)P(B\\mid A)=\\frac{%d}{%d}\\cdot\\frac{%d}{%d}=%s\\).' % (rd, n, rd - 1, n - 1, P(c)))
def cp_dice(r, lv):
    s = r.randint(5, 10); k = r.randint(1, 6); B = [(i, j) for i in range(1, 7) for j in range(1, 7) if i + j == s]; AB = [p for p in B if p[0] == k]
    if not AB: raise AssertionError
    c = F(len(AB), len(B))
    return dict(en='Two dice are rolled. Given that the sum is %d, the probability that the first die shows %d is…' % (s, k), vi='Gieo hai con xúc xắc. Biết tổng số chấm bằng %d, xác suất con thứ nhất ra %d chấm là…' % (s, k),
      opts=popts(r, c, [F(1, 6), F(len(AB), 36), F(len(B), 36), F(2, len(B)), F(1, 12)]), ans=0,
      ee='\\(|B|=%d\\), \\(|A\\cap B|=%d\\).' % (len(B), len(AB)), ev='Các kết quả có tổng %d: %d; trong đó con thứ nhất ra %d: %d.' % (s, len(B), k, len(AB)))
def cp_indep(r, lv):
    a, b = F(r.choice([2, 3, 4, 5]), 10), F(r.choice([3, 4, 5, 6]), 10); ind = r.random() < .5; ab = a * b if ind else a * b + F(r.choice([1, 2]), 100)
    opts = [TT('independent, \\(P(A\\mid B)=P(A)\\)', 'độc lập, \\(P(A\\mid B)=P(A)\\)'), TT('not independent', 'không độc lập')]
    if not ind: opts.reverse()
    return dict(en='\\(P(A)=%s\\), \\(P(B)=%s\\), \\(P(A\\cap B)=%s\\). The events \\(A\\), \\(B\\) are…' % (PE(a), PE(b), PE(ab)), vi='Cho \\(P(A)=%s\\), \\(P(B)=%s\\), \\(P(A\\cap B)=%s\\). Hai biến cố \\(A\\), \\(B\\)…' % (P(a), P(b), P(ab)),
      opts=opts + [TT('mutually exclusive', 'xung khắc'), TT('complementary', 'đối nhau')], ans=0,
      ee='\\(P(A)P(B)=%s\\).' % PE(a * b), ev='\\(P(A)P(B)=%s\\) so với \\(P(A\\cap B)=%s\\).' % (P(a * b), P(ab)))
def cp_num(r, lv):
    N = r.choice([20, 24, 30, 36, 40]); m1, m2 = r.choice([(2, 3), (3, 2), (2, 5), (5, 2), (3, 4), (4, 3)])
    B = [x for x in range(1, N + 1) if x % m1 == 0]; AB = [x for x in B if x % m2 == 0]; c = F(len(AB), len(B))
    return dict(en='A card is drawn from cards numbered 1 to %d. Given that the number is divisible by %d, the probability that it is divisible by %d is…' % (N, m1, m2), vi='Rút một thẻ từ các thẻ đánh số 1 đến %d. Biết số trên thẻ chia hết cho %d, xác suất số đó chia hết cho %d là…' % (N, m1, m2),
      opts=popts(r, c, [F(len(AB), N), F(len([x for x in range(1, N + 1) if x % m2 == 0]), N), F(len(B), N), F(1, m1 * m2), 1 - c]), ans=0,
      ee='%d multiples of %d; %d of them are multiples of %d.' % (len(B), m1, len(AB), m2), ev='Có %d số chia hết cho %d, trong đó %d số chia hết cho %d.' % (len(B), m1, len(AB), m2))
def cp_comp(r, lv):
    c = F(r.choice([1, 2, 3, 4, 5, 6, 7]), r.choice([8, 10, 9]))
    return dict(en='\\(P(A\\mid B)=%s\\). Then \\(P(\\overline A\\mid B)=\\)…' % PE(c), vi='Cho \\(P(A\\mid B)=%s\\). Khi đó \\(P(\\overline A\\mid B)=\\)…' % P(c),
      opts=popts(r, 1 - c, [c, c / 2, 1 - c / 2, F(1, 2) if c != F(1, 2) else F(1, 3)]), ans=0, ee='\\(P(\\overline A\\mid B)=1-P(A\\mid B)\\).', ev='\\(P(\\overline A\\mid B)=1-P(A\\mid B)\\).')
def cp_and(r, lv):
    b = F(r.choice([3, 4, 5, 6, 8]), 10); c = F(r.choice([1, 2, 3, 4]), 5); ab = b * c
    return dict(en='\\(P(B)=%s\\), \\(P(A\\mid B)=%s\\). Then \\(P(A\\cap B)=\\)…' % (PE(b), PE(c)), vi='Cho \\(P(B)=%s\\), \\(P(A\\mid B)=%s\\). Khi đó \\(P(A\\cap B)=\\)…' % (P(b), P(c)),
      opts=popts(r, ab, [c / b if c < b else b - c if b > c else 1 - c, b + c - 1 if b + c > 1 else c, c, b, 1 - ab]), ans=0, ee='\\(P(A\\cap B)=P(B)\\cdot P(A\\mid B)\\).', ev='\\(P(A\\cap B)=P(B)\\cdot P(A\\mid B)=%s\\).' % P(ab))
def cp_kids(r, lv):
    n = r.choice([2, 3, 4]); g = r.choice(['B', 'G']); W = list(itertools.product('BG', repeat=n)); B = [w for w in W if g in w]; AB = [w for w in B if w.count(g) == n]
    c = F(len(AB), len(B)); en_g, vi_g = ('boy', 'trai') if g == 'B' else ('girl', 'gái')
    return dict(en='A family has %d children (boys and girls equally likely). Given that there is at least one %s, the probability that all are %ss is…' % (n, en_g, en_g), vi='Một gia đình có %d con (khả năng trai, gái như nhau). Biết có ít nhất một con %s, xác suất tất cả đều là con %s là…' % (n, vi_g, vi_g),
      opts=popts(r, c, [F(1, 2 ** n), F(1, 2), F(1, n), F(1, n + 1), F(2, 3)]), ans=0,
      ee='\\(|B|=%d\\), \\(|A\\cap B|=1\\).' % len(B), ev='Có %d khả năng có ít nhất một con %s; chỉ 1 khả năng tất cả đều là con %s.' % (len(B), vi_g, vi_g))
def cp_union(r, lv):
    a, b = F(r.choice([3, 4, 5]), 10), F(r.choice([4, 5, 6]), 10); ab = F(r.choice([1, 2]), 10); u = a + b - ab
    return dict(en='\\(P(A)=%s\\), \\(P(A\\cup B)=%s\\), \\(P(A\\cap B)=%s\\). Then \\(P(A\\mid B)=\\)…' % (PE(a), PE(u), PE(ab)), vi='Cho \\(P(A)=%s\\), \\(P(A\\cup B)=%s\\), \\(P(A\\cap B)=%s\\). Khi đó \\(P(A\\mid B)=\\)…' % (P(a), P(u), P(ab)),
      opts=popts(r, ab / b, [ab / a, ab / u, ab, b, ab * b]), ans=0, ee='\\(P(B)=P(A\\cup B)-P(A)+P(A\\cap B)=%s\\).' % PE(b), ev='\\(P(B)=P(A\\cup B)-P(A)+P(A\\cap B)=%s\\), rồi \\(P(A\\mid B)=%s\\).' % (P(b), P(ab / b)))
def cp_three(r, lv):
    rd, bl = r.randint(4, 8), r.randint(2, 6); n = rd + bl; c = F(rd, n) * F(rd - 1, n - 1) * F(rd - 2, n - 2)
    return dict(en='From %d red and %d white balls, draw 3 one by one without replacement. \\(P(\\text{all red})=\\)…' % (rd, bl), vi='Từ %d bi đỏ và %d bi trắng, lấy lần lượt 3 bi không hoàn lại. Xác suất cả 3 bi đều đỏ là…' % (rd, bl),
      opts=popts(r, c, [F(rd, n) ** 3, F(rd - 2, n - 2), F(rd * (rd - 1) * (rd - 2), n ** 3), F(3 * rd, n * (n - 1) * (n - 2))]), ans=0,
      ee='\\(\\frac{%d}{%d}\\cdot\\frac{%d}{%d}\\cdot\\frac{%d}{%d}\\).' % (rd, n, rd - 1, n - 1, rd - 2, n - 2), ev='Công thức nhân: \\(\\frac{%d}{%d}\\cdot\\frac{%d}{%d}\\cdot\\frac{%d}{%d}=%s\\).' % (rd, n, rd - 1, n - 1, rd - 2, n - 2, P(c)))
def cp_six(r, lv):
    k = r.randint(1, 6); W = [(i, j) for i in range(1, 7) for j in range(1, 7)]; B = [w for w in W if k in w]; AB = [w for w in B if w == (k, k)]
    kind = r.choice(['both', 'sum'])
    if kind == 'both': c = F(len(AB), len(B)); q = 'both show %d' % k; qv = 'cả hai đều ra %d chấm' % k
    else:
        s = r.randint(k + 1, k + 6); AB = [w for w in B if sum(w) == s]; c = F(len(AB), len(B)); q = 'the sum is %d' % s; qv = 'tổng số chấm bằng %d' % s
        if not AB: raise AssertionError
    return dict(en='Two dice are rolled. Given that at least one die shows %d, the probability that %s is…' % (k, q), vi='Gieo hai con xúc xắc. Biết có ít nhất một con ra %d chấm, xác suất %s là…' % (k, qv),
      opts=popts(r, c, [F(len(AB), 36), F(1, 6), F(1, 36), F(len(AB), 12), F(2, 11) if c != F(2, 11) else F(3, 11)]), ans=0,
      ee='\\(|B|=11\\), \\(|A\\cap B|=%d\\).' % len(AB), ev='Có 11 kết quả có ít nhất một mặt %d chấm; trong đó %d kết quả thỏa mãn.' % (k, len(AB)))
def cp_med(r, lv):
    sick = r.choice([40, 50, 60]); tp = sick - r.choice([2, 4, 5]); healthy = r.choice([160, 200, 240]); fp = r.choice([8, 10, 12, 16])
    pos = tp + fp; c = F(tp, pos)
    return dict(en='Of %d sick people, %d test positive; of %d healthy people, %d test positive. Given a positive test, the probability that the person is sick is…' % (sick, tp, healthy, fp), vi='Trong %d người bệnh có %d người xét nghiệm dương tính; trong %d người khỏe có %d người dương tính. Biết một người dương tính, xác suất người đó bị bệnh là…' % (sick, tp, healthy, fp),
      opts=popts(r, c, [F(tp, sick), F(tp, sick + healthy), F(sick, sick + healthy), F(fp, pos), F(tp, healthy)]), ans=0,
      ee='\\(\\dfrac{%d}{%d+%d}\\).' % (tp, tp, fp), ev='Chỉ xét %d người dương tính: \\(\\dfrac{%d}{%d}\\).' % (pos, tp, pos))
M18S12 = [cp_formula, cp_table, cp_draw, cp_mult, cp_dice, cp_indep, cp_num, cp_comp, cp_and, cp_kids, cp_union, cp_three, cp_six, cp_med, cp_formula]
# ================= Bài 19. Xác suất toàn phần, Bayes =================
def _pct(r, lo, hi): return F(r.randint(lo, hi), 100)
def tp_basic(r, lv):
    b = F(r.choice([2, 3, 4, 5, 6, 7]), 10); x, y = F(r.choice([1, 2, 3, 4, 5, 6, 7, 8, 9]), 10), F(r.choice([1, 2, 3, 4, 5, 6, 7]), 10); c = b * x + (1 - b) * y
    return dict(en='\\(P(B)=%s\\), \\(P(A\\mid B)=%s\\), \\(P(A\\mid\\overline B)=%s\\). Then \\(P(A)=\\)…' % (PE(b), PE(x), PE(y)), vi='Cho \\(P(B)=%s\\), \\(P(A\\mid B)=%s\\), \\(P(A\\mid\\overline B)=%s\\). Khi đó \\(P(A)=\\)…' % (P(b), P(x), P(y)),
      opts=popts(r, c, [b * x + b * y, x + y if x + y <= 1 else (x + y) / 2, b * x, (1 - b) * x + b * y, b * x + (1 - b) * (1 - y)]), ans=0,
      ee='\\(P(A)=P(B)P(A\\mid B)+P(\\overline B)P(A\\mid\\overline B)\\).', ev='\\(P(A)=P(B)P(A\\mid B)+P(\\overline B)P(A\\mid\\overline B)=%s\\).' % P(c))
def by_basic(r, lv):
    b = F(r.choice([2, 3, 4, 5, 6]), 10); x, y = F(r.choice([2, 3, 5, 6, 7, 8, 9]), 10), F(r.choice([1, 2, 3, 4]), 10); pa = b * x + (1 - b) * y; c = b * x / pa
    return dict(en='\\(P(B)=%s\\), \\(P(A\\mid B)=%s\\), \\(P(A\\mid\\overline B)=%s\\). Then \\(P(B\\mid A)=\\)…' % (PE(b), PE(x), PE(y)), vi='Cho \\(P(B)=%s\\), \\(P(A\\mid B)=%s\\), \\(P(A\\mid\\overline B)=%s\\). Khi đó \\(P(B\\mid A)=\\)…' % (P(b), P(x), P(y)),
      opts=popts(r, c, [b * x, x, pa, (1 - b) * y / pa, b * x / (x + y)]), ans=0,
      ee='\\(P(B\\mid A)=\\dfrac{P(B)P(A\\mid B)}{P(A)}\\), \\(P(A)=%s\\).' % PE(pa), ev='Bayes: \\(P(B\\mid A)=\\dfrac{P(B)P(A\\mid B)}{P(A)}\\) với \\(P(A)=%s\\).' % P(pa))
def _fact(r):
    s = r.choice([(50, 30, 20), (40, 35, 25), (60, 25, 15), (45, 35, 20), (30, 30, 40)]); d = tuple(r.choice([1, 2, 3, 4, 5]) for _ in range(3))
    return [F(x, 100) for x in s], [F(x, 100) for x in d], s, d
def tp_fact(r, lv):
    sh, de, s, d = _fact(r); c = sum(a * b for a, b in zip(sh, de))
    return dict(en='Three machines make %d%%, %d%%, %d%% of the products, with defect rates %d%%, %d%%, %d%%. A random product is defective with probability…' % (s + d), vi='Ba máy sản xuất lần lượt %d%%, %d%%, %d%% sản phẩm, tỉ lệ phế phẩm tương ứng %d%%, %d%%, %d%%. Xác suất một sản phẩm ngẫu nhiên là phế phẩm bằng…' % (s + d),
      opts=popts(r, c, [sum(de) / 3, sum(de), F(sum(d), 100) * F(1, 3) + F(1, 1000), max(de), c * 2]), ans=0,
      ee='\\(\\sum P(B_i)P(A\\mid B_i)=%s\\).' % PE(c), ev='Xác suất toàn phần: \\(\\sum P(B_i)P(A\\mid B_i)=%s\\).' % P(c))
def by_fact(r, lv):
    sh, de, s, d = _fact(r); i = r.randrange(3); pa = sum(a * b for a, b in zip(sh, de)); c = sh[i] * de[i] / pa
    return dict(en='Machines I, II, III make %d%%, %d%%, %d%% of the products with defect rates %d%%, %d%%, %d%%. A product is defective. The probability it came from machine %s is…' % (s + d + ('I' * (i + 1) if i < 3 else '',)), vi='Máy I, II, III sản xuất %d%%, %d%%, %d%% sản phẩm, tỉ lệ phế phẩm %d%%, %d%%, %d%%. Lấy được một phế phẩm. Xác suất nó do máy %s sản xuất là…' % (s + d + ('I' * (i + 1),)),
      opts=popts(r, c, [sh[i] * de[i], sh[i], de[i] / sum(de), F(1, 3), sh[i] * de[i] / sum(de)]), ans=0,
      ee='\\(\\dfrac{%s\\cdot%s}{%s}\\).' % (PE(sh[i]), PE(de[i]), PE(pa)), ev='Bayes: \\(\\dfrac{%s\\cdot%s}{%s}=%s\\).' % (P(sh[i]), P(de[i]), P(pa), P(c)))
def _urn(r):
    r1, w1, r2, w2 = r.randint(1, 6), r.randint(1, 6), r.randint(1, 6), r.randint(1, 6); return r1, w1, r2, w2
def tp_urn(r, lv):
    r1, w1, r2, w2 = _urn(r); c = F(1, 2) * F(r1, r1 + w1) + F(1, 2) * F(r2, r2 + w2)
    return dict(en='Box 1: %d red, %d white; box 2: %d red, %d white. Choose a box at random, then a ball. \\(P(\\text{red})=\\)…' % (r1, w1, r2, w2), vi='Hộp 1 có %d bi đỏ, %d bi trắng; hộp 2 có %d bi đỏ, %d bi trắng. Chọn ngẫu nhiên một hộp rồi lấy một bi. Xác suất lấy được bi đỏ là…' % (r1, w1, r2, w2),
      opts=popts(r, c, [F(r1 + r2, r1 + w1 + r2 + w2), F(r1, r1 + w1) + F(r2, r2 + w2), F(r1, r1 + w1) * F(r2, r2 + w2), F(1, 2), 1 - c]), ans=0,
      ee='\\(\\frac12\\cdot\\frac{%d}{%d}+\\frac12\\cdot\\frac{%d}{%d}\\).' % (r1, r1 + w1, r2, r2 + w2), ev='\\(\\frac12\\cdot\\frac{%d}{%d}+\\frac12\\cdot\\frac{%d}{%d}=%s\\).' % (r1, r1 + w1, r2, r2 + w2, P(c)))
def by_urn(r, lv):
    r1, w1, r2, w2 = _urn(r); pa = F(1, 2) * F(r1, r1 + w1) + F(1, 2) * F(r2, r2 + w2); c = F(1, 2) * F(r1, r1 + w1) / pa
    return dict(en='Box 1: %d red, %d white; box 2: %d red, %d white. A box is chosen at random and a red ball is drawn. The probability that it came from box 1 is…' % (r1, w1, r2, w2), vi='Hộp 1: %d đỏ, %d trắng; hộp 2: %d đỏ, %d trắng. Chọn ngẫu nhiên một hộp rồi lấy được bi đỏ. Xác suất bi đó thuộc hộp 1 là…' % (r1, w1, r2, w2),
      opts=popts(r, c, [F(1, 2), F(r1, r1 + w1), F(r1, r1 + r2), F(1, 2) * F(r1, r1 + w1), 1 - c]), ans=0,
      ee='\\(P(H_1\\mid D)=\\dfrac{\\frac12\\cdot\\frac{%d}{%d}}{%s}\\).' % (r1, r1 + w1, PE(pa)), ev='\\(P(H_1\\mid D)=\\dfrac{\\frac12\\cdot\\frac{%d}{%d}}{%s}=%s\\).' % (r1, r1 + w1, P(pa), P(c)))
def _test(r):
    p = F(r.choice([1, 2, 4, 5, 10]), 100); se = F(r.choice([90, 95, 98, 99]), 100); fp = F(r.choice([2, 4, 5, 10]), 100); return p, se, fp
def tp_test(r, lv):
    p, se, fp = _test(r); c = p * se + (1 - p) * fp
    return dict(en='A disease affects %s%% of people. A test is positive for %s%% of sick people and for %s%% of healthy people. \\(P(\\text{positive})=\\)…' % (PE(p * 100), PE(se * 100), PE(fp * 100)), vi='Một bệnh có tỉ lệ mắc %s%%. Xét nghiệm dương tính với %s%% người bệnh và %s%% người khỏe. Xác suất một người xét nghiệm dương tính là…' % (P(p * 100), P(se * 100), P(fp * 100)),
      opts=popts(r, c, [p * se, se, p * se + p * fp, (1 - p) * fp, p + fp]), ans=0, ee='\\(%s\\cdot%s+%s\\cdot%s\\).' % (PE(p), PE(se), PE(1 - p), PE(fp)), ev='\\(%s\\cdot%s+%s\\cdot%s=%s\\).' % (P(p), P(se), P(1 - p), P(fp), P(c)))
def by_test(r, lv):
    p, se, fp = _test(r); pa = p * se + (1 - p) * fp; c = p * se / pa
    return dict(en='Disease rate %s%%; the test is positive for %s%% of sick and %s%% of healthy people. A person tests positive. The probability that he is sick is…' % (PE(p * 100), PE(se * 100), PE(fp * 100)), vi='Tỉ lệ mắc bệnh %s%%; xét nghiệm dương tính với %s%% người bệnh và %s%% người khỏe. Một người có kết quả dương tính. Xác suất người đó mắc bệnh là…' % (P(p * 100), P(se * 100), P(fp * 100)),
      opts=popts(r, c, [se, p * se, 1 - fp, p, pa]), ans=0, ee='\\(\\dfrac{%s\\cdot%s}{%s}\\).' % (PE(p), PE(se), PE(pa)), ev='Bayes: \\(\\dfrac{%s\\cdot%s}{%s}=%s\\) – nhỏ hơn nhiều so với độ nhạy \\(%s\\).' % (P(p), P(se), P(pa), P(c), P(se)))
def tp_rain(r, lv):
    pr = _pct(r, 2, 6) * 10 / 10; pr = F(r.choice([2, 3, 4, 5, 6]), 10); lr, ln = F(r.choice([3, 4, 5, 6]), 10), F(r.choice([1, 2]), 10); c = pr * lr + (1 - pr) * ln
    return dict(en='It rains with probability %s. If it rains, Nam is late with probability %s; otherwise %s. \\(P(\\text{Nam is late})=\\)…' % (PE(pr), PE(lr), PE(ln)), vi='Xác suất trời mưa là %s. Nếu mưa, Nam đi học muộn với xác suất %s; nếu không mưa là %s. Xác suất Nam đi học muộn là…' % (P(pr), P(lr), P(ln)),
      opts=popts(r, c, [lr + ln, pr * lr, (lr + ln) / 2, pr * lr + pr * ln, 1 - c]), ans=0, ee='Total probability.', ev='Xác suất toàn phần: \\(%s\\cdot%s+%s\\cdot%s=%s\\).' % (P(pr), P(lr), P(1 - pr), P(ln), P(c)))
def by_spam(r, lv):
    s = F(r.choice([2, 3, 4, 5]), 10); w1, w0 = F(r.choice([4, 5, 6, 7, 8]), 10), F(r.choice([1, 2]), 20); pa = s * w1 + (1 - s) * w0; c = s * w1 / pa
    return dict(en='%s%% of e-mails are spam. The word "FREE" appears in %s%% of spam and %s%% of normal e-mails. An e-mail contains "FREE". \\(P(\\text{spam})=\\)…' % (PE(s * 100), PE(w1 * 100), PE(w0 * 100)), vi='%s%% thư là thư rác. Từ "FREE" xuất hiện trong %s%% thư rác và %s%% thư thường. Một thư có chữ "FREE". Xác suất đó là thư rác là…' % (P(s * 100), P(w1 * 100), P(w0 * 100)),
      opts=popts(r, c, [s, w1, s * w1, pa, w1 / (w1 + w0)]), ans=0, ee='\\(\\dfrac{%s\\cdot%s}{%s}\\).' % (PE(s), PE(w1), PE(pa)), ev='Bayes: \\(\\dfrac{%s\\cdot%s}{%s}=%s\\).' % (P(s), P(w1), P(pa), P(c)))
def tp_move(r, lv):
    r1, w1, r2, w2 = r.randint(2, 6), r.randint(2, 6), r.randint(1, 5), r.randint(1, 5); n2 = r2 + w2 + 1
    c = F(r1, r1 + w1) * F(r2 + 1, n2) + F(w1, r1 + w1) * F(r2, n2)
    return dict(en='Box 1: %d red, %d white; box 2: %d red, %d white. A ball is moved from box 1 to box 2, then a ball is drawn from box 2. \\(P(\\text{red})=\\)…' % (r1, w1, r2, w2), vi='Hộp 1: %d đỏ, %d trắng; hộp 2: %d đỏ, %d trắng. Chuyển 1 bi từ hộp 1 sang hộp 2 rồi lấy 1 bi từ hộp 2. Xác suất lấy được bi đỏ là…' % (r1, w1, r2, w2),
      opts=popts(r, c, [F(r2, r2 + w2), F(r2 + 1, n2), F(r1 + r2, r1 + w1 + r2 + w2), F(r2, n2), 1 - c]), ans=0,
      ee='Condition on the moved ball.', ev='Xét hai trường hợp bi chuyển sang: \\(\\frac{%d}{%d}\\cdot\\frac{%d}{%d}+\\frac{%d}{%d}\\cdot\\frac{%d}{%d}=%s\\).' % (r1, r1 + w1, r2 + 1, n2, w1, r1 + w1, r2, n2, P(c)))
def by_neg(r, lv):
    b = F(r.choice([2, 3, 4, 5]), 10); x, y = F(r.choice([6, 7, 8, 9]), 10), F(r.choice([1, 2, 3]), 10); pna = b * (1 - x) + (1 - b) * (1 - y); c = b * (1 - x) / pna
    return dict(en='\\(P(B)=%s\\), \\(P(A\\mid B)=%s\\), \\(P(A\\mid\\overline B)=%s\\). Then \\(P(B\\mid\\overline A)=\\)…' % (PE(b), PE(x), PE(y)), vi='Cho \\(P(B)=%s\\), \\(P(A\\mid B)=%s\\), \\(P(A\\mid\\overline B)=%s\\). Khi đó \\(P(B\\mid\\overline A)=\\)…' % (P(b), P(x), P(y)),
      opts=popts(r, c, [b * (1 - x), 1 - x, b * x / (b * x + (1 - b) * y), pna, b]), ans=0,
      ee='\\(P(\\overline A)=%s\\).' % PE(pna), ev='\\(P(\\overline A)=P(B)P(\\overline A\\mid B)+P(\\overline B)P(\\overline A\\mid\\overline B)=%s\\), rồi dùng Bayes.' % P(pna))
def tp_class(r, lv):
    n1, n2 = r.choice([(40, 35), (45, 30), (36, 44), (42, 38)]); g1, g2 = r.randint(n1 // 4, n1 // 2), r.randint(n2 // 4, n2 // 2)
    p1, p2 = F(n1, n1 + n2), F(n2, n1 + n2); c = p1 * F(g1, n1) + p2 * F(g2, n2)
    return dict(en='Class A has %d students (%d excellent), class B has %d (%d excellent). A student is picked at random from the two classes. \\(P(\\text{excellent})=\\)…' % (n1, g1, n2, g2), vi='Lớp A có %d học sinh (%d học sinh giỏi), lớp B có %d học sinh (%d giỏi). Chọn ngẫu nhiên một học sinh của hai lớp. Xác suất chọn được học sinh giỏi là…' % (n1, g1, n2, g2),
      opts=popts(r, c, [F(g1, n1) / 2 + F(g2, n2) / 2 if F(g1, n1) / 2 + F(g2, n2) / 2 != c else F(g1, n1), F(g1, n1) * F(g2, n2), F(g1 + g2, n1), F(g1, n1 + n2), F(g2, n1 + n2)]), ans=0,
      ee='\\(\\frac{%d+%d}{%d}\\).' % (g1, g2, n1 + n2), ev='\\(\\frac{%d}{%d}\\cdot\\frac{%d}{%d}+\\frac{%d}{%d}\\cdot\\frac{%d}{%d}=\\frac{%d}{%d}\\).' % (n1, n1 + n2, g1, n1, n2, n1 + n2, g2, n2, g1 + g2, n1 + n2))
def by_quiz(r, lv):
    k = F(r.choice([5, 6, 7, 8]), 10); m = r.choice([4, 5]); pa = k + (1 - k) * F(1, m); c = k / pa
    return dict(en='In a test with %d options per question, a student knows the answer with probability %s; otherwise he guesses. He answered correctly. The probability that he knew the answer is…' % (m, PE(k)), vi='Trong bài trắc nghiệm %d phương án, một học sinh biết đáp án với xác suất %s; nếu không biết thì chọn ngẫu nhiên. Em trả lời đúng. Xác suất em thực sự biết đáp án là…' % (m, P(k)),
      opts=popts(r, c, [k, pa, F(1, m), k * pa, 1 - c]), ans=0, ee='\\(\\dfrac{%s}{%s+%s\\cdot\\frac1{%d}}\\).' % (PE(k), PE(k), PE(1 - k), m), ev='Bayes: \\(\\dfrac{%s}{%s+%s\\cdot\\frac1{%d}}=%s\\).' % (P(k), P(k), P(1 - k), m, P(c)))
M19S12 = [tp_basic, by_basic, tp_fact, by_fact, tp_urn, by_urn, tp_test, by_test, tp_rain, by_spam, tp_move, by_neg, tp_class, by_quiz, tp_basic]
