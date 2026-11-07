# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 10 – Bài 23 (quy tắc đếm), Bài 24 (hoán vị, chỉnh hợp, tổ hợp), Bài 25 (nhị thức Newton, n ≤ 5).
Đáp án tính bằng math.comb / math.perm / liệt kê trực tiếp."""
import math, itertools
from fractions import Fraction as F
from mb_selfpractice import pick_opts, fr
from sp_g10f import TT

C, A = math.comb, math.perm
def nums(ws): return [str(w) for w in ws]

# ================= Bài 23. Quy tắc đếm =================
def q_sum(r, lv):
    a, b, c = r.randint(3, 12), r.randint(3, 12), r.randint(2, 9)
    return dict(en='A canteen offers %d kinds of rice dishes, %d kinds of noodle dishes and %d kinds of bread. A student chooses one dish. How many choices are there?' % (a, b, c), vi='Căng tin có %d món cơm, %d món bún/phở và %d loại bánh mì. Một học sinh chọn một món. Có bao nhiêu cách chọn?' % (a, b, c),
      opts=pick_opts(r, str(a + b + c), nums([a * b * c, a * b + c, a + b * c, a + b])), ans=0, ee='Rule of sum (the cases do not overlap).', ev='Quy tắc cộng (ba phương án không trùng nhau): \\(%d+%d+%d=%d\\).' % (a, b, c, a + b + c))


def q_prod(r, lv):
    a, b, c = r.randint(2, 7), r.randint(2, 6), r.randint(2, 5)
    return dict(en='Lan has %d shirts, %d skirts and %d pairs of shoes. An outfit is one of each. How many outfits are there?' % (a, b, c), vi='Lan có %d áo, %d chân váy và %d đôi giày. Một bộ trang phục gồm một áo, một váy, một đôi giày. Có bao nhiêu bộ?' % (a, b, c),
      opts=pick_opts(r, str(a * b * c), nums([a + b + c, a * b + c, a * (b + c), a * b])), ans=0, ee='Rule of product (three successive choices).', ev='Quy tắc nhân (chọn lần lượt ba thứ): \\(%d\\cdot%d\\cdot%d=%d\\).' % (a, b, c, a * b * c))


def q_route(r, lv):
    m, n, k = r.randint(2, 6), r.randint(2, 6), r.randint(1, 4)
    return dict(en='From A to B there are %d roads, from B to C %d roads, and %d direct roads from A to C. How many ways are there to go from A to C?' % (m, n, k), vi='Từ A đến B có %d con đường, từ B đến C có %d con đường, ngoài ra có %d con đường đi thẳng từ A đến C. Có bao nhiêu cách đi từ A đến C?' % (m, n, k),
      opts=pick_opts(r, str(m * n + k), nums([m + n + k, m * n * k, m * n, (m + k) * n])), ans=0, ee='Via B: \\(%d\\cdot%d\\); direct: \\(%d\\); add.' % (m, n, k), ev='Qua B: \\(%d\\cdot%d=%d\\) cách (quy tắc nhân); đi thẳng: %d cách; cộng lại: %d.' % (m, n, m * n, k, m * n + k))


def _digits(r):
    k = r.randint(4, 7); hz = r.random() < .6
    D = sorted(r.sample(range(1, 10), k - (1 if hz else 0)) + ([0] if hz else []))
    return D, hz


def q_rep(r, lv):
    D, hz = _digits(r); n = len(D); L = r.choice([3, 4])
    ok = (n - 1 if hz else n) * n ** (L - 1)
    return dict(en='How many %d-digit numbers can be formed from the digits \\(%s\\) (digits may repeat)?' % (L, ',\\,'.join(map(str, D))), vi='Có bao nhiêu số tự nhiên có %d chữ số được lập từ các chữ số \\(%s\\) (các chữ số có thể lặp lại)?' % (L, ',\\,'.join(map(str, D))),
      opts=pick_opts(r, str(ok), nums([n ** L, A(n, L), (n - 1) * A(n - 1, L - 1) if hz else n * (n - 1) ** (L - 1), ok + n ** (L - 1)])), ans=0,
      ee='First digit: %d choices%s; each other digit: %d.' % (n - 1 if hz else n, ' (not 0)' if hz else '', n), ev='Chữ số đầu: %d cách%s; mỗi chữ số còn lại: %d cách; quy tắc nhân.' % (n - 1 if hz else n, ' (khác 0)' if hz else '', n))


def q_dist(r, lv):
    D, hz = _digits(r); n = len(D); L = r.choice([3, 4])
    if L > n: raise AssertionError
    ok = sum(1 for p in itertools.permutations(D, L) if p[0] != 0)
    return dict(en='How many %d-digit numbers with <b>distinct</b> digits can be formed from \\(%s\\)?' % (L, ',\\,'.join(map(str, D))), vi='Có bao nhiêu số tự nhiên có %d chữ số <b>đôi một khác nhau</b> lập từ các chữ số \\(%s\\)?' % (L, ',\\,'.join(map(str, D))),
      opts=pick_opts(r, str(ok), nums([A(n, L), n ** L, (n - 1) * n ** (L - 1), ok - A(n - 1, L - 1) if hz else ok + A(n - 1, L - 1)])), ans=0,
      ee='First digit%s, then the others without repetition.' % (' not 0' if hz else ''), ev='Chọn chữ số đầu%s, rồi các chữ số còn lại không lặp; kết quả %d.' % (' (khác 0)' if hz else '', ok))


def q_even(r, lv):
    D, hz = _digits(r); L = 3
    if len(D) < 4: raise AssertionError
    ok = sum(1 for p in itertools.permutations(D, L) if p[0] != 0 and p[-1] % 2 == 0)
    tot = sum(1 for p in itertools.permutations(D, L) if p[0] != 0)
    if ok == 0 or ok == tot: raise AssertionError
    return dict(en='How many <b>even</b> 3-digit numbers with distinct digits can be formed from \\(%s\\)?' % ',\\,'.join(map(str, D)), vi='Có bao nhiêu số tự nhiên <b>chẵn</b> có 3 chữ số đôi một khác nhau lập từ các chữ số \\(%s\\)?' % ',\\,'.join(map(str, D)),
      opts=pick_opts(r, str(ok), nums([tot - ok, tot, ok + 2, ok * 2])), ans=0,
      ee='Choose the last digit first (even); if 0 is used, split into cases.', ev='Chọn chữ số hàng đơn vị trước (chẵn); nếu có chữ số 0 thì chia trường hợp tận cùng là 0 hoặc khác 0. Kết quả %d.' % ok)


def q_div(r, lv):
    a, b, c = r.randint(1, 4), r.randint(0, 3), r.randint(0, 2)
    if b + c == 0: raise AssertionError
    N = 2 ** a * 3 ** b * 5 ** c; ok = (a + 1) * (b + 1) * (c + 1)
    return dict(en='How many positive divisors does \\(%d\\) have?' % N, vi='Số \\(%d\\) có bao nhiêu ước nguyên dương?' % N,
      opts=pick_opts(r, str(ok), nums([a * b * c if a * b * c else ok + 1, a + b + c + 1, ok - 1, (a + 1) * (b + 1) * (c + 1) + 2])), ans=0,
      ee='\\(%d=%s\\): a divisor is \\(2^i3^j5^k\\).' % (N, '\\cdot'.join(x for x in ('2^{%d}' % a, '3^{%d}' % b if b else '', '5^{%d}' % c if c else '') if x)), ev='\\(%d=%s\\); mỗi ước có dạng \\(2^i3^j5^k\\): số ước \\(=(%d+1)(%d+1)(%d+1)=%d\\).' % (N, '\\cdot'.join(x for x in ('2^{%d}' % a, '3^{%d}' % b if b else '', '5^{%d}' % c if c else '') if x), a, b, c, ok))


def q_plate(r, lv):
    L, D = r.choice([(1, 4), (2, 3), (1, 5), (2, 4)]); k = r.choice([24, 26])
    ok = k ** L * 10 ** D
    return dict(en='A licence plate has %d letter(s) (from %d letters) followed by %d digits (0–9). How many plates are possible?' % (L, k, D), vi='Một biển số gồm %d chữ cái (chọn trong %d chữ cái) và tiếp theo là %d chữ số (từ 0 đến 9). Có thể tạo được bao nhiêu biển số?' % (L, k, D),
      opts=pick_opts(r, '%d' % ok, nums([k * L + 10 * D, A(k, L) * A(10, D), k ** L + 10 ** D, k * 10 ** D])), ans=0,
      ee='Rule of product: \\(%d^{%d}\\cdot10^{%d}\\).' % (k, L, D), ev='Quy tắc nhân: \\(%d^{%d}\\cdot10^{%d}=%d\\).' % (k, L, D, ok))


M23S10 = [q_sum, q_prod, q_route, q_rep, q_dist, q_even, q_div, q_plate]

# ================= Bài 24. Hoán vị, chỉnh hợp, tổ hợp =================
def h_perm(r, lv):
    n = r.randint(4, 8)
    return dict(en='In how many ways can %d students stand in a row for a photo?' % n, vi='Có bao nhiêu cách xếp %d học sinh đứng thành một hàng ngang để chụp ảnh?' % n,
      opts=pick_opts(r, str(math.factorial(n)), nums([n * n, math.factorial(n - 1), n ** n, 2 ** n])), ans=0, ee='A permutation of %d elements: \\(%d!\\).' % (n, n), ev='Mỗi cách xếp là một hoán vị của %d phần tử: \\(P_{%d}=%d!=%d\\).' % (n, n, n, math.factorial(n)))


def h_arr(r, lv):
    n = r.randint(6, 15)
    return dict(en='A club of %d members elects a president, a vice-president and a secretary (different people). How many results are possible?' % n, vi='Một câu lạc bộ có %d thành viên bầu một chủ nhiệm, một phó chủ nhiệm và một thư kí (ba người khác nhau). Có bao nhiêu kết quả?' % n,
      opts=pick_opts(r, str(A(n, 3)), nums([C(n, 3), n ** 3, 3 * n, A(n, 2)])), ans=0, ee='Order matters: \\(A_{%d}^3\\).' % n, ev='Có phân biệt chức vụ (có thứ tự): \\(A_{%d}^3=%d\\cdot%d\\cdot%d=%d\\).' % (n, n, n - 1, n - 2, A(n, 3)))


def h_comb(r, lv):
    n, k = r.randint(7, 15), r.choice([2, 3, 4])
    return dict(en='A teacher chooses %d students out of %d to clean the classroom. How many choices are there?' % (k, n), vi='Giáo viên chọn %d học sinh trong %d học sinh để trực nhật. Có bao nhiêu cách chọn?' % (k, n),
      opts=pick_opts(r, str(C(n, k)), nums([A(n, k), n ** k, C(n, k - 1), n * k])), ans=0, ee='No order: \\(C_{%d}^{%d}\\).' % (n, k), ev='Không phân biệt thứ tự: \\(C_{%d}^{%d}=%d\\).' % (n, k, C(n, k)))


def h_group(r, lv):
    m, f = r.randint(5, 12), r.randint(4, 10); a, b = r.choice([(2, 1), (1, 2), (2, 2), (3, 1), (1, 3)])
    if a > m or b > f: raise AssertionError
    ok = C(m, a) * C(f, b)
    return dict(en='A class has %d boys and %d girls. Choose a team of %d boys and %d girls. How many teams?' % (m, f, a, b), vi='Một lớp có %d nam và %d nữ. Chọn một đội gồm %d nam và %d nữ. Có bao nhiêu cách?' % (m, f, a, b),
      opts=pick_opts(r, str(ok), nums([C(m, a) + C(f, b), C(m + f, a + b), A(m, a) * A(f, b), C(m, b) * C(f, a)])), ans=0, ee='\\(C_{%d}^{%d}\\cdot C_{%d}^{%d}\\).' % (m, a, f, b), ev='Chọn nam rồi chọn nữ (quy tắc nhân): \\(C_{%d}^{%d}\\cdot C_{%d}^{%d}=%d\\).' % (m, a, f, b, ok))


def h_hand(r, lv):
    n = r.randint(6, 25)
    return dict(en='At a meeting %d people shake hands, each pair once. How many handshakes are there?' % n, vi='Trong một buổi gặp mặt có %d người, mỗi hai người bắt tay nhau đúng một lần. Có bao nhiêu cái bắt tay?' % n,
      opts=pick_opts(r, str(C(n, 2)), nums([A(n, 2), n * n, n * (n - 1) // 2 + n, n - 1])), ans=0, ee='\\(C_{%d}^2\\).' % n, ev='Mỗi cái bắt tay ứng với một cặp không thứ tự: \\(C_{%d}^2=%d\\).' % (n, C(n, 2)))


def h_diag(r, lv):
    n = r.randint(5, 20)
    return dict(en='How many diagonals does a convex polygon with %d sides have?' % n, vi='Một đa giác lồi %d cạnh có bao nhiêu đường chéo?' % n,
      opts=pick_opts(r, str(C(n, 2) - n), nums([C(n, 2), A(n, 2) - n, n * (n - 3), C(n, 2) - 2 * n])), ans=0, ee='Segments joining two vertices minus the sides.', ev='Số đoạn nối hai đỉnh trừ số cạnh: \\(C_{%d}^2-%d=%d\\).' % (n, n, C(n, 2) - n))


def h_tri(r, lv):
    n = r.randint(5, 14)
    return dict(en='%d points lie in a plane, no three collinear. How many triangles have their vertices among these points?' % n, vi='Cho %d điểm trong mặt phẳng, không có ba điểm nào thẳng hàng. Có bao nhiêu tam giác có ba đỉnh là ba trong các điểm đó?' % n,
      opts=pick_opts(r, str(C(n, 3)), nums([A(n, 3), n ** 3, C(n, 2), 3 * n])), ans=0, ee='\\(C_{%d}^3\\).' % n, ev='Mỗi tam giác ứng với một tổ hợp chập 3: \\(C_{%d}^3=%d\\).' % (n, C(n, 3)))


def h_together(r, lv):
    n = r.randint(4, 8)
    ok = 2 * math.factorial(n - 1)
    return dict(en='%d friends, including An and Bình, sit on a bench. In how many ways can they sit so that An and Bình are next to each other?' % n, vi='%d bạn, trong đó có An và Bình, ngồi trên một băng ghế dài. Có bao nhiêu cách xếp để An và Bình ngồi cạnh nhau?' % n,
      opts=pick_opts(r, str(ok), nums([math.factorial(n - 1), math.factorial(n), math.factorial(n) - ok, 2 * math.factorial(n - 2)])), ans=0, ee='Glue An–Bình into one block: \\(2\\cdot(%d-1)!\\).' % n, ev='Coi An–Bình là một "khối": \\((%d-1)!\\) cách xếp, khối có 2 cách đổi chỗ: \\(2\\cdot%d!=%d\\).' % (n, n - 1, ok))


def h_least(r, lv):
    m, f, k = r.randint(5, 10), r.randint(3, 8), r.choice([3, 4])
    ok = C(m + f, k) - C(m, k)
    return dict(en='From %d boys and %d girls choose %d students with <b>at least one girl</b>. How many ways?' % (m, f, k), vi='Từ %d nam và %d nữ, chọn %d học sinh trong đó <b>có ít nhất một nữ</b>. Có bao nhiêu cách?' % (m, f, k),
      opts=pick_opts(r, str(ok), nums([C(m + f, k), f * C(m + f - 1, k - 1), C(f, 1) * C(m, k - 1), C(m + f, k) - C(f, k)])), ans=0, ee='Complement: all choices minus all-boy choices.', ev='Dùng phần bù: \\(C_{%d}^{%d}-C_{%d}^{%d}=%d\\).' % (m + f, k, m, k, ok))


M24S10 = [h_perm, h_arr, h_comb, h_group, h_hand, h_diag, h_tri, h_together, h_least]

# ================= Bài 25. Nhị thức Newton (n = 4, 5) =================
def mono(c, k, v='x'):
    if k == 0: return str(c)
    return ('' if c == 1 else '-' if c == -1 else str(c)) + v + ('' if k == 1 else '^%d' % k)


def binom_str(a, b, n):
    s = ('' if a == 1 else '-' if a == -1 else str(a)) + 'x' + ('%+d' % b)
    return '(%s)^%d' % (s, n)


def n_coef(r, lv):
    n = r.choice([4, 5]); a, b = r.choice([1, 2, 3, -1, -2]), r.choice([1, 2, 3, -1, -2, -3]); k = r.randint(1, n - 1)
    ok = C(n, k) * a ** k * b ** (n - k)
    return dict(en='The coefficient of \\(x^{%d}\\) in \\(%s\\) is…' % (k, binom_str(a, b, n)), vi='Hệ số của \\(x^{%d}\\) trong khai triển \\(%s\\) là…' % (k, binom_str(a, b, n)),
      opts=pick_opts(r, str(ok), nums([C(n, k), C(n, k) * a ** k, C(n, k) * b ** (n - k), -ok, C(n, k) * a ** (n - k) * b ** k])), ans=0,
      ee='Term \\(C_{%d}^{%d}(%dx)^{%d}(%d)^{%d}\\).' % (n, k, a, k, b, n - k), ev='Số hạng chứa \\(x^{%d}\\): \\(C_{%d}^{%d}(%dx)^{%d}(%d)^{%d}\\); hệ số \\(=%d\\).' % (k, n, k, a, k, b, n - k, ok))


def n_const(r, lv):
    c = r.choice([1, 2, 3, -1, -2, -3]); n = 4
    ok = C(4, 2) * c ** 2
    return dict(en='The constant term in \\(\\left(x%s\\dfrac{%d}{x}\\right)^4\\) is…' % ('+' if c > 0 else '-', abs(c)), vi='Số hạng không chứa \\(x\\) trong khai triển \\(\\left(x%s\\dfrac{%d}{x}\\right)^4\\) là…' % ('+' if c > 0 else '-', abs(c)),
      opts=pick_opts(r, str(ok), nums([C(4, 2) * abs(c), c ** 2, 4 * c ** 2, C(4, 1) * c ** 3, ok + 6])), ans=0,
      ee='General term \\(C_4^kx^{4-k}\\left(\\frac{%d}{x}\\right)^k=C_4^k(%d)^kx^{4-2k}\\); \\(k=2\\).' % (c, c), ev='Số hạng tổng quát \\(C_4^k(%d)^kx^{4-2k}\\); không chứa \\(x\\) khi \\(k=2\\): \\(C_4^2\\cdot(%d)^2=%d\\).' % (c, c, ok))


def n_sum(r, lv):
    n = r.choice([4, 5]); a, b = r.choice([1, 2, 3, -1, -2]), r.choice([1, 2, 3, -1, -2, -3])
    if a + b == 0: raise AssertionError
    ok = (a + b) ** n
    return dict(en='The sum of all coefficients in the expansion of \\(%s\\) is…' % binom_str(a, b, n), vi='Tổng các hệ số trong khai triển \\(%s\\) là…' % binom_str(a, b, n),
      opts=pick_opts(r, str(ok), nums([2 ** n, (a - b) ** n, (abs(a) + abs(b)) ** n if (abs(a) + abs(b)) ** n != ok else ok + 1, a ** n + b ** n, n * (a + b)])), ans=0,
      ee='Put \\(x=1\\).', ev='Thay \\(x=1\\): \\((%d%+d)^%d=%d\\).' % (a, b, n, ok))


def n_terms(r, lv):
    n = r.choice([4, 5]); a, b = r.choice([1, 2, 3]), r.choice([1, 2, 3, -1, -2])
    k = r.randint(0, n); ok = C(n, k) * a ** (n - k) * b ** k
    return dict(en='In the expansion of \\(%s\\) in <b>decreasing</b> powers of \\(x\\), the term number %d is…' % (binom_str(a, b, n), k + 1), vi='Khai triển \\(%s\\) theo lũy thừa <b>giảm dần</b> của \\(x\\). Số hạng thứ %d là…' % (binom_str(a, b, n), k + 1),
      opts=pick_opts(r, mono(ok, n - k), [mono(C(n, k) * a ** k * b ** (n - k), k), mono(C(n, k), n - k), mono(ok, k) if k != n - k else mono(-ok, n - k), mono(C(n, k + 1) * a ** (n - k - 1) * b ** (k + 1), n - k - 1) if k < n else mono(ok + 1, 0)]), ans=0,
      ee='Term \\(k+1\\): \\(C_{%d}^{%d}(%dx)^{%d}(%d)^{%d}\\).' % (n, k, a, n - k, b, k), ev='Số hạng thứ \\(k+1\\) là \\(C_{%d}^{k}(%dx)^{%d-k}(%d)^{k}\\) với \\(k=%d\\).' % (n, a, n, b, k))


def n_approx(r, lv):
    a = r.choice([1, 2, 3]); d = r.choice([1, 2, 3, -1, -2]); n = r.choice([4, 5])
    x = F(100 * a + d, 100); exact = x ** n
    two = a ** n + n * a ** (n - 1) * F(d, 100)
    return dict(en='Using the first two terms of the binomial expansion, \\((%s)^%d\\approx\\)…' % (('%.2f' % float(x)).replace('.', '{,}'), n), vi='Dùng hai số hạng đầu của khai triển nhị thức, \\((%s)^%d\\approx\\)…' % (('%.2f' % float(x)).replace('.', '{,}'), n),
      opts=pick_opts(r, ('%.2f' % float(two)).replace('.', '{,}'), [('%.2f' % float(a ** n + F(d, 100))).replace('.', '{,}'), ('%.2f' % float(a ** n + n * F(d, 100))).replace('.', '{,}'), ('%.2f' % float(two + F(1, 10))).replace('.', '{,}'), ('%.2f' % float(a ** n - n * a ** (n - 1) * F(d, 100))).replace('.', '{,}')]), ans=0,
      ee='\\((%d+%s)^%d\\approx%d^%d+%d\\cdot%d^{%d}\\cdot%s\\).' % (a, fr(F(d, 100)), n, a, n, n, a, n - 1, fr(F(d, 100))), ev='\\((%d+%s)^%d\\approx%d^%d+%d\\cdot%d^{%d}\\cdot(%s)=%s\\) (giá trị đúng \\(\\approx%s\\)).' % (a, fr(F(d, 100)), n, a, n, n, a, n - 1, fr(F(d, 100)), ('%.2f' % float(two)).replace('.', '{,}'), ('%.4f' % float(exact)).replace('.', '{,}')))


def n_mid(r, lv):
    a, b = r.choice([1, 2, 3]), r.choice([1, 2, 3, -1, -2, -3])
    ok = C(4, 2) * a ** 2 * b ** 2
    return dict(en='The middle term of the expansion of \\(%s\\) is…' % binom_str(a, b, 4), vi='Số hạng chính giữa của khai triển \\(%s\\) là…' % binom_str(a, b, 4),
      opts=pick_opts(r, mono(ok, 2), [mono(C(4, 2), 2), mono(ok, 3), mono(4 * a ** 3 * b, 3), mono(a * a * b * b, 2)]), ans=0,
      ee='5 terms; the 3rd: \\(C_4^2(%dx)^2(%d)^2\\).' % (a, b), ev='Có 5 số hạng; số hạng thứ 3: \\(C_4^2(%dx)^2(%d)^2=%s\\).' % (a, b, mono(ok, 2)))


def n_find(r, lv):
    n = r.choice([4, 5]); b = r.choice([1, 2, 3, -1, -2, -3]); k = r.randint(1, n - 1); coef = C(n, k) * b ** (n - k)
    return dict(en='In the expansion of \\((x+a)^%d\\) the coefficient of \\(x^{%d}\\) is \\(%d\\), and \\(a\\) is an integer. Then \\(a=\\)…' % (n, k, coef), vi='Trong khai triển \\((x+a)^%d\\), hệ số của \\(x^{%d}\\) bằng \\(%d\\), với \\(a\\) là số nguyên. Khi đó \\(a=\\)…' % (n, k, coef),
      opts=pick_opts(r, str(b), nums(([-b] if (n - k) % 2 else []) + [b + 1, 2 * b, b + 2, b - 2])), ans=0,
      ee='\\(C_{%d}^{%d}a^{%d}=%d\\).' % (n, k, n - k, coef), ev='Hệ số của \\(x^{%d}\\) là \\(C_{%d}^{%d}a^{%d}=%d\\cdot a^{%d}=%d\\) nên \\(a=%d\\)%s.' % (k, n, k, n - k, C(n, k), n - k, coef, b, ' (số mũ chẵn nên \\(a=%d\\) cũng thỏa mãn nhưng không có trong các phương án)' % -b if (n - k) % 2 == 0 else ''))


M25S10 = [n_coef, n_const, n_sum, n_terms, n_approx, n_mid, n_find, n_coef]
