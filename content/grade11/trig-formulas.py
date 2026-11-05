# -*- coding: utf-8 -*-
"""Nội dung bài g11-trigf-03 = Toán 11 KNTT, Chương I, Bài 2: Công thức lượng giác – CHỈ NỘI DUNG.
Mã ngân hàng câu hỏi: TOAN11-C1-B02. Bài tập: mỗi mức một bộ riêng, cùng dạng, khác số liệu (LEVEL_PRACTICE)."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *

LID = 'g11-trigf-03'
CAT = 'Trigonometric Functions'
TOPIC = (CAT, 'Hàm số lượng giác')
CV = 'Hàm số lượng giác'
PI = math.pi
S3 = math.sqrt(3); S2 = math.sqrt(2); S6 = math.sqrt(6)

ensure_vocab([
 ('g11-addition-formula', 'addition formula', 'công thức cộng', CV, 'Use the addition formula for sine.', ''),
 ('g11-double-angle', 'double-angle formula', 'công thức nhân đôi', CV, 'Use the double-angle formula.', r'\(\sin 2\alpha\)'),
 ('g11-power-reducing', 'power-reducing formula', 'công thức hạ bậc', CV, 'The power-reducing formula removes the square.', ''),
 ('g11-product-to-sum', 'product-to-sum formula', 'công thức biến đổi tích thành tổng', CV, 'Turn the product into a sum.', ''),
 ('g11-sum-to-product', 'sum-to-product formula', 'công thức biến đổi tổng thành tích', CV, 'Turn the sum into a product.', ''),
 ('g11-trig-identity', 'identity', 'đẳng thức', CV, 'Prove the identity.', ''),
 ('g11-simplify-expr', 'simplify', 'rút gọn', CV, 'Simplify the expression.', ''),
])
load_vocab()

# ---- kiểm tra số liệu (mọi công thức, ví dụ và đáp án bài tập) ----
ok = lambda x, y: abs(x - y) < 1e-12
for a in (0.37, 1.1, 2.4):
    for b in (0.2, 0.9, 1.7):
        assert ok(math.cos(a - b), math.cos(a) * math.cos(b) + math.sin(a) * math.sin(b))
        assert ok(math.cos(a + b), math.cos(a) * math.cos(b) - math.sin(a) * math.sin(b))
        assert ok(math.sin(a + b), math.sin(a) * math.cos(b) + math.cos(a) * math.sin(b))
        assert ok(math.sin(a - b), math.sin(a) * math.cos(b) - math.cos(a) * math.sin(b))
        assert ok(math.tan(a + b), (math.tan(a) + math.tan(b)) / (1 - math.tan(a) * math.tan(b)))
        assert ok(math.cos(a) * math.cos(b), (math.cos(a - b) + math.cos(a + b)) / 2)
        assert ok(math.sin(a) * math.sin(b), (math.cos(a - b) - math.cos(a + b)) / 2)
        assert ok(math.sin(a) * math.cos(b), (math.sin(a - b) + math.sin(a + b)) / 2)
        assert ok(math.cos(a) + math.cos(b), 2 * math.cos((a + b) / 2) * math.cos((a - b) / 2))
        assert ok(math.cos(a) - math.cos(b), -2 * math.sin((a + b) / 2) * math.sin((a - b) / 2))
        assert ok(math.sin(a) + math.sin(b), 2 * math.sin((a + b) / 2) * math.cos((a - b) / 2))
        assert ok(math.sin(a) - math.sin(b), 2 * math.cos((a + b) / 2) * math.sin((a - b) / 2))
    assert ok(math.sin(2 * a), 2 * math.sin(a) * math.cos(a)) and ok(math.cos(2 * a), 1 - 2 * math.sin(a) ** 2) and ok(math.cos(2 * a), 2 * math.cos(a) ** 2 - 1)
    assert ok(math.tan(2 * a), 2 * math.tan(a) / (1 - math.tan(a) ** 2))
    assert ok(math.sin(a) ** 2, (1 - math.cos(2 * a)) / 2) and ok(math.cos(a) ** 2, (1 + math.cos(2 * a)) / 2)
    assert ok(math.sin(2 * a) / (1 + math.cos(2 * a)), math.tan(a))
    assert ok((math.sin(a) + math.sin(3 * a)) / (math.cos(a) + math.cos(3 * a)), math.tan(2 * a))
# Ví dụ
d = PI / 180
assert abs(math.sin(75 * d) - (S6 + S2) / 4) < 1e-12                                   # VD1
al = PI - math.asin(0.6)                                                               # VD2: sin=3/5, góc phần tư II
assert PI / 2 < al < PI and ok(math.cos(al), -0.8) and ok(math.sin(2 * al), -24 / 25) and ok(math.cos(2 * al), 7 / 25) and ok(math.tan(2 * al), -24 / 7)
assert ok(math.cos(15 * d) * math.cos(75 * d), 0.25)                                   # VD3
# Bài tập
assert ok(2 * math.sin(15 * d) * math.cos(15 * d), 0.5) and ok(4 * math.sin(15 * d) * math.cos(15 * d), 1) and ok(8 * math.sin(15 * d) * math.cos(15 * d), 2)
assert ok(math.cos(40 * d) * math.cos(20 * d) - math.sin(40 * d) * math.sin(20 * d), 0.5)
assert ok(math.sin(50 * d) * math.cos(10 * d) + math.cos(50 * d) * math.sin(10 * d), S3 / 2)
assert ok(math.sin(80 * d) * math.cos(20 * d) - math.cos(80 * d) * math.sin(20 * d), S3 / 2)
assert ok(2 * (5 / 13) * (12 / 13), 120 / 169) and ok(2 * (3 / 5) * (4 / 5), 24 / 25) and ok(2 * (8 / 17) * (15 / 17), 240 / 289) and ok((225 - 64) / 289, 161 / 289)
assert ok(2 * 0.25 - 1, -0.5) and ok(1 - 2 * 0.25, 0.5) and ok(2 * 0 - 1, -1)
assert ok((1 - 0.2) / 2, 0.4) and ok((1 - 0.5) / 2, 0.25) and ok((1 + 0.2) / 2, 0.6)   # sin^2 theo cos2a: 0,2 -> 0,4; 0,5 -> 0,25; -0,2 -> 0,6

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 60 minutes', 'khoảng 60 phút'),
            before=('trigonometric values of an angle and the basic identities (Lesson 1)', 'giá trị lượng giác của một góc và các hệ thức cơ bản (Bài 1)'))
goals = [
 ('recall and use the addition formulas for sine, cosine and tangent;', 'nhớ và dùng các [[công thức cộng]] cho sin, cos và tan;'),
 ('use the double-angle and power-reducing formulas;', 'dùng [[công thức nhân đôi]] và [[công thức hạ bậc]];'),
 ('turn a product into a sum and a sum into a product;', 'biến đổi tích thành tổng và tổng thành tích;'),
 ('simplify expressions and prove trigonometric identities.', '[[rút gọn]] biểu thức và chứng minh [[đẳng thức]] lượng giác.'),
]
vocab = [
 (r'<b>addition formula</b> – a formula for the trigonometric values of \(a\pm b\).', r'[[Công thức cộng]] – công thức tính giá trị lượng giác của \(a\pm b\).'),
 (r'<b>double-angle formula</b> – a formula for \(\sin 2a\), \(\cos 2a\), \(\tan 2a\).', r'[[Công thức nhân đôi]] – công thức tính \(\sin 2a\), \(\cos 2a\), \(\tan 2a\).'),
 (r'<b>power-reducing formula</b> – writes \(\sin^2 a\) or \(\cos^2 a\) with the angle \(2a\).', r'[[Công thức hạ bậc]] – viết \(\sin^2 a\), \(\cos^2 a\) theo góc \(2a\).'),
 ('<b>product-to-sum formula</b> – turns a product of two ratios into a sum.', '[[Công thức biến đổi tích thành tổng]] – đổi tích của hai giá trị lượng giác thành tổng.'),
 ('<b>sum-to-product formula</b> – turns a sum of two ratios into a product.', '[[Công thức biến đổi tổng thành tích]] – đổi tổng của hai giá trị lượng giác thành tích.'),
 ('<b>identity</b> – an equation that is true for every value where both sides are defined.', '[[Đẳng thức]] – đẳng thức đúng với mọi giá trị mà hai vế đều xác định.'),
 ('<b>simplify</b> – write an expression in a shorter form.', '[[Rút gọn]] – viết biểu thức dưới dạng gọn hơn.'),
]
phrases = [
 ('<b>Simplify the expression.</b>', 'Rút gọn biểu thức.'),
 ('<b>Prove the identity.</b>', 'Chứng minh đẳng thức.'),
 (r'<b>Find the exact value of \(\sin 75^\circ\).</b>', r'Tìm giá trị chính xác của \(\sin 75^\circ\).'),
 (r'<b>Express the product as a sum.</b>', r'Biến đổi tích thành tổng.'),
 ('<b>Use the double-angle formula.</b>', 'Dùng công thức nhân đôi.'),
 ('<b>Write the answer as a fraction.</b>', 'Viết đáp số dưới dạng phân số.'),
]
review = (
 T(r'<b>Basic identity.</b> \(\sin^2\alpha+\cos^2\alpha=1\) and \(\tan\alpha=\dfrac{\sin\alpha}{\cos\alpha}\).', r'<b>Hệ thức cơ bản.</b> \(\sin^2\alpha+\cos^2\alpha=1\) và \(\tan\alpha=\dfrac{\sin\alpha}{\cos\alpha}\).') +
 T(r'<b>Special values.</b> \(\sin 30^\circ=\dfrac12\), \(\cos 30^\circ=\dfrac{\sqrt3}{2}\), \(\sin 45^\circ=\cos 45^\circ=\dfrac{\sqrt2}{2}\), \(\cos 60^\circ=\dfrac12\).', r'<b>Giá trị đặc biệt.</b> \(\sin 30^\circ=\dfrac12\), \(\cos 30^\circ=\dfrac{\sqrt3}{2}\), \(\sin 45^\circ=\cos 45^\circ=\dfrac{\sqrt2}{2}\), \(\cos 60^\circ=\dfrac12\).') +
 T(r'<b>Related angles.</b> \(\cos(-\alpha)=\cos\alpha\), \(\sin(-\alpha)=-\sin\alpha\).', r'<b>Góc liên quan.</b> \(\cos(-\alpha)=\cos\alpha\), \(\sin(-\alpha)=-\sin\alpha\).'))

theory = '<h3>5.1 %s</h3>' % TI('Addition formulas', 'Công thức cộng')
theory += BOX('blue', ('Addition formulas', 'Công thức cộng'),
  M(r'\cos(a-b)=\cos a\cos b+\sin a\sin b,\qquad \cos(a+b)=\cos a\cos b-\sin a\sin b'),
  M(r'\sin(a+b)=\sin a\cos b+\cos a\sin b,\qquad \sin(a-b)=\sin a\cos b-\cos a\sin b'),
  M(r'\tan(a+b)=\dfrac{\tan a+\tan b}{1-\tan a\tan b},\qquad \tan(a-b)=\dfrac{\tan a-\tan b}{1+\tan a\tan b}'),
  T(r'The tangent formulas hold when all the tangents and the denominators are defined.', r'Các công thức của tan đúng khi các giá trị tan và mẫu số đều xác định.'))
theory += GEO({'view': [-1.6, 1.6, -1.4, 1.4], 'axes': True, 'equal': True, 'steps': [
    {'type': 'point', 'id': 'O', 'at': [0, 0], 'fixed': True}, {'type': 'point', 'id': 'I', 'at': [1, 0], 'fixed': True, 'off': [6, -16]},
    {'type': 'circle', 'id': 'c', 'center': 'O', 'through': 'I'},
    {'type': 'glider', 'id': 'A', 'at': [math.cos(PI / 3), math.sin(PI / 3)], 'on': 'c'},
    {'type': 'glider', 'id': 'B', 'at': [math.cos(PI / 12), math.sin(PI / 12)], 'on': 'c'},
    {'type': 'segment', 'through': ['O', 'A']}, {'type': 'segment', 'through': ['O', 'B']},
    {'type': 'segment', 'through': ['A', 'B'], 'style': {'strokeColor': '#c2410c', 'strokeWidth': 3, 'dash': 0}},
    {'type': 'angle', 'points': ['B', 'O', 'A'], 'radius': 0.35}]},
  cap=('Idea of the proof: A(cos a; sin a) and B(cos b; sin b) lie on the circle. Computing AB² in two ways gives cos(a − b).', 'Ý tưởng chứng minh: A(cos a; sin a) và B(cos b; sin b) nằm trên đường tròn. Tính AB² bằng hai cách sẽ ra cos(a − b).'),
  alt=('Two points A and B on the trigonometric circle with the chord AB', ''), height=360)
theory += T(r'<b>Why it works.</b> \(AB^2=(\cos a-\cos b)^2+(\sin a-\sin b)^2=2-2(\cos a\cos b+\sin a\sin b)\). Also \(AB^2=2-2\cos(a-b)\) from the angle \(AOB\). Comparing the two gives the formula for \(\cos(a-b)\); the others follow by replacing \(b\) with \(-b\) and using \(\sin x=\cos\left(\dfrac{\pi}{2}-x\right)\).',
            r'<b>Vì sao đúng.</b> \(AB^2=(\cos a-\cos b)^2+(\sin a-\sin b)^2=2-2(\cos a\cos b+\sin a\sin b)\). Mặt khác \(AB^2=2-2\cos(a-b)\) theo góc \(AOB\). So sánh hai kết quả được công thức của \(\cos(a-b)\); các công thức còn lại suy ra bằng cách thay \(b\) bởi \(-b\) và dùng \(\sin x=\cos\left(\dfrac{\pi}{2}-x\right)\).')

theory += '<h3>5.2 %s</h3>' % TI('Double-angle and power-reducing formulas', 'Công thức nhân đôi và hạ bậc')
theory += BOX('blue', ('Double-angle formulas', 'Công thức nhân đôi'),
  T(r'Put \(b=a\) in the addition formulas:', r'Cho \(b=a\) trong các công thức cộng:'),
  M(r'\sin 2a=2\sin a\cos a,\qquad \tan 2a=\dfrac{2\tan a}{1-\tan^2 a}'),
  M(r'\cos 2a=\cos^2 a-\sin^2 a=2\cos^2 a-1=1-2\sin^2 a'))
theory += BOX('mint', ('Power-reducing formulas', 'Công thức hạ bậc'),
  T(r'Solve the last two forms of \(\cos 2a\) for the squares:', r'Giải hai dạng cuối của \(\cos 2a\) để rút ra các bình phương:'),
  M(r'\sin^2 a=\dfrac{1-\cos 2a}{2},\qquad \cos^2 a=\dfrac{1+\cos 2a}{2}'))

theory += '<h3>5.3 %s</h3>' % TI('Product-to-sum and sum-to-product formulas', 'Công thức biến đổi tích thành tổng và tổng thành tích')
theory += BOX('blue', ('Product to sum', 'Tích thành tổng'),
  M(r'\cos a\cos b=\dfrac12\left[\cos(a-b)+\cos(a+b)\right]'),
  M(r'\sin a\sin b=\dfrac12\left[\cos(a-b)-\cos(a+b)\right]'),
  M(r'\sin a\cos b=\dfrac12\left[\sin(a-b)+\sin(a+b)\right]'))
theory += BOX('blue', ('Sum to product', 'Tổng thành tích'),
  M(r'\cos u+\cos v=2\cos\dfrac{u+v}{2}\cos\dfrac{u-v}{2},\qquad \cos u-\cos v=-2\sin\dfrac{u+v}{2}\sin\dfrac{u-v}{2}'),
  M(r'\sin u+\sin v=2\sin\dfrac{u+v}{2}\cos\dfrac{u-v}{2},\qquad \sin u-\sin v=2\cos\dfrac{u+v}{2}\sin\dfrac{u-v}{2}'),
  T(r'The sum-to-product formulas come from the product-to-sum ones with \(u=a+b\), \(v=a-b\).', r'Công thức tổng thành tích suy ra từ công thức tích thành tổng với \(u=a+b\), \(v=a-b\).'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'),
  T(r'\(\sin(a+b)\ne\sin a+\sin b\) and \(\cos 2a\ne 2\cos a\). Signs matter: \(\cos(a+b)\) has a minus sign between the two products.', r'\(\sin(a+b)\ne\sin a+\sin b\) và \(\cos 2a\ne 2\cos a\). Chú ý dấu: \(\cos(a+b)\) có dấu trừ giữa hai tích.'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Exact value with the addition formula', 'Giá trị chính xác bằng công thức cộng'),
  T(r'Find the exact value of \(\sin 75^\circ\).', r'Tính giá trị chính xác của \(\sin 75^\circ\).'),
  (r'Write \(75^\circ=45^\circ+30^\circ\) and use the formula for \(\sin(a+b)\).', r'Viết \(75^\circ=45^\circ+30^\circ\) và dùng công thức \(\sin(a+b)\).'),
  [T(r'\(\sin 75^\circ=\sin 45^\circ\cos 30^\circ+\cos 45^\circ\sin 30^\circ\).', r'\(\sin 75^\circ=\sin 45^\circ\cos 30^\circ+\cos 45^\circ\sin 30^\circ\).'),
   T(r'\(=\dfrac{\sqrt2}{2}\cdot\dfrac{\sqrt3}{2}+\dfrac{\sqrt2}{2}\cdot\dfrac12=\dfrac{\sqrt6+\sqrt2}{4}\).', r'\(=\dfrac{\sqrt2}{2}\cdot\dfrac{\sqrt3}{2}+\dfrac{\sqrt2}{2}\cdot\dfrac12=\dfrac{\sqrt6+\sqrt2}{4}\).')],
  r'\(\sin 75^\circ=\dfrac{\sqrt6+\sqrt2}{4}\).')
examples += EXAMPLE(2, ('Intermediate', 'Trung bình'), ('Double angle', 'Góc nhân đôi'),
  T(r'Given \(\sin\alpha=\dfrac35\) and \(\dfrac{\pi}{2}\lt\alpha\lt\pi\), find \(\sin 2\alpha\), \(\cos 2\alpha\) and \(\tan 2\alpha\).', r'Cho \(\sin\alpha=\dfrac35\) và \(\dfrac{\pi}{2}\lt\alpha\lt\pi\). Tính \(\sin 2\alpha\), \(\cos 2\alpha\) và \(\tan 2\alpha\).'),
  (r'Find \(\cos\alpha\) first (decide its sign), then use the double-angle formulas.', r'Tìm \(\cos\alpha\) trước (xác định dấu), rồi dùng công thức nhân đôi.'),
  [T(r'\(\cos^2\alpha=1-\dfrac{9}{25}=\dfrac{16}{25}\); \(\alpha\) is in quadrant II so \(\cos\alpha=-\dfrac45\).', r'\(\cos^2\alpha=1-\dfrac{9}{25}=\dfrac{16}{25}\); \(\alpha\) thuộc góc phần tư II nên \(\cos\alpha=-\dfrac45\).'),
   T(r'\(\sin 2\alpha=2\cdot\dfrac35\cdot\left(-\dfrac45\right)=-\dfrac{24}{25}\).', r'\(\sin 2\alpha=2\cdot\dfrac35\cdot\left(-\dfrac45\right)=-\dfrac{24}{25}\).'),
   T(r'\(\cos 2\alpha=1-2\sin^2\alpha=1-\dfrac{18}{25}=\dfrac{7}{25}\).', r'\(\cos 2\alpha=1-2\sin^2\alpha=1-\dfrac{18}{25}=\dfrac{7}{25}\).'),
   T(r'\(\tan 2\alpha=\dfrac{\sin 2\alpha}{\cos 2\alpha}=-\dfrac{24}{7}\).', r'\(\tan 2\alpha=\dfrac{\sin 2\alpha}{\cos 2\alpha}=-\dfrac{24}{7}\).')],
  r'\(\sin 2\alpha=-\dfrac{24}{25}\), \(\cos 2\alpha=\dfrac{7}{25}\), \(\tan 2\alpha=-\dfrac{24}{7}\).')
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Product to sum', 'Tích thành tổng'),
  T(r'Compute \(\cos 15^\circ\cos 75^\circ\) without a calculator.', r'Tính \(\cos 15^\circ\cos 75^\circ\) không dùng máy tính.'),
  (r'Use \(\cos a\cos b=\dfrac12[\cos(a-b)+\cos(a+b)]\) with \(a=15^\circ\), \(b=75^\circ\).', r'Dùng \(\cos a\cos b=\dfrac12[\cos(a-b)+\cos(a+b)]\) với \(a=15^\circ\), \(b=75^\circ\).'),
  [T(r'\(\cos 15^\circ\cos 75^\circ=\dfrac12\left[\cos(-60^\circ)+\cos 90^\circ\right]\).', r'\(\cos 15^\circ\cos 75^\circ=\dfrac12\left[\cos(-60^\circ)+\cos 90^\circ\right]\).'),
   T(r'\(=\dfrac12\left(\dfrac12+0\right)=\dfrac14\).', r'\(=\dfrac12\left(\dfrac12+0\right)=\dfrac14\).')],
  r'\(\dfrac14\).')
examples += EXAMPLE(4, ('Advanced', 'Nâng cao'), ('Proving an identity', 'Chứng minh đẳng thức'),
  T(r'Prove that \(\dfrac{\sin 2x}{1+\cos 2x}=\tan x\) (when both sides are defined).', r'Chứng minh \(\dfrac{\sin 2x}{1+\cos 2x}=\tan x\) (khi hai vế xác định).'),
  (r'Rewrite the numerator and the denominator with the double-angle formulas, then cancel.', r'Viết tử và mẫu bằng công thức nhân đôi, rồi rút gọn.'),
  [T(r'\(\sin 2x=2\sin x\cos x\) and \(1+\cos 2x=2\cos^2 x\).', r'\(\sin 2x=2\sin x\cos x\) và \(1+\cos 2x=2\cos^2 x\).'),
   T(r'So the left side is \(\dfrac{2\sin x\cos x}{2\cos^2 x}=\dfrac{\sin x}{\cos x}=\tan x\), which is the right side.', r'Vậy vế trái bằng \(\dfrac{2\sin x\cos x}{2\cos^2 x}=\dfrac{\sin x}{\cos x}=\tan x\), chính là vế phải.')],
  r'The identity is proved.')
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Sum to product', 'Tổng thành tích'),
  T(r'Simplify \(B=\dfrac{\sin x+\sin 3x}{\cos x+\cos 3x}\) (when it is defined).', r'Rút gọn \(B=\dfrac{\sin x+\sin 3x}{\cos x+\cos 3x}\) (khi biểu thức xác định).'),
  (r'Turn the numerator and the denominator into products; the common factor is \(\cos x\).', r'Biến đổi tử và mẫu thành tích; thừa số chung là \(\cos x\).'),
  [T(r'\(\sin x+\sin 3x=2\sin 2x\cos x\).', r'\(\sin x+\sin 3x=2\sin 2x\cos x\).'),
   T(r'\(\cos x+\cos 3x=2\cos 2x\cos x\).', r'\(\cos x+\cos 3x=2\cos 2x\cos x\).'),
   T(r'\(B=\dfrac{2\sin 2x\cos x}{2\cos 2x\cos x}=\tan 2x\).', r'\(B=\dfrac{2\sin 2x\cos x}{2\cos 2x\cos x}=\tan 2x\).')],
  r'\(B=\tan 2x\).')

# ----- Bài tập từng mức: cùng dạng (A1 sin2a, A2 cos2a, A3 công thức cộng; B4, B5 đúng/sai; C6 nhân đôi bằng số, C7 hạ bậc) -----
def _mcq(n, qe, qv, opts, ans, ee, ev): return MCQ(n, (qe, qv), opts, ans, (ee, ev))
H = ('Enter a number or a fraction.', 'Nhập một số hoặc phân số.')
P1 = [
  [_mcq(1, r'If \(\sin\alpha=\dfrac35\) and \(\cos\alpha=\dfrac45\), what is \(\sin 2\alpha\)?', r'Nếu \(\sin\alpha=\dfrac35\) và \(\cos\alpha=\dfrac45\) thì \(\sin 2\alpha\) bằng bao nhiêu?', [r'\dfrac{12}{25}', r'\dfrac{24}{25}', r'\dfrac{7}{25}', r'\dfrac65'], 'b', r'Answer: b. \(2\cdot\dfrac35\cdot\dfrac45=\dfrac{24}{25}\).', r'Đáp án b. \(2\cdot\dfrac35\cdot\dfrac45=\dfrac{24}{25}\).'),
   _mcq(2, r'If \(\cos\alpha=\dfrac12\), what is \(\cos 2\alpha\)?', r'Nếu \(\cos\alpha=\dfrac12\) thì \(\cos 2\alpha\) bằng bao nhiêu?', [r'\dfrac12', r'-\dfrac12', '1', '0'], 'b', r'Answer: b. \(2\cos^2\alpha-1=2\cdot\dfrac14-1=-\dfrac12\).', r'Đáp án b. \(2\cos^2\alpha-1=2\cdot\dfrac14-1=-\dfrac12\).'),
   _mcq(3, r'What is \(\cos 40^\circ\cos 20^\circ-\sin 40^\circ\sin 20^\circ\)?', r'\(\cos 40^\circ\cos 20^\circ-\sin 40^\circ\sin 20^\circ\) bằng bao nhiêu?', [r'\dfrac12', r'\dfrac{\sqrt3}{2}', '0', '1'], 'a', r'Answer: a. It equals \(\cos(40^\circ+20^\circ)=\cos 60^\circ=\dfrac12\).', r'Đáp án a. Biểu thức bằng \(\cos(40^\circ+20^\circ)=\cos 60^\circ=\dfrac12\).')],
  [TF(4, (r'\(\sin 2a=2\sin a\cos a\) for every \(a\).', r'\(\sin 2a=2\sin a\cos a\) với mọi \(a\).'), 'true', (r'True. It is the addition formula with \(b=a\).', r'Đúng. Đây là công thức cộng với \(b=a\).')),
   TF(5, (r'\(\sin(a+b)=\sin a+\sin b\) for every \(a\), \(b\).', r'\(\sin(a+b)=\sin a+\sin b\) với mọi \(a\), \(b\).'), 'false', (r'False. \(\sin(a+b)=\sin a\cos b+\cos a\sin b\). For example \(a=b=\dfrac{\pi}{2}\) gives \(0\ne 2\).', r'Sai. \(\sin(a+b)=\sin a\cos b+\cos a\sin b\). Chẳng hạn \(a=b=\dfrac{\pi}{2}\) cho \(0\ne 2\).'))],
  [SHORT(6, (r'Compute \(2\sin 15^\circ\cos 15^\circ\).', r'Tính \(2\sin 15^\circ\cos 15^\circ\).'), '0.5|1/2', 'number', H, (r'Answer: \(\dfrac12\). It equals \(\sin 30^\circ\).', r'Đáp số: \(\dfrac12\). Biểu thức bằng \(\sin 30^\circ\).')),
   SHORT(7, (r'Given \(\cos 2\alpha=0.2\), find \(\sin^2\alpha\).', r'Cho \(\cos 2\alpha=0{,}2\). Tính \(\sin^2\alpha\).'), '0.4|2/5', 'number', H, (r'Answer: \(0.4\). \(\sin^2\alpha=\dfrac{1-0.2}{2}\).', r'Đáp số: \(0{,}4\). \(\sin^2\alpha=\dfrac{1-0{,}2}{2}\).'))]]
P2 = [
  [_mcq(1, r'If \(\sin\alpha=\dfrac{5}{13}\) and \(\cos\alpha=\dfrac{12}{13}\), what is \(\sin 2\alpha\)?', r'Nếu \(\sin\alpha=\dfrac{5}{13}\) và \(\cos\alpha=\dfrac{12}{13}\) thì \(\sin 2\alpha\) bằng bao nhiêu?', [r'\dfrac{60}{169}', r'\dfrac{120}{169}', r'\dfrac{119}{169}', r'\dfrac{10}{13}'], 'b', r'Answer: b. \(2\cdot\dfrac{5}{13}\cdot\dfrac{12}{13}=\dfrac{120}{169}\).', r'Đáp án b. \(2\cdot\dfrac{5}{13}\cdot\dfrac{12}{13}=\dfrac{120}{169}\).'),
   _mcq(2, r'If \(\sin\alpha=\dfrac12\), what is \(\cos 2\alpha\)?', r'Nếu \(\sin\alpha=\dfrac12\) thì \(\cos 2\alpha\) bằng bao nhiêu?', [r'\dfrac12', r'-\dfrac12', '0', r'\dfrac34'], 'a', r'Answer: a. \(1-2\sin^2\alpha=1-2\cdot\dfrac14=\dfrac12\).', r'Đáp án a. \(1-2\sin^2\alpha=1-2\cdot\dfrac14=\dfrac12\).'),
   _mcq(3, r'What is \(\sin 50^\circ\cos 10^\circ+\cos 50^\circ\sin 10^\circ\)?', r'\(\sin 50^\circ\cos 10^\circ+\cos 50^\circ\sin 10^\circ\) bằng bao nhiêu?', [r'\dfrac12', r'\dfrac{\sqrt3}{2}', '1', r'\dfrac{\sqrt2}{2}'], 'b', r'Answer: b. It equals \(\sin(50^\circ+10^\circ)=\sin 60^\circ=\dfrac{\sqrt3}{2}\).', r'Đáp án b. Biểu thức bằng \(\sin(50^\circ+10^\circ)=\sin 60^\circ=\dfrac{\sqrt3}{2}\).')],
  [TF(4, (r'\(\cos 2a=\cos^2 a+\sin^2 a\) for every \(a\).', r'\(\cos 2a=\cos^2 a+\sin^2 a\) với mọi \(a\).'), 'false', (r'False. \(\cos 2a=\cos^2 a-\sin^2 a\); the sum is always \(1\).', r'Sai. \(\cos 2a=\cos^2 a-\sin^2 a\); còn tổng luôn bằng \(1\).')),
   TF(5, (r'\(\cos(a-b)=\cos a\cos b+\sin a\sin b\) for every \(a\), \(b\).', r'\(\cos(a-b)=\cos a\cos b+\sin a\sin b\) với mọi \(a\), \(b\).'), 'true', (r'True. This is the basic addition formula.', r'Đúng. Đây là công thức cộng cơ bản.'))],
  [SHORT(6, (r'Compute \(4\sin 15^\circ\cos 15^\circ\).', r'Tính \(4\sin 15^\circ\cos 15^\circ\).'), '1', 'number', H, (r'Answer: 1. It equals \(2\sin 30^\circ\).', r'Đáp số: 1. Biểu thức bằng \(2\sin 30^\circ\).')),
   SHORT(7, (r'Given \(\cos 2\alpha=0.5\), find \(\sin^2\alpha\).', r'Cho \(\cos 2\alpha=0{,}5\). Tính \(\sin^2\alpha\).'), '0.25|1/4', 'number', H, (r'Answer: \(0.25\). \(\sin^2\alpha=\dfrac{1-0.5}{2}\).', r'Đáp số: \(0{,}25\). \(\sin^2\alpha=\dfrac{1-0{,}5}{2}\).'))]]
P3 = [
  [_mcq(1, r'If \(\sin\alpha=\dfrac{8}{17}\) and \(\cos\alpha=\dfrac{15}{17}\), what is \(\sin 2\alpha\)?', r'Nếu \(\sin\alpha=\dfrac{8}{17}\) và \(\cos\alpha=\dfrac{15}{17}\) thì \(\sin 2\alpha\) bằng bao nhiêu?', [r'\dfrac{120}{289}', r'\dfrac{240}{289}', r'\dfrac{161}{289}', r'\dfrac{16}{17}'], 'b', r'Answer: b. \(2\cdot\dfrac{8}{17}\cdot\dfrac{15}{17}=\dfrac{240}{289}\).', r'Đáp án b. \(2\cdot\dfrac{8}{17}\cdot\dfrac{15}{17}=\dfrac{240}{289}\).'),
   _mcq(2, r'If \(\cos\alpha=0\), what is \(\cos 2\alpha\)?', r'Nếu \(\cos\alpha=0\) thì \(\cos 2\alpha\) bằng bao nhiêu?', ['1', '-1', '0', r'\dfrac12'], 'b', r'Answer: b. \(2\cos^2\alpha-1=-1\).', r'Đáp án b. \(2\cos^2\alpha-1=-1\).'),
   _mcq(3, r'What is \(\sin 80^\circ\cos 20^\circ-\cos 80^\circ\sin 20^\circ\)?', r'\(\sin 80^\circ\cos 20^\circ-\cos 80^\circ\sin 20^\circ\) bằng bao nhiêu?', [r'\dfrac12', r'\dfrac{\sqrt2}{2}', '1', r'\dfrac{\sqrt3}{2}'], 'd', r'Answer: d. It equals \(\sin(80^\circ-20^\circ)=\sin 60^\circ=\dfrac{\sqrt3}{2}\).', r'Đáp án d. Biểu thức bằng \(\sin(80^\circ-20^\circ)=\sin 60^\circ=\dfrac{\sqrt3}{2}\).')],
  [TF(4, (r'\(\cos 2a=2\cos^2 a-1\) for every \(a\).', r'\(\cos 2a=2\cos^2 a-1\) với mọi \(a\).'), 'true', (r'True. It follows from \(\cos 2a=\cos^2 a-\sin^2 a\) and \(\sin^2 a=1-\cos^2 a\).', r'Đúng. Suy ra từ \(\cos 2a=\cos^2 a-\sin^2 a\) và \(\sin^2 a=1-\cos^2 a\).')),
   TF(5, (r'\(\tan(a+b)=\tan a+\tan b\) whenever it is defined.', r'\(\tan(a+b)=\tan a+\tan b\) mỗi khi hai vế xác định.'), 'false', (r'False. \(\tan(a+b)=\dfrac{\tan a+\tan b}{1-\tan a\tan b}\). For example \(a=b=\dfrac{\pi}{4}\) gives \(\tan\dfrac{\pi}{2}\), not \(2\).', r'Sai. \(\tan(a+b)=\dfrac{\tan a+\tan b}{1-\tan a\tan b}\). Chẳng hạn \(a=b=\dfrac{\pi}{4}\) cho \(\tan\dfrac{\pi}{2}\), không phải \(2\).'))],
  [SHORT(6, (r'Compute \(8\sin 15^\circ\cos 15^\circ\).', r'Tính \(8\sin 15^\circ\cos 15^\circ\).'), '2', 'number', H, (r'Answer: 2. It equals \(4\sin 30^\circ\).', r'Đáp số: 2. Biểu thức bằng \(4\sin 30^\circ\).')),
   SHORT(7, (r'Given \(\cos 2\alpha=-0.2\), find \(\sin^2\alpha\).', r'Cho \(\cos 2\alpha=-0{,}2\). Tính \(\sin^2\alpha\).'), '0.6|3/5', 'number', H, (r'Answer: \(0.6\). \(\sin^2\alpha=\dfrac{1+0.2}{2}\).', r'Đáp số: \(0{,}6\). \(\sin^2\alpha=\dfrac{1+0{,}2}{2}\).'))]]
practice = LEVEL_PRACTICE([('A. Multiple Choice', 'A. Trắc nghiệm'), ('B. True or False', 'B. Đúng hoặc sai'), ('C. Short Answer', 'C. Trả lời ngắn')], {1: P1, 2: P2, 3: P3})

mistakes = [
 (r'<b>Sums.</b> Writing \(\sin(a+b)=\sin a+\sin b\). Use \(\sin(a+b)=\sin a\cos b+\cos a\sin b\).', r'<b>Tổng.</b> Viết \(\sin(a+b)=\sin a+\sin b\). Phải dùng \(\sin(a+b)=\sin a\cos b+\cos a\sin b\).'),
 (r'<b>Signs.</b> Mixing the signs of \(\cos(a+b)\) and \(\cos(a-b)\): the sign in the middle is opposite to the sign inside.', r'<b>Dấu.</b> Nhầm dấu của \(\cos(a+b)\) và \(\cos(a-b)\): dấu ở giữa ngược với dấu trong ngoặc.'),
 (r'<b>Double angle.</b> Writing \(\cos 2a=2\cos a\) or \(\sin 2a=2\sin a\). The angle is doubled, not the value.', r'<b>Góc nhân đôi.</b> Viết \(\cos 2a=2\cos a\) hoặc \(\sin 2a=2\sin a\). Chỉ góc được nhân đôi, giá trị thì không.'),
 (r'<b>Power reducing.</b> Forgetting the factor \(\dfrac12\) in \(\sin^2 a=\dfrac{1-\cos 2a}{2}\).', r'<b>Hạ bậc.</b> Quên thừa số \(\dfrac12\) trong \(\sin^2 a=\dfrac{1-\cos 2a}{2}\).'),
 (r'<b>Domain.</b> Cancelling a factor such as \(\cos x\) without checking that it is not zero.', r'<b>Điều kiện.</b> Rút gọn một thừa số như \(\cos x\) mà không kiểm tra nó khác \(0\).'),
]
summary = [
 (r'\(\cos(a\mp b)=\cos a\cos b\pm\sin a\sin b\); \(\sin(a\pm b)=\sin a\cos b\pm\cos a\sin b\); \(\tan(a\pm b)=\dfrac{\tan a\pm\tan b}{1\mp\tan a\tan b}\).', r'\(\cos(a\mp b)=\cos a\cos b\pm\sin a\sin b\); \(\sin(a\pm b)=\sin a\cos b\pm\cos a\sin b\); \(\tan(a\pm b)=\dfrac{\tan a\pm\tan b}{1\mp\tan a\tan b}\).'),
 (r'\(\sin 2a=2\sin a\cos a\); \(\cos 2a=\cos^2 a-\sin^2 a=2\cos^2 a-1=1-2\sin^2 a\); \(\tan 2a=\dfrac{2\tan a}{1-\tan^2 a}\).', r'\(\sin 2a=2\sin a\cos a\); \(\cos 2a=\cos^2 a-\sin^2 a=2\cos^2 a-1=1-2\sin^2 a\); \(\tan 2a=\dfrac{2\tan a}{1-\tan^2 a}\).'),
 (r'\(\sin^2 a=\dfrac{1-\cos 2a}{2}\), \(\cos^2 a=\dfrac{1+\cos 2a}{2}\).', r'\(\sin^2 a=\dfrac{1-\cos 2a}{2}\), \(\cos^2 a=\dfrac{1+\cos 2a}{2}\).'),
 ('Product-to-sum and sum-to-product formulas turn products into sums and sums into products; they help simplify and solve equations.', 'Công thức tích thành tổng và tổng thành tích giúp đổi qua lại giữa tích và tổng, dùng để rút gọn và giải phương trình.'),
 ('Key English phrases: simplify the expression; prove the identity; express the product as a sum.', 'Cụm tiếng Anh cần nhớ: simplify the expression (rút gọn biểu thức); prove the identity (chứng minh đẳng thức); express the product as a sum (biến đổi tích thành tổng).'),
]
checks = [
 ('I can use the addition formulas to find exact values.', 'Tôi dùng được công thức cộng để tìm giá trị chính xác.'),
 ('I can use the double-angle and power-reducing formulas.', 'Tôi dùng được công thức nhân đôi và hạ bậc.'),
 ('I can turn products into sums and sums into products.', 'Tôi biến đổi được tích thành tổng và tổng thành tích.'),
 ('I can simplify an expression and prove a simple identity.', 'Tôi rút gọn được biểu thức và chứng minh được đẳng thức đơn giản.'),
 STD_SUMMARY_CHECK_EN(),
]

lesson(id=LID, title_en='Trigonometric Formulas', title_vi='Công thức lượng giác', topic=TOPIC,
       folder='trigonometric-functions', file='trigonometric-formulas',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Addition, double-angle, power-reducing, product-to-sum and sum-to-product formulas.', level='Intermediate', minutes=60,
       description_vi='Bài 2 – Công thức cộng, nhân đôi, hạ bậc, biến đổi tích thành tổng và tổng thành tích.',
       tags_vi=['công thức cộng', 'công thức nhân đôi', 'hạ bậc', 'tích thành tổng', 'tổng thành tích', 'rút gọn', 'chứng minh đẳng thức'],
       prerequisites=['g11-trigf-01'], tags=['addition formula', 'double angle', 'product to sum', 'sum to product', 'identity'], order=25)
