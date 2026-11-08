# -*- coding: utf-8 -*-
"""g12-prob-01 = Toán 12 KNTT, Bài 18: Xác suất có điều kiện. Mã ngân hàng câu hỏi: TOAN12-C6-B18.
Mỗi mức 22 câu: 7 câu soạn sẵn + 15 câu tự luyện."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g12f as S
from sp_g12f import P as PV

CV = 'Xác suất có điều kiện'
vocab = defs(CV, [
 ('condp', 'conditional probability', 'xác suất có điều kiện', 'the probability of \\(A\\) given that \\(B\\) has happened: \\(P(A\\mid B)=\\dfrac{P(A\\cap B)}{P(B)}\\) (\\(P(B)\\gt0\\)).', 'xác suất của \\(A\\) khi biết \\(B\\) đã xảy ra: \\(P(A\\mid B)=\\dfrac{P(A\\cap B)}{P(B)}\\) (\\(P(B)\\gt0\\)).', 'Find the conditional probability of A given B.', '\\(P(A\\mid B)\\)'),
 ('multrule', 'multiplication rule', 'công thức nhân xác suất', '\\(P(A\\cap B)=P(B)\\cdot P(A\\mid B)=P(A)\\cdot P(B\\mid A)\\).', '\\(P(A\\cap B)=P(B)\\cdot P(A\\mid B)=P(A)\\cdot P(B\\mid A)\\).', 'Use the multiplication rule for two draws.', ''),
 ('indepev', 'independent events', 'hai biến cố độc lập', '\\(A\\), \\(B\\) with \\(P(A\\cap B)=P(A)P(B)\\); equivalently \\(P(A\\mid B)=P(A)\\).', '\\(A\\), \\(B\\) thỏa \\(P(A\\cap B)=P(A)P(B)\\); tương đương \\(P(A\\mid B)=P(A)\\).', 'The two events are independent.', ''),
 ('without', 'without replacement', 'không hoàn lại', 'a drawn object is not put back, so the second draw depends on the first.', 'vật đã lấy không được trả lại, nên lần lấy sau phụ thuộc lần lấy trước.', 'Two balls are drawn without replacement.', '')])
goals = [('understand what "the probability of \\(A\\) given \\(B\\)" means;', 'hiểu ý nghĩa của [[xác suất có điều kiện]] "\\(A\\) khi biết \\(B\\)";'),
         ('compute \\(P(A\\mid B)\\) by the formula or by counting in the reduced sample space;', 'tính \\(P(A\\mid B)\\) bằng công thức hoặc bằng cách đếm trên không gian mẫu thu hẹp;'),
         ('use the multiplication rule for successive draws and recognise independent events;', 'dùng [[công thức nhân xác suất]] cho các lần lấy liên tiếp và nhận biết [[hai biến cố độc lập]];'),
         ('interpret conditional probabilities in surveys and medical tests.', 'giải thích xác suất có điều kiện trong khảo sát và xét nghiệm y tế.')]
phrases = [('<b>The probability of \\(A\\) given \\(B\\).</b>', 'Xác suất của \\(A\\) với điều kiện \\(B\\).'), ('<b>We know that \\(B\\) has happened.</b>', 'Ta biết \\(B\\) đã xảy ra.'), ('<b>The sample space shrinks to \\(B\\).</b>', 'Không gian mẫu thu hẹp thành \\(B\\).'),
           ('<b>The balls are drawn without replacement.</b>', 'Các viên bi được lấy không hoàn lại.'), ('<b>The two events are independent.</b>', 'Hai biến cố độc lập.')]
review = T('Grade 10–11: classical probability \\(P(A)=\\dfrac{n(A)}{n(\\Omega)}\\); \\(P(\\overline A)=1-P(A)\\); \\(P(A\\cup B)=P(A)+P(B)-P(A\\cap B)\\); for independent \\(A,B\\): \\(P(A\\cap B)=P(A)P(B)\\).',
           'Lớp 10–11: định nghĩa cổ điển \\(P(A)=\\dfrac{n(A)}{n(\\Omega)}\\); \\(P(\\overline A)=1-P(A)\\); \\(P(A\\cup B)=P(A)+P(B)-P(A\\cap B)\\); với \\(A,B\\) độc lập: \\(P(A\\cap B)=P(A)P(B)\\).')
theory = '<h3>18.1 %s</h3>' % TI('Conditional probability', 'Xác suất có điều kiện')
theory += BOX('blue', ('Definition', 'Định nghĩa'), T('For events \\(A\\), \\(B\\) with \\(P(B)\\gt0\\), the probability of \\(A\\) given \\(B\\) is \\[P(A\\mid B)=\\dfrac{P(A\\cap B)}{P(B)}.\\] With equally likely outcomes: \\(P(A\\mid B)=\\dfrac{n(A\\cap B)}{n(B)}\\) – we count only inside \\(B\\) (the reduced sample space).',
  'Cho hai biến cố \\(A\\), \\(B\\) với \\(P(B)\\gt0\\). Xác suất của \\(A\\) với điều kiện \\(B\\) là \\[P(A\\mid B)=\\dfrac{P(A\\cap B)}{P(B)}.\\] Khi các kết quả đồng khả năng: \\(P(A\\mid B)=\\dfrac{n(A\\cap B)}{n(B)}\\) – chỉ đếm trong \\(B\\) (không gian mẫu thu hẹp).'))
theory += TBL(['', TI('Likes football', 'Thích bóng đá'), TI('Does not', 'Không thích'), TI('Total', 'Tổng')], [[TI('Boys', 'Nam'), '25', '15', '40'], [TI('Girls', 'Nữ'), '15', '45', '60'], [TI('Total', 'Tổng'), '40', '60', '100']])
theory += T('<i>In this survey, \\(P(\\text{likes})=\\frac{40}{100}=0{,}4\\), but \\(P(\\text{likes}\\mid\\text{girl})=\\frac{15}{60}=0{,}25\\) and \\(P(\\text{likes}\\mid\\text{boy})=\\frac{25}{40}=0{,}625\\): knowing the group changes the probability.</i>', '<i>Trong khảo sát này \\(P(\\text{thích})=\\frac{40}{100}=0{,}4\\), nhưng \\(P(\\text{thích}\\mid\\text{nữ})=\\frac{15}{60}=0{,}25\\) và \\(P(\\text{thích}\\mid\\text{nam})=\\frac{25}{40}=0{,}625\\): biết thêm nhóm thì xác suất thay đổi.</i>')
theory += BOX('mint', ('Properties', 'Tính chất'), UL([T('\\(0\\le P(A\\mid B)\\le1\\); \\(P(\\overline A\\mid B)=1-P(A\\mid B)\\).', '\\(0\\le P(A\\mid B)\\le1\\); \\(P(\\overline A\\mid B)=1-P(A\\mid B)\\).'),
  T('In general \\(P(A\\mid B)\\ne P(B\\mid A)\\) and \\(P(A\\mid B)\\ne P(A\\cap B)\\).', 'Nói chung \\(P(A\\mid B)\\ne P(B\\mid A)\\) và \\(P(A\\mid B)\\ne P(A\\cap B)\\).')]))
theory += '<h3>18.2 %s</h3>' % TI('Multiplication rule and independence', 'Công thức nhân xác suất và tính độc lập')
theory += BOX('blue', ('Multiplication rule', 'Công thức nhân'), T('\\(P(A\\cap B)=P(B)\\cdot P(A\\mid B)=P(A)\\cdot P(B\\mid A)\\). For three events: \\(P(A\\cap B\\cap C)=P(A)P(B\\mid A)P(C\\mid A\\cap B)\\) (successive draws without replacement).', '\\(P(A\\cap B)=P(B)\\cdot P(A\\mid B)=P(A)\\cdot P(B\\mid A)\\). Với ba biến cố: \\(P(A\\cap B\\cap C)=P(A)P(B\\mid A)P(C\\mid A\\cap B)\\) (lấy liên tiếp không hoàn lại).'))
theory += BOX('mint', ('Independence', 'Tính độc lập'), T('\\(A\\), \\(B\\) (\\(P(B)\\gt0\\)) are independent \\(\\iff P(A\\mid B)=P(A)\\iff P(A\\cap B)=P(A)P(B)\\): knowing \\(B\\) does not change the chance of \\(A\\).', '\\(A\\), \\(B\\) (\\(P(B)\\gt0\\)) độc lập \\(\\iff P(A\\mid B)=P(A)\\iff P(A\\cap B)=P(A)P(B)\\): biết \\(B\\) không làm thay đổi khả năng của \\(A\\).'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('Do not confuse \\(P(A\\mid B)\\) with \\(P(B\\mid A)\\): "the probability that a person who tests positive is sick" is very different from "the probability that a sick person tests positive" (Example 5). With replacement the draws are independent; without replacement they are not.', 'Đừng nhầm \\(P(A\\mid B)\\) với \\(P(B\\mid A)\\): "xác suất người xét nghiệm dương tính bị bệnh" khác xa "xác suất người bệnh xét nghiệm dương tính" (Ví dụ 5). Lấy có hoàn lại thì các lần lấy độc lập; không hoàn lại thì không.'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Reading a table', 'Đọc bảng số liệu'), T('Use the survey table above. A student is chosen at random. a) Given that it is a girl, find the probability that she likes football. b) Given that the student likes football, find the probability that it is a girl.', 'Dùng bảng khảo sát ở trên. Chọn ngẫu nhiên một học sinh. a) Biết đó là nữ, tính xác suất em thích bóng đá. b) Biết học sinh đó thích bóng đá, tính xác suất đó là nữ.'),
  T('Count inside the given group only.', 'Chỉ đếm trong nhóm đã biết.'), [T('a) 60 girls, 15 like football: \\(P=\\frac{15}{60}=\\frac14\\).', 'a) 60 nữ, 15 em thích: \\(P=\\frac{15}{60}=\\frac14\\).'), T('b) 40 like football, 15 are girls: \\(P=\\frac{15}{40}=\\frac38\\).', 'b) 40 em thích, 15 em là nữ: \\(P=\\frac{15}{40}=\\frac38\\).')],
  T('a) \\(\\frac14\\); b) \\(\\frac38\\) – the two conditional probabilities are different.', 'a) \\(\\frac14\\); b) \\(\\frac38\\) – hai xác suất có điều kiện khác nhau.'))
B2 = [(i, j) for i in range(1, 7) for j in range(1, 7) if i + j == 8]; assert len(B2) == 5 and [(3, 5)] == [p for p in B2 if p[0] == 3]
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Two dice', 'Gieo hai xúc xắc'), T('Two dice are rolled. Given that the sum is 8, find the probability that the first die shows 3.', 'Gieo hai con xúc xắc cân đối. Biết tổng số chấm bằng 8, tính xác suất con thứ nhất ra 3 chấm.'), T('List \\(B\\): sum 8.', 'Liệt kê \\(B\\): tổng bằng 8.'),
  [T('\\(B=\\{(2;6),(3;5),(4;4),(5;3),(6;2)\\}\\), \\(n(B)=5\\).', '\\(B=\\{(2;6),(3;5),(4;4),(5;3),(6;2)\\}\\), \\(n(B)=5\\).'), T('\\(A\\cap B=\\{(3;5)\\}\\): \\(P(A\\mid B)=\\frac15\\).', '\\(A\\cap B=\\{(3;5)\\}\\): \\(P(A\\mid B)=\\frac15\\).')], T('\\(\\frac15\\) (without the condition it would be \\(\\frac16\\)).', '\\(\\frac15\\) (không có điều kiện thì là \\(\\frac16\\)).'))
assert F(5, 8) * F(4, 7) == F(5, 14)
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Drawing without replacement', 'Lấy không hoàn lại'), T('A box has 5 red and 3 blue balls. Two balls are drawn one after the other without replacement. a) Given that the first is red, what is the probability that the second is red? b) Find the probability that both are red.', 'Hộp có 5 bi đỏ và 3 bi xanh. Lấy lần lượt 2 bi không hoàn lại. a) Biết bi thứ nhất màu đỏ, tính xác suất bi thứ hai màu đỏ. b) Tính xác suất cả hai bi đều đỏ.'),
  T('After the first red ball, 4 red remain among 7.', 'Sau khi lấy bi đỏ đầu tiên còn 4 đỏ trong 7 bi.'), [T('a) \\(P(B\\mid A)=\\frac47\\).', 'a) \\(P(B\\mid A)=\\frac47\\).'), T('b) \\(P(A\\cap B)=P(A)P(B\\mid A)=\\frac58\\cdot\\frac47=\\frac5{14}\\).', 'b) \\(P(A\\cap B)=P(A)P(B\\mid A)=\\frac58\\cdot\\frac47=\\frac5{14}\\).')],
  T('a) \\(\\frac47\\); b) \\(\\frac5{14}\\).', 'a) \\(\\frac47\\); b) \\(\\frac5{14}\\).'))
assert F(5, 10) + F(4, 10) - F(7, 10) == F(2, 10) and F(2, 10) / F(4, 10) == F(1, 2)
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Using the formula', 'Dùng công thức'), T('\\(P(A)=0{,}5\\), \\(P(B)=0{,}4\\), \\(P(A\\cup B)=0{,}7\\). Find \\(P(A\\mid B)\\) and \\(P(B\\mid A)\\). Are \\(A\\) and \\(B\\) independent?', 'Cho \\(P(A)=0{,}5\\), \\(P(B)=0{,}4\\), \\(P(A\\cup B)=0{,}7\\). Tính \\(P(A\\mid B)\\), \\(P(B\\mid A)\\). Hai biến cố \\(A\\), \\(B\\) có độc lập không?'),
  T('Find \\(P(A\\cap B)\\) first.', 'Tính \\(P(A\\cap B)\\) trước.'), [T('\\(P(A\\cap B)=0{,}5+0{,}4-0{,}7=0{,}2\\).', '\\(P(A\\cap B)=0{,}5+0{,}4-0{,}7=0{,}2\\).'), T('\\(P(A\\mid B)=\\frac{0{,}2}{0{,}4}=0{,}5=P(A)\\); \\(P(B\\mid A)=\\frac{0{,}2}{0{,}5}=0{,}4=P(B)\\).', '\\(P(A\\mid B)=\\frac{0{,}2}{0{,}4}=0{,}5=P(A)\\); \\(P(B\\mid A)=\\frac{0{,}2}{0{,}5}=0{,}4=P(B)\\).')],
  T('\\(0{,}5\\); \\(0{,}4\\); yes, they are independent.', '\\(0{,}5\\); \\(0{,}4\\); có, hai biến cố độc lập.'))
assert F(45, 45 + 95) == F(9, 28) and F(45, 50) == F(9, 10)
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('A medical test', 'Xét nghiệm y tế'), T('Of 1000 people, 50 are sick. 45 of the sick and 95 of the healthy test positive. a) Given that a person is sick, what is the probability of a positive test? b) Given a positive test, what is the probability that the person is sick?', 'Trong 1000 người có 50 người bệnh. Có 45 người bệnh và 95 người khỏe xét nghiệm dương tính. a) Biết một người bị bệnh, xác suất người đó dương tính là bao nhiêu? b) Biết một người dương tính, xác suất người đó bị bệnh là bao nhiêu?'),
  T('Which group is given?', 'Nhóm nào đã biết?'), [T('a) \\(P(+\\mid\\text{sick})=\\frac{45}{50}=0{,}9\\).', 'a) \\(P(+\\mid\\text{bệnh})=\\frac{45}{50}=0{,}9\\).'), T('b) \\(45+95=140\\) positive: \\(P(\\text{sick}\\mid+)=\\frac{45}{140}=\\frac9{28}\\approx0{,}32\\).', 'b) Có \\(45+95=140\\) người dương tính: \\(P(\\text{bệnh}\\mid+)=\\frac{45}{140}=\\frac9{28}\\approx0{,}32\\).')],
  T('a) 0.9; b) about 0.32 – a positive test is far from a sure diagnosis. (Bài 19: Bayes\' formula.)', 'a) 0,9; b) khoảng 0,32 – dương tính chưa chắc đã mắc bệnh. (Bài 19: công thức Bayes.)'))

def lvl(P):
    pb, pab = P['f']; c1 = pab / pb
    o1 = M4(1, '\\(P(B)=%s\\), \\(P(A\\cap B)=%s\\). \\(P(A\\mid B)=\\)…' % (S.PE(pb), S.PE(pab)), 'Cho \\(P(B)=%s\\), \\(P(A\\cap B)=%s\\). Khi đó \\(P(A\\mid B)=\\)…' % (PV(pb), PV(pab)), '\\(%s\\)' % PV(c1), ['\\(%s\\)' % PV(pab * pb), '\\(%s\\)' % PV(pab), '\\(%s\\)' % PV(1 - c1), '\\(%s\\)' % PV(pb - pab)],
            '\\(\\dfrac{P(A\\cap B)}{P(B)}\\).', '\\(\\dfrac{P(A\\cap B)}{P(B)}=%s\\).' % PV(c1))
    a, b, c, d = P['tab']
    o2 = M4(2, 'Of %d boys, %d wear glasses; of %d girls, %d wear glasses. A student wearing glasses is chosen. \\(P(\\text{girl})=\\)…' % (a + b, a, c + d, c), 'Trong %d nam có %d em đeo kính; trong %d nữ có %d em đeo kính. Chọn một học sinh đeo kính. Xác suất đó là nữ là…' % (a + b, a, c + d, c),
            '\\(%s\\)' % PV(F(c, a + c)), ['\\(%s\\)' % PV(F(c, c + d)), '\\(%s\\)' % PV(F(c, a + b + c + d)), '\\(%s\\)' % PV(F(c + d, a + b + c + d))], 'Among %d with glasses, %d are girls.' % (a + c, c), 'Trong %d em đeo kính có %d em nữ.' % (a + c, c))
    rd, bl = P['draw']; n = rd + bl
    o3 = M4(3, '%d red and %d white balls; draw 2 without replacement. \\(P(\\text{both white})=\\)…' % (rd, bl), 'Hộp có %d bi đỏ và %d bi trắng; lấy lần lượt 2 bi không hoàn lại. Xác suất cả hai bi trắng là…' % (rd, bl), '\\(%s\\)' % PV(F(bl, n) * F(bl - 1, n - 1)),
            ['\\(%s\\)' % PV(F(bl, n) ** 2), '\\(%s\\)' % PV(F(bl - 1, n - 1)), '\\(%s\\)' % PV(F(bl, n) * F(bl - 1, n))], '\\(\\frac{%d}{%d}\\cdot\\frac{%d}{%d}\\).' % (bl, n, bl - 1, n - 1), '\\(\\frac{%d}{%d}\\cdot\\frac{%d}{%d}\\).' % (bl, n, bl - 1, n - 1))
    (e4, v4_), (e5, v5_) = P['tf']
    t4 = tf(4, e4[0], e4[1], v4_, e4[2], e4[3]); t5 = tf(5, e5[0], e5[1], v5_, e5[2], e5[3])
    pa6, pb6 = P['and']; s6v = pa6 * pb6
    s6 = sh(6, '\\(P(B)=%s\\), \\(P(A\\mid B)=%s\\). Find \\(P(A\\cap B)\\) (decimal).' % (S.PE(pb6), S.PE(pa6)), 'Cho \\(P(B)=%s\\), \\(P(A\\mid B)=%s\\). Tính \\(P(A\\cap B)\\) (viết dạng thập phân).' % (PV(pb6), PV(pa6)), S.PE(s6v),
            '\\(%s\\cdot%s=%s\\).' % (S.PE(pb6), S.PE(pa6), S.PE(s6v)), '\\(P(A\\cap B)=P(B)P(A\\mid B)=%s\\).' % PV(s6v))
    tot, pos, tp = P['med']; v7 = F(tp, pos); assert v7.denominator in (2, 4, 5, 10, 20, 25, 50, 100)
    s7 = sh(7, 'In a survey of %d people, %d tested positive, of whom %d were actually sick. Find \\(P(\\text{sick}\\mid+)\\) (decimal).' % (tot, pos, tp), 'Khảo sát %d người: %d người dương tính, trong đó %d người thật sự mắc bệnh. Tính \\(P(\\text{bệnh}\\mid+)\\) (viết dạng thập phân).' % (tot, pos, tp), S.PE(v7),
            '\\(\\frac{%d}{%d}=%s\\).' % (tp, pos, S.PE(v7)), '\\(\\frac{%d}{%d}=%s\\).' % (tp, pos, PV(v7)))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
WA = (('\\(P(A\\mid B)=P(B\\mid A)\\) for all events \\(A\\), \\(B\\).', '\\(P(A\\mid B)=P(B\\mid A)\\) với mọi biến cố \\(A\\), \\(B\\).', 'They are equal only when \\(P(A)=P(B)\\) (or \\(P(A\\cap B)=0\\)).', 'Chỉ bằng nhau khi \\(P(A)=P(B)\\) (hoặc \\(P(A\\cap B)=0\\)).'), False)
WB = (('If \\(P(A)=0{,}3\\), \\(P(B)=0{,}5\\), \\(P(A\\cap B)=0{,}15\\) then \\(A\\), \\(B\\) are independent.', 'Nếu \\(P(A)=0{,}3\\), \\(P(B)=0{,}5\\), \\(P(A\\cap B)=0{,}15\\) thì \\(A\\), \\(B\\) độc lập.', '\\(0{,}3\\cdot0{,}5=0{,}15\\).', '\\(0{,}3\\cdot0{,}5=0{,}15\\).'), True)
WC = (('\\(P(\\overline A\\mid B)=1-P(A\\mid B)\\).', '\\(P(\\overline A\\mid B)=1-P(A\\mid B)\\).', 'Given \\(B\\), \\(A\\) and \\(\\overline A\\) are complementary.', 'Khi đã biết \\(B\\), \\(A\\) và \\(\\overline A\\) là hai biến cố đối.'), True)
WD = (('Drawing two balls with replacement, the second draw depends on the first.', 'Lấy hai bi có hoàn lại thì lần lấy thứ hai phụ thuộc lần thứ nhất.', 'With replacement the box is the same each time: independent.', 'Có hoàn lại thì hộp như cũ: hai lần lấy độc lập.'), False)
WE = (('\\(P(A\\cap B)=P(A)\\cdot P(B\\mid A)\\).', '\\(P(A\\cap B)=P(A)\\cdot P(B\\mid A)\\).', 'Multiplication rule.', 'Công thức nhân xác suất.'), True)
WF = (('If \\(P(A\\mid B)=0{,}6\\) then \\(P(A\\cap B)=0{,}6\\).', 'Nếu \\(P(A\\mid B)=0{,}6\\) thì \\(P(A\\cap B)=0{,}6\\).', '\\(P(A\\cap B)=0{,}6\\,P(B)\\), smaller unless \\(P(B)=1\\).', '\\(P(A\\cap B)=0{,}6\\,P(B)\\), nhỏ hơn 0,6 trừ khi \\(P(B)=1\\).'), False)
PP = [dict(f=(F(4, 10), F(1, 10)), tab=(8, 12, 6, 14), draw=(5, 4), tf=(WA, WB), **{'and': (F(1, 2), F(6, 10))}, med=(500, 40, 30)),
      dict(f=(F(5, 10), F(2, 10)), tab=(10, 15, 12, 13), draw=(3, 6), tf=(WC, WD), **{'and': (F(3, 4), F(4, 10))}, med=(800, 50, 35)),
      dict(f=(F(8, 10), F(6, 10)), tab=(9, 21, 15, 25), draw=(4, 5), tf=(WE, WF), **{'and': (F(2, 5), F(5, 10))}, med=(1000, 80, 52))]
practice = three(lvl, PP)
practice = with_self(practice, S.M18S12, start=8)
mistakes = [('<b>Dividing by \\(n(\\Omega)\\) instead of \\(n(B)\\).</b> Given \\(B\\), the sample space is \\(B\\).', '<b>Chia cho \\(n(\\Omega)\\) thay vì \\(n(B)\\).</b> Khi biết \\(B\\), không gian mẫu là \\(B\\).'),
            ('<b>Mixing up \\(P(A\\mid B)\\) and \\(P(B\\mid A)\\).</b> Ask: which event is known?', '<b>Nhầm \\(P(A\\mid B)\\) với \\(P(B\\mid A)\\).</b> Tự hỏi: biến cố nào đã biết?'),
            ('<b>Forgetting that the box changes without replacement.</b>', '<b>Quên rằng hộp thay đổi khi lấy không hoàn lại.</b>'),
            ('<b>Thinking "independent" = "mutually exclusive".</b> Exclusive events with positive probabilities are never independent.', '<b>Nghĩ "độc lập" là "xung khắc".</b> Hai biến cố xung khắc có xác suất dương thì không độc lập.')]
summary = [('\\(P(A\\mid B)=\\dfrac{P(A\\cap B)}{P(B)}=\\dfrac{n(A\\cap B)}{n(B)}\\) (equally likely outcomes).', '\\(P(A\\mid B)=\\dfrac{P(A\\cap B)}{P(B)}=\\dfrac{n(A\\cap B)}{n(B)}\\) (kết quả đồng khả năng).'),
           ('\\(P(A\\cap B)=P(B)P(A\\mid B)\\); \\(P(\\overline A\\mid B)=1-P(A\\mid B)\\).', '\\(P(A\\cap B)=P(B)P(A\\mid B)\\); \\(P(\\overline A\\mid B)=1-P(A\\mid B)\\).'),
           ('\\(A\\), \\(B\\) independent \\(\\iff P(A\\mid B)=P(A)\\iff P(A\\cap B)=P(A)P(B)\\).', '\\(A\\), \\(B\\) độc lập \\(\\iff P(A\\mid B)=P(A)\\iff P(A\\cap B)=P(A)P(B)\\).'),
           ('Key words: conditional probability, given, multiplication rule, independent, without replacement.', 'Từ cần nhớ: conditional probability, given, multiplication rule, independent, without replacement.')]
checks = [('I can compute \\(P(A\\mid B)\\) from a table or by counting.', 'Em tính được \\(P(A\\mid B)\\) từ bảng số liệu hoặc bằng cách đếm.'), ('I can use the formula \\(\\dfrac{P(A\\cap B)}{P(B)}\\).', 'Em dùng được công thức \\(\\dfrac{P(A\\cap B)}{P(B)}\\).'),
          ('I can use the multiplication rule for successive draws.', 'Em dùng được công thức nhân cho các lần lấy liên tiếp.'), ('I can check whether two events are independent.', 'Em kiểm tra được hai biến cố có độc lập không.')]
LL('g12-prob-01', 'Conditional Probability', CV, ('Conditional Probability', 'Xác suất có điều kiện'), 'probability', 'conditional-probability', 180, 'Intermediate', 80, ('classical probability, independent events', 'xác suất cổ điển, biến cố độc lập'),
   'Conditional probability by formula and by counting, the multiplication rule, independence, surveys and medical tests.', 'Bài 18 – Xác suất có điều kiện (công thức, đếm trên không gian mẫu thu hẹp), công thức nhân, tính độc lập, bài toán khảo sát và xét nghiệm.',
   ['conditional probability', 'multiplication rule', 'independent events', 'without replacement'], ['xác suất có điều kiện', 'công thức nhân', 'độc lập', 'không hoàn lại'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g12-stats-02'])
