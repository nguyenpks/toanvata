# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 12 – Chương I (đạo hàm). Đáp án tính bằng số học chính xác và đối chiếu bằng tính số."""
import math
from fractions import Fraction as F
from mb_selfpractice import *

def _ev(c, x):
    v = F(0)
    for a in c: v = v * x + a
    return v
def _num_ext(f, lo, hi, n=20000):
    xs = [lo + (hi - lo) * i / n for i in range(n + 1)]; ys = [f(x) for x in xs]; return min(ys), max(ys)

# ---------- Bài 1: đơn điệu và cực trị ----------
def m1_dec(r, lv):
    R = 2 + lv
    while True:
        a = r.randint(-R, R - 1); b = r.randint(a + 1, R + 1)
        if (a + b) % 2 == 0 and a != b: break
    c = [1, -3 * (a + b) // 2, 3 * a * b, 0]; f = poly(c)
    fp = lambda x: 3 * (x - a) * (x - b); assert fp((a + b) / 2) < 0 and fp(a - 1) > 0 and fp(b + 1) > 0
    ints = ['(%d,%d)' % (a, b), '(-\\infty,%d)' % a, '(%d,+\\infty)' % b, '(%d,+\\infty)' % a]
    return dict(en='On which interval is \\(f(x)=%s\\) decreasing?' % f, vi='Hàm số \\(f(x)=%s\\) nghịch biến trên khoảng nào?' % f, opts=ints, ans=0,
      ee='\\(f\'(x)=3(x%+d)(x%+d)<0\\) exactly when \\(%d<x<%d\\).' % (-a, -b, a, b), ev='\\(f\'(x)=3(x%+d)(x%+d)<0\\) đúng khi \\(%d<x<%d\\).' % (-a, -b, a, b))

def m1_count(r, lv):
    roots = sorted(r.sample(range(-4, 5), 3)); ex = [r.choice([1, 1, 2, 3]) for _ in roots]
    cnt = sum(1 for e in ex if e % 2 == 1)
    if cnt == 0: ex[0] = 1; cnt = 1
    g = ''.join(xm(a) + ('' if e == 1 else '^%d' % e) for a, e in zip(roots, ex))
    others = [x for x in range(0, 5) if x != cnt]; r.shuffle(others)
    return dict(en='Let \\(f\'(x)=%s\\). How many extreme points does \\(f\\) have?' % g, vi='Cho \\(f\'(x)=%s\\). Hàm số \\(f\\) có bao nhiêu điểm cực trị?' % g,
      opts=[str(cnt)] + [str(x) for x in others[:3]], ans=0,
      ee='\\(f\'\\) changes sign only at roots of odd multiplicity: there are %d of them.' % cnt, ev='\\(f\'\\) chỉ đổi dấu tại các nghiệm bội lẻ: có %d nghiệm như vậy.' % cnt)

def m1_extval(r, lv):
    k = r.randint(1, 2 + lv); kind = r.choice(['min', 'max']); f = 'x^3-%dx' % (3 * k * k)
    fx = lambda x: x ** 3 - 3 * k * k * x; lo, hi = _num_ext(fx, 0, 2 * k)
    val = -2 * k ** 3 if kind == 'min' else 2 * k ** 3
    assert abs((lo if kind == 'min' else hi if False else (fx(-k) if kind == 'max' else fx(k))) - val) < 1e-9
    nm = 'minimum' if kind == 'min' else 'maximum'; nv = 'cực tiểu' if kind == 'min' else 'cực đại'; xx = k if kind == 'min' else -k
    return dict(en='Find the local %s value of \\(f(x)=%s\\).' % (nm, f), vi='Tìm giá trị %s của hàm số \\(f(x)=%s\\).' % (nv, f),
      opts=[str(-2 * k ** 3), str(2 * k ** 3), str(-k ** 3), str(k ** 3)] if kind == 'min' else [str(2 * k ** 3), str(-2 * k ** 3), str(k ** 3), str(-k ** 3)], ans=0,
      ee='\\(f\'(x)=3x^2-%d=0\\) at \\(x=\\pm%d\\). At \\(x=%d\\): \\(f(%d)=%d\\).' % (3 * k * k, k, xx, xx, val), ev='\\(f\'(x)=3x^2-%d=0\\) tại \\(x=\\pm%d\\). Tại \\(x=%d\\): \\(f(%d)=%d\\).' % (3 * k * k, k, xx, xx, val))

def m1_param(r, lv):
    a = r.randint(2, 4 + 2 * lv); c = -(-a * a // 3)      # ceil(a^2/3)
    assert 3 * c >= a * a and 3 * (c - 1) < a * a
    f = 'x^3+%dx^2+mx' % a
    return dict(en='Find the smallest integer \\(m\\) such that \\(f(x)=%s\\) is increasing on \\(\\mathbb{R}\\).' % f, vi='Tìm số nguyên \\(m\\) nhỏ nhất để \\(f(x)=%s\\) đồng biến trên \\(\\mathbb{R}\\).' % f,
      opts=[str(c - 1), str(c), str(c + 1), str(c + 2)], ans=1,
      ee='\\(f\'(x)=3x^2+%dx+m\\ge0\\) for all \\(x\\) needs \\(\\Delta\'=%d-3m\\le0\\), so \\(m\\ge\\dfrac{%d}{3}\\). The smallest integer is %d.' % (2 * a, a * a, a * a, c),
      ev='\\(f\'(x)=3x^2+%dx+m\\ge0\\) với mọi \\(x\\) cần \\(\\Delta\'=%d-3m\\le0\\), nên \\(m\\ge\\dfrac{%d}{3}\\). Số nguyên nhỏ nhất là %d.' % (2 * a, a * a, a * a, c))

def m1_sign(r, lv):
    a = r.randint(-4, 1); b = a + r.randint(1, 4); k = r.randint(1, 3); neg = r.choice([True, False])
    g = ('-' if neg else '') + ('' if k == 1 else str(k)) + xm(a) + xm(b)
    ints = ['(%d,%d)' % (a, b), '(-\\infty,%d)\\cup(%d,+\\infty)' % (a, b), '(-\\infty,%d)' % a, '(%d,+\\infty)' % b]
    # f' > 0 trong (a,b) nếu neg, ngoài [a,b] nếu không neg
    ans = 0 if neg else 1
    return dict(en='Let \\(f\'(x)=%s\\). Where is \\(f\\) increasing?' % g, vi='Cho \\(f\'(x)=%s\\). Hàm số \\(f\\) đồng biến ở đâu?' % g, opts=ints, ans=ans,
      ee='%s' % ('The leading coefficient of \\(f\'\\) is negative, so \\(f\'>0\\) between the roots: \\((%d,%d)\\).' % (a, b) if neg else 'The leading coefficient of \\(f\'\\) is positive, so \\(f\'>0\\) outside the roots.'),
      ev='%s' % ('Hệ số cao nhất của \\(f\'\\) âm nên \\(f\'>0\\) giữa hai nghiệm: \\((%d,%d)\\).' % (a, b) if neg else 'Hệ số cao nhất của \\(f\'\\) dương nên \\(f\'>0\\) ngoài hai nghiệm.'))

def m1_inv(r, lv):
    a = r.randint(2, 3 + lv); k = r.randint(2, 4); f = '%dx+\\dfrac{%d}{x}' % (a, a * k * k); val = 2 * a * k
    lo, _ = _num_ext(lambda x: a * x + a * k * k / x, 0.01, 4 * k, 40000); assert abs(lo - val) < 1e-3
    return dict(en='Find the minimum value of \\(f(x)=%s\\) for \\(x>0\\).' % f, vi='Tìm giá trị nhỏ nhất của \\(f(x)=%s\\) với \\(x>0\\).' % f,
      opts=[str(val), str(a * k), str(2 * val), str(a * k * k)], ans=0,
      ee='\\(f\'(x)=%d-\\dfrac{%d}{x^2}=0\\) at \\(x=%d\\), and \\(f(%d)=%d\\).' % (a, a * k * k, k, k, val), ev='\\(f\'(x)=%d-\\dfrac{%d}{x^2}=0\\) tại \\(x=%d\\) và \\(f(%d)=%d\\).' % (a, a * k * k, k, k, val))

M1 = [m1_dec, m1_count, m1_extval, m1_param, m1_sign, m1_inv, m1_dec, m1_extval]

# ---------- Bài 2: giá trị lớn nhất, nhỏ nhất ----------
def _opts_from(r, correct, cands, d=(1, -1, 2, -2, 3)):
    return pick_opts(r, str_(correct), [str_(c) for c in cands if c != correct], lambda k: str_(correct + d[k % len(d)] * (1 + k // len(d))))
def str_(v): return fr(v)

def m2_cubic(r, lv):
    p = r.randint(1, 1 + lv); q = r.choice([-5, -3, -1, 2, 4, 6]); a = r.choice([-2, -1]); b = 2 * p + r.randint(1, 2)
    f = lambda x: x ** 3 - 3 * p * x ** 2 + q; kind = r.choice(['max', 'min'])
    cands = [f(a), f(b), f(0), f(2 * p)]; val = max(cands) if kind == 'max' else min(cands)
    lo, hi = _num_ext(lambda x: float(f(F(x).limit_denominator(10 ** 6))), a, b, 4000); assert abs((hi if kind == 'max' else lo) - val) < 1e-2
    ex = 'x^3-%dx^2%+d' % (3 * p, q)
    return dict(en='Find the %s value of \\(f(x)=%s\\) on \\([%d,%d]\\).' % ('greatest' if kind == 'max' else 'smallest', ex, a, b),
      vi='Tìm giá trị %s của hàm số \\(f(x)=%s\\) trên đoạn \\([%d,%d]\\).' % ('lớn nhất' if kind == 'max' else 'nhỏ nhất', ex, a, b), opts=_opts_from(r, val, cands), ans=0,
      ee='\\(f\'(x)=3x(x-%d)\\). Compare \\(f(%d)=%d\\), \\(f(0)=%d\\), \\(f(%d)=%d\\), \\(f(%d)=%d\\).' % (2 * p, a, f(a), f(0), 2 * p, f(2 * p), b, f(b)),
      ev='\\(f\'(x)=3x(x-%d)\\). So sánh \\(f(%d)=%d\\), \\(f(0)=%d\\), \\(f(%d)=%d\\), \\(f(%d)=%d\\).' % (2 * p, a, f(a), f(0), 2 * p, f(2 * p), b, f(b)))

def m2_quad(r, lv):
    p = r.randint(-2, 4); q = r.randint(-4, 6); a = r.randint(-3, 2); b = a + r.randint(2, 4); kind = r.choice(['max', 'min'])
    f = lambda x: x * x - 2 * p * x + q; cands = [f(a), f(b)] + ([f(p)] if a <= p <= b else [])
    val = max(cands) if kind == 'max' else min(cands)
    lo, hi = _num_ext(lambda x: float(f(F(x).limit_denominator(10 ** 6))), a, b, 4000); assert abs((hi if kind == 'max' else lo) - val) < 1e-2
    ex = 'x^2%s%+d' % ('-%dx' % (2 * p) if p > 0 else '+%dx' % (-2 * p) if p < 0 else '', q)
    return dict(en='Find the %s value of \\(f(x)=%s\\) on \\([%d,%d]\\).' % ('greatest' if kind == 'max' else 'smallest', ex, a, b),
      vi='Tìm giá trị %s của \\(f(x)=%s\\) trên đoạn \\([%d,%d]\\).' % ('lớn nhất' if kind == 'max' else 'nhỏ nhất', ex, a, b), opts=_opts_from(r, val, [f(a), f(b), f(p)]), ans=0,
      ee='The vertex is at \\(x=%d\\). Compare the values at the endpoints%s: \\(f(%d)=%d\\), \\(f(%d)=%d\\).' % (p, ' and at the vertex' if a <= p <= b else ' (the vertex is outside the interval)', a, f(a), b, f(b)),
      ev='Đỉnh có hoành độ \\(x=%d\\). So sánh giá trị ở hai đầu mút%s: \\(f(%d)=%d\\), \\(f(%d)=%d\\).' % (p, ' và tại đỉnh' if a <= p <= b else ' (đỉnh nằm ngoài đoạn)', a, f(a), b, f(b)))

def m2_fence(r, lv):
    P = r.choice([24, 32, 40, 48, 60, 80, 100, 120, 160][:4 + 2 * lv]); s = P // 4
    return dict(en='A farmer has %d m of fence and makes a rectangular garden. What is the greatest possible area (in \\(\\text{m}^2\\))?' % P,
      vi='Một người nông dân có %d m hàng rào để rào một mảnh vườn hình chữ nhật. Diện tích lớn nhất có thể là bao nhiêu (đơn vị \\(\\text{m}^2\\))?' % P,
      opts=[str(s * s), str(2 * s * s), str(4 * s * s), str(s * s - s)], ans=0,
      ee='Sides \\(x\\) and \\(%d-x\\); area \\(S=x(%d-x)\\) is largest at \\(x=%d\\): \\(S=%d\\).' % (P // 2, P // 2, s, s * s), ev='Hai cạnh \\(x\\) và \\(%d-x\\); diện tích \\(S=x(%d-x)\\) lớn nhất tại \\(x=%d\\): \\(S=%d\\).' % (P // 2, P // 2, s, s * s))

def m2_box(r, lv):
    m = r.choice([1, 2, 3, 4, 5, 6][:2 + 2 * lv]); L = 6 * m
    _, hi = _num_ext(lambda x: x * (L - 2 * x) ** 2, 0, L / 2); assert abs(hi - 16 * m ** 3) < 1e-3
    return dict(en='From a square sheet of side %d cm, we cut a square of side \\(x\\) from each corner and fold to make an open box. What is the greatest volume (in \\(\\text{cm}^3\\))?' % L,
      vi='Từ một tấm bìa hình vuông cạnh %d cm, cắt bỏ bốn hình vuông cạnh \\(x\\) ở bốn góc rồi gập thành hộp không nắp. Thể tích lớn nhất là bao nhiêu (đơn vị \\(\\text{cm}^3\\))?' % L,
      opts=[str(16 * m ** 3), str(8 * m ** 3), str(32 * m ** 3), str(4 * m ** 3)], ans=0,
      ee='\\(V(x)=x(%d-2x)^2\\), \\(V\'(x)=0\\) at \\(x=%d\\), and \\(V(%d)=%d\\).' % (L, m, m, 16 * m ** 3), ev='\\(V(x)=x(%d-2x)^2\\), \\(V\'(x)=0\\) tại \\(x=%d\\) và \\(V(%d)=%d\\).' % (L, m, m, 16 * m ** 3))

def m2_inv(r, lv):
    k = r.randint(2, 4); a = r.randint(1, k - 1); b = k + r.randint(1, 3); kind = r.choice(['max', 'min'])
    f = lambda x: x + F(k * k) / x; cands = [f(a), f(b), f(k)]; val = max(f(a), f(b)) if kind == 'max' else 2 * k
    return dict(en='Find the %s value of \\(f(x)=x+\\dfrac{%d}{x}\\) on \\([%d,%d]\\).' % ('greatest' if kind == 'max' else 'smallest', k * k, a, b),
      vi='Tìm giá trị %s của \\(f(x)=x+\\dfrac{%d}{x}\\) trên đoạn \\([%d,%d]\\).' % ('lớn nhất' if kind == 'max' else 'nhỏ nhất', k * k, a, b), opts=_opts_from(r, val, cands), ans=0,
      ee='\\(f\'(x)=1-\\dfrac{%d}{x^2}=0\\) at \\(x=%d\\in[%d,%d]\\). \\(f(%d)=%s\\), \\(f(%d)=%s\\), \\(f(%d)=%d\\).' % (k * k, k, a, b, a, fr(f(a)), b, fr(f(b)), k, 2 * k),
      ev='\\(f\'(x)=1-\\dfrac{%d}{x^2}=0\\) tại \\(x=%d\\in[%d,%d]\\). \\(f(%d)=%s\\), \\(f(%d)=%s\\), \\(f(%d)=%d\\).' % (k * k, k, a, b, a, fr(f(a)), b, fr(f(b)), k, 2 * k))

def m2_sqrt(r, lv):
    k = r.randint(3, 9); kind = r.choice(['max', 'min']); f = '\\sqrt{%d-x^2}' % (k * k)
    return dict(en='Find the %s value of \\(f(x)=%s\\) on its domain.' % ('greatest' if kind == 'max' else 'smallest', f), vi='Tìm giá trị %s của \\(f(x)=%s\\) trên tập xác định.' % ('lớn nhất' if kind == 'max' else 'nhỏ nhất', f),
      opts=[str(k), str(k * k), str(2 * k), '0'] if kind == 'max' else ['0', str(k), str(-k), str(k * k)], ans=0,
      ee='The domain is \\([-%d,%d]\\). \\(0\\le%d-x^2\\le%d\\), so %s.' % (k, k, k * k, k * k, ('the greatest value is %d at \\(x=0\\)' % k) if kind == 'max' else 'the smallest value is 0 at \\(x=\\pm%d\\)' % k),
      ev='Tập xác định là \\([-%d,%d]\\). \\(0\\le%d-x^2\\le%d\\), nên %s.' % (k, k, k * k, k * k, ('giá trị lớn nhất là %d tại \\(x=0\\)' % k) if kind == 'max' else 'giá trị nhỏ nhất là 0 tại \\(x=\\pm%d\\)' % k))

M2 = [m2_cubic, m2_quad, m2_fence, m2_box, m2_inv, m2_sqrt, m2_cubic, m2_quad]

# ---------- Bài 3: đường tiệm cận ----------
def m3_mobius(r, lv):
    while True:
        a = r.choice([1, 2, 3, -1, -2, 4]); b = r.randint(-4, 4); c = r.choice([1, 1, 2, 3]); d = r.choice([-3, -2, -1, 1, 2, 3, 4])
        if a * d - b * c != 0 and (a, c) != (d, c): break
    x0 = F(-d, c); y0 = F(a, c); f = lambda x: (a * x + b) / (c * x + d)
    assert abs(f(1e7) - float(y0)) < 1e-4 and abs(f(-1e7) - float(y0)) < 1e-4 and abs(f(float(x0) + 1e-9)) > 1e6
    t = lambda x, y: 'x=%s,\\ y=%s' % (fr(x), fr(y))
    ex = '\\dfrac{%s}{%s}' % (lin(a, b), lin(c, d))
    return dict(en='Find the vertical and horizontal asymptotes of \\(y=%s\\).' % ex, vi='Tìm tiệm cận đứng và tiệm cận ngang của đồ thị \\(y=%s\\).' % ex,
      opts=pick_opts(r, t(x0, y0), [t(-x0, y0), t(y0, x0), t(x0, -y0), t(-x0, -y0), t(y0, -x0)], lambda k: t(x0 + k, y0)), ans=0,
      ee='Vertical: \\(%s=0\\) gives \\(x=%s\\). Horizontal: \\(\\lim_{x\\to\\infty}y=\\dfrac{%d}{%d}=%s\\).' % (lin(c, d), fr(x0), a, c, fr(y0)),
      ev='Tiệm cận đứng: \\(%s=0\\) cho \\(x=%s\\). Tiệm cận ngang: \\(\\lim_{x\\to\\infty}y=\\dfrac{%d}{%d}=%s\\).' % (lin(c, d), fr(x0), a, c, fr(y0)))

def m3_count(r, lv):
    q = r.randint(1, 3); p = r.choice([x for x in range(-4, 5) if x not in (0,)])
    VA = {q, -q}; num_root = -p; VA.discard(num_root) if num_root in VA else None
    cnt = len(VA) + 1
    ex = '\\dfrac{x%+d}{x^2-%d}' % (p, q * q)
    others = [x for x in range(1, 5) if x != cnt]
    return dict(en='How many asymptotes (vertical and horizontal) does the graph of \\(y=%s\\) have?' % ex, vi='Đồ thị hàm số \\(y=%s\\) có tất cả bao nhiêu đường tiệm cận (đứng và ngang)?' % ex,
      opts=[str(cnt)] + [str(x) for x in others[:3]], ans=0,
      ee='The denominator is zero at \\(x=\\pm%d\\)%s: %d vertical asymptote(s). Since \\(\\deg\\) numerator < \\(\\deg\\) denominator, \\(y=0\\) is a horizontal asymptote. Total: %d.' % (q, ' (the factor \\(x%+d\\) cancels one of them)' % p if num_root in (q, -q) else '', len(VA), cnt),
      ev='Mẫu bằng 0 tại \\(x=\\pm%d\\)%s: có %d tiệm cận đứng. Vì bậc tử nhỏ hơn bậc mẫu nên \\(y=0\\) là tiệm cận ngang. Tổng cộng: %d.' % (q, ' (thừa số \\(x%+d\\) triệt tiêu một nghiệm)' % p if num_root in (q, -q) else '', len(VA), cnt))

def m3_oblique(r, lv):
    while True:
        b = r.randint(-3, 3); c = r.randint(-4, 4); d = r.choice([-3, -2, -1, 1, 2, 3])
        if c + d * (b + d) != 0: break
    s = b + d; t = lambda m, k: 'y=%s' % lin(1, k) if m == 1 else 'y=%s' % lin(m, k)
    nu = poly([1, b, c]); ex = '\\dfrac{%s}{x%+d}' % (nu, -d)
    return dict(en='Find the oblique asymptote of \\(y=%s\\).' % ex, vi='Tìm tiệm cận xiên của đồ thị \\(y=%s\\).' % ex,
      opts=pick_opts(r, t(1, s), [t(1, b - d), t(1, -s), t(1, d), t(1, b), t(-1, s)], lambda k: t(1, s + k)), ans=0,
      ee='Divide: \\(%s=(x%+d)(x%+d)%+d\\). So the asymptote is \\(y=%s\\).' % (nu, -d, s, c + d * s, lin(1, s)),
      ev='Chia đa thức: \\(%s=(x%+d)(x%+d)%+d\\). Vậy tiệm cận xiên là \\(y=%s\\).' % (nu, -d, s, c + d * s, lin(1, s)))

def m3_ha(r, lv):
    while True:
        a = r.randint(1, 6); m = r.randint(1, 4)
        if a != m and F(a, m) != F(m, a): break
    b = r.randint(-3, 3); n = r.randint(-3, 3); c = r.randint(-3, 3); k = r.randint(1, 5)
    f = lambda x: (a * x * x + b * x + c) / (m * x * x + n * x + k); assert abs(f(1e7) - a / m) < 1e-4
    t = lambda v: 'y=%s' % fr(v); ex = '\\dfrac{%s}{%s}' % (poly([a, b, c]), poly([m, n, k]))
    return dict(en='Find the horizontal asymptote of \\(y=%s\\).' % ex, vi='Tìm tiệm cận ngang của đồ thị \\(y=%s\\).' % ex,
      opts=pick_opts(r, t(F(a, m)), [t(F(m, a)), 'y=0', t(F(b, n)) if n else t(a + m), t(a)], lambda k_: t(F(a, m) + k_)), ans=0,
      ee='The degrees are equal, so \\(\\lim_{x\\to\\infty}y=\\dfrac{%d}{%d}\\).' % (a, m), ev='Hai bậc bằng nhau nên \\(\\lim_{x\\to\\infty}y=\\dfrac{%d}{%d}\\).' % (a, m))

def m3_hole(r, lv):
    roots = r.sample(range(-4, 5), 4); D = roots[:3] if r.random() < .5 else roots[:2]; N = [roots[0]] + ([roots[3]] if r.random() < .5 else [])
    VA = [x for x in D if x not in N]; cnt = len(VA)
    ex = '\\dfrac{%s}{%s}' % (''.join(xm(x) for x in N), ''.join(xm(x) for x in D))
    others = [x for x in range(0, 4) if x != cnt]; r.shuffle(others)
    return dict(en='How many vertical asymptotes does the graph of \\(y=%s\\) have?' % ex, vi='Đồ thị hàm số \\(y=%s\\) có bao nhiêu tiệm cận đứng?' % ex,
      opts=[str(cnt)] + [str(x) for x in others[:3]], ans=0,
      ee='Cancel the common factor \\(%s\\): it gives a hole, not an asymptote. The remaining zeros of the denominator give %d vertical asymptote(s).' % (xm(roots[0]), cnt),
      ev='Rút gọn thừa số chung \\(%s\\): đó là điểm hổng, không phải tiệm cận. Các nghiệm còn lại của mẫu cho %d tiệm cận đứng.' % (xm(roots[0]), cnt))

def m3_sqrt(r, lv):
    a = r.randint(2, 6); b = r.randint(-3, 3); c = r.randint(1, 4)
    f = lambda x: (a * x + b) / math.sqrt(x * x + c); assert abs(f(1e7) - a) < 1e-4 and abs(f(-1e7) + a) < 1e-4
    ex = '\\dfrac{%s}{\\sqrt{x^2+%d}}' % (lin(a, b), c)
    return dict(en='Find the horizontal asymptotes of \\(y=%s\\).' % ex, vi='Tìm các tiệm cận ngang của đồ thị \\(y=%s\\).' % ex,
      opts=['y=\\pm%d' % a, 'y=%d' % a, 'y=-%d' % a, 'y=0'], ans=0,
      ee='As \\(x\\to+\\infty\\), \\(y\\to%d\\); as \\(x\\to-\\infty\\), \\(\\sqrt{x^2}=|x|=-x\\), so \\(y\\to-%d\\). Two asymptotes.' % (a, a),
      ev='Khi \\(x\\to+\\infty\\), \\(y\\to%d\\); khi \\(x\\to-\\infty\\), \\(\\sqrt{x^2}=|x|=-x\\) nên \\(y\\to-%d\\). Có hai tiệm cận ngang.' % (a, a))

M3 = [m3_mobius, m3_count, m3_oblique, m3_ha, m3_hole, m3_sqrt, m3_mobius, m3_oblique]

# ---------- Bài 4: khảo sát và vẽ đồ thị ----------
def sk_nsol(r, lv):
    a = r.choice([1, 2, 3]); e = 2 * a ** 3            # y = x^3 - 3a^2 x có cực trị ±2a^3
    m = r.choice([-e, e, 0, e - 1, -e + 1, e + 1, -e - 1, 2 * e]); cnt = 3 if abs(m) < e else 2 if abs(m) == e else 1
    return dict(en='The graph of \\(y=x^3-%dx\\) has local extrema \\(\\pm%d\\). How many solutions does \\(x^3-%dx=%d\\) have?' % (3 * a * a, e, 3 * a * a, m), vi='Đồ thị \\(y=x^3-%dx\\) có hai giá trị cực trị là \\(\\pm%d\\). Phương trình \\(x^3-%dx=%d\\) có bao nhiêu nghiệm?' % (3 * a * a, e, 3 * a * a, m),
      opts=['0', '1', '2', '3'], ans=cnt, ee='Compare the line \\(y=%d\\) with the extrema \\(\\pm%d\\): %d intersection(s).' % (m, e, cnt), ev='So sánh đường \\(y=%d\\) với hai cực trị \\(\\pm%d\\): có %d giao điểm.' % (m, e, cnt))
def sk_center(r, lv):
    a = r.choice([1, 2]); b = r.choice([-6, -3, 3, 6, 9]) * a; c = r.randint(-5, 5); d = r.randint(-5, 5)
    x0 = F(-b, 3 * a); y0 = a * x0 ** 3 + b * x0 ** 2 + c * x0 + d; t = lambda p, q: '(%s;%s)' % (fr(p), fr(q))
    return dict(en='Find the centre of symmetry of the graph of \\(y=%s\\).' % poly([a, b, c, d]), vi='Tìm tâm đối xứng của đồ thị hàm số \\(y=%s\\).' % poly([a, b, c, d]),
      opts=pick_opts(r, t(x0, y0), [t(-x0, y0), t(x0, -y0), t(y0, x0), t(x0 + 1, y0)], fill=lambda k: t(x0 + k, y0 + 2 * k)), ans=0, ee='\\(y\'\'=0\\) at \\(x_0=-\\dfrac{b}{3a}=%s\\); then \\(y_0=%s\\).' % (fr(x0), fr(y0)), ev='\\(y\'\'=0\\) tại \\(x_0=-\\dfrac{b}{3a}=%s\\); khi đó \\(y_0=%s\\).' % (fr(x0), fr(y0)))
def sk_hyper(r, lv):
    while True:
        a, b, c, d = r.randint(-4, 4), r.randint(-4, 4), r.choice([1, 2, 3, -1, -2]), r.randint(-4, 4)
        if a * d - b * c != 0 and a != 0 and F(-d, c) != F(a, c): break
    p, q = F(-d, c), F(a, c); t = lambda x, y: '(%s;%s)' % (fr(x), fr(y))
    return dict(en='Find the intersection of the asymptotes of \\(y=\\dfrac{%s}{%s}\\).' % (lin(a, b), lin(c, d)), vi='Tìm giao điểm hai đường tiệm cận của đồ thị \\(y=\\dfrac{%s}{%s}\\).' % (lin(a, b), lin(c, d)),
      opts=pick_opts(r, t(p, q), [t(q, p), t(-p, q), t(p, -q), t(p + 1, q)], fill=lambda k: t(p + k, q + k)), ans=0, ee='Vertical asymptote \\(x=%s\\), horizontal asymptote \\(y=%s\\).' % (fr(p), fr(q)), ev='Tiệm cận đứng \\(x=%s\\), tiệm cận ngang \\(y=%s\\).' % (fr(p), fr(q)))
def sk_mono(r, lv):
    while True:
        a, b, c, d = r.randint(-4, 4), r.randint(-4, 4), r.randint(1, 4) * r.choice([1, -1]), r.randint(-4, 4)
        if a * d - b * c != 0: break
    D = a * d - b * c; inc = D > 0
    return dict(en='The function \\(y=\\dfrac{%s}{%s}\\) is…' % (lin(a, b), lin(c, d)), vi='Hàm số \\(y=\\dfrac{%s}{%s}\\)…' % (lin(a, b), lin(c, d)),
      opts=['increasing on each interval of its domain', 'decreasing on each interval of its domain', 'increasing on \\(\\mathbb{R}\\)', 'constant'] if False else ['\\text{increases on each interval}', '\\text{decreases on each interval}', '\\text{increases on }\\mathbb{R}', '\\text{is constant}'], ans=0 if inc else 1,
      ee='\\(y\'=\\dfrac{ad-bc}{(cx+d)^2}\\) and \\(ad-bc=%d\\) is %s.' % (D, 'positive' if inc else 'negative'), ev='\\(y\'=\\dfrac{ad-bc}{(cx+d)^2}\\), và \\(ad-bc=%d\\) %s.' % (D, 'dương' if inc else 'âm'))
def sk_quartic(r, lv):
    a = r.choice([1, 2, -1, -2]); b = r.choice([-4, -2, 2, 4, 6, -6]); c = r.randint(-3, 3); n = 3 if a * b < 0 else 1
    return dict(en='How many local extrema does \\(y=%s\\) have?' % poly([a, 0, b, 0, c]), vi='Hàm số \\(y=%s\\) có bao nhiêu điểm cực trị?' % poly([a, 0, b, 0, c]), opts=['0', '1', '2', '3'], ans=n,
      ee='\\(y\'=2x(2ax^2+b)\\cdot\\) : %s' % ('three roots when \\(ab\\lt0\\)' if n == 3 else 'one root (\\(x=0\\)) when \\(ab\\gt0\\)'), ev='\\(y\'=2x(2ax^2+b)\\): %s' % ('ba nghiệm khi \\(ab\\lt0\\)' if n == 3 else 'một nghiệm (\\(x=0\\)) khi \\(ab\\gt0\\)'))
def sk_value(r, lv):
    a = r.choice([1, 2]); k = r.choice([1, 2, 3]); c = r.randint(-4, 6)      # y = a x^3 - 3 a k^2 x + c : cực đại tại x=-k
    f = lambda x: a * x ** 3 - 3 * a * k * k * x + c; v = f(-k)
    return dict(en='Find the local maximum value of \\(y=%s\\).' % poly([a, 0, -3 * a * k * k, c]), vi='Tìm giá trị cực đại của hàm số \\(y=%s\\).' % poly([a, 0, -3 * a * k * k, c]),
      opts=pick_opts(r, str(v), [str(f(k)), str(c), str(v + 2), str(v - 2)], fill=lambda j: str(v + 5 + j)), ans=0, ee='\\(y\'=0\\) at \\(x=\\pm%d\\); the maximum is at \\(x=-%d\\): \\(y=%d\\).' % (k, k, v), ev='\\(y\'=0\\) tại \\(x=\\pm%d\\); cực đại tại \\(x=-%d\\): \\(y=%d\\).' % (k, k, v))
M4S = [sk_nsol, sk_center, sk_hyper, sk_mono, sk_quartic, sk_value, sk_nsol, sk_center]

# ---------- Bài 5: bài toán tối ưu thực tiễn ----------
def op_rect(r, lv):
    P = r.choice([16, 20, 24, 32, 40, 48, 60, 80]); s = P // 4
    return dict(en='A rectangle has perimeter %d m. Its largest possible area is…' % P, vi='Một hình chữ nhật có chu vi %d m. Diện tích lớn nhất có thể là…' % P,
      opts=pick_opts(r, '%d\\ \\text{m}^2' % (s * s), ['%d\\ \\text{m}^2' % (s * s // 2), '%d\\ \\text{m}^2' % (2 * s * s), '%d\\ \\text{m}^2' % (P * P // 8), '%d\\ \\text{m}^2' % (s * s + 4)], fill=lambda k: '%d\\ \\text{m}^2' % (s * s + 7 * k)), ans=0,
      ee='With \\(x+y=%d\\), \\(A=x(%d-x)\\) is largest at \\(x=%d\\): \\(A=%d\\).' % (P // 2, P // 2, s, s * s), ev='Với \\(x+y=%d\\), \\(A=x(%d-x)\\) lớn nhất khi \\(x=%d\\): \\(A=%d\\).' % (P // 2, P // 2, s, s * s))
def op_river(r, lv):
    L = r.choice([40, 60, 80, 100, 120, 160, 200]); A = L * L // 8
    return dict(en='A farmer has %d m of fence and uses a river as one side of a rectangular field. The largest area is…' % L, vi='Một người có %d m hàng rào, dùng bờ sông làm một cạnh của mảnh đất hình chữ nhật. Diện tích lớn nhất là…' % L,
      opts=pick_opts(r, '%d\\ \\text{m}^2' % A, ['%d\\ \\text{m}^2' % (L * L // 16), '%d\\ \\text{m}^2' % (L * L // 4), '%d\\ \\text{m}^2' % (L * L // 6 + 1), '%d\\ \\text{m}^2' % (A + 25)], fill=lambda k: '%d\\ \\text{m}^2' % (A + 50 * k)), ans=0,
      ee='\\(2x+y=%d\\), \\(A=x(%d-2x)\\); the maximum is at \\(x=%d\\): \\(A=%d\\).' % (L, L, L // 4, A), ev='\\(2x+y=%d\\), \\(A=x(%d-2x)\\); lớn nhất tại \\(x=%d\\): \\(A=%d\\).' % (L, L, L // 4, A))
def op_boxx(r, lv):
    a = r.choice([6, 12, 18, 24, 30, 36]); x = a // 6
    return dict(en='A box is made from a square sheet of side %d cm by cutting a square of side x from each corner. Which x gives the largest volume?' % a, vi='Làm hộp không nắp từ tấm bìa hình vuông cạnh %d cm bằng cách cắt bốn góc là bốn hình vuông cạnh x. Giá trị x nào cho thể tích lớn nhất?' % a,
      opts=pick_opts(r, '%d\\ \\text{cm}' % x, ['%d\\ \\text{cm}' % (a // 4), '%d\\ \\text{cm}' % (a // 3), '%d\\ \\text{cm}' % (a // 2), '%d\\ \\text{cm}' % (x + 1)], fill=lambda k: '%d\\ \\text{cm}' % (x + 2 * k)), ans=0,
      ee='\\(V=x(%d-2x)^2\\), \\(V\'=0\\) gives \\(x=%d\\) (the other root \\(x=%d\\) gives \\(V=0\\)).' % (a, x, a // 2), ev='\\(V=x(%d-2x)^2\\), \\(V\'=0\\) cho \\(x=%d\\) (nghiệm \\(x=%d\\) cho \\(V=0\\)).' % (a, x, a // 2))
def op_sum(r, lv):
    S = r.choice([6, 8, 10, 12, 14, 20]); v = S * S // 2
    return dict(en='Two numbers have sum %d. The smallest possible value of the sum of their squares is…' % S, vi='Hai số có tổng bằng %d. Giá trị nhỏ nhất của tổng bình phương hai số đó là…' % S,
      opts=pick_opts(r, str(v), [str(S * S), str(S * S // 4), str(v + 2), str(v - 2)], fill=lambda k: str(v + 3 * k)), ans=0,
      ee='\\(x^2+(%d-x)^2\\) is smallest at \\(x=%d\\): \\(2\\cdot%d^2=%d\\).' % (S, S // 2, S // 2, v), ev='\\(x^2+(%d-x)^2\\) nhỏ nhất tại \\(x=%d\\): \\(2\\cdot%d^2=%d\\).' % (S, S // 2, S // 2, v))
def op_cost(r, lv):
    t = r.choice([2, 3, 4, 5, 6, 8]); k = t * t
    return dict(en='The cost per item is \\(C(x)=x+\\dfrac{%d}{x}\\) (thousand VND) for \\(x\\gt0\\). Its smallest value is…' % k, vi='Chi phí mỗi sản phẩm là \\(C(x)=x+\\dfrac{%d}{x}\\) (nghìn đồng), \\(x\\gt0\\). Giá trị nhỏ nhất của \\(C\\) là…' % k,
      opts=pick_opts(r, str(2 * t), [str(t), str(k), str(2 * t + 1), str(t + k)], fill=lambda j: str(3 * t + j)), ans=0,
      ee='\\(C\'=1-\\dfrac{%d}{x^2}=0\\) at \\(x=%d\\): \\(C=%d\\).' % (k, t, 2 * t), ev='\\(C\'=1-\\dfrac{%d}{x^2}=0\\) tại \\(x=%d\\): \\(C=%d\\).' % (k, t, 2 * t))
def op_profit(r, lv):
    b = r.choice([4, 6, 8, 10, 12, 16]); c = r.choice([5, 9, 12, 20]); v = b * b // 4 - c
    return dict(en='The profit is \\(P(x)=-x^2+%dx-%d\\) (million VND). The largest profit is…' % (b, c), vi='Lợi nhuận là \\(P(x)=-x^2+%dx-%d\\) (triệu đồng). Lợi nhuận lớn nhất là…' % (b, c),
      opts=pick_opts(r, str(v), [str(b // 2), str(b * b // 4), str(v + c), str(v - 2)], fill=lambda k: str(v + 3 * k)), ans=0,
      ee='The vertex is at \\(x=%d\\): \\(P=%d\\).' % (b // 2, v), ev='Đỉnh parabol tại \\(x=%d\\): \\(P=%d\\).' % (b // 2, v))
def op_boxv(r, lv):
    a = r.choice([6, 12, 18, 24]); V = 2 * a ** 3 // 27
    return dict(en='A box is made from a square sheet of side %d cm by cutting four equal corner squares. The largest volume is…' % a, vi='Hộp không nắp làm từ tấm bìa hình vuông cạnh %d cm bằng cách cắt bốn góc bằng nhau. Thể tích lớn nhất là…' % a,
      opts=pick_opts(r, '%d\\ \\text{cm}^3' % V, ['%d\\ \\text{cm}^3' % (a ** 3 // 8), '%d\\ \\text{cm}^3' % (V + 8), '%d\\ \\text{cm}^3' % (V // 2), '%d\\ \\text{cm}^3' % (a ** 3 // 4)], fill=lambda k: '%d\\ \\text{cm}^3' % (V + 16 * k)), ans=0,
      ee='\\(x=%d\\): \\(V=%d\\cdot%d^2=%d\\).' % (a // 6, a // 6, a - a // 3, V), ev='\\(x=%d\\): \\(V=%d\\cdot%d^2=%d\\).' % (a // 6, a // 6, a - a // 3, V))
def op_rect2(r, lv):
    A = r.choice([16, 25, 36, 49, 64, 100, 144]); s = int(math.isqrt(A))
    return dict(en='A rectangle has area %d m². Its smallest possible perimeter is…' % A, vi='Một hình chữ nhật có diện tích %d m². Chu vi nhỏ nhất có thể là…' % A,
      opts=pick_opts(r, '%d\\ \\text{m}' % (4 * s), ['%d\\ \\text{m}' % (2 * s), '%d\\ \\text{m}' % (4 * s + 2), '%d\\ \\text{m}' % (8 * s), '%d\\ \\text{m}' % (2 * s + 4)], fill=lambda k: '%d\\ \\text{m}' % (4 * s + 3 * k)), ans=0,
      ee='\\(2(x+\\dfrac{%d}{x})\\) is smallest at \\(x=%d\\): \\(4\\cdot%d=%d\\).' % (A, s, s, 4 * s), ev='\\(2(x+\\dfrac{%d}{x})\\) nhỏ nhất tại \\(x=%d\\): \\(4\\cdot%d=%d\\).' % (A, s, s, 4 * s))
M5S = [op_rect, op_river, op_boxx, op_sum, op_cost, op_profit, op_boxv, op_rect2]

# ---------- Bài 6: vectơ trong không gian (hình lập phương cạnh a) ----------
_V = {'A': (0, 0, 0), 'B': (1, 0, 0), 'C': (1, 1, 0), 'D': (0, 1, 0), "A'": (0, 0, 1), "B'": (1, 0, 1), "C'": (1, 1, 1), "D'": (0, 1, 1)}
_PR = {"A'": 'A′', "B'": 'B′', "C'": 'C′', "D'": 'D′'}
def _nm(p): return _PR.get(p, p)
def _vec(p, q): return tuple(b - a for a, b in zip(_V[p], _V[q]))
def _dot(u, v): return sum(a * b for a, b in zip(u, v))
_VP = list(_V)
def _pairs(r):
    while True:
        p = r.sample(_VP, 2); q = r.sample(_VP, 2); u, v = _vec(*p), _vec(*q)
        if any(u) and any(v): return p, q, u, v
def vc_dot(r, lv):
    while True:
        p, q, u, v = _pairs(r)
        if p != q and _dot(u, v) not in (0,) or r.random() < .2: break
    a = r.choice([2, 3, 4, 5]); d = _dot(u, v) * a * a; nm = lambda x: _nm(x[0]) + _nm(x[1])
    return dict(en='\\(ABCD.A′B′C′D′\\) is a cube with edge %d. Find \\(\\overrightarrow{%s}\\cdot\\overrightarrow{%s}\\).' % (a, nm(p), nm(q)), vi='Cho hình lập phương \\(ABCD.A′B′C′D′\\) cạnh %d. Tính \\(\\overrightarrow{%s}\\cdot\\overrightarrow{%s}\\).' % (a, nm(p), nm(q)),
      opts=pick_opts(r, str(d), [str(-d) if d else str(a * a), str(d + a * a), str(2 * d) if d else str(2 * a * a), str(d - a * a)], fill=lambda k: str(d + 7 * k)), ans=0,
      ee='Write both vectors with the edge vectors \\(\\overrightarrow{AB},\\overrightarrow{AD},\\overrightarrow{AA′}\\) (pairwise perpendicular, length %d).' % a, ev='Phân tích cả hai vectơ theo \\(\\overrightarrow{AB},\\overrightarrow{AD},\\overrightarrow{AA′}\\) (đôi một vuông góc, độ dài %d).' % a)
def vc_len(r, lv):
    a = r.choice([2, 3, 4, 5, 6]); k = r.choice([('AC', 2), ("AC'", 3), ("BD'", 3), ("A'C", 3), ('BD', 2)])
    return dict(en='In a cube with edge %d, \\(|\\overrightarrow{%s}|^2\\) equals…' % (a, k[0].replace("'", '′')), vi='Trong hình lập phương cạnh %d, \\(|\\overrightarrow{%s}|^2\\) bằng…' % (a, k[0].replace("'", '′')),
      opts=pick_opts(r, str(k[1] * a * a), [str(a * a), str((k[1] % 3 + 1) * a * a), str(k[1] * a), str(4 * a * a)], fill=lambda j: str(k[1] * a * a + j)), ans=0,
      ee='The segment is a %s of the cube: its square is %d·%d².' % ('face diagonal' if k[1] == 2 else 'space diagonal', k[1], a), ev='Đoạn này là %s: bình phương độ dài là %d·%d².' % ('đường chéo mặt' if k[1] == 2 else 'đường chéo hình lập phương', k[1], a))
def vc_angle(r, lv):
    tab = {(1, F(1, 2)): 45, (-1, F(1, 2)): 135, (1, F(1, 4)): 60, (-1, F(1, 4)): 120, (0, F(0)): 90, (1, F(3, 4)): 30, (-1, F(3, 4)): 150}
    while True:
        p, q, u, v = _pairs(r); d = _dot(u, v); nu, nv = _dot(u, u), _dot(v, v)
        key = ((d > 0) - (d < 0), F(d * d, nu * nv))
        if key in tab and tab[key] not in (0, 180) and p[0] != q[0]: break
    ang = tab[key]; nm = lambda x: _nm(x[0]) + _nm(x[1])
    return dict(en='In the cube \\(ABCD.A′B′C′D′\\), the angle between \\(\\overrightarrow{%s}\\) and \\(\\overrightarrow{%s}\\) is…' % (nm(p), nm(q)), vi='Trong hình lập phương \\(ABCD.A′B′C′D′\\), góc giữa hai vectơ \\(\\overrightarrow{%s}\\) và \\(\\overrightarrow{%s}\\) bằng…' % (nm(p), nm(q)),
      opts=pick_opts(r, '%d^\\circ' % ang, ['%d^\\circ' % x for x in (30, 45, 60, 90, 120, 135, 150) if x != ang], fill=lambda k: '%d^\\circ' % (ang + k)), ans=0,
      ee='Use \\(\\cos\\theta=\\dfrac{\\vec u\\cdot\\vec v}{|\\vec u||\\vec v|}\\).', ev='Dùng \\(\\cos\\theta=\\dfrac{\\vec u\\cdot\\vec v}{|\\vec u||\\vec v|}\\).')
def vc_sum(r, lv):
    cases = [("\\overrightarrow{AB}+\\overrightarrow{AD}+\\overrightarrow{AA′}", "\\overrightarrow{AC′}", "A", "C'"), ("\\overrightarrow{BA}+\\overrightarrow{BC}+\\overrightarrow{BB′}", "\\overrightarrow{BD′}", "B", "D'"),
             ("\\overrightarrow{CB}+\\overrightarrow{CD}+\\overrightarrow{CC′}", "\\overrightarrow{CA′}", "C", "A'"), ("\\overrightarrow{DA}+\\overrightarrow{DC}+\\overrightarrow{DD′}", "\\overrightarrow{DB′}", "D", "B'")]
    c = r.choice(cases); allv = ["\\overrightarrow{AC′}", "\\overrightarrow{BD′}", "\\overrightarrow{CA′}", "\\overrightarrow{DB′}", "\\overrightarrow{AC}", "\\overrightarrow{BD}"]
    return dict(en='In a cube, \\(%s=\\;?\\)' % c[0], vi='Trong hình lập phương, \\(%s=\\;?\\)' % c[0], opts=pick_opts(r, c[1], [x for x in allv if x != c[1]]), ans=0,
      ee='Parallelepiped rule: the sum of three edge vectors from one vertex is the space diagonal from that vertex.', ev='Quy tắc hình hộp: tổng ba vectơ cạnh xuất phát từ một đỉnh là vectơ đường chéo của hình lập phương xuất phát từ đỉnh đó.')
def vc_mid(r, lv):
    P, Q = r.choice([('A', 'B'), ('C', 'D'), ('M', 'N'), ('P', 'Q'), ('E', 'F'), ('S', 'T')]); I = r.choice('IKH'); O = r.choice('OGJ')
    return dict(en='\\(%s\\) is the midpoint of \\(%s%s\\) and \\(%s\\) is any point. Then \\(\\overrightarrow{%s%s}=\\)…' % (I, P, Q, O, O, I), vi='\\(%s\\) là trung điểm của \\(%s%s\\), \\(%s\\) là điểm bất kỳ. Khi đó \\(\\overrightarrow{%s%s}=\\)…' % (I, P, Q, O, O, I),
      opts=['\\dfrac12(\\overrightarrow{%s%s}+\\overrightarrow{%s%s})' % (O, P, O, Q), '\\overrightarrow{%s%s}+\\overrightarrow{%s%s}' % (O, P, O, Q), '\\dfrac12(\\overrightarrow{%s%s}-\\overrightarrow{%s%s})' % (O, P, O, Q), '\\overrightarrow{%s%s}-\\overrightarrow{%s%s}' % (O, P, O, Q)], ans=0,
      ee='\\(\\overrightarrow{%s%s}+\\overrightarrow{%s%s}=\\vec0\\) gives \\(2\\overrightarrow{%s%s}=\\overrightarrow{%s%s}+\\overrightarrow{%s%s}\\).' % (I, P, I, Q, O, I, O, P, O, Q), ev='\\(\\overrightarrow{%s%s}+\\overrightarrow{%s%s}=\\vec0\\) suy ra \\(2\\overrightarrow{%s%s}=\\overrightarrow{%s%s}+\\overrightarrow{%s%s}\\).' % (I, P, I, Q, O, I, O, P, O, Q))
def vc_ortho(r, lv):
    cases = [("AB", "AD", 0), ("AB", "AA'", 0), ("AC", "BD", 0), ("AC", "AA'", 0), ("AD'", "AB", 0), ("BD", "A'A", 0), ("BC", "CC'", 0), ("A'C'", "B'B", 0)]
    p, q, z = r.choice(cases)
    import re as _re; pa = tuple(_re.findall(r"[A-D]'?", p)); qa = tuple(_re.findall(r"[A-D]'?", q)); d = _dot(_vec(*pa), _vec(*qa)); assert d == 0
    nm = lambda x: _nm(x[0]) + _nm(x[1])
    return dict(en='In the cube \\(ABCD.A′B′C′D′\\), \\(\\overrightarrow{%s}\\cdot\\overrightarrow{%s}=\\)…' % (nm(pa), nm(qa)), vi='Trong hình lập phương \\(ABCD.A′B′C′D′\\), \\(\\overrightarrow{%s}\\cdot\\overrightarrow{%s}=\\)…' % (nm(pa), nm(qa)),
      opts=['0', '1', '-1', '\\text{depends on the edge}'], ans=0, ee='The two vectors are perpendicular, so the dot product is 0.', ev='Hai vectơ vuông góc nên tích vô hướng bằng 0.')
M6S = [vc_dot, vc_len, vc_angle, vc_sum, vc_mid, vc_ortho, vc_dot, vc_angle]
