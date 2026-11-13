# -*- coding: utf-8 -*-
"""g11-limits-03 = Toán 11 KNTT, Bài 15: Giới hạn của dãy số. Mã ngân hàng câu hỏi: TOAN11-C5-B15."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g11e as S
from sp_g11e import LN, poly, D

CV = 'Giới hạn của dãy số'
vocab = defs(CV, [
 ('slim', 'limit of a sequence', 'giới hạn của dãy số', 'the number \\(a\\) that \\(u_n\\) gets as close to as we like when \\(n\\) is large enough: \\(\\lim u_n=a\\).', 'số \\(a\\) mà \\(u_n\\) gần \\(a\\) bao nhiêu cũng được khi \\(n\\) đủ lớn: \\(\\lim u_n=a\\).', 'The limit of \\(\\frac1n\\) is 0.', '\\(\\lim u_n\\)'),
 ('conv', 'converge', 'hội tụ (có giới hạn hữu hạn)', 'to have a finite limit.', 'có giới hạn là một số thực.', 'The sequence converges to 2.', ''),
 ('infgeo', 'infinite geometric series (with \\(|q|\\lt1\\))', 'cấp số nhân lùi vô hạn', 'a geometric progression with \\(|q|\\lt1\\); its sum is \\(S=\\dfrac{u_1}{1-q}\\).', 'cấp số nhân có công bội \\(|q|\\lt1\\); tổng của nó là \\(S=\\dfrac{u_1}{1-q}\\).', 'Find the sum of the infinite geometric series.', '\\(S\\)'),
 ('infl', 'infinite limit', 'giới hạn vô cực', '\\(\\lim u_n=+\\infty\\): \\(u_n\\) becomes larger than any number when \\(n\\) is large.', '\\(\\lim u_n=+\\infty\\): \\(u_n\\) lớn hơn mọi số dương cho trước khi \\(n\\) đủ lớn.', '\\(\\lim n^2=+\\infty\\).', '\\(\\pm\\infty\\)'),
 ('rdec', 'repeating decimal', 'số thập phân vô hạn tuần hoàn', 'a decimal whose digits repeat forever, like \\(0.(3)=0.333\\dots\\).', 'số thập phân có nhóm chữ số lặp lại mãi, như \\(0{,}(3)=0{,}333\\dots\\).', 'Write the repeating decimal as a fraction.', ''),
 ('conjug', 'conjugate (multiply by)', 'nhân liên hợp', 'multiply by \\(\\sqrt A+B\\) to remove a square root in \\(\\sqrt A-B\\).', 'nhân với \\(\\sqrt A+B\\) để khử căn trong \\(\\sqrt A-B\\).', 'Multiply by the conjugate.', '')])
goals = [('understand the limit of a sequence and the basic limits;', 'hiểu khái niệm [[giới hạn của dãy số]] và các giới hạn cơ bản;'),
         ('use the limit theorems to find limits of quotients, powers and roots;', 'dùng các định lí về giới hạn để tính giới hạn của thương, lũy thừa, căn thức;'),
         ('find the sum of an infinite geometric series and write a repeating decimal as a fraction;', 'tính tổng [[cấp số nhân lùi vô hạn]] và viết [[số thập phân vô hạn tuần hoàn]] thành phân số;'),
         ('recognise infinite limits.', 'nhận biết [[giới hạn vô cực]].')]
phrases = [('<b>Find the limit of the sequence.</b>', 'Tìm giới hạn của dãy số.'), ('<b>Divide the numerator and the denominator by \\(n^2\\).</b>', 'Chia cả tử và mẫu cho \\(n^2\\).'), ('<b>The sequence tends to zero.</b>', 'Dãy số dần tới 0.'),
           ('<b>Find the sum of the infinite geometric series.</b>', 'Tính tổng của cấp số nhân lùi vô hạn.'), ('<b>The limit is plus infinity.</b>', 'Giới hạn bằng dương vô cực.')]
review = T('From Lessons 5–7: a sequence \\((u_n)\\); a geometric progression \\(u_n=u_1q^{n-1}\\) has \\(S_n=u_1\\dfrac{1-q^n}{1-q}\\) (\\(q\\ne1\\)). Also \\(\\left|q^n\\right|=|q|^n\\) becomes very small when \\(|q|\\lt1\\).', 'Từ Bài 5–7: dãy số \\((u_n)\\); cấp số nhân \\(u_n=u_1q^{n-1}\\) có \\(S_n=u_1\\dfrac{1-q^n}{1-q}\\) (\\(q\\ne1\\)). Khi \\(|q|\\lt1\\) thì \\(|q^n|=|q|^n\\) rất nhỏ khi \\(n\\) lớn.')
pts = [{'x': n, 'y': round(1 + (-1) ** n / n, 4)} for n in range(1, 13)]
theory = '<h3>15.1 %s</h3>' % TI('Finite limits', 'Giới hạn hữu hạn của dãy số')
theory += BOX('blue', ('Definition', 'Định nghĩa'), UL([T('\\(\\lim u_n=0\\) if \\(|u_n|\\) can be made smaller than any positive number, for all \\(n\\) large enough.', '\\(\\lim\\limits_{n\\to+\\infty}u_n=0\\) nếu \\(|u_n|\\) có thể nhỏ hơn một số dương bé tùy ý, kể từ một số hạng nào đó trở đi.'),
  T('\\(\\lim u_n=a\\iff\\lim(u_n-a)=0\\).', '\\(\\lim\\limits_{n\\to+\\infty}u_n=a\\iff\\lim\\limits_{n\\to+\\infty}(u_n-a)=0\\).')]))
theory += GRAPH({'view': [0, 13, -0.2, 2.4], 'functions': [{'f': '1', 'label': 'y = 1', 'dash': 2}], 'points': pts},
  cap=('\\(u_n=1+\\frac{(-1)^n}{n}\\): the points jump above and below 1 but get closer and closer to the line \\(y=1\\), so \\(\\lim u_n=1\\).', '\\(u_n=1+\\frac{(-1)^n}{n}\\): các điểm lúc ở trên, lúc ở dưới đường \\(y=1\\) nhưng ngày càng gần nó, nên \\(\\lim u_n=1\\).'), alt=('Points of a sequence approaching the line y = 1', ''), height=280)
theory += BOX('mint', ('Basic limits', 'Các giới hạn cơ bản'), M('\\lim\\dfrac{1}{n^k}=0\\ (k\\in\\mathbb N^*),\\qquad \\lim q^n=0\\ (|q|\\lt1),\\qquad \\lim c=c'))
theory += BOX('blue', ('Theorem', 'Định lí'), T('If \\(\\lim u_n=a\\), \\(\\lim v_n=b\\) then \\(\\lim(u_n\\pm v_n)=a\\pm b\\), \\(\\lim u_nv_n=ab\\), \\(\\lim\\dfrac{u_n}{v_n}=\\dfrac ab\\) (\\(b\\ne0\\)); if \\(u_n\\ge0\\) then \\(a\\ge0\\) and \\(\\lim\\sqrt{u_n}=\\sqrt a\\).', 'Nếu \\(\\lim u_n=a\\), \\(\\lim v_n=b\\) thì \\(\\lim(u_n\\pm v_n)=a\\pm b\\), \\(\\lim u_nv_n=ab\\), \\(\\lim\\dfrac{u_n}{v_n}=\\dfrac ab\\) (\\(b\\ne0\\)); nếu \\(u_n\\ge0\\) thì \\(a\\ge0\\) và \\(\\lim\\sqrt{u_n}=\\sqrt a\\).'))
theory += '<h3>15.2 %s</h3>' % TI('Sum of an infinite geometric series', 'Tổng của cấp số nhân lùi vô hạn')
theory += BOX('mint', ('Formula', 'Công thức'), M('S=u_1+u_1q+u_1q^2+\\dots=\\dfrac{u_1}{1-q}\\qquad(|q|\\lt1)'), T('Because \\(S_n=u_1\\dfrac{1-q^n}{1-q}\\) and \\(q^n\\to0\\).', 'Vì \\(S_n=u_1\\dfrac{1-q^n}{1-q}\\) và \\(q^n\\to0\\).'))
theory += '<h3>15.3 %s</h3>' % TI('Infinite limits', 'Giới hạn vô cực')
theory += BOX('blue', ('Rules', 'Quy tắc'), UL([T('\\(\\lim n^k=+\\infty\\) (\\(k\\in\\mathbb N^*\\)); \\(\\lim q^n=+\\infty\\) (\\(q\\gt1\\)).', '\\(\\lim n^k=+\\infty\\) (\\(k\\in\\mathbb N^*\\)); \\(\\lim q^n=+\\infty\\) (\\(q\\gt1\\)).'),
  T('If \\(\\lim u_n=a\\) and \\(\\lim v_n=\\pm\\infty\\) then \\(\\lim\\dfrac{u_n}{v_n}=0\\).', 'Nếu \\(\\lim u_n=a\\) và \\(\\lim v_n=\\pm\\infty\\) thì \\(\\lim\\dfrac{u_n}{v_n}=0\\).'),
  T('If \\(\\lim u_n=a\\gt0\\), \\(\\lim v_n=0\\) and \\(v_n\\gt0\\), then \\(\\lim\\dfrac{u_n}{v_n}=+\\infty\\). If \\(\\lim u_n=+\\infty\\) and \\(\\lim v_n=a\\gt0\\), then \\(\\lim u_nv_n=+\\infty\\) (change signs as needed).', 'Nếu \\(\\lim u_n=a\\gt0\\), \\(\\lim v_n=0\\) và \\(v_n\\gt0\\) thì \\(\\lim\\dfrac{u_n}{v_n}=+\\infty\\). Nếu \\(\\lim u_n=+\\infty\\), \\(\\lim v_n=a\\gt0\\) thì \\(\\lim u_nv_n=+\\infty\\) (đổi dấu tương ứng).')]))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('\\(\\infty-\\infty\\), \\(\\dfrac{\\infty}{\\infty}\\), \\(\\dfrac00\\), \\(0\\cdot\\infty\\) are not numbers: transform first (divide by the highest power, multiply by the conjugate). For a rational expression: same degree → ratio of leading coefficients; numerator of lower degree → 0; higher degree → \\(\\pm\\infty\\).', '\\(\\infty-\\infty\\), \\(\\dfrac{\\infty}{\\infty}\\), \\(\\dfrac00\\), \\(0\\cdot\\infty\\) không phải là số: phải biến đổi trước (chia cho lũy thừa cao nhất, nhân liên hợp). Với phân thức: cùng bậc → tỉ số hệ số bậc cao nhất; tử bậc thấp hơn → 0; tử bậc cao hơn → \\(\\pm\\infty\\).'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Basic limits', 'Giới hạn cơ bản'), T('Find \\(%s\\left(3+\\dfrac{2}{n^2}\\right)\\), \\(%s\\left(\\dfrac23\\right)^n\\) and \\(%s\\dfrac{(-1)^n}{n}\\).' % (LN, LN, LN), 'Tính \\(%s\\left(3+\\dfrac{2}{n^2}\\right)\\), \\(%s\\left(\\dfrac23\\right)^n\\) và \\(%s\\dfrac{(-1)^n}{n}\\).' % (LN, LN, LN)),
  T('Use the basic limits.', 'Dùng các giới hạn cơ bản.'), [T('\\(\\lim3=3\\), \\(\\lim\\dfrac{2}{n^2}=0\\), so the first limit is 3.', '\\(\\lim3=3\\), \\(\\lim\\dfrac{2}{n^2}=0\\) nên giới hạn thứ nhất bằng 3.'), T('\\(\\left|\\frac23\\right|\\lt1\\): the second limit is 0.', '\\(\\left|\\frac23\\right|\\lt1\\): giới hạn thứ hai bằng 0.'), T('\\(\\left|\\dfrac{(-1)^n}{n}\\right|=\\dfrac1n\\to0\\): the third limit is 0.', '\\(\\left|\\dfrac{(-1)^n}{n}\\right|=\\dfrac1n\\to0\\): giới hạn thứ ba bằng 0.')],
  T('\\(3\\); \\(0\\); \\(0\\).', '\\(3\\); \\(0\\); \\(0\\).'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('A rational expression', 'Phân thức theo \\(n\\)'), T('Find \\(%s\\dfrac{2n^2-3n+1}{5n^2+4}\\).' % LN, 'Tính \\(%s\\dfrac{2n^2-3n+1}{5n^2+4}\\).' % LN), T('Divide by \\(n^2\\).', 'Chia tử và mẫu cho \\(n^2\\).'),
  [T('\\(\\dfrac{2-\\frac3n+\\frac1{n^2}}{5+\\frac4{n^2}}\\to\\dfrac{2-0+0}{5+0}\\).', '\\(\\dfrac{2-\\frac3n+\\frac1{n^2}}{5+\\frac4{n^2}}\\to\\dfrac{2-0+0}{5+0}\\).')], T('\\(\\dfrac25\\).', '\\(\\dfrac25\\).'))
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Powers and roots', 'Lũy thừa và căn thức'), T('Find (a) \\(%s\\dfrac{3^n-2^{n+1}}{3^{n+1}+1}\\); (b) \\(%s\\left(\\sqrt{n^2+4n}-n\\right)\\).' % (LN, LN), 'Tính (a) \\(%s\\dfrac{3^n-2^{n+1}}{3^{n+1}+1}\\); (b) \\(%s\\left(\\sqrt{n^2+4n}-n\\right)\\).' % (LN, LN)),
  T('(a) divide by \\(3^n\\); (b) multiply by the conjugate.', '(a) chia cho \\(3^n\\); (b) nhân liên hợp.'),
  [T('(a) \\(\\dfrac{1-2\\left(\\frac23\\right)^n}{3+\\left(\\frac13\\right)^n}\\to\\dfrac13\\).', '(a) \\(\\dfrac{1-2\\left(\\frac23\\right)^n}{3+\\left(\\frac13\\right)^n}\\to\\dfrac13\\).'), T('(b) \\(\\dfrac{4n}{\\sqrt{n^2+4n}+n}=\\dfrac{4}{\\sqrt{1+\\frac4n}+1}\\to\\dfrac42=2\\).', '(b) \\(\\dfrac{4n}{\\sqrt{n^2+4n}+n}=\\dfrac{4}{\\sqrt{1+\\frac4n}+1}\\to\\dfrac42=2\\).')],
  T('(a) \\(\\dfrac13\\); (b) \\(2\\). Note: in (b), \\(\\infty-\\infty\\) is not 0.', '(a) \\(\\dfrac13\\); (b) \\(2\\). Chú ý: ở (b), \\(\\infty-\\infty\\) không bằng 0.'))
assert F(27, 99) == F(3, 11)
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Series and decimals', 'Tổng vô hạn và số thập phân'), T('(a) Find \\(1-\\dfrac12+\\dfrac14-\\dfrac18+\\dots\\). (b) Write \\(0.(27)=0.2727\\dots\\) as a fraction.', '(a) Tính \\(1-\\dfrac12+\\dfrac14-\\dfrac18+\\dots\\). (b) Viết \\(0{,}(27)=0{,}2727\\dots\\) dưới dạng phân số.'),
  T('Both are infinite geometric series.', 'Cả hai đều là cấp số nhân lùi vô hạn.'),
  [T('(a) \\(u_1=1\\), \\(q=-\\dfrac12\\): \\(S=\\dfrac{1}{1+\\frac12}=\\dfrac23\\).', '(a) \\(u_1=1\\), \\(q=-\\dfrac12\\): \\(S=\\dfrac{1}{1+\\frac12}=\\dfrac23\\).'), T('(b) \\(0.(27)=\\dfrac{27}{100}+\\dfrac{27}{100^2}+\\dots=\\dfrac{\\frac{27}{100}}{1-\\frac1{100}}=\\dfrac{27}{99}\\).', '(b) \\(0{,}(27)=\\dfrac{27}{100}+\\dfrac{27}{100^2}+\\dots=\\dfrac{\\frac{27}{100}}{1-\\frac1{100}}=\\dfrac{27}{99}\\).')],
  T('(a) \\(\\dfrac23\\); (b) \\(\\dfrac{3}{11}\\).', '(a) \\(\\dfrac23\\); (b) \\(\\dfrac{3}{11}\\).'))
T5 = 2 + 2 * 2 * F(3, 4) / (1 - F(3, 4)); assert T5 == 14
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('A bouncing ball', 'Quả bóng nảy'), T('A ball is dropped from 2 m. After each bounce it rises to \\(\\frac34\\) of the previous height. Find the total distance travelled (assume it bounces forever, with smaller and smaller heights).', 'Thả quả bóng từ độ cao 2 m. Sau mỗi lần chạm đất, bóng nảy lên bằng \\(\\frac34\\) độ cao trước đó. Tính tổng quãng đường bóng đi được (giả sử bóng nảy mãi với độ cao ngày càng nhỏ).'),
  T('After the first fall, each bounce adds an up and a down of the same length.', 'Sau lần rơi đầu, mỗi lần nảy gồm một đoạn lên và một đoạn xuống bằng nhau.'),
  [T('Heights after bounces: \\(2\\cdot\\frac34, 2\\left(\\frac34\\right)^2,\\dots\\), sum \\(=\\dfrac{\\frac32}{1-\\frac34}=6\\) m.', 'Các độ cao sau mỗi lần nảy: \\(2\\cdot\\frac34, 2\\left(\\frac34\\right)^2,\\dots\\), tổng \\(=\\dfrac{\\frac32}{1-\\frac34}=6\\) m.'), T('Total \\(=2+2\\cdot6\\).', 'Tổng quãng đường \\(=2+2\\cdot6\\).')],
  T('14 m – a finite distance, although the ball bounces infinitely many times.', '14 m – một quãng đường hữu hạn dù bóng nảy vô số lần.'))

def lvl(P):
    nu, de = P['rat']; v = F(nu[0], de[0]) if len(nu) == len(de) else F(0)
    o1 = M4(1, '\\(%s\\dfrac{%s}{%s}=\\)…' % (LN, poly(nu), poly(de)), '\\(%s\\dfrac{%s}{%s}=\\)…' % (LN, poly(nu), poly(de)), fr(v), [fr(F(nu[-1], de[-1])), '+\\infty', fr(F(nu[0], de[0])) if v == 0 else '0', fr(v + 1)],
            'Divide by the highest power of \\(n\\) in the denominator.', 'Chia tử và mẫu cho lũy thừa bậc cao nhất của \\(n\\) ở mẫu.')
    u1, q = P['geo']; Sg = u1 / (1 - q)
    o2 = M4(2, 'A square of area \\(%s\\ \\text{cm}^2\\) is painted; then a square of \\(%s\\) of that area, then \\(%s\\) of the previous one, and so on forever. The total painted area is…' % (fr(u1), fr(q), fr(q)),
            'Tô một hình vuông diện tích \\(%s\\ \\text{cm}^2\\); tiếp theo tô hình vuông có diện tích bằng \\(%s\\) hình trước, rồi \\(%s\\) hình vừa tô, cứ thế mãi. Tổng diện tích được tô là…' % (fr(u1), fr(q), fr(q)),
            fr(Sg) + '\\ \\text{cm}^2', [fr(u1 / (1 + q)) + '\\ \\text{cm}^2', fr(u1 * q / (1 - q)) + '\\ \\text{cm}^2', '+\\infty'], '\\(S=\\dfrac{u_1}{1-q}=\\dfrac{%s}{1-%s}=%s\\).' % (fr(u1), fr(q), fr(Sg)), '\\(S=\\dfrac{u_1}{1-q}=\\dfrac{%s}{1-%s}=%s\\).' % (fr(u1), fr(q), fr(Sg)))
    a = P['sq']; vs = F(a, 2)
    o3 = M4(3, '\\(%s\\left(\\sqrt{n^2+%dn}-n\\right)=\\)…' % (LN, a), '\\(%s\\left(\\sqrt{n^2+%dn}-n\\right)=\\)…' % (LN, a), fr(vs), ['0', str(a), '+\\infty'],
            'Conjugate: \\(\\dfrac{%dn}{\\sqrt{n^2+%dn}+n}\\to\\dfrac{%d}{2}\\).' % (a, a, a), 'Nhân liên hợp: \\(\\dfrac{%dn}{\\sqrt{n^2+%dn}+n}\\to\\dfrac{%d}{2}\\).' % (a, a, a))
    st = [('\\(%s\\left(\\dfrac{5}{4}\\right)^n=0\\).' % LN, False, '\\(\\frac54\\gt1\\), so the limit is \\(+\\infty\\).', '\\(\\frac54\\gt1\\) nên giới hạn là \\(+\\infty\\).'),
          ('\\(%s\\dfrac{n^3+1}{2n^2-n}=+\\infty\\).' % LN, True, 'The numerator has a higher degree and the leading coefficients are positive.', 'Tử có bậc cao hơn và các hệ số bậc cao nhất dương.'),
          ('\\(%s\\left(\\sqrt{n+1}-\\sqrt n\\right)=0\\).' % LN, True, '\\(\\sqrt{n+1}-\\sqrt n=\\dfrac{1}{\\sqrt{n+1}+\\sqrt n}\\to0\\).', '\\(\\sqrt{n+1}-\\sqrt n=\\dfrac{1}{\\sqrt{n+1}+\\sqrt n}\\to0\\).')][P['t4']]
    t4 = tf(4, st[0], st[0], st[1], st[2], st[3])
    p, k, ok = P['dec']; v5 = F(p, 10 ** k - 1); claim = v5 if ok else F(p, 10 ** k); per = str(p).zfill(k)
    t5 = tf(5, '\\(0.(%s)=%s\\).' % (per, fr(claim)), '\\(0{,}(%s)=%s\\).' % (per, fr(claim)), ok, '\\(0.(%s)=\\dfrac{%d}{%d}=%s\\).' % (per, p, 10 ** k - 1, fr(v5)), '\\(0{,}(%s)=\\dfrac{%d}{%d}=%s\\).' % (per, p, 10 ** k - 1, fr(v5)))
    h, q6 = P['ball']; T6 = h + 2 * h * q6 / (1 - q6); assert T6.denominator == 1
    s6 = sh(6, 'A ball is dropped from \\(%d\\) m and each time rises to \\(%s\\) of the previous height. Find the total distance travelled (m).' % (h, fr(q6)), 'Thả quả bóng từ độ cao \\(%d\\) m, mỗi lần nảy lên bằng \\(%s\\) độ cao trước. Tính tổng quãng đường bóng đi được (m).' % (h, fr(q6)), T6.numerator,
            '\\(%d+2\\cdot\\dfrac{%s}{1-%s}=%d\\).' % (h, fr(h * q6), fr(q6), T6), '\\(%d+2\\cdot\\dfrac{%s}{1-%s}=%d\\).' % (h, fr(h * q6), fr(q6), T6))
    (a7, B, c7, d7) = P['exp']; v7 = F(a7, c7); assert v7.denominator == 1
    s7 = sh(7, 'Find \\(%s\\dfrac{%d\\cdot%d^{n+1}+%d}{%d^{n}+%d}\\).' % (LN, a7, B, d7, B, c7),
            'Tính \\(%s\\dfrac{%d\\cdot%d^{n+1}+%d}{%d^{n}+%d}\\).' % (LN, a7, B, d7, B, c7), a7 * B, 'Divide by \\(%d^n\\): \\(\\dfrac{%d\\cdot%d+\\frac{%d}{%d^n}}{1+\\frac{%d}{%d^n}}\\to%d\\).' % (B, a7, B, d7, B, c7, B, a7 * B), 'Chia cho \\(%d^n\\): \\(\\dfrac{%d\\cdot%d+\\frac{%d}{%d^n}}{1+\\frac{%d}{%d^n}}\\to%d\\).' % (B, a7, B, d7, B, c7, B, a7 * B))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
PP = [dict(rat=([3, -1, 2], [6, 0, 5]), geo=(F(16), F(1, 2)), sq=6, t4=0, dec=(5, 1, True), ball=(5, F(1, 2)), exp=(2, 3, 1, 5)),
      dict(rat=([4, 1], [2, -3, 1]), geo=(F(9), F(1, 3)), sq=10, t4=1, dec=(36, 2, False), ball=(3, F(2, 3)), exp=(3, 2, 1, 4)),
      dict(rat=([-5, 2, 0], [10, 1, -7]), geo=(F(25), F(4, 5)), sq=8, t4=2, dec=(12, 2, True), ball=(4, F(3, 5)), exp=(1, 5, 1, 2))]
practice = three(lvl, PP)
import sp_g11r as RR, sp_g11r2 as R2
# Hiệu chỉnh 13/11/2026: phần D cũ lặp lại các dạng của A–C → 8 dạng mới.
practice = RR.with_d(practice, R2.D15, seeds=(1151, 1152, 1153))
mistakes = [('<b>"\\(\\infty-\\infty=0\\)".</b> \\(\\sqrt{n^2+4n}-n\\to2\\): transform before taking the limit.', '<b>"\\(\\infty-\\infty=0\\)".</b> \\(\\sqrt{n^2+4n}-n\\to2\\): phải biến đổi trước khi lấy giới hạn.'),
            ('<b>Dividing by the wrong power.</b> Divide by the highest power of \\(n\\) in the <b>denominator</b>.', '<b>Chia sai lũy thừa.</b> Chia cho lũy thừa bậc cao nhất của \\(n\\) ở <b>mẫu</b>.'),
            ('<b>Using \\(S=\\dfrac{u_1}{1-q}\\) when \\(|q|\\ge1\\).</b> The formula needs \\(|q|\\lt1\\).', '<b>Dùng \\(S=\\dfrac{u_1}{1-q}\\) khi \\(|q|\\ge1\\).</b> Công thức chỉ đúng khi \\(|q|\\lt1\\).'),
            ('<b>\\(0.(36)=\\dfrac{36}{100}\\).</b> Repeating digits give \\(\\dfrac{36}{99}\\).', '<b>\\(0{,}(36)=\\dfrac{36}{100}\\).</b> Phần tuần hoàn cho \\(\\dfrac{36}{99}\\).')]
summary = [('\\(\\lim\\frac1{n^k}=0\\), \\(\\lim q^n=0\\) (\\(|q|\\lt1\\)), \\(\\lim c=c\\); limits respect \\(+,-,\\times,:\\) and \\(\\sqrt{\\ }\\).', '\\(\\lim\\frac1{n^k}=0\\), \\(\\lim q^n=0\\) (\\(|q|\\lt1\\)), \\(\\lim c=c\\); giới hạn tương thích với \\(+,-,\\times,:\\) và \\(\\sqrt{\\ }\\).'),
           ('Rational in \\(n\\): divide by the highest power of the denominator.', 'Phân thức theo \\(n\\): chia cho lũy thừa cao nhất của mẫu.'),
           ('\\(S=\\dfrac{u_1}{1-q}\\) for \\(|q|\\lt1\\).', '\\(S=\\dfrac{u_1}{1-q}\\) với \\(|q|\\lt1\\).'),
           ('\\(\\lim n^k=+\\infty\\), \\(\\lim q^n=+\\infty\\) (\\(q\\gt1\\)). Key words: limit, converge, infinity.', '\\(\\lim n^k=+\\infty\\), \\(\\lim q^n=+\\infty\\) (\\(q\\gt1\\)). Từ cần nhớ (chạm vào để xem tiếng Anh): <b class="mbl-term" tabindex="0" data-en="limit">giới hạn</b>, <b class="mbl-term" tabindex="0" data-en="converge">hội tụ</b>, <b class="mbl-term" tabindex="0" data-en="infinity">vô cực</b>.')]
checks = [('I know the basic limits of sequences.', 'Em nhớ các giới hạn cơ bản của dãy số.'), ('I can compute limits of rational expressions in \\(n\\).', 'Em tính được giới hạn của phân thức theo \\(n\\).'),
          ('I can sum an infinite geometric series.', 'Em tính được tổng cấp số nhân lùi vô hạn.'), ('I can recognise an infinite limit.', 'Em nhận biết được giới hạn vô cực.')]
LL('g11-limits-03', 'Limits of Sequences', CV, ('Limits and Continuity', 'Giới hạn. Hàm số liên tục'), 'limits', 'sequence-limits', 160, 'Intermediate', 70, ('sequences, geometric progressions', 'dãy số, cấp số nhân'),
   'Finite limits of sequences, limit theorems, infinite geometric series, repeating decimals and infinite limits.', 'Bài 15 – Giới hạn hữu hạn của dãy số, định lí về giới hạn, cấp số nhân lùi vô hạn, số thập phân tuần hoàn, giới hạn vô cực.',
   ['limit', 'sequence', 'geometric series', 'infinity'], ['giới hạn', 'dãy số', 'cấp số nhân lùi vô hạn', 'vô cực'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g11-space-08'])
