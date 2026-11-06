/* MathBridge – tính dữ liệu cho hình vẽ tĩnh (PGFPlots / TikZ) bằng chính lõi toán của web (js/mb-graph-core.js).
   Vào (stdin): JSON danh sách việc  [{graph: cfg} | {curve: {f, view}}]
   Ra  (stdout): JSON danh sách kết quả: nhánh đồ thị (đã ngắt tại tiệm cận/gián đoạn), điểm đặc biệt, khoảng đơn điệu,
   tiếp tuyến, tiệm cận đứng / ngang / xiên tự phát hiện (để vẽ nét đứt). */
'use strict';
var fs = require('fs'), path = require('path');
var Core = require(path.join(__dirname, '..', 'js', 'mb-graph-core.js'));
var fin = function (v) { return typeof v === 'number' && isFinite(v); };
var r6 = function (v) { return Math.round(v * 1e6) / 1e6; };

function pieces(f, lo, hi, y0, y1, n) {
  var out = Core.plotPieces(f, lo, hi, y0, y1, n || 1600), res = [], cur = [];
  var H = y1 - y0, top = y1 + 0.6 * H, bot = y0 - 0.6 * H;
  for (var i = 0; i < out.x.length; i++) {
    var x = out.x[i], y = out.y[i];
    if (!fin(x) || !fin(y)) { if (cur.length > 1) res.push(cur); cur = []; continue; }
    cur.push([r6(x), r6(Math.max(bot, Math.min(top, y)))]);
  }
  if (cur.length > 1) res.push(cur);
  return res;
}
function niceVal(c, tol) {                  // làm tròn hoành độ tiệm cận về giá trị "đẹp" (k/12 hoặc kπ/12) nếu gần
  var cands = [Math.round(c * 12) / 12, Math.round(c / Math.PI * 12) * Math.PI / 12];
  var best = c, bd = tol;
  cands.forEach(function (v) { if (Math.abs(v - c) < bd) { bd = Math.abs(v - c); best = v; } });
  return best;
}
function poles(f, lo, hi, y0, y1) {          // tiệm cận đứng trong khung nhìn
  var ps = pieces(f, lo, hi, y0, y1, 3000), xs = [];
  for (var i = 0; i + 1 < ps.length; i++) {
    var a = ps[i][ps[i].length - 1][0], b = ps[i + 1][0][0], c = niceVal((a + b) / 2, Math.max(b - a, (hi - lo) / 400));
    if (Core.checkAsymptote(f, { type: 'v', x: c }) && xs.every(function (v) { return Math.abs(v - c) > 1e-6; })) xs.push(r6(c));
  }
  return xs;
}
function slantAsym(f) {                      // tiệm cận ngang/xiên y = m x + b (nếu có, kiểm tra cả hai phía)
  var res = [];
  [1, -1].forEach(function (s) {
    var X = s * 1e6, y1 = f(X), y2 = f(2 * X);
    if (!fin(y1) || !fin(y2)) return;
    var m = (y2 - y1) / X, b = y1 - m * X;
    if (Math.abs(m) > 1e3) return;
    m = Math.abs(m - Math.round(m * 1e4) / 1e4) < 1e-5 ? Math.round(m * 1e4) / 1e4 : m;
    b = Math.abs(b - Math.round(b * 1e3) / 1e3) < 1e-3 ? Math.round(b * 1e3) / 1e3 : b;
    var a = { type: m === 0 ? 'h' : 'o', m: m, b: b, y: b };
    if (Core.checkAsymptote(f, a) && !res.some(function (q) { return Math.abs(q.m - m) < 1e-6 && Math.abs(q.b - b) < 1e-6; })) res.push(a);
  });
  return res;
}

function graph(cfg) {
  var v = cfg.view, x0 = v[0], x1 = v[1], y0 = v[2], y1 = v[3];
  var params = cfg.params || [], names = params.map(function (p) { return p.name; }), scope = {};
  params.forEach(function (p) { scope[p.name] = p.value; });
  var fns = (cfg.functions || []).map(function (s) { var c = Core.compile(s.f, names); return function (x) { return c(x, scope); }; });
  var R = { functions: [], marks: [], monotone: [], highlights: [], tangent: null, autoAsym: [] };
  (cfg.functions || []).forEach(function (s, i) {
    var f = fns[i], dom = s.domain, lo = Math.max(x0, dom ? dom[0] : -Infinity), hi = Math.min(x1, dom ? dom[1] : Infinity);
    var o = { pieces: pieces(f, lo, hi, y0, y1), ends: [] };
    if (dom && s.open) [0, 1].forEach(function (k) { var y = f(dom[k]); if (fin(y)) o.ends.push({ x: dom[k], y: r6(y), open: !!s.open[k] }); });
    R.functions.push(o);
    if (!s.dash && !params.length) {          // tiệm cận tự phát hiện (hàm có cực điểm: phân thức, tan, …)
      var vs = poles(f, lo, hi, y0, y1);
      vs.forEach(function (x) { R.autoAsym.push({ type: 'v', x: x, f: i }); });
      if (vs.length && !/sin|cos|tan|cot/.test(s.f)) slantAsym(f).forEach(function (a) { a.f = i; R.autoAsym.push(a); });
    }
  });
  var mk = cfg.mark || {}, mr = cfg.markRange, lo = mr ? Math.max(x0, mr[0]) : x0, hi = mr ? Math.min(x1, mr[1]) : x1, w = hi - lo;
  var A = lo - 0.02 * w, B = hi + 0.02 * w, inView = function (x, y) { return x >= x0 && x <= x1 && y >= y0 && y <= y1; };
  (mk.roots || []).forEach(function (fi) { Core.rootsDetailed(fns[fi], A, B).forEach(function (r) { if (inView(r.x, 0)) R.marks.push({ kind: 'root', x: r6(r.x), y: 0, f: fi, mult: r.mult || 1 }); }); });
  (mk.yint || []).forEach(function (fi) { var y = fns[fi](0); if (fin(y) && inView(0, y)) R.marks.push({ kind: 'yint', x: 0, y: r6(y), f: fi }); });
  (mk.extrema || []).forEach(function (fi) { Core.extrema(fns[fi], A, B).forEach(function (e) { if (inView(e.x, e.y)) R.marks.push({ kind: e.kind, x: r6(e.x), y: r6(e.y), f: fi }); }); });
  (mk.inflections || []).forEach(function (fi) { Core.inflections(fns[fi], A, B).forEach(function (q) { if (inView(q.x, q.y)) R.marks.push({ kind: 'infl', x: r6(q.x), y: r6(q.y), f: fi }); }); });
  (mk.holes || []).forEach(function (fi) { Core.holes(fns[fi], A, B).forEach(function (h) { if (inView(h.x, h.y)) R.marks.push({ kind: 'hole', x: r6(h.x), y: r6(h.y), f: fi }); }); });
  (mk.intersections || []).forEach(function (pr) { Core.intersections(fns[pr[0]], fns[pr[1]], A, B).forEach(function (x) { var y = fns[pr[0]](x); if (inView(x, y)) R.marks.push({ kind: 'int', x: r6(x), y: r6(y) }); }); });
  if (cfg.monotone) {
    var mf = fns[cfg.monotone.f || 0], rg = cfg.monotone.range || [A, B];
    Core.monotoneIntervals(mf, Math.max(rg[0], A), Math.min(rg[1], B)).forEach(function (iv) { R.monotone.push({ up: iv.up, pieces: pieces(mf, iv.from, iv.to, y0, y1, 600) }); });
  }
  (cfg.highlights || []).forEach(function (h) { R.highlights.push({ color: h.color, pieces: pieces(fns[h.f || 0], h.x[0], h.x[1], y0, y1, 600) }); });
  if (cfg.tangent) { var tf = fns[cfg.tangent.f || 0], ats = [].concat(cfg.tangent.at); R.tangent = ats.map(function (t) { return { x: t, y: r6(tf(t)), k: r6(Core.deriv(tf, t)) }; }); }
  return R;
}
var jobs = JSON.parse(fs.readFileSync(0, 'utf8'));
var out = jobs.map(function (j) {
  if (j.graph) return graph(j.graph);
  var c = Core.compile(j.curve.f, []), f = function (x) { return c(x, {}); }, v = j.curve.view;
  return { pieces: pieces(f, v[0], v[1], v[2], v[3]) };
});
process.stdout.write(JSON.stringify(out));
