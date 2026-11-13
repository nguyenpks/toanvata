# -*- coding: utf-8 -*-
"""Nội dung bài g9-circles-03 = Toán 9 KNTT, Bài 15: Độ dài của cung tròn. Diện tích hình quạt tròn và hình vành khuyên – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 5 – Lesson 15; giáo án mẫu Bài 15."""
import os, sys, math
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9

LID = 'g9-circles-03'
CH = 'Đường tròn'
TOPIC = ('Circles', CH)
ensure_vocab([
 ('g9-circumference', 'circumference', 'độ dài đường tròn (chu vi)', CH, 'The circumference of a circle of radius R is 2πR.', r'\(C=2\pi R\)'),
 ('g9-sector', 'sector', 'hình quạt tròn', CH, 'A sector is bounded by two radii and an arc.', ''),
 ('g9-sector-area', 'sector area', 'diện tích hình quạt tròn', CH, 'Sector area: S = πR²n/360.', ''),
 ('g9-annulus', 'annulus (pl. annuli)', 'hình vành khuyên', CH, 'An annulus is the region between two concentric circles.', ''),
 ('g9-concentric', 'concentric circles', 'hai đường tròn đồng tâm', CH, 'Two circles with the same center are concentric circles.', ''),
 ('g9-slant-height', 'slant height', 'đường sinh', CH, 'The radius of the sector becomes the slant height of the cone.', ''),
])
load_vocab()

# ---------- kiểm tra số liệu ----------
assert F(9 * 80, 180) == 4 and F(81 * 80, 360) == 18
assert F(12 * 150, 180) == 10 and F(144 * 150, 360) == 60 and F(150, 360) == F(5, 12)
assert F(180 * 8, 72) == 20 and F(8 * 20, 2) == 80
S4 = 3.14 * (6.5 ** 2 - 5 ** 2); assert abs(S4 - 54.165) < 1e-9 and abs(S4 * 240000 - 12999600) < 1e-3
assert F(18 * 120, 180) == 12 and F(18 * 18 * 120, 360) == 108

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 75 minutes', '75 phút'),
            before=('Lesson 14: arcs; grades 6–7: circumference and area of a circle', 'Bài 14: cung; lớp 6–7: chu vi, diện tích hình tròn'))
goals = [
 (r'use the formula for the length of an arc;', r'vận dụng được công thức tính độ dài cung tròn;'),
 (r'use the formulas for the area of a sector and of an annulus;', r'vận dụng được công thức tính diện tích hình quạt tròn và hình vành khuyên;'),
 (r'solve reverse problems (find the radius or the angle);', r'giải được bài toán ngược (tìm bán kính hoặc số đo cung);'),
 (r'solve real-life problems: garden paths, paving costs, paper fans, party hats.', r'giải được bài toán thực tế: lối đi quanh vườn, chi phí lát nền, quạt giấy, mũ sinh nhật.')]
vocab = [
 (r'<b>circumference</b> – the length of the whole circle, \(C=2\pi R\).', r'[[Độ dài đường tròn (chu vi)|độ dài đường tròn (chu vi)]] – \(C=2\pi R\).'),
 (r'<b>arc length</b> – the length of an arc of \(n^\circ\): \(l=\dfrac{\pi Rn}{180}\).', r'[[Độ dài cung]] \(n^\circ\): \(l=\dfrac{\pi Rn}{180}\).'),
 (r'<b>sector</b> – the region bounded by two radii and the arc between them.', r'[[Hình quạt tròn]] – phần hình tròn giới hạn bởi hai bán kính và cung nằm giữa chúng.'),
 (r'<b>annulus</b> – the region between two <b>concentric circles</b>.', r'[[Hình vành khuyên]] – phần nằm giữa [[hai đường tròn đồng tâm]].'),
 (r'<b>slant height</b> – the radius of the sector becomes the slant height of the cone.', r'[[Đường sinh]] – bán kính hình quạt trở thành đường sinh của hình nón.')]
phrases = [
 (r'<b>The arc represents \(\dfrac{n}{360}\) of the full circumference.</b>', r'Cung chiếm \(\dfrac{n}{360}\) độ dài cả đường tròn.'),
 (r'<b>The sector represents \(\dfrac{n}{360}\) of the full circle.</b>', r'Hình quạt chiếm \(\dfrac{n}{360}\) diện tích cả hình tròn.'),
 (r'<b>Leave your answer in terms of \(\pi\).</b>', r'Để kết quả dưới dạng có chứa \(\pi\).'),
 (r'<b>When a sector is rolled into a cone, its arc becomes the circumference of the base.</b>', r'Khi cuộn hình quạt thành hình nón, cung trở thành đường tròn đáy.'),
 (r'<b>Use \(\pi\approx3.14\).</b>', r'Lấy \(\pi\approx3{,}14\).')]
review = (T(r'<b>Circle.</b> Circumference \(C=2\pi R\); area \(S=\pi R^2\).', r'<b>Hình tròn.</b> Chu vi \(C=2\pi R\); diện tích \(S=\pi R^2\).') +
          T(r'<b>Lesson 14.</b> A whole circle measures \(360^\circ\).', r'<b>Bài 14.</b> Cả đường tròn có số đo \(360^\circ\).'))

G = lambda cfg, en, vi, hgt=280: GEO(sp_g9.auto_labels(cfg), cap=(en, vi), alt=(en, ''), height=hgt)
def pt(i, x, y, name=None, size=3): return {'type': 'point', 'id': i, 'at': [round(x, 4), round(y, 4)], 'name': i if name is None else name, 'style': {'size': size}}
def seg(a, b, **st): return {'type': 'segment', 'through': [a, b], 'style': st}
def txt(x, y, s): return {'type': 'text', 'at': [x, y], 'text': s}
def on(R, deg): return (R * math.cos(math.radians(deg)), R * math.sin(math.radians(deg)))
R = 2.4
FIG1 = G({'view': [-3.2, 3.2, -2.9, 2.9], 'steps': [pt('O', 0, 0), pt('A', *on(R, 15)), pt('B', *on(R, 115)), {'type': 'circle', 'center': 'O', 'radius': R},
          seg('O', 'A', strokeWidth=3), seg('O', 'B', strokeWidth=3), {'type': 'arc', 'points': ['O', 'A', 'B']}, {'type': 'angle', 'points': ['A', 'O', 'B'], 'radius': 0.6, 'label': 'n^\\circ'},
          txt(1.25, -0.05, 'R')]},
         'Sector OAB with radius R and central angle n°; the orange arc AB has length πRn/180.', 'Hình quạt OAB bán kính R, góc ở tâm n°; cung AB (màu cam) có độ dài πRn/180.')
FIG2 = G({'view': [-3.2, 3.2, -2.9, 2.9], 'steps': [pt('O', 0, 0), pt('P', *on(R, 25), name='', size=0), pt('Q', *on(1.3, 140), name='', size=0),
          {'type': 'circle', 'center': 'O', 'radius': R, 'style': {'fillOpacity': 0.35}}, {'type': 'circle', 'center': 'O', 'radius': 1.3, 'style': {'fillOpacity': 1, 'fillColor': 'ffffff'}},
          seg('O', 'P'), seg('O', 'Q'), txt(1.55, 1.12, 'R'), txt(-0.65, 0.2, 'r')]},
         'An annulus: the region between two concentric circles with radii R and r.', 'Hình vành khuyên: phần nằm giữa hai đường tròn đồng tâm bán kính R và r.')

theory = '<h3>5.1 %s</h3>' % TI('Arc length', 'Độ dài của cung tròn')
theory += BOX('blue', ('Formula', 'Công thức'),
  T(r'The circumference of \((O;\,R)\) is \(C=2\pi R\). An arc of \(n^\circ\) is \(\dfrac{n}{360}\) of the circle, so its length is', r'Độ dài đường tròn \((O;\,R)\) là \(C=2\pi R\). Cung \(n^\circ\) chiếm \(\dfrac{n}{360}\) đường tròn nên có độ dài'),
  M(r'l=\dfrac{\pi Rn}{180}'))
theory += FIG1
theory += '<h3>5.2 %s</h3>' % TI('Area of a sector', 'Diện tích hình quạt tròn')
theory += BOX('mint', ('Formula', 'Công thức'),
  T(r'A <b>sector</b> is bounded by two radii and an arc. A sector with central angle \(n^\circ\) has area', r'[[Hình quạt tròn]] giới hạn bởi hai bán kính và một cung. Hình quạt có góc ở tâm \(n^\circ\) có diện tích'),
  M(r'S=\dfrac{\pi R^2n}{360}=\dfrac{lR}{2}'),
  T(r'Both \(l\) and \(S\) are proportional to \(n\) when \(R\) is fixed.', r'Khi \(R\) không đổi, \(l\) và \(S\) đều tỉ lệ thuận với \(n\).'))
theory += '<h3>5.3 %s</h3>' % TI('Area of an annulus', 'Diện tích hình vành khuyên')
theory += FIG2
theory += BOX('yellow', ('Formula', 'Công thức'),
  T(r'The <b>annulus</b> between two concentric circles of radii \(R\gt r\) has area', r'[[Hình vành khuyên]] giới hạn bởi [[hai đường tròn đồng tâm]] bán kính \(R\gt r\) có diện tích'),
  M(r'S=\pi R^2-\pi r^2=\pi\left(R^2-r^2\right)'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Using the formulas', 'Áp dụng công thức'),
  T(r'A circle has radius 9 cm. Find a) its circumference; b) the length of an arc of \(80^\circ\); c) the area of the sector of \(80^\circ\). Leave answers in terms of \(\pi\).', r'Một đường tròn có bán kính 9 cm. Tính a) độ dài đường tròn; b) độ dài cung \(80^\circ\); c) diện tích hình quạt tròn \(80^\circ\). Để kết quả dưới dạng có chứa \(\pi\).'),
  ('\\(R=9\\), \\(n=80\\).', '\\(R=9\\), \\(n=80\\).'),
  [T(r'a) \(C=2\pi\cdot9=18\pi\) cm. b) \(l=\dfrac{\pi\cdot9\cdot80}{180}=4\pi\) cm.', r'a) \(C=2\pi\cdot9=18\pi\) cm. b) \(l=\dfrac{\pi\cdot9\cdot80}{180}=4\pi\) cm.'),
   T(r'c) \(S=\dfrac{\pi\cdot9^2\cdot80}{360}=18\pi\) cm².', r'c) \(S=\dfrac{\pi\cdot9^2\cdot80}{360}=18\pi\) cm².')],
  T(r'\(18\pi\) cm; \(4\pi\) cm; \(18\pi\) cm².', r'\(18\pi\) cm; \(4\pi\) cm; \(18\pi\) cm².'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('A sector', 'Hình quạt tròn'),
  T(r'A sector has radius 12 cm and central angle \(150^\circ\). Find its arc length, its area and the fraction of the whole disk it occupies.', r'Một hình quạt tròn có bán kính 12 cm, góc ở tâm \(150^\circ\). Tính độ dài cung, diện tích hình quạt và cho biết hình quạt chiếm bao nhiêu phần hình tròn.'),
  ('Fraction \\(=\\dfrac{n}{360}\\).', 'Phần chiếm \\(=\\dfrac{n}{360}\\).'),
  [T(r'\(l=\dfrac{\pi\cdot12\cdot150}{180}=10\pi\) cm; \(S=\dfrac{lR}{2}=\dfrac{10\pi\cdot12}{2}=60\pi\) cm².', r'\(l=\dfrac{\pi\cdot12\cdot150}{180}=10\pi\) cm; \(S=\dfrac{lR}{2}=\dfrac{10\pi\cdot12}{2}=60\pi\) cm².'),
   T(r'Fraction: \(\dfrac{150}{360}=\dfrac{5}{12}\).', r'Phần chiếm: \(\dfrac{150}{360}=\dfrac{5}{12}\).')],
  T(r'\(10\pi\) cm; \(60\pi\) cm²; \(\dfrac{5}{12}\).', r'\(10\pi\) cm; \(60\pi\) cm²; \(\dfrac{5}{12}\).'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('Reverse reasoning', 'Bài toán ngược'),
  T(r'An arc of \(72^\circ\) has length \(8\pi\) cm. Find the radius and the area of the corresponding sector.', r'Một cung \(72^\circ\) có độ dài \(8\pi\) cm. Tính bán kính đường tròn và diện tích hình quạt tương ứng.'),
  ('Solve \\(\\dfrac{\\pi R\\cdot72}{180}=8\\pi\\).', 'Giải \\(\\dfrac{\\pi R\\cdot72}{180}=8\\pi\\).'),
  [T(r'\(\dfrac{\pi R\cdot72}{180}=8\pi\Rightarrow R=\dfrac{180\cdot8}{72}=20\) cm.', r'\(\dfrac{\pi R\cdot72}{180}=8\pi\Rightarrow R=\dfrac{180\cdot8}{72}=20\) cm.'),
   T(r'\(S=\dfrac{lR}{2}=\dfrac{8\pi\cdot20}{2}=80\pi\) cm².', r'\(S=\dfrac{lR}{2}=\dfrac{8\pi\cdot20}{2}=80\pi\) cm².')],
  T(r'\(R=20\) cm; \(S=80\pi\) cm².', r'\(R=20\) cm; \(S=80\pi\) cm².'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('A path around a garden', 'Lối đi quanh vườn'),
  T(r'A circular garden has radius 5 m. A path 1.5 m wide is built around the outside. Find the area of the path and the paving cost at 240,000 dong per m² (use \(\pi\approx3.14\)).', r'Một vườn hoa hình tròn bán kính 5 m. Người ta làm lối đi rộng 1,5 m bao quanh bên ngoài vườn. Tính diện tích lối đi và chi phí lát với giá 240 000 đồng/m² (lấy \(\pi\approx3{,}14\)).'),
  ('The path is an annulus.', 'Lối đi là một hình vành khuyên.'),
  [T(r'Outer radius \(5+1.5=6.5\) m. \(S=3.14\left(6.5^2-5^2\right)=3.14\cdot17.25=54.165\) m².', r'Bán kính ngoài \(5+1{,}5=6{,}5\) m. \(S=3{,}14\left(6{,}5^2-5^2\right)=3{,}14\cdot17{,}25=54{,}165\) m².'),
   T(r'Cost \(=54.165\cdot240\,000=12\,999\,600\) dong, about 13 million dong.', r'Chi phí \(=54{,}165\cdot240\,000=12\,999\,600\) đồng, khoảng 13 triệu đồng.')],
  T(r'About 54.17 m²; about 13 million dong.', r'Khoảng 54,17 m²; khoảng 13 triệu đồng.'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('From a sector to a party hat', 'Từ hình quạt đến chiếc mũ sinh nhật'),
  T(r'A party hat is made by rolling a sector of radius 18 cm and central angle \(120^\circ\) (no overlap). a) Find the length of the curved edge. b) It becomes the circumference of the base: find the base radius \(r\). c) Find the area of the sector. What does it represent on the hat?', r'Một chiếc mũ sinh nhật được làm bằng cách cuộn hình quạt bán kính 18 cm, góc ở tâm \(120^\circ\) (không chồng mép). a) Tính độ dài mép cong. b) Mép cong trở thành đường tròn đáy: tính bán kính đáy \(r\). c) Tính diện tích hình quạt. Diện tích này ứng với phần nào của chiếc mũ?'),
  ('Sector arc → base circumference; sector radius → slant height.', 'Cung của hình quạt → đường tròn đáy; bán kính hình quạt → đường sinh.'),
  [T(r'a) \(l=\dfrac{\pi\cdot18\cdot120}{180}=12\pi\) cm. b) \(2\pi r=12\pi\Rightarrow r=6\) cm.', r'a) \(l=\dfrac{\pi\cdot18\cdot120}{180}=12\pi\) cm. b) \(2\pi r=12\pi\Rightarrow r=6\) cm.'),
   T(r'c) \(S=\dfrac{\pi\cdot18^2\cdot120}{360}=108\pi\) cm²: this is the lateral surface area of the cone (the paper of the hat).', r'c) \(S=\dfrac{\pi\cdot18^2\cdot120}{360}=108\pi\) cm²: đó là diện tích xung quanh của hình nón (phần giấy làm mũ).')],
  T(r'\(12\pi\) cm; \(r=6\) cm; \(108\pi\) cm².', r'\(12\pi\) cm; \(r=6\) cm; \(108\pi\) cm².'))

_SETS = sp_g9.BANK(sp_g9.L15_GROUPS, start=1, seeds=(2501, 2502, 2503))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>360 vs 180.</b> Arc length uses \(\dfrac{\pi Rn}{180}\); sector area uses \(\dfrac{\pi R^2n}{360}\).', r'<b>Nhầm 360 và 180.</b> Độ dài cung dùng \(\dfrac{\pi Rn}{180}\); diện tích hình quạt dùng \(\dfrac{\pi R^2n}{360}\).'),
 (r'<b>Forgetting to square.</b> Sector area has \(R^2\); arc length has \(R\).', r'<b>Quên bình phương.</b> Diện tích hình quạt có \(R^2\); độ dài cung chỉ có \(R\).'),
 (r'<b>Annulus.</b> \(\pi\left(R^2-r^2\right)\ne\pi(R-r)^2\).', r'<b>Vành khuyên.</b> \(\pi\left(R^2-r^2\right)\ne\pi(R-r)^2\).'),
 (r'<b>Using the diameter as \(R\).</b> Halve the diameter first.', r'<b>Dùng đường kính thay cho bán kính.</b> Phải chia đôi đường kính trước.')]
summary = [
 (r'\(C=2\pi R\); \(l=\dfrac{\pi Rn}{180}\).', r'\(C=2\pi R\); \(l=\dfrac{\pi Rn}{180}\).'),
 (r'\(S_{\text{sector}}=\dfrac{\pi R^2n}{360}=\dfrac{lR}{2}\).', r'\(S_{\text{quạt}}=\dfrac{\pi R^2n}{360}=\dfrac{lR}{2}\).'),
 (r'\(S_{\text{annulus}}=\pi\left(R^2-r^2\right)\).', r'\(S_{\text{vành khuyên}}=\pi\left(R^2-r^2\right)\).'),
 (r'Key English: circumference, arc length, sector, sector area, annulus, concentric circles, slant height.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[độ dài đường tròn (chu vi)]], [[độ dài cung]], [[hình quạt tròn]], [[diện tích hình quạt tròn]], [[hình vành khuyên]], [[hai đường tròn đồng tâm]], [[đường sinh]].')]
checks = [
 (r'I can find the length of an arc.', r'Em tính được độ dài cung tròn.'),
 (r'I can find the area of a sector and of an annulus.', r'Em tính được diện tích hình quạt tròn, hình vành khuyên.'),
 (r'I can find the radius or the angle from a length or an area.', r'Em tìm được bán kính hoặc số đo cung khi biết độ dài hoặc diện tích.'),
 (r'I can solve real-life problems with sectors and annuli.', r'Em giải được bài toán thực tế về hình quạt, hình vành khuyên.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Arc Length, Sectors and Annuli', title_vi='Độ dài của cung tròn. Diện tích hình quạt tròn và hình vành khuyên', topic=TOPIC,
       folder='circles', file='arc-length-sectors-annuli', catalog_title_vi='Độ dài của cung tròn. Diện tích hình quạt tròn và hình vành khuyên',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Arc length, area of a sector and area of an annulus, with real-life applications.', level='Intermediate', minutes=75,
       description_vi='Bài 15 – Độ dài cung tròn; diện tích hình quạt tròn; diện tích hình vành khuyên; bài toán thực tế.',
       tags_vi=['độ dài cung', 'hình quạt', 'vành khuyên'], prerequisites=['g9-circles-02'], tags=['arc length', 'sector', 'annulus'], order=150)
