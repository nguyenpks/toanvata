/* Bản GIẢ LẬP tối thiểu của JSXGraph, chỉ để kiểm thử phần ghép nối (không vẽ gì). Không dùng cho website thật. */
(function () {
  function Obj(board, type, args, attrs) { this.board = board; this.type = type; this.args = args; this.attrs = attrs || {}; this.label = { setText: function () {}, setAttribute: function () {} }; this.dataX = []; this.dataY = [];
    if (type === 'point' && typeof args[0] === 'number') this.coords = { usrCoords: [1, args[0], args[1]] };
    if (type === 'segment') { this.point1 = args[0]; this.point2 = args[1]; } }
  Obj.prototype.setAttribute = function (a) { Object.assign(this.attrs, a); };
  Obj.prototype.Value = function () { return Math.PI / 2; };
  Obj.prototype.create = function (t, a, at) { var q = new Obj(this.board, t, a, at); this.board.created.push(q); return q; };
  /* Khung nhìn 3D giả: phép chiếu song song với góc phương vị az, góc nâng el (setAngles) và tùy chọn lật gương (mirror) */
  Obj.prototype.project3DTo2D = function (x, y, z) {
    if (Array.isArray(x)) { z = x[2]; y = x[1]; x = x[0]; }
    var az = this.az || 0.6, el = this.el || 0.5, xr = x * Math.cos(az) - y * Math.sin(az), yr = x * Math.sin(az) + y * Math.cos(az);
    return [1, this.mirror ? -xr : xr, z * Math.cos(el) + yr * Math.sin(el)];
  };
  Obj.prototype.setAngles = function (az, el) { this.az = az; this.el = el; this.board.fire('update'); };
  function Board(id, attrs) {
    var c = document.getElementById(id); this.id = id; this.attrs = attrs; this.canvasWidth = c.clientWidth; this.canvasHeight = c.clientHeight;
    this.bb = attrs.boundingbox.slice(); this.created = []; this.grids = [{ setAttribute: function () {} }];
    this.defaultAxes = { x: { defaultTicks: { setAttribute: function () {} } }, y: { defaultTicks: { setAttribute: function () {} } } };
    c.setAttribute('data-mock', '1');
  }
  Board.prototype.create = function (type, args, attrs) {
    var o = new Obj(this, type, args, attrs); this.created.push(o);
    if (type === 'perpendicular') { var l = new Obj(this, 'line', [], {}), p = new Obj(this, 'point', [], {}); this.created.push(l, p); return [l, p]; }
    return o;
  };
  Board.prototype.update = function () { this.created.forEach(function (o) { if (o.type === 'curve' && o.updateDataArray) o.updateDataArray(); }); };
  Board.prototype.getBoundingBox = function () { return this.bb.slice(); };
  Board.prototype.setBoundingBox = function (b) { this.bb = b.slice(); this.update(); this.fire('boundingbox'); };
  Board.prototype.fire = function (ev) { (this.handlers && this.handlers[ev] || []).forEach(function (f) { f(); }); };
  Board.prototype.on = function (ev, fn) { (this.handlers = this.handlers || {})[ev] = (this.handlers[ev] || []).concat([fn]); };
  Board.prototype.removeObject = function (o) { var i = this.created.indexOf(o); if (i >= 0) this.created.splice(i, 1); };
  window.JXG = { View3D: function () {}, JSXGraph: { initBoard: function (id, a) { var b = new Board(id, a); (window.__boards = window.__boards || []).push(b); return b; } } };
})();
