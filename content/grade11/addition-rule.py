# -*- coding: utf-8 -*-
"""g11-prob-02 = Toán 11 KNTT, Bài 29: Công thức cộng xác suất. Mã ngân hàng câu hỏi: TOAN11-C8-B29."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g11j as S
import mb_pgf

CV = 'Công thức cộng xác suất'
dd = S.dec
vocab = defs(CV, [
 ('addrule', 'addition rule', 'công thức cộng xác suất', 'the formula \\(P(A\\cup B)=P(A)+P(B)-P(AB)\\).', 'công thức \\(P(A\\cup B)=P(A)+P(B)-P(AB)\\).', 'Use the addition rule for "A or B".', '\\(P(A\\cup B)\\)'),
 ('venn', 'Venn diagram', 'biểu đồ Venn', 'a picture of sets as overlapping regions inside a rectangle.', 'hình vẽ biểu diễn các tập hợp bằng các miền chồng lên nhau trong một hình chữ nhật.', 'The Venn diagram shows 7 students in both clubs.', ''),
 ('atleast', 'at least one', 'ít nhất một', 'one or more of the events occur; usually computed via the complement.', 'có một hoặc nhiều biến cố xảy ra; thường tính qua biến cố đối.', 'P(at least one six) = 1 − P(no six).', '')])
goals = [('state and use the addition rule \\(P(A\\cup B)=P(A)+P(B)-P(AB)\\);', 'phát biểu và sử dụng [[công thức cộng xác suất]] \\(P(A\\cup B)=P(A)+P(B)-P(AB)\\);'),
         ('use the special case \\(P(A\\cup B)=P(A)+P(B)\\) for mutually exclusive events;', 'dùng trường hợp riêng \\(P(A\\cup B)=P(A)+P(B)\\) cho hai biến cố xung khắc;'),
         ('read survey data from a Venn diagram;', 'đọc số liệu khảo sát từ [[biểu đồ Venn]];'),
         ('combine the addition rule with complements and independence.', 'kết hợp công thức cộng với biến cố đối và tính độc lập (bài toán "[[ít nhất một]]").')]
phrases = [('<b>Do not count the overlap twice.</b>', 'Đừng đếm phần chung hai lần.'), ('<b>The two events are mutually exclusive, so we simply add.</b>', 'Hai biến cố xung khắc nên ta chỉ việc cộng.'),
           ('<b>Subtract the probability of the intersection.</b>', 'Trừ đi xác suất của biến cố giao.'), ('<b>Use the complement: one minus the probability of none.</b>', 'Dùng biến cố đối: một trừ xác suất không có biến cố nào.'), ('<b>Read the numbers from the Venn diagram.</b>', 'Đọc số liệu từ biểu đồ Venn.')]
review = T('From Bài 28: \\(A\\cup B\\), \\(AB\\), mutually exclusive (\\(AB=\\varnothing\\)), independent (\\(P(AB)=P(A)P(B)\\)). Counting: \\(n(A\\cup B)=n(A)+n(B)-n(AB)\\).',
           'Từ Bài 28: \\(A\\cup B\\), \\(AB\\), xung khắc (\\(AB=\\varnothing\\)), độc lập (\\(P(AB)=P(A)P(B)\\)). Đếm: \\(n(A\\cup B)=n(A)+n(B)-n(AB)\\).')

venn = mb_pgf.raw_svg(r'''\begin{tikzpicture}[font=\small, every node/.style={text=ink}]
\draw[ink!70] (-3.6,-1.7) rectangle (3.6,1.7); \node[anchor=north west] at (-3.6,1.7) {$\Omega$: 40};
\begin{scope} \clip (-0.7,0) circle (1.3); \fill[orange!45] (0.7,0) circle (1.3); \end{scope}
\draw[ink, fill=blue!12, fill opacity=0.5] (-0.7,0) circle (1.3); \draw[ink, fill=green!15, fill opacity=0.5] (0.7,0) circle (1.3);
\node at (-1.35,0) {\textbf{11}}; \node at (0,0) {\textbf{7}}; \node at (1.35,0) {\textbf{8}}; \node at (2.9,-1.3) {\textbf{14}};
\node at (-2.45,0.9) {$A$: 18}; \node at (2.45,0.9) {$B$: 15};
\end{tikzpicture}''')

theory = '<h3>29.1 %s</h3>' % TI('The addition rule', 'Công thức cộng xác suất')
theory += BOX('blue', ('Addition rule', 'Công thức cộng'), UL([
  T('For any two events: \\[P(A\\cup B)=P(A)+P(B)-P(AB).\\]', 'Với hai biến cố bất kì: \\[P(A\\cup B)=P(A)+P(B)-P(AB).\\]'),
  T('If \\(A\\), \\(B\\) are mutually exclusive (\\(AB=\\varnothing\\)): \\(P(A\\cup B)=P(A)+P(B)\\).', 'Nếu \\(A\\), \\(B\\) xung khắc (\\(AB=\\varnothing\\)): \\(P(A\\cup B)=P(A)+P(B)\\).'),
  T('Reason: \\(n(A\\cup B)=n(A)+n(B)-n(AB)\\); divide by \\(n(\\Omega)\\). The outcomes in \\(AB\\) are counted twice in \\(n(A)+n(B)\\).', 'Lí do: \\(n(A\\cup B)=n(A)+n(B)-n(AB)\\); chia hai vế cho \\(n(\\Omega)\\). Các kết quả thuộc \\(AB\\) bị đếm hai lần trong \\(n(A)+n(B)\\).')]))
theory += mb_pgf.img(venn, 'Venn diagram of 40 students: 18 play football, 15 badminton, 7 both, 14 neither', 420,
  TI('Class of 40: \\(A\\) = football (18), \\(B\\) = badminton (15), both: 7, neither: 14.', 'Lớp 40 học sinh: \\(A\\) – bóng đá (18 em), \\(B\\) – cầu lông (15 em), cả hai: 7 em, không chơi môn nào: 14 em.'))
theory += BOX('mint', ('Reading the diagram', 'Đọc biểu đồ'), T('\\(P(A\\cup B)=\\frac{18}{40}+\\frac{15}{40}-\\frac{7}{40}=\\frac{26}{40}=0{,}65\\). Check: \\(11+7+8=26\\) students play at least one sport; \\(40-26=14\\) play none.',
  '\\(P(A\\cup B)=\\frac{18}{40}+\\frac{15}{40}-\\frac{7}{40}=\\frac{26}{40}=0{,}65\\). Kiểm tra: \\(11+7+8=26\\) em chơi ít nhất một môn; \\(40-26=14\\) em không chơi môn nào.'))
theory += '<h3>29.2 %s</h3>' % TI('Using complements and independence', 'Kết hợp biến cố đối và tính độc lập')
theory += BOX('blue', ('Useful forms', 'Các dạng thường dùng'), UL([
  T('\\(P(\\text{neither})=1-P(A\\cup B)\\).', '\\(P(\\text{không biến cố nào})=1-P(A\\cup B)\\).'),
  T('If \\(A\\), \\(B\\) are independent: \\(P(A\\cup B)=P(A)+P(B)-P(A)P(B)=1-P(\\overline A)P(\\overline B)\\).', 'Nếu \\(A\\), \\(B\\) độc lập: \\(P(A\\cup B)=P(A)+P(B)-P(A)P(B)=1-P(\\overline A)P(\\overline B)\\).'),
  T('Exactly one of \\(A\\), \\(B\\): \\(P(A\\cup B)-P(AB)=P(A)+P(B)-2P(AB)\\).', 'Đúng một trong hai: \\(P(A\\cup B)-P(AB)=P(A)+P(B)-2P(AB)\\).')]))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('Adding probabilities without subtracting the overlap can give results greater than 1 — a sure sign of an error.', 'Cộng xác suất mà quên trừ phần chung có thể cho kết quả lớn hơn 1 — dấu hiệu chắc chắn có lỗi.'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Direct use', 'Áp dụng trực tiếp'), T('\\(P(A)=0{,}5\\), \\(P(B)=0{,}4\\), \\(P(AB)=0{,}2\\). Find \\(P(A\\cup B)\\) and \\(P(\\overline A\\,\\overline B)\\).', 'Cho \\(P(A)=0{,}5\\), \\(P(B)=0{,}4\\), \\(P(AB)=0{,}2\\). Tính \\(P(A\\cup B)\\) và \\(P(\\overline A\\,\\overline B)\\).'),
  T('\\(\\overline A\\,\\overline B\\) is the complement of \\(A\\cup B\\).', '\\(\\overline A\\,\\overline B\\) là biến cố đối của \\(A\\cup B\\).'), [T('\\(P(A\\cup B)=0{,}5+0{,}4-0{,}2=0{,}7\\).', '\\(P(A\\cup B)=0{,}5+0{,}4-0{,}2=0{,}7\\).'), T('\\(P(\\overline A\\,\\overline B)=1-0{,}7=0{,}3\\).', '\\(P(\\overline A\\,\\overline B)=1-0{,}7=0{,}3\\).')],
  T('\\(0{,}7\\) and \\(0{,}3\\).', '\\(0{,}7\\) và \\(0{,}3\\).'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Mutually exclusive events', 'Hai biến cố xung khắc'), T('Two dice are rolled. Find the probability that the sum is 7 or 11.', 'Gieo hai con xúc xắc. Tính xác suất tổng số chấm bằng 7 hoặc bằng 11.'),
  T('The two events cannot happen together.', 'Hai biến cố không thể cùng xảy ra.'), [T('Sum 7: 6 outcomes; sum 11: \\((5;6),(6;5)\\), 2 outcomes.', 'Tổng 7: 6 kết quả; tổng 11: \\((5;6),(6;5)\\), 2 kết quả.'), T('\\(P=\\frac6{36}+\\frac2{36}=\\frac8{36}\\).', '\\(P=\\frac6{36}+\\frac2{36}=\\frac8{36}\\).')], T('\\(\\dfrac29\\).', '\\(\\dfrac29\\).'))
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Survey', 'Khảo sát'), T('Of 50 households, 30 have a motorbike, 18 have a car and 10 have both. Pick a household at random. Find P(it has a motorbike or a car) and P(it has neither).', 'Khảo sát 50 hộ gia đình: 30 hộ có xe máy, 18 hộ có ô tô, 10 hộ có cả hai. Chọn ngẫu nhiên một hộ. Tính xác suất hộ đó có xe máy hoặc ô tô, và xác suất hộ đó không có loại xe nào.'),
  T('Addition rule, then complement.', 'Công thức cộng, rồi biến cố đối.'), [T('\\(P=\\frac{30+18-10}{50}=\\frac{38}{50}=0{,}76\\).', '\\(P=\\frac{30+18-10}{50}=\\frac{38}{50}=0{,}76\\).'), T('Neither: \\(1-0{,}76=0{,}24\\) (12 households).', 'Không có xe: \\(1-0{,}76=0{,}24\\) (12 hộ).')], T('\\(0{,}76\\) and \\(0{,}24\\).', '\\(0{,}76\\) và \\(0{,}24\\).'))
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Divisibility', 'Tính chia hết'), T('A ticket is drawn from tickets numbered 1 to 100. Find the probability that its number is divisible by 4 or by 6.', 'Rút ngẫu nhiên một vé trong 100 vé đánh số 1 đến 100. Tính xác suất số trên vé chia hết cho 4 hoặc cho 6.'),
  T('Divisible by both 4 and 6 \\(\\iff\\) divisible by 12.', 'Chia hết cho cả 4 và 6 \\(\\iff\\) chia hết cho 12.'), [T('\\(n(A)=25\\), \\(n(B)=16\\), \\(n(AB)=8\\).', '\\(n(A)=25\\), \\(n(B)=16\\), \\(n(AB)=8\\).'), T('\\(P=\\frac{25+16-8}{100}=\\frac{33}{100}\\).', '\\(P=\\frac{25+16-8}{100}=\\frac{33}{100}\\).')], T('\\(0{,}33\\).', '\\(0{,}33\\).'))
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Weather forecast', 'Dự báo thời tiết'), T('Tomorrow it rains in Hà Nội with probability 0,6 and in Đà Nẵng with probability 0,3, independently. Find P(it rains in at least one city) and P(it rains in exactly one city).', 'Ngày mai trời mưa ở Hà Nội với xác suất 0,6 và ở Đà Nẵng với xác suất 0,3, độc lập với nhau. Tính xác suất có mưa ở ít nhất một thành phố, và ở đúng một thành phố.'),
  T('\\(P(AB)=0{,}6\\cdot0{,}3=0{,}18\\).', '\\(P(AB)=0{,}6\\cdot0{,}3=0{,}18\\).'), [T('At least one: \\(0{,}6+0{,}3-0{,}18=0{,}72\\) (or \\(1-0{,}4\\cdot0{,}7\\)).', 'Ít nhất một: \\(0{,}6+0{,}3-0{,}18=0{,}72\\) (hoặc \\(1-0{,}4\\cdot0{,}7\\)).'), T('Exactly one: \\(0{,}72-0{,}18=0{,}54\\).', 'Đúng một: \\(0{,}72-0{,}18=0{,}54\\).')],
  T('\\(0{,}72\\) and \\(0{,}54\\).', '\\(0{,}72\\) và \\(0{,}54\\).'))
examples = EXFIG(examples, 3, mb_pgf.img(venn, 'Venn diagram with counts', 380))


def lvl(P):
    p, q, r = P['pqr']
    o1 = M4(1, '\\(P(A)=%s\\), \\(P(B)=%s\\), \\(P(AB)=%s\\). \\(P(\\overline A\\,\\overline B)=\\)…' % (dd(p), dd(q), dd(r)), 'Cho \\(P(A)=%s\\), \\(P(B)=%s\\), \\(P(AB)=%s\\). Khi đó \\(P(\\overline A\\,\\overline B)=\\)…' % (dd(p), dd(q), dd(r)), '\\(%s\\)' % dd(1 - p - q + r),
            ['\\(%s\\)' % dd(p + q - r), '\\(%s\\)' % dd((1 - p) * (1 - q)), '\\(%s\\)' % dd(1 - r), '\\(%s\\)' % dd(abs(1 - p - q))], '\\(1-P(A\\cup B)\\).', '\\(\\overline A\\,\\overline B\\) là biến cố đối của \\(A\\cup B\\): \\(1-(%s+%s-%s)\\).' % (dd(p), dd(q), dd(r)))
    n, a, b, c = P['srv']
    o2 = M4(2, 'Of %d students, %d like maths, %d like English, %d like both. P(a random student likes exactly one of them) =…' % (n, a, b, c), 'Trong %d học sinh có %d em thích Toán, %d em thích Tiếng Anh, %d em thích cả hai. Chọn ngẫu nhiên một em. Xác suất em đó thích đúng một trong hai môn là…' % (n, a, b, c),
            '\\(%s\\)' % fr(F(a + b - 2 * c, n)), ['\\(%s\\)' % fr(F(a + b - c, n)), '\\(%s\\)' % fr(F(c, n)), '\\(%s\\)' % fr(F(n - a - b + c, n)), '\\(%s\\)' % fr(F(a - c, n))], 'Union minus intersection.', '\\(\\dfrac{%d+%d-2\\cdot%d}{%d}\\).' % (a, b, c, n))
    u, v = P['ind']
    o3 = M4(3, 'Independent events: \\(P(A)=%s\\), \\(P(B)=%s\\). \\(P(A\\cup B)=\\)…' % (dd(u), dd(v)), 'Hai biến cố độc lập với \\(P(A)=%s\\), \\(P(B)=%s\\). Khi đó \\(P(A\\cup B)=\\)…' % (dd(u), dd(v)), '\\(%s\\)' % dd(u + v - u * v),
            ['\\(%s\\)' % dd(u * v), '\\(%s\\)' % dd(min(u + v, 1)) if u + v != u + v - u * v else '\\(1\\)', '\\(%s\\)' % dd((1 - u) * (1 - v))], '\\(P(A)+P(B)-P(A)P(B)\\).', '\\(%s+%s-%s\\cdot%s\\).' % (dd(u), dd(v), dd(u), dd(v)))
    (se, sv), v4 = P['t4']
    t4 = tf(4, se, sv, v4, 'Check with the addition rule.', 'Kiểm tra bằng công thức cộng.')
    (te, tv), v5 = P['t5']
    t5 = tf(5, te, tv, v5, 'Probabilities never exceed 1.', 'Xác suất không vượt quá 1; xem lại điều kiện xung khắc.')
    N, m1, m2 = P['div']; l = m1 * m2 // math.gcd(m1, m2)
    s6 = sh(6, 'Tickets 1–%d. How many tickets are divisible by neither %d nor %d?' % (N, m1, m2), 'Có %d vé đánh số từ 1 đến %d. Có bao nhiêu vé có số không chia hết cho %d và không chia hết cho %d?' % (N, N, m1, m2),
            N - (N // m1 + N // m2 - N // l), '\\(N-n(A\\cup B)\\).', '\\(%d-(%d+%d-%d)\\).' % (N, N // m1, N // m2, N // l))
    w1, w2 = P['pct']
    s7 = sh(7, 'Two alarms ring independently with probabilities %s and %s. P(at least one rings), in percent, is…' % (dd(w1), dd(w2)), 'Hai chuông báo động hoạt động độc lập, xác suất reo khi có sự cố lần lượt là %s và %s. Xác suất có ít nhất một chuông reo bằng bao nhiêu phần trăm?' % (dd(w1), dd(w2)),
            int((1 - (1 - w1) * (1 - w2)) * 100), '\\(1-P(\\overline A)P(\\overline B)\\).', '\\(1-(1-%s)(1-%s)\\).' % (dd(w1), dd(w2)))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]


PP = [dict(pqr=(F(6, 10), F(5, 10), F(3, 10)), srv=(40, 22, 18, 8), ind=(F(5, 10), F(4, 10)),
           t4=(('If \\(P(A)=0{,}4\\), \\(P(B)=0{,}3\\) and \\(A\\), \\(B\\) are mutually exclusive, then \\(P(A\\cup B)=0{,}7\\).', 'Nếu \\(P(A)=0{,}4\\), \\(P(B)=0{,}3\\) và \\(A\\), \\(B\\) xung khắc thì \\(P(A\\cup B)=0{,}7\\).'), True),
           t5=(('Two events with \\(P(A)=0{,}7\\) and \\(P(B)=0{,}6\\) can be mutually exclusive.', 'Có hai biến cố xung khắc với \\(P(A)=0{,}7\\) và \\(P(B)=0{,}6\\).'), False), div=(60, 2, 3), pct=(F(9, 10), F(8, 10))),
      dict(pqr=(F(7, 10), F(4, 10), F(2, 10)), srv=(45, 20, 25, 12), ind=(F(6, 10), F(7, 10)),
           t4=(('For any events, \\(P(A\\cup B)\\le P(A)+P(B)\\).', 'Với hai biến cố bất kì, \\(P(A\\cup B)\\le P(A)+P(B)\\).'), True),
           t5=(('For any events, \\(P(A\\cup B)=P(A)+P(B)\\).', 'Với hai biến cố bất kì, \\(P(A\\cup B)=P(A)+P(B)\\).'), False), div=(100, 4, 10), pct=(F(7, 10), F(6, 10))),
      dict(pqr=(F(5, 10), F(6, 10), F(4, 10)), srv=(50, 28, 21, 9), ind=(F(8, 10), F(3, 10)),
           t4=(('If \\(P(A\\cup B)=P(A)+P(B)\\) and \\(P(A),P(B)>0\\), then \\(A\\), \\(B\\) cannot be independent.', 'Nếu \\(P(A\\cup B)=P(A)+P(B)\\) và \\(P(A),P(B)>0\\) thì \\(A\\), \\(B\\) không thể độc lập.'), True),
           t5=(('\\(P(\\text{exactly one})=P(A)+P(B)-P(AB)\\).', '\\(P(\\text{đúng một trong hai})=P(A)+P(B)-P(AB)\\).'), False), div=(90, 6, 9), pct=(F(5, 10), F(4, 10)))]
practice = three(lvl, PP)
practice = with_self(practice, S.M29S11, start=8)
mistakes = [('<b>Forgetting to subtract \\(P(AB)\\).</b> Only mutually exclusive events allow simple addition.', '<b>Quên trừ \\(P(AB)\\).</b> Chỉ khi xung khắc mới được cộng trực tiếp.'),
            ('<b>Using \\(P(AB)=P(A)P(B)\\) without independence.</b> Survey data must be read, not multiplied.', '<b>Dùng \\(P(AB)=P(A)P(B)\\) khi chưa biết độc lập.</b> Với số liệu khảo sát phải đọc \\(P(AB)\\) từ dữ liệu, không được nhân.'),
            ('<b>Confusing "at least one" with "exactly one".</b>', '<b>Nhầm "ít nhất một" với "đúng một".</b>'),
            ('<b>Accepting a probability greater than 1.</b> Check every answer.', '<b>Chấp nhận xác suất lớn hơn 1.</b> Luôn kiểm tra kết quả.')]
summary = [('\\(P(A\\cup B)=P(A)+P(B)-P(AB)\\).', '\\(P(A\\cup B)=P(A)+P(B)-P(AB)\\).'), ('Mutually exclusive: \\(P(A\\cup B)=P(A)+P(B)\\).', 'Xung khắc: \\(P(A\\cup B)=P(A)+P(B)\\).'),
           ('Independent: \\(P(A\\cup B)=1-P(\\overline A)P(\\overline B)\\); neither: \\(1-P(A\\cup B)\\).', 'Độc lập: \\(P(A\\cup B)=1-P(\\overline A)P(\\overline B)\\); không biến cố nào: \\(1-P(A\\cup B)\\).'), ('Key words: addition rule, Venn diagram, at least one, exactly one.', 'Từ cần nhớ: addition rule, Venn diagram, at least one, exactly one.')]
checks = [('I can apply the addition rule.', 'Em áp dụng được công thức cộng xác suất.'), ('I can read a Venn diagram.', 'Em đọc được biểu đồ Venn.'), ('I can compute "at least one" and "exactly one".', 'Em tính được xác suất "ít nhất một", "đúng một".'), ('I can spot an impossible answer.', 'Em phát hiện được kết quả vô lí.')]
LL('g11-prob-02', 'The Addition Rule of Probability', CV, ('Probability Rules', 'Các quy tắc tính xác suất'), 'probability-rules', 'addition-rule', 300, 'Intermediate', 60, ('union and intersection of events', 'biến cố hợp, biến cố giao'),
   'The addition rule for any two events and for mutually exclusive events, Venn diagrams, surveys, at least one and exactly one.', 'Bài 29 – Công thức cộng xác suất cho hai biến cố bất kì và hai biến cố xung khắc; biểu đồ Venn, số liệu khảo sát; bài toán "ít nhất một", "đúng một".',
   ['addition rule', 'Venn diagram', 'mutually exclusive'], ['công thức cộng', 'biểu đồ Venn', 'xung khắc'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g11-prob-01'])
