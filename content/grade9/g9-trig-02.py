# -*- coding: utf-8 -*-
"""Nội dung bài g9-trig-02 = Toán 9 KNTT, Bài 12: Một số hệ thức giữa cạnh, góc trong tam giác vuông và ứng dụng – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 4 – Lesson 12; Mini project Ch.4 "Measure the Unreachable"."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9

LID = 'g9-trig-02'
CH = 'Hệ thức lượng trong tam giác vuông'
TOPIC = ('Trigonometric Ratios in Right Triangles', CH)
ensure_vocab([
 ('g9-leg', 'leg (of a right triangle)', 'cạnh góc vuông', CH, 'AB and AC are the two legs of right triangle ABC.', ''),
 ('g9-solve-right-tri', 'solve a right triangle', 'giải tam giác vuông', CH, 'Solving a right triangle is to find the unknown sides and angles.', ''),
 ('g9-horizontal', 'horizontal', 'phương nằm ngang', CH, 'The angle of elevation is measured from the horizontal line.', ''),
 ('g9-line-of-sight', 'line of sight', 'tia nhìn', CH, 'The angle between the line of sight and the horizontal.', ''),
 ('g9-nearest-tenth', 'round to the nearest tenth', 'làm tròn đến hàng phần mười', CH, 'Round your answer to the nearest tenth of a meter.', ''),
 ('g9-eye-height', "observer's eye height", 'chiều cao tới mắt người quan sát', CH, "We added the observer's eye height to obtain the total height.", ''),
])
load_vocab()

s_, c_, t_ = (lambda d: math.sin(math.radians(d))), (lambda d: math.cos(math.radians(d))), (lambda d: math.tan(math.radians(d)))
r1 = lambda v: '%.1f' % (math.floor(v * 10 + 0.5) / 10)
# ---------- kiểm tra số liệu ----------
assert (r1(12 * s_(40)), r1(12 * c_(40))) == ('7.7', '9.2')
assert (r1(7 * t_(35)), r1(7 / c_(35))) == ('4.9', '8.5')
assert r1(math.sqrt(89)) == '9.4' and round(math.degrees(math.atan(8 / 5))) == 58
assert r1(20 / t_(32)) == '32.0'
h5 = 20 / (1 / t_(30) - 1 / t_(45)); assert abs(h5 - 10 * (3 ** 0.5 + 1)) < 1e-9 and r1(h5) == '27.3'

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 90 minutes', '90 phút'),
            before=('Lesson 11: trigonometric ratios of an acute angle', 'Bài 11: tỉ số lượng giác của góc nhọn'))
goals = [
 (r'state the relations between the sides and the angles of a right triangle;', r'phát biểu được các hệ thức giữa cạnh và góc trong tam giác vuông;'),
 (r'find a side from another side and an acute angle;', r'tính được một cạnh khi biết một cạnh và một góc nhọn;'),
 (r'solve a right triangle;', r'giải được tam giác vuông;'),
 (r'measure heights and distances using angles of elevation and depression.', r'tính được chiều cao, khoảng cách trong thực tế nhờ góc nâng, góc hạ.')]
vocab = [
 (r'<b>leg</b> – one of the two sides that form the right angle.', r'[[Cạnh góc vuông]] – một trong hai cạnh tạo thành góc vuông.'),
 (r'<b>solve a right triangle</b> – find all unknown sides and angles.', r'[[Giải tam giác vuông]] – tìm tất cả các cạnh và góc chưa biết.'),
 (r'<b>horizontal / line of sight</b> – the level line through the eye / the line from the eye to the object.', r'[[Phương nằm ngang]] / [[tia nhìn]] – đường thẳng nằm ngang qua mắt / đường từ mắt tới vật.'),
 (r'<b>angle of elevation / angle of depression</b> – the angle between the line of sight and the horizontal, looking up / looking down.', r'[[Góc nâng]] / [[góc hạ]] – góc giữa tia nhìn và phương nằm ngang khi nhìn lên / nhìn xuống.'),
 (r'<b>round to the nearest tenth</b> – keep one decimal place: \(7.71\approx7.7\).', r'[[Làm tròn đến hàng phần mười]] – giữ một chữ số thập phân: \(7{,}71\approx7{,}7\).')]
phrases = [
 (r'<b>Each leg equals the hypotenuse times the sine of the opposite angle.</b>', r'Mỗi cạnh góc vuông bằng cạnh huyền nhân với sin góc đối.'),
 (r'<b>Which trigonometric ratio should we use?</b>', r'Ta nên dùng tỉ số lượng giác nào?'),
 (r'<b>Tangent relates the opposite side to the adjacent side.</b>', r'Tan liên hệ cạnh đối với cạnh kề.'),
 (r'<b>The side is approximately 7.7 cm.</b>', r'Cạnh đó xấp xỉ 7,7 cm.'),
 (r'<b>We added the observer’s eye height to obtain the total height.</b>', r'Ta cộng thêm chiều cao tới mắt người quan sát để được chiều cao cần tìm.')]
review = (T(r'<b>Lesson 11.</b> \(\sin=\dfrac{\text{opp}}{\text{hyp}}\), \(\cos=\dfrac{\text{adj}}{\text{hyp}}\), \(\tan=\dfrac{\text{opp}}{\text{adj}}\), \(\cot=\dfrac{\text{adj}}{\text{opp}}\).', r'<b>Bài 11.</b> sin = đối/huyền, cos = kề/huyền, tan = đối/kề, cot = kề/đối.') +
          T(r'<b>Acute angles.</b> In a right triangle \(\widehat B+\widehat C=90^\circ\).', r'<b>Góc nhọn.</b> Trong tam giác vuông \(\widehat B+\widehat C=90^\circ\).'))

G = lambda cfg, en, vi, hgt=280: GEO(sp_g9.auto_labels(cfg), cap=(en, vi), alt=(en, ''), height=hgt)
def pt(i, x, y, name=None, size=3): return {'type': 'point', 'id': i, 'at': [x, y], 'name': i if name is None else name, 'style': {'size': size}}
def seg(a, b, **st): return {'type': 'segment', 'through': [a, b], 'style': st}
def txt(x, y, s): return {'type': 'text', 'at': [x, y], 'text': s}

FIG1 = G({'view': [-1, 6, -0.9, 4.4], 'steps': [pt('A', 0, 0), pt('B', 5, 0), pt('C', 0, 3.6), {'type': 'polygon', 'through': ['A', 'B', 'C']},
          {'type': 'angle', 'points': ['C', 'A', 'B']}, {'type': 'angle', 'points': ['A', 'B', 'C'], 'radius': 0.9, 'label': False}, {'type': 'angle', 'points': ['B', 'C', 'A'], 'radius': 0.7, 'label': False},
          txt(2.75, 2.15, 'a'), txt(-0.38, 1.8, 'b'), txt(2.5, -0.4, 'c')]},
         'Right triangle ABC (right angle at A): hypotenuse BC = a, legs AC = b and AB = c.', 'Tam giác ABC vuông tại A: cạnh huyền BC = a, hai cạnh góc vuông AC = b, AB = c.')

theory = '<h3>5.1 %s</h3>' % TI('Relations between sides and angles', 'Hệ thức giữa cạnh và góc trong tam giác vuông')
theory += FIG1
theory += BOX('blue', ('Theorem', 'Định lí'),
  T(r'In a right triangle, each leg equals', r'Trong tam giác vuông, mỗi [[cạnh góc vuông]] bằng'),
  UL([T(r'the hypotenuse times the sine of the opposite angle, or times the cosine of the adjacent angle;', r'cạnh huyền nhân với sin góc đối hoặc nhân với cos góc kề;'),
      T(r'the other leg times the tangent of the opposite angle, or times the cotangent of the adjacent angle.', r'cạnh góc vuông kia nhân với tan góc đối hoặc nhân với cot góc kề.')]),
  M(r'b=a\sin B=a\cos C,\qquad c=a\sin C=a\cos B'),
  M(r'b=c\tan B=c\cot C,\qquad c=b\tan C=b\cot B'))
theory += '<h3>5.2 %s</h3>' % TI('Solving a right triangle', 'Giải tam giác vuông')
theory += BOX('mint', ('Method', 'Cách làm'),
  T(r'Solving a right triangle is finding all unknown sides and angles. We need two elements, at least one of them a side:', r'[[Giải tam giác vuông]] là tìm tất cả các cạnh và góc chưa biết. Cần biết hai yếu tố, trong đó ít nhất một yếu tố là cạnh:'),
  UL([T(r'one side and one acute angle: the other acute angle is \(90^\circ\) minus it; the other sides come from the relations above;', r'một cạnh và một góc nhọn: góc nhọn còn lại bằng \(90^\circ\) trừ góc đã biết; các cạnh tính theo hệ thức trên;'),
      T(r'two sides: the third side comes from the Pythagorean theorem; an angle comes from a ratio (SHIFT sin/cos/tan on the calculator).', r'hai cạnh: cạnh thứ ba tính theo định lí Pythagore; góc tính từ một tỉ số (bấm SHIFT sin/cos/tan).')]),
  T(r'Keep the full calculator value until the last step, then round.', r'Giữ nguyên kết quả trên máy tính đến bước cuối rồi mới làm tròn.'))
theory += '<h3>5.3 %s</h3>' % TI('Angles of elevation and depression', 'Góc nâng và góc hạ')
theory += BOX('yellow', ('In practice', 'Trong thực tế'),
  T(r'The <b>angle of elevation</b> is the angle between the horizontal and the line of sight when we look up; the <b>angle of depression</b> is that angle when we look down.', r'[[Góc nâng]] là góc giữa [[phương nằm ngang]] và [[tia nhìn]] khi nhìn lên; [[góc hạ]] là góc đó khi nhìn xuống.'),
  T(r'The angle of depression from \(P\) to \(Q\) equals the angle of elevation from \(Q\) to \(P\) (alternate angles).', r'Góc hạ từ \(P\) nhìn xuống \(Q\) bằng góc nâng từ \(Q\) nhìn lên \(P\) (hai góc so le trong).'),
  T(r'When the angle is measured at eye level, add the observer’s eye height to get the height from the ground.', r'Khi góc được đo ở ngang tầm mắt, cộng thêm [[chiều cao tới mắt người quan sát]] để được chiều cao tính từ mặt đất.'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Hypotenuse and an angle', 'Biết cạnh huyền và một góc'),
  T(r'Triangle \(ABC\) is right-angled at \(A\), \(BC=12\) cm and \(\widehat{B}=40^\circ\). Find \(AC\) and \(AB\), rounded to the nearest tenth.', r'Tam giác \(ABC\) vuông tại \(A\), \(BC=12\) cm và \(\widehat{B}=40^\circ\). Tính \(AC\) và \(AB\) (làm tròn đến hàng phần mười).'),
  ('\\(AC\\) is opposite \\(B\\), \\(AB\\) is adjacent to \\(B\\).', '\\(AC\\) là cạnh đối, \\(AB\\) là cạnh kề của góc \\(B\\).'),
  [T(r'\(AC=BC\cdot\sin B=12\sin40^\circ\approx7.7\) cm.', r'\(AC=BC\cdot\sin B=12\sin40^\circ\approx7{,}7\) cm.'),
   T(r'\(AB=BC\cdot\cos B=12\cos40^\circ\approx9.2\) cm.', r'\(AB=BC\cdot\cos B=12\cos40^\circ\approx9{,}2\) cm.')],
  T(r'\(AC\approx7.7\) cm, \(AB\approx9.2\) cm.', r'\(AC\approx7{,}7\) cm, \(AB\approx9{,}2\) cm.'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('A leg and an angle', 'Biết một cạnh góc vuông và một góc'),
  T(r'Triangle \(ABC\) is right-angled at \(A\), \(AB=7\) cm and \(\widehat{B}=35^\circ\). Find \(AC\) and \(BC\) (nearest tenth).', r'Tam giác \(ABC\) vuông tại \(A\), \(AB=7\) cm và \(\widehat{B}=35^\circ\). Tính \(AC\) và \(BC\) (làm tròn đến hàng phần mười).'),
  ('Tangent relates the opposite side to the adjacent side.', 'Tan liên hệ cạnh đối với cạnh kề.'),
  [T(r'\(AC=AB\cdot\tan B=7\tan35^\circ\approx4.9\) cm.', r'\(AC=AB\cdot\tan B=7\tan35^\circ\approx4{,}9\) cm.'),
   T(r'\(AB=BC\cdot\cos B\Rightarrow BC=\dfrac{7}{\cos35^\circ}\approx8.5\) cm.', r'\(AB=BC\cdot\cos B\Rightarrow BC=\dfrac{7}{\cos35^\circ}\approx8{,}5\) cm.')],
  T(r'\(AC\approx4.9\) cm, \(BC\approx8.5\) cm.', r'\(AC\approx4{,}9\) cm, \(BC\approx8{,}5\) cm.'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('Solve a right triangle', 'Giải tam giác vuông'),
  T(r'Solve triangle \(ABC\), right-angled at \(A\), with \(AB=5\) cm and \(AC=8\) cm (side to the nearest tenth, angles to the nearest degree).', r'Giải tam giác \(ABC\) vuông tại \(A\), biết \(AB=5\) cm, \(AC=8\) cm (cạnh làm tròn đến hàng phần mười, góc làm tròn đến độ).'),
  ('Two legs are known: use the Pythagorean theorem and \\(\\tan\\).', 'Biết hai cạnh góc vuông: dùng định lí Pythagore và \\(\\tan\\).'),
  [T(r'\(BC=\sqrt{5^2+8^2}=\sqrt{89}\approx9.4\) cm.', r'\(BC=\sqrt{5^2+8^2}=\sqrt{89}\approx9{,}4\) cm.'),
   T(r'\(\tan B=\dfrac{8}{5}=1.6\Rightarrow\widehat B\approx58^\circ\); \(\widehat C\approx90^\circ-58^\circ=32^\circ\).', r'\(\tan B=\dfrac{8}{5}=1{,}6\Rightarrow\widehat B\approx58^\circ\); \(\widehat C\approx90^\circ-58^\circ=32^\circ\).')],
  T(r'\(BC\approx9.4\) cm, \(\widehat B\approx58^\circ\), \(\widehat C\approx32^\circ\).', r'\(BC\approx9{,}4\) cm, \(\widehat B\approx58^\circ\), \(\widehat C\approx32^\circ\).'))
FIG4 = G({'view': [-1.6, 7.6, -0.9, 4.9], 'steps': [pt('A', 0, 4), pt('B', 0, 0), pt('C', 6.4, 0), pt('H', 6.4, 4, name='', size=0),
          seg('B', 'A', strokeWidth=4), seg('B', 'C'), seg('A', 'C'), seg('A', 'H', dash=True),
          {'type': 'angle', 'points': ['A', 'B', 'C']}, {'type': 'angle', 'points': ['C', 'A', 'H'], 'radius': 1.3, 'label': '32^\\circ'},
          {'type': 'angle', 'points': ['B', 'C', 'A'], 'radius': 1.3, 'label': '32^\\circ'}, txt(-0.75, 2, '20\\text{ m}')]},
         'AB is the building (20 m), C is the car; the dashed line is the horizontal through A; the angle of depression is 32°.',
         'AB là tòa nhà (20 m), C là ô tô; nét đứt là phương nằm ngang qua A; góc hạ bằng 32°.')
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Angle of depression', 'Góc hạ'),
  T(r'From the top \(A\) of a 20 m tall building, a student looks down at a car \(C\) on the ground. The angle of depression is \(32^\circ\). Find the distance \(BC\) from the car to the foot of the building (nearest tenth).', r'Từ đỉnh \(A\) của một tòa nhà cao 20 m, một bạn học sinh nhìn xuống chiếc ô tô \(C\) trên mặt đất với góc hạ \(32^\circ\). Tính khoảng cách \(BC\) từ ô tô đến chân tòa nhà (làm tròn đến hàng phần mười).') + FIG4,
  ('The angle of depression equals \\(\\widehat{ACB}\\) (alternate angles).', 'Góc hạ bằng \\(\\widehat{ACB}\\) (hai góc so le trong).'),
  [T(r'In right triangle \(ABC\): \(\widehat{C}=32^\circ\), \(AB=20\) m is opposite \(C\), \(BC\) is adjacent to \(C\).', r'Trong tam giác vuông \(ABC\): \(\widehat{C}=32^\circ\), \(AB=20\) m là cạnh đối, \(BC\) là cạnh kề của góc \(C\).'),
   T(r'\(AB=BC\cdot\tan C\Rightarrow BC=\dfrac{20}{\tan32^\circ}\approx32.0\) m.', r'\(AB=BC\cdot\tan C\Rightarrow BC=\dfrac{20}{\tan32^\circ}\approx32{,}0\) m.')],
  T(r'About \(32.0\) m.', r'Khoảng \(32{,}0\) m.'))
FIG5 = G({'view': [-1.4, 10.8, -1.1, 6.3], 'steps': [pt('T', 0, 5.46), pt('F', 0, 0), pt('N', 5.46, 0), pt('M', 9.46, 0),
          seg('F', 'T', strokeWidth=4), seg('F', 'M'), seg('T', 'N'), seg('T', 'M'),
          {'type': 'angle', 'points': ['T', 'F', 'N']}, {'type': 'angle', 'points': ['F', 'M', 'T'], 'radius': 1.4, 'label': '30^\\circ'},
          {'type': 'angle', 'points': ['F', 'N', 'T'], 'radius': 0.8, 'label': '45^\\circ'}, txt(7.46, -0.55, '20\\text{ m}'), txt(-0.55, 2.7, 'h')]},
         'TF is the tower of height h; from M the angle of elevation is 30°, from N (20 m closer) it is 45°.',
         'TF là tháp cao h; từ M góc nâng là 30°, từ N (gần tháp hơn 20 m) góc nâng là 45°.', 300)
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Measuring the unreachable', 'Đo chiều cao không đến được'),
  T(r'A group cannot reach the foot \(F\) of a tower. From point \(M\) the angle of elevation to the top \(T\) is \(30^\circ\); after walking 20 m straight towards the tower to \(N\), it is \(45^\circ\). Find the height \(h=TF\) (exact value and nearest tenth).', r'Một nhóm học sinh không đo trực tiếp được chiều cao tháp \(TF\). Từ điểm \(M\), góc nâng nhìn lên đỉnh \(T\) là \(30^\circ\); đi thẳng về phía tháp 20 m đến \(N\) thì góc nâng là \(45^\circ\). Tính chiều cao \(h=TF\) (giá trị đúng và làm tròn đến hàng phần mười).') + FIG5,
  ('Write \\(FM\\) and \\(FN\\) in terms of \\(h\\), then use \\(FM-FN=20\\).', 'Biểu diễn \\(FM\\), \\(FN\\) theo \\(h\\) rồi dùng \\(FM-FN=20\\).'),
  [T(r'\(FN=h\cot45^\circ=h\), \(FM=h\cot30^\circ=h\sqrt3\).', r'\(FN=h\cot45^\circ=h\), \(FM=h\cot30^\circ=h\sqrt3\).'),
   T(r'\(h\sqrt3-h=20\Rightarrow h=\dfrac{20}{\sqrt3-1}=\dfrac{20\left(\sqrt3+1\right)}{2}=10\left(\sqrt3+1\right)\) (rationalize the denominator).', r'\(h\sqrt3-h=20\Rightarrow h=\dfrac{20}{\sqrt3-1}=\dfrac{20\left(\sqrt3+1\right)}{2}=10\left(\sqrt3+1\right)\) (trục căn thức ở mẫu).'),
   T(r'\(h\approx27.3\) m. Measuring from two positions avoids measuring the distance to the foot of the tower.', r'\(h\approx27{,}3\) m. Đo từ hai vị trí giúp không cần đo khoảng cách tới chân tháp.')],
  T(r'\(h=10\left(\sqrt3+1\right)\approx27.3\) m.', r'\(h=10\left(\sqrt3+1\right)\approx27{,}3\) m.'))

_SETS = sp_g9.BANK(sp_g9.L12_GROUPS, start=1, seeds=(2201, 2202, 2203))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Wrong ratio.</b> \(AC\) is opposite \(B\): \(AC=BC\sin B\), not \(BC\cos B\).', r'<b>Chọn sai tỉ số.</b> \(AC\) là cạnh đối của góc \(B\): \(AC=BC\sin B\), không phải \(BC\cos B\).'),
 (r'<b>Multiplying instead of dividing.</b> From \(AB=BC\cos B\) we get \(BC=\dfrac{AB}{\cos B}\), not \(AB\cos B\).', r'<b>Nhân thay vì chia.</b> Từ \(AB=BC\cos B\) suy ra \(BC=\dfrac{AB}{\cos B}\), không phải \(AB\cos B\).'),
 (r'<b>Rounding too early.</b> Keep the calculator value and round only at the end.', r'<b>Làm tròn quá sớm.</b> Giữ nguyên giá trị trên máy tính, chỉ làm tròn ở bước cuối.'),
 (r'<b>Forgetting the eye height.</b> An angle measured at eye level gives the height above the eye, not above the ground.', r'<b>Quên chiều cao tới mắt.</b> Góc đo ngang tầm mắt cho chiều cao tính từ mắt, chưa phải từ mặt đất.')]
summary = [
 (r'\(b=a\sin B=a\cos C\), \(c=a\sin C=a\cos B\); \(b=c\tan B=c\cot C\), \(c=b\tan C=b\cot B\).', r'\(b=a\sin B=a\cos C\), \(c=a\sin C=a\cos B\); \(b=c\tan B=c\cot C\), \(c=b\tan C=b\cot B\).'),
 (r'Solving a right triangle: know two elements, at least one a side; the acute angles add up to \(90^\circ\).', r'Giải tam giác vuông: cần biết hai yếu tố, ít nhất một là cạnh; hai góc nhọn có tổng \(90^\circ\).'),
 (r'Angle of depression from \(P\) to \(Q\) = angle of elevation from \(Q\) to \(P\).', r'Góc hạ từ \(P\) xuống \(Q\) bằng góc nâng từ \(Q\) lên \(P\).'),
 (r'Key English: leg, solve a right triangle, horizontal, line of sight, angle of elevation, angle of depression, round to the nearest tenth.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[cạnh góc vuông]], [[giải tam giác vuông]], [[phương nằm ngang]], [[tia nhìn]], [[góc nâng]], [[góc hạ]], [[làm tròn đến hàng phần mười]].')]
checks = [
 (r'I can state the relations between sides and angles in a right triangle.', r'Em phát biểu được hệ thức giữa cạnh và góc trong tam giác vuông.'),
 (r'I can find a side from a side and an acute angle.', r'Em tính được một cạnh khi biết một cạnh và một góc nhọn.'),
 (r'I can solve a right triangle.', r'Em giải được tam giác vuông.'),
 (r'I can find heights and distances with angles of elevation and depression.', r'Em tính được chiều cao, khoảng cách nhờ góc nâng, góc hạ.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Relationships Between Sides and Angles in a Right Triangle', title_vi='Một số hệ thức giữa cạnh, góc trong tam giác vuông và ứng dụng', topic=TOPIC,
       folder='right-triangle-trigonometry', file='sides-and-angles', catalog_title_vi='Một số hệ thức giữa cạnh, góc trong tam giác vuông và ứng dụng',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Relations between sides and angles in a right triangle, solving right triangles, angles of elevation and depression.', level='Intermediate', minutes=90,
       description_vi='Bài 12 – Hệ thức giữa cạnh và góc trong tam giác vuông; giải tam giác vuông; góc nâng, góc hạ và bài toán đo chiều cao, khoảng cách.',
       tags_vi=['hệ thức lượng', 'giải tam giác vuông', 'góc nâng'],
       prerequisites=['g9-trig-01'], tags=['right triangle', 'solve a triangle', 'angle of elevation'], order=120)
