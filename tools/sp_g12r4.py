# -*- coding: utf-8 -*-
"""Hiệu chỉnh lớp 12 – đợt 14/11/2026: Bài 9, 10 (thống kê), 17 (mặt cầu), 18, 19 (xác suất có điều kiện, Bayes).
Mục tiêu mỗi mức 20 câu: A 6 · B 3 · C 3 · D 8; phần D gồm 8 DẠNG khác nhau và khác các dạng ở A–C.

Mỗi hàm sinh câu (r, lv, ctx) trả về dict như sp_g11r:
  trắc nghiệm : en, vi, opts[4] (opts[0] đúng), ee, ev
  đúng/sai    : en, vi, truth, ee, ev
  trả lời ngắn: en, vi, key (≤ 4 kí tự), ee, ev [, hint]
  tuỳ chọn    : fig = (html_en, html_vi) ghép sau đề (bảng, biểu đồ, hình).
Mọi đáp án được tính ngay trong hàm sinh (Fraction / số nguyên); tools/audit_g12r4.py kiểm tra lại độc lập từ trang đã dựng.
Bài 9–10: dùng bộ tình huống gq.SC, mỗi tình huống tối đa 2 lần trong một mức (ctx đếm số lần dùng)."""
import math, random, re
from fractions import Fraction as F
from mb_lib import TI, MCQ, LEVEL_PRACTICE
from mb_quick import M4, tf, sh, GRP
from sp_g11r import tx, ne, nv, nopt, nopts, key, lab, gtab, TB, grp, Q3D, TD, _fig
from sp_g11r2 import V, frt, fo, HIST
import gq
from gdata import GT
from mb_pgf import texsvg, col
import fig2d as G

def M(s): return '\\(%s\\)' % s
def NE(x): return ne(x)
def NV(x): return nv(x)
def both(fmt, x, lang): return fmt % (ne(x) if lang == 'en' else nv(x))
def tt(en, vi): return tx(en, vi)                         # phương án văn bản hai ngôn ngữ

# ================================================================ lắp bộ đề: giữ câu cũ + thêm câu mới
_QN = re.compile(r'(<div class="mbl-item" data-type="\w+"(?: data-kind="\w+")? data-answer="[^"]*"><div class="mbl-qtext"><b>)(\d+)(\.</b>)')

def _renum(items, start):
    out = []
    for k, h in enumerate(items):
        h2, c = _QN.subn(lambda m: m.group(1) + str(start + k) + m.group(3), h, count=1); assert c == 1
        out.append(h2)
    return out

def _gen(b, r, lv, ctx, used, old):
    import html as _h
    for _ in range(600):
        try: q = b(r, lv, ctx)
        except AssertionError: continue
        if q['en'] in used or _h.escape(q['en'], quote=False) in old: continue
        if 'opts' in q and len(set(q['opts'])) != 4: continue
        used.add(q['en']); return q
    raise RuntimeError('không sinh được câu: ' + b.__name__)

def build(old, A, B, C, D, seeds, ctx_factory=lambda r, lv: {}):
    """old: {lv: [nhóm A, nhóm B, nhóm C]} (HTML câu cũ, có thể rỗng) – giữ nguyên nội dung, chỉ đánh số lại.
    A, B, C, D: hàm sinh câu mới thêm vào cuối từng nhóm. Trả về danh sách nhóm cho QUIZ (đủ 3 mức, D riêng)."""
    used = set(); sets = {}; dsets = {}
    oldtxt = ''.join(''.join(''.join(g) for g in old.get(lv, [[], [], []])) for lv in (1, 2, 3))
    for lv, seed in zip((1, 2, 3), seeds):
        r = random.Random(seed); ctx = ctx_factory(r, lv); og = old.get(lv, [[], [], []])
        gA, gB, gC, gD = [], [], [], []
        for b in A:
            q = _gen(b, r, lv, ctx, used, oldtxt); en, vi = _fig(q); gA.append(M4(1, en, vi, q['opts'][0], q['opts'][1:], q['ee'], q['ev']))
        for b in B:
            q = _gen(b, r, lv, ctx, used, oldtxt); en, vi = _fig(q); gB.append(tf(1, en, vi, q['truth'], q['ee'], q['ev']))
        for b in C:
            q = _gen(b, r, lv, ctx, used, oldtxt); en, vi = _fig(q)
            gC.append(sh(1, en, vi, q['key'], q['ee'], q['ev'], hint=q.get('hint', ('Enter a number.', 'Nhập một số.'))))
        for b in D:
            q = _gen(b, r, lv, ctx, used, oldtxt); en, vi = _fig(q)
            opts = list(q['opts']); good = opts[0]; idx = list(range(4)); r.shuffle(idx); shf = [opts[i] for i in idx]; L = 'abcd'[shf.index(good)]
            gD.append(MCQ(1, (en, vi), shf, L, ('Answer: %s. %s' % (L, q['ee']), 'Đáp án %s. %s' % (L, q['ev']))))
        n = 1; out = []
        for g_old, g_new in zip(og, (gA, gB, gC)):
            grp_ = _renum(list(g_old) + g_new, n); n += len(grp_); out.append(grp_)
        sets[lv] = out; dsets[lv] = _renum(gD, n)
    return LEVEL_PRACTICE(GRP, sets) + [(TD, dsets[lv], [lv]) for lv in (1, 2, 3)]

def old_sets(practice):
    """Từ danh sách nhóm của three()/LEVEL_PRACTICE → {lv: [[A], [B], [C]]}."""
    out = {1: [], 2: [], 3: []}
    for title, items, lvs in practice: out[lvs[0]].append(list(items))
    return out

# ================================================================ thống kê: tình huống, bảng
SC = gq.SC
def sctx(r, lv): return {'cnt': {s['k']: 0 for s in SC}}
def pick(ctx, r, ok=lambda s: True):
    """Tình huống ít dùng nhất (mỗi tình huống tối đa 2 lần/mức)."""
    c = ctx['cnt']; cand = [s for s in SC if ok(s) and c[s['k']] < 2]
    assert cand
    m = min(c[s['k']] for s in cand); s = r.choice([s for s in cand if c[s['k']] == m]); c[s['k']] += 1; return s

def mk(r, sc, need=(), cond=lambda t: True, nset=(20, 24, 28, 32, 36, 40, 44, 48), tries=60):
    for _ in range(tries):
        try: t = gq.mkt(r, sc, need=need, nset=nset)
        except AssertionError: continue
        if cond(t): return t
    raise AssertionError('mk')

def U(sc, lang): return sc['unit'] if lang == 'en' else sc['uv']
def I(sc, lang): return sc['intro'][0 if lang == 'en' else 1]
def VAR(sc, lang): return sc['var'][0 if lang == 'en' else 1]
def ENT(sc, lang): return sc['ent'][0 if lang == 'en' else 1]
def GR(t, i, lang): return grp(t, i, ne if lang == 'en' else nv)
def qgroup(t, j):
    """Nhóm chứa Q_j (j = 1, 2, 3)."""
    return t.quant(j, 4)[0]
def Qj(t, j): return t.quant(j, 4)[1]
def shortok(x):
    try: key(x); return True
    except AssertionError: return False

def cumtab(sc, t, lang):
    """Bảng ghép nhóm với dòng TẦN SỐ TÍCH LŨY (không có dòng tần số)."""
    N = ne if lang == 'en' else nv
    gl = lab(sc['gl'])[0 if lang == 'en' else 1]
    cl = 'Cumulative frequency' if lang == 'en' else 'Tần số tích lũy'
    r1 = '<tr><th scope="row">%s</th>%s</tr>' % (gl, ''.join('<td>%s</td>' % GR(t, i, lang) for i in range(t.k)))
    r2 = '<tr><th scope="row">%s</th>%s</tr>' % (cl, ''.join('<td>\\(%d\\)</td>' % t.cum(i + 1) for i in range(t.k)))
    return '<div class="mbl-tablewrap mbl-freqwrap"><table class="mbl-table mbl-freq"><tbody>%s%s</tbody></table></div>' % (r1, r2)

def two_tabs(sc, t1, t2):
    def one(lang):
        a, b = ('Sample A', 'Sample B') if lang == 'en' else ('Mẫu A', 'Mẫu B')
        return '<p><b>%s</b></p>%s<p><b>%s</b></p>%s' % (a, gtab(sc, t1, lang), b, gtab(sc, t2, lang))
    return (one('en'), one('vi'))

def hb(xs): return [x for x in xs if (2 * F(x)).denominator == 1]       # chỉ giữ phương án nhiễu nguyên hoặc ,5

# ================================================================ BÀI 9 – Khoảng biến thiên, khoảng tứ phân vị
def b9_range(r, lv, ctx):
    sc = pick(ctx, r); t = mk(r, sc); R = t.rng()
    qe = V(lv, ['Find the range \\(R\\) of the %s (in %s).', 'The range of the %s (in %s) is…', 'What is the range of the %s (in %s)?'])
    qv = V(lv, ['Tìm khoảng biến thiên \\(R\\) của %s (đơn vị %s).', 'Khoảng biến thiên của %s (đơn vị %s) là…', 'Khoảng biến thiên của %s (đơn vị %s) bằng bao nhiêu?'])
    return dict(en='%s %s' % (I(sc, 'en'), qe % (VAR(sc, 'en'), U(sc, 'en'))), vi='%s %s' % (I(sc, 'vi'), qv % (VAR(sc, 'vi'), U(sc, 'vi'))),
                opts=nopts(r, R, [t.edge(t.k - 1) - t.edge(0), R - t.h, t.mid(t.k - 1) - t.mid(0), R + t.h], step=t.h), fig=TB(sc, t),
                ee='\\(R=u_{k+1}-u_1=%s-%s=%s\\).' % (ne(t.edge(t.k)), ne(t.edge(0)), ne(R)), ev='\\(R=u_{k+1}-u_1=%s-%s=%s\\).' % (nv(t.edge(t.k)), nv(t.edge(0)), nv(R)))

def _qsteps(t, j, lang):
    N = ne if lang == 'en' else nv; i, q = t.quant(j, 4); pos = F(j * t.n, 4)
    fr = '\\frac n4' if j == 1 else '\\frac{%dn}{4}' % j
    return '\\(%s=%s\\) %s %s; \\(Q_%d=%s+\\dfrac{%s-%d}{%d}\\cdot%s=%s\\).' % (fr, N(pos), 'lies in the group' if lang == 'en' else 'thuộc nhóm', GR(t, i, lang), j, N(t.edge(i)), N(pos), t.cum(i), t.fs[i], N(t.h), N(q))

def b9_q1(r, lv, ctx):
    sc = pick(ctx, r); t = mk(r, sc, need=('q1', 'q3')); q = Qj(t, 1); i = qgroup(t, 1)
    wrong_c = t.edge(i) + (F(t.n, 4) - t.cum(i + 1)) / t.fs[i] * t.h
    qe = V(lv, ['Find the first quartile \\(Q_1\\) of the %s (in %s).', 'The first quartile \\(Q_1\\) of the %s (in %s) is…', 'Estimate the lower quartile \\(Q_1\\) of the %s (in %s).'])
    qv = V(lv, ['Tìm tứ phân vị thứ nhất \\(Q_1\\) của %s (đơn vị %s).', 'Tứ phân vị thứ nhất \\(Q_1\\) của %s (đơn vị %s) là…', 'Ước lượng tứ phân vị thứ nhất \\(Q_1\\) của %s (đơn vị %s).'])
    return dict(en='%s %s' % (I(sc, 'en'), qe % (VAR(sc, 'en'), U(sc, 'en'))), vi='%s %s' % (I(sc, 'vi'), qv % (VAR(sc, 'vi'), U(sc, 'vi'))),
                opts=nopts(r, q, hb([t.edge(i), t.median(), wrong_c, q + t.h, Qj(t, 3)]), step=t.h), fig=TB(sc, t), ee=_qsteps(t, 1, 'en'), ev=_qsteps(t, 1, 'vi'))

def b9_q3hist(r, lv, ctx):
    sc = pick(ctx, r); t = mk(r, sc, need=('q1', 'q3')); q = Qj(t, 3); i = qgroup(t, 3)
    qe = V(lv, ['The histogram shows the grouped data. Find the third quartile \\(Q_3\\) of the %s (in %s).', 'Based on the histogram, the third quartile \\(Q_3\\) of the %s (in %s) is…', 'Use the histogram to estimate the upper quartile \\(Q_3\\) of the %s (in %s).'])
    qv = V(lv, ['Biểu đồ tần số biểu diễn mẫu số liệu ghép nhóm. Tìm tứ phân vị thứ ba \\(Q_3\\) của %s (đơn vị %s).', 'Dựa vào biểu đồ tần số, tứ phân vị thứ ba \\(Q_3\\) của %s (đơn vị %s) là…', 'Dùng biểu đồ tần số, ước lượng tứ phân vị thứ ba \\(Q_3\\) của %s (đơn vị %s).'])
    return dict(en='%s %s' % (I(sc, 'en'), qe % (VAR(sc, 'en'), U(sc, 'en'))), vi='%s %s' % (I(sc, 'vi'), qv % (VAR(sc, 'vi'), U(sc, 'vi'))),
                opts=nopts(r, q, hb([t.edge(i + 1), t.edge(i), Qj(t, 1), t.median(), q + t.h]), step=t.h), fig=HIST(sc, t), ee=_qsteps(t, 3, 'en'), ev=_qsteps(t, 3, 'vi'))

def b9_iqr(r, lv, ctx):
    sc = pick(ctx, r); t = mk(r, sc, need=('q1', 'q3')); a, b = Qj(t, 1), Qj(t, 3); d = b - a
    qe = V(lv, ['Find the interquartile range \\(\\Delta_Q\\) of the %s (in %s).', 'The interquartile range of the %s (in %s) is…', 'How large is the interquartile range \\(\\Delta_Q\\) of the %s (in %s)?'])
    qv = V(lv, ['Tìm khoảng tứ phân vị \\(\\Delta_Q\\) của %s (đơn vị %s).', 'Khoảng tứ phân vị của %s (đơn vị %s) là…', 'Khoảng tứ phân vị \\(\\Delta_Q\\) của %s (đơn vị %s) bằng bao nhiêu?'])
    return dict(en='%s %s' % (I(sc, 'en'), qe % (VAR(sc, 'en'), U(sc, 'en'))), vi='%s %s' % (I(sc, 'vi'), qv % (VAR(sc, 'vi'), U(sc, 'vi'))),
                opts=nopts(r, d, hb([a + b, t.rng(), b - t.median(), d + t.h, (a + b) / 2]), step=t.h), fig=TB(sc, t),
                ee='\\(Q_1=%s\\), \\(Q_3=%s\\), \\(\\Delta_Q=Q_3-Q_1=%s\\).' % (ne(a), ne(b), ne(d)), ev='\\(Q_1=%s\\), \\(Q_3=%s\\), \\(\\Delta_Q=Q_3-Q_1=%s\\).' % (nv(a), nv(b), nv(d)))

def b9_q1group(r, lv, ctx):
    sc = pick(ctx, r); t = mk(r, sc, cond=lambda t: 0 < qgroup(t, 1) < t.k - 1); i = qgroup(t, 1)
    qe = V(lv, ['Which group contains the first quartile \\(Q_1\\)?', 'The first quartile \\(Q_1\\) lies in the group…', 'In which group is \\(Q_1\\)?'])
    qv = V(lv, ['Nhóm nào chứa tứ phân vị thứ nhất \\(Q_1\\)?', 'Tứ phân vị thứ nhất \\(Q_1\\) thuộc nhóm…', '\\(Q_1\\) nằm trong nhóm nào?'])
    others = [j for j in range(t.k) if j != i]; r.shuffle(others)
    opts = [GR(t, i, 'en')] + [GR(t, j, 'en') for j in others[:3]]
    opts = [tt(o, o.replace('.', '{,}')) if '.' in o else o for o in opts]
    cum = ', '.join(str(t.cum(j + 1)) for j in range(t.k))
    return dict(en='%s %s' % (I(sc, 'en'), qe), vi='%s %s' % (I(sc, 'vi'), qv), opts=opts, fig=TB(sc, t),
                ee='\\(\\frac n4=%s\\); cumulative frequencies %s: the first one \\(\\ge%s\\) belongs to %s.' % (ne(F(t.n, 4)), cum, ne(F(t.n, 4)), GR(t, i, 'en')),
                ev='\\(\\frac n4=%s\\); tần số tích lũy %s: số đầu tiên \\(\\ge%s\\) ứng với nhóm %s.' % (nv(F(t.n, 4)), cum, nv(F(t.n, 4)), GR(t, i, 'vi')))

def b9_compare(r, lv, ctx):
    sc = pick(ctx, r)
    for _ in range(200):
        t1 = mk(r, sc, need=('q1', 'q3')); t2 = mk(r, sc, need=('q1', 'q3'), cond=lambda u: u.h == t1.h and u.u0 == t1.u0 and u.k == t1.k)
        if t1.iqr() != t2.iqr() and t1.fs != t2.fs: break
    else: raise AssertionError
    d1, d2 = t1.iqr(), t2.iqr(); A_ = 'A' if d1 < d2 else 'B'; B_ = 'B' if A_ == 'A' else 'A'
    S = [('Sample %s is more concentrated in the middle half.' % A_, 'Mẫu %s tập trung hơn ở nửa giữa số liệu.' % A_),
         ('Sample %s is more concentrated in the middle half.' % B_, 'Mẫu %s tập trung hơn ở nửa giữa số liệu.' % B_),
         ('The two samples are equally spread out.', 'Hai mẫu phân tán như nhau.'),
         ('Sample %s is more concentrated because its range is smaller.' % B_, 'Mẫu %s tập trung hơn vì khoảng biến thiên nhỏ hơn.' % B_)]
    qe = V(lv, ['Two samples were taken. Judging by the interquartile range, which statement is correct?', 'Compare the interquartile ranges of the two samples. Which conclusion is right?', 'Which sample has the smaller spread in its middle half?'])
    qv = V(lv, ['Lấy hai mẫu số liệu. Dựa vào khoảng tứ phân vị, khẳng định nào đúng?', 'So sánh khoảng tứ phân vị của hai mẫu. Kết luận nào đúng?', 'Mẫu nào có nửa giữa số liệu ít phân tán hơn?'])
    return dict(en='%s %s' % (I(sc, 'en'), qe), vi='%s %s' % (I(sc, 'vi'), qv), opts=[tt(*s) for s in S], fig=two_tabs(sc, t1, t2),
                ee='\\(\\Delta_Q(A)=%s\\), \\(\\Delta_Q(B)=%s\\); the smaller \\(\\Delta_Q\\) means more concentrated.' % (ne(d1), ne(d2)),
                ev='\\(\\Delta_Q(A)=%s\\), \\(\\Delta_Q(B)=%s\\); \\(\\Delta_Q\\) nhỏ hơn thì tập trung hơn.' % (nv(d1), nv(d2)))

def b9_tf_q3group(r, lv, ctx):
    sc = pick(ctx, r); t = mk(r, sc, cond=lambda t: 0 < qgroup(t, 3) < t.k - 1); i = qgroup(t, 3); truth = r.random() < .5
    j = i if truth else r.choice([i - 1, i + 1])
    qe = V(lv, ['The third quartile \\(Q_3\\) lies in the group %s.', '\\(Q_3\\) belongs to the group %s.', 'The group %s contains the upper quartile \\(Q_3\\).'])
    qv = V(lv, ['Tứ phân vị thứ ba \\(Q_3\\) thuộc nhóm %s.', '\\(Q_3\\) nằm trong nhóm %s.', 'Nhóm %s chứa tứ phân vị thứ ba \\(Q_3\\).'])
    cum = ', '.join(str(t.cum(k + 1)) for k in range(t.k))
    return dict(en='%s %s' % (I(sc, 'en'), qe % GR(t, j, 'en')), vi='%s %s' % (I(sc, 'vi'), qv % GR(t, j, 'vi')), truth=truth, fig=TB(sc, t),
                ee='\\(\\frac{3n}4=%s\\); cumulative frequencies %s, so \\(Q_3\\) is in %s.' % (ne(F(3 * t.n, 4)), cum, GR(t, i, 'en')),
                ev='\\(\\frac{3n}4=%s\\); tần số tích lũy %s nên \\(Q_3\\) thuộc nhóm %s.' % (nv(F(3 * t.n, 4)), cum, GR(t, i, 'vi')))

B9_CONCEPT = [(('For every grouped sample, \\(\\Delta_Q\\le R\\).', 'Với mọi mẫu số liệu ghép nhóm, \\(\\Delta_Q\\le R\\).'), True, ('\\(Q_1\\) and \\(Q_3\\) lie between the two ends, so \\(Q_3-Q_1\\le R\\).', '\\(Q_1\\), \\(Q_3\\) nằm giữa hai đầu mút nên \\(Q_3-Q_1\\le R\\).')),
              (('Two samples with the same range always have the same interquartile range.', 'Hai mẫu có cùng khoảng biến thiên thì luôn có cùng khoảng tứ phân vị.'), False, ('\\(R\\) only uses the two ends; \\(\\Delta_Q\\) depends on how the middle half is spread.', '\\(R\\) chỉ dùng hai đầu mút; \\(\\Delta_Q\\) phụ thuộc cách phân bố của nửa giữa.')),
              (('The interquartile range is hardly affected by a few very large or very small values.', 'Khoảng tứ phân vị hầu như không bị ảnh hưởng bởi một vài giá trị rất lớn hoặc rất nhỏ.'), True, ('\\(\\Delta_Q\\) only describes the middle 50% of the data.', '\\(\\Delta_Q\\) chỉ mô tả 50% số liệu ở giữa.'))]
def b9_tf_concept(r, lv, ctx):
    (e, v), truth, (ee, ev) = B9_CONCEPT[(lv - 1) % 3]
    return dict(en=e, vi=v, truth=truth, ee=ee, ev=ev)

def b9_tf_meaning(r, lv, ctx):
    sc = pick(ctx, r); t = mk(r, sc, need=('q1', 'q3', 'median')); truth = r.random() < .5
    q3 = Qj(t, 3); val = q3 if truth else r.choice([Qj(t, 1), t.median()])
    if val == q3 and not truth: raise AssertionError
    qe = V(lv, ['About 25%% of the %s have a %s of at least %s %s.', 'Roughly one quarter of the %s have a %s of %s %s or more.', 'About 75%% of the %s have a %s below %s %s.'])
    qv = V(lv, ['Khoảng 25%% số %s có %s từ %s %s trở lên.', 'Khoảng một phần tư số %s có %s từ %s %s trở lên.', 'Khoảng 75%% số %s có %s dưới %s %s.'])
    return dict(en='%s %s' % (I(sc, 'en'), qe % (ENT(sc, 'en'), VAR(sc, 'en'), M(ne(val)), U(sc, 'en'))), vi='%s %s' % (I(sc, 'vi'), qv % (ENT(sc, 'vi'), VAR(sc, 'vi'), M(nv(val)), U(sc, 'vi'))),
                truth=truth, fig=TB(sc, t),
                ee='\\(Q_3=%s\\): about 75%% of the values are below \\(Q_3\\) and about 25%% are at least \\(Q_3\\).' % ne(q3), ev='\\(Q_3=%s\\): khoảng 75%% giá trị nhỏ hơn \\(Q_3\\), khoảng 25%% giá trị từ \\(Q_3\\) trở lên.' % nv(q3))

def b9_sh_q2(r, lv, ctx):
    sc = pick(ctx, r, lambda s: s['k'] not in ('bulb', 'power')); t = mk(r, sc, need=('median',), cond=lambda t: shortok(t.median())); m = t.median()
    qe = V(lv, ['Find the second quartile \\(Q_2\\) of the %s (in %s).', 'Calculate \\(Q_2\\) of the %s (in %s).', 'What is the second quartile \\(Q_2\\) of the %s (in %s)?'])
    qv = V(lv, ['Tìm tứ phân vị thứ hai \\(Q_2\\) của %s (đơn vị %s).', 'Tính \\(Q_2\\) của %s (đơn vị %s).', 'Tứ phân vị thứ hai \\(Q_2\\) của %s (đơn vị %s) bằng bao nhiêu?'])
    return dict(en='%s %s' % (I(sc, 'en'), qe % (VAR(sc, 'en'), U(sc, 'en'))), vi='%s %s' % (I(sc, 'vi'), qv % (VAR(sc, 'vi'), U(sc, 'vi'))), key=key(m), fig=TB(sc, t),
                ee='\\(Q_2\\) is the median. ' + _qsteps(t, 2, 'en'), ev='\\(Q_2\\) là trung vị. ' + _qsteps(t, 2, 'vi'),
                hint=('Enter a number (use a decimal point if needed).', 'Nhập một số (dùng dấu phẩy thập phân nếu cần).'))

def b9_sh_shift(r, lv, ctx):
    sc = pick(ctx, r, lambda s: s['k'] not in ('bulb', 'power')); c = r.choice([2, 3, 4, 5]) if sc['k'] != 'age' else r.choice([1, 2, 3])
    t = mk(r, sc, need=('q3',), cond=lambda t: shortok(Qj(t, 3) + c)); q = Qj(t, 3) + c
    if sc.get('shift'): se, sv = sc['shift'][0][0].format(c=c), sc['shift'][0][1].format(c=c)
    elif sc['k'] == 'age': se, sv = 'The same employees are surveyed again %d years later.' % c, 'Khảo sát lại chính các nhân viên đó sau %d năm.' % c
    else: se, sv = 'Suppose every value increases by %d %s.' % (c, sc['unit']), 'Giả sử mọi giá trị đều tăng thêm %d %s.' % (c, sc['uv'])
    qe = V(lv, ['%s Find the new third quartile \\(Q_3\\).', '%s Calculate \\(Q_3\\) of the new data.', '%s What is the third quartile \\(Q_3\\) after the change?'])
    qv = V(lv, ['%s Tìm tứ phân vị thứ ba \\(Q_3\\) mới.', '%s Tính \\(Q_3\\) của số liệu mới.', '%s Tứ phân vị thứ ba \\(Q_3\\) sau khi thay đổi bằng bao nhiêu?'])
    return dict(en='%s %s' % (I(sc, 'en'), qe % se), vi='%s %s' % (I(sc, 'vi'), qv % sv), key=key(q), fig=TB(sc, t),
                ee='Old \\(Q_3=%s\\); adding \\(%d\\) to every value moves \\(Q_3\\) by \\(%d\\): \\(%s\\).' % (ne(Qj(t, 3)), c, c, ne(q)),
                ev='\\(Q_3\\) cũ \\(=%s\\); cộng \\(%d\\) vào mọi giá trị thì \\(Q_3\\) tăng \\(%d\\): \\(%s\\).' % (nv(Qj(t, 3)), c, c, nv(q)))

def b9_sh_missing(r, lv, ctx):
    sc = pick(ctx, r)
    for _ in range(400):
        t = mk(r, sc, need=('q1',)); u = t.k - 1
        if qgroup(t, 1) == u: continue
        q = Qj(t, 1); sols = [x for x in range(1, 41) if GT(t.u0, t.h, t.fs[:u] + [x]).q1() == q]
        if sols == [t.fs[u]]: break
    else: raise AssertionError
    qe = V(lv, ['The first quartile of the data is \\(Q_1=%s\\). Find \\(x\\).', 'Given \\(Q_1=%s\\), find the missing frequency \\(x\\).', 'The lower quartile equals \\(%s\\). What is \\(x\\)?'])
    qv = V(lv, ['Tứ phân vị thứ nhất của mẫu là \\(Q_1=%s\\). Tìm \\(x\\).', 'Biết \\(Q_1=%s\\), tìm tần số \\(x\\) còn thiếu.', 'Tứ phân vị thứ nhất bằng \\(%s\\). Tìm \\(x\\).'])
    i = qgroup(t, 1)
    return dict(en='%s %s' % (I(sc, 'en'), qe % ne(q)), vi='%s %s' % (I(sc, 'vi'), qv % nv(q)), key=key(t.fs[u]),
                fig=(gtab(sc, t, 'en', unknown=u).replace('<td class="mbl-freq-tot">\\(n=%d\\)</td>' % t.n, '<td class="mbl-freq-tot">\\(n=%d+x\\)</td>' % (t.n - t.fs[u])),
                     gtab(sc, t, 'vi', unknown=u).replace('<td class="mbl-freq-tot">\\(n=%d\\)</td>' % t.n, '<td class="mbl-freq-tot">\\(n=%d+x\\)</td>' % (t.n - t.fs[u]))),
                ee='\\(Q_1\\) is in %s: \\(%s=%s+\\dfrac{\\frac n4-%d}{%d}\\cdot%s\\) gives \\(\\frac n4=%s\\), \\(n=%d\\), so \\(x=%d\\).' % (GR(t, i, 'en'), ne(q), ne(t.edge(i)), t.cum(i), t.fs[i], ne(t.h), ne(F(t.n, 4)), t.n, t.fs[u]),
                ev='\\(Q_1\\) thuộc nhóm %s: \\(%s=%s+\\dfrac{\\frac n4-%d}{%d}\\cdot%s\\) cho \\(\\frac n4=%s\\), \\(n=%d\\), nên \\(x=%d\\).' % (GR(t, i, 'vi'), nv(q), nv(t.edge(i)), t.cum(i), t.fs[i], nv(t.h), nv(F(t.n, 4)), t.n, t.fs[u]))

# ---- phần D, Bài 9
def b9_d_error(r, lv, ctx):
    sc = pick(ctx, r); t = mk(r, sc, need=('q1',), cond=lambda t: qgroup(t, 1) > 0); i = qgroup(t, 1); q = Qj(t, 1)
    bad = t.edge(i) + (F(t.n, 4) - t.cum(i + 1)) / t.fs[i] * t.h
    def steps(lang):
        N = ne if lang == 'en' else nv
        s1 = '\\(n=%d\\), \\(\\frac n4=%s\\).' % (t.n, N(F(t.n, 4)))
        s2 = ('the group containing \\(Q_1\\) is %s.' if lang == 'en' else 'nhóm chứa \\(Q_1\\) là %s.') % GR(t, i, lang)
        s3 = '\\(Q_1=%s+\\dfrac{%s-%d}{%d}\\cdot%s=%s\\).' % (N(t.edge(i)), N(F(t.n, 4)), t.cum(i + 1), t.fs[i], N(t.h), N(bad))
        return ('A student found \\(Q_1\\) as follows. Step 1: %s Step 2: %s Step 3: %s Which statement is correct?' if lang == 'en' else
                'Một bạn tìm \\(Q_1\\) như sau. Bước 1: %s Bước 2: %s Bước 3: %s Nhận xét nào đúng?') % (s1, s2, s3)
    S = [('Step 3 is wrong: \\(C\\) must be the cumulative frequency before the group.', 'Bước 3 sai: \\(C\\) phải là tần số tích lũy của các nhóm đứng trước.'),
         ('Step 1 is wrong.', 'Bước 1 sai.'), ('Step 2 is wrong.', 'Bước 2 sai.'), ('All three steps are correct.', 'Cả ba bước đều đúng.')]
    return dict(en='%s %s' % (I(sc, 'en'), steps('en')), vi='%s %s' % (I(sc, 'vi'), steps('vi')), opts=[tt(*s) for s in S], fig=TB(sc, t),
                ee='\\(C=%d\\) (before the group), so \\(Q_1=%s\\), not \\(%s\\).' % (t.cum(i), ne(q), ne(bad)), ev='\\(C=%d\\) (tích lũy trước nhóm) nên \\(Q_1=%s\\), không phải \\(%s\\).' % (t.cum(i), nv(q), nv(bad)))

D9_CTX = [(('two classes', 'hai lớp'), ('test scores', 'điểm kiểm tra'), 'points', 'điểm'), (('two shops', 'hai cửa hàng'), ('waiting times', 'thời gian chờ'), 'minutes', 'phút'),
          (('two farms', 'hai trang trại'), ('egg masses', 'khối lượng trứng'), 'g', 'g')]
def b9_d_rq(r, lv, ctx):
    (pe, pv), (ve, vv), ue, uv = D9_CTX[(lv - 1) % 3]
    for _ in range(100):
        R1, R2 = sorted(r.sample(range(20, 61, 5), 2), reverse=True); d1 = r.choice(range(6, 15)); d2 = d1 + r.choice(range(3, 9))
        if d2 < R2: break
    S = [('X has the larger range, but its middle half is more concentrated than that of Y.', 'X có khoảng biến thiên lớn hơn nhưng nửa giữa số liệu của X tập trung hơn Y.'),
         ('X is more spread out in every sense.', 'X phân tán hơn Y theo mọi nghĩa.'), ('Y has the larger range.', 'Y có khoảng biến thiên lớn hơn.'),
         ('The middle half of Y is more concentrated than that of X.', 'Nửa giữa số liệu của Y tập trung hơn X.')]
    return dict(en='The %s of %s were compared. Sample X: \\(R=%d\\), \\(\\Delta_Q=%d\\) (%s). Sample Y: \\(R=%d\\), \\(\\Delta_Q=%d\\) (%s). Which statement is correct?' % (ve, pe, R1, d1, ue, R2, d2, ue),
                vi='So sánh %s của %s. Mẫu X: \\(R=%d\\), \\(\\Delta_Q=%d\\) (%s). Mẫu Y: \\(R=%d\\), \\(\\Delta_Q=%d\\) (%s). Khẳng định nào đúng?' % (vv, pv, R1, d1, uv, R2, d2, uv),
                opts=[tt(*s) for s in S], ee='\\(R\\): \\(%d\\gt%d\\); \\(\\Delta_Q\\): \\(%d\\lt%d\\).' % (R1, R2, d1, d2), ev='\\(R\\): \\(%d\\gt%d\\); \\(\\Delta_Q\\): \\(%d\\lt%d\\).' % (R1, R2, d1, d2))

D9_UNIT = [(('hours', 'giờ'), ('minutes', 'phút'), 60, ('The charging times of phones', 'Thời gian sạc pin của các điện thoại')),
           (('m', 'm'), ('cm', 'cm'), 100, ('The long jumps of students', 'Thành tích nhảy xa của học sinh')),
           (('kg', 'kg'), ('g', 'g'), 1000, ('The masses of watermelons', 'Khối lượng các quả dưa hấu'))]
def b9_d_scale(r, lv, ctx):
    (ue, uv), (we, wv), k, (ce, cv) = D9_UNIT[(lv - 1) % 3]
    d = F(r.choice([5, 6, 8, 12, 15, 25]), 10); good = d * k
    return dict(en='%s were grouped and the interquartile range is \\(\\Delta_Q=%s\\) %s. If all values are written in %s, the interquartile range is…' % (ce, ne(d), ue, we),
                vi='%s được ghép nhóm và có khoảng tứ phân vị \\(\\Delta_Q=%s\\) %s. Nếu đổi mọi giá trị sang đơn vị %s thì khoảng tứ phân vị bằng…' % (cv, nv(d), uv, wv),
                opts=[tt('\\(%s\\) %s' % (ne(x), we), '\\(%s\\) %s' % (nv(x), wv)) for x in (good, d, d + k, good * k)],
                ee='Every value is multiplied by \\(%d\\), so \\(Q_1\\), \\(Q_3\\) and \\(\\Delta_Q\\) are multiplied by \\(%d\\): \\(%s\\).' % (k, k, ne(good)),
                ev='Mọi giá trị nhân với \\(%d\\) nên \\(Q_1\\), \\(Q_3\\) và \\(\\Delta_Q\\) cũng nhân với \\(%d\\): \\(%s\\).' % (k, k, nv(good)))

def b9_d_middle(r, lv, ctx):
    sc = pick(ctx, r); t = mk(r, sc, need=('q1', 'q3'), cond=lambda t: t.n % 4 == 0); a, b = Qj(t, 1), Qj(t, 3)
    qe = V(lv, ['About how many %s have a %s between \\(Q_1=%s\\) and \\(Q_3=%s\\)?', 'Estimate the number of %s whose %s lies from \\(Q_1=%s\\) to \\(Q_3=%s\\).', 'Roughly how many %s have a %s in the interval \\([%s;\\,%s)\\)?'])
    qv = V(lv, ['Khoảng bao nhiêu %s có %s nằm giữa \\(Q_1=%s\\) và \\(Q_3=%s\\)?', 'Ước lượng số %s có %s từ \\(Q_1=%s\\) đến \\(Q_3=%s\\).', 'Có khoảng bao nhiêu %s có %s thuộc nửa khoảng \\([%s;\\,%s)\\)?'])
    return dict(en='%s %s' % (I(sc, 'en'), qe % (ENT(sc, 'en'), VAR(sc, 'en'), ne(a), ne(b))), vi='%s %s' % (I(sc, 'vi'), qv % (ENT(sc, 'vi'), VAR(sc, 'vi'), nv(a), nv(b))),
                opts=nopts(r, t.n // 2, [t.n // 4, 3 * t.n // 4, t.n, t.n // 2 + t.fs[0]]), fig=TB(sc, t),
                ee='Between \\(Q_1\\) and \\(Q_3\\) lie about 50%% of the data: \\(\\frac{%d}{2}=%d\\).' % (t.n, t.n // 2), ev='Giữa \\(Q_1\\) và \\(Q_3\\) có khoảng 50%% số liệu: \\(\\frac{%d}{2}=%d\\).' % (t.n, t.n // 2))

def b9_d_impossible(r, lv, ctx):
    sc = pick(ctx, r); t = mk(r, sc, need=('q1', 'q3')); R = t.rng(); d = t.iqr()
    bad = R + r.choice([1, 2]) * t.h
    cands = sorted(set([d, F(R, 2), max(t.h, d - t.h)]))
    if len(cands) < 3: raise AssertionError
    qe = V(lv, ['Without computing the quartiles, which value can NOT be the interquartile range of this sample (in %s)?', 'A student reports the interquartile range of the data (in %s). Which reported value is certainly wrong?', 'Which of the following is impossible as the interquartile range \\(\\Delta_Q\\) (in %s)?'])
    qv = V(lv, ['Không cần tính tứ phân vị, giá trị nào KHÔNG thể là khoảng tứ phân vị của mẫu này (đơn vị %s)?', 'Một bạn báo cáo khoảng tứ phân vị của mẫu (đơn vị %s). Giá trị nào chắc chắn sai?', 'Giá trị nào sau đây không thể là khoảng tứ phân vị \\(\\Delta_Q\\) (đơn vị %s)?'])
    return dict(en='%s %s' % (I(sc, 'en'), qe % U(sc, 'en')), vi='%s %s' % (I(sc, 'vi'), qv % U(sc, 'vi')), opts=[nopt(bad)] + [nopt(c) for c in cands[:3]], fig=TB(sc, t),
                ee='\\(\\Delta_Q\\le R=%s-%s=%s\\), so \\(%s\\) is impossible.' % (ne(t.edge(t.k)), ne(t.edge(0)), ne(R), ne(bad)), ev='\\(\\Delta_Q\\le R=%s-%s=%s\\) nên \\(%s\\) không thể xảy ra.' % (nv(t.edge(t.k)), nv(t.edge(0)), nv(R), nv(bad)))

def b9_d_cum(r, lv, ctx):
    sc = pick(ctx, r); t = mk(r, sc, need=('q1', 'q3')); q = Qj(t, 3); i = qgroup(t, 3)
    wrong = t.edge(i) + (F(3 * t.n, 4) - t.cum(i)) / t.cum(i + 1) * t.h
    qe = V(lv, ['The table gives the cumulative frequencies. Find the third quartile \\(Q_3\\) (in %s).', 'Using the cumulative frequency table, \\(Q_3\\) (in %s) is…', 'From the cumulative frequencies, estimate \\(Q_3\\) (in %s).'])
    qv = V(lv, ['Bảng cho tần số tích lũy. Tìm tứ phân vị thứ ba \\(Q_3\\) (đơn vị %s).', 'Dựa vào bảng tần số tích lũy, \\(Q_3\\) (đơn vị %s) là…', 'Từ tần số tích lũy, ước lượng \\(Q_3\\) (đơn vị %s).'])
    return dict(en='%s %s' % (I(sc, 'en'), qe % U(sc, 'en')), vi='%s %s' % (I(sc, 'vi'), qv % U(sc, 'vi')), opts=nopts(r, q, hb([wrong, t.edge(i), t.edge(i + 1), q + t.h, Qj(t, 1)]), step=t.h),
                fig=(cumtab(sc, t, 'en'), cumtab(sc, t, 'vi')),
                ee='\\(n=%d\\) (last cumulative frequency); frequency of %s is \\(%d-%d=%d\\). ' % (t.n, GR(t, i, 'en'), t.cum(i + 1), t.cum(i), t.fs[i]) + _qsteps(t, 3, 'en'),
                ev='\\(n=%d\\) (tần số tích lũy cuối); tần số nhóm %s là \\(%d-%d=%d\\). ' % (t.n, GR(t, i, 'vi'), t.cum(i + 1), t.cum(i), t.fs[i]) + _qsteps(t, 3, 'vi'))

def b9_d_width(r, lv, ctx):
    k = r.choice([4, 5, 6]); h = r.choice([2, 4, 5, 10]); u0 = r.choice([0, 10, 20, 40, 100]); R = k * h; j = r.choice([2, 3])
    good = (u0 + (j - 1) * h, u0 + j * h)
    C = [good, (u0 + j * h, u0 + (j + 1) * h), (u0 + (j - 1) * R // k + R // 2, u0 + j * h + R // 2), (u0 + (j - 1) * (h + 1), u0 + j * (h + 1))]
    ords = {2: ('second', 'thứ hai'), 3: ('third', 'thứ ba')}[j]
    qe = V(lv, ['A sample is grouped into %d groups of equal width; the first group starts at %d and the range is \\(R=%d\\). The %s group is…', 'Grouped data have %d groups of the same width, starting at %d, with range %d. Which interval is the %s group?', 'The range of a sample with %d equal groups starting from %d is %d. Find the %s group.'])
    qv = V(lv, ['Mẫu số liệu được chia thành %d nhóm có độ dài bằng nhau; nhóm đầu bắt đầu từ %d và khoảng biến thiên \\(R=%d\\). Nhóm %s là…', 'Mẫu ghép nhóm có %d nhóm cùng độ dài, bắt đầu từ %d, khoảng biến thiên bằng %d. Nhóm %s là nửa khoảng nào?', 'Khoảng biến thiên của mẫu có %d nhóm đều nhau bắt đầu từ %d là %d. Tìm nhóm %s.'])
    opts = list(dict.fromkeys('\\([%d;\\,%d)\\)' % c for c in C))
    if len(opts) < 4: raise AssertionError
    return dict(en=qe % (k, u0, R, ords[0]), vi=qv % (k, u0, R, ords[1]), opts=opts,
                ee='\\(h=\\frac Rk=\\frac{%d}{%d}=%d\\); group %d is \\([%d;\\,%d)\\).' % (R, k, h, j, good[0], good[1]), ev='\\(h=\\frac Rk=\\frac{%d}{%d}=%d\\); nhóm %d là \\([%d;\\,%d)\\).' % (R, k, h, j, good[0], good[1]))

def b9_d_extreme(r, lv, ctx):
    sc = pick(ctx, r); t = mk(r, sc); ext = t.edge(t.k) + r.choice([3, 4, 5]) * t.h
    qe = V(lv, ['One more %s with an unusually large %s of %s %s is added. Which measure changes the most?', 'A new value %s %s (very large) joins the sample. Which measure is affected most?', 'If a %s with %s equal to %s %s is added, which of these changes most?'])
    qv = V(lv, ['Thêm một %s có %s rất lớn là %s %s. Số đặc trưng nào thay đổi nhiều nhất?', 'Mẫu có thêm giá trị %s %s (rất lớn). Số đặc trưng nào bị ảnh hưởng nhiều nhất?', 'Nếu thêm một %s có %s bằng %s %s thì số nào thay đổi nhiều nhất?'])
    if lv == 2: en = qe % (M(ne(ext)), sc['unit']); vi = qv % (M(nv(ext)), sc['uv'])
    else: en = qe % (sc['ent1'][0], VAR(sc, 'en'), M(ne(ext)), sc['unit']); vi = qv % (sc['ent1'][1], VAR(sc, 'vi'), M(nv(ext)), sc['uv'])
    S = [('The range \\(R\\)', 'Khoảng biến thiên \\(R\\)'), ('The interquartile range \\(\\Delta_Q\\)', 'Khoảng tứ phân vị \\(\\Delta_Q\\)'), ('The first quartile \\(Q_1\\)', 'Tứ phân vị thứ nhất \\(Q_1\\)'), ('The median \\(Q_2\\)', 'Trung vị \\(Q_2\\)')]
    return dict(en='%s %s' % (I(sc, 'en'), en), vi='%s %s' % (I(sc, 'vi'), vi), opts=[tt(*s) for s in S], fig=TB(sc, t),
                ee='\\(R\\) grows from \\(%s\\) to at least \\(%s\\); the quartiles move only a little (one value among \\(%d\\)).' % (ne(t.rng()), ne(ext - t.edge(0)), t.n + 1),
                ev='\\(R\\) tăng từ \\(%s\\) lên ít nhất \\(%s\\); các tứ phân vị chỉ dịch chuyển rất ít (một giá trị trong \\(%d\\) giá trị).' % (nv(t.rng()), nv(ext - t.edge(0)), t.n + 1))

B9 = dict(A=[b9_range, b9_q1, b9_q3hist, b9_iqr, b9_q1group, b9_compare], B=[b9_tf_q3group, b9_tf_concept, b9_tf_meaning], C=[b9_sh_q2, b9_sh_shift, b9_sh_missing],
          D=[b9_d_error, b9_d_rq, b9_d_scale, b9_d_middle, b9_d_impossible, b9_d_cum, b9_d_width, b9_d_extreme])

# ================================================================ BÀI 10 – Phương sai, độ lệch chuẩn
def vt(r, sc, cond=lambda t: True, **kw):
    """Bảng có số trung bình và phương sai 'đẹp' (≤ 2 chữ số thập phân, ≤ 4 kí tự)."""
    for _ in range(4000):
        try: t = gq.mkt(r, sc, need=('mean',), **kw)
        except AssertionError: continue
        v = t.var()
        if (100 * v).denominator == 1 and shortok(v) and cond(t): return t
    raise AssertionError('vt')

def vsteps(t, lang):
    N = ne if lang == 'en' else nv; m = t.mean(); s2 = sum(f * t.mid(i) ** 2 for i, f in enumerate(t.fs)) / t.n
    return '%s \\(%s\\); \\(\\bar x=%s\\); \\(s^2=\\dfrac1n\\sum n_ix_i^2-\\bar x^2=%s-%s^2=%s\\).' % ('Midpoints' if lang == 'en' else 'Giá trị đại diện', ';\\ '.join(N(t.mid(i)) for i in range(t.k)), N(m), N(s2), N(m), N(t.var()))

def b10_var(r, lv, ctx):
    sc = pick(ctx, r); t = vt(r, sc); v = t.var(); s2 = v + t.mean() ** 2
    qe = V(lv, ['Find the variance \\(s^2\\) of the %s.', 'The variance of the %s is…', 'Estimate the variance \\(s^2\\) of the %s from the grouped data.'])
    qv = V(lv, ['Tìm phương sai \\(s^2\\) của %s.', 'Phương sai của %s là…', 'Ước lượng phương sai \\(s^2\\) của %s từ mẫu ghép nhóm.'])
    return dict(en='%s %s' % (I(sc, 'en'), qe % VAR(sc, 'en')), vi='%s %s' % (I(sc, 'vi'), qv % VAR(sc, 'vi')), opts=nopts(r, v, [x for x in [s2, v * t.n / (t.n - 1), 2 * v, v + t.h, v - t.h] if (100 * x).denominator == 1], step=1), fig=TB(sc, t),
                ee=vsteps(t, 'en'), ev=vsteps(t, 'vi'))

B10_SUM = [(('the masses (kg) of', 'khối lượng (kg) của'), ('pigs on a farm', 'đàn lợn ở một trang trại'), 'kg'), (('the daily sales (million VND) of', 'doanh thu mỗi ngày (triệu đồng) của'), ('a shop', 'một cửa hàng'), 'million VND'),
           (('the speeds (km/h) of', 'tốc độ (km/h) của'), ('cars passing a speed camera', 'các ô tô đi qua trạm đo tốc độ'), 'km/h')]
def b10_sums(r, lv, ctx):
    (ae, av), (be, bv), u = B10_SUM[(lv - 1) % 3]
    n = r.choice([20, 25, 40, 50]); m = r.choice(range(30, 81)); s = r.choice([2, 3, 4, 5, 6, 7]); S1 = n * m; S2 = n * (s * s + m * m)
    return dict(en='For %s %s, a grouped sample of size \\(n=%d\\) gives \\(\\sum n_ix_i=%d\\) and \\(\\sum n_ix_i^2=%d\\). The standard deviation is…' % (ae, be, n, S1, S2),
                vi='Với %s %s, mẫu ghép nhóm cỡ \\(n=%d\\) có \\(\\sum n_ix_i=%d\\) và \\(\\sum n_ix_i^2=%d\\). Độ lệch chuẩn của mẫu là…' % (av, bv, n, S1, S2),
                opts=nopts(r, s, [s * s, F(S2, n) - m, s + 1, m], step=1),
                ee='\\(\\bar x=%d\\), \\(s^2=\\frac{%d}{%d}-%d^2=%d\\), \\(s=%d\\).' % (m, S2, n, m, s * s, s), ev='\\(\\bar x=%d\\), \\(s^2=\\frac{%d}{%d}-%d^2=%d\\), \\(s=%d\\).' % (m, S2, n, m, s * s, s))

B10_UNIT = [(('heights of seedlings', 'chiều cao cây giống'), ('cm', 'cm'), ('cm²', 'cm²')), (('masses of fish', 'khối lượng cá'), ('kg', 'kg'), ('kg²', 'kg²')), (('daily rainfall', 'lượng mưa mỗi ngày'), ('mm', 'mm'), ('mm²', 'mm²'))]
def b10_unit(r, lv, ctx):
    (ve, vv), (ue, uv), (we, wv) = B10_UNIT[(lv - 1) % 3]; s = F(r.choice([12, 15, 18, 25, 35, 45, 6, 9]), 10); v = s * s
    qe = 'The variance of the %s is \\(s^2=%s\\) %s. The standard deviation is…' % (ve, ne(v), we)
    qv = 'Phương sai của %s là \\(s^2=%s\\) %s. Độ lệch chuẩn là…' % (vv, nv(v), wv)
    O = [(s, ue), (v, ue), (s, we), (v / 2, ue)]
    return dict(en=qe, vi=qv, opts=[tt('\\(%s\\) %s' % (ne(x), a), '\\(%s\\) %s' % (nv(x), {ue: uv, we: wv}[a])) for x, a in O],
                ee='\\(s=\\sqrt{%s}=%s\\); \\(s\\) has the same unit as the data (%s).' % (ne(v), ne(s), ue), ev='\\(s=\\sqrt{%s}=%s\\); \\(s\\) có cùng đơn vị với số liệu (%s).' % (nv(v), nv(s), uv))

B10_CMP = [(('Two machines fill bottles of water (ml).', 'Hai máy chiết rót nước vào chai (ml).'), ('machine', 'máy'), ('more stable', 'ổn định hơn')),
           (('Two rice varieties were planted on several fields; yields are in quintals per hectare.', 'Hai giống lúa được trồng trên nhiều thửa ruộng; năng suất tính theo tạ/ha.'), ('variety', 'giống lúa'), ('more stable yield', 'năng suất ổn định hơn')),
           (('Two athletes ran the 100 m many times (seconds).', 'Hai vận động viên chạy 100 m nhiều lần (giây).'), ('athlete', 'vận động viên'), ('more consistent results', 'thành tích ổn định hơn'))]
def b10_compare(r, lv, ctx):
    (ie, iv), (ne_, nv_), (ce, cv) = B10_CMP[(lv - 1) % 3]
    base = {0: 500, 1: 60, 2: 13}[(lv - 1) % 3]; m1 = F(base * 10 + r.randint(-5, 5), 10); m2 = m1 + F(r.choice([2, 3, 4, 5]), 10) * r.choice([1, -1])
    s1 = F(r.randint(5, 30), 10); s2 = s1 + F(r.randint(3, 15), 10)
    if r.random() < .5: (m1, s1), (m2, s2) = (m2, s2), (m1, s1)
    better = 'A' if s1 < s2 else 'B'; worse = 'B' if better == 'A' else 'A'; big = 'A' if m1 > m2 else 'B'
    S = [('%s %s has %s.' % (ne_.capitalize(), better, ce), '%s %s có %s.' % (nv_.capitalize(), better, cv)), ('%s %s has %s.' % (ne_.capitalize(), worse, ce), '%s %s có %s.' % (nv_.capitalize(), worse, cv)),
         ('%s %s has %s because its mean is larger.' % (ne_.capitalize(), big, ce), '%s %s có %s vì số trung bình lớn hơn.' % (nv_.capitalize(), big, cv)), ('Both are equally stable.', 'Hai đối tượng ổn định như nhau.')]
    if S[2][0].split(' has')[0] == S[0][0].split(' has')[0]: S[2] = ('The comparison needs the range, not \\(s\\).', 'Cần so sánh khoảng biến thiên chứ không phải \\(s\\).')
    return dict(en='%s A: mean \\(%s\\), \\(s=%s\\). B: mean \\(%s\\), \\(s=%s\\). Which conclusion is right?' % (ie, ne(m1), ne(s1), ne(m2), ne(s2)),
                vi='%s A: trung bình \\(%s\\), \\(s=%s\\). B: trung bình \\(%s\\), \\(s=%s\\). Kết luận nào đúng?' % (iv, nv(m1), nv(s1), nv(m2), nv(s2)),
                opts=[tt(*x) for x in S], ee='The smaller standard deviation means less spread: \\(%s\\lt%s\\).' % (ne(min(s1, s2)), ne(max(s1, s2))), ev='Độ lệch chuẩn nhỏ hơn thì ít phân tán hơn: \\(%s\\lt%s\\).' % (nv(min(s1, s2)), nv(max(s1, s2))))

B10_FORM = ['\\dfrac1n\\sum n_i(x_i-\\bar x)^2', '\\dfrac1n\\sum n_i(x_i-\\bar x)', '\\sqrt{\\dfrac1n\\sum n_i(x_i-\\bar x)^2}', '\\dfrac1n\\sum n_ix_i^2']
def b10_formula(r, lv, ctx):
    k = (lv - 1) % 3
    if k == 0: return dict(en='For grouped data with midpoints \\(x_i\\) and frequencies \\(n_i\\), the variance is…', vi='Với mẫu ghép nhóm có giá trị đại diện \\(x_i\\), tần số \\(n_i\\), phương sai là…',
                           opts=[M(B10_FORM[0]), M(B10_FORM[1]), M(B10_FORM[2]), M(B10_FORM[3])], ee='\\(s^2\\) is the mean of the squared deviations.', ev='\\(s^2\\) là trung bình của bình phương các độ lệch.')
    if k == 1: return dict(en='Which formula gives the standard deviation \\(s\\) of grouped data?', vi='Công thức nào cho độ lệch chuẩn \\(s\\) của mẫu ghép nhóm?',
                           opts=[M(B10_FORM[2]), M(B10_FORM[0]), M(B10_FORM[1]), M('\\dfrac1n\\sum n_i|x_i|')], ee='\\(s=\\sqrt{s^2}\\).', ev='\\(s=\\sqrt{s^2}\\).')
    return dict(en='Which expression is equal to the variance \\(s^2\\) of grouped data?', vi='Biểu thức nào bằng phương sai \\(s^2\\) của mẫu ghép nhóm?',
                opts=[M('\\dfrac1n\\sum n_ix_i^2-\\bar x^2'), M('\\dfrac1n\\sum n_ix_i^2'), M('\\bar x^2-\\dfrac1n\\sum n_ix_i^2'), M('\\dfrac1n\\sum n_ix_i-\\bar x')],
                ee='Expanding \\((x_i-\\bar x)^2\\) gives \\(s^2=\\frac1n\\sum n_ix_i^2-\\bar x^2\\).', ev='Khai triển \\((x_i-\\bar x)^2\\) được \\(s^2=\\frac1n\\sum n_ix_i^2-\\bar x^2\\).')

def b10_two(r, lv, ctx):
    sc = pick(ctx, r); h = r.choice(sc['h']); u0 = r.choice(sc['u0']); f = r.choice([5, 6, 8, 10, 12]); g = r.choice([1, 2])
    t = GT(u0, h, [f] + [0] * (g - 1) + [f]) if g == 2 else GT(u0, h, [f, f])
    s = F(t.mid(t.k - 1) - t.mid(0), 2); assert t.var() == s * s
    fs = t.fs
    def tab(lang):
        x = gtab(sc, t, lang); return x
    qe = V(lv, ['The sample below has only two non-empty groups with equal frequencies. Its standard deviation is…', 'Find the standard deviation of the %s (in %s).', 'Without a long computation, \\(s\\) of the %s (in %s) is…'])
    qv = V(lv, ['Mẫu dưới đây chỉ có hai nhóm khác rỗng với tần số bằng nhau. Độ lệch chuẩn của mẫu là…', 'Tìm độ lệch chuẩn của %s (đơn vị %s).', 'Không cần tính dài, \\(s\\) của %s (đơn vị %s) là…'])
    en = qe if lv == 1 else qe % (VAR(sc, 'en'), U(sc, 'en')); vi = qv if lv == 1 else qv % (VAR(sc, 'vi'), U(sc, 'vi'))
    return dict(en='%s %s' % (I(sc, 'en'), en), vi='%s %s' % (I(sc, 'vi'), vi), opts=nopts(r, s, [2 * s, s * s, t.rng(), F(s, 2)], step=1), fig=TB(sc, t),
                ee='\\(\\bar x\\) is halfway between the two midpoints, every value is \\(%s\\) away from \\(\\bar x\\), so \\(s=%s\\).' % (ne(s), ne(s)),
                ev='\\(\\bar x\\) nằm chính giữa hai giá trị đại diện, mọi giá trị cách \\(\\bar x\\) đúng \\(%s\\) nên \\(s=%s\\).' % (nv(s), nv(s)))

def b10_tf_var(r, lv, ctx):
    sc = pick(ctx, r); t = vt(r, sc, cond=lambda t: math.isqrt(int(t.var())) ** 2 != t.var()); truth = r.random() < .5; v = t.var()
    if truth:
        e = 'The variance of the %s is \\(s^2=%s\\).' % (VAR(sc, 'en'), ne(v)); vv = 'Phương sai của %s là \\(s^2=%s\\).' % (VAR(sc, 'vi'), nv(v))
    else:
        e = 'The standard deviation of the %s is \\(s=%s\\).' % (VAR(sc, 'en'), ne(v)); vv = 'Độ lệch chuẩn của %s là \\(s=%s\\).' % (VAR(sc, 'vi'), nv(v))
    return dict(en='%s %s' % (I(sc, 'en'), e), vi='%s %s' % (I(sc, 'vi'), vv), truth=truth, fig=TB(sc, t),
                ee=vsteps(t, 'en') + ('' if truth else ' \\(%s\\) is \\(s^2\\), not \\(s\\).' % ne(v)), ev=vsteps(t, 'vi') + ('' if truth else ' \\(%s\\) là \\(s^2\\), không phải \\(s\\).' % nv(v)))

B10_CONCEPT = [(('If every value of a sample increases by 5, the standard deviation does not change.', 'Nếu cộng thêm 5 vào mọi giá trị của mẫu thì độ lệch chuẩn không đổi.'), True),
               (('If every value of a sample is doubled, the variance is doubled.', 'Nếu nhân đôi mọi giá trị của mẫu thì phương sai cũng tăng gấp đôi.'), False),
               (('The standard deviation has the same unit as the data.', 'Độ lệch chuẩn có cùng đơn vị với số liệu.'), True)]
def b10_tf_concept(r, lv, ctx):
    (e, v), truth = B10_CONCEPT[(lv - 1) % 3]
    return dict(en=e, vi=v, truth=truth, ee='Adding \\(c\\): \\(s\\) unchanged. Multiplying by \\(k\\gt0\\): \\(s\\) times \\(k\\), \\(s^2\\) times \\(k^2\\). \\(s\\) has the data unit.',
                ev='Cộng \\(c\\): \\(s\\) không đổi. Nhân \\(k\\gt0\\): \\(s\\) nhân \\(k\\), \\(s^2\\) nhân \\(k^2\\). \\(s\\) có cùng đơn vị với số liệu.')

B10_PCT = [(('salaries', 'tiền lương'), 10, 'variance', 'phương sai'), (('prices of products', 'giá sản phẩm'), 20, 'variance', 'phương sai'), (('rents', 'tiền thuê nhà'), 10, 'standard deviation', 'độ lệch chuẩn')]
def b10_tf_pct(r, lv, ctx):
    (we, wv), p, me, mv = B10_PCT[(lv - 1) % 3]; k = F(100 + p, 100)
    claim = r.choice([p, p * 2 + p * p // 100]); truth_val = (p * 2 + p * p // 100) if me == 'variance' else p; truth = claim == truth_val
    return dict(en='All %s in a company are increased by %d%%. Then the %s of the %s increases by %d%%.' % (we, p, me, we, claim),
                vi='Mọi %s trong một công ty đều tăng %d%%. Khi đó %s của %s tăng %d%%.' % (wv, p, mv, wv, claim), truth=truth,
                ee='Multiplying by \\(%s\\): \\(s\\) is multiplied by \\(%s\\) (+%d%%), \\(s^2\\) by \\(%s\\) (+%d%%).' % (ne(k), ne(k), p, ne(k * k), p * 2 + p * p // 100),
                ev='Nhân với \\(%s\\): \\(s\\) nhân \\(%s\\) (tăng %d%%), \\(s^2\\) nhân \\(%s\\) (tăng %d%%).' % (nv(k), nv(k), p, nv(k * k), p * 2 + p * p // 100))

def b10_sh_meansq(r, lv, ctx):
    m = r.choice(range(4, 31)); s = r.choice([1, 2, 3, 4, 5, 6]); good = m * m + s * s
    if len(str(good)) > 4: raise AssertionError
    qe = V(lv, ['A grouped sample has mean \\(\\bar x=%d\\) and standard deviation \\(s=%d\\). Find \\(\\dfrac1n\\sum n_ix_i^2\\).', 'Given \\(\\bar x=%d\\) and \\(s=%d\\), calculate the mean of the squares \\(\\dfrac1n\\sum n_ix_i^2\\).', 'For a sample, \\(\\bar x=%d\\), \\(s=%d\\). What is \\(\\dfrac1n\\sum n_ix_i^2\\)?'])
    qv = V(lv, ['Mẫu ghép nhóm có số trung bình \\(\\bar x=%d\\) và độ lệch chuẩn \\(s=%d\\). Tính \\(\\dfrac1n\\sum n_ix_i^2\\).', 'Biết \\(\\bar x=%d\\), \\(s=%d\\), tính trung bình bình phương \\(\\dfrac1n\\sum n_ix_i^2\\).', 'Một mẫu có \\(\\bar x=%d\\), \\(s=%d\\). Tìm \\(\\dfrac1n\\sum n_ix_i^2\\).'])
    return dict(en=qe % (m, s), vi=qv % (m, s), key=str(good), ee='\\(s^2=\\frac1n\\sum n_ix_i^2-\\bar x^2\\Rightarrow\\frac1n\\sum n_ix_i^2=%d+%d=%d\\).' % (s * s, m * m, good),
                ev='\\(s^2=\\frac1n\\sum n_ix_i^2-\\bar x^2\\Rightarrow\\frac1n\\sum n_ix_i^2=%d+%d=%d\\).' % (s * s, m * m, good))

def b10_sh_hist(r, lv, ctx):
    sc = pick(ctx, r, lambda s: s['k'] not in ('bulb', 'power')); t = vt(r, sc, cond=lambda t: math.isqrt(int(t.var())) ** 2 != t.var()); v = t.var(); s = math.sqrt(v)
    dig = 2 if s < 10 else 1; val = F(round(s * 10 ** dig)) / 10 ** dig
    if not shortok(val): raise AssertionError
    rule_e = 'round to the hundredths' if dig == 2 else 'round to the tenths'; rule_v = 'làm tròn đến hàng phần trăm' if dig == 2 else 'làm tròn đến hàng phần mười'
    qe = V(lv, ['The histogram shows the grouped data. Find the standard deviation of the %s (%s).', 'Based on the histogram, calculate \\(s\\) for the %s (%s).', 'Use the histogram to estimate the standard deviation of the %s (%s).'])
    qv = V(lv, ['Biểu đồ tần số biểu diễn mẫu số liệu ghép nhóm. Tìm độ lệch chuẩn của %s (%s).', 'Dựa vào biểu đồ tần số, tính \\(s\\) của %s (%s).', 'Dùng biểu đồ tần số, ước lượng độ lệch chuẩn của %s (%s).'])
    return dict(en='%s %s' % (I(sc, 'en'), qe % (VAR(sc, 'en'), rule_e)), vi='%s %s' % (I(sc, 'vi'), qv % (VAR(sc, 'vi'), rule_v)), key=key(val), fig=HIST(sc, t),
                ee=vsteps(t, 'en') + ' \\(s=\\sqrt{%s}\\approx%s\\).' % (ne(v), ne(val)), ev=vsteps(t, 'vi') + ' \\(s=\\sqrt{%s}\\approx%s\\).' % (nv(v), nv(val)),
                hint=('Enter a decimal number, e.g. 3.25.', 'Nhập số thập phân, ví dụ 3,25.'))

def b10_sh_temp(r, lv, ctx):
    k = (lv - 1) % 3
    if k == 0:
        s = F(r.choice([5, 10, 15, 20, 25]), 10); good = F(18, 10) * s
        return dict(en='Noon temperatures in a month have standard deviation \\(s=%s\\ ^\\circ\\text{C}\\). They are converted to Fahrenheit by \\(F=1.8C+32\\). Find the new standard deviation (in \\(^\\circ\\text{F}\\)).' % ne(s),
                    vi='Nhiệt độ buổi trưa trong một tháng có độ lệch chuẩn \\(s=%s\\ ^\\circ\\text{C}\\). Đổi sang độ F theo công thức \\(F=1{,}8C+32\\). Tính độ lệch chuẩn mới (đơn vị \\(^\\circ\\text{F}\\)).' % nv(s),
                    key=key(good), ee='\\(s_F=1.8\\cdot%s=%s\\) (adding 32 does not change \\(s\\)).' % (ne(s), ne(good)), ev='\\(s_F=1{,}8\\cdot%s=%s\\) (cộng 32 không làm đổi \\(s\\)).' % (nv(s), nv(good)),
                    hint=('Enter a decimal number, e.g. 3.25.', 'Nhập số thập phân, ví dụ 3,25.'))
    a, b, s = r.choice([2, 3, 4]), r.choice([5, 10, 20]), r.choice([2, 3, 4, 5, 6])
    if k == 1:
        return dict(en='A test has scores with standard deviation \\(s=%d\\). The teacher converts each score \\(x\\) to \\(%dx+%d\\). Find the new standard deviation.' % (s, a, b),
                    vi='Điểm một bài kiểm tra có độ lệch chuẩn \\(s=%d\\). Giáo viên đổi mỗi điểm \\(x\\) thành \\(%dx+%d\\). Tính độ lệch chuẩn mới.' % (s, a, b),
                    key=str(a * s), ee='\\(s\\) is multiplied by \\(%d\\); adding \\(%d\\) changes nothing: \\(%d\\).' % (a, b, a * s), ev='\\(s\\) nhân với \\(%d\\); cộng \\(%d\\) không làm đổi \\(s\\): \\(%d\\).' % (a, b, a * s))
    return dict(en='The masses of parcels have variance \\(s^2=%d\\) kg². Each parcel is put into a box of mass %d kg, and the total masses are multiplied by %d to get the shipping cost units. Find the new variance.' % (s * s, b // 5, a),
                vi='Khối lượng các bưu kiện có phương sai \\(s^2=%d\\) kg². Mỗi bưu kiện được cho vào hộp nặng %d kg, rồi khối lượng tổng được nhân %d để ra số đơn vị cước. Tính phương sai mới.' % (s * s, b // 5, a),
                key=str(a * a * s * s), ee='Adding a constant keeps \\(s^2\\); multiplying by \\(%d\\) multiplies \\(s^2\\) by \\(%d\\): \\(%d\\).' % (a, a * a, a * a * s * s),
                ev='Cộng hằng số không đổi \\(s^2\\); nhân với \\(%d\\) thì \\(s^2\\) nhân với \\(%d\\): \\(%d\\).' % (a, a * a, a * a * s * s))

# ---- phần D, Bài 10
def b10_d_error(r, lv, ctx):
    sc = pick(ctx, r); t = vt(r, sc); v = t.var(); m = t.mean(); ms = v + m * m; wrong = ms - m
    def txt(lang):
        N = ne if lang == 'en' else nv
        s1 = '\\(\\bar x=%s\\).' % N(m)
        s2 = '\\(\\dfrac1n\\sum n_ix_i^2=%s\\).' % N(ms)
        s3 = '\\(s^2=%s-%s=%s\\).' % (N(ms), N(m), N(wrong))
        return ('A student computed the variance. Step 1: %s Step 2: %s Step 3: %s Where is the mistake?' if lang == 'en' else 'Một bạn tính phương sai như sau. Bước 1: %s Bước 2: %s Bước 3: %s Bạn sai ở đâu?') % (s1, s2, s3)
    S = [('Step 3: one must subtract \\(\\bar x^2\\), not \\(\\bar x\\).', 'Bước 3: phải trừ \\(\\bar x^2\\) chứ không phải \\(\\bar x\\).'), ('Step 1: the mean is wrong.', 'Bước 1: số trung bình sai.'),
         ('Step 2: the group ends must be used instead of the midpoints.', 'Bước 2: phải dùng đầu mút nhóm thay cho giá trị đại diện.'), ('There is no mistake.', 'Không có chỗ sai.')]
    return dict(en='%s %s' % (I(sc, 'en'), txt('en')), vi='%s %s' % (I(sc, 'vi'), txt('vi')), opts=[tt(*x) for x in S], fig=TB(sc, t),
                ee=vsteps(t, 'en'), ev=vsteps(t, 'vi'))

def b10_d_dev(r, lv, ctx):
    n = r.choice([20, 25, 40, 50]); v = F(r.choice([16, 25, 36, 49, 64, 81, 9, 12, 18, 20]))
    S = n * v
    qe = V(lv, ['A grouped sample of size \\(n=%d\\) has \\(\\sum n_i(x_i-\\bar x)^2=%s\\). Its standard deviation is…', 'For \\(n=%d\\) values, the sum of squared deviations is \\(\\sum n_i(x_i-\\bar x)^2=%s\\). Find \\(s\\).', 'The squared deviations from the mean add up to \\(%s\\) for \\(n=%d\\) values. Then \\(s=\\)…'])
    qv = V(lv, ['Mẫu ghép nhóm cỡ \\(n=%d\\) có \\(\\sum n_i(x_i-\\bar x)^2=%s\\). Độ lệch chuẩn của mẫu là…', 'Với \\(n=%d\\) giá trị, tổng bình phương độ lệch là \\(\\sum n_i(x_i-\\bar x)^2=%s\\). Tìm \\(s\\).', 'Tổng bình phương các độ lệch so với số trung bình bằng \\(%s\\) với \\(n=%d\\) giá trị. Khi đó \\(s=\\)…'])
    args = (n, ne(S)) if lv != 3 else (ne(S), n); argv = (n, nv(S)) if lv != 3 else (nv(S), n)
    sq = lambda x: (str(math.isqrt(int(x))) if math.isqrt(int(x)) ** 2 == x else '\\sqrt{%s}' % ne(x))
    opts = [M(sq(v)), M(ne(v)), M(sq(S)), M(ne(F(S, n - 1)) if F(S, n - 1).denominator in (1, 2, 4, 5, 10) else sq(v + 1))]
    return dict(en=qe % args, vi=qv % argv, opts=opts, ee='\\(s^2=\\frac{%s}{%d}=%s\\), \\(s=%s\\).' % (ne(S), n, ne(v), sq(v)), ev='\\(s^2=\\frac{%s}{%d}=%s\\), \\(s=%s\\).' % (nv(S), n, nv(v), sq(v)))

def b10_d_hist2(r, lv, ctx):
    sc = pick(ctx, r)
    for _ in range(300):
        h = r.choice(sc['h']); u0 = r.choice(sc['u0']); k = 5; a = r.randint(2, 4); c = r.randint(8, 12)
        f1 = [a, a + 2, c, a + 2, a]; f2 = [c - 2, a, a + 1, a, c - 2]
        t1, t2 = GT(u0, h, f1), GT(u0, h, f2)
        if t1.mean() == t2.mean() and t1.var() != t2.var(): break
    swap = r.random() < .5
    if swap: t1, t2 = t2, t1
    big = 'A' if t1.var() > t2.var() else 'B'; small = 'B' if big == 'A' else 'A'
    e1 = [ne(t1.edge(i)) for i in range(t1.k + 1)]
    fa = (G.img(G.hist_svg(e1, t1.fs, lab(sc['gl'])[0], lab(sc['fl'])[0]), 'Histogram A', 330), G.img(G.hist_svg(e1, t1.fs, lab(sc['gl'])[1], lab(sc['fl'])[1]), 'Biểu đồ A', 330))
    fb = (G.img(G.hist_svg(e1, t2.fs, lab(sc['gl'])[0], lab(sc['fl'])[0]), 'Histogram B', 330), G.img(G.hist_svg(e1, t2.fs, lab(sc['gl'])[1], lab(sc['fl'])[1]), 'Biểu đồ B', 330))
    fig = ('<p><b>A</b></p>%s<p><b>B</b></p>%s' % (fa[0], fb[0]), '<p><b>A</b></p>%s<p><b>B</b></p>%s' % (fa[1], fb[1]))
    S = [('Sample %s has the larger standard deviation.' % big, 'Mẫu %s có độ lệch chuẩn lớn hơn.' % big), ('Sample %s has the larger standard deviation.' % small, 'Mẫu %s có độ lệch chuẩn lớn hơn.' % small),
         ('The two standard deviations are equal because the means are equal.', 'Hai độ lệch chuẩn bằng nhau vì hai số trung bình bằng nhau.'), ('It cannot be decided without the raw data.', 'Không thể kết luận nếu không có số liệu gốc.')]
    qe = V(lv, ['Two samples have the same mean. Without computing, which statement is correct?', 'Look at the two histograms (same groups, same mean). Which sample is more spread out?', 'Compare the spread of samples A and B shown in the histograms.'])
    qv = V(lv, ['Hai mẫu có cùng số trung bình. Không cần tính, khẳng định nào đúng?', 'Quan sát hai biểu đồ (cùng các nhóm, cùng số trung bình). Mẫu nào phân tán hơn?', 'So sánh độ phân tán của hai mẫu A và B trong biểu đồ.'])
    if t1.mean() != t2.mean(): raise AssertionError
    return dict(en='%s %s' % (I(sc, 'en'), qe), vi='%s %s' % (I(sc, 'vi'), qv), opts=[tt(*x) for x in S], fig=fig,
                ee='In %s most values are in the outer groups, far from \\(\\bar x=%s\\) (\\(s^2_A=%s\\), \\(s^2_B=%s\\)).' % (big, ne(t1.mean()), ne(t1.var()), ne(t2.var())),
                ev='Ở mẫu %s, phần lớn giá trị nằm ở các nhóm ngoài, xa \\(\\bar x=%s\\) (\\(s^2_A=%s\\), \\(s^2_B=%s\\)).' % (big, nv(t1.mean()), nv(t1.var()), nv(t2.var())))

def b10_d_plausible(r, lv, ctx):
    sc = pick(ctx, r); t = vt(r, sc); R = t.rng(); s = math.sqrt(t.var())
    good = F(round(s * 10)) / 10; bads = [F(R), F(R) * 2, -good]
    qe = V(lv, ['Four students report the standard deviation of the %s (in %s). Which value is plausible?', 'Which value could be the standard deviation of the %s (in %s)?', 'Only one of these values can be \\(s\\) for the %s (in %s). Which one?'])
    qv = V(lv, ['Bốn bạn báo cáo độ lệch chuẩn của %s (đơn vị %s). Giá trị nào hợp lí?', 'Giá trị nào có thể là độ lệch chuẩn của %s (đơn vị %s)?', 'Chỉ một trong các giá trị sau có thể là \\(s\\) của %s (đơn vị %s). Đó là giá trị nào?'])
    return dict(en='%s %s' % (I(sc, 'en'), qe % (VAR(sc, 'en'), U(sc, 'en'))), vi='%s %s' % (I(sc, 'vi'), qv % (VAR(sc, 'vi'), U(sc, 'vi'))), opts=[nopt(good)] + [nopt(b) for b in bads], fig=TB(sc, t),
                ee='\\(s\\ge0\\) and \\(s\\) cannot exceed half the range \\(\\frac R2=%s\\); indeed \\(s\\approx%s\\).' % (ne(F(R, 2)), ne(good)),
                ev='\\(s\\ge0\\) và \\(s\\) không vượt quá nửa khoảng biến thiên \\(\\frac R2=%s\\); thật vậy \\(s\\approx%s\\).' % (nv(F(R, 2)), nv(good)))

def b10_d_param(r, lv, ctx):
    sc = pick(ctx, r)
    for _ in range(3000):
        t = vt(r, sc, cond=lambda t: t.k == 4); u = r.randrange(t.k)
        m = t.mean(); sols = [x for x in range(1, 41) if GT(t.u0, t.h, t.fs[:u] + [x] + t.fs[u + 1:]).mean() == m]
        if sols == [t.fs[u]] and (2 * m).denominator == 1: break
    else: raise AssertionError
    v = t.var()
    qe = V(lv, ['The mean of the %s is \\(\\bar x=%s\\). The variance of the sample is…', 'Knowing that \\(\\bar x=%s\\), find the variance of the sample.', 'The sample mean equals \\(%s\\). Then \\(s^2=\\)…'])
    qv = V(lv, ['Số trung bình của %s là \\(\\bar x=%s\\). Phương sai của mẫu là…', 'Biết \\(\\bar x=%s\\), tìm phương sai của mẫu.', 'Số trung bình của mẫu bằng \\(%s\\). Khi đó \\(s^2=\\)…'])
    en = qe % ((VAR(sc, 'en'), ne(m)) if lv == 1 else ne(m)); vi = qv % ((VAR(sc, 'vi'), nv(m)) if lv == 1 else nv(m))
    tb = (gtab(sc, t, 'en', unknown=u), gtab(sc, t, 'vi', unknown=u))
    tb = tuple(x.replace('\\(n=%d\\)' % t.n, '\\(n=%d+x\\)' % (t.n - t.fs[u])) for x in tb)
    return dict(en='%s %s' % (I(sc, 'en'), en), vi='%s %s' % (I(sc, 'vi'), vi), opts=nopts(r, v, [v + m * m, v * 2, v + t.h, F(t.var() * t.n, t.n - 1)], step=1), fig=tb,
                ee='From \\(\\bar x=%s\\): \\(x=%d\\), \\(n=%d\\). ' % (ne(m), t.fs[u], t.n) + vsteps(t, 'en'), ev='Từ \\(\\bar x=%s\\) tìm được \\(x=%d\\), \\(n=%d\\). ' % (nv(m), t.fs[u], t.n) + vsteps(t, 'vi'))

B10_STAT = [(('A sample has \\(s=0\\) exactly when all its values are equal.', 'Mẫu có \\(s=0\\) khi và chỉ khi mọi giá trị bằng nhau.'), ('The variance can be negative.', 'Phương sai có thể âm.'), ('\\(s\\) is always smaller than the mean.', '\\(s\\) luôn nhỏ hơn số trung bình.'), ('Adding a constant to every value changes \\(s\\).', 'Cộng một hằng số vào mọi giá trị thì \\(s\\) thay đổi.')),
            (('The larger \\(s\\) is, the more the data are spread around the mean.', '\\(s\\) càng lớn thì số liệu càng phân tán quanh số trung bình.'), ('\\(s\\) is measured in the squared unit of the data.', '\\(s\\) có đơn vị là bình phương đơn vị của số liệu.'), ('A larger mean always gives a larger \\(s\\).', 'Số trung bình càng lớn thì \\(s\\) càng lớn.'), ('\\(s^2\\le s\\) for every sample.', 'Với mọi mẫu, \\(s^2\\le s\\).')),
            (('The standard deviation is the square root of the variance.', 'Độ lệch chuẩn là căn bậc hai của phương sai.'), ('The variance is the square root of the standard deviation.', 'Phương sai là căn bậc hai của độ lệch chuẩn.'), ('\\(s\\) is the mean of the deviations \\(x_i-\\bar x\\).', '\\(s\\) là trung bình của các độ lệch \\(x_i-\\bar x\\).'), ('Doubling every value doubles the variance.', 'Nhân đôi mọi giá trị thì phương sai tăng gấp đôi.'))]
def b10_d_stat(r, lv, ctx):
    S = B10_STAT[(lv - 1) % 3]
    qe = V(lv, ['Which statement about the variance and the standard deviation is correct?', 'Choose the true statement about the standard deviation \\(s\\).', 'Which of the following is true?'])
    qv = V(lv, ['Khẳng định nào về phương sai và độ lệch chuẩn là đúng?', 'Chọn khẳng định đúng về độ lệch chuẩn \\(s\\).', 'Khẳng định nào sau đây đúng?'])
    return dict(en=qe, vi=qv, opts=[tt(*x) for x in S],
                ee='%s' % S[0][0], ev='%s' % S[0][1])

def b10_d_addmean(r, lv, ctx):
    n = r.choice([9, 15, 19, 24, 39, 49]); v = F(r.choice([10, 20, 25, 40, 50, 100]))
    good = v * n / (n + 1)
    if good.denominator not in (1, 2, 4, 5, 10, 20, 25, 50): raise AssertionError
    E = [('teachers', 'giáo viên'), ('runners', 'vận động viên'), ('apples', 'quả táo')][(lv - 1) % 3]
    return dict(en='A sample of %d %s has mean \\(\\bar x\\) and variance \\(s^2=%s\\). One more value equal to \\(\\bar x\\) is added. The new variance is…' % (n, E[0], ne(v)),
                vi='Một mẫu gồm %d %s có số trung bình \\(\\bar x\\) và phương sai \\(s^2=%s\\). Thêm một giá trị đúng bằng \\(\\bar x\\). Phương sai mới là…' % (n, E[1], nv(v)),
                opts=nopts(r, good, [v, v * (n + 1) / n, v / 2, v * (n - 1) / n], step=1),
                ee='The mean stays \\(\\bar x\\); the sum of squared deviations stays \\(%d\\cdot%s\\) but is divided by \\(%d\\): \\(%s\\).' % (n, ne(v), n + 1, ne(good)),
                ev='Số trung bình vẫn là \\(\\bar x\\); tổng bình phương độ lệch vẫn là \\(%d\\cdot%s\\) nhưng chia cho \\(%d\\): \\(%s\\).' % (n, nv(v), n + 1, nv(good)))

def b10_d_within(r, lv, ctx):
    sc = pick(ctx, r)
    for _ in range(20000):
        h = r.choice(sc['h']); u0 = r.choice(sc['u0']); k = 5; fs = [r.randint(1, 12) for _ in range(k)]
        t = GT(u0, h, fs); m = t.mean(); v = t.var()
        if m == t.edge(2) + F(h, 2) and v == h * h and t.n >= 16: break
    else: raise AssertionError
    good = t.fs[1] + t.fs[2] + t.fs[3]   # [x̄-s; x̄+s] = [mid1; mid3] → ước lượng: nhóm 2,3,4
    s = h
    qe = V(lv, ['For this sample \\(\\bar x=%s\\) and \\(s=%s\\). About how many %s have a value within one standard deviation of the mean, i.e. in \\([\\bar x-s;\\,\\bar x+s]\\)?', 'With \\(\\bar x=%s\\) and \\(s=%s\\), estimate how many %s lie between \\(\\bar x-s\\) and \\(\\bar x+s\\) (count whole groups whose midpoints are in this interval).', 'Here \\(\\bar x=%s\\), \\(s=%s\\). Roughly how many %s are within \\(s\\) of the mean (use the groups whose midpoints lie in \\([\\bar x-s;\\,\\bar x+s]\\))?'])
    qv = V(lv, ['Mẫu này có \\(\\bar x=%s\\), \\(s=%s\\). Có khoảng bao nhiêu %s có giá trị cách số trung bình không quá một độ lệch chuẩn, tức thuộc \\([\\bar x-s;\\,\\bar x+s]\\)?', 'Với \\(\\bar x=%s\\), \\(s=%s\\), ước lượng số %s nằm giữa \\(\\bar x-s\\) và \\(\\bar x+s\\) (đếm các nhóm có giá trị đại diện thuộc đoạn này).', 'Ở đây \\(\\bar x=%s\\), \\(s=%s\\). Có khoảng bao nhiêu %s cách số trung bình không quá \\(s\\) (dùng các nhóm có giá trị đại diện thuộc \\([\\bar x-s;\\,\\bar x+s]\\))?'])
    return dict(en='%s %s' % (I(sc, 'en'), qe % (ne(m), ne(s), ENT(sc, 'en'))), vi='%s %s' % (I(sc, 'vi'), qv % (nv(m), nv(s), ENT(sc, 'vi'))), opts=nopts(r, good, [t.fs[2], t.n, t.fs[1] + t.fs[2], t.n - t.fs[2]]), fig=TB(sc, t),
                ee='\\([\\bar x-s;\\,\\bar x+s]=[%s;\\,%s]\\) contains the midpoints of the 2nd, 3rd and 4th groups: \\(%d+%d+%d=%d\\).' % (ne(m - s), ne(m + s), t.fs[1], t.fs[2], t.fs[3], good),
                ev='\\([\\bar x-s;\\,\\bar x+s]=[%s;\\,%s]\\) chứa giá trị đại diện của nhóm 2, 3, 4: \\(%d+%d+%d=%d\\).' % (nv(m - s), nv(m + s), t.fs[1], t.fs[2], t.fs[3], good))

B10 = dict(A=[b10_var, b10_sums, b10_unit, b10_compare, b10_formula, b10_two], B=[b10_tf_var, b10_tf_concept, b10_tf_pct], C=[b10_sh_meansq, b10_sh_hist, b10_sh_temp],
           D=[b10_d_error, b10_d_dev, b10_d_hist2, b10_d_plausible, b10_d_param, b10_d_stat, b10_d_addmean, b10_d_within])

# ================================================================ BÀI 17 – Phương trình mặt cầu
from sp_g12f import sph, gen
from sp_g12d import eq, V3 as V3d
def dot3(a, b): return sum(x * y for x, y in zip(a, b))
def sub3(a, b): return tuple(x - y for x, y in zip(a, b))
def P3(p): return V3d(p)
def SPH(I, R2): return M(sph(I, R2))
def isq(n): return n >= 0 and math.isqrt(n) ** 2 == n

def fig_oxyz(I, R, pts=None, segs=(), alt='Sphere in the coordinate system Oxyz', lp=None, hc=True, px=300):
    P = {'O': (0, 0, 0), 'I': I}; P.update(pts or {})
    L = max(max(abs(c) for c in I) + R, 3) + 1.5
    cfg = {'points': P, 'proj': 'oxyz', 'axes': True, 'axislen': L, 'spheres': [{'c': 'I', 'R': R, 'fill': '#86e0bd'}],
           'segments': [list(s) for s in segs], 'labelpos': dict({'O': 'below left'}, **(lp or {})), 'px': px}
    if hc: cfg['hcircles'] = [{'c': 'I', 'R': R, 'color': '#64748b'}]
    return Q3D(cfg, alt, px=px)

HL = {'color': '#c2410c', 'width': 3, 'dash': True, 'force': True}
SOL = {'color': '#c2410c', 'width': 3}

def s17_tan_oxy(r, lv, ctx):
    I = (r.randint(1, 4), r.randint(1, 4), r.randint(2, 4)); a, b, c = I; R2 = c * c
    O_ = [SPH(I, R2), SPH(I, c), SPH(I, a * a + b * b + c * c), SPH(I, a * a)]
    if len(set(O_)) < 4: raise AssertionError
    qe = V(lv, ['The sphere \\((S)\\) has center \\(I%s\\) and is tangent to the plane \\((Oxy)\\) (see the figure). The equation of \\((S)\\) is…', 'A ball with center \\(I%s\\) rests on the floor \\((Oxy)\\) (see the figure). Its surface has the equation…', 'The sphere with center \\(I%s\\) touching the plane \\((Oxy)\\) at \\(H\\) (figure) is…'])
    qv = V(lv, ['Mặt cầu \\((S)\\) có tâm \\(I%s\\) và tiếp xúc với mặt phẳng \\((Oxy)\\) (xem hình). Phương trình của \\((S)\\) là…', 'Một quả bóng tâm \\(I%s\\) đặt trên sàn nhà \\((Oxy)\\) (xem hình). Mặt quả bóng có phương trình…', 'Mặt cầu tâm \\(I%s\\) tiếp xúc với mặt phẳng \\((Oxy)\\) tại \\(H\\) (hình vẽ) là…'])
    return dict(en=qe % P3(I), vi=qv % P3(I), opts=O_, fig=fig_oxyz(I, c, {'H': (a, b, 0)}, [('I', 'H', HL)], lp={'H': 'below'}),
                ee='\\(R=d(I,(Oxy))=|z_I|=%d\\), so \\(R^2=%d\\).' % (c, R2), ev='\\(R=d(I,(Oxy))=|z_I|=%d\\) nên \\(R^2=%d\\).' % (c, R2))

def s17_diam(r, lv, ctx):
    I = (r.randint(-3, 3), r.randint(-3, 3), r.randint(-3, 3)); u = (r.randint(-3, 3), r.randint(-3, 3), r.randint(-3, 3))
    if dot3(u, u) == 0: raise AssertionError
    A = tuple(i + x for i, x in zip(I, u)); B = tuple(i - x for i, x in zip(I, u)); R2 = dot3(u, u)
    O_ = [SPH(I, R2), SPH(I, 4 * R2), SPH(A, R2), SPH(tuple(-x for x in I), R2)]
    if len(set(O_)) < 4: raise AssertionError
    cfg = {'points': {'I': (0, 0, 0), 'A': (-2.0, -0.8, 1.1), 'B': (2.0, 0.8, -1.1)}, 'spheres': [{'c': 'I', 'R': 2.42, 'fill': '#86e0bd'}],
           'hcircles': [{'c': 'I', 'R': 2.42, 'color': '#64748b'}], 'segments': [['A', 'B', {'color': '#c2410c', 'width': 3}]], 'px': 260}
    qe = V(lv, ['The sphere with diameter \\(AB\\), where \\(A%s\\), \\(B%s\\), is…', 'Find the equation of the sphere that has \\(AB\\) as a diameter, \\(A%s\\), \\(B%s\\).', 'Given \\(A%s\\) and \\(B%s\\), the sphere with diameter \\(AB\\) (figure) has the equation…'])
    qv = V(lv, ['Mặt cầu đường kính \\(AB\\) với \\(A%s\\), \\(B%s\\) là…', 'Tìm phương trình mặt cầu nhận \\(AB\\) làm đường kính, \\(A%s\\), \\(B%s\\).', 'Cho \\(A%s\\), \\(B%s\\). Mặt cầu đường kính \\(AB\\) (hình vẽ) có phương trình…'])
    return dict(en=qe % (P3(A), P3(B)), vi=qv % (P3(A), P3(B)), opts=O_, fig=Q3D(cfg, 'Sphere with diameter AB', px=260),
                ee='Center = midpoint \\(I%s\\) of \\(AB\\); \\(R^2=\\left(\\frac{AB}{2}\\right)^2=%d\\).' % (P3(I), R2), ev='Tâm là trung điểm \\(I%s\\) của \\(AB\\); \\(R^2=\\left(\\frac{AB}{2}\\right)^2=%d\\).' % (P3(I), R2))

def s17_reflect(r, lv, ctx):
    I = (r.randint(-3, 3), r.randint(-3, 3), r.randint(-3, 3)); R = r.randint(1, 5)
    if 0 in I: raise AssertionError
    k = (lv - 1) % 3
    J, nm, ne_, nv_ = [((I[0], I[1], -I[2]), '(Oxy)', 'the plane \\((Oxy)\\)', 'mặt phẳng \\((Oxy)\\)'), ((-I[0], I[1], I[2]), '(Oyz)', 'the plane \\((Oyz)\\)', 'mặt phẳng \\((Oyz)\\)'), ((-I[0], -I[1], -I[2]), 'O', 'the origin \\(O\\)', 'gốc tọa độ \\(O\\)')][k]
    O_ = [SPH(J, R * R), SPH(I, R * R), SPH((J[0], J[1], -J[2]) if k == 2 else tuple(-x for x in J), R * R), SPH(J, 4 * R * R)]
    if len(set(O_)) < 4: raise AssertionError
    qe = V(lv, ['The sphere \\((S\')\\) is symmetric to \\((S): %s\\) with respect to %s. Its equation is…', 'Find the image of the sphere \\(%s\\) under the reflection in %s.', 'The sphere \\((S): %s\\) is reflected through %s. The new sphere is…'])
    qv = V(lv, ['Mặt cầu \\((S\')\\) đối xứng với \\((S): %s\\) qua %s. Phương trình của \\((S\')\\) là…', 'Tìm ảnh của mặt cầu \\(%s\\) qua phép đối xứng qua %s.', 'Lấy đối xứng mặt cầu \\((S): %s\\) qua %s. Mặt cầu nhận được là…'])
    return dict(en=qe % (sph(I, R * R), ne_), vi=qv % (sph(I, R * R), nv_), opts=O_,
                ee='The center \\(I%s\\) goes to \\(I\'%s\\); the radius stays \\(%d\\).' % (P3(I), P3(J), R), ev='Tâm \\(I%s\\) biến thành \\(I\'%s\\); bán kính giữ nguyên bằng \\(%d\\).' % (P3(I), P3(J), R))

def s17_tf_tanxz(r, lv, ctx):
    a, b, c = r.randint(1, 4), r.randint(2, 4), r.randint(2, 4); truth = r.random() < .5; R = b if truth else r.choice([x for x in (2, 3, 4, 5) if x != b])
    I = (a, b, c); K = (a, 0, c)
    qe = V(lv, ['The sphere \\(%s\\) (figure) is tangent to the plane \\((Oxz)\\).', 'The plane \\((Oxz)\\) touches the sphere \\(%s\\) shown in the figure.', 'The sphere \\((S): %s\\) and the plane \\((Oxz)\\) have exactly one common point.'])
    qv = V(lv, ['Mặt cầu \\(%s\\) (hình vẽ) tiếp xúc với mặt phẳng \\((Oxz)\\).', 'Mặt phẳng \\((Oxz)\\) tiếp xúc với mặt cầu \\(%s\\) trong hình.', 'Mặt cầu \\((S): %s\\) và mặt phẳng \\((Oxz)\\) có đúng một điểm chung.'])
    return dict(en=qe % sph(I, R * R), vi=qv % sph(I, R * R), truth=truth, fig=fig_oxyz(I, R, {'K': K}, [('I', 'K', HL)], lp={'K': 'left'}),
                ee='\\(d(I,(Oxz))=|y_I|=%d\\), \\(R=%d\\): %s.' % (b, R, 'tangent' if truth else 'not tangent'), ev='\\(d(I,(Oxz))=|y_I|=%d\\), \\(R=%d\\): %s.' % (b, R, 'tiếp xúc' if truth else 'không tiếp xúc'))

def s17_sh_m(r, lv, ctx):
    I = (r.randint(-3, 3), r.randint(-3, 3), r.randint(-3, 3)); R = r.randint(1, 5); m = dot3(I, I) - R * R
    s = 'x^2+y^2+z^2'
    for v, ch in zip(I, 'xyz'):
        if v: s += '%+d%s' % (-2 * v, ch)
    s += '+m=0'
    qe = V(lv, ['Find \\(m\\) so that \\(%s\\) is a sphere of radius %d.', 'The equation \\(%s\\) describes a sphere with radius \\(R=%d\\). Find \\(m\\).', 'For which value of \\(m\\) does \\(%s\\) have radius %d?'])
    qv = V(lv, ['Tìm \\(m\\) để \\(%s\\) là phương trình mặt cầu bán kính %d.', 'Phương trình \\(%s\\) là mặt cầu có bán kính \\(R=%d\\). Tìm \\(m\\).', 'Với giá trị nào của \\(m\\) thì \\(%s\\) có bán kính bằng %d?'])
    return dict(en=qe % (s, R), vi=qv % (s, R), key=str(m), ee='\\(R^2=a^2+b^2+c^2-m\\Rightarrow %d=%d-m\\Rightarrow m=%d\\).' % (R * R, dot3(I, I), m), ev='\\(R^2=a^2+b^2+c^2-m\\Rightarrow %d=%d-m\\Rightarrow m=%d\\).' % (R * R, dot3(I, I), m))

def s17_d_box(r, lv, ctx):
    a, b, c = r.choice([(4, 4, 2), (4, 6, 4), (6, 4, 4), (2, 4, 4), (4, 2, 4), (4, 4, 4), (6, 6, 4)])
    if r.random() < .5: a, b = b, a
    I = (a // 2, b // 2, c // 2); R2 = (a * a + b * b + c * c) // 4
    if (a * a + b * b + c * c) % 4: raise AssertionError
    O_ = [SPH(I, R2), SPH(I, 4 * R2), SPH((a, b, c), R2), SPH(I, R2 - I[2] ** 2)]
    if len(set(O_)) < 4: raise AssertionError
    P = {'O': (0, 0, 0), 'A': (a, 0, 0), 'B': (a, b, 0), 'C': (0, b, 0), "O'": (0, 0, c), "A'": (a, 0, c), "B'": (a, b, c), "C'": (0, b, c), 'I': I}
    cfg = {'points': P, 'solid': ['O', 'A', 'B', 'C', "O'", "A'", "B'", "C'"], 'proj': 'oxyz', 'axes': True, 'axislen': max(a, b, c) + 1.5,
           'segments': [['O', "B'", {'color': '#c2410c', 'width': 3, 'dash': True, 'force': True}]], 'labelpos': {'O': 'below left'}, 'px': 320}
    qe = V(lv, ["The box \\(OABC.O'A'B'C'\\) has \\(A(%d;0;0)\\), \\(C(0;%d;0)\\), \\(O'(0;0;%d)\\) (figure). The sphere through all eight vertices is…", "Find the sphere circumscribed about the box \\(OABC.O'A'B'C'\\) with \\(A(%d;0;0)\\), \\(C(0;%d;0)\\), \\(O'(0;0;%d)\\).", "A box-shaped room \\(OABC.O'A'B'C'\\) has \\(A(%d;0;0)\\), \\(C(0;%d;0)\\), \\(O'(0;0;%d)\\) (in m). The sphere passing through its eight corners is…"])
    qv = V(lv, ["Hình hộp chữ nhật \\(OABC.O'A'B'C'\\) có \\(A(%d;0;0)\\), \\(C(0;%d;0)\\), \\(O'(0;0;%d)\\) (hình vẽ). Mặt cầu đi qua cả tám đỉnh là…", "Tìm mặt cầu ngoại tiếp hình hộp chữ nhật \\(OABC.O'A'B'C'\\) với \\(A(%d;0;0)\\), \\(C(0;%d;0)\\), \\(O'(0;0;%d)\\).", "Một căn phòng dạng hình hộp chữ nhật \\(OABC.O'A'B'C'\\) có \\(A(%d;0;0)\\), \\(C(0;%d;0)\\), \\(O'(0;0;%d)\\) (đơn vị m). Mặt cầu đi qua tám góc phòng là…"])
    return dict(en=qe % (a, b, c), vi=qv % (a, b, c), opts=O_, fig=Q3D(cfg, 'Box in the coordinate system with the diagonal OB′', px=320),
                ee="The center is the midpoint \\(I%s\\) of the diagonal \\(OB'\\); \\(R^2=\\frac{OB'^2}{4}=\\frac{%d}{4}=%d\\)." % (P3(I), 4 * R2, R2),
                ev="Tâm là trung điểm \\(I%s\\) của đường chéo \\(OB'\\); \\(R^2=\\frac{OB'^2}{4}=\\frac{%d}{4}=%d\\)." % (P3(I), 4 * R2, R2))

def s17_d_three(r, lv, ctx):
    R = r.randint(1, 4); I = (R, R, R)
    O_ = [SPH(I, R * R), SPH(I, R), SPH((0, 0, R), R * R), SPH(I, 3 * R * R)]
    if len(set(O_)) < 4: raise AssertionError
    qe = V(lv, ['A sphere of radius %d lies in the region \\(x,y,z\\ge0\\) and is tangent to the three coordinate planes (figure). Its equation is…', 'A ball of radius %d sits in the corner of a room: it touches the floor \\((Oxy)\\) and the two walls \\((Oxz)\\), \\((Oyz)\\) (figure). The equation of its surface is…', 'The sphere with radius %d touching \\((Oxy)\\), \\((Oyz)\\), \\((Ozx)\\) and having center with positive coordinates (figure) is…'])
    qv = V(lv, ['Mặt cầu bán kính %d nằm trong miền \\(x,y,z\\ge0\\) và tiếp xúc với ba mặt phẳng tọa độ (hình vẽ). Phương trình của mặt cầu là…', 'Một quả bóng bán kính %d nằm ở góc phòng: tiếp xúc với sàn \\((Oxy)\\) và hai bức tường \\((Oxz)\\), \\((Oyz)\\) (hình vẽ). Phương trình mặt quả bóng là…', 'Mặt cầu bán kính %d tiếp xúc với \\((Oxy)\\), \\((Oyz)\\), \\((Ozx)\\) và có tâm với các tọa độ dương (hình vẽ) là…'])
    return dict(en=qe % R, vi=qv % R, opts=O_, fig=fig_oxyz((R, R, R), R, {'H': (R, R, 0)}, [('I', 'H', HL)], lp={'H': 'below'}),
                ee='The distance from \\(I\\) to each coordinate plane is \\(R=%d\\), so \\(I%s\\).' % (R, P3(I)), ev='Khoảng cách từ \\(I\\) đến mỗi mặt phẳng tọa độ đều bằng \\(R=%d\\) nên \\(I%s\\).' % (R, P3(I)))

TRIP = [(1, 2, 2, 3), (2, 3, 6, 7), (1, 4, 8, 9), (2, 6, 9, 11), (4, 4, 7, 9), (3, 4, 12, 13), (2, 10, 11, 15), (6, 6, 7, 11)]
def trip(r):
    a, b, c, d = r.choice(TRIP); v = [a, b, c]; r.shuffle(v); v = [x * r.choice([1, -1]) for x in v]; return tuple(v), d

def s17_d_maxdist(r, lv, ctx):
    I = (r.randint(-2, 2), r.randint(-2, 2), r.randint(-2, 2)); u, d = trip(r); A = tuple(i + x for i, x in zip(I, u)); R = r.randint(1, d - 1)
    big = lv != 2; good = d + R if big else d - R
    cfg = {'points': {'I': (0, 0, 0), 'A': (4.2, 0, 0.6), '_m': (-1.96, 0, -0.28)}, 'spheres': [{'c': 'I', 'R': 2.0, 'fill': '#86e0bd'}],
           'hcircles': [{'c': 'I', 'R': 2.0, 'color': '#64748b'}], 'segments': [['_m', 'A', {'color': '#c2410c', 'width': 3}]], 'px': 300}
    qe = V(lv, ['\\(M\\) moves on the sphere \\(%s\\) and \\(A%s\\) (figure). The largest possible length \\(AM\\) is…', '\\(M\\) is a point of \\((S): %s\\); \\(A%s\\). The shortest distance \\(AM\\) is…', 'A drone at \\(A%s\\) observes a ball \\((S): %s\\). The farthest point of the ball is at distance…'])
    qv = V(lv, ['\\(M\\) thay đổi trên mặt cầu \\(%s\\) và \\(A%s\\) (hình vẽ). Độ dài lớn nhất của \\(AM\\) là…', '\\(M\\) là điểm thuộc \\((S): %s\\); \\(A%s\\). Khoảng cách \\(AM\\) nhỏ nhất là…', 'Một thiết bị bay ở \\(A%s\\) quan sát quả cầu \\((S): %s\\). Điểm xa nhất của quả cầu cách thiết bị…'])
    if lv == 3: en = qe % (P3(A), sph(I, R * R)); vi = qv % (P3(A), sph(I, R * R))
    else: en = qe % (sph(I, R * R), P3(A)); vi = qv % (sph(I, R * R), P3(A))
    return dict(en=en, vi=vi, opts=nopts(r, good, [d - R if big else d + R, d, R, d * d - R * R]), fig=Q3D(cfg, 'Sphere and an outside point A on the line through the center', px=300),
                ee='\\(IA=%d\\gt R=%d\\); %s.' % (d, R, ('max \\(AM=IA+R=%d\\)' if big else 'min \\(AM=IA-R=%d\\)') % good),
                ev='\\(IA=%d\\gt R=%d\\); %s.' % (d, R, ('\\(AM\\) lớn nhất \\(=IA+R=%d\\)' if big else '\\(AM\\) nhỏ nhất \\(=IA-R=%d\\)') % good))

def s17_d_error(r, lv, ctx):
    I = (r.randint(1, 3) * r.choice([1, -1]), r.randint(1, 3) * r.choice([1, -1]), r.randint(1, 3) * r.choice([1, -1])); R = r.randint(2, 5); d = dot3(I, I) - R * R
    nI = tuple(-x for x in I)
    def T(lang):
        s1 = '\\(%s\\Leftrightarrow %s\\).' % (gen(I, d), sph(nI, R * R))
        return ('A student solved: Step 1: %s Step 2: center \\(I%s\\), radius \\(R=%d\\). Which comment is correct?' if lang == 'en' else
                'Một bạn giải: Bước 1: %s Bước 2: tâm \\(I%s\\), bán kính \\(R=%d\\). Nhận xét nào đúng?') % (s1, P3(nI), R)
    S = [('Step 1 is wrong: the center is \\(I%s\\); the radius %d is right.' % (P3(I), R), 'Bước 1 sai: tâm là \\(I%s\\); bán kính %d đúng.' % (P3(I), R)),
         ('Only the radius is wrong.', 'Chỉ bán kính sai.'), ('Both steps are correct.', 'Cả hai bước đều đúng.'), ('The equation is not a sphere.', 'Phương trình không phải mặt cầu.')]
    return dict(en=T('en'), vi=T('vi'), opts=[tt(*x) for x in S], ee='\\(-2ax\\) with \\(-2a=%d\\) gives \\(a=%d\\): \\(%s\\).' % (-2 * I[0], I[0], sph(I, R * R)),
                ev='\\(-2ax\\) với \\(-2a=%d\\) cho \\(a=%d\\): \\(%s\\).' % (-2 * I[0], I[0], sph(I, R * R)))

def s17_d_chord(r, lv, ctx):
    for _ in range(400):
        a, b, c = r.randint(3, 7), r.randint(0, 3), r.randint(1, 3); k = r.randint(1, 4); R2 = b * b + c * c + k * k
        if isq(R2) and a - k >= 2: break
    else: raise AssertionError
    R = math.isqrt(R2); I = (a, b, c); good = 2 * k
    qe = V(lv, ['The sphere \\(%s\\) cuts the axis \\(Ox\\) at \\(M\\) and \\(N\\); \\(K\\) is the foot of the perpendicular from the center \\(I\\) to \\(Ox\\) (figure). Then \\(MN=\\)…', 'Find the length of the chord cut on the \\(x\\)-axis by \\((S): %s\\).', 'The axis \\(Ox\\) meets the sphere \\(%s\\) at two points. Their distance is…'])
    qv = V(lv, ['Mặt cầu \\(%s\\) cắt trục \\(Ox\\) tại \\(M\\), \\(N\\); \\(K\\) là hình chiếu của tâm \\(I\\) trên \\(Ox\\) (hình vẽ). Khi đó \\(MN=\\)…', 'Tìm độ dài dây cung mà trục \\(Ox\\) cắt trên \\((S): %s\\).', 'Trục \\(Ox\\) cắt mặt cầu \\(%s\\) tại hai điểm. Khoảng cách giữa hai điểm đó là…'])
    return dict(en=qe % sph(I, R2), vi=qv % sph(I, R2), opts=nopts(r, good, [k, 2 * R, R + k, 2 * R - 2 * k]),
                fig=Q3D({'points': {'I': (0, 0, 0), 'K': (0, 0, -1.2), 'M': (-1.6, 0, -1.2), 'N': (1.6, 0, -1.2)}, 'spheres': [{'c': 'I', 'R': 2.0, 'fill': '#86e0bd'}],
                         'segments': [['M', 'N', SOL], ['I', 'K', HL], ['I', 'N', {'color': '#0f766e', 'width': 2.5, 'dash': True, 'force': True}]], 'right': [['I', 'K', 'N']], 'rsize': 0.28,
                         'labelpos': {'K': 'below', 'M': 'left', 'N': 'right', 'I': 'above'}, 'px': 260}, 'Chord MN of the sphere on the axis Ox; IK is perpendicular to MN', px=260),
                ee='\\(d(I,Ox)=\\sqrt{%d^2+%d^2}\\), \\(MN=2\\sqrt{R^2-d^2}=2\\sqrt{%d-%d}=%d\\).' % (b, c, R2, b * b + c * c, good),
                ev='\\(d(I,Ox)=\\sqrt{%d^2+%d^2}\\), \\(MN=2\\sqrt{R^2-d^2}=2\\sqrt{%d-%d}=%d\\).' % (b, c, R2, b * b + c * c, good))

def s17_d_touch(r, lv, ctx):
    I1 = (r.randint(-2, 2), r.randint(-2, 2), r.randint(-2, 2)); u, d = trip(r); I2 = tuple(i + x for i, x in zip(I1, u)); R1 = r.randint(1, d - 1); R2 = d - R1
    cfg = {'points': {'I': (0, 0, 0), 'J': (3.2, 0, 0), 'T': (1.4, 0, 0)}, 'spheres': [{'c': 'I', 'R': 1.4, 'fill': '#86e0bd'}, {'c': 'J', 'R': 1.8, 'fill': '#93c5fd'}],
           'segments': [['I', 'J', {'color': '#c2410c', 'width': 3}]], 'labelpos': {'T': 'above'}, 'px': 320}
    qe = V(lv, ['Two balls touch each other from outside (figure). The first is \\(%s\\); the second has center \\(J%s\\). Its radius is…', 'The sphere with center \\(J%s\\) is tangent externally to \\((S): %s\\). Its radius is…', 'Two spheres touch at one point \\(T\\) (figure): \\((S_1): %s\\) and \\((S_2)\\) with center \\(J%s\\). Find the radius of \\((S_2)\\).'])
    qv = V(lv, ['Hai quả cầu tiếp xúc ngoài với nhau (hình vẽ). Quả thứ nhất là \\(%s\\); quả thứ hai có tâm \\(J%s\\). Bán kính quả thứ hai là…', 'Mặt cầu tâm \\(J%s\\) tiếp xúc ngoài với \\((S): %s\\). Bán kính của mặt cầu đó là…', 'Hai mặt cầu tiếp xúc nhau tại \\(T\\) (hình vẽ): \\((S_1): %s\\) và \\((S_2)\\) có tâm \\(J%s\\). Tìm bán kính của \\((S_2)\\).'])
    if lv == 2: en = qe % (P3(I2), sph(I1, R1 * R1)); vi = qv % (P3(I2), sph(I1, R1 * R1))
    else: en = qe % (sph(I1, R1 * R1), P3(I2)); vi = qv % (sph(I1, R1 * R1), P3(I2))
    return dict(en=en, vi=vi, opts=nopts(r, R2, [d, d + R1, R1, d * d - R1 * R1]), fig=Q3D(cfg, 'Two spheres touching at T', px=320),
                ee='\\(IJ=%d=R_1+R_2\\Rightarrow R_2=%d-%d=%d\\).' % (d, d, R1, R2), ev='\\(IJ=%d=R_1+R_2\\Rightarrow R_2=%d-%d=%d\\).' % (d, d, R1, R2))

def s17_d_tanplane(r, lv, ctx):
    I = (r.randint(-2, 2), r.randint(-2, 2), r.randint(-2, 2)); u, d = trip(r); A = tuple(i + x for i, x in zip(I, u))
    g = eq(*u, -dot3(u, A)); b1 = eq(*u, -dot3(u, I)); b2 = eq(*A, -dot3(A, A)) if dot3(A, A) else eq(*u, dot3(u, A)); b3 = eq(*u, dot3(u, A))
    O_ = [M(g), M(b1), M(b2), M(b3)]
    if len(set(O_)) < 4: raise AssertionError
    qe = V(lv, ['The point \\(A%s\\) lies on the sphere \\(%s\\). The tangent plane to the sphere at \\(A\\) is…', 'Write the equation of the plane tangent to \\((S): %s\\) at \\(A%s\\).', 'The plane touching \\(%s\\) at the point \\(A%s\\) has the equation…'])
    qv = V(lv, ['Điểm \\(A%s\\) thuộc mặt cầu \\(%s\\). Tiếp diện của mặt cầu tại \\(A\\) là…', 'Viết phương trình mặt phẳng tiếp xúc với \\((S): %s\\) tại \\(A%s\\).', 'Mặt phẳng tiếp xúc với \\(%s\\) tại điểm \\(A%s\\) có phương trình…'])
    if lv == 1: en = qe % (P3(A), sph(I, d * d)); vi = qv % (P3(A), sph(I, d * d))
    else: en = qe % (sph(I, d * d), P3(A)); vi = qv % (sph(I, d * d), P3(A))
    return dict(en=en, vi=vi, opts=O_, ee='Normal vector \\(\\overrightarrow{IA}=%s\\), the plane passes through \\(A\\): \\(%s\\).' % (P3(u), g),
                ev='Vectơ pháp tuyến \\(\\overrightarrow{IA}=%s\\), mặt phẳng đi qua \\(A\\): \\(%s\\).' % (P3(u), g))

NORM3 = [(1, 2, 2), (2, -1, 2), (2, 2, -1), (1, -2, 2), (2, 1, -2)]
def s17_d_parallel(r, lv, ctx):
    n = r.choice(NORM3); I = (r.randint(-2, 2), r.randint(-2, 2), r.randint(-2, 2)); R = r.randint(1, 3); k = dot3(n, I)
    m1, m2 = -k + 3 * R, -k - 3 * R
    def pr(a, b): return M('m=%d' % a) if a == b else M('m=%d\\ \\text{or}\\ m=%d' % (min(a, b), max(a, b)))
    def prv(a, b): return M('m=%d' % a) if a == b else M('m=%d\\ \\text{hoặc}\\ m=%d' % (min(a, b), max(a, b)))
    pairs = [(m1, m2), (-k + R, -k - R), (k + 3 * R, k - 3 * R), (-k + 9 * R, -k - 9 * R)]
    if len(set(tuple(sorted(p)) for p in pairs)) < 4: raise AssertionError
    pl = '%s+m=0' % eq(*n, 0)[:-2]
    qe = V(lv, ['Find \\(m\\) so that the plane \\((P): %s\\) is tangent to \\((S): %s\\).', 'The plane \\(%s\\) touches the sphere \\(%s\\) exactly when…', 'For which \\(m\\) is \\((P): %s\\) a tangent plane of \\(%s\\)?'])
    qv = V(lv, ['Tìm \\(m\\) để mặt phẳng \\((P): %s\\) tiếp xúc với \\((S): %s\\).', 'Mặt phẳng \\(%s\\) tiếp xúc với mặt cầu \\(%s\\) khi và chỉ khi…', 'Với giá trị nào của \\(m\\) thì \\((P): %s\\) là tiếp diện của \\(%s\\)?'])
    return dict(en=qe % (pl, sph(I, R * R)), vi=qv % (pl, sph(I, R * R)), opts=[tt(pr(*p), prv(*p)) for p in pairs],
                ee='\\(d(I,(P))=\\dfrac{|%d+m|}{3}=%d\\Leftrightarrow m=%d\\) or \\(m=%d\\).' % (k, R, m1, m2), ev='\\(d(I,(P))=\\dfrac{|%d+m|}{3}=%d\\Leftrightarrow m=%d\\) hoặc \\(m=%d\\).' % (k, R, m1, m2))

B17 = dict(A=[s17_tan_oxy, s17_diam, s17_reflect], B=[s17_tf_tanxz], C=[s17_sh_m],
           D=[s17_d_box, s17_d_three, s17_d_maxdist, s17_d_error, s17_d_chord, s17_d_touch, s17_d_tanplane, s17_d_parallel])

# ================================================================ BÀI 18, 19 – xác suất có điều kiện, toàn phần, Bayes
from mb_pgf import venn_svg
def pe(x): return ne(F(x))
def pv(x): return nv(F(x))
def popt(good, bads):
    out = [nopt(F(good))]
    for b in bads:
        b = F(b)
        if 0 <= b <= 1 and b != F(good) and nopt(b) not in out: out.append(nopt(b))
        if len(out) == 4: return out
    raise AssertionError('thiếu phương án')
def dec(x, d=(2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 200, 250, 500, 1000)): return F(x).denominator in d

def tree_tex(pb, x, y, lang, hide=None, names=('B', 'A'), labels=None):
    """Sơ đồ hình cây hai tầng: P(B)=pb; P(A|B)=x; P(A|B̄)=y. hide ∈ {'b','x','y',None}: nhánh ghi '?'."""
    N = (lambda v: ne(v)) if lang == 'en' else (lambda v: nv(v))
    B, A = names; Bn = '\\overline{%s}' % B; An = '\\overline{%s}' % A
    if labels: B, Bn, A, An = labels
    lab = {'b': N(pb), 'nb': N(1 - pb), 'x': N(x), 'nx': N(1 - x), 'y': N(y), 'ny': N(1 - y)}
    if hide == 'b': lab['b'] = lab['nb'] = '?'
    if hide == 'x': lab['x'] = '?'; lab['nx'] = '?'
    if hide == 'y': lab['y'] = '?'; lab['ny'] = '?'
    o = ['\\begin{tikzpicture}[x=1cm,y=1cm]']
    nodes = [((0, 0), ''), ((2.8, 1.35), B), ((2.8, -1.35), Bn), ((5.6, 2.05), A), ((5.6, 0.65), An), ((5.6, -0.65), A), ((5.6, -2.05), An)]
    edges = [(0, 1, 'b'), (0, 2, 'nb'), (1, 3, 'x'), (1, 4, 'nx'), (2, 5, 'y'), (2, 6, 'ny')]
    for a, b, k in edges:
        (x0, y0), (x1, y1) = nodes[a][0], nodes[b][0]
        o.append('\\draw[color=%s, line width=0.9pt] (%.2f,%.2f) -- (%.2f,%.2f);' % (col('046b4d'), x0 + (0.25 if a else 0.08), y0, x1 - 0.32, y1))
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2 + (0.28 if y1 >= y0 else -0.28)
        o.append('\\node[font=\\small, text=%s, fill=white, inner sep=1pt] at (%.2f,%.2f) {$%s$};' % ('c2410c' if lab[k] == '?' else 'ink', mx, my, lab[k]))
    o.append('\\fill[ink] (0,0) circle (2pt);')
    for (px, py), t in nodes[1:]: o.append('\\node[text=ink] at (%.2f,%.2f) {$%s$};' % (px, py, t))
    o.append('\\end{tikzpicture}')
    return '\n'.join(o).replace('text=c2410c', 'text={rgb,255:red,194;green,65;blue,12}')
def TREE(pb, x, y, hide=None, names=('B', 'A'), labels=None):
    fe = texsvg(tree_tex(pb, x, y, 'en', hide, names, labels)); fv = texsvg(tree_tex(pb, x, y, 'vi', hide, names, labels))
    return (G.img(fe, 'Tree diagram', 330), G.img(fv, 'Sơ đồ hình cây', 330))

def twoway(rows, cols, data, lang, unknown=None):
    """Bảng hai chiều có dòng/cột tổng. rows, cols: [(en, vi)]; data: ma trận số; unknown = (i, j) ô ghi x."""
    L = 0 if lang == 'en' else 1; tot = ('Total', 'Tổng')[L]
    R = len(rows); C = len(cols)
    rs = [sum(data[i]) for i in range(R)]; cs = [sum(data[i][j] for i in range(R)) for j in range(C)]; n = sum(rs)
    cell = lambda i, j: 'x' if unknown == (i, j) else str(data[i][j])
    head = '<thead><tr><th></th>%s<th>%s</th></tr></thead>' % (''.join('<th>%s</th>' % c[L] for c in cols), tot)
    body = ''.join('<tr><th scope="row">%s</th>%s<td>%s</td></tr>' % (rows[i][L], ''.join('<td>\\(%s\\)</td>' % cell(i, j) for j in range(C)), '?' if False else ('\\(%s\\)' % ('%d+x' % (rs[i] - data[i][unknown[1]]) if unknown and unknown[0] == i else rs[i]))) for i in range(R))
    body += '<tr><th scope="row">%s</th>%s<td>\\(%s\\)</td></tr>' % (tot, ''.join('<td>\\(%s\\)</td>' % ('%d+x' % (cs[j] - data[unknown[0]][j]) if unknown and unknown[1] == j else cs[j]) for j in range(C)), ('%d+x' % (n - data[unknown[0]][unknown[1]])) if unknown else n)
    return '<div class="mbl-tablewrap"><table class="mbl-table">%s<tbody>%s</tbody></table></div>' % (head, body)
def TW(rows, cols, data, unknown=None): return (twoway(rows, cols, data, 'en', unknown), twoway(rows, cols, data, 'vi', unknown))

# ---------------- Bài 18
T18 = [(('Uses the school bus', 'Đi xe buýt của trường'), ('Does not', 'Không đi')), (('Plays a sport', 'Chơi thể thao'), ('Does not', 'Không chơi')), (('Reads e-books', 'Đọc sách điện tử'), ('Does not', 'Không đọc'))]
G18 = [('Grade 10', 'Khối 10'), ('Grade 11', 'Khối 11')]
def p18_tree_and(r, lv, ctx):
    pb = F(r.choice([3, 4, 6, 7]), 10); x = F(r.choice([5, 6, 7, 8, 9]), 10); y = F(r.choice([1, 2, 3]), 10)
    which = (lv - 1) % 3; good = [(1 - pb) * y, pb * (1 - x), (1 - pb) * (1 - y)][which]
    ev = ['\\overline B\\cap A', 'B\\cap\\overline A', '\\overline B\\cap\\overline A'][which]
    qe = V(lv, ['The tree diagram shows \\(P(B)\\), \\(P(A\\mid B)\\) and \\(P(A\\mid\\overline B)\\). Find \\(P(%s)\\).', 'Using the tree diagram, \\(P(%s)=\\)…', 'Read the tree diagram. The probability \\(P(%s)\\) is…'])
    qv = V(lv, ['Sơ đồ hình cây cho \\(P(B)\\), \\(P(A\\mid B)\\) và \\(P(A\\mid\\overline B)\\). Tính \\(P(%s)\\).', 'Dựa vào sơ đồ hình cây, \\(P(%s)=\\)…', 'Đọc sơ đồ hình cây. Xác suất \\(P(%s)\\) là…'])
    bads = [y, 1 - pb, pb * x, (1 - pb) + y, 1 - good, x * y]
    return dict(en=qe % ev, vi=qv % ev, opts=popt(good, bads), fig=TREE(pb, x, y),
                ee='Multiply along the branch: \\(P(%s)=%s\\).' % (ev, pe(good)), ev='Nhân các xác suất dọc theo nhánh: \\(P(%s)=%s\\).' % (ev, pv(good)))

def p18_count(r, lv, ctx):
    k = (lv - 1) % 3
    if k == 0:
        N = r.choice([20, 24, 30, 36]); a, b = r.choice([(2, 3), (3, 4), (2, 5), (4, 3)])
        B = [i for i in range(1, N + 1) if i % a == 0]; AB = [i for i in B if i % b == 0]; good = F(len(AB), len(B))
        return dict(en='A card is drawn from cards numbered 1 to %d. Given that the number is divisible by %d, the probability that it is divisible by %d is…' % (N, a, b),
                    vi='Rút ngẫu nhiên một thẻ từ các thẻ đánh số 1 đến %d. Biết số trên thẻ chia hết cho %d, xác suất số đó chia hết cho %d là…' % (N, a, b),
                    opts=popt(good, [F(len(AB), N), F(N // b, N), F(len(B), N), F(len(AB) + 1, len(B))]),
                    ee='\\(n(B)=%d\\), \\(n(A\\cap B)=%d\\): \\(P=%s\\).' % (len(B), len(AB), pe(good)), ev='\\(n(B)=%d\\), \\(n(A\\cap B)=%d\\): \\(P=%s\\).' % (len(B), len(AB), pv(good)))
    if k == 1:
        s = r.choice([5, 6, 7, 8, 9]); B = [(i, j) for i in range(1, 7) for j in range(1, 7) if i + j == s]; v = r.choice(sorted({i for i, j in B}))
        AB = [p for p in B if p[0] == v or p[1] == v]; good = F(len(AB), len(B))
        return dict(en='Two dice are rolled. Given that the sum of the dots is %d, the probability that at least one die shows %d is…' % (s, v),
                    vi='Gieo hai con xúc xắc cân đối. Biết tổng số chấm bằng %d, xác suất có ít nhất một con ra %d chấm là…' % (s, v),
                    opts=popt(good, [F(len(AB), 36), F(11, 36), F(1, 6), F(1, len(B)), F(len(AB) - 1, len(B))]),
                    ee='\\(n(B)=%d\\) outcomes with sum %d; %d of them contain %d: \\(P=%s\\).' % (len(B), s, len(AB), v, pe(good)), ev='Có \\(n(B)=%d\\) kết quả tổng %d; %d kết quả có mặt %d: \\(P=%s\\).' % (len(B), s, len(AB), v, pv(good)))
    n = r.choice([3, 4]); B = [c for c in range(2 ** n) if bin(c).count('1') >= 1]; m = r.choice([2, n]) if n == 4 else n
    AB = [c for c in B if bin(c).count('1') >= m]; good = F(len(AB), len(B))
    return dict(en='A family has %d children; boys and girls are equally likely. Given that there is at least one boy, the probability that there are at least %d boys is…' % (n, m),
                vi='Một gia đình có %d con, khả năng sinh trai hay gái như nhau. Biết gia đình có ít nhất một con trai, xác suất có ít nhất %d con trai là…' % (n, m),
                opts=popt(good, [F(len(AB), 2 ** n), F(1, 2), F(len(AB), len(B) + 1), F(1, 2 ** n)]),
                ee='\\(n(B)=%d\\) of the \\(%d\\) equally likely families; \\(n(A\\cap B)=%d\\): \\(P=%s\\).' % (len(B), 2 ** n, len(AB), pe(good)), ev='\\(n(B)=%d\\) trong \\(%d\\) khả năng; \\(n(A\\cap B)=%d\\): \\(P=%s\\).' % (len(B), 2 ** n, len(AB), pv(good)))

def p18_indep(r, lv, ctx):
    (ye, ne_) = T18[(lv - 1) % 3]
    ind = r.random() < .5
    for _ in range(200):
        a = r.randint(4, 20); b = r.randint(4, 20); k = F(r.choice([1, 2, 3]), r.choice([2, 3, 4]))
        if ind: c, d = a * k, b * k
        else: c, d = a * k + r.choice([-2, 2, 3]), b * k
        if F(c).denominator == 1 and F(d).denominator == 1 and c > 0 and d > 0: c, d = int(c), int(d); break
    data = [[a, b], [c, d]]; n = a + b + c + d; pA = F(a + c, n); pAB = F(a, a + b)
    if (pA == pAB) != ind: raise AssertionError
    S = [('\\(A\\) and \\(B\\) are independent because \\(P(A\\mid B)=P(A)\\).', '\\(A\\) và \\(B\\) độc lập vì \\(P(A\\mid B)=P(A)\\).'),
         ('\\(A\\) and \\(B\\) are not independent because \\(P(A\\mid B)\\ne P(A)\\).', '\\(A\\) và \\(B\\) không độc lập vì \\(P(A\\mid B)\\ne P(A)\\).'),
         ('\\(A\\) and \\(B\\) are mutually exclusive.', '\\(A\\) và \\(B\\) xung khắc.'), ('\\(P(A\\mid B)=P(B\\mid A)\\).', '\\(P(A\\mid B)=P(B\\mid A)\\).')]
    if not ind: S[0], S[1] = S[1], S[0]
    if F(a, a + c) == pAB: raise AssertionError
    return dict(en='A survey of %d students (table). A student is chosen at random. \\(A\\): "the student %s"; \\(B\\): "the student is in %s". Which statement is correct?' % (n, ye[0].lower().replace('uses', 'uses').replace('plays', 'plays').replace('reads', 'reads'), G18[0][0]),
                vi='Khảo sát %d học sinh (bảng). Chọn ngẫu nhiên một học sinh. \\(A\\): "học sinh %s"; \\(B\\): "học sinh thuộc %s". Khẳng định nào đúng?' % (n, ye[1].lower(), G18[0][1].lower()),
                opts=[tt(*x) for x in S], fig=TW(G18, [ye, ne_], data),
                ee='\\(P(A)=\\frac{%d}{%d}=%s\\), \\(P(A\\mid B)=\\frac{%d}{%d}=%s\\).' % (a + c, n, pe(pA), a, a + b, pe(pAB)), ev='\\(P(A)=\\frac{%d}{%d}=%s\\), \\(P(A\\mid B)=\\frac{%d}{%d}=%s\\).' % (a + c, n, pv(pA), a, a + b, pv(pAB)))

def p18_tf_tree(r, lv, ctx):
    pb = F(r.choice([2, 3, 4, 6]), 10); x = F(r.choice([6, 7, 8, 9]), 10); y = F(r.choice([1, 2, 3, 4]), 10); truth = r.random() < .5
    claim = 1 - x if truth else r.choice([x, (1 - pb) * (1 - x), pb * (1 - x)])
    if claim == 1 - x and not truth: raise AssertionError
    qe = V(lv, ['From the tree diagram, \\(P(\\overline A\\mid B)=%s\\).', 'In the tree diagram, the probability that \\(A\\) does not occur given \\(B\\) equals \\(%s\\).', 'The tree diagram gives \\(P(\\overline A\\mid B)=%s\\).'])
    qv = V(lv, ['Theo sơ đồ hình cây, \\(P(\\overline A\\mid B)=%s\\).', 'Trong sơ đồ hình cây, xác suất \\(A\\) không xảy ra khi biết \\(B\\) bằng \\(%s\\).', 'Sơ đồ hình cây cho \\(P(\\overline A\\mid B)=%s\\).'])
    return dict(en=qe % pe(claim), vi=qv % pv(claim), truth=truth, fig=TREE(pb, x, y), ee='\\(P(\\overline A\\mid B)=1-P(A\\mid B)=%s\\).' % pe(1 - x), ev='\\(P(\\overline A\\mid B)=1-P(A\\mid B)=%s\\).' % pv(1 - x))

def p18_sh_cell(r, lv, ctx):
    (ye, ne_) = T18[(lv - 1) % 3]
    for _ in range(400):
        p = r.choice([F(1, 4), F(1, 3), F(2, 5), F(1, 2), F(3, 5), F(2, 3), F(3, 4)]); b = r.randint(4, 20); a = p * b / (1 - p)
        if a.denominator == 1 and 3 <= a <= 40: a = int(a); break
    else: raise AssertionError
    c = r.randint(5, 20); d = r.randint(5, 20); data = [[c, d], [a, b]]
    pt = frt(p)
    qe = V(lv, ['In the table, one number is missing. Given that \\(P(\\text{%s}\\mid\\text{%s})=%s\\), find \\(x\\).', 'The probability that a %s student %s is \\(%s\\). Find \\(x\\).', 'Knowing \\(P(\\text{%s}\\mid\\text{%s})=%s\\), calculate the missing number \\(x\\).'])
    qv = V(lv, ['Trong bảng có một số bị thiếu. Biết \\(P(\\text{%s}\\mid\\text{%s})=%s\\), tìm \\(x\\).', 'Xác suất một học sinh %s %s là \\(%s\\). Tìm \\(x\\).', 'Biết \\(P(\\text{%s}\\mid\\text{%s})=%s\\), tính số còn thiếu \\(x\\).'])
    g1e, g1v = G18[1]
    if lv == 2: en = qe % (g1e, ye[0].lower(), pt); vi = qv % (g1v.lower(), ye[1].lower(), pt)
    else: en = qe % (ye[0].lower(), g1e, pt); vi = qv % (ye[1].lower(), g1v.lower(), pt)
    return dict(en=en, vi=vi, key=str(a), fig=TW(G18, [ye, ne_], data, unknown=(1, 0)),
                ee='\\(\\dfrac{x}{x+%d}=%s\\Rightarrow x=%d\\).' % (b, pt, a), ev='\\(\\dfrac{x}{x+%d}=%s\\Rightarrow x=%d\\).' % (b, pt, a))

def p18_d_notation(r, lv, ctx):
    k = (lv - 1) % 3
    C = [(('a girl', 'nữ'), ('wears glasses', 'đeo kính'), 'G', 'K'), (('a smoker', 'hút thuốc'), ('has a cough', 'bị ho'), 'S', 'H'), (('rainy', 'mưa'), ('the bus is late', 'xe buýt đến muộn'), 'R', 'L')][k]
    (ge, gv), (we, wv), g, w = C
    if k == 0: en = 'A student is chosen. \\(G\\): "the student is %s"; \\(K\\): "the student %s". The probability that a chosen girl wears glasses is…' % (ge, we); vi = 'Chọn một học sinh. \\(G\\): "học sinh là %s"; \\(K\\): "học sinh %s". Xác suất để một bạn nữ được chọn có đeo kính là…' % (gv, wv)
    elif k == 1: en = 'A person is chosen. \\(S\\): "the person is %s"; \\(H\\): "the person %s". The probability that a smoker has a cough is…' % (ge, we); vi = 'Chọn một người. \\(S\\): "người đó %s"; \\(H\\): "người đó %s". Xác suất một người hút thuốc bị ho là…' % (gv, wv)
    else: en = 'A day is chosen. \\(R\\): "the day is %s"; \\(L\\): "%s". On a rainy day, the probability that the bus is late is…' % (ge, we); vi = 'Chọn một ngày. \\(R\\): "ngày đó %s"; \\(L\\): "%s". Vào một ngày mưa, xác suất xe buýt đến muộn là…' % (gv, wv)
    if k == 0: g, w = 'G', 'K'
    opts = [M('P(%s\\mid %s)' % (w, g)), M('P(%s\\mid %s)' % (g, w)), M('P(%s\\cap %s)' % (w, g)), M('P(%s)' % w)]
    return dict(en=en, vi=vi, opts=opts, ee='The known event (the condition) is \\(%s\\), so we need \\(P(%s\\mid %s)\\).' % (g, w, g), ev='Biến cố đã biết (điều kiện) là \\(%s\\) nên cần \\(P(%s\\mid %s)\\).' % (g, w, g))

def p18_d_error(r, lv, ctx):
    (ye, ne_) = T18[(lv - 1) % 3]; a, b, c, d = [r.randint(5, 25) for _ in range(4)]; n = a + b + c + d
    good = F(a, a + b); bad = F(a, n)
    if good == bad: raise AssertionError
    def T(lang):
        N = pe if lang == 'en' else pv; L = 0 if lang == 'en' else 1
        s1 = ('\\(n(\\Omega)=%d\\), %s: %d.' if lang == 'en' else '\\(n(\\Omega)=%d\\), %s: %d.') % (n, ('%s and in %s' % (ye[0].lower(), G18[0][0])) if lang == 'en' else ('%s và thuộc %s' % (ye[1].lower(), G18[0][1].lower())), a)
        s2 = '\\(P(A\\mid B)=\\dfrac{%d}{%d}\\).' % (a, n)
        return ('A student found the probability that a %s student %s. Step 1: %s Step 2: %s Which comment is correct?' if lang == 'en' else 'Một bạn tính xác suất một học sinh %s %s. Bước 1: %s Bước 2: %s Nhận xét nào đúng?') % (
            (G18[0][0], ye[0].lower(), s1, s2) if lang == 'en' else (G18[0][1].lower(), ye[1].lower(), s1, s2))
    S = [('Step 2 is wrong: divide by \\(n(B)=%d\\), the number of %s students.' % (a + b, G18[0][0]), 'Bước 2 sai: phải chia cho \\(n(B)=%d\\) là số học sinh %s.' % (a + b, G18[0][1].lower())),
         ('Step 1 is wrong.', 'Bước 1 sai.'), ('The solution is correct.', 'Lời giải đúng.'), ('Step 2 should divide by %d.' % (a + c), 'Bước 2 phải chia cho %d.' % (a + c))]
    return dict(en=T('en'), vi=T('vi'), opts=[tt(*x) for x in S], fig=TW(G18, [ye, ne_], [[a, b], [c, d]]),
                ee='Given \\(B\\), only the %d students of %s count: \\(P(A\\mid B)=\\frac{%d}{%d}=%s\\).' % (a + b, G18[0][0], a, a + b, pe(good)), ev='Khi biết \\(B\\), chỉ xét %d học sinh %s: \\(P(A\\mid B)=\\frac{%d}{%d}=%s\\).' % (a + b, G18[0][1].lower(), a, a + b, pv(good)))

def p18_d_replace(r, lv, ctx):
    rd, bl = r.randint(3, 7), r.randint(2, 6); n = rd + bl; w = F(rd, n) ** 2; wo = F(rd, n) * F(rd - 1, n - 1)
    S = [('Without replacement: \\(%s\\); with replacement: \\(%s\\). Drawing without replacement gives the smaller probability.' % (frt(wo), frt(w)), 'Không hoàn lại: \\(%s\\); có hoàn lại: \\(%s\\). Lấy không hoàn lại cho xác suất nhỏ hơn.' % (frt(wo), frt(w))),
         ('Both ways give \\(%s\\).' % frt(w), 'Hai cách đều cho \\(%s\\).' % frt(w)), ('Without replacement: \\(%s\\); with replacement: \\(%s\\).' % (frt(w), frt(wo)), 'Không hoàn lại: \\(%s\\); có hoàn lại: \\(%s\\).' % (frt(w), frt(wo))),
         ('Both ways give \\(%s\\).' % frt(wo), 'Hai cách đều cho \\(%s\\).' % frt(wo))]
    E = [('A bag has %d red and %d blue balls. Two balls are drawn one after the other. Compare the probability that both are red when drawing with and without replacement.', 'Túi có %d bi đỏ và %d bi xanh. Lấy lần lượt hai bi. So sánh xác suất cả hai bi đỏ khi lấy có hoàn lại và không hoàn lại.'),
         ('A class has %d boys and %d girls. Two names are picked one after the other for two duties. Compare the probability that both are boys if the same name may (or may not) be picked twice.', 'Lớp có %d nam và %d nữ. Chọn lần lượt hai tên cho hai nhiệm vụ. So sánh xác suất cả hai là nam khi một tên được (hoặc không được) chọn lại.'),
         ('A box has %d good and %d faulty bulbs. Two bulbs are tested one after the other. Compare the probability that both are good with and without putting the first bulb back.', 'Hộp có %d bóng tốt và %d bóng hỏng. Thử lần lượt hai bóng. So sánh xác suất cả hai bóng tốt khi có và không trả bóng đầu tiên lại.')][(lv - 1) % 3]
    return dict(en=E[0] % (rd, bl), vi=E[1] % (rd, bl), opts=[tt(*x) for x in S],
                ee='With: \\(\\left(\\frac{%d}{%d}\\right)^2\\); without: \\(\\frac{%d}{%d}\\cdot\\frac{%d}{%d}\\).' % (rd, n, rd, n, rd - 1, n - 1), ev='Có hoàn lại: \\(\\left(\\frac{%d}{%d}\\right)^2\\); không hoàn lại: \\(\\frac{%d}{%d}\\cdot\\frac{%d}{%d}\\).' % (rd, n, rd, n, rd - 1, n - 1))

def p18_d_back(r, lv, ctx):
    pb = F(r.choice([2, 3, 4, 5, 6, 8]), 10); x = F(r.choice([1, 2, 3, 4]), 5); pab = pb * x
    if not dec(pab): raise AssertionError
    qe = V(lv, ['\\(P(A\\cap B)=%s\\) and \\(P(A\\mid B)=%s\\). Then \\(P(B)=\\)…', 'Given \\(P(A\\mid B)=%s\\) and \\(P(A\\cap B)=%s\\), find \\(P(B)\\).', 'If \\(P(A\\cap B)=%s\\), \\(P(A\\mid B)=%s\\), the probability of \\(B\\) is…'])
    qv = V(lv, ['\\(P(A\\cap B)=%s\\) và \\(P(A\\mid B)=%s\\). Khi đó \\(P(B)=\\)…', 'Cho \\(P(A\\mid B)=%s\\) và \\(P(A\\cap B)=%s\\). Tìm \\(P(B)\\).', 'Nếu \\(P(A\\cap B)=%s\\), \\(P(A\\mid B)=%s\\) thì xác suất của \\(B\\) là…'])
    args = (pe(x), pe(pab)) if lv == 2 else (pe(pab), pe(x)); argv = (pv(x), pv(pab)) if lv == 2 else (pv(pab), pv(x))
    return dict(en=qe % args, vi=qv % argv, opts=popt(pb, [pab * x, x - pab, 1 - pb, pab, x]),
                ee='\\(P(B)=\\dfrac{P(A\\cap B)}{P(A\\mid B)}=%s\\).' % pe(pb), ev='\\(P(B)=\\dfrac{P(A\\cap B)}{P(A\\mid B)}=%s\\).' % pv(pb))

def p18_d_three(r, lv, ctx):
    a, b = r.randint(4, 8), r.randint(2, 5); n = a + b; good = F(a, n) * F(a - 1, n - 1) * F(a - 2, n - 2)
    E = [('A box has %d red and %d white balls. Three balls are drawn one by one without replacement. The probability that all three are red is…', 'Hộp có %d bi đỏ và %d bi trắng. Lấy lần lượt ba bi không hoàn lại. Xác suất cả ba bi đều đỏ là…'),
         ('Among %d good and %d faulty phones, three are tested one after another (not returned). The probability that all three are good is…', 'Trong %d điện thoại tốt và %d điện thoại lỗi, kiểm tra lần lượt ba chiếc (không trả lại). Xác suất cả ba chiếc đều tốt là…'),
         ('A team of %d boys and %d girls picks three captains one after another. The probability that all three are boys is…', 'Một đội gồm %d nam và %d nữ chọn lần lượt ba đội trưởng. Xác suất cả ba đều là nam là…')][(lv - 1) % 3]
    return dict(en=E[0] % (a, b), vi=E[1] % (a, b), opts=popt(good, [F(a, n) ** 3, F(a, n) * F(a - 1, n - 1), F(a - 2, n - 2), F(3 * a, n * 3) * F(a - 1, n)]),
                ee='\\(\\frac{%d}{%d}\\cdot\\frac{%d}{%d}\\cdot\\frac{%d}{%d}=%s\\).' % (a, n, a - 1, n - 1, a - 2, n - 2, frt(good)), ev='\\(\\frac{%d}{%d}\\cdot\\frac{%d}{%d}\\cdot\\frac{%d}{%d}=%s\\).' % (a, n, a - 1, n - 1, a - 2, n - 2, frt(good)))

def p18_d_union(r, lv, ctx):
    pa = F(r.choice([2, 3, 4, 5]), 10); x = F(r.choice([1, 2, 3, 4]), 5); pb = F(r.choice([3, 4, 5, 6]), 10); pab = pa * x
    if pab > min(pa, pb) or not dec(pab): raise AssertionError
    good = pa + pb - pab
    E = [('\\(P(A)=%s\\), \\(P(B\\mid A)=%s\\), \\(P(B)=%s\\). Then \\(P(A\\cup B)=\\)…', '\\(P(A)=%s\\), \\(P(B\\mid A)=%s\\), \\(P(B)=%s\\). Khi đó \\(P(A\\cup B)=\\)…'),
         ('The probability of rain is %s; if it rains, the football match is cancelled with probability %s; overall a match is cancelled with probability %s. The probability that it rains or the match is cancelled is…', 'Xác suất trời mưa là %s; nếu mưa thì trận bóng bị hoãn với xác suất %s; xác suất trận bóng bị hoãn là %s. Xác suất trời mưa hoặc trận bóng bị hoãn là…'),
         ('A student revises with probability %s; given that he revises, he passes with probability %s; he passes with probability %s. The probability that he revises or passes is…', 'Một học sinh ôn bài với xác suất %s; nếu ôn bài thì đạt với xác suất %s; xác suất đạt là %s. Xác suất học sinh ôn bài hoặc đạt là…')][(lv - 1) % 3]
    return dict(en=E[0] % (pe(pa), pe(x), pe(pb)), vi=E[1] % (pv(pa), pv(x), pv(pb)), opts=popt(good, [pa + pb, pa + pb - pa * pb, pab, pa + pb - x, 1 - pab]),
                ee='\\(P(A\\cap B)=P(A)P(B\\mid A)=%s\\); \\(P(A\\cup B)=%s+%s-%s=%s\\).' % (pe(pab), pe(pa), pe(pb), pe(pab), pe(good)),
                ev='\\(P(A\\cap B)=P(A)P(B\\mid A)=%s\\); \\(P(A\\cup B)=%s+%s-%s=%s\\).' % (pv(pab), pv(pa), pv(pb), pv(pab), pv(good)))

def p18_d_exclusive(r, lv, ctx):
    pa, pb = F(r.choice([2, 3, 4]), 10), F(r.choice([3, 4, 5]), 10)
    S = [('\\(P(A\\mid B)=0\\), so \\(A\\), \\(B\\) are not independent.', '\\(P(A\\mid B)=0\\) nên \\(A\\), \\(B\\) không độc lập.'), ('\\(P(A\\mid B)=%s\\), so \\(A\\), \\(B\\) are independent.' % pe(pa), '\\(P(A\\mid B)=%s\\) nên \\(A\\), \\(B\\) độc lập.' % pv(pa)),
         ('\\(P(A\\mid B)=%s\\).' % pe(pa * pb), '\\(P(A\\mid B)=%s\\).' % pv(pa * pb)), ('\\(P(A\\mid B)=1\\).', '\\(P(A\\mid B)=1\\).')]
    qe = V(lv, ['\\(A\\) and \\(B\\) are mutually exclusive with \\(P(A)=%s\\), \\(P(B)=%s\\). Which statement is correct?', 'Two events that cannot happen together have \\(P(A)=%s\\), \\(P(B)=%s\\). Choose the true statement.', 'If \\(A\\cap B=\\varnothing\\), \\(P(A)=%s\\) and \\(P(B)=%s\\), then…'])
    qv = V(lv, ['\\(A\\), \\(B\\) xung khắc với \\(P(A)=%s\\), \\(P(B)=%s\\). Khẳng định nào đúng?', 'Hai biến cố không thể cùng xảy ra có \\(P(A)=%s\\), \\(P(B)=%s\\). Chọn khẳng định đúng.', 'Nếu \\(A\\cap B=\\varnothing\\), \\(P(A)=%s\\), \\(P(B)=%s\\) thì…'])
    return dict(en=qe % (pe(pa), pe(pb)), vi=qv % (pv(pa), pv(pb)), opts=[tt(*x) for x in S],
                ee='\\(P(A\\cap B)=0\\Rightarrow P(A\\mid B)=0\\ne P(A)\\).', ev='\\(P(A\\cap B)=0\\Rightarrow P(A\\mid B)=0\\ne P(A)\\).')

V18 = [(('Math club', 'CLB Toán'), ('English club', 'CLB Tiếng Anh'), 'M', 'E'), (('Football', 'Bóng đá'), ('Badminton', 'Cầu lông'), 'F', 'C'), (('Tea', 'Trà'), ('Coffee', 'Cà phê'), 'T', 'C')]
def p18_d_venn(r, lv, ctx):
    (ae, av), (be, bv), la, lb = V18[(lv - 1) % 3]; x, y, z, w = r.randint(4, 15), r.randint(2, 10), r.randint(4, 15), r.randint(2, 10)
    good = F(y, y + z); fn = venn_svg(x, y, z, w, la, lb)
    qe = V(lv, ['The Venn diagram shows the students of a class: \\(%s\\) = %s, \\(%s\\) = %s. A student of the %s is chosen. The probability that the student is also in the %s is…', 'In the Venn diagram (\\(%s\\): %s, \\(%s\\): %s), find the probability that a person who likes %s also likes %s.', 'Using the Venn diagram (\\(%s\\): %s; \\(%s\\): %s), \\(P(%s\\mid %s)=\\)…'])
    qv = V(lv, ['Biểu đồ Venn mô tả học sinh một lớp: \\(%s\\) là %s, \\(%s\\) là %s. Chọn một học sinh thuộc %s. Xác suất học sinh đó cũng thuộc %s là…', 'Trong biểu đồ Venn (\\(%s\\): %s, \\(%s\\): %s), tính xác suất một người thích %s cũng thích %s.', 'Dựa vào biểu đồ Venn (\\(%s\\): %s; \\(%s\\): %s), \\(P(%s\\mid %s)=\\)…'])
    if lv == 3: en = qe % (la, ae, lb, be, la, lb); vi = qv % (la, av, lb, bv, la, lb)
    else: en = qe % (la, ae, lb, be, be if lv == 1 else be.lower(), ae if lv == 1 else ae.lower()); vi = qv % (la, av, lb, bv, bv if lv == 1 else bv.lower(), av if lv == 1 else av.lower())
    return dict(en=en, vi=vi, opts=popt(good, [F(y, x + y), F(y, x + y + z + w), F(y + z, x + y + z + w), F(z, y + z)]), fig=(G.img(fn, 'Venn diagram', 320), G.img(fn, 'Biểu đồ Venn', 320)),
                ee='Given \\(%s\\): \\(%d+%d=%d\\) people, \\(%d\\) of them in \\(%s\\): \\(P=%s\\).' % (lb, y, z, y + z, y, la, frt(good)), ev='Khi biết \\(%s\\): có \\(%d+%d=%d\\) người, trong đó \\(%d\\) người thuộc \\(%s\\): \\(P=%s\\).' % (lb, y, z, y + z, y, la, frt(good)))

B18 = dict(A=[p18_tree_and, p18_count, p18_indep], B=[p18_tf_tree], C=[p18_sh_cell],
           D=[p18_d_notation, p18_d_error, p18_d_replace, p18_d_back, p18_d_three, p18_d_union, p18_d_exclusive, p18_d_venn])

# ---------------- Bài 19
def p19_post3(r, lv, ctx):
    for _ in range(200):
        sh_ = r.choice([(50, 30, 20), (40, 35, 25), (45, 35, 20), (60, 25, 15), (30, 30, 40)]); d = [r.choice([1, 2, 3, 4, 5]) for _ in range(3)]
        tot = sum(a * b for a, b in zip(sh_, d)); k = r.randrange(3); good = F(sh_[k] * d[k], tot)
        if len(set(d)) >= 2 and good.denominator <= 60: break
    names = [('I', 'I'), ('II', 'II'), ('III', 'III')][k]
    E = [('Three machines I, II, III make %d%%, %d%%, %d%% of the products of a factory; their defect rates are %d%%, %d%%, %d%%. A product is found defective. The probability that it was made by machine %s is…', 'Ba máy I, II, III sản xuất lần lượt %d%%, %d%%, %d%% sản phẩm của nhà máy; tỉ lệ phế phẩm lần lượt %d%%, %d%%, %d%%. Lấy được một phế phẩm. Xác suất phế phẩm đó do máy %s sản xuất là…'),
         ('Three farms I, II, III supply %d%%, %d%%, %d%% of the oranges of a market; %d%%, %d%%, %d%% of their oranges are spoiled. A spoiled orange is found. The probability that it came from farm %s is…', 'Ba trang trại I, II, III cung cấp %d%%, %d%%, %d%% số cam của một chợ; tỉ lệ cam hỏng lần lượt %d%%, %d%%, %d%%. Phát hiện một quả cam hỏng. Xác suất quả cam đó từ trang trại %s là…'),
         ('Three bus lines I, II, III carry %d%%, %d%%, %d%% of the students of a school; the late rates are %d%%, %d%%, %d%%. A student arrives late. The probability that the student took line %s is…', 'Ba tuyến xe buýt I, II, III chở %d%%, %d%%, %d%% học sinh của trường; tỉ lệ đến muộn lần lượt %d%%, %d%%, %d%%. Một học sinh đến muộn. Xác suất học sinh đó đi tuyến %s là…')][(lv - 1) % 3]
    args = tuple(sh_) + tuple(d) + (names[0],)
    return dict(en=E[0] % args, vi=E[1] % args, opts=fo(good, [F(sh_[k] * d[k], 10000), F(d[k], sum(d)), F(sh_[k], 100), F(sh_[k] * d[k], tot + 100)]),
                ee='\\(P(A)=%s\\%%\\); \\(P(B_%d\\mid A)=\\dfrac{%d\\cdot%d}{%d}=%s\\).' % (ne(F(tot, 100)), k + 1, sh_[k], d[k], tot, frt(good)),
                ev='\\(P(A)=%s\\%%\\); \\(P(B_%d\\mid A)=\\dfrac{%d\\cdot%d}{%d}=%s\\).' % (nv(F(tot, 100)), k + 1, sh_[k], d[k], tot, frt(good)))

def p19_move(r, lv, ctx):
    r1, w1, r2, w2 = r.randint(1, 5), r.randint(1, 5), r.randint(1, 5), r.randint(1, 5); n2 = r2 + w2 + 1
    good = F(r1, r1 + w1) * F(r2 + 1, n2) + F(w1, r1 + w1) * F(r2, n2)
    E = [('Box 1 has %d red and %d white balls; box 2 has %d red and %d white balls. One ball is moved from box 1 to box 2, then a ball is drawn from box 2. \\(P(\\text{red})=\\)…', 'Hộp 1 có %d bi đỏ, %d bi trắng; hộp 2 có %d bi đỏ, %d bi trắng. Chuyển một bi từ hộp 1 sang hộp 2 rồi lấy một bi từ hộp 2. Xác suất lấy được bi đỏ là…'),
         ('Bag A holds %d green and %d yellow tickets; bag B holds %d green and %d yellow. A ticket is taken from A and put into B; then a ticket is drawn from B. The probability that it is green is…', 'Túi A có %d phiếu xanh, %d phiếu vàng; túi B có %d phiếu xanh, %d phiếu vàng. Lấy một phiếu từ A bỏ vào B rồi rút một phiếu từ B. Xác suất rút được phiếu xanh là…'),
         ('Basket 1: %d ripe and %d unripe mangoes; basket 2: %d ripe and %d unripe. A mango is moved from basket 1 to basket 2, then one mango is taken from basket 2. Find the probability that it is ripe.', 'Rổ 1 có %d quả xoài chín, %d quả xanh; rổ 2 có %d quả chín, %d quả xanh. Chuyển một quả từ rổ 1 sang rổ 2 rồi lấy một quả từ rổ 2. Tính xác suất lấy được quả chín.')][(lv - 1) % 3]
    return dict(en=E[0] % (r1, w1, r2, w2), vi=E[1] % (r1, w1, r2, w2), opts=fo(good, [F(r2, r2 + w2), F(r2 + 1, n2), F(r1 + r2, r1 + w1 + r2 + w2), F(r1, r1 + w1) * F(r2 + 1, n2)]),
                ee='\\(\\frac{%d}{%d}\\cdot\\frac{%d}{%d}+\\frac{%d}{%d}\\cdot\\frac{%d}{%d}=%s\\).' % (r1, r1 + w1, r2 + 1, n2, w1, r1 + w1, r2, n2, frt(good)),
                ev='\\(\\frac{%d}{%d}\\cdot\\frac{%d}{%d}+\\frac{%d}{%d}\\cdot\\frac{%d}{%d}=%s\\).' % (r1, r1 + w1, r2 + 1, n2, w1, r1 + w1, r2, n2, frt(good)))

def p19_tree_post(r, lv, ctx):
    pb = F(r.choice([2, 3, 4, 5, 6]), 10); x = F(r.choice([6, 7, 8, 9]), 10); y = F(r.choice([1, 2, 3, 4]), 10)
    pa = pb * x + (1 - pb) * y; good = (1 - pb) * y / pa
    qe = V(lv, ['From the tree diagram, \\(P(\\overline B\\mid A)=\\)…', 'Given that \\(A\\) occurred, the probability that \\(B\\) did NOT occur (tree diagram) is…', 'Use the tree diagram to find \\(P(\\overline B\\mid A)\\).'])
    qv = V(lv, ['Theo sơ đồ hình cây, \\(P(\\overline B\\mid A)=\\)…', 'Biết \\(A\\) đã xảy ra, xác suất \\(B\\) KHÔNG xảy ra (sơ đồ hình cây) là…', 'Dùng sơ đồ hình cây, tính \\(P(\\overline B\\mid A)\\).'])
    return dict(en=qe, vi=qv, opts=fo(good, [(1 - pb) * y, y, 1 - pb, 1 - good, pb * x / pa]), fig=TREE(pb, x, y),
                ee='\\(P(A)=%s\\); \\(P(\\overline B\\mid A)=\\dfrac{%s}{%s}=%s\\).' % (pe(pa), pe((1 - pb) * y), pe(pa), frt(good)),
                ev='\\(P(A)=%s\\); \\(P(\\overline B\\mid A)=\\dfrac{%s}{%s}=%s\\).' % (pv(pa), pv((1 - pb) * y), pv(pa), frt(good)))

def p19_tf_update(r, lv, ctx):
    pb = F(r.choice([2, 3, 4, 5]), 10); x = F(r.choice([2, 3, 6, 7, 8]), 10); y = F(r.choice([2, 3, 5, 6]), 10)
    if x == y: raise AssertionError
    pa = pb * x + (1 - pb) * y; post = pb * x / pa; up = post > pb
    claim_up = r.random() < .5; truth = (claim_up == up)
    qe = V(lv, ['From the tree diagram: knowing that \\(A\\) occurred makes \\(B\\) %s likely, i.e. \\(P(B\\mid A)%s P(B)\\).', 'In the tree diagram, \\(P(B\\mid A)%s P(B)\\) (\\(A\\) makes \\(B\\) %s likely).', 'Using the tree diagram: \\(P(B\\mid A)%s P(B)\\).'])
    qv = V(lv, ['Theo sơ đồ hình cây: biết \\(A\\) đã xảy ra thì \\(B\\) %s, tức là \\(P(B\\mid A)%s P(B)\\).', 'Trong sơ đồ hình cây, \\(P(B\\mid A)%s P(B)\\) (\\(A\\) làm \\(B\\) %s).', 'Dùng sơ đồ hình cây: \\(P(B\\mid A)%s P(B)\\).'])
    rel = '\\gt' if claim_up else '\\lt'; we = 'more' if claim_up else 'less'; wv = 'dễ xảy ra hơn' if claim_up else 'khó xảy ra hơn'
    if lv == 1: en = qe % (we, rel); vi = qv % (wv, rel)
    elif lv == 2: en = qe % (rel, we); vi = qv % (rel, wv)
    else: en = qe % rel; vi = qv % rel
    return dict(en=en, vi=vi, truth=truth, fig=TREE(pb, x, y),
                ee='\\(P(A)=%s\\), \\(P(B\\mid A)=\\dfrac{%s}{%s}=%s\\), \\(P(B)=%s\\).' % (pe(pa), pe(pb * x), pe(pa), frt(post), pe(pb)),
                ev='\\(P(A)=%s\\), \\(P(B\\mid A)=\\dfrac{%s}{%s}=%s\\), \\(P(B)=%s\\).' % (pv(pa), pv(pb * x), pv(pa), frt(post), pv(pb)))

def p19_sh_branch(r, lv, ctx):
    pb = F(r.choice([2, 4, 5, 6, 8]), 10); x = F(r.choice([5, 6, 7, 8, 9]), 10); y = F(r.choice([5, 10, 15, 20, 25, 30, 40]), 100)
    pa = pb * x + (1 - pb) * y
    if not dec(pa, (2, 4, 5, 10, 20, 25, 50, 100)): raise AssertionError
    qe = V(lv, ['In the tree diagram one branch is unknown. Given \\(P(A)=%s\\), find \\(P(A\\mid\\overline B)\\) as a percentage.', 'The overall probability of \\(A\\) is \\(%s\\). Find the missing branch \\(P(A\\mid\\overline B)\\) (in %%).', 'Knowing \\(P(A)=%s\\), calculate \\(P(A\\mid\\overline B)\\) and write it in percent.'])
    qv = V(lv, ['Trong sơ đồ hình cây có một nhánh chưa biết. Biết \\(P(A)=%s\\), tìm \\(P(A\\mid\\overline B)\\) theo phần trăm.', 'Xác suất của \\(A\\) là \\(%s\\). Tìm nhánh còn thiếu \\(P(A\\mid\\overline B)\\) (đơn vị %%).', 'Biết \\(P(A)=%s\\), tính \\(P(A\\mid\\overline B)\\) và viết dưới dạng phần trăm.'])
    k = y * 100
    return dict(en=qe % pe(pa), vi=qv % pv(pa), key=key(k), fig=TREE(pb, x, y, hide='y'),
                ee='\\(%s=%s\\cdot%s+%s\\cdot y\\Rightarrow y=%s\\), i.e. %s%%.' % (pe(pa), pe(pb), pe(x), pe(1 - pb), pe(y), ne(k)),
                ev='\\(%s=%s\\cdot%s+%s\\cdot y\\Rightarrow y=%s\\), tức %s%%.' % (pv(pa), pv(pb), pv(x), pv(1 - pb), pv(y), nv(k)),
                hint=('Enter a number of percent, e.g. 15.', 'Nhập số phần trăm, ví dụ 15.'))

def p19_d_error(r, lv, ctx):
    pb = F(r.choice([1, 2, 3, 5]), 100); x = F(r.choice([90, 95, 98]), 100); y = F(r.choice([2, 4, 5, 10]), 100)
    pa = pb * x + (1 - pb) * y; post = pb * x / pa
    def T(lang):
        N = pe if lang == 'en' else pv
        s1 = '\\(P(+)=%s\\cdot%s+%s\\cdot%s=%s\\).' % (N(pb), N(x), N(1 - pb), N(y), N(pa))
        w = 'sick' if lang == 'en' else 'bệnh'
        s2 = '\\(P(\\text{%s}\\mid+)=P(+\\mid\\text{%s})=%s\\).' % (w, w, N(x))
        return ('A disease affects %s of people. A test is positive for %s of sick and %s of healthy people. A student computed the probability that a person with a positive test is sick. Step 1: %s Step 2: %s Which comment is correct?' if lang == 'en' else
                'Một bệnh có tỉ lệ mắc %s. Xét nghiệm dương tính với %s người bệnh và %s người khỏe. Một bạn tính xác suất người xét nghiệm dương tính bị bệnh. Bước 1: %s Bước 2: %s Nhận xét nào đúng?') % (
            '%s%%' % ne(pb * 100) if lang == 'en' else '%s%%' % nv(pb * 100), '%s%%' % ne(x * 100) if lang == 'en' else '%s%%' % nv(x * 100), '%s%%' % ne(y * 100) if lang == 'en' else '%s%%' % nv(y * 100), s1, s2)
    S = [('Step 2 is wrong: \\(P(\\text{sick}\\mid+)=\\dfrac{P(\\text{sick})P(+\\mid\\text{sick})}{P(+)}\\).', 'Bước 2 sai: \\(P(\\text{bệnh}\\mid+)=\\dfrac{P(\\text{bệnh})P(+\\mid\\text{bệnh})}{P(+)}\\).'),
         ('Step 1 is wrong.', 'Bước 1 sai.'), ('Both steps are correct.', 'Cả hai bước đều đúng.'), ('Step 1 must use \\(P(+)=%s+%s\\).' % (pe(x), pe(y)), 'Bước 1 phải dùng \\(P(+)=%s+%s\\).' % (pv(x), pv(y)))]
    return dict(en=T('en'), vi=T('vi'), opts=[tt(*z) for z in S], ee='\\(P(\\text{sick}\\mid+)=\\dfrac{%s}{%s}=%s\\), far from \\(%s\\).' % (pe(pb * x), pe(pa), frt(post), pe(x)),
                ev='\\(P(\\text{bệnh}\\mid+)=\\dfrac{%s}{%s}=%s\\), khác xa \\(%s\\).' % (pv(pb * x), pv(pa), frt(post), pv(x)))

def p19_d_twotests(r, lv, ctx):
    pb = F(r.choice([1, 2, 5, 10]), 100); x = F(r.choice([8, 9]), 10); y = F(r.choice([1, 2]), 10)
    one = pb * x / (pb * x + (1 - pb) * y); two = pb * x * x / (pb * x * x + (1 - pb) * y * y)
    E = [('A disease affects %s%% of people. A test is positive for %s%% of sick and %s%% of healthy people; two tests on the same person are independent given the health status. A person tests positive twice. The probability that the person is sick is…',
          'Một bệnh có tỉ lệ mắc %s%%. Xét nghiệm dương tính với %s%% người bệnh và %s%% người khỏe; hai lần xét nghiệm trên cùng một người độc lập khi biết tình trạng bệnh. Một người dương tính cả hai lần. Xác suất người đó bị bệnh là…'),
         ('%s%% of the e-mails are spam. A filter flags %s%% of spam and %s%% of normal e-mails; two different filters of this kind work independently given the type of e-mail. Both flag an e-mail. The probability that it is spam is…',
          '%s%% thư điện tử là thư rác. Một bộ lọc đánh dấu %s%% thư rác và %s%% thư thường; hai bộ lọc loại này hoạt động độc lập khi biết loại thư. Cả hai cùng đánh dấu một thư. Xác suất thư đó là thư rác là…'),
         ('A machine is faulty with probability %s%%. A sensor gives an alarm for %s%% of faulty and %s%% of good machines; two sensors work independently given the state. Both sensors alarm. The probability that the machine is faulty is…',
          'Một máy bị lỗi với xác suất %s%%. Một cảm biến báo động với %s%% máy lỗi và %s%% máy tốt; hai cảm biến hoạt động độc lập khi biết tình trạng máy. Cả hai cùng báo động. Xác suất máy bị lỗi là…')][(lv - 1) % 3]
    args = (ne(pb * 100), ne(x * 100), ne(y * 100))
    return dict(en=E[0] % args, vi=E[1] % args, opts=fo(two, [one, x * x, pb * x * x, one * one]),
                ee='\\(P=\\dfrac{%s\\cdot%s^2}{%s\\cdot%s^2+%s\\cdot%s^2}=%s\\) (after one test only \\(%s\\)).' % (pe(pb), pe(x), pe(pb), pe(x), pe(1 - pb), pe(y), frt(two), frt(one)),
                ev='\\(P=\\dfrac{%s\\cdot%s^2}{%s\\cdot%s^2+%s\\cdot%s^2}=%s\\) (sau một lần chỉ là \\(%s\\)).' % (pv(pb), pv(x), pv(pb), pv(x), pv(1 - pb), pv(y), frt(two), frt(one)))

def p19_d_prior(r, lv, ctx):
    for _ in range(300):
        x = F(r.choice([6, 7, 8, 9]), 10); y = F(r.choice([1, 2, 3]), 10); pb = F(r.choice([1, 2, 3, 4, 5]), 10)
        post = pb * x / (pb * x + (1 - pb) * y)
        if post.denominator <= 20: break
    else: raise AssertionError
    qe = V(lv, ['\\(P(A\\mid B)=%s\\), \\(P(A\\mid\\overline B)=%s\\) and \\(P(B\\mid A)=%s\\). Then \\(P(B)=\\)…', 'Knowing \\(P(B\\mid A)=%s\\), \\(P(A\\mid B)=%s\\), \\(P(A\\mid\\overline B)=%s\\), find the prior probability \\(P(B)\\).', 'Find \\(P(B)\\) if \\(P(A\\mid B)=%s\\), \\(P(A\\mid\\overline B)=%s\\), \\(P(B\\mid A)=%s\\).'])
    qv = V(lv, ['\\(P(A\\mid B)=%s\\), \\(P(A\\mid\\overline B)=%s\\) và \\(P(B\\mid A)=%s\\). Khi đó \\(P(B)=\\)…', 'Biết \\(P(B\\mid A)=%s\\), \\(P(A\\mid B)=%s\\), \\(P(A\\mid\\overline B)=%s\\), tìm xác suất tiên nghiệm \\(P(B)\\).', 'Tìm \\(P(B)\\) nếu \\(P(A\\mid B)=%s\\), \\(P(A\\mid\\overline B)=%s\\), \\(P(B\\mid A)=%s\\).'])
    fe = lambda z: frt(z) if not dec(z) else pe(z); fv = lambda z: frt(z) if not dec(z) else pv(z)
    a1 = (fe(post), pe(x), pe(y)) if lv == 2 else (pe(x), pe(y), fe(post)); a2 = (fv(post), pv(x), pv(y)) if lv == 2 else (pv(x), pv(y), fv(post))
    return dict(en=qe % a1, vi=qv % a2, opts=popt(pb, [post, post * y / x, 1 - pb, x * post, post - y]),
                ee='Put \\(p=P(B)\\): \\(\\dfrac{%s p}{%s p+%s(1-p)}=%s\\Rightarrow p=%s\\).' % (pe(x), pe(x), pe(y), fe(post), pe(pb)),
                ev='Đặt \\(p=P(B)\\): \\(\\dfrac{%s p}{%s p+%s(1-p)}=%s\\Rightarrow p=%s\\).' % (pv(x), pv(x), pv(y), fv(post), pv(pb)))

def p19_d_compare(r, lv, ctx):
    pb = F(r.choice([1, 2, 5]), 100); s1, f1 = F(r.choice([90, 95]), 100), F(r.choice([5, 10]), 100); s2, f2 = F(r.choice([80, 85]), 100), F(r.choice([1, 2]), 100)
    q1 = pb * s1 / (pb * s1 + (1 - pb) * f1); q2 = pb * s2 / (pb * s2 + (1 - pb) * f2)
    if q1 == q2: raise AssertionError
    best = 'X' if q1 > q2 else 'Y'; other = 'Y' if best == 'X' else 'X'
    S = [('Test %s, because \\(P(B\\mid+)\\) is larger for it.' % best, 'Xét nghiệm %s, vì với nó \\(P(B\\mid+)\\) lớn hơn.' % best), ('Test %s, because it gives a larger \\(P(B\\mid+)\\).' % other, 'Xét nghiệm %s, vì nó cho \\(P(B\\mid+)\\) lớn hơn.' % other),
         ('Test X, because it detects more cases with \\(B\\).', 'Xét nghiệm X, vì phát hiện được nhiều trường hợp có \\(B\\) hơn.') if best == 'Y' else ('Test Y, because it has fewer false positives in total.', 'Xét nghiệm Y, vì tổng số dương tính giả ít hơn.'), ('Both tests are equally reliable.', 'Hai xét nghiệm tin cậy như nhau.')]
    E = [('A disease affects %s%% of people (\\(B\\): "the person has the disease").', 'Một bệnh có tỉ lệ mắc %s%% (\\(B\\): "người đó mắc bệnh").'), ('%s%% of the parts in a factory are faulty (\\(B\\): "the part is faulty").', '%s%% linh kiện của một nhà máy bị lỗi (\\(B\\): "linh kiện bị lỗi").'), ('%s%% of the seeds in a batch are infected (\\(B\\): "the seed is infected").', '%s%% hạt giống trong một lô bị nhiễm bệnh (\\(B\\): "hạt bị nhiễm bệnh").')][(lv - 1) % 3]
    en = E[0] % ne(pb * 100) + ' Test X is positive for %s%% of the cases with \\(B\\) and %s%% of the cases without \\(B\\); test Y for %s%% and %s%%. A case tests positive. With which test is the result more trustworthy?' % (ne(s1 * 100), ne(f1 * 100), ne(s2 * 100), ne(f2 * 100))
    vi = E[1] % nv(pb * 100) + ' Xét nghiệm X dương tính với %s%% trường hợp có \\(B\\) và %s%% trường hợp không có \\(B\\); xét nghiệm Y lần lượt %s%% và %s%%. Một trường hợp cho kết quả dương tính. Với xét nghiệm nào kết quả đáng tin hơn?' % (nv(s1 * 100), nv(f1 * 100), nv(s2 * 100), nv(f2 * 100))
    return dict(en=en, vi=vi, opts=[tt(*z) for z in S], ee='X: \\(P(B\\mid+)=%s\\approx%s\\); Y: \\(%s\\approx%s\\).' % (frt(q1), ne(F(round(float(q1) * 100), 100)), frt(q2), ne(F(round(float(q2) * 100), 100))),
                ev='X: \\(P(B\\mid+)=%s\\approx%s\\); Y: \\(%s\\approx%s\\).' % (frt(q1), nv(F(round(float(q1) * 100), 100)), frt(q2), nv(F(round(float(q2) * 100), 100))))

def p19_d_seeds(r, lv, ctx):
    a = F(r.choice([40, 50, 60, 70]), 100); g1, g2 = F(r.choice([80, 85, 90]), 100), F(r.choice([60, 70, 75]), 100)
    bad = a * (1 - g1) + (1 - a) * (1 - g2); good = a * (1 - g1) / bad
    E = [('A farm buys %s%% of its rice seeds from supplier X and the rest from supplier Y. %s%% of X seeds and %s%% of Y seeds germinate. A seed does not germinate. The probability that it came from X is…', 'Một hợp tác xã mua %s%% hạt giống lúa của cơ sở X, còn lại của cơ sở Y. Tỉ lệ nảy mầm của hạt X là %s%%, của hạt Y là %s%%. Một hạt không nảy mầm. Xác suất hạt đó của cơ sở X là…'),
         ('%s%% of the chicken eggs in an incubator come from farm X, the rest from farm Y. Hatching rates are %s%% (X) and %s%% (Y). An egg does not hatch. Find the probability that it came from X.', '%s%% số trứng gà trong lò ấp của trại X, còn lại của trại Y. Tỉ lệ nở là %s%% (X) và %s%% (Y). Một quả trứng không nở. Tính xác suất quả trứng đó của trại X.'),
         ('A garden plants %s%% of its seedlings from nursery X and the rest from nursery Y. %s%% of X and %s%% of Y seedlings survive. A seedling dies. The probability that it came from X is…', 'Một vườn trồng %s%% cây giống của vườn ươm X, còn lại của vườn ươm Y. Tỉ lệ sống của cây X là %s%%, cây Y là %s%%. Một cây bị chết. Xác suất cây đó của vườn ươm X là…')][(lv - 1) % 3]
    args = (ne(a * 100), ne(g1 * 100), ne(g2 * 100))
    E = (E[0].replace(' is…', ' (see the tree diagram) is…').replace('Find the probability', 'Using the tree diagram, find the probability'), E[1].replace(' là…', ' (xem sơ đồ hình cây) là…').replace('Tính xác suất', 'Dùng sơ đồ hình cây, tính xác suất'))
    return dict(en=E[0] % args, vi=E[1] % args, opts=fo(good, [a, a * g1 / (a * g1 + (1 - a) * g2), 1 - good, a * (1 - g1)]), fig=TREE(a, g1, g2, labels=('X', 'Y', 'G', '\\overline{G}')),
                ee='\\(P(\\overline G)=%s\\cdot%s+%s\\cdot%s=%s\\); \\(P(X\\mid\\overline G)=\\dfrac{%s}{%s}=%s\\).' % (pe(a), pe(1 - g1), pe(1 - a), pe(1 - g2), pe(bad), pe(a * (1 - g1)), pe(bad), frt(good)),
                ev='\\(P(\\overline G)=%s\\cdot%s+%s\\cdot%s=%s\\); \\(P(X\\mid\\overline G)=\\dfrac{%s}{%s}=%s\\).' % (pv(a), pv(1 - g1), pv(1 - a), pv(1 - g2), pv(bad), pv(a * (1 - g1)), pv(bad), frt(good)))

def p19_d_expected(r, lv, ctx):
    N = r.choice([1000, 2000, 5000, 10000]); pb = F(r.choice([1, 2, 4, 5]), 100); x = F(r.choice([90, 95]), 100); y = F(r.choice([2, 4, 5]), 100)
    pos = N * (pb * x + (1 - pb) * y); sickpos = N * pb * x
    if pos.denominator != 1 or sickpos.denominator != 1: raise AssertionError
    pos, sickpos = int(pos), int(sickpos); k = (lv - 1) % 3
    if k == 2: good, bads = sickpos, [pos, int(N * pb), pos - sickpos]
    else: good, bads = pos, [sickpos, int(N * pb), int(N * (1 - pb) * y)]
    qe = ['In a town of %d people, %s%% have a disease. A test is positive for %s%% of sick and %s%% of healthy people. If everyone is tested, about how many positive results are expected?',
          'A school screens %d students for a condition affecting %s%% of them; the screening is positive for %s%% of affected and %s%% of unaffected students. About how many students will be screened positive?',
          'Among %d people, %s%% are sick; the test is positive for %s%% of the sick and %s%% of the healthy. About how many people are sick AND test positive?'][k]
    qv = ['Một thị trấn có %d người, %s%% mắc một bệnh. Xét nghiệm dương tính với %s%% người bệnh và %s%% người khỏe. Nếu xét nghiệm tất cả, có khoảng bao nhiêu kết quả dương tính?',
          'Một trường sàng lọc %d học sinh về một tình trạng có ở %s%% học sinh; kết quả dương tính với %s%% em có và %s%% em không có tình trạng đó. Khoảng bao nhiêu học sinh có kết quả dương tính?',
          'Trong %d người có %s%% người bệnh; xét nghiệm dương tính với %s%% người bệnh và %s%% người khỏe. Có khoảng bao nhiêu người vừa bị bệnh vừa dương tính?'][k]
    return dict(en=qe % (N, ne(pb * 100), ne(x * 100), ne(y * 100)) + ' (Tree diagram: \\(B\\) = sick, \\(A\\) = positive.)', vi=qv % (N, nv(pb * 100), nv(x * 100), nv(y * 100)) + ' (Sơ đồ hình cây: \\(B\\) – bị bệnh, \\(A\\) – dương tính.)',
                opts=nopts(r, good, bads, step=10), fig=TREE(pb, x, y),
                ee='Sick and positive: \\(%d\\cdot%s\\cdot%s=%d\\); healthy and positive: \\(%d\\); total positive \\(%d\\).' % (N, pe(pb), pe(x), sickpos, pos - sickpos, pos),
                ev='Bệnh và dương tính: \\(%d\\cdot%s\\cdot%s=%d\\); khỏe mà dương tính: \\(%d\\); tổng số dương tính \\(%d\\).' % (N, pv(pb), pv(x), sickpos, pos - sickpos, pos))

SYS = [(('\\(B_1\\): "the die shows 1 or 2", \\(B_2\\): "3 or 4", \\(B_3\\): "5 or 6".', '\\(B_1\\): "xúc xắc ra 1 hoặc 2", \\(B_2\\): "ra 3 hoặc 4", \\(B_3\\): "ra 5 hoặc 6".'),
         (('\\(B_1\\): "an even number", \\(B_2\\): "a number greater than 3".', '\\(B_1\\): "ra số chẵn", \\(B_2\\): "ra số lớn hơn 3".'), ('\\(B_1\\): "1 or 2", \\(B_2\\): "4 or 5".', '\\(B_1\\): "ra 1 hoặc 2", \\(B_2\\): "ra 4 hoặc 5".'), ('\\(B_1\\): "an odd number", \\(B_2\\): "a number less than 4".', '\\(B_1\\): "ra số lẻ", \\(B_2\\): "ra số nhỏ hơn 4".'))),
       (('\\(B_1\\): "the student is in grade 10", \\(B_2\\): "grade 11", \\(B_3\\): "grade 12" (a high school student is chosen).', '\\(B_1\\): "học sinh lớp 10", \\(B_2\\): "lớp 11", \\(B_3\\): "lớp 12" (chọn một học sinh THPT).'),
         (('\\(B_1\\): "the student is a girl", \\(B_2\\): "the student is in grade 10".', '\\(B_1\\): "học sinh là nữ", \\(B_2\\): "học sinh lớp 10".'), ('\\(B_1\\): "grade 10", \\(B_2\\): "grade 11".', '\\(B_1\\): "lớp 10", \\(B_2\\): "lớp 11".'), ('\\(B_1\\): "the student likes Math", \\(B_2\\): "the student likes Physics".', '\\(B_1\\): "học sinh thích Toán", \\(B_2\\): "học sinh thích Vật lí".'))),
       (('\\(B\\): "it rains tomorrow", \\(\\overline B\\): "it does not rain tomorrow".', '\\(B\\): "ngày mai mưa", \\(\\overline B\\): "ngày mai không mưa".'),
         (('\\(B_1\\): "it rains tomorrow", \\(B_2\\): "it is windy tomorrow".', '\\(B_1\\): "ngày mai mưa", \\(B_2\\): "ngày mai có gió".'), ('\\(B_1\\): "it rains tomorrow", \\(B_2\\): "it is sunny all day tomorrow".', '\\(B_1\\): "ngày mai mưa", \\(B_2\\): "ngày mai nắng cả ngày".'), ('\\(B_1\\): "the temperature is above 30°C", \\(B_2\\): "it rains".', '\\(B_1\\): "nhiệt độ trên 30°C", \\(B_2\\): "trời mưa".')))]
def p19_d_system(r, lv, ctx):
    good, bads = SYS[(lv - 1) % 3]
    qe = V(lv, ['A die is rolled. Which family of events forms a complete system (exclusive and covering all outcomes)?', 'Which of the following is a complete system of events?', 'For the law of total probability we need a complete system. Which one is it?'])
    qv = V(lv, ['Gieo một con xúc xắc. Nhóm biến cố nào là một hệ đầy đủ (xung khắc từng đôi và phủ mọi kết quả)?', 'Nhóm biến cố nào sau đây là một hệ đầy đủ?', 'Công thức xác suất toàn phần cần một hệ đầy đủ các biến cố. Đó là nhóm nào?'])
    return dict(en=qe, vi=qv, opts=[tt(*good)] + [tt(*b) for b in bads], ee='Only this family is pairwise exclusive and its events cover all cases.', ev='Chỉ nhóm này xung khắc từng đôi và các biến cố phủ hết mọi trường hợp.')

def p19_d_argmax(r, lv, ctx):
    for _ in range(300):
        pr = r.choice([(F(1, 2), F(1, 3), F(1, 6)), (F(1, 3), F(1, 3), F(1, 3)), (F(1, 4), F(1, 4), F(1, 2)), (F(1, 5), F(2, 5), F(2, 5))])
        balls = [(r.randint(1, 6), r.randint(1, 6)) for _ in range(3)]
        w = [p * F(a, a + b) for p, (a, b) in zip(pr, balls)]
        if len(set(w)) == 3: break
    k = max(range(3), key=lambda i: w[i]); tot = sum(w)
    desc_e = '; '.join('box %d (chosen with probability \\(%s\\)) has %d red and %d white balls' % (i + 1, frt(pr[i]), a, b) for i, (a, b) in enumerate(balls))
    desc_v = '; '.join('hộp %d (được chọn với xác suất \\(%s\\)) có %d bi đỏ, %d bi trắng' % (i + 1, frt(pr[i]), a, b) for i, (a, b) in enumerate(balls))
    qe = V(lv, ['A box is chosen, then one ball is drawn: %s. The ball is red. From which box did it most probably come?', 'Three boxes: %s. A red ball was drawn. Which box is the most likely source?', 'Given that the ball drawn is red (%s), the box with the largest posterior probability is…'])
    qv = V(lv, ['Chọn một hộp rồi lấy một bi: %s. Bi lấy được màu đỏ. Bi đó nhiều khả năng nhất là của hộp nào?', 'Ba hộp: %s. Lấy được một bi đỏ. Hộp nào có khả năng cao nhất?', 'Biết bi lấy được màu đỏ (%s), hộp có xác suất hậu nghiệm lớn nhất là…'])
    opts = [tt('Box %d' % (k + 1), 'Hộp %d' % (k + 1))] + [tt('Box %d' % (i + 1), 'Hộp %d' % (i + 1)) for i in range(3) if i != k] + [tt('All boxes are equally likely', 'Ba hộp có khả năng như nhau')]
    post = [x / tot for x in w]
    return dict(en=qe % desc_e, vi=qv % desc_v, opts=opts, ee='Posterior probabilities: %s.' % ', '.join('\\(%s\\)' % frt(p) for p in post), ev='Các xác suất hậu nghiệm: %s.' % ', '.join('\\(%s\\)' % frt(p) for p in post))

B19 = dict(A=[p19_post3, p19_move, p19_tree_post], B=[p19_tf_update], C=[p19_sh_branch],
           D=[p19_d_error, p19_d_twotests, p19_d_prior, p19_d_compare, p19_d_seeds, p19_d_expected, p19_d_system, p19_d_argmax])
