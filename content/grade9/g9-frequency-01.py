# -*- coding: utf-8 -*-
"""Nội dung bài g9-frequency-01 = Toán 9 KNTT, Bài 22: Bảng tần số và biểu đồ tần số – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 7 – Lesson 22."""
import os, sys, random
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9, sp_g9s
from chart_g9 import CHART, HT

LID = 'g9-frequency-01'
CH = 'Tần số và tần số tương đối'
TOPIC = ('Frequency and Relative Frequency', CH)
ensure_vocab([
 ('g9-data-set', 'data set (sample)', 'mẫu dữ liệu', CH, 'The data set has 20 values.', ''),
 ('g9-freq-chart', 'frequency chart', 'biểu đồ tần số', CH, 'Draw a frequency chart for the table.', ''),
 ('g9-bar-chart', 'bar chart', 'biểu đồ cột', CH, 'The bar chart shows the frequency of each value.', ''),
 ('g9-line-graph', 'line graph', 'biểu đồ đoạn thẳng', CH, 'Join the points to make a line graph.', ''),
 ('g9-h-axis', 'horizontal axis', 'trục ngang', CH, 'Write the values on the horizontal axis.', ''),
 ('g9-v-axis', 'vertical axis', 'trục đứng', CH, 'Write the frequencies on the vertical axis.', ''),
])
load_vocab()


def shuffled(counts, seed):
    d = [x for x, m in counts for _ in range(m)]
    random.Random(seed).shuffle(d)
    assert Counter(d) == Counter(dict(counts))
    return d

# ---------- số liệu (kiểm tra bằng máy) ----------
SC = [(6, 3), (7, 5), (8, 7), (9, 3), (10, 2)]              # điểm 20 học sinh (phần lí thuyết)
SC_D = shuffled(SC, 22)
assert sum(m for _, m in SC) == 20
SIB = [(0, 4), (1, 10), (2, 4), (3, 2)]                      # Ví dụ 1: số anh chị em ruột
SIB_D = shuffled(SIB, 221); assert len(SIB_D) == 20
SHOE = [(37, 3), (38, 6), (39, 8), (40, 5), (41, 2)]        # Ví dụ 2, 3: cỡ giày
SHOE_D = shuffled(SHOE, 222); assert len(SHOE_D) == 24
GOAL = [(0, 3), (1, 7), (2, 9), (3, 6), (4, 4), (5, 1)]     # Ví dụ 4: số bàn thắng
assert sum(m for _, m in GOAL) == 30 and 6 + 4 + 1 == 11 and 3 + 7 == 10
AQ = [9, 12, 6, 3]                                           # Ví dụ 5: chất lượng không khí 30 ngày
assert sum(AQ) == 30 and AQ[0] + AQ[1] == 21 and AQ[2] + AQ[3] == 9
L = lambda d: ', '.join(map(str, d))

meta = dict(level=('Basic', 'Cơ bản'), time=('about 90 minutes', '90 phút'), before=('collecting and showing data (Grades 6–8)', 'thu thập và biểu diễn dữ liệu (lớp 6–8)'))
goals = [
 (r'recognize the frequency of a value and a frequency table;', r'nhận biết được tần số của một giá trị và bảng tần số;'),
 (r'make a frequency table from a data set;', r'lập được bảng tần số từ một mẫu dữ liệu;'),
 (r'draw and read frequency bar charts and line graphs;', r'vẽ và đọc được biểu đồ tần số dạng cột, dạng đoạn thẳng;'),
 (r'draw conclusions from real data (air quality, sizes, scores).', r'nhận xét, rút ra kết luận từ dữ liệu thực tế (chất lượng không khí, cỡ giày, điểm số).')]
vocab = [
 (r'<b>data set</b> – the collected values, e.g. the scores of 20 students.', r'[[Mẫu dữ liệu]] – các giá trị thu thập được, ví dụ điểm của 20 học sinh.'),
 (r'<b>frequency</b> – the number of times a value appears; symbol \(m\).', r'[[Tần số]] – số lần xuất hiện của một giá trị; kí hiệu \(m\).'),
 (r'<b>sample size</b> – the number of values in the data set; \(n=m_1+\dots+m_k\).', r'[[Cỡ mẫu]] – số giá trị của mẫu dữ liệu; \(n=m_1+\dots+m_k\).'),
 (r'<b>frequency table</b> – a table listing each value with its frequency.', r'[[Bảng tần số]] – bảng ghi mỗi giá trị kèm tần số của nó.'),
 (r'<b>frequency chart: bar chart / line graph</b> – a picture of a frequency table.', r'[[Biểu đồ tần số]]: [[biểu đồ cột]] / [[biểu đồ đoạn thẳng]] – hình ảnh của bảng tần số.'),
 (r'<b>horizontal axis / vertical axis</b> – values / frequencies.', r'[[Trục ngang]] / [[trục đứng]] – các giá trị / các tần số.')]
phrases = [
 (r'<b>The value 8 appears 7 times, so its frequency is 7.</b>', r'Giá trị 8 xuất hiện 7 lần nên tần số của nó là 7.'),
 (r'<b>The sample size is \(n=20\).</b>', r'Cỡ mẫu là \(n=20\).'),
 (r'<b>The tallest bar shows the most common value.</b>', r'Cột cao nhất cho biết giá trị xuất hiện nhiều nhất.'),
 (r'<b>From the chart, we can see that…</b>', r'Từ biểu đồ, ta thấy rằng…'),
 (r'<b>A survey of 30 days shows that…</b>', r'Kết quả khảo sát trong 30 ngày cho thấy…')]
review = (T(r'<b>Grade 6–7.</b> A bar chart shows data by bars; a line graph joins points by line segments.', r'<b>Lớp 6–7.</b> Biểu đồ cột biểu diễn dữ liệu bằng các cột; biểu đồ đoạn thẳng nối các điểm bằng đoạn thẳng.') +
          T(r'<b>Grade 8.</b> Collect, sort and present data in tables and charts.', r'<b>Lớp 8.</b> Thu thập, phân loại và biểu diễn dữ liệu bằng bảng, biểu đồ.'))

SC_TAB = HT([(('Score (x)', 'Điểm (x)'), [x for x, _ in SC]), (('Frequency (m)', 'Tần số (m)'), [m for _, m in SC])])
theory = '<h3>5.1 %s</h3>' % TI('Frequency and frequency table', 'Tần số và bảng tần số')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'Suppose a data set has \(k\) different values \(x_1, x_2, \dots, x_k\). The <b>frequency</b> \(m_i\) of the value \(x_i\) is the number of times \(x_i\) appears in the data set. The sum \(n=m_1+m_2+\dots+m_k\) is the <b>sample size</b>.',
    r'Giả sử [[mẫu dữ liệu]] có \(k\) giá trị khác nhau \(x_1, x_2, \dots, x_k\). [[Tần số]] \(m_i\) của giá trị \(x_i\) là số lần \(x_i\) xuất hiện trong mẫu dữ liệu. Tổng \(n=m_1+m_2+\dots+m_k\) là [[cỡ mẫu]].'),
  T(r'A <b>frequency table</b> lists the values in the first row and their frequencies in the second row:', r'[[Bảng tần số]] ghi các giá trị ở dòng thứ nhất và tần số tương ứng ở dòng thứ hai:'),
  HT([(('Value (x)', 'Giá trị (x)'), ['\\(x_1\\)', '\\(x_2\\)', '\\(\\dots\\)', '\\(x_k\\)']), (('Frequency (m)', 'Tần số (m)'), ['\\(m_1\\)', '\\(m_2\\)', '\\(\\dots\\)', '\\(m_k\\)'])]))
theory += T(r'<b>For example,</b> the test scores of 20 students are: %s. The frequency table is:' % L(SC_D), r'<b>Ví dụ,</b> điểm bài kiểm tra của 20 học sinh là: %s. Bảng tần số là:' % L(SC_D))
theory += SC_TAB
theory += T(r'The score 8 has the greatest frequency (7); the sample size is \(n=3+5+7+3+2=20\).', r'Điểm 8 có tần số lớn nhất (7); cỡ mẫu là \(n=3+5+7+3+2=20\).')
theory += '<h3>5.2 %s</h3>' % TI('Frequency charts', 'Biểu đồ tần số')
theory += BOX('mint', ('How to draw', 'Cách vẽ'),
  UL([T(r'<b>Bar chart:</b> write the values on the horizontal axis and the frequencies on the vertical axis; draw a bar above each value with height equal to its frequency.',
        r'<b>Dạng cột:</b> ghi các giá trị trên [[trục ngang]], tần số trên [[trục đứng]]; vẽ mỗi cột có chiều cao bằng tần số của giá trị tương ứng.'),
      T(r'<b>Line graph:</b> mark the points \((x_i;\ m_i)\) and join each point to the next one by a line segment.', r'<b>Dạng đoạn thẳng:</b> đánh dấu các điểm \((x_i;\ m_i)\) rồi nối mỗi điểm với điểm kế tiếp bằng đoạn thẳng.'),
      T(r'Always give the chart a title and name both axes.', r'Biểu đồ cần có tên và ghi rõ tên hai trục.')]))
SC_EN = dict(cats=[x for x, _ in SC], vals=[m for _, m in SC], xlab='Score', ylab='Frequency', title='Test scores of 20 students')
SC_VI = dict(cats=[x for x, _ in SC], vals=[m for _, m in SC], xlab='Điểm', ylab='Tần số', title='Điểm bài kiểm tra của 20 học sinh')
theory += CHART('bar', SC_EN, SC_VI, cap=('Frequency bar chart', 'Biểu đồ tần số dạng cột'))
theory += CHART('line', SC_EN, SC_VI, cap=('Frequency line graph', 'Biểu đồ tần số dạng đoạn thẳng'))
theory += BOX('yellow', ('Note', 'Chú ý'),
  T(r'The bar chart and the line graph show the same table: the taller the bar (the higher the point), the greater the frequency.', r'Biểu đồ cột và biểu đồ đoạn thẳng cùng biểu diễn một bảng tần số: cột càng cao (điểm càng cao) thì tần số càng lớn.'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Number of siblings', 'Số anh chị em ruột'),
  T(r'The numbers of siblings of 20 students are: %s. a) List the different values. b) Find the frequencies of the values 1 and 3. c) Find the sample size.' % L(SIB_D),
    r'Số anh chị em ruột của 20 học sinh là: %s. a) Nêu các giá trị khác nhau. b) Tìm tần số của các giá trị 1 và 3. c) Tìm cỡ mẫu.' % L(SIB_D)),
  ('Count how many times each value appears.', 'Đếm số lần xuất hiện của mỗi giá trị.'),
  [T(r'a) The different values are 0, 1, 2, 3.', r'a) Các giá trị khác nhau là 0, 1, 2, 3.'),
   T(r'b) The value 1 appears 10 times and the value 3 appears 2 times: \(m=10\) and \(m=2\).', r'b) Giá trị 1 xuất hiện 10 lần, giá trị 3 xuất hiện 2 lần: \(m=10\) và \(m=2\).'),
   T(r'c) \(n=4+10+4+2=20\).', r'c) \(n=4+10+4+2=20\).')],
  T(r'0, 1, 2, 3; frequencies 10 and 2; \(n=20\).', r'0, 1, 2, 3; tần số 10 và 2; \(n=20\).'))
SHOE_TAB = HT([(('Shoe size (x)', 'Cỡ giày (x)'), [x for x, _ in SHOE]), (('Frequency (m)', 'Tần số (m)'), [m for _, m in SHOE])])
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Shoe sizes', 'Cỡ giày'),
  T(r'A shoe shop records the sizes of 24 pairs of shoes sold in one day: %s. Make the frequency table.' % L(SHOE_D),
    r'Một cửa hàng ghi lại cỡ của 24 đôi giày bán được trong một ngày: %s. Lập bảng tần số.' % L(SHOE_D)),
  ('Tick each value as you count, then check that the frequencies add up to 24.', 'Đánh dấu từng giá trị khi đếm, rồi kiểm tra tổng các tần số bằng 24.'),
  [T(r'The values are 37, 38, 39, 40, 41. Counting gives the table:', r'Các giá trị là 37, 38, 39, 40, 41. Đếm được bảng:') + SHOE_TAB,
   T(r'Check: \(3+6+8+5+2=24\).', r'Kiểm tra: \(3+6+8+5+2=24\).')],
  T(r'See the table above.', r'Xem bảng trên.'))
SH_EN = dict(cats=[x for x, _ in SHOE], vals=[m for _, m in SHOE], xlab='Shoe size', ylab='Frequency', title='Shoes sold in one day')
SH_VI = dict(cats=[x for x, _ in SHOE], vals=[m for _, m in SHOE], xlab='Cỡ giày', ylab='Tần số', title='Số đôi giày bán được trong một ngày')
examples += EXAMPLE(3, ('Basic application', 'Vận dụng thấp'), ('Drawing a bar chart', 'Vẽ biểu đồ cột'),
  T(r'Draw the frequency bar chart for the table in Example 2. Which size should the shop order the most?', r'Vẽ biểu đồ tần số dạng cột cho bảng ở Ví dụ 2. Cửa hàng nên nhập nhiều nhất cỡ giày nào?'),
  ('Values on the horizontal axis, frequencies on the vertical axis.', 'Giá trị trên trục ngang, tần số trên trục đứng.'),
  [T(r'Draw five bars above 37, 38, 39, 40, 41 with heights 3, 6, 8, 5, 2:', r'Vẽ năm cột trên các giá trị 37, 38, 39, 40, 41 với chiều cao 3, 6, 8, 5, 2:') + CHART('bar', SH_EN, SH_VI),
   T(r'The tallest bar is at size 39 (8 pairs), so size 39 sells best.', r'Cột cao nhất ứng với cỡ 39 (8 đôi), nên cỡ 39 bán chạy nhất.')],
  T(r'Size 39.', r'Cỡ 39.'))
GO_EN = dict(cats=[x for x, _ in GOAL], vals=[m for _, m in GOAL], xlab='Goals in a match', ylab='Frequency', title='Goals in 30 matches')
GO_VI = dict(cats=[x for x, _ in GOAL], vals=[m for _, m in GOAL], xlab='Số bàn thắng mỗi trận', ylab='Tần số', title='Số bàn thắng trong 30 trận')
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Reading a line graph', 'Đọc biểu đồ đoạn thẳng'),
  T(r'The line graph shows the number of goals in each of the 30 matches of a school football tournament. a) Make the frequency table. b) In how many matches were at least 3 goals scored?',
    r'Biểu đồ đoạn thẳng cho biết số bàn thắng trong mỗi trận của 30 trận đấu ở giải bóng đá của trường. a) Lập bảng tần số. b) Có bao nhiêu trận có từ 3 bàn thắng trở lên?') +
  CHART('line', GO_EN, GO_VI),
  ('Read the height of each point.', 'Đọc độ cao của mỗi điểm.'),
  [T(r'a) Reading the points:', r'a) Đọc các điểm:') + HT([(('Goals (x)', 'Số bàn thắng (x)'), [x for x, _ in GOAL]), (('Frequency (m)', 'Tần số (m)'), [m for _, m in GOAL])]),
   T(r'b) \(6+4+1=11\) matches.', r'b) \(6+4+1=11\) trận.')],
  T(r'b) 11 matches.', r'b) 11 trận.'))
AQ_EN = dict(cats=['Good', 'Moderate', 'Poor', 'Bad'], vals=AQ, xlab='Air quality', ylab='Number of days', title='Air quality in 30 days')
AQ_VI = dict(cats=['Tốt', 'Trung bình', 'Kém', 'Xấu'], vals=AQ, xlab='Chất lượng không khí', ylab='Số ngày', title='Chất lượng không khí trong 30 ngày')
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Air quality', 'Chất lượng không khí'),
  T(r'A city measured its air quality index (AQI) on 30 days and rated each day as Good, Moderate, Poor or Bad. The results are shown in the bar chart. a) Make the frequency table. b) What can you conclude? Give one piece of advice.',
    r'Một thành phố đo chỉ số chất lượng không khí (AQI) trong 30 ngày và xếp mỗi ngày vào một trong các mức Tốt, Trung bình, Kém, Xấu. Kết quả cho ở biểu đồ cột. a) Lập bảng tần số. b) Em rút ra nhận xét gì? Hãy nêu một lời khuyên.') +
  CHART('bar', AQ_EN, AQ_VI),
  ('Compare the “good or moderate” days with the “poor or bad” days.', 'So sánh số ngày “tốt hoặc trung bình” với số ngày “kém hoặc xấu”.'),
  [T(r'a) The frequency table:', r'a) Bảng tần số:') + HT([(('Air quality', 'Chất lượng không khí'), [('Good', 'Tốt'), ('Moderate', 'Trung bình'), ('Poor', 'Kém'), ('Bad', 'Xấu')]), (('Number of days', 'Số ngày'), AQ)]),
   T(r'b) The most common rating is Moderate (12 days). Good or moderate: \(9+12=21\) days; poor or bad: \(6+3=9\) days.', r'b) Mức xuất hiện nhiều nhất là Trung bình (12 ngày). Tốt hoặc trung bình: \(9+12=21\) ngày; kém hoặc xấu: \(6+3=9\) ngày.'),
   T(r'So the air quality is acceptable on most days, but on 9 days of 30 it is unhealthy. Advice: check the AQI every day and wear a mask outdoors on poor or bad days.',
     r'Vậy phần lớn các ngày không khí ở mức chấp nhận được, nhưng có 9 trong 30 ngày không khí có hại cho sức khỏe. Lời khuyên: theo dõi AQI hằng ngày và đeo khẩu trang khi ra ngoài vào những ngày kém, xấu.')],
  T(r'21 good or moderate days, 9 poor or bad days.', r'21 ngày tốt hoặc trung bình, 9 ngày kém hoặc xấu.'))

_SETS = sp_g9.BANK(sp_g9s.L22_GROUPS, start=1, seeds=(3201, 3202, 3203))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Missing a value when counting.</b> Check that the frequencies add up to the sample size.', r'<b>Đếm sót giá trị.</b> Kiểm tra tổng các tần số bằng cỡ mẫu.'),
 (r'<b>Mixing up value and frequency.</b> The value is on the horizontal axis; the frequency is the height.', r'<b>Nhầm giá trị với tần số.</b> Giá trị ở trục ngang; tần số là chiều cao.'),
 (r'<b>Uneven scale.</b> Use equal steps on the vertical axis.', r'<b>Chia trục không đều.</b> Trục đứng phải chia đều.'),
 (r'<b>No title or axis names.</b> A chart must say what it shows.', r'<b>Thiếu tên biểu đồ, tên trục.</b> Biểu đồ phải cho biết nó biểu diễn gì.')]
summary = [
 (r'The frequency \(m_i\) of \(x_i\) is the number of times \(x_i\) appears; \(n=m_1+\dots+m_k\) is the sample size.', r'Tần số \(m_i\) của \(x_i\) là số lần \(x_i\) xuất hiện; \(n=m_1+\dots+m_k\) là cỡ mẫu.'),
 (r'A frequency table has a row of values and a row of frequencies.', r'Bảng tần số gồm dòng các giá trị và dòng các tần số.'),
 (r'Frequency charts: bar chart (bar height = frequency) and line graph (points \((x_i;\ m_i)\) joined by segments).', r'Biểu đồ tần số: dạng cột (chiều cao cột = tần số) và dạng đoạn thẳng (các điểm \((x_i;\ m_i)\) nối bằng đoạn thẳng).'),
 (r'Key English: data set, frequency, sample size, frequency table, frequency chart, bar chart, line graph, horizontal axis, vertical axis.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[mẫu dữ liệu]], [[tần số]], [[cỡ mẫu]], [[bảng tần số]], [[biểu đồ tần số]], [[biểu đồ cột]], [[biểu đồ đoạn thẳng]], [[trục ngang]], [[trục đứng]].')]
checks = [
 (r'I can find the frequency of a value and the sample size.', r'Em tìm được tần số của một giá trị và cỡ mẫu.'),
 (r'I can make a frequency table from a data set.', r'Em lập được bảng tần số từ một mẫu dữ liệu.'),
 (r'I can draw and read frequency bar charts and line graphs.', r'Em vẽ và đọc được biểu đồ tần số dạng cột, dạng đoạn thẳng.'),
 (r'I can draw conclusions from real data.', r'Em rút ra được nhận xét từ dữ liệu thực tế.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Frequency Tables and Frequency Charts', title_vi='Bảng tần số và biểu đồ tần số', topic=TOPIC,
       folder='frequency-relative-frequency', file='frequency-tables-charts', catalog_title_vi='Bảng tần số và biểu đồ tần số',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Frequency of a value, sample size, frequency tables, frequency bar charts and line graphs, reading real data.', level='Basic', minutes=90,
       description_vi='Bài 22 – Tần số, cỡ mẫu, bảng tần số; biểu đồ tần số dạng cột và dạng đoạn thẳng; đọc và nhận xét dữ liệu thực tế.',
       tags_vi=['tần số', 'bảng tần số', 'biểu đồ cột', 'biểu đồ đoạn thẳng'], prerequisites=[], tags=['frequency', 'frequency table', 'bar chart', 'line graph'], order=220)
