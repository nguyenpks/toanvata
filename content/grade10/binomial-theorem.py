# -*- coding: utf-8 -*-
"""g10-comb-03 = Toán 10 KNTT, Bài 25: Nhị thức Newton (với n = 4, n = 5). Mã ngân hàng câu hỏi: TOAN10-C8-B25."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g10i as S
from sp_g10i import binom_str, mono
import mb_pgf

C = math.comb
CV = 'Nhị thức Newton'
vocab = defs(CV, [
 ('binthm', 'binomial theorem', 'công thức nhị thức Newton', '\\((a+b)^n=\\sum_{k=0}^{n}C_n^ka^{n-k}b^k\\) (here \\(n=4,5\\)).', '\\((a+b)^n=\\sum_{k=0}^{n}C_n^ka^{n-k}b^k\\) (ở đây \\(n=4,5\\)).', 'Expand (x + 2)^4 by the binomial theorem.', ''),
 ('bincoef', 'binomial coefficient', 'hệ số nhị thức', 'the number \\(C_n^k\\) in front of \\(a^{n-k}b^k\\).', 'số \\(C_n^k\\) đứng trước \\(a^{n-k}b^k\\).', 'The binomial coefficients of n = 4 are 1, 4, 6, 4, 1.', '\\(C_n^k\\)'),
 ('pascal', 'Pascal\'s triangle', 'tam giác Pascal', 'a triangle of numbers in which each entry is the sum of the two above it; row \\(n\\) lists \\(C_n^0,\\dots,C_n^n\\).', 'bảng số hình tam giác, mỗi số bằng tổng hai số ngay trên nó; hàng \\(n\\) gồm \\(C_n^0,\\dots,C_n^n\\).', 'Read the coefficients from Pascal\'s triangle.', '')])
goals = [('recognise the binomial expansion of \\((a+b)^4\\) and \\((a+b)^5\\);', 'nhận biết [[công thức nhị thức Newton]] khai triển \\((a+b)^4\\), \\((a+b)^5\\);'),
         ('read the coefficients from combinations or Pascal\'s triangle;', 'đọc [[hệ số nhị thức]] bằng tổ hợp hoặc [[tam giác Pascal]];'),
         ('expand binomials and find a given coefficient or term;', 'khai triển nhị thức, tìm hệ số hoặc số hạng theo yêu cầu;'),
         ('use expansions to approximate numbers (compound interest).', 'dùng khai triển để tính gần đúng (lãi kép).')]
phrases = [('<b>Expand the binomial.</b>', 'Khai triển nhị thức.'), ('<b>The coefficient of x cubed is ten.</b>', 'Hệ số của \\(x^3\\) bằng 10.'), ('<b>The expansion has five terms.</b>', 'Khai triển có năm số hạng.'),
           ('<b>The powers of a go down and the powers of b go up.</b>', 'Số mũ của \\(a\\) giảm dần, số mũ của \\(b\\) tăng dần.'), ('<b>Watch the sign of each term.</b>', 'Chú ý dấu của từng số hạng.')]
review = T('From Bài 24: \\(C_n^k=\\dfrac{n!}{k!(n-k)!}\\), \\(C_n^k=C_n^{n-k}\\). From Grade 8: \\((a+b)^2=a^2+2ab+b^2\\), \\((a+b)^3=a^3+3a^2b+3ab^2+b^3\\).', 'Từ Bài 24: \\(C_n^k=\\dfrac{n!}{k!(n-k)!}\\), \\(C_n^k=C_n^{n-k}\\). Từ lớp 8: \\((a+b)^2=a^2+2ab+b^2\\), \\((a+b)^3=a^3+3a^2b+3ab^2+b^3\\).')
theory = '<h3>25.1 %s</h3>' % TI('Expanding \\((a+b)^4\\) and \\((a+b)^5\\)', 'Khai triển \\((a+b)^4\\) và \\((a+b)^5\\)')
theory += BOX('blue', ('Formulas', 'Công thức'), UL([T('\\((a+b)^4=a^4+4a^3b+6a^2b^2+4ab^3+b^4\\).', '\\((a+b)^4=a^4+4a^3b+6a^2b^2+4ab^3+b^4\\).'),
  T('\\((a+b)^5=a^5+5a^4b+10a^3b^2+10a^2b^3+5ab^4+b^5\\).', '\\((a+b)^5=a^5+5a^4b+10a^3b^2+10a^2b^3+5ab^4+b^5\\).'),
  T('Why: expanding \\((a+b)(a+b)\\cdots(a+b)\\), the term \\(a^{n-k}b^k\\) appears once for each way of choosing the \\(k\\) brackets that give \\(b\\): \\(C_n^k\\) times. So the coefficients are \\(C_n^0, C_n^1,\\dots,C_n^n\\).', 'Vì sao: khi nhân \\((a+b)(a+b)\\cdots(a+b)\\), số hạng \\(a^{n-k}b^k\\) xuất hiện mỗi lần ta chọn \\(k\\) ngoặc lấy \\(b\\): đúng \\(C_n^k\\) lần. Vậy các hệ số là \\(C_n^0, C_n^1,\\dots,C_n^n\\).')]))
rows = [[C(n, k) for k in range(n + 1)] for n in range(6)]
body = ['\\begin{tikzpicture}[x=0.95cm, y=0.8cm]']
for n, row in enumerate(rows):
    body.append('\\node[text=ink!70, font=\\footnotesize, anchor=east] at (-3.6,%s) {$n=%d$};' % (-n, n))
    for k, v in enumerate(row):
        x = k - n / 2
        body.append('\\node[circle, minimum size=0.62cm, inner sep=0pt, fill=%s, font=\\small] (n%d%d) at (%s,%s) {$%d$};' % ('mint!55' if n in (4, 5) else 'gray!12', n, k, x, -n, v))
        if n and 0 < k < n:
            body.append('\\draw[-{Stealth[length=1.4mm]}, draw=ink!45] (n%d%d) -- (n%d%d); \\draw[-{Stealth[length=1.4mm]}, draw=ink!45] (n%d%d) -- (n%d%d);' % (n - 1, k - 1, n, k, n - 1, k, n, k))
body.append('\\end{tikzpicture}')
pas = mb_pgf.raw_svg('\n'.join(body))
theory += mb_pgf.img(pas, 'Pascal triangle rows 0 to 5', 420, TI('Pascal\'s triangle: each number is the sum of the two numbers above it. Rows 4 and 5 give the coefficients 1, 4, 6, 4, 1 and 1, 5, 10, 10, 5, 1.', 'Tam giác Pascal: mỗi số bằng tổng hai số ngay trên nó. Hàng 4 và hàng 5 cho các hệ số 1, 4, 6, 4, 1 và 1, 5, 10, 10, 5, 1.'))
theory += BOX('mint', ('Remarks', 'Nhận xét'), UL([T('\\((a+b)^n\\) has \\(n+1\\) terms; powers of \\(a\\) decrease from \\(n\\) to 0, powers of \\(b\\) increase from 0 to \\(n\\); in every term the exponents add up to \\(n\\).', '\\((a+b)^n\\) có \\(n+1\\) số hạng; số mũ của \\(a\\) giảm từ \\(n\\) về 0, của \\(b\\) tăng từ 0 đến \\(n\\); trong mỗi số hạng tổng hai số mũ bằng \\(n\\).'),
  T('The term containing \\(b^k\\) is \\(C_n^ka^{n-k}b^k\\) (term number \\(k+1\\)).', 'Số hạng chứa \\(b^k\\) là \\(C_n^ka^{n-k}b^k\\) (số hạng thứ \\(k+1\\)).'),
  T('For \\((a-b)^n\\) the signs alternate: \\(+,-,+,\\dots\\). Putting \\(a=b=1\\): \\(C_n^0+\\dots+C_n^n=2^n\\).', 'Với \\((a-b)^n\\) các dấu đan xen \\(+,-,+,\\dots\\). Thay \\(a=b=1\\): \\(C_n^0+\\dots+C_n^n=2^n\\).')]))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('Raise the whole term to the power: \\((2x)^3=8x^3\\), not \\(2x^3\\); \\((-1)^3=-1\\).', 'Nâng cả số hạng lên lũy thừa: \\((2x)^3=8x^3\\), không phải \\(2x^3\\); \\((-1)^3=-1\\).'))

assert [C(4, k) * 2 ** k for k in range(5)] == [1, 8, 24, 32, 16]
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Expanding \\((x+2)^4\\)', 'Khai triển \\((x+2)^4\\)'), T('Expand \\((x+2)^4\\).', 'Khai triển \\((x+2)^4\\).'),
  T('\\(a=x\\), \\(b=2\\), coefficients 1, 4, 6, 4, 1.', '\\(a=x\\), \\(b=2\\), hệ số 1, 4, 6, 4, 1.'), [T('\\(x^4+4x^3\\cdot2+6x^2\\cdot2^2+4x\\cdot2^3+2^4\\).', '\\(x^4+4x^3\\cdot2+6x^2\\cdot2^2+4x\\cdot2^3+2^4\\).')],
  T('\\(x^4+8x^3+24x^2+32x+16\\).', '\\(x^4+8x^3+24x^2+32x+16\\).'))
assert [C(5, k) * 2 ** (5 - k) * (-1) ** k for k in range(6)] == [32, -80, 80, -40, 10, -1]
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Expanding \\((2x-1)^5\\)', 'Khai triển \\((2x-1)^5\\)'), T('Expand \\((2x-1)^5\\).', 'Khai triển \\((2x-1)^5\\).'),
  T('\\(a=2x\\), \\(b=-1\\); signs alternate.', '\\(a=2x\\), \\(b=-1\\); dấu đan xen.'), [T('\\((2x)^5-5(2x)^4+10(2x)^3-10(2x)^2+5(2x)-1\\).', '\\((2x)^5-5(2x)^4+10(2x)^3-10(2x)^2+5(2x)-1\\).')],
  T('\\(32x^5-80x^4+80x^3-40x^2+10x-1\\).', '\\(32x^5-80x^4+80x^3-40x^2+10x-1\\).'))
assert C(5, 3) * 3 ** 3 * (-2) ** 2 == 1080
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('One coefficient', 'Tìm một hệ số'), T('Find the coefficient of \\(x^3\\) in \\((3x-2)^5\\).', 'Tìm hệ số của \\(x^3\\) trong khai triển \\((3x-2)^5\\).'),
  T('The term is \\(C_5^k(3x)^{5-k}(-2)^k\\); need \\(5-k=3\\).', 'Số hạng tổng quát \\(C_5^k(3x)^{5-k}(-2)^k\\); cần \\(5-k=3\\).'), [T('\\(k=2\\): \\(C_5^2\\cdot3^3\\cdot(-2)^2=10\\cdot27\\cdot4\\).', '\\(k=2\\): \\(C_5^2\\cdot3^3\\cdot(-2)^2=10\\cdot27\\cdot4\\).')], T('1080.', '1080.'))
assert C(4, 2) * 2 ** 2 == 24
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Constant term', 'Số hạng không chứa \\(x\\)'), T('Find the term without \\(x\\) in \\(\\left(x+\\dfrac2x\\right)^4\\).', 'Tìm số hạng không chứa \\(x\\) trong khai triển \\(\\left(x+\\dfrac2x\\right)^4\\).'),
  T('\\(C_4^kx^{4-k}\\left(\\dfrac2x\\right)^k=C_4^k2^kx^{4-2k}\\).', '\\(C_4^kx^{4-k}\\left(\\dfrac2x\\right)^k=C_4^k2^kx^{4-2k}\\).'), [T('\\(4-2k=0\\Rightarrow k=2\\): \\(C_4^2\\cdot2^2=6\\cdot4\\).', '\\(4-2k=0\\Rightarrow k=2\\): \\(C_4^2\\cdot2^2=6\\cdot4\\).')], T('24.', '24.'))
assert abs(1.02 ** 5 - 1.1040808032) < 1e-12 and abs((1 + 5 * 0.02 + 10 * 0.0004) - 1.104) < 1e-12
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Compound interest', 'Lãi kép'), T('You deposit 100 million VND at 2% per year, compound interest, for 5 years. Use the first three terms of \\((1+0{,}02)^5\\) to estimate the final amount, and compare with the exact value.', 'Gửi 100 triệu đồng, lãi kép 2%/năm trong 5 năm. Dùng ba số hạng đầu của khai triển \\((1+0{,}02)^5\\) để ước tính số tiền nhận được và so sánh với giá trị đúng.'),
  T('Amount \\(=100(1+0{,}02)^5\\).', 'Số tiền \\(=100(1+0{,}02)^5\\).'),
  [T('\\((1+0{,}02)^5\\approx1+5\\cdot0{,}02+10\\cdot0{,}02^2=1{,}104\\).', '\\((1+0{,}02)^5\\approx1+5\\cdot0{,}02+10\\cdot0{,}02^2=1{,}104\\).'), T('Estimate 110,4 million; exact \\(1{,}02^5=1{,}10408\\ldots\\): 110,408 million. The error is under 10 000 VND.', 'Ước tính 110,4 triệu; giá trị đúng \\(1{,}02^5=1{,}10408\\ldots\\): 110,408 triệu. Sai số dưới 10 000 đồng.')],
  T('About 110,4 million VND.', 'Khoảng 110,4 triệu đồng.'))


def lvl(P):
    (a, b, n, k) = P['coef']; c = C(n, k) * a ** k * b ** (n - k)
    o1 = M4(1, 'The coefficient of \\(x^{%d}\\) in \\(%s\\) is…' % (k, binom_str(a, b, n)), 'Hệ số của \\(x^{%d}\\) trong khai triển \\(%s\\) là…' % (k, binom_str(a, b, n)), '\\(%d\\)' % c,
            ['\\(%d\\)' % C(n, k), '\\(%d\\)' % (C(n, k) * a ** k), '\\(%d\\)' % -c], 'Term \\(C_{%d}^{%d}(%dx)^{%d}(%d)^{%d}\\).' % (n, n - k, a, k, b, n - k), 'Số hạng \\(C_{%d}^{%d}(%dx)^{%d}(%d)^{%d}\\).' % (n, n - k, a, k, b, n - k))
    (a2, b2, n2) = P['sum']; s2 = (a2 + b2) ** n2
    o2 = M4(2, 'The sum of the coefficients of \\(%s\\) is…' % binom_str(a2, b2, n2), 'Tổng các hệ số trong khai triển \\(%s\\) là…' % binom_str(a2, b2, n2), '\\(%d\\)' % s2,
            ['\\(%d\\)' % 2 ** n2, '\\(%d\\)' % (abs(a2) + abs(b2)) ** n2 if (abs(a2) + abs(b2)) ** n2 != s2 else '\\(%d\\)' % (s2 + 1), '\\(%d\\)' % (a2 ** n2 + b2 ** n2)], 'Put \\(x=1\\).', 'Thay \\(x=1\\): \\((%d%+d)^{%d}=%d\\).' % (a2, b2, n2, s2))
    (a3, b3) = P['mid']; m3 = C(4, 2) * a3 ** 2 * b3 ** 2
    o3 = M4(3, 'The middle term of \\(%s\\) is…' % binom_str(a3, b3, 4), 'Số hạng chính giữa của khai triển \\(%s\\) là…' % binom_str(a3, b3, 4), '\\(%s\\)' % mono(m3, 2),
            ['\\(%s\\)' % mono(C(4, 2), 2), '\\(%s\\)' % mono(m3, 3), '\\(%s\\)' % mono(4 * a3 ** 3 * b3, 3)], 'Third of five terms.', 'Số hạng thứ ba trong năm số hạng: \\(C_4^2(%dx)^2(%d)^2\\).' % (a3, b3))
    (se, sv), val = P['stmt']
    t4 = tf(4, se, sv, val, 'Expand or use \\(C_n^k\\).', 'Khai triển hoặc dùng \\(C_n^k\\) để kiểm tra.')
    cc, claim = P['const']; real = C(4, 2) * cc ** 2
    t5 = tf(5, 'The term without \\(x\\) in \\(\\left(x%s\\dfrac{%d}{x}\\right)^4\\) is %d.' % ('+' if cc > 0 else '-', abs(cc), claim), 'Số hạng không chứa \\(x\\) trong khai triển \\(\\left(x%s\\dfrac{%d}{x}\\right)^4\\) bằng %d.' % ('+' if cc > 0 else '-', abs(cc), claim), real == claim,
            '\\(k=2\\): \\(C_4^2\\cdot(%d)^2=%d\\).' % (cc, real), '\\(k=2\\): \\(C_4^2\\cdot(%d)^2=%d\\).' % (cc, real))
    (a6, b6, n6, k6) = P['short']; c6 = C(n6, k6) * a6 ** k6 * b6 ** (n6 - k6)
    s6 = sh(6, 'Find the coefficient of \\(x^{%d}\\) in \\(%s\\).' % (k6, binom_str(a6, b6, n6)), 'Tìm hệ số của \\(x^{%d}\\) trong khai triển \\(%s\\).' % (k6, binom_str(a6, b6, n6)), c6,
            '\\(C_{%d}^{%d}\\cdot%d^{%d}\\cdot(%d)^{%d}\\).' % (n6, k6, a6, k6, b6, n6 - k6), '\\(C_{%d}^{%d}\\cdot%d^{%d}\\cdot(%d)^{%d}=%d\\).' % (n6, k6, a6, k6, b6, n6 - k6, c6))
    M, r, years, est = P['money']
    s7 = sh(7, 'Deposit %d million VND at %d%% per year compound interest for %d years. Using the first two terms of the binomial expansion, estimate the final amount (million VND).' % (M, r, years), 'Gửi %d triệu đồng, lãi kép %d%%/năm trong %d năm. Dùng hai số hạng đầu của khai triển nhị thức, ước tính số tiền nhận được (triệu đồng).' % (M, r, years), est,
            '\\((1+x)^n\\approx1+nx\\).', '\\(%d(1+%s)^{%d}\\approx%d(1+%d\\cdot%s)=%d\\).' % (M, fr(F(r, 100)), years, M, years, fr(F(r, 100)), est))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]


assert C(5, 2) * (-1) ** 3 == -10 and 1 + 4 + 6 + 4 + 1 == 16 and sum(C(5, k) for k in range(6)) == 32
PP = [dict(coef=(2, 3, 4, 3), sum=(2, -3, 5), mid=(1, 3), stmt=(('In \\((x-1)^5\\) the coefficient of \\(x^2\\) is \\(-10\\).', 'Trong khai triển \\((x-1)^5\\), hệ số của \\(x^2\\) bằng \\(-10\\).'), True), const=(3, 54), short=(1, 2, 5, 2), money=(100, 2, 5, 110)),
      dict(coef=(3, -2, 5, 2), sum=(3, -2, 4), mid=(2, -1), stmt=(('\\((x+1)^4=x^4+4x^3+4x^2+4x+1\\).', '\\((x+1)^4=x^4+4x^3+4x^2+4x+1\\).'), False), const=(-2, 16), short=(2, -1, 4, 3), money=(200, 1, 4, 208)),
      dict(coef=(2, -3, 5, 3), sum=(1, 2, 4), mid=(3, 1), stmt=(('\\(C_5^0+C_5^1+C_5^2+C_5^3+C_5^4+C_5^5=32\\).', '\\(C_5^0+C_5^1+C_5^2+C_5^3+C_5^4+C_5^5=32\\).'), True), const=(1, 6), short=(3, 1, 5, 4), money=(50, 3, 4, 56))]
practice = three(lvl, PP)
practice = with_self(practice, S.M25S10, start=8)
mistakes = [('<b>Not raising the coefficient.</b> \\((2x)^3=8x^3\\), not \\(2x^3\\).', '<b>Không nâng lũy thừa hệ số.</b> \\((2x)^3=8x^3\\), không phải \\(2x^3\\).'), ('<b>Losing the minus signs.</b> In \\((x-2)^5\\): \\(b=-2\\), so odd powers of \\(b\\) are negative.', '<b>Mất dấu trừ.</b> Trong \\((x-2)^5\\): \\(b=-2\\), lũy thừa bậc lẻ của \\(b\\) mang dấu âm.'),
            ('<b>Confusing "term number \\(k\\)" with \\(b^k\\).</b> Term number \\(k+1\\) contains \\(b^k\\).', '<b>Nhầm "số hạng thứ \\(k\\)" với \\(b^k\\).</b> Số hạng thứ \\(k+1\\) chứa \\(b^k\\).'), ('<b>Giving the term instead of the coefficient.</b> The coefficient of \\(x^3\\) in \\(1080x^3\\) is 1080.', '<b>Ghi số hạng thay cho hệ số.</b> Hệ số của \\(x^3\\) trong \\(1080x^3\\) là 1080.')]
summary = [('\\((a+b)^4\\): 1, 4, 6, 4, 1; \\((a+b)^5\\): 1, 5, 10, 10, 5, 1 (Pascal\'s triangle).', '\\((a+b)^4\\): 1, 4, 6, 4, 1; \\((a+b)^5\\): 1, 5, 10, 10, 5, 1 (tam giác Pascal).'),
           ('Term with \\(b^k\\): \\(C_n^ka^{n-k}b^k\\); \\(n+1\\) terms; exponents add to \\(n\\).', 'Số hạng chứa \\(b^k\\): \\(C_n^ka^{n-k}b^k\\); có \\(n+1\\) số hạng; tổng số mũ bằng \\(n\\).'),
           ('Sum of coefficients: put \\(x=1\\); \\((1+x)^n\\approx1+nx\\) for small \\(x\\).', 'Tổng các hệ số: thay \\(x=1\\); \\((1+x)^n\\approx1+nx\\) khi \\(x\\) nhỏ.'), ('Key words: binomial theorem, coefficient, term, Pascal\'s triangle.', 'Từ cần nhớ: binomial theorem, coefficient, term, Pascal\'s triangle.')]
checks = [('I can expand \\((a+b)^4\\), \\((a+b)^5\\).', 'Em khai triển được \\((a+b)^4\\), \\((a+b)^5\\).'), ('I can find a given coefficient or term.', 'Em tìm được hệ số, số hạng theo yêu cầu.'),
          ('I can read Pascal\'s triangle.', 'Em đọc được tam giác Pascal.'), ('I can approximate with the first terms.', 'Em tính gần đúng bằng vài số hạng đầu.')]
LL('g10-comb-03', 'The Binomial Theorem', CV, ('Combinatorics', 'Đại số tổ hợp'), 'combinatorics', 'binomial-theorem', 250, 'Intermediate', 60, ('combinations', 'tổ hợp'),
   'Expansions of (a + b)^4 and (a + b)^5, binomial coefficients, Pascal\'s triangle, coefficients of a term, approximations.', 'Bài 25 – Khai triển (a + b)^4, (a + b)^5; hệ số nhị thức, tam giác Pascal; hệ số của một số hạng; tính gần đúng.',
   ['binomial theorem', 'coefficient', 'Pascal\'s triangle'], ['nhị thức Newton', 'hệ số', 'tam giác Pascal'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g10-comb-02'])
