# -*- coding: utf-8 -*-
"""g10-sets-01: Sets and Intervals - chuyển sang khung v2 (nội dung giữ từ bản cũ)."""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
from mb_std import *
from mb_extra import *
import _vocab
figs = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '_sets_figures.json'), encoding='utf-8'))
CAT = ('Sets and Intervals', 'Tập hợp và khoảng')

goals = [
 (r'read and write set notation: \(a\in A\), \(A\subset B\), \(\{x\mid\dots\}\);', r'đọc và viết ký hiệu [[tập hợp]]: \(a\in A\), \(A\subset B\), \(\{x\mid\dots\}\);'),
 (r'find the union, intersection, difference and complement of sets;', r'tìm [[hợp]], [[giao]], [[hiệu]] và [[phần bù]] của các tập hợp;'),
 (r'write intervals in interval notation and show them on a number line;', r'viết các [[khoảng]] và biểu diễn chúng trên [[trục số]];'),
 (r'understand English instructions such as “Find \(A\cap B\)”.', r'hiểu các yêu cầu bằng tiếng Anh như “Find \(A\cap B\)”.')]

vocab = [
 (r'<b>set</b> – a collection of different objects. “A is a set of three numbers.”', r'[[Tập hợp]] – một nhóm các đối tượng khác nhau. “A là một tập hợp gồm ba số.”'),
 (r'<b>element</b> – an object that is in a set. “2 is an element of A.”', r'[[Phần tử]] – đối tượng nằm trong một tập hợp. “2 là một phần tử của A.”'),
 (r'<b>subset</b> – a set whose elements are all in another set. “{1, 2} is a subset of {1, 2, 3}.”', r'[[Tập con]] – tập hợp mà mọi phần tử đều thuộc một tập hợp khác. “{1, 2} là tập con của {1, 2, 3}.”'),
 (r'<b>empty set</b> – a set with no elements. “The empty set has no elements.”', r'[[Tập rỗng]] – tập hợp không có phần tử nào.'),
 (r'<b>union</b> – all elements that are in A, or in B, or in both. “Find the union of A and B.”', r'[[Hợp]] – gồm các phần tử thuộc A, hoặc thuộc B, hoặc thuộc cả hai. “Find the union of A and B.”'),
 (r'<b>intersection</b> – all elements that are in both A and B. “The intersection has one element.”', r'[[Giao]] – gồm các phần tử thuộc cả A và B. “The intersection has one element.”'),
 (r'<b>difference</b> – elements that are in A but not in B. “Find the difference A minus B.”', r'[[Hiệu]] – gồm các phần tử thuộc A nhưng không thuộc B. “Find the difference A minus B.”'),
 (r'<b>complement</b> – elements of the big set E that are not in A. “Find the complement of A in R.”', r'[[Phần bù]] – các phần tử của tập lớn E mà không thuộc A. “Find the complement of A in R.”'),
 (r'<b>interval</b> – the set of all real numbers between two numbers. “The interval from 1 to 3.”', r'[[Khoảng]] – tập các số thực nằm giữa hai số. “The interval from 1 to 3.”'),
 (r'<b>open interval</b> – an interval that does not contain its endpoints. “1 is not in the open interval (1, 3).”', r'[[Khoảng|khoảng (không chứa đầu mút)]] – khoảng không chứa đầu mút. “1 không thuộc khoảng (1, 3).”'),
 (r'<b>closed interval</b> – an interval that contains both endpoints. “3 is in the closed interval [1, 3].”', r'[[Đoạn|đoạn (chứa hai đầu mút)]] – khoảng chứa cả hai đầu mút. “3 thuộc đoạn [1, 3].”'),
 (r'<b>half-open interval</b> – an interval that contains only one endpoint. “[1, 3) is a half-open interval.”', r'[[Nửa khoảng]] – khoảng chỉ chứa một đầu mút. “[1, 3) là một nửa khoảng.”'),
 (r'<b>infinity</b> – a symbol for “without end”. It is not a real number. “x is greater than 2.”', r'[[Vô cực]] – ký hiệu cho “không có điểm dừng”; không phải là một số thực.')]

phrases = [
 (r'“Find \(A\cap B\).” – Find the intersection of \(A\) and \(B\).', r'“Find \(A\cap B\).” – Tìm [[giao]] của \(A\) và \(B\).'),
 (r'“Find \(A\cup B\).” – Find the union of \(A\) and \(B\).', r'“Find \(A\cup B\).” – Tìm [[hợp]] của \(A\) và \(B\).'),
 (r'“Find \(A\setminus B\).” – Find the difference: the elements of \(A\) that are not in \(B\).', r'“Find \(A\setminus B\).” – Tìm [[hiệu]]: các phần tử của \(A\) không thuộc \(B\).'),
 (r'“Write the answer in interval notation.” – Use brackets such as \([1,3)\).', r'“Write the answer in interval notation.” – Viết kết quả bằng ký hiệu khoảng, ví dụ \([1,3)\).'),
 (r'\(x\in A\) is read “x belongs to A” or “x is an element of A”.', r'\(x\in A\) đọc là “x belongs to A” hoặc “x is an element of A” (x [[thuộc]] A).'),
 (r'\(A\subset B\) is read “A is a subset of B”.', r'\(A\subset B\) đọc là “A is a subset of B” (A là [[tập con]] của B).'),
 (r'\(\{x\mid P(x)\}\) is read “the set of all x such that P of x”.', r'\(\{x\mid P(x)\}\) đọc là “the set of all x such that P(x)” (tập hợp các x sao cho P(x)).')]

review = (T(r'Before we start, recall three ideas from earlier grades.', r'Trước khi bắt đầu, hãy nhớ lại ba ý đã học ở các lớp trước.') +
 UL([T(r'An <b>integer</b> is a whole number such as \(-3\), \(0\) or \(7\). The number \(2.5\) is not an integer.', r'[[Số nguyên]] là số như \(-3\), \(0\), \(7\). Số \(2{,}5\) không phải là số nguyên.'),
     T(r'On the <b>number line</b>, the number on the right is greater: \(-3\gt-5\).', r'Trên [[trục số]], số nằm bên phải thì lớn hơn: \(-3\gt-5\).'),
     T(r'To solve \(2x-4\gt0\): add 4 to both sides, then divide by 2. The solution is \(x\gt2\).', r'Giải \(2x-4\gt0\): cộng 4 vào hai vế rồi chia cho 2, được \(x\gt2\).')]))

numtab = TBL([TI('Symbol', 'Ký hiệu'), TI('Name', 'Tên'), TI('Meaning', 'Ý nghĩa')], [
 [r'\(\mathbb{N}\)', TI('natural numbers', '[[số tự nhiên]]'), r'\(0,1,2,3,\dots\)'],
 [r'\(\mathbb{N}^*\)', TI('positive natural numbers', 'số tự nhiên khác 0'), r'\(1,2,3,\dots\)'],
 [r'\(\mathbb{Z}\)', TI('integers', '[[số nguyên]]'), r'\(\dots,-2,-1,0,1,2,\dots\)'],
 [r'\(\mathbb{Q}\)', TI('rational numbers', '[[số hữu tỉ]]'), TI(r'numbers \(\dfrac{a}{b}\) with \(a,b\in\mathbb{Z}\), \(b\ne0\)', r'các số dạng \(\dfrac{a}{b}\), \(a,b\in\mathbb{Z}\), \(b\ne0\)')],
 [r'\(\mathbb{R}\)', TI('real numbers', '[[số thực]]'), TI('all points on the number line', 'mọi điểm trên trục số')]])

inttab = TBL([TI('Interval', 'Khoảng'), TI('Set-builder notation', 'Viết bằng tính chất đặc trưng'), TI('Name', 'Tên gọi')], [
 [r'\((a,b)\)', r'\(\{x\mid a\lt x\lt b\}\)', TI('open interval', '[[khoảng|khoảng (không chứa đầu mút)]]')],
 [r'\([a,b]\)', r'\(\{x\mid a\le x\le b\}\)', TI('closed interval', '[[đoạn|đoạn (chứa hai đầu mút)]]')],
 [r'\([a,b)\)', r'\(\{x\mid a\le x\lt b\}\)', TI('half-open interval', '[[nửa khoảng]]')],
 [r'\((a,b]\)', r'\(\{x\mid a\lt x\le b\}\)', TI('half-open interval', '[[nửa khoảng]]')],
 [r'\((a,+\infty)\)', r'\(\{x\mid x\gt a\}\)', TI('open, unbounded on the right', 'khoảng không bị chặn bên phải')],
 [r'\([a,+\infty)\)', r'\(\{x\mid x\ge a\}\)', TI('half-open, unbounded on the right', 'nửa khoảng không bị chặn bên phải')],
 [r'\((-\infty,b)\)', r'\(\{x\mid x\lt b\}\)', TI('open, unbounded on the left', 'khoảng không bị chặn bên trái')],
 [r'\((-\infty,b]\)', r'\(\{x\mid x\le b\}\)', TI('half-open, unbounded on the left', 'nửa khoảng không bị chặn bên trái')],
 [r'\((-\infty,+\infty)\)', r'\(\mathbb{R}\)', TI('the whole real line', 'toàn bộ trục số')]])

theory = ('<h3>5.1 %s</h3>' % TI('Sets and elements', 'Tập hợp và phần tử') +
 BOX('mint', ('Definition', 'Định nghĩa'), T(r'A <b>set</b> is a collection of different objects. The objects in a set are called <b>elements</b>.', r'Một [[tập hợp]] là một nhóm các đối tượng xác định và khác nhau. Mỗi đối tượng gọi là một [[phần tử]] của tập hợp.')) +
 T(r'We write \(a\in A\) if \(a\) is an element of \(A\), and \(a\notin A\) if it is not.', r'Ta viết \(a\in A\) nếu \(a\) là phần tử của \(A\) (đọc: “\(a\) [[thuộc]] \(A\)”), và \(a\notin A\) nếu không phải.') +
 T(r'<b>Two ways to describe a set:</b>', r'<b>Hai cách cho một tập hợp:</b>') +
 UL([T(r'<b>Listing method</b>: \(A=\{1,2,3\}\).', r'<b>[[Liệt kê]]</b> các phần tử: \(A=\{1,2,3\}\).'),
     T(r'<b>Set-builder notation</b>: \(A=\{x\in\mathbb{N}\mid x\lt4\}\). Read: “the set of all \(x\) in \(\mathbb{N}\) such that \(x\) is less than 4”. This set is \(\{0,1,2,3\}\).', r'<b>[[Nêu tính chất đặc trưng]]</b>: \(A=\{x\in\mathbb{N}\mid x\lt4\}\), đọc là “tập hợp các \(x\) thuộc \(\mathbb{N}\) sao cho \(x\lt4\)”. Tập này bằng \(\{0,1,2,3\}\).')]) +
 T(r'Order and repetition do not matter: \(\{1,2,3\}=\{3,2,1\}=\{1,1,2,3\}\).', r'Thứ tự và sự lặp lại không làm thay đổi tập hợp: \(\{1,2,3\}=\{3,2,1\}=\{1,1,2,3\}\).') + numtab +
 BOX('yellow', ('Watch out!', 'Lưu ý'), T(r'In Vietnam, \(\mathbb{N}\) includes 0. Some English books start \(\mathbb{N}\) at 1.', r'Ở Việt Nam, \(\mathbb{N}\) gồm cả số 0. Một số sách tiếng Anh bắt đầu \(\mathbb{N}\) từ 1.')) +
 '<h3>5.2 %s</h3>' % TI('Subsets, equal sets, the empty set', 'Tập con, hai tập bằng nhau, tập rỗng') +
 BOX('mint', ('Definitions', 'Định nghĩa'),
   T(r'\(A\) is a <b>subset</b> of \(B\), written \(A\subset B\), if every element of \(A\) is also an element of \(B\).', r'\(A\) là [[tập con]] của \(B\), viết \(A\subset B\), nếu mọi phần tử của \(A\) đều thuộc \(B\).'),
   T(r'\(A=B\) if \(A\subset B\) and \(B\subset A\).', r'\(A=B\) khi \(A\subset B\) và \(B\subset A\).'),
   T(r'The <b>empty set</b> \(\varnothing\) has no elements. \(\varnothing\subset A\) and \(A\subset A\) for every set \(A\).', r'[[Tập rỗng]] \(\varnothing\) không có phần tử nào; \(\varnothing\subset A\) và \(A\subset A\) với mọi tập \(A\).')) +
 T(r'Vietnamese books use \(\subset\) (it allows \(A=B\)); some English books write \(\subseteq\).', r'Sách Việt Nam dùng \(\subset\) (cho phép \(A=B\)); một số sách tiếng Anh viết \(\subseteq\).') +
 BOX('yellow', ('Watch out!', 'Lưu ý'), T(r'\(2\in\{1,2,3\}\) is correct (2 is an element). \(\{2\}\subset\{1,2,3\}\) is correct (\(\{2\}\) is a set). But \(\{2\}\in\{1,2,3\}\) is wrong: use \(\in\) for elements and \(\subset\) for sets.', r'\(2\in\{1,2,3\}\) đúng (2 là phần tử). \(\{2\}\subset\{1,2,3\}\) đúng (\(\{2\}\) là tập hợp). Nhưng \(\{2\}\in\{1,2,3\}\) là sai: phần tử dùng \(\in\), tập hợp dùng \(\subset\).')) +
 '<h3>5.3 %s</h3>' % TI('Operations on sets', 'Các phép toán trên tập hợp') +
 T(r'<b>Intersection</b>: in both sets. <b>Union</b>: in at least one set (“or” in Math includes “both”). <b>Difference</b>: in \(A\) but not in \(B\). <b>Complement</b> of \(A\) in \(E\): elements of \(E\) that are not in \(A\).', r'[[Giao]]: thuộc cả hai tập. [[Hợp]]: thuộc ít nhất một tập (chữ “or” trong Toán nghĩa là “hoặc”, có thể cả hai). [[Hiệu]]: thuộc \(A\) nhưng không thuộc \(B\). [[Phần bù]] của \(A\) trong \(E\): các phần tử của \(E\) không thuộc \(A\).') +
 FIGR(figs[0], 'Shaded part: intersection, union, difference.', 'Phần tô màu: giao, hợp, hiệu.') +
 BOX('mint', ('Counting formula', 'Công thức đếm'), T(r'Let \(n(A)\) be the <b>number of elements</b> of \(A\). Then', r'Gọi \(n(A)\) là [[số phần tử]] của \(A\). Khi đó'),
   M(r'n(A\cup B)=n(A)+n(B)-n(A\cap B)'),
   T(r'Elements in both sets are counted twice, so we subtract them once.', r'Phần tử thuộc cả hai tập bị đếm hai lần nên phải trừ đi một lần.')) +
 '<h3>5.4 %s</h3>' % TI('Intervals', 'Khoảng, đoạn, nửa khoảng') +
 T(r'Intervals are subsets of \(\mathbb{R}\). The numbers \(a\) and \(b\) are called <b>endpoints</b>.', r'Các [[khoảng]] là tập con của \(\mathbb{R}\). Hai số \(a\), \(b\) gọi là [[đầu mút]].') + inttab +
 FIGR(figs[1], r'\([-2,3)\): filled dot = included, empty dot = not included.', r'\([-2,3)\): chấm đặc = lấy đầu mút; chấm rỗng = không lấy.') +
 BOX('blue', ('Rules', 'Quy tắc'),
   UL([T(r'Square bracket \([\ ]\) = the endpoint is <b>included</b>. Round bracket \((\ )\) = the endpoint is <b>not included</b>.', r'Ngoặc vuông \([\ ]\) = <b>lấy</b> đầu mút. Ngoặc tròn \((\ )\) = <b>không lấy</b> đầu mút.'),
       T(r'\(+\infty\) and \(-\infty\) are not numbers, so we always write a <b>round bracket</b> next to them.', r'[[Vô cực]] không phải là số, nên luôn dùng <b>ngoặc tròn</b> với \(+\infty\) và \(-\infty\).'),
       T(r'The smaller number goes first: \((1,3)\), not \((3,1)\).', r'Số nhỏ viết trước: \((1,3)\), không viết \((3,1)\).')])) +
 BOX('yellow', ('Notation note', 'Lưu ý ký hiệu'), T(r'Vietnamese books write \((a;b)\) with a semicolon. English books write \((a,b)\) with a comma. In short answers on this site, you can type either one.', r'Sách Việt Nam viết \((a;b)\) với dấu chấm phẩy; sách tiếng Anh viết \((a,b)\) với dấu phẩy. Khi nhập đáp án ngắn, bạn dùng cách nào cũng được.')) +
 BOX('blue', ('Tip: operations on intervals', 'Mẹo: phép toán trên khoảng'), T(r'Draw each set on its own number line. The <b>intersection</b> is the part covered by <b>both</b> lines. The <b>union</b> is the part covered by <b>at least one</b> line. Check each endpoint separately: is it in both sets, one set, or none?', r'Vẽ mỗi tập lên một trục số riêng. [[Giao]] là phần được phủ bởi <b>cả hai</b>; [[hợp]] là phần được phủ bởi <b>ít nhất một</b>. Hãy xét riêng từng đầu mút: nó thuộc cả hai tập, một tập, hay không tập nào?')))

ex = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Operations on finite sets', 'Phép toán trên tập hữu hạn'),
  T(r'Let \(A=\{1,2,3,4,5,6\}\) and \(B=\{2,4,6,8\}\). Find \(A\cap B\), \(A\cup B\) and \(A\setminus B\).', r'Cho \(A=\{1,2,3,4,5,6\}\) và \(B=\{2,4,6,8\}\). Tìm \(A\cap B\), \(A\cup B\) và \(A\setminus B\).'),
  (r'We need three sets: the common elements (intersection), all elements written once (union), and the elements in \(A\) but not in \(B\) (difference).', r'Cần tìm ba tập: các phần tử chung ([[giao]]); tất cả phần tử, mỗi phần tử viết một lần ([[hợp]]); phần tử của \(A\) không thuộc \(B\) ([[hiệu]]).'),
  [T(r'Intersection: the elements in both sets are \(2,4,6\). So \(A\cap B=\{2,4,6\}\).', r'[[Giao]]: các phần tử thuộc cả hai tập là \(2,4,6\). Vậy \(A\cap B=\{2,4,6\}\).'),
   T(r'Union: put all elements together and write each one once: \(A\cup B=\{1,2,3,4,5,6,8\}\).', r'[[Hợp]]: gộp tất cả phần tử, phần tử trùng chỉ viết một lần: \(A\cup B=\{1,2,3,4,5,6,8\}\).'),
   T(r'Difference: remove from \(A\) the elements that are in \(B\): \(A\setminus B=\{1,3,5\}\).', r'[[Hiệu]]: bỏ khỏi \(A\) các phần tử thuộc \(B\): \(A\setminus B=\{1,3,5\}\).')],
  r'\(A\cap B=\{2,4,6\}\); \(A\cup B=\{1,2,3,4,5,6,8\}\); \(A\setminus B=\{1,3,5\}\)')
ex += EXAMPLE(2, ('Intermediate', 'Trung bình'), ('Operations on intervals', 'Phép toán trên khoảng'),
  T(r'Let \(A=[-3,2)\) and \(B=(0,5]\). Find \(A\cap B\), \(A\cup B\) and \(A\setminus B\). Write each answer in interval notation.', r'Cho \(A=[-3,2)\) và \(B=(0,5]\). Tìm \(A\cap B\), \(A\cup B\), \(A\setminus B\); viết kết quả dưới dạng khoảng, đoạn hoặc nửa khoảng.'),
  (r'Both sets are intervals of \(\mathbb{R}\). Compare them on a number line and check each endpoint: \(-3\), \(0\), \(2\), \(5\).', r'Cả hai tập đều là [[khoảng]] của \(\mathbb{R}\). Đặt chúng lên [[trục số]] và xét riêng từng [[đầu mút]]: \(-3\), \(0\), \(2\), \(5\).'),
  [T(r'Write the sets with inequalities: \(A=\{x\mid-3\le x\lt2\}\), \(B=\{x\mid0\lt x\le5\}\).', r'Viết hai tập bằng bất đẳng thức: \(A=\{x\mid-3\le x\lt2\}\), \(B=\{x\mid0\lt x\le5\}\).'),
   T(r'Intersection: we need \(-3\le x\lt2\) <b>and</b> \(0\lt x\le5\). Together: \(0\lt x\lt2\). So \(A\cap B=(0,2)\).', r'[[Giao]]: cần \(-3\le x\lt2\) <b>và</b> \(0\lt x\le5\). Kết hợp: \(0\lt x\lt2\). Vậy \(A\cap B=(0,2)\).'),
   T(r'Union: the intervals overlap on \((0,2)\) and \(2\in B\), so there is no gap, from \(-3\) (included) to \(5\) (included). \(A\cup B=[-3,5]\).', r'[[Hợp]]: hai khoảng chồng lên nhau trên \((0,2)\) và \(2\in B\), nên không bị hở: từ \(-3\) (lấy) đến \(5\) (lấy). \(A\cup B=[-3,5]\).'),
   T(r'Difference: \(x\in A\) and \(x\notin B\). Since \(x\lt2\), the condition \(x\notin B\) means \(x\le0\). So \(A\setminus B=[-3,0]\); \(0\) is included because \(0\in A\) and \(0\notin B\).', r'[[Hiệu]]: \(x\in A\) và \(x\notin B\). Vì \(x\lt2\), điều kiện \(x\notin B\) nghĩa là \(x\le0\). Vậy \(A\setminus B=[-3,0]\); số \(0\) được lấy vì \(0\in A\) và \(0\notin B\).')],
  r'\(A\cap B=(0,2)\); \(A\cup B=[-3,5]\); \(A\setminus B=[-3,0]\)')
ex += EXAMPLE(3, ('Advanced', 'Nâng cao'), ('A class survey', 'Khảo sát một lớp học'),
  T(r'In a class of 40 students, 25 students play football, 18 play volleyball and 8 play both sports. (a) How many students play at least one sport? (b) How many play neither sport? (c) How many play football only? Explain why we subtract 8 in part (a).', r'Một lớp có 40 học sinh: 25 em chơi bóng đá, 18 em chơi bóng chuyền và 8 em chơi cả hai môn. (a) Có bao nhiêu em chơi ít nhất một môn? (b) Có bao nhiêu em không chơi môn nào? (c) Có bao nhiêu em chỉ chơi bóng đá? Giải thích vì sao ở câu (a) phải trừ 8.'),
  (r'Let \(F\) be the set of football players and \(V\) the set of volleyball players. “At least one” means union. “Both” means intersection. “Only football” means \(F\setminus V\).', r'Gọi \(F\) là tập các em chơi bóng đá, \(V\) là tập các em chơi bóng chuyền. “Ít nhất một môn” là [[hợp]]; “cả hai môn” là [[giao]]; “chỉ bóng đá” là [[hiệu]] \(F\setminus V\).'),
  [T(r'We have \(n(F)=25\), \(n(V)=18\), \(n(F\cap V)=8\).', r'Ta có \(n(F)=25\), \(n(V)=18\), \(n(F\cap V)=8\).'),
   T(r'(a) \(n(F\cup V)=25+18-8=35\). So 35 students play at least one sport. Why subtract 8? The 8 students who play both sports are counted once in 25 and again in 18. We must count them only once.', r'(a) \(n(F\cup V)=25+18-8=35\). Có 35 em chơi ít nhất một môn. Vì sao trừ 8? 8 em chơi cả hai môn đã bị đếm một lần trong 25 và một lần nữa trong 18; ta chỉ được đếm họ một lần.'),
   T(r'(b) The other students play neither sport: \(40-35=5\).', r'(b) Số em không chơi môn nào: \(40-35=5\).'),
   T(r'(c) \(n(F\setminus V)=25-8=17\). Check: football only \(17\) + volleyball only \(10\) + both \(8\) = \(35\). It matches (a).', r'(c) \(n(F\setminus V)=25-8=17\). Kiểm tra: chỉ bóng đá \(17\) + chỉ bóng chuyền \(10\) + cả hai \(8\) = \(35\), khớp với câu (a).')],
  r'(a) 35 students; (b) 5 students; (c) 17 students')

YN = lambda: None
_PR1 = [
 (('A. Multiple Choice', 'A. Trắc nghiệm nhiều lựa chọn'), [
  MCQ(1, (r'Which statement is true?', r'Khẳng định nào đúng?'), [r'3\notin\{1,2,3\}', r'\{2\}\in\{1,2,3\}', r'2\in\{1,2,3\}', r'4\in\{1,2,3\}'], 'c',
      (r'Answer: c. 2 is an element of \(\{1,2,3\}\). In (b), \(\{2\}\) is a set, not an element.', r'Đáp án c. 2 là [[phần tử]] của tập. Ở câu b, \(\{2\}\) là tập hợp chứ không phải phần tử; phải viết \(\{2\}\subset\{1,2,3\}\).')),
  MCQ(2, (r'Which set-builder notation describes the interval \((-2,5]\)?', r'Cách viết nào mô tả khoảng \((-2,5]\) bằng tính chất đặc trưng?'), [r'\{x\in\mathbb{R}\mid-2\le x\le5\}', r'\{x\in\mathbb{R}\mid-2\lt x\le5\}', r'\{x\in\mathbb{R}\mid-2\lt x\lt5\}', r'\{x\in\mathbb{R}\mid-2\le x\lt5\}'], 'b',
      (r'Answer: b. The round bracket at \(-2\) means not included (\(\lt\)). The square bracket at 5 means included (\(\le\)).', r'Đáp án b. Ngoặc tròn ở \(-2\): không lấy (\(\lt\)). Ngoặc vuông ở 5: lấy (\(\le\)).')),
  MCQ(3, (r'Let \(A=\{1,3,5\}\) and \(B=\{3,5,7\}\). What is \(A\cup B\)?', r'Cho \(A=\{1,3,5\}\), \(B=\{3,5,7\}\). Tìm \(A\cup B\).'), [r'\{3,5\}', r'\{1,3,5,7\}', r'\{1,7\}', r'\{1,3,5,3,5,7\}'], 'b',
      (r'Answer: b. The union has all elements of both sets, each written once. (a) is the intersection; (d) repeats elements.', r'Đáp án b. [[Hợp]] gồm mọi phần tử của hai tập, mỗi phần tử viết một lần. Đáp án a là [[giao]]; d sai vì viết lặp.')),
  MCQ(4, (r'What is \([1,4]\cap(3,6)\)?', r'Tìm \([1,4]\cap(3,6)\).'), [r'(3,4]', r'[3,4]', r'(3,4)', r'[1,6)'], 'a',
      (r'Answer: a. We need \(1\le x\le4\) and \(3\lt x\lt6\), so \(3\lt x\le4\). 3 is not included since \(3\notin(3,6)\); 4 is included since it is in both sets.', r'Đáp án a. Cần \(1\le x\le4\) và \(3\lt x\lt6\), nên \(3\lt x\le4\). Số 3 không lấy vì \(3\notin(3,6)\); số 4 lấy vì thuộc cả hai tập.')),
  MCQ(5, (r'Which set is the empty set?', r'Tập hợp nào là tập rỗng?'), [r'\{0\}', r'\{x\in\mathbb{R}\mid x^2=-1\}', r'\{x\in\mathbb{Z}\mid |x|\lt1\}', r'\{x\in\mathbb{R}\mid x^2=0\}'], 'b',
      (r'Answer: b. No real number has a square equal to \(-1\). The sets in a, c, d are all \(\{0\}\), which has one element.', r'Đáp án b. Không có số thực nào có bình phương bằng \(-1\). Các tập ở a, c, d đều bằng \(\{0\}\), có một phần tử.'))]),
 (('B. True or False', 'B. Đúng hoặc sai'), [
  TF(6, (r'True or false: \(\mathbb{N}\subset\mathbb{Z}\).', r'Đúng hay sai: \(\mathbb{N}\subset\mathbb{Z}\).'), 'true', (r'True. Every natural number is an integer.', r'Đúng. Mọi số tự nhiên đều là số nguyên.')),
  TF(7, (r'True or false: the interval \([2,+\infty]\) is written correctly.', r'Đúng hay sai: cách viết \([2,+\infty]\) là đúng.'), 'false', (r'False. \(+\infty\) is not a number, so it needs a round bracket: \([2,+\infty)\).', r'Sai. [[Vô cực]] không phải là số nên luôn dùng ngoặc tròn: \([2,+\infty)\).')),
  TF(8, (r'True or false: if \(A\subset B\), then \(A\cap B=A\).', r'Đúng hay sai: nếu \(A\subset B\) thì \(A\cap B=A\).'), 'true', (r'True. Every element of \(A\) is in \(B\), so the common part is exactly \(A\). Example: \(\{1\}\subset\{1,2\}\) gives \(\{1\}\).', r'Đúng. Mọi phần tử của \(A\) đều thuộc \(B\), nên phần chung của hai tập chính là \(A\). Ví dụ \(\{1\}\subset\{1,2\}\): giao là \(\{1\}\).'))]),
 (('C. Short Answer', 'C. Trả lời ngắn'), [
  SHORT(9, (r'How many elements does \(\{x\in\mathbb{Z}\mid-2\le x\lt3\}\) have?', r'Tập \(\{x\in\mathbb{Z}\mid-2\le x\lt3\}\) có bao nhiêu phần tử?'), '5', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'),
        (r'Answer: 5. The integers are \(-2,-1,0,1,2\). The number 3 is not included.', r'Đáp số: 5. Các số nguyên là \(-2,-1,0,1,2\); số 3 không được lấy.')),
  SHORT(10, (r'Write \((-\infty,1]\cap[-1,4)\) as one interval.', r'Viết \((-\infty,1]\cap[-1,4)\) thành một khoảng.'), '[-1,1]', 'interval', (r'Write it like (a,b] or [a,b). You can use a comma or a semicolon.', r'Viết dạng (a,b] hoặc [a,b); dùng dấu phẩy hoặc chấm phẩy đều được.'),
        (r'Answer: \([-1,1]\). We need \(x\le1\) and \(-1\le x\lt4\), so \(-1\le x\le1\).', r'Đáp số: \([-1,1]\). Cần \(x\le1\) và \(-1\le x\lt4\), nên \(-1\le x\le1\); cả hai đầu mút đều được lấy.')),
  SHORT(11, (r'In a group of 30 students, 18 like Math, 15 like English and 6 like both. How many students like neither subject?', r'Trong nhóm 30 học sinh, 18 em thích Toán, 15 em thích Tiếng Anh và 6 em thích cả hai. Có bao nhiêu em không thích môn nào?'), '3', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'),
        (r'Answer: 3. \(n(M\cup E)=18+15-6=27\), so \(30-27=3\) students like neither.', r'Đáp số: 3. \(n(M\cup E)=18+15-6=27\), nên \(30-27=3\) em không thích môn nào.'))]),
 (('D. Mathematical English', 'D. Tiếng Anh Toán học'), [
  MCQ(12, (r'Which instruction means “Tìm giao của \(A\) và \(B\)”?', r'Câu lệnh nào có nghĩa “Tìm giao của \(A\) và \(B\)”?'),
      [r'\text{Find the union of }A\text{ and }B.', r'\text{Find the intersection of }A\text{ and }B.', r'\text{Find the difference of }A\text{ and }B.', r'\text{Find the complement of }A.'], 'b',
      (r'Answer: b. Intersection = giao; union = hợp; difference = hiệu; complement = phần bù.', r'Đáp án b. intersection = giao; union = hợp; difference = hiệu; complement = phần bù.')),
  MCQ(13, (r'How do we read \(x\in A\) in English?', r'Ký hiệu \(x\in A\) đọc bằng tiếng Anh như thế nào?'),
      [r'\text{x contains A}', r'\text{x is a subset of A}', r'\text{x belongs to A}', r'\text{x equals A}'], 'c',
      (r'Answer: c. “x belongs to A” or “x is an element of A”.', r'Đáp án c. “x belongs to A” hoặc “x is an element of A” (x thuộc A).'))]),
 (('E. Problem Solving and Explanation (not scored)', 'E. Tự luận và giải thích (không tính điểm)'), [
  T(r'Let \(A=[-1,4)\) and \(B=(2,7)\). (a) Find \(A\cap B\), \(A\cup B\) and \(A\setminus B\). (b) Is \(4\) an element of \(A\cap B\)? Explain in simple English.', r'Cho \(A=[-1,4)\) và \(B=(2,7)\). (a) Tìm \(A\cap B\), \(A\cup B\), \(A\setminus B\). (b) \(4\) có thuộc \(A\cap B\) không? Giải thích bằng tiếng Anh đơn giản.') +
  REVEAL(T(r'(a) \(A\cap B=(2,4)\); \(A\cup B=[-1,7)\); \(A\setminus B=[-1,2]\). The sets overlap on \((2,4)\). The union starts at \(-1\) (included in \(A\)) and ends at 7 (not included in \(B\)). For the difference, we keep the numbers of \(A\) that are not in \(B\), so \(x\le2\); 2 is kept because \(2\notin B\).', r'(a) \(A\cap B=(2,4)\); \(A\cup B=[-1,7)\); \(A\setminus B=[-1,2]\). Hai tập chồng nhau trên \((2,4)\). Hợp bắt đầu từ \(-1\) (lấy, vì thuộc \(A\)) và kết thúc ở 7 (không lấy, vì \(B\) mở). Với hiệu, giữ các số của \(A\) không thuộc \(B\), tức \(x\le2\); số 2 được giữ vì \(2\notin B\).') +
         T(r'(b) No. The number 4 is not in \(A\) because \(A\) has a round bracket at 4. So 4 is not in \(A\cap B\).', r'(b) Không. Số 4 không thuộc \(A\) (ngoặc tròn ở 4) nên không thuộc \(A\cap B\). Câu trả lời tiếng Anh mẫu: “No. 4 is not in A because A has a round bracket at 4.”')),
  T(r'In 2–3 simple English sentences, explain why \((1,3)\) and \([1,3]\) are different sets.', r'Viết 2–3 câu tiếng Anh đơn giản để giải thích vì sao \((1,3)\) và \([1,3]\) là hai tập khác nhau.') +
  REVEAL(T(r'Sample answer: “The interval \((1,3)\) does not include 1 and 3, because round brackets mean the endpoints are not included. The interval \([1,3]\) includes both 1 and 3. For example, 1 is in \([1,3]\) but not in \((1,3)\).”', r'Câu trả lời mẫu (giữ bằng tiếng Anh). Hãy so sánh: bài của bạn đã nêu được “đầu mút có/không thuộc tập hợp” và một ví dụ cụ thể chưa?'))])]

# ----- Bài tập: mỗi mức một bộ riêng, cùng dạng, khác số liệu (LEVEL_PRACTICE) -----
_T = [g[0] for g in _PR1]
S1 = [g[1] for g in _PR1]
S2 = [
 [MCQ(1, (r'Which of these statements is correct?', r'Khẳng định nào sau đây là chính xác?'), [r'\{4\}\in\{2,4,6\}', r'4\notin\{2,4,6\}', r'6\in\{2,4\}', r'4\in\{2,4,6\}'], 'd',
      (r'Answer: d. 4 is an element of \(\{2,4,6\}\). In (a), \(\{4\}\) is a set, not an element.', r'Đáp án d. 4 là [[phần tử]] của tập \(\{2,4,6\}\). Ở câu a, \(\{4\}\) là tập hợp chứ không phải phần tử; phải viết \(\{4\}\subset\{2,4,6\}\).')),
  MCQ(2, (r'Which set-builder notation describes the interval \([-3,4)\)?', r'Cách viết nào mô tả đoạn nửa khoảng \([-3,4)\) bằng tính chất đặc trưng?'), [r'\{x\in\mathbb{R}\mid-3\lt x\lt4\}', r'\{x\in\mathbb{R}\mid-3\le x\le4\}', r'\{x\in\mathbb{R}\mid-3\le x\lt4\}', r'\{x\in\mathbb{R}\mid-3\lt x\le4\}'], 'c',
      (r'Answer: c. The square bracket at \(-3\) means included (\(\le\)). The round bracket at 4 means not included (\(\lt\)).', r'Đáp án c. Ngoặc vuông ở \(-3\): lấy (\(\le\)). Ngoặc tròn ở 4: không lấy (\(\lt\)).')),
  MCQ(3, (r'Let \(A=\{2,4,6\}\) and \(B=\{4,6,8\}\). What is \(A\cap B\)?', r'Cho \(A=\{2,4,6\}\), \(B=\{4,6,8\}\). Tìm \(A\cap B\).'), [r'\{2,4,6,8\}', r'\{4,6\}', r'\{2,8\}', r'\{4,6,4,6\}'], 'b',
      (r'Answer: b. The intersection has the elements that are in both sets: 4 and 6. (a) is the union; (d) repeats elements.', r'Đáp án b. [[Giao]] gồm các phần tử thuộc cả hai tập: 4 và 6. Đáp án a là [[hợp]]; d sai vì viết lặp.')),
  MCQ(4, (r'What is \([0,5)\cap(2,9)\)?', r'Tìm \([0,5)\cap(2,9)\).'), [r'(2,5)', r'[2,5)', r'(2,5]', r'[0,9)'], 'a',
      (r'Answer: a. We need \(0\le x\lt5\) and \(2\lt x\lt9\), so \(2\lt x\lt5\). 2 is not included since \(2\notin(2,9)\); 5 is not included since \(5\notin[0,5)\).', r'Đáp án a. Cần \(0\le x\lt5\) và \(2\lt x\lt9\), nên \(2\lt x\lt5\). Số 2 không lấy vì \(2\notin(2,9)\); số 5 không lấy vì \(5\notin[0,5)\).')),
  MCQ(5, (r'Which of these sets is empty?', r'Tập hợp nào sau đây là tập rỗng?'), [r'\{x\in\mathbb{Z}\mid |x|\le0\}', r'\{x\in\mathbb{R}\mid x^2\ge0\}', r'\{\varnothing\}', r'\{x\in\mathbb{R}\mid x^2\lt0\}'], 'd',
      (r'Answer: d. The square of a real number is never negative. Set (a) is \(\{0\}\), (b) is \(\mathbb{R}\), and (c) has one element.', r'Đáp án d. Bình phương của một số thực không bao giờ âm. Tập ở a bằng \(\{0\}\), tập ở b bằng \(\mathbb{R}\), tập ở c có một phần tử.'))],
 [TF(6, (r'True or false: \(\mathbb{Z}\subset\mathbb{N}\).', r'Đúng hay sai: \(\mathbb{Z}\subset\mathbb{N}\).'), 'false', (r'False. \(-1\) is an integer but not a natural number. The correct statement is \(\mathbb{N}\subset\mathbb{Z}\).', r'Sai. \(-1\) là số nguyên nhưng không phải số tự nhiên. Khẳng định đúng là \(\mathbb{N}\subset\mathbb{Z}\).')),
  TF(7, (r'True or false: the interval \((-\infty,4]\) is written correctly.', r'Đúng hay sai: cách viết \((-\infty,4]\) là đúng.'), 'true', (r'True. \(-\infty\) is not a number, so it has a round bracket. The endpoint 4 is included, so it has a square bracket.', r'Đúng. [[Vô cực]] không phải là số nên dùng ngoặc tròn; đầu mút 4 được lấy nên dùng ngoặc vuông.')),
  TF(8, (r'True or false: if \(A\subset B\), then \(A\cup B=B\).', r'Đúng hay sai: nếu \(A\subset B\) thì \(A\cup B=B\).'), 'true', (r'True. Every element of \(A\) is already in \(B\), so putting the sets together adds nothing new. Example: \(\{1\}\subset\{1,2\}\) gives \(\{1,2\}\).', r'Đúng. Mọi phần tử của \(A\) đã có trong \(B\), nên gộp hai tập không thêm gì mới. Ví dụ \(\{1\}\subset\{1,2\}\): hợp là \(\{1,2\}\).'))],
 [SHORT(9, (r'How many elements does \(\{x\in\mathbb{Z}\mid-4\le x\lt3\}\) have?', r'Tập \(\{x\in\mathbb{Z}\mid-4\le x\lt3\}\) có bao nhiêu phần tử?'), '7', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'),
        (r'Answer: 7. The integers are \(-4,-3,-2,-1,0,1,2\). The number 3 is not included.', r'Đáp số: 7. Các số nguyên là \(-4,-3,-2,-1,0,1,2\); số 3 không được lấy.')),
  SHORT(10, (r'Write \((-\infty,3)\cap[-2,5]\) as one interval.', r'Viết \((-\infty,3)\cap[-2,5]\) thành một khoảng.'), '[-2,3)', 'interval', (r'Write it like (a,b] or [a,b). You can use a comma or a semicolon.', r'Viết dạng (a,b] hoặc [a,b); dùng dấu phẩy hoặc chấm phẩy đều được.'),
        (r'Answer: \([-2,3)\). We need \(x\lt3\) and \(-2\le x\le5\), so \(-2\le x\lt3\).', r'Đáp số: \([-2,3)\). Cần \(x\lt3\) và \(-2\le x\le5\), nên \(-2\le x\lt3\); đầu mút \(-2\) được lấy, đầu mút 3 không lấy.')),
  SHORT(11, (r'In a group of 40 students, 22 like Math, 20 like English and 9 like both. How many students like neither subject?', r'Trong nhóm 40 học sinh, 22 em thích Toán, 20 em thích Tiếng Anh và 9 em thích cả hai. Có bao nhiêu em không thích môn nào?'), '7', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'),
        (r'Answer: 7. \(n(M\cup E)=22+20-9=33\), so \(40-33=7\) students like neither.', r'Đáp số: 7. \(n(M\cup E)=22+20-9=33\), nên \(40-33=7\) em không thích môn nào.'))],
 [MCQ(12, (r'Which instruction means “Tìm hợp của \(A\) và \(B\)”?', r'Câu lệnh nào có nghĩa “Tìm hợp của \(A\) và \(B\)”?'),
      [r'\text{Find the intersection of }A\text{ and }B.', r'\text{Find the difference of }A\text{ and }B.', r'\text{Find the complement of }A.', r'\text{Find the union of }A\text{ and }B.'], 'd',
      (r'Answer: d. Union = hợp; intersection = giao; difference = hiệu; complement = phần bù.', r'Đáp án d. union = hợp; intersection = giao; difference = hiệu; complement = phần bù.')),
  MCQ(13, (r'How do we read \(A\subset B\) in English?', r'Ký hiệu \(A\subset B\) đọc bằng tiếng Anh như thế nào?'),
      [r'\text{A is a subset of B}', r'\text{A belongs to B}', r'\text{A contains B}', r'\text{A equals B}'], 'a',
      (r'Answer: a. “A is a subset of B”: every element of A is in B.', r'Đáp án a. “A is a subset of B” (A là tập con của B): mọi phần tử của A đều thuộc B.'))],
 [T(r'Let \(A=[-2,3)\) and \(B=(1,6)\). (a) Find \(A\cap B\), \(A\cup B\) and \(A\setminus B\). (b) Is \(3\) an element of \(A\cap B\)? Explain in simple English.', r'Cho \(A=[-2,3)\) và \(B=(1,6)\). (a) Tìm \(A\cap B\), \(A\cup B\), \(A\setminus B\). (b) \(3\) có thuộc \(A\cap B\) không? Giải thích bằng tiếng Anh đơn giản.') +
  REVEAL(T(r'(a) \(A\cap B=(1,3)\); \(A\cup B=[-2,6)\); \(A\setminus B=[-2,1]\). The sets overlap on \((1,3)\). The union starts at \(-2\) (included in \(A\)) and ends at 6 (not included in \(B\)). For the difference, we keep the numbers of \(A\) that are not in \(B\), so \(x\le1\); 1 is kept because \(1\notin B\).', r'(a) \(A\cap B=(1,3)\); \(A\cup B=[-2,6)\); \(A\setminus B=[-2,1]\). Hai tập chồng nhau trên \((1,3)\). Hợp bắt đầu từ \(-2\) (lấy, vì thuộc \(A\)) và kết thúc ở 6 (không lấy, vì \(B\) mở). Với hiệu, giữ các số của \(A\) không thuộc \(B\), tức \(x\le1\); số 1 được giữ vì \(1\notin B\).') +
         T(r'(b) No. The number 3 is not in \(A\) because \(A\) has a round bracket at 3. So 3 is not in \(A\cap B\).', r'(b) Không. Số 3 không thuộc \(A\) (ngoặc tròn ở 3) nên không thuộc \(A\cap B\). Câu trả lời tiếng Anh mẫu: “No. 3 is not in A because A has a round bracket at 3.”')),
  T(r'In 2–3 simple English sentences, explain why \([2,5]\) and \((2,5)\) are different sets.', r'Viết 2–3 câu tiếng Anh đơn giản để giải thích vì sao \([2,5]\) và \((2,5)\) là hai tập khác nhau.') +
  REVEAL(T(r'Sample answer: “The interval \([2,5]\) includes 2 and 5, because square brackets mean the endpoints are included. The interval \((2,5)\) does not include them. For example, 5 is in \([2,5]\) but not in \((2,5)\).”', r'Câu trả lời mẫu (giữ bằng tiếng Anh). Hãy so sánh: bài của bạn đã nêu được “đầu mút có/không thuộc tập hợp” và một ví dụ cụ thể chưa?'))]]
S3 = [
 [MCQ(1, (r'Which statement is written correctly?', r'Khẳng định nào được viết đúng?'), [r'\{1,4\}\in\{1,2,4\}', r'\{1,4\}\subset\{1,2,4\}', r'3\in\{1,2,4\}', r'\{1,4\}\subset\{1,2,3\}'], 'b',
      (r'Answer: b. Every element of \(\{1,4\}\) is in \(\{1,2,4\}\). In (a), \(\{1,4\}\) is a set, so we use \(\subset\), not \(\in\). In (d), 4 is not in \(\{1,2,3\}\).', r'Đáp án b. Mọi phần tử của \(\{1,4\}\) đều thuộc \(\{1,2,4\}\). Ở câu a, \(\{1,4\}\) là tập hợp nên dùng \(\subset\) chứ không dùng \(\in\). Ở câu d, 4 không thuộc \(\{1,2,3\}\).')),
  MCQ(2, (r'Which set-builder notation describes the interval \((-4,1]\)?', r'Cách viết nào mô tả nửa khoảng \((-4,1]\) bằng tính chất đặc trưng?'), [r'\{x\in\mathbb{R}\mid-4\le x\le1\}', r'\{x\in\mathbb{R}\mid-4\lt x\lt1\}', r'\{x\in\mathbb{R}\mid-4\le x\lt1\}', r'\{x\in\mathbb{R}\mid-4\lt x\le1\}'], 'd',
      (r'Answer: d. The round bracket at \(-4\) means not included (\(\lt\)). The square bracket at 1 means included (\(\le\)).', r'Đáp án d. Ngoặc tròn ở \(-4\): không lấy (\(\lt\)). Ngoặc vuông ở 1: lấy (\(\le\)).')),
  MCQ(3, (r'Let \(A=\{1,2,3,4\}\) and \(B=\{3,4,5\}\). What is \(A\setminus B\)?', r'Cho \(A=\{1,2,3,4\}\), \(B=\{3,4,5\}\). Tìm \(A\setminus B\).'), [r'\{1,2\}', r'\{5\}', r'\{3,4\}', r'\{1,2,5\}'], 'a',
      (r'Answer: a. The difference keeps the elements of \(A\) that are not in \(B\): 1 and 2. (c) is the intersection.', r'Đáp án a. [[Hiệu]] giữ các phần tử của \(A\) không thuộc \(B\): 1 và 2. Đáp án c là [[giao]].')),
  MCQ(4, (r'What is \((-3,2]\cap[0,7]\)?', r'Tìm \((-3,2]\cap[0,7]\).'), [r'[0,2]', r'(0,2]', r'[0,2)', r'(-3,7]'], 'a',
      (r'Answer: a. We need \(-3\lt x\le2\) and \(0\le x\le7\), so \(0\le x\le2\). 0 is included since it is in both sets; 2 is included since it is in both sets.', r'Đáp án a. Cần \(-3\lt x\le2\) và \(0\le x\le7\), nên \(0\le x\le2\). Số 0 lấy vì thuộc cả hai tập; số 2 lấy vì thuộc cả hai tập.')),
  MCQ(5, (r'Which set has no elements?', r'Tập hợp nào không có phần tử nào?'), [r'\{x\in\mathbb{Z}\mid x^2=1\}', r'\{x\in\mathbb{R}\mid x^2=4\}', r'\{x\in\mathbb{N}\mid x\lt0\}', r'\{x\in\mathbb{Z}\mid |x|\lt1\}'], 'c',
      (r'Answer: c. Every natural number is at least 0, so none is less than 0. Set (a) is \(\{-1,1\}\), (b) is \(\{-2,2\}\), and (d) is \(\{0\}\).', r'Đáp án c. Mọi số tự nhiên đều không nhỏ hơn 0 nên không có số nào nhỏ hơn 0. Tập ở a bằng \(\{-1,1\}\), tập ở b bằng \(\{-2,2\}\), tập ở d bằng \(\{0\}\).'))],
 [TF(6, (r'True or false: \(\mathbb{Z}\subset\mathbb{Q}\).', r'Đúng hay sai: \(\mathbb{Z}\subset\mathbb{Q}\).'), 'true', (r'True. Every integer is a rational number: \(3=\dfrac{3}{1}\).', r'Đúng. Mọi số nguyên đều là số hữu tỉ: \(3=\dfrac{3}{1}\).')),
  TF(7, (r'True or false: the interval \([-3,+\infty]\) is written correctly.', r'Đúng hay sai: cách viết \([-3,+\infty]\) là đúng.'), 'false', (r'False. \(+\infty\) is not a number, so it needs a round bracket: \([-3,+\infty)\).', r'Sai. [[Vô cực]] không phải là số nên luôn dùng ngoặc tròn: \([-3,+\infty)\).')),
  TF(8, (r'True or false: if \(A\subset B\), then \(A\setminus B=\varnothing\).', r'Đúng hay sai: nếu \(A\subset B\) thì \(A\setminus B=\varnothing\).'), 'true', (r'True. Every element of \(A\) is in \(B\), so no element of \(A\) is left after we remove the elements of \(B\). Example: \(\{1\}\setminus\{1,2\}=\varnothing\).', r'Đúng. Mọi phần tử của \(A\) đều thuộc \(B\), nên bỏ các phần tử của \(B\) đi thì không còn phần tử nào của \(A\). Ví dụ \(\{1\}\setminus\{1,2\}=\varnothing\).'))],
 [SHORT(9, (r'How many elements does \(\{x\in\mathbb{Z}\mid-5\le x\lt1\}\) have?', r'Tập \(\{x\in\mathbb{Z}\mid-5\le x\lt1\}\) có bao nhiêu phần tử?'), '6', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'),
        (r'Answer: 6. The integers are \(-5,-4,-3,-2,-1,0\). The number 1 is not included.', r'Đáp số: 6. Các số nguyên là \(-5,-4,-3,-2,-1,0\); số 1 không được lấy.')),
  SHORT(10, (r'Write \((-\infty,5]\cap[2,9)\) as one interval.', r'Viết \((-\infty,5]\cap[2,9)\) thành một khoảng.'), '[2,5]', 'interval', (r'Write it like (a,b] or [a,b). You can use a comma or a semicolon.', r'Viết dạng (a,b] hoặc [a,b); dùng dấu phẩy hoặc chấm phẩy đều được.'),
        (r'Answer: \([2,5]\). We need \(x\le5\) and \(2\le x\lt9\), so \(2\le x\le5\).', r'Đáp số: \([2,5]\). Cần \(x\le5\) và \(2\le x\lt9\), nên \(2\le x\le5\); cả hai đầu mút đều được lấy.')),
  SHORT(11, (r'In a group of 50 students, 28 play football, 25 play volleyball and 12 play both. How many students play neither sport?', r'Trong nhóm 50 học sinh, 28 em chơi bóng đá, 25 em chơi bóng chuyền và 12 em chơi cả hai. Có bao nhiêu em không chơi môn nào?'), '9', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'),
        (r'Answer: 9. \(n(F\cup V)=28+25-12=41\), so \(50-41=9\) students play neither sport.', r'Đáp số: 9. \(n(F\cup V)=28+25-12=41\), nên \(50-41=9\) em không chơi môn nào.'))],
 [MCQ(12, (r'Which instruction means “Tìm hiệu \(A\setminus B\)”?', r'Câu lệnh nào có nghĩa “Tìm hiệu \(A\setminus B\)”?'),
      [r'\text{Find the union of }A\text{ and }B.', r'\text{Find the intersection of }A\text{ and }B.', r'\text{Find the difference }A\setminus B.', r'\text{Find the complement of }A.'], 'c',
      (r'Answer: c. Difference = hiệu; union = hợp; intersection = giao; complement = phần bù.', r'Đáp án c. difference = hiệu; union = hợp; intersection = giao; complement = phần bù.')),
  MCQ(13, (r'How do we read \(x\notin A\) in English?', r'Ký hiệu \(x\notin A\) đọc bằng tiếng Anh như thế nào?'),
      [r'\text{x contains A}', r'\text{x does not belong to A}', r'\text{x is a subset of A}', r'\text{x is not equal to A}'], 'b',
      (r'Answer: b. “x does not belong to A” or “x is not an element of A”.', r'Đáp án b. “x does not belong to A” hoặc “x is not an element of A” (x không thuộc A).'))],
 [T(r'Let \(A=[-5,0)\) and \(B=(-2,3]\). (a) Find \(A\cap B\), \(A\cup B\) and \(A\setminus B\). (b) Is \(0\) an element of \(A\cap B\)? Explain in simple English.', r'Cho \(A=[-5,0)\) và \(B=(-2,3]\). (a) Tìm \(A\cap B\), \(A\cup B\), \(A\setminus B\). (b) \(0\) có thuộc \(A\cap B\) không? Giải thích bằng tiếng Anh đơn giản.') +
  REVEAL(T(r'(a) \(A\cap B=(-2,0)\); \(A\cup B=[-5,3]\); \(A\setminus B=[-5,-2]\). The sets overlap on \((-2,0)\). The union starts at \(-5\) (included in \(A\)) and ends at 3 (included in \(B\)); there is no gap because \(0\in B\). For the difference, we keep the numbers of \(A\) that are not in \(B\), so \(x\le-2\); \(-2\) is kept because \(-2\in A\) and \(-2\notin B\).', r'(a) \(A\cap B=(-2,0)\); \(A\cup B=[-5,3]\); \(A\setminus B=[-5,-2]\). Hai tập chồng nhau trên \((-2,0)\). Hợp bắt đầu từ \(-5\) (lấy, vì thuộc \(A\)) và kết thúc ở 3 (lấy, vì thuộc \(B\)); không bị hở vì \(0\in B\). Với hiệu, giữ các số của \(A\) không thuộc \(B\), tức \(x\le-2\); số \(-2\) được giữ vì \(-2\in A\) và \(-2\notin B\).') +
         T(r'(b) No. The number 0 is not in \(A\) because \(A\) has a round bracket at 0. So 0 is not in \(A\cap B\).', r'(b) Không. Số 0 không thuộc \(A\) (ngoặc tròn ở 0) nên không thuộc \(A\cap B\). Câu trả lời tiếng Anh mẫu: “No. 0 is not in A because A has a round bracket at 0.”')),
  T(r'In 2–3 simple English sentences, explain why \([1,4)\) and \([1,4]\) are different sets.', r'Viết 2–3 câu tiếng Anh đơn giản để giải thích vì sao \([1,4)\) và \([1,4]\) là hai tập khác nhau.') +
  REVEAL(T(r'Sample answer: “The interval \([1,4]\) includes 4, but the interval \([1,4)\) does not include 4. Both include 1. So the number 4 is in the first set and not in the second set.”', r'Câu trả lời mẫu (giữ bằng tiếng Anh). Hãy so sánh: bài của bạn đã nêu được “đầu mút nào có/không thuộc tập hợp” và một ví dụ cụ thể chưa?'))]]
pr = LEVEL_PRACTICE(_T, {1: S1, 2: S2, 3: S3})

mistakes = [
 (r'<b>Wrong symbol.</b> Writing \(\{2\}\in\{1,2,3\}\) or thinking \(\varnothing=\{0\}\). Correct: \(2\in\{1,2,3\}\) or \(\{2\}\subset\{1,2,3\}\); \(\varnothing\) has no element, \(\{0\}\) has one.', r'<b>Sai ký hiệu.</b> Viết \(\{2\}\in\{1,2,3\}\) hoặc nghĩ \(\varnothing=\{0\}\). Đúng: \(2\in\{1,2,3\}\) hoặc \(\{2\}\subset\{1,2,3\}\); \(\varnothing\) không có phần tử, \(\{0\}\) có một phần tử.'),
 (r'<b>Counting.</b> Using \(n(A\cup B)=n(A)+n(B)\) without subtracting the common part; mixing up \(A\setminus B\) and \(B\setminus A\). Correct: \(n(A\cup B)=n(A)+n(B)-n(A\cap B)\).', r'<b>Đếm sai.</b> Tính \(n(A\cup B)=n(A)+n(B)\) mà không trừ phần chung; nhầm \(A\setminus B\) với \(B\setminus A\). Đúng: \(n(A\cup B)=n(A)+n(B)-n(A\cap B)\).'),
 (r'<b>English terms.</b> Confusing union and intersection; thinking “or” means “only one of them”. In Math, “or” includes “both”.', r'<b>Thuật ngữ tiếng Anh.</b> Nhầm [[hợp]] với [[giao]]; nghĩ “or” nghĩa là “chỉ một trong hai”. Trong Toán, “or” gồm cả trường hợp “cả hai”.'),
 (r'<b>Reading the question.</b> Answering “football” when the question asks “football only”; ignoring “in \(\mathbb{R}\)” or “in \(\mathbb{N}\)”. “Only” means difference.', r'<b>Đọc đề.</b> Trả lời “bóng đá” khi đề hỏi “chỉ bóng đá” (football only); bỏ qua “trong \(\mathbb{R}\)” hoặc “trong \(\mathbb{N}\)”. “Only” nghĩa là hiệu.'),
 (r'<b>Writing solutions.</b> \([2,+\infty]\); \((3,1)\); no final answer. Correct: \([2,+\infty)\); \((1,3)\); write the final answer in the form the question asks for.', r'<b>Trình bày.</b> \([2,+\infty]\); \((3,1)\); không viết kết luận. Đúng: \([2,+\infty)\); \((1,3)\); viết kết luận đúng dạng đề yêu cầu.')]

summary = [
 (r'A <b>set</b> is a collection of different elements; \(\mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}\).', r'[[Tập hợp]] là nhóm các [[phần tử]] khác nhau; \(\mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}\).'),
 (r'\(A\subset B\) if every element of \(A\) is in \(B\); \(\varnothing\subset A\) for every \(A\).', r'\(A\subset B\) nếu mọi phần tử của \(A\) thuộc \(B\); \(\varnothing\subset A\) với mọi \(A\).'),
 (r'\(A\cap B\): in both. \(A\cup B\): in at least one. \(A\setminus B\): in \(A\), not in \(B\). \(C_EA=E\setminus A\).', r'\(A\cap B\): thuộc cả hai. \(A\cup B\): thuộc ít nhất một. \(A\setminus B\): thuộc \(A\), không thuộc \(B\). \(C_EA=E\setminus A\).'),
 (r'Intervals: \([\ ]\) = included, \((\ )\) = not included; always \((\ )\) next to \(\pm\infty\).', r'[[Khoảng]]: \([\ ]\) = lấy đầu mút, \((\ )\) = không lấy; luôn dùng \((\ )\) với \(\pm\infty\).'),
 (r'\(n(A\cup B)=n(A)+n(B)-n(A\cap B)\).', r'\(n(A\cup B)=n(A)+n(B)-n(A\cap B)\).')]

checks = [
 (r'I can read and write \(\in\), \(\notin\), \(\subset\) correctly.', r'Tôi dùng đúng các ký hiệu \(\in\), \(\notin\), \(\subset\).'),
 (r'I can find \(A\cap B\), \(A\cup B\) and \(A\setminus B\) for finite sets.', r'Tôi tìm được [[giao]], [[hợp]], [[hiệu]] của các tập hữu hạn.'),
 (r'I can write and read intervals, and show them on a number line.', r'Tôi viết, đọc và biểu diễn được các [[khoảng]] trên [[trục số]].'),
 (r'I can find the intersection and union of two intervals.', r'Tôi tìm được giao và hợp của hai khoảng.'),
 (r'I can solve a counting problem with \(n(A\cup B)\).', r'Tôi giải được bài toán đếm bằng công thức \(n(A\cup B)\).'),
 STD_SUMMARY_CHECK_EN()]

build('g10-sets-01', 'Sets and Intervals', 'Tập hợp và khoảng', CAT,
  {'level': ('Beginner', 'Cơ bản'), 'time': ('about 45 minutes', 'khoảng 45 phút'), 'before': ('number types, comparing numbers, simple inequalities (grade 9)', 'các loại số, so sánh số, bất phương trình đơn giản (lớp 9)')},
  goals, vocab, phrases, review, theory, ex, pr, mistakes, summary, checks,
  'lessons/grade10/sets-and-intervals/sets-and-intervals.html',
  ENTRY('g10-sets-01', 'Sets and Intervals', 'Learn set notation, set operations and interval notation in English.', 'Beginner', 45, [], 'lessons/grade10/sets-and-intervals/sets-and-intervals.html', ['sets', 'intervals', 'venn diagram', 'vocabulary'], grade=10, order=10), grade=10)
