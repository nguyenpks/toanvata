# -*- coding: utf-8 -*-
"""Nội dung bài g8-identities-04 = Toán 8 KNTT, Bài 9: Phân tích đa thức thành nhân tử – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 8 (2026), Chapter 2 – Lesson 9, tr. 30–31 (factor, common factor, group terms).
Tách hạng tử (x² + 5x + 6, TLTA Exercise 5) chỉ dùng ở mức Vận dụng, có gợi ý (D7 trong DAN-Y-LOP-8.md)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g8
from sp_g8 import Poly, M, L

LID = 'g8-identities-04'
CH = 'Hằng đẳng thức đáng nhớ và ứng dụng'
TOPIC = ('Algebraic Identities and Applications', CH)
ensure_vocab([
 ('g8-factor-poly', 'factor (a polynomial)', 'phân tích đa thức thành nhân tử (lớp 8)', CH, 'Factor the polynomial x² − 3x: x² − 3x = x(x − 3).', ''),
 ('g8-factor-out', 'take out a common factor', 'đặt nhân tử chung (lớp 8)', CH, 'Take out the common factor 3xy.', ''),
 ('g8-group-terms', 'group terms', 'nhóm hạng tử', CH, 'We factor the polynomial by grouping terms.', ''),
])
load_vocab()

# ---------- kiểm tra số liệu ----------
X = lambda c, a, b: (c, (a, b, 0))
assert M(3, (1, 1, 0)) * Poly.of([X(2, 1, 0), X(-3, 0, 1)]) == Poly.of([X(6, 2, 1), X(-9, 1, 2)])                  # Ví dụ 1
assert L(1, -5) * L(1, -5) == Poly.of([X(1, 2, 0), X(-10, 1, 0), X(25, 0, 0)]) and L(3, -4) * L(3, 4) == Poly.of([X(9, 2, 0), X(-16, 0, 0)])
assert L(2, 1) * Poly.of([X(4, 2, 0), X(-2, 1, 0), X(1, 0, 0)]) == Poly.of([X(8, 3, 0), X(1, 0, 0)])             # Ví dụ 2
assert Poly.of([X(1, 1, 0), X(-1, 0, 1)]) * L(1, 3) == Poly.of([X(1, 2, 0), X(-1, 1, 1), X(3, 1, 0), X(-3, 0, 1)])  # Ví dụ 3
assert all(2 * t * t - 8 * t == 0 for t in (0, 4)) and all(t ** 3 - 9 * t == 0 for t in (0, 3, -3))               # Ví dụ 4
assert L(1, 2) * L(1, 3) == Poly.of([X(1, 2, 0), X(5, 1, 0), X(6, 0, 0)]) and 10 * 11 == 110                       # Ví dụ 5

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 60 minutes', '60 phút'),
            before=('the seven identities (Lessons 6–8)', 'bảy hằng đẳng thức đáng nhớ (Bài 6–8)'))
goals = [
 (r'understand what it means to factor a polynomial;', r'hiểu thế nào là [[phân tích đa thức thành nhân tử|phân tích đa thức thành nhân tử (lớp 8)]];'),
 (r'factor by taking out a common factor, by using identities and by grouping terms;', r'phân tích được đa thức thành nhân tử bằng cách [[đặt nhân tử chung|đặt nhân tử chung (lớp 8)]], dùng hằng đẳng thức, [[nhóm hạng tử]];'),
 (r'use factoring to find \(x\) and to calculate quickly.', r'vận dụng để tìm \(x\) và tính nhanh.')]
vocab = [
 (r'<b>factor (a polynomial)</b> – write it as a product of polynomials: \(x^2-3x=x(x-3)\).', r'[[Phân tích đa thức thành nhân tử|phân tích đa thức thành nhân tử (lớp 8)]] – viết đa thức thành một tích của những đa thức: \(x^2-3x=x(x-3)\).'),
 (r'<b>common factor</b> – a factor that appears in every term: \(3xy\) in \(6x^2y-9xy^2\).', r'[[Nhân tử chung]] – nhân tử có mặt trong mọi hạng tử: \(3xy\) trong \(6x^2y-9xy^2\).'),
 (r'<b>take out a common factor</b> – \(AB+AC=A(B+C)\).', r'[[Đặt nhân tử chung|đặt nhân tử chung (lớp 8)]] – \(AB+AC=A(B+C)\).'),
 (r'<b>group terms</b> – put terms in brackets so that a common factor appears.', r'[[Nhóm hạng tử]] – nhóm các hạng tử thích hợp để làm xuất hiện nhân tử chung.'),
 (r'<b>identity / term / polynomial</b> – as in Lessons 2 and 6.', r'[[Hằng đẳng thức]] / [[hạng tử]] / [[đa thức|đa thức (lớp 8)]] – như ở Bài 2, 6.')]
phrases = [
 (r'<b>Factor the following polynomials into a product.</b>', r'Phân tích các đa thức sau thành nhân tử.'),
 (r'<b>Find the common factor of the terms.</b>', r'Tìm nhân tử chung của các hạng tử.'),
 (r'<b>We factor the polynomial by grouping terms.</b>', r'Ta phân tích đa thức thành nhân tử bằng cách nhóm hạng tử.'),
 (r'<b>Which method / identity do we use to factor the polynomial?</b>', r'Dùng phương pháp / hằng đẳng thức nào để phân tích đa thức?'),
 (r'<b>Which terms can be grouped? By grouping …, we can find the common factor.</b>', r'Những hạng tử nào có thể nhóm với nhau? Nhóm … thì xuất hiện nhân tử chung.'),
 (r'<b>Find the value of \(x\), given that…</b>', r'Tìm \(x\), biết…')]
review = (T(r'<b>Distributive property.</b> \(A(B+C)=AB+AC\); read from right to left: \(AB+AC=A(B+C)\).', r'<b>Tính chất phân phối.</b> \(A(B+C)=AB+AC\); đọc từ phải sang trái: \(AB+AC=A(B+C)\).') +
          T(r'<b>Product equal to zero.</b> \(A\cdot B=0\) when \(A=0\) or \(B=0\).', r'<b>Tích bằng 0.</b> \(A\cdot B=0\) khi \(A=0\) hoặc \(B=0\).'))

theory = '<h3>9.1 %s</h3>' % TI('What is factoring?', 'Thế nào là phân tích đa thức thành nhân tử?')
theory += BOX('blue', ('Definition', 'Định nghĩa'),
  T(r'To <b>factor</b> a polynomial is to write it as a product of polynomials.', r'[[Phân tích đa thức thành nhân tử|phân tích đa thức thành nhân tử (lớp 8)]] (hay thừa số) là biến đổi đa thức đó thành một tích của những đa thức.'),
  T(r'Example: \(x^2-9=(x-3)(x+3)\); \(5x^2+10x=5x(x+2)\).', r'Ví dụ: \(x^2-9=(x-3)(x+3)\); \(5x^2+10x=5x(x+2)\).'))
theory += '<h3>9.2 %s</h3>' % TI('Three methods', 'Ba phương pháp')
theory += BOX('mint', ('1. Taking out a common factor', '1. Đặt nhân tử chung'),
  T(r'Find the greatest common factor (GCF of the coefficients, lowest power of each common variable): \(6x^2y-9xy^2=3xy(2x-3y)\).', r'Tìm nhân tử chung (ƯCLN của các hệ số, mỗi biến chung lấy số mũ nhỏ nhất): \(6x^2y-9xy^2=3xy(2x-3y)\).'),
  T(r'Sometimes change signs first: \(x(x-y)+2(y-x)=x(x-y)-2(x-y)=(x-y)(x-2)\).', r'Đôi khi cần đổi dấu: \(x(x-y)+2(y-x)=x(x-y)-2(x-y)=(x-y)(x-2)\).'))
theory += BOX('blue', ('2. Using identities', '2. Dùng hằng đẳng thức'),
  T(r'\(x^2-10x+25=(x-5)^2\); \(9x^2-16=(3x-4)(3x+4)\); \(8x^3+1=(2x+1)(4x^2-2x+1)\).', r'\(x^2-10x+25=(x-5)^2\); \(9x^2-16=(3x-4)(3x+4)\); \(8x^3+1=(2x+1)(4x^2-2x+1)\).'))
theory += BOX('mint', ('3. Grouping terms', '3. Nhóm hạng tử'),
  T(r'Group the terms so that each group has a common factor, then take out the common bracket: \(x^2-xy+3x-3y=x(x-y)+3(x-y)=(x-y)(x+3)\).', r'Nhóm các hạng tử để mỗi nhóm có nhân tử chung, rồi đặt nhân tử chung là cả ngoặc: \(x^2-xy+3x-3y=x(x-y)+3(x-y)=(x-y)(x+3)\).'))
theory += BOX('yellow', ('Tips', 'Lưu ý'),
  T(r'Usually: first take out a common factor, then look for an identity, then try grouping. Factor completely: \(2x^3-8x=2x(x^2-4)=2x(x-2)(x+2)\).', r'Thường làm theo thứ tự: đặt nhân tử chung → dùng hằng đẳng thức → nhóm hạng tử. Phân tích đến cùng: \(2x^3-8x=2x(x^2-4)=2x(x-2)(x+2)\).'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Common factor', 'Đặt nhân tử chung'),
  T(r'Factor \(6x^2y-9xy^2\).', r'Phân tích đa thức \(6x^2y-9xy^2\) thành nhân tử.'),
  ('GCF of 6 and 9 is 3; both terms contain \\(x\\) and \\(y\\).', 'ƯCLN(6, 9) = 3; cả hai hạng tử đều chứa \\(x\\) và \\(y\\).'),
  [T(r'\(6x^2y-9xy^2=3xy\cdot2x-3xy\cdot3y=3xy(2x-3y)\).', r'\(6x^2y-9xy^2=3xy\cdot2x-3xy\cdot3y=3xy(2x-3y)\).')],
  T(r'\(3xy(2x-3y)\).', r'\(3xy(2x-3y)\).'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Using identities', 'Dùng hằng đẳng thức'),
  T(r'Factor: a) \(x^2-10x+25\); b) \(9x^2-16\); c) \(8x^3+1\).', r'Phân tích thành nhân tử: a) \(x^2-10x+25\); b) \(9x^2-16\); c) \(8x^3+1\).'),
  ('Recognize the identity in each case.', 'Nhận ra hằng đẳng thức trong mỗi trường hợp.'),
  [T(r'a) \(x^2-2\cdot x\cdot5+5^2=(x-5)^2\).', r'a) \(x^2-2\cdot x\cdot5+5^2=(x-5)^2\).'),
   T(r'b) \((3x)^2-4^2=(3x-4)(3x+4)\).', r'b) \((3x)^2-4^2=(3x-4)(3x+4)\).'),
   T(r'c) \((2x)^3+1^3=(2x+1)(4x^2-2x+1)\).', r'c) \((2x)^3+1^3=(2x+1)(4x^2-2x+1)\).')],
  T(r'\((x-5)^2\); \((3x-4)(3x+4)\); \((2x+1)(4x^2-2x+1)\).', r'\((x-5)^2\); \((3x-4)(3x+4)\); \((2x+1)(4x^2-2x+1)\).'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('Grouping terms', 'Nhóm hạng tử'),
  T(r'Factor \(x^2-xy+3x-3y\).', r'Phân tích đa thức \(x^2-xy+3x-3y\) thành nhân tử.'),
  ('Group the first two terms and the last two terms.', 'Nhóm hai hạng tử đầu và hai hạng tử cuối.'),
  [T(r'\((x^2-xy)+(3x-3y)=x(x-y)+3(x-y)\).', r'\((x^2-xy)+(3x-3y)=x(x-y)+3(x-y)\).'),
   T(r'\(=(x-y)(x+3)\).', r'\(=(x-y)(x+3)\).')],
  T(r'\((x-y)(x+3)\).', r'\((x-y)(x+3)\).'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Find x', 'Tìm x'),
  T(r'Find \(x\): a) \(2x^2-8x=0\); b) \(x^3-9x=0\).', r'Tìm \(x\), biết: a) \(2x^2-8x=0\); b) \(x^3-9x=0\).'),
  ('Factor the left side, then use \\(A\\cdot B=0\\).', 'Phân tích vế trái thành nhân tử rồi dùng \\(A\\cdot B=0\\).'),
  [T(r'a) \(2x(x-4)=0\Rightarrow x=0\) or \(x=4\).', r'a) \(2x(x-4)=0\Rightarrow x=0\) hoặc \(x=4\).'),
   T(r'b) \(x(x^2-9)=x(x-3)(x+3)=0\Rightarrow x\in\{0;\ 3;\ -3\}\).', r'b) \(x(x^2-9)=x(x-3)(x+3)=0\Rightarrow x\in\{0;\ 3;\ -3\}\).')],
  T(r'a) \(x\in\{0;\ 4\}\); b) \(x\in\{0;\ 3;\ -3\}\).', r'a) \(x\in\{0;\ 4\}\); b) \(x\in\{0;\ 3;\ -3\}\).'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('Sides of a rectangle', 'Kích thước hình chữ nhật'),
  T(r'A rectangle has area \(x^2+5x+6\) (m²). Factor this polynomial to find the sides of the rectangle (hint: \(5x=2x+3x\)). Find the sides and the area when \(x=8\).', r'Một hình chữ nhật có diện tích \(x^2+5x+6\) (m²). Hãy phân tích đa thức này thành nhân tử để tìm hai cạnh của hình chữ nhật (gợi ý: \(5x=2x+3x\)). Tính các cạnh và diện tích khi \(x=8\).'),
  ('Split the middle term, then group.', 'Tách hạng tử giữa rồi nhóm.'),
  [T(r'\(x^2+2x+3x+6=x(x+2)+3(x+2)=(x+2)(x+3)\).', r'\(x^2+2x+3x+6=x(x+2)+3(x+2)=(x+2)(x+3)\).'),
   T(r'Sides \((x+2)\) m and \((x+3)\) m; for \(x=8\): \(10\) m and \(11\) m, area \(110\) m².', r'Hai cạnh là \((x+2)\) m và \((x+3)\) m; khi \(x=8\): \(10\) m và \(11\) m, diện tích \(110\) m².')],
  T(r'\((x+2)(x+3)\); 10 m, 11 m; 110 m².', r'\((x+2)(x+3)\); 10 m và 11 m; 110 m².'))

_SETS = sp_g8.BANK(sp_g8.L9_GROUPS, start=1, seeds=(891, 892, 893))
practice = LEVEL_PRACTICE(sp_g8.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>Not the greatest common factor.</b> \(6x^2y-9xy^2=3x(2xy-3y^2)\) is not finished: take out \(3xy\).', r'<b>Chưa lấy hết nhân tử chung.</b> \(6x^2y-9xy^2=3x(2xy-3y^2)\) chưa xong: phải đặt \(3xy\).'),
 (r'<b>Losing a term.</b> \(3x^2+3x=3x(x+1)\), not \(3x\cdot x\).', r'<b>Mất hạng tử.</b> \(3x^2+3x=3x(x+1)\), không phải \(3x\cdot x\).'),
 (r'<b>\(x^2+4=(x+2)^2\).</b> Wrong: a sum of two squares is not \((x+2)^2\).', r'<b>\(x^2+4=(x+2)^2\).</b> Sai: tổng hai bình phương không bằng \((x+2)^2\).'),
 (r'<b>Sign errors when grouping.</b> \(x^2-xy-3x+3y=x(x-y)-3(x-y)\).', r'<b>Sai dấu khi nhóm.</b> \(x^2-xy-3x+3y=x(x-y)-3(x-y)\).'),
 (r'<b>Dividing by \(x\).</b> From \(x^2=4x\) do not divide by \(x\); write \(x(x-4)=0\), so \(x=0\) or \(x=4\).', r'<b>Chia cả hai vế cho \(x\).</b> Từ \(x^2=4x\) không được chia cho \(x\); viết \(x(x-4)=0\) nên \(x=0\) hoặc \(x=4\).')]
summary = [
 (r'Factoring = writing a polynomial as a product.', r'Phân tích thành nhân tử = viết đa thức thành tích.'),
 (r'Methods: take out a common factor; use identities; group terms (and combine them).', r'Các phương pháp: đặt nhân tử chung; dùng hằng đẳng thức; nhóm hạng tử (và phối hợp chúng).'),
 (r'Application: \(A\cdot B=0\Rightarrow A=0\) or \(B=0\); quick calculation.', r'Ứng dụng: \(A\cdot B=0\Rightarrow A=0\) hoặc \(B=0\); tính nhanh.'),
 (r'Key English: factor, common factor, take out a common factor, group terms.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[phân tích đa thức thành nhân tử|phân tích đa thức thành nhân tử (lớp 8)]], [[nhân tử chung]], [[đặt nhân tử chung|đặt nhân tử chung (lớp 8)]], [[nhóm hạng tử]].')]
checks = [
 (r'I can take out the greatest common factor.', r'Em đặt được nhân tử chung lớn nhất.'),
 (r'I can factor using identities.', r'Em phân tích được đa thức bằng hằng đẳng thức.'),
 (r'I can factor by grouping terms.', r'Em phân tích được đa thức bằng cách nhóm hạng tử.'),
 (r'I can use factoring to find \(x\).', r'Em dùng được phân tích thành nhân tử để tìm \(x\).'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Factoring Polynomials', title_vi='Phân tích đa thức thành nhân tử', topic=TOPIC,
       folder='identities', file='factoring-polynomials', catalog_title_vi='Phân tích đa thức thành nhân tử',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Factoring by a common factor, by identities and by grouping terms.', level='Intermediate', minutes=60,
       description_vi='Bài 9 – Phân tích đa thức thành nhân tử: đặt nhân tử chung, dùng hằng đẳng thức, nhóm hạng tử; tìm x.',
       tags_vi=['phân tích đa thức thành nhân tử', 'nhân tử chung', 'nhóm hạng tử'],
       prerequisites=['g8-identities-03'], tags=['factor', 'common factor', 'grouping'], order=90)
