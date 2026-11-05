# -*- coding: utf-8 -*-
"""Kiểm thử công thức.  python tests/test-mathjax.py [--real]
Chế độ mặc định (không cần mạng): phân tích tĩnh mọi công thức trong lessons.json/HTML:
  ngoặc {} và \\left/\\right cân, \\begin/\\end khớp, môi trường thuộc gói ams, không còn ký tự điều khiển (\\t,\\f,\\b do quên raw string).
Chế độ --real (cần tests/node_modules đã cài mathjax 3.2.2): dựng bằng MathJax thật trong Chromium và kiểm tra
  không có mjx-merror, công thức riêng dòng không làm trang tràn ngang ở 360/768/1024 px, iframe cao đúng nội dung."""
import re, os, sys, glob, json, subprocess, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
ENVS = {'aligned', 'align', 'cases', 'matrix', 'pmatrix', 'bmatrix', 'vmatrix', 'array', 'gathered', 'split', 'equation', 'smallmatrix'}
KNOWN_BAD = re.compile(r'[\x00-\x08\x0b\x0c\x0e-\x1f]')
def check(tex):
    e = []
    s = re.sub(r'\\[{}]', '', tex)
    if s.count('{') != s.count('}'): e.append('ngoặc {} lệch')
    if len(re.findall(r'\\left\b', tex)) != len(re.findall(r'\\right\b', tex)): e.append('\\left/\\right lệch')
    b = re.findall(r'\\begin\{(\w+)\}', tex); en = re.findall(r'\\end\{(\w+)\}', tex)
    if b != en[::-1] and sorted(b) != sorted(en): e.append('\\begin/\\end lệch')
    for x in b:
        if x not in ENVS: e.append('môi trường lạ: ' + x)
    if KNOWN_BAD.search(tex): e.append('ký tự điều khiển (quên raw string?)')
    if re.search(r'\\(?:frac|sqrt)\s*$', tex): e.append('lệnh thiếu đối số')
    return e
fails = 0; total = 0
for f in sorted(glob.glob('lessons/**/*.html', recursive=True)):
    h = open(f, encoding='utf-8').read(); h = re.sub(r'<script.*?</script>', '', h, flags=re.S)
    for m in re.finditer(r'\\\((.*?)\\\)|\\\[(.*?)\\\]', h, flags=re.S):
        tex = m.group(1) if m.group(1) is not None else m.group(2); total += 1
        for er in check(tex.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')):
            fails += 1; print('✗', f.split('lessons/')[1], '|', er, '|', tex[:70].replace('\n', ' '))
print('%d công thức, %d lỗi' % (total, fails))
if fails: sys.exit(1)
if '--real' in sys.argv:
    root = os.path.join(ROOT, 'tests', 'node_modules')
    if not os.path.isdir(os.path.join(root, 'mathjax')): print('Chưa cài: cd tests && npm install'); sys.exit(2)
    from playwright.sync_api import sync_playwright
    srv = subprocess.Popen([sys.executable, '-m', 'http.server', '8781', '--directory', ROOT], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)
    bad = 0
    try:
        with sync_playwright() as p:
            b = p.chromium.launch(); lessons = json.load(open('lessons.json', encoding='utf-8'))
            for L in lessons:
                for w in (360, 768, 1024):
                    pg = b.new_page(viewport={'width': w, 'height': 800})
                    pg.route('**/mathjax*/**', lambda r: r.fulfill(path=os.path.join(root, 'mathjax', 'es5', 'tex-chtml.js'), content_type='application/javascript'))
                    pg.goto('http://localhost:8781/' + L['path']); pg.wait_for_function('window.MathJax && MathJax.startup && MathJax.startup.promise', timeout=15000)
                    pg.evaluate('MathJax.startup.promise'); pg.wait_for_timeout(500)
                    errs = pg.evaluate("document.querySelectorAll('mjx-merror').length")
                    over = pg.evaluate('document.documentElement.scrollWidth - document.documentElement.clientWidth')
                    if errs or over > 1: bad += 1; print('✗', L['path'], w, 'merror=%d tràn=%dpx' % (errs, over))
                    pg.close()
            b.close()
    finally: srv.terminate()
    sys.exit(1 if bad else 0)
