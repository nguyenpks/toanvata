# -*- coding: utf-8 -*-
"""Nội dung bài g8-identities-02 = Toán 8 KNTT, Bài 7: Lập phương của một tổng. Lập phương của một hiệu – CHỈ NỘI DUNG.
Tiếng Anh chuyên ngành: TLTA Toán 8 (2026), Chapter 2 – Lesson 7, tr. 26–27 (cube, cube of a sum, cube of a difference)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_std import *
import sp_g8
from sp_g8 import Poly, M, L

LID = 'g8-identities-02'
CH = 'Hằng đẳng thức đáng nhớ và ứng dụng'
TOPIC = ('Algebraic Identities and Applications', CH)
ensure_vocab([
 ('g8-cube', 'cube', 'lập phương (lớp 8)', CH, 'The cube of 2x is 8x³.', ''),
 ('g8-cube-sum', 'cube of a sum', 'lập phương của một tổng', CH, '(A + B)³ is the cube of a sum.', ''),
 ('g8-cube-diff', 'cube of a difference', 'lập phương của một hiệu', CH, '(A − B)³ is the cube of a difference.', ''),
])
load_vocab()

# ---------- kiểm tra số liệu ----------
X = lambda c, a, b: (c, (a, b, 0))
c = lambda p: p * p * p
assert c(L(1, 2)) == Poly.of([X(1, 3, 0), X(6, 2, 0), X(12, 1, 0), X(8, 0, 0)])                                  # Ví dụ 1
assert c(L(2, -1, (1, 0, 0), (0, 1, 0))) == Poly.of([X(8, 3, 0), X(-12, 2, 1), X(6, 1, 2), X(-1, 0, 3)])          # Ví dụ 2
assert c(L(1, 3)) == Poly.of([X(1, 3, 0), X(9, 2, 0), X(27, 1, 0), X(27, 0, 0)]) and c(L(2, -1)) == Poly.of([X(8, 3, 0), X(-12, 2, 0), X(6, 1, 0), X(-1, 0, 0)])  # Ví dụ 3
assert c(L(1, -2)).at(22) == 8000                                                                                 # Ví dụ 4
assert c(L(1, 1)) - M(1, (3, 0, 0)) == Poly.of([X(3, 2, 0), X(3, 1, 0), X(1, 0, 0)]) and 3 * 100 + 30 + 1 == 331    # Ví dụ 5

meta = dict(level=('Intermediate', 'Trung bình'), time=('about 45 minutes', '45 phút'),
            before=('identities \\((A\\pm B)^2\\) (Lesson 6)', 'hằng đẳng thức \\((A\\pm B)^2\\) (Bài 6)'))
goals = [
 (r'state the identities \((A+B)^3\) and \((A-B)^3\);', r'phát biểu được các hằng đẳng thức [[lập phương của một tổng]] và [[lập phương của một hiệu]];'),
 (r'expand cubes and write polynomials as cubes;', r'khai triển và viết được đa thức dưới dạng [[lập phương|lập phương (lớp 8)]] của một tổng hay một hiệu;'),
 (r'use these identities to evaluate, simplify and solve problems.', r'vận dụng để tính giá trị, rút gọn biểu thức và giải bài toán thực tế.')]
vocab = [
 (r'<b>cube</b> – \(A^3\); the cube of \(2x\) is \(8x^3\).', r'[[Lập phương|lập phương (lớp 8)]] – \(A^3\); lập phương của \(2x\) là \(8x^3\).'),
 (r'<b>cube of a sum</b> – \((A+B)^3=A^3+3A^2B+3AB^2+B^3\).', r'[[Lập phương của một tổng]] – \((A+B)^3=A^3+3A^2B+3AB^2+B^3\).'),
 (r'<b>cube of a difference</b> – \((A-B)^3=A^3-3A^2B+3AB^2-B^3\).', r'[[Lập phương của một hiệu]] – \((A-B)^3=A^3-3A^2B+3AB^2-B^3\).'),
 (r'<b>identity / expand</b> – as in Lesson 6.', r'[[Hằng đẳng thức]] / [[khai triển]] – như ở Bài 6.')]
phrases = [
 (r'<b>Expand the following expressions.</b>', r'Khai triển các biểu thức sau.'),
 (r'<b>Write the following expressions as cubes.</b>', r'Viết các biểu thức sau dưới dạng lập phương.'),
 (r'<b>Write the expression as a cube and evaluate it for \(x=22\).</b>', r'Viết biểu thức dưới dạng lập phương rồi tính giá trị tại \(x=22\).'),
 (r'<b>Prove that the value of the expression is independent of \(x\).</b>', r'Chứng minh giá trị của biểu thức không phụ thuộc vào \(x\).'),
 (r'<b>\((A+B)^3\)</b> is read "the cube of a sum"; <b>\((A-B)^3\)</b> "the cube of a difference".', r'Cách đọc: \((A+B)^3\) – lập phương của một tổng; \((A-B)^3\) – lập phương của một hiệu.')]
review = (T(r'<b>Square of a sum (Lesson 6).</b> \((A+B)^2=A^2+2AB+B^2\).', r'<b>Bình phương của một tổng (Bài 6).</b> \((A+B)^2=A^2+2AB+B^2\).') +
          T(r'<b>Cubes.</b> \((2x)^3=8x^3\), \((-3)^3=-27\).', r'<b>Lập phương.</b> \((2x)^3=8x^3\), \((-3)^3=-27\).'))

theory = '<h3>7.1 %s</h3>' % TI('Cube of a sum', 'Lập phương của một tổng')
theory += BOX('blue', ('Identity', 'Hằng đẳng thức'),
  T(r'\((A+B)^3=A^3+3A^2B+3AB^2+B^3\).', r'\((A+B)^3=A^3+3A^2B+3AB^2+B^3\).'),
  T(r'Proof: \((A+B)^3=(A+B)(A+B)^2=(A+B)(A^2+2AB+B^2)=A^3+3A^2B+3AB^2+B^3\).', r'Chứng minh: \((A+B)^3=(A+B)(A+B)^2=(A+B)(A^2+2AB+B^2)=A^3+3A^2B+3AB^2+B^3\).'),
  T(r'Coefficients \(1,\ 3,\ 3,\ 1\); the power of \(A\) goes down \(3,2,1,0\), the power of \(B\) goes up \(0,1,2,3\).', r'Các hệ số là \(1,\ 3,\ 3,\ 1\); số mũ của \(A\) giảm dần \(3,2,1,0\), số mũ của \(B\) tăng dần \(0,1,2,3\).'))
theory += '<h3>7.2 %s</h3>' % TI('Cube of a difference', 'Lập phương của một hiệu')
theory += BOX('mint', ('Identity', 'Hằng đẳng thức'),
  T(r'\((A-B)^3=A^3-3A^2B+3AB^2-B^3\) (the signs alternate \(+,-,+,-\)).', r'\((A-B)^3=A^3-3A^2B+3AB^2-B^3\) (các dấu đan xen \(+,-,+,-\)).'),
  T(r'Example: \((x-2)^3=x^3-6x^2+12x-8\); conversely \(8x^3-12x^2+6x-1=(2x-1)^3\).', r'Ví dụ: \((x-2)^3=x^3-6x^2+12x-8\); ngược lại \(8x^3-12x^2+6x-1=(2x-1)^3\).'))
theory += BOX('yellow', ('Watch out!', 'Lưu ý'),
  T(r'\((A+B)^3\ne A^3+B^3\). Also \((A-B)^2=(B-A)^2\) but \((A-B)^3=-(B-A)^3\).', r'\((A+B)^3\ne A^3+B^3\). Ngoài ra \((A-B)^2=(B-A)^2\) nhưng \((A-B)^3=-(B-A)^3\).'))

examples = EXAMPLE(1, ('Remembering', 'Nhận biết'), ('Expand a cube of a sum', 'Khai triển lập phương của một tổng'),
  T(r'Expand \((x+2)^3\).', r'Khai triển \((x+2)^3\).'),
  ('Use \\((A+B)^3\\) with \\(A=x,\\ B=2\\).', 'Áp dụng \\((A+B)^3\\) với \\(A=x,\\ B=2\\).'),
  [T(r'\(x^3+3\cdot x^2\cdot2+3\cdot x\cdot2^2+2^3=x^3+6x^2+12x+8\).', r'\(x^3+3\cdot x^2\cdot2+3\cdot x\cdot2^2+2^3=x^3+6x^2+12x+8\).')],
  T(r'\(x^3+6x^2+12x+8\).', r'\(x^3+6x^2+12x+8\).'))
examples += EXAMPLE(2, ('Understanding', 'Thông hiểu'), ('Expand a cube of a difference', 'Khai triển lập phương của một hiệu'),
  T(r'Expand \((2x-y)^3\).', r'Khai triển \((2x-y)^3\).'),
  ('\\(A=2x,\\ B=y\\); be careful with the signs.', '\\(A=2x,\\ B=y\\); chú ý dấu.'),
  [T(r'\((2x)^3-3(2x)^2y+3\cdot2x\cdot y^2-y^3\).', r'\((2x)^3-3(2x)^2y+3\cdot2x\cdot y^2-y^3\).'),
   T(r'\(=8x^3-12x^2y+6xy^2-y^3\).', r'\(=8x^3-12x^2y+6xy^2-y^3\).')],
  T(r'\(8x^3-12x^2y+6xy^2-y^3\).', r'\(8x^3-12x^2y+6xy^2-y^3\).'))
examples += EXAMPLE(3, ('Understanding', 'Thông hiểu'), ('Write as a cube', 'Viết dưới dạng lập phương'),
  T(r'Write as a cube: a) \(x^3+9x^2+27x+27\); b) \(8x^3-12x^2+6x-1\).', r'Viết dưới dạng lập phương của một tổng hoặc một hiệu: a) \(x^3+9x^2+27x+27\); b) \(8x^3-12x^2+6x-1\).'),
  ('Find \\(A\\) from the first term and \\(B\\) from the last term, then check the middle terms.', 'Tìm \\(A\\) từ hạng tử đầu, \\(B\\) từ hạng tử cuối rồi kiểm tra hai hạng tử giữa.'),
  [T(r'a) \(A=x,\ B=3\): \(3A^2B=9x^2\), \(3AB^2=27x\) ✓, so \((x+3)^3\).', r'a) \(A=x,\ B=3\): \(3A^2B=9x^2\), \(3AB^2=27x\) ✓, nên bằng \((x+3)^3\).'),
   T(r'b) \(A=2x,\ B=1\): \(-3A^2B=-12x^2\), \(3AB^2=6x\) ✓, so \((2x-1)^3\).', r'b) \(A=2x,\ B=1\): \(-3A^2B=-12x^2\), \(3AB^2=6x\) ✓, nên bằng \((2x-1)^3\).')],
  T(r'\((x+3)^3\); \((2x-1)^3\).', r'\((x+3)^3\); \((2x-1)^3\).'))
examples += EXAMPLE(4, ('Basic application', 'Vận dụng thấp'), ('Evaluate quickly', 'Tính nhanh giá trị'),
  T(r'Find the value of \(A=x^3-6x^2+12x-8\) at \(x=22\).', r'Tính giá trị của biểu thức \(A=x^3-6x^2+12x-8\) tại \(x=22\).'),
  ('Write \\(A\\) as a cube first.', 'Viết \\(A\\) dưới dạng lập phương trước.'),
  [T(r'\(A=x^3-3\cdot x^2\cdot2+3\cdot x\cdot2^2-2^3=(x-2)^3\).', r'\(A=x^3-3\cdot x^2\cdot2+3\cdot x\cdot2^2-2^3=(x-2)^3\).'),
   T(r'\(x=22\): \(A=20^3=8000\).', r'\(x=22\): \(A=20^3=8000\).')],
  T(r'\(A=8000\).', r'\(A=8000\).'))
examples += EXAMPLE(5, ('Application', 'Vận dụng'), ('A bigger cube', 'Khối lập phương lớn hơn'),
  T(r'A cube has edge \(x\) cm. Each edge is increased by 1 cm. Write a polynomial for the increase of the volume, then find it for \(x=10\).', r'Một khối lập phương có cạnh \(x\) cm. Tăng mỗi cạnh thêm 1 cm. Viết đa thức biểu thị phần thể tích tăng thêm rồi tính khi \(x=10\).'),
  ('Increase = new volume − old volume.', 'Phần tăng = thể tích mới − thể tích cũ.'),
  [T(r'\((x+1)^3-x^3=x^3+3x^2+3x+1-x^3=3x^2+3x+1\).', r'\((x+1)^3-x^3=x^3+3x^2+3x+1-x^3=3x^2+3x+1\).'),
   T(r'\(x=10\): \(300+30+1=331\) (cm³).', r'\(x=10\): \(300+30+1=331\) (cm³).')],
  T(r'\(3x^2+3x+1\); \(331\) cm³.', r'\(3x^2+3x+1\); tăng \(331\) cm³.'))

_SETS = sp_g8.BANK(sp_g8.L7_GROUPS, start=1, seeds=(871, 872, 873))
practice = LEVEL_PRACTICE(sp_g8.ABCD_TITLES(), _SETS)

mistakes = [
 (r'<b>\((x+2)^3=x^3+8\).</b> Wrong: the terms \(6x^2\) and \(12x\) are missing.', r'<b>\((x+2)^3=x^3+8\).</b> Sai: thiếu hai hạng tử \(6x^2\) và \(12x\).'),
 (r'<b>Wrong signs in \((A-B)^3\).</b> They alternate: \(+,-,+,-\).', r'<b>Sai dấu trong \((A-B)^3\).</b> Các dấu đan xen: \(+,-,+,-\).'),
 (r'<b>Cubing only the variable.</b> \((2x)^3=8x^3\), not \(2x^3\).', r'<b>Chỉ lập phương phần biến.</b> \((2x)^3=8x^3\), không phải \(2x^3\).'),
 (r'<b>\((A-B)^3=(B-A)^3\).</b> Wrong: \((A-B)^3=-(B-A)^3\).', r'<b>\((A-B)^3=(B-A)^3\).</b> Sai: \((A-B)^3=-(B-A)^3\).')]
summary = [
 (r'\((A+B)^3=A^3+3A^2B+3AB^2+B^3\).', r'\((A+B)^3=A^3+3A^2B+3AB^2+B^3\).'),
 (r'\((A-B)^3=A^3-3A^2B+3AB^2-B^3\).', r'\((A-B)^3=A^3-3A^2B+3AB^2-B^3\).'),
 (r'Use them to expand, to write as a cube, to evaluate quickly and to simplify.', r'Dùng để khai triển, viết thành lập phương, tính nhanh và rút gọn.'),
 (r'Key English: cube, cube of a sum, cube of a difference.', r'Thuật ngữ cần nhớ (chạm vào để xem tiếng Anh): [[lập phương|lập phương (lớp 8)]], [[lập phương của một tổng]], [[lập phương của một hiệu]].')]
checks = [
 (r'I can expand \((A+B)^3\) and \((A-B)^3\).', r'Em khai triển được \((A+B)^3\) và \((A-B)^3\).'),
 (r'I can write a polynomial as a cube.', r'Em viết được đa thức dưới dạng lập phương.'),
 (r'I can use these identities to evaluate and simplify.', r'Em vận dụng được để tính giá trị và rút gọn biểu thức.'),
 STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Cube of a Sum or a Difference', title_vi='Lập phương của một tổng. Lập phương của một hiệu', topic=TOPIC,
       folder='identities', file='cube-of-sum-difference', catalog_title_vi='Lập phương của một tổng. Lập phương của một hiệu',
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='Identities: cube of a sum and cube of a difference.', level='Intermediate', minutes=45,
       description_vi='Bài 7 – Lập phương của một tổng, lập phương của một hiệu; khai triển, viết thành lập phương, tính nhanh.',
       tags_vi=['lập phương của một tổng', 'lập phương của một hiệu', 'hằng đẳng thức'],
       prerequisites=['g8-identities-01'], tags=['cube of a sum', 'cube of a difference', 'identity'], order=70)
