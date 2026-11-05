# -*- coding: utf-8 -*-
"""Lớp tương thích: cú pháp build(...)/ENTRY(...) cũ của các bài lớp 12, nay chuyển hết sang mb_model.lesson().
KHÔNG còn bố cục, số mục, số lớp hay đăng ký lessons.json nào ở đây: tất cả nằm ở config/model.json + mb_model.py.
Bài mới nên dùng thẳng `lesson(id=..., ...)` (xem content/_TEMPLATE.py)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mb_model import *

def ENTRY(lid, title, desc, level, mins, pre, path, tags, order=0, grade=None):
    """Thông tin danh mục của bài (lớp và chủ đề được suy ra, không khai báo ở đây)."""
    return {"id": lid, "title": title, "description": desc, "level": level, "estimatedMinutes": mins,
            "prerequisites": pre, "path": path, "tags": tags, "order": order}

def build(lid, en_title, vi_title, topic, meta, goals, vocab, phrases, review, theory, examples, practice,
          mistakes, summary, checks, outpath, entry, grade=None):
    if grade is not None and grade != grade_of(lid): raise ValueError("grade không khớp mã bài " + lid)
    return lesson(id=lid, title_en=en_title, title_vi=vi_title, topic=topic, meta=meta, goals=goals, vocab=vocab,
                  phrases=phrases, review=review, theory=theory, examples=examples, practice=practice,
                  mistakes=mistakes, summary=summary, checks=checks, path=outpath,
                  description=entry['description'], level=entry['level'], minutes=entry['estimatedMinutes'],
                  prerequisites=entry['prerequisites'], tags=entry['tags'], order=entry.get('order', 0))

def STD_SUMMARY_CHECK_EN():
    return ('I understand the English instructions in this lesson.', 'Em hiểu các yêu cầu bằng tiếng Anh trong bài này.')
