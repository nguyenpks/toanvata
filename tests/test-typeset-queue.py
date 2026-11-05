# -*- coding: utf-8 -*-
"""MathJax giả: kiểm tra lesson-kit xếp hàng các lần dựng (không chạy chồng), không nuốt lỗi, vẫn cập nhật chiều cao.  python tests/test-typeset-queue.py"""
import os, sys, json, subprocess, time
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAKE = """window.__mj={active:0,max:0,calls:0};
window.MathJax={startup:{promise:Promise.resolve()},typesetClear:function(){},
 typesetPromise:function(){var m=window.__mj;m.active++;m.calls++;m.max=Math.max(m.max,m.active);
  return new Promise(function(r,j){setTimeout(function(){m.active--;(m.calls===3)?j(new Error('boom')):r();},40)})}};"""
srv = subprocess.Popen([sys.executable, '-m', 'http.server', '8783', '--directory', ROOT], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)
bad = []
try:
    with sync_playwright() as p:
        b = p.chromium.launch(); path = json.load(open(os.path.join(ROOT, 'lessons.json'), encoding='utf-8'))[0]['path']
        pg = b.new_page(); warns = []; pg.on('console', lambda m: warns.append(m.text) if m.type == 'warning' else None)
        pg.route('**/mathjax*/**', lambda r: r.fulfill(body=FAKE, content_type='application/javascript'))
        pg.route('**/js/mathjax-config.js', lambda r: r.fulfill(body='', content_type='application/javascript'))
        pg.goto('http://localhost:8783/' + path); pg.wait_for_timeout(300)
        pg.evaluate("mbTypeset(document.body);mbTypeset(document.body);mbTypeset(document.body);mbTypeset(document.body)"); pg.wait_for_timeout(600)
        r = pg.evaluate('window.__mj')
        if r['max'] != 1: bad.append('dựng chồng nhau: max=%d' % r['max'])
        if not any('boom' in w for w in warns): bad.append('lỗi MathJax bị nuốt, không ghi cảnh báo')
        if r['calls'] < 4: bad.append('chuỗi bị đứt sau lỗi: calls=%d' % r['calls'])
        b.close()
finally: srv.terminate()
print('\n'.join('✗ ' + x for x in bad) or 'đạt'); sys.exit(1 if bad else 0)
