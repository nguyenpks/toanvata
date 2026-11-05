# -*- coding: utf-8 -*-
"""Bộ trợ giúp soạn bài nhanh, gọn: từ vựng, trắc nghiệm có đáp án tự đặt vị trí, miền nghiệm (cắt đa giác), đỉnh miền nghiệm."""
import itertools
from fractions import Fraction as F
from mb_std import *
from mb_extra import TBL
from mb_selfpractice import SELF, fr, pick_opts, lin
import mb_std

HN = ('Enter a number.', 'Nhập một số.')
GRP = [('A. Multiple Choice', 'A. Trắc nghiệm nhiều lựa chọn'), ('B. True or False', 'B. Đúng hoặc sai'), ('C. Short Answer', 'C. Trả lời ngắn')]
SELF_T = ('Self-practice: Multiple Choice', 'Tự luyện: trắc nghiệm')

def defs(cv, rows):
    """rows: (key, en, vi, en_def, vi_def, example, symbol). Trả về danh sách vocab của bài và ghi thuật ngữ vào vocab.json."""
    ensure_vocab([('q-' + k, en, vi, cv, ex, sym) for (k, en, vi, d1, d2, ex, sym) in rows]); load_vocab()
    return [('<b>%s</b> – %s' % (en, d1), '[[%s]] – %s' % (vi, d2)) for (k, en, vi, d1, d2, ex, sym) in rows]

def M4(n, qen, qvi, correct, wrongs, een, evi):
    """Câu trắc nghiệm: phương án đúng được đặt ở vị trí cố định theo n để các phương án phân bố đều."""
    opts = [correct] + list(dict.fromkeys(w for w in wrongs if w != correct))[:3]
    assert len(set(opts)) == 4, (qen, opts)
    k = (n * 3 + len(correct)) % 4; opts.pop(0); opts.insert(k, correct); L = 'abcd'[k]
    return MCQ(n, (qen, qvi), opts, L, ('Answer: %s. %s' % (L, een), 'Đáp án %s. %s' % (L, evi)))

def tf(n, qen, qvi, val, een, evi): return TF(n, (qen, qvi), 'true' if val else 'false', (een, evi))
def sh(n, qen, qvi, key, een, evi, hint=HN): return SHORT(n, (qen, qvi), str(key), 'number', hint, (een, evi))

def three(fn, params):
    """Mỗi mức một bộ: fn(p) -> [nhóm A, nhóm B, nhóm C]; sets = {1: ..., 2: ..., 3: ...}."""
    return LEVEL_PRACTICE(GRP, {lv: fn(p) for lv, p in zip((1, 2, 3), params)})

def with_self(practice, builders, start, letter='D'):
    sp = SELF(builders, start=start, avoid=[t[1] for t in practice])
    return practice + [(('%s. Self-practice: Multiple Choice' % letter, '%s. Tự luyện: trắc nghiệm' % letter), sp[lv], [lv]) for lv in (1, 2, 3)]

# ---------- miền nghiệm của hệ bất phương trình (a x + b y ≤ c) ----------
def clip(poly, a, b, c):
    out = []
    for i in range(len(poly)):
        P, Q = poly[i], poly[(i + 1) % len(poly)]
        fp, fq = a * P[0] + b * P[1] + c, a * Q[0] + b * Q[1] + c
        if fp >= 0: out.append(P)
        if (fp > 0 > fq) or (fp < 0 < fq):
            t = fp / (fp - fq); out.append((P[0] + t * (Q[0] - P[0]), P[1] + t * (Q[1] - P[1])))
    return out

def region(view, cons, lines=None, dashed=()):
    """cons: (a,b,c) nghĩa a·x+b·y ≤ c; lines: đường biên cần vẽ (mặc định tất cả cons)."""
    x0, x1, y0, y1 = view; poly = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
    for a, b, c in cons: poly = clip(poly, -a, -b, c)
    steps = []
    if len(poly) >= 3: steps.append({'type': 'polygon', 'through': [[round(p[0], 4), round(p[1], 4)] for p in poly], 'style': {'borders': {'visible': False}}})
    for i, (a, b, c) in enumerate(lines if lines is not None else cons):
        st = {'type': 'lineeq', 'a': a, 'b': b, 'c': -c}
        if i in dashed: st['style'] = {'dash': 2}
        steps.append(st)
    return {'view': list(view), 'axes': True, 'steps': steps}

def vertices(cons):
    """Đỉnh của miền {a x + b y ≤ c} (chính xác, Fraction)."""
    pts = set()
    for (a1, b1, c1), (a2, b2, c2) in itertools.combinations(cons, 2):
        d = a1 * b2 - a2 * b1
        if d == 0: continue
        x = F(c1 * b2 - c2 * b1, d); y = F(a1 * c2 - a2 * c1, d)
        if all(a * x + b * y <= c for a, b, c in cons): pts.add((x, y))
    return sorted(pts)

def GE(cfg, en, vi, h=320): return GEO(cfg, cap=(en, vi), alt=(en, ''), height=h)
