/* MathBridge – bộ tương tác bài học v2 (theo quy định ba mức học tập, Phần III–V).
   Khác bản v1: (a) mức học chuyển tự do, lưu LocalStorage khóa "mathbridge_learning_mode" (level1|level2|level3);
   (b) Mức 1: thuật ngữ in đậm + tooltip tiếng Anh; (c) Mức 2: mỗi khối có nút dịch riêng; (d) Mức 3: không có tiếng Việt;
   (e) đổi mức không xóa bài làm, không đặt lại điểm, không mất vị trí đang đọc.
   Không ghi hoàn thành bài (việc đó chỉ do js/lesson-bridge.js khi học sinh bấm nút). */
(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var KEY = 'mathbridge_learning_mode', MODES = ['level1', 'level2', 'level3'];

  /* ---------- Chuỗi song ngữ do JS tạo ra ---------- */
  function txi(en, vi) { return '<span class="txi"><span class="en">' + en + '</span><span class="vi">' + vi + '</span></span>'; }
  function trBtn() { return '<button type="button" class="mbl-tr" data-tr aria-expanded="false" aria-label="Dịch sang tiếng Việt" title="Dịch sang tiếng Việt">🌐 VI</button>'; }
  function txb(en, vi) { return '<div class="tx"><p class="en">' + en + '</p>' + trBtn() + '<p class="vi">' + vi + '</p></div>'; }

  /* ---------- Chiều cao iframe ---------- */
  function fit() {
    try {
      var f = window.frameElement;
      if (f && f.contentDocument === document) {
        f.style.height = (Math.ceil(document.body.getBoundingClientRect().height) + 12) + 'px';
      }
    } catch (e) { /* khác origin hoặc không nhúng: bỏ qua */ }
  }
  /* Xếp hàng các lần dựng công thức: MathJax không cho chạy chồng nhau, và lỗi phải được ghi lại chứ không nuốt mất. */
  var mjQueue = null;
  /* Công thức trong dòng quá rộng so với khung chứa: cho thành khối cuộn ngang để không làm trang tràn ngang trên điện thoại. */
  function wrapWide() {
    var list = document.querySelectorAll('mjx-container:not([display="true"])');
    for (var i = 0; i < list.length; i++) {
      var m = list[i], host = m.parentElement;
      while (host && host !== document.body && getComputedStyle(host).display.indexOf('inline') === 0) host = host.parentElement;
      if (host && m.offsetWidth > host.clientWidth && host.clientWidth > 0) m.classList.add('mbl-wide-inline');
    }
  }
  function typeset(el) {
    var MJ = window.MathJax;
    if (!(MJ && MJ.typesetPromise)) return;
    var base = mjQueue || (MJ.startup && MJ.startup.promise) || Promise.resolve();
    mjQueue = base.then(function () {
      if (MJ.typesetClear && el) MJ.typesetClear([el]);
      return MJ.typesetPromise(el ? [el] : undefined);
    }).then(function () { wrapWide(); fit(); }).catch(function (e) {
      if (window.console) console.warn('[MathJax]', e && e.message ? e.message : e);
      fit();
    });
  }
  window.mbTypeset = typeset;   // cho nội dung động (lời giải mở ra) và kiểm thử
  if (window.ResizeObserver) new ResizeObserver(fit).observe(document.body);
  window.addEventListener('load', function () {
    fit();
    if (window.MathJax && window.MathJax.startup && window.MathJax.startup.promise) {
      window.MathJax.startup.promise.then(function () { wrapWide(); fit(); }).catch(function () {});
    }
  });

  /* ---------- Chuẩn hóa và so khớp đáp án ---------- */
  function norm(s) {
    return String(s).toLowerCase()
      .replace(/[−–—]/g, '-').replace(/\s+/g, '')
      .replace(/;/g, ',').replace(/∞/g, 'inf').replace(/infinity/g, 'inf');
  }
  /* Số: 5, -2, 0.5, 0,5, 1/2, -3/4. Cho phép chữ đơn vị ở cuối ("5 students"). */
  function parseNumber(s, allowWords) {
    s = norm(s).replace(/\(|\)/g, '');
    if (allowWords) s = s.replace(/[a-z%]+$/, '');
    s = s.replace(',', '.');
    var m = /^([+-]?\d+(?:\.\d+)?|[+-]?\.\d+)(?:\/(\d+(?:\.\d+)?))?$/.exec(s);
    if (!m) return null;
    var v = parseFloat(m[1]);
    if (m[2] !== undefined) { var d = parseFloat(m[2]); if (d === 0) return null; v = v / d; }
    return isFinite(v) ? v : null;
  }
  function parseEnd(s) {
    if (s === 'inf' || s === '+inf') return Infinity;
    if (s === '-inf') return -Infinity;
    return parseNumber(s, false);
  }
  /* Khoảng: (a,b) [a,b] [a,b) (a,b] (-inf,b) (a,+inf) ... Dấu phân cách là dấu phẩy hoặc chấm phẩy. */
  function parseInterval(s) {
    s = norm(s);
    var m = /^([\[(])(.+?),(.+?)([\])])$/.exec(s);
    if (!m) return null;
    var a = parseEnd(m[2]), b = parseEnd(m[3]);
    if (a === null || b === null) return null;
    return { l: m[1], a: a, r: m[4], b: b };
  }
  function same(x, y) { return x === y || Math.abs(x - y) < 1e-9; }
  /* Trả về: 'ok' | 'bad' | 'unreadable' */
  function grade(value, key, kind) {
    var alts = key.split('|');
    var i, v, k;
    if (kind === 'number') {
      v = parseNumber(value, true);
      if (v === null) return 'unreadable';
      for (i = 0; i < alts.length; i++) { k = parseNumber(alts[i], false); if (k !== null && same(v, k)) return 'ok'; }
      return 'bad';
    }
    if (kind === 'interval') {
      v = parseInterval(value);
      if (!v) return 'unreadable';
      for (i = 0; i < alts.length; i++) {
        k = parseInterval(alts[i]);
        if (k && k.l === v.l && k.r === v.r && same(k.a, v.a) && same(k.b, v.b)) return 'ok';
      }
      return 'bad';
    }
    v = norm(value);
    for (i = 0; i < alts.length; i++) if (norm(alts[i]) === v) return 'ok';
    return 'bad';
  }


  /* ---------- Hiện/ẩn lời giải và bản dịch ---------- */
  document.addEventListener('click', function (e) {
    var tr = e.target.closest ? e.target.closest('[data-tr]') : null;
    if (tr) {
      var box = tr.closest('.tx');
      if (!box) return;
      var open = !box.classList.contains('is-open');
      box.classList.toggle('is-open', open);
      tr.setAttribute('aria-expanded', open ? 'true' : 'false');
      fit();
      return;
    }
    var b = e.target.closest ? e.target.closest('[data-reveal]') : null;
    if (b) {
      var t = document.getElementById(b.getAttribute('data-reveal'));
      if (!t) return;
      var opening = t.hidden;
      t.hidden = !opening;
      b.setAttribute('aria-expanded', opening ? 'true' : 'false');
      var ls = $('.lab-show', b), lh = $('.lab-hide', b);
      if (ls && lh) { ls.hidden = opening; lh.hidden = !opening; }
      if (opening) typeset(t); else fit();
      return;
    }
    var lv = e.target.closest ? e.target.closest('.mbl-levels button') : null;
    if (lv) { setLevel(+lv.getAttribute('data-level'), true); return; }
    var a = e.target.closest ? e.target.closest('[data-act]') : null;
    if (!a) return;
    var act = a.getAttribute('data-act');
    var item = a.closest('.mbl-item');
    if (act === 'check' && item) check(item);
    else if (act === 'retry' && item) retry(item);
    else if (act === 'finish') finish(a.closest('.mbl-quiz'));
    else if (act === 'resetall') $$('.mbl-item', a.closest('.mbl-quiz')).forEach(retry);
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' && e.target.classList && e.target.classList.contains('mbl-input') && e.target.tagName === 'INPUT') {
      var item = e.target.closest('.mbl-item');
      if (item && item.getAttribute('data-state') !== 'correct' && item.getAttribute('data-state') !== 'wrong') { e.preventDefault(); check(item); }
    }
  });
  document.addEventListener('change', function (e) {
    var t = e.target;
    if (t.type === 'radio') {
      var item = t.closest('.mbl-item');
      if (item) $$('label', item).forEach(function (l) { l.classList.toggle('is-picked', !!$('input:checked', l)); });
    }
    if (t.closest && t.closest('.mbl-checks')) selfCheck(t.closest('.mbl-checks'));
  });

  /* ---------- Chấm từng câu ---------- */
  function say(item, cls, html) {
    var fb = $('.mbl-fb', item);
    fb.className = 'mbl-fb ' + cls;
    fb.innerHTML = html;
    fb.hidden = false;
  }
  function lock(item, on) {
    $$('input', item).forEach(function (i) { i.disabled = on; });
    var c = $('[data-act="check"]', item), r = $('[data-act="retry"]', item);
    if (c) c.hidden = on;
    if (r) r.hidden = !on;
  }
  function check(item) {
    var type = item.getAttribute('data-type'), key = item.getAttribute('data-answer');
    var result;
    if (type === 'short') {
      var val = $('.mbl-input', item).value;
      if (!val.trim()) { say(item, 'neutral', txb('Type your answer first.', 'Hãy nhập đáp án trước.')); return; }
      result = grade(val, key, item.getAttribute('data-kind') || 'text');
      if (result === 'unreadable') {
        say(item, 'neutral', txb('I cannot read this format, so it is not graded yet. Check the format hint and try again.', 'Chưa nhận dạng được cách viết nên chưa chấm. Hãy xem gợi ý định dạng ở đề bài và nhập lại.'));
        return;
      }
    } else {
      var sel = $('input:checked', item);
      if (!sel) { say(item, 'neutral', txb('Choose an answer first.', 'Hãy chọn một đáp án trước.')); return; }
      result = sel.value === key ? 'ok' : 'bad';
      $$('label', item).forEach(function (l) {
        var inp = $('input', l);
        l.classList.remove('is-picked');
        if (inp.value === key) l.classList.add('is-right');
        else if (inp.checked) l.classList.add('is-wrong');
      });
    }
    item.setAttribute('data-state', result === 'ok' ? 'correct' : 'wrong');
    say(item, result === 'ok' ? 'ok' : 'bad',
      result === 'ok' ? txb('Correct!', 'Chính xác!') : txb('Incorrect. Read the explanation below.', 'Chưa đúng. Hãy đọc giải thích bên dưới.'));
    var ex = $('.mbl-explain', item);
    if (ex) { ex.hidden = false; typeset(ex); }
    lock(item, true);
    updateScore(item.closest('.mbl-quiz'));
    fit();
  }
  function retry(item) {
    item.removeAttribute('data-state');
    $$('input', item).forEach(function (i) { if (i.type === 'radio') i.checked = false; else i.value = ''; });
    $$('label', item).forEach(function (l) { l.classList.remove('is-picked', 'is-right', 'is-wrong'); });
    var fb = $('.mbl-fb', item), ex = $('.mbl-explain', item);
    if (fb) { fb.hidden = true; fb.innerHTML = ''; }
    if (ex) ex.hidden = true;
    lock(item, false);
    var q = item.closest('.mbl-quiz');
    updateScore(q);
    var res = q && $('.mbl-result', q); if (res) res.hidden = true;
    fit();
  }

  /* ---------- Điểm ---------- */
  function activeInLevel(item) {
    var lv = parseInt(document.body.getAttribute('data-level'), 10) || 1;
    for (var n = item; n && n !== document.body; n = n.parentElement) {
      var c = typeof n.className === 'string' ? n.className : '';
      var m = /(?:^|\s)lv-only-(\d+)(?:\s|$)/.exec(c);
      if (m && m[1].indexOf(String(lv)) < 0) return false;
      if (lv < 2 && /(?:^|\s)l23only(?:\s|$)/.test(c)) return false;
    }
    return true;
  }
  function counts(q) {
    var items = $$('.mbl-item', q).filter(activeInLevel);   /* chỉ tính các câu thuộc mức đang học (lớp lv-only-…, l23only) */
    var right = items.filter(function (i) { return i.getAttribute('data-state') === 'correct'; }).length;
    var done = items.filter(function (i) { return i.hasAttribute('data-state'); }).length;
    return { total: items.length, right: right, done: done };
  }
  function updateScore(q) {
    if (!q) return;
    var s = $('.mbl-score', q); if (!s) return;
    var c = counts(q);
    s.innerHTML = txi('Your Score: ' + c.right + ' / ' + c.total + ' (answered ' + c.done + ')', 'Điểm của bạn: ' + c.right + ' / ' + c.total + ' (đã làm ' + c.done + ')');
  }
  function finish(q) {
    if (!q) return;
    var c = counts(q), box = $('.mbl-result', q);
    if (!box) return;
    var pct = c.total ? Math.round(100 * c.right / c.total) : 0;
    var msg = c.done < c.total
      ? txb('Unanswered questions: ' + (c.total - c.done) + '.', 'Còn ' + (c.total - c.done) + ' câu chưa trả lời.')
      : (pct >= 80 ? txb('Well done! You can move on to the next lesson.', 'Làm tốt lắm! Bạn có thể học bài tiếp theo.')
                   : txb('Review the theory and try the questions again.', 'Hãy xem lại lý thuyết và làm lại các câu chưa đúng.'));
    box.innerHTML = '<p class="big">' + c.right + ' / ' + c.total + ' (' + pct + '%)</p>' + msg;
    box.hidden = false;
    /* Gửi kết quả về tài khoản (nếu học sinh đã đăng nhập) */
    var lid = document.body.getAttribute('data-lesson-id');
    if (lid && c.done && window.MathBridgeProgress && window.MathBridgeProgress.recordQuiz) {
      window.MathBridgeProgress.recordQuiz(lid, { level: parseInt(document.body.getAttribute('data-level'), 10) || 1, right: c.right, total: c.total, done: c.done, title: document.title });
    }
    fit();
  }

  /* ---------- Tự đánh giá ---------- */
  function selfCheck(list) {
    var all = $$('input[type=checkbox]', list), n = all.filter(function (c) { return c.checked; }).length;
    var out = $('.mbl-selfmsg', list.parentNode); if (!out) return;
    out.innerHTML = '<b>' + n + ' / ' + all.length + '</b>';
    fit();
  }

  /* ---------- Ba mức học tập ---------- */
  var level = 1;
  function readMode() {
    try { var i = MODES.indexOf(localStorage.getItem(KEY)); return i >= 0 ? i + 1 : 1; } catch (e) { return 1; }
  }
  function saveMode(n) { try { localStorage.setItem(KEY, MODES[n - 1]); } catch (e) { /* bị chặn: vẫn học bình thường */ } }
  function paintLevels() {
    $$('.mbl-levels button').forEach(function (b) {
      b.setAttribute('aria-checked', +b.getAttribute('data-level') === level ? 'true' : 'false');
    });
  }
  /* Phần tử đang nằm gần đầu vùng nhìn, dùng để giữ nguyên vị trí đọc khi đổi mức */
  function viewTop() {
    var bar = $('.mbl-levels'), bh = bar ? bar.offsetHeight : 0;
    try {
      var f = window.frameElement;
      if (f && f.contentDocument === document) {
        var h = window.parent.document.querySelector('.top'), hh = h ? Math.max(0, h.getBoundingClientRect().bottom) : 0;
        return { top: -f.getBoundingClientRect().top + hh + bh, scroller: window.parent };
      }
    } catch (e) { /* bỏ qua */ }
    return { top: bh, scroller: window };
  }
  function pickAnchor(vt) {
    var list = $$('h2, h3, .tx, .mbl-math, .mbl-opts, .mbl-actions'), i, r, fallback = null;
    for (i = 0; i < list.length; i++) {
      r = list[i].getBoundingClientRect();
      if (r.width <= 0 || r.height <= 0) continue;
      if (r.top >= vt.top) return { el: list[i], top: r.top };
      if (!fallback && r.bottom > vt.top + 4) fallback = { el: list[i], top: r.top };
    }
    return fallback;
  }
  function relabelBridge() {
    var box = $('.mb-complete'); if (!box) return;
    var btn = $('button', box), msg = $('span', box);
    if (btn) btn.textContent = level === 3 ? 'Complete Lesson' : 'Tôi đã học xong bài này';
    if (msg && msg.textContent) {
      var map = { 'Đã gửi xác nhận hoàn thành.': 'Completion sent.', 'Đã lưu hoàn thành trên trình duyệt này.': 'Completion saved in this browser.', 'Không lưu được. Trình duyệt có thể đang chặn LocalStorage.': 'Could not save. The browser may be blocking LocalStorage.' };
      var inv = {}; Object.keys(map).forEach(function (k) { inv[map[k]] = k; });
      if (level === 3 && map[msg.textContent]) msg.textContent = map[msg.textContent];
      else if (level !== 3 && inv[msg.textContent]) msg.textContent = inv[msg.textContent];
    }
  }
  function setLevel(n, save) {
    if (n < 1 || n > 3) return;
    var vt = viewTop(), anchor = n !== level ? pickAnchor(vt) : null;
    level = n;
    document.body.setAttribute('data-level', String(n));
    if (save) saveMode(n);
    paintLevels();
    $$('.mbl-quiz').forEach(function (q) { updateScore(q); var r = $('.mbl-result', q); if (r) r.hidden = true; });   /* điểm tính lại cho mức mới */
    hideTip();
    stopSpeech();
    relabelBridge();
    fit();
    if (anchor) {   /* giữ nguyên vị trí học hiện tại */
      var d = anchor.el.getBoundingClientRect().top - anchor.top;
      if (d) { try { vt.scroller.scrollBy({ top: d, left: 0, behavior: 'instant' }); } catch (e) { try { vt.scroller.scrollBy(0, d); } catch (e2) { /* bỏ qua */ } } }
    }
  }
  window.addEventListener('storage', function (e) { if (e.key === KEY) setLevel(readMode(), false); });
  /* ---------- Thanh chọn mức luôn nằm trong tầm nhìn (để đổi mức mà không phải cuộn lên đầu bài) ----------
     Mở riêng: position:sticky (CSS). Nhúng trong iframe tự giãn chiều cao: iframe không tự cuộn nên dịch thanh theo cuộn của trang cha. */
  function stickBar() {
    var bar = $('.mbl-levels'); if (!bar) return;
    var f = null, inFrame = false;
    try { f = window.frameElement; inFrame = !!(f && f.contentDocument === document); } catch (e) { /* bỏ qua */ }
    if (!inFrame) return;
    var slot = document.createElement('div'); slot.className = 'mbl-levels-slot';
    bar.parentNode.insertBefore(slot, bar); slot.appendChild(bar);
    bar.classList.add('is-floating');
    var par = window.parent, queued = false;
    function place() {
      queued = false;
      var h = par.document.querySelector('.top'), hh = h ? Math.max(0, h.getBoundingClientRect().bottom) : 0;
      var bh = bar.offsetHeight; slot.style.minHeight = bh + 'px';
      var slotTop = slot.getBoundingClientRect().top;
      var t = (hh - f.getBoundingClientRect().top) - slotTop;
      var max = document.body.getBoundingClientRect().height - slotTop - bh - 8;
      t = Math.max(0, Math.min(t, max));
      bar.style.transform = t ? 'translateY(' + Math.round(t) + 'px)' : '';
      bar.classList.toggle('is-lifted', t > 0);
    }
    function q() { if (!queued) { queued = true; par.requestAnimationFrame(place); } }
    try { par.addEventListener('scroll', q, { passive: true }); par.addEventListener('resize', q); } catch (e) { return; }
    if (window.ResizeObserver) new ResizeObserver(q).observe(document.body);
    q();
  }


  /* ---------- Tooltip thuật ngữ (Mức 1: rê chuột, chạm, hoặc focus bàn phím) ---------- */
  var tip = document.createElement('div');
  tip.className = 'mbl-tip'; tip.setAttribute('role', 'tooltip'); tip.hidden = true;
  document.body.appendChild(tip);
  var tipFor = null, touchMode = false;
  function hideTip() { tip.hidden = true; tipFor = null; }
  function showTip(el) {
    if (level !== 1) return;
    tip.textContent = el.getAttribute('data-en'); tip.hidden = false; tipFor = el;
    var r = el.getBoundingClientRect(), sx = window.pageXOffset, sy = window.pageYOffset;
    var left = r.left + sx + r.width / 2 - tip.offsetWidth / 2;
    left = Math.max(sx + 6, Math.min(left, sx + document.documentElement.clientWidth - tip.offsetWidth - 6));
    var top = r.top + sy - tip.offsetHeight - 6;
    if (top < sy + 2) top = r.bottom + sy + 6;
    tip.style.left = left + 'px'; tip.style.top = top + 'px';
  }
  function termOf(t) { return t && t.closest ? t.closest('b.mbl-term') : null; }
  document.addEventListener('pointerdown', function (e) { touchMode = e.pointerType === 'touch' || e.pointerType === 'pen'; }, true);
  document.addEventListener('mouseover', function (e) { var a = termOf(e.target); if (a && !touchMode) showTip(a); });
  document.addEventListener('mouseout', function (e) { if (termOf(e.target) && !touchMode) hideTip(); });
  document.addEventListener('focusin', function (e) { var a = termOf(e.target); if (a && !touchMode) showTip(a); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Tab') touchMode = false; }, true);
  document.addEventListener('focusout', function (e) { if (termOf(e.target) && !touchMode) hideTip(); });
  document.addEventListener('click', function (e) {
    var a = termOf(e.target);
    if (a && touchMode) showTip(a);
    else if (!a) hideTip();
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') hideTip(); });
  window.addEventListener('scroll', hideTip, { passive: true });


  /* ---------- Phát âm tiếng Anh (Web Speech API, giọng en-US của thiết bị) ---------- */
  var tts = window.speechSynthesis, speakingBtn = null, cachedVoice = null;
  if (!tts || !window.SpeechSynthesisUtterance) document.body.classList.add('no-tts');
  function pickVoice() {
    if (cachedVoice) return cachedVoice;
    var vs = []; try { vs = tts.getVoices() || []; } catch (e) { /* bỏ qua */ }
    var us = vs.filter(function (v) { return /^en[-_]US$/i.test(v.lang); });
    var pool = us.length ? us : vs.filter(function (v) { return /^en/i.test(v.lang); });
    var best = pool.filter(function (v) { return /natural|neural|google us|aria|jenny|guy|samantha|zira|david/i.test(v.name); })[0] || pool[0] || null;
    if (best && vs.length) cachedVoice = best;
    return best;
  }
  if (tts && tts.addEventListener) tts.addEventListener('voiceschanged', function () { cachedVoice = null; });
  function stopSpeech() {
    try { if (tts) tts.cancel(); } catch (e) { /* bỏ qua */ }
    if (speakingBtn) { speakingBtn.classList.remove('is-speaking'); speakingBtn.setAttribute('aria-pressed', 'false'); speakingBtn = null; }
  }
  function speak(text, btn) {
    if (!tts || !text) return;
    var again = btn && btn === speakingBtn;
    stopSpeech();
    if (again) return;
    var u = new SpeechSynthesisUtterance(text), v = pickVoice();
    u.lang = 'en-US'; u.rate = 0.9; u.pitch = 1;
    if (v) { u.voice = v; u.lang = v.lang; }
    if (btn) { speakingBtn = btn; btn.classList.add('is-speaking'); btn.setAttribute('aria-pressed', 'true'); }
    var done = function () { if (btn && speakingBtn === btn) { btn.classList.remove('is-speaking'); btn.setAttribute('aria-pressed', 'false'); speakingBtn = null; } };
    u.onend = done; u.onerror = done;
    tts.speak(u);
  }
  window.addEventListener('pagehide', stopSpeech);
  document.addEventListener('click', function (e) {
    var sb = e.target.closest ? e.target.closest('[data-say-btn]') : null;
    if (sb) { var box = sb.closest('.tx'), en = box && $('.en', box); if (en) speak(en.getAttribute('data-say') || en.textContent, sb); return; }
    var w = e.target.closest ? e.target.closest('b.mbl-en') : null;
    if (w) { speak(w.textContent, null); return; }
    var t = e.target.closest ? e.target.closest('b.mbl-term') : null;
    if (t && level === 1) speak(t.getAttribute('data-en'), null);
  });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Enter' && e.key !== ' ') return;
    var w = e.target.closest ? e.target.closest('b.mbl-en, b.mbl-term') : null;
    if (!w) return;
    e.preventDefault();
    if (w.classList.contains('mbl-en')) speak(w.textContent, null);
    else if (level === 1) speak(w.getAttribute('data-en'), null);
  });

  $$('.mbl-quiz').forEach(updateScore);
  level = readMode();
  document.body.setAttribute('data-level', String(level));
  paintLevels();
  stickBar();
  window.addEventListener('DOMContentLoaded', relabelBridge);
  window.addEventListener('load', relabelBridge);
})();
