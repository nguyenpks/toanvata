# -*- coding: utf-8 -*-
"""Nội dung bài g12-deriv-app-01 – CHỈ NỘI DUNG. Bố cục, số mục, tên mục, số lớp do config/model.json quyết định."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
from mb_selfpractice import SELF
import sp_g12

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

CAT = 'Applications of Derivatives'
added = ensure_vocab([
 ('v-asymptote', 'asymptote', 'đường tiệm cận', CAT, 'The graph has an asymptote.', ''),
 ('v-vertical-asymptote', 'vertical asymptote', 'tiệm cận đứng', CAT, 'The line x = 3 is a vertical asymptote.', '\\(x=a\\)'),
 ('v-horizontal-asymptote', 'horizontal asymptote', 'tiệm cận ngang', CAT, 'The line y = 2 is a horizontal asymptote.', '\\(y=b\\)'),
 ('v-oblique-asymptote', 'oblique asymptote', 'tiệm cận xiên', CAT, 'The line y = x - 1 is an oblique asymptote.', '\\(y=ax+b\\)'),
 ('v-graph', 'graph', 'đồ thị', CAT, 'Sketch the graph of the function.', ''),
 ('v-limit', 'limit', 'giới hạn', CAT, 'Find the limit as x approaches 3.', '\\(\\lim_{x\\to a}f(x)\\)'),
 ('v-rational-function', 'rational function', 'hàm phân thức', CAT, 'A rational function is a quotient of two polynomials.', '\\(\\dfrac{P(x)}{Q(x)}\\)'),
 ('v-numerator', 'numerator', 'tử số', CAT, 'The numerator is P(x).', ''),
 ('v-denominator', 'denominator', 'mẫu số', CAT, 'The denominator is zero at x = 3.', ''),
 ('v-degree', 'degree', 'bậc', CAT, 'The degree of x^2 + 1 is 2.', '\\(\\deg P\\)'),
 ('v-leading-coefficient', 'leading coefficient', 'hệ số cao nhất', CAT, 'The leading coefficient is 4.', ''),
 ('v-polynomial-division', 'polynomial division', 'phép chia đa thức', CAT, 'Use polynomial division.', ''),
 ('v-quotient', 'quotient', 'thương', CAT, 'The quotient is x - 1.', ''),
 ('v-remainder', 'remainder', 'số dư', CAT, 'The remainder is -1.', ''),
 ('v-removable-discontinuity', 'hole', 'điểm hổng', CAT, 'The graph has a hole at x = 1.', ''),
])
load_vocab()

LID = 'g12-deriv-app-01'

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 40 minutes', 'khoảng 40 phút'),
            before=('limits at infinity, one-sided limits, polynomial division', 'giới hạn tại vô cực, giới hạn một phía, chia đa thức'))
goals = [('define horizontal, vertical and oblique asymptotes using limits;', 'định nghĩa [[tiệm cận ngang]], [[tiệm cận đứng]] và [[tiệm cận xiên]] bằng [[giới hạn]];'),
    ('find all asymptotes of a rational function;', 'tìm tất cả các đường tiệm cận của một [[hàm phân thức]];'),
    ('explain why a common factor gives a hole and not a vertical asymptote;', 'giải thích vì sao nhân tử chung chỉ tạo ra [[điểm hổng]] chứ không tạo ra tiệm cận đứng;'),
    ('read the asymptotes of a graph and state them in English.', 'đọc các đường tiệm cận trên [[đồ thị]] và phát biểu chúng bằng tiếng Anh.')]

vocab = [
 ('<b>asymptote</b> – a line that the graph gets closer and closer to, but need not touch.', '[[Đường tiệm cận]] – đường thẳng mà [[đồ thị]] tiến gần tới vô hạn.'),
 ('<b>vertical asymptote</b> – a vertical line \\(x=a\\) near which the function becomes very large.', '[[Tiệm cận đứng]] – đường thẳng đứng \\(x=a\\) mà khi \\(x\\) tiến gần \\(a\\) thì giá trị hàm số trở nên rất lớn.'),
 ('<b>horizontal asymptote</b> – a horizontal line \\(y=b\\) that the graph approaches as \\(x\\) goes to infinity.', '[[Tiệm cận ngang]] – đường nằm ngang \\(y=b\\) mà đồ thị tiến gần khi \\(x\\) ra xa vô cực.'),
 ('<b>oblique asymptote</b> (also slant asymptote) – a slanted line \\(y=ax+b\\) with \\(a\\ne 0\\).', '[[Tiệm cận xiên]] – đường thẳng nghiêng \\(y=ax+b\\) với \\(a\\ne 0\\).'),
 ('<b>rational function</b> – a quotient of two polynomials, \\(\\dfrac{P(x)}{Q(x)}\\).', '[[Hàm phân thức]] – thương của hai đa thức, \\(\\dfrac{P(x)}{Q(x)}\\).'),
 ('<b>numerator</b> and <b>denominator</b> – the top and the bottom of a fraction.', '[[Tử số]] và [[mẫu số]] – phần trên và phần dưới của phân số.'),
 ('<b>degree</b> – the highest power of \\(x\\) in a polynomial.', '[[Bậc]] – số mũ cao nhất của \\(x\\) trong đa thức.'),
 ('<b>quotient</b> and <b>remainder</b> – the results of polynomial division.', '[[Thương]] và [[số dư]] – kết quả của [[phép chia đa thức]].'),
 ('<b>hole</b> – a single missing point on a graph (a removable discontinuity).', '[[Điểm hổng]] – một điểm bị thiếu trên [[đồ thị]] (gián đoạn có thể khử được).'),
]

phrases = [
 ('Find all asymptotes of the graph of \\(f\\).', 'Tìm tất cả các đường tiệm cận của đồ thị hàm số \\(f\\).'),
 ('The graph approaches the line \\(y=2\\) as \\(x\\) tends to infinity.', 'Đồ thị tiến gần đường thẳng \\(y=2\\) khi \\(x\\) tiến ra vô cực.'),
 ('Find the limit as \\(x\\) approaches 3 from the right.', 'Tìm giới hạn khi \\(x\\) tiến đến 3 từ bên phải.'),
 ('Does the graph have a vertical asymptote? Justify your answer.', 'Đồ thị có tiệm cận đứng không? Hãy giải thích.'),
 ('Divide the numerator by the denominator.', 'Chia tử số cho mẫu số.'),
]

review = ''
review += T('Two facts about limits are used all the time in this lesson. For every positive integer \\(n\\):',
        'Hai kết quả về [[giới hạn]] được dùng liên tục trong bài này. Với mọi số nguyên dương \\(n\\):')
review += M(r'\lim_{x\to+\infty}\frac{1}{x^{n}}=0,\qquad \lim_{x\to-\infty}\frac{1}{x^{n}}=0')
review += T('If the numerator tends to a number \\(k\\ne 0\\) and the denominator tends to \\(0\\), the fraction becomes very large. Its sign depends on the sign of \\(k\\) and on the side from which \\(x\\) approaches \\(a\\). For example:',
        'Nếu [[tử số]] tiến đến số \\(k\\ne 0\\) còn [[mẫu số]] tiến đến \\(0\\) thì phân số trở nên rất lớn. Dấu của nó phụ thuộc dấu của \\(k\\) và phía mà \\(x\\) tiến đến \\(a\\). Ví dụ:')
review += M(r'\lim_{x\to a^{+}}\frac{1}{x-a}=+\infty,\qquad \lim_{x\to a^{-}}\frac{1}{x-a}=-\infty')
theory = ''
theory += '<h3>5.1 %s</h3>' % TI('Horizontal asymptote', 'Tiệm cận ngang')
theory += BOX('mint', ('Definition', 'Định nghĩa'),
    T('The line \\(y=b\\) is a <b>horizontal asymptote</b> of the graph of \\(y=f(x)\\) if at least one of these holds:',
      'Đường thẳng \\(y=b\\) là [[tiệm cận ngang]] của [[đồ thị]] hàm số \\(y=f(x)\\) nếu có ít nhất một trong hai điều kiện:'),
    UL(['\\(\\displaystyle\\lim_{x\\to+\\infty}f(x)=b\\)', '\\(\\displaystyle\\lim_{x\\to-\\infty}f(x)=b\\)']))
theory += '<h3>5.2 %s</h3>' % TI('Vertical asymptote', 'Tiệm cận đứng')
theory += BOX('mint', ('Definition', 'Định nghĩa'),
    T('The line \\(x=a\\) is a <b>vertical asymptote</b> of the graph of \\(y=f(x)\\) if at least one of these holds:',
      'Đường thẳng \\(x=a\\) là [[tiệm cận đứng]] của [[đồ thị]] hàm số \\(y=f(x)\\) nếu có ít nhất một trong bốn điều kiện:'),
    UL(['\\(\\displaystyle\\lim_{x\\to a^{+}}f(x)=+\\infty\\)', '\\(\\displaystyle\\lim_{x\\to a^{+}}f(x)=-\\infty\\)',
        '\\(\\displaystyle\\lim_{x\\to a^{-}}f(x)=+\\infty\\)', '\\(\\displaystyle\\lim_{x\\to a^{-}}f(x)=-\\infty\\)']))
f1 = lambda x: (2 * x + 1) / (x - 3)
theory += FIG(svg_graph(f1, (-4, 10), (-6, 12), vlines=[3], hlines=[2]),
          'The graph of \\(y=\\dfrac{2x+1}{x-3}\\) with its asymptotes \\(x=3\\) and \\(y=2\\).', 'Đồ thị của \\(y=\\dfrac{2x+1}{x-3}\\) cùng hai đường tiệm cận \\(x=3\\) và \\(y=2\\).',
          'Graph of y = (2x+1)/(x-3) with vertical asymptote x = 3 and horizontal asymptote y = 2', '')
theory += '<h3>5.3 %s</h3>' % TI('Oblique asymptote', 'Tiệm cận xiên')
theory += BOX('mint', ('Definition', 'Định nghĩa'),
    T('The line \\(y=ax+b\\) with \\(a\\ne 0\\) is an <b>oblique asymptote</b> of the graph of \\(y=f(x)\\) if at least one of these holds:',
      'Đường thẳng \\(y=ax+b\\) với \\(a\\ne 0\\) là [[tiệm cận xiên]] của [[đồ thị]] hàm số \\(y=f(x)\\) nếu có ít nhất một trong hai điều kiện:'),
    UL(['\\(\\displaystyle\\lim_{x\\to+\\infty}\\big[f(x)-(ax+b)\\big]=0\\)', '\\(\\displaystyle\\lim_{x\\to-\\infty}\\big[f(x)-(ax+b)\\big]=0\\)']))
theory += T('To find \\(a\\) and \\(b\\) (for example when \\(x\\to+\\infty\\)):', 'Để tìm \\(a\\) và \\(b\\) (chẳng hạn khi \\(x\\to+\\infty\\)):')
theory += M(r'a=\lim_{x\to+\infty}\frac{f(x)}{x},\qquad b=\lim_{x\to+\infty}\big[f(x)-ax\big]')
theory += '<h3>5.4 %s</h3>' % TI('Rational functions: a quick method', 'Hàm phân thức: cách làm nhanh')
theory += T('Let \\(f(x)=\\dfrac{P(x)}{Q(x)}\\), where the fraction is already in lowest terms.',
        'Cho \\(f(x)=\\dfrac{P(x)}{Q(x)}\\), trong đó phân thức đã được rút gọn.')
theory += UL([
    T('<b>Vertical:</b> if \\(Q(a)=0\\) and \\(P(a)\\ne 0\\), then \\(x=a\\) is a vertical asymptote.', '<b>Đứng:</b> nếu \\(Q(a)=0\\) và \\(P(a)\\ne 0\\) thì \\(x=a\\) là tiệm cận đứng.'),
    T('<b>Horizontal:</b> if \\(\\deg P<\\deg Q\\), the line \\(y=0\\) is a horizontal asymptote.', '<b>Ngang:</b> nếu \\(\\deg P<\\deg Q\\) thì \\(y=0\\) là tiệm cận ngang.'),
    T('<b>Horizontal:</b> if \\(\\deg P=\\deg Q\\), the line \\(y=\\dfrac{\\text{leading coefficient of }P}{\\text{leading coefficient of }Q}\\) is a horizontal asymptote.', '<b>Ngang:</b> nếu \\(\\deg P=\\deg Q\\) thì đường \\(y=\\dfrac{\\text{hệ số cao nhất của }P}{\\text{hệ số cao nhất của }Q}\\) là tiệm cận ngang.'),
    T('<b>Oblique:</b> if \\(\\deg P=\\deg Q+1\\), divide \\(P\\) by \\(Q\\). If \\(P=Q\\cdot(ax+b)+R\\) with \\(\\deg R<\\deg Q\\), then \\(y=ax+b\\) is an oblique asymptote.', '<b>Xiên:</b> nếu \\(\\deg P=\\deg Q+1\\), hãy chia \\(P\\) cho \\(Q\\). Nếu \\(P=Q\\cdot(ax+b)+R\\) với \\(\\deg R<\\deg Q\\) thì \\(y=ax+b\\) là tiệm cận xiên.'),
    T('If \\(\\deg P>\\deg Q+1\\), the graph has neither a horizontal nor an oblique asymptote.', 'Nếu \\(\\deg P>\\deg Q+1\\) thì đồ thị không có tiệm cận ngang và không có tiệm cận xiên.'),
])
f3 = lambda x: (x * x - 3 * x + 1) / (x - 2)
theory += FIG(svg_graph(f3, (-3, 7), (-6, 7), vlines=[2], lines=[(1, -1, 'y = x - 1')]),
          'The graph of \\(y=\\dfrac{x^2-3x+1}{x-2}\\) with \\(x=2\\) and the oblique asymptote \\(y=x-1\\).', 'Đồ thị của \\(y=\\dfrac{x^2-3x+1}{x-2}\\) với \\(x=2\\) và tiệm cận xiên \\(y=x-1\\).',
          'Graph of y = (x^2-3x+1)/(x-2) with vertical asymptote x = 2 and oblique asymptote y = x - 1', '')
theory += GRAPH({'view': [-3.5, 9, -6, 9], 'functions': [{'f': '(2x+1)/(x-3)', 'label': 'y = (2x+1)/(x−3)'}], 'asymptotes': [{'type': 'v', 'x': 3}, {'type': 'h', 'y': 2}]},
  cap=('Graph of y = (2x+1)/(x−3): the dashed lines x = 3 and y = 2 are the asymptotes; the curve gets closer and closer to them.', 'Đồ thị y = (2x+1)/(x−3): hai đường nét đứt x = 3 và y = 2 là các tiệm cận; đường cong tiến sát dần tới chúng.'),
  alt=('Graph of a rational function with a vertical and a horizontal asymptote', ''), height=340)
theory += GRAPH({'view': [-3, 8, -7, 8], 'functions': [{'f': '(x^2-3x+1)/(x-2)', 'label': 'y = (x²−3x+1)/(x−2)'}], 'asymptotes': [{'type': 'v', 'x': 2}, {'type': 'oblique', 'm': 1, 'b': -1}]},
  cap=('Interactive graph with the vertical asymptote x = 2 and the oblique asymptote y = x − 1.', 'Đồ thị tương tác với tiệm cận đứng x = 2 và tiệm cận xiên y = x − 1.'),
  alt=('Graph of a rational function with an oblique asymptote', ''), height=340)
examples = ''
examples += EXAMPLE(1, ('Basic', 'Cơ bản'), ('One vertical and one horizontal asymptote', 'Một tiệm cận đứng và một tiệm cận ngang'),
    T('Find all asymptotes of the graph of \\(f(x)=\\dfrac{2x+1}{x-3}\\).', 'Tìm tất cả các đường tiệm cận của đồ thị hàm số \\(f(x)=\\dfrac{2x+1}{x-3}\\).'),
    ('The denominator is zero at \\(x=3\\). The degrees of numerator and denominator are equal.', '[[Mẫu số]] bằng 0 tại \\(x=3\\). [[Tử số]] và mẫu số có cùng [[bậc]].'),
    [T('Domain: \\(x\\ne 3\\). At \\(x=3\\) the numerator is \\(7\\ne 0\\).', 'Tập xác định: \\(x\\ne 3\\). Tại \\(x=3\\), tử số bằng \\(7\\ne 0\\).'),
     T('\\(\\displaystyle\\lim_{x\\to3^{+}}\\frac{2x+1}{x-3}=+\\infty\\) and \\(\\displaystyle\\lim_{x\\to3^{-}}\\frac{2x+1}{x-3}=-\\infty\\). So \\(x=3\\) is a vertical asymptote.', '\\(\\displaystyle\\lim_{x\\to3^{+}}\\frac{2x+1}{x-3}=+\\infty\\) và \\(\\displaystyle\\lim_{x\\to3^{-}}\\frac{2x+1}{x-3}=-\\infty\\). Vậy \\(x=3\\) là [[tiệm cận đứng]].'),
     T('\\(\\displaystyle\\lim_{x\\to\\pm\\infty}\\frac{2x+1}{x-3}=\\lim_{x\\to\\pm\\infty}\\frac{2+\\frac1x}{1-\\frac3x}=2\\). So \\(y=2\\) is a horizontal asymptote.', '\\(\\displaystyle\\lim_{x\\to\\pm\\infty}\\frac{2x+1}{x-3}=\\lim_{x\\to\\pm\\infty}\\frac{2+\\frac1x}{1-\\frac3x}=2\\). Vậy \\(y=2\\) là [[tiệm cận ngang]].')],
    '\\(x=3\\) (vertical), \\(y=2\\) (horizontal)')
examples += EXAMPLE(2, ('Intermediate', 'Trung bình'), ('A common factor', 'Có nhân tử chung'),
    T('Find all asymptotes of the graph of \\(f(x)=\\dfrac{x^2-1}{x^2-3x+2}\\).', 'Tìm tất cả các đường tiệm cận của đồ thị hàm số \\(f(x)=\\dfrac{x^2-1}{x^2-3x+2}\\).'),
    ('Factor first. A factor that cancels does not give a vertical asymptote.', 'Hãy phân tích thành nhân tử trước. Nhân tử được rút gọn thì không cho tiệm cận đứng.'),
    [T('Factor: \\(f(x)=\\dfrac{(x-1)(x+1)}{(x-1)(x-2)}=\\dfrac{x+1}{x-2}\\) for \\(x\\ne1,\\ x\\ne2\\).', 'Phân tích: \\(f(x)=\\dfrac{(x-1)(x+1)}{(x-1)(x-2)}=\\dfrac{x+1}{x-2}\\) với \\(x\\ne1,\\ x\\ne2\\).'),
     T('At \\(x=2\\): \\(\\displaystyle\\lim_{x\\to2^{+}}\\frac{x+1}{x-2}=+\\infty\\). So \\(x=2\\) is a vertical asymptote.', 'Tại \\(x=2\\): \\(\\displaystyle\\lim_{x\\to2^{+}}\\frac{x+1}{x-2}=+\\infty\\). Vậy \\(x=2\\) là tiệm cận đứng.'),
     T('At \\(x=1\\): \\(\\displaystyle\\lim_{x\\to1}\\frac{x+1}{x-2}=-2\\), a finite number. So \\(x=1\\) is not an asymptote; the graph has a hole at \\((1,-2)\\).', 'Tại \\(x=1\\): \\(\\displaystyle\\lim_{x\\to1}\\frac{x+1}{x-2}=-2\\) là một số hữu hạn. Vậy \\(x=1\\) không phải tiệm cận; [[đồ thị]] có [[điểm hổng]] tại \\((1,-2)\\).'),
     T('\\(\\displaystyle\\lim_{x\\to\\pm\\infty}\\frac{x+1}{x-2}=1\\). So \\(y=1\\) is a horizontal asymptote.', '\\(\\displaystyle\\lim_{x\\to\\pm\\infty}\\frac{x+1}{x-2}=1\\). Vậy \\(y=1\\) là tiệm cận ngang.')],
    '\\(x=2\\) (vertical), \\(y=1\\) (horizontal)')
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('An oblique asymptote', 'Tiệm cận xiên'),
    T('Find all asymptotes of the graph of \\(f(x)=\\dfrac{x^2-3x+1}{x-2}\\).', 'Tìm tất cả các đường tiệm cận của đồ thị hàm số \\(f(x)=\\dfrac{x^2-3x+1}{x-2}\\).'),
    ('The degree of the numerator is one more than the degree of the denominator, so use polynomial division.', '[[Bậc]] của tử số lớn hơn bậc của mẫu số đúng một đơn vị, nên dùng [[phép chia đa thức]].'),
    [T('Divide: \\(x^2-3x+1=(x-2)(x-1)-1\\). The quotient is \\(x-1\\) and the remainder is \\(-1\\).', 'Chia: \\(x^2-3x+1=(x-2)(x-1)-1\\). [[Thương]] là \\(x-1\\), [[số dư]] là \\(-1\\).'),
     T('So \\(f(x)=x-1-\\dfrac{1}{x-2}\\).', 'Do đó \\(f(x)=x-1-\\dfrac{1}{x-2}\\).'),
     T('\\(f(x)-(x-1)=-\\dfrac1{x-2}\\to0\\) as \\(x\\to\\pm\\infty\\). So \\(y=x-1\\) is an oblique asymptote.', '\\(f(x)-(x-1)=-\\dfrac1{x-2}\\to0\\) khi \\(x\\to\\pm\\infty\\). Vậy \\(y=x-1\\) là tiệm cận xiên.'),
     T('At \\(x=2\\) the numerator is \\(-1\\ne0\\), so \\(x=2\\) is a vertical asymptote. There is no horizontal asymptote because \\(f(x)\\to\\pm\\infty\\) as \\(x\\to\\pm\\infty\\).', 'Tại \\(x=2\\) tử số bằng \\(-1\\ne0\\), nên \\(x=2\\) là tiệm cận đứng. Không có tiệm cận ngang vì \\(f(x)\\to\\pm\\infty\\) khi \\(x\\to\\pm\\infty\\).')],
    '\\(x=2\\) (vertical), \\(y=x-1\\) (oblique)')
examples += EXAMPLE(4, ('Advanced', 'Nâng cao'), ('Counting asymptotes', 'Đếm số đường tiệm cận'),
    T('How many asymptotes does the graph of \\(f(x)=\\dfrac{3x-1}{x^2-4}\\) have? Name them.', 'Đồ thị hàm số \\(f(x)=\\dfrac{3x-1}{x^2-4}\\) có bao nhiêu đường tiệm cận? Hãy nêu tên chúng.'),
    ('Look at the zeros of the denominator, then compare the degrees.', 'Xét các nghiệm của mẫu số, rồi so sánh bậc.'),
    [T('\\(x^2-4=0\\) gives \\(x=2\\) and \\(x=-2\\).', '\\(x^2-4=0\\) cho \\(x=2\\) và \\(x=-2\\).'),
     T('The numerator \\(3x-1\\) equals \\(5\\) at \\(x=2\\) and \\(-7\\) at \\(x=-2\\); both are non-zero. So \\(x=2\\) and \\(x=-2\\) are vertical asymptotes.', 'Tử số \\(3x-1\\) bằng \\(5\\) tại \\(x=2\\) và bằng \\(-7\\) tại \\(x=-2\\); cả hai đều khác 0. Vậy \\(x=2\\) và \\(x=-2\\) là các tiệm cận đứng.'),
     T('\\(\\deg(3x-1)=1<2=\\deg(x^2-4)\\), so \\(y=0\\) is a horizontal asymptote.', '\\(\\deg(3x-1)=1<2=\\deg(x^2-4)\\), nên \\(y=0\\) là tiệm cận ngang.')],
    '3 asymptotes: \\(x=2\\), \\(x=-2\\), \\(y=0\\)')
mc = [
 MCQ(1, ('Which line is a vertical asymptote of \\(y=\\dfrac{x+2}{x-5}\\)?', 'Đường thẳng nào là tiệm cận đứng của đồ thị \\(y=\\dfrac{x+2}{x-5}\\)?'),
     ['x=-2', 'x=5', 'y=1', 'y=5'], 'b',
     ('Answer: b. The denominator is zero at \\(x=5\\) and the numerator is \\(7\\ne0\\). The line \\(y=1\\) is the horizontal asymptote.', 'Đáp án b. Mẫu số bằng 0 tại \\(x=5\\) còn tử số bằng \\(7\\ne0\\). Đường \\(y=1\\) là tiệm cận ngang.')),
 MCQ(2, ('What is the horizontal asymptote of \\(y=\\dfrac{4x^2+1}{2x^2-x}\\)?', 'Tiệm cận ngang của đồ thị \\(y=\\dfrac{4x^2+1}{2x^2-x}\\) là đường nào?'),
     ['y=4', 'y=2', r'y=\frac12', 'y=0'], 'b',
     ('Answer: b. The degrees are equal, so \\(b=\\dfrac{4}{2}=2\\).', 'Đáp án b. Hai bậc bằng nhau nên \\(b=\\dfrac{4}{2}=2\\).')),
 MCQ(3, ('What is the oblique asymptote of \\(y=\\dfrac{x^2+x+1}{x+1}\\)?', 'Tiệm cận xiên của đồ thị \\(y=\\dfrac{x^2+x+1}{x+1}\\) là đường nào?'),
     ['y=x+1', 'y=x', 'y=x-1', 'y=2x'], 'b',
     ('Answer: b. \\(x^2+x+1=(x+1)\\cdot x+1\\), so \\(f(x)=x+\\dfrac1{x+1}\\) and the quotient is \\(x\\).', 'Đáp án b. \\(x^2+x+1=(x+1)\\cdot x+1\\) nên \\(f(x)=x+\\dfrac1{x+1}\\); [[thương]] là \\(x\\).')),
 MCQ(4, ('Which function has the horizontal asymptote \\(y=0\\)?', 'Hàm số nào có tiệm cận ngang \\(y=0\\)?'),
     [r'\frac{x}{x+1}', r'\frac{x+1}{x^2}', r'\frac{x^2}{x+1}', 'x^2+1'], 'b',
     ('Answer: b. Only in \\(\\dfrac{x+1}{x^2}\\) is the degree of the numerator smaller than the degree of the denominator.', 'Đáp án b. Chỉ ở \\(\\dfrac{x+1}{x^2}\\) bậc của tử số nhỏ hơn bậc của mẫu số.')),
]
tf = [
 TF(5, ('True or false: the graph of \\(f(x)=\\dfrac{x^2-4}{x-2}\\) has the vertical asymptote \\(x=2\\).', 'Đúng hay sai: đồ thị hàm số \\(f(x)=\\dfrac{x^2-4}{x-2}\\) có tiệm cận đứng \\(x=2\\).'), 'false',
    ('False. For \\(x\\ne2\\), \\(f(x)=x+2\\), so \\(f(x)\\to4\\) as \\(x\\to2\\). The graph has a hole at \\((2,4)\\), not an asymptote.', 'Sai. Với \\(x\\ne2\\), \\(f(x)=x+2\\) nên \\(f(x)\\to4\\) khi \\(x\\to2\\). [[Đồ thị]] có [[điểm hổng]] tại \\((2,4)\\) chứ không có tiệm cận.')),
 TF(6, ('True or false: the graph of a function can cross its horizontal asymptote.', 'Đúng hay sai: đồ thị hàm số có thể cắt tiệm cận ngang của nó.'), 'true',
    ('True. For \\(f(x)=\\dfrac{2x}{x^2+1}\\), the line \\(y=0\\) is a horizontal asymptote, and the graph passes through the origin.', 'Đúng. Với \\(f(x)=\\dfrac{2x}{x^2+1}\\), đường \\(y=0\\) là tiệm cận ngang và đồ thị đi qua gốc tọa độ.')),
]
sh = [
 SHORT(7, ('How many vertical asymptotes does the graph of \\(y=\\dfrac{x}{x^2-9}\\) have?', 'Đồ thị hàm số \\(y=\\dfrac{x}{x^2-9}\\) có bao nhiêu tiệm cận đứng?'), '2', 'number',
       ('Enter a whole number.', 'Nhập một số nguyên.'),
       ('Answer: 2. The denominator is zero at \\(x=3\\) and \\(x=-3\\), and the numerator is non-zero at both.', 'Đáp án: 2. Mẫu số bằng 0 tại \\(x=3\\) và \\(x=-3\\), còn tử số khác 0 tại cả hai điểm.')),
 SHORT(8, ('The graph of \\(y=\\dfrac{3-x}{2x+7}\\) has a horizontal asymptote \\(y=b\\). Find \\(b\\).', 'Đồ thị \\(y=\\dfrac{3-x}{2x+7}\\) có tiệm cận ngang \\(y=b\\). Tìm \\(b\\).'), '-1/2', 'number',
       ('Enter a number or a fraction, for example -1/2.', 'Nhập một số hoặc phân số, ví dụ -1/2.'),
       ('Answer: \\(-\\dfrac12\\). The leading coefficients are \\(-1\\) and \\(2\\), so \\(b=\\dfrac{-1}{2}\\).', 'Đáp án: \\(-\\dfrac12\\). Hệ số cao nhất là \\(-1\\) và \\(2\\) nên \\(b=\\dfrac{-1}{2}\\).')),
 SHORT(9, ('How many asymptotes (of all types) does the graph of \\(y=\\dfrac{2x^2-x}{x-1}\\) have?', 'Đồ thị hàm số \\(y=\\dfrac{2x^2-x}{x-1}\\) có tất cả bao nhiêu đường tiệm cận (mọi loại)?'), '2', 'number',
       ('Enter a whole number.', 'Nhập một số nguyên.'),
       ('Answer: 2. \\(2x^2-x=(x-1)(2x+1)+1\\), so the asymptotes are \\(x=1\\) (vertical) and \\(y=2x+1\\) (oblique). There is no horizontal asymptote.', 'Đáp án: 2. \\(2x^2-x=(x-1)(2x+1)+1\\) nên các tiệm cận là \\(x=1\\) (đứng) và \\(y=2x+1\\) (xiên). Không có tiệm cận ngang.')),
 SHORT(10, ('The graph of \\(y=\\dfrac{ax+1}{x-2}\\) has the horizontal asymptote \\(y=3\\). Find \\(a\\).', 'Đồ thị \\(y=\\dfrac{ax+1}{x-2}\\) có tiệm cận ngang \\(y=3\\). Tìm \\(a\\).'), '3', 'number',
       ('Enter a number.', 'Nhập một số.'),
       ('Answer: \\(a=3\\). The horizontal asymptote is \\(y=\\dfrac{a}{1}=a\\).', 'Đáp án: \\(a=3\\). Tiệm cận ngang là \\(y=\\dfrac{a}{1}=a\\).')),
]
practice = [(('A. Multiple Choice', 'A. Trắc nghiệm nhiều lựa chọn'), mc), (('B. True or False', 'B. Đúng hoặc sai'), tf), (('C. Short Answer', 'C. Trả lời ngắn'), sh)]
S2 = [
 [_m(1, r'Which line is a vertical asymptote of \(y=\dfrac{x-1}{x+4}\)?§Đường thẳng nào là tiệm cận đứng của đồ thị \(y=\dfrac{x-1}{x+4}\)?', ['x=-4', 'x=4', 'y=1', 'x=1'], 'a',
      r'The denominator is zero at \(x=-4\) and the numerator is \(-5\ne0\). The line \(y=1\) is the horizontal asymptote.§Mẫu số bằng 0 tại \(x=-4\) còn tử số bằng \(-5\ne0\). Đường \(y=1\) là tiệm cận ngang.'),
  _m(2, r'What is the horizontal asymptote of \(y=\dfrac{6x^2+1}{3x^2-x}\)?§Tiệm cận ngang của đồ thị \(y=\dfrac{6x^2+1}{3x^2-x}\) là đường nào?', ['y=6', 'y=3', 'y=2', 'y=0'], 'c',
      r'The degrees are equal, so \(b=\dfrac{6}{3}=2\).§Hai bậc bằng nhau nên \(b=\dfrac{6}{3}=2\).'),
  _m(3, r'What is the oblique asymptote of \(y=\dfrac{x^2+2x+3}{x+1}\)?§Tiệm cận xiên của đồ thị \(y=\dfrac{x^2+2x+3}{x+1}\) là đường nào?', ['y=x', 'y=x+2', 'y=2x', 'y=x+1'], 'd',
      r'\(x^2+2x+3=(x+1)(x+1)+2\), so \(f(x)=x+1+\dfrac{2}{x+1}\) and the quotient is \(x+1\).§\(x^2+2x+3=(x+1)(x+1)+2\) nên \(f(x)=x+1+\dfrac{2}{x+1}\); thương là \(x+1\).'),
  _m(4, r'Which of these functions has \(y=0\) as a horizontal asymptote?§Hàm số nào dưới đây nhận \(y=0\) làm tiệm cận ngang?', [r'\frac{x-1}{x}', r'\frac{x^2}{x-1}', r'\frac{x}{x^2+1}', 'x^2-1'], 'c',
      r'Only in \(\dfrac{x}{x^2+1}\) is the degree of the numerator smaller than the degree of the denominator.§Chỉ ở \(\dfrac{x}{x^2+1}\) bậc của tử số nhỏ hơn bậc của mẫu số.')],
 [_t(5, r'True or false: the graph of \(f(x)=\dfrac{x^2-9}{x-3}\) has the vertical asymptote \(x=3\).§Đúng hay sai: đồ thị hàm số \(f(x)=\dfrac{x^2-9}{x-3}\) có tiệm cận đứng \(x=3\).', 'false',
      r'For \(x\ne3\), \(f(x)=x+3\), so \(f(x)\to6\) as \(x\to3\). The graph has a hole at \((3,6)\), not an asymptote.§Với \(x\ne3\), \(f(x)=x+3\) nên \(f(x)\to6\) khi \(x\to3\). Đồ thị có điểm hổng tại \((3,6)\) chứ không có tiệm cận.'),
  _t(6, r'True or false: the graph of \(f(x)=\dfrac{x-1}{x^2+1}\) has the horizontal asymptote \(y=0\) and meets this line at \(x=1\).§Đúng hay sai: đồ thị hàm số \(f(x)=\dfrac{x-1}{x^2+1}\) có tiệm cận ngang \(y=0\) và cắt đường thẳng này tại \(x=1\).', 'true',
      r'The numerator has smaller degree, so \(y=0\) is a horizontal asymptote, and \(f(1)=0\). A graph can cross its horizontal asymptote.§Tử số có bậc nhỏ hơn nên \(y=0\) là tiệm cận ngang, và \(f(1)=0\). Đồ thị có thể cắt tiệm cận ngang.')],
 [_s(7, r'How many vertical asymptotes does the graph of \(y=\dfrac{x-1}{x^2-4}\) have?§Đồ thị hàm số \(y=\dfrac{x-1}{x^2-4}\) có bao nhiêu tiệm cận đứng?', '2', '2', 'w',
      r'The denominator is zero at \(x=2\) and \(x=-2\), and the numerator is non-zero at both.§Mẫu số bằng 0 tại \(x=2\) và \(x=-2\), còn tử số khác 0 tại cả hai điểm.'),
  _s(8, r'The graph of \(y=\dfrac{7-3x}{2x+1}\) has a horizontal asymptote \(y=b\). Find \(b\).§Đồ thị \(y=\dfrac{7-3x}{2x+1}\) có tiệm cận ngang \(y=b\). Tìm \(b\).', '-3/2', r'\(-\dfrac32\)', 'f',
      r'The leading coefficients are \(-3\) and \(2\), so \(b=\dfrac{-3}{2}\).§Hệ số cao nhất là \(-3\) và \(2\) nên \(b=\dfrac{-3}{2}\).'),
  _s(9, r'How many asymptotes (of all types) does the graph of \(y=\dfrac{x^2+3x}{x+2}\) have?§Đồ thị hàm số \(y=\dfrac{x^2+3x}{x+2}\) có tất cả bao nhiêu đường tiệm cận (mọi loại)?', '2', '2', 'w',
      r'\(x^2+3x=(x+2)(x+1)-2\), so the asymptotes are \(x=-2\) (vertical) and \(y=x+1\) (oblique). There is no horizontal asymptote.§\(x^2+3x=(x+2)(x+1)-2\) nên các tiệm cận là \(x=-2\) (đứng) và \(y=x+1\) (xiên). Không có tiệm cận ngang.'),
  _s(10, r'The graph of \(y=\dfrac{ax+3}{2x-1}\) has the horizontal asymptote \(y=4\). Find \(a\).§Đồ thị \(y=\dfrac{ax+3}{2x-1}\) có tiệm cận ngang \(y=4\). Tìm \(a\).', '8', '8', 'n',
      r'The horizontal asymptote is \(y=\dfrac{a}{2}\), so \(a=8\).§Tiệm cận ngang là \(y=\dfrac{a}{2}\) nên \(a=8\).')]]
S3 = [
 [_m(1, r'Which line is a vertical asymptote of \(y=\dfrac{2x+3}{x-6}\)?§Đường thẳng nào là tiệm cận đứng của đồ thị \(y=\dfrac{2x+3}{x-6}\)?', ['x=2', 'y=2', 'x=6', 'x=-6'], 'c',
      r'The denominator is zero at \(x=6\) and the numerator is \(15\ne0\). The line \(y=2\) is the horizontal asymptote.§Mẫu số bằng 0 tại \(x=6\) còn tử số bằng \(15\ne0\). Đường \(y=2\) là tiệm cận ngang.'),
  _m(2, r'What is the horizontal asymptote of \(y=\dfrac{5x^2+2}{2x^2-x}\)?§Tiệm cận ngang của đồ thị \(y=\dfrac{5x^2+2}{2x^2-x}\) là đường nào?', ['y=5', r'y=\frac52', r'y=\frac25', 'y=2'], 'b',
      r'The degrees are equal, so \(b=\dfrac{5}{2}\).§Hai bậc bằng nhau nên \(b=\dfrac{5}{2}\).'),
  _m(3, r'What is the oblique asymptote of \(y=\dfrac{x^2-3x+5}{x-1}\)?§Tiệm cận xiên của đồ thị \(y=\dfrac{x^2-3x+5}{x-1}\) là đường nào?', ['y=x-2', 'y=x-3', 'y=x-1', 'y=x+2'], 'a',
      r'\(x^2-3x+5=(x-1)(x-2)+3\), so \(f(x)=x-2+\dfrac{3}{x-1}\) and the quotient is \(x-2\).§\(x^2-3x+5=(x-1)(x-2)+3\) nên \(f(x)=x-2+\dfrac{3}{x-1}\); thương là \(x-2\).'),
  _m(4, r'The graph of which function has the line \(y=0\) as a horizontal asymptote?§Đồ thị hàm số nào nhận đường thẳng \(y=0\) làm tiệm cận ngang?', [r'\frac{2x+1}{x-3}', r'\frac{x^2+1}{x}', r'\frac{3}{x^2-1}', 'x^3'], 'c',
      r'Only in \(\dfrac{3}{x^2-1}\) is the degree of the numerator smaller than the degree of the denominator.§Chỉ ở \(\dfrac{3}{x^2-1}\) bậc của tử số nhỏ hơn bậc của mẫu số.')],
 [_t(5, r'True or false: the graph of \(f(x)=\dfrac{x^2-x}{x-1}\) has the vertical asymptote \(x=1\).§Đúng hay sai: đồ thị hàm số \(f(x)=\dfrac{x^2-x}{x-1}\) có tiệm cận đứng \(x=1\).', 'false',
      r'For \(x\ne1\), \(f(x)=\dfrac{x(x-1)}{x-1}=x\), so \(f(x)\to1\) as \(x\to1\). The graph has a hole at \((1,1)\), not an asymptote.§Với \(x\ne1\), \(f(x)=\dfrac{x(x-1)}{x-1}=x\) nên \(f(x)\to1\) khi \(x\to1\). Đồ thị có điểm hổng tại \((1,1)\) chứ không có tiệm cận.'),
  _t(6, r'True or false: the graph of a function can have two different horizontal asymptotes.§Đúng hay sai: đồ thị hàm số có thể có hai tiệm cận ngang khác nhau.', 'true',
      r'For \(y=\arctan x\), the line \(y=\dfrac\pi2\) is an asymptote as \(x\to+\infty\) and \(y=-\dfrac\pi2\) is an asymptote as \(x\to-\infty\).§Với \(y=\arctan x\), đường \(y=\dfrac\pi2\) là tiệm cận khi \(x\to+\infty\) và \(y=-\dfrac\pi2\) là tiệm cận khi \(x\to-\infty\).')],
 [_s(7, r'How many vertical asymptotes does the graph of \(y=\dfrac{x+3}{x^2+9}\) have?§Đồ thị hàm số \(y=\dfrac{x+3}{x^2+9}\) có bao nhiêu tiệm cận đứng?', '0', '0', 'w',
      r'The denominator \(x^2+9\ge9\) is never zero, so there is no vertical asymptote.§Mẫu số \(x^2+9\ge9\) không bao giờ bằng 0 nên không có tiệm cận đứng.'),
  _s(8, r'The graph of \(y=\dfrac{6x+1}{9-2x}\) has a horizontal asymptote \(y=b\). Find \(b\).§Đồ thị \(y=\dfrac{6x+1}{9-2x}\) có tiệm cận ngang \(y=b\). Tìm \(b\).', '-3', r'\(-3\)', 'n',
      r'The leading coefficients are \(6\) and \(-2\), so \(b=\dfrac{6}{-2}=-3\).§Hệ số cao nhất là \(6\) và \(-2\) nên \(b=\dfrac{6}{-2}=-3\).'),
  _s(9, r'How many asymptotes (of all types) does the graph of \(y=\dfrac{2x+1}{x^2-9}\) have?§Đồ thị hàm số \(y=\dfrac{2x+1}{x^2-9}\) có tất cả bao nhiêu đường tiệm cận (mọi loại)?', '3', '3', 'w',
      r'The denominator is zero at \(x=\pm3\) and the numerator is \(7\) and \(-5\), so \(x=3\) and \(x=-3\) are vertical asymptotes. The numerator has the smaller degree, so \(y=0\) is a horizontal asymptote.§Mẫu số bằng 0 tại \(x=\pm3\), tử số lần lượt bằng \(7\) và \(-5\) nên \(x=3\) và \(x=-3\) là tiệm cận đứng. Tử số có bậc nhỏ hơn nên \(y=0\) là tiệm cận ngang.'),
  _s(10, r'The graph of \(y=\dfrac{ax-2}{3x+1}\) has the horizontal asymptote \(y=-2\). Find \(a\).§Đồ thị \(y=\dfrac{ax-2}{3x+1}\) có tiệm cận ngang \(y=-2\). Tìm \(a\).', '-6', r'\(-6\)', 'n',
      r'The horizontal asymptote is \(y=\dfrac{a}{3}\), so \(a=-6\).§Tiệm cận ngang là \(y=\dfrac{a}{3}\) nên \(a=-6\).')]]
_T = [t for t, _ in practice]
S1 = [g for _, g in practice]
practice = LEVEL_PRACTICE(_T, {1: S1, 2: S2, 3: S3})

mistakes = [('<b>Forgetting to simplify.</b> A cancelled factor such as \\(x-1\\) gives a hole, not a vertical asymptote.', '<b>Quên rút gọn.</b> Nhân tử đã được rút gọn như \\(x-1\\) chỉ cho [[điểm hổng]], không cho tiệm cận đứng.'),
        ('<b>Checking only one end.</b> A horizontal asymptote must be checked at \\(+\\infty\\) and at \\(-\\infty\\). The graph of \\(y=\\arctan x\\) has two different ones.', '<b>Chỉ xét một phía.</b> Phải xét [[tiệm cận ngang]] cả khi \\(x\\to+\\infty\\) và \\(x\\to-\\infty\\). Đồ thị \\(y=\\arctan x\\) có hai tiệm cận ngang khác nhau.'),
        ('<b>Mixing up \\(x=a\\) and \\(y=b\\).</b> Vertical asymptotes are lines \\(x=a\\) (zeros of the denominator). Horizontal asymptotes are lines \\(y=b\\) (limits at infinity).', '<b>Nhầm \\(x=a\\) với \\(y=b\\).</b> Tiệm cận đứng có dạng \\(x=a\\) (nghiệm của mẫu số). Tiệm cận ngang có dạng \\(y=b\\) (giới hạn tại vô cực).'),
        ('<b>Looking for an oblique asymptote at the wrong time.</b> For a rational function it exists only when \\(\\deg P=\\deg Q+1\\).', '<b>Tìm tiệm cận xiên sai lúc.</b> Với hàm phân thức, tiệm cận xiên chỉ có khi \\(\\deg P=\\deg Q+1\\).')]
summary = [
    ('Vertical asymptote \\(x=a\\): a one-sided limit at \\(a\\) is \\(\\pm\\infty\\).', 'Tiệm cận đứng \\(x=a\\): giới hạn một phía tại \\(a\\) bằng \\(\\pm\\infty\\).'),
    ('Horizontal asymptote \\(y=b\\): \\(\\displaystyle\\lim_{x\\to\\pm\\infty}f(x)=b\\).', 'Tiệm cận ngang \\(y=b\\): \\(\\displaystyle\\lim_{x\\to\\pm\\infty}f(x)=b\\).'),
    ('Oblique asymptote \\(y=ax+b\\): \\(\\displaystyle\\lim_{x\\to\\pm\\infty}[f(x)-(ax+b)]=0\\); use polynomial division for rational functions.', 'Tiệm cận xiên \\(y=ax+b\\): \\(\\displaystyle\\lim_{x\\to\\pm\\infty}[f(x)-(ax+b)]=0\\); với hàm phân thức, hãy dùng phép chia đa thức.'),
    ('Always simplify the fraction first and compare the degrees of numerator and denominator.', 'Luôn rút gọn phân thức trước và so sánh bậc của tử số với bậc của mẫu số.'),
]
checks = [
    ('I can state the definitions of the three kinds of asymptotes.', 'Em phát biểu được định nghĩa ba loại đường tiệm cận.'),
    ('I can find vertical and horizontal asymptotes of a rational function.', 'Em tìm được tiệm cận đứng và tiệm cận ngang của hàm phân thức.'),
    ('I can find an oblique asymptote by polynomial division.', 'Em tìm được tiệm cận xiên bằng phép chia đa thức.'),
    ('I can tell a hole from a vertical asymptote.', 'Em phân biệt được điểm hổng với tiệm cận đứng.'),
    ('I understand the English instructions in this lesson.', 'Em hiểu các yêu cầu bằng tiếng Anh trong bài này.'),
]

_SP = SELF(sp_g12.M3, start=11, avoid=[t[1] for t in practice])
_L = chr(ord(practice[-1][0][0][0]) + 1)
lesson(id=LID, title_en='Asymptotes of Graphs', title_vi='Đường tiệm cận của đồ thị hàm số', topic=(CAT, 'Ứng dụng đạo hàm'),
       catalog_title_vi='Đường tiệm cận của đồ thị hàm số', description_vi='Bài 3 – Tìm tiệm cận đứng, tiệm cận ngang và tiệm cận xiên bằng giới hạn; phân biệt tiệm cận với điểm hổng.',
       tags_vi=['tiệm cận đứng', 'tiệm cận ngang', 'tiệm cận xiên', 'giới hạn', 'hàm phân thức'],
       folder='derivative-applications', file='asymptotes-of-graphs',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice + [(('%s. Self-practice: Multiple Choice' % _L, '%s. Tự luyện: trắc nghiệm' % _L), _SP[lv], [lv]) for lv in (1, 2, 3)], mistakes=mistakes, summary=summary, checks=checks,
       description='Find vertical, horizontal and oblique asymptotes of graphs of functions.', level='Intermediate', minutes=40,
       prerequisites=[], tags=['asymptote', 'vertical asymptote', 'horizontal asymptote', 'oblique asymptote', 'rational function', 'limits'],
       order=30)
