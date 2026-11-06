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
    """Hình Venn hai tập vẽ bằng TikZ (XeLaTeX → SVG); các số (hoặc dấu ?) ghi vào từng vùng."""
    from mb_pgf import venn_svg, svg_img
    return svg_img(venn_svg(a_only, both, b_only, outside, la, lb), alt, 440)

def reorder(grade, order):
    """Sắp xếp lại các bài của một lớp trong lessons.json theo danh sách id (bài không có trong danh sách xếp cuối)."""
    p = os.path.join(ROOT, 'lessons.json'); d = json.load(open(p, encoding='utf-8'))
    g = sorted([x for x in d if x['grade'] == grade], key=lambda x: order.index(x['id']) if x['id'] in order else 999)
    first = next(i for i, x in enumerate(d) if x['grade'] == grade)
    d = [x for x in d if x['grade'] != grade]; d[first:first] = g
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
