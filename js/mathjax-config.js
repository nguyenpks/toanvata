/* Cấu hình MathJax dùng chung cho website và mọi bài học.
   Trong dòng: \( ... \)   Riêng dòng: \[ ... \]
   Gói ams: aligned, cases, matrix, \text, \tag... (có sẵn trong tex-chtml.js, khai báo rõ để không phụ thuộc bản dựng). */

/* ---------- Ngắt dòng cho công thức trong dòng dài (màn hình điện thoại) ----------
   MathJax 3 không tự xuống dòng bên trong một công thức \( ... \). Một dãy biến đổi dài như
   \((3x^2y+xy-1)+(x^2y-4xy+2)=3x^2y+xy-1+x^2y-4xy+2=4x^2y-3xy+1\) vì thế tràn khỏi màn hình hẹp.
   Trước khi MathJax dựng trang, ta tách các công thức dài thành nhiều công thức nhỏ nối liền nhau:
     - tách trước dấu quan hệ ở ngoài cùng (=, <, >, \le, \ge, \ne, \approx, \Rightarrow, \Leftrightarrow…);
     - mảnh nào vẫn còn dài thì tách tiếp trước dấu +, −, ×, ·, :, ÷ ở ngoài cùng;
     - tách sau dấu phẩy / chấm phẩy ở ngoài cùng (danh sách như 81^\circ,\ 99^\circ,\ ...).
   Mảnh mới bắt đầu bằng {} để giữ đúng khoảng cách của dấu (ví dụ {}=4x^2y). Giữa hai mảnh chỉ có dấu
   cách độ rộng 0 (U+200B): trên màn hình rộng công thức trông như cũ, trên màn hình hẹp trình duyệt
   được phép xuống dòng tại đó. Không tách bên trong { }, ( ), [ ], \left…\right, môi trường \begin…\end,
   và không đụng tới công thức có lệnh đổi kiểu không bao (\color, \bf, \rm…). */
(function () {
  var MIN_SPLIT = 14;      // công thức ngắn hơn (bỏ dấu cách) thì để nguyên
  var MIN_PLUS = 16;       // mảnh dài hơn mới tách tiếp ở dấu + −
  var REL = ['\\Leftrightarrow', '\\Longleftrightarrow', '\\Rightarrow', '\\Longrightarrow', '\\Leftarrow', '\\iff', '\\implies',
             '\\approx', '\\equiv', '\\gt', '\\lt', '\\leqslant', '\\geqslant', '\\leq', '\\geq', '\\le', '\\ge', '\\neq', '\\ne', '\\sim', '\\cong'];
  var STYLE_LEAD = /^\s*(\\displaystyle|\\textstyle)\s*/;
  var UNSAFE = /\\(color|bf|rm|it|sf|tt|cal|large|Large|small|tiny|huge|Huge|scriptsize|footnotesize|normalsize|over|atop|choose|tag|label)(?![a-zA-Z])/;

  var SPACE = /^\\( |,|;|:|!|quad|qquad)$/;
  var OPS = /^\\(cdot|times|div|pm|mp|cup|cap|setminus|in|notin|subset|subseteq|to|mapsto|left|right|frac|dfrac|tfrac|sqrt|overline|widehat|hat|vec|text|mathrm|operatorname)$/;
  /* Dấu + − đứng sau toán hạng thì là dấu của phép tính (cắt được); sau dấu khác / đầu mảnh là dấu âm (không cắt). */
  function isOperand(p) {
    if (!p) return false;
    if (p.charAt(0) === '\\') return p.length > 2 && REL.indexOf(p) < 0 && !OPS.test(p);
    return /^[a-zA-Z0-9)\]}'!|.%]$/.test(p);
  }

  /* Trả về danh sách vị trí cắt ở mức ngoài cùng: {pos, kind} với kind = 'rel' | 'pm' | 'comma'. */
  function scan(s) {
    var cuts = [], depth = 0, bars = false, i = 0, n = s.length, prev = '';   // prev: kí tự / lệnh có nghĩa ngay trước
    while (i < n) {
      var c = s.charAt(i);
      if (c === '\\') {
        var m = /^\\([a-zA-Z]+|.)/.exec(s.slice(i)), cmd = m ? m[0] : '\\';
        if (cmd === '\\left' || cmd === '\\right') {
          depth += cmd === '\\left' ? 1 : -1;
          i += cmd.length;
          while (s.charAt(i) === ' ') i++;
          var d = /^\\([a-zA-Z]+|.)/.exec(s.slice(i));   // bỏ qua kí hiệu ngoặc đi kèm: ( [ \{ . |
          i += d && s.charAt(i) === '\\' ? d[0].length : 1;
          prev = ')';
          continue;
        }
        if (cmd === '\\begin' || cmd === '\\end') {          // môi trường (cases, aligned…): cả khối coi như một ngoặc
          depth += cmd === '\\begin' ? 1 : -1;
          i += cmd.length;
          var env = /^\s*\{[^{}]*\}/.exec(s.slice(i));
          if (env) i += env[0].length;
          prev = ')';
          if (depth < 0) return null;
          continue;
        }
        if (depth === 0 && (cmd === '\\\\' )) return null;   // xuống dòng ở ngoài môi trường: không đụng tới
        if (depth === 0 && i > 0 && REL.indexOf(cmd) >= 0) cuts.push({ pos: i, kind: 'rel' });
        else if (depth === 0 && i > 0 && /^\\(cdot|times|div)$/.test(cmd) && isOperand(prev)) cuts.push({ pos: i, kind: 'pm' });
        i += cmd.length;
        if (!SPACE.test(cmd)) prev = cmd;   // lệnh khoảng trắng không làm đổi "kí tự trước" 
        continue;
      }
      if (c === '&' && depth === 0) return null;
      if (c === '|') { bars = !bars; depth += bars ? 1 : -1; }   // |...|: coi như một cặp ngoặc
      else if (c === '{' || c === '(' || c === '[') depth++;
      else if (c === '}' || c === ')' || c === ']') depth--;
      else if (depth === 0 && i > 0) {
        if (c === '=' || c === '<' || c === '>') cuts.push({ pos: i, kind: 'rel' });
        else if ((c === '+' || c === '-' || c === ':') && isOperand(prev)) cuts.push({ pos: i, kind: 'pm' });   // ':' = phép chia ở Mức 1
        else if ((c === ',' || c === ';') && i + 1 < n)            // phẩy / chấm phẩy ngoài cùng = ngăn cách phần tử (số thập phân viết {,})
          cuts.push({ pos: i + 1, kind: /^(\\ |\\quad|\\qquad|\\;|\\,|\\:|\s)/.test(s.slice(i + 1)) ? 'comma' : 'comma0' });
      }
      if (depth < 0) return null;   // ngoặc lệch: không đụng tới
      if (c !== ' ') prev = c;
      i++;
    }
    return depth === 0 ? cuts : null;
  }

  /* Độ dài "nhìn thấy" gần đúng: mỗi lệnh \abc tính 1 kí tự; bỏ dấu cách, { } ^ _ */
  function len(s) { return s.replace(/\\[a-zA-Z]+/g, 'c').replace(/\\./g, '').replace(/[\s{}^_]/g, '').length; }

  /* Tách một công thức (không kèm \( \)) thành các mảnh TeX; trả về null nếu để nguyên. */
  function splitTeX(tex) {
    if (len(tex) < MIN_SPLIT || UNSAFE.test(tex)) return null;
    var lead = '', m = STYLE_LEAD.exec(tex);
    if (m) { lead = m[1] + ' '; tex = tex.slice(m[0].length); }
    var cuts = scan(tex);
    if (!cuts || !cuts.length) return null;
    // 1) cắt ở dấu quan hệ và dấu phẩy; mỗi mảnh ít nhất 4 kí tự nhìn thấy, phần còn lại cũng vậy (tránh mảnh lẻ như "x" hay "=0")
    var parts = [], last = 0, lastKind = '';
    cuts.forEach(function (c) {
      if (c.kind === 'pm') return;
      if (len(tex.slice(last, c.pos)) >= 4 && len(tex.slice(c.pos)) >= 4) { parts.push({ s: tex.slice(last, c.pos), start: last, kind: lastKind }); last = c.pos; lastKind = c.kind; }
    });
    parts.push({ s: tex.slice(last), start: last, kind: lastKind });
    // 2) mảnh còn dài: cắt tiếp ở + − (mỗi bên đủ dài để không còn mảnh lẻ)
    var out = [];
    parts.forEach(function (p) {
      if (len(p.s) < MIN_PLUS) { out.push(p); return; }
      var end = p.start + p.s.length, from = p.start, kind = p.kind;
      cuts.forEach(function (c) {
        if (c.kind !== 'pm' || c.pos <= p.start || c.pos >= end) return;
        if (len(tex.slice(from, c.pos)) >= 5 && len(tex.slice(c.pos, end)) >= 5) { out.push({ s: tex.slice(from, c.pos), kind: kind }); from = c.pos; kind = 'pm'; }
      });
      out.push({ s: tex.slice(from, end), kind: kind });
    });
    if (out.length < 2) return null;
    var res = out.map(function (p, k) {
      var s = p.s.replace(/^\s*((\\ |\\quad|\\qquad|\\;|\\,)\s*)*/, '');   // khoảng trắng sau dấu phẩy: thay bằng dấu cách thật giữa hai mảnh
      // Mảnh bắt đầu bằng dấu quan hệ / dấu phép tính: thêm {} để giữ khoảng cách như khi chưa tách.
      // Mảnh sau dấu phẩy là phần tử mới của danh sách: dấu − đứng đầu là dấu âm, không thêm {}.
      return lead + (k > 0 && p.kind.indexOf('comma') < 0 ? '{}' : '') + s;
    });
    // khoảng cách giữa hai mảnh: dấu cách thật nếu bản gốc có khoảng trắng sau dấu phẩy, còn lại dấu cách độ rộng 0
    res.seps = out.map(function (p) { return p.kind === 'comma' ? ' ' : '\u200B'; });
    return res;
  }

  /* Viết lại các \( ... \) dài trong mọi nút chữ dưới root (chạy một lần cho mỗi nút). */
  var SKIP = /^(SCRIPT|NOSCRIPT|STYLE|TEXTAREA|PRE|CODE|MJX-CONTAINER)$/;
  function splitMath(root) {
    root = root || document.body;
    if (!root) return 0;
    var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode: function (t) {
        for (var p = t.parentNode; p && p !== root.parentNode; p = p.parentNode) if (p.nodeType === 1 && SKIP.test(p.nodeName)) return NodeFilter.FILTER_REJECT;
        return t.nodeValue.indexOf('\\(') >= 0 ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP;
      }
    });
    var nodes = [], t, count = 0;
    while ((t = walker.nextNode())) nodes.push(t);
    nodes.forEach(function (node) {
      var v = node.nodeValue, changed = false;
      v = v.replace(/\\\(([\s\S]*?)\\\)/g, function (all, tex) {
        var parts = splitTeX(tex);
        if (!parts) return all;
        changed = true; count++;
        var html = '';
        parts.forEach(function (p, k) {
          html += (k > 0 ? parts.seps[k] : '') + '\\(' + p + '\\)';
        });
        return html;
      });
      if (changed) node.nodeValue = v;
    });
    return count;
  }
  window.mbSplitMath = splitMath;
  window.mbSplitTeX = splitTeX;      // để kiểm thử
})();

window.MathJax = {
  tex: {
    inlineMath: [['\\(', '\\)']],
    displayMath: [['\\[', '\\]']],
    packages: { '[+]': ['ams', 'noundefined'] },   // noundefined: lệnh sai hiện đỏ tên lệnh thay vì làm hỏng cả công thức
    processEscapes: true,
    tags: 'none'
  },
  chtml: {
    displayOverflow: 'scroll',       // công thức riêng dòng quá rộng: cuộn ngang, không tràn khỏi khung
    mtextInheritFont: true,          // chữ trong \text{...} dùng cùng phông với bài học
    matchFontHeight: true
  },
  startup: {
    pageReady: function () {         // tách công thức dài trước khi dựng trang (xem ghi chú ở đầu tệp)
      try { window.mbSplitMath(document.body); } catch (e) { if (window.console) console.warn('[mbSplitMath]', e); }
      return MathJax.startup.defaultPageReady();
    }
  },
  options: {
    skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
    renderActions: {
      addMenu: [0, '', '']           // bỏ menu chuột phải: tránh chiếm thao tác chạm trên máy tính bảng
    }
  }
};
