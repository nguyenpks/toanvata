# -*- coding: utf-8 -*-
"""g10-algebra-01: Introduction to Algebra (thay bài kiểm thử kỹ thuật bằng bài đầy đủ theo khung v2)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
from mb_std import *
from mb_extra import *
import _vocab
CAT = ('Algebraic Expressions', 'Biểu thức đại số')

# kiểm tra số học của các đáp án trước khi sinh bài
assert 3*4-2 == 10 and (7-2)+(3-1) == 7 and 2*(-1)**2-3*(-1)+1 == 6 and 2*(-2)**2-3*(-2)+1 == 15
assert (2*2+6)-(2-4) == 12 and 3**2-2*3+3 == 6

goals = [
 (r'read algebraic expressions aloud in English;', r'đọc to các [[biểu thức đại số]] bằng tiếng Anh;'),
 (r'name the parts of an expression: variable, constant, coefficient and term;', r'gọi tên các thành phần: [[biến số]], [[hằng số]], [[hệ số]] và [[hạng tử]];'),
 (r'simplify an expression by combining like terms;', r'[[rút gọn]] biểu thức bằng cách gộp các [[hạng tử đồng dạng|các hạng tử đồng dạng]];'),
 (r'evaluate an expression by substituting numbers;', r'[[tính giá trị]] biểu thức bằng cách [[thay số|thay vào]];'),
 (r'expand brackets with the distributive property;', r'[[khai triển]] dấu ngoặc bằng [[tính chất phân phối]];'),
 (r'translate English phrases into algebraic expressions.', r'chuyển các cụm từ tiếng Anh thành biểu thức đại số.')]

vocab = [
 (r'<b>algebraic expression</b> – numbers, letters and operations written together. “3x + 5 is an algebraic expression.”', r'[[Biểu thức đại số]] – các số, chữ cái và phép toán viết cùng nhau. “3x + 5 là một biểu thức đại số.”'),
 (r'<b>variable</b> – a letter that stands for a number that can change. “The letter x is a variable.”', r'[[Biến số]] – chữ cái đại diện cho một số có thể thay đổi. “Chữ x là một biến số.”'),
 (r'<b>constant</b> – a number that does not change. “In 2x + 5, the number 5 is a constant.”', r'[[Hằng số]] – số không thay đổi. “Trong 2x + 5, số 5 là hằng số.”'),
 (r'<b>term</b> – one part of an expression, separated by + or −. “3x + 5 has two terms.”', r'[[Hạng tử]] – một phần của biểu thức, ngăn cách bởi dấu + hoặc −. “3x + 5 có hai hạng tử.”'),
 (r'<b>coefficient</b> – the number multiplied by the variable. “The coefficient of x in 3x is 3.”', r'[[Hệ số]] – số nhân với biến. “Hệ số của x trong 3x là 3.”'),
 (r'<b>like terms</b> – terms with the same variable part. “3x and 5x are like terms.”', r'[[Hạng tử đồng dạng|các hạng tử đồng dạng]] – các hạng tử có cùng phần biến. “3x và 5x là hạng tử đồng dạng.”'),
 (r'<b>power</b>, <b>base</b>, <b>exponent</b> – in \(2^5\), 2 is the base, 5 is the exponent and \(2^5\) is a power.', r'[[Lũy thừa]], [[cơ số]], [[số mũ]] – trong \(2^5\), 2 là cơ số, 5 là số mũ và \(2^5\) là một lũy thừa.'),
 (r'<b>simplify</b> – make an expression shorter and simpler. “Simplify the expression.”', r'[[Rút gọn]] – viết biểu thức ngắn gọn hơn. “Simplify the expression.”'),
 (r'<b>evaluate</b> – find the value of an expression. “Evaluate the expression when x = 3.”', r'[[Tính giá trị]] của biểu thức. “Evaluate the expression when x = 3.”'),
 (r'<b>substitute</b> – replace a letter by a number. “Substitute x = 2 into the expression.”', r'[[Thay vào]] – thay chữ cái bằng một số. “Substitute x = 2 into the expression.”'),
 (r'<b>expand</b> – remove brackets by multiplying. “Expand the brackets.”', r'[[Khai triển]] – bỏ dấu ngoặc bằng cách nhân. “Expand the brackets.”'),
 (r'<b>distributive property</b> – the rule \(a(b+c)=ab+ac\).', r'[[Tính chất phân phối]] – quy tắc \(a(b+c)=ab+ac\).'),
 (r'<b>order of operations</b> – the order in which we do calculations.', r'[[Thứ tự thực hiện các phép tính]] – thứ tự ta làm các phép tính.')]

phrases = [
 (r'“Simplify the expression.” – Write it in a shorter form.', r'“Simplify the expression.” – [[Rút gọn]] biểu thức.'),
 (r'“Evaluate \(2x+1\) when \(x=3\).” – Substitute 3 for \(x\) and calculate.', r'“Evaluate \(2x+1\) when \(x=3\).” – [[Tính giá trị]] của \(2x+1\) khi \(x=3\).'),
 (r'“Expand the brackets.” – Multiply to remove the brackets.', r'“Expand the brackets.” – [[Khai triển]] để bỏ dấu ngoặc.'),
 (r'How to read: \(3x+5\) is “three x plus five”; \(x^2\) is “x squared”; \(x^3\) is “x cubed”; \(x^n\) is “x to the power of n”.', r'Cách đọc: \(3x+5\) đọc là “three x plus five”; \(x^2\) là “x squared”; \(x^3\) là “x cubed”; \(x^n\) là “x to the power of n”.'),
 (r'“The sum of \(x\) and 5” is \(x+5\). “The product of \(a\) and \(b\)” is \(ab\). “The quotient of \(a\) and \(b\)” is \(\dfrac{a}{b}\).', r'“The sum of \(x\) and 5” là \(x+5\). “The product of \(a\) and \(b\)” là \(ab\). “The quotient of \(a\) and \(b\)” là \(\dfrac{a}{b}\).'),
 (r'“Twice \(y\)” is \(2y\). “5 less than \(x\)” is \(x-5\). “5 more than \(x\)” is \(x+5\).', r'“Twice \(y\)” là \(2y\). “5 less than \(x\)” là \(x-5\). “5 more than \(x\)” là \(x+5\).')]

review = (T(r'In algebra we use the same <b>order of operations</b> as in arithmetic:', r'Trong đại số ta dùng cùng [[thứ tự thực hiện các phép tính]] như trong số học:') +
 OL([T(r'brackets first;', r'dấu ngoặc trước;'), T(r'then powers;', r'rồi lũy thừa;'), T(r'then multiplication and division, from left to right;', r'rồi nhân và chia, từ trái sang phải;'), T(r'then addition and subtraction, from left to right.', r'rồi cộng và trừ, từ trái sang phải.')]) +
 T(r'Example: \(2+3\cdot4=2+12=14\), not \(20\). Signs: a negative times a negative is positive, for example \((-2)\cdot(-3)=6\).', r'Ví dụ: \(2+3\cdot4=2+12=14\), không phải \(20\). Về dấu: âm nhân âm được dương, chẳng hạn \((-2)\cdot(-3)=6\).'))

parts_tab = TBL([TI('Expression', 'Biểu thức'), TI('Terms', 'Các hạng tử'), TI('Coefficients', 'Hệ số'), TI('Constant term', 'Hạng tử tự do')], [
 [r'\(5x+2\)', r'\(5x,\ 2\)', r'\(5\)', r'\(2\)'],
 [r'\(x^2-4x\)', r'\(x^2,\ -4x\)', r'\(1,\ -4\)', TI('none', 'không có')],
 [r'\(4x^2-3x+7\)', r'\(4x^2,\ -3x,\ 7\)', r'\(4,\ -3\)', r'\(7\)']])
words_tab = TBL([TI('English phrase', 'Cụm từ tiếng Anh'), TI('Expression', 'Biểu thức')], [
 [TI('the sum of \\(x\\) and 5', 'tổng của \\(x\\) và 5'), r'\(x+5\)'],
 [TI('5 less than \\(x\\)', '\\(x\\) giảm đi 5'), r'\(x-5\)'],
 [TI('twice a number \\(n\\)', 'gấp đôi một số \\(n\\)'), r'\(2n\)'],
 [TI('the product of 4 and the sum of \\(x\\) and 2', 'tích của 4 và tổng của \\(x\\) và 2'), r'\(4(x+2)\)'],
 [TI('the quotient of \\(a\\) and \\(b\\)', 'thương của \\(a\\) và \\(b\\)'), r'\(\dfrac{a}{b}\)']])

theory = ('<h3>5.1 %s</h3>' % TI('Expressions and their parts', 'Biểu thức và các thành phần') +
 BOX('mint', ('Definition', 'Định nghĩa'), T(r'An <b>algebraic expression</b> is made of numbers, <b>variables</b> (letters) and operation signs. The parts separated by \(+\) or \(-\) are called <b>terms</b>.', r'[[Biểu thức đại số]] gồm các số, [[biến số]] (chữ cái) và các dấu phép toán. Các phần ngăn cách bởi dấu \(+\) hoặc \(-\) gọi là [[hạng tử]].'),
   T(r'In a term such as \(-3x\), the number \(-3\) is the <b>coefficient</b>. A term without a variable, such as \(7\), is a <b>constant</b>.', r'Trong hạng tử \(-3x\), số \(-3\) là [[hệ số]]. Hạng tử không có biến, như \(7\), là [[hằng số]].')) + parts_tab +
 T(r'The <b>degree</b> of an expression is the highest power of the variable. For \(4x^2-3x+7\) the degree is 2.', r'[[Bậc]] của biểu thức là số mũ lớn nhất của biến. Với \(4x^2-3x+7\), bậc là 2.') +
 '<h3>5.2 %s</h3>' % TI('Like terms and simplifying', 'Hạng tử đồng dạng và rút gọn') +
 BOX('mint', ('Rule', 'Quy tắc'), T(r'<b>Like terms</b> have the same variable part, for example \(3x\) and \(5x\). We add or subtract the coefficients: \(3x+5x=8x\). Terms such as \(3x\) and \(3x^2\) are not like terms, so we cannot combine them.', r'[[Hạng tử đồng dạng|các hạng tử đồng dạng]] có cùng phần biến, ví dụ \(3x\) và \(5x\). Ta cộng hoặc trừ các hệ số: \(3x+5x=8x\). Các hạng tử như \(3x\) và \(3x^2\) không đồng dạng nên không gộp được.')) +
 '<h3>5.3 %s</h3>' % TI('Powers', 'Lũy thừa') +
 BOX('mint', ('Rules of powers', 'Quy tắc về lũy thừa'), M(r'x^m\cdot x^n=x^{m+n}\qquad (x^m)^n=x^{mn}\qquad (xy)^n=x^ny^n\qquad x^0=1\ (x\ne0)'),
   T(r'In \(x^n\), \(x\) is the <b>base</b> and \(n\) is the <b>exponent</b>. For example \(x^2\cdot x^3=x^5\) and \((x^3)^2=x^6\).', r'Trong \(x^n\), \(x\) là [[cơ số]] và \(n\) là [[số mũ]]. Ví dụ \(x^2\cdot x^3=x^5\) và \((x^3)^2=x^6\).')) +
 '<h3>5.4 %s</h3>' % TI('Evaluating an expression', 'Tính giá trị của biểu thức') +
 T(r'To <b>evaluate</b> an expression, <b>substitute</b> the number for the letter and follow the order of operations. Put a negative number in brackets: if \(x=-2\), then \(x^2=(-2)^2=4\).', r'Để [[tính giá trị]] biểu thức, hãy [[thay số|thay vào]] vào chữ cái rồi làm theo thứ tự các phép tính. Số âm phải đặt trong ngoặc: nếu \(x=-2\) thì \(x^2=(-2)^2=4\).') +
 '<h3>5.5 %s</h3>' % TI('The distributive property', 'Tính chất phân phối') +
 BOX('mint', ('Rule', 'Quy tắc'), M(r'a(b+c)=ab+ac\qquad a(b-c)=ab-ac'),
   T(r'A minus sign in front of a bracket changes every sign inside: \(-(x-3)=-x+3\).', r'Dấu trừ đứng trước ngoặc làm đổi dấu mọi số hạng trong ngoặc: \(-(x-3)=-x+3\).')) +
 '<h3>5.6 %s</h3>' % TI('From words to expressions', 'Từ lời nói đến biểu thức') + words_tab +
 BOX('yellow', ('Watch out!', 'Lưu ý'), T(r'“5 less than \(x\)” is \(x-5\), not \(5-x\). The word “than” reverses the order.', r'“5 less than \(x\)” là \(x-5\), không phải \(5-x\). Từ “than” đảo thứ tự lại.')))

ex = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Parts of an expression', 'Các thành phần của biểu thức'),
  T(r'For \(4x^2-3x+7\), name the terms, the coefficients, the constant term and the degree.', r'Với \(4x^2-3x+7\), hãy nêu các hạng tử, hệ số, hạng tử tự do và bậc.'),
  (r'Split the expression at each \(+\) or \(-\) sign. The sign belongs to the term after it.', r'Tách biểu thức tại mỗi dấu \(+\) hoặc \(-\). Dấu thuộc về hạng tử đứng sau nó.'),
  [T(r'Terms: \(4x^2\), \(-3x\) and \(7\).', r'Các [[hạng tử]]: \(4x^2\), \(-3x\) và \(7\).'),
   T(r'Coefficients: \(4\) (of \(x^2\)) and \(-3\) (of \(x\)). The constant term is \(7\).', r'[[Hệ số]]: \(4\) (của \(x^2\)) và \(-3\) (của \(x\)). Hạng tử tự do là \(7\).'),
   T(r'The highest power of \(x\) is 2, so the degree is 2.', r'Số mũ lớn nhất của \(x\) là 2 nên bậc là 2.')],
  r'terms \(4x^2,-3x,7\); coefficients \(4,-3\); constant \(7\); degree \(2\)')
ex += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Combining like terms', 'Gộp hạng tử đồng dạng'),
  T(r'Simplify (a) \(3x+5-x+2\) and (b) \(2a^2+3a-a^2+4a\).', r'Rút gọn (a) \(3x+5-x+2\) và (b) \(2a^2+3a-a^2+4a\).'),
  (r'Group the like terms first: terms with \(x\), and constants.', r'Nhóm các [[hạng tử đồng dạng|các hạng tử đồng dạng]] trước: các hạng tử chứa \(x\), và các hằng số.'),
  [T(r'(a) \(3x-x=2x\) and \(5+2=7\). So the result is \(2x+7\).', r'(a) \(3x-x=2x\) và \(5+2=7\). Kết quả: \(2x+7\).'),
   T(r'(b) \(2a^2-a^2=a^2\) and \(3a+4a=7a\). So the result is \(a^2+7a\).', r'(b) \(2a^2-a^2=a^2\) và \(3a+4a=7a\). Kết quả: \(a^2+7a\).'),
   T(r'We do not combine \(a^2\) and \(7a\) because they are not like terms.', r'Không gộp \(a^2\) và \(7a\) vì chúng không đồng dạng.')],
  r'(a) \(2x+7\); (b) \(a^2+7a\)')
ex += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('From words to algebra', 'Từ lời nói đến đại số'),
  T(r'Write an algebraic expression for (a) “five less than three times a number \(x\)” and (b) “the product of 4 and the sum of \(x\) and 2”.', r'Viết biểu thức đại số cho (a) “five less than three times a number \(x\)” và (b) “the product of 4 and the sum of \(x\) and 2”.'),
  (r'Read the phrase in small pieces. “Than” tells us the order: the number after “less than” comes first.', r'Đọc cụm từ theo từng đoạn nhỏ. “Than” cho biết thứ tự: số đứng sau “less than” viết trước.'),
  [T(r'(a) “three times a number \(x\)” is \(3x\). “Five less than” it is \(3x-5\).', r'(a) “three times a number \(x\)” là \(3x\). “Five less than” nó là \(3x-5\).'),
   T(r'(b) “the sum of \(x\) and 2” is \(x+2\). “The product of 4 and” it is \(4(x+2)\), with brackets.', r'(b) “the sum of \(x\) and 2” là \(x+2\). “The product of 4 and” nó là \(4(x+2)\), có dấu ngoặc.')],
  r'(a) \(3x-5\); (b) \(4(x+2)\)')
ex += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Evaluating with a negative number', 'Tính giá trị với số âm'),
  T(r'Evaluate \(2x^2-3x+1\) when \(x=-2\).', r'Tính giá trị của \(2x^2-3x+1\) khi \(x=-2\).'),
  (r'Substitute \(-2\) in brackets. Do the power first, then the multiplications, then add.', r'Thay \(-2\) vào, đặt trong ngoặc. Làm lũy thừa trước, rồi các phép nhân, rồi cộng.'),
  [T(r'\(2(-2)^2-3(-2)+1\).', r'\(2(-2)^2-3(-2)+1\).'),
   T(r'\((-2)^2=4\), so \(2\cdot4=8\). Also \(-3\cdot(-2)=6\).', r'\((-2)^2=4\) nên \(2\cdot4=8\). Còn \(-3\cdot(-2)=6\).'),
   T(r'\(8+6+1=15\).', r'\(8+6+1=15\).')],
  r'\(15\)')
ex += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Expand and simplify', 'Khai triển và rút gọn'),
  T(r'Expand and simplify \(3(x+2)-2(x-1)\).', r'Khai triển và rút gọn \(3(x+2)-2(x-1)\).'),
  (r'Use the distributive property on each bracket. Be careful with the minus sign before the second bracket.', r'Dùng [[tính chất phân phối]] cho từng ngoặc. Cẩn thận với dấu trừ trước ngoặc thứ hai.'),
  [T(r'\(3(x+2)=3x+6\).', r'\(3(x+2)=3x+6\).'),
   T(r'\(-2(x-1)=-2x+2\), because \(-2\cdot(-1)=+2\).', r'\(-2(x-1)=-2x+2\), vì \(-2\cdot(-1)=+2\).'),
   T(r'Combine: \(3x+6-2x+2=x+8\).', r'Gộp lại: \(3x+6-2x+2=x+8\).')],
  r'\(x+8\)')

_PR1 = [
 (('A. Multiple Choice', 'A. Trắc nghiệm nhiều lựa chọn'), [
  MCQ(1, (r'In \(5x^2-7x+2\), what is the coefficient of \(x\)?', r'Trong \(5x^2-7x+2\), hệ số của \(x\) là gì?'), [r'5', r'-7', r'2', r'7'], 'b',
      (r'Answer: b. The term is \(-7x\), so the coefficient is \(-7\). The sign belongs to the coefficient.', r'Đáp án b. Hạng tử là \(-7x\) nên hệ số là \(-7\). Dấu thuộc về hệ số.')),
  MCQ(2, (r'Simplify \(4a+3b-a+2b\).', r'Rút gọn \(4a+3b-a+2b\).'), [r'3a+5b', r'5a+5b', r'3a+b', r'3ab+5'], 'a',
      (r'Answer: a. \(4a-a=3a\) and \(3b+2b=5b\).', r'Đáp án a. \(4a-a=3a\) và \(3b+2b=5b\).')),
  MCQ(3, (r'Evaluate \(x^2-2x+3\) when \(x=3\).', r'Tính giá trị của \(x^2-2x+3\) khi \(x=3\).'), [r'6', r'12', r'0', r'18'], 'a',
      (r'Answer: a. \(3^2-2\cdot3+3=9-6+3=6\).', r'Đáp án a. \(3^2-2\cdot3+3=9-6+3=6\).')),
  MCQ(4, (r'Which expression means “seven less than \(y\)”?', r'Biểu thức nào có nghĩa “seven less than \(y\)”?'), [r'7-y', r'y-7', r'7y', r'y+7'], 'b',
      (r'Answer: b. “Seven less than \(y\)” is \(y-7\).', r'Đáp án b. “Seven less than \(y\)” là \(y-7\).')),
  MCQ(5, (r'Expand \(-2(x-3)\).', r'Khai triển \(-2(x-3)\).'), [r'-2x-6', r'-2x+6', r'2x-6', r'-2x+3'], 'b',
      (r'Answer: b. \(-2\cdot x=-2x\) and \(-2\cdot(-3)=+6\).', r'Đáp án b. \(-2\cdot x=-2x\) và \(-2\cdot(-3)=+6\).'))]),
 (('B. True or False', 'B. Đúng hoặc sai'), [
  TF(6, (r'True or false: \(x^2\cdot x^3=x^6\).', r'Đúng hay sai: \(x^2\cdot x^3=x^6\).'), 'false', (r'False. We add the exponents: \(x^2\cdot x^3=x^5\).', r'Sai. Ta cộng các số mũ: \(x^2\cdot x^3=x^5\).')),
  TF(7, (r'True or false: \(3x\) and \(3x^2\) are like terms.', r'Đúng hay sai: \(3x\) và \(3x^2\) là các hạng tử đồng dạng.'), 'false', (r'False. Their variable parts, \(x\) and \(x^2\), are different.', r'Sai. Phần biến của chúng, \(x\) và \(x^2\), khác nhau.')),
  TF(8, (r'True or false: \((x^3)^2=x^6\).', r'Đúng hay sai: \((x^3)^2=x^6\).'), 'true', (r'True. We multiply the exponents: \(3\cdot2=6\).', r'Đúng. Ta nhân các số mũ: \(3\cdot2=6\).'))]),
 (('C. Short Answer', 'C. Trả lời ngắn'), [
  SHORT(9, (r'Evaluate \(3x-2\) when \(x=4\).', r'Tính giá trị của \(3x-2\) khi \(x=4\).'), '10', 'number', ('Enter a number.', 'Nhập một số.'),
        (r'Answer: 10. \(3\cdot4-2=12-2=10\).', r'Đáp số: 10. \(3\cdot4-2=12-2=10\).')),
  SHORT(10, (r'Simplify \(7x+3-2x-1\). The result is \(ax+b\). Find \(a+b\).', r'Rút gọn \(7x+3-2x-1\). Kết quả có dạng \(ax+b\). Tìm \(a+b\).'), '7', 'number', ('Enter a number.', 'Nhập một số.'),
        (r'Answer: 7. \(7x-2x=5x\) and \(3-1=2\), so the result is \(5x+2\) and \(a+b=5+2=7\).', r'Đáp số: 7. \(7x-2x=5x\) và \(3-1=2\) nên kết quả là \(5x+2\), do đó \(a+b=5+2=7\).')),
  SHORT(11, (r'Evaluate \(2x^2-3x+1\) when \(x=-1\).', r'Tính giá trị của \(2x^2-3x+1\) khi \(x=-1\).'), '6', 'number', ('Enter a number.', 'Nhập một số.'),
        (r'Answer: 6. \(2\cdot1-3\cdot(-1)+1=2+3+1=6\).', r'Đáp số: 6. \(2\cdot1-3\cdot(-1)+1=2+3+1=6\).')),
  SHORT(12, (r'Expand and simplify \(2(x+3)-(x-4)\), then evaluate the result when \(x=2\).', r'Khai triển và rút gọn \(2(x+3)-(x-4)\), rồi tính giá trị của kết quả khi \(x=2\).'), '12', 'number', ('Enter a number.', 'Nhập một số.'),
        (r'Answer: 12. \(2x+6-x+4=x+10\). When \(x=2\), \(x+10=12\).', r'Đáp số: 12. \(2x+6-x+4=x+10\). Khi \(x=2\) thì \(x+10=12\).'))]),
 (('D. Mathematical English', 'D. Tiếng Anh Toán học'), [
  MCQ(13, (r'Which instruction means “Rút gọn biểu thức”?', r'Câu lệnh nào có nghĩa “Rút gọn biểu thức”?'),
      [r'\text{Simplify the expression.}', r'\text{Evaluate the expression.}', r'\text{Expand the brackets.}', r'\text{Solve the equation.}'], 'a',
      (r'Answer: a. Simplify = rút gọn; evaluate = tính giá trị; expand = khai triển; solve = giải.', r'Đáp án a. simplify = rút gọn; evaluate = tính giá trị; expand = khai triển; solve = giải.')),
  MCQ(14, (r'How do we read \(x^3\) in English?', r'Ký hiệu \(x^3\) đọc bằng tiếng Anh như thế nào?'),
      [r'\text{x cubed}', r'\text{x squared}', r'\text{x times three}', r'\text{x plus three}'], 'a',
      (r'Answer: a. \(x^3\) is “x cubed” or “x to the power of three”.', r'Đáp án a. \(x^3\) đọc là “x cubed” hoặc “x to the power of three”.'))]),
 (('E. Explanation (not scored)', 'E. Giải thích (không tính điểm)'), [
  T(r'Write an expression for “the sum of twice a number \(n\) and five”.', r'Viết biểu thức cho “the sum of twice a number \(n\) and five”.') +
  REVEAL(T(r'“Twice a number \(n\)” is \(2n\). “The sum of … and five” gives \(2n+5\).', r'“Twice a number \(n\)” là \(2n\). “The sum of … and five” cho \(2n+5\).')),
  T(r'In 1–2 simple English sentences, explain why we cannot combine \(3x\) and \(3x^2\).', r'Viết 1–2 câu tiếng Anh đơn giản giải thích vì sao không gộp được \(3x\) và \(3x^2\).') +
  REVEAL(T(r'Sample answer: “They are not like terms. The variable parts are different: one has x and the other has x squared.”', r'Câu trả lời mẫu (giữ bằng tiếng Anh). Hãy kiểm tra: bài của bạn đã nói “phần biến khác nhau” chưa?'))])]

# ----- Bài tập: mỗi mức một bộ riêng, cùng dạng, khác số liệu (LEVEL_PRACTICE) -----
_T = [g[0] for g in _PR1]
S1 = [g[1] for g in _PR1]
S2 = [
 [MCQ(1, (r'In \(6x^2+9x-4\), what is the coefficient of \(x\)?', r'Trong \(6x^2+9x-4\), hệ số của \(x\) là gì?'), [r'6', r'-4', r'9', r'-9'], 'c',
      (r'Answer: c. The term is \(9x\), so the coefficient is \(9\).', r'Đáp án c. Hạng tử là \(9x\) nên hệ số là \(9\).')),
  MCQ(2, (r'Simplify \(5m+2n-2m+4n\).', r'Rút gọn \(5m+2n-2m+4n\).'), [r'3m+6n', r'7m+6n', r'3m+2n', r'9mn'], 'a',
      (r'Answer: a. \(5m-2m=3m\) and \(2n+4n=6n\).', r'Đáp án a. \(5m-2m=3m\) và \(2n+4n=6n\).')),
  MCQ(3, (r'Evaluate \(x^2-3x+4\) when \(x=4\).', r'Tính giá trị của \(x^2-3x+4\) khi \(x=4\).'), [r'0', r'8', r'12', r'20'], 'b',
      (r'Answer: b. \(4^2-3\cdot4+4=16-12+4=8\).', r'Đáp án b. \(4^2-3\cdot4+4=16-12+4=8\).')),
  MCQ(4, (r'Which expression means “five more than \(y\)”?', r'Biểu thức nào có nghĩa “five more than \(y\)”?'), [r'5-y', r'y-5', r'5y', r'y+5'], 'd',
      (r'Answer: d. “Five more than \(y\)” is \(y+5\).', r'Đáp án d. “Five more than \(y\)” là \(y+5\).')),
  MCQ(5, (r'Expand \(-3(x-2)\).', r'Khai triển \(-3(x-2)\).'), [r'-3x-6', r'3x-6', r'-3x+6', r'-3x-2'], 'c',
      (r'Answer: c. \(-3\cdot x=-3x\) and \(-3\cdot(-2)=+6\).', r'Đáp án c. \(-3\cdot x=-3x\) và \(-3\cdot(-2)=+6\).'))],
 [TF(6, (r'True or false: \(x^4\cdot x^2=x^8\).', r'Đúng hay sai: \(x^4\cdot x^2=x^8\).'), 'false', (r'False. We add the exponents: \(x^4\cdot x^2=x^6\).', r'Sai. Ta cộng các số mũ: \(x^4\cdot x^2=x^6\).')),
  TF(7, (r'True or false: \(5xy\) and \(2xy\) are like terms.', r'Đúng hay sai: \(5xy\) và \(2xy\) là các hạng tử đồng dạng.'), 'true', (r'True. Their variable parts are the same: \(xy\).', r'Đúng. Phần biến của chúng giống nhau: \(xy\).')),
  TF(8, (r'True or false: \((x^2)^4=x^8\).', r'Đúng hay sai: \((x^2)^4=x^8\).'), 'true', (r'True. We multiply the exponents: \(2\cdot4=8\).', r'Đúng. Ta nhân các số mũ: \(2\cdot4=8\).'))],
 [SHORT(9, (r'Evaluate \(6x-4\) when \(x=3\).', r'Tính giá trị của \(6x-4\) khi \(x=3\).'), '14', 'number', ('Enter a number.', 'Nhập một số.'),
        (r'Answer: 14. \(6\cdot3-4=18-4=14\).', r'Đáp số: 14. \(6\cdot3-4=18-4=14\).')),
  SHORT(10, (r'Simplify \(8x+5-3x-2\). The result is \(ax+b\). Find \(a+b\).', r'Rút gọn \(8x+5-3x-2\). Kết quả có dạng \(ax+b\). Tìm \(a+b\).'), '8', 'number', ('Enter a number.', 'Nhập một số.'),
        (r'Answer: 8. \(8x-3x=5x\) and \(5-2=3\), so the result is \(5x+3\) and \(a+b=5+3=8\).', r'Đáp số: 8. \(8x-3x=5x\) và \(5-2=3\) nên kết quả là \(5x+3\), do đó \(a+b=5+3=8\).')),
  SHORT(11, (r'Evaluate \(3x^2-2x+4\) when \(x=-2\).', r'Tính giá trị của \(3x^2-2x+4\) khi \(x=-2\).'), '20', 'number', ('Enter a number.', 'Nhập một số.'),
        (r'Answer: 20. \(3\cdot4-2\cdot(-2)+4=12+4+4=20\).', r'Đáp số: 20. \(3\cdot4-2\cdot(-2)+4=12+4+4=20\).')),
  SHORT(12, (r'Expand and simplify \(3(x+2)-(x-5)\), then evaluate the result when \(x=3\).', r'Khai triển và rút gọn \(3(x+2)-(x-5)\), rồi tính giá trị của kết quả khi \(x=3\).'), '17', 'number', ('Enter a number.', 'Nhập một số.'),
        (r'Answer: 17. \(3x+6-x+5=2x+11\). When \(x=3\), \(2x+11=17\).', r'Đáp số: 17. \(3x+6-x+5=2x+11\). Khi \(x=3\) thì \(2x+11=17\).'))],
 [MCQ(13, (r'Which instruction means “Khai triển các dấu ngoặc”?', r'Câu lệnh nào có nghĩa “Khai triển các dấu ngoặc”?'),
      [r'\text{Simplify the expression.}', r'\text{Evaluate the expression.}', r'\text{Expand the brackets.}', r'\text{Solve the equation.}'], 'c',
      (r'Answer: c. Expand = khai triển; simplify = rút gọn; evaluate = tính giá trị; solve = giải.', r'Đáp án c. expand = khai triển; simplify = rút gọn; evaluate = tính giá trị; solve = giải.')),
  MCQ(14, (r'How do we read \(x^2\) in English?', r'Ký hiệu \(x^2\) đọc bằng tiếng Anh như thế nào?'),
      [r'\text{x cubed}', r'\text{x squared}', r'\text{x times two}', r'\text{x plus two}'], 'b',
      (r'Answer: b. \(x^2\) is “x squared” or “x to the power of two”.', r'Đáp án b. \(x^2\) đọc là “x squared” hoặc “x to the power of two”.'))],
 [T(r'Write an expression for “the difference of three times a number \(n\) and four”.', r'Viết biểu thức cho “the difference of three times a number \(n\) and four”.') +
  REVEAL(T(r'“Three times a number \(n\)” is \(3n\). “The difference of … and four” gives \(3n-4\).', r'“Three times a number \(n\)” là \(3n\). “The difference of … and four” cho \(3n-4\).')),
  T(r'In 1–2 simple English sentences, explain why we can combine \(5x\) and \(2x\) but not \(5x\) and \(2y\).', r'Viết 1–2 câu tiếng Anh đơn giản giải thích vì sao gộp được \(5x\) và \(2x\) nhưng không gộp được \(5x\) và \(2y\).') +
  REVEAL(T(r'Sample answer: “5x and 2x are like terms because both have x. 5x and 2y are not like terms because the variables are different.”', r'Câu trả lời mẫu (giữ bằng tiếng Anh). Hãy kiểm tra: bài của bạn đã nói “phần biến giống nhau / khác nhau” chưa?'))]]
S3 = [
 [MCQ(1, (r'In \(3x^2-8x+1\), what is the coefficient of \(x\)?', r'Trong \(3x^2-8x+1\), hệ số của \(x\) là gì?'), [r'3', r'8', r'1', r'-8'], 'd',
      (r'Answer: d. The term is \(-8x\), so the coefficient is \(-8\). The sign belongs to the coefficient.', r'Đáp án d. Hạng tử là \(-8x\) nên hệ số là \(-8\). Dấu thuộc về hệ số.')),
  MCQ(2, (r'Simplify \(6p+4q-p-3q\).', r'Rút gọn \(6p+4q-p-3q\).'), [r'5p+7q', r'7p+q', r'5p+q', r'5pq'], 'c',
      (r'Answer: c. \(6p-p=5p\) and \(4q-3q=q\).', r'Đáp án c. \(6p-p=5p\) và \(4q-3q=q\).')),
  MCQ(3, (r'Evaluate \(x^2-4x+5\) when \(x=2\).', r'Tính giá trị của \(x^2-4x+5\) khi \(x=2\).'), [r'1', r'9', r'-1', r'17'], 'a',
      (r'Answer: a. \(2^2-4\cdot2+5=4-8+5=1\).', r'Đáp án a. \(2^2-4\cdot2+5=4-8+5=1\).')),
  MCQ(4, (r'Which expression means “eight more than twice \(y\)”?', r'Biểu thức nào có nghĩa “eight more than twice \(y\)”?'), [r'2y-8', r'8y+2', r'2y+8', r'2(y+8)'], 'c',
      (r'Answer: c. “Twice \(y\)” is \(2y\). “Eight more than” that is \(2y+8\). In (d), the 8 would also be doubled.', r'Đáp án c. “Twice \(y\)” là \(2y\); “eight more than” số đó là \(2y+8\). Ở câu d, số 8 cũng bị nhân đôi.')),
  MCQ(5, (r'Expand \(-5(x-2)\).', r'Khai triển \(-5(x-2)\).'), [r'-5x-10', r'-5x+10', r'5x-10', r'-5x-2'], 'b',
      (r'Answer: b. \(-5\cdot x=-5x\) and \(-5\cdot(-2)=+10\).', r'Đáp án b. \(-5\cdot x=-5x\) và \(-5\cdot(-2)=+10\).'))],
 [TF(6, (r'True or false: \(x^3\cdot x^4=x^{12}\).', r'Đúng hay sai: \(x^3\cdot x^4=x^{12}\).'), 'false', (r'False. We add the exponents: \(x^3\cdot x^4=x^7\).', r'Sai. Ta cộng các số mũ: \(x^3\cdot x^4=x^7\).')),
  TF(7, (r'True or false: \(4a\) and \(4b\) are like terms.', r'Đúng hay sai: \(4a\) và \(4b\) là các hạng tử đồng dạng.'), 'false', (r'False. Their variable parts, \(a\) and \(b\), are different.', r'Sai. Phần biến của chúng, \(a\) và \(b\), khác nhau.')),
  TF(8, (r'True or false: \((x^5)^2=x^{10}\).', r'Đúng hay sai: \((x^5)^2=x^{10}\).'), 'true', (r'True. We multiply the exponents: \(5\cdot2=10\).', r'Đúng. Ta nhân các số mũ: \(5\cdot2=10\).'))],
 [SHORT(9, (r'Evaluate \(5x-8\) when \(x=6\).', r'Tính giá trị của \(5x-8\) khi \(x=6\).'), '22', 'number', ('Enter a number.', 'Nhập một số.'),
        (r'Answer: 22. \(5\cdot6-8=30-8=22\).', r'Đáp số: 22. \(5\cdot6-8=30-8=22\).')),
  SHORT(10, (r'Simplify \(10x+2-4x-5\). The result is \(ax+b\). Find \(a+b\).', r'Rút gọn \(10x+2-4x-5\). Kết quả có dạng \(ax+b\). Tìm \(a+b\).'), '3', 'number', ('Enter a number.', 'Nhập một số.'),
        (r'Answer: 3. \(10x-4x=6x\) and \(2-5=-3\), so the result is \(6x-3\) and \(a+b=6+(-3)=3\).', r'Đáp số: 3. \(10x-4x=6x\) và \(2-5=-3\) nên kết quả là \(6x-3\), do đó \(a+b=6+(-3)=3\).')),
  SHORT(11, (r'Evaluate \(2x^2+x-3\) when \(x=-3\).', r'Tính giá trị của \(2x^2+x-3\) khi \(x=-3\).'), '12', 'number', ('Enter a number.', 'Nhập một số.'),
        (r'Answer: 12. \(2\cdot9+(-3)-3=18-3-3=12\).', r'Đáp số: 12. \(2\cdot9+(-3)-3=18-3-3=12\).')),
  SHORT(12, (r'Expand and simplify \(4(x+1)-(2x-3)\), then evaluate the result when \(x=4\).', r'Khai triển và rút gọn \(4(x+1)-(2x-3)\), rồi tính giá trị của kết quả khi \(x=4\).'), '15', 'number', ('Enter a number.', 'Nhập một số.'),
        (r'Answer: 15. \(4x+4-2x+3=2x+7\). When \(x=4\), \(2x+7=15\).', r'Đáp số: 15. \(4x+4-2x+3=2x+7\). Khi \(x=4\) thì \(2x+7=15\).'))],
 [MCQ(13, (r'Which instruction means “Tính giá trị của biểu thức”?', r'Câu lệnh nào có nghĩa “Tính giá trị của biểu thức”?'),
      [r'\text{Solve the equation.}', r'\text{Expand the brackets.}', r'\text{Simplify the expression.}', r'\text{Evaluate the expression.}'], 'd',
      (r'Answer: d. Evaluate = tính giá trị; solve = giải; expand = khai triển; simplify = rút gọn.', r'Đáp án d. evaluate = tính giá trị; solve = giải; expand = khai triển; simplify = rút gọn.')),
  MCQ(14, (r'How do we read \(x^4\) in English?', r'Ký hiệu \(x^4\) đọc bằng tiếng Anh như thế nào?'),
      [r'\text{x to the power of four}', r'\text{x times four}', r'\text{x plus four}', r'\text{x squared}'], 'a',
      (r'Answer: a. \(x^4\) is “x to the power of four” or “x to the fourth”.', r'Đáp án a. \(x^4\) đọc là “x to the power of four” hoặc “x to the fourth”.'))],
 [T(r'Write an expression for “seven more than the product of a number \(n\) and four”.', r'Viết biểu thức cho “seven more than the product of a number \(n\) and four”.') +
  REVEAL(T(r'“The product of \(n\) and four” is \(4n\). “Seven more than” that is \(4n+7\).', r'“The product of \(n\) and four” là \(4n\). “Seven more than” số đó cho \(4n+7\).')),
  T(r'In 1–2 simple English sentences, explain why \(x^2\cdot x^3=x^5\) and not \(x^6\).', r'Viết 1–2 câu tiếng Anh đơn giản giải thích vì sao \(x^2\cdot x^3=x^5\) chứ không phải \(x^6\).') +
  REVEAL(T(r'Sample answer: “x squared is x times x, and x cubed is x times x times x. Together there are five x. When we multiply powers, we add the exponents.”', r'Câu trả lời mẫu (giữ bằng tiếng Anh). Hãy kiểm tra: bài của bạn đã nói “cộng các số mũ” hoặc “có tất cả năm thừa số x” chưa?'))]]
pr = LEVEL_PRACTICE(_T, {1: S1, 2: S2, 3: S3})

mistakes = [
 (r'<b>Sign errors with brackets.</b> \(-(x-3)=-x+3\), not \(-x-3\). The minus sign changes every sign inside.', r'<b>Sai dấu khi có ngoặc.</b> \(-(x-3)=-x+3\), không phải \(-x-3\). Dấu trừ đổi dấu mọi số hạng trong ngoặc.'),
 (r'<b>Combining unlike terms.</b> \(3x+2x^2\) cannot be written as \(5x^3\).', r'<b>Gộp hạng tử không đồng dạng.</b> \(3x+2x^2\) không thể viết thành \(5x^3\).'),
 (r'<b>Rules of powers.</b> \(x^2\cdot x^3=x^5\), not \(x^6\); \((x^3)^2=x^6\), not \(x^5\).', r'<b>Quy tắc lũy thừa.</b> \(x^2\cdot x^3=x^5\), không phải \(x^6\); \((x^3)^2=x^6\), không phải \(x^5\).'),
 (r'<b>Negative numbers.</b> When \(x=-2\), \(x^2=(-2)^2=4\), not \(-4\). Use brackets.', r'<b>Số âm.</b> Khi \(x=-2\), \(x^2=(-2)^2=4\), không phải \(-4\). Hãy dùng ngoặc.'),
 (r'<b>“Less than”.</b> “5 less than \(x\)” is \(x-5\), not \(5-x\).', r'<b>“Less than”.</b> “5 less than \(x\)” là \(x-5\), không phải \(5-x\).')]
summary = [
 (r'An expression has terms; each term has a coefficient and a variable part; a constant has no variable.', r'Biểu thức có các [[hạng tử]]; mỗi hạng tử có [[hệ số]] và phần biến; [[hằng số]] không có biến.'),
 (r'Combine like terms: add or subtract the coefficients only.', r'Gộp [[hạng tử đồng dạng|các hạng tử đồng dạng]]: chỉ cộng hoặc trừ các hệ số.'),
 (r'\(x^m\cdot x^n=x^{m+n}\), \((x^m)^n=x^{mn}\), \(x^0=1\) for \(x\ne0\).', r'\(x^m\cdot x^n=x^{m+n}\), \((x^m)^n=x^{mn}\), \(x^0=1\) với \(x\ne0\).'),
 (r'\(a(b+c)=ab+ac\); a minus sign before a bracket changes every sign inside.', r'\(a(b+c)=ab+ac\); dấu trừ trước ngoặc đổi dấu mọi số hạng trong ngoặc.'),
 (r'Words to algebra: sum \(+\), product \(\cdot\), quotient \(\div\), “less than” reverses the order.', r'Từ lời sang đại số: sum \(+\), product \(\cdot\), quotient \(\div\); “less than” đảo thứ tự.')]
checks = [
 (r'I can name the terms, coefficients and constant of an expression.', r'Tôi gọi được tên các [[hạng tử]], [[hệ số]] và [[hằng số]] của biểu thức.'),
 (r'I can simplify an expression by combining like terms.', r'Tôi [[rút gọn]] được biểu thức bằng cách gộp hạng tử đồng dạng.'),
 (r'I can evaluate an expression, including with negative numbers.', r'Tôi [[tính giá trị]] được biểu thức, kể cả với số âm.'),
 (r'I can expand brackets with the distributive property.', r'Tôi [[khai triển]] được ngoặc bằng tính chất phân phối.'),
 (r'I can translate simple English phrases into expressions.', r'Tôi chuyển được các cụm từ tiếng Anh đơn giản thành biểu thức.'),
 STD_SUMMARY_CHECK_EN()]

build('g10-algebra-01', 'Introduction to Algebra', 'Làm quen với đại số', CAT,
  {'level': ('Beginner', 'Cơ bản'), 'time': ('about 45 minutes', 'khoảng 45 phút'), 'before': ('arithmetic with negative numbers and fractions (grades 6–8)', 'số học với số âm và phân số (lớp 6–8)')},
  goals, vocab, phrases, review, theory, ex, pr, mistakes, summary, checks,
  'lessons/grade10/algebra/introduction.html',
  ENTRY('g10-algebra-01', 'Introduction to Algebra', 'Read, write and simplify algebraic expressions in English.', 'Beginner', 45, [], 'lessons/grade10/algebra/introduction.html', ['algebra', 'expressions', 'like terms', 'vocabulary'], grade=10, order=30), grade=10)
