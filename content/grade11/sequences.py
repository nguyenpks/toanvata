# -*- coding: utf-8 -*-
"""Nội dung bài g11-sequences-01 = Toán 11 KNTT, Chương II, Bài 5: Dãy số – CHỈ NỘI DUNG.
Mã ngân hàng câu hỏi: TOAN11-C2-B05. Bài tập: mỗi mức một bộ riêng, cùng dạng, khác số liệu (LEVEL_PRACTICE)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
from fractions import Fraction as F

LID = 'g11-sequences-01'
CAT = 'Sequences'
TOPIC = (CAT, 'Dãy số. Cấp số cộng và cấp số nhân')
CV = 'Dãy số'

ensure_vocab([
 ('g11-sequence', 'sequence', 'dãy số', CV, 'A sequence is a list of numbers in order.', r'\((u_n)\)'),
 ('g11-term', 'term', 'số hạng', CV, 'Find the fifth term.', r'\(u_5\)'),
 ('g11-general-term', 'general term', 'số hạng tổng quát', CV, 'The general term is u_n = 2n + 1.', r'\(u_n\)'),
 ('g11-recursive', 'recursive formula', 'công thức truy hồi', CV, 'Use the recursive formula to find the next term.', r'\(u_{n+1}=u_n+3\)'),
 ('g11-finite-seq', 'finite sequence', 'dãy số hữu hạn', CV, 'A finite sequence has a last term.', ''),
 ('g11-infinite-seq', 'infinite sequence', 'dãy số vô hạn', CV, 'An infinite sequence has no last term.', ''),
 ('g11-increasing-seq', 'increasing sequence', 'dãy số tăng', CV, 'Each term is greater than the one before.', r'\(u_{n+1}>u_n\)'),
 ('g11-decreasing-seq', 'decreasing sequence', 'dãy số giảm', CV, 'Each term is smaller than the one before.', r'\(u_{n+1}<u_n\)'),
 ('g11-bounded-above', 'bounded above', 'bị chặn trên', CV, 'The sequence is bounded above by 2.', r'\(u_n\le M\)'),
 ('g11-bounded-below', 'bounded below', 'bị chặn dưới', CV, 'The sequence is bounded below by 0.', r'\(u_n\ge m\)'),
 ('g11-bounded-seq', 'bounded sequence', 'dãy số bị chặn', CV, 'A sequence bounded above and below is a bounded sequence.', ''),
])
load_vocab()

# ---- kiểm tra số liệu ----
def seq(f, N): return [f(n) for n in range(1, N + 1)]
def rec(u1, g, N):
    out = [u1]
    while len(out) < N: out.append(g(out[-1]))
    return out
inc = lambda s: all(b > a for a, b in zip(s, s[1:]))
dec = lambda s: all(b < a for a, b in zip(s, s[1:]))
# VD1
assert seq(lambda n: F(2 * n + 1, n + 2), 5) == [1, F(5, 4), F(7, 5), F(3, 2), F(11, 7)]
# VD2
assert rec(2, lambda u: 3 * u - 1, 5) == [2, 5, 14, 41, 122]
# VD3
assert inc(seq(lambda n: F(n, n + 1), 200)) and all(F(n + 1, n + 2) - F(n, n + 1) == F(1, (n + 1) * (n + 2)) for n in range(1, 200))
assert dec(seq(lambda n: F(1, n), 200))
alt = seq(lambda n: (-1) ** n, 20); assert not inc(alt) and not dec(alt)
# VD4: (2n+1)/(n+1) = 2 - 1/(n+1), 1 <= u_n < 2
assert all(F(2 * n + 1, n + 1) == 2 - F(1, n + 1) and 1 <= F(2 * n + 1, n + 1) < 2 for n in range(1, 500))
assert min(seq(lambda n: n * n, 500)) == 1 and max(seq(lambda n: n * n, 500)) == 500 ** 2   # n² tăng không giới hạn: không bị chặn trên
assert all(n * n > 10 ** 6 for n in (1001, 2000))
# VD5: ghế ở hàng n là 20 + 2(n-1) = 2n + 18
assert all(20 + 2 * (n - 1) == 2 * n + 18 for n in range(1, 30)) and 2 * 10 + 18 == 38 and 2 * 16 + 18 == 50 and 20 + 2 * 15 == 50
# Đồ thị điểm
PTS = [(n, F(2 * n + 1, n + 1)) for n in range(1, 13)]
assert all(y < 2 for _, y in PTS) and inc([y for _, y in PTS])
# Bài tập mức 1
assert 3 * 4 - 2 == 10 and rec(2, lambda u: u + 3, 4)[-1] == 11 and inc(seq(lambda n: n + 3, 100))
assert inc(seq(lambda n: 2 * n - 1, 100)) and not inc(seq(lambda n: n * n, 5)) is False   # n² tăng
assert rec(1, lambda u: u + 4, 5)[-1] == 17 and 3 * 9 - 2 == 25 and all(3 * n - 2 != 25 for n in range(1, 9))
# Bài tập mức 2
assert 5 ** 2 + 1 == 26 and rec(1, lambda u: 2 * u + 1, 4)[-1] == 15 and dec(seq(lambda n: F(1, n), 100))
assert not dec(seq(lambda n: F(n, n + 1), 100)) and inc(seq(lambda n: F(n, n + 1), 100))
assert all(0 < F(1, n) <= 1 for n in range(1, 500)) and rec(3, lambda u: 2 * u, 4)[-1] == 24 and 2 * 13 + 5 == 31
# Bài tập mức 3
assert 2 ** 5 - 1 == 31 and rec(2, lambda u: 3 * u - 1, 4)[-1] == 41 and not inc(alt) and not dec(alt)
assert all(abs(x) <= 1 for x in alt) and all(-n <= -1 for n in range(1, 500))
fib = [1, 1]
while len(fib) < 7: fib.append(fib[-1] + fib[-2])
assert fib == [1, 1, 2, 3, 5, 8, 13] and 9 ** 2 - 1 == 80

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 60 minutes', 'khoảng 60 phút'),
            before=('functions, their graphs and inequalities', 'hàm số, đồ thị và bất đẳng thức'))
goals = [
 ('say what a sequence is and find its terms;', 'nêu được [[dãy số]] là gì và tìm các [[số hạng]] của nó;'),
 ('give a sequence by a formula, a description or a recursive formula;', 'cho dãy số bằng công thức, bằng mô tả hoặc bằng [[công thức truy hồi]];'),
 ('decide whether a sequence is increasing or decreasing;', 'xét được dãy số tăng hay giảm;'),
 ('decide whether a sequence is bounded.', 'xét được dãy số có bị chặn hay không.'),
]
goals[0] = ('say what a sequence is and find its terms;', 'nêu được [[dãy số]] là gì và tìm các [[số hạng]] của nó;')
vocab = [
 ('<b>sequence</b> – numbers listed in a fixed order: \\(u_1,u_2,u_3,\\dots\\)', '[[Dãy số]] – các số xếp theo một thứ tự: \\(u_1,u_2,u_3,\\dots\\)'),
 ('<b>term</b> – one number of the sequence; \\(u_n\\) is the n-th term.', '[[Số hạng]] – một số của dãy; \\(u_n\\) là số hạng thứ n.'),
 ('<b>general term</b> – the formula for \\(u_n\\) in terms of n.', '[[Số hạng tổng quát]] – công thức tính \\(u_n\\) theo n.'),
 ('<b>recursive formula</b> – gives the first term and a rule for the next term from the previous ones.', '[[Công thức truy hồi]] – cho số hạng đầu và quy tắc tính số hạng sau từ các số hạng trước.'),
 ('<b>finite sequence</b> – has a last term.', '[[Dãy số hữu hạn]] – có số hạng cuối cùng.'),
 ('<b>infinite sequence</b> – has no last term.', '[[Dãy số vô hạn]] – không có số hạng cuối cùng.'),
 ('<b>increasing sequence</b> – \\(u_{n+1}>u_n\\) for every n.', '[[Dãy số tăng]] – \\(u_{n+1}>u_n\\) với mọi n.'),
 ('<b>decreasing sequence</b> – \\(u_{n+1}<u_n\\) for every n.', '[[Dãy số giảm]] – \\(u_{n+1}<u_n\\) với mọi n.'),
 ('<b>bounded above</b> – there is M with \\(u_n\\le M\\) for every n.', '[[Bị chặn trên]] – có M để \\(u_n\\le M\\) với mọi n.'),
 ('<b>bounded below</b> – there is m with \\(u_n\\ge m\\) for every n.', '[[Bị chặn dưới]] – có m để \\(u_n\\ge m\\) với mọi n.'),
 ('<b>bounded sequence</b> – bounded above and bounded below.', '[[Dãy số bị chặn]] – vừa bị chặn trên vừa bị chặn dưới.'),
]
phrases = [
 ('<b>Find the first five terms.</b>', 'Tìm năm số hạng đầu.'),
 ('<b>Find the general term.</b>', 'Tìm số hạng tổng quát.'),
 ('<b>Is the sequence increasing or decreasing?</b>', 'Dãy số tăng hay giảm?'),
 ('<b>Is the sequence bounded?</b>', 'Dãy số có bị chặn không?'),
 ('<b>The sequence is defined by…</b>', 'Dãy số được xác định bởi…'),
]
review = (
 T('<b>Evaluating a formula.</b> To find the value of \\(f(n)\\), replace n by the number. For \\(f(n)=2n+1\\), \\(f(3)=7\\).', '<b>Tính giá trị biểu thức.</b> Để tính \\(f(n)\\), thay n bằng số đã cho. Với \\(f(n)=2n+1\\) thì \\(f(3)=7\\).') +
 T('<b>Comparing two numbers.</b> To compare a and b, look at the sign of \\(a-b\\).', '<b>So sánh hai số.</b> Để so sánh a và b, xét dấu của \\(a-b\\).') +
 T('<b>Natural numbers.</b> \\(n=1,2,3,\\dots\\) are positive integers.', '<b>Số tự nhiên.</b> \\(n=1,2,3,\\dots\\) là các số nguyên dương.'))

theory = '<h3>5.1 %s</h3>' % TI('What is a sequence?', 'Dãy số là gì?')
theory += T('A <b>sequence</b> is a list of numbers in a fixed order. We write \\(u_1,u_2,u_3,\\dots\\) or \\((u_n)\\); \\(u_1\\) is the first term and \\(u_n\\) is the n-th term. A sequence with a last term is a <b>finite sequence</b>; if it never ends it is an <b>infinite sequence</b>.',
            '[[Dãy số]] là một danh sách các số theo thứ tự cố định. Ta viết \\(u_1,u_2,u_3,\\dots\\) hay \\((u_n)\\); \\(u_1\\) là số hạng đầu, \\(u_n\\) là [[số hạng]] thứ n. Dãy có số hạng cuối là [[dãy số hữu hạn]]; dãy không kết thúc là [[dãy số vô hạn]].')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T('A sequence is a function whose domain is the positive integers: \\(n\\mapsto u_n\\). Example: \\(u_n=2n+1\\) gives \\(3,5,7,9,\\dots\\)', 'Dãy số là hàm số xác định trên tập các số nguyên dương: \\(n\\mapsto u_n\\). Ví dụ \\(u_n=2n+1\\) cho \\(3,5,7,9,\\dots\\)'))

theory += '<h3>5.2 %s</h3>' % TI('Ways to give a sequence', 'Các cách cho một dãy số')
theory += BOX('blue', ('Three ways', 'Ba cách cho dãy số'),
  T('<b>1. By a formula</b> for the general term: \\(u_n=\\dfrac{n}{n+1}\\).', '<b>1. Bằng công thức</b> của [[số hạng tổng quát]]: \\(u_n=\\dfrac{n}{n+1}\\).'),
  T('<b>2. By a description:</b> \\(u_n\\) is the n-th prime number: \\(2,3,5,7,11,\\dots\\)', '<b>2. Bằng mô tả:</b> \\(u_n\\) là số nguyên tố thứ n: \\(2,3,5,7,11,\\dots\\)'),
  T('<b>3. By a recursive formula:</b> give the first term and the rule to get the next one. Example: \\(u_1=1,\\ u_{n+1}=u_n+2\\) gives \\(1,3,5,7,\\dots\\)', '<b>3. Bằng công thức truy hồi:</b> cho số hạng đầu và quy tắc suy ra số hạng sau. Ví dụ \\(u_1=1,\\ u_{n+1}=u_n+2\\) cho \\(1,3,5,7,\\dots\\)'))
theory += BOX('mint', ('The Fibonacci sequence', 'Dãy Fibonacci'),
  T('\\(u_1=1,\\ u_2=1,\\ u_{n+2}=u_{n+1}+u_n\\). Each term is the sum of the two before it: \\(1,1,2,3,5,8,13,\\dots\\)', '\\(u_1=1,\\ u_2=1,\\ u_{n+2}=u_{n+1}+u_n\\). Mỗi số hạng bằng tổng hai số hạng đứng trước: \\(1,1,2,3,5,8,13,\\dots\\)'))
theory += T('We can draw a sequence as points \\((n;u_n)\\) in the plane. For \\(u_n=\\dfrac{2n+1}{n+1}\\) the points rise and stay below the line \\(y=2\\).', 'Ta có thể vẽ dãy số bằng các điểm \\((n;u_n)\\) trên mặt phẳng. Với \\(u_n=\\dfrac{2n+1}{n+1}\\) các điểm đi lên và luôn nằm dưới đường \\(y=2\\).')
theory += GRAPH({'view': [-0.8, 13.5, -0.3, 2.6], 'functions': [], 'guides': [{'type': 'h', 'y': 2}],
                 'points': [{'x': n, 'y': float(y), 'label': ''} for n, y in PTS]},
                cap=('The points (n; u_n) of u_n = (2n+1)/(n+1). They increase and stay below y = 2.', 'Các điểm (n; u_n) của u_n = (2n+1)/(n+1). Chúng tăng dần và luôn dưới đường y = 2.'),
                alt=('Points of a sequence rising towards the line y = 2', ''), height=300)

theory += '<h3>5.3 %s</h3>' % TI('Increasing and decreasing sequences', 'Dãy số tăng, dãy số giảm')
theory += BOX('blue', ('Monotonic sequences', 'Dãy số đơn điệu'),
  T('\\((u_n)\\) is an <b>increasing sequence</b> if \\(u_{n+1}>u_n\\) for every n.', '\\((u_n)\\) là [[dãy số tăng]] nếu \\(u_{n+1}>u_n\\) với mọi n.'),
  T('\\((u_n)\\) is a <b>decreasing sequence</b> if \\(u_{n+1}<u_n\\) for every n.', '\\((u_n)\\) là [[dãy số giảm]] nếu \\(u_{n+1}<u_n\\) với mọi n.'),
  T('Method: find the sign of \\(u_{n+1}-u_n\\). A sequence can be neither, for example \\(u_n=(-1)^n\\).', 'Cách làm: xét dấu của \\(u_{n+1}-u_n\\). Có dãy không tăng cũng không giảm, ví dụ \\(u_n=(-1)^n\\).'))

theory += '<h3>5.4 %s</h3>' % TI('Bounded sequences', 'Dãy số bị chặn')
theory += BOX('blue', ('Bounded above and below', 'Bị chặn trên và bị chặn dưới'),
  T('\\((u_n)\\) is <b>bounded above</b> if there is a number M with \\(u_n\\le M\\) for every n.', '\\((u_n)\\) [[bị chặn trên]] nếu có số M để \\(u_n\\le M\\) với mọi n.'),
  T('\\((u_n)\\) is <b>bounded below</b> if there is a number m with \\(u_n\\ge m\\) for every n.', '\\((u_n)\\) [[bị chặn dưới]] nếu có số m để \\(u_n\\ge m\\) với mọi n.'),
  T('If both hold, it is a <b>bounded sequence</b>: \\(m\\le u_n\\le M\\).', 'Nếu cả hai đều đúng thì đó là [[dãy số bị chặn]]: \\(m\\le u_n\\le M\\).'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'),
  T('Checking a few terms is not a proof. To show a sequence is increasing, prove \\(u_{n+1}-u_n>0\\) for <b>every</b> n.', 'Thử vài số hạng chưa phải là chứng minh. Để chứng tỏ dãy tăng, phải chứng minh \\(u_{n+1}-u_n>0\\) với <b>mọi</b> n.'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('First terms from a formula', 'Các số hạng đầu từ công thức'),
  T('Find the first five terms of \\(u_n=\\dfrac{2n+1}{n+2}\\).', 'Tìm năm số hạng đầu của dãy \\(u_n=\\dfrac{2n+1}{n+2}\\).'),
  ('Replace n by 1, 2, 3, 4, 5.', 'Thay n lần lượt bằng 1, 2, 3, 4, 5.'),
  [T('\\(u_1=\\dfrac33=1,\\ u_2=\\dfrac54,\\ u_3=\\dfrac75\\).', '\\(u_1=\\dfrac33=1,\\ u_2=\\dfrac54,\\ u_3=\\dfrac75\\).'),
   T('\\(u_4=\\dfrac96=\\dfrac32,\\ u_5=\\dfrac{11}{7}\\).', '\\(u_4=\\dfrac96=\\dfrac32,\\ u_5=\\dfrac{11}{7}\\).')],
  '\\(1,\\ \\dfrac54,\\ \\dfrac75,\\ \\dfrac32,\\ \\dfrac{11}{7}\\).')
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('A recursive sequence', 'Dãy số cho bằng truy hồi'),
  T('A sequence has \\(u_1=2\\) and \\(u_{n+1}=3u_n-1\\). Find \\(u_2,u_3,u_4\\).', 'Dãy số có \\(u_1=2\\) và \\(u_{n+1}=3u_n-1\\). Tìm \\(u_2,u_3,u_4\\).'),
  ('Use each term to get the next one.', 'Dùng mỗi số hạng để tính số hạng kế tiếp.'),
  [T('\\(u_2=3\\cdot2-1=5\\).', '\\(u_2=3\\cdot2-1=5\\).'), T('\\(u_3=3\\cdot5-1=14\\).', '\\(u_3=3\\cdot5-1=14\\).'), T('\\(u_4=3\\cdot14-1=41\\).', '\\(u_4=3\\cdot14-1=41\\).')],
  '\\(u_2=5,\\ u_3=14,\\ u_4=41\\).')
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Increasing or decreasing?', 'Tăng hay giảm?'),
  T('Decide whether each sequence is increasing, decreasing or neither: (a) \\(u_n=\\dfrac{n}{n+1}\\); (b) \\(u_n=\\dfrac1n\\); (c) \\(u_n=(-1)^n\\).', 'Xét mỗi dãy số tăng, giảm hay không đơn điệu: (a) \\(u_n=\\dfrac{n}{n+1}\\); (b) \\(u_n=\\dfrac1n\\); (c) \\(u_n=(-1)^n\\).'),
  ('Find the sign of \\(u_{n+1}-u_n\\).', 'Xét dấu của \\(u_{n+1}-u_n\\).'),
  [T('(a) \\(\\dfrac{n+1}{n+2}-\\dfrac{n}{n+1}=\\dfrac{1}{(n+1)(n+2)}>0\\): increasing.', '(a) \\(\\dfrac{n+1}{n+2}-\\dfrac{n}{n+1}=\\dfrac{1}{(n+1)(n+2)}>0\\): dãy tăng.'),
   T('(b) \\(\\dfrac{1}{n+1}-\\dfrac1n=\\dfrac{-1}{n(n+1)}<0\\): decreasing.', '(b) \\(\\dfrac{1}{n+1}-\\dfrac1n=\\dfrac{-1}{n(n+1)}<0\\): dãy giảm.'),
   T('(c) The terms are \\(-1,1,-1,1,\\dots\\): neither.', '(c) Các số hạng là \\(-1,1,-1,1,\\dots\\): không tăng, không giảm.')],
  'Tăng / giảm / không đơn điệu.' if False else T('(a) increasing; (b) decreasing; (c) neither.', '(a) tăng; (b) giảm; (c) không đơn điệu.'))
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Bounded or not?', 'Bị chặn hay không?'),
  T('Is the sequence bounded? (a) \\(u_n=\\dfrac{2n+1}{n+1}\\); (b) \\(u_n=n^2\\).', 'Dãy số có bị chặn không? (a) \\(u_n=\\dfrac{2n+1}{n+1}\\); (b) \\(u_n=n^2\\).'),
  ('Rewrite the formula to see its range of values.', 'Biến đổi công thức để thấy khoảng giá trị.'),
  [T('(a) \\(u_n=2-\\dfrac{1}{n+1}\\). Since \\(0<\\dfrac1{n+1}\\le\\dfrac12\\), we get \\(\\dfrac32\\le u_n<2\\).', '(a) \\(u_n=2-\\dfrac{1}{n+1}\\). Vì \\(0<\\dfrac1{n+1}\\le\\dfrac12\\) nên \\(\\dfrac32\\le u_n<2\\).'),
   T('So (a) is bounded above and below (also \\(1\\le u_n\\lt 2\\) works for \\(n\\ge1\\)).', 'Vậy (a) bị chặn trên và bị chặn dưới.'),
   T('(b) \\(n^2\\ge1\\): bounded below, but \\(n^2\\) grows without limit, so not bounded above.', '(b) \\(n^2\\ge1\\): bị chặn dưới, nhưng \\(n^2\\) lớn tùy ý nên không bị chặn trên.')],
  T('(a) bounded; (b) not bounded (only bounded below).', '(a) bị chặn; (b) không bị chặn (chỉ bị chặn dưới).'))
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Seats in a theatre', 'Số ghế trong nhà hát'),
  T('A theatre has 20 seats in row 1 and each next row has 2 more seats. (a) How many seats are in row 10? (b) Which row has 50 seats?', 'Một nhà hát có 20 ghế ở hàng 1 và mỗi hàng sau nhiều hơn hàng trước 2 ghế. (a) Hàng 10 có bao nhiêu ghế? (b) Hàng nào có 50 ghế?'),
  ('Write the general term: \\(u_n=20+2(n-1)\\).', 'Viết số hạng tổng quát: \\(u_n=20+2(n-1)\\).'),
  [T('\\(u_n=20+2(n-1)=2n+18\\).', '\\(u_n=20+2(n-1)=2n+18\\).'),
   T('(a) \\(u_{10}=2\\cdot10+18=38\\).', '(a) \\(u_{10}=2\\cdot10+18=38\\).'),
   T('(b) \\(2n+18=50\\Rightarrow n=16\\).', '(b) \\(2n+18=50\\Rightarrow n=16\\).')],
  T('(a) 38 seats; (b) row 16.', '(a) 38 ghế; (b) hàng 16.'))

HN = ('Enter a whole number.', 'Nhập một số nguyên.')
Q1 = [
  [MCQ(1, ('A sequence has \\(u_n=3n-2\\). What is \\(u_4\\)?', 'Dãy số có \\(u_n=3n-2\\). Tính \\(u_4\\).'), ['7', '10', '12', '14'], 'b', ('Answer: b. \\(3\\cdot4-2=10\\).', 'Đáp án b. \\(3\\cdot4-2=10\\).')),
   MCQ(2, ('\\(u_1=2,\\ u_{n+1}=u_n+3\\). What is \\(u_4\\)?', '\\(u_1=2,\\ u_{n+1}=u_n+3\\). Tính \\(u_4\\).'), ['8', '9', '11', '14'], 'c', ('Answer: c. \\(2,5,8,11\\).', 'Đáp án c. \\(2,5,8,11\\).')),
   MCQ(3, ('Which describes \\(u_n=n+3\\)?', 'Dãy \\(u_n=n+3\\) là dãy nào?'), ['increasing', 'decreasing', 'neither', 'constant'], 'a', ('Answer: a. \\(u_{n+1}-u_n=1>0\\).', 'Đáp án a. \\(u_{n+1}-u_n=1>0\\).'))],
  [TF(4, ('The sequence \\(u_n=2n-1\\) is increasing.', 'Dãy số \\(u_n=2n-1\\) là dãy tăng.'), 'true', ('True: \\(u_{n+1}-u_n=2>0\\).', 'Đúng: \\(u_{n+1}-u_n=2>0\\).')),
   TF(5, ('The sequence \\(u_n=n^2\\) is bounded above.', 'Dãy số \\(u_n=n^2\\) bị chặn trên.'), 'false', ('False: \\(n^2\\) grows without limit.', 'Sai: \\(n^2\\) lớn tùy ý.'))],
  [SHORT(6, ('\\(u_1=1,\\ u_{n+1}=u_n+4\\). Find \\(u_5\\).', '\\(u_1=1,\\ u_{n+1}=u_n+4\\). Tìm \\(u_5\\).'), '17', 'number', HN, ('Answer: 17: \\(1,5,9,13,17\\).', 'Đáp số: 17: \\(1,5,9,13,17\\).')),
   SHORT(7, ('For \\(u_n=3n-2\\), which n gives \\(u_n=25\\)?', 'Với \\(u_n=3n-2\\), n bằng bao nhiêu để \\(u_n=25\\)?'), '9', 'number', HN, ('Answer: 9: \\(3n-2=25\\Rightarrow n=9\\).', 'Đáp số: 9: \\(3n-2=25\\Rightarrow n=9\\).'))]]
Q2 = [
  [MCQ(1, ('A sequence has \\(u_n=n^2+1\\). What is \\(u_5\\)?', 'Dãy số có \\(u_n=n^2+1\\). Tính \\(u_5\\).'), ['10', '25', '26', '36'], 'c', ('Answer: c. \\(25+1=26\\).', 'Đáp án c. \\(25+1=26\\).')),
   MCQ(2, ('\\(u_1=1,\\ u_{n+1}=2u_n+1\\). What is \\(u_4\\)?', '\\(u_1=1,\\ u_{n+1}=2u_n+1\\). Tính \\(u_4\\).'), ['7', '9', '15', '31'], 'c', ('Answer: c. \\(1,3,7,15\\).', 'Đáp án c. \\(1,3,7,15\\).')),
   MCQ(3, ('Which describes \\(u_n=\\dfrac1n\\)?', 'Dãy \\(u_n=\\dfrac1n\\) là dãy nào?'), ['increasing', 'decreasing', 'neither', 'constant'], 'b', ('Answer: b. \\(u_{n+1}-u_n=-\\dfrac{1}{n(n+1)}<0\\).', 'Đáp án b. \\(u_{n+1}-u_n=-\\dfrac{1}{n(n+1)}<0\\).'))],
  [TF(4, ('The sequence \\(u_n=\\dfrac{n}{n+1}\\) is decreasing.', 'Dãy số \\(u_n=\\dfrac{n}{n+1}\\) là dãy giảm.'), 'false', ('False: it is increasing, \\(u_{n+1}-u_n=\\dfrac{1}{(n+1)(n+2)}>0\\).', 'Sai: nó là dãy tăng, \\(u_{n+1}-u_n=\\dfrac{1}{(n+1)(n+2)}>0\\).')),
   TF(5, ('The sequence \\(u_n=\\dfrac1n\\) is bounded.', 'Dãy số \\(u_n=\\dfrac1n\\) bị chặn.'), 'true', ('True: \\(0<u_n\\le1\\).', 'Đúng: \\(0<u_n\\le1\\).'))],
  [SHORT(6, ('\\(u_1=3,\\ u_{n+1}=2u_n\\). Find \\(u_4\\).', '\\(u_1=3,\\ u_{n+1}=2u_n\\). Tìm \\(u_4\\).'), '24', 'number', HN, ('Answer: 24: \\(3,6,12,24\\).', 'Đáp số: 24: \\(3,6,12,24\\).')),
   SHORT(7, ('For \\(u_n=2n+5\\), which n gives \\(u_n=31\\)?', 'Với \\(u_n=2n+5\\), n bằng bao nhiêu để \\(u_n=31\\)?'), '13', 'number', HN, ('Answer: 13: \\(2n+5=31\\Rightarrow n=13\\).', 'Đáp số: 13: \\(2n+5=31\\Rightarrow n=13\\).'))]]
Q3 = [
  [MCQ(1, ('A sequence has \\(u_n=2^n-1\\). What is \\(u_5\\)?', 'Dãy số có \\(u_n=2^n-1\\). Tính \\(u_5\\).'), ['9', '15', '31', '63'], 'c', ('Answer: c. \\(32-1=31\\).', 'Đáp án c. \\(32-1=31\\).')),
   MCQ(2, ('\\(u_1=2,\\ u_{n+1}=3u_n-1\\). What is \\(u_4\\)?', '\\(u_1=2,\\ u_{n+1}=3u_n-1\\). Tính \\(u_4\\).'), ['14', '27', '41', '122'], 'c', ('Answer: c. \\(2,5,14,41\\).', 'Đáp án c. \\(2,5,14,41\\).')),
   MCQ(3, ('Which describes \\(u_n=(-1)^n\\)?', 'Dãy \\(u_n=(-1)^n\\) là dãy nào?'), ['increasing', 'decreasing', 'neither increasing nor decreasing', 'constant'], 'c', ('Answer: c. The terms are \\(-1,1,-1,1,\\dots\\)', 'Đáp án c. Các số hạng là \\(-1,1,-1,1,\\dots\\)'))],
  [TF(4, ('The sequence \\(u_n=(-1)^n\\) is bounded.', 'Dãy số \\(u_n=(-1)^n\\) bị chặn.'), 'true', ('True: \\(-1\\le u_n\\le1\\).', 'Đúng: \\(-1\\le u_n\\le1\\).')),
   TF(5, ('The sequence \\(u_n=-n\\) is bounded above.', 'Dãy số \\(u_n=-n\\) bị chặn trên.'), 'true', ('True: \\(u_n\\le-1\\) for every n.', 'Đúng: \\(u_n\\le-1\\) với mọi n.'))],
  [SHORT(6, ('Fibonacci: \\(u_1=u_2=1,\\ u_{n+2}=u_{n+1}+u_n\\). Find \\(u_7\\).', 'Dãy Fibonacci: \\(u_1=u_2=1,\\ u_{n+2}=u_{n+1}+u_n\\). Tìm \\(u_7\\).'), '13', 'number', HN, ('Answer: 13: \\(1,1,2,3,5,8,13\\).', 'Đáp số: 13: \\(1,1,2,3,5,8,13\\).')),
   SHORT(7, ('For \\(u_n=n^2-1\\), which positive n gives \\(u_n=80\\)?', 'Với \\(u_n=n^2-1\\), số nguyên dương n nào cho \\(u_n=80\\)?'), '9', 'number', HN, ('Answer: 9: \\(n^2=81\\).', 'Đáp số: 9: \\(n^2=81\\).'))]]
practice = LEVEL_PRACTICE([('A. Multiple Choice', 'A. Trắc nghiệm'), ('B. True or False', 'B. Đúng hoặc sai'), ('C. Short Answer', 'C. Trả lời ngắn')], {1: Q1, 2: Q2, 3: Q3})

mistakes = [
 ('<b>Index shift.</b> Taking \\(u_0\\) as the first term. Here the first term is \\(u_1\\).', '<b>Lệch chỉ số.</b> Coi \\(u_0\\) là số hạng đầu. Ở đây số hạng đầu là \\(u_1\\).'),
 ('<b>Recursive formula.</b> Using \\(u_n\\) instead of \\(u_{n-1}\\) or mixing \\(u_{n+1}\\) with \\(u_n+1\\). \\(u_{n+1}\\) means the next term.', '<b>Công thức truy hồi.</b> Nhầm \\(u_{n+1}\\) với \\(u_n+1\\). \\(u_{n+1}\\) là số hạng kế tiếp.'),
 ('<b>A few terms are not a proof.</b> Trying \\(n=1,2,3\\) and saying the sequence is increasing.', '<b>Vài số hạng chưa là chứng minh.</b> Thử \\(n=1,2,3\\) rồi kết luận dãy tăng.'),
 ('<b>Wrong sign.</b> Mistakes in \\(u_{n+1}-u_n\\). Write \\(u_{n+1}\\) fully by replacing n with \\(n+1\\).', '<b>Sai dấu.</b> Sai khi tính \\(u_{n+1}-u_n\\). Viết đầy đủ \\(u_{n+1}\\) bằng cách thay n bằng \\(n+1\\).'),
 ('<b>Bounded.</b> Saying \\(u_n=n^2\\) is bounded because it has a smallest term. It must be bounded above and below.', '<b>Bị chặn.</b> Cho rằng \\(u_n=n^2\\) bị chặn vì có số hạng nhỏ nhất. Phải bị chặn cả trên và dưới.'),
]
summary = [
 ('A sequence is a function on the positive integers; it is given by a formula, a description or a recursive formula.', 'Dãy số là hàm số trên tập các số nguyên dương; cho bằng công thức, bằng mô tả hoặc bằng công thức truy hồi.'),
 ('Increasing: \\(u_{n+1}>u_n\\) for all n; decreasing: \\(u_{n+1}<u_n\\) for all n. Study the sign of \\(u_{n+1}-u_n\\).', 'Tăng: \\(u_{n+1}>u_n\\) với mọi n; giảm: \\(u_{n+1}<u_n\\) với mọi n. Xét dấu \\(u_{n+1}-u_n\\).'),
 ('Bounded above: \\(u_n\\le M\\); bounded below: \\(u_n\\ge m\\); bounded: both.', 'Bị chặn trên: \\(u_n\\le M\\); bị chặn dưới: \\(u_n\\ge m\\); bị chặn: cả hai.'),
 ('Key English phrases: find the first five terms; find the general term; is the sequence increasing or decreasing; is the sequence bounded.', 'Cụm tiếng Anh cần nhớ: find the first five terms (tìm năm số hạng đầu); find the general term (tìm số hạng tổng quát); increasing or decreasing (tăng hay giảm); bounded (bị chặn).'),
]
checks = [
 ('I can find terms of a sequence from a formula or a recursive formula.', 'Tôi tìm được số hạng của dãy từ công thức hoặc công thức truy hồi.'),
 ('I can decide whether a sequence is increasing or decreasing.', 'Tôi xét được dãy số tăng hay giảm.'),
 ('I can decide whether a sequence is bounded.', 'Tôi xét được dãy số có bị chặn hay không.'),
 STD_SUMMARY_CHECK_EN(),
]

lesson(id=LID, title_en='Sequences', title_vi='Dãy số', topic=TOPIC,
       folder='sequences', file='sequences',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Sequences: formula and recursive definitions, increasing/decreasing and bounded sequences.', level='Intermediate', minutes=60,
       description_vi='Bài 5 – Dãy số: cho bằng công thức, truy hồi; dãy số tăng, giảm; dãy số bị chặn.',
       tags_vi=['dãy số', 'số hạng tổng quát', 'công thức truy hồi', 'dãy số tăng', 'dãy số giảm', 'dãy số bị chặn'],
       prerequisites=['g11-functions-01'], tags=['sequence', 'general term', 'recursive formula', 'increasing', 'decreasing', 'bounded'], order=36)
