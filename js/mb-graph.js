/* MathBridge – hệ thống biểu diễn đồ thị và hình vẽ Toán học.
   Mỗi hình là một khối  <div class="mbg" data-mbg='{...JSON...}'>  do tools/mb_lib.py (GRAPH/GEO/GEO3D) sinh ra.
   Công nghệ: JSXGraph (đồ thị, hình học, 3D). Tùy chọn engine "geogebra" / "desmos" cho hình phức tạp.
   Toán học (đọc biểu thức, ngắt nhánh tại tiệm cận, nghiệm, cực trị, điểm uốn) nằm ở js/mb-graph-core.js.
   Mô tả cấu hình: docs/GRAPH.md. */
(function () {
  'use strict';
  var Core = window.MBGCore;
  var PALETTE = ['#046b4d', '#c2410c', '#1d4ed8', '#7c3aed', '#be185d', '#0e7490'];
  var INK = '#123428', GRIDC = '#cfe9dd', UP = '#0a8f63', DOWN = '#c2410c';
  var uid = 0, registry = [];

  /* ---------- Chữ trên nút (đổi theo mức học: Mức 3 = English) ---------- */
  var TXT = {
    zin: ['Zoom in', 'Phóng to'], zout: ['Zoom out', 'Thu nhỏ'], reset: ['Reset view', 'Đặt lại khung nhìn'],
    eq: ['Equal scale on both axes (1:1)', 'Cùng tỉ lệ hai trục (1:1)'],
    xp: ['Stretch the x-axis', 'Giãn trục x'], xm: ['Shrink the x-axis', 'Co trục x'],
    yp: ['Stretch the y-axis', 'Giãn trục y'], ym: ['Shrink the y-axis', 'Co trục y'],
    hint: ['Drag to move. Shift + scroll or pinch to zoom.', 'Kéo để di chuyển. Shift + cuộn chuột hoặc chụm hai ngón để thu phóng.'],
    hintGeo: ['Drag the points: the relationships stay true.', 'Kéo các điểm: các quan hệ hình học vẫn luôn đúng.'],
    hint3d: ['Drag to rotate the figure.', 'Kéo để xoay hình.'],
    nolib: ['The graph library could not be loaded. Check your Internet connection and reload the page.', 'Không tải được thư viện vẽ đồ thị. Hãy kiểm tra kết nối Internet rồi tải lại trang.'],
    err: ['This figure could not be drawn: ', 'Không vẽ được hình này: '],
    no3d: ['3D figures need a newer version of the graph library.', 'Hình không gian cần phiên bản thư viện đồ thị mới hơn.'],
    nokey: ['Desmos needs an API key (see docs/GRAPH.md).', 'Desmos cần khóa API (xem docs/GRAPH.md).'],
    up: ['increasing', 'đồng biến'], down: ['decreasing', 'nghịch biến'],
    tp: ['Tangent at the point', 'Tiếp tuyến tại điểm']
  };
  function level() { return parseInt(document.body.getAttribute('data-level'), 10) || 1; }
  function tx(k) { var p = TXT[k]; return level() === 3 ? p[0] : p[1]; }
  function localize() {
    registry.forEach(function (g) {
      [].forEach.call(g.host.querySelectorAll('[data-k]'), function (b) { var t = tx(b.getAttribute('data-k')); b.title = t; b.setAttribute('aria-label', t); });
      var h = g.host.querySelector('.mbg-hint'); if (h) h.textContent = tx(h.getAttribute('data-k'));
    });
  }
  if (window.MutationObserver) new MutationObserver(localize).observe(document.body, { attributes: true, attributeFilter: ['data-level'] });

  /* ---------- Tiện ích ---------- */
  function el(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function showError(g, e) {
    console.error('[MBG]', e);
    var box = el('div', 'mbg-error'); box.setAttribute('role', 'alert');
    box.textContent = tx('err') + (e && e.message ? e.message : e);
    g.stage.innerHTML = ''; g.stage.appendChild(box);
  }
  function loadScript(src, cb, onerr) {
    var s = document.createElement('script'); s.src = src; s.async = true; s.onload = cb; s.onerror = onerr || function () {};
    document.head.appendChild(s);
  }
  function pt(x, y, cfg) { return '(' + (cfg.pi ? Core.formatPi(x) : Core.fmt(x)) + '; ' + Core.fmt(y) + ')'; }

  /* ---------- Thanh công cụ ---------- */
  function toolbar(g, withScale) {
    var bar = el('div', 'mbg-tools'); bar.setAttribute('role', 'toolbar');
    function btn(k, sym, fn) {
      var b = el('button', 'mbg-btn', sym); b.type = 'button'; b.setAttribute('data-k', k);
      b.addEventListener('click', function () { try { fn(); } catch (e) { console.error(e); } });
      bar.appendChild(b);
    }
    function bb() { return g.board.getBoundingBox(); }
    function scale(fx, fy) {                      // phóng/thu quanh tâm khung nhìn
      var b = bb(), cx = (b[0] + b[2]) / 2, cy = (b[1] + b[3]) / 2, hw = (b[2] - b[0]) / 2 * fx, hh = (b[1] - b[3]) / 2 * fy;
      g.board.setBoundingBox([cx - hw, cy + hh, cx + hw, cy - hh], false);
    }
    btn('zin', '＋', function () { scale(1 / 1.25, 1 / 1.25); });
    btn('zout', '－', function () { scale(1.25, 1.25); });
    if (withScale) {
      btn('xp', '↔＋', function () { scale(1 / 1.25, 1); });
      btn('xm', '↔－', function () { scale(1.25, 1); });
      btn('yp', '↕＋', function () { scale(1, 1 / 1.25); });
      btn('ym', '↕－', function () { scale(1, 1.25); });
      btn('eq', '1:1', function () {
        var b = bb(), w = g.board.canvasWidth, h = g.board.canvasHeight, ppu = w / (b[2] - b[0]), cy = (b[1] + b[3]) / 2, hh = h / ppu / 2;
        g.board.setBoundingBox([b[0], cy + hh, b[2], cy - hh], false);
      });
    }
    btn('reset', '⟲', function () { g.board.setBoundingBox(g.home.slice(), false); });
    g.tools = bar; return bar;
  }

  /* ---------- Khởi tạo bảng vẽ ---------- */
  function initBoard(g, cfg, opts) {
    var v = cfg.view || [-6, 6, -5, 5];
    var attrs = {
      boundingbox: [v[0], v[3], v[1], v[2]], axis: !!opts.axis, grid: opts.axis && cfg.grid !== false,
      showCopyright: false, showNavigation: false, keepAspectRatio: !!cfg.equal,
      pan: { enabled: true, needTwoFingers: true }, zoom: { enabled: true, wheel: true, needShift: true, pinch: true, factorX: 1.2, factorY: 1.2 },
      resize: { enabled: true, throttle: 10 }
    };
    if (opts.axis) {
      attrs.defaultAxes = {
        x: { name: cfg.xname || 'x', withLabel: true, strokeColor: INK, strokeWidth: 1.8, highlight: false, lastArrow: { type: 2, size: 7 },
             label: { position: 'rt', offset: [-6, 14], fontSize: 15, strokeColor: INK }, ticks: { strokeColor: '#4b6b5c', label: { fontSize: 12, offset: [0, -11] } } },
        y: { name: cfg.yname || 'y', withLabel: true, strokeColor: INK, strokeWidth: 1.8, highlight: false, lastArrow: { type: 2, size: 7 },
             label: { position: 'rt', offset: [12, -6], fontSize: 15, strokeColor: INK }, ticks: { strokeColor: '#4b6b5c', label: { fontSize: 12, offset: [-10, 0] } } }
      };
    }
    var board = JXG.JSXGraph.initBoard(g.boardId, attrs);
    g.board = board; g.home = [v[0], v[3], v[1], v[2]];
    try { (board.grids || []).forEach(function (gr) { gr.setAttribute({ strokeColor: GRIDC, strokeOpacity: 1, strokeWidth: 1 }); }); } catch (e) { /* kiểu lưới mặc định vẫn dùng được */ }
    if (opts.axis && cfg.pi) {                        // trục x chia theo bội của π
      try {
        var xt = board.defaultAxes.x.defaultTicks;
        xt.setAttribute({ scale: Math.PI, scaleSymbol: '\u03c0', ticksDistance: 0.5, insertTicks: false, minorTicks: 0 });
        xt.generateLabelText = function (tick, zero, value) { var d = tick.usrCoords[1] - zero.usrCoords[1]; return Math.abs(d) < 1e-9 ? '' : Core.formatPi(d); };
      } catch (e) { console.warn('[MBG] không đổi được nhãn π của trục', e); }
    }
    return board;
  }

  /* ---------- Đồ thị hàm số ---------- */
  function drawGraph(g, cfg) {
    var board = initBoard(g, cfg, { axis: true }), scope = {}, params = cfg.params || [], names = params.map(function (p) { return p.name; });
    params.forEach(function (p) { scope[p.name] = p.value; });
    var fns = (cfg.functions || []).map(function (spec, i) {
      var comp = Core.compile(spec.f, names), color = spec.color || PALETTE[i % PALETTE.length];
      var f = function (x) { return comp(x, scope); };
      return { spec: spec, f: f, color: color, i: i };
    });
    function viewRange() { var b = board.getBoundingBox(); return [b[0], b[2], b[3], b[1]]; }

    function curveOf(f, color, width, dash, dom, extra) {
      var c = board.create('curve', [[0], [0]], Object.assign({ strokeColor: color, strokeWidth: width, dash: dash || 0, highlight: false, fixed: true, withLabel: false, lineCap: 'round' }, extra || {}));
      c.updateDataArray = function () {
        var r = viewRange(), lo = Math.max(r[0], dom ? dom[0] : -Infinity), hi = Math.min(r[1], dom ? dom[1] : Infinity);
        var out = Core.plotPieces(f, lo, hi, r[2], r[3], Math.max(400, Math.min(2400, Math.round((board.canvasWidth || 600) * 1.5))));
        this.dataX = out.x; this.dataY = out.y;
      };
      return c;
    }
    function dot(x, y, o) {
      o = o || {};
      return board.create('point', [x, y], { name: o.name || '', size: o.size || 3.5, face: 'o', fillColor: o.open ? '#fff' : (o.color || INK), strokeColor: o.color || INK, strokeWidth: 2, fixed: true,
        highlight: false, withLabel: !!o.name, label: { offset: o.off || [7, -13], fontSize: 13, strokeColor: INK } });
    }

    fns.forEach(function (F) {
      var s = F.spec, dom = s.domain || null;
      curveOf(F.f, F.color, s.width || 2.6, s.dash ? 2 : 0, dom);
      if (dom && s.open) {                            // đầu mút hở (○) hoặc đặc (●) của miền xác định
        [0, 1].forEach(function (k) { var x = dom[k], y = F.f(x); if (isFinite(y)) dot(x, y, { open: !!s.open[k], color: F.color }); });
      }
    });

    (cfg.asymptotes || []).forEach(function (a) {
      var o = { strokeColor: a.color || '#475569', strokeWidth: 1.6, dash: 2, fixed: true, highlight: false, straightFirst: true, straightLast: true };
      if (a.type === 'v') board.create('line', [[a.x, 0], [a.x, 1]], o);
      else if (a.type === 'h') board.create('line', [[0, a.y], [1, a.y]], o);
      else board.create('line', [[0, a.b || 0], [1, (a.m || 0) + (a.b || 0)]], o);
    });
    (cfg.guides || []).forEach(function (a) {          // đường dóng tham khảo (ví dụ giá trị giới hạn): KHÔNG phải tiệm cận nên nét mảnh, chấm
      var o = { strokeColor: a.color || '#94a3b8', strokeWidth: 1.2, dash: 1, fixed: true, highlight: false, straightFirst: true, straightLast: true };
      if (a.type === 'v') board.create('line', [[a.x, 0], [a.x, 1]], o); else board.create('line', [[0, a.y], [1, a.y]], o);
    });
    (cfg.holes || []).forEach(function (h) { dot(h[0], h[1], { open: true, name: h[2] }); });
    (cfg.points || []).forEach(function (p) {
      dot(p.x, p.y, { name: p.label ? p.label : '', open: p.open, color: p.color, off: p.off });
    });
    (cfg.texts || []).forEach(function (t) { board.create('text', [t.x, t.y, t.text], { fontSize: t.size || 14, strokeColor: t.color || INK, fixed: true, highlight: false }); });

    /* Điểm đặc biệt tính bằng số, TÍNH LẠI theo khung nhìn hiện tại mỗi khi người học kéo, phóng/thu hoặc đổi tham số
       (trước đây chỉ tính một lần theo khung ban đầu nên phóng ra là mất điểm, phóng vào thì thiếu điểm sát nhau).
       mark: roots (kèm bội ×m), yint, extrema, inflections, intersections, holes; monotone: tô khoảng đồng/nghịch biến. */
    var mk = cfg.mark || {}, markEls = [], MAXLABEL = 24;
    function mdot(x, y, o) { var e = dot(x, y, o); markEls.push(e); return e; }
    function clearMarks() { markEls.splice(0).forEach(function (e) { try { board.removeObject(e); } catch (er) { /* đã bị xóa */ } }); }
    function drawMarks() {
      clearMarks();
      var v = viewRange(), mr = cfg.markRange, lo = mr ? Math.max(v[0], mr[0]) : v[0], hi = mr ? Math.min(v[1], mr[1]) : v[1];
      if (!(hi > lo)) return;
      var w = hi - lo, A = lo - 0.02 * w, B = hi + 0.02 * w;           // lề nhỏ để điểm sát mép không bị mất
      var inView = function (x, y) { return x >= v[0] && x <= v[1] && y >= v[2] && y <= v[3]; };
      var label = function (n, x, y, suffix) { return n <= MAXLABEL ? pt(x, y, cfg) + (suffix || '') : ''; };
      (mk.roots || []).forEach(function (fi) {
        var rs = Core.rootsDetailed(fns[fi].f, A, B).filter(function (r) { return inView(r.x, 0); });
        rs.forEach(function (r) { mdot(r.x, 0, { name: label(rs.length, r.x, 0, r.mult > 1 ? ' \u00d7' + r.mult : ''), color: fns[fi].color, size: r.mult > 1 ? 5 : 3.5 }); });
      });
      (mk.yint || []).forEach(function (fi) { var y = fns[fi].f(0); if (isFinite(y) && inView(0, y)) mdot(0, y, { name: pt(0, y, cfg), color: fns[fi].color }); });
      (mk.extrema || []).forEach(function (fi) {
        var es = Core.extrema(fns[fi].f, A, B).filter(function (e) { return inView(e.x, e.y); });
        es.forEach(function (e) { mdot(e.x, e.y, { name: label(es.length, e.x, e.y), color: e.kind === 'max' ? DOWN : '#1d4ed8', off: [7, e.kind === 'max' ? 12 : -14] }); });
      });
      (mk.inflections || []).forEach(function (fi) {
        var ps = Core.inflections(fns[fi].f, A, B).filter(function (q) { return inView(q.x, q.y); });
        ps.forEach(function (q) { mdot(q.x, q.y, { name: label(ps.length, q.x, q.y), color: '#7c3aed', open: true }); });
      });
      (mk.holes || []).forEach(function (fi) {
        Core.holes(fns[fi].f, A, B).filter(function (h) { return inView(h.x, h.y); }).forEach(function (h) { mdot(h.x, h.y, { name: pt(h.x, h.y, cfg), color: fns[fi].color, open: true }); });
      });
      (mk.intersections || []).forEach(function (pr) {
        Core.intersections(fns[pr[0]].f, fns[pr[1]].f, A, B).forEach(function (x) { var y = fns[pr[0]].f(x); if (inView(x, y)) mdot(x, y, { name: pt(x, y, cfg), color: INK }); });
      });
      if (cfg.monotone) {
        var mf = fns[cfg.monotone.f || 0], rg = cfg.monotone.range || [A, B];
        Core.monotoneIntervals(mf.f, Math.max(rg[0], A), Math.min(rg[1], B)).forEach(function (iv) {
          markEls.push(curveOf(mf.f, iv.up ? UP : DOWN, 6, 0, [iv.from, iv.to], { strokeOpacity: 0.45 }));
        });
      }
    }
    var markTimer = null, lastBB = '';
    function scheduleMarks() {                          // gom nhiều sự kiện kéo/phóng thành một lần tính
      if (markTimer) return;
      markTimer = setTimeout(function () { markTimer = null; var k = board.getBoundingBox().map(function (n) { return n.toPrecision(7); }).join(); if (k !== lastBB || scheduleMarks.force) { lastBB = k; scheduleMarks.force = false; drawMarks(); board.update(); } }, 90);
    }
    if (mk.roots || mk.yint || mk.extrema || mk.inflections || mk.intersections || mk.holes || cfg.monotone) {
      drawMarks(); lastBB = board.getBoundingBox().map(function (n) { return n.toPrecision(7); }).join();
      if (board.on) board.on('boundingbox', scheduleMarks);
      g.refreshMarks = function () { scheduleMarks.force = true; scheduleMarks(); };
    }
    (cfg.highlights || []).forEach(function (h) { var F = fns[h.f || 0]; curveOf(F.f, h.color || UP, 6, 0, h.x, { strokeOpacity: 0.45 }); });

    /* Thanh trượt tham số (HTML, truy cập được bằng bàn phím) */
    var side = el('div', 'mbg-side');
    params.forEach(function (p) {
      var row = el('label', 'mbg-slider'), out = el('output', 'mbg-val');
      var inp = el('input'); inp.type = 'range'; inp.min = p.min; inp.max = p.max; inp.step = p.step || 0.1; inp.value = p.value;
      var upd = function () { scope[p.name] = parseFloat(inp.value); out.textContent = p.name + ' = ' + Core.fmt(scope[p.name], 2); if (g.refreshMarks) g.refreshMarks(); board.update(); };
      inp.addEventListener('input', upd); row.appendChild(out); row.appendChild(inp); side.appendChild(row); upd();
    });
    if (cfg.tangent) {                                // tiếp tuyến di động: kéo thanh trượt x₀
      var tf = fns[cfg.tangent.f || 0], tg = cfg.tangent, state = { x0: tg.at };
      var P = board.create('point', [function () { return state.x0; }, function () { return tf.f(state.x0); }], { name: 'M', size: 4, fixed: true, strokeColor: '#c2410c', fillColor: '#c2410c', highlight: false, label: { offset: [8, -14], fontSize: 14 } });
      var Q = board.create('point', [function () { return state.x0 + 1; }, function () { return tf.f(state.x0) + Core.deriv(tf.f, state.x0); }], { visible: false, fixed: true, withLabel: false });
      board.create('line', [P, Q], { strokeColor: '#c2410c', strokeWidth: 2, fixed: true, highlight: false });
      var row = el('label', 'mbg-slider'), out = el('output', 'mbg-val'), inp = el('input');
      inp.type = 'range'; inp.min = tg.min != null ? tg.min : cfg.view[0]; inp.max = tg.max != null ? tg.max : cfg.view[1]; inp.step = tg.step || 0.05; inp.value = tg.at;
      var read = el('output', 'mbg-read'); read.setAttribute('aria-live', 'polite');
      var upd2 = function () {
        state.x0 = parseFloat(inp.value); var y = tf.f(state.x0), k = Core.deriv(tf.f, state.x0);
        out.textContent = 'x\u2080 = ' + Core.fmt(state.x0, 2);
        read.textContent = 'f(x\u2080) = ' + Core.fmt(y, 3) + ';  f\u2032(x\u2080) \u2248 ' + Core.fmt(k, 3);
        board.update();
      };
      inp.addEventListener('input', upd2); row.appendChild(out); row.appendChild(inp); side.appendChild(row); side.appendChild(read); upd2();
    }
    if (cfg.legend !== false) {
      var keys = fns.filter(function (F) { return F.spec.label; });
      if (cfg.monotone) keys.push({ color: UP, spec: { label: tx('up') } }, { color: DOWN, spec: { label: tx('down') } });
      if (keys.length) {
        var lg = el('div', 'mbg-legend');
        keys.forEach(function (F) { lg.appendChild(el('span', 'mbg-key', '<i style="background:' + F.color + '"></i>' + F.spec.label)); });
        g.legend = lg;
      }
    }
    g.side = side; g.hintKey = 'hint';
    toolbar(g, true);
    board.update();
  }

  /* ---------- Hình học phẳng: dựng bằng đúng quan hệ (vuông góc, song song, phân giác...), kéo điểm vẫn đúng ---------- */
  function drawGeo(g, cfg) {
    cfg = Object.assign({ equal: true }, cfg);
    var board = initBoard(g, cfg, { axis: !!cfg.axes });
    var O = {};                                       // tên -> đối tượng
    function ref(n) { if (Array.isArray(n)) return n; if (!O[n]) throw new Error('Chưa có đối tượng "' + n + '"'); return O[n]; }
    function refs(a) { return a.map(ref); }
    function style(st, base) { return Object.assign({ highlight: false }, base || {}, st.style || {}); }
    function name(st, obj) { if (st.id) O[st.id] = obj; return obj; }
    var seg = { strokeColor: '#046b4d', strokeWidth: 2.2 }, aux = { strokeColor: '#c2410c', strokeWidth: 1.8, dash: 2 };
    /* Ký hiệu trên đoạn thẳng theo SGK: gạch nhỏ cắt đoạn (đoạn bằng nhau: |, ||, |||) hoặc mũi tên ›, ›› (đường thẳng song song).
       Kích thước tính theo điểm ảnh nên giữ nguyên khi phóng/thu; vị trí bám theo hai đầu mút khi kéo điểm. */
    function segMarks(sg, spec) {
      var kind = spec.kind, count = spec.count || 1, color = spec.color || '#c2410c';
      var c = board.create('curve', [[0], [0]], { strokeColor: color, strokeWidth: 2, highlight: false, fixed: true, withLabel: false });
      c.updateDataArray = function () {
        var A = sg.point1.coords.usrCoords, B = sg.point2.coords.usrCoords, ux = 1 / (board.unitX || 1), uy = 1 / (board.unitY || 1);
        var dx = (B[1] - A[1]) / ux, dy = (B[2] - A[2]) / uy, L = Math.sqrt(dx * dx + dy * dy), X = [], Y = [];
        if (!(L > 1e-9)) { this.dataX = [NaN]; this.dataY = [NaN]; return; }
        var tx = dx / L, ty = dy / L, nx = -ty, ny = tx, mx = (A[1] + B[1]) / 2 / ux, my = (A[2] + B[2]) / 2 / uy, gap = 5, half = 6;   // px
        function P(px, py) { X.push(px * ux); Y.push(py * uy); }
        for (var i = 0; i < count; i++) {
          var o = (i - (count - 1) / 2) * gap * (kind === 'par' ? 1.4 : 1), cx = mx + tx * o, cy = my + ty * o;
          if (kind === 'par') {                   // mũi tên › hướng theo đoạn (từ điểm đầu đến điểm cuối)
            P(cx - tx * 3 + nx * half, cy - ty * 3 + ny * half); P(cx + tx * 3, cy + ty * 3); P(cx - tx * 3 - nx * half, cy - ty * 3 - ny * half);
          } else { P(cx + nx * half, cy + ny * half); P(cx - nx * half, cy - ny * half); }
          X.push(NaN); Y.push(NaN);
        }
        this.dataX = X; this.dataY = Y;
      };
      return c;
    }

    var cen = (function () { var p = (cfg.steps || []).filter(function (q) { return q.type === 'point' && Array.isArray(q.at); }); return p.length ? [p.reduce(function (a, q) { return a + q.at[0]; }, 0) / p.length, p.reduce(function (a, q) { return a + q.at[1]; }, 0) / p.length] : [0, 0]; })();
    function awayFromCenter(at) {                   // nhãn đẩy ra xa tâm các điểm để khỏi đè lên đoạn thẳng
      var dx = at[0] - cen[0], dy = at[1] - cen[1], L = Math.sqrt(dx * dx + dy * dy);
      return L < 1e-9 ? [8, 8] : [Math.round(dx / L * 11), Math.round(dy / L * 11) + 3];
    }
    (cfg.steps || []).forEach(function (st) {
      var t = st.type, o;
      switch (t) {
        case 'point':
          o = board.create('point', st.at, style(st, { name: st.name != null ? st.name : st.id, size: 3.5, fixed: !!st.fixed, strokeColor: '#046b4d', fillColor: '#046b4d', label: { offset: st.off || awayFromCenter(st.at), fontSize: 15, strokeColor: INK } })); break;
        case 'glider':
          o = board.create('glider', [st.at[0], st.at[1], ref(st.on)], style(st, { name: st.name != null ? st.name : st.id, size: 4, strokeColor: '#c2410c', fillColor: '#c2410c', label: { offset: st.off || [8, 8], fontSize: 15, strokeColor: INK } })); break;
        case 'midpoint':
          o = board.create('midpoint', refs(st.of), style(st, { name: st.name != null ? st.name : st.id, size: 3, strokeColor: '#475569', fillColor: '#475569', label: { offset: st.off || [8, 8], fontSize: 14 } })); break;
        case 'intersection':
          o = board.create('intersection', refs(st.of).concat([st.index || 0]), style(st, { name: st.name != null ? st.name : st.id, size: 3, strokeColor: '#475569', fillColor: '#475569', label: { offset: st.off || [8, 8], fontSize: 14 } })); break;
        case 'segment':
          o = board.create('segment', refs(st.through), style(st, seg));
          if (st.mark) segMarks(o, typeof st.mark === 'string' ? { kind: st.mark === 'par' ? 'par' : 'eq', count: parseInt(st.mark.replace(/\D/g, ''), 10) || 1 } : st.mark);   // 'eq', 'eq2', 'par', 'par2'
          break;
        case 'line': o = board.create('line', refs(st.through), style(st, { strokeColor: '#046b4d', strokeWidth: 2 })); break;
        case 'ray': o = board.create('line', refs(st.through), style(st, { strokeColor: '#046b4d', strokeWidth: 2, straightFirst: false, straightLast: true })); break;
        case 'lineeq': o = board.create('line', [st.c, st.a, st.b], style(st, { strokeColor: '#046b4d', strokeWidth: 2 })); break;   // a·x + b·y + c = 0
        case 'polygon': o = board.create('polygon', refs(st.through), style(st, { fillColor: '#86e0bd', fillOpacity: 0.28, borders: { strokeColor: '#046b4d', strokeWidth: 2.2 }, vertices: { visible: false } })); break;
        case 'circle':
          o = board.create('circle', [ref(st.center), typeof st.through === 'string' ? ref(st.through) : st.radius], style(st, { strokeColor: '#046b4d', strokeWidth: 2, fillColor: '#d5f3e4', fillOpacity: 0.2 })); break;
        case 'arc': o = board.create('arc', refs(st.points), style(st, { strokeColor: '#c2410c', strokeWidth: 2.4 })); break;
        case 'parallel': o = board.create('parallel', [ref(st.to), ref(st.through)], style(st, aux)); break;
        case 'perpendicular': {                       // đường thẳng qua điểm, vuông góc với đường cho trước (+ chân đường vuông góc)
          var r = board.create('perpendicular', [ref(st.to), ref(st.from)], style(st, aux)), ln = Array.isArray(r) ? r[0] : r, foot = Array.isArray(r) ? r[1] : board.create('intersection', [ln, ref(st.to), 0], { visible: false, withLabel: false });
          if (st.foot) { O[st.foot] = foot; try { foot.setAttribute({ name: st.footName != null ? st.footName : st.foot, visible: true, size: 3, face: 'o', strokeColor: '#c2410c', fillColor: '#c2410c' }); } catch (e) { /* tùy phiên bản */ } }
          o = ln; break;
        }
        case 'altitude': {                            // đường cao: đoạn từ đỉnh đến chân đường vuông góc hạ xuống cạnh đối diện
          var rr = board.create('perpendicular', [ref(st.to), ref(st.from)], { visible: false, withLabel: false }), foot2 = Array.isArray(rr) ? rr[1] : board.create('intersection', [rr, ref(st.to), 0], { visible: false });
          foot2.setAttribute({ visible: true, size: 3, face: 'o', strokeColor: '#c2410c', fillColor: '#c2410c', name: st.footName || '', withLabel: !!st.footName, label: { offset: [8, -12], fontSize: 14 } });
          if (st.foot) O[st.foot] = foot2;
          o = board.create('segment', [ref(st.from), foot2], style(st, aux)); break;
        }
        case 'median': {
          var mp = board.create('midpoint', [ref(st.to[0]), ref(st.to[1])], { size: 3, strokeColor: '#475569', fillColor: '#475569', name: st.footName || '', withLabel: !!st.footName, label: { offset: [8, -12], fontSize: 14 } });
          if (st.foot) O[st.foot] = mp;
          o = board.create('segment', [ref(st.from), mp], style(st, aux)); break;
        }
        case 'bisector': o = board.create('bisector', refs(st.angle), style(st, { strokeColor: '#7c3aed', strokeWidth: 1.8, dash: 2, straightFirst: false })); break;   // [A, đỉnh, B]
        case 'perpbisector': {                        // trung trực: qua trung điểm, vuông góc với đoạn
          var seg0 = ref(st.of), m2 = board.create('midpoint', [seg0.point1, seg0.point2], { visible: false, withLabel: false });
          var pr = board.create('perpendicular', [seg0, m2], style(st, aux)); o = Array.isArray(pr) ? pr[0] : pr; break;
        }
        case 'tangent': {                             // tiếp tuyến của đường tròn tại T: vuông góc với bán kính OT tại T
          var rad = board.create('segment', [ref(st.center), ref(st.at)], st.showRadius ? seg : { visible: false });
          var tp = board.create('perpendicular', [rad, ref(st.at)], style(st, { strokeColor: '#c2410c', strokeWidth: 2.2 })); o = Array.isArray(tp) ? tp[0] : tp; break;
        }
        case 'angle': {
          o = board.create('angle', refs(st.points), style(st, { radius: st.radius || 0.8, fillColor: '#f59e0b', fillOpacity: 0.3, strokeColor: '#b45309', name: '', withLabel: st.label !== false, selection: 'minor', orthoType: 'square', orthoSensitivity: 1, label: { fontSize: 14, strokeColor: '#7c2d12' } }));
          if (st.label !== false) { try { o.label.setText(function () { return Core.fmt(o.Value() * 180 / Math.PI, 1) + '\u00b0'; }); } catch (e) { /* nhãn mặc định */ } }
          break;
        }
        case 'text': o = board.create('text', [st.at[0], st.at[1], st.text], { fontSize: st.size || 15, strokeColor: st.color || INK, fixed: true, highlight: false }); break;
        case 'curve': {                               // đồ thị hàm trong hình học tọa độ
          var comp = Core.compile(st.f), f = function (x) { return comp(x, {}); };
          o = board.create('curve', [[0], [0]], { strokeColor: st.color || '#046b4d', strokeWidth: 2.4, highlight: false, fixed: true, withLabel: false });
          o.updateDataArray = function () { var b = board.getBoundingBox(), out = Core.plotPieces(f, b[0], b[2], b[3], b[1], 900); this.dataX = out.x; this.dataY = out.y; };
          break;
        }
        default: throw new Error('Loại bước không hỗ trợ: ' + t);
      }
      name(st, o);
    });
    g.side = el('div', 'mbg-side'); g.hintKey = 'hintGeo'; g.objects = O;
    toolbar(g, false);
    board.update();
  }

  /* ---------- Hình không gian (JSXGraph 3D) ---------- */
  function draw3d(g, cfg) {
    var wr = Math.max(1, (g.stage.clientWidth || 600) / (g.stage.clientHeight || 380));
    var board = JXG.JSXGraph.initBoard(g.boardId, { boundingbox: [-6 * wr, 6, 6 * wr, -6], axis: false, grid: false, showCopyright: false, showNavigation: false, keepAspectRatio: true, pan: { enabled: false }, zoom: { enabled: false } });
    g.board = board; g.home = [-6 * wr, 6, 6 * wr, -6];
    if (!JXG.View3D && !(board.create && JXG.createView3D)) throw new Error(tx('no3d'));
    var b = cfg.box || [[-3, 3], [-3, 3], [-3, 3]];
    var view = board.create('view3d', [[-4.5, -4.5], [9, 9], b], { xPlaneRear: { visible: false }, yPlaneRear: { visible: false }, zPlaneRear: { visible: false }, axesPosition: cfg.axes === false ? 'none' : 'center' });
    var P = {}, pts = cfg.points || {}, solid = cfg.solid, hull = null, hullEls = {}, hullCenter = [0, 0, 0];
    if (solid) {                                  // khối đa diện: tính mặt/cạnh từ tọa độ để tự vẽ nét khuất khi xoay
      var sn = Array.isArray(solid) ? solid : Object.keys(pts), sp = {};
      sn.forEach(function (k) { if (!pts[k]) throw new Error('solid: chưa có điểm "' + k + '"'); sp[k] = pts[k]; });
      hull = Core.hull3d(sp);
      sn.forEach(function (k) { for (var t = 0; t < 3; t++) hullCenter[t] += sp[k][t] / sn.length; });
    }
    Object.keys(pts).forEach(function (k) {
      P[k] = view.create('point3d', pts[k], { name: k, size: 3, strokeColor: '#046b4d', fillColor: '#046b4d', fixed: true, withLabel: true, label: { fontSize: 15, strokeColor: INK } });
    });
    function p3(n) { if (!P[n]) throw new Error('Chưa có điểm "' + n + '"'); return P[n]; }
    function ekey(a, b) { return a < b ? a + '|' + b : b + '|' + a; }
    (cfg.polygons || []).forEach(function (pg) {
      var names = pg.points || pg, isFace = !!hull && hull.faces.some(function (f) { return f.names.length === names.length && names.every(function (n) { return f.names.indexOf(n) >= 0; }); });
      view.create('polygon3d', names.map(p3), { fillColor: pg.fill || '#86e0bd', fillOpacity: pg.opacity != null ? pg.opacity : 0.22, borders: isFace ? { visible: false } : { strokeColor: pg.edge || '#046b4d', strokeWidth: 1.5 }, vertices: { visible: false } });   // mặt của khối: viền do nét khuất tự vẽ; mặt cắt: giữ viền
    });
    var baseDash = {};
    (cfg.segments || []).forEach(function (s) {
      var o = s[2] || {}, l = view.create('line3d', [p3(s[0]), p3(s[1])], { straightFirst: false, straightLast: false, strokeColor: o.color || '#046b4d', strokeWidth: o.width || 2.2, dash: o.dash ? 2 : 0 });
      if (hull) { var k = ekey(s[0], s[1]); hullEls[k] = l; baseDash[k] = o.dash ? 2 : 0; }
    });
    if (hull) hull.edges.forEach(function (e) {   // cạnh của khối chưa được khai báo thì tự vẽ
      var k = ekey(e.a, e.b); if (!hullEls[k]) { hullEls[k] = view.create('line3d', [p3(e.a), p3(e.b)], { straightFirst: false, straightLast: false, strokeColor: '#046b4d', strokeWidth: 2.2, dash: 0 }); baseDash[k] = 0; }
    });
    (cfg.lines || []).forEach(function (s) {      // đường thẳng kéo dài hai phía
      var o = s[2] || {}; view.create('line3d', [p3(s[0]), p3(s[1])], { straightFirst: true, straightLast: true, strokeColor: o.color || '#c2410c', strokeWidth: o.width || 1.8, dash: o.dash ? 2 : 0 });
    });
    /* Nét khuất + nhãn điểm tránh đè: tính lại mỗi khi người học xoay hình. Hướng nhìn lấy từ chính phép chiếu của JSXGraph (project3DTo2D). */
    var proj = function (q) { var c = view.project3DTo2D(q[0], q[1], q[2]); return [c[c.length - 2], c[c.length - 1]]; }, vsign = 0, lastSig = '', labelOff = {};
    function refresh3d() {
      try {
        var vd = Core.viewDirection(proj, hullCenter, 1e-3 * 6, vsign); vsign = vd.sign;
        var sig = vd.v.map(function (n) { return n.toFixed(4); }).join();
        if (sig === lastSig) return; lastSig = sig;
        if (hull) {
          var hid = Core.hiddenEdges(hull, vd.v);
          hull.edges.forEach(function (e, i) { var k = ekey(e.a, e.b), l = hullEls[k]; l.setAttribute({ dash: hid[i] ? 2 : baseDash[k], strokeOpacity: hid[i] ? 0.8 : 1 }); });
        }
        var o2 = proj(hullCenter);
        Object.keys(pts).forEach(function (k) {   // nhãn đẩy ra xa tâm khối (theo màn hình) để không đè lên cạnh
          var q = proj(pts[k]), dx = q[0] - o2[0], dy = q[1] - o2[1], L = Math.sqrt(dx * dx + dy * dy) || 1, off = [Math.round(dx / L * 10), Math.round(dy / L * 10) + 2];
          if (!labelOff[k] || labelOff[k][0] !== off[0] || labelOff[k][1] !== off[1]) { labelOff[k] = off; try { P[k].label.setAttribute({ offset: off }); } catch (er) { /* tùy phiên bản */ } }
        });
      } catch (e) { if (!refresh3d.warned) { refresh3d.warned = true; console.warn('[MBG] không tính được nét khuất/nhãn 3D (giữ nét liền)', e); } }
    }
    if (hull || cfg.autoLabels !== false) {
      if (board.on) board.on('update', refresh3d);
      g.refresh3d = refresh3d; g.hull = hull;
    }
    g.side = el('div', 'mbg-side'); g.hintKey = 'hint3d'; g.view = view;
    board.update(); if (g.refresh3d) g.refresh3d();
  }

  /* ---------- Engine ngoài (hình rất phức tạp) ---------- */
  function drawGeoGebra(g, cfg) {
    var id = g.boardId; g.noBoard = true;
    loadScript('https://www.geogebra.org/apps/deployggb.js', function () {
      var w = g.stage.clientWidth || 640, h = g.stage.clientHeight || 400;
      var app = new window.GGBApplet({ appName: cfg.app || 'graphing', width: w, height: h, showToolBar: false, showAlgebraInput: false, showMenuBar: false, enableRightClick: false, borderColor: null, scaleContainerClass: 'mbg-stage',
        appletOnLoad: function (api) { (cfg.commands || []).forEach(function (c) { api.evalCommand(c); }); if (cfg.view) api.setCoordSystem(cfg.view[0], cfg.view[1], cfg.view[2], cfg.view[3]); } }, true);
      app.inject(id);
    }, function () { showError(g, new Error(tx('nolib'))); });
  }
  function drawDesmos(g, cfg) {
    var key = (document.querySelector('meta[name="mbg-desmos-key"]') || {}).content;
    if (!key) throw new Error(tx('nokey'));
    g.noBoard = true;
    loadScript('https://www.desmos.com/api/v1.9/calculator.js?apiKey=' + encodeURIComponent(key), function () {
      var calc = window.Desmos.GraphingCalculator(document.getElementById(g.boardId), { keypad: false, expressions: false, settingsMenu: false, zoomButtons: true });
      (cfg.expressions || []).forEach(function (l, i) { calc.setExpression({ id: 'e' + i, latex: l }); });
      if (cfg.view) calc.setMathBounds({ left: cfg.view[0], right: cfg.view[1], bottom: cfg.view[2], top: cfg.view[3] });
    }, function () { showError(g, new Error(tx('nolib'))); });
  }

  /* ---------- Lắp ráp từng hình ---------- */
  function setup(host) {
    var cfg;
    try { cfg = JSON.parse(host.getAttribute('data-mbg')); } catch (e) { host.textContent = 'Cấu hình hình vẽ không hợp lệ.'; return; }
    var g = { host: host, cfg: cfg, boardId: 'mbg-board-' + (++uid) };
    host.innerHTML = '';
    g.stage = el('div', 'mbg-stage'); g.stage.id = g.boardId; host.appendChild(g.stage);
    g.boardId = g.stage.id;
    registry.push(g); host.__mbg = g;
    var started = false;
    function start() {
      if (started) return;
      var r = g.stage.getBoundingClientRect();
      if (r.width < 20 || r.height < 20) return;      // đang ẩn (ví dụ thuộc mức học khác): đợi hiện ra mới vẽ
      started = true;
      try {
        var kind = cfg.kind || 'graph', ext = kind === 'geogebra' || kind === 'desmos';
        if (!ext && !window.JXG) throw new Error(tx('nolib'));
        if (kind === 'graph') drawGraph(g, cfg);
        else if (kind === 'geo') drawGeo(g, cfg);
        else if (kind === '3d') draw3d(g, cfg);
        else if (kind === 'geogebra') drawGeoGebra(g, cfg);
        else if (kind === 'desmos') drawDesmos(g, cfg);
        else throw new Error('kind không hợp lệ: ' + kind);
        if (g.legend) host.appendChild(g.legend);
        if (g.tools && !g.noBoard) host.insertBefore(g.tools, g.stage);
        if (g.side && g.side.childNodes.length) host.appendChild(g.side);
        var hint = el('p', 'mbg-hint'); hint.setAttribute('data-k', g.hintKey || 'hint'); host.appendChild(hint);
        localize();
      } catch (e) { showError(g, e); }
    }
    if (window.ResizeObserver) new ResizeObserver(start).observe(g.stage); else start();
    start();
  }

  function boot() { [].forEach.call(document.querySelectorAll('.mbg[data-mbg]'), setup); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot); else boot();
  window.MBG = { registry: registry, core: Core, setup: setup };
})();
