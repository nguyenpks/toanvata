# 08 – KẾ HOẠCH KHẮC PHỤC

Nguyên tắc: **chưa sửa bất kỳ nội dung gốc nào**. Mọi thay đổi chỉ tiến hành khi chủ website đồng ý. Sửa ở tệp nguồn (`content/*.py`, `tools/sp_*.py`), sau đó dựng lại bằng `python tools/build_all.py`, không sửa tay tệp HTML. Giữ nguyên cấu trúc dữ liệu và giao diện.

## Ưu tiên 1 – Chặn đạt chuẩn (làm trước khi cho học sinh dùng)

> **08/11/2026:** mục 1–6 **Đã sửa · Đã kiểm tra lại** (chi tiết và số liệu trước/sau trong `10_BAO_CAO_SUA_UU_TIEN_1.md`). Mục 7 **đã thực hiện** (`11_KIEM_DINH_MUC_2_3.md`) và phát sinh các việc Ưu tiên 1 bổ sung (mục 8–10 bên dưới), **đã sửa và kiểm tra lại cùng ngày** (`11_KIEM_DINH_MUC_2_3.md` mục 5). M-102 (trong mục 9) chưa sửa. T-001 được sửa chung tại `tools/mb_lib.py` (`MCQ._o`) thay vì sửa từng tệp; M-003 sửa tại `tools/sp_g10f.py` (`q_mono`).

| # | Mã | Việc | Tệp | Cách kiểm tra lại |
|---|---|---|---|---|
| 1 | M-001 | Sửa phương án đúng của `s_comp` thành `cp(*true)` | `tools/sp_g10.py` 154–161 | Câu 18 Bài 2 lớp 10, cả 3 mức: khóa trỏ tới tập đảo đóng/mở |
| 2 | M-007 | Sửa thứ tự giải nén `(A,B,ae,be,av,bv)` | `content/grade11/union-intersection-independence.py` 83 | Câu 1 Bài 28, 3 mức: \(A\) là "số chấm chẵn"/"lẻ"…; có phương án đúng |
| 3 | M-008 | Giữ dấu ′ trong `sums`/`nm` | `content/grade12/vectors-in-space.py` 65–66 | Câu 1 Bài 6 lớp 12 hiện \(\overrightarrow{AA'}\), đáp án \(\overrightarrow{AC'}\) |
| 4 | M-003 | Thay phương án c; thêm ràng buộc sinh câu | bộ sinh câu Bài 16 lớp 10 | Câu 9 chỉ còn một phương án đúng |
| 5 | T-001 | Bỏ delimiter toán quanh phương án văn bản | `content/grade10/lines-angle-distance.py`, `circle-equations.py`, `content/grade12/sphere-equations.py` | Không còn chuỗi `\lt span` trong HTML |
| 6 | T-002 | Sửa 7 chỗ lồng delimiter/lệnh dính chữ (danh sách trong 07) | các tệp nội dung tương ứng | Dựng MathJax: 0 lỗi lệnh không xác định |
| 7 | — | **Kiểm định thủ công Mức 2 và Mức 3** (2.398 câu) theo cùng quy trình | — | Cập nhật 02–04 · **Đã làm 08/11** |
| 8 | M-108 | Sửa `m1_sign`: không lấy phương án hợp hai khoảng làm khóa; loại nhiễu là khoảng con của khoảng đồng biến | `tools/sp_g12.py` 55–63 | 12 · B1 Mức 3 tự luyện câu 25 có đúng một phương án đúng; thêm `assert` |
| 9 | M-101 (+ M-102) | Sửa `e_sqrt` (và `e_round_err`, câu sai số tương đối): không dùng nhiễu là cận trên đúng | `tools/sp_g10d.py` 190–200 | 10 · B12, cả 3 mức: chỉ một phương án đúng |
| 10 | M-107 | Thay phương án b \((-\infty;-4)\) | `content/grade12/monotonicity-extrema.py` 156 | 12 · B1 Mức 3 câu 1 có đúng một phương án đúng |

## Ưu tiên 2 – Sai sót toán học và thiếu nội dung

| # | Mã | Việc |
|---|---|---|
| 8 | M-002 | Thêm điều kiện "miền đa giác" ở Bài 3 lớp 10 |
| 9 | M-004 | Viết lại Ví dụ 4 Bài 3 lớp 11 (bỏ lập luận "bội chung") |
| 10 | C-01 | Bổ sung tứ phân vị ghép nhóm vào Bài 9 lớp 11 |
| 11 | C-02 | Bổ sung "tốc độ thay đổi" vào Bài 5 lớp 12 (sau khi đối chiếu bản in) |
| 12 | M-006, M-009, M-010, M-011, M-012 | Sửa theo nội dung đề xuất trong 05 |
| 13 | C-03, C-04 | Bổ sung mục thiếu (đối chiếu bản in trước) |
| 14 | T-003 | Bộ sinh câu: số thập phân trong văn bản thường viết "0,9"; thay `\lt b\gt` bằng thẻ `<b>` thật |

## Ưu tiên 3 – Sư phạm và trải nghiệm

| # | Mã | Việc |
|---|---|---|
| 15 | P-01, P-02 | Viết lại lời giải câu Đúng/Sai và câu tự luyện: mỗi lời giải có phép tính hoặc phản ví dụ cụ thể |
| 16 | P-03 | Việt hóa toàn bộ chuỗi tiếng Anh ở Mức 1 |
| 17 | P-04, P-05, P-06, P-07, P-08 | Sửa trình tự, bổ sung mục rỗng, bỏ câu trùng, gắn nhãn "Mở rộng", cân đối số câu |
| 18 | P-09 | Thêm trang ôn tập chương |
| 19 | T-004 | Lưu bài làm và điểm vào LocalStorage, hiển thị ở trang Tiến độ |
| 20 | T-006 | Tìm kiếm không phân biệt dấu |
| 21 | T-007 | Đóng gói MathJax cục bộ hoặc thêm SRI |

## Ưu tiên 4 – Lỗi nhẹ
Các mục Low trong 05, 06, 07 (định dạng, chú thích hình, mã chết, bài khóa truy cập trực tiếp…).

## Kiểm thử bổ sung đề xuất (chống tái phát)
1. **Kiểm thử ngữ nghĩa cho bộ sinh câu:** với mỗi họ câu, viết hàm kiểm tra độc lập (ví dụ: phần bù – kiểm tra phương án đúng không chứa điểm thuộc khoảng gốc; câu khoảng đơn điệu – không phương án nhiễu nào là tập con của khoảng đúng); chạy cho mọi hạt giống.
2. **Kiểm thử dựng thật:** mở từng trang bằng trình duyệt không giao diện, bung mọi lời giải, đếm phần tử MathJax báo lỗi và chuỗi `\(`, `\lt`, `{,}` còn hiển thị → phải bằng 0.
3. **Kiểm thử không có phương án đúng / nhiều phương án đúng** cho các câu tập hợp, khoảng, biến cố.
4. Cập nhật `tests/baseline/html-hashes.json` sau mỗi đợt sửa đã duyệt (hiện `check_html_snapshot.py` đang lỗi).

## Bước 7 – Kiểm định sau sửa
Sau khi sửa: dựng lại toàn bộ; chạy lại `scan` tĩnh và kiểm thử dựng thật; kiểm tra lại từng mã lỗi ở trên (đổi trạng thái thành "Đã sửa" → "Đã kiểm tra lại"); xác nhận không mất nội dung (số câu/mức mỗi bài không đổi), liên kết và chấm điểm vẫn hoạt động.

## Dự kiến điểm sau khi hoàn thành Ưu tiên 1–2
≈ 85–88/100 (Khá), với điều kiện kiểm định Mức 2–3 không phát hiện thêm lỗi hệ thống.
