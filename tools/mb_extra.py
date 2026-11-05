# -*- coding: utf-8 -*-
"""Tiện ích bổ sung dùng chung cho các khối lớp (bảng, hình Venn, sắp xếp lessons.json). Không thay đổi mb_lib."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mb_lib import *

def TBL(head, rows):
    """Bảng chuẩn: head = danh sách ô tiêu đề (HTML), rows = danh sách hàng (mỗi ô là HTML)."""
    h = '<thead><tr>' + ''.join('<th>%s</th>' % c for c in head) + '</tr></thead>'
    b = '<tbody>' + ''.join('<tr>' + ''.join('<td>%s</td>' % c for c in r) + '</tr>' for r in rows) + '</tbody>'
    return '<div class="mbl-tablewrap"><table class="mbl-table">%s%s</table></div>' % (h, b)

def FIGR(svg, cap_en, cap_vi):
    """Hình đã có sẵn aria-label (không thêm nhãn lần nữa)."""
    return '<figure class="mbl-fig">%s<figcaption>%s</figcaption></figure>' % (svg, TI(cap_en, cap_vi))

def venn2(a_only, both, b_only, outside=None, la='A', lb='B', alt='Venn diagram of two sets'):
    """Hình Venn hai tập; các số (hoặc dấu ?) ghi vào từng vùng."""
    o = ['<svg viewBox="0 0 360 200" role="img" aria-label="%s" xmlns="http://www.w3.org/2000/svg" font-family="Segoe UI,Arial,sans-serif">' % alt,
         '<rect x="8" y="8" width="344" height="184" rx="10" fill="#ffffff" stroke="#123428" stroke-width="1.5"/>',
         '<circle cx="140" cy="102" r="66" fill="#d5f3e4" fill-opacity=".85" stroke="#046b4d" stroke-width="2"/>',
         '<circle cx="220" cy="102" r="66" fill="#86e0bd" fill-opacity=".55" stroke="#046b4d" stroke-width="2"/>',
         '<text x="92" y="42" font-size="17" font-style="italic" fill="#123428">%s</text>' % la,
         '<text x="262" y="42" font-size="17" font-style="italic" fill="#123428">%s</text>' % lb]
    for x, v in ((102, a_only), (180, both), (258, b_only)):
        o.append('<text x="%d" y="109" font-size="20" font-weight="700" text-anchor="middle" fill="#123428">%s</text>' % (x, v))
    if outside is not None:
        o.append('<text x="334" y="182" font-size="18" font-weight="700" text-anchor="end" fill="#123428">%s</text>' % outside)
    return ''.join(o) + '</svg>'

def reorder(grade, order):
    """Sắp xếp lại các bài của một lớp trong lessons.json theo danh sách id (bài không có trong danh sách xếp cuối)."""
    p = os.path.join(ROOT, 'lessons.json'); d = json.load(open(p, encoding='utf-8'))
    g = sorted([x for x in d if x['grade'] == grade], key=lambda x: order.index(x['id']) if x['id'] in order else 999)
    first = next(i for i, x in enumerate(d) if x['grade'] == grade)
    d = [x for x in d if x['grade'] != grade]; d[first:first] = g
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
