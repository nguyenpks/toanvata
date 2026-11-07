# -*- coding: utf-8 -*-
"""g11-deriv-03 = Toán 11 KNTT, Bài 33: Đạo hàm cấp hai. Mã ngân hàng câu hỏi: TOAN11-C9-B33."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g11k as S

P_ = S.poly
CV = 'Đạo hàm cấp hai'
vocab = defs(CV, [
 ('secder', 'second derivative', 'đạo hàm cấp hai', 'the derivative of \\(f′\\), written \\(f″\\) or \\(y″\\).', 'đạo hàm của \\(f′\\), kí hiệu \\(f″\\) hay \\(y″\\).', 'The second derivative of x³ is 6x.', '\\(f″\\)'),
 ('instacc', 'instantaneous acceleration', 'gia tốc tức thời', '\\(a(t)=v′(t)=s″(t)\\).', '\\(a(t)=v′(t)=s″(t)\\).', 'The instantaneous acceleration at t = 2 s is 0.', '\\(s″(t)\\)'),
 ('higherder', 'higher-order derivative', 'đạo hàm cấp cao', 'the derivative of order \\(n\\): \\(f^{(n)}=\\left(f^{(n-1)}\\right)′\\).', 'đạo hàm cấp \\(n\\): \\(f^{(n)}=\\left(f^{(n-1)}\\right)′\\).', 'The fourth derivative of sin x is sin x.', '\\(f^{(n)}\\)')])
goals = [('define and compute the second derivative \\(f″\\);', 'hiểu và tính được [[đạo hàm cấp hai]] \\(f″\\);'),
         ('interpret \\(s″(t)\\) as instantaneous acceleration;', 'hiểu \\(s″(t)\\) là [[gia tốc tức thời]] của chuyển động;'),
         ('solve motion problems: when the velocity or acceleration is zero, speeding up or slowing down;', 'giải bài toán chuyển động: khi nào vận tốc, gia tốc bằng 0; vật nhanh dần hay chậm dần;'),
         ('compute some higher-order derivatives.', 'tính một số [[đạo hàm cấp cao]] đơn giản.')]
phrases = [('<b>Differentiate twice.</b>', 'Lấy đạo hàm hai lần.'), ('<b>Acceleration is the derivative of velocity.</b>', 'Gia tốc là đạo hàm của vận tốc.'),
           ('<b>The object stops when the velocity is zero.</b>', 'Vật dừng lại khi vận tốc bằng 0.'), ('<b>The car is slowing down.</b>', 'Xe đang chuyển động chậm dần.'), ('<b>The second derivative of sine is minus sine.</b>', 'Đạo hàm cấp hai của sin là trừ sin.')]
review = T('From Bài 31–32: \\(v(t)=s′(t)\\); \\((x^n)′=nx^{n-1}\\), \\((\\sin u)′=u′\\cos u\\), \\((e^u)′=u′e^u\\), \\((\\ln u)′=\\frac{u′}{u}\\), product and quotient rules.',
           'Từ Bài 31–32: \\(v(t)=s′(t)\\); \\((x^n)′=nx^{n-1}\\), \\((\\sin u)′=u′\\cos u\\), \\((e^u)′=u′e^u\\), \\((\\ln u)′=\\frac{u′}{u}\\), quy tắc tích, thương.')

theory = '<h3>33.1 %s</h3>' % TI('Definition', 'Định nghĩa')
theory += BOX('mint', ('Second derivative', 'Đạo hàm cấp hai'), T('If \\(y=f(x)\\) has a derivative \\(y′=f′(x)\\) on \\((a;b)\\) and \\(f′\\) also has a derivative there, then \\((f′)′\\) is the <b>second derivative</b>: \\(y″=f″(x)=(f′(x))′\\). Similarly \\(f‴=(f″)′\\), \\(f^{(n)}=\\left(f^{(n-1)}\\right)′\\).',
  'Giả sử \\(y=f(x)\\) có đạo hàm \\(y′=f′(x)\\) trên \\((a;b)\\) và \\(f′\\) cũng có đạo hàm trên khoảng đó. Khi đó \\((f′)′\\) gọi là [[đạo hàm cấp hai]] của \\(f\\): \\(y″=f″(x)=(f′(x))′\\). Tương tự \\(f‴=(f″)′\\), [[đạo hàm cấp cao]] cấp \\(n\\): \\(f^{(n)}=\\left(f^{(n-1)}\\right)′\\).'))
theory += BOX('blue', ('Examples', 'Ví dụ nhanh'), UL([T('\\(y=x^4\\): \\(y′=4x^3\\), \\(y″=12x^2\\), \\(y‴=24x\\), \\(y^{(4)}=24\\), \\(y^{(5)}=0\\).', '\\(y=x^4\\): \\(y′=4x^3\\), \\(y″=12x^2\\), \\(y‴=24x\\), \\(y^{(4)}=24\\), \\(y^{(5)}=0\\).'),
  T('\\(y=\\sin x\\): \\(y′=\\cos x\\), \\(y″=-\\sin x\\) (so \\(y″+y=0\\)).', '\\(y=\\sin x\\): \\(y′=\\cos x\\), \\(y″=-\\sin x\\) (nên \\(y″+y=0\\)).'), T('\\(y=e^{kx}\\): \\(y″=k^2e^{kx}\\); \\(y=\\ln x\\): \\(y″=-\\dfrac1{x^2}\\).', '\\(y=e^{kx}\\): \\(y″=k^2e^{kx}\\); \\(y=\\ln x\\): \\(y″=-\\dfrac1{x^2}\\).')]))
theory += '<h3>33.2 %s</h3>' % TI('Mechanical meaning', 'Ý nghĩa cơ học')
theory += BOX('mint', ('Acceleration', 'Gia tốc tức thời'), T('For a motion \\(s=s(t)\\): velocity \\(v(t)=s′(t)\\), acceleration \\(a(t)=v′(t)=s″(t)\\). If \\(v\\) and \\(a\\) have the same sign the object speeds up; opposite signs: it slows down.',
  'Với chuyển động \\(s=s(t)\\): vận tốc \\(v(t)=s′(t)\\), [[gia tốc tức thời]] \\(a(t)=v′(t)=s″(t)\\). Nếu \\(v\\) và \\(a\\) cùng dấu thì vật chuyển động nhanh dần; trái dấu thì chậm dần.'))
assert all(abs(f) < 1e-9 for f in [3 * 1 - 12 * 1 + 9, 3 * 9 - 36 + 9, 6 * 2 - 12])
theory += GRAPH({'view': [-0.3, 4.6, -13, 13], 'functions': [{'f': 'x^3-6x^2+9x', 'label': 's = t³ − 6t² + 9t', 'domain': [0, 4.5]}, {'f': '3x^2-12x+9', 'label': 'v = 3t² − 12t + 9', 'color': '#7c3aed', 'domain': [0, 4.5]}, {'f': '6x-12', 'label': 'a = 6t − 12', 'color': '#c2410c', 'domain': [0, 4.5]}],
                 'points': [{'x': 1, 'y': 0}, {'x': 3, 'y': 0}, {'x': 2, 'y': 0}]},
                cap=('Horizontal axis: time t (s). The velocity v vanishes at t = 1 and t = 3 (the object turns back), the acceleration a vanishes at t = 2.', 'Trục hoành: thời gian t (giây). Vận tốc v bằng 0 tại t = 1 và t = 3 (vật đổi chiều), gia tốc a bằng 0 tại t = 2.'),
                alt=('Graphs of position, velocity and acceleration of a motion over four and a half seconds', ''), height=330)
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('\\(a=0\\) does not mean the object is at rest: at \\(t=2\\) above, \\(v=-3\\) m/s. "At rest" means \\(v=0\\).', '\\(a=0\\) không có nghĩa là vật đứng yên: ở hình trên, tại \\(t=2\\) thì \\(v=-3\\) m/s. Vật dừng khi \\(v=0\\).'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Computing \\(f″\\)', 'Tính đạo hàm cấp hai'), T('Find \\(f″(x)\\) and \\(f″(1)\\) for \\(f(x)=x^3-3x^2+4x-5\\).', 'Tính \\(f″(x)\\) và \\(f″(1)\\) với \\(f(x)=x^3-3x^2+4x-5\\).'),
  T('Differentiate twice.', 'Lấy đạo hàm hai lần.'), [T('\\(f′(x)=3x^2-6x+4\\).', '\\(f′(x)=3x^2-6x+4\\).'), T('\\(f″(x)=6x-6\\), \\(f″(1)=0\\).', '\\(f″(x)=6x-6\\), \\(f″(1)=0\\).')], T('\\(f″(x)=6x-6\\); \\(f″(1)=0\\).', '\\(f″(x)=6x-6\\); \\(f″(1)=0\\).'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Trigonometric and exponential', 'Hàm lượng giác và hàm mũ'), T('Find \\(y″\\) for (a) \\(y=\\cos 2x\\); (b) \\(y=xe^x\\).', 'Tính \\(y″\\): a) \\(y=\\cos 2x\\); b) \\(y=xe^x\\).'),
  T('Chain rule; product rule.', 'Hàm hợp; quy tắc tích.'), [T('(a) \\(y′=-2\\sin 2x\\), \\(y″=-4\\cos 2x\\).', 'a) \\(y′=-2\\sin 2x\\), \\(y″=-4\\cos 2x\\).'), T('(b) \\(y′=e^x+xe^x=(x+1)e^x\\), \\(y″=e^x+(x+1)e^x=(x+2)e^x\\).', 'b) \\(y′=e^x+xe^x=(x+1)e^x\\), \\(y″=e^x+(x+1)e^x=(x+2)e^x\\).')],
  T('\\(-4\\cos 2x\\); \\((x+2)e^x\\).', '\\(-4\\cos 2x\\); \\((x+2)e^x\\).'))
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Motion of an object', 'Chuyển động của một vật'), T('An object moves with \\(s(t)=t^3-6t^2+9t\\) (m, s), \\(0\\le t\\le4{,}5\\). (a) Find the velocity and the acceleration at \\(t=2\\). (b) When is the object at rest? (c) When is it slowing down?', 'Một vật chuyển động theo \\(s(t)=t^3-6t^2+9t\\) (m, s), \\(0\\le t\\le4{,}5\\). a) Tính vận tốc, gia tốc tại \\(t=2\\). b) Khi nào vật dừng lại? c) Trong khoảng nào vật chuyển động chậm dần?'),
  T('\\(v=3t^2-12t+9\\), \\(a=6t-12\\).', '\\(v=3t^2-12t+9\\), \\(a=6t-12\\).'), [T('(a) \\(v(2)=-3\\) m/s, \\(a(2)=0\\).', 'a) \\(v(2)=-3\\) m/s, \\(a(2)=0\\).'), T('(b) \\(v=0\\iff t=1\\) or \\(t=3\\).', 'b) \\(v=0\\iff t=1\\) hoặc \\(t=3\\).'),
   T('(c) Slowing down when \\(v\\), \\(a\\) have opposite signs: \\(0<t<1\\) (\\(v>0\\), \\(a<0\\)) and \\(2<t<3\\) (\\(v<0\\), \\(a>0\\)).', 'c) Chậm dần khi \\(v\\), \\(a\\) trái dấu: \\(0<t<1\\) (\\(v>0\\), \\(a<0\\)) và \\(2<t<3\\) (\\(v<0\\), \\(a>0\\)).')],
  T('(a) \\(-3\\) m/s, \\(0\\); (b) \\(t=1\\), \\(t=3\\); (c) \\((0;1)\\) and \\((2;3)\\).', 'a) \\(-3\\) m/s, \\(0\\); b) \\(t=1\\), \\(t=3\\); c) \\((0;1)\\) và \\((2;3)\\).'))
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Braking car', 'Ô tô phanh gấp'), T('After braking, a car travels \\(s(t)=20t-2{,}5t^2\\) (m). Find its acceleration and the time and distance until it stops.', 'Sau khi đạp phanh, ô tô đi được quãng đường \\(s(t)=20t-2{,}5t^2\\) (m). Tính gia tốc của xe, thời gian và quãng đường từ lúc phanh đến khi dừng.'),
  T('Stop: \\(v=0\\).', 'Xe dừng khi \\(v=0\\).'), [T('\\(v=20-5t\\), \\(a=-5\\) m/s² (constant, opposite to \\(v\\)).', '\\(v=20-5t\\), \\(a=-5\\) m/s² (không đổi, ngược dấu với \\(v\\): chậm dần đều).'), T('\\(v=0\\Rightarrow t=4\\) s; \\(s(4)=80-40=40\\) m.', '\\(v=0\\Rightarrow t=4\\) s; \\(s(4)=80-40=40\\) m.')],
  T('\\(a=-5\\) m/s²; 4 s; 40 m.', '\\(a=-5\\) m/s²; 4 giây; 40 m.'))
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Spring oscillation', 'Dao động của lò xo'), T('A mass on a spring moves with \\(x(t)=4\\cos(\\pi t)\\) (cm, s). Show that \\(x″=-\\pi^2x\\) and find the acceleration at \\(t=\\frac13\\).', 'Một vật gắn lò xo dao động theo \\(x(t)=4\\cos(\\pi t)\\) (cm, s). Chứng minh \\(x″=-\\pi^2x\\) và tính gia tốc tại \\(t=\\frac13\\).'),
  T('Differentiate twice.', 'Lấy đạo hàm hai lần.'), [T('\\(x′=-4\\pi\\sin(\\pi t)\\), \\(x″=-4\\pi^2\\cos(\\pi t)=-\\pi^2x\\).', '\\(x′=-4\\pi\\sin(\\pi t)\\), \\(x″=-4\\pi^2\\cos(\\pi t)=-\\pi^2x\\).'), T('\\(a\\left(\\frac13\\right)=-4\\pi^2\\cdot\\frac12=-2\\pi^2\\approx-19{,}7\\) cm/s².', '\\(a\\left(\\frac13\\right)=-4\\pi^2\\cdot\\frac12=-2\\pi^2\\approx-19{,}7\\) cm/s².')],
  T('\\(-2\\pi^2\\) cm/s² (always pointing towards the equilibrium).', '\\(-2\\pi^2\\) cm/s² (gia tốc luôn hướng về vị trí cân bằng).'))
assert abs(2 * math.pi ** 2 - 19.74) < 0.01


def lvl(P):
    a, b, c, x0 = P['poly']; cs = [a, b, c, 1]; v = 6 * a * x0 + 2 * b
    o1 = M4(1, 'For \\(f(x)=%s\\), \\(f″(%d)=\\)…' % (P_(cs), x0), 'Cho \\(f(x)=%s\\). Khi đó \\(f″(%d)=\\)…' % (P_(cs), x0), '\\(%d\\)' % v,
            ['\\(%d\\)' % (3 * a * x0 * x0 + 2 * b * x0 + c), '\\(%d\\)' % (3 * a * x0 + 2 * b), '\\(%d\\)' % (6 * a * x0 + b), '\\(%d\\)' % (-v)], 'Twice.', '\\(f′(x)=%s\\), \\(f″(x)=%s\\).' % (P_([3 * a, 2 * b, c]), P_([6 * a, 2 * b])))
    kind, k = P['trig']
    if kind == 'sin': f, cor, wr = '\\sin %dx' % k, "\\(y″=-%d\\sin %dx\\)" % (k * k, k), ["\\(y″=%d\\sin %dx\\)" % (k * k, k), "\\(y″=-%d\\sin %dx\\)" % (k, k), "\\(y″=-%d\\cos %dx\\)" % (k * k, k)]
    else: f, cor, wr = 'e^{-%dx}' % k, "\\(y″=%de^{-%dx}\\)" % (k * k, k), ["\\(y″=-%de^{-%dx}\\)" % (k * k, k), "\\(y″=%de^{-%dx}\\)" % (2 * k, k), "\\(y″=-%de^{-%dx}\\)" % (k, k)]
    o2 = M4(2, 'For \\(y=%s\\)…' % f, 'Đạo hàm cấp hai của \\(y=%s\\) là…' % f, cor, wr, 'Chain rule twice.', 'Mỗi lần lấy đạo hàm nhân thêm \\(%s\\).' % (('%d' % k) if kind == 'sin' else '-%d' % k))
    p, q, t0 = P['mot']; cs2 = [1, -p, q, 0]; acc = 6 * t0 - 2 * p
    o3 = M4(3, 'An object moves with \\(s(t)=%s\\) (m, s). The acceleration at \\(t=%d\\) is…' % (P_(cs2, 't'), t0), 'Một vật chuyển động theo \\(s(t)=%s\\) (m, s). Gia tốc tại \\(t=%d\\) là…' % (P_(cs2, 't'), t0), '\\(%d\\) m/s²' % acc,
            ['\\(%d\\) m/s²' % (3 * t0 * t0 - 2 * p * t0 + q), '\\(%d\\) m/s²' % (6 * t0 - p), '\\(%d\\) m/s²' % (t0 ** 3 - p * t0 * t0 + q * t0), '\\(%d\\) m/s²' % (3 * t0 - 2 * p)], '\\(a=s″\\).', '\\(v=%s\\), \\(a=%s\\).' % (P_([3, -2 * p, q], 't'), P_([6, -2 * p], 't')))
    (se, sv), v4 = P['t4']
    t4 = tf(4, se, sv, v4, 'Compute directly.', 'Tính trực tiếp đạo hàm cấp hai.')
    (te, tv), v5 = P['t5']
    t5 = tf(5, te, tv, v5, 'Velocity vs acceleration.', 'Phân biệt vận tốc và gia tốc.')
    u, w = P['brake']
    s6 = sh(6, 'After braking a car travels \\(s(t)=%dt-%s t^2\\) (m). How many metres does it travel before stopping?' % (u, fr(F(w, 2))), 'Sau khi phanh, ô tô đi được \\(s(t)=%dt-%s\\,t^2\\) (m). Ô tô đi thêm bao nhiêu mét thì dừng hẳn?' % (u, fr(F(w, 2))),
            int(F(u * u, 2 * w)), '\\(v=0\\).', '\\(v=%d-%dt=0\\Rightarrow t=%s\\); thay vào \\(s(t)\\).' % (u, w, fr(F(u, w))))
    n, x7 = P['high']
    s7 = sh(7, '\\(f(x)=x^%d\\). Find \\(f‴(%d)\\).' % (n, x7), 'Cho \\(f(x)=x^%d\\). Tính đạo hàm cấp ba \\(f‴(%d)\\).' % (n, x7), n * (n - 1) * (n - 2) * x7 ** (n - 3), 'Three times.', '\\(f‴(x)=%d\\cdot%d\\cdot%d\\,x^{%d}\\).' % (n, n - 1, n - 2, n - 3))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]


PP = [dict(poly=(1, -3, 2, 2), trig=('sin', 2), mot=(6, 5, 3),
           t4=(('\\(y=\\sin x\\) satisfies \\(y″+y=0\\).', 'Hàm số \\(y=\\sin x\\) thỏa mãn \\(y″+y=0\\).'), True),
           t5=(('If the acceleration is zero, the object is at rest.', 'Nếu gia tốc bằng 0 thì vật đứng yên.'), False), brake=(20, 4), high=(4, 2)),
      dict(poly=(2, 1, -4, -1), trig=('exp', 3), mot=(9, 10, 2),
           t4=(('The second derivative of a quadratic function is a constant.', 'Đạo hàm cấp hai của hàm số bậc hai là một hằng số.'), True),
           t5=(('If \\(v\\gt0\\) and \\(a\\lt0\\), the object is speeding up.', 'Nếu \\(v\\gt0\\) và \\(a\\lt0\\) thì vật chuyển động nhanh dần.'), False), brake=(30, 6), high=(5, 1)),
      dict(poly=(-1, 4, 3, 1), trig=('sin', 3), mot=(3, 7, 4),
           t4=(('\\((x^5)^{(5)}=120\\).', 'Đạo hàm cấp năm của \\(x^5\\) bằng 120.'), True),
           t5=(('\\(\\left(\\ln x\\right)″=\\dfrac1{x^2}\\) for \\(x\\gt0\\).', '\\(\\left(\\ln x\\right)″=\\dfrac1{x^2}\\) với \\(x\\gt0\\).'), False), brake=(24, 8), high=(4, 3))]
practice = three(lvl, PP)
practice = with_self(practice, S.M33S11, start=8)
mistakes = [('<b>Taking \\(f″=(f)^2\\) or \\(f′\\cdot f′\\).</b> \\(f″\\) means differentiating \\(f′\\) again.', '<b>Hiểu \\(f″\\) là \\((f′)^2\\).</b> \\(f″\\) là đạo hàm của \\(f′\\).'),
            ('<b>Confusing velocity and acceleration.</b> \\(v=s′\\), \\(a=s″\\).', '<b>Nhầm vận tốc với gia tốc.</b> \\(v=s′\\), \\(a=s″\\).'),
            ('<b>"\\(a=0\\) so the object stops".</b> The object stops when \\(v=0\\).', '<b>"\\(a=0\\) nên vật dừng".</b> Vật dừng khi \\(v=0\\).'),
            ('<b>Losing the factor \\(k\\) twice.</b> \\((\\sin kx)″=-k^2\\sin kx\\).', '<b>Quên nhân \\(k\\) ở lần lấy đạo hàm thứ hai.</b> \\((\\sin kx)″=-k^2\\sin kx\\).')]
summary = [('\\(f″=(f′)′\\); \\(f^{(n)}=\\left(f^{(n-1)}\\right)′\\).', '\\(f″=(f′)′\\); \\(f^{(n)}=\\left(f^{(n-1)}\\right)′\\).'), ('\\(a(t)=v′(t)=s″(t)\\); same signs: speeding up, opposite signs: slowing down.', '\\(a(t)=v′(t)=s″(t)\\); \\(v\\), \\(a\\) cùng dấu: nhanh dần; trái dấu: chậm dần.'),
           ('\\((\\sin kx)″=-k^2\\sin kx\\), \\((e^{kx})″=k^2e^{kx}\\), \\((\\ln x)″=-\\frac1{x^2}\\).', '\\((\\sin kx)″=-k^2\\sin kx\\), \\((e^{kx})″=k^2e^{kx}\\), \\((\\ln x)″=-\\frac1{x^2}\\).'), ('Key words: second derivative, acceleration, speeding up, slowing down.', 'Từ cần nhớ: second derivative, acceleration, speeding up, slowing down.')]
checks = [('I can compute second derivatives.', 'Em tính được đạo hàm cấp hai.'), ('I can find the acceleration of a motion.', 'Em tính được gia tốc tức thời.'), ('I can tell when an object speeds up or slows down.', 'Em xác định được khi nào vật nhanh dần, chậm dần.'), ('I can compute simple higher derivatives.', 'Em tính được đạo hàm cấp cao đơn giản.')]
LL('g11-deriv-03', 'The Second Derivative', CV, ('Derivatives', 'Đạo hàm'), 'derivatives', 'second-derivative', 340, 'Intermediate', 60, ('rules of differentiation', 'các quy tắc tính đạo hàm'),
   'The second derivative and higher derivatives, acceleration, speeding up and slowing down, oscillations.', 'Bài 33 – Đạo hàm cấp hai, đạo hàm cấp cao; ý nghĩa cơ học (gia tốc tức thời); chuyển động nhanh dần, chậm dần; dao động.',
   ['second derivative', 'acceleration', 'motion'], ['đạo hàm cấp hai', 'gia tốc', 'chuyển động'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g11-deriv-02'])
