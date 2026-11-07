# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 11 – Bài 22 (hai đường thẳng vuông góc), Bài 23 (đường thẳng vuông góc với mặt phẳng),
Bài 24 (phép chiếu vuông góc, góc giữa đường thẳng và mặt phẳng). Đáp án lấy từ bảng đã kiểm chứng hoặc tính chính xác."""
import math
from fractions import Fraction as F
from mb_selfpractice import pick_opts, fr
from sp_g11f import TT
from sp_g10h import surd, rt

DEG = lambda d: '%d^\\circ' % d
def degs(k, others=(0, 30, 45, 60, 90, 120)):
    return [DEG(x) for x in others if x != k]
CUBE = 'ABCD.A\'B\'C\'D\''
def co(c, s): return ('' if c == 1 else str(c)) + '\\sqrt%d' % s
def rq(k, d, s):
    q = F(k, d); top = co(q.numerator, s)
    return top if q.denominator == 1 else '\\dfrac{%s}{%d}' % (top, q.denominator)

# ================= Bài 22. Hai đường thẳng vuông góc =================
CUBE_ANG = [("AB", "C'D'", 0, "\\(C'D'\\parallel AB\\)", "\\(C'D'\\parallel AB\\)"), ("AB", "B'C'", 90, "\\(B'C'\\parallel BC\\perp AB\\)", "\\(B'C'\\parallel BC\\) mà \\(BC\\perp AB\\)"),
            ("AC", "A'D'", 45, "\\(A'D'\\parallel AD\\), \\(\\widehat{CAD}=45^\\circ\\)", "\\(A'D'\\parallel AD\\), \\(\\widehat{CAD}=45^\\circ\\)"),
            ("A'B", "B'C", 60, "\\(A'B\\parallel D'C\\); triangle \\(B'CD'\\) is equilateral", "\\(A'B\\parallel D'C\\); tam giác \\(B'CD'\\) đều"),
            ("AC", "B'D'", 90, "\\(B'D'\\parallel BD\\perp AC\\)", "\\(B'D'\\parallel BD\\) mà \\(BD\\perp AC\\)"), ("AB'", "BC'", 60, "\\(AB'\\parallel DC'\\); triangle \\(BC'D\\) is equilateral", "\\(AB'\\parallel DC'\\); tam giác \\(BC'D\\) đều"),
            ("AA'", "BD", 90, "\\(AA'\\perp(ABCD)\\)", "\\(AA'\\perp(ABCD)\\supset BD\\)"), ("A'B", "AD'", 60, "\\(A'B\\parallel D'C\\); triangle \\(ACD'\\) is equilateral", "\\(A'B\\parallel D'C\\); tam giác \\(ACD'\\) đều"),
            ("AD", "B'C'", 0, "\\(B'C'\\parallel BC\\parallel AD\\)", "\\(B'C'\\parallel BC\\parallel AD\\)"), ("BD", "A'C'", 90, "\\(A'C'\\parallel AC\\perp BD\\)", "\\(A'C'\\parallel AC\\perp BD\\)"),
            ("AB", "A'C'", 45, "\\(A'C'\\parallel AC\\), \\(\\widehat{BAC}=45^\\circ\\)", "\\(A'C'\\parallel AC\\), \\(\\widehat{BAC}=45^\\circ\\)")]


def l_cube(r, lv):
    a = r.randint(2, 9); p, q, d, ee, ev = r.choice(CUBE_ANG)
    return dict(en='Cube \\(%s\\) with edge %d. The angle between \\(%s\\) and \\(%s\\) is…' % (CUBE, a, p, q), vi='Cho hình lập phương \\(%s\\) cạnh %d. Góc giữa hai đường thẳng \\(%s\\) và \\(%s\\) bằng…' % (CUBE, a, p, q),
      opts=pick_opts(r, DEG(d), degs(d)), ans=0, ee=ee + '.', ev=ev + '.')


PYR_ANG = [('SA', 'BC', 60, 'BC\\parallel AD', '\\widehat{SAD}'), ('SB', 'AD', 60, 'AD\\parallel BC', '\\widehat{SBC}'), ('SA', 'CD', 60, 'CD\\parallel AB', '\\widehat{SAB}'),
           ('SC', 'AB', 60, 'AB\\parallel CD', '\\widehat{SCD}'), ('SA', 'SC', 90, 'SA^2+SC^2=2a^2=AC^2', '\\widehat{ASC}'), ('SB', 'SD', 90, 'SB^2+SD^2=2a^2=BD^2', '\\widehat{BSD}')]


def l_pyr(r, lv):
    a = r.randint(2, 9); p, q, d, why, ang = r.choice(PYR_ANG)
    return dict(en='Pyramid \\(S.ABCD\\): \\(ABCD\\) is a square of side %d and all lateral edges equal %d. The angle between \\(%s\\) and \\(%s\\) is…' % (a, a, p, q), vi='Hình chóp \\(S.ABCD\\) có đáy là hình vuông cạnh %d và tất cả các cạnh bên bằng %d. Góc giữa \\(%s\\) và \\(%s\\) bằng…' % (a, a, p, q),
      opts=pick_opts(r, DEG(d), degs(d)), ans=0, ee='\\(%s\\); use the angle \\(%s\\).' % (why, ang), ev='\\(%s\\); xét góc \\(%s\\) (các mặt bên là tam giác đều).' % (why, ang))


def l_tet(r, lv):
    k = r.randint(1, 7); kind = r.choice([(3, 60), (2, 90), (1, 60)])
    MN = ('%d\\sqrt{%d}' % (k, kind[0]) if k > 1 else '\\sqrt{%d}' % kind[0]) if kind[0] > 1 else str(k)
    return dict(en='Tetrahedron \\(ABCD\\): \\(AB=CD=%d\\); \\(M\\), \\(N\\) are the midpoints of \\(BC\\), \\(AD\\) and \\(MN=%s\\). The angle between \\(AB\\) and \\(CD\\) is…' % (2 * k, MN),
      vi='Tứ diện \\(ABCD\\) có \\(AB=CD=%d\\); \\(M\\), \\(N\\) là trung điểm của \\(BC\\), \\(AD\\) và \\(MN=%s\\). Góc giữa \\(AB\\) và \\(CD\\) bằng…' % (2 * k, MN),
      opts=pick_opts(r, DEG(kind[1]), degs(kind[1], (30, 45, 60, 90, 120))), ans=0,
      ee='With \\(P\\) the midpoint of \\(AC\\): \\(PM=PN=%d\\), \\(\\cos\\widehat{MPN}=\\dfrac{PM^2+PN^2-MN^2}{2PM\\cdot PN}\\); the angle of the lines is acute.' % k,
      ev='Gọi \\(P\\) là trung điểm \\(AC\\): \\(PM=PN=%d\\), \\(\\cos\\widehat{MPN}=%s\\); góc giữa hai đường thẳng là góc nhọn (hoặc vuông) tương ứng.' % (k, fr(F(2 - kind[0], 2))))


BOX2 = [(3, 4, 5), (4, 3, 5), (5, 12, 13), (6, 8, 10), (8, 6, 10), (12, 5, 13), (8, 15, 17)]
DIAG = [(1, 2, 2, 3), (2, 3, 6, 7), (2, 6, 9, 11), (1, 4, 8, 9), (4, 4, 7, 9), (2, 1, 2, 3), (6, 6, 7, 11), (3, 4, 12, 13), (4, 8, 1, 9)]


def l_box(r, lv):
    a, b, c = r.choice(BOX2); h = r.randint(2, 9)
    return dict(en='A box \\(%s\\) has \\(AB=%d\\), \\(AD=%d\\), \\(AA\'=%d\\). If \\(\\varphi\\) is the angle between \\(AB\\) and \\(A\'C\'\\), then \\(\\cos\\varphi=\\)…' % (CUBE, a, b, h), vi='Hình hộp chữ nhật \\(%s\\) có \\(AB=%d\\), \\(AD=%d\\), \\(AA\'=%d\\). Gọi \\(\\varphi\\) là góc giữa \\(AB\\) và \\(A\'C\'\\). Khi đó \\(\\cos\\varphi=\\)…' % (CUBE, a, b, h),
      opts=pick_opts(r, fr(F(a, c)), [fr(F(b, c)), fr(F(a, b)), fr(F(b, a)), fr(F(a, c + h))]), ans=0, ee='\\(A\'C\'\\parallel AC\\): \\(\\cos\\widehat{BAC}=\\dfrac{AB}{AC}\\).', ev='\\(A\'C\'\\parallel AC\\): \\(\\cos\\widehat{BAC}=\\dfrac{AB}{AC}=\\dfrac{%d}{%d}\\).' % (a, c))


def l_diag(r, lv):
    a, b, c, d = r.choice(DIAG)
    return dict(en='A box \\(%s\\) has \\(AB=%d\\), \\(AD=%d\\), \\(AA\'=%d\\). If \\(\\varphi\\) is the angle between \\(BB\'\\) and \\(AC\'\\), then \\(\\cos\\varphi=\\)…' % (CUBE, a, b, c), vi='Hình hộp chữ nhật \\(%s\\) có \\(AB=%d\\), \\(AD=%d\\), \\(AA\'=%d\\). Gọi \\(\\varphi\\) là góc giữa \\(BB\'\\) và \\(AC\'\\). Khi đó \\(\\cos\\varphi=\\)…' % (CUBE, a, b, c),
      opts=pick_opts(r, fr(F(c, d)), [fr(F(a, d)), fr(F(b, d)), fr(F(c, a + b)), fr(F(d - c, d))]), ans=0,
      ee='\\(BB\'\\parallel CC\'\\): \\(\\cos\\widehat{AC\'C}=\\dfrac{CC\'}{AC\'}\\), \\(AC\'=%d\\).' % d, ev='\\(BB\'\\parallel CC\'\\): \\(\\cos\\widehat{AC\'C}=\\dfrac{CC\'}{AC\'}=\\dfrac{%d}{%d}\\) với \\(AC\'=\\sqrt{%d+%d+%d}=%d\\).' % (c, d, a * a, b * b, c * c, d))


def l_room(r, lv):
    a, b, c = r.choice(BOX2); h = r.choice([3, 4])
    return dict(en='A room is %d m long, %d m wide and %d m high. A cable runs along a diagonal of the floor. If \\(\\varphi\\) is the angle between the cable and a %d m edge of the ceiling, then \\(\\cos\\varphi=\\)…' % (a, b, h, b), vi='Một căn phòng dài %d m, rộng %d m, cao %d m. Một sợi cáp chạy theo đường chéo sàn nhà. Gọi \\(\\varphi\\) là góc giữa sợi cáp và một cạnh dài %d m của trần nhà. Khi đó \\(\\cos\\varphi=\\)…' % (a, b, h, b),
      opts=pick_opts(r, fr(F(b, c)), [fr(F(a, c)), fr(F(b, a)), fr(F(h, c)), fr(F(b, c + h))]), ans=0,
      ee='The ceiling edge is parallel to a floor edge of length %d; the floor diagonal is %d.' % (b, c), ev='Cạnh trần song song với cạnh sàn dài %d m; đường chéo sàn dài %d m nên \\(\\cos\\varphi=\\dfrac{%d}{%d}\\).' % (b, c, b, c))


M22S11 = [l_cube, l_pyr, l_tet, l_box, l_diag, l_room, l_cube, l_pyr]

# ================= Bài 23. Đường thẳng vuông góc với mặt phẳng =================
SQ_PERP = [('(SAB)', 'BC', ['BD', 'SC', 'AC']), ('(SAB)', 'AD', ['SD', 'BD', 'AC']), ('(SAD)', 'CD', ['BD', 'SC', 'AC']), ('(SAD)', 'AB', ['SB', 'AC', 'BD']), ('(SAC)', 'BD', ['SB', 'AB', 'CD'])]


def p_sq(r, lv):
    h = r.randint(2, 9); pl, ok, bad = r.choice(SQ_PERP)
    return dict(en='\\(S.ABCD\\) has a square base and \\(SA\\perp(ABCD)\\), \\(SA=%d\\). Which line is perpendicular to \\(%s\\)?' % (h, pl), vi='Hình chóp \\(S.ABCD\\) có đáy là hình vuông, \\(SA\\perp(ABCD)\\), \\(SA=%d\\). Đường thẳng nào vuông góc với mặt phẳng \\(%s\\)?' % (h, pl),
      opts=pick_opts(r, ok, bad), ans=0, ee='\\(%s\\) is perpendicular to \\(SA\\) and to a second line of \\(%s\\).' % (ok, pl), ev='\\(%s\\) vuông góc với \\(SA\\) và với một đường thẳng nữa của \\(%s\\) (hai đường cắt nhau).' % (ok, pl))


TRI = [('B', 'BC', '(SAB)', ['(SAC)', '(SBC)', '(ABC)']), ('A', 'AB', '(SAC)', ['(SAB)', '(SBC)', '(ABC)']), ('C', 'BC', '(SAC)', ['(SAB)', '(SBC)', '(ABC)']), ('A', 'AC', '(SAB)', ['(SAC)', '(SBC)', '(ABC)']), ('B', 'AB', '(SBC)', ['(SAB)', '(SAC)', '(ABC)'])]


def p_tri(r, lv):
    h = r.randint(2, 9); v, line, ok, bad = r.choice(TRI)
    if v == 'B' and line == 'AB':        # AB ⊥ BC, AB ⊥ SA nhưng SA ⊄ (SBC) → không đúng; bỏ trường hợp này
        raise AssertionError
    return dict(en='\\(S.ABC\\) has \\(SA\\perp(ABC)\\), \\(SA=%d\\), and triangle \\(ABC\\) is right-angled at \\(%s\\). Then \\(%s\\) is perpendicular to…' % (h, v, line), vi='Hình chóp \\(S.ABC\\) có \\(SA\\perp(ABC)\\), \\(SA=%d\\), tam giác \\(ABC\\) vuông tại \\(%s\\). Khi đó \\(%s\\) vuông góc với mặt phẳng…' % (h, v, line),
      opts=pick_opts(r, ok, bad), ans=0, ee='\\(%s\\perp SA\\) and \\(%s\\) is perpendicular to a leg at \\(%s\\).' % (line, line, v), ev='\\(%s\\perp SA\\) và \\(%s\\) vuông góc với cạnh góc vuông còn lại tại \\(%s\\).' % (line, line, v))


SC_T = [(1, 2, 3), (2, 4, 6), (7, 6, 11), (3, 6, 9), (5, 10, 15), (4, 4, 4 * 1)]


def p_sc(r, lv):
    h, a, d = r.choice(SC_T[:5]); k = r.randint(1, 2); h, a, d = h * k, a * k, d * k
    return dict(en='\\(S.ABCD\\): square base of side %d, \\(SA\\perp(ABCD)\\), \\(SA=%d\\). Then \\(SC=\\)…' % (a, h), vi='Hình chóp \\(S.ABCD\\) có đáy là hình vuông cạnh %d, \\(SA\\perp(ABCD)\\), \\(SA=%d\\). Độ dài \\(SC\\) là…' % (a, h),
      opts=pick_opts(r, str(d), [rt(h * h + a * a), str(h + a), rt(2 * a * a), rt(h * h + 4 * a * a)]), ans=0,
      ee='\\(SA\\perp AC\\), \\(AC=%d\\sqrt2\\).' % a, ev='\\(SA\\perp AC\\) nên \\(SC=\\sqrt{SA^2+AC^2}=\\sqrt{%d+%d}=%d\\).' % (h * h, 2 * a * a, d))


def p_oabc(r, lv):
    a, b, c = r.choice(BOX2); k = r.randint(1, 3); w = r.randint(2, 9)
    return dict(en='\\(OA\\), \\(OB\\), \\(OC\\) are pairwise perpendicular with \\(OA=%d\\), \\(OB=%d\\), \\(OC=%d\\). Then \\(AB=\\)…' % (a * k, b * k, w), vi='Cho \\(OA\\), \\(OB\\), \\(OC\\) đôi một vuông góc với \\(OA=%d\\), \\(OB=%d\\), \\(OC=%d\\). Độ dài \\(AB\\) là…' % (a * k, b * k, w),
      opts=pick_opts(r, str(c * k), [rt((a * k) ** 2 + w * w), rt((b * k) ** 2 + w * w), str(a * k + b * k), rt((a * k) ** 2 + (b * k) ** 2 + w * w)]), ans=0,
      ee='\\(OA\\perp(OBC)\\) so \\(OA\\perp OB\\).', ev='\\(OA\\perp OB\\) nên \\(AB=\\sqrt{OA^2+OB^2}=%d\\).' % (c * k))


def p_pole(r, lv):
    a, b, c = r.choice(BOX2); k = r.choice([1, 2])
    return dict(en='A flagpole %d m high stands perpendicular to flat ground. A rope goes from its top to a peg %d m from its foot. The rope is…' % (a * k, b * k), vi='Một cột cờ cao %d m dựng vuông góc với mặt đất phẳng. Một sợi dây nối đỉnh cột với một cọc cách chân cột %d m. Sợi dây dài…' % (a * k, b * k),
      opts=pick_opts(r, '%d\\text{ m}' % (c * k), ['%d\\text{ m}' % (a * k + b * k), '%s\\text{ m}' % rt(abs((a * k) ** 2 - (b * k) ** 2)), '%d\\text{ m}' % (c * k + 1), '%d\\text{ m}' % (c * k - 1)]), ans=0,
      ee='The pole is perpendicular to every line of the ground through its foot.', ev='Cột vuông góc với mặt đất nên vuông góc với đường thẳng nối chân cột với cọc: dây dài \\(\\sqrt{%d+%d}=%d\\) m.' % ((a * k) ** 2, (b * k) ** 2, c * k))


def p_diag(r, lv):
    a, b, c, d = r.choice(DIAG)
    return dict(en='Box \\(%s\\): \\(AB=%d\\), \\(AD=%d\\), \\(AA\'=%d\\). Then \\(A\'C=\\)…' % (CUBE, a, b, c), vi='Hình hộp chữ nhật \\(%s\\) có \\(AB=%d\\), \\(AD=%d\\), \\(AA\'=%d\\). Độ dài \\(A\'C\\) là…' % (CUBE, a, b, c),
      opts=pick_opts(r, str(d), [str(a + b + c), rt(a * a + b * b), rt(b * b + c * c), rt(a * a + c * c)]), ans=0,
      ee='\\(AA\'\\perp(ABCD)\\), so \\(AA\'\\perp AC\\).', ev='\\(AA\'\\perp(ABCD)\\) nên \\(AA\'\\perp AC\\): \\(A\'C=\\sqrt{AC^2+AA\'^2}=\\sqrt{%d+%d+%d}=%d\\).' % (a * a, b * b, c * c, d))


def p_sb(r, lv):
    a, b, c = r.choice(BOX2); k = r.randint(1, 3)
    return dict(en='\\(S.ABC\\) has \\(SA\\perp(ABC)\\), \\(SA=%d\\), \\(AB=%d\\). Then \\(SB=\\)…' % (a * k, b * k), vi='Hình chóp \\(S.ABC\\) có \\(SA\\perp(ABC)\\), \\(SA=%d\\), \\(AB=%d\\). Độ dài \\(SB\\) là…' % (a * k, b * k),
      opts=pick_opts(r, str(c * k), [str(a * k + b * k), rt(abs((a * k) ** 2 - (b * k) ** 2)), str(c * k + 2), str(2 * c * k)]), ans=0,
      ee='\\(SA\\perp AB\\).', ev='\\(SA\\perp(ABC)\\) nên \\(SA\\perp AB\\): \\(SB=\\sqrt{SA^2+AB^2}=%d\\).' % (c * k))


M23S11 = [p_sq, p_tri, p_sc, p_oabc, p_pole, p_diag, p_sb, p_sq]

# ================= Bài 24. Phép chiếu vuông góc. Góc giữa đường thẳng và mặt phẳng =================
def a_sb(r, lv):
    k = r.randint(2, 9); kind = r.choice([('%d\\sqrt3' % k, 60), (str(k), 45), (rq(k, 3, 3), 30)])
    return dict(en='\\(S.ABCD\\): square base of side %d, \\(SA\\perp(ABCD)\\), \\(SA=%s\\). The angle between \\(SB\\) and \\((ABCD)\\) is…' % (k, kind[0]), vi='Hình chóp \\(S.ABCD\\) có đáy là hình vuông cạnh %d, \\(SA\\perp(ABCD)\\), \\(SA=%s\\). Góc giữa \\(SB\\) và mặt phẳng \\((ABCD)\\) bằng…' % (k, kind[0]),
      opts=pick_opts(r, DEG(kind[1]), degs(kind[1], (30, 45, 60, 90))), ans=0,
      ee='Projection of \\(SB\\) is \\(AB\\): \\(\\tan\\widehat{SBA}=\\dfrac{SA}{AB}\\).', ev='Hình chiếu của \\(SB\\) lên đáy là \\(AB\\): \\(\\tan\\widehat{SBA}=\\dfrac{SA}{AB}\\).')


def a_sc(r, lv):
    k = r.randint(2, 9); kind = r.choice([('%d\\sqrt6' % k, 60), ('%d\\sqrt2' % k, 45), (rq(k, 3, 6), 30)])
    return dict(en='\\(S.ABCD\\): square base of side %d, \\(SA\\perp(ABCD)\\), \\(SA=%s\\). The angle between \\(SC\\) and \\((ABCD)\\) is…' % (k, kind[0]), vi='Hình chóp \\(S.ABCD\\) có đáy là hình vuông cạnh %d, \\(SA\\perp(ABCD)\\), \\(SA=%s\\). Góc giữa \\(SC\\) và mặt phẳng \\((ABCD)\\) bằng…' % (k, kind[0]),
      opts=pick_opts(r, DEG(kind[1]), degs(kind[1], (30, 45, 60, 90))), ans=0,
      ee='Projection of \\(SC\\) is \\(AC=%d\\sqrt2\\): \\(\\tan\\widehat{SCA}=\\dfrac{SA}{AC}\\).' % k, ev='Hình chiếu của \\(SC\\) lên đáy là \\(AC=%d\\sqrt2\\): \\(\\tan\\widehat{SCA}=\\dfrac{SA}{AC}\\).' % k)


def a_tan(r, lv):
    h, a = r.randint(1, 9), r.randint(2, 9)
    if math.gcd(h, a) != 1 or h == a: raise AssertionError
    return dict(en='\\(S.ABC\\): \\(SA\\perp(ABC)\\), \\(SA=%d\\), \\(AC=%d\\). If \\(\\varphi\\) is the angle between \\(SC\\) and \\((ABC)\\), then \\(\\tan\\varphi=\\)…' % (h, a), vi='Hình chóp \\(S.ABC\\) có \\(SA\\perp(ABC)\\), \\(SA=%d\\), \\(AC=%d\\). Gọi \\(\\varphi\\) là góc giữa \\(SC\\) và \\((ABC)\\). Khi đó \\(\\tan\\varphi=\\)…' % (h, a),
      opts=pick_opts(r, fr(F(h, a)), [fr(F(a, h)), surd(h, h * h + a * a), surd(a, h * h + a * a), fr(F(h, a + h))]), ans=0,
      ee='\\(\\varphi=\\widehat{SCA}\\), \\(\\tan\\varphi=\\dfrac{SA}{AC}\\).', ev='\\(\\varphi=\\widehat{SCA}\\), \\(\\tan\\varphi=\\dfrac{SA}{AC}=%s\\).' % fr(F(h, a)))


PROJ = [('SB', 'AB'), ('SC', 'AC'), ('SD', 'AD'), ('SO', 'AO')]


def a_proj(r, lv):
    h = r.randint(2, 9); s, p = r.choice(PROJ); bad = [x for x in ('AB', 'AC', 'AD', 'BC', 'CD', 'BD') if x != p]
    return dict(en='\\(S.ABCD\\) (square base, centre \\(O\\)) has \\(SA\\perp(ABCD)\\), \\(SA=%d\\). The orthogonal projection of \\(%s\\) on \\((ABCD)\\) is…' % (h, s), vi='Hình chóp \\(S.ABCD\\) có đáy là hình vuông tâm \\(O\\), \\(SA\\perp(ABCD)\\), \\(SA=%d\\). Hình chiếu vuông góc của \\(%s\\) lên \\((ABCD)\\) là…' % (h, s),
      opts=pick_opts(r, p, bad), ans=0, ee='The projection of \\(S\\) is \\(A\\).', ev='Hình chiếu của \\(S\\) là \\(A\\), của điểm thuộc đáy là chính nó.')


CUBE_LP = [("A'B", '45^\\circ'), ("A'D", '45^\\circ'), ("A'C", '\\tan\\varphi=\\dfrac{\\sqrt2}{2}'), ("BD'", '\\tan\\varphi=\\dfrac{\\sqrt2}{2}'), ("A'C'", '0^\\circ'), ("AC'", '\\tan\\varphi=\\dfrac{\\sqrt2}{2}')]


def a_cube(r, lv):
    a = r.randint(2, 9); l, ok = r.choice(CUBE_LP)
    opts = ['45^\\circ', '0^\\circ', '\\tan\\varphi=\\dfrac{\\sqrt2}{2}', '60^\\circ', '\\tan\\varphi=\\sqrt2', '90^\\circ']
    return dict(en='Cube \\(%s\\) with edge %d. The angle \\(\\varphi\\) between \\(%s\\) and \\((ABCD)\\) satisfies…' % (CUBE, a, l), vi='Hình lập phương \\(%s\\) cạnh %d. Góc \\(\\varphi\\) giữa \\(%s\\) và mặt phẳng \\((ABCD)\\) là…' % (CUBE, a, l),
      opts=pick_opts(r, ok, [o for o in opts if o != ok]), ans=0, ee='Project the upper endpoint vertically onto the base.', ev='Chiếu vuông góc đầu mút trên xuống đáy; với đường chéo khối: \\(\\tan\\varphi=\\dfrac{a}{a\\sqrt2}=\\dfrac{\\sqrt2}2\\).')


def a_reg(r, lv):
    k = r.randint(2, 9); kind = r.choice([(rq(k, 2, 2), 45), (rq(k, 2, 6), 60), (rq(k, 6, 6), 30)])
    return dict(en='Regular pyramid \\(S.ABCD\\): base side %d, height \\(SO=%s\\). The angle between a lateral edge and the base is…' % (k, kind[0]), vi='Hình chóp tứ giác đều \\(S.ABCD\\) có cạnh đáy %d, chiều cao \\(SO=%s\\). Góc giữa cạnh bên và mặt đáy bằng…' % (k, kind[0]),
      opts=pick_opts(r, DEG(kind[1]), degs(kind[1], (30, 45, 60, 90))), ans=0,
      ee='\\(\\tan\\widehat{SAO}=\\dfrac{SO}{AO}\\), \\(AO=\\dfrac{%d\\sqrt2}2\\).' % k, ev='\\(\\tan\\widehat{SAO}=\\dfrac{SO}{AO}\\) với \\(AO=\\dfrac{%d\\sqrt2}2\\).' % k)


LAD = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (12, 16, 20)]


def a_ladder(r, lv):
    a, b, c = r.choice(LAD)
    return dict(en='A %d m ladder leans on a vertical wall; its top is %d m above the flat ground. If \\(\\varphi\\) is the angle between the ladder and the ground, then \\(\\cos\\varphi=\\)…' % (c, b), vi='Một chiếc thang dài %d m dựa vào bức tường thẳng đứng, đỉnh thang cao %d m so với mặt đất phẳng. Gọi \\(\\varphi\\) là góc giữa thang và mặt đất. Khi đó \\(\\cos\\varphi=\\)…' % (c, b),
      opts=pick_opts(r, fr(F(a, c)), [fr(F(b, c)), fr(F(a, b)), fr(F(b, a)), fr(F(a, b + c))]), ans=0,
      ee='The projection of the ladder on the ground has length %d m.' % a, ev='Hình chiếu của thang trên mặt đất dài \\(\\sqrt{%d-%d}=%d\\) m nên \\(\\cos\\varphi=\\dfrac{%d}{%d}\\).' % (c * c, b * b, a, a, c))


RIGHT = [('ABCD là hình chữ nhật', 'ABCD is a rectangle', '\\widehat{SBC}', ['\\widehat{SCB}', '\\widehat{SCA}', '\\widehat{BSC}']), ('ABCD là hình chữ nhật', 'ABCD is a rectangle', '\\widehat{SDC}', ['\\widehat{SCD}', '\\widehat{SCA}', '\\widehat{DSC}']),
         ('ABCD là hình vuông tâm O', 'ABCD is a square with centre O', '\\widehat{SOB}', ['\\widehat{SBO}', '\\widehat{SOA}', '\\widehat{BSO}'])]


def a_three(r, lv):
    h = r.randint(2, 9); vi, en, ok, bad = r.choice(RIGHT)
    return dict(en='\\(S.ABCD\\): %s, \\(SA\\perp(ABCD)\\), \\(SA=%d\\). Which angle is a right angle?' % (en, h), vi='Hình chóp \\(S.ABCD\\) có %s, \\(SA\\perp(ABCD)\\), \\(SA=%d\\). Góc nào là góc vuông?' % (vi, h),
      opts=pick_opts(r, ok, bad), ans=0, ee='Three perpendiculars theorem: the projection of the slant line is perpendicular to the edge.', ev='Định lí ba đường vuông góc: hình chiếu của đường xiên vuông góc với cạnh đáy thì đường xiên cũng vuông góc với cạnh đó.')


M24S11 = [a_sb, a_sc, a_tan, a_proj, a_cube, a_reg, a_ladder, a_three]
