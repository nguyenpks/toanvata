# -*- coding: utf-8 -*-
"""Biểu đồ thống kê TĨNH cho Toán 9 – Chương VII (KNTT): biểu đồ cột, biểu đồ đoạn thẳng, biểu đồ hình quạt tròn.
Vẽ bằng PGFPlots/TikZ (tools/mb_pgf.texsvg) → SVG trong img/tex/. Mỗi biểu đồ có HAI bản nhãn (tiếng Anh, tiếng Việt):
Mức 1 thấy bản tiếng Việt, Mức 2 và Mức 3 thấy bản tiếng Anh (bọc trong <span class="txi">).
Số thập phân trên nhãn: tiếng Anh dùng dấu chấm, tiếng Việt dùng dấu phẩy."""
import math, html as _h
from mb_pgf import texsvg, col, _USED
from mb_lib import TI

BAR = '1d7a5c'
LINE = 'c2410c'
PIE = ['1d7a5c', 'e08a1e', '3b6fc4', 'b8456b', '7a5ab8', '2a9d8f', 'c9a227', '6b7280']


def _n(x, vi):
    if isinstance(x, str): return x
    if abs(x - round(x)) < 1e-9: s = str(int(round(x)))
    else: s = ('%.2f' % x).rstrip('0').rstrip('.')
    return s.replace('.', '{,}') if vi else s


def _t(s):
    """Chuỗi nhãn → TeX (giữ nguyên chữ có dấu; thoát ký tự đặc biệt)."""
    return str(s).replace('%', '\\%').replace('&', '\\&').replace('#', '\\#')


def _ax(o, xs, ymax, step, xlab, ylab, title, w, h):
    o.append('\\begin{axis}[width=%scm, height=%scm, ymin=0, ymax=%s, ytick distance=%s, ymajorgrids, grid style={gray!25},'
             ' axis lines*=left, axis line style={ink, line width=0.7pt}, tick style={ink}, tick label style={font=\\small, text=ink}, xticklabel style={text height=1.7ex, text depth=0.5ex},'
             ' xlabel={%s}, ylabel={%s}, label style={font=\\small, text=ink}, title={%s}, title style={font=\\bfseries\\small, text=ink},'
             ' symbolic x coords={%s}, xtick=data, enlarge x limits=%s, clip=false, nodes near coords style={font=\\footnotesize, text=ink}'
             % (w, h, ymax, step, _t(xlab), _t(ylab), _t(title), ','.join(xs), 0.12 if len(xs) > 3 else 0.3))


def _ymax(vals, step=None):
    m = max(vals)
    if step is None:
        for s in (1, 2, 5, 10, 20, 25, 50, 100, 200, 500):
            if m / s <= 8: step = s; break
    return step * (math.floor(m / step) + 1), step


def bar_svg(cats, vals, xlab, ylab, title, vi=False, pct=False, w=10, h=6.4, step=None, labels=True):
    xs = ['c%d' % i for i in range(len(cats))]
    ymax, step = _ymax(vals, step)
    o = ['\\begin{tikzpicture}']
    _ax(o, xs, ymax, step, xlab, ylab, title, w, h)
    o[-1] += ', xticklabels={%s}, ' % ','.join('{%s}' % _t(_n(c, vi)) for c in cats)
    if pct: o[-1] += 'yticklabel={\\pgfmathprintnumber{\\tick}\\%}, '
    o[-1] += ']'
    coords = ' '.join('(%s,%s)' % (x, v) for x, v in zip(xs, vals))
    if labels:
        o.append('\\addplot[ybar, bar width=%scm, fill=%s, draw=%s, nodes near coords={%s}] coordinates {%s};'
                 % (min(0.9, 6.0 / len(cats)), col(BAR), col(BAR), '', coords))
        # nhãn số trên đỉnh cột: tự ghi để dùng đúng dấu thập phân
        o[-1] = o[-1].replace('nodes near coords={}', '')
        for x, v in zip(xs, vals):
            o.append('\\node[font=\\footnotesize, text=ink, above] at (axis cs:%s,%s) {%s%s};' % (x, v, _n(v, vi), '\\%' if pct else ''))
    else:
        o.append('\\addplot[ybar, bar width=%scm, fill=%s, draw=%s] coordinates {%s};' % (min(0.9, 6.0 / len(cats)), col(BAR), col(BAR), coords))
    o.append('\\end{axis}\\end{tikzpicture}')
    return texsvg('\n'.join(o))


def line_svg(cats, vals, xlab, ylab, title, vi=False, pct=False, w=10, h=6.4, step=None):
    xs = ['c%d' % i for i in range(len(cats))]
    ymax, step = _ymax(vals, step)
    o = ['\\begin{tikzpicture}']
    _ax(o, xs, ymax, step, xlab, ylab, title, w, h)
    o[-1] += ', xticklabels={%s}, ' % ','.join('{%s}' % _t(_n(c, vi)) for c in cats)
    if pct: o[-1] += 'yticklabel={\\pgfmathprintnumber{\\tick}\\%}, '
    o[-1] += ']'
    o.append('\\addplot[color=%s, line width=1.3pt, mark=*, mark options={fill=%s, draw=white, scale=1.15}] coordinates {%s};'
             % (col(LINE), col(LINE), ' '.join('(%s,%s)' % (x, v) for x, v in zip(xs, vals))))
    for i, (x, v) in enumerate(zip(xs, vals)):
        L = vals[i - 1] if i > 0 else None; R = vals[i + 1] if i + 1 < len(vals) else None
        nb = [u for u in (L, R) if u is not None]
        if all(v >= u for u in nb): pos = 'above=2pt'                      # đỉnh: ghi phía trên
        elif all(v <= u for u in nb): pos = 'below=3pt' if v > 0.15 * ymax else ('above left=1pt' if L is None else 'above right=1pt' if R is None else 'above=3pt')   # đáy: ghi phía dưới (sát trục thì ghi bên phải)
        elif (L is not None and L < v) or (R is not None and R > v): pos = 'above left=1pt'   # đoạn đi lên
        else: pos = 'above right=1pt'                                      # đoạn đi xuống
        o.append('\\node[font=\\footnotesize, text=ink, %s] at (axis cs:%s,%s) {%s%s};' % (pos, x, v, _n(v, vi), '\\%' if pct else ''))
    o.append('\\end{axis}\\end{tikzpicture}')
    return texsvg('\n'.join(o))


def pie_svg(cats, pcts, title, vi=False, R=2.1):
    """Biểu đồ hình quạt tròn: pcts là phần trăm (tổng 100). Ghi % trong/ngoài hình quạt, chú giải bên phải."""
    assert abs(sum(pcts) - 100) < 1e-6, pcts
    o = ['\\begin{tikzpicture}[x=1cm, y=1cm]']
    a = 90.0
    for i, (c, p) in enumerate(zip(cats, pcts)):
        b = a - 3.6 * p; colr = col(PIE[i % len(PIE)])
        o.append('\\fill[fill=%s, draw=white, line width=1pt] (0,0) -- (%.4f:%s) arc[start angle=%.4f, end angle=%.4f, radius=%scm] -- cycle;' % (colr, a, R, a, b, R))
        m = (a + b) / 2; inside = p >= 8
        rr = R * 0.64 if inside else R + 0.42
        o.append('\\node[font=\\footnotesize\\bfseries, text=%s] at (%.4f:%s) {%s\\%%};' % ('white' if inside else 'ink', m, rr, _n(p, vi)))
        a = b
    o.append('\\draw[white, line width=1pt] (0,0) circle (%s);' % R)
    for i, c in enumerate(cats):
        y = 0.45 * (len(cats) - 1) / 2 - 0.45 * i
        o.append('\\fill[fill=%s] (%s,%.3f) rectangle ++(0.32,0.26);' % (col(PIE[i % len(PIE)]), R + 0.9, y - 0.13))
        o.append('\\node[anchor=west, font=\\small, text=ink] at (%s,%.3f) {%s};' % (R + 1.32, y, _t(c)))
    o.append('\\node[font=\\bfseries\\small, text=ink] at (%s,%s) {%s};' % (0.9, R + 0.55, _t(title)))
    o.append('\\end{tikzpicture}')
    return texsvg('\n'.join(o))


def _img(fn, alt, px):
    _USED.append(fn)
    return ('<img src="../../../img/tex/%s" alt="%s" loading="lazy" style="display:block;margin:6px auto;width:min(100%%,%dpx);height:auto">'
            % (fn, _h.escape(alt, quote=True), px))


def BI(fn_en, fn_vi, alt_en, alt_vi, px=520):
    """Ảnh hai bản: bản tiếng Anh (Mức 2, 3) và bản tiếng Việt (Mức 1)."""
    return ('<span class="txi" style="display:block"><span class="en" style="display:block">%s</span><span class="vi" style="display:block">%s</span></span>'
            % (_img(fn_en, alt_en, px), _img(fn_vi, alt_vi, px)))


def CHART(kind, en, vi, cap=None, px=520):
    """kind: 'bar' | 'line' | 'pie'. en, vi: dict tham số (cats, vals/pcts, xlab, ylab, title…) cho từng ngôn ngữ."""
    f = {'bar': bar_svg, 'line': line_svg, 'pie': pie_svg}[kind]
    fe = f(**en); fv = f(vi=True, **vi)
    alt_e = en.get('title', 'Chart'); alt_v = vi.get('title', 'Biểu đồ')
    c = '<figcaption>%s</figcaption>' % TI(*cap) if cap else ''
    return '<figure class="mbl-fig mbl-figtex">%s%s</figure>' % (BI(fe, fv, alt_e, alt_v, px), c)


def CHART_Q(kind, en, vi, px=440):
    """Cặp ảnh dùng trong đề câu hỏi tự luyện: trả về (html_en, html_vi) để ghép vào q['en'], q['vi']."""
    f = {'bar': bar_svg, 'line': line_svg, 'pie': pie_svg}[kind]
    fe = f(**en); fv = f(vi=True, **vi)
    return (_img(fe, en.get('title', 'Chart'), px), _img(fv, vi.get('title', 'Biểu đồ'), px))


def HT(rows):
    """Bảng ngang song ngữ kẻ đủ đường (bảng tần số SGK). rows: [((nhãn_en, nhãn_vi), [ô, ...]), ...];
    ô là số/chuỗi chung hoặc cặp (en, vi) khi khác nhau (ví dụ số thập phân)."""
    def cell(v):
        if isinstance(v, tuple): return TI(*v)
        return str(v)
    body = ''.join('<tr><th scope="row">%s</th>%s</tr>' % (TI(*lab), ''.join('<td>%s</td>' % cell(v) for v in cells)) for lab, cells in rows)
    return '<div class="mbl-tablewrap mbl-freqwrap"><table class="mbl-table mbl-freq"><tbody>%s</tbody></table></div>' % body
