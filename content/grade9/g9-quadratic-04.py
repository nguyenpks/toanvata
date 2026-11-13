# -*- coding: utf-8 -*-
"""Nội dung bài g9-quadratic-04 = Toán 9 KNTT, Bài 21: Giải bài toán bằng cách lập phương trình – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 6 – Lesson 21."""
import os, sys, math
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9

LID = 'g9-quadratic-04'
CH = 'Hàm số y = ax² (a ≠ 0). Phương trình bậc hai một ẩn'
TOPIC = ('Quadratic Function and Quadratic Equation', CH)
ensure_vocab([
 ('g9-setup-eq', 'set up an equation', 'lập phương trình', CH, 'Set up an equation and solve it.', ''),
 ('g9-suitable-cond', 'suitable condition', 'điều kiện thích hợp', CH, 'State a suitable condition for the unknown.', ''),
 ('g9-express-in-x', 'express … in terms of x', 'biểu diễn … theo x', CH, 'Express the length in terms of x.', ''),
 ('g9-reject', 'reject (a root)', 'loại (nghiệm)', CH, 'The negative root is rejected.', ''),
 ('g9-downstream', 'downstream', 'xuôi dòng', CH, 'Downstream, the speed of the boat is x + 3 km/h.', ''),
 ('g9-upstream', 'upstream', 'ngược dòng', CH, 'Upstream, the speed of the boat is x − 3 km/h.', ''),
 ('g9-current', 'current (of a river)', 'dòng nước', CH, 'The speed of the current is 3 km/h.', ''),
 ('g9-compound', 'compound interest', 'lãi kép', CH, 'At compound interest, the interest is added to the deposit each year.', ''),
])
load_vocab()

# ---------- kiểm tra số liệu ----------
assert 30 * 60 == 1800 and 60 - 30 == 30
assert 15 * 24 == 360 and (15 + 3) * (24 - 4) == 360
assert 1200000 * F(11, 10) ** 2 == 1452000
assert F(36, 18) + F(36, 12) == 5 and F(1, 2) + 5 == F(11, 2)
assert (100 + 10) * (F(1500, 100) - 3) == 1320
assert 100 * F(109, 100) ** 2 == F(11881, 100)

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 90 minutes', '90 phút'), before=('Lessons 3, 19, 20', 'Bài 3, 19, 20'))
goals = [
 (r'state the steps for solving a problem by setting up an equation;', r'nêu được các bước giải bài toán bằng cách lập phương trình;'),
 (r'choose the unknown, state its condition and express other quantities in terms of it;', r'chọn được ẩn, đặt điều kiện và biểu diễn các đại lượng khác theo ẩn;'),
 (r'solve problems on area, productivity and motion leading to quadratic equations;', r'giải được bài toán về diện tích, năng suất, chuyển động dẫn tới phương trình bậc hai;'),
 (r'solve problems on river currents and percentage growth over two years.', r'giải được bài toán xuôi – ngược dòng và tăng trưởng phần trăm qua hai năm.')]
vocab = [
 (r'<b>set up an equation</b> – write an equation that describes the problem.', r'[[Lập phương trình]] – viết phương trình mô tả bài toán.'),
 (r'<b>suitable condition</b> – e.g. \(x\gt0\) for a length or a speed.', r'[[Điều kiện thích hợp]] – ví dụ \(x\gt0\) với độ dài, vận tốc.'),
 (r'<b>reject a root</b> – a root that does not satisfy the condition is not an answer.', r'[[Loại (nghiệm)|loại (nghiệm)]] – nghiệm không thỏa mãn điều kiện thì không phải đáp số.'),
 (r'<b>downstream / upstream / current</b> – with / against the flow; speed \(x\pm c\).', r'[[Xuôi dòng]] / [[ngược dòng]] / [[dòng nước]] – theo / ngược chiều nước chảy; vận tốc \(x\pm c\).'),
 (r'<b>compound interest</b> – \(A=P(1+r)^2\) after two years.', r'[[Lãi kép]] – sau hai năm \(A=P(1+r)^2\).')]
phrases = [
 (r'<b>Let \(x\) (m) be the width of the pitch, \(x\gt0\).</b>', r'Gọi chiều rộng của sân là \(x\) (m), \(x\gt0\).'),
 (r'<b>Express the length in terms of \(x\).</b>', r'Biểu diễn chiều dài theo \(x\).'),
 (r'<b>We obtain the equation …</b>', r'Ta có phương trình …'),
 (r'<b>The root \(-60\) does not satisfy the condition, so it is rejected.</b>', r'Nghiệm \(-60\) không thỏa mãn điều kiện nên bị loại.'),
 (r'<b>Hence, the pitch is 60 m long and 30 m wide.</b>', r'Vậy sân dài 60 m, rộng 30 m.')]
review = (T(r'<b>Lesson 3.</b> Steps for word problems with systems: choose unknowns, set up, solve, check.', r'<b>Bài 3.</b> Các bước giải bài toán bằng cách lập hệ phương trình: chọn ẩn, lập hệ, giải, đối chiếu.') +
          T(r'<b>Lesson 19.</b> Solve \(ax^2+bx+c=0\) with \(\Delta\) or \(\Delta^{\prime}\).', r'<b>Bài 19.</b> Giải \(ax^2+bx+c=0\) bằng \(\Delta\) hoặc \(\Delta^{\prime}\).'))

theory = '<h3>5.1 %s</h3>' % TI('The steps', 'Các bước giải bài toán bằng cách lập phương trình')
theory += BOX('blue', ('Steps', 'Các bước'),
  UL([T(r'<b>Step 1. Set up the equation:</b> choose the unknown and state a suitable condition; express the other quantities in terms of the unknown; write the equation.', r'<b>Bước 1. Lập phương trình:</b> chọn ẩn và đặt điều kiện thích hợp; biểu diễn các đại lượng chưa biết theo ẩn; lập phương trình.'),
      T(r'<b>Step 2. Solve the equation.</b>', r'<b>Bước 2. Giải phương trình.</b>'),
      T(r'<b>Step 3. Answer:</b> check which roots satisfy the condition, reject the others, and answer the question.', r'<b>Bước 3. Kết luận:</b> kiểm tra nghiệm nào thỏa mãn điều kiện, loại nghiệm không thỏa mãn rồi trả lời.')]))
theory += '<h3>5.2 %s</h3>' % TI('Useful relations', 'Một số quan hệ thường dùng')
theory += TABLE([('Type of problem', 'Dạng bài'), ('Relation', 'Quan hệ')],
  [[TI('area', 'diện tích'), TI('area = length × width', 'diện tích = dài × rộng')],
   [TI('productivity', 'năng suất'), TI('work = rate × time', 'khối lượng công việc = năng suất × thời gian')],
   [TI('motion', 'chuyển động'), TI('distance = speed × time', 'quãng đường = vận tốc × thời gian')],
   [TI('river', 'xuôi – ngược dòng'), TI('downstream \\(x+c\\), upstream \\(x-c\\)', 'xuôi dòng \\(x+c\\), ngược dòng \\(x-c\\)')],
   [TI('growth over 2 years', 'tăng trưởng qua 2 năm'), TI('\\(A=P(1+r)^2\\)', '\\(A=P(1+r)^2\\)')]])

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('A football pitch', 'Sân bóng đá mini'),
  T(r'A seven-a-side football pitch is 30 m shorter in width than in length and has an area of 1,800 m². Find its length and width.', r'Một sân bóng đá 7 người có chiều rộng ngắn hơn chiều dài 30 m và diện tích 1 800 m². Tìm chiều dài và chiều rộng của sân.'),
  ('Let the width be \\(x\\) m.', 'Gọi chiều rộng là \\(x\\) m.'),
  [T(r'Let \(x\) (m) be the width, \(x\gt0\). The length is \(x+30\) (m). We obtain \(x(x+30)=1800\Leftrightarrow x^2+30x-1800=0\).', r'Gọi chiều rộng là \(x\) (m), \(x\gt0\). Chiều dài là \(x+30\) (m). Ta có \(x(x+30)=1800\Leftrightarrow x^2+30x-1800=0\).'),
   T(r'\(\Delta^{\prime}=225+1800=2025=45^2\): \(x=-15\pm45\), so \(x=30\) or \(x=-60\). The root \(-60\) is rejected.', r'\(\Delta^{\prime}=225+1800=2025=45^2\): \(x=-15\pm45\), tức \(x=30\) hoặc \(x=-60\). Loại nghiệm \(-60\).')],
  T(r'60 m long and 30 m wide.', r'Dài 60 m, rộng 30 m.'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Unchanged area', 'Diện tích không đổi'),
  T(r'A rectangular plot has an area of 360 m². If its width is increased by 3 m and its length decreased by 4 m, the area does not change. Find its dimensions.', r'Một mảnh đất hình chữ nhật có diện tích 360 m². Nếu tăng chiều rộng 3 m và giảm chiều dài 4 m thì diện tích không đổi. Tìm các kích thước của mảnh đất.'),
  ('Express the length in terms of the width \\(x\\).', 'Biểu diễn chiều dài theo chiều rộng \\(x\\).'),
  [T(r'Let \(x\) (m) be the width, \(x\gt0\); the length is \(\dfrac{360}{x}\). Then \((x+3)\left(\dfrac{360}{x}-4\right)=360\).', r'Gọi chiều rộng là \(x\) (m), \(x\gt0\); chiều dài là \(\dfrac{360}{x}\). Ta có \((x+3)\left(\dfrac{360}{x}-4\right)=360\).'),
   T(r'\(\Leftrightarrow 4x^2+12x-1080=0\Leftrightarrow x^2+3x-270=0\Rightarrow x=15\) or \(x=-18\) (rejected). Length \(=\dfrac{360}{15}=24\) m.', r'\(\Leftrightarrow 4x^2+12x-1080=0\Leftrightarrow x^2+3x-270=0\Rightarrow x=15\) hoặc \(x=-18\) (loại). Chiều dài \(=\dfrac{360}{15}=24\) m.')],
  T(r'24 m and 15 m.', r'24 m và 15 m.'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('Population growth', 'Tăng dân số'),
  T(r'The population of a city increased from 1,200,000 to 1,452,000 in two years. By what percentage did it increase each year on average?', r'Dân số một thành phố tăng từ 1 200 000 người lên 1 452 000 người sau hai năm. Trung bình mỗi năm dân số tăng bao nhiêu phần trăm?'),
  ('After one year the population is multiplied by \\(1+x\\).', 'Sau mỗi năm dân số được nhân với \\(1+x\\).'),
  [T(r'Let \(x\) be the yearly rate, \(x\gt0\): \(1\,200\,000(1+x)^2=1\,452\,000\Leftrightarrow(1+x)^2=1.21\).', r'Gọi tỉ lệ tăng mỗi năm là \(x\), \(x\gt0\): \(1\,200\,000(1+x)^2=1\,452\,000\Leftrightarrow(1+x)^2=1{,}21\).'),
   T(r'\(1+x=1.1\) (since \(1+x\gt0\)), so \(x=0.1=10\%\).', r'\(1+x=1{,}1\) (vì \(1+x\gt0\)) nên \(x=0{,}1=10\%\).')],
  T(r'10% per year.', r'10% mỗi năm.'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Downstream and upstream', 'Xuôi dòng và ngược dòng'),
  T(r'River ports \(A\) and \(B\) are 36 km apart. A boat sails from \(A\) to \(B\), stops there for 30 minutes and returns to \(A\). The whole journey takes 5.5 hours. The current is 3 km/h. Find the speed of the boat in still water.', r'Hai bến sông \(A\), \(B\) cách nhau 36 km. Một ca nô đi từ \(A\) đến \(B\), nghỉ tại \(B\) 30 phút rồi quay về \(A\). Tổng thời gian là 5,5 giờ. Vận tốc dòng nước là 3 km/h. Tính vận tốc của ca nô khi nước yên lặng.') +
  TABLE([('', ''), ('Speed (km/h)', 'Vận tốc (km/h)'), ('Distance (km)', 'Quãng đường (km)'), ('Time (h)', 'Thời gian (h)')],
        [[TI('downstream', 'xuôi dòng'), '\\(x+3\\)', '\\(36\\)', '\\(\\dfrac{36}{x+3}\\)'], [TI('upstream', 'ngược dòng'), '\\(x-3\\)', '\\(36\\)', '\\(\\dfrac{36}{x-3}\\)']]),
  ('Moving time \\(=5.5-0.5=5\\) h.', 'Thời gian di chuyển \\(=5{,}5-0{,}5=5\\) giờ.'),
  [T(r'Let \(x\) (km/h) be the speed in still water, \(x\gt3\). Then \(\dfrac{36}{x+3}+\dfrac{36}{x-3}=5\).', r'Gọi vận tốc ca nô khi nước yên lặng là \(x\) (km/h), \(x\gt3\). Ta có \(\dfrac{36}{x+3}+\dfrac{36}{x-3}=5\).'),
   T(r'\(\Leftrightarrow 5x^2-72x-45=0\Rightarrow x=15\) or \(x=-0.6\) (rejected).', r'\(\Leftrightarrow 5x^2-72x-45=0\Rightarrow x=15\) hoặc \(x=-0{,}6\) (loại).')],
  T(r'15 km/h.', r'15 km/h.'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('A workshop', 'Năng suất của xưởng may'),
  T(r'A workshop has to make 1,500 shirts in a given time. In fact it made 10 shirts a day more than planned, so three days before the deadline it had already made 1,320 shirts. How many shirts a day did it plan to make?', r'Một xưởng phải may 1 500 chiếc áo trong một thời gian quy định. Thực tế mỗi ngày xưởng may nhiều hơn dự định 10 chiếc nên 3 ngày trước thời hạn đã may được 1 320 chiếc. Theo kế hoạch mỗi ngày xưởng may bao nhiêu chiếc?'),
  ('Planned time \\(=\\dfrac{1500}{x}\\) days.', 'Thời gian dự định \\(=\\dfrac{1500}{x}\\) ngày.'),
  [T(r'Let \(x\) be the planned number per day, \(x\in\mathbb N^*\). In \(\dfrac{1500}{x}-3\) days it made \(x+10\) a day: \((x+10)\left(\dfrac{1500}{x}-3\right)=1320\).', r'Gọi số áo may mỗi ngày theo kế hoạch là \(x\), \(x\in\mathbb N^*\). Trong \(\dfrac{1500}{x}-3\) ngày, mỗi ngày may \(x+10\) chiếc: \((x+10)\left(\dfrac{1500}{x}-3\right)=1320\).'),
   T(r'\(\Leftrightarrow 3x^2-150x-15000=0\Leftrightarrow x^2-50x-5000=0\Rightarrow x=100\) or \(x=-50\) (rejected).', r'\(\Leftrightarrow 3x^2-150x-15000=0\Leftrightarrow x^2-50x-5000=0\Rightarrow x=100\) hoặc \(x=-50\) (loại).')],
  T(r'100 shirts a day.', r'100 chiếc mỗi ngày.'))

_SETS = sp_g9.BANK(sp_g9.L21_GROUPS, start=1, seeds=(3101, 3102, 3103))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>No condition.</b> Always state the condition of the unknown before solving.', r'<b>Không đặt điều kiện.</b> Luôn đặt điều kiện cho ẩn trước khi giải.'),
 (r'<b>Keeping a negative root.</b> A length, speed or number of objects cannot be negative.', r'<b>Giữ nghiệm âm.</b> Độ dài, vận tốc, số lượng không thể âm.'),
 (r'<b>Forgetting the stop.</b> Subtract the resting time from the total time.', r'<b>Quên thời gian nghỉ.</b> Phải trừ thời gian nghỉ khỏi tổng thời gian.'),
 (r'<b>Percentage growth.</b> Two years at rate \(r\) gives \((1+r)^2\), not \(1+2r\).', r'<b>Tăng trưởng phần trăm.</b> Hai năm với tỉ lệ \(r\) cho \((1+r)^2\), không phải \(1+2r\).')]
summary = [
 (r'Steps: choose the unknown and its condition, express the quantities, set up the equation; solve; check and answer.', r'Các bước: chọn ẩn, đặt điều kiện, biểu diễn đại lượng, lập phương trình; giải; đối chiếu điều kiện và kết luận.'),
 (r'Downstream \(x+c\), upstream \(x-c\) (\(x\gt c\)); time \(=\dfrac{\text{distance}}{\text{speed}}\).', r'Xuôi dòng \(x+c\), ngược dòng \(x-c\) (\(x\gt c\)); thời gian \(=\dfrac{\text{quãng đường}}{\text{vận tốc}}\).'),
 (r'Two years of growth at rate \(r\): \(A=P(1+r)^2\).', r'Tăng trưởng hai năm với tỉ lệ \(r\): \(A=P(1+r)^2\).'),
 (r'Key English: set up an equation, suitable condition, express … in terms of x, reject a root, downstream, upstream, current, compound interest.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[lập phương trình]], [[điều kiện thích hợp]], [[biểu diễn … theo x]], [[loại (nghiệm)]], [[xuôi dòng]], [[ngược dòng]], [[dòng nước]], [[lãi kép]].')]
checks = [
 (r'I can state the steps of solving a problem by setting up an equation.', r'Em nêu được các bước giải bài toán bằng cách lập phương trình.'),
 (r'I can choose the unknown and its condition.', r'Em chọn được ẩn và đặt được điều kiện.'),
 (r'I can solve area, productivity and motion problems.', r'Em giải được bài toán diện tích, năng suất, chuyển động.'),
 (r'I can solve river and percentage-growth problems.', r'Em giải được bài toán xuôi – ngược dòng và tăng trưởng phần trăm.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Solving Problems by Setting Up Equations', title_vi='Giải bài toán bằng cách lập phương trình', topic=TOPIC,
       folder='quadratic-functions-equations', file='word-problems-quadratic', catalog_title_vi='Giải bài toán bằng cách lập phương trình',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Word problems on area, productivity, motion, river currents and percentage growth leading to quadratic equations.', level='Intermediate', minutes=90,
       description_vi='Bài 21 – Giải bài toán bằng cách lập phương trình bậc hai: diện tích, năng suất, chuyển động, xuôi – ngược dòng, tăng trưởng phần trăm.',
       tags_vi=['lập phương trình', 'bài toán thực tế', 'phương trình bậc hai'], prerequisites=['g9-quadratic-02'], tags=['word problems', 'quadratic equation', 'modeling'], order=210)
