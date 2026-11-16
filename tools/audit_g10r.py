# -*- coding: utf-8 -*-
"""Kiểm định ĐỘC LẬP đáp án Lớp 10, Bài 7–11 (vectơ) sau đợt hiệu chỉnh 14/11/2026.
Không dùng mã sinh câu (sp_g10r, sp_g10c, sp_g10d). Đọc trang đã dựng và nguồn TeX của hình (lưới ô vuông: mũi tên, điểm, trục),
tự dựng mô hình hình học (tọa độ tổng quát của hình bình hành, hình chữ nhật, lục giác đều, tam giác với trung điểm, trọng tâm),
tự tính kết quả và so với đáp án trang; trắc nghiệm phải có đúng MỘT phương án khớp.

    python tools/audit_g10r.py
"""
import os, re, sys, math, html as _h
from fractions import Fraction as F
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from question_bank import parse_page

PAGES = {'g10-vec-01': 'lessons/grade10/vectors/vector-concepts.html', 'g10-vec-02': 'lessons/grade10/vectors/vector-sum-difference.html',
         'g10-vec-03': 'lessons/grade10/vectors/vector-scalar-multiple.html', 'g10-vec-04': 'lessons/grade10/vectors/vectors-coordinate-plane.html',
         'g10-vec-05': 'lessons/grade10/vectors/dot-product.html'}

def txt(h): return re.sub(r'\s+', ' ', _h.unescape(re.sub(r'<[^>]+>', ' ', h))).strip()
def en_part(o):
    m = re.search(r'<span class="en">(.*?)</span>', o, re.S); return m.group(1) if m else o
def ot(o): return re.sub(r'\\dfrac(\d)(\d)', r'\\dfrac{\1}{\2}', txt(en_part(o)))
def inner(o):
    s = ot(o).strip(); return s[2:-2] if s.startswith('\\(') and s.endswith('\\)') else s
def getv(T, n):
    m = re.search(r'\\vec %s=(\((?:-?[\d.]+);\\,(?:-?[\d.]+)\))' % n, T); return pair(m.group(1)) if m else None

def val(s):
    """Số dạng 'a', '-a', '\\dfrac{p}{q}', 'a\\sqrt{b}', '\\sqrt{b}' (có thể kèm đơn vị) → float."""
    s = s.replace('\\(', '').replace('\\)', '').replace('{,}', '.').replace('\\ \\text{N}', '').strip()
    m = re.fullmatch(r'(-?)(\d*)\\sqrt\{(\d+)\}', s)
    if m: return (-1 if m.group(1) else 1) * (int(m.group(2)) if m.group(2) else 1) * math.sqrt(int(m.group(3)))
    m = re.fullmatch(r'(-?)\\dfrac\{(\d+)\}\{(\d+)\}', s)
    if m: return (-1 if m.group(1) else 1) * int(m.group(2)) / int(m.group(3))
    m = re.fullmatch(r'-?\d+(?:\.\d+)?', s)
    return float(s) if m else None
def num(s):
    s = s.replace('\\(', '').replace('\\)', '').replace('{,}', '.')
    m = re.search(r'(-?)\\dfrac\{(\d+)\}\{(\d+)\}', s)
    if m: return (-1 if m.group(1) else 1) * F(int(m.group(2)), int(m.group(3)))
    m = re.search(r'-?\d+(?:\.\d+)?', s); return F(m.group(0)) if m else None
def pair(s):
    m = re.search(r'\((-?(?:\\dfrac\{\d+\}\{\d+\}|[\d.]+));\\,(-?(?:\\dfrac\{\d+\}\{\d+\}|[\d.]+))\)', s)
    return (num(m.group(1)), num(m.group(2))) if m else None
def pts(s):
    return {m.group(1): (num(m.group(2)), num(m.group(3))) for m in re.finditer(r'([A-Z])\((-?(?:\\dfrac\{\d+\}\{\d+\}|\d+));\\,(-?(?:\\dfrac\{\d+\}\{\d+\}|\d+))\)', s)}

# ---------------- hình mẫu tổng quát (không có quan hệ ngẫu nhiên giữa các cạnh)
def add(a, b): return (a[0] + b[0], a[1] + b[1])
def sub(a, b): return (a[0] - b[0], a[1] - b[1])
def mul(k, a): return (k * a[0], k * a[1])
def mid(a, b): return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
def dotp(a, b): return a[0] * b[0] + a[1] * b[1]
PGM = {'A': (F(0), F(0)), 'B': (F(5), F(0)), 'D': (F(13, 10), F(27, 10))}; PGM['C'] = add(PGM['B'], PGM['D']); PGM['O'] = mid(PGM['A'], PGM['C'])
RECT = {'A': (F(0), F(0)), 'B': (F(5), F(0)), 'C': (F(5), F(3)), 'D': (F(0), F(3))}; RECT['O'] = mid(RECT['A'], RECT['C'])
HEXF = {k: (math.cos(math.radians(60 * i)), math.sin(math.radians(60 * i))) for i, k in enumerate('ABCDEF')}; HEXF['O'] = (0.0, 0.0)
TRI = {'A': (F(13, 10), F(41, 10)), 'B': (F(0), F(0)), 'C': (F(6), F(0))}
TRI['M'] = mid(TRI['A'], TRI['B']); TRI['N'] = mid(TRI['A'], TRI['C']); TRI['P'] = mid(TRI['B'], TRI['C']); TRI['I'] = TRI['P']
TRI['G'] = ((TRI['A'][0] + TRI['B'][0] + TRI['C'][0]) / 3, (TRI['A'][1] + TRI['B'][1] + TRI['C'][1]) / 3)
TWO = {'A': (F(0), F(0)), 'B': (F(12, 5), F(0)), 'C': (F(24, 5), F(0)), 'D': (F(1), F(9, 5))}; TWO['E'] = add(TWO['D'], TWO['B']); TWO['F'] = add(TWO['D'], TWO['C'])

def vexpr(s, P):
    """Giá trị của biểu thức ±\\overrightarrow{XY}±… (hoặc \\vec0) trên hình P."""
    s = s.replace(' ', '')
    if s in ('\\vec0', '\\vec{0}'): return (0, 0)
    tot = (0, 0); ok = False
    for sg, a, b in re.findall(r'([+-]?)\\overrightarrow\{([A-Z])([A-Z])\}', s):
        v = sub(P[b], P[a]); tot = add(tot, mul(-1 if sg == '-' else 1, v)); ok = True
    return tot if ok else None
def veq(u, v): return u is not None and v is not None and abs(u[0] - v[0]) < 1e-9 and abs(u[1] - v[1]) < 1e-9

# ---------------- đọc hình lưới ô vuông từ nguồn TeX
def tex_of(h):
    return [open(os.path.join(ROOT, 'img', 'tex', f[:-4] + '.tex'), encoding='utf-8').read() for f in re.findall(r'img/tex/([0-9a-f]+\.svg)', h)]
U = 0.42
def grid_read(tex):
    arrows = [((float(a), float(b)), (float(c), float(d))) for a, b, c, d in re.findall(r'-\{Stealth\[length=2\.8mm\]\}\] \((-?[\d.]+),(-?[\d.]+)\) -- \((-?[\d.]+),(-?[\d.]+)\);', tex)]
    vlab = re.findall(r'fill=white\] at \([^)]*\) \{\$(\\vec [a-z])\$\}', tex)
    ax = re.findall(r'ink!85, line width=0\.7pt, -\{Stealth\[length=2\.2mm\]\}\] \((-?[\d.]+),(-?[\d.]+)\) -- \((-?[\d.]+),(-?[\d.]+)\);', tex)
    org = (float(ax[1][0]), float(ax[0][1])) if ax else None
    dots = [(float(a), float(b)) for a, b in re.findall(r'\\fill\[[^\]]*\] \((-?[\d.]+),(-?[\d.]+)\) circle', tex)]
    labs = [(float(a), float(b), n) for a, b, n in re.findall(r'at \((-?[\d.]+),(-?[\d.]+)\) \{\$([A-Z])\$\}', tex)]
    P = {}
    for x, y, n in labs:
        if not dots or n == 'O': continue
        d = min(dots, key=lambda p: (p[0] - x) ** 2 + (p[1] - y) ** 2); P[n] = d
    R = lambda p: (round((p[0] - org[0]) / U), round((p[1] - org[1]) / U)) if org else (round(p[0] / U), round(p[1] / U))
    V = {n: (round((b[0] - a[0]) / U), round((b[1] - a[1]) / U)) for n, (a, b) in zip(vlab, arrows)}
    return {k: R(v) for k, v in P.items()}, V

ok = bad = 0; report = []
def check_mcq(q, pred, tag):
    global ok, bad
    hits = [i for i, o in enumerate(q['options']) if pred(o)]
    if len(hits) == 1 and 'abcd'[hits[0]] == q['answer']: ok += 1
    else: bad += 1; report.append(('SAI', tag, q['answer'], hits, txt(q['en'])[:150]))
def check_num(q, v, tag):
    if q['type'] == 'mcq': return check_mcq(q, lambda o: val(ot(o)) is not None and abs(val(ot(o)) - float(v)) < 1e-9, tag)
    global ok, bad
    if abs(float(F(q['answer'].replace(',', '.'))) - float(v)) < 1e-9: ok += 1
    else: bad += 1; report.append(('SAI', tag, q['answer'], v, txt(q['en'])[:150]))
def check_tf(q, t, tag):
    global ok, bad
    if q['answer'] == ('true' if t else 'false'): ok += 1
    else: bad += 1; report.append(('SAI', tag, q['answer'], t, txt(q['en'])[:150]))
def check_vec(q, target, P, tag): return check_mcq(q, lambda o: veq(vexpr(inner(o), P), target), tag)
def check_text(q, needle, tag): return check_mcq(q, lambda o: needle in ot(o), tag)
def lastexpr(T):
    m = re.findall(r'\\\(([^()]*?(?:\\overrightarrow\{[A-Z]{2}\}[^()]*?)+)\\\)', T); return m[-1] if m else None

def solve(lid, q):
    e = q['en']; T = txt(e); typ = q['type']
    ns = [int(x) for x in re.findall(r'(?<![\w{])(\d+)(?![\w}])', T)]
    if lid == 'g10-vec-01':
        if 'no three on a line' in T: n = int(re.search(r'There are (\d+)', T).group(1)); return check_num(q, n * (n - 1), 'v7-count')
        if 'parallelogram with center O. Which vector equals' in T:
            tg = vexpr(re.search(r'equals \\\((.*?)\\\)', T).group(1), PGM); return check_vec(q, tg, PGM, 'v7-pgm-eq')
        if 'square with side' in T: a = int(re.search(r'side (\d+)', T).group(1)); return check_num(q, 2 * a * a, 'v7-square')
        if 'In the parallelogram ABCD,' in T:
            l, r_ = re.search(r'\\\((\\overrightarrow\{..\})=(\\overrightarrow\{..\})\\\)', T).groups(); return check_tf(q, veq(vexpr(l, PGM), vexpr(r_, PGM)), 'v7-tf-pgm')
        if 'regular hexagon ABCDEF with center O,' in T and 'opposite vectors' in T:
            u, v = re.findall(r'\\overrightarrow\{(..)\}', T); a = sub(HEXF[u[1]], HEXF[u[0]]); b = sub(HEXF[v[1]], HEXF[v[0]]); return check_tf(q, veq(a, mul(-1, b)), 'v7-tf-hex')
        if 'rectangle with AB =' in T: p, s = [int(x) for x in re.findall(r'= (\d+)', T)]; return check_num(q, math.hypot(p, s), 'v7-rect')
        if 'midpoints of' in T and ('equal to' in T or 'equals' in T):
            tg = vexpr(re.findall(r'\\\((\\overrightarrow\{..\})\\\)', T)[-1], TRI); return check_vec(q, tg, TRI, 'v7-mid')
        if 'Among the vectors' in T:
            _, V = grid_read(tex_of(e)[0]); a = V['\\vec a']; vs = [V[k] for k in ('\\vec b', '\\vec c', '\\vec d', '\\vec e')]
            col = [v for v in vs if a[0] * v[1] == a[1] * v[0]]
            if 'same direction' in T: n = sum(1 for v in col if dotp(a, v) > 0)
            elif 'collinear' in T: n = len(col)
            else: n = sum(1 for v in vs if v == a)
            return check_num(q, n, 'v7-grid')
        if 'rectangle with center' in T and typ == 'tf':
            st = T.split('(figure).')[1].strip()
            if 'opposite vectors' in st:
                u, v = re.findall(r'\\overrightarrow\{(..)\}', st); return check_tf(q, veq(sub(RECT[u[1]], RECT[u[0]]), mul(-1, sub(RECT[v[1]], RECT[v[0]]))), 'v7-tf-rect')
            if 'equal vectors' in st:
                u, v = re.findall(r'\\overrightarrow\{(..)\}', st); return check_tf(q, veq(sub(RECT[u[1]], RECT[u[0]]), sub(RECT[v[1]], RECT[v[0]])), 'v7-tf-rect')
            if 'same direction' in st:
                u, v = re.findall(r'\\overrightarrow\{(..)\}', st); a, b = sub(RECT[u[1]], RECT[u[0]]), sub(RECT[v[1]], RECT[v[0]]); return check_tf(q, a[0] * b[1] == a[1] * b[0] and dotp(a, b) > 0, 'v7-tf-rect')
            if '|' in st:
                u, v = re.findall(r'\\overrightarrow\{(..)\}', st); a, b = sub(RECT[u[1]], RECT[u[0]]), sub(RECT[v[1]], RECT[v[0]]); return check_tf(q, dotp(a, a) == dotp(b, b), 'v7-tf-rect')
            l, r_ = re.search(r'\\\((\\overrightarrow\{..\})=(\\overrightarrow\{..\})\\\)', st).groups(); return check_tf(q, veq(vexpr(l, RECT), vexpr(r_, RECT)), 'v7-tf-rect')
        if 'two equal parallelograms' in T:
            tg = re.search(r'other than \\\(\\overrightarrow\{(..)\}', T).group(1); d = sub(TWO[tg[1]], TWO[tg[0]])
            n = sum(1 for a in TWO for b in TWO if a != b and a + b != tg and sub(TWO[b], TWO[a]) == d); return check_num(q, n, 'v7-two')
        if 'rhombus with side' in T:
            a = int(re.search(r'side \\\((\d+)', T).group(1)); ang = int(re.search(r'=(\d+)\^\\circ', T).group(1)); d = re.search(r'\|\\overrightarrow\{(..)\}\|', T).group(1)
            t = math.radians(ang); A = (0, 0); B = (a, 0); D = (a * math.cos(t), a * math.sin(t)); C = add(B, D); Pm = {'A': A, 'B': B, 'C': C, 'D': D}
            return check_num(q, math.dist(Pm[d[0]], Pm[d[1]]), 'v7-rhombus')
        if 'A student wrote' in T:
            want = {'|\\overrightarrow{AB}|=|\\overrightarrow{CD}|': 'also need the same direction', 'are collinear, they have the same direction': 'may have opposite directions', 'always form a parallelogram': 'may lie on one line'}
            for k, w in want.items():
                if k in T: return check_text(q, w, 'v7-error')
        if 'zero vector' in T or T.startswith('Choose the true statement') or T.startswith('Which of the following is true'):
            good = ['same direction as every vector', '\\overrightarrow{MM}=\\overrightarrow{NN}=\\vec0', 'exactly when \\(A\\equiv B\\)']
            return check_mcq(q, lambda o: any(g in ot(o) for g in good), 'v7-zero')
        if 'velocity vectors are opposite' in T: s = re.search(r'at \\\((\d+)\\\)', T).group(1); return check_text(q, 'exactly when \\(v=%s\\)' % s, 'v7-opp')
        if 'right-angled at' in T and 'midpoint of \\(BC\\)' in T:
            p, s = [int(x) for x in re.findall(r'(?:AB|AC)=(\d+)', T)]; return check_num(q, math.hypot(p, s) / 2, 'v7-median')
        if 'The point \\(M\\) satisfies' in T:
            l, r_ = re.search(r'\\\((\\overrightarrow\{..\})=(\\overrightarrow\{..\})\\\)', T).groups(); v = vexpr(r_, PGM); s, t = l[-3], l[-2]
            M_ = add(PGM[s], v) if t == 'M' else sub(PGM[t], v)
            nm = [k for k in 'ABCD' if PGM[k] == M_]; return check_text(q, '\\(M\\equiv %s\\)' % nm[0], 'v7-point') if nm else None
        if ('collinear' in T and 'points' in T) or 'lie on one line exactly' in T or 'lie on a line?' in T: return check_text(q, 'are collinear', 'v7-collinear')
    if lid == 'g10-vec-02':
        if T.startswith('Simplify'):
            ts = re.findall(r'([+-]?)\\overrightarrow\{(.)(.)\}', T); D = {}
            for sg, a, b in ts:
                D.setdefault(a, 0); D.setdefault(b, 0); s_ = -1 if sg == '-' else 1; D[b] += s_; D[a] -= s_
            st = [k for k, v in D.items() if v == -1]; en = [k for k, v in D.items() if v == 1]
            return check_text(q, '\\overrightarrow{%s%s}' % (st[0], en[0]), 'v8-chasles')
        if T.startswith('ABCD is a parallelogram.'):
            ex = re.search(r'\\\((.*?)\\\)', T.replace('ABCD is a parallelogram.', '')).group(1).split('=')[0]; return check_vec(q, vexpr(ex, PGM), PGM, 'v8-pgm')
        if 'rectangle with AB =' in T: p, s = [int(x) for x in re.findall(r'= (\d+)', T)]; return check_num(q, math.hypot(p, s), 'v8-rect')
        if 'In a parallelogram ABCD,' in T:
            l, r_ = re.search(r'\\\((.*?)=(.*?)\\\)', T).groups(); return check_tf(q, veq(vexpr(l, PGM), vexpr(r_, PGM)), 'v8-tf-pgm')
        if 'For a regular hexagon' in T:
            l, r_ = re.search(r'O: \\\((.*?)=(.*?)\\\)', T).groups(); return check_tf(q, veq(vexpr(l, HEXF), vexpr(r_, HEXF)), 'v8-tf-hex')
        if 'Two forces of' in T: p, s = [int(x) for x in re.findall(r'(\d+) N', T)]; return check_num(q, math.hypot(p, s), 'v8-force')
        if 'square with side' in T: a = int(re.search(r'side (\d+)', T).group(1)); return check_num(q, 2 * a * a, 'v8-square')
        if 'vectors drawn' in T or 'which vector is equal to' in T or 'find the vector equal to' in T:
            _, V = grid_read(tex_of(e)[0]); a, b = V['\\vec a'], V['\\vec b']; g = add(a, b) if '\\vec a+\\vec b' in T else sub(a, b)
            nm = [k for k in ('\\vec x', '\\vec y', '\\vec z', '\\vec w') if V[k] == g]; return check_mcq(q, lambda o: ot(o) == '\\(%s\\)' % nm[0], 'v8-grid') if len(nm) == 1 else report.append(('SAI', 'v8-grid', nm))
        if 'are the midpoints of' in T:
            ex = re.search(r'Then \\\((.*?)=', T).group(1); return check_vec(q, vexpr(ex, TRI), TRI, 'v8-mid')
        if 'is the centroid of triangle' in T and 'midpoint of \\(BC\\)' in T and typ == 'tf':
            st = T.split('(figure).')[1]; l, r_ = re.search(r'\\\((.*?)=(.*?)\\\)', st).groups(); return check_tf(q, veq(vexpr(l, TRI), vexpr(r_, TRI)), 'v8-tf-cent')
        if 'equilateral with side' in T:
            a = int(re.search(r'side \\\((\d+)', T).group(1)); E = {'A': (0, 0), 'B': (a, 0), 'C': (a / 2, a * math.sqrt(3) / 2)}
            ex = re.search(r'\|(.*?)\|', T).group(1); v = (0, 0)
            for sg, x, y in re.findall(r'([+-]?)\\overrightarrow\{(.)(.)\}', ex): v = add(v, mul(-1 if sg == '-' else 1, sub(E[y], E[x])))
            return check_num(q, math.hypot(*v), 'v8-equil')
        if 'A student wrote' in T:
            l, r_ = re.search(r'wrote \\\((.*?)=(.*?)\\\)', T).groups(); a, b = l.split('-'); x, y = a[-3:-1], b[-3:-1]
            return check_text(q, 'the correct result is \\(%s=\\overrightarrow{%s%s}\\)' % (l, y[1], x[1]), 'v8-error')
        if 'a point \\(M\\) with' in T:
            ts = re.findall(r'([+-]?)\\overrightarrow\{M(.)\}', T); pos = [x for s, x in ts if s != '-']; neg = [x for s, x in ts if s == '-'][0]
            # M = P1 + P2 - Pneg  (từ tổng (X - M) = 0)
            P = dict(TRI); P['M'] = sub(add(P[pos[0]], P[pos[1]]), P[neg])
            def ev(o):
                m = re.fullmatch(r'\\\(([A-Z]{4})\\\) is a parallelogram', ot(o))
                if m:
                    a, b, c, d = m.group(1); return veq(sub(P[b], P[a]), sub(P[c], P[d]))
                m = re.fullmatch(r'\\\(M\\\) is the midpoint of \\\(([A-Z])([A-Z])\\\)', ot(o))
                if m: return veq(P['M'], mid(P[m.group(1)], P[m.group(2)]))
                return 'centroid' in ot(o) and veq(P['M'], TRI['G'])
            return check_mcq(q, ev, 'v8-point')
        if 'Two forces \\(\\vec F_1\\)' in T:
            Fv = int(re.search(r'each of \\\((\d+)', T).group(1)); ang = int(re.search(r'is \\\((\d+)\^\\circ', T).group(1))
            return check_num(q, 2 * Fv * math.cos(math.radians(ang / 2)), 'v8-forces')
        if 'regular hexagon with center' in T:
            ex = re.search(r'Then \\\((.*?)=', T).group(1); return check_vec(q, vexpr(ex, HEXF), HEXF, 'v8-hex')
        if 'Which value can' in T or 'Which value can the length' in T or 'Which value is possible' in T:
            p, s = [int(x) for x in re.findall(r'(\d+)', T)[:2]]; lo, hi = abs(p - s), p + s
            return check_mcq(q, lambda o: lo <= val(ot(o)) <= hi, 'v8-ineq')
        if 'is the centroid of triangle' in T:
            ex = re.search(r'Then \\\((.*?)=', T).group(1); return check_vec(q, vexpr(ex, TRI), TRI, 'v8-cent')
        if 'rectangle with \\(AB=' in T:
            p, s = [int(x) for x in re.findall(r'(?:AB|AD)=(\d+)', T)]; return check_num(q, 2 * math.hypot(p, s), 'v8-rect3')
    if lid == 'g10-vec-03':
        if re.search(r'Then \\\(\|.*\\vec a\|=', T) or (typ == 'short' and 'Find \\(|' in T):
            a = int(re.search(r'\|\\vec a\|=(\d+)', T).group(1)); k = re.search(r'\|(-?(?:\\dfrac\{\d+\}\{\d+\}|\d*))\\vec a\|(?:=|\\\))', T.split('Then')[-1] if 'Then' in T else T.split('Find')[-1]).group(1)
            kk = abs(num(k)) if k not in ('', '-') else 1; return check_num(q, kk * a, 'v9-len')
        if 'M is on side BC' in T:
            t = num(re.search(r'BM\}=(\\dfrac\{\d+\}\{\d+\})', T).group(1)); return check_num(q, t if 'with \\(z=' in T else 1 - t, 'v9-am')
        if 'PR}=k' in T:
            k = num(re.search(r'PQ\}=(-?\d+)', T).group(1)); return check_num(q, 1 / k, 'v9-ratio')
        if 'G is the centroid of triangle ABC.' in T:
            ts = re.findall(r'\\overrightarrow\{(..)\}', T); v = (0, 0)
            for x in ts: v = add(v, sub(TRI[x[1]], TRI[x[0]]))
            return check_tf(q, veq(v, (0, 0)), 'v9-tf-g')
        if 'with \\(\\vec a\\ne\\vec0\\), then' in T:
            k = num(re.search(r'\\vec b=(-?(?:\\dfrac\{\d+\}\{\d+\}|\d+))\\vec a', T).group(1)); same = 'the same direction' in T; return check_tf(q, (k > 0) == same, 'v9-tf-dir')
        if 'median AI has length' in T: return check_num(q, F(2, 3) * int(re.search(r'length (\d+)', T).group(1)), 'v9-ag')
        if re.search(r'\\overrightarrow\{MA\}\+\d?\\overrightarrow\{MB\}=\\vec0', T):
            c = re.search(r'(\d?)\\overrightarrow\{MA\}\+(\d?)\\overrightarrow\{MB\}', T); p, s = int(c.group(1) or 1), int(c.group(2) or 1); return check_num(q, F(s, p + s), 'v9-point')
        if 'equal parts' in T:
            n = int(re.search(r'(?:into|with) (\d+) equal', T).group(1)); tex = tex_of(e)[0]
            xs = {nm: float(x) for x, nm in re.findall(r'at \((-?[\d.]+),[\d.-]+\) \{\$([A-Z])\$\}', tex)}; L = xs['B'] - xs['A']; pos = {k: round((v - xs['A']) / L * n) for k, v in xs.items()}
            ex = re.findall(r'\\overrightarrow\{(..)\}', T)
            if typ == 'tf':
                k = num(re.search(r'=(-?\\dfrac\{\d+\}\{\d+\}|-?\d+)\\,', T).group(1)); (p1, q1), (u1, w1) = ex[0], ex[1]
                return check_tf(q, F(pos[q1] - pos[p1], pos[w1] - pos[u1]) == k, 'v9-tf-seg')
            if 'MA}+' in T.replace('\\overrightarrow{MA}+', 'MA}+'):
                c = re.search(r'(\d?)\\overrightarrow\{MA\}\+(\d?)\\overrightarrow\{MB\}', T); p, s = int(c.group(1) or 1), int(c.group(2) or 1); return check_num(q, F(s, p + s), 'v9-point')
            (p1, q1), (u1, w1) = ex[0], ex[1]; return check_num(q, F(pos[q1] - pos[p1], pos[w1] - pos[u1]), 'v9-seg')
        if '\\vec v=k\\,\\vec u' in T and 'figure' in T.lower() or 'Using the grid, the number' in T:
            _, V = grid_read(tex_of(e)[0]); u, v = V['\\vec u'], V['\\vec v']; k = F(v[0], u[0]) if u[0] else F(v[1], u[1]); return check_num(q, k, 'v9-grid')
        if 'Express \\(\\vec u\\)' in T or 'the vector \\(\\vec u\\) equals' in T or 'write \\(\\vec u=x' in T:
            _, V = grid_read(tex_of(e)[0]); a, b, u = V['\\vec a'], V['\\vec b'], V['\\vec u']
            def ev(o):
                s = inner(o); m = re.fullmatch(r'(-?)(\\dfrac\{\d+\}\{\d+\}|\d*)\\vec a([+-])(\\dfrac\{\d+\}\{\d+\}|\d*)\\vec b', s)
                x = (num(m.group(2)) if m.group(2) else 1) * (-1 if m.group(1) else 1); y = (num(m.group(4)) if m.group(4) else 1) * (-1 if m.group(3) == '-' else 1)
                return add(mul(x, a), mul(y, b)) == u
            return check_mcq(q, ev, 'v9-decomp')
        if 'is the centroid of triangle' in T:
            tg = re.search(r'Then \\\((\\overrightarrow\{..\})=', T).group(1); P = TRI; v = vexpr(tg, P); AB, AC = sub(P['B'], P['A']), sub(P['C'], P['A'])
            def ev(o):
                s = inner(o); tot = (0, 0)
                for sg, k, x in re.findall(r'([+-]?)(\\dfrac\{\d+\}\{\d+\}|\d*)\\overrightarrow\{(..)\}', s):
                    kk = (num(k) if k else 1) * (-1 if sg == '-' else 1); tot = add(tot, mul(kk, sub(P[x[1]], P[x[0]])))
                return veq(tot, v)
            return check_mcq(q, ev, 'v9-centroid')
        if 'A student claims' in T:
            want = {'are collinear, so there is': 'needs \\(\\vec a\\ne\\vec0\\)', 'k\\vec a=\\vec 0': '\\(k\\) may be \\(0\\)', '|k\\vec a|=k|\\vec a|': '|k|\\,|\\vec a|'}
            for k, w in want.items():
                if k in T: return check_text(q, w, 'v9-error')
        if 'are collinear when \\(m=' in T or 'lie on a line, where' in T or 'For which \\(m\\) are' in T:
            a1, b1 = re.search(r'AB\}=(-?\d*)\\vec u([+-]\d*)\\vec v', T).groups(); b2 = re.search(r'AC\}=m\\vec u([+-]\d*)\\vec v', T).group(1)
            a1 = int(a1) if a1 not in ('', '-') else (1 if a1 == '' else -1); b1 = int(b1) if b1 not in ('+', '-') else int(b1 + '1'); b2 = int(b2) if b2 not in ('+', '-') else int(b2 + '1')
            return check_num(q, F(b2, b1) * a1, 'v9-collin')
        if 'trapezoid' in T: a, b = [int(x) for x in re.findall(r'(?:AB|CD)=(\d+)', T)]; return check_num(q, F(a + b, 2), 'v9-trap')
        if 'parallelogram with center' in T:
            tg = re.search(r'Then \\\((\\overrightarrow\{..\})=', T).group(1); P = PGM; v = vexpr(tg, P)
            def ev(o):
                s = inner(o); tot = (0, 0)
                for sg, k, x in re.findall(r'([+-]?)(\\dfrac\{\d+\}\{\d+\}|\d*)\\overrightarrow\{(..)\}', s):
                    kk = (num(k) if k else 1) * (-1 if sg == '-' else 1); tot = add(tot, mul(kk, sub(P[x[1]], P[x[0]])))
                return veq(tot, v)
            return check_mcq(q, ev, 'v9-para')
        if 'Then \\(\\vec w=k\\,\\vec v\\)' in T:
            sp = [int(x) for x in re.findall(r'at \\\((\d+)\\\)', T)]; dirs = re.findall(r'(east|west|north|south|downstream|upstream)', T)
            opp = {('east', 'west'), ('west', 'east'), ('downstream', 'upstream'), ('north', 'south')}; sg = -1 if (dirs[0], dirs[1]) in opp else 1
            return check_num(q, sg * F(sp[1], sp[0]), 'v9-speed')
    if lid == 'g10-vec-04':
        P = pts(T)
        if 'a bus stop is at' in T: return check_mcq(q, lambda o: pair(ot(o)) == sub(P['B'], P['A']), 'v10-ab')
        if 'The coordinates of' in T and '\\vec a=' in T:
            a = pair(T.split('\\vec a=')[1]); b = pair(T.split('\\vec b=')[1]); ex = re.search(r'coordinates of \\\((.*?)\\\)', T).group(1); v = (0, 0)
            for sg, k, x in re.findall(r'([+-]?)(\d*)\\vec ([ab])', ex): v = add(v, mul((int(k) if k else 1) * (-1 if sg == '-' else 1), a if x == 'a' else b))
            return check_mcq(q, lambda o: pair(ot(o)) == v, 'v10-lin')
        if 'A garden' in T: return check_mcq(q, lambda o: pair(ot(o)) == sub(add(P['A'], P['C']), P['B']), 'v10-pgm')
        if 'are collinear.' in T and typ == 'tf':
            u = pair(T.split('\\vec u=')[1]); w = pair(T.split('\\vec w=')[1]); return check_tf(q, u[0] * w[1] == u[1] * w[0], 'v10-tf-col')
        if 'centroid of triangle \\(EFH\\)' in T:
            G = ((P['E'][0] + P['F'][0] + P['H'][0]) / 3, (P['E'][1] + P['F'][1] + P['H'][1]) / 3); c = pair(T.split('meeting point is')[1]); return check_tf(q, c == G, 'v10-tf-g')
        if 'real distance' in T:
            u = int(re.search(r'1 unit = (\d+)', T).group(1)); d = math.dist(P['A'], P['B']); return check_num(q, d * u, 'v10-dist')
        if 'Find \\(m\\) so that \\(A\\), \\(B\\), \\(C\\) are collinear' in T:
            A, B = P['A'], P['B']; xc = num(re.search(r'C\((-?\d+);', T).group(1)); m = A[1] + (B[1] - A[1]) * (xc - A[0]) / (B[0] - A[0]); return check_num(q, m, 'v10-m')
        tex = tex_of(e); G_ = grid_read(tex[0]) if tex else ({}, {})
        if 'Read the coordinates of \\(\\vec u\\)' in T or 'shows the vector \\(\\vec u\\)' in T or '\\(\\vec u=\\)…' in T:
            u = G_[1]['\\vec u']; return check_mcq(q, lambda o: pair(ot(o)) == u, 'v10-readvec')
        if '|\\overrightarrow{AB}|' in T or 'length of \\(\\overrightarrow{AB}\\)' in T or 'find \\(AB\\)' in T:
            A, B = G_[0]['A'], G_[0]['B']; return check_num(q, math.dist(A, B), 'v10-readlen')
        if typ == 'tf' and 'coordinate grid' in T:
            A, B, C = G_[0]['A'], G_[0]['B'], G_[0]['C']; return check_tf(q, (C[0] * 2, C[1] * 2) == (A[0] + B[0], A[1] + B[1]), 'v10-tf-mid')
        if 'x\\vec a+y\\vec b' in T:
            a, b, c = getv(T, 'a'), getv(T, 'b'), getv(T, 'c')
            det = a[0] * b[1] - a[1] * b[0]; x = F(c[0] * b[1] - c[1] * b[0], det); y = F(a[0] * c[1] - a[1] * c[0], det)
            return check_mcq(q, lambda o: [int(v) for v in re.findall(r'-?\d+', ot(o))] == [x, y], 'v10-comb')
        if 'axis \\(Ox\\)' in T:
            A, B = P['A'], P['B']; x = A[0] - A[1] * (B[0] - A[0]) / (B[1] - A[1]); return check_mcq(q, lambda o: pair(ot(o)) == (x, 0), 'v10-axis')
        if 'symmetric to \\(A\\)' in T or 'midpoint of \\(AC\\)' in T or 'reflection of \\(A\\)' in T:
            A, B = G_[0]['A'], G_[0]['B']; return check_mcq(q, lambda o: pair(ot(o)) == (2 * B[0] - A[0], 2 * B[1] - A[1]), 'v10-sym')
        if 'a student wrote' in T:
            A, B = G_[0]['A'], G_[0]['B']; w = pair(T.split('wrote')[1]); return check_text(q, 'Wrong: \\(\\overrightarrow{AB}=%s\\)' % ('(%d;\\,%d)' % sub(B, A)) if w != sub(B, A) else 'Correct', 'v10-error')
        if 'centroid \\(G' in T or 'centroid of triangle \\(ABC\\) is \\(G' in T:
            G = P['G']; return check_mcq(q, lambda o: pair(ot(o)) == (3 * G[0] - P['A'][0] - P['B'][0], 3 * G[1] - P['A'][1] - P['B'][1]), 'v10-third')
        if 'MA}=-' in T:
            k = int(re.search(r'MA\}=-(\d)', T).group(1)); A, B = G_[0]['A'], G_[0]['B']; Mp = (F(A[0] + k * B[0], k + 1), F(A[1] + k * B[1], k + 1))
            return check_mcq(q, lambda o: pair(ot(o)) == Mp, 'v10-divide')
        if '|\\vec v|=' in T:
            u = pair(T.split('\\vec u=')[1]); L = int(re.search(r'\|\\vec v\|=(\d+)', T).group(1)); k = F(L, int(math.isqrt(int(dotp(u, u))))); k = k if 'same direction' in T else -k
            return check_mcq(q, lambda o: pair(ot(o)) == mul(k, u), 'v10-scale')
        if 'perimeter' in T:
            A, B, C = G_[0]['A'], G_[0]['B'], G_[0]['C']; return check_num(q, math.dist(A, B) + math.dist(B, C) + math.dist(C, A), 'v10-perim')
    if lid == 'g10-vec-05':
        P = pts(T)
        if 'Triangle \\(ABC\\) is equilateral with side' in T and 'A student' not in T:
            a = int(re.search(r'side \\\((\d+)', T).group(1)); E = {'A': (0, 0), 'B': (a, 0), 'C': (a / 2, a * math.sqrt(3) / 2)}
            u, v = re.findall(r'\\overrightarrow\{(..)\}', T)[:2]; return check_num(q, dotp(sub(E[u[1]], E[u[0]]), sub(E[v[1]], E[v[0]])), 'v11-equil')
        if 'Then \\(\\vec a\\cdot\\vec b=' in T and '\\vec a=(' in T:
            a = pair(T.split('\\vec a=')[1]); b = pair(T.split('\\vec b=')[1]); return check_num(q, dotp(a, b), 'v11-dot')
        if 'The angle between' in T:
            u = pair(T.split('\\vec u=')[1]); v = pair(T.split('\\vec v=')[1]); ang = round(math.degrees(math.acos(dotp(u, v) / math.hypot(*u) / math.hypot(*v))))
            return check_mcq(q, lambda o: re.search(r'(\d+)\^\\circ', ot(o)) and int(re.search(r'(\d+)\^\\circ', ot(o)).group(1)) == ang, 'v11-angle')
        if 'posts of a fence' in T:
            d = dotp(sub(P['B'], P['A']), sub(P['C'], P['A'])); kind = 'right' if 'right angle' in T else ('obtuse' if 'obtuse' in T else 'acute')
            return check_tf(q, {'right': d == 0, 'obtuse': d < 0, 'acute': d > 0}[kind], 'v11-tf-fence')
        if '|\\vec a+\\vec b|=' in T and typ == 'tf':
            a, b, ang, c = [int(x) for x in re.findall(r'=(\d+)', T)[:4]]; return check_tf(q, abs(a * a + b * b + 2 * a * b * math.cos(math.radians(ang)) - c * c) < 1e-9, 'v11-tf-norm')
        if 'sled' in T: Fv = pair(T.split('\\vec F=')[1]); dv = pair(T.split('\\vec d=')[1]); return check_num(q, dotp(Fv, dv), 'v11-work')
        if 'Find \\(m\\) so that \\(\\vec g\\perp\\vec h\\)' in T:
            g = pair(T.split('\\vec g=')[1]); hx = num(re.search(r'\\vec h=\((-?\d+)', T).group(1)); return check_num(q, -g[0] * hx / g[1], 'v11-perp')
        if 'square with side' in T:
            a = int(re.search(r'side \\\((\d+)', T).group(1)); S = {'A': (0, 0), 'B': (a, 0), 'C': (a, a), 'D': (0, a)}; u, v = re.findall(r'\\overrightarrow\{(..)\}', T)[:2]
            return check_num(q, dotp(sub(S[u[1]], S[u[0]]), sub(S[v[1]], S[v[0]])), 'v11-square')
        if 'right-angled at \\(A\\)' in T:
            p, s = [int(x) for x in re.findall(r'(?:AB|AC)=(\d+)', T)]; R_ = {'A': (0, 0), 'B': (0, p), 'C': (s, 0)}; u, v = re.findall(r'\\overrightarrow\{(..)\}', T)[:2]
            return check_num(q, dotp(sub(R_[u[1]], R_[u[0]]), sub(R_[v[1]], R_[v[0]])), 'v11-right')
        if 'rectangle with \\(AB\\ne AD\\)' in T:
            st = T.split('(figure).')[1]; u, v = re.findall(r'\\overrightarrow\{(..)\}', st)[:2]; d = dotp(sub(RECT[u[1]], RECT[u[0]]), sub(RECT[v[1]], RECT[v[0]]))
            if '=0' in st: t = d == 0
            elif '\\gt0' in st: t = d > 0
            else: X = re.search(r'=(A[BD])\^2', st).group(1); t = d == dotp(sub(RECT[X[1]], RECT[X[0]]), sub(RECT[X[1]], RECT[X[0]]))
            return check_tf(q, t, 'v11-tf-rect')
        if 'foot of the altitude' in T:
            bh, hc = [int(x) for x in re.findall(r'(?:BH|HC)=(\d+)', T)]; return check_num(q, bh * (bh + hc), 'v11-proj')
        if '\\(|\\vec a-\\vec b|=\\)' in T:
            a, b, ang = [int(x) for x in re.findall(r'=(\d+)', T)[:3]]; return check_num(q, math.sqrt(a * a + b * b - 2 * a * b * math.cos(math.radians(ang))), 'v11-diff')
        if 'A student wrote' in T:
            a = int(re.search(r'side \\\((\d+)', T).group(1)); E = {'A': (0, 0), 'B': (a, 0), 'C': (a / 2, a * math.sqrt(3) / 2)}; u, v = re.findall(r'\\overrightarrow\{(..)\}', T)[:2]
            true = round(dotp(sub(E[u[1]], E[u[0]]), sub(E[v[1]], E[v[0]]))); return check_text(q, 'so the result is \\(%d\\)' % true, 'v11-error')
        if '(m;\\,1)' in T:
            p, s = getv(T, 'a'); lo, hi = [int(x) for x in (re.search(r'\[(-?\d+);\\,(-?\d+)\]', T) or re.search(r'from \\\((-?\d+)\\\) to \\\((-?\d+)\\\)', T)).groups()]
            n = sum(1 for m in range(lo, hi + 1) if p * m + s > 0 and p * 1 != s * m); return check_num(q, n, 'v11-acute')
        if 'grid' in T and 'triangle' in T.lower():
            Q = grid_read(tex_of(e)[0])[0]; rt = [k for k in 'ABC' if dotp(sub(Q[[x for x in 'ABC' if x != k][0]], Q[k]), sub(Q[[x for x in 'ABC' if x != k][1]], Q[k])) == 0]
            return check_text(q, 'right-angled at \\(%s\\)' % rt[0] if rt else 'not a right triangle', 'v11-righttri')
        if '|\\vec a+\\vec b|^2=' in T or '|\\vec a-\\vec b|^2=' in T:
            a, b, s2 = [int(x) for x in re.findall(r'=(\d+)', T)[:3]]; d = F(s2 - a * a - b * b, 2) if '+\\vec b|^2' in T else F(a * a + b * b - s2, 2); return check_num(q, d, 'v11-norm')
        if 'work' in T.lower() and 'situation' in T:
            good = ['carries a box and walks along a level floor', 'gravity points to the center', 'holds a tray up while walking horizontally']
            return check_mcq(q, lambda o: any(g in ot(o) for g in good), 'v11-work0')
        if 'rectangle with \\(AB=' in T:
            a, b = [int(x) for x in re.findall(r'(?:AB|AD)=(\d+)', T)]; R_ = {'A': (0, 0), 'B': (a, 0), 'C': (a, b), 'D': (0, b)}; u, v = re.findall(r'\\overrightarrow\{(..)\}', T)[:2]
            return check_num(q, dotp(sub(R_[u[1]], R_[u[0]]), sub(R_[v[1]], R_[v[0]])), 'v11-rect')
    return 'skip'

def main():
    per = {}
    for lid, p in PAGES.items():
        o0, b0, sk = ok, bad, 0
        for q in parse_page(open(os.path.join(ROOT, p), encoding='utf-8').read()):
            try: r = solve(lid, q)
            except Exception as ex: r = 'skip'; report.append(('LỖI GIẢI', lid, repr(ex)[:90], txt(q['en'])[:120]))
            if r == 'skip': sk += 1; report.append(('CHƯA GIẢI', lid, q['level'], q['section'], txt(q['en'])[:140]))
        per[lid] = (ok - o0, bad - b0, sk)
    for k, (a, b, c) in per.items(): print('%-11s đúng %3d | sai %d | chưa giải %d' % (k, a, b, c))
    S = sum(v[2] for v in per.values()); print('TỔNG: %d/%d đúng, %d sai, %d chưa có bộ giải' % (ok, ok + bad + S, bad, S))
    for r in report: print(*r)
    return 0 if bad == 0 and S == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
