# -*- coding: utf-8 -*-
"""g10-trig-01 = Toán 10 KNTT, Bài 5: Giá trị lượng giác của một góc từ 0° đến 180°. Mã ngân hàng câu hỏi: TOAN10-C3-B05."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g10b, trigval as TV

CV = 'Giá trị lượng giác của góc từ 0° đến 180°'
vocab = defs(CV, [
 ('semicircle', 'unit semicircle', 'nửa đường tròn đơn vị', 'the upper half of the circle with centre \\(O\\) and radius 1.', 'nửa trên của đường tròn tâm \\(O\\), bán kính 1.', 'Draw a point on the unit semicircle.', ''),
 ('sine', 'sine', 'sin (sin của góc)', 'the \\(y\\)-coordinate of the point on the unit semicircle.', 'tung độ của điểm trên nửa đường tròn đơn vị.', 'The sine of 30 degrees is one half.', '\\(\\sin\\alpha\\)'),
 ('cosine', 'cosine', 'cos (cos của góc)', 'the \\(x\\)-coordinate of the point on the unit semicircle.', 'hoành độ của điểm trên nửa đường tròn đơn vị.', 'The cosine of 60 degrees is one half.', '\\(\\cos\\alpha\\)'),
 ('tangent', 'tangent', 'tan (tang của góc)', '\\(\\sin\\alpha\\) divided by \\(\\cos\\alpha\\).', '\\(\\sin\\alpha\\) chia \\(\\cos\\alpha\\) (khi \\(\\cos\\alpha\\ne0\\)).', 'The tangent of 45 degrees is 1.', '\\(\\tan\\alpha\\)'),
 ('cotangent', 'cotangent', 'cot (cotang của góc)', '\\(\\cos\\alpha\\) divided by \\(\\sin\\alpha\\).', '\\(\\cos\\alpha\\) chia \\(\\sin\\alpha\\) (khi \\(\\sin\\alpha\\ne0\\)).', 'The cotangent of 45 degrees is 1.', '\\(\\cot\\alpha\\)'),
 ('suppl', 'supplementary angles', 'hai góc bù nhau', 'two angles whose sum is \\(180^\\circ\\).', 'hai góc có tổng bằng \\(180^\\circ\\).', '30 and 150 degrees are supplementary angles.', ''),
 ('obtuse', 'obtuse angle', 'góc tù', 'an angle between \\(90^\\circ\\) and \\(180^\\circ\\).', 'góc lớn hơn \\(90^\\circ\\) và nhỏ hơn \\(180^\\circ\\).', '120 degrees is an obtuse angle.', ''),
 ('identity', 'identity', 'đẳng thức (hệ thức)', 'an equation that is true for every allowed value.', 'đẳng thức đúng với mọi giá trị cho phép.', 'Use the identity sin squared plus cos squared equals 1.', '')])
goals = [('define \\(\\sin,\\cos,\\tan,\\cot\\) of an angle from \\(0^\\circ\\) to \\(180^\\circ\\);', 'nhận biết [[sin (sin của góc)]], [[cos (cos của góc)]], [[tan (tang của góc)]], [[cot (cotang của góc)]] của góc từ \\(0^\\circ\\) đến \\(180^\\circ\\);'),
 ('remember the values at special angles;', 'nhớ giá trị lượng giác của các góc đặc biệt;'),
 ('use supplementary angles and the basic identities;', 'dùng [[hai góc bù nhau]] và các [[đẳng thức (hệ thức)]] cơ bản;'),
 ('solve simple geometry and real-life problems.', 'giải bài toán hình học và thực tế đơn giản.')]
phrases = [('<b>Find the value of \\(\\sin 120^\\circ\\).</b>', 'Tính giá trị của \\(\\sin 120^\\circ\\).'), ('<b>supplementary angles</b>', 'hai góc bù nhau'), ('<b>Find the angle \\(\\alpha\\).</b>', 'Tìm góc \\(\\alpha\\).'), ('<b>is defined / undefined</b>', 'xác định / không xác định')]
review = T('In a right triangle: \\(\\sin\\alpha=\\dfrac{\\text{opposite}}{\\text{hypotenuse}}\\), \\(\\cos\\alpha=\\dfrac{\\text{adjacent}}{\\text{hypotenuse}}\\), \\(\\tan\\alpha=\\dfrac{\\text{opposite}}{\\text{adjacent}}\\) for acute angles.', 'Trong tam giác vuông, với góc nhọn: \\(\\sin\\alpha=\\dfrac{\\text{đối}}{\\text{huyền}}\\), \\(\\cos\\alpha=\\dfrac{\\text{kề}}{\\text{huyền}}\\), \\(\\tan\\alpha=\\dfrac{\\text{đối}}{\\text{kề}}\\).')
c60 = [0.5, 3 ** .5 / 2]
fig = GE({'view': [-1.4, 1.4, -0.45, 1.4], 'axes': True, 'steps': [
  {'type': 'point', 'id': 'O', 'at': [0, 0], 'name': 'O', 'fixed': True}, {'type': 'circle', 'center': 'O', 'radius': 1, 'style': {'fillOpacity': 0, 'dash': 0}},
  {'type': 'point', 'id': 'P', 'at': c60, 'name': 'P', 'fixed': True}, {'type': 'segment', 'through': ['O', 'P']},
  {'type': 'point', 'id': 'H', 'at': [c60[0], 0], 'name': 'H', 'fixed': True}, {'type': 'segment', 'through': ['P', 'H'], 'style': {'dash': 2, 'strokeColor': '#c2410c'}},
  {'type': 'point', 'id': 'A', 'at': [1, 0], 'name': 'A', 'fixed': True}, {'type': 'angle', 'points': ['A', 'O', 'P'], 'radius': 0.25}]},
  'The point \\(P\\) on the unit circle with \\(\\widehat{AOP}=\\alpha\\): \\(\\cos\\alpha=OH\\) (the \\(x\\)-coordinate) and \\(\\sin\\alpha=PH\\) (the \\(y\\)-coordinate).', 'Điểm \\(P\\) trên đường tròn đơn vị với \\(\\widehat{AOP}=\\alpha\\): \\(\\cos\\alpha=OH\\) (hoành độ) và \\(\\sin\\alpha=PH\\) (tung độ).', 330)
rows = []
for a in TV.ANG:
    rows.append(['\\(%d^\\circ\\)' % a] + ['\\(%s\\)' % TV.val(f, a) if TV.val(f, a) is not None else '—' for f in ('sin', 'cos', 'tan', 'cot')])
theory = '<h3>5.1 %s</h3>' % TI('Trigonometric ratios of an angle \\(0^\\circ\\le\\alpha\\le180^\\circ\\)', 'Giá trị lượng giác của góc \\(\\alpha\\) (\\(0^\\circ\\le\\alpha\\le180^\\circ\\))')
theory += BOX('blue', ('Definition', 'Định nghĩa'), T('Take the point \\(P(x_0;y_0)\\) on the unit semicircle with \\(\\widehat{AOP}=\\alpha\\). Then \\(\\sin\\alpha=y_0\\), \\(\\cos\\alpha=x_0\\), \\(\\tan\\alpha=\\dfrac{y_0}{x_0}\\) (\\(\\alpha\\ne90^\\circ\\)), \\(\\cot\\alpha=\\dfrac{x_0}{y_0}\\) (\\(\\alpha\\ne0^\\circ,180^\\circ\\)).', 'Lấy điểm \\(P(x_0;y_0)\\) trên nửa đường tròn đơn vị sao cho \\(\\widehat{AOP}=\\alpha\\). Khi đó \\(\\sin\\alpha=y_0\\), \\(\\cos\\alpha=x_0\\), \\(\\tan\\alpha=\\dfrac{y_0}{x_0}\\) (\\(\\alpha\\ne90^\\circ\\)), \\(\\cot\\alpha=\\dfrac{x_0}{y_0}\\) (\\(\\alpha\\ne0^\\circ,180^\\circ\\)).'))
theory += fig
theory += BOX('mint', ('Signs', 'Dấu'), T('\\(\\sin\\alpha\\ge0\\) for all \\(\\alpha\\) in \\([0^\\circ,180^\\circ]\\). For an <b>obtuse angle</b>: \\(\\cos\\alpha\\lt0\\), \\(\\tan\\alpha\\lt0\\), \\(\\cot\\alpha\\lt0\\).', '\\(\\sin\\alpha\\ge0\\) với mọi \\(\\alpha\\in[0^\\circ,180^\\circ]\\). Với [[góc tù]]: \\(\\cos\\alpha\\lt0\\), \\(\\tan\\alpha\\lt0\\), \\(\\cot\\alpha\\lt0\\).'))
theory += '<h3>5.2 %s</h3>' % TI('Special values', 'Giá trị lượng giác của các góc đặc biệt')
theory += TBL(['\\(\\alpha\\)', '\\(\\sin\\alpha\\)', '\\(\\cos\\alpha\\)', '\\(\\tan\\alpha\\)', '\\(\\cot\\alpha\\)'], rows)
theory += '<h3>5.3 %s</h3>' % TI('Supplementary angles and identities', 'Hai góc bù nhau và các hệ thức cơ bản')
theory += BOX('blue', ('Supplementary angles', 'Hai góc bù nhau'), M('\\sin(180^\\circ-\\alpha)=\\sin\\alpha,\\quad \\cos(180^\\circ-\\alpha)=-\\cos\\alpha'), M('\\tan(180^\\circ-\\alpha)=-\\tan\\alpha,\\quad \\cot(180^\\circ-\\alpha)=-\\cot\\alpha'))
theory += BOX('mint', ('Basic identities', 'Các hệ thức cơ bản'), M('\\sin^2\\alpha+\\cos^2\\alpha=1'), M('1+\\tan^2\\alpha=\\dfrac{1}{\\cos^2\\alpha}\\ (\\alpha\\ne90^\\circ)\\qquad 1+\\cot^2\\alpha=\\dfrac{1}{\\sin^2\\alpha}\\ (0^\\circ\\lt\\alpha\\lt180^\\circ)'), M('\\tan\\alpha\\cdot\\cot\\alpha=1\\qquad \\sin(90^\\circ-\\alpha)=\\cos\\alpha'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('\\(\\tan90^\\circ\\) is undefined, and \\(\\cot0^\\circ\\), \\(\\cot180^\\circ\\) are undefined. Use a calculator in <b>degree</b> mode.', '\\(\\tan90^\\circ\\) không xác định; \\(\\cot0^\\circ\\), \\(\\cot180^\\circ\\) cũng không xác định. Dùng máy tính ở chế độ <b>độ</b>.'))
assert all(abs(TV.num('sin', a) ** 2 + TV.num('cos', a) ** 2 - 1) < 1e-12 for a in TV.ANG)
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Special values', 'Giá trị đặc biệt'),
  T('Find \\(\\sin120^\\circ\\), \\(\\cos135^\\circ\\) and \\(\\tan150^\\circ\\).', 'Tính \\(\\sin120^\\circ\\), \\(\\cos135^\\circ\\) và \\(\\tan150^\\circ\\).'), ('Write the angle as \\(180^\\circ-\\beta\\) with \\(\\beta\\) acute.', 'Viết góc dạng \\(180^\\circ-\\beta\\) với \\(\\beta\\) nhọn.'),
  [T('\\(\\sin120^\\circ=\\sin60^\\circ=\\dfrac{\\sqrt3}{2}\\).', '\\(\\sin120^\\circ=\\sin60^\\circ=\\dfrac{\\sqrt3}{2}\\).'), T('\\(\\cos135^\\circ=-\\cos45^\\circ=-\\dfrac{\\sqrt2}{2}\\).', '\\(\\cos135^\\circ=-\\cos45^\\circ=-\\dfrac{\\sqrt2}{2}\\).'), T('\\(\\tan150^\\circ=-\\tan30^\\circ=-\\dfrac{\\sqrt3}{3}\\).', '\\(\\tan150^\\circ=-\\tan30^\\circ=-\\dfrac{\\sqrt3}{3}\\).')],
  T('\\(\\dfrac{\\sqrt3}{2},\\ -\\dfrac{\\sqrt2}{2},\\ -\\dfrac{\\sqrt3}{3}\\).', '\\(\\dfrac{\\sqrt3}{2},\\ -\\dfrac{\\sqrt2}{2},\\ -\\dfrac{\\sqrt3}{3}\\).'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('From sine to cosine', 'Từ sin tính cos'),
  T('Angle \\(\\alpha\\) is obtuse and \\(\\sin\\alpha=\\dfrac35\\). Find \\(\\cos\\alpha\\) and \\(\\tan\\alpha\\).', 'Góc \\(\\alpha\\) tù và \\(\\sin\\alpha=\\dfrac35\\). Tính \\(\\cos\\alpha\\) và \\(\\tan\\alpha\\).'), ('Use \\(\\sin^2+\\cos^2=1\\) and the sign for an obtuse angle.', 'Dùng \\(\\sin^2+\\cos^2=1\\) và dấu của góc tù.'),
  [T('\\(\\cos^2\\alpha=1-\\dfrac{9}{25}=\\dfrac{16}{25}\\), so \\(\\cos\\alpha=\\pm\\dfrac45\\).', '\\(\\cos^2\\alpha=1-\\dfrac{9}{25}=\\dfrac{16}{25}\\) nên \\(\\cos\\alpha=\\pm\\dfrac45\\).'), T('The angle is obtuse, so \\(\\cos\\alpha=-\\dfrac45\\) and \\(\\tan\\alpha=\\dfrac{3/5}{-4/5}=-\\dfrac34\\).', 'Góc tù nên \\(\\cos\\alpha=-\\dfrac45\\) và \\(\\tan\\alpha=\\dfrac{3/5}{-4/5}=-\\dfrac34\\).')], T('\\(\\cos\\alpha=-\\dfrac45,\\ \\tan\\alpha=-\\dfrac34\\).', '\\(\\cos\\alpha=-\\dfrac45,\\ \\tan\\alpha=-\\dfrac34\\).'))
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Evaluate an expression', 'Tính giá trị biểu thức'),
  T('Compute \\(A=\\sin30^\\circ+\\cos120^\\circ+\\tan135^\\circ\\).', 'Tính \\(A=\\sin30^\\circ+\\cos120^\\circ+\\tan135^\\circ\\).'), ('Replace each value from the table.', 'Thay từng giá trị từ bảng.'),
  [T('\\(\\sin30^\\circ=\\dfrac12\\), \\(\\cos120^\\circ=-\\dfrac12\\), \\(\\tan135^\\circ=-1\\).', '\\(\\sin30^\\circ=\\dfrac12\\), \\(\\cos120^\\circ=-\\dfrac12\\), \\(\\tan135^\\circ=-1\\).'), T('\\(A=\\dfrac12-\\dfrac12-1=-1\\).', '\\(A=\\dfrac12-\\dfrac12-1=-1\\).')], T('\\(A=-1\\).', '\\(A=-1\\).'))
assert abs(TV.num('sin', 30) + TV.num('cos', 120) + TV.num('tan', 135) + 1) < 1e-12
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Using \\(\\tan\\alpha\\)', 'Dùng giá trị của \\(\\tan\\alpha\\)'),
  T('Given \\(\\tan\\alpha=3\\), find \\(B=\\dfrac{2\\sin\\alpha+\\cos\\alpha}{\\sin\\alpha-\\cos\\alpha}\\).', 'Cho \\(\\tan\\alpha=3\\). Tính \\(B=\\dfrac{2\\sin\\alpha+\\cos\\alpha}{\\sin\\alpha-\\cos\\alpha}\\).'), ('Divide the numerator and the denominator by \\(\\cos\\alpha\\ne0\\).', 'Chia cả tử và mẫu cho \\(\\cos\\alpha\\ne0\\).'),
  [T('\\(B=\\dfrac{2\\tan\\alpha+1}{\\tan\\alpha-1}=\\dfrac{2\\cdot3+1}{3-1}=\\dfrac72\\).', '\\(B=\\dfrac{2\\tan\\alpha+1}{\\tan\\alpha-1}=\\dfrac{2\\cdot3+1}{3-1}=\\dfrac72\\).')], T('\\(B=\\dfrac72\\).', '\\(B=\\dfrac72\\).'))
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('A real-life problem', 'Bài toán thực tế'),
  T('A kite string is 40 m long and makes an angle of \\(60^\\circ\\) with the ground. Find the height of the kite, and the horizontal distance from the kite to the person.', 'Dây diều dài 40 m, tạo với mặt đất góc \\(60^\\circ\\). Tính độ cao của diều và khoảng cách theo phương ngang từ diều đến người thả.'), ('The string is the hypotenuse of a right triangle.', 'Sợi dây là cạnh huyền của tam giác vuông.'),
  [T('Height \\(=40\\sin60^\\circ=40\\cdot\\dfrac{\\sqrt3}{2}=20\\sqrt3\\approx34.6\\) m.', 'Độ cao \\(=40\\sin60^\\circ=40\\cdot\\dfrac{\\sqrt3}{2}=20\\sqrt3\\approx34{,}6\\) m.'), T('Horizontal distance \\(=40\\cos60^\\circ=20\\) m.', 'Khoảng cách ngang \\(=40\\cos60^\\circ=20\\) m.')], T('About 34.6 m high and 20 m away horizontally.', 'Cao khoảng 34,6 m; cách theo phương ngang 20 m.'))
assert abs(20 * 3 ** .5 - 34.641) < 1e-3

def lvl(p):
    f1, a1, sn, tn, ang, ee_ = p['f'], p['a'], p['sin'], p['t'], p['ang'], p['e']
    FNn = {'sin': '\\sin', 'cos': '\\cos', 'tan': '\\tan', 'cot': '\\cot'}
    v1 = TV.val(f1, a1); pool = list(dict.fromkeys(TV.val(g, b) for g in FNn for b in (30, 45, 60, 120, 135, 150) if TV.val(g, b) and TV.val(g, b) != v1))
    o1 = M4(1, 'What is \\(%s%d^\\circ\\)?' % (FNn[f1], a1), 'Giá trị của \\(%s%d^\\circ\\) là bao nhiêu?' % (FNn[f1], a1), v1, pool[:3], 'Use the table: \\(%s%d^\\circ=%s\\).' % (FNn[f1], a1, v1), 'Dùng bảng: \\(%s%d^\\circ=%s\\).' % (FNn[f1], a1, v1))
    s_, c_ = sn; cs = fr(F(-c_, 1)) if False else None
    a_, b_, c__ = s_
    o2 = M4(2, 'Angle \\(\\alpha\\) is obtuse, \\(\\sin\\alpha=\\dfrac{%d}{%d}\\). Find \\(\\cos\\alpha\\).' % (a_, c__), 'Góc \\(\\alpha\\) tù, \\(\\sin\\alpha=\\dfrac{%d}{%d}\\). Tính \\(\\cos\\alpha\\).' % (a_, c__), fr(F(-b_, c__)), [fr(F(b_, c__)), fr(F(-a_, c__)), fr(F(-b_, a_))], 'Use \\(\\cos^2\\alpha=1-\\sin^2\\alpha\\); the angle is obtuse so the cosine is negative.', 'Dùng \\(\\cos^2\\alpha=1-\\sin^2\\alpha\\); góc tù nên cos âm.')
    t = tn; v3 = F(t + 1, t - 1)
    o3 = M4(3, 'Given \\(\\tan\\alpha=%d\\), find \\(\\dfrac{\\sin\\alpha+\\cos\\alpha}{\\sin\\alpha-\\cos\\alpha}\\).' % t, 'Cho \\(\\tan\\alpha=%d\\). Tính \\(\\dfrac{\\sin\\alpha+\\cos\\alpha}{\\sin\\alpha-\\cos\\alpha}\\).' % t, fr(v3), [fr(F(t - 1, t + 1)), fr(v3 + 1), fr(-v3)], 'Divide by \\(\\cos\\alpha\\): \\(\\dfrac{\\tan\\alpha+1}{\\tan\\alpha-1}=%s\\).' % fr(v3), 'Chia cho \\(\\cos\\alpha\\): \\(\\dfrac{\\tan\\alpha+1}{\\tan\\alpha-1}=%s\\).' % fr(v3))
    x = p['x']; tfv = p['tfv']
    stm = ['\\cos(180^\\circ-%d^\\circ)=\\cos%d^\\circ' % (x, x), '\\tan(180^\\circ-%d^\\circ)=-\\tan%d^\\circ' % (x, x), '\\sin(180^\\circ-%d^\\circ)=\\sin%d^\\circ' % (x, x)][p['k']]
    t4 = tf(4, 'The equality \\(%s\\) is true.' % stm, 'Đẳng thức \\(%s\\) là đúng.' % stm, tfv[0], 'Supplementary angles: sin is equal, the others change sign.', 'Hai góc bù: sin bằng nhau, các giá trị khác đổi dấu.')
    y = p['y']; stm2 = p['id'] % (y, y)
    t5 = tf(5, 'The equality \\(%s\\) is true.' % stm2, 'Đẳng thức \\(%s\\) là đúng.' % stm2, tfv[1], p['idn'], p['idv'])
    s6 = sh(6, 'Compute \\(%s\\).' % p['ex'], 'Tính \\(%s\\).' % p['ex'], p['exv'], 'Substitute special values: %s.' % p['exv'], 'Thay giá trị đặc biệt: %s.' % p['exv'])
    s7 = sh(7, 'Find the obtuse angle \\(\\alpha\\) (in degrees) with \\(%s\\).' % p['ang'][0], 'Tìm góc tù \\(\\alpha\\) (đơn vị độ) thỏa \\(%s\\).' % p['ang'][0], p['ang'][1], 'Use the table: \\(\\alpha=%d^\\circ\\).' % p['ang'][1], 'Dùng bảng: \\(\\alpha=%d^\\circ\\).' % p['ang'][1])
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
P = [dict(f='sin', a=120, sin=((3, 4, 5), 0), t=2, e=0, x=40, k=0, tfv=(False, True), y=50, id='\\sin^2%d^\\circ+\\cos^2%d^\\circ=1', idn='\\(\\sin^2\\alpha+\\cos^2\\alpha=1\\) for every angle.', idv='\\(\\sin^2\\alpha+\\cos^2\\alpha=1\\) với mọi góc.', ex='\\sin30^\\circ+\\cos60^\\circ', exv=1, ang=('\\sin\\alpha=\\dfrac12', 150)),
     dict(f='cos', a=135, sin=((5, 12, 13), 0), t=3, e=0, x=25, k=1, tfv=(True, False), y=30, id='1+\\tan^2%d^\\circ=\\dfrac{1}{\\sin^2%d^\\circ}', idn='The correct identity is \\(1+\\tan^2\\alpha=\\dfrac{1}{\\cos^2\\alpha}\\).', idv='Hệ thức đúng là \\(1+\\tan^2\\alpha=\\dfrac{1}{\\cos^2\\alpha}\\).', ex='\\sin150^\\circ+\\cos120^\\circ', exv=0, ang=('\\cos\\alpha=-\\dfrac12', 120)),
     dict(f='tan', a=150, sin=((8, 15, 17), 0), t=5, e=0, x=70, k=2, tfv=(True, True), y=60, id='1+\\cot^2%d^\\circ=\\dfrac{1}{\\sin^2%d^\\circ}', idn='This is a correct identity.', idv='Đây là một hệ thức đúng.', ex='2\\sin90^\\circ+\\cos180^\\circ', exv=1, ang=('\\tan\\alpha=-1', 135))]
for q in P: q['sin'] = (q['sin'][0], 0)
for q in P:
    for a, b, c in [q['sin'][0]]: assert a * a + b * b == c * c
assert all(abs(1 + TV.num('tan', 25) ** 2 - 1 / TV.num('cos', 25) ** 2) < 1e-9 for _ in [0]) and abs(1 + TV.num('cot', 60) ** 2 - 1 / TV.num('sin', 60) ** 2) < 1e-9
assert abs(TV.num('sin', 30) + TV.num('cos', 60) - 1) < 1e-12 and abs(TV.num('sin', 150) + TV.num('cos', 120)) < 1e-12 and abs(2 * TV.num('sin', 90) + TV.num('cos', 180) - 1) < 1e-12
assert TV.val('sin', 150) == '\\dfrac{1}{2}' and TV.val('cos', 120) == '-\\dfrac{1}{2}' and TV.val('tan', 135) == '-1'
practice = LEVEL_PRACTICE(GRP, {lv: lvl(p) for lv, p in zip((1, 2, 3), P)})
practice = with_self(practice, sp_g10b.B5, start=8)
mistakes = [('<b>Wrong sign for an obtuse angle.</b> \\(\\cos,\\tan,\\cot\\) are negative when \\(90^\\circ\\lt\\alpha\\lt180^\\circ\\).', '<b>Sai dấu với góc tù.</b> \\(\\cos,\\tan,\\cot\\) âm khi \\(90^\\circ\\lt\\alpha\\lt180^\\circ\\).'),
 ('<b>Mixing \\(\\sin\\) and \\(\\cos\\) in \\(180^\\circ-\\alpha\\).</b> Only \\(\\sin\\) keeps its sign.', '<b>Nhầm \\(\\sin\\) với \\(\\cos\\) ở góc \\(180^\\circ-\\alpha\\).</b> Chỉ \\(\\sin\\) giữ nguyên dấu.'),
 ('<b>Using \\(\\tan90^\\circ\\).</b> It is undefined.', '<b>Dùng \\(\\tan90^\\circ\\).</b> Giá trị này không xác định.'),
 ('<b>Calculator in radian mode.</b> Switch to degrees.', '<b>Máy tính ở chế độ radian.</b> Hãy chuyển sang độ.'),
 ('<b>Forgetting \\(\\sin^2\\alpha+\\cos^2\\alpha=1\\) gives two signs.</b> Choose the sign from the angle.', '<b>Quên \\(\\sin^2\\alpha+\\cos^2\\alpha=1\\) cho hai dấu.</b> Chọn dấu theo góc.')]
summary = [('\\(\\sin\\alpha\\) and \\(\\cos\\alpha\\) are the coordinates of a point on the unit semicircle.', '\\(\\sin\\alpha\\) và \\(\\cos\\alpha\\) là tung độ và hoành độ của điểm trên nửa đường tròn đơn vị.'),
 ('Supplementary angles: \\(\\sin\\) equal; \\(\\cos,\\tan,\\cot\\) opposite.', 'Hai góc bù nhau: \\(\\sin\\) bằng nhau; \\(\\cos,\\tan,\\cot\\) đối nhau.'),
 ('\\(\\sin^2\\alpha+\\cos^2\\alpha=1\\); \\(\\tan\\alpha=\\dfrac{\\sin\\alpha}{\\cos\\alpha}\\); \\(\\cot\\alpha=\\dfrac{\\cos\\alpha}{\\sin\\alpha}\\).', '\\(\\sin^2\\alpha+\\cos^2\\alpha=1\\); \\(\\tan\\alpha=\\dfrac{\\sin\\alpha}{\\cos\\alpha}\\); \\(\\cot\\alpha=\\dfrac{\\cos\\alpha}{\\sin\\alpha}\\).'),
 ('Remember the table of special values for \\(0^\\circ,30^\\circ,45^\\circ,60^\\circ,90^\\circ\\).', 'Nhớ bảng giá trị đặc biệt của \\(0^\\circ,30^\\circ,45^\\circ,60^\\circ,90^\\circ\\).'),
 ('Key English words: sine, cosine, tangent, cotangent, supplementary angles, obtuse angle.', 'Từ tiếng Anh cần nhớ: sine, cosine, tangent, cotangent, supplementary angles, obtuse angle.')]
checks = [('I can read \\(\\sin,\\cos\\) from the unit semicircle.', 'Tôi đọc được sin, cos từ nửa đường tròn đơn vị.'), ('I know the special values.', 'Tôi nhớ các giá trị đặc biệt.'), ('I can use supplementary angles.', 'Tôi dùng được hai góc bù nhau.'), ('I can use the basic identities.', 'Tôi dùng được các hệ thức cơ bản.'), STD_SUMMARY_CHECK_EN()]
lesson(id='g10-trig-01', title_en='Trigonometric Ratios of Angles from 0° to 180°', title_vi='Giá trị lượng giác của một góc từ 0° đến 180°', topic=('Basic Trigonometry', 'Hệ thức lượng trong tam giác'), folder='trigonometry', file='trig-ratios-0-180',
  catalog_title_vi='Giá trị lượng giác của một góc từ 0° đến 180°', meta=dict(level=('Intermediate', 'Trung bình'), time=('about 70 minutes', 'khoảng 70 phút'), before=('right-triangle ratios, \\(\\sqrt{\\ }\\), fractions', 'tỉ số lượng giác trong tam giác vuông, căn bậc hai, phân số')),
  goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples, practice=practice, mistakes=mistakes, summary=summary, checks=checks,
  description='Sine, cosine, tangent and cotangent of angles from 0 to 180 degrees, special values and basic identities.', level='Intermediate', minutes=70,
  description_vi='Bài 5 – Giá trị lượng giác của góc từ 0° đến 180°, giá trị đặc biệt, hai góc bù nhau và các hệ thức cơ bản.',
  tags_vi=['sin', 'cos', 'tan', 'cot', 'góc tù', 'hai góc bù nhau'], prerequisites=[], tags=['sine', 'cosine', 'tangent', 'supplementary angles'], order=50)
