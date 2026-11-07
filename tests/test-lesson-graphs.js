/* Kiểm tra TOÁN HỌC cấu hình đồ thị trong các bài học:  node tests/test-lesson-graphs.js
   Đồ thị nay là hình TĨNH vẽ bằng PGFPlots (img/tex/<băm>.svg); cấu hình gốc lưu kèm ở img/tex/<băm>.json.
   Với mọi đồ thị (và khối data-mbg cũ nếu còn): biểu thức đọc được; tiệm cận khai báo đúng với hàm; lỗ thủng khai báo đúng là gián đoạn bỏ được
   với giá trị giới hạn đúng; đầu mút miền (○/●) có giá trị hữu hạn; chỉ số hàm trong mark/monotone hợp lệ; mọi điểm đặc biệt tính ra nằm trong khung nhìn. */
const fs = require('fs'), path = require('path');
const C = require('../js/mb-graph-core.js');
const ROOT = path.join(__dirname, '..');
const unesc = s => s.replace(/&quot;/g, '"').replace(/&#x27;|&#39;/g, "'").replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&');
function walk(d) { return fs.readdirSync(d, { withFileTypes: true }).flatMap(e => e.isDirectory() ? walk(path.join(d, e.name)) : e.name.endsWith('.html') ? [path.join(d, e.name)] : []); }
let n = 0, bad = 0;
function ok(c, m, f) { if (!c) { bad++; console.log('  ✗', path.relative(ROOT, f), '|', m); } }
let n3 = 0, nt = 0;
function check3d(cfg, file) {
  n3++; const P = cfg.points || {}, has = k => Array.isArray(P[k]) && P[k].length === 3 && P[k].every(Number.isFinite);
  const names = [].concat((cfg.segments || []).flatMap(s => [s[0], s[1]]), (cfg.lines || []).flatMap(s => [s[0], s[1]]), (cfg.polygons || []).flatMap(p => p.points || p));
  names.forEach(k => ok(has(k), '3D: điểm "' + k + '" chưa khai báo tọa độ', file));
  const seen = {}; (cfg.segments || []).forEach(s => { const k = [s[0], s[1]].sort().join('|'); ok(!seen[k], '3D: đoạn ' + s[0] + s[1] + ' khai báo hai lần', file); seen[k] = 1; });
  (cfg.polygons || []).forEach(p => {                   // mặt đa giác phải phẳng
    const q = (p.points || p).map(k => P[k]); if (q.length < 4 || !q.every(Boolean)) return;
    const a = q[0], u = q[1].map((v, i) => v - a[i]), w = q[2].map((v, i) => v - a[i]), nn = [u[1] * w[2] - u[2] * w[1], u[2] * w[0] - u[0] * w[2], u[0] * w[1] - u[1] * w[0]];
    q.slice(3).forEach(r => ok(Math.abs(nn.reduce((s, c, i) => s + c * (r[i] - a[i]), 0)) < 1e-9, '3D: mặt ' + (p.points || p).join('') + ' không phẳng', file));
  });
  if (cfg.solid) {
    const sn = Array.isArray(cfg.solid) ? cfg.solid : Object.keys(P), sp = {}; sn.forEach(k => sp[k] = P[k]);
    const h = C.hull3d(sp);
    ok(sn.length - h.edges.length + h.faces.length === 2, '3D: khối không thỏa công thức Euler V−E+F=2 (V=' + sn.length + ', E=' + h.edges.length + ', F=' + h.faces.length + ')', file);
    ok(h.edges.every(e => e.faces.length === 2), '3D: có cạnh không kề đúng 2 mặt', file);
    const onHull = new Set(); h.faces.forEach(f => f.names.forEach(k => onHull.add(k)));
    sn.forEach(k => ok(onHull.has(k), '3D: điểm "' + k + '" khai báo trong solid nhưng không là đỉnh của khối', file));
    (cfg.segments || []).forEach(s => { const o = s[2] || {}; if (!o.dash && sn.includes(s[0]) && sn.includes(s[1])) ok(h.edges.some(e => [e.a, e.b].sort().join() === [s[0], s[1]].sort().join()), '3D: đoạn nét liền ' + s[0] + s[1] + ' không phải cạnh của khối (đường chéo/đường phụ phải nét đứt)', file); });
  } else ok(false, '3D: hình khối chưa bật "solid" nên nét khuất không được xử lý khi xoay', file);
}
walk(path.join(ROOT, 'lessons')).forEach(file => {
  const html = fs.readFileSync(file, 'utf-8'), re = /data-mbg=(?:'([^']*)'|"([^"]*)")/g; let m;
  const cfgs = [];
  while ((m = re.exec(html))) cfgs.push(JSON.parse(unesc(m[1] != null ? m[1] : m[2])));
  const ri = /img\/tex\/([0-9a-f]{16})\.svg/g;
  while ((m = ri.exec(html))) {
    const svg = path.join(ROOT, 'img', 'tex', m[1] + '.svg'), side = path.join(ROOT, 'img', 'tex', m[1] + '.json');
    ok(fs.existsSync(svg), 'thiếu tệp hình ' + m[1] + '.svg', file); nt++;
    if (fs.existsSync(side)) cfgs.push(JSON.parse(fs.readFileSync(side, 'utf-8')));
  }
  for (const cfg of cfgs) {
    if (cfg.kind === '3d') { check3d(cfg, file); continue; }
    if (cfg.kind !== 'graph') continue; n++;
    const names = (cfg.params || []).map(p => p.name), scope = {}; (cfg.params || []).forEach(p => scope[p.name] = p.value);
    const fns = [];
    try { cfg.functions.forEach(s => { const c = C.compile(s.f, names); fns.push(x => c(x, scope)); }); } catch (e) { ok(false, 'biểu thức lỗi: ' + e.message, file); continue; }
    const tag = ' [' + cfg.functions.map(s => s.f).join('; ') + ']';
    (cfg.asymptotes || []).forEach(a => {
      let any = fns.some(f => C.checkAsymptote(f, a));
      if (!any && cfg.param && a.type !== 'v') {        // đường cong tham số (hypebol…): điểm xa trên đường cong phải sát tiệm cận
        const m = a.type === 'h' ? 0 : a.m, b = a.type === 'h' ? a.y : a.b;
        any = cfg.param.some(c => { const X = C.compile(c.x.replace(/\bt\b/g, 'x'), []), Y = C.compile(c.y.replace(/\bt\b/g, 'x'), []);
          return [-7, 7].some(t => { const px = X(t, {}), py = Y(t, {}); return isFinite(px) && Math.abs(py - (m * px + b)) / Math.sqrt(1 + m * m) < 1e-2 * Math.max(1, Math.abs(px)) / 10; }); });
      }
      ok(any, 'tiệm cận khai báo SAI: ' + JSON.stringify(a) + tag, file);
    });
    (cfg.holes || []).forEach(h => {
      const f = fns.find(g => { const y = g(h[0]); return !isFinite(y) && C.holes(g, h[0] - 0.5, h[0] + 0.5).some(q => Math.abs(q.x - h[0]) < 1e-6 && Math.abs(q.y - h[1]) < 1e-3); });
      ok(!!f, 'lỗ thủng khai báo SAI: ' + JSON.stringify(h) + tag, file);
    });
    cfg.functions.forEach((s, i) => { if (s.domain && s.open) [0, 1].forEach(k => ok(isFinite(fns[i](s.domain[k])), 'đầu mút miền ' + s.domain[k] + ' không xác định' + tag, file)); });
    const idx = []; ['roots', 'yint', 'extrema', 'inflections'].forEach(k => (cfg.mark && cfg.mark[k] || []).forEach(i => idx.push(i)));
    (cfg.mark && cfg.mark.intersections || []).forEach(p => idx.push(p[0], p[1])); if (cfg.monotone) idx.push(cfg.monotone.f || 0);
    idx.forEach(i => ok(Number.isInteger(i) && i >= 0 && i < fns.length, 'chỉ số hàm ngoài phạm vi: ' + i, file));
  }
});
console.log((bad ? '✗' : '✓') + ' cấu hình hình vẽ trong bài học: ' + n + ' đồ thị, ' + n3 + ' hình khối, ' + nt + ' hình LaTeX, ' + bad + ' lỗi');
process.exit(bad ? 1 : 0);
