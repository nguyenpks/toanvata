# -*- coding: utf-8 -*-
"""Hiệu chỉnh lớp 12 – đợt 1 (13/11/2026): phần D (8 câu trắc nghiệm, 8 DẠNG khác nhau, khác các dạng ở A–C) cho
Bài 5 (ứng dụng đạo hàm), 6 (vectơ trong không gian), 7 (hệ trục Oxyz), 8 (biểu thức tọa độ), 11 (nguyên hàm), 12 (tích phân).
Mỗi hàm sinh (r, lv, ctx) → dict(en, vi, opts (opts[0] đúng), ee, ev[, fig]). Đáp án tính trong hàm (Fraction / số nguyên),
kiểm tra độc lập ở scripts/audit11.py."""
import math, random, itertools
from fractions import Fraction as F
from sp_g11r import tx, ne, nv, nopt, nopts, Q3D
from sp_g11r2 import frt, fo, V
import fig2d as G
from fig2d import Canvas, lw

def M(s): return '\\(%s\\)' % s
def V3(p): return '(%s;\\,%s;\\,%s)' % tuple(frt(x) for x in p)
def V3s(p): return '(%s;%s;%s)' % tuple(frt(x) for x in p)
def sq(n):
    """√n rút gọn → TeX (n nguyên ≥ 0)."""
    n = int(n); a, b = 1, n; k = 2
    while k * k <= b:
        while b % (k * k) == 0: b //= k * k; a *= k
        k += 1
    if b == 1: return str(a)
    return ('' if a == 1 else str(a)) + '\\sqrt{%d}' % b
def ksq(c, n):
    """c·√n (c Fraction) → TeX."""
    n = int(n); a, b = 1, n; k = 2
    while k * k <= b:
        while b % (k * k) == 0: b //= k * k; a *= k
        k += 1
    c = F(c) * a
    if b == 1: return frt(c)
    if c == 1: return '\\sqrt{%d}' % b
    if c.denominator == 1: return '%d\\sqrt{%d}' % (c.numerator, b)
    return '\\dfrac{%s\\sqrt{%d}}{%d}' % ('' if abs(c.numerator) == 1 else abs(c.numerator), b, c.denominator) if c > 0 else '-' + ksq(-c / a, n)
def dot(a, b): return sum(x * y for x, y in zip(a, b))
def sub(a, b): return tuple(x - y for x, y in zip(a, b))
def add(a, b): return tuple(x + y for x, y in zip(a, b))
def mul(k, a): return tuple(F(k) * x for x in a)
def n2(a): return dot(a, a)
def isq(n): return n >= 0 and math.isqrt(n) ** 2 == n

# =============================================================== Bài 5 – Ứng dụng đạo hàm giải bài toán thực tiễn
def o5_semicircle(r, lv, ctx):
    R = r.choice([4, 5, 6, 8, 10, 12])
    c = Canvas(); s = 2.3; xr = s / math.sqrt(2)
    arc = [(s * math.cos(math.pi * i / 90), s * math.sin(math.pi * i / 90)) for i in range(91)]
    c.poly([(-s - .35, 0), (s + .35, 0)], 'ink, line width=0.8pt'); c.poly(arc, 'color=%s, line width=1.2pt' % G.col(G.GREEN))
    c.poly([(-xr, 0), (-xr, xr), (xr, xr), (xr, 0)], 'color=%s, line width=1.1pt' % G.col(G.ORANGE))
    c.poly([(0, 0), (xr, xr)], 'ink, line width=0.6pt, dash pattern=on 3pt off 2pt')
    for p in [(-xr, 0), (xr, 0), (xr, xr), (-xr, xr), (0, 0)]: c.dot(*p)
    for (x, y), nm, cd in [((-xr, 0), 'A', [(0, -.3)]), ((xr, 0), 'B', [(0, -.3)]), ((xr, xr), 'C', [(.3, .25), (.32, 0)]), ((-xr, xr), 'D', [(-.3, .25), (-.32, 0)]), ((0, 0), 'O', [(0, -.3)])]:
        c.label(x, y, '$%s$' % nm, .3, .36, cd)
    c.label(xr / 2, xr / 2, '$R$', .3, .36, [(-.18, .22), (.22, -.18)])
    fig = G.FIG(c.svg(), 'Rectangle in a semicircle', 'Hình chữ nhật nội tiếp nửa hình tròn', 330)
    good = R * R
    return dict(en='A window has the shape of a rectangle \\(ABCD\\) inscribed in a semicircle of radius \\(R=%d\\) dm (see the figure; \\(A\\), \\(B\\) lie on the diameter). What is the largest possible area of the rectangle (dm²)?' % R,
                vi='Một ô cửa có dạng hình chữ nhật \\(ABCD\\) nội tiếp nửa hình tròn bán kính \\(R=%d\\) dm (xem hình; \\(A\\), \\(B\\) nằm trên đường kính). Diện tích lớn nhất của hình chữ nhật là bao nhiêu (dm²)?' % R,
                opts=nopts(r, good, [F(good, 2), 2 * good, F(3 * good, 4)]), fig=fig,
                ee='Let \\(OB=x\\); then \\(BC=\\sqrt{%d-x^2}\\) and \\(S=2x\\sqrt{%d-x^2}\\). \\(S^2=4x^2(%d-x^2)\\) is largest when \\(x^2=%s\\), so \\(S_{\\max}=R^2=%d\\).' % (R * R, R * R, R * R, frt(F(R * R, 2)), good),
                ev='Đặt \\(OB=x\\); khi đó \\(BC=\\sqrt{%d-x^2}\\) và \\(S=2x\\sqrt{%d-x^2}\\). \\(S^2=4x^2(%d-x^2)\\) lớn nhất khi \\(x^2=%s\\), nên \\(S_{\\max}=R^2=%d\\).' % (R * R, R * R, R * R, frt(F(R * R, 2)), good))

def o5_can(r, lv, ctx):
    rr = r.choice([2, 3, 4, 5]); Vk = 2 * rr ** 3
    if lv < 3:
        return dict(en='A closed cylindrical can must hold \\(%d\\pi\\ \\text{cm}^3\\). Which base radius (cm) uses the least metal (smallest total surface area)?' % Vk,
                    vi='Một lon hình trụ có nắp cần chứa \\(%d\\pi\\ \\text{cm}^3\\). Bán kính đáy bằng bao nhiêu (cm) thì tốn ít vật liệu nhất (diện tích toàn phần nhỏ nhất)?' % Vk,
                    opts=nopts(r, rr, [2 * rr, rr + 1, rr - 1 if rr > 2 else rr + 2]),
                    ee='\\(h=\\dfrac{%d}{r^2}\\), \\(S=2\\pi r^2+\\dfrac{%d\\pi}{r}\\), \\(S\'=4\\pi r-\\dfrac{%d\\pi}{r^2}=0\\Leftrightarrow r^3=%d\\Leftrightarrow r=%d\\).' % (Vk, 2 * Vk, 2 * Vk, rr ** 3, rr),
                    ev='\\(h=\\dfrac{%d}{r^2}\\), \\(S=2\\pi r^2+\\dfrac{%d\\pi}{r}\\), \\(S\'=4\\pi r-\\dfrac{%d\\pi}{r^2}=0\\Leftrightarrow r^3=%d\\Leftrightarrow r=%d\\).' % (Vk, 2 * Vk, 2 * Vk, rr ** 3, rr))
    S = 6 * rr * rr
    return dict(en='A closed cylindrical can must hold \\(%d\\pi\\ \\text{cm}^3\\). What is the smallest possible total surface area (cm²)?' % Vk,
                vi='Một lon hình trụ có nắp cần chứa \\(%d\\pi\\ \\text{cm}^3\\). Diện tích toàn phần nhỏ nhất của lon là bao nhiêu (cm²)?' % Vk,
                opts=['%d\\pi' % S, '%d\\pi' % (4 * rr * rr), '%d\\pi' % (8 * rr * rr), '%d\\pi' % (S + 2 * rr)],
                ee='The minimum is at \\(r=%d\\), \\(h=%d\\): \\(S=2\\pi\\cdot%d+2\\pi\\cdot%d\\cdot%d=%d\\pi\\).' % (rr, 2 * rr, rr * rr, rr, 2 * rr, S),
                ev='Nhỏ nhất khi \\(r=%d\\), \\(h=%d\\): \\(S=2\\pi\\cdot%d+2\\pi\\cdot%d\\cdot%d=%d\\pi\\).' % (rr, 2 * rr, rr * rr, rr, 2 * rr, S))

PIPE = [(5, 4, 3, 4), (5, 4, 6, 8), (5, 3, 4, 3), (5, 3, 8, 6), (13, 12, 5, 12), (5, 4, 9, 12)]   # c1, c2, rộng w, x*
def o5_pipe(r, lv, ctx):
    c1, c2, w, x = r.choice(PIPE); assert F(c1 * x) ** 2 == F(c2) ** 2 * (w * w + x * x)
    b = x + r.choice([3, 4, 5, 6]); k = r.choice([10, 20])
    c = Canvas(); W_ = 7.0; Hh = 1.6; sx = W_ / (b + 1)
    c.o.append('\\fill[color=%s, opacity=0.18] (0,0) rectangle (%.3f,%.3f);' % (G.col(G.BLUE), W_, Hh))
    c.poly([(0, 0), (W_, 0)], 'ink, line width=0.7pt'); c.poly([(0, Hh), (W_, Hh)], 'ink, line width=0.7pt')
    A = (0.5, 0); H = (0.5, Hh); P = (0.5 + x * sx, Hh); B = (0.5 + b * sx, Hh)
    c.poly([A, P], 'color=%s, line width=1.2pt' % G.col(G.ORANGE)); c.poly([P, B], 'color=%s, line width=1.2pt' % G.col(G.GREEN))
    c.poly([A, H], 'ink, line width=0.6pt, dash pattern=on 3pt off 2pt')
    for p in (A, H, P, B): c.dot(*p)
    c.label(*A, '$A$', .3, .36, [(0, -.3), (-.3, -.2)]); c.label(*H, '$H$', .3, .36, [(0, .3), (-.3, .25)])
    c.label(*P, '$M$', .3, .36, [(0, .3), (.25, .3)]); c.label(*B, '$B$', .3, .36, [(0, .3), (.3, .25)])
    fig = G.FIG(c.svg(), 'River and cable', 'Dòng sông và đường dây', 380)
    en = ('A power station \\(A\\) is on one bank of a straight river \\(%d\\) km wide; a factory \\(B\\) is on the other bank, \\(%d\\) km from the point \\(H\\) opposite \\(A\\) (see the figure). '
          'A cable goes underwater from \\(A\\) to \\(M\\) on the other bank, then along the bank to \\(B\\). It costs \\(%d\\) million VND per km underwater and \\(%d\\) million VND per km on land. How far from \\(H\\) should \\(M\\) be (km) to make the cost smallest?' % (w, b, c1 * k, c2 * k))
    vi = ('Nhà máy điện \\(A\\) ở một bờ sông thẳng rộng \\(%d\\) km; xưởng \\(B\\) ở bờ bên kia, cách điểm \\(H\\) đối diện \\(A\\) là \\(%d\\) km (xem hình). '
          'Dây điện đi dưới nước từ \\(A\\) tới \\(M\\) ở bờ bên kia rồi đi dọc bờ tới \\(B\\). Chi phí là \\(%d\\) triệu đồng/km dưới nước và \\(%d\\) triệu đồng/km trên bờ. Điểm \\(M\\) cách \\(H\\) bao nhiêu km thì chi phí nhỏ nhất?' % (w, b, c1 * k, c2 * k))
    return dict(en=en, vi=vi, opts=nopts(r, x, [b, w, 0, x + 1]), fig=fig,
                ee='\\(C(x)=%d\\sqrt{%d+x^2}+%d(%d-x)\\); \\(C\'(x)=0\\Leftrightarrow %d x=%d\\sqrt{%d+x^2}\\Leftrightarrow x=%d\\).' % (c1 * k, w * w, c2 * k, b, c1, c2, w * w, x),
                ev='\\(C(x)=%d\\sqrt{%d+x^2}+%d(%d-x)\\); \\(C\'(x)=0\\Leftrightarrow %d x=%d\\sqrt{%d+x^2}\\Leftrightarrow x=%d\\).' % (c1 * k, w * w, c2 * k, b, c1, c2, w * w, x))

def o5_ticket(r, lv, ctx):
    for _ in range(500):
        p0 = r.choice([40, 50, 60, 80]); s = r.choice([5, 10]); d = r.choice([2, 4, 5, 10, 20]); k = r.randint(2, 8)
        if (d * (2 * s * k + p0)) % s: continue
        n0 = d * (2 * s * k + p0) // s
        if 100 <= n0 <= 600 and n0 - d * 2 * k > 0: break
    else: raise AssertionError
    best = p0 + s * k
    R_ = lambda j: (p0 + s * j) * (n0 - d * j)
    assert all(R_(k) >= R_(j) for j in range(0, n0 // d))
    return dict(en='A cinema sells \\(%d\\) tickets a day at \\(%d\\) thousand VND each. Each time the price rises by \\(%d\\) thousand VND, it sells \\(%d\\) fewer tickets. Which price (thousand VND) gives the largest revenue?' % (n0, p0, s, d),
                vi='Một rạp chiếu phim bán được \\(%d\\) vé mỗi ngày với giá \\(%d\\) nghìn đồng/vé. Cứ tăng giá thêm \\(%d\\) nghìn đồng thì bán ít đi \\(%d\\) vé. Giá vé bao nhiêu (nghìn đồng) thì doanh thu lớn nhất?' % (n0, p0, s, d),
                opts=nopts(r, best, [p0, best + s, best - s, p0 + s * 2 * k]),
                ee='After \\(x\\) rises: \\(R(x)=(%d+%dx)(%d-%dx)\\), \\(R\'(x)=0\\Leftrightarrow x=%d\\), price \\(%d+%d\\cdot%d=%d\\).' % (p0, s, n0, d, k, p0, s, k, best),
                ev='Sau \\(x\\) lần tăng: \\(R(x)=(%d+%dx)(%d-%dx)\\), \\(R\'(x)=0\\Leftrightarrow x=%d\\), giá vé \\(%d+%d\\cdot%d=%d\\).' % (p0, s, n0, d, k, p0, s, k, best))

def o5_drug(r, lv, ctx):
    b = r.choice([1, 4, 9, 16]); rb = math.isqrt(b); m = r.choice([1, 2, 3, F(1, 2), F(3, 2)]); a = 2 * rb * m
    if a.denominator != 1 if isinstance(a, F) else False: raise AssertionError
    a = int(a); cm = F(a, 2 * rb)
    fx = 'C(t)=\\dfrac{%dt}{t^2+%d}' % (a, b)
    if lv == 1:
        return dict(en='After an injection, the concentration of a drug in the blood is \\(%s\\) (mg/l), \\(t\\) in hours. After how many hours is the concentration highest?' % fx,
                    vi='Sau khi tiêm, nồng độ thuốc trong máu là \\(%s\\) (mg/l), \\(t\\) tính bằng giờ. Sau bao nhiêu giờ thì nồng độ cao nhất?' % fx,
                    opts=nopts(r, rb, [b, 2 * rb, rb + 1, cm]),
                    ee='\\(C\'(t)=\\dfrac{%d(%d-t^2)}{(t^2+%d)^2}=0\\Leftrightarrow t=%d\\); \\(C\'\\) changes from \\(+\\) to \\(-\\).' % (a, b, b, rb),
                    ev='\\(C\'(t)=\\dfrac{%d(%d-t^2)}{(t^2+%d)^2}=0\\Leftrightarrow t=%d\\); \\(C\'\\) đổi dấu từ \\(+\\) sang \\(-\\).' % (a, b, b, rb))
    return dict(en='After an injection, the concentration of a drug in the blood is \\(%s\\) (mg/l), \\(t\\) in hours. What is the highest concentration (mg/l)?' % fx,
                vi='Sau khi tiêm, nồng độ thuốc trong máu là \\(%s\\) (mg/l), \\(t\\) tính bằng giờ. Nồng độ cao nhất là bao nhiêu (mg/l)?' % fx,
                opts=nopts(r, cm, [F(a, b + 1), F(a, rb) if rb > 1 else a, 2 * cm, cm + 1]),
                ee='Highest at \\(t=%d\\): \\(C(%d)=\\dfrac{%d}{%d}=%s\\).' % (rb, rb, a * rb, 2 * b, ne(cm)),
                ev='Cao nhất khi \\(t=%d\\): \\(C(%d)=\\dfrac{%d}{%d}=%s\\).' % (rb, rb, a * rb, 2 * b, nv(cm)))

def o5_ships(r, lv, ctx):
    k = r.choice([1, 2]); p, q = r.choice([(3, 4), (4, 3)]); p *= k; q *= k; j = r.choice([1, 2])
    d = 25 * k * j                       # t* = d p /(p²+q²)
    t = F(d * p, p * p + q * q); dm = F(d * q * 5 * k, (p * p + q * q))      # d·q/√(p²+q²), √ = 5k
    assert t.denominator == 1 and dm == F(d * q, 5 * k)
    c = Canvas(); L = 6.0
    c.poly([(0, 0), (L + .3, 0)], 'ink!85, line width=0.7pt, -{Stealth[length=2.4mm]}'); c.poly([(0, 0), (0, 3.2)], 'ink!85, line width=0.7pt, -{Stealth[length=2.4mm]}')
    c.poly([(L, 0), (L - 2.2, 0)], 'color=%s, line width=1.6pt, -{Stealth[length=2.6mm]}' % G.col(G.ORANGE)); c.poly([(0, 0), (0, 1.8)], 'color=%s, line width=1.6pt, -{Stealth[length=2.6mm]}' % G.col(G.BLUE))
    c.dot(L, 0); c.dot(0, 0)
    c.label(L, 0, '$A$', .3, .36, [(0, -.3)]); c.label(0, 0, '$O$', .3, .36, [(-.25, -.25)])
    c.label(L + .3, 0, '\\text{E}', .3, .36, [(0, .28)]); c.label(0, 3.2, '\\text{N}', .3, .36, [(.28, 0)])
    fig = G.FIG(c.svg(), 'Two ships', 'Hai con tàu', 300)
    if lv < 3:
        return dict(en='At noon ship \\(A\\) is \\(%d\\) km east of port \\(O\\) and sails west towards \\(O\\) at \\(%d\\) km/h; at the same time ship \\(B\\) leaves \\(O\\) sailing north at \\(%d\\) km/h. After how many hours are the ships closest?' % (d, p, q),
                    vi='Lúc 12 giờ, tàu \\(A\\) cách cảng \\(O\\) \\(%d\\) km về phía đông và đi về phía tây (về \\(O\\)) với vận tốc \\(%d\\) km/h; cùng lúc tàu \\(B\\) rời \\(O\\) đi về phía bắc với vận tốc \\(%d\\) km/h. Sau bao nhiêu giờ hai tàu gần nhau nhất?' % (d, p, q),
                    opts=nopts(r, t, [F(d, p), F(d, p + q), t + 1, F(d, q)]), fig=fig,
                    ee='\\(AB^2=(%d-%dt)^2+(%dt)^2\\); its derivative \\(2(%d)t-2\\cdot%d\\cdot%d=0\\Leftrightarrow t=%s\\).' % (d, p, q, p * p + q * q, d, p, ne(t)),
                    ev='\\(AB^2=(%d-%dt)^2+(%dt)^2\\); đạo hàm \\(2(%d)t-2\\cdot%d\\cdot%d=0\\Leftrightarrow t=%s\\).' % (d, p, q, p * p + q * q, d, p, nv(t)))
    return dict(en='Ship \\(A\\) is \\(%d\\) km east of port \\(O\\) and sails west towards \\(O\\) at \\(%d\\) km/h; at the same time ship \\(B\\) leaves \\(O\\) sailing north at \\(%d\\) km/h. What is the smallest distance between them (km)?' % (d, p, q),
                vi='Tàu \\(A\\) cách cảng \\(O\\) \\(%d\\) km về phía đông, đi về phía tây (về \\(O\\)) với vận tốc \\(%d\\) km/h; cùng lúc tàu \\(B\\) rời \\(O\\) đi về phía bắc với vận tốc \\(%d\\) km/h. Khoảng cách nhỏ nhất giữa hai tàu là bao nhiêu km?' % (d, p, q),
                opts=nopts(r, dm, [F(d, 2), d * F(p, 5 * k), dm + 5, t]), fig=fig,
                ee='Smallest at \\(t=%s\\): \\(AB=\\sqrt{%d^2+%d^2}=%s\\).' % (ne(t), int(d - p * t), int(q * t), ne(dm)),
                ev='Nhỏ nhất khi \\(t=%s\\): \\(AB=\\sqrt{%d^2+%d^2}=%s\\).' % (nv(t), int(d - p * t), int(q * t), nv(dm)))

def o5_pens(r, lv, ctx):
    n = r.choice([2, 3, 4]); m = r.choice([5, 10, 15]); L = 4 * (n + 1) * m
    x, y = (n + 1) * m, 2 * m; A = x * y; assert 2 * x + (n + 1) * y == L and A == F(L * L, 8 * (n + 1))
    c = Canvas(); W_, H_ = 5.6, 2.4
    c.poly([(0, 0), (W_, 0), (W_, H_), (0, H_)], 'color=%s, line width=1.3pt' % G.col(G.GREEN), close=True)
    for i in range(1, n): c.poly([(W_ * i / n, 0), (W_ * i / n, H_)], 'color=%s, line width=1.3pt' % G.col(G.GREEN))
    c.label(W_ / 2, 0, '$x$', .3, .36, [(0, -.3)]); c.label(0, H_ / 2, '$y$', .3, .36, [(-.3, 0)])
    fig = G.FIG(c.svg(), 'Pens', 'Chuồng', 300)
    return dict(en='A farmer uses \\(%d\\) m of fence to build a rectangular pen divided into \\(%d\\) equal parts by fences parallel to one side (see the figure). What is the largest total area (m²)?' % (L, n),
                vi='Một bác nông dân dùng \\(%d\\) m lưới rào thành một khu hình chữ nhật, chia thành \\(%d\\) ô bằng nhau bởi các hàng rào song song với một cạnh (xem hình). Tổng diện tích lớn nhất là bao nhiêu (m²)?' % (L, n),
                opts=nopts(r, A, [F(L * L, 16), F(L * L, 4 * (n + 2) * 4), F(L * L, 8 * n) if F(L * L, 8 * n) != A else A + 50, A + 2 * m]), fig=fig,
                ee='\\(2x+%dy=%d\\), \\(S=xy=\\dfrac{x(%d-2x)}{%d}\\), \\(S\'=0\\Leftrightarrow x=%d\\), \\(y=%d\\), \\(S=%d\\).' % (n + 1, L, L, n + 1, x, y, A),
                ev='\\(2x+%dy=%d\\), \\(S=xy=\\dfrac{x(%d-2x)}{%d}\\), \\(S\'=0\\Leftrightarrow x=%d\\), \\(y=%d\\), \\(S=%d\\).' % (n + 1, L, L, n + 1, x, y, A))

POSTER = [(2, 1, 5, 10), (2, 1, 6, 12), (3, 2, 4, 6), (3, 2, 6, 9), (4, 3, 6, 8), (3, 2, 8, 12)]   # lề trên/dưới a, lề bên b, chữ x×y (x/y=b/a)
def o5_poster(r, lv, ctx):
    a, b, x, y = r.choice(POSTER); A = x * y; assert F(x, y) == F(b, a)
    P = (x + 2 * b) * (y + 2 * a)
    for xx in range(1, 200):
        if A % xx == 0: assert (xx + 2 * b) * (A // xx + 2 * a) >= P
    c = Canvas(); s = 0.2; Wp, Hp = (x + 2 * b) * s * 1.0, (y + 2 * a) * s
    sc = 3.6 / max(Wp, Hp); Wp *= sc; Hp *= sc
    c.poly([(0, 0), (Wp, 0), (Wp, Hp), (0, Hp)], 'ink, line width=1.1pt', close=True)
    bx, ay = b * s * sc, a * s * sc
    c.o.append('\\fill[color=%s, opacity=0.25] (%.3f,%.3f) rectangle (%.3f,%.3f);' % (G.col(G.GREEN), bx, ay, Wp - bx, Hp - ay))
    c.poly([(bx, ay), (Wp - bx, ay), (Wp - bx, Hp - ay), (bx, Hp - ay)], 'ink, line width=0.6pt, dash pattern=on 3pt off 2pt', close=True)
    c.label(Wp / 2, Hp - ay / 2, '$%d$' % a, .3, .3, [(0, 0)]); c.label(bx / 2, Hp / 2, '$%d$' % b, .3, .3, [(0, 0)])
    c.poly([(Wp / 2 + .25, Hp - ay), (Wp / 2 + .25, Hp)], 'ink, line width=0.5pt, {Stealth[length=1.6mm]}-{Stealth[length=1.6mm]}'); c.poly([(0, Hp / 2 - .25), (bx, Hp / 2 - .25)], 'ink, line width=0.5pt, {Stealth[length=1.6mm]}-{Stealth[length=1.6mm]}')
    fig = G.FIG(c.svg(), 'Poster', 'Áp phích', max(120, min(260, round(300 * Wp / Hp))))
    return dict(en='The printed part of a poster has area \\(%d\\ \\text{dm}^2\\). The margins are \\(%d\\) dm at the top and bottom and \\(%d\\) dm at each side (see the figure). What is the smallest possible area of the poster (dm²)?' % (A, a, b),
                vi='Phần in chữ của một tấm áp phích có diện tích \\(%d\\ \\text{dm}^2\\). Lề trên và lề dưới đều rộng \\(%d\\) dm, lề hai bên đều rộng \\(%d\\) dm (xem hình). Diện tích nhỏ nhất của tấm áp phích là bao nhiêu (dm²)?' % (A, a, b),
                opts=nopts(r, P, [A + 2 * a * x + 2 * b * y, P + 4 * a * b, (y + 2 * b) * (x + 2 * a) if (y + 2 * b) * (x + 2 * a) != P else P + 8, A]), fig=fig,
                ee='Printed part \\(x\\times y\\), \\(xy=%d\\): \\(S=(x+%d)(y+%d)=%d+%dx+\\dfrac{%d}{x}\\), smallest at \\(x=%d\\), \\(y=%d\\): \\(S=%d\\cdot%d=%d\\).' % (A, 2 * b, 2 * a, A + 4 * a * b, 2 * a, 2 * b * A, x, y, x + 2 * b, y + 2 * a, P),
                ev='Phần chữ \\(x\\times y\\), \\(xy=%d\\): \\(S=(x+%d)(y+%d)=%d+%dx+\\dfrac{%d}{x}\\), nhỏ nhất khi \\(x=%d\\), \\(y=%d\\): \\(S=%d\\cdot%d=%d\\).' % (A, 2 * b, 2 * a, A + 4 * a * b, 2 * a, 2 * b * A, x, y, x + 2 * b, y + 2 * a, P))

D5 = [o5_semicircle, o5_can, o5_pipe, o5_ticket, o5_drug, o5_ships, o5_pens, o5_poster]

# =============================================================== Bài 6 – Vectơ trong không gian
CUBE1 = {'A': (0, 0, 0), 'B': (1, 0, 0), 'C': (1, 1, 0), 'D': (0, 1, 0), 'A′': (0, 0, 1), 'B′': (1, 0, 1), 'C′': (1, 1, 1), 'D′': (0, 1, 1)}
CUBE4 = {k: tuple(4 * x for x in v) for k, v in CUBE1.items()}
def vv(a, b): return '\\overrightarrow{%s}' % (a + b)
NICE = {F(1, 4): (60, 120), F(1, 2): (45, 135), F(0): (90, 90), F(3, 4): (30, 150)}

def v6_cube_angle(r, lv, ctx):
    names = list(CUBE1)
    for _ in range(2000):
        a, b, c_, d = r.sample(names, 4) if r.random() < .5 else (lambda s: (s[0], s[1], s[0], s[2]))(r.sample(names, 3))
        u, w = sub(CUBE1[b], CUBE1[a]), sub(CUBE1[d], CUBE1[c_])
        if n2(u) == 3 and n2(w) == 3: continue
        cs = F(dot(u, w) ** 2, n2(u) * n2(w))
        if cs not in NICE or cs == 1: continue
        ang = NICE[cs][0] if dot(u, w) >= 0 else NICE[cs][1]
        if ang in (90,) and r.random() < .6: continue
        break
    else: raise AssertionError
    cfg = {'solid': True, 'points': {k: tuple(float(x) for x in v) for k, v in CUBE4.items()},
           'segments': [[a, b, {'color': '#c2410c', 'width': 3, 'arrow': True}], [c_, d, {'color': '#1d4ed8', 'width': 3, 'arrow': True}]], 'px': 260}
    opts = [str(ang)] + [str(x) for x in (30, 45, 60, 90, 120, 135, 150) if x != ang]
    r.shuffle(opts[1:]); opts = [opts[0]] + [o for o in opts[1:] if o != str(180 - ang)][:2] + [str(180 - ang) if ang != 90 else '45']
    if len(set(opts)) < 4: raise AssertionError
    return dict(en='\\(ABCD.A′B′C′D′\\) is a cube. What is the angle (in degrees) between \\(%s\\) and \\(%s\\)?' % (vv(a, b), vv(c_, d)),
                vi='Cho hình lập phương \\(ABCD.A′B′C′D′\\). Góc (độ) giữa hai vectơ \\(%s\\) và \\(%s\\) bằng bao nhiêu?' % (vv(a, b), vv(c_, d)),
                opts=opts, fig=Q3D(cfg, 'Cube'),
                ee='Put the cube with edge 1 on coordinates: \\(%s=%s\\), \\(%s=%s\\), \\(\\cos=\\dfrac{%d}{\\sqrt{%d}\\cdot\\sqrt{%d}}\\), so the angle is \\(%d^\\circ\\).' % (vv(a, b), V3(u), vv(c_, d), V3(w), dot(u, w), n2(u), n2(w), ang),
                ev='Gắn hình lập phương cạnh 1 vào hệ tọa độ: \\(%s=%s\\), \\(%s=%s\\), \\(\\cos=\\dfrac{%d}{\\sqrt{%d}\\cdot\\sqrt{%d}}\\), nên góc bằng \\(%d^\\circ\\).' % (vv(a, b), V3(u), vv(c_, d), V3(w), dot(u, w), n2(u), n2(w), ang))

TETF = {'A': (F(-1, 5), F(3, 10), F(17, 5)), 'B': (F(-13, 5), 0, 0), 'C': (F(4, 5), -2, 0), 'D': (F(14, 5), F(8, 5), 0)}
def v6_centroid(r, lv, ctx):
    kind = r.choice(['tet', 'face'])
    P = dict(TETF)
    if kind == 'tet':
        P['G'] = tuple(sum(P[k][i] for k in 'ABCD') / 4 for i in range(3)); k = F(1, 4)
        en_w, vi_w = '\\(G\\) is the centroid of the tetrahedron \\(ABCD\\)', '\\(G\\) là trọng tâm của tứ diện \\(ABCD\\)'
    else:
        P['G'] = tuple(sum(P[k][i] for k in 'BCD') / 3 for i in range(3)); k = F(1, 3)
        en_w, vi_w = '\\(G\\) is the centroid of the face \\(BCD\\) of the tetrahedron \\(ABCD\\)', '\\(G\\) là trọng tâm của mặt \\(BCD\\) của tứ diện \\(ABCD\\)'
    lhs = sub(P['G'], P['A']); rhs = add(add(sub(P['B'], P['A']), sub(P['C'], P['A'])), sub(P['D'], P['A']))
    assert lhs == mul(k, rhs)
    segs = [['A', 'G', {'color': '#c2410c', 'width': 3, 'arrow': True}]] + ([['B', 'G', {'dash': True, 'width': 1.5}], ['C', 'G', {'dash': True, 'width': 1.5}], ['D', 'G', {'dash': True, 'width': 1.5}]] if kind == 'face' else [])
    cfg = {'solid': ['A', 'B', 'C', 'D'], 'points': {kk: tuple(float(x) for x in v) for kk, v in P.items()}, 'segments': segs, 'px': 260}
    pe, pv = V(lv, [('Then', 'Khi đó'), ('It is known that', 'Biết rằng'), ('Suppose', 'Giả sử')])
    return dict(en=('%s. ' + pe + ' \\(\\overrightarrow{AG}=k\\left(\\overrightarrow{AB}+\\overrightarrow{AC}+\\overrightarrow{AD}\\right)\\) with \\(k=\\)…') % en_w,
                vi=('%s. ' + pv + ' \\(\\overrightarrow{AG}=k\\left(\\overrightarrow{AB}+\\overrightarrow{AC}+\\overrightarrow{AD}\\right)\\) với \\(k=\\)…') % vi_w,
                opts=fo(k, [F(1, 3) if k == F(1, 4) else F(1, 4), F(1, 2), F(2, 3), F(3, 4)]), fig=Q3D(cfg, 'Tetrahedron'),
                ee=('\\(\\overrightarrow{GA}+\\overrightarrow{GB}+\\overrightarrow{GC}+\\overrightarrow{GD}=\\vec 0\\Rightarrow 4\\overrightarrow{AG}=\\overrightarrow{AB}+\\overrightarrow{AC}+\\overrightarrow{AD}\\).' if kind == 'tet'
                    else '\\(\\overrightarrow{GB}+\\overrightarrow{GC}+\\overrightarrow{GD}=\\vec 0\\Rightarrow 3\\overrightarrow{AG}=\\overrightarrow{AB}+\\overrightarrow{AC}+\\overrightarrow{AD}\\).'),
                ev=('\\(\\overrightarrow{GA}+\\overrightarrow{GB}+\\overrightarrow{GC}+\\overrightarrow{GD}=\\vec 0\\Rightarrow 4\\overrightarrow{AG}=\\overrightarrow{AB}+\\overrightarrow{AC}+\\overrightarrow{AD}\\).' if kind == 'tet'
                    else '\\(\\overrightarrow{GB}+\\overrightarrow{GC}+\\overrightarrow{GD}=\\vec 0\\Rightarrow 3\\overrightarrow{AG}=\\overrightarrow{AB}+\\overrightarrow{AC}+\\overrightarrow{AD}\\).'))

PRISMF = {'A': (0, 0, 0), 'B': (4, 0, 0), 'C': (1, 3, 0), 'A′': (0, 0, 4), 'B′': (4, 0, 4), 'C′': (1, 3, 4)}
def comb(c):
    """(ca, cb, cc) → TeX của ca·a + cb·b + cc·c."""
    out = ''
    for k, nm in zip(c, ('\\vec a', '\\vec b', '\\vec c')):
        k = F(k)
        if k == 0: continue
        t = nm if abs(k) == 1 else frt(abs(k)) + nm
        out += ('-' if k < 0 else ('+' if out else '')) + t
    return out or '\\vec 0'
def v6_prism(r, lv, ctx):
    P = dict(PRISMF); kind = r.choice(['M', 'N', 'G', 'K'])
    if kind == 'M': P['M'] = tuple(F(x + y, 2) for x, y in zip(P['B′'], P['C′'])); co = (1, F(1, 2), F(1, 2)); en_w, vi_w = '\\(M\\) is the midpoint of \\(B′C′\\)', '\\(M\\) là trung điểm của \\(B′C′\\)'
    elif kind == 'N': P['M'] = tuple(F(x + y, 2) for x, y in zip(P['B'], P['C′'])); co = (F(1, 2), F(1, 2), F(1, 2)); en_w, vi_w = '\\(M\\) is the midpoint of \\(BC′\\)', '\\(M\\) là trung điểm của \\(BC′\\)'
    elif kind == 'G': P['M'] = tuple(F(x + y + z, 3) for x, y, z in zip(P['A′'], P['B′'], P['C′'])); co = (1, F(1, 3), F(1, 3)); en_w, vi_w = '\\(M\\) is the centroid of triangle \\(A′B′C′\\)', '\\(M\\) là trọng tâm tam giác \\(A′B′C′\\)'
    else: P['M'] = tuple(F(x + y, 2) for x, y in zip(P['C'], P['C′'])); co = (F(1, 2), 0, 1); en_w, vi_w = '\\(M\\) is the midpoint of \\(CC′\\)', '\\(M\\) là trung điểm của \\(CC′\\)'
    a, b, c = sub(P['A′'], P['A']), sub(P['B'], P['A']), sub(P['C'], P['A'])
    assert sub(P['M'], P['A']) == add(add(mul(co[0], a), mul(co[1], b)), mul(co[2], c))
    bads = [(co[0], co[2], co[1]) if co[1] != co[2] else (co[1], co[0], co[2]), tuple(F(1, 2) * x if x != 1 else 1 for x in co[::-1]), (1, 1, 1), (co[0] * 2 if co[0] != 1 else F(1, 2), co[1], co[2]), (0, co[1], co[2]), (1, F(1, 2), 0)]
    cfg = {'solid': list(PRISMF), 'points': {kk: tuple(float(x) for x in v) for kk, v in P.items()}, 'segments': [['A', 'M', {'color': '#c2410c', 'width': 3, 'arrow': True}]], 'px': 260}
    return dict(en='\\(ABC.A′B′C′\\) is a triangular prism with \\(\\overrightarrow{AA′}=\\vec a\\), \\(\\overrightarrow{AB}=\\vec b\\), \\(\\overrightarrow{AC}=\\vec c\\); %s. Then \\(\\overrightarrow{AM}=\\)…' % en_w,
                vi='Cho hình lăng trụ tam giác \\(ABC.A′B′C′\\) với \\(\\overrightarrow{AA′}=\\vec a\\), \\(\\overrightarrow{AB}=\\vec b\\), \\(\\overrightarrow{AC}=\\vec c\\); %s. Khi đó \\(\\overrightarrow{AM}=\\)…' % vi_w,
                opts=fo(comb(co), [comb(x) for x in bads]), fig=Q3D(cfg, 'Prism'),
                ee='Go from \\(A\\) to \\(M\\) along the edges: \\(\\overrightarrow{AM}=%s\\).' % comb(co), ev='Đi từ \\(A\\) tới \\(M\\) theo các cạnh: \\(\\overrightarrow{AM}=%s\\).' % comb(co))

CL = [(('A', 'B'), ('A', 'D'), ('A', 'A′')), (('A', 'B'), ('A', 'D')), (('A', 'B'), ('B', 'C′')), (('A', 'C'), ('A', 'A′')), (('A', 'B'), ('A', 'D′')), (('A', 'C'), ('C′', 'A′'), ('A', 'B'))]
def v6_cube_len(r, lv, ctx):
    a = r.choice([2, 3, 4, 5])
    for _ in range(200):
        vs = r.choice(CL); sg = [1] + [r.choice([1, -1]) for _ in vs[1:]]
        tot = (0, 0, 0)
        for s, (p, q) in zip(sg, vs): tot = add(tot, mul(s, sub(CUBE1[q], CUBE1[p])))
        n = n2(tot)
        if n not in (0, 1) and n.denominator == 1: break
    else: raise AssertionError
    n = int(n); expr = ''.join(('' if i == 0 else ('+' if s > 0 else '-')) + vv(p, q) for i, (s, (p, q)) in enumerate(zip(sg, vs)))
    good = ksq(a, n)
    pool = [ksq(a, m) for m in (2, 3, 5, 6, 1, 4) if m != n] + [str(a * n)]
    used = set(x for pq in vs for x in pq)
    cfg = {'solid': True, 'points': {k: tuple(float(x) for x in v) for k, v in CUBE4.items()},
           'segments': [[p, q, {'color': '#c2410c', 'width': 3, 'arrow': True}] for p, q in vs], 'px': 250}
    return dict(en='\\(ABCD.A′B′C′D′\\) is a cube with edge \\(%d\\). Find \\(\\left|%s\\right|\\).' % (a, expr),
                vi='Cho hình lập phương \\(ABCD.A′B′C′D′\\) cạnh \\(%d\\). Tính \\(\\left|%s\\right|\\).' % (a, expr),
                opts=fo(good, pool), fig=Q3D(cfg, 'Cube'),
                ee='With \\(\\overrightarrow{AB}\\), \\(\\overrightarrow{AD}\\), \\(\\overrightarrow{AA′}\\) as unit directions (length \\(%d\\)), the vector is \\(%d\\cdot%s\\), length \\(%d\\sqrt{%d}=%s\\).' % (a, a, V3(tot), a, n, good),
                ev='Lấy \\(\\overrightarrow{AB}\\), \\(\\overrightarrow{AD}\\), \\(\\overrightarrow{AA′}\\) làm ba hướng (độ dài \\(%d\\)), vectơ bằng \\(%d\\cdot%s\\), độ dài \\(%d\\sqrt{%d}=%s\\).' % (a, a, V3(tot), a, n, good))

def v6_work(r, lv, ctx):
    Fm = r.choice([50, 80, 100, 120, 150, 200]); d = r.choice([5, 10, 12, 20, 25]); ang, cs = r.choice([(60, F(1, 2)), (0, F(1)), (90, F(0)), (120, F(-1, 2))]) if lv > 1 else (60, F(1, 2))
    W = Fm * d * cs
    return dict(en='A force \\(\\vec F\\) of \\(%d\\) N pulls a sled along a straight road for \\(%d\\) m. The angle between \\(\\vec F\\) and the displacement is \\(%d^\\circ\\). The work \\(A=\\vec F\\cdot\\vec d\\) (J) is…' % (Fm, d, ang),
                vi='Một lực \\(\\vec F\\) có độ lớn \\(%d\\) N kéo xe trượt đi \\(%d\\) m trên đường thẳng. Góc giữa \\(\\vec F\\) và độ dời là \\(%d^\\circ\\). Công \\(A=\\vec F\\cdot\\vec d\\) (J) bằng…' % (Fm, d, ang),
                opts=nopts(r, W, [Fm * d, Fm * d // 2 if W != Fm * d // 2 else -Fm * d // 2, -W if W else Fm, Fm + d]),
                ee='\\(A=|\\vec F|\\cdot|\\vec d|\\cos%d^\\circ=%d\\cdot%d\\cdot%s=%d\\).' % (ang, Fm, d, frt(cs), W), ev='\\(A=|\\vec F|\\cdot|\\vec d|\\cos%d^\\circ=%d\\cdot%d\\cdot%s=%d\\).' % (ang, Fm, d, frt(cs), W))

TP = {k: (F(v[0]), F(v[1]), F(v[2])) for k, v in TETF.items()}
TP['M'] = tuple((x + y) / 2 for x, y in zip(TP['A'], TP['B'])); TP['N'] = tuple((x + y) / 2 for x, y in zip(TP['C'], TP['D']))
TP['I'] = tuple((x + y) / 2 for x, y in zip(TP['M'], TP['N']))
def VEC(p, q): return sub(TP[q], TP[p])
STM = [('\\overrightarrow{IA}+\\overrightarrow{IB}+\\overrightarrow{IC}+\\overrightarrow{ID}=\\vec 0', lambda: add(add(VEC('I', 'A'), VEC('I', 'B')), add(VEC('I', 'C'), VEC('I', 'D'))), lambda: (0, 0, 0)),
       ('\\overrightarrow{MN}=\\dfrac12\\left(\\overrightarrow{AD}+\\overrightarrow{BC}\\right)', lambda: VEC('M', 'N'), lambda: mul(F(1, 2), add(VEC('A', 'D'), VEC('B', 'C')))),
       ('\\overrightarrow{MN}=\\dfrac12\\left(\\overrightarrow{AC}+\\overrightarrow{BD}\\right)', lambda: VEC('M', 'N'), lambda: mul(F(1, 2), add(VEC('A', 'C'), VEC('B', 'D')))),
       ('\\overrightarrow{IM}+\\overrightarrow{IN}=\\vec 0', lambda: add(VEC('I', 'M'), VEC('I', 'N')), lambda: (0, 0, 0)),
       ('\\overrightarrow{MN}=\\overrightarrow{AC}+\\overrightarrow{BD}', lambda: VEC('M', 'N'), lambda: add(VEC('A', 'C'), VEC('B', 'D'))),
       ('\\overrightarrow{IA}+\\overrightarrow{IB}=\\overrightarrow{IC}+\\overrightarrow{ID}', lambda: add(VEC('I', 'A'), VEC('I', 'B')), lambda: add(VEC('I', 'C'), VEC('I', 'D'))),
       ('\\overrightarrow{AB}+\\overrightarrow{CD}=2\\overrightarrow{MN}', lambda: add(VEC('A', 'B'), VEC('C', 'D')), lambda: mul(2, VEC('M', 'N'))),
       ('\\overrightarrow{MN}=\\dfrac12\\left(\\overrightarrow{AB}+\\overrightarrow{CD}\\right)', lambda: VEC('M', 'N'), lambda: mul(F(1, 2), add(VEC('A', 'B'), VEC('C', 'D')))),
       ('\\overrightarrow{IA}+\\overrightarrow{IB}+\\overrightarrow{IC}+\\overrightarrow{ID}=2\\overrightarrow{MN}', lambda: add(add(VEC('I', 'A'), VEC('I', 'B')), add(VEC('I', 'C'), VEC('I', 'D'))), lambda: mul(2, VEC('M', 'N'))),
       ('\\overrightarrow{AM}=\\overrightarrow{NC}', lambda: VEC('A', 'M'), lambda: VEC('N', 'C'))]
def v6_statement(r, lv, ctx):
    tv = [s for s in STM if s[1]() == s[2]()]; fv = [s for s in STM if s[1]() != s[2]()]
    assert len(tv) == 4 and len(fv) == 6
    good = r.choice(tv); bads = r.sample(fv, 3)
    cfg = {'solid': ['A', 'B', 'C', 'D'], 'points': {k: tuple(float(x) for x in TP[k]) for k in 'ABCDMNI'}, 'segments': [['M', 'N', {'dash': False, 'color': '#c2410c', 'width': 2.5}]], 'px': 260}
    q_e, q_v = V(lv, [('Which equality is true?', 'Đẳng thức nào đúng?'), ('Which of the following equalities holds?', 'Đẳng thức nào sau đây luôn đúng?'), ('Exactly one equality below is correct. Which one?', 'Chỉ có một đẳng thức đúng. Đó là đẳng thức nào?')])
    return dict(en='In the tetrahedron \\(ABCD\\), \\(M\\), \\(N\\) are the midpoints of \\(AB\\), \\(CD\\) and \\(I\\) is the midpoint of \\(MN\\). ' + q_e,
                vi='Cho tứ diện \\(ABCD\\); \\(M\\), \\(N\\) là trung điểm của \\(AB\\), \\(CD\\) và \\(I\\) là trung điểm của \\(MN\\). ' + q_v,
                opts=[good[0]] + [b[0] for b in bads], fig=Q3D(cfg, 'Tetrahedron'),
                ee='Use midpoints: \\(\\overrightarrow{IA}+\\overrightarrow{IB}=2\\overrightarrow{IM}\\), \\(\\overrightarrow{IC}+\\overrightarrow{ID}=2\\overrightarrow{IN}\\), \\(\\overrightarrow{IM}+\\overrightarrow{IN}=\\vec0\\); \\(2\\overrightarrow{MN}=\\overrightarrow{AD}+\\overrightarrow{BC}=\\overrightarrow{AC}+\\overrightarrow{BD}\\). Only \\(%s\\) is among the true ones.' % good[0],
                ev='Dùng trung điểm: \\(\\overrightarrow{IA}+\\overrightarrow{IB}=2\\overrightarrow{IM}\\), \\(\\overrightarrow{IC}+\\overrightarrow{ID}=2\\overrightarrow{IN}\\), \\(\\overrightarrow{IM}+\\overrightarrow{IN}=\\vec0\\); \\(2\\overrightarrow{MN}=\\overrightarrow{AD}+\\overrightarrow{BC}=\\overrightarrow{AC}+\\overrightarrow{BD}\\). Trong các phương án chỉ \\(%s\\) đúng.' % good[0])

LAMP = [(5, 4, 3), (13, 12, 5), (5, 3, 4), (10, 8, 6)]   # dây L, chiều cao h, nửa đường chéo đáy
def v6_lamp(r, lv, ctx):
    L, h, e = r.choice(LAMP); assert L * L == h * h + e * e
    k = r.choice([1, 2, 3]); P = 4 * h * k; T = F(P * L, 4 * h); assert T == L * k
    s = e / math.sqrt(2)
    pts = {'A': (-s, -s, 0), 'B': (s, -s, 0), 'C': (s, s, 0), 'D': (-s, s, 0), 'S': (0, 0, float(h))}
    cfg = {'solid': ['S', 'A', 'B', 'C', 'D'], 'points': pts, 'segments': [['S', 'A', {'color': '#c2410c', 'width': 3, 'arrow': True}]], 'px': 240}
    return dict(en='A square lamp \\(ABCD\\) weighing \\(%d\\) N hangs from a hook \\(S\\) by four equal chains \\(SA, SB, SC, SD\\), each \\(%d\\) dm long; \\(S\\) is \\(%d\\) dm above the lamp (see the figure). The tension in each chain (N) is…' % (P, L, h),
                vi='Một chiếc đèn hình vuông \\(ABCD\\) nặng \\(%d\\) N được treo vào móc \\(S\\) bằng bốn sợi xích bằng nhau \\(SA, SB, SC, SD\\), mỗi sợi dài \\(%d\\) dm; \\(S\\) cao hơn mặt đèn \\(%d\\) dm (xem hình). Lực căng của mỗi sợi xích (N) là…' % (P, L, h),
                opts=nopts(r, T, [F(P, 4), F(P * h, 4 * L), F(P * L, h), T + k]), fig=Q3D(cfg, 'Lamp'),
                ee='The vertical parts of the four tensions balance the weight: \\(4T\\cos\\alpha=%d\\) with \\(\\cos\\alpha=\\dfrac{%d}{%d}\\), so \\(T=%s\\).' % (P, h, L, ne(T)),
                ev='Thành phần thẳng đứng của bốn lực căng cân bằng trọng lực: \\(4T\\cos\\alpha=%d\\) với \\(\\cos\\alpha=\\dfrac{%d}{%d}\\), nên \\(T=%s\\).' % (P, h, L, nv(T)))

def v6_angle_dot(r, lv, ctx):
    a, b = r.choice([(2, 3), (3, 4), (2, 5), (4, 5), (3, 6), (2, 4)]); ang, cs = r.choice([(60, F(1, 2)), (120, F(-1, 2)), (90, F(0)), (180, F(-1))] if lv > 1 else [(60, F(1, 2)), (120, F(-1, 2))])
    d = a * b * cs
    return dict(en='\\(|\\vec a|=%d\\), \\(|\\vec b|=%d\\) and \\(\\vec a\\cdot\\vec b=%s\\). The angle between \\(\\vec a\\) and \\(\\vec b\\) is…' % (a, b, frt(d)),
                vi='Cho \\(|\\vec a|=%d\\), \\(|\\vec b|=%d\\) và \\(\\vec a\\cdot\\vec b=%s\\). Góc giữa hai vectơ \\(\\vec a\\) và \\(\\vec b\\) bằng…' % (a, b, frt(d)),
                opts=['%d^\\circ' % ang] + ['%d^\\circ' % x for x in ([180 - ang, 30, 150] if ang not in (90, 180) else [60, 120, 0 if ang == 180 else 45])],
                ee='\\(\\cos(\\vec a,\\vec b)=\\dfrac{%s}{%d\\cdot%d}=%s\\), so the angle is \\(%d^\\circ\\).' % (frt(d), a, b, frt(cs), ang),
                ev='\\(\\cos(\\vec a,\\vec b)=\\dfrac{%s}{%d\\cdot%d}=%s\\), nên góc bằng \\(%d^\\circ\\).' % (frt(d), a, b, frt(cs), ang))

D6 = [v6_cube_angle, v6_centroid, v6_prism, v6_cube_len, v6_work, v6_statement, v6_lamp, v6_angle_dot]

# =============================================================== Bài 7 – Hệ trục tọa độ trong không gian
def boxcfg(a, b, c, extra=None, segs=(), px=300):
    P = {'O': (0, 0, 0), 'A': (a, 0, 0), 'C': (0, b, 0), 'B': (a, b, 0), 'O′': (0, 0, c), 'A′': (a, 0, c), 'C′': (0, b, c), 'B′': (a, b, c)}
    P.update(extra or {})
    return {'proj': 'oxyz', 'axes': True, 'solid': ['O', 'A', 'B', 'C', 'O′', 'A′', 'B′', 'C′'], 'box': [[-1, a + 1], [-1, b + 1], [-1, c + 1]],
            'points': {k: tuple(float(x) for x in v) for k, v in P.items()}, 'segments': [list(s) for s in segs], 'px': px}

def c7_box(r, lv, ctx):
    a, b, c = r.sample([2, 3, 4, 5], 3); tgt = r.choice(['B′', 'C′', 'A′', 'B'])
    P = {'B′': (a, b, c), 'C′': (0, b, c), 'A′': (a, 0, c), 'B': (a, b, 0)}[tgt]
    bads = [(b, a, c), (a, b, 0) if tgt != 'B' else (a, b, c), (P[0], P[2], P[1]), (c, b, a), (0, b, c) if tgt != 'C′' else (a, 0, c)]
    return dict(en='The rectangular box \\(OABC.O′A′B′C′\\) has \\(O\\) at the origin, \\(A\\) on \\(Ox\\), \\(C\\) on \\(Oy\\), \\(O′\\) on \\(Oz\\), with \\(OA=%d\\), \\(OC=%d\\), \\(OO′=%d\\) (see the figure). The coordinates of \\(%s\\) are…' % (a, b, c, tgt),
                vi='Hình hộp chữ nhật \\(OABC.O′A′B′C′\\) có \\(O\\) là gốc tọa độ, \\(A\\) thuộc \\(Ox\\), \\(C\\) thuộc \\(Oy\\), \\(O′\\) thuộc \\(Oz\\), với \\(OA=%d\\), \\(OC=%d\\), \\(OO′=%d\\) (xem hình). Tọa độ của \\(%s\\) là…' % (a, b, c, tgt),
                opts=fo(V3(P), [V3(x) for x in bads]), fig=Q3D(boxcfg(a, b, c), 'Box in Oxyz'),
                ee='\\(%s\\) is reached by going \\(%d\\) along \\(Ox\\), \\(%d\\) along \\(Oy\\), \\(%d\\) along \\(Oz\\): \\(%s%s\\).' % (tgt, P[0], P[1], P[2], tgt, V3(P)),
                ev='Từ \\(O\\) tới \\(%s\\): đi \\(%d\\) theo \\(Ox\\), \\(%d\\) theo \\(Oy\\), \\(%d\\) theo \\(Oz\\): \\(%s%s\\).' % (tgt, P[0], P[1], P[2], tgt, V3(P)))

def nz(r, lo=-7, hi=7):
    while True:
        x = r.randint(lo, hi)
        if x: return x
def c7_sym_plane(r, lv, ctx):
    M = (nz(r), nz(r), nz(r)); pl = r.choice(['Oxy', 'Oyz', 'Oxz'])
    img = {'Oxy': (M[0], M[1], -M[2]), 'Oyz': (-M[0], M[1], M[2]), 'Oxz': (M[0], -M[1], M[2])}
    oth = [img[p] for p in img if p != pl] + [tuple(-x for x in M)]
    return dict(en='The point symmetric to \\(M%s\\) with respect to the plane \\((%s)\\) is…' % (V3(M), pl), vi='Điểm đối xứng với \\(M%s\\) qua mặt phẳng \\((%s)\\) là…' % (V3(M), pl),
                opts=fo(V3(img[pl]), [V3(x) for x in oth]),
                ee='Reflecting in \\((%s)\\) changes only the sign of the coordinate along the axis perpendicular to it.' % pl, ev='Đối xứng qua \\((%s)\\) chỉ đổi dấu tọa độ ứng với trục vuông góc với mặt phẳng đó.' % pl)

PY = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 6, 10), (4, 3, 5), (12, 5, 13)]
def c7_dist_axis(r, lv, ctx):
    p, q, h = r.choice(PY); ax = r.choice(['Ox', 'Oy', 'Oz']); t = nz(r, -9, 9); sp = [r.choice([1, -1]), r.choice([1, -1])]
    M = {'Oz': (sp[0] * p, sp[1] * q, t), 'Ox': (t, sp[0] * p, sp[1] * q), 'Oy': (sp[0] * p, t, sp[1] * q)}[ax]
    full = p * p + q * q + t * t
    return dict(en='The distance from \\(M%s\\) to the axis \\(%s\\) is…' % (V3(M), ax), vi='Khoảng cách từ \\(M%s\\) đến trục \\(%s\\) bằng…' % (V3(M), ax),
                opts=fo(str(h), [str(abs(t)), sq(full), sq(t * t + p * p), sq(t * t + q * q)]),
                ee='The foot of the perpendicular on \\(%s\\) keeps only the \\(%s\\)-coordinate, so the distance is \\(\\sqrt{%d^2+%d^2}=%d\\).' % (ax, ax[1].lower(), p, q, h),
                ev='Hình chiếu của \\(M\\) trên \\(%s\\) chỉ giữ tọa độ \\(%s\\), nên khoảng cách là \\(\\sqrt{%d^2+%d^2}=%d\\).' % (ax, ax[1].lower(), p, q, h))

def ijk(v):
    out = ''
    for k, e in zip(v, ('\\vec i', '\\vec j', '\\vec k')):
        if k == 0: continue
        t = e if abs(k) == 1 else '%d%s' % (abs(k), e)
        out += ('-' if k < 0 else ('+' if out else '')) + t
    return out
def c7_ijk(r, lv, ctx):
    for _ in range(100):
        v = [nz(r, -6, 6), nz(r, -6, 6), nz(r, -6, 6)]; v[r.randrange(3)] = 0; v = tuple(v)
        if len(set(v)) == 3: break
    nzv = [x for x in v if x]
    bads = [tuple(nzv + [0]), (0,) + tuple(nzv), (v[1], v[0], v[2]), tuple(-x for x in v), (v[0], v[2], v[1])]
    bads = [b for b in bads if b != v]
    return dict(en='In \\(Oxyz\\), \\(\\overrightarrow{OM}=%s\\). The coordinates of \\(M\\) are…' % ijk(v), vi='Trong không gian \\(Oxyz\\), \\(\\overrightarrow{OM}=%s\\). Tọa độ điểm \\(M\\) là…' % ijk(v),
                opts=fo(V3(v), [V3(b) for b in bads]),
                ee='\\(\\overrightarrow{OM}=x\\vec i+y\\vec j+z\\vec k\\Leftrightarrow M(x;y;z)\\); a missing vector means coordinate 0: \\(M%s\\).' % V3(v),
                ev='\\(\\overrightarrow{OM}=x\\vec i+y\\vec j+z\\vec k\\Leftrightarrow M(x;y;z)\\); vectơ đơn vị không có mặt ứng với tọa độ 0: \\(M%s\\).' % V3(v))

def c7_on_axis(r, lv, ctx):
    ax = r.choice([0, 1, 2]); nm = 'xyz'[ax]
    for _ in range(500):
        A = tuple(r.randint(-5, 5) for _ in range(3)); B = tuple(r.randint(-5, 5) for _ in range(3))
        if A[ax] == B[ax]: continue
        num = n2(B) - n2(A); den = 2 * (B[ax] - A[ax])
        if num % den == 0 and num // den != 0 and abs(num // den) <= 9: t = num // den; break
    else: raise AssertionError
    P = [0, 0, 0]; P[ax] = t
    assert n2(sub(P, A)) == n2(sub(P, B))
    lab = 'O%s' % nm
    return dict(en='Find the point \\(M\\) on the axis \\(%s\\) that is equidistant from \\(A%s\\) and \\(B%s\\).' % (lab, V3(A), V3(B)),
                vi='Tìm điểm \\(M\\) thuộc trục \\(%s\\) cách đều hai điểm \\(A%s\\) và \\(B%s\\).' % (lab, V3(A), V3(B)),
                opts=fo(V3(P), [V3(tuple(-t if i == ax else 0 for i in range(3))), V3(tuple(t if i == (ax + 1) % 3 else 0 for i in range(3))), V3(tuple(F(A[i] + B[i], 2) if i == ax else 0 for i in range(3))), V3(tuple(t + 1 if i == ax else 0 for i in range(3)))]),
                ee='\\(M\\) has only the \\(%s\\)-coordinate \\(t\\). \\(MA^2=MB^2\\) gives a linear equation in \\(t\\): \\(t=%d\\).' % (nm, t),
                ev='\\(M\\) chỉ có tọa độ \\(%s=t\\). Từ \\(MA^2=MB^2\\) được phương trình bậc nhất ẩn \\(t\\): \\(t=%d\\).' % (nm, t))

ROOMS = [(2, 3, 6, 7), (1, 4, 8, 9), (2, 6, 9, 11), (4, 4, 7, 9), (6, 6, 7, 11), (3, 4, 12, 13), (2, 10, 11, 15), (4, 8, 8, 12)]
def c7_room(r, lv, ctx):
    a, b, c, d = r.choice(ROOMS); assert a * a + b * b + c * c == d * d
    L, W_, H_ = r.sample([a, b, c], 3)
    if H_ > 6: L, H_ = H_, L
    if H_ > 6: W_, H_ = H_, W_
    return dict(en='A room is a rectangular box \\(%d\\) m long (along \\(Ox\\)), \\(%d\\) m wide (along \\(Oy\\)) and \\(%d\\) m high (along \\(Oz\\)), with a floor corner at \\(O\\). A cable is stretched from \\(O\\) to the opposite corner of the ceiling. How long is the cable (m)?' % (L, W_, H_),
                vi='Một căn phòng dạng hình hộp chữ nhật dài \\(%d\\) m (theo \\(Ox\\)), rộng \\(%d\\) m (theo \\(Oy\\)), cao \\(%d\\) m (theo \\(Oz\\)), một góc sàn ở \\(O\\). Người ta căng một sợi dây từ \\(O\\) đến góc đối diện trên trần. Sợi dây dài bao nhiêu mét?' % (L, W_, H_),
                opts=nopts(r, d, [L + W_ + H_, math.isqrt(L * L + W_ * W_) if isq(L * L + W_ * W_) else d + 1, d - 1, d + 2]),
                ee='The opposite ceiling corner is \\(%s\\), so the length is \\(\\sqrt{%d^2+%d^2+%d^2}=%d\\).' % (V3((L, W_, H_)), L, W_, H_, d),
                ev='Góc trần đối diện là \\(%s\\), nên độ dài là \\(\\sqrt{%d^2+%d^2+%d^2}=%d\\).' % (V3((L, W_, H_)), L, W_, H_, d))

def c7_right(r, lv, ctx):
    for _ in range(2000):
        P = tuple(r.randint(-3, 4) for _ in range(3)); u = tuple(r.randint(-3, 3) for _ in range(3)); w = tuple(r.randint(-3, 3) for _ in range(3))
        if n2(u) == 0 or n2(w) == 0 or dot(u, w) != 0 or n2(u) == n2(w): continue
        vtx = r.choice('ABC'); Q, R_ = add(P, u), add(P, w)
        pts = {'A': None, 'B': None, 'C': None}; others = [c for c in 'ABC' if c != vtx]
        pts[vtx] = P; pts[others[0]] = Q; pts[others[1]] = R_
        break
    else: raise AssertionError
    for c in 'ABC':
        o = [x for x in 'ABC' if x != c]
        if c != vtx: assert dot(sub(pts[o[0]], pts[c]), sub(pts[o[1]], pts[c])) != 0
    return dict(en='\\(A%s\\), \\(B%s\\), \\(C%s\\). Triangle \\(ABC\\)…' % (V3(pts['A']), V3(pts['B']), V3(pts['C'])),
                vi='Cho \\(A%s\\), \\(B%s\\), \\(C%s\\). Tam giác \\(ABC\\)…' % (V3(pts['A']), V3(pts['B']), V3(pts['C'])),
                opts=[tx('has a right angle at \\(%s\\)' % c, 'vuông tại \\(%s\\)' % c) for c in [vtx] + others] + [tx('has no right angle', 'không có góc vuông')],
                ee='\\(\\overrightarrow{%s%s}\\cdot\\overrightarrow{%s%s}=0\\), so the right angle is at \\(%s\\).' % (vtx, others[0], vtx, others[1], vtx),
                ev='\\(\\overrightarrow{%s%s}\\cdot\\overrightarrow{%s%s}=0\\), nên tam giác vuông tại \\(%s\\).' % (vtx, others[0], vtx, others[1], vtx))

def c7_divide(r, lv, ctx):
    k = r.choice([2, 3, F(1, 2)])
    for _ in range(500):
        A = tuple(r.randint(-6, 6) for _ in range(3)); B = tuple(r.randint(-6, 6) for _ in range(3))
        Mp = tuple((a + k * b) / (1 + k) for a, b in zip(A, B))
        if A != B and all(F(x).denominator == 1 for x in Mp) and Mp != A: break
    else: raise AssertionError
    assert sub(Mp, A) == mul(k, sub(B, Mp))
    alt = tuple((k * a + b) / (1 + k) for a, b in zip(A, B)); mid = tuple(F(a + b, 2) for a, b in zip(A, B)); ext_ = tuple(a + k * (b - a) for a, b in zip(A, B))
    ks = frt(k)
    return dict(en='\\(A%s\\), \\(B%s\\). \\(M\\) lies on segment \\(AB\\) with \\(MA=%s\\,MB\\). The coordinates of \\(M\\) are…' % (V3(A), V3(B), ks),
                vi='Cho \\(A%s\\), \\(B%s\\). Điểm \\(M\\) thuộc đoạn \\(AB\\) sao cho \\(MA=%s\\,MB\\). Tọa độ của \\(M\\) là…' % (V3(A), V3(B), ks),
                opts=fo(V3(Mp), [V3(alt), V3(mid), V3(ext_), V3(tuple(x + 1 for x in Mp))]),
                ee='\\(\\overrightarrow{AM}=%s\\overrightarrow{MB}\\Rightarrow M=\\dfrac{A+%s B}{1+%s}=%s\\).' % (ks, ks, ks, V3(Mp)),
                ev='\\(\\overrightarrow{AM}=%s\\overrightarrow{MB}\\Rightarrow M=\\dfrac{A+%s B}{1+%s}=%s\\).' % (ks, ks, ks, V3(Mp)))

D7 = [c7_box, c7_sym_plane, c7_dist_axis, c7_ijk, c7_on_axis, c7_room, c7_right, c7_divide]

# =============================================================== Bài 8 – Biểu thức tọa độ của các phép toán vectơ
def c8_angle(r, lv, ctx):
    for _ in range(5000):
        a = tuple(r.randint(-3, 3) for _ in range(3)); b = tuple(r.randint(-3, 3) for _ in range(3))
        if not n2(a) or not n2(b) or len([x for x in a if x]) < 2: continue
        d = dot(a, b); cs = F(d * d, n2(a) * n2(b))
        if cs in (F(1, 4), F(1, 2)) and (lv == 1 or d < 0 or r.random() < .4): break
    else: raise AssertionError
    ang = NICE[cs][0] if d > 0 else NICE[cs][1]
    return dict(en='The angle between \\(\\vec a=%s\\) and \\(\\vec b=%s\\) is…' % (V3(a), V3(b)), vi='Góc giữa hai vectơ \\(\\vec a=%s\\) và \\(\\vec b=%s\\) bằng…' % (V3(a), V3(b)),
                opts=['%d^\\circ' % ang, '%d^\\circ' % (180 - ang), '%d^\\circ' % ({60: 45, 120: 135, 45: 60, 135: 120}[ang]), '%d^\\circ' % ({60: 30, 120: 150, 45: 30, 135: 150}[ang])],
                ee='\\(\\cos=\\dfrac{%d}{\\sqrt{%d}\\cdot\\sqrt{%d}}\\), whose square is \\(%s\\); the angle is \\(%d^\\circ\\).' % (d, n2(a), n2(b), frt(cs), ang),
                ev='\\(\\cos=\\dfrac{%d}{\\sqrt{%d}\\cdot\\sqrt{%d}}\\), bình phương bằng \\(%s\\); góc bằng \\(%d^\\circ\\).' % (d, n2(a), n2(b), frt(cs), ang))

def c8_box(r, lv, ctx):
    a, b, c = r.sample([2, 3, 4], 3)
    P = {'O': (0, 0, 0), 'A': (a, 0, 0), 'C': (0, b, 0), 'B': (a, b, 0), 'O′': (0, 0, c), 'A′': (a, 0, c), 'C′': (0, b, c), 'B′': (a, b, c)}
    pairs = [('O', 'B′', 'A', 'C'), ('O', 'B′', 'A', 'C′'), ('A', 'C′', 'O', 'B′'), ('O', 'B′', 'C', 'A′'), ('A′', 'C', 'O', 'B'), ('O′', 'B', 'A', 'C′')]
    p, q, s, t = r.choice(pairs); u, w = sub(P[q], P[p]), sub(P[t], P[s]); d = dot(u, w)
    if d == 0: raise AssertionError
    segs = [(p, q, {'color': '#c2410c', 'width': 3, 'arrow': True}), (s, t, {'color': '#1d4ed8', 'width': 3, 'arrow': True})]
    return dict(en='The rectangular box \\(OABC.O′A′B′C′\\) has \\(O\\) at the origin and \\(B′%s\\) (see the figure). Then \\(\\overrightarrow{%s}\\cdot\\overrightarrow{%s}=\\)…' % (V3((a, b, c)), p + q, s + t),
                vi='Hình hộp chữ nhật \\(OABC.O′A′B′C′\\) có \\(O\\) là gốc tọa độ và \\(B′%s\\) (xem hình). Khi đó \\(\\overrightarrow{%s}\\cdot\\overrightarrow{%s}=\\)…' % (V3((a, b, c)), p + q, s + t),
                opts=nopts(r, d, [-d, a * a + b * b + c * c, d + 2, abs(a * a - b * b) + c * c]), fig=Q3D(boxcfg(a, b, c, segs=segs), 'Box'),
                ee='\\(\\overrightarrow{%s}=%s\\), \\(\\overrightarrow{%s}=%s\\), dot product \\(%d\\).' % (p + q, V3(u), s + t, V3(w), d),
                ev='\\(\\overrightarrow{%s}=%s\\), \\(\\overrightarrow{%s}=%s\\), tích vô hướng bằng \\(%d\\).' % (p + q, V3(u), s + t, V3(w), d))

QUAD = [(1, 2, 2, 3), (2, 3, 6, 7), (1, 4, 8, 9), (2, 6, 9, 11), (4, 4, 7, 9), (2, 10, 11, 15), (6, 6, 7, 11), (3, 4, 12, 13)]
def c8_find_m(r, lv, ctx):
    q = list(r.choice(QUAD)); n = q.pop(); r.shuffle(q); m = q[0]; y, z = q[1] * r.choice([1, -1]), q[2] * r.choice([1, -1])
    return dict(en='\\(\\vec a=(m;%d;%d)\\) with \\(m\\gt0\\) and \\(|\\vec a|=%d\\). Then \\(m=\\)…' % (y, z, n), vi='Cho \\(\\vec a=(m;%d;%d)\\) với \\(m\\gt0\\) và \\(|\\vec a|=%d\\). Khi đó \\(m=\\)…' % (y, z, n),
                opts=nopts(r, m, [n - abs(y) - abs(z) if n - abs(y) - abs(z) != m else m + 2, m * m, n, m + 1]),
                ee='\\(m^2+%d+%d=%d\\Rightarrow m^2=%d\\Rightarrow m=%d\\).' % (y * y, z * z, n * n, m * m, m), ev='\\(m^2+%d+%d=%d\\Rightarrow m^2=%d\\Rightarrow m=%d\\).' % (y * y, z * z, n * n, m * m, m))

def c8_opposite(r, lv, ctx):
    q = list(r.choice(QUAD)); n = q.pop(); a = tuple(x * r.choice([1, -1]) for x in r.sample(q, 3)); k = r.choice([2, 3]) if lv > 1 else r.choice([1, 2])
    b = mul(-k, a)
    return dict(en='\\(\\vec b\\) has the opposite direction to \\(\\vec a=%s\\) and \\(|\\vec b|=%d\\). Then \\(\\vec b=\\)…' % (V3(a), k * n),
                vi='Vectơ \\(\\vec b\\) ngược hướng với \\(\\vec a=%s\\) và \\(|\\vec b|=%d\\). Khi đó \\(\\vec b=\\)…' % (V3(a), k * n),
                opts=fo(V3(b), [V3(mul(k, a)), V3(mul(-k * n, a)), V3(mul(-1, a)) if k != 1 else V3(mul(-2, a)), V3(mul(k * n, a))]),
                ee='\\(|\\vec a|=%d\\), so \\(\\vec b=-%s\\vec a=%s\\).' % (n, '' if k == 1 else str(k), V3(b)), ev='\\(|\\vec a|=%d\\), nên \\(\\vec b=-%s\\vec a=%s\\).' % (n, '' if k == 1 else str(k), V3(b)))

def c8_obtuse(r, lv, ctx):
    for _ in range(2000):
        p, q, s = nz(r, -3, 3), nz(r, -3, 3), nz(r, -3, 3); a0, a2 = nz(r, -3, 3), nz(r, -3, 3)
        c0 = p * a0 + s * a2                 # a=(a0; m; a2), b=(p; q; s): a·b = c0 + q m
        if c0 % q: continue
        t = -F(c0, q)
        if F(a0, p) == F(a2, s): continue     # tránh trường hợp có thể cùng phương
        break
    else: raise AssertionError
    good = 'm\\lt %s' % frt(t) if q > 0 else 'm\\gt %s' % frt(t)
    bad = ['m\\gt %s' % frt(t) if q > 0 else 'm\\lt %s' % frt(t), 'm\\lt %s' % frt(-t) if q > 0 else 'm\\gt %s' % frt(-t), 'm=%s' % frt(t)]
    if t == 0: bad[1] = 'm\\ne0'
    return dict(en='\\(\\vec a=(%d;m;%d)\\), \\(\\vec b=%s\\). The angle between \\(\\vec a\\) and \\(\\vec b\\) is obtuse exactly when…' % (a0, a2, V3((p, q, s))),
                vi='Cho \\(\\vec a=(%d;m;%d)\\), \\(\\vec b=%s\\). Góc giữa \\(\\vec a\\) và \\(\\vec b\\) là góc tù khi và chỉ khi…' % (a0, a2, V3((p, q, s))),
                opts=[good] + bad,
                ee='Obtuse \\(\\Leftrightarrow\\vec a\\cdot\\vec b\\lt0\\) (the vectors are never collinear here): \\(%d%sm\\lt0\\Leftrightarrow %s\\).' % (c0, ('+%d' % q) if q > 0 else str(q), good),
                ev='Góc tù \\(\\Leftrightarrow\\vec a\\cdot\\vec b\\lt0\\) (ở đây hai vectơ không thể cùng phương): \\(%d%sm\\lt0\\Leftrightarrow %s\\).' % (c0, ('+%d' % q) if q > 0 else str(q), good))

def c8_system(r, lv, ctx):
    a = tuple(r.randint(-5, 5) for _ in range(3)); b = tuple(r.randint(-5, 5) for _ in range(3))
    if a == b or not n2(b): raise AssertionError
    u, w = add(a, b), sub(a, b); ask = r.choice(['a', 'b']); good = a if ask == 'a' else b
    return dict(en='\\(\\vec a+\\vec b=%s\\) and \\(\\vec a-\\vec b=%s\\). Then \\(\\vec %s=\\)…' % (V3(u), V3(w), ask), vi='Cho \\(\\vec a+\\vec b=%s\\) và \\(\\vec a-\\vec b=%s\\). Khi đó \\(\\vec %s=\\)…' % (V3(u), V3(w), ask),
                opts=fo(V3(good), [V3(b if ask == 'a' else a), V3(u), V3(w), V3(tuple(-x for x in good))]),
                ee='Add or subtract the two equalities: \\(\\vec a=\\dfrac{%s+%s}{2}=%s\\), \\(\\vec b=%s\\).' % (V3(u), V3(w), V3(a), V3(b)),
                ev='Cộng hoặc trừ hai đẳng thức: \\(\\vec a=\\dfrac{%s+%s}{2}=%s\\), \\(\\vec b=%s\\).' % (V3(u), V3(w), V3(a), V3(b)))

def c8_balance(r, lv, ctx):
    F1 = tuple(r.randint(-8, 8) for _ in range(3)); F2 = tuple(r.randint(-8, 8) for _ in range(3)); F3 = tuple(-x for x in add(F1, F2))
    if not n2(F3) or len(set(F3)) < 2: raise AssertionError
    return dict(en='A drone hovers still under three forces \\(\\vec F_1=%s\\), \\(\\vec F_2=%s\\) and \\(\\vec F_3\\) (newtons). Then \\(\\vec F_3=\\)…' % (V3(F1), V3(F2)),
                vi='Một drone đứng yên dưới tác dụng của ba lực \\(\\vec F_1=%s\\), \\(\\vec F_2=%s\\) và \\(\\vec F_3\\) (đơn vị N). Khi đó \\(\\vec F_3=\\)…' % (V3(F1), V3(F2)),
                opts=fo(V3(F3), [V3(add(F1, F2)), V3(sub(F1, F2)), V3(sub(F2, F1)), V3(tuple(-x for x in F1))]),
                ee='Standing still: \\(\\vec F_1+\\vec F_2+\\vec F_3=\\vec0\\Rightarrow\\vec F_3=-(\\vec F_1+\\vec F_2)=%s\\).' % V3(F3),
                ev='Đứng yên: \\(\\vec F_1+\\vec F_2+\\vec F_3=\\vec0\\Rightarrow\\vec F_3=-(\\vec F_1+\\vec F_2)=%s\\).' % V3(F3))

PQ = [(1, 2, 2), (2, 1, 2), (2, 2, 1), (2, 3, 6), (3, 6, 2), (6, 2, 3), (1, 4, 8), (4, 4, 7), (2, 6, 9)]
def c8_cos_tri(r, lv, ctx):
    for _ in range(500):
        u = tuple(x * r.choice([1, -1]) for x in r.choice(PQ)); w = tuple(x * r.choice([1, -1]) for x in r.choice(PQ))
        d = dot(u, w)
        if d != 0 and u != w and u != tuple(-x for x in w): break
    else: raise AssertionError
    A = tuple(r.randint(-3, 3) for _ in range(3)); B, C = add(A, u), add(A, w)
    nu, nw = math.isqrt(n2(u)), math.isqrt(n2(w)); cs = F(d, nu * nw)
    return dict(en='\\(A%s\\), \\(B%s\\), \\(C%s\\). Then \\(\\cos\\widehat{BAC}=\\)…' % (V3(A), V3(B), V3(C)), vi='Cho \\(A%s\\), \\(B%s\\), \\(C%s\\). Khi đó \\(\\cos\\widehat{BAC}=\\)…' % (V3(A), V3(B), V3(C)),
                opts=fo(cs, [-cs, F(d, nu * nu + nw * nw) if F(d, nu * nu + nw * nw) != cs else cs / 2, F(d, nu * nw * 2), F(nu, nw) if F(nu, nw) != cs else 1 - cs]),
                ee='\\(\\overrightarrow{AB}=%s\\), \\(\\overrightarrow{AC}=%s\\): \\(\\cos=\\dfrac{%d}{%d\\cdot%d}=%s\\).' % (V3(u), V3(w), d, nu, nw, frt(cs)),
                ev='\\(\\overrightarrow{AB}=%s\\), \\(\\overrightarrow{AC}=%s\\): \\(\\cos=\\dfrac{%d}{%d\\cdot%d}=%s\\).' % (V3(u), V3(w), d, nu, nw, frt(cs)))

D8 = [c8_angle, c8_box, c8_find_m, c8_opposite, c8_obtuse, c8_system, c8_balance, c8_cos_tri]

# =============================================================== Bài 11 – Nguyên hàm
def poly_tex(c2, c1, c0, v='x'):
    """c2 x² + c1 x + c0 (Fraction) → TeX."""
    out = ''
    for c, p in ((c2, 2), (c1, 1), (c0, 0)):
        c = F(c)
        if c == 0: continue
        mag = abs(c); body = ('' if mag == 1 and p else frt(mag)) + ({2: v + '^2', 1: v, 0: ''}[p])
        if p and mag != 1 and mag.denominator != 1: body = frt(mag) + {2: v + '^2', 1: v}[p]
        out += ('-' if c < 0 else ('+' if out else '')) + body
    return out or '0'
def i11_graph(r, lv, ctx):
    for _ in range(200):
        a = r.choice([1, 2, -1, -2, 3, F(1, 2), F(-1, 2)]); b = r.randint(-3, 3)
        x1, x2 = (0, 2) if F(a).denominator == 2 else (0, 1)
        if b != 0 and -4 <= a * 2 + b <= 5: break
    f = lambda x: float(a * x + b)
    img = G.graph_svg([(f, G.GREEN)], (-2.6, 3.6), (-4.6, 5.6), G.int_ticks(-2, 3), G.int_ticks(-4, 5), dots=[(x1, a * x1 + b, False), (x2, a * x2 + b, False)], W=5.5, H=5.6)
    good = poly_tex(F(a, 2), b, 0)
    pe, pv = V(lv, [('The figure shows the graph of the linear function \\(y=f(x)\\). Which function is an antiderivative of \\(f\\)?', 'Hình vẽ là đồ thị hàm số bậc nhất \\(y=f(x)\\). Hàm số nào là một nguyên hàm của \\(f\\)?'),
                    ('The line in the figure is the graph of \\(y=f(x)\\). Which of the following is an antiderivative of \\(f\\)?', 'Đường thẳng trong hình là đồ thị của \\(y=f(x)\\). Hàm số nào sau đây là một nguyên hàm của \\(f\\)?'),
                    ('Read \\(f(x)\\) from its graph (a straight line) in the figure. Which function \\(F\\) satisfies \\(F\'(x)=f(x)\\)?', 'Đọc \\(f(x)\\) từ đồ thị (một đường thẳng) trong hình. Hàm số \\(F\\) nào thỏa mãn \\(F\'(x)=f(x)\\)?')])
    return dict(en=pe, vi=pv,
                opts=fo('F(x)=' + good, ['F(x)=' + poly_tex(a, b, 0), 'F(x)=' + poly_tex(F(a, 2), -b, 0), 'F(x)=' + poly_tex(F(b, 2), a, 0), 'F(x)=' + poly_tex(0, a, b) if F(a, 2) != 0 else 'F(x)=x']), fig=G.FIG(img, 'Graph of f', 'Đồ thị của f', 300),
                ee='The line passes through \\((%d;%s)\\) and \\((%d;%s)\\), so \\(f(x)=%s\\) and \\(F(x)=%s+C\\).' % (x1, frt(a * x1 + b), x2, frt(a * x2 + b), poly_tex(0, a, b), good),
                ev='Đường thẳng đi qua \\((%d;%s)\\) và \\((%d;%s)\\), nên \\(f(x)=%s\\) và \\(F(x)=%s+C\\).' % (x1, frt(a * x1 + b), x2, frt(a * x2 + b), poly_tex(0, a, b), good))

def cf(k, body):
    k = F(k)
    if k == 1: return body
    if k == -1: return '-' + body
    return frt(k) + body if k.denominator == 1 else ('-' if k < 0 else '') + '\\dfrac{%d}{%d}%s' % (abs(k.numerator), k.denominator, body)
def i11_power(r, lv, ctx):
    k = r.choice([1, 2, 3, 4, 6]); t = r.choice(['sqrt', 'inv2', 'isqrt', 'xsqrt'])
    if t == 'sqrt': q, g, b = cf(k, '\\sqrt x'), cf(F(2 * k, 3), 'x\\sqrt x'), [cf(F(k, 2), '\\dfrac{1}{\\sqrt x}'), cf(F(3 * k, 2), 'x\\sqrt x'), cf(k, 'x\\sqrt x')]
    elif t == 'inv2': q, g, b = '\\dfrac{%d}{x^2}' % k, cf(-k, '\\dfrac{1}{x}'), [cf(k, '\\dfrac{1}{x}'), cf(-2 * k, '\\dfrac{1}{x^3}'), cf(k, '\\ln x^2')]
    elif t == 'isqrt': q, g, b = '\\dfrac{%d}{\\sqrt x}' % k, cf(2 * k, '\\sqrt x'), [cf(k, '\\sqrt x'), cf(F(k, 2), '\\sqrt x'), cf(F(-k, 2), '\\dfrac{1}{x\\sqrt x}')]
    else: q, g, b = cf(k, 'x\\sqrt x'), cf(F(2 * k, 5), 'x^2\\sqrt x'), [cf(F(3 * k, 2), '\\sqrt x'), cf(F(k, 2), 'x^2\\sqrt x'), cf(F(5 * k, 2), 'x^2\\sqrt x')]
    return dict(en='On \\((0;+\\infty)\\), \\(\\displaystyle\\int %s\\,dx=\\)…' % q, vi='Trên \\((0;+\\infty)\\), \\(\\displaystyle\\int %s\\,dx=\\)…' % q,
                opts=[g + '+C'] + [x + '+C' for x in b],
                ee='Write the integrand as a power \\(x^{\\alpha}\\) and use \\(\\displaystyle\\int x^{\\alpha}dx=\\dfrac{x^{\\alpha+1}}{\\alpha+1}+C\\): the result is \\(%s+C\\).' % g,
                ev='Viết hàm dưới dấu nguyên hàm dạng lũy thừa \\(x^{\\alpha}\\) rồi dùng \\(\\displaystyle\\int x^{\\alpha}dx=\\dfrac{x^{\\alpha+1}}{\\alpha+1}+C\\): kết quả \\(%s+C\\).' % g)

def i11_expbase(r, lv, ctx):
    t = r.choice(['a', 'ab', 'ka'])
    if t == 'a': a = r.choice([3, 5, 7]); q = '%d^x' % a; g = '\\dfrac{%d^x}{\\ln %d}' % (a, a); b = ['%d^x\\ln %d' % (a, a), '%d^x' % a, '\\dfrac{%d^{x+1}}{x+1}' % a]
    elif t == 'ab': a, c = r.choice([(2, 3), (2, 5), (3, 4)]); q = '%d^x\\cdot%d^x' % (a, c); g = '\\dfrac{%d^x}{\\ln %d}' % (a * c, a * c); b = ['%d^x\\ln %d' % (a * c, a * c), '\\dfrac{%d^x\\cdot%d^x}{\\ln %d\\cdot\\ln %d}' % (a, c, a, c), '\\dfrac{%d^{x+1}}{x+1}' % (a * c)]
    else: a = r.choice([2, 3]); k = r.choice([2, 3]); q = '%d^{%dx}' % (a, k); g = '\\dfrac{%d^{%dx}}{%d\\ln %d}' % (a, k, k, a); b = ['\\dfrac{%d^{%dx}}{\\ln %d}' % (a, k, a), '%d\\cdot%d^{%dx}\\ln %d' % (k, a, k, a), '\\dfrac{%d^{%dx+1}}{%dx+1}' % (a, k, k)]
    return dict(en='\\(\\displaystyle\\int %s\\,dx=\\)…' % q, vi='\\(\\displaystyle\\int %s\\,dx=\\)…' % q, opts=[g + '+C'] + [x + '+C' for x in b],
                ee='\\(\\displaystyle\\int a^x\\,dx=\\dfrac{a^x}{\\ln a}+C\\) (\\(0\\lt a\\ne1\\)); here the result is \\(%s+C\\).' % g, ev='\\(\\displaystyle\\int a^x\\,dx=\\dfrac{a^x}{\\ln a}+C\\) (\\(0\\lt a\\ne1\\)); ở đây kết quả là \\(%s+C\\).' % g)

TRIGI = [('\\tan^2x', '\\tan x-x', ['\\tan x+x', '\\dfrac{\\tan^3x}{3}', '\\tan x']), ('\\cot^2x', '-\\cot x-x', ['\\cot x-x', '-\\cot x+x', '\\dfrac{\\cot^3x}{3}']),
         ('\\dfrac{1}{\\cos^2x}', '\\tan x', ['-\\tan x', '\\cot x', '\\dfrac{1}{\\cos x}']), ('\\dfrac{1}{\\sin^2x}', '-\\cot x', ['\\cot x', '\\tan x', '-\\dfrac{1}{\\sin x}']),
         ('1+\\tan^2x', '\\tan x', ['x+\\tan x', '\\dfrac{\\tan^3x}{3}+x', '-\\cot x']), ('\\dfrac{2}{\\cos^2x}-1', '2\\tan x-x', ['2\\tan x+x', '-2\\tan x-x', '2\\cot x-x'])]
def i11_tan(r, lv, ctx):
    q, g, b = r.choice(TRIGI)
    return dict(en='\\(\\displaystyle\\int\\left(%s\\right)dx=\\)…' % q, vi='\\(\\displaystyle\\int\\left(%s\\right)dx=\\)…' % q, opts=[g + '+C'] + [x + '+C' for x in b],
                ee='Use \\(1+\\tan^2x=\\dfrac{1}{\\cos^2x}\\), \\(1+\\cot^2x=\\dfrac{1}{\\sin^2x}\\) and \\(\\displaystyle\\int\\dfrac{dx}{\\cos^2x}=\\tan x+C\\), \\(\\displaystyle\\int\\dfrac{dx}{\\sin^2x}=-\\cot x+C\\): the result is \\(%s+C\\).' % g,
                ev='Dùng \\(1+\\tan^2x=\\dfrac{1}{\\cos^2x}\\), \\(1+\\cot^2x=\\dfrac{1}{\\sin^2x}\\) và \\(\\displaystyle\\int\\dfrac{dx}{\\cos^2x}=\\tan x+C\\), \\(\\displaystyle\\int\\dfrac{dx}{\\sin^2x}=-\\cot x+C\\): kết quả \\(%s+C\\).' % g)

def i11_simplify(r, lv, ctx):
    if r.random() < .5:
        k = nz(r, -6, 6); m = r.choice([1, 2, 3])
        q = '\\dfrac{%s}{x}' % poly_tex(m, 0, k); g = poly_tex(F(m, 2), 0, 0) + ('+' if k > 0 else '-') + ('' if abs(k) == 1 else str(abs(k))) + '\\ln x'
        b = [poly_tex(F(m, 2), 0, 0) + ('+' if k < 0 else '-') + ('' if abs(k) == 1 else str(abs(k))) + '\\ln x', poly_tex(m, 0, 0) + ('+' if k > 0 else '-') + ('' if abs(k) == 1 else str(abs(k))) + '\\ln x',
             '\\dfrac{%s}{\\ln x}' % poly_tex(F(m, 3), 0, k).replace('x^2', 'x^3') if False else poly_tex(F(m, 2), 0, 0) + ('+' if k > 0 else '-') + '\\dfrac{%d}{x^2}' % abs(k)]
        ex = '\\dfrac{%s}{x}=%s%s\\dfrac{%d}{x}' % (poly_tex(m, 0, k), poly_tex(0, m, 0), '+' if k > 0 else '-', abs(k))
    else:
        p, s = nz(r, -4, 4), nz(r, -4, 4)
        if p + s == 0: raise AssertionError
        q = '(x%s)(x%s)' % (('+%d' % p) if p > 0 else str(p), ('+%d' % s) if s > 0 else str(s))
        c2, c1, c0 = 1, p + s, p * s
        g = '\\dfrac{x^3}{3}' + ('' if c1 == 0 else (('+' if c1 > 0 else '-') + cf(F(abs(c1), 2), 'x^2'))) + (('+' if c0 > 0 else '-') + cf(abs(c0), 'x'))
        b = ['\\dfrac{x^3}{3}' + (('+' if c0 > 0 else '-') + cf(abs(c0), 'x')), '\\dfrac{(x%s)^2}{2}\\cdot\\dfrac{(x%s)^2}{2}' % (('+%d' % p) if p > 0 else str(p), ('+%d' % s) if s > 0 else str(s)),
             'x^3' + ('' if c1 == 0 else (('+' if c1 > 0 else '-') + cf(abs(c1), 'x^2'))) + (('+' if c0 > 0 else '-') + cf(abs(c0), 'x'))]
        ex = '%s=%s' % (q, poly_tex(1, c1, c0))
    if lv == 1 and 'ln' in g: pass
    return dict(en='On \\((0;+\\infty)\\), \\(\\displaystyle\\int %s\\,dx=\\)…' % q, vi='Trên \\((0;+\\infty)\\), \\(\\displaystyle\\int %s\\,dx=\\)…' % q,
                opts=[g + '+C'] + [x + '+C' for x in b],
                ee='First simplify: \\(%s\\); then integrate term by term: \\(%s+C\\).' % (ex, g), ev='Biến đổi trước: \\(%s\\); rồi lấy nguyên hàm từng hạng tử: \\(%s+C\\).' % (ex, g))

def i11_tree(r, lv, ctx):
    k = r.choice([2, 3, 4, 5, 6]); h1 = r.choice([20, 30, 40, 50]); T = r.choice([4, 9, 16]); rt = math.isqrt(T)
    hT = h1 + 2 * k * (rt - 1)
    return dict(en='The height of a young tree grows at the rate \\(h\'(t)=\\dfrac{%d}{\\sqrt t}\\) (cm per year), \\(t\\ge1\\) in years. At \\(t=1\\) the tree is \\(%d\\) cm tall. How tall is it at \\(t=%d\\) (cm)?' % (k, h1, T),
                vi='Chiều cao của một cây non tăng với tốc độ \\(h\'(t)=\\dfrac{%d}{\\sqrt t}\\) (cm/năm), \\(t\\ge1\\) tính bằng năm. Khi \\(t=1\\) cây cao \\(%d\\) cm. Khi \\(t=%d\\) cây cao bao nhiêu cm?' % (k, h1, T),
                opts=nopts(r, hT, [h1 + k * (rt - 1), h1 + 2 * k * rt, h1 + F(k, rt), h1 + k * (T - 1)]),
                ee='\\(h(t)=%d\\sqrt t+C\\), \\(h(1)=%d\\Rightarrow C=%d\\); \\(h(%d)=%d\\cdot%d+%d=%d\\).' % (2 * k, h1, h1 - 2 * k, T, 2 * k, rt, h1 - 2 * k, hT),
                ev='\\(h(t)=%d\\sqrt t+C\\), \\(h(1)=%d\\Rightarrow C=%d\\); \\(h(%d)=%d\\cdot%d+%d=%d\\).' % (2 * k, h1, h1 - 2 * k, T, 2 * k, rt, h1 - 2 * k, hT))

def i11_second(r, lv, ctx):
    a = r.choice([6, 12, -6, 18]); b = r.choice([2, -2, 4, 0]); p = r.randint(-3, 3); q = r.randint(-3, 4)
    v = F(a, 6) + F(b, 2) + p + q
    ftex = poly_tex(0, a, b) if b else '%dx' % a
    return dict(en='\\(f\'\'(x)=%s\\), \\(f\'(0)=%d\\) and \\(f(0)=%d\\). Then \\(f(1)=\\)…' % (ftex, p, q), vi='Cho \\(f\'\'(x)=%s\\), \\(f\'(0)=%d\\) và \\(f(0)=%d\\). Khi đó \\(f(1)=\\)…' % (ftex, p, q),
                opts=nopts(r, v, [F(a, 2) + b + p + q, F(a, 6) + F(b, 2) + q, F(a, 6) + F(b, 2) + p, v + 1]),
                ee='\\(f\'(x)=%s+%d\\), \\(f(x)=%s+%d x+%d\\), so \\(f(1)=%s\\).' % (poly_tex(F(a, 2), b, 0), p, ('\\dfrac{%d}{6}x^3' % a) + (('+' if b > 0 else '-') + cf(F(abs(b), 2), 'x^2') if b else ''), p, q, ne(v)),
                ev='\\(f\'(x)=%s+%d\\), \\(f(x)=%s+%d x+%d\\), nên \\(f(1)=%s\\).' % (poly_tex(F(a, 2), b, 0), p, ('\\dfrac{%d}{6}x^3' % a) + (('+' if b > 0 else '-') + cf(F(abs(b), 2), 'x^2') if b else ''), p, q, nv(v)))

ST_T = [('\\displaystyle\\int kf(x)\\,dx=k\\int f(x)\\,dx\\) for every constant \\(k\\ne0', '\\displaystyle\\int kf(x)\\,dx=k\\int f(x)\\,dx\\) với mọi hằng số \\(k\\ne0'),
        ('\\displaystyle\\int f\'(x)\\,dx=f(x)+C', '\\displaystyle\\int f\'(x)\\,dx=f(x)+C'),
        ('if \\(F\\) is an antiderivative of \\(f\\), so is \\(F(x)+5', 'nếu \\(F\\) là một nguyên hàm của \\(f\\) thì \\(F(x)+5\\) cũng vậy'),
        ('\\displaystyle\\int\\left[f(x)+g(x)\\right]dx=\\int f(x)\\,dx+\\int g(x)\\,dx', '\\displaystyle\\int\\left[f(x)+g(x)\\right]dx=\\int f(x)\\,dx+\\int g(x)\\,dx')]
ST_F = [('\\displaystyle\\int f(x)g(x)\\,dx=\\int f(x)\\,dx\\cdot\\int g(x)\\,dx', '\\displaystyle\\int f(x)g(x)\\,dx=\\int f(x)\\,dx\\cdot\\int g(x)\\,dx'),
        ('\\displaystyle\\int\\sin x\\,dx=\\cos x+C', '\\displaystyle\\int\\sin x\\,dx=\\cos x+C'),
        ('\\displaystyle\\int e^{2x}\\,dx=e^{2x}+C', '\\displaystyle\\int e^{2x}\\,dx=e^{2x}+C'),
        ('\\displaystyle\\int x^{\\alpha}dx=\\dfrac{x^{\\alpha+1}}{\\alpha+1}+C\\) for every real \\(\\alpha', '\\displaystyle\\int x^{\\alpha}dx=\\dfrac{x^{\\alpha+1}}{\\alpha+1}+C\\) với mọi số thực \\(\\alpha'),
        ('\\displaystyle\\int\\dfrac{f(x)}{g(x)}\\,dx=\\dfrac{\\int f(x)\\,dx}{\\int g(x)\\,dx}', '\\displaystyle\\int\\dfrac{f(x)}{g(x)}\\,dx=\\dfrac{\\int f(x)\\,dx}{\\int g(x)\\,dx}'),
        ('\\displaystyle\\int\\cos 2x\\,dx=2\\sin 2x+C', '\\displaystyle\\int\\cos 2x\\,dx=2\\sin 2x+C')]
def i11_statement(r, lv, ctx):
    g = r.choice(ST_T); b = r.sample(ST_F, 3)
    W = lambda s: tx('\\(' + s[0] + '\\)', '\\(' + s[1] + '\\)')
    pe, pv = V(lv, [('Which statement is true (\\(f\\), \\(g\\) continuous)?', 'Khẳng định nào đúng (\\(f\\), \\(g\\) liên tục)?'), ('For continuous functions \\(f\\), \\(g\\), which property of antiderivatives is correct?', 'Với \\(f\\), \\(g\\) liên tục, tính chất nào của nguyên hàm là đúng?'), ('Exactly one of these statements is true (\\(f\\), \\(g\\) continuous). Which one?', 'Chỉ có một khẳng định đúng (\\(f\\), \\(g\\) liên tục). Đó là khẳng định nào?')])
    return dict(en=pe, vi=pv, opts=[W(g)] + [W(x) for x in b],
                ee='Only sums and constant multiples can be split; products and quotients cannot; \\(\\displaystyle\\int\\sin x\\,dx=-\\cos x+C\\), \\(\\displaystyle\\int e^{2x}dx=\\dfrac{e^{2x}}{2}+C\\), \\(\\displaystyle\\int\\cos 2x\\,dx=\\dfrac{\\sin 2x}{2}+C\\); the power rule needs \\(\\alpha\\ne-1\\).',
                ev='Chỉ tách được tổng và hằng số nhân; không tách được tích, thương; \\(\\displaystyle\\int\\sin x\\,dx=-\\cos x+C\\), \\(\\displaystyle\\int e^{2x}dx=\\dfrac{e^{2x}}{2}+C\\), \\(\\displaystyle\\int\\cos 2x\\,dx=\\dfrac{\\sin 2x}{2}+C\\); công thức lũy thừa cần \\(\\alpha\\ne-1\\).')

D11 = [i11_graph, i11_power, i11_expbase, i11_tan, i11_simplify, i11_tree, i11_second, i11_statement]

# =============================================================== Bài 12 – Tích phân
def i12_area(r, lv, ctx):
    for _ in range(500):
        n = r.choice([4, 5, 6]); ys = [r.randint(-2, 3) for _ in range(n + 1)]
        if lv == 1 and min(ys) < 0: continue
        if any(ys[i] * ys[i + 1] < 0 for i in range(n)): continue        # chỉ đổi dấu tại đỉnh lưới → mỗi đoạn là hình thang/tam giác
        if len(set(ys)) >= 3 and (lv == 1 or min(ys) < 0): break
    else: raise AssertionError
    I = sum(F(ys[i] + ys[i + 1], 2) for i in range(n))
    absI = sum(F(abs(ys[i]) + abs(ys[i + 1]), 2) for i in range(n))
    f = lambda x: (lambda i: ys[i] + (ys[i + 1] - ys[i]) * (x - i))(min(int(x), n - 1)) if 0 <= x <= n else None
    img = G.graph_svg([(f, G.GREEN)], (-.8, n + .7), (-2.7, 3.7), G.int_ticks(1, n), G.int_ticks(-2, 3), dots=[(i, ys[i], False) for i in range(n + 1)], W=6.2, H=4.4)
    return dict(en='The figure shows the graph of \\(y=f(x)\\) on \\([0;%d]\\) (a broken line through the marked points). Find \\(\\displaystyle\\int_0^{%d}f(x)\\,dx\\).' % (n, n),
                vi='Hình vẽ là đồ thị của \\(y=f(x)\\) trên \\([0;%d]\\) (đường gấp khúc qua các điểm được đánh dấu). Tính \\(\\displaystyle\\int_0^{%d}f(x)\\,dx\\).' % (n, n),
                opts=nopts(r, I, [absI if absI != I else I + 2, I + 1, I - 1, sum(ys)]), fig=G.FIG(img, 'Broken line graph', 'Đồ thị đường gấp khúc', 340),
                ee='Add the signed areas of the pieces between the graph and \\(Ox\\) (areas below \\(Ox\\) count as negative): \\(%s\\).' % ne(I),
                ev='Cộng diện tích có dấu của các mảnh giữa đồ thị và \\(Ox\\) (phần dưới \\(Ox\\) mang dấu âm): \\(%s\\).' % nv(I))

def i12_semicircle(r, lv, ctx):
    R = r.choice([2, 3, 4]); half = r.random() < .5
    f = lambda x: math.sqrt(max(R * R - x * x, 0)) if abs(x) <= R else None
    W_ = 5.6; img = G.graph_svg([(f, G.GREEN)], (-1.25 * R, 1.25 * R), (-.25 * R, 1.25 * R), G.int_ticks(-R, R), G.int_ticks(1, R - 1), W=W_, H=W_ * 1.5 / 2.5)
    lo = 0 if half else -R; good = F(R * R, 4 if half else 2)
    gt = '\\dfrac{%d\\pi}{%d}' % (good.numerator, good.denominator) if good.denominator != 1 else '%d\\pi' % good.numerator
    if good.numerator == 1 and good.denominator != 1: gt = '\\dfrac{\\pi}{%d}' % good.denominator
    def pt(x):
        x = F(x)
        if x.denominator == 1: return '%d\\pi' % x.numerator if x != 1 else '\\pi'
        return '\\dfrac{%s\\pi}{%d}' % ('' if x.numerator == 1 else x.numerator, x.denominator)
    return dict(en='The figure shows the graph of \\(y=\\sqrt{%d-x^2}\\). Find \\(\\displaystyle\\int_{%d}^{%d}\\sqrt{%d-x^2}\\,dx\\).' % (R * R, lo, R, R * R),
                vi='Hình vẽ là đồ thị của \\(y=\\sqrt{%d-x^2}\\). Tính \\(\\displaystyle\\int_{%d}^{%d}\\sqrt{%d-x^2}\\,dx\\).' % (R * R, lo, R, R * R),
                opts=[pt(good), pt(good * 2), pt(good / 2), pt(F(R * R)) if F(R * R) not in (good, good * 2, good / 2) else pt(good * 4)], fig=G.FIG(img, 'Semicircle', 'Nửa đường tròn', 300),
                ee='The graph is %s the circle of radius \\(%d\\); the integral is that area: \\(%s\\).' % ('a quarter of' if half else 'half of', R, pt(good)),
                ev='Đồ thị là %s đường tròn bán kính \\(%d\\); tích phân bằng diện tích phần đó: \\(%s\\).' % ('một phần tư' if half else 'nửa', R, pt(good)))

def i12_odd(r, lv, ctx):
    a = r.choice([1, 2, 3]); k = nz(r, -5, 5); c = nz(r, -4, 4); t = r.choice(['x^3', 'x^5', '\\sin x', 'x^3-x'])
    q = '%s%s%s' % (cf(c, t) if t != 'x^3-x' else '%d(x^3-x)' % c, '+' if k > 0 else '-', abs(k))
    good = 2 * a * k
    return dict(en='\\(\\displaystyle\\int_{-%d}^{%d}\\left(%s\\right)dx=\\)…' % (a, a, q), vi='\\(\\displaystyle\\int_{-%d}^{%d}\\left(%s\\right)dx=\\)…' % (a, a, q),
                opts=nopts(r, good, [0, a * k, good + 2 * c * a, -good]),
                ee='The part \\(%s\\) is odd, so its integral over \\([-%d;%d]\\) is 0; the constant gives \\(%d\\cdot%d=%d\\).' % (cf(c, t) if t != 'x^3-x' else '%d(x^3-x)' % c, a, a, k, 2 * a, good),
                ev='Phần \\(%s\\) là hàm lẻ nên tích phân trên \\([-%d;%d]\\) bằng 0; hằng số cho \\(%d\\cdot%d=%d\\).' % (cf(c, t) if t != 'x^3-x' else '%d(x^3-x)' % c, a, a, k, 2 * a, good))

def i12_param(r, lv, ctx):
    m = r.randint(2, 6); c = r.randint(-3, 4); T = m * m + c * m
    if T <= 0: raise AssertionError
    other = -m - c
    return dict(en='Find the positive number \\(m\\) such that \\(\\displaystyle\\int_0^m(2x%s)\\,dx=%d\\).' % ('' if c == 0 else ('%+d' % c), T),
                vi='Tìm số dương \\(m\\) sao cho \\(\\displaystyle\\int_0^m(2x%s)\\,dx=%d\\).' % ('' if c == 0 else ('%+d' % c), T),
                opts=nopts(r, m, [m + 1, abs(other) if abs(other) != m else m + 2, T // 2 if T // 2 != m else m - 1, max(1, m - 1) if m - 1 != m else 7]),
                ee='\\(\\displaystyle\\int_0^m(2x%s)dx=m^2%s=%d\\Rightarrow m=%d\\) (the other root \\(%d\\) is not positive).' % ('' if c == 0 else ('%+d' % c), '' if c == 0 else ('%+dm' % c), T, m, other),
                ev='\\(\\displaystyle\\int_0^m(2x%s)dx=m^2%s=%d\\Rightarrow m=%d\\) (nghiệm còn lại \\(%d\\) không dương).' % ('' if c == 0 else ('%+d' % c), '' if c == 0 else ('%+dm' % c), T, m, other))

def i12_ftc(r, lv, ctx):
    a, b = sorted(r.sample(range(-2, 6), 2)); fa = r.randint(-5, 8); I = nz(r, -6, 9)
    if r.random() < .5:
        return dict(en='\\(f\\) has a continuous derivative, \\(f(%d)=%d\\) and \\(\\displaystyle\\int_{%d}^{%d}f\'(x)\\,dx=%d\\). Then \\(f(%d)=\\)…' % (a, fa, a, b, I, b),
                    vi='Hàm số \\(f\\) có đạo hàm liên tục, \\(f(%d)=%d\\) và \\(\\displaystyle\\int_{%d}^{%d}f\'(x)\\,dx=%d\\). Khi đó \\(f(%d)=\\)…' % (a, fa, a, b, I, b),
                    opts=nopts(r, fa + I, [I - fa, fa - I, I, fa * I]),
                    ee='\\(\\displaystyle\\int_{%d}^{%d}f\'(x)dx=f(%d)-f(%d)\\Rightarrow f(%d)=%d+%d=%d\\).' % (a, b, b, a, b, fa, I, fa + I),
                    ev='\\(\\displaystyle\\int_{%d}^{%d}f\'(x)dx=f(%d)-f(%d)\\Rightarrow f(%d)=%d+%d=%d\\).' % (a, b, b, a, b, fa, I, fa + I))
    fb = fa + I
    return dict(en='\\(F\\) is an antiderivative of \\(f\\) on \\(\\mathbb R\\) with \\(F(%d)=%d\\) and \\(F(%d)=%d\\). Then \\(\\displaystyle\\int_{%d}^{%d}f(x)\\,dx=\\)…' % (a, fa, b, fb, b, a),
                vi='\\(F\\) là một nguyên hàm của \\(f\\) trên \\(\\mathbb R\\) với \\(F(%d)=%d\\) và \\(F(%d)=%d\\). Khi đó \\(\\displaystyle\\int_{%d}^{%d}f(x)\\,dx=\\)…' % (a, fa, b, fb, b, a),
                opts=nopts(r, -I, [I, fa + fb, fb, -fa - fb if -fa - fb != -I else I + 1]),
                ee='Note the order of the limits: \\(\\displaystyle\\int_{%d}^{%d}f(x)dx=F(%d)-F(%d)=%d\\).' % (b, a, a, b, -I), ev='Chú ý thứ tự cận: \\(\\displaystyle\\int_{%d}^{%d}f(x)dx=F(%d)-F(%d)=%d\\).' % (b, a, a, b, -I))

def i12_piece(r, lv, ctx):
    a = r.choice([2, 4, -2, 6]); b = 1 - a
    I = F(1, 3) + F(a * 3, 2) + b
    return dict(en='\\(f(x)=\\begin{cases}x^2&\\text{if } x\\le1\\\\%s&\\text{if } x\\gt1\\end{cases}\\) (continuous). Then \\(\\displaystyle\\int_0^2f(x)\\,dx=\\)…' % poly_tex(0, a, b),
                vi='Cho \\(f(x)=\\begin{cases}x^2&\\text{khi } x\\le1\\\\%s&\\text{khi } x\\gt1\\end{cases}\\) (liên tục). Khi đó \\(\\displaystyle\\int_0^2f(x)\\,dx=\\)…' % poly_tex(0, a, b),
                opts=fo(I, [F(8, 3), F(a * 2) + 2 * b, I + 1, F(1, 3) + 2 * a + 2 * b if F(1, 3) + 2 * a + 2 * b != I else I - 1]),
                ee='Split at 1: \\(\\displaystyle\\int_0^1x^2dx+\\int_1^2(%s)dx=\\dfrac13+%s=%s\\).' % (poly_tex(0, a, b), frt(F(3 * a, 2) + b), frt(I)),
                ev='Tách tại 1: \\(\\displaystyle\\int_0^1x^2dx+\\int_1^2(%s)dx=\\dfrac13+%s=%s\\).' % (poly_tex(0, a, b), frt(F(3 * a, 2) + b), frt(I)))

def i12_vt(r, lv, ctx):
    for _ in range(100):
        t1 = r.randint(1, 3); t2 = t1 + r.randint(2, 5); t3 = t2 + r.randint(1, 3); Vm = r.choice([4, 6, 8, 10, 12])
        if t3 <= 10: break
    S = F(Vm * (t3 + t2 - t1), 2)
    f = lambda x: (Vm * x / t1 if x <= t1 else Vm if x <= t2 else Vm * (t3 - x) / (t3 - t2)) if 0 <= x <= t3 else None
    img = G.graph_svg([(f, G.GREEN)], (-.6, t3 + 1), (-1, Vm + 2), G.int_ticks(1, t3 + 0), [(Vm, str(Vm))] + ([(Vm // 2, str(Vm // 2))] if Vm >= 6 else []),
                      dots=[(t1, Vm, False), (t2, Vm, False), (t3, 0, False)], W=6.2, H=3.6, names=('t', 'v'))
    ne_, nv_ = V(lv, [('a cart', 'một xe đẩy'), ('a lift (elevator)', 'một thang máy'), ('a train between two stations', 'một đoàn tàu giữa hai ga')])
    return dict(en='The figure shows the velocity \\(v\\) (m/s) of %s against time \\(t\\) (s). How far does it travel from \\(t=0\\) until it stops (m)?' % ne_,
                vi='Hình vẽ là đồ thị vận tốc \\(v\\) (m/s) theo thời gian \\(t\\) (s) của %s. Từ \\(t=0\\) đến khi dừng, nó đi được bao nhiêu mét?' % nv_,
                opts=nopts(r, S, [Vm * t3, Vm * (t2 - t1), F(Vm * t3, 2), S + Vm]), fig=G.FIG(img, 'Velocity graph', 'Đồ thị vận tốc', 340),
                ee='Distance = area under the graph (a trapezoid): \\(\\dfrac{(%d+%d)\\cdot%d}{2}=%s\\).' % (t3, t2 - t1, Vm, ne(S)),
                ev='Quãng đường = diện tích dưới đồ thị (hình thang): \\(\\dfrac{(%d+%d)\\cdot%d}{2}=%s\\).' % (t3, t2 - t1, Vm, nv(S)))

def i12_mean(r, lv, ctx):
    for _ in range(500):
        h = r.choice([4, 6, 8, 12]); a = r.randint(18, 26); c = r.choice([F(1, 4), F(1, 2), F(1, 3), F(1, 6)]); b = r.choice([1, 2, 3, 4])
        avg = a + F(b * h, 2) - c * F(h * h, 3)
        if avg.denominator == 1 and all(a + b * t - c * t * t > 0 for t in range(h + 1)): break
    else: raise AssertionError
    Tt = 'T(t)=%d+%dt-%st^2' % (a, b, frt(c)) if b != 1 else 'T(t)=%d+t-%st^2' % (a, frt(c))
    vals = [a + b * t - c * t * t for t in (0, h)]
    return dict(en='The temperature of a room is \\(%s\\) (°C), \\(0\\le t\\le%d\\) (hours). Its average temperature on this interval, \\(\\dfrac{1}{%d}\\displaystyle\\int_0^{%d}T(t)\\,dt\\), is (°C)…' % (Tt, h, h, h),
                vi='Nhiệt độ một căn phòng là \\(%s\\) (°C), \\(0\\le t\\le%d\\) (giờ). Nhiệt độ trung bình trong khoảng này, \\(\\dfrac{1}{%d}\\displaystyle\\int_0^{%d}T(t)\\,dt\\), bằng (°C)…' % (Tt, h, h, h),
                opts=nopts(r, avg, [avg * h, F(vals[0] + vals[1], 2) if F(vals[0] + vals[1], 2) != avg else avg + 1, a, avg + 2]),
                ee='\\(\\displaystyle\\int_0^{%d}T\\,dt=%s\\), divided by \\(%d\\): \\(%s\\).' % (h, ne(avg * h), h, ne(avg)), ev='\\(\\displaystyle\\int_0^{%d}T\\,dt=%s\\), chia cho \\(%d\\): \\(%s\\).' % (h, nv(avg * h), h, nv(avg)))

D12 = [i12_area, i12_semicircle, i12_odd, i12_param, i12_ftc, i12_piece, i12_vt, i12_mean]
