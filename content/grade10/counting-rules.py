# -*- coding: utf-8 -*-
"""g10-comb-01 = Toán 10 KNTT, Bài 23: Quy tắc đếm. Mã ngân hàng câu hỏi: TOAN10-C8-B23."""
import os, sys, math, itertools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g10i as S
import mb_pgf

CV = 'Quy tắc đếm'
vocab = defs(CV, [
 ('rsum', 'rule of sum', 'quy tắc cộng', 'if a job can be done in one of two ways with no common outcome, having \\(m\\) and \\(n\\) options, there are \\(m+n\\) ways.', 'nếu một công việc được hoàn thành bởi một trong hai phương án không trùng nhau, có \\(m\\) và \\(n\\) cách, thì có \\(m+n\\) cách.', 'By the rule of sum there are 9 ways.', '\\(m+n\\)'),
 ('rprod', 'rule of product', 'quy tắc nhân', 'if a job has two successive stages with \\(m\\) and \\(n\\) options, there are \\(m\\cdot n\\) ways.', 'nếu một công việc gồm hai công đoạn liên tiếp có \\(m\\) và \\(n\\) cách, thì có \\(m\\cdot n\\) cách.', 'By the rule of product there are 6 outfits.', '\\(m\\cdot n\\)'),
 ('treed', 'tree diagram', 'sơ đồ hình cây', 'a diagram whose branches list all outcomes stage by stage.', 'sơ đồ liệt kê mọi kết quả theo từng công đoạn bằng các nhánh.', 'Draw a tree diagram of the outfits.', '')])
goals = [('recognise the rule of sum and the rule of product;', 'nhận biết [[quy tắc cộng]] và [[quy tắc nhân]];'),
         ('list outcomes with a [[sơ đồ hình cây]] tree diagram;', 'liệt kê kết quả bằng [[sơ đồ hình cây]];'),
         ('count numbers, codes and routes, splitting into cases and stages;', 'đếm số, mã, đường đi bằng cách chia trường hợp và chia công đoạn;'),
         ('use the complement to count "at least one" situations.', 'dùng phần bù để đếm các tình huống "có ít nhất một".')]
goals[1] = ('list outcomes with a tree diagram;', goals[1][1])
phrases = [('<b>There are two cases, so we add.</b>', 'Có hai trường hợp nên ta cộng.'), ('<b>There are three stages, so we multiply.</b>', 'Có ba công đoạn nên ta nhân.'),
           ('<b>The first digit cannot be zero.</b>', 'Chữ số đầu tiên phải khác 0.'), ('<b>Count the complement and subtract.</b>', 'Đếm phần bù rồi lấy tổng trừ đi.'), ('<b>Each branch of the tree is one outcome.</b>', 'Mỗi nhánh của cây là một kết quả.')]
review = T('From Bài 2: for disjoint finite sets \\(n(A\\cup B)=n(A)+n(B)\\); in general \\(n(A\\cup B)=n(A)+n(B)-n(A\\cap B)\\). A natural number with \\(k\\) digits has a non-zero first digit.',
           'Từ Bài 2: với hai tập hữu hạn rời nhau \\(n(A\\cup B)=n(A)+n(B)\\); tổng quát \\(n(A\\cup B)=n(A)+n(B)-n(A\\cap B)\\). Số tự nhiên có \\(k\\) chữ số có chữ số đầu tiên khác 0.')
theory = '<h3>23.1 %s</h3>' % TI('The rule of sum', 'Quy tắc cộng')
theory += BOX('blue', ('Rule', 'Quy tắc'), UL([T('A job can be done by <b>one</b> of two methods: method 1 has \\(m\\) ways, method 2 has \\(n\\) ways, and no way is shared. Then the job can be done in \\(m+n\\) ways.', 'Một công việc được hoàn thành bởi <b>một trong</b> hai phương án: phương án 1 có \\(m\\) cách, phương án 2 có \\(n\\) cách, không có cách nào trùng nhau. Khi đó có \\(m+n\\) cách hoàn thành công việc.'),
  T('It extends to several methods. Key word: <i>or</i> (cases).', 'Mở rộng cho nhiều phương án. Dấu hiệu: <i>hoặc</i> (các trường hợp).')]))
theory += '<h3>23.2 %s</h3>' % TI('The rule of product', 'Quy tắc nhân')
theory += BOX('blue', ('Rule', 'Quy tắc'), UL([T('A job consists of two <b>successive</b> stages: stage 1 has \\(m\\) ways and, for each of them, stage 2 has \\(n\\) ways. Then the job can be done in \\(m\\cdot n\\) ways.', 'Một công việc gồm hai <b>công đoạn liên tiếp</b>: công đoạn 1 có \\(m\\) cách, ứng với mỗi cách đó công đoạn 2 có \\(n\\) cách. Khi đó có \\(m\\cdot n\\) cách hoàn thành công việc.'),
  T('It extends to several stages. Key word: <i>and then</i> (stages). A tree diagram shows the stages as branching levels.', 'Mở rộng cho nhiều công đoạn. Dấu hiệu: <i>rồi</i>, <i>và</i> (các công đoạn). Sơ đồ hình cây thể hiện mỗi công đoạn là một tầng rẽ nhánh.')]))
tree = mb_pgf.raw_svg(r'''\begin{tikzpicture}[grow=right, level distance=2.9cm, level 1/.style={sibling distance=1.9cm}, level 2/.style={sibling distance=0.85cm},
  every node/.style={font=\small, text=ink}, edge from parent/.style={draw=ink!70, line width=0.7pt}]
\node[circle, fill=ink, inner sep=1.6pt] {}
  child {node[fill=mint!45, rounded corners=2pt, inner sep=2pt] {$A_3$} child {node {$A_3Q_2$}} child {node {$A_3Q_1$}}}
  child {node[fill=mint!45, rounded corners=2pt, inner sep=2pt] {$A_2$} child {node {$A_2Q_2$}} child {node {$A_2Q_1$}}}
  child {node[fill=mint!45, rounded corners=2pt, inner sep=2pt] {$A_1$} child {node {$A_1Q_2$}} child {node {$A_1Q_1$}}};
\node[text=ink!70, font=\footnotesize] at (2.9,-3.1) {áo / shirt};
\node[text=ink!70, font=\footnotesize] at (5.8,-3.1) {quần / trousers};
\end{tikzpicture}''')
theory += mb_pgf.img(tree, 'Tree diagram of 3 shirts and 2 pairs of trousers: 6 outfits', 460, TI('Tree diagram: 3 shirts, then 2 pairs of trousers for each – \\(3\\cdot2=6\\) outfits.', 'Sơ đồ hình cây: 3 áo, mỗi áo có 2 quần – \\(3\\cdot2=6\\) bộ.'))
theory += '<h3>23.3 %s</h3>' % TI('Combining the rules', 'Phối hợp hai quy tắc')
theory += BOX('mint', ('Strategy', 'Chiến lược'), UL([T('Split into disjoint <b>cases</b> (add), then count each case by <b>stages</b> (multiply).', 'Chia thành các <b>trường hợp</b> rời nhau (cộng), rồi đếm mỗi trường hợp theo <b>công đoạn</b> (nhân).'),
  T('Put the most restricted position first (first digit \\(\\ne0\\), last digit even, …).', 'Ưu tiên vị trí bị ràng buộc nhiều nhất (chữ số đầu khác 0, chữ số cuối chẵn, …).'),
  T('"At least one": count everything, subtract the complement ("none").', '"Có ít nhất một": đếm tất cả rồi trừ phần bù ("không có").')]))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('Add only when the cases do not overlap; multiply only when the number of choices at a stage does not depend on earlier choices.', 'Chỉ cộng khi các trường hợp không giao nhau; chỉ nhân khi số cách ở mỗi công đoạn không phụ thuộc vào lựa chọn trước đó.'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Rule of sum', 'Quy tắc cộng'), T('From Hà Nội to Huế you can fly (3 flights a day), take the train (2 trains) or take a coach (4 coaches). How many ways are there to choose one trip?', 'Từ Hà Nội vào Huế có thể đi máy bay (3 chuyến/ngày), tàu hỏa (2 chuyến) hoặc xe khách (4 chuyến). Có bao nhiêu cách chọn một chuyến đi?'),
  T('Three non-overlapping options.', 'Ba phương án không trùng nhau.'), [T('\\(3+2+4=9\\).', '\\(3+2+4=9\\).')], T('9 ways.', '9 cách.'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Rule of product', 'Quy tắc nhân'), T('Minh has 3 shirts \\(A_1,A_2,A_3\\) and 2 pairs of trousers \\(Q_1,Q_2\\). How many outfits (one shirt and one pair) can he wear? List them.', 'Minh có 3 áo \\(A_1,A_2,A_3\\) và 2 quần \\(Q_1,Q_2\\). Có bao nhiêu bộ (một áo và một quần)? Liệt kê.'),
  T('Stage 1 shirt, stage 2 trousers.', 'Công đoạn 1 chọn áo, công đoạn 2 chọn quần.'), [T('\\(3\\cdot2=6\\); the tree gives \\(A_1Q_1, A_1Q_2, A_2Q_1, A_2Q_2, A_3Q_1, A_3Q_2\\).', '\\(3\\cdot2=6\\); sơ đồ cây cho \\(A_1Q_1, A_1Q_2, A_2Q_1, A_2Q_2, A_3Q_1, A_3Q_2\\).')], T('6 outfits.', '6 bộ.'))
D = [0, 1, 2, 3, 4, 5]
assert sum(1 for p in itertools.permutations(D, 3) if p[0]) == 100 and sum(1 for p in itertools.permutations(D, 3) if p[0] and p[2] % 2 == 0) == 52
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Numbers with conditions', 'Lập số có điều kiện'), T('From the digits \\(0,1,2,3,4,5\\): a) how many 3-digit numbers with distinct digits? b) how many of them are even?', 'Từ các chữ số \\(0,1,2,3,4,5\\): a) lập được bao nhiêu số có 3 chữ số đôi một khác nhau? b) bao nhiêu số trong đó là số chẵn?'),
  T('a) first digit \\(\\ne0\\); b) cases: last digit 0, or last digit 2 or 4.', 'a) chữ số đầu khác 0; b) chia trường hợp: tận cùng là 0, hoặc tận cùng là 2 hoặc 4.'),
  [T('a) \\(5\\cdot5\\cdot4=100\\) (hundreds 5 ways, tens 5, units 4).', 'a) \\(5\\cdot5\\cdot4=100\\) (hàng trăm 5 cách, hàng chục 5, hàng đơn vị 4).'),
   T('b) Last digit 0: \\(5\\cdot4=20\\). Last digit 2 or 4: 2 ways, then the first digit 4 ways (not 0, not the last), the middle 4 ways: \\(2\\cdot4\\cdot4=32\\).', 'b) Tận cùng 0: \\(5\\cdot4=20\\). Tận cùng 2 hoặc 4: 2 cách, chữ số đầu 4 cách (khác 0 và khác chữ số cuối), chữ số giữa 4 cách: \\(2\\cdot4\\cdot4=32\\).'), T('\\(20+32=52\\).', '\\(20+32=52\\).')],
  T('a) 100; b) 52.', 'a) 100; b) 52.'))
assert sum(1 for d in range(1, 361) if 360 % d == 0) == 24
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Counting divisors', 'Đếm ước số'), T('How many positive divisors does 360 have?', 'Số 360 có bao nhiêu ước nguyên dương?'),
  T('\\(360=2^3\\cdot3^2\\cdot5\\); a divisor is \\(2^i3^j5^k\\).', '\\(360=2^3\\cdot3^2\\cdot5\\); mỗi ước có dạng \\(2^i3^j5^k\\).'),
  [T('\\(i\\in\\{0,1,2,3\\}\\) (4 ways), \\(j\\) 3 ways, \\(k\\) 2 ways.', '\\(i\\in\\{0,1,2,3\\}\\) (4 cách), \\(j\\) có 3 cách, \\(k\\) có 2 cách.'), T('\\(4\\cdot3\\cdot2=24\\).', '\\(4\\cdot3\\cdot2=24\\).')], T('24 divisors.', '24 ước.'))
assert 36 ** 6 - 26 ** 6 == 1867866560
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('A password policy', 'Quy định mật khẩu'), T('A password has 6 characters, each a digit (10) or a lowercase letter (26), and must contain <b>at least one digit</b>. How many passwords are possible?', 'Mật khẩu gồm 6 kí tự, mỗi kí tự là một chữ số (10) hoặc một chữ cái thường (26), và phải có <b>ít nhất một chữ số</b>. Có bao nhiêu mật khẩu?'),
  T('Complement: passwords with no digit.', 'Phần bù: mật khẩu không có chữ số nào.'),
  [T('All: \\(36^6=2\\,176\\,782\\,336\\).', 'Tất cả: \\(36^6=2\\,176\\,782\\,336\\).'), T('No digit: \\(26^6=308\\,915\\,776\\).', 'Không có chữ số: \\(26^6=308\\,915\\,776\\).'), T('\\(36^6-26^6=1\\,867\\,866\\,560\\).', '\\(36^6-26^6=1\\,867\\,866\\,560\\).')],
  T('1 867 866 560 passwords (about 86% of all strings).', '1 867 866 560 mật khẩu (khoảng 86% số chuỗi).'))
examples = EXFIG(examples, 2, mb_pgf.img(tree, 'Tree diagram of 6 outfits', 420))


def lvl(P):
    a, b, c = P['sum']
    o1 = M4(1, 'A library shelf has %d maths books, %d physics books and %d chemistry books (all different). In how many ways can you borrow one book?' % (a, b, c), 'Một giá sách có %d cuốn Toán, %d cuốn Vật lí, %d cuốn Hóa học (đôi một khác nhau). Có bao nhiêu cách mượn một cuốn?' % (a, b, c), '\\(%d\\)' % (a + b + c),
            ['\\(%d\\)' % (a * b * c), '\\(%d\\)' % (a * b + c), '\\(%d\\)' % (a + b)], 'Rule of sum.', 'Quy tắc cộng: \\(%d+%d+%d\\).' % (a, b, c))
    x, y, z = P['prod']
    o2 = M4(2, 'A set menu has one starter (%d kinds), one main dish (%d kinds) and one drink (%d kinds). How many menus?' % (x, y, z), 'Một suất ăn gồm một món khai vị (%d loại), một món chính (%d loại) và một đồ uống (%d loại). Có bao nhiêu suất ăn khác nhau?' % (x, y, z), '\\(%d\\)' % (x * y * z),
            ['\\(%d\\)' % (x + y + z), '\\(%d\\)' % (x * y + z), '\\(%d\\)' % (x * (y + z))], 'Rule of product.', 'Quy tắc nhân: \\(%d\\cdot%d\\cdot%d\\).' % (x, y, z))
    m, n, k = P['route']
    o3 = M4(3, 'A→B: %d roads; B→C: %d roads; A→C directly: %d roads. Ways from A to C?' % (m, n, k), 'Từ A đến B có %d đường, từ B đến C có %d đường, từ A đến thẳng C có %d đường. Số cách đi từ A đến C là…' % (m, n, k), '\\(%d\\)' % (m * n + k),
            ['\\(%d\\)' % (m + n + k), '\\(%d\\)' % (m * n * k), '\\(%d\\)' % (m * n)], 'Via B: \\(%d\\cdot%d\\); direct: %d.' % (m, n, k), 'Qua B: \\(%d\\cdot%d\\); đi thẳng: %d; cộng lại.' % (m, n, k))
    Dg, L, claim = P['rep']; n4 = len(Dg); real = (n4 - (1 if 0 in Dg else 0)) * n4 ** (L - 1)
    t4 = tf(4, 'From the digits \\(%s\\) one can form exactly %d numbers with %d digits (repetition allowed).' % (',\\,'.join(map(str, Dg)), claim, L), 'Từ các chữ số \\(%s\\) lập được đúng %d số có %d chữ số (các chữ số có thể lặp lại).' % (',\\,'.join(map(str, Dg)), claim, L), real == claim,
            'There are %d such numbers.' % real, 'Có \\(%d\\cdot%d^{%d}=%d\\) số.' % (n4 - (1 if 0 in Dg else 0), n4, L - 1, real))
    N, claim5 = P['div']; real5 = sum(1 for d in range(1, N + 1) if N % d == 0)
    t5 = tf(5, '%d has exactly %d positive divisors.' % (N, claim5), 'Số %d có đúng %d ước nguyên dương.' % (N, claim5), real5 == claim5, 'It has %d.' % real5, 'Phân tích thừa số nguyên tố rồi nhân các (số mũ + 1): có %d ước.' % real5)
    Dd = P['dist']; real6 = sum(1 for p in itertools.permutations(Dd, 3) if p[0] != 0)
    s6 = sh(6, 'How many 3-digit numbers with distinct digits can be formed from \\(%s\\)?' % ',\\,'.join(map(str, Dd)), 'Từ các chữ số \\(%s\\) lập được bao nhiêu số có 3 chữ số đôi một khác nhau?' % ',\\,'.join(map(str, Dd)), real6,
            'First digit not 0, no repetition.', 'Chữ số đầu khác 0, các chữ số không lặp: %d số.' % real6)
    L7 = P['pin']; real7 = math.perm(10, L7)
    s7 = sh(7, 'A door code has %d digits, all different. How many codes are possible?' % L7, 'Mã khóa cửa gồm %d chữ số đôi một khác nhau. Có bao nhiêu mã?' % L7, real7,
            '\\(10\\cdot9\\cdots\\).', 'Quy tắc nhân: \\(%s=%d\\).' % ('\\cdot'.join(str(10 - i) for i in range(L7)), real7))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]


PP = [dict(sum=(7, 5, 4), prod=(3, 5, 4), route=(3, 4, 2), rep=([1, 2, 3, 4], 3, 64), div=(72, 12), dist=[0, 1, 2, 3, 4], pin=3),
      dict(sum=(12, 9, 6), prod=(4, 6, 3), route=(5, 3, 2), rep=([0, 1, 2, 3, 5], 3, 125), div=(100, 9), dist=[1, 3, 5, 7, 9], pin=4),
      dict(sum=(15, 8, 11), prod=(2, 7, 5), route=(4, 3, 2), rep=([0, 2, 4, 6], 4, 192), div=(90, 10), dist=[0, 2, 4, 6, 8, 9], pin=5)]
practice = three(lvl, PP)
practice = with_self(practice, S.M23S10, start=8)
mistakes = [('<b>Adding instead of multiplying.</b> Shirt <i>and then</i> trousers are stages: multiply.', '<b>Cộng thay vì nhân.</b> Chọn áo <i>rồi</i> chọn quần là các công đoạn: phải nhân.'),
            ('<b>Forgetting that the first digit is not 0.</b> With 0 among the digits, treat the first position first.', '<b>Quên chữ số đầu khác 0.</b> Khi có chữ số 0, phải xét vị trí đầu tiên trước.'),
            ('<b>Adding overlapping cases.</b> "Even or divisible by 5" counts numbers ending in 0 twice.', '<b>Cộng các trường hợp giao nhau.</b> "Chẵn hoặc chia hết cho 5" đếm hai lần các số tận cùng bằng 0.'),
            ('<b>Counting "at least one" directly with many cases.</b> Use the complement: total minus "none".', '<b>Đếm "ít nhất một" trực tiếp qua nhiều trường hợp.</b> Dùng phần bù: tất cả trừ "không có".')]
summary = [('Rule of sum: disjoint cases \\(\\Rightarrow m+n\\).', 'Quy tắc cộng: các trường hợp rời nhau \\(\\Rightarrow m+n\\).'), ('Rule of product: successive stages \\(\\Rightarrow m\\cdot n\\); tree diagrams list outcomes.', 'Quy tắc nhân: các công đoạn liên tiếp \\(\\Rightarrow m\\cdot n\\); sơ đồ cây liệt kê kết quả.'),
           ('Strategy: cases (add) of stages (multiply); restricted positions first; complement for "at least".', 'Chiến lược: chia trường hợp (cộng), mỗi trường hợp chia công đoạn (nhân); ưu tiên vị trí có ràng buộc; dùng phần bù cho "ít nhất".'),
           ('Key words: rule of sum, rule of product, tree diagram, case, stage.', 'Từ cần nhớ: rule of sum, rule of product, tree diagram, case, stage.')]
checks = [('I can tell when to add and when to multiply.', 'Em phân biệt được khi nào cộng, khi nào nhân.'), ('I can draw a tree diagram.', 'Em vẽ được sơ đồ hình cây.'),
          ('I can count numbers with conditions on digits.', 'Em đếm được các số có điều kiện về chữ số.'), ('I can use the complement.', 'Em dùng được phần bù.')]
LL('g10-comb-01', 'Counting Rules', CV, ('Combinatorics', 'Đại số tổ hợp'), 'combinatorics', 'counting-rules', 230, 'Beginner', 65, ('sets, union of sets', 'tập hợp, hợp của các tập hợp'),
   'Rule of sum, rule of product, tree diagrams; counting numbers, codes, routes and divisors.', 'Bài 23 – Quy tắc cộng, quy tắc nhân, sơ đồ hình cây; đếm số, mã, đường đi, ước số.',
   ['rule of sum', 'rule of product', 'tree diagram'], ['quy tắc cộng', 'quy tắc nhân', 'sơ đồ hình cây'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g10-sets-01'])
