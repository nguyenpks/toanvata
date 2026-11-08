# 10 – BÁO CÁO SỬA ƯU TIÊN 1 VÀ KIỂM TRA LẠI (BƯỚC 7)

Ngày sửa: 08/11/2026 · Căn cứ: chủ website đồng ý "Sửa Ưu tiên 1" (mục Ưu tiên 1 trong `08_KE_HOACH_KHAC_PHUC.md`).
Nguyên tắc đã giữ: chỉ sửa tệp nguồn (`content/*.py`, `tools/*.py`), dựng lại bằng `python tools/build_all.py`, không sửa tay HTML, không đổi cấu trúc dữ liệu/giao diện, không đổi hạt giống (seed) sinh câu, không đụng mã TikZ của hình vẽ.

## 1. Các thay đổi

| Mã | Tệp nguồn | Thay đổi | Trạng thái |
|---|---|---|---|
| M-001 | `tools/sp_g10.py` (`s_comp`) | Phương án đúng = `cp(*true)` (phần bù thật: đảo đóng/mở ở mỗi đầu mút). Thêm `assert` kiểm tra trên lưới số: phương án đúng trùng phần bù, 3 nhiễu đều sai. Thêm lời giải chỉ rõ quy tắc đầu mút. | **Đã sửa · Đã kiểm tra lại** |
| M-007 | `content/grade11/union-intersection-independence.py` dòng 83 | Giải nén đúng thứ tự `(A, B, ae, be, av, bv)` | **Đã sửa · Đã kiểm tra lại** |
| M-008 | `content/grade12/vectors-in-space.py` dòng 65 | `nm` tách tên điểm bằng `[A-Z]'?` nên giữ dấu phẩy trên (AA′, AC′…) | **Đã sửa · Đã kiểm tra lại** |
| M-003 | `tools/sp_g10f.py` (`q_mono`) | Hai phương án nhiễu "đồng biến trên \((m;+\infty)\)" / "nghịch biến trên \((-\infty;n)\)" được chọn sao cho **không** là khoảng con của khoảng đơn điệu thật (có `assert`) | **Đã sửa · Đã kiểm tra lại** |
| T-001 | `tools/mb_lib.py` (`MCQ._o`) | Không bọc `\( … \)` quanh phương án đã là HTML (`TI`/`TT`) hoặc đã chứa `\(`. Phương án là công thức thuần vẫn bọc như cũ. Một chỗ sửa chung thay cho sửa từng tệp `lines-angle-distance.py`, `circle-equations.py`, `sphere-equations.py`. | **Đã sửa · Đã kiểm tra lại** |
| T-002 | `tools/mb_lib.py` (như trên); `content/grade10/linear-inequalities-two-variables.py`; `content/grade11/exp-log-equations.py`; `tools/sp_g11j.py` | Lồng delimiter (B3 lớp 10, B17/B31/B33 lớp 11, B21 lớp 10, B17 lớp 12) hết nhờ sửa chung ở `MCQ._o`. Phương án "đường nét đứt/liền" B3 lớp 10 chuyển sang song ngữ `TI(...)` (trước đây chỉ có tiếng Anh, cả ở Mức 1). Thêm dấu cách: `\Rightarrow x`, `A_1\cap A_2`, `A_1\cup A_2\cup A_3`. | **Đã sửa · Đã kiểm tra lại** |
| (mục 7) | — | Kiểm định thủ công Mức 2 và Mức 3 (2.398 câu) | **Đã thực hiện 08/11** – xem `11_KIEM_DINH_MUC_2_3.md` (phát hiện M-108 Critical, M-101 và M-107 High – **đã sửa, kiểm tra lại 08/11**, xem `11` mục 5) |

## 2. Kết quả kiểm tra lại

| Kiểm tra | Trước sửa | Sau sửa |
|---|---|---|
| Quét tĩnh HTML: lồng delimiter `\(…\(` | 66 (6 bài) | **0** |
| Quét tĩnh: lệnh TeX dính chữ (`\Rightarrowx`, `\capA`…) | 10 (2 bài) | **0** |
| Quét tĩnh: `\lt span/b` | 275 (11 bài) | 95 (8 bài). Trong đó: (i) phần còn lại là `\lt b` = "nhỏ hơn \(b\)" trong công thức hoặc nằm trong thuộc tính `data-say` (không hiển thị); (ii) **56 chỗ ở 4 bài vẫn hiển thị thô** `\lt b\gt…\lt /b\gt` (`counting-rules` 24, `binomial-theorem` 12, `permutations-combinations` 12, `parallel-projection` 8) – thuộc **T-003** (Ưu tiên 2), chưa sửa. *(Đính chính 08/11: bản trước của dòng này ghi nhầm "đều không phải lỗi hiển thị".)* |
| Dựng MathJax trên trình duyệt, 90 trang, bung mọi lời giải và mọi mức: lỗi lệnh (đỏ) | 76 | **0** |
| Như trên: mảnh TeX/HTML thô hiển thị | 396 (21 bài) | 157 (14 bài) – thuộc T-003 (`{,}`/`\dfrac` ngoài công thức, Ưu tiên 2) và `\lt b\gt` hiện thô trong đề bài Phép chiếu song song lớp 11 (`g11-space-08`) – chưa thuộc phạm vi Ưu tiên 1 |
| Số câu trắc nghiệm / đúng-sai trong HTML | 2.595 / 486 | 2.595 / 486 (không đổi) |
| Khóa đáp án không có trong phương án; phương án trùng | 0 / 0 | 0 / 0 |

**Kiểm tra tay sau sửa (cả 3 mức):**
- M-001: \([0,2]\to(-\infty,0)\cup(2,+\infty)\); \((-3,0]\to(-\infty,-3]\cup(0,+\infty)\); \((-3,1]\to(-\infty,-3]\cup(1,+\infty)\) – khóa đúng ở cả 3 mức.
- M-007: "chẵn" ∩ "≥ 3" = {4; 6}; "lẻ" ∩ "≤ 3" = {1; 3}; "nguyên tố" ∩ "khác 1 và 3" = {2; 5} – nhãn khớp dữ liệu, có đúng một phương án đúng.
- M-008: \(\overrightarrow{AB}+\overrightarrow{AD}+\overrightarrow{AA'}=\overrightarrow{AC'}\), tương tự với đỉnh C, D (Mức 1–3) và đỉnh B, D, C (tự luyện); không còn vectơ \(\overrightarrow{AA}\)… trong trang.
- M-003: \(y=3x^2+12x+12\) (đỉnh \(x=-2\)): nhiễu mới "đồng biến trên \((-3;+\infty)\)", "nghịch biến trên \((-\infty;-1)\)" – đều sai; chỉ còn phương án b đúng. Các câu cùng họ còn lại cũng chỉ có một phương án đúng.

**Bộ kiểm thử của dự án** (`python tests/run_all.py`): 12/13 bước đạt (đồ thị, hình TikZ, mô hình bài học, giao diện giả lập, các bài lớp 10/11/12, ký hiệu hình học, MathJax, hàng đợi dựng công thức). Bước "So sánh HTML với baseline" **không đạt – như trước khi sửa**: baseline đã cũ, liệt kê cả những trang không hề thay đổi (vd `local-extrema.html`). `python tools/build_all.py --check`: "Mô hình hợp lệ". Lưu ý: các bộ kiểm thử này chỉ kiểm tra tính nhất quán nội bộ, không kiểm tra đáp án toán học.

## 3. Thay đổi phụ (không phải do sửa nội dung)

- Dựng lại trên Windows ghi CRLF; đã chuyển lại LF cho mọi tệp sinh ra. Sau chuẩn hóa, **19 trang** khác bản trước: 11 trang do các sửa ở trên + 8 trang chỉ khác ở việc tự động gắn chú giải thuật ngữ (glossary), xảy ra cả khi dựng lại mà không sửa gì: `permutations-combinations`, `linear-inequality-systems`, `counting-with-venn-diagrams`, `sets-and-intervals`, `antiderivatives` (12), `conditional-probability`, `total-probability-bayes`, `angle-formulas`.
- `tests/run_all.py` chạy `tools/make_graph_demo.py` và ghi lại `demo/graph-demo.html`; nội dung trùng khít bản trong git, đã khôi phục LF.

## 4. Phát hiện mới trong lúc kiểm tra lại

**T-016 (Medium) · Dấu `<` trần trong công thức làm mất chữ** – `lessons/grade12/monotonicity-extrema/local-extrema.html` (`g12-mono-02`), lý thuyết "cực đại/cực tiểu": `\(f(x)<f(x_0)\)` viết `<` trực tiếp trong HTML nên trình duyệt hiểu `<f(x_0)…` là thẻ, công thức hiển thị cụt ("sao cho \(f(x)" …). Có từ trước, không do lần sửa này. Đề xuất: dùng `\lt` như các bài khác. Chưa sửa (ngoài phạm vi Ưu tiên 1).

## 5. Ảnh hưởng tới kết luận

Hai lỗi Critical (M-001, M-007) và các lỗi High M-003, M-008, T-001, T-002 đã được xử lý. Website **vẫn chưa được xếp "đạt chuẩn"**, vì: (1) kiểm định Mức 2–3 (xem `11`) còn các lỗi Medium/Low chưa sửa (ba lỗi chặn M-108, M-101, M-107 đã sửa); (2) còn M-002 (High) và các lỗi Ưu tiên 2; (3) còn thiếu nội dung bắt buộc C-01…C-04 (xem 09).
