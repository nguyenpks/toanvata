# -*- coding: utf-8 -*-
"""g10-coord-02 = Toán 10 KNTT, Bài 20: Vị trí tương đối giữa hai đường thẳng. Góc và khoảng cách. Mã ngân hàng câu hỏi: TOAN10-C7-B20."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_quick import *
import sp_g10h as S
from sp_g10h import surd, rt
from sp_g10g import leq, V2

CV = 'Vị trí tương đối, góc và khoảng cách'
vocab = defs(CV, [
 ('relpos', 'relative position of two lines', 'vị trí tương đối của hai đường thẳng', 'intersecting, parallel or coincident.', 'cắt nhau, song song hoặc trùng nhau.', 'Find the relative position of the two lines.', ''),
 ('angl2', 'angle between two lines', 'góc giữa hai đường thẳng', 'the smallest angle formed by the two lines, between \\(0^\\circ\\) and \\(90^\\circ\\).', 'góc nhỏ nhất tạo bởi hai đường thẳng, có số đo từ \\(0^\\circ\\) đến \\(90^\\circ\\).', 'The angle between the lines is 45°.', '\\(\\varphi\\)'),
 ('dptl', 'distance from a point to a line', 'khoảng cách từ một điểm đến một đường thẳng', 'the length of the perpendicular segment from the point to the line.', 'độ dài đoạn vuông góc kẻ từ điểm đến đường thẳng.', 'The distance from M to the line is 2.', '\\(d(M,\\Delta)\\)')])
goals = [('recognise when two lines intersect, are parallel, coincide or are perpendicular;', 'nhận biết điều kiện để hai đường thẳng cắt nhau, song song, trùng nhau, vuông góc;'),
         ('find the [[angle between two lines|angl2]] from normal (or direction) vectors;', 'tính [[góc giữa hai đường thẳng]] từ vectơ pháp tuyến (hoặc vectơ chỉ phương);'),
         ('compute the [[distance from a point to a line|dptl]] and between two parallel lines;', 'tính [[khoảng cách từ một điểm đến một đường thẳng]] và giữa hai đường thẳng song song;'),
         ('solve problems on areas, heights and shortest routes.', 'giải bài toán về diện tích, đường cao, đường đi ngắn nhất.')]
goals = [(e.replace('[[angle between two lines|angl2]]', 'angle between two lines').replace('[[distance from a point to a line|dptl]]', 'distance from a point to a line'), v) for e, v in goals]
phrases = [('<b>The two lines are parallel.</b>', 'Hai đường thẳng song song.'), ('<b>The normal vectors are perpendicular, so the lines are perpendicular.</b>', 'Hai vectơ pháp tuyến vuông góc nên hai đường thẳng vuông góc.'),
           ('<b>The angle between the two lines is forty-five degrees.</b>', 'Góc giữa hai đường thẳng bằng 45°.'), ('<b>The distance from M to the line is two units.</b>', 'Khoảng cách từ M đến đường thẳng bằng 2 đơn vị.'),
           ('<b>Take the absolute value of the numerator.</b>', 'Lấy giá trị tuyệt đối ở tử số.')]
review = T('From Bài 19: \\(ax+by+c=0\\) has normal vector \\(\\vec n=(a;b)\\). From Bài 11: \\(\\cos(\\vec u,\\vec v)=\\dfrac{\\vec u\\cdot\\vec v}{|\\vec u|\\,|\\vec v|}\\), \\(\\vec u\\perp\\vec v\\iff\\vec u\\cdot\\vec v=0\\).',
           'Từ Bài 19: \\(ax+by+c=0\\) có vectơ pháp tuyến \\(\\vec n=(a;b)\\). Từ Bài 11: \\(\\cos(\\vec u,\\vec v)=\\dfrac{\\vec u\\cdot\\vec v}{|\\vec u|\\,|\\vec v|}\\), \\(\\vec u\\perp\\vec v\\iff\\vec u\\cdot\\vec v=0\\).')
theory = '<h3>20.1 %s</h3>' % TI('Relative position of two lines', 'Vị trí tương đối giữa hai đường thẳng')
theory += BOX('blue', ('Rule', 'Quy tắc'), UL([T('For \\(\\Delta_1: a_1x+b_1y+c_1=0\\) and \\(\\Delta_2: a_2x+b_2y+c_2=0\\), the number of common points is the number of solutions of the system of the two equations: one solution – they <b>intersect</b>; no solution – they are <b>parallel</b>; infinitely many – they <b>coincide</b>.',
   'Với \\(\\Delta_1: a_1x+b_1y+c_1=0\\) và \\(\\Delta_2: a_2x+b_2y+c_2=0\\), số điểm chung bằng số nghiệm của hệ hai phương trình: một nghiệm – hai đường thẳng <b>cắt nhau</b>; vô nghiệm – <b>song song</b>; vô số nghiệm – <b>trùng nhau</b>.'),
  T('Quick test with normal vectors: if \\(\\vec n_1\\), \\(\\vec n_2\\) are not collinear (\\(a_1b_2-a_2b_1\\ne0\\)) the lines intersect; if they are collinear, take a point of \\(\\Delta_1\\): it lies on \\(\\Delta_2\\) – coincident, otherwise – parallel.',
   'Kiểm tra nhanh bằng vectơ pháp tuyến: nếu \\(\\vec n_1\\), \\(\\vec n_2\\) không cùng phương (\\(a_1b_2-a_2b_1\\ne0\\)) thì hai đường thẳng cắt nhau; nếu cùng phương, lấy một điểm của \\(\\Delta_1\\): điểm đó thuộc \\(\\Delta_2\\) thì trùng nhau, ngược lại thì song song.'),
  T('\\(\\Delta_1\\perp\\Delta_2\\iff\\vec n_1\\cdot\\vec n_2=0\\iff a_1a_2+b_1b_2=0\\). With slopes: \\(k_1k_2=-1\\).', '\\(\\Delta_1\\perp\\Delta_2\\iff\\vec n_1\\cdot\\vec n_2=0\\iff a_1a_2+b_1b_2=0\\). Theo hệ số góc: \\(k_1k_2=-1\\).')]))
theory += '<h3>20.2 %s</h3>' % TI('Angle between two lines', 'Góc giữa hai đường thẳng')
theory += BOX('blue', ('Definition and formula', 'Định nghĩa và công thức'), UL([T('Two intersecting lines form four angles; the smallest is the angle \\(\\varphi\\) between them. Parallel or coincident lines make an angle of \\(0^\\circ\\). So \\(0^\\circ\\le\\varphi\\le90^\\circ\\).',
   'Hai đường thẳng cắt nhau tạo thành bốn góc; góc nhỏ nhất là góc \\(\\varphi\\) giữa chúng. Hai đường thẳng song song hoặc trùng nhau tạo góc \\(0^\\circ\\). Vậy \\(0^\\circ\\le\\varphi\\le90^\\circ\\).'),
  T('\\(\\cos\\varphi=|\\cos(\\vec n_1,\\vec n_2)|=\\dfrac{|a_1a_2+b_1b_2|}{\\sqrt{a_1^2+b_1^2}\\,\\sqrt{a_2^2+b_2^2}}\\). The same formula works with direction vectors.', '\\(\\cos\\varphi=|\\cos(\\vec n_1,\\vec n_2)|=\\dfrac{|a_1a_2+b_1b_2|}{\\sqrt{a_1^2+b_1^2}\\,\\sqrt{a_2^2+b_2^2}}\\). Công thức đúng cả với vectơ chỉ phương.')]))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'), T('The angle between two <i>lines</i> is never obtuse: use the absolute value. The angle between two <i>vectors</i> can be up to \\(180^\\circ\\).', 'Góc giữa hai <i>đường thẳng</i> không bao giờ tù: luôn lấy giá trị tuyệt đối. Góc giữa hai <i>vectơ</i> có thể đến \\(180^\\circ\\).'))
theory += '<h3>20.3 %s</h3>' % TI('Distance from a point to a line', 'Khoảng cách từ một điểm đến một đường thẳng')
theory += BOX('blue', ('Formula', 'Công thức'), UL([T('For \\(M(x_0;y_0)\\) and \\(\\Delta: ax+by+c=0\\): \\(d(M,\\Delta)=\\dfrac{|ax_0+by_0+c|}{\\sqrt{a^2+b^2}}\\).', 'Với \\(M(x_0;y_0)\\) và \\(\\Delta: ax+by+c=0\\): \\(d(M,\\Delta)=\\dfrac{|ax_0+by_0+c|}{\\sqrt{a^2+b^2}}\\).'),
  T('Two parallel lines \\(ax+by+c_1=0\\), \\(ax+by+c_2=0\\) are at distance \\(\\dfrac{|c_1-c_2|}{\\sqrt{a^2+b^2}}\\) (distance from any point of one to the other).', 'Hai đường thẳng song song \\(ax+by+c_1=0\\), \\(ax+by+c_2=0\\) cách nhau \\(\\dfrac{|c_1-c_2|}{\\sqrt{a^2+b^2}}\\) (khoảng cách từ một điểm bất kì của đường này đến đường kia).')]))
theory += GEO({'view': [-1.5, 7, -1.5, 5.5], 'axes': True, 'steps': [
  {'type': 'point', 'id': 'P', 'at': [0, 3], 'name': ''}, {'type': 'point', 'id': 'Q', 'at': [4, 0], 'name': ''},
  {'type': 'line', 'id': 'd', 'through': ['P', 'Q'], 'style': {'strokeColor': '#046b4d'}},
  {'type': 'point', 'id': 'M', 'at': [5, 4], 'name': 'M(5; 4)'},
  {'type': 'altitude', 'from': 'M', 'to': ['P', 'Q'], 'foot': 'H', 'footName': 'H'},
  {'type': 'text', 'at': [0.5, 4.2], 'text': 'Δ: 3x + 4y − 12 = 0'}]},
  cap=('\\(d(M,\\Delta)=MH=\\dfrac{|3\\cdot5+4\\cdot4-12|}{\\sqrt{3^2+4^2}}=\\dfrac{19}{5}\\). \\(MH\\) is the shortest segment from \\(M\\) to \\(\\Delta\\).', '\\(d(M,\\Delta)=MH=\\dfrac{|3\\cdot5+4\\cdot4-12|}{\\sqrt{3^2+4^2}}=\\dfrac{19}{5}\\). \\(MH\\) là đoạn ngắn nhất nối \\(M\\) với \\(\\Delta\\).'),
  alt=('Distance from M to the line as the perpendicular segment MH', ''), height=320)
assert abs(3 * 5 + 4 * 4 - 12) == 19

assert (1 - 2 * 2 + 3, 2 * 1 + 2 - 4, 1 * 2 + (-2) * 1) == (0, 0, 0)
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Relative positions', 'Xét vị trí tương đối'), T('Let \\(\\Delta_1: x-2y+3=0\\). Find its position relative to \\(\\Delta_2: 2x-4y+1=0\\), \\(\\Delta_3: -2x+4y-6=0\\), \\(\\Delta_4: 2x+y-4=0\\).', 'Cho \\(\\Delta_1: x-2y+3=0\\). Xét vị trí tương đối của \\(\\Delta_1\\) với \\(\\Delta_2: 2x-4y+1=0\\), \\(\\Delta_3: -2x+4y-6=0\\), \\(\\Delta_4: 2x+y-4=0\\).'),
  T('Compare normal vectors, then test one point.', 'So sánh vectơ pháp tuyến, rồi thử một điểm.'),
  [T('\\(\\vec n_2=(2;-4)=2\\vec n_1\\); the point \\((-3;0)\\in\\Delta_1\\) gives \\(-6+1\\ne0\\): \\(\\Delta_1\\parallel\\Delta_2\\).', '\\(\\vec n_2=(2;-4)=2\\vec n_1\\); điểm \\((-3;0)\\in\\Delta_1\\) cho \\(-6+1\\ne0\\): \\(\\Delta_1\\parallel\\Delta_2\\).'),
   T('\\(\\Delta_3\\) is \\(\\Delta_1\\) multiplied by \\(-2\\): they coincide.', '\\(\\Delta_3\\) là \\(\\Delta_1\\) nhân với \\(-2\\): trùng nhau.'),
   T('\\(\\vec n_1\\cdot\\vec n_4=2-2=0\\): \\(\\Delta_1\\perp\\Delta_4\\); solving the system gives the common point \\((1;2)\\).', '\\(\\vec n_1\\cdot\\vec n_4=2-2=0\\): \\(\\Delta_1\\perp\\Delta_4\\); giải hệ được giao điểm \\((1;2)\\).')],
  T('Parallel; coincident; perpendicular at \\((1;2)\\).', 'Song song; trùng nhau; vuông góc tại \\((1;2)\\).'))
assert 2 * 1 + (-1) * (-3) == 5 and 5 * 5 == 25 and 5 * 10 == 50
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Angle between two lines', 'Góc giữa hai đường thẳng'), T('Find the angle between \\(\\Delta_1: 2x-y+1=0\\) and \\(\\Delta_2: x-3y+4=0\\).', 'Tính góc giữa hai đường thẳng \\(\\Delta_1: 2x-y+1=0\\) và \\(\\Delta_2: x-3y+4=0\\).'),
  T('\\(\\cos\\varphi=\\dfrac{|a_1a_2+b_1b_2|}{|\\vec n_1|\\,|\\vec n_2|}\\).', '\\(\\cos\\varphi=\\dfrac{|a_1a_2+b_1b_2|}{|\\vec n_1|\\,|\\vec n_2|}\\).'),
  [T('\\(\\vec n_1=(2;-1)\\), \\(\\vec n_2=(1;-3)\\), \\(\\vec n_1\\cdot\\vec n_2=2+3=5\\).', '\\(\\vec n_1=(2;-1)\\), \\(\\vec n_2=(1;-3)\\), \\(\\vec n_1\\cdot\\vec n_2=2+3=5\\).'), T('\\(\\cos\\varphi=\\dfrac5{\\sqrt5\\cdot\\sqrt{10}}=\\dfrac5{5\\sqrt2}=\\dfrac{\\sqrt2}2\\).', '\\(\\cos\\varphi=\\dfrac5{\\sqrt5\\cdot\\sqrt{10}}=\\dfrac5{5\\sqrt2}=\\dfrac{\\sqrt2}2\\).')],
  T('\\(\\varphi=45^\\circ\\).', '\\(\\varphi=45^\\circ\\).'))
assert abs(3 * 2 + 4 * (-1) - 12) == 10 and abs(-12 - 3) == 15
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Two distances', 'Hai loại khoảng cách'), T('a) Find the distance from \\(M(2;-1)\\) to \\(\\Delta: 3x+4y-12=0\\). b) Find the distance between \\(\\Delta\\) and \\(\\Delta\': 3x+4y+3=0\\).', 'a) Tính khoảng cách từ \\(M(2;-1)\\) đến \\(\\Delta: 3x+4y-12=0\\). b) Tính khoảng cách giữa \\(\\Delta\\) và \\(\\Delta\': 3x+4y+3=0\\).'),
  T('\\(\\sqrt{3^2+4^2}=5\\).', '\\(\\sqrt{3^2+4^2}=5\\).'),
  [T('a) \\(d=\\dfrac{|6-4-12|}{5}=\\dfrac{10}5=2\\).', 'a) \\(d=\\dfrac{|6-4-12|}{5}=\\dfrac{10}5=2\\).'), T('b) \\(\\Delta\\parallel\\Delta\'\\); \\(A(4;0)\\in\\Delta\\): \\(d=\\dfrac{|12+0+3|}5=3\\) (or \\(\\dfrac{|-12-3|}5\\)).', 'b) \\(\\Delta\\parallel\\Delta\'\\); \\(A(4;0)\\in\\Delta\\): \\(d=\\dfrac{|12+0+3|}5=3\\) (hoặc \\(\\dfrac{|-12-3|}5\\)).')],
  T('a) 2; b) 3.', 'a) 2; b) 3.'))
assert 4 * 1 - 3 * 1 - 1 == 0 and 4 * 4 - 3 * 5 - 1 == 0 and abs(4 * 5 - 3 * 0 - 1) == 19 and abs(1 * (5 - 0) + 4 * (0 - 1) + 5 * (1 - 5)) == 19
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Area by a height', 'Diện tích qua đường cao'), T('Find the area of triangle \\(ABC\\) with \\(A(1;1)\\), \\(B(4;5)\\), \\(C(5;0)\\).', 'Tính diện tích tam giác \\(ABC\\) với \\(A(1;1)\\), \\(B(4;5)\\), \\(C(5;0)\\).'),
  T('\\(S=\\frac12\\,AB\\cdot d(C,AB)\\).', '\\(S=\\frac12\\,AB\\cdot d(C,AB)\\).'),
  [T('\\(\\overrightarrow{AB}=(3;4)\\), \\(AB=5\\); \\(AB: 4(x-1)-3(y-1)=0\\iff4x-3y-1=0\\).', '\\(\\overrightarrow{AB}=(3;4)\\), \\(AB=5\\); \\(AB: 4(x-1)-3(y-1)=0\\iff4x-3y-1=0\\).'), T('\\(d(C,AB)=\\dfrac{|20-0-1|}{5}=\\dfrac{19}5\\); \\(S=\\frac12\\cdot5\\cdot\\frac{19}5=\\frac{19}2\\).', '\\(d(C,AB)=\\dfrac{|20-0-1|}{5}=\\dfrac{19}5\\); \\(S=\\frac12\\cdot5\\cdot\\frac{19}5=\\frac{19}2\\).')],
  T('\\(S=\\dfrac{19}2=9{,}5\\).', '\\(S=\\dfrac{19}2=9{,}5\\).'))
t5 = F(4 + 12 - 7, 5); H5 = (4 - t5, 6 - 2 * t5); assert H5 == (F(11, 5), F(12, 5)) and H5[0] + 2 * H5[1] - 7 == 0
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('The nearest point of a railway', 'Điểm gần nhất trên đường ray'), T('On a map (unit 1 km) a railway runs along \\(\\Delta: x+2y-7=0\\). A village is at \\(T(4;6)\\). Find the length of the shortest road from \\(T\\) to the railway and the point \\(H\\) where it meets the railway.', 'Trên bản đồ (đơn vị 1 km), một đường ray chạy theo đường thẳng \\(\\Delta: x+2y-7=0\\). Một ngôi làng ở \\(T(4;6)\\). Tính độ dài con đường ngắn nhất từ \\(T\\) đến đường ray và tìm điểm \\(H\\) nơi đường đó gặp đường ray.'),
  T('The shortest road is perpendicular to \\(\\Delta\\): \\(TH\\) has direction \\(\\vec n=(1;2)\\).', 'Đường ngắn nhất vuông góc với \\(\\Delta\\): \\(TH\\) có vectơ chỉ phương \\(\\vec n=(1;2)\\).'),
  [T('\\(d=\\dfrac{|4+12-7|}{\\sqrt5}=\\dfrac9{\\sqrt5}=\\dfrac{9\\sqrt5}5\\approx4{,}02\\) km.', '\\(d=\\dfrac{|4+12-7|}{\\sqrt5}=\\dfrac9{\\sqrt5}=\\dfrac{9\\sqrt5}5\\approx4{,}02\\) km.'),
   T('\\(TH: x=4+t,\\ y=6+2t\\); substitute: \\(4+t+12+4t-7=0\\Rightarrow t=-\\frac95\\); \\(H\\left(\\frac{11}5;\\frac{12}5\\right)\\).', '\\(TH: x=4+t,\\ y=6+2t\\); thay vào \\(\\Delta\\): \\(4+t+12+4t-7=0\\Rightarrow t=-\\frac95\\); \\(H\\left(\\frac{11}5;\\frac{12}5\\right)\\).')],
  T('About 4,02 km, meeting the railway at \\(H(2{,}2;\\,2{,}4)\\).', 'Khoảng 4,02 km, gặp đường ray tại \\(H(2{,}2;\\,2{,}4)\\).'))


def lvl(P):
    (a, b, c), k, kind = P['pos']; a2, b2, c2 = (k * a, k * b, k * c + 3) if kind == 0 else (-b, a, 2)
    names = [('parallel', 'song song'), ('perpendicular', 'vuông góc'), ('coincident', 'trùng nhau'), ('intersecting, not perpendicular', 'cắt nhau nhưng không vuông góc')]
    right = 0 if kind == 0 else 1
    o1 = M4(1, 'The lines \\(%s\\) and \\(%s\\) are…' % (leq(a, b, c), leq(a2, b2, c2)), 'Hai đường thẳng \\(%s\\) và \\(%s\\)…' % (leq(a, b, c), leq(a2, b2, c2)), TI(*names[right]),
            [TI(*names[j]) for j in range(4) if j != right], 'Compare \\(\\vec n_1=%s\\), \\(\\vec n_2=%s\\).' % (V2((a, b)), V2((a2, b2))), 'So sánh \\(\\vec n_1=%s\\) và \\(\\vec n_2=%s\\).' % (V2((a, b)), V2((a2, b2))))
    (p, q, cc), M = P['dist']; N = abs(p * M[0] + q * M[1] + cc); s = p * p + q * q
    o2 = M4(2, 'The distance from \\(M%s\\) to \\(%s\\) is…' % (V2(M), leq(p, q, cc)), 'Khoảng cách từ \\(M%s\\) đến đường thẳng \\(%s\\) là…' % (V2(M), leq(p, q, cc)), '\\(%s\\)' % surd(N, s),
            ['\\(%s\\)' % str(N), '\\(%s\\)' % surd(N, s * s), '\\(%s\\)' % surd(abs(p * M[0] + q * M[1] - cc), s)], '\\(d=\\dfrac{|ax_0+by_0+c|}{\\sqrt{a^2+b^2}}\\).', '\\(d=\\dfrac{|%d\\cdot(%d)%+d\\cdot(%d)%+d|}{\\sqrt{%d}}=%s\\).' % (p, M[0], q, M[1], cc, s, surd(N, s)))
    n1, n2 = P['ang']; pp = abs(n1[0] * n2[0] + n1[1] * n2[1]); ss = (n1[0] ** 2 + n1[1] ** 2) * (n2[0] ** 2 + n2[1] ** 2); cos = pp / math.sqrt(ss)
    deg = round(math.degrees(math.acos(cos))); assert abs(math.degrees(math.acos(cos)) - deg) < 1e-6 and deg in (45, 90, 60, 30)
    o3 = M4(3, 'The angle between \\(%s\\) and \\(%s\\) is…' % (leq(*n1, 1), leq(*n2, -2)), 'Góc giữa hai đường thẳng \\(%s\\) và \\(%s\\) bằng…' % (leq(*n1, 1), leq(*n2, -2)), '\\(%d^\\circ\\)' % deg,
            ['\\(%d^\\circ\\)' % x for x in (30, 60, 90, 135, 45) if x != deg], '\\(\\cos\\varphi=\\dfrac{%d}{\\sqrt{%d}}\\).' % (pp, ss), '\\(\\cos\\varphi=\\dfrac{|\\vec n_1\\cdot\\vec n_2|}{|\\vec n_1||\\vec n_2|}=\\dfrac{%d}{\\sqrt{%d}}\\).' % (pp, ss))
    (u, v, w), (u2, v2) = P['perp']; tv = u * u2 + v * v2 == 0
    t4 = tf(4, 'The lines \\(%s\\) and \\(%s\\) are perpendicular.' % (leq(u, v, w), leq(u2, v2, 3)), 'Hai đường thẳng \\(%s\\) và \\(%s\\) vuông góc với nhau.' % (leq(u, v, w), leq(u2, v2, 3)), tv,
            '\\(a_1a_2+b_1b_2=%d\\).' % (u * u2 + v * v2), '\\(a_1a_2+b_1b_2=%d\\).' % (u * u2 + v * v2))
    (e, f, g), M5, claim = P['claim']; N5 = abs(e * M5[0] + f * M5[1] + g); real = F(N5, math.isqrt(e * e + f * f))
    t5 = tf(5, 'The distance from \\(M%s\\) to \\(%s\\) equals \\(%s\\).' % (V2(M5), leq(e, f, g), fr(claim)), 'Khoảng cách từ \\(M%s\\) đến đường thẳng \\(%s\\) bằng \\(%s\\).' % (V2(M5), leq(e, f, g), fr(claim)), real == claim,
            '\\(d=\\dfrac{%d}{%d}=%s\\).' % (N5, math.isqrt(e * e + f * f), fr(real)), '\\(d=\\dfrac{%d}{%d}=%s\\).' % (N5, math.isqrt(e * e + f * f), fr(real)))
    (h, i), c1, c2 = P['par']; dd = F(abs(c1 - c2), math.isqrt(h * h + i * i)); assert dd.denominator == 1
    s6 = sh(6, 'Find the distance between the parallel lines \\(%s\\) and \\(%s\\).' % (leq(h, i, c1), leq(h, i, c2)), 'Tính khoảng cách giữa hai đường thẳng song song \\(%s\\) và \\(%s\\).' % (leq(h, i, c1), leq(h, i, c2)), int(dd),
            '\\(\\dfrac{|c_1-c_2|}{\\sqrt{a^2+b^2}}=\\dfrac{%d}{%d}\\).' % (abs(c1 - c2), math.isqrt(h * h + i * i)), '\\(\\dfrac{|c_1-c_2|}{\\sqrt{a^2+b^2}}=\\dfrac{%d}{%d}=%d\\).' % (abs(c1 - c2), math.isqrt(h * h + i * i), int(dd)))
    (j, kk, l), Hh = P['pipe']; N7 = abs(j * Hh[0] + kk * Hh[1] + l); d7 = F(N7, math.isqrt(j * j + kk * kk)) * 100; assert d7.denominator == 1
    s7 = sh(7, 'On a map (unit 100 m) a house is at \\(H%s\\) and a water main runs along \\(%s\\). Find the length in metres of the shortest pipe from the house to the main.' % (V2(Hh), leq(j, kk, l)), 'Trên bản đồ (đơn vị 100 m), một ngôi nhà ở \\(H%s\\), đường ống chính chạy theo đường thẳng \\(%s\\). Tính chiều dài (mét) đoạn ống ngắn nhất nối nhà với đường ống chính.' % (V2(Hh), leq(j, kk, l)), int(d7),
            '\\(d=\\dfrac{%d}{%d}\\) units.' % (N7, math.isqrt(j * j + kk * kk)), '\\(d=\\dfrac{%d}{%d}\\) đơn vị \\(=%d\\) m.' % (N7, math.isqrt(j * j + kk * kk), int(d7)))
    return [[o1, o2, o3], [t4, t5], [s6, s7]]


PP = [dict(pos=((1, -3, 2), 2, 0), dist=((3, -4, 1), (2, 3)), ang=((1, 2), (3, 1)), perp=((2, 3, -1), (3, -2)), claim=((6, 8, -5), (1, 2), F(17, 10)), par=((3, 4), -7, 8), pipe=((4, 3, -24), (1, 2))),
      dict(pos=((2, 5, -1), 1, 1), dist=((5, 12, -3), (1, -1)), ang=((2, 1), (1, -2)), perp=((1, 4, 2), (4, 1)), claim=((3, 4, 2), (2, -1), 1), par=((5, 12), 6, -20), pipe=((3, -4, 10), (2, 5))),
      dict(pos=((3, -1, 4), -2, 0), dist=((8, 6, 5), (-2, 1)), ang=((1, 1), (0, 1)), perp=((5, -2, 3), (2, 5)), claim=((4, -3, 6), (1, 1), 2), par=((8, -6), 3, 33), pipe=((12, 5, -30), (1, 1)))]
practice = three(lvl, PP)
practice = with_self(practice, S.M20S10, start=8)
mistakes = [('<b>Forgetting the absolute value in \\(\\cos\\varphi\\).</b> An angle between lines is at most \\(90^\\circ\\), so \\(\\cos\\varphi\\ge0\\).', '<b>Quên dấu giá trị tuyệt đối trong \\(\\cos\\varphi\\).</b> Góc giữa hai đường thẳng không quá \\(90^\\circ\\) nên \\(\\cos\\varphi\\ge0\\).'),
            ('<b>Writing the line in a non-general form before using \\(d(M,\\Delta)\\).</b> First bring it to \\(ax+by+c=0\\) (e.g. \\(y=2x-1\\to2x-y-1=0\\)).', '<b>Dùng công thức khoảng cách khi đường thẳng chưa ở dạng tổng quát.</b> Phải đưa về \\(ax+by+c=0\\) (ví dụ \\(y=2x-1\\to2x-y-1=0\\)).'),
            ('<b>Distance between parallel lines with different coefficients.</b> \\(x+2y+1=0\\) and \\(2x+4y-3=0\\): first make \\(a\\), \\(b\\) equal (\\(2x+4y+2=0\\)).', '<b>Khoảng cách giữa hai đường song song có hệ số khác nhau.</b> \\(x+2y+1=0\\) và \\(2x+4y-3=0\\): phải đưa về cùng \\(a\\), \\(b\\) (\\(2x+4y+2=0\\)) trước.'),
            ('<b>Concluding "parallel" only because the normal vectors are collinear.</b> Check a point: the lines may coincide.', '<b>Kết luận "song song" chỉ vì hai vectơ pháp tuyến cùng phương.</b> Phải thử một điểm: hai đường thẳng có thể trùng nhau.')]
summary = [('Position: solve the system, or compare \\(\\vec n_1\\), \\(\\vec n_2\\) and test one point; \\(\\perp\\iff a_1a_2+b_1b_2=0\\).', 'Vị trí tương đối: giải hệ, hoặc so sánh \\(\\vec n_1\\), \\(\\vec n_2\\) và thử một điểm; vuông góc \\(\\iff a_1a_2+b_1b_2=0\\).'),
           ('Angle: \\(\\cos\\varphi=\\dfrac{|a_1a_2+b_1b_2|}{\\sqrt{a_1^2+b_1^2}\\sqrt{a_2^2+b_2^2}}\\), \\(0^\\circ\\le\\varphi\\le90^\\circ\\).', 'Góc: \\(\\cos\\varphi=\\dfrac{|a_1a_2+b_1b_2|}{\\sqrt{a_1^2+b_1^2}\\sqrt{a_2^2+b_2^2}}\\), \\(0^\\circ\\le\\varphi\\le90^\\circ\\).'),
           ('Distance: \\(d(M,\\Delta)=\\dfrac{|ax_0+by_0+c|}{\\sqrt{a^2+b^2}}\\); parallel lines: \\(\\dfrac{|c_1-c_2|}{\\sqrt{a^2+b^2}}\\).', 'Khoảng cách: \\(d(M,\\Delta)=\\dfrac{|ax_0+by_0+c|}{\\sqrt{a^2+b^2}}\\); hai đường song song: \\(\\dfrac{|c_1-c_2|}{\\sqrt{a^2+b^2}}\\).'),
           ('Key words: parallel, coincident, perpendicular, angle between lines, distance.', 'Từ cần nhớ: parallel, coincident, perpendicular, angle between lines, distance.')]
checks = [('I can decide the relative position of two lines.', 'Em xét được vị trí tương đối của hai đường thẳng.'), ('I can compute the angle between two lines.', 'Em tính được góc giữa hai đường thẳng.'),
          ('I can compute distances from a point and between parallel lines.', 'Em tính được khoảng cách từ một điểm và giữa hai đường song song.'), ('I can use distances for areas and shortest routes.', 'Em dùng khoảng cách để tính diện tích, đường đi ngắn nhất.')]
LL('g10-coord-02', 'Relative Position, Angle and Distance', CV, ('Coordinate Geometry in the Plane', 'Phương pháp tọa độ trong mặt phẳng'), 'plane-coordinates', 'lines-angle-distance', 200, 'Intermediate', 70, ('equations of a line, dot product', 'phương trình đường thẳng, tích vô hướng'),
   'Intersecting, parallel, coincident and perpendicular lines; angle between two lines; distance from a point to a line.', 'Bài 20 – Vị trí tương đối giữa hai đường thẳng; góc giữa hai đường thẳng; khoảng cách từ một điểm đến một đường thẳng.',
   ['relative position', 'angle between lines', 'distance'], ['vị trí tương đối', 'góc giữa hai đường thẳng', 'khoảng cách'],
   goals, vocab, phrases, review, theory, examples, practice, mistakes, summary, checks, prerequisites=['g10-coord-01'])
