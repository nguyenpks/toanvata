# -*- coding: utf-8 -*-
"""g11-prob-01 = Toán 11 KNTT, Bài 28: Biến cố hợp, biến cố giao, biến cố độc lập. Mã ngân hàng câu hỏi: TOAN11-C8-B28."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g11j as S
import mb_pgf

CV = 'Biến cố hợp, giao, độc lập'
vocab = defs(CV, [
 ('unionev', 'union of events', 'biến cố hợp', 'the event "A or B occurs" (at least one of them occurs), written \\(A\\cup B\\).', 'biến cố "A hoặc B xảy ra" (ít nhất một trong hai xảy ra), kí hiệu \\(A\\cup B\\).', 'Rain or wind tomorrow is a union of events.', '\\(A\\cup B\\)'),
 ('interev', 'intersection of events', 'biến cố giao', 'the event "both A and B occur", written \\(A\\cap B\\) or \\(AB\\).', 'biến cố "cả A và B cùng xảy ra", kí hiệu \\(A\\cap B\\) hay \\(AB\\).', 'Both shooters hit: an intersection.', '\\(AB\\)'),
 ('mutexcl', 'mutually exclusive', 'xung khắc', 'two events that cannot occur together: \\(A\\cap B=\\varnothing\\).', 'hai biến cố không thể cùng xảy ra: \\(A\\cap B=\\varnothing\\).', '"Even" and "odd" are mutually exclusive.', '\\(AB=\\varnothing\\)'),
 ('indepev11', 'independent events', 'biến cố độc lập', 'events where the occurrence of one does not change the probability of the other; then \\(P(AB)=P(A)P(B)\\).', 'hai biến cố mà việc xảy ra hay không của biến cố này không làm thay đổi xác suất của biến cố kia; khi đó \\(P(AB)=P(A)P(B)\\).', 'Two different dice give independent events.', '')])
goals = [('describe the union and the intersection of two events as sets of outcomes;', 'mô tả [[biến cố hợp]] và [[biến cố giao]] dưới dạng tập hợp các kết quả;'),
         ('recognise mutually exclusive events and independent events;', 'nhận biết hai biến cố [[xung khắc]] và hai [[biến cố độc lập]];'),
         ('use \\(P(AB)=P(A)P(B)\\) for independent events and check independence with it;', 'dùng \\(P(AB)=P(A)P(B)\\) cho hai biến cố độc lập và dùng đẳng thức này để kiểm tra tính độc lập;'),
         ('translate real situations (shooters, machines, weather) into unions and intersections.', 'chuyển tình huống thực tế (xạ thủ, máy móc, thời tiết) thành biến cố hợp, giao.')]
phrases = [('<b>A or B occurs.</b>', 'A hoặc B xảy ra.'), ('<b>Both A and B occur.</b>', 'Cả A và B cùng xảy ra.'), ('<b>The two events cannot happen at the same time.</b>', 'Hai biến cố không thể cùng xảy ra.'),
           ('<b>The result of one does not affect the other.</b>', 'Kết quả của phép thử này không ảnh hưởng đến phép thử kia.'), ('<b>At least one of the shooters hits the target.</b>', 'Có ít nhất một xạ thủ bắn trúng.')]
review = T('From Grade 10 (Bài 26): sample space \\(\\Omega\\), an event is a subset \\(A\\subset\\Omega\\), \\(P(A)=\\dfrac{n(A)}{n(\\Omega)}\\), \\(P(\\overline A)=1-P(A)\\). Set operations: \\(\\cup\\), \\(\\cap\\).',
           'Từ lớp 10 (Bài 26): không gian mẫu \\(\\Omega\\), biến cố là tập con \\(A\\subset\\Omega\\), \\(P(A)=\\dfrac{n(A)}{n(\\Omega)}\\), \\(P(\\overline A)=1-P(A)\\). Phép toán tập hợp: \\(\\cup\\), \\(\\cap\\).')

venn = mb_pgf.raw_svg(r'''\begin{tikzpicture}[font=\small, every node/.style={text=ink}]
\begin{scope}[shift={(0,0)}]
\draw[ink!70] (-1.9,-1.25) rectangle (1.9,1.25); \node at (-1.65,1.0) {$\Omega$};
\begin{scope} \clip (-0.45,0) circle (0.85); \fill[blue!25] (-2,-2) rectangle (2,2); \end{scope}
\begin{scope} \clip (0.45,0) circle (0.85); \fill[blue!25] (-2,-2) rectangle (2,2); \end{scope}
\draw[ink] (-0.45,0) circle (0.85) (0.45,0) circle (0.85); \node at (-0.85,0) {$A$}; \node at (0.85,0) {$B$}; \node at (0,-1.55) {$A\cup B$};
\end{scope}
\begin{scope}[shift={(4.3,0)}]
\draw[ink!70] (-1.9,-1.25) rectangle (1.9,1.25); \node at (-1.65,1.0) {$\Omega$};
\begin{scope} \clip (-0.45,0) circle (0.85); \fill[orange!45] (0.45,0) circle (0.85); \end{scope}
\draw[ink] (-0.45,0) circle (0.85) (0.45,0) circle (0.85); \node at (-0.85,0) {$A$}; \node at (0.85,0) {$B$}; \node at (0,-1.55) {$A\cap B=AB$};
\end{scope}
\begin{scope}[shift={(8.6,0)}]
\draw[ink!70] (-1.9,-1.25) rectangle (1.9,1.25); \node at (-1.65,1.0) {$\Omega$};
\draw[ink, fill=green!20] (-0.85,0) circle (0.65) (0.85,0) circle (0.65); \node at (-0.85,0) {$A$}; \node at (0.85,0) {$B$}; \node at (0,-1.55) {$AB=\varnothing$};
\end{scope}
\end{tikzpicture}''')

theory = '<h3>28.1 %s</h3>' % TI('Union and intersection of events', 'Biến cố hợp và biến cố giao')
theory += BOX('blue', ('Definitions', 'Định nghĩa'), UL([
  T('The <b>union</b> \\(A\\cup B\\) is the event "\\(A\\) or \\(B\\) occurs" (at least one of them). As sets: \\(\\Omega_{A\\cup B}=\\Omega_A\\cup\\Omega_B\\).', '[[Biến cố hợp]] \\(A\\cup B\\) là biến cố "\\(A\\) hoặc \\(B\\) xảy ra" (ít nhất một trong hai). Về tập hợp: \\(\\Omega_{A\\cup B}=\\Omega_A\\cup\\Omega_B\\).'),
  T('The <b>intersection</b> \\(A\\cap B\\) (also written \\(AB\\)) is the event "both \\(A\\) and \\(B\\) occur". As sets: \\(\\Omega_{AB}=\\Omega_A\\cap\\Omega_B\\).', '[[Biến cố giao]] \\(A\\cap B\\) (viết gọn \\(AB\\)) là biến cố "cả \\(A\\) và \\(B\\) cùng xảy ra". Về tập hợp: \\(\\Omega_{AB}=\\Omega_A\\cap\\Omega_B\\).'),
  T('\\(A\\), \\(B\\) are <b>mutually exclusive</b> if \\(AB=\\varnothing\\): they cannot occur together. \\(A\\) and \\(\\overline A\\) are always mutually exclusive.', '\\(A\\), \\(B\\) [[xung khắc]] nếu \\(AB=\\varnothing\\): chúng không thể cùng xảy ra. \\(A\\) và \\(\\overline A\\) luôn xung khắc.')]))
theory += mb_pgf.img(venn, 'Venn diagrams of the union, the intersection, and two mutually exclusive events', 600, TI('Left: \\(A\\cup B\\). Middle: \\(AB\\). Right: mutually exclusive events.', 'Trái: \\(A\\cup B\\). Giữa: \\(AB\\). Phải: hai biến cố xung khắc.'))
theory += BOX('mint', ('Example', 'Ví dụ'), T('Roll a die. \\(A\\): "even" \\(=\\{2;4;6\\}\\), \\(B\\): "at least 4" \\(=\\{4;5;6\\}\\). Then \\(A\\cup B=\\{2;4;5;6\\}\\), \\(AB=\\{4;6\\}\\). \\(A\\) and \\(C\\): "odd" are mutually exclusive.',
  'Gieo một con xúc xắc. \\(A\\): "số chẵn" \\(=\\{2;4;6\\}\\), \\(B\\): "không nhỏ hơn 4" \\(=\\{4;5;6\\}\\). Khi đó \\(A\\cup B=\\{2;4;5;6\\}\\), \\(AB=\\{4;6\\}\\). \\(A\\) và \\(C\\): "số lẻ" xung khắc.'))
theory += '<h3>28.2 %s</h3>' % TI('Independent events', 'Biến cố độc lập')
theory += BOX('blue', ('Definition and property', 'Định nghĩa và tính chất'), UL([
  T('\\(A\\), \\(B\\) are <b>independent</b> if whether one occurs does not change the probability of the other (typically: two separate experiments — two dice, two shooters, two machines).', 'Hai biến cố \\(A\\), \\(B\\) [[độc lập|biến cố độc lập]] nếu việc xảy ra hay không xảy ra của biến cố này không làm ảnh hưởng tới xác suất của biến cố kia (thường gặp: hai phép thử riêng rẽ — hai xúc xắc, hai xạ thủ, hai máy).'),
  T('If \\(A\\), \\(B\\) are independent, so are \\(A,\\overline B\\); \\(\\overline A,B\\); \\(\\overline A,\\overline B\\).', 'Nếu \\(A\\), \\(B\\) độc lập thì các cặp \\(A,\\overline B\\); \\(\\overline A,B\\); \\(\\overline A,\\overline B\\) cũng độc lập.'),
  T('\\(A\\), \\(B\\) independent \\(\\iff P(AB)=P(A)\\cdot P(B)\\) (the multiplication formula, studied in detail in Bài 30).', '\\(A\\), \\(B\\) độc lập \\(\\iff P(AB)=P(A)\\cdot P(B)\\) (công thức nhân, học kĩ ở Bài 30).')]))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('"Mutually exclusive" and "independent" are different. If \\(P(A)>0\\), \\(P(B)>0\\) and \\(A\\), \\(B\\) are mutually exclusive, then \\(P(AB)=0\\ne P(A)P(B)\\): they are <b>not</b> independent.',
  '"Xung khắc" và "độc lập" là hai khái niệm khác nhau. Nếu \\(P(A)>0\\), \\(P(B)>0\\) và \\(A\\), \\(B\\) xung khắc thì \\(P(AB)=0\\ne P(A)P(B)\\): chúng <b>không</b> độc lập.'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Describing a union and an intersection', 'Mô tả biến cố hợp, giao'), T('A number is chosen from 1 to 20. \\(A\\): "divisible by 2", \\(B\\): "divisible by 3". Describe \\(AB\\) and find \\(n(A\\cup B)\\).', 'Chọn ngẫu nhiên một số từ 1 đến 20. \\(A\\): "số chia hết cho 2", \\(B\\): "số chia hết cho 3". Mô tả biến cố \\(AB\\) và tính \\(n(A\\cup B)\\).'),
  T('\\(AB\\): divisible by both, i.e. by 6.', '\\(AB\\): chia hết cho cả 2 và 3, tức chia hết cho 6.'),
  [T('\\(AB=\\{6;12;18\\}\\), \\(n(AB)=3\\).', '\\(AB=\\{6;12;18\\}\\), \\(n(AB)=3\\).'), T('\\(n(A)=10\\), \\(n(B)=6\\), so \\(n(A\\cup B)=10+6-3=13\\).', '\\(n(A)=10\\), \\(n(B)=6\\), nên \\(n(A\\cup B)=10+6-3=13\\).')], T('\\(AB=\\{6;12;18\\}\\), \\(n(A\\cup B)=13\\).', '\\(AB=\\{6;12;18\\}\\), \\(n(A\\cup B)=13\\).'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Shooters', 'Hai xạ thủ'), T('Two shooters each fire once. \\(A\\): "the first hits", \\(B\\): "the second hits". Express in terms of \\(A\\), \\(B\\): (a) both hit; (b) at least one hits; (c) nobody hits.', 'Hai xạ thủ mỗi người bắn một phát. \\(A\\): "người thứ nhất bắn trúng", \\(B\\): "người thứ hai bắn trúng". Biểu diễn qua \\(A\\), \\(B\\): a) cả hai trúng; b) có ít nhất một người trúng; c) không ai trúng.'),
  T('"and" ↔ intersection, "or / at least one" ↔ union.', '"và" ↔ giao, "hoặc / ít nhất một" ↔ hợp.'), [T('(a) \\(AB\\); (b) \\(A\\cup B\\); (c) \\(\\overline A\\,\\overline B\\), the complement of \\(A\\cup B\\).', 'a) \\(AB\\); b) \\(A\\cup B\\); c) \\(\\overline A\\,\\overline B\\), là biến cố đối của \\(A\\cup B\\).')],
  T('\\(AB\\), \\(A\\cup B\\), \\(\\overline A\\,\\overline B=\\overline{A\\cup B}\\).', '\\(AB\\), \\(A\\cup B\\), \\(\\overline A\\,\\overline B=\\overline{A\\cup B}\\).'))
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Checking independence by counting', 'Kiểm tra tính độc lập bằng cách đếm'), T('Two dice are rolled. \\(A\\): "the first die shows 6", \\(B\\): "the sum is 7". Are \\(A\\), \\(B\\) independent?', 'Gieo hai con xúc xắc. \\(A\\): "con thứ nhất ra mặt 6", \\(B\\): "tổng số chấm bằng 7". Hai biến cố \\(A\\), \\(B\\) có độc lập không?'),
  T('Compare \\(P(AB)\\) with \\(P(A)P(B)\\).', 'So sánh \\(P(AB)\\) với \\(P(A)P(B)\\).'), [T('\\(P(A)=\\frac{6}{36}=\\frac16\\), \\(P(B)=\\frac{6}{36}=\\frac16\\).', '\\(P(A)=\\frac{6}{36}=\\frac16\\), \\(P(B)=\\frac{6}{36}=\\frac16\\).'), T('\\(AB=\\{(6;1)\\}\\): \\(P(AB)=\\frac1{36}=\\frac16\\cdot\\frac16\\).', '\\(AB=\\{(6;1)\\}\\): \\(P(AB)=\\frac1{36}=\\frac16\\cdot\\frac16\\).')],
  T('Yes, they are independent (a surprising but true fact).', 'Có, \\(A\\) và \\(B\\) độc lập (khá bất ngờ nhưng đúng).'))
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Two boxes', 'Hai hộp bi'), T('Box I: 3 red, 2 white balls. Box II: 4 red, 6 white. One ball is taken from each box. Find P(both red) and P(both white).', 'Hộp I có 3 bi đỏ, 2 bi trắng; hộp II có 4 bi đỏ, 6 bi trắng. Lấy ngẫu nhiên từ mỗi hộp một viên. Tính xác suất hai viên đều đỏ và hai viên đều trắng.'),
  T('The two draws are independent.', 'Hai lần lấy độc lập với nhau.'), [T('\\(P(\\text{both red})=\\frac35\\cdot\\frac4{10}=\\frac{6}{25}\\).', '\\(P(\\text{hai đỏ})=\\frac35\\cdot\\frac4{10}=\\frac{6}{25}\\).'), T('\\(P(\\text{both white})=\\frac25\\cdot\\frac6{10}=\\frac{6}{25}\\).', '\\(P(\\text{hai trắng})=\\frac25\\cdot\\frac6{10}=\\frac{6}{25}\\).')],
  T('\\(0{,}24\\) and \\(0{,}24\\).', '\\(0{,}24\\) và \\(0{,}24\\).'))
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Exclusive is not independent', 'Xung khắc không phải độc lập'), T('A die is rolled. \\(A\\): "the number is 1 or 2", \\(B\\): "the number is 5 or 6", \\(C\\): "the number is even". Which pairs are mutually exclusive? Which are independent?', 'Gieo một con xúc xắc. \\(A\\): "ra mặt 1 hoặc 2", \\(B\\): "ra mặt 5 hoặc 6", \\(C\\): "ra mặt chẵn". Cặp nào xung khắc? Cặp nào độc lập?'),
  T('Use sets and \\(P(XY)=P(X)P(Y)\\).', 'Dùng tập hợp và đẳng thức \\(P(XY)=P(X)P(Y)\\).'),
  [T('\\(AB=\\varnothing\\): mutually exclusive, and \\(P(AB)=0\\ne\\frac13\\cdot\\frac13\\): not independent.', '\\(AB=\\varnothing\\): xung khắc, và \\(P(AB)=0\\ne\\frac13\\cdot\\frac13\\): không độc lập.'),
   T('\\(AC=\\{2\\}\\): \\(P(AC)=\\frac16=\\frac13\\cdot\\frac12\\): independent.', '\\(AC=\\{2\\}\\): \\(P(AC)=\\frac16=\\frac13\\cdot\\frac12\\): độc lập.'), T('\\(BC=\\{6\\}\\): likewise independent.', '\\(BC=\\{6\\}\\): tương tự, độc lập.')],
  T('Only \\(A,B\\) are mutually exclusive; \\(A,C\\) and \\(B,C\\) are independent.', 'Chỉ \\(A,B\\) xung khắc; các cặp \\(A,C\\) và \\(B,C\\) độc lập.'))
examples = EXFIG(examples, 1, mb_pgf.img(venn, 'Venn diagrams of union and intersection', 520))


def dstr(x):
    return S.dec(x)


def lvl(P):
    (A, B, ae, av, be, bv) = P['sets']
    o1 = M4(1, 'A die is rolled. \\(A\\): "%s", \\(B\\): "%s". The event \\(A\\cap B\\) is…' % (ae, be), 'Gieo một con xúc xắc. \\(A\\): "%s", \\(B\\): "%s". Biến cố \\(A\\cap B\\) là…' % (av, bv), '\\(%s\\)' % S.setstr(A & B),
            ['\\(%s\\)' % S.setstr(A | B), '\\(%s\\)' % S.setstr(A - B), '\\(%s\\)' % S.setstr(B - A)], 'Common outcomes.', 'Các kết quả thuộc cả \\(A\\) và \\(B\\).')
    p, q = P['pq']
    o2 = M4(2, '\\(A\\), \\(B\\) are independent, \\(P(A)=%s\\), \\(P(B)=%s\\). \\(P(A\\overline B)=\\)…' % (dstr(p), dstr(q)), 'Hai biến cố \\(A\\), \\(B\\) độc lập, \\(P(A)=%s\\), \\(P(B)=%s\\). Khi đó \\(P(A\\overline B)=\\)…' % (dstr(p), dstr(q)), '\\(%s\\)' % dstr(p * (1 - q)),
            ['\\(%s\\)' % dstr(p * q), '\\(%s\\)' % dstr((1 - p) * q), '\\(%s\\)' % dstr((1 - p) * (1 - q))], '\\(A\\), \\(\\overline B\\) are independent.', '\\(A\\) và \\(\\overline B\\) độc lập: \\(%s\\cdot(1-%s)\\).' % (dstr(p), dstr(q)))
    a, b, c, d = P['box']
    pr = F(a, a + b) * F(c, c + d)
    o3 = M4(3, 'Box I: %d red, %d blue; box II: %d red, %d blue. One ball from each box. P(both blue) =…' % (a, b, c, d), 'Hộp I có %d bi đỏ, %d bi xanh; hộp II có %d bi đỏ, %d bi xanh. Lấy mỗi hộp một viên. Xác suất lấy được hai viên xanh là…' % (a, b, c, d), '\\(%s\\)' % fr(F(b, a + b) * F(d, c + d)),
            ['\\(%s\\)' % fr(pr), '\\(%s\\)' % fr(F(b + d, a + b + c + d)), '\\(%s\\)' % fr(F(b, a + b) + F(d, c + d) - F(b, a + b) * F(d, c + d))], 'Independent draws.', 'Hai lần lấy độc lập: \\(\\dfrac{%d}{%d}\\cdot\\dfrac{%d}{%d}\\).' % (b, a + b, d, c + d))
    (se, sv), v4 = P['t4']
    t4 = tf(4, se, sv, v4, 'Compare the definitions.', 'Đối chiếu định nghĩa xung khắc và độc lập.')
    (te, tv), v5 = P['t5']
    t5 = tf(5, te, tv, v5, 'Translate into union/intersection.', 'Chuyển sang ngôn ngữ hợp, giao.')
    N, m1, m2 = P['div']; l = m1 * m2 // math.gcd(m1, m2)
    s6 = sh(6, 'A number is chosen from 1 to %d. \\(A\\): "divisible by %d", \\(B\\): "divisible by %d". How many outcomes are in \\(A\\cup B\\)?' % (N, m1, m2), 'Chọn một số từ 1 đến %d. \\(A\\): "chia hết cho %d", \\(B\\): "chia hết cho %d". Biến cố \\(A\\cup B\\) có bao nhiêu kết quả thuận lợi?' % (N, m1, m2),
            N // m1 + N // m2 - N // l, '\\(n(A)+n(B)-n(AB)\\).', '\\(%d+%d-%d\\) (\\(AB\\): chia hết cho %d).' % (N // m1, N // m2, N // l, l))
    u, v = P['pct']
    s7 = sh(7, 'Two machines work independently with probabilities %s and %s. P(both work), as a percentage, is…' % (dstr(u), dstr(v)), 'Hai máy hoạt động độc lập với xác suất tốt lần lượt %s và %s. Xác suất cả hai máy đều tốt bằng bao nhiêu phần trăm?' % (dstr(u), dstr(v)),
            int(u * v * 100), '\\(P(AB)=P(A)P(B)\\).', '\\(%s\\cdot%s=%s\\).' % (dstr(u), dstr(v), dstr(u * v)))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]


PP = [dict(sets=({2, 4, 6}, {3, 4, 5, 6}, 'even number', 'at least 3', 'số chấm chẵn', 'số chấm không nhỏ hơn 3'), pq=(F(7, 10), F(4, 10)), box=(3, 2, 1, 4),
           t4=(('Two mutually exclusive events with positive probabilities are never independent.', 'Hai biến cố xung khắc có xác suất dương thì không độc lập.'), True),
           t5=(('"Nobody hits" is the complement of "at least one hits".', '"Không ai bắn trúng" là biến cố đối của "có ít nhất một người bắn trúng".'), True), div=(30, 2, 5), pct=(F(8, 10), F(9, 10))),
      dict(sets=({1, 3, 5}, {1, 2, 3}, 'odd number', 'at most 3', 'số chấm lẻ', 'số chấm không lớn hơn 3'), pq=(F(6, 10), F(3, 10)), box=(4, 1, 3, 2),
           t4=(('If \\(A\\), \\(B\\) are independent then \\(\\overline A\\), \\(\\overline B\\) are independent.', 'Nếu \\(A\\), \\(B\\) độc lập thì \\(\\overline A\\), \\(\\overline B\\) cũng độc lập.'), True),
           t5=(('The event "both hit" is \\(A\\cup B\\).', 'Biến cố "cả hai cùng bắn trúng" là \\(A\\cup B\\).'), False), div=(40, 4, 6), pct=(F(7, 10), F(9, 10))),
      dict(sets=({2, 3, 5}, {2, 4, 5, 6}, 'prime number', 'not 1 or 3', 'số nguyên tố', 'khác 1 và 3'), pq=(F(9, 10), F(3, 10)), box=(5, 3, 1, 4),
           t4=(('Mutually exclusive events are always independent.', 'Hai biến cố xung khắc thì luôn độc lập.'), False),
           t5=(('\\(A\\cup B\\) occurs when exactly one of \\(A\\), \\(B\\) occurs.', 'Biến cố \\(A\\cup B\\) chỉ xảy ra khi đúng một trong hai biến cố \\(A\\), \\(B\\) xảy ra.'), False), div=(50, 3, 4), pct=(F(6, 10), F(5, 10)))]
practice = three(lvl, PP)
practice = with_self(practice, S.M28S11, start=8)
mistakes = [('<b>Mixing up "or" and "and".</b> "At least one" is a union, "both" is an intersection.', '<b>Nhầm "hoặc" với "và".</b> "Ít nhất một" là hợp, "cả hai" là giao.'),
            ('<b>Thinking mutually exclusive means independent.</b> Exclusive events with positive probabilities are dependent.', '<b>Cho rằng xung khắc là độc lập.</b> Hai biến cố xung khắc có xác suất dương thì không độc lập.'),
            ('<b>Counting common outcomes twice.</b> \\(n(A\\cup B)=n(A)+n(B)-n(AB)\\).', '<b>Đếm hai lần các kết quả chung.</b> \\(n(A\\cup B)=n(A)+n(B)-n(AB)\\).'),
            ('<b>Assuming independence without reason.</b> Drawing two balls from the same box without replacement gives dependent events.', '<b>Mặc nhiên coi là độc lập.</b> Lấy lần lượt hai viên bi từ cùng một hộp không hoàn lại cho các biến cố không độc lập.')]
summary = [('\\(A\\cup B\\): at least one occurs; \\(AB\\): both occur.', '\\(A\\cup B\\): ít nhất một biến cố xảy ra; \\(AB\\): cả hai cùng xảy ra.'), ('Mutually exclusive: \\(AB=\\varnothing\\).', 'Xung khắc: \\(AB=\\varnothing\\).'),
           ('Independent: \\(P(AB)=P(A)P(B)\\); complements of independent events are independent.', 'Độc lập: \\(P(AB)=P(A)P(B)\\); các biến cố đối của chúng cũng độc lập.'), ('Key words: union, intersection, mutually exclusive, independent.', 'Từ cần nhớ: union, intersection, mutually exclusive, independent.')]
checks = [('I can write a union and an intersection as sets.', 'Em viết được biến cố hợp, giao dưới dạng tập hợp.'), ('I can tell exclusive events from independent ones.', 'Em phân biệt được biến cố xung khắc và độc lập.'),
          ('I can check independence with \\(P(AB)=P(A)P(B)\\).', 'Em kiểm tra được tính độc lập bằng \\(P(AB)=P(A)P(B)\\).'), ('I can model real situations with events.', 'Em mô tả được tình huống thực tế bằng biến cố.')]
LL('g11-prob-01', 'Union, Intersection and Independent Events', CV, ('Probability Rules', 'Các quy tắc tính xác suất'), 'probability-rules', 'union-intersection-independence', 290, 'Intermediate', 60, ('classical probability (Grade 10)', 'xác suất cổ điển (lớp 10)'),
   'Union and intersection of events, mutually exclusive events, independent events with real situations.', 'Bài 28 – Biến cố hợp, biến cố giao, biến cố xung khắc, biến cố độc lập qua các tình huống thực tế.',
   ['union', 'intersection', 'independent'], ['biến cố hợp', 'biến cố giao', 'độc lập'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g10-prob-02'])
