# -*- coding: utf-8 -*-
"""Ngân hàng câu hỏi Toán 9 (KNTT) – Chương VII. Tần số và tần số tương đối: Bài 22, Bài 23.
Dùng chung BANK/ABCD_TITLES của sp_g9. Câu có bảng hoặc biểu đồ trả thêm khóa fig = (html_en, html_vi), ghép sau đề.
Mọi đáp án tính bằng số nguyên/Fraction từ chính dữ liệu sinh ra (đếm lại dãy dữ liệu, cộng lại tần số)."""
import random
from fractions import Fraction as F
from sp_g9 import BANK, ABCD_TITLES, tx, dm, dopt, pick_opts
from chart_g9 import CHART_Q

# ---------------------------------------------------------------- bối cảnh dữ liệu
CTX = [
    dict(le='Score', lv='Điểm', ae='the test scores of %d students', av='điểm bài kiểm tra của %d học sinh', ue='students', uv='học sinh', vals=[5, 6, 7, 8, 9, 10], ne='the score', nv='điểm'),
    dict(le='Number of children', lv='Số con', ae='the number of children in %d families', av='số con của %d gia đình', ue='families', uv='gia đình', vals=[0, 1, 2, 3, 4], ne='the number of children', nv='số con'),
    dict(le='Shoe size', lv='Cỡ giày', ae='the shoe sizes of %d students', av='cỡ giày của %d học sinh', ue='students', uv='học sinh', vals=[36, 37, 38, 39, 40, 41], ne='the shoe size', nv='cỡ giày'),
    dict(le='Hours of sleep', lv='Số giờ ngủ', ae='the hours of sleep of %d students last night', av='số giờ ngủ đêm qua của %d học sinh', ue='students', uv='học sinh', vals=[6, 7, 8, 9, 10], ne='the number of hours of sleep', nv='số giờ ngủ'),
    dict(le='Books read', lv='Số sách đã đọc', ae='the number of books read last month by %d students', av='số quyển sách đã đọc trong tháng trước của %d học sinh', ue='students', uv='học sinh', vals=[0, 1, 2, 3, 4, 5], ne='the number of books read', nv='số sách đã đọc'),
    dict(le='Goals', lv='Số bàn thắng', ae='the number of goals scored in %d football matches', av='số bàn thắng trong %d trận bóng đá', ue='matches', uv='trận', vals=[0, 1, 2, 3, 4, 5], ne='the number of goals', nv='số bàn thắng'),
]
CATS = [
    dict(le='Fruit', lv='Loại quả', ae='the favourite fruits of %d students', av='loại quả yêu thích của %d học sinh', ue='students', uv='học sinh',
         vals=[('apple', 'táo'), ('banana', 'chuối'), ('mango', 'xoài'), ('orange', 'cam'), ('grape', 'nho')]),
    dict(le='Sport', lv='Môn thể thao', ae='the favourite sports of %d students', av='môn thể thao yêu thích của %d học sinh', ue='students', uv='học sinh',
         vals=[('football', 'bóng đá'), ('badminton', 'cầu lông'), ('swimming', 'bơi lội'), ('chess', 'cờ vua'), ('basketball', 'bóng rổ')]),
    dict(le='Transport', lv='Phương tiện', ae='how %d students travel to school', av='phương tiện đến trường của %d học sinh', ue='students', uv='học sinh',
         vals=[('bicycle', 'xe đạp'), ('on foot', 'đi bộ'), ('bus', 'xe buýt'), ('motorbike', 'xe máy'), ('e-bike', 'xe đạp điện')]),
]
FEN, FVI = 'Frequency (m)', 'Tần số (m)'
RFEN, RFVI = 'Relative frequency (f)', 'Tần số tương đối (f)'


def favour(s):
    """Tiếng Anh Mỹ: favorite."""
    return s.replace('favourite', 'favorite')


for _c in CATS: _c['ae'] = favour(_c['ae'])


def _vx(x, lang):
    if isinstance(x, tuple): return x[0] if lang == 'en' else x[1]
    return str(x)


def times(m): return 'once' if m == 1 else '%d times' % m


def psum(L):
    return '+'.join(map(str, L)) if len(L) > 1 else None


def pct(m, n): return F(100 * m, n)


def pe(x):
    """Phần trăm/số dạng tiếng Anh (12.5)."""
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else ('%g' % float(x))


def pv(x): return pe(x).replace('.', ',')


def htab(rows, lang):
    """Bảng ngang kẻ đủ đường. rows: [(nhãn_en, nhãn_vi, [ô...]), ...]; ô số tự đổi dấu thập phân."""
    def cell(v):
        if isinstance(v, (F, float)): v = pe(v) if lang == 'en' else pv(v)
        return _vx(v, lang)
    s = ''.join('<tr><th scope="row">%s</th>%s</tr>' % (re if lang == 'en' else rv, ''.join('<td>%s</td>' % cell(v) for v in cells)) for re, rv, cells in rows)
    return '<div class="mbl-tablewrap mbl-freqwrap"><table class="mbl-table mbl-freq"><tbody>%s</tbody></table></div>' % s


def ftab(c, xs, ms, rel=False):
    lab = (RFEN, RFVI) if rel else (FEN, FVI)
    ms2 = [('%s%%' % pe(m), '%s%%' % pv(m)) if rel and m != '?' else m for m in ms]
    rows = [(c['le'] + ' (x)', c['lv'] + ' (x)', xs), (lab[0], lab[1], ms2)]
    return (htab(rows, 'en'), htab(rows, 'vi'))


def gen(r, c=None, n=(12, 24), k=(4, 6), uniq=True, ns=None):
    """Sinh (bối cảnh, giá trị, tần số). ns: tập cỡ mẫu cho phép."""
    c = c or r.choice(CTX)
    kk = r.randint(k[0], min(k[1], len(c['vals'])))
    st = r.randint(0, len(c['vals']) - kk); xs = c['vals'][st:st + kk]
    for _ in range(2000):
        ms = [r.randint(1, 9) for _ in xs]; N = sum(ms)
        if (ns and N not in ns) or (not ns and not n[0] <= N <= n[1]): continue
        if uniq and (ms.count(max(ms)) > 1 or ms.count(min(ms)) > 1): continue
        return c, xs, ms
    raise AssertionError


def data_list(r, xs, ms, lang='en'):
    d = [x for x, m in zip(xs, ms) for _ in range(m)]
    r2 = random.Random(r.random()); r2.shuffle(d)
    return ', '.join(_vx(x, lang) for x in d), d


def chart(kind, c, xs, ms, rel=False, title=None):
    ye, yv = (RFEN, RFVI) if rel else (FEN.replace(' (m)', ''), FVI.replace(' (m)', ''))
    te, tv = title or ('Frequency chart', 'Biểu đồ tần số')
    return CHART_Q(kind, dict(cats=[_vx(x, 'en') for x in xs], vals=[float(v) for v in ms], xlab=c['le'], ylab=ye, title=te, pct=rel),
                   dict(cats=[_vx(x, 'vi') for x in xs], vals=[float(v) for v in ms], xlab=c['lv'], ylab=yv, title=tv, pct=rel))


def iopts(r, good, bads):
    return pick_opts(r, str(good), [str(b) for b in bads if b != good and b >= 0], fill=lambda k: str(good + k))


def vopts(r, good, others):
    """Phương án là giá trị dữ liệu (số hoặc chữ song ngữ)."""
    def f(x): return tx(x[0], x[1]) if isinstance(x, tuple) else str(x)
    o = [f(good)] + [f(x) for x in others if x != good]
    return o[:4]


def popts(r, good, bads):
    """Phương án phần trăm (EN dấu chấm, VI dấu phẩy)."""
    o = [dopt('%s\\%%' % pe(good))]
    for b in bads:
        b = F(b)
        if b != F(good) and 0 <= b <= 100 and dopt('%s\\%%' % pe(b)) not in o: o.append(dopt('%s\\%%' % pe(b)))
        if len(o) == 4: break
    k = 0
    while len(o) < 4:
        k += 1; v = F(good) + 5 * k
        if dopt('%s\\%%' % pe(v)) not in o and v <= 100: o.append(dopt('%s\\%%' % pe(v)))
        if k > 40: raise AssertionError
    return o


def about(c, n): return c['ae'] % n, c['av'] % n


def about0(c): return c['ae'].replace('%d ', ''), c['av'].replace('%d ', '')

# =====================================================================================================
# BÀI 22. Bảng tần số và biểu đồ tần số
# =====================================================================================================
def b22_count(r, lv):
    c, xs, ms = gen(r, n=(12, 20))
    i = r.randrange(len(xs)); v, m = xs[i], ms[i]; n = sum(ms)
    le, _ = data_list(r, xs, ms); ae, av = about(c, n)
    return dict(en='The data below are %s: %s. What is the frequency of the value %s?' % (ae, le, v),
                vi='Dãy dữ liệu sau là %s: %s. Tần số của giá trị %s là bao nhiêu?' % (av, le, v),
                opts=iopts(r, m, [m + 1, m - 1, n - m, len(xs), m + 2]), ans=0,
                ee='Count the times %s appears: \\(m=%d\\).' % (v, m), ev='Đếm số lần giá trị %s xuất hiện: \\(m=%d\\).' % (v, m))


def b22_n(r, lv):
    c, xs, ms = gen(r, n=(15, 45))
    n = sum(ms)
    return dict(en='The frequency table shows %s. What is the sample size?' % about0(c)[0],
                vi='Bảng tần số sau cho biết %s. Cỡ mẫu là bao nhiêu?' % about0(c)[1],
                opts=iopts(r, n, [len(xs), max(ms), n + 1, n - 1, n + 2]), ans=0,
                ee='\\(n=%s=%d\\).' % ('+'.join(map(str, ms)), n), ev='\\(n=%s=%d\\).' % ('+'.join(map(str, ms)), n), fig=ftab(c, xs, ms))


def b22_bar(r, lv):
    c = r.choice(CTX + CATS)
    c, xs, ms = gen(r, c, n=(15, 40), k=(4, 5))
    n = sum(ms); i = ms.index(max(ms))
    if r.random() < 0.5:
        others = [x for j, x in enumerate(xs) if j != i]; r.shuffle(others)
        return dict(en='The bar chart shows the frequencies of %s. Which value has the greatest frequency?' % about(c, n)[0],
                    vi='Biểu đồ cột cho biết tần số của %s. Giá trị nào có tần số lớn nhất?' % about(c, n)[1],
                    opts=vopts(r, xs[i], others), ans=0, ee='The tallest bar is at %s.' % _vx(xs[i], 'en'), ev='Cột cao nhất ứng với %s.' % _vx(xs[i], 'vi'),
                    fig=chart('bar', c, xs, ms))
    j = r.randrange(len(xs)); m = ms[j]
    return dict(en='The bar chart shows the frequencies of %s. What is the frequency of the value “%s”?' % (about(c, n)[0], _vx(xs[j], 'en')),
                vi='Biểu đồ cột cho biết tần số của %s. Tần số của giá trị “%s” là bao nhiêu?' % (about(c, n)[1], _vx(xs[j], 'vi')),
                opts=iopts(r, m, [x for x in ms if x != m] + [n]), ans=0, ee='The bar of “%s” has height %d.' % (_vx(xs[j], 'en'), m), ev='Cột ứng với “%s” cao %d.' % (_vx(xs[j], 'vi'), m),
                fig=chart('bar', c, xs, ms))


def b22_tf_table(r, lv):
    c, xs, ms = gen(r, n=(12, 18))
    i = r.randrange(len(xs)); v, m = xs[i], ms[i]; n = sum(ms)
    le, _ = data_list(r, xs, ms); truth = r.random() < 0.5
    claim = m if truth else r.choice([m + 1, m - 1] if m > 1 else [m + 1, m + 2])
    ae, av = about(c, n)
    return dict(en='The data are %s: %s. In the frequency table of these data, the value %s has frequency %d.' % (ae, le, v, claim),
                vi='Dữ liệu là %s: %s. Trong bảng tần số của mẫu dữ liệu này, giá trị %s có tần số %d.' % (av, le, v, claim), ans=truth,
                ee='The value %s appears %s.' % (v, times(m)), ev='Giá trị %s xuất hiện %d lần.' % (v, m))


def b22_tf_line(r, lv):
    c, xs, ms = gen(r, n=(20, 45))
    n = sum(ms); ae, av = about(c, n)
    ae = ae.replace('%d ' % n, ''); av = av.replace('%d ' % n, '')
    if r.random() < 0.5:
        truth = r.random() < 0.5; claim = n if truth else n + r.choice([-2, -1, 1, 2])
        return dict(en='The line graph shows the frequencies of %s. The sample size is %d.' % (ae, claim),
                    vi='Biểu đồ đoạn thẳng cho biết tần số của %s. Cỡ mẫu là %d.' % (av, claim), ans=truth,
                    ee='\\(n=%s=%d\\).' % ('+'.join(map(str, ms)), n), ev='\\(n=%s=%d\\).' % ('+'.join(map(str, ms)), n), fig=chart('line', c, xs, ms))
    i, j = r.sample(range(len(xs)), 2); truth = ms[i] > ms[j]
    return dict(en='The line graph shows the frequencies of %s. The value %s appears more often than the value %s.' % (ae, xs[i], xs[j]),
                vi='Biểu đồ đoạn thẳng cho biết tần số của %s. Giá trị %s xuất hiện nhiều lần hơn giá trị %s.' % (av, xs[i], xs[j]), ans=truth,
                ee='Frequencies: %s has %d, %s has %d.' % (xs[i], ms[i], xs[j], ms[j]), ev='Tần số: %s là %d, %s là %d.' % (xs[i], ms[i], xs[j], ms[j]), fig=chart('line', c, xs, ms))


def b22_short_missing(r, lv):
    c, xs, ms = gen(r, n=(20, 45))
    n = sum(ms); i = r.randrange(len(xs)); m = ms[i]
    shown = [('?' if j == i else x) for j, x in enumerate(ms)]
    return dict(en='The frequency table below has sample size \\(n=%d\\). Find the missing frequency.' % n,
                vi='Bảng tần số dưới đây có cỡ mẫu \\(n=%d\\). Tìm tần số còn thiếu.' % n, key=str(m),
                ee='\\(%d-(%s)=%d\\).' % (n, '+'.join(str(x) for j, x in enumerate(ms) if j != i), m),
                ev='\\(%d-(%s)=%d\\).' % (n, '+'.join(str(x) for j, x in enumerate(ms) if j != i), m), fig=ftab(c, xs, shown))


def b22_short_atleast(r, lv):
    c, xs, ms = gen(r, n=(20, 45), k=(5, 6))
    n = sum(ms); j = r.randrange(1, len(xs) - 1); v = xs[j]; s = sum(ms[j:])
    return dict(en='The bar chart shows %s. For how many %s is %s at least %s?' % (about(c, n)[0], c['ue'], c['ne'], v),
                vi='Biểu đồ cột cho biết %s. Có bao nhiêu %s có %s lớn hơn hoặc bằng %s?' % (about(c, n)[1], c['uv'], c['nv'], v), key=str(s),
                ee='\\(%s=%d\\).' % ('+'.join(map(str, ms[j:])), s), ev='\\(%s=%d\\).' % ('+'.join(map(str, ms[j:])), s), fig=chart('bar', c, xs, ms))


def b22_d1_def(r, lv):
    k = r.choice(['freq', 'n', 'line', 'diff'])
    if k == 'freq':
        o = [tx('the number of times it appears', 'số lần giá trị đó xuất hiện'), tx('the value itself', 'chính giá trị đó'),
             tx('the sum of all the values', 'tổng của tất cả các giá trị'), tx('the number of different values', 'số các giá trị khác nhau')]
        return dict(en='In a data set, the frequency of a value is…', vi='Trong một mẫu dữ liệu, tần số của một giá trị là…', opts=o, ans=0,
                    ee='Frequency = number of times the value appears.', ev='Tần số là số lần xuất hiện của giá trị đó.')
    if k == 'n':
        o = [tx('the sum of all the frequencies', 'tổng các tần số'), tx('the greatest frequency', 'tần số lớn nhất'),
             tx('the number of different values', 'số các giá trị khác nhau'), tx('the greatest value', 'giá trị lớn nhất')]
        return dict(en='In a frequency table, the sample size \\(n\\) is equal to…', vi='Trong bảng tần số, cỡ mẫu \\(n\\) bằng…', opts=o, ans=0,
                    ee='\\(n=m_1+m_2+\\dots+m_k\\).', ev='\\(n=m_1+m_2+\\dots+m_k\\).')
    if k == 'line':
        o = [tx('the points \\((x_i;\\ m_i)\\) joined by line segments', 'các điểm \\((x_i;\\ m_i)\\) nối với nhau bằng các đoạn thẳng'), tx('bars of equal height', 'các cột cao bằng nhau'),
             tx('sectors of a circle', 'các hình quạt tròn'), tx('the points \\((m_i;\\ x_i)\\) only', 'chỉ các điểm \\((m_i;\\ x_i)\\)')]
        return dict(en='A frequency line graph is made of…', vi='Biểu đồ tần số dạng đoạn thẳng gồm…', opts=o, ans=0,
                    ee='Mark \\((x_i;\\ m_i)\\) and join consecutive points.', ev='Đánh dấu các điểm \\((x_i;\\ m_i)\\) rồi nối các điểm liên tiếp.')
    o = [tx('the data values', 'các giá trị của dữ liệu'), tx('the frequencies', 'các tần số'), tx('the sample size', 'cỡ mẫu'), tx('the percentages', 'các tỉ lệ phần trăm')]
    return dict(en='In a frequency bar chart, the horizontal axis shows…', vi='Trong biểu đồ tần số dạng cột, trục ngang biểu diễn…', opts=o, ans=0,
                ee='Horizontal axis: values; vertical axis: frequencies.', ev='Trục ngang: các giá trị; trục đứng: tần số.')


def b22_d1_axis(r, lv):
    k = r.choice(['height', 'vert', 'tallest', 'nbars'])
    if k == 'height':
        o = [tx('the frequency of the value', 'tần số của giá trị đó'), tx('the value itself', 'chính giá trị đó'), tx('the sample size', 'cỡ mẫu'), tx('the number of bars', 'số cột')]
        return dict(en='In a frequency bar chart, the height of each bar shows…', vi='Trong biểu đồ tần số dạng cột, chiều cao mỗi cột biểu diễn…', opts=o, ans=0,
                    ee='Height = frequency.', ev='Chiều cao cột bằng tần số.')
    if k == 'vert':
        o = [tx('the frequencies', 'các tần số'), tx('the data values', 'các giá trị'), tx('the sample sizes', 'các cỡ mẫu'), tx('the names of the bars', 'tên các cột')]
        return dict(en='In a frequency chart, the vertical axis shows…', vi='Trong biểu đồ tần số, trục đứng biểu diễn…', opts=o, ans=0,
                    ee='Vertical axis: frequencies.', ev='Trục đứng biểu diễn tần số.')
    if k == 'tallest':
        o = [tx('the value with the greatest frequency', 'giá trị có tần số lớn nhất'), tx('the greatest value', 'giá trị lớn nhất'), tx('the sample size', 'cỡ mẫu'), tx('the last value', 'giá trị cuối cùng')]
        return dict(en='In a frequency bar chart, the tallest bar belongs to…', vi='Trong biểu đồ tần số dạng cột, cột cao nhất ứng với…', opts=o, ans=0,
                    ee='Taller bar = greater frequency.', ev='Cột càng cao thì tần số càng lớn.')
    o = [tx('the number of different values', 'số các giá trị khác nhau'), tx('the sample size', 'cỡ mẫu'), tx('the greatest frequency', 'tần số lớn nhất'), tx('the sum of the values', 'tổng các giá trị')]
    return dict(en='The number of bars in a frequency bar chart is equal to…', vi='Số cột của biểu đồ tần số dạng cột bằng…', opts=o, ans=0,
                ee='One bar for each different value.', ev='Mỗi giá trị khác nhau ứng với một cột.')


def b22_d1_read(r, lv):
    c, xs, ms = gen(r, n=(15, 40))
    i = r.choice([j for j in range(len(xs)) if ms.count(ms[j]) == 1]); m = ms[i]     # tần số được hỏi phải duy nhất
    others = [x for j, x in enumerate(xs) if j != i]; r.shuffle(others)
    return dict(en='In the frequency table below, which value has frequency %d?' % m, vi='Trong bảng tần số dưới đây, giá trị nào có tần số %d?' % m,
                opts=vopts(r, xs[i], others), ans=0, ee='Read the column with \\(m=%d\\): the value is %s.' % (m, xs[i]),
                ev='Đọc cột có \\(m=%d\\): giá trị là %s.' % (m, xs[i]), fig=ftab(c, xs, ms))


def b22_d2_list(r, lv):
    c, xs, ms = gen(r, n=(12, 18), k=(4, 4))
    le, _ = data_list(r, xs, ms); n = sum(ms)
    good = ';\\ '.join(map(str, ms))
    bads = []
    for _ in range(30):
        b = list(ms); t = r.random()
        if t < 0.4: r.shuffle(b)
        else:
            i, j = r.sample(range(4), 2); b[i] += 1; b[j] -= 1
            if b[j] <= 0: continue
        s = ';\\ '.join(map(str, b))
        if s != good and s not in bads: bads.append(s)
        if len(bads) == 3: break
    ae, av = about(c, n)
    return dict(en='The data are %s: %s. The frequencies of the values %s are respectively…' % (ae, le, ', '.join(map(str, xs))),
                vi='Dữ liệu là %s: %s. Tần số của các giá trị %s lần lượt là…' % (av, le, ', '.join(map(str, xs))),
                opts=[good] + bads, ans=0, ee='Count each value: \\(%s\\).' % good, ev='Đếm từng giá trị: \\(%s\\).' % good)


def b22_d2_less(r, lv):
    c, xs, ms = gen(r, n=(12, 20), k=(4, 6))
    le, d = data_list(r, xs, ms); n = sum(ms)
    j = r.randrange(2, len(xs)); v = xs[j]; s = sum(ms[:j])
    ae, av = about(c, n)
    return dict(en='The data are %s: %s. For how many %s is %s less than %s?' % (ae, le, c['ue'], c['ne'], v),
                vi='Dữ liệu là %s: %s. Có bao nhiêu %s có %s nhỏ hơn %s?' % (av, le, c['uv'], c['nv'], v),
                opts=iopts(r, s, [s + ms[j], s - 1, n - s, s + 1]), ans=0, ee='\\(%s=%d\\).' % ('+'.join(map(str, ms[:j])), s), ev='\\(%s=%d\\).' % ('+'.join(map(str, ms[:j])), s))


def b22_d2_cat(r, lv):
    c, xs, ms = gen(r, r.choice(CATS), n=(10, 16), k=(3, 4))
    n = sum(ms); i = r.randrange(len(xs)); m = ms[i]
    le, _ = data_list(r, xs, ms, 'en'); lvv, _ = data_list(random.Random(r.random()), xs, ms, 'vi')
    ae, av = about(c, n)
    return dict(en='The answers of a survey about %s are: %s. What is the frequency of “%s”?' % (ae, le, xs[i][0]),
                vi='Kết quả khảo sát về %s là: %s. Tần số của “%s” là bao nhiêu?' % (av, lvv, xs[i][1]),
                opts=iopts(r, m, [m + 1, m - 1, n - m, len(xs)]), ans=0, ee='“%s” appears %s.' % (xs[i][0], times(m)), ev='“%s” xuất hiện %d lần.' % (xs[i][1], m))


def b22_d3_more(r, lv):
    c, xs, ms = gen(r, n=(20, 45), k=(5, 6))
    n = sum(ms); j = r.randrange(1, len(xs) - 2); v = xs[j]; s = sum(ms[j + 1:])
    return dict(en='The line graph shows %s. For how many %s is %s greater than %s?' % (about(c, n)[0], c['ue'], c['ne'], v),
                vi='Biểu đồ đoạn thẳng cho biết %s. Có bao nhiêu %s có %s lớn hơn %s?' % (about(c, n)[1], c['uv'], c['nv'], v),
                opts=iopts(r, s, [s + ms[j], n - s, s - 1, s + 1]), ans=0, ee='\\(%s=%d\\).' % ('+'.join(map(str, ms[j + 1:])), s), ev='\\(%s=%d\\).' % ('+'.join(map(str, ms[j + 1:])), s),
                fig=chart('line', c, xs, ms))


def b22_d3_diff(r, lv):
    c = r.choice(CATS + CTX)
    c, xs, ms = gen(r, c, n=(20, 45), k=(4, 5))
    n = sum(ms); a, b = ms.index(max(ms)), ms.index(min(ms)); d = ms[a] - ms[b]
    return dict(en='The bar chart shows %s. How many more %s chose the most popular answer than the least popular answer?' % (about(c, n)[0], c['ue']) if c in CATS else
                'The bar chart shows %s. What is the difference between the greatest and the least frequency?' % about(c, n)[0],
                vi='Biểu đồ cột cho biết %s. Số %s chọn câu trả lời được chọn nhiều nhất nhiều hơn số %s chọn câu trả lời được chọn ít nhất là bao nhiêu?' % (about(c, n)[1], c['uv'], c['uv']) if c in CATS else
                'Biểu đồ cột cho biết %s. Hiệu giữa tần số lớn nhất và tần số nhỏ nhất là bao nhiêu?' % about(c, n)[1],
                opts=iopts(r, d, [ms[a], ms[b], ms[a] + ms[b], d + 1, d - 1]), ans=0, ee='\\(%d-%d=%d\\).' % (ms[a], ms[b], d), ev='\\(%d-%d=%d\\).' % (ms[a], ms[b], d),
                fig=chart('bar', c, xs, ms))


def b22_d3_total(r, lv):
    c, xs, ms = gen(r, r.choice(CATS), n=(25, 50), k=(4, 5))
    n = sum(ms)
    ae, av = about0(c); cl = '9' + r.choice('ABCDEG')
    return dict(en='The bar chart shows the results of a survey about %s in class %s. How many %s took part in the survey?' % (ae, cl, c['ue']),
                vi='Biểu đồ cột cho biết kết quả khảo sát về %s lớp %s. Có bao nhiêu %s tham gia khảo sát?' % (av, cl, c['uv']),
                opts=iopts(r, n, [n - 1, n + 1, max(ms), len(xs), n - min(ms)]), ans=0, ee='\\(n=%s=%d\\).' % ('+'.join(map(str, ms)), n), ev='\\(n=%s=%d\\).' % ('+'.join(map(str, ms)), n),
                fig=chart('bar', c, xs, ms, title=('Survey results', 'Kết quả khảo sát')))


AQI = [('Good', 'Tốt'), ('Moderate', 'Trung bình'), ('Poor', 'Kém'), ('Bad', 'Xấu')]
AQC = dict(le='Air quality', lv='Chất lượng không khí', ue='days', uv='ngày')


def b22_d4_aqi(r, lv):
    for _ in range(500):
        ms = [r.randint(5, 14), r.randint(6, 14), r.randint(2, 8), r.randint(0, 5)]
        if sum(ms) == 30 and ms[3] >= 1: break
    else: raise AssertionError
    g, pb = ms[0], ms[2] + ms[3]; d = g - pb
    if d <= 0: raise AssertionError
    mo = r.choice([('April', 'tháng Tư'), ('June', 'tháng Sáu'), ('September', 'tháng Chín'), ('November', 'tháng Mười Một')])
    return dict(en='The bar chart shows the air quality index (AQI) of a city over 30 days of %s. How many more days had good air quality than poor or bad air quality?' % mo[0],
                vi='Biểu đồ cột cho biết chất lượng không khí (theo chỉ số AQI) của một thành phố trong 30 ngày của %s. Số ngày không khí tốt nhiều hơn số ngày không khí kém hoặc xấu là bao nhiêu?' % mo[1],
                opts=iopts(r, d, [g - ms[2], g - ms[3], pb, d + 1, 30 - g]), ans=0, ee='\\(%d-(%d+%d)=%d\\).' % (g, ms[2], ms[3], d), ev='\\(%d-(%d+%d)=%d\\).' % (g, ms[2], ms[3], d),
                fig=chart('bar', AQC, AQI, ms, title=('AQI in %s' % mo[0], 'Chất lượng không khí %s' % mo[1])))


def b22_d4_eq(r, lv):
    for _ in range(500):
        c, xs, ms = gen(r, r.choice([CTX[0], CTX[2], CTX[3]]), n=(25, 45), k=(4, 5), uniq=False)
        i = len(xs) - 2; j = len(xs) - 1; kf = r.choice([2, 3])
        if ms[i] == kf * ms[j]: break
    else: raise AssertionError
    n = sum(ms); rest = n - ms[i] - ms[j]
    shown = [('?' if t in (i, j) else x) for t, x in enumerate(ms)]
    return dict(en='The frequency table below has sample size \\(n=%d\\). The frequency of %s is %d times the frequency of %s. Find the frequency of %s.' % (n, xs[i], kf, xs[j], xs[j]),
                vi='Bảng tần số dưới đây có cỡ mẫu \\(n=%d\\). Tần số của giá trị %s gấp %d lần tần số của giá trị %s. Tìm tần số của giá trị %s.' % (n, xs[i], kf, xs[j], xs[j]),
                opts=iopts(r, ms[j], [ms[i], n - rest, ms[j] + 1, ms[j] - 1]), ans=0,
                ee='\\(%dm+m=%d-%d=%d\\Rightarrow m=%d\\).' % (kf, n, rest, n - rest, ms[j]), ev='\\(%dm+m=%d-%d=%d\\Rightarrow m=%d\\).' % (kf, n, rest, n - rest, ms[j]),
                fig=ftab(c, xs, shown))


def b22_d4_compare(r, lv):
    c = CTX[0]; xs = [5, 6, 7, 8, 9, 10]; t = r.choice([7, 8, 9]); k = xs.index(t)
    A, B = r.choice([('9A', '9B'), ('9C', '9D'), ('9A', '9C'), ('9B', '9D'), ('9E', '9G')])
    for _ in range(500):
        a = [r.randint(1, 9) for _ in xs]; b = [r.randint(1, 9) for _ in xs]
        sa, sb = sum(a[k:]), sum(b[k:])
        if sa != sb and 25 <= sum(a) <= 45 and 25 <= sum(b) <= 45: break
    else: raise AssertionError
    d = abs(sa - sb); big, small = (A, B) if sa > sb else (B, A)
    rows = [(c['le'] + ' (x)', c['lv'] + ' (x)', xs), (A + ': ' + FEN, A + ': ' + FVI, a), (B + ': ' + FEN, B + ': ' + FVI, b)]
    o = [tx('class %s, %d students more' % (big, d), 'lớp %s, nhiều hơn %d học sinh' % (big, d)),
         tx('class %s, %d students more' % (small, d), 'lớp %s, nhiều hơn %d học sinh' % (small, d)),
         tx('class %s, %d students more' % (big, d + 1), 'lớp %s, nhiều hơn %d học sinh' % (big, d + 1)),
         tx('both classes have the same number', 'hai lớp bằng nhau')]
    return dict(en='The table shows the test scores of classes %s and %s. Which class has more students scoring %d or more, and by how many?' % (A, B, t),
                vi='Bảng sau cho biết điểm bài kiểm tra của lớp %s và lớp %s. Lớp nào có nhiều học sinh đạt từ %d điểm trở lên hơn và nhiều hơn bao nhiêu?' % (A, B, t),
                opts=o, ans=0, ee='%s: \\(%s=%d\\); %s: \\(%s=%d\\).' % (A, '+'.join(map(str, a[k:])), sa, B, '+'.join(map(str, b[k:])), sb),
                ev='%s: \\(%s=%d\\); %s: \\(%s=%d\\).' % (A, '+'.join(map(str, a[k:])), sa, B, '+'.join(map(str, b[k:])), sb),
                fig=(htab(rows, 'en'), htab(rows, 'vi')))


L22_GROUPS = [[('mcq', b22_count), ('mcq', b22_n), ('mcq', b22_bar)], [('tf', b22_tf_table), ('tf', b22_tf_line)], [('short', b22_short_missing), ('short', b22_short_atleast)],
              [('mcq', b22_d1_def), ('mcq', b22_d1_axis), ('mcq', b22_d1_read)], [('mcq', b22_d2_list), ('mcq', b22_d2_less), ('mcq', b22_d2_cat)],
              [('mcq', b22_d3_more), ('mcq', b22_d3_diff), ('mcq', b22_d3_total)], [('mcq', b22_d4_aqi), ('mcq', b22_d4_eq), ('mcq', b22_d4_compare)]]

# =====================================================================================================
# BÀI 23. Bảng tần số tương đối và biểu đồ tần số tương đối
# =====================================================================================================
NS = (20, 25, 40, 50)


def b23_f(r, lv):
    c, xs, ms = gen(r, ns=NS)
    n = sum(ms); i = r.randrange(len(xs)); m = ms[i]; f = pct(m, n)
    return dict(en='The frequency table below has sample size \\(n=%d\\). What is the relative frequency of the value %s?' % (n, xs[i]),
                vi='Bảng tần số dưới đây có cỡ mẫu \\(n=%d\\). Tần số tương đối của giá trị %s là bao nhiêu?' % (n, xs[i]),
                opts=popts(r, f, [m, pct(ms[(i + 1) % len(ms)], n), 100 - f, F(m, 2)]), ans=0,
                ee='\\(f=\\dfrac{%d}{%d}\\cdot100\\%%=%s\\%%\\).' % (m, n, pe(f)), ev='\\(f=\\dfrac{%d}{%d}\\cdot100\\%%=%s\\%%\\).' % (m, n, dm(pe(f))), fig=ftab(c, xs, ms))


def b23_m(r, lv):
    c = r.choice(CATS); i = r.randrange(len(c['vals'])); v = c['vals'][i]
    while True:
        n = r.choice([40, 50, 80, 120, 150, 200, 250, 300]); f = r.choice([10, 12, 15, 16, 20, 24, 25, 30, 35, 40, 45])
        if (n * f) % 100 == 0: break
    m = n * f // 100
    return dict(en='In a survey of %d %s, the relative frequency of the answer “%s” is %d%%. How many %s gave this answer?' % (n, c['ue'], v[0], f, c['ue']),
                vi='Khảo sát %d %s, tần số tương đối của câu trả lời “%s” là %d%%. Có bao nhiêu %s chọn câu trả lời này?' % (n, c['uv'], v[1], f, c['uv']),
                opts=iopts(r, m, [f, n - m, m * 2, m + 5, n // f if n % f == 0 else m + 1]), ans=0,
                ee='\\(m=%d\\cdot%d\\%%=%d\\).' % (n, f, m), ev='\\(m=%d\\cdot%d\\%%=%d\\).' % (n, f, m))


def _pie_data(r, c, n, k=4):
    for _ in range(3000):
        ms = [r.randint(1, n) for _ in range(k)]
        if sum(ms) == n and all((100 * m) % n == 0 for m in ms) and len(set(ms)) == k and min(ms) * 100 >= 5 * n: return ms
    raise AssertionError


def pie_q(c, xs, ms, title):
    n = sum(ms); ps = [pct(m, n) for m in ms]
    return CHART_Q('pie', dict(cats=[_vx(x, 'en') for x in xs], pcts=[float(p) for p in ps], title=title[0]),
                   dict(cats=[_vx(x, 'vi') for x in xs], pcts=[float(p) for p in ps], title=title[1]), px=460)


def b23_pie(r, lv):
    c = r.choice(CATS); xs = r.sample(c['vals'], 4); n = r.choice([20, 25, 40, 50, 80, 100, 200])
    ms = _pie_data(r, c, n); i = r.randrange(4); m = ms[i]; f = pct(m, n)
    ae, av = about(c, n)
    return dict(en='The pie chart shows the relative frequencies of %s. How many students chose “%s”?' % (ae, xs[i][0]),
                vi='Biểu đồ hình quạt tròn cho biết tần số tương đối của %s. Có bao nhiêu học sinh chọn “%s”?' % (av, xs[i][1]),
                opts=iopts(r, m, [int(f) if f.denominator == 1 else m + 2, n - m, m + 1, m - 1, ms[(i + 1) % 4]]), ans=0,
                ee='\\(m=%d\\cdot%s\\%%=%d\\).' % (n, pe(f), m), ev='\\(m=%d\\cdot%s\\%%=%d\\).' % (n, dm(pe(f)), m),
                fig=pie_q(c, xs, ms, ('Survey results', 'Kết quả khảo sát')))


def b23_tf_sum(r, lv):
    c, xs, ms = gen(r, ns=NS)
    n = sum(ms); fs = [pct(m, n) for m in ms]; i = r.randrange(len(xs)); truth = r.random() < 0.5
    claim = fs[i] if truth else fs[i] + r.choice([-5, 5, 10, F(5, 2)])
    if claim <= 0: claim = fs[i] + 5
    shown = [('?' if j == i else f) for j, f in enumerate(fs)]
    return dict(en='In the relative frequency table below, the missing relative frequency is \\(%s\\%%\\).' % pe(claim),
                vi='Trong bảng tần số tương đối dưới đây, tần số tương đối còn thiếu là \\(%s\\%%\\).' % dm(pe(claim)), ans=truth,
                ee='The relative frequencies add up to \\(100\\%%\\): missing \\(=%s\\%%\\).' % pe(fs[i]), ev='Tổng các tần số tương đối bằng \\(100\\%%\\): còn thiếu \\(%s\\%%\\).' % dm(pe(fs[i])),
                fig=ftab(c, xs, shown, rel=True))


def b23_tf_angle(r, lv):
    f = r.choice([5, 10, 12.5, 15, 20, 25, 30, 35, 40, 45, 37.5, 62.5, 22.5]); f = F(str(f)); a = f * F(18, 5)
    truth = r.random() < 0.5; claim = a if truth else r.choice([f, a + 18, a - 18, f * 3])
    if claim == a: truth = True
    return dict(en='In a pie chart, the sector of a value with relative frequency \\(%s\\%%\\) has a central angle of \\(%s^\\circ\\).' % (pe(f), pe(claim)),
                vi='Trong biểu đồ hình quạt tròn, hình quạt ứng với giá trị có tần số tương đối \\(%s\\%%\\) có góc ở tâm bằng \\(%s^\\circ\\).' % (dm(pe(f)), dm(pe(claim))), ans=truth,
                ee='\\(%s\\%%\\cdot360^\\circ=%s^\\circ\\).' % (pe(f), pe(a)), ev='\\(%s\\%%\\cdot360^\\circ=%s^\\circ\\).' % (dm(pe(f)), dm(pe(a))))


def b23_short_missing(r, lv):
    c, xs, ms = gen(r, ns=NS, k=(4, 5))
    n = sum(ms); fs = [pct(m, n) for m in ms]; i = r.randrange(len(xs))
    shown = [('?' if j == i else f) for j, f in enumerate(fs)]
    k = pe(fs[i])
    ae, av = about(c, n)
    return dict(en='The table below shows the relative frequencies of %s. Find the missing relative frequency (in %%).' % ae,
                vi='Bảng dưới đây cho biết tần số tương đối của %s. Tìm tần số tương đối (tính theo %%) còn thiếu.' % av, key=k,
                hint=('Enter a number (e.g. 12.5).', 'Nhập một số (ví dụ 12,5).'),
                ee='\\(100-(%s)=%s\\).' % ('+'.join(pe(f) for j, f in enumerate(fs) if j != i), k), ev='\\(100-(%s)=%s\\).' % ('+'.join(dm(pe(f)) for j, f in enumerate(fs) if j != i), dm(k)),
                fig=ftab(c, xs, shown, rel=True))


def b23_short_count(r, lv):
    c, xs, ms = gen(r, ns=NS, k=(4, 5))
    n = sum(ms); fs = [pct(m, n) for m in ms]; i = r.randrange(len(xs))
    ae, av = about(c, n)
    return dict(en='The bar chart shows the relative frequencies of %s. For how many %s is %s equal to %s?' % (ae, c['ue'], c['ne'], xs[i]),
                vi='Biểu đồ cột cho biết tần số tương đối của %s. Có bao nhiêu %s có %s bằng %s?' % (av, c['uv'], c['nv'], xs[i]), key=str(ms[i]),
                ee='\\(m=%d\\cdot%s\\%%=%d\\).' % (n, pe(fs[i]), ms[i]), ev='\\(m=%d\\cdot%s\\%%=%d\\).' % (n, dm(pe(fs[i])), ms[i]),
                fig=chart('bar', c, xs, fs, rel=True, title=('Relative frequency chart', 'Biểu đồ tần số tương đối')))


def b23_d1_formula(r, lv):
    k = r.choice(['f', 'unit', 'm'])
    if k == 'f':
        o = ['f_i=\\dfrac{m_i}{n}\\cdot100\\%', 'f_i=\\dfrac{n}{m_i}\\cdot100\\%', 'f_i=m_i\\cdot n', 'f_i=\\dfrac{m_i}{100}']
        return dict(en='A value \\(x_i\\) has frequency \\(m_i\\) in a sample of size \\(n\\). Its relative frequency is…', vi='Giá trị \\(x_i\\) có tần số \\(m_i\\) trong mẫu có cỡ \\(n\\). Tần số tương đối của \\(x_i\\) là…',
                    opts=o, ans=0, ee='\\(f_i=\\dfrac{m_i}{n}\\cdot100\\%\\).', ev='\\(f_i=\\dfrac{m_i}{n}\\cdot100\\%\\).')
    if k == 'unit':
        o = [tx('a percentage of the sample size', 'tỉ số phần trăm so với cỡ mẫu'), tx('a number of times', 'một số lần'), tx('a value of the data', 'một giá trị của dữ liệu'), tx('an angle', 'một góc')]
        return dict(en='The relative frequency of a value tells us its frequency as…', vi='Tần số tương đối của một giá trị cho biết tần số đó dưới dạng…', opts=o, ans=0,
                    ee='It is the ratio \\(m_i:n\\) written as a percentage.', ev='Đó là tỉ số \\(m_i:n\\) viết dưới dạng phần trăm.')
    o = ['m_i=\\dfrac{f_i\\cdot n}{100}', 'm_i=\\dfrac{n}{f_i}', 'm_i=f_i+n', 'm_i=\\dfrac{100\\,f_i}{n}']
    return dict(en='If the relative frequency \\(f_i\\) (in %) and the sample size \\(n\\) are known, then the frequency is…', vi='Nếu biết tần số tương đối \\(f_i\\) (tính theo %) và cỡ mẫu \\(n\\) thì tần số là…',
                opts=o, ans=0, ee='From \\(f_i=\\dfrac{m_i}{n}\\cdot100\\) we get \\(m_i=\\dfrac{f_i\\cdot n}{100}\\).', ev='Từ \\(f_i=\\dfrac{m_i}{n}\\cdot100\\) suy ra \\(m_i=\\dfrac{f_i\\cdot n}{100}\\).')


def b23_d1_total(r, lv):
    k = r.choice(['sum', 'circle', 'angle', 'bar'])
    if k == 'sum':
        o = ['100\\%', '1\\%', 'n', '360\\%']
        return dict(en='The sum of all relative frequencies in a relative frequency table is…', vi='Tổng các tần số tương đối trong bảng tần số tương đối bằng…', opts=o, ans=0,
                    ee='\\(f_1+f_2+\\dots+f_k=100\\%\\).', ev='\\(f_1+f_2+\\dots+f_k=100\\%\\).')
    if k == 'circle':
        o = [tx('the whole sample (100%)', 'toàn bộ mẫu dữ liệu (100%)'), tx('the greatest value', 'giá trị lớn nhất'), tx('the greatest frequency', 'tần số lớn nhất'), tx('one value of the data', 'một giá trị của dữ liệu')]
        return dict(en='In a pie chart, the whole circle represents…', vi='Trong biểu đồ hình quạt tròn, cả hình tròn biểu diễn…', opts=o, ans=0,
                    ee='The whole circle is 100%.', ev='Cả hình tròn ứng với 100%.')
    if k == 'angle':
        o = ['f_i\\cdot360^\\circ', 'f_i\\cdot180^\\circ', 'f_i\\cdot100^\\circ', '\\dfrac{360^\\circ}{f_i}']
        return dict(en='In a pie chart, the sector of a value with relative frequency \\(f_i\\) has central angle…', vi='Trong biểu đồ hình quạt tròn, hình quạt ứng với giá trị có tần số tương đối \\(f_i\\) có góc ở tâm bằng…',
                    opts=o, ans=0, ee='Angle \\(=f_i\\cdot360^\\circ\\).', ev='Góc ở tâm \\(=f_i\\cdot360^\\circ\\).')
    o = [tx('the relative frequency of the value', 'tần số tương đối của giá trị đó'), tx('the value itself', 'chính giá trị đó'), tx('the sample size', 'cỡ mẫu'), tx('the central angle', 'góc ở tâm')]
    return dict(en='In a relative frequency bar chart, the height of each bar shows…', vi='Trong biểu đồ tần số tương đối dạng cột, chiều cao mỗi cột biểu diễn…', opts=o, ans=0,
                ee='Height = relative frequency (%).', ev='Chiều cao cột bằng tần số tương đối (%).')


def b23_d1_read(r, lv):
    c, xs, ms = gen(r, ns=NS)
    n = sum(ms); fs = [pct(m, n) for m in ms]; i = r.choice([j for j in range(len(xs)) if ms.count(ms[j]) == 1])
    others = [x for j, x in enumerate(xs) if j != i]; r.shuffle(others)
    return dict(en='In the relative frequency table below, which value has relative frequency \\(%s\\%%\\)?' % pe(fs[i]),
                vi='Trong bảng tần số tương đối dưới đây, giá trị nào có tần số tương đối \\(%s\\%%\\)?' % dm(pe(fs[i])),
                opts=vopts(r, xs[i], others), ans=0, ee='Read the table: %s.' % xs[i], ev='Đọc bảng: %s.' % xs[i], fig=ftab(c, xs, fs, rel=True))


def b23_d2_table(r, lv):
    c, xs, ms = gen(r, ns=NS, k=(4, 4))
    n = sum(ms); fs = [pct(m, n) for m in ms]
    def L(v): return tx('\\(%s\\)' % ';\\ '.join(pe(x) + '\\%' for x in v), '\\(%s\\)' % ';\\ '.join(dm(pe(x)) + '\\%' for x in v))
    good = L(fs); bads = []
    for cand in ([F(m) for m in ms], [pct(m, n) for m in reversed(ms)], [F(m, n) for m in ms], [x + (5 if j == 0 else -5 if j == 1 else 0) for j, x in enumerate(fs)]):
        o = L(cand)
        if o != good and o not in bads and all(x >= 0 for x in cand): bads.append(o)
    if len(bads) < 3: raise AssertionError
    return dict(en='Using the frequency table below (sample size \\(n=%d\\)), the relative frequencies of %s are respectively…' % (n, ', '.join(map(str, xs))),
                vi='Từ bảng tần số dưới đây (cỡ mẫu \\(n=%d\\)), tần số tương đối của các giá trị %s lần lượt là…' % (n, ', '.join(map(str, xs))),
                opts=[good] + bads[:3], ans=0, ee='\\(f_i=\\dfrac{m_i}{%d}\\cdot100\\%%\\).' % n, ev='\\(f_i=\\dfrac{m_i}{%d}\\cdot100\\%%\\).' % n, fig=ftab(c, xs, ms))


def b23_d2_angle(r, lv):
    while True:
        n = r.choice([20, 24, 30, 36, 40, 45, 60, 72, 90, 120]); m = r.randint(1, n // 2)
        a = F(360 * m, n)
        if a.denominator == 1: break
    c = r.choice(CATS); v = r.choice(c['vals']); a = int(a)
    return dict(en='In a survey of %d students, %d chose “%s”. In the pie chart of the results, what is the central angle of the sector for “%s”?' % (n, m, v[0], v[0]),
                vi='Khảo sát %d học sinh, có %d em chọn “%s”. Trong biểu đồ hình quạt tròn biểu diễn kết quả, góc ở tâm của hình quạt ứng với “%s” bằng bao nhiêu?' % (n, m, v[1], v[1]),
                opts=['%d^\\circ' % a] + ['%s^\\circ' % x for x in pick_opts(r, str(a), [str(x) for x in (m, 180 * m // n if 180 * m % n == 0 else a + 10, a + 18, a - 18, 3 * m) if x > 0 and x != a], fill=lambda k: str(a + 9 * k))[1:]],
                ans=0, ee='\\(\\dfrac{%d}{%d}\\cdot360^\\circ=%d^\\circ\\).' % (m, n, a), ev='\\(\\dfrac{%d}{%d}\\cdot360^\\circ=%d^\\circ\\).' % (m, n, a))


def b23_d2_data(r, lv):
    c, xs, ms = gen(r, ns=(20, 25), k=(4, 5))
    n = sum(ms); i = r.randrange(len(xs)); f = pct(ms[i], n)
    le, _ = data_list(r, xs, ms); ae, av = about(c, n)
    return dict(en='The data are %s: %s. What is the relative frequency of the value %s?' % (ae, le, xs[i]),
                vi='Dữ liệu là %s: %s. Tần số tương đối của giá trị %s là bao nhiêu?' % (av, le, xs[i]),
                opts=popts(r, f, [ms[i], pct(ms[i] + 1, n), pct(ms[i] - 1, n), 100 - f]), ans=0,
                ee='\\(m=%d\\), \\(f=\\dfrac{%d}{%d}\\cdot100\\%%=%s\\%%\\).' % (ms[i], ms[i], n, pe(f)), ev='\\(m=%d\\), \\(f=\\dfrac{%d}{%d}\\cdot100\\%%=%s\\%%\\).' % (ms[i], ms[i], n, dm(pe(f))))


def b23_d3_bar(r, lv):
    c, xs, ms = gen(r, ns=NS, k=(4, 5))
    n = sum(ms); fs = [pct(m, n) for m in ms]; d = max(fs) - min(fs)
    ae, av = about(c, n)
    return dict(en='The bar chart shows the relative frequencies of %s. By how many percentage points does the greatest relative frequency exceed the least one?' % ae,
                vi='Biểu đồ cột cho biết tần số tương đối của %s. Tần số tương đối lớn nhất hơn tần số tương đối nhỏ nhất bao nhiêu điểm phần trăm?' % av,
                opts=popts(r, d, [max(fs), min(fs), max(ms) - min(ms), max(fs) + min(fs)]), ans=0,
                ee='\\(%s\\%%-%s\\%%=%s\\%%\\).' % (pe(max(fs)), pe(min(fs)), pe(d)), ev='\\(%s\\%%-%s\\%%=%s\\%%\\).' % (dm(pe(max(fs))), dm(pe(min(fs))), dm(pe(d))),
                fig=chart('bar', c, xs, fs, rel=True, title=('Relative frequency chart', 'Biểu đồ tần số tương đối')))


def b23_d3_pie_n(r, lv):
    c = r.choice(CATS); xs = r.sample(c['vals'], 4); n = r.choice([40, 50, 80, 100, 200, 120])
    ms = _pie_data(r, c, n); i = r.randrange(4); f = pct(ms[i], n)
    return dict(en='The pie chart shows the results of a survey about %s. Exactly %d students chose “%s”. How many students took part in the survey?' % (about0(c)[0], ms[i], xs[i][0]),
                vi='Biểu đồ hình quạt tròn cho biết kết quả khảo sát về %s. Có đúng %d học sinh chọn “%s”. Hỏi có bao nhiêu học sinh tham gia khảo sát?' % (about0(c)[1], ms[i], xs[i][1]),
                opts=iopts(r, n, [ms[i] * 2, n + 10, n - 10, 100, ms[i] + 100]), ans=0,
                ee='\\(n=\\dfrac{%d\\cdot100}{%s}=%d\\).' % (ms[i], pe(f), n), ev='\\(n=\\dfrac{%d\\cdot100}{%s}=%d\\).' % (ms[i], dm(pe(f)), n),
                fig=pie_q(c, xs, ms, ('Survey results', 'Kết quả khảo sát')))


def b23_d3_n(r, lv):
    while True:
        n = r.choice([40, 50, 60, 80, 120, 150, 160, 200, 240, 300, 400]); f = r.choice([5, 10, 15, 20, 25, 30, 35, 40, 45, 12.5, 7.5])
        m = F(str(f)) * n / 100
        if m.denominator == 1 and m > 0: break
    m = int(m); f = F(str(f))
    return dict(en='In a sample, the value \\(a\\) has frequency %d and relative frequency \\(%s\\%%\\). What is the sample size?' % (m, pe(f)),
                vi='Trong một mẫu dữ liệu, giá trị \\(a\\) có tần số %d và tần số tương đối \\(%s\\%%\\). Cỡ mẫu là bao nhiêu?' % (m, dm(pe(f))),
                opts=iopts(r, n, [int(m * f) if (m * f).denominator == 1 else n + 20, m + 100, 2 * n, n // 2]), ans=0,
                ee='\\(n=\\dfrac{%d\\cdot100}{%s}=%d\\).' % (m, pe(f), n), ev='\\(n=\\dfrac{%d\\cdot100}{%s}=%d\\).' % (m, dm(pe(f)), n))


def b23_d4_compare(r, lv):
    for _ in range(3000):
        na, nb = r.choice([36, 40, 45, 32]), r.choice([25, 30, 20, 24])
        ma, mb = r.randint(5, na - 5), r.randint(5, nb - 5)
        fa, fb = pct(ma, na), pct(mb, nb)
        if ma > mb and fa < fb and (fa * 10).denominator == 1 and (fb * 10).denominator == 1: break
    else: raise AssertionError
    o = [tx('9B, because %s%% > %s%%' % (pe(fb), pe(fa)), '9B, vì %s%% > %s%%' % (pv(fb), pv(fa))),
         tx('9A, because %d > %d' % (ma, mb), '9A, vì %d > %d' % (ma, mb)),
         tx('9A, because %s%% > %s%%' % (pe(fa), pe(fb)), '9A, vì %s%% > %s%%' % (pv(fa), pv(fb))),
         tx('the two classes are the same', 'hai lớp như nhau')]
    return dict(en='Class 9A has %d students, %d of whom read books every day. Class 9B has %d students, %d of whom read books every day. In which class is the proportion of students who read every day higher?' % (na, ma, nb, mb),
                vi='Lớp 9A có %d học sinh, trong đó %d em đọc sách mỗi ngày. Lớp 9B có %d học sinh, trong đó %d em đọc sách mỗi ngày. Lớp nào có tỉ lệ học sinh đọc sách mỗi ngày cao hơn?' % (na, ma, nb, mb),
                opts=o, ans=0, ee='9A: \\(\\dfrac{%d}{%d}\\cdot100\\%%=%s\\%%\\); 9B: \\(\\dfrac{%d}{%d}\\cdot100\\%%=%s\\%%\\). Compare relative frequencies, not frequencies.' % (ma, na, pe(fa), mb, nb, pe(fb)),
                ev='9A: \\(\\dfrac{%d}{%d}\\cdot100\\%%=%s\\%%\\); 9B: \\(\\dfrac{%d}{%d}\\cdot100\\%%=%s\\%%\\). Cần so sánh tần số tương đối, không so sánh tần số.' % (ma, na, dm(pe(fa)), mb, nb, dm(pe(fb))))


def b23_d4_diff(r, lv):
    c = r.choice(CATS); v = r.choice(c['vals'])
    for _ in range(3000):
        n1, n2 = r.choice([40, 50, 80, 120, 160, 200]), r.choice([40, 50, 80, 120, 160, 200, 250])
        m1, m2 = r.randint(4, n1 // 2), r.randint(4, n2 // 2)
        f1, f2 = pct(m1, n1), pct(m2, n2)
        if n1 != n2 and (f1 * 2).denominator == 1 and (f2 * 2).denominator == 1 and f1 != f2 and (m1 - m2) * (f1 - f2) < 0: break
    else: raise AssertionError
    d = abs(f2 - f1); up = f2 > f1
    return dict(en='In a survey about %s last year, %d of %d students chose “%s”. This year, %d of %d students chose it. By how many percentage points did the relative frequency of “%s” %s?' % (about0(c)[0], m1, n1, v[0], m2, n2, v[0], 'increase' if up else 'decrease'),
                vi='Năm ngoái, trong cuộc khảo sát về %s, có %d trong số %d học sinh chọn “%s”. Năm nay, có %d trong số %d học sinh chọn “%s”. Tần số tương đối của “%s” đã %s bao nhiêu điểm phần trăm?' % (about0(c)[1], m1, n1, v[1], m2, n2, v[1], v[1], 'tăng' if up else 'giảm'),
                opts=popts(r, d, [abs(m2 - m1), f1, f2, d + 5]), ans=0,
                ee='\\(%s\\%%\\to%s\\%%\\): the difference is \\(%s\\%%\\).' % (pe(f1), pe(f2), pe(d)), ev='\\(%s\\%%\\to%s\\%%\\): chênh lệch \\(%s\\%%\\).' % (dm(pe(f1)), dm(pe(f2)), dm(pe(d))))


ACT = [('sleep', 'ngủ'), ('school', 'học ở trường'), ('homework', 'tự học'), ('sport', 'thể thao'), ('other', 'việc khác')]


def b23_d4_day(r, lv):
    for _ in range(3000):
        h = [r.choice([7, 8, 9]), r.choice([5, 6, 7]), r.choice([2, 3, 4]), r.choice([1, 2])]; h.append(24 - sum(h))
        if h[4] >= 1 and all((F(h_ * 100, 24) * 2).denominator == 1 for h_ in h): break
    else:
        h = [9, 6, 3, 2, 4]
    i = r.randrange(5); a = 15 * h[i]; f = F(100 * h[i], 24)
    return dict(en='A student spends a day of 24 hours as follows: sleep %d h, school %d h, homework %d h, sport %d h, other %d h. In a pie chart of this day, what is the central angle of the sector for “%s”?' % (tuple(h) + (ACT[i][0],)),
                vi='Một học sinh sử dụng 24 giờ trong ngày như sau: ngủ %d giờ, học ở trường %d giờ, tự học %d giờ, thể thao %d giờ, việc khác %d giờ. Trong biểu đồ hình quạt tròn biểu diễn ngày này, góc ở tâm của hình quạt “%s” bằng bao nhiêu?' % (tuple(h) + (ACT[i][1],)),
                opts=['%d^\\circ' % a] + ['%d^\\circ' % x for x in pick_opts(r, a, [x for x in (10 * h[i], 30 * h[i], a + 15, 360 - a, h[i] * 24) if x != a and x > 0], fill=lambda k: a + 5 * k)[1:]],
                ans=0, ee='\\(\\dfrac{%d}{24}\\cdot360^\\circ=%d^\\circ\\).' % (h[i], a), ev='\\(\\dfrac{%d}{24}\\cdot360^\\circ=%d^\\circ\\).' % (h[i], a))


L23_GROUPS = [[('mcq', b23_f), ('mcq', b23_m), ('mcq', b23_pie)], [('tf', b23_tf_sum), ('tf', b23_tf_angle)], [('short', b23_short_missing), ('short', b23_short_count)],
              [('mcq', b23_d1_formula), ('mcq', b23_d1_total), ('mcq', b23_d1_read)], [('mcq', b23_d2_table), ('mcq', b23_d2_angle), ('mcq', b23_d2_data)],
              [('mcq', b23_d3_bar), ('mcq', b23_d3_pie_n), ('mcq', b23_d3_n)], [('mcq', b23_d4_compare), ('mcq', b23_d4_diff), ('mcq', b23_d4_day)]]
