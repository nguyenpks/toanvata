# -*- coding: utf-8 -*-
"""Nội dung bài g9-probability-01 = Toán 9 KNTT, Bài 25: Phép thử ngẫu nhiên và không gian mẫu – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 8 – Lesson 25."""
import os, sys, itertools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9, sp_g9p
from chart_g9 import BI

LID = 'g9-probability-01'
CH = 'Xác suất'
TOPIC = ('Probability', 'Xác suất của biến cố trong một số mô hình xác suất đơn giản')
ensure_vocab([
 ('g9-outcome', 'outcome', 'kết quả có thể (của phép thử)', CH, 'Rolling a die has six possible outcomes.', ''),
 ('g9-coin-toss', 'coin toss', 'gieo đồng xu (phép thử)', CH, 'In a coin toss the outcomes are heads (H) and tails (T).', ''),
 ('g9-die', 'die (plural: dice)', 'con xúc xắc (phép thử)', CH, 'Roll a die and read the number on top.', ''),
])
load_vocab()
setx, pair = sp_g9p.setx, sp_g9p.pair

# ---------- số liệu (kiểm tra bằng máy) ----------
C2 = [a + b for a in 'NS' for b in 'NS']; C2E = [a + b for a in 'HT' for b in 'HT']
assert C2 == ['NN', 'NS', 'SN', 'SS'] and len(C2E) == 4
D2 = [(i, j) for i in range(1, 7) for j in range(1, 7)]; assert len(D2) == 36 and (2, 5) in D2 and (5, 2) in D2
BALLS = [('R', 'Đ'), ('B', 'X'), ('Y', 'V')]                              # đỏ, xanh, vàng
NR = list(itertools.permutations(range(3), 2)); assert len(NR) == 6 and all(a != b for a, b in NR)
DISH = [('rice', 'cơm'), ('pho', 'phở'), ('noodle soup', 'bún')]; DRK = [('iced tea', 'trà đá'), ('orange juice', 'nước cam')]
assert len(DISH) * len(DRK) == 6 and len(DISH) * len(DRK) * 2 == 12

def TREE(l1, l2, outs, head, cap, px=430):
    fe = sp_g9p.tree_svg(l1[0], l2[0], outs[0], head[0]); fv = sp_g9p.tree_svg(l1[1], l2[1], outs[1], head[1])
    return '<figure class="mbl-fig mbl-figtex">%s<figcaption>%s</figcaption></figure>' % (BI(fe, fv, 'Tree diagram', 'Sơ đồ hình cây', px), TI(*cap))

TREE_COIN = TREE((['H', 'T'], ['N', 'S']), ([['H', 'T']] * 2, [['N', 'S']] * 2), (C2E, C2), (('Coin 1', 'Coin 2', 'Outcome'), ('Đồng xu 1', 'Đồng xu 2', 'Kết quả')),
                 ('Tossing two coins: 4 outcomes', 'Gieo hai đồng xu: 4 kết quả'))
TREE_BALL = TREE(([b[0] for b in BALLS], [b[1] for b in BALLS]),
                 ([[BALLS[j][0] for j in range(3) if j != i] for i in range(3)], [[BALLS[j][1] for j in range(3) if j != i] for i in range(3)]),
                 (['(%s; %s)' % (BALLS[a][0], BALLS[b][0]) for a, b in NR], ['(%s; %s)' % (BALLS[a][1], BALLS[b][1]) for a, b in NR]),
                 (('1st ball', '2nd ball', 'Outcome'), ('Lần 1', 'Lần 2', 'Kết quả')), ('Taking two balls without putting back: 6 outcomes', 'Lấy hai quả bóng không trả lại: 6 kết quả'))
TREE_MENU = TREE(([d[0] for d in DISH], [d[1] for d in DISH]), ([[k[0] for k in DRK]] * 3, [[k[1] for k in DRK]] * 3),
                 ([d[0] + ', ' + k[0] for d in DISH for k in DRK], [d[1] + ', ' + k[1] for d in DISH for k in DRK]),
                 (('Dish', 'Drink', 'Outcome'), ('Món ăn', 'Đồ uống', 'Kết quả')), ('Choosing a dish and a drink: 6 outcomes', 'Chọn món ăn và đồ uống: 6 kết quả'))

def DICE():
    h = '<tr><th scope="col">%s</th>%s</tr>' % (TI('Die 1 \\ Die 2', 'Xúc xắc 1 \\ Xúc xắc 2'), ''.join('<th scope="col">%d</th>' % j for j in range(1, 7)))
    b = ''.join('<tr><th scope="row">%d</th>%s</tr>' % (i, ''.join('<td>\\((%d;\\,%d)\\)</td>' % (i, j) for j in range(1, 7))) for i in range(1, 7))
    return '<div class="mbl-tablewrap mbl-freqwrap"><table class="mbl-table mbl-freq"><tbody>%s%s</tbody></table></div>' % (h, b)

meta = dict(level=('Basic', 'Cơ bản'), time=('about 60 minutes', '60 phút'), before=('Experimental probability (grades 6–8)', 'Xác suất thực nghiệm (lớp 6–8)'))
goals = [
 (r'recognize a random experiment and its possible outcomes;', r'nhận biết được phép thử ngẫu nhiên và các kết quả có thể của nó;'),
 (r'describe the sample space \(\Omega\) of a simple experiment (coin, die, cards);', r'mô tả được không gian mẫu \(\Omega\) của phép thử đơn giản (đồng xu, xúc xắc, rút thẻ);'),
 (r'describe the sample space of a two-step experiment with a table or a tree diagram;', r'mô tả được không gian mẫu của phép thử hai bước bằng bảng hoặc sơ đồ hình cây;'),
 (r'count the outcomes in real situations (menus, codes).', r'đếm được số kết quả trong tình huống thực tế (chọn món, mã số).')]
vocab = [
 (r'<b>random experiment</b> – an action whose outcome we cannot know in advance, although we know all its possible outcomes.', r'[[Phép thử ngẫu nhiên]] – hoạt động mà ta không biết trước được kết quả, nhưng biết tất cả các kết quả có thể.'),
 (r'<b>outcome</b> – a possible result of the experiment.', r'[[Kết quả có thể|kết quả có thể (của phép thử)]] – một kết quả có thể xảy ra của phép thử.'),
 (r'<b>sample space</b> \(\Omega\) – the set of all possible outcomes.', r'[[Không gian mẫu]] \(\Omega\) – tập hợp tất cả các kết quả có thể của phép thử.'),
 (r'<b>coin toss / die (dice)</b> – heads (H), tails (T); a die has faces 1 to 6.', r'[[Gieo đồng xu|gieo đồng xu (phép thử)]] / [[con xúc xắc|con xúc xắc (phép thử)]] – mặt ngửa (N), mặt sấp (S); xúc xắc có các mặt 1 đến 6 chấm.'),
 (r'<b>ordered pair / tree diagram</b> – an outcome \((a;\,b)\) of a two-step experiment; a diagram of branches listing all outcomes.', r'[[Cặp số|cặp số]] có thứ tự / [[sơ đồ hình cây]] – kết quả \((a;\,b)\) của phép thử hai bước; sơ đồ các nhánh liệt kê mọi kết quả.')]
phrases = [
 (r'<b>Rolling a die is a random experiment.</b>', r'Gieo một con xúc xắc là một phép thử ngẫu nhiên.'),
 (r'<b>List all the possible outcomes.</b>', r'Liệt kê tất cả các kết quả có thể.'),
 (r'<b>The sample space is \(\Omega=\{H;\,T\}\).</b>', r'Không gian mẫu là \(\Omega=\{N;\,S\}\).'),
 (r'<b>Draw a tree diagram to show the sample space.</b>', r'Vẽ sơ đồ hình cây để mô tả không gian mẫu.'),
 (r'<b>The sample space has 36 outcomes.</b>', r'Không gian mẫu có 36 kết quả.')]
review = (T(r'<b>Grades 6–8.</b> We did experiments (tossing coins, rolling dice) many times and counted how often each result appeared.', r'<b>Lớp 6–8.</b> Ta đã làm thí nghiệm (tung đồng xu, gieo xúc xắc) nhiều lần và đếm số lần xuất hiện của mỗi kết quả.') +
          T(r'<b>Sets.</b> A set is written with braces: \(\{1;\,2;\,3\}\).', r'<b>Tập hợp.</b> Tập hợp được viết trong dấu ngoặc nhọn: \(\{1;\,2;\,3\}\).'))

theory = '<h3>5.1 %s</h3>' % TI('Random experiments', 'Phép thử ngẫu nhiên')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'An action or an experiment whose outcome <b>cannot be known in advance</b>, although we know <b>all its possible outcomes</b>, is called a <b>random experiment</b>.',
    r'Hoạt động mà ta <b>không biết trước được kết quả</b> của nó, nhưng <b>biết được tất cả các kết quả có thể</b> xảy ra, được gọi là [[phép thử ngẫu nhiên]] (gọi tắt là phép thử).'))
theory += T(r'For example, tossing a coin, rolling a die, drawing a card from a box without looking are random experiments. Counting the days of a week is not (we know the result: 7).',
            r'Chẳng hạn, tung đồng xu, gieo xúc xắc, rút một tấm thẻ trong hộp mà không nhìn là các phép thử ngẫu nhiên. Đếm số ngày trong tuần thì không phải (ta biết trước kết quả là 7).')
theory += '<h3>5.2 %s</h3>' % TI('Sample space', 'Không gian mẫu')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'The set of all possible outcomes of a random experiment is called its <b>sample space</b>, denoted \(\Omega\).',
    r'Tập hợp tất cả các kết quả có thể của một phép thử được gọi là [[không gian mẫu]] của phép thử đó, kí hiệu là \(\Omega\).'),
  UL([T(r'Toss a coin (H: heads, T: tails): \(\Omega=\{H;\,T\}\).', r'Gieo một đồng xu (N: mặt ngửa, S: mặt sấp): \(\Omega=\{N;\,S\}\).'),
      T(r'Roll a die: \(\Omega=\{1;\,2;\,3;\,4;\,5;\,6\}\).', r'Gieo một con xúc xắc: \(\Omega=\{1;\,2;\,3;\,4;\,5;\,6\}\).')]))
theory += '<h3>5.3 %s</h3>' % TI('Two-step experiments: tables and tree diagrams', 'Phép thử hai bước: dùng bảng hoặc sơ đồ hình cây')
theory += BOX('mint', ('How to describe the sample space', 'Cách mô tả không gian mẫu'),
  T(r'When an experiment has two steps, each outcome is an <b>ordered pair</b> \((a;\,b)\): \(a\) is the result of step 1, \(b\) of step 2. We list all outcomes with a <b>table</b> (rows: step 1, columns: step 2) or a <b>tree diagram</b>.',
    r'Khi phép thử gồm hai bước, mỗi kết quả là một [[cặp số|cặp số]] có thứ tự \((a;\,b)\): \(a\) là kết quả bước 1, \(b\) là kết quả bước 2. Ta liệt kê mọi kết quả bằng <b>bảng</b> (hàng: bước 1, cột: bước 2) hoặc [[sơ đồ hình cây]].'),
  T(r'If step 1 has \(m\) outcomes and, for each of them, step 2 has \(n\) outcomes, then \(\Omega\) has \(m\cdot n\) outcomes.', r'Nếu bước 1 có \(m\) kết quả và ứng với mỗi kết quả đó, bước 2 có \(n\) kết quả thì \(\Omega\) có \(m\cdot n\) kết quả.'))
theory += T(r'Tossing two coins: \(\Omega=\{HH;\,HT;\,TH;\,TT\}\) (here \(HT\) means coin 1 heads, coin 2 tails).', r'Gieo hai đồng xu: \(\Omega=\{NN;\,NS;\,SN;\,SS\}\) (ở đây \(NS\) nghĩa là đồng xu thứ nhất ngửa, đồng xu thứ hai sấp).')
theory += TREE_COIN
theory += T(r'Rolling two dice: the table has \(6\cdot6=36\) outcomes; \((2;\,5)\) and \((5;\,2)\) are different outcomes.', r'Gieo hai con xúc xắc: bảng có \(6\cdot6=36\) kết quả; \((2;\,5)\) và \((5;\,2)\) là hai kết quả khác nhau.')
theory += DICE()

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Random or not?', 'Có phải phép thử ngẫu nhiên?'),
  T(r'Which activities are random experiments? Give the sample space of each random experiment. (a) Draw a card at random from a box of 5 cards numbered 1 to 5. (b) Count the number of corners of a triangle. (c) Spin a spinner with 4 equal sectors numbered 1 to 4.',
    r'Hoạt động nào là phép thử ngẫu nhiên? Viết không gian mẫu của mỗi phép thử đó. a) Rút ngẫu nhiên một tấm thẻ từ hộp có 5 tấm thẻ đánh số từ 1 đến 5. b) Đếm số đỉnh của một tam giác. c) Quay một vòng quay có 4 hình quạt bằng nhau đánh số từ 1 đến 4.'),
  ('Ask: do we know the result in advance? Do we know all possible results?', 'Tự hỏi: có biết trước kết quả không? Có biết tất cả các kết quả có thể không?'),
  [T(r'(a) Random: \(\Omega=\{1;\,2;\,3;\,4;\,5\}\).', r'a) Là phép thử ngẫu nhiên: \(\Omega=\{1;\,2;\,3;\,4;\,5\}\).'),
   T(r'(b) Not random: the answer is always 3.', r'b) Không phải: kết quả luôn là 3.'),
   T(r'(c) Random: \(\Omega=\{1;\,2;\,3;\,4\}\).', r'c) Là phép thử ngẫu nhiên: \(\Omega=\{1;\,2;\,3;\,4\}\).')],
  T(r'(a) and (c).', r'a) và c).'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Two coins', 'Gieo hai đồng xu'),
  T(r'Toss two coins one after the other. Use a tree diagram to write the sample space. How many outcomes are there?', r'Gieo lần lượt hai đồng xu. Dùng sơ đồ hình cây để viết không gian mẫu. Có bao nhiêu kết quả?'),
  ('Coin 1 has 2 outcomes; for each of them coin 2 has 2 outcomes.', 'Đồng xu thứ nhất có 2 kết quả; ứng với mỗi kết quả, đồng xu thứ hai có 2 kết quả.'),
  [T(r'See the tree diagram in 5.3: \(\Omega=\{HH;\,HT;\,TH;\,TT\}\).', r'Xem sơ đồ hình cây ở mục 5.3: \(\Omega=\{NN;\,NS;\,SN;\,SS\}\).'),
   T(r'\(2\cdot2=4\) outcomes. Note: \(HT\neq TH\).', r'Có \(2\cdot2=4\) kết quả. Chú ý: \(NS\neq SN\).')],
  T(r'4 outcomes.', r'4 kết quả.'))
examples += EXAMPLE(3, ('Basic application', 'Vận dụng thấp'), ('Two dice', 'Gieo hai con xúc xắc'),
  T(r'Roll a red die and a blue die. (a) How many outcomes does the sample space have? (b) Write the outcomes in which the two dice show the same number.', r'Gieo một con xúc xắc màu đỏ và một con xúc xắc màu xanh. a) Không gian mẫu có bao nhiêu kết quả? b) Viết các kết quả mà hai xúc xắc ra cùng số chấm.'),
  ('Use the 6 × 6 table in 5.3 (row: red die, column: blue die).', 'Dùng bảng 6 × 6 ở mục 5.3 (hàng: xúc xắc đỏ, cột: xúc xắc xanh).'),
  [T(r'(a) \(6\cdot6=36\) outcomes.', r'a) Có \(6\cdot6=36\) kết quả.'),
   T(r'(b) The diagonal of the table: \((1;\,1)\), \((2;\,2)\), \((3;\,3)\), \((4;\,4)\), \((5;\,5)\), \((6;\,6)\).', r'b) Đường chéo của bảng: \((1;\,1)\), \((2;\,2)\), \((3;\,3)\), \((4;\,4)\), \((5;\,5)\), \((6;\,6)\).')],
  T(r'(a) 36; (b) 6 outcomes on the diagonal.', r'a) 36; b) 6 kết quả trên đường chéo.'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Without putting back', 'Lấy không trả lại'),
  T(r'A bag has three balls: red (R), blue (B), yellow (Y). Take one ball, do not put it back, then take a second ball. Write the sample space.', r'Một túi có ba quả bóng: đỏ (Đ), xanh (X), vàng (V). Lấy một quả, không trả lại túi, rồi lấy tiếp quả thứ hai. Viết không gian mẫu.'),
  ('After the first ball is taken, only two balls are left.', 'Sau lần lấy thứ nhất, trong túi chỉ còn hai quả.'),
  [TREE_BALL,
   T(r'\(\Omega=\{(R;\,B);\,(R;\,Y);\,(B;\,R);\,(B;\,Y);\,(Y;\,R);\,(Y;\,B)\}\): \(3\cdot2=6\) outcomes. The pairs \((R;\,R)\), … are not possible.', r'\(\Omega=\{(Đ;\,X);\,(Đ;\,V);\,(X;\,Đ);\,(X;\,V);\,(V;\,Đ);\,(V;\,X)\}\): có \(3\cdot2=6\) kết quả. Các cặp như \((Đ;\,Đ)\) không thể xảy ra.')],
  T(r'6 outcomes.', r'6 kết quả.'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Choosing lunch', 'Chọn bữa trưa'),
  T(r'A school canteen offers rice, pho or noodle soup, with iced tea or orange juice. Mai chooses one dish and one drink at random. (a) Draw a tree diagram and find the number of outcomes. (b) The canteen adds a choice of dessert: yogurt or fruit. How many outcomes are there now?',
    r'Căng tin của trường có cơm, phở hoặc bún, kèm trà đá hoặc nước cam. Mai chọn ngẫu nhiên một món ăn và một loại đồ uống. a) Vẽ sơ đồ hình cây và tìm số kết quả có thể. b) Căng tin bổ sung món tráng miệng: sữa chua hoặc trái cây. Lúc này có bao nhiêu kết quả có thể?'),
  ('Each branch of the tree is followed by the same number of new branches.', 'Mỗi nhánh của cây được nối tiếp bởi cùng một số nhánh mới.'),
  [TREE_MENU, T(r'(a) \(3\cdot2=6\) outcomes.', r'a) Có \(3\cdot2=6\) kết quả.'),
   T(r'(b) Each of the 6 outcomes is followed by 2 desserts: \(6\cdot2=12\) outcomes.', r'b) Mỗi kết quả trong 6 kết quả trên được nối tiếp bởi 2 món tráng miệng: \(6\cdot2=12\) kết quả.')],
  T(r'(a) 6; (b) 12.', r'a) 6; b) 12.'))

_SETS = sp_g9.BANK(sp_g9p.L25_GROUPS, start=1, seeds=(2501, 2502, 2503))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Forgetting the order.</b> When rolling two different dice, \((2;\,5)\) and \((5;\,2)\) are two outcomes.', r'<b>Quên thứ tự.</b> Khi gieo hai con xúc xắc khác nhau, \((2;\,5)\) và \((5;\,2)\) là hai kết quả.'),
 (r'<b>Adding instead of multiplying.</b> 3 dishes and 2 drinks give \(3\cdot2=6\) outcomes, not \(3+2\).', r'<b>Cộng thay vì nhân.</b> 3 món ăn và 2 đồ uống cho \(3\cdot2=6\) kết quả, không phải \(3+2\).'),
 (r'<b>Allowing impossible outcomes.</b> Without putting back, the same ball cannot be taken twice.', r'<b>Liệt kê kết quả không thể xảy ra.</b> Lấy không trả lại thì không thể lấy cùng một quả bóng hai lần.'),
 (r'<b>Writing the sample space wrongly.</b> \(\Omega\) lists every possible outcome exactly once, inside braces.', r'<b>Viết sai không gian mẫu.</b> \(\Omega\) liệt kê mỗi kết quả có thể đúng một lần, trong dấu ngoặc nhọn.')]
summary = [
 (r'A random experiment: the outcome is not known in advance, but all possible outcomes are known.', r'Phép thử ngẫu nhiên: không biết trước kết quả nhưng biết tất cả các kết quả có thể.'),
 (r'The sample space \(\Omega\) is the set of all possible outcomes.', r'Không gian mẫu \(\Omega\) là tập hợp tất cả các kết quả có thể.'),
 (r'Two-step experiments: outcomes are ordered pairs; list them with a table or a tree diagram (\(m\cdot n\) outcomes).', r'Phép thử hai bước: kết quả là cặp có thứ tự; liệt kê bằng bảng hoặc sơ đồ hình cây (có \(m\cdot n\) kết quả).'),
 (r'Key English: random experiment, outcome, sample space, coin toss, die (dice), tree diagram.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[phép thử ngẫu nhiên]], [[kết quả có thể|kết quả có thể (của phép thử)]], [[không gian mẫu]], [[gieo đồng xu|gieo đồng xu (phép thử)]], [[con xúc xắc|con xúc xắc (phép thử)]], [[sơ đồ hình cây]].')]
checks = [
 (r'I can tell whether an activity is a random experiment.', r'Em nhận biết được một hoạt động có phải là phép thử ngẫu nhiên không.'),
 (r'I can write the sample space of a coin toss, a die roll or a card draw.', r'Em viết được không gian mẫu của phép thử gieo đồng xu, gieo xúc xắc, rút thẻ.'),
 (r'I can describe a two-step sample space with a table or a tree diagram.', r'Em mô tả được không gian mẫu của phép thử hai bước bằng bảng hoặc sơ đồ hình cây.'),
 (r'I can count the outcomes in real situations.', r'Em đếm được số kết quả có thể trong tình huống thực tế.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Random Experiments and Sample Spaces', title_vi='Phép thử ngẫu nhiên và không gian mẫu', topic=TOPIC,
       folder='probability', file='random-experiments-sample-spaces', catalog_title_vi='Phép thử ngẫu nhiên và không gian mẫu',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Random experiments, outcomes, sample spaces; two-step experiments with tables and tree diagrams.', level='Basic', minutes=60,
       description_vi='Bài 25 – Phép thử ngẫu nhiên, kết quả có thể, không gian mẫu; phép thử hai bước: bảng và sơ đồ hình cây.',
       tags_vi=['phép thử ngẫu nhiên', 'không gian mẫu', 'sơ đồ hình cây'], prerequisites=['g9-frequency-03'], tags=['random experiment', 'sample space', 'tree diagram'], order=250)
