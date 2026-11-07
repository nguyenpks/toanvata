# -*- coding: utf-8 -*-
"""g10-prob-02 = Toán 10 KNTT, Bài 27: Thực hành tính xác suất theo định nghĩa cổ điển. Mã ngân hàng câu hỏi: TOAN10-C9-B27."""
import os, sys, math, itertools, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g10j as S
import mb_pgf

C = math.comb
D2 = list(itertools.product(range(1, 7), repeat=2))
CV = 'Thực hành tính xác suất'
vocab = defs(CV, [
 ('relfreq2', 'experimental frequency', 'tần suất thực nghiệm', 'the number of times an event occurs divided by the number of trials.', 'số lần biến cố xảy ra chia cho số lần thử.', 'The experimental frequency of a six is 0.165.', '\\(\\dfrac{k}{N}\\)'),
 ('simul', 'simulation', 'mô phỏng', 'imitating a random experiment many times (with a computer or a spreadsheet).', 'bắt chước một phép thử ngẫu nhiên nhiều lần (bằng máy tính, bảng tính).', 'We simulate 600 rolls of a die.', ''),
 ('equlik', 'equally likely', 'đồng khả năng', 'having the same chance of occurring.', 'có cùng khả năng xảy ra.', 'The 36 outcomes are equally likely.', '')])
goals = [('list the outcomes of an experiment with tables and tree diagrams;', 'liệt kê kết quả của phép thử bằng bảng, sơ đồ hình cây;'),
         ('compute probabilities by listing and by combinations;', 'tính xác suất bằng phương pháp liệt kê và bằng tổ hợp;'),
         ('run or read a simulation and compare the [[tần suất thực nghiệm]] with the probability;', 'thực hiện hoặc đọc kết quả [[mô phỏng]], so sánh [[tần suất thực nghiệm]] với xác suất;'),
         ('analyse simple games of chance.', 'phân tích các trò chơi may rủi đơn giản.')]
goals[2] = ('run or read a simulation and compare the experimental frequency with the probability;', goals[2][1])
phrases = [('<b>Draw a tree with three levels.</b>', 'Vẽ sơ đồ cây ba tầng.'), ('<b>Each branch is equally likely.</b>', 'Mỗi nhánh đồng khả năng.'),
           ('<b>The experimental frequency gets closer to the probability.</b>', 'Tần suất thực nghiệm tiến gần đến xác suất.'), ('<b>We repeated the experiment six hundred times.</b>', 'Chúng ta lặp lại phép thử 600 lần.'), ('<b>The game is not fair.</b>', 'Trò chơi không công bằng.')]
review = T('From Bài 26: \\(P(A)=\\dfrac{n(A)}{n(\\Omega)}\\), \\(P(\\overline A)=1-P(A)\\). From Bài 23: tree diagrams.', 'Từ Bài 26: \\(P(A)=\\dfrac{n(A)}{n(\\Omega)}\\), \\(P(\\overline A)=1-P(A)\\). Từ Bài 23: sơ đồ hình cây.')
theory = '<h3>27.1 %s</h3>' % TI('Listing outcomes', 'Liệt kê kết quả')
theory += BOX('blue', ('Tools', 'Công cụ'), UL([T('<b>Table</b> for two stages (two dice, a coin and a die).', '<b>Bảng</b> cho phép thử hai bước (hai xúc xắc, một đồng xu và một xúc xắc).'), T('<b>Tree diagram</b> for several stages (three coins, three children).', '<b>Sơ đồ cây</b> cho phép thử nhiều bước (ba đồng xu, ba người con).'),
  T('<b>Combinations</b> when the list is too long (drawing balls, choosing people).', '<b>Tổ hợp</b> khi danh sách quá dài (lấy cầu, chọn người).')]))
tree = mb_pgf.raw_svg(r'''\begin{tikzpicture}[grow=right, level distance=2.3cm, level 1/.style={sibling distance=3.2cm}, level 2/.style={sibling distance=1.6cm}, level 3/.style={sibling distance=0.8cm},
  every node/.style={font=\small, text=ink}, edge from parent/.style={draw=ink!60, line width=0.6pt}]
\node[circle, fill=ink, inner sep=1.5pt] {}
  child {node {N} child {node {N} child {node {N \quad NNN}} child {node {S \quad NNS}}} child {node {S} child {node {N \quad NSN}} child {node {S \quad NSS}}}}
  child {node {S} child {node {N} child {node {N \quad SNN}} child {node {S \quad SNS}}} child {node {S} child {node {N \quad SSN}} child {node {S \quad SSS}}}};
\end{tikzpicture}''')
theory += mb_pgf.img(tree, 'Tree diagram of three coin tosses with 8 outcomes', 440, TI('Three coin tosses (S = head, N = tail): 8 equally likely outcomes.', 'Gieo đồng xu ba lần (S: sấp, N: ngửa): 8 kết quả đồng khả năng.'))
theory += '<h3>27.2 %s</h3>' % TI('Simulation and experimental frequency', 'Mô phỏng và tần suất thực nghiệm')
theory += BOX('mint', ('Idea', 'Ý tưởng'), T('Repeat an experiment \\(N\\) times; if \\(A\\) occurs \\(k\\) times, its experimental frequency is \\(\\dfrac kN\\). When \\(N\\) is large, \\(\\dfrac kN\\) is usually close to \\(P(A)\\) (but rarely equal to it).', 'Lặp lại phép thử \\(N\\) lần; nếu \\(A\\) xảy ra \\(k\\) lần thì tần suất thực nghiệm là \\(\\dfrac kN\\). Khi \\(N\\) lớn, \\(\\dfrac kN\\) thường gần \\(P(A)\\) (nhưng hiếm khi bằng đúng).'))
rr = random.Random(5); cnt = 0; pts = []
for n in range(1, 601):
    cnt += rr.randint(1, 6) == 6
    if n % 5 == 0: pts.append((n, cnt / n))
assert cnt == 99
plot = mb_pgf.raw_svg(r'''\begin{tikzpicture}\begin{axis}[scale only axis, width=9.5cm, height=4.6cm, xmin=0, xmax=600, ymin=0, ymax=0.35, axis lines=left,
 axis line style={draw=ink!85, -{Stealth[length=2.2mm]}}, xlabel={$N$}, ylabel={$k/N$}, grid=major, major grid style={draw=gray!16}, ticklabel style={font=\footnotesize},
 yticklabel style={/pgf/number format/fixed}, legend style={at={(0.98,0.95)}, anchor=north east, draw=none, fill=white, font=\small}]
\addplot[color={rgb,255:red,4;green,107;blue,77}, line width=1.1pt] coordinates {''' + ' '.join('(%d,%.4f)' % p for p in pts) + r'''};
\addlegendentry{tần suất / frequency}
\addplot[guide, domain=0:600, samples=2] {1/6}; \addlegendentry{$P=\frac16$}
\end{axis}\end{tikzpicture}''')
theory += mb_pgf.img(plot, 'Experimental frequency of a six over 600 simulated rolls approaching 1/6', 560, TI('Simulation of 600 rolls: the frequency of a six wobbles at first, then settles near \\(\\frac16\\approx0{,}167\\) (here 99 sixes: 0,165).', 'Mô phỏng 600 lần gieo: tần suất mặt 6 dao động lúc đầu, sau đó ổn định gần \\(\\frac16\\approx0{,}167\\) (ở đây có 99 lần: 0,165).'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('A simulation never <i>proves</i> a probability; it only estimates it. "After 5 tails, a head is more likely" is false: the coin has no memory.', 'Mô phỏng không <i>chứng minh</i> xác suất mà chỉ ước lượng. "Sau 5 lần ngửa thì lần sau dễ ra sấp hơn" là sai: đồng xu không có trí nhớ.'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Three coins', 'Ba đồng xu'), T('A coin is tossed three times. Find the probability of exactly two heads, and of at least one head.', 'Gieo một đồng xu ba lần. Tính xác suất có đúng hai lần sấp, và có ít nhất một lần sấp.'),
  T('Use the tree: 8 outcomes.', 'Dùng sơ đồ cây: 8 kết quả.'), [T('Exactly two heads: \\(SSN, SNS, NSS\\): \\(\\frac38\\).', 'Đúng hai lần sấp: \\(SSN, SNS, NSS\\): \\(\\frac38\\).'), T('At least one head: \\(1-P(NNN)=1-\\frac18\\).', 'Ít nhất một lần sấp: \\(1-P(NNN)=1-\\frac18\\).')], T('\\(\\dfrac38\\) and \\(\\dfrac78\\).', '\\(\\dfrac38\\) và \\(\\dfrac78\\).'))
assert sum(a * b % 2 == 1 for a, b in D2) == 9
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('An even product', 'Tích chẵn'), T('Two dice are rolled. Find the probability that the product of the numbers is even.', 'Gieo hai con xúc xắc. Tính xác suất tích số chấm là số chẵn.'),
  T('Complement: the product is odd \\(\\iff\\) both numbers odd.', 'Biến cố đối: tích lẻ \\(\\iff\\) cả hai số đều lẻ.'), [T('Both odd: \\(3\\cdot3=9\\) outcomes.', 'Cả hai lẻ: \\(3\\cdot3=9\\) kết quả.'), T('\\(P=1-\\frac9{36}=\\frac{27}{36}\\).', '\\(P=1-\\frac9{36}=\\frac{27}{36}\\).')], T('\\(\\dfrac34\\).', '\\(\\dfrac34\\).'))
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Three children', 'Gia đình ba con'), T('A family has three children; assume boy and girl are equally likely and independent. Find the probability of at least two girls.', 'Một gia đình có ba con; giả sử khả năng sinh con trai, con gái như nhau và độc lập. Tính xác suất có ít nhất hai con gái.'),
  T('Same tree as three coins (G/B).', 'Cùng sơ đồ cây với ba đồng xu (G/T).'), [T('Two girls: 3 outcomes; three girls: 1 outcome.', 'Hai con gái: 3 kết quả; ba con gái: 1 kết quả.')], T('\\(\\dfrac48=\\dfrac12\\).', '\\(\\dfrac48=\\dfrac12\\).'))
assert F(C(5, 2) + C(4, 2), C(9, 2)) == F(4, 9)
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('An even sum of two cards', 'Tổng chẵn của hai thẻ'), T('Nine cards are numbered 1–9. Two cards are drawn. Find the probability that the sum is even.', 'Có 9 tấm thẻ đánh số từ 1 đến 9. Rút ngẫu nhiên hai thẻ. Tính xác suất tổng hai số là số chẵn.'),
  T('Even sum: both odd or both even.', 'Tổng chẵn: hai số cùng lẻ hoặc cùng chẵn.'), [T('\\(n(\\Omega)=C_9^2=36\\); both odd \\(C_5^2=10\\), both even \\(C_4^2=6\\).', '\\(n(\\Omega)=C_9^2=36\\); cùng lẻ \\(C_5^2=10\\), cùng chẵn \\(C_4^2=6\\).')], T('\\(\\dfrac{16}{36}=\\dfrac49\\).', '\\(\\dfrac{16}{36}=\\dfrac49\\).'))
assert sum(a + b == 7 for a, b in D2) == 6 and sum(a + b == 2 for a, b in D2) == 1
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Is the game fair?', 'Trò chơi có công bằng không?'), T('Two players roll two dice. An wins if the sum is 7; Bình wins if the sum is 2, 3 or 12. Who is more likely to win? Check with the simulation idea.', 'Hai bạn gieo hai con xúc xắc. An thắng nếu tổng bằng 7; Bình thắng nếu tổng bằng 2, 3 hoặc 12. Bạn nào có khả năng thắng cao hơn? Kiểm tra bằng ý tưởng mô phỏng.'),
  T('Count in the 36-cell table.', 'Đếm trong bảng 36 ô.'), [T('Sum 7: 6 outcomes, \\(P=\\frac6{36}\\).', 'Tổng 7: 6 kết quả, \\(P=\\frac6{36}\\).'), T('Sums 2, 3, 12: \\(1+2+1=4\\) outcomes, \\(P=\\frac4{36}\\).', 'Tổng 2, 3, 12: \\(1+2+1=4\\) kết quả, \\(P=\\frac4{36}\\).'), T('In 360 rounds we expect about 60 wins for An and 40 for Bình.', 'Trong 360 ván, dự kiến An thắng khoảng 60 ván, Bình khoảng 40 ván.')],
  T('An is more likely to win: the game is not fair.', 'An có khả năng thắng cao hơn: trò chơi không công bằng.'))
examples = EXFIG(examples, 1, mb_pgf.img(tree, 'Tree of three coin tosses', 400))


def lvl(P):
    m = P['max']; k1 = sum(max(a, b) == m for a, b in D2)
    o1 = M4(1, 'Two dice are rolled. P(the larger number is %d) =…' % m, 'Gieo hai con xúc xắc. Xác suất số chấm lớn nhất bằng %d là…' % m, '\\(%s\\)' % fr(F(k1, 36)),
            ['\\(%s\\)' % fr(F(1, 6)), '\\(%s\\)' % fr(F(m, 36)), '\\(%s\\)' % fr(F(2 * m, 36))], '%d outcomes.' % k1, 'Có \\(2\\cdot%d-1=%d\\) kết quả thuận lợi.' % (m, k1))
    d = P['diff']; k2 = sum(abs(a - b) == d for a, b in D2)
    o2 = M4(2, 'Two dice are rolled. P(the difference is %d) =…' % d, 'Gieo hai con xúc xắc. Xác suất hiệu số chấm (lớn trừ nhỏ) bằng %d là…' % d, '\\(%s\\)' % fr(F(k2, 36)),
            ['\\(%s\\)' % fr(F(6 - d, 36)), '\\(%s\\)' % fr(F(1, 6)) if F(k2, 36) != F(1, 6) else '\\(%s\\)' % fr(F(1, 9)), '\\(%s\\)' % fr(F(k2 + 2, 36))], '%d outcomes.' % k2, 'Có %d cặp thỏa mãn.' % k2)
    n = P['adj']
    o3 = M4(3, '%d students including An and Bình line up at random. P(An and Bình are adjacent) =…' % n, '%d học sinh, trong đó có An và Bình, xếp hàng ngẫu nhiên. Xác suất An và Bình đứng cạnh nhau là…' % n, '\\(%s\\)' % fr(F(2, n)),
            ['\\(%s\\)' % fr(F(1, n)), '\\(%s\\)' % fr(F(2, n - 1)), '\\(%s\\)' % fr(F(1, n - 1))], '\\(\\dfrac{2(n-1)!}{n!}\\).', '\\(\\dfrac{2\\cdot(%d-1)!}{%d!}=%s\\).' % (n, n, fr(F(2, n))))
    (se, sv), v4 = P['kids']
    t4 = tf(4, se, sv, v4, 'Use the 8-branch tree.', 'Dùng sơ đồ cây 8 nhánh.')
    (te, tv), v5 = P['sim']
    t5 = tf(5, te, tv, v5, 'Frequency estimates probability.', 'Tần suất chỉ ước lượng xác suất, dao động quanh xác suất khi số lần thử lớn.')
    (fe, fv), k6 = P['fav']
    s6 = sh(6, fe, fv, k6, 'Count in the table.', 'Đếm trong bảng 36 ô.')
    (ee, ev), k7 = P['exp']
    s7 = sh(7, ee, ev, k7, 'Expected count \\(\\approx N\\cdot P\\).', 'Số lần dự kiến \\(\\approx N\\cdot P\\).')
    return [[o1, o2, o3], [t4, t5], [s6, s7]]


assert sum(a + b == 9 for a, b in D2) == 4 and sum(a * b == 12 for a, b in D2) == 4 and sum(abs(a - b) == 1 for a, b in D2) == 10
PP = [dict(max=4, diff=2, adj=5, kids=(('Family with 3 children: P(all girls) = 1/8.', 'Gia đình 3 con: xác suất cả ba là con gái bằng \\(\\frac18\\).'), True),
           sim=(('After 1000 rolls the frequency of a six must be exactly 1/6.', 'Sau 1000 lần gieo, tần suất mặt 6 chấm phải đúng bằng \\(\\frac16\\).'), False),
           fav=(('Two dice are rolled. How many outcomes give a sum of 9?', 'Gieo hai con xúc xắc. Có bao nhiêu kết quả cho tổng bằng 9?'), 4),
           exp=(('A die is rolled 600 times. About how many sixes do we expect?', 'Gieo một con xúc xắc 600 lần. Dự kiến có khoảng bao nhiêu lần ra mặt 6?'), 100)),
      dict(max=5, diff=1, adj=6, kids=(('Family with 3 children: P(exactly one boy) = 1/3.', 'Gia đình 3 con: xác suất có đúng một con trai bằng \\(\\frac13\\).'), False),
           sim=(('When the number of trials grows, the experimental frequency tends to get close to the probability.', 'Khi số lần thử tăng, tần suất thực nghiệm có xu hướng tiến gần đến xác suất.'), True),
           fav=(('Two dice are rolled. How many outcomes give a product of 12?', 'Gieo hai con xúc xắc. Có bao nhiêu kết quả cho tích bằng 12?'), 4),
           exp=(('Two coins are tossed 300 times. About how many times do we expect two heads?', 'Gieo hai đồng xu 300 lần. Dự kiến có khoảng bao nhiêu lần cả hai đều sấp?'), 75)),
      dict(max=2, diff=3, adj=4, kids=(('Family with 3 children: P(at least one boy) = 7/8.', 'Gia đình 3 con: xác suất có ít nhất một con trai bằng \\(\\frac78\\).'), True),
           sim=(('After 5 tails in a row, the next toss is more likely to be a head.', 'Sau 5 lần ngửa liên tiếp, lần gieo tiếp theo dễ ra mặt sấp hơn.'), False),
           fav=(('Two dice are rolled. How many outcomes have numbers differing by 1?', 'Gieo hai con xúc xắc. Có bao nhiêu kết quả mà hai số chấm hơn kém nhau 1?'), 10),
           exp=(('Two dice are rolled 360 times. About how many times do we expect a sum of 7?', 'Gieo hai con xúc xắc 360 lần. Dự kiến có khoảng bao nhiêu lần tổng bằng 7?'), 60))]
practice = three(lvl, PP)
practice = with_self(practice, S.M27S10, start=8)
mistakes = [('<b>Forgetting the order in a tree.</b> \\(SSN\\), \\(SNS\\), \\(NSS\\) are three different outcomes.', '<b>Bỏ qua thứ tự trong sơ đồ cây.</b> \\(SSN\\), \\(SNS\\), \\(NSS\\) là ba kết quả khác nhau.'),
            ('<b>Expecting a simulation to give exactly the probability.</b> It gives an estimate.', '<b>Mong mô phỏng cho đúng bằng xác suất.</b> Mô phỏng chỉ cho giá trị ước lượng.'),
            ('<b>"Gambler\'s fallacy".</b> Independent tosses do not remember the past.', '<b>"Ảo tưởng của người chơi".</b> Các lần gieo độc lập không "nhớ" kết quả trước.'),
            ('<b>Listing outcomes that are not equally likely.</b> "0, 1, 2, 3 heads" are not equally likely.', '<b>Liệt kê các kết quả không đồng khả năng.</b> "0, 1, 2, 3 lần sấp" không đồng khả năng.')]
summary = [('Tables for 2 stages, trees for several stages, combinations for large counts.', 'Bảng cho phép thử 2 bước, sơ đồ cây cho nhiều bước, tổ hợp khi số lượng lớn.'), ('\\(P(A)=\\dfrac{n(A)}{n(\\Omega)}\\); use the complement when easier.', '\\(P(A)=\\dfrac{n(A)}{n(\\Omega)}\\); dùng biến cố đối khi thuận tiện.'),
           ('Simulation: frequency \\(\\dfrac kN\\approx P(A)\\) for large \\(N\\); expected count \\(\\approx N\\cdot P(A)\\).', 'Mô phỏng: tần suất \\(\\dfrac kN\\approx P(A)\\) khi \\(N\\) lớn; số lần dự kiến \\(\\approx N\\cdot P(A)\\).'), ('Key words: tree diagram, simulation, frequency, fair game.', 'Từ cần nhớ: tree diagram, simulation, frequency, fair game.')]
checks = [('I can list outcomes with a tree or a table.', 'Em liệt kê được kết quả bằng sơ đồ cây hoặc bảng.'), ('I can compute probabilities by listing.', 'Em tính được xác suất bằng liệt kê.'), ('I can read a simulation.', 'Em đọc được kết quả mô phỏng.'), ('I can decide if a game is fair.', 'Em đánh giá được trò chơi có công bằng không.')]
LL('g10-prob-02', 'Practice: Computing Classical Probabilities', CV, ('Classical Probability', 'Xác suất theo định nghĩa cổ điển'), 'probability', 'probability-practice', 270, 'Intermediate', 60, ('classical probability', 'định nghĩa cổ điển của xác suất'),
   'Listing outcomes with tables and trees, combinations, simulation and experimental frequency, fair games.', 'Bài 27 – Liệt kê kết quả bằng bảng, sơ đồ cây; dùng tổ hợp; mô phỏng và tần suất thực nghiệm; trò chơi công bằng.',
   ['tree diagram', 'simulation', 'frequency'], ['sơ đồ cây', 'mô phỏng', 'tần suất'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g10-prob-01'])
