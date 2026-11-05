# -*- coding: utf-8 -*-
"""So sánh HTML sinh ra với baseline.  python tests/check_html_snapshot.py [--update]
Dùng khi chuẩn hóa LaTeX: đổi mã nguồn mà HTML không đổi => đúng nội dung."""
import hashlib, json, glob, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
B = 'tests/baseline/html-hashes.json'
h = lambda f: hashlib.sha256(open(f, 'rb').read()).hexdigest()
cur = {f: h(f) for f in sorted(glob.glob('lessons/**/*.html', recursive=True))}; cur['lessons.json'] = h('lessons.json')
if '--update' in sys.argv: json.dump(cur, open(B, 'w'), indent=1); print('đã cập nhật baseline', len(cur)); sys.exit(0)
old = json.load(open(B)); diff = [f for f in sorted(set(old) | set(cur)) if old.get(f) != cur.get(f)]
for f in diff: print('  khác:', f)
sys.exit(1 if diff else 0)
