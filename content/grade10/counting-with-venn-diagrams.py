# -*- coding: utf-8 -*-
"""g10-sets-02: Counting with Venn Diagrams (bài mới theo khung v2)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
from mb_std import *
from mb_extra import *
import _vocab
S = 'Tập hợp và khoảng'
ensure_vocab([
 ('v-region', 'region', 'vùng', S, 'Write a number in each region.', ''),
 ('v-disjoint-sets', 'disjoint sets', 'hai tập rời nhau', S, 'A and B are disjoint sets.', '\\(A\\cap B=\\varnothing\\)'),
 ('v-inclusion-exclusion', 'inclusion–exclusion formula', 'công thức bao hàm – loại trừ', S, 'Use the inclusion–exclusion formula for three sets.', ''),
])
load_vocab()
CAT = ('Sets and Intervals', 'Tập hợp và khoảng')

# kiểm tra số học của các đáp án
assert 14+9-4 == 19 and 24-6 == 18 and 18+17-30 == 5 and 60-48 == 12
assert 20+15-7 == 28 and 20-7 == 13 and 15-7 == 8
assert (50-10) == 40 and 30+25-40 == 15 and 30-15 == 15 and 25-15 == 10 and 15+15+10 == 40
assert 28+22-(45-8) == 13 and 28-13 == 15 and 22-13 == 9 and 15+13+9 == 37
assert 12+10+8-5-3-2+1 == 21 and 10+8+6-3-2-1+1 == 19
assert 60-(35+28-10) == 7 and 25+19-38 == 6 and 20+22-36 == 6

goals = [
 (r'read a Venn diagram of two sets and name its four regions;', r'đọc [[biểu đồ Venn]] của hai tập hợp và gọi tên bốn [[vùng]];'),
 (r'use \(n(A\cup B)=n(A)+n(B)-n(A\cap B)\);', r'dùng công thức \(n(A\cup B)=n(A)+n(B)-n(A\cap B)\);'),
 (r'find “only”, “both”, “at least one” and “neither” counts;', r'tìm số phần tử “chỉ”, “cả hai”, “ít nhất một” và “không … nào”;'),
 (r'solve word problems with a Venn diagram;', r'giải bài toán có lời văn bằng biểu đồ Venn;'),
 (r'(extension) count with three sets.', r'(mở rộng) đếm với ba tập hợp.')]

vocab = [
 (r'<b>Venn diagram</b> – a picture that uses circles to show sets. “Draw a Venn diagram of the two sets.”', r'[[Biểu đồ Venn]] – hình dùng các đường tròn để biểu diễn tập hợp. “Draw a Venn diagram of the two sets.”'),
 (r'<b>region</b> – a part of a Venn diagram. “Write a number in each region.”', r'[[Vùng]] – một phần của biểu đồ Venn. “Write a number in each region.”'),
 (r'<b>number of elements</b> – how many elements a set has. We write \(n(A)\).', r'[[Số phần tử]] – tập hợp có bao nhiêu phần tử. Ta viết \(n(A)\).'),
 (r'<b>union</b> – elements in \(A\), in \(B\), or in both: \(A\cup B\).', r'[[Hợp]] – phần tử thuộc \(A\), thuộc \(B\), hoặc thuộc cả hai: \(A\cup B\).'),
 (r'<b>intersection</b> – elements in both \(A\) and \(B\): \(A\cap B\).', r'[[Giao]] – phần tử thuộc cả \(A\) và \(B\): \(A\cap B\).'),
 (r'<b>difference</b> – elements in \(A\) but not in \(B\): \(A\setminus B\).', r'[[Hiệu]] – phần tử thuộc \(A\) nhưng không thuộc \(B\): \(A\setminus B\).'),
 (r'<b>disjoint sets</b> – two sets with no common element: \(A\cap B=\varnothing\).', r'[[Hai tập rời nhau]] – hai tập không có phần tử chung: \(A\cap B=\varnothing\).')]

phrases = [
 (r'“at least one” – in the union. “Find how many students play at least one sport.”', r'“at least one” – thuộc [[hợp]]. “Find how many students play at least one sport.”'),
 (r'“both” – in the intersection. “Find how many students like both subjects.”', r'“both” – thuộc [[giao]]. “Find how many students like both subjects.”'),
 (r'“only A” – in \(A\) but not in \(B\), so use \(n(A)-n(A\cap B)\).', r'“only A” – thuộc \(A\) nhưng không thuộc \(B\), dùng \(n(A)-n(A\cap B)\).'),
 (r'“neither” – outside both circles: total minus \(n(A\cup B)\).', r'“neither” – nằm ngoài cả hai đường tròn: tổng trừ \(n(A\cup B)\).'),
 (r'“Draw a Venn diagram and fill in the numbers.” – Vẽ biểu đồ Venn và điền số vào các vùng.', r'“Draw a Venn diagram and fill in the numbers.” – Vẽ [[biểu đồ Venn]] và điền số vào các vùng.')]

review = (T(r'Let \(A=\{1,2,3\}\) and \(B=\{2,3,4,5\}\). Then \(A\cap B=\{2,3\}\) and \(A\cup B=\{1,2,3,4,5\}\).', r'Cho \(A=\{1,2,3\}\) và \(B=\{2,3,4,5\}\). Khi đó \(A\cap B=\{2,3\}\) và \(A\cup B=\{1,2,3,4,5\}\).') +
 T(r'The <b>number of elements</b> are \(n(A)=3\), \(n(B)=4\), \(n(A\cap B)=2\), \(n(A\cup B)=5\). Notice that \(5=3+4-2\). This is the idea of the whole lesson.', r'[[Số phần tử]]: \(n(A)=3\), \(n(B)=4\), \(n(A\cap B)=2\), \(n(A\cup B)=5\). Chú ý \(5=3+4-2\). Đây là ý tưởng của cả bài học.'))

reg_tab = TBL([TI('English phrase', 'Cụm từ tiếng Anh'), TI('Region', 'Vùng'), TI('Count', 'Cách đếm')], [
 [TI('at least one', 'ít nhất một'), r'\(A\cup B\)', r'\(n(A)+n(B)-n(A\cap B)\)'],
 [TI('both', 'cả hai'), r'\(A\cap B\)', r'\(n(A\cap B)\)'],
 [TI('only A', 'chỉ A'), r'\(A\setminus B\)', r'\(n(A)-n(A\cap B)\)'],
 [TI('only B', 'chỉ B'), r'\(B\setminus A\)', r'\(n(B)-n(A\cap B)\)'],
 [TI('neither', 'không … nào'), TI('outside both circles', 'ngoài cả hai đường tròn'), TI('total \\(-\\,n(A\\cup B)\\)', 'tổng \\(-\\,n(A\\cup B)\\)')]])

theory = ('<h3>5.1 %s</h3>' % TI('A Venn diagram with two sets', 'Biểu đồ Venn của hai tập hợp') +
 T(r'A <b>Venn diagram</b> uses two circles. They make four <b>regions</b>: \(A\) only, both, \(B\) only, and neither (outside the circles).', r'[[Biểu đồ Venn]] dùng hai đường tròn. Chúng tạo ra bốn [[vùng]]: chỉ \(A\), cả hai, chỉ \(B\), và không thuộc tập nào (ngoài hai đường tròn).') +
 FIGR(venn2('A∖B', 'A∩B', 'B∖A', 'neither', alt='Venn diagram with four regions'), 'The four regions of a Venn diagram.', 'Bốn vùng của biểu đồ Venn.') +
 '<h3>5.2 %s</h3>' % TI('Counting formulas', 'Các công thức đếm') +
 BOX('mint', ('Formulas', 'Công thức'),
   M(r'n(A\cup B)=n(A)+n(B)-n(A\cap B)'), M(r'n(A\setminus B)=n(A)-n(A\cap B)\qquad n(B\setminus A)=n(B)-n(A\cap B)'),
   T(r'If \(E\) is the whole group, then the number of elements in neither set is \(n(E)-n(A\cup B)\).', r'Nếu \(E\) là cả nhóm, số phần tử không thuộc tập nào là \(n(E)-n(A\cup B)\).'),
   T(r'If \(A\) and \(B\) are <b>disjoint sets</b>, then \(n(A\cup B)=n(A)+n(B)\).', r'Nếu \(A\) và \(B\) là [[hai tập rời nhau]] thì \(n(A\cup B)=n(A)+n(B)\).')) +
 T(r'Why do we subtract \(n(A\cap B)\)? Elements in both sets are counted once in \(n(A)\) and once in \(n(B)\). We keep only one of the two counts.', r'Vì sao phải trừ \(n(A\cap B)\)? Phần tử thuộc cả hai tập bị đếm một lần trong \(n(A)\) và một lần nữa trong \(n(B)\). Ta chỉ giữ một trong hai lần đếm.') +
 '<h3>5.3 %s</h3>' % TI('Words and regions', 'Từ ngữ và vùng tương ứng') + reg_tab +
 '<h3>5.4 %s</h3>' % TI('Method for word problems', 'Cách giải bài toán có lời văn') +
 OL([T(r'Name the sets (for example \(F\) and \(V\)) and write the given numbers.', r'Đặt tên cho các tập (ví dụ \(F\) và \(V\)) và ghi các số đã cho.'),
     T(r'Draw two circles inside a rectangle for the whole group.', r'Vẽ hai đường tròn trong một hình chữ nhật biểu diễn cả nhóm.'),
     T(r'Fill the middle region (both) first, then the “only” regions, then the outside.', r'Điền vùng giữa (cả hai) trước, rồi các vùng “chỉ”, rồi vùng ngoài.'),
     T(r'Check: all regions must add up to the total.', r'Kiểm tra: tổng các vùng phải bằng tổng số.')]) +
 '<h3>5.5 %s</h3>' % TI('Extension: three sets', 'Mở rộng: ba tập hợp') +
 BOX('lavender', ('Extension', 'Mở rộng'), T(r'For three sets the <b>inclusion–exclusion formula</b> is', r'Với ba tập hợp, [[công thức bao hàm – loại trừ]] là'),
   M(r'n(A\cup B\cup C)=n(A)+n(B)+n(C)-n(A\cap B)-n(A\cap C)-n(B\cap C)+n(A\cap B\cap C)'),
   T(r'We subtract the pairs, but this removes the triple intersection too many times, so we add it back once.', r'Ta trừ các cặp, nhưng như vậy phần giao của cả ba tập bị trừ quá nhiều lần, nên phải cộng lại một lần.')))

ex = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Two sets', 'Hai tập hợp'),
  T(r'Let \(n(A)=20\), \(n(B)=15\) and \(n(A\cap B)=7\). Find \(n(A\cup B)\), \(n(A\setminus B)\) and \(n(B\setminus A)\).', r'Cho \(n(A)=20\), \(n(B)=15\), \(n(A\cap B)=7\). Tìm \(n(A\cup B)\), \(n(A\setminus B)\) và \(n(B\setminus A)\).'),
  (r'We know the middle region (7) and the totals of the two circles. Subtract the middle from each total.', r'Ta biết vùng giữa (7) và tổng của hai đường tròn. Lấy mỗi tổng trừ vùng giữa.'),
  [T(r'\(n(A\cup B)=20+15-7=28\).', r'\(n(A\cup B)=20+15-7=28\).'),
   T(r'\(n(A\setminus B)=20-7=13\) and \(n(B\setminus A)=15-7=8\).', r'\(n(A\setminus B)=20-7=13\) và \(n(B\setminus A)=15-7=8\).'),
   T(r'Check: \(13+7+8=28\).', r'Kiểm tra: \(13+7+8=28\).') +
   FIGR(venn2(13, 7, 8, alt='Venn diagram: 13, 7 and 8'), 'Venn diagram for Example 1.', 'Biểu đồ Venn cho Ví dụ 1.')],
  r'\(28\); \(13\); \(8\)')
ex += EXAMPLE(2, ('Intermediate', 'Trung bình'), ('A survey with “neither”', 'Khảo sát có “không … nào”'),
  T(r'In a group of 50 students, 30 like pop music, 25 like rock music and 10 like neither. How many like both? How many like pop only?', r'Trong nhóm 50 học sinh, 30 em thích nhạc pop, 25 em thích nhạc rock và 10 em không thích loại nào. Có bao nhiêu em thích cả hai? Bao nhiêu em chỉ thích pop?'),
  (r'First find the students who like at least one kind of music. Then use the formula backwards to find “both”.', r'Trước hết tìm số em thích ít nhất một loại nhạc. Rồi dùng công thức theo chiều ngược lại để tìm “cả hai”.'),
  [T(r'At least one: \(50-10=40\), so \(n(P\cup R)=40\).', r'Ít nhất một loại: \(50-10=40\), nên \(n(P\cup R)=40\).'),
   T(r'\(40=30+25-n(P\cap R)\), so \(n(P\cap R)=55-40=15\).', r'\(40=30+25-n(P\cap R)\) nên \(n(P\cap R)=55-40=15\).'),
   T(r'Pop only: \(30-15=15\). Rock only: \(25-15=10\). Check: \(15+15+10=40\).', r'Chỉ pop: \(30-15=15\). Chỉ rock: \(25-15=10\). Kiểm tra: \(15+15+10=40\).') +
   FIGR(venn2(15, 15, 10, outside=10, la='P', lb='R', alt='Venn diagram: 15, 15, 10 and 10 outside'), 'Venn diagram for Example 2 (10 outside).', 'Biểu đồ Venn cho Ví dụ 2 (10 em ở ngoài).')],
  r'both: \(15\); pop only: \(15\)')
ex += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('Finding “both” from “neither”', 'Tìm “cả hai” từ “không … nào”'),
  T(r'In a class of 45 students, 28 study French, 22 study German and 8 study neither language. How many study both? How many study French only?', r'Lớp có 45 học sinh: 28 em học tiếng Pháp, 22 em học tiếng Đức và 8 em không học thứ tiếng nào. Có bao nhiêu em học cả hai? Bao nhiêu em chỉ học tiếng Pháp?'),
  (r'The students who study at least one language are the whole class minus the “neither” group.', r'Số em học ít nhất một thứ tiếng bằng cả lớp trừ nhóm “không … nào”.'),
  [T(r'\(n(F\cup G)=45-8=37\).', r'\(n(F\cup G)=45-8=37\).'),
   T(r'\(n(F\cap G)=28+22-37=13\).', r'\(n(F\cap G)=28+22-37=13\).'),
   T(r'French only: \(28-13=15\). German only: \(22-13=9\). Check: \(15+13+9+8=45\).', r'Chỉ tiếng Pháp: \(28-13=15\). Chỉ tiếng Đức: \(22-13=9\). Kiểm tra: \(15+13+9+8=45\).')],
  r'both: \(13\); French only: \(15\)')
ex += EXAMPLE(4, ('Extension', 'Mở rộng'), ('Three sets', 'Ba tập hợp'),
  T(r'Let \(n(A)=12\), \(n(B)=10\), \(n(C)=8\), \(n(A\cap B)=5\), \(n(A\cap C)=3\), \(n(B\cap C)=2\) and \(n(A\cap B\cap C)=1\). Find \(n(A\cup B\cup C)\).', r'Cho \(n(A)=12\), \(n(B)=10\), \(n(C)=8\), \(n(A\cap B)=5\), \(n(A\cap C)=3\), \(n(B\cap C)=2\) và \(n(A\cap B\cap C)=1\). Tìm \(n(A\cup B\cup C)\).'),
  (r'Use the inclusion–exclusion formula for three sets: add the singles, subtract the pairs, add the triple.', r'Dùng [[công thức bao hàm – loại trừ]] cho ba tập: cộng các tập đơn, trừ các cặp, cộng lại phần giao của cả ba.'),
  [T(r'Add the singles: \(12+10+8=30\).', r'Cộng các tập đơn: \(12+10+8=30\).'),
   T(r'Subtract the pairs: \(30-(5+3+2)=20\).', r'Trừ các cặp: \(30-(5+3+2)=20\).'),
   T(r'Add the triple: \(20+1=21\).', r'Cộng phần giao của cả ba: \(20+1=21\).')],
  r'\(21\)')

_PR1 = [
 (('A. Multiple Choice', 'A. Trắc nghiệm nhiều lựa chọn'), [
  MCQ(1, (r'If \(n(A)=14\), \(n(B)=9\) and \(n(A\cap B)=4\), what is \(n(A\cup B)\)?', r'Nếu \(n(A)=14\), \(n(B)=9\), \(n(A\cap B)=4\) thì \(n(A\cup B)\) bằng bao nhiêu?'), [r'23', r'19', r'27', r'10'], 'b',
      (r'Answer: b. \(14+9-4=19\).', r'Đáp án b. \(14+9-4=19\).')),
  MCQ(2, (r'In a group of 40 students, 24 play chess, 18 draw and 6 do both. How many play chess only?', r'Trong nhóm 40 học sinh, 24 em chơi cờ, 18 em vẽ và 6 em làm cả hai. Có bao nhiêu em chỉ chơi cờ?'), [r'6', r'12', r'18', r'24'], 'c',
      (r'Answer: c. Chess only = \(24-6=18\).', r'Đáp án c. Chỉ chơi cờ = \(24-6=18\).')),
  MCQ(3, (r'If \(n(A\cup B)=30\), \(n(A)=18\) and \(n(B)=17\), what is \(n(A\cap B)\)?', r'Nếu \(n(A\cup B)=30\), \(n(A)=18\), \(n(B)=17\) thì \(n(A\cap B)\) bằng bao nhiêu?'), [r'5', r'12', r'13', r'35'], 'a',
      (r'Answer: a. \(n(A\cap B)=18+17-30=5\).', r'Đáp án a. \(n(A\cap B)=18+17-30=5\).')),
  MCQ(4, (r'Which expression gives the number of elements in \(B\) only?', r'Biểu thức nào cho số phần tử chỉ thuộc \(B\)?'), [r'n(B)-n(A)', r'n(B)-n(A\cap B)', r'n(A\cup B)-n(B)', r'n(A\cap B)-n(B)'], 'b',
      (r'Answer: b. Remove the common part from \(n(B)\).', r'Đáp án b. Bỏ phần chung khỏi \(n(B)\).')),
  MCQ(5, (r'In a group of 60, \(n(A\cup B)=48\). How many are in neither set?', r'Trong nhóm 60 người, \(n(A\cup B)=48\). Có bao nhiêu người không thuộc tập nào?'), [r'12', r'48', r'108', r'18'], 'a',
      (r'Answer: a. \(60-48=12\).', r'Đáp án a. \(60-48=12\).'))]),
 (('B. True or False', 'B. Đúng hoặc sai'), [
  TF(6, (r'True or false: \(n(A\cup B)=n(A)+n(B)\) is always true.', r'Đúng hay sai: \(n(A\cup B)=n(A)+n(B)\) luôn đúng.'), 'false', (r'False. It is true only when \(A\) and \(B\) have no common element.', r'Sai. Công thức chỉ đúng khi \(A\) và \(B\) không có phần tử chung.')),
  TF(7, (r'True or false: if \(A\cap B=\varnothing\), then \(n(A\cup B)=n(A)+n(B)\).', r'Đúng hay sai: nếu \(A\cap B=\varnothing\) thì \(n(A\cup B)=n(A)+n(B)\).'), 'true', (r'True. Then \(n(A\cap B)=0\).', r'Đúng. Khi đó \(n(A\cap B)=0\).')),
  TF(8, (r'True or false: \(n(A\cup B)\) can be smaller than \(n(A)\).', r'Đúng hay sai: \(n(A\cup B)\) có thể nhỏ hơn \(n(A)\).'), 'false', (r'False. \(A\subset A\cup B\), so \(A\cup B\) has at least as many elements as \(A\).', r'Sai. \(A\subset A\cup B\) nên \(A\cup B\) có ít nhất nhiều phần tử bằng \(A\).'))]),
 (('C. Short Answer', 'C. Trả lời ngắn'), [
  SHORT(9, (r'In a group of 60 students, 35 study French, 28 study German and 10 study both. How many study neither language?', r'Trong nhóm 60 học sinh, 35 em học tiếng Pháp, 28 em học tiếng Đức và 10 em học cả hai. Có bao nhiêu em không học thứ tiếng nào?'), '7', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'),
        (r'Answer: 7. \(35+28-10=53\) study at least one language, so \(60-53=7\).', r'Đáp số: 7. \(35+28-10=53\) em học ít nhất một thứ tiếng nên \(60-53=7\).')),
  SHORT(10, (r'If \(n(A)=25\), \(n(B)=19\) and \(n(A\cup B)=38\), find \(n(A\cap B)\).', r'Nếu \(n(A)=25\), \(n(B)=19\), \(n(A\cup B)=38\), tìm \(n(A\cap B)\).'), '6', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'),
        (r'Answer: 6. \(25+19-38=6\).', r'Đáp số: 6. \(25+19-38=6\).')),
  SHORT(11, (r'(Extension) Let \(n(A)=10\), \(n(B)=8\), \(n(C)=6\), \(n(A\cap B)=3\), \(n(A\cap C)=2\), \(n(B\cap C)=1\) and \(n(A\cap B\cap C)=1\). Find \(n(A\cup B\cup C)\).', r'(Mở rộng) Cho \(n(A)=10\), \(n(B)=8\), \(n(C)=6\), \(n(A\cap B)=3\), \(n(A\cap C)=2\), \(n(B\cap C)=1\), \(n(A\cap B\cap C)=1\). Tìm \(n(A\cup B\cup C)\).'), '19', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'),
        (r'Answer: 19. \(10+8+6-3-2-1+1=19\).', r'Đáp số: 19. \(10+8+6-3-2-1+1=19\).')),
  SHORT(12, (r'In a class of 36 students, 20 like tea and 22 like coffee. Every student likes at least one drink. How many like both?', r'Lớp có 36 học sinh, 20 em thích trà và 22 em thích cà phê. Mỗi em thích ít nhất một loại. Có bao nhiêu em thích cả hai?'), '6', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'),
        (r'Answer: 6. \(36=20+22-n(T\cap C)\), so \(n(T\cap C)=6\).', r'Đáp số: 6. \(36=20+22-n(T\cap C)\) nên \(n(T\cap C)=6\).'))]),
 (('D. Mathematical English', 'D. Tiếng Anh Toán học'), [
  MCQ(13, (r'“Find the number of students who like tea only” means:', r'“Find the number of students who like tea only” có nghĩa là:'),
      [r'\text{students who like tea but not coffee}', r'\text{students who like both drinks}', r'\text{students who like neither drink}', r'\text{students who like at least one drink}'], 'a',
      (r'Answer: a. “Only” means the difference: tea but not coffee.', r'Đáp án a. “Only” nghĩa là hiệu: thích trà nhưng không thích cà phê.')),
  MCQ(14, (r'In a Venn diagram, “neither” is the region:', r'Trong biểu đồ Venn, “neither” là vùng:'),
      [r'\text{inside circle A only}', r'\text{inside both circles}', r'\text{outside both circles}', r'\text{inside circle B only}'], 'c',
      (r'Answer: c. “Neither” means not in \(A\) and not in \(B\).', r'Đáp án c. “Neither” nghĩa là không thuộc \(A\) và không thuộc \(B\).'))]),
 (('E. Explanation (not scored)', 'E. Giải thích (không tính điểm)'), [
  T(r'In 2–3 simple English sentences, explain why \(n(A\cup B)\) is not always \(n(A)+n(B)\).', r'Viết 2–3 câu tiếng Anh đơn giản giải thích vì sao \(n(A\cup B)\) không phải lúc nào cũng bằng \(n(A)+n(B)\).') +
  REVEAL(T(r'Sample answer: “Some elements are in both sets. When we add n(A) and n(B), we count these elements twice. So we subtract the elements in the intersection once.”', r'Câu trả lời mẫu (giữ bằng tiếng Anh). Hãy kiểm tra: bài của bạn đã nói “phần tử chung bị đếm hai lần” chưa?'))])]

# ----- Bài tập: mỗi mức một bộ riêng, cùng dạng, khác số liệu (LEVEL_PRACTICE) -----
_T = [g[0] for g in _PR1]
S1 = [g[1] for g in _PR1]
S2 = [
 [MCQ(1, (r'If \(n(A)=16\), \(n(B)=11\) and \(n(A\cap B)=5\), what is \(n(A\cup B)\)?', r'Nếu \(n(A)=16\), \(n(B)=11\), \(n(A\cap B)=5\) thì \(n(A\cup B)\) bằng bao nhiêu?'), [r'27', r'32', r'22', r'11'], 'c',
      (r'Answer: c. \(16+11-5=22\).', r'Đáp án c. \(16+11-5=22\).')),
  MCQ(2, (r'In a group of 45 students, 27 play badminton, 20 swim and 8 do both. How many play badminton only?', r'Trong nhóm 45 học sinh, 27 em chơi cầu lông, 20 em bơi và 8 em làm cả hai. Có bao nhiêu em chỉ chơi cầu lông?'), [r'19', r'8', r'12', r'27'], 'a',
      (r'Answer: a. Badminton only = \(27-8=19\).', r'Đáp án a. Chỉ chơi cầu lông = \(27-8=19\).')),
  MCQ(3, (r'If \(n(A\cup B)=34\), \(n(A)=21\) and \(n(B)=19\), what is \(n(A\cap B)\)?', r'Nếu \(n(A\cup B)=34\), \(n(A)=21\), \(n(B)=19\) thì \(n(A\cap B)\) bằng bao nhiêu?'), [r'40', r'15', r'13', r'6'], 'd',
      (r'Answer: d. \(n(A\cap B)=21+19-34=6\).', r'Đáp án d. \(n(A\cap B)=21+19-34=6\).')),
  MCQ(4, (r'Which expression gives the number of elements in \(A\) only?', r'Biểu thức nào cho số phần tử chỉ thuộc \(A\)?'), [r'n(A)-n(B)', r'n(A\cup B)-n(A)', r'n(A)-n(A\cap B)', r'n(A\cap B)-n(A)'], 'c',
      (r'Answer: c. Remove the common part from \(n(A)\).', r'Đáp án c. Bỏ phần chung khỏi \(n(A)\).')),
  MCQ(5, (r'In a group of 80, \(n(A\cup B)=65\). How many are in neither set?', r'Trong nhóm 80 người, \(n(A\cup B)=65\). Có bao nhiêu người không thuộc tập nào?'), [r'145', r'15', r'65', r'25'], 'b',
      (r'Answer: b. \(80-65=15\).', r'Đáp án b. \(80-65=15\).'))],
 [TF(6, (r'True or false: \(n(A\cup B)=n(A)+n(B)-n(A\cap B)\) is always true.', r'Đúng hay sai: \(n(A\cup B)=n(A)+n(B)-n(A\cap B)\) luôn đúng.'), 'true', (r'True. This is the counting formula. It works for any two finite sets.', r'Đúng. Đây là công thức đếm; nó đúng với hai tập hữu hạn bất kì.')),
  TF(7, (r'True or false: if \(A\) and \(B\) have a common element, then \(n(A\cup B)=n(A)+n(B)\).', r'Đúng hay sai: nếu \(A\) và \(B\) có phần tử chung thì \(n(A\cup B)=n(A)+n(B)\).'), 'false', (r'False. The common elements are counted twice, so we must subtract them once.', r'Sai. Các phần tử chung bị đếm hai lần nên phải trừ đi một lần.')),
  TF(8, (r'True or false: \(n(A\cap B)\) can be larger than \(n(A)\).', r'Đúng hay sai: \(n(A\cap B)\) có thể lớn hơn \(n(A)\).'), 'false', (r'False. \(A\cap B\subset A\), so \(A\cap B\) has at most as many elements as \(A\).', r'Sai. \(A\cap B\subset A\) nên \(A\cap B\) có nhiều nhất bằng số phần tử của \(A\).'))],
 [SHORT(9, (r'In a group of 50 students, 30 study Japanese, 24 study Korean and 9 study both. How many study neither language?', r'Trong nhóm 50 học sinh, 30 em học tiếng Nhật, 24 em học tiếng Hàn và 9 em học cả hai. Có bao nhiêu em không học thứ tiếng nào?'), '5', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'),
        (r'Answer: 5. \(30+24-9=45\) study at least one language, so \(50-45=5\).', r'Đáp số: 5. \(30+24-9=45\) em học ít nhất một thứ tiếng nên \(50-45=5\).')),
  SHORT(10, (r'If \(n(A)=30\), \(n(B)=22\) and \(n(A\cup B)=44\), find \(n(A\cap B)\).', r'Nếu \(n(A)=30\), \(n(B)=22\), \(n(A\cup B)=44\), tìm \(n(A\cap B)\).'), '8', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'),
        (r'Answer: 8. \(30+22-44=8\).', r'Đáp số: 8. \(30+22-44=8\).')),
  SHORT(11, (r'(Extension) Let \(n(A)=12\), \(n(B)=9\), \(n(C)=7\), \(n(A\cap B)=4\), \(n(A\cap C)=3\), \(n(B\cap C)=2\) and \(n(A\cap B\cap C)=1\). Find \(n(A\cup B\cup C)\).', r'(Mở rộng) Cho \(n(A)=12\), \(n(B)=9\), \(n(C)=7\), \(n(A\cap B)=4\), \(n(A\cap C)=3\), \(n(B\cap C)=2\), \(n(A\cap B\cap C)=1\). Tìm \(n(A\cup B\cup C)\).'), '20', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'),
        (r'Answer: 20. \(12+9+7-4-3-2+1=20\).', r'Đáp số: 20. \(12+9+7-4-3-2+1=20\).')),
  SHORT(12, (r'In a class of 42 students, 25 like pizza and 28 like noodles. Every student likes at least one food. How many like both?', r'Lớp có 42 học sinh, 25 em thích pizza và 28 em thích mì. Mỗi em thích ít nhất một món. Có bao nhiêu em thích cả hai món?'), '11', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'),
        (r'Answer: 11. \(42=25+28-n(P\cap N)\), so \(n(P\cap N)=11\).', r'Đáp số: 11. \(42=25+28-n(P\cap N)\) nên \(n(P\cap N)=11\).'))],
 [MCQ(13, (r'“Find the number of students who play badminton only” means:', r'“Find the number of students who play badminton only” có nghĩa là:'),
      [r'\text{students who play both sports}', r'\text{students who play badminton but not swimming}', r'\text{students who play neither sport}', r'\text{students who play at least one sport}'], 'b',
      (r'Answer: b. “Only” means the difference: badminton but not swimming.', r'Đáp án b. “Only” nghĩa là hiệu: chơi cầu lông nhưng không bơi.')),
  MCQ(14, (r'In a Venn diagram, “both” is the region:', r'Trong biểu đồ Venn, “both” là vùng:'),
      [r'\text{outside both circles}', r'\text{inside circle A only}', r'\text{inside both circles}', r'\text{inside circle B only}'], 'c',
      (r'Answer: c. “Both” means in \(A\) and in \(B\): the overlap of the two circles.', r'Đáp án c. “Both” nghĩa là thuộc \(A\) và thuộc \(B\): phần chung của hai hình tròn.'))],
 [T(r'In 2–3 simple English sentences, explain why we subtract \(n(A\cap B)\) in the formula \(n(A\cup B)=n(A)+n(B)-n(A\cap B)\).', r'Viết 2–3 câu tiếng Anh đơn giản giải thích vì sao trong công thức \(n(A\cup B)=n(A)+n(B)-n(A\cap B)\) phải trừ \(n(A\cap B)\).') +
  REVEAL(T(r'Sample answer: “The elements in the intersection are in both sets. When we add n(A) and n(B), we count them two times. We subtract them one time, so every element is counted once.”', r'Câu trả lời mẫu (giữ bằng tiếng Anh). Hãy kiểm tra: bài của bạn đã nói “phần tử chung bị đếm hai lần, nên trừ một lần” chưa?'))]]
S3 = [
 [MCQ(1, (r'If \(n(A)=18\), \(n(B)=13\) and \(n(A\cap B)=6\), what is \(n(A\cup B)\)?', r'Nếu \(n(A)=18\), \(n(B)=13\), \(n(A\cap B)=6\) thì \(n(A\cup B)\) bằng bao nhiêu?'), [r'37', r'31', r'19', r'25'], 'd',
      (r'Answer: d. \(18+13-6=25\).', r'Đáp án d. \(18+13-6=25\).')),
  MCQ(2, (r'In a group of 50 students, 28 read comics, 19 play chess and 7 do both. How many read comics only?', r'Trong nhóm 50 học sinh, 28 em đọc truyện tranh, 19 em chơi cờ và 7 em làm cả hai. Có bao nhiêu em chỉ đọc truyện tranh?'), [r'7', r'28', r'12', r'21'], 'd',
      (r'Answer: d. Comics only = \(28-7=21\).', r'Đáp án d. Chỉ đọc truyện tranh = \(28-7=21\).')),
  MCQ(3, (r'If \(n(A\cup B)=40\), \(n(A)=26\) and \(n(B)=24\), what is \(n(A\cap B)\)?', r'Nếu \(n(A\cup B)=40\), \(n(A)=26\), \(n(B)=24\) thì \(n(A\cap B)\) bằng bao nhiêu?'), [r'50', r'10', r'14', r'16'], 'b',
      (r'Answer: b. \(n(A\cap B)=26+24-40=10\).', r'Đáp án b. \(n(A\cap B)=26+24-40=10\).')),
  MCQ(4, (r'In a group of \(N\) people, which expression gives the number of people in neither set?', r'Trong nhóm \(N\) người, biểu thức nào cho số người không thuộc tập nào?'), [r'N-n(A\cup B)', r'N-n(A)-n(B)', r'n(A\cup B)-N', r'N+n(A\cup B)'], 'a',
      (r'Answer: a. Take away everyone who is in at least one set. (b) is wrong because it removes the common part twice.', r'Đáp án a. Bỏ đi tất cả những người thuộc ít nhất một tập. Câu b sai vì trừ phần chung hai lần.')),
  MCQ(5, (r'In a group of 90, \(n(A\cup B)=71\). How many are in neither set?', r'Trong nhóm 90 người, \(n(A\cup B)=71\). Có bao nhiêu người không thuộc tập nào?'), [r'161', r'71', r'19', r'29'], 'c',
      (r'Answer: c. \(90-71=19\).', r'Đáp án c. \(90-71=19\).'))],
 [TF(6, (r'True or false: \(n(A\cap B)\le n(A)\) is always true.', r'Đúng hay sai: \(n(A\cap B)\le n(A)\) luôn đúng.'), 'true', (r'True. \(A\cap B\subset A\), so \(A\cap B\) cannot have more elements than \(A\).', r'Đúng. \(A\cap B\subset A\) nên \(A\cap B\) không thể có nhiều phần tử hơn \(A\).')),
  TF(7, (r'True or false: if \(n(A)=n(B)\), then \(A=B\).', r'Đúng hay sai: nếu \(n(A)=n(B)\) thì \(A=B\).'), 'false', (r'False. Two sets can have the same number of elements but different elements: \(\{1,2\}\) and \(\{3,4\}\).', r'Sai. Hai tập có thể có cùng số phần tử nhưng khác phần tử: \(\{1,2\}\) và \(\{3,4\}\).')),
  TF(8, (r'True or false: \(n(A\cup B)\) can be equal to \(n(A)\).', r'Đúng hay sai: \(n(A\cup B)\) có thể bằng \(n(A)\).'), 'true', (r'True. This happens when \(B\subset A\). Example: \(A=\{1,2,3\}\), \(B=\{2\}\), so \(A\cup B=A\).', r'Đúng. Điều này xảy ra khi \(B\subset A\). Ví dụ \(A=\{1,2,3\}\), \(B=\{2\}\) thì \(A\cup B=A\).'))],
 [SHORT(9, (r'In a group of 70 students, 40 study English, 32 study Chinese and 12 study both. How many study neither language?', r'Trong nhóm 70 học sinh, 40 em học tiếng Anh, 32 em học tiếng Trung và 12 em học cả hai. Có bao nhiêu em không học thứ tiếng nào?'), '10', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'),
        (r'Answer: 10. \(40+32-12=60\) study at least one language, so \(70-60=10\).', r'Đáp số: 10. \(40+32-12=60\) em học ít nhất một thứ tiếng nên \(70-60=10\).')),
  SHORT(10, (r'If \(n(A)=33\), \(n(B)=27\) and \(n(A\cup B)=51\), find \(n(A\cap B)\).', r'Nếu \(n(A)=33\), \(n(B)=27\), \(n(A\cup B)=51\), tìm \(n(A\cap B)\).'), '9', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'),
        (r'Answer: 9. \(33+27-51=9\).', r'Đáp số: 9. \(33+27-51=9\).')),
  SHORT(11, (r'(Extension) Let \(n(A)=15\), \(n(B)=11\), \(n(C)=9\), \(n(A\cap B)=5\), \(n(A\cap C)=4\), \(n(B\cap C)=3\) and \(n(A\cap B\cap C)=2\). Find \(n(A\cup B\cup C)\).', r'(Mở rộng) Cho \(n(A)=15\), \(n(B)=11\), \(n(C)=9\), \(n(A\cap B)=5\), \(n(A\cap C)=4\), \(n(B\cap C)=3\), \(n(A\cap B\cap C)=2\). Tìm \(n(A\cup B\cup C)\).'), '25', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'),
        (r'Answer: 25. \(15+11+9-5-4-3+2=25\).', r'Đáp số: 25. \(15+11+9-5-4-3+2=25\).')),
  SHORT(12, (r'In a class of 48 students, 30 like cats and 26 like dogs. Every student likes at least one animal. How many like both?', r'Lớp có 48 học sinh, 30 em thích mèo và 26 em thích chó. Mỗi em thích ít nhất một con vật. Có bao nhiêu em thích cả hai?'), '8', 'number', ('Enter a whole number.', 'Nhập một số nguyên.'),
        (r'Answer: 8. \(48=30+26-n(C\cap D)\), so \(n(C\cap D)=8\).', r'Đáp số: 8. \(48=30+26-n(C\cap D)\) nên \(n(C\cap D)=8\).'))],
 [MCQ(13, (r'“Find the number of students who like cats only” means:', r'“Find the number of students who like cats only” có nghĩa là:'),
      [r'\text{students who like both animals}', r'\text{students who like dogs but not cats}', r'\text{students who like cats but not dogs}', r'\text{students who like neither animal}'], 'c',
      (r'Answer: c. “Only” means the difference: cats but not dogs.', r'Đáp án c. “Only” nghĩa là hiệu: thích mèo nhưng không thích chó.')),
  MCQ(14, (r'In a Venn diagram, “at least one” is the region:', r'Trong biểu đồ Venn, “at least one” là vùng:'),
      [r'\text{outside both circles}', r'\text{inside at least one circle}', r'\text{the overlap only}', r'\text{inside circle B only}'], 'b',
      (r'Answer: b. “At least one” means in \(A\) or in \(B\) or in both: everything inside the two circles.', r'Đáp án b. “At least one” nghĩa là thuộc \(A\), hoặc thuộc \(B\), hoặc thuộc cả hai: toàn bộ phần bên trong hai hình tròn.'))],
 [T(r'In 2–3 simple English sentences, explain why \(n(A\cup B)=n(A)+n(B)\) is correct when \(A\) and \(B\) have no common element.', r'Viết 2–3 câu tiếng Anh đơn giản giải thích vì sao \(n(A\cup B)=n(A)+n(B)\) đúng khi \(A\) và \(B\) không có phần tử chung.') +
  REVEAL(T(r'Sample answer: “If there is no common element, no element is in both sets. So no element is counted two times. We can just add n(A) and n(B).”', r'Câu trả lời mẫu (giữ bằng tiếng Anh). Hãy kiểm tra: bài của bạn đã nói “không có phần tử nào bị đếm hai lần” chưa?'))]]
pr = LEVEL_PRACTICE(_T, {1: S1, 2: S2, 3: S3})

mistakes = [
 (r'<b>Forgetting to subtract.</b> \(n(A\cup B)=n(A)+n(B)\) counts the common part twice. Use \(n(A\cup B)=n(A)+n(B)-n(A\cap B)\).', r'<b>Quên trừ phần chung.</b> \(n(A\cup B)=n(A)+n(B)\) đếm phần chung hai lần. Phải dùng \(n(A\cup B)=n(A)+n(B)-n(A\cap B)\).'),
 (r'<b>“Only” and “both”.</b> “Chess only” is \(n(A)-n(A\cap B)\), not \(n(A)\).', r'<b>“Only” và “both”.</b> “Chỉ chơi cờ” là \(n(A)-n(A\cap B)\), không phải \(n(A)\).'),
 (r'<b>Forgetting “neither”.</b> The total group is bigger than \(n(A\cup B)\) when some students are in neither set.', r'<b>Quên nhóm “neither”.</b> Cả nhóm lớn hơn \(n(A\cup B)\) khi có em không thuộc tập nào.'),
 (r'<b>No final check.</b> Always check that all regions add up to the total.', r'<b>Không kiểm tra lại.</b> Luôn kiểm tra tổng các vùng bằng tổng số.')]
summary = [
 (r'A Venn diagram with two sets has four regions: \(A\) only, both, \(B\) only, neither.', r'[[Biểu đồ Venn]] hai tập có bốn [[vùng]]: chỉ \(A\), cả hai, chỉ \(B\), không thuộc tập nào.'),
 (r'\(n(A\cup B)=n(A)+n(B)-n(A\cap B)\); \(n(A\setminus B)=n(A)-n(A\cap B)\).', r'\(n(A\cup B)=n(A)+n(B)-n(A\cap B)\); \(n(A\setminus B)=n(A)-n(A\cap B)\).'),
 (r'“At least one” = union; “both” = intersection; “only” = difference; “neither” = outside.', r'“At least one” = [[hợp]]; “both” = [[giao]]; “only” = [[hiệu]]; “neither” = ngoài hai vòng.'),
 (r'Fill the middle first, then the “only” regions, then check the total.', r'Điền vùng giữa trước, rồi các vùng “chỉ”, rồi kiểm tra tổng.')]
checks = [
 (r'I can read a Venn diagram with two sets.', r'Tôi đọc được [[biểu đồ Venn]] của hai tập.'),
 (r'I can use \(n(A\cup B)=n(A)+n(B)-n(A\cap B)\).', r'Tôi dùng được công thức \(n(A\cup B)=n(A)+n(B)-n(A\cap B)\).'),
 (r'I can find “only”, “both” and “neither” counts.', r'Tôi tìm được số phần tử “chỉ”, “cả hai” và “không … nào”.'),
 (r'I can solve a word problem with a Venn diagram.', r'Tôi giải được bài toán có lời văn bằng biểu đồ Venn.'),
 STD_SUMMARY_CHECK_EN()]

build('g10-sets-02', 'Counting with Venn Diagrams', 'Đếm bằng biểu đồ Venn', CAT,
  {'level': ('Intermediate', 'Trung bình'), 'time': ('about 50 minutes', 'khoảng 50 phút'), 'before': ('sets, union, intersection, difference', 'tập hợp, hợp, giao, hiệu')},
  goals, vocab, phrases, review, theory, ex, pr, mistakes, summary, checks,
  'lessons/grade10/sets-and-intervals/counting-with-venn-diagrams.html',
  ENTRY('g10-sets-02', 'Counting with Venn Diagrams', 'Count elements of two sets with Venn diagrams and the formula for the union.', 'Intermediate', 50, ['g10-sets-01'], 'lessons/grade10/sets-and-intervals/counting-with-venn-diagrams.html', ['venn diagram', 'counting', 'union', 'intersection'], grade=10, order=20), grade=10)
