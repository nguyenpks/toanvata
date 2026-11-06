# -*- coding: utf-8 -*-
"""Thư viện hình khối dùng chung cho hình vẽ tĩnh (GEO3D -> TikZ -> SVG).
fig(kind, pts={...}, seg=[...], poly=[...], hl={...}) trả về cấu hình cho GEO3D.
  kind: 'pyr'  – chóp S.ABCD đáy hình bình hành (O = AC ∩ BD có sẵn khi gọi pt('O'))
        'pyrsq' – chóp S.ABCD đáy hình vuông, SA ⟂ (ABCD)
        'tet'  – tứ diện ABCD
        'cube' – hình lập phương ABCD.A′B′C′D′ (cạnh 4)
        'box'  – hình hộp ABCD.A′B′C′D′ (xiên)
  pts: điểm thêm, giá trị là tọa độ hoặc biểu thức kiểu 'mid:S,C', 'on:A,B,1/3' (AM = 1/3 AB), 'cen:A,B,C'.
  seg: đoạn thêm ['M', 'N'] hoặc ['M', 'N', {'color': HL}]; poly: mặt tô màu; hl: tô màu cạnh có sẵn {('A','B'): '#c2410c'}."""
from fractions import Fraction as F

HL, BL, GR, PU = '#c2410c', '#1d4ed8', '#0f766e', '#7c3aed'
BASE = {
 'pyr': ({'A': (-3, -2, 0), 'B': (2, -2, 0), 'C': (3, 2, 0), 'D': (-2, 2, 0), 'S': (0, 0, 3.4)}, ['S', 'A', 'B', 'C', 'D']),
 'pyrsq': ({'A': (-2, -2, 0), 'B': (2, -2, 0), 'C': (2, 2, 0), 'D': (-2, 2, 0), 'S': (-2, -2, 3.6)}, ['S', 'A', 'B', 'C', 'D']),
 'tet': ({'B': (-2.6, 0, 0), 'C': (0.8, -2, 0), 'D': (2.8, 1.6, 0), 'A': (-0.2, 0.3, 3.4)}, ['A', 'B', 'C', 'D']),
 'cube': ({'A': (0, 0, 0), 'B': (4, 0, 0), 'C': (4, 4, 0), 'D': (0, 4, 0), 'A′': (0, 0, 4), 'B′': (4, 0, 4), 'C′': (4, 4, 4), 'D′': (0, 4, 4)}, ['A', 'B', 'C', 'D', 'A′', 'B′', 'C′', 'D′']),
 'box': ({'A': (-3, -2, 0), 'B': (1, -2, 0), 'C': (3, 1.5, 0), 'D': (-1, 1.5, 0), 'A′': (-2.2, -1.4, 3), 'B′': (1.8, -1.4, 3), 'C′': (3.8, 2.1, 3), 'D′': (-0.2, 2.1, 3)}, ['A', 'B', 'C', 'D', 'A′', 'B′', 'C′', 'D′']),
}

def _val(P, v):
    if not isinstance(v, str): return tuple(float(x) for x in v)
    kind, arg = v.split(':', 1); a = arg.split(',')
    if kind == 'mid': p, q = P[a[0]], P[a[1]]; return tuple((x + y) / 2 for x, y in zip(p, q))
    if kind == 'on': p, q = P[a[0]], P[a[1]]; t = float(F(a[2])); return tuple(x + t * (y - x) for x, y in zip(p, q))
    if kind == 'cen': ps = [P[n] for n in a]; return tuple(sum(c) / len(ps) for c in zip(*ps))
    if kind == 'meet':          # giao của hai đường thẳng a0a1 và a2a3 (cùng mặt phẳng)
        import numpy as np
        p, u = np.array(P[a[0]]), np.array(P[a[1]]) - np.array(P[a[0]]); q, w = np.array(P[a[2]]), np.array(P[a[3]]) - np.array(P[a[2]])
        t = np.linalg.lstsq(np.array([u, -w]).T, q - p, rcond=None)[0][0]; return tuple(float(x) for x in p + t * u)
    raise ValueError(v)

def fig(kind, pts=None, seg=None, poly=None, hl=None, **kw):
    base, solid = BASE[kind]
    P = {k: tuple(float(x) for x in v) for k, v in base.items()}
    if kind in ('pyr', 'pyrsq') and 'O' in (pts or {}) and pts['O'] == 'O': pts = dict(pts); pts['O'] = 'mid:A,C'
    for k, v in (pts or {}).items(): P[k] = _val(P, v)
    segs = []
    for s in seg or []:
        o = dict(s[2]) if len(s) > 2 else {}
        if isinstance(o.get('color'), str) and 'width' not in o: o['width'] = 3.6
        segs.append([s[0], s[1], o] if o else [s[0], s[1]])
    for (a, b), c in (hl or {}).items(): segs.append([a, b, {'color': c, 'width': 3.6}])
    polys = []
    for pg in poly or []:
        polys.append(pg if isinstance(pg, dict) else {'points': list(pg), 'fill': '#86e0bd', 'opacity': .35})
    cfg = {'solid': solid, 'points': P, 'segments': segs, 'polygons': polys, 'px': 360}
    cfg.update(kw)
    return cfg

def FILL(names, color='#86e0bd', op=.35): return {'points': list(names), 'fill': color, 'opacity': op}
