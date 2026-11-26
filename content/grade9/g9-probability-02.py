# -*- coding: utf-8 -*-
"""Nội dung bài g9-probability-02 = Toán 9 KNTT, Bài 26: Xác suất của biến cố liên quan tới phép thử – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 8 – Lesson 26; Mini project Ch.8 (Data, Chance and Decision Making)."""
import os, sys
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9, sp_g9p

LID = 'g9-probability-02'
CH = 'Xác suất'
TOPIC = ('Probability', 'Xác suất của biến cố trong một số mô hình xác suất đơn giản')
ensure_vocab([
 ('g9-favorable', 'favorable outcome', 'kết quả thuận lợi (cho biến cố)', CH, 'The outcome 2 is favorable to the event “the number is even”.', ''),
 ('g9-probability', 'probability', 'xác suất (của biến cố)', CH, 'The probability of getting a 6 is 1/6.', r'\(P(A)\)'),
 ('g9-fair', 'fair (coin, die)', 'cân đối và đồng chất (đồng xu, xúc xắc)', CH, 'A fair die: each face is equally likely.', ''),
])
load_vocab()

# ---------- số liệu (kiểm tra bằng máy) ----------
D2 = [(i, j) for i in range(1, 7) for j in range(1, 7)]
S7 = [x for x in D2 if sum(x) == 7]; assert len(S7) == 6 and F(len(S7), 36) == F(1, 6)
C20 = [x for x in range(1, 21) if x % 4 == 0]; assert C20 == [4, 8, 12, 16, 20] and F(5, 20) == F(1, 4)
SPA, SPB = [1, 2, 3], [1, 2, 3, 4]
EV = [(a, b) for a in SPA for b in SPB if (a * b) % 2 == 0]; assert len(EV) == 8 and F(8, 12) == F(2, 3)
G1, G2, G3 = F(1, 6), F(1, 4), F(len([x for x in D2 if sum(x) >= 10]), 36)
assert G3 == F(1, 6) and G2 > G1 == G3 and 1 - G2 == F(3, 4)

def DICE_HL(fav, cap):
    h = '<tr><th scope="col">%s</th>%s</tr>' % (TI('Die 1 \\ Die 2', 'Xúc xắc 1 \\ Xúc xắc 2'), ''.join('<th scope="col">%d</th>' % j for j in range(1, 7)))
    b = ''.join('<tr><th scope="row">%d</th>%s</tr>' % (i, ''.join('<td%s>\\((%d;\\,%d)\\)</td>' % (' style="background:#fde68a;font-weight:700"' if (i, j) in fav else '', i, j) for j in range(1, 7))) for i in range(1, 7))
    return ('<figure class="mbl-fig"><div class="mbl-tablewrap mbl-freqwrap"><table class="mbl-table mbl-freq"><tbody>%s%s</tbody></table></div><figcaption>%s</figcaption></figure>' % (h, b, TI(*cap)))

def SPIN_HL():
    h = '<tr><th scope="col">%s</th>%s</tr>' % (TI('A \\ B', 'A \\ B'), ''.join('<th scope="col">%d</th>' % j for j in SPB))
    b = ''.join('<tr><th scope="row">%d</th>%s</tr>' % (a, ''.join('<td%s>\\(%d\\)</td>' % (' style="background:#fde68a;font-weight:700"' if (a, c) in EV else '', a * c) for c in SPB)) for a in SPA)
    return ('<figure class="mbl-fig"><div class="mbl-tablewrap mbl-freqwrap"><table class="mbl-table mbl-freq"><tbody>%s%s</tbody></table></div><figcaption>%s</figcaption></figure>'
            % (h, b, TI('Products of the two numbers (even products highlighted)', 'Tích hai số (tích chẵn được tô màu)')))

meta = dict(level=('Basic', 'Cơ bản'), time=('about 90 minutes', '90 phút'), before=('Lesson 25: sample spaces', 'Bài 25: không gian mẫu'))
goals = [
 (r'recognize an event, its favorable outcomes and equally likely outcomes;', r'nhận biết được biến cố, kết quả thuận lợi cho biến cố và các kết quả đồng khả năng;'),
 (r'use \(P(A)=\dfrac{n(A)}{n(\Omega)}\) for one-step experiments;', r'dùng công thức \(P(A)=\dfrac{n(A)}{n(\Omega)}\) với phép thử một bước;'),
 (r'compute probabilities in two-step experiments (two dice, two spinners);', r'tính được xác suất trong phép thử hai bước (hai con xúc xắc, hai vòng quay);'),
 (r'use probabilities to make decisions (games at a school fair).', r'dùng xác suất để ra quyết định (trò chơi ở hội chợ trường).')]
vocab = [
 (r'<b>event</b> – a statement about the outcome of an experiment; it happens or does not happen.', r'[[Biến cố|biến cố (phép thử)]] – một sự kiện liên quan đến kết quả của phép thử; nó có thể xảy ra hoặc không xảy ra.'),
 (r'<b>favorable outcome</b> – an outcome that makes the event happen.', r'[[Kết quả thuận lợi|kết quả thuận lợi (cho biến cố)]] – kết quả làm cho biến cố xảy ra.'),
 (r'<b>equally likely outcomes</b> – outcomes that have the same chance.', r'Các kết quả [[đồng khả năng]] – các kết quả có khả năng xảy ra như nhau.'),
 (r'<b>probability</b> \(P(A)\) – a number from 0 to 1 measuring how likely \(A\) is.', r'[[Xác suất|xác suất (của biến cố)]] \(P(A)\) – số từ 0 đến 1 đo khả năng xảy ra của biến cố \(A\).'),
 (r'<b>fair coin / fair die</b> – a coin or die whose faces are equally likely.', r'Đồng xu, xúc xắc [[cân đối và đồng chất|cân đối và đồng chất (đồng xu, xúc xắc)]] – các mặt có khả năng xuất hiện như nhau.')]
phrases = [
 (r'<b>The outcomes 2, 4, 6 are favorable to the event \(A\).</b>', r'Các kết quả 2, 4, 6 là các kết quả thuận lợi cho biến cố \(A\).'),
 (r'<b>The outcomes are equally likely.</b>', r'Các kết quả là đồng khả năng.'),
 (r'<b>Find the probability of the event \(A\).</b>', r'Tính xác suất của biến cố \(A\).'),
 (r'<b>The probability of getting a sum of 7 is \(\dfrac{1}{6}\).</b>', r'Xác suất để tổng số chấm bằng 7 là \(\dfrac{1}{6}\).'),
 (r'<b>Which game gives you the best chance of winning?</b>', r'Trò chơi nào cho em cơ hội thắng cao nhất?')]
review = (T(r'<b>Lesson 25.</b> The sample space \(\Omega\) is the set of all possible outcomes; \(n(\Omega)\) is the number of its outcomes.', r'<b>Bài 25.</b> Không gian mẫu \(\Omega\) là tập hợp tất cả các kết quả có thể; \(n(\Omega)\) là số phần tử của nó.') +
          T(r'<b>Fractions.</b> Simplify: \(\dfrac{6}{36}=\dfrac{1}{6}\).', r'<b>Phân số.</b> Rút gọn: \(\dfrac{6}{36}=\dfrac{1}{6}\).'))

theory = '<h3>5.1 %s</h3>' % TI('Events and favorable outcomes', 'Biến cố và kết quả thuận lợi')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'An <b>event</b> related to a random experiment is a statement about the outcome; after the experiment we know whether it happened. An outcome is <b>favorable</b> to the event \(A\) if, when it appears, \(A\) happens.',
    r'[[Biến cố|biến cố (phép thử)]] liên quan tới phép thử là một sự kiện mà việc xảy ra hay không xảy ra của nó phụ thuộc vào kết quả của phép thử. Kết quả làm cho biến cố \(A\) xảy ra gọi là [[kết quả thuận lợi|kết quả thuận lợi (cho biến cố)]] cho \(A\).'))
theory += T(r'Roll a die. For the event \(A\): “the number is even”, the favorable outcomes are 2, 4, 6. If the die shows 3, then \(A\) does not happen.', r'Gieo một con xúc xắc. Với biến cố \(A\): “Số chấm xuất hiện là số chẵn”, các kết quả thuận lợi là 2, 4, 6. Nếu xúc xắc ra 3 chấm thì \(A\) không xảy ra.')
theory += '<h3>5.2 %s</h3>' % TI('The probability of an event', 'Xác suất của biến cố')
theory += BOX('blue', ('Formula', 'Công thức'),
  T(r'Suppose the outcomes of the experiment are <b>equally likely</b> (fair coin, fair die, cards of the same shape…). Then the probability of the event \(A\) is', r'Giả sử các kết quả có thể của phép thử là [[đồng khả năng]] (đồng xu, xúc xắc cân đối và đồng chất, các tấm thẻ giống nhau…). Khi đó xác suất của biến cố \(A\) là'),
  M(r'P(A)=\dfrac{n(A)}{n(\Omega)}'),
  T(r'where \(n(A)\) is the number of favorable outcomes and \(n(\Omega)\) the number of all outcomes. Always \(0\le P(A)\le1\).', r'trong đó \(n(A)\) là số kết quả thuận lợi cho \(A\), \(n(\Omega)\) là số phần tử của không gian mẫu. Luôn có \(0\le P(A)\le1\).'))
theory += BOX('mint', ('Steps', 'Các bước tính'),
  OL([T(r'Describe \(\Omega\) and count \(n(\Omega)\) (list, table or tree diagram).', r'Mô tả không gian mẫu và tính \(n(\Omega)\) (liệt kê, bảng hoặc sơ đồ hình cây).'),
      T(r'Check that the outcomes are equally likely.', r'Kiểm tra các kết quả là đồng khả năng.'),
      T(r'List and count the favorable outcomes \(n(A)\).', r'Liệt kê và đếm các kết quả thuận lợi \(n(A)\).'),
      T(r'Compute \(P(A)=\dfrac{n(A)}{n(\Omega)}\) and simplify.', r'Tính \(P(A)=\dfrac{n(A)}{n(\Omega)}\) rồi rút gọn.')]))
theory += BOX('yellow', ('Extension: the complementary event', 'Mở rộng: biến cố đối'),
  T(r'The event “\(A\) does not happen” is the <b>complementary event</b> \(\overline{A}\). Its favorable outcomes are the other outcomes, so \(P(\overline{A})=1-P(A)\). Example: \(P(\text{not }6)=1-\dfrac{1}{6}=\dfrac{5}{6}\).',
    r'Biến cố “\(A\) không xảy ra” gọi là [[biến cố đối]] của \(A\), kí hiệu \(\overline{A}\). Các kết quả thuận lợi cho \(\overline{A}\) là các kết quả còn lại nên \(P(\overline{A})=1-P(A)\). Ví dụ: xác suất không ra 6 chấm là \(1-\dfrac{1}{6}=\dfrac{5}{6}\).'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Favorable outcomes', 'Kết quả thuận lợi'),
  T(r'Roll a fair die. Let \(A\): “the number is a prime number”. Which outcomes are favorable to \(A\)? Does \(A\) happen if the die shows 4?', r'Gieo một con xúc xắc cân đối. Xét biến cố \(A\): “Số chấm xuất hiện là số nguyên tố”. Những kết quả nào thuận lợi cho \(A\)? Nếu xúc xắc ra 4 chấm thì \(A\) có xảy ra không?'),
  ('The primes from 1 to 6 are 2, 3, 5.', 'Các số nguyên tố từ 1 đến 6 là 2, 3, 5.'),
  [T(r'Favorable outcomes: 2, 3, 5.', r'Các kết quả thuận lợi: 2, 3, 5.'), T(r'4 is not prime, so \(A\) does not happen.', r'4 không là số nguyên tố nên \(A\) không xảy ra.')],
  T(r'2, 3, 5; no.', r'2, 3, 5; không.'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Drawing a card', 'Rút thẻ'),
  T(r'A box has 20 cards numbered 1 to 20. Draw one card at random. Find the probability that the number is a multiple of 4.', r'Một hộp có 20 tấm thẻ đánh số từ 1 đến 20. Rút ngẫu nhiên một thẻ. Tính xác suất để số trên thẻ là bội của 4.'),
  ('The cards are the same, so the 20 outcomes are equally likely.', 'Các tấm thẻ giống nhau nên 20 kết quả là đồng khả năng.'),
  [T(r'\(n(\Omega)=20\). Favorable outcomes: 4, 8, 12, 16, 20, so \(n(A)=5\).', r'\(n(\Omega)=20\). Các kết quả thuận lợi: 4, 8, 12, 16, 20, nên \(n(A)=5\).'),
   T(r'\(P(A)=\dfrac{5}{20}=\dfrac{1}{4}\).', r'\(P(A)=\dfrac{5}{20}=\dfrac{1}{4}\).')],
  T(r'\(\dfrac{1}{4}\).', r'\(\dfrac{1}{4}\).'))
examples += EXAMPLE(3, ('Basic application', 'Vận dụng thấp'), ('Two dice', 'Hai con xúc xắc'),
  T(r'Roll two fair dice. Find the probability that the sum of the two numbers is 7.', r'Gieo hai con xúc xắc cân đối. Tính xác suất để tổng số chấm trên hai con xúc xắc bằng 7.'),
  ('Use the 6 × 6 table of Lesson 25 and highlight the favorable outcomes.', 'Dùng bảng 6 × 6 ở Bài 25 và tô màu các kết quả thuận lợi.'),
  [DICE_HL(S7, ('The 6 outcomes with sum 7 (highlighted)', '6 kết quả có tổng bằng 7 (được tô màu)')),
   T(r'\(n(\Omega)=36\), \(n(A)=6\): \(P(A)=\dfrac{6}{36}=\dfrac{1}{6}\).', r'\(n(\Omega)=36\), \(n(A)=6\): \(P(A)=\dfrac{6}{36}=\dfrac{1}{6}\).')],
  T(r'\(\dfrac{1}{6}\).', r'\(\dfrac{1}{6}\).'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Two spinners', 'Hai vòng quay'),
  T(r'Spinner A has the numbers 1, 2, 3 and spinner B has the numbers 1, 2, 3, 4 (equal sectors). Spin both and multiply the two numbers. Find the probability that the product is even.', r'Vòng quay A có các số 1, 2, 3; vòng quay B có các số 1, 2, 3, 4 (các hình quạt bằng nhau). Quay cả hai vòng rồi nhân hai số nhận được. Tính xác suất để tích là số chẵn.'),
  ('Make a table of the products: rows for A, columns for B.', 'Lập bảng các tích: hàng ứng với A, cột ứng với B.'),
  [SPIN_HL(), T(r'\(n(\Omega)=3\cdot4=12\); there are 8 even products: \(P=\dfrac{8}{12}=\dfrac{2}{3}\).', r'\(n(\Omega)=3\cdot4=12\); có 8 tích chẵn: \(P=\dfrac{8}{12}=\dfrac{2}{3}\).')],
  T(r'\(\dfrac{2}{3}\).', r'\(\dfrac{2}{3}\).'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Games at the school fair', 'Trò chơi ở hội chợ trường'),
  T(r'At the school fair there are three games. Game 1: roll a die, you win if you get a 6. Game 2: toss two coins, you win if both show heads. Game 3: roll two dice, you win if the sum is at least 10. (a) Which game gives the best chance of winning? (b) In that game, what is the probability of NOT winning?',
    r'Hội chợ của trường có ba trò chơi. Trò 1: gieo một con xúc xắc, thắng nếu được mặt 6 chấm. Trò 2: gieo hai đồng xu, thắng nếu cả hai đều ngửa. Trò 3: gieo hai con xúc xắc, thắng nếu tổng số chấm không nhỏ hơn 10. a) Trò chơi nào cho cơ hội thắng cao nhất? b) Ở trò chơi đó, xác suất KHÔNG thắng là bao nhiêu?'),
  ('Compute the three probabilities and compare them.', 'Tính ba xác suất rồi so sánh.'),
  [T(r'Game 1: \(\dfrac{1}{6}\). Game 2: \(\Omega=\{HH;\,HT;\,TH;\,TT\}\), \(P=\dfrac{1}{4}\). Game 3: sums 10, 11, 12 come from \((4;\,6),(5;\,5),(6;\,4),(5;\,6),(6;\,5),(6;\,6)\), \(P=\dfrac{6}{36}=\dfrac{1}{6}\).',
     r'Trò 1: \(\dfrac{1}{6}\). Trò 2: \(\Omega=\{NN;\,NS;\,SN;\,SS\}\), \(P=\dfrac{1}{4}\). Trò 3: tổng 10, 11, 12 ứng với \((4;\,6),(5;\,5),(6;\,4),(5;\,6),(6;\,5),(6;\,6)\), \(P=\dfrac{6}{36}=\dfrac{1}{6}\).'),
   T(r'(a) \(\dfrac{1}{4}\gt\dfrac{1}{6}\): game 2 is best. (b) \(1-\dfrac{1}{4}=\dfrac{3}{4}\).', r'a) \(\dfrac{1}{4}\gt\dfrac{1}{6}\): trò 2 có cơ hội thắng cao nhất. b) \(1-\dfrac{1}{4}=\dfrac{3}{4}\).')],
  T(r'(a) Game 2; (b) \(\dfrac{3}{4}\).', r'a) Trò 2; b) \(\dfrac{3}{4}\).'))

_SETS = sp_g9.BANK(sp_g9p.L26_GROUPS, start=1, seeds=(2601, 2602, 2603))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Using the formula when outcomes are not equally likely.</b> For the sum of two dice, the sums 2, 3, …, 12 are NOT equally likely; use the 36 ordered pairs.', r'<b>Dùng công thức khi các kết quả không đồng khả năng.</b> Với tổng số chấm của hai xúc xắc, các tổng 2, 3, …, 12 KHÔNG đồng khả năng; phải dùng 36 cặp có thứ tự.'),
 (r'<b>Turning the fraction upside down.</b> \(P(A)=\dfrac{n(A)}{n(\Omega)}\le1\).', r'<b>Viết ngược phân số.</b> \(P(A)=\dfrac{n(A)}{n(\Omega)}\le1\).'),
 (r'<b>Forgetting some favorable outcomes.</b> \((2;\,5)\) and \((5;\,2)\) are both favorable to “sum 7”.', r'<b>Bỏ sót kết quả thuận lợi.</b> Cả \((2;\,5)\) và \((5;\,2)\) đều thuận lợi cho “tổng bằng 7”.'),
 (r'<b>Comparing counts instead of probabilities.</b> More red balls does not always mean a better chance: compare \(\dfrac{n(A)}{n(\Omega)}\).', r'<b>So sánh số lượng thay vì xác suất.</b> Nhiều quả đỏ hơn chưa chắc có cơ hội cao hơn: phải so sánh \(\dfrac{n(A)}{n(\Omega)}\).')]
summary = [
 (r'Favorable outcomes of \(A\): the outcomes that make \(A\) happen.', r'Kết quả thuận lợi cho \(A\): các kết quả làm cho \(A\) xảy ra.'),
 (r'If the outcomes are equally likely: \(P(A)=\dfrac{n(A)}{n(\Omega)}\), \(0\le P(A)\le1\).', r'Nếu các kết quả đồng khả năng: \(P(A)=\dfrac{n(A)}{n(\Omega)}\), \(0\le P(A)\le1\).'),
 (r'Two-step experiments: count with a table or a tree diagram. Extension: \(P(\overline{A})=1-P(A)\).', r'Phép thử hai bước: đếm bằng bảng hoặc sơ đồ hình cây. Mở rộng: \(P(\overline{A})=1-P(A)\).'),
 (r'Key English: event, favorable outcome, equally likely, probability, fair die.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[biến cố|biến cố (phép thử)]], [[kết quả thuận lợi|kết quả thuận lợi (cho biến cố)]], [[đồng khả năng]], [[xác suất|xác suất (của biến cố)]], [[cân đối và đồng chất|cân đối và đồng chất (đồng xu, xúc xắc)]].')]
checks = [
 (r'I can list the favorable outcomes of an event.', r'Em liệt kê được các kết quả thuận lợi cho một biến cố.'),
 (r'I can compute \(P(A)=\dfrac{n(A)}{n(\Omega)}\) for one-step experiments.', r'Em tính được \(P(A)=\dfrac{n(A)}{n(\Omega)}\) với phép thử một bước.'),
 (r'I can compute probabilities for two dice, two coins, two spinners.', r'Em tính được xác suất khi gieo hai xúc xắc, hai đồng xu, quay hai vòng quay.'),
 (r'I can use probabilities to choose the better option.', r'Em dùng được xác suất để chọn phương án có lợi hơn.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Probability of Events Related to a Random Experiment', title_vi='Xác suất của biến cố liên quan tới phép thử', topic=TOPIC,
       folder='probability', file='probability-of-events', catalog_title_vi='Xác suất của biến cố liên quan tới phép thử',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Events, favorable outcomes, equally likely outcomes, P(A) = n(A)/n(Ω), two-step experiments, complementary events (extension).', level='Basic', minutes=90,
       description_vi='Bài 26 – Biến cố, kết quả thuận lợi, xác suất P(A) = n(A)/n(Ω); phép thử hai bước; mở rộng: biến cố đối.',
       tags_vi=['biến cố', 'xác suất', 'kết quả thuận lợi'], prerequisites=['g9-probability-01'], tags=['event', 'probability', 'favorable outcome'], order=260)
