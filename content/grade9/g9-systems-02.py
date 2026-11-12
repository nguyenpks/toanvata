# -*- coding: utf-8 -*-
"""Nội dung bài g9-systems-02 = Toán 9 KNTT, Bài 2: Giải hệ hai phương trình bậc nhất hai ẩn – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 1 – Lesson 2, tr. 8–9; Part 3 – Substitution Method (tr. 130)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9
from sp_g9 import solve2

LID = 'g9-systems-02'
CH = 'Phương trình và hệ hai phương trình bậc nhất hai ẩn'
TOPIC = ('Linear Equations and Systems of Linear Equations in Two Variables', CH)
ensure_vocab([
 ('g9-subst', 'substitution method', 'phương pháp thế', CH, 'To solve by the substitution method, we express x in terms of y.', ''),
 ('g9-elim', 'elimination method', 'phương pháp cộng đại số', CH, 'Use the elimination method: add the two equations to eliminate y.', ''),
 ('g9-unique', 'unique solution', 'nghiệm duy nhất', CH, 'If two lines intersect at one point, the system has a unique solution.', ''),
 ('g9-eliminate', 'eliminate (a variable)', 'khử ẩn', CH, 'Subtract the equations to eliminate x.', ''),
 ('g9-express', 'express … in terms of …', 'biểu diễn theo', CH, 'Express y in terms of x.', ''),
 ('g9-calculator', 'calculator', 'máy tính cầm tay', CH, 'Check your answer with a calculator.', ''),
 ('g9-opposite', 'opposite numbers', 'hai số đối nhau', CH, 'The coefficients of y are opposite numbers, so add the equations.', ''),
])
load_vocab()

# ---------- kiểm tra số liệu ----------
assert solve2(1, -2, 1, 3, 1, 10) == ('one', 3, 1)            # Ví dụ 1
assert solve2(2, 3, 7, 2, -1, 3) == ('one', 2, 1)             # Ví dụ 2
assert solve2(3, 2, 4, 2, -3, 7) == ('one', 2, -1)            # Ví dụ 3
assert solve2(1, -2, 3, -2, 4, 1) == ('none',) and solve2(1, 1, 2, 2, 2, 4) == ('inf',)   # Ví dụ 4
assert solve2(1, 1, 3, -2, 1, -3) == ('one', 2, 1)            # Ví dụ 5: y = 2x + 1
assert solve2(2, 1, 4, 1, -1, -1) == ('one', 1, 2)            # hình mục 5.3

meta = dict(level=('Beginner', 'Cơ bản'), time=('about 60 minutes', '60 phút'),
            before=('Lesson 1: solutions of a system; solving linear equations in one variable', 'Bài 1: nghiệm của hệ phương trình; giải phương trình bậc nhất một ẩn'))
goals = [
 (r'describe the steps of the substitution method and of the elimination method;', r'nêu được các bước của [[phương pháp thế]] và [[phương pháp cộng đại số]];'),
 (r'solve a system of two linear equations in two variables by either method;', r'giải được [[hệ hai phương trình bậc nhất hai ẩn]] bằng một trong hai phương pháp;'),
 (r'recognize when a system has a unique solution, no solution or infinitely many solutions;', r'nhận biết hệ có [[nghiệm duy nhất]], [[vô nghiệm]] hay có [[vô số nghiệm]];'),
 (r'check the answer with a calculator and use systems to find a line through two points.', r'kiểm tra kết quả bằng [[máy tính cầm tay]] và dùng hệ phương trình để tìm đường thẳng đi qua hai điểm.')]
vocab = [
 (r'<b>substitution method</b> – express one variable from one equation and put it into the other equation.', r'[[Phương pháp thế]] – rút một ẩn từ một phương trình rồi thế vào phương trình còn lại.'),
 (r'<b>elimination method</b> – add or subtract the equations to remove one variable.', r'[[Phương pháp cộng đại số]] – cộng hoặc trừ từng vế hai phương trình để mất đi một ẩn.'),
 (r'<b>eliminate</b> – make a variable disappear.', r'[[Khử ẩn]] – làm cho một ẩn biến mất khỏi phương trình.'),
 (r'<b>express \(x\) in terms of \(y\)</b> – write \(x=\dots\) using \(y\).', r'[[Biểu diễn|biểu diễn theo]] \(x\) theo \(y\) – viết \(x=\dots\) bằng một biểu thức chứa \(y\).'),
 (r'<b>unique solution</b> – exactly one solution.', r'[[Nghiệm duy nhất]] – có đúng một nghiệm.'),
 (r'<b>no solution</b> – no pair satisfies both equations.', r'[[Vô nghiệm]] – không có cặp số nào thỏa mãn cả hai phương trình.'),
 (r'<b>infinitely many solutions</b> – every solution of one equation is a solution of the other.', r'[[Vô số nghiệm]] – mọi nghiệm của phương trình này đều là nghiệm của phương trình kia.'),
 (r'<b>opposite numbers</b> – such as \(3\) and \(-3\).', r'[[Hai số đối nhau]] – chẳng hạn \(3\) và \(-3\).')]
phrases = [
 (r'<b>Solve the system by the substitution method / by the elimination method.</b>', r'Giải hệ bằng phương pháp thế / bằng phương pháp cộng đại số.'),
 (r'<b>From the first equation, we have \(x=\dots\)</b>', r'Từ phương trình thứ nhất ta có \(x=\dots\)'),
 (r'<b>Substitute \(\dots\) into the second equation.</b>', r'Thế \(\dots\) vào phương trình thứ hai.'),
 (r'<b>Add / Subtract the two equations side by side.</b>', r'Cộng / Trừ từng vế hai phương trình.'),
 (r'<b>Multiply both sides of the first equation by 3.</b>', r'Nhân hai vế của phương trình thứ nhất với 3.'),
 (r'<b>The system has a unique solution / no solution / infinitely many solutions.</b>', r'Hệ có nghiệm duy nhất / vô nghiệm / có vô số nghiệm.')]
review = (T(r'<b>Lesson 1.</b> A solution of a system satisfies <b>both</b> equations; it is a common point of the two lines.', r'<b>Bài 1.</b> Nghiệm của hệ thỏa mãn <b>cả hai</b> phương trình; đó là điểm chung của hai đường thẳng.') +
          T(r'<b>Moving a term.</b> When a term moves to the other side, its sign changes: \(x-2y=1\Leftrightarrow x=1+2y\).', r'<b>Chuyển vế.</b> Khi chuyển một hạng tử sang vế kia thì phải đổi dấu: \(x-2y=1\Leftrightarrow x=1+2y\).'))

G = lambda cfg, en, vi: GEO(sp_g9.auto_labels(cfg), cap=(en, vi), alt=(en, ''), height=300)
def pt(i, x, y): return {'type': 'point', 'id': i, 'at': [x, y], 'name': i}

theory = '<h3>5.1 %s</h3>' % TI('The substitution method', 'Phương pháp thế')
theory += BOX('blue', ('Steps', 'Các bước'),
  UL([T(r'<b>Step 1.</b> From one equation, express one variable in terms of the other (for example \(x\) in terms of \(y\)).', r'<b>Bước 1.</b> Từ một phương trình của hệ, biểu diễn một ẩn theo ẩn kia (chẳng hạn \(x\) theo \(y\)).'),
      T(r'<b>Step 2.</b> Substitute it into the other equation. You get an equation in one variable; solve it.', r'<b>Bước 2.</b> Thế vào phương trình còn lại để được phương trình một ẩn; giải phương trình đó.'),
      T(r'<b>Step 3.</b> Find the other variable and write the solution of the system.', r'<b>Bước 3.</b> Tìm ẩn còn lại và kết luận nghiệm của hệ.')]),
  T(r'Tip: choose the equation where a variable has coefficient \(1\) or \(-1\).', r'Mẹo: nên rút ẩn có hệ số bằng \(1\) hoặc \(-1\).'))
theory += '<h3>5.2 %s</h3>' % TI('The elimination method', 'Phương pháp cộng đại số')
theory += BOX('mint', ('Steps', 'Các bước'),
  UL([T(r'<b>Step 1.</b> If needed, multiply both sides of each equation by suitable numbers so that the coefficients of one variable are <b>equal</b> or <b>opposite</b>.', r'<b>Bước 1.</b> Nếu cần, nhân hai vế của mỗi phương trình với một số thích hợp để hệ số của cùng một ẩn <b>bằng nhau</b> hoặc <b>đối nhau</b>.'),
      T(r'<b>Step 2.</b> Subtract the equations (equal coefficients) or add them (opposite coefficients). One variable is eliminated.', r'<b>Bước 2.</b> Trừ từng vế (hệ số bằng nhau) hoặc cộng từng vế (hệ số đối nhau) để [[khử ẩn]], được phương trình một ẩn.'),
      T(r'<b>Step 3.</b> Solve it, find the other variable and write the solution.', r'<b>Bước 3.</b> Giải phương trình một ẩn, tìm ẩn còn lại và kết luận.')]))
theory += '<h3>5.3 %s</h3>' % TI('How many solutions?', 'Số nghiệm của hệ')
theory += T(r'When we solve, we may get an equation of the form \(0x=k\) (or \(0y=k\)):', r'Khi giải, có thể gặp phương trình dạng \(0x=k\) (hoặc \(0y=k\)):')
theory += TABLE([('What we get', 'Kết quả khi giải'), ('Number of solutions', 'Số nghiệm của hệ'), ('The two lines', 'Hai đường thẳng')],
  [[TI('one value of \\(x\\) and \\(y\\)', 'tìm được một giá trị \\(x\\), \\(y\\)'), TI('unique solution', 'nghiệm duy nhất'), TI('intersect', 'cắt nhau')],
   [TI('\\(0x=k\\) with \\(k\\ne0\\)', '\\(0x=k\\) với \\(k\\ne0\\)'), TI('no solution', 'vô nghiệm'), TI('are parallel', 'song song')],
   [TI('\\(0x=0\\)', '\\(0x=0\\)'), TI('infinitely many solutions', 'vô số nghiệm'), TI('coincide', 'trùng nhau')]])
theory += G({'view': [-2, 4, -1, 5], 'axes': True, 'steps': [{'type': 'lineeq', 'a': 2, 'b': 1, 'c': -4}, {'type': 'lineeq', 'a': 1, 'b': -1, 'c': 1, 'style': {'strokeColor': '#c2410c'}}, pt('M', 1, 2)]},
            r'The system \(\begin{cases}2x+y=4\\ x-y=-1\end{cases}\): the two lines intersect at \(M(1;2)\), so the unique solution is \((1;\ 2)\).',
            r'Hệ \(\begin{cases}2x+y=4\\ x-y=-1\end{cases}\): hai đường thẳng cắt nhau tại \(M(1;2)\) nên hệ có nghiệm duy nhất \((1;\ 2)\).')
theory += '<h3>5.4 %s</h3>' % TI('Using a calculator', 'Dùng máy tính cầm tay')
theory += BOX('yellow', ('Calculator', 'Máy tính cầm tay'),
  T(r'Choose the mode for systems of two linear equations in two variables, enter \(a, b, c\) of the first equation and \(a′, b′, c′\) of the second, then press “=” to read \(x\) and \(y\). Use it to <b>check</b> your work, not to skip the method.', r'Chọn chương trình giải hệ hai phương trình bậc nhất hai ẩn, nhập lần lượt \(a, b, c\) của phương trình thứ nhất và \(a′, b′, c′\) của phương trình thứ hai, rồi nhấn “=” để đọc \(x\), \(y\). Dùng [[máy tính cầm tay]] để <b>kiểm tra</b> kết quả, không thay cho cách giải.'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Substitution', 'Phương pháp thế'),
  T(r'Solve the system \(\begin{cases}x-2y=1\\ 3x+y=10\end{cases}\) by the substitution method.', r'Giải hệ \(\begin{cases}x-2y=1\\ 3x+y=10\end{cases}\) bằng phương pháp thế.'),
  ('In the first equation \\(x\\) has coefficient 1, so express \\(x\\) in terms of \\(y\\).', 'Ở phương trình thứ nhất, \\(x\\) có hệ số 1 nên rút \\(x\\) theo \\(y\\).'),
  [T(r'From the first equation: \(x=1+2y\).', r'Từ phương trình thứ nhất: \(x=1+2y\).'),
   T(r'Substitute into the second: \(3(1+2y)+y=10\Rightarrow 7y=7\Rightarrow y=1\).', r'Thế vào phương trình thứ hai: \(3(1+2y)+y=10\Rightarrow 7y=7\Rightarrow y=1\).'),
   T(r'Then \(x=1+2\cdot1=3\). Check: \(3-2=1\) ✓, \(9+1=10\) ✓.', r'Suy ra \(x=1+2\cdot1=3\). Thử lại: \(3-2=1\) ✓, \(9+1=10\) ✓.')],
  T(r'The solution is \((3;\ 1)\).', r'Hệ có nghiệm \((3;\ 1)\).'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Elimination (equal coefficients)', 'Cộng đại số (hệ số bằng nhau)'),
  T(r'Solve \(\begin{cases}2x+3y=7\\ 2x-y=3\end{cases}\).', r'Giải hệ \(\begin{cases}2x+3y=7\\ 2x-y=3\end{cases}\).'),
  ('The coefficients of \\(x\\) are equal (both 2): subtract.', 'Hệ số của \\(x\\) bằng nhau (cùng bằng 2): trừ từng vế.'),
  [T(r'Subtract the equations: \((2x+3y)-(2x-y)=7-3\Rightarrow 4y=4\Rightarrow y=1\).', r'Trừ từng vế: \((2x+3y)-(2x-y)=7-3\Rightarrow 4y=4\Rightarrow y=1\).'),
   T(r'Substitute \(y=1\) into \(2x-y=3\): \(2x=4\Rightarrow x=2\).', r'Thay \(y=1\) vào \(2x-y=3\): \(2x=4\Rightarrow x=2\).')],
  T(r'\((2;\ 1)\).', r'\((2;\ 1)\).'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('Multiply first, then add', 'Nhân rồi cộng đại số'),
  T(r'Solve \(\begin{cases}3x+2y=4\\ 2x-3y=7\end{cases}\).', r'Giải hệ \(\begin{cases}3x+2y=4\\ 2x-3y=7\end{cases}\).'),
  ('No coefficients are equal or opposite yet. Multiply to make the coefficients of \\(y\\) opposite.', 'Chưa có hệ số nào bằng nhau hay đối nhau. Nhân để hệ số của \\(y\\) đối nhau.'),
  [T(r'Multiply the first equation by 3 and the second by 2: \(\begin{cases}9x+6y=12\\ 4x-6y=14\end{cases}\).', r'Nhân hai vế phương trình thứ nhất với 3, phương trình thứ hai với 2: \(\begin{cases}9x+6y=12\\ 4x-6y=14\end{cases}\).'),
   T(r'Add: \(13x=26\Rightarrow x=2\). Then \(3\cdot2+2y=4\Rightarrow y=-1\).', r'Cộng từng vế: \(13x=26\Rightarrow x=2\). Thay vào: \(3\cdot2+2y=4\Rightarrow y=-1\).')],
  T(r'\((2;\ -1)\).', r'\((2;\ -1)\).'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('No solution, infinitely many solutions', 'Hệ vô nghiệm, hệ có vô số nghiệm'),
  T(r'Solve a) \(\begin{cases}x-2y=3\\ -2x+4y=1\end{cases}\); b) \(\begin{cases}x+y=2\\ 2x+2y=4\end{cases}\).', r'Giải các hệ a) \(\begin{cases}x-2y=3\\ -2x+4y=1\end{cases}\); b) \(\begin{cases}x+y=2\\ 2x+2y=4\end{cases}\).'),
  ('Eliminate \\(x\\) and look at what is left.', 'Khử \\(x\\) rồi xem phương trình còn lại.'),
  [T(r'a) Multiply the first equation by 2: \(2x-4y=6\). Add to the second: \(0x+0y=7\), which is never true. <b>No solution</b> (the lines are parallel).', r'a) Nhân phương trình thứ nhất với 2: \(2x-4y=6\). Cộng với phương trình thứ hai: \(0x+0y=7\), vô lí. Hệ <b>vô nghiệm</b> (hai đường thẳng song song).'),
   G({'view': [-2, 5, -3, 2], 'axes': True, 'steps': [{'type': 'lineeq', 'a': 1, 'b': -2, 'c': -3}, {'type': 'lineeq', 'a': -2, 'b': 4, 'c': -1, 'style': {'strokeColor': '#c2410c'}}]},
     r'a) \(x-2y=3\) and \(-2x+4y=1\) are parallel lines.', r'a) Hai đường thẳng \(x-2y=3\) và \(-2x+4y=1\) song song.'),
   T(r'b) Multiply the first equation by 2: \(2x+2y=4\), exactly the second equation. Subtracting gives \(0x+0y=0\): <b>infinitely many solutions</b> \((x;\ 2-x)\), \(x\in\mathbb{R}\) (the lines coincide).', r'b) Nhân phương trình thứ nhất với 2 được \(2x+2y=4\), trùng với phương trình thứ hai. Trừ từng vế được \(0x+0y=0\): hệ có <b>vô số nghiệm</b> \((x;\ 2-x)\), \(x\in\mathbb{R}\) (hai đường thẳng trùng nhau).')],
  T(r'a) No solution. b) Infinitely many solutions \((x;\ 2-x)\).', r'a) Vô nghiệm. b) Vô số nghiệm \((x;\ 2-x)\).'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('A line through two points', 'Đường thẳng đi qua hai điểm'),
  T(r'Find \(a\) and \(b\) so that the line \(y=ax+b\) passes through \(A(1;\ 3)\) and \(B(-2;\ -3)\).', r'Tìm \(a\) và \(b\) để đường thẳng \(y=ax+b\) đi qua hai điểm \(A(1;\ 3)\) và \(B(-2;\ -3)\).'),
  ('A point lies on the line when its coordinates satisfy \\(y=ax+b\\). Two points give a system in \\(a\\) and \\(b\\).', 'Điểm thuộc đường thẳng khi tọa độ thỏa mãn \\(y=ax+b\\). Hai điểm cho một hệ phương trình ẩn \\(a, b\\).'),
  [T(r'\(A\): \(3=a+b\). \(B\): \(-3=-2a+b\). System \(\begin{cases}a+b=3\\ -2a+b=-3\end{cases}\).', r'\(A\): \(3=a+b\). \(B\): \(-3=-2a+b\). Ta có hệ \(\begin{cases}a+b=3\\ -2a+b=-3\end{cases}\).'),
   T(r'Subtract: \(3a=6\Rightarrow a=2\), then \(b=1\).', r'Trừ từng vế: \(3a=6\Rightarrow a=2\), suy ra \(b=1\).')],
  T(r'\(y=2x+1\).', r'\(y=2x+1\).'))

_SETS = sp_g9.BANK(sp_g9.L2_GROUPS, start=1, seeds=(1201, 1202, 1203))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Forgetting to change the sign when moving a term.</b> \(x-2y=1\Rightarrow x=1+2y\), not \(x=1-2y\).', r'<b>Quên đổi dấu khi chuyển vế.</b> \(x-2y=1\Rightarrow x=1+2y\), không phải \(x=1-2y\).'),
 (r'<b>Multiplying only one side.</b> Multiply <b>both</b> sides of the equation by the same number.', r'<b>Chỉ nhân một vế.</b> Phải nhân <b>cả hai vế</b> của phương trình với cùng một số.'),
 (r'<b>Adding when the coefficients are equal.</b> Equal coefficients → subtract; opposite coefficients → add.', r'<b>Cộng khi hệ số bằng nhau.</b> Hệ số bằng nhau thì trừ; hệ số đối nhau thì cộng.'),
 (r'<b>Stopping after finding one variable.</b> The solution of a system is a pair \((x;\ y)\).', r'<b>Tìm được một ẩn rồi dừng.</b> Nghiệm của hệ là một cặp số \((x;\ y)\).'),
 (r'<b>Reading \(0x=0\) as “no solution”.</b> \(0x=0\) is always true: infinitely many solutions.', r'<b>Hiểu \(0x=0\) là vô nghiệm.</b> \(0x=0\) luôn đúng nên hệ có vô số nghiệm.')]
summary = [
 (r'Substitution: express one variable, substitute, solve, then find the other variable.', r'Phương pháp thế: rút một ẩn, thế vào phương trình kia, giải rồi tìm ẩn còn lại.'),
 (r'Elimination: make the coefficients of one variable equal or opposite, then subtract or add.', r'Phương pháp cộng đại số: làm cho hệ số của một ẩn bằng nhau hoặc đối nhau rồi trừ hoặc cộng từng vế.'),
 (r'\(0x=k\ (k\ne0)\): no solution (parallel lines). \(0x=0\): infinitely many solutions (coinciding lines).', r'\(0x=k\ (k\ne0)\): hệ vô nghiệm (hai đường thẳng song song). \(0x=0\): hệ có vô số nghiệm (hai đường thẳng trùng nhau).'),
 (r'Always check the solution in both equations (or with a calculator).', r'Luôn thử lại nghiệm vào cả hai phương trình (hoặc bằng máy tính cầm tay).'),
 (r'Key English: substitution method, elimination method, unique solution, no solution.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[phương pháp thế]], [[phương pháp cộng đại số]], [[nghiệm duy nhất]], [[vô nghiệm]].')]
checks = [
 (r'I can solve a system by the substitution method.', r'Em giải được hệ bằng phương pháp thế.'),
 (r'I can solve a system by the elimination method.', r'Em giải được hệ bằng phương pháp cộng đại số.'),
 (r'I can tell when a system has no solution or infinitely many solutions.', r'Em nhận biết được khi nào hệ vô nghiệm hoặc có vô số nghiệm.'),
 (r'I can find the line \(y=ax+b\) through two given points.', r'Em tìm được đường thẳng \(y=ax+b\) đi qua hai điểm cho trước.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Solving Systems of Linear Equations in Two Variables', title_vi='Giải hệ hai phương trình bậc nhất hai ẩn', topic=TOPIC,
       folder='systems-of-equations', file='solving-systems', catalog_title_vi='Giải hệ hai phương trình bậc nhất hai ẩn',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='The substitution and elimination methods, the number of solutions of a system, and using a calculator.', level='Beginner', minutes=60,
       description_vi='Bài 2 – Giải hệ bằng phương pháp thế, phương pháp cộng đại số; hệ vô nghiệm, vô số nghiệm; dùng máy tính cầm tay.',
       tags_vi=['phương pháp thế', 'phương pháp cộng đại số', 'hệ phương trình', 'số nghiệm'],
       prerequisites=['g9-systems-01'], tags=['substitution', 'elimination', 'system'], order=20)
