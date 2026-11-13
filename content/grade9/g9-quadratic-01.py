# -*- coding: utf-8 -*-
"""Nội dung bài g9-quadratic-01 = Toán 9 KNTT, Bài 18: Hàm số y = ax² (a ≠ 0) – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 6 – Lesson 18."""
import os, sys, math
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9

LID = 'g9-quadratic-01'
CH = 'Hàm số y = ax² (a ≠ 0). Phương trình bậc hai một ẩn'
TOPIC = ('Quadratic Function and Quadratic Equation', CH)
ensure_vocab([
 ('g9-parabola', 'parabola (pl. parabolas)', 'parabol', CH, 'The graph of y = ax² is a parabola.', ''),
 ('g9-vertex', 'vertex (of a parabola)', 'đỉnh (của parabol)', CH, 'The vertex of the parabola y = ax² is O.', ''),
 ('g9-table-values', 'table of values', 'bảng giá trị', CH, 'Complete a table of values for x = −2, −1, 0, 1, 2.', ''),
 ('g9-abscissa', 'abscissa (x-coordinate)', 'hoành độ', CH, 'The point has abscissa 2.', ''),
 ('g9-ordinate', 'ordinate (y-coordinate)', 'tung độ', CH, 'Find the points whose ordinate is 8.', ''),
 ('g9-sym-about', 'symmetric about', 'đối xứng nhau qua', CH, 'The two points are symmetric about the y-axis.', ''),
 ('g9-graph-of', 'graph (of a function)', 'đồ thị (của hàm số)', CH, 'Draw the graph of y = 2x².', ''),
])
load_vocab()

# ---------- kiểm tra số liệu ----------
f = lambda a, x: F(a) * x * x
assert [f(F(1, 2), x) for x in (-2, -1, 0, 1, 2)] == [2, F(1, 2), 0, F(1, 2), 2]
assert f(-2, F(1, 2)) == F(-1, 2) and f(-2, F(-1, 2)) == F(-1, 2)
assert F(2, 4) == F(1, 2) and f(F(1, 2), -2) == 2 and f(F(1, 2), 4) == 8
a4 = F(-9, 2) / 9; assert a4 == F(-1, 2) and F(9, 2) + f(a4, 2) == F(5, 2) and F(9, 2) + f(a4, 1) == 4
a5 = F(75, 200 ** 2); assert a5 == F(3, 1600) and f(a5, 100) == F(75, 4)

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 75 minutes', '75 phút'), before=('Grade 8: functions and their graphs', 'Lớp 8: hàm số và đồ thị'))
goals = [
 (r'recognize the function \(y=ax^2\ (a\ne0)\) and make a table of values;', r'nhận biết được hàm số \(y=ax^2\ (a\ne0)\) và lập được bảng giá trị;'),
 (r'describe the graph: a parabola with vertex \(O\) and axis of symmetry \(Oy\);', r'mô tả được đồ thị: parabol có đỉnh \(O\), nhận \(Oy\) làm trục đối xứng;'),
 (r'draw the graph; find \(a\) or points of the graph from given data;', r'vẽ được đồ thị; tìm được \(a\) hoặc các điểm của đồ thị từ dữ kiện cho trước;'),
 (r'solve real-life problems (falling objects, parabolic arches, suspension bridges).', r'giải được bài toán thực tế (vật rơi, cổng parabol, cầu treo).')]
vocab = [
 (r'<b>parabola</b> – the graph of \(y=ax^2\).', r'[[Parabol]] – đồ thị của hàm số \(y=ax^2\).'),
 (r'<b>vertex</b> – the lowest (\(a\gt0\)) or highest (\(a\lt0\)) point, here \(O\).', r'[[Đỉnh|đỉnh (của parabol)]] – điểm thấp nhất (\(a\gt0\)) hoặc cao nhất (\(a\lt0\)), ở đây là \(O\).'),
 (r'<b>table of values</b> – values of \(y\) for chosen \(x\).', r'[[Bảng giá trị]] – các giá trị của \(y\) ứng với các giá trị của \(x\).'),
 (r'<b>abscissa / ordinate</b> – the \(x\)- / \(y\)-coordinate of a point.', r'[[Hoành độ]] / [[tung độ]] – tọa độ \(x\) / \(y\) của một điểm.'),
 (r'<b>symmetric about</b> \(Oy\) – \((x;\,y)\) and \((-x;\,y)\).', r'[[Đối xứng nhau qua]] \(Oy\) – \((x;\,y)\) và \((-x;\,y)\).')]
phrases = [
 (r'<b>The graph of \(y=ax^2\) is a parabola with vertex \(O\).</b>', r'Đồ thị hàm số \(y=ax^2\) là một parabol có đỉnh \(O\).'),
 (r'<b>The parabola is symmetric about the \(y\)-axis.</b>', r'Parabol nhận trục \(Oy\) làm trục đối xứng.'),
 (r'<b>If \(a\gt0\), the graph lies above the \(x\)-axis.</b>', r'Nếu \(a\gt0\) thì đồ thị nằm phía trên trục hoành.'),
 (r'<b>Plot the points and join them with a smooth curve.</b>', r'Vẽ các điểm rồi nối chúng bằng một đường cong trơn.'),
 (r'<b>Substitute the coordinates of the point into the formula.</b>', r'Thay tọa độ của điểm vào công thức.')]
review = (T(r'<b>Grade 8.</b> A point \(M(x_0;\,y_0)\) lies on the graph of \(y=f(x)\) when \(y_0=f(x_0)\).', r'<b>Lớp 8.</b> Điểm \(M(x_0;\,y_0)\) thuộc đồ thị hàm số \(y=f(x)\) khi \(y_0=f(x_0)\).') +
          T(r'<b>Symmetry.</b> \((x;\,y)\) and \((-x;\,y)\) are symmetric about \(Oy\).', r'<b>Đối xứng.</b> \((x;\,y)\) và \((-x;\,y)\) đối xứng nhau qua \(Oy\).'))

G = lambda cfg, en, vi, hgt=300: GEO(sp_g9.auto_labels(cfg), cap=(en, vi), alt=(en, ''), height=hgt)
def pt(i, x, y, name=None, size=3): return {'type': 'point', 'id': i, 'at': [round(x, 4), round(y, 4)], 'name': i if name is None else name, 'style': {'size': size}}
def seg(a, b, **st): return {'type': 'segment', 'through': [a, b], 'style': st}
FIG1 = G({'view': [-3.4, 3.4, -0.9, 4.6], 'axes': True, 'steps': [{'type': 'curve', 'f': '0.5*x^2'}, pt('A', -2, 2), pt('B', -1, 0.5), pt('B1', 1, 0.5, name="B'"), pt('A1', 2, 2, name="A'")]},
         'Graph of y = (1/2)x²: a parabola above the x-axis, vertex O; A and A′, B and B′ are symmetric about Oy.', 'Đồ thị hàm số y = (1/2)x²: parabol nằm phía trên trục hoành, đỉnh O; A và A′, B và B′ đối xứng nhau qua Oy.')
FIG2 = G({'view': [-2.4, 2.4, -4.8, 0.9], 'axes': True, 'steps': [{'type': 'curve', 'f': '-2*x^2', 'style': {'strokeColor': '#c2410c'}}, pt('M', -1, -2), pt('M1', 1, -2, name="M'"), pt('N', -0.5, -0.5), pt('N1', 0.5, -0.5, name="N'")]},
         'Graph of y = −2x²: a parabola below the x-axis, vertex O (the highest point).', 'Đồ thị hàm số y = −2x²: parabol nằm phía dưới trục hoành, đỉnh O là điểm cao nhất.')
FIG3 = G({'view': [-4.2, 4.2, -5.4, 1.0], 'axes': True, 'steps': [{'type': 'curve', 'f': '-0.5*x^2'}, pt('A', -3, -4.5), pt('B', 3, -4.5), pt('I', 0, -4.5), pt('H', 2, -4.5), pt('K', 2, -2),
          seg('A', 'B', strokeWidth=3), seg('H', 'K', dash=True)]},
         'Arch y = −(1/2)x² with base AB = 6 m and height OI = 4.5 m; HK is the height of the arch above H.', 'Cổng y = −(1/2)x² có chân AB = 6 m, chiều cao OI = 4,5 m; HK là chiều cao của cổng tại H.', 280)

theory = '<h3>5.1 %s</h3>' % TI('The function and its table of values', 'Hàm số y = ax² và bảng giá trị')
theory += BOX('blue', ('Definition', 'Khái niệm'),
  T(r'A function given by \(y=ax^2\) with \(a\ne0\) is defined for every real \(x\); \(a\) is its coefficient. Example: the area of a square, \(S=a^2\); the distance fallen, \(s=4.9t^2\).', r'Hàm số cho bởi công thức \(y=ax^2\) với \(a\ne0\) xác định với mọi số thực \(x\); \(a\) là hệ số. Ví dụ: diện tích hình vuông \(S=a^2\); quãng đường rơi tự do \(s=4{,}9t^2\).'))
theory += TABLE([('\\(x\\)', '\\(x\\)')] + [('\\(%d\\)' % v, '\\(%d\\)' % v) for v in (-2, -1, 0, 1, 2)],
  [[TI('\\(y=\\dfrac12x^2\\)', '\\(y=\\dfrac12x^2\\)'), '\\(2\\)', '\\(\\dfrac12\\)', '\\(0\\)', '\\(\\dfrac12\\)', '\\(2\\)']])
theory += '<h3>5.2 %s</h3>' % TI('The graph', 'Đồ thị của hàm số y = ax² (a ≠ 0)')
theory += FIG1
theory += BOX('mint', ('Properties', 'Tính chất'),
  T(r'The graph of \(y=ax^2\) is a curve called a <b>parabola</b> with vertex \(O\); it is symmetric about \(Oy\).', r'Đồ thị hàm số \(y=ax^2\) là một đường cong gọi là [[parabol]], có đỉnh \(O\) và nhận \(Oy\) làm trục đối xứng.'),
  T(r'If \(a\gt0\), the graph lies above the \(x\)-axis and \(O\) is its lowest point. If \(a\lt0\), it lies below the \(x\)-axis and \(O\) is its highest point.', r'Nếu \(a\gt0\), đồ thị nằm phía trên trục hoành, \(O\) là điểm thấp nhất. Nếu \(a\lt0\), đồ thị nằm phía dưới trục hoành, \(O\) là điểm cao nhất.'))
theory += FIG2
theory += BOX('yellow', ('Drawing the graph', 'Cách vẽ đồ thị'),
  T(r'Make a table of values (\(x=0;\ \pm1;\ \pm2\)), plot the points, and join them with a smooth curve symmetric about \(Oy\).', r'Lập bảng giá trị (\(x=0;\ \pm1;\ \pm2\)), biểu diễn các điểm trên mặt phẳng tọa độ rồi nối bằng một đường cong trơn đối xứng qua \(Oy\).'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Table of values', 'Lập bảng giá trị'),
  T(r'Complete the table of values of \(y=\dfrac12x^2\) for \(x=-2;\ -1;\ 0;\ 1;\ 2\) and name the points of the graph.', r'Lập bảng giá trị của hàm số \(y=\dfrac12x^2\) với \(x=-2;\ -1;\ 0;\ 1;\ 2\) và chỉ ra các điểm tương ứng của đồ thị.'),
  ('Square \\(x\\) first, then multiply by \\(\\dfrac12\\).', 'Bình phương \\(x\\) trước rồi nhân với \\(\\dfrac12\\).'),
  [T(r'\(y=2;\ \dfrac12;\ 0;\ \dfrac12;\ 2\).', r'\(y=2;\ \dfrac12;\ 0;\ \dfrac12;\ 2\).'),
   T(r'Points: \(A(-2;\,2)\), \(B\left(-1;\,\dfrac12\right)\), \(O(0;\,0)\), \(B^{\prime}\left(1;\,\dfrac12\right)\), \(A^{\prime}(2;\,2)\) (see the first graph).', r'Các điểm: \(A(-2;\,2)\), \(B\left(-1;\,\dfrac12\right)\), \(O(0;\,0)\), \(B^{\prime}\left(1;\,\dfrac12\right)\), \(A^{\prime}(2;\,2)\) (xem đồ thị thứ nhất).')],
  T(r'\(2;\ \dfrac12;\ 0;\ \dfrac12;\ 2\).', r'\(2;\ \dfrac12;\ 0;\ \dfrac12;\ 2\).'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Points with a given ordinate', 'Điểm có tung độ cho trước'),
  T(r'For \(y=-2x^2\): a) describe its graph; b) find the points of the graph whose ordinate is \(-\dfrac12\) and describe their symmetry.', r'Cho hàm số \(y=-2x^2\). a) Nêu đặc điểm đồ thị. b) Tìm các điểm thuộc đồ thị có tung độ bằng \(-\dfrac12\) và nhận xét về tính đối xứng của chúng.'),
  ('\\(a=-2\\lt0\\).', '\\(a=-2\\lt0\\).'),
  [T(r'a) \(a=-2\lt0\): a parabola below the \(x\)-axis, vertex \(O\) is the highest point, symmetric about \(Oy\).', r'a) \(a=-2\lt0\): parabol nằm phía dưới trục hoành, đỉnh \(O\) là điểm cao nhất, nhận \(Oy\) làm trục đối xứng.'),
   T(r'b) \(-2x^2=-\dfrac12\Rightarrow x^2=\dfrac14\Rightarrow x=\pm\dfrac12\). Points \(N\left(-\dfrac12;\,-\dfrac12\right)\), \(N^{\prime}\left(\dfrac12;\,-\dfrac12\right)\): symmetric about \(Oy\).', r'b) \(-2x^2=-\dfrac12\Rightarrow x^2=\dfrac14\Rightarrow x=\pm\dfrac12\). Hai điểm \(N\left(-\dfrac12;\,-\dfrac12\right)\), \(N^{\prime}\left(\dfrac12;\,-\dfrac12\right)\) đối xứng nhau qua \(Oy\).')],
  T(r'\(\left(\pm\dfrac12;\,-\dfrac12\right)\).', r'\(\left(\pm\dfrac12;\,-\dfrac12\right)\).'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('Finding the coefficient', 'Tìm hệ số a'),
  T(r'The parabola \(y=ax^2\) passes through \((2;\,2)\). a) Find \(a\). b) Find the ordinate of its point with abscissa \(-2\). c) Find its points with ordinate 8.', r'Parabol \(y=ax^2\) đi qua điểm \((2;\,2)\). a) Tìm \(a\). b) Tìm tung độ của điểm thuộc parabol có hoành độ \(-2\). c) Tìm các điểm thuộc parabol có tung độ bằng 8.'),
  ('Substitute \\(x=2\\), \\(y=2\\).', 'Thay \\(x=2\\), \\(y=2\\).'),
  [T(r'a) \(2=a\cdot2^2\Rightarrow a=\dfrac12\). b) \(y=\dfrac12\cdot(-2)^2=2\).', r'a) \(2=a\cdot2^2\Rightarrow a=\dfrac12\). b) \(y=\dfrac12\cdot(-2)^2=2\).'),
   T(r'c) \(\dfrac12x^2=8\Rightarrow x^2=16\Rightarrow x=\pm4\): points \((-4;\,8)\) and \((4;\,8)\).', r'c) \(\dfrac12x^2=8\Rightarrow x^2=16\Rightarrow x=\pm4\): hai điểm \((-4;\,8)\) và \((4;\,8)\).')],
  T(r'\(a=\dfrac12\); 2; \((\pm4;\,8)\).', r'\(a=\dfrac12\); 2; \((\pm4;\,8)\).'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('A parabolic arch', 'Cổng hình parabol'),
  T(r'An arch has the shape of the parabola \(y=ax^2\) (top at \(O\)). Its base \(AB\) is 6 m wide and its height \(OI\) is 4.5 m. a) Find \(a\). b) \(H\) lies on the base 2 m from \(I\); find the height \(HK\) of the arch above \(H\). c) Can a truck 2 m wide and 3 m high pass through the middle?', r'Một cổng có dạng parabol \(y=ax^2\) (đỉnh cổng là \(O\)). Chân cổng \(AB\) rộng 6 m, chiều cao \(OI\) là 4,5 m. a) Tìm \(a\). b) Điểm \(H\) trên chân cổng cách \(I\) 2 m; tính chiều cao \(HK\) của cổng tại \(H\). c) Một xe tải rộng 2 m, cao 3 m đi vào chính giữa cổng có qua được không?') + FIG3,
  ('\\(B(3;\\,-4{,}5)\\) lies on the parabola.', '\\(B(3;\\,-4{,}5)\\) thuộc parabol.'),
  [T(r'a) \(-4.5=a\cdot3^2\Rightarrow a=-\dfrac12\).', r'a) \(-4{,}5=a\cdot3^2\Rightarrow a=-\dfrac12\).'),
   T(r'b) \(K(2;\,y_K)\) with \(y_K=-\dfrac12\cdot2^2=-2\), so \(HK=4.5-2=2.5\) m.', r'b) \(K(2;\,y_K)\) với \(y_K=-\dfrac12\cdot2^2=-2\) nên \(HK=4{,}5-2=2{,}5\) m.'),
   T(r'c) The edge of the truck is at \(x=1\): the arch there is \(4.5-\dfrac12\cdot1^2=4\) m high \(\gt3\) m. The truck can pass.', r'c) Mép xe ở \(x=1\): cổng tại đó cao \(4{,}5-\dfrac12\cdot1^2=4\) m \(\gt3\) m. Xe qua được.')],
  T(r'\(a=-\dfrac12\); \(HK=2.5\) m; yes.', r'\(a=-\dfrac12\); \(HK=2{,}5\) m; qua được.'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('A suspension bridge', 'Cầu treo'),
  T(r'A suspension bridge has two towers 75 m high and 400 m apart. Its cable has the shape of a parabola \(y=ax^2\) with its lowest point at \(O\) (on the road, midway between the towers). Find the height of the cable at a point 100 m from the center.', r'Một cây cầu treo có hai trụ cao 75 m, cách nhau 400 m. Dây cáp có dạng parabol \(y=ax^2\) với điểm thấp nhất là \(O\) (trên mặt cầu, chính giữa hai trụ). Tính chiều cao của dây cáp tại điểm cách tâm 100 m.'),
  ('The top of a tower is the point \\((200;\\,75)\\).', 'Đỉnh trụ là điểm \\((200;\\,75)\\).'),
  [T(r'\(75=a\cdot200^2\Rightarrow a=\dfrac{75}{40000}=\dfrac{3}{1600}\).', r'\(75=a\cdot200^2\Rightarrow a=\dfrac{75}{40000}=\dfrac{3}{1600}\).'),
   T(r'At \(x=100\): \(y=\dfrac{3}{1600}\cdot100^2=18.75\) m.', r'Tại \(x=100\): \(y=\dfrac{3}{1600}\cdot100^2=18{,}75\) m.')],
  T(r'18.75 m.', r'18,75 m.'))

_SETS = sp_g9.BANK(sp_g9.L18_GROUPS, start=1, seeds=(2801, 2802, 2803))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Squaring a negative number.</b> \((-3)^2=9\), so for \(y=2x^2\), \(y(-3)=18\), not \(-18\).', r'<b>Bình phương số âm.</b> \((-3)^2=9\) nên với \(y=2x^2\) thì \(y(-3)=18\), không phải \(-18\).'),
 (r'<b>Only one point.</b> For a given ordinate there are usually two points \((\pm x_0;\,y_0)\).', r'<b>Chỉ tìm một điểm.</b> Với một tung độ cho trước thường có hai điểm \((\pm x_0;\,y_0)\).'),
 (r'<b>Joining points with straight segments.</b> The graph is a smooth curve, not a broken line.', r'<b>Nối các điểm bằng đoạn thẳng.</b> Đồ thị là đường cong trơn, không phải đường gấp khúc.'),
 (r'<b>Wrong side.</b> \(a\lt0\): the parabola lies below the \(x\)-axis.', r'<b>Sai vị trí.</b> \(a\lt0\): parabol nằm phía dưới trục hoành.')]
summary = [
 (r'\(y=ax^2\ (a\ne0)\) is defined for every \(x\); its graph is a parabola with vertex \(O\), symmetric about \(Oy\).', r'\(y=ax^2\ (a\ne0)\) xác định với mọi \(x\); đồ thị là parabol đỉnh \(O\), nhận \(Oy\) làm trục đối xứng.'),
 (r'\(a\gt0\): above \(Ox\), lowest point \(O\); \(a\lt0\): below \(Ox\), highest point \(O\).', r'\(a\gt0\): nằm trên trục hoành, \(O\) thấp nhất; \(a\lt0\): nằm dưới trục hoành, \(O\) cao nhất.'),
 (r'\(M(x_0;\,y_0)\) is on the graph \(\iff y_0=ax_0^2\).', r'\(M(x_0;\,y_0)\) thuộc đồ thị \(\iff y_0=ax_0^2\).'),
 (r'Key English: parabola, vertex, table of values, abscissa, ordinate, symmetric about, graph.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[parabol]], [[đỉnh (của parabol)]], [[bảng giá trị]], [[hoành độ]], [[tung độ]], [[đối xứng nhau qua]], [[đồ thị (của hàm số)]].')]
checks = [
 (r'I can make a table of values of \(y=ax^2\).', r'Em lập được bảng giá trị của hàm số \(y=ax^2\).'),
 (r'I can describe and draw the graph.', r'Em mô tả và vẽ được đồ thị.'),
 (r'I can find \(a\) or the points of the graph from given data.', r'Em tìm được \(a\) hoặc các điểm thuộc đồ thị từ dữ kiện.'),
 (r'I can solve problems with parabolic arches and bridges.', r'Em giải được bài toán cổng parabol, cầu treo.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='The Function y = ax² (a ≠ 0)', title_vi='Hàm số y = ax² (a ≠ 0)', topic=TOPIC,
       folder='quadratic-functions-equations', file='function-y-ax2', catalog_title_vi='Hàm số y = ax² (a ≠ 0)',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='The function y = ax², its table of values and its graph, a parabola with vertex O.', level='Intermediate', minutes=75,
       description_vi='Bài 18 – Hàm số y = ax² (a ≠ 0); bảng giá trị; đồ thị là parabol đỉnh O; bài toán thực tế.',
       tags_vi=['hàm số bậc hai', 'parabol', 'đồ thị'], prerequisites=[], tags=['quadratic function', 'parabola', 'graph'], order=180)
