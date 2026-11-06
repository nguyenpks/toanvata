# Bản đồ chương trình ToánvàTA – Toán 10, 11, 12 (Giai đoạn 1)

> **Lưu ý:** đây là chương trình đề xuất, tham khảo cấu trúc sách Toán THPT hiện hành nhưng **chưa được đối chiếu với văn bản chính thức** của Bộ Giáo dục và Đào tạo. Giáo viên cần kiểm tra lại trước khi công bố là chương trình chuẩn.

## Điều chỉnh so với danh mục gợi ý trong đề bài

- Lớp 10: thêm chủ đề *Counting* vào *Probability* (tổ hợp là nền cho xác suất); đổi tên *Probability* thành *Counting and Probability*.
- Lớp 12: bỏ mục *Exponential and Logarithmic Functions* (đã có ở lớp 11 để các lớp kế thừa, không lặp); đổi *Three-Dimensional Geometry* thành *Coordinates in Space* (phương trình mặt phẳng, đường thẳng, mặt cầu trong Oxyz); tách *Statistics* và *Probability*.

## Quy ước

- Mã bài: `g<lớp>-<mã chủ đề ngắn>-<số thứ tự 2 chữ số>`; thư mục: `lessons/grade<lớp>/<thư-mục-chủ-đề>/<tên-bài>.html`.
- Trạng thái: **BUILT** = đã viết đầy đủ; **TEST** = bài kiểm thử kỹ thuật của AI số 1, sẽ được thay bằng nội dung thật ở cùng `id`; **PLANNED** = đã lập kế hoạch, chưa viết. Chỉ bài BUILT/TEST có trong `lessons.json` (tránh liên kết đến file chưa có).
- `prerequisites` của mỗi bài PLANNED mặc định là bài liền trước trong cùng chủ đề; bài đầu chủ đề trỏ đến bài cuối của chủ đề nền tương ứng khi triển khai.

## Grade 10 – Toán lớp 10

| # | Topic – Chủ đề | Mã bài | Bài học | Trạng thái |
|---|---|---|---|---|
| 2 | Mệnh đề và tập hợp – Bài 2 | `g10-sets-01` | Sets and Operations on Sets (gộp cả khoảng và đếm bằng biểu đồ Venn) | BUILT (v3, Bài 2 KNTT) |
| – | (đã gộp vào Bài 2) | `g10-sets-02` | Counting with Venn Diagrams | LOCKED (tạm khóa; nội dung đã gộp vào `g10-sets-01`) |
| – | Algebraic Expressions | `g10-algebra-01` | Introduction to Algebra | LOCKED (ngoài danh mục Toán 10 KNTT) |
| 2 | Algebraic Expressions – Biểu thức đại số | `g10-algebra-02` | Expanding and Factoring | PLANNED |
| 2 | Algebraic Expressions – Biểu thức đại số | `g10-algebra-03` | Rational Expressions | PLANNED |
| 3 | Equations and Inequalities – Phương trình và bất phương trình | `g10-equations-01` | Linear Equations | PLANNED |
| 3 | Equations and Inequalities – Phương trình và bất phương trình | `g10-equations-02` | Systems of Equations | PLANNED |
| 3 | Equations and Inequalities – Phương trình và bất phương trình | `g10-equations-03` | Linear Inequalities | PLANNED |
| 4 | Functions – Hàm số | `g10-functions-01` | Function Notation, Domain and Range | PLANNED |
| 4 | Functions – Hàm số | `g10-functions-02` | Graphs of Functions | PLANNED |
| 4 | Functions – Hàm số | `g10-functions-03` | Increasing and Decreasing Functions | PLANNED |
| 5 | Quadratic Functions – Hàm số bậc hai | `g10-quad-01` | Parabolas and Quadratic Functions | PLANNED |
| 5 | Quadratic Functions – Hàm số bậc hai | `g10-quad-02` | Quadratic Equations | PLANNED |
| 5 | Quadratic Functions – Hàm số bậc hai | `g10-quad-03` | Quadratic Inequalities | PLANNED |
| 6 | Coordinate Geometry – Hình học tọa độ | `g10-coord-01` | Coordinates in the Plane | PLANNED |
| 6 | Coordinate Geometry – Hình học tọa độ | `g10-coord-02` | Equations of Lines | PLANNED |
| 6 | Coordinate Geometry – Hình học tọa độ | `g10-coord-03` | Circles | PLANNED |
| 7 | Vectors – Vectơ | `g10-vectors-01` | Vectors and Their Operations | PLANNED |
| 7 | Vectors – Vectơ | `g10-vectors-02` | The Dot Product | PLANNED |
| 8 | Basic Trigonometry – Lượng giác cơ bản | `g10-trig-01` | Trigonometric Ratios of Angles from 0° to 180° | PLANNED |
| 8 | Basic Trigonometry – Lượng giác cơ bản | `g10-trig-02` | Law of Sines and Law of Cosines | PLANNED |
| 9 | Statistics – Thống kê | `g10-statistics-01` | Measures of Central Tendency | PLANNED |
| 9 | Statistics – Thống kê | `g10-statistics-02` | Measures of Spread | PLANNED |
| 10 | Counting and Probability – Đếm và xác suất | `g10-probability-01` | Counting Rules | PLANNED |
| 10 | Counting and Probability – Đếm và xác suất | `g10-probability-02` | Permutations and Combinations | PLANNED |
| 10 | Counting and Probability – Đếm và xác suất | `g10-probability-03` | Probability of Events | PLANNED |

## Grade 11 – Toán lớp 11

| # | Topic – Chủ đề | Mã bài | Bài học | Trạng thái |
|---|---|---|---|---|
| 1 | Trigonometric Functions – Hàm số lượng giác | `g11-trigf-01` | Bài 1 (KNTT). Trigonometric Values of Oriented Angles – Giá trị lượng giác của góc lượng giác | BUILT (viết lại theo SGK) |
| 1 | Trigonometric Functions – Hàm số lượng giác | `g11-trigf-03` | Bài 2 (KNTT). Trigonometric Formulas – Công thức lượng giác | BUILT (mới) |
| 1 | Trigonometric Functions – Hàm số lượng giác | `g11-trigf-02` | Bài 3 (KNTT). Graphs and Properties – Hàm số lượng giác | BUILT (viết lại theo SGK) |
| 2 | Trigonometric Equations – Phương trình lượng giác | `g11-trige-01` | Bài 4 (KNTT). Basic Trigonometric Equations – Phương trình lượng giác cơ bản | BUILT (mới) |
| 2 | Trigonometric Equations – Phương trình lượng giác | `g11-trige-02` | Solving Trigonometric Equations | PLANNED |
| 3 | Sequences – Dãy số | `g11-sequences-01` | Bài 5 (KNTT). Sequences – Dãy số (gồm tăng/giảm, bị chặn) | BUILT (mới) |
| 3 | Sequences – Dãy số | `g11-sequences-02` | Monotonic and Bounded Sequences | PLANNED |
| 4 | Arithmetic Progressions – Cấp số cộng | `g11-arith-01` | Arithmetic Progressions | PLANNED |
| 4 | Arithmetic Progressions – Cấp số cộng | `g11-arith-02` | Sum of an Arithmetic Progression | PLANNED |
| 5 | Geometric Progressions – Cấp số nhân | `g11-geom-01` | Geometric Progressions | PLANNED |
| 5 | Geometric Progressions – Cấp số nhân | `g11-geom-02` | Sum of a Geometric Progression | PLANNED |
| 6 | Limits – Giới hạn | `g11-limits-01` | Limits of Sequences | PLANNED |
| 6 | Limits – Giới hạn | `g11-limits-02` | Limits of Functions | BUILT |
| 6 | Limits – Giới hạn | `g11-limits-03` | Continuity | PLANNED |
| 7 | Derivatives – Đạo hàm | `g11-derivatives-01` | The Derivative: Definition | BUILT |
| 7 | Derivatives – Đạo hàm | `g11-derivatives-02` | Rules of Differentiation | PLANNED |
| 7 | Derivatives – Đạo hàm | `g11-derivatives-03` | Higher-order Derivatives | PLANNED |
| 8 | Exponential Functions – Hàm số mũ | `g11-exp-01` | Powers and Exponents | PLANNED |
| 8 | Exponential Functions – Hàm số mũ | `g11-exp-02` | Exponential Functions and Equations | BUILT |
| 9 | Logarithmic Functions – Hàm số logarit | `g11-log-01` | Logarithms | PLANNED |
| 9 | Logarithmic Functions – Hàm số logarit | `g11-log-02` | Logarithmic Functions and Equations | PLANNED |
| 10 | Lines and Planes in Space – Đường thẳng và mặt phẳng trong không gian | `g11-space-01` | Points, Lines and Planes in Space | PLANNED |
| 10 | Lines and Planes in Space – Đường thẳng và mặt phẳng trong không gian | `g11-space-02` | Parallel Lines and Planes | BUILT |
| 10 | Lines and Planes in Space – Đường thẳng và mặt phẳng trong không gian | `g11-space-03` | Perpendicularity | BUILT |
| 11 | Statistics and Probability – Thống kê và xác suất | `g11-statprob-01` | Grouped Data and Measures of Spread | PLANNED |
| 11 | Statistics and Probability – Thống kê và xác suất | `g11-statprob-02` | Probability of Compound Events | PLANNED |

## Grade 12 – Toán lớp 12

| # | Topic – Chủ đề | Mã bài | Bài học | Trạng thái |
|---|---|---|---|---|
| 3 | Đường tiệm cận | `g12-deriv-app-01` | Asymptotes of Graphs (Bài 3 KNTT) | BUILT (v2) |
| 1 | Applications of Derivatives – Ứng dụng đạo hàm | `g12-deriv-app-02` | Sketching Graphs of Functions | BUILT |
| 1 | Tính đơn điệu và cực trị | `g12-mono-01` | Monotonicity and Extrema of Functions (Bài 1 KNTT, gộp mono-01 + mono-02) | BUILT (v2) |
| – | (đã gộp vào Bài 1) | `g12-mono-02` | Local Extrema | LOCKED (tạm khóa) |
| 2 | GTLN – GTNN | `g12-mono-03` | Maximum and Minimum Values (Bài 2 KNTT) | BUILT (v2) |
| 3 | Antiderivatives – Nguyên hàm | `g12-antider-01` | Antiderivatives | BUILT |
| 3 | Antiderivatives – Nguyên hàm | `g12-antider-02` | Techniques of Finding Antiderivatives | BUILT |
| 4 | Integrals – Tích phân | `g12-integrals-01` | Definite Integrals | PLANNED |
| 4 | Integrals – Tích phân | `g12-integrals-02` | Properties and Calculation of Integrals | PLANNED |
| 5 | Applications of Integrals – Ứng dụng tích phân | `g12-int-app-01` | Area of a Plane Region | PLANNED |
| 5 | Applications of Integrals – Ứng dụng tích phân | `g12-int-app-02` | Volume of a Solid | PLANNED |
| 6 | Vectors in Space – Vectơ trong không gian | `g12-vecspace-01` | Vectors in Space | PLANNED |
| 6 | Vectors in Space – Vectơ trong không gian | `g12-vecspace-02` | Coordinates of Vectors | PLANNED |
| 7 | Coordinates in Space – Tọa độ trong không gian | `g12-oxyz-01` | Equation of a Plane | PLANNED |
| 7 | Coordinates in Space – Tọa độ trong không gian | `g12-oxyz-02` | Equation of a Line in Space | PLANNED |
| 7 | Coordinates in Space – Tọa độ trong không gian | `g12-oxyz-03` | Equation of a Sphere | PLANNED |
| 8 | Statistics – Thống kê | `g12-statistics-01` | Range and Interquartile Range | PLANNED |
| 8 | Statistics – Thống kê | `g12-statistics-02` | Variance and Standard Deviation | PLANNED |
| 9 | Probability – Xác suất | `g12-probability-01` | Conditional Probability | PLANNED |
| 9 | Probability – Xác suất | `g12-probability-02` | Total Probability and Bayes' Formula | PLANNED |

**Tổng cộng: 71 bài** (đợt lớp 10 – 1: g10-sets-01 (chuyển sang v2), g10-sets-02, g10-algebra-01 đã BUILT; lớp 12 có 7 bài BUILT; lớp 11 có 11 bài BUILT: `g11-functions-01` (đã thay bài TEST cũ, ngoài bản đồ), `g11-trigf-01`, `g11-trigf-03`, `g11-trigf-02`, `g11-trige-01`, `g11-sequences-01`, `g11-limits-02`, `g11-derivatives-01`, `g11-exp-02`, `g11-space-02`, `g11-space-03`; các bài lớp 11 có đồ thị/hình tương tác (xem `docs/GRAPH.md`) và bài tập riêng cho từng mức).

> Bài TEST `g12-calculus-01` đã được xóa theo yêu cầu. Các bài TEST của AI số 1 (`g10-algebra-01`, `g11-functions-01`) đều đã được viết lại thành bài thật. Khi viết bài thật, giữ nguyên các `id` này nếu muốn tiếp tục dùng; hoặc thay bằng id mới của bản đồ trên và cập nhật `lessons.json`. Bản đồ này chưa xếp `g11-functions-01` vào chủ đề nào, vì chủ đề *Functions* lớp 11 được bao hàm trong *Trigonometric Functions*/*Exponential Functions*; cần AI số 1 hoặc giáo viên quyết định giữ hay xóa.

## Cấu trúc thư mục
```
mathbridge/
├─ css/lesson-kit.css      (MỚI – thành phần bài học, tiền tố mbl-)
├─ js/lesson-kit.js        (MỚI – tương tác: hiện/ẩn lời giải, chấm câu hỏi, điểm, tự chỉnh chiều cao iframe)
├─ lessons.json            (đã thêm g10-sets-01)
├─ data/vocab.json         (đã thêm 12 thuật ngữ Sets and Intervals)
└─ lessons/grade10/sets-and-intervals/sets-and-intervals.html   (BÀI MẪU HOÀN CHỈNH)
```
Đường dẫn đầy đủ dự kiến của các bài còn lại:
```
lessons/grade10/sets-and-intervals/sets-and-intervals.html
lessons/grade10/sets-and-intervals/counting-with-venn-diagrams.html
lessons/grade10/algebra/introduction-to-algebra.html
lessons/grade10/algebra/expanding-and-factoring.html
lessons/grade10/algebra/rational-expressions.html
lessons/grade10/equations/linear-equations.html
lessons/grade10/equations/systems-of-equations.html
lessons/grade10/equations/linear-inequalities.html
lessons/grade10/functions/function-notation-domain-and-range.html
lessons/grade10/functions/graphs-of-functions.html
lessons/grade10/functions/increasing-and-decreasing-functions.html
lessons/grade10/quadratic/parabolas-and-quadratic-functions.html
lessons/grade10/quadratic/quadratic-equations.html
lessons/grade10/quadratic/quadratic-inequalities.html
lessons/grade10/coordinate-geometry/coordinates-in-the-plane.html
lessons/grade10/coordinate-geometry/equations-of-lines.html
lessons/grade10/coordinate-geometry/circles.html
lessons/grade10/vectors/vectors-and-their-operations.html
lessons/grade10/vectors/the-dot-product.html
lessons/grade10/trigonometry/trigonometric-ratios-of-angles-from-0-to-180.html
lessons/grade10/trigonometry/law-of-sines-and-law-of-cosines.html
lessons/grade10/statistics/measures-of-central-tendency.html
lessons/grade10/statistics/measures-of-spread.html
lessons/grade10/probability/counting-rules.html
lessons/grade10/probability/permutations-and-combinations.html
lessons/grade10/probability/probability-of-events.html
lessons/grade11/trig-functions/radians-and-trigonometric-functions.html
lessons/grade11/trig-functions/graphs-and-properties.html
lessons/grade11/trig-equations/basic-trigonometric-equations.html
lessons/grade11/trig-equations/solving-trigonometric-equations.html
lessons/grade11/sequences/sequences-and-their-terms.html
lessons/grade11/sequences/monotonic-and-bounded-sequences.html
lessons/grade11/arithmetic-progressions/arithmetic-progressions.html
lessons/grade11/arithmetic-progressions/sum-of-an-arithmetic-progression.html
lessons/grade11/geometric-progressions/geometric-progressions.html
lessons/grade11/geometric-progressions/sum-of-a-geometric-progression.html
lessons/grade11/limits/limits-of-sequences.html
lessons/grade11/limits/limits-of-functions.html
lessons/grade11/limits/continuity.html
lessons/grade11/derivatives/the-derivative-definition.html
lessons/grade11/derivatives/rules-of-differentiation.html
lessons/grade11/derivatives/higher-order-derivatives.html
lessons/grade11/exponential-functions/powers-and-exponents.html
lessons/grade11/exponential-functions/exponential-functions-and-equations.html
lessons/grade11/logarithmic-functions/logarithms.html
lessons/grade11/logarithmic-functions/logarithmic-functions-and-equations.html
lessons/grade11/space-geometry/points-lines-and-planes-in-space.html
lessons/grade11/space-geometry/parallel-lines-and-planes.html
lessons/grade11/space-geometry/perpendicularity.html
lessons/grade11/statistics-probability/grouped-data-and-measures-of-spread.html
lessons/grade11/statistics-probability/probability-of-compound-events.html
lessons/grade12/derivative-applications/asymptotes-of-graphs.html
lessons/grade12/derivative-applications/sketching-graphs-of-functions.html
lessons/grade12/monotonicity-extrema/monotonicity-of-functions.html
lessons/grade12/monotonicity-extrema/local-extrema.html
lessons/grade12/monotonicity-extrema/maximum-and-minimum-values.html
lessons/grade12/antiderivatives/antiderivatives.html
lessons/grade12/antiderivatives/techniques-of-finding-antiderivatives.html
lessons/grade12/integrals/definite-integrals.html
lessons/grade12/integrals/properties-and-calculation-of-integrals.html
lessons/grade12/integral-applications/area-of-a-plane-region.html
lessons/grade12/integral-applications/volume-of-a-solid.html
lessons/grade12/vectors-in-space/vectors-in-space.html
lessons/grade12/vectors-in-space/coordinates-of-vectors.html
lessons/grade12/coordinates-in-space/equation-of-a-plane.html
lessons/grade12/coordinates-in-space/equation-of-a-line-in-space.html
lessons/grade12/coordinates-in-space/equation-of-a-sphere.html
lessons/grade12/statistics/range-and-interquartile-range.html
lessons/grade12/statistics/variance-and-standard-deviation.html
lessons/grade12/probability/conditional-probability.html
lessons/grade12/probability/total-probability-and-bayes-formula.html
```


## Đợt soạn lớp 10 và lớp 12 theo danh mục SGK Kết nối tri thức (đợt 4)

Căn cứ: `Toan_10_Ket_noi_tri_thuc.md`, `Toan_12_Ket_noi_tri_thuc.md`. Soạn trước 3 bài mỗi khối.

| Khối | Bài (SGK) | Mã bài | Ghi chú |
|---|---|---|---|
| 10 | Bài 1. Mệnh đề | `g10-logic-01` | Mới; nhóm D = 8 câu trắc nghiệm tự luyện |
| 10 | Bài 2. Tập hợp và các phép toán trên tập hợp | `g10-sets-01` | Gộp `g10-sets-02` (Venn); nhóm F = 8 câu tự luyện |
| 10 | Bài 3. Bất phương trình bậc nhất hai ẩn | `g10-ineq2-01` | Mới; 3 hình miền nghiệm (JSXGraph); nhóm D tự luyện |
| 12 | Bài 1. Tính đơn điệu và cực trị | `g12-mono-01` | Gộp mono-01 + mono-02; thêm 3 đồ thị tương tác; nhóm G tự luyện |
| 12 | Bài 2. GTLN – GTNN | `g12-mono-03` | Nhóm D tự luyện |
| 12 | Bài 3. Đường tiệm cận | `g12-deriv-app-01` | Thêm 2 đồ thị; tự luyện câu 11–18 |

**Cơ chế tạm khóa.** `config/model.json` có `lockedLessons` (mã bài → lý do) và `lessonOrder` (thứ tự theo SGK). Bài bị khóa vẫn còn trong thư mục, hiện thẻ mờ “Tạm khóa”, không mở được, không tính vào thống kê; bài khác coi tiên quyết bị khóa là đã thỏa. Danh sách khóa: `g10-algebra-01`, `g10-sets-02`, `g11-functions-01`, `g12-mono-02`. Bài nào dùng lại được thì gộp (như trên) thay vì xóa.

**Trắc nghiệm tự luyện.** `tools/mb_selfpractice.py` (hàm `SELF`) cùng `tools/sp_g10.py`, `tools/sp_g12.py` sinh 8 câu/mức/bài, số liệu theo hạt giống cố định, đáp án tính bằng máy (phân số chính xác hoặc duyệt số), không trùng đề với bài tập sẵn có và không trùng giữa các mức.

## Đợt 5 – 9 bài mới (lớp 10, 11, 12) và ẩn Tiểu học/THCS

Thứ tự và số bài theo `Toan_<lớp>_Ket_noi_tri_thuc.md` (`lessonOrder`, `lessonNo` trong `config/model.json`). Mỗi bài có 3 mức học, mỗi mức 15 câu (A trắc nghiệm, B đúng/sai, C trả lời ngắn, D tự luyện 8 câu trắc nghiệm).

| Lớp | Bài | Mã bài | Tên bài |
|---|---|---|---|
| 10 | 4 | `g10-ineq-sys-01` | Hệ bất phương trình bậc nhất hai ẩn |
| 10 | 5 | `g10-trig-01` | Giá trị lượng giác của một góc từ 0° đến 180° |
| 10 | 6 | `g10-trig-02` | Hệ thức lượng trong tam giác |
| 11 | 6 | `g11-sequences-02` | Cấp số cộng |
| 11 | 7 | `g11-sequences-03` | Cấp số nhân |
| 11 | 8 | `g11-stats-01` | Mẫu số liệu ghép nhóm |
| 12 | 4 | `g12-deriv-app-02` | Khảo sát và vẽ đồ thị hàm số (thêm 8 câu tự luyện) |
| 12 | 5 | `g12-optim-01` | Ứng dụng đạo hàm để giải quyết một số vấn đề thực tiễn |
| 12 | 6 | `g12-vec-01` | Vectơ và các phép toán trong không gian |

Lớp 11 Bài 1–5 đã được đánh số: `g11-trigf-01`=1, `g11-trigf-03` (công thức lượng giác)=2, `g11-trigf-02` (hàm số lượng giác)=3, `g11-trige-01`=4, `g11-sequences-01`=5. Các bài lớp 11 cũ chưa soạn lại (`limits-02`, `derivatives-01`, `exp-02`, `space-02`, `space-03`) giữ nguyên, chưa đánh số, xếp sau các bài đã đánh số.

**Ẩn cấp học.** Trong `config/model.json`, cấp `th` (Tiểu học) và `thcs` (THCS) có `"hidden": true`; `js/app.js` (`applyStages`) bỏ các cấp này nên không hiện ở trang chủ, bộ lọc, tìm kiếm và thống kê. Muốn mở lại: xóa `hidden` ở cả `config/model.json` và bản dự phòng `STAGES` trong `js/app.js`.

Mã nguồn bài tự luyện: `tools/sp_g10b.py`, `tools/sp_g11.py`, `tools/sp_g12.py`; công cụ chung `tools/mb_quick.py`, `tools/trigval.py`.

## Đợt 6 — 9 bài mới (3 bài mỗi khối, theo thứ tự SGK Kết nối tri thức)

| Lớp | Bài | Mã bài | Nội dung |
|---|---|---|---|
| 10 | 7 | g10-vec-01 | Các khái niệm mở đầu về vectơ |
| 10 | 8 | g10-vec-02 | Tổng và hiệu của hai vectơ |
| 10 | 9 | g10-vec-03 | Tích của một vectơ với một số |
| 11 | 9 | g11-stats-02 | Các số đặc trưng đo xu thế trung tâm (số liệu ghép nhóm) |
| 11 | 10 | g11-space-04 | Đường thẳng và mặt phẳng trong không gian |
| 11 | 11 | g11-space-05 | Hai đường thẳng song song |
| 12 | 7 | g12-coord-01 | Hệ trục tọa độ trong không gian |
| 12 | 8 | g12-coord-02 | Biểu thức tọa độ của các phép toán vectơ |
| 12 | 9 | g12-stats-01 | Khoảng biến thiên, khoảng tứ phân vị |

Mỗi bài có 15 câu/mức (7 câu bài + 8 câu tự luyện trắc nghiệm). Sinh câu tự luyện: `tools/sp_g10c.py`, `sp_g11b.py`, `sp_g11c.py`, `sp_g12b.py`; số liệu ghép nhóm: `tools/gdata.py`.

## Đợt 7 — 9 bài mới (3 bài mỗi khối, theo thứ tự SGK Kết nối tri thức)

| Lớp | Bài | Mã bài | Nội dung |
|---|---|---|---|
| 10 | 10 | g10-vec-04 | Vectơ trong mặt phẳng tọa độ |
| 10 | 11 | g10-vec-05 | Tích vô hướng của hai vectơ |
| 10 | 12 | g10-stats-01 | Số gần đúng và sai số |
| 11 | 12 | g11-space-06 | Đường thẳng và mặt phẳng song song |
| 11 | 13 | g11-space-07 | Hai mặt phẳng song song (gồm lăng trụ, hình hộp, chóp cụt) |
| 11 | 14 | g11-space-08 | Phép chiếu song song |
| 12 | 10 | g12-stats-02 | Phương sai và độ lệch chuẩn |
| 12 | 11 | g12-int-01 | Nguyên hàm |
| 12 | 12 | g12-int-02 | Tích phân |

Mỗi bài 15 câu/mức (3 trắc nghiệm + 2 đúng/sai + 2 trả lời ngắn + 8 trắc nghiệm tự luyện), 5 ví dụ có lời giải; mọi đáp số được kiểm bằng `assert` hoặc tính bằng máy (Fraction).
Sinh câu tự luyện: `tools/sp_g10d.py`, `tools/sp_g11d.py`, `tools/sp_g12c.py`.

**Tạm khóa thêm:** `g11-space-02` (đã soạn lại thành Bài 12, 13), `g12-antider-01` (đã soạn lại thành Bài 11), `g12-antider-02` (đổi biến, từng phần – ngoài danh mục KNTT). Nội dung cũ vẫn giữ trong `content/`.

**Thuật ngữ mới tự gắn vào bài cũ:** từ vựng mới (tung độ, hoành độ, cạnh bên, hình hộp, tích vô hướng, đường thẳng song song với mặt phẳng) được hệ thống tự bọc trong câu hỏi của một số bài cũ (chỉ thêm chú thích khi bấm, nội dung không đổi). Hai thuật ngữ dễ nhầm nghĩa được đặt khóa riêng: "số đúng (giá trị thật)", "góc nhọn (nhỏ hơn 90°)".

## Đợt 8 — 6 bài mới (2 bài mỗi khối) và sửa ký hiệu dấu phẩy trên

| Lớp | Bài | Mã bài | Nội dung |
|---|---|---|---|
| 10 | 13 | g10-stats-02 | Các số đặc trưng đo xu thế trung tâm |
| 10 | 14 | g10-stats-03 | Các số đặc trưng đo độ phân tán |
| 11 | 15 | g11-limits-03 | Giới hạn của dãy số |
| 11 | 16 | g11-limits-04 | Giới hạn của hàm số |
| 12 | 13 | g12-int-03 | Ứng dụng hình học của tích phân |
| 12 | 14 | g12-coord-03 | Phương trình mặt phẳng |

Sinh câu tự luyện: `tools/sp_g10e.py`, `tools/sp_g11e.py`, `tools/sp_g12d.py`. Tạm khóa thêm `g11-limits-02` (đã soạn lại thành Bài 16).

**Ký hiệu dấu phẩy trên (A', B', f'(x)):** ký tự `′` (U+2032) trong công thức bị MathJax vẽ ở chân chữ ("Aı"). `tools/mb_model.py` (`fix_math_prime`) tự đổi `′` thành `'` bên trong `\( … \)` và `\[ … \]` khi dựng trang, nên người soạn vẫn có thể gõ `A′` trong nội dung; nhãn trên hình vẽ và chữ thường giữ nguyên `′`.

## Đợt 9 — 6 bài mới (2 bài mỗi khối)

| Lớp | Bài | Mã bài | Nội dung |
|---|---|---|---|
| 10 | 15 | g10-func-01 | Hàm số (tập xác định, tập giá trị, đồ thị, đồng biến/nghịch biến, hàm cho bởi nhiều công thức) |
| 10 | 16 | g10-func-02 | Hàm số bậc hai (đỉnh, trục đối xứng, bảng biến thiên, GTLN/GTNN, bài toán thực tế) |
| 11 | 17 | g11-limits-05 | Hàm số liên tục (liên tục tại một điểm, trên một khoảng, tìm tham số, định lí giá trị trung gian) |
| 11 | 18 | g11-exp-03 | Lũy thừa với số mũ thực (căn bậc n, số mũ hữu tỉ và thực, so sánh, lãi kép, chu kì bán rã) |
| 12 | 15 | g12-coord-04 | Phương trình đường thẳng trong không gian (tham số, chính tắc, vị trí tương đối) |
| 12 | 16 | g12-coord-05 | Công thức tính góc trong không gian (đường–đường, đường–mặt, mặt–mặt, góc trong hình lập phương) |

Sinh câu tự luyện: `tools/sp_g10f.py`, `tools/sp_g11f.py`, `tools/sp_g12e.py`. Bài cũ `g11-exp-02` (Hàm số mũ và phương trình mũ) vẫn mở, xếp sau Bài 18 (`lessonOrder` = 200, chưa đánh số).

## Hình không gian tĩnh (TikZ → SVG)

Hình không gian không còn dùng JSXGraph 3D (xoay được nhưng hay lỗi khi tải). `GEO3D(cfg, …)` nay vẽ **hình tĩnh** bằng TikZ:

- `tools/mb_tikz3d.py` dựng mã TikZ từ cấu hình cũ (`points`, `solid`, `segments`, `polygons`), biên dịch bằng `pdflatex`, chuyển sang SVG bằng `pdftocairo -svg`, lưu ở `img/fig3d/<mã băm>.svg` (kèm tệp `.tex`; mã TikZ không đổi thì không biên dịch lại).
- Phép chiếu song song kiểu SGK: hộp/lập phương trục sâu 30°, hệ số 1/2; chóp, tứ diện 42°, hệ số 0,6; `'proj': 'oxyz'` cho hình trong hệ tọa độ (Ox hướng xuống trái, có thể thêm `'axes': True`).
- **Nét khuất tự tính**: một điểm bị che nếu tia từ điểm đó về phía người nhìn đi qua khối; đoạn thẳng tự tách thành phần nét liền / nét đứt.
- Tùy chọn thêm: `'right': [['S','A','B']]` (kí hiệu góc vuông tại A), `'angles': [['S','C','A']]` (cung góc tại C), `'nolabel'`, `'labelpos'`, `'arrow': True` cho đoạn thẳng.
- `tools/mb_solids.py`: thư viện khối dựng sẵn (`fig('pyr' | 'pyrsq' | 'tet' | 'cube' | 'box', pts={'M': 'mid:S,C', 'G': 'cen:A,B,C', 'P': 'on:A,B,1/3'}, …)`).
- `EXFIG(examples, n, GEO3D(...))` chèn hình vào đề của Ví dụ n. Đã thêm hình cho các ví dụ hình không gian lớp 11 (Bài 10–13, quan hệ vuông góc) và lớp 12 (hệ tọa độ, vectơ trong không gian, công thức tính góc).
- Cần TeX Live có `pgf/tikz` và `poppler-utils` (`pdftocairo`) trên máy dựng bài; người học chỉ tải SVG.

Sửa lỗi "Phân tích: d": khi phần phân tích của ví dụ được truyền dưới dạng khối `T(...)`, `EXAMPLE` trước đây chỉ lấy kí tự thứ hai ("d"). Nay chèn đúng nhãn "Phân tích:" vào khối đó; ví dụ không có phân tích thì không hiện dòng này.
