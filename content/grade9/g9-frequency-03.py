# -*- coding: utf-8 -*-
"""Nội dung bài g9-frequency-03 = Toán 9 KNTT, Bài 24: Bảng tần số, tần số tương đối ghép nhóm và biểu đồ – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 9 (2026), Chapter 7 – Lesson 24."""
import os, sys
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g9, sp_g9p
from chart_g9 import HT, BI

LID = 'g9-frequency-03'
CH = 'Tần số và tần số tương đối'
TOPIC = ('Frequency and Relative Frequency', CH)
ensure_vocab([
 ('g9-grouped-ftable', 'grouped frequency table', 'bảng tần số ghép nhóm', CH, 'Make a grouped frequency table with groups of width 5.', ''),
 ('g9-grouped-rtable', 'grouped relative frequency table', 'bảng tần số tương đối ghép nhóm', CH, 'The grouped relative frequency table shows percentages.', ''),
 ('g9-grouped-rchart', 'grouped relative frequency chart', 'biểu đồ tần số tương đối ghép nhóm', CH, 'Draw a grouped relative frequency chart (histogram).', ''),
 ('g9-class-width', 'class width (group width)', 'độ dài nhóm', CH, 'The group [10; 15) has class width 5.', ''),
])
load_vocab()

pe, pv = sp_g9p.pe, sp_g9p.pv
def P(x): return ('\\(%s\\%%\\)' % pe(x), '\\(%s\\%%\\)' % pv(x).replace(',', '{,}'))
def GN(a, b): return sp_g9p.gname(a, b)

# ---------- số liệu (kiểm tra bằng máy) ----------
TED = [5, 10, 15, 20, 25, 30]; TM = [6, 10, 12, 8, 4]                     # thời gian đến trường của 40 học sinh lớp 9A
NT = sum(TM); TF = [F(100 * m, NT) for m in TM]
assert NT == 40 and TF == [15, 25, 30, 20, 10] and sum(TF) == 100
MID = [F(TED[i] + TED[i + 1], 2) for i in range(5)]; assert MID == [F(15, 2), F(25, 2), F(35, 2), F(45, 2), F(55, 2)]
HRAW = [17, 12, 20, 25, 15, 22, 19, 14, 27, 24, 16, 21, 10, 18, 29, 23, 15, 26, 20, 17]   # chiều cao (cm) của 20 cây giống
HED = [10, 15, 20, 25, 30]
HM = [sum(1 for x in HRAW if HED[i] <= x < HED[i + 1]) for i in range(4)]
assert len(HRAW) == 20 and HM == [3, 7, 6, 4] and min(HRAW) == 10 and max(HRAW) == 29
B9 = [4, 6, 7, 5, 3]; NB = sum(B9); assert NB == 25                       # lớp 9B (Ví dụ 5)
A20, B20 = TM[3] + TM[4], B9[3] + B9[4]
assert (A20, B20) == (12, 8) and F(100 * A20, NT) == 30 and F(100 * B20, NB) == 32
ALL = F(100 * (A20 + B20), NT + NB); assert 30 < ALL < 31 and round(float(ALL), 1) == 30.8

TROW = (('Group (minutes)', 'Nhóm (phút)'), [GN(TED[i], TED[i + 1]) for i in range(5)])

def GFIG(ed, vals, lab, title, pct=False, kind='bar', cap=None, px=500):
    fe = sp_g9p.gchart_svg(ed, vals, lab[0][0], lab[0][1], title[0], False, pct, kind)
    fv = sp_g9p.gchart_svg(ed, vals, lab[1][0], lab[1][1], title[1], True, pct, kind)
    c = '<figcaption>%s</figcaption>' % TI(*cap) if cap else ''
    return '<figure class="mbl-fig mbl-figtex">%s%s</figure>' % (BI(fe, fv, title[0], title[1], px), c)

TLAB = (('Time (minutes)', 'Relative frequency'), ('Thời gian (phút)', 'Tần số tương đối'))
TTITLE = ('Time to school of 40 students in class 9A', 'Thời gian đến trường của 40 học sinh lớp 9A')

meta = dict(level=('Basic', 'Cơ bản'), time=('about 90 minutes', '90 phút'), before=('Lesson 23: relative frequency', 'Bài 23: tần số tương đối'))
goals = [
 (r'recognize grouped data, groups \([a;\,b)\), the width and the midpoint of a group;', r'nhận biết được mẫu số liệu ghép nhóm, nhóm \([a;\,b)\), độ dài nhóm và giá trị đại diện của nhóm;'),
 (r'make a grouped frequency table and a grouped relative frequency table;', r'lập được bảng tần số ghép nhóm và bảng tần số tương đối ghép nhóm;'),
 (r'draw and read grouped relative frequency charts (histograms and line charts);', r'vẽ và đọc được biểu đồ tần số tương đối ghép nhóm dạng cột và dạng đoạn thẳng;'),
 (r'choose a suitable grouping and draw conclusions from real data.', r'chọn được cách ghép nhóm phù hợp và rút ra nhận xét từ dữ liệu thực tế.')]
vocab = [
 (r'<b>grouped data</b> – data whose values are put into groups (class intervals) \([a;\,b)\).', r'[[Mẫu số liệu ghép nhóm]] – mẫu số liệu mà các giá trị được xếp vào các nhóm dạng \([a;\,b)\).'),
 (r'<b>group (class interval)</b> \([a;\,b)\) – all values \(x\) with \(a\le x\lt b\); \(a\) is the lower boundary, \(b\) the upper boundary.', r'[[Nhóm|nhóm số liệu]] \([a;\,b)\) – gồm các giá trị \(x\) thỏa mãn \(a\le x\lt b\); \(a\) là đầu mút trái, \(b\) là đầu mút phải.'),
 (r'<b>class width</b> – the difference \(b-a\).', r'[[Độ dài nhóm]] – hiệu \(b-a\).'),
 (r'<b>midpoint (representative value)</b> – the number \(\dfrac{a+b}{2}\).', r'[[Giá trị đại diện]] của nhóm – số \(\dfrac{a+b}{2}\).'),
 (r'<b>grouped frequency table / grouped relative frequency table</b> – tables of the groups and their frequencies / relative frequencies.', r'[[Bảng tần số ghép nhóm]] / [[bảng tần số tương đối ghép nhóm]] – bảng ghi các nhóm cùng tần số / tần số tương đối của chúng.'),
 (r'<b>grouped relative frequency chart</b> – a histogram (touching bars) or a line chart through the midpoints.', r'[[Biểu đồ tần số tương đối ghép nhóm]] – dạng cột (các cột liền nhau) hoặc dạng đoạn thẳng (qua các giá trị đại diện).')]
phrases = [
 (r'<b>Group the data into class intervals of width 5.</b>', r'Ghép số liệu thành các nhóm có độ dài 5.'),
 (r'<b>The value 15 belongs to the group \([15;\,20)\), not to \([10;\,15)\).</b>', r'Giá trị 15 thuộc nhóm \([15;\,20)\), không thuộc nhóm \([10;\,15)\).'),
 (r'<b>The group \([10;\,15)\) has frequency 10 and relative frequency 25%.</b>', r'Nhóm \([10;\,15)\) có tần số 10 và tần số tương đối 25%.'),
 (r'<b>The bars of a histogram touch each other.</b>', r'Các cột của biểu đồ tần số tương đối ghép nhóm dạng cột nằm liền nhau.'),
 (r'<b>Plot each point at the midpoint of its group.</b>', r'Mỗi điểm được đặt tại giá trị đại diện của nhóm.')]
review = (T(r'<b>Lesson 22.</b> The frequency \(m\) of a value is the number of times it appears; the frequencies add up to the sample size \(n\).', r'<b>Bài 22.</b> Tần số \(m\) của một giá trị là số lần giá trị đó xuất hiện; tổng các tần số bằng cỡ mẫu \(n\).') +
          T(r'<b>Lesson 23.</b> Relative frequency \(f=\dfrac{m}{n}\cdot100\%\); the relative frequencies add up to \(100\%\).', r'<b>Bài 23.</b> Tần số tương đối \(f=\dfrac{m}{n}\cdot100\%\); tổng các tần số tương đối bằng \(100\%\).'))

theory = '<h3>5.1 %s</h3>' % TI('Grouped data and the grouped frequency table', 'Mẫu số liệu ghép nhóm và bảng tần số ghép nhóm')
theory += T(r'When the data have many different values (heights, times, masses…), a frequency table of single values is long and hard to read. We put the values into <b>groups</b>.',
            r'Khi mẫu số liệu có nhiều giá trị khác nhau (chiều cao, thời gian, khối lượng…), bảng tần số từng giá trị rất dài và khó nhận xét. Khi đó ta xếp các giá trị vào các <b>nhóm</b>.')
theory += BOX('blue', ('Groups', 'Nhóm số liệu'),
  T(r'A <b>group</b> \([a;\,b)\) contains every value \(x\) with \(a\le x\lt b\): the value \(a\) belongs to the group, the value \(b\) does not (it belongs to the next group \([b;\,c)\)).',
    r'[[Nhóm|nhóm số liệu]] \([a;\,b)\) gồm mọi giá trị \(x\) thỏa mãn \(a\le x\lt b\): giá trị \(a\) thuộc nhóm, giá trị \(b\) không thuộc nhóm (nó thuộc nhóm tiếp theo \([b;\,c)\)).'),
  UL([T(r'\(a\), \(b\): the lower and upper boundaries; \(b-a\): the <b>class width</b>.', r'\(a\), \(b\): đầu mút trái và đầu mút phải; \(b-a\): [[độ dài nhóm]].'),
      T(r'\(\dfrac{a+b}{2}\): the <b>midpoint</b> (representative value) of the group.', r'\(\dfrac{a+b}{2}\): [[giá trị đại diện]] của nhóm.')]),
  T(r'The <b>frequency</b> of a group is the number of values in it. A <b>grouped frequency table</b> lists the groups and their frequencies.',
    r'[[Tần số]] của một nhóm là số giá trị thuộc nhóm đó. [[Bảng tần số ghép nhóm]] ghi các nhóm và tần số tương ứng.'),
  HT([(('Group', 'Nhóm'), ['\\([a_1;\\,a_2)\\)', '\\([a_2;\\,a_3)\\)', '\\(\\dots\\)', '\\([a_k;\\,a_{k+1})\\)']), (('Frequency (m)', 'Tần số (m)'), ['\\(m_1\\)', '\\(m_2\\)', '\\(\\dots\\)', '\\(m_k\\)'])]),
  T(r'Always \(m_1+m_2+\dots+m_k=n\).', r'Luôn có \(m_1+m_2+\dots+m_k=n\).'))
theory += BOX('yellow', ('How to group', 'Cách ghép nhóm'),
  UL([T(r'Usually the groups have the <b>same width</b>; we often choose from 4 to 8 groups.', r'Thường chia các nhóm có <b>cùng độ dài</b>; số nhóm thường từ 4 đến 8.'),
      T(r'The first group must contain the smallest value, the last group the largest value.', r'Nhóm đầu tiên phải chứa giá trị nhỏ nhất, nhóm cuối cùng phải chứa giá trị lớn nhất.'),
      T(r'The last group may be written \([a_k;\,a_{k+1}]\) so that it also contains its upper boundary.', r'Nhóm cuối có thể viết dạng \([a_k;\,a_{k+1}]\) để chứa cả đầu mút phải.')]))
theory += T(r'<b>For example,</b> the time (minutes) that 40 students of class 9A take to go to school:', r'<b>Ví dụ,</b> thời gian (phút) đi từ nhà đến trường của 40 học sinh lớp 9A:')
theory += HT([TROW, (('Frequency (m)', 'Tần số (m)'), TM)])
theory += '<h3>5.2 %s</h3>' % TI('The grouped relative frequency table', 'Bảng tần số tương đối ghép nhóm')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'The <b>relative frequency</b> of the group \(i\) is \(f_i=\dfrac{m_i}{n}\cdot100\%\). The <b>grouped relative frequency table</b> lists the groups and their relative frequencies; \(f_1+f_2+\dots+f_k=100\%\).',
    r'[[Tần số tương đối]] của nhóm thứ \(i\) là \(f_i=\dfrac{m_i}{n}\cdot100\%\). [[Bảng tần số tương đối ghép nhóm]] ghi các nhóm và tần số tương đối tương ứng; \(f_1+f_2+\dots+f_k=100\%\).'))
theory += T(r'For the 40 students: \(\dfrac{6}{40}\cdot100\%=15\%\), \(\dfrac{10}{40}\cdot100\%=25\%\), …', r'Với 40 học sinh trên: \(\dfrac{6}{40}\cdot100\%=15\%\), \(\dfrac{10}{40}\cdot100\%=25\%\), …')
theory += HT([TROW, (('Relative frequency (f)', 'Tần số tương đối (f)'), [P(f) for f in TF])])
theory += '<h3>5.3 %s</h3>' % TI('Grouped relative frequency charts', 'Biểu đồ tần số tương đối ghép nhóm')
theory += BOX('mint', ('Two kinds of chart', 'Hai dạng biểu đồ'),
  UL([T(r'<b>Histogram (bar chart):</b> on the horizontal axis mark the boundaries of the groups; above each group draw a bar whose height is its relative frequency. The bars <b>touch each other</b> (there are no gaps between groups).',
        r'<b>Dạng cột:</b> trên trục ngang ghi các đầu mút của nhóm; trên mỗi nhóm vẽ một cột có chiều cao bằng tần số tương đối của nhóm. Các cột <b>nằm liền nhau</b> (giữa các nhóm không có khoảng trống).'),
      T(r'<b>Line chart:</b> for each group plot the point \((x_i;\,f_i)\), where \(x_i\) is the midpoint of the group; join the points by segments.',
        r'<b>Dạng đoạn thẳng:</b> với mỗi nhóm, vẽ điểm \((x_i;\,f_i)\), trong đó \(x_i\) là giá trị đại diện của nhóm; nối các điểm liên tiếp bằng các đoạn thẳng.')]),
  T(r'In the same way we draw grouped <b>frequency</b> charts (the heights are the frequencies \(m_i\)).', r'Tương tự, ta vẽ biểu đồ <b>tần số</b> ghép nhóm (chiều cao là tần số \(m_i\)).'))
theory += GFIG(TED, TF, TLAB, TTITLE, pct=True, cap=('Grouped relative frequency histogram', 'Biểu đồ tần số tương đối ghép nhóm dạng cột'))
theory += GFIG(TED, TF, TLAB, TTITLE, pct=True, kind='line', cap=('Grouped relative frequency line chart (points at the midpoints 7.5; 12.5; …)', 'Biểu đồ tần số tương đối ghép nhóm dạng đoạn thẳng (các điểm tại giá trị đại diện 7,5; 12,5; …)'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Groups, width and midpoint', 'Nhóm, độ dài nhóm, giá trị đại diện'),
  T(r'The times of the 40 students above are grouped into \([5;\,10)\), \([10;\,15)\), \([15;\,20)\), \([20;\,25)\), \([25;\,30)\). (a) Which group contains a student who needs exactly 15 minutes? (b) What is the class width? (c) What is the midpoint of the group \([20;\,25)\)?',
    r'Thời gian của 40 học sinh ở trên được ghép thành các nhóm \([5;\,10)\), \([10;\,15)\), \([15;\,20)\), \([20;\,25)\), \([25;\,30)\). a) Bạn cần đúng 15 phút thuộc nhóm nào? b) Độ dài mỗi nhóm bằng bao nhiêu? c) Giá trị đại diện của nhóm \([20;\,25)\) là bao nhiêu?'),
  ('A group \\([a;\\,b)\\) contains \\(a\\) but not \\(b\\).', 'Nhóm \\([a;\\,b)\\) chứa \\(a\\) nhưng không chứa \\(b\\).'),
  [T(r'(a) \(15\le15\lt20\): the group \([15;\,20)\) (not \([10;\,15)\), because \(15\) is not less than \(15\)).', r'a) \(15\le15\lt20\): nhóm \([15;\,20)\) (không phải \([10;\,15)\) vì \(15\) không nhỏ hơn \(15\)).'),
   T(r'(b) The width is \(10-5=5\) (minutes).', r'b) Độ dài nhóm là \(10-5=5\) (phút).'),
   T(r'(c) \(\dfrac{20+25}{2}=22.5\).', r'c) \(\dfrac{20+25}{2}=22{,}5\).')],
  T(r'(a) \([15;\,20)\); (b) 5 minutes; (c) 22.5.', r'a) \([15;\,20)\); b) 5 phút; c) 22,5.'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Making a grouped frequency table', 'Lập bảng tần số ghép nhóm'),
  T(r'The heights (cm) of 20 seedlings in a school garden are: %s. Make the grouped frequency table with the groups \([10;\,15)\), \([15;\,20)\), \([20;\,25)\), \([25;\,30)\).' % ', '.join(map(str, HRAW)),
    r'Chiều cao (cm) của 20 cây giống trong vườn trường là: %s. Lập bảng tần số ghép nhóm với các nhóm \([10;\,15)\), \([15;\,20)\), \([20;\,25)\), \([25;\,30)\).' % ', '.join(map(str, HRAW))),
  ('Count the values in each group; a value equal to a boundary goes to the group on its right.', 'Đếm số giá trị thuộc mỗi nhóm; giá trị bằng đầu mút thì xếp vào nhóm bên phải.'),
  [T(r'\([10;\,15)\): 12, 14, 10 → 3 values. \([15;\,20)\): 17, 15, 19, 16, 18, 15, 17 → 7 values.', r'\([10;\,15)\): 12, 14, 10 → 3 giá trị. \([15;\,20)\): 17, 15, 19, 16, 18, 15, 17 → 7 giá trị.'),
   T(r'\([20;\,25)\): 20, 22, 24, 21, 23, 20 → 6 values. \([25;\,30)\): 25, 27, 29, 26 → 4 values. Check: \(3+7+6+4=20\).', r'\([20;\,25)\): 20, 22, 24, 21, 23, 20 → 6 giá trị. \([25;\,30)\): 25, 27, 29, 26 → 4 giá trị. Kiểm tra: \(3+7+6+4=20\).'),
   T(r'The grouped frequency table:', r'Bảng tần số ghép nhóm:') + HT([(('Height (cm)', 'Chiều cao (cm)'), [GN(HED[i], HED[i + 1]) for i in range(4)]), (('Frequency (m)', 'Tần số (m)'), HM)])],
  T(r'Frequencies 3, 7, 6, 4.', r'Tần số lần lượt là 3, 7, 6, 4.'))
examples += EXAMPLE(3, ('Basic application', 'Vận dụng thấp'), ('A grouped relative frequency table', 'Bảng tần số tương đối ghép nhóm'),
  T(r'Make the grouped relative frequency table for the times of the 40 students of class 9A (table in 5.1).', r'Lập bảng tần số tương đối ghép nhóm cho thời gian đến trường của 40 học sinh lớp 9A (bảng ở mục 5.1).'),
  ('Divide each frequency by 40, then multiply by 100%.', 'Chia mỗi tần số cho 40 rồi nhân với 100%.'),
  [T(r'\(\dfrac{6}{40}=15\%\); \(\dfrac{10}{40}=25\%\); \(\dfrac{12}{40}=30\%\); \(\dfrac{8}{40}=20\%\); \(\dfrac{4}{40}=10\%\).', r'\(\dfrac{6}{40}=15\%\); \(\dfrac{10}{40}=25\%\); \(\dfrac{12}{40}=30\%\); \(\dfrac{8}{40}=20\%\); \(\dfrac{4}{40}=10\%\).'),
   HT([TROW, (('Relative frequency (f)', 'Tần số tương đối (f)'), [P(f) for f in TF])]),
   T(r'Check: \(15+25+30+20+10=100\).', r'Kiểm tra: \(15+25+30+20+10=100\).')],
  T(r'15%, 25%, 30%, 20%, 10%.', r'15%, 25%, 30%, 20%, 10%.'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Drawing the charts', 'Vẽ biểu đồ'),
  T(r'Draw the grouped relative frequency histogram and line chart for the table in Example 3. Give the coordinates of the point for the group \([15;\,20)\).', r'Vẽ biểu đồ tần số tương đối ghép nhóm dạng cột và dạng đoạn thẳng cho bảng ở Ví dụ 3. Cho biết tọa độ của điểm ứng với nhóm \([15;\,20)\).'),
  ('Histogram: touching bars of heights 15, 25, 30, 20, 10 (%). Line chart: points at the midpoints 7.5; 12.5; 17.5; 22.5; 27.5.', 'Dạng cột: các cột liền nhau, cao 15; 25; 30; 20; 10 (%). Dạng đoạn thẳng: các điểm tại giá trị đại diện 7,5; 12,5; 17,5; 22,5; 27,5.'),
  [T(r'Histogram: mark 5, 10, 15, 20, 25, 30 on the horizontal axis and draw touching bars (see the first chart in 5.3).', r'Dạng cột: ghi 5, 10, 15, 20, 25, 30 trên trục ngang rồi vẽ các cột liền nhau (xem biểu đồ thứ nhất ở mục 5.3).'),
   T(r'Line chart: the point of \([15;\,20)\) is \(\left(\dfrac{15+20}{2};\,30\right)=(17.5;\,30)\); the five points are joined by segments (second chart in 5.3).', r'Dạng đoạn thẳng: điểm ứng với nhóm \([15;\,20)\) là \(\left(\dfrac{15+20}{2};\,30\right)=(17{,}5;\,30)\); nối năm điểm bằng các đoạn thẳng (biểu đồ thứ hai ở mục 5.3).')],
  T(r'\((17.5;\,30)\).', r'\((17{,}5;\,30)\).'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Should the school run a bus?', 'Có nên mở tuyến xe đưa đón?'),
  T(r'The school will run a school bus if at least 30% of the students of classes 9A and 9B together need 20 minutes or more to go to school. Class 9B has 25 students:', r'Nhà trường sẽ mở tuyến xe đưa đón nếu có ít nhất 30% học sinh của hai lớp 9A và 9B cần từ 20 phút trở lên để đến trường. Lớp 9B có 25 học sinh:') +
  HT([(('Group (minutes)', 'Nhóm (phút)'), [GN(TED[i], TED[i + 1]) for i in range(5)]), (('Frequency – 9B', 'Tần số – 9B'), B9)]) +
  T(r'(a) Which class has the higher proportion of students needing at least 20 minutes? (b) Will the school run the bus?', r'a) Lớp nào có tỉ lệ học sinh cần từ 20 phút trở lên cao hơn? b) Nhà trường có mở tuyến xe không?'),
  ('“At least 20 minutes” = the groups \\([20;\\,25)\\) and \\([25;\\,30)\\). The classes have different sizes, so compare proportions.', '“Từ 20 phút trở lên” gồm hai nhóm \\([20;\\,25)\\) và \\([25;\\,30)\\). Hai lớp có sĩ số khác nhau nên phải so sánh tỉ lệ.'),
  [T(r'9A: \(8+4=12\) students, \(\dfrac{12}{40}\cdot100\%=30\%\). 9B: \(5+3=8\) students, \(\dfrac{8}{25}\cdot100\%=32\%\). So the proportion is higher in 9B (although \(8\lt12\)).',
     r'9A: \(8+4=12\) học sinh, \(\dfrac{12}{40}\cdot100\%=30\%\). 9B: \(5+3=8\) học sinh, \(\dfrac{8}{25}\cdot100\%=32\%\). Vậy tỉ lệ ở lớp 9B cao hơn (dù \(8\lt12\)).'),
   T(r'Both classes: \(\dfrac{12+8}{40+25}\cdot100\%=\dfrac{20}{65}\cdot100\%\approx30.8\%\ge30\%\). The school will run the bus.', r'Cả hai lớp: \(\dfrac{12+8}{40+25}\cdot100\%=\dfrac{20}{65}\cdot100\%\approx30{,}8\%\ge30\%\). Nhà trường sẽ mở tuyến xe.')],
  T(r'(a) 9B (32% > 30%); (b) yes (about 30.8%).', r'a) Lớp 9B (32% > 30%); b) Có (khoảng 30,8%).'))

_SETS = sp_g9.BANK(sp_g9p.L24_GROUPS, start=1, seeds=(2401, 2402, 2403))
practice = LEVEL_PRACTICE(sp_g9.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Putting a boundary value in the wrong group.</b> The value 15 belongs to \([15;\,20)\), not to \([10;\,15)\).', r'<b>Xếp giá trị bằng đầu mút vào sai nhóm.</b> Giá trị 15 thuộc nhóm \([15;\,20)\), không thuộc nhóm \([10;\,15)\).'),
 (r'<b>Confusing the width and the midpoint.</b> \([20;\,25)\) has width \(5\) and midpoint \(22.5\).', r'<b>Nhầm độ dài nhóm với giá trị đại diện.</b> Nhóm \([20;\,25)\) có độ dài \(5\) và giá trị đại diện \(22{,}5\).'),
 (r'<b>Leaving gaps between the bars.</b> In a grouped histogram the bars touch each other.', r'<b>Vẽ các cột cách nhau.</b> Ở biểu đồ ghép nhóm dạng cột, các cột phải nằm liền nhau.'),
 (r'<b>Plotting the line chart at a boundary.</b> Each point is at the midpoint of its group.', r'<b>Đặt điểm của biểu đồ đoạn thẳng tại đầu mút.</b> Mỗi điểm phải đặt tại giá trị đại diện của nhóm.'),
 (r'<b>Comparing frequencies of samples of different sizes.</b> Compare relative frequencies.', r'<b>So sánh tần số của hai mẫu khác cỡ.</b> Phải so sánh tần số tương đối.')]
summary = [
 (r'Group \([a;\,b)\): \(a\le x\lt b\); width \(b-a\); midpoint \(\dfrac{a+b}{2}\).', r'Nhóm \([a;\,b)\): \(a\le x\lt b\); độ dài nhóm \(b-a\); giá trị đại diện \(\dfrac{a+b}{2}\).'),
 (r'Grouped frequency table: \(m_1+\dots+m_k=n\); grouped relative frequency table: \(f_i=\dfrac{m_i}{n}\cdot100\%\), \(f_1+\dots+f_k=100\%\).', r'Bảng tần số ghép nhóm: \(m_1+\dots+m_k=n\); bảng tần số tương đối ghép nhóm: \(f_i=\dfrac{m_i}{n}\cdot100\%\), \(f_1+\dots+f_k=100\%\).'),
 (r'Charts: histogram (touching bars) and line chart (points at the midpoints).', r'Biểu đồ: dạng cột (các cột liền nhau) và dạng đoạn thẳng (các điểm tại giá trị đại diện).'),
 (r'Key English: grouped data, class interval, class width, midpoint, grouped frequency table, grouped relative frequency chart.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[mẫu số liệu ghép nhóm]], [[nhóm|nhóm số liệu]], [[độ dài nhóm]], [[giá trị đại diện]], [[bảng tần số ghép nhóm]], [[biểu đồ tần số tương đối ghép nhóm]].')]
checks = [
 (r'I can tell which group a value belongs to, and find the width and the midpoint of a group.', r'Em biết một giá trị thuộc nhóm nào, tính được độ dài nhóm và giá trị đại diện.'),
 (r'I can make grouped frequency and relative frequency tables.', r'Em lập được bảng tần số và bảng tần số tương đối ghép nhóm.'),
 (r'I can draw and read grouped histograms and line charts.', r'Em vẽ và đọc được biểu đồ ghép nhóm dạng cột và dạng đoạn thẳng.'),
 (r'I can compare grouped data of samples of different sizes.', r'Em so sánh được số liệu ghép nhóm của hai mẫu khác cỡ.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Grouped Frequency and Relative Frequency Tables and Charts', title_vi='Bảng tần số, tần số tương đối ghép nhóm và biểu đồ', topic=TOPIC,
       folder='frequency-relative-frequency', file='grouped-frequency-tables-charts', catalog_title_vi='Bảng tần số, tần số tương đối ghép nhóm và biểu đồ',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Grouped data, groups [a; b), class width and midpoint, grouped frequency and relative frequency tables, histograms and line charts.', level='Basic', minutes=90,
       description_vi='Bài 24 – Mẫu số liệu ghép nhóm; bảng tần số, tần số tương đối ghép nhóm; biểu đồ tần số tương đối ghép nhóm dạng cột và dạng đoạn thẳng.',
       tags_vi=['ghép nhóm', 'bảng tần số ghép nhóm', 'biểu đồ ghép nhóm'], prerequisites=['g9-frequency-02'], tags=['grouped data', 'histogram', 'class interval'], order=240)
