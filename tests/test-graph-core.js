/* Kiểm thử lõi toán học của hệ thống đồ thị:  node tests/test-graph-core.js */
const C = require('../js/mb-graph-core.js');
let pass = 0, fail = 0;
function ok(cond, msg) { if (cond) pass++; else { fail++; console.log('  ✗ SAI:', msg); } }
function near(a, b, t) { return Math.abs(a - b) < (t || 1e-6); }
function nearList(got, want, t) { return got.length === want.length && got.every((v, i) => near(v, want[i], t || 1e-5)); }
const F = (s, p) => C.compile(s, p);

// --- 1. Bộ đọc biểu thức ---
ok(near(F('3x^2-2x+1')(2), 9), '3x^2-2x+1 tại 2');
ok(near(F('-x^2')(3), -9), '-x^2 = -(x^2)');
ok(near(F('2^3^2')(0), 512), '2^3^2 kết hợp phải');
ok(near(F('2^-x')(1), 0.5), '2^-x');
ok(near(F('(x+1)(x-1)')(3), 8), 'nhân ngầm hai ngoặc');
ok(near(F('2sin(x)')(Math.PI / 2), 2), '2sin(x)');
ok(near(F('x(x+2)')(3), 15), 'x(x+2)');
ok(near(F('log(100)')(0), 2) && near(F('log(2,8)')(0), 3) && near(F('ln(e)')(0), 1), 'log / ln');
ok(Number.isNaN(F('sqrt(x)')(-1)) && Number.isNaN(F('ln(x)')(-1)), 'miền xác định thực');
ok(near(F('cbrt(x)')(-8), -2), 'cbrt số âm');
ok(near(F('abs(x-3)')(1), 2), 'abs');
ok(near(F('a*x+b', ['a', 'b'])(2, { a: 3, b: 1 }), 7), 'tham số a, b');
ok(near(F('2π')(0), 2 * Math.PI) && near(F('√(x)')(9), 3), 'ký hiệu π, √');
for (const bad of ['x+', 'foo(x)', '2 $ x', '(x+1', 'y+1']) { let t = false; try { F(bad); } catch (e) { t = true; } ok(t, 'phải báo lỗi: ' + bad); }

// --- 2. Lấy mẫu có ngắt nhánh ---
function straddles(r, x0) {      // có đoạn thẳng nối hai điểm ở hai phía x0 mà không bị ngắt không?
  for (let i = 0; i + 1 < r.x.length; i++) {
    if (Number.isFinite(r.x[i]) && Number.isFinite(r.x[i + 1]) && r.x[i] < x0 && r.x[i + 1] > x0) return true;
  }
  return false;
}
function breaks(r) { return r.x.filter(Number.isNaN).length; }
let r = C.plotPieces(F('1/x'), -5, 5, -6, 6, 1200);
ok(!straddles(r, 0) && breaks(r) >= 1, '1/x không nối qua x=0');
r = C.plotPieces(F('tan(x)'), -2 * Math.PI, 2 * Math.PI, -6, 6, 1500);
ok(breaks(r) === 4, 'tan: 4 chỗ ngắt, nhận được ' + breaks(r));
[-3 * Math.PI / 2, -Math.PI / 2, Math.PI / 2, 3 * Math.PI / 2].forEach(p => ok(!straddles(r, p), 'tan không nối qua ' + p.toFixed(3)));
r = C.plotPieces(F('(x^2-1)/(x-2)'), -6, 10, -10, 10, 1500);
ok(!straddles(r, 2), '(x²−1)/(x−2) không nối qua tiệm cận x=2');
r = C.plotPieces(F('(x^2-4)/(x-2)'), -6, 6, -6, 6, 1200);
ok(r.y.filter(Number.isFinite).every((y, i, a) => i === 0 || Math.abs(y - a[i - 1]) < 1), '(x²−4)/(x−2) liên tục (chỉ thủng 1 điểm)');
r = C.plotPieces(F('exp(10x)'), -3, 3, -5, 5, 1000);
ok(breaks(r) === 0, 'e^(10x) dốc nhưng liên tục: không ngắt');
r = C.plotPieces(x => (x < 1 ? x : x + 2), -3, 4, -6, 6, 1000);
ok(breaks(r) === 1 && !straddles(r, 1), 'hàm từng đoạn nhảy 1→3: ngắt, không nối qua x=1');
r = C.plotPieces(x => (x < 0 ? -1 : 1), -2, 2, -3, 3, 800); ok(breaks(r) === 1 && !straddles(r, 0), 'hàm dấu: ngắt tại 0');
r = C.plotPieces(F('x^9'), -2, 2, -5, 5, 1000); ok(breaks(r) === 0, 'x⁹ dốc đứng nhưng liên tục');
r = C.plotPieces(F('atan(10x)'), -3, 3, -2, 2, 1000); ok(breaks(r) === 0, 'arctan(10x) liên tục');
r = C.plotPieces(F('sqrt(x)'), -4, 9, -2, 5, 800);
ok(r.x.filter(Number.isFinite).every(x => x >= 0), 'sqrt chỉ vẽ x ≥ 0');
r = C.plotPieces(F('1/x^2'), -3, 3, -2, 8, 1000);
ok(!straddles(r, 0), '1/x² không nối qua x=0');
r = C.plotPieces(F('sin(x)'), -7, 7, -2, 2, 1000);
ok(breaks(r) === 0, 'sin không có chỗ ngắt');
r = C.plotPieces(F('ln(x)'), -2, 6, -4, 4, 1000);
ok(r.x.filter(Number.isFinite).every(x => x > 0), 'ln chỉ vẽ x > 0');

// --- 3. Nghiệm, giao điểm ---
ok(nearList(C.roots(F('x^3-x'), -3, 3), [-1, 0, 1]), 'nghiệm x³−x');
ok(nearList(C.roots(F('(x-1)^2'), -3, 3), [1], 1e-4), 'nghiệm kép (x−1)²');
ok(C.roots(F('1/x'), -3, 3).length === 0, '1/x không có nghiệm (không nhận đổi dấu ở tiệm cận)');
ok(nearList(C.roots(F('tan(x)'), -4, 4), [-Math.PI, 0, Math.PI], 1e-5), 'nghiệm tan(x) trong [−4,4] (loại tiệm cận)');
ok(nearList(C.roots(F('x^2-2'), -3, 3), [-Math.SQRT2, Math.SQRT2]), 'nghiệm x²−2');
ok(nearList(C.intersections(F('x^2'), F('x+2'), -5, 5), [-1, 2]), 'giao x² và x+2');
ok(nearList(C.intersections(F('2^x'), F('x+1'), -5, 5), [0, 1]), 'giao 2^x và x+1');
ok(C.intersections(F('1/x'), F('0'), -5, 5).length === 0, 'giao 1/x với trục hoành rỗng');

// --- 4. Cực trị, điểm uốn, đơn điệu ---
let ex = C.extrema(F('x^3-3x'), -3, 3);
ok(ex.length === 2 && ex[0].kind === 'max' && near(ex[0].x, -1, 1e-4) && near(ex[0].y, 2, 1e-4) && ex[1].kind === 'min' && near(ex[1].x, 1, 1e-4) && near(ex[1].y, -2, 1e-4), 'cực trị x³−3x');
ex = C.extrema(F('abs(x)'), -3, 3); ok(ex.length === 1 && ex[0].kind === 'min' && near(ex[0].x, 0, 1e-5), 'cực tiểu tại góc của |x|');
ok(C.extrema(F('1/x'), -3, 3).length === 0, '1/x không có cực trị');
ex = C.extrema(F('sin(x)'), 0, 2 * Math.PI); ok(ex.length === 2 && near(ex[0].x, Math.PI / 2, 1e-4) && ex[0].kind === 'max' && near(ex[1].x, 3 * Math.PI / 2, 1e-4), 'cực trị sin trên [0,2π]');
ok(C.extrema(F('x^3'), -3, 3).length === 0, 'x³ không có cực trị');
ok(C.extrema(F('5'), -3, 3).length === 0, 'hàm hằng không có cực trị');
let inf = C.inflections(F('x^3'), -3, 3); ok(inf.length === 1 && near(inf[0].x, 0, 1e-3), 'điểm uốn x³');
ok(C.inflections(F('x^4'), -3, 3).length === 0, 'x⁴ không có điểm uốn');
ok(C.inflections(F('1/x'), -3, 3).length === 0, '1/x không có điểm uốn (loại tiệm cận)');
ok(C.inflections(F('3'), -3, 3).length === 0, 'hàm hằng không có điểm uốn');
inf = C.inflections(F('x^3-3x^2'), -3, 5); ok(inf.length === 1 && near(inf[0].x, 1, 1e-3) && near(inf[0].y, -2, 1e-3), 'điểm uốn x³−3x²');
const mi = C.monotoneIntervals(F('x^3-3x'), -3, 3);
ok(mi.length === 3 && mi[0].up && !mi[1].up && mi[2].up && near(mi[0].to, -1, 1e-4), 'đơn điệu x³−3x');
ok(near(C.deriv(F('x^2'), 3), 6, 1e-6) && near(C.deriv(F('sin(x)'), 0), 1, 1e-6), 'đạo hàm số');

// --- 6. Bội nghiệm, lỗ thủng, khoảng đơn điệu, tiệm cận (giai đoạn 2) ---
const mult = (e, a, b) => C.rootsDetailed(F(e), a, b).map(r => [+r.x.toFixed(4), r.mult, r.crosses]);
ok(JSON.stringify(mult('(x-1)^2*(x+2)', -7, 7)) === '[[-2,1,true],[1,2,false]]', 'bội: (x-1)^2(x+2)');
ok(JSON.stringify(mult('(x-1)^3', -7, 7)) === '[[1,3,true]]', 'bội 3 đổi dấu');
ok(JSON.stringify(mult('(x-1)^4', -7, 7)) === '[[1,4,false]]', 'bội 4 không đổi dấu');
ok(JSON.stringify(mult('x^2*(x-3)^3', -7, 7)) === '[[0,2,false],[3,3,true]]', 'bội: x^2(x-3)^3');
ok(mult('sin(x)^2', -7, 7).every(r => r[1] === 2 && r[2] === false), 'sin^2: nghiệm kép');
const holeList = e => C.holes(F(e), -7, 7).map(h => [+h.x.toFixed(4), +h.y.toFixed(4)]);
ok(JSON.stringify(holeList('(x^2-1)/(x-1)')) === '[[1,2]]', 'lỗ thủng (x²−1)/(x−1)');
ok(JSON.stringify(holeList('sin(x)/x')) === '[[0,1]]', 'lỗ thủng sin x / x');
ok(holeList('1/x').length === 0 && holeList('tan(x)').length === 0, 'tiệm cận KHÔNG bị nhận nhầm là lỗ thủng');
ok(C.roots(F('x^2/x'), -6, 6).length === 0, 'điểm không xác định không phải nghiệm');
const mono = (e, a, b) => JSON.stringify(C.monotoneIntervals(F(e), a, b).map(i => [+i.from.toFixed(3), +i.to.toFixed(3), i.up]));
ok(mono('x^3', -2, 2) === '[[-2,2,true]]', 'x³ đồng biến trên cả khoảng (đạo hàm = 0 tại 0 vẫn không đổi chiều)');
ok(mono('1/x', -3, 3) === '[[-3,0,false],[0,3,false]]', '1/x nghịch biến trên từng khoảng, tách tại tiệm cận');
ok(mono('x^3-3*x', -3, 3) === '[[-3,-1,true],[-1,1,false],[1,3,true]]', 'x³−3x');
ok(mono('sqrt(x)', -1, 4) === '[[0,4,true]]', 'căn x: chỉ trong tập xác định');
ok(mono('(x^2-1)/(x-1)', -3, 3) === '[[-3,3,true]]', 'hàm có lỗ thủng vẫn đồng biến liền khoảng');
ok(JSON.stringify(C.monotoneIntervals(F('tan(x)'), -1.4, 4.5).map(i => +i.to.toFixed(3))) === '[1.571,4.5]' || mono('tan(x)', -1.4, 4.5).includes('1.571'), 'tan: tách tại π/2');
ok(C.checkAsymptote(F('1/(x-2)'), { type: 'v', x: 2 }) && !C.checkAsymptote(F('1/(x-2)'), { type: 'v', x: 3 }), 'tiệm cận đứng đúng/sai');
ok(C.checkAsymptote(F('(2x+1)/(x-1)'), { type: 'h', y: 2 }) && !C.checkAsymptote(F('(2x+1)/(x-1)'), { type: 'h', y: 1 }), 'tiệm cận ngang đúng/sai');
ok(C.checkAsymptote(F('(x^2+1)/x'), { type: 'o', m: 1, b: 0 }) && !C.checkAsymptote(F('(x^2+1)/x'), { type: 'o', m: 1, b: 1 }), 'tiệm cận xiên đúng/sai');

// --- 7. Hình khối: mặt, cạnh, nét khuất (giai đoạn 3) ---
const cube = { A: [-2, -2, -2], B: [2, -2, -2], C: [2, 2, -2], D: [-2, 2, -2], A1: [-2, -2, 2], B1: [2, -2, 2], C1: [2, 2, 2], D1: [-2, 2, 2] };
const pyr = { A: [-3, -2, 0], B: [1, -2, 0], C: [3, 2, 0], D: [-1, 2, 0], S: [0, 0, 3.2] };
const prism = { A: [0, 0, 0], B: [3, 0, 0], C: [1, 2, 0], A1: [0, 0, 4], B1: [3, 0, 4], C1: [1, 2, 4] };
const box = { A: [0, 0, 0], B: [5, 0, 0], C: [5, 3, 0], D: [0, 3, 0], A1: [0, 0, 2], B1: [5, 0, 2], C1: [5, 3, 2], D1: [0, 3, 2] };
function euler(P) { const h = C.hull3d(P); return { V: Object.keys(P).length, E: h.edges.length, F: h.faces.length, h }; }
[['hình lập phương', cube, 8, 12, 6], ['hình chóp tứ giác', pyr, 5, 8, 5], ['lăng trụ tam giác', prism, 6, 9, 5], ['hình hộp chữ nhật', box, 8, 12, 6]].forEach(([name, P, V, E, Fc]) => {
  const r = euler(P);
  ok(r.V - r.E + r.F === 2 && r.E === E && r.F === Fc, name + ': ' + r.V + ' đỉnh, ' + r.E + ' cạnh, ' + r.F + ' mặt (Euler V−E+F=2)');
  ok(r.h.edges.every(e => e.faces.length === 2), name + ': mỗi cạnh kề đúng 2 mặt');
  const cen = [0, 0, 0]; Object.values(P).forEach(p => { for (let i = 0; i < 3; i++) cen[i] += p[i] / V; });
  ok(r.h.faces.every(f => f.n[0] * (f.c[0] - cen[0]) + f.n[1] * (f.c[1] - cen[1]) + f.n[2] * (f.c[2] - cen[2]) > 0), name + ': pháp tuyến mọi mặt hướng ra ngoài');
});
ok(C.hull3d(pyr).faces.some(f => f.names.length === 4) && C.hull3d(pyr).faces.filter(f => f.names.length === 3).length === 4, 'hình chóp: 1 đáy tứ giác + 4 mặt bên tam giác');
const projOf = (az, el, mirror) => p => { const xr = p[0] * Math.cos(az) - p[1] * Math.sin(az), yr = p[0] * Math.sin(az) + p[1] * Math.cos(az); return [mirror ? -xr : xr, p[2] * Math.cos(el) + yr * Math.sin(el)]; };
const hidSet = (P, az, el, mirror, sign) => { const h = C.hull3d(P), vd = C.viewDirection(projOf(az, el, mirror), [0, 0, 0], 1e-3, sign || 0), hid = C.hiddenEdges(h, vd.v); return h.edges.filter((e, i) => hid[i]).map(e => [e.a, e.b].sort().join('')).sort().join(','); };
[[0.6, 0.5], [2.5, 0.8], [-1.2, 0.3], [4, 1.2]].forEach(([az, el]) => {
  ok(hidSet(cube, az, el, false).split(',').length === 3, 'lập phương nhìn từ trên (az=' + az + ', el=' + el + '): đúng 3 cạnh khuất');
  ok(hidSet(cube, az, el, false) === hidSet(cube, az, el, true), 'phép chiếu bị lật gương cho CÙNG tập cạnh khuất (hướng nhìn không phụ thuộc chiều màn hình)');
});
// Chiều lật gương cho CÙNG tập cạnh khuất khi ánh xạ phản chiếu theo trục x nhưng người xem vẫn ở trên: kiểm tra hướng v có z > 0
ok(C.viewDirection(projOf(0.6, 0.5, true), [0, 0, 0], 1e-3, 0).v[2] > 0 && C.viewDirection(projOf(0.6, 0.5, false), [0, 0, 0], 1e-3, 0).v[2] > 0, 'hướng nhìn chuẩn hóa: người xem ở phía trên (z > 0)');
// Xoay liên tục: dấu giữ nguyên, tập cạnh khuất đổi liên tục theo góc (không nhảy khi đi qua mặt phẳng nằm ngang)
const sg = C.viewDirection(projOf(0.6, 0.5, false), [0, 0, 0], 1e-3, 0).sign;
ok(C.viewDirection(projOf(0.6, -0.4, false), [0, 0, 0], 1e-3, sg).v[2] < 0, 'nhìn từ dưới (el < 0) sau khi chuẩn hóa: v_z < 0, các cạnh đáy trở thành nét liền');
// So với kiểm tra độc lập "tia nhìn": cạnh khuất ⇔ điểm giữa cạnh dời một đoạn nhỏ về phía người xem nằm TRONG khối
function inside(P, q) { const xs = Object.values(P); const lo = [0, 1, 2].map(i => Math.min(...xs.map(p => p[i]))), hi = [0, 1, 2].map(i => Math.max(...xs.map(p => p[i]))); return [0, 1, 2].every(i => q[i] > lo[i] + 1e-9 && q[i] < hi[i] - 1e-9); }
[[0.6, 0.5], [2.5, 0.8], [-1.2, 0.3], [4, 1.2]].forEach(([az, el]) => {
  const h = C.hull3d(cube), vd = C.viewDirection(projOf(az, el, false), [0, 0, 0], 1e-3, 0), hid = C.hiddenEdges(h, vd.v);
  const ref = h.edges.map(e => { const m = [0, 1, 2].map(i => (cube[e.a][i] + cube[e.b][i]) / 2 + 0.01 * vd.v[i]); return inside(cube, m); });
  ok(hid.every((x, i) => x === ref[i]), 'nét khuất khớp phép thử tia nhìn độc lập (az=' + az + ', el=' + el + ')');
});

// --- 5. Định dạng ---
const P = Math.PI;
ok(C.formatPi(0) === '0' && C.formatPi(P) === 'π' && C.formatPi(P / 2) === 'π/2' && C.formatPi(3 * P / 2) === '3π/2' && C.formatPi(2 * P) === '2π' && C.formatPi(-P / 3) === '−π/3' && C.formatPi(5 * P / 6) === '5π/6' && C.formatPi(-P) === '−π', 'nhãn bội của π');
ok(C.fmt(1.23456) === '1.235' && C.fmt(-2) === '\u22122' && C.fmt(1e-12) === '0', 'định dạng số');

console.log((fail ? '✗' : '✓') + ' lõi đồ thị: ' + pass + ' đạt, ' + fail + ' lỗi');
process.exit(fail ? 1 : 0);
