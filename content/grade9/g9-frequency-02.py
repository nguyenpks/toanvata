# -*- coding: utf-8 -*-
"""Nội dung bài g9-frequency-02 = Toán 9 KNTT, Bài 23: Bảng tần số tương đối và biểu đồ tần số tương đối – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 7 – Lesson 23."""
import os, sys
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9, sp_g9s
from chart_g9 import CHART, HT

LID = 'g9-frequency-02'
CH = 'Tần số và tần số tương đối'
TOPIC = ('Frequency and Relative Frequency', CH)
ensure_vocab([
 ('g9-rel-freq', 'relative frequency', 'tần số tương đối', CH, 'The relative frequency of 8 is 35%.', ''),
 ('g9-rel-table', 'relative frequency table', 'bảng tần số tương đối', CH, 'Make the relative frequency table.', ''),
 ('g9-rel-chart', 'relative frequency chart', 'biểu đồ tần số tương đối', CH, 'Draw a relative frequency chart.', ''),
 ('g9-pie-chart', 'pie chart', 'biểu đồ hình quạt tròn', CH, 'The pie chart shows the favorite sports of 40 students.', ''),
 ('g9-pct-point', 'percentage point', 'điểm phần trăm', CH, 'The proportion rose by 5 percentage points.', ''),
])
load_vocab()

pe, pv = sp_g9s.pe, sp_g9s.pv
def P(x): return ('\\(%s\\%%\\)' % pe(x), '\\(%s\\%%\\)' % pv(x).replace(',', '{,}'))

# ---------- số liệu (kiểm tra bằng máy) ----------
SIB = [(0, 4), (1, 10), (2, 4), (3, 2)]                         # Ví dụ 1 (số liệu Bài 22, Ví dụ 1)
assert sum(m for _, m in SIB) == 20 and F(10, 20) * 100 == 50 and F(2, 20) * 100 == 10
SPORT = [(('Football', 'Bóng đá'), 14), (('Badminton', 'Cầu lông'), 10), (('Swimming', 'Bơi lội'), 9), (('Chess', 'Cờ vua'), 7)]
NS = sum(m for _, m in SPORT); assert NS == 40
SF = [F(100 * m, NS) for _, m in SPORT]; assert SF == [35, 25, F(45, 2), F(35, 2)] and sum(SF) == 100
ANG = [f * F(18, 5) for f in SF]; assert ANG == [126, 90, 81, 63] and sum(ANG) == 360
SC = [(6, 3), (7, 5), (8, 7), (9, 3), (10, 2)]                  # phần lí thuyết (số liệu Bài 22)
SCF = [F(100 * m, 20) for _, m in SC]; assert SCF == [15, 25, 35, 15, 10]
A9, B9 = (40, 14), (32, 12)                                      # Ví dụ 5
fa, fb = F(100 * A9[1], A9[0]), F(100 * B9[1], B9[0]); assert fa == 35 and fb == F(75, 2) and fb - fa == F(5, 2)

meta = dict(level=('Basic', 'Cơ bản'), time=('about 90 minutes', '90 phút'), before=('Lesson 22; percentages (Grade 6)', 'Bài 22; tỉ số phần trăm (lớp 6)'))
goals = [
 (r'state the definition of relative frequency \(f=\dfrac{m}{n}\cdot100\%\);', r'nêu được định nghĩa tần số tương đối \(f=\dfrac{m}{n}\cdot100\%\);'),
 (r'make a relative frequency table;', r'lập được bảng tần số tương đối;'),
 (r'draw and read relative frequency bar charts and pie charts;', r'vẽ và đọc được biểu đồ tần số tương đối dạng cột và dạng hình quạt tròn;'),
 (r'compare samples of different sizes using relative frequencies.', r'so sánh được hai mẫu có cỡ mẫu khác nhau nhờ tần số tương đối.')]
vocab = [
 (r'<b>relative frequency</b> – the frequency as a percentage of the sample size.', r'[[Tần số tương đối]] – tần số tính theo tỉ số phần trăm so với cỡ mẫu.'),
 (r'<b>relative frequency table</b> – a table of values and their relative frequencies.', r'[[Bảng tần số tương đối]] – bảng ghi các giá trị và tần số tương đối của chúng.'),
 (r'<b>relative frequency chart</b> – a bar chart or a pie chart of relative frequencies.', r'[[Biểu đồ tần số tương đối]] – biểu đồ cột hoặc hình quạt tròn biểu diễn tần số tương đối.'),
 (r'<b>pie chart</b> – a circle divided into sectors; the whole circle is 100%.', r'[[Biểu đồ hình quạt tròn]] – hình tròn chia thành các hình quạt; cả hình tròn ứng với 100%.'),
 (r'<b>proportion / percentage point</b> – a share of the whole / the difference between two percentages.', r'Tỉ lệ / [[điểm phần trăm]] – phần so với toàn thể / hiệu của hai tỉ số phần trăm.')]
phrases = [
 (r'<b>The relative frequency of “football” is 35%.</b>', r'Tần số tương đối của “bóng đá” là 35%.'),
 (r'<b>The relative frequencies add up to 100%.</b>', r'Tổng các tần số tương đối bằng 100%.'),
 (r'<b>The sector for “swimming” has a central angle of 81°.</b>', r'Hình quạt ứng với “bơi lội” có góc ở tâm 81°.'),
 (r'<b>The proportion in class 9B is higher than in class 9A.</b>', r'Tỉ lệ ở lớp 9B cao hơn ở lớp 9A.'),
 (r'<b>It rose by 2.5 percentage points.</b>', r'Tỉ lệ đó tăng 2,5 điểm phần trăm.')]
review = (T(r'<b>Lesson 22.</b> The frequency \(m\) of a value is the number of times it appears; \(n\) is the sample size.', r'<b>Bài 22.</b> Tần số \(m\) của một giá trị là số lần giá trị đó xuất hiện; \(n\) là cỡ mẫu.') +
          T(r'<b>Grade 6.</b> The percentage of \(a\) out of \(b\) is \(\dfrac{a}{b}\cdot100\%\).', r'<b>Lớp 6.</b> Tỉ số phần trăm của \(a\) so với \(b\) là \(\dfrac{a}{b}\cdot100\%\).'))

theory = '<h3>5.1 %s</h3>' % TI('Relative frequency and the relative frequency table', 'Tần số tương đối và bảng tần số tương đối')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'The <b>relative frequency</b> \(f_i\) of a value \(x_i\) is the ratio of its frequency \(m_i\) to the sample size \(n\), written as a percentage:',
    r'[[Tần số tương đối]] \(f_i\) của giá trị \(x_i\) là tỉ số giữa tần số \(m_i\) của giá trị đó và cỡ mẫu \(n\), viết dưới dạng phần trăm:'),
  M(r'f_i=\dfrac{m_i}{n}\cdot100\%'),
  T(r'A <b>relative frequency table</b> lists the values and their relative frequencies:', r'[[Bảng tần số tương đối]] ghi các giá trị và tần số tương đối tương ứng:'),
  HT([(('Value (x)', 'Giá trị (x)'), ['\\(x_1\\)', '\\(x_2\\)', '\\(\\dots\\)', '\\(x_k\\)']), (('Relative frequency (f)', 'Tần số tương đối (f)'), ['\\(f_1\\)', '\\(f_2\\)', '\\(\\dots\\)', '\\(f_k\\)'])]),
  T(r'Always \(f_1+f_2+\dots+f_k=100\%\).', r'Luôn có \(f_1+f_2+\dots+f_k=100\%\).'))
theory += T(r'<b>For example,</b> for the scores of 20 students in Lesson 22 (frequencies 3, 5, 7, 3, 2):', r'<b>Ví dụ,</b> với điểm của 20 học sinh ở Bài 22 (tần số 3, 5, 7, 3, 2):')
theory += HT([(('Score (x)', 'Điểm (x)'), [x for x, _ in SC]), (('Relative frequency (f)', 'Tần số tương đối (f)'), [P(f) for f in SCF])])
theory += T(r'For example \(f=\dfrac{7}{20}\cdot100\%=35\%\) for the score 8. Check: \(15+25+35+15+10=100\).', r'Chẳng hạn điểm 8 có \(f=\dfrac{7}{20}\cdot100\%=35\%\). Kiểm tra: \(15+25+35+15+10=100\).')
theory += BOX('yellow', ('Note', 'Chú ý'),
  T(r'When a relative frequency is not a whole number, we may round it (for example to one decimal place); then the sum may differ slightly from 100%.',
    r'Khi tần số tương đối không là số nguyên, có thể làm tròn (chẳng hạn đến hàng phần mười); khi đó tổng có thể lệch một chút so với 100%.'))
theory += '<h3>5.2 %s</h3>' % TI('Relative frequency charts', 'Biểu đồ tần số tương đối')
theory += BOX('mint', ('Two kinds of chart', 'Hai dạng biểu đồ'),
  UL([T(r'<b>Bar chart:</b> like a frequency bar chart, but the height of each bar is the relative frequency (%).', r'<b>Dạng cột:</b> như biểu đồ tần số dạng cột nhưng chiều cao mỗi cột là tần số tương đối (%).'),
      T(r'<b>Pie chart:</b> the whole circle is 100%; the sector of \(x_i\) has central angle \(f_i\cdot360^\circ\).', r'<b>Dạng hình quạt tròn:</b> cả hình tròn ứng với 100%; hình quạt của \(x_i\) có góc ở tâm bằng \(f_i\cdot360^\circ\).')]))
SCE = dict(cats=[x for x, _ in SC], vals=[float(f) for f in SCF], xlab='Score', ylab='Relative frequency', title='Scores of 20 students', pct=True)
SCV = dict(cats=[x for x, _ in SC], vals=[float(f) for f in SCF], xlab='Điểm', ylab='Tần số tương đối', title='Điểm của 20 học sinh', pct=True)
theory += CHART('bar', SCE, SCV, cap=('Relative frequency bar chart', 'Biểu đồ tần số tương đối dạng cột'))
theory += CHART('pie', dict(cats=[str(x) for x, _ in SC], pcts=[float(f) for f in SCF], title='Scores of 20 students'),
                dict(cats=[str(x) for x, _ in SC], pcts=[float(f) for f in SCF], title='Điểm của 20 học sinh'), cap=('Relative frequency pie chart', 'Biểu đồ tần số tương đối dạng hình quạt tròn'), px=460)
theory += BOX('yellow', ('Why relative frequency?', 'Vì sao dùng tần số tương đối?'),
  T(r'To compare two samples of <b>different sizes</b>, compare proportions (relative frequencies), not frequencies.', r'Muốn so sánh hai mẫu có <b>cỡ mẫu khác nhau</b>, ta so sánh tỉ lệ (tần số tương đối), không so sánh tần số.'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('One relative frequency', 'Tính một tần số tương đối'),
  T(r'The frequency table shows the number of siblings of 20 students. Find the relative frequencies of the values 1 and 3.', r'Bảng tần số sau cho biết số anh chị em ruột của 20 học sinh. Tìm tần số tương đối của các giá trị 1 và 3.') +
  HT([(('Number of siblings (x)', 'Số anh chị em ruột (x)'), [x for x, _ in SIB]), (('Frequency (m)', 'Tần số (m)'), [m for _, m in SIB])]),
  ('Use \\(f=\\dfrac{m}{n}\\cdot100\\%\\) with \\(n=20\\).', 'Dùng \\(f=\\dfrac{m}{n}\\cdot100\\%\\) với \\(n=20\\).'),
  [T(r'Value 1: \(f=\dfrac{10}{20}\cdot100\%=50\%\).', r'Giá trị 1: \(f=\dfrac{10}{20}\cdot100\%=50\%\).'),
   T(r'Value 3: \(f=\dfrac{2}{20}\cdot100\%=10\%\).', r'Giá trị 3: \(f=\dfrac{2}{20}\cdot100\%=10\%\).')],
  T(r'50% and 10%.', r'50% và 10%.'))
SP_ROW = (('Sport', 'Môn thể thao'), [s for s, _ in SPORT])
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Favorite sports', 'Môn thể thao yêu thích'),
  T(r'In a survey, 40 students chose their favorite sport. Make the relative frequency table.', r'Trong một cuộc khảo sát, 40 học sinh chọn môn thể thao yêu thích. Lập bảng tần số tương đối.') +
  HT([SP_ROW, (('Frequency (m)', 'Tần số (m)'), [m for _, m in SPORT])]),
  ('Divide each frequency by 40, then multiply by 100%.', 'Chia mỗi tần số cho 40 rồi nhân với 100%.'),
  [T(r'\(\dfrac{14}{40}\cdot100\%=35\%\); \(\dfrac{10}{40}\cdot100\%=25\%\); \(\dfrac{9}{40}\cdot100\%=22.5\%\); \(\dfrac{7}{40}\cdot100\%=17.5\%\).', r'\(\dfrac{14}{40}\cdot100\%=35\%\); \(\dfrac{10}{40}\cdot100\%=25\%\); \(\dfrac{9}{40}\cdot100\%=22{,}5\%\); \(\dfrac{7}{40}\cdot100\%=17{,}5\%\).'),
   T(r'The relative frequency table:', r'Bảng tần số tương đối:') + HT([SP_ROW, (('Relative frequency (f)', 'Tần số tương đối (f)'), [P(f) for f in SF])]),
   T(r'Check: \(35+25+22.5+17.5=100\).', r'Kiểm tra: \(35+25+22{,}5+17{,}5=100\).')],
  T(r'35%, 25%, 22.5%, 17.5%.', r'35%, 25%, 22,5%, 17,5%.'))
SPE = dict(cats=[s[0] for s, _ in SPORT], vals=[float(f) for f in SF], xlab='Sport', ylab='Relative frequency', title='Favorite sports of 40 students', pct=True)
SPV = dict(cats=[s[1] for s, _ in SPORT], vals=[float(f) for f in SF], xlab='Môn thể thao', ylab='Tần số tương đối', title='Môn thể thao yêu thích của 40 học sinh', pct=True)
examples += EXAMPLE(3, ('Basic application', 'Vận dụng thấp'), ('A relative frequency bar chart', 'Biểu đồ cột tần số tương đối'),
  T(r'Draw the relative frequency bar chart for the table in Example 2. Which sport is chosen by about a quarter of the students?', r'Vẽ biểu đồ tần số tương đối dạng cột cho bảng ở Ví dụ 2. Môn thể thao nào được khoảng một phần tư số học sinh chọn?'),
  ('The heights of the bars are 35, 25, 22.5 and 17.5 (%).', 'Chiều cao các cột là 35; 25; 22,5 và 17,5 (%).'),
  [T(r'Sports on the horizontal axis, percentages on the vertical axis:', r'Các môn thể thao trên trục ngang, tỉ số phần trăm trên trục đứng:') + CHART('bar', SPE, SPV),
   T(r'A quarter is 25%: badminton.', r'Một phần tư là 25%: cầu lông.')],
  T(r'Badminton.', r'Cầu lông.'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('A pie chart', 'Biểu đồ hình quạt tròn'),
  T(r'Find the central angles and draw the pie chart for the table in Example 2.', r'Tính góc ở tâm của các hình quạt rồi vẽ biểu đồ hình quạt tròn cho bảng ở Ví dụ 2.'),
  ('Central angle \\(=f\\cdot360^\\circ\\).', 'Góc ở tâm \\(=f\\cdot360^\\circ\\).'),
  [T(r'Football: \(35\%\cdot360^\circ=126^\circ\); badminton: \(25\%\cdot360^\circ=90^\circ\); swimming: \(22.5\%\cdot360^\circ=81^\circ\); chess: \(17.5\%\cdot360^\circ=63^\circ\). Check: \(126+90+81+63=360\).',
     r'Bóng đá: \(35\%\cdot360^\circ=126^\circ\); cầu lông: \(25\%\cdot360^\circ=90^\circ\); bơi lội: \(22{,}5\%\cdot360^\circ=81^\circ\); cờ vua: \(17{,}5\%\cdot360^\circ=63^\circ\). Kiểm tra: \(126+90+81+63=360\).'),
   T(r'Draw a circle and the four sectors with these angles; write the percentage on each sector:', r'Vẽ hình tròn và bốn hình quạt có các góc ở tâm trên; ghi tỉ số phần trăm trên mỗi hình quạt:') +
   CHART('pie', dict(cats=SPE['cats'], pcts=SPE['vals'], title='Favorite sports of 40 students'), dict(cats=SPV['cats'], pcts=SPV['vals'], title='Môn thể thao yêu thích của 40 học sinh'), px=460)],
  T(r'126°, 90°, 81°, 63°.', r'126°, 90°, 81°, 63°.'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Comparing two classes', 'So sánh hai lớp'),
  T(r'Class 9A has 40 students and 14 of them like football best. Class 9B has 32 students and 12 of them like football best. Lan says: “More students like football in 9A, so football is more popular in 9A.” Is she right?',
    r'Lớp 9A có 40 học sinh, trong đó 14 em thích bóng đá nhất. Lớp 9B có 32 học sinh, trong đó 12 em thích bóng đá nhất. Lan nói: “Lớp 9A có nhiều bạn thích bóng đá hơn nên bóng đá được ưa thích ở lớp 9A hơn.” Lan nói đúng không?'),
  ('The class sizes are different, so compare relative frequencies.', 'Hai lớp có sĩ số khác nhau nên phải so sánh tần số tương đối.'),
  [T(r'9A: \(f=\dfrac{14}{40}\cdot100\%=35\%\); 9B: \(f=\dfrac{12}{32}\cdot100\%=37.5\%\).', r'9A: \(f=\dfrac{14}{40}\cdot100\%=35\%\); 9B: \(f=\dfrac{12}{32}\cdot100\%=37{,}5\%\).'),
   T(r'\(37.5\%\gt35\%\): the proportion of students who like football is higher in 9B, by \(2.5\) percentage points. Lan is not right: 14 > 12 only because 9A is bigger.',
     r'\(37{,}5\%\gt35\%\): tỉ lệ học sinh thích bóng đá ở lớp 9B cao hơn, hơn \(2{,}5\) điểm phần trăm. Lan nói chưa đúng: 14 > 12 chỉ vì lớp 9A đông hơn.')],
  T(r'No; football is more popular in 9B (37.5% > 35%).', r'Không; bóng đá được ưa thích ở lớp 9B hơn (37,5% > 35%).'))

_SETS = sp_g9.BANK(sp_g9s.L23_GROUPS, start=1, seeds=(3301, 3302, 3303))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Dividing the wrong way.</b> \(f=\dfrac{m}{n}\cdot100\%\), not \(\dfrac{n}{m}\).', r'<b>Chia ngược.</b> \(f=\dfrac{m}{n}\cdot100\%\), không phải \(\dfrac{n}{m}\).'),
 (r'<b>Forgetting “×100%”.</b> \(\dfrac{7}{20}=0.35=35\%\).', r'<b>Quên nhân 100%.</b> \(\dfrac{7}{20}=0{,}35=35\%\).'),
 (r'<b>Wrong central angle.</b> The angle is \(f\cdot360^\circ\), not \(f\) degrees.', r'<b>Sai góc ở tâm.</b> Góc ở tâm là \(f\cdot360^\circ\), không phải \(f\) độ.'),
 (r'<b>Comparing frequencies of samples with different sizes.</b> Compare relative frequencies.', r'<b>So sánh tần số của hai mẫu khác cỡ.</b> Phải so sánh tần số tương đối.')]
summary = [
 (r'Relative frequency: \(f_i=\dfrac{m_i}{n}\cdot100\%\); the relative frequencies add up to \(100\%\).', r'Tần số tương đối: \(f_i=\dfrac{m_i}{n}\cdot100\%\); tổng các tần số tương đối bằng \(100\%\).'),
 (r'Relative frequency charts: bar chart (height = \(f_i\)) and pie chart (central angle \(f_i\cdot360^\circ\)).', r'Biểu đồ tần số tương đối: dạng cột (chiều cao = \(f_i\)) và dạng hình quạt tròn (góc ở tâm \(f_i\cdot360^\circ\)).'),
 (r'Use relative frequencies to compare samples of different sizes.', r'Dùng tần số tương đối để so sánh các mẫu có cỡ mẫu khác nhau.'),
 (r'Key English: relative frequency, relative frequency table, relative frequency chart, pie chart, percentage point.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[tần số tương đối]], [[bảng tần số tương đối]], [[biểu đồ tần số tương đối]], [[biểu đồ hình quạt tròn]], [[điểm phần trăm]].')]
checks = [
 (r'I can compute a relative frequency.', r'Em tính được tần số tương đối.'),
 (r'I can make a relative frequency table.', r'Em lập được bảng tần số tương đối.'),
 (r'I can draw and read relative frequency bar charts and pie charts.', r'Em vẽ và đọc được biểu đồ tần số tương đối dạng cột và dạng hình quạt tròn.'),
 (r'I can compare two samples of different sizes.', r'Em so sánh được hai mẫu có cỡ mẫu khác nhau.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Relative Frequency Tables and Relative Frequency Charts', title_vi='Bảng tần số tương đối và biểu đồ tần số tương đối', topic=TOPIC,
       folder='frequency-relative-frequency', file='relative-frequency-tables-charts', catalog_title_vi='Bảng tần số tương đối và biểu đồ tần số tương đối',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Relative frequency, relative frequency tables, relative frequency bar charts and pie charts, comparing samples of different sizes.', level='Basic', minutes=90,
       description_vi='Bài 23 – Tần số tương đối, bảng tần số tương đối; biểu đồ tần số tương đối dạng cột và hình quạt tròn; so sánh hai mẫu khác cỡ.',
       tags_vi=['tần số tương đối', 'biểu đồ hình quạt tròn', 'tỉ lệ phần trăm'], prerequisites=['g9-frequency-01'], tags=['relative frequency', 'pie chart', 'percentage'], order=230)
