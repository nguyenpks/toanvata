# -*- coding: utf-8 -*-
"""Bộ sinh câu TRẮC NGHIỆM TỰ LUYỆN: mỗi mức một bộ riêng (cùng dạng, khác số liệu), đáp án do máy tính tính và tự kiểm.
Dùng: SELF([builder, ...], start=11) -> {1: [MCQ...], 2: [...], 3: [...]}. Mỗi builder(r, lv) trả dict(en, vi, opts[4], ans, ee, ev)."""
import random
from fractions import Fraction as F
from mb_lib import MCQ

def fr(x):
    x = F(x)
    if x.denominator == 1: return str(x.numerator)
    return ('-' if x < 0 else '') + '\\dfrac{%d}{%d}' % (abs(x.numerator), x.denominator)

def lin(a, c=0, var='x'):
    """a*var + c dưới dạng tex."""
    s = '' if a == 0 else ('' if a == 1 else '-' if a == -1 else str(a)) + var
    if c == 0: return s or '0'
    return s + ('+' if c > 0 and s else '') + str(c)

def xm(a, var='x'):
    """(x - a) dưới dạng tex."""
    return '(%s%s%d)' % (var, '-' if a > 0 else '+', abs(a)) if a != 0 else var

def poly(c, var='x'):
    n = len(c) - 1; s = ''
    for i, a in enumerate(c):
        p = n - i
        if a == 0: continue
        ab = abs(a); body = str(ab) if p == 0 else ('' if ab == 1 else str(ab)) + var + ('' if p == 1 else '^%d' % p)
        s += ('-' if a < 0 else ('+' if s else '')) + body
    return s or '0'

def interval(lo, lc, hi, hc):
    f = lambda v: '-\\infty' if v is None and v is lo else ('+\\infty' if v is None else fr(v))
    return '%s%s,%s%s' % ('[' if lc else '(', '-\\infty' if lo is None else fr(lo), '+\\infty' if hi is None else fr(hi), ']' if hc else ')')

def pick_opts(r, correct, others, fill=None):
    """4 phương án phân biệt: correct + 3 phương án sai lấy từ others (ưu tiên thứ tự), bổ sung bằng fill() nếu thiếu."""
    opts = [correct]
    for o in others:
        if o not in opts: opts.append(o)
        if len(opts) == 4: break
    k = 0
    while len(opts) < 4 and fill is not None:
        k += 1; o = fill(k)
        if o not in opts: opts.append(o)
        assert k < 50
    assert len(opts) == 4, (correct, others)
    return opts

def _items_html(x):
    if isinstance(x, str): return x
    if isinstance(x, (list, tuple)): return ''.join(_items_html(y) for y in x)
    return ''

def SELF(builders, start=1, seeds=(101, 202, 303), avoid=()):
    """avoid: các mục bài tập đã có trong bài (để không sinh trùng câu hỏi)."""
    import html as _h
    out, used = {}, set(); old = _items_html(list(avoid))
    for lv, seed in zip((1, 2, 3), seeds):
        r = random.Random(seed); items = []; n = start
        for b in builders:
            for _ in range(300):
                try: q = b(r, lv)
                except AssertionError: continue
                if q['en'] not in used and len(set(q['opts'])) == 4 and q['en'] not in old and _h.escape(q['en'], quote=False) not in old: break
            else: raise RuntimeError('không sinh được câu không trùng: ' + b.__name__)
            used.add(q['en'])
            def esc(t):                                  # tránh < > thô trong HTML, nhưng giữ nguyên bảng tần số và phương án văn bản '§'
                if t.startswith('§'): return t
                import re as _re
                return ''.join(x if x.startswith('<div class="mbl-tablewrap') else x.replace('<', '\\lt ').replace('>', '\\gt ') for x in _re.split(r'(<div class="mbl-tablewrap.*?</table></div>)', t, flags=_re.S))
            q = dict(q, en=esc(q['en']), vi=esc(q['vi']), ee=esc(q['ee']), ev=esc(q['ev']), opts=[esc(o) for o in q['opts']])
            opts = list(q['opts']); correct = opts[q['ans']]; assert len(set(opts)) == 4, (b.__name__, opts)
            idx = list(range(4)); r.shuffle(idx); sh = [opts[i] for i in idx]; L = 'abcd'[sh.index(correct)]
            items.append(MCQ(n, (q['en'], q['vi']), sh, L, ('Answer: %s. %s' % (L, q['ee']), 'Đáp án %s. %s' % (L, q['ev']))))
            n += 1
        out[lv] = items
    return out
