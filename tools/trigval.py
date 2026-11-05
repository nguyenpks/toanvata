# -*- coding: utf-8 -*-
"""Giá trị lượng giác đặc biệt (dạng tex) của góc 0°–180°, kiểm tra bằng số."""
import math
_S = {0: '0', 30: '\\dfrac{1}{2}', 45: '\\dfrac{\\sqrt2}{2}', 60: '\\dfrac{\\sqrt3}{2}', 90: '1'}
_T = {0: '0', 30: '\\dfrac{\\sqrt3}{3}', 45: '1', 60: '\\sqrt3'}
_C = {30: '\\sqrt3', 45: '1', 60: '\\dfrac{\\sqrt3}{3}', 90: '0'}
def _neg(s): return '0' if s == '0' else '-' + s
def val(fn, a):
    """Giá trị đúng của sin/cos/tan/cot tại góc a (độ) hoặc None nếu không xác định."""
    b = 180 - a if a > 90 else a
    if fn == 'sin': return _S[b]
    if fn == 'cos': return _S[90 - b] if a <= 90 else _neg(_S[90 - b])
    if fn == 'tan':
        if a == 90: return None
        return _T[b] if a <= 90 else _neg(_T[b])
    if fn == 'cot':
        if a in (0, 180): return None
        return _C[b] if a <= 90 else _neg(_C[b])
def num(fn, a):
    r = math.radians(a)
    return {'sin': math.sin(r), 'cos': math.cos(r), 'tan': math.tan(r) if a != 90 else None, 'cot': 1 / math.tan(r) if a not in (0, 180) and a != 90 else (0.0 if a == 90 else None)}[fn]
def _eval(t):
    import re
    s = t.replace('\\dfrac{', '(').replace('}{', ')/(').replace('\\sqrt', 'math.sqrt')
    s = re.sub(r'math\.sqrt(\d)', r'math.sqrt(\1)', s).replace('}', ')')
    s = s.replace('math.sqrt2)', 'math.sqrt(2))').replace('math.sqrt3)', 'math.sqrt(3))')
    s = re.sub(r'math\.sqrt(\d)(?!\d*\))', r'math.sqrt(\1)', s)
    return s
ANG = [0, 30, 45, 60, 90, 120, 135, 150, 180]
def selftest():
    for fn in ('sin', 'cos', 'tan', 'cot'):
        for a in ANG:
            v = val(fn, a); n = num(fn, a)
            assert (v is None) == (n is None), (fn, a)
            if v is not None:
                t = v.replace('\\dfrac{\\sqrt2}{2}', '(2**.5/2)').replace('\\dfrac{\\sqrt3}{2}', '(3**.5/2)').replace('\\dfrac{\\sqrt3}{3}', '(3**.5/3)').replace('\\dfrac{1}{2}', '0.5').replace('\\sqrt3', '(3**.5)')
                assert abs(eval(t) - n) < 1e-9, (fn, a, v, n)
selftest()
