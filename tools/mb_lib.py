# -*- coding: utf-8 -*-
"""Thư viện sinh bài học MathBridge theo quy định ba mức học tập (v2).
Mỗi đoạn nội dung viết MỘT lần với cặp (en, vi) -> cùng kiến thức, công thức, ví dụ, câu hỏi, đáp án ở cả ba mức.
Thuật ngữ trong chuỗi tiếng Việt đánh dấu [[thuật ngữ]] hoặc [[hiển thị|khóa]]; thư viện tra data/vocab.json để gắn từ tiếng Anh
cho tooltip (bảo đảm một thuật ngữ luôn ứng với đúng một từ tiếng Anh trong toàn bộ bài)."""
import json, os, re, math

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_vocab = {}

def load_vocab():
    global _vocab
    data = json.load(open(os.path.join(ROOT, 'data', 'vocab.json'), encoding='utf-8'))
    _vocab = {v['vi'].lower(): v['term'] for v in data}
    return data

def ensure_vocab(entries):
    """Thêm các thuật ngữ còn thiếu vào data/vocab.json (idempotent). entries: (id, term, vi, category, example, symbol)."""
    data = load_vocab()
    have = {v['id'] for v in data}
    added = []
    for (i, term, vi, cat, ex, sym) in entries:
        if i in have or vi.lower() in _vocab:
            continue
        d = {'id': i, 'term': term, 'vi': vi, 'category': cat, 'example': ex}
        if sym: d['symbol'] = sym
        data.append(d); added.append(term)
    if added:
        json.dump(data, open(os.path.join(ROOT, 'data', 'vocab.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    load_vocab()
    return added

_used_terms = {}
def terms(vi):
    def rep(m):
        body = m.group(1)
        shown, key = (body.split('|', 1) + [None])[:2] if '|' in body else (body, body)
        k = key.lower()
        if k not in _vocab:
            raise KeyError('Thuật ngữ chưa có trong vocab.json: ' + k)
        _used_terms[k] = _vocab[k]
        return '<b class="mbl-term" tabindex="0" data-en="%s">%s</b>' % (_vocab[k], shown)
    return re.sub(r'\[\[(.+?)\]\]', rep, vi)

_AUTO = {}
def autoterms(html):
    """Bọc tự động thuật ngữ trong vocab.json (từ 2 âm tiết trở lên) ở phần tiếng Việt của câu hỏi để Mức 1 có hover.
    Bỏ qua công thức, thẻ HTML và thuật ngữ đã bọc."""
    if _AUTO.get('n') != len(_vocab):
        ks = sorted((k for k in _vocab if ' ' in k or len(k) >= 6), key=len, reverse=True)
        _AUTO['n'] = len(_vocab); _AUTO['re'] = re.compile(r'(?<!\w)(' + '|'.join(re.escape(k) for k in ks) + r')(?!\w)', re.I) if ks else None
    rx = _AUTO['re']
    if not rx: return html
    def rep(m):
        k = m.group(1).lower(); _used_terms[k] = _vocab[k]
        return '<b class="mbl-term" tabindex="0" data-en="%s">%s</b>' % (_vocab[k], m.group(1))
    parts = re.split(r'(<b class="mbl-term".*?</b>|\\\(.*?\\\)|\\\[.*?\\\]|<[^>]*>)', html, flags=re.S)
    return ''.join(x if i % 2 else rx.sub(rep, x) for i, x in enumerate(parts))

def plain(en):
    if '[[' in en: raise ValueError('Không dùng [[ ]] trong tiếng Anh: ' + en)
    return en

BTN = '<button type="button" class="mbl-tr" data-tr aria-expanded="false" aria-label="Dịch sang tiếng Việt" title="Dịch sang tiếng Việt">🌐 VI</button>'

SAY = '<button type="button" class="mbl-say" data-say-btn aria-pressed="false" aria-label="Nghe đọc tiếng Anh / Listen" title="Listen">🔊</button>'

def _frac(t):
    # \dfrac{A}{B} -> A over B (lặp cho đến khi hết)
    pat = re.compile(r'\\[dt]?frac\s*\{([^{}]*)\}\s*\{([^{}]*)\}')
    while pat.search(t): t = pat.sub(lambda m: ' , %s , over %s , ' % (m.group(1), m.group(2)), t)
    return t

def _target(t):
    t = t.strip()
    t = re.sub(r'^(.*)\^\{?\+\}?$', r'\1 from the right', t)
    t = re.sub(r'^(.*)\^\{?-\}?$', r'\1 from the left', t)
    return t

def speak_math(tex):
    t = tex
    t = re.sub(r'\\(displaystyle|big|Big|bigg|left|right|,|;|!|quad|qquad)', ' ', t)
    t = re.sub(r'\\lim_\{\s*([a-zA-Z])\s*\\to\s*([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}', lambda m: ' the limit as %s approaches %s of ' % (m.group(1), _target(m.group(2))), t)
    t = re.sub(r'\\([dt]?frac)\s*([0-9a-zA-Z])\s*([0-9a-zA-Z])', r'\\\1{\2}{\3}', t)
    t = re.sub(r'\\([dt]?frac)\s*([0-9a-zA-Z])\s*\{', r'\\\1{\2}{', t)
    t = _frac(t); t = _frac(t)
    t = re.sub(r'\\sqrt\{([^{}]*)\}', r' square root of \1 ', t)
    t = re.sub(r'\\text\{([^{}]*)\}', r' \1 ', t)
    t = re.sub(r'\^\{?2\}?', ' squared ', t); t = re.sub(r'\^\{?3\}?', ' cubed ', t)
    t = re.sub(r'\^\{?4\}?', ' to the fourth ', t)
    t = re.sub(r'\^\{?([a-zA-Z0-9]+)\}?', r' to the power \1 ', t)
    for k, v in [('0','zero'),('1','one'),('2','two'),('3','three')]:
        t = re.sub(r'_\{?%s\}?' % k, ' ' + v + ' ', t)
    t = re.sub(r'_\{?([a-zA-Z]+)\}?', r' sub \1 ', t)
    rep = [('\\int', ' the integral of '), ('\\tan', ' tangent '), ('\\cot', ' cotangent '), ('\\ln', ' natural log of '), ('\\pm\\infty', ' plus or minus infinity '), ('+\\infty', ' positive infinity '), ('-\\infty', ' negative infinity '), ('\\infty', ' infinity '),
           ('\\to', ' approaches '), ('\\le', ' is less than or equal to '), ('\\ge', ' is greater than or equal to '), ('\\ne', ' is not equal to '),
           ('\\lt', ' is less than '), ('\\gt', ' is greater than '), ('\\cdot', ' times '), ('\\pm', ' plus or minus '), ('\\cup', ' union '), ('\\cap', ' intersection '),
           ('\\setminus', ' without '), ('\\mid', ' such that '), ('\\in', ' belongs to '), ('\\mathbb{R}', ' the real numbers '), ('\\deg', ' degree of '),
           ('\\arctan', ' arc tangent '), ('\\sin', ' sine '), ('\\cos', ' cosine '), ('\\varnothing', ' the empty set '), ('\\Delta', ' delta '), ('\\sum', ' the sum of '),
           ('\\Rightarrow', ' implies '), ('\\Leftrightarrow', ' if and only if '), ('\\pi', ' pi '), ('\\overrightarrow', ' vector '), ('\\vec', ' vector '),
           ('=', ' equals '), ('<', ' is less than '), ('>', ' is greater than '), ('+', ' plus '), ("''", ' double prime '), ("'", ' prime '), ('\\{', ' '), ('\\}', ' '), ('|', ' absolute value ')]
    for a, b in rep: t = t.replace(a, b)
    t = re.sub(r'(?<![\w)\]])-\s*(?=[\w(\\])', ' minus ', t); t = t.replace('-', ' minus ')
    t = re.sub(r'\b([fgFGPQS])\s*((?:double )?prime)?\s*\(([^()]*)\)', lambda m: '%s %sof %s' % (m.group(1), (m.group(2) + ' ') if m.group(2) else '', m.group(3)), t)
    t = re.sub(r'\\[a-zA-Z]+', ' ', t); t = re.sub(r'[{}()\[\]$\\^_]', ' ', t)
    t = re.sub(r'(\d)([a-zA-Z])', r'\1 \2', t)
    t = t.replace('+', ' plus ')
    return re.sub(r'\s+', ' ', t).strip()

def say_text(en):
    x = re.sub(r'\\\((.+?)\\\)', lambda m: ' ' + speak_math(m.group(1)) + ' ', en, flags=re.S)
    x = re.sub(r'<[^>]+>', '', x)
    x = re.sub(r'\s+([,.;:?!])', r'\1', re.sub(r'\s+', ' ', x)).strip()
    return x.replace('"', '&quot;')

def T(en, vi, tag='p', auto=False):
    """Khối văn bản: Mức 1 = vi; Mức 2 = en + nút dịch + nút nghe; Mức 3 = en + nút nghe."""
    if '<table' in en or '<table' in vi: tag = 'div'
    return '<div class="tx"><%s class="en" data-say="%s">%s</%s>%s%s<%s class="vi">%s</%s></div>' % (tag, say_text(plain(en)), plain(en), tag, SAY, BTN, tag, autoterms(terms(vi)) if auto else terms(vi), tag)

def VOC(en, vi):
    """Mục từ vựng: từ in đậm tiếng Anh bấm để nghe."""
    en = re.sub(r'<b>(.+?)</b>', lambda m: '<b class="mbl-en" tabindex="0" role="button" title="Listen">%s</b>' % m.group(1), en)
    return T(en, vi)

def reset():
    _rid[0] = 0; _qid[0] = 0; del _sec[:]

def TI(en, vi):
    """Nhãn ngắn trên một dòng (không có nút dịch)."""
    return '<span class="txi"><span class="en">%s</span><span class="vi">%s</span></span>' % (plain(en), terms(vi))

def HT(en, vi):
    return '<span class="tx htx"><span class="en">%s</span>%s<span class="vi">%s</span></span>' % (plain(en), BTN, terms(vi))

def M(tex):
    return '<div class="mbl-math">\\[ %s \\]</div>' % tex

def UL(items):
    return '<ul>' + ''.join('<li>%s</li>' % i for i in items) + '</ul>'

def OL(items):
    return '<ol class="mbl-steps">' + ''.join('<li>%s</li>' % i for i in items) + '</ol>'

def BOX(kind, title, *inner):
    t = '<p class="t">%s</p>' % TI(*title) if title else ''
    return '<div class="box %s">%s%s</div>' % (kind, t, ''.join(inner))

# ---------- Hình vẽ đồ thị bằng SVG ----------
def svg_graph(f, xr, yr, vlines=(), hlines=(), lines=(), w=340, h=250, label_pts=()):
    (x0, x1), (y0, y1) = xr, yr
    pad = 26
    sx = lambda x: pad + (x - x0) / (x1 - x0) * (w - 2 * pad)
    sy = lambda y: h - pad - (y - y0) / (y1 - y0) * (h - 2 * pad)
    o = ['<svg viewBox="0 0 %d %d" role="img" xmlns="http://www.w3.org/2000/svg" font-family="Segoe UI,Arial,sans-serif" font-size="12">' % (w, h)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="#ffffff"/>' % (w, h))
    if x0 < 0 < x1: o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="#4b675c" stroke-width="1"/>' % (sx(0), pad - 8, sx(0), h - pad + 8))
    if y0 < 0 < y1: o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#4b675c" stroke-width="1"/>' % (pad - 8, sy(0), w - pad + 8, sy(0)))
    o.append('<text x="%d" y="%.1f" fill="#123428" font-style="italic">x</text>' % (w - pad + 10, (sy(0) if y0 < 0 < y1 else h - pad) + 4))
    o.append('<text x="%.1f" y="%d" fill="#123428" font-style="italic">y</text>' % ((sx(0) if x0 < 0 < x1 else pad) + 6, pad - 10))
    dash = 'stroke="#b4415a" stroke-width="1.6" stroke-dasharray="6 4"'
    for a in vlines:
        o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" %s/>' % (sx(a), pad - 8, sx(a), h - pad + 8, dash))
        o.append('<text x="%.1f" y="%d" fill="#b4415a">x = %s</text>' % (sx(a) + 4, pad - 2, ('%g' % a)))
    for b in hlines:
        o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" %s/>' % (pad - 8, sy(b), w - pad + 8, sy(b), dash))
        o.append('<text x="%d" y="%.1f" fill="#b4415a" text-anchor="end">y = %s</text>' % (w - pad, sy(b) - 5, ('%g' % b)))
    for (m, c, lab) in lines:   # đường xiên y = m x + c
        xa, xb = x0, x1
        ya, yb = m * xa + c, m * xb + c
        o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" %s/>' % (sx(xa), sy(ya), sx(xb), sy(yb), dash))
        o.append('<text x="%.1f" y="%.1f" fill="#b4415a">%s</text>' % (w - pad - 70, pad + 14, lab))
    # đường cong: tách nhánh khi vượt khung hoặc không xác định
    N = 900
    seg, segs = [], []
    for i in range(N + 1):
        x = x0 + (x1 - x0) * i / N
        try:
            y = f(x)
        except ZeroDivisionError:
            y = None
        if y is None or not math.isfinite(y) or y < y0 - 0.5 or y > y1 + 0.5:
            if len(seg) > 1: segs.append(seg)
            seg = []
        else:
            seg.append((x, y))
    if len(seg) > 1: segs.append(seg)
    for s in segs:
        d = 'M' + ' L'.join('%.1f %.1f' % (sx(x), sy(y)) for x, y in s)
        o.append('<path d="%s" fill="none" stroke="#046B4D" stroke-width="2.4" stroke-linejoin="round"/>' % d)
    for (x, y, lab) in label_pts:
        o.append('<circle cx="%.1f" cy="%.1f" r="4" fill="#ffffff" stroke="#046B4D" stroke-width="2"/>' % (sx(x), sy(y)))
    o.append('</svg>')
    return ''.join(o)

def FIG(svg, cap_en, cap_vi, alt_en, alt_vi):
    return '<figure class="mbl-fig">%s<figcaption>%s</figcaption></figure>' % (svg.replace('role="img"', 'role="img" aria-label="%s"' % alt_en), TI(cap_en, cap_vi))

# ---------- Đồ thị và hình vẽ tương tác (JSXGraph; xem docs/GRAPH.md) ----------
def _mbg(cfg, kind, cap, alt, height):
    import html as _h
    cfg = dict(cfg); cfg['kind'] = kind
    data = _h.escape(json.dumps(cfg, ensure_ascii=False, separators=(',', ':')), quote=True)
    label = ' aria-label="%s"' % _h.escape(alt[0], quote=True) if alt else ''
    c = '<figcaption>%s</figcaption>' % TI(*cap) if cap else ''
    return ('<figure class="mbl-fig mbg-fig"><div class="mbg" role="group"%s style="--mbg-h:%dpx" data-mbg="%s"></div>%s</figure>'
            % (label, height, data, c))

def GRAPH(cfg, cap=None, alt=None, height=360):
    """Đồ thị hàm số tương tác: cfg = {view:[xmin,xmax,ymin,ymax], functions:[{f:'x^2-1', label:'y = x² − 1'}], ...}."""
    return _mbg(cfg, 'graph', cap, alt, height)

def GEO(cfg, cap=None, alt=None, height=360):
    """Hình học phẳng dựng bằng quan hệ thật: cfg = {view:[...], steps:[{type:'point',...},{type:'perpendicular',...}]}."""
    return _mbg(cfg, 'geo', cap, alt, height)

def GEO3D(cfg, cap=None, alt=None, height=380):
    """Hình không gian TĨNH: vẽ bằng TikZ, biên dịch thành SVG (tools/mb_tikz3d.py). Nét khuất tự tính; không xoay."""
    import html as _h
    from mb_tikz3d import svg as _svg
    fn = _svg(cfg)
    drop = re.compile(r'\s*(Drag (the figure )?to rotate( the cube)?\.?|(Hãy )?[Kk]éo (hình )?để xoay hình( lập phương)?\.?)')
    c = '<figcaption>%s</figcaption>' % TI(drop.sub('', cap[0]), drop.sub('', cap[1])) if cap else ''
    a = _h.escape(alt[0] if alt else 'Figure', quote=True)
    return ('<figure class="mbl-fig mbl-fig3d"><img src="../../../img/fig3d/%s" alt="%s" loading="lazy" '
            'style="display:block;margin:0 auto;width:min(100%%,%dpx);height:auto"></figure>' % (fn, a, cfg.get('px', 440))).replace('</figure>', c + '</figure>')

def LEVEL_PRACTICE(titles, sets):
    """Bài tập mỗi mức một bộ RIÊNG nhưng cùng dạng (khác số liệu/hàm số), không dịch lại cùng một bài.
    titles: [(en, vi), ...] tên các nhóm A, B, C...; sets: {1: [mục_nhóm_A, mục_nhóm_B, ...], 2: [...], 3: [...]}.
    Mỗi mức phải có cùng số nhóm và cùng số câu mỗi nhóm; chỉ bộ của mức đang học được hiện và được tính điểm."""
    assert sorted(sets) == [1, 2, 3], 'cần đủ ba bộ bài tập cho Mức 1, 2, 3'
    shape = [len(g) for g in sets[1]]
    for lv in (2, 3):
        assert [len(g) for g in sets[lv]] == shape and len(sets[lv]) == len(titles), 'ba bộ phải cùng dạng (cùng số nhóm, số câu)'
    return [(titles[i], sets[lv][i], [lv]) for lv in (1, 2, 3) for i in range(len(titles))]

def LV(levels, html):
    """Chỉ hiện nội dung ở các mức học nêu (ví dụ LV([1], ...) = chỉ Mức 1)."""
    c = level_class(levels)
    return '<div class="%s">%s</div>' % (c, html) if c else html

# ---------- Cấu trúc bài ----------
_sec = []
_rid = [0]
_qid = [0]

def H2(n, en, vi):
    _sec.append((n, en, vi))
    return '<h2 id="s%d"><span class="mbl-no">%d</span><span>%s</span></h2>' % (n, n, HT(en, vi))

def REVEAL(inner):
    _rid[0] += 1
    i = 'r%d' % _rid[0]
    return ('<div class="mbl-reveal"><button type="button" class="mbl-btn ghost" data-reveal="%s" aria-expanded="false" aria-controls="%s">'
            '<span class="lab-show">%s</span><span class="lab-hide" hidden>%s</span></button>'
            '<div id="%s" class="mbl-panel" hidden>%s</div></div>') % (i, i, TI('Show Solution', 'Xem lời giải'), TI('Hide Solution', 'Ẩn lời giải'), i, inner)

def EXAMPLE(n, tag, title, problem, analysis, steps, answer_html):
    s = '<section class="mbl-ex" aria-label="Example %d">' % n
    s += '<h3>%s %d<span class="mbl-tag">%s</span> – %s</h3>' % (TI('Example', 'Ví dụ'), n, TI(*tag), TI(*title))
    s += '<div class="box blue">%s</div>' % problem
    if isinstance(analysis, str):          # khối T(...) đã dựng sẵn: chèn nhãn "Phân tích" vào hai dòng en / vi
        if re.sub(r'<[^>]+>|\s', '', analysis):
            analysis = re.sub(r'(<(p|div) class="en"[^>]*>)', r'\1<b>Analysis:</b> ', analysis, count=1)
            s += re.sub(r'(<(p|div) class="vi">)', r'\1<b>Phân tích:</b> ', analysis, count=1)
    elif analysis and (analysis[0] or analysis[1]):
        s += '<div class="tx"><p class="en"><b>Analysis:</b> %s</p>%s<p class="vi"><b>Phân tích:</b> %s</p></div>' % (plain(analysis[0]), BTN, terms(analysis[1]))
    s += REVEAL(OL(steps) + '<div class="mbl-answer">%s %s</div>' % (TI('Answer:', 'Đáp số:'), answer_html))
    return s + '</section>'

def _actions():
    return ('<div class="mbl-actions"><button type="button" class="mbl-btn" data-act="check">%s</button>'
            '<button type="button" class="mbl-btn ghost" data-act="retry" hidden>%s</button></div>'
            '<div class="mbl-fb" role="status" aria-live="polite" hidden></div>') % (TI('Check Answer', 'Kiểm tra đáp án'), TI('Try Again', 'Làm lại'))

def MCQ(n, q, opts, ans, expl, raw=False):
    """raw=True: các phương án là văn bản/HTML (không bọc công thức), ví dụ câu hỏi chọn câu lệnh tiếng Anh."""
    _qid[0] += 1
    name = 'q%d' % _qid[0]
    def _o(t):
        if t.startswith('§'): return t[1:]
        if raw: return t
        return t if (t.startswith('\\(') and t.endswith('\\)') and t.count('\\(') == 1) else '\\(%s\\)' % t
    o = ''.join('<label><input type="radio" name="%s" value="%s"><span>%s</span></label>' % (name, 'abcd'[i], _o(t)) for i, t in enumerate(opts))
    return ('<div class="mbl-item" data-type="mcq" data-answer="%s"><div class="mbl-qtext"><b>%d.</b></div>%s<div class="mbl-opts">%s</div>%s'
            '<div class="mbl-explain" hidden>%s</div></div>') % (ans, n, T(*q, auto=True), o, _actions(), T(*expl, auto=True))

def TF(n, q, ans, expl):
    _qid[0] += 1
    name = 'q%d' % _qid[0]
    o = ('<label><input type="radio" name="%s" value="true"><span>%s</span></label>'
         '<label><input type="radio" name="%s" value="false"><span>%s</span></label>') % (name, TI('True', 'Đúng'), name, TI('False', 'Sai'))
    return ('<div class="mbl-item" data-type="tf" data-answer="%s"><div class="mbl-qtext"><b>%d.</b></div>%s<div class="mbl-opts tf">%s</div>%s'
            '<div class="mbl-explain" hidden>%s</div></div>') % (ans, n, T(*q, auto=True), o, _actions(), T(*expl, auto=True))

def SHORT(n, q, key, kind, hint, expl):
    return ('<div class="mbl-item" data-type="short" data-kind="%s" data-answer="%s"><div class="mbl-qtext"><b>%d.</b></div>%s%s'
            '<p><input class="mbl-input" type="text" inputmode="text" autocomplete="off" aria-label="Answer"></p>%s'
            '<div class="mbl-explain" hidden>%s</div></div>') % (kind, key, n, T(*q, auto=True), T(*hint), _actions(), T(*expl, auto=True))

def QUIZ(groups):
    s = '<div class="mbl-quiz"><p class="mbl-scorebar"><span class="mbl-score" aria-live="polite"></span></p>'
    for grp in groups:
        g, items = grp[0], grp[1]
        part = '<p class="mbl-group">%s</p>' % TI(*g) + ''.join(items)
        lv = level_class(grp[2]) if len(grp) > 2 else ''
        s += '<div class="%s">%s</div>' % (lv, part) if lv else part
    s += ('<div class="mbl-actions"><button type="button" class="mbl-btn" data-act="finish">%s</button>'
          '<button type="button" class="mbl-btn ghost" data-act="resetall">%s</button></div><div class="mbl-result" hidden></div></div>') % (TI('Submit', 'Nộp bài'), TI('Try Again', 'Làm lại'))
    return s

def TABLE(head, rows):
    """Bảng song ngữ. head: danh sách (en, vi) hoặc None (cột chỉ có tiếng Việt thì dùng ('', vi)); rows: danh sách hàng, mỗi ô là HTML."""
    th = ''.join('<th>%s</th>' % (TI(*h) if h[0] else terms(h[1])) for h in head)
    tr = ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % c for c in r) for r in rows)
    return '<div class="mbl-tablewrap"><table class="mbl-table"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (th, tr)

def CHECKS(items):
    s = '<div><ul class="mbl-checks">'
    for en, vi in items:
        s += '<li><label><input type="checkbox"><span>%s</span></label></li>' % TI(en, vi)
    return s + '</ul><p class="mbl-selfmsg" role="status" aria-live="polite"></p></div>'

_model_cache = []
def model():
    """Đọc config/model.json (mô hình bài học duy nhất)."""
    if not _model_cache:
        _model_cache.append(json.load(open(os.path.join(ROOT, 'config', 'model.json'), encoding='utf-8')))
    return _model_cache[0]

def level_class(levels):
    """Lớp CSS ẩn/hiện mục theo mức học. Mọi mức -> không có lớp; [2,3] giữ tên cũ l23only."""
    lv = sorted(set(levels or [1, 2, 3]))
    if lv == [1, 2, 3]: return ''
    if lv == [2, 3]: return 'l23only'
    return 'lv-only-' + ''.join(str(x) for x in lv)

def PAGE(lesson_id, title, depth, sub, meta_html, body_html, toc):
    """Khung trang bài học: đọc config/page-template.html và config/model.json (mô hình chung cho mọi lớp).
    toc: danh sách (số, en, vi, levels)."""
    m = model(); pg = m['page']; up = '../' * depth
    tpl = open(os.path.join(ROOT, pg['template']), encoding='utf-8').read()
    head = [('<link rel="stylesheet" href="%s%s">' % (up, c)) for c in pg['css']]
    head_js = [('<script src="%s%s"></script>' % (up, j)) for j in pg['scriptsBeforeBody']]
    foot = [('<script src="%s%s"></script>' % (up, j)) for j in pg['scriptsAfterBody']]
    _u = lambda r: r if r.startswith('http') else up + r
    extra_foot = []
    for opt in pg.get('optional', []):                 # tài nguyên chỉ nạp khi nội dung cần (ví dụ thư viện đồ thị)
        if opt['trigger'] in body_html:
            head += [('<link rel="stylesheet" href="%s">' % _u(c)) for c in opt.get('css', [])]
            head += [('<meta name="%s" content="%s">' % (k, v)) for k, v in opt.get('meta', {}).items() if v]
            extra_foot += [('<script src="%s"></script>' % _u(j)) for j in opt.get('scripts', [])]
    head += head_js
    head.append('<script async src="%s"></script>' % pg['mathjax'])
    foot = extra_foot + foot
    btns = ''.join('<button type="button" role="radio" data-level="%d" aria-checked="%s">%s</button>' % (
        l['id'], 'true' if l['id'] == m['defaultLevel'] else 'false', l['label']) for l in m['levels'])
    bar = '<div class="mbl-levels" role="radiogroup" aria-label="%s">%s</div>' % (m['levelBarLabel'], btns)
    toc_html = ''
    for (n, en, vi, lv) in toc:
        c = level_class(lv) if not isinstance(lv, bool) else ('l23only' if lv else '')
        toc_html += '<li%s><a href="#s%d">%d. %s</a></li>' % (' class="%s"' % c if c else '', n, n, TI(en, vi))
    vals = {'title': title, 'head_links': '\n'.join(head), 'id': lesson_id, 'default_level': m['defaultLevel'],
            'h1': HT(*title_pair(lesson_id, title, sub)), 'sub': sub, 'level_bar': bar, 'toc': toc_html,
            'body': body_html, 'foot_scripts': '\n'.join(foot)}
    return re.sub(r'\{\{(\w+)\}\}', lambda mo: str(vals[mo.group(1)]), tpl)

_titles = {}
def title_pair(lid, en, _):
    return _titles[lid]
def set_title(lid, en, vi):
    _titles[lid] = (en, vi)


def EXFIG(examples, n, fig_html):
    """Chèn hình vẽ vào đề của Ví dụ n (ngay sau đề bài, trong khung xanh)."""
    tag = '<section class="mbl-ex" aria-label="Example %d">' % n
    i = examples.index(tag); j = examples.index('<div class="box blue">', i) + len('<div class="box blue">')
    k = examples.index('</div></div>', j) + len('</div>')       # hết khối T(...) của đề bài
    return examples[:k] + fig_html + examples[k:]
