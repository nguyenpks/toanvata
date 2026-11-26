# -*- coding: utf-8 -*-
"""Ngân hàng câu hỏi Toán 9 (KNTT) – Bài 24 (ghép nhóm), Bài 25–26 (xác suất), Bài 27 (góc nội tiếp).
Dùng chung BANK/ABCD_TITLES của sp_g9. Câu có bảng, biểu đồ hoặc hình trả thêm khóa fig = (html_en, html_vi), ghép sau đề.
Mọi đáp án tính bằng số nguyên/Fraction từ chính dữ liệu sinh ra (đếm lại dãy dữ liệu, liệt kê lại không gian mẫu, đo lại góc).
Phần D (tự luyện 4 mức độ) dùng dạng câu khác với phần A–C."""
import random, math, itertools
from fractions import Fraction as F
from sp_g9 import tx, dm, pick_opts
from sp_g9s import htab, pe, pv, pct, popts, iopts
from mb_pgf import texsvg, col, _USED
import html as _h

INK = 'ink'


def img(fn, alt, px=440):
    _USED.append(fn)
    return ('<img src="../../../img/tex/%s" alt="%s" loading="lazy" style="display:block;margin:8px auto;width:min(100%%,%dpx);height:auto">'
            % (fn, _h.escape(alt, quote=True), px))


def _num(x, vi):
    x = F(x)
    s = str(x.numerator) if x.denominator == 1 else ('%g' % float(x))
    return s.replace('.', '{,}') if vi else s


def _t(s): return str(s).replace('%', '\\%').replace('&', '\\&')


# =====================================================================================================
# BIỂU ĐỒ GHÉP NHÓM: dạng cột (cột liền nhau) và dạng đoạn thẳng (qua giá trị đại diện)
# =====================================================================================================
def gchart_svg(edges, vals, xlab, ylab, title, vi=False, pct_=False, kind='bar', W=8.0, H=4.4):
    """edges: k+1 đầu mút; vals: k giá trị (tần số hoặc tần số tương đối %). kind: 'bar' | 'line'.
    Dạng đoạn thẳng: điểm (giá trị đại diện; giá trị), trục ngang ghi giá trị đại diện."""
    k = len(vals); bw = W / k; m = max(vals)
    for step in (1, 2, 5, 10, 20, 25, 50):
        if m / step <= 6: break
    top = step * (int(m // step) + 1); sy = H / top
    o = ['\\begin{tikzpicture}']
    for v in range(step, int(top) + 1, step):          # lưới ngang mờ
        o.append('\\draw[gray!25, line width=0.4pt] (0,%.3f) -- (%.3f,%.3f);' % (v * sy, W + 0.2, v * sy))
    o.append('\\draw[ink!85, line width=0.7pt, -{Stealth[length=2.4mm]}] (0,0) -- (%.3f,0);' % (W + 0.6))
    o.append('\\draw[ink!85, line width=0.7pt, -{Stealth[length=2.4mm]}] (0,0) -- (0,%.3f);' % (H + 0.5))
    if kind == 'bar':
        for i, f in enumerate(vals):
            o.append('\\draw[draw=%s, fill=%s, line width=0.6pt] (%.3f,0) rectangle (%.3f,%.3f);' % (col('046b4d'), col('86e0bd'), i * bw, (i + 1) * bw, float(f) * sy))
            o.append('\\node[font=\\footnotesize, text=ink, above] at (%.3f,%.3f) {$%s%s$};' % ((i + 0.5) * bw, float(f) * sy, _num(f, vi), '\\%' if pct_ else ''))
        for i, e in enumerate(edges):
            o.append('\\draw[ink!70] (%.3f,0) -- (%.3f,-0.08) node[below, font=\\small, text=ink] {$%s$};' % (i * bw, i * bw, _num(e, vi)))
    else:
        pts = [((i + 0.5) * bw, float(f) * sy) for i, f in enumerate(vals)]
        for x, _ in pts:
            o.append('\\draw[ink!40, dash pattern=on 2pt off 2pt] (%.3f,0) -- (%.3f,%.3f);' % (x, x, _ + 0.0))
        o.append('\\draw[color=%s, line width=1.3pt] %s;' % (col('c2410c'), ' -- '.join('(%.3f,%.3f)' % p for p in pts)))
        for i, ((x, y), f) in enumerate(zip(pts, vals)):
            o.append('\\fill[color=%s] (%.3f,%.3f) circle (2.4pt);' % (col('c2410c'), x, y))
            L = float(vals[i - 1]) if i else None; R = float(vals[i + 1]) if i + 1 < k else None
            nb = [u for u in (L, R) if u is not None]
            pos = 'above=3pt' if all(float(f) >= u for u in nb) else ('above left=1pt' if (L is not None and L < float(f)) or (R is not None and R > float(f)) else 'above right=1pt')
            if all(float(f) <= u for u in nb): pos = 'below right=2pt' if float(f) * sy > 0.5 else 'above right=2pt'
            o.append('\\node[font=\\footnotesize, text=ink, %s] at (%.3f,%.3f) {$%s%s$};' % (pos, x, y, _num(f, vi), '\\%' if pct_ else ''))
            md = F(edges[i] + edges[i + 1], 2)
            o.append('\\draw[ink!70] (%.3f,0) -- (%.3f,-0.08) node[below, font=\\small, text=ink] {$%s$};' % (x, x, _num(md, vi)))
    for v in range(step, int(top) + 1, step):
        o.append('\\draw[ink!70] (0,%.3f) -- (-0.08,%.3f) node[left, font=\\small, text=ink] {$%s%s$};' % (v * sy, v * sy, v, '\\%' if pct_ else ''))
    o.append('\\node[font=\\small, text=ink, anchor=north east] at (%.3f,-0.55) {%s};' % (W + 0.6, _t(xlab)))
    o.append('\\node[font=\\small, text=ink, anchor=south west] at (0.12,%.3f) {%s};' % (H + 0.5, _t(ylab)))
    o.append('\\node[font=\\bfseries\\small, text=ink] at (%.3f,%.3f) {%s};' % (W / 2, H + 1.45, _t(title)))
    o.append('\\end{tikzpicture}')
    return texsvg('\n'.join(o))


def GCHART_Q(edges, vals, lab, title, pct_=False, kind='bar', px=460):
    """Cặp ảnh (en, vi) đặt trong đề. lab: ((xlab_en, ylab_en), (xlab_vi, ylab_vi)); title: (en, vi)."""
    fe = gchart_svg(edges, vals, lab[0][0], lab[0][1], title[0], False, pct_, kind)
    fv = gchart_svg(edges, vals, lab[1][0], lab[1][1], title[1], True, pct_, kind)
    return (img(fe, title[0], px), img(fv, title[1], px))


# =====================================================================================================
# BÀI 24. Bảng tần số, tần số tương đối ghép nhóm và biểu đồ
# =====================================================================================================
GCTX = [
    dict(le='Time (minutes)', lv='Thời gian (phút)', ae='the time (in minutes) %d students take to go to school', av='thời gian (phút) đi từ nhà đến trường của %d học sinh',
         ue='students', uv='học sinh', edges=[0, 5, 10, 15, 20, 25, 30, 35], unit=('minutes', 'phút'), what=('time', 'thời gian')),
    dict(le='Height (cm)', lv='Chiều cao (cm)', ae='the heights (in cm) of %d students', av='chiều cao (cm) của %d học sinh',
         ue='students', uv='học sinh', edges=[145, 150, 155, 160, 165, 170, 175, 180], unit=('cm', 'cm'), what=('height', 'chiều cao')),
    dict(le='Mass (g)', lv='Khối lượng (g)', ae='the masses (in grams) of %d eggs', av='khối lượng (g) của %d quả trứng gà',
         ue='eggs', uv='quả trứng', edges=[40, 45, 50, 55, 60, 65, 70], unit=('g', 'g'), what=('mass', 'khối lượng')),
    dict(le='Speed (km/h)', lv='Tốc độ (km/h)', ae='the speeds (in km/h) of %d motorbikes passing a speed camera', av='tốc độ (km/h) của %d xe máy đi qua một trạm đo tốc độ',
         ue='motorbikes', uv='xe máy', edges=[20, 30, 40, 50, 60, 70, 80], unit=('km/h', 'km/h'), what=('speed', 'tốc độ')),
    dict(le='Score', lv='Điểm', ae='the scores (out of 100) of %d students in a math contest', av='điểm (thang điểm 100) của %d học sinh trong một cuộc thi Toán',
         ue='students', uv='học sinh', edges=[40, 50, 60, 70, 80, 90, 100], unit=('points', 'điểm'), what=('score', 'điểm')),
    dict(le='Screen time (minutes)', lv='Thời gian (phút)', ae='the daily screen time (in minutes) of %d students', av='thời gian dùng điện thoại mỗi ngày (phút) của %d học sinh',
         ue='students', uv='học sinh', edges=[0, 30, 60, 90, 120, 150, 180], unit=('minutes', 'phút'), what=('screen time', 'thời gian dùng điện thoại')),
    dict(le='Rainfall (mm)', lv='Lượng mưa (mm)', ae='the daily rainfall (in mm) on %d rainy days', av='lượng mưa (mm) trong %d ngày mưa',
         ue='days', uv='ngày', edges=[0, 10, 20, 30, 40, 50, 60], unit=('mm', 'mm'), what=('rainfall', 'lượng mưa')),
]
GNS = (20, 25, 40, 50)
GFE, GFV = 'Frequency (m)', 'Tần số (m)'
GRE, GRV = 'Relative frequency (f)', 'Tần số tương đối (f)'


def gname(a, b, last=False): return '[%s; %s%s' % (a, b, ']' if last else ')')


def gtex(a, b, last=False): return '\\([%s;\\,%s%s\\)' % (a, b, ']' if last else ')')


def ggen(r, c=None, k=(4, 6), ns=GNS, uniq=True):
    """(bối cảnh, đầu mút, tần số). Các nhóm liên tiếp lấy từ c['edges']."""
    c = c or r.choice(GCTX)
    kk = r.randint(k[0], min(k[1], len(c['edges']) - 1)); st = r.randint(0, len(c['edges']) - 1 - kk)
    ed = c['edges'][st:st + kk + 1]
    for _ in range(4000):
        ms = [r.randint(1, 15) for _ in range(kk)]; n = sum(ms)
        if n not in ns: continue
        if uniq and (ms.count(max(ms)) > 1): continue
        return c, ed, ms
    raise AssertionError


def gtab(c, ed, ms, rel=False, hide=None):
    """Bảng ghép nhóm ngang, hai bản ngôn ngữ. hide: chỉ số ô ghi '?'."""
    lab = (GRE, GRV) if rel else (GFE, GFV)
    cells = []
    for i, m in enumerate(ms):
        if i == hide: cells.append('?')
        elif rel: cells.append(('%s%%' % pe(m), '%s%%' % pv(m)))
        else: cells.append(m)
    groups = [gname(ed[i], ed[i + 1]) for i in range(len(ms))]
    rows = [('Group (%s)' % c['le'], 'Nhóm (%s)' % c['lv'], groups), (lab[0], lab[1], cells)]
    return (htab(rows, 'en'), htab(rows, 'vi'))


def glab(c, rel):
    y = ('Relative frequency', 'Tần số tương đối') if rel else ('Frequency', 'Tần số')
    return ((c['le'], y[0]), (c['lv'], y[1]))


def graw(r, ed, ms, boundary=True):
    """Dãy dữ liệu thô (số nguyên) có đúng tần số ms trong các nhóm [ed_i; ed_i+1). Có thể có giá trị bằng đầu mút trái."""
    d = []
    for i, m in enumerate(ms):
        a, b = ed[i], ed[i + 1]
        vals = [r.randint(a, b - 1) for _ in range(m)]
        if boundary and m >= 2 and i > 0: vals[0] = a                   # giá trị đúng bằng đầu mút: thuộc nhóm bên phải
        d += vals
    r.shuffle(d)
    for i, m in enumerate(ms): assert sum(1 for x in d if ed[i] <= x < ed[i + 1]) == m
    return d


def about(c, n): return c['ae'] % n, c['av'] % n


def gopts(ed, good, k=None):
    """Phương án là tên nhóm."""
    n = len(ed) - 1; o = [gtex(ed[good], ed[good + 1])]
    for j in [good - 1, good + 1, good + 2, good - 2, good + 3, good - 3]:
        if 0 <= j < n and len(o) < 4: o.append(gtex(ed[j], ed[j + 1]))
    assert len(o) == 4
    return o


def b24_member(r, lv):
    c, ed, ms = ggen(r, k=(4, 6))
    i = r.randint(1, len(ms) - 1); x = ed[i]                           # giá trị đúng bằng đầu mút
    if r.random() < 0.35: x = r.randint(ed[i - 1] + 1, ed[i] - 1); i = i - 1
    return dict(en='The data on %s are grouped into the groups %s. Which group contains the value \\(%s\\)?' % (c['what'][0], ', '.join(gtex(ed[j], ed[j + 1]) for j in range(len(ms))), x),
                vi='Dữ liệu về %s được ghép thành các nhóm %s. Giá trị \\(%s\\) thuộc nhóm nào?' % (c['what'][1], ', '.join(gtex(ed[j], ed[j + 1]) for j in range(len(ms))), x),
                opts=gopts(ed, i), ans=0,
                ee='The group \\([a;\\,b)\\) contains \\(a\\) but not \\(b\\): \\(%d\\le %s\\lt %d\\).' % (ed[i], x, ed[i + 1]),
                ev='Nhóm \\([a;\\,b)\\) chứa \\(a\\) nhưng không chứa \\(b\\): \\(%d\\le %s\\lt %d\\).' % (ed[i], x, ed[i + 1]))


def b24_ngroups(r, lv):
    h = r.choice([5, 10, 20, 50]); lo = r.randint(1, 6) * h; k = r.randint(4, 8); hi = lo + k * h - r.randint(1, h - 1)
    mn = lo + r.randint(0, h // 2); mx = hi
    k_ = -(-(mx - lo + 1) // h)
    assert k_ == k
    return dict(en='The smallest value of a data set is %d and the largest is %d. The data are grouped into groups \\([%d;\\,%d)\\), \\([%d;\\,%d)\\), … of the same width %d. How many groups are needed?' % (mn, mx, lo, lo + h, lo + h, lo + 2 * h, h),
                vi='Giá trị nhỏ nhất của một mẫu số liệu là %d, giá trị lớn nhất là %d. Ghép số liệu thành các nhóm \\([%d;\\,%d)\\), \\([%d;\\,%d)\\), … có cùng độ dài %d. Cần bao nhiêu nhóm?' % (mn, mx, lo, lo + h, lo + h, lo + 2 * h, h),
                opts=iopts(r, k, [k - 1, k + 1, (mx - mn) // h, k + 2]), ans=0,
                ee='The last group must contain %d: \\([%d;\\,%d)\\). From %d to %d there are \\(\\dfrac{%d-%d}{%d}=%d\\) groups.' % (mx, lo + (k - 1) * h, lo + k * h, lo, lo + k * h, lo + k * h, lo, h, k),
                ev='Nhóm cuối phải chứa %d: \\([%d;\\,%d)\\). Từ %d đến %d có \\(\\dfrac{%d-%d}{%d}=%d\\) nhóm.' % (mx, lo + (k - 1) * h, lo + k * h, lo, lo + k * h, lo + k * h, lo, h, k))


def b24_relgroup(r, lv):
    c, ed, ms = ggen(r)
    n = sum(ms); i = r.randrange(len(ms)); f = pct(ms[i], n)
    ae, av = about(c, n)
    return dict(en='The grouped frequency table shows %s. What is the relative frequency of the group %s?' % (ae, gtex(ed[i], ed[i + 1])),
                vi='Bảng tần số ghép nhóm cho biết %s. Tần số tương đối của nhóm %s là bao nhiêu?' % (av, gtex(ed[i], ed[i + 1])),
                opts=popts(r, f, [ms[i], pct(ms[(i + 1) % len(ms)], n), 100 - f, f + 10]), ans=0,
                ee='\\(f=\\dfrac{%d}{%d}\\cdot100\\%%=%s\\%%\\).' % (ms[i], n, pe(f)), ev='\\(f=\\dfrac{%d}{%d}\\cdot100\\%%=%s\\%%\\).' % (ms[i], n, dm(pe(f))),
                fig=gtab(c, ed, ms))


def b24_tf_count(r, lv):
    c, ed, ms = ggen(r, k=(4, 4), ns=(20,))
    d = graw(r, ed, ms); i = r.randint(1, len(ms) - 1); m = ms[i]
    truth = r.random() < 0.5
    claim = m if truth else m + r.choice([-1, 1]) * r.choice([1, 1, 2])
    if claim == m: truth = True
    if claim <= 0: claim = m + 1; truth = False
    ae, av = about(c, len(d))
    return dict(en='Here are %s: %s. The group %s has frequency %d.' % (ae, ', '.join(map(str, d)), gtex(ed[i], ed[i + 1]), claim),
                vi='Dưới đây là %s: %s. Nhóm %s có tần số %d.' % (av, ', '.join(map(str, d)), gtex(ed[i], ed[i + 1]), claim), ans=truth,
                ee='Count the values \\(x\\) with \\(%d\\le x\\lt %d\\) (the value %d belongs to this group, the value %d does not): there are %d.' % (ed[i], ed[i + 1], ed[i], ed[i + 1], m),
                ev='Đếm các giá trị \\(x\\) thỏa mãn \\(%d\\le x\\lt %d\\) (giá trị %d thuộc nhóm này, giá trị %d thì không): có %d giá trị.' % (ed[i], ed[i + 1], ed[i], ed[i + 1], m))


def b24_tf_mid(r, lv):
    c = r.choice(GCTX); ed = c['edges']; i = r.randrange(len(ed) - 1); a, b = ed[i], ed[i + 1]; md = F(a + b, 2)
    truth = r.random() < 0.5; claim = md if truth else r.choice([F(b - a), F(b - a, 2), F(b), F(a)])
    if claim == md: truth = True
    return dict(en='In the relative frequency line chart of grouped data, the point of the group %s has horizontal coordinate \\(%s\\).' % (gtex(a, b), pe(claim)),
                vi='Trong biểu đồ tần số tương đối ghép nhóm dạng đoạn thẳng, điểm ứng với nhóm %s có hoành độ \\(%s\\).' % (gtex(a, b), dm(pe(claim))), ans=truth,
                ee='The horizontal coordinate is the midpoint \\(\\dfrac{%d+%d}{2}=%s\\).' % (a, b, pe(md)), ev='Hoành độ là giá trị đại diện \\(\\dfrac{%d+%d}{2}=%s\\).' % (a, b, dm(pe(md))))


def b24_short_missing(r, lv):
    c, ed, ms = ggen(r)
    n = sum(ms); i = r.randrange(len(ms)); ae, av = about(c, n)
    return dict(en='The grouped frequency table shows %s, with one frequency missing. Find the missing frequency.' % ae,
                vi='Bảng tần số ghép nhóm cho biết %s, trong đó bị mất một tần số. Tìm tần số còn thiếu.' % av, key=str(ms[i]),
                ee='\\(%d-(%s)=%d\\).' % (n, '+'.join(str(m) for j, m in enumerate(ms) if j != i), ms[i]),
                ev='\\(%d-(%s)=%d\\).' % (n, '+'.join(str(m) for j, m in enumerate(ms) if j != i), ms[i]), fig=gtab(c, ed, ms, hide=i))


def b24_short_below(r, lv):
    c, ed, ms = ggen(r, k=(4, 6))
    n = sum(ms); fs = [pct(m, n) for m in ms]; j = r.randint(1, len(ms) - 1)
    s = sum(fs[:j]); ae, av = about(c, n)
    up = r.random() < 0.5
    val = s if not up else 100 - s
    if up:
        en = 'The relative frequency histogram shows %s. What percentage of the %s have a value of at least %d %s?' % (ae, c['ue'], ed[j], c['unit'][0])
        vi = 'Biểu đồ tần số tương đối ghép nhóm dạng cột cho biết %s. Bao nhiêu phần trăm số %s có giá trị từ %d %s trở lên?' % (av, c['uv'], ed[j], c['unit'][1])
        ee = 'Add the bars from %d on: \\(%s=%s\\).' % (ed[j], '+'.join(pe(f) for f in fs[j:]), pe(val)); ev = 'Cộng các cột từ %d trở đi: \\(%s=%s\\).' % (ed[j], '+'.join(dm(pe(f)) for f in fs[j:]), dm(pe(val)))
    else:
        en = 'The relative frequency histogram shows %s. What percentage of the %s have a value less than %d %s?' % (ae, c['ue'], ed[j], c['unit'][0])
        vi = 'Biểu đồ tần số tương đối ghép nhóm dạng cột cho biết %s. Bao nhiêu phần trăm số %s có giá trị nhỏ hơn %d %s?' % (av, c['uv'], ed[j], c['unit'][1])
        ee = 'Add the bars before %d: \\(%s=%s\\).' % (ed[j], '+'.join(pe(f) for f in fs[:j]), pe(val)); ev = 'Cộng các cột đứng trước %d: \\(%s=%s\\).' % (ed[j], '+'.join(dm(pe(f)) for f in fs[:j]), dm(pe(val)))
    return dict(en=en, vi=vi, key=pe(val), hint=('Enter a number (e.g. 37.5).', 'Nhập một số (ví dụ 37,5).'), ee=ee, ev=ev,
                fig=GCHART_Q(ed, fs, glab(c, True), ('Relative frequency histogram', 'Biểu đồ tần số tương đối ghép nhóm'), pct_=True))


def b24_d1_def(r, lv):
    a = r.choice([10, 20, 40, 150]); h = r.choice([5, 10]); b = a + h
    k = r.choice(['contain', 'width', 'mid'])
    if k == 'contain':
        o = [tx('\\(%d\\) belongs to it, \\(%d\\) does not' % (a, b), '\\(%d\\) thuộc nhóm, \\(%d\\) không thuộc nhóm' % (a, b)),
             tx('\\(%d\\) does not belong to it, \\(%d\\) does' % (a, b), '\\(%d\\) không thuộc nhóm, \\(%d\\) thuộc nhóm' % (a, b)),
             tx('both \\(%d\\) and \\(%d\\) belong to it' % (a, b), 'cả \\(%d\\) và \\(%d\\) đều thuộc nhóm' % (a, b)),
             tx('neither \\(%d\\) nor \\(%d\\) belongs to it' % (a, b), 'cả \\(%d\\) và \\(%d\\) đều không thuộc nhóm' % (a, b))]
        return dict(en='Which statement about the group \\([%d;\\,%d)\\) is correct?' % (a, b), vi='Khẳng định nào về nhóm \\([%d;\\,%d)\\) là đúng?' % (a, b), opts=o, ans=0,
                    ee='\\([%d;\\,%d)\\) means \\(%d\\le x\\lt %d\\).' % (a, b, a, b), ev='\\([%d;\\,%d)\\) gồm các giá trị \\(x\\) với \\(%d\\le x\\lt %d\\).' % (a, b, a, b))
    if k == 'width':
        return dict(en='What is the width of the group \\([%d;\\,%d)\\)?' % (a, b), vi='Độ dài của nhóm \\([%d;\\,%d)\\) bằng bao nhiêu?' % (a, b),
                    opts=['%d' % h, '%d' % (a + b), '%s' % pe(F(a + b, 2)), '%d' % (h + 1)], ans=0, ee='Width \\(=%d-%d=%d\\).' % (b, a, h), ev='Độ dài nhóm \\(=%d-%d=%d\\).' % (b, a, h))
    md = F(a + b, 2)
    return dict(en='What is the midpoint (representative value) of the group \\([%d;\\,%d)\\)?' % (a, b), vi='Giá trị đại diện của nhóm \\([%d;\\,%d)\\) là bao nhiêu?' % (a, b),
                opts=[tx('\\(%s\\)' % pe(md), '\\(%s\\)' % dm(pe(md))), '%d' % h, '%d' % (a + b), tx('\\(%s\\)' % pe(F(h, 2)), '\\(%s\\)' % dm(pe(F(h, 2))))], ans=0,
                ee='\\(\\dfrac{%d+%d}{2}=%s\\).' % (a, b, pe(md)), ev='\\(\\dfrac{%d+%d}{2}=%s\\).' % (a, b, dm(pe(md))))


def b24_d1_mode(r, lv):
    c, ed, ms = ggen(r, ns=(20, 25, 40, 50), uniq=True)
    i = ms.index(max(ms)); n = sum(ms); ae, av = about(c, n)
    which = r.choice(['max', 'min']) if ms.count(min(ms)) == 1 else 'max'
    i = ms.index(max(ms)) if which == 'max' else ms.index(min(ms))
    return dict(en='The histogram shows %s. Which group has the %s frequency?' % (ae, 'greatest' if which == 'max' else 'smallest'),
                vi='Biểu đồ tần số ghép nhóm dạng cột cho biết %s. Nhóm nào có tần số %s?' % (av, 'lớn nhất' if which == 'max' else 'nhỏ nhất'),
                opts=gopts(ed, i), ans=0, ee='The %s bar: %s, frequency %d.' % ('highest' if which == 'max' else 'lowest', gtex(ed[i], ed[i + 1]), ms[i]),
                ev='Cột %s: %s, tần số %d.' % ('cao nhất' if which == 'max' else 'thấp nhất', gtex(ed[i], ed[i + 1]), ms[i]),
                fig=GCHART_Q(ed, ms, glab(c, False), ('Grouped frequency chart', 'Biểu đồ tần số ghép nhóm')))


def b24_d1_sum(r, lv):
    k = r.choice(['rel', 'n', 'calc', 'calc'])
    if k == 'calc':
        c, ed, ms = ggen(r, k=(4, 5), ns=range(15, 46)); n = sum(ms)
        return dict(en='A grouped frequency table about %s has the frequencies %s. What is the sample size?' % (c['what'][0], ', '.join(map(str, ms))),
                    vi='Bảng tần số ghép nhóm về %s có các tần số %s. Cỡ mẫu bằng bao nhiêu?' % (c['what'][1], ', '.join(map(str, ms))),
                    opts=iopts(r, n, [len(ms), max(ms), n - ms[-1], n + ms[0]]), ans=0,
                    ee='\\(n=%s=%d\\).' % ('+'.join(map(str, ms)), n), ev='\\(n=%s=%d\\).' % ('+'.join(map(str, ms)), n))
    if k == 'rel':
        o = [tx('\\(100\\%\\)', '\\(100\\%\\)'), tx('the sample size \\(n\\)', 'cỡ mẫu \\(n\\)'), tx('\\(1\\%\\)', '\\(1\\%\\)'), tx('the number of groups', 'số nhóm')]
        return dict(en='In a grouped relative frequency table, the sum of all relative frequencies is…', vi='Trong bảng tần số tương đối ghép nhóm, tổng tất cả các tần số tương đối bằng…', opts=o, ans=0,
                    ee='\\(f_1+f_2+\\dots+f_k=100\\%\\).', ev='\\(f_1+f_2+\\dots+f_k=100\\%\\).')
    o = [tx('the sample size \\(n\\)', 'cỡ mẫu \\(n\\)'), tx('\\(100\\%\\)', '\\(100\\%\\)'), tx('the number of groups', 'số nhóm'), tx('the width of a group', 'độ dài một nhóm')]
    return dict(en='In a grouped frequency table, the sum of all frequencies is equal to…', vi='Trong bảng tần số ghép nhóm, tổng tất cả các tần số bằng…', opts=o, ans=0,
                ee='Each value belongs to exactly one group, so \\(m_1+m_2+\\dots+m_k=n\\).', ev='Mỗi giá trị thuộc đúng một nhóm nên \\(m_1+m_2+\\dots+m_k=n\\).')


def b24_d2_raw(r, lv):
    c, ed, ms = ggen(r, k=(4, 4), ns=(20,))
    d = graw(r, ed, ms); i = r.randrange(len(ms)); m = ms[i]
    near = sum(1 for x in d if ed[i] < x <= ed[i + 1])
    ae, av = about(c, len(d))
    return dict(en='Here are %s: %s. Group the data into %s. What is the frequency of the group %s?' % (ae, ', '.join(map(str, d)), ', '.join(gtex(ed[j], ed[j + 1]) for j in range(len(ms))), gtex(ed[i], ed[i + 1])),
                vi='Dưới đây là %s: %s. Ghép số liệu thành các nhóm %s. Tần số của nhóm %s là bao nhiêu?' % (av, ', '.join(map(str, d)), ', '.join(gtex(ed[j], ed[j + 1]) for j in range(len(ms))), gtex(ed[i], ed[i + 1])),
                opts=iopts(r, m, [near, m + 1, m - 1, ms[(i + 1) % 4]]), ans=0,
                ee='Values \\(x\\) with \\(%d\\le x\\lt %d\\): %d values.' % (ed[i], ed[i + 1], m), ev='Các giá trị \\(x\\) với \\(%d\\le x\\lt %d\\): có %d giá trị.' % (ed[i], ed[i + 1], m))


def b24_d2_count(r, lv):
    c, ed, ms = ggen(r)
    n = sum(ms); i = r.randrange(len(ms)); fs = [pct(m, n) for m in ms]; ae, av = about(c, n)
    return dict(en='The grouped relative frequency table shows %s. How many %s are in the group %s?' % (ae, c['ue'], gtex(ed[i], ed[i + 1])),
                vi='Bảng tần số tương đối ghép nhóm cho biết %s. Có bao nhiêu %s thuộc nhóm %s?' % (av, c['uv'], gtex(ed[i], ed[i + 1])),
                opts=iopts(r, ms[i], [int(fs[i]) if fs[i].denominator == 1 and fs[i] != ms[i] else ms[i] + 2, ms[i] + 1, ms[i] - 1, n - ms[i]]), ans=0,
                ee='\\(m=%d\\cdot%s\\%%=%d\\).' % (n, pe(fs[i]), ms[i]), ev='\\(m=%d\\cdot%s\\%%=%d\\).' % (n, dm(pe(fs[i])), ms[i]), fig=gtab(c, ed, fs, rel=True))


def b24_d2_point(r, lv):
    c, ed, ms = ggen(r)
    n = sum(ms); i = r.randrange(len(ms)); f = pct(ms[i], n); md = F(ed[i] + ed[i + 1], 2)
    def P(x, y): return tx('\\((%s;\\,%s)\\)' % (pe(x), pe(y)), '\\((%s;\\,%s)\\)' % (dm(pe(x)), dm(pe(y))))
    o = [P(md, f), P(ed[i], f), P(md, ms[i]), P(ed[i + 1], f)]
    ae, av = about(c, n)
    return dict(en='The table shows %s. In the relative frequency line chart, the point of the group %s has coordinates…' % (ae, gtex(ed[i], ed[i + 1])),
                vi='Bảng dưới đây cho biết %s. Trong biểu đồ tần số tương đối ghép nhóm dạng đoạn thẳng, điểm ứng với nhóm %s có tọa độ là…' % (av, gtex(ed[i], ed[i + 1])),
                opts=o, ans=0, ee='(midpoint; relative frequency) \\(=\\left(\\dfrac{%d+%d}{2};\\,\\dfrac{%d}{%d}\\cdot100\\right)=(%s;\\,%s)\\).' % (ed[i], ed[i + 1], ms[i], n, pe(md), pe(f)),
                ev='(giá trị đại diện; tần số tương đối) \\(=\\left(\\dfrac{%d+%d}{2};\\,\\dfrac{%d}{%d}\\cdot100\\right)=(%s;\\,%s)\\).' % (ed[i], ed[i + 1], ms[i], n, dm(pe(md)), dm(pe(f))),
                fig=gtab(c, ed, ms))


def b24_d3_line(r, lv):
    c, ed, ms = ggen(r)
    n = sum(ms); fs = [pct(m, n) for m in ms]; i = r.randrange(len(ms)); md = F(ed[i] + ed[i + 1], 2); ae, av = about(c, n)
    return dict(en='The relative frequency line chart shows %s. How many %s are in the group whose midpoint is \\(%s\\)?' % (ae, c['ue'], pe(md)),
                vi='Biểu đồ tần số tương đối ghép nhóm dạng đoạn thẳng cho biết %s. Có bao nhiêu %s thuộc nhóm có giá trị đại diện \\(%s\\)?' % (av, c['uv'], dm(pe(md))),
                opts=iopts(r, ms[i], [int(fs[i]) if fs[i].denominator == 1 and fs[i] != ms[i] else ms[i] + 2, ms[i] + 1, n - ms[i], ms[(i + 1) % len(ms)]]), ans=0,
                ee='The midpoint \\(%s\\) belongs to %s with \\(f=%s\\%%\\): \\(m=%d\\cdot%s\\%%=%d\\).' % (pe(md), gtex(ed[i], ed[i + 1]), pe(fs[i]), n, pe(fs[i]), ms[i]),
                ev='Giá trị đại diện \\(%s\\) ứng với nhóm %s có \\(f=%s\\%%\\): \\(m=%d\\cdot%s\\%%=%d\\).' % (dm(pe(md)), gtex(ed[i], ed[i + 1]), dm(pe(fs[i])), n, dm(pe(fs[i])), ms[i]),
                fig=GCHART_Q(ed, fs, glab(c, True), ('Relative frequency line chart', 'Biểu đồ tần số tương đối ghép nhóm dạng đoạn thẳng'), pct_=True, kind='line'))


def b24_d3_bar(r, lv):
    c, ed, ms = ggen(r)
    n = sum(ms); fs = [pct(m, n) for m in ms]; i = r.randrange(len(ms))
    o = [tx('\\(%s\\%%\\)' % pe(fs[i]), '\\(%s\\%%\\)' % dm(pe(fs[i])))]
    for b in (ms[i], 2 * fs[i], 100 - fs[i], fs[i] + 5, fs[i] + 10):
        t = tx('\\(%s\\%%\\)' % pe(b), '\\(%s\\%%\\)' % dm(pe(b)))
        if b != fs[i] and 0 < b <= 100 and t not in o and len(o) < 4: o.append(t)
    ae, av = about(c, n)
    return dict(en='We draw the relative frequency histogram for the table below (%s). How high is the bar of the group %s?' % (ae, gtex(ed[i], ed[i + 1])),
                vi='Vẽ biểu đồ tần số tương đối ghép nhóm dạng cột cho bảng dưới đây (%s). Cột ứng với nhóm %s cao bao nhiêu?' % (av, gtex(ed[i], ed[i + 1])),
                opts=o, ans=0, ee='Height = relative frequency \\(=\\dfrac{%d}{%d}\\cdot100\\%%=%s\\%%\\).' % (ms[i], n, pe(fs[i])),
                ev='Chiều cao cột = tần số tương đối \\(=\\dfrac{%d}{%d}\\cdot100\\%%=%s\\%%\\).' % (ms[i], n, dm(pe(fs[i]))), fig=gtab(c, ed, ms))


def b24_d3_merge(r, lv):
    c = r.choice(GCTX)
    st = r.randrange(0, len(c['edges']) - 5); ed = c['edges'][st:st + 5]
    for _ in range(3000):
        ms = [r.randint(1, 15) for _ in range(4)]
        if sum(ms) in GNS: break
    n = sum(ms); j = r.choice([0, 2]); a, b = ed[j], ed[j + 2]; m = ms[j] + ms[j + 1]
    return dict(en='The table shows a grouped frequency table with groups of width %d. If we regroup the data into groups of width %d, what is the frequency of the new group %s?' % (ed[1] - ed[0], 2 * (ed[1] - ed[0]), gtex(a, b)),
                vi='Bảng tần số ghép nhóm dưới đây có các nhóm độ dài %d. Nếu ghép lại thành các nhóm có độ dài %d thì nhóm mới %s có tần số bằng bao nhiêu?' % (ed[1] - ed[0], 2 * (ed[1] - ed[0]), gtex(a, b)),
                opts=iopts(r, m, [ms[j], ms[j + 1], ms[j + 1] + ms[(j + 2) % 4], m + 1]), ans=0,
                ee='%s is the union of %s and %s: \\(%d+%d=%d\\).' % (gtex(a, b), gtex(ed[j], ed[j + 1]), gtex(ed[j + 1], ed[j + 2]), ms[j], ms[j + 1], m),
                ev='Nhóm %s gồm hai nhóm %s và %s: \\(%d+%d=%d\\).' % (gtex(a, b), gtex(ed[j], ed[j + 1]), gtex(ed[j + 1], ed[j + 2]), ms[j], ms[j + 1], m),
                fig=gtab(c, ed, ms))


def b24_d4_compare(r, lv):
    c = GCTX[4] if r.random() < 0.5 else GCTX[0]
    ed = c['edges'][2:7] if c is GCTX[4] else c['edges'][1:6]
    for _ in range(5000):
        na, nb = r.choice([40, 50]), r.choice([20, 25])
        ma = [r.randint(2, 15) for _ in range(4)]; mb = [r.randint(1, 10) for _ in range(4)]
        if sum(ma) != na or sum(mb) != nb: continue
        A, B = ma[2] + ma[3], mb[2] + mb[3]
        fa, fb = pct(A, na), pct(B, nb)
        if A > B and fa < fb and (fa * 2).denominator == 1: break
    else: raise AssertionError
    thr = ed[2]
    if c is GCTX[4]:
        en = 'Two schools take part in a math contest. School X has %d students and school Y has %d students; their scores are grouped below. In which school is the proportion of students scoring at least %d points higher?' % (na, nb, thr)
        vi = 'Hai trường tham gia một cuộc thi Toán. Trường X có %d học sinh, trường Y có %d học sinh; điểm được ghép nhóm như bảng dưới. Trường nào có tỉ lệ học sinh đạt từ %d điểm trở lên cao hơn?' % (na, nb, thr)
    else:
        en = 'Class 9A has %d students and class 9B has %d students. The table shows the time (minutes) they take to go to school. In which class is the proportion of students who need at least %d minutes higher?' % (na, nb, thr)
        vi = 'Lớp 9A có %d học sinh, lớp 9B có %d học sinh. Bảng dưới cho biết thời gian (phút) đi đến trường của các em. Lớp nào có tỉ lệ học sinh cần từ %d phút trở lên cao hơn?' % (na, nb, thr)
    X, Y = ('X', 'Y') if c is GCTX[4] else ('9A', '9B')
    o = [tx('%s (%s%% > %s%%)' % (Y, pe(fb), pe(fa)), '%s (%s%% > %s%%)' % (Y, pv(fb), pv(fa))), tx('%s (%d > %d)' % (X, A, B), '%s (%d > %d)' % (X, A, B)),
         tx('%s (%s%% > %s%%)' % (X, pe(fa), pe(fb)), '%s (%s%% > %s%%)' % (X, pv(fa), pv(fb))), tx('the two are the same', 'như nhau')]
    groups = [gname(ed[i], ed[i + 1]) for i in range(4)]
    rows = [('Group', 'Nhóm', groups), ('Frequency – %s' % X, 'Tần số – %s' % X, ma), ('Frequency – %s' % Y, 'Tần số – %s' % Y, mb)]
    return dict(en=en, vi=vi, opts=o, ans=0,
                ee='%s: \\(\\dfrac{%d+%d}{%d}\\cdot100\\%%=%s\\%%\\); %s: \\(\\dfrac{%d+%d}{%d}\\cdot100\\%%=%s\\%%\\). The sample sizes differ, so compare relative frequencies.' % (X, ma[2], ma[3], na, pe(fa), Y, mb[2], mb[3], nb, pe(fb)),
                ev='%s: \\(\\dfrac{%d+%d}{%d}\\cdot100\\%%=%s\\%%\\); %s: \\(\\dfrac{%d+%d}{%d}\\cdot100\\%%=%s\\%%\\). Hai mẫu có cỡ khác nhau nên phải so sánh tần số tương đối.' % (X, ma[2], ma[3], na, dm(pe(fa)), Y, mb[2], mb[3], nb, dm(pe(fb))),
                fig=(htab(rows, 'en'), htab(rows, 'vi')))


def b24_d4_speed(r, lv):
    c = GCTX[3]; ed = [30, 40, 50, 60, 70, 80]; lim = r.choice([50, 60]); j = ed.index(lim)
    for _ in range(5000):
        ms = [r.randint(2, 20) for _ in range(5)]; n = sum(ms)
        if n in (25, 40, 50) and sum(ms[j:]) >= 3: break
    over = sum(ms[j:]); f = pct(over, n)
    gs = [gtex(ed[t], ed[t + 1]) for t in range(j, 5)]
    return dict(en='The histogram shows the speeds of %d motorbikes on a road with a speed limit of %d km/h. What percentage of the motorbikes were speeding (speed at least %d km/h)?' % (n, lim, lim),
                vi='Biểu đồ dưới đây cho biết tốc độ của %d xe máy trên một đoạn đường có tốc độ tối đa cho phép %d km/h. Bao nhiêu phần trăm số xe đã chạy quá tốc độ (từ %d km/h trở lên)?' % (n, lim, lim),
                opts=popts(r, f, [over, pct(ms[-1], n), 100 - f, pct(ms[j], n)]), ans=0,
                ee='Groups %s: \\(%s=%d\\) motorbikes; \\(\\dfrac{%d}{%d}\\cdot100\\%%=%s\\%%\\).' % (', '.join(gs), '+'.join(map(str, ms[j:])), over, over, n, pe(f)),
                ev='Các nhóm %s: \\(%s=%d\\) xe; \\(\\dfrac{%d}{%d}\\cdot100\\%%=%s\\%%\\).' % (', '.join(gs), '+'.join(map(str, ms[j:])), over, over, n, dm(pe(f))),
                fig=GCHART_Q(ed, ms, glab(c, False), ('Speeds of %d motorbikes' % n, 'Tốc độ của %d xe máy' % n)))


def b24_d4_choose(r, lv):
    lo, hi = r.choice([(31, 78), (142, 179), (12, 59), (41, 68), (102, 149)])
    span = hi - lo
    good = None; cands = [1, 2, 5, 10, 20, 50]
    # nhóm có độ dài h bắt đầu tại bội của h ngay dưới lo: số nhóm
    def ng(h): return (hi // h) - (lo // h) + 1
    hs = [h for h in cands if 4 <= ng(h) <= 8]
    good = hs[0]
    bad = [h for h in cands if ng(h) > 12][-1:] + [h for h in cands if ng(h) <= 2][:1] + [h for h in cands if h not in hs and 2 < ng(h) < 4][:1]
    bad = [b for b in bad if b != good]
    while len(bad) < 3:
        for h in (1, 100, 3):
            if h not in bad and h != good and len(bad) < 3: bad.append(h)
    o = [tx('width %d (%d groups)' % (good, ng(good)), 'độ dài %d (%d nhóm)' % (good, ng(good)))] + [tx('width %d (%d groups)' % (h, ng(h)), 'độ dài %d (%d nhóm)' % (h, ng(h))) for h in bad[:3]]
    assert len(set(o)) == 4
    return dict(en='The values of a data set of 40 observations lie between %d and %d. We want between 4 and 8 groups of the same width, starting at a multiple of the width. Which grouping is suitable?' % (lo, hi),
                vi='Các giá trị của một mẫu 40 số liệu nằm trong khoảng từ %d đến %d. Ta muốn ghép thành từ 4 đến 8 nhóm có cùng độ dài, nhóm đầu bắt đầu tại một bội của độ dài nhóm. Cách ghép nào phù hợp?' % (lo, hi),
                opts=o, ans=0,
                ee='Width %d: groups from \\(%d\\) to \\(%d\\), that is %d groups. Too many groups (or too few) make the table hard to read.' % (good, lo // good * good, (hi // good + 1) * good, ng(good)),
                ev='Độ dài %d: các nhóm từ \\(%d\\) đến \\(%d\\), tức là %d nhóm. Quá nhiều (hoặc quá ít) nhóm thì bảng khó đọc, khó nhận xét.' % (good, lo // good * good, (hi // good + 1) * good, ng(good)))


L24_GROUPS = [[('mcq', b24_member), ('mcq', b24_ngroups), ('mcq', b24_relgroup)], [('tf', b24_tf_count), ('tf', b24_tf_mid)], [('short', b24_short_missing), ('short', b24_short_below)],
              [('mcq', b24_d1_def), ('mcq', b24_d1_mode), ('mcq', b24_d1_sum)], [('mcq', b24_d2_raw), ('mcq', b24_d2_count), ('mcq', b24_d2_point)],
              [('mcq', b24_d3_line), ('mcq', b24_d3_bar), ('mcq', b24_d3_merge)], [('mcq', b24_d4_compare), ('mcq', b24_d4_speed), ('mcq', b24_d4_choose)]]


# =====================================================================================================
# BÀI 25. Phép thử ngẫu nhiên và không gian mẫu
# =====================================================================================================
COIN = {'en': ('H', 'T'), 'vi': ('N', 'S')}            # heads/ngửa, tails/sấp
SECT = ['86e0bd', 'fcd34d', '93c5fd', 'f9a8d4', 'c4b5fd', 'fdba74', 'a7f3d0', 'fca5a5']


def spinner_svg(labels, R=1.6):
    """Vòng quay chia đều thành len(labels) hình quạt, ghi nhãn ở giữa mỗi hình quạt, kim chỉ ở tâm."""
    k = len(labels); o = ['\\begin{tikzpicture}']
    for i, lab in enumerate(labels):
        a, b = 90 - 360 * i / k, 90 - 360 * (i + 1) / k
        o.append('\\fill[fill=%s, draw=white, line width=1pt] (0,0) -- (%.3f:%s) arc[start angle=%.3f, end angle=%.3f, radius=%scm] -- cycle;' % (col(SECT[i % 8]), a, R, a, b, R))
        o.append('\\node[font=\\bfseries, text=ink] at (%.3f:%.3f) {%s};' % ((a + b) / 2, R * 0.68, lab))
    o.append('\\draw[ink, line width=0.9pt] (0,0) circle (%s);' % R)
    o.append('\\draw[ink, line width=1.6pt, -{Stealth[length=3mm]}] (0,0) -- (%.3f:%.3f);' % (90 - 360 / k * 0.5 + 360 / k * 0.25 if k > 2 else 20, R * 0.42))
    o.append('\\fill[ink] (0,0) circle (2.2pt);')
    o.append('\\end{tikzpicture}')
    return texsvg('\n'.join(o))


def _w(t): return 0.2 + 0.165 * len(str(t))          # bề rộng ước lượng (cm) của nhãn cỡ \\small


def tree_svg(l1, l2, outs, head=None):
    """Sơ đồ hình cây hai tầng (nằm ngang). l1: nhãn tầng 1; l2: danh sách nhãn tầng 2 cho từng nhánh; outs: nhãn kết quả ở lá.
    Vị trí các cột tính theo bề rộng nhãn dài nhất để nét nối không đi qua chữ."""
    leaves = sum(len(x) for x in l2); dy = 0.62; H = (leaves - 1) * dy
    leaf_y = [H / 2 - dy * t for t in range(leaves)]; ycent = []; k = 0
    for sub in l2:
        ys = leaf_y[k:k + len(sub)]; k += len(sub); ycent.append(sum(ys) / len(ys))
    W1 = max(_w(a) for a in l1); W2 = max(_w(b) for sub in l2 for b in sub)
    x1 = 1.7; x2 = x1 + W1 + 1.3; x3 = x2 + W2 + 0.35
    if head:
        x2 = max(x2, x1 + max(W1, _w(head[0])) + 0.5); x3 = max(x3, x2 + max(W2, _w(head[1])) + 0.3)
    st1 = 'draw=%s, fill=white, rounded corners=2pt, inner sep=2pt, font=\\small, text=ink, anchor=west' % col('046b4d')
    st2 = 'draw=%s, fill=white, rounded corners=2pt, inner sep=2pt, font=\\small, text=ink, anchor=west' % col('c2410c')
    o = ['\\begin{tikzpicture}', '\\fill[ink] (0,0) circle (1.8pt);']
    k = 0
    for i, (a, sub) in enumerate(zip(l1, l2)):
        yc = ycent[i]
        o.append('\\node[%s] (a%d) at (%.3f,%.3f) {%s};' % (st1, i, x1, yc, a))
        o.append('\\draw[color=%s, line width=0.8pt] (0.08,0) -- (a%d.west);' % (col('046b4d'), i))
        for b in sub:
            yl = leaf_y[k]
            o.append('\\node[%s] (b%d) at (%.3f,%.3f) {%s};' % (st2, k, x2, yl, b))
            o.append('\\draw[color=%s, line width=0.8pt] (a%d.east) -- (b%d.west);' % (col('c2410c'), i, k))
            o.append('\\node[anchor=west, font=\\small, text=ink] at (%.3f,%.3f) {%s};' % (x3, yl, outs[k]))
            k += 1
    if head:
        yh = H / 2 + 0.62
        o.append('\\node[font=\\small\\bfseries, text=ink, anchor=west] at (%.3f,%.3f) {%s};' % (x1, yh, head[0]))
        o.append('\\node[font=\\small\\bfseries, text=ink, anchor=west] at (%.3f,%.3f) {%s};' % (x2, yh, head[1]))
        o.append('\\node[font=\\small\\bfseries, text=ink, anchor=west] at (%.3f,%.3f) {%s};' % (x3, yh, head[2]))
    o.append('\\end{tikzpicture}')
    return texsvg('\n'.join(o))


def TREE_Q(l1, l2, outs, head, px=420):
    """l1, l2, outs, head: cặp (en, vi) cho mỗi phần."""
    fe = tree_svg(l1[0], l2[0], outs[0], head[0]); fv = tree_svg(l1[1], l2[1], outs[1], head[1])
    return (img(fe, 'Tree diagram', px), img(fv, 'Sơ đồ hình cây', px))


def setx(xs):
    """Tập hợp kết quả viết bằng dấu chấm phẩy: {1; 2; 3}."""
    return '\\{%s\\}' % ';\\,'.join(str(x) for x in xs)


def pair(a, b): return '(%s;\\,%s)' % (a, b)


def gridtab(rows, cols, cell, head=('', '')):
    """Bảng hai chiều (không gian mẫu phép thử hai bước): hàng = kết quả bước 1, cột = kết quả bước 2."""
    def one(lang):
        h = '<tr><th scope="col">%s</th>%s</tr>' % (head[0] if lang == 'en' else head[1], ''.join('<th scope="col">%s</th>' % c for c in cols))
        b = ''.join('<tr><th scope="row">%s</th>%s</tr>' % (rw, ''.join('<td>%s</td>' % cell(rw, c) for c in cols)) for rw in rows)
        return '<div class="mbl-tablewrap mbl-freqwrap"><table class="mbl-table mbl-freq"><tbody>%s%s</tbody></table></div>' % (h, b)
    return (one('en'), one('vi'))


EXPS = [  # (en, vi, Ω_en, Ω_vi)
    ('toss a coin', 'gieo một đồng xu', setx(COIN['en']), setx(COIN['vi'])),
    ('roll a die', 'gieo một con xúc xắc', setx(range(1, 7)), setx(range(1, 7))),
]


RAND = [('rolling a die and reading the number on top', 'gieo một con xúc xắc và xem số chấm xuất hiện'),
        ('drawing a card without looking from a box of cards numbered 1 to 10', 'rút ngẫu nhiên một tấm thẻ từ hộp có 10 tấm thẻ đánh số từ 1 đến 10'),
        ('tossing a coin and seeing which side faces up', 'tung một đồng xu và xem mặt nào xuất hiện'),
        ('spinning a spinner with 5 equal sectors and reading the number', 'quay một vòng quay có 5 hình quạt bằng nhau và xem kim chỉ vào số nào'),
        ('choosing a student at random from class 9A and noting the month of birth', 'chọn ngẫu nhiên một học sinh lớp 9A và xem bạn đó sinh vào tháng nào')]
NRAND = [('counting the days in a week', 'đếm số ngày trong một tuần'), ('measuring the length of a 30 cm ruler', 'đo chiều dài một cây thước 30 cm'),
         ('adding 2 and 3', 'tính tổng của 2 và 3'), ('reading the date on a calendar', 'xem ngày hôm nay trên tờ lịch'),
         ('dropping a stone and seeing whether it falls down', 'thả một hòn đá và xem nó có rơi xuống không'), ('counting the corners of a square', 'đếm số góc của một hình vuông')]


def b25_random(r, lv):
    k = r.choice(['is', 'not'])
    if k == 'is':
        good = r.choice(RAND); o = [tx(*good)] + [tx(*b) for b in r.sample(NRAND, 3)]
        st = r.choice([('Which of the following is a random experiment?', 'Hoạt động nào sau đây là một phép thử ngẫu nhiên?'),
                       ('Which activity below is a random experiment?', 'Trong các hoạt động dưới đây, hoạt động nào là phép thử ngẫu nhiên?')])
    else:
        good = r.choice(NRAND); o = [tx(*good)] + [tx(*b) for b in r.sample(RAND, 3)]
        st = r.choice([('Which of the following is NOT a random experiment?', 'Hoạt động nào sau đây KHÔNG phải là phép thử ngẫu nhiên?'),
                       ('Which activity below is NOT a random experiment?', 'Trong các hoạt động dưới đây, hoạt động nào KHÔNG phải là phép thử ngẫu nhiên?')])
    return dict(en=st[0], vi=st[1], opts=o, ans=0,
                ee='In a random experiment we cannot know the outcome in advance, but we know all the possible outcomes. Answer: %s.' % good[0],
                ev='Phép thử ngẫu nhiên: không biết trước kết quả nhưng biết tất cả các kết quả có thể. Đáp án: %s.' % good[1])


CARDS = [('cards', 'tấm thẻ'), ('balls', 'quả bóng'), ('tickets', 'lá phiếu')]


def b25_omega(r, lv):
    k = r.choice(['coin', 'die', 'box', 'spin'])
    if k == 'coin':
        en, vi = 'A coin is tossed once (H: heads, T: tails). The sample space is…', 'Gieo một đồng xu một lần (N: mặt ngửa, S: mặt sấp). Không gian mẫu là…'
        g = (setx('HT'), setx('NS')); bad = [(setx('H'), setx('N')), (setx(['HT']), setx(['NS'])), (setx(['HH', 'HT', 'TH', 'TT']), setx(['NN', 'NS', 'SN', 'SS']))]
    elif k == 'die':
        en, vi = 'A die is rolled once. The sample space is…', 'Gieo một con xúc xắc một lần. Không gian mẫu là…'
        g = (setx(range(1, 7)),) * 2; bad = [(setx(range(0, 7)),) * 2, (setx(range(1, 6)),) * 2, (setx([2, 4, 6]),) * 2]
    elif k == 'box':
        n = r.randint(4, 9); a = r.choice([1, 1, 10, 20]); it = r.choice(CARDS)
        en, vi = 'A box has %d %s numbered %s. One is taken at random. The sample space is…' % (n, it[0], ', '.join(str(a + i) for i in range(n))), \
                 'Một hộp có %d %s đánh số %s. Lấy ngẫu nhiên một %s. Không gian mẫu là…' % (n, it[1], ', '.join(str(a + i) for i in range(n)), it[1].split()[-1] if False else it[1])
        g = (setx(range(a, a + n)),) * 2; bad = [(setx(range(a, a + n - 1)),) * 2, (setx(range(a + 1, a + n + 1)),) * 2, (setx([n]),) * 2]
    else:
        n = r.randint(3, 8)
        en, vi = 'A spinner has %d equal sectors numbered 1 to %d. It is spun once. The sample space is…' % (n, n), 'Một vòng quay có %d hình quạt bằng nhau đánh số từ 1 đến %d. Quay một lần. Không gian mẫu là…' % (n, n)
        g = (setx(range(1, n + 1)),) * 2; bad = [(setx(range(0, n + 1)),) * 2, (setx(range(1, n)),) * 2, (setx([n]),) * 2]
    o = [tx('\\(\\Omega=%s\\)' % g[0], '\\(\\Omega=%s\\)' % g[1])] + [tx('\\(\\Omega=%s\\)' % b[0], '\\(\\Omega=%s\\)' % b[1]) for b in bad]
    return dict(en=en, vi=vi, opts=o, ans=0, ee='\\(\\Omega\\) is the set of all possible outcomes: \\(\\Omega=%s\\).' % g[0], ev='\\(\\Omega\\) là tập hợp tất cả các kết quả có thể: \\(\\Omega=%s\\).' % g[1])


def b25_count2(r, lv):
    k = r.choice(['2coin', 'coindie', '2dice', 'menu', 'spin2'])
    if k == '2coin': n = 4; en, vi = 'Two coins are tossed together. How many outcomes does the sample space have?', 'Gieo đồng thời hai đồng xu. Không gian mẫu có bao nhiêu kết quả?'; bad = [2, 3, 8]; why = '2\\cdot2=4'
    elif k == 'coindie': n = 12; en, vi = 'A coin is tossed and a die is rolled. How many outcomes does the sample space have?', 'Gieo một đồng xu và một con xúc xắc. Không gian mẫu có bao nhiêu kết quả?'; bad = [8, 6, 36]; why = '2\\cdot6=12'
    elif k == '2dice': n = 36; en, vi = 'Two dice are rolled together. How many outcomes does the sample space have?', 'Gieo đồng thời hai con xúc xắc. Không gian mẫu có bao nhiêu kết quả?'; bad = [12, 21, 11]; why = '6\\cdot6=36'
    elif k == 'menu':
        a, b = r.randint(2, 5), r.randint(2, 5); n = a * b; bad = [a + b, n + 1, max(a, b)]; why = '%d\\cdot%d=%d' % (a, b, n)
        en, vi = 'A canteen offers %d main dishes and %d drinks. Minh chooses one main dish and one drink at random. How many outcomes are there?' % (a, b), 'Căng tin có %d món chính và %d loại đồ uống. Minh chọn ngẫu nhiên một món chính và một loại đồ uống. Có bao nhiêu kết quả có thể?' % (a, b)
    else:
        a, b = r.randint(3, 6), r.randint(2, 5); n = a * b; bad = [a + b, n - 1, a * a]; why = '%d\\cdot%d=%d' % (a, b, n)
        en, vi = 'Spinner A has %d equal sectors and spinner B has %d equal sectors. Both are spun once. How many outcomes does the sample space have?' % (a, b), 'Vòng quay A có %d hình quạt bằng nhau, vòng quay B có %d hình quạt bằng nhau. Quay mỗi vòng một lần. Không gian mẫu có bao nhiêu kết quả?' % (a, b)
    return dict(en=en, vi=vi, opts=iopts(r, n, bad), ans=0, ee='Each outcome is an ordered pair: \\(%s\\) outcomes.' % why, ev='Mỗi kết quả là một cặp có thứ tự: có \\(%s\\) kết quả.' % why)


def b25_tf_pair(r, lv):
    n = r.randint(4, 7); a = r.randint(1, n); same = r.random() < 0.5
    b = a if same else r.choice([x for x in range(1, n + 1) if x != a])
    rep = r.random() < 0.5
    truth = (not same) or rep
    en = 'A box has %d cards numbered 1 to %d. Draw one card, %s, then draw a second card. The outcome \\(%s\\) belongs to the sample space.' % (n, n, 'put it back' if rep else 'do not put it back', pair(a, b))
    vi = 'Một hộp có %d tấm thẻ đánh số từ 1 đến %d. Rút một thẻ, %s, rồi rút thẻ thứ hai. Kết quả \\(%s\\) thuộc không gian mẫu.' % (n, n, 'trả lại hộp' if rep else 'không trả lại hộp', pair(a, b))
    if rep: ee, ev = 'The card is put back, so the two numbers can be equal or different: \\(%s\\in\\Omega\\).' % pair(a, b), 'Thẻ được trả lại nên hai số có thể bằng nhau hoặc khác nhau: \\(%s\\in\\Omega\\).' % pair(a, b)
    elif same: ee, ev = 'Without putting back, the two cards are different, so \\(%s\\notin\\Omega\\).' % pair(a, b), 'Không trả lại nên hai thẻ khác nhau, do đó \\(%s\\notin\\Omega\\).' % pair(a, b)
    else: ee, ev = 'Two different cards: \\(%s\\in\\Omega\\).' % pair(a, b), 'Hai thẻ khác nhau: \\(%s\\in\\Omega\\).' % pair(a, b)
    return dict(en=en, vi=vi, ans=truth, ee=ee, ev=ev)


def b25_tf_noreplace(r, lv):
    n = r.randint(3, 7); rep = r.random() < 0.5; good = n * n if rep else n * (n - 1)
    truth = r.random() < 0.5; claim = good if truth else (n * (n - 1) if rep else n * n)
    return dict(en='A bag has %d balls numbered 1 to %d. Take one ball, %s, then take a second ball. The sample space has %d outcomes.' % (n, n, 'put it back' if rep else 'do not put it back', claim),
                vi='Một túi có %d quả bóng đánh số từ 1 đến %d. Lấy một quả, %s, rồi lấy quả thứ hai. Không gian mẫu có %d kết quả.' % (n, n, 'trả lại túi' if rep else 'không trả lại túi', claim),
                ans=truth, ee='%s: \\(%d\\cdot%d=%d\\) ordered pairs.' % ('With replacement' if rep else 'Without replacement', n, n if rep else n - 1, good),
                ev='%s: có \\(%d\\cdot%d=%d\\) cặp có thứ tự.' % ('Có trả lại' if rep else 'Không trả lại', n, n if rep else n - 1, good))


def b25_short_menu(r, lv):
    a, b, c = r.randint(2, 4), r.randint(2, 4), r.randint(2, 3)
    n = a * b * c
    return dict(en='A set lunch: choose one of %d rice dishes, one of %d soups and one of %d fruits. A student chooses at random. How many outcomes does the sample space have?' % (a, b, c),
                vi='Một suất ăn trưa gồm: một trong %d món cơm, một trong %d món canh và một trong %d loại trái cây. Một học sinh chọn ngẫu nhiên. Không gian mẫu có bao nhiêu kết quả?' % (a, b, c),
                key=str(n), ee='Three steps: \\(%d\\cdot%d\\cdot%d=%d\\).' % (a, b, c, n), ev='Ba bước chọn: \\(%d\\cdot%d\\cdot%d=%d\\).' % (a, b, c, n))


NAMES = ['An', 'Chi', 'Lan', 'Minh', 'Nam', 'Khoa']


def b25_short_pairs(r, lv):
    k = r.randint(4, 6); nm = NAMES[:k]; n = k * (k - 1) // 2
    return dict(en='The teacher chooses at random 2 of the %d students %s to clean the board (the order does not matter). How many outcomes does the sample space have?' % (k, ', '.join(nm)),
                vi='Cô giáo chọn ngẫu nhiên 2 trong %d bạn %s để lau bảng (không phân biệt thứ tự). Không gian mẫu có bao nhiêu kết quả?' % (k, ', '.join(nm)),
                key=str(n), ee='List the pairs: %s… In total \\(%s=%d\\).' % (', '.join('%s–%s' % (nm[0], x) for x in nm[1:]), '+'.join(str(i) for i in range(k - 1, 0, -1)), n),
                ev='Liệt kê các cặp: %s… Tổng cộng \\(%s=%d\\).' % (', '.join('%s–%s' % (nm[0], x) for x in nm[1:]), '+'.join(str(i) for i in range(k - 1, 0, -1)), n))


def b25_d1_term(r, lv):
    k = r.choice(['omega', 'outcome', 'pair'])
    if k == 'omega':
        o = [tx('the set of all possible outcomes', 'tập hợp tất cả các kết quả có thể'), tx('the outcome that happens', 'kết quả xảy ra'), tx('the number of times we do the experiment', 'số lần thực hiện phép thử'), tx('one possible outcome', 'một kết quả có thể')]
        return dict(en='The sample space \\(\\Omega\\) of a random experiment is…', vi='Không gian mẫu \\(\\Omega\\) của một phép thử ngẫu nhiên là…', opts=o, ans=0, ee='Definition of the sample space.', ev='Định nghĩa không gian mẫu.')
    if k == 'outcome':
        o = [tx('we do not know the outcome in advance, but we know all possible outcomes', 'không biết trước kết quả nhưng biết tất cả các kết quả có thể'),
             tx('we know the outcome in advance', 'biết trước kết quả'), tx('there is only one possible outcome', 'chỉ có một kết quả có thể'), tx('we do not know any possible outcome', 'không biết được kết quả có thể nào')]
        return dict(en='An experiment is called random when…', vi='Một phép thử được gọi là phép thử ngẫu nhiên khi…', opts=o, ans=0, ee='Definition of a random experiment.', ev='Định nghĩa phép thử ngẫu nhiên.')
    o = [tx('\\((2;\\,5)\\) and \\((5;\\,2)\\) are different outcomes', '\\((2;\\,5)\\) và \\((5;\\,2)\\) là hai kết quả khác nhau'), tx('\\((2;\\,5)\\) and \\((5;\\,2)\\) are the same outcome', '\\((2;\\,5)\\) và \\((5;\\,2)\\) là cùng một kết quả'),
         tx('\\((5;\\,2)\\) is not an outcome', '\\((5;\\,2)\\) không phải là kết quả có thể'), tx('the sample space has 12 outcomes', 'không gian mẫu có 12 kết quả')]
    return dict(en='A red die and a blue die are rolled; an outcome \\((a;\\,b)\\) means \\(a\\) on the red die and \\(b\\) on the blue die. Which statement is correct?', vi='Gieo một con xúc xắc đỏ và một con xúc xắc xanh; kết quả \\((a;\\,b)\\) nghĩa là xúc xắc đỏ ra \\(a\\) chấm, xúc xắc xanh ra \\(b\\) chấm. Khẳng định nào đúng?',
                opts=o, ans=0, ee='The order matters: red 2 – blue 5 differs from red 5 – blue 2; \\(n(\\Omega)=36\\).', ev='Có phân biệt thứ tự: đỏ 2 – xanh 5 khác đỏ 5 – xanh 2; không gian mẫu có 36 kết quả.')


def b25_d1_spin(r, lv):
    k = r.randint(3, 8); start = r.choice([1, 1, 2, 5, 10]); step = r.choice([1, 1, 2, 5])
    labs = [start + step * i for i in range(k)]
    fn = spinner_svg([str(x) for x in labs])
    o = [setx(labs), setx(labs[:-1]), setx(range(1, k + 1)) if labs != list(range(1, k + 1)) else setx(range(0, k)), setx([k])]
    return dict(en='The spinner in the figure has %d equal sectors. It is spun once and we read the number where the arrow stops. The sample space is…' % k, vi='Vòng quay trong hình có %d hình quạt bằng nhau. Quay một lần và đọc số mà kim chỉ vào khi dừng. Không gian mẫu là…' % k,
                opts=['\\Omega=%s' % x for x in o], ans=0, ee='All numbers on the spinner: \\(\\Omega=%s\\).' % setx(labs), ev='Tất cả các số trên vòng quay: \\(\\Omega=%s\\).' % setx(labs),
                fig=(img(fn, 'Spinner', 260), img(fn, 'Vòng quay', 260)))


def b25_d1_notout(r, lv):
    k = r.choice(['2coin', 'coindie', '2dice'])
    if k == '2coin':
        good = ('HHT', 'NNS'); oth = [('HT', 'NS'), ('TT', 'SS'), ('TH', 'SN')]
        en, vi = 'Two coins are tossed (H: heads, T: tails). Which of the following is NOT an outcome?', 'Gieo hai đồng xu (N: ngửa, S: sấp). Kết quả nào sau đây KHÔNG thuộc không gian mẫu?'
        ee, ev = 'Each outcome has exactly two letters (one per coin).', 'Mỗi kết quả gồm đúng hai chữ cái (ứng với hai đồng xu).'
    elif k == 'coindie':
        good = ('(H;\\,7)', '(N;\\,7)'); oth = [('(H;\\,6)', '(N;\\,6)'), ('(T;\\,1)', '(S;\\,1)'), ('(T;\\,4)', '(S;\\,4)')]
        en, vi = 'A coin is tossed and a die is rolled (H: heads, T: tails). Which of the following is NOT an outcome?', 'Gieo một đồng xu và một con xúc xắc (N: ngửa, S: sấp). Kết quả nào sau đây KHÔNG thuộc không gian mẫu?'
        ee, ev = 'A die has only the numbers 1 to 6.', 'Con xúc xắc chỉ có từ 1 đến 6 chấm.'
    else:
        a = r.randint(1, 5); bad = r.choice([pair(a, 0), pair(7, a), pair(0, a + 1), pair(a, 8)]); good = (bad,) * 2; oth = [(pair(a, 6),) * 2, (pair(6, a),) * 2, (pair(a + 1, a + 1),) * 2]
        en, vi = 'Two dice are rolled. Which of the following is NOT an outcome?', 'Gieo hai con xúc xắc. Kết quả nào sau đây KHÔNG thuộc không gian mẫu?'
        ee, ev = 'Each die shows a number from 1 to 6.', 'Mỗi con xúc xắc ra từ 1 đến 6 chấm.'
    o = [tx('\\(%s\\)' % good[0], '\\(%s\\)' % good[1])] + [tx('\\(%s\\)' % x[0], '\\(%s\\)' % x[1]) for x in oth]
    return dict(en=en, vi=vi, opts=o, ans=0, ee=ee, ev=ev)


FOODS = [('rice', 'cơm'), ('noodles', 'mì'), ('bread', 'bánh mì'), ('pho', 'phở')]
DRINKS = [('milk', 'sữa'), ('juice', 'nước ép'), ('tea', 'trà'), ('water', 'nước lọc')]


def b25_d2_tree(r, lv):
    a = r.randint(2, 3); b = r.randint(2, 3)
    F1 = r.sample(FOODS, a); D1 = r.sample(DRINKS, b)
    outs = [[(f[0] + ', ' + d[0]) for f in F1 for d in D1], [(f[1] + ', ' + d[1]) for f in F1 for d in D1]]
    fig = TREE_Q(([f[0] for f in F1], [f[1] for f in F1]), ([[d[0] for d in D1]] * a, [[d[1] for d in D1]] * a), outs,
                 (('Food', 'Drink', 'Outcome'), ('Món ăn', 'Đồ uống', 'Kết quả')))
    n = a * b; ask = r.choice(['n', 'has']); who = r.choice(['Lan', 'Minh', 'Hoa', 'Nam'])
    if ask == 'n':
        return dict(en='The tree diagram shows how %s chooses breakfast at random. How many outcomes does the sample space have?' % who, vi='Sơ đồ hình cây cho biết cách %s chọn ngẫu nhiên bữa sáng. Không gian mẫu có bao nhiêu kết quả?' % who,
                    opts=iopts(r, n, [a + b, n + 1, a]), ans=0, ee='Count the branches at the end: \\(%d\\cdot%d=%d\\).' % (a, b, n), ev='Đếm số nhánh cuối: \\(%d\\cdot%d=%d\\).' % (a, b, n), fig=fig)
    f = r.choice(F1); n2 = b
    return dict(en='The tree diagram shows how %s chooses breakfast at random. How many outcomes contain %s?' % (who, f[0]), vi='Sơ đồ hình cây cho biết cách %s chọn ngẫu nhiên bữa sáng. Có bao nhiêu kết quả có món %s?' % (who, f[1]),
                opts=iopts(r, n2, [n, 1, n2 + 1]), ans=0, ee='The branch “%s” has %d drinks after it.' % (f[0], b), ev='Nhánh “%s” có %d nhánh đồ uống.' % (f[1], b), fig=fig)


def b25_d2_desc(r, lv):
    n = r.randint(2, 4); cols = r.sample([('red', 'đỏ', 'R', 'Đ'), ('blue', 'xanh', 'B', 'X'), ('yellow', 'vàng', 'Y', 'V'), ('white', 'trắng', 'W', 'T')], n)
    c1 = setx(['(%s;\\,%s)' % (c[2], s) for c in cols for s in COIN['en']]); c1v = setx(['(%s;\\,%s)' % (c[3], s) for c in cols for s in COIN['vi']])
    w1 = setx([c[2] for c in cols] + list(COIN['en'])); w1v = setx([c[3] for c in cols] + list(COIN['vi']))
    w2 = setx(['(%s;\\,%s)' % (c[2], 'H') for c in cols]); w2v = setx(['(%s;\\,%s)' % (c[3], 'N') for c in cols])
    w3 = setx(['(%s;\\,%s)' % (s, c[2]) for s in COIN['en'] for c in cols][:n * 2 - 1]); w3v = setx(['(%s;\\,%s)' % (s, c[3]) for s in COIN['vi'] for c in cols][:n * 2 - 1])
    o = [tx('\\(\\Omega=%s\\)' % c1, '\\(\\Omega=%s\\)' % c1v), tx('\\(\\Omega=%s\\)' % w1, '\\(\\Omega=%s\\)' % w1v), tx('\\(\\Omega=%s\\)' % w2, '\\(\\Omega=%s\\)' % w2v), tx('\\(\\Omega=%s\\)' % w3, '\\(\\Omega=%s\\)' % w3v)]
    return dict(en='A bag has %d balls: %s (one of each color). Take one ball at random, then toss a coin (H: heads, T: tails). Which is the sample space?' % (n, ', '.join('%s (%s)' % (c[0], c[2]) for c in cols)),
                vi='Một túi có %d quả bóng: %s (mỗi màu một quả). Lấy ngẫu nhiên một quả bóng rồi gieo một đồng xu (N: ngửa, S: sấp). Không gian mẫu là…' % (n, ', '.join('%s (%s)' % (c[1], c[3]) for c in cols)),
                opts=o, ans=0, ee='Each outcome is a pair (ball; coin): \\(%d\\cdot2=%d\\) outcomes.' % (n, 2 * n), ev='Mỗi kết quả là một cặp (bóng; đồng xu): có \\(%d\\cdot2=%d\\) kết quả.' % (n, 2 * n))


def b25_d2_repl(r, lv):
    n = r.randint(3, 6); rep = r.random() < 0.5; good = n * n if rep else n * (n - 1)
    it = r.choice([('cards numbered 1 to %d' % n, '%d tấm thẻ đánh số từ 1 đến %d' % (n, n)), ('pens of %d different colors' % n, '%d chiếc bút có màu khác nhau' % n)])
    return dict(en='A box contains %s. Take one, %s, then take one more. How many outcomes does the sample space have (the order matters)?' % (it[0], 'put it back' if rep else 'keep it out'),
                vi='Một hộp có %s. Lấy ra một chiếc, %s, rồi lấy tiếp một chiếc nữa. Không gian mẫu có bao nhiêu kết quả (có phân biệt thứ tự)?' % (it[1], 'trả lại hộp' if rep else 'không trả lại'),
                opts=iopts(r, good, [n * (n - 1) if rep else n * n, 2 * n, n * (n - 1) // 2]), ans=0,
                ee='%d choices for the first and %d for the second: \\(%d\\cdot%d=%d\\).' % (n, n if rep else n - 1, n, n if rep else n - 1, good),
                ev='Lần đầu có %d cách, lần sau có %d cách: \\(%d\\cdot%d=%d\\).' % (n, n if rep else n - 1, n, n if rep else n - 1, good))


def b25_d3_code(r, lv):
    L = r.choice([['A', 'B'], ['A', 'B', 'C'], ['X', 'Y', 'Z']]); d = r.randint(3, 6)
    n = len(L) * d
    return dict(en='A locker code has one letter from %s followed by one digit from 1 to %d. A code is chosen at random. How many outcomes are there? Give one example.' % (', '.join(L), d),
                vi='Mã khóa tủ gồm một chữ cái trong các chữ %s, theo sau là một chữ số từ 1 đến %d. Chọn ngẫu nhiên một mã. Có bao nhiêu kết quả có thể? Nêu một ví dụ.' % (', '.join(L), d),
                opts=[tx('%d outcomes, e.g. %s%d' % (n, L[-1], d), '%d kết quả, ví dụ %s%d' % (n, L[-1], d)), tx('%d outcomes, e.g. %s%d' % (len(L) + d, L[0], 1), '%d kết quả, ví dụ %s%d' % (len(L) + d, L[0], 1)),
                      tx('%d outcomes, e.g. %d%s' % (n, d, L[0]), '%d kết quả, ví dụ %d%s' % (n, d, L[0])), tx('%d outcomes, e.g. %s%d' % (n, L[0], d + 1), '%d kết quả, ví dụ %s%d' % (n, L[0], d + 1))], ans=0,
                ee='\\(%d\\cdot%d=%d\\) codes; the letter comes first and the digit is from 1 to %d.' % (len(L), d, n, d), ev='\\(%d\\cdot%d=%d\\) mã; chữ cái đứng trước, chữ số từ 1 đến %d.' % (len(L), d, n, d))


def b25_d3_grid(r, lv):
    a, b = r.randint(2, 4), r.randint(3, 5)
    rows = ['%d' % i for i in range(1, a + 1)]; cols = [chr(65 + j) for j in range(b)]
    i, j = r.randrange(a), r.randrange(b)
    def cell(rw, c): return '?' if (rw, c) == (rows[i], cols[j]) else '\\((%s;\\,%s)\\)' % (rw, c)
    fig = gridtab(rows, cols, cell, ('Spinner 1 \\ Spinner 2', 'Vòng 1 \\ Vòng 2'))
    good = '\\((%s;\\,%s)\\)' % (rows[i], cols[j])
    o = [good, '\\((%s;\\,%s)\\)' % (cols[j], rows[i]), '\\((%s;\\,%s)\\)' % (rows[(i + 1) % a], cols[j]), '\\((%s;\\,%s)\\)' % (rows[i], cols[(j + 1) % b])]
    return dict(en='Spinner 1 has the numbers 1 to %d and spinner 2 has the letters %s. The table lists the sample space of spinning both (%d outcomes). Which outcome is hidden by “?”?' % (a, ', '.join(cols), a * b),
                vi='Vòng quay 1 có các số từ 1 đến %d, vòng quay 2 có các chữ %s. Bảng dưới liệt kê không gian mẫu khi quay cả hai vòng (%d kết quả). Ô “?” là kết quả nào?' % (a, ', '.join(cols), a * b),
                opts=['§' + x for x in o], ans=0, ee='Row %s and column %s: %s.' % (rows[i], cols[j], good), ev='Hàng %s, cột %s: %s.' % (rows[i], cols[j], good), fig=fig)


def b25_d3_power(r, lv):
    k = r.choice([('three coins are tossed', 'gieo ba đồng xu', 3), ('a family has three children (B: boy, G: girl, in order of birth)', 'một gia đình có ba con (T: trai, G: gái, theo thứ tự sinh)', 3),
                  ('a coin is tossed four times', 'gieo một đồng xu bốn lần', 4), ('a family has two children (B: boy, G: girl, in order of birth)', 'một gia đình có hai con (T: trai, G: gái, theo thứ tự sinh)', 2)])
    n = 2 ** k[2]
    return dict(en='Use a tree diagram: when %s, how many outcomes does the sample space have?' % k[0], vi='Dùng sơ đồ hình cây: khi %s, không gian mẫu có bao nhiêu kết quả?' % k[1],
                opts=iopts(r, n, [2 * k[2], k[2] + 1, n * 2 if n < 16 else n - 2]), ans=0,
                ee='Each step doubles the branches: \\(2^{%d}=%d\\).' % (k[2], n), ev='Mỗi bước nhân đôi số nhánh: \\(2^{%d}=%d\\).' % (k[2], n))


def b25_d4_code2(r, lv):
    L = r.randint(2, 3); D = r.randint(3, 5)
    n = L * D * (D - 1)
    return dict(en='A security code is one letter (from %d letters) followed by two DIFFERENT digits chosen from %s. A code is chosen at random. How many outcomes does the sample space have?' % (L, ', '.join(str(i) for i in range(1, D + 1))),
                vi='Mã bảo mật gồm một chữ cái (trong %d chữ cái) theo sau là hai chữ số KHÁC NHAU lấy từ %s. Chọn ngẫu nhiên một mã. Không gian mẫu có bao nhiêu kết quả?' % (L, ', '.join(str(i) for i in range(1, D + 1))),
                opts=iopts(r, n, [L * D * D, L + D + D - 1, L * D]), ans=0,
                ee='Tree diagram: %d letters, then %d digits, then %d digits: \\(%d\\cdot%d\\cdot%d=%d\\).' % (L, D, D - 1, L, D, D - 1, n), ev='Sơ đồ hình cây: %d chữ cái, rồi %d chữ số, rồi %d chữ số: \\(%d\\cdot%d\\cdot%d=%d\\).' % (L, D, D - 1, L, D, D - 1, n))


def b25_d4_league(r, lv):
    k = r.randint(4, 7); n = k * (k - 1) // 2
    return dict(en='%d teams play a football tournament; every two teams play each other exactly once. A reporter chooses one match at random to write about. How many outcomes does the sample space have?' % k,
                vi='%d đội bóng thi đấu vòng tròn một lượt (hai đội bất kì gặp nhau đúng một lần). Một phóng viên chọn ngẫu nhiên một trận để viết bài. Không gian mẫu có bao nhiêu kết quả?' % k,
                opts=iopts(r, n, [k * (k - 1), k * k, k]), ans=0, ee='The matches are the unordered pairs of teams: \\(\\dfrac{%d\\cdot%d}{2}=%d\\).' % (k, k - 1, n), ev='Mỗi trận ứng với một cặp đội không phân biệt thứ tự: \\(\\dfrac{%d\\cdot%d}{2}=%d\\).' % (k, k - 1, n))


def b25_d4_branch(r, lv):
    s = r.randint(3, 6)
    n = 6 + s
    return dict(en='Toss a coin. If it shows heads, roll a die; if it shows tails, spin a spinner with %d equal sectors numbered 1 to %d. How many outcomes does the sample space have?' % (s, s),
                vi='Gieo một đồng xu. Nếu được mặt ngửa thì gieo tiếp một con xúc xắc; nếu được mặt sấp thì quay một vòng quay có %d hình quạt bằng nhau đánh số từ 1 đến %d. Không gian mẫu có bao nhiêu kết quả?' % (s, s),
                opts=iopts(r, n, [2 * 6 * s // 2 if 6 * s // 2 != n else 6 * s, 2 * 6, 2 * s]), ans=0,
                ee='Tree diagram: the heads branch has 6 outcomes, the tails branch has %d: \\(6+%d=%d\\).' % (s, s, n), ev='Sơ đồ hình cây: nhánh ngửa có 6 kết quả, nhánh sấp có %d kết quả: \\(6+%d=%d\\).' % (s, s, n))


L25_GROUPS = [[('mcq', b25_random), ('mcq', b25_omega), ('mcq', b25_count2)], [('tf', b25_tf_pair), ('tf', b25_tf_noreplace)], [('short', b25_short_menu), ('short', b25_short_pairs)],
              [('mcq', b25_d1_term), ('mcq', b25_d1_spin), ('mcq', b25_d1_notout)], [('mcq', b25_d2_tree), ('mcq', b25_d2_desc), ('mcq', b25_d2_repl)],
              [('mcq', b25_d3_code), ('mcq', b25_d3_grid), ('mcq', b25_d3_power)], [('mcq', b25_d4_code2), ('mcq', b25_d4_league), ('mcq', b25_d4_branch)]]


# =====================================================================================================
# BÀI 26. Xác suất của biến cố liên quan tới phép thử
# =====================================================================================================
def frt(x):
    """Phân số tối giản dạng TeX."""
    x = F(x)
    if x.denominator == 1: return str(x.numerator)
    return '\\dfrac{%d}{%d}' % (x.numerator, x.denominator)


def fexp(k, n):
    """\\dfrac{k}{n} (=rút gọn)."""
    s = '\\dfrac{%d}{%d}' % (k, n)
    return s if F(k, n) == F(k, n).numerator and n == 1 or (F(k, n).denominator == n) else s + '=' + frt(F(k, n))


def fopts(r, good, bads):
    good = F(good); o = [frt(good)]
    for b in bads:
        b = F(b)
        if 0 <= b <= 1 and frt(b) not in o: o.append(frt(b))
        if len(o) == 4: break
    k = 1
    while len(o) < 4:
        for c in (good + F(1, good.denominator * k), good - F(1, good.denominator * k) if good > F(1, good.denominator * k) else F(1, 2 * good.denominator + k), F(1, k + 1)):
            if 0 < c <= 1 and frt(c) not in o and len(o) < 4: o.append(frt(c))
        k += 1
    return o


DIE_EV = [('an even number', 'số chấm chẵn', lambda x: x % 2 == 0), ('an odd number', 'số chấm lẻ', lambda x: x % 2 == 1),
          ('a number greater than 4', 'số chấm lớn hơn 4', lambda x: x > 4), ('a number less than 3', 'số chấm nhỏ hơn 3', lambda x: x < 3),
          ('a multiple of 3', 'số chấm là bội của 3', lambda x: x % 3 == 0), ('a prime number', 'số chấm là số nguyên tố', lambda x: x in (2, 3, 5)),
          ('a number at least 2', 'số chấm không nhỏ hơn 2', lambda x: x >= 2), ('a divisor of 6', 'số chấm là ước của 6', lambda x: 6 % x == 0)]
PRIMES = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}


def b26_die(r, lv):
    e = r.choice(DIE_EV); A = [x for x in range(1, 7) if e[2](x)]; k = len(A)
    return dict(en='A fair die is rolled once. Find the probability that it shows %s.' % e[0], vi='Gieo một con xúc xắc cân đối một lần. Tính xác suất của biến cố “%s”.' % (e[1][0].upper() + e[1][1:]),
                opts=fopts(r, F(k, 6), [F(1, 6), F(k, 5), F(6 - k, 6), F(1, k)]), ans=0,
                ee='Favorable outcomes: %s, so \\(P=%s\\).' % (', '.join(map(str, A)), fexp(k, 6)), ev='Các kết quả thuận lợi: %s, nên \\(P=%s\\).' % (', '.join(map(str, A)), fexp(k, 6)))


def b26_cards(r, lv):
    n = r.choice([10, 12, 15, 20, 25, 30]); k = r.choice(['mult', 'prime', 'sq'])
    if k == 'mult':
        d = r.choice([3, 4, 5]); A = [x for x in range(1, n + 1) if x % d == 0]; ee = 'multiples of %d' % d; ev = 'bội của %d' % d
        en, vi = 'a multiple of %d' % d, 'là bội của %d' % d
    elif k == 'prime':
        A = [x for x in range(1, n + 1) if x in PRIMES]; en, vi = 'a prime number', 'là số nguyên tố'; ee, ev = 'prime numbers', 'số nguyên tố'
    else:
        A = [x * x for x in range(1, 6) if x * x <= n]; en, vi = 'a perfect square', 'là số chính phương'; ee, ev = 'perfect squares', 'số chính phương'
    m = len(A)
    return dict(en='A box has %d cards numbered 1 to %d. One card is drawn at random. What is the probability that its number is %s?' % (n, n, en),
                vi='Một hộp có %d tấm thẻ đánh số từ 1 đến %d. Rút ngẫu nhiên một thẻ. Tính xác suất để số trên thẻ %s.' % (n, n, vi),
                opts=fopts(r, F(m, n), [F(m + 1, n), F(n - m, n), F(1, m), F(m, n - 1)]), ans=0,
                ee='\\(n(\\Omega)=%d\\); %s: %s (%d cards); \\(P=%s\\).' % (n, ee, ', '.join(map(str, A)), m, fexp(m, n)), ev='\\(n(\\Omega)=%d\\); các %s: %s (%d thẻ); \\(P=%s\\).' % (n, ev, ', '.join(map(str, A)), m, fexp(m, n)))


COLS = [('red', 'đỏ'), ('blue', 'xanh'), ('yellow', 'vàng'), ('white', 'trắng'), ('green', 'xanh lá')]


def b26_bag(r, lv):
    cs = r.sample(COLS[:4], 3); ns = [r.randint(2, 9) for _ in cs]; n = sum(ns); i = r.randrange(3)
    return dict(en='A bag has %s balls of the same size. One ball is taken at random. Find the probability that it is %s.' % (', '.join('%d %s' % (a, c[0]) for a, c in zip(ns, cs)), cs[i][0]),
                vi='Một túi có %s; các quả bóng có cùng kích thước. Lấy ngẫu nhiên một quả. Tính xác suất lấy được quả bóng màu %s.' % (', '.join('%d quả bóng %s' % (a, c[1]) for a, c in zip(ns, cs)), cs[i][1]),
                opts=fopts(r, F(ns[i], n), [F(ns[i], n - ns[i]), F(1, 3), F(n - ns[i], n), F(ns[i], 10)]), ans=0,
                ee='\\(n(\\Omega)=%d\\), favorable: %d; \\(P=%s\\).' % (n, ns[i], fexp(ns[i], n)), ev='\\(n(\\Omega)=%d\\), số kết quả thuận lợi: %d; \\(P=%s\\).' % (n, ns[i], fexp(ns[i], n)))


def b26_tf_coins(r, lv):
    k = r.choice(['atleast', 'same', 'two', 'none'])
    E = {'atleast': ('at least one coin shows heads', 'có ít nhất một đồng xu ngửa', F(3, 4)), 'same': ('the two coins show the same side', 'hai đồng xu cùng mặt', F(1, 2)),
         'two': ('both coins show heads', 'cả hai đồng xu đều ngửa', F(1, 4)), 'none': ('no coin shows heads', 'không có đồng xu nào ngửa', F(1, 4))}[k]
    truth = r.random() < 0.5; claim = E[2] if truth else r.choice([x for x in (F(1, 3), F(2, 3), F(1, 2), F(3, 4), F(1, 4)) if x != E[2]])
    return dict(en='Two fair coins are tossed. The probability that %s is \\(%s\\).' % (E[0], frt(claim)), vi='Gieo hai đồng xu cân đối. Xác suất của biến cố “%s” bằng \\(%s\\).' % (E[1][0].upper() + E[1][1:], frt(claim)),
                ans=truth, ee='\\(\\Omega=\\{HH;\\,HT;\\,TH;\\,TT\\}\\) (4 equally likely outcomes): \\(P=%s\\).' % frt(E[2]), ev='\\(\\Omega=\\{NN;\\,NS;\\,SN;\\,SS\\}\\) (4 kết quả đồng khả năng): \\(P=%s\\).' % frt(E[2]))


def dsum(s): return [(i, j) for i in range(1, 7) for j in range(1, 7) if i + j == s]


def b26_tf_sum(r, lv):
    s = r.randint(3, 11); k = len(dsum(s)); truth = r.random() < 0.5; claim = k if truth else r.choice([k + 1, k - 1 if k > 1 else k + 2, s - 1 if s - 1 != k else k + 2])
    if claim == k: truth = True
    return dict(en='Two dice are rolled. Exactly %d outcomes are favorable to the event “the sum of the two numbers is %d”.' % (claim, s), vi='Gieo hai con xúc xắc. Có đúng %d kết quả thuận lợi cho biến cố “Tổng số chấm trên hai con xúc xắc bằng %d”.' % (claim, s),
                ans=truth, ee='The favorable outcomes: %s (%d outcomes).' % (', '.join('\\(%s\\)' % pair(a, b) for a, b in dsum(s)), k), ev='Các kết quả thuận lợi: %s (%d kết quả).' % (', '.join('\\(%s\\)' % pair(a, b) for a, b in dsum(s)), k))


def b26_short_count(r, lv):
    k = r.choice(['prod', 'diff', 'both'])
    if k == 'prod':
        p = r.choice([4, 6, 12, 18, 8, 10, 20, 24]); A = [(i, j) for i in range(1, 7) for j in range(1, 7) if i * j == p]
        en, vi = 'the product of the two numbers is %d' % p, 'Tích số chấm trên hai con xúc xắc bằng %d' % p
    elif k == 'diff':
        d = r.randint(1, 4); A = [(i, j) for i in range(1, 7) for j in range(1, 7) if abs(i - j) == d]
        en, vi = 'the two numbers differ by %d' % d, 'Hai số chấm hơn kém nhau %d' % d
    else:
        t = r.randint(3, 5); A = [(i, j) for i in range(1, 7) for j in range(1, 7) if i > t and j > t]
        en, vi = 'both numbers are greater than %d' % t, 'Cả hai số chấm đều lớn hơn %d' % t
    return dict(en='Two dice are rolled. How many outcomes are favorable to the event “%s”?' % en, vi='Gieo hai con xúc xắc. Có bao nhiêu kết quả thuận lợi cho biến cố “%s”?' % vi, key=str(len(A)),
                ee='%s: %d outcomes.' % (', '.join('\\(%s\\)' % pair(a, b) for a, b in A), len(A)), ev='%s: %d kết quả.' % (', '.join('\\(%s\\)' % pair(a, b) for a, b in A), len(A)))


def b26_short_dec(r, lv):
    n = r.choice([20, 25, 40, 50]); m = r.randint(2, n // 2)
    while (F(m, n) * 100).denominator != 1: m = r.randint(2, n // 2)
    it = r.choice([('tickets', 'lá phiếu', 'a winning ticket', 'phiếu trúng thưởng', 'winning tickets', 'phiếu trúng thưởng'),
                   ('eggs', 'quả trứng', 'a double-yolk egg', 'quả trứng hai lòng đỏ', 'double-yolk eggs', 'quả trứng hai lòng đỏ'),
                   ('seeds', 'hạt giống', 'a red-flower seed', 'hạt cho hoa đỏ', 'red-flower seeds', 'hạt cho hoa đỏ')])
    p = F(m, n); key = pe(p)
    return dict(en='Among %d %s, there are %d %s. One is chosen at random. Find the probability of getting %s (write it as a decimal).' % (n, it[0], m, it[4], it[2]),
                vi='Trong %d %s có %d %s. Chọn ngẫu nhiên một %s. Tính xác suất chọn được %s (viết dưới dạng số thập phân).' % (n, it[1], m, it[5], it[1], it[3]), key=key,
                hint=('Enter a decimal (e.g. 0.25).', 'Nhập số thập phân (ví dụ 0,25).'),
                ee='\\(P=\\dfrac{%d}{%d}=%s\\).' % (m, n, key), ev='\\(P=\\dfrac{%d}{%d}=%s\\).' % (m, n, dm(key)))


def b26_d1_fav(r, lv):
    e = r.choice(DIE_EV); A = [x for x in range(1, 7) if e[2](x)]
    nA = [x for x in range(1, 7) if not e[2](x)]
    o = [setx(A), setx(nA), setx(A[:-1]) if len(A) > 1 else setx([7]), setx(range(1, 7))]
    return dict(en='A die is rolled. Which set lists the outcomes favorable to the event “the die shows %s”?' % e[0],
                vi='Gieo một con xúc xắc. Tập hợp nào gồm các kết quả thuận lợi cho biến cố “%s”?' % (e[1][0].upper() + e[1][1:]),
                opts=o, ans=0, ee='The outcomes that make the event happen: \\(%s\\).' % setx(A), ev='Các kết quả làm cho biến cố xảy ra: \\(%s\\).' % setx(A))


def b26_d1_range(r, lv):
    k = r.choice(['notp', 'formula', 'equal'])
    if k == 'notp':
        bad = r.choice(['1.2', '-0.3', '\\dfrac{7}{5}', '150\\%']); badv = bad.replace('.', '{,}')
        goods = r.sample(['0', '1', '0.5', '\\dfrac{3}{8}', '0.07', '\\dfrac{9}{10}'], 3)
        o = [tx('\\(%s\\)' % bad, '\\(%s\\)' % badv)] + [tx('\\(%s\\)' % g, '\\(%s\\)' % g.replace('.', '{,}')) for g in goods]
        return dict(en='Which number CANNOT be the probability of an event?', vi='Số nào KHÔNG thể là xác suất của một biến cố?', opts=o, ans=0,
                    ee='Always \\(0\\le P(A)\\le 1\\).', ev='Luôn có \\(0\\le P(A)\\le 1\\).')
    if k == 'formula':
        o = ['P(A)=\\dfrac{n(A)}{n(\\Omega)}', 'P(A)=\\dfrac{n(\\Omega)}{n(A)}', 'P(A)=n(A)\\cdot n(\\Omega)', 'P(A)=n(\\Omega)-n(A)']
        return dict(en='The outcomes of an experiment are equally likely; \\(n(A)\\) is the number of favorable outcomes of \\(A\\). Then…', vi='Các kết quả của phép thử là đồng khả năng; \\(n(A)\\) là số kết quả thuận lợi cho \\(A\\). Khi đó…',
                    opts=o, ans=0, ee='\\(P(A)=\\dfrac{n(A)}{n(\\Omega)}\\).', ev='\\(P(A)=\\dfrac{n(A)}{n(\\Omega)}\\).')
    o = [tx('a fair die', 'một con xúc xắc cân đối và đồng chất'), tx('a die with one face heavier than the others', 'một con xúc xắc bị làm nặng một mặt'),
         tx('a spinner with sectors of different sizes', 'một vòng quay có các hình quạt không bằng nhau'), tx('a coin bent on one side', 'một đồng xu bị cong một phía')]
    return dict(en='For which object are all the outcomes equally likely?', vi='Với vật nào sau đây, các kết quả có thể là đồng khả năng?', opts=o, ans=0,
                ee='A fair die: each face has the same chance \\(\\dfrac{1}{6}\\).', ev='Xúc xắc cân đối và đồng chất: mỗi mặt có cùng khả năng xuất hiện \\(\\dfrac{1}{6}\\).')


def b26_d1_spin(r, lv):
    k = r.choice([4, 5, 6, 8]); labs = r.sample(range(1, 13), k); labs.sort()
    ev = r.choice([('an even number', 'số chẵn', lambda x: x % 2 == 0), ('a number greater than 6', 'số lớn hơn 6', lambda x: x > 6), ('an odd number', 'số lẻ', lambda x: x % 2 == 1)])
    A = [x for x in labs if ev[2](x)]
    if not 0 < len(A) < k: raise AssertionError
    fn = spinner_svg([str(x) for x in labs])
    return dict(en='The spinner has %d equal sectors. It is spun once. What is the probability that the arrow stops at %s?' % (k, ev[0]), vi='Vòng quay có %d hình quạt bằng nhau. Quay một lần. Tính xác suất để kim dừng ở %s.' % (k, ev[1]),
                opts=fopts(r, F(len(A), k), [F(k - len(A), k), F(len(A), 12), F(1, k)]), ans=0,
                ee='Favorable: %s; \\(P=%s\\).' % (', '.join(map(str, A)), fexp(len(A), k)), ev='Kết quả thuận lợi: %s; \\(P=%s\\).' % (', '.join(map(str, A)), fexp(len(A), k)),
                fig=(img(fn, 'Spinner', 260), img(fn, 'Vòng quay', 260)))


def b26_d2_coindie(r, lv):
    k = r.choice([('heads and an even number', 'mặt ngửa và số chấm chẵn', 'H', lambda x: x % 2 == 0), ('tails and a number greater than 4', 'mặt sấp và số chấm lớn hơn 4', 'T', lambda x: x > 4),
                  ('heads and a 6', 'mặt ngửa và mặt 6 chấm', 'H', lambda x: x == 6), ('tails and a number at most 2', 'mặt sấp và số chấm không quá 2', 'T', lambda x: x <= 2)])
    A = [x for x in range(1, 7) if k[3](x)]; m = len(A)
    cv = {'H': 'N', 'T': 'S'}[k[2]]
    return dict(en='A fair coin is tossed and a fair die is rolled. Find the probability of getting %s.' % k[0], vi='Gieo một đồng xu và một con xúc xắc cân đối. Tính xác suất được %s.' % k[1],
                opts=fopts(r, F(m, 12), [F(m, 6), F(m + 1, 12), F(1, 2), F(m, 8)]), ans=0,
                ee='\\(n(\\Omega)=12\\); favorable: %s; \\(P=%s\\).' % (', '.join('\\(%s\\)' % pair(k[2], x) for x in A), fexp(m, 12)),
                ev='\\(n(\\Omega)=12\\); thuận lợi: %s; \\(P=%s\\).' % (', '.join('\\(%s\\)' % pair(cv, x) for x in A), fexp(m, 12)))


def b26_d2_range(r, lv):
    a = r.choice([10, 20, 30, 40]); b = a + r.choice([9, 19, 14, 24]); n = b - a + 1
    k = r.choice(['prime', 'mult', 'digit'])
    if k == 'prime': A = [x for x in range(a, b + 1) if x in PRIMES]; en, vi = 'a prime number', 'số nguyên tố'
    elif k == 'mult': d = r.choice([4, 6, 7]); A = [x for x in range(a, b + 1) if x % d == 0]; en, vi = 'a multiple of %d' % d, 'bội của %d' % d
    else: A = [x for x in range(a, b + 1) if x % 10 == x // 10 % 10 or x % 11 == 0]; en, vi = 'a number with two equal digits', 'số có hai chữ số giống nhau'
    if not A: raise AssertionError
    return dict(en='A whole number from %d to %d is chosen at random. What is the probability that it is %s?' % (a, b, en), vi='Chọn ngẫu nhiên một số tự nhiên từ %d đến %d. Tính xác suất để số được chọn là %s.' % (a, b, vi),
                opts=fopts(r, F(len(A), n), [F(len(A), b - a), F(len(A) + 1, n), F(n - len(A), n), F(1, len(A) + 1)]), ans=0,
                ee='\\(n(\\Omega)=%d-%d+1=%d\\); favorable: %s; \\(P=%s\\).' % (b, a, n, ', '.join(map(str, A)), fexp(len(A), n)),
                ev='\\(n(\\Omega)=%d-%d+1=%d\\); thuận lợi: %s; \\(P=%s\\).' % (b, a, n, ', '.join(map(str, A)), fexp(len(A), n)))


def b26_d2_grid(r, lv):
    a, b = r.randint(3, 4), r.randint(3, 4)
    rows = list(range(1, a + 1)); cols = list(range(1, b + 1))
    k = r.choice(['same', 'sum', 'bigger'])
    if k == 'same': A = [(i, j) for i in rows for j in cols if i == j]; en, vi = 'the two numbers are equal', 'hai số bằng nhau'
    elif k == 'sum': s = r.randint(4, a + b - 1); A = [(i, j) for i in rows for j in cols if i + j == s]; en, vi = 'the sum of the two numbers is %d' % s, 'tổng hai số bằng %d' % s
    else: A = [(i, j) for i in rows for j in cols if i > j]; en, vi = 'the number on spinner 1 is greater', 'số ở vòng quay 1 lớn hơn'
    fig = gridtab([str(x) for x in rows], [str(x) for x in cols], lambda rw, c: '\\((%s;\\,%s)\\)' % (rw, c), ('Spinner 1 \\ Spinner 2', 'Vòng 1 \\ Vòng 2'))
    n = a * b
    return dict(en='Spinner 1 (numbers 1 to %d) and spinner 2 (numbers 1 to %d) are spun; the table shows all equally likely outcomes. Find the probability that %s.' % (a, b, en),
                vi='Quay vòng quay 1 (số 1 đến %d) và vòng quay 2 (số 1 đến %d); bảng dưới liệt kê các kết quả đồng khả năng. Tính xác suất để %s.' % (a, b, vi),
                opts=fopts(r, F(len(A), n), [F(len(A) + 1, n), F(len(A), a + b), F(n - len(A), n), F(1, a)]), ans=0,
                ee='\\(n(\\Omega)=%d\\); favorable: %s; \\(P=%s\\).' % (n, ', '.join('\\(%s\\)' % pair(*x) for x in A), fexp(len(A), n)),
                ev='\\(n(\\Omega)=%d\\); thuận lợi: %s; \\(P=%s\\).' % (n, ', '.join('\\(%s\\)' % pair(*x) for x in A), fexp(len(A), n)), fig=fig)


def b26_d3_dice(r, lv):
    k = r.choice(['sum', 'atleast', 'double'])
    if k == 'sum': s = r.randint(4, 10); A = dsum(s); en, vi = 'the sum is %d' % s, 'Tổng số chấm bằng %d' % s
    elif k == 'atleast': s = r.randint(9, 11); A = [(i, j) for i in range(1, 7) for j in range(1, 7) if i + j >= s]; en, vi = 'the sum is at least %d' % s, 'Tổng số chấm không nhỏ hơn %d' % s
    else: A = [(i, i) for i in range(1, 7)]; en, vi = 'the two dice show the same number', 'Hai con xúc xắc có cùng số chấm'
    m = len(A)
    return dict(en='Two fair dice are rolled. Find the probability of the event “%s”.' % en, vi='Gieo hai con xúc xắc cân đối. Tính xác suất của biến cố “%s”.' % vi,
                opts=fopts(r, F(m, 36), [F(m, 11), F(m, 12), F(m + 1, 36), F(36 - m, 36)]), ans=0,
                ee='\\(n(\\Omega)=36\\); %d favorable outcomes; \\(P=%s\\).' % (m, fexp(m, 36)), ev='\\(n(\\Omega)=36\\); có %d kết quả thuận lợi; \\(P=%s\\).' % (m, fexp(m, 36)))


def b26_d3_two(r, lv):
    n = r.randint(4, 6); k = r.choice(['even', 'odd', 'gt'])
    om = [(a, b) for a in range(1, n + 1) for b in range(1, n + 1) if a != b]
    if k == 'even': A = [x for x in om if (x[0] + x[1]) % 2 == 0]; en, vi = 'the sum of the two numbers is even', 'tổng hai số là số chẵn'
    elif k == 'odd': A = [x for x in om if (x[0] * x[1]) % 2 == 1]; en, vi = 'the product of the two numbers is odd', 'tích hai số là số lẻ'
    else: t = n + 1; A = [x for x in om if x[0] + x[1] > t]; en, vi = 'the sum of the two numbers is greater than %d' % t, 'tổng hai số lớn hơn %d' % t
    m = len(A); N = len(om)
    return dict(en='A box has %d cards numbered 1 to %d. Draw a card, do not put it back, then draw a second card. Find the probability that %s.' % (n, n, en),
                vi='Hộp có %d tấm thẻ đánh số từ 1 đến %d. Rút một thẻ, không trả lại, rồi rút thẻ thứ hai. Tính xác suất để %s.' % (n, n, vi),
                opts=fopts(r, F(m, N), [F(m, n * n), F(m + 2, N), F(N - m, N), F(1, 2)]), ans=0,
                ee='\\(n(\\Omega)=%d\\cdot%d=%d\\) ordered pairs; %d of them are favorable; \\(P=%s\\).' % (n, n - 1, N, m, fexp(m, N)),
                ev='\\(n(\\Omega)=%d\\cdot%d=%d\\) cặp có thứ tự; có %d cặp thuận lợi; \\(P=%s\\).' % (n, n - 1, N, m, fexp(m, N)))


def b26_d3_kids(r, lv):
    c = r.choice([2, 3]); k = r.choice(['atleast', 'exact', 'all'])
    om = list(itertools.product('BG', repeat=c))
    if k == 'atleast': A = [x for x in om if 'G' in x]; en, vi = 'at least one girl', 'có ít nhất một con gái'
    elif k == 'exact': A = [x for x in om if x.count('G') == 1]; en, vi = 'exactly one girl', 'có đúng một con gái'
    else: A = [x for x in om if len(set(x)) == 1]; en, vi = 'all the children are of the same sex', 'các con đều cùng giới tính'
    m = len(A); N = len(om)
    return dict(en='A family has %d children. Assume that boys (B) and girls (G) are equally likely and the order of birth matters. Find the probability that the family has %s.' % (c, en),
                vi='Một gia đình có %d con. Giả sử sinh con trai (T) và con gái (G) là đồng khả năng và có phân biệt thứ tự sinh. Tính xác suất để gia đình đó %s.' % (c, vi),
                opts=fopts(r, F(m, N), [F(m, c + 1), F(1, 2), F(m + 1, N), F(N - m, N)]), ans=0,
                ee='Tree diagram: \\(n(\\Omega)=2^{%d}=%d\\); %d favorable outcomes; \\(P=%s\\).' % (c, N, m, fexp(m, N)), ev='Sơ đồ hình cây: \\(n(\\Omega)=2^{%d}=%d\\); có %d kết quả thuận lợi; \\(P=%s\\).' % (c, N, m, fexp(m, N)))


def b26_d4_game(r, lv):
    s = r.randint(7, 9); A = [(i, j) for i in range(1, 7) for j in range(1, 7) if i + j >= s]; a = len(A); b = 36 - a
    who = r.choice([('An', 'Nam'), ('Mai', 'Lan'), ('Minh', 'Hoa')])
    if a == b: raise AssertionError
    win = who[0] if a > b else who[1]; lose = who[1] if a > b else who[0]
    hi_, lo_ = max(a, b), min(a, b)
    o = [tx('%s, because \\(\\dfrac{%d}{36}\\gt\\dfrac{%d}{36}\\)' % (win, hi_, lo_), '%s, vì \\(\\dfrac{%d}{36}\\gt\\dfrac{%d}{36}\\)' % (win, hi_, lo_)),
         tx('%s, because \\(\\dfrac{%d}{36}\\gt\\dfrac{%d}{36}\\)' % (lose, hi_, lo_), '%s, vì \\(\\dfrac{%d}{36}\\gt\\dfrac{%d}{36}\\)' % (lose, hi_, lo_)),
         tx('the game is fair, both have probability \\(\\dfrac{1}{2}\\)', 'trò chơi công bằng, hai bạn có cùng xác suất \\(\\dfrac{1}{2}\\)'),
         tx('we cannot compare, it is only luck', 'không so sánh được, chỉ do may mắn')]
    if len(set(o)) < 4: raise AssertionError
    return dict(en='%s and %s roll two dice. %s wins if the sum is at least %d; otherwise %s wins. Who is more likely to win?' % (who[0], who[1], who[0], s, who[1]),
                vi='%s và %s gieo hai con xúc xắc. Nếu tổng số chấm không nhỏ hơn %d thì %s thắng, ngược lại %s thắng. Bạn nào có khả năng thắng cao hơn?' % (who[0], who[1], s, who[0], who[1]),
                opts=o, ans=0, ee='Sum at least %d: %d outcomes, so \\(P(%s)=\\dfrac{%d}{36}\\), \\(P(%s)=\\dfrac{%d}{36}\\).' % (s, a, who[0], a, who[1], b),
                ev='Tổng không nhỏ hơn %d: có %d kết quả, nên xác suất %s thắng là \\(\\dfrac{%d}{36}\\), xác suất %s thắng là \\(\\dfrac{%d}{36}\\).' % (s, a, who[0], a, who[1], b))


def b26_d4_comp(r, lv):
    k = r.choice(['ticket', 'double', 'notsix'])
    if k == 'ticket':
        n = r.choice([50, 100, 200]); m = r.choice([n // 10, n // 20, n // 25, 3 * n // 20])
        p = F(n - m, n)
        return dict(en='In a school fair, %d of the %d lucky tickets win a prize. A student buys one ticket. What is the probability that the ticket does NOT win?' % (m, n),
                    vi='Ở hội chợ của trường, trong %d phiếu bốc thăm có %d phiếu trúng thưởng. Một bạn mua một phiếu. Tính xác suất để phiếu đó KHÔNG trúng thưởng.' % (n, m),
                    opts=fopts(r, p, [F(m, n), F(n - m, n + m), F(1, 2), F(m, n - m)]), ans=0,
                    ee='\\(P(\\overline{A})=1-P(A)=1-\\dfrac{%d}{%d}=%s\\).' % (m, n, frt(p)), ev='\\(P(\\overline{A})=1-P(A)=1-\\dfrac{%d}{%d}=%s\\).' % (m, n, frt(p)))
    if k == 'double':
        return dict(en='Two fair dice are rolled. What is the probability that the two numbers are DIFFERENT?', vi='Gieo hai con xúc xắc cân đối. Tính xác suất để hai số chấm KHÁC nhau.',
                    opts=fopts(r, F(5, 6), [F(1, 6), F(30, 36) - F(1, 36), F(1, 2), F(2, 3)]), ans=0,
                    ee='Complement: both equal (6 outcomes). \\(P=1-\\dfrac{6}{36}=\\dfrac{5}{6}\\).', ev='Biến cố đối: hai số bằng nhau (6 kết quả). \\(P=1-\\dfrac{6}{36}=\\dfrac{5}{6}\\).')
    return dict(en='Two fair dice are rolled. What is the probability that at least one die shows a 6?', vi='Gieo hai con xúc xắc cân đối. Tính xác suất để có ít nhất một con xúc xắc ra mặt 6 chấm.',
                opts=fopts(r, F(11, 36), [F(1, 6), F(12, 36), F(25, 36), F(2, 6)]), ans=0,
                ee='Complement: no 6 on either die, \\(5\\cdot5=25\\) outcomes. \\(P=1-\\dfrac{25}{36}=\\dfrac{11}{36}\\).', ev='Biến cố đối: không con nào ra 6 chấm, có \\(5\\cdot5=25\\) kết quả. \\(P=1-\\dfrac{25}{36}=\\dfrac{11}{36}\\).')


def b26_d4_boxes(r, lv):
    for _ in range(2000):
        r1, n1, r2, n2 = r.randint(2, 8), r.randint(8, 15), r.randint(2, 8), r.randint(8, 15)
        if r1 < n1 and r2 < n2 and F(r1, n1) != F(r2, n2) and (r1 - r2) * (F(r1, n1) - F(r2, n2)) < 0: break
    else: raise AssertionError
    best = 'A' if F(r1, n1) > F(r2, n2) else 'B'; other = 'B' if best == 'A' else 'A'
    pa, pb = F(r1, n1), F(r2, n2)
    o = [tx('box %s' % best, 'hộp %s' % best), tx('box %s, because it has more red balls' % other, 'hộp %s, vì có nhiều quả đỏ hơn' % other), tx('both boxes give the same chance', 'hai hộp như nhau'), tx('cannot be decided', 'không thể biết được')]
    return dict(en='Box A has %d balls, %d of them red. Box B has %d balls, %d of them red. You win if you take a red ball. From which box should you take one ball at random?' % (n1, r1, n2, r2),
                vi='Hộp A có %d quả bóng, trong đó %d quả màu đỏ. Hộp B có %d quả bóng, trong đó %d quả màu đỏ. Lấy được quả đỏ thì thắng. Nên lấy ngẫu nhiên một quả từ hộp nào?' % (n1, r1, n2, r2),
                opts=o, ans=0, ee='\\(P_A=\\dfrac{%d}{%d}\\approx%s\\), \\(P_B=\\dfrac{%d}{%d}\\approx%s\\): choose box %s.' % (r1, n1, '%.2f' % float(pa), r2, n2, '%.2f' % float(pb), best),
                ev='\\(P_A=\\dfrac{%d}{%d}\\approx%s\\), \\(P_B=\\dfrac{%d}{%d}\\approx%s\\): chọn hộp %s.' % (r1, n1, ('%.2f' % float(pa)).replace('.', '{,}'), r2, n2, ('%.2f' % float(pb)).replace('.', '{,}'), best))


L26_GROUPS = [[('mcq', b26_die), ('mcq', b26_cards), ('mcq', b26_bag)], [('tf', b26_tf_coins), ('tf', b26_tf_sum)], [('short', b26_short_count), ('short', b26_short_dec)],
              [('mcq', b26_d1_fav), ('mcq', b26_d1_range), ('mcq', b26_d1_spin)], [('mcq', b26_d2_coindie), ('mcq', b26_d2_range), ('mcq', b26_d2_grid)],
              [('mcq', b26_d3_dice), ('mcq', b26_d3_two), ('mcq', b26_d3_kids)], [('mcq', b26_d4_game), ('mcq', b26_d4_comp), ('mcq', b26_d4_boxes)]]


# =====================================================================================================
# BÀI 27. Góc nội tiếp – hình tĩnh (TikZ). Nhãn điểm đặt ra phía ngoài và tránh mọi nét vẽ; góc vuông vẽ bằng ô vuông.
# =====================================================================================================
from fig2d import Canvas


def cfig(pts, segs=(), O=True, arcs=(), right=(), R=1.9, dash=(), hl_arc=None, inner=None, ocand=None):
    """pts: {tên: góc (độ)} điểm trên đường tròn tâm O; inner: {tên: (x, y)} điểm không nằm trên đường tròn;
    segs: [(P, Q)] nét liền; dash: nét đứt; arcs: [(P, V, Q, nhãn TeX hoặc '')] cung đánh dấu góc tại V;
    right: [(P, V, Q)] kí hiệu góc vuông tại V; hl_arc: (P, Q) tô đậm cung nhỏ đi ngược chiều kim đồng hồ từ P đến Q."""
    c = Canvas()
    P = {k: (R * math.cos(math.radians(a)), R * math.sin(math.radians(a))) for k, a in pts.items()}
    if O: P['O'] = (0.0, 0.0)
    if inner: P.update(inner)
    ring = [(R * math.cos(2 * math.pi * i / 160), R * math.sin(2 * math.pi * i / 160)) for i in range(161)]
    c.seg_only(ring); c.o.append('\\draw[color=%s, line width=1.1pt] (0,0) circle (%.3f);' % (col('046b4d'), R))
    if hl_arc:
        a0, a1 = pts[hl_arc[0]], pts[hl_arc[1]]
        if a1 < a0: a1 += 360
        c.o.append('\\draw[color=%s, line width=2.4pt] (%.3f:%.3f) arc[start angle=%.3f, end angle=%.3f, radius=%.3fcm];' % (col('c2410c'), a0, R, a0, a1, R))
    for a, b in segs: c.poly([P[a], P[b]], 'ink, line width=0.85pt')
    for a, b in dash: c.poly([P[a], P[b]], 'ink, line width=0.7pt, dash pattern=on 3.5pt off 2.5pt')
    for a, v, b in right:
        V = P[v]; u1 = _unit(V, P[a]); u2 = _unit(V, P[b]); s = 0.24
        q1 = (V[0] + s * u1[0], V[1] + s * u1[1]); q2 = (V[0] + s * u2[0], V[1] + s * u2[1]); q3 = (q1[0] + s * u2[0], q1[1] + s * u2[1])
        c.poly([q1, q3, q2], 'ink, line width=0.7pt')
    for a, v, b, lab in arcs:
        V = P[v]; t1 = math.atan2(P[a][1] - V[1], P[a][0] - V[0]); t2 = math.atan2(P[b][1] - V[1], P[b][0] - V[0])
        d = (t2 - t1) % (2 * math.pi)
        if d > math.pi: t1, t2 = t2, t1; d = 2 * math.pi - d
        rr = 0.42; arcp = [(V[0] + rr * math.cos(t1 + d * i / 20), V[1] + rr * math.sin(t1 + d * i / 20)) for i in range(21)]
        c.poly(arcp, '%s, line width=0.9pt' % ('color=' + col('c2410c')))
        if lab:
            m = t1 + d / 2; w = 0.2 + 0.13 * len(lab.replace('^\\circ', 'o').replace('\\', ''))
            c.label(V[0], V[1], '$%s$' % lab, w, 0.34, [((0.78 + k * 0.12) * math.cos(m), (0.78 + k * 0.12) * math.sin(m)) for k in range(4)], white=True)
    for k, (x, y) in P.items():
        c.dot(x, y, color='1f2937')
    for k, (x, y) in P.items():
        nm = k if len(k) == 1 else k[0] + "'"
        if k in pts:
            cands = [(0.34 * math.cos(math.radians(pts[k] + da)), 0.34 * math.sin(math.radians(pts[k] + da))) for da in (0, 18, -18, 35, -35, 55, -55)]
        else:
            cands = [(0.3 * math.cos(math.radians(a)), 0.3 * math.sin(math.radians(a))) for a in (ocand or (-110, -70, 250, 200, -20, 160, 20, 90, 135, 45))]
        c.label(x, y, '$%s$' % nm, 0.3, 0.36, cands)
    return c.svg()


def _unit(V, Q):
    d = math.hypot(Q[0] - V[0], Q[1] - V[1]); return ((Q[0] - V[0]) / d, (Q[1] - V[1]) / d)


def CFIG(**kw):
    fn = cfig(**kw)
    return (img(fn, 'Figure', 300), img(fn, 'Hình vẽ', 300))


def A(x): return '\\widehat{%s}' % x
def deg(x): return '%s^\\circ' % pe(x)
def degv(x): return '%s^\\circ' % dm(pe(x))
def dopts(r, good, bads, step=5):
    return pick_opts(r, tx('\\(%s\\)' % deg(good), '\\(%s\\)' % degv(good)),
                     [tx('\\(%s\\)' % deg(b), '\\(%s\\)' % degv(b)) for b in bads if b != good and 0 < b < 360],
                     fill=lambda k: tx('\\(%s\\)' % deg(good + step * k), '\\(%s\\)' % degv(good + step * k)))


ARC = ('\\overset{\\frown}{%s}', '\\overset{\\frown}{%s}')
def arcm(x, lang): return ('m\\overset{\\frown}{%s}' if lang == 'en' else '\\text{sđ}\\,\\overset{\\frown}{%s}') % x


def b27_which(r, lv):
    a = r.randint(200, 250); b = r.randint(290, 330); c_ = r.randint(20, 70); d = r.randint(100, 150)
    L = r.choice(['ABCD', 'MNPQ', 'EFGH', 'ABCE']); P1, P2, P3, P4 = L
    pts = {P1: d, P2: a, P3: b, P4: c_}
    ins, cen, bad = A(P2 + P1 + P3), A(P2 + 'O' + P3), A('O' + P2 + P3)
    o = [ins, cen, bad, A('O' + P4 + P3) if r.random() < 0.5 else A(P1 + 'O' + P4)]
    return dict(en='In the figure, \\(%s\\), \\(%s\\), \\(%s\\), \\(%s\\) lie on the circle with center \\(O\\). Which angle is an inscribed angle?' % tuple(L),
                vi='Trong hình vẽ, \\(%s\\), \\(%s\\), \\(%s\\), \\(%s\\) nằm trên đường tròn tâm \\(O\\). Góc nào là góc nội tiếp?' % tuple(L), opts=o, ans=0,
                ee='\\(%s\\) has its vertex \\(%s\\) on the circle and its sides contain the chords \\(%s%s\\), \\(%s%s\\). \\(%s\\) is a central angle; the side \\(%sO\\) of \\(%s\\) is not a chord.' % (ins, P1, P1, P2, P1, P3, cen, P2, bad),
                ev='\\(%s\\) có đỉnh \\(%s\\) nằm trên đường tròn và hai cạnh chứa hai dây \\(%s%s\\), \\(%s%s\\). \\(%s\\) là góc ở tâm; cạnh \\(%sO\\) của \\(%s\\) không phải là dây.' % (ins, P1, P1, P2, P1, P3, cen, P2, bad),
                fig=CFIG(pts=pts, segs=[(P1, P2), (P1, P3), ('O', P2), ('O', P3), ('O', P4), (P4, P3)]))


def b27_arc(r, lv):
    x = r.choice(range(40, 321, 2)); g = F(x, 2); P_, Q_ = r.choice([('A', 'B'), ('M', 'N'), ('B', 'C')]); V = r.choice(['C', 'D', 'E']) if 'C' not in (P_, Q_) else 'D'
    return dict(en='The inscribed angle \\(%s\\) intercepts the arc \\(%s\\) with \\(%s=%s\\). Find \\(%s\\).' % (A(P_ + V + Q_), '\\overset{\\frown}{%s%s}' % (P_, Q_), arcm(P_ + Q_, 'en'), deg(x), A(P_ + V + Q_)),
                vi='Góc nội tiếp \\(%s\\) chắn cung \\(%s\\) có \\(%s=%s\\). Tính \\(%s\\).' % (A(P_ + V + Q_), '\\overset{\\frown}{%s%s}' % (P_, Q_), arcm(P_ + Q_, 'vi'), deg(x), A(P_ + V + Q_)),
                opts=dopts(r, g, [x, 180 - g, 2 * x, 90 - g / 2 if g < 180 else g + 10]), ans=0,
                ee='An inscribed angle is half its intercepted arc: \\(\\dfrac{%d^\\circ}{2}=%s\\).' % (x, deg(g)), ev='Số đo góc nội tiếp bằng nửa số đo cung bị chắn: \\(\\dfrac{%d^\\circ}{2}=%s\\).' % (x, degv(g)))


def b27_central(r, lv):
    x = r.choice(range(50, 171, 2)); g = x // 2
    a = r.randint(200, 230); b = a + x; c_ = r.randint(60, 140)
    return dict(en='In the figure, \\(%s=%d^\\circ\\) and \\(C\\) lies on the major arc \\(AB\\). Find \\(%s\\).' % (A('AOB'), x, A('ACB')), vi='Trong hình vẽ, \\(%s=%d^\\circ\\) và \\(C\\) nằm trên cung lớn \\(AB\\). Tính \\(%s\\).' % (A('AOB'), x, A('ACB')),
                opts=dopts(r, g, [x, 180 - x, 2 * x, 90 - g]), ans=0,
                ee='\\(%s\\) and the central angle \\(%s\\) intercept the same arc: \\(%s=\\dfrac{%d^\\circ}{2}=%d^\\circ\\).' % (A('ACB'), A('AOB'), A('ACB'), x, g),
                ev='Góc nội tiếp \\(%s\\) và góc ở tâm \\(%s\\) cùng chắn cung \\(AB\\): \\(%s=\\dfrac{%d^\\circ}{2}=%d^\\circ\\).' % (A('ACB'), A('AOB'), A('ACB'), x, g),
                fig=CFIG(pts={'A': a, 'B': b % 360, 'C': c_ if not a < c_ < b else c_ + 180}, segs=[('C', 'A'), ('C', 'B'), ('O', 'A'), ('O', 'B')], arcs=[('A', 'O', 'B', '%d^\\circ' % x)]))


def _four(r):
    """A, B ở dưới; C, D cùng nằm trên cung lớn AB (phía trên)."""
    a = r.randint(195, 215); b = r.randint(325, 345); c_ = r.randint(20, 60); d = r.randint(110, 160)
    return {'A': a, 'B': b, 'C': c_, 'D': d}, (b - a)


def b27_tf_same(r, lv):
    pts, arcAB = _four(r); g = F(arcAB, 2)
    if g.denominator != 1: pts['B'] += 1; arcAB += 1; g = F(arcAB, 2)
    x = int(g); truth = r.random() < 0.5; claim = x if truth else r.choice([2 * x, 180 - x, x + 10])
    if claim == x: truth = True
    return dict(en='In the figure, \\(C\\) and \\(D\\) lie on the same arc \\(AB\\) and \\(%s=%d^\\circ\\). Then \\(%s=%d^\\circ\\).' % (A('ACB'), x, A('ADB'), claim),
                vi='Trong hình vẽ, \\(C\\) và \\(D\\) nằm trên cùng một cung \\(AB\\) và \\(%s=%d^\\circ\\). Khi đó \\(%s=%d^\\circ\\).' % (A('ACB'), x, A('ADB'), claim), ans=truth,
                ee='Inscribed angles intercepting the same arc are equal: \\(%s=%s=%d^\\circ\\).' % (A('ADB'), A('ACB'), x), ev='Các góc nội tiếp cùng chắn một cung thì bằng nhau: \\(%s=%s=%d^\\circ\\).' % (A('ADB'), A('ACB'), x),
                fig=CFIG(pts=pts, segs=[('C', 'A'), ('C', 'B'), ('D', 'A'), ('D', 'B')], O=False))


def b27_tf_semi(r, lv):
    c_ = r.randint(30, 150); x = r.randint(20, 70)
    k = r.choice(['right', 'sum'])
    if k == 'right':
        truth = r.random() < 0.5; claim = 90 if truth else r.choice([60, 120, 100, 80])
        return dict(en='\\(AB\\) is a diameter of circle \\((O)\\) and \\(C\\) is a point of the circle (\\(C\\ne A,\\,B\\)). Then \\(%s=%d^\\circ\\).' % (A('ACB'), claim),
                    vi='\\(AB\\) là một đường kính của đường tròn \\((O)\\), \\(C\\) là một điểm thuộc đường tròn (\\(C\\ne A,\\,B\\)). Khi đó \\(%s=%d^\\circ\\).' % (A('ACB'), claim), ans=truth,
                    ee='An inscribed angle intercepting a semicircle is a right angle.', ev='Góc nội tiếp chắn nửa đường tròn là góc vuông.')
    y = 90 - x; truth = r.random() < 0.5; claim = y if truth else r.choice([180 - x, x, 90 + x])
    if claim == y: truth = True
    return dict(en='In the figure, \\(AB\\) is a diameter and \\(%s=%d^\\circ\\). Then \\(%s=%d^\\circ\\).' % (A('CAB'), x, A('CBA'), claim),
                vi='Trong hình vẽ, \\(AB\\) là đường kính và \\(%s=%d^\\circ\\). Khi đó \\(%s=%d^\\circ\\).' % (A('CAB'), x, A('CBA'), claim), ans=truth,
                ee='\\(%s=90^\\circ\\) (semicircle), so \\(%s=90^\\circ-%d^\\circ=%d^\\circ\\).' % (A('ACB'), A('CBA'), x, y), ev='\\(%s=90^\\circ\\) (chắn nửa đường tròn) nên \\(%s=90^\\circ-%d^\\circ=%d^\\circ\\).' % (A('ACB'), A('CBA'), x, y),
                fig=CFIG(pts={'A': 180, 'B': 0, 'C': 2 * x}, segs=[('A', 'B'), ('C', 'A'), ('C', 'B')], right=[('A', 'C', 'B')]))


def b27_short_comp(r, lv):
    x = r.randint(20, 70); y = 90 - x
    return dict(en='In the figure, \\(AB\\) is a diameter of \\((O)\\) and \\(%s=%d^\\circ\\). Find \\(%s\\) (in degrees).' % (A('ABC'), x, A('BAC')),
                vi='Trong hình vẽ, \\(AB\\) là đường kính của \\((O)\\) và \\(%s=%d^\\circ\\). Tính số đo \\(%s\\) (độ).' % (A('ABC'), x, A('BAC')), key=str(y),
                ee='\\(%s=90^\\circ\\); \\(%s=90^\\circ-%d^\\circ=%d^\\circ\\).' % (A('ACB'), A('BAC'), x, y), ev='\\(%s=90^\\circ\\); \\(%s=90^\\circ-%d^\\circ=%d^\\circ\\).' % (A('ACB'), A('BAC'), x, y),
                fig=CFIG(pts={'A': 180, 'B': 0, 'C': (180 - 2 * x) * (1 if r.random() < 0.5 else -1)}, segs=[('A', 'B'), ('C', 'A'), ('C', 'B')], right=[('A', 'C', 'B')]))


def b27_short_arc(r, lv):
    y = r.randint(15, 85); x = 2 * y; k = r.choice(['M', 'N', 'K'])
    return dict(en='The inscribed angle \\(%s=%d^\\circ\\) intercepts the minor arc \\(AB\\). Find the measure of the minor arc \\(AB\\) (in degrees).' % (A('A' + k + 'B'), y),
                vi='Góc nội tiếp \\(%s=%d^\\circ\\) chắn cung nhỏ \\(AB\\). Tính số đo cung nhỏ \\(AB\\) (độ).' % (A('A' + k + 'B'), y), key=str(x),
                ee='The arc is twice the inscribed angle: \\(2\\cdot%d^\\circ=%d^\\circ\\).' % (y, x), ev='Số đo cung bị chắn gấp đôi góc nội tiếp: \\(2\\cdot%d^\\circ=%d^\\circ\\).' % (y, x))


def b27_d1_def(r, lv):
    k = r.choice(['def', 'arc', 'vertex'])
    if k == 'def':
        o = [tx('its vertex is on the circle and its two sides contain two chords', 'có đỉnh nằm trên đường tròn và hai cạnh chứa hai dây của đường tròn'),
             tx('its vertex is the center of the circle', 'có đỉnh trùng với tâm đường tròn'), tx('its vertex is inside the circle', 'có đỉnh nằm bên trong đường tròn'), tx('its two sides are radii', 'có hai cạnh là hai bán kính')]
        return dict(en='An angle is called an inscribed angle of a circle when…', vi='Một góc được gọi là góc nội tiếp đường tròn khi…', opts=o, ans=0, ee='Definition of an inscribed angle.', ev='Định nghĩa góc nội tiếp.')
    if k == 'arc':
        o = [tx('the arc \\(BC\\) inside the angle', 'cung \\(BC\\) nằm bên trong góc'), tx('the arc \\(AB\\)', 'cung \\(AB\\)'), tx('the arc \\(AC\\)', 'cung \\(AC\\)'), tx('the whole circle', 'cả đường tròn')]
        return dict(en='\\(A\\), \\(B\\), \\(C\\) lie on a circle. Which arc does the inscribed angle \\(%s\\) intercept?' % A('BAC'), vi='\\(A\\), \\(B\\), \\(C\\) nằm trên một đường tròn. Góc nội tiếp \\(%s\\) chắn cung nào?' % A('BAC'), opts=o, ans=0,
                    ee='The intercepted arc lies inside the angle, between \\(B\\) and \\(C\\) (not containing \\(A\\)).', ev='Cung bị chắn nằm bên trong góc, nối \\(B\\) và \\(C\\) (không chứa \\(A\\)).')
    o = [tx('\\(%s\\)' % A('MPN'), '\\(%s\\)' % A('MPN')), tx('\\(%s\\)' % A('MON'), '\\(%s\\)' % A('MON')), tx('\\(%s\\)' % A('OMN'), '\\(%s\\)' % A('OMN')), tx('\\(%s\\)' % A('MNO'), '\\(%s\\)' % A('MNO'))]
    return dict(en='\\(M\\), \\(N\\), \\(P\\) lie on the circle \\((O)\\). Which angle is an inscribed angle intercepting the arc \\(MN\\)?', vi='\\(M\\), \\(N\\), \\(P\\) nằm trên đường tròn \\((O)\\). Góc nào là góc nội tiếp chắn cung \\(MN\\)?', opts=o, ans=0,
                ee='The vertex \\(P\\) is on the circle and the sides \\(PM\\), \\(PN\\) are chords.', ev='Đỉnh \\(P\\) nằm trên đường tròn, hai cạnh \\(PM\\), \\(PN\\) là hai dây.')


def b27_d1_semi(r, lv):
    nm = r.choice([('MN', 'P'), ('CD', 'E'), ('EF', 'K')])
    return dict(en='\\(%s\\) is a diameter of a circle and \\(%s\\) is another point of the circle. What is the measure of \\(%s\\)?' % (nm[0], nm[1], A(nm[0][0] + nm[1] + nm[0][1])),
                vi='\\(%s\\) là một đường kính của đường tròn, \\(%s\\) là một điểm khác của đường tròn. Số đo của \\(%s\\) bằng bao nhiêu?' % (nm[0], nm[1], A(nm[0][0] + nm[1] + nm[0][1])),
                opts=['90^\\circ', '180^\\circ', '60^\\circ', '45^\\circ'], ans=0, ee='It intercepts a semicircle (\\(180^\\circ\\)): \\(\\dfrac{180^\\circ}{2}=90^\\circ\\).', ev='Góc này chắn nửa đường tròn (\\(180^\\circ\\)): \\(\\dfrac{180^\\circ}{2}=90^\\circ\\).')


def b27_d1_half(r, lv):
    k = r.choice(['ins', 'cen', 'arc'])
    if k == 'ins':
        o = ['%s=\\dfrac{1}{2}%s' % (A('BAC'), A('BOC')), '%s=2%s' % (A('BAC'), A('BOC')), '%s=%s' % (A('BAC'), A('BOC')), '%s=180^\\circ-%s' % (A('BAC'), A('BOC'))]
        en, vi = 'In \\((O)\\), the inscribed angle \\(%s\\) (less than \\(90^\\circ\\)) and the central angle \\(%s\\) intercept the same arc. Then…' % (A('BAC'), A('BOC')), 'Trong \\((O)\\), góc nội tiếp \\(%s\\) (nhỏ hơn \\(90^\\circ\\)) và góc ở tâm \\(%s\\) cùng chắn một cung. Khi đó…' % (A('BAC'), A('BOC'))
    elif k == 'cen':
        o = ['%s=2%s' % (A('MON'), A('MPN')), '%s=\\dfrac{1}{2}%s' % (A('MON'), A('MPN')), '%s=%s' % (A('MON'), A('MPN')), '%s=90^\\circ-%s' % (A('MON'), A('MPN'))]
        en, vi = 'In \\((O)\\), the central angle \\(%s\\) and the inscribed angle \\(%s\\) (less than \\(90^\\circ\\)) intercept the same arc. Then…' % (A('MON'), A('MPN')), 'Trong \\((O)\\), góc ở tâm \\(%s\\) và góc nội tiếp \\(%s\\) (nhỏ hơn \\(90^\\circ\\)) cùng chắn một cung. Khi đó…' % (A('MON'), A('MPN'))
    else:
        o = ['%s=\\dfrac{1}{2}\\,%s' % (A('ACB'), '{m}\\overset{\\frown}{AB}'), '%s=2\\,%s' % (A('ACB'), '{m}\\overset{\\frown}{AB}'), '%s=%s' % (A('ACB'), '{m}\\overset{\\frown}{AB}'), '%s=360^\\circ-%s' % (A('ACB'), '{m}\\overset{\\frown}{AB}')]
        o = [x.replace('{m}', 'm') for x in o]
        en, vi = 'The inscribed angle \\(%s\\) intercepts the arc \\(AB\\) (\\(m\\overset{\\frown}{AB}\\) is its measure). Then…' % A('ACB'), 'Góc nội tiếp \\(%s\\) chắn cung \\(AB\\) (\\(m\\overset{\\frown}{AB}\\) là số đo cung đó). Khi đó…' % A('ACB')
    return dict(en=en, vi=vi, opts=o, ans=0, ee='An inscribed angle is half the central angle (and half the arc) it intercepts.', ev='Góc nội tiếp bằng nửa góc ở tâm (và bằng nửa số đo cung) cùng chắn một cung.')


def b27_d2_major(r, lv):
    x = r.choice(range(60, 161, 2)); g = (360 - x) // 2
    a = r.randint(60, 80); b = a + x; c_ = (a + b) // 2
    return dict(en='In the figure, \\(%s=%d^\\circ\\) and \\(C\\) lies on the minor arc \\(AB\\). Find \\(%s\\).' % (A('AOB'), x, A('ACB')), vi='Trong hình vẽ, \\(%s=%d^\\circ\\) và \\(C\\) nằm trên cung nhỏ \\(AB\\). Tính \\(%s\\).' % (A('AOB'), x, A('ACB')),
                opts=dopts(r, g, [x // 2, 360 - x, 180 - x // 2 + 10, x]), ans=0,
                ee='\\(%s\\) intercepts the major arc \\(AB\\) of \\(360^\\circ-%d^\\circ=%d^\\circ\\): \\(%s=%d^\\circ\\).' % (A('ACB'), x, 360 - x, A('ACB'), g),
                ev='\\(%s\\) chắn cung lớn \\(AB\\) có số đo \\(360^\\circ-%d^\\circ=%d^\\circ\\): \\(%s=%d^\\circ\\).' % (A('ACB'), x, 360 - x, A('ACB'), g),
                fig=CFIG(pts={'A': a, 'B': b, 'C': c_}, segs=[('C', 'A'), ('C', 'B'), ('O', 'A'), ('O', 'B')], arcs=[('A', 'O', 'B', '%d^\\circ' % x)]))


def b27_d2_ratio(r, lv):
    for _ in range(500):
        p = sorted(r.sample(range(1, 8), 3))
        if 360 % sum(p) == 0 and all((360 // sum(p) * q) % 2 == 0 for q in p): break
    u = 360 // sum(p); arcs = [u * q for q in p]; angs = [a // 2 for a in arcs]
    ask = r.choice(['max', 'min'])
    good = max(angs) if ask == 'max' else min(angs)
    return dict(en='Points \\(A\\), \\(B\\), \\(C\\) divide a circle into three arcs \\(AB\\), \\(BC\\), \\(CA\\) in the ratio \\(%d:%d:%d\\). Find the %s angle of triangle \\(ABC\\).' % (p[0], p[1], p[2], 'largest' if ask == 'max' else 'smallest'),
                vi='Ba điểm \\(A\\), \\(B\\), \\(C\\) chia đường tròn thành ba cung \\(AB\\), \\(BC\\), \\(CA\\) tỉ lệ với \\(%d:%d:%d\\). Tính góc %s của tam giác \\(ABC\\).' % (p[0], p[1], p[2], 'lớn nhất' if ask == 'max' else 'nhỏ nhất'),
                opts=dopts(r, good, [2 * good, max(arcs) if ask == 'max' else min(arcs), 180 - good, good + 20]), ans=0,
                ee='The arcs are %s; each angle of the triangle is half the arc opposite it: %s.' % (', '.join('\\(%d^\\circ\\)' % a for a in arcs), ', '.join('\\(%d^\\circ\\)' % a for a in angs)),
                ev='Ba cung có số đo %s; mỗi góc của tam giác bằng nửa cung bị chắn: %s.' % (', '.join('\\(%d^\\circ\\)' % a for a in arcs), ', '.join('\\(%d^\\circ\\)' % a for a in angs)))


def b27_d2_iso(r, lv):
    x = r.choice(range(20, 71)); cen = 180 - 2 * x; g = F(cen, 2)
    return dict(en='\\(AB\\) is a chord of \\((O)\\) with \\(%s=%d^\\circ\\); \\(C\\) lies on the major arc \\(AB\\). Find \\(%s\\).' % (A('OAB'), x, A('ACB')),
                vi='\\(AB\\) là một dây của \\((O)\\) với \\(%s=%d^\\circ\\); \\(C\\) nằm trên cung lớn \\(AB\\). Tính \\(%s\\).' % (A('OAB'), x, A('ACB')),
                opts=dopts(r, g, [cen, x, 90 - x // 2 if (90 - x // 2) != g else 2 * x, 180 - x]), ans=0,
                ee='\\(OA=OB\\) so \\(%s=180^\\circ-2\\cdot%d^\\circ=%d^\\circ\\); \\(%s=\\dfrac{%d^\\circ}{2}=%s\\).' % (A('AOB'), x, cen, A('ACB'), cen, deg(g)),
                ev='\\(OA=OB\\) nên \\(%s=180^\\circ-2\\cdot%d^\\circ=%d^\\circ\\); \\(%s=\\dfrac{%d^\\circ}{2}=%s\\).' % (A('AOB'), x, cen, A('ACB'), cen, degv(g)))


def b27_d3_triangle(r, lv):
    a = r.randint(35, 80); b = r.randint(35, 80); c_ = 180 - a - b
    if c_ < 25: raise AssertionError
    ask = r.choice(['BC', 'CA', 'AB']); val = {'BC': 2 * a, 'CA': 2 * b, 'AB': 2 * c_}[ask]
    bads = [x for x in (2 * a, 2 * b, 2 * c_, val // 2, 360 - val) if x != val]
    return dict(en='Triangle \\(ABC\\) is inscribed in \\((O)\\), \\(%s=%d^\\circ\\), \\(%s=%d^\\circ\\). Find the measure of the arc \\(%s\\) not containing the third vertex.' % (A('BAC'), a, A('ABC'), b, ask),
                vi='Tam giác \\(ABC\\) nội tiếp đường tròn \\((O)\\), \\(%s=%d^\\circ\\), \\(%s=%d^\\circ\\). Tính số đo cung \\(%s\\) không chứa đỉnh còn lại.' % (A('BAC'), a, A('ABC'), b, ask),
                opts=dopts(r, val, bads), ans=0,
                ee='\\(%s=180^\\circ-%d^\\circ-%d^\\circ=%d^\\circ\\). The arc %s is twice the opposite angle: \\(%d^\\circ\\).' % (A('ACB'), a, b, c_, ask, val),
                ev='\\(%s=180^\\circ-%d^\\circ-%d^\\circ=%d^\\circ\\). Cung %s có số đo gấp đôi góc đối diện: \\(%d^\\circ\\).' % (A('ACB'), a, b, c_, ask, val))


def b27_d3_quad(r, lv):
    """ABCD trên đường tròn (theo thứ tự). ∠BAC = x, ∠ACB = y ⇒ ∠BDC = x, ∠ADB = y ⇒ ∠ADC = x + y."""
    for _ in range(500):
        a, b, c_, d = 120, 220, 320, r.randint(20, 80)
        pa, pb, pc, pd = [r.randint(-12, 12) + t for t in (a, b, c_)] + [d]
        x2 = (pc - pb); y2 = (pb - pa)          # cung BC (không chứa A) và cung AB (không chứa C)
        if x2 % 2 == 0 and y2 % 2 == 0: break
    x, y = x2 // 2, y2 // 2
    return dict(en='In the figure, \\(A\\), \\(B\\), \\(C\\), \\(D\\) lie on a circle in this order, \\(%s=%d^\\circ\\) and \\(%s=%d^\\circ\\). Find \\(%s\\).' % (A('BAC'), x, A('ACB'), y, A('ADC')),
                vi='Trong hình vẽ, \\(A\\), \\(B\\), \\(C\\), \\(D\\) nằm trên một đường tròn theo thứ tự đó, \\(%s=%d^\\circ\\) và \\(%s=%d^\\circ\\). Tính \\(%s\\).' % (A('BAC'), x, A('ACB'), y, A('ADC')),
                opts=dopts(r, x + y, [x, y, 180 - x - y, 2 * (x + y)]), ans=0,
                ee='\\(%s=%s=%d^\\circ\\) (same arc \\(BC\\)); \\(%s=%s=%d^\\circ\\) (same arc \\(AB\\)); \\(%s=%d^\\circ+%d^\\circ=%d^\\circ\\).' % (A('BDC'), A('BAC'), x, A('ADB'), A('ACB'), y, A('ADC'), x, y, x + y),
                ev='\\(%s=%s=%d^\\circ\\) (cùng chắn cung \\(BC\\)); \\(%s=%s=%d^\\circ\\) (cùng chắn cung \\(AB\\)); \\(%s=%d^\\circ+%d^\\circ=%d^\\circ\\).' % (A('BDC'), A('BAC'), x, A('ADB'), A('ACB'), y, A('ADC'), x, y, x + y),
                fig=CFIG(pts={'A': pa, 'B': pb, 'C': pc, 'D': pd}, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('A', 'C'), ('B', 'D')], O=False))


def b27_d3_clock(r, lv):
    v = 12; a, b = sorted(r.sample(range(1, 12), 2))
    if b - a < 2: raise AssertionError
    arc = 30 * (b - a); g = arc // 2
    pts = {'M': 90 - 30 * a, 'N': 90 - 30 * b, 'P': 90}
    return dict(en='On a round clock face, \\(P\\) is at the number 12, \\(M\\) at the number %d and \\(N\\) at the number %d. Find \\(%s\\).' % (a, b, A('MPN')),
                vi='Trên mặt đồng hồ hình tròn, điểm \\(P\\) ở số 12, điểm \\(M\\) ở số %d và điểm \\(N\\) ở số %d. Tính \\(%s\\).' % (a, b, A('MPN')),
                opts=dopts(r, g, [arc, 6 * (b - a), 180 - g, g + 15]), ans=0,
                ee='Neighboring numbers are \\(30^\\circ\\) apart, so the arc \\(MN\\) not containing \\(P\\) is \\(%d\\cdot30^\\circ=%d^\\circ\\); \\(%s=\\dfrac{%d^\\circ}{2}=%d^\\circ\\).' % (b - a, arc, A('MPN'), arc, g),
                ev='Hai số liền nhau cách nhau \\(30^\\circ\\) nên cung \\(MN\\) không chứa \\(P\\) có số đo \\(%d\\cdot30^\\circ=%d^\\circ\\); \\(%s=\\dfrac{%d^\\circ}{2}=%d^\\circ\\).' % (b - a, arc, A('MPN'), arc, g),
                fig=CFIG(pts=pts, segs=[('P', 'M'), ('P', 'N')], O=True))


def b27_d4_stage(r, lv):
    x = r.choice(range(60, 141, 4)); g = x // 2
    k = r.choice(['angle', 'compare'])
    if k == 'angle':
        return dict(en='The front edge \\(AB\\) of a stage is a chord of a circle with center \\(O\\) and \\(%s=%d^\\circ\\). The seats \\(M\\), \\(N\\) are on the major arc \\(AB\\). From each seat, under what angle is the stage edge seen?' % (A('AOB'), x),
                    vi='Mép sân khấu \\(AB\\) là một dây của đường tròn tâm \\(O\\) với \\(%s=%d^\\circ\\). Hai ghế \\(M\\), \\(N\\) nằm trên cung lớn \\(AB\\). Từ mỗi ghế, người xem nhìn mép sân khấu dưới góc bao nhiêu độ?' % (A('AOB'), x),
                    opts=[tx('\\(%d^\\circ\\) from both seats' % g, '\\(%d^\\circ\\) ở cả hai ghế' % g), tx('\\(%d^\\circ\\) from both seats' % x, '\\(%d^\\circ\\) ở cả hai ghế' % x),
                          tx('\\(%d^\\circ\\) from \\(M\\), less from \\(N\\)' % g, '\\(%d^\\circ\\) ở ghế \\(M\\), nhỏ hơn ở ghế \\(N\\)' % g), tx('\\(%d^\\circ\\) from both seats' % (180 - g if 180 - g != x else 90 + g), '\\(%d^\\circ\\) ở cả hai ghế' % (180 - g if 180 - g != x else 90 + g))], ans=0,
                    ee='\\(%s\\) and \\(%s\\) intercept the same arc \\(AB\\): both equal \\(\\dfrac{%d^\\circ}{2}=%d^\\circ\\).' % (A('AMB'), A('ANB'), x, g), ev='\\(%s\\) và \\(%s\\) cùng chắn cung \\(AB\\): đều bằng \\(\\dfrac{%d^\\circ}{2}=%d^\\circ\\).' % (A('AMB'), A('ANB'), x, g))
    return dict(en='A camera must see the stage edge \\(AB\\) under an angle of exactly \\(%d^\\circ\\). The circle through \\(A\\), \\(B\\) has \\(%s=%d^\\circ\\). Where can the camera be placed (on the side of the audience)?' % (g, A('AOB'), x),
                vi='Một máy quay cần nhìn mép sân khấu \\(AB\\) dưới góc đúng \\(%d^\\circ\\). Đường tròn qua \\(A\\), \\(B\\) có \\(%s=%d^\\circ\\). Có thể đặt máy quay ở đâu (phía khán giả)?' % (g, A('AOB'), x),
                opts=[tx('at any point of the major arc \\(AB\\)', 'tại bất kì điểm nào trên cung lớn \\(AB\\)'), tx('only at the center \\(O\\)', 'chỉ tại tâm \\(O\\)'), tx('only at the midpoint of \\(AB\\)', 'chỉ tại trung điểm của \\(AB\\)'), tx('at any point inside the circle', 'tại bất kì điểm nào bên trong đường tròn')], ans=0,
                ee='Every inscribed angle on the major arc intercepts the arc \\(AB\\) of \\(%d^\\circ\\), so it equals \\(%d^\\circ\\).' % (x, g), ev='Mọi góc nội tiếp có đỉnh trên cung lớn đều chắn cung \\(AB\\) có số đo \\(%d^\\circ\\) nên đều bằng \\(%d^\\circ\\).' % (x, g))


def b27_d4_radius(r, lv):
    k = r.choice([30, 90, 30, 90]); a = r.choice([4, 6, 8, 10, 12, 14])
    if k == 30:
        good = '%d\\text{ cm}' % a; o = [good, '%d\\text{ cm}' % (a // 2), '%d\\text{ cm}' % (2 * a), '%d\\sqrt3\\text{ cm}' % a]
        ee = '\\(%s=2\\cdot30^\\circ=60^\\circ\\) and \\(OA=OB\\): triangle \\(OAB\\) is equilateral, \\(R=AB=%d\\) cm.' % (A('AOB'), a); ev = '\\(%s=2\\cdot30^\\circ=60^\\circ\\) và \\(OA=OB\\): tam giác \\(OAB\\) đều, \\(R=AB=%d\\) cm.' % (A('AOB'), a)
    else:
        good = '%d\\text{ cm}' % (a // 2); o = [good, '%d\\text{ cm}' % a, '%d\\text{ cm}' % (2 * a), '%d\\sqrt2\\text{ cm}' % (a // 2)]
        ee = 'A right inscribed angle intercepts a semicircle: \\(AB\\) is a diameter, \\(R=\\dfrac{%d}{2}=%d\\) cm.' % (a, a // 2); ev = 'Góc nội tiếp vuông chắn nửa đường tròn: \\(AB\\) là đường kính, \\(R=\\dfrac{%d}{2}=%d\\) cm.' % (a, a // 2)
    return dict(en='Triangle \\(ABC\\) is inscribed in \\((O;\\,R)\\) with \\(AB=%d\\) cm and \\(%s=%d^\\circ\\). Find \\(R\\).' % (a, A('ACB'), k),
                vi='Tam giác \\(ABC\\) nội tiếp đường tròn \\((O;\\,R)\\) có \\(AB=%d\\) cm và \\(%s=%d^\\circ\\). Tính \\(R\\).' % (a, A('ACB'), k), opts=o, ans=0, ee=ee, ev=ev)


def b27_d4_obc(r, lv):
    x = r.randint(25, 85); y = 90 - x
    return dict(en='Triangle \\(ABC\\) is inscribed in \\((O)\\) and \\(%s=%d^\\circ\\) (acute triangle). Find \\(%s\\).' % (A('BAC'), x, A('OBC')),
                vi='Tam giác nhọn \\(ABC\\) nội tiếp đường tròn \\((O)\\) và \\(%s=%d^\\circ\\). Tính \\(%s\\).' % (A('BAC'), x, A('OBC')),
                opts=dopts(r, y, [x, 2 * x, 180 - 2 * x, 90 + x]), ans=0,
                ee='\\(%s=2\\cdot%d^\\circ=%d^\\circ\\); \\(OB=OC\\), so \\(%s=\\dfrac{180^\\circ-%d^\\circ}{2}=%d^\\circ\\).' % (A('BOC'), x, 2 * x, A('OBC'), 2 * x, y),
                ev='\\(%s=2\\cdot%d^\\circ=%d^\\circ\\); \\(OB=OC\\) nên \\(%s=\\dfrac{180^\\circ-%d^\\circ}{2}=%d^\\circ\\).' % (A('BOC'), x, 2 * x, A('OBC'), 2 * x, y))


L27_GROUPS = [[('mcq', b27_which), ('mcq', b27_arc), ('mcq', b27_central)], [('tf', b27_tf_same), ('tf', b27_tf_semi)], [('short', b27_short_comp), ('short', b27_short_arc)],
              [('mcq', b27_d1_def), ('mcq', b27_d1_semi), ('mcq', b27_d1_half)], [('mcq', b27_d2_major), ('mcq', b27_d2_ratio), ('mcq', b27_d2_iso)],
              [('mcq', b27_d3_triangle), ('mcq', b27_d3_quad), ('mcq', b27_d3_clock)], [('mcq', b27_d4_stage), ('mcq', b27_d4_radius), ('mcq', b27_d4_obc)]]
