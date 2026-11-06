# -*- coding: utf-8 -*-
"""g10-func-04 = Toán 10 KNTT, Bài 18: Phương trình quy về phương trình bậc hai. Mã ngân hàng câu hỏi: TOAN10-C6-B18."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g10g as S
from sp_g10f import poly

CV = 'Phương trình quy về phương trình bậc hai'
vocab = defs(CV, [
 ('rteq', 'equation with a square root', 'phương trình chứa căn thức', 'an equation in which the unknown appears under \\(\\sqrt{\\ }\\).', 'phương trình có ẩn nằm dưới dấu căn bậc hai.', 'Solve the equation with a square root.', ''),
 ('squaring', 'square both sides', 'bình phương hai vế', 'raise both sides to the power 2; it may create extra roots, so every root must be checked.', 'nâng hai vế lên lũy thừa 2; có thể sinh nghiệm thừa nên phải thử lại.', 'Square both sides of the equation.', ''),
 ('extrarts', 'extraneous root', 'nghiệm ngoại lai', 'a root of the squared equation that does not satisfy the original equation.', 'nghiệm của phương trình sau khi bình phương nhưng không thỏa mãn phương trình ban đầu.', 'x = −3 is an extraneous root.', ''),
 ('biquad', 'biquadratic equation', 'phương trình trùng phương', '\\(ax^4+bx^2+c=0\\) (\\(a\\ne0\\)); put \\(t=x^2\\ge0\\).', '\\(ax^4+bx^2+c=0\\) (\\(a\\ne0\\)); đặt \\(t=x^2\\ge0\\).', 'A biquadratic equation can have four roots.', '')])
goals = [('recognise equations that reduce to quadratic equations;', 'nhận biết các dạng phương trình quy về phương trình bậc hai;'),
         ('solve \\(\\sqrt{f(x)}=\\sqrt{g(x)}\\) and \\(\\sqrt{f(x)}=g(x)\\) by squaring and checking;', 'giải [[phương trình chứa căn thức]] \\(\\sqrt{f(x)}=\\sqrt{g(x)}\\), \\(\\sqrt{f(x)}=g(x)\\) bằng cách [[bình phương hai vế]] rồi thử lại;'),
         ('solve biquadratic equations with a new unknown;', 'giải [[phương trình trùng phương]] bằng cách đặt ẩn phụ;'),
         ('set up and solve such equations in real problems.', 'lập và giải phương trình trong bài toán thực tế.')]
phrases = [('<b>Square both sides.</b>', 'Bình phương hai vế.'), ('<b>Check each root in the original equation.</b>', 'Thử lại từng nghiệm vào phương trình ban đầu.'),
           ('<b>This root is extraneous, so we reject it.</b>', 'Nghiệm này là nghiệm ngoại lai nên bị loại.'), ('<b>Put \\(t\\) equals \\(x\\) squared, with \\(t\\) not negative.</b>', 'Đặt \\(t=x^2\\), \\(t\\ge0\\).'), ('<b>The solution set is three.</b>', 'Tập nghiệm là \\(\\{3\\}\\).')]
review = T('From Bài 17 and Grade 9: solving \\(ax^2+bx+c=0\\) with \\(\\Delta\\); \\(\\sqrt{A}\\) is defined when \\(A\\ge0\\) and \\(\\sqrt A\\ge0\\); \\(\\sqrt A=B\\iff B\\ge0\\) and \\(A=B^2\\).',
           'Từ Bài 17 và lớp 9: giải \\(ax^2+bx+c=0\\) bằng \\(\\Delta\\); \\(\\sqrt{A}\\) có nghĩa khi \\(A\\ge0\\) và \\(\\sqrt A\\ge0\\); \\(\\sqrt A=B\\iff B\\ge0\\) và \\(A=B^2\\).')
theory = '<h3>18.1 %s</h3>' % TI('Equations of the form \\(\\sqrt{ax^2+bx+c}=\\sqrt{dx^2+ex+f}\\)', 'Phương trình dạng \\(\\sqrt{ax^2+bx+c}=\\sqrt{dx^2+ex+f}\\)')
theory += BOX('blue', ('Method', 'Cách giải'), UL([T('Square both sides: \\(ax^2+bx+c=dx^2+ex+f\\) and solve this quadratic (or linear) equation.', 'Bình phương hai vế: \\(ax^2+bx+c=dx^2+ex+f\\), giải phương trình bậc hai (hoặc bậc nhất) nhận được.'),
  T('Substitute each root into the original equation (it is enough to check that one radicand is \\(\\ge0\\)); keep the roots that satisfy it.', 'Thay từng nghiệm vào phương trình ban đầu (chỉ cần kiểm tra một biểu thức dưới căn \\(\\ge0\\)); giữ lại nghiệm thỏa mãn.')]))
theory += '<h3>18.2 %s</h3>' % TI('Equations of the form \\(\\sqrt{ax^2+bx+c}=dx+e\\)', 'Phương trình dạng \\(\\sqrt{ax^2+bx+c}=dx+e\\)')
theory += BOX('blue', ('Method', 'Cách giải'), UL([T('Square both sides: \\(ax^2+bx+c=(dx+e)^2\\); solve.', 'Bình phương hai vế: \\(ax^2+bx+c=(dx+e)^2\\); giải phương trình.'),
  T('Keep only the roots with \\(dx+e\\ge0\\) (the left side is never negative). Equivalently: \\(\\sqrt{A}=B\\iff\\begin{cases}B\\ge0\\\\A=B^2\\end{cases}\\).', 'Chỉ giữ các nghiệm thỏa \\(dx+e\\ge0\\) (vế trái không âm). Tương đương: \\(\\sqrt{A}=B\\iff\\begin{cases}B\\ge0\\\\A=B^2\\end{cases}\\).')]))
theory += '<h3>18.3 %s</h3>' % TI('Using a new unknown', 'Đặt ẩn phụ')
theory += BOX('mint', ('Biquadratic equations', 'Phương trình trùng phương'), T('\\(ax^4+bx^2+c=0\\): put \\(t=x^2\\ (t\\ge0)\\), solve \\(at^2+bt+c=0\\), keep \\(t\\ge0\\), then \\(x=\\pm\\sqrt t\\). Each \\(t\\gt0\\) gives two roots, \\(t=0\\) gives one.', '\\(ax^4+bx^2+c=0\\): đặt \\(t=x^2\\ (t\\ge0)\\), giải \\(at^2+bt+c=0\\), giữ \\(t\\ge0\\), rồi \\(x=\\pm\\sqrt t\\). Mỗi \\(t\\gt0\\) cho hai nghiệm, \\(t=0\\) cho một nghiệm.'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('Squaring is <b>not</b> an equivalent transformation: \\(x=-1\\) does not satisfy \\(\\sqrt{x+2}=x\\) although \\(x+2=x^2\\) at \\(x=-1\\). Always check. Do not write "\\(\\sqrt{x^2}=x\\)": \\(\\sqrt{x^2}=|x|\\).', 'Bình phương <b>không</b> phải phép biến đổi tương đương: \\(x=-1\\) thỏa \\(x+2=x^2\\) nhưng không thỏa \\(\\sqrt{x+2}=x\\). Luôn thử lại. Không viết "\\(\\sqrt{x^2}=x\\)": \\(\\sqrt{x^2}=|x|\\).'))

g = lambda x: x * x - x - 2; assert g(3) == 4 and g(0) == -2 and 2 * 9 - 12 - 2 == g(3)
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Two square roots', 'Hai căn bằng nhau'), T('Solve \\(\\sqrt{2x^2-4x-2}=\\sqrt{x^2-x-2}\\).', 'Giải phương trình \\(\\sqrt{2x^2-4x-2}=\\sqrt{x^2-x-2}\\).'), T('Square, then check \\(x^2-x-2\\ge0\\).', 'Bình phương rồi kiểm tra \\(x^2-x-2\\ge0\\).'),
  [T('\\(2x^2-4x-2=x^2-x-2\\iff x^2-3x=0\\iff x=0\\) or \\(x=3\\).', '\\(2x^2-4x-2=x^2-x-2\\iff x^2-3x=0\\iff x=0\\) hoặc \\(x=3\\).'), T('\\(x=0\\): \\(x^2-x-2=-2\\lt0\\) – rejected. \\(x=3\\): \\(9-3-2=4\\ge0\\) – accepted.', '\\(x=0\\): \\(x^2-x-2=-2\\lt0\\) – loại. \\(x=3\\): \\(9-3-2=4\\ge0\\) – nhận.')],
  T('\\(S=\\{3\\}\\).', '\\(S=\\{3\\}\\).'))
assert (2 + 7) == (2 + 1) ** 2 and -3 + 7 == 4 and -3 + 1 < 0
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Root equals a linear expression', 'Căn bằng biểu thức bậc nhất'), T('Solve \\(\\sqrt{x+7}=x+1\\).', 'Giải phương trình \\(\\sqrt{x+7}=x+1\\).'), T('Condition \\(x+1\\ge0\\), then square.', 'Điều kiện \\(x+1\\ge0\\), rồi bình phương.'),
  [T('\\(x+7=x^2+2x+1\\iff x^2+x-6=0\\iff x=2\\) or \\(x=-3\\).', '\\(x+7=x^2+2x+1\\iff x^2+x-6=0\\iff x=2\\) hoặc \\(x=-3\\).'), T('\\(x=-3\\): \\(x+1=-2\\lt0\\) – extraneous. \\(x=2\\): \\(\\sqrt9=3=2+1\\) ✓.', '\\(x=-3\\): \\(x+1=-2\\lt0\\) – nghiệm ngoại lai. \\(x=2\\): \\(\\sqrt9=3=2+1\\) ✓.')],
  T('\\(S=\\{2\\}\\).', '\\(S=\\{2\\}\\).'))
assert all(math.isqrt(2 * x * x - x + 3) == x + 1 and (x + 1) ** 2 == 2 * x * x - x + 3 for x in (1, 2))
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Both roots can be valid', 'Có thể nhận cả hai nghiệm'), T('Solve \\(\\sqrt{2x^2-x+3}=x+1\\).', 'Giải phương trình \\(\\sqrt{2x^2-x+3}=x+1\\).'), T('\\(\\sqrt A=B\\iff B\\ge0,\\ A=B^2\\).', '\\(\\sqrt A=B\\iff B\\ge0,\\ A=B^2\\).'),
  [T('\\(2x^2-x+3=x^2+2x+1\\iff x^2-3x+2=0\\iff x=1\\) or \\(x=2\\).', '\\(2x^2-x+3=x^2+2x+1\\iff x^2-3x+2=0\\iff x=1\\) hoặc \\(x=2\\).'), T('Both satisfy \\(x+1\\ge0\\): \\(\\sqrt4=2\\), \\(\\sqrt9=3\\) ✓.', 'Cả hai thỏa \\(x+1\\ge0\\): \\(\\sqrt4=2\\), \\(\\sqrt9=3\\) ✓.')],
  T('\\(S=\\{1;2\\}\\).', '\\(S=\\{1;2\\}\\).'))
assert all(x ** 4 - 13 * x * x + 36 == 0 for x in (2, -2, 3, -3))
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('A biquadratic equation', 'Phương trình trùng phương'), T('Solve \\(x^4-13x^2+36=0\\).', 'Giải phương trình \\(x^4-13x^2+36=0\\).'), T('Put \\(t=x^2\\ge0\\).', 'Đặt \\(t=x^2\\ge0\\).'),
  [T('\\(t^2-13t+36=0\\iff t=4\\) or \\(t=9\\) (both \\(\\ge0\\)).', '\\(t^2-13t+36=0\\iff t=4\\) hoặc \\(t=9\\) (đều \\(\\ge0\\)).'), T('\\(x^2=4\\iff x=\\pm2\\); \\(x^2=9\\iff x=\\pm3\\).', '\\(x^2=4\\iff x=\\pm2\\); \\(x^2=9\\iff x=\\pm3\\).')],
  T('\\(S=\\{-3;-2;2;3\\}\\).', '\\(S=\\{-3;-2;2;3\\}\\).'))
assert math.isqrt(64 + 36) == 2 * 8 - 6 == 10
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('A guy rope', 'Dây néo cột'), T('A 6 m pole stands vertically. A rope goes from its top to a point on the ground \\(x\\) m from its foot. The rope is 6 m shorter than twice that distance. Find \\(x\\) and the rope length.', 'Một cột cao 6 m dựng thẳng đứng. Sợi dây nối đỉnh cột với một điểm trên mặt đất cách chân cột \\(x\\) m. Độ dài dây ngắn hơn hai lần khoảng cách đó 6 m. Tìm \\(x\\) và độ dài dây.'),
  T('Pythagoras: rope \\(=\\sqrt{x^2+36}\\).', 'Định lí Pythagore: độ dài dây \\(=\\sqrt{x^2+36}\\).'),
  [T('\\(\\sqrt{x^2+36}=2x-6\\) (need \\(x\\ge3\\)).', '\\(\\sqrt{x^2+36}=2x-6\\) (cần \\(x\\ge3\\)).'), T('\\(x^2+36=4x^2-24x+36\\iff3x^2-24x=0\\iff x=0\\) or \\(x=8\\).', '\\(x^2+36=4x^2-24x+36\\iff3x^2-24x=0\\iff x=0\\) hoặc \\(x=8\\).'), T('\\(x=0\\lt3\\) is rejected; \\(x=8\\): rope \\(=\\sqrt{100}=10\\) m.', '\\(x=0\\lt3\\) bị loại; \\(x=8\\): dây dài \\(\\sqrt{100}=10\\) m.')],
  T('\\(x=8\\) m, the rope is 10 m long.', '\\(x=8\\) m, dây dài 10 m.'))

def lvl(P):
    c, r1, r2 = P['t2']; a, b = r1 + r2 - 2 * c, c * c - r1 * r2; L = S.lhs(a, b); R = S.rhs(c)
    o1 = M4(1, 'Solve \\(%s=%s\\).' % (L, R), 'Giải phương trình \\(%s=%s\\).' % (L, R), '\\(S=\\{%d\\}\\)' % r1, ['\\(S=\\{%d;\\,%d\\}\\)' % (min(r1, r2), max(r1, r2)), '\\(S=\\{%d\\}\\)' % r2, '\\(S=\\varnothing\\)'],
            'Need \\(x\\ge%d\\); squaring gives %d and %d.' % (c, r1, r2), 'Cần \\(x\\ge%d\\); bình phương được %d và %d, loại %d.' % (c, r1, r2, r2))
    (p, q), (m, n) = P['t1']; good = [x for x in (p, q) if m * x + n >= 0]; bb = -(p + q) + m; cc = p * q + n
    ok = '\\(S=\\{%s\\}\\)' % ';\\,'.join(map(str, good)) if good else '\\(S=\\varnothing\\)'
    o2 = M4(2, 'Solve \\(\\sqrt{%s}=\\sqrt{%s}\\).' % (poly([1, bb, cc]), poly([m, n])), 'Giải phương trình \\(\\sqrt{%s}=\\sqrt{%s}\\).' % (poly([1, bb, cc]), poly([m, n])), ok,
            ['\\(S=\\{%d;\\,%d\\}\\)' % (p, q), '\\(S=\\{%d\\}\\)' % p, '\\(S=\\{%d\\}\\)' % q, '\\(S=\\varnothing\\)'],
            'Squaring: roots %d, %d; check \\(%s\\ge0\\).' % (p, q, poly([m, n])), 'Bình phương: nghiệm %d, %d; kiểm tra \\(%s\\ge0\\).' % (p, q, poly([m, n])))
    u, v = P['bi']; nb = sum(1 if t == 0 else 2 if t > 0 else 0 for t in (u, v))
    o3 = M4(3, 'How many real roots does \\(%s=0\\) have?' % poly([1, 0, -(u + v), 0, u * v]), 'Phương trình \\(%s=0\\) có bao nhiêu nghiệm thực?' % poly([1, 0, -(u + v), 0, u * v]), str(nb), [str(k) for k in range(5) if k != nb],
            '\\(t=x^2\\): \\(t=%d\\) or \\(t=%d\\).' % (u, v), '\\(t=x^2\\): \\(t=%d\\) hoặc \\(t=%d\\).' % (u, v))
    c4, s4, x4 = P['ext']; a4, b4 = s4[0] + s4[1] - 2 * c4, c4 * c4 - s4[0] * s4[1]; truth4 = x4 < c4
    t4 = tf(4, '\\(x=%d\\) is an extraneous root of \\(%s=%s\\) (after squaring we get \\(x=%d\\), \\(x=%d\\)).' % (x4, S.lhs(a4, b4), S.rhs(c4), s4[0], s4[1]), '\\(x=%d\\) là nghiệm ngoại lai của phương trình \\(%s=%s\\) (sau khi bình phương được \\(x=%d\\), \\(x=%d\\)).' % (x4, S.lhs(a4, b4), S.rhs(c4), s4[0], s4[1]), truth4,
            'At \\(x=%d\\) the right side is \\(%d\\).' % (x4, x4 - c4), 'Tại \\(x=%d\\) vế phải bằng \\(%d\\).' % (x4, x4 - c4))
    x5, k5, e5 = P['tf5']; val = k5 * x5 * x5 + e5; truth5 = val >= 0 and math.isqrt(val) ** 2 == val and math.isqrt(val) == x5 - 1
    t5 = tf(5, '\\(x=%d\\) satisfies \\(\\sqrt{%s}=x-1\\).' % (x5, poly([k5, 0, e5])), '\\(x=%d\\) là nghiệm của phương trình \\(\\sqrt{%s}=x-1\\).' % (x5, poly([k5, 0, e5])), truth5,
            'Left side \\(\\sqrt{%d}\\), right side \\(%d\\).' % (val, x5 - 1), 'Vế trái \\(\\sqrt{%d}\\), vế phải \\(%d\\).' % (val, x5 - 1))
    c6, r61, r62 = P['sum']; a6, b6 = r61 + r62 - 2 * c6, c6 * c6 - r61 * r62
    s6 = sh(6, 'Find the sum of all solutions of \\(%s=%s\\).' % (S.lhs(a6, b6), S.rhs(c6)), 'Tính tổng các nghiệm của phương trình \\(%s=%s\\).' % (S.lhs(a6, b6), S.rhs(c6)), sum(x for x in (r61, r62) if x >= c6),
            'Valid roots: %s.' % ', '.join(str(x) for x in (r61, r62) if x >= c6), 'Nghiệm thỏa mãn: %s.' % ', '.join(str(x) for x in (r61, r62) if x >= c6))
    h = P['rope']; x7 = 4 * h // 3; assert x7 * x7 + h * h == (2 * x7 - h) ** 2
    s7 = sh(7, 'A \\(%d\\) m pole; a rope from its top to the ground, \\(x\\) m from the foot, is \\(%d\\) m shorter than \\(2x\\). Find \\(x\\) (m).' % (h, h), 'Cột cao \\(%d\\) m; dây nối đỉnh cột với điểm trên mặt đất cách chân cột \\(x\\) m, ngắn hơn \\(2x\\) là \\(%d\\) m. Tìm \\(x\\) (m).' % (h, h), x7,
            '\\(\\sqrt{x^2+%d}=2x-%d\\Rightarrow3x^2-%dx=0\\), \\(x=%d\\) (reject 0).' % (h * h, h, 4 * h, x7), '\\(\\sqrt{x^2+%d}=2x-%d\\Rightarrow3x^2-%dx=0\\), \\(x=%d\\) (loại \\(x=0\\)).' % (h * h, h, 4 * h, x7))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
PP = [dict(t2=(1, 3, -2), t1=((1, 4), (1, -2)), bi=(1, 9), ext=(0, (2, -3), -3), tf5=(3, 1, -5), sum=(0, 4, -1), rope=6),
      dict(t2=(-1, 2, -5), t1=((-3, 2), (2, 1)), bi=(0, 4), ext=(2, (5, 1), 5), tf5=(4, 2, -23), sum=(-2, 3, 1), rope=9),
      dict(t2=(2, 6, -1), t1=((-2, 5), (-1, 3)), bi=(-4, 16), ext=(-1, (3, -4), -4), tf5=(5, 1, 7), sum=(1, 5, 2), rope=3)]
practice = three(lvl, PP)
practice = with_self(practice, S.M18S10, start=8)
mistakes = [('<b>Not checking the roots after squaring.</b> Squaring can add extraneous roots.', '<b>Không thử lại sau khi bình phương.</b> Bình phương có thể sinh nghiệm ngoại lai.'),
            ('<b>Squaring \\(x+1\\) wrongly.</b> \\((x+1)^2=x^2+2x+1\\), not \\(x^2+1\\).', '<b>Bình phương sai.</b> \\((x+1)^2=x^2+2x+1\\), không phải \\(x^2+1\\).'),
            ('<b>Keeping \\(t\\lt0\\) in a biquadratic equation.</b> \\(t=x^2\\) cannot be negative.', '<b>Giữ \\(t\\lt0\\) trong phương trình trùng phương.</b> \\(t=x^2\\) không thể âm.'),
            ('<b>Forgetting the real-life condition.</b> A length must be positive and satisfy the conditions of the problem.', '<b>Quên điều kiện thực tế.</b> Độ dài phải dương và thỏa điều kiện của bài toán.')]
summary = [('\\(\\sqrt{f}=\\sqrt{g}\\): square, solve \\(f=g\\), keep roots with \\(f\\ge0\\) (or \\(g\\ge0\\)).', '\\(\\sqrt{f}=\\sqrt{g}\\): bình phương, giải \\(f=g\\), giữ nghiệm có \\(f\\ge0\\) (hoặc \\(g\\ge0\\)).'),
           ('\\(\\sqrt{f}=g\\iff g\\ge0\\) and \\(f=g^2\\).', '\\(\\sqrt{f}=g\\iff g\\ge0\\) và \\(f=g^2\\).'),
           ('\\(ax^4+bx^2+c=0\\): \\(t=x^2\\ge0\\).', '\\(ax^4+bx^2+c=0\\): đặt \\(t=x^2\\ge0\\).'),
           ('Key words: square root, square both sides, extraneous root, biquadratic.', 'Từ cần nhớ: square root, square both sides, extraneous root, biquadratic.')]
checks = [('I can solve \\(\\sqrt{f(x)}=\\sqrt{g(x)}\\).', 'Em giải được phương trình \\(\\sqrt{f(x)}=\\sqrt{g(x)}\\).'), ('I can solve \\(\\sqrt{f(x)}=g(x)\\) and reject extraneous roots.', 'Em giải được \\(\\sqrt{f(x)}=g(x)\\) và loại được nghiệm ngoại lai.'),
          ('I can solve a biquadratic equation.', 'Em giải được phương trình trùng phương.'), ('I can set up an equation from a real problem.', 'Em lập được phương trình từ bài toán thực tế.')]
LL('g10-func-04', 'Equations Reducible to Quadratics', CV, ('Functions and Graphs', 'Hàm số, đồ thị và ứng dụng'), 'functions', 'equations-to-quadratic', 180, 'Intermediate', 65, ('quadratic equations, square roots', 'phương trình bậc hai, căn bậc hai'),
   'Equations with square roots solved by squaring and checking; biquadratic equations; real problems.', 'Bài 18 – Phương trình chứa căn \\(\\sqrt{f}=\\sqrt{g}\\), \\(\\sqrt f=g\\), phương trình trùng phương và bài toán thực tế.',
   ['square root equation', 'extraneous root', 'biquadratic', 'squaring'], ['phương trình chứa căn', 'nghiệm ngoại lai', 'trùng phương', 'bình phương hai vế'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g10-func-03'])
