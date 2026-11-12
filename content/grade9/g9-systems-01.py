# -*- coding: utf-8 -*-
"""Nội dung bài g9-systems-01 = Toán 9 KNTT, Bài 1: Khái niệm phương trình và hệ hai phương trình bậc nhất hai ẩn – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: Tài liệu hướng dẫn dạy học bằng tiếng Anh – Toán 9 (Bộ GD&ĐT, 2026), Chapter 1 – Lesson 1, tr. 6–7.
Sửa lỗi tài liệu: TLTA ghi (2;0) và (x; (2−x)/3) là nghiệm của x + 3y = 3 – đúng ra là của x + 3y = 2 (đã dùng phương trình đúng ở Ví dụ 3)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9

LID = 'g9-systems-01'
CH = 'Phương trình và hệ hai phương trình bậc nhất hai ẩn'
TOPIC = ('Linear Equations and Systems of Linear Equations in Two Variables', CH)
ensure_vocab([
 ('g9-lin2', 'linear equation in two variables', 'phương trình bậc nhất hai ẩn', CH, 'x + 3y = 2 is a linear equation in two variables.', r'\(ax+by=c\)'),
 ('g9-ordered-pair', 'ordered pair', 'cặp số', CH, 'The ordered pair (2; 0) is a solution of x + 3y = 2.', r'\((x_0;\ y_0)\)'),
 ('g9-gen-sol', 'general solution', 'nghiệm tổng quát', CH, 'The general solution of 2x − y = 1 is (x; 2x − 1).', ''),
 ('g9-coord-plane', 'coordinate plane', 'mặt phẳng tọa độ', CH, 'Graph the solutions on the coordinate plane.', r'\(Oxy\)'),
 ('g9-line', 'line', 'đường thẳng', CH, 'The solutions of a linear equation in two variables form a line.', ''),
 ('g9-geo-rep', 'geometric representation', 'biểu diễn hình học', CH, 'The geometric representation of the solutions is a line.', ''),
 ('g9-sys2', 'system of two linear equations in two variables', 'hệ hai phương trình bậc nhất hai ẩn', CH, 'x + y = 2 and x + 3y = 2 form a system of two linear equations in two variables.', ''),
 ('g9-system', 'system of equations', 'hệ phương trình', CH, 'Solve the system of equations.', ''),
 ('g9-solve-sys', 'solve a system', 'giải hệ phương trình', CH, 'To solve a system means to find all its solutions.', ''),
 ('g9-inf-many', 'infinitely many solutions', 'vô số nghiệm', CH, 'Any linear equation in two variables has infinitely many solutions.', ''),
 ('g9-sol-eq', 'solution of an equation', 'nghiệm của phương trình', CH, '(1; 1) is a solution of the equation 2x − y = 1.', ''),
 ('g9-sol-set', 'solution set', 'tập nghiệm', CH, 'The solution set is represented by a line.', ''),
 ('g9-intersect', 'intersect', 'cắt nhau', CH, 'If two lines intersect at one point, the system has a unique solution.', ''),
 ('g9-coincide', 'coincide', 'trùng nhau', CH, 'If two lines coincide, the system has infinitely many solutions.', ''),
])
load_vocab()

# ---------- kiểm tra số liệu của bài bằng máy ----------
assert all(2 * x - (2 * x - 1) == 1 for x in range(-5, 6))                       # (x; 2x-1) là nghiệm của 2x - y = 1
assert 2 * 1 - (-2) == 4 and 1 + 2 * (-2) == -3 and 2 * 2 - 0 == 4 and 2 + 0 != -3  # Ví dụ 4
assert 3 * 5 + 2 * (-4) == 7                                                      # Ví dụ 4b: m = 5
assert 0 + 2 * 2 == 4 and 4 + 0 == 4                                              # Ví dụ 3: x + 2y = 4 qua (0;2), (4;0)
assert 2 * 15 + 2 * 10 == 50 and 15 - 10 == 5                                     # Ví dụ 5
assert sp_g9.solve2(1, 1, 2, 1, 3, 2) == ('one', 2, 0)                            # hệ minh họa ở mục 5.4

meta = dict(level=('Beginner', 'Cơ bản'), time=('about 45 minutes', '45 phút'),
            before=('linear equations in one variable; the coordinate plane; graph of y = ax + b', 'phương trình bậc nhất một ẩn; mặt phẳng tọa độ; đồ thị hàm số y = ax + b (lớp 8)'))
goals = [
 (r'recognize a linear equation in two variables \(ax+by=c\) and its coefficients;', r'nhận biết [[phương trình bậc nhất hai ẩn]] \(ax+by=c\) và các [[hệ số]] của nó;'),
 (r'check whether an ordered pair is a solution of an equation or of a system;', r'kiểm tra một [[cặp số]] có là nghiệm của phương trình hoặc của hệ phương trình hay không;'),
 (r'write the general solution and draw the line that represents all solutions;', r'viết [[nghiệm tổng quát]] và vẽ [[đường thẳng]] biểu diễn [[tập nghiệm]];'),
 (r'recognize a system of two linear equations in two variables and write one for a real situation.', r'nhận biết [[hệ hai phương trình bậc nhất hai ẩn]] và lập hệ cho một tình huống thực tế.')]
vocab = [
 (r'<b>linear equation in two variables</b> – an equation \(ax+by=c\) where \(a\) and \(b\) are not both 0.', r'[[Phương trình bậc nhất hai ẩn]] – phương trình dạng \(ax+by=c\), trong đó \(a\) và \(b\) không đồng thời bằng 0.'),
 (r'<b>coefficient</b> – the numbers \(a, b, c\) in \(ax+by=c\). Example: \(3x-2y=7\) has \(a=3,\ b=-2,\ c=7\).', r'[[Hệ số]] – các số \(a, b, c\) trong \(ax+by=c\). Ví dụ: \(3x-2y=7\) có \(a=3,\ b=-2,\ c=7\).'),
 (r'<b>ordered pair</b> – two numbers written in order, \((x_0;\ y_0)\).', r'[[Cặp số]] – hai số viết theo thứ tự, \((x_0;\ y_0)\).'),
 (r'<b>solution</b> – an ordered pair that makes the equation true.', r'[[Nghiệm|nghiệm (cặp số)]] – cặp số làm cho phương trình trở thành đẳng thức đúng.'),
 (r'<b>general solution</b> – a formula that describes all solutions, e.g. \((x;\ 2x-1)\).', r'[[Nghiệm tổng quát]] – cách viết mô tả mọi nghiệm, ví dụ \((x;\ 2x-1)\).'),
 (r'<b>coordinate plane</b> – the plane with the axes \(Ox\) and \(Oy\).', r'[[Mặt phẳng tọa độ]] – mặt phẳng có hai trục \(Ox\) và \(Oy\).'),
 (r'<b>system of two linear equations in two variables</b> – two such equations considered together.', r'[[Hệ hai phương trình bậc nhất hai ẩn]] – hai phương trình bậc nhất hai ẩn được xét đồng thời.'),
 (r'<b>infinitely many solutions</b> – more solutions than we can count.', r'[[Vô số nghiệm]] – có nhiều nghiệm đến mức không đếm hết.'),
 (r'<b>intersect / coincide</b> – two lines meet at one point / lie on top of each other.', r'[[Cắt nhau]] / [[trùng nhau]] – hai đường thẳng có một điểm chung / nằm chồng lên nhau.')]
phrases = [
 (r'<b>Identify the coefficients \(a\), \(b\) and \(c\).</b>', r'Xác định các hệ số \(a\), \(b\) và \(c\).'),
 (r'<b>Which of the following equations are linear equations in two variables?</b>', r'Phương trình nào sau đây là phương trình bậc nhất hai ẩn?'),
 (r'<b>Check if the ordered pair is a solution of the equation / system of equations.</b>', r'Kiểm tra cặp số có là nghiệm của phương trình / hệ phương trình không.'),
 (r'<b>Substitute \(x=\dots\), \(y=\dots\) into the equation.</b>', r'Thay \(x=\dots\), \(y=\dots\) vào phương trình.'),
 (r'<b>Write the general solution and graph it on the coordinate plane.</b>', r'Viết nghiệm tổng quát và biểu diễn trên mặt phẳng tọa độ.'),
 (r'<b>Find the value of \(m\) so that …</b>', r'Tìm giá trị của \(m\) để …')]
review = (T(r'<b>Linear equation in one variable.</b> \(ax+b=0\) with \(a\ne0\) has exactly one solution \(x=-\dfrac{b}{a}\). Example: \(2x-6=0\Leftrightarrow x=3\).', r'<b>Phương trình bậc nhất một ẩn.</b> \(ax+b=0\) với \(a\ne0\) có đúng một nghiệm \(x=-\dfrac{b}{a}\). Ví dụ: \(2x-6=0\Leftrightarrow x=3\).') +
          T(r'<b>Graph of \(y=ax+b\).</b> On the coordinate plane it is a straight line. Two points are enough to draw it, for example the points with \(x=0\) and \(y=0\).', r'<b>Đồ thị hàm số \(y=ax+b\).</b> Trên mặt phẳng tọa độ, đồ thị là một đường thẳng. Chỉ cần hai điểm để vẽ, chẳng hạn điểm có \(x=0\) và điểm có \(y=0\).'))

G = lambda cfg, en, vi: GEO(sp_g9.auto_labels(cfg), cap=(en, vi), alt=(en, ''), height=320)
def pt(i, x, y, name=None): return {'type': 'point', 'id': i, 'at': [x, y], 'name': name or i}

theory = '<h3>5.1 %s</h3>' % TI('Linear equations in two variables', 'Phương trình bậc nhất hai ẩn')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'A <b>linear equation in two variables</b> \(x\) and \(y\) is an equation of the form \(ax+by=c\), where \(a, b, c\) are known numbers and \(a, b\) are <b>not both 0</b>.', r'[[Phương trình bậc nhất hai ẩn]] \(x\) và \(y\) là phương trình dạng \(ax+by=c\), trong đó \(a, b, c\) là các số đã biết và \(a, b\) <b>không đồng thời bằng 0</b>.'),
  T(r'If \(ax_0+by_0=c\) is a true equality, the ordered pair \((x_0;\ y_0)\) is called a <b>solution</b> of the equation.', r'Nếu \(ax_0+by_0=c\) là đẳng thức đúng thì [[cặp số]] \((x_0;\ y_0)\) được gọi là một [[nghiệm|nghiệm (cặp số)]] của phương trình.'))
theory += T(r'Examples: \(2x-y=1\) (\(a=2,\ b=-1,\ c=1\)); \(0x+3y=6\) (\(a=0,\ b=3,\ c=6\)) are linear equations in two variables. The equations \(x^2+y=1\), \(xy=2\) and \(0x+0y=5\) are not.', r'Ví dụ: \(2x-y=1\) (\(a=2,\ b=-1,\ c=1\)) và \(0x+3y=6\) (\(a=0,\ b=3,\ c=6\)) là các phương trình bậc nhất hai ẩn. Các phương trình \(x^2+y=1\), \(xy=2\), \(0x+0y=5\) không phải là phương trình bậc nhất hai ẩn.')
theory += '<h3>5.2 %s</h3>' % TI('All solutions form a line', 'Biểu diễn tập nghiệm trên mặt phẳng tọa độ')
theory += BOX('mint', ('Remember', 'Ghi nhớ'),
  T(r'A linear equation in two variables always has <b>infinitely many solutions</b>.', r'Phương trình bậc nhất hai ẩn luôn có [[vô số nghiệm]].'),
  T(r'On the coordinate plane, all its solutions form the line \(ax+by=c\).', r'Trên [[mặt phẳng tọa độ]], [[tập nghiệm]] của nó được biểu diễn bởi [[đường thẳng]] \(ax+by=c\).'),
  UL([T(r'If \(b\ne0\): the line is \(y=-\dfrac{a}{b}x+\dfrac{c}{b}\); the general solution is \(\left(x;\ -\dfrac{a}{b}x+\dfrac{c}{b}\right)\) with \(x\in\mathbb{R}\).', r'Nếu \(b\ne0\): đường thẳng là \(y=-\dfrac{a}{b}x+\dfrac{c}{b}\); [[nghiệm tổng quát]] là \(\left(x;\ -\dfrac{a}{b}x+\dfrac{c}{b}\right)\) với \(x\in\mathbb{R}\).'),
      T(r'If \(a=0,\ b\ne0\): the line \(y=\dfrac{c}{b}\) is parallel to (or on) the \(x\)-axis.', r'Nếu \(a=0,\ b\ne0\): đường thẳng \(y=\dfrac{c}{b}\) song song hoặc trùng với trục hoành.'),
      T(r'If \(a\ne0,\ b=0\): the line \(x=\dfrac{c}{a}\) is parallel to (or on) the \(y\)-axis.', r'Nếu \(a\ne0,\ b=0\): đường thẳng \(x=\dfrac{c}{a}\) song song hoặc trùng với trục tung.')]))
theory += G({'view': [-3, 4, -3, 4], 'axes': True, 'steps': [{'type': 'lineeq', 'a': 2, 'b': -1, 'c': -1}, pt('A', 0, -1), pt('B', 1, 1), pt('C', 2, 3),
             {'type': 'lineeq', 'a': 0, 'b': 1, 'c': -2, 'style': {'strokeColor': '#c2410c'}}]},
            r'The line \(2x-y=1\) (green) passes through \(A(0;-1)\), \(B(1;1)\), \(C(2;3)\): each point is a solution. The line \(0x+y=2\), i.e. \(y=2\) (orange), is parallel to \(Ox\).',
            r'Đường thẳng \(2x-y=1\) (màu xanh) đi qua \(A(0;-1)\), \(B(1;1)\), \(C(2;3)\): mỗi điểm là một nghiệm. Đường thẳng \(0x+y=2\), tức \(y=2\) (màu cam), song song với \(Ox\).')
theory += '<h3>5.3 %s</h3>' % TI('Systems of two linear equations in two variables', 'Hệ hai phương trình bậc nhất hai ẩn')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'A <b>system of two linear equations in two variables</b> has the form \(\begin{cases}ax+by=c\\ a′x+b′y=c′\end{cases}\), where each equation is a linear equation in two variables.', r'[[Hệ hai phương trình bậc nhất hai ẩn]] có dạng \(\begin{cases}ax+by=c\\ a′x+b′y=c′\end{cases}\), trong đó mỗi phương trình là một phương trình bậc nhất hai ẩn.'),
  T(r'A pair \((x_0;\ y_0)\) is a <b>solution of the system</b> if it is a solution of <b>both</b> equations. To <b>solve a system</b> is to find all its solutions.', r'Cặp số \((x_0;\ y_0)\) là [[nghiệm của hệ]] nếu nó là nghiệm của <b>cả hai</b> phương trình. [[Giải hệ phương trình]] là tìm tất cả các nghiệm của hệ.'))
theory += '<h3>5.4 %s</h3>' % TI('Picture of a system', 'Minh họa hình học nghiệm của hệ')
theory += T(r'Each solution of the system is a common point of the two lines. Two lines can <b>intersect</b> (one common point), be <b>parallel</b> (no common point) or <b>coincide</b> (infinitely many common points). You will use this in Lesson 2.', r'Mỗi nghiệm của hệ là một điểm chung của hai đường thẳng. Hai đường thẳng có thể [[cắt nhau]] (một điểm chung), [[song song]] (không có điểm chung) hoặc [[trùng nhau]] (vô số điểm chung). Em sẽ dùng điều này ở Bài 2.')
theory += G({'view': [-2, 5, -2, 3], 'axes': True, 'steps': [{'type': 'lineeq', 'a': 1, 'b': 1, 'c': -2}, {'type': 'lineeq', 'a': 1, 'b': 3, 'c': -2, 'style': {'strokeColor': '#c2410c'}}, pt('M', 2, 0)]},
            r'The lines \(x+y=2\) and \(x+3y=2\) intersect at \(M(2;0)\): the system \(\begin{cases}x+y=2\\ x+3y=2\end{cases}\) has the solution \((2;\ 0)\).',
            r'Hai đường thẳng \(x+y=2\) và \(x+3y=2\) cắt nhau tại \(M(2;0)\): hệ \(\begin{cases}x+y=2\\ x+3y=2\end{cases}\) có nghiệm \((2;\ 0)\).')

examples = EXAMPLE(1, ('Remembering', 'Biết'), ('Recognize the equation', 'Nhận biết phương trình bậc nhất hai ẩn'),
  T(r'Which equations are linear equations in two variables? Give \(a, b, c\). \(\ 2x-3y=5;\ \ 0x+4y=8;\ \ x^2+y=1;\ \ 0x+0y=3\).', r'Phương trình nào là phương trình bậc nhất hai ẩn? Chỉ ra \(a, b, c\). \(\ 2x-3y=5;\ \ 0x+4y=8;\ \ x^2+y=1;\ \ 0x+0y=3\).'),
  ('Compare each equation with \\(ax+by=c\\), where \\(a, b\\) are not both 0.', 'So sánh từng phương trình với dạng \\(ax+by=c\\), \\(a, b\\) không đồng thời bằng 0.'),
  [T(r'\(2x-3y=5\): yes, \(a=2,\ b=-3,\ c=5\).', r'\(2x-3y=5\): có, \(a=2,\ b=-3,\ c=5\).'),
   T(r'\(0x+4y=8\): yes, \(a=0,\ b=4,\ c=8\) (only \(a\) is 0).', r'\(0x+4y=8\): có, \(a=0,\ b=4,\ c=8\) (chỉ \(a\) bằng 0).'),
   T(r'\(x^2+y=1\): no, because of \(x^2\). \(0x+0y=3\): no, because \(a=b=0\).', r'\(x^2+y=1\): không, vì có \(x^2\). \(0x+0y=3\): không, vì \(a=b=0\).')],
  T(r'\(2x-3y=5\) and \(0x+4y=8\).', r'\(2x-3y=5\) và \(0x+4y=8\).'))
examples += EXAMPLE(2, ('Understanding', 'Hiểu'), ('Check a solution, write the general solution', 'Kiểm tra nghiệm, viết nghiệm tổng quát'),
  T(r'a) Which of the pairs \((1;-2)\), \((2;1)\) is a solution of \(2x-y=4\)? b) Write the general solution of \(2x-y=4\).', r'a) Cặp số nào trong hai cặp \((1;-2)\), \((2;1)\) là nghiệm của phương trình \(2x-y=4\)? b) Viết nghiệm tổng quát của phương trình \(2x-y=4\).'),
  ('Substitute each pair. Then express \\(y\\) in terms of \\(x\\).', 'Thay từng cặp số vào phương trình. Sau đó biểu diễn \\(y\\) theo \\(x\\).'),
  [T(r'\((1;-2)\): \(2\cdot1-(-2)=4\). True, so it is a solution.', r'\((1;-2)\): \(2\cdot1-(-2)=4\). Đúng, nên là nghiệm.'),
   T(r'\((2;1)\): \(2\cdot2-1=3\ne4\). It is not a solution.', r'\((2;1)\): \(2\cdot2-1=3\ne4\). Không phải là nghiệm.'),
   T(r'\(2x-y=4\Leftrightarrow y=2x-4\). The general solution is \((x;\ 2x-4)\) with \(x\in\mathbb{R}\).', r'\(2x-y=4\Leftrightarrow y=2x-4\). Nghiệm tổng quát là \((x;\ 2x-4)\) với \(x\in\mathbb{R}\).')],
  T(r'a) \((1;-2)\). b) \((x;\ 2x-4)\), \(x\in\mathbb{R}\).', r'a) \((1;-2)\). b) \((x;\ 2x-4)\), \(x\in\mathbb{R}\).'))
assert 2 * 1 - (-2) == 4 and 2 * 2 - 1 == 3
examples += EXAMPLE(3, ('Understanding', 'Hiểu'), ('Draw all solutions', 'Biểu diễn tập nghiệm'),
  T(r'Write the general solution of \(x+2y=4\) and draw the line that represents its solutions.', r'Viết nghiệm tổng quát của phương trình \(x+2y=4\) và vẽ đường thẳng biểu diễn tập nghiệm.'),
  ('Solve for \\(y\\); find two easy points (with \\(x=0\\) and with \\(y=0\\)).', 'Rút \\(y\\) theo \\(x\\); tìm hai điểm dễ tính (với \\(x=0\\) và với \\(y=0\\)).'),
  [T(r'\(2y=4-x\Rightarrow y=\dfrac{4-x}{2}\). General solution: \(\left(x;\ \dfrac{4-x}{2}\right)\), \(x\in\mathbb{R}\).', r'\(2y=4-x\Rightarrow y=\dfrac{4-x}{2}\). Nghiệm tổng quát: \(\left(x;\ \dfrac{4-x}{2}\right)\), \(x\in\mathbb{R}\).'),
   T(r'\(x=0\Rightarrow y=2\): point \(A(0;2)\). \(y=0\Rightarrow x=4\): point \(B(4;0)\).', r'\(x=0\Rightarrow y=2\): điểm \(A(0;2)\). \(y=0\Rightarrow x=4\): điểm \(B(4;0)\).'),
   G({'view': [-2, 6, -2, 4], 'axes': True, 'steps': [{'type': 'lineeq', 'a': 1, 'b': 2, 'c': -4}, pt('A', 0, 2), pt('B', 4, 0)]},
     r'The line \(x+2y=4\) through \(A(0;2)\) and \(B(4;0)\).', r'Đường thẳng \(x+2y=4\) đi qua \(A(0;2)\) và \(B(4;0)\).')],
  T(r'The solutions are represented by the line \(AB\): \(x+2y=4\).', r'Tập nghiệm được biểu diễn bởi đường thẳng \(AB\): \(x+2y=4\).'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Systems and a parameter', 'Nghiệm của hệ và tham số'),
  T(r'a) Which of \((1;-2)\) and \((2;0)\) is a solution of the system \(\begin{cases}2x-y=4\\ x+2y=-3\end{cases}\)? b) Find \(m\) so that \((3;-4)\) is a solution of \(mx+2y=7\).', r'a) Cặp số nào trong hai cặp \((1;-2)\) và \((2;0)\) là nghiệm của hệ \(\begin{cases}2x-y=4\\ x+2y=-3\end{cases}\)? b) Tìm \(m\) để \((3;-4)\) là nghiệm của phương trình \(mx+2y=7\).'),
  ('A solution of the system must satisfy both equations. For b), substitute and solve for \\(m\\).', 'Nghiệm của hệ phải thỏa mãn cả hai phương trình. Câu b) thay số rồi giải tìm \\(m\\).'),
  [T(r'\((1;-2)\): \(2+2=4\) ✓ and \(1-4=-3\) ✓. So \((1;-2)\) is a solution of the system.', r'\((1;-2)\): \(2+2=4\) ✓ và \(1-4=-3\) ✓. Vậy \((1;-2)\) là nghiệm của hệ.'),
   T(r'\((2;0)\): \(4-0=4\) ✓ but \(2+0=2\ne-3\). It satisfies only the first equation, so it is not a solution of the system.', r'\((2;0)\): \(4-0=4\) ✓ nhưng \(2+0=2\ne-3\). Cặp số chỉ thỏa mãn phương trình thứ nhất nên không là nghiệm của hệ.'),
   T(r'b) \(m\cdot3+2\cdot(-4)=7\Rightarrow 3m=15\Rightarrow m=5\).', r'b) \(m\cdot3+2\cdot(-4)=7\Rightarrow 3m=15\Rightarrow m=5\).')],
  T(r'a) \((1;-2)\). b) \(m=5\).', r'a) \((1;-2)\). b) \(m=5\).'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('A garden', 'Mảnh vườn hình chữ nhật'),
  T(r'A rectangular garden has a perimeter of 50 m. Its length is 5 m longer than its width. Let \(x\) be the length and \(y\) the width (in meters). Write a system for this situation and check that \((15;\ 10)\) is its solution.', r'Một mảnh vườn hình chữ nhật có chu vi 50 m, chiều dài hơn chiều rộng 5 m. Gọi \(x\) là chiều dài, \(y\) là chiều rộng (mét). Lập hệ phương trình mô tả tình huống và kiểm tra \((15;\ 10)\) là nghiệm của hệ.'),
  ('Perimeter of a rectangle = 2 × (length + width).', 'Chu vi hình chữ nhật = 2 × (dài + rộng).'),
  [T(r'Perimeter: \(2x+2y=50\). Length minus width: \(x-y=5\). System: \(\begin{cases}2x+2y=50\\ x-y=5\end{cases}\).', r'Chu vi: \(2x+2y=50\). Chiều dài hơn chiều rộng 5 m: \(x-y=5\). Hệ: \(\begin{cases}2x+2y=50\\ x-y=5\end{cases}\).'),
   T(r'Check \((15;10)\): \(30+20=50\) ✓, \(15-10=5\) ✓.', r'Thử \((15;10)\): \(30+20=50\) ✓, \(15-10=5\) ✓.')],
  T(r'The garden is 15 m long and 10 m wide.', r'Mảnh vườn dài 15 m, rộng 10 m.'))

_SETS = sp_g9.BANK(sp_g9.L1_GROUPS, start=1, seeds=(1101, 1102, 1103))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Forgetting the condition on \(a, b\).</b> \(0x+0y=3\) is not a linear equation in two variables, but \(0x+4y=8\) is (only one coefficient is 0).', r'<b>Quên điều kiện của \(a, b\).</b> \(0x+0y=3\) không phải là phương trình bậc nhất hai ẩn, nhưng \(0x+4y=8\) thì có (chỉ một hệ số bằng 0).'),
 (r'<b>Swapping \(x\) and \(y\).</b> In \((x_0;\ y_0)\) the first number is \(x\). \((1;-2)\) and \((-2;1)\) are different pairs.', r'<b>Đổi chỗ \(x\) và \(y\).</b> Trong \((x_0;\ y_0)\), số thứ nhất là \(x\). \((1;-2)\) và \((-2;1)\) là hai cặp số khác nhau.'),
 (r'<b>Checking only one equation of a system.</b> A solution of the system must satisfy both equations.', r'<b>Chỉ thử một phương trình của hệ.</b> Nghiệm của hệ phải thỏa mãn cả hai phương trình.'),
 (r'<b>Thinking the equation has one solution.</b> A linear equation in two variables has infinitely many solutions.', r'<b>Nghĩ rằng phương trình chỉ có một nghiệm.</b> Phương trình bậc nhất hai ẩn luôn có vô số nghiệm.'),
 (r'<b>Sign errors when substituting negative numbers.</b> Write brackets: \(2\cdot1-(-2)=4\).', r'<b>Sai dấu khi thay số âm.</b> Hãy viết dấu ngoặc: \(2\cdot1-(-2)=4\).')]
summary = [
 (r'Linear equation in two variables: \(ax+by=c\) with \(a, b\) not both 0; it has infinitely many solutions.', r'Phương trình bậc nhất hai ẩn: \(ax+by=c\) với \(a, b\) không đồng thời bằng 0; có vô số nghiệm.'),
 (r'All solutions are represented by the line \(ax+by=c\) on the coordinate plane.', r'Tập nghiệm được biểu diễn bởi đường thẳng \(ax+by=c\) trên mặt phẳng tọa độ.'),
 (r'If \(b\ne0\), the general solution is \(\left(x;\ \dfrac{c-ax}{b}\right)\), \(x\in\mathbb{R}\).', r'Nếu \(b\ne0\), nghiệm tổng quát là \(\left(x;\ \dfrac{c-ax}{b}\right)\), \(x\in\mathbb{R}\).'),
 (r'A solution of a system satisfies both equations: it is a common point of the two lines.', r'Nghiệm của hệ thỏa mãn cả hai phương trình: đó là điểm chung của hai đường thẳng.'),
 (r'Key English: linear equation in two variables, ordered pair, general solution, system of equations.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[phương trình bậc nhất hai ẩn]], [[cặp số]], [[nghiệm tổng quát]], [[hệ phương trình]].')]
checks = [
 (r'I can recognize a linear equation in two variables and name \(a, b, c\).', r'Em nhận biết được phương trình bậc nhất hai ẩn và chỉ ra được \(a, b, c\).'),
 (r'I can check whether a pair is a solution of an equation or a system.', r'Em kiểm tra được một cặp số có là nghiệm của phương trình hoặc hệ phương trình.'),
 (r'I can write the general solution and draw the line of solutions.', r'Em viết được nghiệm tổng quát và vẽ được đường thẳng biểu diễn tập nghiệm.'),
 (r'I can write a system for a simple real situation.', r'Em lập được hệ phương trình cho một tình huống thực tế đơn giản.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Linear Equations and Systems of Linear Equations in Two Variables', title_vi='Khái niệm phương trình và hệ hai phương trình bậc nhất hai ẩn', topic=TOPIC,
       folder='systems-of-equations', file='linear-equations-two-variables', catalog_title_vi='Khái niệm phương trình và hệ hai phương trình bậc nhất hai ẩn',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Linear equations in two variables, their solutions and lines, and systems of two linear equations.', level='Beginner', minutes=45,
       description_vi='Bài 1 – Phương trình bậc nhất hai ẩn, nghiệm và đường thẳng biểu diễn tập nghiệm; hệ hai phương trình bậc nhất hai ẩn.',
       tags_vi=['phương trình bậc nhất hai ẩn', 'nghiệm', 'nghiệm tổng quát', 'hệ phương trình', 'mặt phẳng tọa độ'],
       prerequisites=[], tags=['linear equation', 'two variables', 'system', 'ordered pair'], order=10)
