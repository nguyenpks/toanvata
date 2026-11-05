/* Lưu tiến độ học: khóa LocalStorage "mathbridge_progress".
   Cấu trúc: { version:1, grade:10, lastLesson:"id", completed:{ "id":{completedAt:"ISO"} },
               history:[{id,type:"view"|"complete",at:"ISO"}] }
   Hàm dùng chung đánh dấu hoàn thành: MathBridgeProgress.markComplete(id).
   Chỉ gọi hàm này khi học sinh chủ động bấm xác nhận. */
(function (w) {
  'use strict';
  var KEY = 'mathbridge_progress';
  function empty() { return { version: 1, grade: 10, completed: {}, history: [] }; }
  function load() {
    try {
      var d = JSON.parse(localStorage.getItem(KEY));
      if (d && d.version === 1 && d.completed && d.history) return d;
    } catch (e) { /* dữ liệu hỏng hoặc bị chặn: dùng dữ liệu rỗng */ }
    return empty();
  }
  function save(d) {
    try { localStorage.setItem(KEY, JSON.stringify(d)); return true; } catch (e) { return false; }
  }
  function log(d, id, type) {
    d.history.unshift({ id: id, type: type, at: new Date().toISOString() });
    d.history = d.history.slice(0, 100);
  }
  w.MathBridgeProgress = {
    KEY: KEY,
    get: load,
    isComplete: function (id) { return !!load().completed[id]; },
    markComplete: function (id) {
      var d = load();
      if (!d.completed[id]) { d.completed[id] = { completedAt: new Date().toISOString() }; log(d, id, 'complete'); }
      return save(d);
    },
    recordView: function (id) { var d = load(); log(d, id, 'view'); d.lastLesson = id; return save(d); },
    setGrade: function (g) { var d = load(); d.grade = g; return save(d); },
    reset: function () { return save(empty()); }
  };
})(window);
