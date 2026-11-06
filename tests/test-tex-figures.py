# -*- coding: utf-8 -*-
"""Kiểm tra hình vẽ LaTeX trong bài học:  python tests/test-tex-figures.py
- Mọi hình là SVG tĩnh biên dịch từ LaTeX (img/tex/*.svg từ PGFPlots/tkz-euclide/TikZ; img/fig3d/*.svg từ TikZ 3D), có tệp .tex nguồn.
- Không còn bảng vẽ tương tác (data-mbg) hay SVG viết tay chèn trực tiếp trong bài.
- Mọi tiệm cận (khai báo hoặc tự phát hiện) được vẽ bằng kiểu 'asym' = NÉT ĐỨT."""
import os, re, json, glob, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fails = []
def ok(c, m):
    if not c: fails.append(m); print('  ✗', m)
n = {'tex': 0, 'fig3d': 0, 'asym': 0}
for f in sorted(glob.glob(os.path.join(ROOT, 'lessons', '**', '*.html'), recursive=True)):
    h = open(f, encoding='utf-8').read(); r = os.path.relpath(f, ROOT)
    ok('data-mbg' not in h, r + ': còn bảng vẽ tương tác data-mbg')
    ok('<svg' not in h, r + ': còn SVG viết tay chèn trực tiếp')
    for d, k in re.findall(r'img/(tex|fig3d)/([0-9a-f]{16})\.svg', h):
        n['tex' if d == 'tex' else 'fig3d'] += 1
        base = os.path.join(ROOT, 'img', d, k)
        ok(os.path.exists(base + '.svg'), r + ': thiếu ' + d + '/' + k + '.svg')
        ok(os.path.exists(base + '.tex'), r + ': thiếu nguồn LaTeX ' + d + '/' + k + '.tex')
        if d != 'tex' or not os.path.exists(base + '.tex'): continue
        tex = open(base + '.tex', encoding='utf-8').read()
        ok('asym/.style={asy, line width=0.9pt, dash pattern=' in tex, r + ': kiểu tiệm cận không phải nét đứt (' + k + ')')
        if os.path.exists(base + '.json'):
            cfg = json.load(open(base + '.json', encoding='utf-8'))
            want = len([a for a in cfg.get('asymptotes', []) if a.get('type') != 'v' or cfg['view'][0] < a['x'] < cfg['view'][1]])
            got = len(re.findall(r'\\(?:draw|addplot)\[asym', tex))
            n['asym'] += got
            ok(got >= want, r + ': đồ thị %s khai báo %d tiệm cận nhưng chỉ vẽ %d đường nét đứt' % (k, want, got))
print(('✗' if fails else '✓') + ' hình LaTeX: %d hình 2D (PGFPlots/tkz-euclide/TikZ), %d hình không gian (TikZ 3D), %d đường tiệm cận nét đứt; %d lỗi' % (n['tex'], n['fig3d'], n['asym'], len(fails)))
sys.exit(1 if fails else 0)
