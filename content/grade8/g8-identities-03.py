# -*- coding: utf-8 -*-
"""Nội dung bài g8-identities-03 = Toán 8 KNTT, Bài 8: Tổng và hiệu hai lập phương – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 8 (2026), Chapter 2 – Lesson 8, tr. 28–29 (sum of two cubes, difference of two cubes)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g8
from sp_g8 import Poly, M, L, tri

LID = 'g8-identities-03'
CH = 'Hằng đẳng thức đáng nhớ và ứng dụng'
TOPIC = ('Algebraic Identities and Applications', CH)
ensure_vocab([
 ('g8-sum-cubes', 'sum of two cubes', 'tổng hai lập phương', CH, 'A³ + B³ is the sum of two cubes.', ''),
 ('g8-diff-cubes', 'difference of two cubes', 'hiệu hai lập phương', CH, 'A³ − B³ is the difference of two cubes.', ''),
])
load_vocab()

# ---------- kiểm tra số liệu ----------
X = lambda c, a, b: (c, (a, b, 0))
x_, two = M(1, (1, 0, 0)), M(2, (0, 0, 0))
assert (x_ + two) * tri(x_, two, 1) == Poly.of([X(1, 3, 0), X(8, 0, 0)])                                          # Ví dụ 1
assert L(3, -1) * Poly.of([X(9, 2, 0), X(3, 1, 0), X(1, 0, 0)]) == Poly.of([X(27, 3, 0), X(-1, 0, 0)])           # Ví dụ 2
assert L(1, 2, (1, 0, 0), (0, 1, 0)) * Poly.of([X(1, 2, 0), X(-2, 1, 1), X(4, 0, 2)]) == Poly.of([X(1, 3, 0), X(8, 0, 3)])
A3 = L(1, -3) * Poly.of([X(1, 2, 0), X(3, 1, 0), X(9, 0, 0)]) - x_ * Poly.of([X(1, 2, 0), X(-5, 0, 0)])
assert A3 == Poly.of([X(5, 1, 0), X(-27, 0, 0)]) and A3.at(4) == -7                                               # Ví dụ 3
assert 4 ** 3 - 3 * 3 * 4 == 28 and 1 ** 3 + 3 ** 3 == 28                                                         # Ví dụ 4 (a, b = 1, 3)
assert 12 ** 3 - 8 == 1720 and 10 * (144 + 24 + 4) == 1720                                                       # Ví dụ 5

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 45 minutes', '45 phút'),
            before=('identities of Lessons 6–7', 'các hằng đẳng thức ở Bài 6, 7'))
goals = [
 (r'state the identities \(A^3+B^3\) and \(A^3-B^3\);', r'phát biểu được các hằng đẳng thức [[tổng hai lập phương]] và [[hiệu hai lập phương]];'),
 (r'expand products and write sums or differences of cubes as products;', r'khai triển tích và viết tổng, hiệu hai lập phương dưới dạng tích;'),
 (r'use all seven identities to simplify, evaluate and solve problems.', r'vận dụng bảy hằng đẳng thức đáng nhớ để rút gọn, tính giá trị và giải bài toán.')]
vocab = [
 (r'<b>sum of two cubes</b> – \(A^3+B^3=(A+B)(A^2-AB+B^2)\).', r'[[Tổng hai lập phương]] – \(A^3+B^3=(A+B)(A^2-AB+B^2)\).'),
 (r'<b>difference of two cubes</b> – \(A^3-B^3=(A-B)(A^2+AB+B^2)\).', r'[[Hiệu hai lập phương]] – \(A^3-B^3=(A-B)(A^2+AB+B^2)\).'),
 (r'<b>cube / product / expand</b> – as in Lessons 4–7.', r'[[Lập phương|lập phương (lớp 8)]] / [[tích]] / [[khai triển]] – như ở Bài 4–7.')]
phrases = [
 (r'<b>Expand the following expressions.</b>', r'Khai triển các biểu thức sau.'),
 (r'<b>Write the following expressions as products.</b>', r'Viết các biểu thức sau dưới dạng tích.'),
 (r'<b>Given \(a+b=4\) and \(ab=3\), calculate the value of \(a^3+b^3\).</b>', r'Cho \(a+b=4\) và \(ab=3\). Tính giá trị của \(a^3+b^3\).'),
 (r'<b>Prove the identity \(a^3+b^3=(a+b)^3-3ab(a+b)\).</b>', r'Chứng minh hằng đẳng thức \(a^3+b^3=(a+b)^3-3ab(a+b)\).'),
 (r'<b>\(A^3+B^3\)</b> is read "the sum of two cubes"; <b>\(A^3-B^3\)</b> "the difference of two cubes".', r'Cách đọc: \(A^3+B^3\) – tổng hai lập phương; \(A^3-B^3\) – hiệu hai lập phương.')]
review = (T(r'<b>Cubes (Lesson 7).</b> \((A+B)^3=A^3+3A^2B+3AB^2+B^3\).', r'<b>Lập phương (Bài 7).</b> \((A+B)^3=A^3+3A^2B+3AB^2+B^3\).'))

theory = '<h3>8.1 %s</h3>' % TI('Sum and difference of two cubes', 'Tổng và hiệu hai lập phương')
theory += BOX('blue', ('Identities', 'Hằng đẳng thức'),
  T(r'<b>Sum of two cubes:</b> \(A^3+B^3=(A+B)(A^2-AB+B^2)\).', r'<b>[[Tổng hai lập phương]]:</b> \(A^3+B^3=(A+B)(A^2-AB+B^2)\).'),
  T(r'<b>Difference of two cubes:</b> \(A^3-B^3=(A-B)(A^2+AB+B^2)\).', r'<b>[[Hiệu hai lập phương]]:</b> \(A^3-B^3=(A-B)(A^2+AB+B^2)\).'),
  T(r'Check by multiplying: \((A+B)(A^2-AB+B^2)=A^3-A^2B+AB^2+A^2B-AB^2+B^3=A^3+B^3\).', r'Kiểm tra bằng phép nhân: \((A+B)(A^2-AB+B^2)=A^3-A^2B+AB^2+A^2B-AB^2+B^3=A^3+B^3\).'),
  T(r'Examples: \(x^3+8=(x+2)(x^2-2x+4)\); \(27x^3-1=(3x-1)(9x^2+3x+1)\).', r'Ví dụ: \(x^3+8=(x+2)(x^2-2x+4)\); \(27x^3-1=(3x-1)(9x^2+3x+1)\).'))
theory += '<h3>8.2 %s</h3>' % TI('The seven identities', 'Bảy hằng đẳng thức đáng nhớ')
theory += TABLE([('Name', 'Tên'), ('Identity', 'Hằng đẳng thức')],
  [[TI('Square of a sum', 'Bình phương của một tổng'), '\\((A+B)^2=A^2+2AB+B^2\\)'],
   [TI('Square of a difference', 'Bình phương của một hiệu'), '\\((A-B)^2=A^2-2AB+B^2\\)'],
   [TI('Difference of two squares', 'Hiệu hai bình phương'), '\\(A^2-B^2=(A-B)(A+B)\\)'],
   [TI('Cube of a sum', 'Lập phương của một tổng'), '\\((A+B)^3=A^3+3A^2B+3AB^2+B^3\\)'],
   [TI('Cube of a difference', 'Lập phương của một hiệu'), '\\((A-B)^3=A^3-3A^2B+3AB^2-B^3\\)'],
   [TI('Sum of two cubes', 'Tổng hai lập phương'), '\\(A^3+B^3=(A+B)(A^2-AB+B^2)\\)'],
   [TI('Difference of two cubes', 'Hiệu hai lập phương'), '\\(A^3-B^3=(A-B)(A^2+AB+B^2)\\)']])
theory += BOX('yellow', ('Watch out!', 'Lưu ý'),
  T(r'\(A^3+B^3\ne(A+B)^3\). In the second factor of \(A^3+B^3\) the middle sign is <b>minus</b>; for \(A^3-B^3\) it is <b>plus</b>.', r'\(A^3+B^3\ne(A+B)^3\). Thừa số thứ hai của \(A^3+B^3\) có dấu <b>trừ</b> ở giữa; của \(A^3-B^3\) có dấu <b>cộng</b> ở giữa.'),
  T(r'Useful: \(a^3+b^3=(a+b)^3-3ab(a+b)\) and \(a^3-b^3=(a-b)^3+3ab(a-b)\).', r'Hay dùng: \(a^3+b^3=(a+b)^3-3ab(a+b)\) và \(a^3-b^3=(a-b)^3+3ab(a-b)\).'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Expand', 'Khai triển'),
  T(r'Expand \((x+2)(x^2-2x+4)\).', r'Khai triển \((x+2)(x^2-2x+4)\).'),
  ('It has the form \\((A+B)(A^2-AB+B^2)\\) with \\(A=x,\\ B=2\\).', 'Biểu thức có dạng \\((A+B)(A^2-AB+B^2)\\) với \\(A=x,\\ B=2\\).'),
  [T(r'\((x+2)(x^2-2x+4)=x^3+2^3=x^3+8\).', r'\((x+2)(x^2-2x+4)=x^3+2^3=x^3+8\).')],
  T(r'\(x^3+8\).', r'\(x^3+8\).'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Write as products', 'Viết dưới dạng tích'),
  T(r'Write as products: a) \(27x^3-1\); b) \(x^3+8y^3\).', r'Viết dưới dạng tích: a) \(27x^3-1\); b) \(x^3+8y^3\).'),
  ('Write each term as a cube.', 'Viết mỗi hạng tử dưới dạng lập phương.'),
  [T(r'a) \((3x)^3-1^3=(3x-1)(9x^2+3x+1)\).', r'a) \((3x)^3-1^3=(3x-1)(9x^2+3x+1)\).'),
   T(r'b) \(x^3+(2y)^3=(x+2y)(x^2-2xy+4y^2)\).', r'b) \(x^3+(2y)^3=(x+2y)(x^2-2xy+4y^2)\).')],
  T(r'\((3x-1)(9x^2+3x+1)\); \((x+2y)(x^2-2xy+4y^2)\).', r'\((3x-1)(9x^2+3x+1)\); \((x+2y)(x^2-2xy+4y^2)\).'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('Simplify', 'Rút gọn'),
  T(r'Simplify \(A=(x-3)(x^2+3x+9)-x(x^2-5)\), then find \(A\) at \(x=4\).', r'Rút gọn biểu thức \(A=(x-3)(x^2+3x+9)-x(x^2-5)\) rồi tính giá trị tại \(x=4\).'),
  ('The first product is \\(x^3-27\\).', 'Tích thứ nhất bằng \\(x^3-27\\).'),
  [T(r'\(A=x^3-27-x^3+5x=5x-27\).', r'\(A=x^3-27-x^3+5x=5x-27\).'),
   T(r'\(x=4\): \(A=20-27=-7\).', r'\(x=4\): \(A=20-27=-7\).')],
  T(r'\(A=5x-27=-7\).', r'\(A=5x-27\); tại \(x=4\), \(A=-7\).'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Without finding a and b', 'Không cần tìm a, b'),
  T(r'Given \(a+b=4\) and \(ab=3\), find \(a^3+b^3\).', r'Cho \(a+b=4\) và \(ab=3\). Tính \(a^3+b^3\).'),
  ('Use \\(a^3+b^3=(a+b)^3-3ab(a+b)\\).', 'Dùng \\(a^3+b^3=(a+b)^3-3ab(a+b)\\).'),
  [T(r'From \((a+b)^3=a^3+b^3+3ab(a+b)\): \(a^3+b^3=(a+b)^3-3ab(a+b)\).', r'Từ \((a+b)^3=a^3+b^3+3ab(a+b)\) suy ra \(a^3+b^3=(a+b)^3-3ab(a+b)\).'),
   T(r'\(a^3+b^3=4^3-3\cdot3\cdot4=64-36=28\).', r'\(a^3+b^3=4^3-3\cdot3\cdot4=64-36=28\).')],
  T(r'\(a^3+b^3=28\).', r'\(a^3+b^3=28\).'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Filling a tank', 'Đổ nước vào bể'),
  T(r'A cube-shaped tank has edge \(x\) dm. A cube-shaped stone with edge 2 dm lies at the bottom. The water needed to fill the tank is \(x^3-8\) liters. Write this as a product and find it when \(x=12\).', r'Một bể nước hình lập phương cạnh \(x\) dm, dưới đáy có một khối đá hình lập phương cạnh 2 dm. Lượng nước cần đổ để đầy bể là \(x^3-8\) (lít). Viết biểu thức này dưới dạng tích và tính giá trị khi \(x=12\).'),
  ('\\(x^3-8\\) is a difference of two cubes.', '\\(x^3-8\\) là hiệu hai lập phương.'),
  [T(r'\(x^3-8=x^3-2^3=(x-2)(x^2+2x+4)\).', r'\(x^3-8=x^3-2^3=(x-2)(x^2+2x+4)\).'),
   T(r'\(x=12\): \(10\cdot(144+24+4)=10\cdot172=1720\) (liters).', r'\(x=12\): \(10\cdot(144+24+4)=10\cdot172=1720\) (lít).')],
  T(r'\((x-2)(x^2+2x+4)\); 1720 liters.', r'\((x-2)(x^2+2x+4)\); cần 1720 lít nước.'))

_SETS = sp_g8.BANK(sp_g8.L8_GROUPS, start=1, seeds=(881, 882, 883))
practice = LEVEL_PRACTICE(sp_g8.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>\(x^3+8=(x+2)^3\).</b> Wrong: \(x^3+8=(x+2)(x^2-2x+4)\).', r'<b>\(x^3+8=(x+2)^3\).</b> Sai: \(x^3+8=(x+2)(x^2-2x+4)\).'),
 (r'<b>Wrong middle sign.</b> \(x^3-1=(x-1)(x^2+x+1)\), not \((x-1)(x^2-x+1)\).', r'<b>Sai dấu ở giữa.</b> \(x^3-1=(x-1)(x^2+x+1)\), không phải \((x-1)(x^2-x+1)\).'),
 (r'<b>Writing \(2AB\) instead of \(AB\).</b> The second factor is \(A^2\mp AB+B^2\), not a perfect square.', r'<b>Viết \(2AB\) thay cho \(AB\).</b> Thừa số thứ hai là \(A^2\mp AB+B^2\), không phải bình phương đúng.'),
 (r'<b>Not writing terms as cubes.</b> \(27x^3=(3x)^3\), so \(A=3x\), not \(A=27x\).', r'<b>Không viết hạng tử thành lập phương.</b> \(27x^3=(3x)^3\) nên \(A=3x\), không phải \(27x\).')]
summary = [
 (r'\(A^3+B^3=(A+B)(A^2-AB+B^2)\); \(A^3-B^3=(A-B)(A^2+AB+B^2)\).', r'\(A^3+B^3=(A+B)(A^2-AB+B^2)\); \(A^3-B^3=(A-B)(A^2+AB+B^2)\).'),
 (r'Seven identities: \((A\pm B)^2\), \(A^2-B^2\), \((A\pm B)^3\), \(A^3\pm B^3\).', r'Bảy hằng đẳng thức đáng nhớ: \((A\pm B)^2\), \(A^2-B^2\), \((A\pm B)^3\), \(A^3\pm B^3\).'),
 (r'\(a^3+b^3=(a+b)^3-3ab(a+b)\): use it when \(a+b\) and \(ab\) are known.', r'\(a^3+b^3=(a+b)^3-3ab(a+b)\): dùng khi biết \(a+b\) và \(ab\).'),
 (r'Key English: sum of two cubes, difference of two cubes.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[tổng hai lập phương]], [[hiệu hai lập phương]].')]
checks = [
 (r'I can expand \((A\pm B)(A^2\mp AB+B^2)\).', r'Em khai triển được \((A\pm B)(A^2\mp AB+B^2)\).'),
 (r'I can write \(A^3\pm B^3\) as a product.', r'Em viết được \(A^3\pm B^3\) dưới dạng tích.'),
 (r'I can use the seven identities to simplify and evaluate.', r'Em vận dụng được bảy hằng đẳng thức để rút gọn và tính giá trị.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Sum or Difference of Two Cubes', title_vi='Tổng và hiệu hai lập phương', topic=TOPIC,
       folder='identities', file='sum-difference-of-cubes', catalog_title_vi='Tổng và hiệu hai lập phương',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Identities: sum of two cubes and difference of two cubes; the seven identities.', level='Intermediate', minutes=45,
       description_vi='Bài 8 – Tổng hai lập phương, hiệu hai lập phương; bảng bảy hằng đẳng thức đáng nhớ.',
       tags_vi=['tổng hai lập phương', 'hiệu hai lập phương', 'bảy hằng đẳng thức'],
       prerequisites=['g8-identities-02'], tags=['sum of two cubes', 'difference of two cubes', 'identity'], order=80)
