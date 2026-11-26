# -*- coding: utf-8 -*-
"""Nội dung bài g9-solids-01 = Toán 9 KNTT, Bài 31: Hình trụ và hình nón – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 10 – Lesson 31; Mini project Ch.10 (Curved-Surface Design)."""
import os, sys, math
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9, sp_g9p, sp_g9q as Q
from mb_pgf import texsvg, col

LID = 'g9-solids-01'
CH = 'Một số hình khối trong thực tiễn'
TOPIC = ('Solid Shapes in Everyday Life', CH)
ensure_vocab([
 ('g9-cylinder', 'cylinder', 'hình trụ (lớp 9)', CH, 'A can of milk has the shape of a cylinder.', ''),
 ('g9-cone', 'cone', 'hình nón (lớp 9)', CH, 'A conical palm-leaf hat has the shape of a cone.', ''),
 ('g9-lateral-area', 'lateral (surface) area', 'diện tích xung quanh (hình trụ, hình nón)', CH, 'The lateral area of a cylinder is 2πrh.', r'\(S_{xq}\)'),
 ('g9-net', 'net', 'hình khai triển (mặt xung quanh)', CH, 'The net of the lateral surface of a cylinder is a rectangle.', ''),
])
load_vocab()

def FIG(fn, cap, px=220): return '<figure class="mbl-fig mbl-figtex">%s<figcaption>%s</figcaption></figure>' % (sp_g9p.img(fn, cap[0], px), TI(*cap))
G, O_ = col('046b4d'), col('c2410c')
NET_CYL = texsvg('\n'.join(['\\begin{tikzpicture}',
  '\\draw[color=%s, line width=1pt, fill=%s, fill opacity=0.15] (0,0) rectangle (4.4,2.2);' % (G, col('86e0bd')),
  '\\draw[color=%s, line width=1pt] (2.2,2.9) circle (0.7); \\draw[color=%s, line width=1pt] (2.2,-0.7) circle (0.7);' % (G, G),
  '\\node[font=\\small, text=ink, below] at (1.1,0) {$2\\pi r$}; \\node[font=\\small, text=ink, right] at (4.4,1.1) {$h$};',
  '\\draw[color=%s, line width=1pt] (2.2,2.9) -- (2.9,2.9); \\node[font=\\small, text=ink, above] at (2.55,2.9) {$r$};' % O_, '\\end{tikzpicture}']))
NET_CONE = texsvg('\n'.join(['\\begin{tikzpicture}',
  '\\fill[color=%s, opacity=0.15] (0,0) -- (-35:2.6) arc[start angle=-35, end angle=-145, radius=2.6] -- cycle;' % col('86e0bd'),
  '\\draw[color=%s, line width=1pt] (0,0) -- (-35:2.6) arc[start angle=-35, end angle=-145, radius=2.6] -- cycle;' % G,
  '\\draw[color=%s, line width=1pt] (0,-3.75) circle (0.8);' % G,
  '\\node[font=\\small, text=ink, above right] at (-35:1.3) {$l$}; \\node[font=\\small, text=ink, above] at (0,-2.6) {$2\\pi r$};',
  '\\draw[color=%s, line width=1pt] (0,-3.75) -- (0.8,-3.75); \\node[font=\\small, text=ink, above] at (0.4,-3.75) {$r$};' % O_, '\\end{tikzpicture}']))

# ---------- số liệu (kiểm tra bằng máy) ----------
assert 2 * 3 * 10 == 60 and 3 * 3 * 10 == 90                     # VD2: r=3, h=10
assert 6 ** 2 + 8 ** 2 == 10 ** 2 and 6 * 10 == 60 and F(1, 3) * 36 * 8 == 96   # VD3: r=6, h=8, l=10
L5, A5 = 30, 144; r5 = F(L5 * A5, 360); assert r5 == 12 and 30 ** 2 - 12 ** 2 == 756          # VD5 (a)
h5 = math.sqrt(756); assert round(h5, 1) == 27.5
assert round(3.14 * 0.6 ** 2 * 1.5 * 1000) == 1696

meta = dict(level=('Basic', 'Cơ bản'), time=('about 90 minutes', '90 phút'), before=('Lesson 15: arc length; area of a disk', 'Bài 15: độ dài cung tròn; diện tích hình tròn'))
goals = [
 (r'recognize cylinders and cones and their elements (base, radius, height, generatrix, vertex);', r'nhận biết được hình trụ, hình nón và các yếu tố: đáy, bán kính đáy, chiều cao, đường sinh, đỉnh;'),
 (r'use \(S_{xq}=2\pi rh\), \(V=\pi r^2h\) (cylinder) and \(S_{xq}=\pi rl\), \(V=\dfrac13\pi r^2h\) (cone);', r'dùng được các công thức \(S_{xq}=2\pi rh\), \(V=\pi r^2h\) (hình trụ) và \(S_{xq}=\pi rl\), \(V=\dfrac13\pi r^2h\) (hình nón);'),
 (r'find the slant height with Pythagoras’ theorem;', r'tính được đường sinh bằng định lí Pythagore;'),
 (r'solve real problems (water tanks, conical hats, party hats from a sector).', r'giải được bài toán thực tế (bồn nước, nón lá, mũ sinh nhật cuộn từ hình quạt).')]
vocab = [
 (r'<b>cylinder</b> – obtained by rotating a rectangle one full turn about one side.', r'[[Hình trụ|hình trụ (lớp 9)]] – tạo thành khi quay một hình chữ nhật một vòng quanh một cạnh cố định.'),
 (r'<b>cone</b> – obtained by rotating a right triangle one full turn about one leg.', r'[[Hình nón|hình nón (lớp 9)]] – tạo thành khi quay một tam giác vuông một vòng quanh một cạnh góc vuông cố định.'),
 (r'<b>base, radius \(r\), height \(h\)</b> – the circular base(s), its radius, the distance between the bases (from the vertex to the base).', r'Đáy, bán kính đáy \(r\), chiều cao \(h\) – (các) hình tròn đáy, bán kính của nó, khoảng cách giữa hai đáy (từ đỉnh đến đáy).'),
 (r'<b>generatrix / slant height \(l\)</b> – a segment on the lateral surface joining the two bases (the vertex and the base circle).', r'[[Đường sinh]] \(l\) – đoạn thẳng trên mặt xung quanh nối hai đáy (nối đỉnh với đường tròn đáy).'),
 (r'<b>lateral area / volume / net</b> – area of the curved surface; space inside; the flat shape after cutting it open.', r'[[Diện tích xung quanh|diện tích xung quanh (hình trụ, hình nón)]] / [[thể tích]] / [[hình khai triển|hình khai triển (mặt xung quanh)]] – diện tích mặt cong; phần không gian bên trong; hình phẳng sau khi cắt và trải mặt xung quanh.')]
phrases = [
 (r'<b>The cylinder has base radius 3 cm and height 10 cm.</b>', r'Hình trụ có bán kính đáy 3 cm và chiều cao 10 cm.'),
 (r'<b>The lateral area of the cylinder is \(2\pi rh\).</b>', r'Diện tích xung quanh của hình trụ là \(2\pi rh\).'),
 (r'<b>Find the slant height of the cone.</b>', r'Tính độ dài đường sinh của hình nón.'),
 (r'<b>The volume of a cone is one third of the volume of a cylinder with the same base and height.</b>', r'Thể tích hình nón bằng một phần ba thể tích hình trụ có cùng đáy và chiều cao.'),
 (r'<b>Round the answer to one decimal place.</b>', r'Làm tròn kết quả đến hàng phần mười.')]
review = (T(r'<b>Grade 6–7.</b> A disk of radius \(r\): circumference \(2\pi r\), area \(\pi r^2\).', r'<b>Lớp 6–7.</b> Hình tròn bán kính \(r\): chu vi \(2\pi r\), diện tích \(\pi r^2\).') +
          T(r'<b>Lesson 15.</b> Arc of \(n^\circ\) on a circle of radius \(R\): length \(\dfrac{\pi Rn}{180}\).', r'<b>Bài 15.</b> Cung \(n^\circ\) của đường tròn bán kính \(R\) có độ dài \(\dfrac{\pi Rn}{180}\).'))

theory = '<h3>5.1 %s</h3>' % TI('The cylinder', 'Hình trụ')
theory += BOX('blue', ('Elements and formulas', 'Các yếu tố và công thức'),
  T(r'Rotating rectangle \(ABCD\) about the side \(AB\) gives a <b>cylinder</b>: \(AB\) is the axis, \(h=AB\) the height; the two bases are equal disks of radius \(r=BC\); each segment like \(CD\) is a <b>generatrix</b> (length \(h\)).', r'Quay hình chữ nhật \(ABCD\) một vòng quanh cạnh \(AB\) ta được [[hình trụ|hình trụ (lớp 9)]]: \(AB\) là trục, chiều cao \(h=AB\); hai đáy là hai hình tròn bằng nhau bán kính \(r=BC\); mỗi đoạn như \(CD\) là một [[đường sinh]] (dài bằng \(h\)).'),
  M(r'S_{xq}=2\pi rh,\qquad S_{tp}=2\pi rh+2\pi r^2,\qquad V=\pi r^2h'))
theory += '<div style="display:flex;flex-wrap:wrap;gap:10px;justify-content:center">%s%s</div>' % (
  FIG(Q.solid_svg('cyl'), ('Cylinder: radius \\(r\\), height \\(h\\).', 'Hình trụ: bán kính đáy \\(r\\), chiều cao \\(h\\).')),
  FIG(NET_CYL, ('Net: the lateral surface is a rectangle \\(2\\pi r\\times h\\).', 'Hình khai triển: mặt xung quanh là hình chữ nhật \\(2\\pi r\\times h\\).'), px=260))
theory += '<h3>5.2 %s</h3>' % TI('The cone', 'Hình nón')
theory += BOX('blue', ('Elements and formulas', 'Các yếu tố và công thức'),
  T(r'Rotating the right triangle \(AOC\) (right angle at \(O\)) about the leg \(AO\) gives a <b>cone</b>: \(A\) is the vertex, \(h=AO\) the height, \(r=OC\) the base radius, \(l=AC\) a <b>slant height</b> (generatrix), with \(l^2=r^2+h^2\).', r'Quay tam giác \(AOC\) vuông tại \(O\) một vòng quanh cạnh góc vuông \(AO\) ta được [[hình nón|hình nón (lớp 9)]]: \(A\) là đỉnh, chiều cao \(h=AO\), bán kính đáy \(r=OC\), \(l=AC\) là [[đường sinh]], \(l^2=r^2+h^2\).'),
  M(r'S_{xq}=\pi rl,\qquad S_{tp}=\pi rl+\pi r^2,\qquad V=\dfrac13\pi r^2h'))
theory += '<div style="display:flex;flex-wrap:wrap;gap:10px;justify-content:center">%s%s</div>' % (
  FIG(Q.solid_svg('cone'), ('Cone: radius \\(r\\), height \\(h\\), slant height \\(l\\).', 'Hình nón: bán kính đáy \\(r\\), chiều cao \\(h\\), đường sinh \\(l\\).')),
  FIG(NET_CONE, ('Net: the lateral surface is a sector of radius \\(l\\) and arc length \\(2\\pi r\\).', 'Hình khai triển: mặt xung quanh là hình quạt bán kính \\(l\\), độ dài cung \\(2\\pi r\\).'), px=200))
theory += BOX('yellow', ('Note', 'Chú ý'),
  T(r'A cone has one third of the volume of the cylinder with the same base and height.', r'Thể tích hình nón bằng một phần ba thể tích hình trụ có cùng đáy và cùng chiều cao.'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Naming the elements', 'Gọi tên các yếu tố'),
  T(r'Rectangle \(ABCD\) with \(AB=5\) cm and \(BC=2\) cm is rotated about \(AB\). Rotating triangle \(AOC\) (right angle at \(O\)) with \(AO=4\) cm, \(OC=3\) cm about \(AO\). Name the solids, their radius and height.', r'Quay hình chữ nhật \(ABCD\) có \(AB=5\) cm, \(BC=2\) cm quanh cạnh \(AB\). Quay tam giác \(AOC\) vuông tại \(O\) có \(AO=4\) cm, \(OC=3\) cm quanh cạnh \(AO\). Gọi tên các hình nhận được, bán kính đáy và chiều cao của chúng.'),
  ('The fixed side is the axis (height).', 'Cạnh cố định là trục (chiều cao).'),
  [T(r'Rectangle: a cylinder with \(r=2\) cm, \(h=5\) cm.', r'Hình chữ nhật: hình trụ có \(r=2\) cm, \(h=5\) cm.'), T(r'Triangle: a cone with \(r=3\) cm, \(h=4\) cm, slant height \(l=AC=5\) cm.', r'Tam giác: hình nón có \(r=3\) cm, \(h=4\) cm, đường sinh \(l=AC=5\) cm.')],
  T(r'A cylinder (2 cm; 5 cm) and a cone (3 cm; 4 cm).', r'Hình trụ (2 cm; 5 cm) và hình nón (3 cm; 4 cm).'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('A cylinder', 'Hình trụ'),
  T(r'A cylinder has base radius 3 cm and height 10 cm. Find its lateral area and its volume.', r'Một hình trụ có bán kính đáy 3 cm và chiều cao 10 cm. Tính diện tích xung quanh và thể tích.'),
  ('\\(S_{xq}=2\\pi rh\\), \\(V=\\pi r^2h\\).', '\\(S_{xq}=2\\pi rh\\), \\(V=\\pi r^2h\\).'),
  [T(r'\(S_{xq}=2\pi\cdot3\cdot10=60\pi\approx188.5\) cm².', r'\(S_{xq}=2\pi\cdot3\cdot10=60\pi\approx188{,}5\) cm².'), T(r'\(V=\pi\cdot3^2\cdot10=90\pi\approx282.7\) cm³.', r'\(V=\pi\cdot3^2\cdot10=90\pi\approx282{,}7\) cm³.')],
  T(r'\(60\pi\) cm²; \(90\pi\) cm³.', r'\(60\pi\) cm²; \(90\pi\) cm³.'))
examples += EXAMPLE(3, ('Basic application', 'Vận dụng thấp'), ('A cone', 'Hình nón'),
  T(r'A cone has base radius 6 cm and height 8 cm. Find its slant height, lateral area and volume.', r'Một hình nón có bán kính đáy 6 cm và chiều cao 8 cm. Tính đường sinh, diện tích xung quanh và thể tích.'),
  ('\\(l=\\sqrt{r^2+h^2}\\).', '\\(l=\\sqrt{r^2+h^2}\\).'),
  [T(r'\(l=\sqrt{6^2+8^2}=10\) cm; \(S_{xq}=\pi\cdot6\cdot10=60\pi\) cm².', r'\(l=\sqrt{6^2+8^2}=10\) cm; \(S_{xq}=\pi\cdot6\cdot10=60\pi\) cm².'), T(r'\(V=\dfrac13\pi\cdot6^2\cdot8=96\pi\) cm³.', r'\(V=\dfrac13\pi\cdot6^2\cdot8=96\pi\) cm³.')],
  T(r'10 cm; \(60\pi\) cm²; \(96\pi\) cm³.', r'10 cm; \(60\pi\) cm²; \(96\pi\) cm³.'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('A water tank', 'Bồn nước'),
  T(r'A cylindrical water tank has base radius 0.6 m and height 1.5 m. How many liters of water can it hold? (\(\pi\approx3.14\); round to the nearest liter.)', r'Một bồn nước hình trụ có bán kính đáy 0,6 m, chiều cao 1,5 m. Bồn chứa được bao nhiêu lít nước? (\(\pi\approx3{,}14\); làm tròn đến lít.)'),
  ('\\(1\\text{ m}^3=1000\\) liters.', '\\(1\\text{ m}^3=1000\\) lít.'),
  [T(r'\(V=\pi r^2h\approx3.14\cdot0.36\cdot1.5=1.6956\) m³ \(\approx1696\) liters.', r'\(V=\pi r^2h\approx3{,}14\cdot0{,}36\cdot1{,}5=1{,}6956\) m³ \(\approx1696\) lít.')],
  T(r'About 1696 liters.', r'Khoảng 1696 lít.'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('A party hat and a conical hat', 'Mũ sinh nhật và nón lá'),
  T(r'(a) A sector of radius 30 cm and arc \(144^\circ\) is rolled into a party hat (no overlap). Find the base radius and the height of the hat. (b) A conical palm-leaf hat has base radius 20 cm and slant height 30 cm. How much leaf area is needed for its lateral surface?', r'a) Cuộn một hình quạt bán kính 30 cm, số đo cung \(144^\circ\) thành chiếc mũ sinh nhật hình nón (không chồng mép). Tính bán kính đáy và chiều cao của mũ. b) Một chiếc nón lá có bán kính đáy 20 cm, đường sinh 30 cm. Cần bao nhiêu lá (tính theo diện tích) để phủ mặt xung quanh?'),
  ('(a) The arc of the sector becomes the base circle; the radius of the sector becomes the slant height.', 'a) Cung của hình quạt trở thành đường tròn đáy; bán kính hình quạt trở thành đường sinh.'),
  [T(r'(a) \(l=30\); \(2\pi r=\dfrac{\pi\cdot30\cdot144}{180}=24\pi\Rightarrow r=12\) cm; \(h=\sqrt{30^2-12^2}=\sqrt{756}\approx27.5\) cm.', r'a) \(l=30\); \(2\pi r=\dfrac{\pi\cdot30\cdot144}{180}=24\pi\Rightarrow r=12\) cm; \(h=\sqrt{30^2-12^2}=\sqrt{756}\approx27{,}5\) cm.'),
   T(r'(b) \(S_{xq}=\pi\cdot20\cdot30=600\pi\approx1885\) cm².', r'b) \(S_{xq}=\pi\cdot20\cdot30=600\pi\approx1885\) cm².')],
  T(r'(a) 12 cm; about 27.5 cm; (b) \(600\pi\approx1885\) cm².', r'a) 12 cm; khoảng 27,5 cm; b) \(600\pi\approx1885\) cm².'))
assert round(600 * math.pi) == 1885 and round(60 * math.pi, 1) == 188.5 and round(90 * math.pi, 1) == 282.7

_SETS = sp_g9.BANK(Q.L31_GROUPS, start=1, seeds=(3101, 3102, 3103))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Using the diameter as the radius.</b> Halve the diameter first.', r'<b>Dùng đường kính thay cho bán kính.</b> Phải chia đôi đường kính trước.'),
 (r'<b>Using the height instead of the slant height.</b> \(S_{xq}\) of a cone uses \(l\), not \(h\); \(l=\sqrt{r^2+h^2}\).', r'<b>Dùng chiều cao thay cho đường sinh.</b> \(S_{xq}\) của hình nón dùng \(l\), không dùng \(h\); \(l=\sqrt{r^2+h^2}\).'),
 (r'<b>Forgetting \(\dfrac13\).</b> \(V_{\text{cone}}=\dfrac13\pi r^2h\).', r'<b>Quên \(\dfrac13\).</b> \(V_{\text{nón}}=\dfrac13\pi r^2h\).'),
 (r'<b>Mixing units.</b> \(1\text{ m}^3=1000\) liters; cm² for area, cm³ for volume.', r'<b>Nhầm đơn vị.</b> \(1\text{ m}^3=1000\) lít; diện tích dùng cm², thể tích dùng cm³.')]
summary = [
 (r'Cylinder: \(S_{xq}=2\pi rh\), \(S_{tp}=2\pi rh+2\pi r^2\), \(V=\pi r^2h\).', r'Hình trụ: \(S_{xq}=2\pi rh\), \(S_{tp}=2\pi rh+2\pi r^2\), \(V=\pi r^2h\).'),
 (r'Cone: \(l^2=r^2+h^2\), \(S_{xq}=\pi rl\), \(V=\dfrac13\pi r^2h\).', r'Hình nón: \(l^2=r^2+h^2\), \(S_{xq}=\pi rl\), \(V=\dfrac13\pi r^2h\).'),
 (r'Nets: cylinder → rectangle \(2\pi r\times h\); cone → sector of radius \(l\), arc \(2\pi r\).', r'Hình khai triển: hình trụ → hình chữ nhật \(2\pi r\times h\); hình nón → hình quạt bán kính \(l\), cung dài \(2\pi r\).'),
 (r'Key English: cylinder, cone, base, height, slant height (generatrix), lateral area, volume, net.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[hình trụ|hình trụ (lớp 9)]], [[hình nón|hình nón (lớp 9)]], [[đường sinh]], [[diện tích xung quanh|diện tích xung quanh (hình trụ, hình nón)]], [[thể tích]], [[hình khai triển|hình khai triển (mặt xung quanh)]].')]
checks = [
 (r'I can name the elements of a cylinder and a cone.', r'Em gọi tên được các yếu tố của hình trụ, hình nón.'),
 (r'I can compute lateral areas and volumes.', r'Em tính được diện tích xung quanh và thể tích.'),
 (r'I can find the slant height of a cone.', r'Em tính được đường sinh của hình nón.'),
 (r'I can solve real problems with cylinders and cones.', r'Em giải được bài toán thực tế về hình trụ, hình nón.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Cylinders and Cones', title_vi='Hình trụ và hình nón', topic=TOPIC,
       folder='solids', file='cylinders-cones', catalog_title_vi='Hình trụ và hình nón',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Cylinders and cones: elements, lateral area, total area and volume; slant height; nets; real problems.', level='Basic', minutes=90,
       description_vi='Bài 31 – Hình trụ, hình nón: các yếu tố, diện tích xung quanh, thể tích, đường sinh, hình khai triển, bài toán thực tế.',
       tags_vi=['hình trụ', 'hình nón', 'thể tích'], prerequisites=['g9-circles-03'], tags=['cylinder', 'cone', 'volume'], order=310)
