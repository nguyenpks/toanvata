# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 10 – Bài 15 (hàm số), Bài 16 (hàm số bậc hai). Đáp án tính chính xác bằng Fraction."""
from fractions import Fraction as F
from mb_selfpractice import pick_opts, fr
from mb_lib import TI
from freqtable import num

def TT(en, vi): return '§' + TI(en, vi)
def D(x): return num(F(x))
def poly(cs, v='x'):
    d = len(cs) - 1; s = ''
    for i, c in enumerate(cs):
        p = d - i; c = F(c)
        if c == 0: continue
        sg = '-' if c < 0 else ('+' if s else ''); a = abs(c)
        body = (v if p == 1 else '%s^2' % v if p == 2 else '%s^{%d}' % (v, p)) if p else ''
        coef = '' if (a == 1 and p) else fr(a)
        s += sg + coef + body
    return s or '0'
def iv(a, b, lo='[', hi=')'):
    """Khoảng/đoạn theo kí hiệu SGK; a hoặc b có thể là ±∞."""
    A = '-\\infty' if a is None else fr(F(a)); B = '+\\infty' if b is None else fr(F(b))
    return '%s%s;\\,%s%s' % ('(' if a is None else lo, A, B, ')' if b is None else hi)
# ================= Bài 15. Hàm số =================
def fn_dom(r, lv):
    k = r.choice(['sqrt', 'frac', 'both']); a, b = r.choice([1, 2, 3, -1, -2]), r.randint(-6, 6)
    if k == 'sqrt':
        x0 = F(-b, a); f = '\\sqrt{%s}' % poly([a, b])
        ok = '[%s;\\,+\\infty)' % fr(x0) if a > 0 else '(-\\infty;\\,%s]' % fr(x0)
        wr = ['(%s;\\,+\\infty)' % fr(x0) if a > 0 else '(-\\infty;\\,%s)' % fr(x0), '(-\\infty;\\,%s]' % fr(x0) if a > 0 else '[%s;\\,+\\infty)' % fr(x0), '\\mathbb R\\setminus\\{%s\\}' % fr(x0), '\\mathbb R']
        ee = 'Need \\(%s\\ge0\\).' % poly([a, b])
    elif k == 'frac':
        x0 = F(-b, a); f = '\\dfrac{%d}{%s}' % (r.choice([1, 2, 3]), poly([a, b]))
        ok = '\\mathbb R\\setminus\\{%s\\}' % fr(x0); wr = ['\\mathbb R', '(%s;\\,+\\infty)' % fr(x0), '[%s;\\,+\\infty)' % fr(x0), '\\mathbb R\\setminus\\{%s\\}' % fr(-x0) if x0 else '\\mathbb R\\setminus\\{1\\}']
        ee = 'Need \\(%s\\ne0\\).' % poly([a, b])
    else:
        p, q = r.randint(-3, 3), r.randint(4, 8); f = '\\dfrac{\\sqrt{x%+d}}{x-%d}' % (-p, q) if p else '\\dfrac{\\sqrt{x}}{x-%d}' % q
        ok = '[%d;\\,+\\infty)\\setminus\\{%d\\}' % (p, q); wr = ['[%d;\\,+\\infty)' % p, '(%d;\\,+\\infty)' % p, '\\mathbb R\\setminus\\{%d\\}' % q, '(%d;\\,+\\infty)\\setminus\\{%d\\}' % (p, q)]
        ee = 'Need \\(x\\ge%d\\) and \\(x\\ne%d\\).' % (p, q)
    return dict(en='The domain of \\(y=%s\\) is…' % f, vi='Tập xác định của hàm số \\(y=%s\\) là…' % f, opts=pick_opts(r, ok, wr), ans=0, ee=ee, ev=ee.replace('Need', 'Điều kiện:').replace(' and ', ' và '))
def fn_val(r, lv):
    cs = [r.choice([1, 2, -1, 3]), r.randint(-5, 5), r.randint(-6, 6)]; x0 = r.randint(-3, 3); v = cs[0] * x0 * x0 + cs[1] * x0 + cs[2]
    return dict(en='\\(f(x)=%s\\). Then \\(f(%d)=\\)…' % (poly(cs), x0), vi='Cho \\(f(x)=%s\\). Khi đó \\(f(%d)=\\)…' % (poly(cs), x0),
      opts=pick_opts(r, str(v), [str(-cs[0] * x0 * x0 + cs[1] * x0 + cs[2]), str(cs[0] * x0 * x0 - cs[1] * x0 + cs[2]), str(v + 1), str(v - 2)]), ans=0,
      ee='Substitute \\(x=%d\\): \\(%d\\).' % (x0, v), ev='Thay \\(x=%d\\): \\(%d\\).' % (x0, v))
def fn_pt(r, lv):
    a, b = r.choice([2, -1, 3, -2, 1]), r.randint(-4, 4); x0 = r.randint(-3, 3); good = (x0, a * x0 + b)
    bad = [(x0 + 1, a * x0 + b), (x0, a * x0 + b + 1), (-x0 if x0 else 2, a * x0 + b), (x0 + 2, a * x0 + b - 1)]
    bad = [p for p in bad if p[1] != a * p[0] + b]
    return dict(en='Which point lies on the graph of \\(y=%s\\)?' % poly([a, b]), vi='Điểm nào thuộc đồ thị hàm số \\(y=%s\\)?' % poly([a, b]),
      opts=pick_opts(r, '(%d;\\,%d)' % good, ['(%d;\\,%d)' % p for p in bad]), ans=0, ee='\\(%s\\) at \\(x=%d\\) gives \\(%d\\).' % (poly([a, b]), x0, good[1]), ev='Thay \\(x=%d\\) được \\(y=%d\\).' % (x0, good[1]))
def fn_mono(r, lv):
    kind = r.choice(['lin', 'inv', 'sq']);
    if kind == 'lin':
        a, b = r.choice([2, -3, -1, 4, F(1, 2), F(-1, 2)]), r.randint(-5, 5); f = poly([a, b]); inc = a > 0
        ok = TT('increasing on \\(\\mathbb R\\)', 'đồng biến trên \\(\\mathbb R\\)') if inc else TT('decreasing on \\(\\mathbb R\\)', 'nghịch biến trên \\(\\mathbb R\\)')
        wr = [TT('decreasing on \\(\\mathbb R\\)', 'nghịch biến trên \\(\\mathbb R\\)') if inc else TT('increasing on \\(\\mathbb R\\)', 'đồng biến trên \\(\\mathbb R\\)'), TT('constant', 'là hàm hằng'), TT('increasing only on \\((0;+\\infty)\\)', 'chỉ đồng biến trên \\((0;+\\infty)\\)')]
        ee = 'Slope \\(a=%s\\) is %s.' % (fr(F(a)), 'positive' if inc else 'negative')
    elif kind == 'inv':
        k = r.choice([1, 2, 3, -1, -2]); f = '\\dfrac{%d}{x}' % k; inc = k < 0
        ok = TT('%s on \\((0;+\\infty)\\)' % ('increasing' if inc else 'decreasing'), '%s trên \\((0;+\\infty)\\)' % ('đồng biến' if inc else 'nghịch biến'))
        wr = [TT('%s on \\((0;+\\infty)\\)' % ('decreasing' if inc else 'increasing'), '%s trên \\((0;+\\infty)\\)' % ('nghịch biến' if inc else 'đồng biến')), TT('increasing on \\(\\mathbb R\\)', 'đồng biến trên \\(\\mathbb R\\)'), TT('decreasing on \\(\\mathbb R\\)', 'nghịch biến trên \\(\\mathbb R\\)')]
        ee = 'For \\(0\\lt x_1\\lt x_2\\): \\(\\dfrac{%d}{x_1}-\\dfrac{%d}{x_2}=\\dfrac{%d(x_2-x_1)}{x_1x_2}\\) has the sign of %d.' % (k, k, k, k)
    else:
        c = r.randint(-3, 3); f = 'x^2%s' % ('%+d' % c if c else '')
        ok = TT('decreasing on \\((-\\infty;0)\\), increasing on \\((0;+\\infty)\\)', 'nghịch biến trên \\((-\\infty;0)\\), đồng biến trên \\((0;+\\infty)\\)')
        wr = [TT('increasing on \\((-\\infty;0)\\), decreasing on \\((0;+\\infty)\\)', 'đồng biến trên \\((-\\infty;0)\\), nghịch biến trên \\((0;+\\infty)\\)'), TT('increasing on \\(\\mathbb R\\)', 'đồng biến trên \\(\\mathbb R\\)'), TT('decreasing on \\(\\mathbb R\\)', 'nghịch biến trên \\(\\mathbb R\\)')]
        ee = 'The parabola opens upward with vertex at \\(x=0\\).'
    return dict(en='The function \\(y=%s\\) is…' % f, vi='Hàm số \\(y=%s\\)…' % f, opts=[ok] + wr, ans=0, ee=ee, ev=ee.replace('Slope', 'Hệ số góc').replace('is positive', 'dương').replace('is negative', 'âm').replace('For', 'Với').replace('has the sign of', 'cùng dấu với').replace('The parabola opens upward with vertex at', 'Parabol quay bề lõm lên, đỉnh tại'))
def fn_taxi(r, lv):
    f1, km1, p2, km2, p3 = r.choice([(12, 1, 15, 30, 11), (10, 1, 14, 25, 12), (15, 2, 16, 30, 13)]); d = r.choice([5, 8, 12, 20, 35, 40])
    cost = f1 if d <= km1 else (f1 + (min(d, km2) - km1) * p2 + max(0, d - km2) * p3)
    wrong = [f1 + d * p2, f1 + (d - km1) * p3, d * p2, cost + p2]
    return dict(en='A taxi charges %d thousand VND for the first %d km, %d thousand VND/km from km %d to km %d, and %d thousand VND/km after that. The fare for %d km is… (thousand VND)' % (f1, km1, p2, km1, km2, p3, d),
      vi='Một hãng taxi tính %d nghìn đồng cho %d km đầu, %d nghìn đồng/km từ trên km thứ %d đến km thứ %d, và %d nghìn đồng/km từ trên km thứ %d. Giá cước cho %d km là… (nghìn đồng)' % (f1, km1, p2, km1, km2, p3, km2, d),
      opts=pick_opts(r, str(cost), [str(w) for w in wrong]), ans=0, ee='Piecewise function: \\(%d+%d\\cdot%d+%d\\cdot%d=%d\\).' % (f1, min(d, km2) - km1, p2, max(0, d - km2), p3, cost),
      ev='Hàm số cho bởi nhiều công thức: \\(%d+%d\\cdot%d+%d\\cdot%d=%d\\).' % (f1, min(d, km2) - km1, p2, max(0, d - km2), p3, cost))
def fn_range(r, lv):
    c = r.randint(-4, 5); k = r.choice(['sq', 'sqrt', 'neg'])
    if k == 'sq': f, ok, wr = 'x^2%s' % ('%+d' % c if c else ''), '[%d;\\,+\\infty)' % c, ['\\mathbb R', '(%d;\\,+\\infty)' % c, '(-\\infty;\\,%d]' % c]
    elif k == 'sqrt': f, ok, wr = '\\sqrt x%s' % ('%+d' % c if c else ''), '[%d;\\,+\\infty)' % c, ['[0;\\,+\\infty)' if c else '\\mathbb R', '(%d;\\,+\\infty)' % c, '\\mathbb R']
    else: f, ok, wr = '-x^2%s' % ('%+d' % c if c else ''), '(-\\infty;\\,%d]' % c, ['[%d;\\,+\\infty)' % c, '\\mathbb R', '(-\\infty;\\,%d)' % c]
    return dict(en='The range of \\(y=%s\\) is…' % f, vi='Tập giá trị của hàm số \\(y=%s\\) là…' % f, opts=pick_opts(r, ok, wr), ans=0,
      ee='\\(x^2\\ge0\\) and \\(\\sqrt x\\ge0\\), with equality at \\(x=0\\).', ev='\\(x^2\\ge0\\), \\(\\sqrt x\\ge0\\), dấu bằng xảy ra tại \\(x=0\\).')
def fn_elec(r, lv):
    t = [(50, 1.8), (50, 1.9), (100, 2.2)]; kwh = r.choice([40, 80, 120, 150, 180]); cost = F(0); left = kwh; rows = []
    for lim, pr in t:
        u = min(left, lim); cost += u * F(str(pr)); left -= u
        if left == 0: break
    cost += left * F('2.8')
    return dict(en='Electricity prices (thousand VND/kWh): first 50 kWh: 1.8; next 50 kWh: 1.9; next 100 kWh: 2.2; above 200 kWh: 2.8. A family uses %d kWh. The bill (without tax) is… thousand VND' % kwh,
      vi='Giá điện (nghìn đồng/kWh): 50 kWh đầu: 1,8; 50 kWh tiếp: 1,9; 100 kWh tiếp: 2,2; trên 200 kWh: 2,8. Một gia đình dùng %d kWh. Tiền điện (chưa thuế) là… nghìn đồng' % kwh,
      opts=pick_opts(r, D(cost), [D(kwh * F('1.8')), D(kwh * F('2.2')), D(cost + 10), D(kwh * F('1.9'))]), ans=0, ee='Add the cost of each tier.', ev='Cộng tiền của từng bậc.')
M15S10 = [fn_dom, fn_val, fn_pt, fn_mono, fn_taxi, fn_range, fn_elec, fn_dom]
# ================= Bài 16. Hàm số bậc hai =================
def _q(r):
    a = r.choice([1, -1, 2, -2, 3, F(1, 2), -3]); h = r.randint(-3, 3); k = r.randint(-4, 5)
    b, c = -2 * a * h, a * h * h + k
    if F(b).denominator != 1 or F(c).denominator != 1: raise AssertionError
    return F(a), F(h), F(k), F(b), F(c)
def q_vertex(r, lv):
    a, h, k, b, c = _q(r)
    return dict(en='The vertex of the parabola \\(y=%s\\) is…' % poly([a, b, c]), vi='Đỉnh của parabol \\(y=%s\\) là…' % poly([a, b, c]),
      opts=pick_opts(r, '(%s;\\,%s)' % (fr(h), fr(k)), ['(%s;\\,%s)' % (fr(-h), fr(k)), '(%s;\\,%s)' % (fr(h), fr(c)), '(%s;\\,%s)' % (fr(k), fr(h)), '(%s;\\,%s)' % (fr(-h), fr(a * h * h + b * -h + c))]), ans=0,
      ee='\\(x_I=-\\dfrac{b}{2a}=%s\\), \\(y_I=f(%s)=%s\\).' % (fr(h), fr(h), fr(k)), ev='\\(x_I=-\\dfrac{b}{2a}=%s\\), \\(y_I=f(%s)=%s\\).' % (fr(h), fr(h), fr(k)))
def q_mono(r, lv):
    a, h, k, b, c = _q(r); up = a > 0
    o1 = TT('decreasing on \\(%s\\), increasing on \\(%s\\)' % (iv(None, h, hi=')'), iv(h, None, lo='(')), 'nghịch biến trên \\(%s\\), đồng biến trên \\(%s\\)' % (iv(None, h, hi=')'), iv(h, None, lo='(')))
    o2 = TT('increasing on \\(%s\\), decreasing on \\(%s\\)' % (iv(None, h, hi=')'), iv(h, None, lo='(')), 'đồng biến trên \\(%s\\), nghịch biến trên \\(%s\\)' % (iv(None, h, hi=')'), iv(h, None, lo='(')))
    # Kiểm định 08/11/2026 (M-003): nhiễu không được là khoảng con của khoảng đơn điệu thật (vd a>0, h=-2: "đồng biến trên (2;+∞)" cũng đúng).
    m3 = -h if (not up or -h < h) else h - 1          # đồng biến trên (m3;+∞) sai  <=>  a<0 hoặc m3<h
    n4 = k if (not up or k > h) else h + 1            # nghịch biến trên (-∞;n4) sai <=>  a<0 hoặc n4>h
    assert (not up or m3 < h) and (not up or n4 > h)
    o3 = TT('increasing on \\(%s\\)' % iv(m3, None, lo='('), 'đồng biến trên \\(%s\\)' % iv(m3, None, lo='(')) if h else TT('increasing on \\(\\mathbb R\\)', 'đồng biến trên \\(\\mathbb R\\)')
    o4 = TT('decreasing on \\(%s\\)' % iv(None, n4, hi=')'), 'nghịch biến trên \\(%s\\)' % iv(None, n4, hi=')')) if k != h else TT('decreasing on \\(\\mathbb R\\)', 'nghịch biến trên \\(\\mathbb R\\)')
    return dict(en='The function \\(y=%s\\) is…' % poly([a, b, c]), vi='Hàm số \\(y=%s\\)…' % poly([a, b, c]), opts=[o1 if up else o2, o2 if up else o1, o3, o4], ans=0,
      ee='\\(a%s0\\) and \\(-\\dfrac b{2a}=%s\\).' % ('\\gt' if up else '\\lt', fr(h)), ev='\\(a%s0\\) và \\(-\\dfrac b{2a}=%s\\).' % ('\\gt' if up else '\\lt', fr(h)))
def q_ext(r, lv):
    a, h, k, b, c = _q(r); up = a > 0
    w = ('minimum', 'nhỏ nhất') if up else ('maximum', 'lớn nhất')
    return dict(en='The %s value of \\(y=%s\\) is…' % (w[0], poly([a, b, c])), vi='Giá trị %s của hàm số \\(y=%s\\) là…' % (w[1], poly([a, b, c])),
      opts=pick_opts(r, fr(k), [fr(h), fr(c), fr(-k) if k else '1', fr(k + 1), fr(k - 2), fr(a)]), ans=0, ee='It is \\(y_I=%s\\), reached at \\(x=%s\\).' % (fr(k), fr(h)), ev='Đó là \\(y_I=%s\\), đạt tại \\(x=%s\\).' % (fr(k), fr(h)))
def q_find(r, lv):
    a, h, k, b, c = _q(r)
    return dict(en='The parabola \\(y=ax^2+bx+c\\) has vertex \\(I(%s;\\,%s)\\) and passes through \\((%s;\\,%s)\\). Then \\(a=\\)…' % (fr(h), fr(k), fr(h + 1), fr(a + k)),
      vi='Parabol \\(y=ax^2+bx+c\\) có đỉnh \\(I(%s;\\,%s)\\) và đi qua điểm \\((%s;\\,%s)\\). Khi đó \\(a=\\)…' % (fr(h), fr(k), fr(h + 1), fr(a + k)),
      opts=pick_opts(r, fr(a), [fr(-a), fr(a + k), fr(2 * a), fr(a + 1)]), ans=0,
      ee='\\(y=a(x-%s)^2+%s\\); substitute the point: \\(a\\cdot1+%s=%s\\Rightarrow a=%s\\).' % (fr(h), fr(k), fr(k), fr(a + k), fr(a)), ev='\\(y=a(x-%s)^2+%s\\); thay tọa độ điểm: \\(a\\cdot1+%s=%s\\Rightarrow a=%s\\).' % (fr(h), fr(k), fr(k), fr(a + k), fr(a)))
def q_ball(r, lv):
    v0, h0 = r.choice([(10, 1), (20, 2), (15, F(3, 2)), (12, 1), (8, 2)]); g = F(5)   # h(t) = -5t^2 + v0 t + h0
    t = F(v0, 10); H = -g * t * t + v0 * t + h0
    return dict(en='A ball is thrown upward; its height is \\(h(t)=-5t^2+%dt+%s\\) (m). Its greatest height is…' % (v0, num(F(h0), comma=False)), vi='Một quả bóng được ném lên, độ cao \\(h(t)=-5t^2+%dt+%s\\) (m). Độ cao lớn nhất của bóng là…' % (v0, D(h0)),
      opts=pick_opts(r, D(H) + '\\ \\text{m}', [D(t) + '\\ \\text{m}', D(H - h0) + '\\ \\text{m}', D(-g * 4 * t * t + 2 * v0 * t + h0) + '\\ \\text{m}', D(H + 5) + '\\ \\text{m}']), ans=0,
      ee='Vertex at \\(t=\\dfrac{%d}{10}=%s\\): \\(h=%s\\).' % (v0, D(t), D(H)), ev='Đỉnh tại \\(t=\\dfrac{%d}{10}=%s\\): \\(h=%s\\).' % (v0, D(t), D(H)))
def q_fence(r, lv):
    L = r.choice([20, 40, 60, 80, 100]); kind = r.choice(['four', 'wall'])
    if kind == 'four': A = F(L * L, 16); en, vi = 'a rectangle with %d m of fence' % L, 'hình chữ nhật bằng %d m lưới' % L; ee = 'Sides \\(x\\), \\(\\frac{%d}2-x\\); \\(S=x(%s-x)\\) is largest at \\(x=%s\\).' % (L, fr(F(L, 2)), fr(F(L, 4)))
    else: A = F(L * L, 8); en, vi = 'a rectangle along a wall (three sides fenced) with %d m of fence' % L, 'hình chữ nhật dựa vào bức tường (rào ba cạnh) bằng %d m lưới' % L; ee = '\\(S=x(%d-2x)\\) is largest at \\(x=%s\\).' % (L, fr(F(L, 4)))
    return dict(en='A farmer makes %s. The largest possible area is…' % en, vi='Bác nông dân rào một mảnh đất %s. Diện tích lớn nhất có thể là…' % vi,
      opts=pick_opts(r, fr(A) + '\\ \\text{m}^2', [fr(x) + '\\ \\text{m}^2' for x in (F(L * L, 4), F(L * L, 16) if kind == 'wall' else F(L * L, 8), F(L * L, 2), A + L)]), ans=0, ee=ee, ev=ee.replace('Sides', 'Các cạnh').replace('is largest at', 'lớn nhất khi'))
def q_axis(r, lv):
    a, h, k, b, c = _q(r)
    return dict(en='The axis of symmetry of \\(y=%s\\) is…' % poly([a, b, c]), vi='Trục đối xứng của parabol \\(y=%s\\) là…' % poly([a, b, c]),
      opts=pick_opts(r, 'x=%s' % fr(h), ['x=%s' % fr(-h) if h else 'x=1', 'y=%s' % fr(k), 'x=%s' % fr(b) if b != h else 'x=%s' % fr(h + 2), 'x=%s' % fr(k) if k != h else 'x=%s' % fr(h - 2)]), ans=0,
      ee='\\(x=-\\dfrac{b}{2a}=%s\\).' % fr(h), ev='\\(x=-\\dfrac{b}{2a}=%s\\).' % fr(h))
def q_price(r, lv):
    p0, q0, dq, c = r.choice([(50, 200, 10, 20), (40, 300, 20, 15), (35, 120, 8, 15), (100, 200, 5, 40), (80, 300, 10, 40), (60, 240, 12, 30)])   # giá p0, bán q0 chiếc; giảm 1 nghìn đồng bán thêm dq chiếc; giá nhập c
    # lợi nhuận theo giảm x: (p0 - x - c)(q0 + dq x); đỉnh x* = ((p0-c)dq - q0)/(2dq)
    xs = F((p0 - c) * dq - q0, 2 * dq)
    if xs <= 0 or xs >= p0 - c: raise AssertionError
    price = p0 - xs
    return dict(en='A shop buys a T-shirt for %d thousand VND and sells %d shirts a month at %d thousand VND. Each 1 thousand VND price cut sells %d more shirts. Which selling price gives the largest profit?' % (c, q0, p0, dq),
      vi='Một cửa hàng nhập áo thun giá %d nghìn đồng, bán giá %d nghìn đồng thì mỗi tháng bán được %d chiếc. Cứ giảm giá 1 nghìn đồng thì bán thêm %d chiếc. Giá bán nào cho lợi nhuận lớn nhất?' % (c, p0, q0, dq),
      opts=pick_opts(r, D(price), [str(p0), D(p0 - 2 * xs), D(F(p0 + c, 2)), D(price + 1)]), ans=0,
      ee='Cut \\(x\\): profit \\((%d-x)(%d+%dx)\\), a parabola with vertex at \\(x=%s\\).' % (p0 - c, q0, dq, D(xs)), ev='Giảm \\(x\\): lợi nhuận \\((%d-x)(%d+%dx)\\) là hàm bậc hai, đỉnh tại \\(x=%s\\).' % (p0 - c, q0, dq, D(xs)))
M16S10 = [q_vertex, q_mono, q_ext, q_find, q_ball, q_fence, q_axis, q_price]
