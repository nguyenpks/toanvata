# -*- coding: utf-8 -*-
"""Lắp các họ câu hỏi của gq.py thành bộ bài tập 3 mức cho một bài học (7 câu/mức: 3 trắc nghiệm, 2 đúng/sai, 2 trả lời ngắn)."""
import random
from mb_quick import M4, tf, sh
import gq

def _get(fam, r, used):
    for _ in range(400):
        try: d = fam(r)
        except AssertionError: continue
        if d['en'] in used: continue
        used.add(d['en']); return d
    raise RuntimeError('không sinh được câu: ' + fam.__name__)

def level_set(seed, mcq, tfs, shs, used):
    r = random.Random(seed); out = [[], [], []]
    for i, f in enumerate(mcq):
        d = _get(f, r, used); out[0].append(M4(i + 1, d['en'], d['vi'], d['opts'][0], d['opts'][1:], d['ee'], d['ev']))
    for i, f in enumerate(tfs):
        d = _get(f, r, used); out[1].append(tf(len(mcq) + i + 1, d['en'], d['vi'], d['truth'], d['ee'], d['ev']))
    for i, f in enumerate(shs):
        d = _get(f, r, used); out[2].append(sh(len(mcq) + len(tfs) + i + 1, d['en'], d['vi'], d['key'], d['ee'], d['ev']))
    return out

def make_levels(plan):
    """plan = [(seed, mcq_fams, tf_fams, sh_fams)] cho mức 1, 2, 3 -> LEVEL_PRACTICE dùng chung bộ 'used' để không trùng đề giữa các mức."""
    from mb_quick import three
    used = set()
    P = [dict(a=a) for a in plan]
    return three(lambda p: level_set(p['a'][0], p['a'][1], p['a'][2], p['a'][3], used), P)
