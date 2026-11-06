# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 10 – Bài 17 (dấu của tam thức bậc hai), Bài 18 (phương trình quy về phương trình bậc hai),
Bài 19 (phương trình đường thẳng). Đáp án tính chính xác bằng số nguyên / Fraction."""
import math
from fractions import Fraction as F
from mb_selfpractice import pick_opts, fr
from sp_g10f import TT, D, poly, iv

def iv2(a, b, lo, hi): return iv(a, b, lo, hi)
def union(p, q, closed):
    """(-∞; p) ∪ (q; +∞) hoặc dạng nửa khoảng."""
    return '(-\\infty;\\,%s%s\\cup%s%s;\\,+\\infty)' % (fr(F(p)), ']' if closed else ')', '[' if closed else '(', fr(F(q)))
def seg(p, q, closed): return '%s%s;\\,%s%s' % ('[' if closed else '(', fr(F(p)), fr(F(q)), ']' if closed else ')')
def _roots(r, lo=-5, hi=6):
    p, q = sorted(r.sample(range(lo, hi), 2)); return p, q
# ================= Bài 17. Dấu của tam thức bậc hai =================
def ts_ineq(r, lv):
    p, q = _roots(r); a = r.choice([1, 2, -1, -2, 3]); cs = [a, -a * (p + q), a * p * q]
    rel = r.choice(['\\gt', '\\lt', '\\ge', '\\le']); closed = rel in ('\\ge', '\\le')
    pos = rel in ('\\gt', '\\ge')
    inside = (pos and a < 0) or (not pos and a > 0)          # nghiệm nằm giữa hai nghiệm?
    ok = seg(p, q, closed) if inside else union(p, q, closed)
    wr = [union(p, q, closed) if inside else seg(p, q, closed), seg(p, q, not closed) if inside else union(p, q, not closed), seg(-q, -p, closed) if p + q else seg(p - 1, q + 1, closed), '\\mathbb R']
    return dict(en='Solve \\(%s%s0\\).' % (poly(cs), rel), vi='Giải bất phương trình \\(%s%s0\\).' % (poly(cs), rel), opts=pick_opts(r, ok, wr), ans=0,
      ee='Roots \\(%d\\), \\(%d\\); \\(a=%d\\): \\(f\\) has the sign of \\(a\\) outside \\([%d;%d]\\).' % (p, q, a, p, q), ev='Hai nghiệm \\(%d\\), \\(%d\\); \\(a=%d\\): \\(f\\) cùng dấu \\(a\\) ở ngoài đoạn \\([%d;%d]\\), trái dấu \\(a\\) ở giữa.' % (p, q, a, p, q))
def ts_sign(r, lv):
    p, q = _roots(r); a = r.choice([1, -1, 2, -3]); cs = [a, -a * (p + q), a * p * q]
    x0 = r.choice([p - 1, q + 1, F(p + q, 2)]); v = a * (x0 - p) * (x0 - q)
    if v == 0: raise AssertionError
    s = 'positive' if v > 0 else 'negative'
    return dict(en='For \\(f(x)=%s\\), the sign of \\(f(%s)\\) is…' % (poly(cs), fr(F(x0))), vi='Với \\(f(x)=%s\\), dấu của \\(f(%s)\\) là…' % (poly(cs), fr(F(x0))),
      opts=[TT('positive', 'dương'), TT('negative', 'âm'), TT('zero', 'bằng 0'), TT('cannot be decided', 'không xác định được')] if v > 0 else [TT('negative', 'âm'), TT('positive', 'dương'), TT('zero', 'bằng 0'), TT('cannot be decided', 'không xác định được')], ans=0,
      ee='\\(f(%s)=%s\\).' % (fr(F(x0)), fr(F(v))), ev='\\(f(%s)=%s\\) nên \\(f(%s)\\) %s.' % (fr(F(x0)), fr(F(v)), fr(F(x0)), 'dương' if v > 0 else 'âm'))
def ts_all(r, lv):
    s = r.choice([1, 2, 3, 4]); k = s * s; extra = r.choice([0, 1, 2])
    # f(x) = x^2 - 2mx + k  >  0 với mọi x  <=>  Δ' = m^2 - k < 0  <=>  -s < m < s
    return dict(en='\\(x^2-2mx+%d\\gt0\\) for every real \\(x\\) exactly when…' % k, vi='\\(x^2-2mx+%d\\gt0\\) với mọi \\(x\\in\\mathbb R\\) khi và chỉ khi…' % k,
      opts=pick_opts(r, '-%d\\lt m\\lt%d' % (s, s), ['m\\in(-\\infty;\\,-%d)\\cup(%d;\\,+\\infty)' % (s, s), '-%d\\le m\\le%d' % (s, s), '0\\lt m\\lt%d' % k, 'm\\lt%d' % s]), ans=0,
      ee='\\(a=1\\gt0\\), need \\(\\Delta\'=m^2-%d\\lt0\\).' % k, ev='\\(a=1\\gt0\\), cần \\(\\Delta\'=m^2-%d\\lt0\\iff-%d\\lt m\\lt%d\\).' % (k, s, s))
def ts_double(r, lv):
    p = r.randint(-4, 4); a = r.choice([1, -1, 4, -4, 9]); cs = [a, -2 * a * p, a * p * p]
    rel = r.choice(['\\gt', '\\ge']) if a > 0 else r.choice(['\\lt', '\\le'])
    ok = '\\mathbb R\\setminus\\{%d\\}' % p if rel in ('\\gt', '\\lt') else '\\mathbb R'
    return dict(en='Solve \\(%s%s0\\).' % (poly(cs), rel), vi='Giải bất phương trình \\(%s%s0\\).' % (poly(cs), rel),
      opts=pick_opts(r, ok, ['\\varnothing', '\\{%d\\}' % p, '\\mathbb R' if ok != '\\mathbb R' else '\\mathbb R\\setminus\\{%d\\}' % p, '(%d;\\,+\\infty)' % p]), ans=0,
      ee='\\(\\Delta=0\\): \\(f(x)=%s(x%+d)^2\\) has the sign of \\(a\\) except at \\(x=%d\\).' % ('' if a == 1 else '-' if a == -1 else a, -p, p), ev='\\(\\Delta=0\\): \\(f(x)\\) cùng dấu \\(a\\) với mọi \\(x\\ne%d\\).' % p)
def ts_count(r, lv):
    p, q = _roots(r, -4, 8)
    if q - p < 2: raise AssertionError
    cs = [1, -(p + q), p * q]; closed = r.random() < .5; n = q - p + 1 if closed else q - p - 1
    return dict(en='How many integers \\(x\\) satisfy \\(%s%s0\\)?' % (poly(cs), '\\le' if closed else '\\lt'), vi='Bất phương trình \\(%s%s0\\) có bao nhiêu nghiệm nguyên?' % (poly(cs), '\\le' if closed else '\\lt'),
      opts=pick_opts(r, str(n), [str(n + 1), str(n + 2), str(n - 1) if n > 1 else str(n + 3), TT('infinitely many', 'vô số')]), ans=0,
      ee='Solution set \\(%s\\).' % seg(p, q, closed), ev='Tập nghiệm \\(%s\\).' % seg(p, q, closed))
def ts_profit(r, lv):
    p, q = _roots(r, 2, 15)
    if q - p < 3: raise AssertionError
    k = r.choice([1, 2]); cs = [-k, k * (p + q), -k * p * q]
    return dict(en='A workshop makes \\(x\\) hundred items a day; its daily profit is \\(L(x)=%s\\) (million VND). It does not make a loss (\\(L\\ge0\\)) when…' % poly(cs),
      vi='Một xưởng sản xuất \\(x\\) trăm sản phẩm mỗi ngày, lợi nhuận \\(L(x)=%s\\) (triệu đồng). Xưởng không bị lỗ (\\(L\\ge0\\)) khi…' % poly(cs),
      opts=pick_opts(r, '%d\\le x\\le%d' % (p, q), ['x\\in[0;\\,%d]\\cup[%d;\\,+\\infty)' % (p, q), '%d\\lt x\\lt%d' % (p, q), '0\\le x\\le%d' % q, 'x\\ge%d' % p]), ans=0,
      ee='Roots %d, %d; \\(a\\lt0\\): \\(L\\ge0\\) between the roots.' % (p, q), ev='Hai nghiệm %d, %d; \\(a\\lt0\\): \\(L\\ge0\\) giữa hai nghiệm.' % (p, q))
def ts_ball(r, lv):
    p, q = r.choice([(1, 3), (1, 2), (2, 3), (1, 4), (2, 4)]); H = r.choice([15, 20, 25]); c = -5 * p * q + H
    if c < 0: raise AssertionError
    cs = [-5, 5 * (p + q), c]
    return dict(en='A ball\'s height is \\(h(t)=%s\\) (m, \\(t\\) in s). It is higher than %d m when…' % (poly(cs, 't'), H), vi='Độ cao quả bóng là \\(h(t)=%s\\) (m, \\(t\\) tính bằng giây). Bóng ở cao hơn %d m khi…' % (poly(cs, 't'), H),
      opts=pick_opts(r, '%s\\lt t\\lt%s' % (fr(F(p)), fr(F(q))), ['t\\in(0;\\,%s)\\cup(%s;\\,+\\infty)' % (fr(F(p)), fr(F(q))), '0\\lt t\\lt%s' % fr(F(q)), '%s\\le t\\le%s' % (fr(F(p)), fr(F(q + 1))), 't\\gt%s' % fr(F(p))]), ans=0,
      ee='\\(h(t)-%d=-5(t-%s)(t-%s)\\gt0\\).' % (H, fr(F(p)), fr(F(q))), ev='\\(h(t)-%d=-5(t-%s)(t-%s)\\gt0\\).' % (H, fr(F(p)), fr(F(q))))
def ts_delta(r, lv):
    a = r.choice([1, 2, -1, -2, 3]); b = r.randint(-4, 4); c = r.randint(-5, 6); d = b * b - 4 * a * c
    return dict(en='The discriminant of \\(%s\\) is…' % poly([a, b, c]), vi='Biệt thức của tam thức \\(%s\\) là…' % poly([a, b, c]),
      opts=pick_opts(r, '\\Delta=%d' % d, ['\\Delta=%d' % (b * b + 4 * a * c), '\\Delta=%d' % (b * b - 2 * a * c), '\\Delta=%d' % (-d) if d else '\\Delta=1', '\\Delta=%d' % (b - 4 * a * c)]), ans=0,
      ee='\\(\\Delta=b^2-4ac=%d-4\\cdot(%d)\\cdot(%d)\\).' % (b * b, a, c), ev='\\(\\Delta=b^2-4ac=%d-4\\cdot(%d)\\cdot(%d)=%d\\).' % (b * b, a, c, d))
M17S10 = [ts_delta, ts_sign, ts_ineq, ts_double, ts_all, ts_count, ts_profit, ts_ball]
# ================= Bài 18. Phương trình quy về phương trình bậc hai =================
def _t2(r):
    """√(ax+b) = x - c có nghiệm đúng r1 ≥ c và nghiệm ngoại lai r2 < c."""
    c = r.randint(-2, 3); r1 = r.randint(c, c + 6); r2 = r.randint(c - 6, c - 1); a = r1 + r2 - 2 * c; b = c * c - r1 * r2
    if a == 0: raise AssertionError
    return c, r1, r2, a, b
def lhs(a, b): return '\\sqrt{%s}' % poly([a, b])
def rhs(c): return 'x' if c == 0 else 'x%+d' % -c
def eq_t2(r, lv):
    c, r1, r2, a, b = _t2(r)
    return dict(en='Solve \\(%s=%s\\).' % (lhs(a, b), rhs(c)), vi='Giải phương trình \\(%s=%s\\).' % (lhs(a, b), rhs(c)),
      opts=pick_opts(r, 'S=\\{%d\\}' % r1, ['S=\\{%d;\\,%d\\}' % (min(r1, r2), max(r1, r2)), 'S=\\{%d\\}' % r2, 'S=\\varnothing', 'S=\\{%d\\}' % (-r1) if r1 else 'S=\\{1\\}']), ans=0,
      ee='Square (with \\(x\\ge%d\\)): roots %d, %d; only \\(x=%d\\) satisfies \\(x\\ge%d\\).' % (c, r1, r2, r1, c), ev='Điều kiện \\(x\\ge%d\\); bình phương được hai nghiệm %d, %d; chỉ \\(x=%d\\) thỏa mãn.' % (c, r1, r2, r1))
def eq_t1(r, lv):
    p, q = _roots(r, -4, 6); m, n = r.choice([1, 2, -1, 3]), r.randint(-4, 6)
    # √(x² + bx + c) = √(mx + n): x² + bx + c = mx + n có nghiệm p, q; giữ nghiệm có mx+n ≥ 0
    b = -(p + q) + m; c = p * q + n
    good = [x for x in (p, q) if m * x + n >= 0]
    if not good or len(good) == 2 and r.random() < .3: pass
    ok = 'S=\\varnothing' if not good else 'S=\\{%s\\}' % ';\\,'.join(str(x) for x in good)
    allr = 'S=\\{%d;\\,%d\\}' % (p, q)
    wr = [allr if ok != allr else 'S=\\{%d\\}' % p, 'S=\\{%d\\}' % (-p if -p not in (p, q) else 7), 'S=\\varnothing' if good else 'S=\\{%d\\}' % q, 'S=\\{%d\\}' % (q + 1)]
    return dict(en='Solve \\(\\sqrt{%s}=\\sqrt{%s}\\).' % (poly([1, b, c]), poly([m, n])), vi='Giải phương trình \\(\\sqrt{%s}=\\sqrt{%s}\\).' % (poly([1, b, c]), poly([m, n])),
      opts=pick_opts(r, ok, wr), ans=0,
      ee='Square: \\(%s=0\\), roots %d, %d; keep those with \\(%s\\ge0\\).' % (poly([1, b - m, c - n]), p, q, poly([m, n])), ev='Bình phương: \\(%s=0\\), nghiệm %d, %d; giữ nghiệm thỏa \\(%s\\ge0\\).' % (poly([1, b - m, c - n]), p, q, poly([m, n])))
def eq_bi(r, lv):
    u, v = r.sample([0, 1, 4, 9, 16, -1, -4], 2); cs = [1, 0, -(u + v), 0, u * v]
    n = sum(1 if t == 0 else 2 if t > 0 else 0 for t in (u, v))
    return dict(en='How many real roots does \\(%s=0\\) have?' % poly(cs), vi='Phương trình \\(%s=0\\) có bao nhiêu nghiệm thực?' % poly(cs),
      opts=pick_opts(r, str(n), [str(k) for k in range(5) if k != n]), ans=0,
      ee='Put \\(t=x^2\\ge0\\): \\(t=%d\\) or \\(t=%d\\).' % (u, v), ev='Đặt \\(t=x^2\\ge0\\): \\(t=%d\\) hoặc \\(t=%d\\); mỗi \\(t\\gt0\\) cho 2 nghiệm, \\(t=0\\) cho 1 nghiệm.' % (u, v))
def eq_extra(r, lv):
    c, r1, r2, a, b = _t2(r)
    return dict(en='After squaring \\(%s=%s\\) we get the roots %d and %d. Which is extraneous?' % (lhs(a, b), rhs(c), min(r1, r2), max(r1, r2)), vi='Bình phương hai vế phương trình \\(%s=%s\\) được hai nghiệm %d và %d. Nghiệm nào là nghiệm ngoại lai?' % (lhs(a, b), rhs(c), min(r1, r2), max(r1, r2)),
      opts=[TT('\\(x=%d\\)' % r2, '\\(x=%d\\)' % r2), TT('\\(x=%d\\)' % r1, '\\(x=%d\\)' % r1), TT('both', 'cả hai'), TT('neither', 'không có')], ans=0,
      ee='At \\(x=%d\\) the right side is \\(%d\\lt0\\).' % (r2, r2 - c), ev='Tại \\(x=%d\\) vế phải bằng \\(%d\\lt0\\).' % (r2, r2 - c))
def eq_sum(r, lv):
    c, r1, r2, a, b = _t2(r)
    return dict(en='The sum of all solutions of \\(%s=%s\\) is…' % (lhs(a, b), rhs(c)), vi='Tổng các nghiệm của phương trình \\(%s=%s\\) là…' % (lhs(a, b), rhs(c)),
      opts=pick_opts(r, str(r1), [str(r1 + r2), str(r2), str(r1 - r2), str(r1 + 1)]), ans=0,
      ee='Only \\(x=%d\\) is a solution.' % r1, ev='Phương trình chỉ có nghiệm \\(x=%d\\) (loại \\(x=%d\\)).' % (r1, r2))
def MM(x, y): return TT('%d m and %d m' % (x, y), '%d m và %d m' % (x, y))
TRIPLES = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15), (12, 16, 20), (7, 24, 25)]
def eq_rect(r, lv):
    a, b, c = r.choice(TRIPLES)
    return dict(en='A rectangle has perimeter \\(%d\\) m and diagonal \\(%d\\) m. Its sides are…' % (2 * (a + b), c), vi='Một hình chữ nhật có chu vi \\(%d\\) m và đường chéo \\(%d\\) m. Hai cạnh là…' % (2 * (a + b), c),
      opts=pick_opts(r, MM(a, b), [MM(a - 1, b + 1), MM(a + 1, b - 1), MM(a + 2, b - 2), MM(a, c)]), ans=0,
      ee='\\(x+y=%d\\), \\(x^2+y^2=%d\\Rightarrow x^2-%dx+%d=0\\).' % (a + b, c * c, a + b, a * b), ev='\\(x+y=%d\\), \\(x^2+y^2=%d\\Rightarrow x^2-%dx+%d=0\\).' % (a + b, c * c, a + b, a * b))
def eq_ladder(r, lv):
    a, b, c = r.choice(TRIPLES[:5]); d = r.choice([1, 2])
    # thang dài c, chân cách tường a; kéo chân ra thêm? -> dùng √(c² - x²) = b
    return dict(en='A %d m ladder leans on a wall; its foot is \\(x\\) m from the wall and its top is \\(\\sqrt{%d-x^2}\\) m high. The top is at \\(%d\\) m when \\(x=\\)…' % (c, c * c, b), vi='Một chiếc thang dài %d m dựa vào tường; chân thang cách tường \\(x\\) m, đỉnh thang cao \\(\\sqrt{%d-x^2}\\) m. Đỉnh thang ở độ cao %d m khi \\(x=\\)…' % (c, c * c, b),
      opts=pick_opts(r, '%d\\text{ m}' % a, ['%d\\text{ m}' % (c - b), '%d\\text{ m}' % (a + d), '%d\\text{ m}' % (c - a), '%d\\text{ m}' % b]), ans=0,
      ee='\\(%d-x^2=%d\\Rightarrow x^2=%d\\), \\(x\\gt0\\).' % (c * c, b * b, a * a), ev='\\(%d-x^2=%d\\Rightarrow x^2=%d\\), \\(x\\gt0\\Rightarrow x=%d\\).' % (c * c, b * b, a * a, a))
M18S10 = [eq_t2, eq_t1, eq_bi, eq_extra, eq_sum, eq_rect, eq_ladder, eq_t2]
# ================= Bài 19. Phương trình đường thẳng =================
def norm3(a, b, c):
    g = math.gcd(math.gcd(abs(a), abs(b)), abs(c)) or 1; a, b, c = a // g, b // g, c // g
    if a < 0 or (a == 0 and b < 0): a, b, c = -a, -b, -c
    return a, b, c
def leq(a, b, c):
    s = ''
    for k, v in ((a, 'x'), (b, 'y')):
        if k == 0: continue
        s += ('-' if k < 0 else ('+' if s else '')) + ('' if abs(k) == 1 else str(abs(k))) + v
    if c: s += '%+d' % c
    return s + '=0'
def V2(v): return '(%s;\\,%s)' % (fr(F(v[0])), fr(F(v[1])))
def _pt(r): return (r.randint(-4, 5), r.randint(-4, 5))
def _vec(r):
    v = (r.randint(-3, 3), r.randint(-3, 3))
    if v == (0, 0) or math.gcd(abs(v[0]), abs(v[1])) != 1: raise AssertionError
    return v
def l_normal(r, lv):
    a, b = _vec(r); c = r.randint(-6, 6); k = r.choice([1, 2, -1, -2])
    return dict(en='A normal vector of \\(%s\\) is…' % leq(a, b, c), vi='Một vectơ pháp tuyến của đường thẳng \\(%s\\) là…' % leq(a, b, c),
      opts=pick_opts(r, '\\vec n=%s' % V2((k * a, k * b)), ['\\vec n=%s' % V2((b, -a)), '\\vec n=%s' % V2((a, c)) if (a, c) != (a, b) else '\\vec n=%s' % V2((a, b + 1)), '\\vec n=%s' % V2((-b, a)), '\\vec n=%s' % V2((a, -b)) if b else '\\vec n=%s' % V2((a + 1, 1))]), ans=0,
      ee='\\(ax+by+c=0\\) has normal vector \\((a;b)=%s\\) (or a non-zero multiple).' % V2((a, b)), ev='\\(ax+by+c=0\\) có vectơ pháp tuyến \\((a;b)=%s\\) (hoặc bội khác 0).' % V2((a, b)))
def l_dir(r, lv):
    a, b = _vec(r); c = r.randint(-6, 6)
    return dict(en='A direction vector of \\(%s\\) is…' % leq(a, b, c), vi='Một vectơ chỉ phương của đường thẳng \\(%s\\) là…' % leq(a, b, c),
      opts=pick_opts(r, '\\vec u=%s' % V2((b, -a)), ['\\vec u=%s' % V2((a, b)), '\\vec u=%s' % V2((b, a)) if (b, a) != (-b, a) else '\\vec u=%s' % V2((b + 1, a)), '\\vec u=%s' % V2((a, -b)), '\\vec u=%s' % V2((a + b, 1))]), ans=0,
      ee='\\(\\vec u=(b;-a)\\perp\\vec n=(a;b)\\).', ev='\\(\\vec u=(b;-a)\\) vuông góc với \\(\\vec n=(a;b)\\).')
def l_two(r, lv):
    A, B = _pt(r), _pt(r)
    if A == B: raise AssertionError
    u = (B[0] - A[0], B[1] - A[1]); a, b = u[1], -u[0]; c = -(a * A[0] + b * A[1]); a, b, c = norm3(a, b, c)
    w = [leq(*norm3(u[0], u[1], -(u[0] * A[0] + u[1] * A[1]))) if u[0] or u[1] else '', leq(*norm3(a, b, -c)) if c else leq(*norm3(a, -b, c)), leq(*norm3(a, b, c + 1)), leq(*norm3(b, a, c)) if (a, b) != (b, a) else leq(*norm3(a, b + 1, c))]
    return dict(en='The line through \\(A%s\\) and \\(B%s\\) is…' % (V2(A), V2(B)), vi='Đường thẳng đi qua \\(A%s\\) và \\(B%s\\) có phương trình…' % (V2(A), V2(B)),
      opts=pick_opts(r, leq(a, b, c), [x for x in w if x]), ans=0,
      ee='\\(\\overrightarrow{AB}=%s\\Rightarrow\\vec n=%s\\).' % (V2(u), V2((u[1], -u[0]))), ev='\\(\\overrightarrow{AB}=%s\\Rightarrow\\vec n=%s\\), thay \\(A\\) để tìm hệ số tự do.' % (V2(u), V2((u[1], -u[0]))))
def l_pn(r, lv):
    M = _pt(r); n = _vec(r); c = -(n[0] * M[0] + n[1] * M[1]); a, b, c = norm3(n[0], n[1], c)
    return dict(en='The line through \\(M%s\\) with normal vector \\(\\vec n=%s\\) is…' % (V2(M), V2(n)), vi='Đường thẳng đi qua \\(M%s\\) và có vectơ pháp tuyến \\(\\vec n=%s\\) là…' % (V2(M), V2(n)),
      opts=pick_opts(r, leq(a, b, c), [leq(*norm3(n[0], n[1], -c)) if c else leq(*norm3(n[0], n[1], 1)), leq(*norm3(M[0], M[1], -(M[0] * n[0] + M[1] * n[1]))) if any(M) else leq(1, 1, 1), leq(*norm3(n[1], -n[0], c)), leq(*norm3(n[0], n[1], c + 2))]), ans=0,
      ee='\\(%d(x%+d)%+d(y%+d)=0\\).' % (n[0], -M[0], n[1], -M[1]), ev='\\(%d(x%+d)%+d(y%+d)=0\\).' % (n[0], -M[0], n[1], -M[1]))
def l_slope(r, lv):
    A, B = _pt(r), _pt(r)
    if A[0] == B[0] or A[1] == B[1]: raise AssertionError
    k = F(B[1] - A[1], B[0] - A[0])
    return dict(en='The slope of the line through \\(A%s\\) and \\(B%s\\) is…' % (V2(A), V2(B)), vi='Hệ số góc của đường thẳng đi qua \\(A%s\\) và \\(B%s\\) là…' % (V2(A), V2(B)),
      opts=pick_opts(r, fr(k), [fr(1 / k), fr(-k), fr(-1 / k), fr(k + 1)]), ans=0,
      ee='\\(k=\\dfrac{y_B-y_A}{x_B-x_A}=%s\\).' % fr(k), ev='\\(k=\\dfrac{y_B-y_A}{x_B-x_A}=%s\\).' % fr(k))
def pr2(M, u):
    def one(m, a, v):
        if a == 0: return '%s=%d' % (v, m)
        t = ('' if abs(a) == 1 else str(abs(a))) + 't'
        return '%s=%s' % (v, (('-' if a < 0 else '') + t) if m == 0 else '%d%s%s' % (m, '+' if a > 0 else '-', t))
    return '\\begin{cases}%s\\\\%s\\end{cases}' % (one(M[0], u[0], 'x'), one(M[1], u[1], 'y'))
def l_par(r, lv):
    M = _pt(r); u = _vec(r)
    if not all(u) or M == u: raise AssertionError
    return dict(en='The line through \\(M%s\\) with direction vector \\(\\vec u=%s\\) has parametric equations…' % (V2(M), V2(u)), vi='Đường thẳng đi qua \\(M%s\\), có vectơ chỉ phương \\(\\vec u=%s\\) có phương trình tham số…' % (V2(M), V2(u)),
      opts=pick_opts(r, pr2(M, u), [pr2(u, M), pr2((-M[0], -M[1]), u) if any(M) else pr2(M, (u[0], -u[1])), pr2(M, (u[1], u[0])) if u[0] != u[1] else pr2(M, (u[0], -u[1])), pr2(M, (-u[1], u[0]))]), ans=0,
      ee='\\(x=x_0+at\\), \\(y=y_0+bt\\).', ev='\\(x=x_0+at\\), \\(y=y_0+bt\\) với \\(M(x_0;y_0)\\), \\(\\vec u=(a;b)\\).')
def l_on(r, lv):
    a, b = _vec(r); P = _pt(r); c = -(a * P[0] + b * P[1]); others = []
    for _ in range(50):
        Q = (P[0] + r.randint(-2, 2), P[1] + r.randint(-2, 2))
        if a * Q[0] + b * Q[1] + c != 0 and V2(Q) not in others: others.append(V2(Q))
    return dict(en='Which point lies on \\(%s\\)?' % leq(a, b, c), vi='Điểm nào thuộc đường thẳng \\(%s\\)?' % leq(a, b, c), opts=pick_opts(r, V2(P), others[:4]), ans=0,
      ee='Substitute: \\(%d\\cdot(%d)%+d\\cdot(%d)%+d=0\\).' % (a, P[0], b, P[1], c), ev='Thay tọa độ: \\(%d\\cdot(%d)%+d\\cdot(%d)%+d=0\\).' % (a, P[0], b, P[1], c))
def l_axes(r, lv):
    p, q = r.choice([-4, -3, -2, 2, 3, 4, 5, 6]), r.choice([-4, -3, -2, 2, 3, 4, 6])
    if abs(p) == abs(q): raise AssertionError
    a, b, c = norm3(q, p, -p * q)
    return dict(en='The line cutting \\(Ox\\) at \\(A(%d;0)\\) and \\(Oy\\) at \\(B(0;%d)\\) is…' % (p, q), vi='Đường thẳng cắt \\(Ox\\) tại \\(A(%d;0)\\) và \\(Oy\\) tại \\(B(0;%d)\\) có phương trình…' % (p, q),
      opts=pick_opts(r, leq(a, b, c), [leq(*norm3(p, q, -p * q)), leq(*norm3(q, p, p * q)), leq(*norm3(q, -p, -p * q)), leq(*norm3(1, 1, -(p + q))) if p + q else leq(1, 1, 1)]), ans=0,
      ee='\\(\\dfrac{x}{%d}+\\dfrac{y}{%d}=1\\).' % (p, q), ev='Phương trình đoạn chắn \\(\\dfrac{x}{%d}+\\dfrac{y}{%d}=1\\).' % (p, q))
M19S10 = [l_normal, l_dir, l_two, l_pn, l_slope, l_par, l_on, l_axes]
