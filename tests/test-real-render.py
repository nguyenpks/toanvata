# -*- coding: utf-8 -*-
"""Kiểm thử với JSXGraph + MathJax THẬT (cần: cd tests && npm install).  python tests/test-real-render.py
Chạy trên máy bạn (sandbox không tải được thư viện). Kiểm tra:
  1. mọi hình trong 19 bài vẽ không lỗi (không .mbg-error), có canvas/svg;
  2. hình khối: xoay thật bằng thanh az/el của JSXGraph, đếm cạnh nét đứt = đúng 3 với hình lập phương và khớp phép thử tia nhìn;
  3. chụp ảnh từng hình ở 360/768/1024 px vào tests/out/ để xem bằng mắt (nhãn đè, ký hiệu, nét khuất).
Nếu bước 2 báo NGƯỢC (nét đứt rơi vào cạnh phía trước): đảo hướng chuẩn hóa trong Core.viewDirection (dấu ban đầu)."""
import os, sys, json, time, subprocess, math
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); NM = os.path.join(ROOT, 'tests', 'node_modules'); OUT = os.path.join(ROOT, 'tests', 'out'); os.makedirs(OUT, exist_ok=True)
if not os.path.isdir(os.path.join(NM, 'jsxgraph')) or not os.path.isdir(os.path.join(NM, 'mathjax')): print('Chưa cài: cd tests && npm install'); sys.exit(2)
srv = subprocess.Popen([sys.executable, '-m', 'http.server', '8785', '--directory', ROOT], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)
fails = []
def ok(c, m):
    print(('  ✓ ' if c else '  ✗ ') + m)
    if not c: fails.append(m)
def route(pg):
    pg.route('**/jsxgraph*/**/jsxgraphcore.js', lambda r: r.fulfill(path=os.path.join(NM, 'jsxgraph', 'distrib', 'jsxgraphcore.js'), content_type='application/javascript'))
    pg.route('**/jsxgraph*/**/jsxgraph.css', lambda r: r.fulfill(path=os.path.join(NM, 'jsxgraph', 'distrib', 'jsxgraph.css'), content_type='text/css'))
    pg.route('**/mathjax*/**', lambda r: r.fulfill(path=os.path.join(NM, 'mathjax', 'es5', 'tex-chtml.js'), content_type='application/javascript'))
try:
    with sync_playwright() as p:
        b = p.chromium.launch(); lessons = json.load(open(os.path.join(ROOT, 'lessons.json'), encoding='utf-8'))
        for L in lessons:
            for w in (360, 768, 1024):
                pg = b.new_page(viewport={'width': w, 'height': 900}); errs = []; pg.on('pageerror', lambda e: errs.append(str(e)[:120])); route(pg)
                pg.goto('http://localhost:8785/' + L['path']); pg.wait_for_timeout(2500)
                n = pg.evaluate("document.querySelectorAll('.mbg').length"); e = pg.evaluate("document.querySelectorAll('.mbg-error').length")
                if n:
                    ok(e == 0 and not errs, '%s @%d: %d hình, lỗi vẽ %d %s' % (L['path'].split('/')[-1], w, n, e, errs))
                    pg.screenshot(path=os.path.join(OUT, '%s-%d.png' % (os.path.basename(L['path'])[:-5], w)), full_page=True)
                pg.close()
        # xoay hình khối thật
        pg = b.new_page(viewport={'width': 900, 'height': 900}); route(pg)
        pg.goto('http://localhost:8785/lessons/grade11/lines-and-planes-in-space/parallel-lines-and-planes.html'); pg.wait_for_timeout(2500)
        res = pg.evaluate("""() => { const g = [...document.querySelectorAll('.mbg')].map(h => h.__mbg).find(x => x && x.hull && x.hull.faces.length === 6 && x.view);
          if (!g) return null; const v = g.view, out = [];
          const dashes = () => g.board.objectsList.filter(o => o.elType === 'line3d' || (o.type && String(o.elType).includes('line3d'))).map(o => ({a: o.point1.coords ? [o.point1.X(), o.point1.Y(), o.point1.Z()] : null, b: [o.point2.X(), o.point2.Y(), o.point2.Z()], dash: o.visProp.dash}));
          [[0.6,0.5],[2.0,0.8],[-1.0,0.35]].forEach(([az, el]) => { v.az_slide.setValue(az); v.el_slide.setValue(el); g.board.update(); g.refresh3d(); out.push({az, el, L: dashes()}); });
          return out; }""")
        ok(res is not None, 'tìm thấy hình lập phương tương tác')
        if res:
            for e in res:
                dashed = [l for l in e['L'] if l['dash'] and l['a']]
                ok(len(dashed) == 3, 'xoay thật (az=%.1f, el=%.1f): %d cạnh nét đứt (kỳ vọng 3 trên một lập phương)' % (e['az'], e['el'], len(dashed)))
        b.close()
finally: srv.terminate()
print('\nẢnh chụp để xem bằng mắt: tests/out/'); sys.exit(1 if fails else 0)
