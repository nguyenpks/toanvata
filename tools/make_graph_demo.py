# -*- coding: utf-8 -*-
"""Sinh demo/graph-demo.html: bộ ví dụ cấu hình mẫu cho hệ thống đồ thị và hình vẽ (xem docs/GRAPH.md).
Chạy:  python tools/make_graph_demo.py   rồi mở http://localhost:8000/demo/graph-demo.html"""
import os, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mb_lib import *
GRAPH, GEO = GRAPH_LIVE, GEO_LIVE    # demo của bộ vẽ tương tác JSXGraph (bài học dùng hình LaTeX tĩnh)
import math

def sec(title, *figs): return '<h2>%s</h2>' % title + ''.join(figs)
PI = math.pi
D = []
D.append(sec('1. Hàm đa thức: cực trị, điểm uốn, đồng biến – nghịch biến', GRAPH({
  'view': [-4, 4, -5, 5], 'functions': [{'f': 'x^3-3x', 'label': 'y = x³ − 3x'}],
  'mark': {'roots': [0], 'yint': [0], 'extrema': [0], 'inflections': [0]}, 'monotone': {'f': 0}},
  cap=('y = x³ − 3x: roots, extrema, inflection point.', 'y = x³ − 3x: nghiệm, cực trị, điểm uốn.'), alt=('Graph of y = x³ − 3x', '')) ))
D.append(sec('2. Hàm phân thức: tiệm cận đứng và tiệm cận xiên (không nối qua tiệm cận)', GRAPH({
  'view': [-8, 10, -12, 14], 'functions': [{'f': '(x^2-1)/(x-2)', 'label': 'y = (x² − 1)/(x − 2)'}],
  'asymptotes': [{'type': 'v', 'x': 2}, {'type': 'oblique', 'm': 1, 'b': 2}], 'mark': {'roots': [0], 'yint': [0]}},
  cap=('Vertical asymptote x = 2 and oblique asymptote y = x + 2.', 'Tiệm cận đứng x = 2 và tiệm cận xiên y = x + 2.'), alt=('Rational function graph', ''))))
D.append(sec('3. Hàm lượng giác: trục chia theo π', GRAPH({
  'view': [-2 * PI - 0.5, 2 * PI + 0.5, -2, 2], 'pi': True,
  'functions': [{'f': 'sin(x)', 'label': 'y = sin x'}, {'f': 'cos(x)', 'label': 'y = cos x'}],
  'mark': {'intersections': [[0, 1]]}}, cap=('sin x and cos x share the same period 2π.', 'sin x và cos x cùng chu kì 2π.'), alt=('Sine and cosine graphs', ''))))
D.append(sec('4. Hàm tan: ngắt nhánh tại x = π/2 + kπ', GRAPH({
  'view': [-5, 5, -6, 6], 'pi': True, 'functions': [{'f': 'tan(x)', 'label': 'y = tan x'}],
  'asymptotes': [{'type': 'v', 'x': PI / 2}, {'type': 'v', 'x': -PI / 2}, {'type': 'v', 'x': 3 * PI / 2}, {'type': 'v', 'x': -3 * PI / 2}]},
  alt=('Tangent graph', ''))))
D.append(sec('5. Hàm mũ và logarit (đối xứng qua y = x, tỉ lệ 1:1)', GRAPH({
  'view': [-4, 7, -4, 7], 'equal': True,
  'functions': [{'f': '2^x', 'label': 'y = 2ˣ'}, {'f': 'log(2,x)', 'label': 'y = log₂ x'}, {'f': 'x', 'label': 'y = x', 'dash': True, 'color': '#64748b', 'width': 1.6}],
  'asymptotes': [{'type': 'h', 'y': 0, 'color': '#c2410c'}, {'type': 'v', 'x': 0, 'color': '#1d4ed8'}], 'mark': {'yint': [0]}}, alt=('Exponential and logarithm', ''))))
D.append(sec('6. Hàm căn thức, trị tuyệt đối, hàm từng đoạn', GRAPH({
  'view': [-5, 7, -3, 6],
  'functions': [{'f': 'sqrt(x+1)', 'label': 'y = √(x + 1)'}, {'f': 'abs(x-2)', 'label': 'y = |x − 2|'},
                {'f': 'x+3', 'domain': [-5, -2], 'open': [False, True], 'color': '#7c3aed', 'label': 'hàm từng đoạn'},
                {'f': '-1', 'domain': [-2, 0], 'open': [False, True], 'color': '#7c3aed'}],
  'mark': {'extrema': [1]}}, alt=('Radical, absolute value and piecewise functions', ''))))
D.append(sec('7. Tham số bằng thanh trượt: y = ax² + bx + c', GRAPH({
  'view': [-6, 6, -6, 8], 'params': [{'name': 'a', 'min': -3, 'max': 3, 'value': 1, 'step': 0.1}, {'name': 'b', 'min': -5, 'max': 5, 'value': 0, 'step': 0.1}, {'name': 'c', 'min': -5, 'max': 5, 'value': -2, 'step': 0.1}],
  'functions': [{'f': 'a*x^2+b*x+c', 'label': 'y = ax² + bx + c'}]}, alt=('Parabola with sliders', ''))))
D.append(sec('8. Tiếp tuyến di động', GRAPH({
  'view': [-3, 3, -4, 4], 'functions': [{'f': 'x^3-2x', 'label': 'f(x) = x³ − 2x'}], 'tangent': {'f': 0, 'at': 1, 'min': -2.5, 'max': 2.5}}, alt=('Tangent line moving along a cubic', ''))))
D.append(sec('9. Hình học phẳng: đường cao, trung tuyến, phân giác (kéo các đỉnh)', GEO({
  'view': [-6, 8, -4, 7], 'steps': [
    {'type': 'point', 'id': 'A', 'at': [-4, -2]}, {'type': 'point', 'id': 'B', 'at': [5, -2]}, {'type': 'point', 'id': 'C', 'at': [1, 5]},
    {'type': 'polygon', 'through': ['A', 'B', 'C']}, {'type': 'segment', 'id': 'AB', 'through': ['A', 'B'], 'style': {'visible': False}},
    {'type': 'altitude', 'from': 'C', 'to': 'AB', 'foot': 'H', 'footName': 'H'},
    {'type': 'median', 'from': 'A', 'to': ['B', 'C'], 'foot': 'M', 'footName': 'M'},
    {'type': 'bisector', 'angle': ['A', 'B', 'C']},
    {'type': 'angle', 'points': ['B', 'H', 'C'], 'radius': 0.7}]},
  cap=('Altitude CH is built as a true perpendicular.', 'Đường cao CH được dựng bằng quan hệ vuông góc thật.'), alt=('Triangle with altitude, median and bisector', ''))))
D.append(sec('10. Đường tròn và tiếp tuyến; đường song song', GEO({
  'view': [-6, 8, -5, 6], 'steps': [
    {'type': 'point', 'id': 'O', 'at': [-1.5, 0]}, {'type': 'point', 'id': 'R', 'at': [1.5, 0]},
    {'type': 'circle', 'id': 'c', 'center': 'O', 'through': 'R'}, {'type': 'glider', 'id': 'T', 'at': [-1.5, 3], 'on': 'c'},
    {'type': 'tangent', 'center': 'O', 'at': 'T', 'showRadius': True},
    {'type': 'point', 'id': 'P', 'at': [4, 3]}, {'type': 'point', 'id': 'Q', 'at': [7, 0]}, {'type': 'line', 'id': 'PQ', 'through': ['P', 'Q']},
    {'type': 'point', 'id': 'S', 'at': [4, -3]}, {'type': 'parallel', 'through': 'S', 'to': 'PQ'}]}, alt=('Circle tangent and parallel lines', ''))))
D.append(sec('11. Hình không gian (TikZ → SVG, hình tĩnh): chóp S.ABCD', GEO3D({
  'box': [[-3, 3], [-3, 3], [-1, 4]], 'points': {'A': [-2, -2, 0], 'B': [2, -2, 0], 'C': [2, 2, 0], 'D': [-2, 2, 0], 'S': [0, 0, 3.2]},
  'polygons': [['A', 'B', 'C', 'D']], 'segments': [['S', 'A'], ['S', 'B'], ['S', 'C'], ['S', 'D']]}, alt=('Pyramid S.ABCD', ''))))
page = '''<!DOCTYPE html>
<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Thử nghiệm hệ thống đồ thị và hình vẽ – MathBridge</title>
<link rel="stylesheet" href="../css/lesson.css"><link rel="stylesheet" href="../css/lesson-kit-v2.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/jsxgraph@1.9.2/distrib/jsxgraph.css"><link rel="stylesheet" href="../css/mb-graph.css">
<style>body{max-width:980px;margin:0 auto;padding:16px}h2{margin-top:28px}</style></head>
<body data-level="1"><article><h1>Thử nghiệm hệ thống đồ thị và hình vẽ</h1>
<p>Trang này do <code>tools/make_graph_demo.py</code> sinh ra; mỗi hình là một cấu hình mẫu (xem <code>docs/GRAPH.md</code>).</p>
%s</article>
<script src="https://cdn.jsdelivr.net/npm/jsxgraph@1.9.2/distrib/jsxgraphcore.js"></script>
<script src="../js/mb-graph-core.js"></script><script src="../js/mb-graph.js"></script></body></html>''' % ''.join(D)
os.makedirs(os.path.join(ROOT, 'demo'), exist_ok=True)
open(os.path.join(ROOT, 'demo', 'graph-demo.html'), 'w', encoding='utf-8').write(page.replace('../../../img/', '../img/'))
print('demo/graph-demo.html', len(page))
