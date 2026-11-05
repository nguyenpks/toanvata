/* MathBridge – lõi toán học của hệ thống đồ thị (không phụ thuộc thư viện vẽ, chạy được cả trong Node để kiểm thử).
   - compile(expr, params): đọc biểu thức như  (x^2-1)/(x-2), 2sin(3x), abs(x), sqrt(x), ln(x), 2^x ...
   - plotPieces(f, xmin, xmax, ymin, ymax, n): lấy mẫu đồ thị, NGẮT nhánh tại điểm gián đoạn/tiệm cận (không nối qua).
   - roots / intersections / extrema / inflections: tìm điểm đặc biệt bằng đổi dấu + chia đôi, loại các "nghiệm giả" ở tiệm cận.
   - formatPi(v): nhãn trục dạng π/2, 3π/2... */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.MBGCore = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  /* ---------- 1. Bộ đọc biểu thức ---------- */
  var FUNCS = {
    sin: Math.sin, cos: Math.cos, tan: Math.tan,
    cot: function (x) { return 1 / Math.tan(x); }, sec: function (x) { return 1 / Math.cos(x); }, csc: function (x) { return 1 / Math.sin(x); },
    asin: Math.asin, acos: Math.acos, atan: Math.atan, arcsin: Math.asin, arccos: Math.acos, arctan: Math.atan,
    sinh: Math.sinh, cosh: Math.cosh, tanh: Math.tanh,
    sqrt: Math.sqrt, cbrt: Math.cbrt, abs: Math.abs, exp: Math.exp, ln: Math.log, log2: Math.log2,
    floor: Math.floor, ceil: Math.ceil, round: Math.round, sign: Math.sign
  };
  var CONSTS = { pi: Math.PI, e: Math.E };

  function tokenize(src) {
    var s = String(src).replace(/\u2212/g, '-').replace(/\u00d7|\u00b7/g, '*').replace(/\u03c0/g, 'pi').replace(/\u221a/g, 'sqrt');
    var toks = [], i = 0, m;
    while (i < s.length) {
      var c = s[i];
      if (/\s/.test(c)) { i++; continue; }
      if ((m = /^(\d+\.?\d*|\.\d+)/.exec(s.slice(i)))) { toks.push({ t: 'num', v: parseFloat(m[1]) }); i += m[1].length; continue; }
      if ((m = /^[A-Za-z_][A-Za-z_0-9]*/.exec(s.slice(i)))) { toks.push({ t: 'id', v: m[0] }); i += m[0].length; continue; }
      if ('+-*/^(),'.indexOf(c) >= 0) { toks.push({ t: c }); i++; continue; }
      throw new Error('Ký tự không hợp lệ "' + c + '" trong biểu thức: ' + src);
    }
    return toks;
  }

  /* Biên dịch thành hàm f(x, scope). Hàm số được hiểu trong tập số thực: căn của số âm, ln của số không dương... cho NaN. */
  function compile(src, params) {
    var toks = tokenize(src), pos = 0, pset = {};
    (params || []).forEach(function (p) { pset[p] = true; });
    function peek() { return toks[pos]; }
    function eat(t) { if (!peek() || peek().t !== t) throw new Error('Thiếu "' + t + '" trong biểu thức: ' + src); return toks[pos++]; }
    function startsPrimary(tk) { return tk && (tk.t === 'num' || tk.t === 'id' || tk.t === '('); }

    function parseExpr() {
      var left = parseTerm();
      while (peek() && (peek().t === '+' || peek().t === '-')) {
        var op = toks[pos++].t, right = parseTerm(), l = left;
        left = op === '+' ? (function (a, b) { return function (x, sc) { return a(x, sc) + b(x, sc); }; })(l, right)
                          : (function (a, b) { return function (x, sc) { return a(x, sc) - b(x, sc); }; })(l, right);
      }
      return left;
    }
    function parseTerm() {
      var left = parseUnary();
      for (;;) {
        var tk = peek();
        if (tk && (tk.t === '*' || tk.t === '/')) {
          pos++; var r = parseUnary(), l = left;
          left = tk.t === '*' ? (function (a, b) { return function (x, sc) { return a(x, sc) * b(x, sc); }; })(l, r)
                              : (function (a, b) { return function (x, sc) { return a(x, sc) / b(x, sc); }; })(l, r);
        } else if (startsPrimary(tk)) {          // nhân ngầm: 2x, 2(x+1), (x+1)(x-1), x(x+2)
          var r2 = parseUnary(), l2 = left;
          left = (function (a, b) { return function (x, sc) { return a(x, sc) * b(x, sc); }; })(l2, r2);
        } else break;
      }
      return left;
    }
    function parseUnary() {
      var tk = peek();
      if (tk && tk.t === '-') { pos++; var u = parseUnary(); return function (x, sc) { return -u(x, sc); }; }
      if (tk && tk.t === '+') { pos++; return parseUnary(); }
      return parsePower();
    }
    function parsePower() {
      var base = parsePrimary();
      if (peek() && peek().t === '^') {
        pos++; var ex = parseUnary();            // luỹ thừa kết hợp phải: 2^3^2 = 2^(3^2); 2^-x hợp lệ
        return function (x, sc) { return Math.pow(base(x, sc), ex(x, sc)); };
      }
      return base;
    }
    function parsePrimary() {
      var tk = peek();
      if (!tk) throw new Error('Biểu thức kết thúc đột ngột: ' + src);
      if (tk.t === 'num') { pos++; var v = tk.v; return function () { return v; }; }
      if (tk.t === '(') { pos++; var inner = parseExpr(); eat(')'); return inner; }
      if (tk.t === 'id') {
        pos++; var name = tk.v, lname = name.toLowerCase();
        if (peek() && peek().t === '(' && (FUNCS[lname] || lname === 'log' || lname === 'pow' || lname === 'min' || lname === 'max' || lname === 'root')) {
          pos++; var args = [parseExpr()];
          while (peek() && peek().t === ',') { pos++; args.push(parseExpr()); }
          eat(')');
          if (lname === 'log') {                  // log(x) = lg x (cơ số 10); log(a, x) = log_a x
            if (args.length === 1) return function (x, sc) { return Math.log10(args[0](x, sc)); };
            return function (x, sc) { return Math.log(args[1](x, sc)) / Math.log(args[0](x, sc)); };
          }
          if (lname === 'pow') return function (x, sc) { return Math.pow(args[0](x, sc), args[1](x, sc)); };
          if (lname === 'min') return function (x, sc) { return Math.min(args[0](x, sc), args[1](x, sc)); };
          if (lname === 'max') return function (x, sc) { return Math.max(args[0](x, sc), args[1](x, sc)); };
          if (lname === 'root') return function (x, sc) { var n = args[0](x, sc), a = args[1](x, sc); return (a < 0 && Math.abs(n % 2) === 1) ? -Math.pow(-a, 1 / n) : Math.pow(a, 1 / n); };
          var fn = FUNCS[lname]; return function (x, sc) { return fn(args[0](x, sc)); };
        }
        if (name === 'x') return function (x) { return x; };
        if (pset[name]) return function (x, sc) { return sc[name]; };
        if (CONSTS.hasOwnProperty(lname)) { var cv = CONSTS[lname]; return function () { return cv; }; }
        throw new Error('Biến hoặc hàm không xác định "' + name + '" trong biểu thức: ' + src);
      }
      throw new Error('Không đọc được biểu thức: ' + src);
    }
    var f = parseExpr();
    if (pos < toks.length) throw new Error('Thừa ký hiệu trong biểu thức: ' + src);
    return function (x, scope) { return f(x, scope || {}); };
  }

  /* ---------- 2. Lấy mẫu có ngắt nhánh ---------- */
  function fin(v) { return typeof v === 'number' && isFinite(v); }

  /* Kiểm tra giữa x0 và x1 hàm có thực sự gián đoạn không (hay chỉ dốc đứng): chia đôi về phía có bước nhảy lớn hơn. */
  function breakAt(f, x0, y0, x1, y1, thr) {      // vị trí gián đoạn trong (x0, x1) hoặc null nếu hàm chỉ dốc
    var a = x0, b = x1, ya = y0, yb = y1;
    for (var k = 0; k < 48; k++) {
      var m = (a + b) / 2, ym = f(m);
      if (!fin(ym)) return m;                     // điểm không xác định nằm giữa: ngắt
      if (Math.abs(ya - ym) >= Math.abs(ym - yb)) { b = m; yb = ym; } else { a = m; ya = ym; }
      if (Math.abs(yb - ya) <= thr) return null;  // bước nhảy co lại: hàm liên tục (chỉ dốc)
    }
    return Math.abs(yb - ya) > thr ? (a + b) / 2 : null;
  }
  function isBreak(f, x0, y0, x1, y1, thr) { return breakAt(f, x0, y0, x1, y1, thr) !== null; }

  /* Trả về { x: [...], y: [...] }, các nhánh cách nhau bằng NaN (thư viện vẽ bỏ qua NaN nên không nối qua tiệm cận). */
  function plotPieces(f, xmin, xmax, ymin, ymax, n) {
    var X = [], Y = [];
    if (!(xmax > xmin)) return { x: [NaN], y: [NaN] };
    var H = Math.max(ymax - ymin, 1e-9), thr = H * 0.01, lim = H * 1e4, ymid = (ymax + ymin) / 2;   // ngưỡng ≈ vài điểm ảnh: bước nhảy lớn hơn mới kiểm tra
    var step = (xmax - xmin) / n, px = null, py = null, havePrev = false;
    function push(x, y) { X.push(x); Y.push(y); }
    for (var i = 0; i <= n; i++) {
      var x = i === n ? xmax : xmin + i * step, y = f(x);
      if (!fin(y)) { if (havePrev) push(NaN, NaN); havePrev = false; continue; }
      y = Math.max(ymid - lim, Math.min(ymid + lim, y));
      if (havePrev && Math.abs(y - py) > thr && isBreak(f, px, py, x, y, thr)) { push(NaN, NaN); }
      push(x, y); px = x; py = y; havePrev = true;
    }
    if (!X.length) return { x: [NaN], y: [NaN] };
    return { x: X, y: Y };
  }

  /* ---------- 3. Điểm đặc biệt ---------- */
  function bisect(g, a, b, ga, gb, iters) {
    for (var k = 0; k < (iters || 80); k++) {
      var m = (a + b) / 2, gm = g(m);
      if (!fin(gm)) return null;
      if (gm === 0) return m;
      if ((ga < 0) === (gm < 0)) { a = m; ga = gm; } else { b = m; gb = gm; }
    }
    return (a + b) / 2;
  }
  function continuousAt(f, x, scale) {
    var y = f(x); if (!fin(y)) return false;
    var d = 1e-7 * Math.max(1, Math.abs(x)), tol = 1e-4 * (1 + Math.abs(y)) + 1e-9 * scale;
    var l = f(x - d), r = f(x + d);
    return fin(l) && fin(r) && Math.abs(l - y) < tol && Math.abs(r - y) < tol;
  }
  function dedupe(arr, eps) {
    arr.sort(function (a, b) { return a - b; });
    return arr.filter(function (v, i) { return i === 0 || Math.abs(v - arr[i - 1]) > eps; });
  }

  function roots(f, a, b, n) {
    n = n || 6000; var out = [], step = (b - a) / n, px = a, py = f(a);
    var ys = [py], xs = [px];
    for (var i = 1; i <= n; i++) { var x = a + i * step, y = f(x); xs.push(x); ys.push(y); }
    for (i = 0; i < n; i++) {
      var y0 = ys[i], y1 = ys[i + 1];
      if (!fin(y0) || !fin(y1)) continue;
      if (y0 === 0) { out.push(xs[i]); continue; }
      if ((y0 < 0) !== (y1 < 0) && y1 !== 0) {
        var r = bisect(f, xs[i], xs[i + 1], y0, y1);
        if (r !== null && fin(f(r)) && Math.abs(f(r)) < 1e-6 * (1 + Math.abs(y0) + Math.abs(y1))) out.push(r);   // loại đổi dấu qua tiệm cận
      }
    }
    for (i = 1; i < n; i++) {                      // nghiệm kép (chạm trục): cực tiểu của |f| xấp xỉ 0
      var a0 = Math.abs(ys[i - 1]), a1 = Math.abs(ys[i]), a2 = Math.abs(ys[i + 1]);
      if (fin(a0) && fin(a1) && fin(a2) && a1 <= a0 && a1 <= a2 && a1 < 1e-2 && a1 > 0) {
        var lo = xs[i - 1], hi = xs[i + 1];
        for (var k = 0; k < 100; k++) { var m1 = lo + (hi - lo) / 3, m2 = hi - (hi - lo) / 3; if (Math.abs(f(m1)) < Math.abs(f(m2))) hi = m2; else lo = m1; }
        var xm = (lo + hi) / 2; if (Math.abs(f(xm)) < 1e-9) out.push(xm);
      }
    }
    return dedupe(out, (b - a) * 1e-6);
  }

  function intersections(f, g, a, b) { return roots(function (x) { return f(x) - g(x); }, a, b).filter(function (x) { return fin(f(x)) && fin(g(x)); }); }

  function deriv(f, x) {
    var h = 1e-4 * Math.max(1, Math.abs(x));
    return (8 * (f(x + h) - f(x - h)) - (f(x + 2 * h) - f(x - 2 * h))) / (12 * h);
  }
  function deriv2(f, x) { var h = 1e-3 * Math.max(1, Math.abs(x)); return (f(x + h) - 2 * f(x) + f(x - h)) / (h * h); }

  /* Quét đổi dấu của g (bỏ qua giá trị quá nhỏ) rồi chia đôi trong đoạn giữa hai mẫu có dấu ngược nhau. */
  function signChanges(g, a, b, n, eps) {
    var out = [], step = (b - a) / n, lastX = null, lastS = 0;
    for (var i = 0; i <= n; i++) {
      var x = a + i * step, v = g(x);
      if (!fin(v)) { lastS = 0; lastX = null; continue; }
      var s = Math.abs(v) < eps ? 0 : (v > 0 ? 1 : -1);
      if (s === 0) continue;
      if (lastS !== 0 && s !== lastS) {
        var gl = g(lastX), r = bisect(g, lastX, x, gl, v);
        if (r !== null) out.push({ x: r, from: lastS, to: s });
      }
      lastS = s; lastX = x;
    }
    return out;
  }

  function extrema(f, a, b, n) {
    n = n || 6000;
    return signChanges(function (x) { return deriv(f, x); }, a, b, n, 1e-7)
      .filter(function (c) { return continuousAt(f, c.x, b - a); })
      .map(function (c) { return { x: c.x, y: f(c.x), kind: c.from > 0 ? 'max' : 'min' }; });
  }
  function inflections(f, a, b, n) {
    n = n || 4000;
    return signChanges(function (x) { return deriv2(f, x); }, a, b, n, 1e-5)
      .filter(function (c) { return continuousAt(f, c.x, b - a); })
      .map(function (c) { return { x: c.x, y: f(c.x) }; });
  }
  /* Các đoạn liên tục của f trên [a, b]: cắt tại điểm không xác định (ngoài tập xác định, tiệm cận) và tại bước nhảy.
     Trả về [{from, to}] đã thu hẹp vào phần f xác định; bước nhảy được chia đôi để biết đúng vị trí gián đoạn. */
  function continuousPieces(f, a, b, n) {
    n = n || 2000; var step = (b - a) / n, out = [], start = null, px = null, py = null, i, x, y;
    var ys = []; for (i = 0; i <= n; i++) ys.push(f(a + i * step));
    var fin2 = ys.filter(fin), H = fin2.length ? Math.max(Math.max.apply(null, fin2) - Math.min.apply(null, fin2), 1e-9) : 1, thr = H * 0.02;
    function edge(lo, hi) {                         // biên của miền xác định giữa lo (không xác định) và hi (xác định)
      for (var k = 0; k < 60; k++) { var m = (lo + hi) / 2; if (fin(f(m))) hi = m; else lo = m; }
      return hi;
    }
    function edgeR(lo, hi) {                        // lo xác định, hi không xác định
      for (var k = 0; k < 60; k++) { var m = (lo + hi) / 2; if (fin(f(m))) lo = m; else hi = m; }
      return lo;
    }
    for (i = 0; i <= n; i++) {
      x = a + i * step; y = ys[i];
      if (!fin(y)) { if (start !== null) { out.push({ from: start, to: edgeR(px, x) }); start = null; } px = null; continue; }
      if (start === null) start = (i === 0) ? x : edge(a + (i - 1) * step, x);
      else if (Math.abs(y - py) > thr) { var bx = breakAt(f, px, py, x, y, thr); if (bx !== null) { out.push({ from: start, to: bx }); start = bx; } }
      px = x; py = y;
    }
    if (start !== null) out.push({ from: start, to: px });
    return out.filter(function (p) { return p.to - p.from > step * 1e-3; });
  }

  /* Khoảng đồng biến / nghịch biến trên [a, b]: cắt tại cực trị và tại điểm gián đoạn, chiều biến thiên lấy theo
     hiệu f(đầu) − f(cuối) của từng khoảng (đúng cả khi đạo hàm triệt tiêu mà không đổi dấu, như x³), rồi gộp khoảng liền kề cùng chiều
     nếu giữa chúng f liên tục. */
  function monotoneIntervals(f, a, b, n) {
    var pieces = continuousPieces(f, a, b), out = [];
    pieces.forEach(function (pc) {
      var ex = extrema(f, pc.from, pc.to, n).map(function (e) { return e.x; }).filter(function (x) { return x > pc.from + 1e-9 && x < pc.to - 1e-9; });
      var cuts = [pc.from].concat(ex).concat([pc.to]), seg = [];
      for (var i = 0; i < cuts.length - 1; i++) {
        var lo = cuts[i], hi = cuts[i + 1], e = (hi - lo) * 1e-6, yl = f(lo + e), yh = f(hi - e);
        if (!fin(yl) || !fin(yh) || Math.abs(yh - yl) < 1e-12) continue;
        var up = yh > yl;
        if (seg.length && seg[seg.length - 1].up === up && seg[seg.length - 1].to === lo) seg[seg.length - 1].to = hi;
        else seg.push({ from: lo, to: hi, up: up });
      }
      out = out.concat(seg);
    });
    return out;
  }

  /* ---------- 3b. Bội của nghiệm, lỗ thủng ---------- */
  /* Bội m của nghiệm x0: |f(x0 ± d)| ≈ c·d^m. Ước lượng m từ tỉ số tại hai bán kính d và d/2 (lấy phía có |f| lớn hơn),
     làm tròn đến số nguyên 1..6; crosses = f đổi dấu qua x0 (bội lẻ). */
  function rootMultiplicity(f, x0) {
    var best = 1, bestErr = Infinity;
    [0.02, 0.01, 0.005].forEach(function (d0) {
      var d = d0 * Math.max(1, Math.abs(x0)), vals = [];
      [-1, 1].forEach(function (sg) { var u = Math.abs(f(x0 + sg * d)), w = Math.abs(f(x0 + sg * d / 2)); if (fin(u) && fin(w) && u > 0 && w > 0) vals.push(Math.log(u / w) / Math.LN2); });
      vals.forEach(function (m) { var r = Math.max(1, Math.min(6, Math.round(m))), e = Math.abs(m - r); if (e < bestErr) { bestErr = e; best = r; } });
    });
    var d1 = 1e-3 * Math.max(1, Math.abs(x0)), l = f(x0 - d1), r2 = f(x0 + d1);
    return { mult: best, crosses: fin(l) && fin(r2) && (l < 0) !== (r2 < 0) };
  }
  function rootsDetailed(f, a, b, n) {
    return roots(f, a, b, n).map(function (x) { var m = rootMultiplicity(f, x); return { x: x, mult: m.mult, crosses: m.crosses }; });
  }

  /* Lỗ thủng (gián đoạn bỏ được): f không xác định tại x0 nhưng giới hạn hai phía hữu hạn và bằng nhau.
     Ứng viên: các điểm "đẹp" (bội của 1/12 và của π/12) và các điểm không xác định cô lập trên lưới lấy mẫu. */
  function holes(f, a, b, n) {
    var cand = [], i, k, x;
    for (k = Math.ceil(a * 12); k <= Math.floor(b * 12); k++) cand.push(k / 12);
    for (k = Math.ceil(a / Math.PI * 12); k <= Math.floor(b / Math.PI * 12); k++) cand.push(k * Math.PI / 12);
    n = n || 2000; var step = (b - a) / n;
    for (i = 1; i < n; i++) { x = a + i * step; if (!fin(f(x))) cand.push(x); }
    var out = [];
    cand.forEach(function (c) {
      if (fin(f(c))) return;
      var ds = [1e-4, 1e-5, 1e-6], L = [], R = [];
      ds.forEach(function (d) { d *= Math.max(1, Math.abs(c)); L.push(f(c - d)); R.push(f(c + d)); });
      var all = L.concat(R); if (!all.every(fin)) return;
      var lim = (L[2] + R[2]) / 2, tol = 1e-3 * (1 + Math.abs(lim));
      if (Math.abs(L[2] - R[2]) < tol && Math.abs(L[1] - L[2]) < tol && Math.abs(R[1] - R[2]) < tol) out.push({ x: c, y: lim });
    });
    out.sort(function (p, q) { return p.x - q.x; });
    return out.filter(function (h, j) { return j === 0 || Math.abs(h.x - out[j - 1].x) > (b - a) * 1e-6; });
  }

  /* Kiểm tra một đường tiệm cận khai báo có đúng với hàm không (dùng trong kiểm thử bài học). */
  function checkAsymptote(f, a) {
    var BIG = 1e7;
    if (a.type === 'v') {
      var l = Math.abs(f(a.x - 1e-7)), r = Math.abs(f(a.x + 1e-7)), l2 = Math.abs(f(a.x - 1e-9)), r2 = Math.abs(f(a.x + 1e-9));
      return (fin(l) && l > 1e3 && l2 > l * 1.5) || (fin(r) && r > 1e3 && r2 > r * 1.5);
    }
    var side = [BIG, -BIG].map(function (X) {
      var y = f(X), y2 = f(2 * X); if (!fin(y) || !fin(y2)) return null;
      if (a.type === 'h') return Math.abs(y - a.y) < 1e-3 * (1 + Math.abs(a.y)) && Math.abs(y2 - a.y) < 1e-3 * (1 + Math.abs(a.y));
      var tol = 1e-3 * (1 + Math.abs(a.b || 0));   // sai số tuyệt đối: khác nhau 1 đơn vị là sai
      return Math.abs(y - ((a.m || 0) * X + (a.b || 0))) < tol && Math.abs(y2 - ((a.m || 0) * 2 * X + (a.b || 0))) < tol;
    });
    return side.some(function (v) { return v === true; });
  }

  /* ---------- 3c. Hình khối: bao lồi, mặt, cạnh, nét khuất ---------- */
  function sub3(a, b) { return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]; }
  function cross3(a, b) { return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]; }
  function dot3(a, b) { return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]; }
  function norm3(a) { return Math.sqrt(dot3(a, a)); }

  /* Bao lồi của các điểm {tên: [x, y, z]} (số điểm nhỏ, ≤ ~20): trả về
       faces: [{ names: [tên đỉnh theo thứ tự quanh mặt], n: pháp tuyến đơn vị HƯỚNG RA NGOÀI, c: tâm mặt }]
       edges: [{ a, b, faces: [chỉ số mặt kề] }]  (mỗi cạnh của khối kề đúng 2 mặt).
     Mặt phẳng nhận được khi mọi điểm còn lại nằm cùng một phía; các điểm đồng phẳng gộp thành một mặt (đáy hình chóp, mặt hộp...). */
  function hull3d(pts) {
    var names = Object.keys(pts), n = names.length, i, j, k, m;
    var size = 0; names.forEach(function (a) { names.forEach(function (b) { size = Math.max(size, norm3(sub3(pts[a], pts[b]))); }); });
    var eps = 1e-9 * Math.max(1, size), cen = [0, 0, 0];
    names.forEach(function (a) { for (var t = 0; t < 3; t++) cen[t] += pts[a][t] / n; });
    var faces = {};
    for (i = 0; i < n; i++) for (j = i + 1; j < n; j++) for (k = j + 1; k < n; k++) {
      var nrm = cross3(sub3(pts[names[j]], pts[names[i]]), sub3(pts[names[k]], pts[names[i]])), len = norm3(nrm);
      if (len < eps * Math.max(1, size)) continue;                     // thẳng hàng
      nrm = [nrm[0] / len, nrm[1] / len, nrm[2] / len];
      var pos = 0, neg = 0, on = [];
      for (m = 0; m < n; m++) { var d = dot3(nrm, sub3(pts[names[m]], pts[names[i]])); if (Math.abs(d) <= eps * Math.max(1, size) * 10) on.push(names[m]); else if (d > 0) pos++; else neg++; }
      if (pos && neg) continue;                                        // không phải mặt phẳng tựa
      if (pos) nrm = [-nrm[0], -nrm[1], -nrm[2]];                      // hướng ra ngoài: các điểm còn lại ở phía −n
      var key = on.slice().sort().join('|');
      if (!faces[key]) faces[key] = { names: on, n: nrm };
    }
    var list = Object.keys(faces).map(function (key) { return faces[key]; });
    list.forEach(function (f) {
      var c = [0, 0, 0]; f.names.forEach(function (a) { for (var t = 0; t < 3; t++) c[t] += pts[a][t] / f.names.length; }); f.c = c;
      var u = sub3(pts[f.names[0]], c), uu = norm3(u); u = [u[0] / uu, u[1] / uu, u[2] / uu];
      var w = cross3(f.n, u);                                          // (u, w, n) thuận chiều: sắp xếp ngược chiều kim đồng hồ khi nhìn từ ngoài vào
      f.names.sort(function (p, q) {
        var dp = sub3(pts[p], c), dq = sub3(pts[q], c);
        return Math.atan2(dot3(dp, w), dot3(dp, u)) - Math.atan2(dot3(dq, w), dot3(dq, u));
      });
    });
    var emap = {};
    list.forEach(function (f, fi) {
      for (var t = 0; t < f.names.length; t++) {
        var a = f.names[t], b = f.names[(t + 1) % f.names.length], key = a < b ? a + '|' + b : b + '|' + a;
        (emap[key] = emap[key] || { a: a, b: b, faces: [] }).faces.push(fi);
      }
    });
    return { faces: list, edges: Object.keys(emap).map(function (key) { return emap[key]; }) };
  }

  /* Hướng nhìn: vector đơn vị (hệ tọa độ thế giới) từ vật THỂ hướng về phía NGƯỜI XEM, suy ra từ ánh xạ chiếu project(p) → [sx, sy]
     (phép chiếu song song: hai hàng của ma trận chiếu cho hai trục màn hình; tích có hướng của chúng vuông góc màn hình).
     Dấu +/− không thể suy ra từ riêng phép chiếu, nên chuẩn hóa bằng sign: lần đầu gọi (sign = 0) chọn dấu sao cho người xem ở PHÍA TRÊN
     (thành phần z > 0), vì khung 3D luôn khởi tạo nhìn từ trên xuống; trả về {v, sign} để các lần sau (khi người học xoay) dùng cùng dấu. */
  function viewDirection(project, center, h, sign) {
    h = h || 1e-3; var c = center || [0, 0, 0], o = project(c), r = [[0, 0, 0], [0, 0, 0]];
    for (var t = 0; t < 3; t++) { var q = c.slice(); q[t] += h; var pq = project(q); r[0][t] = (pq[0] - o[0]) / h; r[1][t] = (pq[1] - o[1]) / h; }
    var v = cross3(r[0], r[1]), L = norm3(v); if (L < 1e-12) return { v: [0, 0, 1], sign: sign || 1 };
    v = [v[0] / L, v[1] / L, v[2] / L];
    if (!sign) sign = v[2] >= 0 ? 1 : -1;
    return { v: [v[0] * sign, v[1] * sign, v[2] * sign], sign: sign };
  }

  /* Cạnh nào bị che (nét đứt): cạnh khuất khi mọi mặt kề đều quay lưng về phía người xem (n·v ≤ 0). Mặt nhìn nghiêng đúng cạnh (n·v ≈ 0) coi như quay lưng. */
  function hiddenEdges(hull, v) {
    var eps = 1e-9;
    return hull.edges.map(function (e) { return e.faces.every(function (fi) { return dot3(hull.faces[fi].n, v) <= eps; }); });
  }

  /* ---------- 4. Định dạng ---------- */
  function fmt(v, digits) {
    digits = digits == null ? 3 : digits;
    if (Math.abs(v) < 1e-9) return '0';
    var s = (+v.toFixed(digits)).toString().replace('-', '\u2212');
    return s;
  }
  function gcd(a, b) { a = Math.abs(a); b = Math.abs(b); while (b) { var t = a % b; a = b; b = t; } return a; }
  /* Nhãn bội của π: 0, π/2, π, 3π/2, 2π, −π/3 ... (mẫu số 1, 2, 3, 4, 6, 12); không khớp thì trả về số thập phân. */
  function formatPi(v) {
    if (Math.abs(v) < 1e-9) return '0';
    var dens = [1, 2, 3, 4, 6, 12];
    for (var i = 0; i < dens.length; i++) {
      var d = dens[i], k = v / Math.PI * d;
      if (Math.abs(k - Math.round(k)) < 1e-6) {
        var num = Math.round(k), g = gcd(num, d); num /= g; var den = d / g, sign = num < 0 ? '\u2212' : '', an = Math.abs(num);
        var top = an === 1 ? '\u03c0' : an + '\u03c0';
        return sign + (den === 1 ? top : top + '/' + den);
      }
    }
    return fmt(v);
  }

  return { compile: compile, plotPieces: plotPieces, isBreak: isBreak, roots: roots, intersections: intersections,
           deriv: deriv, deriv2: deriv2, extrema: extrema, inflections: inflections, monotoneIntervals: monotoneIntervals, continuousPieces: continuousPieces,
           hull3d: hull3d, viewDirection: viewDirection, hiddenEdges: hiddenEdges,
           rootMultiplicity: rootMultiplicity, rootsDetailed: rootsDetailed, holes: holes, checkAsymptote: checkAsymptote,
           fmt: fmt, formatPi: formatPi, signChanges: signChanges };
});
