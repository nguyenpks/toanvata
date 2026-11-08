# 12 – SỬA TRÌNH BÀY THEO GÓP Ý CỦA CHỦ WEBSITE (08/11/2026)

Góp ý: (1) dấu chia hết / chia không hết chưa đúng; (2) câu có nhiều ý a) b) c) hay (1) (2) (3) nên xuống dòng; (3) phân số nên dùng `\dfrac`; (4) đáp án/liệt kê nên nằm dưới câu hỏi, không viết ngang hàng; (5) một bài có quá nhiều câu về cùng một nội dung (vd Bài 6 lớp 12: quá nhiều câu về hình lập phương).

## 1. Đã sửa

| # | Việc | Cách làm | Phạm vi |
|---|---|---|---|
| 1 | Kí hiệu chia hết | Viết theo SGK Việt Nam: \(n\,\vdots\,6\) ("\(n\) chia hết cho 6"), \(3\,\not\vdots\,6\); bỏ cách viết \(6\mid n\). Câu đọc tiếng Anh: "is divisible by". | `content/grade10/propositions.py`, `tools/sp_g10.py` (câu kéo theo), `tools/mb_lib.py` (đọc). Kí hiệu \(\{x\mid\ldots\}\) của tập hợp và \(P(A\mid B)\) giữ nguyên. |
| 2 | Các ý xuống dòng | Bước hậu xử lý chung `fix_layout` (`tools/mb_model.py`): trong một đoạn, các ý a) b) c)…, (a) (b)… hoặc (1) (2)… (ngoài công thức, đúng thứ tự, đứng sau dấu ":", ";", ".", "?") được tách thành từng dòng. Câu "từ (1) và (2) suy ra…", "nên (a) đúng" không bị tách. Câu "Trong bốn phát biểu sau…" (lớp 10 Bài 1) nay đưa số thứ tự ra ngoài công thức. | Toàn bộ trang (mọi bài, cả 3 mức, ví dụ, lời giải). |
| 3 | Phân số `\dfrac` | Cũng trong `fix_layout`: `\frac` → `\dfrac` và phân số số học `a/b` → `\dfrac{a}{b}` ở dòng chính. **Giữ nguyên** trong số mũ/chỉ số/cận (\(2^{t/20}\), \(16^{-\frac34}\), \(\big|_0^{\pi/2}\)), vì `\dfrac` ở đó làm chữ to bất thường. Phân số có chữ được sửa ở nguồn: \(\left(\dfrac{c}{a};0\right)\), \(\dfrac{2\pi}{\frac{\pi}{6}}\), \(M_e=u_m+\dfrac{\frac n2-C}{n_m}h\), \(Q_j\), \(\dfrac{P(A\cap B)}{P(B)}\), \(\dfrac{a}{\frac{a\sqrt2}{2}}\)… | Toàn bộ trang; nguồn: 8 tệp. |
| 4 | Liệt kê dưới câu hỏi | `fix_layout`: câu hỏi kết thúc bằng "?" mà có danh sách công thức theo sau thì danh sách xuống dòng (vd "Cặp nào là nghiệm của \(3x-2y\le5\)?" rồi xuống dòng \((1;1)\), \((3;1)\), \((0;-3)\)). Phương án trắc nghiệm vốn đã xếp dọc. | Toàn bộ trang. |
| 5 | Bài 6 lớp 12 đa dạng hơn | Mỗi mức 15 câu, câu về hình lập phương giảm từ khoảng 13 xuống **4**. Câu chính: quy tắc hình hộp (hình hộp bất kì), trung điểm trong tứ diện, tích vô hướng và góc trong **tứ diện đều**, hợp lực của **ba lực đôi một vuông góc**, **hình chóp** đáy hình bình hành, 1 câu tích vô hướng trong hình lập phương. Tự luyện: thêm 3 bộ sinh câu (tứ diện đều, lực, hình chóp), thay phương án tiếng Anh "depends on the edge" bằng tiếng Việt. | `content/grade12/vectors-in-space.py`, `tools/sp_g12.py`. Mọi đáp án đều có `assert` kiểm tra bằng tọa độ. |

## 2. Kiểm tra lại

- Dựng lại toàn bộ; số câu không đổi (2.595 trắc nghiệm, 486 đúng/sai; Mức 2–3: 2.398).
- **Dựng MathJax trên trình duyệt, 90 trang, mở hết lời giải và cả 3 mức: 0 lỗi.** Ba chỗ còn hiện mã thô là các lỗi đã có từ trước (T-003 ở `g10-ineq-sys-01`, `g10-prob-02`; T-016 ở `g12-mono-02`).
- Đã xem trực quan: kí hiệu \(n\,\vdots\,6\Rightarrow n\,\vdots\,3\) (lớp 10 Bài 1), các ý a) b) xuống dòng (lớp 10 Bài 21, Ví dụ 1), câu "Trong bốn phát biểu…" mỗi phát biểu một dòng.
- Bài 6 lớp 12: đã giải lại thủ công cả 45 câu của 3 mức sau khi đổi (đúng hết).
- Quét tĩnh: 0 lồng delimiter, 0 lệnh dính chữ, 0 khóa ngoài phương án, 0 phương án trùng. `build_all.py --check` hợp lệ; `test-lessons-g11.py` 10, 11, 12, `test-mathjax.py` và `test-geometry-notation.py` đều đạt. (Lần chạy đầu, bước lớp 12 báo câu trung điểm ở Mức 1 và Mức 3 trùng nhau; đã đổi Mức 3 sang trung điểm của \(AD\), \(BC\) với \(\overrightarrow{MN}=\tfrac12(\overrightarrow{AB}+\overrightarrow{DC})\), rồi chạy lại đạt.)

## 3. Lưu ý

- `fix_layout` áp dụng tự động cho mọi bài dựng sau này. Người soạn **không cần** tự chèn `<br>` hay đổi `\frac`. Trong văn bản tự luyện (`tools/sp_*.py`) **không** được chèn `<br>`, vì dấu `<` bị thoát thành `\lt`.
- Việc tách ý chỉ áp dụng cho đoạn `<p>`/`<li>`. Các ý nằm **trong** một công thức duy nhất cần sửa ở nguồn (như câu "Trong bốn phát biểu…" đã sửa).
