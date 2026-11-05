# -*- coding: utf-8 -*-
"""Ký hiệu hình học theo SGK Toán Việt Nam (Kết nối tri thức).  python tests/test-geometry-notation.py
Trong công thức \\( \\) của mọi bài: vectơ \\overrightarrow{AB} (không \\vec), góc \\widehat{ABC} (không \\angle), song song \\parallel, vuông góc \\perp,
độ \\(...^\\circ\\); không dùng \\overline{AB} cho đoạn thẳng, \\hat{} cho góc ba chữ cái, '//' cho song song, \\bot, \\measuredangle."""
import re, glob, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
RULES = [(r'\\vec\s*\{', 'dùng \\overrightarrow{AB} cho vectơ (SGK), không dùng \\vec'),
         (r'\\angle\b', 'dùng \\widehat{ABC} cho góc (SGK), không dùng \\angle'),
         (r'\\hat\s*\{[A-Z]{3}\}', 'góc ba chữ cái viết \\widehat{ABC}, không dùng \\hat'),
         (r'\\measuredangle', 'không dùng \\measuredangle'), (r'\\bot\b', 'dùng \\perp cho vuông góc'),
         (r'\\overline\s*\{[A-Z]{2}\}', 'đoạn thẳng viết AB, không gạch ngang đầu (\\overline{AB} dành cho số phức/trung bình)'),
         (r'(?<!\\)[A-Za-z]{1,2}\s*//\s*[A-Za-z]{1,2}', 'song song viết \\parallel, không dùng //')]
bad = 0; total = 0
for f in sorted(glob.glob('lessons/**/*.html', recursive=True)):
    h = re.sub(r'<script.*?</script>', '', open(f, encoding='utf-8').read(), flags=re.S)
    for m in re.finditer(r'\\\((.*?)\\\)|\\\[(.*?)\\\]', h, flags=re.S):
        s = (m.group(1) if m.group(1) is not None else m.group(2)); total += 1
        for rx, msg in RULES:
            if re.search(rx, s): bad += 1; print('✗', f.split('lessons/')[1], '|', msg, '|', s[:60].replace('\n', ' '))
print('%d công thức kiểm tra ký hiệu hình học, %d lỗi' % (total, bad)); sys.exit(1 if bad else 0)
