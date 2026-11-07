# -*- coding: utf-8 -*-
"""g10-comb-02 = Toán 10 KNTT, Bài 24: Hoán vị, chỉnh hợp và tổ hợp. Mã ngân hàng câu hỏi: TOAN10-C8-B24."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g10i as S

C, A = math.comb, math.perm
CV = 'Hoán vị, chỉnh hợp và tổ hợp'
vocab = defs(CV, [
 ('perm', 'permutation', 'hoán vị', 'an arrangement of all \\(n\\) elements in order; \\(P_n=n!\\).', 'một cách sắp xếp thứ tự \\(n\\) phần tử; \\(P_n=n!\\).', 'There are 5! permutations of 5 books.', '\\(P_n\\)'),
 ('arrang', 'arrangement (k-permutation)', 'chỉnh hợp', 'an ordered choice of \\(k\\) of \\(n\\) elements; \\(A_n^k=\\dfrac{n!}{(n-k)!}\\).', 'cách chọn \\(k\\) trong \\(n\\) phần tử có sắp thứ tự; \\(A_n^k=\\dfrac{n!}{(n-k)!}\\).', 'The podium is an arrangement of 3 of 8 runners.', '\\(A_n^k\\)'),
 ('combin', 'combination', 'tổ hợp', 'an unordered choice of \\(k\\) of \\(n\\) elements; \\(C_n^k=\\dfrac{n!}{k!(n-k)!}\\).', 'cách chọn \\(k\\) trong \\(n\\) phần tử không kể thứ tự; \\(C_n^k=\\dfrac{n!}{k!(n-k)!}\\).', 'A team of 3 is a combination.', '\\(C_n^k\\)'),
 ('factorial', 'factorial', 'giai thừa', '\\(n!=1\\cdot2\\cdots n\\), \\(0!=1\\).', '\\(n!=1\\cdot2\\cdots n\\), quy ước \\(0!=1\\).', '5! = 120.', '\\(n!\\)')])
goals = [('recognise permutations, arrangements and combinations and their formulas;', 'nhận biết [[hoán vị]], [[chỉnh hợp]], [[tổ hợp]] và công thức tính;'),
         ('decide whether order matters and choose the right formula;', 'xác định có quan tâm thứ tự hay không để chọn công thức phù hợp;'),
         ('count arrangements, selections and seatings with conditions;', 'đếm số cách sắp xếp, lựa chọn, xếp chỗ có điều kiện;'),
         ('solve real problems (teams, lotteries, tournaments).', 'giải bài toán thực tế (lập đội, xổ số, giải đấu).')]
phrases = [('<b>Order matters, so it is an arrangement.</b>', 'Có thứ tự nên đây là chỉnh hợp.'), ('<b>Order does not matter, so it is a combination.</b>', 'Không quan tâm thứ tự nên đây là tổ hợp.'),
           ('<b>Five factorial equals one hundred and twenty.</b>', '5 giai thừa bằng 120.'), ('<b>Treat the two friends as one block.</b>', 'Coi hai bạn là một khối.'), ('<b>Choose the boys, then the girls.</b>', 'Chọn nam, rồi chọn nữ.')]
review = T('From Bài 23: rule of sum (cases) and rule of product (stages). \\(n!=1\\cdot2\\cdot3\\cdots n\\), e.g. \\(4!=24\\), \\(5!=120\\), \\(6!=720\\).', 'Từ Bài 23: quy tắc cộng (trường hợp) và quy tắc nhân (công đoạn). \\(n!=1\\cdot2\\cdot3\\cdots n\\), ví dụ \\(4!=24\\), \\(5!=120\\), \\(6!=720\\).')
theory = '<h3>24.1 %s</h3>' % TI('Permutations', 'Hoán vị')
theory += BOX('blue', ('Definition and formula', 'Định nghĩa và công thức'), T('Each ordering of \\(n\\) distinct elements is a permutation. By the rule of product: \\(P_n=n\\cdot(n-1)\\cdots2\\cdot1=n!\\).', 'Mỗi cách sắp thứ tự \\(n\\) phần tử phân biệt là một hoán vị. Theo quy tắc nhân: \\(P_n=n\\cdot(n-1)\\cdots2\\cdot1=n!\\).'))
theory += '<h3>24.2 %s</h3>' % TI('Arrangements', 'Chỉnh hợp')
theory += BOX('blue', ('Definition and formula', 'Định nghĩa và công thức'), T('Choosing \\(k\\) of \\(n\\) elements (\\(1\\le k\\le n\\)) <b>and ordering them</b> is an arrangement: \\(A_n^k=n(n-1)\\cdots(n-k+1)=\\dfrac{n!}{(n-k)!}\\). Note \\(A_n^n=P_n\\).', 'Chọn \\(k\\) phần tử trong \\(n\\) phần tử (\\(1\\le k\\le n\\)) <b>và sắp thứ tự</b> chúng là một chỉnh hợp: \\(A_n^k=n(n-1)\\cdots(n-k+1)=\\dfrac{n!}{(n-k)!}\\). Lưu ý \\(A_n^n=P_n\\).'))
theory += '<h3>24.3 %s</h3>' % TI('Combinations', 'Tổ hợp')
theory += BOX('blue', ('Definition and formula', 'Định nghĩa và công thức'), UL([T('A subset of \\(k\\) elements of an \\(n\\)-set (order ignored) is a combination: \\(C_n^k=\\dfrac{A_n^k}{k!}=\\dfrac{n!}{k!\\,(n-k)!}\\) (\\(0\\le k\\le n\\), \\(C_n^0=1\\)).', 'Mỗi tập con gồm \\(k\\) phần tử của tập \\(n\\) phần tử (không kể thứ tự) là một tổ hợp: \\(C_n^k=\\dfrac{A_n^k}{k!}=\\dfrac{n!}{k!\\,(n-k)!}\\) (\\(0\\le k\\le n\\), \\(C_n^0=1\\)).'),
  T('Properties: \\(C_n^k=C_n^{n-k}\\); \\(C_{n}^{k}+C_{n}^{k+1}=C_{n+1}^{k+1}\\) (Pascal).', 'Tính chất: \\(C_n^k=C_n^{n-k}\\); \\(C_{n}^{k}+C_{n}^{k+1}=C_{n+1}^{k+1}\\) (Pascal).')]))
theory += TBL([TI('Situation', 'Tình huống'), TI('Order?', 'Thứ tự?'), TI('Formula', 'Công thức')], [
  [TI('Line up all \\(n\\) people', 'Xếp cả \\(n\\) người thành hàng'), TI('yes', 'có'), '\\(P_n=n!\\)'],
  [TI('Choose \\(k\\) people for \\(k\\) different posts', 'Chọn \\(k\\) người vào \\(k\\) chức vụ khác nhau'), TI('yes', 'có'), '\\(A_n^k\\)'],
  [TI('Choose a group of \\(k\\) people', 'Chọn một nhóm \\(k\\) người'), TI('no', 'không'), '\\(C_n^k\\)']])
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('Test: swap two chosen elements. If you get a <i>different</i> outcome, order matters (\\(A\\)); if the <i>same</i>, it does not (\\(C\\)).', 'Thử đổi chỗ hai phần tử đã chọn: nếu được kết quả <i>khác</i> thì có thứ tự (\\(A\\)); nếu <i>như cũ</i> thì không có thứ tự (\\(C\\)).'))

assert math.factorial(5) == 120 and A(8, 3) == 336
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Order matters', 'Có thứ tự'), T('a) In how many ways can 5 different books be put on a shelf? b) 8 runners race; in how many ways can the gold, silver and bronze medals be awarded?', 'a) Có bao nhiêu cách xếp 5 cuốn sách khác nhau lên giá? b) 8 vận động viên chạy thi; có bao nhiêu cách trao huy chương vàng, bạc, đồng?'),
  T('a) all elements; b) 3 of 8 with order.', 'a) xếp tất cả; b) chọn 3 trong 8 có thứ tự.'), [T('a) \\(P_5=5!=120\\).', 'a) \\(P_5=5!=120\\).'), T('b) \\(A_8^3=8\\cdot7\\cdot6=336\\).', 'b) \\(A_8^3=8\\cdot7\\cdot6=336\\).')], T('a) 120; b) 336.', 'a) 120; b) 336.'))
assert C(10, 3) == 120 and C(12, 2) == 66
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Order does not matter', 'Không có thứ tự'), T('a) Choose 3 students of 10 for a cleaning team. b) 12 people shake hands, each pair once. Count.', 'a) Chọn 3 trong 10 học sinh vào đội trực nhật. b) 12 người bắt tay nhau, mỗi cặp một lần. Đếm số cách / số cái bắt tay.'),
  T('Swapping two chosen people gives the same team / handshake.', 'Đổi chỗ hai người đã chọn vẫn là đội đó / cái bắt tay đó.'), [T('a) \\(C_{10}^3=120\\).', 'a) \\(C_{10}^3=120\\).'), T('b) \\(C_{12}^2=66\\).', 'b) \\(C_{12}^2=66\\).')], T('a) 120; b) 66.', 'a) 120; b) 66.'))
assert C(6, 2) * C(5, 2) == 150
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Mixed team', 'Đội hỗn hợp'), T('A group has 6 boys and 5 girls. How many ways to choose a team of 2 boys and 2 girls?', 'Một nhóm có 6 nam và 5 nữ. Có bao nhiêu cách chọn một đội gồm 2 nam và 2 nữ?'),
  T('Stage 1 boys, stage 2 girls.', 'Công đoạn 1 chọn nam, công đoạn 2 chọn nữ.'), [T('\\(C_6^2=15\\), \\(C_5^2=10\\); rule of product: \\(15\\cdot10\\).', '\\(C_6^2=15\\), \\(C_5^2=10\\); quy tắc nhân: \\(15\\cdot10\\).')], T('150 ways.', '150 cách.'))
assert 2 * math.factorial(5) == 240 and math.factorial(6) - 240 == 480
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Sitting together', 'Ngồi cạnh nhau'), T('6 friends, including An and Bình, sit in a row. In how many ways a) are An and Bình next to each other? b) are they not next to each other?', '6 bạn, trong đó có An và Bình, ngồi thành một hàng. Có bao nhiêu cách xếp sao cho a) An và Bình ngồi cạnh nhau? b) An và Bình không ngồi cạnh nhau?'),
  T('a) glue them into one block; b) complement.', 'a) coi hai bạn là một khối; b) dùng phần bù.'), [T('a) 5 "objects": \\(5!\\); inside the block 2 orders: \\(2\\cdot120=240\\).', 'a) 5 "đối tượng": \\(5!\\) cách; trong khối có 2 cách: \\(2\\cdot120=240\\).'), T('b) \\(6!-240=720-240=480\\).', 'b) \\(6!-240=720-240=480\\).')], T('a) 240; b) 480.', 'a) 240; b) 480.'))
assert C(45, 6) == 8145060
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('A lottery', 'Xổ số'), T('In the Mega 6/45 lottery a ticket picks 6 numbers from 1 to 45 (order not important). How many different tickets are there? What is the chance that one ticket wins the jackpot?', 'Trong xổ số Mega 6/45, mỗi vé chọn 6 số từ 1 đến 45 (không kể thứ tự). Có bao nhiêu vé khác nhau? Một vé có cơ hội trúng giải đặc biệt là bao nhiêu?'),
  T('A ticket is a combination of 6 of 45.', 'Mỗi vé là một tổ hợp chập 6 của 45.'), [T('\\(C_{45}^6=8\\,145\\,060\\).', '\\(C_{45}^6=8\\,145\\,060\\).'), T('Only one ticket wins: chance \\(\\dfrac1{8\\,145\\,060}\\approx0{,}00000012\\).', 'Chỉ một vé trúng: cơ hội \\(\\dfrac1{8\\,145\\,060}\\approx0{,}00000012\\).')],
  T('8 145 060 tickets; about 1 in 8 million.', '8 145 060 vé; khoảng 1 phần 8 triệu.'))


def lvl(P):
    n1 = P['perm']
    o1 = M4(1, 'In how many ways can %d people stand in a queue?' % n1, 'Có bao nhiêu cách xếp %d người thành một hàng dọc?' % n1, '\\(%d\\)' % math.factorial(n1),
            ['\\(%d\\)' % (n1 * n1), '\\(%d\\)' % math.factorial(n1 - 1), '\\(%d\\)' % (2 ** n1)], '\\(P_{%d}=%d!\\).' % (n1, n1), '\\(P_{%d}=%d!=%d\\).' % (n1, n1, math.factorial(n1)))
    n2, k2 = P['arr']
    o2 = M4(2, 'From %d candidates choose %d people for %d different posts. Number of ways?' % (n2, k2, k2), 'Từ %d ứng viên chọn %d người vào %d chức vụ khác nhau. Số cách là…' % (n2, k2, k2), '\\(A_{%d}^{%d}=%d\\)' % (n2, k2, A(n2, k2)),
            ['\\(C_{%d}^{%d}=%d\\)' % (n2, k2, C(n2, k2)), '\\(%d^{%d}=%d\\)' % (n2, k2, n2 ** k2), '\\(%d!=%d\\)' % (k2, math.factorial(k2))], 'Order matters.', 'Có phân biệt chức vụ (có thứ tự): chỉnh hợp.')
    n3, k3 = P['comb']
    o3 = M4(3, 'From %d students choose a group of %d. Number of ways?' % (n3, k3), 'Từ %d học sinh chọn một nhóm %d bạn. Số cách là…' % (n3, k3), '\\(C_{%d}^{%d}=%d\\)' % (n3, k3, C(n3, k3)),
            ['\\(A_{%d}^{%d}=%d\\)' % (n3, k3, A(n3, k3)), '\\(%d!=%d\\)' % (n3, math.factorial(n3)), '\\(%d^{%d}=%d\\)' % (k3, n3, k3 ** n3)], 'No order.', 'Không kể thứ tự: tổ hợp.')
    (se, sv), val = P['id']
    t4 = tf(4, se, sv, val, 'Compute both sides.', 'Tính hai vế để kiểm tra.')
    n5, claim = P['diag']; real = C(n5, 2) - n5
    t5 = tf(5, 'A convex polygon with %d sides has %d diagonals.' % (n5, claim), 'Đa giác lồi %d cạnh có %d đường chéo.' % (n5, claim), real == claim, '\\(C_{%d}^2-%d=%d\\).' % (n5, n5, real), '\\(C_{%d}^2-%d=%d\\).' % (n5, n5, real))
    m, f, a, b = P['team']; real6 = C(m, a) * C(f, b)
    s6 = sh(6, 'A class has %d boys and %d girls. How many ways to choose %d boys and %d girls?' % (m, f, a, b), 'Một lớp có %d nam, %d nữ. Có bao nhiêu cách chọn %d nam và %d nữ?' % (m, f, a, b), real6,
            '\\(C_{%d}^{%d}\\cdot C_{%d}^{%d}\\).' % (m, a, f, b), '\\(C_{%d}^{%d}\\cdot C_{%d}^{%d}=%d\\).' % (m, a, f, b, real6))
    (te, tv), n7, k7 = P['real']; real7 = C(n7, k7)
    s7 = sh(7, te, tv, real7, '\\(C_{%d}^{%d}\\).' % (n7, k7), 'Không kể thứ tự: \\(C_{%d}^{%d}=%d\\).' % (n7, k7, real7))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]


assert C(10, 3) == C(10, 7) and A(8, 2) != C(8, 2) and A(7, 3) == 6 * C(7, 3)
PP = [dict(perm=6, arr=(10, 3), comb=(12, 4), id=(('\\(C_{10}^3=C_{10}^7\\).', '\\(C_{10}^3=C_{10}^7\\).'), True), diag=(6, 9), team=(8, 6, 2, 1), real=(('A lottery ticket picks 5 numbers from 1 to 35 (order not important). How many tickets are there?', 'Mỗi vé xổ số chọn 5 số từ 1 đến 35 (không kể thứ tự). Có bao nhiêu vé khác nhau?'), 35, 5)),
      dict(perm=7, arr=(12, 2), comb=(15, 3), id=(('\\(A_8^2=C_8^2\\).', '\\(A_8^2=C_8^2\\).'), False), diag=(8, 24), team=(10, 7, 1, 2), real=(('A league has 20 teams; every two teams play exactly one match. How many matches?', 'Một giải đấu có 20 đội, mỗi hai đội gặp nhau đúng một trận. Có bao nhiêu trận?'), 20, 2)),
      dict(perm=5, arr=(9, 4), comb=(14, 5), id=(('\\(A_7^3=3!\\cdot C_7^3\\).', '\\(A_7^3=3!\\cdot C_7^3\\).'), True), diag=(10, 35), team=(9, 8, 2, 2), real=(('A test takes 3 questions from a bank of 30 (order not important). How many different tests?', 'Một đề kiểm tra lấy 3 câu từ ngân hàng 30 câu (không kể thứ tự). Có bao nhiêu đề khác nhau?'), 30, 3))]
practice = three(lvl, PP)
practice = with_self(practice, S.M24S10, start=8)
mistakes = [('<b>Using \\(C\\) when order matters.</b> President–vice–secretary is ordered: \\(A_n^3\\), not \\(C_n^3\\).', '<b>Dùng \\(C\\) khi có thứ tự.</b> Chủ nhiệm – phó – thư kí có phân biệt: \\(A_n^3\\), không phải \\(C_n^3\\).'),
            ('<b>Using \\(A\\) for a group.</b> A team of 3 is the same in any order: \\(C_n^3\\).', '<b>Dùng \\(A\\) cho một nhóm.</b> Đội 3 người không đổi khi đổi thứ tự: \\(C_n^3\\).'),
            ('<b>Forgetting internal orders of a block.</b> Two friends side by side can swap: multiply by 2.', '<b>Quên hoán đổi bên trong khối.</b> Hai bạn ngồi cạnh nhau có thể đổi chỗ: nhân thêm 2.'),
            ('<b>Adding instead of multiplying in mixed teams.</b> Boys <i>and</i> girls: \\(C_m^a\\cdot C_f^b\\).', '<b>Cộng thay vì nhân khi chọn đội hỗn hợp.</b> Chọn nam <i>và</i> nữ: \\(C_m^a\\cdot C_f^b\\).')]
summary = [('\\(P_n=n!\\) (order all), \\(A_n^k=\\dfrac{n!}{(n-k)!}\\) (choose and order), \\(C_n^k=\\dfrac{n!}{k!(n-k)!}\\) (choose).', '\\(P_n=n!\\) (xếp tất cả), \\(A_n^k=\\dfrac{n!}{(n-k)!}\\) (chọn và xếp), \\(C_n^k=\\dfrac{n!}{k!(n-k)!}\\) (chỉ chọn).'),
           ('\\(A_n^k=k!\\,C_n^k\\); \\(C_n^k=C_n^{n-k}\\); \\(C_n^k+C_n^{k+1}=C_{n+1}^{k+1}\\).', '\\(A_n^k=k!\\,C_n^k\\); \\(C_n^k=C_n^{n-k}\\); \\(C_n^k+C_n^{k+1}=C_{n+1}^{k+1}\\).'),
           ('Swap test: different outcome → order matters.', 'Phép thử đổi chỗ: kết quả khác → có thứ tự.'), ('Key words: permutation, arrangement, combination, factorial.', 'Từ cần nhớ: permutation, arrangement, combination, factorial.')]
checks = [('I can tell \\(P\\), \\(A\\), \\(C\\) apart.', 'Em phân biệt được \\(P\\), \\(A\\), \\(C\\).'), ('I can compute them by hand and with a calculator.', 'Em tính được bằng tay và bằng máy tính cầm tay.'),
          ('I can count seatings with conditions.', 'Em đếm được cách xếp chỗ có điều kiện.'), ('I can count teams and lottery tickets.', 'Em đếm được số đội, số vé xổ số.')]
LL('g10-comb-02', 'Permutations, Arrangements and Combinations', CV, ('Combinatorics', 'Đại số tổ hợp'), 'combinatorics', 'permutations-combinations', 240, 'Intermediate', 75, ('counting rules', 'quy tắc đếm'),
   'Permutations, arrangements, combinations; choosing the right formula; seatings, teams, lotteries.', 'Bài 24 – Hoán vị, chỉnh hợp, tổ hợp; chọn đúng công thức; xếp chỗ, lập đội, xổ số.',
   ['permutation', 'arrangement', 'combination'], ['hoán vị', 'chỉnh hợp', 'tổ hợp'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g10-comb-01'])
