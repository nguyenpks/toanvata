# -*- coding: utf-8 -*-
"""g10-stats-01 = Toán 10 KNTT, Bài 12: Số gần đúng và sai số. Mã ngân hàng câu hỏi: TOAN10-C5-B12."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g10d as S
from sp_g10d import D, rnd, target_unit, UNIT

def E(x): return D(x).replace('{,}', '.')                        # bản tiếng Anh: dấu chấm thập phân
CV = 'Số gần đúng và sai số'
vocab = defs(CV, [
 ('approx', 'approximate number', 'số gần đúng', 'a number \\(a\\) used instead of the exact value \\(\\bar a\\) (from measuring, rounding or calculating).', 'số \\(a\\) dùng thay cho giá trị đúng \\(\\bar a\\) (do đo đạc, làm tròn hoặc tính toán).', '\\(3.14\\) is an approximate number for \\(\\pi\\).', '\\(a\\)'),
 ('exact', 'exact value', 'số đúng (giá trị thật)', 'the true value \\(\\bar a\\) of a quantity; often we cannot know it.', 'giá trị thật \\(\\bar a\\) của một đại lượng; thường ta không biết chính xác.', 'The exact value of \\(\\sqrt2\\) has infinitely many digits.', '\\(\\bar a\\)'),
 ('abserr', 'absolute error', 'sai số tuyệt đối', '\\(\\Delta_a=|\\bar a-a|\\), the distance between the exact value and the approximate number.', '\\(\\Delta_a=|\\bar a-a|\\), khoảng cách giữa số đúng và số gần đúng.', 'The absolute error is at most 0.01.', '\\(\\Delta_a\\)'),
 ('accur', 'accuracy (bound of the error)', 'độ chính xác', 'a number \\(d\\) with \\(\\Delta_a\\le d\\); we write \\(\\bar a=a\\pm d\\).', 'số \\(d\\) sao cho \\(\\Delta_a\\le d\\); ta viết \\(\\bar a=a\\pm d\\).', 'The length is \\(152\\pm0.2\\) m.', '\\(d\\)'),
 ('relerr', 'relative error', 'sai số tương đối', '\\(\\delta_a=\\dfrac{\\Delta_a}{|a|}\\), usually written as a percentage; it is at most \\(\\dfrac{d}{|a|}\\).', '\\(\\delta_a=\\dfrac{\\Delta_a}{|a|}\\), thường viết dưới dạng phần trăm; không vượt quá \\(\\dfrac{d}{|a|}\\).', 'The relative error is less than 1%.', '\\(\\delta_a\\)'),
 ('round', 'round (a number)', 'quy tròn', 'replace a number by a simpler number with fewer digits.', 'thay một số bằng số gọn hơn, có ít chữ số hơn.', 'Round 3.14159 to the hundredths.', ''),
 ('place', 'place value (rounding place)', 'hàng (của chữ số)', 'the position of a digit: units, tens, tenths, hundredths…', 'vị trí của chữ số: hàng đơn vị, chục, phần mười, phần trăm…', 'Round to the nearest thousand.', '')])
goals = [('tell an exact value from an approximate number;', 'phân biệt [[số đúng|số đúng (giá trị thật)]] và [[số gần đúng]];'),
         ('find the absolute error, the accuracy and the relative error;', 'xác định [[sai số tuyệt đối]], [[độ chính xác]] và [[sai số tương đối]];'),
         ('round an approximate number with a given accuracy and state the error of rounding;', '[[quy tròn]] số gần đúng với độ chính xác cho trước và nêu sai số của số quy tròn;'),
         ('compare the precision of two measurements in real life.', 'so sánh độ chính xác của hai phép đo trong thực tế.')]
phrases = [('<b>Find the absolute error.</b>', 'Tìm sai số tuyệt đối.'), ('<b>The length is 152 plus or minus 0.2 metres.</b>', 'Chiều dài là 152 cộng trừ 0,2 mét.'),
           ('<b>Estimate the relative error.</b>', 'Ước lượng sai số tương đối.'), ('<b>Round the number to the nearest hundredth.</b>', 'Quy tròn số đến hàng phần trăm.'), ('<b>Which measurement is more precise?</b>', 'Phép đo nào chính xác hơn?')]
review = T('Rounding rule from lower grades: look at the first digit after the rounding place; if it is 5 or more, add 1 to the rounding digit; otherwise keep it. Then drop (or replace by 0) the digits after it. Example: \\(3.14159\\approx3.14\\) (hundredths), \\(2\\,841\\,675\\approx2\\,842\\,000\\) (thousands).',
           'Quy tắc làm tròn đã học: xét chữ số ngay sau hàng quy tròn; nếu chữ số đó lớn hơn hoặc bằng 5 thì cộng thêm 1 vào chữ số của hàng quy tròn, nếu nhỏ hơn 5 thì giữ nguyên; rồi bỏ đi (hoặc thay bằng 0) các chữ số phía sau. Ví dụ: \\(3{,}14159\\approx3{,}14\\) (hàng phần trăm), \\(2\\,841\\,675\\approx2\\,842\\,000\\) (hàng nghìn).')
theory = '<h3>12.1 %s</h3>' % TI('Approximate numbers', 'Số gần đúng')
theory += BOX('blue', ('Idea', 'Ý tưởng'), T('When we measure (a length, a mass, a time) or compute \\(\\sqrt2\\), \\(\\pi\\)…, we usually get a number \\(a\\) close to the exact value \\(\\bar a\\). We call \\(a\\) an approximate number of \\(\\bar a\\).',
  'Khi đo đạc (độ dài, khối lượng, thời gian) hay tính \\(\\sqrt2\\), \\(\\pi\\)…, ta thường chỉ nhận được số \\(a\\) gần với [[số đúng|số đúng (giá trị thật)]] \\(\\bar a\\). Ta gọi \\(a\\) là [[số gần đúng]] của \\(\\bar a\\).'))
theory += '<h3>12.2 %s</h3>' % TI('Errors', 'Sai số')
theory += BOX('mint', ('Absolute error and accuracy', 'Sai số tuyệt đối và độ chính xác'), M('\\Delta_a=|\\bar a-a|\\le d\\iff a-d\\le\\bar a\\le a+d\\qquad(\\text{viết } \\bar a=a\\pm d)'),
  T('Usually \\(\\bar a\\) is unknown, so we cannot find \\(\\Delta_a\\) exactly; we only give an upper bound \\(d\\), called the accuracy of \\(a\\). A smaller \\(d\\) is better.', 'Thường ta không biết \\(\\bar a\\) nên không tính được đúng \\(\\Delta_a\\); ta chỉ chặn trên nó bởi số \\(d\\), gọi là [[độ chính xác]] của số gần đúng \\(a\\). \\(d\\) càng nhỏ thì càng tốt.'))
theory += BOX('blue', ('Relative error', 'Sai số tương đối'), M('\\delta_a=\\dfrac{\\Delta_a}{|a|}\\le\\dfrac{d}{|a|}'),
  T('\\(\\delta_a\\) is usually written as a percentage. To compare two measurements of <b>different sizes</b> (a desk and a road), compare their relative errors: the smaller one is more precise.', '\\(\\delta_a\\) thường viết dạng phần trăm. Muốn so sánh hai phép đo có <b>độ lớn khác nhau</b> (cái bàn và con đường), ta so sánh sai số tương đối: phép đo nào có sai số tương đối nhỏ hơn thì chính xác hơn.'))
theory += '<h3>12.3 %s</h3>' % TI('Rounding approximate numbers', 'Quy tròn số gần đúng')
theory += BOX('mint', ('Two rules', 'Hai quy tắc'), UL([
  T('If \\(a\\) is the number rounded to some place, its absolute error is at most <b>half a unit of that place</b>. Example: rounding to the hundredths gives an error \\(\\le0.005\\).', 'Nếu \\(a\\) là số quy tròn đến một hàng nào đó thì sai số tuyệt đối của \\(a\\) không vượt quá <b>nửa đơn vị của hàng quy tròn</b>. Ví dụ: quy tròn đến hàng phần trăm thì sai số \\(\\le0{,}005\\).'),
  T('Given \\(a\\) with accuracy \\(d\\) and no rounding place, round \\(a\\) to the <b>lowest place for which \\(d\\) is less than one unit</b> of that place. Example: \\(d=0.002\\lt0.01\\) so round to the hundredths; \\(d=300\\lt1000\\) so round to the thousands.', 'Cho số gần đúng \\(a\\) với độ chính xác \\(d\\); khi không nói rõ hàng quy tròn, ta quy tròn \\(a\\) đến <b>hàng thấp nhất mà \\(d\\) nhỏ hơn một đơn vị của hàng đó</b>. Ví dụ: \\(d=0{,}002\\lt0{,}01\\) nên quy tròn đến hàng phần trăm; \\(d=300\\lt1000\\) nên quy tròn đến hàng nghìn.')]))
theory += TBL([TI('Accuracy \\(d\\)', 'Độ chính xác \\(d\\)'), TI('Round to the', 'Quy tròn đến hàng'), TI('Error of the rounded number', 'Sai số của số quy tròn')],
  [['\\(%s\\)' % D(d), TI(target_unit(d)[1], target_unit(d)[2]), '\\(\\le%s\\)' % D(target_unit(d)[0] / 2)] for d in (F(4, 1000), F(3, 100), F(2, 10), F(5), F(300))])
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('Do not round to a place finer than the accuracy: writing \\(2.2361\\) when \\(d=0.02\\) shows digits that are not reliable. Also, after rounding, the total error can grow: it is at most \\(d\\) plus the rounding error.',
  'Không quy tròn đến hàng nhỏ hơn mức độ chính xác cho phép: viết \\(2{,}2361\\) khi \\(d=0{,}02\\) là đưa ra những chữ số không đáng tin. Ngoài ra, sau khi quy tròn, sai số có thể tăng: tối đa bằng \\(d\\) cộng sai số quy tròn.'))
assert target_unit(F(4, 1000))[0] == F(1, 100) and target_unit(F(300))[0] == 1000 and target_unit(F(2, 10))[0] == 1

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('An error bound for \\(\\pi\\)', 'Chặn sai số khi lấy \\(\\pi\\approx3{,}14\\)'), T('Knowing \\(3.141\\lt\\pi\\lt3.142\\), estimate the absolute error when we take \\(\\pi\\approx3.14\\).', 'Biết \\(3{,}141\\lt\\pi\\lt3{,}142\\). Hãy ước lượng sai số tuyệt đối khi lấy \\(\\pi\\approx3{,}14\\).'),
  T('We cannot compute \\(|\\pi-3.14|\\) exactly, so we bound it.', 'Không tính được đúng \\(|\\pi-3{,}14|\\) nên ta chặn trên nó.'),
  [T('\\(3.141-3.14\\lt\\pi-3.14\\lt3.142-3.14\\), so \\(0.001\\lt\\pi-3.14\\lt0.002\\).', '\\(3{,}141-3{,}14\\lt\\pi-3{,}14\\lt3{,}142-3{,}14\\) nên \\(0{,}001\\lt\\pi-3{,}14\\lt0{,}002\\).')],
  T('\\(\\Delta=|\\pi-3.14|\\lt0.002\\); we can write \\(\\pi=3.14\\pm0.002\\).', '\\(\\Delta=|\\pi-3{,}14|\\lt0{,}002\\); có thể viết \\(\\pi=3{,}14\\pm0{,}002\\).'))
assert 3.141 < math.pi < 3.142
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Reading \\(a\\pm d\\)', 'Đọc kết quả \\(a\\pm d\\)'), T('A bridge is measured as \\(152\\pm0.2\\) m. In which interval is the true length? Estimate the relative error.', 'Chiều dài một cây cầu đo được là \\(152\\pm0{,}2\\) m. Chiều dài thật nằm trong đoạn nào? Ước lượng sai số tương đối.'),
  T('\\(a=152\\), \\(d=0.2\\).', '\\(a=152\\), \\(d=0{,}2\\).'),
  [T('\\(152-0.2\\le\\bar a\\le152+0.2\\), i.e. \\(\\bar a\\in[151.8;\\,152.2]\\).', '\\(152-0{,}2\\le\\bar a\\le152+0{,}2\\), tức \\(\\bar a\\in[151{,}8;\\,152{,}2]\\).'), T('\\(\\delta\\le\\dfrac{0.2}{152}\\approx0.0013=0.13\\%\\).', '\\(\\delta\\le\\dfrac{0{,}2}{152}\\approx0{,}0013=0{,}13\\%\\).')],
  T('\\([151.8;\\,152.2]\\); relative error at most about \\(0.13\\%\\).', '\\([151{,}8;\\,152{,}2]\\); sai số tương đối không quá khoảng \\(0{,}13\\%\\).'))
assert round(0.2 / 152 * 100, 2) == 0.13
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('An elephant and an orange', 'Con voi và quả cam'), T('A zoo weighs an elephant: \\(5000\\pm50\\) kg. A shop weighs an orange: \\(200\\pm5\\) g. Which weighing is more precise?', 'Vườn thú cân một con voi được \\(5000\\pm50\\) kg. Cửa hàng cân một quả cam được \\(200\\pm5\\) g. Phép cân nào chính xác hơn?'),
  T('The accuracies (50 kg and 5 g) are of different sizes: compare relative errors.', 'Hai độ chính xác (50 kg và 5 g) khác hẳn độ lớn: phải so sánh sai số tương đối.'),
  [T('Elephant: \\(\\dfrac{50}{5000}=1\\%\\).', 'Con voi: \\(\\dfrac{50}{5000}=1\\%\\).'), T('Orange: \\(\\dfrac{5}{200}=2.5\\%\\).', 'Quả cam: \\(\\dfrac{5}{200}=2{,}5\\%\\).')],
  T('\\(1\\%\\lt2.5\\%\\): weighing the elephant is more precise, although its error in kilograms is much larger.', '\\(1\\%\\lt2{,}5\\%\\): phép cân con voi chính xác hơn, dù sai số tính theo kilôgam lớn hơn nhiều.'))
r1, r2 = rnd(F(2841675), 1000), rnd(F(314159, 100000), F(1, 100)); assert r1 == 2842000 and r2 == F(314, 100) and target_unit(F(300))[0] == 1000 and target_unit(F(2, 1000))[0] == F(1, 100)
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Round with a given accuracy', 'Quy tròn khi biết độ chính xác'), T('Round: (a) the population of a city \\(a=2\\,841\\,675\\) with \\(d=300\\); (b) \\(a=3.14159\\) with \\(d=0.002\\). Give the error of each rounded number.', 'Hãy quy tròn: (a) dân số một thành phố \\(a=2\\,841\\,675\\) với \\(d=300\\); (b) \\(a=3{,}14159\\) với \\(d=0{,}002\\). Nêu sai số của mỗi số quy tròn.'),
  T('Find the lowest place for which \\(d\\) is less than one unit.', 'Tìm hàng thấp nhất mà \\(d\\) nhỏ hơn một đơn vị của hàng đó.'),
  [T('(a) \\(300\\lt1000\\) (but \\(300\\gt100\\)): round to the thousands, \\(a\\approx2\\,842\\,000\\).', '(a) \\(300\\lt1000\\) (nhưng \\(300\\gt100\\)): quy tròn đến hàng nghìn, \\(a\\approx2\\,842\\,000\\).'), T('(b) \\(0.002\\lt0.01\\) (but \\(\\gt0.001\\)): round to the hundredths, \\(a\\approx3.14\\).', '(b) \\(0{,}002\\lt0{,}01\\) (nhưng \\(\\gt0{,}001\\)): quy tròn đến hàng phần trăm, \\(a\\approx3{,}14\\).'),
   T('Rounding errors: \\(|2\\,842\\,000-2\\,841\\,675|=325\\le500\\) and \\(|3.14-3.14159|=0.00159\\le0.005\\).', 'Sai số quy tròn: \\(|2\\,842\\,000-2\\,841\\,675|=325\\le500\\) và \\(|3{,}14-3{,}14159|=0{,}00159\\le0{,}005\\).')],
  T('(a) \\(2\\,842\\,000\\); (b) \\(3.14\\).', '(a) \\(2\\,842\\,000\\); (b) \\(3{,}14\\).'))
lo, hi = F(199, 10) * F(149, 10), F(201, 10) * F(151, 10); assert (lo, hi) == (F(29651, 100), F(30351, 100)) and hi - 300 == F(351, 100) and 300 - lo == F(349, 100)
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Error of an area', 'Sai số của diện tích'), T('A rectangular garden is measured as \\(20\\pm0.1\\) m by \\(15\\pm0.1\\) m. Its area is given as \\(S=20\\cdot15=300\\ \\text{m}^2\\). Find an accuracy for \\(S\\) and its relative error.', 'Một mảnh vườn hình chữ nhật đo được hai cạnh \\(20\\pm0{,}1\\) m và \\(15\\pm0{,}1\\) m. Diện tích được ghi là \\(S=20\\cdot15=300\\ \\text{m}^2\\). Tìm một độ chính xác của \\(S\\) và sai số tương đối.'),
  T('Find the smallest and the largest possible area.', 'Tìm diện tích nhỏ nhất và lớn nhất có thể.'),
  [T('\\(19.9\\cdot14.9\\le\\bar S\\le20.1\\cdot15.1\\), i.e. \\(296.51\\le\\bar S\\le303.51\\).', '\\(19{,}9\\cdot14{,}9\\le\\bar S\\le20{,}1\\cdot15{,}1\\), tức \\(296{,}51\\le\\bar S\\le303{,}51\\).'), T('So \\(|\\bar S-300|\\le3.51\\).', 'Do đó \\(|\\bar S-300|\\le3{,}51\\).'), T('\\(\\delta_S\\le\\dfrac{3.51}{300}=1.17\\%\\).', '\\(\\delta_S\\le\\dfrac{3{,}51}{300}=1{,}17\\%\\).')],
  T('\\(S=300\\pm3.51\\ \\text{m}^2\\); relative error at most \\(1.17\\%\\) (about the sum \\(0.5\\%+0.67\\%\\) of the relative errors of the sides).', '\\(S=300\\pm3{,}51\\ \\text{m}^2\\); sai số tương đối không quá \\(1{,}17\\%\\) (xấp xỉ tổng \\(0{,}5\\%+0{,}67\\%\\) sai số tương đối của hai cạnh).'))
assert F(351, 100) / 300 == F(117, 10000)

def lvl(P):
    ctx, t, a = P['abs']; dl = abs(t - a)
    o1 = M4(1, '%s The exact amount is \\(%s\\) %s; the label shows \\(%s\\) %s. The absolute error is…' % (ctx[0], E(t), ctx[2], E(a), ctx[2]), '%s Lượng thực tế là \\(%s\\) %s; trên nhãn ghi \\(%s\\) %s. Sai số tuyệt đối là…' % (ctx[1], D(t), ctx[3], D(a), ctx[3]),
            D(dl), [D(dl * 10), D(a - F(int(a))), D(dl / 10)], '\\(\\Delta=|%s-%s|=%s\\).' % (E(t), E(a), E(dl)), '\\(\\Delta=|%s-%s|=%s\\).' % (D(t), D(a), D(dl)))
    ctx2, a2, d2 = P['int']
    o2 = M4(2, '%s \\(%s\\pm%s\\). The true value lies in…' % (ctx2[0], E(a2), E(d2)), '%s \\(%s\\pm%s\\). Giá trị thật nằm trong đoạn…' % (ctx2[1], D(a2), D(d2)),
            '[%s;\\,%s]' % (D(a2 - d2), D(a2 + d2)), ['[%s;\\,%s]' % (D(a2), D(a2 + d2)), '[%s;\\,%s]' % (D(a2 - d2), D(a2)), '[%s;\\,%s]' % (D(a2 - 2 * d2), D(a2 + 2 * d2))], '\\(a-d\\le\\bar a\\le a+d\\).', '\\(a-d\\le\\bar a\\le a+d\\).')
    a3, d3 = P['rd']; u, en, vi = target_unit(d3); r3 = rnd(a3, u); others = [rnd(a3, x[0]) for x in UNIT if x[0] != u and x[0] < abs(a3)]
    others = [w for w in sorted(set(others), key=lambda w: abs(w - r3)) if w != r3]
    o3 = M4(3, 'An approximate number \\(a=%s\\) has accuracy \\(d=%s\\). The correct rounded number is…' % (E(a3), E(d3)), 'Số gần đúng \\(a=%s\\) có độ chính xác \\(d=%s\\). Số quy tròn của \\(a\\) là…' % (D(a3), D(d3)),
            D(r3), [D(w) for w in others], '\\(d\\lt1\\) unit of the %s place: round to the %s.' % (en, en), '\\(d\\) nhỏ hơn 1 đơn vị hàng %s: quy tròn đến hàng %s.' % (vi, vi))
    a4, d4, pc, ok = P['rel']; real = d4 / a4 * 100; assert (real <= pc) == ok
    t4 = tf(4, 'A runner\'s time is \\(%s\\pm%s\\) s. The relative error is at most \\(%s\\%%\\).' % (E(a4), E(d4), E(pc)), 'Thành tích của một vận động viên là \\(%s\\pm%s\\) giây. Sai số tương đối không vượt quá \\(%s\\%%\\).' % (D(a4), D(d4), D(pc)), ok,
            '\\(\\dfrac{d}{a}=\\dfrac{%s}{%s}\\approx%s\\%%\\).' % (E(d4), E(a4), E(rnd(real, F(1, 1000)))), '\\(\\dfrac{d}{a}=\\dfrac{%s}{%s}\\approx%s\\%%\\).' % (D(d4), D(a4), D(rnd(real, F(1, 1000)))))
    (n1, b1, e1), (n2, b2, e2), claim = P['cmp']; p1, p2 = e1 / b1, e2 / b2; assert p1 != p2; first_better = p1 < p2
    t5 = tf(5, 'Measuring %s gives \\(%s\\pm%s\\); measuring %s gives \\(%s\\pm%s\\) (same unit). The first measurement is more precise.' % (n1[0], E(b1), E(e1), n2[0], E(b2), E(e2)),
            'Đo %s được \\(%s\\pm%s\\); đo %s được \\(%s\\pm%s\\) (cùng đơn vị). Phép đo thứ nhất chính xác hơn.' % (n1[1], D(b1), D(e1), n2[1], D(b2), D(e2)), first_better,
            'Relative errors: \\(%s\\%%\\) and \\(%s\\%%\\).' % (E(rnd(p1 * 100, F(1, 100))), E(rnd(p2 * 100, F(1, 100)))), 'Sai số tương đối: \\(%s\\%%\\) và \\(%s\\%%\\).' % (D(rnd(p1 * 100, F(1, 100))), D(rnd(p2 * 100, F(1, 100)))))
    x6, uu = P['round']; u6 = [x for x in UNIT if x[0] == uu][0]; r6 = rnd(x6, uu)
    s6 = sh(6, 'Round \\(%s\\) to the %s.' % (E(x6), u6[1]), 'Quy tròn số \\(%s\\) đến hàng %s.' % (D(x6), u6[2]), E(r6) if r6.denominator != 1 else r6.numerator, 'The digit after the rounding place decides: \\(%s\\).' % E(r6), 'Xét chữ số ngay sau hàng quy tròn: \\(%s\\).' % D(r6))
    s, ds = P['sq']; dS = (s + ds) ** 2 - s * s
    s7 = sh(7, 'A square tile has side \\(%s\\pm%s\\) cm. Its area is written as \\(%s\\ \\text{cm}^2\\). Find the largest possible absolute error of this area.' % (E(s), E(ds), E(s * s)),
            'Một viên gạch hình vuông có cạnh \\(%s\\pm%s\\) cm, diện tích được ghi là \\(%s\\ \\text{cm}^2\\). Tìm sai số tuyệt đối lớn nhất có thể của diện tích này.' % (D(s), D(ds), D(s * s)), E(dS),
            '\\((%s+%s)^2-%s=%s\\); the other side gives \\(%s-(%s-%s)^2=%s\\), which is smaller.' % (E(s), E(ds), E(s * s), E(dS), E(s * s), E(s), E(ds), E(s * s - (s - ds) ** 2)),
            '\\((%s+%s)^2-%s=%s\\); phía còn lại cho \\(%s-(%s-%s)^2=%s\\), nhỏ hơn.' % (D(s), D(ds), D(s * s), D(dS), D(s * s), D(s), D(ds), D(s * s - (s - ds) ** 2)))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]
PP = [dict(abs=(('A bottle of juice.', 'Một chai nước ép.', 'litres', 'lít'), F(4986, 1000), F(5)), int=(('A child\'s height (cm) is', 'Chiều cao (cm) của một em bé là'), F(1085, 10), F(5, 10)), rd=(F(375684, 100000), F(3, 1000)),
           rel=(F(125, 10), F(5, 100), F(4, 10), True), cmp=((('a desk', 'chiếc bàn'), F(120), F(5, 10)), (('a classroom', 'phòng học'), F(900), F(2)), None), round=(F(271828, 100000), F(1, 100)), sq=(F(20), F(1, 10))),
      dict(abs=(('A bag of rice.', 'Một túi gạo.', 'kg', 'kg'), F(10035, 1000), F(10)), int=(('The mass of a parcel is (kg)', 'Khối lượng một kiện hàng là (kg)'), F(253, 10), F(2, 10)), rd=(F(4518237), F(400)),
           rel=(F(48), F(2, 10), F(3, 10), False), cmp=((('a field', 'sân bóng'), F(10500), F(10)), (('a pencil', 'cây bút chì'), F(18), F(1, 10)), None), round=(F(1732051, 1000), F(1)), sq=(F(30), F(2, 10))),
      dict(abs=(('A can of paint.', 'Một thùng sơn.', 'litres', 'lít'), F(17862, 1000), F(18)), int=(('A road is (km)', 'Một con đường dài (km)'), F(126, 10), F(5, 100)), rd=(F(1234567, 10000), F(4, 100)),
           rel=(F(96), F(3, 10), F(5, 10), True), cmp=((('a hair', 'sợi tóc'), F(8, 100), F(1, 100)), (('a book', 'cuốn sách'), F(24), F(1, 10)), None), round=(F(6283185, 1000), F(10)), sq=(F(25), F(1, 2)))]
practice = three(lvl, PP)
practice = with_self(practice, S.M12S10, start=8)
mistakes = [('<b>Confusing \\(\\Delta_a\\) and \\(d\\).</b> \\(\\Delta_a\\) is the real distance (usually unknown); \\(d\\) is a bound for it.', '<b>Nhầm \\(\\Delta_a\\) với \\(d\\).</b> \\(\\Delta_a\\) là khoảng cách thật (thường không biết); \\(d\\) là số chặn trên của nó.'),
            ('<b>Comparing accuracies of different sizes.</b> Compare relative errors \\(\\dfrac d{|a|}\\), not \\(d\\).', '<b>So sánh độ chính xác của hai đại lượng khác cỡ.</b> Phải so sánh sai số tương đối \\(\\dfrac d{|a|}\\), không so \\(d\\).'),
            ('<b>Rounding too finely.</b> With \\(d=0.03\\) round to the tenths (\\(0.03\\lt0.1\\)), not to the hundredths.', '<b>Quy tròn quá mịn.</b> Với \\(d=0{,}03\\) phải quy tròn đến hàng phần mười (\\(0{,}03\\lt0{,}1\\)), không phải hàng phần trăm.'),
            ('<b>Error of a rounded number.</b> It is at most half a unit of the rounding place, not one unit.', '<b>Sai số của số quy tròn.</b> Không vượt quá nửa đơn vị hàng quy tròn, không phải một đơn vị.')]
summary = [('\\(\\Delta_a=|\\bar a-a|\\le d\\iff\\bar a=a\\pm d\\iff a-d\\le\\bar a\\le a+d\\).', '\\(\\Delta_a=|\\bar a-a|\\le d\\iff\\bar a=a\\pm d\\iff a-d\\le\\bar a\\le a+d\\).'),
           ('\\(\\delta_a=\\dfrac{\\Delta_a}{|a|}\\le\\dfrac{d}{|a|}\\); smaller relative error means more precise.', '\\(\\delta_a=\\dfrac{\\Delta_a}{|a|}\\le\\dfrac{d}{|a|}\\); sai số tương đối nhỏ hơn thì chính xác hơn.'),
           ('A number rounded to a place has error \\(\\le\\) half a unit of that place.', 'Số quy tròn đến một hàng có sai số không quá nửa đơn vị hàng đó.'),
           ('With accuracy \\(d\\): round to the lowest place whose unit is greater than \\(d\\). Key words: approximate, absolute error, relative error, round.', 'Biết độ chính xác \\(d\\): quy tròn đến hàng thấp nhất có đơn vị lớn hơn \\(d\\). Từ cần nhớ: approximate, absolute error, relative error, round.')]
checks = [('I can write a measurement as \\(a\\pm d\\) and read its interval.', 'Em viết được kết quả đo dạng \\(a\\pm d\\) và đọc được đoạn chứa giá trị đúng.'), ('I can find absolute and relative errors.', 'Em tính được sai số tuyệt đối, sai số tương đối.'),
          ('I can round a number with a given accuracy.', 'Em quy tròn được số gần đúng khi biết độ chính xác.'), ('I can compare the precision of two measurements.', 'Em so sánh được độ chính xác của hai phép đo.')]
LL('g10-stats-01', 'Approximate Numbers and Errors', CV, ('Statistics', 'Các số đặc trưng của mẫu số liệu không ghép nhóm'), 'statistics', 'approximate-numbers-errors', 120, 'Beginner', 55, ('rounding numbers, percentages', 'làm tròn số, tỉ số phần trăm'),
   'Approximate numbers, absolute error, accuracy, relative error and rounding with a given accuracy.', 'Bài 12 – Số gần đúng, sai số tuyệt đối, độ chính xác, sai số tương đối và quy tròn số gần đúng.',
   ['approximate number', 'absolute error', 'relative error', 'rounding'], ['số gần đúng', 'sai số tuyệt đối', 'sai số tương đối', 'quy tròn'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g10-vec-05'])
