# Hình vẽ Toán học bằng LaTeX (PGFPlots, tkz-euclide, TikZ) — từ Đợt 11

> **Hiện hành:** mọi đồ thị và hình minh họa trong bài là **hình tĩnh** viết bằng LaTeX, biên dịch **XeLaTeX → PDF → SVG** (`pdftocairo -svg`), lưu đệm theo mã băm.
>
> | Loại hình | Gói LaTeX | Hàm Python | Thư mục |
> |---|---|---|---|
> | Đồ thị hàm số, dữ liệu | PGFPlots (+ pgfplotstable) | `GRAPH(cfg, …)`, `svg_graph(f, …)` | `img/tex/` |
> | Hình học phẳng | tkz-euclide (+ TikZ angles, calc) | `GEO(cfg, …)`, `region(…)` | `img/tex/` |
> | Hình học không gian | TikZ 3D (phép chiếu song song, nét khuất tự tính) | `GEO3D(cfg, …)` | `img/fig3d/` |
> | Biểu đồ Venn, trục số | TikZ | `venn2(…)`, `mb_pgf.venn_ops_svg()`, `mb_pgf.numberline_svg(…)` | `img/tex/` |
>
> * Bộ chuyển: `tools/mb_pgf.py`; số liệu (nhánh đồ thị ngắt tại tiệm cận, nghiệm, cực trị, giao điểm, khoảng đơn điệu, tiếp tuyến) tính bằng chính lõi `js/mb-graph-core.js` qua `tools/graph_eval.js` (Node).
> * **Tiệm cận luôn vẽ NÉT ĐỨT** (kiểu `asym`): cả tiệm cận khai báo trong `asymptotes` lẫn tiệm cận đứng/ngang/xiên **tự phát hiện** cho hàm có cực điểm. Đường dóng (`guides`) vẽ chấm mảnh để không nhầm với tiệm cận.
> * Thay thanh trượt bằng **họ đồ thị**: `'family': [{'a': 2, '_label': 'y = 2ˣ'}, {'a': 0.5, …}]` vẽ mỗi bộ tham số một đường; `tangent.at` nhận danh sách để vẽ nhiều tiếp tuyến.
> * Mỗi đồ thị có kèm `img/tex/<băm>.json` (cấu hình gốc) để `tests/test-lesson-graphs.js` kiểm tra toán học; `tests/test-tex-figures.py` kiểm tra đủ tệp và tiệm cận nét đứt. Tệp `.tex` nằm cạnh `.svg` để giáo viên chỉnh tay khi cần.
>
> Phần dưới đây mô tả cú pháp cấu hình (vẫn dùng nguyên) và bộ vẽ tương tác JSXGraph cũ (chỉ còn dùng trong `demo/graph-demo.html`).

# Hệ thống đồ thị và hình vẽ Toán học (JSXGraph)

Mỗi hình trong bài là một khối `<div class="mbg" data-mbg='{...}'>` do hàm `GRAPH`, `GEO`, `GEO3D` (trong `tools/mb_lib.py`) sinh ra từ một cấu hình Python. Thư viện **JSXGraph** chỉ được tải ở các bài có hình (`page.optional` trong `config/model.json`); các bài khác không bị ảnh hưởng.

| Thành phần | Tệp | Vai trò |
|---|---|---|
| Lõi toán học | `js/mb-graph-core.js` | đọc biểu thức, lấy mẫu đồ thị **ngắt nhánh tại gián đoạn/tiệm cận**, tìm nghiệm, cực trị, điểm uốn, đơn điệu, nhãn π |
| Bộ hiển thị | `js/mb-graph.js` | dùng JSXGraph vẽ trục, lưới, đồ thị, hình học, 3D; thanh công cụ; thanh trượt |
| Giao diện | `css/mb-graph.css` | khung, nút, thanh trượt |
| Công nghệ | JSXGraph 1.9.2 (jsDelivr), MathJax cho công thức; GeoGebra/Desmos là lựa chọn thêm |

## 1. Đồ thị hàm số: `GRAPH(cfg, cap=(en, vi), alt=(en, vi), height=360)`
```python
GRAPH({'view': [-4, 4, -5, 5],                       # [xmin, xmax, ymin, ymax]
       'functions': [{'f': 'x^3-3x', 'label': 'y = x³ − 3x'}],
       'mark': {'roots': [0], 'yint': [0], 'extrema': [0], 'inflections': [0]},
       'monotone': {'f': 0}},                          # tô màu khoảng đồng biến / nghịch biến
      cap=('English caption', 'Chú thích tiếng Việt'), alt=('Alt text', ''))
```
| Khóa | Ý nghĩa |
|---|---|
| `view` | khung nhìn ban đầu; nút ⟲ đặt lại về đây |
| `functions[]` | `f` biểu thức theo `x`; `label`; `color`; `dash`; `width`; `domain:[a,b]` và `open:[trái, phải]` (đầu mút hở ○ / đặc ●) – dùng để vẽ **hàm từng đoạn** |
| `params[]` | thanh trượt `{name, min, max, value, step}`, dùng tên đó trong biểu thức (`a*x^2+b*x+c`) |
| `asymptotes[]` | `{'type':'v','x':2}`, `{'type':'h','y':1}`, `{'type':'oblique','m':1,'b':2}` |
| `holes`, `points`, `texts` | điểm thủng `[x,y,nhãn]`, điểm tùy ý `{x,y,label,open}`, chữ `{x,y,text}` |
| `mark` | `roots`, `yint`, `extrema`, `inflections` (danh sách chỉ số hàm), `intersections` (danh sách cặp chỉ số). Tính bằng số trên `markRange` (mặc định: khung nhìn mở rộng ×3). **Không dùng cùng `params`** |
| `monotone` | `{f:0}` tô khoảng đồng biến (xanh) và nghịch biến (cam) |
| `highlights[]` | `{f, x:[a,b], color}` tô đậm một đoạn của đồ thị |
| `tangent` | `{f, at, min, max}` tiếp tuyến di động với thanh trượt x₀ và dòng đọc f(x₀), f′(x₀) |
| `pi: True` | trục x chia theo bội của π (π/2, π, 3π/2…) và nhãn điểm theo π |
| `equal: True` | giữ tỉ lệ 1:1 |
| `grid`, `legend`, `xname`, `yname` | bật/tắt lưới và chú giải; tên trục |

Biểu thức hỗ trợ: `+ - * / ^`, nhân ngầm (`2x`, `2(x+1)`, `(x+1)(x-1)`), `sin cos tan cot sec csc asin acos atan sinh cosh tanh sqrt cbrt abs exp ln log log2 floor ceil round sign min max pow root`, hằng `pi`, `e`, ký hiệu `π`, `√`. `log(x)` là logarit thập phân, `log(a, x)` là logarit cơ số a. Hàm được hiểu trong tập số thực (căn của số âm, ln của số không dương cho ra “không xác định” và không được vẽ).

**Đảm bảo đúng toán học:** phát hiện gián đoạn bằng chia đôi khoảng nên đường dốc đứng liên tục (như `e^(10x)`) không bị cắt nhầm, còn tiệm cận (`1/x`, `tan x`) và chỗ nhảy của hàm từng đoạn thì bị ngắt, không nối. Đồ thị được lấy mẫu lại mỗi khi phóng, thu hoặc di chuyển.

**Công cụ cho học sinh:** ＋ − (phóng/thu), ↔＋ ↔－ (giãn/co trục x), ↕＋ ↕－ (trục y), **1:1** (cùng tỉ lệ hai trục), ⟲ (đặt lại). Kéo để di chuyển; Shift + cuộn chuột hoặc chụm hai ngón để thu phóng. Nhãn nút đổi sang tiếng Anh ở Mức 3.

## 2. Hình học phẳng: `GEO(cfg, ...)`
Các bước dựng dùng **ràng buộc hình học thật** của JSXGraph, nên khi kéo điểm các quan hệ vẫn đúng (không vẽ theo cảm tính).
```python
GEO({'view': [-6, 8, -4, 7], 'steps': [
  {'type': 'point', 'id': 'A', 'at': [-4, -2]}, {'type': 'point', 'id': 'B', 'at': [5, -2]}, {'type': 'point', 'id': 'C', 'at': [1, 5]},
  {'type': 'polygon', 'through': ['A', 'B', 'C']}, {'type': 'segment', 'id': 'AB', 'through': ['A', 'B']},
  {'type': 'altitude', 'from': 'C', 'to': 'AB', 'foot': 'H', 'footName': 'H'},
  {'type': 'angle', 'points': ['B', 'H', 'C']}]})        # dấu vuông chỉ hiện khi góc đúng bằng 90°
```
| `type` | Tham số | Dựng bằng |
|---|---|---|
| `point`, `glider` (điểm chạy trên đường tròn/đường) | `at`, `on` | điểm tự do / điểm trên đối tượng |
| `midpoint`, `intersection` | `of`, `index` | trung điểm, giao điểm |
| `segment`, `line`, `ray`, `lineeq` | `through` ; `a,b,c` cho `ax+by+c=0` | đoạn, đường thẳng, tia, đường theo phương trình |
| `polygon`, `circle`, `arc` | `through` ; `center`+`through` hoặc `radius` ; `points` | đa giác, đường tròn, cung |
| `perpendicular` | `from` (điểm), `to` (đường), `foot`, `footName` | `perpendicular` của JSXGraph |
| `parallel` | `through` (điểm), `to` (đường) | `parallel` của JSXGraph |
| `altitude`, `median` | `from`, `to` (cạnh / `[B, C]`), `foot` | đường vuông góc hạ xuống cạnh; trung điểm |
| `bisector`, `perpbisector` | `angle:[A, đỉnh, B]` ; `of` | phân giác; trung trực |
| `tangent` | `center`, `at` (điểm trên đường tròn) | vuông góc với bán kính tại tiếp điểm |
| `angle` | `points:[A, đỉnh, B]`, `radius` | góc nhỏ hơn, nhãn đo bằng độ, ô vuông khi 90° |
| `curve` | `f` | đồ thị hàm trong hình học tọa độ (`'axes': True` để hiện trục) |

`style` trong mỗi bước (ví dụ `{'visible': False}`, `{'strokeColor': '#c2410c'}`) ghi đè kiểu mặc định.

## 3. Hình không gian: `GEO3D(cfg, ...)`
```python
GEO3D({'box': [[-3, 3], [-3, 3], [-1, 4]],
       'points': {'A': (-2, -2, 0), 'B': (2, -2, 0), 'C': (2, 2, 0), 'D': (-2, 2, 0), 'S': (0, 0, 3.2)},
       'polygons': [['A', 'B', 'C', 'D']],                       # hoặc {'points': [...], 'fill': '#86e0bd', 'opacity': .3}
       'segments': [['S', 'A'], ['A', 'C', {'dash': True, 'color': '#64748b'}]]})
```
Kéo hình để xoay. Dùng JSXGraph 3D (cần bản ≥ 1.6; bài dùng 1.9.2). Tọa độ do người soạn cho; trong file bài nên kiểm tra quan hệ bằng vectơ (xem `content/grade11/parallel-in-space.py`, `perpendicularity.py`).

## 4. Hình rất phức tạp: GeoGebra hoặc Desmos
`GRAPH({'kind': ...})` không dùng; thay vào đó dùng `kind` ở cấu hình dựng tay:
- `{'kind':'geogebra', 'app':'graphing'|'geometry'|'3d'|'classic', 'commands':['f(x)=x^2', ...], 'view':[x1,x2,y1,y2]}` (cần Internet, không cần khóa).
- `{'kind':'desmos', 'expressions':['y=x^2', ...], 'view':[...]}` cần khóa Desmos API: đặt trong `config/model.json` → `page.optional[0].meta["mbg-desmos-key"]`.

Dùng JSXGraph cho mọi hình trong bài; chỉ dùng hai engine này khi JSXGraph không đủ.

## 5. Bài tập từng mức khác nhau, cùng dạng: `LEVEL_PRACTICE`
```python
S1 = [[MCQ(1, ...), MCQ(2, ...)], [TF(3, ...)], [SHORT(4, ...)]]      # bộ của Mức 1: nhóm A, B, C
S2, S3 = ...                                                         # cùng số nhóm, cùng số câu, khác số liệu
practice = LEVEL_PRACTICE([('A. Multiple Choice', 'A. Trắc nghiệm'), ('B. True or False', 'B. Đúng hoặc sai'), ('C. Short Answer', 'C. Trả lời ngắn')], {1: S1, 2: S2, 3: S3})
```
Mỗi mức chỉ hiện bộ của mình và điểm chỉ tính các câu của mức đang học. `LV([1], html)` ẩn/hiện bất kỳ nội dung nào theo mức.

## 6. Kiểm thử
```
node tests/test-graph-core.js          # lõi toán học: biểu thức, ngắt nhánh, nghiệm, cực trị, điểm uốn, nhãn π
python tests/test-graph-ui.py          # trang demo: thanh trượt, tiếp tuyến, thu phóng, 1:1, nhãn theo mức, dựng hình học
python tests/test-lessons-g11.py 11    # từng bài lớp 11: bộ bài tập từng mức, điểm, công thức, hình
```
**Giới hạn đã biết:** các kiểm thử ghép nối dùng JSXGraph **giả lập** (`tests/mock-jxg.js`) vì môi trường tạo bài không có Internet; chúng xác nhận cấu hình được chuyển đúng thành các lời gọi dựng hình (ví dụ đường cao dùng `perpendicular`) nhưng **không** thay cho việc xem hình thật. Trước khi phát hành hãy mở `demo/graph-demo.html` (cần Internet) và duyệt mắt từng hình: trục, nhãn π, mũi tên, góc vuông, xoay 3D.

## Cập nhật giai đoạn 2 (độ chính xác của đồ thị)
- `mark.*` được **tính lại theo khung nhìn hiện tại** khi kéo, phóng/thu hoặc đổi tham số (trước đây chỉ tính một lần). Quá 24 điểm cùng loại thì bỏ nhãn để khỏi chồng chữ.
- `mark.roots`: nghiệm bội ≥ 2 được vẽ to hơn và ghi `×m` (ví dụ `(1; 0) ×2`). Lõi: `MBGCore.rootsDetailed`.
- `mark.holes: [chỉ số hàm]`: tự nhận lỗ thủng (gián đoạn bỏ được). Lõi: `MBGCore.holes`. Khai báo tay `holes: [[x, y, nhãn]]` vẫn dùng được và được kiểm thử.
- `guides: [{type:'h'|'v', y|x}]`: đường dóng tham khảo (nét mảnh, chấm). Dùng thay cho `asymptotes` khi đường đó KHÔNG phải tiệm cận (ví dụ y = giới hạn tại lỗ thủng).
- `monotone`: khoảng đồng/nghịch biến cắt tại cực trị VÀ tại điểm gián đoạn, chỉ trong tập xác định; đúng với x³ (đạo hàm 0 mà không đổi dấu) và 1/x.
- `tests/test-lesson-graphs.js` kiểm tra toán học mọi đồ thị trong bài: tiệm cận khai báo phải đúng với hàm, lỗ thủng phải đúng giá trị giới hạn.

## Cập nhật giai đoạn 3 (hình học)
- **Hình khối** (`kind: '3d'`): thêm `solid: true` (mọi điểm là đỉnh) hoặc `solid: ['S','A','B','C','D']` (chỉ các đỉnh của khối; điểm phụ như trung điểm, tâm đáy để ngoài danh sách). Hệ thống tự tính mặt/cạnh bằng bao lồi, rồi **vẽ nét đứt cho cạnh bị che và cập nhật khi người học xoay hình**. Cạnh đã khai báo trong `segments` giữ màu/độ dày riêng; cạnh chưa khai báo được tự vẽ; đường chéo/đường phụ phải khai báo `dash: true`.
- Hướng nhìn lấy từ `view.project3DTo2D` của JSXGraph, chuẩn hóa để người xem ở phía trên lúc khởi tạo. Nếu khi chạy `tests/test-real-render.py` thấy nét đứt rơi vào cạnh phía trước, đảo dấu ban đầu trong `Core.viewDirection`.
- **Đoạn thẳng** (`kind: 'geo'`, bước `segment`): `mark: 'eq' | 'eq2' | 'eq3'` (gạch nhỏ: đoạn bằng nhau), `mark: 'par' | 'par2'` (mũi tên ›: song song). Kích thước theo điểm ảnh, không đổi khi phóng/thu.
- Nhãn điểm tự đẩy ra xa tâm hình (2D lúc khởi tạo; 3D mỗi lần xoay) để không đè lên cạnh. Vẫn có thể đặt tay bằng `off`.
- Ký hiệu theo SGK: xem `docs/KY-HIEU-HINH-HOC.md`; `tests/test-geometry-notation.py` kiểm tra tự động.
