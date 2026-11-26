# -*- coding: utf-8 -*-
"""Nội dung bài g9-solids-02 = Toán 9 KNTT, Bài 32: Hình cầu – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 10 – Lesson 32. Quy ước Q5: sphere → hình cầu; surface of a sphere → mặt cầu."""
import os, sys, math
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9, sp_g9p, sp_g9q as Q
from mb_pgf import texsvg, col

LID = 'g9-solids-02'
CH = 'Một số hình khối trong thực tiễn'
TOPIC = ('Solid Shapes in Everyday Life', CH)
ensure_vocab([
 ('g9-sphere', 'sphere (solid sphere, ball)', 'hình cầu (lớp 9)', CH, 'A football has the shape of a sphere.', ''),
 ('g9-sphere-surface', 'surface of a sphere', 'mặt cầu (bề mặt hình cầu)', CH, 'The area of the surface of a sphere is 4πR².', ''),
 ('g9-great-circle', 'great circle', 'đường tròn lớn (mặt cầu)', CH, 'The equator is a great circle of the Earth.', ''),
 ('g9-hemisphere', 'hemisphere', 'nửa hình cầu (lớp 9)', CH, 'The dome is a hemisphere.', ''),
 ('g9-cross-section', 'cross-section', 'mặt cắt (của hình cầu)', CH, 'Every cross-section of a ball is a disk.', ''),
])
load_vocab()

def FIG(fn, cap, px=220): return '<figure class="mbl-fig mbl-figtex">%s<figcaption>%s</figcaption></figure>' % (sp_g9p.img(fn, cap[0], px), TI(*cap))
G, O_ = col('046b4d'), col('c2410c')
SECT = texsvg('\n'.join(['\\begin{tikzpicture}',
  '\\draw[color=%s, line width=1pt] (0,0) circle (1.6);' % G,
  '\\fill[color=%s, opacity=0.25] (0,0.8) ellipse (1.386 and 0.32);' % col('fdba74'),
  '\\draw[color=%s, line width=0.9pt] (-1.386,0.8) arc[start angle=180, end angle=360, x radius=1.386cm, y radius=0.32cm];' % O_,
  '\\draw[color=%s, line width=0.7pt, dash pattern=on 3pt off 2.5pt] (1.386,0.8) arc[start angle=0, end angle=180, x radius=1.386cm, y radius=0.32cm];' % O_,
  '\\draw[ink, line width=0.7pt, dash pattern=on 3pt off 2.5pt] (0,0) -- (0,0.8); \\draw[ink, line width=0.8pt] (0,0) -- (1.386,0.8); \\draw[ink, line width=0.8pt] (0,0.8) -- (1.386,0.8);',
  '\\fill[ink] (0,0) circle (1.4pt); \\fill[ink] (0,0.8) circle (1.4pt);',
  '\\node[font=\\small, text=ink, below] at (0,0) {$O$}; \\node[font=\\small, text=ink, left] at (0,0.4) {$d$};',
  '\\node[font=\\small, text=ink, below right] at (0.62,0.45) {$R$}; \\node[font=\\small, text=ink, above] at (0.7,0.8) {$r$};',
  '\\draw[ink, line width=0.6pt] (0,0.62) -- (0.18,0.62) -- (0.18,0.8);', '\\end{tikzpicture}']))
assert abs(math.hypot(1.386, 0.8) - 1.6) < 1e-3

# ---------- số liệu (kiểm tra bằng máy) ----------
assert 4 * 3 ** 2 == 36 and F(4, 3) * 27 == 36            # VD2: R = 3
assert 5 ** 2 - 3 ** 2 == 16                                # VD3: R = 5, d = 3 → r = 4
assert F(2, 3) * 27 == 18 and 3 * 9 == 27                   # VD4: nửa hình cầu R = 3
R5 = 3; cyl = R5 * R5 * 2 * R5; ball = F(4, 3) * R5 ** 3; assert cyl == 54 and ball == 36 and ball / cyl == F(2, 3)
tank = 3 ** 2 * 10 + F(4, 3) * 27; assert tank == 126

meta = dict(level=('Basic', 'Cơ bản'), time=('about 90 minutes', '90 phút'), before=('Lesson 31: cylinders and cones', 'Bài 31: hình trụ, hình nón'))
goals = [
 (r'recognize a sphere (ball), its surface, center, radius; know that every cross-section is a disk;', r'nhận biết được hình cầu, mặt cầu, tâm, bán kính; biết mặt cắt của hình cầu là hình tròn;'),
 (r'use \(S=4\pi R^2\) and \(V=\dfrac43\pi R^3\);', r'dùng được các công thức \(S=4\pi R^2\) và \(V=\dfrac43\pi R^3\);'),
 (r'compute areas and volumes of spheres and hemispheres;', r'tính được diện tích mặt cầu, thể tích hình cầu, nửa hình cầu;'),
 (r'solve combined problems (a ball in a box, a tank made of a cylinder and two hemispheres).', r'giải được bài toán kết hợp (quả bóng trong hộp hình trụ, bồn chứa gồm hình trụ và hai nửa hình cầu).')]
vocab = [
 (r'<b>sphere (solid sphere, ball)</b> – obtained by rotating a semicircle (half-disk) about its diameter.', r'[[Hình cầu|hình cầu (lớp 9)]] – tạo thành khi quay nửa hình tròn một vòng quanh đường kính của nó.'),
 (r'<b>surface of a sphere</b> – the points at distance \(R\) from the center \(O\).', r'[[Mặt cầu|mặt cầu (bề mặt hình cầu)]] – các điểm cách tâm \(O\) một khoảng bằng \(R\).'),
 (r'<b>center, radius, diameter</b> – \(O\), \(R\), \(2R\).', r'Tâm, bán kính, đường kính – \(O\), \(R\), \(2R\).'),
 (r'<b>cross-section / great circle</b> – the cut by a plane (a disk); the circle cut by a plane through \(O\).', r'[[Mặt cắt|mặt cắt (của hình cầu)]] / [[đường tròn lớn|đường tròn lớn (mặt cầu)]] – phần cắt bởi một mặt phẳng (hình tròn); đường tròn cắt bởi mặt phẳng đi qua \(O\).'),
 (r'<b>hemisphere</b> – half of a ball cut by a plane through the center.', r'[[Nửa hình cầu|nửa hình cầu (lớp 9)]] – một nửa hình cầu bị cắt bởi mặt phẳng đi qua tâm.')]
phrases = [
 (r'<b>The ball has radius 3 cm.</b>', r'Hình cầu có bán kính 3 cm.'),
 (r'<b>The area of the surface of the sphere is \(4\pi R^2\).</b>', r'Diện tích mặt cầu là \(4\pi R^2\).'),
 (r'<b>The volume of the ball is \(\dfrac43\pi R^3\).</b>', r'Thể tích hình cầu là \(\dfrac43\pi R^3\).'),
 (r'<b>A plane cuts the sphere in a circle.</b>', r'Mặt phẳng cắt mặt cầu theo một đường tròn.'),
 (r'<b>The dome has the shape of a hemisphere.</b>', r'Mái vòm có dạng nửa hình cầu.')]
review = (T(r'<b>Lesson 31.</b> Cylinder: \(V=\pi r^2h\).', r'<b>Bài 31.</b> Hình trụ: \(V=\pi r^2h\).') +
          T(r'<b>Pythagoras.</b> \(R^2=d^2+r^2\) in a right triangle with hypotenuse \(R\).', r'<b>Định lí Pythagore.</b> \(R^2=d^2+r^2\) trong tam giác vuông có cạnh huyền \(R\).'))

theory = '<h3>5.1 %s</h3>' % TI('The sphere', 'Hình cầu')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'Rotating a half-disk one full turn about its diameter \(AB\) gives a <b>ball</b> (a sphere); its boundary is the <b>surface of the sphere</b>. The midpoint \(O\) of \(AB\) is the center, \(R=OA\) the radius.', r'Quay nửa hình tròn một vòng quanh đường kính \(AB\) cố định ta được một [[hình cầu|hình cầu (lớp 9)]]; phần mặt bao quanh là [[mặt cầu|mặt cầu (bề mặt hình cầu)]]. Trung điểm \(O\) của \(AB\) là tâm, \(R=OA\) là bán kính.'),
  T(r'Every plane cutting the ball gives a <b>disk</b>. If the plane is at distance \(d\lt R\) from \(O\), the radius of the cross-section is \(r=\sqrt{R^2-d^2}\); if it passes through \(O\) we get a <b>great circle</b> (radius \(R\)).', r'Mọi mặt phẳng cắt hình cầu đều cho mặt cắt là một <b>hình tròn</b>. Nếu mặt phẳng cách \(O\) một khoảng \(d\lt R\) thì bán kính mặt cắt là \(r=\sqrt{R^2-d^2}\); nếu mặt phẳng đi qua \(O\) ta được [[đường tròn lớn|đường tròn lớn (mặt cầu)]] (bán kính \(R\)).'))
theory += '<div style="display:flex;flex-wrap:wrap;gap:10px;justify-content:center">%s%s</div>' % (
  FIG(Q.solid_svg('sph', ('R',)), ('A sphere with center \\(O\\) and radius \\(R\\) (the hidden half of the equator is dashed).', 'Hình cầu tâm \\(O\\), bán kính \\(R\\) (nửa khuất của đường xích đạo vẽ nét đứt).')),
  FIG(SECT, ('Cross-section at distance \\(d\\): \\(r=\\sqrt{R^2-d^2}\\).', 'Mặt cắt cách tâm \\(d\\): \\(r=\\sqrt{R^2-d^2}\\).')))
theory += '<h3>5.2 %s</h3>' % TI('Surface area and volume', 'Diện tích mặt cầu và thể tích hình cầu')
theory += BOX('mint', ('Formulas', 'Công thức'), M(r'S=4\pi R^2\qquad V=\dfrac43\pi R^3'),
  T(r'Hemisphere: curved surface \(2\pi R^2\), volume \(\dfrac23\pi R^3\).', r'Nửa hình cầu: mặt cong \(2\pi R^2\), thể tích \(\dfrac23\pi R^3\).'))
theory += BOX('yellow', ('Note', 'Chú ý'),
  T(r'A ball fitting exactly in a cylinder (radius \(R\), height \(2R\)) fills \(\dfrac{\frac43\pi R^3}{2\pi R^3}=\dfrac23\) of it.', r'Hình cầu đặt vừa khít trong hình trụ (bán kính \(R\), chiều cao \(2R\)) chiếm \(\dfrac{\frac43\pi R^3}{2\pi R^3}=\dfrac23\) thể tích hình trụ.'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Sphere or not?', 'Hình cầu?'),
  T(r'Which objects have the shape of a sphere: a football, a can of milk, an orange, a conical hat? A plane through the center of a ball of radius 5 cm cuts it; what is the cross-section?', r'Vật nào có dạng hình cầu: quả bóng đá, hộp sữa, quả cam, chiếc nón lá? Một mặt phẳng đi qua tâm cắt hình cầu bán kính 5 cm; mặt cắt là hình gì?'),
  ('Cans are cylinders, conical hats are cones.', 'Hộp sữa là hình trụ, nón lá là hình nón.'),
  [T(r'The football and the orange. The cross-section is a disk bounded by a great circle of radius 5 cm.', r'Quả bóng đá và quả cam. Mặt cắt là hình tròn giới hạn bởi đường tròn lớn bán kính 5 cm.')],
  T(r'Football, orange; a disk of radius 5 cm.', r'Quả bóng đá, quả cam; hình tròn bán kính 5 cm.'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Area and volume', 'Diện tích và thể tích'),
  T(r'A ball has radius 3 cm. Find the area of its surface and its volume.', r'Một hình cầu có bán kính 3 cm. Tính diện tích mặt cầu và thể tích hình cầu.'),
  ('\\(S=4\\pi R^2\\), \\(V=\\dfrac43\\pi R^3\\).', '\\(S=4\\pi R^2\\), \\(V=\\dfrac43\\pi R^3\\).'),
  [T(r'\(S=4\pi\cdot9=36\pi\approx113.1\) cm².', r'\(S=4\pi\cdot9=36\pi\approx113{,}1\) cm².'), T(r'\(V=\dfrac43\pi\cdot27=36\pi\approx113.1\) cm³.', r'\(V=\dfrac43\pi\cdot27=36\pi\approx113{,}1\) cm³.')],
  T(r'\(36\pi\) cm²; \(36\pi\) cm³.', r'\(36\pi\) cm²; \(36\pi\) cm³.'))
examples += EXAMPLE(3, ('Basic application', 'Vận dụng thấp'), ('A cross-section', 'Mặt cắt'),
  T(r'A ball of radius 5 cm is cut by a plane at distance 3 cm from its center. Find the radius and the area of the cross-section.', r'Một hình cầu bán kính 5 cm bị cắt bởi mặt phẳng cách tâm 3 cm. Tính bán kính và diện tích mặt cắt.'),
  ('\\(r=\\sqrt{R^2-d^2}\\).', '\\(r=\\sqrt{R^2-d^2}\\).'),
  [T(r'\(r=\sqrt{5^2-3^2}=4\) cm; area \(\pi\cdot4^2=16\pi\) cm².', r'\(r=\sqrt{5^2-3^2}=4\) cm; diện tích \(\pi\cdot4^2=16\pi\) cm².')],
  T(r'4 cm; \(16\pi\) cm².', r'4 cm; \(16\pi\) cm².'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('A hemisphere bowl', 'Cái bát nửa hình cầu'),
  T(r'A bowl has the shape of a hemisphere of radius 3 dm. (a) How many liters of water can it hold? (b) Find the area of its inside surface. (\(1\text{ dm}^3=1\) liter.)', r'Một cái bát có dạng nửa hình cầu bán kính 3 dm. a) Bát chứa được bao nhiêu lít nước? b) Tính diện tích mặt trong của bát. (\(1\text{ dm}^3=1\) lít.)'),
  ('Half of the ball, half of the sphere surface.', 'Một nửa thể tích hình cầu, một nửa diện tích mặt cầu.'),
  [T(r'(a) \(V=\dfrac23\pi\cdot3^3=18\pi\approx56.5\) liters.', r'a) \(V=\dfrac23\pi\cdot3^3=18\pi\approx56{,}5\) lít.'), T(r'(b) \(S=2\pi\cdot3^2=18\pi\approx56.5\) dm².', r'b) \(S=2\pi\cdot3^2=18\pi\approx56{,}5\) dm².')],
  T(r'(a) about 56.5 liters; (b) about 56.5 dm².', r'a) khoảng 56,5 lít; b) khoảng 56,5 dm².'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('A ball in a box; a gas tank', 'Bóng trong hộp; bồn chứa'),
  T(r'(a) A ball of radius 3 cm fits exactly in a cylindrical box. What fraction of the box is empty? (b) A gas tank is a cylinder of radius 3 dm and length 10 dm with a hemisphere of radius 3 dm at each end. Find its volume.', r'a) Một quả bóng bán kính 3 cm đặt vừa khít trong hộp hình trụ. Phần trống chiếm bao nhiêu phần thể tích hộp? b) Một bồn chứa gồm hình trụ bán kính 3 dm, dài 10 dm và hai nửa hình cầu bán kính 3 dm ở hai đầu. Tính thể tích bồn.'),
  ('The box has radius 3 and height 6; two hemispheres make one ball.', 'Hộp có bán kính 3, chiều cao 6; hai nửa hình cầu ghép thành một hình cầu.'),
  [T(r'(a) Box \(\pi\cdot9\cdot6=54\pi\), ball \(36\pi\); empty \(18\pi\), that is \(\dfrac{18}{54}=\dfrac13\) of the box.', r'a) Hộp \(\pi\cdot9\cdot6=54\pi\), bóng \(36\pi\); phần trống \(18\pi\), tức \(\dfrac{18}{54}=\dfrac13\) hộp.'),
   T(r'(b) \(V=\pi\cdot3^2\cdot10+\dfrac43\pi\cdot3^3=90\pi+36\pi=126\pi\approx395.8\) dm³.', r'b) \(V=\pi\cdot3^2\cdot10+\dfrac43\pi\cdot3^3=90\pi+36\pi=126\pi\approx395{,}8\) dm³.')],
  T(r'(a) \(\dfrac13\); (b) \(126\pi\approx395.8\) dm³.', r'a) \(\dfrac13\); b) \(126\pi\approx395{,}8\) dm³.'))
assert round(36 * math.pi, 1) == 113.1 and round(18 * math.pi, 1) == 56.5 and round(126 * math.pi, 1) == 395.8

_SETS = sp_g9.BANK(Q.L32_GROUPS, start=1, seeds=(3201, 3202, 3203))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Using the diameter in the formulas.</b> \(S=4\pi R^2\) uses the radius.', r'<b>Dùng đường kính trong công thức.</b> \(S=4\pi R^2\) dùng bán kính.'),
 (r'<b>Swapping \(R^2\) and \(R^3\).</b> Area: \(R^2\) (cm²); volume: \(R^3\) (cm³).', r'<b>Nhầm \(R^2\) và \(R^3\).</b> Diện tích: \(R^2\) (cm²); thể tích: \(R^3\) (cm³).'),
 (r'<b>Forgetting the flat face of a solid hemisphere.</b> Total surface \(2\pi R^2+\pi R^2=3\pi R^2\).', r'<b>Quên mặt đáy phẳng của khối nửa hình cầu.</b> Diện tích toàn phần \(2\pi R^2+\pi R^2=3\pi R^2\).'),
 (r'<b>Wrong scaling.</b> Doubling \(R\) multiplies the area by 4 and the volume by 8.', r'<b>Sai khi phóng to.</b> Gấp đôi \(R\) thì diện tích gấp 4, thể tích gấp 8.')]
summary = [
 (r'Sphere (ball) of center \(O\), radius \(R\); every cross-section is a disk, \(r=\sqrt{R^2-d^2}\).', r'Hình cầu tâm \(O\), bán kính \(R\); mọi mặt cắt là hình tròn, \(r=\sqrt{R^2-d^2}\).'),
 (r'\(S=4\pi R^2\), \(V=\dfrac43\pi R^3\); hemisphere: \(2\pi R^2\), \(\dfrac23\pi R^3\).', r'\(S=4\pi R^2\), \(V=\dfrac43\pi R^3\); nửa hình cầu: \(2\pi R^2\), \(\dfrac23\pi R^3\).'),
 (r'A ball in a cylinder of the same width and height \(2R\) fills \(\dfrac23\) of it.', r'Hình cầu vừa khít trong hình trụ cao \(2R\) chiếm \(\dfrac23\) thể tích hình trụ.'),
 (r'Key English: sphere, surface of a sphere, great circle, cross-section, hemisphere.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[hình cầu|hình cầu (lớp 9)]], [[mặt cầu|mặt cầu (bề mặt hình cầu)]], [[đường tròn lớn|đường tròn lớn (mặt cầu)]], [[mặt cắt|mặt cắt (của hình cầu)]], [[nửa hình cầu|nửa hình cầu (lớp 9)]].')]
checks = [
 (r'I can recognize spheres and their elements.', r'Em nhận biết được hình cầu và các yếu tố của nó.'),
 (r'I can compute the area of a sphere and the volume of a ball.', r'Em tính được diện tích mặt cầu và thể tích hình cầu.'),
 (r'I can compute with hemispheres and cross-sections.', r'Em tính được với nửa hình cầu và mặt cắt.'),
 (r'I can solve combined real problems.', r'Em giải được bài toán thực tế kết hợp nhiều hình.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Spheres', title_vi='Hình cầu', topic=TOPIC,
       folder='solids', file='spheres', catalog_title_vi='Hình cầu',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Spheres: elements, cross-sections, surface area 4πR², volume 4/3πR³, hemispheres and combined solids.', level='Basic', minutes=90,
       description_vi='Bài 32 – Hình cầu, mặt cầu, mặt cắt; diện tích mặt cầu, thể tích hình cầu, nửa hình cầu; bài toán kết hợp.',
       tags_vi=['hình cầu', 'mặt cầu', 'thể tích'], prerequisites=['g9-solids-01'], tags=['sphere', 'surface area', 'volume'], order=320)
