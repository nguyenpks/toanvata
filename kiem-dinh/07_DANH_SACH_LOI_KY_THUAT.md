# 07 – DANH SÁCH LỖI KỸ THUẬT

> **Cập nhật 08/11/2026:** M-001, M-003, M-007, M-008, T-001, T-002 đã chuyển sang **Đã sửa · Đã kiểm tra lại** – xem `10_BAO_CAO_SUA_UU_TIEN_1.md`. Kiểm định thủ công Mức 2–3 (08/11) và các lỗi mới phát hiện (M-101…M-108, P-101…P-109): xem ``11_KIEM_DINH_MUC_2_3.md``. Nội dung bên dưới giữ nguyên như lúc kiểm định (07/11/2026).

Môi trường kiểm thử: Windows 10, Python 3.15, Node 26; máy chủ tĩnh `python -m http.server` (127.0.0.1); trình duyệt Chromium tích hợp trong ứng dụng Claude; MathJax 3.2.2 từ CDN; mô phỏng điện thoại 375×812.
Tổng: **2 High · 6 Medium · 7 Low**.

## 1. Kết quả chạy thử chức năng

| Chức năng | Kết quả |
|---|---|
| Trang chủ, menu, danh mục lớp 10 (27 thẻ bài) | Đạt |
| Breadcrumb, Bài trước / Bài tiếp theo | Đạt |
| Tìm kiếm "tích phân" → Bài 11, 12, 13 lớp 12 | Đạt |
| Tìm kiếm từ khóa lạ → thông báo không tìm thấy | Đạt |
| Tìm kiếm không dấu "tich phan" → 0 kết quả | **Không đạt** (T-006) |
| Mở id sai `#/lesson/abc`, mở bài khóa qua giao diện | Báo "Không tìm thấy" – Đạt |
| Chèn `<img onerror>` vào tham số tìm kiếm | Không thực thi (đã thoát HTML) – Đạt |
| Chấm câu trả lời ngắn: "3,0" với đáp án 3; "280 m" với đáp án 280 | Đạt |
| Chấm trắc nghiệm, cập nhật điểm | Đạt |
| Tải lại trang bài học | **Mất toàn bộ bài làm và điểm** (T-004) |
| "Đánh dấu đã hoàn thành" → Tiến độ cập nhật | Đạt |
| Điện thoại 375 px: trang không cuộn ngang; bảng rộng có thanh cuộn riêng | Đạt |
| Dựng MathJax 79 trang (bung mọi lời giải, mọi mức) | **76 lỗi lệnh TeX** + **396 mảnh TeX/HTML thô hiển thị** ở 21 bài (T-002, T-003) |
| Bộ kiểm thử dự án | 12/13 đạt; `check_html_snapshot.py` **không đạt** (5 tệp lớp 12 khác bản gốc) (T-005) |

## 2. Danh sách lỗi

### HIGH

**T-001 · Phương án trắc nghiệm hiển thị mã HTML thô**
| Trường | Nội dung |
|---|---|
| Vị trí | Lớp 10 · Bài 20 (`lines-angle-distance.html`) câu 1; Bài 21 (`circles.html`) câu 1, 2; Lớp 12 · Bài 17 (`sphere-equations.html`) câu 3 – cả 3 mức |
| Hiện tại | `\(\lt span class="txi">\lt span class="en">parallel\lt /span>\lt span class="vi">song song\lt /span>\lt /span>\)` |
| Vấn đề | Trên trang, phương án hiện thành "< spanclass = ″txi″ >< spanclass = ″en″ > parallel </span >…", tràn ngang khung (đã chụp màn hình). Học sinh không đọc được câu hỏi, trong đó có phương án đúng. |
| Căn cứ | Phương án dạng văn bản song ngữ bị bọc trong `\( … \)` và thoát `<` thành `\lt` khi dựng |
| Đề xuất | Không bọc phương án văn bản trong delimiter toán; dùng `TI(en, vi)` như các câu khác; thêm kiểm thử từ khóa `\lt span` |
| Nội dung sửa | Bài 20 câu 1: (a) vuông góc (b) song song (c) trùng nhau (d) cắt nhau nhưng không vuông góc |

**T-002 · Lỗi dựng công thức MathJax (76 lỗi)**
| Bài | Số lỗi | Nguyên nhân |
|---|---:|---|
| 10 · B3 câu 2, 7 (mọi mức) | 12 | Lồng delimiter: `\(a dashed line \(x-y=3\)\)` |
| 10 · B21 câu 1–2 | 24 | Lồng delimiter (kết hợp T-001) |
| 11 · B17 câu 3 | 3 | `\(\((-\infty;1)\), \((1;4)\)…\)` – lỗi đúng ở phương án ĐÚNG |
| 11 · B21 câu 1 (lời giải) | 2 | Lệnh dính chữ `\Rightarrowx` |
| 11 · B28 câu 14 | 8 | `A_1\capA_2`, `\cupA_2` |
| 11 · B31 câu 3; 11 · B33 câu 3 | 24 | `\(\(10\) m/s\)` |
| 12 · B17 câu 3 | 3 | Lồng delimiter |
Mức độ **High** vì làm hỏng phương án/đề. Đề xuất: sửa nguồn; thêm kiểm thử dựng thật bằng MathJax (không chỉ kiểm tra ngoặc) – kịch bản đo đã dùng có thể đưa vào `tests/`.

### MEDIUM

| Mã | Vấn đề | Vị trí / số liệu | Đề xuất |
|---|---|---|---|
| T-003 | Mã TeX/HTML lọt ra ngoài công thức, hiển thị nguyên văn: `0{,}9` (dấu phẩy thập phân), `\lt b\gt…\lt /b\gt` (chữ đậm), `\dfrac{384}{11}`, `\dfrac{1}{2}`, `3;\ 4;\ 4`, `numerator \lt denominator` | 396 lần ở 15 bài: 11·B30 (108), 10·B23 (48), 11·B9 (32), 10·B24, B25 (24 mỗi bài), 11·B8 (22), 11·B14 (16), 12·B19 (15), 11·B28, B29 (12), 10·B27 (6), 10·B4, 12·B9 (4), 12·B3 (3) | Bộ sinh câu dùng `dstr()` cho văn bản thường phải trả "0,9" không có `{,}`; dùng thẻ `<b>` thật thay cho `\lt b\gt` |
| T-004 | Không lưu bài làm, điểm, số câu đúng; tải lại trang là mất. Lịch sử học chỉ ghi "đã mở"/"hoàn thành" | `js/lesson-kit-v2.js`, `js/progress.js` | Lưu trạng thái câu theo `lessonId`/mức vào LocalStorage; hiển thị điểm cao nhất trong Tiến độ |
| T-005 | Bộ kiểm thử báo "0 lỗi" công thức (`test-mathjax.py`: 59.507 công thức) dù dựng thật có 76 lỗi; không kiểm tra tính đúng của khóa đáp án; `check_html_snapshot.py` lỗi do bản gốc cũ (`range-interquartile-range`, `variance-standard-deviation`, `coordinate-system-oxyz`, `vector-coordinates`, `vectors-in-space`) | `tests/` | Thêm kiểm thử dựng MathJax thật, kiểm thử "đáp án đúng thỏa đề" cho từng họ câu sinh máy; cập nhật baseline sau khi duyệt |
| T-006 | Tìm kiếm phân biệt dấu ("tich phan" không ra kết quả), chỉ tìm tiêu đề/mô tả/thẻ, không tìm nội dung | `js/app.js` hàm `courses()` | Chuẩn hóa NFD bỏ dấu khi so khớp; bổ sung chỉ mục từ khóa |
| T-007 | Phụ thuộc MathJax từ CDN; mất mạng là mọi công thức hiện dạng `\(…\)`; thẻ `<script>` không có SRI | `config/model.json` → `page.mathjax` | Đóng gói MathJax cục bộ hoặc thêm thuộc tính `integrity`; thông báo khi tải thất bại |
| T-013 | Hình minh họa không khớp dữ kiện ví dụ | 11·B29 Ví dụ 3 (50 hộ: 30/18/10) dùng lại hình Venn của lớp 40 HS (18/15/7/14) | Vẽ hình riêng hoặc bỏ hình |

### LOW

| Mã | Vấn đề | Vị trí |
|---|---|---|
| T-008 | 11 bài tạm khóa vẫn tải được trực tiếp (HTTP 200), ví dụ `lessons/grade12/antiderivatives/antiderivatives.html` | thư mục `lessons/` |
| T-009 | Đáp án nằm sẵn trong DOM (`data-answer`) – học sinh xem mã nguồn là thấy | mọi bài; chấp nhận được với web tự học, cần ghi nhận nếu dùng để kiểm tra |
| T-010 | Mã chết trong `lessonView` (nhánh `if (l.locked)` thứ hai không bao giờ chạy); `P.recordView` vẫn ghi lượt xem cho id bài khóa | `js/app.js` dòng 143–144, 214 |
| T-011 | Kí tự `‴` (U+2034) trong công thức: hiển thị được nhưng không phải cú pháp TeX chuẩn (`f'''`) | 11·B33 (13 chỗ) |
| T-012 | Nhập "324.632" (dấu chấm phân nghìn kiểu Việt) bị hiểu là 324,632; khoảng có số thập phân dấu phẩy "[1,5;3]" bị tách sai | `parseNumber`, `parseInterval` trong `js/lesson-kit-v2.js` |
| T-014 | Chú thích hình còn chữ "Đồ thị tương tác" dù hình đã chuyển sang ảnh tĩnh; hai hình trùng nội dung | 12·B3 |
| T-015 | Hồ sơ `docs/CURRICULUM.md` trỏ tới các tệp `Toan_1x_Ket_noi_tri_thuc.md` không có trong dự án, không truy được nguồn đối chiếu SGK | `docs/` |

## 3. Bảo mật và dữ liệu
- Không có máy chủ, không thu thập dữ liệu cá nhân; tiến độ lưu LocalStorage – phù hợp.
- Mọi chuỗi từ URL được thoát HTML trước khi chèn (`esc`), đã thử chèn mã – không thực thi.
- `postMessage` từ bài học kiểm tra `origin`, đúng iframe và đúng `lessonId` – tốt.
- Không phát hiện lỗi bảo mật nghiêm trọng.
