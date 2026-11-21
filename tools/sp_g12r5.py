# -*- coding: utf-8 -*-
"""Hiệu chỉnh lớp 12 – đợt 21/11/2026: Bài 5 (bài toán tối ưu), 6 (vectơ trong không gian), 7 (hệ trục Oxyz), 8 (biểu thức tọa độ).
Mỗi bài đang có 15 câu/mức (A 3 · B 2 · C 2 · D 8). Đợt này GIỮ NGUYÊN toàn bộ câu cũ (A–D) và thêm 5 câu/mức
(A +3, B +1, C +1) → 20 câu/mức (A 6 · B 3 · C 3 · D 8). Mỗi câu mới là một DẠNG khác các dạng đã có ở A–D của bài.

Hàm sinh (r, lv, ctx) → dict như sp_g12r4: en, vi; opts (opts[0] đúng) | truth | key; ee, ev; fig = (html_en, html_vi) tùy chọn.
Cách hỏi đổi theo mức bằng V(lv, [...]) → ba mức không có câu trùng. Đáp án tính bằng số nguyên / Fraction ngay trong hàm;
tools/audit_g12r5.py kiểm tra lại độc lập từ trang đã dựng (không dùng mã trong tệp này)."""
import math, random, re
from fractions import Fraction as F
from mb_quick import tf, sh, GRP
from mb_lib import MCQ
from sp_g11r import tx, ne, nv, nopts, key, Q3D, TD, _fig
from sp_g11r2 import frt, fo, V
from sp_g12r import V3, sq, dot, sub, add, mul, n2, isq, CUBE1, CUBE4, vv, nz
import sp_g12r4 as R4
import fig2d as G
from fig2d import Canvas

def M(s): return '\\(%s\\)' % s
HN = ('Enter a number.', 'Nhập một số.')

# ================================================================ lắp bộ đề: giữ mọi câu cũ, thêm câu mới vào cuối A, B, C
def extend(practice, A, B, C, seeds):
    """practice: danh sách nhóm (tiêu đề, câu, [mức]) đang dùng, mỗi mức đúng 4 nhóm A, B, C, D (TD).
    Thêm câu do A, B, C sinh vào cuối từng nhóm; đánh số lại liên tục A → D. Nội dung câu cũ giữ nguyên."""
    oldtxt = ''.join(''.join(g[1]) for g in practice); used = set(); out = []
    for lv, seed in zip((1, 2, 3), seeds):
        gs = [g for g in practice if g[2] == [lv]]
        assert [g[0] for g in gs] == GRP + [TD], [g[0] for g in gs]
        r = random.Random(seed)
        oA, oB, oC, oD = [list(g[1]) for g in gs]
        n0 = len(oA)
        cnt = {L: 0 for L in 'abcd'}                    # đặt đáp án đúng của câu mới vào chữ cái đang ít dùng nhất ở mức này
        for h in oA + oD:
            m = re.search(r'data-type="mcq" data-answer="([abcd])"', h)
            if m: cnt[m.group(1)] += 1
        nA = []
        for i, b in enumerate(A):
            q = R4._gen(b, r, lv, {}, used, oldtxt); en, vi = _fig(q)
            lo = min(cnt.values()); L = r.choice([x for x in 'abcd' if cnt[x] == lo]); cnt[L] += 1; k = 'abcd'.index(L)
            opts = list(q['opts'][1:]); opts.insert(k, q['opts'][0]); assert len(set(opts)) == 4
            nA.append(MCQ(n0 + 1 + i, (en, vi), opts, L, ('Answer: %s. %s' % (L, q['ee']), 'Đáp án %s. %s' % (L, q['ev']))))
        nB = []
        for b in B:
            q = R4._gen(b, r, lv, {}, used, oldtxt); en, vi = _fig(q); nB.append(tf(1, en, vi, q['truth'], q['ee'], q['ev']))
        nC = []
        for b in C:
            q = R4._gen(b, r, lv, {}, used, oldtxt); en, vi = _fig(q)
            nC.append(sh(1, en, vi, q['key'], q['ee'], q['ev'], hint=q.get('hint', HN)))
        n = 1
        for title, items in zip(GRP + [TD], (oA + nA, oB + nB, oC + nC, oD)):
            items = R4._renum(items, n); n += len(items); out.append((title, items, [lv]))
    return out

# ================================================================ BÀI 5 – Ứng dụng đạo hàm giải bài toán thực tiễn
def o5_rate_graph(r, lv, ctx):
    """Đọc đồ thị của V'(t) (tốc độ thay đổi thể tích nước) → thời điểm V lớn nhất. Nhầm hay gặp: chọn đỉnh của đồ thị V'."""
    a = r.choice([4, 6, 8]); T = a + r.choice([2, 3]); c = F(1, 2) if a == 4 else (F(1, 4) if a == 6 else F(1, 8))
    f = lambda t: float(c * F(t).limit_denominator(1000) * (a - F(t).limit_denominator(1000)))
    top = float(c * a * a / 4); bot = float(c * T * (a - T))
    fn = G.graph_svg([(lambda t: f(t) if 0 <= t <= T else None, G.GREEN)], (-0.6, T + 0.8), (bot - 0.6, top + 0.6),
                     [(a / 2, ne(F(a, 2))), (a, str(a)), (T, str(T))], [], dots=[(0, 0, False), (a, 0, False)],
                     W=6.4, H=3.8, names=('t', "y=V'(t)"))
    fig = G.FIG(fn, "Graph of V'(t)", "Đồ thị của V'(t)", 380)
    qe = V(lv, ['The figure shows the graph of \\(V\'(t)\\), the rate of change of the volume \\(V(t)\\) of water in a reservoir, for \\(0\\le t\\le %d\\) (\\(t\\) in hours). At what time \\(t\\) is the volume of water largest?',
                'Water flows into and out of a tank. The graph of \\(V\'(t)\\) on \\([0;\\,%d]\\) is shown (\\(t\\) in hours). The amount of water in the tank is greatest at \\(t=\\)…',
                'A lake gains and loses water; the graph of the rate \\(V\'(t)\\) for \\(t\\in[0;\\,%d]\\) (hours) is given. Choose the time when the lake holds the most water.'])
    qv = V(lv, ['Hình bên là đồ thị của \\(V\'(t)\\) – tốc độ thay đổi thể tích \\(V(t)\\) của nước trong một hồ chứa, với \\(0\\le t\\le %d\\) (\\(t\\) tính bằng giờ). Thể tích nước lớn nhất tại thời điểm \\(t\\) nào?',
                'Nước vừa chảy vào vừa chảy ra khỏi một bể. Đồ thị của \\(V\'(t)\\) trên \\([0;\\,%d]\\) cho như hình (\\(t\\) tính bằng giờ). Lượng nước trong bể nhiều nhất khi \\(t=\\)…',
                'Một hồ nước vừa nhận vừa mất nước; đồ thị tốc độ \\(V\'(t)\\) với \\(t\\in[0;\\,%d]\\) (giờ) cho như hình. Chọn thời điểm hồ chứa nhiều nước nhất.'])
    return dict(en=qe % T, vi=qv % T, opts=[str(a), ne(F(a, 2)), str(T), '0'], fig=fig,
                ee='\\(V\'(t)\\gt0\\) on \\((0;\\,%d)\\) and \\(V\'(t)\\lt0\\) on \\((%d;\\,%d]\\): \\(V\\) increases, then decreases, so it is largest at \\(t=%d\\). (The top of the graph of \\(V\'\\) only shows when water rises fastest.)' % (a, a, T, a),
                ev='\\(V\'(t)\\gt0\\) trên \\((0;\\,%d)\\) và \\(V\'(t)\\lt0\\) trên \\((%d;\\,%d]\\): \\(V\\) tăng rồi giảm nên lớn nhất tại \\(t=%d\\). (Đỉnh đồ thị \\(V\'\\) chỉ là lúc nước dâng nhanh nhất.)' % (a, a, T, a))

def o5_speed(r, lv, ctx):
    """s(t) = -t³ + 3p t² + q t → v = s' = -3t² + 6pt + q lớn nhất tại t = p trên [0; T]."""
    p = r.choice([2, 3, 4]); q = r.choice([3, 5, 6, 9, 12]); T = p + r.choice([2, 3])
    v = lambda t: -3 * t * t + 6 * p * t + q; s = lambda t: -t ** 3 + 3 * p * t * t + q * t
    good = v(p); assert all(v(t) <= good for t in range(0, T + 1))
    qe = V(lv, ['A self-driving test car moves on a straight track; its distance from the start is \\(s(t)=-t^3+%dt^2+%dt\\) (m), \\(0\\le t\\le %d\\) (s). Its largest velocity (m/s) is…',
                'The position of a toy train is \\(s(t)=-t^3+%dt^2+%dt\\) (m) for \\(t\\in[0;\\,%d]\\) (s). Find the maximum velocity (m/s).',
                'In the first \\(%d\\) seconds a robot covers \\(s(t)=-t^3+%dt^2+%dt\\) metres along a line. What is its highest speed (m/s)?'.replace('metres', 'meters')])
    qv = V(lv, ['Một xe tự lái chạy thử trên đường thẳng, quãng đường đi được là \\(s(t)=-t^3+%dt^2+%dt\\) (m), \\(0\\le t\\le %d\\) (s). Vận tốc lớn nhất của xe (m/s) là…',
                'Vị trí của một tàu đồ chơi là \\(s(t)=-t^3+%dt^2+%dt\\) (m) với \\(t\\in[0;\\,%d]\\) (s). Tìm vận tốc lớn nhất (m/s).',
                'Trong \\(%d\\) giây đầu, một robot đi được \\(s(t)=-t^3+%dt^2+%dt\\) mét trên một đường thẳng. Vận tốc lớn nhất của robot (m/s) là bao nhiêu?'])
    args = (3 * p, q, T) if lv != 3 else (T, 3 * p, q)
    return dict(en=qe % args, vi=qv % args, opts=nopts(r, good, [s(p), v(T) if v(T) > 0 else q, q, 3 * p * p, p]),
                ee='\\(v(t)=s\'(t)=-3t^2+%dt+%d\\), \\(v\'(t)=-6t+%d=0\\Leftrightarrow t=%d\\in[0;\\,%d]\\). \\(v(0)=%d\\), \\(v(%d)=%d\\), \\(v(%d)=%d\\), so \\(v_{\\max}=%d\\).' % (6 * p, q, 6 * p, p, T, q, p, good, T, v(T), good),
                ev='\\(v(t)=s\'(t)=-3t^2+%dt+%d\\), \\(v\'(t)=-6t+%d=0\\Leftrightarrow t=%d\\in[0;\\,%d]\\). \\(v(0)=%d\\), \\(v(%d)=%d\\), \\(v(%d)=%d\\), nên \\(v_{\\max}=%d\\).' % (6 * p, q, 6 * p, p, T, q, p, good, T, v(T), good))

def tri_fig(a, b):
    c = Canvas(); s = 4.2 / max(a, b); W_, H_ = a * s, b * s; x0, y0 = W_ * 0.55, H_ * 0.45
    c.poly([(0, 0), (W_, 0), (0, H_)], 'color=%s, line width=1.3pt' % G.col(G.GREEN), close=True)
    c.o.append('\\fill[color=%s, opacity=0.25] (0,0) rectangle (%.3f,%.3f);' % (G.col(G.ORANGE), x0, y0))
    c.poly([(0, 0), (x0, 0), (x0, y0), (0, y0)], 'color=%s, line width=1.1pt' % G.col(G.ORANGE), close=True)
    c.poly([(0, .22), (.22, .22), (.22, 0)], 'ink, line width=0.6pt')
    for (x, y), nm, cd in [((0, 0), 'A', [(-.3, -.25)]), ((W_, 0), 'B', [(.3, -.25), (0, -.3)]), ((0, H_), 'C', [(-.3, .2), (-.3, 0)]), ((x0, y0), 'M', [(.3, .25), (.32, 0)])]:
        c.dot(x, y); c.label(x, y, '$%s$' % nm, .3, .36, cd)
    c.label(x0 / 2, 0, '$x$', .3, .36, [(0, -.3)]); c.label(0, y0 / 2, '$y$', .3, .36, [(-.3, 0)])
    return G.FIG(c.svg(), 'Rectangle in a right triangle', 'Hình chữ nhật trong tam giác vuông', 300)

def o5_garden(r, lv, ctx):
    """Hình chữ nhật có một đỉnh ở góc vuông, đỉnh đối diện trên cạnh huyền: S = xy, x/a + y/b = 1 → S max = ab/4."""
    for _ in range(100):
        a, b = r.choice([8, 10, 12, 16, 20, 24]), r.choice([6, 8, 10, 12, 14, 18])
        if a != b and a * b % 4 == 0: break
    good = F(a * b, 4)
    qe = V(lv, ['A garden is a right triangle \\(ABC\\) with \\(AB=%d\\) m, \\(AC=%d\\) m (right angle at \\(A\\)). A rectangular vegetable bed has one corner at \\(A\\), two sides along \\(AB\\), \\(AC\\) and the opposite corner \\(M\\) on \\(BC\\) (see the figure). The largest area of the bed (m²) is…',
                'A triangular plot \\(ABC\\) has a right angle at \\(A\\), \\(AB=%d\\) m and \\(AC=%d\\) m. A farmer marks a rectangle with a vertex at \\(A\\) and the opposite vertex \\(M\\) on \\(BC\\) (figure). What is the greatest possible area (m²)?',
                'In the right triangle \\(ABC\\) (\\(\\widehat{A}=90^\\circ\\), \\(AB=%d\\) m, \\(AC=%d\\) m) a rectangular fish pond is dug: one vertex at \\(A\\), the opposite vertex \\(M\\) on \\(BC\\) (figure). Find the maximum area of the pond (m²).'])
    qv = V(lv, ['Một mảnh vườn hình tam giác \\(ABC\\) vuông tại \\(A\\), \\(AB=%d\\) m, \\(AC=%d\\) m. Người ta làm một luống rau hình chữ nhật có một đỉnh tại \\(A\\), hai cạnh nằm trên \\(AB\\), \\(AC\\) và đỉnh đối diện \\(M\\) nằm trên \\(BC\\) (xem hình). Diện tích lớn nhất của luống rau (m²) là…',
                'Một thửa đất hình tam giác \\(ABC\\) vuông tại \\(A\\), \\(AB=%d\\) m, \\(AC=%d\\) m. Bác nông dân rào một hình chữ nhật có một đỉnh tại \\(A\\) và đỉnh đối diện \\(M\\) thuộc \\(BC\\) (hình vẽ). Diện tích lớn nhất có thể là bao nhiêu (m²)?',
                'Trong tam giác \\(ABC\\) vuông tại \\(A\\) (\\(AB=%d\\) m, \\(AC=%d\\) m) người ta đào một ao cá hình chữ nhật: một đỉnh tại \\(A\\), đỉnh đối diện \\(M\\) thuộc \\(BC\\) (hình vẽ). Tìm diện tích lớn nhất của ao (m²).'])
    return dict(en=qe % (a, b), vi=qv % (a, b), opts=nopts(r, good, [F(a * b, 2), F(a * b, 8), F(a * b, 3), F(a + b, 1)]), fig=tri_fig(a, b),
                ee='With sides \\(x\\) on \\(AB\\) and \\(y\\) on \\(AC\\): \\(\\dfrac{x}{%d}+\\dfrac{y}{%d}=1\\), so \\(S=xy=\\dfrac{%d}{%d}x(%d-x)\\), \\(S\'=0\\Leftrightarrow x=%s\\), \\(y=%s\\), \\(S_{\\max}=%s\\).' % (a, b, b, a, a, ne(F(a, 2)), ne(F(b, 2)), ne(good)),
                ev='Gọi các cạnh là \\(x\\) (trên \\(AB\\)) và \\(y\\) (trên \\(AC\\)): \\(\\dfrac{x}{%d}+\\dfrac{y}{%d}=1\\), nên \\(S=xy=\\dfrac{%d}{%d}x(%d-x)\\), \\(S\'=0\\Leftrightarrow x=%s\\), \\(y=%s\\), \\(S_{\\max}=%s\\).' % (a, b, b, a, a, nv(F(a, 2)), nv(F(b, 2)), nv(good)))

def o5_tf_bacteria(r, lv, ctx):
    """N(t) = t³ − 3(p+q)/2·t² + 3pq·t + N0 trên [0; T]: so sánh cực đại với giá trị ở đầu mút."""
    want = r.random() < .5; kind = r.choice(['p', 'q'])
    for _ in range(400):
        p = r.choice([1, 2, 3]); q = p + r.choice([2, 4]); T = q + r.choice([1, 2, 3]); N0 = r.choice([20, 30, 40, 50])
        N = lambda t: F(t) ** 3 - F(3 * (p + q), 2) * F(t) ** 2 + 3 * p * q * F(t) + N0
        vals = {t: N(t) for t in (0, p, q, T)}
        if not (len(set(vals.values())) == 4 and all(v > 0 and v.denominator == 1 for v in vals.values())): continue
        ok = (max(vals, key=lambda t: vals[t]) == p) if kind == 'p' else (min(vals, key=lambda t: vals[t]) == q)
        if ok == want: break
    else: raise AssertionError
    tmax = max(vals, key=lambda t: vals[t])
    if kind == 'p':
        claim_t, truth = p, tmax == p
        se, sv = 'the number of bacteria is largest at \\(t=%d\\)' % p, 'số vi khuẩn lớn nhất tại thời điểm \\(t=%d\\)' % p
    else:
        tmin = min(vals, key=lambda t: vals[t]); claim_t, truth = q, tmin == q
        se, sv = 'the number of bacteria is smallest at \\(t=%d\\)' % q, 'số vi khuẩn nhỏ nhất tại thời điểm \\(t=%d\\)' % q
    b2 = F(3 * (p + q), 2); b2e, b2v = ne(b2), nv(b2)
    qe = V(lv, ['In a culture, the number of bacteria (thousands) after \\(t\\) hours is \\(N(t)=t^3-%st^2+%dt+%d\\). During \\(0\\le t\\le %d\\), %s.',
                'A lab models a bacteria colony by \\(N(t)=t^3-%st^2+%dt+%d\\) (thousand cells), \\(t\\) in hours. On the interval \\([0;\\,%d]\\), %s.',
                'The bacteria count is \\(N(t)=t^3-%st^2+%dt+%d\\) (thousands) for \\(t\\in[0;\\,%d]\\) hours. Then %s.'])
    qv = V(lv, ['Trong một môi trường nuôi cấy, số vi khuẩn (nghìn con) sau \\(t\\) giờ là \\(N(t)=t^3-%st^2+%dt+%d\\). Trong khoảng \\(0\\le t\\le %d\\), %s.',
                'Một phòng thí nghiệm mô tả đàn vi khuẩn bởi \\(N(t)=t^3-%st^2+%dt+%d\\) (nghìn con), \\(t\\) tính bằng giờ. Trên đoạn \\([0;\\,%d]\\), %s.',
                'Số vi khuẩn là \\(N(t)=t^3-%st^2+%dt+%d\\) (nghìn con) với \\(t\\in[0;\\,%d]\\) giờ. Khi đó %s.'])
    lst_e = ', '.join('\\(N(%d)=%d\\)' % (t, vals[t]) for t in (0, p, q, T)); ext = 'largest' if kind == 'p' else 'smallest'
    tt = max(vals, key=lambda t: vals[t]) if kind == 'p' else min(vals, key=lambda t: vals[t])
    return dict(en=qe % (b2e, 3 * p * q, N0, T, se), vi=qv % (b2v, 3 * p * q, N0, T, sv), truth=truth,
                ee='\\(N\'(t)=3t^2-%st+%d=3(t-%d)(t-%d)\\). Compare the critical points with the ends: %s. The %s value is at \\(t=%d\\), so the statement is %s.' % (ne(2 * b2), 3 * p * q, p, q, lst_e, ext, tt, 'true' if truth else 'false'),
                ev='\\(N\'(t)=3t^2-%st+%d=3(t-%d)(t-%d)\\). So sánh giá trị tại các điểm tới hạn và hai đầu mút: %s. Giá trị %s đạt tại \\(t=%d\\), nên mệnh đề %s.' % (nv(2 * b2), 3 * p * q, p, q, lst_e, 'lớn nhất' if kind == 'p' else 'nhỏ nhất', tt, 'đúng' if truth else 'sai'))

def wall_fig():
    c = Canvas(); W_, H_ = 4.6, 2.4
    c.poly([(0, 0), (W_, 0)], 'color=%s, line width=3pt' % G.col(G.ORANGE))
    c.poly([(0, 0), (0, H_), (W_, H_), (W_, 0)], 'color=%s, line width=1.2pt, dash pattern=on 4pt off 2pt' % G.col(G.GREEN))
    c.label(W_ / 2, 0, '$x$', .3, .36, [(0, -.32)]); c.label(W_, H_ / 2, '$y$', .3, .36, [(.32, 0)])
    return G.FIG(c.svg(), 'Rectangular yard: wall (thick) and fence (dashed)', 'Khu đất hình chữ nhật: tường (nét đậm) và lưới rào (nét đứt)', 280)

def o5_sh_wall(r, lv, ctx):
    """Chi phí = p1·x + p2·(x + 2y), xy = S → nhỏ nhất khi x = √(2p2·S/(p1+p2)), chi phí min = 2(p1+p2)x."""
    for _ in range(300):
        p1 = r.choice([3, 4, 5, 6]); p2 = r.choice([1, 2]); x0 = r.choice([10, 12, 15, 18, 20, 24, 30])
        S = F(x0 * x0 * (p1 + p2), 2 * p2)
        if S.denominator == 1 and S <= 2000: break
    else: raise AssertionError
    S = int(S); cost = F(2 * (p1 + p2) * x0, 10)       # triệu đồng (p tính theo trăm nghìn đồng/m)
    ask = 'x' if lv == 2 else 'c'
    if ask == 'c' and len(key(cost)) > 4: ask = 'x'
    good = x0 if ask == 'x' else cost
    qe = V(lv, ['A rectangular yard of area \\(%d\\ \\text{m}^2\\) is built beside a road. The side along the road (thick in the figure) is a wall costing \\(%d00\\,000\\) VND per meter; the other three sides are a fence costing \\(%d00\\,000\\) VND per meter. Find the smallest total cost (million VND).',
                'A school builds a rectangular garden of \\(%d\\ \\text{m}^2\\). One side \\(x\\) is a brick wall (\\(%d00\\,000\\) VND/m), the other three sides are wire fence (\\(%d00\\,000\\) VND/m), as in the figure. Find \\(x\\) (m) so that the cost is smallest.',
                'A parking lot shaped like a rectangle has area \\(%d\\ \\text{m}^2\\). Its front side is a wall at \\(%d00\\,000\\) VND per meter and the remaining sides are a fence at \\(%d00\\,000\\) VND per meter (figure). What is the least possible cost (million VND)?'])
    qv = V(lv, ['Một khu đất hình chữ nhật rộng \\(%d\\ \\text{m}^2\\) nằm cạnh đường. Cạnh giáp đường (nét đậm trên hình) xây tường giá \\(%d00\\,000\\) đồng/m, ba cạnh còn lại rào lưới giá \\(%d00\\,000\\) đồng/m. Tìm tổng chi phí nhỏ nhất (triệu đồng).',
                'Một trường làm vườn hình chữ nhật diện tích \\(%d\\ \\text{m}^2\\). Một cạnh dài \\(x\\) xây tường gạch (\\(%d00\\,000\\) đồng/m), ba cạnh còn lại rào lưới (\\(%d00\\,000\\) đồng/m) như hình. Tìm \\(x\\) (m) để chi phí nhỏ nhất.',
                'Một bãi đỗ xe hình chữ nhật có diện tích \\(%d\\ \\text{m}^2\\). Cạnh phía trước xây tường giá \\(%d00\\,000\\) đồng/m, các cạnh còn lại rào lưới giá \\(%d00\\,000\\) đồng/m (hình vẽ). Chi phí nhỏ nhất là bao nhiêu triệu đồng?'])
    k_ = (p1 + p2) / 10
    return dict(en=qe % (S, p1, p2), vi=qv % (S, p1, p2), key=key(good), fig=wall_fig(),
                hint=('Enter a number; use a decimal point if needed.', 'Nhập một số; dùng dấu phẩy thập phân nếu cần.'),
                ee='With \\(y=\\dfrac{%d}{x}\\): \\(C(x)=%s\\left(x+\\dfrac{%d}{x}\\right)\\) (million VND), \\(C\'(x)=0\\Leftrightarrow x^2=%d\\Leftrightarrow x=%d\\); \\(C(%d)=%s\\).' % (S, ne(F(p1 + p2, 10)), 2 * p2 * S // (p1 + p2), x0 * x0, x0, x0, ne(cost)),
                ev='Với \\(y=\\dfrac{%d}{x}\\): \\(C(x)=%s\\left(x+\\dfrac{%d}{x}\\right)\\) (triệu đồng), \\(C\'(x)=0\\Leftrightarrow x^2=%d\\Leftrightarrow x=%d\\); \\(C(%d)=%s\\).' % (S, nv(F(p1 + p2, 10)), 2 * p2 * S // (p1 + p2), x0 * x0, x0, x0, nv(cost)))

B5 = dict(A=[o5_rate_graph, o5_speed, o5_garden], B=[o5_tf_bacteria], C=[o5_sh_wall])

# ================================================================ BÀI 6 – Vectơ trong không gian
BOX6 = {'A': (0, 0, 0), 'B': (5, 0, 0), 'C': (5, 3, 0), 'D': (0, 3, 0), 'A′': (0, 0, 3), 'B′': (5, 0, 3), 'C′': (5, 3, 3), 'D′': (0, 3, 3)}
def boxfig(P, segs, alt='Rectangular box', px=260):
    cfg = {'solid': True, 'points': {k: tuple(float(x) for x in v) for k, v in P.items()}, 'segments': [list(s) for s in segs], 'px': px}
    return Q3D(cfg, alt, px=px)
ARR = {'color': '#c2410c', 'width': 3, 'arrow': True}; ARR2 = {'color': '#1d4ed8', 'width': 3, 'arrow': True}

def v6_count(r, lv, ctx):
    """Đếm vectơ (điểm đầu, điểm cuối là đỉnh hình hộp) bằng / đối với một vectơ cho trước."""
    names = list(BOX6)
    p, q = r.choice([(x, y) for x in names for y in names if x != y])
    u = sub(BOX6[q], BOX6[p]); mode = r.choice(['eq', 'op']) if lv != 1 else 'eq'
    allv = [(x, y) for x in names for y in names if x != y]
    if mode == 'eq': good = sum(1 for x, y in allv if sub(BOX6[y], BOX6[x]) == u and (x, y) != (p, q))
    else: good = sum(1 for x, y in allv if sub(BOX6[y], BOX6[x]) == mul(-1, u))
    we = 'equal to \\(%s\\) (not counting \\(%s\\) itself)' % (vv(p, q), vv(p, q)) if mode == 'eq' else 'opposite to \\(%s\\) (same length, opposite direction)' % vv(p, q)
    wv = 'bằng \\(%s\\) (không kể chính \\(%s\\))' % (vv(p, q), vv(p, q)) if mode == 'eq' else 'đối của \\(%s\\) (cùng độ dài, ngược hướng)' % vv(p, q)
    qe = V(lv, ['\\(ABCD.A′B′C′D′\\) is a parallelepiped (see the figure). How many vectors whose start and end points are vertices of it are %s?',
                'Count the vectors with both endpoints among the vertices of the parallelepiped \\(ABCD.A′B′C′D′\\) (figure) that are %s.',
                'Consider the vectors joining two vertices of the parallelepiped \\(ABCD.A′B′C′D′\\) (figure). The number of such vectors that are %s is…'])
    qv = V(lv, ['Cho hình hộp \\(ABCD.A′B′C′D′\\) (xem hình). Có bao nhiêu vectơ có điểm đầu, điểm cuối là các đỉnh của hình hộp và %s?',
                'Đếm số vectơ có điểm đầu, điểm cuối là đỉnh của hình hộp \\(ABCD.A′B′C′D′\\) (hình vẽ) và %s.',
                'Xét các vectơ nối hai đỉnh của hình hộp \\(ABCD.A′B′C′D′\\) (hình vẽ). Số vectơ %s là…'])
    kind_e = {1: 'an edge', 2: 'a face diagonal', 3: 'a space diagonal'}[sum(1 for x in u if x)]
    kind_v = {1: 'một cạnh', 2: 'một đường chéo của mặt', 3: 'một đường chéo của hình hộp'}[sum(1 for x in u if x)]
    return dict(en=qe % we, vi=qv % wv, opts=fo(str(good), [str(x) for x in (0, 1, 2, 3, 4) if x != good]), fig=boxfig(BOX6, [(p, q, ARR)], 'Parallelepiped'),
                ee='\\(%s\\) is %s; the opposite faces of a parallelepiped are parallelograms, so we list the parallel segments of the same length and keep the right direction: %d vectors.' % (vv(p, q), kind_e, good),
                ev='\\(%s\\) là %s; các mặt đối diện của hình hộp là hình bình hành nên ta liệt kê các đoạn song song, cùng độ dài rồi chọn đúng hướng: có %d vectơ.' % (vv(p, q), kind_v, good))

QUAD = [(2, 3, 6, 7), (1, 4, 8, 9), (2, 6, 9, 11), (4, 4, 7, 9), (6, 6, 7, 11), (3, 4, 12, 13), (2, 10, 11, 15), (4, 8, 8, 12), (1, 2, 2, 3), (2, 2, 1, 3)]
def v6_room_cos(r, lv, ctx):
    """Phòng hình hộp a×b×c: cos giữa hai đường chéo (vectơ) của hình hộp."""
    for _ in range(500):
        a, b, c, d = r.choice(QUAD); a, b, c = r.sample([a, b, c], 3)
        if 2 <= c <= (4 if lv != 3 else 6) and min(a, b) >= 3 and len({a, b, c}) >= 2: break
    else: raise AssertionError
    P = {'A': (0, 0, 0), 'B': (a, 0, 0), 'C': (a, b, 0), 'D': (0, b, 0), 'A′': (0, 0, c), 'B′': (a, 0, c), 'C′': (a, b, c), 'D′': (0, b, c)}
    pairs = [('A', 'C′', 'B', 'D′'), ('A', 'C′', 'D', 'B′'), ('A', 'C′', 'C', 'A′'), ('B', 'D′', 'C', 'A′')]
    p1, q1, p2, q2 = r.choice(pairs); u, w = sub(P[q1], P[p1]), sub(P[q2], P[p2]); cs = F(dot(u, w), d * d)
    if cs == 0: raise AssertionError
    qe = V(lv, ['A room is a rectangular box \\(ABCD.A′B′C′D′\\) with \\(AB=%d\\) m, \\(AD=%d\\) m, \\(AA′=%d\\) m. Two light strings are stretched along \\(%s\\) and \\(%s\\) (see the figure). Find \\(\\cos\\left(%s,%s\\right)\\).',
                'To decorate a classroom shaped like the box \\(ABCD.A′B′C′D′\\) (\\(AB=%d\\) m, \\(AD=%d\\) m, \\(AA′=%d\\) m), ribbons follow \\(%s\\) and \\(%s\\) (figure). The cosine of the angle between these two vectors is…',
                'In a hall \\(ABCD.A′B′C′D′\\) with \\(AB=%d\\) m, \\(AD=%d\\) m, height \\(AA′=%d\\) m, two cables run along \\(%s\\) and \\(%s\\) (figure). Then \\(\\cos\\left(%s,%s\\right)=\\)…'])
    qv = V(lv, ['Một căn phòng có dạng hình hộp chữ nhật \\(ABCD.A′B′C′D′\\) với \\(AB=%d\\) m, \\(AD=%d\\) m, \\(AA′=%d\\) m. Hai dây đèn trang trí được căng theo \\(%s\\) và \\(%s\\) (xem hình). Tính \\(\\cos\\left(%s,%s\\right)\\).',
                'Để trang trí một lớp học dạng hình hộp chữ nhật \\(ABCD.A′B′C′D′\\) (\\(AB=%d\\) m, \\(AD=%d\\) m, \\(AA′=%d\\) m), người ta căng dây ruy băng theo \\(%s\\) và \\(%s\\) (hình vẽ). Côsin của góc giữa hai vectơ này là…',
                'Trong một hội trường \\(ABCD.A′B′C′D′\\) có \\(AB=%d\\) m, \\(AD=%d\\) m, chiều cao \\(AA′=%d\\) m, hai sợi cáp chạy theo \\(%s\\) và \\(%s\\) (hình vẽ). Khi đó \\(\\cos\\left(%s,%s\\right)=\\)…'])
    U, W = vv(p1, q1), vv(p2, q2)
    args = (a, b, c, U, W, U, W) if lv != 2 else (a, b, c, U, W)
    bads = [-cs, F(dot(u, w), d), F(abs(dot(u, w)) + 2 * min(a, b, c) ** 2, d * d), F(1, d * d) * (a * a + b * b - c * c), 1 - cs]
    return dict(en=qe % args, vi=qv % args, opts=fo(cs, [x for x in bads if x != cs]), fig=boxfig(P, [(p1, q1, ARR), (p2, q2, ARR2)], 'Room'),
                ee='Put \\(A\\) at the origin, \\(AB\\), \\(AD\\), \\(AA′\\) on the axes: \\(%s=%s\\), \\(%s=%s\\), both of length \\(\\sqrt{%d}=%d\\). \\(\\cos=\\dfrac{%d}{%d}=%s\\).' % (U, V3(u), W, V3(w), d * d, d, dot(u, w), d * d, frt(cs)),
                ev='Đặt \\(A\\) ở gốc tọa độ, \\(AB\\), \\(AD\\), \\(AA′\\) trên các trục: \\(%s=%s\\), \\(%s=%s\\), cùng độ dài \\(\\sqrt{%d}=%d\\). \\(\\cos=\\dfrac{%d}{%d}=%s\\).' % (U, V3(u), W, V3(w), d * d, d, dot(u, w), d * d, frt(cs)))

def v6_tent(r, lv, ctx):
    """Lều dạng chóp tứ giác đều S.ABCD, tâm đáy O, OA = e, SO = h: SA·SC = h² − e², SA·SB = h²."""
    e, h = r.choice([(3, 4), (4, 3), (6, 8), (5, 12), (8, 6), (12, 5), (2, 3), (3, 2)]); kind = ['SC', 'SB', r.choice(['SC', 'SB'])][lv - 1]
    A_, B_, C_, D_, S_ = (e, 0, 0), (0, e, 0), (-e, 0, 0), (0, -e, 0), (0, 0, h)
    SA = sub(A_, S_); X = sub(C_ if kind == 'SC' else B_, S_); good = dot(SA, X)
    assert good == (h * h - e * e if kind == 'SC' else h * h)
    pts = {'A': (-e / math.sqrt(2), -e / math.sqrt(2), 0), 'B': (e / math.sqrt(2), -e / math.sqrt(2), 0), 'C': (e / math.sqrt(2), e / math.sqrt(2), 0), 'D': (-e / math.sqrt(2), e / math.sqrt(2), 0), 'S': (0, 0, float(h)), 'O': (0, 0, 0)}
    cfg = {'solid': ['S', 'A', 'B', 'C', 'D'], 'points': pts, 'segments': [['S', 'O', {'dash': True, 'width': 1.5}], ['A', 'C', {'dash': True, 'width': 1.2}], ['S', 'A', ARR], ['S', kind[1], ARR2]], 'right': [['S', 'O', 'A']], 'px': 240}
    qe = V(lv, ['A camping tent has the shape of a regular pyramid \\(S.ABCD\\); \\(O\\) is the center of the square base, \\(OA=%d\\) dm and the height \\(SO=%d\\) dm (see the figure). Find \\(\\overrightarrow{SA}\\cdot\\overrightarrow{%s}\\).',
                'The frame of a tent is a regular pyramid \\(S.ABCD\\) with base center \\(O\\), \\(OA=%d\\) dm, \\(SO=%d\\) dm (figure). The dot product \\(\\overrightarrow{SA}\\cdot\\overrightarrow{%s}\\) equals…',
                'A pyramid-shaped tent \\(S.ABCD\\) is regular; its base has center \\(O\\) with \\(OA=%d\\) dm and its pole \\(SO=%d\\) dm (figure). Then \\(\\overrightarrow{SA}\\cdot\\overrightarrow{%s}=\\)…'])
    qv = V(lv, ['Một chiếc lều cắm trại có dạng hình chóp tứ giác đều \\(S.ABCD\\); \\(O\\) là tâm của đáy, \\(OA=%d\\) dm và chiều cao \\(SO=%d\\) dm (xem hình). Tính \\(\\overrightarrow{SA}\\cdot\\overrightarrow{%s}\\).',
                'Khung một chiếc lều là hình chóp tứ giác đều \\(S.ABCD\\) có tâm đáy \\(O\\), \\(OA=%d\\) dm, \\(SO=%d\\) dm (hình vẽ). Tích vô hướng \\(\\overrightarrow{SA}\\cdot\\overrightarrow{%s}\\) bằng…',
                'Một lều hình chóp tứ giác đều \\(S.ABCD\\) có tâm đáy \\(O\\), \\(OA=%d\\) dm và cột chống \\(SO=%d\\) dm (hình vẽ). Khi đó \\(\\overrightarrow{SA}\\cdot\\overrightarrow{%s}=\\)…'])
    hyp = h * h + e * e
    return dict(en=qe % (e, h, kind), vi=qv % (e, h, kind), opts=nopts(r, good, [-good, hyp, e * e - h * h if kind == 'SB' else h * h, h * e, 2 * h * h - e * e]), fig=Q3D(cfg, 'Tent'),
                ee=('\\(\\overrightarrow{SA}\\cdot\\overrightarrow{SC}=(\\overrightarrow{SO}+\\overrightarrow{OA})\\cdot(\\overrightarrow{SO}-\\overrightarrow{OA})=SO^2-OA^2=%d-%d=%d\\).' % (h * h, e * e, good)) if kind == 'SC'
                   else '\\(\\overrightarrow{SA}\\cdot\\overrightarrow{SB}=(\\overrightarrow{SO}+\\overrightarrow{OA})\\cdot(\\overrightarrow{SO}+\\overrightarrow{OB})=SO^2+\\overrightarrow{OA}\\cdot\\overrightarrow{OB}=%d+0=%d\\) because \\(OA\\perp OB\\) and \\(SO\\) is perpendicular to the base.' % (h * h, good),
                ev=('\\(\\overrightarrow{SA}\\cdot\\overrightarrow{SC}=(\\overrightarrow{SO}+\\overrightarrow{OA})\\cdot(\\overrightarrow{SO}-\\overrightarrow{OA})=SO^2-OA^2=%d-%d=%d\\).' % (h * h, e * e, good)) if kind == 'SC'
                   else '\\(\\overrightarrow{SA}\\cdot\\overrightarrow{SB}=(\\overrightarrow{SO}+\\overrightarrow{OA})\\cdot(\\overrightarrow{SO}+\\overrightarrow{OB})=SO^2+\\overrightarrow{OA}\\cdot\\overrightarrow{OB}=%d+0=%d\\) vì \\(OA\\perp OB\\) và \\(SO\\) vuông góc với đáy.' % (h * h, good))

def v6_tf_perp(r, lv, ctx):
    names = list(CUBE1)
    cand = [(p, q) for p in names for q in names if p != q and n2(sub(CUBE1[q], CUBE1[p])) >= 2]
    want = r.random() < .5
    for _ in range(2000):
        (p, q), (s, t) = r.sample(cand, 2)
        u, w = sub(CUBE1[q], CUBE1[p]), sub(CUBE1[t], CUBE1[s])
        if len({p, q, s, t}) < 3 or u == w or u == mul(-1, w): continue
        if (dot(u, w) == 0) == want: break
    else: raise AssertionError
    truth = dot(u, w) == 0
    qe = V(lv, ['\\(ABCD.A′B′C′D′\\) is a cube (see the figure). Then \\(%s\\perp%s\\).', 'In the cube \\(ABCD.A′B′C′D′\\) (figure), the vectors \\(%s\\) and \\(%s\\) are perpendicular.', 'For the cube \\(ABCD.A′B′C′D′\\) shown in the figure: \\(%s\\cdot%s=0\\).'])
    qv = V(lv, ['Cho hình lập phương \\(ABCD.A′B′C′D′\\) (xem hình). Khi đó \\(%s\\perp%s\\).', 'Trong hình lập phương \\(ABCD.A′B′C′D′\\) (hình vẽ), hai vectơ \\(%s\\) và \\(%s\\) vuông góc với nhau.', 'Với hình lập phương \\(ABCD.A′B′C′D′\\) như hình vẽ: \\(%s\\cdot%s=0\\).'])
    return dict(en=qe % (vv(p, q), vv(s, t)), vi=qv % (vv(p, q), vv(s, t)), truth=truth, fig=boxfig(CUBE4, [(p, q, ARR), (s, t, ARR2)], 'Cube'),
                ee='Take the cube with edge 1 and \\(A\\) at the origin: \\(%s=%s\\), \\(%s=%s\\), dot product \\(%d\\), so the statement is %s.' % (vv(p, q), V3(u), vv(s, t), V3(w), dot(u, w), 'true' if truth else 'false'),
                ev='Xét hình lập phương cạnh 1, \\(A\\) ở gốc tọa độ: \\(%s=%s\\), \\(%s=%s\\), tích vô hướng bằng \\(%d\\), nên mệnh đề %s.' % (vv(p, q), V3(u), vv(s, t), V3(w), dot(u, w), 'đúng' if truth else 'sai'))

TETM = {'A': (F(-1, 5), F(3, 10), F(17, 5)), 'B': (F(-13, 5), 0, 0), 'C': (F(4, 5), -2, 0), 'D': (F(14, 5), F(8, 5), 0)}
def v6_sh_midlen(r, lv, ctx):
    """M, N trung điểm AD, BC: MN = (AB + DC)/2 → MN² = (p² + q² + 2pq·cosφ)/4."""
    opts_ = []
    for p in range(2, 13):
        for q in range(2, 13):
            for ang, cs in ((60, F(1, 2)), (90, F(0)), (120, F(-1, 2))):
                m2 = F(p * p + q * q, 4) + F(p * q, 2) * cs
                if m2.denominator == 1 and m2 > 0 and isq(int(m2)) and p != q: opts_.append((p, q, ang, cs, math.isqrt(int(m2))))
    p, q, ang, cs, mn = r.choice(opts_)
    P = dict(TETM); P['M'] = tuple((x + y) / 2 for x, y in zip(P['A'], P['D'])); P['N'] = tuple((x + y) / 2 for x, y in zip(P['B'], P['C']))
    cfg = {'solid': ['A', 'B', 'C', 'D'], 'points': {k: tuple(float(x) for x in v) for k, v in P.items()}, 'segments': [['M', 'N', {'color': '#c2410c', 'width': 3}]], 'px': 250}
    qe = V(lv, ['The tetrahedron \\(ABCD\\) has \\(AB=%d\\), \\(CD=%d\\) and the angle between \\(\\overrightarrow{AB}\\) and \\(\\overrightarrow{DC}\\) is \\(%d^\\circ\\). \\(M\\), \\(N\\) are the midpoints of \\(AD\\), \\(BC\\) (see the figure). Find \\(MN\\).',
                'In the tetrahedron \\(ABCD\\) (figure), \\(AB=%d\\), \\(CD=%d\\), \\(\\left(\\overrightarrow{AB},\\overrightarrow{DC}\\right)=%d^\\circ\\); \\(M\\) and \\(N\\) are the midpoints of \\(AD\\) and \\(BC\\). Compute the length \\(MN\\).',
                'Given a tetrahedron \\(ABCD\\) with \\(AB=%d\\), \\(CD=%d\\), the vectors \\(\\overrightarrow{AB}\\), \\(\\overrightarrow{DC}\\) form an angle of \\(%d^\\circ\\). Let \\(M\\), \\(N\\) be the midpoints of \\(AD\\), \\(BC\\) (figure). What is \\(MN\\)?'])
    qv = V(lv, ['Cho tứ diện \\(ABCD\\) có \\(AB=%d\\), \\(CD=%d\\) và góc giữa hai vectơ \\(\\overrightarrow{AB}\\), \\(\\overrightarrow{DC}\\) bằng \\(%d^\\circ\\). \\(M\\), \\(N\\) là trung điểm của \\(AD\\), \\(BC\\) (xem hình). Tính \\(MN\\).',
                'Trong tứ diện \\(ABCD\\) (hình vẽ), \\(AB=%d\\), \\(CD=%d\\), \\(\\left(\\overrightarrow{AB},\\overrightarrow{DC}\\right)=%d^\\circ\\); \\(M\\), \\(N\\) lần lượt là trung điểm của \\(AD\\), \\(BC\\). Tính độ dài \\(MN\\).',
                'Cho tứ diện \\(ABCD\\) với \\(AB=%d\\), \\(CD=%d\\), hai vectơ \\(\\overrightarrow{AB}\\), \\(\\overrightarrow{DC}\\) tạo với nhau góc \\(%d^\\circ\\). Gọi \\(M\\), \\(N\\) là trung điểm của \\(AD\\), \\(BC\\) (hình vẽ). \\(MN\\) bằng bao nhiêu?'])
    m2 = mn * mn
    return dict(en=qe % (p, q, ang), vi=qv % (p, q, ang), key=key(mn), fig=Q3D(cfg, 'Tetrahedron'),
                ee='\\(2\\overrightarrow{MN}=\\overrightarrow{AB}+\\overrightarrow{DC}\\), so \\(4MN^2=%d+%d+2\\cdot%d\\cdot%d\\cos%d^\\circ=%d\\), \\(MN^2=%d\\), \\(MN=%d\\).' % (p * p, q * q, p, q, ang, 4 * m2, m2, mn),
                ev='\\(2\\overrightarrow{MN}=\\overrightarrow{AB}+\\overrightarrow{DC}\\), nên \\(4MN^2=%d+%d+2\\cdot%d\\cdot%d\\cos%d^\\circ=%d\\), \\(MN^2=%d\\), \\(MN=%d\\).' % (p * p, q * q, p, q, ang, 4 * m2, m2, mn))

B6 = dict(A=[v6_count, v6_room_cos, v6_tent], B=[v6_tf_perp], C=[v6_sh_midlen])

# ================================================================ BÀI 7 – Hệ trục tọa độ trong không gian
def oxyz_fig(pts, segs=(), alt='Points in Oxyz', lp=None, extra_axis=4, px=280, nolabel=()):
    P = {'O': (0, 0, 0)}; P.update({k: tuple(float(x) for x in v) for k, v in pts.items()})
    L = max(max(abs(c) for c in v) for v in P.values()) + 1.5
    cfg = {'proj': 'oxyz', 'axes': True, 'axislen': max(L, extra_axis), 'points': P, 'segments': [list(s) for s in segs], 'labelpos': dict({'O': 'below left'}, **(lp or {})), 'nolabel': list(nolabel), 'px': px}
    return Q3D(cfg, alt, px=px)
DSH = {'dash': True, 'width': 1.2, 'force': True}
def far_o(*pts):
    """Hình chiếu (phép chiếu 'oxyz' của mb_tikz3d) của các điểm không sát gốc O, để nhãn không đè nhau."""
    return all(math.hypot(-0.433 * p[0] + p[1], -0.25 * p[0] + p[2]) > 1.3 for p in pts)

def c7_vec(r, lv, ctx):
    for _ in range(100):
        A = tuple(r.randint(0, 5) for _ in range(3)); B = tuple(r.randint(0, 5) for _ in range(3)); u = sub(B, A)
        if A != B and 0 not in u and len(set(map(abs, u))) == 3 and min(A + B) >= 0 and sum(1 for x in A + B if x == 0) <= 1 and far_o(A, B): break
    else: raise AssertionError
    qe = V(lv, ['In \\(Oxyz\\), \\(A%s\\) and \\(B%s\\) (see the figure). The coordinates of \\(\\overrightarrow{AB}\\) are…', 'Given \\(A%s\\), \\(B%s\\) in \\(Oxyz\\) (figure), find the coordinates of the vector \\(\\overrightarrow{AB}\\).', 'For the points \\(A%s\\) and \\(B%s\\) (figure), \\(\\overrightarrow{AB}=\\)…'])
    qv = V(lv, ['Trong không gian \\(Oxyz\\), cho \\(A%s\\) và \\(B%s\\) (xem hình). Tọa độ của \\(\\overrightarrow{AB}\\) là…', 'Cho \\(A%s\\), \\(B%s\\) trong không gian \\(Oxyz\\) (hình vẽ). Tìm tọa độ của vectơ \\(\\overrightarrow{AB}\\).', 'Với hai điểm \\(A%s\\) và \\(B%s\\) (hình vẽ), \\(\\overrightarrow{AB}=\\)…'])
    return dict(en=qe % (V3(A), V3(B)), vi=qv % (V3(A), V3(B)), opts=fo(V3(u), [V3(sub(A, B)), V3(add(A, B)), V3(tuple(abs(x) for x in u)), V3((u[1], u[0], u[2]))]),
                fig=oxyz_fig({'A': A, 'B': B}, [('A', 'B', ARR)]),
                ee='\\(\\overrightarrow{AB}=(x_B-x_A;\\,y_B-y_A;\\,z_B-z_A)=%s\\).' % V3(u), ev='\\(\\overrightarrow{AB}=(x_B-x_A;\\,y_B-y_A;\\,z_B-z_A)=%s\\).' % V3(u))

def c7_flycam(r, lv, ctx):
    """Góc phòng O; tường (Oxz), (Oyz), sàn (Oxy): khoảng cách tới (Oyz), (Oxz), (Oxy) là x, y, z."""
    d1, d2, h = r.sample([2, 3, 4, 5, 6], 3)
    good = (d1, d2, h); bads = [(d2, d1, h), (h, d2, d1), (d1, h, d2), (d2, h, d1), (h, d1, d2)]
    qe = V(lv, ['A room has a floor corner at \\(O\\); the floor is the plane \\((Oxy)\\), the two walls are \\((Oxz)\\) and \\((Oyz)\\). A flycam \\(M\\) hovers \\(%d\\) m from the wall \\((Oyz)\\), \\(%d\\) m from the wall \\((Oxz)\\) and \\(%d\\) m above the floor (see the figure). The coordinates of \\(M\\) are…',
                'In a warehouse, \\(O\\) is a floor corner, the floor is \\((Oxy)\\) and the walls are \\((Oxz)\\), \\((Oyz)\\). A lamp \\(M\\) is \\(%d\\) m from \\((Oyz)\\), \\(%d\\) m from \\((Oxz)\\) and \\(%d\\) m above the floor (figure). Find the coordinates of \\(M\\).',
                'A drone \\(M\\) flies inside a gym whose floor corner is \\(O\\) (floor \\((Oxy)\\), walls \\((Oxz)\\), \\((Oyz)\\)). It is \\(%d\\) m from \\((Oyz)\\), \\(%d\\) m from \\((Oxz)\\) and at height \\(%d\\) m (figure). Then \\(M\\) has coordinates…'])
    qv = V(lv, ['Một căn phòng có góc sàn tại \\(O\\); sàn là mặt phẳng \\((Oxy)\\), hai bức tường là \\((Oxz)\\) và \\((Oyz)\\). Một flycam \\(M\\) bay cách tường \\((Oyz)\\) \\(%d\\) m, cách tường \\((Oxz)\\) \\(%d\\) m và cách sàn \\(%d\\) m (xem hình). Tọa độ của \\(M\\) là…',
                'Trong một nhà kho, \\(O\\) là một góc sàn, sàn là \\((Oxy)\\), các bức tường là \\((Oxz)\\), \\((Oyz)\\). Một bóng đèn \\(M\\) cách \\((Oyz)\\) \\(%d\\) m, cách \\((Oxz)\\) \\(%d\\) m và cách sàn \\(%d\\) m (hình vẽ). Tìm tọa độ của \\(M\\).',
                'Một drone \\(M\\) bay trong nhà thi đấu có góc sàn \\(O\\) (sàn \\((Oxy)\\), tường \\((Oxz)\\), \\((Oyz)\\)). Drone cách \\((Oyz)\\) \\(%d\\) m, cách \\((Oxz)\\) \\(%d\\) m và ở độ cao \\(%d\\) m (hình vẽ). Khi đó \\(M\\) có tọa độ…'])
    return dict(en=qe % (d1, d2, h), vi=qv % (d1, d2, h), opts=fo(V3(good), [V3(b) for b in bads]),
                fig=oxyz_fig({'M': good, 'H': (d1, d2, 0), 'P': (d1, 0, 0), 'Q': (0, d2, 0)}, [('M', 'H', DSH), ('H', 'P', DSH), ('H', 'Q', DSH)], lp={'H': 'below'}, nolabel=['P', 'Q']),
                ee='The distance to \\((Oyz)\\) is \\(|x|\\), to \\((Oxz)\\) is \\(|y|\\), to \\((Oxy)\\) is \\(|z|\\); \\(M\\) is inside the room, so all coordinates are positive: \\(M%s\\).' % V3(good),
                ev='Khoảng cách tới \\((Oyz)\\) là \\(|x|\\), tới \\((Oxz)\\) là \\(|y|\\), tới \\((Oxy)\\) là \\(|z|\\); \\(M\\) ở trong phòng nên các tọa độ đều dương: \\(M%s\\).' % V3(good))

def c7_cube_pt(r, lv, ctx):
    a = r.choice([2, 4, 6, 8]); h = F(a, 2)
    P = {'A': (0, 0, 0), 'B': (a, 0, 0), 'C': (a, a, 0), 'D': (0, a, 0), 'A′': (0, 0, a), 'B′': (a, 0, a), 'C′': (a, a, a), 'D′': (0, a, a)}
    T = [('the center \\(I\\) of the cube', 'tâm \\(I\\) của hình lập phương', (h, h, h), ('A', 'C′')),
         ('the center \\(I\\) of the face \\(BCC′B′\\)', 'tâm \\(I\\) của mặt \\(BCC′B′\\)', (a, h, h), ('B', 'C′')),
         ('the center \\(I\\) of the face \\(A′B′C′D′\\)', 'tâm \\(I\\) của mặt \\(A′B′C′D′\\)', (h, h, a), ('A′', 'C′')),
         ('the midpoint \\(I\\) of the edge \\(C′D′\\)', 'trung điểm \\(I\\) của cạnh \\(C′D′\\)', (h, a, a), ('C′', 'D′')),
         ('the center \\(I\\) of the face \\(CDD′C′\\)', 'tâm \\(I\\) của mặt \\(CDD′C′\\)', (h, a, h), ('C', 'D′'))]
    we, wv, I, (p, q) = r.choice(T)
    bads = [(I[1], I[0], I[2]), (I[0], I[2], I[1]), (I[2], I[1], I[0]), tuple(2 * x for x in I), (h, h, h) if I != (h, h, h) else (a, a, a)]
    bads = [b for b in bads if b != I]
    P2 = dict(P); P2['I'] = I
    cfg = {'proj': 'oxyz', 'axes': True, 'solid': list(P), 'points': {k: tuple(float(x) for x in v) for k, v in P2.items()}, 'segments': [[p, q, {'width': 1.2}]], 'labelpos': {'A': 'below left'}, 'px': 280}
    qe = V(lv, ['The cube \\(ABCD.A′B′C′D′\\) has edge \\(%d\\), \\(A\\equiv O\\), \\(B\\in Ox\\), \\(D\\in Oy\\), \\(A′\\in Oz\\) (all with positive coordinates; see the figure). The coordinates of %s are…',
                'Place the cube \\(ABCD.A′B′C′D′\\) with edge \\(%d\\) in \\(Oxyz\\) so that \\(A\\) is the origin and \\(B\\), \\(D\\), \\(A′\\) lie on the positive parts of \\(Ox\\), \\(Oy\\), \\(Oz\\) (figure). Find the coordinates of %s.',
                'A cube \\(ABCD.A′B′C′D′\\) of edge \\(%d\\) sits in the corner of \\(Oxyz\\): \\(A=O\\), \\(B\\), \\(D\\), \\(A′\\) on the positive axes \\(Ox\\), \\(Oy\\), \\(Oz\\) (figure). What are the coordinates of %s?'])
    qv = V(lv, ['Hình lập phương \\(ABCD.A′B′C′D′\\) có cạnh \\(%d\\), \\(A\\equiv O\\), \\(B\\in Ox\\), \\(D\\in Oy\\), \\(A′\\in Oz\\) (các tọa độ đều không âm; xem hình). Tọa độ của %s là…',
                'Đặt hình lập phương \\(ABCD.A′B′C′D′\\) cạnh \\(%d\\) vào hệ \\(Oxyz\\) sao cho \\(A\\) là gốc tọa độ và \\(B\\), \\(D\\), \\(A′\\) nằm trên các tia \\(Ox\\), \\(Oy\\), \\(Oz\\) (hình vẽ). Tìm tọa độ của %s.',
                'Một hình lập phương \\(ABCD.A′B′C′D′\\) cạnh \\(%d\\) đặt ở góc hệ \\(Oxyz\\): \\(A\\) trùng \\(O\\); \\(B\\), \\(D\\), \\(A′\\) nằm trên các tia \\(Ox\\), \\(Oy\\), \\(Oz\\) (hình vẽ). Tọa độ của %s là…'])
    return dict(en=qe % (a, we), vi=qv % (a, wv), opts=fo(V3(I), [V3(b) for b in bads]), fig=Q3D(cfg, 'Cube in Oxyz', px=280),
                ee='\\(B(%d;0;0)\\), \\(D(0;%d;0)\\), \\(A′(0;0;%d)\\); \\(I\\) is the midpoint of \\(%s%s\\) with \\(%s%s\\), \\(%s%s\\), so \\(I%s\\).' % (a, a, a, p, q, p, V3(P[p]), q, V3(P[q]), V3(I)),
                ev='\\(B(%d;0;0)\\), \\(D(0;%d;0)\\), \\(A′(0;0;%d)\\); \\(I\\) là trung điểm của \\(%s%s\\) với \\(%s%s\\), \\(%s%s\\), nên \\(I%s\\).' % (a, a, a, p, q, p, V3(P[p]), q, V3(P[q]), V3(I)))

def c7_tf_plane(r, lv, ctx):
    M = tuple(r.sample([1, 2, 3, 4, 5, 6], 3))
    pl = r.choice(['Oxy', 'Oyz', 'Oxz']); idx = {'Oxy': 2, 'Oyz': 0, 'Oxz': 1}[pl]; right = abs(M[idx])
    truth = r.random() < .5
    val = right if truth else r.choice([abs(M[i]) for i in range(3) if i != idx])
    H = list(M); H[idx] = 0
    qe = V(lv, ['The distance from \\(M%s\\) to the plane \\((%s)\\) equals \\(%d\\).', 'In \\(Oxyz\\), the point \\(M%s\\) is at distance \\(%d\\) from the plane \\((%s)\\) (\\(H\\) is the foot of the perpendicular, see the figure).', '\\(d\\left(M,(%s)\\right)=%d\\) for \\(M%s\\) (see the figure).'])
    qv = V(lv, ['Khoảng cách từ \\(M%s\\) đến mặt phẳng \\((%s)\\) bằng \\(%d\\).', 'Trong không gian \\(Oxyz\\), điểm \\(M%s\\) cách mặt phẳng \\((%s)\\) một khoảng bằng \\(%d\\) (\\(H\\) là hình chiếu vuông góc, xem hình).', '\\(d\\left(M,(%s)\\right)=%d\\) với \\(M%s\\) (xem hình).'])
    args = {1: (V3(M), pl, val), 2: (V3(M), val, pl), 3: (pl, val, V3(M))}[lv]
    argv = {1: (V3(M), pl, val), 2: (V3(M), pl, val), 3: (pl, val, V3(M))}[lv]
    ax = {'Oxy': 'z', 'Oyz': 'x', 'Oxz': 'y'}[pl]
    return dict(en=qe % args, vi=qv % argv, truth=truth, fig=oxyz_fig({'M': M, 'H': tuple(H)}, [('M', 'H', DSH)], lp={'H': 'below'}),
                ee='The plane \\((%s)\\) is \\(%s=0\\), so \\(d=|%s_M|=%d\\). The statement is %s.' % (pl, ax, ax, right, 'true' if truth else 'false'),
                ev='Mặt phẳng \\((%s)\\) có phương trình \\(%s=0\\), nên \\(d=|%s_M|=%d\\). Mệnh đề %s.' % (pl, ax, ax, right, 'đúng' if truth else 'sai'))

def c7_sh_move(r, lv, ctx):
    """Biết A và vectơ dịch chuyển AB → tìm một tọa độ của B (tính ngược)."""
    for _ in range(100):
        A = tuple(r.randint(1, 6) for _ in range(3)); u = tuple(r.randint(-5, 5) for _ in range(3)); B = add(A, u)
        if 0 not in u and len(set(u)) == 3 and min(B) >= 1 and max(B) <= 7 and far_o(A, B): break
    else: raise AssertionError
    k = r.choice([0, 1, 2]); nm = 'xyz'[k]
    if lv == 3: k, nm = None, 'sum'
    good = sum(B) if k is None else B[k]
    qe = V(lv, ['A crane moves a crate from \\(A%s\\) by the displacement vector \\(\\overrightarrow{AB}=%s\\) (meters, see the figure). Find the \\(%s\\)-coordinate of the new position \\(B\\).',
                'A delivery drone starts at \\(A%s\\) and flies along \\(\\overrightarrow{AB}=%s\\) (figure). What is the \\(%s\\)-coordinate of the point \\(B\\) it reaches?',
                'Given \\(A%s\\) and \\(\\overrightarrow{AB}=%s\\) (figure), find \\(x_B+y_B+z_B\\).'])
    qv = V(lv, ['Một cần cẩu di chuyển kiện hàng từ vị trí \\(A%s\\) theo vectơ dịch chuyển \\(\\overrightarrow{AB}=%s\\) (đơn vị mét, xem hình). Tìm %s của vị trí mới \\(B\\).',
                'Một drone giao hàng xuất phát từ \\(A%s\\) và bay theo vectơ \\(\\overrightarrow{AB}=%s\\) (hình vẽ). Tìm %s của điểm \\(B\\) mà drone tới được.',
                'Cho \\(A%s\\) và \\(\\overrightarrow{AB}=%s\\) (hình vẽ). Tính \\(x_B+y_B+z_B\\).'])
    tv = {'x': 'hoành độ', 'y': 'tung độ', 'z': 'cao độ'}
    args_e = (V3(A), V3(u)) + ((nm,) if lv != 3 else ()); args_v = (V3(A), V3(u)) + ((tv.get(nm, ''),) if lv != 3 else ())
    cfg_pts = {'A': A, 'B': B}
    return dict(en=qe % args_e, vi=qv % args_v, key=key(good), fig=oxyz_fig(cfg_pts, [('A', 'B', ARR)], 'Displacement in Oxyz'),
                ee='\\(\\overrightarrow{AB}=(x_B-x_A;\\,y_B-y_A;\\,z_B-z_A)\\Rightarrow B=A+\\overrightarrow{AB}=%s\\)%s.' % (V3(B), ', so \\(x_B+y_B+z_B=%d\\)' % good if k is None else ''),
                ev='\\(\\overrightarrow{AB}=(x_B-x_A;\\,y_B-y_A;\\,z_B-z_A)\\Rightarrow B=A+\\overrightarrow{AB}=%s\\)%s.' % (V3(B), ', nên \\(x_B+y_B+z_B=%d\\)' % good if k is None else ''))

B7 = dict(A=[c7_vec, c7_flycam, c7_cube_pt], B=[c7_tf_plane], C=[c7_sh_move])

# ================================================================ BÀI 8 – Biểu thức tọa độ của các phép toán vectơ

BASE = (4, 4, 4)
def vecfig(vs, segs):
    """Các vectơ vẽ từ cùng một điểm gốc K(4; 4; 4) trong hệ Oxyz (vectơ tự do: độ dài, hướng đúng; tọa độ điểm đầu không ảnh hưởng)."""
    P = {'O': (0, 0, 0), 'K': BASE}; P.update({k: add(BASE, v) for k, v in vs.items()})
    assert all(min(p) >= 0 for p in P.values())
    return {'proj': 'oxyz', 'axes': True, 'axislen': max(max(p) for p in P.values()) + 1.5, 'points': {k: tuple(float(x) for x in v) for k, v in P.items()},
            'segments': segs, 'nolabel': [k for k in P if k not in ('O',)], 'labelpos': {'O': 'below left'}, 'px': 280}
def pr(m, n, lang='en'): return '\\(m=%s,\\ n=%s\\)' % (frt(m), frt(n))
def c8_collinear(r, lv, ctx):
    """a = (p; m; q), b = (kp; s; n) cùng phương ⇔ b = k·a ⇒ m = s/k, n = kq."""
    for _ in range(200):
        p = nz(r, -4, 4); q = nz(r, -4, 4); k = r.choice([2, 3, -2, -1, F(1, 2)]); s = r.choice([x for x in range(-8, 9) if x])
        m = F(s) / k; n = F(k * q)
        if m.denominator == 1 and n.denominator == 1 and F(k * p).denominator == 1 and abs(k * p) <= 9: break
    else: raise AssertionError
    bp = k * p
    good = pr(m, n); bads = [pr(s * k, F(q) / k), pr(-m, n), pr(m, -n), pr(F(s) / k * -1, -n), pr(s, q)]
    bads = [b for b in dict.fromkeys(bads) if b != good]
    qe = V(lv, ['\\(\\vec a=(%d;\\,m;\\,%d)\\) and \\(\\vec b=(%s;\\,%d;\\,n)\\) are collinear when…', 'Find \\(m\\), \\(n\\) so that \\(\\vec a=(%d;\\,m;\\,%d)\\) and \\(\\vec b=(%s;\\,%d;\\,n)\\) have the same or opposite directions.', 'The vectors \\(\\vec a=(%d;\\,m;\\,%d)\\), \\(\\vec b=(%s;\\,%d;\\,n)\\) are parallel exactly when…'])
    qv = V(lv, ['Hai vectơ \\(\\vec a=(%d;\\,m;\\,%d)\\) và \\(\\vec b=(%s;\\,%d;\\,n)\\) cùng phương khi…', 'Tìm \\(m\\), \\(n\\) để hai vectơ \\(\\vec a=(%d;\\,m;\\,%d)\\) và \\(\\vec b=(%s;\\,%d;\\,n)\\) cùng phương.', 'Hai vectơ \\(\\vec a=(%d;\\,m;\\,%d)\\), \\(\\vec b=(%s;\\,%d;\\,n)\\) cùng phương khi và chỉ khi…'])
    args = (p, q, frt(bp), s)
    return dict(en=qe % args, vi=qv % args, opts=[good] + bads[:3],
                ee='The first coordinates give \\(\\vec b=%s\\,\\vec a\\). Then \\(%d=%s\\cdot m\\Rightarrow m=%s\\) and \\(n=%s\\cdot%d=%s\\).' % (frt(k), s, frt(k), frt(m), frt(k), q, frt(n)),
                ev='Từ hoành độ: \\(\\vec b=%s\\,\\vec a\\). Khi đó \\(%d=%s\\cdot m\\Rightarrow m=%s\\) và \\(n=%s\\cdot%d=%s\\).' % (frt(k), s, frt(k), frt(m), frt(k), q, frt(n)))

def c8_work(r, lv, ctx):
    for _ in range(300):
        Fv = tuple(r.randint(-6, 8) for _ in range(3)); A = tuple(r.randint(1, 5) for _ in range(3)); B = tuple(r.randint(1, 6) for _ in range(3)); d = sub(B, A)
        W = dot(Fv, d)
        if W > 0 and 0 not in d and n2(Fv) and W != dot(Fv, B) and W != dot(Fv, A) and far_o(A, B): break
    else: raise AssertionError
    qe = V(lv, ['A constant force \\(\\vec F=%s\\) (N) moves a box in a straight line from \\(A%s\\) to \\(B%s\\) (meters, see the figure). The work \\(W=\\vec F\\cdot\\overrightarrow{AB}\\) (J) is…',
                'A robot arm pushes an object from \\(A%s\\) to \\(B%s\\) (m) with a constant force \\(\\vec F=%s\\) (N), as in the figure. How much work (J) does the force do?',
                'Under the constant force \\(\\vec F=%s\\) (N), a cart moves from \\(A%s\\) to \\(B%s\\) (m) (figure). Find the work of \\(\\vec F\\) (J).'])
    qv = V(lv, ['Một lực không đổi \\(\\vec F=%s\\) (N) làm một thùng hàng di chuyển thẳng từ \\(A%s\\) đến \\(B%s\\) (đơn vị mét, xem hình). Công \\(W=\\vec F\\cdot\\overrightarrow{AB}\\) (J) bằng…',
                'Một cánh tay robot đẩy vật từ \\(A%s\\) đến \\(B%s\\) (m) bằng lực không đổi \\(\\vec F=%s\\) (N) như hình. Lực thực hiện công bằng bao nhiêu jun?',
                'Dưới tác dụng của lực không đổi \\(\\vec F=%s\\) (N), một xe đẩy đi từ \\(A%s\\) đến \\(B%s\\) (m) (hình vẽ). Tính công của lực \\(\\vec F\\) (J).'])
    args = (V3(Fv), V3(A), V3(B)) if lv != 2 else (V3(A), V3(B), V3(Fv))
    return dict(en=qe % args, vi=qv % args, opts=nopts(r, W, [dot(Fv, B), -W, dot(Fv, add(A, B)), sum(Fv) * sum(d)]), fig=oxyz_fig({'A': A, 'B': B}, [('A', 'B', ARR)], 'Displacement AB'),
                ee='\\(\\overrightarrow{AB}=%s\\), \\(W=%s=%d\\).' % (V3(d), '+'.join('(%d)\\cdot(%d)' % (x, y) for x, y in zip(Fv, d)), W),
                ev='\\(\\overrightarrow{AB}=%s\\), \\(W=%s=%d\\).' % (V3(d), '+'.join('(%d)\\cdot(%d)' % (x, y) for x, y in zip(Fv, d)), W))

def c8_combo(r, lv, ctx):
    """c = x·a + y·b: giải hệ hai phương trình rồi kiểm tra phương trình thứ ba."""
    for _ in range(500):
        a = tuple(r.randint(-3, 3) for _ in range(3)); b = tuple(r.randint(-3, 3) for _ in range(3)); x, y = nz(r, -3, 3), nz(r, -3, 3)
        if a[0] * b[1] - a[1] * b[0] == 0 or 0 in a or x == y: continue
        c = add(mul(x, a), mul(y, b))
        if 0 not in c and all(abs(v) <= 4 for v in c): break
    else: raise AssertionError
    ask = 'sum' if lv != 1 else 'pair'
    if ask == 'pair':
        good = '\\(x=%d,\\ y=%d\\)' % (x, y); bads = ['\\(x=%d,\\ y=%d\\)' % t for t in ((y, x), (-x, y), (x, -y), (-x, -y)) if t != (x, y)]
        opts = [good] + list(dict.fromkeys(bads))[:3]
    else:
        opts = nopts(r, x + y, [x - y, y - x, x * y, -(x + y)])
    qe = V(lv, ['\\(\\vec a=%s\\), \\(\\vec b=%s\\), \\(\\vec c=%s\\) (see the figure). The numbers \\(x\\), \\(y\\) with \\(\\vec c=x\\vec a+y\\vec b\\) are…', 'Given \\(\\vec a=%s\\), \\(\\vec b=%s\\), \\(\\vec c=%s\\) (figure), and \\(\\vec c=x\\vec a+y\\vec b\\). Find \\(x+y\\).', 'Write \\(\\vec c=%s\\) as \\(x\\vec a+y\\vec b\\) with \\(\\vec a=%s\\), \\(\\vec b=%s\\) (figure). Then \\(x+y=\\)…'])
    qv = V(lv, ['Cho \\(\\vec a=%s\\), \\(\\vec b=%s\\), \\(\\vec c=%s\\) (xem hình). Các số \\(x\\), \\(y\\) thỏa mãn \\(\\vec c=x\\vec a+y\\vec b\\) là…', 'Cho \\(\\vec a=%s\\), \\(\\vec b=%s\\), \\(\\vec c=%s\\) (hình vẽ) và \\(\\vec c=x\\vec a+y\\vec b\\). Tính \\(x+y\\).', 'Biểu diễn \\(\\vec c=%s\\) dưới dạng \\(x\\vec a+y\\vec b\\) với \\(\\vec a=%s\\), \\(\\vec b=%s\\) (hình vẽ). Khi đó \\(x+y=\\)…'])
    args = (V3(a), V3(b), V3(c)) if lv != 3 else (V3(c), V3(a), V3(b))
    cfg = vecfig({'P': a, 'Q': b, 'R': c}, [['K', 'P', ARR], ['K', 'Q', ARR2], ['K', 'R', {'color': '#15803d', 'width': 3, 'arrow': True}]])
    lab_e = '<p style="text-align:center;font-size:.9em">%s</p>' % 'Orange: \\(\\vec a\\); blue: \\(\\vec b\\); green: \\(\\vec c\\).'
    lab_v = '<p style="text-align:center;font-size:.9em">%s</p>' % 'Cam: \\(\\vec a\\); xanh dương: \\(\\vec b\\); xanh lá: \\(\\vec c\\).'
    fe, fv = Q3D(cfg, 'Vectors a, b, c from O', px=280)
    return dict(en=qe % args, vi=qv % args, opts=opts, fig=(fe + lab_e, fv + lab_v),
                ee='From the first two coordinates: \\(%dx%+dy=%d\\), \\(%dx%+dy=%d\\Rightarrow x=%d,\\ y=%d\\); check the third: \\(%d\\cdot%d%+d\\cdot%d=%d\\).%s' % (a[0], b[0], c[0], a[1], b[1], c[1], x, y, a[2], x, b[2], y, c[2], '' if ask == 'pair' else ' So \\(x+y=%d\\).' % (x + y)),
                ev='Từ hai tọa độ đầu: \\(%dx%+dy=%d\\), \\(%dx%+dy=%d\\Rightarrow x=%d,\\ y=%d\\); kiểm tra tọa độ thứ ba: \\(%d\\cdot%d%+d\\cdot%d=%d\\).%s' % (a[0], b[0], c[0], a[1], b[1], c[1], x, y, a[2], x, b[2], y, c[2], '' if ask == 'pair' else ' Vậy \\(x+y=%d\\).' % (x + y)))

def c8_tf_closer(r, lv, ctx):
    for _ in range(500):
        A = tuple(r.randint(0, 5) for _ in range(2)) + (r.randint(2, 5),); B = tuple(r.randint(0, 5) for _ in range(2)) + (r.randint(2, 5),); Mh = tuple(r.randint(1, 5) for _ in range(2)) + (0,)
        da, db = n2(sub(A, Mh)), n2(sub(B, Mh))
        if A != B and da != db and abs(da - db) <= 12 and far_o(A, B, Mh) and math.hypot(-0.433 * (A[0] - B[0]) + A[1] - B[1], -0.25 * (A[0] - B[0]) + A[2] - B[2]) > 1.2: break
    else: raise AssertionError
    claimA = r.random() < .5; truth = (da < db) == claimA
    near = 'A' if claimA else 'B'
    qe = V(lv, ['Two Wi-Fi routers are at \\(A%s\\) and \\(B%s\\) (meters) and a laptop is at \\(M%s\\) (see the figure). The laptop is closer to the router at \\(%s\\).',
                'In a library, two signal boosters are placed at \\(A%s\\), \\(B%s\\) and a reader sits at \\(M%s\\) (figure). Then \\(M\\) is nearer to \\(%s\\) than to the other booster.',
                'Lamps hang at \\(A%s\\) and \\(B%s\\) above a desk at \\(M%s\\) (figure). The desk is closer to lamp \\(%s\\).'])
    qv = V(lv, ['Hai bộ phát Wi-Fi đặt tại \\(A%s\\) và \\(B%s\\) (đơn vị mét), một máy tính xách tay ở \\(M%s\\) (xem hình). Máy tính ở gần bộ phát \\(%s\\) hơn.',
                'Trong thư viện, hai bộ khuếch đại sóng đặt tại \\(A%s\\), \\(B%s\\) và một bạn đọc ngồi ở \\(M%s\\) (hình vẽ). Khi đó \\(M\\) gần \\(%s\\) hơn bộ còn lại.',
                'Hai bóng đèn treo tại \\(A%s\\) và \\(B%s\\) phía trên một bàn học tại \\(M%s\\) (hình vẽ). Bàn học gần đèn \\(%s\\) hơn.'])
    args = (V3(A), V3(B), V3(Mh), near)
    return dict(en=qe % args, vi=qv % args, truth=truth, fig=oxyz_fig({'A': A, 'B': B, 'M': Mh}, [('M', 'A', DSH), ('M', 'B', DSH)], 'Two points and M'),
                ee='\\(MA^2=%d\\), \\(MB^2=%d\\), so \\(M\\) is closer to \\(%s\\). The statement is %s.' % (da, db, 'A' if da < db else 'B', 'true' if truth else 'false'),
                ev='\\(MA^2=%d\\), \\(MB^2=%d\\), nên \\(M\\) gần \\(%s\\) hơn. Mệnh đề %s.' % (da, db, 'A' if da < db else 'B', 'đúng' if truth else 'sai'))

def c8_sh_angle(r, lv, ctx):
    """Góc giữa hai ống (vectơ chỉ phương), làm tròn đến độ; tránh giá trị sát ,5 và góc đặc biệt."""
    for _ in range(2000):
        u = tuple(r.randint(-4, 4) for _ in range(3)); w = tuple(r.randint(-4, 4) for _ in range(3))
        if not n2(u) or not n2(w) or 0 in u: continue
        cs = dot(u, w) / math.sqrt(n2(u) * n2(w))
        if abs(cs) > .98: continue
        ang = math.degrees(math.acos(cs)); fr = ang - math.floor(ang)
        if .1 < fr < .4 or .6 < fr < .9:
            if round(ang) not in (30, 45, 60, 90, 120, 135, 150): break
    else: raise AssertionError
    good = round(ang)
    qe = V(lv, ['Two straight pipes leave the same point in the directions \\(\\vec u=%s\\) and \\(\\vec v=%s\\) (see the figure). Find the angle between \\(\\vec u\\) and \\(\\vec v\\) in degrees, rounded to the nearest degree.',
                'Two steel bars of a roof frame point along \\(\\vec u=%s\\) and \\(\\vec v=%s\\) (figure). Compute the angle \\((\\vec u,\\vec v)\\) (degrees, round to a whole number).',
                'Two laser beams start at one point with directions \\(\\vec u=%s\\), \\(\\vec v=%s\\) (figure). What is the angle between them, to the nearest degree?'])
    qv = V(lv, ['Hai đường ống thẳng xuất phát từ cùng một điểm theo hướng \\(\\vec u=%s\\) và \\(\\vec v=%s\\) (xem hình). Tính góc giữa \\(\\vec u\\) và \\(\\vec v\\) theo độ (làm tròn đến hàng đơn vị).',
                'Hai thanh thép của khung mái hướng theo \\(\\vec u=%s\\) và \\(\\vec v=%s\\) (hình vẽ). Tính góc \\((\\vec u,\\vec v)\\) (độ, làm tròn đến số nguyên).',
                'Hai tia laser xuất phát từ một điểm với hướng \\(\\vec u=%s\\), \\(\\vec v=%s\\) (hình vẽ). Góc giữa hai tia bằng bao nhiêu độ (làm tròn đến độ)?'])
    cfg = vecfig({'P': u, 'Q': w}, [['K', 'P', ARR], ['K', 'Q', ARR2]])
    fe, fv = Q3D(cfg, 'Two direction vectors', px=280)
    lab_e = '<p style="text-align:center;font-size:.9em">Orange: \\(\\vec u\\); blue: \\(\\vec v\\).</p>'; lab_v = '<p style="text-align:center;font-size:.9em">Cam: \\(\\vec u\\); xanh dương: \\(\\vec v\\).</p>'
    cse = '%.4f' % cs
    return dict(en=qe % (V3(u), V3(w)), vi=qv % (V3(u), V3(w)), key=key(good), fig=(fe + lab_e, fv + lab_v), hint=('Enter a whole number of degrees.', 'Nhập số độ (số nguyên).'),
                ee='\\(\\cos(\\vec u,\\vec v)=\\dfrac{%d}{\\sqrt{%d}\\cdot\\sqrt{%d}}\\approx%s\\), so the angle \\(\\approx%d^\\circ\\).' % (dot(u, w), n2(u), n2(w), cse, good),
                ev='\\(\\cos(\\vec u,\\vec v)=\\dfrac{%d}{\\sqrt{%d}\\cdot\\sqrt{%d}}\\approx%s\\), nên góc \\(\\approx%d^\\circ\\).' % (dot(u, w), n2(u), n2(w), cse.replace('.', '{,}'), good))

B8 = dict(A=[c8_collinear, c8_work, c8_combo], B=[c8_tf_closer], C=[c8_sh_angle])
