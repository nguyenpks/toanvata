# -*- coding: utf-8 -*-
"""MẪU nội dung một bài học (dùng cho BẤT KỲ lớp nào từ 1 đến 12).
Chỉ nhập NỘI DUNG. Đừng viết số mục, tên mục, số lớp, khung trang: tất cả do config/model.json quyết định.
Lớp được suy ra từ mã bài (g5-... = lớp 5). Tạo bài mới bằng:  python tools/new_lesson.py g5-fractions-01 "Fractions" "Phân số"

Quy ước viết:
  - Mỗi đoạn là một cặp (tiếng Anh, tiếng Việt):  T('English text', 'Văn bản tiếng Việt')
  - Thuật ngữ trong tiếng Việt đặt trong [[...]]; thuật ngữ phải có trong data/vocab.json (khai báo bằng ensure_vocab).
  - Công thức:  \\( ... \\) trong dòng,  M(r'...') riêng dòng.
  - Tiêu đề phụ trong lý thuyết viết '<h3>5.1 ...' – số đầu sẽ tự đổi theo số mục thật trong mô hình.
  - Mục nào để trống (''/[]) và không bắt buộc thì bị bỏ qua; mục bắt buộc thiếu thì báo lỗi.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tools'))
from mb_std import *

LID = 'g5-example-01'                      # g<lớp>-<chủ đề ngắn>-<số thứ tự>
TOPIC = ('Example Topic', 'Chủ đề ví dụ')  # (tên tiếng Anh, tên tiếng Việt) – dùng làm "category" trong lessons.json

ensure_vocab([
    # (id, từ tiếng Anh, tiếng Việt, chủ đề, câu ví dụ tiếng Anh, ký hiệu hoặc '')
    # ('v-example', 'example', 'ví dụ', 'Example Topic', 'This is an example.', ''),
])

meta = dict(level=('Beginner', 'Cơ bản'), time=('about 30 minutes', 'khoảng 30 phút'), before=('nothing special', 'không cần gì đặc biệt'))
goals = [('understand the idea of the lesson;', 'hiểu ý chính của bài học;')]
vocab = [('<b>example</b> – a sample to show an idea.', 'Một mẫu minh họa cho một ý.')]
phrases = [('Look at the example.', 'Hãy nhìn ví dụ.')]
review = T('Remember what you learned before.', 'Hãy nhớ lại điều đã học.')
theory = '<h3>5.1 %s</h3>' % TI('Main idea', 'Ý chính') + T('Write the theory here.', 'Viết lý thuyết ở đây.')
examples = EXAMPLE(1, ('Basic', 'Cơ bản'), ('A first example', 'Ví dụ đầu tiên'),
                   T('Compute \\(1+1\\).', 'Tính \\(1+1\\).'),
                   ('Add the two numbers.', 'Cộng hai số.'),
                   [T('Add 1 and 1.', 'Cộng 1 với 1.')], '\\(2\\)')
# Thêm ví dụ: examples += EXAMPLE(2, ...) – mức ('Basic'|'Intermediate'|'Advanced', ...)
practice = [(('A. Multiple Choice', 'A. Trắc nghiệm'), [MCQ(1, ('1 + 1 = ?', '1 + 1 = ?'), ['1', '2', '3', '4'], 'b', ('1 + 1 = 2.', '1 + 1 = 2.'))])]
mistakes = [('<b>Rushing.</b> Read the question twice.', '<b>Làm vội.</b> Hãy đọc đề hai lần.')]
summary = [('This lesson explained one main idea.', 'Bài học giải thích một ý chính.')]
checks = [('I can explain the main idea.', 'Em giải thích được ý chính.'), STD_SUMMARY_CHECK_EN()]

lesson(id=LID, title_en='Example Lesson', title_vi='Bài ví dụ', topic=TOPIC,
       folder='example-topic', file='example-lesson',                 # -> lessons/grade5/example-topic/example-lesson.html
       meta=meta, goals=goals, vocab=vocab, phrases=phrases, review=review, theory=theory, examples=examples,
       practice=practice, mistakes=mistakes, summary=summary, checks=checks,
       description='One-sentence description in English.', level='Beginner', minutes=30,
       description_vi='Mô tả một câu bằng tiếng Việt (hiện trong danh sách bài).', tags_vi=['ví dụ'],
       prerequisites=[], tags=['example'], order=10)               # order: thứ tự bài trong lớp (10, 20, 30...)
