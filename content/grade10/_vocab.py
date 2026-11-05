# -*- coding: utf-8 -*-
"""Từ vựng bổ sung cho các bài lớp 10 (idempotent, ghi vào data/vocab.json)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from mb_lib import *
S = 'Tập hợp và khoảng'; A = 'Đại số'
ensure_vocab([
 ('v-natural-numbers', 'natural numbers', 'số tự nhiên', S, 'The set of natural numbers includes 0.', '\\(\\mathbb{N}\\)'),
 ('v-integers', 'integers', 'số nguyên', S, 'Every integer is a rational number.', '\\(\\mathbb{Z}\\)'),
 ('v-rational-numbers', 'rational numbers', 'số hữu tỉ', S, 'One half is a rational number.', '\\(\\mathbb{Q}\\)'),
 ('v-real-numbers', 'real numbers', 'số thực', S, 'Every point on the number line is a real number.', '\\(\\mathbb{R}\\)'),
 ('v-number-line', 'number line', 'trục số', S, 'Show the interval on a number line.', ''),
 ('v-half-open-interval', 'half-open interval', 'nửa khoảng', S, '[1, 3) is a half-open interval.', ''),
 ('v-listing-method', 'listing method', 'liệt kê', S, 'Write the set by the listing method.', ''),
 ('v-set-builder', 'set-builder notation', 'nêu tính chất đặc trưng', S, 'Use set-builder notation to describe the set.', '\\(\\{x\\mid\\dots\\}\\)'),
 ('v-belongs-to', 'belongs to', 'thuộc', S, 'The number 2 belongs to the set A.', '\\(\\in\\)'),
 ('v-venn-diagram', 'Venn diagram', 'biểu đồ Venn', S, 'Draw a Venn diagram of the two sets.', ''),
 ('v-number-of-elements', 'number of elements', 'số phần tử', S, 'Find the number of elements of A.', '\\(n(A)\\)'),
 ('v-variable', 'variable', 'biến số', A, 'The letter x is a variable.', ''),
 ('v-constant', 'constant', 'hằng số', A, 'In 2x + 5, the number 5 is a constant.', ''),
 ('v-algebraic-expression', 'algebraic expression', 'biểu thức đại số', A, 'Simplify the algebraic expression.', ''),
 ('v-term', 'term', 'hạng tử', A, 'The expression 3x + 5 has two terms.', ''),
 ('v-coefficient', 'coefficient', 'hệ số', A, 'The coefficient of x in 3x is 3.', ''),
 ('v-like-terms', 'like terms', 'các hạng tử đồng dạng', A, 'Combine like terms.', ''),
 ('v-exponent', 'exponent', 'số mũ', A, 'In x^3, the exponent is 3.', '\\(x^n\\)'),
 ('v-base', 'base', 'cơ số', A, 'In 2^5, the base is 2.', ''),
 ('v-power', 'power', 'lũy thừa', A, 'x^3 is the third power of x.', ''),
 ('v-simplify', 'simplify', 'rút gọn', A, 'Simplify the expression.', ''),
 ('v-evaluate', 'evaluate', 'tính giá trị', A, 'Evaluate the expression when x = 3.', ''),
 ('v-substitute', 'substitute', 'thay vào', A, 'Substitute x = 2 into the expression.', ''),
 ('v-expand', 'expand', 'khai triển', A, 'Expand the brackets.', ''),
 ('v-distributive-property', 'distributive property', 'tính chất phân phối', A, 'Use the distributive property.', '\\(a(b+c)=ab+ac\\)'),
 ('v-degree', 'degree', 'bậc', A, 'The degree of 4x^2 is 2.', ''),
 ('v-order-of-operations', 'order of operations', 'thứ tự thực hiện các phép tính', A, 'Follow the order of operations.', ''),
])
load_vocab()
