# -*- coding: utf-8 -*-
"""Nội dung bài g9-systems-03 = Toán 9 KNTT, Bài 3: Giải bài toán bằng cách lập hệ phương trình – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 1 – Lesson 3, tr. 10–11; Mini project "The Smart Plan Choice" (tr. 135).
Số liệu tiền tệ của TLTA (đô la) đã đổi sang nghìn đồng. TLTA ghi "system of equations = phương trình" – đúng là "hệ phương trình"."""
import os, sys
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9
from sp_g9 import solve2

LID = 'g9-systems-03'
CH = 'Phương trình và hệ hai phương trình bậc nhất hai ẩn'
TOPIC = ('Linear Equations and Systems of Linear Equations in Two Variables', CH)
ensure_vocab([
 ('g9-unknown', 'unknown', 'ẩn số', CH, 'Let x and y be the unknowns.', ''),
 ('g9-cond-unknown', 'condition for the unknowns', 'điều kiện của ẩn', CH, 'The condition for the unknowns is x > y > 0.', ''),
 ('g9-setup-sys', 'set up a system of equations', 'lập hệ phương trình', CH, 'Use the given information to set up a system of equations.', ''),
 ('g9-respectively', 'respectively', 'lần lượt', CH, 'Let x and y be the numbers of students in class A and class B, respectively.', ''),
 ('g9-exceed', 'exceed (the plan)', 'vượt mức', CH, 'Workshop A exceeded the plan by 15%.', ''),
 ('g9-word-problem', 'word problem', 'bài toán thực tế', CH, 'Solve the word problem by setting up a system of equations.', ''),
])
load_vocab()

# ---------- kiểm tra số liệu ----------
assert solve2(1, 1, 85, 1, -1, 3) == ('one', 44, 41)                          # Ví dụ 1
assert solve2(2, 1, 40, 3, 2, 65) == ('one', 15, 10)                          # Ví dụ 2
assert solve2(24, 6, 1440, 18, 3, 900) == ('one', 30, 120)                    # Ví dụ 3
assert solve2(1, 1, 720, F(115, 100), F(112, 100), 819) == ('one', 420, 300)  # Ví dụ 4
assert solve2(2, 2, 200, 10, -10, 200) == ('one', 60, 40)                     # Ví dụ 5

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 60 minutes', '60 phút'),
            before=('Lesson 2: solving a system; percentages; distance = speed × time', 'Bài 2: giải hệ phương trình; tỉ số phần trăm; quãng đường = vận tốc × thời gian'))
goals = [
 (r'describe the three steps of solving a word problem with a system of equations;', r'nêu được ba bước giải bài toán bằng cách [[lập hệ phương trình]];'),
 (r'choose the unknowns, state their conditions and express the quantities in terms of the unknowns;', r'chọn [[ẩn số]], đặt [[điều kiện của ẩn]] và biểu diễn các đại lượng chưa biết theo ẩn;'),
 (r'solve problems about totals and differences, shopping, productivity, percentages and motion;', r'giải các bài toán về tổng – hiệu, mua bán, năng suất, phần trăm và chuyển động;'),
 (r'check the answer against the conditions and answer in a full sentence.', r'đối chiếu nghiệm với điều kiện và trả lời bằng câu đầy đủ.')]
vocab = [
 (r'<b>unknown</b> – a quantity we do not know yet; we call it \(x\) or \(y\).', r'[[Ẩn số]] – đại lượng chưa biết, thường gọi là \(x\) hoặc \(y\).'),
 (r'<b>condition for the unknowns</b> – what values make sense (e.g. a number of students is a positive whole number).', r'[[Điều kiện của ẩn]] – các giá trị có nghĩa với bài toán (ví dụ số học sinh là số tự nhiên khác 0).'),
 (r'<b>set up a system of equations</b> – turn the words of the problem into two equations.', r'[[Lập hệ phương trình]] – chuyển lời văn của bài toán thành hai phương trình.'),
 (r'<b>respectively</b> – in the same order as listed.', r'[[Lần lượt]] – theo đúng thứ tự đã nêu.'),
 (r'<b>exceed the plan by 15%</b> – make 15% more than planned.', r'[[Vượt mức]] kế hoạch 15% – làm được nhiều hơn kế hoạch 15%.'),
 (r'<b>word problem</b> – a problem told in words about a real situation.', r'[[Bài toán thực tế]] – bài toán được kể bằng lời về một tình huống trong đời sống.')]
phrases = [
 (r'<b>What are the unknowns in this problem?</b>', r'Ẩn số của bài toán là gì?'),
 (r'<b>Let \(x\) and \(y\) be … , respectively.</b>', r'Gọi \(x\) và \(y\) lần lượt là …'),
 (r'<b>The condition for the unknowns is \(x\gt0,\ y\gt0\).</b>', r'Điều kiện của ẩn là \(x\gt0,\ y\gt0\).'),
 (r'<b>From the first piece of information, we have the equation …</b>', r'Từ dữ kiện thứ nhất, ta có phương trình …'),
 (r'<b>The values satisfy the conditions.</b>', r'Các giá trị tìm được thỏa mãn điều kiện.'),
 (r'<b>So the answer is …</b>', r'Vậy …')]
review = (T(r'<b>Lesson 2.</b> Solve a system by substitution or by elimination; check the solution in both equations.', r'<b>Bài 2.</b> Giải hệ bằng phương pháp thế hoặc phương pháp cộng đại số; thử lại nghiệm vào cả hai phương trình.') +
          T(r'<b>Useful formulas.</b> money = price × quantity; distance = speed × time; increasing \(x\) by \(p\%\) gives \(x+\dfrac{p}{100}x\).', r'<b>Công thức hay dùng.</b> Số tiền = đơn giá × số lượng; quãng đường = vận tốc × thời gian; tăng \(x\) thêm \(p\%\) được \(x+\dfrac{p}{100}x\).'))

theory = '<h3>5.1 %s</h3>' % TI('Three steps', 'Ba bước giải bài toán bằng cách lập hệ phương trình')
theory += BOX('blue', ('Steps', 'Các bước'),
  UL([T(r'<b>Step 1. Set up the system.</b> Choose two unknowns and state their conditions. Express the other quantities in terms of the unknowns. Write two equations from the information.', r'<b>Bước 1. Lập hệ phương trình.</b> Chọn hai ẩn số và đặt điều kiện thích hợp cho chúng; biểu diễn các đại lượng chưa biết theo các ẩn; lập hai phương trình từ các dữ kiện.'),
      T(r'<b>Step 2. Solve the system.</b>', r'<b>Bước 2. Giải hệ phương trình.</b>'),
      T(r'<b>Step 3. Check and answer.</b> Check which solutions satisfy the conditions, then answer the question.', r'<b>Bước 3. Kiểm tra và trả lời.</b> Kiểm tra nghiệm có thỏa mãn điều kiện của ẩn không, rồi trả lời câu hỏi của bài toán.')]))
theory += '<h3>5.2 %s</h3>' % TI('Common types of problems', 'Một số dạng bài thường gặp')
theory += TABLE([('Type', 'Dạng bài'), ('Relation to use', 'Mối liên hệ cần dùng')],
  [[TI('total and difference', 'tổng – hiệu'), TI('\\(x+y=S\\), \\(x-y=d\\)', '\\(x+y=S\\), \\(x-y=d\\)')],
   [TI('shopping', 'mua bán'), TI('money = price × quantity', 'số tiền = đơn giá × số lượng')],
   [TI('productivity, percentages', 'năng suất, phần trăm'), TI('increase by \\(p\\%\\): \\(\\left(1+\\dfrac{p}{100}\\right)x\\)', 'tăng thêm \\(p\\%\\): \\(\\left(1+\\dfrac{p}{100}\\right)x\\)')],
   [TI('motion', 'chuyển động'), TI('distance = speed × time; toward each other: the speeds add; same direction: the speeds subtract', 'quãng đường = vận tốc × thời gian; ngược chiều: cộng hai vận tốc; cùng chiều: trừ hai vận tốc')]])
theory += BOX('yellow', ('Watch out!', 'Lưu ý'),
  T(r'Write the units, and remember: a number of people or objects must be a positive whole number; a length, a price or a speed must be positive.', r'Ghi rõ đơn vị. Số người, số đồ vật phải là số tự nhiên khác 0; độ dài, giá tiền, vận tốc phải là số dương.'))

examples = EXAMPLE(1, ('Remembering', 'Biết'), ('Total and difference', 'Tổng và hiệu'),
  T(r'Classes 9A and 9B have 85 students in total. Class 9A has 3 more students than class 9B. How many students does each class have?', r'Hai lớp 9A và 9B có tổng cộng 85 học sinh. Lớp 9A nhiều hơn lớp 9B 3 học sinh. Hỏi mỗi lớp có bao nhiêu học sinh?'),
  ('Two unknowns: the numbers of students of the two classes.', 'Hai ẩn: số học sinh của hai lớp.'),
  [T(r'Let \(x\) and \(y\) be the numbers of students of 9A and 9B, respectively (\(x, y\) natural numbers, \(x\gt y\)).', r'Gọi \(x\), \(y\) lần lượt là số học sinh lớp 9A và 9B (\(x, y\) là số tự nhiên, \(x\gt y\)).'),
   T(r'System: \(\begin{cases}x+y=85\\ x-y=3\end{cases}\). Add: \(2x=88\Rightarrow x=44\); \(y=41\).', r'Ta có hệ \(\begin{cases}x+y=85\\ x-y=3\end{cases}\). Cộng từng vế: \(2x=88\Rightarrow x=44\); \(y=41\).'),
   T(r'Both are natural numbers and \(44\gt41\): the conditions hold.', r'Hai số đều là số tự nhiên và \(44\gt41\): thỏa mãn điều kiện.')],
  T(r'Class 9A has 44 students, class 9B has 41 students.', r'Lớp 9A có 44 học sinh, lớp 9B có 41 học sinh.'))
examples += EXAMPLE(2, ('Understanding', 'Hiểu'), ('Shopping', 'Mua bán'),
  T(r'Two bread rolls and one box of milk cost 40 thousand dong. Three bread rolls and two boxes of milk cost 65 thousand dong. Find the price of each item.', r'Mua 2 ổ bánh mì và 1 hộp sữa hết 40 nghìn đồng; mua 3 ổ bánh mì và 2 hộp sữa hết 65 nghìn đồng. Tìm giá mỗi ổ bánh mì và mỗi hộp sữa.'),
  ('money = price × quantity.', 'Số tiền = đơn giá × số lượng.'),
  [T(r'Let \(x\), \(y\) (thousand dong) be the prices of a bread roll and a box of milk (\(x\gt0,\ y\gt0\)).', r'Gọi \(x\), \(y\) (nghìn đồng) lần lượt là giá một ổ bánh mì và một hộp sữa (\(x\gt0,\ y\gt0\)).'),
   T(r'\(\begin{cases}2x+y=40\\ 3x+2y=65\end{cases}\). From the first: \(y=40-2x\). Substitute: \(3x+80-4x=65\Rightarrow x=15\); \(y=10\).', r'\(\begin{cases}2x+y=40\\ 3x+2y=65\end{cases}\). Từ phương trình thứ nhất: \(y=40-2x\). Thế vào: \(3x+80-4x=65\Rightarrow x=15\); \(y=10\).')],
  T(r'A bread roll costs 15 thousand dong, a box of milk costs 10 thousand dong.', r'Một ổ bánh mì giá 15 nghìn đồng, một hộp sữa giá 10 nghìn đồng.'))
examples += EXAMPLE(3, ('Basic application', 'Vận dụng thấp'), ('Buying plants', 'Mua cây cho vườn trường'),
  T(r'A school buys flowers and bushes for its garden. The first order was 24 flowers and 6 bushes for 1 440 thousand dong. The second order was 18 flowers and 3 bushes for 900 thousand dong. Find the price of one flower and one bush.', r'Trường mua cây hoa và cây bụi cho vườn trường. Lần thứ nhất mua 24 cây hoa và 6 cây bụi hết 1 440 nghìn đồng. Lần thứ hai mua 18 cây hoa và 3 cây bụi hết 900 nghìn đồng. Tìm giá một cây hoa và một cây bụi.'),
  ('Make the coefficients of \\(y\\) equal by multiplying the second equation by 2.', 'Nhân phương trình thứ hai với 2 để hệ số của \\(y\\) bằng nhau.'),
  [T(r'Let \(x\), \(y\) (thousand dong) be the prices of one flower and one bush (\(x, y\gt0\)): \(\begin{cases}24x+6y=1440\\ 18x+3y=900\end{cases}\).', r'Gọi \(x\), \(y\) (nghìn đồng) lần lượt là giá một cây hoa và một cây bụi (\(x, y\gt0\)): \(\begin{cases}24x+6y=1440\\ 18x+3y=900\end{cases}\).'),
   T(r'Multiply the second equation by 2: \(36x+6y=1800\). Subtract the first: \(12x=360\Rightarrow x=30\). Then \(18\cdot30+3y=900\Rightarrow y=120\).', r'Nhân phương trình thứ hai với 2: \(36x+6y=1800\). Trừ phương trình thứ nhất: \(12x=360\Rightarrow x=30\). Khi đó \(18\cdot30+3y=900\Rightarrow y=120\).')],
  T(r'A flower costs 30 thousand dong, a bush costs 120 thousand dong.', r'Một cây hoa giá 30 nghìn đồng, một cây bụi giá 120 nghìn đồng.'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Exceeding the plan', 'Vượt mức kế hoạch'),
  T(r'Two workshops planned to make 720 products. Workshop A exceeded its plan by 15% and workshop B by 12%, so together they made 819 products. How many products did each workshop plan to make?', r'Theo kế hoạch, hai tổ sản xuất 720 sản phẩm. Thực tế tổ A vượt mức 15%, tổ B vượt mức 12% kế hoạch của mình nên cả hai tổ làm được 819 sản phẩm. Hỏi theo kế hoạch mỗi tổ phải làm bao nhiêu sản phẩm?'),
  ('Exceeding by 15% means making \\(x+0.15x=1.15x\\).', 'Vượt mức 15% nghĩa là làm được \\(x+0{,}15x=1{,}15x\\).'),
  [T(r'Let \(x\), \(y\) be the planned numbers of products of A and B (\(x, y\) natural numbers less than 720).', r'Gọi \(x\), \(y\) lần lượt là số sản phẩm tổ A, tổ B phải làm theo kế hoạch (\(x, y\) là số tự nhiên nhỏ hơn 720).'),
   T(r'\(\begin{cases}x+y=720\\ 1.15x+1.12y=819\end{cases}\). From the first: \(y=720-x\). Then \(1.15x+806.4-1.12x=819\Rightarrow 0.03x=12.6\Rightarrow x=420\); \(y=300\).', r'\(\begin{cases}x+y=720\\ 1{,}15x+1{,}12y=819\end{cases}\). Từ phương trình thứ nhất: \(y=720-x\). Suy ra \(1{,}15x+806{,}4-1{,}12x=819\Rightarrow 0{,}03x=12{,}6\Rightarrow x=420\); \(y=300\).'),
   T(r'Check: \(1.15\cdot420+1.12\cdot300=483+336=819\) ✓.', r'Thử lại: \(1{,}15\cdot420+1{,}12\cdot300=483+336=819\) ✓.')],
  T(r'Workshop A planned 420 products, workshop B planned 300 products.', r'Theo kế hoạch, tổ A làm 420 sản phẩm, tổ B làm 300 sản phẩm.'))
assert F(115, 100) * 420 == 483 and F(112, 100) * 300 == 336
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Two cars', 'Hai ô tô'),
  T(r'Two towns are 200 km apart. Two cars start from the two towns at the same time. If they drive toward each other, they meet after 2 hours. If they drive in the same direction, the faster car catches up with the slower one after 10 hours. Find the speed of each car.', r'Hai thị trấn cách nhau 200 km. Hai ô tô khởi hành cùng lúc từ hai thị trấn. Nếu đi ngược chiều thì sau 2 giờ chúng gặp nhau. Nếu đi cùng chiều thì sau 10 giờ xe nhanh đuổi kịp xe chậm. Tính vận tốc mỗi xe.'),
  ('Toward each other: together they cover 200 km. Same direction: the faster car gains 200 km.', 'Ngược chiều: tổng quãng đường hai xe đi là 200 km. Cùng chiều: xe nhanh đi nhiều hơn xe chậm 200 km.'),
  [T(r'Let \(x\), \(y\) (km/h) be the speeds of the faster and the slower car (\(x\gt y\gt0\)).', r'Gọi \(x\), \(y\) (km/h) lần lượt là vận tốc của xe nhanh và xe chậm (\(x\gt y\gt0\)).'),
   T(r'\(\begin{cases}2x+2y=200\\ 10x-10y=200\end{cases}\Leftrightarrow\begin{cases}x+y=100\\ x-y=20\end{cases}\Rightarrow x=60,\ y=40\).', r'\(\begin{cases}2x+2y=200\\ 10x-10y=200\end{cases}\Leftrightarrow\begin{cases}x+y=100\\ x-y=20\end{cases}\Rightarrow x=60,\ y=40\).'),
   T(r'\(60\gt40\gt0\): the conditions hold.', r'\(60\gt40\gt0\): thỏa mãn điều kiện.')],
  T(r'The speeds are 60 km/h and 40 km/h.', r'Vận tốc hai xe là 60 km/h và 40 km/h.'))

_SETS = sp_g9.BANK(sp_g9.L3_GROUPS, start=1, seeds=(1301, 1302, 1303))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>No conditions for the unknowns.</b> Always write them (e.g. \(x, y\) natural numbers) and check them at the end.', r'<b>Không đặt điều kiện cho ẩn.</b> Luôn viết điều kiện (ví dụ \(x, y\) là số tự nhiên) và đối chiếu ở bước cuối.'),
 (r'<b>Mixing up the unknowns.</b> Say clearly which quantity is \(x\) and which is \(y\) (“respectively”).', r'<b>Nhầm hai ẩn.</b> Nói rõ đại lượng nào là \(x\), đại lượng nào là \(y\) (dùng từ “lần lượt”).'),
 (r'<b>Wrong percentage.</b> Exceeding by 15% gives \(1.15x\), not \(0.15x\) and not \(x+15\).', r'<b>Sai phần trăm.</b> Vượt mức 15% được \(1{,}15x\), không phải \(0{,}15x\) hay \(x+15\).'),
 (r'<b>Adding speeds in the wrong case.</b> Toward each other: add the speeds; same direction: subtract them.', r'<b>Cộng vận tốc sai trường hợp.</b> Ngược chiều thì cộng hai vận tốc; cùng chiều thì trừ.'),
 (r'<b>No final answer.</b> End with a sentence that answers the question, with units.', r'<b>Không trả lời.</b> Kết thúc bằng câu trả lời đầy đủ, có đơn vị.')]
summary = [
 (r'Three steps: set up the system – solve it – check the conditions and answer.', r'Ba bước: lập hệ phương trình – giải hệ – kiểm tra điều kiện và trả lời.'),
 (r'Choose the unknowns carefully, state their conditions and units.', r'Chọn ẩn cẩn thận, ghi rõ điều kiện và đơn vị.'),
 (r'Useful relations: money = price × quantity; distance = speed × time; increase by \(p\%\): \(\left(1+\dfrac{p}{100}\right)x\).', r'Các mối liên hệ hay dùng: số tiền = đơn giá × số lượng; quãng đường = vận tốc × thời gian; tăng \(p\%\): \(\left(1+\dfrac{p}{100}\right)x\).'),
 (r'Key English: let \(x\) and \(y\) be …, respectively; the condition for the unknowns is …', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[ẩn số]], [[lần lượt]], [[điều kiện của ẩn]], [[lập hệ phương trình]].')]
checks = [
 (r'I can list the three steps of solving a word problem with a system.', r'Em nêu được ba bước giải bài toán bằng cách lập hệ phương trình.'),
 (r'I can choose the unknowns and state their conditions.', r'Em chọn được ẩn và đặt được điều kiện cho ẩn.'),
 (r'I can set up and solve systems for shopping, percentage and motion problems.', r'Em lập và giải được hệ cho các bài toán mua bán, phần trăm, chuyển động.'),
 (r'I can check the answer and write a full answer with units.', r'Em kiểm tra được nghiệm và trả lời đầy đủ, có đơn vị.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Solving Word Problems Using Systems of Equations', title_vi='Giải bài toán bằng cách lập hệ phương trình', topic=TOPIC,
       folder='systems-of-equations', file='word-problems-systems', catalog_title_vi='Giải bài toán bằng cách lập hệ phương trình',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Setting up and solving systems of two linear equations for real-world problems.', level='Intermediate', minutes=60,
       description_vi='Bài 3 – Ba bước giải bài toán bằng cách lập hệ phương trình; các dạng tổng – hiệu, mua bán, năng suất, phần trăm, chuyển động.',
       tags_vi=['lập hệ phương trình', 'bài toán thực tế', 'chuyển động', 'phần trăm'],
       prerequisites=['g9-systems-02'], tags=['word problem', 'system', 'modelling'], order=30)
