# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 11 – Bài 25 (hai mặt phẳng vuông góc), Bài 26 (khoảng cách), Bài 27 (thể tích).
Đáp án lấy từ bảng đã kiểm chứng hoặc tính chính xác (Fraction, căn thức rút gọn)."""
import math
from fractions import Fraction as F
from mb_selfpractice import pick_opts, fr
from sp_g11f import TT
from sp_g10h import surd, rt
from sp_g11h import DEG, degs, CUBE, co, rq

TRIP = [(3, 4, 5), (4, 3, 5), (6, 8, 10), (8, 6, 10), (5, 12, 13), (12, 5, 13), (9, 12, 15), (8, 15, 17)]

# ================= Bài 25. Hai mặt phẳng vuông góc =================
def v_sqdih(r, lv):
    k = r.randint(2, 9); kind = r.choice([('%d\\sqrt3' % k, 60), (str(k), 45), (rq(k, 3, 3), 30)])
    return dict(en='\\(S.ABCD\\): square base of side %d, \\(SA\\perp(ABCD)\\), \\(SA=%s\\). The angle between \\((SBC)\\) and \\((ABCD)\\) is…' % (k, kind[0]), vi='Hình chóp \\(S.ABCD\\) có đáy là hình vuông cạnh %d, \\(SA\\perp(ABCD)\\), \\(SA=%s\\). Góc giữa hai mặt phẳng \\((SBC)\\) và \\((ABCD)\\) bằng…' % (k, kind[0]),
      opts=pick_opts(r, DEG(kind[1]), degs(kind[1], (30, 45, 60, 90))), ans=0,
      ee='\\(BC\\perp(SAB)\\): the angle is \\(\\widehat{SBA}\\), \\(\\tan=\\dfrac{SA}{AB}\\).', ev='\\(BC\\perp AB\\), \\(BC\\perp SB\\) nên góc cần tìm là \\(\\widehat{SBA}\\) với \\(\\tan\\widehat{SBA}=\\dfrac{SA}{AB}\\).')


def v_reg4(r, lv):
    k = 2 * r.randint(1, 5); kind = r.choice([(rq(k, 2, 3), 60), (rq(k, 2, 1) if False else str(k // 2), 45), (rq(k, 6, 3), 30)])
    return dict(en='Regular pyramid \\(S.ABCD\\): base side %d, height \\(SO=%s\\). The angle between a lateral face and the base is…' % (k, kind[0]), vi='Hình chóp tứ giác đều \\(S.ABCD\\) có cạnh đáy %d, chiều cao \\(SO=%s\\). Góc giữa mặt bên và mặt đáy bằng…' % (k, kind[0]),
      opts=pick_opts(r, DEG(kind[1]), degs(kind[1], (30, 45, 60, 90))), ans=0,
      ee='With \\(M\\) the midpoint of \\(CD\\): \\(\\tan\\widehat{SMO}=\\dfrac{SO}{OM}\\), \\(OM=%d\\).' % (k // 2), ev='Gọi \\(M\\) là trung điểm \\(CD\\): góc cần tìm là \\(\\widehat{SMO}\\), \\(\\tan\\widehat{SMO}=\\dfrac{SO}{OM}\\) với \\(OM=%d\\).' % (k // 2))


def v_reg3(r, lv):
    k = 6 * r.randint(1, 2); kind = r.choice([(str(k // 2), 60), (rq(k, 6, 3), 45), (str(k // 6), 30)])
    return dict(en='Regular pyramid \\(S.ABC\\): base side %d, height \\(SO=%s\\). The angle between a lateral face and the base is…' % (k, kind[0]), vi='Hình chóp tam giác đều \\(S.ABC\\) có cạnh đáy %d, chiều cao \\(SO=%s\\). Góc giữa mặt bên và mặt đáy bằng…' % (k, kind[0]),
      opts=pick_opts(r, DEG(kind[1]), degs(kind[1], (30, 45, 60, 90))), ans=0,
      ee='\\(OM=\\dfrac{a\\sqrt3}{6}=%s\\) (\\(M\\) the midpoint of \\(BC\\)).' % rq(k, 6, 3), ev='\\(OM=\\dfrac{a\\sqrt3}{6}=%s\\) (\\(M\\) là trung điểm \\(BC\\)); \\(\\tan\\widehat{SMO}=\\dfrac{SO}{OM}\\).' % rq(k, 6, 3))


PERP_PL = [('(SAB)', '(ABCD)', ['(SBC)', '(SCD)', '(SBD)']), ('(SAD)', '(ABCD)', ['(SBC)', '(SCD)', '(SBD)']), ('(SAC)', '(SBD)', ['(SAB)', '(SBC)', '(SCD)']), ('(SAB)', '(SBC)', ['(SCD)', '(SAC)', '(SBD)']), ('(SAD)', '(SCD)', ['(SBC)', '(SAC)', '(SBD)'])]


def v_which(r, lv):
    h = r.randint(2, 9); p, q, bad = r.choice(PERP_PL)
    return dict(en='\\(S.ABCD\\): square base, \\(SA\\perp(ABCD)\\), \\(SA=%d\\). Which plane is perpendicular to \\(%s\\)?' % (h, q), vi='Hình chóp \\(S.ABCD\\) có đáy là hình vuông, \\(SA\\perp(ABCD)\\), \\(SA=%d\\). Mặt phẳng nào vuông góc với mặt phẳng \\(%s\\)?' % (h, q),
      opts=pick_opts(r, p, bad), ans=0, ee='One plane must contain a line perpendicular to the other.', ev='Hai mặt phẳng vuông góc khi một mặt chứa một đường thẳng vuông góc với mặt kia (ví dụ \\(SA\\), \\(BC\\), \\(CD\\), \\(BD\\)).')


def v_apothem(r, lv):
    h, half, sm = r.choice(TRIP)
    return dict(en='Regular pyramid \\(S.ABCD\\): base side %d, height %d. The slant height \\(SM\\) (\\(M\\) the midpoint of \\(CD\\)) is…' % (2 * half, h), vi='Hình chóp tứ giác đều \\(S.ABCD\\) có cạnh đáy %d, chiều cao %d. Trung đoạn \\(SM\\) (\\(M\\) là trung điểm \\(CD\\)) bằng…' % (2 * half, h),
      opts=pick_opts(r, str(sm), [rt(h * h + 4 * half * half), rt(h * h + 2 * half * half), str(h + half), rt(abs(h * h - half * half)) if h != half else '1']), ans=0,
      ee='\\(SM=\\sqrt{SO^2+OM^2}\\), \\(OM=%d\\).' % half, ev='\\(SO\\perp OM\\): \\(SM=\\sqrt{SO^2+OM^2}=\\sqrt{%d+%d}=%d\\).' % (h * h, half * half, sm))


def v_cube(r, lv):
    a = r.randint(2, 9)
    return dict(en='Cube \\(%s\\) with edge %d. The angle \\(\\varphi\\) between \\((A\'BD)\\) and \\((ABCD)\\) satisfies…' % (CUBE, a), vi='Hình lập phương \\(%s\\) cạnh %d. Góc \\(\\varphi\\) giữa hai mặt phẳng \\((A\'BD)\\) và \\((ABCD)\\) thỏa mãn…' % (CUBE, a),
      opts=pick_opts(r, '\\tan\\varphi=\\sqrt2', ['\\tan\\varphi=\\dfrac{\\sqrt2}{2}', '\\varphi=45^\\circ', '\\varphi=60^\\circ', '\\tan\\varphi=\\sqrt3']), ans=0,
      ee='With \\(O=AC\\cap BD\\): \\(\\varphi=\\widehat{A\'OA}\\), \\(\\tan\\varphi=\\dfrac{AA\'}{AO}\\).', ev='Gọi \\(O=AC\\cap BD\\): \\(BD\\perp(AA\'O)\\) nên \\(\\varphi=\\widehat{A\'OA}\\), \\(\\tan\\varphi=\\dfrac{a}{\\frac{a\\sqrt2}{2}}=\\sqrt2\\).')


def v_roof(r, lv):
    rise, half, sl = r.choice(TRIP); w = 2 * half
    return dict(en='A gable roof covers a house %d m wide; the ridge is %d m above the eaves. If \\(\\varphi\\) is the angle between a roof plane and the horizontal ceiling, then \\(\\cos\\varphi=\\)…' % (w, rise), vi='Mái nhà hai mái che một ngôi nhà rộng %d m; nóc mái cao hơn mép mái %d m. Gọi \\(\\varphi\\) là góc giữa một mặt mái và mặt trần nằm ngang. Khi đó \\(\\cos\\varphi=\\)…' % (w, rise),
      opts=pick_opts(r, fr(F(half, sl)), [fr(F(rise, sl)), fr(F(half, rise)), fr(F(rise, half)), fr(F(w, sl + w))]), ans=0,
      ee='In the cross-section: half-width %d, rise %d, slope %d.' % (half, rise, sl), ev='Xét mặt cắt vuông góc với nóc: nửa bề rộng %d m, chiều cao %d m, mái dài %d m; \\(\\cos\\varphi=\\dfrac{%d}{%d}\\).' % (half, rise, sl, half, sl))


M25S11 = [v_sqdih, v_reg4, v_reg3, v_which, v_apothem, v_cube, v_roof, v_sqdih]

# ================= Bài 26. Khoảng cách =================
def k_asbc(r, lv):
    h, a, s = r.choice(TRIP)
    return dict(en='\\(S.ABCD\\): square base of side %d, \\(SA\\perp(ABCD)\\), \\(SA=%d\\). The distance from \\(A\\) to \\((SBC)\\) is…' % (a, h), vi='Hình chóp \\(S.ABCD\\) có đáy là hình vuông cạnh %d, \\(SA\\perp(ABCD)\\), \\(SA=%d\\). Khoảng cách từ \\(A\\) đến mặt phẳng \\((SBC)\\) bằng…' % (a, h),
      opts=pick_opts(r, fr(F(h * a, s)), [str(h), str(a), fr(F(h * a, h + a)), fr(F(s, 2))]), ans=0,
      ee='\\(AH\\perp SB\\): \\(AH=\\dfrac{SA\\cdot AB}{SB}\\).', ev='Kẻ \\(AH\\perp SB\\); vì \\(BC\\perp(SAB)\\) nên \\(AH\\perp(SBC)\\): \\(AH=\\dfrac{SA\\cdot AB}{SB}=\\dfrac{%d\\cdot%d}{%d}\\).' % (h, a, s))


CUBE_D = [("A", "(BDD'B')", '\\dfrac{a\\sqrt2}{2}', 'distance to the diagonal plane = half the diagonal \\(AC\\)', 'khoảng cách bằng \\(AO=\\frac12AC\\)'),
          ("AA'", 'BD', '\\dfrac{a\\sqrt2}{2}', '\\(AO\\) is the common perpendicular', '\\(AO\\) là đoạn vuông góc chung'),
          ('AB', "CC'", 'a', '\\(BC\\) is the common perpendicular', '\\(BC\\) là đoạn vuông góc chung'),
          ('(ABCD)', "(A'B'C'D')", 'a', 'parallel faces at distance \\(AA\'\\)', 'hai mặt song song cách nhau \\(AA\'\\)'),
          ('A', "(A'BD)", '\\dfrac{a\\sqrt3}{3}', '\\(\\frac{1}{d^2}=\\frac1{a^2}+\\frac1{a^2}+\\frac1{a^2}\\)', '\\(\\frac{1}{d^2}=\\frac1{a^2}+\\frac1{a^2}+\\frac1{a^2}\\)'),
          ('AB', "C'D'", 'a\\sqrt2', 'parallel lines; distance \\(BC\'\\)', 'hai đường song song; khoảng cách \\(BC\'\\)'),
          ('B', "(ACC'A')", '\\dfrac{a\\sqrt2}{2}', 'equals \\(BO\\)', 'bằng \\(BO\\)')]


def k_cube(r, lv):
    p, q, ok, ee, ev = r.choice(CUBE_D)
    others = ['a', 'a\\sqrt2', '\\dfrac{a\\sqrt2}{2}', '\\dfrac{a\\sqrt3}{3}', 'a\\sqrt3', '\\dfrac{a}{2}']
    lab = 'from \\(%s\\) to \\(%s\\)' % (p, q); labv = 'giữa \\(%s\\) và \\(%s\\)' % (p, q)
    return dict(en='Cube \\(%s\\) with edge \\(a\\). The distance %s is…' % (CUBE, lab), vi='Hình lập phương \\(%s\\) cạnh \\(a\\). Khoảng cách %s bằng…' % (CUBE, labv),
      opts=pick_opts(r, ok, [o for o in others if o != ok]), ans=0, ee=ee[0].upper() + ee[1:] + '.', ev=ev[0].upper() + ev[1:] + '.')


def k_sbc(r, lv):
    h, a, s = r.choice(TRIP)
    return dict(en='\\(S.ABCD\\): square base of side %d, \\(SA\\perp(ABCD)\\), \\(SA=%d\\). The distance from \\(S\\) to the line \\(BC\\) is…' % (a, h), vi='Hình chóp \\(S.ABCD\\) có đáy là hình vuông cạnh %d, \\(SA\\perp(ABCD)\\), \\(SA=%d\\). Khoảng cách từ \\(S\\) đến đường thẳng \\(BC\\) bằng…' % (a, h),
      opts=pick_opts(r, str(s), [str(h), rt(h * h + 2 * a * a), str(a), fr(F(h * a, s))]), ans=0,
      ee='\\(BC\\perp(SAB)\\Rightarrow SB\\perp BC\\).', ev='\\(BC\\perp(SAB)\\) nên \\(SB\\perp BC\\): khoảng cách là \\(SB=\\sqrt{%d+%d}=%d\\).' % (h * h, a * a, s))


SBD = [(4, 1, 3), (8, 2, 6), (12, 3, 9)]


def k_sbd(r, lv):
    a, h, so = r.choice(SBD)
    return dict(en='\\(S.ABCD\\): square base of side %d, centre \\(O\\), \\(SA\\perp(ABCD)\\), \\(SA=%d\\). The distance from \\(S\\) to \\(BD\\) is…' % (a, h), vi='Hình chóp \\(S.ABCD\\) có đáy là hình vuông cạnh %d tâm \\(O\\), \\(SA\\perp(ABCD)\\), \\(SA=%d\\). Khoảng cách từ \\(S\\) đến đường thẳng \\(BD\\) bằng…' % (a, h),
      opts=pick_opts(r, str(so), [rt(h * h + a * a), str(h), rt(2 * a * a) if False else co(a // 2, 2) if a // 2 > 1 else '\\sqrt2', rt(h * h + 2 * a * a)]), ans=0,
      ee='\\(BD\\perp(SAO)\\Rightarrow SO\\perp BD\\).', ev='\\(BD\\perp AC\\), \\(BD\\perp SA\\) nên \\(BD\\perp SO\\): khoảng cách là \\(SO=\\sqrt{SA^2+AO^2}=\\sqrt{%d+%d}=%d\\).' % (h * h, a * a // 2, so))


def k_reg(r, lv):
    h, half, sm = r.choice(TRIP)
    return dict(en='Regular pyramid \\(S.ABCD\\): base side %d, height \\(SO=%d\\). The distance from \\(O\\) to \\((SCD)\\) is…' % (2 * half, h), vi='Hình chóp tứ giác đều \\(S.ABCD\\) có cạnh đáy %d, chiều cao \\(SO=%d\\). Khoảng cách từ \\(O\\) đến mặt phẳng \\((SCD)\\) bằng…' % (2 * half, h),
      opts=pick_opts(r, fr(F(h * half, sm)), [str(half), str(h), fr(F(2 * h * half, sm)), fr(F(h * half, h + half))]), ans=0,
      ee='\\(OH\\perp SM\\) (\\(M\\) the midpoint of \\(CD\\)): \\(OH=\\dfrac{SO\\cdot OM}{SM}\\).', ev='Gọi \\(M\\) là trung điểm \\(CD\\), kẻ \\(OH\\perp SM\\): \\(OH=\\dfrac{SO\\cdot OM}{SM}=\\dfrac{%d\\cdot%d}{%d}\\).' % (h, half, sm))


def k_box(r, lv):
    a, b, c = r.randint(2, 9), r.randint(2, 9), r.randint(2, 9)
    if len({a, b, c}) < 3: raise AssertionError
    return dict(en='Box \\(%s\\): \\(AB=%d\\), \\(AD=%d\\), \\(AA\'=%d\\). The distance between \\((ABB\'A\')\\) and \\((DCC\'D\')\\) is…' % (CUBE, a, b, c), vi='Hình hộp chữ nhật \\(%s\\) có \\(AB=%d\\), \\(AD=%d\\), \\(AA\'=%d\\). Khoảng cách giữa hai mặt phẳng \\((ABB\'A\')\\) và \\((DCC\'D\')\\) bằng…' % (CUBE, a, b, c),
      opts=pick_opts(r, str(b), [str(a), str(c), rt(a * a + b * b), rt(b * b + c * c)]), ans=0, ee='\\(AD\\) is perpendicular to both faces.', ev='\\(AD\\) vuông góc với cả hai mặt nên khoảng cách bằng \\(AD=%d\\).' % b)


def k_oabc(r, lv):
    a = r.choice([1, 2, 3, 4, 6])
    return dict(en='\\(OA\\), \\(OB\\), \\(OC\\) are pairwise perpendicular and \\(OA=OB=OC=%d\\). The distance from \\(O\\) to \\((ABC)\\) is…' % a, vi='Cho \\(OA\\), \\(OB\\), \\(OC\\) đôi một vuông góc và \\(OA=OB=OC=%d\\). Khoảng cách từ \\(O\\) đến mặt phẳng \\((ABC)\\) bằng…' % a,
      opts=pick_opts(r, rq(a, 3, 3), [rq(a, 2, 2), str(a), rq(a, 3, 1) if False else co(a, 3) if a > 1 else '\\sqrt3', rq(a, 2, 3)]), ans=0,
      ee='\\(\\dfrac1{d^2}=\\dfrac1{OA^2}+\\dfrac1{OB^2}+\\dfrac1{OC^2}\\).', ev='\\(\\dfrac1{d^2}=\\dfrac3{%d}\\Rightarrow d=%s\\).' % (a * a, rq(a, 3, 3)))


M26S11 = [k_asbc, k_cube, k_sbc, k_sbd, k_reg, k_box, k_oabc, k_asbc]

# ================= Bài 27. Thể tích =================
def t_pyr(r, lv):
    a, h = r.randint(2, 9), r.randint(2, 12)
    return dict(en='A pyramid has a square base of side %d and height %d. Its volume is…' % (a, h), vi='Hình chóp có đáy là hình vuông cạnh %d và chiều cao %d. Thể tích của khối chóp là…' % (a, h),
      opts=pick_opts(r, fr(F(a * a * h, 3)), [str(a * a * h), fr(F(a * a * h, 6)), fr(F(a * h, 3)), fr(F(2 * a * a * h, 3))]), ans=0, ee='\\(V=\\frac13Bh\\).', ev='\\(V=\\frac13Bh=\\frac13\\cdot%d\\cdot%d=%s\\).' % (a * a, h, fr(F(a * a * h, 3))))


def t_prism(r, lv):
    p, q, h = r.randint(2, 9), r.randint(2, 9), r.randint(2, 10)
    return dict(en='A right prism has a right-triangle base with legs %d and %d, and height %d. Its volume is…' % (p, q, h), vi='Lăng trụ đứng có đáy là tam giác vuông với hai cạnh góc vuông %d và %d, chiều cao %d. Thể tích khối lăng trụ là…' % (p, q, h),
      opts=pick_opts(r, fr(F(p * q * h, 2)), [str(p * q * h), fr(F(p * q * h, 6)), fr(F(p * q * h, 3)), str(p + q + h)]), ans=0, ee='\\(V=Bh\\), \\(B=\\frac12pq\\).', ev='\\(V=Bh=\\frac12\\cdot%d\\cdot%d\\cdot%d=%s\\).' % (p, q, h, fr(F(p * q * h, 2))))


def t_oabc(r, lv):
    a, b, c = r.randint(2, 9), r.randint(2, 9), r.randint(2, 9)
    return dict(en='\\(OA\\), \\(OB\\), \\(OC\\) pairwise perpendicular, \\(OA=%d\\), \\(OB=%d\\), \\(OC=%d\\). The volume of \\(OABC\\) is…' % (a, b, c), vi='Tứ diện \\(OABC\\) có \\(OA\\), \\(OB\\), \\(OC\\) đôi một vuông góc, \\(OA=%d\\), \\(OB=%d\\), \\(OC=%d\\). Thể tích tứ diện là…' % (a, b, c),
      opts=pick_opts(r, fr(F(a * b * c, 6)), [str(a * b * c), fr(F(a * b * c, 3)), fr(F(a * b * c, 2)), fr(F(a * b * c, 12))]), ans=0, ee='\\(V=\\frac13\\cdot\\frac12OA\\cdot OB\\cdot OC\\).', ev='\\(V=\\frac13\\cdot S_{OAB}\\cdot OC=\\frac16\\cdot%d\\cdot%d\\cdot%d=%s\\).' % (a, b, c, fr(F(a * b * c, 6))))


def t_cube(r, lv):
    a = r.randint(2, 6)
    return dict(en='A cube has diagonal \\(%s\\). Its volume is…' % co(a, 3), vi='Hình lập phương có đường chéo bằng \\(%s\\). Thể tích khối lập phương là…' % co(a, 3),
      opts=pick_opts(r, str(a ** 3), [str(3 * a ** 3), co(a ** 3, 3), str(a * a), str((a + 1) ** 3)]), ans=0, ee='Diagonal \\(a\\sqrt3\\Rightarrow\\) edge \\(%d\\).' % a, ev='Đường chéo \\(a\\sqrt3=%s\\Rightarrow a=%d\\), \\(V=a^3=%d\\).' % (co(a, 3), a, a ** 3))


def t_frustum(r, lv):
    a, b = sorted(r.sample(range(2, 10), 2))[::-1]; h = 3 * r.randint(1, 4)
    V = F(h, 3) * (a * a + b * b + a * b)
    return dict(en='A frustum of a regular square pyramid has base sides %d and %d and height %d. Its volume is…' % (a, b, h), vi='Khối chóp cụt tứ giác đều có cạnh hai đáy %d và %d, chiều cao %d. Thể tích khối chóp cụt là…' % (a, b, h),
      opts=pick_opts(r, fr(V), [fr(F(h, 3) * (a * a + b * b)), fr(F(h, 2) * (a * a + b * b)), str(h * a * a - h * b * b), fr(F(h, 3) * a * a)]), ans=0,
      ee='\\(V=\\frac h3(S+S\'+\\sqrt{SS\'})\\).', ev='\\(V=\\frac h3(S+S\'+\\sqrt{SS\'})=\\frac{%d}3(%d+%d+%d)=%s\\).' % (h, a * a, b * b, a * b, fr(V)))


def t_tet(r, lv):
    a = r.choice([1, 2, 3, 6])
    V = rq(a ** 3, 12, 2)
    return dict(en='A regular tetrahedron has edge %d. Its volume is…' % a, vi='Tứ diện đều có cạnh %d. Thể tích khối tứ diện là…' % a,
      opts=pick_opts(r, V, [rq(a ** 3, 4, 3), rq(a ** 3, 12, 3), rq(a ** 3, 6, 2), rq(a ** 3, 3, 2)]), ans=0,
      ee='\\(V=\\dfrac{a^3\\sqrt2}{12}\\).', ev='Đáy là tam giác đều diện tích \\(\\frac{a^2\\sqrt3}4\\), chiều cao \\(\\frac{a\\sqrt6}3\\): \\(V=\\dfrac{a^3\\sqrt2}{12}=%s\\).' % V)


def t_ratio(r, lv):
    p, q = r.choice([(1, 2), (1, 3), (2, 3), (1, 4), (3, 4)]), r.choice([(1, 2), (1, 3), (2, 3), (1, 4)])
    k = F(p[0], p[1]) * F(q[0], q[1])
    return dict(en='Tetrahedron \\(S.ABC\\): \\(M\\in SA\\), \\(N\\in SB\\) with \\(SM=%s\\,SA\\), \\(SN=%s\\,SB\\). Then \\(\\dfrac{V_{S.MNC}}{V_{S.ABC}}=\\)…' % (fr(F(*p)), fr(F(*q))), vi='Cho khối chóp \\(S.ABC\\); \\(M\\in SA\\), \\(N\\in SB\\) với \\(SM=%s\\,SA\\), \\(SN=%s\\,SB\\). Tỉ số \\(\\dfrac{V_{S.MNC}}{V_{S.ABC}}\\) bằng…' % (fr(F(*p)), fr(F(*q))),
      opts=pick_opts(r, fr(k), [fr(F(*p) + F(*q)), fr(k * k), fr(1 - k), fr(F(*p))]), ans=0, ee='Ratio \\(=\\dfrac{SM}{SA}\\cdot\\dfrac{SN}{SB}\\cdot\\dfrac{SC}{SC}\\).', ev='Tỉ số thể tích \\(=\\dfrac{SM}{SA}\\cdot\\dfrac{SN}{SB}\\cdot\\dfrac{SC}{SC}=%s\\).' % fr(k))


def t_tank(r, lv):
    a, b, c = r.randint(5, 20), r.randint(4, 12), r.randint(5, 15)
    return dict(en='A water tank is a box %d dm long, %d dm wide and %d dm high. How many litres does it hold when full?' % (a, b, c), vi='Một bể nước hình hộp chữ nhật dài %d dm, rộng %d dm, cao %d dm. Khi đầy, bể chứa bao nhiêu lít nước?' % (a, b, c),
      opts=pick_opts(r, '%d' % (a * b * c), ['%d' % (a * b * c * 10), '%d' % (a * b * c // 10) if a * b * c % 10 == 0 else fr(F(a * b * c, 10)), '%d' % (2 * (a * b + b * c + c * a)), '%d' % (a * b * c * 1000)]), ans=0,
      ee='\\(1\\text{ dm}^3=1\\) litre.', ev='\\(V=%d\\cdot%d\\cdot%d=%d\\text{ dm}^3\\); \\(1\\text{ dm}^3=1\\) lít.' % (a, b, c, a * b * c))


M27S11 = [t_pyr, t_prism, t_oabc, t_cube, t_frustum, t_tet, t_ratio, t_tank]
