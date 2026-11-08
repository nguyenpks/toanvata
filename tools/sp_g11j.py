# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 11 – Bài 28 (biến cố hợp, giao, độc lập), Bài 29 (công thức cộng xác suất),
Bài 30 (công thức nhân xác suất cho hai biến cố độc lập). Tính chính xác bằng Fraction, hiển thị thập phân khi hữu hạn."""
import math, itertools
from fractions import Fraction as F
from mb_selfpractice import pick_opts, fr
from sp_g11f import TT


def dec(x):
    x = F(x); d = x.denominator
    while d % 2 == 0: d //= 2
    while d % 5 == 0: d //= 5
    if d != 1: return fr(x)
    s = ('%.6f' % float(x)).rstrip('0').rstrip('.')
    return s.replace('.', '{,}')
def decs(xs): return [dec(x) for x in xs]
def setstr(S): return '\\{%s\\}' % ';\\,'.join(map(str, sorted(S))) if S else '\\varnothing'
PS = [F(k, 10) for k in (5, 6, 7, 8, 9)] + [F(3, 4), F(1, 4), F(2, 5)]

# ================= Bài 28 =================
def _die_events(r):
    kinds = [('even', 'chẵn', {2, 4, 6}), ('odd', 'lẻ', {1, 3, 5}), ('prime', 'nguyên tố', {2, 3, 5})]
    a = r.choice(kinds); k = r.randint(2, 5); b = ('at least %d' % k, 'không nhỏ hơn %d' % k, set(range(k, 7)))
    return a, b


def e_union(r, lv):
    (ae, av, A), (be, bv, B) = _die_events(r)
    return dict(en='A die is rolled. \\(A\\): "the number is %s", \\(B\\): "the number is %s". Then \\(A\\cup B=\\)…' % (ae, be), vi='Gieo một con xúc xắc. \\(A\\): "số chấm là số %s", \\(B\\): "số chấm %s". Khi đó \\(A\\cup B=\\)…' % (av, bv),
      opts=pick_opts(r, setstr(A | B), [setstr(A & B), setstr(A), setstr(B), setstr(set(range(1, 7)) - (A | B)) if A | B != set(range(1, 7)) else setstr({1, 2})]), ans=0,
      ee='Union: outcomes in \\(A\\) or in \\(B\\).', ev='\\(A=%s\\), \\(B=%s\\); \\(A\\cup B\\) gồm các kết quả thuộc \\(A\\) hoặc \\(B\\).' % (setstr(A), setstr(B)))


def e_inter(r, lv):
    (ae, av, A), (be, bv, B) = _die_events(r)
    if not (A & B) or A & B == A or A & B == B: raise AssertionError
    return dict(en='A die is rolled. \\(A\\): "the number is %s", \\(B\\): "the number is %s". Then \\(A\\cap B=\\)…' % (ae, be), vi='Gieo một con xúc xắc. \\(A\\): "số chấm là số %s", \\(B\\): "số chấm %s". Khi đó \\(A\\cap B\\) (hay \\(AB\\)) \\(=\\)…' % (av, bv),
      opts=pick_opts(r, setstr(A & B), [setstr(A | B), setstr(A), setstr(B), setstr(A - B)]), ans=0, ee='Intersection: outcomes in both.', ev='\\(A=%s\\), \\(B=%s\\); \\(AB\\) gồm các kết quả thuộc cả hai.' % (setstr(A), setstr(B)))


def e_indep(r, lv):
    p, q = r.sample(PS, 2)
    return dict(en='\\(A\\), \\(B\\) are independent, \\(P(A)=%s\\), \\(P(B)=%s\\). Then \\(P(AB)=\\)…' % (dec(p), dec(q)), vi='Hai biến cố \\(A\\), \\(B\\) độc lập, \\(P(A)=%s\\), \\(P(B)=%s\\). Khi đó \\(P(AB)=\\)…' % (dec(p), dec(q)),
      opts=pick_opts(r, dec(p * q), decs([p + q - p * q, (1 - p) * (1 - q), p * (1 - q), min(p, q), abs(p - q)])), ans=0, ee='Independent: \\(P(AB)=P(A)P(B)\\).', ev='\\(A\\), \\(B\\) độc lập nên \\(P(AB)=P(A)\\cdot P(B)=%s\\cdot%s\\).' % (dec(p), dec(q)))


def e_indep2(r, lv):
    p, q = r.sample(PS, 2)
    return dict(en='\\(A\\), \\(B\\) are independent, \\(P(A)=%s\\), \\(P(B)=%s\\). Then \\(P(\\overline AB)=\\)…' % (dec(p), dec(q)), vi='Hai biến cố \\(A\\), \\(B\\) độc lập, \\(P(A)=%s\\), \\(P(B)=%s\\). Khi đó \\(P(\\overline AB)=\\)…' % (dec(p), dec(q)),
      opts=pick_opts(r, dec((1 - p) * q), decs([p * q, p * (1 - q), (1 - p) * (1 - q), 1 - p * q, q - p if q > p else p - q])), ans=0,
      ee='\\(\\overline A\\) and \\(B\\) are also independent.', ev='\\(\\overline A\\) và \\(B\\) cũng độc lập: \\(P(\\overline AB)=(1-%s)\\cdot%s\\).' % (dec(p), dec(q)))


def e_boxes(r, lv):
    a, b, c, d = r.randint(2, 7), r.randint(2, 7), r.randint(2, 7), r.randint(2, 7)
    p = F(a, a + b) * F(c, c + d)
    return dict(en='Box I has %d red and %d white balls; box II has %d red and %d white. One ball is drawn from each box. P(both red) =…' % (a, b, c, d), vi='Hộp I có %d cầu đỏ, %d cầu trắng; hộp II có %d cầu đỏ, %d cầu trắng. Lấy ngẫu nhiên mỗi hộp một quả. Xác suất lấy được hai quả đỏ là…' % (a, b, c, d),
      opts=pick_opts(r, fr(p), [fr(F(a + c, a + b + c + d)), fr(F(a, a + b) + F(c, c + d) - p), fr(F(C2(a + c), C2(a + b + c + d))), fr(F(a * c, (a + b + c + d) ** 2))]), ans=0,
      ee='The two draws are independent.', ev='Hai lần lấy độc lập: \\(\\dfrac{%d}{%d}\\cdot\\dfrac{%d}{%d}=%s\\).' % (a, a + b, c, c + d, fr(p)))
def C2(n): return math.comb(n, 2)


def e_excl(r, lv):
    k = r.randint(2, 5)
    pairs = [(('"even"', '"odd"'), ('"chẵn"', '"lẻ"'), True), (('"prime"', '"even"'), ('"nguyên tố"', '"chẵn"'), False), (('"at least %d"' % (k + 1), '"less than %d"' % k), ('"không nhỏ hơn %d"' % (k + 1), '"nhỏ hơn %d"' % k), True),
             (('"at most %d"' % k, '"at least %d"' % k), ('"không lớn hơn %d"' % k, '"không nhỏ hơn %d"' % k), False)]
    (e1, e2), (v1, v2), ok = r.choice(pairs)
    return dict(en='A die is rolled. Are the events %s and %s mutually exclusive?' % (e1, e2), vi='Gieo một con xúc xắc. Hai biến cố %s và %s có xung khắc không?' % (v1, v2),
      opts=[TT('yes, they cannot occur together', 'có, chúng không thể cùng xảy ra'), TT('no, they can occur together', 'không, chúng có thể cùng xảy ra'), TT('they are complementary only if both are certain', 'chỉ khi cả hai chắc chắn'), TT('it depends on the number of rolls', 'tùy số lần gieo')] if ok else
           [TT('no, they can occur together', 'không, chúng có thể cùng xảy ra'), TT('yes, they cannot occur together', 'có, chúng không thể cùng xảy ra'), TT('they are complementary only if both are certain', 'chỉ khi cả hai chắc chắn'), TT('it depends on the number of rolls', 'tùy số lần gieo')], ans=0,
      ee='Check whether \\(A\\cap B=\\varnothing\\).', ev='Xét xem \\(A\\cap B\\) có rỗng không.')


def e_words(r, lv):
    n = r.choice([2, 3])
    opts_en = [('"at least one hits"', '"có ít nhất một người bắn trúng"'), ('"all hit"', '"tất cả đều bắn trúng"'), ('"exactly one hits"', '"có đúng một người bắn trúng"'), ('"nobody hits"', '"không ai bắn trúng"')]
    kind = r.choice(['union', 'inter'])
    ok = opts_en[0] if kind == 'union' else opts_en[1]
    sym = ('\\cup ' if kind == 'union' else '\\cap ').join('A_%d' % i for i in range(1, n + 1))  # T-002: thiếu dấu cách tạo lệnh lạ \capA
    return dict(en='%d shooters fire once; \\(A_i\\): "shooter %s hits". The event \\(%s\\) is…' % (n, 'i', sym), vi='%d xạ thủ mỗi người bắn một phát; \\(A_i\\): "xạ thủ thứ \\(i\\) bắn trúng". Biến cố \\(%s\\) là…' % (n, sym),
      opts=[TT(ok[0], ok[1])] + [TT(*o) for o in opts_en if o != ok], ans=0, ee='Union = at least one; intersection = all.', ev='Hợp: ít nhất một biến cố xảy ra; giao: tất cả cùng xảy ra.')


M28S11 = [e_union, e_inter, e_indep, e_indep2, e_boxes, e_excl, e_words, e_indep]

# ================= Bài 29 =================
def c_add(r, lv):
    p, q = r.sample(PS, 2); pq = r.choice([F(k, 10) for k in range(1, 5)])
    if pq > min(p, q) or p + q - pq > 1: raise AssertionError
    return dict(en='\\(P(A)=%s\\), \\(P(B)=%s\\), \\(P(AB)=%s\\). Then \\(P(A\\cup B)=\\)…' % (dec(p), dec(q), dec(pq)), vi='Cho \\(P(A)=%s\\), \\(P(B)=%s\\), \\(P(AB)=%s\\). Khi đó \\(P(A\\cup B)=\\)…' % (dec(p), dec(q), dec(pq)),
      opts=pick_opts(r, dec(p + q - pq), decs([p + q, p + q - 2 * pq, p * q, 1 - pq, p + q + pq])), ans=0, ee='\\(P(A\\cup B)=P(A)+P(B)-P(AB)\\).', ev='Công thức cộng: \\(%s+%s-%s\\).' % (dec(p), dec(q), dec(pq)))


def c_survey(r, lv):
    n = r.choice([40, 50, 30, 45]); a, b = r.randint(n // 4, n // 2), r.randint(n // 4, n // 2); c = r.randint(3, min(a, b) - 2)
    return dict(en='In a class of %d students, %d play football, %d play badminton and %d play both. A student is chosen at random. P(plays at least one of the two) =…' % (n, a, b, c), vi='Một lớp có %d học sinh, %d em chơi bóng đá, %d em chơi cầu lông, %d em chơi cả hai. Chọn ngẫu nhiên một em. Xác suất em đó chơi ít nhất một trong hai môn là…' % (n, a, b, c),
      opts=pick_opts(r, fr(F(a + b - c, n)), [fr(F(a + b, n)) if a + b <= n else fr(F(a + b - 2 * c, n)), fr(F(c, n)), fr(F(a + b - 2 * c, n)), fr(F(n - a - b + c, n))]), ans=0,
      ee='\\(\\dfrac{%d+%d-%d}{%d}\\).' % (a, b, c, n), ev='\\(P(A\\cup B)=\\dfrac{%d}{%d}+\\dfrac{%d}{%d}-\\dfrac{%d}{%d}=%s\\).' % (a, n, b, n, c, n, fr(F(a + b - c, n))))


def c_excl(r, lv):
    p, q = r.sample([F(k, 10) for k in range(1, 6)], 2)
    return dict(en='\\(A\\), \\(B\\) are mutually exclusive, \\(P(A)=%s\\), \\(P(B)=%s\\). Then \\(P(A\\cup B)=\\)…' % (dec(p), dec(q)), vi='Hai biến cố \\(A\\), \\(B\\) xung khắc, \\(P(A)=%s\\), \\(P(B)=%s\\). Khi đó \\(P(A\\cup B)=\\)…' % (dec(p), dec(q)),
      opts=pick_opts(r, dec(p + q), decs([p * q, p + q - p * q, abs(p - q), 1 - p - q])), ans=0, ee='\\(P(AB)=0\\).', ev='Xung khắc nên \\(P(AB)=0\\): \\(P(A\\cup B)=%s+%s\\).' % (dec(p), dec(q)))


def c_inter(r, lv):
    p, q = r.sample(PS, 2); u = r.choice([F(k, 10) for k in range(int(max(p, q) * 10) + 1, 11)]) if max(p, q) < 1 else F(1)
    pq = p + q - u
    if pq < 0 or pq > min(p, q): raise AssertionError
    return dict(en='\\(P(A)=%s\\), \\(P(B)=%s\\), \\(P(A\\cup B)=%s\\). Then \\(P(AB)=\\)…' % (dec(p), dec(q), dec(u)), vi='Cho \\(P(A)=%s\\), \\(P(B)=%s\\), \\(P(A\\cup B)=%s\\). Khi đó \\(P(AB)=\\)…' % (dec(p), dec(q), dec(u)),
      opts=pick_opts(r, dec(pq), decs([p * q, u - p, u - q, p + q + u - 1 if p + q + u > 1 else 1 - u, 1 - pq])), ans=0, ee='\\(P(AB)=P(A)+P(B)-P(A\\cup B)\\).', ev='\\(P(AB)=%s+%s-%s\\).' % (dec(p), dec(q), dec(u)))


def c_div(r, lv):
    N = r.choice([20, 30, 50, 60, 100]); a, b = r.choice([(2, 3), (2, 5), (3, 5), (3, 4)])
    k = sum(1 for x in range(1, N + 1) if x % a == 0 or x % b == 0)
    return dict(en='A number is chosen at random from 1 to %d. P(divisible by %d or by %d) =…' % (N, a, b), vi='Chọn ngẫu nhiên một số từ 1 đến %d. Xác suất số đó chia hết cho %d hoặc cho %d là…' % (N, a, b),
      opts=pick_opts(r, fr(F(k, N)), [fr(F(N // a + N // b, N)), fr(F(N // (a * b), N)), fr(F(k + 1, N)), fr(F(N // a, N))]), ans=0,
      ee='\\(%d+%d-%d=%d\\) numbers.' % (N // a, N // b, N // (a * b // math.gcd(a, b)), k), ev='Công thức cộng: \\(%d+%d-%d=%d\\) số (trừ các số chia hết cho cả hai).' % (N // a, N // b, N // (a * b // math.gcd(a, b)), k))


def c_none(r, lv):
    n = r.choice([40, 50, 60]); a, b = r.randint(n // 4, n // 2), r.randint(n // 5, n // 3); c = r.randint(2, min(a, b) - 1)
    return dict(en='In a survey of %d people, %d read newspaper X, %d read Y, %d read both. P(a random person reads neither) =…' % (n, a, b, c), vi='Khảo sát %d người: %d người đọc báo X, %d người đọc báo Y, %d người đọc cả hai. Chọn ngẫu nhiên một người. Xác suất người đó không đọc báo nào là…' % (n, a, b, c),
      opts=pick_opts(r, fr(F(n - a - b + c, n)), [fr(F(a + b - c, n)), fr(F(n - a - b, n)) if n > a + b else fr(F(c, n)), fr(F(c, n)), fr(F(n - a, n))]), ans=0,
      ee='\\(1-P(X\\cup Y)\\).', ev='\\(1-P(X\\cup Y)=1-\\dfrac{%d+%d-%d}{%d}\\).' % (a, b, c, n))


def c_six(r, lv):
    n = r.choice([2, 3]); m = r.randint(1, 6)
    p = 1 - F(5, 6) ** n
    return dict(en='%d dice are rolled. P(at least one shows %d) =…' % (n, m), vi='Gieo %d con xúc xắc. Xác suất có ít nhất một con xuất hiện mặt %d chấm là…' % (n, m),
      opts=pick_opts(r, fr(p), [fr(F(n, 6)), fr(F(1, 6) ** n), fr(F(5, 6) ** n), fr(p + F(1, 36))]), ans=0, ee='Complement: no %d at all.' % m, ev='Biến cố đối "không con nào ra mặt %d": \\(\\left(\\frac56\\right)^%d\\); lấy 1 trừ đi.' % (m, n))


M29S11 = [c_add, c_survey, c_excl, c_inter, c_div, c_none, c_six, c_add]

# ================= Bài 30 =================
def m_two(r, lv):
    p, q = r.sample(PS[:5], 2)
    return dict(en='Two shooters hit the target independently with probabilities %s and %s. P(both hit) =…' % (dec(p), dec(q)), vi='Hai xạ thủ bắn độc lập, xác suất bắn trúng lần lượt là %s và %s. Xác suất cả hai cùng trúng là…' % (dec(p), dec(q)),
      opts=pick_opts(r, dec(p * q), decs([p + q - p * q, (p + q) / 2, (1 - p) * (1 - q), p * (1 - q) + q * (1 - p)])), ans=0, ee='\\(P(AB)=P(A)P(B)\\).', ev='Độc lập: \\(%s\\cdot%s\\).' % (dec(p), dec(q)))


def m_least(r, lv):
    p, q = r.sample(PS[:5], 2)
    return dict(en='Two shooters hit independently with probabilities %s and %s. P(the target is hit at least once) =…' % (dec(p), dec(q)), vi='Hai xạ thủ bắn độc lập với xác suất trúng %s và %s. Xác suất mục tiêu bị trúng ít nhất một phát là…' % (dec(p), dec(q)),
      opts=pick_opts(r, dec(1 - (1 - p) * (1 - q)), decs([p * q, p + q, (1 - p) * (1 - q), p * (1 - q) + q * (1 - p)])), ans=0, ee='\\(1-P(\\overline A)P(\\overline B)\\).', ev='\\(1-(1-%s)(1-%s)\\).' % (dec(p), dec(q)))


def m_one(r, lv):
    p, q = r.sample(PS[:5], 2)
    return dict(en='Two machines work independently with probabilities %s and %s. P(exactly one works) =…' % (dec(p), dec(q)), vi='Hai máy hoạt động độc lập, xác suất mỗi máy hoạt động tốt là %s và %s. Xác suất có đúng một máy hoạt động tốt là…' % (dec(p), dec(q)),
      opts=pick_opts(r, dec(p * (1 - q) + q * (1 - p)), decs([p * q, 1 - p * q, (1 - p) * (1 - q), p + q - p * q])), ans=0, ee='\\(P(A\\overline B)+P(\\overline AB)\\).', ev='\\(%s\\cdot(1-%s)+(1-%s)\\cdot%s\\) (hai trường hợp xung khắc).' % (dec(p), dec(q), dec(p), dec(q)))


def m_three(r, lv):
    p, q, s = r.sample(PS[:5], 3)
    return dict(en='Three independent components work with probabilities %s, %s, %s. A device works only if all three work. P(device works) =…' % (dec(p), dec(q), dec(s)), vi='Một thiết bị gồm ba bộ phận hoạt động độc lập với xác suất %s, %s, %s; thiết bị chỉ chạy khi cả ba bộ phận đều hoạt động. Xác suất thiết bị chạy là…' % (dec(p), dec(q), dec(s)),
      opts=pick_opts(r, dec(p * q * s), decs([min(p, q, s), (p + q + s) / 3, 1 - (1 - p) * (1 - q) * (1 - s), p * q])), ans=0, ee='Product of the three.', ev='Quy tắc nhân cho các biến cố độc lập: \\(%s\\cdot%s\\cdot%s\\).' % (dec(p), dec(q), dec(s)))


def m_coindie(r, lv):
    k = r.randint(1, 6); side = r.choice([('head', 'sấp'), ('tail', 'ngửa')])
    kind = r.choice(['eq', 'ge']); m = r.randint(3, 6)
    pe = F(1, 6) if kind == 'eq' else F(7 - m, 6)
    de, dv = ('shows %d' % k, 'ra mặt %d chấm' % k) if kind == 'eq' else ('shows at least %d' % m, 'ra mặt không nhỏ hơn %d chấm' % m)
    return dict(en='A coin is tossed and a die is rolled. P(the coin shows %s and the die %s) =…' % (side[0], de), vi='Gieo một đồng xu và một con xúc xắc. Xác suất đồng xu ra mặt %s và con xúc xắc %s là…' % (side[1], dv),
      opts=pick_opts(r, fr(F(1, 2) * pe), [fr(F(1, 2) + pe), fr(pe), fr(F(1, 2) + pe - F(1, 2) * pe), fr(F(1, 12) + F(1, 36))]), ans=0, ee='Independent: \\(\\frac12\\cdot%s\\).' % fr(pe), ev='Hai phép thử độc lập: \\(\\frac12\\cdot%s\\).' % fr(pe))


def m_miss(r, lv):
    p = r.choice(PS[:5]); n = r.choice([2, 3, 4])
    return dict(en='A player scores a penalty with probability %s, independently each time. P(he misses all %d penalties) =…' % (dec(p), n), vi='Một cầu thủ sút phạt đền thành công với xác suất %s, các lần sút độc lập. Xác suất cầu thủ đó sút trượt cả %d quả là…' % (dec(p), n),
      opts=pick_opts(r, dec((1 - p) ** n), decs([1 - p ** n, n * (1 - p), (1 - p) / n, p ** n])), ans=0, ee='\\((1-p)^%d\\).' % n, ev='\\((1-%s)^%d\\).' % (dec(p), n))


def m_check(r, lv):
    p, q = r.sample(PS[:5], 2); ok = r.random() < .5; pq = p * q if ok else p * q + F(1, 10)
    if pq > min(p, q): raise AssertionError
    return dict(en='\\(P(A)=%s\\), \\(P(B)=%s\\), \\(P(AB)=%s\\). Are \\(A\\) and \\(B\\) independent?' % (dec(p), dec(q), dec(pq)), vi='Cho \\(P(A)=%s\\), \\(P(B)=%s\\), \\(P(AB)=%s\\). Hai biến cố \\(A\\), \\(B\\) có độc lập không?' % (dec(p), dec(q), dec(pq)),
      opts=([TT('yes, since \\(P(AB)=P(A)P(B)\\)', 'có, vì \\(P(AB)=P(A)P(B)\\)'), TT('no, since \\(P(AB)\\ne P(A)P(B)\\)', 'không, vì \\(P(AB)\\ne P(A)P(B)\\)')] if ok else [TT('no, since \\(P(AB)\\ne P(A)P(B)\\)', 'không, vì \\(P(AB)\\ne P(A)P(B)\\)'), TT('yes, since \\(P(AB)=P(A)P(B)\\)', 'có, vì \\(P(AB)=P(A)P(B)\\)')]) +
           [TT('yes, since \\(P(AB)\\lt P(A)\\)', 'có, vì \\(P(AB)\\lt P(A)\\)'), TT('cannot be decided', 'không xác định được')], ans=0,
      ee='Compare \\(P(AB)\\) with \\(P(A)P(B)=%s\\).' % dec(p * q), ev='So sánh \\(P(AB)\\) với \\(P(A)P(B)=%s\\).' % dec(p * q))


def m_guess(r, lv):
    n = r.choice([3, 4, 5]); k = 4
    return dict(en='A student guesses %d multiple-choice questions, each with %d options. P(at least one correct) =…' % (n, k), vi='Một học sinh đoán ngẫu nhiên %d câu trắc nghiệm, mỗi câu có %d phương án. Xác suất đúng ít nhất một câu là…' % (n, k),
      opts=pick_opts(r, fr(1 - F(3, 4) ** n), [fr(F(1, 4) ** n), fr(F(n, 4)) if n < 4 else fr(F(3, 4)), fr(F(3, 4) ** n), fr(1 - F(1, 4) ** n)]), ans=0, ee='Complement: all wrong \\(\\left(\\frac34\\right)^%d\\).' % n, ev='Biến cố đối "sai cả %d câu": \\(\\left(\\frac34\\right)^%d\\) (các câu độc lập).' % (n, n))


M30S11 = [m_two, m_least, m_one, m_three, m_coindie, m_miss, m_check, m_guess]
