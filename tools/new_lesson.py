# -*- coding: utf-8 -*-
"""Tạo tệp nội dung trống cho một bài mới ở bất kỳ lớp nào.
    python tools/new_lesson.py g5-fractions-01 "Fractions" "Phân số" "Number Sense" "Số học"
Tham số: mã bài, tên EN, tên VI, [chủ đề EN], [chủ đề VI]. Kết quả: content/grade<lớp>/<mã bài>.py"""
import os, sys, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
if len(sys.argv) < 4:
    sys.exit(__doc__)
lid, en, vi = sys.argv[1:4]
t_en = sys.argv[4] if len(sys.argv) > 4 else 'Topic'; t_vi = sys.argv[5] if len(sys.argv) > 5 else 'Chủ đề'
m = re.match(r'^g(\d{1,2})-', lid)
if not m or not 1 <= int(m.group(1)) <= 12: sys.exit('Mã bài phải dạng g<lớp 1-12>-<chủ đề>-<số>, ví dụ g5-fractions-01')
g = int(m.group(1)); slug = lambda s: re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
s = open(os.path.join(ROOT, 'content', '_TEMPLATE.py'), encoding='utf-8').read()
s = s.replace("LID = 'g5-example-01'", "LID = '%s'" % lid).replace("('Example Topic', 'Chủ đề ví dụ')", "(%r, %r)" % (t_en, t_vi))
s = s.replace("'Example Topic'", repr(t_en)).replace("title_en='Example Lesson', title_vi='Bài ví dụ'", "title_en=%r, title_vi=%r" % (en, vi))
s = s.replace("folder='example-topic', file='example-lesson',", "folder=%r, file=%r," % (slug(t_en), slug(en))).replace('lessons/grade5/example-topic/example-lesson.html', 'lessons/grade%d/%s/%s.html' % (g, slug(t_en), slug(en)))
d = os.path.join(ROOT, 'content', 'grade%d' % g); os.makedirs(d, exist_ok=True)
out = os.path.join(d, lid + '.py')
if os.path.exists(out): sys.exit('Đã có: ' + out)
open(out, 'w', encoding='utf-8').write(s); print('Đã tạo', os.path.relpath(out, ROOT))
