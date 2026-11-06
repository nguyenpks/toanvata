# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 11 – Bài 12 (đường thẳng và mặt phẳng song song), Bài 13 (hai mặt phẳng song song), Bài 14 (phép chiếu song song).
Đếm cạnh song song/nằm trong/cắt mặt phẳng bằng tọa độ nguyên (tích có hướng, tích vô hướng) – chính xác, không đếm tay."""
from fractions import Fraction as F
from mb_selfpractice import pick_opts, fr
from mb_lib import TI
from sp_g11c import SOL, edges, _cross, _dot, _sub

def TT(en, vi): return '§' + TI(en, vi)
STEMS = [('Which statement is true?', 'Khẳng định nào sau đây đúng?'), ('Choose the correct statement.', 'Chọn khẳng định đúng.'), ('Which of the following is correct?', 'Mệnh đề nào sau đây là đúng?'), ('Which sentence is always true?', 'Phát biểu nào sau đây luôn đúng?')]
# ---------- hình khối và mặt phẳng (tọa độ nguyên) ----------
FACES = {'cube': ['ABCD', 'A′B′C′D′', 'ABB′A′', 'BCC′B′', 'ACC′A′', 'BDD′B′'], 'box': ['ABCD', 'A′B′C′D′', 'ABB′A′', 'ADD′A′', 'ACC′A′'],
         'prism': ['ABC', 'A′B′C′', 'ABB′A′', 'BCC′B′'], 'pyr': ['ABCD', 'SAB', 'SCD', 'SAC'], 'tetra': ['ABC', 'BCD', 'ACD']}
def pts_of(name_plane):
    out, i = [], 0
    while i < len(name_plane):
        if i + 1 < len(name_plane) and name_plane[i + 1] == '′': out.append(name_plane[i:i + 2]); i += 2
        else: out.append(name_plane[i]); i += 1
    return out
def plane_rel(solid, plane):
    """Trả (số cạnh song song, số cạnh nằm trong, số cạnh cắt) với mặt phẳng plane của khối solid."""
    P = SOL[solid][0]; ps = pts_of(plane); A, B, C = (P[ps[0]], P[ps[1]], P[ps[2]]); n = _cross(_sub(B, A), _sub(C, A))
    on = lambda X: _dot(_sub(X, A), n) == 0
    par = inn = cut = 0
    for e in edges(solid):
        X, Y = P[e[0]], P[e[1]]
        if on(X) and on(Y): inn += 1
        elif _dot(_sub(Y, X), n) == 0: par += 1
        else: cut += 1
    return par, inn, cut
NM = {'cube': ('the cube \\(ABCD.A′B′C′D′\\)', 'hình lập phương \\(ABCD.A′B′C′D′\\)'), 'box': ('the rectangular box \\(ABCD.A′B′C′D′\\)', 'hình hộp chữ nhật \\(ABCD.A′B′C′D′\\)'),
      'prism': ('the triangular prism \\(ABC.A′B′C′\\)', 'hình lăng trụ tam giác \\(ABC.A′B′C′\\)'), 'pyr': ('the pyramid \\(S.ABCD\\) with a square base', 'hình chóp \\(S.ABCD\\) có đáy là hình vuông'), 'tetra': ('the tetrahedron \\(ABCD\\)', 'tứ diện \\(ABCD\\)')}
def lp_count(r, lv):
    solid = r.choice(list(FACES)); plane = r.choice(FACES[solid]); par, inn, cut = plane_rel(solid, plane)
    if par == 0: raise AssertionError
    return dict(en='How many edges of %s are parallel to the plane \\((%s)\\)?' % (NM[solid][0], plane), vi='Có bao nhiêu cạnh của %s song song với mặt phẳng \\((%s)\\)?' % (NM[solid][1], plane),
      opts=pick_opts(r, str(par), [str(par + inn), str(inn), str(cut), str(par + 1)], fill=lambda k: str(par + 2 * k)), ans=0,
      ee='An edge is parallel to the plane when it is not in the plane and is parallel to a line in it: %d edge(s); %d lie in the plane.' % (par, inn), ev='Cạnh song song với mặt phẳng khi không nằm trong mặt phẳng và song song với một đường thẳng nằm trong nó: %d cạnh; còn %d cạnh nằm trong mặt phẳng.' % (par, inn))
def lp_cut(r, lv):
    solid = r.choice(list(FACES)); plane = r.choice(FACES[solid]); par, inn, cut = plane_rel(solid, plane)
    if cut == 0: raise AssertionError
    return dict(en='How many lines containing an edge of %s meet the plane \\((%s)\\) at exactly one point?' % (NM[solid][0], plane), vi='Có bao nhiêu đường thẳng chứa cạnh của %s cắt mặt phẳng \\((%s)\\) (có đúng một điểm chung)?' % (NM[solid][1], plane),
      opts=pick_opts(r, str(cut), [str(par), str(cut + inn), str(inn), str(cut - 1)], fill=lambda k: str(cut + 2 * k)), ans=0,
      ee='Edges: %d parallel, %d in the plane, %d cutting it.' % (par, inn, cut), ev='Các cạnh: %d song song, %d nằm trong, %d cắt mặt phẳng.' % (par, inn, cut))
def lp_thales(r, lv):
    p, q = r.choice([(1, 2), (1, 3), (2, 3), (1, 4), (3, 4), (2, 5), (3, 5)]); L = q * r.choice([2, 3, 4, 5, 6]); x = F(p * L, q)
    seg = r.choice([('AB', 'BC', 'AC'), ('SA', 'AB', 'SB'), ('DA', 'AC', 'DC')])
    a, b, c = seg; P0 = a[0]
    return dict(en='In a tetrahedron, \\(M\\in %s\\) with \\(%sM=\\dfrac{%d}{%d}%s\\). A plane through \\(M\\) parallel to \\(%s\\) cuts \\(%s\\) at \\(N\\). If \\(%s=%d\\), then \\(MN=\\)…' % (a, P0, p, q, a, b, c, b, L),
      vi='Trong một tứ diện, điểm \\(M\\in %s\\) với \\(%sM=\\dfrac{%d}{%d}%s\\). Mặt phẳng qua \\(M\\) song song với \\(%s\\) cắt \\(%s\\) tại \\(N\\). Nếu \\(%s=%d\\) thì \\(MN=\\)…' % (a, P0, p, q, a, b, c, b, L),
      opts=pick_opts(r, fr(x), [fr(F((q - p) * L, q)), fr(F(L, 2)), str(L), fr(F(q * L, p))], fill=lambda k: fr(x + k)), ans=0,
      ee='The plane cuts \\((%s)\\) along \\(MN\\parallel %s\\); by Thales, \\(MN=\\dfrac{%d}{%d}\\cdot%d=%s\\).' % (a + c[1], b, p, q, L, fr(x)), ev='Mặt phẳng cắt \\((%s)\\) theo \\(MN\\parallel %s\\); theo Thalès, \\(MN=\\dfrac{%d}{%d}\\cdot%d=%s\\).' % (a + c[1], b, p, q, L, fr(x)))
ST12 = [  # (đúng?, en, vi)
 (True, 'If \\(a\\not\\subset(P)\\) and \\(a\\parallel b\\) with \\(b\\subset(P)\\), then \\(a\\parallel(P)\\).', 'Nếu \\(a\\not\\subset(P)\\) và \\(a\\parallel b\\) với \\(b\\subset(P)\\) thì \\(a\\parallel(P)\\).'),
 (True, 'If \\(a\\parallel(P)\\) and a plane \\((Q)\\) through \\(a\\) cuts \\((P)\\) along \\(b\\), then \\(b\\parallel a\\).', 'Nếu \\(a\\parallel(P)\\) và mặt phẳng \\((Q)\\) chứa \\(a\\) cắt \\((P)\\) theo giao tuyến \\(b\\) thì \\(b\\parallel a\\).'),
 (True, 'Two intersecting planes both parallel to a line \\(d\\) meet along a line parallel to \\(d\\).', 'Hai mặt phẳng cắt nhau cùng song song với đường thẳng \\(d\\) thì giao tuyến của chúng song song với \\(d\\).'),
 (False, 'If \\(a\\parallel(P)\\), then \\(a\\) is parallel to every line in \\((P)\\).', 'Nếu \\(a\\parallel(P)\\) thì \\(a\\) song song với mọi đường thẳng nằm trong \\((P)\\).'),
 (False, 'If two lines are parallel to the same plane, then they are parallel.', 'Hai đường thẳng cùng song song với một mặt phẳng thì song song với nhau.'),
 (False, 'If \\(a\\parallel b\\) and \\(b\\subset(P)\\), then always \\(a\\parallel(P)\\).', 'Nếu \\(a\\parallel b\\) và \\(b\\subset(P)\\) thì luôn có \\(a\\parallel(P)\\).')]
def lp_theory(r, lv):
    tr = r.choice([s for s in ST12 if s[0]]); fa = r.sample([s for s in ST12 if not s[0]], 3)
    st = r.choice(STEMS)
    return dict(en=st[0], vi=st[1], opts=[TT(tr[1], tr[2])] + [TT(s[1], s[2]) for s in fa], ans=0,
      ee='The false ones: a line parallel to \\((P)\\) may be skew to lines in \\((P)\\); two lines parallel to one plane may meet or be skew; \\(a\\) may lie in \\((P)\\).', ev='Các khẳng định sai: đường thẳng song song với \\((P)\\) có thể chéo nhau với đường thẳng trong \\((P)\\); hai đường cùng song song với một mặt phẳng có thể cắt nhau hoặc chéo nhau; \\(a\\) có thể nằm trong \\((P)\\).')
def fd(x, comma=True):
    """Số thập phân hữu hạn: dấu phẩy (tiếng Việt, comma=True) hoặc dấu chấm."""
    x = F(x); t = str(x.numerator) if x.denominator == 1 else ('%.6f' % float(x)).rstrip('0')
    return t.replace('.', '{,}') if comma else t
def lp_ceiling(r, lv):
    h = r.choice([3, F(32, 10), F(28, 10), F(35, 10)]); d = r.choice([F(5, 10), F(4, 10), F(8, 10)]); k = h - d
    return dict(en='A straight LED tube is hung parallel to the floor, \\(%s\\) m below the ceiling. The room is \\(%s\\) m high (the ceiling is parallel to the floor). How far above the floor is every point of the tube?' % (fd(d, False), fd(h, False)),
      vi='Một bóng đèn LED dạng ống thẳng được treo song song với sàn nhà, cách trần \\(%s\\) m. Phòng cao \\(%s\\) m (trần song song với sàn). Mọi điểm của bóng đèn cách sàn bao nhiêu mét?' % (fd(d), fd(h)),
      opts=pick_opts(r, '%s\\ \\text{m}' % fd(k), ['%s\\ \\text{m}' % fd(x) for x in (h + d, d, h, k - F(1, 10))]), ans=0,
      ee='The tube is parallel to the floor, so all its points are at the same height: \\(%s-%s=%s\\).' % (fd(h, False), fd(d, False), fd(k, False)), ev='Bóng đèn song song với sàn nên mọi điểm cách sàn như nhau: \\(%s-%s=%s\\).' % (fd(h), fd(d), fd(k)))
def lp_mid(r, lv):
    L = r.choice([6, 8, 10, 12, 14, 16, 20]); which = r.choice([('S.ABCD', 'SA', 'SB', 'AB', '(SCD)'), ('ABCD', 'AB', 'AC', 'BC', '(BCD)'), ('S.ABC', 'SB', 'SC', 'BC', '(ABC)')])
    sol, s1, s2, base, pl = which
    return dict(en='In %s, \\(M\\), \\(N\\) are the midpoints of \\(%s\\), \\(%s\\) and \\(%s=%d\\). Which is correct?' % (sol, s1, s2, base, L), vi='Trong %s, \\(M\\), \\(N\\) là trung điểm của \\(%s\\), \\(%s\\) và \\(%s=%d\\). Khẳng định nào đúng?' % (sol, s1, s2, base, L),
      opts=[TT('\\(MN\\parallel %s\\) and \\(MN=%d\\)' % (base, L // 2), '\\(MN\\parallel %s\\) và \\(MN=%d\\)' % (base, L // 2)), TT('\\(MN\\parallel %s\\) and \\(MN=%d\\)' % (base, L), '\\(MN\\parallel %s\\) và \\(MN=%d\\)' % (base, L)),
            TT('\\(MN\\) cuts \\(%s\\) and \\(MN=%d\\)' % (base, L // 2), '\\(MN\\) cắt \\(%s\\) và \\(MN=%d\\)' % (base, L // 2)), TT('\\(MN\\) and \\(%s\\) are skew' % base, '\\(MN\\) và \\(%s\\) chéo nhau' % base)], ans=0,
      ee='\\(MN\\) is a midline: \\(MN\\parallel %s\\), \\(MN=\\dfrac{%d}{2}\\); hence \\(MN\\) is parallel to every plane containing \\(%s\\) but not \\(MN\\).' % (base, L, base), ev='\\(MN\\) là đường trung bình: \\(MN\\parallel %s\\), \\(MN=\\dfrac{%d}{2}\\); do đó \\(MN\\) song song với mọi mặt phẳng chứa \\(%s\\) mà không chứa \\(MN\\).' % (base, L, base))
M12S11 = [lp_count, lp_thales, lp_theory, lp_cut, lp_mid, lp_ceiling, lp_count, lp_thales]

# ================= Bài 13. Hai mặt phẳng song song =================
def pp_thales(r, lv):
    a, b = r.choice([(2, 3), (3, 5), (4, 6), (3, 4), (5, 2), (6, 9), (4, 10)]); k = r.choice([F(3, 2), 2, F(1, 2), 3, F(5, 2), F(4, 3)]); c = a * k; x = b * k
    if F(c).denominator != 1: raise AssertionError
    ctx = r.choice([('Three parallel floors of a building cut a straight rope at \\(A,B,C\\) and a straight cable at \\(A′,B′,C′\\).', 'Ba sàn nhà song song cắt một sợi dây thẳng tại \\(A,B,C\\) và một dây cáp thẳng tại \\(A′,B′,C′\\).'),
                    ('Three parallel planes \\((P)\\parallel(Q)\\parallel(R)\\) cut two lines at \\(A,B,C\\) and \\(A′,B′,C′\\).', 'Ba mặt phẳng song song \\((P)\\parallel(Q)\\parallel(R)\\) cắt hai đường thẳng lần lượt tại \\(A,B,C\\) và \\(A′,B′,C′\\).')])
    return dict(en='%s \\(AB=%d\\), \\(BC=%d\\), \\(A′B′=%s\\). Then \\(B′C′=\\)…' % (ctx[0], a, b, fr(c)), vi='%s \\(AB=%d\\), \\(BC=%d\\), \\(A′B′=%s\\). Khi đó \\(B′C′=\\)…' % (ctx[1], a, b, fr(c)),
      opts=pick_opts(r, fr(x), [fr(F(a * b) / c), fr(c + b - a), fr(F(b) / k), fr(x + 1)], fill=lambda k_: fr(x + k_)), ans=0,
      ee='Thales in space: \\(\\dfrac{AB}{A′B′}=\\dfrac{BC}{B′C′}\\Rightarrow B′C′=\\dfrac{%d\\cdot%s}{%d}=%s\\).' % (b, fr(c), a, fr(x)), ev='Định lí Thalès trong không gian: \\(\\dfrac{AB}{A′B′}=\\dfrac{BC}{B′C′}\\Rightarrow B′C′=\\dfrac{%d\\cdot%s}{%d}=%s\\).' % (b, fr(c), a, fr(x)))
def pp_prism(r, lv):
    n = r.choice([3, 4, 5, 6, 7, 8]); kind = r.choice(['faces', 'edges', 'lat', 'verts'])
    v = {'faces': n + 2, 'edges': 3 * n, 'lat': n, 'verts': 2 * n}[kind]; w = {'faces': ('faces', 'mặt'), 'edges': ('edges', 'cạnh'), 'lat': ('lateral edges', 'cạnh bên'), 'verts': ('vertices', 'đỉnh')}[kind]
    return dict(en='A prism has a base with %d sides. How many %s does it have?' % (n, w[0]), vi='Một hình lăng trụ có đáy là đa giác %d cạnh. Hình lăng trụ đó có bao nhiêu %s?' % (n, w[1]),
      opts=pick_opts(r, str(v), [str(x) for x in (n + 2, 3 * n, n, 2 * n, n + 1, 2 * n + 2) if x != v]), ans=0,
      ee='An \\(n\\)-gonal prism has \\(n\\) lateral edges, \\(3n\\) edges, \\(2n\\) vertices and \\(n+2\\) faces.', ev='Lăng trụ \\(n\\)-giác có \\(n\\) cạnh bên, \\(3n\\) cạnh, \\(2n\\) đỉnh và \\(n+2\\) mặt.')
def pp_frustum(r, lv):
    p, q = r.choice([(1, 2), (1, 3), (2, 3), (3, 4), (2, 5), (3, 5)]); L = q * r.choice([2, 3, 4, 5]); x = F(p * L, q)
    return dict(en='A plane parallel to the base of the pyramid \\(S.ABCD\\) cuts \\(SA, SB, SC, SD\\) at \\(A′,B′,C′,D′\\) with \\(\\dfrac{SA′}{SA}=\\dfrac{%d}{%d}\\). If \\(AB=%d\\), the edge \\(A′B′\\) of the frustum is…' % (p, q, L),
      vi='Một mặt phẳng song song với đáy của hình chóp \\(S.ABCD\\) cắt \\(SA, SB, SC, SD\\) tại \\(A′,B′,C′,D′\\) với \\(\\dfrac{SA′}{SA}=\\dfrac{%d}{%d}\\). Nếu \\(AB=%d\\) thì cạnh \\(A′B′\\) của hình chóp cụt bằng…' % (p, q, L),
      opts=pick_opts(r, fr(x), [fr(F((q - p) * L, q)), fr(F(q * L, p)), fr(F(L, 2)) if x != F(L, 2) else fr(F(L, 3)), str(L)], fill=lambda k: fr(x + k)), ans=0,
      ee='\\(A′B′\\parallel AB\\) and \\(\\dfrac{A′B′}{AB}=\\dfrac{SA′}{SA}=\\dfrac{%d}{%d}\\): \\(A′B′=%s\\).' % (p, q, fr(x)), ev='\\(A′B′\\parallel AB\\) và \\(\\dfrac{A′B′}{AB}=\\dfrac{SA′}{SA}=\\dfrac{%d}{%d}\\): \\(A′B′=%s\\).' % (p, q, fr(x)))
ST13 = [
 (True, 'If \\((P)\\) contains two intersecting lines that are both parallel to \\((Q)\\), then \\((P)\\parallel(Q)\\).', 'Nếu \\((P)\\) chứa hai đường thẳng cắt nhau cùng song song với \\((Q)\\) thì \\((P)\\parallel(Q)\\).'),
 (True, 'If \\((P)\\parallel(Q)\\) and \\((R)\\) cuts \\((P)\\) along \\(a\\), then \\((R)\\) cuts \\((Q)\\) along a line \\(b\\parallel a\\).', 'Nếu \\((P)\\parallel(Q)\\) và \\((R)\\) cắt \\((P)\\) theo giao tuyến \\(a\\) thì \\((R)\\) cắt \\((Q)\\) theo giao tuyến \\(b\\parallel a\\).'),
 (True, 'If \\((P)\\parallel(Q)\\), then every line in \\((P)\\) is parallel to \\((Q)\\).', 'Nếu \\((P)\\parallel(Q)\\) thì mọi đường thẳng nằm trong \\((P)\\) đều song song với \\((Q)\\).'),
 (False, 'If \\((P)\\) contains two lines parallel to \\((Q)\\), then \\((P)\\parallel(Q)\\).', 'Nếu \\((P)\\) chứa hai đường thẳng song song với \\((Q)\\) thì \\((P)\\parallel(Q)\\).'),
 (False, 'If \\((P)\\parallel(Q)\\), \\(a\\subset(P)\\), \\(b\\subset(Q)\\), then \\(a\\parallel b\\).', 'Nếu \\((P)\\parallel(Q)\\), \\(a\\subset(P)\\), \\(b\\subset(Q)\\) thì \\(a\\parallel b\\).'),
 (False, 'Through a point outside \\((Q)\\) there are infinitely many planes parallel to \\((Q)\\).', 'Qua một điểm nằm ngoài \\((Q)\\) có vô số mặt phẳng song song với \\((Q)\\).')]
def pp_theory(r, lv):
    tr = r.choice([s for s in ST13 if s[0]]); fa = r.sample([s for s in ST13 if not s[0]], 3)
    st = r.choice(STEMS)
    return dict(en=st[0], vi=st[1], opts=[TT(tr[1], tr[2])] + [TT(s[1], s[2]) for s in fa], ans=0,
      ee='The two lines must intersect; lines in two parallel planes may be skew; through a point there is exactly one parallel plane.', ev='Hai đường thẳng phải cắt nhau; hai đường thẳng nằm trên hai mặt phẳng song song có thể chéo nhau; qua một điểm có đúng một mặt phẳng song song.')
def pp_planes_box(r, lv):
    solid = r.choice(['cube', 'box']); face = r.choice(['ABCD', 'ABB′A′', 'ADD′A′', 'BCC′B′']); opp = {'ABCD': 'A′B′C′D′', 'ABB′A′': 'DCC′D′', 'ADD′A′': 'BCC′B′', 'BCC′B′': 'ADD′A′'}[face]
    wrong = [x for x in ['A′B′C′D′', 'DCC′D′', 'BCC′B′', 'ADD′A′', 'ABB′A′', 'ACC′A′'] if x not in (opp, face)]
    return dict(en='In %s, which plane is parallel to \\((%s)\\)?' % (NM[solid][0], face), vi='Trong %s, mặt phẳng nào song song với \\((%s)\\)?' % (NM[solid][1], face),
      opts=pick_opts(r, '(%s)' % opp, ['(%s)' % x for x in r.sample(wrong, 3)]), ans=0,
      ee='Opposite faces of a box lie in parallel planes.', ev='Hai mặt đối diện của hình hộp nằm trên hai mặt phẳng song song.')
def pp_shelf(r, lv):
    n = r.choice([4, 5, 6, 7]); g = r.choice([30, 32, 35, 40]); t = r.choice([2, 3])
    H = (n - 1) * g + n * t
    return dict(en='A bookcase has %d shelves (boards) of thickness %d cm, all parallel to the floor; the gap between two neighbouring shelves is %d cm. From the bottom of the lowest board to the top of the highest board is…' % (n, t, g),
      vi='Một giá sách có %d tấm kệ dày %d cm, đều song song với sàn; khoảng hở giữa hai kệ liền nhau là %d cm. Khoảng cách từ mặt dưới kệ thấp nhất đến mặt trên kệ cao nhất là…' % (n, t, g),
      opts=pick_opts(r, '%d\\ \\text{cm}' % H, ['%d\\ \\text{cm}' % x for x in (n * g + n * t, (n - 1) * g, (n - 1) * (g + t), n * (g + t) + t)]), ans=0,
      ee='\\(%d\\) boards and \\(%d\\) gaps: \\(%d\\cdot%d+%d\\cdot%d=%d\\).' % (n, n - 1, n, t, n - 1, g, H), ev='\\(%d\\) tấm kệ và \\(%d\\) khoảng hở: \\(%d\\cdot%d+%d\\cdot%d=%d\\).' % (n, n - 1, n, t, n - 1, g, H))
M13S11 = [pp_thales, pp_prism, pp_frustum, pp_theory, pp_planes_box, pp_shelf, pp_thales, pp_frustum]

# ================= Bài 14. Phép chiếu song song =================
def pj_ratio(r, lv):
    p, q = r.choice([(1, 2), (1, 3), (2, 3), (1, 4), (3, 5), (2, 5)]); L = (p + q) * r.choice([1, 2, 3, 4]); x = F(p * L, p + q)
    return dict(en='\\(M\\) lies on segment \\(AB\\) with \\(\\dfrac{AM}{MB}=\\dfrac{%d}{%d}\\). Under a parallel projection, \\(A,B,M\\) go to \\(A′,B′,M′\\) and \\(A′B′=%d\\). Then \\(A′M′=\\)…' % (p, q, L),
      vi='Điểm \\(M\\) thuộc đoạn \\(AB\\) với \\(\\dfrac{AM}{MB}=\\dfrac{%d}{%d}\\). Qua một phép chiếu song song, \\(A,B,M\\) có hình chiếu \\(A′,B′,M′\\) và \\(A′B′=%d\\). Khi đó \\(A′M′=\\)…' % (p, q, L),
      opts=pick_opts(r, fr(x), [fr(F(q * L, p + q)), fr(F(p * L, q)), fr(F(L, 2)) if x != F(L, 2) else fr(F(L, 3)), str(L)], fill=lambda k: fr(x + k)), ans=0,
      ee='Parallel projection keeps the ratio on a line: \\(\\dfrac{A′M′}{A′B′}=\\dfrac{AM}{AB}=\\dfrac{%d}{%d}\\).' % (p, p + q), ev='Phép chiếu song song giữ nguyên tỉ số trên một đường thẳng: \\(\\dfrac{A′M′}{A′B′}=\\dfrac{AM}{AB}=\\dfrac{%d}{%d}\\).' % (p, p + q))
def pj_shadow(r, lv):
    h1, s1 = r.choice([(F(15, 10), 2), (2, F(25, 10)), (1, F(12, 10)), (F(16, 10), 2), (F(18, 10), F(24, 10))]); k = r.choice([4, 5, 6, F(15, 2), 3])
    h2 = h1 * k; s2 = s1 * k
    f = lambda v: fr(v) if F(v).denominator == 1 else str(float(v)).replace('.', '{,}')
    return dict(en='Sunlight is a parallel projection. At the same moment, a vertical stick %s m high casts a shadow %s m long on flat ground, and a vertical flagpole casts a shadow %s m long. The flagpole is…' % (f(h1).replace('{,}', '.'), f(s1).replace('{,}', '.'), f(s2).replace('{,}', '.')),
      vi='Ánh nắng mặt trời là một phép chiếu song song. Cùng một thời điểm, chiếc cọc thẳng đứng cao %s m có bóng dài %s m trên mặt đất phẳng, còn cột cờ thẳng đứng có bóng dài %s m. Cột cờ cao…' % (f(h1).replace('{,}', ','), f(s1).replace('{,}', ','), f(s2).replace('{,}', ',')),
      opts=pick_opts(r, '%s\\ \\text{m}' % f(h2), ['%s\\ \\text{m}' % f(v) for v in (s2 * s1 / h1, s2 - s1 + h1, s2, h2 + 1)]), ans=0,
      ee='Parallel segments keep their ratio: \\(\\dfrac{h}{%s}=\\dfrac{%s}{%s}\\), so \\(h=%s\\) m.' % (f(s2), f(h1), f(s1), f(h2)), ev='Hai đoạn song song giữ tỉ số: \\(\\dfrac{h}{%s}=\\dfrac{%s}{%s}\\) nên \\(h=%s\\) m.' % (f(s2), f(h1), f(s1), f(h2)))
SHAPES = [('a square', 'hình vuông', 'a parallelogram', 'hình bình hành'), ('a rectangle', 'hình chữ nhật', 'a parallelogram', 'hình bình hành'), ('a circle', 'đường tròn', 'an ellipse', 'đường elip'),
          ('an isosceles trapezoid', 'hình thang cân', 'a trapezoid', 'hình thang'), ('a regular hexagon', 'lục giác đều', 'a hexagon with three pairs of parallel opposite sides', 'lục giác có ba cặp cạnh đối song song')]
def pj_shape(r, lv):
    s = r.choice(SHAPES); others = [(x[2], x[3]) for x in SHAPES if x[2] != s[2]] + [('always a square', 'luôn là hình vuông'), ('always a rectangle', 'luôn là hình chữ nhật'), ('a triangle', 'tam giác')]
    others = list(dict.fromkeys(others)); r.shuffle(others)
    return dict(en='In a drawing of a solid (a parallel projection), %s is usually drawn as…' % s[0],
      vi='Trong hình biểu diễn của một hình không gian (phép chiếu song song), %s thường được vẽ thành…' % s[1],
      opts=[TT(s[2], s[3])] + [TT(a, b) for a, b in others[:3]], ans=0,
      ee='Parallel projection keeps parallelism and ratios on parallel segments, but not angles or lengths.', ev='Phép chiếu song song giữ tính song song và tỉ số các đoạn thẳng song song, nhưng không giữ góc và độ dài.')
PROP = [(True, 'parallelism of lines (not parallel to the direction)', 'tính song song của hai đường thẳng (không song song với phương chiếu)'), (True, 'the ratio of two segments on one line', 'tỉ số hai đoạn thẳng nằm trên một đường thẳng'),
        (True, 'the midpoint of a segment', 'trung điểm của đoạn thẳng'), (True, 'the order of three points on a line', 'thứ tự ba điểm trên một đường thẳng'),
        (False, 'the size of an angle', 'số đo của góc'), (False, 'the length of a segment', 'độ dài đoạn thẳng'), (False, 'a right angle', 'góc vuông'), (False, 'the shape of a circle', 'hình dạng đường tròn')]
def pj_notkept(r, lv):
    bad = r.choice([p for p in PROP if not p[0]]); good = r.sample([p for p in PROP if p[0]], 3)
    st = r.choice([('Which property is <b>not</b> always kept by a parallel projection?', 'Phép chiếu song song <b>không</b> luôn giữ nguyên tính chất nào sau đây?'), ('A parallel projection may change which of the following?', 'Qua phép chiếu song song, yếu tố nào sau đây có thể bị thay đổi?'), ('Which of these is <b>not</b> preserved by every parallel projection?', 'Yếu tố nào sau đây <b>không</b> được bảo toàn qua mọi phép chiếu song song?')])
    return dict(en=st[0], vi=st[1], opts=[TT(bad[1], bad[2])] + [TT(p[1], p[2]) for p in good], ans=0,
      ee='Angles and lengths can change; parallelism, midpoints and ratios on a line are kept.', ev='Góc và độ dài có thể thay đổi; tính song song, trung điểm và tỉ số trên một đường thẳng được giữ nguyên.')
def pj_par(r, lv):
    k = r.choice([2, 3, F(1, 2), F(3, 2), F(2, 3), 4]); x = r.choice([2, 3, 4, 6, 8]); y = k * x
    if F(y).denominator != 1: raise AssertionError
    return dict(en='\\(ABCD\\) is a trapezoid with \\(AB\\parallel CD\\) and \\(AB=%s\\,CD\\). Its image under a parallel projection is \\(A′B′C′D′\\) with \\(C′D′=%d\\). Then \\(A′B′=\\)…' % (fr(k), x),
      vi='Hình thang \\(ABCD\\) có \\(AB\\parallel CD\\), \\(AB=%s\\,CD\\). Hình chiếu song song của nó là \\(A′B′C′D′\\) với \\(C′D′=%d\\). Khi đó \\(A′B′=\\)…' % (fr(k), x),
      opts=pick_opts(r, fr(y), [str(x), fr(F(x) / k), fr(y + x), fr(y + 1)], fill=lambda k_: fr(y + 2 * k_)), ans=0,
      ee='The images of parallel segments keep their ratio: \\(A′B′=%s\\cdot%d=%s\\).' % (fr(k), x, fr(y)), ev='Hình chiếu của hai đoạn song song giữ nguyên tỉ số: \\(A′B′=%s\\cdot%d=%s\\).' % (fr(k), x, fr(y)))
def pj_centroid(r, lv):
    obj = r.choice([('the centroid \\(G\\) of triangle \\(ABC\\)', 'trọng tâm \\(G\\) của tam giác \\(ABC\\)', 'the centroid of triangle \\(A′B′C′\\)', 'trọng tâm tam giác \\(A′B′C′\\)'),
                    ('the midpoint \\(I\\) of \\(AB\\)', 'trung điểm \\(I\\) của \\(AB\\)', 'the midpoint of \\(A′B′\\)', 'trung điểm của \\(A′B′\\)'),
                    ('the centre \\(O\\) of the parallelogram \\(ABCD\\)', 'tâm \\(O\\) của hình bình hành \\(ABCD\\)', 'the centre of the parallelogram \\(A′B′C′D′\\)', 'tâm hình bình hành \\(A′B′C′D′\\)')])
    wrong = [('the orthocentre of the image', 'trực tâm của hình chiếu'), ('the circumcentre of the image', 'tâm đường tròn ngoại tiếp hình chiếu'), ('a point that cannot be determined', 'một điểm không xác định được')]
    return dict(en='Under a parallel projection (plane of the figure not parallel to the direction), the image of %s is…' % obj[0], vi='Qua phép chiếu song song (mặt phẳng chứa hình không song song với phương chiếu), hình chiếu của %s là…' % obj[1],
      opts=[TT(obj[2], obj[3])] + [TT(a, b) for a, b in wrong], ans=0, ee='Midpoints and ratios on a line are kept, so medians go to medians and diagonals to diagonals.', ev='Trung điểm và tỉ số trên một đường thẳng được giữ nên trung tuyến biến thành trung tuyến, đường chéo thành đường chéo.')
M14S11 = [pj_ratio, pj_shadow, pj_shape, pj_notkept, pj_par, pj_centroid, pj_ratio, pj_par]
