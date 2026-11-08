# 01 – TỔNG QUAN KIỂM ĐỊNH WEBSITE TOÁN THPT "TOÁN VÀ TIẾNG ANH"

Ngày kiểm định: 07/11/2026 · Phiên bản kiểm định: mã nguồn hiện có trong thư mục `toanvata` (nhánh `main`, không có thay đổi chưa lưu).
Hồ sơ gồm 9 tệp `01_…` đến `09_…` trong thư mục `kiem-dinh/`. **Không có nội dung gốc nào bị sửa** trong lần kiểm định này.

> **Cập nhật 08/11/2026:** theo yêu cầu "Sửa Ưu tiên 1", đã sửa và kiểm tra lại M-001, M-007 (Critical), M-003, M-008, T-001, T-002 (High) – xem `10_BAO_CAO_SUA_UU_TIEN_1.md`. Mục 7 của Ưu tiên 1 (kiểm định thủ công Mức 2–3) **đã làm xong: 2.398/2.398 câu**, xem `11_KIEM_DINH_MUC_2_3.md`. Kết quả phát hiện thêm **1 lỗi Critical (M-108: khóa sai), 2 lỗi High (M-101, M-107: nhiều phương án đúng)**, 4 lỗi Medium và một số lỗi Low. **M-101 có cả ở Mức 1 câu 14 và đã bị bỏ sót trong lần kiểm định 07/11.** Ba lỗi chặn M-108, M-101, M-107 **đã sửa và kiểm tra lại** ngày 08/11. Cùng ngày đã sửa trình bày theo góp ý của chủ website (kí hiệu chia hết, các ý xuống dòng, `\dfrac`, liệt kê dưới câu hỏi, đa dạng hóa Bài 6 lớp 12): xem `12_SUA_TRINH_BAY_THEO_GOP_Y.md`. Kết luận "chưa đạt chuẩn" bên dưới vẫn giữ nguyên; điểm 74,5 chưa được chấm lại. Các bảng trạng thái trong 02–07 phản ánh thời điểm 07/11/2026.

---

## 1. Kết luận trả lời câu hỏi cuối cùng

> **Website CHƯA đủ điều kiện để học sinh dùng làm tài liệu học Toán chính thức.**
> Phần lý thuyết và ví dụ có chất lượng toán học **tốt** (không phát hiện định nghĩa, định lí hay công thức cốt lõi nào sai), nhưng hệ thống bài tập còn **đáp án sai mang tính hệ thống** (lỗi trong bộ sinh câu hỏi, lặp lại ở cả 3 mức học), một số câu không đọc được do lỗi hiển thị, và còn thiếu một số nội dung bắt buộc của SGK.
> Theo **quy tắc chặn điểm** (có đáp án sai chưa xử lý; thiếu nội dung bắt buộc chưa ghi nhận), website **không được xếp loại đạt chuẩn**, bất kể điểm tổng.
> Sau khi khắc phục nhóm lỗi Ưu tiên 1–2 trong `08_KE_HOACH_KHAC_PHUC.md` và kiểm định Mức 2–3, website có khả năng đạt mức **Khá**.

## 2. Phạm vi và phương pháp

| Hạng mục | Số liệu |
|---|---|
| Công nghệ | Website tĩnh: HTML/CSS/JS thuần, MathJax 3.2.2 (CDN), LocalStorage; nội dung soạn bằng Python (`content/*.py`) → dựng thành HTML (`tools/mb_model.py`, `tools/build_all.py`); câu "tự luyện" sinh tự động (`tools/sp_*.py`); hình vẽ TikZ/PGFPlots → SVG (`img/`) |
| Nguồn dữ liệu | `lessons.json` (90 mục), `config/model.json` (khóa bài, thứ tự, số bài SGK), `content/grade10–12/*.py`, `lessons/**/*.html` |
| Tổng số bài trong danh mục | 90 (lớp 10: 29, lớp 11: 39, lớp 12: 22) |
| Bài đang mở cho học sinh | **79** (27 + 33 + 19) – khớp số bài của SGK KNTT 10/11/12 |
| Bài tạm khóa (ẩn, không tính) | 11 – **không kiểm định nội dung** (xem mục 5) |
| Số câu luyện tập (bài đang mở) | **3.597 câu** = 3 mức × 1.199 câu. Mức 1, 2, 3 là **ba bộ câu khác nhau** (khác số liệu) |
| Ví dụ có lời giải | ≈ 400 (5–8 ví dụ/bài) |

**Đã thực hiện:**
1. Đọc toàn văn (bản tiếng Việt – Mức 1) **79/79 bài**: lý thuyết, mọi ví dụ, mọi câu luyện tập Mức 1 (**1.199 câu**), lỗi thường gặp, tổng kết. Mỗi đáp số được tính lại độc lập bằng tay (cấp số, tích phân, tứ phân vị ghép nhóm, phương sai, tích có hướng, Bayes…), không dùng mô hình AI khác để xác nhận.
2. Truy ngược mã nguồn với các lỗi tìm thấy để xác định lỗi đơn lẻ hay lỗi hệ thống của bộ sinh câu.
3. Quét tự động toàn bộ HTML (cả 3 mức): khóa đáp án không có trong phương án, phương án trùng nhau, LaTeX lồng nhau, mã HTML thô trong công thức, mã TeX lọt ra ngoài công thức.
4. Dựng thật 79 trang bằng MathJax trong trình duyệt (máy chủ tĩnh cục bộ), đếm lỗi lệnh TeX không xác định và chuỗi TeX thô còn hiển thị.
5. Chạy bộ kiểm thử sẵn có của dự án (các bài kiểm thử không ghi tệp), đọc mã `js/app.js`, `js/lesson-kit-v2.js`, `js/progress.js`, `js/lesson-bridge.js`; thử chức năng: duyệt, tìm kiếm, lọc, mở bài, chấm câu, đánh dấu hoàn thành, tiến độ, giao diện điện thoại.

**Chưa thực hiện / giới hạn (ghi rõ để không bị hiểu nhầm là "đã kiểm tra toàn bộ"):**
- **Mức 2 và Mức 3 (2.398 câu) chưa được giải lại thủ công từng câu.** Chỉ được quét tự động và kiểm tra có chủ đích các họ câu đã phát hiện lỗi ở Mức 1 (xác nhận 3 lỗi hệ thống lặp lại ở cả 3 mức). → Trạng thái lúc 07/11: *Chưa kiểm định thủ công*. **Cập nhật 08/11: đã giải lại thủ công toàn bộ 2.398 câu, xem `11_KIEM_DINH_MUC_2_3.md`.**
- Bản tiếng Anh (Mức 2–3) chỉ được xem khi cần đối chiếu, không kiểm định chất lượng ngôn ngữ.
- **Không có tệp SGK trong dự án.** Tài liệu nội bộ `docs/CURRICULUM.md` nhắc tới `Toan_10_Ket_noi_tri_thuc.md`… nhưng các tệp này không có trong thư mục. Việc đối chiếu chương trình dựa trên **mục lục SGK Toán 10, 11, 12 – bộ Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam)** theo hiểu biết của hội đồng kiểm định; các điểm cần mở sách in để khẳng định được đánh dấu **"Cần đối chiếu bản in"**.
- Không kiểm tra trên thiết bị iOS/Android thật; giao diện điện thoại kiểm tra bằng mô phỏng 375×812.
- 11 bài tạm khóa không được kiểm định nội dung.

## 3. Bảng điểm (thang nội bộ 100, không phải chứng nhận chính thức)

| Hạng mục | Trọng số | Điểm | Căn cứ chính |
|---|---:|---:|---|
| Độ chính xác toán học | 30 | **24** | Lý thuyết/ví dụ: 0 lỗi định nghĩa–định lí–công thức sai; nhưng 2 lỗi Critical hệ thống (khóa đáp án sai/không có phương án đúng), 1 câu 2 đáp án đúng, 1 câu sai bản chất (mất dấu ′), 1 chứng minh lập luận không hợp lệ, một số phát biểu thiếu điều kiện |
| Độ đầy đủ và bám sát SGK | 20 | **15** | 79/79 bài khớp danh mục KNTT; thiếu tứ phân vị ở Bài 9 lớp 11, thiếu "tốc độ thay đổi" ở Bài 5 lớp 12, thiếu "k·vectơ" trong không gian (Bài 6 lớp 12), thiếu định lí giao tuyến ba mặt phẳng (Bài 11 lớp 11); không có bài tập cuối chương; một số nội dung mở rộng không gắn nhãn |
| Chất lượng lý thuyết và sư phạm | 15 | **11** | Cấu trúc bài tốt, dẫn nhập–ví dụ phân mức hợp lí; nhưng nhiều lời giải câu Đúng/Sai "né tránh", lời giải sinh máy chung chung, chữ tiếng Anh lọt vào Mức 1 |
| Bài tập và lời giải | 15 | **10** | 3.597 câu, phân bố mức độ hợp lí; lỗi hệ thống ở 3 họ câu; ⅔ ngân hàng câu chưa kiểm định thủ công |
| Hình vẽ, đồ thị, LaTeX | 8 | **5** | 153 hình TikZ/PGF đạt kiểm thử; nhưng 76 lỗi MathJax (lệnh dính chữ, lồng delimiter), ≈400 mảnh TeX thô hiển thị, 4 câu có phương án là mã HTML rác, 1 hình Venn không khớp ví dụ |
| Giao diện và trải nghiệm | 5 | **4** | Gọn, nhất quán, có menu điện thoại, bảng có cuộn ngang |
| Chức năng và kỹ thuật | 4 | **3** | Chấm đáp án đúng (chấp nhận "3,0", "280 m"…); không lưu bài làm/điểm; tìm kiếm không hỗ trợ gõ không dấu |
| Bảo mật và dữ liệu | 3 | **2,5** | Thoát chuỗi HTML đúng, kiểm tra origin của postMessage; đáp án nằm sẵn trong DOM; bài khóa vẫn truy cập trực tiếp được |
| **Tổng** | **100** | **74,5** | Xếp loại theo điểm: **Cần cải thiện** – và **bị chặn đạt chuẩn** do quy tắc chặn điểm |

## 4. Tổng hợp lỗi

| Mức độ | Toán học (05) | Sư phạm / chương trình (06, 09) | Kỹ thuật (07) | Tổng |
|---|---:|---:|---:|---:|
| Critical | 2 | 0 | 0 | **2** |
| High | 4 | 2 | 2 | **8** |
| Medium | 5 | 11 | 6 | **22** |
| Low | 14 | 10 | 7 | **31** |

Ba lỗi nặng nhất:
1. **M-001 (Critical)** – Bài 2 lớp 10: mọi câu "Tìm phần bù của khoảng trong ℝ" có **khóa đáp án sai** ở cả 3 mức (lỗi `tools/sp_g10.py:154–161`).
2. **M-007 (Critical)** – Bài 28 lớp 11, câu 1: nhãn biến cố bị tráo (lỗi giải nén `content/grade11/union-intersection-independence.py:83`) → đề hiển thị **không có phương án đúng**, ở cả 3 mức.
3. **M-008 (High)** – Bài 6 lớp 12, câu 1: mất dấu phẩy trên (AA′ thành AA) → câu hỏi về quy tắc hình hộp biến thành câu khác, lời giải sai, ở cả 3 mức.

## 5. Danh sách bài đã / chưa kiểm định

- **Đã kiểm định (Mức 1 + lý thuyết + ví dụ): 79 bài** – liệt kê từng bài trong `02_`, `03_`, `04_`.
- **Chỉ quét tự động (chưa giải tay): Mức 2 và Mức 3 của cả 79 bài.**
- **Chưa kiểm định (bài tạm khóa, học sinh không mở được qua giao diện):** `g10-sets-02`, `g10-algebra-01`, `g11-functions-01`, `g11-limits-02`, `g11-derivatives-01`, `g11-space-02`, `g11-exp-02`, `g11-space-03`, `g12-antider-01`, `g12-antider-02`, `g12-mono-02`. Lưu ý: các tệp HTML này vẫn tải được bằng đường dẫn trực tiếp (T-008).

## 6. Nhận xét về bộ kiểm thử sẵn có

12/13 kiểm thử của dự án **đạt** (`test-graph-core`: 103/103; `test-lesson-graphs`; `test-tex-figures`: 153 hình; `build_all --check`; `test-lessons-g11` cho lớp 10, 11, 12; `test-mathjax`: "59.507 công thức, 0 lỗi"…); riêng `check_html_snapshot.py` **không đạt** vì bản gốc so sánh đã cũ (5 tệp lớp 12). (Không chạy `make_graph_demo.py` vì kiểm thử này ghi đè tệp trong dự án.) Tuy nhiên các kiểm thử này chủ yếu kiểm tra **tính tự nhất quán** (ví dụ: chọn đúng khóa đáp án thì được điểm tối đa) chứ **không kiểm tra khóa đáp án có đúng về toán học**, và không phát hiện TeX thô/HTML rác trong phương án. Vì vậy "tất cả đạt" không đồng nghĩa với "nội dung đúng". Xem đề xuất kiểm thử bổ sung trong `08_`.
