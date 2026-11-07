# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 10 – Bài 26 (biến cố, định nghĩa cổ điển của xác suất), Bài 27 (thực hành tính xác suất).
Mọi đáp án được tính bằng cách LIỆT KÊ không gian mẫu (itertools) – đúng tuyệt đối."""
import math, itertools
from fractions import Fraction as F
from mb_selfpractice import pick_opts, fr
from sp_g10f import TT

C = math.comb
D2 = list(itertools.product(range(1, 7), repeat=2))
def P(fav, tot): return F(fav, tot)
def frs(xs): return [fr(x) for x in xs]

# ================= Bài 26 =================
def b_dice_sum(r, lv):
    s = r.randint(3, 11); k = sum(1 for a, b in D2 if a + b == s)
    return dict(en='Two fair dice are rolled. The probability that the sum is %d is…' % s, vi='Gieo hai con xúc xắc cân đối. Xác suất để tổng số chấm bằng %d là…' % s,
      opts=pick_opts(r, fr(P(k, 36)), frs([F(k, 6) if k < 6 else F(1, 2), F(k + 1, 36), F(1, 11), F(k, 12), F(s, 36)])), ans=0,
      ee='\\(n(\\Omega)=36\\); favourable outcomes: %d.' % k, ev='\\(n(\\Omega)=36\\); các kết quả thuận lợi: %s – có %d kết quả.' % (', '.join('(%d,%d)' % (a, b) for a, b in D2 if a + b == s), k))


def b_coins(r, lv):
    n = r.choice([3, 4]); k = r.randint(1, n - 1)
    return dict(en='%d fair coins are tossed. The probability of exactly %d heads is…' % (n, k), vi='Gieo %d đồng xu cân đối. Xác suất có đúng %d mặt sấp là…' % (n, k),
      opts=pick_opts(r, fr(F(C(n, k), 2 ** n)), frs([F(1, 2 ** n), F(k, n), F(1, n + 1), F(C(n, k), 2 ** n) + F(1, 2 ** n), F(1, 2)])), ans=0,
      ee='\\(n(\\Omega)=2^%d\\); choose the positions of the heads: \\(C_{%d}^{%d}\\).' % (n, n, k), ev='\\(n(\\Omega)=2^%d=%d\\); số kết quả thuận lợi \\(C_{%d}^{%d}=%d\\).' % (n, 2 ** n, n, k, C(n, k)))


def b_box1(r, lv):
    a, b, c = r.randint(2, 9), r.randint(2, 9), r.randint(1, 6); n = a + b + c
    return dict(en='A box has %d red, %d blue and %d green balls. One ball is drawn at random. P(the ball is not red) =…' % (a, b, c), vi='Một hộp có %d quả cầu đỏ, %d quả xanh dương và %d quả xanh lá. Lấy ngẫu nhiên một quả. Xác suất lấy được quả không phải màu đỏ là…' % (a, b, c),
      opts=pick_opts(r, fr(F(b + c, n)), frs([F(a, n), F(b, n), F(b + c, a), F(c, n), F(2, 3)])), ans=0, ee='\\(\\dfrac{%d+%d}{%d}\\).' % (b, c, n), ev='\\(n(\\Omega)=%d\\), thuận lợi \\(%d+%d=%d\\).' % (n, b, c, b + c))


def b_two(r, lv):
    a, b = r.randint(3, 8), r.randint(3, 8); n = a + b
    return dict(en='A box has %d white and %d black balls. Two balls are drawn at random. P(both are white) =…' % (a, b), vi='Một hộp có %d quả cầu trắng và %d quả cầu đen. Lấy ngẫu nhiên hai quả. Xác suất cả hai quả đều trắng là…' % (a, b),
      opts=pick_opts(r, fr(F(C(a, 2), C(n, 2))), frs([F(a, n) ** 2, F(a, n), F(C(a, 2), n * n), F(a * b, C(n, 2)), F(C(b, 2), C(n, 2))])), ans=0,
      ee='\\(\\dfrac{C_{%d}^2}{C_{%d}^2}\\).' % (a, n), ev='\\(n(\\Omega)=C_{%d}^2=%d\\); thuận lợi \\(C_{%d}^2=%d\\).' % (n, C(n, 2), a, C(a, 2)))


def b_least(r, lv):
    a, b, k = r.randint(3, 7), r.randint(3, 7), r.choice([2, 3]); n = a + b
    return dict(en='From %d boys and %d girls, %d students are chosen at random. P(at least one girl) =…' % (a, b, k), vi='Chọn ngẫu nhiên %d học sinh từ %d nam và %d nữ. Xác suất chọn được ít nhất một nữ là…' % (k, a, b),
      opts=pick_opts(r, fr(1 - F(C(a, k), C(n, k))), frs([F(C(a, k), C(n, k)), F(b, n), 1 - F(a, n) ** k, F(C(b, k), C(n, k)), F(b * C(n - 1, k - 1), C(n, k))])), ans=0,
      ee='Complement: all boys, \\(\\dfrac{C_{%d}^{%d}}{C_{%d}^{%d}}\\).' % (a, k, n, k), ev='Biến cố đối "toàn nam": \\(\\dfrac{C_{%d}^{%d}}{C_{%d}^{%d}}\\); lấy 1 trừ đi.' % (a, k, n, k))


def b_omega(r, lv):
    kind = r.randrange(4)
    data = [('A coin is tossed and a die is rolled', 'Gieo một đồng xu và một con xúc xắc', 12), ('Two dice are rolled', 'Gieo hai con xúc xắc', 36), ('Three coins are tossed', 'Gieo ba đồng xu', 8),
            ('A coin is tossed twice and a die is rolled once', 'Gieo một đồng xu hai lần và một con xúc xắc một lần', 24)][kind]
    return dict(en='%s. The number of elements of the sample space is…' % data[0], vi='%s. Số phần tử của không gian mẫu là…' % data[1],
      opts=pick_opts(r, str(data[2]), [str(x) for x in (8, 12, 24, 36, 6, 18) if x != data[2]]), ans=0, ee='Rule of product.', ev='Quy tắc nhân: \\(n(\\Omega)=%d\\).' % data[2])


def b_div(r, lv):
    N = r.choice([20, 30, 50, 100, 40, 60]); k = r.choice([3, 4, 6, 7])
    return dict(en='A number is chosen at random from \\(1,2,\\dots,%d\\). P(it is divisible by %d) =…' % (N, k), vi='Chọn ngẫu nhiên một số trong các số \\(1,2,\\dots,%d\\). Xác suất số đó chia hết cho %d là…' % (N, k),
      opts=pick_opts(r, fr(F(N // k, N)), frs([F(1, k), F(N // k + 1, N), F(k, N), F(N // k, N - 1)])), ans=0, ee='There are \\(\\lfloor %d/%d\\rfloor=%d\\) multiples.' % (N, k, N // k), ev='Có %d bội của %d trong \\([1;%d]\\).' % (N // k, k, N))


def b_team(r, lv):
    a, b = r.randint(4, 9), r.randint(3, 8); n = a + b
    return dict(en='Choose 3 students at random from %d boys and %d girls. P(exactly 2 boys and 1 girl) =…' % (a, b), vi='Chọn ngẫu nhiên 3 học sinh từ %d nam và %d nữ. Xác suất chọn được đúng 2 nam và 1 nữ là…' % (a, b),
      opts=pick_opts(r, fr(F(C(a, 2) * b, C(n, 3))), frs([F(C(a, 2) + b, C(n, 3)), F(C(a, 2), C(n, 3)), F(a * C(b, 2), C(n, 3)), F(2, 3)])), ans=0,
      ee='\\(\\dfrac{C_{%d}^2\\cdot C_{%d}^1}{C_{%d}^3}\\).' % (a, b, n), ev='\\(\\dfrac{C_{%d}^2\\cdot%d}{C_{%d}^3}=\\dfrac{%d}{%d}\\).' % (a, b, n, C(a, 2) * b, C(n, 3)))


M26S10 = [b_dice_sum, b_coins, b_box1, b_two, b_least, b_omega, b_div, b_team]

# ================= Bài 27 =================
def t_prod(r, lv):
    kind = r.choice(['even', 'odd', 'six'])
    if kind == 'even': k = sum(1 for a, b in D2 if a * b % 2 == 0); e, v = 'the product is even', 'tích số chấm là số chẵn'
    elif kind == 'odd': k = sum(1 for a, b in D2 if a * b % 2 == 1); e, v = 'the product is odd', 'tích số chấm là số lẻ'
    else: m = r.choice([6, 12, 4]); k = sum(1 for a, b in D2 if a * b == m); e, v = 'the product equals %d' % m, 'tích số chấm bằng %d' % m
    return dict(en='Two dice are rolled. P(%s) =…' % e, vi='Gieo hai con xúc xắc. Xác suất để %s là…' % v,
      opts=pick_opts(r, fr(P(k, 36)), frs([F(1, 2), F(k, 6) if k < 6 else F(1, 4), F(k + 2, 36), F(36 - k, 36), F(1, 3)])), ans=0, ee='List the table of 36 outcomes.', ev='Lập bảng 36 kết quả; có %d kết quả thuận lợi.' % k)


def t_diff(r, lv):
    d = r.randint(0, 4); k = sum(1 for a, b in D2 if abs(a - b) == d)
    return dict(en='Two dice are rolled. P(the difference of the numbers is %d) =…' % d, vi='Gieo hai con xúc xắc. Xác suất hiệu (lớn trừ nhỏ) số chấm bằng %d là…' % d,
      opts=pick_opts(r, fr(P(k, 36)), frs([F(k, 2 * 36), F(6 - d, 36), F(1, 6), F(k + 2, 36), F(2 * (6 - d), 36) if d else F(1, 3), F(k + 1, 36), F(k + 4, 36)])), ans=0, ee='Count pairs \\((a,b)\\) with \\(|a-b|=%d\\).' % d, ev='Đếm các cặp \\((a,b)\\) có \\(|a-b|=%d\\): %d cặp.' % (d, k))


def t_max(r, lv):
    m = r.randint(1, 6); big = r.random() < .5
    if (big and m == 1) or (not big and m == 6): raise AssertionError
    k = sum(1 for a, b in D2 if (max(a, b) if big else min(a, b)) == m)
    e, v = ('larger', 'lớn nhất') if big else ('smaller', 'nhỏ nhất')
    return dict(en='Two dice are rolled. P(the %s number is %d) =…' % (e, m), vi='Gieo hai con xúc xắc. Xác suất số chấm %s bằng %d là…' % (v, m),
      opts=pick_opts(r, fr(P(k, 36)), frs([F(1, 6), F(m, 36), F(2 * m, 36), F(k + 1, 36), F(m * m, 36), F(k + 2, 36)])), ans=0, ee='Count the cells of the table.', ev='Đếm trong bảng 36 ô: có %d kết quả thuận lợi.' % k)


def t_ge(r, lv):
    s = r.randint(7, 11); k = sum(1 for a, b in D2 if a + b >= s)
    return dict(en='Two dice are rolled. P(the sum is at least %d) =…' % s, vi='Gieo hai con xúc xắc. Xác suất tổng số chấm không nhỏ hơn %d là…' % s,
      opts=pick_opts(r, fr(P(k, 36)), frs([F(13 - s, 11), F(k, 6) if k < 6 else F(1, 2), F(36 - k, 36), F(k - 1, 36) if k > 1 else F(1, 9), F(k + 3, 36)])), ans=0, ee='Count the table entries.', ev='Đếm trong bảng: %d kết quả.' % k)


def t_pair(r, lv):
    n = r.randint(6, 12)
    ev_ = sum(1 for a, b in itertools.combinations(range(1, n + 1), 2) if (a + b) % 2 == 0)
    return dict(en='Two different numbers are chosen at random from \\(1,2,\\dots,%d\\). P(their sum is even) =…' % n, vi='Chọn ngẫu nhiên hai số khác nhau từ \\(1,2,\\dots,%d\\). Xác suất tổng hai số là số chẵn là…' % n,
      opts=pick_opts(r, fr(F(ev_, C(n, 2))), frs([F(1, 2), F(ev_ + 1, C(n, 2)), F(C(n, 2) - ev_, C(n, 2)), F(ev_, n * n)])), ans=0,
      ee='Even sum: both even or both odd.', ev='Tổng chẵn khi hai số cùng chẵn hoặc cùng lẻ: \\(%d\\) cặp trên \\(C_{%d}^2=%d\\).' % (ev_, n, C(n, 2)))


def t_adj(r, lv):
    n = r.randint(4, 8)
    return dict(en='%d students, including An and Bình, line up in a random order. P(An and Bình stand next to each other) =…' % n, vi='%d học sinh, trong đó có An và Bình, xếp hàng ngang ngẫu nhiên. Xác suất An và Bình đứng cạnh nhau là…' % n,
      opts=pick_opts(r, fr(F(2, n)), frs([F(1, n), F(2, n - 1), F(1, n - 1), F(2, n * (n - 1))])), ans=0, ee='\\(\\dfrac{2\\cdot(%d-1)!}{%d!}\\).' % (n, n), ev='\\(\\dfrac{2\\cdot(%d-1)!}{%d!}=\\dfrac2{%d}\\).' % (n, n, n))


def t_card(r, lv):
    n = r.choice([10, 12, 15, 20]); kind = r.choice(['prime', 'square'])
    S = [x for x in range(1, n + 1) if (kind == 'prime' and x > 1 and all(x % d for d in range(2, int(x ** .5) + 1))) or (kind == 'square' and int(x ** .5) ** 2 == x)]
    e, v = ('a prime number', 'số nguyên tố') if kind == 'prime' else ('a perfect square', 'số chính phương')
    return dict(en='%d cards are numbered 1 to %d. One card is drawn. P(the number is %s) =…' % (n, n, e), vi='Có %d tấm thẻ đánh số từ 1 đến %d. Rút ngẫu nhiên một thẻ. Xác suất số trên thẻ là %s là…' % (n, n, v),
      opts=pick_opts(r, fr(F(len(S), n)), frs([F(len(S) + 1, n), F(len(S) - 1, n), F(1, 2), F(len(S), n - 1)])), ans=0, ee='Favourable: %s.' % ', '.join(map(str, S)), ev='Các số thuận lợi: %s (%d số).' % (', '.join(map(str, S)), len(S)))


def t_sim(r, lv):
    N = r.choice([50, 100, 200]); p = r.choice([F(1, 6), F(1, 4), F(1, 2), F(1, 3)])
    return dict(en='A die is rolled %d times by simulation. Theoretically, about how many times do we expect the event of probability %s to occur?' % (N, fr(p)), vi='Mô phỏng gieo xúc xắc %d lần. Về lí thuyết, biến cố có xác suất %s xảy ra khoảng bao nhiêu lần?' % (N, fr(p)),
      opts=pick_opts(r, fr(N * p) if (N * p).denominator == 1 else '%.1f' % float(N * p), [str(N // 2) if N * p != N // 2 else str(N // 3), str(N // 10), str(N), fr(F(N, 6)) if N * p != F(N, 6) else str(N // 5)]), ans=0,
      ee='Expected count \\(\\approx N\\cdot P\\).', ev='Số lần dự kiến \\(\\approx N\\cdot P=%d\\cdot%s\\); tần suất thực nghiệm dao động quanh xác suất.' % (N, fr(p)))


M27S10 = [t_prod, t_diff, t_max, t_ge, t_pair, t_adj, t_card, t_sim]
