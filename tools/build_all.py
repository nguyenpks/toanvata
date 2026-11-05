# -*- coding: utf-8 -*-
"""Dựng lại TOÀN BỘ bài học của MỌI khối lớp theo mô hình config/model.json, rồi đồng bộ lessons.json.

    python tools/build_all.py            # dựng tất cả
    python tools/build_all.py 12         # chỉ dựng nội dung của lớp 12
    python tools/build_all.py --check    # chỉ kiểm tra mô hình, không ghi gì

Nội dung nằm trong content/grade<lớp>/*.py (mỗi tệp gọi lesson(...) cho một hoặc nhiều bài)."""
import os, sys, glob, runpy
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import mb_model

def main(argv):
    mb_model.check_model()
    if '--check' in argv:
        print('Mô hình hợp lệ.'); return
    grades = [a for a in argv if a.isdigit()]
    files = []
    for d in sorted(glob.glob(os.path.join(mb_model.ROOT, 'content', 'grade*')), key=lambda p: int(os.path.basename(p)[5:])):
        if grades and os.path.basename(d)[5:] not in grades: continue
        files += sorted(f for f in glob.glob(os.path.join(d, '*.py')) if not os.path.basename(f).startswith('_'))
    for f in files:
        print('==', os.path.relpath(f, mb_model.ROOT)); runpy.run_path(f)
    res = mb_model.sync_lessons_json()
    print('lessons.json: %d bài; dựng %d bài' % (len(res), len(mb_model.REGISTRY)))

if __name__ == '__main__':
    main(sys.argv[1:])
