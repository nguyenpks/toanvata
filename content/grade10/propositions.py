# -*- coding: utf-8 -*-
"""Nội dung bài g10-logic-01 = Toán 10 KNTT, Chương I, Bài 1: Mệnh đề – CHỈ NỘI DUNG.
Mã ngân hàng câu hỏi: TOAN10-C1-B01. Bài tập: mỗi mức một bộ riêng, cùng dạng, khác số liệu (LEVEL_PRACTICE) + nhóm D trắc nghiệm tự luyện."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
from mb_selfpractice import SELF
from mb_extra import TBL
import sp_g10

LID = 'g10-logic-01'
CAT = 'Propositions and Sets'
TOPIC = (CAT, 'Mệnh đề và tập hợp')
CV = 'Mệnh đề và tập hợp'

ensure_vocab([
 ('g10-proposition', 'proposition', 'mệnh đề', CV, 'A proposition is true or false.', ''),
 ('g10-true-false', 'true / false', 'đúng / sai', CV, 'Is the statement true or false?', ''),
 ('g10-open-statement', 'open statement', 'mệnh đề chứa biến', CV, 'x + 1 = 3 is an open statement.', r'\(P(x)\)'),
 ('g10-negation', 'negation', 'mệnh đề phủ định', CV, 'Write the negation of the statement.', r'\(\overline{P}\)'),
 ('g10-implication', 'implication', 'mệnh đề kéo theo', CV, 'If P, then Q is an implication.', r'\(P\Rightarrow Q\)'),
 ('g10-hypothesis', 'hypothesis', 'giả thiết', CV, 'P is the hypothesis.', ''),
 ('g10-conclusion', 'conclusion', 'kết luận', CV, 'Q is the conclusion.', ''),
 ('g10-converse', 'converse', 'mệnh đề đảo', CV, 'State the converse of the implication.', r'\(Q\Rightarrow P\)'),
 ('g10-equivalence', 'equivalence', 'mệnh đề tương đương', CV, 'P if and only if Q.', r'\(P\Leftrightarrow Q\)'),
 ('g10-universal', 'for all (universal quantifier)', 'với mọi (kí hiệu ∀)', CV, 'For all real numbers x, x squared is not negative.', r'\(\forall\)'),
 ('g10-existential', 'there exists (existential quantifier)', 'tồn tại (kí hiệu ∃)', CV, 'There exists a real number x such that x + 1 = 3.', r'\(\exists\)'),
 ('g10-counterexample', 'counterexample', 'phản ví dụ', CV, 'Give a counterexample.', ''),
 ('g10-necessary-sufficient', 'necessary and sufficient condition', 'điều kiện cần và đủ', CV, 'P is a necessary and sufficient condition for Q.', ''),
])
load_vocab()

# ---- kiểm tra số liệu (duyệt máy) ----
prime = lambda m: m > 1 and all(m % d for d in range(2, int(m ** .5) + 1))
assert prime(7) and not 2 ** 5 == 30 and 2 ** 5 == 32 and not prime(21) and prime(2)
assert 17 % 3 != 0 and math.sqrt(2) > 1.4
assert all((n % 6 != 0) or (n % 3 == 0) for n in range(1, 500)) and (3 % 3 == 0 and 3 % 6 != 0)         # 6|n ⇒ 3|n đúng, đảo sai (n=3)
assert all(x * x >= 0 for x in range(-50, 51)) and not any(x * x == -1 for x in range(-50, 51))
assert not all(x * x > x for x in [i / 2 for i in range(-20, 21)]) and (0.5 ** 2 <= 0.5) and not (0 ** 2 > 0)
smallest = lambda f: next(n for n in range(1, 500) if not prime(f(n)))
assert smallest(lambda n: n * n - n + 11) == 11 and 11 * 11 - 11 + 11 == 121 == 11 ** 2
assert smallest(lambda n: n * n - n + 41) == 41 and smallest(lambda n: n * n - n + 17) == 17
assert all((n * n) % 2 == 1 for n in range(1, 200, 2))
assert sum(1 for x in range(-3, 4) if x * x < 4) == 3 and sum(1 for x in range(-4, 5) if x * x < 9) == 5 and sum(1 for x in range(-5, 6) if x * x < 16) == 7
assert all((n % 3 != 0) or (n % 9 != 0) or True for n in range(100)) and all((n % 9 != 0) or (n % 3 == 0) for n in range(1, 500))
assert not all((n % 3 != 0) or (n % 6 == 0) for n in range(1, 50)) and not all((n % 4 != 0) or (n % 8 == 0) for n in range(1, 50)) and not all((n % 5 != 0) or (n % 10 == 0) for n in range(1, 50))
assert all(((n % 2 == 0) == ((n * n) % 2 == 0)) for n in range(0, 200))

meta = dict(level=('Beginner', 'Cơ bản'), time=('about 50 minutes', 'khoảng 50 phút'),
            before=('numbers, simple equations and inequalities (grade 9)', 'số, phương trình và bất đẳng thức đơn giản (lớp 9)'))
goals = [
 ('decide whether a sentence is a proposition and whether it is true or false;', 'nhận biết một câu có phải [[mệnh đề]] không và [[đúng / sai]];'),
 ('write the negation of a proposition;', 'viết [[mệnh đề phủ định]] của một mệnh đề;'),
 ('read implications and equivalences, and find a counterexample;', 'hiểu [[mệnh đề kéo theo]], [[mệnh đề tương đương]] và tìm [[phản ví dụ]];'),
 ('use the symbols for all and there exists, and negate them.', 'dùng kí hiệu [[với mọi (kí hiệu ∀)]], [[tồn tại (kí hiệu ∃)]] và phủ định chúng.'),
]
goals[0] = ('decide whether a sentence is a proposition, and whether it is true or false;', 'nhận biết một câu có phải [[mệnh đề]] không và đúng hay sai;')
goals[1] = ('write the negation of a proposition;', 'viết [[mệnh đề phủ định]] của một mệnh đề;')
goals[2] = ('read implications and equivalences, and find a counterexample;', 'hiểu [[mệnh đề kéo theo]], [[mệnh đề tương đương]] và tìm [[phản ví dụ]];')
goals[3] = ('use the symbols for all and there exists, and negate them.', 'dùng các kí hiệu ∀, ∃ và lập phủ định của chúng.')
vocab = [
 ('<b>proposition</b> – a sentence that is either true or false, not both.', '[[Mệnh đề]] – câu khẳng định chắc chắn đúng hoặc sai, không thể vừa đúng vừa sai.'),
 ('<b>true / false</b> – the two possible truth values of a proposition.', '[[Đúng / sai]] – hai giá trị chân lí có thể có của một mệnh đề.'),
 (r'<b>open statement</b> – a sentence with a variable, such as \(x+1=3\); it becomes a proposition when we give \(x\) a value.', r'[[Mệnh đề chứa biến]] – câu có biến, như \(x+1=3\); trở thành mệnh đề khi cho \(x\) một giá trị.'),
 (r'<b>negation</b> – the proposition \(\overline{P}\) that is true when \(P\) is false.', r'[[Mệnh đề phủ định]] – mệnh đề \(\overline{P}\) đúng khi \(P\) sai.'),
 (r'<b>implication</b> – “if \(P\), then \(Q\)”, written \(P\Rightarrow Q\).', r'[[Mệnh đề kéo theo]] – “nếu \(P\) thì \(Q\)”, viết \(P\Rightarrow Q\).'),
 ('<b>hypothesis / conclusion</b> – \\(P\\) is the hypothesis and \\(Q\\) is the conclusion of \\(P\\Rightarrow Q\\).', '[[Giả thiết]] / [[kết luận]] – \\(P\\) là giả thiết, \\(Q\\) là kết luận của \\(P\\Rightarrow Q\\).'),
 (r'<b>converse</b> – the implication \(Q\Rightarrow P\).', r'[[Mệnh đề đảo]] – mệnh đề \(Q\Rightarrow P\).'),
 (r'<b>equivalence</b> – \(P\Leftrightarrow Q\): \(P\Rightarrow Q\) and \(Q\Rightarrow P\) are both true.', r'[[Mệnh đề tương đương]] – \(P\Leftrightarrow Q\): cả \(P\Rightarrow Q\) và \(Q\Rightarrow P\) đều đúng.'),
 (r'<b>for all</b> (\(\forall\)) and <b>there exists</b> (\(\exists\)) – the two quantifiers.', r'[[Với mọi (kí hiệu ∀)]] và [[tồn tại (kí hiệu ∃)]] – hai kí hiệu lượng từ.'),
 ('<b>counterexample</b> – one example that shows a statement is false.', '[[Phản ví dụ]] – một ví dụ cho thấy phát biểu là sai.'),
]
vocab = [(a, b.replace('[[Với mọi (kí hiệu ∀)]] và [[tồn tại (kí hiệu ∃)]]', '[[Với mọi (kí hiệu ∀)]] và [[tồn tại (kí hiệu ∃)]]')) for a, b in vocab]
phrases = [
 ('<b>Is the statement true or false?</b>', 'Phát biểu đúng hay sai?'),
 ('<b>Write the negation of the statement.</b>', 'Viết phủ định của phát biểu.'),
 ('<b>If … then …</b>', 'Nếu … thì …'),
 ('<b>… if and only if …</b>', '… khi và chỉ khi …'),
 ('<b>Give a counterexample.</b>', 'Hãy nêu một phản ví dụ.'),
 ('<b>For all … / There exists …</b>', 'Với mọi … / Tồn tại …'),
]
review = (
 T('<b>Equations and inequalities.</b> \\(x+1=3\\) is true only for \\(x=2\\). \\(x>4\\) is true for \\(x=5\\) and false for \\(x=1\\).', '<b>Phương trình, bất phương trình.</b> \\(x+1=3\\) chỉ đúng khi \\(x=2\\). \\(x>4\\) đúng khi \\(x=5\\), sai khi \\(x=1\\).') +
 T('<b>Divisibility.</b> “\\(n\\,\\vdots\\,6\\)” means \\(n\\) is divisible by 6. Every multiple of 6 is a multiple of 3.', '<b>Chia hết.</b> “\\(n\\,\\vdots\\,6\\)” nghĩa là \\(n\\) chia hết cho 6. Mọi bội của 6 đều là bội của 3.') +
 T('<b>Prime numbers.</b> A prime has exactly two divisors, 1 and itself: 2, 3, 5, 7, 11, …', '<b>Số nguyên tố.</b> Số nguyên tố có đúng hai ước là 1 và chính nó: 2, 3, 5, 7, 11, …'))

theory = '<h3>5.1 %s</h3>' % TI('Propositions', 'Mệnh đề')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T('A <b>proposition</b> is a sentence that is either true or false, but not both.', '[[Mệnh đề]] là một câu khẳng định chắc chắn <b>đúng</b> hoặc <b>sai</b>, không thể vừa đúng vừa sai.'),
  T('“\\(5>3\\)” is a true proposition. “\\(2+2=5\\)” is a false proposition. A question or an order is not a proposition.', '“\\(5>3\\)” là mệnh đề đúng. “\\(2+2=5\\)” là mệnh đề sai. Câu hỏi hay câu mệnh lệnh không phải là mệnh đề.'))
theory += BOX('mint', ('Open statements', 'Mệnh đề chứa biến'),
  T('A sentence with a variable, such as \\(x+1=3\\), is an <b>open statement</b> \\(P(x)\\). It is not a proposition yet. When we give \\(x\\) a value, or say “for all” or “there exists”, it becomes a proposition.', 'Câu có biến, như \\(x+1=3\\), là [[mệnh đề chứa biến]] \\(P(x)\\); nó chưa phải mệnh đề. Khi gán cho \\(x\\) một giá trị, hoặc thêm “với mọi”, “tồn tại”, nó trở thành mệnh đề.'),
  T('Example: \\(P(2)\\): “\\(2+1=3\\)” is true, and \\(P(5)\\): “\\(5+1=3\\)” is false.', 'Ví dụ: \\(P(2)\\): “\\(2+1=3\\)” đúng, \\(P(5)\\): “\\(5+1=3\\)” sai.'))

theory += '<h3>5.2 %s</h3>' % TI('Negation', 'Mệnh đề phủ định')
theory += BOX('blue', ('Negation', 'Phủ định'),
  T('The <b>negation</b> of \\(P\\) is written \\(\\overline{P}\\) (read “not \\(P\\)”). \\(P\\) and \\(\\overline{P}\\) always have opposite truth values.', '[[Mệnh đề phủ định]] của \\(P\\) kí hiệu \\(\\overline{P}\\) (đọc “không \\(P\\)”). \\(P\\) và \\(\\overline{P}\\) luôn có giá trị đúng – sai trái ngược nhau.'),
  T('Example: \\(P\\): “17 is a prime number” (true). \\(\\overline{P}\\): “17 is not a prime number” (false).', 'Ví dụ: \\(P\\): “17 là số nguyên tố” (đúng). \\(\\overline{P}\\): “17 không là số nguyên tố” (sai).'))
theory += TBL([TI('Statement', 'Mệnh đề'), TI('Negation', 'Phủ định')], [[r'\(a=b\)', r'\(a\ne b\)'], [r'\(a>b\)', r'\(a\le b\)'], [r'\(a\ge b\)', r'\(a\lt b\)'], [r'\(a\lt b\)', r'\(a\ge b\)'], [r'\(a\le b\)', r'\(a>b\)']])

theory += '<h3>5.3 %s</h3>' % TI('Implications and equivalences', 'Mệnh đề kéo theo và mệnh đề tương đương')
theory += BOX('blue', ('Implication', 'Mệnh đề kéo theo'),
  T('“If \\(P\\), then \\(Q\\)” is the <b>implication</b> \\(P\\Rightarrow Q\\). \\(P\\) is the <b>hypothesis</b> and \\(Q\\) is the <b>conclusion</b>.', '“Nếu \\(P\\) thì \\(Q\\)” là [[mệnh đề kéo theo]] \\(P\\Rightarrow Q\\); \\(P\\) là [[giả thiết]], \\(Q\\) là [[kết luận]].'),
  T('\\(P\\Rightarrow Q\\) is <b>false only when</b> \\(P\\) is true and \\(Q\\) is false. In all other cases it is true.', '\\(P\\Rightarrow Q\\) <b>chỉ sai khi</b> \\(P\\) đúng và \\(Q\\) sai. Các trường hợp còn lại đều đúng.'),
  T('The <b>converse</b> of \\(P\\Rightarrow Q\\) is \\(Q\\Rightarrow P\\). A true implication can have a false converse.', '[[Mệnh đề đảo]] của \\(P\\Rightarrow Q\\) là \\(Q\\Rightarrow P\\). Mệnh đề đúng có thể có mệnh đề đảo sai.'))
theory += TBL([r'\(P\)', r'\(Q\)', r'\(P\Rightarrow Q\)'], [[TI('true', 'đúng'), TI('true', 'đúng'), TI('true', 'đúng')], [TI('true', 'đúng'), TI('false', 'sai'), TI('false', 'sai')], [TI('false', 'sai'), TI('true', 'đúng'), TI('true', 'đúng')], [TI('false', 'sai'), TI('false', 'sai'), TI('true', 'đúng')]])
theory += BOX('mint', ('Equivalence and conditions', 'Mệnh đề tương đương và điều kiện'),
  T('If both \\(P\\Rightarrow Q\\) and \\(Q\\Rightarrow P\\) are true, we write \\(P\\Leftrightarrow Q\\) and read “\\(P\\) if and only if \\(Q\\)”. We say \\(P\\) is a <b>necessary and sufficient condition</b> for \\(Q\\).', 'Nếu cả \\(P\\Rightarrow Q\\) và \\(Q\\Rightarrow P\\) đều đúng, ta viết \\(P\\Leftrightarrow Q\\) và đọc “\\(P\\) khi và chỉ khi \\(Q\\)”; \\(P\\) là [[điều kiện cần và đủ]] để có \\(Q\\).'),
  T('When \\(P\\Rightarrow Q\\) is true: \\(P\\) is a <i>sufficient</i> condition for \\(Q\\) (đủ), and \\(Q\\) is a <i>necessary</i> condition for \\(P\\) (cần).', 'Khi \\(P\\Rightarrow Q\\) đúng: \\(P\\) là điều kiện <i>đủ</i> để có \\(Q\\), còn \\(Q\\) là điều kiện <i>cần</i> để có \\(P\\).'),
  T('To show a statement is false, one <b>counterexample</b> is enough.', 'Để chứng tỏ một phát biểu sai, chỉ cần một [[phản ví dụ]].'))

theory += '<h3>5.4 %s</h3>' % TI('For all and there exists', 'Kí hiệu ∀ và ∃')
theory += BOX('blue', ('Quantifiers', 'Lượng từ'),
  T('\\(\\forall x\\in X,\\ P(x)\\): “for all \\(x\\) in \\(X\\), \\(P(x)\\)”. It is true only if \\(P(x)\\) holds for <b>every</b> \\(x\\).', '\\(\\forall x\\in X,\\ P(x)\\): “với mọi \\(x\\) thuộc \\(X\\), \\(P(x)\\)”. Chỉ đúng khi \\(P(x)\\) đúng với <b>mọi</b> \\(x\\).'),
  T('\\(\\exists x\\in X,\\ P(x)\\): “there exists \\(x\\) in \\(X\\) such that \\(P(x)\\)”. It is true if <b>at least one</b> \\(x\\) works.', '\\(\\exists x\\in X,\\ P(x)\\): “tồn tại \\(x\\) thuộc \\(X\\) sao cho \\(P(x)\\)”. Đúng khi có <b>ít nhất một</b> \\(x\\) thỏa mãn.'))
theory += BOX('yellow', ('Negating quantifiers', 'Phủ định lượng từ'),
  T('Swap \\(\\forall\\) and \\(\\exists\\), then negate the sentence after it.', 'Đổi \\(\\forall\\) thành \\(\\exists\\) (và ngược lại), rồi phủ định phần mệnh đề phía sau.'),
  M(r'\overline{\forall x\in X,\ P(x)}=\exists x\in X,\ \overline{P(x)}\qquad\overline{\exists x\in X,\ P(x)}=\forall x\in X,\ \overline{P(x)}'),
  T('Example: the negation of \\(\\forall x\\in\\mathbb{R},\\ x^2>0\\) is \\(\\exists x\\in\\mathbb{R},\\ x^2\\le 0\\).', 'Ví dụ: phủ định của \\(\\forall x\\in\\mathbb{R},\\ x^2>0\\) là \\(\\exists x\\in\\mathbb{R},\\ x^2\\le 0\\).'))

examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('Is it a proposition?', 'Có phải mệnh đề không?'),
  T('Which of these are propositions? Say whether each proposition is true or false. (a) \\(7\\) is a prime number. (b) \\(3x-1=5\\). (c) \\(2^5=30\\).', 'Câu nào là mệnh đề? Mệnh đề đó đúng hay sai? (a) \\(7\\) là số nguyên tố. (b) \\(3x-1=5\\). (c) \\(2^5=30\\).'),
  ('A proposition is certainly true or false. A sentence with a variable is not.', 'Mệnh đề chắc chắn đúng hoặc sai. Câu có biến thì chưa phải mệnh đề.'),
  [T('(a) It is a proposition, and it is true: 7 has only the divisors 1 and 7.', '(a) Là mệnh đề đúng: 7 chỉ có ước là 1 và 7.'),
   T('(b) It has the variable \\(x\\): it is an open statement, not a proposition.', '(b) Có biến \\(x\\): là mệnh đề chứa biến, chưa phải mệnh đề.'),
   T('(c) It is a proposition, and it is false because \\(2^5=32\\).', '(c) Là mệnh đề sai vì \\(2^5=32\\).')],
  T('(a) true proposition; (b) not a proposition; (c) false proposition.', '(a) mệnh đề đúng; (b) không phải mệnh đề; (c) mệnh đề sai.'))
examples += EXAMPLE(2, ('Basic', 'Cơ bản'), ('Writing a negation', 'Lập mệnh đề phủ định'),
  T('Write the negation of each proposition and say which one is true. (a) \\(P\\): “17 is divisible by 3”. (b) \\(Q\\): \\(\\sqrt2>1.4\\).', 'Lập phủ định của mỗi mệnh đề và cho biết mệnh đề nào đúng. (a) \\(P\\): “17 chia hết cho 3”. (b) \\(Q\\): \\(\\sqrt2>1.4\\).'),
  ('Negate the sentence, and for an inequality use the table of negations.', 'Phủ định cả câu; với bất đẳng thức dùng bảng phủ định.'),
  [T('(a) \\(\\overline{P}\\): “17 is not divisible by 3”. \\(17=3\\cdot5+2\\), so \\(P\\) is false and \\(\\overline{P}\\) is true.', '(a) \\(\\overline{P}\\): “17 không chia hết cho 3”. \\(17=3\\cdot5+2\\) nên \\(P\\) sai, \\(\\overline{P}\\) đúng.'),
   T('(b) \\(\\overline{Q}\\): \\(\\sqrt2\\le1.4\\). Since \\(\\sqrt2\\approx1.4142>1.4\\), \\(Q\\) is true and \\(\\overline{Q}\\) is false.', '(b) \\(\\overline{Q}\\): \\(\\sqrt2\\le1.4\\). Vì \\(\\sqrt2\\approx1.4142>1.4\\) nên \\(Q\\) đúng, \\(\\overline{Q}\\) sai.')],
  T('(a) “17 is not divisible by 3” (true); (b) \\(\\sqrt2\\le1.4\\) (false).', '(a) “17 không chia hết cho 3” (đúng); (b) \\(\\sqrt2\\le1.4\\) (sai).'))
examples += EXAMPLE(3, ('Intermediate', 'Trung bình'), ('An implication and its converse', 'Mệnh đề kéo theo và mệnh đề đảo'),
  T('Let \\(P\\): “\\(n\\) is divisible by 6” and \\(Q\\): “\\(n\\) is divisible by 3”. Is \\(P\\Rightarrow Q\\) true? State the converse and decide if it is true.', 'Cho \\(P\\): “\\(n\\) chia hết cho 6” và \\(Q\\): “\\(n\\) chia hết cho 3”. \\(P\\Rightarrow Q\\) có đúng không? Phát biểu mệnh đề đảo và xét tính đúng sai.'),
  ('A statement about all \\(n\\) is true only if there is no counterexample.', 'Phát biểu về mọi \\(n\\) chỉ đúng khi không có phản ví dụ.'),
  [T('If \\(n\\,\\vdots\\,6\\), then \\(n=6k=3\\cdot(2k)\\), so \\(n\\,\\vdots\\,3\\). Hence \\(P\\Rightarrow Q\\) is true.', 'Nếu \\(n\\,\\vdots\\,6\\) thì \\(n=6k=3\\cdot(2k)\\) nên \\(n\\,\\vdots\\,3\\). Vậy \\(P\\Rightarrow Q\\) đúng.'),
   T('The converse \\(Q\\Rightarrow P\\): “if \\(n\\,\\vdots\\,3\\), then \\(n\\,\\vdots\\,6\\)”.', 'Mệnh đề đảo \\(Q\\Rightarrow P\\): “nếu \\(n\\,\\vdots\\,3\\) thì \\(n\\,\\vdots\\,6\\)”.'),
   T('Counterexample: \\(n=3\\). \\(3\\,\\vdots\\,3\\) but \\(3\\,\\not\\vdots\\,6\\). So the converse is false.', 'Phản ví dụ: \\(n=3\\). \\(3\\,\\vdots\\,3\\) nhưng \\(3\\,\\not\\vdots\\,6\\). Vậy mệnh đề đảo sai.')],
  T('\\(P\\Rightarrow Q\\) is true; its converse is false (counterexample \\(n=3\\)).', '\\(P\\Rightarrow Q\\) đúng; mệnh đề đảo sai (phản ví dụ \\(n=3\\)).'))
examples += EXAMPLE(4, ('Intermediate', 'Trung bình'), ('Quantifiers and their negations', 'Lượng từ và phủ định'),
  T('Decide if each proposition is true. Then write the negation of (b). (a) \\(\\forall x\\in\\mathbb{R},\\ x^2\\ge0\\). (b) \\(\\forall x\\in\\mathbb{R},\\ x^2>x\\). (c) \\(\\exists x\\in\\mathbb{R},\\ x^2=-1\\).', 'Xét tính đúng sai của mỗi mệnh đề, rồi viết phủ định của (b). (a) \\(\\forall x\\in\\mathbb{R},\\ x^2\\ge0\\). (b) \\(\\forall x\\in\\mathbb{R},\\ x^2>x\\). (c) \\(\\exists x\\in\\mathbb{R},\\ x^2=-1\\).'),
  ('For \\(\\forall\\), look for a counterexample. For \\(\\exists\\), look for one value that works.', 'Với \\(\\forall\\) hãy tìm phản ví dụ. Với \\(\\exists\\) hãy tìm một giá trị thỏa mãn.'),
  [T('(a) A real square is never negative, so (a) is true.', '(a) Bình phương số thực không âm nên (a) đúng.'),
   T('(b) For \\(x=0\\): \\(0>0\\) is false. This counterexample shows (b) is false.', '(b) Với \\(x=0\\): \\(0>0\\) sai. Phản ví dụ này cho thấy (b) sai.'),
   T('(c) \\(x^2\\ge0\\) for every real \\(x\\), so no \\(x\\) gives \\(-1\\): (c) is false.', '(c) \\(x^2\\ge0\\) với mọi số thực \\(x\\) nên không có \\(x\\) nào cho \\(-1\\): (c) sai.'),
   T('The negation of (b) is \\(\\exists x\\in\\mathbb{R},\\ x^2\\le x\\). It is true (take \\(x=0\\)).', 'Phủ định của (b) là \\(\\exists x\\in\\mathbb{R},\\ x^2\\le x\\). Mệnh đề này đúng (lấy \\(x=0\\)).')],
  T('(a) true; (b) false; (c) false. \\(\\overline{(b)}\\): \\(\\exists x\\in\\mathbb{R},\\ x^2\\le x\\).', '(a) đúng; (b) sai; (c) sai. \\(\\overline{(b)}\\): \\(\\exists x\\in\\mathbb{R},\\ x^2\\le x\\).'))
examples += EXAMPLE(5, ('Advanced', 'Nâng cao'), ('Prove or disprove', 'Chứng minh hoặc bác bỏ'),
  T('(a) Is the proposition “for every positive integer \\(n\\), \\(n^2-n+11\\) is a prime number” true? (b) Prove: “if \\(n\\) is odd, then \\(n^2\\) is odd”.', '(a) Mệnh đề “với mọi số nguyên dương \\(n\\), \\(n^2-n+11\\) là số nguyên tố” đúng hay sai? (b) Chứng minh: “nếu \\(n\\) lẻ thì \\(n^2\\) lẻ”.'),
  ('For (a) search for a counterexample. For (b) write \\(n\\) in the form \\(2k+1\\).', 'Ở (a) hãy tìm phản ví dụ. Ở (b) viết \\(n\\) dạng \\(2k+1\\).'),
  [T('(a) Try \\(n=1,2,3,\\dots\\): the values 11, 13, 17, 23, 31, … are all prime.', '(a) Thử \\(n=1,2,3,\\dots\\): các giá trị 11, 13, 17, 23, 31, … đều nguyên tố.'),
   T('But for \\(n=11\\): \\(11^2-11+11=121=11\\cdot11\\) is not prime. So the proposition is <b>false</b>.', 'Nhưng với \\(n=11\\): \\(11^2-11+11=121=11\\cdot11\\) không nguyên tố. Vậy mệnh đề <b>sai</b>.'),
   T('(b) Let \\(n=2k+1\\). Then \\(n^2=4k^2+4k+1=2(2k^2+2k)+1\\), which is odd. The implication is true.', '(b) Đặt \\(n=2k+1\\). Khi đó \\(n^2=4k^2+4k+1=2(2k^2+2k)+1\\) là số lẻ. Mệnh đề kéo theo đúng.')],
  T('(a) false (counterexample \\(n=11\\)); (b) true.', '(a) sai (phản ví dụ \\(n=11\\)); (b) đúng.'))

HN = ('Enter a whole number.', 'Nhập một số nguyên.')
Q1 = [
  [MCQ(1, ('Which of these is a proposition?', 'Câu nào sau đây là một mệnh đề?'), ['x+2=5', '7-3=5', 'y\\gt1', 'a+b=c'], 'b', ('Answer: b. \\(7-3=5\\) has no variable: it is a (false) proposition.', 'Đáp án b. \\(7-3=5\\) không chứa biến: đó là mệnh đề (sai).')),
   MCQ(2, ('What is the negation of \\(x\\ge3\\)?', 'Phủ định của \\(x\\ge3\\) là gì?'), ['x\\lt3', 'x\\gt3', 'x\\le3', 'x\\ne3'], 'a', ('Answer: a. The negation of \\(\\ge\\) is \\(\\lt\\).', 'Đáp án a. Phủ định của \\(\\ge\\) là \\(\\lt\\).')),
   MCQ(3, ('Which implication is true for every positive integer \\(n\\)?', 'Mệnh đề kéo theo nào đúng với mọi số nguyên dương \\(n\\)?'), ['n\\,\\vdots\\,6\\Rightarrow n\\,\\vdots\\,3', 'n\\,\\vdots\\,3\\Rightarrow n\\,\\vdots\\,6', 'n\\,\\vdots\\,4\\Rightarrow n\\,\\vdots\\,8', 'n\\,\\vdots\\,5\\Rightarrow n\\,\\vdots\\,10'], 'a', ('Answer: a. Every multiple of 6 is a multiple of 3. The others fail for \\(n=3,4,5\\).', 'Đáp án a. Mọi bội của 6 đều là bội của 3. Các câu còn lại sai khi \\(n=3,4,5\\).'))],
  [TF(4, ('The proposition \\(\\forall x\\in\\mathbb{R},\\ x^2>0\\) is true.', 'Mệnh đề \\(\\forall x\\in\\mathbb{R},\\ x^2>0\\) là đúng.'), 'false', ('False: for \\(x=0\\), \\(x^2=0\\).', 'Sai: với \\(x=0\\) thì \\(x^2=0\\).')),
   TF(5, ('If \\(P\\Rightarrow Q\\) is true, then \\(Q\\Rightarrow P\\) is also true.', 'Nếu \\(P\\Rightarrow Q\\) đúng thì \\(Q\\Rightarrow P\\) cũng đúng.'), 'false', ('False: for example \\(n\\,\\vdots\\,6\\Rightarrow n\\,\\vdots\\,3\\) is true but its converse is false.', 'Sai: chẳng hạn \\(n\\,\\vdots\\,6\\Rightarrow n\\,\\vdots\\,3\\) đúng nhưng mệnh đề đảo sai.'))],
  [SHORT(6, ('How many integers \\(x\\) satisfy \\(-3\\le x\\le3\\) and \\(x^2\\lt4\\)?', 'Có bao nhiêu số nguyên \\(x\\) thỏa \\(-3\\le x\\le3\\) và \\(x^2\\lt4\\)?'), '3', 'number', HN, ('Answer: 3: \\(x=-1,0,1\\).', 'Đáp số: 3: \\(x=-1,0,1\\).')),
   SHORT(7, ('Find the smallest positive integer \\(n\\) for which “\\(n^2-n+11\\) is prime” is false.', 'Tìm số nguyên dương \\(n\\) nhỏ nhất để “\\(n^2-n+11\\) là số nguyên tố” sai.'), '11', 'number', HN, ('Answer: 11, because \\(11^2-11+11=121=11^2\\).', 'Đáp số: 11, vì \\(11^2-11+11=121=11^2\\).'))]]
Q2 = [
  [MCQ(1, ('Which sentence below is a proposition?', 'Câu nào dưới đây là một mệnh đề?'), ['n-4\\gt1', '5\\times4=20', 'k^2=2k', 't\\le-1'], 'b', ('Answer: b. \\(5\\times4=20\\) has no variable and is true.', 'Đáp án b. \\(5\\times4=20\\) không có biến và đúng.')),
   MCQ(2, ('What is the negation of \\(x\\lt5\\)?', 'Phủ định của \\(x\\lt5\\) là gì?'), ['x\\gt5', 'x\\le5', 'x\\ne5', 'x\\ge5'], 'd', ('Answer: d. The negation of \\(\\lt\\) is \\(\\ge\\).', 'Đáp án d. Phủ định của \\(\\lt\\) là \\(\\ge\\).')),
   MCQ(3, ('Which implication is always true for positive integers \\(n\\)?', 'Mệnh đề kéo theo nào luôn đúng với các số nguyên dương \\(n\\)?'), ['n\\,\\vdots\\,4\\Rightarrow n\\,\\vdots\\,12', 'n\\,\\vdots\\,12\\Rightarrow n\\,\\vdots\\,4', 'n\\,\\vdots\\,2\\Rightarrow n\\,\\vdots\\,6', 'n\\,\\vdots\\,5\\Rightarrow n\\,\\vdots\\,15'], 'b', ('Answer: b. Every multiple of 12 is a multiple of 4. The others fail for \\(n=4,2,5\\).', 'Đáp án b. Mọi bội của 12 đều là bội của 4. Các câu còn lại sai khi \\(n=4,2,5\\).'))],
  [TF(4, ('The proposition \\(\\exists x\\in\\mathbb{R},\\ x^2=-4\\) is true.', 'Mệnh đề \\(\\exists x\\in\\mathbb{R},\\ x^2=-4\\) là đúng.'), 'false', ('False: \\(x^2\\ge0\\) for every real \\(x\\).', 'Sai: \\(x^2\\ge0\\) với mọi số thực \\(x\\).')),
   TF(5, ('\\(P\\Leftrightarrow Q\\) means that both \\(P\\Rightarrow Q\\) and \\(Q\\Rightarrow P\\) are true.', '\\(P\\Leftrightarrow Q\\) nghĩa là cả \\(P\\Rightarrow Q\\) và \\(Q\\Rightarrow P\\) đều đúng.'), 'true', ('True. This is the definition of an equivalence.', 'Đúng. Đó là định nghĩa mệnh đề tương đương.'))],
  [SHORT(6, ('How many integers \\(x\\) satisfy \\(-4\\le x\\le4\\) and \\(x^2\\lt9\\)?', 'Có bao nhiêu số nguyên \\(x\\) thỏa \\(-4\\le x\\le4\\) và \\(x^2\\lt9\\)?'), '5', 'number', HN, ('Answer: 5: \\(x=-2,-1,0,1,2\\).', 'Đáp số: 5: \\(x=-2,-1,0,1,2\\).')),
   SHORT(7, ('Find the smallest positive integer \\(n\\) for which “\\(n^2-n+41\\) is prime” is false.', 'Tìm số nguyên dương \\(n\\) nhỏ nhất để “\\(n^2-n+41\\) là số nguyên tố” sai.'), '41', 'number', HN, ('Answer: 41, because \\(41^2-41+41=1681=41^2\\).', 'Đáp số: 41, vì \\(41^2-41+41=1681=41^2\\).'))]]
Q3 = [
  [MCQ(1, ('Which statement here is a proposition?', 'Phát biểu nào sau đây là một mệnh đề?'), ['3z\\gt12', 'm\\ge5', 'x+y=10', '\\sqrt{25}=5'], 'd', ('Answer: d. \\(\\sqrt{25}=5\\) has no variable and is true.', 'Đáp án d. \\(\\sqrt{25}=5\\) không có biến và đúng.')),
   MCQ(2, ('What is the negation of \\(x\\le-2\\)?', 'Phủ định của \\(x\\le-2\\) là gì?'), ['x\\ge-2', 'x\\gt-2', 'x\\lt-2', 'x\\ne-2'], 'b', ('Answer: b. The negation of \\(\\le\\) is \\(\\gt\\).', 'Đáp án b. Phủ định của \\(\\le\\) là \\(\\gt\\).')),
   MCQ(3, ('Which of these implications holds for all positive integers \\(n\\)?', 'Mệnh đề kéo theo nào dưới đây đúng với mọi số nguyên dương \\(n\\)?'), ['n\\,\\vdots\\,3\\Rightarrow n\\,\\vdots\\,9', 'n\\,\\vdots\\,2\\Rightarrow n\\,\\vdots\\,4', 'n\\,\\vdots\\,9\\Rightarrow n\\,\\vdots\\,3', 'n\\,\\vdots\\,5\\Rightarrow n\\,\\vdots\\,25'], 'c', ('Answer: c. Every multiple of 9 is a multiple of 3. The others fail for \\(n=3,2,5\\).', 'Đáp án c. Mọi bội của 9 đều là bội của 3. Các câu còn lại sai khi \\(n=3,2,5\\).'))],
  [TF(4, ('The negation of \\(\\forall x\\in\\mathbb{R},\\ x^2\\ge0\\) is \\(\\exists x\\in\\mathbb{R},\\ x^2\\lt0\\).', 'Phủ định của \\(\\forall x\\in\\mathbb{R},\\ x^2\\ge0\\) là \\(\\exists x\\in\\mathbb{R},\\ x^2\\lt0\\).'), 'true', ('True: swap \\(\\forall\\) to \\(\\exists\\) and negate \\(\\ge\\) to \\(\\lt\\).', 'Đúng: đổi \\(\\forall\\) thành \\(\\exists\\) và phủ định \\(\\ge\\) thành \\(\\lt\\).')),
   TF(5, ('For integers, “\\(n\\) is even” \\(\\Leftrightarrow\\) “\\(n^2\\) is even”.', 'Với số nguyên, “\\(n\\) chẵn” \\(\\Leftrightarrow\\) “\\(n^2\\) chẵn”.'), 'true', ('True: if \\(n\\) is even then \\(n^2\\) is even; if \\(n\\) is odd then \\(n^2\\) is odd.', 'Đúng: \\(n\\) chẵn thì \\(n^2\\) chẵn; \\(n\\) lẻ thì \\(n^2\\) lẻ.'))],
  [SHORT(6, ('How many integers \\(x\\) satisfy \\(-5\\le x\\le5\\) and \\(x^2\\lt16\\)?', 'Có bao nhiêu số nguyên \\(x\\) thỏa \\(-5\\le x\\le5\\) và \\(x^2\\lt16\\)?'), '7', 'number', HN, ('Answer: 7: \\(x=-3,\\dots,3\\).', 'Đáp số: 7: \\(x=-3,\\dots,3\\).')),
   SHORT(7, ('Find the smallest positive integer \\(n\\) for which “\\(n^2-n+17\\) is prime” is false.', 'Tìm số nguyên dương \\(n\\) nhỏ nhất để “\\(n^2-n+17\\) là số nguyên tố” sai.'), '17', 'number', HN, ('Answer: 17, because \\(17^2-17+17=289=17^2\\).', 'Đáp số: 17, vì \\(17^2-17+17=289=17^2\\).'))]]
_T = [('A. Multiple Choice', 'A. Trắc nghiệm nhiều lựa chọn'), ('B. True or False', 'B. Đúng hoặc sai'), ('C. Short Answer', 'C. Trả lời ngắn')]
practice = LEVEL_PRACTICE(_T, {1: Q1, 2: Q2, 3: Q3})
_SP = SELF(sp_g10.B1, start=8, avoid=[t[1] for t in practice])
practice = practice + [(('D. Self-practice: Multiple Choice', 'D. Tự luyện: trắc nghiệm'), _SP[lv], [lv]) for lv in (1, 2, 3)]

mistakes = [
 ('<b>Calling an open statement a proposition.</b> “\\(x+1=3\\)” is true or false only after we know \\(x\\).', '<b>Coi câu có biến là mệnh đề.</b> “\\(x+1=3\\)” chỉ đúng hoặc sai khi biết \\(x\\).'),
 ('<b>Wrong negation of an inequality.</b> The negation of \\(a>b\\) is \\(a\\le b\\), not \\(a\\lt b\\).', '<b>Phủ định sai bất đẳng thức.</b> Phủ định của \\(a>b\\) là \\(a\\le b\\), không phải \\(a\\lt b\\).'),
 ('<b>Forgetting to swap \\(\\forall\\) and \\(\\exists\\).</b> \\(\\overline{\\forall x,P(x)}\\) is \\(\\exists x,\\overline{P(x)}\\).', '<b>Quên đổi \\(\\forall\\) và \\(\\exists\\).</b> \\(\\overline{\\forall x,P(x)}\\) là \\(\\exists x,\\overline{P(x)}\\).'),
 ('<b>Mixing an implication with its converse.</b> \\(P\\Rightarrow Q\\) true does not make \\(Q\\Rightarrow P\\) true.', '<b>Nhầm mệnh đề kéo theo với mệnh đề đảo.</b> \\(P\\Rightarrow Q\\) đúng chưa chắc \\(Q\\Rightarrow P\\) đúng.'),
 ('<b>Proving “for all” by examples.</b> Checking a few values is not a proof; one counterexample is enough to disprove.', '<b>Chứng minh “với mọi” bằng vài ví dụ.</b> Thử vài giá trị chưa phải chứng minh; một phản ví dụ là đủ để bác bỏ.'),
]
summary = [
 ('A proposition is a sentence that is true or false (not both). A sentence with a variable is an open statement.', 'Mệnh đề là câu chắc chắn đúng hoặc sai (không cả hai). Câu có biến là mệnh đề chứa biến.'),
 ('\\(\\overline{P}\\) has the opposite truth value of \\(P\\). Negations: \\(=\\to\\ne\\), \\(>\\to\\le\\), \\(\\ge\\to\\lt\\).', '\\(\\overline{P}\\) có giá trị trái ngược \\(P\\). Phủ định: \\(=\\to\\ne\\), \\(>\\to\\le\\), \\(\\ge\\to\\lt\\).'),
 ('\\(P\\Rightarrow Q\\) is false only when \\(P\\) is true and \\(Q\\) is false. \\(P\\Leftrightarrow Q\\) needs both directions.', '\\(P\\Rightarrow Q\\) chỉ sai khi \\(P\\) đúng và \\(Q\\) sai. \\(P\\Leftrightarrow Q\\) cần cả hai chiều.'),
 ('\\(\\forall\\): true only if no counterexample. \\(\\exists\\): true if one example works. Negation swaps \\(\\forall\\) and \\(\\exists\\).', '\\(\\forall\\): đúng khi không có phản ví dụ. \\(\\exists\\): đúng khi có một ví dụ. Phủ định đổi \\(\\forall\\) và \\(\\exists\\).'),
 ('Key English phrases: true or false; write the negation; if … then …; if and only if; give a counterexample.', 'Cụm tiếng Anh cần nhớ: true or false (đúng hay sai); write the negation (viết phủ định); if … then …; if and only if; give a counterexample.'),
]
checks = [
 ('I can tell a proposition from an open statement.', 'Tôi phân biệt được mệnh đề với mệnh đề chứa biến.'),
 ('I can write the negation of a proposition.', 'Tôi viết được mệnh đề phủ định.'),
 ('I can decide whether an implication or its converse is true.', 'Tôi xét được tính đúng sai của mệnh đề kéo theo và mệnh đề đảo.'),
 ('I can use \\(\\forall\\), \\(\\exists\\) and negate them.', 'Tôi dùng được ∀, ∃ và lập phủ định của chúng.'),
 STD_SUMMARY_CHECK_EN(),
]

lesson(id=LID, title_en='Propositions', title_vi='Mệnh đề', topic=TOPIC, folder='propositions-and-sets', file='propositions',
       catalog_title_vi='Mệnh đề', meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Propositions, negation, implications, equivalences and the symbols for all and there exists.', level='Beginner', minutes=50,
       description_vi='Bài 1 – Mệnh đề, mệnh đề phủ định, mệnh đề kéo theo, mệnh đề tương đương, kí hiệu ∀ và ∃.',
       tags_vi=['mệnh đề', 'phủ định', 'kéo theo', 'tương đương', 'với mọi', 'tồn tại'],
       prerequisites=[], tags=['proposition', 'negation', 'implication', 'equivalence', 'quantifier', 'counterexample'], order=10)
