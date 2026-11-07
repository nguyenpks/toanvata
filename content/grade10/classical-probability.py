# -*- coding: utf-8 -*-
"""g10-prob-01 = Toán 10 KNTT, Bài 26: Biến cố và định nghĩa cổ điển của xác suất. Mã ngân hàng câu hỏi: TOAN10-C9-B26."""
import os, sys, math, itertools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g10j as S
import mb_pgf

C = math.comb
CV = 'Biến cố và định nghĩa cổ điển của xác suất'
vocab = defs(CV, [
 ('randexp', 'random experiment', 'phép thử ngẫu nhiên', 'an action whose result cannot be predicted, although all possible results are known.', 'hoạt động mà ta không đoán trước được kết quả, dù đã biết tập hợp các kết quả có thể xảy ra.', 'Rolling a die is a random experiment.', ''),
 ('samplesp', 'sample space', 'không gian mẫu', 'the set of all possible outcomes of an experiment.', 'tập hợp tất cả các kết quả có thể xảy ra của phép thử.', 'The sample space has 36 outcomes.', '\\(\\Omega\\)'),
 ('event10', 'event', 'biến cố (phép thử)', 'a subset of the sample space.', 'một tập con của không gian mẫu.', 'A is the event "the sum is 7".', '\\(A\\subset\\Omega\\)'),
 ('compev', 'complementary event', 'biến cố đối', 'the event \\(\\overline A=\\Omega\\setminus A\\): "\\(A\\) does not occur".', 'biến cố \\(\\overline A=\\Omega\\setminus A\\): "\\(A\\) không xảy ra".', 'The complement of "at least one boy" is "all girls".', '\\(\\overline A\\)'),
 ('classprob', 'classical probability', 'định nghĩa cổ điển của xác suất', '\\(P(A)=\\dfrac{n(A)}{n(\\Omega)}\\) when all outcomes are equally likely.', '\\(P(A)=\\dfrac{n(A)}{n(\\Omega)}\\) khi các kết quả đồng khả năng.', 'The probability of a six is 1/6.', '\\(P(A)\\)')])
goals = [('recognise random experiments, sample spaces and events;', 'nhận biết [[phép thử ngẫu nhiên]], [[không gian mẫu]], [[biến cố (phép thử)|biến cố (phép thử)]], [[biến cố đối]];'),
         ('compute probabilities with the classical definition;', 'tính xác suất bằng [[định nghĩa cổ điển của xác suất]];'),
         ('count favourable outcomes with tables, trees and combinations;', 'đếm số kết quả thuận lợi bằng bảng, sơ đồ cây, tổ hợp;'),
         ('use complements and interpret lotteries and games.', 'dùng biến cố đối; giải thích cơ hội trong xổ số, trò chơi.')]
phrases = [('<b>The sample space has thirty-six equally likely outcomes.</b>', 'Không gian mẫu có 36 kết quả đồng khả năng.'), ('<b>There are six favourable outcomes.</b>', 'Có 6 kết quả thuận lợi.'),
           ('<b>The probability of the complement is one minus the probability.</b>', 'Xác suất của biến cố đối bằng 1 trừ xác suất của biến cố.'), ('<b>The chance of winning is very small.</b>', 'Cơ hội trúng thưởng rất nhỏ.'), ('<b>List all the outcomes.</b>', 'Liệt kê tất cả các kết quả.')]
review = T('From Bài 23–24: rules of sum and product, \\(C_n^k\\). From Bài 2: subsets, complement \\(\\Omega\\setminus A\\).', 'Từ Bài 23–24: quy tắc cộng, quy tắc nhân, \\(C_n^k\\). Từ Bài 2: tập con, phần bù \\(\\Omega\\setminus A\\).')
theory = '<h3>26.1 %s</h3>' % TI('Experiments, sample spaces, events', 'Phép thử, không gian mẫu, biến cố')
theory += BOX('blue', ('Definitions', 'Định nghĩa'), UL([T('A random experiment has outcomes we cannot predict; the set of all outcomes is the sample space \\(\\Omega\\).', 'Phép thử ngẫu nhiên có kết quả không đoán trước được; tập hợp mọi kết quả là không gian mẫu \\(\\Omega\\).'),
  T('An event is a subset \\(A\\subset\\Omega\\); outcomes in \\(A\\) are <b>favourable</b> to \\(A\\). \\(\\Omega\\) is the sure event, \\(\\varnothing\\) the impossible event.', 'Biến cố là một tập con \\(A\\subset\\Omega\\); các kết quả thuộc \\(A\\) là kết quả <b>thuận lợi</b> cho \\(A\\). \\(\\Omega\\) là biến cố chắc chắn, \\(\\varnothing\\) là biến cố không thể.'),
  T('The complementary event \\(\\overline A=\\Omega\\setminus A\\) occurs exactly when \\(A\\) does not.', 'Biến cố đối \\(\\overline A=\\Omega\\setminus A\\) xảy ra khi và chỉ khi \\(A\\) không xảy ra.')]))
theory += '<h3>26.2 %s</h3>' % TI('Classical definition of probability', 'Định nghĩa cổ điển của xác suất')
theory += BOX('mint', ('Formula and properties', 'Công thức và tính chất'), UL([T('If all outcomes of \\(\\Omega\\) are equally likely: \\(P(A)=\\dfrac{n(A)}{n(\\Omega)}\\).', 'Nếu các kết quả của \\(\\Omega\\) đồng khả năng: \\(P(A)=\\dfrac{n(A)}{n(\\Omega)}\\).'),
  T('\\(0\\le P(A)\\le1\\), \\(P(\\Omega)=1\\), \\(P(\\varnothing)=0\\), \\(P(\\overline A)=1-P(A)\\).', '\\(0\\le P(A)\\le1\\), \\(P(\\Omega)=1\\), \\(P(\\varnothing)=0\\), \\(P(\\overline A)=1-P(A)\\).'),
  T('Principle of small probability: an event with a very small probability is practically considered not to happen in a single trial.', 'Nguyên lí xác suất bé: biến cố có xác suất rất nhỏ thì trong thực tế coi như không xảy ra trong một lần thử.')]))
cells = []
for a in range(1, 7):
    for b in range(1, 7):
        on = a + b == 7
        cells.append('\\node[draw=ink!35, minimum size=0.78cm, inner sep=0pt, fill=%s, font=\\small] at (%s,%s) {$%d$};' % ('mint!80' if on else 'white', a * 0.8, -b * 0.8, a + b))
grid = mb_pgf.raw_svg('\\begin{tikzpicture}\n' + '\n'.join(cells) + '\n' + '\n'.join('\\node[font=\\small\\bfseries, text=ink] at (%s,0) {%d}; \\node[font=\\small\\bfseries, text=ink] at (0,%s) {%d};' % (k * 0.8, k, -k * 0.8, k) for k in range(1, 7)) +
                      '\n\\node[font=\\footnotesize, text=ink!70, anchor=south] at (2.8,0.35) {xúc xắc 1 / die 1};\n\\node[font=\\footnotesize, text=ink!70, rotate=90, anchor=south] at (-0.35,-2.8) {xúc xắc 2 / die 2};\n\\end{tikzpicture}')
theory += mb_pgf.img(grid, 'Table of the 36 sums of two dice; the 6 cells with sum 7 are shaded', 380, TI('The 36 outcomes of two dice (sums shown). The 6 shaded cells give sum 7: \\(P=\\frac6{36}=\\frac16\\).', '36 kết quả khi gieo hai con xúc xắc (ghi tổng). 6 ô tô màu có tổng bằng 7: \\(P=\\frac6{36}=\\frac16\\).'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('The formula needs <b>equally likely</b> outcomes: the sums 2, 3, …, 12 are <i>not</i> equally likely, so do not write \\(P(\\text{sum}=7)=\\frac1{11}\\).', 'Công thức chỉ dùng khi các kết quả <b>đồng khả năng</b>: các tổng 2, 3, …, 12 <i>không</i> đồng khả năng nên không được viết \\(P(\\text{tổng}=7)=\\frac1{11}\\).'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Two coins', 'Hai lần gieo đồng xu'), T('A coin is tossed twice. Describe \\(\\Omega\\) and find the probability of at least one head (S = head, N = tail).', 'Gieo một đồng xu hai lần. Mô tả không gian mẫu và tính xác suất có ít nhất một lần xuất hiện mặt sấp (S: sấp, N: ngửa).'),
  T('List the outcomes.', 'Liệt kê các kết quả.'), [T('\\(\\Omega=\\{SS,SN,NS,NN\\}\\), \\(n(\\Omega)=4\\).', '\\(\\Omega=\\{SS,SN,NS,NN\\}\\), \\(n(\\Omega)=4\\).'), T('\\(A=\\{SS,SN,NS\\}\\), or \\(\\overline A=\\{NN\\}\\): \\(P(A)=1-\\frac14\\).', '\\(A=\\{SS,SN,NS\\}\\), hoặc \\(\\overline A=\\{NN\\}\\): \\(P(A)=1-\\frac14\\).')], T('\\(P(A)=\\dfrac34\\).', '\\(P(A)=\\dfrac34\\).'))
D2 = list(itertools.product(range(1, 7), repeat=2)); assert sum(a + b == 7 for a, b in D2) == 6 and sum(a + b >= 10 for a, b in D2) == 6
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Two dice', 'Hai con xúc xắc'), T('Two dice are rolled. Find \\(P(\\text{sum}=7)\\) and \\(P(\\text{sum}\\ge10)\\).', 'Gieo hai con xúc xắc. Tính \\(P(\\text{tổng}=7)\\) và \\(P(\\text{tổng}\\ge10)\\).'),
  T('\\(n(\\Omega)=6\\cdot6=36\\); use the table.', '\\(n(\\Omega)=6\\cdot6=36\\); dùng bảng.'), [T('Sum 7: \\((1,6),(2,5),\\dots,(6,1)\\): 6 outcomes.', 'Tổng 7: \\((1,6),(2,5),\\dots,(6,1)\\): 6 kết quả.'), T('Sum \\(\\ge10\\): \\((4,6),(5,5),(6,4),(5,6),(6,5),(6,6)\\): 6 outcomes.', 'Tổng \\(\\ge10\\): \\((4,6),(5,5),(6,4),(5,6),(6,5),(6,6)\\): 6 kết quả.')],
  T('Both equal \\(\\dfrac16\\).', 'Cả hai bằng \\(\\dfrac16\\).'))
assert F(C(5, 2) * 4, C(9, 3)) == F(10, 21)
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Drawing balls', 'Lấy cầu'), T('A box has 5 red and 4 blue balls. Three balls are drawn at random. Find the probability of exactly 2 red balls.', 'Một hộp có 5 quả cầu đỏ và 4 quả cầu xanh. Lấy ngẫu nhiên 3 quả. Tính xác suất lấy được đúng 2 quả đỏ.'),
  T('\\(n(\\Omega)=C_9^3\\).', '\\(n(\\Omega)=C_9^3\\).'), [T('\\(n(\\Omega)=84\\); favourable: \\(C_5^2\\cdot C_4^1=10\\cdot4=40\\).', '\\(n(\\Omega)=84\\); thuận lợi: \\(C_5^2\\cdot C_4^1=10\\cdot4=40\\).')], T('\\(\\dfrac{40}{84}=\\dfrac{10}{21}\\).', '\\(\\dfrac{40}{84}=\\dfrac{10}{21}\\).'))
assert 1 - F(C(12, 4), C(20, 4)) == F(290, 323)
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Using the complement', 'Dùng biến cố đối'), T('A group has 8 boys and 12 girls. Four students are chosen at random. Find the probability that at least one boy is chosen.', 'Một nhóm có 8 nam và 12 nữ. Chọn ngẫu nhiên 4 bạn. Tính xác suất chọn được ít nhất một nam.'),
  T('Complement: all four are girls.', 'Biến cố đối: cả bốn bạn đều là nữ.'), [T('\\(P(\\overline A)=\\dfrac{C_{12}^4}{C_{20}^4}=\\dfrac{495}{4845}=\\dfrac{33}{323}\\).', '\\(P(\\overline A)=\\dfrac{C_{12}^4}{C_{20}^4}=\\dfrac{495}{4845}=\\dfrac{33}{323}\\).')],
  T('\\(P(A)=1-\\dfrac{33}{323}=\\dfrac{290}{323}\\approx0{,}90\\).', '\\(P(A)=1-\\dfrac{33}{323}=\\dfrac{290}{323}\\approx0{,}90\\).'))
p3 = F(C(6, 3) * C(39, 3), C(45, 6)); assert p3 == F(9139, 407253)
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Mega 6/45: three correct numbers', 'Mega 6/45: trúng ba số'), T('A Mega 6/45 ticket has 6 numbers; 6 winning numbers are drawn from 1–45. What is the probability that a ticket matches exactly 3 winning numbers?', 'Mỗi vé Mega 6/45 có 6 số; xổ ra 6 số trúng thưởng trong 45 số. Tính xác suất một vé trùng đúng 3 số trúng thưởng.'),
  T('Choose which 3 of the 6 winning numbers are on the ticket, and 3 of the 39 others.', 'Chọn 3 trong 6 số trúng có trên vé và 3 trong 39 số còn lại.'),
  [T('\\(n(\\Omega)=C_{45}^6=8\\,145\\,060\\); favourable \\(C_6^3\\cdot C_{39}^3=20\\cdot9139=182\\,780\\).', '\\(n(\\Omega)=C_{45}^6=8\\,145\\,060\\); thuận lợi \\(C_6^3\\cdot C_{39}^3=20\\cdot9139=182\\,780\\).'), T('\\(P\\approx0{,}0224\\): about 1 ticket in 45.', '\\(P\\approx0{,}0224\\): khoảng 1 vé trong 45 vé.')],
  T('\\(P=\\dfrac{9139}{407253}\\approx2{,}2\\%\\).', '\\(P=\\dfrac{9139}{407253}\\approx2{,}2\\%\\).'))


def lvl(P):
    s = P['sum']; k = sum(1 for a, b in D2 if a + b == s)
    o1 = M4(1, 'Two dice are rolled. \\(P(\\text{sum}=%d)=\\)…' % s, 'Gieo hai con xúc xắc. \\(P(\\text{tổng}=%d)\\) bằng…' % s, '\\(%s\\)' % fr(F(k, 36)),
            ['\\(%s\\)' % fr(F(1, 11)), '\\(%s\\)' % fr(F(k + 1, 36)), '\\(%s\\)' % fr(F(k, 6))], '%d favourable outcomes.' % k, 'Có %d kết quả thuận lợi trên 36.' % k)
    n, kk = P['coin']
    o2 = M4(2, '%d coins are tossed. \\(P(\\text{exactly %d heads})=\\)…' % (n, kk), 'Gieo %d đồng xu. Xác suất có đúng %d mặt sấp là…' % (n, kk), '\\(%s\\)' % fr(F(C(n, kk), 2 ** n)),
            ['\\(%s\\)' % fr(F(1, 2 ** n)), '\\(%s\\)' % fr(F(kk, n)), '\\(%s\\)' % fr(F(1, n + 1))], '\\(C_{%d}^{%d}/2^{%d}\\).' % (n, kk, n), '\\(\\dfrac{C_{%d}^{%d}}{2^{%d}}\\).' % (n, kk, n))
    a, b = P['two']
    o3 = M4(3, 'A box has %d white and %d black balls; two are drawn. \\(P(\\text{both black})=\\)…' % (a, b), 'Hộp có %d cầu trắng, %d cầu đen; lấy ngẫu nhiên 2 quả. Xác suất cả hai đều đen là…' % (a, b), '\\(%s\\)' % fr(F(C(b, 2), C(a + b, 2))),
            ['\\(%s\\)' % fr(F(b, a + b) ** 2), '\\(%s\\)' % fr(F(b, a + b)), '\\(%s\\)' % fr(F(C(a, 2), C(a + b, 2)))], '\\(\\dfrac{C_{%d}^2}{C_{%d}^2}\\).' % (b, a + b), '\\(\\dfrac{C_{%d}^2}{C_{%d}^2}\\).' % (b, a + b))
    (r_, g_), claim = P['comp']; real = F(g_, r_ + g_)
    t4 = tf(4, 'A box has %d red and %d green balls. One is drawn. \\(P(\\text{not red})=%s\\).' % (r_, g_, fr(claim)), 'Hộp có %d cầu đỏ và %d cầu xanh. Lấy ngẫu nhiên 1 quả. Xác suất không lấy được quả đỏ là \\(%s\\).' % (r_, g_, fr(claim)), real == claim,
            '\\(1-\\dfrac{%d}{%d}=%s\\).' % (r_, r_ + g_, fr(real)), '\\(P(\\overline A)=1-\\dfrac{%d}{%d}=%s\\).' % (r_, r_ + g_, fr(real)))
    (te, tv), v5 = P['dice']
    t5 = tf(5, te, tv, v5, 'Use the 36-cell table.', 'Dùng bảng 36 ô.')
    (oe, ov), n6 = P['omega']
    s6 = sh(6, oe, ov, n6, 'Rule of product / combinations.', 'Dùng quy tắc nhân hoặc tổ hợp.')
    (le, lv_), n7 = P['lotto']
    s7 = sh(7, le, lv_, n7, 'Choose the matching numbers, then the others.', 'Chọn các số trùng, rồi chọn các số còn lại.')
    return [[o1, o2, o3], [t4, t5], [s6, s7]]


assert F(sum(a == b for a, b in D2), 36) == F(1, 6) and F(sum((a + b) % 2 for a, b in D2), 36) == F(1, 2) and F(sum(6 in (a, b) for a, b in D2), 36) == F(11, 36)
PP = [dict(sum=8, coin=(3, 2), two=(4, 5), comp=((3, 7), F(7, 10)), dice=(('Two dice: P(both show the same number) = 1/6.', 'Gieo hai con xúc xắc: xác suất hai mặt có cùng số chấm bằng \\(\\frac16\\).'), True),
           omega=(('Two students are chosen from 10 for a duty. How many elements does the sample space have?', 'Chọn 2 trong 10 học sinh đi trực. Không gian mẫu có bao nhiêu phần tử?'), 45),
           lotto=(('In a 5/35 lottery, how many tickets match exactly 4 of the 5 winning numbers?', 'Trong xổ số 5/35, có bao nhiêu vé trùng đúng 4 trong 5 số trúng thưởng?'), C(5, 4) * C(30, 1))),
      dict(sum=5, coin=(4, 3), two=(6, 3), comp=((5, 3), F(5, 8)), dice=(('Two dice: P(the sum is odd) = 1/3.', 'Gieo hai con xúc xắc: xác suất tổng số chấm là số lẻ bằng \\(\\frac13\\).'), False),
           omega=(('Three coins are tossed and a die is rolled. How many elements does the sample space have?', 'Gieo ba đồng xu và một con xúc xắc. Không gian mẫu có bao nhiêu phần tử?'), 48),
           lotto=(('In Mega 6/45, how many tickets match exactly 5 of the 6 winning numbers?', 'Trong Mega 6/45, có bao nhiêu vé trùng đúng 5 trong 6 số trúng thưởng?'), C(6, 5) * C(39, 1))),
      dict(sum=10, coin=(4, 2), two=(3, 7), comp=((2, 6), F(3, 4)), dice=(('Two dice: P(at least one six) = 11/36.', 'Gieo hai con xúc xắc: xác suất có ít nhất một mặt 6 chấm bằng \\(\\frac{11}{36}\\).'), True),
           omega=(('Three dice are rolled. How many elements does the sample space have?', 'Gieo ba con xúc xắc. Không gian mẫu có bao nhiêu phần tử?'), 216),
           lotto=(('In a 5/35 lottery, how many tickets match exactly 3 of the 5 winning numbers?', 'Trong xổ số 5/35, có bao nhiêu vé trùng đúng 3 trong 5 số trúng thưởng?'), C(5, 3) * C(30, 2)))]
practice = three(lvl, PP)
practice = with_self(practice, S.M26S10, start=8)
mistakes = [('<b>Using outcomes that are not equally likely.</b> Sums of two dice are not equally likely: use ordered pairs.', '<b>Dùng các kết quả không đồng khả năng.</b> Các tổng của hai xúc xắc không đồng khả năng: phải dùng cặp có thứ tự.'),
            ('<b>Counting \\((1,6)\\) and \\((6,1)\\) as one outcome.</b> The two dice are different: they are two outcomes.', '<b>Coi \\((1,6)\\) và \\((6,1)\\) là một kết quả.</b> Hai con xúc xắc khác nhau: đó là hai kết quả.'),
            ('<b>Mixing order and no order.</b> If \\(n(\\Omega)\\) uses \\(C\\), the favourable count must use \\(C\\) too.', '<b>Lẫn lộn có thứ tự và không thứ tự.</b> Nếu \\(n(\\Omega)\\) dùng \\(C\\) thì số kết quả thuận lợi cũng phải dùng \\(C\\).'),
            ('<b>Long case-work for "at least".</b> Use \\(P(A)=1-P(\\overline A)\\).', '<b>Chia nhiều trường hợp cho "ít nhất".</b> Dùng \\(P(A)=1-P(\\overline A)\\).')]
summary = [('\\(\\Omega\\): all outcomes; event \\(A\\subset\\Omega\\); \\(\\overline A=\\Omega\\setminus A\\).', '\\(\\Omega\\): mọi kết quả; biến cố \\(A\\subset\\Omega\\); \\(\\overline A=\\Omega\\setminus A\\).'), ('\\(P(A)=\\dfrac{n(A)}{n(\\Omega)}\\) (equally likely outcomes).', '\\(P(A)=\\dfrac{n(A)}{n(\\Omega)}\\) (các kết quả đồng khả năng).'),
           ('\\(0\\le P(A)\\le1\\); \\(P(\\overline A)=1-P(A)\\).', '\\(0\\le P(A)\\le1\\); \\(P(\\overline A)=1-P(A)\\).'), ('Key words: experiment, sample space, event, complement, probability.', 'Từ cần nhớ: experiment, sample space, event, complement, probability.')]
checks = [('I can describe a sample space.', 'Em mô tả được không gian mẫu.'), ('I can compute classical probabilities.', 'Em tính được xác suất theo định nghĩa cổ điển.'), ('I can use the complement.', 'Em dùng được biến cố đối.'), ('I can explain lottery chances.', 'Em giải thích được cơ hội trúng xổ số.')]
LL('g10-prob-01', 'Events and Classical Probability', CV, ('Classical Probability', 'Xác suất theo định nghĩa cổ điển'), 'probability', 'classical-probability', 260, 'Intermediate', 70, ('counting, combinations', 'quy tắc đếm, tổ hợp'),
   'Random experiments, sample spaces, events, complements; classical definition of probability; dice, cards, lotteries.', 'Bài 26 – Phép thử, không gian mẫu, biến cố, biến cố đối; định nghĩa cổ điển của xác suất; xúc xắc, thẻ, xổ số.',
   ['sample space', 'event', 'probability'], ['không gian mẫu', 'biến cố', 'xác suất'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g10-comb-02'])
