# -*- coding: utf-8 -*-
"""Nội dung các bài g12-mono-01..03 – CHỈ NỘI DUNG. Bố cục, số mục, tên mục, số lớp do config/model.json quyết định."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
from mb_selfpractice import SELF
import sp_g12, re
_cap = {}
_real_build = build
def build(lid, *a, **k):               # ghi nhận ba bài cũ; cuối tệp dựng lại theo danh mục SGK (Bài 1, Bài 2)
    _cap[lid] = (list(a), k)

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

CAT = 'Monotonicity and Extrema'
TOPIC = (CAT, 'Tính đơn điệu và cực trị')
ensure_vocab([
 ('v-derivative','derivative','đạo hàm',CAT,'Find the derivative of f.','\\(f\'(x)\\)'),
 ('v-increasing','increasing function','hàm số đồng biến',CAT,'The function is increasing on (0, 2).',''),
 ('v-decreasing','decreasing function','hàm số nghịch biến',CAT,'The function is decreasing on (-1, 1).',''),
 ('v-monotonicity','monotonicity','tính đơn điệu',CAT,'Study the monotonicity of the function.',''),
 ('v-critical-point','critical point','điểm tới hạn',CAT,'Find the critical points of f.',''),
 ('v-sign-table','sign table','bảng xét dấu',CAT,'Make a sign table for f\'.',''),
 ('v-variation-table','variation table','bảng biến thiên',CAT,'Complete the variation table.',''),
 ('v-extremum','extremum','cực trị',CAT,'Find the extrema of the function.',''),
 ('v-local-maximum','local maximum','cực đại',CAT,'The function has a local maximum at x = 0.',''),
 ('v-local-minimum','local minimum','cực tiểu',CAT,'The function has a local minimum at x = 2.',''),
 ('v-second-derivative','second derivative','đạo hàm cấp hai',CAT,'Use the second derivative test.','\\(f\'\'(x)\\)'),
 ('v-discriminant','discriminant','biệt thức',CAT,'The discriminant is negative.','\\(\\Delta\\)'),
 ('v-parameter','parameter','tham số',CAT,'Find the values of the parameter m.',''),
 ('v-domain','domain','tập xác định',CAT,'State the domain of the function.',''),
 ('v-maximum-value','maximum value','giá trị lớn nhất',CAT,'Find the maximum value of f on [0, 2].',''),
 ('v-minimum-value','minimum value','giá trị nhỏ nhất',CAT,'Find the minimum value of f on [0, 2].',''),
 ('v-endpoint','endpoint','đầu mút',CAT,'Evaluate f at the endpoints.',''),
 ('v-continuous','continuous function','hàm số liên tục',CAT,'A continuous function on a closed interval.',''),
])
load_vocab()

OPEN = lambda a, b: '(%s,%s)' % (a, b)

# =====================================================================
# BÀI 1: Monotonicity of Functions
# =====================================================================
review = (T('A <b>derivative</b> tells us the slope of the tangent line. Recall these rules:', '[[Đạo hàm]] cho biết hệ số góc của tiếp tuyến. Nhắc lại các quy tắc:') +
  UL([T('\\((x^n)\'=nx^{n-1}\\)', '\\((x^n)\'=nx^{n-1}\\)'), T('\\(\\left(\\dfrac{u}{v}\\right)\'=\\dfrac{u\'v-uv\'}{v^2}\\)', '\\(\\left(\\dfrac{u}{v}\\right)\'=\\dfrac{u\'v-uv\'}{v^2}\\)')]) +
  T('The sign of a quadratic \\(ax^2+bx+c\\) (with \\(a>0\\)) is positive outside its roots and negative between them.', 'Dấu của tam thức bậc hai \\(ax^2+bx+c\\) (với \\(a>0\\)): dương ngoài hai nghiệm, âm giữa hai nghiệm.'))
theory = ('<h3>5.1 %s</h3>' % TI('Increasing and decreasing functions', 'Hàm số đồng biến, nghịch biến') +
  BOX('mint', ('Definition', 'Định nghĩa'),
    T('Let \\(K\\) be an interval. A function \\(f\\) is an <b>increasing function</b> on \\(K\\) if \\(x_1<x_2\\) implies \\(f(x_1)<f(x_2)\\). It is a <b>decreasing function</b> on \\(K\\) if \\(x_1<x_2\\) implies \\(f(x_1)>f(x_2)\\), for all \\(x_1,x_2\\in K\\).',
      'Cho \\(K\\) là một khoảng. Hàm số \\(f\\) là [[hàm số đồng biến]] trên \\(K\\) nếu \\(x_1<x_2\\) thì \\(f(x_1)<f(x_2)\\); là [[hàm số nghịch biến]] trên \\(K\\) nếu \\(x_1<x_2\\) thì \\(f(x_1)>f(x_2)\\), với mọi \\(x_1,x_2\\in K\\).')) +
  '<h3>5.2 %s</h3>' % TI('The derivative test for monotonicity', 'Dùng đạo hàm xét tính đơn điệu') +
  BOX('mint', ('Theorem', 'Định lí'),
    T('Let \\(f\\) have a derivative on an interval \\(K\\).', 'Cho hàm số \\(f\\) có [[đạo hàm]] trên khoảng \\(K\\).'),
    UL([T('If \\(f\'(x)>0\\) for all \\(x\\in K\\), then \\(f\\) is increasing on \\(K\\).', 'Nếu \\(f\'(x)>0\\) với mọi \\(x\\in K\\) thì \\(f\\) đồng biến trên \\(K\\).'),
        T('If \\(f\'(x)<0\\) for all \\(x\\in K\\), then \\(f\\) is decreasing on \\(K\\).', 'Nếu \\(f\'(x)<0\\) với mọi \\(x\\in K\\) thì \\(f\\) nghịch biến trên \\(K\\).'),
        T('The statements stay true if \\(f\'(x)=0\\) at only finitely many points of \\(K\\).', 'Các kết luận vẫn đúng nếu \\(f\'(x)=0\\) chỉ tại hữu hạn điểm của \\(K\\).')])) +
  '<h3>5.3 %s</h3>' % TI('Method', 'Các bước xét tính đơn điệu') +
  OL([T('Find the domain.', 'Tìm [[tập xác định]].'), T('Compute \\(f\'(x)\\) and find where \\(f\'(x)=0\\) or \\(f\'(x)\\) does not exist.', 'Tính \\(f\'(x)\\); tìm các điểm \\(f\'(x)=0\\) hoặc \\(f\'(x)\\) không xác định.'),
      T('Make a sign table of \\(f\'\\) (a variation table).', 'Lập [[bảng xét dấu]] của \\(f\'\\) (hoặc [[bảng biến thiên]]).'), T('Read the intervals where \\(f\\) increases and decreases.', 'Đọc các khoảng đồng biến, nghịch biến.')]))

theory += GRAPH({'view': [-1.8, 4.6, -4.2, 3.2], 'functions': [{'f': 'x^3-3x^2+1', 'label': 'y = x³ − 3x² + 1'}], 'mark': {'extrema': [0]}, 'monotone': {'f': 0}},
  cap=('Green: the function is increasing. Orange: decreasing. The dots are the local extrema, where the derivative changes sign.', 'Màu xanh: hàm số đồng biến. Màu cam: nghịch biến. Các chấm là điểm cực trị, nơi đạo hàm đổi dấu.'),
  alt=('Graph of a cubic with colored increasing and decreasing parts', ''), height=340)

ex = EXAMPLE(1, ('Basic', 'Cơ bản'), ('A cubic function', 'Hàm số bậc ba'),
  T('Find the intervals on which \\(f(x)=x^3-3x^2+1\\) is increasing or decreasing.', 'Tìm các khoảng đồng biến, nghịch biến của hàm số \\(f(x)=x^3-3x^2+1\\).'),
  ('The domain is \\(\\mathbb{R}\\). We need the sign of \\(f\'\\).', 'Tập xác định là \\(\\mathbb{R}\\). Cần xét dấu của \\(f\'\\).'),
  [T('\\(f\'(x)=3x^2-6x=3x(x-2)\\), and \\(f\'(x)=0\\) at \\(x=0\\) and \\(x=2\\).', '\\(f\'(x)=3x^2-6x=3x(x-2)\\) và \\(f\'(x)=0\\) tại \\(x=0\\), \\(x=2\\).'),
   T('Sign of \\(f\'\\): positive for \\(x<0\\), negative for \\(0<x<2\\), positive for \\(x>2\\).', 'Dấu của \\(f\'\\): dương khi \\(x<0\\), âm khi \\(0<x<2\\), dương khi \\(x>2\\).'),
   T('So \\(f\\) is increasing on \\((-\\infty,0)\\) and \\((2,+\\infty)\\), and decreasing on \\((0,2)\\).', 'Vậy \\(f\\) đồng biến trên \\((-\\infty,0)\\) và \\((2,+\\infty)\\), nghịch biến trên \\((0,2)\\).')],
  'increasing on \\((-\\infty,0)\\), \\((2,+\\infty)\\); decreasing on \\((0,2)\\)')
ex += EXAMPLE(2, ('Intermediate', 'Trung bình'), ('A rational function', 'Hàm phân thức'),
  T('Study the monotonicity of \\(f(x)=\\dfrac{2x+1}{x-1}\\).', 'Xét tính đơn điệu của hàm số \\(f(x)=\\dfrac{2x+1}{x-1}\\).'),
  ('The domain is \\(\\mathbb{R}\\setminus\\{1\\}\\), which is not one interval.', 'Tập xác định là \\(\\mathbb{R}\\setminus\\{1\\}\\), không phải một khoảng duy nhất.'),
  [T('\\(f\'(x)=\\dfrac{2(x-1)-(2x+1)}{(x-1)^2}=\\dfrac{-3}{(x-1)^2}\\).', '\\(f\'(x)=\\dfrac{2(x-1)-(2x+1)}{(x-1)^2}=\\dfrac{-3}{(x-1)^2}\\).'),
   T('\\(f\'(x)<0\\) for every \\(x\\ne1\\).', '\\(f\'(x)<0\\) với mọi \\(x\\ne1\\).'),
   T('So \\(f\\) is decreasing on \\((-\\infty,1)\\) and on \\((1,+\\infty)\\). We must not say it is decreasing on the union.', 'Vậy \\(f\\) nghịch biến trên \\((-\\infty,1)\\) và trên \\((1,+\\infty)\\). Không được nói nghịch biến trên hợp của hai khoảng.')],
  'decreasing on \\((-\\infty,1)\\) and on \\((1,+\\infty)\\)')
ex += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('A sum with a fraction', 'Tổng có phân thức'),
  T('Study the monotonicity of \\(f(x)=x+\\dfrac{4}{x}\\).', 'Xét tính đơn điệu của hàm số \\(f(x)=x+\\dfrac{4}{x}\\).'),
  ('The domain is \\(x\\ne0\\). Write \\(f\'\\) as one fraction.', 'Tập xác định \\(x\\ne0\\). Viết \\(f\'\\) thành một phân thức.'),
  [T('\\(f\'(x)=1-\\dfrac{4}{x^2}=\\dfrac{x^2-4}{x^2}\\). It is zero at \\(x=\\pm2\\).', '\\(f\'(x)=1-\\dfrac{4}{x^2}=\\dfrac{x^2-4}{x^2}\\). Nó bằng 0 tại \\(x=\\pm2\\).'),
   T('\\(f\'>0\\) for \\(x<-2\\) and \\(x>2\\); \\(f\'<0\\) for \\(-2<x<0\\) and \\(0<x<2\\).', '\\(f\'>0\\) khi \\(x<-2\\) và \\(x>2\\); \\(f\'<0\\) khi \\(-2<x<0\\) và \\(0<x<2\\).'),
   T('So \\(f\\) is increasing on \\((-\\infty,-2)\\) and \\((2,+\\infty)\\); decreasing on \\((-2,0)\\) and \\((0,2)\\).', 'Vậy \\(f\\) đồng biến trên \\((-\\infty,-2)\\) và \\((2,+\\infty)\\); nghịch biến trên \\((-2,0)\\) và \\((0,2)\\).')],
  'increasing on \\((-\\infty,-2)\\), \\((2,+\\infty)\\); decreasing on \\((-2,0)\\), \\((0,2)\\)')
ex += EXAMPLE(4, ('Advanced', 'Nâng cao'), ('A parameter', 'Bài toán tham số'),
  T('Find all values of the <b>parameter</b> \\(m\\) such that \\(f(x)=x^3+3x^2+mx+1\\) is increasing on \\(\\mathbb{R}\\).', 'Tìm tất cả các giá trị của [[tham số]] \\(m\\) để hàm số \\(f(x)=x^3+3x^2+mx+1\\) đồng biến trên \\(\\mathbb{R}\\).'),
  ('We need \\(f\'(x)\\ge0\\) for all \\(x\\). A quadratic with \\(a>0\\) is never negative when its <b>discriminant</b> is at most 0.', 'Cần \\(f\'(x)\\ge0\\) với mọi \\(x\\). Tam thức có \\(a>0\\) không âm với mọi \\(x\\) khi [[biệt thức]] không dương.'),
  [T('\\(f\'(x)=3x^2+6x+m\\), with \\(a=3>0\\).', '\\(f\'(x)=3x^2+6x+m\\), có \\(a=3>0\\).'),
   T('\\(\\Delta\'=9-3m\\le0\\) gives \\(m\\ge3\\).', '\\(\\Delta\'=9-3m\\le0\\) cho \\(m\\ge3\\).'),
   T('For \\(m=3\\), \\(f\'(x)=3(x+1)^2\\) is zero only at \\(x=-1\\), so \\(f\\) is still increasing.', 'Với \\(m=3\\), \\(f\'(x)=3(x+1)^2\\) chỉ bằng 0 tại \\(x=-1\\) nên \\(f\\) vẫn đồng biến.')],
  '\\(m\\ge3\\)')
pr = [
 ('A. Multiple Choice', 'A. Trắc nghiệm nhiều lựa chọn'), [
  MCQ(1, ('On which interval is \\(f(x)=-x^2+4x\\) increasing?', 'Hàm số \\(f(x)=-x^2+4x\\) đồng biến trên khoảng nào?'), ['(-\\infty,2)', '(2,+\\infty)', '(-\\infty,4)', '(0,4)'], 'a',
      ('Answer: a. \\(f\'(x)=-2x+4>0\\) when \\(x<2\\).', 'Đáp án a. \\(f\'(x)=-2x+4>0\\) khi \\(x<2\\).')),
  MCQ(2, ('On which interval is \\(f(x)=x^3-3x\\) decreasing?', 'Hàm số \\(f(x)=x^3-3x\\) nghịch biến trên khoảng nào?'), ['(-\\infty,-1)', '(-1,1)', '(1,+\\infty)', '\\mathbb{R}'], 'b',
      ('Answer: b. \\(f\'(x)=3x^2-3<0\\) exactly when \\(-1<x<1\\).', 'Đáp án b. \\(f\'(x)=3x^2-3<0\\) đúng khi \\(-1<x<1\\).')),
  MCQ(3, ('Let \\(f(x)=\\dfrac{x-2}{x+1}\\). On which interval is \\(f\\) increasing?', 'Cho \\(f(x)=\\dfrac{x-2}{x+1}\\). Hàm số đồng biến trên khoảng nào?'), ['(-2,0)', '(-1,2)', '(-\\infty,0)', '\\mathbb{R}'], 'b',
      ('Answer: b. \\(f\'(x)=\\dfrac{3}{(x+1)^2}>0\\) for \\(x\\ne-1\\), but an interval must not contain \\(-1\\). Only \\((-1,2)\\) qualifies.', 'Đáp án b. \\(f\'(x)=\\dfrac{3}{(x+1)^2}>0\\) với \\(x\\ne-1\\), nhưng khoảng không được chứa \\(-1\\). Chỉ có \\((-1,2)\\) thỏa mãn.')),
  MCQ(4, ('Let \\(f\'(x)=(x-1)(x+2)^2\\). On which interval is \\(f\\) increasing?', 'Cho \\(f\'(x)=(x-1)(x+2)^2\\). Hàm số đồng biến trên khoảng nào?'), ['(-\\infty,1)', '(1,+\\infty)', '(-2,1)', '(-\\infty,-2)'], 'b',
      ('Answer: b. \\((x+2)^2\\ge0\\), so \\(f\'>0\\) exactly when \\(x>1\\).', 'Đáp án b. \\((x+2)^2\\ge0\\) nên \\(f\'>0\\) đúng khi \\(x>1\\).'))]
]
pr = [pr] if False else [(pr[0], pr[1]), (('B. True or False', 'B. Đúng hoặc sai'), [
  TF(5, ('True or false: if \\(f\'(x)>0\\) on \\((a,b)\\), then \\(f\\) is increasing on \\((a,b)\\).', 'Đúng hay sai: nếu \\(f\'(x)>0\\) trên \\((a,b)\\) thì \\(f\\) đồng biến trên \\((a,b)\\).'), 'true',
     ('True. This is the derivative test.', 'Đúng. Đây là định lí về dấu của đạo hàm.')),
  TF(6, ('True or false: \\(f(x)=\\dfrac1x\\) is decreasing on its whole domain \\(\\mathbb{R}\\setminus\\{0\\}\\).', 'Đúng hay sai: \\(f(x)=\\dfrac1x\\) nghịch biến trên toàn bộ tập xác định \\(\\mathbb{R}\\setminus\\{0\\}\\).'), 'false',
     ('False. It is decreasing on \\((-\\infty,0)\\) and on \\((0,+\\infty)\\) separately. But \\(-1<1\\) while \\(f(-1)=-1<f(1)=1\\).', 'Sai. Hàm số nghịch biến trên từng khoảng \\((-\\infty,0)\\) và \\((0,+\\infty)\\). Nhưng \\(-1<1\\) mà \\(f(-1)=-1<f(1)=1\\).'))]),
 (('C. Short Answer', 'C. Trả lời ngắn'), [
  SHORT(7, ('Write the interval on which \\(f(x)=x^2-6x+5\\) is decreasing.', 'Viết khoảng mà hàm số \\(f(x)=x^2-6x+5\\) nghịch biến.'), '(-inf,3)|(-inf,3]', 'interval',
        ('Format: (-inf,3). You may type inf for infinity.', 'Định dạng: (-inf,3). Có thể gõ inf cho vô cực.'),
        ('Answer: \\((-\\infty,3)\\). \\(f\'(x)=2x-6<0\\) when \\(x<3\\).', 'Đáp án: \\((-\\infty,3)\\). \\(f\'(x)=2x-6<0\\) khi \\(x<3\\).')),
  SHORT(8, ('How many solutions does \\(f\'(x)=0\\) have for \\(f(x)=x^4-2x^2\\)?', 'Với \\(f(x)=x^4-2x^2\\), phương trình \\(f\'(x)=0\\) có bao nhiêu nghiệm?'), '3', 'number',
        ('Enter a whole number.', 'Nhập một số nguyên.'),
        ('Answer: 3. \\(f\'(x)=4x^3-4x=4x(x-1)(x+1)\\).', 'Đáp án: 3. \\(f\'(x)=4x^3-4x=4x(x-1)(x+1)\\).')),
  SHORT(9, ('Find the smallest integer \\(m\\) such that \\(f(x)=x^3+3x^2+mx\\) is increasing on \\(\\mathbb{R}\\).', 'Tìm số nguyên \\(m\\) nhỏ nhất để \\(f(x)=x^3+3x^2+mx\\) đồng biến trên \\(\\mathbb{R}\\).'), '3', 'number',
        ('Enter a whole number.', 'Nhập một số nguyên.'),
        ('Answer: 3. We need \\(9-3m\\le0\\), so \\(m\\ge3\\).', 'Đáp án: 3. Cần \\(9-3m\\le0\\) nên \\(m\\ge3\\).')),
  SHORT(10, ('Find the smallest integer \\(m\\) such that \\(f(x)=\\dfrac{mx+1}{x-1}\\) is decreasing on each interval of its domain.', 'Tìm số nguyên \\(m\\) nhỏ nhất để \\(f(x)=\\dfrac{mx+1}{x-1}\\) nghịch biến trên từng khoảng xác định.'), '0', 'number',
        ('Enter a whole number.', 'Nhập một số nguyên.'),
        ('Answer: 0. \\(f\'(x)=\\dfrac{-m-1}{(x-1)^2}<0\\) exactly when \\(m>-1\\), so the smallest integer is 0.', 'Đáp án: 0. \\(f\'(x)=\\dfrac{-m-1}{(x-1)^2}<0\\) đúng khi \\(m>-1\\), nên số nguyên nhỏ nhất là 0.'))])]
S2 = [
 [_m(1, r'On which interval is \(f(x)=-x^2+6x\) increasing?§Hàm số \(f(x)=-x^2+6x\) đồng biến trên khoảng nào?', [r'(3,+\infty)', r'(0,6)', r'(-\infty,3)', r'(-\infty,6)'], 'c',
      r'\(f′(x)=-2x+6>0\) when \(x<3\).§\(f′(x)=-2x+6>0\) khi \(x<3\).'),
  _m(2, r'On which interval is \(f(x)=x^3-12x\) decreasing?§Hàm số \(f(x)=x^3-12x\) nghịch biến trên khoảng nào?', [r'(-2,2)', r'(-\infty,-2)', r'(2,+\infty)', r'\mathbb{R}'], 'a',
      r'\(f′(x)=3x^2-12<0\) exactly when \(-2<x<2\).§\(f′(x)=3x^2-12<0\) đúng khi \(-2<x<2\).'),
  _m(3, r'Let \(f(x)=\dfrac{x-3}{x+2}\). On which interval is \(f\) increasing?§Cho \(f(x)=\dfrac{x-3}{x+2}\). Hàm số đồng biến trên khoảng nào?', [r'(-3,0)', r'(-4,-1)', r'(-\infty,-1)', r'(-2,3)'], 'd',
      r'\(f′(x)=\dfrac{5}{(x+2)^2}>0\) for \(x\ne-2\), but an interval must not contain \(-2\). Only \((-2,3)\) qualifies.§\(f′(x)=\dfrac{5}{(x+2)^2}>0\) với \(x\ne-2\), nhưng khoảng không được chứa \(-2\). Chỉ có \((-2,3)\) thỏa mãn.'),
  _m(4, r'Let \(f′(x)=(x-2)(x+1)^2\). On which interval is \(f\) increasing?§Cho \(f′(x)=(x-2)(x+1)^2\). Hàm số đồng biến trên khoảng nào?', [r'(-\infty,2)', r'(2,+\infty)', r'(-1,2)', r'(-\infty,-1)'], 'b',
      r'\((x+1)^2\ge0\), so \(f′>0\) exactly when \(x>2\).§\((x+1)^2\ge0\) nên \(f′>0\) đúng khi \(x>2\).')],
 [_t(5, r'True or false: if \(f′(x)<0\) on \((a,b)\), then \(f\) is decreasing on \((a,b)\).§Đúng hay sai: nếu \(f′(x)<0\) trên \((a,b)\) thì \(f\) nghịch biến trên \((a,b)\).', 'true',
      r'This is the derivative test.§Đây là định lí về dấu của đạo hàm.'),
  _t(6, r'True or false: \(f(x)=-\dfrac1x\) is increasing on its whole domain \(\mathbb{R}\setminus\{0\}\).§Đúng hay sai: \(f(x)=-\dfrac1x\) đồng biến trên toàn bộ tập xác định \(\mathbb{R}\setminus\{0\}\).', 'false',
      r'It is increasing on \((-\infty,0)\) and on \((0,+\infty)\) separately. But \(-1<1\) while \(f(-1)=1>f(1)=-1\).§Hàm số đồng biến trên từng khoảng \((-\infty,0)\) và \((0,+\infty)\). Nhưng \(-1<1\) mà \(f(-1)=1>f(1)=-1\).')],
 [_s(7, r'Write the interval on which \(f(x)=x^2-8x+3\) is decreasing.§Viết khoảng mà hàm số \(f(x)=x^2-8x+3\) nghịch biến.', '(-inf,4)|(-inf,4]', r'\((-\infty,4)\)', 'i',
      r'\(f′(x)=2x-8<0\) when \(x<4\).§\(f′(x)=2x-8<0\) khi \(x<4\).'),
  _s(8, r'How many solutions does \(f′(x)=0\) have for \(f(x)=x^3-3x^2\)?§Với \(f(x)=x^3-3x^2\), phương trình \(f′(x)=0\) có bao nhiêu nghiệm?', '2', '2', 'w',
      r'\(f′(x)=3x^2-6x=3x(x-2)\), so \(x=0\) or \(x=2\).§\(f′(x)=3x^2-6x=3x(x-2)\) nên \(x=0\) hoặc \(x=2\).'),
  _s(9, r'Find the smallest integer \(m\) such that \(f(x)=x^3+6x^2+mx\) is increasing on \(\mathbb{R}\).§Tìm số nguyên \(m\) nhỏ nhất để \(f(x)=x^3+6x^2+mx\) đồng biến trên \(\mathbb{R}\).', '12', '12', 'w',
      r'\(f′(x)=3x^2+12x+m\). We need \(\Delta′=36-3m\le0\), so \(m\ge12\).§\(f′(x)=3x^2+12x+m\). Cần \(\Delta′=36-3m\le0\) nên \(m\ge12\).'),
  _s(10, r'Find the smallest integer \(m\) such that \(f(x)=\dfrac{mx+4}{x+2}\) is increasing on each interval of its domain.§Tìm số nguyên \(m\) nhỏ nhất để \(f(x)=\dfrac{mx+4}{x+2}\) đồng biến trên từng khoảng xác định.', '3', '3', 'w',
      r'\(f′(x)=\dfrac{2m-4}{(x+2)^2}>0\) exactly when \(m>2\), so the smallest integer is 3.§\(f′(x)=\dfrac{2m-4}{(x+2)^2}>0\) đúng khi \(m>2\), nên số nguyên nhỏ nhất là 3.')]]
S3 = [
 [_m(1, r'On which interval is \(f(x)=-x^2-4x\) increasing?§Hàm số \(f(x)=-x^2-4x\) đồng biến trên khoảng nào?', [r'(-2,+\infty)', r'(-3,-1)', r'(-4,0)', r'(-\infty,-2)'], 'd',  # M-107: thay (-inf,-4) (khoảng con của (-inf,-2), cũng đúng)
      r'\(f′(x)=-2x-4>0\) when \(x<-2\).§\(f′(x)=-2x-4>0\) khi \(x<-2\).'),
  _m(2, r'On which interval is \(f(x)=x^3-3x^2\) decreasing?§Hàm số \(f(x)=x^3-3x^2\) nghịch biến trên khoảng nào?', [r'(-\infty,0)', r'(0,2)', r'(2,+\infty)', r'(-2,0)'], 'b',
      r'\(f′(x)=3x(x-2)<0\) exactly when \(0<x<2\).§\(f′(x)=3x(x-2)<0\) đúng khi \(0<x<2\).'),
  _m(3, r'Let \(f(x)=\dfrac{2x-1}{x+1}\). On which interval is \(f\) increasing?§Cho \(f(x)=\dfrac{2x-1}{x+1}\). Hàm số đồng biến trên khoảng nào?', [r'(-2,2)', r'(-3,0)', r'(-1,4)', r'(-\infty,0)'], 'c',
      r'\(f′(x)=\dfrac{3}{(x+1)^2}>0\) for \(x\ne-1\), but an interval must not contain \(-1\). Only \((-1,4)\) qualifies.§\(f′(x)=\dfrac{3}{(x+1)^2}>0\) với \(x\ne-1\), nhưng khoảng không được chứa \(-1\). Chỉ có \((-1,4)\) thỏa mãn.'),
  _m(4, r'Let \(f′(x)=(x-4)(x+3)^2\). On which interval is \(f\) increasing?§Cho \(f′(x)=(x-4)(x+3)^2\). Hàm số đồng biến trên khoảng nào?', [r'(4,+\infty)', r'(-3,4)', r'(-\infty,4)', r'(-\infty,-3)'], 'a',
      r'\((x+3)^2\ge0\), so \(f′>0\) exactly when \(x>4\).§\((x+3)^2\ge0\) nên \(f′>0\) đúng khi \(x>4\).')],
 [_t(5, r'True or false: if \(f′(x)>0\) on \((a,b)\) and \(a<x_1<x_2<b\), then \(f(x_1)<f(x_2)\).§Đúng hay sai: nếu \(f′(x)>0\) trên \((a,b)\) và \(a<x_1<x_2<b\) thì \(f(x_1)<f(x_2)\).', 'true',
      r'By the derivative test, \(f\) is increasing on \((a,b)\).§Theo định lí về dấu của đạo hàm, \(f\) đồng biến trên \((a,b)\).'),
  _t(6, r'True or false: \(f(x)=\dfrac{x+2}{x-1}\) is decreasing on its whole domain \(\mathbb{R}\setminus\{1\}\).§Đúng hay sai: \(f(x)=\dfrac{x+2}{x-1}\) nghịch biến trên toàn bộ tập xác định \(\mathbb{R}\setminus\{1\}\).', 'false',
      r'It is decreasing on \((-\infty,1)\) and on \((1,+\infty)\) separately. But \(0<2\) while \(f(0)=-2<f(2)=4\).§Hàm số nghịch biến trên từng khoảng \((-\infty,1)\) và \((1,+\infty)\). Nhưng \(0<2\) mà \(f(0)=-2<f(2)=4\).')],
 [_s(7, r'Write the interval on which \(f(x)=x^2-10x+7\) is decreasing.§Viết khoảng mà hàm số \(f(x)=x^2-10x+7\) nghịch biến.', '(-inf,5)|(-inf,5]', r'\((-\infty,5)\)', 'i',
      r'\(f′(x)=2x-10<0\) when \(x<5\).§\(f′(x)=2x-10<0\) khi \(x<5\).'),
  _s(8, r'How many solutions does \(f′(x)=0\) have for \(f(x)=x^4+2x^2\)?§Với \(f(x)=x^4+2x^2\), phương trình \(f′(x)=0\) có bao nhiêu nghiệm?', '1', '1', 'w',
      r'\(f′(x)=4x^3+4x=4x(x^2+1)\), which is zero only at \(x=0\).§\(f′(x)=4x^3+4x=4x(x^2+1)\) chỉ bằng 0 tại \(x=0\).'),
  _s(9, r'Find the smallest integer \(m\) such that \(f(x)=x^3+x^2+mx\) is increasing on \(\mathbb{R}\).§Tìm số nguyên \(m\) nhỏ nhất để \(f(x)=x^3+x^2+mx\) đồng biến trên \(\mathbb{R}\).', '1', '1', 'w',
      r'\(f′(x)=3x^2+2x+m\). We need \(\Delta′=1-3m\le0\), so \(m\ge\dfrac13\) and the smallest integer is 1.§\(f′(x)=3x^2+2x+m\). Cần \(\Delta′=1-3m\le0\) nên \(m\ge\dfrac13\), số nguyên nhỏ nhất là 1.'),
  _s(10, r'Find the smallest integer \(m\) such that \(f(x)=\dfrac{mx+3}{x-2}\) is decreasing on each interval of its domain.§Tìm số nguyên \(m\) nhỏ nhất để \(f(x)=\dfrac{mx+3}{x-2}\) nghịch biến trên từng khoảng xác định.', '-1', r'\(-1\)', 'w',
      r'\(f′(x)=\dfrac{-2m-3}{(x-2)^2}<0\) exactly when \(m>-\dfrac32\), so the smallest integer is \(-1\).§\(f′(x)=\dfrac{-2m-3}{(x-2)^2}<0\) đúng khi \(m>-\dfrac32\), nên số nguyên nhỏ nhất là \(-1\).')]]
_T = [t for t, _ in pr]
S1 = [g for _, g in pr]
pr = LEVEL_PRACTICE(_T, {1: S1, 2: S2, 3: S3})

build('g12-mono-01', 'Monotonicity of Functions', 'Tính đơn điệu của hàm số', TOPIC,
  {'level': ('Intermediate', 'Trung bình'), 'time': ('about 45 minutes', 'khoảng 45 phút'), 'before': ('derivative rules, sign of a quadratic, intervals', 'quy tắc đạo hàm, dấu tam thức bậc hai, khoảng')},
  [('use the derivative to find where a function increases or decreases;', 'dùng [[đạo hàm]] để tìm các khoảng [[hàm số đồng biến]], [[hàm số nghịch biến]];'),
   ('write a correct sign table and conclusion;', 'lập [[bảng xét dấu]] và kết luận đúng;'),
   ('solve a simple <b>parameter</b> problem;', 'giải bài toán [[tham số]] đơn giản;'),
   ('state the answer in English.', 'phát biểu kết quả bằng tiếng Anh.')],
  [('<b>increasing function</b> – a function whose values go up as \\(x\\) goes up.', '[[Hàm số đồng biến]] – giá trị tăng khi \\(x\\) tăng.'),
   ('<b>decreasing function</b> – a function whose values go down as \\(x\\) goes up.', '[[Hàm số nghịch biến]] – giá trị giảm khi \\(x\\) tăng.'),
   ('<b>monotonicity</b> – whether a function increases or decreases.', '[[Tính đơn điệu]] – việc hàm số tăng hay giảm.'),
   ('<b>derivative</b> – the rate of change \\(f\'(x)\\).', '[[Đạo hàm]] – tốc độ thay đổi \\(f\'(x)\\).'),
   ('<b>sign table</b> – a table showing where \\(f\'\\) is positive or negative.', '[[Bảng xét dấu]] – bảng cho biết \\(f\'\\) dương hay âm ở đâu.'),
   ('<b>parameter</b> – a letter such as \\(m\\) that stands for a fixed unknown number.', '[[Tham số]] – chữ như \\(m\\) đại diện cho một số chưa biết cố định.'),
   ('<b>discriminant</b> – the number \\(\\Delta=b^2-4ac\\).', '[[Biệt thức]] – số \\(\\Delta=b^2-4ac\\).'),
   ('<b>domain</b> – all values of \\(x\\) for which \\(f(x)\\) is defined.', '[[Tập xác định]] – mọi giá trị \\(x\\) để \\(f(x)\\) có nghĩa.')],
  [('Find the intervals on which the function is increasing.', 'Tìm các khoảng mà hàm số đồng biến.'), ('Make a sign table for the derivative.', 'Lập bảng xét dấu của đạo hàm.'),
   ('The function is decreasing on the interval \\((0,2)\\).', 'Hàm số nghịch biến trên khoảng \\((0,2)\\).'), ('Find all values of \\(m\\) such that \\(f\\) is increasing on \\(\\mathbb{R}\\).', 'Tìm tất cả giá trị của \\(m\\) để \\(f\\) đồng biến trên \\(\\mathbb{R}\\).')],
  review, theory, ex, pr,
  [('<b>Using the union of intervals.</b> For \\(\\dfrac{2x+1}{x-1}\\) write “decreasing on each interval”, not on \\((-\\infty,1)\\cup(1,+\\infty)\\).', '<b>Dùng hợp các khoảng.</b> Với \\(\\dfrac{2x+1}{x-1}\\) phải viết “nghịch biến trên từng khoảng”, không viết trên \\((-\\infty,1)\\cup(1,+\\infty)\\).'),
   ('<b>Forgetting the domain.</b> Points where \\(f\\) is not defined split the intervals.', '<b>Quên tập xác định.</b> Các điểm hàm số không xác định chia nhỏ các khoảng.'),
   ('<b>Wrong inequality for \\(m\\).</b> “Increasing on \\(\\mathbb{R}\\)” means \\(f\'\\ge0\\) (with isolated zeros allowed), so check the case \\(\\Delta=0\\).', '<b>Sai dấu bất đẳng thức với \\(m\\).</b> “Đồng biến trên \\(\\mathbb{R}\\)” nghĩa là \\(f\'\\ge0\\) (cho phép bằng 0 tại điểm rời rạc), nên phải kiểm tra trường hợp \\(\\Delta=0\\).')],
  [('If \\(f\'>0\\) on \\(K\\), \\(f\\) is increasing on \\(K\\); if \\(f\'<0\\), it is decreasing.', 'Nếu \\(f\'>0\\) trên \\(K\\) thì \\(f\\) đồng biến; nếu \\(f\'<0\\) thì nghịch biến.'),
   ('Steps: domain, \\(f\'\\), roots of \\(f\'\\), sign table, conclusion.', 'Các bước: tập xác định, \\(f\'\\), nghiệm của \\(f\'\\), bảng xét dấu, kết luận.'),
   ('For parameter problems on \\(\\mathbb{R}\\), use the discriminant of \\(f\'\\).', 'Với bài toán tham số trên \\(\\mathbb{R}\\), dùng biệt thức của \\(f\'\\).')],
  [('I can find the intervals where a function increases or decreases.', 'Em tìm được các khoảng đồng biến, nghịch biến của hàm số.'), ('I can make a correct sign table.', 'Em lập đúng bảng xét dấu.'),
   ('I can solve a simple parameter problem.', 'Em giải được bài toán tham số đơn giản.'), ('I understand the English instructions in this lesson.', 'Em hiểu các yêu cầu bằng tiếng Anh trong bài này.')],
  'lessons/grade12/monotonicity-extrema/monotonicity-of-functions.html',
  ENTRY('g12-mono-01', 'Monotonicity of Functions', 'Use the derivative to find where a function increases or decreases.', 'Intermediate', 45, [], 'lessons/grade12/monotonicity-extrema/monotonicity-of-functions.html', ['monotonicity', 'increasing', 'decreasing', 'derivative'], order=30))

# =====================================================================
# BÀI 2: Local Extrema
# =====================================================================
review2 = (T('From the last lesson: the sign of \\(f\'\\) tells us where \\(f\\) increases or decreases. A <b>critical point</b> is a point where \\(f\'(x)=0\\) or \\(f\'(x)\\) does not exist.', 'Từ bài trước: dấu của \\(f\'\\) cho biết \\(f\\) đồng biến hay nghịch biến. [[Điểm tới hạn]] là điểm mà \\(f\'(x)=0\\) hoặc \\(f\'(x)\\) không xác định.') +
  T('The <b>second derivative</b> \\(f\'\'\\) is the derivative of \\(f\'\\). For example, if \\(f(x)=x^3-3x^2\\), then \\(f\'(x)=3x^2-6x\\) and \\(f\'\'(x)=6x-6\\).', '[[Đạo hàm cấp hai]] \\(f\'\'\\) là đạo hàm của \\(f\'\\). Ví dụ, nếu \\(f(x)=x^3-3x^2\\) thì \\(f\'(x)=3x^2-6x\\) và \\(f\'\'(x)=6x-6\\).'))
theory2 = ('<h3>5.1 %s</h3>' % TI('Local maximum and local minimum', 'Cực đại và cực tiểu') +
  BOX('mint', ('Definition', 'Định nghĩa'),
    T('The point \\(x_0\\) is a <b>local maximum</b> of \\(f\\) if there is an interval \\((a,b)\\) containing \\(x_0\\) such that \\(f(x)<f(x_0)\\) for all \\(x\\in(a,b)\\setminus\\{x_0\\}\\). For a <b>local minimum</b> the inequality is \\(f(x)>f(x_0)\\). Both are called <b>extrema</b>.',
      'Điểm \\(x_0\\) là điểm [[cực đại]] của \\(f\\) nếu có khoảng \\((a,b)\\) chứa \\(x_0\\) sao cho \\(f(x)<f(x_0)\\) với mọi \\(x\\in(a,b)\\setminus\\{x_0\\}\\). Với điểm [[cực tiểu]] thì \\(f(x)>f(x_0)\\). Cả hai gọi chung là [[cực trị]].')) +
  '<h3>5.2 %s</h3>' % TI('First derivative test', 'Điều kiện đủ thứ nhất') +
  BOX('mint', ('Theorem', 'Định lí'), T('Let \\(f\\) be continuous at \\(x_0\\) and have a derivative near \\(x_0\\) (except possibly at \\(x_0\\)).', 'Cho \\(f\\) liên tục tại \\(x_0\\) và có đạo hàm ở lân cận \\(x_0\\) (có thể trừ \\(x_0\\)).'),
    UL([T('If \\(f\'\\) changes from positive to negative at \\(x_0\\), then \\(x_0\\) is a local maximum.', 'Nếu \\(f\'\\) đổi dấu từ dương sang âm tại \\(x_0\\) thì \\(x_0\\) là điểm cực đại.'),
        T('If \\(f\'\\) changes from negative to positive at \\(x_0\\), then \\(x_0\\) is a local minimum.', 'Nếu \\(f\'\\) đổi dấu từ âm sang dương tại \\(x_0\\) thì \\(x_0\\) là điểm cực tiểu.'),
        T('If \\(f\'\\) does not change sign, there is no extremum at \\(x_0\\).', 'Nếu \\(f\'\\) không đổi dấu thì \\(x_0\\) không là điểm cực trị.')])) +
  '<h3>5.3 %s</h3>' % TI('Second derivative test', 'Điều kiện đủ thứ hai') +
  BOX('mint', ('Theorem', 'Định lí'), T('Suppose \\(f\'(x_0)=0\\) and \\(f\'\'(x_0)\\) exists.', 'Giả sử \\(f\'(x_0)=0\\) và tồn tại \\(f\'\'(x_0)\\).'),
    UL([T('If \\(f\'\'(x_0)<0\\), then \\(x_0\\) is a local maximum.', 'Nếu \\(f\'\'(x_0)<0\\) thì \\(x_0\\) là điểm cực đại.'), T('If \\(f\'\'(x_0)>0\\), then \\(x_0\\) is a local minimum.', 'Nếu \\(f\'\'(x_0)>0\\) thì \\(x_0\\) là điểm cực tiểu.'),
        T('If \\(f\'\'(x_0)=0\\), the test fails; use the first derivative test.', 'Nếu \\(f\'\'(x_0)=0\\) thì không kết luận được; dùng điều kiện đủ thứ nhất.')])))
theory2 += GRAPH({'view': [-1.8, 4.6, -4.2, 3.2], 'functions': [{'f': 'x^3-3x^2+1', 'label': 'y = x³ − 3x² + 1'}], 'mark': {'extrema': [0]},
  'tangent': {'f': 0, 'at': [0, 1, 2], 'min': -1, 'max': 3.5}},
  cap=('Tangent lines at x = 0, 1, 2. At the extrema (x = 0 and x = 2) the tangent is horizontal, so f′(x₀) = 0; at x = 1 the slope is f′(1) = −3.', 'Tiếp tuyến tại x = 0, 1, 2. Tại hai điểm cực trị (x = 0 và x = 2) tiếp tuyến nằm ngang nên f′(x₀) = 0; tại x = 1 hệ số góc là f′(1) = −3.'),
  alt=('Cubic graph with three tangent lines', ''), height=340)

ex2 = EXAMPLE(5, ('Basic', 'Cơ bản'), ('Sign change of the derivative', 'Đổi dấu của đạo hàm'),
  T('Find the extrema of \\(f(x)=x^3-3x^2+1\\).', 'Tìm cực trị của hàm số \\(f(x)=x^3-3x^2+1\\).'),
  ('Find the roots of \\(f\'\\), then check the sign change.', 'Tìm nghiệm của \\(f\'\\), rồi xét đổi dấu.'),
  [T('\\(f\'(x)=3x(x-2)\\), zero at \\(x=0\\) and \\(x=2\\).', '\\(f\'(x)=3x(x-2)\\), bằng 0 tại \\(x=0\\) và \\(x=2\\).'),
   T('\\(f\'\\) changes from \\(+\\) to \\(-\\) at \\(x=0\\): local maximum, \\(f(0)=1\\).', '\\(f\'\\) đổi dấu từ \\(+\\) sang \\(-\\) tại \\(x=0\\): cực đại, \\(f(0)=1\\).'),
   T('\\(f\'\\) changes from \\(-\\) to \\(+\\) at \\(x=2\\): local minimum, \\(f(2)=8-12+1=-3\\).', '\\(f\'\\) đổi dấu từ \\(-\\) sang \\(+\\) tại \\(x=2\\): cực tiểu, \\(f(2)=8-12+1=-3\\).')],
  'local maximum \\(f(0)=1\\); local minimum \\(f(2)=-3\\)')
ex2 += EXAMPLE(6, ('Intermediate', 'Trung bình'), ('The second derivative test', 'Dùng đạo hàm cấp hai'),
  T('Find the extrema of \\(f(x)=x^4-2x^2+3\\).', 'Tìm cực trị của hàm số \\(f(x)=x^4-2x^2+3\\).'),
  ('Find \\(f\'\\) and \\(f\'\'\\), then test each critical point.', 'Tính \\(f\'\\) và \\(f\'\'\\), rồi xét từng điểm tới hạn.'),
  [T('\\(f\'(x)=4x(x^2-1)\\), zero at \\(x=-1,\\ 0,\\ 1\\). Also \\(f\'\'(x)=12x^2-4\\).', '\\(f\'(x)=4x(x^2-1)\\), bằng 0 tại \\(x=-1,\\ 0,\\ 1\\). Và \\(f\'\'(x)=12x^2-4\\).'),
   T('\\(f\'\'(0)=-4<0\\): local maximum, \\(f(0)=3\\).', '\\(f\'\'(0)=-4<0\\): cực đại, \\(f(0)=3\\).'),
   T('\\(f\'\'(\\pm1)=8>0\\): local minima, \\(f(\\pm1)=2\\).', '\\(f\'\'(\\pm1)=8>0\\): cực tiểu, \\(f(\\pm1)=2\\).')],
  'local maximum \\(f(0)=3\\); local minima \\(f(\\pm1)=2\\)')
ex2 += EXAMPLE(7, ('Intermediate', 'Trung bình'), ('Zero derivative, no extremum', 'Đạo hàm bằng 0 nhưng không có cực trị'),
  T('Does \\(f(x)=x^3\\) have an extremum at \\(x=0\\)?', 'Hàm số \\(f(x)=x^3\\) có cực trị tại \\(x=0\\) không?'),
  ('Check the sign of \\(f\'\\) on both sides of 0.', 'Xét dấu của \\(f\'\\) ở hai phía của 0.'),
  [T('\\(f\'(x)=3x^2\\), so \\(f\'(0)=0\\).', '\\(f\'(x)=3x^2\\) nên \\(f\'(0)=0\\).'),
   T('But \\(f\'(x)>0\\) for \\(x<0\\) and for \\(x>0\\). It does not change sign.', 'Nhưng \\(f\'(x)>0\\) khi \\(x<0\\) và khi \\(x>0\\). Nó không đổi dấu.'),
   T('So there is no extremum. \\(f\'(x_0)=0\\) is necessary, not sufficient.', 'Vậy không có cực trị. Điều kiện \\(f\'(x_0)=0\\) là cần, chưa đủ.')],
  'No extremum at \\(x=0\\)')
ex2 += EXAMPLE(8, ('Advanced', 'Nâng cao'), ('A parameter', 'Bài toán tham số'),
  T('Find all values of \\(m\\) such that \\(f(x)=x^3-3x^2+mx\\) has two extreme points.', 'Tìm tất cả giá trị của \\(m\\) để hàm số \\(f(x)=x^3-3x^2+mx\\) có hai điểm cực trị.'),
  ('Two extreme points need \\(f\'\\) to have two different roots and to change sign at them.', 'Có hai điểm cực trị khi \\(f\'\\) có hai nghiệm phân biệt và đổi dấu tại đó.'),
  [T('\\(f\'(x)=3x^2-6x+m\\) is a quadratic.', '\\(f\'(x)=3x^2-6x+m\\) là tam thức bậc hai.'),
   T('Two distinct roots: \\(\\Delta\'=9-3m>0\\), so \\(m<3\\).', 'Hai nghiệm phân biệt: \\(\\Delta\'=9-3m>0\\) nên \\(m<3\\).')],
  '\\(m<3\\)')
pr2 = [(('A. Multiple Choice', 'A. Trắc nghiệm nhiều lựa chọn'), [
  MCQ(11, ('At which \\(x\\) does \\(f(x)=x^2-4x+1\\) have a local minimum?', 'Hàm số \\(f(x)=x^2-4x+1\\) đạt cực tiểu tại \\(x\\) bằng bao nhiêu?'), ['x=-2', 'x=2', 'x=4', 'x=1'], 'b', ('Answer: b. \\(f\'(x)=2x-4=0\\) at \\(x=2\\) and \\(f\'\'=2>0\\).', 'Đáp án b. \\(f\'(x)=2x-4=0\\) tại \\(x=2\\) và \\(f\'\'=2>0\\).')),
  MCQ(12, ('At which \\(x\\) does \\(f(x)=-x^3+3x\\) have a local maximum?', 'Hàm số \\(f(x)=-x^3+3x\\) đạt cực đại tại \\(x\\) bằng bao nhiêu?'), ['x=-1', 'x=0', 'x=1', 'x=3'], 'c', ('Answer: c. \\(f\'(x)=-3x^2+3=0\\) at \\(x=\\pm1\\), and \\(f\'\'(1)=-6<0\\).', 'Đáp án c. \\(f\'(x)=-3x^2+3=0\\) tại \\(x=\\pm1\\), và \\(f\'\'(1)=-6<0\\).')),
  MCQ(13, ('Let \\(f\'(x)=x(x-1)^2(x+2)\\). How many extreme points does \\(f\\) have?', 'Cho \\(f\'(x)=x(x-1)^2(x+2)\\). Hàm số \\(f\\) có bao nhiêu điểm cực trị?'), ['1', '2', '3', '4'], 'b', ('Answer: b. \\(f\'\\) changes sign at \\(x=0\\) and \\(x=-2\\), but not at \\(x=1\\) because \\((x-1)^2\\ge0\\).', 'Đáp án b. \\(f\'\\) đổi dấu tại \\(x=0\\) và \\(x=-2\\), nhưng không đổi dấu tại \\(x=1\\) vì \\((x-1)^2\\ge0\\).'))]),
 (('B. True or False', 'B. Đúng hoặc sai'), [
  TF(14, ('True or false: if \\(f\'(x_0)=0\\), then \\(x_0\\) is an extreme point.', 'Đúng hay sai: nếu \\(f\'(x_0)=0\\) thì \\(x_0\\) là điểm cực trị.'), 'false', ('False. For \\(f(x)=x^3\\), \\(f\'(0)=0\\) but there is no extremum.', 'Sai. Với \\(f(x)=x^3\\), \\(f\'(0)=0\\) nhưng không có cực trị.')),
  TF(15, ('True or false: \\(f(x)=|x|\\) has a local minimum at \\(x=0\\), although \\(f\'(0)\\) does not exist.', 'Đúng hay sai: \\(f(x)=|x|\\) đạt cực tiểu tại \\(x=0\\) dù không tồn tại \\(f\'(0)\\).'), 'true', ('True. \\(f(x)\\ge0=f(0)\\) near 0, and \\(f\'\\) changes from \\(-1\\) to \\(1\\).', 'Đúng. \\(f(x)\\ge0=f(0)\\) gần 0, và \\(f\'\\) đổi từ \\(-1\\) sang \\(1\\).')),
  TF(16, ('True or false: \\(f(x)=x^4\\) has a local minimum at \\(x=0\\) even though \\(f\'\'(0)=0\\).', 'Đúng hay sai: \\(f(x)=x^4\\) đạt cực tiểu tại \\(x=0\\) dù \\(f\'\'(0)=0\\).'), 'true', ('True. \\(f\'(x)=4x^3\\) changes from negative to positive at 0. The second derivative test simply fails here.', 'Đúng. \\(f\'(x)=4x^3\\) đổi dấu từ âm sang dương tại 0. Điều kiện đủ thứ hai không kết luận được ở đây.'))]),
 (('C. Short Answer', 'C. Trả lời ngắn'), [
  SHORT(17, ('Find the local minimum value of \\(f(x)=x^3-3x\\).', 'Tìm giá trị cực tiểu của hàm số \\(f(x)=x^3-3x\\).'), '-2', 'number', ('Enter a number.', 'Nhập một số.'), ('Answer: \\(-2\\). The local minimum is at \\(x=1\\): \\(f(1)=1-3=-2\\).', 'Đáp án: \\(-2\\). Cực tiểu tại \\(x=1\\): \\(f(1)=1-3=-2\\).')),
  SHORT(18, ('How many extreme points does \\(f(x)=x^4-2x^2\\) have?', 'Hàm số \\(f(x)=x^4-2x^2\\) có bao nhiêu điểm cực trị?'), '3', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'), ('Answer: 3 (two minima and one maximum).', 'Đáp án: 3 (hai cực tiểu và một cực đại).')),
  SHORT(19, ('Find the largest integer \\(m\\) such that \\(f(x)=x^3-3x^2+mx\\) has two extreme points.', 'Tìm số nguyên \\(m\\) lớn nhất để \\(f(x)=x^3-3x^2+mx\\) có hai điểm cực trị.'), '2', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'), ('Answer: 2. We need \\(m<3\\).', 'Đáp án: 2. Cần \\(m<3\\).')),
  SHORT(20, ('Find the local minimum value of \\(f(x)=x+\\dfrac4x\\) for \\(x>0\\).', 'Tìm giá trị cực tiểu của \\(f(x)=x+\\dfrac4x\\) với \\(x>0\\).'), '4', 'number', ('Enter a number.', 'Nhập một số.'), ('Answer: 4. \\(f\'(x)=1-\\dfrac4{x^2}=0\\) at \\(x=2\\), \\(f\'\'(2)=1>0\\), and \\(f(2)=2+2=4\\).', 'Đáp án: 4. \\(f\'(x)=1-\\dfrac4{x^2}=0\\) tại \\(x=2\\), \\(f\'\'(2)=1>0\\) và \\(f(2)=2+2=4\\).'))])]
S2 = [
 [_m(11, r'At which \(x\) does \(f(x)=x^2-6x+2\) have a local minimum?§Hàm số \(f(x)=x^2-6x+2\) đạt cực tiểu tại \(x\) bằng bao nhiêu?', ['x=6', 'x=-3', 'x=2', 'x=3'], 'd',
      r'\(f′(x)=2x-6=0\) at \(x=3\) and \(f″=2>0\).§\(f′(x)=2x-6=0\) tại \(x=3\) và \(f″=2>0\).'),
  _m(12, r'At which \(x\) does \(f(x)=-x^3+12x\) have a local maximum?§Hàm số \(f(x)=-x^3+12x\) đạt cực đại tại \(x\) bằng bao nhiêu?', ['x=2', 'x=-2', 'x=0', 'x=12'], 'a',
      r'\(f′(x)=-3x^2+12=0\) at \(x=\pm2\), and \(f″(2)=-12<0\).§\(f′(x)=-3x^2+12=0\) tại \(x=\pm2\), và \(f″(2)=-12<0\).'),
  _m(13, r'Let \(f′(x)=x^2(x-1)(x+2)(x-3)\). How many extreme points does \(f\) have?§Cho \(f′(x)=x^2(x-1)(x+2)(x-3)\). Hàm số \(f\) có bao nhiêu điểm cực trị?', ['1', '2', '3', '4'], 'c',
      r'\(f′\) changes sign at \(x=1\), \(x=-2\) and \(x=3\), but not at \(x=0\) because \(x^2\ge0\).§\(f′\) đổi dấu tại \(x=1\), \(x=-2\) và \(x=3\), nhưng không đổi dấu tại \(x=0\) vì \(x^2\ge0\).')],
 [_t(14, r'True or false: if \(f′(x_0)=0\) and \(f″(x_0)=0\), then \(x_0\) is never an extreme point.§Đúng hay sai: nếu \(f′(x_0)=0\) và \(f″(x_0)=0\) thì \(x_0\) không bao giờ là điểm cực trị.', 'false',
      r'For \(f(x)=x^4\), \(f′(0)=f″(0)=0\) but \(x=0\) is a local minimum.§Với \(f(x)=x^4\), \(f′(0)=f″(0)=0\) nhưng \(x=0\) là điểm cực tiểu.'),
  _t(15, r'True or false: \(f(x)=|x-1|\) has a local minimum at \(x=1\), although \(f′(1)\) does not exist.§Đúng hay sai: \(f(x)=|x-1|\) đạt cực tiểu tại \(x=1\) dù không tồn tại \(f′(1)\).', 'true',
      r'\(f(x)\ge0=f(1)\) near 1, and \(f′\) changes from \(-1\) to \(1\).§\(f(x)\ge0=f(1)\) gần 1, và \(f′\) đổi từ \(-1\) sang \(1\).'),
  _t(16, r'True or false: \(f(x)=-x^4\) has a local maximum at \(x=0\) even though \(f″(0)=0\).§Đúng hay sai: \(f(x)=-x^4\) đạt cực đại tại \(x=0\) dù \(f″(0)=0\).', 'true',
      r'\(f′(x)=-4x^3\) changes from positive to negative at 0. The second derivative test simply fails here.§\(f′(x)=-4x^3\) đổi dấu từ dương sang âm tại 0. Điều kiện đủ thứ hai không kết luận được ở đây.')],
 [_s(17, r'Find the local minimum value of \(f(x)=x^3-12x\).§Tìm giá trị cực tiểu của hàm số \(f(x)=x^3-12x\).', '-16', r'\(-16\)', 'n',
      r'The local minimum is at \(x=2\): \(f(2)=8-24=-16\).§Cực tiểu tại \(x=2\): \(f(2)=8-24=-16\).'),
  _s(18, r'How many extreme points does \(f(x)=x^4+4x^2\) have?§Hàm số \(f(x)=x^4+4x^2\) có bao nhiêu điểm cực trị?', '1', '1', 'w',
      r'\(f′(x)=4x^3+8x=4x(x^2+2)\) is zero only at \(x=0\), and \(f′\) changes from negative to positive there.§\(f′(x)=4x^3+8x=4x(x^2+2)\) chỉ bằng 0 tại \(x=0\), và \(f′\) đổi dấu từ âm sang dương tại đó.'),
  _s(19, r'Find the largest integer \(m\) such that \(f(x)=x^3-6x^2+mx\) has two extreme points.§Tìm số nguyên \(m\) lớn nhất để \(f(x)=x^3-6x^2+mx\) có hai điểm cực trị.', '11', '11', 'w',
      r'\(f′(x)=3x^2-12x+m\). We need \(\Delta′=36-3m>0\), so \(m<12\).§\(f′(x)=3x^2-12x+m\). Cần \(\Delta′=36-3m>0\) nên \(m<12\).'),
  _s(20, r'Find the local minimum value of \(f(x)=2x+\dfrac8x\) for \(x>0\).§Tìm giá trị cực tiểu của \(f(x)=2x+\dfrac8x\) với \(x>0\).', '8', '8', 'n',
      r'\(f′(x)=2-\dfrac8{x^2}=0\) at \(x=2\), \(f″(2)=2>0\), and \(f(2)=4+4=8\).§\(f′(x)=2-\dfrac8{x^2}=0\) tại \(x=2\), \(f″(2)=2>0\) và \(f(2)=4+4=8\).')]]
S3 = [
 [_m(11, r'At which \(x\) does \(f(x)=x^2+2x-5\) have a local minimum?§Hàm số \(f(x)=x^2+2x-5\) đạt cực tiểu tại \(x\) bằng bao nhiêu?', ['x=1', 'x=-2', 'x=-1', 'x=2'], 'c',
      r'\(f′(x)=2x+2=0\) at \(x=-1\) and \(f″=2>0\).§\(f′(x)=2x+2=0\) tại \(x=-1\) và \(f″=2>0\).'),
  _m(12, r'At which \(x\) does \(f(x)=x^3-12x\) have a local maximum?§Hàm số \(f(x)=x^3-12x\) đạt cực đại tại \(x\) bằng bao nhiêu?', ['x=2', 'x=-2', 'x=0', 'x=4'], 'b',
      r'\(f′(x)=3x^2-12=0\) at \(x=\pm2\), and \(f″(-2)=-12<0\).§\(f′(x)=3x^2-12=0\) tại \(x=\pm2\), và \(f″(-2)=-12<0\).'),
  _m(13, r'Let \(f′(x)=(x-5)(x+1)^2(x-2)^2\). How many extreme points does \(f\) have?§Cho \(f′(x)=(x-5)(x+1)^2(x-2)^2\). Hàm số \(f\) có bao nhiêu điểm cực trị?', ['1', '2', '3', '4'], 'a',
      r'\(f′\) changes sign only at \(x=5\); at \(x=-1\) and \(x=2\) the squared factors do not change sign.§\(f′\) chỉ đổi dấu tại \(x=5\); tại \(x=-1\) và \(x=2\) các thừa số bình phương không đổi dấu.')],
 [_t(14, r'True or false: \(f(x)=x^3+1\) has a local minimum at \(x=0\) because \(f′(0)=0\).§Đúng hay sai: \(f(x)=x^3+1\) đạt cực tiểu tại \(x=0\) vì \(f′(0)=0\).', 'false',
      r'\(f′(x)=3x^2\ge0\) does not change sign at 0, so there is no extremum.§\(f′(x)=3x^2\ge0\) không đổi dấu tại 0 nên không có cực trị.'),
  _t(15, r'True or false: \(f(x)=|x|+3\) has a local minimum at \(x=0\), although \(f′(0)\) does not exist.§Đúng hay sai: \(f(x)=|x|+3\) đạt cực tiểu tại \(x=0\) dù không tồn tại \(f′(0)\).', 'true',
      r'\(f(x)\ge3=f(0)\) near 0, and \(f′\) changes from \(-1\) to \(1\).§\(f(x)\ge3=f(0)\) gần 0, và \(f′\) đổi từ \(-1\) sang \(1\).'),
  _t(16, r'True or false: \(f(x)=(x-1)^4\) has a local minimum at \(x=1\) even though \(f″(1)=0\).§Đúng hay sai: \(f(x)=(x-1)^4\) đạt cực tiểu tại \(x=1\) dù \(f″(1)=0\).', 'true',
      r'\(f′(x)=4(x-1)^3\) changes from negative to positive at 1. The second derivative test fails here.§\(f′(x)=4(x-1)^3\) đổi dấu từ âm sang dương tại 1. Điều kiện đủ thứ hai không kết luận được ở đây.')],
 [_s(17, r'Find the local minimum value of \(f(x)=x^3-3x^2\).§Tìm giá trị cực tiểu của hàm số \(f(x)=x^3-3x^2\).', '-4', r'\(-4\)', 'n',
      r'\(f′(x)=3x(x-2)\), \(f″(2)=6>0\), so the local minimum is \(f(2)=8-12=-4\).§\(f′(x)=3x(x-2)\), \(f″(2)=6>0\) nên giá trị cực tiểu là \(f(2)=8-12=-4\).'),
  _s(18, r'How many extreme points does \(f(x)=x^3-3x\) have?§Hàm số \(f(x)=x^3-3x\) có bao nhiêu điểm cực trị?', '2', '2', 'w',
      r'\(f′(x)=3x^2-3=3(x-1)(x+1)\) changes sign at \(x=1\) and \(x=-1\).§\(f′(x)=3x^2-3=3(x-1)(x+1)\) đổi dấu tại \(x=1\) và \(x=-1\).'),
  _s(19, r'Find the largest integer \(m\) such that \(f(x)=x^3+x^2+mx\) has two extreme points.§Tìm số nguyên \(m\) lớn nhất để \(f(x)=x^3+x^2+mx\) có hai điểm cực trị.', '0', '0', 'w',
      r'\(f′(x)=3x^2+2x+m\). We need \(\Delta′=1-3m>0\), so \(m<\dfrac13\) and the largest integer is 0.§\(f′(x)=3x^2+2x+m\). Cần \(\Delta′=1-3m>0\) nên \(m<\dfrac13\), số nguyên lớn nhất là 0.'),
  _s(20, r'Find the local minimum value of \(f(x)=x+\dfrac{25}{x}\) for \(x>0\).§Tìm giá trị cực tiểu của \(f(x)=x+\dfrac{25}{x}\) với \(x>0\).', '10', '10', 'n',
      r'\(f′(x)=1-\dfrac{25}{x^2}=0\) at \(x=5\), \(f″(5)>0\), and \(f(5)=5+5=10\).§\(f′(x)=1-\dfrac{25}{x^2}=0\) tại \(x=5\), \(f″(5)>0\) và \(f(5)=5+5=10\).')]]
_T = [t for t, _ in pr2]
S1 = [g for _, g in pr2]
pr2 = LEVEL_PRACTICE(_T, {1: S1, 2: S2, 3: S3})

build('g12-mono-02', 'Local Extrema', 'Cực trị của hàm số', TOPIC,
  {'level': ('Intermediate', 'Trung bình'), 'time': ('about 45 minutes', 'khoảng 45 phút'), 'before': ('monotonicity of functions, second derivative', 'tính đơn điệu của hàm số, đạo hàm cấp hai')},
  [('define a local maximum and a local minimum;', 'định nghĩa điểm [[cực đại]] và điểm [[cực tiểu]];'), ('find extrema with the first and second derivative tests;', 'tìm [[cực trị]] bằng hai điều kiện đủ;'),
   ('explain why \\(f\'(x_0)=0\\) is not enough;', 'giải thích vì sao \\(f\'(x_0)=0\\) chưa đủ;'), ('say the results in English.', 'phát biểu kết quả bằng tiếng Anh.')],
  [('<b>extremum</b> (plural: extrema) – a local maximum or a local minimum.', '[[Cực trị]] – điểm cực đại hoặc cực tiểu.'), ('<b>local maximum</b> – a point where \\(f\\) is larger than at nearby points.', '[[Cực đại]] – điểm mà \\(f\\) lớn hơn ở các điểm lân cận.'),
   ('<b>local minimum</b> – a point where \\(f\\) is smaller than at nearby points.', '[[Cực tiểu]] – điểm mà \\(f\\) nhỏ hơn ở các điểm lân cận.'), ('<b>critical point</b> – a point where \\(f\'=0\\) or \\(f\'\\) does not exist.', '[[Điểm tới hạn]] – điểm mà \\(f\'=0\\) hoặc \\(f\'\\) không xác định.'),
   ('<b>second derivative</b> – the derivative of the derivative, \\(f\'\'\\).', '[[Đạo hàm cấp hai]] – đạo hàm của đạo hàm, \\(f\'\'\\).'), ('<b>variation table</b> – a table of the sign of \\(f\'\\) and the behavior of \\(f\\).', '[[Bảng biến thiên]] – bảng ghi dấu \\(f\'\\) và chiều biến thiên của \\(f\\).')],
  [('Find the local extrema of the function.', 'Tìm các cực trị của hàm số.'), ('The function has a local maximum at \\(x=0\\).', 'Hàm số đạt cực đại tại \\(x=0\\).'), ('Use the second derivative test.', 'Dùng điều kiện đủ thứ hai (đạo hàm cấp hai).'), ('The derivative changes sign at this point.', 'Đạo hàm đổi dấu tại điểm này.')],
  review2, theory2, ex2, pr2,
  [('<b>Treating every root of \\(f\'\\) as an extremum.</b> The sign of \\(f\'\\) must change.', '<b>Coi mọi nghiệm của \\(f\'\\) là cực trị.</b> Dấu của \\(f\'\\) phải đổi.'),
   ('<b>Mixing the point and the value.</b> The local maximum is at \\(x=0\\); the maximum value is \\(f(0)\\).', '<b>Nhầm điểm cực trị với giá trị cực trị.</b> Cực đại đạt tại \\(x=0\\); giá trị cực đại là \\(f(0)\\).'),
   ('<b>Trusting the second derivative test when \\(f\'\'(x_0)=0\\).</b> Then use the sign of \\(f\'\\).', '<b>Tin điều kiện đủ thứ hai khi \\(f\'\'(x_0)=0\\).</b> Khi đó phải xét dấu \\(f\'\\).')],
  [('A local extremum needs \\(f\'\\) to change sign.', 'Cực trị cần \\(f\'\\) đổi dấu.'), ('\\(f\'\'(x_0)<0\\) gives a maximum; \\(f\'\'(x_0)>0\\) gives a minimum.', '\\(f\'\'(x_0)<0\\) cho cực đại; \\(f\'\'(x_0)>0\\) cho cực tiểu.'), ('\\(f\'(x_0)=0\\) is necessary but not sufficient.', '\\(f\'(x_0)=0\\) là điều kiện cần, chưa đủ.')],
  [('I can find local extrema using the sign of \\(f\'\\).', 'Em tìm được cực trị bằng dấu của \\(f\'\\).'), ('I can use the second derivative test.', 'Em dùng được đạo hàm cấp hai để tìm cực trị.'), ('I can explain why \\(f\'(x_0)=0\\) is not enough.', 'Em giải thích được vì sao \\(f\'(x_0)=0\\) chưa đủ.'), ('I understand the English instructions in this lesson.', 'Em hiểu các yêu cầu bằng tiếng Anh trong bài này.')],
  'lessons/grade12/monotonicity-extrema/local-extrema.html',
  ENTRY('g12-mono-02', 'Local Extrema', 'Find local maxima and minima with the first and second derivative tests.', 'Intermediate', 45, ['g12-mono-01'], 'lessons/grade12/monotonicity-extrema/local-extrema.html', ['extrema', 'local maximum', 'local minimum', 'derivative'], order=40))

# =====================================================================
# BÀI 3: Maximum and Minimum Values
# =====================================================================
review3 = T('You can already find the critical points of a function and the sign of \\(f\'\\). A <b>continuous function</b> has no jumps or holes on its interval. Now we compare function values to find the largest and the smallest.', 'Em đã biết tìm điểm tới hạn và xét dấu \\(f\'\\). [[Hàm số liên tục]] không bị đứt đoạn trên khoảng đang xét. Bây giờ ta so sánh các giá trị hàm số để tìm giá trị lớn nhất và nhỏ nhất.')
theory3 = ('<h3>5.1 %s</h3>' % TI('Definitions', 'Định nghĩa') +
  BOX('mint', ('Definition', 'Định nghĩa'), T('The <b>maximum value</b> of \\(f\\) on \\(K\\) is a number \\(M=f(x_0)\\) with \\(x_0\\in K\\) and \\(f(x)\\le M\\) for all \\(x\\in K\\). The <b>minimum value</b> is defined in the same way with \\(f(x)\\ge m\\). We write \\(\\max_K f\\) and \\(\\min_K f\\).',
     '[[Giá trị lớn nhất]] của \\(f\\) trên \\(K\\) là số \\(M=f(x_0)\\) với \\(x_0\\in K\\) và \\(f(x)\\le M\\) với mọi \\(x\\in K\\). [[Giá trị nhỏ nhất]] định nghĩa tương tự với \\(f(x)\\ge m\\). Kí hiệu \\(\\max_K f\\) và \\(\\min_K f\\).')) +
  '<h3>5.2 %s</h3>' % TI('On a closed interval \\([a,b]\\)', 'Trên đoạn \\([a,b]\\)') +
  BOX('mint', ('Theorem', 'Định lí'), T('A continuous function on \\([a,b]\\) always has a maximum value and a minimum value.', 'Hàm số liên tục trên đoạn \\([a,b]\\) luôn có giá trị lớn nhất và giá trị nhỏ nhất.')) +
  OL([T('Find the critical points of \\(f\\) that lie inside \\((a,b)\\).', 'Tìm các [[điểm tới hạn]] của \\(f\\) nằm trong \\((a,b)\\).'), T('Compute \\(f\\) at these points and at the two <b>endpoints</b> \\(a\\) and \\(b\\).', 'Tính \\(f\\) tại các điểm đó và tại hai [[đầu mút]] \\(a\\), \\(b\\).'), T('The largest number is the maximum value; the smallest is the minimum value.', 'Số lớn nhất là giá trị lớn nhất; số nhỏ nhất là giá trị nhỏ nhất.')]) +
  '<h3>5.3 %s</h3>' % TI('On other intervals', 'Trên khoảng khác') +
  T('On \\((a,b)\\), \\((a,+\\infty)\\) and so on, make a variation table and look at the limits at the ends. A maximum or minimum may not exist.', 'Trên \\((a,b)\\), \\((a,+\\infty)\\),… hãy lập [[bảng biến thiên]] và xét giới hạn ở hai đầu. Giá trị lớn nhất hay nhỏ nhất có thể không tồn tại.'))
theory3 += GRAPH({'view': [-1.8, 3.8, -4.6, 2.6], 'functions': [{'f': 'x^3-3x^2+1', 'label': 'y = x³ − 3x² + 1'}], 'highlights': [{'f': 0, 'x': [-1, 3], 'color': '#c2410c'}],
  'points': [{'x': -1, 'y': -3, 'label': 'f(−1) = −3'}, {'x': 0, 'y': 1, 'label': 'f(0) = 1'}, {'x': 2, 'y': -3, 'label': 'f(2) = −3'}, {'x': 3, 'y': 1, 'label': 'f(3) = 1'}],
  'guides': [{'type': 'h', 'y': 1}, {'type': 'h', 'y': -3}]},
  cap=('On [−1, 3] (thick part) the greatest value is 1 and the smallest value is −3. Compare the values at the endpoints and at the critical points.', 'Trên [−1; 3] (phần đậm) giá trị lớn nhất là 1 và nhỏ nhất là −3. So sánh giá trị tại hai đầu mút và tại các điểm tới hạn.'),
  alt=('Cubic graph on a closed interval with the greatest and smallest values', ''), height=340)

ex3 = EXAMPLE(1, ('Basic', 'Cơ bản'), ('A closed interval', 'Trên một đoạn'),
  T('Find the maximum and minimum values of \\(f(x)=x^3-3x+1\\) on \\([0,2]\\).', 'Tìm giá trị lớn nhất và nhỏ nhất của \\(f(x)=x^3-3x+1\\) trên đoạn \\([0,2]\\).'),
  ('Use the three-step method on a closed interval.', 'Dùng phương pháp ba bước trên một đoạn.'),
  [T('\\(f\'(x)=3x^2-3=0\\) gives \\(x=\\pm1\\). Only \\(x=1\\) is in \\((0,2)\\).', '\\(f\'(x)=3x^2-3=0\\) cho \\(x=\\pm1\\). Chỉ \\(x=1\\) thuộc \\((0,2)\\).'),
   T('\\(f(0)=1\\), \\(f(1)=-1\\), \\(f(2)=3\\).', '\\(f(0)=1\\), \\(f(1)=-1\\), \\(f(2)=3\\).'), T('The maximum value is \\(3\\) (at \\(x=2\\)); the minimum value is \\(-1\\) (at \\(x=1\\)).', 'Giá trị lớn nhất là \\(3\\) (tại \\(x=2\\)); giá trị nhỏ nhất là \\(-1\\) (tại \\(x=1\\)).')],
  '\\(\\max=3\\), \\(\\min=-1\\)')
ex3 += EXAMPLE(2, ('Intermediate', 'Trung bình'), ('Two critical points inside', 'Hai điểm tới hạn nằm trong đoạn'),
  T('Find the maximum and minimum values of \\(f(x)=2x^3+3x^2-12x\\) on \\([-3,2]\\).', 'Tìm giá trị lớn nhất và nhỏ nhất của \\(f(x)=2x^3+3x^2-12x\\) trên đoạn \\([-3,2]\\).'),
  ('Factor \\(f\'\\) and check both roots.', 'Phân tích \\(f\'\\) và xét cả hai nghiệm.'),
  [T('\\(f\'(x)=6x^2+6x-12=6(x+2)(x-1)\\). Both \\(x=-2\\) and \\(x=1\\) are in \\((-3,2)\\).', '\\(f\'(x)=6x^2+6x-12=6(x+2)(x-1)\\). Cả \\(x=-2\\) và \\(x=1\\) đều thuộc \\((-3,2)\\).'),
   T('\\(f(-3)=9\\), \\(f(-2)=20\\), \\(f(1)=-7\\), \\(f(2)=4\\).', '\\(f(-3)=9\\), \\(f(-2)=20\\), \\(f(1)=-7\\), \\(f(2)=4\\).'), T('So the maximum value is \\(20\\) and the minimum value is \\(-7\\).', 'Vậy giá trị lớn nhất là \\(20\\) và giá trị nhỏ nhất là \\(-7\\).')],
  '\\(\\max=20\\), \\(\\min=-7\\)')
ex3 += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('An interval that is not closed', 'Khoảng không phải đoạn'),
  T('Find the minimum value of \\(f(x)=x+\\dfrac4x\\) on \\((0,+\\infty)\\). Does a maximum value exist?', 'Tìm giá trị nhỏ nhất của \\(f(x)=x+\\dfrac4x\\) trên \\((0,+\\infty)\\). Có giá trị lớn nhất không?'),
  ('There are no endpoints in the interval, so use a variation table.', 'Khoảng này không chứa đầu mút nên dùng bảng biến thiên.'),
  [T('\\(f\'(x)=1-\\dfrac4{x^2}=0\\) gives \\(x=2\\). \\(f\'<0\\) on \\((0,2)\\) and \\(f\'>0\\) on \\((2,+\\infty)\\).', '\\(f\'(x)=1-\\dfrac4{x^2}=0\\) cho \\(x=2\\). \\(f\'<0\\) trên \\((0,2)\\) và \\(f\'>0\\) trên \\((2,+\\infty)\\).'),
   T('So the minimum value is \\(f(2)=4\\).', 'Vậy giá trị nhỏ nhất là \\(f(2)=4\\).'), T('As \\(x\\to0^+\\) or \\(x\\to+\\infty\\), \\(f(x)\\to+\\infty\\), so there is no maximum value.', 'Khi \\(x\\to0^+\\) hoặc \\(x\\to+\\infty\\) thì \\(f(x)\\to+\\infty\\), nên không có giá trị lớn nhất.')],
  '\\(\\min=4\\); no maximum value')
ex3 += EXAMPLE(4, ('Advanced', 'Nâng cao'), ('An application', 'Bài toán thực tế'),
  T('A rectangle has perimeter 20 cm. Find its largest possible area.', 'Một hình chữ nhật có chu vi 20 cm. Tìm diện tích lớn nhất có thể.'),
  ('Write the area as a function of one side.', 'Viết diện tích như hàm số của một cạnh.'),
  [T('Let one side be \\(x\\) cm, so the other is \\(10-x\\), with \\(0<x<10\\). The area is \\(S(x)=x(10-x)=10x-x^2\\).', 'Gọi một cạnh là \\(x\\) cm thì cạnh kia là \\(10-x\\), với \\(0<x<10\\). Diện tích \\(S(x)=x(10-x)=10x-x^2\\).'),
   T('\\(S\'(x)=10-2x=0\\) gives \\(x=5\\). \\(S\'>0\\) for \\(x<5\\) and \\(S\'<0\\) for \\(x>5\\).', '\\(S\'(x)=10-2x=0\\) cho \\(x=5\\). \\(S\'>0\\) khi \\(x<5\\) và \\(S\'<0\\) khi \\(x>5\\).'),
   T('The maximum is \\(S(5)=25\\): the best rectangle is a square.', 'Giá trị lớn nhất là \\(S(5)=25\\): hình chữ nhật tốt nhất là hình vuông.')],
  '\\(25\\ \\text{cm}^2\\)')
pr3 = [(('A. Multiple Choice', 'A. Trắc nghiệm nhiều lựa chọn'), [
  MCQ(1, ('What is the maximum value of \\(f(x)=-x^2+2x+3\\) on \\(\\mathbb{R}\\)?', 'Giá trị lớn nhất của \\(f(x)=-x^2+2x+3\\) trên \\(\\mathbb{R}\\) là bao nhiêu?'), ['3', '4', '5', '2'], 'b', ('Answer: b. The vertex is at \\(x=1\\), and \\(f(1)=4\\).', 'Đáp án b. Đỉnh tại \\(x=1\\), và \\(f(1)=4\\).')),
  MCQ(2, ('What is the minimum value of \\(f(x)=x^2-2x\\) on \\([0,3]\\)?', 'Giá trị nhỏ nhất của \\(f(x)=x^2-2x\\) trên \\([0,3]\\) là bao nhiêu?'), ['-1', '0', '3', '-2'], 'a', ('Answer: a. \\(f(0)=0\\), \\(f(1)=-1\\), \\(f(3)=3\\).', 'Đáp án a. \\(f(0)=0\\), \\(f(1)=-1\\), \\(f(3)=3\\).')),
  MCQ(3, ('What is the minimum value of \\(f(x)=4-x^2\\) on \\([-1,3]\\)?', 'Giá trị nhỏ nhất của \\(f(x)=4-x^2\\) trên \\([-1,3]\\) là bao nhiêu?'), ['-5', '3', '4', '-1'], 'a', ('Answer: a. \\(f(-1)=3\\), \\(f(0)=4\\), \\(f(3)=-5\\).', 'Đáp án a. \\(f(-1)=3\\), \\(f(0)=4\\), \\(f(3)=-5\\).'))]),
 (('B. True or False', 'B. Đúng hoặc sai'), [
  TF(4, ('True or false: a continuous function on a closed interval \\([a,b]\\) always has a maximum value and a minimum value.', 'Đúng hay sai: hàm số liên tục trên đoạn \\([a,b]\\) luôn có giá trị lớn nhất và giá trị nhỏ nhất.'), 'true', ('True. This is the extreme value theorem.', 'Đúng. Đây là định lí về giá trị lớn nhất, nhỏ nhất của hàm liên tục trên đoạn.')),
  TF(5, ('True or false: \\(f(x)=\\dfrac1x\\) has a maximum value on \\((0,1]\\).', 'Đúng hay sai: \\(f(x)=\\dfrac1x\\) có giá trị lớn nhất trên \\((0,1]\\).'), 'false', ('False. \\(f(x)\\to+\\infty\\) as \\(x\\to0^+\\). The minimum value is \\(f(1)=1\\).', 'Sai. \\(f(x)\\to+\\infty\\) khi \\(x\\to0^+\\). Giá trị nhỏ nhất là \\(f(1)=1\\).'))]),
 (('C. Short Answer', 'C. Trả lời ngắn'), [
  SHORT(6, ('Find the maximum value of \\(f(x)=x^3-3x\\) on \\([0,2]\\).', 'Tìm giá trị lớn nhất của \\(f(x)=x^3-3x\\) trên đoạn \\([0,2]\\).'), '2', 'number', ('Enter a number.', 'Nhập một số.'), ('Answer: 2. \\(f(0)=0\\), \\(f(1)=-2\\), \\(f(2)=2\\).', 'Đáp án: 2. \\(f(0)=0\\), \\(f(1)=-2\\), \\(f(2)=2\\).')),
  SHORT(7, ('Find the minimum value of \\(f(x)=x^3-3x\\) on \\([0,2]\\).', 'Tìm giá trị nhỏ nhất của \\(f(x)=x^3-3x\\) trên đoạn \\([0,2]\\).'), '-2', 'number', ('Enter a number.', 'Nhập một số.'), ('Answer: \\(-2\\), reached at \\(x=1\\).', 'Đáp án: \\(-2\\), đạt tại \\(x=1\\).')),
  SHORT(8, ('Find the minimum value of \\(f(x)=x+\\dfrac9x\\) on \\((0,+\\infty)\\).', 'Tìm giá trị nhỏ nhất của \\(f(x)=x+\\dfrac9x\\) trên \\((0,+\\infty)\\).'), '6', 'number', ('Enter a number.', 'Nhập một số.'), ('Answer: 6. \\(f\'(x)=1-\\dfrac9{x^2}=0\\) at \\(x=3\\), and \\(f(3)=3+3=6\\).', 'Đáp án: 6. \\(f\'(x)=1-\\dfrac9{x^2}=0\\) tại \\(x=3\\) và \\(f(3)=3+3=6\\).')),
  SHORT(9, ('Find the maximum value of \\(f(x)=x^4-2x^2\\) on \\([0,2]\\).', 'Tìm giá trị lớn nhất của \\(f(x)=x^4-2x^2\\) trên đoạn \\([0,2]\\).'), '8', 'number', ('Enter a number.', 'Nhập một số.'), ('Answer: 8. \\(f(0)=0\\), \\(f(1)=-1\\), \\(f(2)=8\\).', 'Đáp án: 8. \\(f(0)=0\\), \\(f(1)=-1\\), \\(f(2)=8\\).')),
  SHORT(10, ('A rectangle has perimeter 20 cm. What is the largest possible area, in \\(\\text{cm}^2\\)?', 'Một hình chữ nhật có chu vi 20 cm. Diện tích lớn nhất là bao nhiêu \\(\\text{cm}^2\\)?'), '25', 'number', ('Enter a number.', 'Nhập một số.'), ('Answer: 25 (a square with side 5 cm).', 'Đáp án: 25 (hình vuông cạnh 5 cm).'))])]
S2 = [
 [_m(1, r'What is the maximum value of \(f(x)=-x^2+4x+1\) on \(\mathbb{R}\)?§Giá trị lớn nhất của \(f(x)=-x^2+4x+1\) trên \(\mathbb{R}\) là bao nhiêu?', ['4', '6', '5', '1'], 'c',
      r'The vertex is at \(x=2\), and \(f(2)=-4+8+1=5\).§Đỉnh tại \(x=2\), và \(f(2)=-4+8+1=5\).'),
  _m(2, r'What is the minimum value of \(f(x)=x^2-4x\) on \([0,5]\)?§Giá trị nhỏ nhất của \(f(x)=x^2-4x\) trên \([0,5]\) là bao nhiêu?', ['-4', '0', '5', '-5'], 'a',
      r'\(f(0)=0\), \(f(2)=-4\), \(f(5)=5\).§\(f(0)=0\), \(f(2)=-4\), \(f(5)=5\).'),
  _m(3, r'What is the minimum value of \(f(x)=9-x^2\) on \([-2,4]\)?§Giá trị nhỏ nhất của \(f(x)=9-x^2\) trên \([-2,4]\) là bao nhiêu?', ['5', '9', '-7', '-2'], 'c',
      r'\(f(-2)=5\), \(f(0)=9\), \(f(4)=-7\).§\(f(-2)=5\), \(f(0)=9\), \(f(4)=-7\).')],
 [_t(4, r'True or false: \(f(x)=x^2\) has both a maximum value and a minimum value on \([-1,2]\).§Đúng hay sai: \(f(x)=x^2\) có cả giá trị lớn nhất và giá trị nhỏ nhất trên đoạn \([-1,2]\).', 'true',
      r'The minimum value is \(f(0)=0\) and the maximum value is \(f(2)=4\).§Giá trị nhỏ nhất là \(f(0)=0\) và giá trị lớn nhất là \(f(2)=4\).'),
  _t(5, r'True or false: \(f(x)=\dfrac1x\) has a minimum value on \((0,1)\).§Đúng hay sai: \(f(x)=\dfrac1x\) có giá trị nhỏ nhất trên \((0,1)\).', 'false',
      r'\(f(x)\to+\infty\) as \(x\to0^+\), and \(f(x)\to1\) as \(x\to1^-\) without ever reaching 1. So there is no minimum (and no maximum).§\(f(x)\to+\infty\) khi \(x\to0^+\), và \(f(x)\to1\) khi \(x\to1^-\) nhưng không bao giờ bằng 1. Vậy không có giá trị nhỏ nhất (và cũng không có giá trị lớn nhất).')],
 [_s(6, r'Find the maximum value of \(f(x)=x^3-12x\) on \([0,4]\).§Tìm giá trị lớn nhất của \(f(x)=x^3-12x\) trên đoạn \([0,4]\).', '16', '16', 'n',
      r'\(f(0)=0\), \(f(2)=-16\), \(f(4)=16\).§\(f(0)=0\), \(f(2)=-16\), \(f(4)=16\).'),
  _s(7, r'Find the minimum value of \(f(x)=x^3-12x\) on \([0,4]\).§Tìm giá trị nhỏ nhất của \(f(x)=x^3-12x\) trên đoạn \([0,4]\).', '-16', r'\(-16\)', 'n',
      r'\(-16\), reached at \(x=2\).§\(-16\), đạt tại \(x=2\).'),
  _s(8, r'Find the minimum value of \(f(x)=x+\dfrac{16}{x}\) on \((0,+\infty)\).§Tìm giá trị nhỏ nhất của \(f(x)=x+\dfrac{16}{x}\) trên \((0,+\infty)\).', '8', '8', 'n',
      r'\(f′(x)=1-\dfrac{16}{x^2}=0\) at \(x=4\), and \(f(4)=4+4=8\).§\(f′(x)=1-\dfrac{16}{x^2}=0\) tại \(x=4\) và \(f(4)=4+4=8\).'),
  _s(9, r'Find the maximum value of \(f(x)=x^4-8x^2\) on \([0,3]\).§Tìm giá trị lớn nhất của \(f(x)=x^4-8x^2\) trên đoạn \([0,3]\).', '9', '9', 'n',
      r'\(f(0)=0\), \(f(2)=-16\), \(f(3)=9\).§\(f(0)=0\), \(f(2)=-16\), \(f(3)=9\).'),
  _s(10, r'A rectangle has perimeter 40 cm. What is the largest possible area, in \(\text{cm}^2\)?§Một hình chữ nhật có chu vi 40 cm. Diện tích lớn nhất là bao nhiêu \(\text{cm}^2\)?', '100', '100', 'n',
      r'100 (a square with side 10 cm).§100 (hình vuông cạnh 10 cm).')]]
S3 = [
 [_m(1, r'What is the maximum value of \(f(x)=-x^2-2x+5\) on \(\mathbb{R}\)?§Giá trị lớn nhất của \(f(x)=-x^2-2x+5\) trên \(\mathbb{R}\) là bao nhiêu?', ['5', '6', '7', '4'], 'b',
      r'The vertex is at \(x=-1\), and \(f(-1)=-1+2+5=6\).§Đỉnh tại \(x=-1\), và \(f(-1)=-1+2+5=6\).'),
  _m(2, r'What is the minimum value of \(f(x)=x^2-6x\) on \([0,4]\)?§Giá trị nhỏ nhất của \(f(x)=x^2-6x\) trên \([0,4]\) là bao nhiêu?', ['-8', '-9', '0', '-6'], 'b',
      r'\(f(0)=0\), \(f(3)=-9\), \(f(4)=-8\).§\(f(0)=0\), \(f(3)=-9\), \(f(4)=-8\).'),
  _m(3, r'What is the minimum value of \(f(x)=1-x^2\) on \([-3,2]\)?§Giá trị nhỏ nhất của \(f(x)=1-x^2\) trên \([-3,2]\) là bao nhiêu?', ['-3', '1', '-1', '-8'], 'd',
      r'\(f(-3)=-8\), \(f(0)=1\), \(f(2)=-3\).§\(f(-3)=-8\), \(f(0)=1\), \(f(2)=-3\).')],
 [_t(4, r'True or false: \(f(x)=x^3\) has both a maximum value and a minimum value on \([-2,1]\).§Đúng hay sai: \(f(x)=x^3\) có cả giá trị lớn nhất và giá trị nhỏ nhất trên đoạn \([-2,1]\).', 'true',
      r'The minimum value is \(f(-2)=-8\) and the maximum value is \(f(1)=1\).§Giá trị nhỏ nhất là \(f(-2)=-8\) và giá trị lớn nhất là \(f(1)=1\).'),
  _t(5, r'True or false: \(f(x)=x^2\) has a maximum value on the interval \((0,2)\).§Đúng hay sai: \(f(x)=x^2\) có giá trị lớn nhất trên khoảng \((0,2)\).', 'false',
      r'The values get close to 4 as \(x\to2^-\) but never reach it, so there is no maximum.§Giá trị tiến gần 4 khi \(x\to2^-\) nhưng không bao giờ bằng 4, nên không có giá trị lớn nhất.')],
 [_s(6, r'Find the maximum value of \(f(x)=x^3-3x^2-9x\) on \([-2,4]\).§Tìm giá trị lớn nhất của \(f(x)=x^3-3x^2-9x\) trên đoạn \([-2,4]\).', '5', '5', 'n',
      r'\(f′(x)=3(x-3)(x+1)\). \(f(-2)=-2\), \(f(-1)=5\), \(f(3)=-27\), \(f(4)=-20\).§\(f′(x)=3(x-3)(x+1)\). \(f(-2)=-2\), \(f(-1)=5\), \(f(3)=-27\), \(f(4)=-20\).'),
  _s(7, r'Find the minimum value of \(f(x)=x^3-3x^2-9x\) on \([-2,4]\).§Tìm giá trị nhỏ nhất của \(f(x)=x^3-3x^2-9x\) trên đoạn \([-2,4]\).', '-27', r'\(-27\)', 'n',
      r'\(-27\), reached at \(x=3\).§\(-27\), đạt tại \(x=3\).'),
  _s(8, r'Find the minimum value of \(f(x)=4x+\dfrac9x\) on \((0,+\infty)\).§Tìm giá trị nhỏ nhất của \(f(x)=4x+\dfrac9x\) trên \((0,+\infty)\).', '12', '12', 'n',
      r'\(f′(x)=4-\dfrac9{x^2}=0\) at \(x=\dfrac32\), and \(f\left(\dfrac32\right)=6+6=12\).§\(f′(x)=4-\dfrac9{x^2}=0\) tại \(x=\dfrac32\) và \(f\left(\dfrac32\right)=6+6=12\).'),
  _s(9, r'Find the maximum value of \(f(x)=x^4-4x^2\) on \([0,3]\).§Tìm giá trị lớn nhất của \(f(x)=x^4-4x^2\) trên đoạn \([0,3]\).', '45', '45', 'n',
      r'\(f(0)=0\), \(f(\sqrt2)=-4\), \(f(3)=45\).§\(f(0)=0\), \(f(\sqrt2)=-4\), \(f(3)=45\).'),
  _s(10, r'A rectangle has perimeter 36 cm. What is the largest possible area, in \(\text{cm}^2\)?§Một hình chữ nhật có chu vi 36 cm. Diện tích lớn nhất là bao nhiêu \(\text{cm}^2\)?', '81', '81', 'n',
      r'81 (a square with side 9 cm).§81 (hình vuông cạnh 9 cm).')]]
_T = [t for t, _ in pr3]
S1 = [g for _, g in pr3]
pr3 = LEVEL_PRACTICE(_T, {1: S1, 2: S2, 3: S3})

build('g12-mono-03', 'Maximum and Minimum Values', 'Giá trị lớn nhất và giá trị nhỏ nhất', TOPIC,
  {'level': ('Intermediate', 'Trung bình'), 'time': ('about 50 minutes', 'khoảng 50 phút'), 'before': ('critical points, local extrema, variation tables', 'điểm tới hạn, cực trị, bảng biến thiên')},
  [('find the maximum and minimum values on a closed interval;', 'tìm [[giá trị lớn nhất]] và [[giá trị nhỏ nhất]] trên một đoạn;'), ('use a variation table on other intervals;', 'dùng [[bảng biến thiên]] trên các khoảng khác;'), ('solve a simple optimization problem;', 'giải bài toán tối ưu đơn giản;'), ('explain your steps in English.', 'trình bày các bước bằng tiếng Anh.')],
  [('<b>maximum value</b> – the largest value of a function on an interval.', '[[Giá trị lớn nhất]] – giá trị lớn nhất của hàm số trên một khoảng.'), ('<b>minimum value</b> – the smallest value of a function on an interval.', '[[Giá trị nhỏ nhất]] – giá trị nhỏ nhất của hàm số trên một khoảng.'),
   ('<b>endpoint</b> – the first or last point of an interval.', '[[Đầu mút]] – điểm đầu hoặc điểm cuối của một khoảng.'), ('<b>continuous function</b> – a function whose graph has no breaks.', '[[Hàm số liên tục]] – hàm số có đồ thị không bị đứt.'),
   ('<b>critical point</b> – a point where \\(f\'=0\\) or \\(f\'\\) does not exist.', '[[Điểm tới hạn]] – điểm mà \\(f\'=0\\) hoặc \\(f\'\\) không xác định.'), ('<b>variation table</b> – a table showing how \\(f\\) increases and decreases.', '[[Bảng biến thiên]] – bảng cho biết \\(f\\) tăng giảm thế nào.')],
  [('Find the maximum and minimum values of \\(f\\) on the interval \\([0,2]\\).', 'Tìm giá trị lớn nhất và nhỏ nhất của \\(f\\) trên đoạn \\([0,2]\\).'), ('Evaluate the function at the endpoints.', 'Tính giá trị hàm số tại các đầu mút.'), ('The maximum value is reached at \\(x=2\\).', 'Giá trị lớn nhất đạt tại \\(x=2\\).'), ('Does the function have a minimum value? Explain.', 'Hàm số có giá trị nhỏ nhất không? Hãy giải thích.')],
  review3, theory3, ex3, pr3,
  [('<b>Forgetting the endpoints.</b> On \\([a,b]\\) the maximum or minimum is often at \\(a\\) or \\(b\\).', '<b>Quên các đầu mút.</b> Trên \\([a,b]\\), giá trị lớn nhất hay nhỏ nhất thường đạt tại \\(a\\) hoặc \\(b\\).'),
   ('<b>Using a critical point outside the interval.</b> Only points inside \\((a,b)\\) count.', '<b>Dùng điểm tới hạn ngoài đoạn.</b> Chỉ các điểm thuộc \\((a,b)\\) mới được xét.'),
   ('<b>Assuming a maximum always exists.</b> On an interval that is not closed, check the limits.', '<b>Cho rằng luôn có giá trị lớn nhất.</b> Trên khoảng không phải đoạn, phải xét giới hạn.')],
  [('On \\([a,b]\\): compare \\(f\\) at the critical points inside and at \\(a\\), \\(b\\).', 'Trên \\([a,b]\\): so sánh \\(f\\) tại các điểm tới hạn trong khoảng và tại \\(a\\), \\(b\\).'), ('On other intervals: use a variation table and limits.', 'Trên khoảng khác: dùng bảng biến thiên và giới hạn.'), ('For word problems: write one function of one variable, with its domain.', 'Bài toán thực tế: lập một hàm số một biến, kèm tập xác định.')],
  [('I can find max and min values on a closed interval.', 'Em tìm được giá trị lớn nhất, nhỏ nhất trên một đoạn.'), ('I can decide when a maximum or minimum does not exist.', 'Em biết khi nào không tồn tại giá trị lớn nhất hay nhỏ nhất.'), ('I can solve a simple optimization problem.', 'Em giải được bài toán tối ưu đơn giản.'), ('I understand the English instructions in this lesson.', 'Em hiểu các yêu cầu bằng tiếng Anh trong bài này.')],
  'lessons/grade12/monotonicity-extrema/maximum-and-minimum-values.html',
  ENTRY('g12-mono-03', 'Maximum and Minimum Values', 'Find the greatest and smallest values of a function on an interval.', 'Intermediate', 50, ['g12-mono-02'], 'lessons/grade12/monotonicity-extrema/maximum-and-minimum-values.html', ['maximum', 'minimum', 'optimization', 'closed interval'], order=50))


# =====================================================================
# DỰNG THEO DANH MỤC SGK: Bài 1 (gộp g12-mono-01 + g12-mono-02) và Bài 2 (g12-mono-03)
# =====================================================================
def _dedupe(L, key=lambda x: x[0]):
    out, seen = [], set()
    for x in L:
        k = key(x)
        if k not in seen: seen.add(k); out.append(x)
    return out
_term = lambda x: re.findall(r'<b>(.*?)</b>', x[0])[0] if '<b>' in x[0] else x[0]
def _relabel(parts, shift, tag):
    out = []
    for (en, vi), items, lv in parts:
        L_ = en[0]; nl = chr(ord(L_) + shift)
        out.append(((nl + en[1:] + ' – ' + tag[0], nl + vi[1:] + ' – ' + tag[1]), items, lv))
    return out
def _add_self(practice, selfset, letter, title):
    return practice + [((letter + '. ' + title[0], letter + '. ' + title[1]), selfset[lv], [lv]) for lv in (1, 2, 3)]
SELF_T = ('Self-practice: Multiple Choice', 'Tự luyện: trắc nghiệm')
TOPIC12 = ('Applications of Derivatives', 'Ứng dụng đạo hàm')

(a1, _), (a2, _), (a3, _) = _cap['g12-mono-01'], _cap['g12-mono-02'], _cap['g12-mono-03']
_pr = _relabel(a1[10], 0, ('monotonicity', 'tính đơn điệu')) + _relabel(a2[10], 3, ('extrema', 'cực trị'))
_prac1 = _add_self(_pr, SELF(sp_g12.M1, start=21, avoid=[t[1] for t in _pr]), 'G', SELF_T)
_prac1.sort(key=lambda t: t[2][0])         # giữ thứ tự theo mức học
lesson(id='g12-mono-01', title_en='Monotonicity and Extrema of Functions', title_vi='Tính đơn điệu và cực trị của hàm số', topic=TOPIC12,
  catalog_title_vi='Tính đơn điệu và cực trị của hàm số', description_vi='Bài 1 – Dùng đạo hàm xét chiều biến thiên, tìm cực trị bằng bảng xét dấu và đạo hàm cấp hai; bài toán tham số đơn giản.',
  tags_vi=['tính đơn điệu', 'cực trị', 'đạo hàm', 'bảng xét dấu', 'tham số'],
  meta={'level': ('Intermediate', 'Trung bình'), 'time': ('about 80 minutes', 'khoảng 80 phút'), 'before': ('derivative rules, sign of a quadratic, intervals, second derivative', 'quy tắc đạo hàm, dấu tam thức bậc hai, khoảng, đạo hàm cấp hai')},
  goals=a1[4][:3] + a2[4][:3] + [a1[4][3]], vocab=_dedupe(a1[5] + a2[5], _term), phrases=_dedupe(a1[6] + a2[6]), review=a1[7],
  theory=a1[8] + a2[8], examples=a1[9] + a2[9], practice=_prac1, mistakes=a1[11] + a2[11], summary=a1[12] + a2[12], checks=_dedupe(a1[13] + a2[13]),
  path='lessons/grade12/monotonicity-extrema/monotonicity-of-functions.html',
  description='Use the derivative to find where a function increases or decreases and to find its local extrema.', level='Intermediate', minutes=80,
  prerequisites=[], tags=['monotonicity', 'extrema', 'derivative', 'sign table'], order=10)

_prac2 = _add_self(a3[10], SELF(sp_g12.M2, start=11, avoid=[t[1] for t in a3[10]]), 'D', SELF_T)
lesson(id='g12-mono-03', title_en='Maximum and Minimum Values', title_vi='Giá trị lớn nhất và giá trị nhỏ nhất của hàm số', topic=TOPIC12,
  catalog_title_vi='Giá trị lớn nhất và giá trị nhỏ nhất của hàm số', description_vi='Bài 2 – Tìm giá trị lớn nhất, nhỏ nhất trên một đoạn bằng đạo hàm; bài toán tối ưu trong thực tế.',
  tags_vi=['giá trị lớn nhất', 'giá trị nhỏ nhất', 'đoạn', 'tối ưu'],
  meta=a3[3], goals=a3[4], vocab=a3[5], phrases=a3[6], review=a3[7], theory=a3[8], examples=a3[9], practice=_prac2, mistakes=a3[11], summary=a3[12], checks=a3[13],
  path=a3[14], description=a3[15]['description'], level='Intermediate', minutes=50, prerequisites=['g12-mono-01'], tags=a3[15]['tags'], order=20)
