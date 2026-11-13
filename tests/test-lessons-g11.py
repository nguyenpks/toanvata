# -*- coding: utf-8 -*-
"""Kiểm thử các bài lớp 11 trong trình duyệt (JSXGraph GIẢ LẬP, MathJax tắt):  python tests/test-lessons-g11.py [lớp]
Với mỗi bài: (1) mỗi mức có cùng số câu nhưng KHÔNG câu nào trùng giữa các mức; (2) làm đúng toàn bộ mỗi mức ra điểm tuyệt đối,
chỉ tính câu của mức đang học; (3) công thức \\( \\) cân bằng ngoặc, không còn [[ ]]; (4) hình vẽ khởi tạo, không lỗi JavaScript."""
import sys, os, json, re, subprocess, time
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GRADE = int(sys.argv[1]) if len(sys.argv) > 1 else 11
MOCK = open(os.path.join(ROOT, 'tests', 'mock-jxg.js'), encoding='utf-8').read()
lessons = [x for x in json.load(open(os.path.join(ROOT, 'lessons.json'), encoding='utf-8')) if x['grade'] == GRADE]
if os.environ.get('ONLY'): lessons = [x for x in lessons if x['id'] in os.environ['ONLY'].split(',')]   # chỉ kiểm tra các bài nêu tên
srv = subprocess.Popen([sys.executable, '-m', 'http.server', '8779', '--directory', ROOT], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)
fails = []
def ok(c, m):
    if not c: fails.append(m); print('   ✗', m)
def tex_ok(t):
    for m in re.finditer(r'\\\((.*?)\\\)', t, flags=re.S):
        s = m.group(1)
        if s.count('{') != s.count('}') or s.count('\\left') != s.count('\\right'): return s[:60]
    return None
try:
    with sync_playwright() as p:
        b = p.chromium.launch()
        for L in lessons:
            pg = b.new_page(viewport={'width': 800, 'height': 900}); errs = []
            pg.on('pageerror', lambda e: errs.append(str(e)[:150]))
            pg.route('**/jsxgraph*/**/jsxgraphcore.js', lambda r: r.fulfill(body=MOCK, content_type='application/javascript'))
            pg.route('**/jsxgraph*/**/jsxgraph.css', lambda r: r.fulfill(body='', content_type='text/css'))
            pg.route('**/mathjax*/**', lambda r: r.fulfill(body='', content_type='application/javascript'))
            pg.goto('http://localhost:8779/' + L['path']); pg.wait_for_timeout(700)
            info = {}; texts = {}
            for lv in (1, 2, 3):
                pg.click('button[data-level="%d"]' % lv); pg.wait_for_timeout(150)
                items = [i for i in pg.query_selector_all('.mbl-item') if i.is_visible()]
                texts[lv] = [re.sub(r'\s+', ' ', i.query_selector('.tx .en').text_content()) for i in items]
                for i in items:
                    t, a = i.get_attribute('data-type'), i.get_attribute('data-answer')
                    if t in ('mcq', 'tf'): i.query_selector('input[value="%s"]' % a).check(force=True)
                    else: i.query_selector('input.mbl-input').fill(a.split('|')[0])
                    i.query_selector('[data-act="check"]').click(force=True)
                pg.click('.mbl-quiz [data-act="finish"]'); pg.wait_for_timeout(100)
                info[lv] = (len(items), re.search(r'(\d+) / (\d+)', pg.inner_text('.mbl-score')).groups())
            n = [info[k][0] for k in (1, 2, 3)]
            ok(len(set(n)) == 1 and n[0] >= 6, '%s: số câu mỗi mức không đều %s' % (L['id'], n))
            ok(all(info[k][1][0] == info[k][1][1] == str(n[0]) for k in (1, 2, 3)), '%s: làm đúng hết mà điểm không tuyệt đối %s' % (L['id'], info))
            same = (set(texts[1]) & set(texts[2])) | (set(texts[1]) & set(texts[3])) | (set(texts[2]) & set(texts[3]))
            ok(not same, '%s: có câu trùng giữa các mức: %s' % (L['id'], list(same)[:2]))
            html = open(os.path.join(ROOT, L['path']), encoding='utf-8').read()
            bad = tex_ok(html); ok(bad is None, '%s: công thức mất cân bằng ngoặc: %s' % (L['id'], bad))
            plain = re.sub(r'data-mbg="[^"]*"', '', html); plain = re.sub(r'<script.*?</script>', '', plain, flags=re.S)
            ok('[[' not in plain and '\\\\(' not in plain, '%s: còn [[ ]] hoặc \\\\( trong trang' % L['id'])
            pg.evaluate("() => document.querySelectorAll('figure img').forEach(i => { i.loading = 'eager'; })"); pg.wait_for_timeout(300)
            nb = pg.evaluate("() => [...document.querySelectorAll('figure img')].filter(i => i.complete && i.naturalWidth > 0).length")
            want = sum(len(re.findall(r'<img', f)) for f in re.findall(r'<figure.*?</figure>', html, flags=re.S))   # hình LaTeX tĩnh (PGFPlots, tkz-euclide, TikZ); biểu đồ song ngữ có 2 ảnh/hình
            ok(nb == want, '%s: %d/%d hình LaTeX tải được' % (L['id'], nb, want))
            pg.click('button[data-level="1"]'); pg.wait_for_timeout(200)
            ok(not errs, '%s: lỗi JavaScript %s' % (L['id'], errs))
            print('%-20s mỗi mức %d câu | điểm %s | hình đã vẽ %d/%d | %s' % (L['id'], n[0], '/'.join('%s/%s' % info[k][1] for k in (1, 2, 3)), nb, want, 'OK' if not [f for f in fails if L['id'] in f] else 'LỖI'))
            pg.close()
        b.close()
finally:
    srv.terminate()
print('\n' + ('TẤT CẢ ĐẠT' if not fails else 'CÓ %d LỖI' % len(fails))); sys.exit(1 if fails else 0)
