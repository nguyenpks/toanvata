# -*- coding: utf-8 -*-
"""Chạy toàn bộ kiểm thử:  python tests/run_all.py"""
import subprocess, sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
steps = [(['node', 'tests/test-graph-core.js'], 'Lõi toán học của đồ thị'), (['node', 'tests/test-lesson-graphs.js'], 'Toán học của đồ thị trong bài (tiệm cận, lỗ thủng, đầu mút)'), ([sys.executable, 'tools/build_all.py', '--check'], 'Mô hình bài học'),
         ([sys.executable, 'tools/make_graph_demo.py'], 'Sinh trang demo'), ([sys.executable, 'tests/test-graph-ui.py'], 'Giao diện đồ thị / hình học / 3D (giả lập)'),
         ([sys.executable, 'tests/test-lessons-g11.py', '10'], 'Các bài lớp 10'),
         ([sys.executable, 'tests/test-lessons-g11.py', '11'], 'Các bài lớp 11'),
         ([sys.executable, 'tests/test-lessons-g11.py', '12'], 'Các bài lớp 12'),
         ([sys.executable, 'tests/test-geometry-notation.py'], 'Ký hiệu hình học theo SGK'),
         ([sys.executable, 'tests/test-mathjax.py'], 'Công thức: ngoặc, môi trường, ký tự điều khiển'),
         ([sys.executable, 'tests/test-typeset-queue.py'], 'Hàng đợi dựng công thức (MathJax giả)'),
         ([sys.executable, 'tests/check_html_snapshot.py'], 'So sánh HTML với bản gốc (baseline)')]
bad = 0
for cmd, name in steps:
    r = subprocess.run(cmd, capture_output=True, text=True); ok = r.returncode == 0; bad += (not ok)
    print(('✓ ' if ok else '✗ ') + name)
    if not ok: print(r.stdout[-1500:], r.stderr[-800:])
sys.exit(1 if bad else 0)
