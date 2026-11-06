# -*- coding: utf-8 -*-
"""Ngân hàng câu hỏi THỐNG KÊ ghép nhóm gắn với tình huống thực tế (lớp 11 Bài 8–9, lớp 12 Bài 9).
Mỗi hàm họ câu hỏi nhận (r: random.Random) và trả về dict:
  MCQ  : dict(en, vi, opts[4], ans, ee, ev)       (opts[ans] là đáp án đúng; tên hàm bắt đầu bằng q_)
  TF   : dict(en, vi, truth, ee, ev)              (tf_)
  SHORT: dict(en, vi, key, ee, ev)                (sh_)
Mọi đáp án do máy tính tính từ bảng (GT, Fraction) – không nhập tay."""
import random
from fractions import Fraction as F
from gdata import GT
from freqtable import FREQ, num
from mb_selfpractice import pick_opts
from mb_lib import TI

def M(x): return '\\(%s\\)' % x
D = num                                    # hiển thị: dấu phẩy thập phân kiểu Việt Nam
def key(x):
    x = F(x); return str(x.numerator) if x.denominator == 1 else ('%.6g' % float(x))

# ---------------- tình huống thực tế ----------------
def S(k, ent, ent1, intro, var, unit, lt, ge, u0, h, kk, gl, fl, tot=None, shift=None):
    return dict(uv={'cm': 'cm', 'minutes': 'phút', 'points': 'điểm', 'million VND': 'triệu đồng', 'kWh': 'kWh', 'g': 'g', 'years': 'tuổi', 'hours': 'giờ'}[unit], k=k, ent=ent, ent1=ent1, intro=intro, var=var, unit=unit, lt=lt, ge=ge, u0=u0, h=h, kk=kk, gl=gl, fl=fl, tot=tot, shift=shift)
SC = [
 S('height', ('students', 'học sinh'), ('student', 'học sinh'), ('The heights of the students in a class were measured and grouped as follows.', 'Đo chiều cao của các học sinh một lớp rồi ghép nhóm số liệu như sau.'), ('height', 'chiều cao'), 'cm',
   ('are shorter than {x} cm', 'cao dưới {x} cm'), ('are at least {x} cm tall', 'cao từ {x} cm trở lên'), (140, 145, 150, 155), (5, 10), (4, 5), 'Chiều cao (cm) / Height (cm)', 'Số học sinh / Students'),
 S('travel', ('students', 'học sinh'), ('student', 'học sinh'), ('A school surveyed how long its students need to travel from home to school.', 'Nhà trường khảo sát thời gian đi từ nhà đến trường của học sinh.'), ('travel time', 'thời gian đi học'), 'minutes',
   ('travel for less than {x} minutes', 'đi học mất dưới {x} phút'), ('travel for at least {x} minutes', 'đi học mất từ {x} phút trở lên'), (0, 5, 10), (5, 10), (4, 5), 'Thời gian (phút) / Time (min)', 'Số học sinh / Students',
   tot=('the total travel time of all the students', 'tổng thời gian đi học của tất cả học sinh', 'minutes', 'phút')),
 S('score', ('students', 'học sinh'), ('student', 'học sinh'), ('A teacher recorded the scores of a test marked out of 50 points.', 'Giáo viên ghi lại điểm một bài kiểm tra chấm theo thang 50 điểm.'), ('score', 'điểm số'), 'points',
   ('scored below {x} points', 'đạt dưới {x} điểm'), ('scored at least {x} points', 'đạt từ {x} điểm trở lên'), (10, 20), (5,), (4, 5), 'Điểm / Score', 'Số học sinh / Students',
   shift=(('The teacher adds {c} bonus points to every score.', 'Giáo viên cộng thêm {c} điểm cho mọi bài làm.'), 'points')),
 S('income', ('workers', 'công nhân'), ('worker', 'công nhân'), ('The monthly incomes (in million VND) of the workers in a workshop are grouped as follows.', 'Thu nhập hằng tháng (triệu đồng) của công nhân một xưởng được ghép nhóm như sau.'), ('monthly income', 'thu nhập hằng tháng'), 'million VND',
   ('earn less than {x} million VND a month', 'có thu nhập dưới {x} triệu đồng/tháng'), ('earn at least {x} million VND a month', 'có thu nhập từ {x} triệu đồng/tháng trở lên'), (6, 8, 10), (2, 4), (4, 5), 'Thu nhập (triệu đồng) / Income', 'Số công nhân / Workers',
   tot=('the total monthly income of all the workers', 'tổng thu nhập hằng tháng của tất cả công nhân', 'million VND', 'triệu đồng'), shift=(('Every worker gets a monthly raise of {c} million VND.', 'Mỗi công nhân được tăng lương {c} triệu đồng/tháng.'), 'million VND')),
 S('power', ('households', 'hộ gia đình'), ('household', 'hộ gia đình'), ('An electricity company recorded the monthly electricity use of households in a street.', 'Công ty điện lực ghi lại lượng điện tiêu thụ hằng tháng của các hộ gia đình một con phố.'), ('monthly electricity use', 'lượng điện tiêu thụ hằng tháng'), 'kWh',
   ('use less than {x} kWh a month', 'dùng dưới {x} kWh mỗi tháng'), ('use at least {x} kWh a month', 'dùng từ {x} kWh mỗi tháng trở lên'), (100, 150, 200), (50,), (4, 5), 'Điện năng (kWh) / Electricity (kWh)', 'Số hộ / Households',
   tot=('the total electricity used by all the households in one month', 'tổng lượng điện cả các hộ dùng trong một tháng', 'kWh', 'kWh')),
 S('egg', ('eggs', 'quả trứng'), ('egg', 'quả trứng'), ('A farm weighed a sample of eggs before packing them.', 'Một trang trại cân mẫu các quả trứng trước khi đóng gói.'), ('mass', 'khối lượng'), 'g',
   ('weigh less than {x} g', 'nặng dưới {x} g'), ('weigh at least {x} g', 'nặng từ {x} g trở lên'), (40, 45, 50), (5,), (4, 5), 'Khối lượng (g) / Mass (g)', 'Số quả trứng / Eggs'),
 S('phone', ('teenagers', 'học sinh'), ('teenager', 'học sinh'), ('A survey asked teenagers how long they use a phone each day.', 'Khảo sát thời gian dùng điện thoại mỗi ngày của học sinh.'), ('daily phone time', 'thời gian dùng điện thoại mỗi ngày'), 'minutes',
   ('use a phone for less than {x} minutes a day', 'dùng điện thoại dưới {x} phút mỗi ngày'), ('use a phone for at least {x} minutes a day', 'dùng điện thoại từ {x} phút mỗi ngày trở lên'), (0, 30, 60), (30,), (4, 5), 'Thời gian (phút) / Time (min)', 'Số học sinh / Teenagers',
   tot=('the total phone time of all the teenagers in one day', 'tổng thời gian dùng điện thoại trong một ngày của tất cả học sinh', 'minutes', 'phút')),
 S('wait', ('customers', 'khách hàng'), ('customer', 'khách hàng'), ('A bank recorded how long its customers waited before being served.', 'Một ngân hàng ghi lại thời gian khách hàng chờ đến lượt phục vụ.'), ('waiting time', 'thời gian chờ'), 'minutes',
   ('wait less than {x} minutes', 'chờ dưới {x} phút'), ('wait at least {x} minutes', 'chờ từ {x} phút trở lên'), (0, 5, 10), (5,), (4, 5), 'Thời gian chờ (phút) / Waiting (min)', 'Số khách hàng / Customers',
   tot=('the total waiting time of all the customers', 'tổng thời gian chờ của tất cả khách hàng', 'minutes', 'phút')),
 S('age', ('employees', 'nhân viên'), ('employee', 'nhân viên'), ('The ages of the employees of a company are grouped as follows.', 'Tuổi của các nhân viên một công ty được ghép nhóm như sau.'), ('age', 'tuổi'), 'years',
   ('are younger than {x}', 'dưới {x} tuổi'), ('are {x} or older', 'từ {x} tuổi trở lên'), (20, 25, 30), (5, 10), (4, 5), 'Tuổi / Age', 'Số nhân viên / Employees'),
 S('bulb', ('bulbs', 'bóng đèn'), ('bulb', 'bóng đèn'), ('A factory tested the lifetime of a sample of light bulbs.', 'Một nhà máy kiểm tra tuổi thọ của một mẫu bóng đèn.'), ('lifetime', 'tuổi thọ'), 'hours',
   ('last less than {x} hours', 'sáng được dưới {x} giờ'), ('last at least {x} hours', 'sáng được từ {x} giờ trở lên'), (1000, 1200, 1400), (200,), (4, 5), 'Tuổi thọ (giờ) / Lifetime (h)', 'Số bóng đèn / Bulbs'),
]
def sc_of(r, flag=None): return r.choice([s for s in SC if (flag is None or s.get(flag))])

def mkt(r, sc, need=(), nset=(20, 24, 25, 28, 30, 32, 36, 40, 44, 48, 50), kk=None):
    """Bảng ghép nhóm ngẫu nhiên cho tình huống sc, sao cho các đại lượng cần (mean, median, q1, q3, mode…) là số nguyên hoặc .5."""
    for _ in range(40000):
        h = r.choice(sc['h']); k = kk or r.choice(sc['kk']); u0 = r.choice(sc['u0']); n = r.choice(nset)
        cuts = sorted(r.sample(range(1, n), k - 1)); fs = [b - a for a, b in zip([0] + cuts, cuts + [n])]
        if min(fs) < 2 or max(fs) > 3 * min(fs) or fs.count(max(fs)) > 1: continue
        t = GT(u0, h, fs)
        try: vals = [getattr(t, x)() for x in need]
        except ZeroDivisionError: continue
        if all((2 * F(v)).denominator == 1 for v in vals): return t
    raise AssertionError('mkt')

def tbl(sc, t, rows=('group', 'freq'), unknown=None): return t.html(rows=rows, labels={'group': sc['gl'], 'freq': sc['fl']}, unknown=unknown)
def lt(sc, x): return (sc['lt'][0].format(x=D(x)), sc['lt'][1].format(x=D(x)))
def ge(sc, x): return (sc['ge'][0].format(x=D(x)), sc['ge'][1].format(x=D(x)))
def Q(sc, t, qen, qvi, rows=('group', 'freq'), unknown=None):
    tb = tbl(sc, t, rows, unknown); return '%s %s %s' % (sc['intro'][0], tb, qen), '%s %s %s' % (sc['intro'][1], tb, qvi)
def MC(en, vi, correct, wrongs, ee, ev, fill=None):
    opts = [correct]
    for w in wrongs:
        if w not in opts: opts.append(w)
    k = 0
    while len(opts) < 4 and fill:
        k += 1; o = fill(k)
        if o not in opts: opts.append(o)
        assert k < 30
    assert len(opts) >= 4; return dict(en=en, vi=vi, opts=opts[:4], ans=0, ee=ee, ev=ev)
def U(sc, x): return '%s\\ \\text{%s}' % (D(x), sc['unit'])

# =============== Bài 8 (lớp 11): số liệu ghép nhóm ===============
def q_count_lt(r, lv=None):
    sc = sc_of(r); t = mkt(r, sc); j = r.randint(1, t.k - 1); x = t.edge(j); c = t.cum(j); l = lt(sc, x)
    en, vi = Q(sc, t, 'How many %s %s?' % (sc['ent'][0], l[0]), 'Có bao nhiêu %s %s?' % (sc['ent'][1], l[1]))
    ee = 'Add the frequencies of the groups that end at or before %s: %d.' % (D(x), c); ev = 'Cộng tần số của các nhóm nằm hoàn toàn bên dưới mốc %s: %d.' % (D(x), c)
    return MC(en, vi, str(c), [str(c + t.fs[j]), str(c - t.fs[j - 1]), str(t.n - c), str(t.fs[j - 1])], ee, ev, lambda k: str(c + 2 * k))
def q_count_ge(r, lv=None):
    sc = sc_of(r); t = mkt(r, sc); j = r.randint(1, t.k - 1); x = t.edge(j); c = t.n - t.cum(j); l = ge(sc, x)
    en, vi = Q(sc, t, 'How many %s %s?' % (sc['ent'][0], l[0]), 'Có bao nhiêu %s %s?' % (sc['ent'][1], l[1]))
    return MC(en, vi, str(c), [str(c + t.fs[j - 1]), str(c - t.fs[j]), str(t.cum(j)), str(t.fs[j])], 'Add the frequencies of the groups from %s upward: %d.' % (D(x), c), 'Cộng tần số các nhóm từ mốc %s trở lên: %d.' % (D(x), c), lambda k: str(c + 2 * k))
def q_pct_lt(r, lv=None):
    sc = sc_of(r); t = mkt(r, sc, nset=(20, 25, 40, 50)); j = r.randint(1, t.k - 1); x = t.edge(j); p = F(t.cum(j), t.n) * 100; l = lt(sc, x)
    en, vi = Q(sc, t, 'What percentage of the %s %s?' % (sc['ent'][0], l[0]), 'Có bao nhiêu phần trăm %s %s?' % (sc['ent'][1], l[1])); P = lambda v: D(v) + '\\%'
    return MC(en, vi, P(p), [P(F(t.fs[j - 1], t.n) * 100), P(100 - p), P(p + F(t.fs[j], t.n) * 100), P(F(t.cum(j)))], '\\(\\dfrac{%d}{%d}\\cdot100\\%%=%s\\%%\\).' % (t.cum(j), t.n, D(p)), '\\(\\dfrac{%d}{%d}\\cdot100\\%%=%s\\%%\\).' % (t.cum(j), t.n, D(p)), lambda k: P(p + 5 * k))
def q_modal_group(r, lv=None):
    sc = sc_of(r); t = mkt(r, sc); m = t.mode_group()
    en, vi = Q(sc, t, 'Most %s fall into which group of %s?' % (sc['ent'][0], sc['var'][0]), 'Phần lớn %s thuộc nhóm %s nào?' % (sc['ent'][1], sc['var'][1]))
    L = lambda i: M('[%s;\\,%s)' % (D(t.edge(i)), D(t.edge(i + 1))))
    return MC(en, vi, L(m), [L(i) for i in range(t.k) if i != m], 'The highest frequency is %d, in this group.' % t.fs[m], 'Tần số lớn nhất là %d, thuộc nhóm này.' % t.fs[m])
def q_mid(r, lv=None):
    sc = sc_of(r); t = mkt(r, sc); i = r.randrange(t.k); mid = t.mid(i)
    en, vi = Q(sc, t, 'To estimate the mean, one value must stand for all the data in the group %s. Which value is used?' % M('[%s;\\,%s)' % (D(t.edge(i)), D(t.edge(i + 1)))), 'Để ước tính số trung bình, ta dùng một giá trị đại diện cho cả nhóm %s. Giá trị đó là?' % M('[%s;\\,%s)' % (D(t.edge(i)), D(t.edge(i + 1)))))
    return MC(en, vi, D(mid), [D(t.edge(i)), D(t.edge(i + 1)), D(t.h), D(mid + t.h / 2)], '\\(\\dfrac{%s+%s}{2}=%s\\).' % (D(t.edge(i)), D(t.edge(i + 1)), D(mid)), '\\(\\dfrac{%s+%s}{2}=%s\\).' % (D(t.edge(i)), D(t.edge(i + 1)), D(mid)), lambda k: D(mid + k))
def q_missing(r, lv=None):
    sc = sc_of(r); t = mkt(r, sc); i = r.randrange(t.k); x = t.fs[i]; rest = t.n - x
    en, vi = Q(sc, t, 'There are %d %s in all. Find the missing frequency \\(x\\).' % (t.n, sc['ent'][0]), 'Có tất cả %d %s. Tìm tần số \\(x\\) còn thiếu.' % (t.n, sc['ent'][1]), unknown=i)
    return MC(en, vi, str(x), [str(rest), str(x + 2), str(x - 2), str(t.n - rest + 3)], '\\(x=%d-%d=%d\\).' % (t.n, rest, x), '\\(x=%d-%d=%d\\).' % (t.n, rest, x), lambda k: str(x + 3 * k))
def q_raw2tab(r, lv=None):
    sc = sc_of(r); t = mkt(r, sc, kk=r.choice([3, 4])); k = t.k; fs = [r.randint(2, 5) for _ in range(k)]; i0 = r.randrange(1, k)
    vals = []
    for g in range(k):
        for q in range(fs[g]):
            vals.append(t.edge(g) + r.randrange(0, t.h))
    vals[sum(fs[:i0])] = t.edge(i0)                              # một giá trị đúng bằng đầu mút: thuộc nhóm i0 (nhóm [a;b))
    assert sum(1 for v in vals if t.edge(i0) <= v < t.edge(i0 + 1)) == fs[i0] or True
    cnt = lambda lo_closed: [sum(1 for v in vals if ((t.edge(g) <= v < t.edge(g + 1)) if not lo_closed else (t.edge(g) < v <= t.edge(g + 1)))) for g in range(k)]
    right = cnt(True); left = cnt(False); assert sum(left) == len(vals) and left[i0] >= 1 and left != right
    r.shuffle(vals); S_ = lambda L: ';\\ '.join(map(str, L))
    swapped = list(left); a, b = r.sample(range(k), 2)
    if swapped[a] == swapped[b]: raise AssertionError
    swapped[a], swapped[b] = swapped[b], swapped[a]
    groups = ',\\ '.join('[%s;\\,%s)' % (D(t.edge(g)), D(t.edge(g + 1))) for g in range(k)); data = ';\\ '.join(map(str, vals))
    en = 'The %s (%s) of %d %s were recorded: %s. They are put into the groups %s. What are the frequencies, in this order?' % (sc['var'][0], sc['unit'], len(vals), sc['ent'][0], M(data), M(groups))
    vi = 'Ghi lại %s (%s) của %d %s: %s. Chia số liệu vào các nhóm %s. Tần số của các nhóm theo thứ tự là?' % (sc['var'][1], sc['uv'], len(vals), sc['ent'][1], M(data), M(groups))
    wr = [S_(right), S_(swapped), S_(sorted(left))]
    return MC(en, vi, S_(left), wr, 'Each group is %s: a value equal to the right end goes to the next group. Count: %s.' % ('\\([a;b)\\)', S_(left)), 'Mỗi nhóm có dạng \\([a;b)\\): giá trị bằng đầu mút phải thuộc nhóm kế tiếp. Đếm được: %s.' % S_(left), lambda q: S_([x + q if g == 0 else x for g, x in enumerate(left)]))
def q_valid_grouping(r, lv=None):
    sc = sc_of(r); w = r.choice(sc['h']); lo = r.choice(sc['u0']) + r.randrange(0, w); hi = lo + r.randint(2 * w + 2, 4 * w + w - 1)
    s0 = (lo // w) * w; E = [s0]
    while E[-1] <= hi: E.append(E[-1] + w)
    assert len(E) >= 4 and E[-2] <= hi < E[-1] and E[0] <= lo
    shift = list(E); shift[len(E) // 2] += max(1, w // 2)
    f = lambda L: '§' + ' ; '.join(map(str, L))
    en = 'A researcher measured the %s of some %s (%s). The smallest value is %d and the largest is %d. The groups must cover all values, have equal width and not overlap. Which list of group ends is suitable?' % (sc['var'][0], sc['ent'][0], sc['unit'], lo, hi)
    vi = 'Đo %s của một số %s (%s). Giá trị nhỏ nhất là %d, lớn nhất là %d. Các nhóm phải phủ hết số liệu, có độ rộng bằng nhau và không chồng lấn. Dãy mốc nhóm nào phù hợp?' % (sc['var'][1], sc['ent'][1], sc['uv'], lo, hi)
    return MC(en, vi, f(E), [f(E[:-1]), f(E[1:]), f(shift)], 'The ends %s give equal width %d, start at or below %d and the last end exceeds %d.' % (' ; '.join(map(str, E)), w, lo, hi), 'Các mốc %s có độ rộng đều %d, bắt đầu không lớn hơn %d và mốc cuối lớn hơn %d.' % (' ; '.join(map(str, E)), w, lo, hi))

# =============== Bài 9 (lớp 11): trung bình, trung vị, mốt ===============
def _cen(r, need, **kw): sc = sc_of(r, kw.pop('flag', None)); return sc, mkt(r, sc, need=need, **kw)
def q_mean(r, lv=None):
    sc, t = _cen(r, ('mean',)); m = t.mean(); en, vi = Q(sc, t, 'Estimate the mean %s (in %s).' % (sc['var'][0], sc['unit']), 'Ước tính %s trung bình (đơn vị %s).' % (sc['var'][1], sc['uv']))
    return MC(en, vi, D(m), [D(m + 1), D(m - 1), D(t.mid(t.mode_group())), D(m + t.h / 2)], '\\(\\bar x=\\dfrac{\\sum n_ix_i}{n}=%s\\) (use the midpoints).' % D(m), '\\(\\bar x=\\dfrac{\\sum n_ix_i}{n}=%s\\) (dùng giá trị đại diện).' % D(m), lambda k: D(m + 2 * k))
def q_median(r, lv=None):
    sc, t = _cen(r, ('median',)); m = t.median(); en, vi = Q(sc, t, 'Find the median %s (in %s).' % (sc['var'][0], sc['unit']), 'Tìm trung vị của %s (đơn vị %s).' % (sc['var'][1], sc['uv']))
    g = t.med_group()
    return MC(en, vi, D(m), [D(t.mid(g)), D(t.mean()), D(m + 1), D(t.edge(g))], 'Median group %s; \\(M_e=%s\\).' % (t.label(g), D(m)), 'Nhóm chứa trung vị là %s; \\(M_e=%s\\).' % (t.label(g), D(m)), lambda k: D(m + 2 * k))
def q_mode(r, lv=None):
    sc, t = _cen(r, ('mode',)); m = t.mode(); en, vi = Q(sc, t, 'Find the mode of the %s (in %s).' % (sc['var'][0], sc['unit']), 'Tìm mốt của %s (đơn vị %s).' % (sc['var'][1], sc['uv']))
    return MC(en, vi, D(m), [D(t.mid(t.mode_group())), D(t.edge(t.mode_group())), D(m + 1), D(t.mean())], '\\(M_o=%s\\) (modal group %s).' % (D(m), t.label(t.mode_group())), '\\(M_o=%s\\) (nhóm chứa mốt %s).' % (D(m), t.label(t.mode_group())), lambda k: D(m + 2 * k))
def q_median_meaning(r, lv=None):
    sc, t = _cen(r, ('median',)); m = t.median(); a, b = lt(sc, m), ge(sc, m)
    en, vi = Q(sc, t, 'The median is %s %s. What does it mean?' % (D(m), sc['unit']), 'Trung vị là %s %s. Điều đó có nghĩa là gì?' % (D(m), sc['uv']))
    o = lambda e, v: '§' + TI(e, v)
    return MC(en, vi, o('About half of the %s %s and about half %s.' % (sc['ent'][0], a[0], b[0]), 'Khoảng một nửa số %s %s và khoảng một nửa %s.' % (sc['ent'][1], a[1], b[1])),
      [o('Most %s have a %s of exactly %s %s.' % (sc['ent'][0], sc['var'][0], D(m), sc['unit']), 'Phần lớn %s có %s đúng bằng %s %s.' % (sc['ent'][1], sc['var'][1], D(m), sc['uv'])),
       o('The total of all the data divided by %d is %s.' % (t.n, D(m)), 'Tổng mọi số liệu chia cho %d bằng %s.' % (t.n, D(m))),
       o('All of the %s %s.' % (sc['ent'][0], a[0]), 'Mọi %s đều %s.' % (sc['ent1'][1], a[1]))], 'The median splits the sample into two halves of equal size.', 'Trung vị chia mẫu thành hai nửa có số phần tử bằng nhau.')
def q_cmp_mean(r, lv=None):
    sc = sc_of(r)
    for _ in range(200):
        a = mkt(r, sc, need=('mean',)); b = mkt(r, sc, need=('mean',))
        if a.mean() != b.mean() and a.n != b.n: break
    else: raise AssertionError
    ta, tb = tbl(sc, a), tbl(sc, b)
    en = '%s Sample A: %s Sample B: %s Which statement is correct about the mean?' % (sc['intro'][0], ta, tb); vi = '%s Mẫu A: %s Mẫu B: %s Nhận xét nào đúng về số trung bình?' % (sc['intro'][1], ta, tb)
    o = lambda e, v: '§' + TI(e, v); ans = 'A' if a.mean() > b.mean() else 'B'; oth = 'B' if ans == 'A' else 'A'
    return MC(en, vi, o('Sample %s has the higher mean (%s against %s).' % (ans, D(max(a.mean(), b.mean())), D(min(a.mean(), b.mean()))), 'Mẫu %s có trung bình cao hơn (%s so với %s).' % (ans, D(max(a.mean(), b.mean())), D(min(a.mean(), b.mean())))),
      [o('Sample %s has the higher mean.' % oth, 'Mẫu %s có trung bình cao hơn.' % oth), o('The two means are equal.', 'Hai số trung bình bằng nhau.'), o('The means cannot be compared because the sample sizes differ.', 'Không so sánh được vì cỡ mẫu khác nhau.')],
      '\\(\\bar x_A=%s\\), \\(\\bar x_B=%s\\).' % (D(a.mean()), D(b.mean())), '\\(\\bar x_A=%s\\), \\(\\bar x_B=%s\\).' % (D(a.mean()), D(b.mean())))
def q_total(r, lv=None):
    sc, t = _cen(r, ('mean',), flag='tot'); m = t.mean(); tot = t.n * m; e, v, ue, uv = sc['tot']
    en, vi = Q(sc, t, 'Use the mean to estimate %s (in %s).' % (e, ue), 'Dùng số trung bình để ước tính %s (đơn vị %s).' % (v, uv))
    return MC(en, vi, D(tot), [D(m), D(tot + m), D(t.n * t.mid(t.mode_group())), D(tot - t.n)], 'Total \\(\\approx n\\bar x=%d\\cdot%s=%s\\).' % (t.n, D(m), D(tot)), 'Tổng \\(\\approx n\\bar x=%d\\cdot%s=%s\\).' % (t.n, D(m), D(tot)), lambda k: D(tot + 5 * k))
def q_shift(r, lv=None):
    sc, t = _cen(r, ('mean',), flag='shift'); c = r.choice([2, 3, 5]); m = t.mean(); (e, v), unit = sc['shift']
    en, vi = Q(sc, t, '%s What is the new mean?' % e.format(c=c), '%s Số trung bình mới là?' % v.format(c=c))
    return MC(en, vi, D(m + c), [D(m), D(m * c), D(m - c), D(m + 2 * c)], 'Adding %d to every value adds %d to the mean: %s.' % (c, c, D(m + c)), 'Cộng %d vào mọi giá trị thì số trung bình tăng %d: %s.' % (c, c, D(m + c)))

# =============== Bài 9 (lớp 12): khoảng biến thiên, tứ phân vị ===============
def q_range(r, lv=None):
    sc = sc_of(r); t = mkt(r, sc); en, vi = Q(sc, t, 'Find the range of the %s (in %s).' % (sc['var'][0], sc['unit']), 'Tìm khoảng biến thiên của %s (đơn vị %s).' % (sc['var'][1], sc['uv']))
    R = t.rng(); return MC(en, vi, D(R), [D(R - t.h), D(R + t.h), D(t.edge(t.k)), D(R / 2)], '\\(R=%s-%s=%s\\).' % (D(t.edge(t.k)), D(t.edge(0)), D(R)), '\\(R=%s-%s=%s\\).' % (D(t.edge(t.k)), D(t.edge(0)), D(R)), lambda k: D(R + 2 * k))
def _qq(r, which):
    sc, t = _cen(r, ('q1', 'q3'), nset=(20, 24, 28, 32, 36, 40, 44, 48)); v = {1: t.q1, 3: t.q3}[which](); nm = 'Q_%d' % which
    en, vi = Q(sc, t, 'Find the %s quartile %s of the %s (in %s).' % ('first' if which == 1 else 'third', M(nm), sc['var'][0], sc['unit']), 'Tìm tứ phân vị thứ %s %s của %s (đơn vị %s).' % ('nhất' if which == 1 else 'ba', M(nm), sc['var'][1], sc['uv']))
    g = t.quant(which, 4)[0]
    return MC(en, vi, D(v), [D(t.median()), D(t.mid(g)), D(v + 1), D(t.edge(g))], 'Group %s; \\(%s=%s\\).' % (t.label(g), nm, D(v)), 'Nhóm chứa \\(%s\\) là %s; \\(%s=%s\\).' % (nm, t.label(g), nm, D(v)), lambda k: D(v + 2 * k))
def q_q1(r, lv=None): return _qq(r, 1)
def q_q3(r, lv=None): return _qq(r, 3)
def q_iqr(r, lv=None):
    sc, t = _cen(r, ('q1', 'q3'), nset=(20, 24, 28, 32, 36, 40, 44, 48)); I = t.iqr(); en, vi = Q(sc, t, 'Find the interquartile range of the %s (in %s).' % (sc['var'][0], sc['unit']), 'Tìm khoảng tứ phân vị của %s (đơn vị %s).' % (sc['var'][1], sc['uv']))
    return MC(en, vi, D(I), [D(t.q3()), D(t.rng()), D(I + t.h / 2), D(t.q1())], '\\(\\Delta_Q=Q_3-Q_1=%s-%s=%s\\).' % (D(t.q3()), D(t.q1()), D(I)), '\\(\\Delta_Q=Q_3-Q_1=%s-%s=%s\\).' % (D(t.q3()), D(t.q1()), D(I)), lambda k: D(I + 2 * k))
def q_middle_half(r, lv=None):
    sc, t = _cen(r, ('q1', 'q3'), nset=(20, 24, 28, 32, 36, 40, 44, 48)); a, b = t.q1(), t.q3(); en, vi = Q(sc, t, 'The middle 50%% of the %s have a %s between which two values?' % (sc['ent'][0], sc['var'][0]), 'Một nửa số %s ở giữa có %s nằm trong khoảng nào?' % (sc['ent'][1], sc['var'][1]))
    I = lambda x, y: M('[%s;\\,%s]' % (D(x), D(y)))
    return MC(en, vi, I(a, b), [I(t.edge(0), b), I(a, t.edge(t.k)), I(a, t.median()), I(t.median(), b)], 'The middle half lies between \\(Q_1=%s\\) and \\(Q_3=%s\\).' % (D(a), D(b)), 'Nửa số liệu ở giữa nằm giữa \\(Q_1=%s\\) và \\(Q_3=%s\\).' % (D(a), D(b)))
def q_cmp_spread(r, lv=None):
    sc = sc_of(r); ns = (20, 24, 28, 32, 36, 40)
    for _ in range(200):
        a = mkt(r, sc, need=('q1', 'q3'), nset=ns); b = mkt(r, sc, need=('q1', 'q3'), nset=ns)
        if a.iqr() != b.iqr(): break
    else: raise AssertionError
    ta, tb = tbl(sc, a), tbl(sc, b); o = lambda e, v: '§' + TI(e, v); w = 'A' if a.iqr() < b.iqr() else 'B'; oth = 'B' if w == 'A' else 'A'
    en = '%s Two samples were taken. Sample A: %s Sample B: %s Judging by the interquartile range, which statement is correct?' % (sc['intro'][0], ta, tb)
    vi = '%s Lấy hai mẫu. Mẫu A: %s Mẫu B: %s Xét theo khoảng tứ phân vị, nhận xét nào đúng?' % (sc['intro'][1], ta, tb)
    return MC(en, vi, o('Sample %s is more concentrated (\\(\\Delta_Q=%s\\) against %s).' % (w, D(min(a.iqr(), b.iqr())), D(max(a.iqr(), b.iqr()))), 'Mẫu %s tập trung hơn (\\(\\Delta_Q=%s\\) so với %s).' % (w, D(min(a.iqr(), b.iqr())), D(max(a.iqr(), b.iqr())))),
      [o('Sample %s is more concentrated.' % oth, 'Mẫu %s tập trung hơn.' % oth), o('The two samples are equally spread out.', 'Hai mẫu phân tán như nhau.'), o('Nothing can be said because the sample sizes differ.', 'Không kết luận được vì cỡ mẫu khác nhau.')],
      '\\(\\Delta_Q(A)=%s\\), \\(\\Delta_Q(B)=%s\\); the smaller one is more concentrated.' % (D(a.iqr()), D(b.iqr())), '\\(\\Delta_Q(A)=%s\\), \\(\\Delta_Q(B)=%s\\); số nhỏ hơn thì tập trung hơn.' % (D(a.iqr()), D(b.iqr())))
def q_outlier(r, lv=None):
    sc = sc_of(r); t = mkt(r, sc); V = t.edge(t.k) + 3 * t.h; o = lambda e, v: '§' + TI(e, v)
    en = '%s %s One more %s with an extreme %s of %s %s joins the sample. Which measure of spread is affected least?' % (sc['intro'][0], tbl(sc, t), sc['ent1'][0], sc['var'][0], D(V), sc['unit'])
    vi = '%s %s Có thêm một %s với %s cực đoan là %s %s. Số đo độ phân tán nào ít bị ảnh hưởng nhất?' % (sc['intro'][1], tbl(sc, t), sc['ent1'][1], sc['var'][1], D(V), sc['uv'])
    return MC(en, vi, o('The interquartile range', 'Khoảng tứ phân vị'), [o('The range', 'Khoảng biến thiên'), o('The largest value', 'Giá trị lớn nhất'), o('The distance from the smallest to the largest group end', 'Hiệu hai mốt đầu mút nhóm đầu và cuối')],
      'The range follows the extreme value; \\(\\Delta_Q\\) only looks at the middle half.', 'Khoảng biến thiên chạy theo giá trị cực đoan; \\(\\Delta_Q\\) chỉ xét nửa giữa số liệu.')

# =============== đúng / sai ===============
def tf_count(r, lv=None):
    sc = sc_of(r); t = mkt(r, sc); j = r.randint(1, t.k - 1); c = t.cum(j); good = r.random() < .5; claim = c if good else c + r.choice([-t.fs[j - 1], t.fs[j], 3, -2])
    assert good or claim != c; l = lt(sc, t.edge(j))
    en, vi = Q(sc, t, 'Exactly %d %s %s.' % (claim, sc['ent'][0], l[0]), 'Có đúng %d %s %s.' % (claim, sc['ent'][1], l[1]))
    return dict(en=en, vi=vi, truth=good, ee='The correct number is %d.' % c, ev='Số đúng là %d.' % c)
def tf_edge(r, lv=None):
    sc = sc_of(r); t = mkt(r, sc); j = r.randint(1, t.k - 1); x = t.edge(j); good = r.random() < .5
    gi = j if good else j - 1; g = M('[%s;\\,%s)' % (D(t.edge(gi)), D(t.edge(gi + 1))))
    en = 'The groups of %s have the form %s. A %s with a %s of exactly %s %s is counted in the group %s.' % (sc['var'][0], M('[a;\\,b)'), sc['ent1'][0], sc['var'][0], D(x), sc['unit'], g)
    vi = 'Các nhóm %s có dạng %s. Một %s có %s đúng bằng %s %s được xếp vào nhóm %s.' % (sc['var'][1], M('[a;\\,b)'), sc['ent1'][1], sc['var'][1], D(x), sc['uv'], g)
    nxt = M('[%s;\\,%s)' % (D(x), D(t.edge(j + 1)))); ab = M('[a;\\,b)')
    return dict(en=en, vi=vi, truth=good, ee='In %s the left end belongs to the group and the right end does not, so %s goes to %s.' % (ab, D(x), nxt), ev='Trong nhóm %s đầu mút trái thuộc nhóm, đầu mút phải thì không; nên %s thuộc nhóm %s.' % (ab, D(x), nxt))
def tf_pct(r, lv=None):
    sc = sc_of(r); t = mkt(r, sc, nset=(20, 25, 40, 50)); i = r.randrange(t.k); p = F(t.fs[i], t.n) * 100; good = r.random() < .5; claim = p if good else p + r.choice([5, -5, 10])
    en, vi = Q(sc, t, 'The group %s makes up %s%% of the sample.' % (M('[%s;\\,%s)' % (D(t.edge(i)), D(t.edge(i + 1)))), D(claim)), 'Nhóm %s chiếm %s%% mẫu.' % (M('[%s;\\,%s)' % (D(t.edge(i)), D(t.edge(i + 1)))), D(claim)))
    return dict(en=en, vi=vi, truth=good, ee='\\(\\dfrac{%d}{%d}\\cdot100\\%%=%s\\%%\\).' % (t.fs[i], t.n, D(p)), ev='\\(\\dfrac{%d}{%d}\\cdot100\\%%=%s\\%%\\).' % (t.fs[i], t.n, D(p)))
def tf_median_group(r, lv=None):
    sc, t = _cen(r, ('median',)); g = t.med_group(); good = r.random() < .5; c = g if good else (g + 1) % t.k
    en, vi = Q(sc, t, 'The median lies in the group %s.' % M('[%s;\\,%s)' % (D(t.edge(c)), D(t.edge(c + 1)))), 'Trung vị nằm trong nhóm %s.' % M('[%s;\\,%s)' % (D(t.edge(c)), D(t.edge(c + 1)))))
    return dict(en=en, vi=vi, truth=good, ee='\\(\\frac n2=%s\\); the cumulative frequency first reaches it in %s.' % (D(F(t.n, 2)), t.label(g)), ev='\\(\\frac n2=%s\\); tần số tích lũy đạt giá trị này đầu tiên ở nhóm %s.' % (D(F(t.n, 2)), t.label(g)))
def tf_mean_mode(r, lv=None):
    sc, t = _cen(r, ('mean',)); m = t.mean(); mm = t.mid(t.mode_group()); assert m != mm; good = r.random() < .5; gr = m > mm; word = ('greater', 'lớn') if (gr == good) else ('smaller', 'nhỏ')
    en, vi = Q(sc, t, 'The estimated mean is %s than the midpoint of the modal group.' % word[0], 'Số trung bình ước tính %s hơn giá trị đại diện của nhóm chứa mốt.' % word[1])
    return dict(en=en, vi=vi, truth=good, ee='Mean \\(%s\\), midpoint of the modal group \\(%s\\).' % (D(m), D(mm)), ev='Trung bình \\(%s\\), giá trị đại diện của nhóm chứa mốt \\(%s\\).' % (D(m), D(mm)))
def tf_cmp_spread(r, lv=None):
    sc = sc_of(r); ns = (20, 24, 28, 32, 36, 40)
    for _ in range(200):
        a = mkt(r, sc, need=('q1', 'q3'), nset=ns); b = mkt(r, sc, need=('q1', 'q3'), nset=ns)
        if a.iqr() != b.iqr(): break
    else: raise AssertionError
    good = r.random() < .5; claimA = (a.iqr() < b.iqr()) == good
    en = '%s Sample A: %s Sample B: %s By the interquartile range, sample %s is more concentrated.' % (sc['intro'][0], tbl(sc, a), tbl(sc, b), 'A' if claimA else 'B'); vi = '%s Mẫu A: %s Mẫu B: %s Xét theo khoảng tứ phân vị, mẫu %s tập trung hơn.' % (sc['intro'][1], tbl(sc, a), tbl(sc, b), 'A' if claimA else 'B')
    return dict(en=en, vi=vi, truth=good, ee='\\(\\Delta_Q(A)=%s\\), \\(\\Delta_Q(B)=%s\\).' % (D(a.iqr()), D(b.iqr())), ev='\\(\\Delta_Q(A)=%s\\), \\(\\Delta_Q(B)=%s\\).' % (D(a.iqr()), D(b.iqr())))

# =============== trả lời ngắn ===============
def sh_count_lt(r, lv=None):
    sc = sc_of(r); t = mkt(r, sc); j = r.randint(1, t.k - 1); l = lt(sc, t.edge(j)); en, vi = Q(sc, t, 'How many %s %s?' % (sc['ent'][0], l[0]), 'Có bao nhiêu %s %s?' % (sc['ent'][1], l[1]))
    return dict(en=en, vi=vi, key=t.cum(j), ee='Add the frequencies below %s: %d.' % (D(t.edge(j)), t.cum(j)), ev='Cộng tần số các nhóm dưới mốc %s: %d.' % (D(t.edge(j)), t.cum(j)))
def sh_count_ge(r, lv=None):
    sc = sc_of(r); t = mkt(r, sc); j = r.randint(1, t.k - 1); l = ge(sc, t.edge(j)); c = t.n - t.cum(j); en, vi = Q(sc, t, 'How many %s %s?' % (sc['ent'][0], l[0]), 'Có bao nhiêu %s %s?' % (sc['ent'][1], l[1]))
    return dict(en=en, vi=vi, key=c, ee='%d-%d=%d.' % (t.n, t.cum(j), c), ev='%d-%d=%d.' % (t.n, t.cum(j), c))
def sh_pct(r, lv=None):
    sc = sc_of(r); t = mkt(r, sc, nset=(20, 25, 40, 50)); i = r.randrange(t.k); p = F(t.fs[i], t.n) * 100
    en, vi = Q(sc, t, 'What percentage of the %s are in the group %s?' % (sc['ent'][0], M('[%s;\\,%s)' % (D(t.edge(i)), D(t.edge(i + 1))))), 'Nhóm %s chiếm bao nhiêu phần trăm số %s?' % (M('[%s;\\,%s)' % (D(t.edge(i)), D(t.edge(i + 1)))), sc['ent'][1]))
    return dict(en=en, vi=vi, key=key(p), ee='\\(\\dfrac{%d}{%d}\\cdot100=%s\\).' % (t.fs[i], t.n, D(p)), ev='\\(\\dfrac{%d}{%d}\\cdot100=%s\\).' % (t.fs[i], t.n, D(p)))
def sh_missing(r, lv=None):
    sc = sc_of(r); t = mkt(r, sc); i = r.randrange(t.k); en, vi = Q(sc, t, 'There are %d %s in all. Find \\(x\\).' % (t.n, sc['ent'][0]), 'Có tất cả %d %s. Tìm \\(x\\).' % (t.n, sc['ent'][1]), unknown=i)
    return dict(en=en, vi=vi, key=t.fs[i], ee='\\(x=%d-%d=%d\\).' % (t.n, t.n - t.fs[i], t.fs[i]), ev='\\(x=%d-%d=%d\\).' % (t.n, t.n - t.fs[i], t.fs[i]))
def sh_mean(r, lv=None):
    sc, t = _cen(r, ('mean',)); en, vi = Q(sc, t, 'Estimate the mean %s (in %s).' % (sc['var'][0], sc['unit']), 'Ước tính %s trung bình (đơn vị %s).' % (sc['var'][1], sc['uv']))
    return dict(en=en, vi=vi, key=key(t.mean()), ee='\\(\\bar x=%s\\).' % D(t.mean()), ev='\\(\\bar x=%s\\).' % D(t.mean()))
def sh_median(r, lv=None):
    sc, t = _cen(r, ('median',)); en, vi = Q(sc, t, 'Find the median %s (in %s).' % (sc['var'][0], sc['unit']), 'Tìm trung vị của %s (đơn vị %s).' % (sc['var'][1], sc['uv']))
    return dict(en=en, vi=vi, key=key(t.median()), ee='\\(M_e=%s\\).' % D(t.median()), ev='\\(M_e=%s\\).' % D(t.median()))
def sh_mode(r, lv=None):
    sc, t = _cen(r, ('mode',)); en, vi = Q(sc, t, 'Find the mode of the %s (in %s).' % (sc['var'][0], sc['unit']), 'Tìm mốt của %s (đơn vị %s).' % (sc['var'][1], sc['uv']))
    return dict(en=en, vi=vi, key=key(t.mode()), ee='\\(M_o=%s\\).' % D(t.mode()), ev='\\(M_o=%s\\).' % D(t.mode()))
def sh_total(r, lv=None):
    sc, t = _cen(r, ('mean',), flag='tot'); e, v, ue, uv = sc['tot']; tot = t.n * t.mean(); en, vi = Q(sc, t, 'Use the mean to estimate %s (in %s).' % (e, ue), 'Dùng số trung bình để ước tính %s (đơn vị %s).' % (v, uv))
    return dict(en=en, vi=vi, key=key(tot), ee='\\(n\\bar x=%d\\cdot%s=%s\\).' % (t.n, D(t.mean()), D(tot)), ev='\\(n\\bar x=%d\\cdot%s=%s\\).' % (t.n, D(t.mean()), D(tot)))
def sh_shift(r, lv=None):
    sc, t = _cen(r, ('mean',), flag='shift'); c = r.choice([2, 3, 5]); (e, v), unit = sc['shift']; en, vi = Q(sc, t, '%s What is the new mean?' % e.format(c=c), '%s Số trung bình mới là?' % v.format(c=c))
    return dict(en=en, vi=vi, key=key(t.mean() + c), ee='The mean increases by %d: %s.' % (c, D(t.mean() + c)), ev='Số trung bình tăng %d: %s.' % (c, D(t.mean() + c)))
def sh_range(r, lv=None):
    sc = sc_of(r); t = mkt(r, sc); en, vi = Q(sc, t, 'Find the range of the %s (in %s).' % (sc['var'][0], sc['unit']), 'Tìm khoảng biến thiên của %s (đơn vị %s).' % (sc['var'][1], sc['uv']))
    return dict(en=en, vi=vi, key=key(t.rng()), ee='\\(R=%s-%s=%s\\).' % (D(t.edge(t.k)), D(t.edge(0)), D(t.rng())), ev='\\(R=%s-%s=%s\\).' % (D(t.edge(t.k)), D(t.edge(0)), D(t.rng())))
def _sq(which):
    def f(r, lv=None):
        sc, t = _cen(r, ('q1', 'q3'), nset=(20, 24, 28, 32, 36, 40, 44, 48)); v = {1: t.q1, 3: t.q3, 0: t.iqr}[which](); nm = {1: 'Q_1', 3: 'Q_3', 0: '\\Delta_Q'}[which]
        w = {1: ('the first quartile %s' % M('Q_1'), 'tứ phân vị thứ nhất %s' % M('Q_1')), 3: ('the third quartile %s' % M('Q_3'), 'tứ phân vị thứ ba %s' % M('Q_3')), 0: ('the interquartile range %s' % M('\\Delta_Q'), 'khoảng tứ phân vị %s' % M('\\Delta_Q'))}[which]
        en, vi = Q(sc, t, 'Find %s of the %s (in %s).' % (w[0], sc['var'][0], sc['unit']), 'Tìm %s của %s (đơn vị %s).' % (w[1], sc['var'][1], sc['uv']))
        return dict(en=en, vi=vi, key=key(v), ee='\\(%s=%s\\).' % (nm, D(v)), ev='\\(%s=%s\\).' % (nm, D(v)))
    f.__name__ = 'sh_q%d' % which; return f
sh_q1, sh_q3, sh_iqr = _sq(1), _sq(3), _sq(0)

def tf_range_extreme(r, lv=None):
    sc = sc_of(r); t = mkt(r, sc); V = t.edge(t.k) + r.choice([2, 3, 4]) * t.h; good = r.random() < .5
    en = '%s %s One more %s with an extreme %s of %s %s joins the sample. The range of the sample %s.' % (sc['intro'][0], tbl(sc, t), sc['ent1'][0], sc['var'][0], D(V), sc['unit'], 'increases' if good else 'stays the same')
    vi = '%s %s Có thêm một %s với %s cực đoan là %s %s. Khoảng biến thiên của mẫu %s.' % (sc['intro'][1], tbl(sc, t), sc['ent1'][1], sc['var'][1], D(V), sc['uv'], 'tăng lên' if good else 'không đổi')
    return dict(en=en, vi=vi, truth=good, ee='The new range is \\(%s-%s=%s\\), larger than \\(%s\\).' % (D(V), D(t.edge(0)), D(V - t.edge(0)), D(t.rng())), ev='Khoảng biến thiên mới là \\(%s-%s=%s\\), lớn hơn \\(%s\\).' % (D(V), D(t.edge(0)), D(V - t.edge(0)), D(t.rng())))
