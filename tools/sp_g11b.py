# -*- coding: utf-8 -*-
"""Trắc nghiệm tự luyện lớp 11 – Bài 9 (số đặc trưng đo xu thế trung tâm, ghép nhóm)."""
import functools
from fractions import Fraction as F
from mb_selfpractice import *
from gdata import GT, nice, dec

@functools.lru_cache(maxsize=None)
def T9(seed): return nice(seed, need=('mean', 'median', 'mode'))
def _t(r): return T9(r.randint(100, 260))
def _eq(t): return 'The table is %s.' % t.html()
def gc_mean(r, lv):
    t = _t(r); m = t.mean(); alt = sum(f * t.edge(i) for i, f in enumerate(t.fs)) / t.n
    return dict(en='A frequency table: %s. The mean is…' % t.html(), vi='Bảng tần số ghép nhóm: %s. Số trung bình là…' % t.html(),
      opts=pick_opts(r, dec(m), [dec(alt), dec(m + 1), dec(m - 1), dec(t.mid(t.mode_group()))], fill=lambda k: dec(m + 2 * k)), ans=0,
      ee='\\(\\bar x=\\dfrac{\\sum n_ix_i}{n}\\) with the midpoints \\(x_i\\): \\(\\bar x=%s\\).' % dec(m), ev='\\(\\bar x=\\dfrac{\\sum n_ix_i}{n}\\) với giá trị đại diện \\(x_i\\): \\(\\bar x=%s\\).' % dec(m))
def gc_median(r, lv):
    t = _t(r); v = t.median(); i = t.med_group()
    return dict(en='A frequency table: %s. The median is…' % t.html(), vi='Bảng tần số ghép nhóm: %s. Trung vị là…' % t.html(),
      opts=pick_opts(r, dec(v), [dec(t.mid(i)), dec(t.edge(i)), dec(v + 1), dec(t.edge(i + 1))], fill=lambda k: dec(v + 2 * k)), ans=0,
      ee='The median group is %s (it contains the \\(\\frac n2\\)-th value). \\(M_e=u+\\dfrac{n/2-C}{n_m}h=%s\\).' % (t.label(i), dec(v)), ev='Nhóm chứa trung vị là %s (chứa giá trị thứ \\(\\frac n2\\)). \\(M_e=u+\\dfrac{n/2-C}{n_m}h=%s\\).' % (t.label(i), dec(v)))
def gc_mode(r, lv):
    t = _t(r); v = t.mode(); i = t.mode_group()
    return dict(en='A frequency table: %s. The mode is…' % t.html(), vi='Bảng tần số ghép nhóm: %s. Mốt là…' % t.html(),
      opts=pick_opts(r, dec(v), [dec(t.mid(i)), dec(t.edge(i)), dec(v + 1), dec(t.edge(i + 1))], fill=lambda k: dec(v + 2 * k)), ans=0,
      ee='The modal group is %s. \\(M_o=u+\\dfrac{n_m-n_{m-1}}{(n_m-n_{m-1})+(n_m-n_{m+1})}h=%s\\).' % (t.label(i), dec(v)), ev='Nhóm chứa mốt là %s. \\(M_o=u+\\dfrac{n_m-n_{m-1}}{(n_m-n_{m-1})+(n_m-n_{m+1})}h=%s\\).' % (t.label(i), dec(v)))
def gc_medgroup(r, lv):
    t = _t(r); i = t.med_group(); L = lambda j: '\\(%s\\)' % t.label(j) if False else t.label(j)
    return dict(en='A frequency table: %s. Which group contains the median?' % t.html(), vi='Bảng tần số ghép nhóm: %s. Nhóm nào chứa trung vị?' % t.html(),
      opts=pick_opts(r, t.label(i), [t.label(j) for j in range(t.k) if j != i]), ans=0,
      ee='\\(\\frac n2=%s\\); the cumulative frequency first reaches it in %s.' % (dec(F(t.n, 2)), t.label(i)), ev='\\(\\frac n2=%s\\); tần số tích lũy lần đầu đạt giá trị này ở nhóm %s.' % (dec(F(t.n, 2)), t.label(i)))
def gc_modegroup(r, lv):
    t = _t(r); i = t.mode_group()
    return dict(en='A frequency table: %s. Which is the modal group?' % t.html(), vi='Bảng tần số ghép nhóm: %s. Nhóm chứa mốt là nhóm nào?' % t.html(),
      opts=pick_opts(r, t.label(i), [t.label(j) for j in range(t.k) if j != i]), ans=0, ee='The modal group has the highest frequency, %d.' % t.fs[i], ev='Nhóm chứa mốt là nhóm có tần số lớn nhất, bằng %d.' % t.fs[i])
def gc_cumul(r, lv):
    t = _t(r); j = r.randint(1, t.k - 1); c = t.cum(j)
    return dict(en='A frequency table: %s. How many values are less than %d?' % (t.html(), t.edge(j)), vi='Bảng tần số ghép nhóm: %s. Có bao nhiêu giá trị nhỏ hơn %d?' % (t.html(), t.edge(j)),
      opts=pick_opts(r, str(c), [str(c + t.fs[j]), str(c + 1), str(c - 1), str(t.n - c)], fill=lambda k: str(c + 3 * k)), ans=0, ee='Add the frequencies of the groups before %d: %d.' % (t.edge(j), c), ev='Cộng tần số các nhóm đứng trước %d: %d.' % (t.edge(j), c))
def gc_n2(r, lv):
    t = _t(r); i = t.med_group(); C = t.cum(i)
    return dict(en='A frequency table: %s. For the median group, the cumulative frequency before it is…' % t.html(), vi='Bảng tần số ghép nhóm: %s. Tần số tích lũy của các nhóm đứng trước nhóm chứa trung vị là…' % t.html(),
      opts=pick_opts(r, str(C), [str(C + t.fs[i]), str(F(t.n, 2)) if F(t.n, 2).denominator == 1 else str(C + 1), str(t.n - C), str(C + 2)], fill=lambda k: str(C + 3 * k)), ans=0, ee='\\(C=%d\\).' % C, ev='\\(C=%d\\).' % C)
M9G = [gc_mean, gc_median, gc_mode, gc_medgroup, gc_modegroup, gc_cumul, gc_mean, gc_median]
