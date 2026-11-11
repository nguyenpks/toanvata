(function () {
  'use strict';
  const P = window.MathBridgeProgress;
  const A = window.MathBridgeAccount;
  const $ = (s) => document.querySelector(s);
  /* Ba cấp học. Bài học khai báo grade là số từ 1 đến 12 trong lessons.json. */
  let STAGES = [
    { id: 'th', name: 'Tiểu học', range: 'Lớp 1 – Lớp 5', grades: [1, 2, 3, 4, 5], color: 'mint', hidden: true,
      desc: 'Làm quen số, phép tính và hình học đầu tiên, cùng những từ Toán tiếng Anh đơn giản.' },
    { id: 'thcs', name: 'Trung học cơ sở', range: 'Lớp 6 – Lớp 9', grades: [6, 7, 8, 9], color: 'blue', hidden: true,
      desc: 'Xây nền đại số, hình học và thống kê, chuẩn bị bước vào chương trình trung học phổ thông.' },
    { id: 'thpt', name: 'Trung học phổ thông', range: 'Lớp 10 – Lớp 12', grades: [10, 11, 12], color: 'lavender',
      desc: 'Hàm số, giải tích, vectơ, thống kê và xác suất, học song song tiếng Việt và tiếng Anh.' }
  ]; /* Bản dự phòng. Nguồn chính: "stages" trong config/model.json (nạp ở init). */
  let GRADES = [], COLOR = {};
  const stageOf = (g) => STAGES.find((st) => st.grades.indexOf(g) >= 0);
  const applyStages = (arr) => { STAGES = arr.filter((st) => !st.hidden);   /* cấp học có "hidden": true (tạm khóa) không hiện trên web */
    GRADES = STAGES.reduce((a, st) => a.concat(st.grades), []); COLOR = {}; GRADES.forEach((g) => { COLOR[g] = stageOf(g).color; }); };
  applyStages(STAGES);
  const gradeOptions = (cur, all) => (all ? '<option value="">Tất cả</option>' : '') + STAGES.map((st) =>
    `<optgroup label="${st.name}">${st.grades.map((x) => `<option value="${x}"${x === cur ? ' selected' : ''}>Lớp ${x}</option>`).join('')}</optgroup>`).join('');
  const LEVEL = { Beginner: 'Cơ bản', Intermediate: 'Trung bình', Advanced: 'Nâng cao' };
  let lessons = [], vocab = [], error = null, currentId = null;

  const esc = (s) => String(s == null ? '' : s).replace(/[&<>"']/g, (c) =>
    ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const fmt = (iso) => { try { return new Date(iso).toLocaleString('vi-VN'); } catch (e) { return iso; } };
  const live = () => lessons.filter((l) => !l.locked);   // bài tạm khóa không tính vào tiến độ, gợi ý, điều hướng
  const byGrade = (g) => live().filter((l) => l.grade === g);
  const byId = (id) => lessons.find((l) => l.id === id);

  function stats(g) {
    const list = Array.isArray(g) ? live().filter((l) => g.indexOf(l.grade) >= 0) : g ? byGrade(g) : live();
    const done = list.filter((l) => P.isComplete(l.id)).length;
    return { total: list.length, done, pct: list.length ? Math.round(done / list.length * 100) : 0 };
  }
  const bar = (p) => `<div class="bar" role="progressbar" aria-valuenow="${p}" aria-valuemin="0" aria-valuemax="100"><span style="width:${p}%"></span></div>`;
  const box = (t) => `<div class="empty">${t}</div>`;
  const link = (id) => { const l = byId(id); return l && l.locked ? esc(ttl(l)) + ' (tạm khóa)' : l ? `<a href="#/lesson/${encodeURIComponent(id)}">${esc(ttl(l))}</a>` : esc(id); };

  function go(path, params) {
    const q = new URLSearchParams();
    Object.keys(params || {}).forEach((k) => { if (params[k]) q.set(k, params[k]); });
    const s = q.toString();
    location.hash = '#' + path + (s ? '?' + s : '');
  }

  const ttl = (l) => (l.no ? 'Bài ' + l.no + '. ' : '') + l.title;   // số bài theo SGK
  function lessonCard(l) {
    if (l.locked) return `<div class="card locked" aria-disabled="true">
      <span class="chips"><span class="chip">Lớp ${l.grade}</span><span class="chip lock">Tạm khóa</span></span>
      <h3>${esc(l.title)}</h3><p>${esc(l.lockNote || 'Bài này tạm thời chưa mở.')}</p>
      <small>${esc(l.category)}</small></div>`;
    const done = P.isComplete(l.id);
    return `<a class="card ${COLOR[l.grade] || 'blue'}" href="#/lesson/${encodeURIComponent(l.id)}">
      <span class="chips"><span class="chip">Lớp ${l.grade}</span><span class="chip">${esc(LEVEL[l.level] || l.level)}</span>${done ? '<span class="chip ok">Đã hoàn thành</span>' : ''}</span>
      <h3>${esc(ttl(l))}</h3><p>${esc(l.description)}</p>
      <small>${esc(l.category)} – ${esc(l.estimatedMinutes)} phút</small></a>`;
  }
  function vocabCard(v) {
    return `<div class="card yellow"><h3>${esc(v.term)}</h3><p><b>${esc(v.vi)}</b></p>
      ${v.example ? `<p class="muted"><i>${esc(v.example)}</i></p>` : ''}
      ${v.symbol ? `<p>${esc(v.symbol)}</p>` : ''}<small>${esc(v.category)}</small></div>`;
  }
  function nextFor(g) {
    const todo = byGrade(g).filter((l) => !P.isComplete(l.id));
    const ok = (id) => { const q = byId(id); return !q || q.locked || P.isComplete(id); };   // bài tiên quyết tạm khóa coi như đã đạt
    return todo.find((l) => (l.prerequisites || []).every(ok)) || todo[0] || null;
  }

  /* ===== CÁC TRANG ===== */
  function home() {
    const A = window.MathBridgeArt || { back: '', hero: '', stage: {} };
    const cards = STAGES.map((st) => { const sx = stats(st.grades), has = live().filter((l) => st.grades.indexOf(l.grade) >= 0).length;
      const chips = st.grades.map((g) => `<a class="gchip${byGrade(g).length ? '' : ' soon'}" href="#/courses?grade=${g}">Lớp ${g}${byGrade(g).length ? '' : ' <i>sắp có</i>'}</a>`).join('');
      return `<div class="card stage ${st.color}"><span class="stage-art">${A.stage[st.id] || ''}</span>
        <h3><a href="#/courses?stage=${st.id}">${st.name}</a></h3><p class="range">${st.range}</p><p>${st.desc}</p>
        <div class="gchips">${chips}</div>${has ? bar(sx.pct) + `<small>${sx.done}/${sx.total} bài đã hoàn thành</small>` : '<small>Đang biên soạn nội dung.</small>'}</div>`; }).join('');
    const all = stats();
    return `<div class="home"><div class="home-art" aria-hidden="true">${A.back}</div>
    <section class="hero card yellow"><div class="hero-art" aria-hidden="true">${A.hero}</div><div class="hero-text">
      <h1 class="slogan">Toán Thật Dễ</h1>
      <p class="lead">Hiểu Toán bằng tiếng Việt, làm quen Toán bằng tiếng Anh!</p>
      <p class="steps-line">Học từng bước – Hiểu bản chất – Tự tin khám phá.</p>
      <div class="row"><a class="btn" href="#/dashboard">Vào học thôi</a><a class="btn ghost" href="#/courses">Xem các bài học</a></div></div></section>
    <h2>Chọn cấp học của bạn</h2><div class="grid stages">${cards}</div>
    <h2>Phương pháp học</h2><div class="grid">
      <div class="card blue"><h3>Học thuật ngữ trước</h3><p>Làm quen từ khóa tiếng Anh cùng nghĩa tiếng Việt trước khi vào bài.</p></div>
      <div class="card mint"><h3>Đọc tiếng Anh, hiểu bằng tiếng Việt</h3><p>Tài liệu viết bằng tiếng Anh đơn giản, kèm giải thích tiếng Việt.</p></div>
      <div class="card lavender"><h3>Tự xác nhận hoàn thành</h3><p>Bài chỉ được tính hoàn thành khi bạn bấm xác nhận.</p></div></div>
    <h2>Lộ trình học</h2><ol class="steps"><li>Chọn cấp học, lớp và chủ đề.</li><li>Học từng bài theo thứ tự gợi ý.</li><li>Bấm xác nhận khi đã học xong để cập nhật tiến độ.</li></ol>
    <h2>Tiến độ của bạn</h2><div class="card lavender">${bar(all.pct)}<p>${all.done}/${all.total} bài đã hoàn thành (${all.pct}%). Lưu trên trình duyệt này.</p></div></div>`;
  }

  function dashboard() {
    const d = P.get(); const g = GRADES.includes(d.grade) ? d.grade : 10; const s = stats(g);
    const recent = [], seen = {};
    d.history.forEach((h) => { if (h.type === 'view' && !seen[h.id] && byId(h.id) && !byId(h.id).locked && recent.length < 4) { seen[h.id] = 1; recent.push(byId(h.id)); } });
    const nx = nextFor(g);
    return `<h1>Tổng quan học tập</h1>
    <label class="field">Khối lớp đang học
      <select id="gradeSel">${gradeOptions(g)}</select></label>
    <div class="grid">
      <div class="card blue"><small>Tổng số bài lớp ${g}</small><div class="stat">${s.total}</div></div>
      <div class="card mint"><small>Đã hoàn thành</small><div class="stat">${s.done}</div></div>
      <div class="card lavender"><small>Tỷ lệ hoàn thành</small><div class="stat">${s.pct}%</div>${bar(s.pct)}</div></div>
    <h2>Bài học gợi ý tiếp theo</h2>${nx ? `<div class="grid">${lessonCard(nx)}</div>` : box(s.total ? 'Bạn đã hoàn thành mọi bài của lớp này.' : 'Lớp này chưa có bài học.')}
    <h2>Bài học gần đây</h2>${recent.length ? `<div class="grid">${recent.map(lessonCard).join('')}</div>` : box('Bạn chưa mở bài học nào.')}
    <h2>Truy cập nhanh</h2><div class="row"><a class="btn" href="#/vocab">Từ vựng Toán học</a><a class="btn ghost" href="#/courses?grade=${g}">Danh sách bài lớp ${g}</a></div>`;
  }

  function courses(p) {
    const g = +p.get('grade') || 0, cat = p.get('category') || '', q = (p.get('q') || '').trim();
    const stg = g ? stageOf(g) : STAGES.find((st) => st.id === p.get('stage'));
    const inScope = (l) => (g ? l.grade === g : stg ? stg.grades.indexOf(l.grade) >= 0 : true);
    const cats = [...new Set(live().filter(inScope).map((l) => l.category))];
    const ql = q.toLowerCase();
    const list = live().filter((l) => inScope(l) && (!cat || l.category === cat) &&
      (!ql || [l.title, l.description, l.category, (l.tags || []).join(' ')].join(' ').toLowerCase().includes(ql)));
    let out = `<nav class="crumb" aria-label="Breadcrumb"><a href="#/">Trang chủ</a> / <span>Chương trình học</span></nav><h1>Chương trình học</h1>
    <form id="filterForm" class="filters">
      <label class="field">Từ khóa<input type="search" name="q" value="${esc(q)}" placeholder="Tên bài, từ khóa…"></label>
      <label class="field">Cấp học<select name="stage"><option value="">Tất cả</option>${STAGES.map((st) => `<option value="${st.id}"${stg && st.id === stg.id ? ' selected' : ''}>${st.name}</option>`).join('')}</select></label>
      <label class="field">Khối lớp<select name="grade">${gradeOptions(g, true)}</select></label>
      <label class="field">Chủ đề<select name="category"><option value="">Tất cả</option>${cats.map((c) => `<option${c === cat ? ' selected' : ''}>${esc(c)}</option>`).join('')}</select></label>
      <button class="btn" type="submit">Lọc</button></form>`;
    if (!live().length) return out + box('Chưa có bài học nào trong lessons.json.');
    if (!list.length) return out + box(!q && !cat && (g || stg) ? `${g ? 'Lớp ' + g : stg.name} đang được biên soạn, chưa có bài học. <a href="#/courses">Xem tất cả bài học</a>.` : 'Không tìm thấy bài học phù hợp. Hãy thử từ khóa khác hoặc bỏ bớt bộ lọc.');
    STAGES.forEach((st) => {
      const sl = list.filter((l) => st.grades.indexOf(l.grade) >= 0); if (!sl.length) return;
      out += `<h2 class="stage-h">${st.name} <small>${st.range}</small></h2>`;
      st.grades.forEach((x) => {
        const gl = sl.filter((l) => l.grade === x); if (!gl.length) return;
        out += `<h3 class="grade-h">Toán lớp ${x}</h3>`;
        [...new Set(gl.map((l) => l.category))].forEach((c) => {
          out += `<h4 class="cat">${esc(c)}</h4><div class="grid">${gl.filter((l) => l.category === c).sort((x, y) => (x.locked ? 1 : 0) - (y.locked ? 1 : 0)).map(lessonCard).join('')}</div>`; });
      });
    });
    return out;
  }

  function lessonView(id) {
    const l = byId(id);
    if (!l || l.locked) return `<h1>Không tìm thấy bài học</h1>${box(`Không có bài học "${esc(id)}". <a href="#/courses">Quay lại chương trình học</a>.`)}`;
    if (l.locked) return `<nav class="crumb"><a href="#/">Trang chủ</a> / <a href="#/courses?grade=${l.grade}">Lớp ${l.grade}</a></nav><h1>${esc(l.title)}</h1>${box(`Bài này đang <b>tạm khóa</b>: ${esc(l.lockNote || '')}. <a href="#/courses?grade=${l.grade}">Quay lại danh sách bài</a>.`)}`;
    currentId = id;
    const sib = byGrade(l.grade), i = sib.indexOf(l), prev = sib[i - 1], next = sib[i + 1];
    const preL = (l.prerequisites || []).filter((id) => { const q = byId(id); return q && !q.locked; });
    const pre = preL.length ? `<p><b>Cần học trước:</b> ${preL.map(link).join(', ')}</p>` : '';
    return `<nav class="crumb" aria-label="Breadcrumb"><a href="#/">Trang chủ</a> / <a href="#/courses">Chương trình học</a> / <a href="#/courses?grade=${l.grade}">Lớp ${l.grade}</a> / <a href="#/courses?grade=${l.grade}&category=${encodeURIComponent(l.category)}">${esc(l.category)}</a></nav>
    <h1>${esc(ttl(l))}</h1><p>${esc(l.description)}</p>
    <p class="chips"><span class="chip">${esc(LEVEL[l.level] || l.level)}</span><span class="chip">${esc(l.estimatedMinutes)} phút</span>${(l.tags || []).map((t) => `<span class="chip">${esc(t)}</span>`).join('')}</p>${pre}
    <div id="frameWrap"><iframe id="lessonFrame" src="${esc(l.path)}" title="${esc(l.title)}"></iframe></div>
    <div id="completeBox" class="row"></div>
    <div class="row pager">${prev ? `<a class="btn ghost" href="#/lesson/${encodeURIComponent(prev.id)}">Bài trước</a>` : ''}<a class="btn ghost" href="#/courses?grade=${l.grade}">Danh sách bài</a>${next ? `<a class="btn" href="#/lesson/${encodeURIComponent(next.id)}">Bài tiếp theo</a>` : ''}</div>`;
  }
  function completeUI() {
    const b = $('#completeBox'); if (!b || !currentId) return;
    b.innerHTML = P.isComplete(currentId)
      ? '<span class="chip ok big">Bạn đã đánh dấu hoàn thành bài này</span>'
      : `<button class="btn" data-action="complete" data-id="${esc(currentId)}">Đánh dấu đã hoàn thành</button><small class="muted">Chỉ bấm khi bạn đã học xong.</small>`;
  }
  function afterLesson(l) {
    completeUI();
    const f = $('#lessonFrame');
    fetch(l.path, { method: 'HEAD' }).then((r) => {
      if (!r.ok) $('#frameWrap').innerHTML = box('Bài học này chưa có nội dung (không tìm thấy file ' + esc(l.path) + ').');
    }).catch(() => {});
    if (f) f.addEventListener('load', () => {
      try { if (!f.style.height || f.style.height === '0px') f.style.height = (f.contentDocument.documentElement.scrollHeight + 8) + 'px'; } catch (e) { /* giữ chiều cao mặc định */ }
    });
  }

  function vocabView(p) {
    const q = (p.get('q') || '').trim(), cat = p.get('category') || '', ql = q.toLowerCase();
    const cats = [...new Set(vocab.map((v) => v.category))].sort();
    const list = vocab.filter((v) => (!cat || v.category === cat) && (!ql || [v.term, v.vi, v.example].join(' ').toLowerCase().includes(ql)));
    return `<h1>Từ vựng Toán học</h1>
    <form id="vocabForm" class="filters">
      <label class="field">Tìm thuật ngữ<input type="search" name="q" value="${esc(q)}" placeholder="Tiếng Anh hoặc tiếng Việt"></label>
      <label class="field">Chủ đề<select name="category"><option value="">Tất cả</option>${cats.map((c) => `<option${c === cat ? ' selected' : ''}>${esc(c)}</option>`).join('')}</select></label>
      <button class="btn" type="submit">Tìm</button></form>
    ${!vocab.length ? box('Chưa có dữ liệu trong data/vocab.json.') : list.length ? `<div class="grid">${list.map(vocabCard).join('')}</div>` : box('Không tìm thấy thuật ngữ phù hợp.')}`;
  }

  function progressView() {
    const d = P.get(), done = Object.keys(d.completed).map(byId).filter(Boolean);
    const topics = [...new Set(done.map((l) => `Lớp ${l.grade} – ${l.category}`))];
    const seen = [...new Set(d.history.filter((h) => h.type === 'view').map((h) => h.id))].filter(byId).length;
    return `<h1>Tiến độ học tập</h1>
    ${A.user() ? `<div class="note">Tiến độ đang lưu vào tài khoản <b>${esc(A.user().tk)}</b> (${esc(A.user().ten)}, lớp ${esc(A.user().lop)}). Đăng nhập ở máy khác sẽ thấy cùng tiến độ.${A.status ? ' ' + esc(A.status) : ''}${A.pending() ? ` Còn ${A.pending()} hoạt động chờ gửi.` : ''}</div>`
      : `<div class="note">Bạn chưa đăng nhập: tiến độ chỉ lưu trên trình duyệt của thiết bị này.${A.enabled ? ' <a href="#/login">Đăng nhập</a> để lưu theo tài khoản và học tiếp trên máy khác.' : ''}</div>`}
    <div class="grid"><div class="card blue"><small>Số bài đã học (đã mở)</small><div class="stat">${seen}</div></div>
      <div class="card mint"><small>Số bài đã hoàn thành</small><div class="stat">${done.length}</div></div></div>
    <h2>Hoàn thành theo cấp học</h2><div class="grid">${STAGES.map((st) => { const s = stats(st.grades), gs = st.grades.filter((g) => byGrade(g).length).map((g) => { const t = stats(g); return `Lớp ${g}: ${t.done}/${t.total}`; }).join(' · ');
      return `<div class="card ${st.color}"><h3>${st.name}</h3><p class="range">${st.range}</p>${bar(s.pct)}<small>${s.total ? `${s.done}/${s.total} (${s.pct}%)` : 'Đang biên soạn'}</small>${gs ? `<p><small>${gs}</small></p>` : ''}</div>`; }).join('')}</div>
    <h2>Chủ đề đã học</h2>${topics.length ? `<p class="chips">${topics.map((t) => `<span class="chip">${esc(t)}</span>`).join('')}</p>` : box('Chưa có chủ đề nào hoàn thành.')}
    ${quizTable(d)}
    <h2>Lịch sử học tập</h2>${d.history.length ? `<ul class="hist">${d.history.slice(0, 20).map((h) => `<li>${fmt(h.at)} – ${h.type === 'complete' ? 'Hoàn thành' : 'Đã mở'}: ${link(h.id)}</li>`).join('')}</ul>` : box('Chưa có lịch sử.')}
    ${A.user() ? '' : '<p><button class="btn ghost" data-action="reset">Xóa toàn bộ tiến độ</button></p>'}`;
  }
  function quizTable(d) {
    const rows = Object.keys(d.quiz || {}).map((k) => d.quiz[k]).sort((a, b) => (a.lastAt < b.lastAt ? 1 : -1));
    if (!rows.length) return '';
    return `<h2>Kết quả luyện tập</h2><div class="tbl-wrap"><table class="tbl"><thead><tr><th>Bài</th><th>Mức</th><th>Số lần nộp</th><th>Lần gần nhất</th><th>Cao nhất</th></tr></thead><tbody>${rows.map((q) =>
      `<tr><td>${link(q.id)}</td><td>Mức ${esc(q.level)}</td><td>${q.attempts}</td><td>${q.last}%</td><td>${q.best}%</td></tr>`).join('')}</tbody></table></div>`;
  }
  function loginView() {
    if (!A.enabled) return `<h1>Đăng nhập</h1>${box('Website chưa bật chức năng đăng nhập.')}`;
    const u = A.user();
    if (u) return `<h1>Tài khoản</h1><div class="card mint acct-card"><h3>${esc(u.ten)}</h3><p>Lớp ${esc(u.lop)} · Tên đăng nhập: <b>${esc(u.tk)}</b></p>
      <p class="muted">${esc(A.status || 'Tiến độ học của bạn được lưu vào tài khoản.')}</p>
      <div class="row"><a class="btn" href="#/dashboard">Vào học</a><a class="btn ghost" href="#/progress">Xem tiến độ</a><button class="btn ghost" data-action="logout">Đăng xuất</button></div></div>`;
    return `<h1>Đăng nhập</h1>
    <form id="loginForm" class="card login-card" autocomplete="on">
      <label class="field">Tên đăng nhập<input name="user" required autocomplete="username" autocapitalize="none" spellcheck="false" placeholder="Ví dụ: MNNAnh10a1"></label>
      <label class="field">Mật khẩu<input name="pass" type="password" required autocomplete="current-password" inputmode="numeric" placeholder="Mật khẩu do giáo viên cấp"></label>
      <p id="loginMsg" class="err" role="alert"></p>
      <button class="btn" type="submit">Đăng nhập</button>
      <p class="muted"><small>Tài khoản do giáo viên cấp. Quên mật khẩu, hãy hỏi giáo viên. Trên máy dùng chung, nhớ bấm Đăng xuất khi học xong.</small></p>
    </form>`;
  }
  function acctUI() {
    const el = $('#acct'); if (!el) return;
    if (!A.enabled) { el.innerHTML = ''; return; }
    const u = A.user();
    el.innerHTML = u ? `<a class="acct-chip" href="#/login" title="Tài khoản"><span class="acct-dot">${esc((u.ten.split(' ').pop() || '?')[0])}</span><span class="acct-name">${esc(u.ten.split(' ').slice(-2).join(' '))}</span></a>`
      : '<a class="btn small ghost" href="#/login">Đăng nhập</a>';
  }

  /* ===== ĐIỀU HƯỚNG ===== */
  function render() {
    const [path, qs] = (location.hash.slice(1) || '/').split('?');
    const params = new URLSearchParams(qs || ''), parts = path.split('/').filter(Boolean), route = parts[0] || 'home';
    const view = $('#view'); currentId = null;
    if (error) view.innerHTML = `<h1>Không tải được dữ liệu</h1>${box(esc(error))}`;
    else if (route === 'home') view.innerHTML = home();
    else if (route === 'dashboard') view.innerHTML = dashboard();
    else if (route === 'courses') view.innerHTML = courses(params);
    else if (route === 'vocab') view.innerHTML = vocabView(params);
    else if (route === 'progress') view.innerHTML = progressView();
    else if (route === 'login') view.innerHTML = loginView();
    else if (route === 'lesson') {
      const id = decodeURIComponent(parts[1] || ''), l = byId(id);
      view.innerHTML = lessonView(id);
      if (l) { P.recordView(id); afterLesson(l); }
    } else view.innerHTML = `<h1>Không tìm thấy trang</h1>${box('<a href="#/">Về trang chủ</a>')}`;
    document.querySelectorAll('#side [data-nav]').forEach((a) => a.classList.toggle('on', a.dataset.nav === (route === 'lesson' ? 'courses' : route)));
    closeMenu(); window.scrollTo(0, 0);
    if (window.MathJax && MathJax.typesetPromise) MathJax.typesetPromise([view]).catch(() => {});
  }
  function closeMenu() { document.body.classList.remove('menu-open'); $('#menuBtn').setAttribute('aria-expanded', 'false'); }

  document.addEventListener('submit', (e) => {
    const f = e.target;
    if (f.id === 'loginForm') {
      e.preventDefault(); const d = new FormData(f), btn = f.querySelector('button[type=submit]'), msg = $('#loginMsg');
      btn.disabled = true; btn.textContent = 'Đang đăng nhập…'; msg.textContent = '';
      A.login(d.get('user').trim(), d.get('pass').trim()).then(() => { acctUI(); go('/dashboard'); })
        .catch((err) => { msg.textContent = err.message; btn.disabled = false; btn.textContent = 'Đăng nhập'; });
      return;
    }
    if (f.id === 'searchForm') { e.preventDefault(); go('/courses', { q: $('#q').value.trim() }); }
    else if (f.id === 'filterForm') { e.preventDefault(); const d = new FormData(f); go('/courses', { q: d.get('q').trim(), stage: d.get('grade') ? '' : d.get('stage'), grade: d.get('grade'), category: d.get('category') }); }
    else if (f.id === 'vocabForm') { e.preventDefault(); const d = new FormData(f); go('/vocab', { q: d.get('q').trim(), category: d.get('category') }); }
  });
  document.addEventListener('change', (e) => {
    if (e.target.id === 'gradeSel') { P.setGrade(+e.target.value); render(); }
  });
  document.addEventListener('click', (e) => {
    const b = e.target.closest('[data-action]'); if (!b) return;
    if (b.dataset.action === 'menu') {
      const open = document.body.classList.toggle('menu-open'); b.setAttribute('aria-expanded', String(open));
    } else if (b.dataset.action === 'closemenu') {
      closeMenu();
    } else if (b.dataset.action === 'complete') {
      if (!P.markComplete(b.dataset.id)) alert('Không lưu được tiến độ. Trình duyệt có thể đang chặn LocalStorage.');
      completeUI();
    } else if (b.dataset.action === 'logout') {
      b.disabled = true; A.logout().then(() => { acctUI(); go('/login'); render(); });
    } else if (b.dataset.action === 'reset') {
      if (confirm('Xóa toàn bộ tiến độ đã lưu trên trình duyệt này?')) { P.reset(); render(); }
    }
  });
  /* Nhận xác nhận hoàn thành từ bài học nhúng trong iframe (chỉ cùng origin, đúng iframe, đúng bài) */
  window.addEventListener('message', (e) => {
    if (e.origin !== location.origin) return;
    const f = $('#lessonFrame');
    if (!f || e.source !== f.contentWindow) return;
    const d = e.data;
    if (!d || d.type !== 'mathbridge:lesson-complete' || d.lessonId !== currentId) return;
    P.markComplete(d.lessonId); completeUI();
  });
  window.addEventListener('hashchange', render);
  window.addEventListener('storage', (e) => { if (e.key === P.KEY && !currentId) render(); });
  A.onChange(() => { acctUI(); const r = (location.hash.slice(1) || '/').split('?')[0].split('/')[1] || 'home';
    if (currentId) completeUI(); else if (['dashboard', 'progress'].indexOf(r) >= 0 || (r === 'login' && !document.getElementById('loginForm'))) render(); });

  async function init() {
    try {
      const [a, b, c] = await Promise.all([fetch('lessons.json'), fetch('data/vocab.json'), fetch('config/model.json')]);
      if (c.ok) { try { const m = await c.json(); if (Array.isArray(m.stages) && m.stages.length) applyStages(m.stages); } catch (e) { /* dùng bản dự phòng */ } }
      if (!a.ok) throw new Error('lessons.json (mã ' + a.status + ')');
      lessons = await a.json();
      vocab = b.ok ? await b.json() : [];
      if (!Array.isArray(lessons)) throw new Error('lessons.json phải là một mảng');
      const tmap = {}; lessons.forEach((l) => { tmap[l.id] = 'Lớp ' + l.grade + ' – ' + ttl(l); }); P.setTitles(tmap);
    } catch (e) {
      error = 'Hãy chạy website bằng máy chủ tĩnh (xem README.md), không mở trực tiếp file index.html. Chi tiết: ' + e.message;
    }
    acctUI(); render(); A.refresh();
  }
  init();
})();
