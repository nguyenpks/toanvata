# -*- coding: utf-8 -*-
"""Hiệu chỉnh 13/11/2026 – ngân hàng câu hỏi MỚI cho Toán 11 KNTT, Bài 9, 10, 11, 21, 32 (đợt 1).
Mục tiêu: mỗi mức 15 câu, KHÔNG có hai câu cùng dạng; bối cảnh thực tế luân phiên; bài hình không gian có hình trong đề.

Mỗi hàm sinh câu nhận (r, lv, ctx) và trả về dict:
  trắc nghiệm : en, vi, opts[4] (opts[0] đúng), ee, ev            (kind 'mcq')
  đúng/sai    : en, vi, truth, ee, ev                              (kind 'tf')
  trả lời ngắn: en, vi, key (≤ 4 kí tự, dấu phẩy thập phân), ee, ev (kind 'short')
  tuỳ chọn    : fig = (html_en, html_vi) ghép sau đề (bảng, hình).
Mọi đáp án được tính bằng Fraction/tọa độ ngay trong hàm sinh; tools/… audit kiểm tra lại độc lập."""
import math, random, itertools
from fractions import Fraction as F
from mb_lib import TI, MCQ
from mb_quick import M4, tf, sh, GRP
from mb_selfpractice import pick_opts
import mb_std

# ---------------------------------------------------------------- tiện ích chung
def tx(en, vi): return '§' + TI(en, vi)
def ne(x):
    """Số dạng tiếng Anh (dấu chấm)."""
    x = F(x)
    if x.denominator == 1: return str(x.numerator)
    d = x.denominator
    while d % 2 == 0: d //= 2
    while d % 5 == 0: d //= 5
    if d == 1: return ('%.6f' % float(x)).rstrip('0').rstrip('.')
    return ('-' if x < 0 else '') + '\\dfrac{%d}{%d}' % (abs(x.numerator), x.denominator)
def nv(x): return ne(x).replace('.', '{,}')
def nopt(x):
    """Phương án số: số nguyên dùng chung, số thập phân tách hai ngôn ngữ."""
    return ne(x) if ne(x) == nv(x) else tx('\\(%s\\)' % ne(x), '\\(%s\\)' % nv(x))
def key(x):
    s = ne(x); assert '\\' not in s; s = s.replace('.', ',')
    if len(s) > 4: raise AssertionError('đáp số trả lời ngắn dài hơn 4 kí tự')
    return s
def nopts(r, good, bads, step=1):
    good = F(good); out = [nopt(good)]
    for b in bads:
        o = nopt(F(b))
        if F(b) != good and o not in out: out.append(o)
        if len(out) == 4: return out
    k = 0
    while len(out) < 4:
        k += 1; o = nopt(good + step * k)
        if o not in out: out.append(o)
        assert k < 60
    return out

def QIMG(fn, alt, folder='fig3d', px=300):
    return ('<img src="../../../img/%s/%s" alt="%s" loading="lazy" style="display:block;margin:8px auto;width:min(100%%,%dpx);height:auto">' % (folder, fn, alt, px))

def Q3D(cfg, alt='Figure', px=300):
    from mb_tikz3d import svg
    h = QIMG(svg(cfg), alt, px=px); return (h, h)

# ---------------------------------------------------------------- lắp bộ đề
TD = ('D. Self-practice: Multiple Choice', 'D. Tự luyện: trắc nghiệm')

def _q(b, r, lv, ctx, used):
    for _ in range(500):
        try: q = b(r, lv, ctx)
        except AssertionError: continue
        if q['en'] in used: continue
        if 'opts' in q and len(set(q['opts'])) != 4: continue
        used.add(q['en']); return q
    raise RuntimeError('không sinh được câu: ' + b.__name__)

def _fig(q):
    if 'fig' in q: return q['en'] + q['fig'][0], q['vi'] + q['fig'][1]
    return q['en'], q['vi']

def assemble(A, B, C, D, seeds, ctx_factory=lambda r: {}):
    """A, B, C, D: danh sách hàm sinh (mỗi hàm dùng đúng một lần ở mỗi mức). Trả về danh sách nhóm cho QUIZ (đủ 3 mức)."""
    from mb_lib import LEVEL_PRACTICE
    used = set(); sets = {}; dsets = {}
    for lv, seed in zip((1, 2, 3), seeds):
        r = random.Random(seed); ctx = ctx_factory(r); n = 1; gA, gB, gC, gD = [], [], [], []
        for b in A:
            q = _q(b, r, lv, ctx, used); en, vi = _fig(q); gA.append(M4(n, en, vi, q['opts'][0], q['opts'][1:], q['ee'], q['ev'])); n += 1
        for b in B:
            q = _q(b, r, lv, ctx, used); en, vi = _fig(q); gB.append(tf(n, en, vi, q['truth'], q['ee'], q['ev'])); n += 1
        for b in C:
            q = _q(b, r, lv, ctx, used); en, vi = _fig(q); gC.append(sh(n, en, vi, q['key'], q['ee'], q['ev'], hint=q.get('hint', ('Enter a number.', 'Nhập một số.')))); n += 1
        for b in D:
            q = _q(b, r, lv, ctx, used); en, vi = _fig(q)
            opts = list(q['opts']); good = opts[0]; idx = list(range(4)); r.shuffle(idx); shf = [opts[i] for i in idx]; L = 'abcd'[shf.index(good)]
            gD.append(MCQ(n, (en, vi), shf, L, ('Answer: %s. %s' % (L, q['ee']), 'Đáp án %s. %s' % (L, q['ev'])))); n += 1
        sets[lv] = [gA, gB, gC]; dsets[lv] = gD
    pr = LEVEL_PRACTICE(GRP, sets)
    return pr + [(TD, dsets[lv], [lv]) for lv in (1, 2, 3)]

# =====================================================================================================
# BÀI 9. Các số đặc trưng đo xu thế trung tâm của mẫu số liệu ghép nhóm
# =====================================================================================================
from gdata import GT
import gq
SCN = gq.SC

def stats_ctx(r):
    """Mỗi mức: xoay vòng các tình huống, mỗi tình huống dùng tối đa 2 lần."""
    order = list(range(len(SCN))); r.shuffle(order); return {'q': order * 2, 'i': 0}
def take(ctx, flag=None):
    for _ in range(len(ctx['q'])):
        sc = SCN[ctx['q'][ctx['i'] % len(ctx['q'])]]; ctx['i'] += 1
        if flag is None or sc.get(flag): return sc
    raise AssertionError

def lab(s):
    vi, en = s.split(' / '); return en, vi
UNIT_EN = {'cm': 'cm', 'minutes': 'min', 'points': 'points', 'million VND': 'million VND', 'kWh': 'kWh', 'g': 'g', 'years': 'years', 'hours': 'h'}
def gtab(sc, t, lang, rows=('group', 'freq'), unknown=None):
    """Bảng ghép nhóm ngang, kẻ đủ đường, nhãn và số theo đúng ngôn ngữ."""
    N = ne if lang == 'en' else nv
    gl = lab(sc['gl'])[0 if lang == 'en' else 1]; fl = lab(sc['fl'])[0 if lang == 'en' else 1]
    rowsH = []
    for rw in rows:
        if rw == 'group': L = gl; cells = ['\\([%s;\\,%s)\\)' % (N(t.edge(i)), N(t.edge(i + 1))) for i in range(t.k)]; tot = 'Total' if lang == 'en' else 'Cộng'
        elif rw == 'freq': L = fl; cells = ['\\(x\\)' if i == unknown else '\\(%d\\)' % t.fs[i] for i in range(t.k)]; tot = '\\(n=%d\\)' % t.n if unknown is None else '\\(n=%d\\)' % t.n
        elif rw == 'mid': L = 'Midpoint \\(x_i\\)' if lang == 'en' else 'Giá trị đại diện \\(x_i\\)'; cells = ['\\(%s\\)' % N(t.mid(i)) for i in range(t.k)]; tot = ''
        rowsH.append('<tr><th scope="row">%s</th>%s<td class="mbl-freq-tot">%s</td></tr>' % (L, ''.join('<td>%s</td>' % c for c in cells), tot))
    return '<div class="mbl-tablewrap mbl-freqwrap"><table class="mbl-table mbl-freq"><tbody>%s</tbody></table></div>' % ''.join(rowsH)
def TB(sc, t, **kw): return (gtab(sc, t, 'en', **kw), gtab(sc, t, 'vi', **kw))
def U(sc, lang): return sc['unit'] if lang == 'en' else sc['uv']
def grp(t, i, N): return '\\([%s;\\,%s)\\)' % (N(t.edge(i)), N(t.edge(i + 1)))

def s9_mean(r, lv, ctx):
    sc = take(ctx); t = gq.mkt(r, sc, need=('mean',)); m = t.mean()
    return dict(en='%s Estimate the mean %s (in %s).' % (sc['intro'][0], sc['var'][0], sc['unit']), vi='%s Ước tính %s trung bình (đơn vị %s).' % (sc['intro'][1], sc['var'][1], sc['uv']),
                opts=nopts(r, m, [t.mid(t.mode_group()), m + t.h / 2, m - t.h / 2, sum(t.mid(i) for i in range(t.k)) / t.k], step=1),
                ee='\\(\\bar x=\\dfrac{\\sum n_ix_i}{n}=%s\\) (use the midpoints).' % ne(m), ev='\\(\\bar x=\\dfrac{\\sum n_ix_i}{n}=%s\\) (dùng giá trị đại diện).' % nv(m), fig=TB(sc, t))

def s9_median(r, lv, ctx):
    sc = take(ctx); t = gq.mkt(r, sc, need=('median',)); m = t.median(); g = t.med_group()
    return dict(en='%s Find the median of the %s (in %s).' % (sc['intro'][0], sc['var'][0], sc['unit']), vi='%s Tìm trung vị của %s (đơn vị %s).' % (sc['intro'][1], sc['var'][1], sc['uv']),
                opts=nopts(r, m, [t.mid(g), t.edge(g), t.edge(g + 1), t.mean()]),
                ee='The median group is %s; \\(M_e=%s\\).' % (grp(t, g, ne), ne(m)), ev='Nhóm chứa trung vị là %s; \\(M_e=%s\\).' % (grp(t, g, nv), nv(m)), fig=TB(sc, t))

def s9_mode(r, lv, ctx):
    sc = take(ctx); t = gq.mkt(r, sc, need=('mode',)); m = t.mode(); g = t.mode_group()
    return dict(en='%s Find the mode of the %s (in %s).' % (sc['intro'][0], sc['var'][0], sc['unit']), vi='%s Tìm mốt của %s (đơn vị %s).' % (sc['intro'][1], sc['var'][1], sc['uv']),
                opts=nopts(r, m, [t.mid(g), t.edge(g), t.edge(g + 1), t.mean()]),
                ee='Modal group %s; \\(M_o=%s\\).' % (grp(t, g, ne), ne(m)), ev='Nhóm chứa mốt %s; \\(M_o=%s\\).' % (grp(t, g, nv), nv(m)), fig=TB(sc, t))

def s9_tf_medgroup(r, lv, ctx):
    sc = take(ctx); t = gq.mkt(r, sc); g = t.med_group(); truth = r.random() < 0.5
    c = g if truth else r.choice([i for i in range(t.k) if i != g])
    return dict(en='%s The median of the %s lies in the group %s.' % (sc['intro'][0], sc['var'][0], grp(t, c, ne)), vi='%s Trung vị của %s thuộc nhóm %s.' % (sc['intro'][1], sc['var'][1], grp(t, c, nv)), truth=(c == g),
                ee='\\(\\dfrac n2=%s\\); the cumulative frequency first reaches it in %s.' % (ne(F(t.n, 2)), grp(t, g, ne)), ev='\\(\\dfrac n2=%s\\); tần số tích lũy lần đầu đạt giá trị này ở nhóm %s.' % (nv(F(t.n, 2)), grp(t, g, nv)), fig=TB(sc, t))

def s9_tf_q1(r, lv, ctx):
    sc = take(ctx); t = gq.mkt(r, sc, need=('q1',), nset=(20, 24, 28, 32, 36, 40, 44, 48)); q = t.q1(); truth = r.random() < 0.5
    c = q if truth else r.choice([v for v in (q + F(t.h, 2), q - F(t.h, 2), t.mid(t.quant(1, 4)[0])) if (2 * v).denominator == 1 and v != q])
    if c == q: truth = True
    return dict(en='%s The first quartile of the %s is \\(Q_1=%s\\) %s.' % (sc['intro'][0], sc['var'][0], ne(c), sc['unit']), vi='%s Tứ phân vị thứ nhất của %s là \\(Q_1=%s\\) %s.' % (sc['intro'][1], sc['var'][1], nv(c), sc['uv']), truth=truth,
                ee='\\(\\dfrac n4=%s\\), group %s: \\(Q_1=%s\\).' % (ne(F(t.n, 4)), grp(t, t.quant(1, 4)[0], ne), ne(q)), ev='\\(\\dfrac n4=%s\\), nhóm %s: \\(Q_1=%s\\).' % (nv(F(t.n, 4)), grp(t, t.quant(1, 4)[0], nv), nv(q)), fig=TB(sc, t))

def s9_sh_q3(r, lv, ctx):
    sc = take(ctx); t = gq.mkt(r, sc, need=('q3',), nset=(20, 24, 28, 32, 36, 40, 44, 48)); q = t.q3()
    return dict(en='%s Find the third quartile \\(Q_3\\) of the %s (in %s).' % (sc['intro'][0], sc['var'][0], sc['unit']), vi='%s Tìm tứ phân vị thứ ba \\(Q_3\\) của %s (đơn vị %s).' % (sc['intro'][1], sc['var'][1], sc['uv']), key=key(q),
                ee='\\(\\dfrac{3n}4=%s\\), group %s: \\(Q_3=%s\\).' % (ne(F(3 * t.n, 4)), grp(t, t.quant(3, 4)[0], ne), ne(q)), ev='\\(\\dfrac{3n}4=%s\\), nhóm %s: \\(Q_3=%s\\).' % (nv(F(3 * t.n, 4)), grp(t, t.quant(3, 4)[0], nv), nv(q)), fig=TB(sc, t))

def s9_sh_missing(r, lv, ctx):
    """Ngược: biết số trung bình, tìm tần số còn thiếu."""
    sc = take(ctx)
    for _ in range(300):
        t = gq.mkt(r, sc, need=('mean',)); i = r.randrange(t.k)
        if t.fs[i] >= 2: break
    m = t.mean(); x = t.fs[i]
    other = sum(t.fs[j] * t.mid(j) for j in range(t.k) if j != i); nn = t.n - x
    # (other + x*mid_i) / (nn + x) = m  =>  x = (m*nn - other)/(mid_i - m)
    assert t.mid(i) != m and (m * nn - other) / (t.mid(i) - m) == x
    return dict(en='%s The mean %s is \\(%s\\) %s. Find the missing frequency \\(x\\).' % (sc['intro'][0], sc['var'][0], ne(m), sc['unit']), vi='%s Số trung bình của %s là \\(%s\\) %s. Tìm tần số \\(x\\) còn thiếu.' % (sc['intro'][1], sc['var'][1], nv(m), sc['uv']), key=key(x),
                ee='\\(\\dfrac{%s+%s\\,x}{%d+x}=%s\\Rightarrow x=%d\\).' % (ne(other), ne(t.mid(i)), nn, ne(m), x), ev='\\(\\dfrac{%s+%s\\,x}{%d+x}=%s\\Rightarrow x=%d\\).' % (nv(other), nv(t.mid(i)), nn, nv(m), x),
                fig=(gtab(sc, t, 'en', rows=('group', 'freq'), unknown=i).replace('\\(n=%d\\)' % t.n, '').replace('<td class="mbl-freq-tot">Total</td>', '<td class="mbl-freq-tot"></td>'),
                     gtab(sc, t, 'vi', rows=('group', 'freq'), unknown=i).replace('\\(n=%d\\)' % t.n, '').replace('<td class="mbl-freq-tot">Cộng</td>', '<td class="mbl-freq-tot"></td>')))

def s9_d_mid(r, lv, ctx):
    sc = take(ctx); t = gq.mkt(r, sc); i = r.randrange(t.k); m = t.mid(i)
    return dict(en='%s To estimate the mean, which value represents the group %s?' % (sc['intro'][0], grp(t, i, ne)), vi='%s Khi ước tính số trung bình, giá trị đại diện của nhóm %s là bao nhiêu?' % (sc['intro'][1], grp(t, i, nv)),
                opts=nopts(r, m, [t.edge(i), t.edge(i + 1), t.h, m + t.h]), ee='\\(\\dfrac{%s+%s}2=%s\\).' % (ne(t.edge(i)), ne(t.edge(i + 1)), ne(m)), ev='\\(\\dfrac{%s+%s}2=%s\\).' % (nv(t.edge(i)), nv(t.edge(i + 1)), nv(m)), fig=TB(sc, t))

def s9_d_modal(r, lv, ctx):
    sc = take(ctx); t = gq.mkt(r, sc); g = t.mode_group()
    o = lambda i: tx(grp(t, i, ne), grp(t, i, nv))
    return dict(en='%s Which group contains the mode?' % sc['intro'][0], vi='%s Nhóm nào chứa mốt?' % sc['intro'][1],
                opts=[o(g)] + [o(i) for i in range(t.k) if i != g][:3], ee='It has the greatest frequency (%d).' % t.fs[g], ev='Nhóm có tần số lớn nhất (%d).' % t.fs[g], fig=TB(sc, t))

def s9_d_meaning(r, lv, ctx):
    sc = take(ctx); t = gq.mkt(r, sc, need=('median',)); m = t.median(); a, b = gq.lt(sc, m), gq.ge(sc, m)
    fx = lambda s: s.replace('{,}', '.')
    return dict(en='%s The median of the %s is \\(%s\\) %s. What does this tell us?' % (sc['intro'][0], sc['var'][0], ne(m), sc['unit']), vi='%s Trung vị của %s là \\(%s\\) %s. Điều đó cho biết gì?' % (sc['intro'][1], sc['var'][1], nv(m), sc['uv']),
                opts=[tx('About half of the %s %s, and about half %s.' % (sc['ent'][0], fx(a[0]), fx(b[0])), 'Khoảng một nửa số %s %s và khoảng một nửa %s.' % (sc['ent'][1], a[1].replace('{,}', ','), b[1].replace('{,}', ','))),
                      tx('Most %s have a %s of exactly this value.' % (sc['ent'][0], sc['var'][0]), 'Phần lớn %s có %s đúng bằng giá trị này.' % (sc['ent'][1], sc['var'][1])),
                      tx('It is the sum of all the data divided by %d.' % t.n, 'Đó là tổng mọi số liệu chia cho %d.' % t.n),
                      tx('All of the %s %s.' % (sc['ent'][0], fx(a[0])), 'Tất cả %s đều %s.' % (sc['ent'][1], a[1].replace('{,}', ',')))],
                ee='The median splits the sample into two halves.', ev='Trung vị chia mẫu thành hai nửa có số phần tử bằng nhau.', fig=TB(sc, t))

def s9_d_shift(r, lv, ctx):
    sc = take(ctx, 'shift'); t = gq.mkt(r, sc, need=('mean', 'median')); c = r.choice([1, 2, 3, 5]); (e, v), _ = sc['shift']
    m, me = t.mean(), t.median()
    o = lambda x, y: tx('mean \\(%s\\), median \\(%s\\)' % (ne(x), ne(y)), 'trung bình \\(%s\\), trung vị \\(%s\\)' % (nv(x), nv(y)))
    return dict(en='%s Before the change, the mean is \\(%s\\) and the median is \\(%s\\). %s What are the new mean and median?' % (sc['intro'][0], ne(m), ne(me), e.format(c=c)),
                vi='%s Trước khi thay đổi, số trung bình là \\(%s\\) và trung vị là \\(%s\\). %s Số trung bình và trung vị mới là?' % (sc['intro'][1], nv(m), nv(me), v.format(c=c)),
                opts=[o(m + c, me + c), o(m + c, me), o(m, me + c), o(m * c, me * c) if c > 1 else o(m + 2 * c, me + 2 * c)],
                ee='Adding \\(%d\\) to every value adds \\(%d\\) to both the mean and the median.' % (c, c), ev='Cộng \\(%d\\) vào mọi giá trị thì cả số trung bình và trung vị đều tăng \\(%d\\).' % (c, c))

def s9_d_total(r, lv, ctx):
    sc = take(ctx, 'tot'); t = gq.mkt(r, sc, need=('mean',)); m = t.mean(); tot = t.n * m; e, v, ue, uv = sc['tot']
    return dict(en='%s Use the mean to estimate %s (in %s).' % (sc['intro'][0], e, ue), vi='%s Dùng số trung bình để ước tính %s (đơn vị %s).' % (sc['intro'][1], v, uv),
                opts=nopts(r, tot, [m, t.n * t.mid(t.mode_group()), tot + t.n * t.h / 2, tot - t.n * t.h / 2], step=10),
                ee='Total \\(\\approx n\\bar x=%d\\cdot%s=%s\\).' % (t.n, ne(m), ne(tot)), ev='Tổng \\(\\approx n\\bar x=%d\\cdot%s=%s\\).' % (t.n, nv(m), nv(tot)), fig=TB(sc, t))

def s9_d_compare(r, lv, ctx):
    sc = take(ctx)
    for _ in range(300):
        a = gq.mkt(r, sc, need=('mean',)); b = gq.mkt(r, sc, need=('mean',))
        if a.mean() != b.mean() and a.n != b.n and [a.edge(0), a.h, a.k] == [b.edge(0), b.h, b.k]: break
    else: raise AssertionError
    hi = 'A' if a.mean() > b.mean() else 'B'; lo = 'B' if hi == 'A' else 'A'; M1, M2 = max(a.mean(), b.mean()), min(a.mean(), b.mean())
    o = lambda e, v: tx(e, v)
    return dict(en='%s Two samples were collected. Which statement about their means is correct?' % sc['intro'][0], vi='%s Thu được hai mẫu số liệu. Nhận xét nào về số trung bình của hai mẫu là đúng?' % sc['intro'][1],
                opts=[o('Sample %s has the higher mean (\\(%s\\) against \\(%s\\)).' % (hi, ne(M1), ne(M2)), 'Mẫu %s có trung bình cao hơn (\\(%s\\) so với \\(%s\\)).' % (hi, nv(M1), nv(M2))),
                      o('Sample %s has the higher mean.' % lo, 'Mẫu %s có trung bình cao hơn.' % lo), o('The two means are equal.', 'Hai số trung bình bằng nhau.'),
                      o('They cannot be compared because the sample sizes differ.', 'Không so sánh được vì cỡ mẫu khác nhau.')],
                ee='\\(\\bar x_A=%s\\), \\(\\bar x_B=%s\\).' % (ne(a.mean()), ne(b.mean())), ev='\\(\\bar x_A=%s\\), \\(\\bar x_B=%s\\).' % (nv(a.mean()), nv(b.mean())),
                fig=('<p>Sample A:</p>' + gtab(sc, a, 'en') + '<p>Sample B:</p>' + gtab(sc, b, 'en'), '<p>Mẫu A:</p>' + gtab(sc, a, 'vi') + '<p>Mẫu B:</p>' + gtab(sc, b, 'vi')))

def s9_d_error(r, lv, ctx):
    """Phát hiện lỗi: dùng đầu mút trái thay cho giá trị đại diện."""
    sc = take(ctx); t = gq.mkt(r, sc, need=('mean',)); m = t.mean(); wrong = sum(t.fs[i] * t.edge(i) for i in range(t.k)) / t.n
    assert wrong == m - F(t.h, 2)
    return dict(en='%s Nam estimated the mean and got \\(%s\\) %s, but the correct estimate is \\(%s\\) %s. What mistake did Nam most likely make?' % (sc['intro'][0], ne(wrong), sc['unit'], ne(m), sc['unit']),
                vi='%s Bạn Nam ước tính số trung bình được \\(%s\\) %s, nhưng kết quả đúng là \\(%s\\) %s. Nhiều khả năng bạn Nam đã mắc lỗi gì?' % (sc['intro'][1], nv(wrong), sc['uv'], nv(m), sc['uv']),
                opts=[tx('He used the left end of each group instead of its midpoint.', 'Bạn dùng đầu mút trái của mỗi nhóm thay cho giá trị đại diện.'),
                      tx('He used the right end of each group instead of its midpoint.', 'Bạn dùng đầu mút phải của mỗi nhóm thay cho giá trị đại diện.'),
                      tx('He divided by the number of groups instead of \\(n\\).', 'Bạn chia cho số nhóm thay vì chia cho \\(n\\).'),
                      tx('He forgot the last group.', 'Bạn bỏ sót nhóm cuối cùng.')],
                ee='Using left ends lowers every value by \\(\\dfrac h2=%s\\), so the result is \\(%s\\) less.' % (ne(F(t.h, 2)), ne(F(t.h, 2))), ev='Dùng đầu mút trái làm mỗi giá trị giảm \\(\\dfrac h2=%s\\), nên kết quả nhỏ hơn \\(%s\\).' % (nv(F(t.h, 2)), nv(F(t.h, 2))), fig=TB(sc, t))

def s9_d_middle(r, lv, ctx):
    sc = take(ctx); t = gq.mkt(r, sc, need=('q1', 'q3'), nset=(20, 24, 28, 32, 36, 40, 44, 48)); a, b = t.q1(), t.q3()
    o = lambda x, y: tx('\\([%s;\\,%s]\\)' % (ne(x), ne(y)), '\\([%s;\\,%s]\\)' % (nv(x), nv(y)))
    if len({(a, b), (t.edge(0), b), (a, t.median()), (t.median(), b)}) < 4: raise AssertionError
    return dict(en='%s About half of the %s lie in the middle of the data. Between which two values is their %s?' % (sc['intro'][0], sc['ent'][0], sc['var'][0]),
                vi='%s Khoảng một nửa số %s nằm ở phần giữa của mẫu. %s của họ nằm trong khoảng nào?' % (sc['intro'][1], sc['ent'][1], sc['var'][1].capitalize()),
                opts=[o(a, b), o(t.edge(0), b), o(a, t.median()), o(t.median(), b)],
                ee='The middle half lies between \\(Q_1=%s\\) and \\(Q_3=%s\\).' % (ne(a), ne(b)), ev='Nửa ở giữa nằm giữa \\(Q_1=%s\\) và \\(Q_3=%s\\).' % (nv(a), nv(b)), fig=TB(sc, t))

L9 = dict(A=[s9_mean, s9_median, s9_mode], B=[s9_tf_medgroup, s9_tf_q1], C=[s9_sh_q3, s9_sh_missing],
          D=[s9_d_mid, s9_d_modal, s9_d_meaning, s9_d_shift, s9_d_total, s9_d_compare, s9_d_error, s9_d_middle], ctx=stats_ctx)


# =====================================================================================================
# HÌNH KHÔNG GIAN – công cụ tọa độ (Bài 10, 11)
# =====================================================================================================
def vsub(a, b): return tuple(x - y for x, y in zip(a, b))
def vadd(a, b): return tuple(x + y for x, y in zip(a, b))
def vmul(a, k): return tuple(x * k for x in a)
def cross(a, b): return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
def dot(a, b): return sum(x * y for x, y in zip(a, b))
def Fp(p): return tuple(F(x).limit_denominator(1000) if isinstance(x, float) else F(x) for x in p)
def on_plane(X, A, B, C): return dot(vsub(X, A), cross(vsub(B, A), vsub(C, A))) == 0
def collinear(A, B, C): return cross(vsub(B, A), vsub(C, A)) == (0, 0, 0)
def parallel(u, v): return cross(u, v) == (0, 0, 0) and any(u) and any(v)
def rf(x):
    x = F(x); return str(x.numerator) if x.denominator == 1 else '\\tfrac{%d}{%d}' % (x.numerator, x.denominator)
def lerp(A, B, t): return tuple(a + (b - a) * F(t) for a, b in zip(A, B))
def meet(A, B, C, D):
    """Giao của hai đường thẳng AB, CD (đồng phẳng, không song song) – tính chính xác."""
    u, w = vsub(B, A), vsub(D, C); n = cross(u, w); assert any(n)
    t = F(dot(cross(vsub(C, A), w), n)) / dot(n, n)
    X = vadd(A, vmul(u, t)); assert collinear(C, D, X); return X
def line_plane(A, B, P, Q, R):
    n = cross(vsub(Q, P), vsub(R, P)); u = vsub(B, A); d = dot(n, u); assert d != 0
    t = F(dot(n, vsub(P, A))) / d; return vadd(A, vmul(u, t))
def rel_lines(A, B, C, D):
    u, w = vsub(B, A), vsub(D, C)
    if cross(u, w) == (0, 0, 0): return 'par' if cross(vsub(C, A), u) != (0, 0, 0) else 'same'
    return 'int' if dot(vsub(C, A), cross(u, w)) == 0 else 'skew'

PYR = {'A': (-3, -2, 0), 'B': (2, -2, 0), 'C': (3, 2, 0), 'D': (-2, 2, 0), 'S': (0, 0, F(17, 5))}            # đáy hình bình hành
TRAP = {'A': (-3, -2, 0), 'B': (3, -2, 0), 'C': (F(3, 2), 2, 0), 'D': (F(-3, 2), 2, 0), 'S': (0, 0, F(18, 5))}   # đáy hình thang AB ∥ CD
QUAD = {'A': (-3, -2, 0), 'B': (2, F(-5, 2), 0), 'C': (3, F(3, 2), 0), 'D': (-2, 2, 0), 'S': (0, 0, F(17, 5))}    # đáy tứ giác, AB cắt CD
TET = {'B': (F(-13, 5), 0, 0), 'C': (F(4, 5), -2, 0), 'D': (F(14, 5), F(8, 5), 0), 'A': (F(-1, 5), F(3, 10), F(17, 5))}
CUBE = {'A': (0, 0, 0), 'B': (4, 0, 0), 'C': (4, 4, 0), 'D': (0, 4, 0), 'A′': (0, 0, 4), 'B′': (4, 0, 4), 'C′': (4, 4, 4), 'D′': (0, 4, 4)}
PRISM = {'A': (0, 0, 0), 'B': (4, 0, 0), 'C': (1, 3, 0), 'A′': (0, 0, 4), 'B′': (4, 0, 4), 'C′': (1, 3, 4)}
HL = '#c2410c'; BL = '#1d4ed8'; PU = '#7c3aed'

def G(base, solid, extra=None, segs=(), polys=(), px=300, **kw):
    """Cấu hình hình vẽ: base (đỉnh khối), extra (điểm thêm), segs: [(X, Y, {...}), ...]."""
    P = {k: tuple(float(x) for x in v) for k, v in base.items()}
    for k, v in (extra or {}).items(): P[k] = tuple(float(x) for x in v)
    cfg = {'solid': list(solid), 'points': P, 'segments': [[a, b, o] if o else [a, b] for a, b, o in [(x[0], x[1], x[2] if len(x) > 2 else {}) for x in segs]],
           'polygons': [{'points': list(p), 'fill': c, 'opacity': .3} for p, c in polys], 'px': px}
    cfg.update(kw); return cfg
def seg(a, b, color=None, w=3.0): return (a, b, {'color': color, 'width': w}) if color else (a, b)
def ext(a, b):
    """Đoạn kéo dài (nét đứt mảnh, luôn đứt) – dùng cho đường dựng phụ ngoài khối."""
    return (a, b, {'dash': True, 'force': True, 'color': '#64748b', 'width': 1.6})
def fig3(cfg, alt): return Q3D(cfg, alt)
def L2(a, b): return '%s%s' % (a, b)
def pl(*n): return '\\((%s)\\)' % ''.join(n)

# ---------------- Bài 10: Đường thẳng và mặt phẳng trong không gian ----------------
def _gt_case(r):
    k = r.choice(['center', 'trap', 'quad', 'mid'])
    if k == 'center':
        P = dict(PYR); P['O'] = meet(P['A'], P['C'], P['B'], P['D'])
        planes = (('S', 'A', 'C'), ('S', 'B', 'D')); good = ('S', 'O')
        cand = [('S', 'O'), ('S', 'A'), ('S', 'C'), ('B', 'D'), ('A', 'C'), ('S', 'B')]
        cfg = G(PYR, 'SABCD', {'O': P['O']}, [('A', 'C'), ('B', 'D')])
        txt = ('the pyramid \\(S.ABCD\\) has a parallelogram base, and \\(O\\) is the intersection of \\(AC\\) and \\(BD\\)', 'hình chóp \\(S.ABCD\\) có đáy là hình bình hành, \\(O\\) là giao điểm của \\(AC\\) và \\(BD\\)')
    elif k == 'trap':
        P = dict(TRAP); P['I'] = meet(P['A'], P['D'], P['B'], P['C'])
        planes = (('S', 'A', 'D'), ('S', 'B', 'C')); good = ('S', 'I')
        cand = [('S', 'I'), ('S', 'A'), ('S', 'D'), ('S', 'B'), ('A', 'D'), ('S', 'C')]
        cfg = G(TRAP, 'SABCD', {'I': P['I']}, [ext('D', 'I'), ext('C', 'I'), ('S', 'I', {'color': None, 'width': 1.6, 'dash': True, 'force': True})])
        txt = ('the pyramid \\(S.ABCD\\) has a trapezoid base with \\(AB\\parallel CD\\), and \\(I\\) is the intersection of \\(AD\\) and \\(BC\\)', 'hình chóp \\(S.ABCD\\) có đáy là hình thang \\(AB\\parallel CD\\), \\(I\\) là giao điểm của \\(AD\\) và \\(BC\\)')
    elif k == 'quad':
        P = dict(QUAD); P['J'] = meet(P['A'], P['B'], P['D'], P['C'])
        planes = (('S', 'A', 'B'), ('S', 'C', 'D')); good = ('S', 'J')
        cand = [('S', 'J'), ('S', 'A'), ('S', 'C'), ('A', 'B'), ('S', 'D'), ('C', 'D')]
        cfg = G(QUAD, 'SABCD', {'J': P['J']}, [ext('B', 'J'), ext('C', 'J'), ('S', 'J', {'dash': True, 'force': True, 'width': 1.6})])
        txt = ('the pyramid \\(S.ABCD\\) has a base \\(ABCD\\) in which \\(AB\\) and \\(CD\\) meet at \\(J\\)', 'hình chóp \\(S.ABCD\\) có đáy \\(ABCD\\), trong đó \\(AB\\) và \\(CD\\) cắt nhau tại \\(J\\)')
    else:
        P = dict(PYR); P['O'] = meet(P['A'], P['C'], P['B'], P['D']); P['M'] = lerp(P['S'], P['C'], F(1, 2))
        planes = (('M', 'B', 'D'), ('S', 'A', 'C')); good = ('M', 'O')
        cand = [('M', 'O'), ('S', 'O'), ('M', 'B'), ('B', 'D'), ('M', 'D'), ('A', 'M')]
        cfg = G(PYR, 'SABCD', {'O': P['O'], 'M': P['M']}, [('A', 'C'), ('B', 'D'), ('M', 'B'), ('M', 'D')])
        txt = ('the pyramid \\(S.ABCD\\) has a parallelogram base with centre \\(O\\), and \\(M\\) is the midpoint of \\(SC\\)', 'hình chóp \\(S.ABCD\\) có đáy là hình bình hành tâm \\(O\\), \\(M\\) là trung điểm của \\(SC\\)')
    for X in good: assert all(on_plane(P[X], *[P[n] for n in pln]) for pln in planes)
    ok = [c for c in cand if all(on_plane(P[c[0]], *[P[n] for n in pln]) and on_plane(P[c[1]], *[P[n] for n in pln]) for pln in planes)]
    assert ok == [good]
    return P, planes, good, cand, cfg, txt

def g10_gt(r, lv, ctx):
    P, planes, good, cand, cfg, txt = _gt_case(r)
    wr = cand[1:]; r.shuffle(wr)
    o = lambda c: '\\(%s\\)' % L2(*c)
    return dict(en='In the figure, %s. The line of intersection of %s and %s is…' % (txt[0].replace('centre', 'center'), pl(*planes[0]), pl(*planes[1])), vi='Trong hình vẽ, %s. Giao tuyến của %s và %s là…' % (txt[1], pl(*planes[0]), pl(*planes[1])),
                opts=[o(good)] + [o(c) for c in wr[:3]], ee='\\(%s\\) and \\(%s\\) are two common points of the two planes.' % good, ev='\\(%s\\) và \\(%s\\) là hai điểm chung của hai mặt phẳng.' % good,
                fig=fig3(cfg, 'Pyramid S.ABCD'))

def g10_gd(r, lv, ctx):
    k = r.choice(['tetMN', 'tetNP', 'pyrAM'])
    if k == 'pyrAM':
        P = dict(PYR); P['O'] = meet(P['A'], P['C'], P['B'], P['D']); P['M'] = lerp(P['S'], P['C'], F(1, 2)); P['G'] = meet(P['A'], P['M'], P['S'], P['O'])
        X = line_plane(P['A'], P['M'], P['S'], P['B'], P['D']); assert X == P['G']
        cfg = G(PYR, 'SABCD', {k_: P[k_] for k_ in 'OMG'}, [('A', 'C'), ('B', 'D'), ('S', 'O'), ('A', 'M', {'color': HL, 'width': 2.4})])
        q = ('In the pyramid \\(S.ABCD\\) with a parallelogram base, \\(O=AC\\cap BD\\), \\(M\\) is the midpoint of \\(SC\\) and \\(G=AM\\cap SO\\). The intersection point of the line \\(AM\\) and the plane \\((SBD)\\) is…',
             'Cho hình chóp \\(S.ABCD\\) có đáy là hình bình hành, \\(O=AC\\cap BD\\), \\(M\\) là trung điểm của \\(SC\\) và \\(G=AM\\cap SO\\). Giao điểm của đường thẳng \\(AM\\) và mặt phẳng \\((SBD)\\) là…')
        good, bad = 'G', ['O', 'M', 'S']; why = ('\\(G\\in AM\\) and \\(G\\in SO\\subset(SBD)\\).', '\\(G\\in AM\\) và \\(G\\in SO\\subset(SBD)\\).')
    else:
        P = dict(TET); t = r.choice([F(1, 2), F(1, 3)]); u = r.choice([F(2, 3), F(3, 4)])
        if k == 'tetMN':
            P['M'] = lerp(P['A'], P['B'], t); P['N'] = lerp(P['A'], P['C'], u); P['I'] = meet(P['M'], P['N'], P['B'], P['C'])
            assert line_plane(P['M'], P['N'], P['B'], P['C'], P['D']) == P['I']
            cfg = G(TET, 'ABCD', {k_: P[k_] for k_ in 'MNI'}, [('M', 'N', {'color': HL, 'width': 2.4}), ext('N', 'I'), ext('C', 'I')])
            q = ('In the tetrahedron \\(ABCD\\), \\(M\\in AB\\), \\(N\\in AC\\) with \\(AM=%s\\,AB\\), \\(AN=%s\\,AC\\), and \\(I=MN\\cap BC\\). The intersection point of \\(MN\\) and \\((BCD)\\) is…' % (rf(t), rf(u)),
                 'Cho tứ diện \\(ABCD\\), \\(M\\in AB\\), \\(N\\in AC\\) sao cho \\(AM=%s\\,AB\\), \\(AN=%s\\,AC\\), và \\(I=MN\\cap BC\\). Giao điểm của \\(MN\\) và \\((BCD)\\) là…' % (rf(t), rf(u)))
            good, bad = 'I', ['M', 'N', 'B']; why = ('\\(I\\in MN\\) and \\(I\\in BC\\subset(BCD)\\).', '\\(I\\in MN\\) và \\(I\\in BC\\subset(BCD)\\).')
        else:
            P['N'] = lerp(P['A'], P['C'], t); P['P'] = lerp(P['A'], P['D'], u); P['J'] = meet(P['N'], P['P'], P['C'], P['D'])
            assert line_plane(P['N'], P['P'], P['B'], P['C'], P['D']) == P['J']
            cfg = G(TET, 'ABCD', {k_: P[k_] for k_ in 'NPJ'}, [('N', 'P', {'color': HL, 'width': 2.4}), ext('P', 'J'), ext('D', 'J')])
            q = ('In the tetrahedron \\(ABCD\\), \\(N\\in AC\\), \\(P\\in AD\\) with \\(AN=%s\\,AC\\), \\(AP=%s\\,AD\\), and \\(J=NP\\cap CD\\). The intersection point of \\(NP\\) and \\((BCD)\\) is…' % (rf(t), rf(u)),
                 'Cho tứ diện \\(ABCD\\), \\(N\\in AC\\), \\(P\\in AD\\) sao cho \\(AN=%s\\,AC\\), \\(AP=%s\\,AD\\), và \\(J=NP\\cap CD\\). Giao điểm của \\(NP\\) và \\((BCD)\\) là…' % (rf(t), rf(u)))
            good, bad = 'J', ['N', 'P', 'D']; why = ('\\(J\\in NP\\) and \\(J\\in CD\\subset(BCD)\\).', '\\(J\\in NP\\) và \\(J\\in CD\\subset(BCD)\\).')
    return dict(en=q[0], vi=q[1], opts=['\\(%s\\)' % good] + ['\\(%s\\)' % b for b in bad], ee=why[0], ev=why[1], fig=fig3(cfg, 'Figure'))

def _section(P, edges, plane):
    A_, B_, C_ = plane; pts = []
    n = cross(vsub(B_, A_), vsub(C_, A_))
    for a, b in edges:
        da, db = dot(vsub(P[a], A_), n), dot(vsub(P[b], A_), n)
        if da == 0: X = P[a]
        elif db == 0: X = P[b]
        elif (da > 0) != (db > 0): X = vadd(P[a], vmul(vsub(P[b], P[a]), F(da) / (da - db)))
        else: continue
        if X not in pts: pts.append(X)
    return len(pts)
TET_E = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
PYR_E = [('S', 'A'), ('S', 'B'), ('S', 'C'), ('S', 'D'), ('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')]
SHAPE = {3: ('a triangle', 'tam giác'), 4: ('a quadrilateral', 'tứ giác'), 5: ('a pentagon', 'ngũ giác'), 2: ('a segment', 'một đoạn thẳng')}

def g10_section(r, lv, ctx):
    k = r.choice(['tet3', 'tet4', 'pyr3', 'pyr4'])
    if k == 'tet3':
        P = dict(TET); P['M'] = lerp(P['A'], P['B'], F(1, 2)); P['N'] = lerp(P['A'], P['C'], F(1, 2)); P['P'] = lerp(P['A'], P['D'], F(1, 2))
        pts = 'MNP'; q = ('In the tetrahedron \\(ABCD\\), \\(M, N, P\\) are the midpoints of \\(AB, AC, AD\\).', 'Cho tứ diện \\(ABCD\\), \\(M, N, P\\) lần lượt là trung điểm của \\(AB, AC, AD\\).'); base, solid, E = TET, 'ABCD', TET_E
    elif k == 'tet4':
        P = dict(TET); P['M'] = lerp(P['A'], P['B'], F(1, 2)); P['N'] = lerp(P['A'], P['C'], F(1, 2)); P['P'] = lerp(P['C'], P['D'], F(1, 2))
        pts = 'MNP'; q = ('In the tetrahedron \\(ABCD\\), \\(M, N\\) are the midpoints of \\(AB, AC\\) and \\(P\\) is the midpoint of \\(CD\\).', 'Cho tứ diện \\(ABCD\\), \\(M, N\\) là trung điểm của \\(AB, AC\\) và \\(P\\) là trung điểm của \\(CD\\).'); base, solid, E = TET, 'ABCD', TET_E
    elif k == 'pyr3':
        P = dict(PYR); P['M'] = lerp(P['S'], P['A'], F(1, 2)); P['N'] = lerp(P['S'], P['B'], F(1, 2)); P['P'] = lerp(P['S'], P['C'], F(1, 2))
        pts = 'MNP'; q = ('In the pyramid \\(S.ABCD\\) with a parallelogram base, \\(M, N, P\\) are the midpoints of \\(SA, SB, SC\\).', 'Cho hình chóp \\(S.ABCD\\) có đáy là hình bình hành, \\(M, N, P\\) lần lượt là trung điểm của \\(SA, SB, SC\\).'); base, solid, E = PYR, 'SABCD', PYR_E
    else:
        P = dict(PYR); P['M'] = lerp(P['S'], P['C'], F(1, 2))
        pts = 'ABM'; q = ('In the pyramid \\(S.ABCD\\) with a parallelogram base, \\(M\\) is the midpoint of \\(SC\\).', 'Cho hình chóp \\(S.ABCD\\) có đáy là hình bình hành, \\(M\\) là trung điểm của \\(SC\\).'); base, solid, E = PYR, 'SABCD', PYR_E
    nside = _section(P, E, [P[c] for c in pts]); good = SHAPE[nside]
    o = [tx(*good)] + [tx(*SHAPE[s]) for s in (3, 4, 5, 2) if s != nside][:3]
    extra = {c: P[c] for c in pts if c not in base}
    return dict(en='%s The cross-section of the solid by the plane \\((%s)\\) is…' % (q[0], pts), vi='%s Thiết diện của khối cắt bởi mặt phẳng \\((%s)\\) là…' % (q[1], pts), opts=o,
                ee='The plane meets %d edges of the solid, so the section has %d vertices.' % (nside, nside), ev='Mặt phẳng cắt %d cạnh của khối nên thiết diện có %d đỉnh.' % (nside, nside),
                fig=fig3(G(base, solid, extra, []), 'Solid with marked points'))

def g10_collinear(r, lv, ctx):
    P = dict(TET); rs = [F(1, 4), F(1, 3), F(2, 5), F(1, 2), F(3, 5), F(2, 3)]
    a, b, c = r.sample(rs, 3)
    if b > F(1, 2): raise AssertionError                                                 # N không sát C: nhãn N không bị nhiều nét cắt qua
    P['M'] = lerp(P['A'], P['B'], a); P['N'] = lerp(P['A'], P['C'], b); P['P'] = lerp(P['A'], P['D'], c)
    P['I'] = meet(P['M'], P['N'], P['B'], P['C']); P['J'] = meet(P['N'], P['P'], P['C'], P['D']); P['K'] = meet(P['M'], P['P'], P['B'], P['D'])
    if max(abs(x) for X in 'IJK' for x in P[X]) > F(26, 5): raise AssertionError          # các giao điểm không quá xa: hình rõ, không bị thu nhỏ
    assert collinear(P['I'], P['J'], P['K'])
    cand = [('I', 'J', 'K'), ('I', 'J', 'B'), ('M', 'N', 'K'), ('I', 'K', 'C'), ('J', 'K', 'B'), ('M', 'J', 'B')]
    ok = [x for x in cand if collinear(*[P[n] for n in x])]; assert ok == [('I', 'J', 'K')]
    wr = cand[1:]; r.shuffle(wr)
    o = lambda x: '\\(%s,\\ %s,\\ %s\\)' % x
    cfg = G(TET, 'ABCD', {k_: P[k_] for k_ in 'MNPIJK'}, [('M', 'N'), ('N', 'P'), ('M', 'P'), ext('N', 'I'), ext('C', 'I'), ext('P', 'J'), ext('D', 'J'), ext('P', 'K'), ext('D', 'K')], px=320)
    rt = '\\(AM=%s\\,AB\\), \\(AN=%s\\,AC\\), \\(AP=%s\\,AD\\)' % tuple(rf(x) for x in (a, b, c))
    return dict(en='In the tetrahedron \\(ABCD\\), \\(M\\in AB\\), \\(N\\in AC\\), \\(P\\in AD\\) with %s; \\(I=MN\\cap BC\\), \\(J=NP\\cap CD\\), \\(K=MP\\cap BD\\). Which three points are collinear?' % rt,
                vi='Cho tứ diện \\(ABCD\\), \\(M\\in AB\\), \\(N\\in AC\\), \\(P\\in AD\\) với %s; \\(I=MN\\cap BC\\), \\(J=NP\\cap CD\\), \\(K=MP\\cap BD\\). Ba điểm nào thẳng hàng?' % rt,
                opts=[o(('I', 'J', 'K'))] + [o(x) for x in wr[:3]], ee='\\(I, J, K\\) are common points of \\((MNP)\\) and \\((BCD)\\), so they lie on the line of intersection.',
                ev='\\(I, J, K\\) là các điểm chung của \\((MNP)\\) và \\((BCD)\\) nên cùng nằm trên giao tuyến.', fig=fig3(cfg, 'Tetrahedron with I, J, K'))

DET = [  # (mệnh đề, xác định đúng một mặt phẳng?)
 (('three non-collinear points', 'ba điểm không thẳng hàng'), True), (('three collinear points', 'ba điểm thẳng hàng'), False),
 (('a line and a point not on it', 'một đường thẳng và một điểm không thuộc nó'), True), (('a line and a point on it', 'một đường thẳng và một điểm thuộc nó'), False),
 (('two intersecting lines', 'hai đường thẳng cắt nhau'), True), (('two parallel lines', 'hai đường thẳng song song'), True), (('two points', 'hai điểm'), False), (('a single line', 'một đường thẳng'), False)]
def g10_determine(r, lv, ctx):
    want = r.choice([True, False])
    good = r.choice([d for d in DET if d[1] == want]); bad = r.sample([d for d in DET if d[1] != want], 3)
    q = r.choice([('Which of the following determines exactly one plane?', 'Trường hợp nào sau đây xác định đúng một mặt phẳng?'), ('Through which of the following can we draw exactly one plane?', 'Có đúng một mặt phẳng đi qua đối tượng nào sau đây?')]) if want else \
        r.choice([('Which of the following does NOT determine a unique plane?', 'Trường hợp nào sau đây KHÔNG xác định được duy nhất một mặt phẳng?'), ('Through which of the following can we draw infinitely many planes?', 'Có vô số mặt phẳng đi qua đối tượng nào sau đây?')])
    if not want and q[0].startswith('Through'):
        bad = [d for d in DET if d[1]][:0] + r.sample([d for d in DET if d[1]], 3); good = r.choice([d for d in DET if not d[1] and d[0][0] != 'three non-collinear points'])
    return dict(en=q[0], vi=q[1], opts=[tx(*good[0])] + [tx(*b[0]) for b in bad], ee='A plane is determined by three non-collinear points, a line and a point off it, two intersecting lines or two parallel lines.',
                ev='Mặt phẳng được xác định bởi ba điểm không thẳng hàng, một đường thẳng và một điểm ngoài nó, hai đường thẳng cắt nhau hoặc hai đường thẳng song song.')

def g10_point_plane(r, lv, ctx):
    P = dict(PYR); P['O'] = meet(P['A'], P['C'], P['B'], P['D']); P['M'] = lerp(P['S'], P['C'], F(1, 2)); P['N'] = lerp(P['S'], P['A'], F(1, 2))
    X = r.choice(['O', 'M', 'N'])
    planes = [('S', 'A', 'C'), ('S', 'A', 'B'), ('S', 'B', 'C'), ('S', 'C', 'D'), ('S', 'A', 'D'), ('S', 'B', 'D')]
    inn = [p for p in planes if on_plane(P[X], *[P[n] for n in p])]; out = [p for p in planes if p not in inn]
    good = r.choice(inn); wr = r.sample(out, 3)
    nm = {'O': ('\\(O\\) is the intersection of \\(AC\\) and \\(BD\\)', '\\(O\\) là giao điểm của \\(AC\\) và \\(BD\\)'), 'M': ('\\(M\\) is the midpoint of \\(SC\\)', '\\(M\\) là trung điểm của \\(SC\\)'), 'N': ('\\(N\\) is the midpoint of \\(SA\\)', '\\(N\\) là trung điểm của \\(SA\\)')}[X]
    o = lambda p: pl(*p)
    cfg = G(PYR, 'SABCD', {X: P[X]}, [('A', 'C'), ('B', 'D')] if X == 'O' else [])
    return dict(en='In the pyramid \\(S.ABCD\\) with a parallelogram base, %s. The point \\(%s\\) lies in which plane?' % (nm[0], X), vi='Cho hình chóp \\(S.ABCD\\) có đáy là hình bình hành, %s. Điểm \\(%s\\) thuộc mặt phẳng nào?' % (nm[1], X),
                opts=[o(good)] + [o(p) for p in wr], ee='\\(%s\\) lies on a line of the plane %s.' % (X, pl(*good)), ev='\\(%s\\) thuộc một đường thẳng nằm trong mặt phẳng %s.' % (X, pl(*good)), fig=fig3(cfg, 'Pyramid'))

def g10_common(r, lv, ctx):
    k = r.choice(['adj', 'opp', 'tet'])
    if k == 'adj': q = ('the planes \\((SAB)\\) and \\((SBC)\\) of the pyramid \\(S.ABCD\\)', 'hai mặt phẳng \\((SAB)\\) và \\((SBC)\\) của hình chóp \\(S.ABCD\\)'); line = ('the line \\(SB\\)', 'đường thẳng \\(SB\\)')
    elif k == 'opp': q = ('the planes \\((SAC)\\) and \\((SBD)\\) of the pyramid \\(S.ABCD\\)', 'hai mặt phẳng \\((SAC)\\) và \\((SBD)\\) của hình chóp \\(S.ABCD\\)'); line = ('the line \\(SO\\) (\\(O=AC\\cap BD\\))', 'đường thẳng \\(SO\\) (\\(O=AC\\cap BD\\))')
    else: q = ('the planes \\((ABC)\\) and \\((ABD)\\) of the tetrahedron \\(ABCD\\)', 'hai mặt phẳng \\((ABC)\\) và \\((ABD)\\) của tứ diện \\(ABCD\\)'); line = ('the line \\(AB\\)', 'đường thẳng \\(AB\\)')
    return dict(en='How many common points do %s have?' % q[0], vi='%s có bao nhiêu điểm chung?' % (q[1][0].upper() + q[1][1:]),
                opts=[tx('infinitely many: all the points of %s' % line[0], 'vô số: mọi điểm của %s' % line[1]), tx('exactly one point', 'đúng một điểm'), tx('exactly two points', 'đúng hai điểm'), tx('no common point', 'không có điểm chung')],
                ee='Two different planes with a common point meet along a whole line.', ev='Hai mặt phẳng phân biệt có điểm chung thì cắt nhau theo cả một đường thẳng.')

def g10_area_ratio(r, lv, ctx):
    k = r.choice([F(1, 2), F(1, 3), F(2, 3), F(1, 4), F(3, 4)]); P = dict(TET)
    for n_ in 'BCD': P[{'B': 'M', 'C': 'N', 'D': 'P'}[n_]] = lerp(P['A'], P[n_], k)
    # tỉ số diện tích MNP / BCD = k^2 (tam giác đồng dạng, tỉ số k) – kiểm bằng tích có hướng
    area = lambda X, Y, Z: dot(cross(vsub(Y, X), vsub(Z, X)), cross(vsub(Y, X), vsub(Z, X)))
    assert area(P['M'], P['N'], P['P']) / area(P['B'], P['C'], P['D']) == k ** 4
    kk = k * k; o = lambda x: ne(x) if x.denominator == 1 else '\\dfrac{%d}{%d}' % (x.numerator, x.denominator)
    return dict(en='In the tetrahedron \\(ABCD\\), \\(M, N, P\\) lie on \\(AB, AC, AD\\) with \\(\\dfrac{AM}{AB}=\\dfrac{AN}{AC}=\\dfrac{AP}{AD}=%s\\). The ratio of the area of triangle \\(MNP\\) to the area of triangle \\(BCD\\) is…' % o(k),
                vi='Cho tứ diện \\(ABCD\\), các điểm \\(M, N, P\\) thuộc \\(AB, AC, AD\\) sao cho \\(\\dfrac{AM}{AB}=\\dfrac{AN}{AC}=\\dfrac{AP}{AD}=%s\\). Tỉ số diện tích tam giác \\(MNP\\) và tam giác \\(BCD\\) bằng…' % o(k),
                opts=[o(kk), o(k), o(2 * k * (1 - k)) if 2 * k * (1 - k) not in (kk, k) else o(kk / 2), o(1 - kk)],
                ee='\\(MN, NP, PM\\) are parallel to \\(BC, CD, DB\\) with ratio \\(%s\\): area ratio \\(\\left(%s\\right)^2=%s\\).' % (o(k), o(k), o(kk)), ev='\\(MN, NP, PM\\) song song với \\(BC, CD, DB\\) với tỉ số \\(%s\\): tỉ số diện tích \\(\\left(%s\\right)^2=%s\\).' % (o(k), o(k), o(kk)),
                fig=fig3(G(TET, 'ABCD', {c: P[c] for c in 'MNP'}, [('M', 'N', {'color': HL, 'width': 2.4}), ('N', 'P', {'color': HL, 'width': 2.4}), ('P', 'M', {'color': HL, 'width': 2.4})]), 'Tetrahedron with triangle MNP'))

def g10_line_in(r, lv, ctx):
    P = dict(PYR); P['O'] = meet(P['A'], P['C'], P['B'], P['D']); P['M'] = lerp(P['S'], P['C'], F(1, 2))
    pln = r.choice([('S', 'A', 'C'), ('S', 'B', 'D'), ('A', 'B', 'M')])
    lines = [('S', 'O'), ('A', 'M'), ('B', 'D'), ('S', 'B'), ('A', 'C'), ('O', 'M'), ('S', 'D'), ('B', 'M'), ('C', 'D'), ('S', 'A')]
    inn = [l for l in lines if on_plane(P[l[0]], *[P[n] for n in pln]) and on_plane(P[l[1]], *[P[n] for n in pln])]
    out = [l for l in lines if l not in inn]
    good = r.choice(inn); wr = r.sample(out, 3); o = lambda l: '\\(%s\\)' % L2(*l)
    return dict(en='In the pyramid \\(S.ABCD\\) with a parallelogram base, \\(O=AC\\cap BD\\) and \\(M\\) is the midpoint of \\(SC\\). Which line lies in the plane %s?' % pl(*pln),
                vi='Cho hình chóp \\(S.ABCD\\) có đáy là hình bình hành, \\(O=AC\\cap BD\\), \\(M\\) là trung điểm của \\(SC\\). Đường thẳng nào nằm trong mặt phẳng %s?' % pl(*pln),
                opts=[o(good)] + [o(l) for l in wr], ee='Both points of \\(%s\\) belong to %s.' % (L2(*good), pl(*pln)), ev='Hai điểm của \\(%s\\) đều thuộc %s.' % (L2(*good), pl(*pln)),
                fig=fig3(G(PYR, 'SABCD', {'O': P['O'], 'M': P['M']}, [('A', 'C'), ('B', 'D')]), 'Pyramid'))

def g10_count_planes(r, lv, ctx):
    n = r.choice([5, 6, 7, 8, 9, 10]); c = n * (n - 1) * (n - 2) // 6
    return dict(en='There are %d points in space, no four of them in one plane. How many planes pass through three of them?' % n, vi='Cho %d điểm trong không gian, không có bốn điểm nào đồng phẳng. Có bao nhiêu mặt phẳng đi qua ba trong số các điểm đó?' % n,
                opts=[str(c), str(n * (n - 1) // 2), str(n * (n - 1) * (n - 2)), str(c + n)], ee='\\(\\mathrm C_{%d}^3=%d\\).' % (n, c), ev='\\(\\mathrm C_{%d}^3=%d\\).' % (n, c))

def g10_solid_count(r, lv, ctx):
    sol = r.choice(['pyr', 'prism']); n = r.choice([3, 4, 5, 6, 7, 8]); what = r.choice(['edges', 'faces', 'verts'])
    val = {'pyr': {'edges': 2 * n, 'faces': n + 1, 'verts': n + 1}, 'prism': {'edges': 3 * n, 'faces': n + 2, 'verts': 2 * n}}[sol][what]
    W = {'edges': ('edges', 'cạnh'), 'faces': ('faces', 'mặt'), 'verts': ('vertices', 'đỉnh')}[what]; S_ = {'pyr': ('pyramid', 'Hình chóp'), 'prism': ('prism', 'Hình lăng trụ')}[sol]
    return dict(en='A %s has a base with %d sides. How many %s does it have?' % (S_[0], n, W[0]), vi='%s có đáy là đa giác %d cạnh. Số %s của nó là…' % (S_[1], n, W[1]),
                opts=[str(val)] + [str(v) for v in dict.fromkeys([val + 1, val - 1, 2 * n + 1, n, 3 * n, n + 2, 2 * n]) if v != val][:3], ee='Count the base(s) and the lateral parts: %d.' % val, ev='Đếm phần đáy và phần bên: %d.' % val)

TF10 = [('Three points always lie in exactly one plane.', 'Ba điểm bất kì luôn nằm trong đúng một mặt phẳng.', False, 'Three collinear points lie in infinitely many planes.', 'Ba điểm thẳng hàng nằm trong vô số mặt phẳng.'),
        ('If two points of a line lie in a plane, every point of the line lies in that plane.', 'Nếu một đường thẳng có hai điểm phân biệt thuộc một mặt phẳng thì mọi điểm của đường thẳng đều thuộc mặt phẳng đó.', True, 'This is a basic property (axiom).', 'Đây là một tính chất thừa nhận.'),
        ('Two different planes can have exactly one common point.', 'Hai mặt phẳng phân biệt có thể có đúng một điểm chung.', False, 'If they share a point, they share a whole line.', 'Nếu có điểm chung thì chúng có chung cả một đường thẳng.'),
        ('A tetrahedron has 4 faces and 6 edges.', 'Tứ diện có 4 mặt và 6 cạnh.', True, '4 triangular faces, 6 edges.', '4 mặt tam giác, 6 cạnh.'),
        ('A line and a point on it determine exactly one plane.', 'Một đường thẳng và một điểm thuộc nó xác định đúng một mặt phẳng.', False, 'The point must be off the line.', 'Điểm phải không thuộc đường thẳng.'),
        ('There exist four points that do not lie in one plane.', 'Tồn tại bốn điểm không cùng thuộc một mặt phẳng.', True, 'This is a basic property (axiom).', 'Đây là một tính chất thừa nhận.')]
def g10_tf1(r, lv, ctx):
    e = TF10[(lv - 1) * 2 % 6]; return dict(en=e[0], vi=e[1], truth=e[2], ee=e[3], ev=e[4])
def g10_tf2(r, lv, ctx):
    e = TF10[((lv - 1) * 2 + 1) % 6]; return dict(en=e[0], vi=e[1], truth=e[2], ee=e[3], ev=e[4])
def g10_sh_lines(r, lv, ctx):
    n = r.choice([6, 7, 8, 9, 10, 11, 12]); c = n * (n - 1) // 2
    return dict(en='There are %d points in space, no three of them on one line. How many lines pass through two of them?' % n, vi='Cho %d điểm trong không gian, không có ba điểm nào thẳng hàng. Có bao nhiêu đường thẳng đi qua hai trong số các điểm đó?' % n, key=key(c),
                ee='\\(\\mathrm C_{%d}^2=%d\\).' % (n, c), ev='\\(\\mathrm C_{%d}^2=%d\\).' % (n, c))
def g10_sh_ratio(r, lv, ctx):
    P = dict(PYR); P['O'] = meet(P['A'], P['C'], P['B'], P['D']); P['M'] = lerp(P['S'], P['C'], F(1, 2)); P['G'] = meet(P['A'], P['M'], P['S'], P['O'])
    which = r.choice(['AG/GM', 'SG/GO', 'SO/GO'])
    d = lambda X, Y: dot(vsub(P[X], P[Y]), vsub(P[X], P[Y]))
    val = {'AG/GM': F(2), 'SG/GO': F(2), 'SO/GO': F(3)}[which]
    a, b = which.split('/'); assert d(a[0], a[1]) == val ** 2 * d(b[0], b[1])
    return dict(en='In the pyramid \\(S.ABCD\\) with a parallelogram base, \\(O=AC\\cap BD\\), \\(M\\) is the midpoint of \\(SC\\) and \\(G\\) is the intersection point of \\(AM\\) and \\((SBD)\\). Find \\(\\dfrac{%s}{%s}\\).' % (a, b),
                vi='Cho hình chóp \\(S.ABCD\\) có đáy là hình bình hành, \\(O=AC\\cap BD\\), \\(M\\) là trung điểm của \\(SC\\) và \\(G\\) là giao điểm của \\(AM\\) với \\((SBD)\\). Tính \\(\\dfrac{%s}{%s}\\).' % (a, b), key=key(val),
                ee='\\(G=AM\\cap SO\\) is the centroid of triangle \\(SAC\\): \\(\\dfrac{%s}{%s}=%s\\).' % (a, b, ne(val)), ev='\\(G=AM\\cap SO\\) là trọng tâm tam giác \\(SAC\\): \\(\\dfrac{%s}{%s}=%s\\).' % (a, b, ne(val)),
                fig=fig3(G(PYR, 'SABCD', {k_: P[k_] for k_ in 'OMG'}, [('A', 'C'), ('B', 'D'), ('S', 'O'), ('A', 'M')]), 'Pyramid with G'))

L10 = dict(A=[g10_count_planes, g10_solid_count, g10_gt], B=[g10_tf1, g10_tf2], C=[g10_sh_lines, g10_sh_ratio],
           D=[g10_gd, g10_section, g10_collinear, g10_determine, g10_point_plane, g10_common, g10_area_ratio, g10_line_in])


# ---------------- Bài 11: Hai đường thẳng song song ----------------
REL = {'par': ('parallel', 'song song'), 'int': ('intersecting', 'cắt nhau'), 'skew': ('skew', 'chéo nhau')}
def p11_rel(r, lv, ctx):
    """Vị trí tương đối của hai đường thẳng trong hình lập phương (có cả đường chéo mặt)."""
    P = dict(CUBE); names = list(P)
    for _ in range(200):
        a, b = r.sample(names, 2); c, d = r.sample(names, 2)
        if {a, b} & {c, d}: continue
        k = rel_lines(P[a], P[b], P[c], P[d])
        if k != 'same': break
    want = r.choice(['par', 'int', 'skew'])
    for _ in range(400):
        a, b = r.sample(names, 2); c, d = r.sample(names, 2)
        if len({a, b, c, d}) < 4: continue
        if rel_lines(P[a], P[b], P[c], P[d]) == want: break
    else: raise AssertionError
    k = want; o = [tx(*REL[k])] + [tx(*REL[x]) for x in REL if x != k] + [tx('perpendicular and intersecting', 'vuông góc và cắt nhau') if k != 'int' else tx('they coincide', 'trùng nhau')]
    hl = [(a, b, {'color': HL, 'width': 3.0}), (c, d, {'color': BL, 'width': 3.0})]
    return dict(en='In the cube \\(ABCD.A′B′C′D′\\), what is the relative position of the lines \\(%s%s\\) and \\(%s%s\\)?' % (a, b, c, d), vi='Trong hình lập phương \\(ABCD.A′B′C′D′\\), vị trí tương đối của hai đường thẳng \\(%s%s\\) và \\(%s%s\\) là…' % (a, b, c, d),
                opts=o[:4], ee='The two lines are %s.' % REL[k][0], ev='Hai đường thẳng đó %s.' % REL[k][1], fig=fig3(G(CUBE, list(CUBE), None, hl), 'Cube'))

def p11_parallel_to(r, lv, ctx):
    P = dict(PYR); pairs = [('SA', 'SB', 'M', 'N'), ('SB', 'SC', 'N', 'P'), ('SC', 'SD', 'P', 'Q'), ('SA', 'SD', 'M', 'Q')]
    e1, e2, X, Y = r.choice(pairs); P[X] = lerp(P['S'], P[e1[1]], F(1, 2)); P[Y] = lerp(P['S'], P[e2[1]], F(1, 2))
    cand = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('S', 'C'), ('A', 'C'), ('S', 'A'), ('B', 'D'), ('S', 'B'), ('S', 'D')]
    u = vsub(P[Y], P[X]); par = [c for c in cand if parallel(u, vsub(P[c[1]], P[c[0]]))]; no = [c for c in cand if c not in par]
    good = r.choice(par); wr = r.sample(no, 3); o = lambda c: '\\(%s\\)' % L2(*c)
    return dict(en='In the pyramid \\(S.ABCD\\) with a parallelogram base, \\(%s, %s\\) are the midpoints of \\(%s, %s\\). The line \\(%s%s\\) is parallel to…' % (X, Y, e1, e2, X, Y),
                vi='Cho hình chóp \\(S.ABCD\\) có đáy là hình bình hành, \\(%s, %s\\) lần lượt là trung điểm của \\(%s, %s\\). Đường thẳng \\(%s%s\\) song song với…' % (X, Y, e1, e2, X, Y),
                opts=[o(good)] + [o(c) for c in wr], ee='\\(%s%s\\) is a midline of triangle \\(S%s%s\\), so \\(%s%s\\parallel %s%s\\); and \\(ABCD\\) is a parallelogram.' % (X, Y, e1[1], e2[1], X, Y, e1[1], e2[1]),
                ev='\\(%s%s\\) là đường trung bình của tam giác \\(S%s%s\\) nên \\(%s%s\\parallel %s%s\\); lại có \\(ABCD\\) là hình bình hành.' % (X, Y, e1[1], e2[1], X, Y, e1[1], e2[1]),
                fig=fig3(G(PYR, 'SABCD', {X: P[X], Y: P[Y]}, [(X, Y, {'color': HL, 'width': 2.6})]), 'Pyramid with a midline'))

def p11_gt_par(r, lv, ctx):
    trap = r.random() < 0.4; base = TRAP if trap else PYR; P = dict(base)
    k = (('S', 'A', 'B'), ('S', 'C', 'D'), ('A', 'B')) if trap else r.choice([(('S', 'A', 'B'), ('S', 'C', 'D'), ('A', 'B')), (('S', 'A', 'D'), ('S', 'B', 'C'), ('A', 'D'))])
    p1, p2, ab = k; u = cross(cross(vsub(P[p1[1]], P[p1[0]]), vsub(P[p1[2]], P[p1[0]])), cross(vsub(P[p2[1]], P[p2[0]]), vsub(P[p2[2]], P[p2[0]])))
    assert parallel(u, vsub(P[ab[1]], P[ab[0]]))
    other = ('A', 'D') if ab == ('A', 'B') else ('A', 'B')
    o = [tx('the line through \\(S\\) parallel to \\(%s\\)' % L2(*ab), 'đường thẳng qua \\(S\\) và song song với \\(%s\\)' % L2(*ab)), tx('the line through \\(S\\) parallel to \\(%s\\)' % L2(*other), 'đường thẳng qua \\(S\\) và song song với \\(%s\\)' % L2(*other)),
         tx('the line \\(SO\\), where \\(O=AC\\cap BD\\)', 'đường thẳng \\(SO\\), với \\(O=AC\\cap BD\\)'), tx('the two planes have only the point \\(S\\) in common', 'hai mặt phẳng chỉ có một điểm chung \\(S\\)')]
    Sx = P['S']; d_ = vsub(P[ab[1]], P[ab[0]]); e1 = vadd(Sx, vmul(d_, F(-3, 5))); e2 = vadd(Sx, vmul(d_, F(3, 5)))
    bt = ('a trapezoid base with \\(AB\\parallel CD\\)', 'đáy là hình thang với \\(AB\\parallel CD\\)') if trap else ('a parallelogram base', 'đáy là hình bình hành')
    if trap: o[2] = tx('the line \\(SI\\), where \\(I=AD\\cap BC\\)', 'đường thẳng \\(SI\\), với \\(I=AD\\cap BC\\)')
    return dict(en='The pyramid \\(S.ABCD\\) has %s. The line of intersection of %s and %s is…' % (bt[0], pl(*p1), pl(*p2)), vi='Cho hình chóp \\(S.ABCD\\) có %s. Giao tuyến của %s và %s là…' % (bt[1], pl(*p1), pl(*p2)),
                opts=o, ee='The planes contain the parallel lines \\(%s\\) and \\(%s\\) and share \\(S\\), so the line of intersection passes through \\(S\\) and is parallel to \\(%s\\).' % (L2(*ab), 'CD' if ab == ('A', 'B') else 'BC', L2(*ab)),
                ev='Hai mặt phẳng chứa hai đường thẳng song song \\(%s\\), \\(%s\\) và có điểm chung \\(S\\) nên giao tuyến qua \\(S\\) và song song với \\(%s\\).' % (L2(*ab), 'CD' if ab == ('A', 'B') else 'BC', L2(*ab)),
                fig=fig3(G(base, 'SABCD', {'_e1': e1, 'd': e2}, [('_e1', 'd', {'color': HL, 'width': 2.4})], nolabel=[]), 'Pyramid with the line of intersection'))

def p11_thales(r, lv, ctx):
    k = r.choice([F(1, 3), F(2, 3), F(1, 4), F(3, 4), F(2, 5), F(3, 5)]); ab = r.choice([6, 8, 9, 10, 12, 15, 16, 20])
    if (k * ab).denominator != 1: raise AssertionError
    P = dict(TET); P['M'] = lerp(P['A'], P['B'], k); P['N'] = lerp(P['A'], P['C'], k)
    assert parallel(vsub(P['N'], P['M']), vsub(P['C'], P['B']))
    v = k * ab; o = lambda x: nopt(x)
    return dict(en='In the tetrahedron \\(ABCD\\), \\(M\\in AB\\), \\(N\\in AC\\) with \\(\\dfrac{AM}{AB}=\\dfrac{AN}{AC}=%s\\) and \\(BC=%d\\). Then \\(MN\\parallel BC\\) and \\(MN=\\)…' % (rf(k).replace('tfrac', 'dfrac'), ab),
                vi='Cho tứ diện \\(ABCD\\), \\(M\\in AB\\), \\(N\\in AC\\) sao cho \\(\\dfrac{AM}{AB}=\\dfrac{AN}{AC}=%s\\) và \\(BC=%d\\). Khi đó \\(MN\\parallel BC\\) và \\(MN=\\)…' % (rf(k).replace('tfrac', 'dfrac'), ab),
                opts=nopts(r, v, [(1 - k) * ab, ab / 2, ab - k, ab / k if (ab / k).denominator == 1 else ab + 1]), ee='Thales: \\(MN=%s\\cdot%d=%s\\).' % (rf(k).replace('tfrac', 'dfrac'), ab, ne(v)), ev='Định lí Thalès: \\(MN=%s\\cdot%d=%s\\).' % (rf(k).replace('tfrac', 'dfrac'), ab, nv(v)),
                fig=fig3(G(TET, 'ABCD', {'M': P['M'], 'N': P['N']}, [('M', 'N', {'color': HL, 'width': 2.6})]), 'Tetrahedron'))

CON11 = [(('Two lines with no common point are always parallel.', 'Hai đường thẳng không có điểm chung thì luôn song song.'), False),
         (('Two parallel lines lie in one plane and have no common point.', 'Hai đường thẳng song song thì cùng nằm trong một mặt phẳng và không có điểm chung.'), True),
         (('Through a point not on a line there is exactly one line parallel to it.', 'Qua một điểm nằm ngoài một đường thẳng có đúng một đường thẳng song song với đường thẳng đó.'), True),
         (('Two lines parallel to a third line are skew.', 'Hai đường thẳng cùng song song với đường thẳng thứ ba thì chéo nhau.'), False),
         (('Two skew lines may lie in one plane.', 'Hai đường thẳng chéo nhau có thể cùng nằm trong một mặt phẳng.'), False),
         (('If three planes meet in three different lines, these lines are concurrent or pairwise parallel.', 'Nếu ba mặt phẳng cắt nhau theo ba giao tuyến phân biệt thì ba giao tuyến đó đồng quy hoặc đôi một song song.'), True),
         (('Two lines that are not parallel always intersect.', 'Hai đường thẳng không song song thì luôn cắt nhau.'), False)]
def p11_concept(r, lv, ctx):
    want = r.choice([True, False]); good = r.choice([c for c in CON11 if c[1] == want]); bad = r.sample([c for c in CON11 if c[1] != want], 3)
    q = r.choice([('Which statement is correct?', 'Mệnh đề nào sau đây đúng?'), ('Which statement about two lines in space is true?', 'Mệnh đề nào sau đây về hai đường thẳng trong không gian là đúng?')]) if want else \
        r.choice([('Which statement is false?', 'Mệnh đề nào sau đây sai?'), ('Which statement about two lines in space is NOT true?', 'Mệnh đề nào sau đây về hai đường thẳng trong không gian là sai?')])
    return dict(en=q[0], vi=q[1], opts=[tx(*good[0])] + [tx(*b[0]) for b in bad], ee='Parallel lines must be coplanar; skew lines are not coplanar.', ev='Hai đường thẳng song song phải đồng phẳng; hai đường thẳng chéo nhau thì không đồng phẳng.')

def p11_quad(r, lv, ctx):
    k = r.choice(['any', 'eq', 'perp']); P = dict(TET)
    if k == 'eq':   # AC = BD
        P = {'A': (0, 0, 4), 'B': (-2, -2, 0), 'C': (3, -1, 0), 'D': (1, 2, 1)}
        AC2 = dot(vsub(P['C'], P['A']), vsub(P['C'], P['A'])); BD2 = dot(vsub(P['D'], P['B']), vsub(P['D'], P['B'])); assert AC2 == BD2 and dot(vsub(P['C'], P['A']), vsub(P['D'], P['B'])) != 0
        cond = ('\\(AC=BD\\)', '\\(AC=BD\\)'); good = ('a rhombus', 'hình thoi')
    elif k == 'perp':
        P = {'A': (0, 0, 4), 'B': (-3, 0, 0), 'C': (1, 2, 0), 'D': (2, -2, F(1, 4))}
        assert dot(vsub(P['C'], P['A']), vsub(P['D'], P['B'])) == 0
        cond = ('\\(AC\\perp BD\\)', '\\(AC\\perp BD\\)'); good = ('a rectangle', 'hình chữ nhật')
    else:
        cond = None; good = ('a parallelogram', 'hình bình hành')
    for a, b, n_ in (('A', 'B', 'M'), ('B', 'C', 'N'), ('C', 'D', 'P'), ('D', 'A', 'Q')): P[n_] = lerp(P[a], P[b], F(1, 2))
    MN, NP = vsub(P['N'], P['M']), vsub(P['P'], P['N']); assert parallel(MN, vsub(P['Q'], P['P'])) and parallel(NP, vsub(P['M'], P['Q']))
    if k == 'eq': assert dot(MN, MN) == dot(NP, NP)
    if k == 'perp': assert dot(MN, NP) == 0
    shapes = [('a parallelogram', 'hình bình hành'), ('a rhombus', 'hình thoi'), ('a rectangle', 'hình chữ nhật'), ('a trapezoid that is not a parallelogram', 'hình thang không phải hình bình hành')]
    if k == 'any': shapes[3] = ('a square', 'hình vuông')
    o = [tx(*good)] + [tx(*x) for x in shapes if x != good][:3]
    c_ = (' with %s' % cond[0], ' có %s' % cond[1]) if cond else ('', '')
    base = {k_: v for k_, v in P.items() if k_ in 'ABCD'}
    return dict(en='In the tetrahedron \\(ABCD\\)%s, \\(M, N, P, Q\\) are the midpoints of \\(AB, BC, CD, DA\\). The quadrilateral \\(MNPQ\\) is…' % c_[0],
                vi='Cho tứ diện \\(ABCD\\)%s; \\(M, N, P, Q\\) lần lượt là trung điểm của \\(AB, BC, CD, DA\\). Tứ giác \\(MNPQ\\) là…' % c_[1],
                opts=o, ee='\\(MN\\parallel PQ\\parallel AC\\), \\(MN=PQ=\\dfrac12AC\\); \\(NP\\parallel MQ\\parallel BD\\), \\(NP=MQ=\\dfrac12BD\\).', ev='\\(MN\\parallel PQ\\parallel AC\\), \\(MN=PQ=\\dfrac12AC\\); \\(NP\\parallel MQ\\parallel BD\\), \\(NP=MQ=\\dfrac12BD\\).',
                fig=fig3(G(base, 'ABCD', {c: P[c] for c in 'MNPQ'}, [('M', 'N', {'color': HL, 'width': 2.4}), ('N', 'P', {'color': HL, 'width': 2.4}), ('P', 'Q', {'color': HL, 'width': 2.4}), ('Q', 'M', {'color': HL, 'width': 2.4})]), 'Tetrahedron with MNPQ'))

def p11_trap(r, lv, ctx):
    P = dict(PYR); cyc = 'ABCD'
    X0, X1 = r.choice([('A', 'B'), ('B', 'C'), ('C', 'D'), ('A', 'D')])
    nb = lambda X, other: [y for y in (cyc[(cyc.index(X) + 1) % 4], cyc[(cyc.index(X) - 1) % 4]) if y != other][0]
    Y0, Y1 = nb(X0, X1), nb(X1, X0)                       # tứ giác M N Y1 Y0 (không tự cắt)
    P['M'] = lerp(P['S'], P[X0], F(1, 2)); P['N'] = lerp(P['S'], P[X1], F(1, 2))
    MN = vsub(P['N'], P['M']); base = vsub(P[Y1], P[Y0])
    assert parallel(MN, base) and 4 * dot(MN, MN) == dot(base, base) and dot(MN, base) > 0
    q = 'MN%s%s' % (Y1, Y0); e0, e1 = 'S' + X0, 'S' + X1; bl = L2(Y0, Y1)
    o = [tx('a trapezoid with \\(%s=2MN\\)' % bl, 'hình thang có \\(%s=2MN\\)' % bl), tx('a parallelogram', 'hình bình hành'), tx('a trapezoid with \\(MN=2%s\\)' % bl, 'hình thang có \\(MN=2%s\\)' % bl), tx('not a plane figure', 'không phải là hình phẳng')]
    return dict(en='The pyramid \\(S.ABCD\\) has a parallelogram base; \\(M, N\\) are the midpoints of \\(%s, %s\\). The quadrilateral \\(%s\\) is…' % (e0, e1, q),
                vi='Cho hình chóp \\(S.ABCD\\) có đáy là hình bình hành; \\(M, N\\) lần lượt là trung điểm của \\(%s, %s\\). Tứ giác \\(%s\\) là…' % (e0, e1, q),
                opts=o, ee='\\(MN\\parallel %s%s\\parallel %s\\) and \\(MN=\\dfrac12%s%s=\\dfrac12%s\\).' % (X0, X1, bl, X0, X1, bl), ev='\\(MN\\parallel %s%s\\parallel %s\\) và \\(MN=\\dfrac12%s%s=\\dfrac12%s\\).' % (X0, X1, bl, X0, X1, bl),
                fig=fig3(G(PYR, 'SABCD', {'M': P['M'], 'N': P['N']}, [('M', 'N', {'color': HL, 'width': 2.4}), ('N', Y1), ('M', Y0)]), 'Pyramid'))

def p11_through(r, lv, ctx):
    P = dict(CUBE); X = r.choice(['A′', 'B′', 'C′', 'D′', 'A', 'C']); Y, Z = r.choice([('B', 'C'), ('A', 'B'), ('C', 'D'), ('A', 'D'), ('B', 'B′'), ('C', 'C′')])
    d_ = vsub(P[Z], P[Y]); cand = [n for n in P if n != X and parallel(vsub(P[n], P[X]), d_)]
    if len(cand) != 1 or X in (Y, Z): raise AssertionError
    good = cand[0]; others = [n for n in P if n not in (X, good)]; wr = r.sample(others, 3)
    o = lambda n: '\\(%s%s\\)' % (X, n)
    return dict(en='In the cube \\(ABCD.A′B′C′D′\\), the line through \\(%s\\) parallel to \\(%s%s\\) is…' % (X, Y, Z), vi='Trong hình lập phương \\(ABCD.A′B′C′D′\\), đường thẳng qua \\(%s\\) và song song với \\(%s%s\\) là…' % (X, Y, Z),
                opts=[o(good)] + [o(n) for n in wr], ee='\\(%s%s\\parallel %s%s\\) (the cube has parallel equal edges / faces are squares).' % (X, good, Y, Z), ev='\\(%s%s\\parallel %s%s\\).' % (X, good, Y, Z),
                fig=fig3(G(CUBE, list(CUBE), None, [(Y, Z, {'color': BL, 'width': 3.0})]), 'Cube'))

# A–C Bài 11 (có hình)
def p11_count(r, lv, ctx):
    from sp_g11c import count, NM, KN
    nm = r.choice(['cube', 'box', 'tetra', 'prism']); kd = r.choice(['par', 'skew', 'int']); c = count(nm, kd)
    if c == 0: raise AssertionError
    fg = {'cube': (CUBE, list(CUBE)), 'box': (CUBE, list(CUBE)), 'tetra': (TET, 'ABCD'), 'prism': (PRISM, list(PRISM))}[nm]
    return dict(en='How many pairs of edges of %s are %s?' % (NM[nm][0], KN[kd][0]), vi='Có bao nhiêu cặp cạnh của %s %s?' % (NM[nm][1], KN[kd][1]),
                opts=[str(c)] + [str(x) for x in dict.fromkeys([c + 1, c - 1, 2 * c, c + 6, c + 3]) if x != c and x >= 0][:3], ee='Check each pair of edges: %d.' % c, ev='Xét từng cặp cạnh: %d.' % c,
                fig=fig3(G(fg[0], fg[1]), 'Solid'))
def p11_midlen(r, lv, ctx):
    x = r.choice([6, 8, 10, 12, 14, 16, 18, 20]); P = dict(PYR); P['M'] = lerp(P['S'], P['A'], F(1, 2)); P['N'] = lerp(P['S'], P['B'], F(1, 2))
    return dict(en='In the pyramid \\(S.ABCD\\), \\(M, N\\) are the midpoints of \\(SA, SB\\). If \\(AB=%d\\), then \\(MN=\\)…' % x, vi='Trong hình chóp \\(S.ABCD\\), \\(M, N\\) là trung điểm của \\(SA, SB\\). Nếu \\(AB=%d\\) thì \\(MN=\\)…' % x,
                opts=[str(x // 2), str(x), str(2 * x), str(x // 2 + 2)], ee='Midline: \\(MN=\\dfrac12AB=%d\\).' % (x // 2), ev='Đường trung bình: \\(MN=\\dfrac12AB=%d\\).' % (x // 2),
                fig=fig3(G(PYR, 'SABCD', {'M': P['M'], 'N': P['N']}, [('M', 'N', {'color': HL, 'width': 2.6})]), 'Pyramid'))
def p11_perim(r, lv, ctx):
    a, b = r.choice([(6, 8), (10, 12), (8, 14), (12, 16), (6, 10), (14, 18), (4, 10), (16, 20)]); P = dict(TET)
    for u, v, n_ in (('A', 'B', 'M'), ('B', 'C', 'N'), ('C', 'D', 'P'), ('D', 'A', 'Q')): P[n_] = lerp(P[u], P[v], F(1, 2))
    return dict(en='In the tetrahedron \\(ABCD\\), \\(M, N, P, Q\\) are the midpoints of \\(AB, BC, CD, DA\\). If \\(AC=%d\\) and \\(BD=%d\\), the perimeter of \\(MNPQ\\) is…' % (a, b),
                vi='Cho tứ diện \\(ABCD\\), \\(M, N, P, Q\\) là trung điểm của \\(AB, BC, CD, DA\\). Biết \\(AC=%d\\), \\(BD=%d\\). Chu vi tứ giác \\(MNPQ\\) bằng…' % (a, b),
                opts=[str(a + b), str((a + b) // 2), str(2 * (a + b)), str(a * b // 2)], ee='\\(MN=PQ=\\dfrac{AC}2\\), \\(NP=MQ=\\dfrac{BD}2\\): perimeter \\(=AC+BD=%d\\).' % (a + b), ev='\\(MN=PQ=\\dfrac{AC}2\\), \\(NP=MQ=\\dfrac{BD}2\\): chu vi \\(=AC+BD=%d\\).' % (a + b),
                fig=fig3(G(TET, 'ABCD', {c: P[c] for c in 'MNPQ'}, [('M', 'N'), ('N', 'P'), ('P', 'Q'), ('Q', 'M')]), 'Tetrahedron'))
TF11 = [('Two skew lines have no common point.', 'Hai đường thẳng chéo nhau thì không có điểm chung.', True, 'Skew lines are not coplanar and do not meet.', 'Hai đường thẳng chéo nhau không đồng phẳng và không cắt nhau.'),
        ('In a cube \\(ABCD.A′B′C′D′\\), \\(AB\\) and \\(C′D′\\) are parallel.', 'Trong hình lập phương \\(ABCD.A′B′C′D′\\), \\(AB\\) và \\(C′D′\\) song song.', True, '\\(AB\\parallel CD\\parallel C′D′\\).', '\\(AB\\parallel CD\\parallel C′D′\\).'),
        ('Through a point not on a line there are infinitely many lines parallel to it.', 'Qua một điểm nằm ngoài một đường thẳng có vô số đường thẳng song song với đường thẳng đó.', False, 'There is exactly one.', 'Có đúng một đường thẳng.'),
        ('In a cube \\(ABCD.A′B′C′D′\\), \\(AB\\) and \\(DD′\\) intersect.', 'Trong hình lập phương \\(ABCD.A′B′C′D′\\), \\(AB\\) và \\(DD′\\) cắt nhau.', False, 'They are skew.', 'Chúng chéo nhau.'),
        ('If \\(a\\parallel c\\) and \\(b\\parallel c\\) (three different lines), then \\(a\\parallel b\\).', 'Nếu \\(a\\parallel c\\) và \\(b\\parallel c\\) (ba đường thẳng phân biệt) thì \\(a\\parallel b\\).', True, 'Two lines parallel to a third line are parallel.', 'Hai đường thẳng phân biệt cùng song song với đường thẳng thứ ba thì song song.'),
        ('Two lines with no common point are parallel.', 'Hai đường thẳng không có điểm chung thì song song.', False, 'They may be skew.', 'Chúng có thể chéo nhau.')]
def p11_tf1(r, lv, ctx): e = TF11[(lv - 1) * 2]; return dict(en=e[0], vi=e[1], truth=e[2], ee=e[3], ev=e[4])
def p11_tf2(r, lv, ctx): e = TF11[(lv - 1) * 2 + 1]; return dict(en=e[0], vi=e[1], truth=e[2], ee=e[3], ev=e[4])
def p11_sh_centroid(r, lv, ctx):
    cd = r.choice([6, 9, 12, 15, 18, 21, 24, 27]); P = dict(TET)
    P['G'] = tuple(sum(c) / 3 for c in zip(P['A'], P['B'], P['C'])); P['H'] = tuple(sum(c) / 3 for c in zip(P['A'], P['B'], P['D']))
    GH = vsub(P['H'], P['G']); CD = vsub(P['D'], P['C']); assert parallel(GH, CD) and 9 * dot(GH, GH) == dot(CD, CD)
    return dict(en='In the tetrahedron \\(ABCD\\), \\(G\\) and \\(H\\) are the centroids of triangles \\(ABC\\) and \\(ABD\\). Given \\(CD=%d\\), find \\(GH\\).' % cd, vi='Cho tứ diện \\(ABCD\\), \\(G\\) và \\(H\\) lần lượt là trọng tâm các tam giác \\(ABC\\) và \\(ABD\\). Biết \\(CD=%d\\), tính \\(GH\\).' % cd, key=key(F(cd, 3)),
                ee='With \\(I\\) the midpoint of \\(AB\\): \\(\\dfrac{IG}{IC}=\\dfrac{IH}{ID}=\\dfrac13\\), so \\(GH\\parallel CD\\), \\(GH=\\dfrac{CD}3=%d\\).' % (cd // 3), ev='Gọi \\(I\\) là trung điểm \\(AB\\): \\(\\dfrac{IG}{IC}=\\dfrac{IH}{ID}=\\dfrac13\\) nên \\(GH\\parallel CD\\), \\(GH=\\dfrac{CD}3=%d\\).' % (cd // 3),
                fig=fig3(G(TET, 'ABCD', {'G': P['G'], 'H': P['H']}, [('G', 'H', {'color': HL, 'width': 2.6})]), 'Tetrahedron with G, H'))
def p11_sh_area(r, lv, ctx):
    p, q = r.choice([(6, 8), (10, 12), (12, 16), (8, 10), (6, 14), (10, 16), (8, 12), (14, 16)])
    P = {'A': (0, 0, 4), 'B': (-3, 0, 0), 'C': (1, 2, 0), 'D': (2, -2, F(1, 4))}
    assert dot(vsub(P['C'], P['A']), vsub(P['D'], P['B'])) == 0
    for u, v, n_ in (('A', 'B', 'M'), ('B', 'C', 'N'), ('C', 'D', 'P'), ('D', 'A', 'Q')): P[n_] = lerp(P[u], P[v], F(1, 2))
    return dict(en='In the tetrahedron \\(ABCD\\), \\(AC\\perp BD\\), \\(AC=%d\\), \\(BD=%d\\); \\(M, N, P, Q\\) are the midpoints of \\(AB, BC, CD, DA\\). Find the area of \\(MNPQ\\).' % (p, q),
                vi='Cho tứ diện \\(ABCD\\) có \\(AC\\perp BD\\), \\(AC=%d\\), \\(BD=%d\\); \\(M, N, P, Q\\) là trung điểm của \\(AB, BC, CD, DA\\). Tính diện tích tứ giác \\(MNPQ\\).' % (p, q), key=key(F(p * q, 4)),
                ee='\\(MNPQ\\) is a rectangle with sides \\(\\dfrac{AC}2\\), \\(\\dfrac{BD}2\\): area \\(%s\\).' % ne(F(p * q, 4)), ev='\\(MNPQ\\) là hình chữ nhật có hai cạnh \\(\\dfrac{AC}2\\), \\(\\dfrac{BD}2\\): diện tích \\(%s\\).' % nv(F(p * q, 4)),
                fig=fig3(G({k_: P[k_] for k_ in 'ABCD'}, 'ABCD', {c: P[c] for c in 'MNPQ'}, [('M', 'N'), ('N', 'P'), ('P', 'Q'), ('Q', 'M')]), 'Tetrahedron'))

L11 = dict(A=[p11_count, p11_midlen, p11_perim], B=[p11_tf1, p11_tf2], C=[p11_sh_centroid, p11_sh_area],
           D=[p11_rel, p11_parallel_to, p11_gt_par, p11_thales, p11_concept, p11_quad, p11_trap, p11_through])


# ---------------- phần D bổ sung cho bài đã có A–C (Bài 21, 32) ----------------
def with_d(practice, D, seeds=(2101, 2102, 2103)):
    import re as _re, html as _h
    old = ''.join(''.join(g[1]) for g in practice)
    used = set()
    out = []
    for lv, seed in zip((1, 2, 3), seeds):
        r = random.Random(seed); n = 1 + sum(len(g[1]) for g in practice if g[2] == [lv]); items = []
        for b in D:
            for _ in range(500):
                try: q = b(r, lv, {})
                except AssertionError: continue
                if q['en'] in used or _h.escape(q['en'], quote=False) in old or len(set(q['opts'])) != 4: continue
                break
            else: raise RuntimeError('không sinh được câu: ' + b.__name__)
            used.add(q['en']); en, vi = _fig(q)
            opts = list(q['opts']); good = opts[0]; idx = list(range(4)); r.shuffle(idx); shf = [opts[i] for i in idx]; L = 'abcd'[shf.index(good)]
            items.append(MCQ(n, (en, vi), shf, L, ('Answer: %s. %s' % (L, q['ee']), 'Đáp án %s. %s' % (L, q['ev'])))); n += 1
        out.append((TD, items, [lv]))
    return practice + out

def frl(x):
    x = F(x); return ne(x)

# ---- Bài 21: phương trình, bất phương trình mũ và lôgarit ----
def e_count(r, lv, ctx):
    for _ in range(200):
        r1, r2 = sorted(r.sample(range(-6, 9), 2)); p = r.randint(-5, 5); q = r.randint(-5, 5)
        if p == q: continue
        k = (r1 + p) * (r1 + q)
        if k <= 0 or (r2 + p) * (r2 + q) != k or -(p + q) != r1 + r2: continue
        valid = [x for x in (r1, r2) if x + p > 0 and x + q > 0]
        a = r.choice([2, 3, 5]); break
    else: raise AssertionError
    c = len(valid)
    f = lambda t: 'x%+d' % t if t else 'x'
    return dict(en='How many solutions does the equation \\(\\log_{%d}(%s)+\\log_{%d}(%s)=\\log_{%d}%d\\) have?' % (a, f(p), a, f(q), a, k), vi='Phương trình \\(\\log_{%d}(%s)+\\log_{%d}(%s)=\\log_{%d}%d\\) có bao nhiêu nghiệm?' % (a, f(p), a, f(q), a, k),
                opts=[str(c)] + [str(x) for x in (0, 1, 2, 3) if x != c][:3],
                ee='Condition \\(x\\gt%d\\). Then \\((%s)(%s)=%d\\) gives \\(x=%d\\) or \\(x=%d\\); %d of them satisfy the condition.' % (max(-p, -q), f(p), f(q), k, r1, r2, c),
                ev='Điều kiện \\(x\\gt%d\\). Khi đó \\((%s)(%s)=%d\\) cho \\(x=%d\\) hoặc \\(x=%d\\); có %d nghiệm thỏa mãn điều kiện.' % (max(-p, -q), f(p), f(q), k, r1, r2, c))

def e_product(r, lv, ctx):
    a = r.choice([2, 3, 5, 7]); b = r.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]); c = r.choice([1, 2, 3, 4, 5, 6, 8, 10, 12])
    if b * b + 4 * c <= 0: raise AssertionError
    s_ = 'x^2%+dx' % b if b not in (1, -1) else ('x^2+x' if b == 1 else 'x^2-x')
    return dict(en='The product of the solutions of \\(%d^{%s}=%d^{%d}\\) is…' % (a, s_, a, c), vi='Tích các nghiệm của phương trình \\(%d^{%s}=%d^{%d}\\) bằng…' % (a, s_, a, c),
                opts=[str(-c), str(c), str(-b), str(b) if b != c and b != -c else str(c + 1)],
                ee='\\(%s-%d=0\\) has two solutions; by Viète their product is \\(%d\\).' % (s_, c, -c), ev='\\(%s-%d=0\\) có hai nghiệm; theo định lí Viète, tích hai nghiệm là \\(%d\\).' % (s_, c, -c))

def e_intcount(r, lv, ctx):
    m, n = sorted(r.sample(range(-4, 7), 2)); a = r.choice([2, 3, 5, 10]); s_ = m + n; pr_ = m * n
    ex = 'x^2' + ('' if s_ == 0 else ('-%dx' % s_ if s_ > 1 else ('-x' if s_ == 1 else ('+x' if s_ == -1 else '+%dx' % -s_))))
    cnt = n - m + 1
    return dict(en='How many integers \\(x\\) satisfy \\(%d^{%s}\\le %d^{%d}\\)?' % (a, ex, a, -pr_), vi='Có bao nhiêu số nguyên \\(x\\) thỏa mãn \\(%d^{%s}\\le %d^{%d}\\)?' % (a, ex, a, -pr_),
                opts=[str(cnt), str(cnt - 1), str(cnt + 1), str(cnt - 2) if cnt > 2 else str(cnt + 2)],
                ee='Base \\(%d\\gt1\\): \\(%s\\le%d\\iff %d\\le x\\le %d\\): %d integers.' % (a, ex, -pr_, m, n, cnt), ev='Cơ số \\(%d\\gt1\\): \\(%s\\le%d\\iff %d\\le x\\le %d\\): có %d số nguyên.' % (a, ex, -pr_, m, n, cnt))

def e_domain(r, lv, ctx):
    a = r.randint(-5, 3); b = a + r.randint(2, 7); base = r.choice([2, 3, 5]); c = r.randint(0, 3)
    I = lambda lo, hi, L='(', R=')': '\\(x\\in%s%d;\\,%d%s\\)' % (L, lo, hi, R)
    fa = 'x%+d' % -a if a else 'x'
    return dict(en='What is the condition of the equation \\(\\log_{%d}(%s)+\\log_{%d}(%d-x)=%d\\)?' % (base, fa, base, b, c), vi='Điều kiện xác định của phương trình \\(\\log_{%d}(%s)+\\log_{%d}(%d-x)=%d\\) là…' % (base, fa, base, b, c),
                opts=[I(a, b), I(a, b, '[', ']'), '\\(x\\gt%d\\)' % a, '\\(x\\lt%d\\)' % b], ee='Need \\(%s\\gt0\\) and \\(%d-x\\gt0\\): \\(%d\\lt x\\lt%d\\).' % (fa, b, a, b), ev='Cần \\(%s\\gt0\\) và \\(%d-x\\gt0\\): \\(%d\\lt x\\lt%d\\).' % (fa, b, a, b))

def e_minint(r, lv, ctx):
    a = r.randint(-3, 5); k = r.choice([1, 2, 3, 4]); thr = a + 2 ** k
    fa = 'x%+d' % -a if a else 'x'
    return dict(en='The smallest integer \\(x\\) satisfying \\(\\log_{\\frac12}(%s)\\lt-%d\\) is…' % (fa, k), vi='Số nguyên \\(x\\) nhỏ nhất thỏa mãn \\(\\log_{\\frac12}(%s)\\lt-%d\\) là…' % (fa, k),
                opts=[str(thr + 1), str(thr), str(a + 1), str(a - 2 ** k + 1)],
                ee='Base \\(\\frac12\\lt1\\): reverse the sign, \\(%s\\gt\\left(\\frac12\\right)^{-%d}=%d\\), so \\(x\\gt%d\\).' % (fa, k, 2 ** k, thr), ev='Cơ số \\(\\frac12\\lt1\\): đổi chiều, \\(%s\\gt\\left(\\frac12\\right)^{-%d}=%d\\) nên \\(x\\gt%d\\).' % (fa, k, 2 ** k, thr))

def e_decay(r, lv, ctx):
    T = r.choice([5, 8, 10, 12, 20, 30]); p = r.choice([30, 20, 15, 10, 5]); sub = r.choice([('a radioactive substance', 'một chất phóng xạ'), ('a medicine in the blood', 'một loại thuốc trong máu')])
    t = T * math.log2(100 / p); n = math.ceil(t - 1e-12)
    unit = ('years', 'năm') if sub[0].startswith('a radio') else ('hours', 'giờ')
    return dict(en='The amount of %s halves every %d %s: \\(m(t)=m_0\\left(\\frac12\\right)^{t/%d}\\). After at least how many whole %s is at most %d%% of it left?' % (sub[0], T, unit[0], T, unit[0], p),
                vi='Lượng %s giảm một nửa sau mỗi %d %s: \\(m(t)=m_0\\left(\\frac12\\right)^{t/%d}\\). Sau ít nhất bao nhiêu %s (số nguyên) thì lượng còn lại không quá %d%%?' % (sub[1], T, unit[1], T, unit[1], p),
                opts=[str(n), str(n - 1), str(n + T), str(int(T * 100 / p / 2))], ee='\\(\\left(\\frac12\\right)^{t/%d}\\le%s\\iff t\\ge%d\\log_2%s\\approx%s\\).' % (T, ne(F(p, 100)), T, ne(F(100, p)), '%.2f' % t),
                ev='\\(\\left(\\frac12\\right)^{t/%d}\\le%s\\iff t\\ge%d\\log_2%s\\approx%s\\).' % (T, nv(F(p, 100)), T, nv(F(100, p)), ('%.2f' % t).replace('.', '{,}')))

def e_growth(r, lv, ctx):
    rate = r.choice([F(8, 1000), F(1, 100), F(12, 1000), F(15, 1000), F(2, 100), F(25, 1000)]); y0 = r.choice([2020, 2024, 2025]); k = r.choice([F(3, 2), F(2), F(5, 4)])
    t = math.log(float(k)) / float(rate); n = math.ceil(t - 1e-12)
    return dict(en='A town has a population \\(P(t)=P_0e^{%st}\\), where \\(t\\) is the number of years after %d. In which year does the population first exceed \\(%s\\) times \\(P_0\\)?' % (ne(rate), y0, ne(k)),
                vi='Dân số một thị trấn là \\(P(t)=P_0e^{%st}\\), với \\(t\\) là số năm kể từ năm %d. Năm nào dân số lần đầu vượt quá \\(%s\\) lần \\(P_0\\)?' % (nv(rate), y0, nv(k)),
                opts=[str(y0 + n), str(y0 + n - 1), str(y0 + n + 1), str(y0 + int(float(k) / float(rate)))], ee='\\(e^{%st}\\gt%s\\iff t\\gt\\dfrac{\\ln %s}{%s}\\approx%s\\): year \\(%d+%d\\).' % (ne(rate), ne(k), ne(k), ne(rate), '%.2f' % t, y0, n),
                ev='\\(e^{%st}\\gt%s\\iff t\\gt\\dfrac{\\ln %s}{%s}\\approx%s\\): năm \\(%d+%d\\).' % (nv(rate), nv(k), nv(k), nv(rate), ('%.2f' % t).replace('.', '{,}'), y0, n))

def e_error(r, lv, ctx):
    k = r.choice(['flip', 'square', 'domain'])
    if k == 'flip':
        b = r.choice([2, 3]); c = r.randint(1, 3); R = b ** c
        st = ('Solve \\(\\left(\\frac1{%d}\\right)^x\\gt%d\\). Step 1: \\(%d=\\left(\\frac1{%d}\\right)^{-%d}\\). Step 2: so \\(x\\gt-%d\\). Step 3: the solution set is \\((-%d;+\\infty)\\).' % (b, R, R, b, c, c, c),
              'Giải bất phương trình \\(\\left(\\frac1{%d}\\right)^x\\gt%d\\). Bước 1: \\(%d=\\left(\\frac1{%d}\\right)^{-%d}\\). Bước 2: suy ra \\(x\\gt-%d\\). Bước 3: tập nghiệm là \\((-%d;+\\infty)\\).' % (b, R, R, b, c, c, c))
        good = 2; why = ('The base is less than 1, so the sign must be reversed: \\(x\\lt-%d\\).' % c, 'Cơ số nhỏ hơn 1 nên phải đổi chiều: \\(x\\lt-%d\\).' % c)
    elif k == 'square':
        a = r.choice([2, 3]); c = r.choice([2, 4]); R = a ** (c // 2)
        st = ('Solve \\(\\log_{%d}x^2=%d\\). Step 1: condition \\(x\\ne0\\). Step 2: \\(\\log_{%d}x^2=2\\log_{%d}x\\), so \\(\\log_{%d}x=%d\\). Step 3: \\(x=%d\\).' % (a, c, a, a, a, c // 2, R),
              'Giải phương trình \\(\\log_{%d}x^2=%d\\). Bước 1: điều kiện \\(x\\ne0\\). Bước 2: \\(\\log_{%d}x^2=2\\log_{%d}x\\) nên \\(\\log_{%d}x=%d\\). Bước 3: \\(x=%d\\).' % (a, c, a, a, a, c // 2, R))
        good = 2; why = ('\\(\\log_{%d}x^2=2\\log_{%d}|x|\\); the solutions are \\(x=\\pm%d\\).' % (a, a, R), '\\(\\log_{%d}x^2=2\\log_{%d}|x|\\); nghiệm là \\(x=\\pm%d\\).' % (a, a, R))
    else:
        m = r.choice([1, 2, 3])
        # log2(x - m) + log2(x + m) = log2(...)  with roots ±R where -R rejected
        R = r.choice([3, 4, 5]); K = R * R - m * m
        if K <= 0: raise AssertionError
        st = ('Solve \\(\\log_2(x-%d)+\\log_2(x+%d)=\\log_2%d\\). Step 1: \\(\\log_2(x^2-%d)=\\log_2%d\\). Step 2: \\(x^2=%d\\). Step 3: \\(x=\\pm%d\\).' % (m, m, K, m * m, K, R * R, R),
              'Giải phương trình \\(\\log_2(x-%d)+\\log_2(x+%d)=\\log_2%d\\). Bước 1: \\(\\log_2(x^2-%d)=\\log_2%d\\). Bước 2: \\(x^2=%d\\). Bước 3: \\(x=\\pm%d\\).' % (m, m, K, m * m, K, R * R, R))
        good = 3; why = ('The condition \\(x\\gt%d\\) was not checked: only \\(x=%d\\).' % (m, R), 'Chưa đối chiếu điều kiện \\(x\\gt%d\\): chỉ nhận \\(x=%d\\).' % (m, R))
    steps = [tx('Step %d' % i, 'Bước %d' % i) for i in (1, 2, 3)] + [tx('There is no mistake.', 'Không có bước nào sai.')]
    return dict(en='%s In which step is the first mistake?' % st[0], vi='%s Lời giải sai từ bước nào?' % st[1], opts=[steps[good - 1]] + [s_ for i, s_ in enumerate(steps) if i != good - 1], ee=why[0], ev=why[1])

D21 = [e_count, e_product, e_intcount, e_domain, e_minint, e_decay, e_growth, e_error]

# ---- Bài 32: các quy tắc tính đạo hàm ----
def _p(c, v='x'):
    from mb_selfpractice import poly as _poly
    return _poly(c, v)
def d_param(r, lv, ctx):
    """Ngược: biết f'(x0) = k, tìm tham số m trong f(x) = x^3 + m x^2 + b x + c."""
    x0 = r.choice([-2, -1, 1, 2, 3]); m = r.choice([-3, -2, -1, 1, 2, 3, 4]); b = r.choice([-5, -4, -2, -1, 1, 3, 6]); c = r.randint(-4, 4)
    k = 3 * x0 * x0 + 2 * m * x0 + b
    fx = 'x^3+mx^2' + ('%+dx' % b if abs(b) != 1 else ('+x' if b == 1 else '-x')) + ('%+d' % c if c else '')
    return dict(en='Given \\(f(x)=%s\\) and \\(f^{\\prime}(%d)=%d\\), the value of \\(m\\) is…' % (fx, x0, k), vi='Cho \\(f(x)=%s\\) và \\(f^{\\prime}(%d)=%d\\). Giá trị của \\(m\\) là…' % (fx, x0, k),
                opts=[str(m), str(-m), str(m + 1), str(m - 2) if m - 2 != -m else str(m + 3)],
                ee='\\(f^{\\prime}(x)=3x^2+2mx%+d\\), so \\(%d%+d\\,m%+d=%d\\Rightarrow m=%d\\).' % (b, 3 * x0 * x0, 2 * x0, b, k, m), ev='\\(f^{\\prime}(x)=3x^2+2mx%+d\\) nên \\(%d%+d\\,m%+d=%d\\Rightarrow m=%d\\).' % (b, 3 * x0 * x0, 2 * x0, b, k, m))
def d_zero(r, lv, ctx):
    p, q = sorted(r.sample(range(-4, 5), 2))
    # f' = 3(x-p)(x-q) = 3x^2 - 3(p+q)x + 3pq  => f = x^3 - 3(p+q)/2 x^2 + 3pq x + c  (cần (p+q) chẵn)
    if (p + q) % 2: raise AssertionError
    c = r.randint(-5, 5); f = _p([1, -3 * (p + q) // 2, 3 * p * q, c])
    S_ = lambda a_, b_: '\\(x=%d,\\ x=%d\\)' % (a_, b_)
    return dict(en='Solve \\(f^{\\prime}(x)=0\\) for \\(f(x)=%s\\).' % f, vi='Giải phương trình \\(f^{\\prime}(x)=0\\) với \\(f(x)=%s\\).' % f,
                opts=[S_(p, q), S_(-p, -q) if (-q, -p) != (p, q) else S_(p, q + 1), S_(p, q + 2), S_(3 * p, 3 * q) if p * q != 0 or (3 * p, 3 * q) != (p, q) else S_(p - 1, q)],
                ee='\\(f^{\\prime}(x)=3x^2%+dx%+d=3(x%+d)(x%+d)\\).' % (-3 * (p + q), 3 * p * q, -p, -q), ev='\\(f^{\\prime}(x)=3x^2%+dx%+d=3(x%+d)(x%+d)\\).' % (-3 * (p + q), 3 * p * q, -p, -q))
def d_velocity(r, lv, ctx):
    a, b, c = r.choice([1, 2]), r.randint(-6, 6), r.randint(1, 9); t0 = r.randint(1, 5)
    s_ = _p([a, b, c, 0], 't'); v = 3 * a * t0 * t0 + 2 * b * t0 + c
    if v <= 0: raise AssertionError
    return dict(en='An object moves with \\(s(t)=%s\\) (metres, \\(t\\) in seconds). Its velocity at \\(t=%d\\) s is…'.replace('metres', 'meters') % (s_, t0), vi='Một vật chuyển động theo phương trình \\(s(t)=%s\\) (mét, \\(t\\) tính bằng giây). Vận tốc của vật tại \\(t=%d\\) giây là…' % (s_, t0),
                opts=[tx('\\(%d\\) m/s' % v, '\\(%d\\) m/s' % v), tx('\\(%d\\) m/s' % (a * t0 ** 3 + b * t0 ** 2 + c * t0), '\\(%d\\) m/s' % (a * t0 ** 3 + b * t0 ** 2 + c * t0)), tx('\\(%d\\) m/s' % (6 * a * t0 + 2 * b), '\\(%d\\) m/s' % (6 * a * t0 + 2 * b)), tx('\\(%d\\) m/s' % (v + c), '\\(%d\\) m/s' % (v + c))],
                ee='\\(v(t)=s^{\\prime}(t)=%s\\), \\(v(%d)=%d\\).' % (_p([3 * a, 2 * b, c], 't'), t0, v), ev='\\(v(t)=s^{\\prime}(t)=%s\\), \\(v(%d)=%d\\).' % (_p([3 * a, 2 * b, c], 't'), t0, v))
def d_balloon(r, lv, ctx):
    k = r.choice([2, 3, 4, 5, 6, 10]); good = 4 * k * k
    P = lambda c: '%d\\pi' % c
    return dict(en='A balloon has volume \\(V(r)=\\dfrac43\\pi r^3\\). Find \\(V^{\\prime}(%d)\\), the rate of change of the volume with respect to the radius when \\(r=%d\\) cm.' % (k, k),
                vi='Một quả bóng có thể tích \\(V(r)=\\dfrac43\\pi r^3\\). Tính \\(V^{\\prime}(%d)\\), tốc độ thay đổi của thể tích theo bán kính khi \\(r=%d\\) cm.' % (k, k),
                opts=[P(good), P(4 * k ** 3) if 4 * k ** 3 != good else P(good + 1), '\\dfrac{%d}{3}\\pi' % (4 * k ** 3) if (4 * k ** 3) % 3 else P(4 * k ** 3 // 3), P(4 * k)],
                ee='\\(V^{\\prime}(r)=4\\pi r^2\\), so \\(V^{\\prime}(%d)=%d\\pi\\).' % (k, good), ev='\\(V^{\\prime}(r)=4\\pi r^2\\) nên \\(V^{\\prime}(%d)=%d\\pi\\).' % (k, good))
def d_parallel(r, lv, ctx):
    a = r.choice([1, 2, -1]); b = r.randint(-6, 6); c = r.randint(-5, 5); x0 = r.randint(-3, 4); k = 2 * a * x0 + b; m = r.randint(-4, 4)
    y0 = a * x0 * x0 + b * x0 + c
    if y0 == k * x0 + m: raise AssertionError
    pt = lambda x: '\\(M(%d;\\,%d)\\)' % (x, a * x * x + b * x + c)
    return dict(en='The tangent to \\(y=%s\\) is parallel to the line \\(y=%s\\) at the point…' % (_p([a, b, c]), _p([k, m])), vi='Tiếp tuyến của đồ thị \\(y=%s\\) song song với đường thẳng \\(y=%s\\) tại điểm…' % (_p([a, b, c]), _p([k, m])),
                opts=[pt(x0), pt(x0 + 1), pt(-x0) if x0 != 0 else pt(2), pt(x0 - 2)], ee='\\(y^{\\prime}=%s=%d\\iff x=%d\\).' % (_p([2 * a, b]), k, x0), ev='\\(y^{\\prime}=%s=%d\\iff x=%d\\).' % (_p([2 * a, b]), k, x0))
def d_error(r, lv, ctx):
    n = r.choice([2, 3, 4]); fn = r.choice([('\\sin x', '\\cos x'), ('\\cos x', '-\\sin x'), ('e^x', 'e^x')])
    xn = 'x^%d' % n; d1 = '%dx%s' % (n, '' if n == 2 else '^%d' % (n - 1))
    right = '%s%s+%s%s' % (d1, fn[0], xn, fn[1]) if not fn[1].startswith('-') else '%s%s-%s%s' % (d1, fn[0], xn, fn[1][1:])
    wrong = '%s\\cdot %s' % (d1, fn[1])
    return dict(en='Lan wrote \\((%s%s)^{\\prime}=%s\\). Which is correct?' % (xn, fn[0], wrong), vi='Bạn Lan viết \\((%s%s)^{\\prime}=%s\\). Nhận xét nào đúng?' % (xn, fn[0], wrong),
                opts=[tx('Lan is wrong; the correct result is \\(%s\\).' % right, 'Lan sai; kết quả đúng là \\(%s\\).' % right), tx('Lan is right.', 'Lan đúng.'),
                      tx('Lan is wrong; the correct result is \\(%s%s\\).' % (d1, fn[0]), 'Lan sai; kết quả đúng là \\(%s%s\\).' % (d1, fn[0])), tx('Lan is wrong; the correct result is \\(%s%s\\).' % (xn, fn[1]), 'Lan sai; kết quả đúng là \\(%s%s\\).' % (xn, fn[1]))],
                ee='Product rule: \\((uv)^{\\prime}=u^{\\prime}v+uv^{\\prime}\\), not \\(u^{\\prime}v^{\\prime}\\).', ev='Quy tắc tích: \\((uv)^{\\prime}=u^{\\prime}v+uv^{\\prime}\\), không phải \\(u^{\\prime}v^{\\prime}\\).')
def d_sqrt(r, lv, ctx):
    a = r.choice([1, 2, 3, 4, 5, 6, 8]); x0 = r.randint(0, 6); s = r.choice([2, 3, 4, 5, 6]); b = s * s - a * x0
    if b < -20 or b > 40: raise AssertionError
    v = F(a, 2 * s); fb = '%+d' % b if b else ''
    o = lambda x: ne(x)
    return dict(en='Given \\(y=\\sqrt{%dx%s}\\), the value of \\(y^{\\prime}(%d)\\) is…' % (a, fb, x0) if a != 1 else 'Given \\(y=\\sqrt{x%s}\\), the value of \\(y^{\\prime}(%d)\\) is…' % (fb, x0),
                vi='Cho \\(y=\\sqrt{%dx%s}\\). Giá trị \\(y^{\\prime}(%d)\\) bằng…' % (a, fb, x0) if a != 1 else 'Cho \\(y=\\sqrt{x%s}\\). Giá trị \\(y^{\\prime}(%d)\\) bằng…' % (fb, x0),
                opts=[o(v), o(F(1, 2 * s)), o(F(a, s)), o(F(a, 2 * s * s))], ee='\\(y^{\\prime}=\\dfrac{%d}{2\\sqrt{%dx%s}}\\), at \\(x=%d\\): \\(\\dfrac{%d}{2\\cdot%d}=%s\\).' % (a, a, fb, x0, a, s, o(v)),
                ev='\\(y^{\\prime}=\\dfrac{%d}{2\\sqrt{%dx%s}}\\), tại \\(x=%d\\): \\(\\dfrac{%d}{2\\cdot%d}=%s\\).' % (a, a, fb, x0, a, s, nv(v)))
def d_ln(r, lv, ctx):
    a = r.choice([1, 2, 3]); b = r.choice([1, 2, 3, 4, 5, 6]); x0 = r.choice([1, 2, -1, 3])
    v = F(2 * a * x0, a * x0 * x0 + b); inner = _p([a, 0, b])
    return dict(en='What is the slope of the tangent to the graph of \\(y=\\ln(%s)\\) at the point with \\(x=%d\\)?' % (inner, x0), vi='Hệ số góc của tiếp tuyến với đồ thị hàm số \\(y=\\ln(%s)\\) tại điểm có hoành độ \\(x=%d\\) là…' % (inner, x0),
                opts=nopts(r, v, [F(1, a * x0 * x0 + b), F(2 * a * x0), F(a * x0, a * x0 * x0 + b), -v]), ee='\\(y^{\\prime}=\\dfrac{%s}{%s}\\), so \\(y^{\\prime}(%d)=%s\\).' % (_p([2 * a, 0]), inner, x0, ne(v)),
                ev='\\(y^{\\prime}=\\dfrac{%s}{%s}\\) nên \\(y^{\\prime}(%d)=%s\\).' % (_p([2 * a, 0]), inner, x0, nv(v)))

D32 = [d_param, d_zero, d_velocity, d_balloon, d_parallel, d_error, d_sqrt, d_ln]
