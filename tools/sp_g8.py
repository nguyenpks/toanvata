# -*- coding: utf-8 -*-
"""Ngân hàng câu hỏi sinh tự động cho Toán 8 (KNTT) – Chương I. Đa thức (Bài 1–5).
Dùng chung khung BANK / ABCD_TITLES của sp_g9 (3 mức ngôn ngữ; A, B, C rồi D1–D4).
Đa thức biểu diễn bằng dict {(mũ x, mũ y, mũ z): hệ số Fraction}; mọi đáp án do máy tính tính và tự kiểm lại."""
import random, re
from math import gcd
from fractions import Fraction as F
from sp_g9 import tx, nz, pick_opts, BANK, ABCD_TITLES
from mb_selfpractice import fr

V = 'xyz'

# ===================================================================================== đơn thức, đa thức
def vpart(e):
    """Phần biến: (2,1,0) -> x^2y."""
    s = ''
    for v, k in zip(V, e):
        if k == 1: s += v
        elif k > 1: s += '%s^%s' % (v, k if k < 10 else '{%d}' % k)
    return s

def mtex(c, e, first=True):
    """Đơn thức c·(phần biến e) dưới dạng TeX, có dấu nếu không đứng đầu."""
    c = F(c); p = vpart(e)
    a = abs(c)
    if not p: body = fr(a)
    elif a == 1: body = p
    else: body = fr(a) + p
    if first: return ('-' if c < 0 else '') + body
    return ('-' if c < 0 else '+') + body

def deg(e): return sum(e)

class Poly(dict):
    """Đa thức: {e: hệ số}; tự bỏ hạng tử có hệ số 0."""
    @staticmethod
    def of(terms):
        p = Poly()
        for c, e in terms: p[tuple(e)] = p.get(tuple(e), 0) + F(c)
        return p.clean()
    def clean(self):
        for k in [k for k, v in self.items() if v == 0]: del self[k]
        return self
    def __add__(self, o): return Poly.of(list(self.items_ce()) + list(o.items_ce()))
    def __sub__(self, o): return Poly.of(list(self.items_ce()) + [(-c, e) for c, e in o.items_ce()])
    def __mul__(self, o):
        if not isinstance(o, Poly): o = Poly.of([(o, (0, 0, 0))])
        return Poly.of([(c1 * c2, tuple(a + b for a, b in zip(e1, e2))) for c1, e1 in self.items_ce() for c2, e2 in o.items_ce()])
    __rmul__ = __mul__
    def __neg__(self): return Poly.of([(-c, e) for c, e in self.items_ce()])
    def items_ce(self): return [(c, e) for e, c in self.items()]
    def order(self): return sorted(self.items_ce(), key=lambda t: (-deg(t[1]), [-k for k in t[1]]))
    def tex(self, order=None):
        ts = order if order is not None else self.order()
        if not ts: return '0'
        return ''.join(mtex(c, e, i == 0) for i, (c, e) in enumerate(ts))
    def deg(self): return max((deg(e) for e in self), default=None)
    def at(self, x=0, y=0, z=0):
        return sum((c * F(x) ** e[0] * F(y) ** e[1] * F(z) ** e[2] for e, c in self.items()), F(0))
    def __eq__(self, o): return dict(self) == dict(o)
    def __hash__(self): return hash(tuple(sorted(self.items())))

def ptex(terms):
    """Viết đa thức theo đúng thứ tự cho trước (chưa thu gọn)."""
    return ''.join(mtex(c, e, i == 0) for i, (c, e) in enumerate(terms))

def M(c, e): return Poly.of([(c, e)])

def rexp(r, nv=2, lo=0, hi=3, nonzero=True):
    """Bộ số mũ ngẫu nhiên cho nv biến đầu (x, y[, z])."""
    while True:
        e = tuple(r.randint(lo, hi) if i < nv else 0 for i in range(3))
        if not nonzero or all(e[i] > 0 for i in range(nv)): return e

def par(c, e):
    """Đơn thức đặt trong ngoặc nếu có dấu âm (dùng khi viết tích)."""
    t = mtex(c, e)
    return '(%s)' % t if F(c) < 0 else t

def ptxt(p):
    """Đa thức trong ngoặc khi nhân/chia."""
    return '(%s)' % p.tex()

def popts(r, good, bads, fill):
    """Phương án là đa thức: so sánh theo TeX đã thu gọn."""
    return pick_opts(r, good.tex(), [b.tex() for b in bads if b != good], fill=lambda t: fill(t).tex())

def nopts(r, x, extra=(), step=1):
    x = F(x)
    return pick_opts(r, fr(x), [fr(F(o)) for o in extra if F(o) != x], fill=lambda t: fr(x + step * t * (1 if t % 2 else -1)))

def num(x):
    """Đáp số trả lời ngắn (số nguyên hoặc thập phân hữu hạn)."""
    x = F(x)
    if x.denominator == 1: return str(x.numerator)
    s = '%g' % float(x); assert F(s) == x, x
    return s

def vn(x):
    """Số trong công thức tiếng Việt: 1{,}5."""
    x = F(x)
    if x.denominator == 1: return str(x.numerator)
    s = '%g' % float(x); assert F(s) == x
    return s.replace('.', '{,}')

def en_(x):
    x = F(x)
    if x.denominator == 1: return str(x.numerator)
    s = '%g' % float(x); assert F(s) == x
    return s

PICK = lambda r, L: L[r.randrange(len(L))]

# =====================================================================================================
# BÀI 1. ĐƠN THỨC
# =====================================================================================================
def _coef(r, frac=False):
    if frac and r.random() < .4:
        d = r.choice([2, 3, 4, 5]); n = nz(r, -7, 7)
        if F(n, d).denominator != 1: return F(n, d)
    return F(nz(r, -9, 9))

def _nonmono(r):
    """Biểu thức không là đơn thức (có phép cộng/trừ, biến ở mẫu, căn của biến)."""
    a, b = r.randint(2, 9), r.randint(2, 9)
    return PICK(r, ['%dx+y' % a, 'x^2-%d' % b, '\\dfrac{%d}{x}' % a, '\\dfrac{x}{y}', '\\sqrt{x}', '%dxy-%d' % (a, b), 'x+\\dfrac{1}{y}', '\\dfrac{%d}{xy}' % a])

def _mono_any(r):
    c = _coef(r, True); e = rexp(r, 2, 0, 3, nonzero=False)
    if e == (0, 0, 0): e = (1, 1, 0)
    return mtex(c, e)

def b1_is_mono(r, lv):
    good = _mono_any(r); bads = []
    while len(bads) < 3:
        b = _nonmono(r)
        if b not in bads: bads.append(b)
    q = PICK(r, [('Which expression is a monomial?', 'Biểu thức nào là đơn thức?'), ('Choose the monomial.', 'Chọn biểu thức là đơn thức.'),
                 ('Only one of these expressions is a monomial. Which one?', 'Chỉ có một biểu thức là đơn thức. Đó là biểu thức nào?'),
                 ('Which of the following is a monomial?', 'Biểu thức nào sau đây là đơn thức?')])
    return dict(en=q[0], vi=q[1], opts=[good] + bads, ans=0,
                ee='A monomial is a number, a variable, or a product of numbers and variables. The other expressions contain a sum/difference, a variable in a denominator or a square root of a variable.',
                ev='Đơn thức là một số, một biến hoặc một tích giữa các số và các biến. Các biểu thức còn lại có phép cộng/trừ, có biến ở mẫu hoặc căn của biến.')

def b1_deg(r, lv):
    c1, c2 = nz(r, -6, 6), nz(r, -6, 6); e1, e2 = rexp(r, 2, 1, 4), rexp(r, 2, 1, 3)
    e = tuple(a + b for a, b in zip(e1, e2)); d = deg(e)
    t = '%s\\cdot %s' % (mtex(c1, e1), par(c2, e2))
    return dict(en='Find the degree of the monomial \\(%s\\).' % t, vi='Tìm bậc của đơn thức \\(%s\\).' % t,
                opts=nopts(r, d, [deg(e1) * deg(e2), d + 1, d - 1, max(e) ]), ans=0,
                ee='Simplify: \\(%s\\). The degree is \\(%d+%d=%d\\).' % (mtex(c1 * c2, e), e[0], e[1], d),
                ev='Thu gọn: \\(%s\\). Bậc của đơn thức là \\(%d+%d=%d\\).' % (mtex(c1 * c2, e), e[0], e[1], d))

def b1_like(r, lv):
    c = nz(r, -9, 9); e = rexp(r, 2, 1, 4)
    while e[0] == e[1]: e = rexp(r, 2, 1, 4)
    k = nz(r, -9, 9)
    good = mtex(k, e); sw = (e[1], e[0], 0)
    bads = [mtex(c, sw), mtex(c, (e[0] + 1, e[1], 0)), mtex(c, (e[0], e[1], 1)), mtex(k, (e[0], e[1] + 1, 0))]
    t = mtex(c, e)
    return dict(en='Which monomial is like \\(%s\\)?' % t, vi='Đơn thức nào đồng dạng với đơn thức \\(%s\\)?' % t,
                opts=pick_opts(r, good, bads), ans=0,
                ee='Like terms have nonzero coefficients and the same literal part \\(%s\\).' % vpart(e),
                ev='Hai đơn thức đồng dạng có hệ số khác 0 và cùng phần biến \\(%s\\).' % vpart(e))

def b1_tf_coef(r, lv):
    c = _coef(r, True); e = rexp(r, 2, 1, 4); t = mtex(c, e)
    kind = r.choice(['coef', 'deg']); truth = r.random() < .5
    if kind == 'coef':
        claim = c if truth else (-c if r.random() < .5 else F(deg(e)))
        if claim == c: truth = True
        en, vi = 'The coefficient of the monomial \\(%s\\) is \\(%s\\).' % (t, fr(claim)), 'Hệ số của đơn thức \\(%s\\) là \\(%s\\).' % (t, fr(claim))
        ee, ev = 'The coefficient is the number part: \\(%s\\).' % fr(c), 'Hệ số là phần số: \\(%s\\).' % fr(c)
    else:
        d = deg(e); claim = d if truth else r.choice([e[0] * e[1], d + 1, max(e)])
        if claim == d: truth = True
        en, vi = 'The degree of the monomial \\(%s\\) is %d.' % (t, claim), 'Bậc của đơn thức \\(%s\\) là %d.' % (t, claim)
        ee, ev = 'Degree = sum of the exponents \\(=%d+%d=%d\\).' % (e[0], e[1], d), 'Bậc = tổng các số mũ của các biến \\(=%d+%d=%d\\).' % (e[0], e[1], d)
    return dict(en=en, vi=vi, ans=truth, ee=ee, ev=ev)

def b1_tf_like(r, lv):
    e = rexp(r, 2, 1, 4)
    while e[0] == e[1]: e = rexp(r, 2, 1, 4)
    a, b = nz(r, -9, 9), nz(r, -9, 9); truth = r.random() < .5
    e2 = e if truth else (e[1], e[0], 0)
    t1, t2 = mtex(a, e), mtex(b, e2)
    return dict(en='The monomials \\(%s\\) and \\(%s\\) are like terms.' % (t1, t2), vi='Hai đơn thức \\(%s\\) và \\(%s\\) đồng dạng.' % (t1, t2), ans=truth,
                ee=('Both have the literal part \\(%s\\).' % vpart(e)) if truth else ('The literal parts \\(%s\\) and \\(%s\\) are different.' % (vpart(e), vpart(e2))),
                ev=('Cả hai có cùng phần biến \\(%s\\).' % vpart(e)) if truth else ('Phần biến \\(%s\\) và \\(%s\\) khác nhau.' % (vpart(e), vpart(e2))))

def b1_short_val(r, lv):
    c = nz(r, -5, 5); e = rexp(r, 2, 1, 3); x, y = nz(r, -3, 3), nz(r, -2, 2)
    v = M(c, e).at(x, y); t = mtex(c, e)
    return dict(en='Find the value of the monomial \\(%s\\) at \\(x=%d,\\ y=%d\\).' % (t, x, y), vi='Tính giá trị của đơn thức \\(%s\\) tại \\(x=%d,\\ y=%d\\).' % (t, x, y),
                key=num(v), ee='\\(%s\\cdot(%d)^{%d}\\cdot(%d)^{%d}=%s\\).' % (c, x, e[0], y, e[1], fr(v)), ev='\\(%s\\cdot(%d)^{%d}\\cdot(%d)^{%d}=%s\\).' % (c, x, e[0], y, e[1], fr(v)))

def b1_short_prod(r, lv):
    e1, e2 = rexp(r, 2, 1, 4), rexp(r, 3, 1, 3); c1, c2 = nz(r, -5, 5), nz(r, -5, 5)
    e = tuple(a + b for a, b in zip(e1, e2)); t = '%s\\cdot %s' % (mtex(c1, e1), par(c2, e2))
    return dict(en='Simplify the monomial \\(%s\\). What is its degree?' % t, vi='Thu gọn đơn thức \\(%s\\). Đơn thức thu gọn có bậc bằng bao nhiêu?' % t,
                key=str(deg(e)), ee='\\(%s\\cdot %s=%s\\), degree \\(%d\\).' % (mtex(c1, e1), par(c2, e2), mtex(c1 * c2, e), deg(e)),
                ev='\\(%s\\cdot %s=%s\\), bậc \\(%d\\).' % (mtex(c1, e1), par(c2, e2), mtex(c1 * c2, e), deg(e)))

# ---- tự luyện Bài 1
def b1_d1_coef(r, lv):
    c = _coef(r, True); e = rexp(r, 3 if r.random() < .4 else 2, 1, 3); t = mtex(c, e)
    return dict(en='What is the coefficient of the monomial \\(%s\\)?' % t, vi='Hệ số của đơn thức \\(%s\\) là' % t,
                opts=nopts(r, c, [-c, deg(e), abs(c) + 1]), ans=0, ee='The coefficient is the number in front of the literal part.', ev='Hệ số là phần số đứng trước phần biến.')

def b1_d1_part(r, lv):
    c = _coef(r); e = rexp(r, 2, 1, 4); t = mtex(c, e)
    bads = [mtex(c, e), vpart((e[1], e[0], 0)) if e[0] != e[1] else vpart((e[0] + 1, e[1], 0)), vpart((e[0], e[1] + 1, 0)), vpart((e[0], 0, 0))]
    return dict(en='What is the literal part of the monomial \\(%s\\)?' % t, vi='Phần biến của đơn thức \\(%s\\) là' % t,
                opts=pick_opts(r, vpart(e), bads), ans=0, ee='The literal part is the product of the variables: \\(%s\\).' % vpart(e), ev='Phần biến là tích các biến: \\(%s\\).' % vpart(e))

def b1_d1_count(r, lv):
    k = r.randint(1, 4); items = [_mono_any(r) for _ in range(k)] + [_nonmono(r) for _ in range(5 - k)]
    if len(set(items)) < 5: raise AssertionError
    r.shuffle(items); lst = ';\\ '.join(items)
    return dict(en='How many of the following expressions are monomials? \\(%s\\)' % lst, vi='Trong các biểu thức sau, có bao nhiêu đơn thức? \\(%s\\)' % lst,
                opts=nopts(r, k, [5 - k, k + 1, k - 1, 5]), ans=0,
                ee='An expression with a sum/difference, a variable in a denominator or a root of a variable is not a monomial.',
                ev='Biểu thức có phép cộng/trừ, có biến ở mẫu hoặc căn của biến thì không là đơn thức.')

def b1_d2_mul(r, lv):
    c1, c2 = _coef(r, True), nz(r, -6, 6); e1, e2 = rexp(r, 2, 1, 3), rexp(r, 2, 1, 3)
    e = tuple(a + b for a, b in zip(e1, e2)); t = '%s\\cdot %s' % (mtex(c1, e1), par(c2, e2))
    good = mtex(c1 * c2, e); bads = [mtex(-c1 * c2, e), mtex(c1 * c2, tuple(a * b for a, b in zip(e1, e2))), mtex(c1 + c2, e), mtex(c1 * c2, (e[0], e[1] - 1, 0))]
    return dict(en='Simplify \\(%s\\).' % t, vi='Thu gọn đơn thức \\(%s\\).' % t, opts=pick_opts(r, good, bads), ans=0,
                ee='Multiply the coefficients and add the exponents of each variable.', ev='Nhân các hệ số với nhau và cộng số mũ của từng biến.')

def b1_d2_sum(r, lv):
    e = rexp(r, 2, 1, 3); a, b, c = nz(r, -9, 9), nz(r, -9, 9), nz(r, -9, 9); s = a + b + c
    if s == 0: raise AssertionError
    t = ptex([(a, e), (b, e), (c, e)])
    good = mtex(s, e); bads = [mtex(a + b - c, e), mtex(s, tuple(3 * k for k in e)), mtex(-s, e), mtex(abs(a) + abs(b) + abs(c), e)]
    return dict(en='Find the sum \\(%s\\).' % t, vi='Tính tổng \\(%s\\).' % t, opts=pick_opts(r, good, bads, fill=lambda k: mtex(s + k, e)), ans=0,
                ee='Add the coefficients, keep the literal part: \\((%d)+(%d)+(%d)=%d\\).' % (a, b, c, s), ev='Cộng các hệ số, giữ nguyên phần biến: \\((%d)+(%d)+(%d)=%d\\).' % (a, b, c, s))

def b1_d2_pow(r, lv):
    k, n = r.choice([2, 3]), r.randint(2, 5); e = rexp(r, 2, 1, 4); d = deg(e)
    t = '%d^%dx%sy%s' % (n, k, '^%d' % e[0] if e[0] > 1 else '', '^%d' % e[1] if e[1] > 1 else '')
    return dict(en='What is the degree of the monomial \\(%s\\)?' % t, vi='Bậc của đơn thức \\(%s\\) là' % t, opts=nopts(r, d, [d + k, k, n ** k]), ans=0,
                ee='\\(%d^%d\\) is part of the coefficient; only the exponents of the variables count: \\(%d+%d=%d\\).' % (n, k, e[0], e[1], d),
                ev='\\(%d^%d\\) thuộc hệ số; chỉ cộng số mũ của các biến: \\(%d+%d=%d\\).' % (n, k, e[0], e[1], d))

def b1_d3_val(r, lv):
    e = rexp(r, 2, 1, 2); a, b = nz(r, -6, 6), nz(r, -6, 6); d = r.choice([2, 3]); c = F(nz(r, -5, 5), d)
    s = a + b + c
    x, y = r.choice([-3, -2, 2, 3]) * (1 if d == 2 or e[0] == 0 else 1), nz(r, -3, 3)
    v = s * F(x) ** e[0] * F(y) ** e[1]
    if s == 0 or v.denominator != 1 or abs(v) > 400: raise AssertionError
    t = ptex([(a, e), (b, e), (c, e)])
    return dict(en='Find the value of \\(A=%s\\) at \\(x=%d,\\ y=%d\\).' % (t, x, y), vi='Tính giá trị của biểu thức \\(A=%s\\) tại \\(x=%d,\\ y=%d\\).' % (t, x, y),
                opts=nopts(r, v, [-v, v * 2, a + b]), ans=0,
                ee='First combine like terms: \\(A=%s\\). Then \\(A=%s\\).' % (mtex(s, e), fr(v)), ev='Thu gọn trước: \\(A=%s\\). Thay số được \\(A=%s\\).' % (mtex(s, e), fr(v)))

def b1_d3_find(r, lv):
    e = rexp(r, 3, 1, 2); a, b = r.randint(2, 9), nz(r, -9, 9)
    op = r.choice(['-', '+'])
    A = (b + a) if op == '-' else (b - a)
    if A == 0 or A == b - a and op == '-': raise AssertionError
    t = 'A%s%s=%s' % (op, mtex(a, e), mtex(b, e))
    good = mtex(A, e); bads = [mtex(b - a if op == '-' else b + a, e), mtex(-A, e), mtex(A, tuple(2 * k for k in e))]
    return dict(en='Find the monomial \\(A\\) such that \\(%s\\).' % t, vi='Tìm đơn thức \\(A\\) biết \\(%s\\).' % t, opts=pick_opts(r, good, bads, fill=lambda k: mtex(A + k, e)), ans=0,
                ee='\\(A=%s%s%s=%s\\).' % (mtex(b, e), '+' if op == '-' else '-', mtex(abs(a), e), good), ev='\\(A=%s%s%s=%s\\).' % (mtex(b, e), '+' if op == '-' else '-', mtex(abs(a), e), good))

def b1_d3_three(r, lv):
    cs = [nz(r, -4, 4) for _ in range(3)]; es = [rexp(r, 2, 0, 2, nonzero=False) for _ in range(3)]
    es = [e if e != (0, 0, 0) else (1, 0, 0) for e in es]
    c = cs[0] * cs[1] * cs[2]; e = tuple(sum(k) for k in zip(*es))
    if 0 in e[:2]: raise AssertionError
    t = '\\cdot '.join(par(cc, ee) if i else mtex(cc, ee) for i, (cc, ee) in enumerate(zip(cs, es)))
    return dict(en='Simplify \\(%s\\), then give the coefficient of the result.' % t, vi='Thu gọn đơn thức \\(%s\\) rồi cho biết hệ số.' % t,
                opts=nopts(r, c, [-c, cs[0] + cs[1] + cs[2], deg(e)]), ans=0,
                ee='\\(%s\\); coefficient \\(%d\\).' % (mtex(c, e), c), ev='\\(%s\\); hệ số \\(%d\\).' % (mtex(c, e), c))

def b1_d4_garden(r, lv):
    a, b, k = r.randint(3, 8), r.randint(2, 6), r.randint(1, 2); x = r.randint(2, 9)
    if k >= min(a, b): raise AssertionError
    S = a * b - k * k; v = S * x * x
    return dict(en='A rectangular garden is \\(%dx\\) m long and \\(%dx\\) m wide. A square pond with side \\(%sx\\) m is dug in it. Write the area of the remaining part as a monomial and evaluate it for \\(x=%d\\).' % (a, b, '' if k == 1 else k, x),
                vi='Một mảnh vườn hình chữ nhật dài \\(%dx\\) m, rộng \\(%dx\\) m. Người ta đào một cái ao hình vuông cạnh \\(%sx\\) m trong vườn. Viết đơn thức biểu thị diện tích phần đất còn lại và tính giá trị tại \\(x=%d\\).' % (a, b, '' if k == 1 else k, x),
                opts=pick_opts(r, '%dx^2;\\ %d\\text{ m}^2' % (S, v), ['%dx^2;\\ %d\\text{ m}^2' % (a * b, a * b * x * x), '%dx^2;\\ %d\\text{ m}^2' % (a * b + k * k, (a * b + k * k) * x * x), '%dx;\\ %d\\text{ m}^2' % (S, S * x)]), ans=0,
                ee='\\(%dx\\cdot %dx-(%sx)^2=%dx^2-%dx^2=%dx^2\\); at \\(x=%d\\): \\(%d\\cdot %d=%d\\) m².' % (a, b, '' if k == 1 else k, a * b, k * k, S, x, S, x * x, v),
                ev='\\(%dx\\cdot %dx-(%sx)^2=%dx^2-%dx^2=%dx^2\\); tại \\(x=%d\\): \\(%d\\cdot %d=%d\\) m².' % (a, b, '' if k == 1 else k, a * b, k * k, S, x, S, x * x, v))

def b1_d4_box(r, lv):
    a, b, c = r.randint(2, 5), r.randint(2, 5), r.randint(1, 4); x = r.randint(2, 6); V0 = a * b * c; v = V0 * x ** 3
    return dict(en='A box in the shape of a rectangular prism has length \\(%dx\\) cm, width \\(%dx\\) cm and height \\(%sx\\) cm. Find its volume when \\(x=%d\\).' % (a, b, '' if c == 1 else c, x),
                vi='Một chiếc hộp hình hộp chữ nhật có chiều dài \\(%dx\\) cm, chiều rộng \\(%dx\\) cm và chiều cao \\(%sx\\) cm. Tính thể tích của hộp khi \\(x=%d\\).' % (a, b, '' if c == 1 else c, x),
                opts=pick_opts(r, '%d\\text{ cm}^3' % v, ['%d\\text{ cm}^3' % (V0 * x), '%d\\text{ cm}^3' % ((a + b + c) * x), '%d\\text{ cm}^3' % (V0 * x * x)]), ans=0,
                ee='\\(V=%dx\\cdot %dx\\cdot %sx=%dx^3=%d\\cdot %d=%d\\) cm³.' % (a, b, '' if c == 1 else c, V0, V0, x ** 3, v),
                ev='\\(V=%dx\\cdot %dx\\cdot %sx=%dx^3=%d\\cdot %d=%d\\) cm³.' % (a, b, '' if c == 1 else c, V0, V0, x ** 3, v))

def b1_d4_ab(r, lv):
    m, n, a1, b1 = r.randint(2, 6), r.randint(2, 6), r.randint(0, 3), r.randint(0, 3)
    a, b = m - a1, n - b1
    if a < 1 or b < 1: raise AssertionError
    c1, c2 = nz(r, -9, 9), nz(r, -9, 9)
    t1 = '%dx^{a%s}y^{%d}' % (c1, '' if a1 == 0 else '+%d' % a1, n)
    t2 = '%dx^{%d}y^{b%s}' % (c2, m, '' if b1 == 0 else '+%d' % b1)
    return dict(en='The monomials \\(%s\\) and \\(%s\\) are like terms. Find \\(a+b\\).' % (t1, t2), vi='Biết hai đơn thức \\(%s\\) và \\(%s\\) đồng dạng. Tính \\(a+b\\).' % (t1, t2),
                opts=nopts(r, a + b, [m + n, a + b + a1 + b1, m * n]), ans=0,
                ee='Same literal part: \\(a%s=%d\\Rightarrow a=%d\\); \\(b%s=%d\\Rightarrow b=%d\\). So \\(a+b=%d\\).' % ('' if a1 == 0 else '+%d' % a1, m, a, '' if b1 == 0 else '+%d' % b1, n, b, a + b),
                ev='Cùng phần biến: \\(a%s=%d\\Rightarrow a=%d\\); \\(b%s=%d\\Rightarrow b=%d\\). Vậy \\(a+b=%d\\).' % ('' if a1 == 0 else '+%d' % a1, m, a, '' if b1 == 0 else '+%d' % b1, n, b, a + b))

L1_GROUPS = [[('mcq', b1_is_mono), ('mcq', b1_deg), ('mcq', b1_like)], [('tf', b1_tf_coef), ('tf', b1_tf_like)], [('short', b1_short_val), ('short', b1_short_prod)],
             [('mcq', b1_d1_coef), ('mcq', b1_d1_part), ('mcq', b1_d1_count)], [('mcq', b1_d2_mul), ('mcq', b1_d2_sum), ('mcq', b1_d2_pow)],
             [('mcq', b1_d3_val), ('mcq', b1_d3_find), ('mcq', b1_d3_three)], [('mcq', b1_d4_garden), ('mcq', b1_d4_box), ('mcq', b1_d4_ab)]]

# =====================================================================================================
# BÀI 2. ĐA THỨC
# =====================================================================================================
def _rpoly(r, n, nv=2, hi=3, cr=9, const=True):
    """Đa thức thu gọn n hạng tử khác phần biến (có thể có hằng số)."""
    seen = set(); ts = []
    while len(ts) < n:
        e = rexp(r, nv, 0, hi, nonzero=False)
        if e == (0, 0, 0) and not const: continue
        if e in seen: continue
        seen.add(e); ts.append((F(nz(r, -cr, cr)), e))
    return ts

def _split_like(r, ts, extra=2):
    """Viết đa thức dưới dạng CHƯA thu gọn: tách một số hạng tử thành tổng hai hạng tử đồng dạng, rồi xáo trộn."""
    out = []
    for c, e in ts:
        if extra and r.random() < .7:
            a = nz(r, -9, 9)
            if a != c: out += [(a, e), (c - a, e)]; extra -= 1; continue
        out.append((c, e))
    r.shuffle(out)
    return out

def _with_cancel(r, nv=2):
    """Đa thức chưa thu gọn có hạng tử bậc cao nhất triệt tiêu (bẫy khi tìm bậc)."""
    while True:
        ts = _rpoly(r, 3, nv, 3)
        top = rexp(r, nv, 2, 4)
        if deg(top) <= max(deg(e) for _, e in ts) or top in [e for _, e in ts]: continue
        a = nz(r, -7, 7)
        out = ts + [(a, top), (-a, top)]; r.shuffle(out)
        return out, Poly.of(ts)

def b2_is_poly(r, lv):
    good = ptex(_rpoly(r, 3, 2, 2))
    bads = []
    while len(bads) < 3:
        a = r.randint(2, 9)
        b = PICK(r, ['x+\\dfrac{%d}{x}' % a, '\\dfrac{%d}{x-y}' % a, 'x^2+\\sqrt{x}', '\\dfrac{x+y}{x}', '%dxy-\\dfrac{1}{y}' % a, '\\sqrt{xy}+%d' % a])
        if b not in bads: bads.append(b)
    q = PICK(r, [('Which expression is a polynomial?', 'Biểu thức nào là đa thức?'), ('Choose the polynomial.', 'Chọn biểu thức là đa thức.'),
                 ('Only one of these expressions is a polynomial. Which one?', 'Chỉ có một biểu thức là đa thức. Đó là biểu thức nào?'), ('Which of the following is a polynomial?', 'Biểu thức nào sau đây là đa thức?')])
    return dict(en=q[0], vi=q[1], opts=[good] + bads, ans=0,
                ee='A polynomial is a sum of monomials. The other expressions contain a variable in a denominator or a square root of a variable.',
                ev='Đa thức là một tổng của những đơn thức. Các biểu thức còn lại có biến ở mẫu hoặc căn của biến.')

def b2_deg(r, lv):
    w, p = _with_cancel(r); d = p.deg(); t = ptex(w)
    return dict(en='Find the degree of the polynomial \\(%s\\).' % t, vi='Tìm bậc của đa thức \\(%s\\).' % t,
                opts=nopts(r, d, [max(deg(e) for _, e in w), d + 1, len(p)]), ans=0,
                ee='Simplify first: \\(%s\\); the term of highest degree has degree \\(%d\\).' % (p.tex(), d),
                ev='Thu gọn trước: \\(%s\\); hạng tử có bậc cao nhất có bậc \\(%d\\).' % (p.tex(), d))

def b2_simplify(r, lv):
    ts = _rpoly(r, 3, 2, 3); w = _split_like(r, ts, 3); p = Poly.of(ts)
    if len(w) < 5: raise AssertionError
    t = ptex(w)
    b1 = Poly.of([(c if i else -c, e) for i, (c, e) in enumerate(p.order())])
    b2 = Poly.of([(abs(c), e) for c, e in p.order()])
    b3 = p + M(1, p.order()[-1][1])
    return dict(en='Simplify the polynomial \\(%s\\).' % t, vi='Thu gọn đa thức \\(%s\\).' % t,
                opts=popts(r, p, [b1, b2, b3], lambda k: p + M(k + 1, p.order()[0][1])), ans=0,
                ee='Group and add the like terms.', ev='Nhóm các hạng tử đồng dạng rồi cộng các hệ số.')

def b2_tf_terms(r, lv):
    n = r.randint(2, 5); p = Poly.of(_rpoly(r, n, 2, 3)); truth = r.random() < .5
    claim = n if truth else r.choice([n + 1, n - 1])
    return dict(en='The polynomial \\(%s\\) has %d terms.' % (p.tex(), claim), vi='Đa thức \\(%s\\) có %d hạng tử.' % (p.tex(), claim), ans=(claim == n),
                ee='Its terms are \\(%s\\): %d terms.' % (',\\ '.join(mtex(c, e) for c, e in p.order()), n), ev='Các hạng tử là \\(%s\\): %d hạng tử.' % (',\\ '.join(mtex(c, e) for c, e in p.order()), n))

def b2_tf_deg(r, lv):
    w, p = _with_cancel(r); d = p.deg(); truth = r.random() < .5
    claim = d if truth else max(deg(e) for _, e in w)
    t = ptex(w)
    return dict(en='The polynomial \\(%s\\) has degree %d.' % (t, claim), vi='Đa thức \\(%s\\) có bậc là %d.' % (t, claim), ans=(claim == d),
                ee='After simplifying: \\(%s\\), so the degree is %d.' % (p.tex(), d), ev='Thu gọn được \\(%s\\) nên bậc của đa thức là %d.' % (p.tex(), d))

def b2_short_val(r, lv):
    p = Poly.of(_rpoly(r, 3, 2, 2, cr=6)); x, y = nz(r, -3, 3), nz(r, -3, 3); v = p.at(x, y)
    if abs(v) > 300: raise AssertionError
    return dict(en='Find the value of the polynomial \\(P=%s\\) at \\(x=%d,\\ y=%d\\).' % (p.tex(), x, y), vi='Tính giá trị của đa thức \\(P=%s\\) tại \\(x=%d,\\ y=%d\\).' % (p.tex(), x, y),
                key=num(v), ee='Substitute and calculate: \\(P=%s\\).' % fr(v), ev='Thay \\(x=%d,\\ y=%d\\) rồi tính: \\(P=%s\\).' % (x, y, fr(v)))

def b2_short_deg(r, lv):
    w, p = _with_cancel(r, 3 if r.random() < .3 else 2); d = p.deg(); t = ptex(w)
    return dict(en='What is the degree of the polynomial \\(%s\\)?' % t, vi='Đa thức \\(%s\\) có bậc bằng bao nhiêu?' % t, key=str(d),
                ee='Simplify: \\(%s\\). Degree \\(%d\\).' % (p.tex(), d), ev='Thu gọn: \\(%s\\). Bậc \\(%d\\).' % (p.tex(), d))

def b2_d1_const(r, lv):
    ts = _rpoly(r, 3, 2, 3, const=False); k = nz(r, -15, 15); p = Poly.of(ts + [(k, (0, 0, 0))])
    order = ts + [(k, (0, 0, 0))]; r.shuffle(order); t = ptex(order)
    return dict(en='What is the constant term of the polynomial \\(%s\\)?' % t, vi='Hệ số tự do (hạng tử không chứa biến) của đa thức \\(%s\\) là' % t,
                opts=nopts(r, k, [-k, ts[0][0], len(order)]), ans=0, ee='The constant term is the term without variables: \\(%d\\).' % k, ev='Hạng tử không chứa biến là \\(%d\\).' % k)

TXT_KIND = [tx('a monomial', 'đơn thức'), tx('a binomial', 'nhị thức (đa thức có 2 hạng tử)'), tx('a trinomial', 'tam thức (đa thức có 3 hạng tử)'), tx('a polynomial with 4 terms', 'đa thức có 4 hạng tử')]
def b2_d1_kind(r, lv):
    n = r.randint(1, 4); p = Poly.of(_rpoly(r, n, 2, 3))
    o = TXT_KIND[n - 1:n] + TXT_KIND[:n - 1] + TXT_KIND[n:]
    return dict(en='The polynomial \\(%s\\) is…' % p.tex(), vi='Đa thức \\(%s\\) là' % p.tex(), opts=o, ans=0,
                ee='It has %d term%s.' % (n, '' if n == 1 else 's'), ev='Đa thức có %d hạng tử.' % n)

def b2_d1_terms(r, lv):
    ts = _rpoly(r, 3, 2, 3); p = Poly.of(ts); od = p.order()
    good = ';\\ '.join(mtex(c, e) for c, e in od)
    b1 = ';\\ '.join(mtex(abs(c), e) for c, e in od)
    b2 = ';\\ '.join(vpart(e) or fr(c) for c, e in od)
    b3 = ';\\ '.join(mtex(-c, e) for c, e in od)
    return dict(en='What are the terms of the polynomial \\(%s\\)?' % p.tex(), vi='Các hạng tử của đa thức \\(%s\\) là' % p.tex(),
                opts=pick_opts(r, good, [b1, b2, b3]), ans=0, ee='Each term keeps its own sign.', ev='Mỗi hạng tử mang theo dấu đứng trước nó.')

def b2_d2_simplify(r, lv):
    ts = _rpoly(r, 4, 2, 2); w = _split_like(r, ts, 2); p = Poly.of(ts); t = ptex(w)
    b1 = Poly.of([(c, e) for c, e in p.order()[:-1]]); b2 = -p; b3 = p + M(2, p.order()[1][1])
    return dict(en='Which polynomial is the simplified form of \\(%s\\)?' % t, vi='Dạng thu gọn của đa thức \\(%s\\) là' % t,
                opts=popts(r, p, [b1, b2, b3], lambda k: p + M(k, p.order()[0][1])), ans=0,
                ee='Combine the like terms.', ev='Cộng các hạng tử đồng dạng.')

def b2_d2_degk(r, lv):
    while True:
        ts = _rpoly(r, 5, 2, 3); p = Poly.of(ts); k = r.choice([2, 3, 4])
        good = [(c, e) for c, e in p.order() if deg(e) == k]
        if 1 <= len(good) <= 2: break
    g = ';\\ '.join(mtex(c, e) for c, e in good)
    others = [(c, e) for c, e in p.order() if deg(e) != k]
    b1 = ';\\ '.join(mtex(c, e) for c, e in others[:2]); b2 = ';\\ '.join(mtex(c, e) for c, e in good + others[:1]); b3 = ';\\ '.join(mtex(c, e) for c, e in p.order()[:1] if deg(e) != k) or mtex(1, (k, 0, 0))
    return dict(en='Which terms of the polynomial \\(%s\\) have degree %d?' % (p.tex(), k), vi='Các hạng tử bậc %d của đa thức \\(%s\\) là' % (k, p.tex()),
                opts=pick_opts(r, g, [b1, b2, b3], fill=lambda t: mtex(t + 1, (k, 0, 0))), ans=0,
                ee='Add the exponents in each term and keep those equal to %d.' % k, ev='Cộng số mũ các biến của từng hạng tử, chọn các hạng tử có tổng bằng %d.' % k)

def b2_d2_coef(r, lv):
    ts = _rpoly(r, 3, 2, 3); w = _split_like(r, ts, 3); p = Poly.of(ts); c, e = r.choice([t for t in p.order() if deg(t[1]) > 0] or p.order())
    t = ptex(w); vp = vpart(e)
    if not vp: raise AssertionError
    raw = [cc for cc, ee in w if ee == e]
    return dict(en='After simplifying \\(%s\\), what is the coefficient of \\(%s\\)?' % (t, vp), vi='Sau khi thu gọn đa thức \\(%s\\), hệ số của hạng tử chứa \\(%s\\) là' % (t, vp),
                opts=nopts(r, c, [raw[0], -c, c + 1]), ans=0, ee='Add the coefficients of the terms in \\(%s\\): \\(%s\\).' % (vp, fr(c)), ev='Cộng hệ số các hạng tử chứa \\(%s\\): \\(%s\\).' % (vp, fr(c)))

def b2_d3_val(r, lv):
    d = r.choice([2, 3, 4]); a = F(nz(r, -5, 5), d); e = rexp(r, 2, 1, 2); rest = _rpoly(r, 2, 2, 2, cr=5)
    if e in [x for _, x in rest]: raise AssertionError
    w = [(a, e)] + rest + [(-a, e)]; r.shuffle(w); p = Poly.of(rest)
    x, y = nz(r, -3, 3), nz(r, -3, 3); v = p.at(x, y)
    if abs(v) > 200: raise AssertionError
    t = ptex(w)
    return dict(en='Find the value of \\(A=%s\\) at \\(x=%d,\\ y=%d\\).' % (t, x, y), vi='Tính giá trị của đa thức \\(A=%s\\) tại \\(x=%d,\\ y=%d\\).' % (t, x, y),
                opts=nopts(r, v, [-v, v + Poly.of([(a, e)]).at(x, y), v * 2]), ans=0,
                ee='Simplify first: \\(A=%s\\), so \\(A=%s\\).' % (p.tex(), fr(v)), ev='Thu gọn trước: \\(A=%s\\), suy ra \\(A=%s\\).' % (p.tex(), fr(v)))

def b2_d3_param(r, lv):
    e = rexp(r, 2, 1, 3); c = nz(r, -9, 9); low = _rpoly(r, 2, 2, 1, cr=7)
    if deg(e) <= max(deg(x) for _, x in low): raise AssertionError
    t = ptex([(1, e)]).replace(vpart(e), 'a' + vpart(e), 1) if False else 'a' + vpart(e) + mtex(c, e, False) + ptex(low).join(['', '']) if False else None
    t = 'a%s%s%s' % (vpart(e), mtex(c, e, False), ''.join(mtex(cc, ee, False) for cc, ee in low))
    d2 = max(deg(x) for _, x in low)
    return dict(en='Find \\(a\\) so that the polynomial \\(%s\\) has degree %d.' % (t, d2), vi='Tìm \\(a\\) để đa thức \\(%s\\) có bậc bằng %d.' % (t, d2),
                opts=nopts(r, -c, [c, 0, d2]), ans=0,
                ee='The terms in \\(%s\\) must cancel: \\(a%s=0\\Rightarrow a=%d\\).' % (vpart(e), mtex(c, (0, 0, 0), False), -c),
                ev='Các hạng tử chứa \\(%s\\) phải triệt tiêu: \\(a%s=0\\Rightarrow a=%d\\).' % (vpart(e), mtex(c, (0, 0, 0), False), -c))

def b2_d3_lead(r, lv):
    w, p = _with_cancel(r); c, e = p.order()[0]
    if len([1 for _, x in p.items_ce() if deg(x) == deg(e)]) > 1: raise AssertionError
    t = ptex(w)
    topw = max(w, key=lambda t: deg(t[1]))
    return dict(en='Simplify \\(%s\\). What is the coefficient of its term of highest degree?' % t, vi='Thu gọn đa thức \\(%s\\). Hệ số của hạng tử có bậc cao nhất là' % t,
                opts=nopts(r, c, [topw[0], -c, deg(e)]), ans=0, ee='\\(%s\\); the term of highest degree is \\(%s\\).' % (p.tex(), mtex(c, e)), ev='\\(%s\\); hạng tử bậc cao nhất là \\(%s\\).' % (p.tex(), mtex(c, e)))

def b2_d4_box(r, lv):
    x, y, z = r.sample(range(3, 13), 3); S = 2 * (x * y + y * z + z * x)
    return dict(en='A box has length \\(x\\) cm, width \\(y\\) cm and height \\(z\\) cm. Its total surface area is \\(S=2xy+2yz+2zx\\). Find \\(S\\) when \\(x=%d,\\ y=%d,\\ z=%d\\).' % (x, y, z),
                vi='Một chiếc hộp hình hộp chữ nhật có chiều dài \\(x\\) cm, chiều rộng \\(y\\) cm, chiều cao \\(z\\) cm. Tổng diện tích các mặt của hộp là \\(S=2xy+2yz+2zx\\). Tính \\(S\\) khi \\(x=%d,\\ y=%d,\\ z=%d\\).' % (x, y, z),
                opts=pick_opts(r, '%d\\text{ cm}^2' % S, ['%d\\text{ cm}^2' % (S // 2), '%d\\text{ cm}^2' % (x * y * z), '%d\\text{ cm}^2' % (2 * x * y + y * z + z * x)]), ans=0,
                ee='\\(S=2(%d\\cdot%d+%d\\cdot%d+%d\\cdot%d)=%d\\) cm².' % (x, y, y, z, z, x, S), ev='\\(S=2(%d\\cdot%d+%d\\cdot%d+%d\\cdot%d)=%d\\) cm².' % (x, y, y, z, z, x, S))

def b2_d4_shop(r, lv):
    a, b, c = r.choice([6, 8, 10, 12]), r.choice([4, 5, 7]), r.choice([25, 30, 35, 45]); x, y, z = r.randint(3, 12), r.randint(2, 10), r.randint(1, 4)
    T = a * x + b * y + c * z
    return dict(en='A notebook costs %d thousand VND, a pen costs %d thousand VND and a box of crayons costs %d thousand VND. Buying \\(x\\) notebooks, \\(y\\) pens and \\(z\\) boxes of crayons costs \\(T=%dx+%dy+%dz\\) (thousand VND). Find \\(T\\) for \\(x=%d,\\ y=%d,\\ z=%d\\).' % (a, b, c, a, b, c, x, y, z),
                vi='Một quyển vở giá %d nghìn đồng, một cây bút giá %d nghìn đồng, một hộp bút màu giá %d nghìn đồng. Mua \\(x\\) quyển vở, \\(y\\) cây bút và \\(z\\) hộp bút màu hết \\(T=%dx+%dy+%dz\\) (nghìn đồng). Tính \\(T\\) khi \\(x=%d,\\ y=%d,\\ z=%d\\).' % (a, b, c, a, b, c, x, y, z),
                opts=nopts(r, T, [a + b + c, T + c, T - b], step=5), ans=0,
                ee='\\(T=%d\\cdot%d+%d\\cdot%d+%d\\cdot%d=%d\\) thousand VND.' % (a, x, b, y, c, z, T), ev='\\(T=%d\\cdot%d+%d\\cdot%d+%d\\cdot%d=%d\\) (nghìn đồng).' % (a, x, b, y, c, z, T))

def b2_d4_sheet(r, lv):
    k = r.choice([2, 3, 4, 5]); x, y = r.randint(15, 30), r.randint(12, 25); S = x * y - 4 * k * k
    return dict(en='From a rectangular sheet of cardboard \\(x\\) cm by \\(y\\) cm, four squares with side %d cm are cut from the corners. The remaining area is \\(S=xy-%d\\) (cm²). Find \\(S\\) when \\(x=%d,\\ y=%d\\).' % (k, 4 * k * k, x, y),
                vi='Từ một tấm bìa hình chữ nhật kích thước \\(x\\) cm và \\(y\\) cm, người ta cắt bỏ ở bốn góc bốn hình vuông cạnh %d cm. Diện tích phần còn lại là \\(S=xy-%d\\) (cm²). Tính \\(S\\) khi \\(x=%d,\\ y=%d\\).' % (k, 4 * k * k, x, y),
                opts=nopts(r, S, [x * y - k * k, x * y, x * y - 4 * k], step=4), ans=0,
                ee='\\(S=%d\\cdot%d-%d=%d\\) cm².' % (x, y, 4 * k * k, S), ev='\\(S=%d\\cdot%d-%d=%d\\) cm².' % (x, y, 4 * k * k, S))

L2_GROUPS = [[('mcq', b2_is_poly), ('mcq', b2_deg), ('mcq', b2_simplify)], [('tf', b2_tf_terms), ('tf', b2_tf_deg)], [('short', b2_short_val), ('short', b2_short_deg)],
             [('mcq', b2_d1_const), ('mcq', b2_d1_kind), ('mcq', b2_d1_terms)], [('mcq', b2_d2_simplify), ('mcq', b2_d2_degk), ('mcq', b2_d2_coef)],
             [('mcq', b2_d3_val), ('mcq', b2_d3_param), ('mcq', b2_d3_lead)], [('mcq', b2_d4_box), ('mcq', b2_d4_shop), ('mcq', b2_d4_sheet)]]

# =====================================================================================================
# BÀI 3. PHÉP CỘNG VÀ PHÉP TRỪ ĐA THỨC
# =====================================================================================================
def _pair(r, nv=2, share=2, n=3, hi=2, cr=9):
    """Hai đa thức thu gọn có `share` phần biến chung (để có hạng tử đồng dạng khi cộng/trừ)."""
    P = _rpoly(r, n, nv, hi, cr)
    common = [e for _, e in P][:share]
    Q = [(F(nz(r, -cr, cr)), e) for e in common]
    seen = set(common)
    while len(Q) < n:
        e = rexp(r, nv, 0, hi, nonzero=False)
        if e in seen or e in [x for _, x in P]: continue
        seen.add(e); Q.append((F(nz(r, -cr, cr)), e))
    r.shuffle(Q)
    return Poly.of(P), Poly.of(Q)

def _wrong_minus(P, Q):
    """Lỗi hay gặp khi trừ: chỉ đổi dấu hạng tử đầu của Q."""
    od = Q.order(); bad = Poly.of([(-c if i == 0 else c, e) for i, (c, e) in enumerate(od)])
    return P + bad

def b3_sum(r, lv):
    P, Q = _pair(r); S = P + Q
    if len(S) < 2: raise AssertionError
    return dict(en='Given \\(P=%s\\) and \\(Q=%s\\). Find \\(P+Q\\).' % (P.tex(), Q.tex()), vi='Cho \\(P=%s\\) và \\(Q=%s\\). Tính \\(P+Q\\).' % (P.tex(), Q.tex()),
                opts=popts(r, S, [P - Q, Q - P, -S], lambda k: S + M(k, (0, 0, 0))), ans=0,
                ee='Remove the brackets and combine like terms: \\(P+Q=%s\\).' % S.tex(), ev='Bỏ dấu ngoặc rồi cộng các hạng tử đồng dạng: \\(P+Q=%s\\).' % S.tex())

def b3_diff(r, lv):
    P, Q = _pair(r); D = P - Q
    if len(D) < 2: raise AssertionError
    return dict(en='Given \\(A=%s\\) and \\(B=%s\\). Find \\(A-B\\).' % (P.tex(), Q.tex()), vi='Cho \\(A=%s\\) và \\(B=%s\\). Tính \\(A-B\\).' % (P.tex(), Q.tex()),
                opts=popts(r, D, [P + Q, _wrong_minus(P, Q), Q - P], lambda k: D + M(k, (0, 0, 0))), ans=0,
                ee='\\(A-B=(%s)-(%s)\\): change the sign of <b>every</b> term of \\(B\\), then combine: \\(%s\\).' % (P.tex(), Q.tex(), D.tex()),
                ev='\\(A-B=(%s)-(%s)\\): đổi dấu <b>tất cả</b> các hạng tử của \\(B\\) rồi thu gọn: \\(%s\\).' % (P.tex(), Q.tex(), D.tex()))

def b3_findM(r, lv):
    B, C = _pair(r); op = r.choice(['+', '-'])
    Mx = C - B if op == '+' else C + B
    if len(Mx) < 2: raise AssertionError
    t = 'M%s(%s)=%s' % (op, B.tex(), C.tex())
    return dict(en='Find the polynomial \\(M\\) such that \\(%s\\).' % t, vi='Tìm đa thức \\(M\\) biết \\(%s\\).' % t,
                opts=popts(r, Mx, [C + B if op == '+' else C - B, B - C, -Mx], lambda k: Mx + M(k, (0, 0, 0))), ans=0,
                ee='\\(M=(%s)%s(%s)=%s\\).' % (C.tex(), '-' if op == '+' else '+', B.tex(), Mx.tex()), ev='\\(M=(%s)%s(%s)=%s\\).' % (C.tex(), '-' if op == '+' else '+', B.tex(), Mx.tex()))

def b3_tf_sum(r, lv):
    P, Q = _pair(r); truth = r.random() < .5; op = r.choice(['+', '-'])
    good = P + Q if op == '+' else P - Q; claim = good if truth else (P - Q if op == '+' else _wrong_minus(P, Q))
    if claim == good: truth = True
    return dict(en='If \\(A=%s\\) and \\(B=%s\\), then \\(A%sB=%s\\).' % (P.tex(), Q.tex(), op, claim.tex()), vi='Nếu \\(A=%s\\) và \\(B=%s\\) thì \\(A%sB=%s\\).' % (P.tex(), Q.tex(), op, claim.tex()),
                ans=truth, ee='\\(A%sB=%s\\).' % (op, good.tex()), ev='\\(A%sB=%s\\).' % (op, good.tex()))

def b3_tf_deg(r, lv):
    while True:
        P, Q = _pair(r, hi=3); top = P.order()[0]
        Q = Q + M(top[0] - Q.get(top[1], 0), top[1])     # hạng tử bậc cao nhất của P và Q giống nhau → triệt tiêu khi trừ
        D = P - Q
        if len(D) >= 2 and D.deg() < P.deg(): break
    truth = r.random() < .5; claim = D.deg() if truth else P.deg()
    return dict(en='Given \\(A=%s\\) and \\(B=%s\\). The polynomial \\(A-B\\) has degree %d.' % (P.tex(), Q.tex(), claim), vi='Cho \\(A=%s\\) và \\(B=%s\\). Đa thức \\(A-B\\) có bậc %d.' % (P.tex(), Q.tex(), claim),
                ans=truth, ee='\\(A-B=%s\\) has degree %d (the terms of highest degree cancel).' % (D.tex(), D.deg()), ev='\\(A-B=%s\\) có bậc %d (các hạng tử bậc cao nhất triệt tiêu).' % (D.tex(), D.deg()))

def b3_short_val(r, lv):
    P, Q = _pair(r, cr=6); op = r.choice(['+', '-']); R = P + Q if op == '+' else P - Q
    x, y = nz(r, -3, 3), nz(r, -2, 2); v = R.at(x, y)
    if abs(v) > 300: raise AssertionError
    return dict(en='Given \\(A=%s\\) and \\(B=%s\\). Find the value of \\(A%sB\\) at \\(x=%d,\\ y=%d\\).' % (P.tex(), Q.tex(), op, x, y),
                vi='Cho \\(A=%s\\) và \\(B=%s\\). Tính giá trị của \\(A%sB\\) tại \\(x=%d,\\ y=%d\\).' % (P.tex(), Q.tex(), op, x, y),
                key=num(v), ee='\\(A%sB=%s\\); substitute: \\(%s\\).' % (op, R.tex(), fr(v)), ev='\\(A%sB=%s\\); thay số được \\(%s\\).' % (op, R.tex(), fr(v)))

def b3_short_coef(r, lv):
    P, Q = _pair(r, share=2); D = P - Q; common = [e for e in P if e in Q and e in D and deg(e) > 0]
    if not common: raise AssertionError
    e = r.choice(common)
    return dict(en='Given \\(A=%s\\) and \\(B=%s\\). In \\(A-B\\), what is the coefficient of \\(%s\\)?' % (P.tex(), Q.tex(), vpart(e)),
                vi='Cho \\(A=%s\\) và \\(B=%s\\). Trong đa thức \\(A-B\\), hệ số của hạng tử chứa \\(%s\\) là bao nhiêu?' % (P.tex(), Q.tex(), vpart(e)),
                key=num(D[e]), ee='\\((%s)-(%s)=%s\\).' % (fr(P[e]), fr(Q[e]), fr(D[e])), ev='\\((%s)-(%s)=%s\\).' % (fr(P[e]), fr(Q[e]), fr(D[e])))

def b3_d1_write(r, lv):
    P, Q = _pair(r)
    good = '(%s)-(%s)' % (P.tex(), Q.tex()); b1 = '%s-%s' % (P.tex(), Q.tex()); b2 = '(%s)+(%s)' % (P.tex(), Q.tex()); b3 = '(%s)-(%s)' % (Q.tex(), P.tex())
    return dict(en='Given \\(A=%s\\) and \\(B=%s\\). Which expression is \\(A-B\\)?' % (P.tex(), Q.tex()), vi='Cho \\(A=%s\\) và \\(B=%s\\). Biểu thức nào biểu diễn \\(A-B\\)?' % (P.tex(), Q.tex()),
                opts=[good, b1, b2, b3], ans=0, ee='Put each polynomial in brackets: the minus sign applies to the whole of \\(B\\).', ev='Đặt mỗi đa thức trong dấu ngoặc: dấu trừ áp dụng cho cả đa thức \\(B\\).')

def b3_d1_bracket(r, lv):
    Q = Poly.of(_rpoly(r, 3, 2, 2)); good = -Q; b1 = _wrong_minus(Poly(), Q); b2 = Q
    b3 = Poly.of([(c if i == 2 else -c, e) for i, (c, e) in enumerate(Q.order())])
    return dict(en='Remove the brackets: \\(-(%s)\\).' % Q.tex(), vi='Bỏ dấu ngoặc: \\(-(%s)\\).' % Q.tex(), opts=popts(r, good, [b1, b2, b3], lambda k: good + M(k, (0, 0, 0))), ans=0,
                ee='A minus sign in front of brackets changes the sign of every term inside.', ev='Dấu trừ đứng trước dấu ngoặc: đổi dấu tất cả các hạng tử trong ngoặc.')

def b3_d1_rule(r, lv):
    Q = PICK(r, [('To subtract a polynomial, we…', 'Muốn trừ một đa thức, ta…'), ('When we find \\(A-B\\), we…', 'Khi tính \\(A-B\\), ta…'),
                 ('Which rule is used to find the difference of two polynomials?', 'Quy tắc nào dùng để tính hiệu hai đa thức?'), ('How do we subtract polynomial \\(B\\) from polynomial \\(A\\)?', 'Làm thế nào để trừ đa thức \\(B\\) cho đa thức \\(A\\)?')])
    o = [tx('change the sign of every term of \\(B\\), then add it to \\(A\\) and combine like terms', 'đổi dấu tất cả các hạng tử của \\(B\\) rồi cộng với \\(A\\), thu gọn các hạng tử đồng dạng'),
         tx('change the sign of the first term of \\(B\\) only', 'chỉ đổi dấu hạng tử đầu tiên của \\(B\\)'),
         tx('subtract the coefficients and the exponents of like terms', 'trừ cả hệ số và số mũ của các hạng tử đồng dạng'),
         tx('remove the brackets without changing any sign', 'bỏ dấu ngoặc mà không đổi dấu hạng tử nào')]
    return dict(en=Q[0], vi=Q[1], opts=o, ans=0, ee='\\(A-B=A+(-B)\\).', ev='\\(A-B=A+(-B)\\).')

def b3_d2_sum3(r, lv):
    P, Q = _pair(r, nv=3, n=3, hi=1); S = P + Q
    if len(S) < 2: raise AssertionError
    return dict(en='Find the sum of \\(%s\\) and \\(%s\\).' % (P.tex(), Q.tex()), vi='Tính tổng của hai đa thức \\(%s\\) và \\(%s\\).' % (P.tex(), Q.tex()),
                opts=popts(r, S, [P - Q, -S, S + M(1, P.order()[0][1])], lambda k: S + M(k, (0, 0, 0))), ans=0, ee='\\(%s\\).' % S.tex(), ev='\\(%s\\).' % S.tex())

def b3_d2_diff(r, lv):
    q = b3_diff(r, lv); q['en'] = q['en'].replace('Find \\(A-B\\).', 'Which polynomial equals \\(A-B\\)?'); q['vi'] = q['vi'].replace('Tính \\(A-B\\).', 'Đa thức \\(A-B\\) là'); return q

def b3_d2_findM(r, lv):
    B, C = _pair(r, hi=3); Mx = C + B
    t = 'M-(%s)=%s' % (B.tex(), C.tex())
    return dict(en='Find \\(M\\), given that \\(%s\\).' % t, vi='Tìm đa thức \\(M\\), biết \\(%s\\).' % t,
                opts=popts(r, Mx, [C - B, B - C, -Mx], lambda k: Mx + M(k, (0, 0, 0))), ans=0, ee='\\(M=(%s)+(%s)=%s\\).' % (C.tex(), B.tex(), Mx.tex()), ev='\\(M=(%s)+(%s)=%s\\).' % (C.tex(), B.tex(), Mx.tex()))

def b3_d3_three(r, lv):
    A, B = _pair(r, cr=6); C = Poly.of(_rpoly(r, 2, 2, 2, cr=6)); R = A + B - C
    if len(R) < 2: raise AssertionError
    return dict(en='Given \\(M=%s\\), \\(N=%s\\), \\(P=%s\\). Find \\(M+N-P\\).' % (A.tex(), B.tex(), C.tex()), vi='Cho \\(M=%s\\), \\(N=%s\\), \\(P=%s\\). Tính \\(M+N-P\\).' % (A.tex(), B.tex(), C.tex()),
                opts=popts(r, R, [A + B + C, A - B - C, A + B - _wrong_minus(Poly(), C) * -1], lambda k: R + M(k, (0, 0, 0))), ans=0, ee='\\(M+N-P=%s\\).' % R.tex(), ev='\\(M+N-P=%s\\).' % R.tex())

def b3_d3_val(r, lv):
    while True:
        A, B = _pair(r, cr=5); D = A - B; x, y = nz(r, -3, 3), nz(r, -3, 3); v = D.at(x, y)
        if abs(v) <= 250: break
    return dict(en='Given \\(A=%s\\) and \\(B=%s\\). Evaluate \\(A-B\\) at \\(x=%d,\\ y=%d\\).' % (A.tex(), B.tex(), x, y), vi='Cho \\(A=%s\\) và \\(B=%s\\). Tính giá trị của \\(A-B\\) tại \\(x=%d,\\ y=%d\\).' % (A.tex(), B.tex(), x, y),
                opts=nopts(r, v, [(A + B).at(x, y), -v, _wrong_minus(A, B).at(x, y)]), ans=0, ee='\\(A-B=%s=%s\\).' % (D.tex(), fr(v)), ev='\\(A-B=%s=%s\\).' % (D.tex(), fr(v)))

def b3_d3_deg(r, lv):
    while True:
        P, Q = _pair(r, hi=3); top = P.order()[0]
        Q = Q + M(-top[0] - Q.get(top[1], 0), top[1])     # hạng tử bậc cao nhất đối nhau → triệt tiêu khi cộng
        S = P + Q
        if len(S) >= 2 and S.deg() < P.deg(): break
    return dict(en='Given \\(A=%s\\) and \\(B=%s\\). What is the degree of \\(A+B\\)?' % (P.tex(), Q.tex()), vi='Cho \\(A=%s\\) và \\(B=%s\\). Đa thức \\(A+B\\) có bậc là' % (P.tex(), Q.tex()),
                opts=nopts(r, S.deg(), [P.deg(), P.deg() + Q.deg(), S.deg() + 1]), ans=0, ee='\\(A+B=%s\\).' % S.tex(), ev='\\(A+B=%s\\).' % S.tex())

def b3_d4_profit(r, lv):
    while True:
        a, b, c = r.choice([1, 2]), r.choice([100, 120, 150, 160]), r.choice([20, 30, 40]); f = r.choice([300, 500, 800]); x = r.choice([20, 30, 40, 50])
        Rv, Cv = Poly.of([(-a, (2, 0, 0)), (b, (1, 0, 0))]), Poly.of([(c, (1, 0, 0)), (f, (0, 0, 0))]); Pf = Rv - Cv; v = Pf.at(x)
        if v > 0: break
    return dict(en='A workshop sells \\(x\\) products. Its revenue is \\(R=%s\\) and its cost is \\(C=%s\\) (thousand VND). Find the profit \\(R-C\\) when \\(x=%d\\).' % (Rv.tex(), Cv.tex(), x),
                vi='Một xưởng bán \\(x\\) sản phẩm, doanh thu là \\(R=%s\\) và chi phí là \\(C=%s\\) (nghìn đồng). Tính lợi nhuận \\(R-C\\) khi \\(x=%d\\).' % (Rv.tex(), Cv.tex(), x),
                opts=nopts(r, v, [(Rv + Cv).at(x), _wrong_minus(Rv, Cv).at(x), Rv.at(x)], step=100), ans=0,
                ee='\\(R-C=%s\\); at \\(x=%d\\) the profit is %d thousand VND.' % (Pf.tex(), x, v), ev='\\(R-C=%s\\); khi \\(x=%d\\), lợi nhuận là %d nghìn đồng.' % (Pf.tex(), x, v))

def b3_d4_tri(r, lv):
    a, b, c, d, e, f = [r.randint(1, 5) for _ in range(6)]; x, y = r.randint(2, 6), r.randint(1, 5)
    s1, s2, s3 = Poly.of([(a, (1, 0, 0)), (b, (0, 1, 0))]), Poly.of([(c, (1, 0, 0)), (-1, (0, 1, 0)), (d, (0, 0, 0))]), Poly.of([(e, (0, 1, 0)), (f, (0, 0, 0))])
    if min(s.at(x, y) for s in (s1, s2, s3)) <= 0: raise AssertionError
    L = [s.at(x, y) for s in (s1, s2, s3)]; L.sort()
    if L[0] + L[1] <= L[2]: raise AssertionError
    Pp = s1 + s2 + s3; v = Pp.at(x, y)
    return dict(en='The sides of a triangle are \\(%s\\), \\(%s\\) and \\(%s\\) (cm). Write its perimeter as a polynomial and find it when \\(x=%d,\\ y=%d\\).' % (s1.tex(), s2.tex(), s3.tex(), x, y),
                vi='Ba cạnh của một tam giác có độ dài \\(%s\\), \\(%s\\) và \\(%s\\) (cm). Viết đa thức biểu thị chu vi tam giác và tính chu vi khi \\(x=%d,\\ y=%d\\).' % (s1.tex(), s2.tex(), s3.tex(), x, y),
                opts=pick_opts(r, '%s;\\ %d\\text{ cm}' % (Pp.tex(), v), ['%s;\\ %d\\text{ cm}' % ((s1 + s2 - s3).tex(), (s1 + s2 - s3).at(x, y)), '%s;\\ %d\\text{ cm}' % (Pp.tex(), v + 2), '%s;\\ %d\\text{ cm}' % ((Pp + M(2, (0, 1, 0))).tex(), (Pp + M(2, (0, 1, 0))).at(x, y))]), ans=0,
                ee='\\(%s\\) cm; at \\(x=%d,\\ y=%d\\): \\(%d\\) cm.' % (Pp.tex(), x, y, v), ev='Chu vi \\(%s\\) (cm); khi \\(x=%d,\\ y=%d\\): \\(%d\\) cm.' % (Pp.tex(), x, y, v))

def b3_d4_findval(r, lv):
    B, C = _pair(r, cr=5); Mx = C - B; x, y = nz(r, -2, 2), nz(r, -2, 2); v = Mx.at(x, y)
    t = 'P+(%s)=%s' % (B.tex(), C.tex())
    return dict(en='Find the polynomial \\(P\\) such that \\(%s\\), then evaluate \\(P\\) at \\(x=%d,\\ y=%d\\).' % (t, x, y), vi='Tìm đa thức \\(P\\) biết \\(%s\\), rồi tính giá trị của \\(P\\) tại \\(x=%d,\\ y=%d\\).' % (t, x, y),
                opts=nopts(r, v, [(C + B).at(x, y), -v, C.at(x, y)]), ans=0, ee='\\(P=(%s)-(%s)=%s\\), so \\(P=%s\\).' % (C.tex(), B.tex(), Mx.tex(), fr(v)), ev='\\(P=(%s)-(%s)=%s\\), suy ra \\(P=%s\\).' % (C.tex(), B.tex(), Mx.tex(), fr(v)))

L3_GROUPS = [[('mcq', b3_sum), ('mcq', b3_diff), ('mcq', b3_findM)], [('tf', b3_tf_sum), ('tf', b3_tf_deg)], [('short', b3_short_val), ('short', b3_short_coef)],
             [('mcq', b3_d1_write), ('mcq', b3_d1_bracket), ('mcq', b3_d1_rule)], [('mcq', b3_d2_sum3), ('mcq', b3_d2_diff), ('mcq', b3_d2_findM)],
             [('mcq', b3_d3_three), ('mcq', b3_d3_val), ('mcq', b3_d3_deg)], [('mcq', b3_d4_profit), ('mcq', b3_d4_tri), ('mcq', b3_d4_findval)]]

# =====================================================================================================
# BÀI 4. PHÉP NHÂN ĐA THỨC
# =====================================================================================================
def _bin(r, v1=(1, 0, 0), v2=(0, 0, 0), cr=5):
    return Poly.of([(nz(r, -cr, cr), v1), (nz(r, -cr, cr), v2)])

def _mono(r, nv=2, hi=2, cr=5):
    return M(nz(r, -cr, cr), rexp(r, nv, 1, hi))

def b4_mono_poly(r, lv):
    m = _mono(r); P = Poly.of(_rpoly(r, 3, 2, 2, cr=6)); R = m * P
    c, e = list(m.items_ce())[0]
    wrong1 = Poly.of([(c * cc, tuple(a + b for a, b in zip(e, ee))) if i == 0 else (cc, ee) for i, (cc, ee) in enumerate(P.order())])
    return dict(en='Find the product \\(%s%s\\).' % (m.tex(), ptxt(P)), vi='Thực hiện phép nhân \\(%s%s\\).' % (m.tex(), ptxt(P)),
                opts=popts(r, R, [wrong1, -R, m * P + M(1, (0, 0, 0)) - M(1, (0, 0, 0)) + M(c, e)], lambda k: R + M(k, e)), ans=0,
                ee='Multiply the monomial by each term of the polynomial.', ev='Nhân đơn thức với từng hạng tử của đa thức rồi cộng các tích.')

def b4_bin_bin(r, lv):
    A = _bin(r, (1, 0, 0), (0, 1, 0)); B = _bin(r, (1, 0, 0), (0, 1, 0)); R = A * B
    if len(R) < 2: raise AssertionError
    (a, _), (b, _) = A.order()[0], A.order()[1]; (c, _), (d, _) = B.order()[0], B.order()[1]
    w1 = Poly.of([(a * c, (2, 0, 0)), (b * d, (0, 2, 0))]); w2 = Poly.of([(a * c, (2, 0, 0)), (a * d - b * c, (1, 1, 0)), (b * d, (0, 2, 0))])
    return dict(en='Expand \\(%s%s\\).' % (ptxt(A), ptxt(B)), vi='Thực hiện phép nhân \\(%s%s\\).' % (ptxt(A), ptxt(B)),
                opts=popts(r, R, [w1, w2, -R], lambda k: R + M(k, (1, 1, 0))), ans=0,
                ee='Multiply each term of the first polynomial by each term of the second, then combine: \\(%s\\).' % R.tex(),
                ev='Nhân mỗi hạng tử của đa thức thứ nhất với từng hạng tử của đa thức thứ hai rồi thu gọn: \\(%s\\).' % R.tex())

def b4_coef(r, lv):
    A = _bin(r); B = Poly.of([(1, (2, 0, 0)), (nz(r, -6, 6), (1, 0, 0)), (nz(r, -6, 6), (0, 0, 0))]); R = A * B
    k = r.choice([1, 2]); c = R.get((k, 0, 0), F(0))
    return dict(en='In the product \\(%s%s\\), what is the coefficient of \\(%s\\)?' % (ptxt(A), ptxt(B), vpart((k, 0, 0))), vi='Trong tích \\(%s%s\\), hệ số của \\(%s\\) là' % (ptxt(A), ptxt(B), vpart((k, 0, 0))),
                opts=nopts(r, c, [A.get((1, 0, 0)) * B.get((k - 1, 0, 0), 0), A.get((0, 0, 0)) * B.get((k, 0, 0), 0), -c]), ans=0,
                ee='The product is \\(%s\\).' % R.tex(), ev='Tích bằng \\(%s\\).' % R.tex())

def b4_tf_xab(r, lv):
    a, b = nz(r, -9, 9), nz(r, -9, 9); truth = r.random() < .5
    R = Poly.of([(1, (1, 0, 0)), (a, (0, 0, 0))]) * Poly.of([(1, (1, 0, 0)), (b, (0, 0, 0))])
    claim = R if truth else Poly.of([(1, (2, 0, 0)), (a * b, (1, 0, 0)), (a + b, (0, 0, 0))])
    if claim == R: truth = True
    A, B = Poly.of([(1, (1, 0, 0)), (a, (0, 0, 0))]), Poly.of([(1, (1, 0, 0)), (b, (0, 0, 0))])
    return dict(en='\\(%s%s=%s\\).' % (ptxt(A), ptxt(B), claim.tex()), vi='\\(%s%s=%s\\).' % (ptxt(A), ptxt(B), claim.tex()), ans=truth,
                ee='\\(%s%s=%s\\).' % (ptxt(A), ptxt(B), R.tex()), ev='\\(%s%s=%s\\).' % (ptxt(A), ptxt(B), R.tex()))

def b4_tf_deg(r, lv):
    A = Poly.of(_rpoly(r, 2, 2, 3)); B = Poly.of(_rpoly(r, 2, 2, 2)); R = A * B; d = R.deg(); truth = r.random() < .5
    claim = d if truth else r.choice([A.deg() * B.deg(), max(A.deg(), B.deg())])
    if claim == d: truth = True
    return dict(en='The product \\(%s%s\\) is a polynomial of degree %d.' % (ptxt(A), ptxt(B), claim), vi='Tích \\(%s%s\\) là một đa thức bậc %d.' % (ptxt(A), ptxt(B), claim), ans=truth,
                ee='The product has degree \\(%d+%d=%d\\).' % (A.deg(), B.deg(), d), ev='Tích có bậc \\(%d+%d=%d\\).' % (A.deg(), B.deg(), d))

def _expr4(r):
    """A = m1·P1 + m2·P2 (có hạng tử triệt tiêu)."""
    a, b, c = nz(r, -4, 4), nz(r, -4, 4), nz(r, -4, 4)
    P1 = Poly.of([(1, (2, 0, 0)), (a, (0, 1, 0))]); P2 = Poly.of([(1, (1, 0, 0)), (b, (0, 1, 0))]); P3 = Poly.of([(c, (1, 0, 0)), (1, (0, 1, 0))])
    X, X2, Y = M(1, (1, 0, 0)), M(1, (2, 0, 0)), M(1, (0, 1, 0))
    R = X * P1 - X2 * P2 + Y * P3
    t = 'x%s-x^2%s+y%s' % (ptxt(P1), ptxt(P2), ptxt(P3))
    return t, R

def b4_short_val(r, lv):
    t, R = _expr4(r); x, y = nz(r, -3, 3), nz(r, -3, 3); v = R.at(x, y)
    if abs(v) > 300: raise AssertionError
    return dict(en='Simplify \\(A=%s\\), then find its value at \\(x=%d,\\ y=%d\\).' % (t, x, y), vi='Rút gọn biểu thức \\(A=%s\\) rồi tính giá trị tại \\(x=%d,\\ y=%d\\).' % (t, x, y),
                key=num(v), ee='\\(A=%s=%s\\).' % (R.tex(), fr(v)), ev='\\(A=%s=%s\\).' % (R.tex(), fr(v)))

def _indep(r):
    """P = (x^2+ay)(x+1) - (x^2-ay)(x-1) + bx^2... được chọn để triệt tiêu biến, chỉ còn hằng số k."""
    a, k = r.randint(1, 5), nz(r, -15, 15)
    A = Poly.of([(1, (2, 0, 0)), (a, (0, 1, 0))]) * Poly.of([(1, (1, 0, 0)), (1, (0, 0, 0))])
    B = Poly.of([(1, (2, 0, 0)), (-a, (0, 1, 0))]) * Poly.of([(1, (1, 0, 0)), (-1, (0, 0, 0))])
    D = A - B; C = -D + M(k, (0, 0, 0))
    t = '(x^2+%sy)(x+1)-(x^2-%sy)(x-1)%s' % ('' if a == 1 else a, '' if a == 1 else a, ''.join(mtex(c, e, False) for c, e in C.order()))
    assert A - B + C == M(k, (0, 0, 0))
    return t, k, D

def b4_short_indep(r, lv):
    t, k, D = _indep(r)
    return dict(en='Show that the value of \\(P=%s\\) does not depend on the variables. What is this value?' % t, vi='Chứng tỏ giá trị của biểu thức \\(P=%s\\) không phụ thuộc vào giá trị của biến. Giá trị đó bằng bao nhiêu?' % t,
                key=str(k), ee='The first two products give \\(%s\\); everything cancels except \\(%d\\).' % (D.tex(), k), ev='Hiệu hai tích đầu bằng \\(%s\\); các hạng tử chứa biến triệt tiêu hết, còn lại \\(%d\\).' % (D.tex(), k))

def b4_d1_rule(r, lv):
    Q = PICK(r, [('To multiply a monomial by a polynomial, we…', 'Muốn nhân một đơn thức với một đa thức, ta…'), ('How do we find \\(A\\cdot(B+C)\\) when \\(A\\) is a monomial?', 'Muốn tính \\(A\\cdot(B+C)\\) với \\(A\\) là đơn thức, ta làm thế nào?'),
                 ('Which rule is used to multiply a monomial by a polynomial?', 'Quy tắc nhân đơn thức với đa thức là'), ('Complete: to multiply a monomial by a polynomial, …', 'Hoàn thành: muốn nhân đơn thức với đa thức, …')])
    o = [tx('multiply the monomial by each term of the polynomial and add the products', 'nhân đơn thức với từng hạng tử của đa thức rồi cộng các tích với nhau'),
         tx('multiply the monomial by the first term only', 'chỉ nhân đơn thức với hạng tử đầu tiên'),
         tx('add the monomial to each term of the polynomial', 'cộng đơn thức với từng hạng tử của đa thức'),
         tx('multiply the coefficients and multiply the exponents', 'nhân các hệ số và nhân các số mũ')]
    return dict(en=Q[0], vi=Q[1], opts=o, ans=0, ee='Distributive property: \\(A(B+C)=AB+AC\\).', ev='Tính chất phân phối: \\(A(B+C)=AB+AC\\).')

def b4_d1_mm(r, lv):
    a, b = _mono(r, 3, 3), _mono(r, 2, 3); R = a * b; (c1, e1), = a.items_ce(); (c2, e2), = b.items_ce()
    w1 = M(c1 * c2, tuple(p * q for p, q in zip(e1, e2))); w2 = M(c1 + c2, tuple(p + q for p, q in zip(e1, e2))); w3 = -R
    return dict(en='Find the product \\(%s\\cdot %s\\).' % (a.tex(), par(c2, e2)), vi='Tính tích \\(%s\\cdot %s\\).' % (a.tex(), par(c2, e2)),
                opts=popts(r, R, [w1, w2, w3], lambda k: R + R * k), ans=0, ee='Multiply the coefficients, add the exponents.', ev='Nhân các hệ số, cộng số mũ của cùng một biến.')

def b4_d1_count(r, lv):
    m, n = r.randint(2, 4), r.randint(2, 4)
    A = Poly.of(_rpoly(r, m, 1, 4, cr=5)); B = Poly.of([(nz(r, -5, 5), (0, k, 0)) for k in range(n)])
    if len(A) != m or len(B) != n: raise AssertionError
    return dict(en='Before combining like terms, how many products do we get when we expand \\(%s%s\\)?' % (ptxt(A), ptxt(B)),
                vi='Khi nhân \\(%s%s\\), trước khi thu gọn ta được bao nhiêu tích?' % (ptxt(A), ptxt(B)),
                opts=nopts(r, m * n, [m + n, max(m, n), m * n + 1]), ans=0, ee='Each of the %d terms is multiplied by each of the %d terms: \\(%d\\cdot%d=%d\\) products.' % (m, n, m, n, m * n),
                ev='Mỗi hạng tử trong %d hạng tử nhân với từng hạng tử trong %d hạng tử: \\(%d\\cdot%d=%d\\) tích.' % (m, n, m, n, m * n))

def b4_d2_bin(r, lv):
    A = _bin(r, (1, 0, 0), (0, 0, 0)); B = Poly.of([(1, (2, 0, 0)), (nz(r, -5, 5), (1, 0, 0)), (nz(r, -5, 5), (0, 0, 0))]); R = A * B
    od = A.order(); w = Poly.of([(od[0][0], (3, 0, 0)), (od[1][0] * B[(0, 0, 0)], (0, 0, 0))])
    return dict(en='Expand \\(%s%s\\).' % (ptxt(A), ptxt(B)), vi='Thực hiện phép nhân \\(%s%s\\).' % (ptxt(A), ptxt(B)),
                opts=popts(r, R, [w, -R, R + M(2, (1, 0, 0))], lambda k: R + M(k, (2, 0, 0))), ans=0, ee='\\(%s\\).' % R.tex(), ev='\\(%s\\).' % R.tex())

def b4_d2_xy(r, lv):
    a, b = nz(r, -5, 5), nz(r, -5, 5)
    P1 = Poly.of([(1, (1, 0, 0)), (a, (0, 1, 0))]); P2 = Poly.of([(b, (1, 0, 0)), (1, (0, 1, 0))])
    R = M(1, (1, 0, 0)) * P1 - M(1, (0, 1, 0)) * P2
    t = 'x%s-y%s' % (ptxt(P1), ptxt(P2))
    w = M(1, (1, 0, 0)) * P1 - Poly.of([(b, (1, 1, 0)), (-1, (0, 2, 0))])
    return dict(en='Simplify \\(%s\\).' % t, vi='Rút gọn biểu thức \\(%s\\).' % t, opts=popts(r, R, [w, -R, M(1, (1, 0, 0)) * P1 + M(1, (0, 1, 0)) * P2], lambda k: R + M(k, (1, 1, 0))), ans=0,
                ee='\\(%s\\).' % R.tex(), ev='\\(%s\\).' % R.tex())

def b4_d2_three(r, lv):
    a, b = nz(r, -4, 4), nz(r, -4, 4); m = _mono(r, 1, 2, 3)
    R = m * Poly.of([(1, (1, 0, 0)), (a, (0, 0, 0))]) * Poly.of([(1, (1, 0, 0)), (b, (0, 0, 0))])
    t = '%s(x%s)(x%s)' % (m.tex(), mtex(a, (0, 0, 0), False), mtex(b, (0, 0, 0), False))
    (c, e), = m.items_ce()
    return dict(en='Expand \\(%s\\).' % t, vi='Thực hiện phép nhân \\(%s\\).' % t,
                opts=popts(r, R, [m * Poly.of([(1, (2, 0, 0)), (a * b, (0, 0, 0))]), -R, m * Poly.of([(1, (2, 0, 0)), (a * b, (1, 0, 0)), (a + b, (0, 0, 0))])], lambda k: R + M(k, (1, 0, 0))), ans=0,
                ee='First \\((x%s)(x%s)=%s\\), then multiply by \\(%s\\).' % (mtex(a, (0, 0, 0), False), mtex(b, (0, 0, 0), False), (Poly.of([(1, (1, 0, 0)), (a, (0, 0, 0))]) * Poly.of([(1, (1, 0, 0)), (b, (0, 0, 0))])).tex(), m.tex()),
                ev='Tính \\((x%s)(x%s)=%s\\) rồi nhân với \\(%s\\).' % (mtex(a, (0, 0, 0), False), mtex(b, (0, 0, 0), False), (Poly.of([(1, (1, 0, 0)), (a, (0, 0, 0))]) * Poly.of([(1, (1, 0, 0)), (b, (0, 0, 0))])).tex(), m.tex()))

def b4_d3_val(r, lv):
    t, R = _expr4(r); x, y = nz(r, -3, 3), nz(r, -3, 3); v = R.at(x, y)
    if abs(v) > 300: raise AssertionError
    return dict(en='Find the value of \\(A=%s\\) at \\(x=%d,\\ y=%d\\).' % (t, x, y), vi='Tính giá trị của biểu thức \\(A=%s\\) tại \\(x=%d,\\ y=%d\\).' % (t, x, y),
                opts=nopts(r, v, [-v, v + 2 * x * y, R.at(y, x)]), ans=0, ee='Simplify first: \\(A=%s\\), so \\(A=%s\\).' % (R.tex(), fr(v)), ev='Rút gọn trước: \\(A=%s\\), suy ra \\(A=%s\\).' % (R.tex(), fr(v)))

def b4_d3_findx(r, lv):
    a, b, x = nz(r, -6, 6), r.randint(1, 4), nz(r, -9, 9)
    # x(x+a) - (x-b)(x+b)... = c  ->  ax + b^2 = c
    c = a * x + b * b
    t = 'x(x%s)-(x-%d)(x+%d)=%d' % (mtex(a, (0, 0, 0), False), b, b, c)
    return dict(en='Find \\(x\\), given that \\(%s\\).' % t, vi='Tìm \\(x\\), biết \\(%s\\).' % t, opts=nopts(r, x, [-x, F(c, a), F(c - b, a)]), ans=0,
                ee='\\(x^2%s-x^2+%d=%d\\Rightarrow %s=%d\\Rightarrow x=%d\\).' % (mtex(a, (1, 0, 0), False), b * b, c, mtex(a, (1, 0, 0)), c - b * b, x),
                ev='\\(x^2%s-x^2+%d=%d\\Rightarrow %s=%d\\Rightarrow x=%d\\).' % (mtex(a, (1, 0, 0), False), b * b, c, mtex(a, (1, 0, 0)), c - b * b, x))

def b4_d3_indep(r, lv):
    t, k, D = _indep(r)
    return dict(en='The value of \\(P=%s\\) does not depend on \\(x\\) and \\(y\\). Find it.' % t, vi='Giá trị của biểu thức \\(P=%s\\) không phụ thuộc vào \\(x\\), \\(y\\). Giá trị đó là' % t,
                opts=nopts(r, k, [-k, k + 2, k - 2]), ans=0, ee='Expanding gives \\(P=%d\\).' % k, ev='Khai triển và thu gọn được \\(P=%d\\).' % k)

def b4_d4_tank(r, lv):
    a, b = r.randint(1, 5), r.randint(1, 4); x = r.randint(3, 8)
    if a == b: raise AssertionError
    Vp = M(1, (1, 0, 0)) * Poly.of([(1, (1, 0, 0)), (a, (0, 0, 0))]) * Poly.of([(1, (1, 0, 0)), (b, (0, 0, 0))]); v = Vp.at(x)
    return dict(en='A tank has a rectangular base \\((x+%d)\\) dm by \\((x+%d)\\) dm and height \\(x\\) dm. Write its volume as a polynomial and find how many liters it holds when \\(x=%d\\).' % (a, b, x),
                vi='Một bể nước có đáy là hình chữ nhật kích thước \\((x+%d)\\) dm và \\((x+%d)\\) dm, chiều cao \\(x\\) dm. Viết đa thức biểu thị thể tích của bể và tính bể chứa được bao nhiêu lít nước khi \\(x=%d\\).' % (a, b, x),
                opts=pick_opts(r, '%s;\\ %d' % (Vp.tex(), v), ['%s;\\ %d' % ((M(1, (1, 0, 0)) * Poly.of([(1, (2, 0, 0)), (a * b, (0, 0, 0))])).tex(), x ** 3 + a * b * x), '%s;\\ %d' % (Vp.tex(), v + x * x), '%s;\\ %d' % ((Vp + M(a * b, (0, 0, 0))).tex(), v + a * b)]), ans=0,
                ee='\\(V=x(x+%d)(x+%d)=%s\\); at \\(x=%d\\): \\(%d\\) dm³ = %d liters.' % (a, b, Vp.tex(), x, v, v), ev='\\(V=x(x+%d)(x+%d)=%s\\); khi \\(x=%d\\): \\(%d\\) dm³ = %d lít.' % (a, b, Vp.tex(), x, v, v))

def b4_d4_frame(r, lv):
    k = r.randint(1, 3); x, y = r.randint(10, 30), r.randint(8, 20)
    S = Poly.of([(1, (1, 0, 0)), (2 * k, (0, 0, 0))]) * Poly.of([(1, (0, 1, 0)), (2 * k, (0, 0, 0))]) - M(1, (1, 1, 0)); v = S.at(x, y)
    return dict(en='A photo is \\(x\\) cm by \\(y\\) cm. It is put in a frame of width %d cm on every side. Write the area of the frame (not the photo) as a polynomial and find it when \\(x=%d,\\ y=%d\\).' % (k, x, y),
                vi='Một bức ảnh hình chữ nhật kích thước \\(x\\) cm và \\(y\\) cm được lồng vào khung rộng %d cm ở mỗi phía. Viết đa thức biểu thị diện tích phần khung (không tính ảnh) và tính diện tích đó khi \\(x=%d,\\ y=%d\\).' % (k, x, y),
                opts=pick_opts(r, '%s;\\ %d\\text{ cm}^2' % (S.tex(), v), ['%s;\\ %d\\text{ cm}^2' % ((S - M(2 * k * k, (0, 0, 0))).tex(), v - 2 * k * k), '%s;\\ %d\\text{ cm}^2' % ((S + M(1, (1, 1, 0))).tex(), v + x * y), '%s;\\ %d\\text{ cm}^2' % (S.tex(), v + 4 * k)]), ans=0,
                ee='\\((x+%d)(y+%d)-xy=%s\\); at the given values: \\(%d\\) cm².' % (2 * k, 2 * k, S.tex(), v), ev='\\((x+%d)(y+%d)-xy=%s\\); thay số được \\(%d\\) cm².' % (2 * k, 2 * k, S.tex(), v))

def _vnd(n, lang):
    s = '{:,}'.format(n)
    return s if lang == 'en' else s.replace(',', ' ')

def b4_d4_interest(r, lv):
    a = r.choice([50, 100, 200, 120, 80]) * 1000000; p = r.choice([5, 6, 7, 8])
    T = a * (100 + p) ** 2 // 10000; assert T * 10000 == a * (100 + p) ** 2
    simple = a + 2 * a * p // 100
    o_en = [_vnd(T, 'en'), _vnd(simple, 'en'), _vnd(a + a * p // 100, 'en'), _vnd(a * (100 + 2 * p) ** 2 // 10000 if a * (100 + 2 * p) ** 2 % 10000 == 0 else T + 100000, 'en')]
    if len(set(o_en)) < 4: raise AssertionError
    o = [tx('%s VND' % _vnd(int(s.replace(',', '')), 'en'), '%s đồng' % _vnd(int(s.replace(',', '')), 'vi')) for s in o_en]
    return dict(en='A deposit of %s VND earns \\(x=%d\\%%\\) interest per year, compounded yearly. After 2 years the amount is \\(%s(1+x)(1+x)\\) VND. How much is it?' % (_vnd(a, 'en'), p, _vnd(a, 'vi').replace(' ', '\\,')),
                vi='Gửi tiết kiệm %s đồng với lãi suất \\(x=%d\\%%\\) một năm, tiền lãi năm trước được nhập vào gốc năm sau (lãi kép). Sau 2 năm, số tiền có được là \\(%s(1+x)(1+x)\\) đồng. Số tiền đó là bao nhiêu?' % (_vnd(a, 'vi'), p, _vnd(a, 'vi').replace(' ', '\\,')),
                opts=o, ans=0, ee='\\((1+x)(1+x)=1+2x+x^2\\); with \\(x=%s\\): the amount is %s VND.' % (en_(F(p, 100)), _vnd(T, 'en')),
                ev='\\((1+x)(1+x)=1+2x+x^2\\); với \\(x=%s\\): số tiền là %s đồng.' % (vn(F(p, 100)), _vnd(T, 'vi')))

L4_GROUPS = [[('mcq', b4_mono_poly), ('mcq', b4_bin_bin), ('mcq', b4_coef)], [('tf', b4_tf_xab), ('tf', b4_tf_deg)], [('short', b4_short_val), ('short', b4_short_indep)],
             [('mcq', b4_d1_rule), ('mcq', b4_d1_mm), ('mcq', b4_d1_count)], [('mcq', b4_d2_bin), ('mcq', b4_d2_xy), ('mcq', b4_d2_three)],
             [('mcq', b4_d3_val), ('mcq', b4_d3_findx), ('mcq', b4_d3_indep)], [('mcq', b4_d4_tank), ('mcq', b4_d4_frame), ('mcq', b4_d4_interest)]]

# =====================================================================================================
# BÀI 5. PHÉP CHIA ĐA THỨC CHO ĐƠN THỨC   (Mức 1: dấu ":" như SGK; Mức 2–3: dấu "÷")
# =====================================================================================================
def divisible(eA, eB): return all(a >= b for a, b in zip(eA, eB))
def mdiv(cA, eA, cB, eB): return F(cA) / F(cB), tuple(a - b for a, b in zip(eA, eB))

def DIV(a, b, lang):
    return '%s%s%s' % (a, '\\div ' if lang == 'en' else ':', b)

def _divpair(r, ok=True, nv=3):
    """Đơn thức A, B (B có hệ số, số mũ ≤ A nếu ok)."""
    eA = rexp(r, nv, 1, 4); cB = nz(r, -6, 6); k = r.randint(1, 4)
    cA = cB * nz(r, -5, 5) if r.random() < .7 else cB * k + nz(r, 1, 3)
    if ok: eB = tuple(r.randint(0, a) for a in eA)
    else:
        eB = list(r.randint(0, a) for a in eA); i = r.randrange(nv); eB[i] = eA[i] + r.randint(1, 2); eB = tuple(eB)
    if eB == (0, 0, 0): raise AssertionError
    return F(cA), eA, F(cB), eB

def b5_exact(r, lv):
    cA, eA, cB, eB = _divpair(r, True); good = (mtex(cA, eA), mtex(cB, eB))
    bads = []
    while len(bads) < 3:
        a, ea, b, eb = _divpair(r, False)
        bads.append((mtex(a, ea), mtex(b, eb)))
    Q = PICK(r, [('Which division is exact (the dividend is divisible by the divisor)?', 'Phép chia nào là phép chia hết?'), ('Which monomial division is exact?', 'Phép chia đơn thức nào sau đây là phép chia hết?'),
                 ('In which case is the first monomial divisible by the second?', 'Trường hợp nào đơn thức thứ nhất chia hết cho đơn thức thứ hai?'), ('Only one of these divisions is exact. Which one?', 'Chỉ có một phép chia hết. Đó là phép chia nào?')])
    o = [tx('\\(%s\\)' % DIV(a, par(F(b[0] == '-' and -1 or 1), (0, 0, 0)) if False else ('(%s)' % b if b.startswith('-') else b), 'en'), '\\(%s\\)' % DIV(a, ('(%s)' % b if b.startswith('-') else b), 'vi')) for a, b in [good] + bads]
    if len(set(o)) < 4: raise AssertionError
    return dict(en=Q[0], vi=Q[1], opts=o, ans=0,
                ee='\\(A\\) is divisible by \\(B\\) when every variable of \\(B\\) is in \\(A\\) with an exponent not greater than its exponent in \\(A\\).',
                ev='Đơn thức \\(A\\) chia hết cho đơn thức \\(B\\) khi mỗi biến của \\(B\\) đều là biến của \\(A\\) với số mũ không lớn hơn số mũ của nó trong \\(A\\).')

def _q(r, nv=3):
    while True:
        cA, eA, cB, eB = _divpair(r, True, nv)
        c, e = mdiv(cA, eA, cB, eB)
        if c.denominator in (1, 2, 3) and e != (0, 0, 0): return cA, eA, cB, eB, c, e

def b5_mm(r, lv):
    cA, eA, cB, eB, c, e = _q(r); A, B = mtex(cA, eA), par(cB, eB)
    good = mtex(c, e); bads = [mtex(-c, e), mtex(cA * cB, e), mtex(c, tuple(a + b for a, b in zip(eA, eB)))]
    return dict(en='Find the quotient \\(%s\\).' % DIV(A, B, 'en'), vi='Tìm thương của phép chia \\(%s\\).' % DIV(A, B, 'vi'), opts=pick_opts(r, good, bads, fill=lambda k: mtex(c + k, e)), ans=0,
                ee='Divide the coefficients and subtract the exponents of like bases.', ev='Chia hệ số cho hệ số, trừ số mũ của cùng một biến.')

def _pm(r, nv=2):
    """Đa thức chia hết cho đơn thức m: P = m·Q."""
    m = M(nz(r, -5, 5), rexp(r, nv, 1, 2)); Q = Poly.of(_rpoly(r, 3, nv, 2, cr=6)); return m, Q, m * Q

def b5_pm(r, lv):
    m, Q, P = _pm(r); (c, e), = m.items_ce()
    w = Poly.of([(cc / c, tuple(a - b for a, b in zip(ee, e))) if i == 0 else (cc, ee) for i, (cc, ee) in enumerate(P.order())])
    return dict(en='Find the quotient \\(%s\\).' % DIV(ptxt(P), par(c, e), 'en'), vi='Tìm thương của phép chia \\(%s\\).' % DIV(ptxt(P), par(c, e), 'vi'),
                opts=popts(r, Q, [w, -Q, Q + M(1, (0, 0, 0))], lambda k: Q + M(k, Q.order()[0][1])), ans=0,
                ee='Divide each term of the polynomial by the monomial: \\(%s\\).' % Q.tex(), ev='Chia từng hạng tử của đa thức cho đơn thức rồi cộng các kết quả: \\(%s\\).' % Q.tex())

def b5_tf_div(r, lv):
    truth = r.random() < .5; cA, eA, cB, eB = _divpair(r, truth)
    A, B = mtex(cA, eA), mtex(cB, eB)
    why = 'every variable of \\(%s\\) appears in \\(%s\\) with an exponent that is not greater' % (B, A) if truth else 'some variable of \\(%s\\) has a larger exponent than in \\(%s\\)' % (B, A)
    whyv = 'mỗi biến của \\(%s\\) đều có trong \\(%s\\) với số mũ không lớn hơn' % (B, A) if truth else 'có biến của \\(%s\\) với số mũ lớn hơn số mũ của nó trong \\(%s\\)' % (B, A)
    return dict(en='The monomial \\(%s\\) is divisible by the monomial \\(%s\\).' % (A, B), vi='Đơn thức \\(%s\\) chia hết cho đơn thức \\(%s\\).' % (A, B), ans=truth,
                ee='Because %s.' % why, ev='Vì %s.' % whyv)

def b5_tf_q(r, lv):
    cA, eA, cB, eB, c, e = _q(r); truth = r.random() < .5
    claim = (c, e) if truth else r.choice([(-c, e), (c, tuple(a + b for a, b in zip(eA, eB)))])
    if claim == (c, e): truth = True
    A, B = mtex(cA, eA), par(cB, eB)
    return dict(en='\\(%s=%s\\).' % (DIV(A, B, 'en'), mtex(*claim)), vi='\\(%s=%s\\).' % (DIV(A, B, 'vi'), mtex(*claim)), ans=truth,
                ee='The quotient is \\(%s\\).' % mtex(c, e), ev='Thương đúng là \\(%s\\).' % mtex(c, e))

def b5_short_val(r, lv):
    m, Q, P = _pm(r); (c, e), = m.items_ce(); x, y = nz(r, -3, 3), nz(r, -3, 3); v = Q.at(x, y)
    if abs(v) > 200: raise AssertionError
    return dict(en='Let \\(Q=%s\\). Find the value of \\(Q\\) at \\(x=%d,\\ y=%d\\).' % (DIV(ptxt(P), par(c, e), 'en'), x, y), vi='Cho \\(Q=%s\\). Tính giá trị của \\(Q\\) tại \\(x=%d,\\ y=%d\\).' % (DIV(ptxt(P), par(c, e), 'vi'), x, y),
                key=num(v), ee='\\(Q=%s\\), so \\(Q=%s\\).' % (Q.tex(), fr(v)), ev='\\(Q=%s\\), suy ra \\(Q=%s\\).' % (Q.tex(), fr(v)))

def b5_short_n(r, lv):
    a, b, k = r.randint(2, 6), r.randint(1, 5), r.randint(2, 5); c1, c2 = nz(r, -9, 9), nz(r, -9, 9); n0 = a
    t1 = '%dx^ny^{%d}' % (c1, b + k); t2 = '%sx^{%d}y^{%d}' % (mtex(c2, (0, 0, 0)), a, b)
    return dict(en='Find the smallest natural number \\(n\\) such that the monomial \\(%s\\) is divisible by \\(%s\\).' % (t1, t2),
                vi='Tìm số tự nhiên \\(n\\) nhỏ nhất để đơn thức \\(%s\\) chia hết cho đơn thức \\(%s\\).' % (t1, t2), key=str(n0),
                ee='We need \\(n\\ge %d\\) (and \\(%d\\ge %d\\) already holds), so the smallest \\(n\\) is %d.' % (a, b + k, b, n0),
                ev='Cần \\(n\\ge %d\\) (số mũ của \\(y\\): \\(%d\\ge %d\\) đã thỏa mãn) nên \\(n\\) nhỏ nhất là %d.' % (a, b + k, b, n0))

def b5_d1_rule(r, lv):
    Q = PICK(r, [('To divide a polynomial by a monomial (when every term is divisible), we…', 'Muốn chia đa thức cho đơn thức (trường hợp các hạng tử đều chia hết), ta…'),
                 ('How do we divide a polynomial by a monomial?', 'Quy tắc chia đa thức cho đơn thức là'), ('Which rule is used to divide a polynomial by a monomial?', 'Muốn chia đa thức \\(A\\) cho đơn thức \\(B\\), ta làm thế nào?'),
                 ('Complete: to divide a polynomial by a monomial, …', 'Hoàn thành: muốn chia đa thức cho đơn thức, …')])
    o = [tx('divide each term of the polynomial by the monomial and add the results', 'chia từng hạng tử của đa thức cho đơn thức rồi cộng các kết quả'),
         tx('divide only the first term by the monomial', 'chỉ chia hạng tử đầu tiên cho đơn thức'),
         tx('subtract the monomial from each term', 'trừ mỗi hạng tử cho đơn thức'),
         tx('divide the coefficients and add the exponents', 'chia các hệ số và cộng các số mũ')]
    return dict(en=Q[0], vi=Q[1], opts=o, ans=0, ee='\\((A+B):C=A:C+B:C\\).'.replace(':', '\\div '), ev='\\((A+B):C=A:C+B:C\\).')

def b5_d1_pow(r, lv):
    m, n = r.randint(5, 12), r.randint(1, 4)
    return dict(en='Find \\(%s\\).' % DIV('x^{%d}' % m, 'x^{%d}' % n, 'en'), vi='Tính \\(%s\\).' % DIV('x^{%d}' % m, 'x^{%d}' % n, 'vi'),
                opts=pick_opts(r, 'x^{%d}' % (m - n), ['x^{%d}' % (m + n), 'x^{%d}' % (m // n) if m % n == 0 and m // n != m - n else 'x^{%d}' % (m * n), '1']), ans=0,
                ee='\\(x^m\\div x^n=x^{m-n}\\ (m\\ge n)\\).', ev='\\(x^m:x^n=x^{m-n}\\ (m\\ge n)\\).')

def b5_d1_which(r, lv):
    cA, eA, cB, eB = _divpair(r, True)
    good = mtex(cB, eB); bads = []
    for _ in range(20):
        a, ea, b, eb = _divpair(r, False)
        eb2 = tuple(max(x, y) if i == 0 else x for i, (x, y) in enumerate(zip(eb, eA)))
        if not divisible(eA, eb) and mtex(b, eb) not in bads: bads.append(mtex(b, eb))
        if len(bads) == 3: break
    if len(bads) < 3: raise AssertionError
    A = mtex(cA, eA)
    return dict(en='The monomial \\(%s\\) is divisible by which monomial?' % A, vi='Đơn thức \\(%s\\) chia hết cho đơn thức nào sau đây?' % A, opts=[good] + bads, ans=0,
                ee='Compare the exponents of each variable.', ev='So sánh số mũ của từng biến.')

def b5_d2_mm(r, lv):
    while True:
        cA, eA, cB, eB, c, e = _q(r, 2)
        if c.denominator != 1: break
    A, B = mtex(cA, eA), par(cB, eB)
    return dict(en='Which monomial is the quotient of \\(%s\\)?' % DIV(A, B, 'en'), vi='Thương của phép chia \\(%s\\) là' % DIV(A, B, 'vi'),
                opts=pick_opts(r, mtex(c, e), [mtex(-c, e), mtex(1 / c, e), mtex(c, tuple(a + b for a, b in zip(eA, eB)))]), ans=0, ee='\\(%s\\).' % mtex(c, e), ev='\\(%s\\).' % mtex(c, e))

def b5_d2_pm(r, lv):
    q = b5_pm(r, lv); q['en'] = q['en'].replace('Find the quotient', 'Divide'); q['vi'] = q['vi'].replace('Tìm thương của phép chia', 'Thực hiện phép chia'); return q

def b5_d2_findP(r, lv):
    m, Q, P = _pm(r); (c, e), = m.items_ce()
    return dict(en='Find the polynomial \\(A\\) such that \\(A\\cdot %s=%s\\).' % (par(c, e), P.tex()), vi='Tìm đa thức \\(A\\) biết \\(A\\cdot %s=%s\\).' % (par(c, e), P.tex()),
                opts=popts(r, Q, [-Q, P * m, Q + M(1, (0, 0, 0))], lambda k: Q + M(k, (0, 0, 0))), ans=0,
                ee='\\(A=%s=%s\\).' % (DIV(ptxt(P), par(c, e), 'en'), Q.tex()), ev='\\(A=%s=%s\\).' % (DIV(ptxt(P), par(c, e), 'vi'), Q.tex()))

def b5_d3_two(r, lv):
    m1, Q1, P1 = _pm(r); m2, Q2, P2 = _pm(r); R = Q1 - Q2
    if len(R) < 2: raise AssertionError
    (c1, e1), = m1.items_ce(); (c2, e2), = m2.items_ce()
    def t(l): return '%s-%s' % (DIV(ptxt(P1), par(c1, e1), l), DIV(ptxt(P2), par(c2, e2), l))
    return dict(en='Simplify \\(M=%s\\).' % t('en'), vi='Rút gọn biểu thức \\(M=%s\\).' % t('vi'), opts=popts(r, R, [Q1 + Q2, Q2 - Q1, R + M(1, (0, 0, 0))], lambda k: R + M(k, (0, 0, 0))), ans=0,
                ee='\\(M=(%s)-(%s)=%s\\).' % (Q1.tex(), Q2.tex(), R.tex()), ev='\\(M=(%s)-(%s)=%s\\).' % (Q1.tex(), Q2.tex(), R.tex()))

def b5_d3_val(r, lv):
    m, Q, P = _pm(r); (c, e), = m.items_ce(); x, y = nz(r, -3, 3), nz(r, -3, 3); v = Q.at(x, y)
    if abs(v) > 200: raise AssertionError
    return dict(en='Find the value of \\(%s\\) at \\(x=%d,\\ y=%d\\).' % (DIV(ptxt(P), par(c, e), 'en'), x, y), vi='Tính giá trị của biểu thức \\(%s\\) tại \\(x=%d,\\ y=%d\\).' % (DIV(ptxt(P), par(c, e), 'vi'), x, y),
                opts=nopts(r, v, [-v, P.at(x, y), v + 1]), ans=0, ee='The quotient is \\(%s\\), its value is \\(%s\\).' % (Q.tex(), fr(v)), ev='Thương là \\(%s\\), có giá trị \\(%s\\).' % (Q.tex(), fr(v)))

def b5_d3_n(r, lv):
    a, b, k = r.randint(3, 7), r.randint(2, 6), r.randint(1, 3); c1, c2 = nz(r, -9, 9), nz(r, -9, 9)
    P = Poly.of([(c1, (a, k + 1, 0)), (c2, (a + 2, k, 0))])
    return dict(en='Find the largest natural number \\(n\\) such that \\(%s\\) is divisible by \\(x^ny^{%d}\\).' % (P.tex(), k), vi='Tìm số tự nhiên \\(n\\) lớn nhất để đa thức \\(%s\\) chia hết cho đơn thức \\(x^ny^{%d}\\).' % (P.tex(), k),
                opts=nopts(r, a, [a + 2, a + 1, k]), ans=0, ee='Every term must be divisible: \\(n\\le %d\\) and \\(n\\le %d\\), so \\(n=%d\\).' % (a, a + 2, a),
                ev='Mọi hạng tử đều phải chia hết: \\(n\\le %d\\) và \\(n\\le %d\\) nên \\(n=%d\\).' % (a, a + 2, a))

def b5_d4_rect(r, lv):
    a, b, k = r.randint(2, 5), r.randint(2, 5), r.randint(1, 4); x, y = r.randint(2, 6), r.randint(1, 5)
    W = M(k, (2, 1, 0)); L = Poly.of([(a, (1, 0, 0)), (b, (0, 1, 0))]); S = W * L; v = L.at(x, y)
    return dict(en='A rectangle has area \\(%s\\) (cm²) and width \\(%s\\) (cm). Find its length, then evaluate it for \\(x=%d,\\ y=%d\\).' % (S.tex(), W.tex(), x, y),
                vi='Một hình chữ nhật có diện tích \\(%s\\) (cm²) và chiều rộng \\(%s\\) (cm). Tìm chiều dài của hình chữ nhật rồi tính chiều dài khi \\(x=%d,\\ y=%d\\).' % (S.tex(), W.tex(), x, y),
                opts=pick_opts(r, '%s;\\ %d\\text{ cm}' % (L.tex(), v), ['%s;\\ %d\\text{ cm}' % ((S * W).tex() if False else Poly.of([(a, (2, 0, 0)), (b, (1, 1, 0))]).tex(), a * x * x + b * x * y), '%s;\\ %d\\text{ cm}' % (L.tex(), v + 1), '%s;\\ %d\\text{ cm}' % (Poly.of([(a, (1, 0, 0)), (-b, (0, 1, 0))]).tex(), a * x - b * y)]), ans=0,
                ee='Length \\(=%s=%s\\); at \\(x=%d,\\ y=%d\\): \\(%d\\) cm.' % (DIV(ptxt(S), W.tex(), 'en'), L.tex(), x, y, v), ev='Chiều dài \\(=%s=%s\\); khi \\(x=%d,\\ y=%d\\): \\(%d\\) cm.' % (DIV(ptxt(S), W.tex(), 'vi'), L.tex(), x, y, v))

def b5_d4_box(r, lv):
    a, b = r.randint(1, 5), r.randint(1, 6); x = r.randint(2, 6)
    base = M(r.choice([2, 3, 4]), (2, 0, 0)); h = Poly.of([(a, (1, 0, 0)), (b, (0, 0, 0))]); Vp = base * h; v = h.at(x)
    return dict(en='A box in the shape of a rectangular prism has volume \\(%s\\) (cm³) and base area \\(%s\\) (cm²). Find its height when \\(x=%d\\).' % (Vp.tex(), base.tex(), x),
                vi='Một chiếc hộp hình hộp chữ nhật có thể tích \\(%s\\) (cm³) và diện tích đáy \\(%s\\) (cm²). Tính chiều cao của hộp khi \\(x=%d\\).' % (Vp.tex(), base.tex(), x),
                opts=nopts(r, v, [a * x, Vp.at(x), v + b]), ans=0, ee='Height \\(=%s=%s\\); at \\(x=%d\\): %d cm.' % (DIV(ptxt(Vp), base.tex(), 'en'), h.tex(), x, v),
                ev='Chiều cao \\(=%s=%s\\); khi \\(x=%d\\): %d cm.' % (DIV(ptxt(Vp), base.tex(), 'vi'), h.tex(), x, v))

def b5_d4_share(r, lv):
    a, b, k = r.randint(2, 6), r.randint(1, 5), r.choice([3, 4, 5, 6]); x, y = r.randint(2, 5), r.randint(10, 30)
    D = M(k, (1, 0, 0)); Q = Poly.of([(a, (1, 0, 0)), (b, (0, 1, 0))]); T = D * Q; v = Q.at(x, y)
    return dict(en='A class of \\(%sx\\) students pays \\(%s\\) thousand VND in total for a trip, shared equally. How much does each student pay? Find it for \\(x=%d,\\ y=%d\\).' % (k, T.tex(), x, y),
                vi='Một lớp có \\(%sx\\) học sinh góp tổng cộng \\(%s\\) nghìn đồng cho chuyến tham quan, mỗi bạn góp như nhau. Mỗi bạn góp bao nhiêu? Tính số tiền đó khi \\(x=%d,\\ y=%d\\).' % (k, T.tex(), x, y),
                opts=pick_opts(r, '%s;\\ %d' % (Q.tex(), v), ['%s;\\ %d' % (Poly.of([(a, (1, 0, 0)), (b * k, (0, 1, 0))]).tex(), a * x + b * k * y), '%s;\\ %d' % (Q.tex(), v * k), '%s;\\ %d' % (Poly.of([(a, (2, 0, 0)), (b, (1, 1, 0))]).tex(), a * x * x + b * x * y)]), ans=0,
                ee='\\(%s=%s\\) thousand VND; for the given values: %d thousand VND.' % (DIV(ptxt(T), D.tex(), 'en'), Q.tex(), v), ev='\\(%s=%s\\) (nghìn đồng); thay số: %d nghìn đồng.' % (DIV(ptxt(T), D.tex(), 'vi'), Q.tex(), v))

L5_GROUPS = [[('mcq', b5_exact), ('mcq', b5_mm), ('mcq', b5_pm)], [('tf', b5_tf_div), ('tf', b5_tf_q)], [('short', b5_short_val), ('short', b5_short_n)],
             [('mcq', b5_d1_rule), ('mcq', b5_d1_pow), ('mcq', b5_d1_which)], [('mcq', b5_d2_mm), ('mcq', b5_d2_pm), ('mcq', b5_d2_findP)],
             [('mcq', b5_d3_two), ('mcq', b5_d3_val), ('mcq', b5_d3_n)], [('mcq', b5_d4_rect), ('mcq', b5_d4_box), ('mcq', b5_d4_share)]]

# =====================================================================================================
# CHƯƠNG II. HẰNG ĐẲNG THỨC ĐÁNG NHỚ VÀ ỨNG DỤNG (Bài 6–9)
# =====================================================================================================
XV, YV = (1, 0, 0), (0, 1, 0)
def L(a, b, v1=XV, v2=(0, 0, 0)):
    """Nhị thức a·v1 + b·v2 (mặc định ax + b)."""
    return Poly.of([(a, v1), (b, v2)])
def br(p): return '(%s)' % p.tex()
def sq(p): return '(%s)^2' % p.tex()
def cb(p): return '(%s)^3' % p.tex()
def tpoly(r, pp, bads, fill=None):
    """Phương án là đa thức (so sánh theo giá trị); bỏ phương án trùng giá trị với đáp án."""
    bads = [b for b in bads if b != pp]
    return pick_opts(r, pp.tex(), [b.tex() for b in bads], fill=(lambda t: fill(t).tex()) if fill else None)

def _ab(r, two=False, lo=1, hi=5):
    """(A, B) dạng (ax, b) hoặc (ax, by)."""
    a = r.randint(lo, hi); b = r.randint(1, 9)
    A = M(a, XV); B = M(b, YV) if two else M(b, (0, 0, 0))
    return A, B, a, b

# ----------------------------------------------------------------------------------- BÀI 6
def b6_expand(r, lv):
    A, B, a, b = _ab(r, r.random() < .5); s = r.choice([1, -1]); P = A + s * B; R = P * P
    w1 = A * A + B * B * s; w2 = A * A + s * 2 * A * B * F(1, 2) + B * B; w3 = A * A - s * 2 * A * B + B * B
    return dict(en='Expand \\(%s\\).' % sq(P), vi='Khai triển \\(%s\\).' % sq(P), opts=tpoly(r, R, [w1, w2, w3, A * A + B * B]), ans=0,
                ee='\\((A%sB)^2=A^2%s2AB+B^2\\) with \\(A=%s,\\ B=%s\\): \\(%s\\).' % ('+' if s > 0 else '-', '+' if s > 0 else '-', A.tex(), B.tex(), R.tex()),
                ev='\\((A%sB)^2=A^2%s2AB+B^2\\) với \\(A=%s,\\ B=%s\\): \\(%s\\).' % ('+' if s > 0 else '-', '+' if s > 0 else '-', A.tex(), B.tex(), R.tex()))

def b6_dsq(r, lv):
    A, B, a, b = _ab(r, r.random() < .4, 1, 6)
    if gcd(a, b) > 1: raise AssertionError
    P = A * A - B * B
    good = '%s%s' % (br(A - B), br(A + B)); bads = [sq(A - B), sq(A + B), '%s%s' % (br(A - B), br(B - A)) if False else '%s%s' % (br(A * 1 - B * 2 if b > 1 else A - B * 3), br(A + B * 2 if b > 1 else A + B * 3)), '(%s)(%s)' % ((A - B).tex(), (A - B).tex())]
    bads = list(dict.fromkeys(x for x in bads if x != good))
    return dict(en='Write \\(%s\\) as a product.' % P.tex(), vi='Viết đa thức \\(%s\\) dưới dạng tích.' % P.tex(), opts=pick_opts(r, good, bads), ans=0,
                ee='\\(A^2-B^2=(A-B)(A+B)\\) with \\(A=%s,\\ B=%s\\).' % (A.tex(), B.tex()), ev='\\(A^2-B^2=(A-B)(A+B)\\) với \\(A=%s,\\ B=%s\\).' % (A.tex(), B.tex()))

def b6_identity(r, lv):
    a = r.randint(1, 6); b = r.randint(2, 9)
    good = '(x+%d)^2=x^2+%dx+%d' % (a, 2 * a, a * a)
    bads = ['(x+%d)^2=x^2+%d' % (a, a * a), '%dx+%d=%dx' % (b, a, b + a), 'x^2-%d=0' % (a * a), '(x-%d)^2=x^2-%d' % (a, a * a)]
    r.shuffle(bads); bads = bads[:3]
    q = PICK(r, [('Which equality is an identity?', 'Đẳng thức nào là hằng đẳng thức?'), ('Which equality is true for every value of \\(x\\)?', 'Đẳng thức nào đúng với mọi giá trị của \\(x\\)?'),
                 ('Choose the identity.', 'Chọn đẳng thức là hằng đẳng thức.'), ('Only one of these equalities is an identity. Which one?', 'Chỉ có một đẳng thức là hằng đẳng thức. Đó là đẳng thức nào?')])
    return dict(en=q[0], vi=q[1], opts=[good] + bads, ans=0, ee='An identity is an equality that is true for all values of the variables.', ev='Hằng đẳng thức là đẳng thức mà hai vế luôn nhận cùng một giá trị với mọi giá trị của biến.')

def b6_tf_sq(r, lv):
    a = r.randint(2, 9); s = r.choice([1, -1]); truth = r.random() < .5; P = L(1, s * a); R = P * P
    claim = R if truth else Poly.of([(1, (2, 0, 0)), (s * a * a if s > 0 else -a * a, (0, 0, 0))])
    return dict(en='\\(%s=%s\\).' % (sq(P), claim.tex()), vi='\\(%s=%s\\).' % (sq(P), claim.tex()), ans=(claim == R),
                ee='\\(%s=%s\\): do not forget the middle term \\(%s\\).' % (sq(P), R.tex(), mtex(2 * s * a, XV)), ev='\\(%s=%s\\): không được quên hạng tử \\(%s\\).' % (sq(P), R.tex(), mtex(2 * s * a, XV)))

def b6_tf_dsq(r, lv):
    a, k = r.randint(1, 5), r.randint(1, 9); truth = r.random() < .5
    P = Poly.of([(a * a, (2, 0, 0)), (-k * k, (0, 0, 0))])
    claim = '(%s)(%s)' % (L(a, -k).tex(), L(a, k).tex()) if truth else r.choice([sq(L(a, -k)), '(%s)(%s)' % (L(a, -k).tex(), L(-a, k).tex())])
    return dict(en='\\(%s=%s\\).' % (P.tex(), claim), vi='\\(%s=%s\\).' % (P.tex(), claim), ans=truth,
                ee='\\(%s=(%s)(%s)\\).' % (P.tex(), L(a, -k).tex(), L(a, k).tex()), ev='\\(%s=(%s)(%s)\\).' % (P.tex(), L(a, -k).tex(), L(a, k).tex()))

def b6_short_fast(r, lv):
    kind = r.choice(['sq', 'prod'])
    if kind == 'sq':
        base, k, s = r.choice([20, 30, 40, 50, 60, 70, 100]), r.randint(1, 3), r.choice([1, -1]); n = base + s * k; v = n * n
        return dict(en='Calculate \\(%d^2\\) quickly using an identity.' % n, vi='Tính nhanh \\(%d^2\\) bằng hằng đẳng thức.' % n, key=str(v),
                    ee='\\(%d^2=(%d%s%d)^2=%d%s%d+%d=%d\\).' % (n, base, '+' if s > 0 else '-', k, base * base, '+' if s > 0 else '-', 2 * base * k, k * k, v),
                    ev='\\(%d^2=(%d%s%d)^2=%d%s%d+%d=%d\\).' % (n, base, '+' if s > 0 else '-', k, base * base, '+' if s > 0 else '-', 2 * base * k, k * k, v))
    base, k = r.choice([20, 30, 40, 50, 60, 70]), r.randint(1, 4); v = base * base - k * k
    return dict(en='Calculate \\(%d\\cdot %d\\) quickly using an identity.' % (base - k, base + k), vi='Tính nhanh \\(%d\\cdot %d\\) bằng hằng đẳng thức.' % (base - k, base + k), key=str(v),
                ee='\\((%d-%d)(%d+%d)=%d^2-%d^2=%d\\).' % (base, k, base, k, base, k, v), ev='\\((%d-%d)(%d+%d)=%d^2-%d^2=%d\\).' % (base, k, base, k, base, k, v))

def b6_short_mid(r, lv):
    a, b = r.randint(1, 5), r.randint(1, 9); s = r.choice([1, -1]); m = 2 * a * b
    t = '%sx^2%s\\square\\, x+%d=(%sx%s%d)^2' % ('' if a == 1 else a * a, '+' if s > 0 else '-', b * b, '' if a == 1 else a, '+' if s > 0 else '-', b)
    return dict(en='Find the positive number in the box: \\(%s\\).' % t, vi='Tìm số dương thích hợp điền vào ô trống: \\(%s\\).' % t, key=str(m),
                ee='The middle term is \\(2\\cdot %sx\\cdot %d=%dx\\).' % ('' if a == 1 else a, b, m), ev='Hạng tử giữa là \\(2\\cdot %sx\\cdot %d=%dx\\).' % ('' if a == 1 else a, b, m))

ID_FORMS = [('(A+B)^2', 'A^2+2AB+B^2', ['A^2+B^2', 'A^2+AB+B^2', 'A^2-2AB+B^2'], 'the square of a sum', 'bình phương của một tổng'),
            ('(A-B)^2', 'A^2-2AB+B^2', ['A^2-B^2', 'A^2+2AB-B^2', 'A^2-AB+B^2'], 'the square of a difference', 'bình phương của một hiệu'),
            ('A^2-B^2', '(A-B)(A+B)', ['(A-B)^2', '(A+B)^2', '(B-A)(A+B)'], 'the difference of two squares', 'hiệu hai bình phương')]
def b6_d1_formula(r, lv):
    lhs, good, bads, en, vi = PICK(r, ID_FORMS)
    return dict(en='Complete the identity (%s): \\(%s=\\,?\\)' % (en, lhs), vi='Hoàn thành hằng đẳng thức (%s): \\(%s=\\,?\\)' % (vi, lhs), opts=[good] + bads, ans=0,
                ee='\\(%s=%s\\).' % (lhs, good), ev='\\(%s=%s\\).' % (lhs, good))

def b6_d1_read(r, lv):
    lhs, good, bads, en, vi = PICK(r, ID_FORMS)
    o = [tx(x[3], x[4]) for x in ID_FORMS if x[0] == lhs] + [tx(x[3], x[4]) for x in ID_FORMS if x[0] != lhs] + [tx('the sum of two squares', 'tổng hai bình phương')]
    return dict(en='How do we read \\(%s\\)?' % lhs, vi='Biểu thức \\(%s\\) được gọi là' % lhs, opts=o, ans=0, ee='\\(%s\\) is %s.' % (lhs, en), ev='\\(%s\\) là %s.' % (lhs, vi))

def b6_d1_AB(r, lv):
    a, b = r.randint(2, 6), r.randint(1, 9); s = r.choice([1, -1]); P = L(a, s * b) * L(a, s * b)
    good = 'A=%dx,\\ B=%d' % (a, b); bads = ['A=%dx,\\ B=%d' % (a * a, b * b), 'A=%dx,\\ B=%d' % (a, b * b), 'A=x,\\ B=%d' % b]
    return dict(en='Write \\(%s\\) in the form \\((A%sB)^2\\). Then…' % (P.tex(), '+' if s > 0 else '-'), vi='Viết \\(%s\\) dưới dạng \\((A%sB)^2\\). Khi đó' % (P.tex(), '+' if s > 0 else '-'),
                opts=pick_opts(r, good, bads), ans=0, ee='\\(%s=(%dx)^2%s2\\cdot%dx\\cdot%d+%d^2\\).' % (P.tex(), a, '+' if s > 0 else '-', a, b, b), ev='\\(%s=(%dx)^2%s2\\cdot%dx\\cdot%d+%d^2\\).' % (P.tex(), a, '+' if s > 0 else '-', a, b, b))

def b6_d2_exp(r, lv):
    A, B, a, b = _ab(r, True, 1, 5); P = A - B; R = P * P
    return dict(en='Expand \\(%s\\).' % sq(P), vi='Khai triển \\(%s\\).' % sq(P), opts=tpoly(r, R, [A * A - B * B, A * A + 2 * A * B + B * B, A * A - A * B + B * B]), ans=0,
                ee='\\(%s\\).' % R.tex(), ev='\\(%s\\).' % R.tex())

def b6_d2_conj(r, lv):
    A, B, a, b = _ab(r, True, 2, 7); R = (A - B) * (A + B)
    return dict(en='Find the product \\(%s%s\\).' % (br(A - B), br(A + B)), vi='Tính \\(%s%s\\).' % (br(A - B), br(A + B)),
                opts=tpoly(r, R, [A * A + B * B, (A - B) * (A - B), Poly.of([(a, (2, 0, 0)), (-b, (0, 2, 0))])]), ans=0,
                ee='\\((A-B)(A+B)=A^2-B^2=%s\\).' % R.tex(), ev='\\((A-B)(A+B)=A^2-B^2=%s\\).' % R.tex())

def b6_d2_tosq(r, lv):
    a, b = r.randint(1, 5), r.randint(1, 9)
    if gcd(a, b) > 1: raise AssertionError
    s = r.choice([1, -1]); P = L(a, s * b); R = P * P
    good = sq(P); bads = [sq(L(a, -s * b)), sq(L(a * a, s * b)) if a > 1 else sq(L(1, s * b * 2)), '(%s)(%s)' % (L(a, -b).tex(), L(a, b).tex())]
    return dict(en='Write \\(%s\\) as the square of a binomial.' % R.tex(), vi='Viết đa thức \\(%s\\) dưới dạng bình phương của một tổng hoặc một hiệu.' % R.tex(), opts=pick_opts(r, good, bads), ans=0,
                ee='\\(%s=%s\\).' % (R.tex(), good), ev='\\(%s=%s\\).' % (R.tex(), good))

def b6_d3_simp(r, lv):
    a = r.randint(1, 9); kind = r.choice(['-', '+']); P1, P2 = L(1, a), L(1, -a)
    R = P1 * P1 - P2 * P2 if kind == '-' else P1 * P1 + P2 * P2
    bads = [M(2 * a, XV), Poly.of([(2, (2, 0, 0))]), M(4 * a, XV) if kind == '+' else Poly.of([(2, (2, 0, 0)), (2 * a * a, (0, 0, 0))]), M(0, XV) + M(a * a * 2, (0, 0, 0))]
    return dict(en='Simplify \\(%s%s%s\\).' % (sq(P1), kind, sq(P2)), vi='Rút gọn biểu thức \\(%s%s%s\\).' % (sq(P1), kind, sq(P2)), opts=tpoly(r, R, bads, lambda t: R + M(t, (0, 0, 0))), ans=0,
                ee='\\(=%s\\).' % R.tex(), ev='\\(=%s\\).' % R.tex())

def b6_d3_val(r, lv):
    s = r.choice([1, -1]); base = r.choice([10, 20, 50, 100]); y = r.randint(1, 9); x = base - s * y
    P = '%s' % ('x^2+2xy+y^2' if s > 0 else 'x^2-2xy+y^2'); v = base * base
    return dict(en='Find the value of \\(%s\\) at \\(x=%d,\\ y=%d\\).' % (P, x, y), vi='Tính giá trị của biểu thức \\(%s\\) tại \\(x=%d,\\ y=%d\\).' % (P, x, y),
                opts=nopts(r, v, [x * x + y * y, (x - s * y) ** 2, v + 2 * x * y], step=100), ans=0,
                ee='\\(%s=(x%sy)^2=%d^2=%d\\).' % (P, '+' if s > 0 else '-', base, v), ev='\\(%s=(x%sy)^2=%d^2=%d\\).' % (P, '+' if s > 0 else '-', base, v))

def b6_d3_fast(r, lv):
    base, k = r.choice([30, 40, 50, 60, 70, 80]), r.randint(2, 9); v = base * base - k * k
    return dict(en='Calculate quickly: \\(%d\\cdot %d\\).' % (base - k, base + k), vi='Tính nhanh: \\(%d\\cdot %d\\).' % (base - k, base + k), opts=nopts(r, v, [base * base + k * k, base * base, v - 10]), ans=0,
                ee='\\(=%d^2-%d^2=%d-%d=%d\\).' % (base, k, base * base, k * k, v), ev='\\(=%d^2-%d^2=%d-%d=%d\\).' % (base, k, base * base, k * k, v))

def b6_d4_ab(r, lv):
    while True:
        a, b = r.randint(2, 9), r.randint(1, 8)
        if a > b: break
    s2, p = a * a + b * b, a * b; ask = r.choice(['+', '-']); v = a + b if ask == '+' else a - b
    return dict(en='Given \\(a>b>0\\), \\(a^2+b^2=%d\\) and \\(ab=%d\\). Find \\(a%sb\\).' % (s2, p, ask), vi='Cho \\(a>b>0\\) thỏa mãn \\(a^2+b^2=%d\\) và \\(ab=%d\\). Tính \\(a%sb\\).' % (s2, p, ask),
                opts=nopts(r, v, [a - b if ask == '+' else a + b, s2 + 2 * p if ask == '+' else s2 - 2 * p, v + 1]), ans=0,
                ee='\\((a%sb)^2=a^2+b^2%s2ab=%d\\) and \\(a%sb>0\\), so \\(a%sb=%d\\).' % (ask, ask, v * v, ask, ask, v),
                ev='\\((a%sb)^2=a^2+b^2%s2ab=%d\\) mà \\(a%sb>0\\) nên \\(a%sb=%d\\).' % (ask, ask, v * v, ask, ask, v))

def b6_d4_garden(r, lv):
    k = r.randint(1, 5); x = r.randint(6, 20); inc = 2 * k * x + k * k
    return dict(en='A square garden has side \\(x\\) m. Each side is increased by %d m, and the area increases by %d m². Find \\(x\\).' % (k, inc),
                vi='Một mảnh vườn hình vuông cạnh \\(x\\) m. Người ta mở rộng mỗi cạnh thêm %d m thì diện tích tăng thêm %d m². Tìm \\(x\\).' % (k, inc),
                opts=nopts(r, x, [F(inc, 2 * k), x + k, F(inc - k * k, k)]), ans=0,
                ee='\\((x+%d)^2-x^2=%dx+%d=%d\\Rightarrow x=%d\\).' % (k, 2 * k, k * k, inc, x), ev='\\((x+%d)^2-x^2=%dx+%d=%d\\Rightarrow x=%d\\).' % (k, 2 * k, k * k, inc, x))

def b6_d4_min(r, lv):
    a, c = r.randint(1, 9), r.randint(1, 15); P = Poly.of([(1, (2, 0, 0)), (-2 * a, XV), (a * a + c, (0, 0, 0))])
    return dict(en='Find the smallest value of \\(P=%s\\).' % P.tex(), vi='Tìm giá trị nhỏ nhất của biểu thức \\(P=%s\\).' % P.tex(), opts=nopts(r, c, [a * a + c, a, -c]), ans=0,
                ee='\\(P=(x-%d)^2+%d\\ge %d\\); equality at \\(x=%d\\).' % (a, c, c, a), ev='\\(P=(x-%d)^2+%d\\ge %d\\); dấu bằng xảy ra khi \\(x=%d\\).' % (a, c, c, a))

L6_GROUPS = [[('mcq', b6_expand), ('mcq', b6_dsq), ('mcq', b6_identity)], [('tf', b6_tf_sq), ('tf', b6_tf_dsq)], [('short', b6_short_fast), ('short', b6_short_mid)],
             [('mcq', b6_d1_formula), ('mcq', b6_d1_read), ('mcq', b6_d1_AB)], [('mcq', b6_d2_exp), ('mcq', b6_d2_conj), ('mcq', b6_d2_tosq)],
             [('mcq', b6_d3_simp), ('mcq', b6_d3_val), ('mcq', b6_d3_fast)], [('mcq', b6_d4_ab), ('mcq', b6_d4_garden), ('mcq', b6_d4_min)]]

# ----------------------------------------------------------------------------------- BÀI 7
def b7_exp(r, lv, s=None):
    a = r.randint(1, 3); b = r.randint(1, 5); s = s or r.choice([1, -1]); P = L(a, s * b); R = P * P * P
    A, B = M(a, XV), M(s * b, (0, 0, 0))
    w1 = A * A * A + B * B * B; w2 = A * A * A + 3 * A * A * B + 3 * A * B * B * -1 + B * B * B; w3 = A * A * A + A * A * B + A * B * B + B * B * B
    return dict(en='Expand \\(%s\\).' % cb(P), vi='Khai triển \\(%s\\).' % cb(P), opts=tpoly(r, R, [w1, w2, w3, A * A * A + 3 * A * B * B + B * B * B]), ans=0,
                ee='\\((A%sB)^3=A^3%s3A^2B+3AB^2%sB^3\\): \\(%s\\).' % ('+' if s > 0 else '-', '+' if s > 0 else '-', '+' if s > 0 else '-', R.tex()),
                ev='\\((A%sB)^3=A^3%s3A^2B+3AB^2%sB^3\\): \\(%s\\).' % ('+' if s > 0 else '-', '+' if s > 0 else '-', '+' if s > 0 else '-', R.tex()))
def b7_exp_sum(r, lv): return b7_exp(r, lv, 1)
def b7_exp_diff(r, lv): return b7_exp(r, lv, -1)

def b7_tocube(r, lv):
    a, b = r.randint(1, 3), r.randint(1, 5)
    if gcd(a, b) > 1: raise AssertionError
    s = r.choice([1, -1]); P = L(a, s * b); R = P * P * P
    good = cb(P); bads = [cb(L(a, -s * b)), cb(L(a, s * b * 3)) if b < 4 else cb(L(a, s * (b + 1))), '(%s)^3' % L(a * a * a, s * b * b * b).tex() if a > 1 or b > 1 else cb(L(1, s * 2))]
    bads = [x for x in dict.fromkeys(bads) if x != good]
    return dict(en='Write \\(%s\\) as a cube.' % R.tex(), vi='Viết đa thức \\(%s\\) dưới dạng lập phương của một tổng hoặc một hiệu.' % R.tex(), opts=pick_opts(r, good, bads, fill=lambda t: cb(L(a, s * (b + t + 1)))), ans=0,
                ee='\\(%s=%s\\).' % (R.tex(), good), ev='\\(%s=%s\\).' % (R.tex(), good))

def b7_tf_cube(r, lv):
    a = r.randint(1, 6); s = r.choice([1, -1]); truth = r.random() < .5; P = L(1, s * a); R = P * P * P
    claim = R if truth else Poly.of([(1, (3, 0, 0)), (s * a ** 3, (0, 0, 0))])
    return dict(en='\\(%s=%s\\).' % (cb(P), claim.tex()), vi='\\(%s=%s\\).' % (cb(P), claim.tex()), ans=(claim == R), ee='\\(%s=%s\\).' % (cb(P), R.tex()), ev='\\(%s=%s\\).' % (cb(P), R.tex()))

def b7_tf_sign(r, lv):
    a = r.randint(1, 9); k = r.choice([2, 3]); truth = r.random() < .5
    lhs = '(x-%d)^%d' % (a, k); rhs = ('-(%d-x)^%d' if (k == 3) == truth else '(%d-x)^%d') % (a, k)
    real = (k == 2 and not rhs.startswith('-')) or (k == 3 and rhs.startswith('-'))
    return dict(en='\\(%s=%s\\) for every \\(x\\).' % (lhs, rhs), vi='\\(%s=%s\\) với mọi \\(x\\).' % (lhs, rhs), ans=real,
                ee='\\((A-B)^2=(B-A)^2\\) but \\((A-B)^3=-(B-A)^3\\).', ev='\\((A-B)^2=(B-A)^2\\) nhưng \\((A-B)^3=-(B-A)^3\\).')

def b7_short_val(r, lv):
    a = r.randint(1, 5); s = r.choice([1, -1]); base = r.choice([10, 20, 100]); x = base - s * a
    R = L(1, s * a) * L(1, s * a) * L(1, s * a); v = base ** 3
    return dict(en='Find the value of \\(%s\\) at \\(x=%d\\).' % (R.tex(), x), vi='Tính giá trị của biểu thức \\(%s\\) tại \\(x=%d\\).' % (R.tex(), x), key=str(v),
                ee='\\(=(x%s%d)^3=%d^3=%d\\).' % ('+' if s > 0 else '-', a, base, v), ev='\\(=(x%s%d)^3=%d^3=%d\\).' % ('+' if s > 0 else '-', a, base, v))

def b7_short_coef(r, lv):
    a, b = r.randint(1, 3), r.randint(1, 4); s = r.choice([1, -1]); P = L(a, s * b); R = P * P * P; k = r.choice([1, 2])
    return dict(en='In the expansion of \\(%s\\), what is the coefficient of \\(%s\\)?' % (cb(P), vpart((k, 0, 0))), vi='Trong khai triển của \\(%s\\), hệ số của \\(%s\\) là bao nhiêu?' % (cb(P), vpart((k, 0, 0))),
                key=num(R[(k, 0, 0)]), ee='\\(%s=%s\\).' % (cb(P), R.tex()), ev='\\(%s=%s\\).' % (cb(P), R.tex()))

CUBE_FORMS = [('(A+B)^3', 'A^3+3A^2B+3AB^2+B^3', ['A^3+B^3', 'A^3+3AB+B^3', 'A^3-3A^2B+3AB^2-B^3'], 'the cube of a sum', 'lập phương của một tổng'),
              ('(A-B)^3', 'A^3-3A^2B+3AB^2-B^3', ['A^3-B^3', 'A^3-3A^2B-3AB^2-B^3', 'A^3+3A^2B+3AB^2-B^3'], 'the cube of a difference', 'lập phương của một hiệu')]
def b7_d1_formula(r, lv):
    lhs, good, bads, en, vi = PICK(r, CUBE_FORMS); form = r.choice([0, 1])
    q = (('Complete the identity (%s): \\(%s=\\,?\\)' % (en, lhs), 'Hoàn thành hằng đẳng thức (%s): \\(%s=\\,?\\)' % (vi, lhs)) if form == 0 else
         ('Which expression is equal to \\(%s\\)?' % lhs, 'Biểu thức nào bằng \\(%s\\)?' % lhs))
    return dict(en=q[0], vi=q[1], opts=[good] + bads, ans=0, ee='\\(%s=%s\\).' % (lhs, good), ev='\\(%s=%s\\).' % (lhs, good))

def b7_d1_const(r, lv):
    a = r.randint(2, 6); s = r.choice([1, -1]); P = L(1, s * a); c = (s * a) ** 3
    return dict(en='What is the constant term in the expansion of \\(%s\\)?' % cb(P), vi='Hạng tử tự do (không chứa \\(x\\)) trong khai triển của \\(%s\\) là' % cb(P),
                opts=nopts(r, c, [-c, s * 3 * a, s * a]), ans=0, ee='It is \\(B^3=(%d)^3=%d\\).' % (s * a, c), ev='Đó là \\(B^3=(%d)^3=%d\\).' % (s * a, c))

def b7_d1_AB(r, lv):
    a, b = r.randint(2, 4), r.randint(1, 5); s = r.choice([1, -1]); R = L(a, s * b) * L(a, s * b) * L(a, s * b)
    good = 'A=%dx,\\ B=%d' % (a, b); bads = ['A=%dx,\\ B=%d' % (a ** 3, b ** 3), 'A=%dx,\\ B=%d' % (a, b ** 3), 'A=x,\\ B=%d' % b]
    return dict(en='Write \\(%s\\) in the form \\((A%sB)^3\\). Then…' % (R.tex(), '+' if s > 0 else '-'), vi='Viết \\(%s\\) dưới dạng \\((A%sB)^3\\). Khi đó' % (R.tex(), '+' if s > 0 else '-'),
                opts=pick_opts(r, good, bads), ans=0, ee='\\(A^3=%dx^3\\Rightarrow A=%dx\\); \\(B^3=%d\\Rightarrow B=%d\\).' % (a ** 3, a, b ** 3, b), ev='\\(A^3=%dx^3\\Rightarrow A=%dx\\); \\(B^3=%d\\Rightarrow B=%d\\).' % (a ** 3, a, b ** 3, b))

def b7_d2_two(r, lv):
    a, b = r.randint(1, 3), r.randint(1, 3); s = r.choice([1, -1]); P = Poly.of([(a, XV), (s * b, YV)]); R = P * P * P
    A, B = M(a, XV), M(s * b, YV)
    return dict(en='Expand \\(%s\\).' % cb(P), vi='Khai triển \\(%s\\).' % cb(P), opts=tpoly(r, R, [A * A * A + B * B * B, A * A * A + 3 * A * B + B * B * B if False else A * A * A + 3 * A * A * B - 3 * A * B * B + B * B * B, A * A * A + A * A * B + A * B * B + B * B * B]), ans=0,
                ee='\\(%s\\).' % R.tex(), ev='\\(%s\\).' % R.tex())

def b7_d2_tocube(r, lv):
    q = b7_tocube(r, lv); q['en'] = q['en'].replace('Write', 'Which cube equals').replace(' as a cube.', '?'); q['vi'] = q['vi'].replace('Viết đa thức', 'Đa thức').replace(' dưới dạng lập phương của một tổng hoặc một hiệu.', ' bằng'); return q

def b7_d2_coef(r, lv):
    a, b = r.randint(2, 3), r.randint(1, 4); s = r.choice([1, -1]); P = L(a, s * b); R = P * P * P
    c = R[(2, 0, 0)]
    return dict(en='What is the coefficient of \\(x^2\\) in the expansion of \\(%s\\)?' % cb(P), vi='Hệ số của \\(x^2\\) trong khai triển của \\(%s\\) là' % cb(P),
                opts=nopts(r, c, [s * 3 * a * b, a * a * s * b, -c]), ans=0, ee='\\(3A^2B=3\\cdot(%dx)^2\\cdot(%d)=%s\\).' % (a, s * b, mtex(c, (2, 0, 0))), ev='\\(3A^2B=3\\cdot(%dx)^2\\cdot(%d)=%s\\).' % (a, s * b, mtex(c, (2, 0, 0))))

def b7_d3_val(r, lv):
    a = r.randint(1, 4); s = r.choice([1, -1]); base = r.choice([10, 20, 30]); x = base - s * a; R = L(1, s * a) * L(1, s * a) * L(1, s * a); v = base ** 3
    return dict(en='Write \\(%s\\) as a cube and evaluate it at \\(x=%d\\).' % (R.tex(), x), vi='Viết biểu thức \\(%s\\) dưới dạng lập phương rồi tính giá trị tại \\(x=%d\\).' % (R.tex(), x),
                opts=nopts(r, v, [x ** 3, (x + s * a) ** 3 + 1, base ** 2], step=1000), ans=0, ee='\\((x%s%d)^3=%d^3=%d\\).' % ('+' if s > 0 else '-', a, base, v), ev='\\((x%s%d)^3=%d^3=%d\\).' % ('+' if s > 0 else '-', a, base, v))

def b7_d3_indep(r, lv):
    a = r.randint(1, 4); P1, P2 = L(1, a), L(1, -a); D = P1 * P1 * P1 - P2 * P2 * P2   # = 6a x^2 + 2a^3
    k = 6 * a; c = 2 * a ** 3
    t = '%s-%s-%dx^2' % (cb(P1), cb(P2), k)
    return dict(en='Show that \\(%s\\) does not depend on \\(x\\). Its value is…' % t, vi='Biểu thức \\(%s\\) không phụ thuộc vào \\(x\\) và có giá trị bằng' % t,
                opts=nopts(r, c, [0, a ** 3, 2 * a]), ans=0, ee='\\(%s-%s=%s\\), so the expression equals \\(%d\\).' % (cb(P1), cb(P2), D.tex(), c), ev='\\(%s-%s=%s\\) nên biểu thức bằng \\(%d\\).' % (cb(P1), cb(P2), D.tex(), c))

def b7_d3_fast(r, lv):
    base, k = r.choice([10, 20, 100]), 1; s = r.choice([1, -1]); n = base + s * k; v = n ** 3
    return dict(en='Calculate \\(%d^3\\) using \\((A%sB)^3\\).' % (n, '+' if s > 0 else '-'), vi='Tính \\(%d^3\\) bằng hằng đẳng thức \\((A%sB)^3\\).' % (n, '+' if s > 0 else '-'),
                opts=nopts(r, v, [base ** 3 + s * 1, base ** 3 + s * 3 * base * base, v + 2 * base]), ans=0,
                ee='\\((%d%s1)^3=%d%s%d+%d%s1=%d\\).' % (base, '+' if s > 0 else '-', base ** 3, '+' if s > 0 else '-', 3 * base * base, 3 * base, '+' if s > 0 else '-', v),
                ev='\\((%d%s1)^3=%d%s%d+%d%s1=%d\\).' % (base, '+' if s > 0 else '-', base ** 3, '+' if s > 0 else '-', 3 * base * base, 3 * base, '+' if s > 0 else '-', v))

def b7_d4_grow(r, lv):
    x, k = r.randint(4, 12), r.randint(1, 3); inc = (x + k) ** 3 - x ** 3; P = L(1, k) * L(1, k) * L(1, k) - M(1, (3, 0, 0))
    return dict(en='A cube has edge \\(x\\) cm. Each edge is increased by %d cm. Write the increase of its volume as a polynomial and evaluate it for \\(x=%d\\).' % (k, x),
                vi='Một khối lập phương có cạnh \\(x\\) cm. Người ta tăng mỗi cạnh thêm %d cm. Viết đa thức biểu thị phần thể tích tăng thêm và tính giá trị khi \\(x=%d\\).' % (k, x),
                opts=pick_opts(r, '%s;\\ %d\\text{ cm}^3' % (P.tex(), inc), ['%d;\\ %d\\text{ cm}^3' % (k ** 3, k ** 3), '%s;\\ %d\\text{ cm}^3' % ((P - M(3 * k * k, XV)).tex(), inc - 3 * k * k * x), '%s;\\ %d\\text{ cm}^3' % ((L(1, k) * L(1, k) * L(1, k)).tex(), (x + k) ** 3)]), ans=0,
                ee='\\((x+%d)^3-x^3=%s\\); at \\(x=%d\\): \\(%d\\) cm³.' % (k, P.tex(), x, inc), ev='\\((x+%d)^3-x^3=%s\\); khi \\(x=%d\\): \\(%d\\) cm³.' % (k, P.tex(), x, inc))

def b7_d4_sum(r, lv):
    a, b = r.sample(range(1, 9), 2); s, p = a + b, a * b; v = a ** 3 + b ** 3
    return dict(en='Use \\((a+b)^3=a^3+b^3+3ab(a+b)\\): given \\(a+b=%d\\) and \\(ab=%d\\), find \\(a^3+b^3\\).' % (s, p), vi='Sử dụng \\((a+b)^3=a^3+b^3+3ab(a+b)\\): cho \\(a+b=%d\\) và \\(ab=%d\\), tính \\(a^3+b^3\\).' % (s, p),
                opts=nopts(r, v, [s ** 3, s ** 3 + 3 * p * s, s ** 3 - p * s]), ans=0, ee='\\(a^3+b^3=%d^3-3\\cdot%d\\cdot%d=%d\\).' % (s, p, s, v), ev='\\(a^3+b^3=%d^3-3\\cdot%d\\cdot%d=%d\\).' % (s, p, s, v))

def b7_d4_cut(r, lv):
    x, k = r.randint(8, 15), r.randint(1, 3); d = x ** 3 - (x - k) ** 3
    return dict(en='A wooden cube has edge \\(x\\) cm. It is cut down so that each edge is %d cm shorter. By how much does the volume decrease when \\(x=%d\\)?' % (k, x),
                vi='Một khối gỗ hình lập phương cạnh \\(x\\) cm được gọt bớt để mỗi cạnh ngắn đi %d cm. Thể tích khối gỗ giảm bao nhiêu khi \\(x=%d\\)?' % (k, x),
                opts=pick_opts(r, '%d\\text{ cm}^3' % d, ['%d\\text{ cm}^3' % (k ** 3), '%d\\text{ cm}^3' % ((x - k) ** 3), '%d\\text{ cm}^3' % (3 * k * x * x)]), ans=0,
                ee='\\(x^3-(x-%d)^3=%d^3-%d^3=%d\\) cm³.' % (k, x, x - k, d), ev='\\(x^3-(x-%d)^3=%d^3-%d^3=%d\\) cm³.' % (k, x, x - k, d))

L7_GROUPS = [[('mcq', b7_exp_sum), ('mcq', b7_exp_diff), ('mcq', b7_tocube)], [('tf', b7_tf_cube), ('tf', b7_tf_sign)], [('short', b7_short_val), ('short', b7_short_coef)],
             [('mcq', b7_d1_formula), ('mcq', b7_d1_const), ('mcq', b7_d1_AB)], [('mcq', b7_d2_two), ('mcq', b7_d2_tocube), ('mcq', b7_d2_coef)],
             [('mcq', b7_d3_val), ('mcq', b7_d3_indep), ('mcq', b7_d3_fast)], [('mcq', b7_d4_grow), ('mcq', b7_d4_sum), ('mcq', b7_d4_cut)]]

# ----------------------------------------------------------------------------------- BÀI 8
def _cubes(r, two=False, hi=3):
    a, b = r.randint(1, hi), r.randint(1, 5)
    A = M(a, XV); B = M(b, YV) if two else M(b, (0, 0, 0))
    return A, B

def tri(A, B, s):
    """A² ∓ AB + B² (s=+1 cho tổng hai lập phương: dấu trừ ở giữa)."""
    return A * A - s * A * B + B * B

def b8_expand(r, lv):
    A, B = _cubes(r, r.random() < .3); s = r.choice([1, -1]); R = A * A * A + s * B * B * B
    t = '%s%s' % (br(A + s * B), br(tri(A, B, s)))
    return dict(en='Find the product \\(%s\\).' % t, vi='Tính \\(%s\\).' % t, opts=tpoly(r, R, [A * A * A - s * B * B * B, (A + s * B) * (A + s * B) * (A + s * B), A * A * A + s * B * B]), ans=0,
                ee='It is the %s of two cubes: \\(%s\\).' % ('sum' if s > 0 else 'difference', R.tex()), ev='Đây là %s hai lập phương: \\(%s\\).' % ('tổng' if s > 0 else 'hiệu', R.tex()))

def _fac_opts(r, A, B, s):
    good = '%s%s' % (br(A + s * B), br(tri(A, B, s)))
    bads = ['%s%s' % (br(A + s * B), br(tri(A, B, -s))), '%s%s' % (br(A - s * B), br(tri(A, B, s))), '%s%s' % (br(A + s * B), br(A * A + B * B))]
    return good, bads

def b8_fac(r, lv, s=None):
    A, B = _cubes(r, r.random() < .3)
    if gcd(int(list(A.values())[0]), int(list(B.values())[0])) > 1: raise AssertionError
    s = s or r.choice([1, -1]); P = A * A * A + s * B * B * B
    good, bads = _fac_opts(r, A, B, s)
    return dict(en='Write \\(%s\\) as a product.' % P.tex(), vi='Viết đa thức \\(%s\\) dưới dạng tích.' % P.tex(), opts=pick_opts(r, good, bads), ans=0,
                ee='\\(A^3%sB^3=(A%sB)(A^2%sAB+B^2)\\) with \\(A=%s,\\ B=%s\\).' % ('+' if s > 0 else '-', '+' if s > 0 else '-', '-' if s > 0 else '+', A.tex(), B.tex()),
                ev='\\(A^3%sB^3=(A%sB)(A^2%sAB+B^2)\\) với \\(A=%s,\\ B=%s\\).' % ('+' if s > 0 else '-', '+' if s > 0 else '-', '-' if s > 0 else '+', A.tex(), B.tex()))
def b8_fac_diff(r, lv): return b8_fac(r, lv, -1)
def b8_fac_sum(r, lv):
    q = b8_fac(r, lv, 1); q['en'] = q['en'].replace('Write', 'Factor').replace(' as a product.', '.'); q['vi'] = q['vi'].replace('Viết đa thức', 'Phân tích đa thức').replace(' dưới dạng tích.', ' thành tích.'); return q

def b8_tf_prod(r, lv):
    a = r.randint(1, 9); s = r.choice([1, -1]); truth = r.random() < .5; A, B = M(1, XV), M(a, (0, 0, 0))
    t2 = tri(A, B, s) if truth else tri(A, B, -s); R = A * A * A + s * B * B * B
    return dict(en='\\(%s%s=%s\\).' % (br(A + s * B), br(t2), R.tex()), vi='\\(%s%s=%s\\).' % (br(A + s * B), br(t2), R.tex()), ans=((A + s * B) * t2 == R),
                ee='\\(%s%s=%s\\).' % (br(A + s * B), br(tri(A, B, s)), R.tex()), ev='\\(%s%s=%s\\).' % (br(A + s * B), br(tri(A, B, s)), R.tex()))

def b8_tf_cube(r, lv):
    a = r.randint(1, 6); s = r.choice([1, -1]); truth = r.random() < .5; P = Poly.of([(1, (3, 0, 0)), (s * a ** 3, (0, 0, 0))])
    claim = '(x%s%d)(x^2%s%dx+%d)' % ('+' if s > 0 else '-', a, '-' if s > 0 else '+', a, a * a) if truth else '(x%s%d)^3' % ('+' if s > 0 else '-', a)
    return dict(en='\\(%s=%s\\).' % (P.tex(), claim), vi='\\(%s=%s\\).' % (P.tex(), claim), ans=truth,
                ee='\\(%s=(x%s%d)(x^2%s%dx+%d)\\); note \\((x%s%d)^3\\ne %s\\).' % (P.tex(), '+' if s > 0 else '-', a, '-' if s > 0 else '+', a, a * a, '+' if s > 0 else '-', a, P.tex()),
                ev='\\(%s=(x%s%d)(x^2%s%dx+%d)\\); chú ý \\((x%s%d)^3\\ne %s\\).' % (P.tex(), '+' if s > 0 else '-', a, '-' if s > 0 else '+', a, a * a, '+' if s > 0 else '-', a, P.tex()))

def b8_short_ab(r, lv):
    a, b = r.sample(range(1, 8), 2); s = r.choice([1, -1])
    if s < 0 and a < b: a, b = b, a
    if s > 0: v = a ** 3 + b ** 3; en = 'Given \\(a+b=%d\\) and \\(ab=%d\\), find \\(a^3+b^3\\).' % (a + b, a * b); vi = 'Cho \\(a+b=%d\\) và \\(ab=%d\\). Tính \\(a^3+b^3\\).' % (a + b, a * b)
    else: v = a ** 3 - b ** 3; en = 'Given \\(a-b=%d\\) and \\(ab=%d\\), find \\(a^3-b^3\\).' % (a - b, a * b); vi = 'Cho \\(a-b=%d\\) và \\(ab=%d\\). Tính \\(a^3-b^3\\).' % (a - b, a * b)
    if s > 0: e = '\\(a^3+b^3=(a+b)^3-3ab(a+b)=%d\\).' % v
    else: e = '\\(a^3-b^3=(a-b)^3+3ab(a-b)=%d\\).' % v
    return dict(en=en, vi=vi, key=str(v), ee=e, ev=e)

def b8_short_const(r, lv):
    a = r.randint(1, 6); s = r.choice([1, -1]); A, B = M(1, XV), M(a, (0, 0, 0)); c = s * a ** 3
    t = '%s%s-x^3' % (br(A + s * B), br(tri(A, B, s)))
    return dict(en='Simplify \\(%s\\). What number do you get?' % t, vi='Rút gọn biểu thức \\(%s\\). Kết quả là số nào?' % t, key=str(c),
                ee='\\(=x^3%s%d-x^3=%d\\).' % ('+' if s > 0 else '-', a ** 3, c), ev='\\(=x^3%s%d-x^3=%d\\).' % ('+' if s > 0 else '-', a ** 3, c))

SC_FORMS = [('A^3+B^3', '(A+B)(A^2-AB+B^2)', ['(A+B)(A^2+AB+B^2)', '(A+B)^3', '(A-B)(A^2-AB+B^2)'], 'the sum of two cubes', 'tổng hai lập phương'),
            ('A^3-B^3', '(A-B)(A^2+AB+B^2)', ['(A-B)(A^2-AB+B^2)', '(A-B)^3', '(A+B)(A^2+AB+B^2)'], 'the difference of two cubes', 'hiệu hai lập phương')]
def b8_d1_formula(r, lv):
    lhs, good, bads, en, vi = PICK(r, SC_FORMS); form = r.choice([0, 1])
    q = (('Complete the identity (%s): \\(%s=\\,?\\)' % (en, lhs), 'Hoàn thành hằng đẳng thức (%s): \\(%s=\\,?\\)' % (vi, lhs)) if form == 0 else
         ('Which product is equal to \\(%s\\)?' % lhs, 'Tích nào bằng \\(%s\\)?' % lhs))
    return dict(en=q[0], vi=q[1], opts=[good] + bads, ans=0, ee='\\(%s=%s\\).' % (lhs, good), ev='\\(%s=%s\\).' % (lhs, good))

def b8_d1_fill(r, lv):
    a = r.randint(2, 9); s = r.choice([1, -1]); A, B = M(1, XV), M(a, (0, 0, 0)); P = A * A * A + s * B * B * B
    good = tri(A, B, s); bads = [tri(A, B, -s), A * A + B * B, (A + s * B) * (A + s * B)]
    return dict(en='Fill in the missing factor: \\(%s=%s\\cdot(\\ \\dots\\ )\\).' % (P.tex(), br(A + s * B)), vi='Điền đa thức thích hợp vào chỗ trống: \\(%s=%s\\cdot(\\ \\dots\\ )\\).' % (P.tex(), br(A + s * B)),
                opts=tpoly(r, good, bads), ans=0, ee='The missing factor is \\(%s\\).' % good.tex(), ev='Đa thức cần điền là \\(%s\\).' % good.tex())

def b8_d1_read(r, lv):
    forms = [('A^3+B^3', 'the sum of two cubes', 'tổng hai lập phương'), ('A^3-B^3', 'the difference of two cubes', 'hiệu hai lập phương'),
             ('(A+B)^3', 'the cube of a sum', 'lập phương của một tổng'), ('(A-B)^3', 'the cube of a difference', 'lập phương của một hiệu')]
    i = r.randrange(4); o = [tx(forms[i][1], forms[i][2])] + [tx(f[1], f[2]) for j, f in enumerate(forms) if j != i]
    return dict(en='How do we read \\(%s\\)?' % forms[i][0], vi='Biểu thức \\(%s\\) được gọi là' % forms[i][0], opts=o, ans=0, ee='\\(%s\\) is %s.' % (forms[i][0], forms[i][1]), ev='\\(%s\\) là %s.' % (forms[i][0], forms[i][2]))

def b8_d2_fac2(r, lv):
    A, B = _cubes(r, True)
    if gcd(int(list(A.values())[0]), int(list(B.values())[0])) > 1: raise AssertionError
    s = r.choice([1, -1]); P = A * A * A + s * B * B * B; good, bads = _fac_opts(r, A, B, s)
    return dict(en='Factor \\(%s\\).' % P.tex(), vi='Phân tích đa thức \\(%s\\) thành nhân tử.' % P.tex(), opts=pick_opts(r, good, bads), ans=0, ee='\\(%s=%s\\).' % (P.tex(), good), ev='\\(%s=%s\\).' % (P.tex(), good))

def b8_d2_exp(r, lv):
    A, B = _cubes(r, True); s = r.choice([1, -1]); R = A * A * A + s * B * B * B
    t = '%s%s' % (br(A + s * B), br(tri(A, B, s)))
    return dict(en='Expand \\(%s\\).' % t, vi='Thực hiện phép nhân \\(%s\\).' % t, opts=tpoly(r, R, [A * A * A - s * B * B * B, (A + s * B) * (A + s * B) * (A + s * B), A * A * A + s * 3 * A * B * B * 0 + s * B * B]), ans=0,
                ee='\\(=%s\\).' % R.tex(), ev='\\(=%s\\).' % R.tex())

def b8_d2_diff2(r, lv):
    a = r.randint(1, 6); A, B = M(1, XV), M(a, (0, 0, 0)); R = (A + B) * tri(A, B, 1) - (A - B) * tri(A, B, -1)
    t = '%s%s-%s%s' % (br(A + B), br(tri(A, B, 1)), br(A - B), br(tri(A, B, -1)))
    return dict(en='Simplify \\(%s\\).' % t, vi='Rút gọn biểu thức \\(%s\\).' % t, opts=tpoly(r, R, [M(0, XV) + M(2, (3, 0, 0)), M(0, XV) + M(a ** 3, (0, 0, 0)), M(0, XV) + M(-2 * a ** 3, (0, 0, 0))]), ans=0,
                ee='\\((x^3+%d)-(x^3-%d)=%d\\).' % (a ** 3, a ** 3, 2 * a ** 3), ev='\\((x^3+%d)-(x^3-%d)=%d\\).' % (a ** 3, a ** 3, 2 * a ** 3))

def b8_d3_ab(r, lv):
    while True:
        a, b = r.randint(2, 9), r.randint(1, 8)
        if a > b: break
    v = a ** 3 - b ** 3; d, p = a - b, a * b
    return dict(en='Given \\(a-b=%d\\) and \\(ab=%d\\), find \\(a^3-b^3\\).' % (d, p), vi='Cho \\(a-b=%d\\) và \\(ab=%d\\). Tính \\(a^3-b^3\\).' % (d, p),
                opts=nopts(r, v, [d ** 3, d ** 3 - 3 * p * d, d * p]), ans=0, ee='\\(a^3-b^3=(a-b)^3+3ab(a-b)=%d+%d=%d\\).' % (d ** 3, 3 * p * d, v), ev='\\(a^3-b^3=(a-b)^3+3ab(a-b)=%d+%d=%d\\).' % (d ** 3, 3 * p * d, v))

def b8_d3_val(r, lv):
    a, k = r.randint(1, 4), r.randint(2, 6); A, B = M(1, XV), M(a, (0, 0, 0))
    R = (A - B) * tri(A, B, -1) - M(1, XV) * Poly.of([(1, (2, 0, 0)), (-k, (0, 0, 0))])     # = kx - a^3
    x = nz(r, -6, 6); v = R.at(x)
    t = '%s%s-x(x^2-%d)' % (br(A - B), br(tri(A, B, -1)), k)
    return dict(en='Simplify \\(A=%s\\), then find its value at \\(x=%d\\).' % (t, x), vi='Rút gọn biểu thức \\(A=%s\\) rồi tính giá trị tại \\(x=%d\\).' % (t, x),
                opts=nopts(r, v, [k * x + a ** 3, -v, v - k]), ans=0, ee='\\(A=%s\\), so \\(A=%d\\).' % (R.tex(), v), ev='\\(A=%s\\) nên \\(A=%d\\).' % (R.tex(), v))

def b8_d3_x(r, lv):
    a, k = r.randint(1, 3), r.randint(2, 6); x = nz(r, -6, 6); A, B = M(1, XV), M(a, (0, 0, 0))
    c = a ** 3 + k * x    # (x+a)(x^2-ax+a^2) - x(x^2-k) = a^3 + kx
    t = '%s%s-x(x^2-%d)=%d' % (br(A + B), br(tri(A, B, 1)), k, c)
    return dict(en='Find \\(x\\), given that \\(%s\\).' % t, vi='Tìm \\(x\\), biết \\(%s\\).' % t, opts=nopts(r, x, [-x, F(c, k), F(c + a ** 3, k)]), ans=0,
                ee='\\(x^3+%d-x^3+%dx=%d\\Rightarrow %dx=%d\\Rightarrow x=%d\\).' % (a ** 3, k, c, k, c - a ** 3, x), ev='\\(x^3+%d-x^3+%dx=%d\\Rightarrow %dx=%d\\Rightarrow x=%d\\).' % (a ** 3, k, c, k, c - a ** 3, x))

def b8_d4_tank(r, lv):
    k = r.randint(1, 3); x = r.randint(k + 6, 15); v = x ** 3 - k ** 3
    good = '(x-%d)(x^2+%sx+%d);\\ %d' % (k, '' if k == 1 else k, k * k, v)
    bads = ['(x-%d)(x^2-%sx+%d);\\ %d' % (k, '' if k == 1 else k, k * k, (x - k) * (x * x - k * x + k * k)), '(x-%d)^3;\\ %d' % (k, (x - k) ** 3), '(x-%d)(x^2+%sx+%d);\\ %d' % (k, '' if k == 1 else k, k * k, v + k ** 3 * 2)]
    return dict(en='A cube-shaped tank has edge \\(x\\) dm. A cube-shaped stone block with edge %d dm lies at the bottom. The amount of water needed to fill the tank is \\(x^3-%d\\) liters. Write it as a product and find it when \\(x=%d\\).' % (k, k ** 3, x),
                vi='Một bể nước hình lập phương cạnh \\(x\\) dm, dưới đáy có đặt một khối đá hình lập phương cạnh %d dm. Lượng nước cần đổ để đầy bể là \\(x^3-%d\\) (lít). Viết biểu thức đó dưới dạng tích và tính giá trị khi \\(x=%d\\).' % (k, k ** 3, x),
                opts=pick_opts(r, good, bads), ans=0, ee='\\(x^3-%d=(x-%d)(x^2+%sx+%d)\\); at \\(x=%d\\): %d liters.' % (k ** 3, k, '' if k == 1 else k, k * k, x, v),
                ev='\\(x^3-%d=(x-%d)(x^2+%sx+%d)\\); khi \\(x=%d\\): %d lít.' % (k ** 3, k, '' if k == 1 else k, k * k, x, v))

def b8_d4_two(r, lv):
    a, b = r.sample(range(2, 10), 2); v = a ** 3 + b ** 3
    return dict(en='Two cubes have edges \\(a\\) cm and \\(b\\) cm with \\(a+b=%d\\) and \\(ab=%d\\). Find their total volume.' % (a + b, a * b), vi='Hai khối lập phương có cạnh \\(a\\) cm và \\(b\\) cm, biết \\(a+b=%d\\) và \\(ab=%d\\). Tính tổng thể tích của hai khối.' % (a + b, a * b),
                opts=pick_opts(r, '%d\\text{ cm}^3' % v, ['%d\\text{ cm}^3' % (a + b) ** 3, '%d\\text{ cm}^3' % ((a + b) ** 3 - a * b * (a + b)), '%d\\text{ cm}^3' % ((a + b) ** 3 + 3 * a * b * (a + b))]), ans=0,
                ee='\\(a^3+b^3=(a+b)^3-3ab(a+b)=%d\\) cm³.' % v, ev='\\(a^3+b^3=(a+b)^3-3ab(a+b)=%d\\) cm³.' % v)

def b8_d4_shell(r, lv):
    x = r.randint(3, 12); v = (x + 1) ** 3 - (x - 1) ** 3
    return dict(en='A hollow cube box has outer edge \\((x+1)\\) cm and inner edge \\((x-1)\\) cm. The volume of its walls is \\((x+1)^3-(x-1)^3\\). Find this volume when \\(x=%d\\).' % x,
                vi='Một chiếc hộp hình lập phương rỗng có cạnh ngoài \\((x+1)\\) cm và cạnh trong \\((x-1)\\) cm. Thể tích phần vỏ hộp là \\((x+1)^3-(x-1)^3\\). Tính thể tích đó khi \\(x=%d\\).' % x,
                opts=pick_opts(r, '%d\\text{ cm}^3' % v, ['%d\\text{ cm}^3' % (2 * x ** 3), '%d\\text{ cm}^3' % (6 * x * x), '%d\\text{ cm}^3' % 2]), ans=0,
                ee='\\(A^3-B^3=(A-B)(A^2+AB+B^2)=2(3x^2+1)=6x^2+2=%d\\) cm³.' % v, ev='\\(A^3-B^3=(A-B)(A^2+AB+B^2)=2(3x^2+1)=6x^2+2=%d\\) cm³.' % v)

L8_GROUPS = [[('mcq', b8_expand), ('mcq', b8_fac_diff), ('mcq', b8_fac_sum)], [('tf', b8_tf_prod), ('tf', b8_tf_cube)], [('short', b8_short_ab), ('short', b8_short_const)],
             [('mcq', b8_d1_formula), ('mcq', b8_d1_fill), ('mcq', b8_d1_read)], [('mcq', b8_d2_fac2), ('mcq', b8_d2_exp), ('mcq', b8_d2_diff2)],
             [('mcq', b8_d3_ab), ('mcq', b8_d3_val), ('mcq', b8_d3_x)], [('mcq', b8_d4_tank), ('mcq', b8_d4_two), ('mcq', b8_d4_shell)]]

# ----------------------------------------------------------------------------------- BÀI 9

def b9_common(r, lv):
    while True:
        g = r.randint(2, 6); e1, e2 = rexp(r, 2, 1, 3), rexp(r, 2, 1, 3); m = tuple(min(a, b) for a, b in zip(e1, e2))
        c1, c2 = nz(r, -5, 5), nz(r, -5, 5)
        if gcd(abs(c1), abs(c2)) == 1 and e1 != e2: break
    k = M(g, m); u, w = M(c1, tuple(a - b for a, b in zip(e1, m))), M(c2, tuple(a - b for a, b in zip(e2, m))); P = k * (u + w)
    good = '%s%s' % (k.tex(), br(u + w))
    bads = ['%s%s' % (k.tex(), br(-u + w)), '%s%s' % (k.tex(), br(u - w)), '%s%s' % (k.tex(), br(u + w + M(1, (0, 0, 0))))]
    return dict(en='Factor \\(%s\\) by taking out the common factor.' % P.tex(), vi='Phân tích đa thức \\(%s\\) thành nhân tử bằng cách đặt nhân tử chung.' % P.tex(),
                opts=pick_opts(r, good, bads), ans=0, ee='The greatest common factor is \\(%s\\): \\(%s\\).' % (k.tex(), good), ev='Nhân tử chung là \\(%s\\): \\(%s\\).' % (k.tex(), good))

def b9_ident(r, lv):
    a, b = r.randint(1, 5), r.randint(1, 9)
    if gcd(a, b) > 1: raise AssertionError
    kind = r.choice(['dsq', 'sq'])
    if kind == 'dsq':
        P = Poly.of([(a * a, (2, 0, 0)), (-b * b, (0, 0, 0))]); good = '(%s)(%s)' % (L(a, -b).tex(), L(a, b).tex()); bads = [sq(L(a, -b)), sq(L(a, b)), '(%s)(%s)' % (L(a, -b).tex(), L(-a, -b).tex())]
    else:
        s = r.choice([1, -1]); P = L(a, s * b) * L(a, s * b); good = sq(L(a, s * b)); bads = [sq(L(a, -s * b)), '(%s)(%s)' % (L(a, -b).tex(), L(a, b).tex()), sq(L(a * a, s * b)) if a > 1 else sq(L(1, s * b * b))]
    return dict(en='Factor \\(%s\\) using an identity.' % P.tex(), vi='Phân tích đa thức \\(%s\\) thành nhân tử bằng hằng đẳng thức.' % P.tex(), opts=pick_opts(r, good, bads), ans=0,
                ee='\\(%s=%s\\).' % (P.tex(), good), ev='\\(%s=%s\\).' % (P.tex(), good))

def _group(r):
    """(x + a y)(b x + c) khai triển 4 hạng tử, nhóm được."""
    a, b, c = nz(r, -5, 5), r.randint(1, 4), nz(r, -6, 6)
    F1, F2 = Poly.of([(1, XV), (a, YV)]), L(b, c)
    return F1, F2, F1 * F2

def b9_group(r, lv):
    F1, F2, P = _group(r)
    if len(P) != 4: raise AssertionError
    od = [(1 * F2.order()[0][0], (2, 0, 0)), (F1[YV] * F2.order()[0][0], (1, 1, 0)), (F2[(0, 0, 0)], XV), (F1[YV] * F2[(0, 0, 0)], YV)]
    t = ptex(od); good = '%s%s' % (br(F1), br(F2))
    bads = ['%s%s' % (br(Poly.of([(1, XV), (-F1[YV], YV)])), br(F2)), '%s%s' % (br(F1), br(L(F2[XV], -F2[(0, 0, 0)]))), '%s%s' % (br(Poly.of([(1, XV), (F1[YV], (0, 0, 0))])), br(Poly.of([(F2[XV], XV), (F2[(0, 0, 0)], YV)])))]
    return dict(en='Factor \\(%s\\) by grouping terms.' % t, vi='Phân tích đa thức \\(%s\\) thành nhân tử bằng cách nhóm hạng tử.' % t, opts=pick_opts(r, good, bads), ans=0,
                ee='Group the first two and the last two terms: \\(%s\\).' % good, ev='Nhóm hai hạng tử đầu và hai hạng tử cuối: \\(%s\\).' % good)

def b9_tf_fac(r, lv):
    a = r.randint(2, 9); truth = r.random() < .5; P = Poly.of([(1, (2, 0, 0)), (-a * a, (0, 0, 0))])
    claim = '(x-%d)(x+%d)' % (a, a) if truth else r.choice(['(x-%d)^2' % a, '(x-%d)(x+%d)' % (a * a, 1)])
    return dict(en='\\(%s=%s\\).' % (P.tex(), claim), vi='\\(%s=%s\\).' % (P.tex(), claim), ans=truth, ee='\\(%s=(x-%d)(x+%d)\\).' % (P.tex(), a, a), ev='\\(%s=(x-%d)(x+%d)\\).' % (P.tex(), a, a))

def b9_tf_group(r, lv):
    a, b = r.randint(1, 9), r.randint(1, 9); truth = r.random() < .5
    t = 'x^2+%dx+%sx+%d' % (a, '' if b == 1 else b, a * b) if False else 'x^2+%dx-%sx-%d' % (a, '' if b == 1 else b, a * b)
    good = '(x+%d)(x-%d)' % (a, b); claim = good if truth else '(x-%d)(x+%d)' % (a, b)
    if a == b and not truth: claim = '(x+%d)^2' % a
    return dict(en='\\(%s=%s\\).' % (t, claim), vi='\\(%s=%s\\).' % (t, claim), ans=truth,
                ee='\\(x(x+%d)-%s(x+%d)=(x+%d)(x-%d)\\).' % (a, b, a, a, b), ev='\\(x(x+%d)-%s(x+%d)=(x+%d)(x-%d)\\).' % (a, b, a, a, b))

def b9_short_x(r, lv):
    a = r.randint(1, 6); x0 = nz(r, -9, 9); b = a * x0
    t = '%sx^2%s=0' % ('' if a == 1 else a, mtex(-b, XV, False))
    return dict(en='Find the nonzero value of \\(x\\) such that \\(%s\\).' % t, vi='Tìm giá trị \\(x\\) khác 0 thỏa mãn \\(%s\\).' % t, key=str(x0),
                ee='\\(%sx(x%s)=0\\Rightarrow x=0\\) or \\(x=%d\\).' % ('' if a == 1 else a, mtex(-x0, (0, 0, 0), False), x0), ev='\\(%sx(x%s)=0\\Rightarrow x=0\\) hoặc \\(x=%d\\).' % ('' if a == 1 else a, mtex(-x0, (0, 0, 0), False), x0))

def b9_short_fast(r, lv):
    a = r.randint(12, 99); b = r.randint(11, 89); c = 100 - b
    return dict(en='Calculate quickly: \\(%d\\cdot %d+%d\\cdot %d\\).' % (a, b, a, c), vi='Tính nhanh: \\(%d\\cdot %d+%d\\cdot %d\\).' % (a, b, a, c), key=str(100 * a),
                ee='\\(=%d(%d+%d)=%d\\cdot100=%d\\).' % (a, b, c, a, 100 * a), ev='\\(=%d(%d+%d)=%d\\cdot100=%d\\).' % (a, b, c, a, 100 * a))

def b9_d1_gcf(r, lv):
    while True:
        g = r.randint(2, 6); e1, e2 = rexp(r, 2, 1, 3), rexp(r, 2, 1, 3); m = tuple(min(a, b) for a, b in zip(e1, e2)); c1, c2 = r.randint(1, 5), -r.randint(1, 5)
        if gcd(c1, -c2) == 1 and e1 != e2: break
    P = M(g * c1, e1) + M(g * c2, e2); k = M(g, m)
    bads = [M(g * c1 * -c2, m), M(g, e1), M(1, m)]
    return dict(en='What is the greatest common factor of the terms of \\(%s\\)?' % P.tex(), vi='Nhân tử chung của các hạng tử trong đa thức \\(%s\\) là' % P.tex(),
                opts=tpoly(r, k, bads, lambda t: M(g + t + 1, m)), ans=0, ee='GCF of the coefficients: %d; lowest powers: \\(%s\\).' % (g, vpart(m)), ev='ƯCLN của các hệ số là %d; mỗi biến lấy số mũ nhỏ nhất: \\(%s\\).' % (g, vpart(m)))

METH = [tx('taking out a common factor', 'đặt nhân tử chung'), tx('using an identity', 'dùng hằng đẳng thức'), tx('grouping terms', 'nhóm hạng tử'), tx('none: it cannot be factored', 'không phân tích được')]
def b9_d1_method(r, lv):
    """Chọn phương pháp; dùng lại đề của b9_common / b9_ident / b9_group."""
    k = r.randrange(3)
    if k == 0: q = b9_common(r, lv)
    elif k == 1: q = b9_ident(r, lv)
    else: q = b9_group(r, lv)
    P = re.search(r'\\\((.*?)\\\)', q['en']).group(1)
    o = [METH[k]] + [m for i, m in enumerate(METH) if i != k]
    return dict(en='Which method is the most suitable to factor \\(%s\\)?' % P, vi='Phương pháp thích hợp nhất để phân tích đa thức \\(%s\\) thành nhân tử là' % P, opts=o, ans=0,
                ee=q['ee'], ev=q['ev'])

def b9_d1_def(r, lv):
    Q = PICK(r, [('Factoring a polynomial means…', 'Phân tích đa thức thành nhân tử là'), ('What does it mean to factor a polynomial?', 'Thế nào là phân tích một đa thức thành nhân tử?'),
                 ('Complete: to factor a polynomial is to…', 'Hoàn thành: phân tích đa thức thành nhân tử là…'), ('Which statement describes factoring a polynomial?', 'Phát biểu nào mô tả đúng việc phân tích đa thức thành nhân tử?')])
    o = [tx('writing it as a product of polynomials', 'biến đổi đa thức đó thành một tích của những đa thức'), tx('writing it as a sum of monomials', 'biến đổi đa thức thành tổng các đơn thức'),
         tx('finding its degree', 'tìm bậc của đa thức'), tx('finding its value', 'tính giá trị của đa thức')]
    return dict(en=Q[0], vi=Q[1], opts=o, ans=0, ee='Example: \\(x^2-x=x(x-1)\\).', ev='Ví dụ: \\(x^2-x=x(x-1)\\).')

def b9_d2_sq(r, lv):
    a, b = r.randint(1, 4), r.randint(1, 5)
    if gcd(a, b) > 1: raise AssertionError
    s = r.choice([1, -1]); P = Poly.of([(a, XV), (s * b, YV)]); R = P * P
    good = sq(P); bads = [sq(Poly.of([(a, XV), (-s * b, YV)])), '(%s)(%s)' % (Poly.of([(a, XV), (-b, YV)]).tex(), Poly.of([(a, XV), (b, YV)]).tex()), sq(Poly.of([(a * a, XV), (s * b * b, YV)])) if a > 1 or b > 1 else sq(Poly.of([(1, XV), (2 * s, YV)]))]
    return dict(en='Factor \\(%s\\).' % R.tex(), vi='Phân tích đa thức \\(%s\\) thành nhân tử.' % R.tex(), opts=pick_opts(r, good, bads), ans=0, ee='\\(%s=%s\\).' % (R.tex(), good), ev='\\(%s=%s\\).' % (R.tex(), good))

def b9_d2_cube(r, lv):
    q = b8_fac(r, lv); q['en'] = q['en'].replace('Write', 'Factor').replace(' as a product.', '.'); q['vi'] = q['vi'].replace('Viết đa thức', 'Phân tích đa thức').replace(' dưới dạng tích.', ' thành nhân tử.'); return q

def b9_d2_binom(r, lv):
    a, b, c = r.randint(1, 9), r.randint(2, 6), r.randint(2, 9); swap = r.random() < .5
    if swap:
        t = '%dx(x-%d)+%d(%d-x)' % (b, a, c, a); good = '(x-%d)(%dx-%d)' % (a, b, c); bads = ['(x-%d)(%dx+%d)' % (a, b, c), '(x+%d)(%dx-%d)' % (a, b, c), '(x-%d)(%dx-%d)' % (a, b + c, 1)]
    else:
        t = '%dx(x-%d)-%d(x-%d)' % (b, a, c, a); good = '(x-%d)(%dx-%d)' % (a, b, c); bads = ['(x-%d)(%dx+%d)' % (a, b, c), '(x-%d)^2(%dx-%d)' % (a, b, c), '%dx(x-%d)' % (b - c, a) if b != c else '(x+%d)(%dx-%d)' % (a, b, c)]
    return dict(en='Factor \\(%s\\).' % t, vi='Phân tích đa thức \\(%s\\) thành nhân tử.' % t, opts=pick_opts(r, good, bads), ans=0,
                ee=('Note \\(%d(%d-x)=-%d(x-%d)\\); the common factor is \\(x-%d\\).' % (c, a, c, a, a)) if swap else 'The common factor is \\(x-%d\\).' % a,
                ev=('Chú ý \\(%d(%d-x)=-%d(x-%d)\\); nhân tử chung là \\(x-%d\\).' % (c, a, c, a, a)) if swap else 'Nhân tử chung là \\(x-%d\\).' % a)

def b9_d3_x(r, lv):
    k = r.randint(1, 7); a = r.choice([1, 2])
    t = '%sx^3-%dx=0' % ('' if a == 1 else a, a * k * k)
    good = 'x\\in\\{0;\\ %d;\\ -%d\\}' % (k, k); bads = ['x\\in\\{%d;\\ -%d\\}' % (k, k), 'x\\in\\{0;\\ %d\\}' % k, 'x\\in\\{0;\\ %d;\\ -%d\\}' % (k * k, k * k)]
    return dict(en='Find all \\(x\\) such that \\(%s\\).' % t, vi='Tìm tất cả các giá trị của \\(x\\), biết \\(%s\\).' % t, opts=pick_opts(r, good, bads), ans=0,
                ee='\\(%sx(x-%d)(x+%d)=0\\).' % ('' if a == 1 else a, k, k), ev='\\(%sx(x-%d)(x+%d)=0\\).' % ('' if a == 1 else a, k, k))

def b9_d3_comb(r, lv):
    a = r.randint(1, 5); s = r.choice([1, -1]); P = M(1, XV) * Poly.of([(1, XV), (s * a, YV)]) * Poly.of([(1, XV), (s * a, YV)])
    good = 'x(x%s%sy)^2' % ('+' if s > 0 else '-', '' if a == 1 else a)
    bads = ['x(x%s%sy)^2' % ('-' if s > 0 else '+', '' if a == 1 else a), 'x(x-%sy)(x+%sy)' % ('' if a == 1 else a, '' if a == 1 else a), '(x%s%sy)^2' % ('+' if s > 0 else '-', '' if a == 1 else a)]
    return dict(en='Factor \\(%s\\).' % P.tex(), vi='Phân tích đa thức \\(%s\\) thành nhân tử.' % P.tex(), opts=pick_opts(r, good, bads), ans=0,
                ee='Take out \\(x\\), then use the square identity: \\(%s\\).' % good, ev='Đặt nhân tử chung \\(x\\) rồi dùng hằng đẳng thức: \\(%s\\).' % good)

def b9_d3_gid(r, lv):
    k = r.randint(1, 6); t = 'x^2-2xy+y^2-%d' % (k * k)
    good = '(x-y-%d)(x-y+%d)' % (k, k); bads = ['(x-y-%d)^2' % k, '(x+y-%d)(x+y+%d)' % (k, k), '(x-y-%d)(x+y+%d)' % (k, k)]
    return dict(en='Factor \\(%s\\).' % t, vi='Phân tích đa thức \\(%s\\) thành nhân tử.' % t, opts=pick_opts(r, good, bads), ans=0,
                ee='\\((x-y)^2-%d^2=(x-y-%d)(x-y+%d)\\).' % (k, k, k), ev='\\((x-y)^2-%d^2=(x-y-%d)(x-y+%d)\\).' % (k, k, k))

def b9_d4_rect(r, lv):
    a, b = r.sample(range(1, 8), 2); a, b = min(a, b), max(a, b); x = r.randint(3, 12); S = L(1, a) * L(1, b)
    good = '(x+%d)\\text{ m and }(x+%d)\\text{ m}' % (a, b)
    return dict(en='A rectangular plot has area \\(%s\\) (m²). Hint: \\(%s=x^2+%dx+%dx+%d\\). Its sides are \\((x+%d)\\) m and \\((x+%d)\\) m. What is its area when \\(x=%d\\)?' % (S.tex(), S.tex(), a, b, a * b, a, b, x),
                vi='Một mảnh đất hình chữ nhật có diện tích \\(%s\\) (m²). Gợi ý: \\(%s=x^2+%sx+%dx+%d\\). Các cạnh của mảnh đất là \\((x+%d)\\) m và \\((x+%d)\\) m. Tính diện tích khi \\(x=%d\\).' % (S.tex(), S.tex(), '' if a == 1 else a, b, a * b, a, b, x),
                opts=nopts(r, (x + a) * (x + b), [x * x + a * b, (x + a + b) * x, (x + a) * (x + b) + a]), ans=0,
                ee='\\((x+%d)(x+%d)=%d\\cdot%d=%d\\) m².' % (a, b, x + a, x + b, (x + a) * (x + b)), ev='\\((x+%d)(x+%d)=%d\\cdot%d=%d\\) m².' % (a, b, x + a, x + b, (x + a) * (x + b)))

def b9_d4_fast(r, lv):
    b = r.randint(2, 40); a = r.choice([k * 10 - b for k in range(7, 14) if 55 <= k * 10 - b <= 99] or [0])
    if a <= b: raise AssertionError
    v = a * a - b * b
    return dict(en='Calculate quickly: \\(%d^2-%d^2\\).' % (a, b), vi='Tính nhanh: \\(%d^2-%d^2\\).' % (a, b), opts=nopts(r, v, [(a - b) ** 2, a * a + b * b, v + 100]), ans=0,
                ee='\\(=(%d-%d)(%d+%d)=%d\\cdot%d=%d\\).' % (a, b, a, b, a - b, a + b, v), ev='\\(=(%d-%d)(%d+%d)=%d\\cdot%d=%d\\).' % (a, b, a, b, a - b, a + b, v))

def b9_d4_div(r, lv):
    k = r.randrange(3)
    expr, fac = [('n^3-n', '(n-1)n(n+1)'), ('n^3+5n', 'n^3-n+6n=(n-1)n(n+1)+6n'), ('n^3+11n', 'n^3-n+12n=(n-1)n(n+1)+12n')][k]
    o = [tx('6', '6'), tx('12', '12'), tx('5', '5'), tx('9', '9')]
    return dict(en='For every integer \\(n\\), the number \\(%s\\) is always divisible by…' % expr, vi='Với mọi số nguyên \\(n\\), số \\(%s\\) luôn chia hết cho' % expr, opts=o, ans=0,
                ee='\\(%s\\); the product of three consecutive integers is divisible by 2 and by 3, so by 6.' % fac, ev='\\(%s\\); tích ba số nguyên liên tiếp chia hết cho 2 và cho 3 nên chia hết cho 6.' % fac)

L9_GROUPS = [[('mcq', b9_common), ('mcq', b9_ident), ('mcq', b9_group)], [('tf', b9_tf_fac), ('tf', b9_tf_group)], [('short', b9_short_x), ('short', b9_short_fast)],
             [('mcq', b9_d1_gcf), ('mcq', b9_d1_method), ('mcq', b9_d1_def)], [('mcq', b9_d2_sq), ('mcq', b9_d2_cube), ('mcq', b9_d2_binom)],
             [('mcq', b9_d3_x), ('mcq', b9_d3_comb), ('mcq', b9_d3_gid)], [('mcq', b9_d4_rect), ('mcq', b9_d4_fast), ('mcq', b9_d4_div)]]
