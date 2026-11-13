# -*- coding: utf-8 -*-
"""Bảng tần số / tần số ghép nhóm theo cách trình bày Toán THPT Việt Nam (bảng ngang, kẻ đủ đường).

FREQ(edges, freqs, rows=('group','freq'), ...) -> HTML <table> dùng được trong lời giải, ví dụ, đề bài.
  edges  : các đầu mút a1<a2<...<a_{k+1} (int, float, str '0.5', Fraction)
  freqs  : tần số n_i (số nguyên)
  rows   : tùy chọn và theo thứ tự hiển thị: 'group' Nhóm | 'mid' Giá trị đại diện | 'freq' Tần số |
           'rel' Tần số tương đối (tần suất) | 'cum' Tần số tích lũy
  last_closed=True : nhóm cuối dạng [a;b]; các nhóm còn lại [a;b)
  rel='pct' (phần trăm) | 'frac' (phân số n_i/n) | 'dec' (số thập phân)
  total=True : thêm cột "Cộng" ghi n
  Tự tính: giá trị đại diện, tần suất, tần số tích lũy, cỡ mẫu. Số thập phân dùng dấu phẩy {,} (chuẩn Việt Nam).
Công thức viết bằng LaTeX trong \\( \\) (MathJax trên web; cú pháp tương thích KaTeX).
"""
from fractions import Fraction as F

LABELS = {'group': ('Nhóm', 'Group', ''), 'mid': ('Giá trị đại diện', 'Midpoint', 'x_i'), 'freq': ('Tần số', 'Frequency', 'n_i'),
          'rel': ('Tần số tương đối', 'Relative frequency', 'f_i'), 'cum': ('Tần số tích lũy', 'Cumulative frequency', '')}

def _fr(x):
    if isinstance(x, F): return x
    if isinstance(x, float): return F(str(x))
    return F(str(x))

def num(x, comma=True):
    """Định dạng LaTeX: số nguyên, số thập phân hữu hạn (dấu phẩy) hoặc phân số tối giản."""
    x = F(x); 
    if x.denominator == 1: return str(x.numerator)
    d = x.denominator
    while d % 2 == 0: d //= 2
    while d % 5 == 0: d //= 5
    if d == 1:
        s = ('%.10f' % float(x)).rstrip('0'); return s.replace('.', '{,}' if comma else '.')
    return ('-' if x < 0 else '') + '\\dfrac{%d}{%d}' % (abs(x.numerator), x.denominator)

def interval(a, b, closed=False): return '[%s;\\,%s%s' % (num(a), num(b), ']' if closed else ')')

class FT:
    def __init__(s, edges, freqs, last_closed=False):
        s.e = [_fr(x) for x in edges]; s.f = list(freqs); assert len(s.e) == len(s.f) + 1 and all(s.e[i] < s.e[i + 1] for i in range(len(s.f)))
        s.n = sum(s.f); s.k = len(s.f); s.lc = last_closed
    def group(s, i): return interval(s.e[i], s.e[i + 1], s.lc and i == s.k - 1)
    def mid(s, i): return (s.e[i] + s.e[i + 1]) / 2
    def rel(s, i): return F(s.f[i], s.n)
    def cum(s, i): return sum(s.f[:i + 1])
    def mean(s): return sum(s.f[i] * s.mid(i) for i in range(s.k)) / s.n

def FREQ(edges, freqs, rows=('group', 'freq'), last_closed=False, rel='pct', total=True, cls='', caption=None, labels=None, unknown=None, lang=None):
    """lang='en' | 'vi': nhãn và dấu thập phân theo một ngôn ngữ (dùng cho bảng song ngữ T(en, vi)); None: như cũ."""
    t = edges if isinstance(edges, FT) else FT(edges, freqs, last_closed)
    def relcell(i):
        v = t.rel(i)
        if rel == 'frac': return '\\(%s\\)' % (num(v) if v.denominator == 1 else '\\dfrac{%d}{%d}' % (t.f[i], t.n))
        if rel == 'dec': return '\\(%s\\)' % num(v)
        return '\\(%s\\%%\\)' % num(v * 100)
    cells = {'group': lambda i: '\\(%s\\)' % t.group(i), 'mid': lambda i: '\\(%s\\)' % num(t.mid(i)), 'freq': lambda i: ('\\(x\\)' if i == unknown else '\\(%d\\)' % t.f[i]), 'rel': relcell, 'cum': lambda i: '\\(%d\\)' % t.cum(i)}
    tot = {'group': 'Cộng / Total', 'freq': '\\(n=%d\\)' % t.n, 'rel': '\\(%s\\)' % ('100\\%' if rel == 'pct' else '1'), 'mid': '', 'cum': ''}
    out = ['<div class="mbl-tablewrap mbl-freqwrap"><table class="mbl-table mbl-freq%s">' % (' ' + cls if cls else '')]
    if caption: out.append('<caption>%s</caption>' % caption)
    out.append('<tbody>')
    for r in rows:
        vi, en, sy = LABELS[r]
        lab = (labels or {}).get(r) or '%s%s' % (en if lang == 'en' else vi, (' \\(%s\\)' % sy) if sy else '')
        row = '<tr><th scope="row">%s</th>' % lab
        row += ''.join(('<th scope="col">%s</th>' if r == 'group' else '<td>%s</td>') % cells[r](i) for i in range(t.k))
        if total: row += '<td class="mbl-freq-tot">%s</td>' % (tot[r] if r != 'group' else ('Total' if lang == 'en' else 'Cộng'))
        out.append(row + '</tr>')
    out.append('</tbody></table></div>')
    h = ''.join(out)
    return h.replace('{,}', '.') if lang == 'en' else h

if __name__ == '__main__':
    print(FREQ([0, 10, 20, 30, 40], [4, 12, 20, 14], rows=('group', 'mid', 'freq', 'rel', 'cum')))
    t = FT(['0.5', '1.5', '2.5'], [3, 5], True); assert t.mean() == F(3 * 1 + 5 * 2, 8) and num(F(1, 3)) == '\\dfrac{1}{3}' and num(F(5, 4)) == '1{,}25'
