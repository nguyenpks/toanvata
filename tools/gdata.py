# -*- coding: utf-8 -*-
"""Mẫu số liệu ghép nhóm: tính chính xác (Fraction) và sinh bảng cho các giá trị đẹp (nguyên hoặc .5)."""
import random
from fractions import Fraction as F

class GT:
    def __init__(s, u0, h, fs): s.u0, s.h, s.fs = u0, h, list(fs); s.n = sum(fs); s.k = len(fs)
    def edge(s, i): return s.u0 + i * s.h
    def mid(s, i): return F(2 * s.u0 + (2 * i + 1) * s.h, 2)
    def cum(s, i): return sum(s.fs[:i])                       # tần số tích lũy trước nhóm i
    def mean(s): return sum(f * s.mid(i) for i, f in enumerate(s.fs)) / s.n
    def quant(s, num, den):
        pos = F(num * s.n, den)
        for i in range(s.k):
            if s.cum(i + 1) >= pos: return i, s.edge(i) + (pos - s.cum(i)) / s.fs[i] * s.h
    def median(s): return s.quant(1, 2)[1]
    def q1(s): return s.quant(1, 4)[1]
    def q3(s): return s.quant(3, 4)[1]
    def med_group(s): return s.quant(1, 2)[0]
    def mode_group(s): return max(range(s.k), key=lambda i: (s.fs[i], -i))
    def mode(s):
        m = s.mode_group(); a = s.fs[m - 1] if m > 0 else 0; b = s.fs[m + 1] if m < s.k - 1 else 0
        return s.edge(m) + F(s.fs[m] - a, (s.fs[m] - a) + (s.fs[m] - b)) * s.h
    def rng(s): return s.edge(s.k) - s.edge(0)
    def iqr(s): return s.q3() - s.q1()
    def label(s, i): return '[%d;%d)' % (s.edge(i), s.edge(i + 1))
    def text(s): return ';\\ '.join('%s: %d' % (s.label(i), f) for i, f in enumerate(s.fs))
    def html(s, rows=('group', 'freq'), **kw):
        from freqtable import FREQ
        return FREQ([s.edge(i) for i in range(s.k + 1)], s.fs, rows=rows, **kw)
    def var(s): m = s.mean(); return sum(f * (s.mid(i) - m) ** 2 for i, f in enumerate(s.fs)) / s.n

def half(x): return (2 * x).denominator == 1
def dec(x):
    x = F(x)
    if x.denominator == 1: return str(x.numerator)
    if (10 * x).denominator == 1: return '%d.%d' % (int(x * 10) // 10, int(x * 10) % 10)
    return '%.2f' % float(x)

def nice(seed, need=('mean', 'median', 'mode'), h_opts=(5, 10), k_opts=(4, 5), nmod=4, extra=None):
    """Bảng ngẫu nhiên (hạt giống cố định) sao cho các đại lượng cần thiết là số nguyên hoặc .5."""
    r = random.Random(seed)
    for _ in range(400000):
        h = r.choice(h_opts); k = r.choice(k_opts); fs = [r.randint(2, 14) for _ in range(k)]
        if sum(fs) % nmod or sum(fs) > 60 or sum(fs) < 16 or max(fs) > 3 * min(fs) or max(fs) == min(fs): continue
        t = GT(r.choice([0, 0, 5, 10, 20]), h, fs)
        if len(set(fs)) < k - 1: continue
        if max(fs) in fs[:fs.index(max(fs))] + fs[fs.index(max(fs)) + 1:]: continue       # mốt duy nhất
        try: vals = [getattr(t, nm)() for nm in need]
        except ZeroDivisionError: continue
        if all(half(v) for v in vals) and (extra is None or extra(t)): return t
    raise RuntimeError('không tìm được bảng đẹp, seed=%s' % seed)
