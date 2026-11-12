# -*- coding: utf-8 -*-
"""MathBridge – hình vẽ TĨNH bằng LaTeX (XeLaTeX) → SVG.

    Đồ thị hàm số, dữ liệu : PGFPlots (pgfplotstable sẵn dùng cho bảng dữ liệu)
    Hình học phẳng          : tkz-euclide (+ thư viện TikZ angles, quotes, calc)
    Hình học không gian     : tools/mb_tikz3d.py (TikZ 3D, nét khuất tự tính)
    Biểu đồ Venn, trục số   : TikZ

Mọi đường TIỆM CẬN vẽ bằng NÉT ĐỨT (cả tiệm cận khai báo lẫn tiệm cận tự phát hiện bằng js/mb-graph-core.js).
Biên dịch: xelatex → PDF → pdftocairo -svg; lưu đệm theo mã băm vào img/tex/<băm>.svg (+ .tex nguồn để sửa tay)."""
import os, re, json, math, hashlib, subprocess, tempfile, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'img', 'tex')
PALETTE = ['046b4d', 'c2410c', '1d4ed8', '7c3aed', 'be185d', '0e7490']
INK, UP, DOWN, ASY = '123428', '0a8f63', 'c2410c', '475569'

PRE = r'''\documentclass[border=4pt]{standalone}
\usepackage{fontspec}
\usepackage{amsmath}
\usepackage{unicode-math}
\setmainfont{Latin Modern Roman}
\setmathfont{Latin Modern Math}
\usepackage{pgfplots}
\usepackage{pgfplotstable}
\pgfplotsset{compat=1.18}
\usepackage{tkz-euclide}
\usetikzlibrary{arrows.meta,calc,angles,quotes,patterns,3d,backgrounds}
\definecolor{ink}{HTML}{123428}
\definecolor{asy}{HTML}{475569}
\definecolor{mint}{HTML}{86e0bd}
\tikzset{asym/.style={asy, line width=0.9pt, dash pattern=on 5pt off 3.5pt},
         guide/.style={gray!70, line width=0.6pt, densely dotted},
         dot/.style={circle, inner sep=0pt, minimum size=5pt, draw=white, line width=0.5pt},
         odot/.style={circle, inner sep=0pt, minimum size=5.5pt, fill=white, line width=1pt},
         lab/.style={font=\footnotesize, inner sep=1.5pt, text=ink}}
'''


def col(h):
    h = (h or INK).lstrip('#')
    if len(h) == 3: h = ''.join(c * 2 for c in h)
    return '{rgb,255:red,%d;green,%d;blue,%d}' % (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def texsvg(body, pre=PRE):
    """Biên dịch một tikzpicture (có bộ nhớ đệm) → tên tệp SVG trong img/tex/."""
    tex = pre + '\\begin{document}\n' + body + '\n\\end{document}\n'
    h = hashlib.md5(tex.encode('utf-8')).hexdigest()[:16]
    os.makedirs(OUT, exist_ok=True)
    fn = os.path.join(OUT, h + '.svg')
    if not os.path.exists(fn):
        tmp = tempfile.mkdtemp()
        try:
            open(os.path.join(tmp, 'f.tex'), 'w', encoding='utf-8').write(tex)
            r = subprocess.run(['xelatex', '-interaction=nonstopmode', '-halt-on-error', 'f.tex'], cwd=tmp, capture_output=True, text=True)
            if r.returncode: raise RuntimeError('LaTeX lỗi:\n' + r.stdout[-3000:] + '\n' + tex[-4000:])
            subprocess.run(['pdftocairo', '-svg', 'f.pdf', 'f.svg'], cwd=tmp, check=True)
            shutil.copy(os.path.join(tmp, 'f.svg'), fn)
            open(os.path.join(OUT, h + '.tex'), 'w', encoding='utf-8').write(tex)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    return h + '.svg'


def used():
    """Tên các tệp đã dùng trong lần dựng này (để dọn tệp cũ)."""
    return set(_USED)
_USED = []


def img(fn, alt, px, cap=None):
    import html as _h
    _USED.append(fn)
    return ('<figure class="mbl-fig mbl-figtex"><img src="../../../img/tex/%s" alt="%s" loading="lazy" '
            'style="display:block;margin:0 auto;width:min(100%%,%dpx);height:auto">%s</figure>'
            % (fn, _h.escape(alt or 'Figure', quote=True), px, ('<figcaption>%s</figcaption>' % cap) if cap else ''))


# ---------- nhãn: chữ Unicode → LaTeX ----------
SUP = {'²': '^{2}', '³': '^{3}', 'ˣ': '^{x}', '⁻¹': '^{-1}'}
SUB = {'ₐ': '_{a}', '₀': '_{0}', '₁': '_{1}', '₂': '_{2}', '₃': '_{3}', 'ₙ': '_{n}'}


def tmath(s):
    """Biểu thức toán viết kiểu Unicode (y = (2x+1)/(x−3), logₐx, √(x + 1)…) → mã TeX (chế độ toán)."""
    s = str(s)
    s = s.replace('  ', ' \\quad ')
    if '\\quad' not in s: s = re.sub(r'(?<=\S) \((?=[^()]*[<>≤≥][^()]*\)$)', r' \\quad (', s)
    s = re.sub(r'√\(([^()]*)\)', r'\\sqrt{\1}', s)
    s = re.sub(r'√(\d+|[a-z])', r'\\sqrt{\1}', s)
    s = re.sub(r'(\d*[a-z][²]?)/(\d+)', lambda m: '\\frac{%s}{%s}' % (m.group(1), m.group(2)), s)
    s = re.sub(r'\((\d+)/(\d+)\)', r'\\left(\\tfrac{\1}{\2}\\right)', s)
    s = re.sub(r'\(([^()]*)\)/\(([^()]*)\)', r'\\dfrac{\1}{\2}', s)
    for a, b in list(SUP.items()) + list(SUB.items()):
        s = s.replace(a, b)
    rep = [('−', '-'), ('≤', '\\le '), ('≥', '\\ge '), ('·', '\\cdot '), ('π', '\\pi '), ('×', '\\times '), ('′', "'"),
           ('α', '\\alpha '), ('°', '^{\\circ}'), ('∞', '\\infty '), ('≠', '\\ne '), ('∖', '\\setminus '), ('∩', '\\cap '), ('∪', '\\cup ')]
    for a, b in rep: s = s.replace(a, b)
    s = re.sub(r'(?<![A-Za-z\\])(sin|cos|tan|cot|log|ln)(?![a-z])', r'\\\1', s)
    s = re.sub(r'\\(sin|cos|tan|cot|log|ln)(?=[a-zA-Z0-9])', r'\\\1 ', s)
    # chữ có dấu tiếng Việt (giảm, tăng, …) → \text{}
    s = re.sub(r'([A-Za-zÀ-ỹ]*[À-ỹ][A-Za-zÀ-ỹ]*)', r'\\text{\1}', s)
    return s


def lab(s):
    s = str(s or '').strip()
    return ('$%s$' % tmath(s)) if s else ''


def fmt(v, d=2):
    if abs(v - round(v)) < 1e-9: v = round(v)
    t = ('%.*f' % (d, v)).rstrip('0').rstrip('.') if not isinstance(v, int) else str(v)
    return '0' if t in ('-0', '') else t


def fmt_pi(x):
    for den in (1, 2, 3, 4, 6, 12):
        k = x / math.pi * den
        if abs(k - round(k)) < 1e-6:
            k = int(round(k))
            if k == 0: return '0'
            g = math.gcd(abs(k), den); k, d = k // g, den // g
            num = ('' if abs(k) == 1 else str(abs(k))) + '\\pi'
            return ('-' if k < 0 else '') + (num if d == 1 else '\\frac{%s}{%d}' % (num, d))
    return fmt(x)


def ptlab(x, y, pi=False):
    return '$(%s;\\,%s)$' % (fmt_pi(x) if pi else fmt(x), fmt(y))


def nice_step(r, n=12):
    for s in (0.1, 0.2, 0.25, 0.5, 1, 2, 5, 10, 20, 25, 50, 100, 200, 500, 1000):
        if r / s <= n: return s
    return 10 ** math.ceil(math.log10(r / n))


def ticks(lo, hi, step):
    k0, k1 = math.ceil(lo / step - 1e-9), math.floor(hi / step + 1e-9)
    return [round(k * step, 6) for k in range(k0, k1 + 1)]


def anchor_for(dx, dy):
    v = 'south' if dy > 2 else ('north' if dy < -2 else '')
    h = 'west' if dx > 2 else ('east' if dx < -2 else '')
    return (v + ' ' + h).strip() or 'south west'


def _eval(jobs):
    r = subprocess.run(['node', os.path.join(ROOT, 'tools', 'graph_eval.js')], input=json.dumps(jobs), capture_output=True, text=True)
    if r.returncode: raise RuntimeError('graph_eval.js lỗi: ' + r.stderr[-2000:])
    return json.loads(r.stdout)


def coords(piece):
    return ' '.join('(%s,%s)' % (fmt(x, 5), fmt(y, 5)) for x, y in piece)


def _sub_params(f, scope):
    for k, v in sorted(scope.items(), key=lambda kv: -len(kv[0])):
        f = re.sub(r'(?<![A-Za-z])%s(?![A-Za-z(])' % re.escape(k), '(%s)' % repr(v), f)
    return f


# ---------- ĐỒ THỊ HÀM SỐ (PGFPlots) ----------
def graph_tex(cfg, height=360):
    cfg = json.loads(json.dumps(cfg))
    fam = cfg.pop('family', None)
    params = cfg.pop('params', None) or []
    funcs = []
    if fam:            # họ đồ thị: vẽ mỗi bộ tham số một đường (thay cho thanh trượt)
        names = [p['name'] for p in params]
        for i, s in enumerate(cfg.get('functions', [])):
            if not any(re.search(r'(?<![A-Za-z])%s(?![A-Za-z(])' % n, s['f']) for n in names):
                funcs.append(s); continue
            for j, sc in enumerate(fam):
                t = dict(s); t['f'] = _sub_params(s['f'], sc)
                t['label'] = sc.get('_labels', {}).get(str(i)) or sc.get('_label') or (s.get('label', '') + '  (' + ', '.join('%s = %s' % (k, fmt(v)) for k, v in sc.items() if not k.startswith('_')) + ')')
                t['color'] = sc.get('_colors', {}).get(str(i)) or sc.get('_color') or '#' + PALETTE[(len(funcs)) % len(PALETTE)]
                funcs.append(t)
        cfg['functions'] = funcs
    elif params:       # giá trị mặc định của tham số
        sc = {p['name']: p['value'] for p in params}
        for s in cfg.get('functions', []): s['f'] = _sub_params(s['f'], sc)
    R = _eval([{'graph': cfg}])[0]
    x0, x1, y0, y1 = cfg['view']; pi = cfg.get('pi')
    W = 10.0; H = W * (y1 - y0) / (x1 - x0) if cfg.get('equal') else max(4.6, min(8.0, height / 360 * 6.4))
    o = []
    # trục và vạch chia
    if pi:
        st = math.pi / 2 if (x1 - x0) <= 4.2 * math.pi else math.pi
        xt = [k * st for k in range(math.ceil(x0 / st), math.floor(x1 / st) + 1) if abs(k) > 0]
        xtl = ['$%s$' % fmt_pi(v) for v in xt]
    else:
        stx = nice_step(x1 - x0, 9); xt = [v for v in ticks(x0, x1, stx) if abs(v) > 1e-9 and x0 < v < x1]
        xtl = ['$%s$' % fmt(v) for v in xt]
    sty = nice_step(y1 - y0, 8); yt = [v for v in ticks(y0, y1, sty) if abs(v) > 1e-9 and y0 < v < y1]
    xn, yn = cfg.get('xname', 'x'), cfg.get('yname', 'y')
    opts = ['scale only axis', 'width=%.2fcm' % W, 'height=%.2fcm' % H, 'axis lines=middle',
            'xmin=%s, xmax=%s, ymin=%s, ymax=%s' % (x0, x1, y0, y1),
            'axis line style={draw=ink!85, line width=0.7pt, -{Stealth[length=2.4mm]}}',
            'xlabel={$%s$}, ylabel={$%s$}' % (xn, yn),
            'xlabel style={at={(ticklabel* cs:1)}, anchor=north east, inner sep=2pt}',
            'ylabel style={at={(ticklabel* cs:1)}, anchor=north west, inner sep=3pt}',
            'grid=major, major grid style={draw=gray!16, line width=0.4pt}',
            'tick style={draw=ink!70}', 'ticklabel style={font=\\footnotesize, text=ink!85}',
            'xtick={%s}' % ','.join(fmt(v, 6) for v in xt), 'xticklabels={%s}' % ','.join(xtl),
            'ytick={%s}' % ','.join(fmt(v, 6) for v in yt), 'yticklabels={%s}' % ','.join('$%s$' % fmt(v) for v in yt),
            'clip mode=individual', 'every axis plot/.append style={line join=round}']
    labs = [s.get('label') for s in cfg.get('functions', []) + cfg.get('param', []) if s.get('label')]
    nleg = len(labs) + (2 if cfg.get('monotone') else 0)
    if nleg and cfg.get('legend', True) is not False:
        L = [len(re.sub(r'[^\w=+<>]', '', x)) + 4 for x in labs] + ([24, 24] if cfg.get('monotone') else [])
        ncol = -1 if sum(L) <= 52 else (2 if max(L) <= 30 else 1)
        opts.append('legend style={at={(0.5,%s)}, anchor=north, draw=none, fill=none, font=\\small, legend columns=%d, '
                    '/tikz/every even column/.append style={column sep=10pt}}' % ('-0.03' if y0 < 0 else '-0.09', ncol))
        opts.append('legend cell align=left')
    o.append('\\begin{axis}[\n  ' + ',\n  '.join(opts) + ']')
    if x0 < 0 < x1 and y0 < 0 < y1:
        o.append('\\node[lab, anchor=north east] at (axis cs:0,0) {$O$};')
    # tô khoảng đồng biến / nghịch biến (vẽ dưới đồ thị)
    leg_extra = []
    for iv in R.get('monotone', []):
        c = UP if iv['up'] else DOWN
        for p in iv['pieces']:
            o.append('\\addplot[color=%s, line width=5pt, opacity=0.40, forget plot] coordinates {%s};' % (col(c), coords(p)))
    for h in R.get('highlights', []):
        for p in h['pieces']:
            o.append('\\addplot[color=%s, line width=5pt, opacity=0.35, forget plot] coordinates {%s};' % (col(h.get('color') or DOWN), coords(p)))
    # đường dóng (không phải tiệm cận): chấm mảnh
    for g in cfg.get('guides', []):
        if g.get('type') == 'h': o.append('\\draw[guide] (axis cs:%s,%s) -- (axis cs:%s,%s);' % (x0, g['y'], x1, g['y']))
        else: o.append('\\draw[guide] (axis cs:%s,%s) -- (axis cs:%s,%s);' % (g['x'], y0, g['x'], y1))
    # TIỆM CẬN: nét đứt
    asy = []
    for a in cfg.get('asymptotes', []):
        t = a.get('type'); t = 'o' if t in ('o', 'oblique', 's', 'slant') else t
        asy.append(dict(a, type=t, m=a.get('m', 0), b=a.get('b', a.get('y', 0))))
    for a in R.get('autoAsym', []):
        dup = any(q['type'] == a['type'] and (abs(q.get('x', 0) - a.get('x', 0)) < 1e-6 if a['type'] == 'v' else (abs(q['m'] - a['m']) < 1e-6 and abs(q['b'] - a['b']) < 1e-6)) for q in asy)
        if a['type'] == 'h': dup = dup or any(q['type'] == 'h' and abs(q.get('y', q['b']) - a['b']) < 1e-6 for q in asy)
        if not dup: asy.append(dict(a, auto=True))
    show_lab = len(asy) <= 3 and not pi
    for a in asy:
        c = col(a.get('color') or ASY)
        if a['type'] == 'v':
            if not (x0 < a['x'] < x1): continue
            o.append('\\draw[asym, draw=%s] (axis cs:%s,%s) -- (axis cs:%s,%s);' % (c, fmt(a['x'], 6), y0, fmt(a['x'], 6), y1))
            xl = a.get('label') or (('x=%s' % fmt(a['x'])) if abs(a['x'] * 100 - round(a['x'] * 100)) < 1e-6 else '')
            if show_lab and xl: o.append('\\node[lab, text=asy, anchor=north west, font=\\scriptsize] at (axis cs:%s,%s) {%s};' % (fmt(a['x'], 6), y1, lab(xl)))
        else:
            m, b = a['m'], a['b']
            if a['type'] == 'h': m = 0; b = a.get('y', b)
            if m == 0 and not (y0 <= b <= y1): continue
            o.append('\\addplot[asym, draw=%s, forget plot, domain=%s:%s, samples=2] {%s*x+(%s)};' % (c, x0, x1, fmt(m, 6), fmt(b, 6)))
            if show_lab:
                xe = x1
                if m:
                    ye = m * x1 + b
                    if ye > y1: xe = (y1 - b) / m
                    if ye < y0: xe = (y0 - b) / m
                ye = m * xe + b
                t = tmath(a['label']) if a.get('label') else 'y=%s' % fmt(b) if m == 0 else 'y=%s%s' % ('' if m == 1 else ('-' if m == -1 else fmt(m)), 'x' + ('' if b == 0 else ('+%s' % fmt(b) if b > 0 else fmt(b))))
                o.append('\\node[lab, text=asy, anchor=%s, font=\\scriptsize] at (axis cs:%s,%s) {$%s$};' % ('south east', fmt(xe, 6), fmt(ye, 6), t))
    # đồ thị
    for i, (s, F) in enumerate(zip(cfg.get('functions', []), R['functions'])):
        c = col(s.get('color') or '#' + PALETTE[i % len(PALETTE)])
        w = 0.5 * float(s.get('width', 2.6))
        st = 'color=%s, line width=%.2fpt' % (c, w) + (', dash pattern=on 4pt off 3pt' if s.get('dash') else '')
        first = True
        for p in F['pieces']:
            leg = first and s.get('label') and cfg.get('legend', True) is not False
            o.append('\\addplot[%s%s] coordinates {%s};' % (st, '' if leg else ', forget plot', coords(p)))
            if leg: o.append('\\addlegendentry{%s}' % lab(s['label']))
            first = False
        for e in F.get('ends', []):
            if not (x0 < e['x'] < x1 and y0 < e['y'] < y1): continue
            o.append('\\node[%s, %s] at (axis cs:%s,%s) {};' % ('odot, draw=' + c if e['open'] else 'dot, fill=' + c, '', fmt(e['x'], 6), fmt(e['y'], 6)))
    # đường cong tham số (elip, hypebol, parabol, đường tròn…): {'x': '3*cos(t)', 'y': '2*sin(t)', 'range': [0, 360]} (góc tính bằng độ)
    for j, c in enumerate(cfg.get('param', [])):
        cc = col(c.get('color') or '#' + PALETTE[(len(cfg.get('functions', [])) + j) % len(PALETTE)])
        lo_, hi_ = c.get('range', [0, 360]); leg = c.get('label') and cfg.get('legend', True) is not False
        o.append('\\addplot[color=%s, line width=1.3pt, variable=\\t, domain=%s:%s, samples=%d, smooth%s] ({%s},{%s});' % (cc, lo_, hi_, c.get('samples', 160), '' if leg else ', forget plot', c['x'].replace('t', '\\t'), c['y'].replace('t', '\\t')))
        if leg: o.append('\\addlegendentry{%s}' % lab(c['label']))
    if cfg.get('monotone') and cfg.get('legend', True) is not False:
        o.append('\\addlegendimage{color=%s, line width=5pt, opacity=0.4}\\addlegendentry{increasing (đồng biến)}' % col(UP))
        o.append('\\addlegendimage{color=%s, line width=5pt, opacity=0.4}\\addlegendentry{decreasing (nghịch biến)}' % col(DOWN))
    # tiếp tuyến
    tg = R.get('tangent') or []
    for j, t in enumerate(tg):
        k = round(t['k'], 6)
        o.append('\\addplot[color=%s, line width=1.1pt, forget plot, domain=%s:%s, samples=2] {%s*(x-(%s))+(%s)};' % (col('c2410c'), x0, x1, k, t['x'], t['y']))
        o.append('\\node[dot, fill=%s, minimum size=6pt] at (axis cs:%s,%s) {};' % (col('c2410c'), t['x'], t['y']))
        if len(tg) == 1: o.append('\\node[lab, anchor=north west] at (axis cs:%s,%s) {$M$};' % (t['x'], t['y']))
    # điểm đặc biệt tự tính
    kinds = {}
    for m in R.get('marks', []): kinds.setdefault(m['kind'], []).append(m)
    for kind, ms in kinds.items():
        many = len(ms) > 6
        for m in ms:
            c = {'max': DOWN, 'min': '1d4ed8', 'infl': '7c3aed', 'int': INK}.get(kind)
            if c is None: c = (cfg['functions'][m['f']].get('color') or '#' + PALETTE[m['f'] % len(PALETTE)]) if 'f' in m else INK
            open_ = kind in ('infl', 'hole')
            o.append('\\node[%s=%s] at (axis cs:%s,%s) {};' % ('odot, draw' if open_ else 'dot, fill', col(c), fmt(m['x'], 6), fmt(m['y'], 6)))
            if not many:
                t = ptlab(m['x'], m['y'], pi) + (' $\\times%d$' % m['mult'] if m.get('mult', 1) > 1 else '')
                anc = {'max': 'south', 'min': 'north', 'root': 'north west', 'yint': 'south east' if m['y'] > 0 else 'north east'}.get(kind, 'south west')
                o.append('\\node[lab, anchor=%s, fill=white, fill opacity=0.8, text opacity=1] at (axis cs:%s,%s) {%s};' % (anc, fmt(m['x'], 6), fmt(m['y'], 6), t))
    # lỗ hổng và điểm khai báo
    for h in cfg.get('holes', []):
        o.append('\\node[odot, draw=%s] at (axis cs:%s,%s) {};' % (col(PALETTE[0]), h[0], h[1]))
        if len(h) > 2 and h[2]: o.append('\\node[lab, anchor=south west] at (axis cs:%s,%s) {%s};' % (h[0], h[1], lab(h[2])))
    for p in cfg.get('points', []):
        c = col(p.get('color') or INK)
        o.append('\\node[%s] at (axis cs:%s,%s) {};' % (('odot, draw=' + c) if p.get('open') else ('dot, fill=' + c), fmt(p['x'], 6), fmt(p['y'], 6)))
        if p.get('label'):
            dx, dy = (p.get('off') or [7, 7])
            o.append('\\node[lab, anchor=%s, fill=white, fill opacity=0.8, text opacity=1] at (axis cs:%s,%s) {%s};' % (anchor_for(dx, dy), fmt(p['x'], 6), fmt(p['y'], 6), lab(p['label'])))
    for t in cfg.get('texts', []):
        o.append('\\node[lab] at (axis cs:%s,%s) {%s};' % (t['x'], t['y'], lab(t['text'])))
    o.append('\\end{axis}')
    return '\\begin{tikzpicture}\n' + '\n'.join(o) + '\n\\end{tikzpicture}'


def graph_svg(cfg, height=360):
    fn = texsvg(graph_tex(cfg, height))
    side = os.path.join(OUT, fn[:-4] + '.json')     # cấu hình gốc, để tests/test-lesson-graphs.js kiểm tra toán học
    json.dump(dict(cfg, kind='graph'), open(side, 'w', encoding='utf-8'), ensure_ascii=False)
    return fn


def fn_svg(f, xr, yr, vlines=(), hlines=(), lines=(), label_pts=(), w=340, h=250):
    """Thay svg_graph cũ: hàm Python f, các tiệm cận đứng/ngang/xiên vẽ NÉT ĐỨT bằng PGFPlots."""
    (x0, x1), (y0, y1) = xr, yr
    N = 1200; segs, cur = [], []
    H = y1 - y0
    for i in range(N + 1):
        x = x0 + (x1 - x0) * i / N
        try: y = f(x)
        except (ZeroDivisionError, ValueError): y = None
        if y is None or not math.isfinite(y) or y < y0 - 0.6 * H or y > y1 + 0.6 * H:
            if len(cur) > 1: segs.append(cur)
            cur = []
        else: cur.append((x, y))
    if len(cur) > 1: segs.append(cur)
    stx = nice_step(x1 - x0, 9); sty = nice_step(y1 - y0, 8)
    xt = [v for v in ticks(x0, x1, stx) if abs(v) > 1e-9 and x0 < v < x1]
    yt = [v for v in ticks(y0, y1, sty) if abs(v) > 1e-9 and y0 < v < y1]
    W = 9.0; Hc = W * h / w
    o = ['\\begin{tikzpicture}', '\\begin{axis}[scale only axis, width=%.2fcm, height=%.2fcm, axis lines=middle, xmin=%s, xmax=%s, ymin=%s, ymax=%s,' % (W, Hc, x0, x1, y0, y1),
         '  axis line style={draw=ink!85, line width=0.7pt, -{Stealth[length=2.4mm]}}, xlabel={$x$}, ylabel={$y$},',
         '  xlabel style={at={(ticklabel* cs:1)}, anchor=north east}, ylabel style={at={(ticklabel* cs:1)}, anchor=north west},',
         '  grid=major, major grid style={draw=gray!16}, ticklabel style={font=\\footnotesize, text=ink!85}, tick style={draw=ink!70},',
         '  xtick={%s}, ytick={%s}, clip mode=individual]' % (','.join(fmt(v, 6) for v in xt), ','.join(fmt(v, 6) for v in yt))]
    if x0 < 0 < x1 and y0 < 0 < y1: o.append('\\node[lab, anchor=north east] at (axis cs:0,0) {$O$};')
    for a in vlines:
        o.append('\\draw[asym] (axis cs:%s,%s) -- (axis cs:%s,%s);' % (a, y0, a, y1))
        o.append('\\node[lab, text=asy, anchor=north west, font=\\scriptsize] at (axis cs:%s,%s) {$x=%s$};' % (a, y1, fmt(a)))
    for b in hlines:
        o.append('\\draw[asym] (axis cs:%s,%s) -- (axis cs:%s,%s);' % (x0, b, x1, b))
        o.append('\\node[lab, text=asy, anchor=south east, font=\\scriptsize] at (axis cs:%s,%s) {$y=%s$};' % (x1, b, fmt(b)))
    for (m, c, t) in lines:
        o.append('\\addplot[asym, domain=%s:%s, samples=2] {%s*x+(%s)};' % (x0, x1, m, c))
        xe = x1; ye = m * x1 + c
        if ye > y1: xe = (y1 - c) / m
        if ye < y0: xe = (y0 - c) / m
        o.append('\\node[lab, text=asy, anchor=south east, font=\\scriptsize] at (axis cs:%s,%s) {%s};' % (fmt(xe, 5), fmt(m * xe + c, 5), lab(t)))
    for sgm in segs:
        o.append('\\addplot[color=%s, line width=1.3pt] coordinates {%s};' % (col(PALETTE[0]), coords(sgm)))
    for (x, y, t) in label_pts:
        o.append('\\node[dot, fill=%s] at (axis cs:%s,%s) {};' % (col(PALETTE[0]), x, y))
        if t: o.append('\\node[lab, anchor=south west] at (axis cs:%s,%s) {%s};' % (x, y, lab(t)))
    o += ['\\end{axis}', '\\end{tikzpicture}']
    return texsvg('\n'.join(o))


# ---------- HÌNH HỌC PHẲNG (tkz-euclide) ----------
def _clip_line(P, d, view):
    """Đoạn của đường thẳng qua P, chỉ phương d, nằm trong khung view."""
    x0, x1, y0, y1 = view; ts = []
    for k, (lo, hi) in enumerate(((x0, x1), (y0, y1))):
        if abs(d[k]) < 1e-12:
            if not (lo <= P[k] <= hi): return None
            continue
        ts.append(sorted(((lo - P[k]) / d[k], (hi - P[k]) / d[k])))
    a = max(t[0] for t in ts) if ts else -1e9; b = min(t[1] for t in ts) if ts else 1e9
    if a >= b: return None
    return (P[0] + a * d[0], P[1] + a * d[1]), (P[0] + b * d[0], P[1] + b * d[1])


def _foot(P, A, B):
    dx, dy = B[0] - A[0], B[1] - A[1]; t = ((P[0] - A[0]) * dx + (P[1] - A[1]) * dy) / (dx * dx + dy * dy)
    return (A[0] + t * dx, A[1] + t * dy)


def geo_tex(cfg, height=360):
    view = cfg['view']; x0, x1, y0, y1 = view
    W = 9.0; ux = W / (x1 - x0)
    uy = ux if cfg.get('equal', True) else max(4.6, min(8, height / 360 * 6.2)) / (y1 - y0)
    if (y1 - y0) * uy > 10: ux = uy = 10 / (y1 - y0) if cfg.get('equal', True) else ux
    P, names, lines, circles = {}, {}, {}, {}
    pts_draw, defs, draw, labels, marks = [], [], [], [], []
    k = [0]; rmk = set()

    def pid(xy):
        k[0] += 1; n = 'tmp%d' % k[0]; P[n] = xy; return n

    def get(r):
        if isinstance(r, (list, tuple)): return pid(tuple(r))
        return r

    def lsty(st, base='ink'):
        st = st or {}; c = col(st.get('strokeColor')) if st.get('strokeColor') else base
        w = float(st.get('strokeWidth', 2)) * 0.45
        s = 'draw=%s, line width=%.2fpt' % (c, w)
        if st.get('dash'): s += ', dash pattern=on 4pt off 3pt'
        if st.get('lastArrow'): s += ', -{Stealth[length=%.1fmm, width=%.1fmm]}' % (2.2 + w, 1.6 + w * 0.8)
        return s

    for st in cfg['steps']:
        t = st['type']
        if t in ('point', 'glider'):
            xy = tuple(st['at'])
            if t == 'glider' and st.get('on') in circles:
                c, r = circles[st['on']]; d = math.hypot(xy[0] - c[0], xy[1] - c[1]) or 1
                xy = (c[0] + r * (xy[0] - c[0]) / d, c[1] + r * (xy[1] - c[1]) / d)
            P[st['id']] = xy
            nm = st.get('name', st['id'])
            sz = (st.get('style') or {}).get('size', 3)
            if sz > 1: pts_draw.append((st['id'], '046b4d' if t == 'point' else 'c2410c'))
            if nm: names[st['id']] = (nm, st.get('off'))
        elif t == 'segment':
            a, b = [get(r) for r in st['through']]
            if st.get('id'): lines[st['id']] = (P[a], P[b])
            draw.append('\\tkzDrawSegment[%s](%s,%s)' % (lsty(st.get('style')), a, b))
        elif t == 'line':
            a, b = st['through']; A, B = P[a], P[b]
            lines[st.get('id', a + b)] = (A, B)
            if (st.get('style') or {}).get('visible', True) is False: continue
            e = _clip_line(A, (B[0] - A[0], B[1] - A[1]), view)
            if e: draw.append('\\tkzDrawSegment[%s](%s,%s)' % (lsty(st.get('style')), pid(e[0]), pid(e[1])))
        elif t == 'lineeq':
            a, b, c = st['a'], st['b'], st['c']
            Q = (-a * c / (a * a + b * b), -b * c / (a * a + b * b)); e = _clip_line(Q, (b, -a), view)
            if e: draw.append('\\tkzDrawSegment[%s](%s,%s)' % (lsty(dict({'strokeColor': '#046b4d'}, **(st.get('style') or {}))), pid(e[0]), pid(e[1])))
        elif t == 'polygon':
            ids = [get(r) for r in st['through']]; sty = st.get('style') or {}
            op = sty.get('fillOpacity', 0.28)
            draw.insert(0, '\\tkzFillPolygon[fill=%s, fill opacity=%s](%s)' % (col(sty.get('fillColor') or '86e0bd'), op, ','.join(ids)))
            if (sty.get('borders') or {}).get('visible', True) is not False:
                draw.append('\\tkzDrawPolygon[draw=%s, line width=0.9pt](%s)' % (col('046b4d'), ','.join(ids)))
        elif t == 'circle':
            O = P[st['center']]
            r = st['radius'] if 'radius' in st else math.hypot(P[st['through']][0] - O[0], P[st['through']][1] - O[1])
            circles[st.get('id', 'c')] = (O, r)
            sty = st.get('style') or {}
            th = pid((O[0] + r, O[1]))
            draw.append('\\tkzDrawCircle[draw=%s, line width=0.9pt%s](%s,%s)' % (col('046b4d'), ', fill=mint, fill opacity=%s' % sty['fillOpacity'] if sty.get('fillOpacity') else '', st['center'], th))
        elif t in ('perpendicular', 'altitude'):
            A, B = lines[st['to']] if isinstance(st['to'], str) else (P[st['to'][0]], P[st['to'][1]])
            Pp = P[st['from']]; H = _foot(Pp, A, B); hn = st.get('foot', 'H'); P[hn] = H
            if t == 'perpendicular':
                e = _clip_line(Pp, (H[0] - Pp[0], H[1] - Pp[1]), view)
                if e: draw.append('\\tkzDrawSegment[%s](%s,%s)' % (lsty({'strokeColor': '#c2410c'}), pid(e[0]), pid(e[1])))
            else:
                draw.append('\\tkzDrawSegment[%s](%s,%s)' % (lsty(dict({'strokeColor': '#c2410c', 'dash': 2}, **(st.get('style') or {}))), st['from'], hn))
            ref = pid(A if math.hypot(A[0] - H[0], A[1] - H[1]) > 1e-6 else B)
            marks.append('\\tkzMarkRightAngle[size=%.2f, draw=%s, line width=0.7pt](%s,%s,%s)' % (0.3 / ux, col('7c2d12'), ref, hn, st['from'])); rmk.add(hn)
            pts_draw.append((hn, 'c2410c'))
            if st.get('footName'): names[hn] = (st['footName'], [8, -12])
        elif t == 'tangent':
            O, T = P[st['center']], P[st['at']]
            d = (-(T[1] - O[1]), T[0] - O[0]); e = _clip_line(T, d, view)
            if st.get('showRadius'): draw.append('\\tkzDrawSegment[%s](%s,%s)' % (lsty({'dash': 2, 'strokeColor': '#475569'}), st['center'], st['at']))
            if e: draw.append('\\tkzDrawSegment[%s](%s,%s)' % (lsty({'strokeColor': '#c2410c', 'strokeWidth': 2.4}), pid(e[0]), pid(e[1])))
            marks.append('\\tkzMarkRightAngle[size=%.2f, draw=%s, line width=0.7pt](%s,%s,%s)' % (0.3 / ux, col('7c2d12'), st['center'], st['at'], pid(e[1] if e else T))); rmk.add(st['at'])
        elif t == 'arc':
            c, a, b = st['points']
            draw.append('\\tkzDrawArc[draw=%s, line width=1.6pt](%s,%s)(%s)' % (col('c2410c'), c, a, b))
        elif t == 'angle':
            a, v, b = st['points']; A, V, B = P[a], P[v], P[b]
            ang = (math.degrees(math.atan2(B[1] - V[1], B[0] - V[0]) - math.atan2(A[1] - V[1], A[0] - V[0]))) % 360
            if ang > 180: a, b, ang = b, a, 360 - ang
            r = st.get('radius', 0.8)
            if abs(ang - 90) < 1e-6:
                if v in rmk: continue
                marks.append('\\tkzMarkRightAngle[size=%.2f, draw=%s, line width=0.7pt, fill=%s, fill opacity=0.3](%s,%s,%s)' % (0.3 / ux, col('b45309'), col('f59e0b'), a, v, b))
            else:
                marks.append('\\tkzFillAngle[size=%s, fill=%s, fill opacity=0.3](%s,%s,%s)' % (fmt(r, 4), col('f59e0b'), a, v, b))
                marks.append('\\tkzMarkAngle[size=%s, draw=%s, line width=0.7pt, mark=none](%s,%s,%s)' % (fmt(r, 4), col('b45309'), a, v, b))
                if st.get('label', True) is not False:      # 'label': chữ thay cho số đo (ví dụ '\\alpha'); False = không ghi
                    marks.append('\\tkzLabelAngle[pos=%s, text=%s, font=\\footnotesize](%s,%s,%s){$%s$}' % (fmt(r + 0.42 / ux * 1.0, 3), col('7c2d12'), a, v, b, st['label'] if isinstance(st.get('label'), str) else fmt(ang, 1) + '^{\\circ}'))
        elif t == 'text':
            labels.append('\\node[lab, font=\\normalsize] at (%s,%s) {%s};' % (fmt(st['at'][0], 5), fmt(st['at'][1], 5), lab(st['text'])))
        elif t == 'curve':
            R = _eval([{'curve': {'f': st['f'], 'view': view}}])[0]
            c = col((st.get('style') or {}).get('strokeColor') or '046b4d')
            for pc in R['pieces']:
                draw.append('\\draw[draw=%s, line width=1.3pt, line join=round] plot coordinates {%s};' % (c, coords(pc)))
        else:
            raise ValueError('Bước dựng hình chưa hỗ trợ: ' + t)
    # nhãn điểm: hướng ra xa trọng tâm các điểm có tên
    named = [P[i] for i in names] or [((x0 + x1) / 2, (y0 + y1) / 2)]
    cx = sum(p[0] for p in named) / len(named); cy = sum(p[1] for p in named) / len(named)
    for i, (nm, off) in names.items():
        X, Y = P[i]
        if off: dx, dy = off
        else:
            dx, dy = X - cx, Y - cy
            if abs(dx) < 1e-9 and abs(dy) < 1e-9: dx, dy = -1, -1
            n = math.hypot(dx, dy); dx, dy = dx / n * 9, dy / n * 9
            if cfg.get('axes') and abs(Y) < 1e-9: dy = -9
        if cfg.get('shiftLabels') and off:          # Toán 9: nhãn đặt lệch hẳn theo vectơ off (pt), tâm nhãn, không đè lên đường
            labels.append('\\node[lab, font=\\normalsize, anchor=center, xshift=%spt, yshift=%spt] at (%s,%s) {%s};' % (fmt(dx, 2), fmt(dy, 2), fmt(X, 5), fmt(Y, 5), lab(nm)))
            continue
        labels.append('\\node[lab, font=\\normalsize, anchor=%s] at (%s,%s) {%s};' % (anchor_for(dx * 3, dy * 3), fmt(X, 5), fmt(Y, 5), lab(nm)))
    o = ['\\begin{tikzpicture}[x=%.4fcm, y=%.4fcm]' % (ux, uy)]
    if cfg.get('axes'):
        stx = nice_step(x1 - x0, 8); sty = nice_step(y1 - y0, 8)
        if stx < 1 and x1 - x0 < 4: stx = 1
        if sty < 1 and y1 - y0 < 4: sty = 1
        onax = [P[i] for i in names]
        o.append('\\draw[gray!16, line width=0.4pt] %s;' % ' '.join('(%s,%s) -- (%s,%s)' % (v, y0, v, y1) for v in ticks(x0, x1, stx)) + '')
        o.append('\\draw[gray!16, line width=0.4pt] %s;' % ' '.join('(%s,%s) -- (%s,%s)' % (x0, v, x1, v) for v in ticks(y0, y1, sty)))
        o.append('\\draw[ink!85, line width=0.7pt, -{Stealth[length=2.4mm]}] (%s,0) -- (%s,0) node[anchor=north east, lab, font=\\normalsize] {$x$};' % (x0, x1))
        o.append('\\draw[ink!85, line width=0.7pt, -{Stealth[length=2.4mm]}] (0,%s) -- (0,%s) node[anchor=north west, lab, font=\\normalsize] {$y$};' % (y0, y1))
        tk = 0.08 / ux
        for v in ticks(x0, x1, stx):
            if abs(v) > 1e-9 and x0 < v < x1 - 0.3 * stx and not any(abs(q[0] - v) < 1e-6 and abs(q[1]) < 0.15 * sty for q in onax + [P[n] for n, _ in pts_draw]): o.append('\\draw[ink!70] (%s,%s) -- (%s,%s) node[below, lab, font=\\footnotesize] {$%s$};' % (v, tk, v, -tk, fmt(v)))
        for v in ticks(y0, y1, sty):
            if abs(v) > 1e-9 and y0 < v < y1 - 0.3 * sty and not any(abs(q[1] - v) < 1e-6 and abs(q[0]) < 0.15 * stx for q in onax): o.append('\\draw[ink!70] (%s,%s) -- (%s,%s) node[left, lab, font=\\footnotesize] {$%s$};' % (tk, v, -tk, v, fmt(v)))
        if 'O' not in [n for n, _ in names.values()]: o.append('\\node[lab, anchor=north east] at (0,0) {$O$};')
    o += ['\\tkzDefPoint(%s,%s){%s}' % (fmt(xy[0], 6), fmt(xy[1], 6), n) for n, xy in P.items()]
    o.append('\\begin{scope}')
    o.append('\\clip (%s,%s) rectangle (%s,%s);' % (x0, y0, x1, y1))
    o += draw
    o.append('\\end{scope}')
    o += marks
    for n, c in pts_draw:
        o.append('\\node[dot, fill=%s] at (%s) {};' % (col(c), n))
    o += labels
    o.append('\\end{tikzpicture}')
    return '\n'.join(o)


def geo_svg(cfg, height=360):
    return texsvg(geo_tex(cfg, height))


# ---------- Biểu đồ Venn hai tập (TikZ) ----------
def venn_tex(a_only, both, b_only, outside=None, la='A', lb='B', shade=None, title=None):
    """shade: None | 'inter' | 'union' | 'diff' | 'sym' – phần tô màu."""
    o = ['\\begin{tikzpicture}[x=1cm, y=1cm]', '\\def\\A{(-0.85,0) circle (1.45)}', '\\def\\B{(0.85,0) circle (1.45)}']
    if shade == 'inter': o.append('\\begin{scope}\\clip \\A; \\fill[mint] \\B;\\end{scope}')
    elif shade == 'union': o.append('\\fill[mint] \\A; \\fill[mint] \\B;')
    elif shade == 'diff': o.append('\\begin{scope}\\clip (-3,-2) rectangle (3,2); \\fill[mint] \\A; \\fill[white] \\B;\\end{scope}')
    else: o.append('\\fill[mint!45] \\A; \\fill[mint!70, fill opacity=0.6] \\B;')
    o += ['\\draw[ink, line width=0.8pt, rounded corners=6pt] (-3.1,-1.85) rectangle (3.1,1.95);',
          '\\draw[draw=%s, line width=1.1pt] \\A; \\draw[draw=%s, line width=1.1pt] \\B;' % (col('046b4d'), col('046b4d')),
          '\\node[font=\\large] at (-2.15,1.45) {$%s$};' % la, '\\node[font=\\large] at (2.15,1.45) {$%s$};' % lb]
    def v(t):
        if isinstance(t, str) and re.fullmatch(r'[A-Za-zÀ-ỹ ]{2,}', t): return t
        return lab(t) if isinstance(t, str) else '$%s$' % t
    for x, t in ((-1.5, a_only), (0, both), (1.5, b_only)):
        if t is not None and t != '': o.append('\\node[font=%s, text=ink] at (%s,0) {%s};' % ('\\Large\\bfseries' if str(t).isdigit() or t == '?' else '\\normalsize', x, v(t)))
    if outside is not None: o.append('\\node[font=%s, text=ink, anchor=south east] at (3.0,-1.8) {%s};' % ('\\Large\\bfseries' if str(outside).isdigit() or outside == '?' else '\\normalsize', v(outside)))
    if title: o.append('\\node[font=\\normalsize, text=ink] at (0,-2.3) {%s};' % title)
    o.append('\\end{tikzpicture}')
    return '\n'.join(o)


def venn_svg(*a, **k):
    return texsvg(venn_tex(*a, **k))


def raw_svg(tikz_body):
    """Một tikzpicture viết tay (trục số, sơ đồ…)."""
    return texsvg(tikz_body)


def venn_ops_svg():
    """Ba biểu đồ Venn: A ∩ B, A ∪ B, A \\ B (phần tô màu)."""
    o = ['\\begin{tikzpicture}[x=1cm, y=1cm]']
    for k, (sh, t) in enumerate((('inter', 'A\\cap B'), ('union', 'A\\cup B'), ('diff', 'A\\setminus B'))):
        X = k * 4.2
        A = '(%s,0) circle (1.05)' % (X - 0.55); B = '(%s,0) circle (1.05)' % (X + 0.55)
        if sh == 'inter': o.append('\\begin{scope}\\clip %s; \\fill[mint!80] %s;\\end{scope}' % (A, B))
        elif sh == 'union': o.append('\\fill[mint!80] %s; \\fill[mint!80] %s;' % (A, B))
        else: o.append('\\begin{scope}\\fill[mint!80] %s; \\fill[white] %s;\\end{scope}' % (A, B))
        o.append('\\draw[draw=%s, line width=1.1pt] %s %s;' % (col('046b4d'), A, B))
        o.append('\\node at (%s,0) {$A$}; \\node at (%s,0) {$B$};' % (X - 1.05, X + 1.05))
        o.append('\\node[text=ink] at (%s,-1.5) {$%s$};' % (X, t))
    o.append('\\end{tikzpicture}')
    return texsvg('\n'.join(o))


def numberline_svg(a, b, a_in=True, b_in=False, lo=None, hi=None, label=None):
    """Trục số biểu diễn khoảng (a; b): chấm đặc = lấy đầu mút, chấm rỗng = không lấy (TikZ)."""
    lo = math.floor(a) - 1 if lo is None else lo; hi = math.ceil(b) + 1 if hi is None else hi
    o = ['\\begin{tikzpicture}[x=1.15cm, y=1cm]',
         '\\draw[ink, line width=0.8pt, -{Stealth[length=2.6mm]}] (%s,0) -- (%s,0) node[right] {$x$};' % (lo - 0.4, hi + 0.5),
         '\\draw[%s, line width=6pt, opacity=0.75] (%s,0) -- (%s,0);' % ('mint', a, b)]
    for v in range(lo, hi + 1):
        o.append('\\draw[ink, line width=0.8pt] (%s,0.12) -- (%s,-0.12) node[below=1pt] {$%s$};' % (v, v, v))
    for v, inc in ((a, a_in), (b, b_in)):
        o.append('\\node[circle, inner sep=0pt, minimum size=8pt, draw=%s, line width=1.2pt, fill=%s] at (%s,0) {};' % (col('046b4d'), col('046b4d') if inc else 'white', v))
    if label: o.append('\\node[text=ink, font=\\large] at (%s,-1.05) {$%s$};' % ((a + b) / 2, label))
    o.append('\\end{tikzpicture}')
    return texsvg('\n'.join(o))


def svg_img(fn, alt, px=480):
    import html as _h
    _USED.append(fn)
    return '<img src="../../../img/tex/%s" alt="%s" role="img" loading="lazy" style="display:block;margin:0 auto;width:min(100%%,%dpx);height:auto">' % (fn, _h.escape(alt, quote=True), px)
