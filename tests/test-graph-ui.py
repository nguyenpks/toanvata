# -*- coding: utf-8 -*-
"""Kiểm thử phần ghép nối của hệ thống đồ thị bằng trình duyệt thật + JSXGraph GIẢ LẬP (tests/mock-jxg.js).
Không thay thế việc xem hình thật với thư viện JSXGraph; xem docs/GRAPH.md mục "Kiểm thử"."""
import sys, os, json, subprocess, time
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = sys.argv[1] if len(sys.argv) > 1 else 'demo/graph-demo.html'
MOCK = open(os.path.join(ROOT, 'tests', 'mock-jxg.js'), encoding='utf-8').read()
srv = subprocess.Popen([sys.executable, '-m', 'http.server', '8777', '--directory', ROOT], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)
fails = []
def ok(c, m):
    print(('  ✓ ' if c else '  ✗ ') + m)
    if not c: fails.append(m)
try:
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 900, 'height': 900}); errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)[:200]))
        pg.route('**/jsxgraph*/**/jsxgraphcore.js', lambda r: r.fulfill(body=MOCK, content_type='application/javascript'))
        pg.route('**/jsxgraph*/**/jsxgraph.css', lambda r: r.fulfill(body='', content_type='text/css'))
        pg.route('**/mathjax*/**', lambda r: r.fulfill(body='', content_type='application/javascript'))
        pg.goto('http://localhost:8777/' + PAGE); pg.wait_for_timeout(800)
        info = pg.evaluate("""() => (window.__boards||[]).map(b => ({
            id: b.id, types: b.created.reduce((m,o)=>{m[o.type]=(m[o.type]||0)+1;return m},{}), bb: b.bb,
            curves: b.created.filter(o=>o.type==='curve').map(o=>({x:o.dataX, y:o.dataY, color:o.attrs.strokeColor})) }))""")
        print('Số bảng vẽ đã khởi tạo:', len(info))
        ok(len(info) >= 11, 'đủ 11 hình trong trang demo (nhận %d)' % len(info))
        def isnan(v): return v is None or v != v
        def nan_breaks(c): return sum(1 for v in c['x'] if isnan(v))
        def has_cross(c, x0):
            xs = c['x']
            return any((not isnan(xs[i])) and (not isnan(xs[i+1])) and xs[i] < x0 < xs[i+1] for i in range(len(xs)-1))
        # 1. đa thức
        t = info[0]['types']; ok(t.get('curve', 0) >= 4 and t.get('point', 0) >= 7, 'x³−3x: đường cong chính + 3 khoảng đơn điệu, ≥7 điểm đặc biệt (cong %d, điểm %d)' % (t.get('curve', 0), t.get('point', 0)))
        # 2. phân thức
        c = info[1]['curves'][0]; ok(nan_breaks(c) >= 1 and not has_cross(c, 2), 'phân thức: ngắt tại tiệm cận x=2, không nối qua')
        ok(info[1]['types'].get('line', 0) == 2, 'phân thức: 2 đường tiệm cận (đứng + xiên)')
        # 4. tan
        c = info[3]['curves'][0]; ok(nan_breaks(c) == 4, 'tan: 4 chỗ ngắt trong [-5,5] (nhận %d)' % nan_breaks(c))
        # 6. từng đoạn: 2 đoạn có đầu mút hở
        ok(any(o for o in info[5]['curves']) and info[5]['types'].get('point', 0) >= 3, 'hàm từng đoạn: có điểm đầu mút hở/đặc và cực tiểu |x−2|')
        # 7. thanh trượt làm đổi đồ thị
        before = max(y for y in info[6]['curves'][0]['y'] if not isnan(y))
        pg.evaluate("""() => { var host=document.querySelectorAll('.mbg')[6]; var s=host.querySelector('input[type=range]'); s.value=3; s.dispatchEvent(new Event('input')); }""")
        after = pg.evaluate("() => Math.max(...window.__boards[6].created.filter(o=>o.type==='curve')[0].dataY.filter(v=>v!==null && isFinite(v)))")
        ok(abs(after - before) > 1, 'thanh trượt a đổi đồ thị (%.1f → %.1f)' % (before, after))
        # 8. tiếp tuyến di động
        ok(info[7]['types'].get('line', 0) >= 1, 'tiếp tuyến: có đường thẳng tiếp tuyến')
        pg.evaluate("""() => { var s=document.querySelectorAll('.mbg')[7].querySelector('input[type=range]'); s.value=-1; s.dispatchEvent(new Event('input')); }""")
        read = pg.evaluate("() => document.querySelectorAll('.mbg')[7].querySelector('.mbg-read').textContent")
        ok('f′(x₀) ≈ 1' in read, 'tại x₀=−1 của x³−2x: f′ = 3·1−2 = 1 → "%s"' % read)
        # 9. hình học: dựng bằng quan hệ thật
        g = pg.evaluate("""() => { var b=window.__boards[8]; var m=b.created;
            var perp = m.find(o=>o.type==='perpendicular'); var seg = m.find(o=>o.type==='segment' && o.args[0].args && o.args[0].args[0]===-4);
            return { types: b.created.reduce((a,o)=>{a[o.type]=(a[o.type]||0)+1;return a},{}),
                     perpArgs: perp.args.map(a=>a.type+(a.args&&a.args.length?'['+a.args.join(',')+']':'')),
                     bis: m.find(o=>o.type==='bisector').args.length, angle: m.find(o=>o.type==='angle').args.length,
                     angleSel: m.find(o=>o.type==='angle').attrs.selection } }""")
        ok(g['types'].get('perpendicular', 0) >= 1 and g['perpArgs'][0].startswith('segment') and g['perpArgs'][1].startswith('point'), 'đường cao dùng ràng buộc "perpendicular"(đoạn, điểm): ' + str(g['perpArgs'][:2]))
        ok(g['types'].get('midpoint', 0) == 1 and g['bis'] == 3 and g['angle'] == 3, 'trung tuyến dùng midpoint; phân giác & góc nhận 3 điểm')
        # 10. tiếp tuyến đường tròn = vuông góc với bán kính; song song
        g2 = pg.evaluate("""() => { var b=window.__boards[9]; var t=b.created.reduce((a,o)=>{a[o.type]=(a[o.type]||0)+1;return a},{}); return t }""")
        ok(g2.get('perpendicular', 0) == 1 and g2.get('parallel', 0) == 1 and g2.get('glider', 0) == 1 and g2.get('circle', 0) == 1, 'tiếp tuyến = perpendicular(bán kính, tiếp điểm); song song = parallel; glider trên đường tròn ' + str(g2))
        # 11. 3D
        g3 = pg.evaluate("() => window.__boards[10].created.reduce((a,o)=>{a[o.type]=(a[o.type]||0)+1;return a},{})")
        ok(g3.get('view3d') == 1 and g3.get('point3d') == 5 and g3.get('polygon3d') == 1 and g3.get('line3d') == 4, 'chóp S.ABCD: 5 điểm, 1 đáy, 4 cạnh bên ' + str(g3))
        # Thu phóng, tỉ lệ, đặt lại
        i = 0
        bb0 = pg.evaluate("() => window.__boards[0].bb.slice()")
        pg.evaluate("() => document.querySelectorAll('.mbg')[0].querySelector('[data-k=zin]').click()")
        bb1 = pg.evaluate("() => window.__boards[0].bb.slice()")
        ok((bb1[2] - bb1[0]) < (bb0[2] - bb0[0]) * 0.9, 'nút ＋ phóng to')
        xs = pg.evaluate("() => window.__boards[0].created.filter(o=>o.type==='curve')[0].dataX.filter(v=>v!==null)")
        ok(min(xs) >= bb1[0] - 1e-6 and max(xs) <= bb1[2] + 1e-6, 'sau khi phóng to, đồ thị được lấy mẫu lại theo khung mới')
        pg.evaluate("() => document.querySelectorAll('.mbg')[0].querySelector('[data-k=eq]').click()")
        r = pg.evaluate("() => { var b=window.__boards[0], bb=b.bb; return [(bb[2]-bb[0])/b.canvasWidth, (bb[1]-bb[3])/b.canvasHeight]; }")
        ok(abs(r[0] - r[1]) < 1e-9, 'nút 1:1 làm hai trục cùng tỉ lệ (%.5f vs %.5f)' % (r[0], r[1]))
        pg.evaluate("() => document.querySelectorAll('.mbg')[0].querySelector('[data-k=reset]').click()")
        ok(pg.evaluate("() => window.__boards[0].bb.join(',')") == '-4,5,4,-5', 'nút ⟲ đặt lại khung nhìn ban đầu')
        # Mức học đổi nhãn nút
        t1 = pg.evaluate("() => document.querySelectorAll('.mbg')[0].querySelector('[data-k=zin]').title")
        pg.evaluate("() => document.body.setAttribute('data-level','3')"); pg.wait_for_timeout(200)
        t3 = pg.evaluate("() => document.querySelectorAll('.mbg')[0].querySelector('[data-k=zin]').title")
        ok(t1 == 'Phóng to' and t3 == 'Zoom in', 'nhãn nút đổi theo mức học: "%s" → "%s"' % (t1, t3))
        # --- Giai đoạn 2: điểm đặc biệt tính lại theo khung nhìn, bội nghiệm, lỗ thủng tự nhận ---
        r = pg.evaluate("""() => new Promise(done => {
          const host = document.createElement('div'); host.className = 'mbg'; host.style.height = '360px'; document.body.appendChild(host);
          host.setAttribute('data-mbg', JSON.stringify({kind:'graph', view:[-4,4,-2,2], functions:[{f:'sin(x)'},{f:'(x-1)^2*(x+2)'},{f:'(x^2-1)/(x-1)'}], mark:{roots:[0,1], extrema:[0], holes:[2]}}));
          MBG.setup(host); const g = host.__mbg, b = g.board;
          const pts = () => b.created.filter(o => o.type === 'point' && o.attrs.size).map(o => ({x:o.args[0], y:o.args[1], n:o.attrs.name, s:o.attrs.size}));
          const n0 = pts().length; b.setBoundingBox([-12,3,12,-3]);
          setTimeout(() => { const z1 = pts(), n1 = z1.length; b.setBoundingBox([0.9,0.2,1.1,-0.2]);
            setTimeout(() => { const z = pts(); done({n0, n1, z, z1}); }, 250); }, 250);
        })""")
        ok(r['n1'] > r['n0'], 'thu nhỏ khung nhìn: điểm đặc biệt MỚI xuất hiện (%d → %d điểm)' % (r['n0'], r['n1']))
        ok(any(abs(q['x'] - 1) < 1e-3 and abs(q['y']) < 1e-6 and q['s'] == 5 and '×2' in (q['n'] or '') for q in r['z']), 'phóng vào quanh x=1: nghiệm kép được ghi "×2" và vẽ to hơn')
        ok(any(abs(q['x'] - 1) < 1e-6 and abs(q['y'] - 2) < 1e-3 for q in r['z1']), 'lỗ thủng (1; 2) của (x²−1)/(x−1) được nhận tự động')
        # --- Giai đoạn 3: nét khuất 3D, ký hiệu đoạn bằng nhau / song song, nhãn điểm ---
        r3 = pg.evaluate("""() => new Promise(done => {
          const cube = {A:[-2,-2,-2],B:[2,-2,-2],C:[2,2,-2],D:[-2,2,-2],"A'":[-2,-2,2],"B'":[2,-2,2],"C'":[2,2,2],"D'":[-2,2,2]};
          const host = document.createElement('div'); host.className = 'mbg'; host.style.height = '380px'; document.body.appendChild(host);
          host.setAttribute('data-mbg', JSON.stringify({kind:'3d', solid:true, box:[[-3,3],[-3,3],[-3,3]], points:cube, segments:[['A','B',{color:'#c2410c',width:4.5}]]}));
          MBG.setup(host); const g = host.__mbg, v = g.view, out = [];
          const lines = () => g.board.created.filter(o => o.type === 'line3d').map(o => ({a:o.args[0].args.join(), b:o.args[1].args.join(), dash:o.attrs.dash}));
          out.push({az:0.6, el:0.5, v:[0,0,0], L:lines()});
          [[2.5,0.8],[-1.2,0.3]].forEach(([az, el]) => { v.setAngles(az, el); out.push({az, el, L:lines()}); });
          done({out, cube, nlines: lines().length});
        })""")
        import math
        def view_vec(az, el):
            r1 = (math.cos(az), -math.sin(az), 0.0); r2 = (math.sin(el)*math.sin(az), math.sin(el)*math.cos(az), math.cos(el))
            v = (r1[1]*r2[2]-r1[2]*r2[1], r1[2]*r2[0]-r1[0]*r2[2], r1[0]*r2[1]-r1[1]*r2[0])
            return v if v[2] >= 0 else tuple(-c for c in v)
        ok(r3['nlines'] == 12, '3D: khối lập phương có đúng 12 cạnh (cạnh đã khai báo không bị vẽ lặp): %d' % r3['nlines'])
        cube = r3['cube']
        for e in r3['out']:
            v = view_vec(e['az'], e['el']); bad = 0; hidden = 0
            for l in e['L']:
                A = [float(x) for x in l['a'].split(',')]; B = [float(x) for x in l['b'].split(',')]
                m = [(A[i]+B[i])/2 + 0.01*v[i] for i in range(3)]; behind = all(-2 < m[i] < 2 for i in range(3))
                hidden += 1 if behind else 0
                if bool(l['dash']) != behind: bad += 1
            ok(bad == 0 and hidden == 3, '3D (az=%.1f, el=%.1f): đúng 3 cạnh nét đứt, khớp phép thử tia nhìn (sai %d)' % (e['az'], e['el'], bad))
        # ký hiệu trên đoạn
        r4 = pg.evaluate("""() => {
          const host = document.createElement('div'); host.className = 'mbg'; host.style.height = '300px'; document.body.appendChild(host);
          host.setAttribute('data-mbg', JSON.stringify({kind:'geo', view:[-5,5,-3,3], steps:[{type:'point',id:'A',at:[-3,0]},{type:'point',id:'B',at:[3,0]},{type:'point',id:'C',at:[0,2]},
            {type:'segment',through:['A','B'],mark:'eq3'},{type:'segment',through:['A','C'],mark:'eq'},{type:'segment',through:['B','C'],mark:'par2'}]}));
          MBG.setup(host); const b = host.__mbg.board; b.update();
          return b.created.filter(o => o.type === 'curve').map(o => ({x:o.dataX, y:o.dataY, n:o.attrs.strokeColor}));
        }""")
        cnt = lambda c: sum(1 for i, v in enumerate(c['x']) if v != v)    # mỗi dấu kết thúc bằng một NaN
        ok([cnt(c) for c in r4] == [3, 1, 2], 'ký hiệu đoạn: đoạn bằng nhau 3 gạch, 1 gạch, song song 2 mũi tên %s' % [cnt(c) for c in r4])
        ok(abs(sum(v for v in r4[0]['x'] if v == v)/9 - 0) < 1e-9, 'ba gạch nằm đối xứng quanh trung điểm của AB')
        ok(not errs, 'không có lỗi JavaScript ' + str(errs))
        b.close()
finally:
    srv.terminate()
print('\n' + ('TẤT CẢ ĐẠT' if not fails else 'CÓ %d LỖI' % len(fails)))
sys.exit(1 if fails else 0)
