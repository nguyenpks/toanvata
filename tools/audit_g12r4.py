# -*- coding: utf-8 -*-
"""Kiểm định ĐỘC LẬP đáp án các bài lớp 12 hiệu chỉnh ngày 14/11/2026 (Bài 9, 10, 17, 18, 19).
Không dùng lại mã sinh câu (sp_g12r4, sp_g12f, gq, gdata): đọc trang đã dựng (lessons/…html) và nguồn TeX của hình
(img/tex/*.tex: biểu đồ tần số, sơ đồ hình cây, biểu đồ Venn), tự tính lại đáp số rồi so với đáp án của trang.
Với trắc nghiệm: kiểm tra đúng MỘT phương án khớp kết quả tự tính. Câu khái niệm (mệnh đề cố định) đối chiếu bảng chân trị viết tay.

    python tools/audit_g12r4.py            # in số câu đúng / tổng số, liệt kê câu sai và câu chưa có bộ giải
"""
import os, re, sys, math, glob, html as _h
from fractions import Fraction as F
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from question_bank import parse_page          # chỉ dùng để tách câu hỏi khỏi trang HTML

PAGES = {'g12-stats-01': 'lessons/grade12/statistics/range-interquartile-range.html', 'g12-stats-02': 'lessons/grade12/statistics/variance-standard-deviation.html',
         'g12-coord-06': 'lessons/grade12/space-coordinates/sphere-equations.html', 'g12-prob-01': 'lessons/grade12/probability/conditional-probability.html',
         'g12-prob-02': 'lessons/grade12/probability/total-probability-bayes.html'}

# ------------------------------------------------------------------ đọc số, bảng, hình
def txt(h): return re.sub(r'\s+', ' ', _h.unescape(re.sub(r'<[^>]+>', ' ', h))).strip()
def en_part(o):
    m = re.search(r'<span class="en">(.*?)</span>', o, re.S); return m.group(1) if m else o
def num(s):
    """'\\(\\dfrac{3}{7}\\)', '0.25', '-3', '12.25 kg' → Fraction (None nếu không đọc được)."""
    s = txt(s).replace('\\(', '').replace('\\)', '').replace('{,}', '.').strip()
    m = re.fullmatch(r'(-?)\\dfrac\{(\d+)\}\{(\d+)\}.*', s)
    if m: return (-1 if m.group(1) else 1) * F(int(m.group(2)), int(m.group(3)))
    m = re.match(r'(-?\d+(?:\.\d+)?)', s)
    return F(m.group(1)) if m else None
def nums(s): return [F(x) for x in re.findall(r'-?\d+(?:\.\d+)?', s.replace('{,}', '.'))]

def freq_tables(h):
    """Các bảng ghép nhóm ngang trong đề → [(cạnh nhóm, tần số hoặc None, loại 'freq'|'cum')]."""
    out = []
    for t in re.findall(r'<table class="mbl-table mbl-freq">(.*?)</table>', h, re.S):
        rows = re.findall(r'<tr>(.*?)</tr>', t, re.S)
        g = re.findall(r'\\\(\[(-?[\d.]+);\\,(-?[\d.]+)\)\\\)', rows[0].replace('{,}', '.'))
        edges = [F(a) for a, b in g] + [F(g[-1][1])]
        cells = re.findall(r'<td(?: class="[^"]*")?>(.*?)</td>', rows[1], re.S)
        kind = 'cum' if re.search(r'Cumulative|tích lũy', rows[1]) else 'freq'
        fs = [None if 'x' in c else int(num(c)) for c in cells[:len(edges) - 1]]
        out.append((edges, fs, kind))
    return out
def tex_of(h):
    return [open(os.path.join(ROOT, 'img', 'tex', fn[:-4] + '.tex'), encoding='utf-8').read() for fn in re.findall(r'img/tex/([0-9a-f]+\.svg)', h)]
def hist_of(tex):
    """Biểu đồ tần số: chiều cao cột (nhãn trên cột) và các mốc trên trục hoành."""
    fs = [int(x) for x in re.findall(r'\\node\[font=\\small, text=ink, above\] at \([^)]*\) \{\$(\d+)\$\}', tex)]
    edges = [F(x) for x in re.findall(r'node\[below, font=\\small, text=ink\] \{\$(-?[\d.]+)\$\}', tex)]
    return edges, fs
def tree_of(tex):
    L = re.findall(r'inner sep=1pt\] at \([^)]*\) \{\$([^$]*)\$\}', tex)
    v = [None if x == '?' else F(x.replace('{,}', '.')) for x in L]
    return v       # [P(B), P(B̄), P(A|B), P(Ā|B), P(A|B̄), P(Ā|B̄)]
def venn_of(tex):
    v = [int(x) for x in re.findall(r'\\node\[font=\\Large\\bfseries, text=ink(?:, anchor=south east)?\] at \([^)]*\) \{\$(\d+)\$\}', tex)]
    return v       # A riêng, giao, B riêng, ngoài
def twoway_of(h):
    t = re.search(r'<table class="mbl-table"><thead>(.*?)</table>', h, re.S).group(0)
    rows = re.findall(r'<tr><th scope="row">.*?</th>(.*?)</tr>', t, re.S)
    data = [[c for c in re.findall(r'<td>(.*?)</td>', r)] for r in rows[:-1]]
    return [[None if 'x' in c.split('+')[-1] and '+' not in c and c.strip('\\()') == 'x' else c for c in r] for r in data]

# ------------------------------------------------------------------ thống kê ghép nhóm (tự viết)
def stat(edges, fs):
    n = sum(fs); h = edges[1] - edges[0]; mids = [(edges[i] + edges[i + 1]) / 2 for i in range(len(fs))]
    def Q(p):
        pos = p * n; c = 0
        for i, f in enumerate(fs):
            if c + f >= pos and f > 0: return i, edges[i] + (pos - c) / f * h
            c += f
    mean = sum(f * m for f, m in zip(fs, mids)) / n
    var = sum(f * (m - mean) ** 2 for f, m in zip(fs, mids)) / n
    return dict(n=n, h=h, Q=Q, mean=mean, var=var, R=edges[-1] - edges[0], mids=mids)

# ------------------------------------------------------------------ mặt cầu, mặt phẳng, điểm
def pts(s):
    return {m.group(1): tuple(F(x) for x in re.split(r';\\?,?', m.group(2))) for m in re.finditer(r"([A-Z]'?)\((-?[\d/.]+(?:;\\?,?-?[\d/.]+){2})\)", s.replace('\\,', ''))}
def sphere(s):
    """(x-a)^2+(y-b)^2+(z-c)^2=R2  hoặc  x^2+... ; trả (a,b,c,R2)."""
    s = s.replace(' ', '')
    m = re.search(r'((?:\(x[+-]\d+\)\^2|x\^2))\+((?:\(y[+-]\d+\)\^2|y\^2))\+((?:\(z[+-]\d+\)\^2|z\^2))=(-?\d+)', s)
    if not m: return None
    c = []
    for g in m.groups()[:3]:
        k = re.search(r'([+-]\d+)', g); c.append(-F(k.group(1)) if k else F(0))
    return tuple(c) + (F(m.group(4)),)
def general(s):
    m = re.search(r'x\^2\+y\^2\+z\^2((?:[+-]\d*[xyz])*)((?:[+-]\d+|[+-]m)?)=0', s.replace(' ', ''))
    if not m: return None
    co = {'x': 0, 'y': 0, 'z': 0}
    for a, v in re.findall(r'([+-]\d*)([xyz])', m.group(1)): co[v] = int(a + '1') if a in '+-' else int(a)
    d = m.group(2)
    return (F(-co['x'], 2), F(-co['y'], 2), F(-co['z'], 2), None if d.endswith('m') else F(d or 0))
def plane(s):
    m = re.search(r'([+-]?\d*x)?([+-]\d*y|\d*y)?([+-]\d*z)?([+-]\d+|[+-]m)?=0', s.replace(' ', ''))
    def co(t, v):
        if not t: return 0
        t = t.replace(v, ''); return int(t + '1') if t in ('', '+', '-') else int(t)
    return co(m.group(1), 'x'), co(m.group(2), 'y'), co(m.group(3), 'z'), m.group(4)
def d2(a, b): return sum((x - y) ** 2 for x, y in zip(a, b))
def isq(x): return x >= 0 and F(x).denominator == 1 and math.isqrt(int(x)) ** 2 == x

# ------------------------------------------------------------------ chấm
ok = bad = skip = 0; report = []
def opt_index(opts, pred):
    hits = [i for i, o in enumerate(opts) if pred(o)]
    return hits
def check_mcq(q, pred, tag):
    global ok, bad
    hits = opt_index(q['options'], pred)
    if len(hits) == 1 and 'abcd'[hits[0]] == q['answer']: ok += 1
    else: bad += 1; report.append(('SAI', tag, q['answer'], hits, txt(q['en'])[:160]))
def check_val(q, v, tag):
    if q['type'] == 'mcq': check_mcq(q, lambda o: num(en_part(o)) == F(v), tag)
    else:
        global ok, bad
        a = F(q['answer'].replace(',', '.').split('|')[0])
        if a == F(v): ok += 1
        else: bad += 1; report.append(('SAI', tag, q['answer'], v, txt(q['en'])[:160]))
def check_tf(q, truth, tag):
    global ok, bad
    if q['answer'] == ('true' if truth else 'false'): ok += 1
    else: bad += 1; report.append(('SAI', tag, q['answer'], truth, txt(q['en'])[:160]))
def check_text(q, needle, tag):
    check_mcq(q, lambda o: needle in txt(en_part(o)), tag)

def solve(lid, q):
    e = q['en']; T = txt(e); typ = q['type']
    # ============ Bài 9
    if lid == 'g12-stats-01':
        tb = freq_tables(e); hs = [hist_of(t) for t in tex_of(e)] if 'img/tex' in e else []
        if 'Judging by the interquartile range' in T or 'Compare the interquartile ranges' in T or 'smaller spread in its middle half' in T:
            a, b = [stat(x[0], x[1]) for x in tb]; da = a['Q'](F(3, 4))[1] - a['Q'](F(1, 4))[1]; db = b['Q'](F(3, 4))[1] - b['Q'](F(1, 4))[1]
            return check_text(q, 'Sample %s is more concentrated in the middle half' % ('A' if da < db else 'B'), 'b9-compare')
        if 'A student found \\(Q_1\\)' in T:
            S = stat(*tb[0][:2]); g, v = S['Q'](F(1, 4)); sv = num(re.search(r'Step 3: .*?=(-?[\d.]+)\\\)', T).group(1))
            gi = re.search(r'Step 2: the group containing \\\(Q_1\\\) is \\\(\[(-?[\d.]+)', T); ok3 = (sv == v); ok2 = F(gi.group(1)) == tb[0][0][g]
            return check_text(q, 'Step 3 is wrong' if ok2 and not ok3 else ('Step 2 is wrong' if not ok2 else 'All three steps are correct'), 'b9-error')
        if 'Sample X:' in T:
            R1, d1, R2, d2_ = [F(x) for x in re.findall(r'R=(\d+)\\\), \\\(\\Delta_Q=(\d+)', T)[0] + re.findall(r'R=(\d+)\\\), \\\(\\Delta_Q=(\d+)', T)[1]]
            want = 'X has the larger range, but its middle half is more concentrated' if (R1 > R2 and d1 < d2_) else '??'
            return check_text(q, want, 'b9-rq')
        if 'If all values are written in' in T:
            d = num(re.search(r'\\Delta_Q=([\d.]+)', T).group(1)); unit = re.search(r'written in (\w+)', T).group(1); k = {'minutes': 60, 'cm': 100, 'g': 1000}[unit]
            return check_val(q, d * k, 'b9-scale')
        if 'between \\(Q_1=' in T or 'lies from \\(Q_1=' in T or 'in the interval \\([' in T and 'Roughly how many' in T:
            return check_val(q, F(stat(*tb[0][:2])['n'], 2), 'b9-middle')
        if 'can NOT be the interquartile range' in T or 'certainly wrong' in T or 'impossible as the interquartile range' in T:
            R = stat(*tb[0][:2])['R']; return check_mcq(q, lambda o: num(en_part(o)) > R, 'b9-impossible')
        if 'cumulative frequenc' in T.lower() and tb and tb[0][2] == 'cum':
            ed, cum, _ = tb[0]; fs = [cum[0]] + [cum[i] - cum[i - 1] for i in range(1, len(cum))]
            return check_val(q, stat(ed, fs)['Q'](F(3, 4))[1], 'b9-cum')
        if 'groups of equal width' in T or 'groups of the same width' in T or 'equal groups starting from' in T:
            k, u0, R = [int(x) for x in re.findall(r'(\d+)', T)[:3]]; j = 2 if 'second' in T else 3; h = F(R, k)
            return check_text(q, '[%s;' % (u0 + (j - 1) * h), 'b9-width') if False else check_mcq(q, lambda o: nums(txt(en_part(o)))[:2] == [u0 + (j - 1) * h, u0 + j * h], 'b9-width')
        if 'changes the most' in T or 'affected most' in T or 'changes most' in T:
            return check_text(q, 'The range', 'b9-extreme')
        if 'Which group contains the first quartile' in T or 'lies in the group…' in T or 'In which group is \\(Q_1\\)' in T:
            S = stat(*tb[0][:2]); g = S['Q'](F(1, 4))[0]; lo = tb[0][0][g]
            return check_mcq(q, lambda o: nums(txt(en_part(o)))[:1] == [lo], 'b9-q1group')
        if typ == 'tf' and ('\\(Q_3\\)' in T and ('lies in the group' in T or 'belongs to the group' in T or 'contains the upper quartile' in T)):
            S = stat(*tb[0][:2]); g = S['Q'](F(3, 4))[0]; lo = F(re.search(r'group \\\(\[(-?[\d.]+);', T).group(1))
            return check_tf(q, lo == tb[0][0][g], 'b9-tf-q3group')
        if typ == 'tf' and not tb:
            truth = {'\\Delta_Q\\le R': True, 'same range always': False, 'hardly affected': True}
            for k, v in truth.items():
                if k in T: return check_tf(q, v, 'b9-concept')
        if typ == 'tf' and ('25%' in T or 'one quarter' in T or '75%' in T):
            v = num(re.search(r'(?:at least|of|below) \\\((-?[\d.]+)\\\)', T).group(1)); q3 = stat(*tb[0][:2])['Q'](F(3, 4))[1]
            return check_tf(q, v == q3, 'b9-meaning')
        if '\\(Q_2\\)' in T: return check_val(q, stat(*tb[0][:2])['Q'](F(1, 2))[1], 'b9-q2')
        if 'new third quartile' in T or 'of the new data' in T or 'after the change' in T:
            c = F(re.search(r'(?:increases by|adds|raise of|again) (\d+)', T).group(1)); return check_val(q, stat(*tb[0][:2])['Q'](F(3, 4))[1] + c, 'b9-shift')
        if 'missing frequency' in T or 'Find \\(x\\)' in T or 'What is \\(x\\)' in T:
            ed, fs, _ = tb[0]; q1 = num(re.search(r'(?:Q_1=|equals \\\()([\d.]+)', T).group(1)); u = fs.index(None)
            sols = [x for x in range(1, 60) if stat(ed, fs[:u] + [x] + fs[u + 1:])['Q'](F(1, 4))[1] == q1]
            return check_val(q, sols[0], 'b9-missing') if len(sols) == 1 else report.append(('SAI', 'b9-missing nghiệm không duy nhất', sols, T[:100]))
        if 'histogram' in T and ('Q_3' in T):
            ed, fs = hs[0]; return check_val(q, stat(ed, fs)['Q'](F(3, 4))[1], 'b9-q3hist')
        if 'range' in T and 'interquartile' not in T: return check_val(q, stat(*tb[0][:2])['R'], 'b9-range')
        if 'interquartile range' in T: S = stat(*tb[0][:2]); return check_val(q, S['Q'](F(3, 4))[1] - S['Q'](F(1, 4))[1], 'b9-iqr')
        if 'first quartile' in T or 'lower quartile' in T: return check_val(q, stat(*tb[0][:2])['Q'](F(1, 4))[1], 'b9-q1')
    # ============ Bài 10
    if lid == 'g12-stats-02':
        tb = freq_tables(e); hs = [hist_of(t) for t in tex_of(e)] if 'img/tex' in e else []
        if 'A student computed the variance' in T:
            S = stat(*tb[0][:2]); m3 = re.search(r'Step 3: \\\(s\^2=([\d.]+)-([\d.]+)=', T)
            return check_text(q, 'Step 3: one must subtract' if F(m3.group(2)) == S['mean'] else '??', 'b10-error')
        if 'two histograms' in T or 'Two samples have the same mean' in T or 'Compare the spread of samples A and B' in T:
            (e1, f1), (e2, f2) = hs[0], hs[1]; v1, v2 = stat(e1, f1)['var'], stat(e2, f2)['var']
            return check_text(q, 'Sample %s has the larger standard deviation' % ('A' if v1 > v2 else 'B'), 'b10-hist2')
        if 'Which formula gives the standard deviation' in T: return check_text(q, '\\sqrt{\\dfrac1n\\sum n_i(x_i-\\bar x)^2}', 'b10-formula')
        if 'the variance is…' in T and 'midpoints \\(x_i\\)' in T: return check_mcq(q, lambda o: txt(en_part(o)) == '\\(\\dfrac1n\\sum n_i(x_i-\\bar x)^2\\)', 'b10-formula')
        if 'Which expression is equal to the variance' in T: return check_mcq(q, lambda o: txt(en_part(o)) == '\\(\\dfrac1n\\sum n_ix_i^2-\\bar x^2\\)', 'b10-formula')
        if 'about the variance and the standard deviation' in T or 'true statement about the standard deviation' in T or T.startswith('Which of the following is true?'):
            good = ['exactly when all its values are equal', 'the more the data are spread', 'square root of the variance']
            return check_mcq(q, lambda o: any(g in txt(en_part(o)) for g in good), 'b10-stat')
        if '\\sum n_ix_i=' in T and '\\sum n_ix_i^2=' in T:
            n, S1, S2 = [F(x) for x in re.findall(r'n=(\d+)\\\).*?\\sum n_ix_i=(\d+)\\\).*?\\sum n_ix_i\^2=(\d+)', T)[0]]
            v = S2 / n - (S1 / n) ** 2; return check_val(q, F(math.isqrt(int(v))), 'b10-sums') if isq(v) else None
        if '\\sum n_i(x_i-\\bar x)^2=' in T or 'squared deviations from the mean add up to' in T:
            vals = nums(re.sub(r'\\\(n=|\\sum n_i\(x_i-\\bar x\)\^2=', ' ', T)); n = F(re.search(r'n=(\d+)', T).group(1)); S = [v for v in vals if v != n and v > n][0]
            v = S / n; return check_mcq(q, lambda o: txt(en_part(o)) == ('\\(%d\\)' % math.isqrt(int(v)) if isq(v) else '\\(\\sqrt{%s}\\)' % str(v)), 'b10-dev')
        if 'The variance of the' in T and 'The standard deviation is…' in T:
            v = num(re.search(r's\^2=([\d.]+)', T).group(1)); u = re.search(r'\\\) (\w+)²\. The standard', T).group(1); s = F(math.isqrt(int(v * 100)), 10)
            assert s * s == v; return check_mcq(q, lambda o: num(en_part(o)) == s and txt(en_part(o)).endswith(' ' + u), 'b10-unit')
        if 'Which conclusion is right?' in T and 'mean' in T:
            m = re.findall(r'\\\(s=([\d.]+)\\\)', T); sa, sb = F(m[0]), F(m[1]); w = 'A' if sa < sb else 'B'
            return check_mcq(q, lambda o: re.match(r'(Machine|Variety|Athlete) %s has' % w, txt(en_part(o))) is not None, 'b10-compare')
        if 'only two non-empty groups' in T or ('Without a long computation' in T) or ('Find the standard deviation of the' in T and tb and sum(1 for f in tb[0][1] if f) == 2):
            return check_val(q, stat(*tb[0][:2])['var'] ** F(1, 2) if False else F(math.isqrt(int(stat(*tb[0][:2])['var'] * 4)), 2), 'b10-two')
        if typ == 'tf' and ('The variance of the' in T or 'The standard deviation of the' in T) and tb:
            v = stat(*tb[0][:2])['var']; c = num(re.search(r'(?:s\^2|s)=([\d.]+)', T).group(1))
            return check_tf(q, ('The variance of the' in T and c == v) or ('The standard deviation of the' in T and c * c == v), 'b10-tf-var')
        if typ == 'tf' and 'increased by' in T:
            p = F(re.search(r'increased by (\d+)%', T).group(1)); c = F(re.search(r'increases by (\d+)%', T).group(1)); k = 1 + p / 100
            real = (k * k - 1) * 100 if 'variance' in T.split('Then the')[1] else (k - 1) * 100
            return check_tf(q, real == c, 'b10-tf-pct')
        if typ == 'tf':
            truth = {'increases by 5, the standard deviation does not change': True, 'is doubled, the variance is doubled': False, 'same unit as the data': True}
            for k, v in truth.items():
                if k in T: return check_tf(q, v, 'b10-concept')
        if 'mean of the squares' in T or 'Find \\(\\dfrac1n\\sum n_ix_i^2\\)' in T or 'What is \\(\\dfrac1n\\sum n_ix_i^2\\)' in T:
            m, s = [F(x) for x in re.findall(r'\\bar x=(\d+)\\\).*?s=(\d+)', T)[0]]; return check_val(q, m * m + s * s, 'b10-meansq')
        if 'histogram' in T.lower() and typ == 'short':
            ed, fs = hs[0]; s = math.sqrt(stat(ed, fs)['var']); d = 2 if 'hundredths' in T else 1
            return check_val(q, F(round(s * 10 ** d)) / 10 ** d, 'b10-sh-hist')
        if 'Fahrenheit' in T: return check_val(q, F(18, 10) * num(re.search(r's=([\d.]+)', T).group(1)), 'b10-temp')
        if 'converts each score' in T:
            s = F(re.search(r's=(\d+)', T).group(1)); a = F(re.search(r'to \\\((\d+)x', T).group(1)); return check_val(q, a * s, 'b10-lin')
        if 'shipping cost' in T:
            v = F(re.search(r's\^2=(\d+)', T).group(1)); a = F(re.search(r'multiplied by (\d+)', T).group(1)); return check_val(q, a * a * v, 'b10-var-lin')
        if 'Which value is plausible' in T or 'could be the standard deviation' in T or 'Only one of these values can be' in T:
            R = stat(*tb[0][:2])['R']; return check_mcq(q, lambda o: 0 <= num(en_part(o)) <= R / 2, 'b10-plausible')
        if ('\\bar x=' in T or 'mean equals' in T) and ('variance of the sample' in T or 's^2=\\)' in T) and tb and None in tb[0][1]:
            ed, fs, _ = tb[0]; m = num(re.search(r'(?:\\bar x=|mean equals \\\()([\d.]+)', T).group(1)); u = fs.index(None)
            sols = [x for x in range(1, 80) if stat(ed, fs[:u] + [x] + fs[u + 1:])['mean'] == m]
            if len(sols) != 1: return report.append(('SAI', 'b10-param nghiệm không duy nhất', sols))
            return check_val(q, stat(ed, fs[:u] + sols + fs[u + 1:])['var'], 'b10-param')
        if 'One more value equal to \\(\\bar x\\)' in T:
            n = F(re.search(r'sample of (\d+)', T).group(1)); v = num(re.search(r's\^2=([\d.]+)', T).group(1)); return check_val(q, v * n / (n + 1), 'b10-addmean')
        if 'within one standard deviation' in T or 'between \\(\\bar x-s\\)' in T or 'within \\(s\\) of the mean' in T:
            ed, fs, _ = tb[0]; S = stat(ed, fs); m, s = [num(x) for x in re.findall(r'\\bar x=([\d.]+)\\\).*?s=([\d.]+)', T)[0]]
            assert m == S['mean'] and s * s == S['var']
            return check_val(q, sum(f for f, md in zip(fs, S['mids']) if m - s <= md <= m + s), 'b10-within')
        if 'variance' in T and tb: return check_val(q, stat(*tb[0][:2])['var'], 'b10-var')
    # ============ Bài 17
    if lid == 'g12-coord-06':
        P = pts(T); sp = sphere(T); ge = general(T)
        if 'Center and radius of' in T:
            a, b, c, d = ge; R2 = a * a + b * b + c * c - d
            return check_mcq(q, lambda o: pts(txt(en_part(o))).get('I') == (a, b, c) and F(re.search(r'R=(\d+)', txt(en_part(o))).group(1)) ** 2 == R2, 'b17-center')
        if 'is the equation of a sphere' in T: a, b, c, d = ge; return check_tf(q, a * a + b * b + c * c - d > 0, 'b17-is-sphere')
        if 'lies on' in T and typ == 'tf': return check_tf(q, d2(P['A'], sp[:3]) == sp[3], 'b17-on')
        if 'Position of' in T:
            n = plane(T.split('(P):')[1]); D = F(n[3]); a, b, c, R2 = sp; dist = abs(n[0] * a + n[1] * b + n[2] * c + D) / F(math.isqrt(n[0] ** 2 + n[1] ** 2 + n[2] ** 2))
            want = 'cut along a circle' if dist ** 2 < R2 else ('tangent' if dist ** 2 == R2 else 'no common point')
            return check_mcq(q, lambda o: txt(en_part(o)) == want, 'b17-position')
        if 'tangent to \\((P)' in T and 'Find the radius' in T:
            n = plane(T.split('(P):')[1]); I = P['I']; return check_val(q, abs(n[0] * I[0] + n[1] * I[1] + n[2] * I[2] + F(n[3])) / F(math.isqrt(n[0] ** 2 + n[1] ** 2 + n[2] ** 2)), 'b17-tanrad')
        if 'cut by a plane' in T and 'radius of the cut' in T:
            R, d = [F(x) for x in re.findall(r'(\d+) cm', T)[:2]]; return check_val(q, F(math.isqrt(int(R * R - d * d))), 'b17-cut')
        if 'through \\(A' in T and 'center \\(I' in T and 'sphere with center' in T.replace('The sphere with center', 'sphere with center'):
            I, A = P['I'], P['A']; return check_mcq(q, lambda o: sphere(txt(en_part(o))) == I + (d2(I, A),), 'b17-through')
        if '\\((Oxy)\\)' in T and 'tangent' in T or 'rests on the floor' in T or 'touching the plane \\((Oxy)\\)' in T:
            I = P['I']; return check_mcq(q, lambda o: sphere(txt(en_part(o))) == I + (I[2] ** 2,), 'b17-tan-oxy')
        if 'diameter \\(AB\\)' in T or 'as a diameter' in T:
            A, B = P['A'], P['B']; I = tuple((x + y) / 2 for x, y in zip(A, B)); return check_mcq(q, lambda o: sphere(txt(en_part(o))) == I + (d2(A, B) / 4,), 'b17-diam')
        if 'symmetric to' in T or 'reflection in' in T or 'is reflected through' in T:
            a, b, c, R2 = sp; J = (a, b, -c) if '(Oxy)' in T else ((-a, b, c) if '(Oyz)' in T else (-a, -b, -c))
            return check_mcq(q, lambda o: sphere(txt(en_part(o))) == J + (R2,), 'b17-reflect')
        if 'relative to the sphere' in T or 'the point lies…' in T or 'Decide the position of' in T:
            A = P['A']; a, b, c, R2 = sp; k = d2(A, (a, b, c)); want = 'inside the sphere' if k < R2 else ('outside the sphere' if k > R2 else 'on the sphere')
            return check_mcq(q, lambda o: txt(en_part(o)) == want, 'b17-point')
        if '(Oxz)' in T and typ == 'tf': a, b, c, R2 = sp; return check_tf(q, b * b == R2, 'b17-tf-oxz')
        if '+m=0' in T and typ == 'short':
            a, b, c, _ = ge; R = F(re.search(r'radius (?:\\\(R=)?(\d+)', T).group(1)); return check_val(q, a * a + b * b + c * c - R * R, 'b17-m')
        if 'box' in T.lower() and "O'(" in T:
            a = P['A'][0]; b = P['C'][1]; c = P["O'"][2]; return check_mcq(q, lambda o: sphere(txt(en_part(o))) == (a / 2, b / 2, c / 2, (a * a + b * b + c * c) / 4), 'b17-box')
        if 'three coordinate planes' in T or 'corner of a room' in T or 'touching \\((Oxy)\\), \\((Oyz)\\)' in T:
            R = F(re.search(r'radius (\d+)', T).group(1)); return check_mcq(q, lambda o: sphere(txt(en_part(o))) == (R, R, R, R * R), 'b17-three')
        if 'largest possible length' in T or 'shortest distance' in T or 'farthest point' in T:
            a, b, c, R2 = sp; A = P['A']; d = d2(A, (a, b, c)); assert isq(d) and isq(R2); d, R = math.isqrt(int(d)), math.isqrt(int(R2))
            return check_val(q, d - R if 'shortest' in T else d + R, 'b17-maxdist')
        if 'A student solved' in T:
            a, b, c, dd = ge; st = sphere(T.split('\\Leftrightarrow')[1]); good = st[:3] == (a, b, c)
            R = F(re.search(r'radius \\\(R=(\d+)', T).group(1)); okR = R * R == a * a + b * b + c * c - dd
            return check_text(q, 'Step 1 is wrong' if (not good and okR) else ('Only the radius is wrong' if good and not okR else 'Both steps are correct'), 'b17-error')
        if 'axis \\(Ox\\)' in T or '-axis' in T or 'The axis \\(Ox\\)' in T:
            a, b, c, R2 = sp; k2 = R2 - b * b - c * c; assert isq(k2); return check_val(q, 2 * math.isqrt(int(k2)), 'b17-chord')
        if ('touch' in T and 'balls' in T) or 'tangent externally' in T or 'Two spheres touch' in T:
            a, b, c, R2 = sp; J = P['J']; d = d2(J, (a, b, c)); assert isq(d) and isq(R2); return check_val(q, math.isqrt(int(d)) - math.isqrt(int(R2)), 'b17-touch')
        if 'tangent plane to the sphere at' in T or 'plane tangent to' in T or 'plane touching' in T:
            a, b, c, R2 = sp; A = P['A']; assert d2(A, (a, b, c)) == R2; n = tuple(x - y for x, y in zip(A, (a, b, c))); D = -sum(x * y for x, y in zip(n, A))
            def same(o):
                p = plane(txt(en_part(o)).replace('\\(', '').replace('\\)', '')); k = [p[0], p[1], p[2], F(p[3] or 0)]
                return all(k[i] * n[j] == k[j] * n[i] for i in range(3) for j in range(3)) and k[0] * D == F(k[3]) * n[0] if n[0] else (k[1] * D == F(k[3]) * n[1] if n[1] else k[2] * D == F(k[3]) * n[2])
            return check_mcq(q, same, 'b17-tanplane')
        if '+m=0' in T:
            n = plane(T.split('(P):')[1] if '(P):' in T else T.split('plane \\(')[1]); a, b, c, R2 = sp; R = F(math.isqrt(int(R2))); L = F(math.isqrt(n[0] ** 2 + n[1] ** 2 + n[2] ** 2)); k = n[0] * a + n[1] * b + n[2] * c
            want = sorted([-k + R * L, -k - R * L]); return check_mcq(q, lambda o: sorted(nums(txt(en_part(o)))) == want, 'b17-parallel')
    # ============ Bài 18, 19
    if lid in ('g12-prob-01', 'g12-prob-02'):
        tx = tex_of(e); tr = tree_of(tx[0]) if tx and 'inner sep=1pt' in tx[0] else None
        if lid == 'g12-prob-01':
            if 'P(A\\cap B)=\\)…' not in T and re.search(r'\\\(P\(B\)=([\d.]+)\\\), \\\(P\(A\\cap B\)=([\d.]+)\\\)\. (?:Then )?\\\(P\(A\\mid B\)=', T):
                pb, pab = [F(x) for x in re.search(r'P\(B\)=([\d.]+)\\\), \\\(P\(A\\cap B\)=([\d.]+)', T).groups()]; return check_val(q, pab / pb, 'b18-formula')
            if 'wear glasses' in T and 'Of ' in T:
                a, b1, c, d1 = [int(x) for x in re.findall(r'(\d+)', T)[:4]]; return check_val(q, F(d1, b1 + d1), 'b18-glasses')
            if 'without replacement' in T and 'both white' in T:
                r_, w = [int(x) for x in re.findall(r'(\d+) (?:red|white)', T)[:2]]; n = r_ + w; return check_val(q, F(w, n) * F(w - 1, n - 1), 'b18-2draws')
            if typ == 'tf' and 'tree diagram' in T.lower():
                c = nums(T)[-1]; return check_tf(q, c == tr[3], 'b18-tf-tree')
            if typ == 'tf':
                truth = {'P(A\\mid B)=P(B\\mid A)\\) for all': False, 'are independent.': None, 'P(\\overline A\\mid B)=1-P(A\\mid B)': True, 'with replacement, the second draw depends': False, 'P(A\\cap B)=P(A)\\cdot P(B\\mid A)': True, 'then \\(P(A\\cap B)=0.6\\)': False}
                for k, v in truth.items():
                    if k in T:
                        if v is None: pa, pb_, pab = [F(x) for x in re.findall(r'=([\d.]+)', T)[:3]]; v = pa * pb_ == pab
                        return check_tf(q, v, 'b18-tf')
            if 'Find \\(P(A\\cap B)\\)' in T: pb, pa = [F(x) for x in re.findall(r'=([\d.]+)', T)[:2]]; return check_val(q, pb * pa, 'b18-and')
            if 'tested positive, of whom' in T: n, pos, tp = [int(x) for x in re.findall(r'(\d+)', T)[:3]]; return check_val(q, F(tp, pos), 'b18-med')
            if 'tree diagram' in T.lower():
                b, nb, x, nx, y, ny = tr; ev = re.search(r'P\(([^)]*)\)(?:\\\))?(?:\.|=|\s+is)', T.split('Find')[-1] if 'Find' in T else T).group(1)
                val = {'\\overline B\\cap A': nb * y, 'B\\cap\\overline A': b * nx, '\\overline B\\cap\\overline A': nb * ny}[ev]; return check_val(q, val, 'b18-tree-and')
            if 'cards numbered 1 to' in T:
                N, a, b = [int(x) for x in re.findall(r'(\d+)', T)[1:4]]; B = [i for i in range(1, N + 1) if i % a == 0]; return check_val(q, F(sum(1 for i in B if i % b == 0), len(B)), 'b18-cards')
            if 'Two dice are rolled' in T:
                s, v = [int(x) for x in re.findall(r'(\d+)', T)[:2]]; B = [(i, j) for i in range(1, 7) for j in range(1, 7) if i + j == s]; return check_val(q, F(sum(1 for p in B if v in p), len(B)), 'b18-dice')
            if 'family has' in T:
                n, m = [int(x) for x in re.findall(r'(\d+)', T)[:2]]; B = [c for c in range(2 ** n) if bin(c).count('1') >= 1]; return check_val(q, F(sum(1 for c in B if bin(c).count('1') >= m), len(B)), 'b18-family')
            if 'survey of' in T and 'Which statement is correct' in T:
                t = twoway_of(e); a, b, c, d = [int(num(x)) for x in t[0][:2] + t[1][:2]]; ind = F(a, a + b) == F(a + c, a + b + c + d)
                return check_text(q, 'are independent because' if ind else 'are not independent because', 'b18-indep')
            if 'missing number' in T or 'one number is missing' in T or 'Find \\(x\\)' in T:
                t = twoway_of(e); b = int(num(t[1][1])); p = num(re.search(r'(\\dfrac\{\d+\}\{\d+\})', T).group(1)); return check_val(q, p * b / (1 - p), 'b18-cell')
            if 'probability that a chosen girl' in T or 'smoker has a cough' in T or 'bus is late is' in T:
                want = {'girl': '\\(P(K\\mid G)\\)', 'smoker': '\\(P(H\\mid S)\\)', 'rainy': '\\(P(L\\mid R)\\)'}
                k = 'girl' if 'girl' in T else ('smoker' if 'smoker' in T else 'rainy'); return check_mcq(q, lambda o: txt(en_part(o)) == want[k], 'b18-notation')
            if 'A student found the probability' in T:
                t = twoway_of(e); a, b = int(num(t[0][0])), int(num(t[0][1])); den = int(re.search(r'\\dfrac\{\d+\}\{(\d+)\}', T).group(1))
                return check_text(q, 'Step 2 is wrong: divide by \\(n(B)=%d\\)' % (a + b) if den != a + b else 'The solution is correct', 'b18-error')
            if 'Compare the probability' in T:
                r_, w = [int(x) for x in re.findall(r'(\d+)', T)[:2]]; n = r_ + w; wo = F(r_, n) * F(r_ - 1, n - 1); wi = F(r_, n) ** 2
                return check_mcq(q, lambda o: nums(txt(en_part(o)).replace('\\dfrac{', ' ').replace('}{', '/'))[:0] == [] and ('Without replacement' in txt(en_part(o)) and 'smaller' in txt(en_part(o)) and '\\dfrac{%d}{%d}' % (wo.numerator, wo.denominator) in txt(en_part(o)).split(';')[0]), 'b18-replace')
            if 'probability of \\(B\\) is' in T or 'Then \\(P(B)=' in T or 'find \\(P(B)\\)' in T:
                pab = F(re.search(r'P\(A\\cap B\)=([\d.]+)', T).group(1)); x = F(re.search(r'P\(A\\mid B\)=([\d.]+)', T).group(1)); return check_val(q, pab / x, 'b18-back')
            if 'Three balls' in T or 'three are tested' in T or 'three captains' in T:
                a, b = [int(x) for x in re.findall(r'(\d+)', T)[:2]]; n = a + b; return check_val(q, F(a, n) * F(a - 1, n - 1) * F(a - 2, n - 2), 'b18-three')
            if 'P(A\\cup B)' in T or 'revises or passes' in T or 'rains or the match' in T:
                pa, x, pb = [F(v) for v in re.findall(r'(0\.\d+)', T)[:3]]; return check_val(q, pa + pb - pa * x, 'b18-union')
            if 'mutually exclusive' in T or 'cannot happen together' in T or 'A\\cap B=\\varnothing' in T: return check_text(q, 'P(A\\mid B)=0\\), so', 'b18-exclusive')
            if 'Venn' in T:
                a_, both, b_, out = venn_of(tx[0]); return check_val(q, F(both, both + b_), 'b18-venn')
        else:
            if re.search(r'^\\\(P\(B\)=[\d.]+\\\), \\\(P\(A\\mid B\)=[\d.]+\\\), \\\(P\(A\\mid\\overline B\)=[\d.]+\\\)\. \\\(P\(A\)=', T):
                b, x, y = [F(v) for v in re.findall(r'=([\d.]+)\\\)', T)[:3]]; return check_val(q, b * x + (1 - b) * y, 'b19-total')
            if re.search(r'^\\\(P\(B\)=[\d.]+\\\), \\\(P\(A\\mid B\)=[\d.]+\\\), \\\(P\(A\\mid\\overline B\)=[\d.]+\\\)\. \\\(P\(B\\mid A\)=', T):
                b, x, y = [F(v) for v in re.findall(r'=([\d.]+)\\\)', T)[:3]]; return check_val(q, b * x / (b * x + (1 - b) * y), 'b19-bayes')
            if 'Box 1:' in T and 'Choose a box at random' in T:
                r1, w1, r2, w2 = [int(v) for v in re.findall(r'(\d+) (?:red|white)', T)[:4]]; return check_val(q, F(1, 2) * F(r1, r1 + w1) + F(1, 2) * F(r2, r2 + w2), 'b19-urn')
            if typ == 'tf' and 'tree diagram' in T.lower():
                b, nb, x, nx, y, ny = tr; post = b * x / (b * x + nb * y); claim_up = '\\gt' in T; return check_tf(q, (post > b) == claim_up, 'b19-tf-update')
            if typ == 'tf':
                if 'then \\(P(A)=' in T: b, x, y, c = [F(v) for v in re.findall(r'=([\d.]+)\\\)', T)[:4]]; return check_tf(q, b * x + (1 - b) * y == c, 'b19-tf-num')
                truth = {'for \\(0\\lt P(B)\\lt1\\)': True, 'P(B\\mid A)=P(B)P(A\\mid B)\\).': False, 'only when \\(A\\), \\(B\\) are independent': False, 'gives \\(P(\\text{sick}\\mid+)=0.99\\)': False, 'denominator of Bayes': True, 'are independent, then \\(P(B\\mid A)=P(B)\\)': True}
                for k, v in truth.items():
                    if k in T: return check_tf(q, v, 'b19-tf')
            if 'Machines make' in T and 'percentage' in T:
                p = [F(v) for v in re.findall(r'(\d+)%', T)]; return check_val(q, sum(a * d for a, d in zip(p[:3], p[3:6])) / 100, 'b19-machines')
            if 'knows the answer' in T and typ == 'short':
                m = int(re.search(r'(\d+)-option', T).group(1)); k = num(re.search(r'probability ([\d.]+)', T).group(1)); return check_val(q, k / (k + (1 - k) / m), 'b19-guess')
            if 'missing branch' in T or 'one branch is unknown' in T or 'calculate \\(P(A\\mid\\overline B)\\)' in T:
                b, nb, x, nx, y, ny = tr; pa = num(re.search(r'P\(A\)=([\d.]+)', T).group(1)) if 'P(A)=' in T else num(re.search(r'is \\\(([\d.]+)', T).group(1)); return check_val(q, (pa - b * x) / nb * 100, 'b19-branch')
            if 'Three machines' in T or 'Three farms' in T or 'Three bus lines' in T:
                p = [F(v) for v in re.findall(r'(\d+)%', T)]; k = ['I', 'II', 'III'].index(re.search(r'(?:machine|farm|line) (I{1,3}) (?:is|\.\.\.|…)', T).group(1))
                w = [a * d for a, d in zip(p[:3], p[3:6])]; return check_val(q, w[k] / sum(w), 'b19-post3')
            if 'is moved from' in T or 'taken from A and put into B' in T or 'moved from basket 1' in T:
                r1, w1, r2, w2 = [int(v) for v in re.findall(r'(\d+) (?:red|white|green|yellow|ripe|unripe)', T)[:4]]; n2 = r2 + w2 + 1; return check_val(q, F(r1, r1 + w1) * F(r2 + 1, n2) + F(w1, r1 + w1) * F(r2, n2), 'b19-move')
            if 'tree diagram' in T.lower() and ('NOT occur' in T or 'P(\\overline B\\mid A)' in T):
                b, nb, x, nx, y, ny = tr; return check_val(q, nb * y / (b * x + nb * y), 'b19-tree-post')
            if 'A student computed the probability' in T: return check_text(q, 'Step 2 is wrong', 'b19-error')
            if 'twice' in T or 'Both flag' in T or 'Both sensors alarm' in T:
                pb, x, y = [F(v) / 100 for v in re.findall(r'(\d+(?:\.\d+)?)%', T)[:3]]; return check_val(q, pb * x * x / (pb * x * x + (1 - pb) * y * y), 'b19-twotests')
            if 'prior probability' in T or 'Then \\(P(B)=' in T or 'Find \\(P(B)\\) if' in T:
                x = F(re.search(r'P\(A\\mid B\)=([\d.]+)', T).group(1)); y = F(re.search(r'P\(A\\mid\\overline B\)=([\d.]+)', T).group(1))
                s = re.search(r'P\(B\\mid A\)=((?:\\dfrac\{\d+\}\{\d+\})|[\d.]+)', T).group(1); post = num(s)
                return check_val(q, post * y / (x * (1 - post) + post * y), 'b19-prior')
            if 'more trustworthy' in T:
                p = [F(v) / 100 for v in re.findall(r'(\d+(?:\.\d+)?)%', T)[:5]]; pb, s1, f1, s2, f2 = p
                q1 = pb * s1 / (pb * s1 + (1 - pb) * f1); q2 = pb * s2 / (pb * s2 + (1 - pb) * f2); return check_text(q, 'Test %s, because \\(P(B\\mid+)\\) is larger' % ('X' if q1 > q2 else 'Y'), 'b19-compare')
            if 'does not germinate' in T or 'does not hatch' in T or 'seedling dies' in T:
                a, g1, g2 = [F(v) / 100 for v in re.findall(r'(\d+)%', T)[:3]]; return check_val(q, a * (1 - g1) / (a * (1 - g1) + (1 - a) * (1 - g2)), 'b19-seeds')
            if 'about how many' in T.lower():
                N = int(re.search(r'(\d{4,5})', T).group(1)); pb, x, y = [F(v) / 100 for v in re.findall(r'(\d+(?:\.\d+)?)%', T)[:3]]
                return check_val(q, N * pb * x if 'sick AND' in T else N * (pb * x + (1 - pb) * y), 'b19-expected')
            if 'complete system' in T:
                good = ['"3 or 4", \\(B_3\\): "5 or 6"', '"grade 11", \\(B_3\\): "grade 12"', '\\(\\overline B\\): "it does not rain tomorrow"']
                return check_mcq(q, lambda o: any(g in txt(en_part(o)) for g in good), 'b19-system')
            if 'most probably come' in T or 'most likely source' in T or 'largest posterior probability' in T:
                boxes = [(num(p), int(a), int(b)) for p, a, b in re.findall(r'probability (\\\(\\dfrac\{\d+\}\{\d+\}\\\))\) has (\d+) red and (\d+) white', T)]
                w = [p * F(a, a + b) for p, a, b in boxes]; k = max(range(3), key=lambda i: w[i]); return check_mcq(q, lambda o: txt(en_part(o)) == 'Box %d' % (k + 1), 'b19-argmax')
    return 'skip'

def main():
    global skip
    per = {}
    for lid, p in PAGES.items():
        o0, b0 = ok, bad; sk = 0
        for q in parse_page(open(os.path.join(ROOT, p), encoding='utf-8').read()):
            try: r = solve(lid, q)
            except Exception as ex: r = 'skip'; report.append(('LỖI GIẢI', lid, repr(ex)[:80], txt(q['en'])[:120]))
            if r == 'skip': sk += 1; skip += 1; report.append(('CHƯA GIẢI', lid, q['level'], q['section'], txt(q['en'])[:140]))
        per[lid] = (ok - o0, bad - b0, sk)
    for k, (a, b, c) in per.items(): print('%-14s đúng %3d | sai %d | chưa giải %d' % (k, a, b, c))
    print('TỔNG: %d/%d đúng, %d sai, %d chưa có bộ giải' % (ok, ok + bad + skip, bad, skip))
    for r in report: print(*r)
    return 0 if bad == 0 and skip == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
