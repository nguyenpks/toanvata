# -*- coding: utf-8 -*-
"""Nội dung g12-deriv-app-02, g12-antider-01, g12-antider-02 – CHỈ NỘI DUNG. Bố cục, số mục, tên mục, số lớp do config/model.json quyết định."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *

# ---- Bài tập riêng từng mức: Mức 1 giữ bộ cũ; Mức 2 và Mức 3 là bộ mới, cùng dạng, khác số liệu ----
# Chuỗi 'tiếng Anh§tiếng Việt'; nếu không có § thì dùng chung cho cả hai ngôn ngữ.
def _p(s): return tuple(s.split('§')) if '§' in s else (s, s)
def _m(n, q, o, a, x, raw=False):
    xe, xv = _p(x); return MCQ(n, _p(q), o, a, ('Answer: %s. %s' % (a, xe), 'Đáp án %s. %s' % (a, xv)), raw=raw)
def _t(n, q, a, x):
    xe, xv = _p(x); return TF(n, _p(q), a, (('True. ' if a == 'true' else 'False. ') + xe, ('Đúng. ' if a == 'true' else 'Sai. ') + xv))
_H = {'n': ('Enter a number.', 'Nhập một số.'), 'w': ('Enter a whole number.', 'Nhập một số nguyên.'),
      'f': ('Enter a number or a fraction, for example -1/2.', 'Nhập một số hoặc phân số, ví dụ -1/2.'),
      'd': ('Enter a number, for example 3.5.', 'Nhập một số, ví dụ 3.5.'),
      'i': ('Format: (-inf,3). You may type inf for infinity.', 'Định dạng: (-inf,3). Có thể gõ inf cho vô cực.')}
def _s(n, q, a, shown, kind, x):
    xe, xv = _p(x); return SHORT(n, _p(q), a, 'interval' if kind == 'i' else 'number', _H[kind], ('Answer: %s. %s' % (shown, xe), 'Đáp án: %s. %s' % (shown, xv)))

ensure_vocab([
 ('v-sketching','sketching a graph','khảo sát và vẽ đồ thị','Applications of Derivatives','Sketch the graph of the function.',''),
 ('v-even-function','even function','hàm số chẵn','Applications of Derivatives','An even function is symmetric about the y-axis.',''),
 ('v-odd-function','odd function','hàm số lẻ','Applications of Derivatives','An odd function is symmetric about the origin.',''),
 ('v-center-symmetry','center of symmetry','tâm đối xứng','Applications of Derivatives','The center of symmetry is (-1, 2).',''),
 ('v-intercept','intercept','giao điểm với trục','Applications of Derivatives','Find the x-intercepts.',''),
 ('v-antiderivative','antiderivative','nguyên hàm','Antiderivatives','F is an antiderivative of f.','\\(\\int f(x)\\,dx\\)'),
 ('v-constant-integration','constant of integration','hằng số tích phân','Antiderivatives','Do not forget the constant C.','\\(C\\)'),
 ('v-initial-condition','initial condition','điều kiện ban đầu','Antiderivatives','Use the initial condition F(1) = 4.',''),
 ('v-substitution','substitution','phép đổi biến','Antiderivatives','Use the substitution u = x^2 + 1.',''),
 ('v-integration-parts','integration by parts','nguyên hàm từng phần','Antiderivatives','Use integration by parts.',''),
 ('v-linear-expression','linear expression','biểu thức bậc nhất','Antiderivatives','Replace x by the linear expression ax + b.',''),
])
load_vocab()
CAT1 = ('Applications of Derivatives', 'Ứng dụng đạo hàm'); CAT3 = ('Antiderivatives', 'Nguyên hàm')

# ========================= g12-deriv-app-02 =========================
f1 = lambda x: (x - 1) ** 2 * (x + 2)
f2 = lambda x: x ** 4 - 2 * x ** 2
f3 = lambda x: (2 * x - 1) / (x + 1)
f4 = lambda x: x + 1 / (x - 1)
fig = lambda f, xr, yr, **k: FIG(svg_graph(f, xr, yr, **k), '', '', 'Graph of the function', '')
def FG(f, xr, yr, cap, **k): return FIG(svg_graph(f, xr, yr, **k), cap[0], cap[1], cap[0].replace('\\(', '').replace('\\)', ''), '')

review = (T('To sketch a graph you combine four earlier skills: the <b>domain</b>, the sign of the derivative, limits and <b>asymptotes</b>, and values at special points.', 'Để vẽ đồ thị, ta kết hợp bốn kĩ năng đã học: [[tập xác định]], dấu của [[đạo hàm]], giới hạn và [[đường tiệm cận]], cùng giá trị tại các điểm đặc biệt.') +
  T('A function is <b>even</b> if \\(f(-x)=f(x)\\) and <b>odd</b> if \\(f(-x)=-f(x)\\) for every \\(x\\) in a domain that is symmetric about 0.', 'Hàm số là [[hàm số chẵn]] nếu \\(f(-x)=f(x)\\) và [[hàm số lẻ]] nếu \\(f(-x)=-f(x)\\) với mọi \\(x\\) thuộc tập xác định đối xứng qua 0.'))
theory = ('<h3>5.1 %s</h3>' % TI('Steps for sketching a graph', 'Các bước khảo sát và vẽ đồ thị') +
  OL([T('Find the domain. Check whether the function is even, odd or neither.', 'Tìm [[tập xác định]]. Xét hàm số chẵn, lẻ hay không.'),
      T('Compute \\(f\'(x)\\); find the sign of \\(f\'\\), the intervals of increase and decrease, and the extrema.', 'Tính \\(f\'(x)\\); xét dấu \\(f\'\\), các khoảng đồng biến, nghịch biến và [[cực trị]].'),
      T('Find the limits at the ends of the domain and the asymptotes.', 'Tìm các giới hạn ở hai đầu tập xác định và các tiệm cận.'),
      T('Make a variation table.', 'Lập [[bảng biến thiên]].'),
      T('Find the <b>intercepts</b> with the axes and a few more points.', 'Tìm [[giao điểm với trục]] và vài điểm bổ sung.'),
      T('Draw the graph, showing asymptotes with dashed lines.', 'Vẽ đồ thị, vẽ tiệm cận bằng nét đứt.')]) +
  '<h3>5.2 %s</h3>' % TI('Symmetry', 'Tính đối xứng') +
  UL([T('The graph of an even function is symmetric about the y-axis.', 'Đồ thị hàm số chẵn đối xứng qua trục tung.'), T('The graph of an odd function is symmetric about the origin.', 'Đồ thị hàm số lẻ đối xứng qua gốc tọa độ.')]) +
  '<h3>5.3 %s</h3>' % TI('Three common types', 'Ba dạng hàm thường gặp') +
  UL([T('Cubic \\(y=ax^3+bx^2+cx+d\\): at most two extreme points; the graph is symmetric about a <b>center of symmetry</b>.', 'Hàm bậc ba \\(y=ax^3+bx^2+cx+d\\): có tối đa hai điểm cực trị; đồ thị có một [[tâm đối xứng]].'),
      T('Quartic \\(y=ax^4+bx^2+c\\): even function, with one or three extreme points.', 'Hàm trùng phương \\(y=ax^4+bx^2+c\\): là hàm chẵn, có một hoặc ba điểm cực trị.'),
      T('\\(y=\\dfrac{ax+b}{cx+d}\\) with \\(ad-bc\\ne0\\): \\(y\'=\\dfrac{ad-bc}{(cx+d)^2}\\) has a constant sign; the asymptotes are \\(x=-\\dfrac dc\\) and \\(y=\\dfrac ac\\), and their intersection is the center of symmetry.', '\\(y=\\dfrac{ax+b}{cx+d}\\) với \\(ad-bc\\ne0\\): \\(y\'=\\dfrac{ad-bc}{(cx+d)^2}\\) có dấu không đổi; các tiệm cận là \\(x=-\\dfrac dc\\) và \\(y=\\dfrac ac\\), giao điểm của chúng là tâm đối xứng.')]))
ex = EXAMPLE(1, ('Basic', 'Cơ bản'), ('A cubic function', 'Hàm số bậc ba'),
  T('Sketch the graph of \\(y=x^3-3x+2=(x-1)^2(x+2)\\).', 'Khảo sát và vẽ đồ thị \\(y=x^3-3x+2=(x-1)^2(x+2)\\).'),
  ('The domain is \\(\\mathbb{R}\\). Use \\(y\'\\) to find the extrema, then the intercepts.', 'Tập xác định là \\(\\mathbb{R}\\). Dùng \\(y\'\\) tìm cực trị, rồi tìm giao điểm với trục.'),
  [T('\\(y\'=3x^2-3=3(x-1)(x+1)\\). Increasing on \\((-\\infty,-1)\\) and \\((1,+\\infty)\\); decreasing on \\((-1,1)\\).', '\\(y\'=3x^2-3=3(x-1)(x+1)\\). Đồng biến trên \\((-\\infty,-1)\\) và \\((1,+\\infty)\\); nghịch biến trên \\((-1,1)\\).'),
   T('Local maximum \\(y(-1)=4\\); local minimum \\(y(1)=0\\). Limits: \\(y\\to\\pm\\infty\\) as \\(x\\to\\pm\\infty\\).', 'Cực đại \\(y(-1)=4\\); cực tiểu \\(y(1)=0\\). Giới hạn: \\(y\\to\\pm\\infty\\) khi \\(x\\to\\pm\\infty\\).'),
   T('Intercepts: \\(y(0)=2\\); \\(y=0\\) at \\(x=-2\\) and \\(x=1\\) (a double root, so the graph touches the x-axis).', 'Giao điểm: \\(y(0)=2\\); \\(y=0\\) tại \\(x=-2\\) và \\(x=1\\) (nghiệm kép nên đồ thị tiếp xúc trục hoành).'),
   FG(f1, (-3, 3), (-3, 6), ('The graph of \\(y=x^3-3x+2\\).', 'Đồ thị của \\(y=x^3-3x+2\\).'), label_pts=[(-1, 4, ''), (1, 0, '')])],
  'max \\((-1,4)\\), min \\((1,0)\\), passes through \\((-2,0)\\), \\((0,2)\\)')
ex += EXAMPLE(2, ('Intermediate', 'Trung bình'), ('An even quartic function', 'Hàm trùng phương (hàm chẵn)'),
  T('Sketch the graph of \\(y=x^4-2x^2\\).', 'Khảo sát và vẽ đồ thị \\(y=x^4-2x^2\\).'),
  ('The function is even, so the graph is symmetric about the y-axis.', 'Hàm số chẵn nên đồ thị đối xứng qua trục tung.'),
  [T('\\(y(-x)=y(x)\\): even. \\(y\'=4x(x^2-1)\\), zero at \\(x=0,\\pm1\\).', '\\(y(-x)=y(x)\\): hàm chẵn. \\(y\'=4x(x^2-1)\\), bằng 0 tại \\(x=0,\\pm1\\).'),
   T('Local minima \\(y(\\pm1)=-1\\); local maximum \\(y(0)=0\\).', 'Cực tiểu \\(y(\\pm1)=-1\\); cực đại \\(y(0)=0\\).'),
   T('The x-intercepts are \\(x=0\\) and \\(x=\\pm\\sqrt2\\).', 'Giao điểm với trục hoành: \\(x=0\\) và \\(x=\\pm\\sqrt2\\).'),
   FG(f2, (-2, 2), (-2, 3), ('The graph of \\(y=x^4-2x^2\\).', 'Đồ thị của \\(y=x^4-2x^2\\).'), label_pts=[(-1, -1, ''), (1, -1, ''), (0, 0, '')])],
  'min \\((\\pm1,-1)\\), max \\((0,0)\\)')
ex += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('A rational function', 'Hàm phân thức bậc nhất'),
  T('Sketch the graph of \\(y=\\dfrac{2x-1}{x+1}\\).', 'Khảo sát và vẽ đồ thị \\(y=\\dfrac{2x-1}{x+1}\\).'),
  ('Here \\(ad-bc=2\\cdot1-(-1)\\cdot1=3>0\\).', 'Ở đây \\(ad-bc=2\\cdot1-(-1)\\cdot1=3>0\\).'),
  [T('Domain \\(x\\ne-1\\). \\(y\'=\\dfrac{3}{(x+1)^2}>0\\): increasing on each of \\((-\\infty,-1)\\) and \\((-1,+\\infty)\\), no extrema.', 'Tập xác định \\(x\\ne-1\\). \\(y\'=\\dfrac{3}{(x+1)^2}>0\\): đồng biến trên từng khoảng \\((-\\infty,-1)\\) và \\((-1,+\\infty)\\), không có cực trị.'),
   T('Asymptotes: \\(x=-1\\) (vertical) and \\(y=2\\) (horizontal). The center of symmetry is \\((-1,2)\\).', 'Tiệm cận: \\(x=-1\\) (đứng) và \\(y=2\\) (ngang). Tâm đối xứng là \\((-1,2)\\).'),
   T('Intercepts: \\(y(0)=-1\\); \\(y=0\\) at \\(x=\\tfrac12\\).', 'Giao điểm: \\(y(0)=-1\\); \\(y=0\\) tại \\(x=\\tfrac12\\).'),
   FG(f3, (-5, 4), (-4, 7), ('The graph of \\(y=\\dfrac{2x-1}{x+1}\\).', 'Đồ thị của \\(y=\\dfrac{2x-1}{x+1}\\).'), vlines=[-1], hlines=[2])],
  'asymptotes \\(x=-1\\), \\(y=2\\); center \\((-1,2)\\)')
ex += EXAMPLE(4, ('Advanced', 'Nâng cao'), ('An oblique asymptote', 'Có tiệm cận xiên'),
  T('Sketch the graph of \\(y=\\dfrac{x^2-x+1}{x-1}\\).', 'Khảo sát và vẽ đồ thị \\(y=\\dfrac{x^2-x+1}{x-1}\\).'),
  ('Divide first: \\(y=x+\\dfrac{1}{x-1}\\).', 'Chia đa thức trước: \\(y=x+\\dfrac{1}{x-1}\\).'),
  [T('Domain \\(x\\ne1\\). \\(y\'=1-\\dfrac{1}{(x-1)^2}=\\dfrac{x(x-2)}{(x-1)^2}\\), zero at \\(x=0\\) and \\(x=2\\).', 'Tập xác định \\(x\\ne1\\). \\(y\'=1-\\dfrac{1}{(x-1)^2}=\\dfrac{x(x-2)}{(x-1)^2}\\), bằng 0 tại \\(x=0\\) và \\(x=2\\).'),
   T('Local maximum \\(y(0)=-1\\); local minimum \\(y(2)=3\\). Increasing on \\((-\\infty,0)\\) and \\((2,+\\infty)\\); decreasing on \\((0,1)\\) and \\((1,2)\\).', 'Cực đại \\(y(0)=-1\\); cực tiểu \\(y(2)=3\\). Đồng biến trên \\((-\\infty,0)\\) và \\((2,+\\infty)\\); nghịch biến trên \\((0,1)\\) và \\((1,2)\\).'),
   T('Asymptotes: \\(x=1\\) (vertical) and \\(y=x\\) (oblique).', 'Tiệm cận: \\(x=1\\) (đứng) và \\(y=x\\) (xiên).'),
   FG(f4, (-3, 5), (-5, 7), ('The graph of \\(y=\\dfrac{x^2-x+1}{x-1}\\).', 'Đồ thị của \\(y=\\dfrac{x^2-x+1}{x-1}\\).'), vlines=[1], lines=[(1, 0, 'y = x')], label_pts=[(0, -1, ''), (2, 3, '')])],
  'max \\((0,-1)\\), min \\((2,3)\\); asymptotes \\(x=1\\), \\(y=x\\)')
Q = lambda *a: a
pr = [(('A. Multiple Choice', 'A. Trắc nghiệm nhiều lựa chọn'), [
  MCQ(1, ('Where is the local minimum point of \\(y=x^3-3x^2\\)?', 'Điểm cực tiểu của đồ thị \\(y=x^3-3x^2\\) là điểm nào?'), ['(0,0)', '(2,-4)', '(-2,-20)', '(1,-2)'], 'b', ('Answer: b. \\(y\'=3x(x-2)\\); the sign changes from \\(-\\) to \\(+\\) at \\(x=2\\), and \\(y(2)=8-12=-4\\).', 'Đáp án b. \\(y\'=3x(x-2)\\); dấu đổi từ \\(-\\) sang \\(+\\) tại \\(x=2\\), và \\(y(2)=8-12=-4\\).')),
  MCQ(2, ('What is the center of symmetry of \\(y=\\dfrac{2x-1}{x+1}\\)?', 'Tâm đối xứng của đồ thị \\(y=\\dfrac{2x-1}{x+1}\\) là điểm nào?'), ['(-1,2)', '(2,-1)', '(1,-2)', '(-1,-2)'], 'a', ('Answer: a. It is the intersection of the asymptotes \\(x=-1\\) and \\(y=2\\).', 'Đáp án a. Đó là giao điểm của hai tiệm cận \\(x=-1\\) và \\(y=2\\).')),
  MCQ(3, ('What is the horizontal asymptote of \\(y=\\dfrac{3x+1}{x-2}\\)?', 'Tiệm cận ngang của đồ thị \\(y=\\dfrac{3x+1}{x-2}\\) là đường nào?'), ['y=3', 'y=2', 'y=-2', r'y=\frac13'], 'a', ('Answer: a. \\(y=\\dfrac ac=\\dfrac31=3\\).', 'Đáp án a. \\(y=\\dfrac ac=\\dfrac31=3\\).')),
  MCQ(4, ('What is the local maximum value of \\(y=x^3-3x+2\\)?', 'Giá trị cực đại của hàm số \\(y=x^3-3x+2\\) là bao nhiêu?'), ['4', '0', '2', '-4'], 'a', ('Answer: a. The maximum is at \\(x=-1\\): \\(-1+3+2=4\\).', 'Đáp án a. Cực đại tại \\(x=-1\\): \\(-1+3+2=4\\).'))]),
 (('B. True or False', 'B. Đúng hoặc sai'), [
  TF(5, ('True or false: the graph of \\(y=x^4-2x^2\\) is symmetric about the y-axis.', 'Đúng hay sai: đồ thị \\(y=x^4-2x^2\\) đối xứng qua trục tung.'), 'true', ('True. The function is even.', 'Đúng. Đây là hàm số chẵn.')),
  TF(6, ('True or false: the graph of \\(y=x^3\\) is symmetric about the y-axis.', 'Đúng hay sai: đồ thị \\(y=x^3\\) đối xứng qua trục tung.'), 'false', ('False. \\(y=x^3\\) is odd: its graph is symmetric about the origin.', 'Sai. \\(y=x^3\\) là hàm số lẻ: đồ thị đối xứng qua gốc tọa độ.'))]),
 (('C. Short Answer', 'C. Trả lời ngắn'), [
  SHORT(7, ('Find the y-intercept of \\(y=(x-1)^2(x+2)\\).', 'Tìm tung độ giao điểm của \\(y=(x-1)^2(x+2)\\) với trục tung.'), '2', 'number', ('Enter a number.', 'Nhập một số.'), ('Answer: 2. \\(y(0)=1\\cdot2=2\\).', 'Đáp án: 2. \\(y(0)=1\\cdot2=2\\).')),
  SHORT(8, ('How many different x-intercepts does \\(y=x^4-2x^2\\) have?', 'Đồ thị \\(y=x^4-2x^2\\) có bao nhiêu giao điểm phân biệt với trục hoành?'), '3', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'), ('Answer: 3. \\(x^2(x^2-2)=0\\) gives \\(x=0,\\pm\\sqrt2\\).', 'Đáp án: 3. \\(x^2(x^2-2)=0\\) cho \\(x=0,\\pm\\sqrt2\\).')),
  SHORT(9, ('Find the local minimum value of \\(y=\\dfrac{x^2-x+1}{x-1}\\) at \\(x=2\\).', 'Tìm giá trị cực tiểu của \\(y=\\dfrac{x^2-x+1}{x-1}\\) tại \\(x=2\\).'), '3', 'number', ('Enter a number.', 'Nhập một số.'), ('Answer: 3. \\(y(2)=\\dfrac{4-2+1}{1}=3\\).', 'Đáp án: 3. \\(y(2)=\\dfrac{4-2+1}{1}=3\\).')),
  SHORT(10, ('The graph of \\(y=\\dfrac{ax+1}{x-1}\\) has the center of symmetry \\((1,2)\\). Find \\(a\\).', 'Đồ thị \\(y=\\dfrac{ax+1}{x-1}\\) có tâm đối xứng \\((1,2)\\). Tìm \\(a\\).'), '2', 'number', ('Enter a number.', 'Nhập một số.'), ('Answer: 2. The horizontal asymptote is \\(y=a\\), so \\(a=2\\).', 'Đáp án: 2. Tiệm cận ngang là \\(y=a\\) nên \\(a=2\\).'))])]
S2 = [
 [_m(1, r'Where is the local minimum point of \(y=x^3-6x^2\)?§Điểm cực tiểu của đồ thị \(y=x^3-6x^2\) là điểm nào?', ['(0,0)', '(2,-16)', '(4,-32)', '(-4,-160)'], 'c',
      r'\(y′=3x(x-4)\); the sign changes from \(-\) to \(+\) at \(x=4\), and \(y(4)=64-96=-32\).§\(y′=3x(x-4)\); dấu đổi từ \(-\) sang \(+\) tại \(x=4\), và \(y(4)=64-96=-32\).'),
  _m(2, r'What is the center of symmetry of \(y=\dfrac{3x+2}{x-1}\)?§Tâm đối xứng của đồ thị \(y=\dfrac{3x+2}{x-1}\) là điểm nào?', ['(3,1)', '(-1,3)', '(1,-3)', '(1,3)'], 'd',
      r'It is the intersection of the asymptotes \(x=1\) and \(y=3\).§Đó là giao điểm của hai tiệm cận \(x=1\) và \(y=3\).'),
  _m(3, r'What is the horizontal asymptote of \(y=\dfrac{5x-2}{x+4}\)?§Tiệm cận ngang của đồ thị \(y=\dfrac{5x-2}{x+4}\) là đường nào?', ['y=-4', 'y=4', 'y=5', 'y=-2'], 'c',
      r'\(y=\dfrac ac=\dfrac51=5\).'),
  _m(4, r'What is the local maximum value of \(y=x^3-12x+5\)?§Giá trị cực đại của hàm số \(y=x^3-12x+5\) là bao nhiêu?', ['21', '-11', '5', '-21'], 'a',
      r'The maximum is at \(x=-2\): \(-8+24+5=21\).§Cực đại tại \(x=-2\): \(-8+24+5=21\).')],
 [_t(5, r'True or false: the graph of \(y=x^6-x^2\) is symmetric about the y-axis.§Đúng hay sai: đồ thị \(y=x^6-x^2\) đối xứng qua trục tung.', 'true',
      r'The function is even.§Đây là hàm số chẵn.'),
  _t(6, r'True or false: the graph of \(y=x^3-x\) is symmetric about the y-axis.§Đúng hay sai: đồ thị \(y=x^3-x\) đối xứng qua trục tung.', 'false',
      r'\(y=x^3-x\) is odd: its graph is symmetric about the origin.§\(y=x^3-x\) là hàm số lẻ: đồ thị đối xứng qua gốc tọa độ.')],
 [_s(7, r'Find the y-intercept of \(y=(x+1)^2(x-3)\).§Tìm tung độ giao điểm của \(y=(x+1)^2(x-3)\) với trục tung.', '-3', r'\(-3\)', 'n',
      r'\(y(0)=1\cdot(-3)=-3\).'),
  _s(8, r'How many different x-intercepts does \(y=x^4-5x^2+4\) have?§Đồ thị \(y=x^4-5x^2+4\) có bao nhiêu giao điểm phân biệt với trục hoành?', '4', '4', 'w',
      r'\((x^2-1)(x^2-4)=0\) gives \(x=\pm1,\pm2\).§\((x^2-1)(x^2-4)=0\) cho \(x=\pm1,\pm2\).'),
  _s(9, r'Find the local minimum value of \(y=\dfrac{x^2-2x+4}{x-2}\) at \(x=4\).§Tìm giá trị cực tiểu của \(y=\dfrac{x^2-2x+4}{x-2}\) tại \(x=4\).', '6', '6', 'n',
      r'\(y(4)=\dfrac{16-8+4}{2}=6\).'),
  _s(10, r'The graph of \(y=\dfrac{ax-1}{x+2}\) has the center of symmetry \((-2,3)\). Find \(a\).§Đồ thị \(y=\dfrac{ax-1}{x+2}\) có tâm đối xứng \((-2,3)\). Tìm \(a\).', '3', '3', 'n',
      r'The horizontal asymptote is \(y=a\), so \(a=3\).§Tiệm cận ngang là \(y=a\) nên \(a=3\).')]]
S3 = [
 [_m(1, r'Where is the local minimum point of \(y=x^3-12x\)?§Điểm cực tiểu của đồ thị \(y=x^3-12x\) là điểm nào?', ['(2,-16)', '(-2,16)', '(0,0)', '(4,16)'], 'a',
      r'\(y′=3x^2-12\); the sign changes from \(-\) to \(+\) at \(x=2\), and \(y(2)=8-24=-16\).§\(y′=3x^2-12\); dấu đổi từ \(-\) sang \(+\) tại \(x=2\), và \(y(2)=8-24=-16\).'),
  _m(2, r'What is the center of symmetry of \(y=\dfrac{4x+1}{x+3}\)?§Tâm đối xứng của đồ thị \(y=\dfrac{4x+1}{x+3}\) là điểm nào?', ['(3,4)', '(4,-3)', '(-3,4)', '(-3,-4)'], 'c',
      r'It is the intersection of the asymptotes \(x=-3\) and \(y=4\).§Đó là giao điểm của hai tiệm cận \(x=-3\) và \(y=4\).'),
  _m(3, r'What is the horizontal asymptote of \(y=\dfrac{2x+7}{3x-1}\)?§Tiệm cận ngang của đồ thị \(y=\dfrac{2x+7}{3x-1}\) là đường nào?', [r'y=\frac32', 'y=2', r'y=-\frac13', r'y=\frac23'], 'd',
      r'\(y=\dfrac ac=\dfrac23\).'),
  _m(4, r'What is the local maximum value of \(y=-x^3+3x+1\)?§Giá trị cực đại của hàm số \(y=-x^3+3x+1\) là bao nhiêu?', ['-1', '1', '5', '3'], 'd',
      r'\(y′=-3x^2+3=0\) at \(x=\pm1\). The maximum is at \(x=1\): \(-1+3+1=3\).§\(y′=-3x^2+3=0\) tại \(x=\pm1\). Cực đại tại \(x=1\): \(-1+3+1=3\).')],
 [_t(5, r'True or false: the graph of \(y=-x^4+4x^2\) is symmetric about the y-axis.§Đúng hay sai: đồ thị \(y=-x^4+4x^2\) đối xứng qua trục tung.', 'true',
      r'The function is even.§Đây là hàm số chẵn.'),
  _t(6, r'True or false: the graph of \(y=x^3+2x\) is symmetric about the y-axis.§Đúng hay sai: đồ thị \(y=x^3+2x\) đối xứng qua trục tung.', 'false',
      r'\(y=x^3+2x\) is odd: its graph is symmetric about the origin.§\(y=x^3+2x\) là hàm số lẻ: đồ thị đối xứng qua gốc tọa độ.')],
 [_s(7, r'Find the y-intercept of \(y=(x-2)^2(x+1)\).§Tìm tung độ giao điểm của \(y=(x-2)^2(x+1)\) với trục tung.', '4', '4', 'n',
      r'\(y(0)=4\cdot1=4\).'),
  _s(8, r'How many different x-intercepts does \(y=x^4+x^2-2\) have?§Đồ thị \(y=x^4+x^2-2\) có bao nhiêu giao điểm phân biệt với trục hoành?', '2', '2', 'w',
      r'\((x^2+2)(x^2-1)=0\) gives only \(x=\pm1\), because \(x^2+2>0\).§\((x^2+2)(x^2-1)=0\) chỉ cho \(x=\pm1\) vì \(x^2+2>0\).'),
  _s(9, r'Find the local minimum value of \(y=\dfrac{x^2-4x+9}{x-4}\) at \(x=7\).§Tìm giá trị cực tiểu của \(y=\dfrac{x^2-4x+9}{x-4}\) tại \(x=7\).', '10', '10', 'n',
      r'\(y(7)=\dfrac{49-28+9}{3}=10\).'),
  _s(10, r'The graph of \(y=\dfrac{ax+2}{x-3}\) has the center of symmetry \((3,4)\). Find \(a\).§Đồ thị \(y=\dfrac{ax+2}{x-3}\) có tâm đối xứng \((3,4)\). Tìm \(a\).', '4', '4', 'n',
      r'The horizontal asymptote is \(y=a\), so \(a=4\).§Tiệm cận ngang là \(y=a\) nên \(a=4\).')]]
_T = [t for t, _ in pr]
S1 = [g for _, g in pr]
pr = LEVEL_PRACTICE(_T, {1: S1, 2: S2, 3: S3})
import sp_g12 as _spg
from mb_selfpractice import SELF as _SELF
_sf = _SELF(_spg.M4S, start=11, avoid=[t[1] for t in pr])
pr = pr + [(('%s. Self-practice: Multiple Choice' % chr(ord('A') + len({t[0][0][0] for t in pr})), '%s. Tự luyện: trắc nghiệm' % chr(ord('A') + len({t[0][0][0] for t in pr}))), _sf[lv], [lv]) for lv in (1, 2, 3)]
pr.sort(key=lambda t: t[2][0])

build('g12-deriv-app-02', 'Sketching Graphs of Functions', 'Khảo sát và vẽ đồ thị hàm số', CAT1,
  {'level': ('Intermediate', 'Trung bình'), 'time': ('about 60 minutes', 'khoảng 60 phút'), 'before': ('asymptotes, monotonicity, extrema', 'tiệm cận, tính đơn điệu, cực trị')},
  [('follow the standard steps to study and sketch a graph;', 'thực hiện đúng các bước khảo sát và vẽ đồ thị;'), ('use symmetry, asymptotes and the variation table;', 'dùng tính đối xứng, tiệm cận và [[bảng biến thiên]];'), ('sketch cubic, quartic and rational graphs;', 'vẽ đồ thị hàm bậc ba, trùng phương và phân thức;'), ('describe a graph in English.', 'mô tả đồ thị bằng tiếng Anh.')],
  [('<b>sketching a graph</b> – studying a function and drawing its graph.', '[[Khảo sát và vẽ đồ thị]] – nghiên cứu hàm số rồi vẽ đồ thị.'), ('<b>even function</b> – \\(f(-x)=f(x)\\).', '[[Hàm số chẵn]] – \\(f(-x)=f(x)\\).'), ('<b>odd function</b> – \\(f(-x)=-f(x)\\).', '[[Hàm số lẻ]] – \\(f(-x)=-f(x)\\).'),
   ('<b>center of symmetry</b> – a point about which the graph is symmetric.', '[[Tâm đối xứng]] – điểm mà đồ thị đối xứng qua nó.'), ('<b>intercept</b> – a point where the graph meets an axis.', '[[Giao điểm với trục]] – điểm đồ thị cắt một trục tọa độ.'), ('<b>variation table</b> – a table showing increase, decrease and extrema.', '[[Bảng biến thiên]] – bảng cho biết chiều biến thiên và cực trị.')],
  [('Study and sketch the graph of the function.', 'Khảo sát và vẽ đồ thị của hàm số.'), ('The graph is symmetric about the y-axis.', 'Đồ thị đối xứng qua trục tung.'), ('Find the intercepts with the axes.', 'Tìm giao điểm của đồ thị với các trục tọa độ.'), ('Draw the asymptotes with dashed lines.', 'Vẽ các đường tiệm cận bằng nét đứt.')],
  review, theory, ex, pr,
  [('<b>Skipping the domain.</b> A missing point (like \\(x=1\\)) changes the whole shape.', '<b>Bỏ qua tập xác định.</b> Điểm bị thiếu (như \\(x=1\\)) làm thay đổi hình dạng đồ thị.'), ('<b>Forgetting the limits.</b> The ends of the graph come from the limits, not from the extrema.', '<b>Quên giới hạn.</b> Hai đầu đồ thị do giới hạn quyết định, không phải do cực trị.'), ('<b>Drawing the graph across an asymptote.</b> A vertical asymptote splits the graph into separate branches.', '<b>Vẽ đồ thị cắt qua tiệm cận đứng.</b> Tiệm cận đứng chia đồ thị thành các nhánh riêng.')],
  [('Follow the six steps: domain, derivative, limits, variation table, intercepts, drawing.', 'Sáu bước: tập xác định, đạo hàm, giới hạn, bảng biến thiên, giao điểm, vẽ.'), ('Even functions are symmetric about the y-axis; odd ones about the origin.', 'Hàm chẵn đối xứng qua trục tung; hàm lẻ đối xứng qua gốc tọa độ.'), ('For \\(\\dfrac{ax+b}{cx+d}\\), the asymptotes cross at the center of symmetry.', 'Với \\(\\dfrac{ax+b}{cx+d}\\), hai tiệm cận cắt nhau tại tâm đối xứng.')],
  [('I can follow the steps to sketch a graph.', 'Em thực hiện được các bước khảo sát và vẽ đồ thị.'), ('I can use symmetry and asymptotes.', 'Em dùng được tính đối xứng và tiệm cận.'), ('I can read a graph and describe it.', 'Em đọc và mô tả được đồ thị.'), STD_SUMMARY_CHECK_EN()],
  'lessons/grade12/derivative-applications/sketching-graphs.html',
  ENTRY('g12-deriv-app-02', 'Sketching Graphs of Functions', 'Study a function and sketch its graph step by step.', 'Intermediate', 60, ['g12-deriv-app-01'], 'lessons/grade12/derivative-applications/sketching-graphs.html', ['graph', 'sketching', 'symmetry', 'asymptote'], order=20))

# ========================= g12-antider-01 =========================
review = T('Differentiating and finding an <b>antiderivative</b> are reverse operations. Recall: \\((x^n)\'=nx^{n-1}\\), \\((e^x)\'=e^x\\), \\((\\sin x)\'=\\cos x\\), \\((\\cos x)\'=-\\sin x\\), \\((\\ln|x|)\'=\\dfrac1x\\).', 'Lấy [[đạo hàm]] và tìm [[nguyên hàm]] là hai phép toán ngược nhau. Nhắc lại: \\((x^n)\'=nx^{n-1}\\), \\((e^x)\'=e^x\\), \\((\\sin x)\'=\\cos x\\), \\((\\cos x)\'=-\\sin x\\), \\((\\ln|x|)\'=\\dfrac1x\\).')
theory = ('<h3>5.1 %s</h3>' % TI('Definition', 'Định nghĩa') +
  BOX('mint', ('Definition', 'Định nghĩa'), T('Let \\(f\\) be defined on an interval \\(K\\). A function \\(F\\) is an <b>antiderivative</b> of \\(f\\) on \\(K\\) if \\(F\'(x)=f(x)\\) for all \\(x\\in K\\).', 'Cho hàm số \\(f\\) xác định trên khoảng \\(K\\). Hàm số \\(F\\) là [[nguyên hàm]] của \\(f\\) trên \\(K\\) nếu \\(F\'(x)=f(x)\\) với mọi \\(x\\in K\\).')) +
  T('If \\(F\\) is one antiderivative of \\(f\\), then every antiderivative has the form \\(F(x)+C\\), where \\(C\\) is the <b>constant of integration</b>. We write:', 'Nếu \\(F\\) là một nguyên hàm của \\(f\\) thì mọi nguyên hàm có dạng \\(F(x)+C\\), trong đó \\(C\\) là [[hằng số tích phân]]. Kí hiệu:') + M(r'\int f(x)\,dx=F(x)+C') +
  '<h3>5.2 %s</h3>' % TI('Basic antiderivatives', 'Bảng nguyên hàm cơ bản') +
  UL(['\\(\\displaystyle\\int 0\\,dx=C,\\quad \\int dx=x+C\\)', '\\(\\displaystyle\\int x^n\\,dx=\\frac{x^{n+1}}{n+1}+C\\ (n\\ne-1)\\)', '\\(\\displaystyle\\int \\frac1x\\,dx=\\ln|x|+C\\ (x\\ne0)\\)', '\\(\\displaystyle\\int e^x\\,dx=e^x+C\\)',
      '\\(\\displaystyle\\int \\sin x\\,dx=-\\cos x+C,\\quad \\int \\cos x\\,dx=\\sin x+C\\)', '\\(\\displaystyle\\int \\frac{1}{\\cos^2x}\\,dx=\\tan x+C,\\quad \\int \\frac{1}{\\sin^2x}\\,dx=-\\cot x+C\\)']) +
  '<h3>5.3 %s</h3>' % TI('Properties and initial condition', 'Tính chất và điều kiện ban đầu') +
  UL([T('\\(\\displaystyle\\int kf(x)\\,dx=k\\int f(x)\\,dx\\) for a constant \\(k\\ne0\\).', '\\(\\displaystyle\\int kf(x)\\,dx=k\\int f(x)\\,dx\\) với hằng số \\(k\\ne0\\).'), T('\\(\\displaystyle\\int [f(x)\\pm g(x)]\\,dx=\\int f(x)\\,dx\\pm\\int g(x)\\,dx\\).', '\\(\\displaystyle\\int [f(x)\\pm g(x)]\\,dx=\\int f(x)\\,dx\\pm\\int g(x)\\,dx\\).'),
      T('An <b>initial condition</b> such as \\(F(x_0)=y_0\\) fixes the value of \\(C\\).', '[[Điều kiện ban đầu]] dạng \\(F(x_0)=y_0\\) xác định giá trị của \\(C\\).')]))
ex = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Checking an antiderivative', 'Kiểm tra một nguyên hàm'),
  T('Show that \\(F(x)=x^3+2x\\) is an antiderivative of \\(f(x)=3x^2+2\\) on \\(\\mathbb{R}\\).', 'Chứng tỏ \\(F(x)=x^3+2x\\) là một nguyên hàm của \\(f(x)=3x^2+2\\) trên \\(\\mathbb{R}\\).'),
  ('Differentiate \\(F\\) and compare with \\(f\\).', 'Lấy đạo hàm của \\(F\\) rồi so với \\(f\\).'),
  [T('\\(F\'(x)=3x^2+2=f(x)\\) for all \\(x\\in\\mathbb{R}\\).', '\\(F\'(x)=3x^2+2=f(x)\\) với mọi \\(x\\in\\mathbb{R}\\).'), T('So \\(F\\) is an antiderivative of \\(f\\).', 'Vậy \\(F\\) là một nguyên hàm của \\(f\\).')], '\\(F\'=f\\)')
ex += EXAMPLE(2, ('Basic', 'Cơ bản'), ('A polynomial', 'Đa thức'),
  T('Find \\(\\displaystyle\\int(3x^2-4x+5)\\,dx\\).', 'Tìm \\(\\displaystyle\\int(3x^2-4x+5)\\,dx\\).'), ('Use the sum rule and the power rule term by term.', 'Dùng quy tắc tổng và quy tắc lũy thừa cho từng số hạng.'),
  [T('\\(\\displaystyle\\int3x^2dx=x^3\\), \\(\\displaystyle\\int4x\\,dx=2x^2\\), \\(\\displaystyle\\int5\\,dx=5x\\).', '\\(\\displaystyle\\int3x^2dx=x^3\\), \\(\\displaystyle\\int4x\\,dx=2x^2\\), \\(\\displaystyle\\int5\\,dx=5x\\).'), T('Combine and add one constant \\(C\\).', 'Gộp lại và cộng một hằng số \\(C\\).')], '\\(x^3-2x^2+5x+C\\)')
ex += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Negative powers and exponentials', 'Lũy thừa âm và hàm mũ'),
  T('Find \\(\\displaystyle\\int\\left(\\frac1{x^2}+2e^x\\right)dx\\) on \\((0,+\\infty)\\).', 'Tìm \\(\\displaystyle\\int\\left(\\frac1{x^2}+2e^x\\right)dx\\) trên \\((0,+\\infty)\\).'), ('Write \\(\\dfrac1{x^2}=x^{-2}\\).', 'Viết \\(\\dfrac1{x^2}=x^{-2}\\).'),
  [T('\\(\\displaystyle\\int x^{-2}dx=\\frac{x^{-1}}{-1}=-\\frac1x\\).', '\\(\\displaystyle\\int x^{-2}dx=\\frac{x^{-1}}{-1}=-\\frac1x\\).'), T('\\(\\displaystyle\\int2e^xdx=2e^x\\).', '\\(\\displaystyle\\int2e^xdx=2e^x\\).')], '\\(-\\dfrac1x+2e^x+C\\)')
ex += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('An initial condition', 'Có điều kiện ban đầu'),
  T('Find the antiderivative \\(F\\) of \\(f(x)=2x-3\\) such that \\(F(1)=4\\).', 'Tìm nguyên hàm \\(F\\) của \\(f(x)=2x-3\\) thỏa mãn \\(F(1)=4\\).'), ('First find the general antiderivative, then find \\(C\\).', 'Tìm nguyên hàm tổng quát trước, rồi tìm \\(C\\).'),
  [T('\\(F(x)=x^2-3x+C\\).', '\\(F(x)=x^2-3x+C\\).'), T('\\(F(1)=1-3+C=4\\) gives \\(C=6\\).', '\\(F(1)=1-3+C=4\\) cho \\(C=6\\).')], '\\(F(x)=x^2-3x+6\\)')
pr = [(('A. Multiple Choice', 'A. Trắc nghiệm nhiều lựa chọn'), [
  MCQ(1, ('Find \\(\\displaystyle\\int2x\\,dx\\).', 'Tìm \\(\\displaystyle\\int2x\\,dx\\).'), ['x^2+C', '2x^2+C', 'x+C', '2+C'], 'a', ('Answer: a. \\((x^2)\'=2x\\).', 'Đáp án a. \\((x^2)\'=2x\\).')),
  MCQ(2, ('Find \\(\\displaystyle\\int\\cos x\\,dx\\).', 'Tìm \\(\\displaystyle\\int\\cos x\\,dx\\).'), ['-\\sin x+C', '\\cos x+C', '\\sin x+C', '-\\cos x+C'], 'c', ('Answer: c. \\((\\sin x)\'=\\cos x\\).', 'Đáp án c. \\((\\sin x)\'=\\cos x\\).')),
  MCQ(3, ('Find \\(\\displaystyle\\int x^3\\,dx\\).', 'Tìm \\(\\displaystyle\\int x^3\\,dx\\).'), [r'\frac{x^4}{4}+C', '3x^2+C', 'x^4+C', r'\frac{x^3}{3}+C'], 'a', ('Answer: a. Power rule with \\(n=3\\).', 'Đáp án a. Quy tắc lũy thừa với \\(n=3\\).')),
  MCQ(4, ('Find \\(\\displaystyle\\int(\\sin x+2)\\,dx\\).', 'Tìm \\(\\displaystyle\\int(\\sin x+2)\\,dx\\).'), ['\\cos x+2x+C', '-\\cos x+2x+C', '-\\cos x+2+C', '\\sin x+2x+C'], 'b', ('Answer: b. \\(\\int\\sin x\\,dx=-\\cos x\\) and \\(\\int2\\,dx=2x\\).', 'Đáp án b. \\(\\int\\sin x\\,dx=-\\cos x\\) và \\(\\int2\\,dx=2x\\).'))]),
 (('B. True or False', 'B. Đúng hoặc sai'), [
  TF(5, ('True or false: \\(x^2+5\\) and \\(x^2-1\\) are both antiderivatives of \\(2x\\).', 'Đúng hay sai: \\(x^2+5\\) và \\(x^2-1\\) đều là nguyên hàm của \\(2x\\).'), 'true', ('True. They differ only by a constant.', 'Đúng. Chúng chỉ khác nhau một hằng số.')),
  TF(6, ('True or false: \\(\\displaystyle\\int\\frac1x\\,dx=\\ln x+C\\) for every \\(x\\ne0\\).', 'Đúng hay sai: \\(\\displaystyle\\int\\frac1x\\,dx=\\ln x+C\\) với mọi \\(x\\ne0\\).'), 'false', ('False. The correct form is \\(\\ln|x|+C\\), because \\(\\ln x\\) is not defined for \\(x<0\\).', 'Sai. Dạng đúng là \\(\\ln|x|+C\\), vì \\(\\ln x\\) không xác định khi \\(x<0\\).'))]),
 (('C. Short Answer', 'C. Trả lời ngắn'), [
  SHORT(7, ('Let \\(F\\) be an antiderivative of \\(f(x)=4x-1\\) with \\(F(0)=3\\). Find \\(F(1)\\).', 'Cho \\(F\\) là nguyên hàm của \\(f(x)=4x-1\\) với \\(F(0)=3\\). Tìm \\(F(1)\\).'), '4', 'number', ('Enter a number.', 'Nhập một số.'), ('Answer: 4. \\(F(x)=2x^2-x+3\\), so \\(F(1)=2-1+3=4\\).', 'Đáp án: 4. \\(F(x)=2x^2-x+3\\) nên \\(F(1)=2-1+3=4\\).')),
  SHORT(8, ('\\(\\displaystyle\\int6x^2\\,dx=kx^3+C\\). Find \\(k\\).', '\\(\\displaystyle\\int6x^2\\,dx=kx^3+C\\). Tìm \\(k\\).'), '2', 'number', ('Enter a number.', 'Nhập một số.'), ('Answer: 2. \\(\\dfrac{6x^3}{3}=2x^3\\).', 'Đáp án: 2. \\(\\dfrac{6x^3}{3}=2x^3\\).')),
  SHORT(9, ('Let \\(F(x)=\\displaystyle\\int(3x^2+1)\\,dx\\) with \\(F(0)=0\\). Find \\(F(2)\\).', 'Cho \\(F(x)=\\displaystyle\\int(3x^2+1)\\,dx\\) với \\(F(0)=0\\). Tìm \\(F(2)\\).'), '10', 'number', ('Enter a number.', 'Nhập một số.'), ('Answer: 10. \\(F(x)=x^3+x\\), so \\(F(2)=8+2=10\\).', 'Đáp án: 10. \\(F(x)=x^3+x\\) nên \\(F(2)=8+2=10\\).')),
  SHORT(10, ('Let \\(F\\) be an antiderivative of \\(f(x)=e^x+1\\) with \\(F(0)=2\\). Find \\(F(0)+F\'(0)\\).', 'Cho \\(F\\) là nguyên hàm của \\(f(x)=e^x+1\\) với \\(F(0)=2\\). Tìm \\(F(0)+F\'(0)\\).'), '4', 'number', ('Enter a number.', 'Nhập một số.'), ('Answer: 4. \\(F\'(0)=f(0)=e^0+1=2\\) and \\(F(0)=2\\).', 'Đáp án: 4. \\(F\'(0)=f(0)=e^0+1=2\\) và \\(F(0)=2\\).'))])]
S2 = [
 [_m(1, r'Find \(\displaystyle\int4x\,dx\).§Tìm \(\displaystyle\int4x\,dx\).', ['4x^2+C', '2x^2+C', 'x^2+C', '4+C'], 'b', r'\((2x^2)′=4x\).'),
  _m(2, r'Find \(\displaystyle\int\sin x\,dx\).§Tìm \(\displaystyle\int\sin x\,dx\).', [r'\cos x+C', r'\sin x+C', r'-\sin x+C', r'-\cos x+C'], 'd', r'\((-\cos x)′=\sin x\).'),
  _m(3, r'Find \(\displaystyle\int x^5\,dx\).§Tìm \(\displaystyle\int x^5\,dx\).', [r'\frac{x^5}{5}+C', '5x^4+C', r'\frac{x^6}{6}+C', 'x^6+C'], 'c', r'Power rule with \(n=5\).§Quy tắc lũy thừa với \(n=5\).'),
  _m(4, r'Find \(\displaystyle\int(\cos x+3)\,dx\).§Tìm \(\displaystyle\int(\cos x+3)\,dx\).', [r'\sin x+3x+C', r'-\sin x+3x+C', r'\sin x+3+C', r'\cos x+3x+C'], 'a',
      r'\(\int\cos x\,dx=\sin x\) and \(\int3\,dx=3x\).§\(\int\cos x\,dx=\sin x\) và \(\int3\,dx=3x\).')],
 [_t(5, r'True or false: \(x^3+1\) and \(x^3-4\) are both antiderivatives of \(3x^2\).§Đúng hay sai: \(x^3+1\) và \(x^3-4\) đều là nguyên hàm của \(3x^2\).', 'true',
      r'They differ only by a constant.§Chúng chỉ khác nhau một hằng số.'),
  _t(6, r'True or false: \(\displaystyle\int\cos x\,dx=-\sin x+C\).§Đúng hay sai: \(\displaystyle\int\cos x\,dx=-\sin x+C\).', 'false',
      r'The correct result is \(\sin x+C\), because \((\sin x)′=\cos x\).§Kết quả đúng là \(\sin x+C\), vì \((\sin x)′=\cos x\).')],
 [_s(7, r'Let \(F\) be an antiderivative of \(f(x)=6x+2\) with \(F(0)=1\). Find \(F(1)\).§Cho \(F\) là nguyên hàm của \(f(x)=6x+2\) với \(F(0)=1\). Tìm \(F(1)\).', '6', '6', 'n',
      r'\(F(x)=3x^2+2x+1\), so \(F(1)=3+2+1=6\).§\(F(x)=3x^2+2x+1\) nên \(F(1)=3+2+1=6\).'),
  _s(8, r'\(\displaystyle\int12x^3\,dx=kx^4+C\). Find \(k\).§\(\displaystyle\int12x^3\,dx=kx^4+C\). Tìm \(k\).', '3', '3', 'n',
      r'\(\dfrac{12x^4}{4}=3x^4\).'),
  _s(9, r'Let \(F(x)=\displaystyle\int(4x^3+2)\,dx\) with \(F(0)=0\). Find \(F(2)\).§Cho \(F(x)=\displaystyle\int(4x^3+2)\,dx\) với \(F(0)=0\). Tìm \(F(2)\).', '20', '20', 'n',
      r'\(F(x)=x^4+2x\), so \(F(2)=16+4=20\).§\(F(x)=x^4+2x\) nên \(F(2)=16+4=20\).'),
  _s(10, r'Let \(F\) be an antiderivative of \(f(x)=e^x+3\) with \(F(0)=1\). Find \(F(0)+F′(0)\).§Cho \(F\) là nguyên hàm của \(f(x)=e^x+3\) với \(F(0)=1\). Tìm \(F(0)+F′(0)\).', '5', '5', 'n',
      r'\(F′(0)=f(0)=e^0+3=4\) and \(F(0)=1\).§\(F′(0)=f(0)=e^0+3=4\) và \(F(0)=1\).')]]
S3 = [
 [_m(1, r'Find \(\displaystyle\int6x\,dx\).§Tìm \(\displaystyle\int6x\,dx\).', ['3x^2+C', '6x^2+C', 'x^2+C', '6+C'], 'a', r'\((3x^2)′=6x\).'),
  _m(2, r'Find \(\displaystyle\int\frac{1}{\cos^2x}\,dx\).§Tìm \(\displaystyle\int\frac{1}{\cos^2x}\,dx\).', [r'-\cot x+C', r'\sin x+C', r'\tan x+C', r'-\tan x+C'], 'c', r'\((\tan x)′=\dfrac{1}{\cos^2x}\).'),
  _m(3, r'Find \(\displaystyle\int x^4\,dx\).§Tìm \(\displaystyle\int x^4\,dx\).', ['4x^3+C', r'\frac{x^5}{5}+C', 'x^5+C', r'\frac{x^4}{4}+C'], 'b', r'Power rule with \(n=4\).§Quy tắc lũy thừa với \(n=4\).'),
  _m(4, r'Find \(\displaystyle\int(e^x+2)\,dx\).§Tìm \(\displaystyle\int(e^x+2)\,dx\).', ['e^x+2+C', 'e^x+2x^2+C', 'xe^x+2x+C', 'e^x+2x+C'], 'd',
      r'\(\int e^x\,dx=e^x\) and \(\int2\,dx=2x\).§\(\int e^x\,dx=e^x\) và \(\int2\,dx=2x\).')],
 [_t(5, r'True or false: \(\sin x+2\) and \(\sin x-7\) are both antiderivatives of \(\cos x\).§Đúng hay sai: \(\sin x+2\) và \(\sin x-7\) đều là nguyên hàm của \(\cos x\).', 'true',
      r'They differ only by a constant.§Chúng chỉ khác nhau một hằng số.'),
  _t(6, r'True or false: \(\displaystyle\int(-\sin x)\,dx=-\cos x+C\).§Đúng hay sai: \(\displaystyle\int(-\sin x)\,dx=-\cos x+C\).', 'false',
      r'The correct result is \(\cos x+C\), because \((\cos x)′=-\sin x\).§Kết quả đúng là \(\cos x+C\), vì \((\cos x)′=-\sin x\).')],
 [_s(7, r'Let \(F\) be an antiderivative of \(f(x)=2x-5\) with \(F(0)=-1\). Find \(F(1)\).§Cho \(F\) là nguyên hàm của \(f(x)=2x-5\) với \(F(0)=-1\). Tìm \(F(1)\).', '-5', r'\(-5\)', 'n',
      r'\(F(x)=x^2-5x-1\), so \(F(1)=1-5-1=-5\).§\(F(x)=x^2-5x-1\) nên \(F(1)=1-5-1=-5\).'),
  _s(8, r'\(\displaystyle\int20x^4\,dx=kx^5+C\). Find \(k\).§\(\displaystyle\int20x^4\,dx=kx^5+C\). Tìm \(k\).', '4', '4', 'n',
      r'\(\dfrac{20x^5}{5}=4x^5\).'),
  _s(9, r'Let \(F(x)=\displaystyle\int(6x^2-2)\,dx\) with \(F(0)=0\). Find \(F(2)\).§Cho \(F(x)=\displaystyle\int(6x^2-2)\,dx\) với \(F(0)=0\). Tìm \(F(2)\).', '12', '12', 'n',
      r'\(F(x)=2x^3-2x\), so \(F(2)=16-4=12\).§\(F(x)=2x^3-2x\) nên \(F(2)=16-4=12\).'),
  _s(10, r'Let \(F\) be an antiderivative of \(f(x)=3e^x+2\) with \(F(0)=1\). Find \(F(0)+F′(0)\).§Cho \(F\) là nguyên hàm của \(f(x)=3e^x+2\) với \(F(0)=1\). Tìm \(F(0)+F′(0)\).', '6', '6', 'n',
      r'\(F′(0)=f(0)=3e^0+2=5\) and \(F(0)=1\).§\(F′(0)=f(0)=3e^0+2=5\) và \(F(0)=1\).')]]
_T = [t for t, _ in pr]
S1 = [g for _, g in pr]
pr = LEVEL_PRACTICE(_T, {1: S1, 2: S2, 3: S3})

build('g12-antider-01', 'Antiderivatives', 'Nguyên hàm', CAT3,
  {'level': ('Intermediate', 'Trung bình'), 'time': ('about 45 minutes', 'khoảng 45 phút'), 'before': ('derivative rules', 'quy tắc tính đạo hàm')},
  [('define an antiderivative and the constant of integration;', 'định nghĩa [[nguyên hàm]] và [[hằng số tích phân]];'), ('use the table of basic antiderivatives;', 'dùng bảng nguyên hàm cơ bản;'), ('use an initial condition to find \\(C\\);', 'dùng [[điều kiện ban đầu]] để tìm \\(C\\);'), ('read antiderivative rules in English.', 'đọc các quy tắc nguyên hàm bằng tiếng Anh.')],
  [('<b>antiderivative</b> – a function \\(F\\) whose derivative is \\(f\\).', '[[Nguyên hàm]] – hàm số \\(F\\) có đạo hàm bằng \\(f\\).'), ('<b>constant of integration</b> – the arbitrary constant \\(C\\).', '[[Hằng số tích phân]] – hằng số tùy ý \\(C\\).'), ('<b>initial condition</b> – a given value such as \\(F(1)=4\\).', '[[Điều kiện ban đầu]] – giá trị cho trước như \\(F(1)=4\\).'), ('<b>derivative</b> – the rate of change \\(f\'(x)\\).', '[[Đạo hàm]] – tốc độ thay đổi \\(f\'(x)\\).')],
  [('Find the antiderivative of the function.', 'Tìm nguyên hàm của hàm số.'), ('Do not forget the constant of integration.', 'Đừng quên hằng số tích phân.'), ('Use the initial condition to find the constant.', 'Dùng điều kiện ban đầu để tìm hằng số.'), ('Differentiate your answer to check it.', 'Lấy đạo hàm kết quả để kiểm tra.')],
  review, theory, ex, pr,
  [('<b>Forgetting \\(+C\\).</b> An antiderivative problem has infinitely many answers.', '<b>Quên \\(+C\\).</b> Bài toán nguyên hàm có vô số đáp án.'), ('<b>Using the power rule with \\(n=-1\\).</b> \\(\\int\\dfrac1x\\,dx=\\ln|x|+C\\).', '<b>Dùng quy tắc lũy thừa với \\(n=-1\\).</b> \\(\\int\\dfrac1x\\,dx=\\ln|x|+C\\).'), ('<b>Sign errors with sine and cosine.</b> \\(\\int\\sin x\\,dx=-\\cos x+C\\).', '<b>Nhầm dấu với sin và cos.</b> \\(\\int\\sin x\\,dx=-\\cos x+C\\).')],
  [('\\(F\'=f\\) means \\(F\\) is an antiderivative of \\(f\\); all antiderivatives are \\(F+C\\).', '\\(F\'=f\\) nghĩa là \\(F\\) là nguyên hàm của \\(f\\); mọi nguyên hàm có dạng \\(F+C\\).'), ('Use the table and the sum and constant rules term by term.', 'Dùng bảng nguyên hàm cùng quy tắc tổng và hằng số cho từng số hạng.'), ('Check by differentiating.', 'Kiểm tra bằng cách lấy đạo hàm.')],
  [('I can check that \\(F\\) is an antiderivative of \\(f\\).', 'Em kiểm tra được \\(F\\) là nguyên hàm của \\(f\\).'), ('I can use the basic table.', 'Em dùng được bảng nguyên hàm cơ bản.'), ('I can use an initial condition.', 'Em dùng được điều kiện ban đầu.'), STD_SUMMARY_CHECK_EN()],
  'lessons/grade12/antiderivatives/antiderivatives.html',
  ENTRY('g12-antider-01', 'Antiderivatives', 'Learn antiderivatives, the basic table and initial conditions.', 'Intermediate', 45, [], 'lessons/grade12/antiderivatives/antiderivatives.html', ['antiderivative', 'integral', 'constant of integration'], order=60))

# ========================= g12-antider-02 =========================
review = T('You know the basic table. Now you need two ideas: replacing a part of the function by a new variable (<b>substitution</b>) and reversing the product rule (<b>integration by parts</b>).', 'Em đã biết bảng nguyên hàm cơ bản. Bây giờ cần hai ý tưởng: thay một phần của hàm bằng biến mới ([[phép đổi biến]]) và đảo ngược quy tắc đạo hàm của tích ([[nguyên hàm từng phần]]).')
theory = ('<h3>5.1 %s</h3>' % TI('A linear expression inside', 'Biểu thức bậc nhất bên trong') +
  BOX('mint', ('Rule', 'Quy tắc'), T('If \\(\\int f(x)\\,dx=F(x)+C\\), then for \\(a\\ne0\\), with a <b>linear expression</b> \\(ax+b\\):', 'Nếu \\(\\int f(x)\\,dx=F(x)+C\\) thì với \\(a\\ne0\\) và [[biểu thức bậc nhất]] \\(ax+b\\):'), M(r'\int f(ax+b)\,dx=\frac1a\,F(ax+b)+C')) +
  '<h3>5.2 %s</h3>' % TI('Substitution', 'Phương pháp đổi biến') +
  OL([T('Choose \\(u=g(x)\\) so that \\(g\'(x)\\,dx\\) appears in the integral.', 'Chọn \\(u=g(x)\\) sao cho \\(g\'(x)\\,dx\\) xuất hiện trong tích phân.'), T('Replace: \\(du=g\'(x)\\,dx\\).', 'Thay: \\(du=g\'(x)\\,dx\\).'), T('Find the antiderivative in \\(u\\), then go back to \\(x\\).', 'Tìm nguyên hàm theo \\(u\\), rồi quay về \\(x\\).')]) +
  '<h3>5.3 %s</h3>' % TI('Integration by parts', 'Nguyên hàm từng phần') +
  BOX('mint', ('Formula', 'Công thức'), M(r'\int u\,dv=uv-\int v\,du'), T('Choose \\(u\\) as the part that becomes simpler when differentiated (for example \\(x\\)).', 'Chọn \\(u\\) là phần đơn giản hơn khi lấy đạo hàm (ví dụ \\(x\\)).')))
ex = EXAMPLE(1, ('Basic', 'Cơ bản'), ('A power of a linear expression', 'Lũy thừa của biểu thức bậc nhất'),
  T('Find \\(\\displaystyle\\int(2x+1)^5\\,dx\\).', 'Tìm \\(\\displaystyle\\int(2x+1)^5\\,dx\\).'), ('Here \\(a=2\\) and \\(f(t)=t^5\\).', 'Ở đây \\(a=2\\) và \\(f(t)=t^5\\).'),
  [T('\\(\\int t^5dt=\\dfrac{t^6}{6}\\).', '\\(\\int t^5dt=\\dfrac{t^6}{6}\\).'), T('Multiply by \\(\\dfrac1a=\\dfrac12\\): \\(\\dfrac{(2x+1)^6}{12}\\).', 'Nhân với \\(\\dfrac1a=\\dfrac12\\): \\(\\dfrac{(2x+1)^6}{12}\\).')], '\\(\\dfrac{(2x+1)^6}{12}+C\\)')
ex += EXAMPLE(2, ('Basic', 'Cơ bản'), ('An exponential', 'Hàm mũ'),
  T('Find \\(\\displaystyle\\int e^{3x-1}\\,dx\\).', 'Tìm \\(\\displaystyle\\int e^{3x-1}\\,dx\\).'), ('Here \\(a=3\\).', 'Ở đây \\(a=3\\).'),
  [T('\\(\\int e^tdt=e^t\\), then multiply by \\(\\dfrac13\\).', '\\(\\int e^tdt=e^t\\), rồi nhân với \\(\\dfrac13\\).')], '\\(\\dfrac13e^{3x-1}+C\\)')
ex += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Substitution', 'Đổi biến'),
  T('Find \\(\\displaystyle\\int x(x^2+1)^3\\,dx\\).', 'Tìm \\(\\displaystyle\\int x(x^2+1)^3\\,dx\\).'), ('The derivative of \\(x^2+1\\) is \\(2x\\), and \\(x\\) is almost there.', 'Đạo hàm của \\(x^2+1\\) là \\(2x\\), và \\(x\\) gần như đã có sẵn.'),
  [T('Let \\(u=x^2+1\\). Then \\(du=2x\\,dx\\), so \\(x\\,dx=\\tfrac12du\\).', 'Đặt \\(u=x^2+1\\). Khi đó \\(du=2x\\,dx\\) nên \\(x\\,dx=\\tfrac12du\\).'), T('\\(\\displaystyle\\int\\tfrac12u^3du=\\frac{u^4}{8}\\).', '\\(\\displaystyle\\int\\tfrac12u^3du=\\frac{u^4}{8}\\).'), T('Go back: \\(u=x^2+1\\).', 'Quay về biến \\(x\\): \\(u=x^2+1\\).')], '\\(\\dfrac{(x^2+1)^4}{8}+C\\)')
ex += EXAMPLE(4, ('Advanced', 'Nâng cao'), ('Integration by parts', 'Nguyên hàm từng phần'),
  T('Find \\(\\displaystyle\\int xe^x\\,dx\\).', 'Tìm \\(\\displaystyle\\int xe^x\\,dx\\).'), ('Let \\(u=x\\) and \\(dv=e^xdx\\).', 'Đặt \\(u=x\\) và \\(dv=e^xdx\\).'),
  [T('Then \\(du=dx\\) and \\(v=e^x\\).', 'Khi đó \\(du=dx\\) và \\(v=e^x\\).'), T('\\(\\int xe^xdx=xe^x-\\int e^xdx=xe^x-e^x+C\\).', '\\(\\int xe^xdx=xe^x-\\int e^xdx=xe^x-e^x+C\\).')], '\\(e^x(x-1)+C\\)')
pr = [(('A. Multiple Choice', 'A. Trắc nghiệm nhiều lựa chọn'), [
  MCQ(1, ('Find \\(\\displaystyle\\int\\cos2x\\,dx\\).', 'Tìm \\(\\displaystyle\\int\\cos2x\\,dx\\).'), ['\\sin2x+C', r'\frac12\sin2x+C', '2\\sin2x+C', r'-\frac12\sin2x+C'], 'b', ('Answer: b. Multiply by \\(\\dfrac1a=\\dfrac12\\).', 'Đáp án b. Nhân với \\(\\dfrac1a=\\dfrac12\\).')),
  MCQ(2, ('Find \\(\\displaystyle\\int e^{2x}\\,dx\\).', 'Tìm \\(\\displaystyle\\int e^{2x}\\,dx\\).'), ['2e^{2x}+C', 'e^{2x}+C', r'\frac12e^{2x}+C', r'\frac12e^{x}+C'], 'c', ('Answer: c.', 'Đáp án c.')),
  MCQ(3, ('Find \\(\\displaystyle\\int\\frac{1}{3x+1}\\,dx\\).', 'Tìm \\(\\displaystyle\\int\\frac{1}{3x+1}\\,dx\\).'), [r'\ln|3x+1|+C', r'\frac13\ln|3x+1|+C', r'3\ln|3x+1|+C', r'-\frac13\ln|3x+1|+C'], 'b', ('Answer: b. \\(\\int\\dfrac1t\\,dt=\\ln|t|\\), times \\(\\dfrac13\\).', 'Đáp án b. \\(\\int\\dfrac1t\\,dt=\\ln|t|\\), nhân với \\(\\dfrac13\\).')),
  MCQ(4, ('Find \\(\\displaystyle\\int(x+1)^4\\,dx\\).', 'Tìm \\(\\displaystyle\\int(x+1)^4\\,dx\\).'), [r'\frac{(x+1)^5}{5}+C', '4(x+1)^3+C', '(x+1)^5+C', r'\frac{x^5}{5}+x+C'], 'a', ('Answer: a. Here \\(a=1\\).', 'Đáp án a. Ở đây \\(a=1\\).'))]),
 (('B. True or False', 'B. Đúng hoặc sai'), [
  TF(5, ('True or false: \\(\\displaystyle\\int(2x+1)^3\\,dx=\\dfrac{(2x+1)^4}{4}+C\\).', 'Đúng hay sai: \\(\\displaystyle\\int(2x+1)^3\\,dx=\\dfrac{(2x+1)^4}{4}+C\\).'), 'false', ('False. We must also multiply by \\(\\dfrac12\\): the result is \\(\\dfrac{(2x+1)^4}{8}+C\\).', 'Sai. Còn phải nhân với \\(\\dfrac12\\): kết quả là \\(\\dfrac{(2x+1)^4}{8}+C\\).')),
  TF(6, ('True or false: \\(\\displaystyle\\int2xe^{x^2}\\,dx=e^{x^2}+C\\).', 'Đúng hay sai: \\(\\displaystyle\\int2xe^{x^2}\\,dx=e^{x^2}+C\\).'), 'true', ('True. Let \\(u=x^2\\), \\(du=2x\\,dx\\).', 'Đúng. Đặt \\(u=x^2\\), \\(du=2x\\,dx\\).'))]),
 (('C. Short Answer', 'C. Trả lời ngắn'), [
  SHORT(7, ('\\(\\displaystyle\\int\\sin3x\\,dx=k\\cos3x+C\\). Find \\(k\\).', '\\(\\displaystyle\\int\\sin3x\\,dx=k\\cos3x+C\\). Tìm \\(k\\).'), '-1/3', 'number', ('Enter a number or fraction, for example -1/3.', 'Nhập số hoặc phân số, ví dụ -1/3.'), ('Answer: \\(-\\dfrac13\\).', 'Đáp án: \\(-\\dfrac13\\).')),
  SHORT(8, ('\\(\\displaystyle\\int x(x^2+1)^3dx=\\dfrac{(x^2+1)^4}{k}+C\\). Find \\(k\\).', '\\(\\displaystyle\\int x(x^2+1)^3dx=\\dfrac{(x^2+1)^4}{k}+C\\). Tìm \\(k\\).'), '8', 'number', ('Enter a number.', 'Nhập một số.'), ('Answer: 8. See Example 3.', 'Đáp án: 8. Xem Ví dụ 3.')),
  SHORT(9, ('\\(\\displaystyle\\int x\\cos x\\,dx=x\\sin x+k\\cos x+C\\). Find \\(k\\).', '\\(\\displaystyle\\int x\\cos x\\,dx=x\\sin x+k\\cos x+C\\). Tìm \\(k\\).'), '1', 'number', ('Enter a number.', 'Nhập một số.'), ('Answer: 1. With \\(u=x\\), \\(dv=\\cos x\\,dx\\): \\(x\\sin x-\\int\\sin x\\,dx=x\\sin x+\\cos x\\).', 'Đáp án: 1. Với \\(u=x\\), \\(dv=\\cos x\\,dx\\): \\(x\\sin x-\\int\\sin x\\,dx=x\\sin x+\\cos x\\).')),
  SHORT(10, ('Let \\(F\\) be an antiderivative of \\(f(x)=e^{2x}\\) with \\(F(0)=2\\). Find \\(F(\\ln2)\\).', 'Cho \\(F\\) là nguyên hàm của \\(f(x)=e^{2x}\\) với \\(F(0)=2\\). Tìm \\(F(\\ln2)\\).'), '3.5|7/2', 'number', ('Enter a number, for example 3.5.', 'Nhập một số, ví dụ 3.5.'), ('Answer: 3.5. \\(F(x)=\\tfrac12e^{2x}+\\tfrac32\\), so \\(F(\\ln2)=\\tfrac12\\cdot4+\\tfrac32=3.5\\).', 'Đáp án: 3.5. \\(F(x)=\\tfrac12e^{2x}+\\tfrac32\\) nên \\(F(\\ln2)=\\tfrac12\\cdot4+\\tfrac32=3.5\\).'))])]
S2 = [
 [_m(1, r'Find \(\displaystyle\int\cos3x\,dx\).§Tìm \(\displaystyle\int\cos3x\,dx\).', [r'\sin3x+C', r'3\sin3x+C', r'\frac13\sin3x+C', r'-\frac13\sin3x+C'], 'c', r'Multiply by \(\dfrac1a=\dfrac13\).§Nhân với \(\dfrac1a=\dfrac13\).'),
  _m(2, r'Find \(\displaystyle\int e^{3x}\,dx\).§Tìm \(\displaystyle\int e^{3x}\,dx\).', [r'\frac13e^{3x}+C', '3e^{3x}+C', 'e^{3x}+C', r'\frac13e^{x}+C'], 'a', r'Multiply by \(\dfrac13\).§Nhân với \(\dfrac13\).'),
  _m(3, r'Find \(\displaystyle\int\frac{1}{2x-1}\,dx\).§Tìm \(\displaystyle\int\frac{1}{2x-1}\,dx\).', [r'2\ln|2x-1|+C', r'\ln|2x-1|+C', r'\frac12\ln|2x-1|+C', r'-\frac12\ln|2x-1|+C'], 'c',
      r'\(\int\dfrac1t\,dt=\ln|t|\), times \(\dfrac12\).§\(\int\dfrac1t\,dt=\ln|t|\), nhân với \(\dfrac12\).'),
  _m(4, r'Find \(\displaystyle\int(x-2)^3\,dx\).§Tìm \(\displaystyle\int(x-2)^3\,dx\).', ['3(x-2)^2+C', r'\frac{(x-2)^4}{4}+C', '(x-2)^4+C', r'\frac{x^4}{4}-2x+C'], 'b', r'Here \(a=1\).§Ở đây \(a=1\).')],
 [_t(5, r'True or false: \(\displaystyle\int(3x+1)^2\,dx=\dfrac{(3x+1)^3}{3}+C\).§Đúng hay sai: \(\displaystyle\int(3x+1)^2\,dx=\dfrac{(3x+1)^3}{3}+C\).', 'false',
      r'We must also multiply by \(\dfrac13\): the result is \(\dfrac{(3x+1)^3}{9}+C\).§Còn phải nhân với \(\dfrac13\): kết quả là \(\dfrac{(3x+1)^3}{9}+C\).'),
  _t(6, r'True or false: \(\displaystyle\int3x^2e^{x^3}\,dx=e^{x^3}+C\).§Đúng hay sai: \(\displaystyle\int3x^2e^{x^3}\,dx=e^{x^3}+C\).', 'true',
      r'Let \(u=x^3\), \(du=3x^2\,dx\).§Đặt \(u=x^3\), \(du=3x^2\,dx\).')],
 [_s(7, r'\(\displaystyle\int\sin5x\,dx=k\cos5x+C\). Find \(k\).§\(\displaystyle\int\sin5x\,dx=k\cos5x+C\). Tìm \(k\).', '-1/5', r'\(-\dfrac15\)', 'f',
      r'\(\int\sin ax\,dx=-\dfrac1a\cos ax\).'),
  _s(8, r'\(\displaystyle\int x(x^2+2)^4dx=\dfrac{(x^2+2)^5}{k}+C\). Find \(k\).§\(\displaystyle\int x(x^2+2)^4dx=\dfrac{(x^2+2)^5}{k}+C\). Tìm \(k\).', '10', '10', 'n',
      r'Let \(u=x^2+2\), \(du=2x\,dx\): \(\dfrac12\cdot\dfrac{u^5}{5}=\dfrac{u^5}{10}\).§Đặt \(u=x^2+2\), \(du=2x\,dx\): \(\dfrac12\cdot\dfrac{u^5}{5}=\dfrac{u^5}{10}\).'),
  _s(9, r'\(\displaystyle\int xe^x\,dx=xe^x+ke^x+C\). Find \(k\).§\(\displaystyle\int xe^x\,dx=xe^x+ke^x+C\). Tìm \(k\).', '-1', r'\(-1\)', 'n',
      r'With \(u=x\), \(dv=e^x\,dx\): \(xe^x-\int e^x\,dx=xe^x-e^x\).§Với \(u=x\), \(dv=e^x\,dx\): \(xe^x-\int e^x\,dx=xe^x-e^x\).'),
  _s(10, r'Let \(F\) be an antiderivative of \(f(x)=e^{2x}\) with \(F(0)=1\). Find \(F(\ln3)\).§Cho \(F\) là nguyên hàm của \(f(x)=e^{2x}\) với \(F(0)=1\). Tìm \(F(\ln3)\).', '5', '5', 'n',
      r'\(F(x)=\tfrac12e^{2x}+\tfrac12\), so \(F(\ln3)=\tfrac12\cdot9+\tfrac12=5\).§\(F(x)=\tfrac12e^{2x}+\tfrac12\) nên \(F(\ln3)=\tfrac12\cdot9+\tfrac12=5\).')]]
S3 = [
 [_m(1, r'Find \(\displaystyle\int\cos4x\,dx\).§Tìm \(\displaystyle\int\cos4x\,dx\).', [r'\frac14\sin4x+C', r'4\sin4x+C', r'\sin4x+C', r'-\frac14\sin4x+C'], 'a', r'Multiply by \(\dfrac1a=\dfrac14\).§Nhân với \(\dfrac1a=\dfrac14\).'),
  _m(2, r'Find \(\displaystyle\int e^{4x}\,dx\).§Tìm \(\displaystyle\int e^{4x}\,dx\).', ['4e^{4x}+C', r'\frac14e^{4x}+C', 'e^{4x}+C', r'\frac14e^{x}+C'], 'b', r'Multiply by \(\dfrac14\).§Nhân với \(\dfrac14\).'),
  _m(3, r'Find \(\displaystyle\int\frac{1}{5x+2}\,dx\).§Tìm \(\displaystyle\int\frac{1}{5x+2}\,dx\).', [r'\ln|5x+2|+C', r'5\ln|5x+2|+C', r'-\frac15\ln|5x+2|+C', r'\frac15\ln|5x+2|+C'], 'd',
      r'\(\int\dfrac1t\,dt=\ln|t|\), times \(\dfrac15\).§\(\int\dfrac1t\,dt=\ln|t|\), nhân với \(\dfrac15\).'),
  _m(4, r'Find \(\displaystyle\int(x+3)^5\,dx\).§Tìm \(\displaystyle\int(x+3)^5\,dx\).', ['5(x+3)^4+C', '(x+3)^6+C', r'\frac{(x+3)^6}{6}+C', r'\frac{x^6}{6}+3x+C'], 'c', r'Here \(a=1\).§Ở đây \(a=1\).')],
 [_t(5, r'True or false: \(\displaystyle\int e^{2x+1}\,dx=e^{2x+1}+C\).§Đúng hay sai: \(\displaystyle\int e^{2x+1}\,dx=e^{2x+1}+C\).', 'false',
      r'We must also multiply by \(\dfrac12\): the result is \(\dfrac12e^{2x+1}+C\).§Còn phải nhân với \(\dfrac12\): kết quả là \(\dfrac12e^{2x+1}+C\).'),
  _t(6, r'True or false: \(\displaystyle\int2x\cos(x^2)\,dx=\sin(x^2)+C\).§Đúng hay sai: \(\displaystyle\int2x\cos(x^2)\,dx=\sin(x^2)+C\).', 'true',
      r'Let \(u=x^2\), \(du=2x\,dx\).§Đặt \(u=x^2\), \(du=2x\,dx\).')],
 [_s(7, r'\(\displaystyle\int\sin4x\,dx=k\cos4x+C\). Find \(k\).§\(\displaystyle\int\sin4x\,dx=k\cos4x+C\). Tìm \(k\).', '-1/4', r'\(-\dfrac14\)', 'f',
      r'\(\int\sin ax\,dx=-\dfrac1a\cos ax\).'),
  _s(8, r'\(\displaystyle\int x(x^2-1)^2dx=\dfrac{(x^2-1)^3}{k}+C\). Find \(k\).§\(\displaystyle\int x(x^2-1)^2dx=\dfrac{(x^2-1)^3}{k}+C\). Tìm \(k\).', '6', '6', 'n',
      r'Let \(u=x^2-1\), \(du=2x\,dx\): \(\dfrac12\cdot\dfrac{u^3}{3}=\dfrac{u^3}{6}\).§Đặt \(u=x^2-1\), \(du=2x\,dx\): \(\dfrac12\cdot\dfrac{u^3}{3}=\dfrac{u^3}{6}\).'),
  _s(9, r'\(\displaystyle\int2x\cos x\,dx=2x\sin x+k\cos x+C\). Find \(k\).§\(\displaystyle\int2x\cos x\,dx=2x\sin x+k\cos x+C\). Tìm \(k\).', '2', '2', 'n',
      r'With \(u=2x\), \(dv=\cos x\,dx\): \(2x\sin x-\int2\sin x\,dx=2x\sin x+2\cos x\).§Với \(u=2x\), \(dv=\cos x\,dx\): \(2x\sin x-\int2\sin x\,dx=2x\sin x+2\cos x\).'),
  _s(10, r'Let \(F\) be an antiderivative of \(f(x)=e^{4x}\) with \(F(0)=1\). Find \(F(\ln2)\).§Cho \(F\) là nguyên hàm của \(f(x)=e^{4x}\) với \(F(0)=1\). Tìm \(F(\ln2)\).', '4.75|19/4', '4.75', 'd',
      r'\(F(x)=\tfrac14e^{4x}+\tfrac34\), so \(F(\ln2)=\tfrac14\cdot16+\tfrac34=4.75\).§\(F(x)=\tfrac14e^{4x}+\tfrac34\) nên \(F(\ln2)=\tfrac14\cdot16+\tfrac34=4.75\).')]]
_T = [t for t, _ in pr]
S1 = [g for _, g in pr]
pr = LEVEL_PRACTICE(_T, {1: S1, 2: S2, 3: S3})

build('g12-antider-02', 'Techniques of Finding Antiderivatives', 'Các phương pháp tìm nguyên hàm', CAT3,
  {'level': ('Intermediate', 'Trung bình'), 'time': ('about 50 minutes', 'khoảng 50 phút'), 'before': ('antiderivatives, chain rule, product rule', 'nguyên hàm, đạo hàm hàm hợp, đạo hàm của tích')},
  [('integrate functions of a linear expression;', 'tìm nguyên hàm của hàm có [[biểu thức bậc nhất]] bên trong;'), ('use a substitution \\(u=g(x)\\);', 'dùng [[phép đổi biến]] \\(u=g(x)\\);'), ('use integration by parts for simple products;', 'dùng [[nguyên hàm từng phần]] cho tích đơn giản;'), ('explain each step in English.', 'giải thích từng bước bằng tiếng Anh.')],
  [('<b>substitution</b> – replacing part of the integrand by a new variable \\(u\\).', '[[Phép đổi biến]] – thay một phần biểu thức bằng biến mới \\(u\\).'), ('<b>integration by parts</b> – the formula \\(\\int u\\,dv=uv-\\int v\\,du\\).', '[[Nguyên hàm từng phần]] – công thức \\(\\int u\\,dv=uv-\\int v\\,du\\).'), ('<b>linear expression</b> – an expression \\(ax+b\\).', '[[Biểu thức bậc nhất]] – biểu thức \\(ax+b\\).'), ('<b>antiderivative</b> – a function whose derivative is the given function.', '[[Nguyên hàm]] – hàm số có đạo hàm bằng hàm đã cho.')],
  [('Use the substitution \\(u=x^2+1\\).', 'Dùng phép đổi biến \\(u=x^2+1\\).'), ('Replace \\(x\\,dx\\) by \\(\\tfrac12du\\).', 'Thay \\(x\\,dx\\) bằng \\(\\tfrac12du\\).'), ('Use integration by parts with \\(u=x\\).', 'Dùng nguyên hàm từng phần với \\(u=x\\).'), ('Go back to the variable \\(x\\).', 'Quay về biến \\(x\\).')],
  review, theory, ex, pr,
  [('<b>Forgetting the factor \\(\\dfrac1a\\).</b> \\(\\int f(ax+b)\\,dx\\) needs \\(\\dfrac1a\\).', '<b>Quên thừa số \\(\\dfrac1a\\).</b> \\(\\int f(ax+b)\\,dx\\) phải nhân \\(\\dfrac1a\\).'), ('<b>Not returning to \\(x\\).</b> The final answer must be in the original variable.', '<b>Không quay về biến \\(x\\).</b> Kết quả cuối phải theo biến ban đầu.'), ('<b>Choosing \\(u\\) badly in parts.</b> Take \\(u=x\\), not \\(u=e^x\\).', '<b>Chọn \\(u\\) chưa hợp lí khi lấy từng phần.</b> Nên chọn \\(u=x\\), không chọn \\(u=e^x\\).')],
  [('\\(\\int f(ax+b)\\,dx=\\dfrac1aF(ax+b)+C\\).', '\\(\\int f(ax+b)\\,dx=\\dfrac1aF(ax+b)+C\\).'), ('Substitution: choose \\(u\\), replace \\(du\\), integrate, return to \\(x\\).', 'Đổi biến: chọn \\(u\\), thay \\(du\\), lấy nguyên hàm, quay về \\(x\\).'), ('By parts: \\(\\int u\\,dv=uv-\\int v\\,du\\).', 'Từng phần: \\(\\int u\\,dv=uv-\\int v\\,du\\).')],
  [('I can integrate \\(f(ax+b)\\).', 'Em tìm được nguyên hàm của \\(f(ax+b)\\).'), ('I can use a substitution.', 'Em dùng được phép đổi biến.'), ('I can use integration by parts.', 'Em dùng được nguyên hàm từng phần.'), STD_SUMMARY_CHECK_EN()],
  'lessons/grade12/antiderivatives/techniques-of-antiderivatives.html',
  ENTRY('g12-antider-02', 'Techniques of Finding Antiderivatives', 'Use linear substitution, change of variable and integration by parts.', 'Intermediate', 50, ['g12-antider-01'], 'lessons/grade12/antiderivatives/techniques-of-antiderivatives.html', ['substitution', 'integration by parts', 'antiderivative'], order=70))

# sắp xếp lại các bài lớp 12 theo bản đồ chương trình
order = ['g12-deriv-app-01','g12-deriv-app-02','g12-mono-01','g12-mono-02','g12-mono-03','g12-optim-01','g12-vec-01','g12-coord-01','g12-coord-02','g12-stats-01','g12-antider-01','g12-antider-02']
p = os.path.join(ROOT, 'lessons.json'); d = json.load(open(p, encoding='utf-8'))
g12 = sorted([x for x in d if x['grade'] == 12], key=lambda x: order.index(x['id']) if x['id'] in order else 99)
first = next(i for i, x in enumerate(d) if x['grade'] == 12)
d = [x for x in d if x['grade'] != 12]; d[first:first] = g12
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print([x['id'] for x in d])
