/* MathBridge – bộ tương tác dùng chung cho bài học (AI số 2).
   Không dùng LocalStorage và không ghi hoàn thành bài: việc đó chỉ do js/lesson-bridge.js (khi học sinh bấm nút).
   Chức năng:
   1. Nút hiện/ẩn  : <button data-reveal="id" data-show-label=".." data-hide-label="..">  (lời giải, bản dịch)
   2. Câu hỏi      : .mbl-item[data-type=mcq|tf|short][data-answer][data-kind=number|interval|text]
   3. Tính điểm    : .mbl-quiz  (nút data-act="finish" / "resetall", vùng .mbl-result, .mbl-score)
   4. Tự đánh giá  : .mbl-checks
   5. Tự chỉnh chiều cao iframe cho trang cha (cùng origin).
   6. Ba mức ngôn ngữ (body[data-level]) và tooltip thuật ngữ <abbr class="mbl-term" data-en="..."> (xem lesson-kit.css).
   Mọi chuỗi do JS tạo ra dùng cặp <span class="en">/<span class="vi"> để theo mức ngôn ngữ. */
(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  /* Cặp song ngữ: hiển thị theo mức (CSS) */
  function pair(en, vi) { return '<span class="inl"><span class="en">' + en + '</span><span class="vi">' + vi + '</span></span>'; }
  function blk(en, vi) { return '<span class="en">' + en + '</span><span class="vi">' + vi + '</span>'; }

  /* ---------- Chiều cao iframe ---------- */
  function fit() {
    try {
      var f = window.frameElement;
      if (f && f.contentDocument === document) {
        f.style.height = (Math.ceil(document.body.getBoundingClientRect().height) + 12) + 'px';
      }
    } catch (e) { /* khác origin hoặc không nhúng: bỏ qua */ }
  }
  function typeset(el) {
    if (window.MathJax && window.MathJax.typesetPromise) {
      window.MathJax.typesetPromise(el ? [el] : undefined).then(fit).catch(function () {});
    }
  }
  if (window.ResizeObserver) new ResizeObserver(fit).observe(document.body);
  window.addEventListener('load', function () {
    fit();
    if (window.MathJax && window.MathJax.startup && window.MathJax.startup.promise) {
      window.MathJax.startup.promise.then(fit).catch(function () {});
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

  /* ---------- Hiện/ẩn ---------- */
  document.addEventListener('click', function (e) {
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
      if (!val.trim()) { say(item, 'neutral', pair('Type your answer first.', 'Hãy nhập đáp án trước.')); return; }
      result = grade(val, key, item.getAttribute('data-kind') || 'text');
      if (result === 'unreadable') {
        say(item, 'neutral', pair('I cannot read this format, so it is not graded yet. Check the format hint and try again.', 'Chưa nhận dạng được cách viết nên chưa chấm. Hãy xem gợi ý định dạng ở đề bài và nhập lại.'));
        return;
      }
    } else {
      var sel = $('input:checked', item);
      if (!sel) { say(item, 'neutral', pair('Choose an answer first.', 'Hãy chọn một đáp án trước.')); return; }
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
      result === 'ok' ? pair('Correct!', 'Chính xác!') : pair('Not quite. Read the explanation below.', 'Chưa đúng. Hãy đọc giải thích bên dưới.'));
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
  function counts(q) {
    var items = $$('.mbl-item', q);
    var right = items.filter(function (i) { return i.getAttribute('data-state') === 'correct'; }).length;
    var done = items.filter(function (i) { return i.hasAttribute('data-state'); }).length;
    return { total: items.length, right: right, done: done };
  }
  function updateScore(q) {
    if (!q) return;
    var s = $('.mbl-score', q); if (!s) return;
    var c = counts(q);
    s.innerHTML = pair('Score: ' + c.right + ' / ' + c.total + ' (answered ' + c.done + ')', 'Điểm: ' + c.right + ' / ' + c.total + ' (đã làm ' + c.done + ')');
  }
  /* Hoàn thành một mức = làm hết các câu chấm điểm và đạt từ 80% trở lên */
  var PASS = 80;
  function finish(q) {
    if (!q) return;
    var c = counts(q), box = $('.mbl-result', q);
    if (!box) return;
    var pct = c.total ? Math.round(100 * c.right / c.total) : 0;
    var en, vi;
    if (c.done < c.total) {
      en = 'Unanswered questions: ' + (c.total - c.done) + '.'; vi = 'Còn ' + (c.total - c.done) + ' câu chưa trả lời.';
    } else if (pct >= PASS) {
      completeLevel(level);
      if (level < 3) { en = 'Level ' + level + ' completed. Level ' + (level + 1) + ' is unlocked.'; vi = 'Đã hoàn thành Mức ' + level + '. Mức ' + (level + 1) + ' đã được mở.'; }
      else { en = 'Level 3 completed.'; vi = 'Đã hoàn thành Mức 3.'; }
    } else {
      en = 'Required score: ' + PASS + '%.'; vi = 'Cần đạt từ ' + PASS + '%.';
    }
    box.innerHTML = '<p class="big">' + c.right + ' / ' + c.total + ' (' + pct + '%)</p><p>' + blk(en, vi) + '</p>';
    box.hidden = false;
    fit();
  }

  /* ---------- Tự đánh giá ---------- */
  function selfCheck(list) {
    var all = $$('input[type=checkbox]', list), n = all.filter(function (c) { return c.checked; }).length;
    var out = $('.mbl-selfmsg', list.parentNode); if (!out) return;
    out.innerHTML = '<b>' + n + ' / ' + all.length + '</b>';
    fit();
  }

  /* ---------- Mức ngôn ngữ (mở khóa lần lượt: phải hoàn thành mức trước mới học mức sau) ---------- */
  var level = 1;      /* mức đang học */
  var unlocked = 1;   /* mức cao nhất đã mở. Chỉ lưu trong bộ nhớ trang, không dùng LocalStorage riêng (xem INTEGRATION.md) */
  function paintLevels() {
    $$('.mbl-levels button').forEach(function (b) {
      var n = +b.getAttribute('data-level'), locked = n > unlocked;
      b.setAttribute('aria-checked', n === level ? 'true' : 'false');
      b.setAttribute('aria-disabled', locked ? 'true' : 'false');
      b.classList.toggle('is-locked', locked);
      if (locked) b.setAttribute('title', 'Mức ' + (n - 1) + ' → Mức ' + n); else b.removeAttribute('title');
    });
  }
  function completeLevel(n) { if (n >= unlocked && n < 3) unlocked = n + 1; paintLevels(); }
  function resetPractice() {
    $$('.mbl-item').forEach(function (it) {
      if (it.hasAttribute('data-state')) retry(it);
      var t = $('textarea', it); if (t) t.value = '';
    });
    $$('.mbl-result').forEach(function (r) { r.hidden = true; });
    $$('.mbl-checks input').forEach(function (i) { i.checked = false; });
    $$('.mbl-selfmsg').forEach(function (m) { m.innerHTML = ''; });
  }
  function setLevel(n) {
    if (n > unlocked) return;
    var changed = n !== level;
    level = n;
    document.body.setAttribute('data-level', String(n));
    if (changed) resetPractice();   /* mỗi mức làm lại bài tập từ đầu */
    paintLevels();
    hideTip();
    fit();
  }
  document.body.setAttribute('data-level', '1');
  document.addEventListener('click', function (e) {
    var b = e.target.closest ? e.target.closest('.mbl-levels button') : null;
    if (b) setLevel(+b.getAttribute('data-level'));
  });

  /* ---------- Tooltip thuật ngữ (nổi trên trang, không bị bảng cắt) ---------- */
  var tip = document.createElement('div');
  tip.className = 'mbl-tip'; tip.setAttribute('role', 'tooltip'); tip.hidden = true;
  document.body.appendChild(tip);
  function hideTip() { tip.hidden = true; }
  function showTip(el) {
    if (level !== 1) return;
    tip.textContent = el.getAttribute('data-en'); tip.hidden = false;
    var r = el.getBoundingClientRect(), sx = window.pageXOffset, sy = window.pageYOffset;
    var left = r.left + sx + r.width / 2 - tip.offsetWidth / 2;
    left = Math.max(sx + 6, Math.min(left, sx + document.documentElement.clientWidth - tip.offsetWidth - 6));
    var top = r.top + sy - tip.offsetHeight - 6;
    if (top < sy + 2) top = r.bottom + sy + 6;
    tip.style.left = left + 'px'; tip.style.top = top + 'px';
  }
  function termOf(t) { return t && t.closest ? t.closest('abbr.mbl-term') : null; }
  document.addEventListener('mouseover', function (e) { var a = termOf(e.target); if (a) showTip(a); });
  document.addEventListener('mouseout', function (e) { if (termOf(e.target)) hideTip(); });
  document.addEventListener('focusin', function (e) { var a = termOf(e.target); if (a) showTip(a); });
  document.addEventListener('focusout', function (e) { if (termOf(e.target)) hideTip(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') hideTip(); });
  window.addEventListener('scroll', hideTip, { passive: true });

  $$('.mbl-quiz').forEach(updateScore);
  paintLevels();
})();
