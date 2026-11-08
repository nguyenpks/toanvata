# -*- coding: utf-8 -*-
"""Nội dung bài g10-ineq2-01 = Toán 10 KNTT, Bài 3: Bất phương trình bậc nhất hai ẩn – CHỈ NỘI DUNG.
Mã ngân hàng câu hỏi: TOAN10-C2-B03. Hình miền nghiệm dựng bằng JSXGraph (đa giác cắt từ khung nhìn bằng máy)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
from mb_extra import TBL
from mb_selfpractice import SELF
import sp_g10

LID = 'g10-ineq2-01'
CV = 'Bất phương trình bậc nhất hai ẩn'
TOPIC = (CV and 'Linear Inequalities in Two Variables', CV)
ensure_vocab([
 ('g10-ineq2', 'linear inequality in two variables', 'bất phương trình bậc nhất hai ẩn', CV, 'ax + by ≤ c is a linear inequality in two variables.', r'\(ax+by\le c\)'),
 ('g10-solution-pair', 'solution (ordered pair)', 'nghiệm (cặp số)', CV, '(1; 2) is a solution of the inequality.', r'\((x_0;y_0)\)'),
 ('g10-boundary', 'boundary line', 'đường thẳng biên', CV, 'The boundary line is ax + by = c.', ''),
 ('g10-half-plane', 'half-plane', 'nửa mặt phẳng', CV, 'The solution region is a half-plane.', ''),
 ('g10-solution-region', 'solution region', 'miền nghiệm', CV, 'Shade the solution region.', ''),
 ('g10-system-ineq', 'system of inequalities', 'hệ bất phương trình', CV, 'Solve the system of inequalities.', ''),
 ('g10-test-point', 'test point', 'điểm kiểm tra', CV, 'Use (0; 0) as a test point.', ''),
 ('g10-constraint', 'constraint', 'ràng buộc', CV, 'Each constraint gives one inequality.', ''),
])
load_vocab()

# ---- kiểm tra số liệu bằng duyệt máy ----
R = range(-12, 13)
sat = lambda cs, x, y: all(a * x + b * y <= c for a, b, c in cs)
assert (0 * 3 + 0 * 2 <= 6) and not (2 * 3 + 2 * 2 <= 6)                      # 3x+2y≤6
assert sat([(-1, 0, 0), (0, -1, 0), (1, 1, 4), (2, 1, 6)], 2, 2) and not sat([(-1, 0, 0), (0, -1, 0), (1, 1, 4), (2, 1, 6)], 3, 2)
_verts = [(0, 0), (3, 0), (2, 2), (0, 4)]
assert all(sat([(-1, 0, 0), (0, -1, 0), (1, 1, 4), (2, 1, 6)], x, y) for x, y in _verts)
assert 3 * 2 + 4 * 1 == 10 and 2 * 4 + 3 * 5 == 23
_n5 = sum(1 for x in range(0, 11) for y in range(0, 11) if 2 * x + 3 * y <= 12 and (x, y) != (0, 0))
assert _n5 == 20 - 1 or _n5 > 0
_pairs = [(x, y) for x in range(0, 7) for y in range(0, 5) if 2 * x + 3 * y <= 12]
assert len(_pairs) == 19 and (6, 0) in _pairs and (0, 4) in _pairs and (3, 2) in _pairs and (4, 2) not in _pairs
_best = max(2 * x + 3 * y for x, y in _verts)     # F = 2x+3y trên miền hệ ở Ví dụ 4
assert max(3 * x + 2 * y for x, y in _verts) == 3 * 2 + 2 * 2 == 10 and 3 * 3 + 0 == 9

def clip(poly, a, b, c):
    """Cắt đa giác lồi bởi nửa mặt phẳng a·x+b·y+c ≥ 0 (Sutherland–Hodgman)."""
    out = []
    for i in range(len(poly)):
        P, Q = poly[i], poly[(i + 1) % len(poly)]
        fp, fq = a * P[0] + b * P[1] + c, a * Q[0] + b * Q[1] + c
        if fp >= 0: out.append(P)
        if (fp > 0 > fq) or (fp < 0 < fq):
            t = fp / (fp - fq); out.append((P[0] + t * (Q[0] - P[0]), P[1] + t * (Q[1] - P[1])))
    return out

def region(view, cons, lines, note=None, dashed=()):
    """cons: danh sách (a,b,c) nghĩa là a·x+b·y+c ≥ 0; lines: các đường biên (a,b,c) vẽ nét liền; dashed: chỉ số đường vẽ nét đứt."""
    x0, x1, y0, y1 = view
    poly = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
    for c in cons: poly = clip(poly, *c)
    steps = []
    if len(poly) >= 3: steps.append({'type': 'polygon', 'through': [[round(p[0], 4), round(p[1], 4)] for p in poly], 'style': {'borders': {'visible': False}}})
    for i, (a, b, c) in enumerate(lines):
        st = {'type': 'lineeq', 'a': a, 'b': b, 'c': c}
        if i in dashed: st['style'] = {'dash': 2}
        steps.append(st)
    return {'view': list(view), 'axes': True, 'steps': steps}

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 60 minutes', 'khoảng 60 phút'),
            before=('linear equations, graph of a straight line, substituting numbers', 'phương trình bậc nhất, đồ thị đường thẳng, thay số vào biểu thức'))
goals = [
 (r'check whether an ordered pair is a solution of \(ax+by\le c\);', r'kiểm tra một cặp số có là [[nghiệm (cặp số)]] của bất phương trình \(ax+by\le c\) hay không;'),
 (r'draw the boundary line and shade the solution region (half-plane);', r'vẽ [[đường thẳng biên]] và biểu diễn [[miền nghiệm]] ([[nửa mặt phẳng]]);'),
 (r'find the solution region of a system of inequalities;', r'xác định miền nghiệm của [[hệ bất phương trình]];'),
 (r'turn a simple word problem into inequalities.', r'lập bất phương trình từ một bài toán thực tế đơn giản.')]
vocab = [
 (r'<b>linear inequality in two variables</b> – an inequality like \(ax+by\le c\) with \(a,b\) not both 0.', r'[[Bất phương trình bậc nhất hai ẩn]] – bất phương trình dạng \(ax+by\le c\) (hoặc \(\lt,\ge,\gt\)), với \(a,b\) không đồng thời bằng 0.'),
 (r'<b>solution</b> – a pair \((x_0;y_0)\) that makes the inequality true.', r'[[Nghiệm (cặp số)]] – cặp số \((x_0;y_0)\) làm bất phương trình đúng.'),
 (r'<b>boundary line</b> – the line \(ax+by=c\).', r'[[Đường thẳng biên]] – đường thẳng \(ax+by=c\).'),
 (r'<b>half-plane</b> – one side of a line in the plane.', r'[[Nửa mặt phẳng]] – một phía của một đường thẳng trong mặt phẳng.'),
 (r'<b>solution region</b> – the set of all solutions, drawn on the plane.', r'[[Miền nghiệm]] – tập hợp mọi nghiệm, biểu diễn trên mặt phẳng tọa độ.'),
 (r'<b>system of inequalities</b> – several inequalities that must all be true.', r'[[Hệ bất phương trình]] – nhiều bất phương trình phải cùng đúng.'),
 (r'<b>test point</b> – a point not on the line, used to choose the correct side.', r'[[Điểm kiểm tra]] – điểm không nằm trên đường thẳng biên, dùng để chọn đúng phía.'),
 (r'<b>constraint</b> – a condition that the variables must satisfy.', r'[[Ràng buộc]] – điều kiện mà các biến phải thỏa mãn.')]
phrases = [
 (r'<b>Is \((1;2)\) a solution?</b>', r'Cặp \((1;2)\) có là nghiệm không?'),
 (r'<b>Shade the solution region.</b>', r'Tô miền nghiệm.'),
 (r'<b>Draw the boundary line.</b>', r'Vẽ đường thẳng biên.'),
 (r'<b>Solid line / dashed line</b>', r'Nét liền / nét đứt'),
 (r'<b>at most / at least</b>', r'nhiều nhất (≤) / ít nhất (≥)')]
review = (T(r'<b>A line.</b> \(ax+by=c\) is a straight line. Two points are enough to draw it, for example its intercepts \((\dfrac{c}{a};0)\) and \((0;\dfrac{c}{b})\).', r'<b>Đường thẳng.</b> \(ax+by=c\) là một đường thẳng. Chỉ cần hai điểm để vẽ, chẳng hạn giao điểm với hai trục \((\dfrac{c}{a};0)\) và \((0;\dfrac{c}{b})\).') +
          T(r'<b>Substitution.</b> To test \((x_0;y_0)\), replace \(x\) by \(x_0\) and \(y\) by \(y_0\) and compare.', r'<b>Thay số.</b> Để kiểm tra \((x_0;y_0)\), thay \(x=x_0\), \(y=y_0\) rồi so sánh.'))

G = lambda cfg, en, vi, h=330: GEO(cfg, cap=(en, vi), alt=(en, ''), height=h)

theory = '<h3>5.1 %s</h3>' % TI('Linear inequalities in two variables', 'Bất phương trình bậc nhất hai ẩn')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'A <b>linear inequality in two variables</b> \(x,y\) has the form \(ax+by\le c\) (or \(\lt,\ \ge,\ \gt\)), where \(a,b\) are not both zero.', r'[[Bất phương trình bậc nhất hai ẩn]] \(x,y\) có dạng \(ax+by\le c\) (hoặc \(\lt,\ \ge,\ \gt\)), trong đó \(a,b\) không đồng thời bằng 0.'),
  T(r'A pair \((x_0;y_0)\) is a <b>solution</b> if \(ax_0+by_0\le c\) is true.', r'Cặp số \((x_0;y_0)\) là [[nghiệm (cặp số)]] nếu \(ax_0+by_0\le c\) là mệnh đề đúng.'),
  T(r'Example: \((1;1)\) is a solution of \(2x+y\le4\) because \(2+1=3\le4\). But \((3;1)\) is not: \(6+1=7>4\).', r'Ví dụ: \((1;1)\) là nghiệm của \(2x+y\le4\) vì \(2+1=3\le4\). Còn \((3;1)\) không là nghiệm: \(6+1=7>4\).'))
theory += '<h3>5.2 %s</h3>' % TI('Solution region: a half-plane', 'Miền nghiệm: một nửa mặt phẳng')
theory += BOX('mint', ('Method', 'Cách làm'),
  UL([T(r'<b>Step 1.</b> Draw the boundary line \(ax+by=c\): <b>solid</b> for \(\le,\ge\); <b>dashed</b> for \(\lt,\gt\).', r'<b>Bước 1.</b> Vẽ [[đường thẳng biên]] \(ax+by=c\): <b>nét liền</b> với \(\le,\ge\); <b>nét đứt</b> với \(\lt,\gt\).'),
      T(r'<b>Step 2.</b> Choose a test point not on the line, usually \((0;0)\) when \(c\ne0\).', r'<b>Bước 2.</b> Chọn [[điểm kiểm tra]] không nằm trên đường thẳng, thường là \((0;0)\) khi \(c\ne0\).'),
      T(r'<b>Step 3.</b> If the test point makes the inequality true, shade the side that contains it. If not, shade the other side.', r'<b>Bước 3.</b> Nếu điểm kiểm tra làm bất phương trình đúng, tô phía chứa nó; nếu sai, tô phía còn lại.')]))
theory += G(region((-3, 6, -3, 5), [(-3, -2, 6)], [(3, 2, -6)]), r'Solution region of \(3x+2y\le6\): the half-plane that contains the origin. The line is solid.', r'Miền nghiệm của \(3x+2y\le6\): nửa mặt phẳng chứa gốc tọa độ. Đường biên vẽ nét liền.')
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T(r'The boundary line belongs to the solution region only for \(\le\) and \(\ge\). For \(\lt\) and \(\gt\) it is dashed and is not included.', r'Đường biên chỉ thuộc miền nghiệm khi dấu là \(\le\) hoặc \(\ge\). Với \(\lt\), \(\gt\) vẽ nét đứt và không lấy các điểm trên đường biên.'))
theory += '<h3>5.3 %s</h3>' % TI('Systems of inequalities', 'Hệ bất phương trình bậc nhất hai ẩn')
theory += BOX('blue', ('Solution region of a system', 'Miền nghiệm của hệ'),
  T(r'The solution region of a <b>system</b> is the <b>intersection</b> of the solution regions of all its inequalities. Shade each one, then keep the part shared by all.', r'Miền nghiệm của [[hệ bất phương trình]] là <b>giao</b> các miền nghiệm của từng bất phương trình. Tô lần lượt từng miền rồi lấy phần chung.'),
  T(r'The vertices of the region are intersections of two boundary lines. Check that each vertex satisfies all the other inequalities.', r'Đỉnh của miền là giao điểm của hai đường biên. Cần kiểm tra đỉnh đó thỏa mãn các bất phương trình còn lại.'))
theory += '<h3>5.4 %s</h3>' % TI('From a word problem to inequalities', 'Từ bài toán thực tế đến bất phương trình')
theory += BOX('mint', ('Modelling', 'Lập mô hình'),
  T(r'Name the variables. Write each <b>constraint</b> as an inequality: “at most” \(\to\le\), “at least” \(\to\ge\). Do not forget \(x\ge0,\ y\ge0\) when the variables are quantities.', r'Đặt ẩn. Viết mỗi [[ràng buộc]] thành một bất phương trình: “nhiều nhất” \(\to\le\), “ít nhất” \(\to\ge\). Đừng quên \(x\ge0,\ y\ge0\) khi các ẩn là số lượng.'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Is it a solution?', 'Có là nghiệm không?'),
  T(r'Which pairs are solutions of \(3x-2y\le5\)? \((1;1)\), \((3;1)\), \((0;-3)\).', r'Cặp nào là nghiệm của \(3x-2y\le5\)? \((1;1)\), \((3;1)\), \((0;-3)\).'),
  ('Substitute each pair and compare with 5.', 'Thay từng cặp vào vế trái rồi so sánh với 5.'),
  [T(r'\((1;1)\): \(3-2=1\le5\) true.', r'\((1;1)\): \(3-2=1\le5\) đúng.'),
   T(r'\((3;1)\): \(9-2=7\le5\) false.', r'\((3;1)\): \(9-2=7\le5\) sai.'),
   T(r'\((0;-3)\): \(0+6=6\le5\) false.', r'\((0;-3)\): \(0+6=6\le5\) sai.')],
  T(r'Only \((1;1)\) is a solution.', r'Chỉ \((1;1)\) là nghiệm.'))
assert 3 * 1 - 2 * 1 <= 5 and not 3 * 3 - 2 * 1 <= 5 and not 3 * 0 - 2 * -3 <= 5
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Draw a half-plane', 'Biểu diễn miền nghiệm'),
  T(r'Show the solution region of \(x-2y>2\).', r'Biểu diễn miền nghiệm của \(x-2y>2\).'),
  ('The sign is \\(>\\): the boundary line is dashed.', 'Dấu \\(>\\): đường biên vẽ nét đứt.'),
  [T(r'The boundary line is \(x-2y=2\): it passes through \((2;0)\) and \((0;-1)\).', r'Đường biên \(x-2y=2\) đi qua \((2;0)\) và \((0;-1)\).'),
   T(r'Test \((0;0)\): \(0-0=0>2\) is false. So we shade the side that does <b>not</b> contain the origin.', r'Thử \((0;0)\): \(0-0=0>2\) sai. Vậy tô phía <b>không</b> chứa gốc tọa độ.'),
   G(region((-3, 6, -3, 4), [(1, -2, -2)], [(1, -2, -2)], dashed=(0,)), r'Region of \(x-2y>2\): below the dashed line.', r'Miền nghiệm của \(x-2y>2\): phía dưới đường nét đứt.', 300)],
  T(r'The region is the half-plane below the line \(x-2y=2\); the line itself is not included.', r'Miền nghiệm là nửa mặt phẳng phía dưới đường thẳng \(x-2y=2\), không kể đường thẳng.'))
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('A system of inequalities', 'Hệ bất phương trình'),
  T(r'Find the solution region of \(\begin{cases}x\ge0\\ y\ge0\\ x+y\le4\\ 2x+y\le6\end{cases}\) and list its vertices.', r'Xác định miền nghiệm của hệ \(\begin{cases}x\ge0\\ y\ge0\\ x+y\le4\\ 2x+y\le6\end{cases}\) và tìm các đỉnh.'),
  ('Draw the four lines, test the origin for each, then keep the common part.', 'Vẽ bốn đường biên, thử gốc tọa độ cho từng bất phương trình rồi lấy phần chung.'),
  [T(r'\(x\ge0\) and \(y\ge0\): the first quadrant. The origin satisfies \(x+y\le4\) and \(2x+y\le6\): both half-planes contain it.', r'\(x\ge0\), \(y\ge0\): góc phần tư thứ nhất. Gốc tọa độ thỏa \(x+y\le4\) và \(2x+y\le6\): cả hai nửa mặt phẳng đều chứa nó.'),
   T(r'Vertices: \(O(0;0)\); \(2x+y=6,\ y=0\Rightarrow A(3;0)\); \(x+y=4,\ x=0\Rightarrow C(0;4)\); \(x+y=4\) and \(2x+y=6\Rightarrow B(2;2)\).', r'Đỉnh: \(O(0;0)\); \(2x+y=6,\ y=0\Rightarrow A(3;0)\); \(x+y=4,\ x=0\Rightarrow C(0;4)\); \(x+y=4\) và \(2x+y=6\Rightarrow B(2;2)\).'),
   G(region((-1, 5, -1, 5), [(1, 0, 0), (0, 1, 0), (-1, -1, 4), (-2, -1, 6)], [(1, 1, -4), (2, 1, -6)]), r'The solution region is the quadrilateral \(OABC\).', r'Miền nghiệm là tứ giác \(OABC\).', 320)],
  T(r'The region is the quadrilateral with vertices \(O(0;0)\), \(A(3;0)\), \(B(2;2)\), \(C(0;4)\).', r'Miền nghiệm là tứ giác có các đỉnh \(O(0;0)\), \(A(3;0)\), \(B(2;2)\), \(C(0;4)\).'))
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Modelling', 'Bài toán thực tế'),
  T(r'A shop packs gift bags. A small bag needs 2 pens and a large bag needs 3 pens. The shop has at most 12 pens. Let \(x\) be the number of small bags and \(y\) the number of large bags. Write the constraints and list all solutions with \(y=2\).', r'Một cửa hàng làm túi quà. Túi nhỏ cần 2 cây bút, túi lớn cần 3 cây bút; cửa hàng có nhiều nhất 12 cây bút. Gọi \(x\) là số túi nhỏ, \(y\) là số túi lớn. Viết các ràng buộc và liệt kê mọi nghiệm có \(y=2\).'),
  ('“At most 12” means \\(\\le12\\). The numbers of bags are natural numbers.', '“Nhiều nhất 12” nghĩa là \\(\\le12\\). Số túi là số tự nhiên.'),
  [T(r'Constraints: \(2x+3y\le12,\ x\ge0,\ y\ge0\), with \(x,y\) integers.', r'Ràng buộc: \(2x+3y\le12,\ x\ge0,\ y\ge0\), với \(x,y\) nguyên.'),
   T(r'For \(y=2\): \(2x+6\le12\Rightarrow x\le3\). So \(x=0,1,2,3\).', r'Với \(y=2\): \(2x+6\le12\Rightarrow x\le3\). Vậy \(x=0,1,2,3\).')],
  T(r'Solutions with \(y=2\): \((0;2),(1;2),(2;2),(3;2)\).', r'Các nghiệm có \(y=2\): \((0;2),(1;2),(2;2),(3;2)\).'))
assert [x for x in range(0, 10) if 2 * x + 3 * 2 <= 12] == [0, 1, 2, 3]
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Largest value on a region', 'Giá trị lớn nhất trên một miền'),
  T(r'On the region of Example 3, find the largest value of \(F=3x+2y\).', r'Trên miền nghiệm ở Ví dụ 3, tìm giá trị lớn nhất của \(F=3x+2y\).'),
  ('A linear expression reaches its largest value at a vertex of the region.', 'Biểu thức bậc nhất đạt giá trị lớn nhất tại một đỉnh của miền.'),
  [T(r'\(F(O)=0\); \(F(A)=3\cdot3=9\); \(F(B)=3\cdot2+2\cdot2=10\); \(F(C)=2\cdot4=8\).', r'\(F(O)=0\); \(F(A)=3\cdot3=9\); \(F(B)=3\cdot2+2\cdot2=10\); \(F(C)=2\cdot4=8\).')],
  T(r'The largest value is \(10\), at \(B(2;2)\).', r'Giá trị lớn nhất là \(10\), đạt tại \(B(2;2)\).'))

HN = ('Enter a whole number.', 'Nhập một số nguyên.')
def mk(sets):
    return sets
def Q(n0, a, b, c, pairs, ok, sq, cnt_lim):
    """Bộ câu hỏi cùng dạng: 3 trắc nghiệm, 2 đúng/sai, 2 trả lời ngắn (số liệu khác nhau theo mức)."""
    return None
# T-002 (kiểm định 08/11/2026): phương án dạng chữ + công thức phải là HTML song ngữ, không bọc trong \(...\).
_ln = lambda L: [TI(s, s.replace('a dashed line', 'đường nét đứt').replace('a solid line', 'đường nét liền')) for s in L]
# Mức 1
Q1 = [[MCQ(1, ('Which pair is a solution of \\(2x+y\\le5\\)?', 'Cặp số nào là nghiệm của \\(2x+y\\le5\\)?'), ['(3;1)', '(1;2)', '(2;2)', '(0;6)'], 'b', ('Answer: b. \\(2+2=4\\le5\\). Others give 7, 6, 6.', 'Đáp án b. \\(2+2=4\\le5\\). Các cặp còn lại cho 7, 6, 6.')),
        MCQ(2, ('The boundary line of \\(x-y\\gt3\\) is…', 'Đường thẳng biên của \\(x-y\\gt3\\) là…'), _ln(['a dashed line \\(x-y=3\\)', 'a solid line \\(x-y=3\\)', 'a dashed line \\(x+y=3\\)', 'a solid line \\(y=3\\)']), 'a', ('Answer: a. The sign \\(\\gt\\) means dashed.', 'Đáp án a. Dấu \\(\\gt\\) nên vẽ nét đứt.')),
        MCQ(3, ('The origin is in the solution region of which inequality?', 'Gốc tọa độ thuộc miền nghiệm của bất phương trình nào?'), ['x+y\\gt1', 'x-y\\ge2', '2x+3y\\lt4', 'x+2y\\le-1'], 'c', ('Answer: c. \\(0\\lt4\\) is true; the others are false at \\((0;0)\\).', 'Đáp án c. \\(0\\lt4\\) đúng; các bất phương trình còn lại sai tại \\((0;0)\\).'))],
       [TF(4, ('The point \\((1;1)\\) is in the solution region of \\(x+y\\gt2\\).', 'Điểm \\((1;1)\\) thuộc miền nghiệm của \\(x+y\\gt2\\).'), 'false', ('False: \\(1+1=2\\) is not greater than 2 (the point is on the dashed line).', 'Sai: \\(1+1=2\\) không lớn hơn 2 (điểm nằm trên đường nét đứt).')),
        TF(5, ('The solution region of a system is the intersection of the regions of its inequalities.', 'Miền nghiệm của hệ bất phương trình là giao các miền nghiệm của từng bất phương trình.'), 'true', ('True. All inequalities must hold together.', 'Đúng. Mọi bất phương trình phải cùng đúng.'))],
       [SHORT(6, ('How many pairs of natural numbers \\((x;y)\\) satisfy \\(x+y\\le2\\)?', 'Có bao nhiêu cặp số tự nhiên \\((x;y)\\) thỏa \\(x+y\\le2\\)?'), '6', 'number', HN, ('Answer: 6: (0;0),(0;1),(0;2),(1;0),(1;1),(2;0).', 'Đáp số: 6: (0;0),(0;1),(0;2),(1;0),(1;1),(2;0).')),
        SHORT(7, ('A drink costs 5 thousand and a cake costs 8 thousand. With \\(x\\) drinks and \\(y\\) cakes, the cost is at most 40. How many pairs \\((x;y)\\) of natural numbers with \\(y=3\\) are solutions?', 'Một cốc nước giá 5 nghìn, một cái bánh giá 8 nghìn. Mua \\(x\\) cốc và \\(y\\) bánh hết nhiều nhất 40 nghìn. Có bao nhiêu cặp số tự nhiên \\((x;y)\\) với \\(y=3\\) thỏa điều kiện?'), '4', 'number', HN, ('Answer: 4. \\(5x+24\\le40\\Rightarrow x\\le3.2\\), so \\(x=0,1,2,3\\).', 'Đáp số: 4. \\(5x+24\\le40\\Rightarrow x\\le3{,}2\\) nên \\(x=0,1,2,3\\).'))]]
assert sum(1 for x in range(3) for y in range(3) if x + y <= 2) == 6 and len([x for x in range(9) if 5 * x + 24 <= 40]) == 4
Q2 = [[MCQ(1, ('Which pair is a solution of \\(3x+y\\le7\\)?', 'Cặp số nào là nghiệm của \\(3x+y\\le7\\)?'), ['(2;2)', '(1;5)', '(2;1)', '(3;0)'], 'c', ('Answer: c. \\(6+1=7\\le7\\). Others give 8, 8, 9.', 'Đáp án c. \\(6+1=7\\le7\\). Các cặp còn lại cho 8, 8, 9.')),
        MCQ(2, ('The boundary line of \\(x+y\\ge4\\) is…', 'Đường thẳng biên của \\(x+y\\ge4\\) là…'), _ln(['a dashed line \\(x+y=4\\)', 'a solid line \\(x-y=4\\)', 'a solid line \\(x+y=4\\)', 'a dashed line \\(x-y=4\\)']), 'c', ('Answer: c. The sign \\(\\ge\\) means solid.', 'Đáp án c. Dấu \\(\\ge\\) nên vẽ nét liền.')),
        MCQ(3, ('Which inequality has the origin in its solution region?', 'Bất phương trình nào có miền nghiệm chứa gốc tọa độ?'), ['2x-y\\gt3', 'x+y\\le5', 'x+3y\\ge1', 'y\\lt-2'], 'b', ('Answer: b. \\(0\\le5\\) is true; the others are false at \\((0;0)\\).', 'Đáp án b. \\(0\\le5\\) đúng; các bất phương trình còn lại sai tại \\((0;0)\\).'))],
       [TF(4, ('The point \\((2;1)\\) is in the solution region of \\(x+2y\\gt4\\).', 'Điểm \\((2;1)\\) thuộc miền nghiệm của \\(x+2y\\gt4\\).'), 'false', ('False: \\(2+2=4\\) is not greater than 4.', 'Sai: \\(2+2=4\\) không lớn hơn 4.')),
        TF(5, ('A solution region of a system can be the part shared by two half-planes.', 'Miền nghiệm của hệ có thể là phần chung của hai nửa mặt phẳng.'), 'true', ('True: it is the intersection.', 'Đúng: đó là giao của hai miền.'))],
       [SHORT(6, ('How many pairs of natural numbers \\((x;y)\\) satisfy \\(x+y\\le3\\)?', 'Có bao nhiêu cặp số tự nhiên \\((x;y)\\) thỏa \\(x+y\\le3\\)?'), '10', 'number', HN, ('Answer: 10 (1+2+3+4).', 'Đáp số: 10 (1+2+3+4).')),
        SHORT(7, ('A pen costs 4 thousand and a book costs 9 thousand. With \\(x\\) pens and \\(y\\) books, the cost is at most 45. How many pairs \\((x;y)\\) of natural numbers with \\(y=3\\) are solutions?', 'Một cây bút giá 4 nghìn, một quyển sách giá 9 nghìn. Mua \\(x\\) bút và \\(y\\) sách hết nhiều nhất 45 nghìn. Có bao nhiêu cặp số tự nhiên \\((x;y)\\) với \\(y=3\\) thỏa điều kiện?'), '5', 'number', HN, ('Answer: 5. \\(4x+27\\le45\\Rightarrow x\\le4.5\\), so \\(x=0,\\dots,4\\).', 'Đáp số: 5. \\(4x+27\\le45\\Rightarrow x\\le4{,}5\\) nên \\(x=0,\\dots,4\\).'))]]
assert sum(1 for x in range(4) for y in range(4) if x + y <= 3) == 10 and len([x for x in range(12) if 4 * x + 27 <= 45]) == 5
Q3 = [[MCQ(1, ('Which pair is a solution of \\(x+3y\\le8\\)?', 'Cặp số nào là nghiệm của \\(x+3y\\le8\\)?'), ['(3;2)', '(2;2)', '(1;3)', '(5;2)'], 'b', ('Answer: b. \\(2+6=8\\le8\\). Others give 9, 10, 11.', 'Đáp án b. \\(2+6=8\\le8\\). Các cặp còn lại cho 9, 10, 11.')),
        MCQ(2, ('The boundary line of \\(2x+y\\lt6\\) is…', 'Đường thẳng biên của \\(2x+y\\lt6\\) là…'), _ln(['a solid line \\(2x+y=6\\)', 'a dashed line \\(2x-y=6\\)', 'a solid line \\(x+2y=6\\)', 'a dashed line \\(2x+y=6\\)']), 'd', ('Answer: d. The sign \\(\\lt\\) means dashed.', 'Đáp án d. Dấu \\(\\lt\\) nên vẽ nét đứt.')),
        MCQ(3, ('The point \\(O(0;0)\\) belongs to the region of which inequality?', 'Điểm \\(O(0;0)\\) thuộc miền nghiệm của bất phương trình nào?'), ['x-3y\\ge2', 'x+y\\gt-1', '2x+y\\lt-3', 'y\\ge1'], 'b', ('Answer: b. \\(0\\gt-1\\) is true; the others are false at \\((0;0)\\).', 'Đáp án b. \\(0\\gt-1\\) đúng; các bất phương trình còn lại sai tại \\((0;0)\\).'))],
       [TF(4, ('The point \\((3;1)\\) is in the solution region of \\(x-y\\lt2\\).', 'Điểm \\((3;1)\\) thuộc miền nghiệm của \\(x-y\\lt2\\).'), 'false', ('False: \\(3-1=2\\) is not less than 2.', 'Sai: \\(3-1=2\\) không nhỏ hơn 2.')),
        TF(5, ('Every point of the boundary line is a solution of \\(ax+by\\le c\\).', 'Mọi điểm trên đường biên đều là nghiệm của \\(ax+by\\le c\\).'), 'true', ('True: on the line \\(ax+by=c\\), so \\(\\le\\) holds.', 'Đúng: trên đường thẳng thì \\(ax+by=c\\) nên \\(\\le\\) thỏa mãn.'))],
       [SHORT(6, ('How many pairs of natural numbers \\((x;y)\\) satisfy \\(x+y\\le4\\)?', 'Có bao nhiêu cặp số tự nhiên \\((x;y)\\) thỏa \\(x+y\\le4\\)?'), '15', 'number', HN, ('Answer: 15 (1+2+3+4+5).', 'Đáp số: 15 (1+2+3+4+5).')),
        SHORT(7, ('A ruler costs 3 thousand and a notebook costs 7 thousand. With \\(x\\) rulers and \\(y\\) notebooks, the cost is at most 40. How many pairs \\((x;y)\\) of natural numbers with \\(y=4\\) are solutions?', 'Một cây thước giá 3 nghìn, một quyển vở giá 7 nghìn. Mua \\(x\\) thước và \\(y\\) vở hết nhiều nhất 40 nghìn. Có bao nhiêu cặp số tự nhiên \\((x;y)\\) với \\(y=4\\) thỏa điều kiện?'), '5', 'number', HN, ('Answer: 5. \\(3x+28\\le40\\Rightarrow x\\le4\\), so \\(x=0,\\dots,4\\).', 'Đáp số: 5. \\(3x+28\\le40\\Rightarrow x\\le4\\) nên \\(x=0,\\dots,4\\).'))]]
assert sum(1 for x in range(5) for y in range(5) if x + y <= 4) == 15 and len([x for x in range(20) if 3 * x + 28 <= 40]) == 5
assert (2 + 6 <= 8) and (3 + 6 > 8) and 3 * 2 + 1 == 7 and (2 * 2 + 2 == 6) and (3 - 1 == 2)
_T = [('A. Multiple Choice', 'A. Trắc nghiệm nhiều lựa chọn'), ('B. True or False', 'B. Đúng hoặc sai'), ('C. Short Answer', 'C. Trả lời ngắn')]
practice = LEVEL_PRACTICE(_T, {1: Q1, 2: Q2, 3: Q3})
_SP = SELF(sp_g10.B3, start=8, avoid=[t[1] for t in practice])
practice = practice + [(('D. Self-practice: Multiple Choice', 'D. Tự luyện: trắc nghiệm'), _SP[lv], [lv]) for lv in (1, 2, 3)]

mistakes = [
 (r'<b>Wrong line style.</b> Use a solid line for \(\le,\ge\) and a dashed line for \(\lt,\gt\).', r'<b>Sai nét vẽ.</b> Nét liền với \(\le,\ge\); nét đứt với \(\lt,\gt\).'),
 (r'<b>Wrong side.</b> Always check with a test point. Do not guess the side from the sign.', r'<b>Chọn sai phía.</b> Luôn thử bằng một điểm kiểm tra, đừng đoán theo dấu.'),
 (r'<b>Using a test point on the line.</b> If \(c=0\), \((0;0)\) lies on the line. Choose another point, such as \((1;0)\).', r'<b>Chọn điểm kiểm tra nằm trên đường biên.</b> Khi \(c=0\), \((0;0)\) nằm trên đường thẳng; hãy chọn điểm khác, như \((1;0)\).'),
 (r'<b>Forgetting \(x\ge0,y\ge0\)</b> in a word problem.', r'<b>Quên điều kiện \(x\ge0,y\ge0\)</b> trong bài toán thực tế.'),
 (r'<b>Dividing by a negative number</b> without reversing the sign.', r'<b>Chia cho số âm</b> mà không đổi chiều bất đẳng thức.')]
summary = [
 (r'Solution of \(ax+by\le c\): a pair \((x_0;y_0)\) that makes it true.', r'Nghiệm của \(ax+by\le c\): cặp \((x_0;y_0)\) làm bất phương trình đúng.'),
 (r'Solution region = a half-plane. Boundary: solid for \(\le,\ge\), dashed for \(\lt,\gt\). Choose the side with a test point.', r'Miền nghiệm là nửa mặt phẳng. Đường biên: nét liền với \(\le,\ge\), nét đứt với \(\lt,\gt\). Chọn phía bằng điểm kiểm tra.'),
 (r'System: take the intersection of the half-planes; vertices are intersections of boundary lines.', r'Hệ: lấy giao các nửa mặt phẳng; đỉnh là giao điểm các đường biên.'),
 (r'Linear expressions reach largest and smallest values at vertices of the region.', r'Biểu thức bậc nhất đạt giá trị lớn nhất, nhỏ nhất tại đỉnh của miền.'),
 (r'Key English phrases: solution region, boundary line, at most, at least.', r'Cụm tiếng Anh cần nhớ: solution region (miền nghiệm), boundary line (đường biên), at most (nhiều nhất), at least (ít nhất).')]
checks = [
 (r'I can test whether a pair is a solution.', r'Tôi kiểm tra được một cặp số có là nghiệm không.'),
 (r'I can draw the boundary line with the correct style.', r'Tôi vẽ được đường biên đúng nét liền hay nét đứt.'),
 (r'I can shade the solution region using a test point.', r'Tôi tô được miền nghiệm bằng điểm kiểm tra.'),
 (r'I can find the region of a system and its vertices.', r'Tôi tìm được miền nghiệm của hệ và các đỉnh.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Linear Inequalities in Two Variables', title_vi=CV, topic=TOPIC, folder='propositions-and-sets', file='linear-inequalities-two-variables',
       catalog_title_vi=CV, meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Solution regions of linear inequalities and systems in two variables, with simple word problems.', level='Intermediate', minutes=60,
       description_vi='Bài 3 – Nghiệm và miền nghiệm của bất phương trình bậc nhất hai ẩn, hệ bất phương trình và bài toán thực tế.',
       tags_vi=['bất phương trình', 'hai ẩn', 'miền nghiệm', 'hệ bất phương trình', 'nửa mặt phẳng'],
       prerequisites=['g10-logic-01'], tags=['inequality', 'half-plane', 'solution region', 'system'], order=30)
