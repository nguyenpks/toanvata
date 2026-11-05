# -*- coding: utf-8 -*-
"""Sinh js/art.js: hình Toán học (đồ thị, hình không gian, công thức) dạng SVG để làm nền chìm cho trang chủ."""
import math, json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
G = '#046B4D'

def path(pts):
    return 'M' + ' L'.join('%.1f %.1f' % p for p in pts)

def curve(f, x0, x1, mp, n=90, clip=None):
    segs, cur = [], []
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n
        try: y = f(x)
        except ZeroDivisionError: y = None
        if y is None or (clip and abs(y) > clip):
            if len(cur) > 1: segs.append(cur)
            cur = []
        else: cur.append(mp(x, y))
    if len(cur) > 1: segs.append(cur)
    return ''.join('<path d="%s"/>' % path(s) for s in segs)

def line(a, b, dash=False):
    return '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"%s/>' % (a[0], a[1], b[0], b[1], ' stroke-dasharray="6 6"' if dash else '')

def plane(ox, oy, w, h, xr, yr, grid=True):
    (x0, x1), (y0, y1) = xr, yr
    mp = lambda x, y: (ox + (x - x0) / (x1 - x0) * w, oy + h - (y - y0) / (y1 - y0) * h)
    s = ''
    if grid:
        s += '<g stroke-width="1" opacity=".45">'
        for gx in range(int(math.ceil(x0)), int(x1) + 1): s += line(mp(gx, y0), mp(gx, y1))
        for gy in range(int(math.ceil(y0)), int(y1) + 1): s += line(mp(x0, gy), mp(x1, gy))
        s += '</g>'
    s += line(mp(x0, 0), mp(x1, 0)) + line(mp(0, y0), mp(0, y1))
    s += '<path d="M%.1f %.1f l-9 -4 l0 8 z M%.1f %.1f l-4 9 l8 0 z" fill="%s" stroke="none"/>' % (mp(x1, 0)[0], mp(x1, 0)[1], mp(0, y1)[0], mp(0, y1)[1], G)
    return s, mp

def cube(x, y, s=110, d=(46, -40)):
    A = (x, y + s); B = (x + s, y + s); C = (x + s, y); D = (x, y)
    sh = lambda p: (p[0] + d[0], p[1] + d[1])
    o = '<path d="%s Z"/>' % path([A, B, C, D])
    o += '<path d="%s"/>' % path([D, sh(D), sh(C), C]) + line(sh(C), sh(B)) + line(B, sh(B))
    o += line(sh(D), sh(A), True) + line(A, sh(A), True) + line(sh(A), sh(B), True)
    return o

def sphere(cx, cy, r):
    o = '<circle cx="%d" cy="%d" r="%d"/>' % (cx, cy, r)
    o += '<path d="M%d %d A%d %d 0 0 0 %d %d"/>' % (cx - r, cy, r, r * .3, cx + r, cy)
    o += '<path d="M%d %d A%d %d 0 0 1 %d %d" stroke-dasharray="6 6"/>' % (cx - r, cy, r, r * .3, cx + r, cy)
    o += '<ellipse cx="%d" cy="%d" rx="%d" ry="%d" opacity=".6"/>' % (cx, cy, r * .38, r)
    return o

def cone(cx, top, h, r):
    by = top + h; k = r * .28
    o = line((cx, top), (cx - r, by)) + line((cx, top), (cx + r, by))
    o += '<path d="M%d %d A%d %d 0 0 0 %d %d"/>' % (cx - r, by, r, k, cx + r, by)
    o += '<path d="M%d %d A%d %d 0 0 1 %d %d" stroke-dasharray="6 6"/>' % (cx - r, by, r, k, cx + r, by)
    o += line((cx, top), (cx, by), True)
    return o

def cylinder(cx, top, h, r):
    k = r * .28; by = top + h
    o = '<ellipse cx="%d" cy="%d" rx="%d" ry="%.1f"/>' % (cx, top, r, k)
    o += line((cx - r, top), (cx - r, by)) + line((cx + r, top), (cx + r, by))
    o += '<path d="M%d %d A%d %.1f 0 0 0 %d %d"/>' % (cx - r, by, r, k, cx + r, by)
    o += '<path d="M%d %d A%d %.1f 0 0 1 %d %d" stroke-dasharray="6 6"/>' % (cx - r, by, r, k, cx + r, by)
    return o

def tetra(x, y, s=120):
    A = (x, y + s * .7); B = (x + s, y + s * .7); C = (x + s * .55, y + s * .95); T = (x + s * .45, y)
    o = '<path d="%s Z"/>' % path([A, T, B]) + line(T, C) + line(A, C) + line(C, B)
    o += line(A, B, True)
    return o

def text(x, y, t, size=56, rot=0):
    return '<text x="%d" y="%d" font-size="%d" transform="rotate(%d %d %d)" fill="%s" stroke="none" font-family="\'Cambria Math\',\'STIX Two Math\',\'Times New Roman\',serif" font-style="italic">%s</text>' % (x, y, size, rot, x, y, G, t)

def svg(vb, body, extra=''):
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="%s" %s aria-hidden="true" focusable="false"><g fill="none" stroke="%s" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">%s</g></svg>' % (vb, extra, G, body)

# ---------------- nền chìm toàn trang ----------------
b = ''
p, mp = plane(660, 30, 300, 240, (-4, 4), (-2, 6))
b += p + curve(lambda x: x * x / 2 - 1, -3.9, 3.9, mp) + curve(lambda x: 2.2 * math.sin(1.6 * x) + 2, -4, 4, mp, 120)
p, mp = plane(50, 330, 300, 260, (-4, 4), (-4, 4))
b += p + curve(lambda x: 1 / x, -4, 4, mp, 200, clip=4) + curve(lambda x: 1 / x + 1.5, -4, 4, mp, 200, clip=2.5)
b += line(mp(-4, 1.5), mp(4, 1.5), True)
b += cube(700, 430) + sphere(150, 720, 80) + cone(800, 790, 150, 80) + cylinder(850, 1130, 120, 55)
b += '<path d="%s Z"/>' % path([(60, 1110), (230, 1110), (60, 990)]) + '<path d="M60 1096 h14 v14"/>'
b += '<rect x="60" y="1110" width="170" height="170"/><rect x="-110" y="990" width="170" height="120"/>' if False else ''
p, mp = plane(520, 1250, 380, 160, (-4, 4), (0, 1.2), grid=False)
b += curve(lambda x: math.exp(-x * x / 2), -4, 4, mp, 120) + line(mp(-1, 0), mp(-1, .61), True) + line(mp(1, 0), mp(1, .61), True)
b += tetra(90, 1290, 130)
b += text(430, 140, '∫', 120) + text(480, 700, 'Σ', 90) + text(70, 665, 'π', 70) + text(860, 770, '√x', 60) + text(250, 1060, 'a²+b²=c²', 38) \
   + text(380, 1400, 'sin²x+cos²x=1', 36) + text(300, 960, 'f(x)', 54) + text(560, 440, 'lim', 40) + text(40, 1440, 'Δ = b²−4ac', 34) + text(900, 470, '∞', 70) + text(300, 640, 'x²+y²=r²', 34)
BACK = svg('0 0 1000 1500', b, 'preserveAspectRatio="xMidYMin slice" class="art-bg"')

# ---------------- hình trong khung hero (nét trắng) ----------------
h = ''
p, mp = plane(30, 40, 250, 200, (-4, 4), (-3, 4))
h += p + curve(lambda x: 0.3 * x ** 3 - 1.5 * x, -3.2, 3.2, mp, 90, clip=3.8) + curve(lambda x: 1.8 * math.sin(1.7 * x), -4, 4, mp, 120)
h += cube(330, 70, 90, (38, -32)) + sphere(470, 190, 52) + cone(380, 190, 80, 48)
h += text(330, 280, '∫ f(x)dx', 30) + text(30, 285, 'y = f(x)', 26)
HERO = svg('0 0 540 310', h, 'preserveAspectRatio="xMaxYMid meet" class="art-hero"').replace(G, '#ffffff')

# ---------------- biểu tượng ba cấp học ----------------
def icon(body): return svg('0 0 120 90', body, 'class="art-stage"')
TH = icon(text(6, 50, '1 2 3', 34) + '<rect x="62" y="12" width="28" height="28"/><circle cx="104" cy="26" r="13"/><path d="M62 78 L92 78 L77 52 Z"/>')
THCS = icon('<path d="M10 78 L70 78 L10 28 Z"/><path d="M10 66 h12 v12"/><circle cx="92" cy="40" r="22"/><path d="M92 40 L108 28"/>' + text(30, 68, 'x', 20))
THPT = icon(line((8, 76), (112, 76)) + line((18, 84), (18, 8)) + curve(lambda x: math.sin(x), 0, 6.2, lambda x, y: (18 + x * 15, 42 - y * 24), 60) + cube(70, 10, 20, (10, -8)))

js = '/* Sinh tự động bởi tools/make_art.py – hình Toán học làm nền chìm cho trang chủ. Không sửa tay. */\nwindow.MathBridgeArt = ' + json.dumps({'back': BACK, 'hero': HERO, 'stage': {'th': TH, 'thcs': THCS, 'thpt': THPT}}, ensure_ascii=False) + ';\n'
open(os.path.join(ROOT, 'js', 'art.js'), 'w', encoding='utf-8').write(js)
print('art.js', len(js), 'bytes')
