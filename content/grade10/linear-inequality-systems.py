# -*- coding: utf-8 -*-
"""g10-ineq-sys-01 = Toán 10 KNTT, Bài 4: Hệ bất phương trình bậc nhất hai ẩn. Mã ngân hàng câu hỏi: TOAN10-C2-B04."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g10b

CV = 'Hệ bất phương trình bậc nhất hai ẩn'
vocab = defs(CV, [
 ('sys', 'system of inequalities', 'hệ bất phương trình bậc nhất hai ẩn', 'several linear inequalities in \\(x,y\\) that must all be true.', 'gồm hai hay nhiều bất phương trình bậc nhất hai ẩn phải cùng đúng.', 'The system has three inequalities.', ''),
 ('sysol', 'solution of a system', 'nghiệm của hệ', 'a pair \\((x_0;y_0)\\) that satisfies every inequality.', 'cặp số \\((x_0;y_0)\\) thỏa mãn mọi bất phương trình của hệ.', '(1; 1) is a solution of the system.', ''),
 ('vertex', 'vertex of the region', 'đỉnh của miền nghiệm', 'a corner point where two boundary lines meet.', 'giao điểm của hai đường biên, là “góc” của miền.', 'Find the vertices of the region.', ''),
 ('objective', 'objective function', 'biểu thức mục tiêu', 'the expression \\(F=px+qy\\) we want to make largest or smallest.', 'biểu thức \\(F=px+qy\\) cần tìm giá trị lớn nhất hoặc nhỏ nhất.', 'Maximise the objective function.', ''),
 ('maxim', 'maximum / minimum', 'giá trị lớn nhất / nhỏ nhất', 'the greatest / the least value.', 'giá trị lớn nhất / nhỏ nhất.', 'Find the maximum value of F.', ''),
 ('bounded', 'bounded region', 'miền bị chặn', 'a region that fits inside a big circle (a polygon).', 'miền nằm gọn trong một hình tròn đủ lớn (một đa giác).', 'The region is bounded.', '')])
goals = [('recognise a system of linear inequalities and check a solution;', 'nhận biết [[hệ bất phương trình bậc nhất hai ẩn]] và kiểm tra [[nghiệm của hệ]];'),
 ('draw the solution region of a system and find its vertices;', 'biểu diễn miền nghiệm của hệ bằng đồ thị và tìm các [[đỉnh của miền nghiệm]];'),
 ('find the largest or smallest value of \\(F=px+qy\\) on a region;', 'tìm [[giá trị lớn nhất / nhỏ nhất]] của [[biểu thức mục tiêu]] \\(F=px+qy\\) trên một miền;'),
 ('solve a simple optimisation word problem.', 'giải bài toán tối ưu thực tế đơn giản.')]
phrases = [('<b>Find the solution region.</b>', 'Tìm miền nghiệm.'), ('<b>Find the maximum value of \\(F\\).</b>', 'Tìm giá trị lớn nhất của \\(F\\).'), ('<b>at most / at least</b>', 'nhiều nhất (≤) / ít nhất (≥)'), ('<b>subject to</b> (constraints)', 'với các ràng buộc')]
review = T('Recall Lesson 3: the solution region of one inequality is a half-plane; its boundary is solid for \\(\\le,\\ge\\) and dashed for \\(\\lt,\\gt\\). Test the origin to choose the side.', 'Nhắc lại Bài 3: miền nghiệm của một bất phương trình là nửa mặt phẳng; đường biên nét liền với \\(\\le,\\ge\\), nét đứt với \\(\\lt,\\gt\\). Thử gốc tọa độ để chọn phía.')
SYS = '\\begin{cases}x\\ge0,\\ y\\ge0\\\\ x+y\\le4\\\\ 2x+y\\le6\\end{cases}'
theory = '<h3>5.1 %s</h3>' % TI('Systems of inequalities', 'Hệ bất phương trình bậc nhất hai ẩn')
theory += BOX('blue', ('Definition', 'Định nghĩa'), T('A <b>system of inequalities</b> in \\(x,y\\) has two or more linear inequalities. A <b>solution</b> is a pair \\((x_0;y_0)\\) that makes <b>all</b> of them true.', '[[Hệ bất phương trình bậc nhất hai ẩn]] gồm hai hay nhiều bất phương trình bậc nhất hai ẩn. [[Nghiệm của hệ]] là cặp \\((x_0;y_0)\\) thỏa mãn <b>tất cả</b> các bất phương trình.'),
  T('The set of all solutions, drawn on the plane, is the <b>solution region</b> of the system: the part shared by all the half-planes.', 'Tập hợp mọi nghiệm biểu diễn trên mặt phẳng là miền nghiệm của hệ: phần chung của tất cả các nửa mặt phẳng.'))
theory += '<h3>5.2 %s</h3>' % TI('Drawing the solution region', 'Biểu diễn miền nghiệm')
theory += BOX('mint', ('Method', 'Cách làm'), UL([T('Draw the boundary line of each inequality.', 'Vẽ đường biên của từng bất phương trình.'), T('Use a test point (often \\((0;0)\\)) to find the correct side of each line.', 'Dùng điểm kiểm tra (thường là \\((0;0)\\)) để chọn phía của từng đường.'), T('Keep the part that is on the correct side of <b>all</b> lines.', 'Giữ phần nằm đúng phía của <b>mọi</b> đường.'), T('Find the vertices: solve two boundary equations, then check the other inequalities.', 'Tìm các đỉnh: giải hệ hai phương trình biên, rồi kiểm tra các bất phương trình còn lại.')]))
theory += GE(region((-1, 5, -1, 5), [(-1, 0, 0), (0, -1, 0), (1, 1, 4), (2, 1, 6)]), 'Region of the system \\(x\\ge0,\\ y\\ge0,\\ x+y\\le4,\\ 2x+y\\le6\\): the quadrilateral \\(OABC\\).', 'Miền nghiệm của hệ \\(x\\ge0,\\ y\\ge0,\\ x+y\\le4,\\ 2x+y\\le6\\): tứ giác \\(OABC\\).')
theory += '<h3>5.3 %s</h3>' % TI('Largest and smallest values', 'Giá trị lớn nhất, nhỏ nhất của biểu thức \\(F=px+qy\\)')
theory += BOX('blue', ('Key fact', 'Kết quả quan trọng'), T('If the solution region is a polygon, \\(F=px+qy\\) reaches its largest and smallest values at <b>vertices</b> of the polygon.', 'Nếu miền nghiệm là một đa giác thì \\(F=px+qy\\) đạt giá trị lớn nhất và nhỏ nhất tại các <b>đỉnh</b> của đa giác.'),
  T('So: find all vertices, compute \\(F\\) at each, and compare.', 'Vì vậy: tìm mọi đỉnh, tính \\(F\\) tại từng đỉnh rồi so sánh.'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('If the region is not bounded, a largest (or smallest) value may not exist. Check that the region is a polygon first.', 'Nếu miền không bị chặn thì có thể không tồn tại giá trị lớn nhất (hoặc nhỏ nhất). Hãy kiểm tra miền có phải đa giác trước.'))
theory += '<h3>5.4 %s</h3>' % TI('Optimisation problems', 'Bài toán tối ưu thực tế')
theory += BOX('mint', ('Steps', 'Các bước'), UL([T('Name the variables and write the constraints as a system.', 'Đặt ẩn và viết các ràng buộc thành hệ bất phương trình.'), T('Write the quantity to optimise as \\(F=px+qy\\).', 'Viết đại lượng cần tối ưu dạng \\(F=px+qy\\).'), T('Find the vertices and compute \\(F\\) at each.', 'Tìm các đỉnh và tính \\(F\\) tại mỗi đỉnh.'), T('Answer the question in words (and check that \\(x,y\\) are whole numbers if needed).', 'Trả lời bằng lời (và kiểm tra \\(x,y\\) nguyên nếu đề yêu cầu).')]))
V = vertices([(-1, 0, 0), (0, -1, 0), (1, 1, 4), (2, 1, 6)]); assert [(int(x), int(y)) for x, y in V] == [(0, 0), (0, 4), (2, 2), (3, 0)]
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Is it a solution of the system?', 'Có là nghiệm của hệ không?'),
  T('Which pairs are solutions of \\(%s\\)? (a) \\((1;2)\\) (b) \\((3;1)\\) (c) \\((2;2)\\).' % SYS, 'Cặp nào là nghiệm của hệ \\(%s\\)? (a) \\((1;2)\\) (b) \\((3;1)\\) (c) \\((2;2)\\).' % SYS),
  ('Substitute into every inequality.', 'Thay vào từng bất phương trình.'),
  [T('(a) \\(1+2=3\\le4\\) and \\(2+2=4\\le6\\): true.', '(a) \\(1+2=3\\le4\\) và \\(2+2=4\\le6\\): đúng.'), T('(b) \\(2\\cdot3+1=7\\le6\\) is false.', '(b) \\(2\\cdot3+1=7\\le6\\) sai.'), T('(c) \\(2+2=4\\le4\\) and \\(4+2=6\\le6\\): true.', '(c) \\(2+2=4\\le4\\) và \\(4+2=6\\le6\\): đúng.')], T('(a) and (c) are solutions.', '(a) và (c) là nghiệm.'))
assert 1 + 2 <= 4 and 2 + 2 <= 6 and not 2 * 3 + 1 <= 6 and 2 + 2 <= 4 and 4 + 2 <= 6
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Draw the region of a system', 'Biểu diễn miền nghiệm'),
  T('Draw the solution region of \\(\\begin{cases}x\\ge1\\\\ y\\ge0\\\\ x+y\\le5\\end{cases}\\) and name its vertices.', 'Biểu diễn miền nghiệm của hệ \\(\\begin{cases}x\\ge1\\\\ y\\ge0\\\\ x+y\\le5\\end{cases}\\) và nêu các đỉnh.'),
  ('Three lines: \\(x=1\\), \\(y=0\\), \\(x+y=5\\).', 'Ba đường biên: \\(x=1\\), \\(y=0\\), \\(x+y=5\\).'),
  [T('The origin fails \\(x\\ge1\\), so we take the right of \\(x=1\\). It satisfies \\(y\\ge0\\) above the axis and \\(x+y\\le5\\) below the line.', 'Gốc tọa độ không thỏa \\(x\\ge1\\) nên lấy phía bên phải \\(x=1\\); \\(y\\ge0\\) lấy phía trên trục hoành; \\(x+y\\le5\\) lấy phía dưới đường thẳng.'),
   T('Vertices: \\(A(1;0)\\), \\(B(5;0)\\), \\(C(1;4)\\). The region is the triangle \\(ABC\\).', 'Các đỉnh: \\(A(1;0)\\), \\(B(5;0)\\), \\(C(1;4)\\). Miền nghiệm là tam giác \\(ABC\\).'),
   GE(region((-1, 6, -1, 6), [(-1, 0, -1), (0, -1, 0), (1, 1, 5)]), 'The triangle \\(ABC\\).', 'Tam giác \\(ABC\\).', 280)], T('Triangle with vertices \\(A(1;0)\\), \\(B(5;0)\\), \\(C(1;4)\\).', 'Tam giác có các đỉnh \\(A(1;0)\\), \\(B(5;0)\\), \\(C(1;4)\\).'))
assert [(int(x), int(y)) for x, y in vertices([(-1, 0, -1), (0, -1, 0), (1, 1, 5)])] == [(1, 0), (1, 4), (5, 0)]
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Largest and smallest values', 'Giá trị lớn nhất, nhỏ nhất'),
  T('On the region of Example 2 find the largest and smallest values of \\(F=2x+3y\\).', 'Trên miền nghiệm của Ví dụ 2, tìm giá trị lớn nhất và nhỏ nhất của \\(F=2x+3y\\).'),
  ('Compute \\(F\\) at the three vertices.', 'Tính \\(F\\) tại ba đỉnh.'),
  [T('\\(F(A)=2\\cdot1=2\\); \\(F(B)=2\\cdot5=10\\); \\(F(C)=2+3\\cdot4=14\\).', '\\(F(A)=2\\cdot1=2\\); \\(F(B)=2\\cdot5=10\\); \\(F(C)=2+3\\cdot4=14\\).')], T('Largest value 14 at \\(C(1;4)\\); smallest value 2 at \\(A(1;0)\\).', 'Giá trị lớn nhất là 14 tại \\(C(1;4)\\); nhỏ nhất là 2 tại \\(A(1;0)\\).'))
assert [2 * x + 3 * y for x, y in [(1, 0), (5, 0), (1, 4)]] == [2, 10, 14]
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('A production problem', 'Bài toán sản xuất'),
  T('A bakery makes \\(x\\) cakes of type A and \\(y\\) cakes of type B. Each day it can make at most 8 cakes in total, and the flour allows \\(2x+y\\le12\\). Profit: 30 thousand for A, 20 thousand for B. Find \\(x,y\\) for the largest daily profit.', 'Một tiệm bánh làm \\(x\\) bánh loại A và \\(y\\) bánh loại B. Mỗi ngày làm nhiều nhất 8 cái, và lượng bột cho phép \\(2x+y\\le12\\). Lãi: 30 nghìn/bánh A, 20 nghìn/bánh B. Tìm \\(x,y\\) để lãi ngày lớn nhất.'),
  ('Write the system, find the vertices, compute \\(F=30x+20y\\).', 'Viết hệ, tìm các đỉnh, tính \\(F=30x+20y\\).'),
  [T('System: \\(x\\ge0,\\ y\\ge0,\\ x+y\\le8,\\ 2x+y\\le12\\). Vertices: \\(O(0;0)\\), \\((6;0)\\), \\((4;4)\\), \\((0;8)\\).', 'Hệ: \\(x\\ge0,\\ y\\ge0,\\ x+y\\le8,\\ 2x+y\\le12\\). Các đỉnh: \\(O(0;0)\\), \\((6;0)\\), \\((4;4)\\), \\((0;8)\\).'),
   T('\\(F=0;\\ 180;\\ 200;\\ 160\\). The largest is 200.', '\\(F=0;\\ 180;\\ 200;\\ 160\\). Lớn nhất là 200.')], T('Make 4 cakes of A and 4 of B: profit 200 thousand.', 'Làm 4 bánh A và 4 bánh B: lãi 200 nghìn đồng.'))
_V4 = vertices([(-1, 0, 0), (0, -1, 0), (1, 1, 8), (2, 1, 12)]); assert max(30 * x + 20 * y for x, y in _V4) == 200 and sorted(_V4)[2] == (4, 4)
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('A minimum problem', 'Bài toán tìm giá trị nhỏ nhất'),
  T('A diet needs at least 12 units of vitamin and 8 units of protein. Food I has 3 vitamin and 1 protein per kg (cost 4 thousand). Food II has 1 vitamin and 2 protein per kg (cost 5 thousand). Find the cheapest mix.', 'Một khẩu phần cần ít nhất 12 đơn vị vitamin và 8 đơn vị protein. Thức ăn I có 3 vitamin và 1 protein mỗi kg (giá 4 nghìn). Thức ăn II có 1 vitamin và 2 protein mỗi kg (giá 5 nghìn). Tìm cách trộn rẻ nhất.'),
  ('Let \\(x,y\\) be kg of foods I, II. Minimise \\(F=4x+5y\\) with \\(\\ge\\) constraints.', 'Gọi \\(x,y\\) là số kg thức ăn I, II. Cực tiểu hóa \\(F=4x+5y\\) với các ràng buộc dạng \\(\\ge\\).'),
  [T('System: \\(x,y\\ge0,\\ 3x+y\\ge12,\\ x+2y\\ge8\\). The vertices are \\((0;12)\\), \\((8;0)\\) and \\((16/5;12/5)\\) (the meeting point of the two lines).', 'Hệ: \\(x,y\\ge0,\\ 3x+y\\ge12,\\ x+2y\\ge8\\). Đỉnh: \\((0;12)\\), \\((8;0)\\) và \\((16/5;12/5)\\) (giao của hai đường).'),
   T('\\(F(0;12)=60\\); \\(F(8;0)=32\\); \\(F(16/5;12/5)=64/5+12=124/5=24.8\\).', '\\(F(0;12)=60\\); \\(F(8;0)=32\\); \\(F(16/5;12/5)=64/5+12=124/5=24{,}8\\).')], T('The smallest cost is 24.8 thousand, with 3.2 kg of I and 2.4 kg of II.', 'Chi phí nhỏ nhất là 24,8 nghìn đồng, với 3,2 kg thức ăn I và 2,4 kg thức ăn II.'))
_V5 = vertices([(-1, 0, 0), (0, -1, 0), (-3, -1, -12), (-1, -2, -8)]); assert set(_V5) == {(F(16, 5), F(12, 5)), (0, 12), (8, 0)} and min(4 * x + 5 * y for x, y in _V5) == F(124, 5)

E2 = lambda a, b: lin(a, 0, 'x') + '+' + ('' if b == 1 else str(b)) + 'y'
def prm(s, a, b, c, p, q, pt, tv):
    def fn(_):
        n = 0
        cons = [(-1, 0, 0), (0, -1, 0), (1, 1, s), (a, b, c)]; V = vertices(cons); vals = {(x, y): p * x + q * y for x, y in V}; mx = max(vals.values())
        okp = lambda P: all(u * P[0] + v * P[1] <= w for u, v, w in cons)
        gp = [P for P in [(1, 1), (1, 2), (2, 1), (2, 2), (1, 3), (3, 1)] if okp(P)][0]
        bp = [P for P in [(s, 1), (s, s), (1, s), (s - 1, 3), (a + 1, c)] if not okp(P)][:3]
        sysx = '\\begin{cases}x\\ge0,\\ y\\ge0\\\\ x+y\\le%d\\\\ %s\\le%d\\end{cases}' % (s, E2(a, b), c)
        f = lambda P: '(%d;%d)' % P
        ix, iy = F(c - b * s, a - b), s - F(c - b * s, a - b)
        cnt = sum(1 for x in range(s + 1) for y in range(s + 1) if okp((x, y)))
        o1 = M4(1, 'Which pair is a solution of \\(%s\\)?' % sysx, 'Cặp số nào là nghiệm của hệ \\(%s\\)?' % sysx, f(gp), [f(P) for P in bp], 'It satisfies all the inequalities; the others break one.', 'Cặp này thỏa mọi bất phương trình; các cặp khác vi phạm ít nhất một.')
        t = lambda u, v: '(%s;%s)' % (fr(u), fr(v))
        o2 = M4(2, 'The lines \\(x+y=%d\\) and \\(%s=%d\\) meet at which point?' % (s, E2(a, b), c), 'Hai đường thẳng \\(x+y=%d\\) và \\(%s=%d\\) cắt nhau tại điểm nào?' % (s, E2(a, b), c), t(ix, iy), [t(iy, ix), t(ix + 1, iy), t(ix, iy + 1), t(ix + 1, iy + 1), t(ix - 1, iy)], 'Solve the two equations.', 'Giải hệ hai phương trình.')
        others = sorted({v for v in vals.values() if v != mx})
        o3 = M4(3, 'On the region of \\(%s\\) the largest value of \\(F=%s\\) is…' % (sysx, E2(p, q)), 'Trên miền nghiệm của hệ \\(%s\\), giá trị lớn nhất của \\(F=%s\\) là…' % (sysx, E2(p, q)), str(mx), [str(v) for v in others[-2:]] + [str(mx + 2)], 'Compute \\(F\\) at every vertex: the largest is %d.' % mx, 'Tính \\(F\\) tại mọi đỉnh: lớn nhất là %d.' % mx)
        t4 = f(pt); ok4 = okp(pt)
        tf4 = tf(4, 'The pair %s is a solution of \\(%s\\).' % (t4, sysx), 'Cặp %s là nghiệm của hệ \\(%s\\).' % (t4, sysx), ok4, 'Check each inequality.', 'Kiểm tra từng bất phương trình.')
        claim = mx if tv else mx + 1
        tf5 = tf(5, 'On the region of \\(%s\\), the largest value of \\(F=%s\\) is %d.' % (sysx, E2(p, q), claim), 'Trên miền nghiệm của hệ \\(%s\\), giá trị lớn nhất của \\(F=%s\\) là %d.' % (sysx, E2(p, q), claim), tv, 'The largest value is %d.' % mx, 'Giá trị lớn nhất là %d.' % mx)
        s6 = sh(6, 'How many pairs of natural numbers \\((x;y)\\) satisfy \\(%s\\)?' % sysx, 'Có bao nhiêu cặp số tự nhiên \\((x;y)\\) thỏa \\(%s\\)?' % sysx, cnt, 'Count the pairs: %d.' % cnt, 'Đếm các cặp: %d.' % cnt)
        s7 = sh(7, 'What is the largest value of \\(F=%s\\) on the region \\(%s\\)?' % (E2(p, q), sysx), 'Giá trị lớn nhất của \\(F=%s\\) trên miền \\(%s\\) là bao nhiêu?' % (E2(p, q), sysx), mx, 'Largest value: %d.' % mx, 'Giá trị lớn nhất: %d.' % mx)
        return [[o1, o2, o3], [tf4, tf5], [s6, s7]]
    return fn
_fns = [prm(4, 2, 1, 6, 3, 2, (3, 1), True), prm(5, 3, 1, 9, 2, 3, (2, 3), False), prm(6, 3, 2, 15, 4, 3, (4, 3), True)]
from mb_std import LEVEL_PRACTICE
practice = LEVEL_PRACTICE(GRP, {lv: fn(None) for lv, fn in zip((1, 2, 3), _fns)})
practice = with_self(practice, sp_g10b.B4, start=8)
mistakes = [('<b>Using “or” instead of “and”.</b> A solution must satisfy <b>all</b> inequalities.', '<b>Nhầm “hoặc” với “và”.</b> Nghiệm của hệ phải thỏa <b>tất cả</b> các bất phương trình.'),
 ('<b>Forgetting \\(x\\ge0,\\ y\\ge0\\).</b> Quantities like numbers of items cannot be negative.', '<b>Quên \\(x\\ge0,\\ y\\ge0\\).</b> Các đại lượng như số sản phẩm không thể âm.'),
 ('<b>Not checking a vertex.</b> An intersection of two lines is a vertex only if it satisfies the other inequalities.', '<b>Không kiểm tra đỉnh.</b> Giao điểm của hai đường chỉ là đỉnh khi thỏa các bất phương trình còn lại.'),
 ('<b>Optimising at a non-vertex.</b> Compare \\(F\\) at the vertices only.', '<b>Tối ưu tại điểm không phải đỉnh.</b> Chỉ so sánh \\(F\\) tại các đỉnh.'),
 ('<b>Forgetting whole numbers.</b> If \\(x,y\\) must be integers, check the answer.', '<b>Quên điều kiện nguyên.</b> Nếu \\(x,y\\) phải nguyên, hãy kiểm tra lại đáp số.')]
summary = [('A system of inequalities: all inequalities must hold; the region is the intersection of half-planes.', 'Hệ bất phương trình: mọi bất phương trình phải cùng đúng; miền nghiệm là giao các nửa mặt phẳng.'),
 ('Vertices come from two boundary lines and must satisfy the other inequalities.', 'Đỉnh là giao của hai đường biên và phải thỏa các bất phương trình còn lại.'),
 ('On a polygon, \\(F=px+qy\\) is largest or smallest at a vertex.', 'Trên một đa giác, \\(F=px+qy\\) đạt lớn nhất hoặc nhỏ nhất tại một đỉnh.'),
 ('Word problems: variables, constraints, \\(F\\), vertices, answer.', 'Bài toán thực tế: đặt ẩn, ràng buộc, \\(F\\), đỉnh, trả lời.'),
 ('Key English phrases: system of inequalities, vertex, objective function, maximum, minimum.', 'Cụm tiếng Anh cần nhớ: system of inequalities, vertex, objective function, maximum, minimum.')]
checks = [('I can check a solution of a system.', 'Tôi kiểm tra được nghiệm của hệ.'), ('I can draw the region and find its vertices.', 'Tôi vẽ được miền nghiệm và tìm các đỉnh.'), ('I can find the largest or smallest value of \\(F\\).', 'Tôi tìm được giá trị lớn nhất, nhỏ nhất của \\(F\\).'), ('I can solve a simple optimisation problem.', 'Tôi giải được bài toán tối ưu đơn giản.'), STD_SUMMARY_CHECK_EN()]
lesson(id='g10-ineq-sys-01', title_en='Systems of Linear Inequalities in Two Variables', title_vi=CV, topic=('Linear Inequalities in Two Variables', 'Bất phương trình bậc nhất hai ẩn'), folder='propositions-and-sets', file='linear-inequality-systems',
  catalog_title_vi=CV, meta=dict(level=('Intermediate', 'Trung bình'), time=('about 60 minutes', 'khoảng 60 phút'), before=('one linear inequality and its region', 'một bất phương trình bậc nhất hai ẩn và miền nghiệm của nó')),
  goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples, practice=practice, mistakes=mistakes, summary=summary, checks=checks,
  description='Systems of linear inequalities in two variables: solution regions, vertices and simple optimisation.', level='Intermediate', minutes=60,
  description_vi='Bài 4 – Hệ bất phương trình bậc nhất hai ẩn: miền nghiệm, đỉnh của miền và bài toán tối ưu đơn giản.',
  tags_vi=['hệ bất phương trình', 'miền nghiệm', 'đỉnh', 'tối ưu'], prerequisites=['g10-ineq2-01'], tags=['system of inequalities', 'region', 'vertex', 'optimisation'], order=40)
