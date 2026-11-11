/* Lưu tiến độ học.
   - Chưa đăng nhập: lưu trên trình duyệt (LocalStorage, khóa "mathbridge_progress"), như trước.
   - Đã đăng nhập: lưu theo từng tài khoản (khóa "mathbridge_progress:<tên đăng nhập>") và gửi về
     máy chủ (Google Apps Script + Google Sheets của giáo viên). Đăng nhập ở máy khác sẽ tải lại tiến độ.
   Cấu trúc: { version:1, grade:10, lastLesson:"id", completed:{ "id":{completedAt:"ISO"} },
               history:[{id,type:"view"|"complete",at:"ISO"}], quiz:{ "id|mức":{attempts,best,last,lastAt} } }
   MathBridgeProgress.markComplete(id) chỉ gọi khi học sinh chủ động bấm xác nhận. */
(function (w) {
  'use strict';
  /* Địa chỉ Web app Apps Script (…/exec). Để trống thì website chạy như cũ, không có đăng nhập. */
  var API = w.MATHBRIDGE_API || 'https://script.google.com/macros/s/AKfycbyA7C_jhTamq9t7PSOjrr8db5dcUTMK31O8g9OtTBvDxMBMS_puxIh1r4xAUrVtT7nN/exec';
  var BASE = 'mathbridge_progress', SESSION = 'mathbridge_session', OUTBOX = 'mathbridge_outbox';
  var listeners = [];

  function ls(k, v) {
    try {
      if (v === undefined) return localStorage.getItem(k);
      if (v === null) localStorage.removeItem(k); else localStorage.setItem(k, v);
    } catch (e) { return null; }
    return true;
  }
  function session() { try { var s = JSON.parse(ls(SESSION)); return s && s.token && s.user ? s : null; } catch (e) { return null; } }
  function key() { var s = session(); return s ? BASE + ':' + s.user.tk.toLowerCase() : BASE; }
  function empty() { return { version: 1, grade: 10, completed: {}, history: [], quiz: {} }; }
  function load() {
    try {
      var d = JSON.parse(ls(key()));
      if (d && d.version === 1 && d.completed && d.history) { d.quiz = d.quiz || {}; return d; }
    } catch (e) { /* dữ liệu hỏng hoặc bị chặn: dùng dữ liệu rỗng */ }
    return empty();
  }
  function save(d) { return ls(key(), JSON.stringify(d)) === true; }
  function log(d, id, type) {
    d.history.unshift({ id: id, type: type, at: new Date().toISOString() });
    d.history = d.history.slice(0, 100);
  }
  function uid() { return Date.now().toString(36) + Math.random().toString(36).slice(2, 8); }
  function notify() { listeners.forEach(function (f) { try { f(); } catch (e) { /* bỏ qua */ } }); }

  /* ---------- Hàng đợi gửi lên máy chủ ---------- */
  function outbox() { var s = session(); if (!s) return null; try { return JSON.parse(ls(OUTBOX + ':' + s.user.tk.toLowerCase())) || []; } catch (e) { return []; } }
  function setOutbox(a) { var s = session(); if (s) ls(OUTBOX + ':' + s.user.tk.toLowerCase(), JSON.stringify(a.slice(-500))); }
  function queue(ev) {
    var a = outbox(); if (!a) return;
    ev.uid = uid(); ev.at = new Date().toISOString(); a.push(ev); setOutbox(a); flushSoon();
  }
  var timer = null, busy = false;
  function flushSoon() { if (!timer) timer = setTimeout(function () { timer = null; flush(); }, 800); }
  function post(body) {
    return fetch(API, { method: 'POST', body: JSON.stringify(body) }).then(function (r) { return r.json(); });
  }
  /* Ghép tiến độ trên máy chủ vào bản trên máy (lấy hợp các bài đã hoàn thành) */
  function merge(remote) {
    if (!remote) return;
    var d = load();
    Object.keys(remote.completed || {}).forEach(function (id) { if (!d.completed[id]) d.completed[id] = remote.completed[id]; });
    var seen = {}; d.history = (remote.history || []).concat(d.history).filter(function (h) {
      var k = h.id + h.type + h.at; if (seen[k]) return false; seen[k] = 1; return true;
    }).sort(function (a, b) { return a.at < b.at ? 1 : -1; }).slice(0, 100);
    if (remote.lastLesson && !d.lastLesson) d.lastLesson = remote.lastLesson;
    d.quiz = remote.quiz || d.quiz || {};
    save(d);
  }
  function handleAuth(res) {
    if (res && res.auth) { ls(SESSION, null); Account.status = 'Phiên đăng nhập hết hạn, hãy đăng nhập lại.'; notify(); return true; }
    return false;
  }
  function flush() {
    var s = session(); if (!API || !s || busy) return Promise.resolve();
    var a = outbox(); if (!a.length) return Promise.resolve();
    busy = true; var sending = a.slice(0, 100);
    return post({ action: 'sync', token: s.token, events: sending }).then(function (res) {
      busy = false;
      if (handleAuth(res)) return;
      if (!res.ok) throw new Error(res.error || 'Lỗi máy chủ');
      var rest = outbox().filter(function (e) { return !sending.some(function (x) { return x.uid === e.uid; }); });
      setOutbox(rest); merge(res.progress);
      Account.status = 'Đã lưu lên tài khoản lúc ' + new Date().toLocaleTimeString('vi-VN'); notify();
      if (rest.length) flushSoon();
    }).catch(function () {
      busy = false; Account.status = 'Chưa gửi được (mất mạng?). Tiến độ vẫn lưu trên máy và sẽ gửi lại sau.'; notify();
    });
  }

  var P = w.MathBridgeProgress = {
    get KEY() { return key(); },
    get: load,
    isComplete: function (id) { return !!load().completed[id]; },
    markComplete: function (id) {
      var d = load(), isNew = !d.completed[id];
      if (isNew) { d.completed[id] = { completedAt: new Date().toISOString() }; log(d, id, 'complete'); }
      var ok = save(d);
      if (isNew) queue({ type: 'complete', id: id, title: titleOf(id) });
      return ok;
    },
    recordView: function (id) {
      var d = load(); log(d, id, 'view'); d.lastLesson = id; var ok = save(d);
      queue({ type: 'view', id: id, title: titleOf(id) });
      return ok;
    },
    /* Kết quả khi học sinh bấm "Nộp bài / Xem kết quả" ở phần luyện tập */
    recordQuiz: function (id, r) {
      var d = load(), k = id + '|' + r.level, q = d.quiz[k] || (d.quiz[k] = { id: id, level: r.level, attempts: 0, best: 0, last: 0 });
      var pct = r.total ? Math.round(1000 * r.right / r.total) / 10 : 0;
      q.attempts++; q.last = pct; q.best = Math.max(q.best, pct); q.lastAt = new Date().toISOString();
      save(d);
      queue({ type: 'quiz', id: id, title: titleOf(id) || r.title, level: r.level, right: r.right, total: r.total, done: r.done });
    },
    setGrade: function (g) { var d = load(); d.grade = g; return save(d); },
    reset: function () { return save(empty()); }
  };
  var titles = {};
  function titleOf(id) {
    if (titles[id]) return titles[id];
    try { if (w.parent !== w && w.parent.MathBridgeProgress) return w.parent.MathBridgeProgress.titleOf(id); } catch (e) { /* khác origin */ }
    return '';
  }
  P.titleOf = titleOf;
  P.setTitles = function (map) { titles = map || {}; };

  /* ---------- Tài khoản ---------- */
  var Account = w.MathBridgeAccount = {
    enabled: !!API,
    status: '',
    user: function () { var s = session(); return s ? s.user : null; },
    login: function (user, pass) {
      if (!API) return Promise.reject(new Error('Website chưa bật đăng nhập.'));
      return post({ action: 'login', user: user, pass: pass }).then(function (res) {
        if (!res.ok) throw new Error(res.error || 'Đăng nhập không thành công.');
        ls(SESSION, JSON.stringify({ token: res.token, user: res.user }));
        merge(res.progress); Account.status = 'Đã tải tiến độ từ tài khoản.'; notify(); flush();
        return res.user;
      }, function () { throw new Error('Không kết nối được máy chủ. Kiểm tra mạng Internet.'); });
    },
    logout: function () { var go = function () { ls(SESSION, null); Account.status = ''; notify(); }; return flush().then(go, go); },
    refresh: function () {
      var s = session(); if (!API || !s) return Promise.resolve();
      return post({ action: 'progress', token: s.token }).then(function (res) {
        if (handleAuth(res) || !res.ok) return; merge(res.progress); notify(); flush();
      }, function () { /* mất mạng: dùng bản trên máy */ });
    },
    pending: function () { var a = outbox(); return a ? a.length : 0; },
    onChange: function (f) { listeners.push(f); }
  };
  if (API) {
    w.addEventListener('online', function () { flush(); });
    if (session()) flushSoon();
  }
})(window);
