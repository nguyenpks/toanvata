# -*- coding: utf-8 -*-
"""g11-prob-03 = Toán 11 KNTT, Bài 30: Công thức nhân xác suất cho hai biến cố độc lập. Mã ngân hàng câu hỏi: TOAN11-C8-B30."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g11j as S
import mb_pgf

CV = 'Công thức nhân xác suất'
dd = S.dec
vocab = defs(CV, [
 ('multrule', 'multiplication rule', 'công thức nhân xác suất', 'for independent events: \\(P(AB)=P(A)\\cdot P(B)\\).', 'với hai biến cố độc lập: \\(P(AB)=P(A)\\cdot P(B)\\).', 'By the multiplication rule, P(both hit) = 0.8 · 0.7.', '\\(P(AB)\\)'),
 ('indtrial', 'independent trials', 'phép thử độc lập', 'experiments whose results do not influence each other.', 'các phép thử mà kết quả của phép thử này không ảnh hưởng đến phép thử kia.', 'Repeated penalty kicks are modelled as independent trials.', ''),
 ('reliab', 'reliability', 'độ tin cậy', 'the probability that a device or system works.', 'xác suất để một thiết bị, hệ thống hoạt động tốt.', 'Two backup pumps increase the reliability.', '')])
goals = [('state the multiplication rule \\(P(AB)=P(A)P(B)\\) for independent events;', 'phát biểu [[công thức nhân xác suất]] \\(P(AB)=P(A)P(B)\\) cho hai biến cố độc lập;'),
         ('compute probabilities over several independent trials with tree diagrams;', 'tính xác suất qua nhiều [[phép thử độc lập]] bằng sơ đồ hình cây;'),
         ('combine the multiplication and addition rules ("exactly one", "at least one");', 'phối hợp công thức nhân và công thức cộng (bài toán "đúng một", "ít nhất một");'),
         ('compute the reliability of systems in series and in parallel.', 'tính [[độ tin cậy]] của hệ thống mắc nối tiếp, song song.')]
phrases = [('<b>The two shots are independent.</b>', 'Hai lần bắn độc lập với nhau.'), ('<b>Multiply along a branch, add across branches.</b>', 'Nhân dọc theo nhánh, cộng các nhánh lại.'),
           ('<b>The system works if at least one pump works.</b>', 'Hệ thống hoạt động nếu có ít nhất một máy bơm hoạt động.'), ('<b>The probability of missing all three is small.</b>', 'Xác suất trượt cả ba lần là nhỏ.'), ('<b>These cases are mutually exclusive.</b>', 'Các trường hợp này xung khắc với nhau.')]
review = T('From Bài 28–29: independent events, \\(P(\\overline A)=1-P(A)\\), \\(P(A\\cup B)=P(A)+P(B)-P(AB)\\); mutually exclusive events add.',
           'Từ Bài 28–29: biến cố độc lập, \\(P(\\overline A)=1-P(A)\\), \\(P(A\\cup B)=P(A)+P(B)-P(AB)\\); các biến cố xung khắc thì cộng xác suất.')

tree = mb_pgf.raw_svg(r'''\begin{tikzpicture}[grow=right, level distance=3cm, level 1/.style={sibling distance=3cm}, level 2/.style={sibling distance=1.5cm},
  every node/.style={font=\small, text=ink}, edge from parent/.style={draw=ink!60, line width=0.6pt}, el/.style={font=\footnotesize, fill=white, inner sep=1pt}]
\node[circle, fill=ink, inner sep=1.5pt] {}
  child {node {$\overline A$} child {node[label={[text=ink]right:$0{,}2\cdot0{,}3=0{,}06$}] {$\overline B$} edge from parent node[el] {$0{,}3$}} child {node[label={[text=ink]right:$0{,}2\cdot0{,}7=0{,}14$}] {$B$} edge from parent node[el] {$0{,}7$}} edge from parent node[el] {$0{,}2$}}
  child {node {$A$} child {node[label={[text=ink]right:$0{,}8\cdot0{,}3=0{,}24$}] {$\overline B$} edge from parent node[el] {$0{,}3$}} child {node[label={[text=ink]right:$0{,}8\cdot0{,}7=0{,}56$}] {$B$} edge from parent node[el] {$0{,}7$}} edge from parent node[el] {$0{,}8$}};
\end{tikzpicture}''')

circ = mb_pgf.raw_svg(r'''\begin{tikzpicture}[font=\small, every node/.style={text=ink}, box/.style={draw=ink, fill=blue!10, minimum width=1.1cm, minimum height=0.6cm}]
\draw[ink, line width=0.7pt] (0,0) -- (0.6,0); \node[box] (a) at (1.2,0) {$0{,}9$}; \draw[ink, line width=0.7pt] (a.east) -- (2.3,0); \node[box] (b) at (2.9,0) {$0{,}8$}; \draw[ink, line width=0.7pt] (b.east) -- (4.1,0);
\node at (2.05,-0.75) {nối tiếp: $0{,}9\cdot0{,}8=0{,}72$};
\begin{scope}[shift={(6,0)}]
\draw[ink, line width=0.7pt] (0,0) -- (0.5,0) -- (0.5,0.55) -- (1.1,0.55) (0.5,0) -- (0.5,-0.55) -- (1.1,-0.55);
\node[box] (c) at (1.65,0.55) {$0{,}9$}; \node[box] (d) at (1.65,-0.55) {$0{,}8$};
\draw[ink, line width=0.7pt] (c.east) -- (2.8,0.55) -- (2.8,-0.55) -- (d.east) (2.8,0) -- (3.3,0);
\node at (1.65,-1.3) {song song: $1-0{,}1\cdot0{,}2=0{,}98$};
\end{scope}
\end{tikzpicture}''')

theory = '<h3>30.1 %s</h3>' % TI('The multiplication rule', 'Công thức nhân xác suất')
theory += BOX('blue', ('Multiplication rule', 'Công thức nhân'), UL([
  T('If \\(A\\), \\(B\\) are independent: \\[P(AB)=P(A)\\cdot P(B).\\]', 'Nếu \\(A\\), \\(B\\) là hai biến cố độc lập thì \\[P(AB)=P(A)\\cdot P(B).\\]'),
  T('Conversely, if \\(P(AB)\\ne P(A)P(B)\\) then \\(A\\), \\(B\\) are <b>not</b> independent.', 'Ngược lại, nếu \\(P(AB)\\ne P(A)P(B)\\) thì \\(A\\), \\(B\\) <b>không</b> độc lập.'),
  T('For \\(n\\) mutually independent events: \\(P(A_1A_2\\ldots A_n)=P(A_1)P(A_2)\\ldots P(A_n)\\).', 'Với \\(n\\) biến cố độc lập: \\(P(A_1A_2\\ldots A_n)=P(A_1)P(A_2)\\ldots P(A_n)\\).')]))
theory += mb_pgf.img(tree, 'Tree diagram of two independent shooters with hit probabilities 0.8 and 0.7', 520,
  TI('Two independent shooters (\\(P(A)=0{,}8\\), \\(P(B)=0{,}7\\)): multiply along each branch; the four products add up to 1.', 'Hai xạ thủ bắn độc lập (\\(P(A)=0{,}8\\), \\(P(B)=0{,}7\\)): nhân dọc theo nhánh; bốn tích có tổng bằng 1.'))
theory += BOX('mint', ('Reading the tree', 'Đọc sơ đồ cây'), UL([T('Both hit: \\(0{,}56\\). Exactly one hits: \\(0{,}24+0{,}14=0{,}38\\) (two mutually exclusive branches).', 'Cả hai trúng: \\(0{,}56\\). Đúng một người trúng: \\(0{,}24+0{,}14=0{,}38\\) (hai nhánh xung khắc).'),
  T('At least one hits: \\(1-0{,}06=0{,}94\\).', 'Ít nhất một người trúng: \\(1-0{,}06=0{,}94\\).')]))
theory += '<h3>30.2 %s</h3>' % TI('Repeated trials and reliability', 'Phép thử lặp và độ tin cậy')
theory += BOX('blue', ('Typical patterns', 'Các dạng thường gặp'), UL([
  T('\\(n\\) independent trials, success probability \\(p\\) each: P(all succeed) \\(=p^n\\); P(at least one success) \\(=1-(1-p)^n\\).', '\\(n\\) phép thử độc lập, mỗi lần thành công với xác suất \\(p\\): P(thành công cả \\(n\\) lần) \\(=p^n\\); P(ít nhất một lần thành công) \\(=1-(1-p)^n\\).'),
  T('<b>Series</b> system (works only if all parts work): multiply the probabilities.', 'Hệ <b>nối tiếp</b> (chỉ hoạt động khi mọi bộ phận hoạt động): nhân các xác suất.'),
  T('<b>Parallel</b> system (works if at least one part works): \\(1-\\) product of failure probabilities.', 'Hệ <b>song song</b> (hoạt động khi có ít nhất một bộ phận hoạt động): \\(1-\\) tích các xác suất hỏng.')]))
theory += mb_pgf.img(circ, 'Two components in series and in parallel with reliabilities 0.9 and 0.8', 520, TI('Series: \\(0{,}72\\). Parallel (backup): \\(0{,}98\\) — redundancy increases reliability.', 'Nối tiếp: \\(0{,}72\\). Song song (dự phòng): \\(0{,}98\\) — mắc dự phòng làm tăng độ tin cậy.'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('Use the multiplication rule only for independent events. Drawing two balls one after another from the same box <i>without replacement</i> is not independent.', 'Chỉ dùng công thức nhân cho các biến cố độc lập. Lấy lần lượt hai viên bi từ cùng một hộp <i>không hoàn lại</i> thì các biến cố không độc lập.'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('A coin and a die', 'Đồng xu và xúc xắc'), T('A coin is tossed and a die is rolled. Find P(head and a number greater than 4).', 'Gieo một đồng xu và một con xúc xắc. Tính xác suất đồng xu ra mặt sấp và con xúc xắc ra số chấm lớn hơn 4.'),
  T('The two experiments are independent.', 'Hai phép thử độc lập.'), [T('\\(P(S)=\\frac12\\), \\(P(\\{5;6\\})=\\frac26=\\frac13\\).', '\\(P(S)=\\frac12\\), \\(P(\\{5;6\\})=\\frac26=\\frac13\\).'), T('\\(P=\\frac12\\cdot\\frac13\\).', '\\(P=\\frac12\\cdot\\frac13\\).')], T('\\(\\dfrac16\\).', '\\(\\dfrac16\\).'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Two shooters', 'Hai xạ thủ'), T('Two shooters hit with probabilities 0,8 and 0,7, independently. Find P(both hit), P(exactly one hits), P(at least one hits).', 'Hai xạ thủ bắn độc lập với xác suất trúng 0,8 và 0,7. Tính xác suất cả hai trúng, đúng một người trúng, ít nhất một người trúng.'),
  T('Use the tree above.', 'Dùng sơ đồ cây ở trên.'), [T('Both: \\(0{,}8\\cdot0{,}7=0{,}56\\).', 'Cả hai: \\(0{,}8\\cdot0{,}7=0{,}56\\).'), T('Exactly one: \\(0{,}8\\cdot0{,}3+0{,}2\\cdot0{,}7=0{,}38\\).', 'Đúng một: \\(0{,}8\\cdot0{,}3+0{,}2\\cdot0{,}7=0{,}38\\).'), T('At least one: \\(1-0{,}2\\cdot0{,}3=0{,}94\\).', 'Ít nhất một: \\(1-0{,}2\\cdot0{,}3=0{,}94\\).')],
  T('\\(0{,}56\\); \\(0{,}38\\); \\(0{,}94\\).', '\\(0{,}56\\); \\(0{,}38\\); \\(0{,}94\\).'))
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Penalty kicks', 'Sút phạt đền'), T('A player scores a penalty with probability 0,8; kicks are independent. In 3 kicks, find P(all scored) and P(at least one scored).', 'Một cầu thủ sút phạt đền thành công với xác suất 0,8; các lần sút độc lập. Trong 3 lần sút, tính xác suất thành công cả 3 lần và xác suất thành công ít nhất một lần.'),
  T('Repeated independent trials.', 'Phép thử lặp độc lập.'), [T('All: \\(0{,}8^3=0{,}512\\).', 'Cả 3 lần: \\(0{,}8^3=0{,}512\\).'), T('At least one: \\(1-0{,}2^3=1-0{,}008=0{,}992\\).', 'Ít nhất một lần: \\(1-0{,}2^3=1-0{,}008=0{,}992\\).')], T('\\(0{,}512\\) and \\(0{,}992\\).', '\\(0{,}512\\) và \\(0{,}992\\).'))
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Backup pumps', 'Máy bơm dự phòng'), T('A farm has two pumps working independently with reliability 0,9 and 0,8. Water is supplied if at least one pump works. Compare with using only the better pump.', 'Một trang trại có hai máy bơm hoạt động độc lập với độ tin cậy 0,9 và 0,8. Nước được cấp nếu có ít nhất một máy hoạt động. So sánh với việc chỉ dùng máy tốt hơn.'),
  T('Parallel system.', 'Hệ song song.'), [T('Both fail: \\(0{,}1\\cdot0{,}2=0{,}02\\).', 'Cả hai hỏng: \\(0{,}1\\cdot0{,}2=0{,}02\\).'), T('Reliability: \\(1-0{,}02=0{,}98>0{,}9\\).', 'Độ tin cậy: \\(1-0{,}02=0{,}98>0{,}9\\).')], T('\\(0{,}98\\): the backup pump cuts the failure risk from 10% to 2%.', '\\(0{,}98\\): máy dự phòng giảm nguy cơ mất nước từ 10% xuống 2%.'))
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Guessing a test', 'Đoán trắc nghiệm'), T('A student guesses 4 questions, each with 4 options, independently. Find P(exactly one correct) and P(at least one correct).', 'Một học sinh đoán ngẫu nhiên 4 câu trắc nghiệm, mỗi câu 4 phương án, các câu độc lập. Tính xác suất đúng đúng một câu và xác suất đúng ít nhất một câu.'),
  T('Exactly one: choose which question is correct (4 mutually exclusive cases).', 'Đúng một câu: chọn câu đúng (4 trường hợp xung khắc).'),
  [T('Each case: \\(\\frac14\\cdot\\left(\\frac34\\right)^3=\\frac{27}{256}\\); exactly one: \\(4\\cdot\\frac{27}{256}=\\frac{108}{256}=\\frac{27}{64}\\).', 'Mỗi trường hợp: \\(\\frac14\\cdot\\left(\\frac34\\right)^3=\\frac{27}{256}\\); đúng một câu: \\(4\\cdot\\frac{27}{256}=\\frac{27}{64}\\).'),
   T('At least one: \\(1-\\left(\\frac34\\right)^4=1-\\frac{81}{256}=\\frac{175}{256}\\).', 'Ít nhất một câu: \\(1-\\left(\\frac34\\right)^4=1-\\frac{81}{256}=\\frac{175}{256}\\).')], T('\\(\\dfrac{27}{64}\\approx0{,}42\\) and \\(\\dfrac{175}{256}\\approx0{,}68\\).', '\\(\\dfrac{27}{64}\\approx0{,}42\\) và \\(\\dfrac{175}{256}\\approx0{,}68\\).'))
examples = EXFIG(examples, 2, mb_pgf.img(tree, 'Tree diagram for two shooters', 460))


def lvl(P):
    p, q = P['pq']
    o1 = M4(1, 'Two independent shooters hit with probabilities %s and %s. P(exactly one hits) =…' % (dd(p), dd(q)), 'Hai xạ thủ bắn độc lập với xác suất trúng %s và %s. Xác suất có đúng một người bắn trúng là…' % (dd(p), dd(q)), '\\(%s\\)' % dd(p * (1 - q) + q * (1 - p)),
            ['\\(%s\\)' % dd(p * q), '\\(%s\\)' % dd(1 - (1 - p) * (1 - q)), '\\(%s\\)' % dd((1 - p) * (1 - q)), '\\(%s\\)' % dd(p * (1 - q))], 'Two exclusive branches.', '\\(%s\\cdot%s+%s\\cdot%s\\).' % (dd(p), dd(1 - q), dd(1 - p), dd(q)))
    a, b, c = P['ser']
    o2 = M4(2, 'A device has 3 independent parts in series with reliabilities %s, %s, %s. P(device works) =…' % (dd(a), dd(b), dd(c)), 'Một thiết bị gồm 3 bộ phận mắc nối tiếp, hoạt động độc lập với độ tin cậy %s, %s, %s. Xác suất thiết bị hoạt động là…' % (dd(a), dd(b), dd(c)), '\\(%s\\)' % dd(a * b * c),
            ['\\(%s\\)' % dd(1 - (1 - a) * (1 - b) * (1 - c)), '\\(%s\\)' % dd(min(a, b, c)), '\\(%s\\)' % dd(a * b), '\\(%s\\)' % dd((a + b + c) / 3)], 'Series: multiply.', 'Nối tiếp: \\(%s\\cdot%s\\cdot%s\\).' % (dd(a), dd(b), dd(c)))
    k, n = P['kick']
    o3 = M4(3, 'Each kick scores with probability %s, independently. P(at least one goal in %d kicks) =…' % (dd(k), n), 'Mỗi lần sút thành công với xác suất %s, các lần độc lập. Xác suất có ít nhất một lần thành công trong %d lần sút là…' % (dd(k), n), '\\(%s\\)' % dd(1 - (1 - k) ** n),
            ['\\(%s\\)' % dd(k ** n), '\\(%s\\)' % dd((1 - k) ** n), '\\(%s\\)' % dd(1 - k ** n)], 'Complement: all miss.', '\\(1-(1-%s)^%d\\).' % (dd(k), n))
    (se, sv), v4 = P['t4']
    t4 = tf(4, se, sv, v4, 'Independence is needed for the product.', 'Công thức nhân chỉ đúng cho biến cố độc lập.')
    (te, tv), v5 = P['t5']
    t5 = tf(5, te, tv, v5, 'Series multiplies, parallel uses the complement.', 'Nối tiếp: nhân; song song: dùng biến cố đối.')
    u, v = P['par']
    s6 = sh(6, 'Two backup generators work independently with reliabilities %s and %s. The reliability of the pair (at least one works), in percent, is…' % (dd(u), dd(v)), 'Hai máy phát điện dự phòng hoạt động độc lập với độ tin cậy %s và %s. Độ tin cậy của hệ (có ít nhất một máy chạy) bằng bao nhiêu phần trăm?' % (dd(u), dd(v)),
            int((1 - (1 - u) * (1 - v)) * 100), '\\(1-(1-u)(1-v)\\).', '\\(1-%s\\cdot%s\\).' % (dd(1 - u), dd(1 - v)))
    m = P['dice']
    s7 = sh(7, 'Two dice are rolled. P(both show a number at most %d) \\(=\\dfrac{a}{36}\\). Find \\(a\\).' % m, 'Gieo hai con xúc xắc. Xác suất cả hai con đều ra số chấm không lớn hơn %d bằng \\(\\dfrac{a}{36}\\). Tìm \\(a\\).' % m,
            m * m, '\\(\\frac m6\\cdot\\frac m6\\).', '\\(\\dfrac{%d}{6}\\cdot\\dfrac{%d}{6}=\\dfrac{%d}{36}\\).' % (m, m, m * m))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]


PP = [dict(pq=(F(9, 10), F(6, 10)), ser=(F(9, 10), F(9, 10), F(8, 10)), kick=(F(7, 10), 2),
           t4=(('If \\(A\\), \\(B\\) are independent, \\(P(A)=0{,}5\\), \\(P(B)=0{,}4\\), then \\(P(AB)=0{,}2\\).', 'Nếu \\(A\\), \\(B\\) độc lập, \\(P(A)=0{,}5\\), \\(P(B)=0{,}4\\) thì \\(P(AB)=0{,}2\\).'), True),
           t5=(('A parallel system is less reliable than each of its parts.', 'Hệ mắc song song có độ tin cậy nhỏ hơn từng bộ phận.'), False), par=(F(8, 10), F(7, 10)), dice=4),
      dict(pq=(F(7, 10), F(5, 10)), ser=(F(9, 10), F(8, 10), F(5, 10)), kick=(F(6, 10), 3),
           t4=(('Drawing two balls one after another without replacement from one box gives independent events.', 'Lấy lần lượt không hoàn lại hai viên bi từ cùng một hộp thì các biến cố "lần 1 đỏ", "lần 2 đỏ" độc lập.'), False),
           t5=(('A series system is at most as reliable as its weakest part.', 'Độ tin cậy của hệ nối tiếp không vượt quá độ tin cậy của bộ phận kém nhất.'), True), par=(F(9, 10), F(6, 10)), dice=5),
      dict(pq=(F(8, 10), F(4, 10)), ser=(F(8, 10), F(7, 10), F(5, 10)), kick=(F(4, 10), 3),
           t4=(('If \\(P(A)=0{,}6\\), \\(P(B)=0{,}5\\), \\(P(AB)=0{,}3\\), then \\(A\\), \\(B\\) are independent.', 'Nếu \\(P(A)=0{,}6\\), \\(P(B)=0{,}5\\), \\(P(AB)=0{,}3\\) thì \\(A\\), \\(B\\) độc lập.'), True),
           t5=(('Adding a backup in parallel always increases reliability (if the backup works with positive probability).', 'Mắc thêm một bộ phận dự phòng song song (có xác suất hoạt động dương) luôn làm tăng độ tin cậy.'), True), par=(F(5, 10), F(5, 10)), dice=2)]
practice = three(lvl, PP)
practice = with_self(practice, S.M30S11, start=8)
mistakes = [('<b>Multiplying dependent events.</b> Check independence first.', '<b>Nhân xác suất của các biến cố không độc lập.</b> Phải kiểm tra tính độc lập trước.'),
            ('<b>Adding instead of multiplying along a branch.</b> "and" multiplies, "or" (exclusive) adds.', '<b>Cộng thay vì nhân dọc theo nhánh.</b> "và" thì nhân, "hoặc" (xung khắc) thì cộng.'),
            ('<b>Forgetting a case in "exactly one".</b> Both branches \\(A\\overline B\\) and \\(\\overline AB\\) count.', '<b>Bỏ sót trường hợp khi tính "đúng một".</b> Cả hai nhánh \\(A\\overline B\\) và \\(\\overline AB\\) đều được tính.'),
            ('<b>Writing \\(P(\\text{at least one})=n\\cdot p\\).</b> Use \\(1-(1-p)^n\\).', '<b>Viết \\(P(\\text{ít nhất một})=n\\cdot p\\).</b> Phải dùng \\(1-(1-p)^n\\).')]
summary = [('Independent: \\(P(AB)=P(A)P(B)\\).', 'Độc lập: \\(P(AB)=P(A)P(B)\\).'), ('Trees: multiply along a branch, add mutually exclusive branches.', 'Sơ đồ cây: nhân dọc nhánh, cộng các nhánh xung khắc.'),
           ('\\(n\\) trials: all \\(p^n\\), at least one \\(1-(1-p)^n\\). Series: product; parallel: \\(1-\\prod(1-p_i)\\).', '\\(n\\) lần thử: tất cả \\(p^n\\), ít nhất một \\(1-(1-p)^n\\). Nối tiếp: tích; song song: \\(1-\\prod(1-p_i)\\).'), ('Key words: multiplication rule, independent trials, reliability.', 'Từ cần nhớ: multiplication rule, independent trials, reliability.')]
checks = [('I can apply \\(P(AB)=P(A)P(B)\\).', 'Em áp dụng được \\(P(AB)=P(A)P(B)\\).'), ('I can draw and read a probability tree.', 'Em vẽ và đọc được sơ đồ cây xác suất.'), ('I can compute "exactly one" and "at least one".', 'Em tính được xác suất "đúng một", "ít nhất một".'), ('I can compute the reliability of simple systems.', 'Em tính được độ tin cậy của hệ đơn giản.')]
LL('g11-prob-03', 'The Multiplication Rule for Independent Events', CV, ('Probability Rules', 'Các quy tắc tính xác suất'), 'probability-rules', 'multiplication-rule', 310, 'Intermediate', 60, ('addition rule of probability', 'công thức cộng xác suất'),
   'The multiplication rule for independent events, probability trees, repeated trials and the reliability of series and parallel systems.', 'Bài 30 – Công thức nhân xác suất cho hai biến cố độc lập; sơ đồ cây; phép thử lặp; độ tin cậy của hệ nối tiếp, song song.',
   ['multiplication rule', 'tree diagram', 'reliability'], ['công thức nhân', 'sơ đồ cây', 'độ tin cậy'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g11-prob-02'])
