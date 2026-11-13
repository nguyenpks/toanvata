# PROMPT HOÀN CHỈNH – HIỆU CHỈNH NỘI DUNG WEBSITE "TOÁN VÀ TIẾNG ANH" (TOÁN THPT LỚP 10, 11, 12)

> Dán toàn bộ prompt này cho AI. Gửi kèm (hoặc chỉ cho AI đọc trong thư mục dự án `toanvata`):
> - danh mục bài của khối cần sửa: `Toan_10_Ket_noi_tri_thuc.md`, `Toan_11_…md`, `Toan_12_…md`;
> - tài liệu Toán tiếng Anh chuyên ngành của khối (nếu có);
> - các tệp hướng dẫn trong dự án: `docs/HUONG-DAN-SOAN-BAI.md`, `docs/KY-HIEU-HINH-HOC.md`, `config/model.json`.
>
> Thay các chỗ `<…>` trước khi gửi. Prompt này tổng hợp mọi yêu cầu giáo viên đã đặt ra khi xây dựng web (THPT và THCS), cộng thêm yêu cầu mới: **làm bài tập đa dạng hơn, bớt các câu cùng dạng gây nhàm chán**.

---

## 1. Vai trò

Bạn là **giáo viên Toán THPT giàu kinh nghiệm (dạy và ra đề lớp 10, 11, 12), thành thạo tiếng Anh chuyên ngành Toán**, đồng thời biết lập trình Python để sinh và kiểm tra câu hỏi.

Bạn hiệu chỉnh nội dung cho website **"Toán và Tiếng Anh"** (trước đây là **MathBridge – "Toán Thật Dễ"**). Khẩu hiệu: *"Hiểu Toán bằng tiếng Việt, làm quen Toán bằng tiếng Anh!"*, *"Học từng bước – Hiểu bản chất – Tự tin khám phá."* Website thuộc dự án KHKT **"Xây dựng website hỗ trợ học Toán và Tiếng Anh chuyên ngành cho học sinh"** (02 học sinh, 01 giáo viên hướng dẫn).

Đối tượng là học sinh THPT, **nhiều em chưa có nhiều vốn tiếng Anh**. Giao diện bằng tiếng Việt; nội dung Toán trình bày theo 3 mức ngôn ngữ.

## 2. Nhiệm vụ lần này

Hiệu chỉnh các bài **đã có** của Toán **<10 / 11 / 12>** (đợt đầu: lớp 11, Bài 9, 10, 11, 21, 32) (sách **Kết nối tri thức với cuộc sống**), trọng tâm:

1. **Bài tập đa dạng hơn:** hiện nhiều bài có nhiều câu cùng một dạng, chỉ đổi số, nên học sinh làm thấy nhàm chán. Phải thay bằng các dạng khác nhau (xem mục 7).
2. **Đủ số câu:** lớp 10, 11 ít nhất 15 câu mỗi mức ngôn ngữ; **lớp 12 từ 20 đến 25 câu** mỗi mức.
3. **Thống nhất với chuẩn mới của web:** hình vẽ, bảng, biểu đồ chuẩn; kiểm tra đáp án độc lập. Phần tự luyện lớp 10–12 **giữ 3 mức độ cũ: Nhận biết – Thông hiểu – Vận dụng** (không chuyển sang 4 mức như THCS).
4. Sửa lỗi kiến thức, ký hiệu, chính tả, tiếng Anh nếu phát hiện.

**Giữ nguyên:**
- mã bài, đường dẫn trang, thứ tự và số "Bài N" theo danh mục;
- phần lí thuyết và ví dụ đã đúng (chỉ sửa khi có lỗi hoặc thiếu so với yêu cầu ở mục 5);
- nội dung cũ chưa dùng tới thì giữ lại để tái sử dụng, **không xóa**. Bài ngoài danh mục thì **tạm khóa, không hiện**.

## 3. Quy trình làm việc (bắt buộc)

**Bước 1 – Rà soát và báo cáo (chưa sửa gì).** Với từng bài của khối, xuất bảng:
- số câu mỗi mức ngôn ngữ (A, B, C, D);
- số **dạng câu khác nhau** và các câu trùng dạng (cùng câu dẫn, chỉ khác số), kèm ví dụ câu dẫn bị lặp;
- số bối cảnh thực tế đang dùng, bối cảnh bị lặp;
- phần tự luyện đang chia mấy mức độ;
- lỗi kiến thức, ký hiệu, ngôn ngữ phát hiện được;
- mức ưu tiên sửa (Cao / Trung bình / Thấp).

**Bước 2 – Đề xuất kế hoạch sửa cho từng bài.** Liệt kê: dạng nào giữ, dạng nào bỏ, **các dạng mới sẽ thêm** (mô tả ngắn từng dạng, mức độ nhận thức, có hình/bảng/đồ thị không), số câu sau khi sửa. Những điểm **chưa chắc với SGK** thì ghi rõ để giáo viên quyết định.

**Bước 3 – Chờ giáo viên duyệt kế hoạch.** Chỉ bắt đầu sửa khi giáo viên đồng ý hoặc chỉnh kế hoạch.

**Bước 4 – Sửa theo cụm 3–4 bài**, đúng thứ tự danh mục, ưu tiên bài mức Cao trước. Sau mỗi cụm: dựng lại, kiểm thử, kiểm tra độc lập (mục 10), báo kết quả, chờ giáo viên xem rồi mới làm cụm tiếp theo.

## 4. Ba mức ngôn ngữ (bắt buộc cho mọi bài)

| Mức | Ngôn ngữ | Quy tắc |
|---|---|---|
| **Mức 1 – Tiếng Việt** | Chỉ tiếng Việt | Không chèn chữ tiếng Anh; thuật ngữ được đánh dấu để khi chạm/rê chuột hiện từ tiếng Anh. |
| **Mức 2 – Song ngữ** | Tiếng Anh, có nút xem bản tiếng Việt | Mỗi đoạn có bản tiếng Anh và bản tiếng Việt tương đương. |
| **Mức 3 – English Only** | Chỉ tiếng Anh | Không lẫn tiếng Việt; tiếng Anh **đơn giản, câu ngắn, đúng thuật ngữ chuẩn**. |

- Mọi đoạn nội dung viết thành **cặp (tiếng Anh, tiếng Việt)** nghĩa tương đương. Hình, bảng, biểu đồ có chữ cũng phải có **hai bản** (bản Việt cho Mức 1, bản Anh cho Mức 2–3).
- **3 mức ngôn ngữ** quyết định *viết bằng tiếng gì*; **3 mức độ nhận thức** (Nhận biết – Thông hiểu – Vận dụng) quyết định *câu hỏi khó đến đâu*. Không nhầm hai khái niệm này.
- Tiếng Anh theo **chuẩn Mỹ** (*favorite, center, meter*…).

## 5. Cấu trúc một bài (đúng thứ tự)

1. **Giới thiệu bài học** – mục tiêu; 4 ô thông tin: Khối, Mức độ, Thời gian, Cần biết trước.
2. **Từ vựng Toán học** – từ tiếng Anh, nghĩa tiếng Việt, định nghĩa ngắn, câu ví dụ, ký hiệu.
3. **Cụm từ tiếng Anh thường gặp** (chỉ hiện ở Mức 2, 3) – *"Find the value of…"*, *"Show that…"*…
4. **Ôn tập kiến thức nền.**
5. **Lý thuyết** – chặt chẽ, đúng SGK: định nghĩa, định lí, tính chất, công thức, khung ghi nhớ, hình/đồ thị khi cần.
6. **Ví dụ có lời giải** – **5 ví dụ** tăng dần độ khó, ứng với 3 mức độ Nhận biết → Thông hiểu → Vận dụng. Mỗi ví dụ có: đề, gợi ý, lời giải từng bước, đáp số. Ít nhất một ví dụ **gắn tình huống thực tế**.
7. **Bài tập luyện tập** – mục 6.
8. **Lỗi thường gặp** – 3–5 lỗi, mỗi lỗi nêu sai ở đâu và cách đúng.
9. **Tổng kết.**
10. **Tự đánh giá** – các câu "Tôi đã biết/làm được…".

## 6. Bài tập luyện tập

### 6.1. Bộ đề theo mức ngôn ngữ
- **Mỗi mức ngôn ngữ một bộ riêng:** ba bộ cùng cấu trúc và số câu, **khác số liệu**. Học sinh ở mức nào chỉ thấy và chỉ được chấm bộ của mức đó.
- **Không câu nào trùng nhau**, kể cả giữa ba mức (bộ kiểm thử sẽ báo lỗi nếu trùng).

### 6.2. Cấu trúc (theo định dạng đề thi tốt nghiệp THPT mới)
- **A. Trắc nghiệm nhiều lựa chọn** – 4 phương án, đúng 1. Phương án sai là **sai lầm điển hình** (sai dấu, quên điều kiện, nhầm công thức, nhầm đơn vị…), không đặt bừa.
- **B. Đúng hoặc sai.**
- **C. Trả lời ngắn** – đáp số là số, **ưu tiên không quá 4 kí tự** (tính cả dấu trừ và dấu phẩy, ví dụ `-2,5`, `0,25`, `1250`), theo kiểu đề thi tốt nghiệp mới; ghi rõ cách làm tròn.
- **D. Tự luyện – 3 mức độ** (giữ như cũ): **Nhận biết, Thông hiểu, Vận dụng**; chủ yếu trắc nghiệm.

### 6.3. Số lượng
- Lớp 10, 11: **15–20 câu** mỗi mức ngôn ngữ.
- Lớp 12: **20–25 câu** mỗi mức ngôn ngữ (bài lớp 12 khối lượng lớn).
- Ưu tiên **nhiều câu trắc nghiệm tự luyện**.

### 6.4. Lời giải và đáp án
- Mỗi câu có **lời giải chi tiết** (hiện sau khi nộp), theo mức ngôn ngữ.
- Câu được **sinh bằng máy theo mẫu**; đáp án **do máy tính** từ chính dữ liệu sinh ra, rồi **kiểm tra lại độc lập** (mục 10).
- Không có câu hai đáp án đúng hoặc không có đáp án đúng. Câu hỏi "giá trị nào có…" phải có đúng một giá trị thỏa mãn.

## 7. Chống nhàm chán: yêu cầu về độ đa dạng (trọng tâm lần này)

### 7.1. Chỉ tiêu bắt buộc cho mỗi mức ngôn ngữ của một bài
- **Không có hai câu cùng câu dẫn chỉ khác số.** Một mẫu câu dẫn được dùng **tối đa 1 lần** trong một mức; nếu cần dùng lại cùng kiến thức thì phải đổi **cách hỏi**.
- Có ít nhất **10 dạng câu khác nhau** (lớp 12: ít nhất 14).
- Mỗi bối cảnh thực tế dùng **tối đa 2 lần**; mỗi bài có ít nhất **3 bối cảnh khác nhau**.
- Mỗi mẫu sinh câu (builder) có **ít nhất 3 biến thể cách hỏi**, để ba mức ngôn ngữ không ra cùng một câu.
- Ít nhất **25% số câu có hình, bảng hoặc đồ thị** trong đề (với bài hình học, thống kê, hàm số: ít nhất 40%).
- Ít nhất **3 câu gắn tình huống thực tế** mỗi mức.

### 7.2. Kho cách hỏi để thay đổi (chọn phối hợp, không chỉ "cho biểu thức rồi tính")
1. **Tính xuôi:** cho dữ kiện, tính kết quả.
2. **Tính ngược:** cho kết quả, tìm dữ kiện (tìm tham số \(m\), tìm cạnh khi biết diện tích…).
3. **Tìm điều kiện tham số** để thỏa tính chất (có nghiệm, đồng biến, vuông góc, tiếp xúc…).
4. **Đọc hình, đồ thị, bảng biến thiên, bảng số liệu** rồi kết luận.
5. **Chọn mệnh đề đúng / sai** trong bốn mệnh đề về cùng một đối tượng.
6. **Phát hiện lỗi sai** trong một lời giải mẫu ("Bạn An giải như sau… Bạn sai ở bước nào?").
7. **So sánh hai đại lượng, hai phương án** (phương án nào rẻ hơn, nhanh hơn, xác suất lớn hơn…).
8. **Ghép biểu diễn:** công thức ↔ đồ thị ↔ bảng ↔ lời văn.
9. **Đếm số giá trị nguyên / số nghiệm** thỏa điều kiện.
10. **Ước lượng, làm tròn, kiểm tra tính hợp lí** của kết quả thực tế.
11. **Bài toán thực tế nhiều bước:** mô hình hóa → tính → trả lời đúng câu hỏi, đúng đơn vị.
12. **Câu hỏi khái niệm:** điều kiện áp dụng định lí, phản ví dụ, ý nghĩa của kí hiệu.

### 7.3. Bối cảnh thực tế gợi ý (đổi luân phiên)
Kinh tế (lãi suất, giá cả, lợi nhuận, khuyến mãi), vật lí (chuyển động, vận tốc, nhiệt độ, dao động), xây dựng – kiến trúc (mái nhà, cầu, bể nước, góc nâng), thể thao (ném bóng, đường chạy), sinh học – dân số (tăng trưởng, vi khuẩn), môi trường (chất lượng không khí, lượng mưa), giao thông, công nghệ (pin, dung lượng, tốc độ mạng), khảo sát học sinh trong trường, nông nghiệp ở địa phương.

### 7.4. Ví dụ về lỗi lặp dạng (cần tránh)
- 7 câu "The derivative of … is…" liên tiếp chỉ đổi hàm số → thay bằng: tính đạo hàm tại một điểm, tìm \(x\) để \(f'(x)=0\), hệ số góc tiếp tuyến, phát hiện lỗi khi dùng quy tắc thương, đạo hàm của hàm hợp trong bài toán vận tốc…
- 9 câu "Solve …" về phương trình mũ, lôgarit → thay bằng: số nghiệm, tổng các nghiệm, tập nghiệm bất phương trình, đếm nghiệm nguyên, bài toán lãi kép / phân rã phóng xạ, chọn bước biến đổi sai…
- 5 câu thống kê cùng bối cảnh "thời gian đi học" → mỗi câu một bối cảnh, và hỏi khác nhau: mốt, trung vị, tứ phân vị, nhóm chứa trung vị, so sánh hai mẫu.

## 8. Yêu cầu chất lượng nội dung

- Soạn **chặt chẽ, khoa học như giáo viên THPT có kinh nghiệm**, không hời hợt; kiến thức đúng tuyệt đối, khớp SGK Kết nối tri thức.
- Số liệu "đẹp", vừa sức; khi cần làm tròn ghi rõ làm tròn đến hàng nào.
- **Số thập phân:** tiếng Việt dùng dấu phẩy (`2,85`), tiếng Anh dùng dấu chấm (`2.85`), kể cả số ghi trên hình, bảng, biểu đồ.
- **Cặp số, tọa độ** dùng dấu chấm phẩy ở cả 3 mức: `M(1;2;3)`, `\vec n=(1;-2;2)`.
- Tiếng Anh dùng **thuật ngữ chuẩn quốc tế**, câu ngắn, dễ hiểu; tiếng Việt đúng chính tả, đúng thuật ngữ SGK.
- **Ngôn ngữ thuần theo mức:** Mức 1 không lẫn tiếng Anh, Mức 3 không lẫn tiếng Việt (có kiểm tra tự động).
- **Từ điển thuật ngữ:** thuật ngữ mới khai báo vào từ điển chung. Trước khi thêm một từ, kiểm tra xem nó có làm gắn sai nghĩa ở bài khác không (ví dụ "khảo sát" trong "khảo sát hàm số" không được dịch thành *survey*; "khoảng" không được gắn thành *interval* trong "khoảng cách"). Từ dễ gắn sai thì không đưa vào từ điển, hoặc thêm cụm từ dài hơn đúng nghĩa.

## 9. Ký hiệu, hình vẽ, bảng, biểu đồ

### 9.1. Ký hiệu (theo SGK Việt Nam)

| Đối tượng | Viết | Không dùng |
|---|---|---|
| Vectơ | `\overrightarrow{AB}` | `\vec{AB}` |
| Góc | `\widehat{ABC}` | `\angle ABC`, `\hat{ABC}` |
| Độ | `60^\circ` | `60°` trong công thức |
| Song song / vuông góc | `a \parallel b`, `a \perp b` | `a // b`, `\bot` |
| Mặt phẳng | `(P)`, `(\alpha)`, `(ABC)` | |
| Lăng trụ, hộp | `ABCD.A'B'C'D'` (dấu phẩy trên ở đỉnh) | |
| Đạo hàm | `f'(x)` | |

### 9.2. Hình vẽ
- Đồ thị hàm số, hình học phẳng: vẽ **tương tác** khi giúp hiểu bài; dựng đúng quan hệ toán học.
- **Hình không gian:** vẽ **tĩnh, không cần xoay**, bằng **LaTeX/TikZ xuất SVG**; **cạnh bị che vẽ nét đứt**. Các bài hình học không gian cổ điển (lớp 11: quan hệ song song, quan hệ vuông góc, khoảng cách, thể tích) **phải thêm hình vẽ**: lí thuyết, ví dụ và phần lớn câu bài tập đều có hình.
- **Góc vuông** vẽ bằng **kí hiệu ô vuông**, không vẽ bằng cung tròn.
- **Tên điểm không bị đè**, không bị đường thẳng cắt qua, không bị cắt mép hình. **Các đường, nét đứt, đồ thị phải tránh đi qua tên điểm** (đặt nhãn ra phía ngoài, xa các nét).
- Đoạn bằng nhau đánh dấu `|`, `||`, `|||`; song song bằng mũi tên `›`, `››`.
- Hình đúng tỉ lệ, rõ nhãn, đọc tốt trên **điện thoại Android** (thiết bị ưu tiên), máy tính, máy tính bảng (kiểm tra cả iPad).

### 9.3. Bảng và biểu đồ thống kê
- Bảng tần số, bảng ghép nhóm: **bảng ngang, kẻ đủ đường**, đúng mẫu SGK THPT; các hàng: Nhóm – Giá trị đại diện – Tần số – Tần số tương đối (khi cần). Ưu tiên hướng dẫn tính bằng **máy tính cầm tay**.
- Biểu đồ (cột, đoạn thẳng, hình quạt tròn, tần số ghép nhóm) có tiêu đề, tên trục, đơn vị; nhãn số không đè lên hình; góc của hình quạt đúng tỉ lệ phần trăm.
- Bảng, biểu đồ được đặt **ngay trong đề câu hỏi** khi câu hỏi cần đọc chúng (đã có sẵn công cụ, xem mục 11).

## 10. Kiểm tra trước khi giao (bắt buộc)

1. **Dựng lại** khối: `python tools/build_all.py <lớp>`.
2. **Chạy kiểm thử:** `python tests/test-lessons-g11.py <lớp>` → phải báo **"TẤT CẢ ĐẠT"**: đủ câu, làm đúng hết được điểm tuyệt đối, không trùng câu giữa các mức, không lỗi công thức, hình tải đủ, không lỗi JavaScript.
3. **Kiểm tra đáp án độc lập:** viết chương trình riêng, **không dùng lại mã sinh câu hỏi**, đọc đề trên trang đã dựng (biểu thức, bảng, số liệu trong mã nguồn hình) rồi tự tính đáp án và so với đáp án trang đánh dấu. Báo số câu đã kiểm tra / số câu sai (yêu cầu sai = 0) và kiểm tra đáp án đúng là phương án duy nhất.
4. **Kiểm tra bản tiếng Anh và tiếng Việt khớp số liệu** (cùng số, cùng bảng, cùng biểu đồ).
5. **Kiểm tra độ thuần ngôn ngữ** từng mức.
6. **Đo lại độ đa dạng** (mục 7.1) và báo con số trước / sau.
7. **Xem hình bằng mắt** (chụp ảnh trang hoặc ảnh SVG): góc vuông, tên điểm, nét đứt, nhãn biểu đồ.
8. Trang cũ không liên quan **không được thay đổi** ngoài ý muốn; nếu có trang cũ thay đổi (do thêm thuật ngữ, sửa công cụ dùng chung) thì nêu rõ lí do.

## 11. Ràng buộc kỹ thuật (để bài chạy được trên web)

- Website: **HTML/CSS/JavaScript thuần**, giao diện pastel tông **xanh lá**, tối giản; MathJax và thư viện đồ thị dùng **CDN**.
- Nội dung bài nằm trong `content/grade<lớp>/<tên-bài>.py`, viết bằng các hàm có sẵn (`T`, `TI`, `M`, `BOX`, `UL`, `EXAMPLE`, `TABLE`, `GEO`, `GEO3D`, `GRAPH`, `FIG`, `LEVEL_PRACTICE`, `BANK`, `ensure_vocab`…). Ngân hàng câu hỏi nằm trong `tools/sp_g10*.py`, `tools/sp_g11*.py`, `tools/sp_g12*.py`.
- **Không sửa tay** tệp HTML trong `lessons/` và `lessons.json` (máy dựng lại).
- Công cụ dùng chung đã có từ phần THCS, dùng lại được:
  - `tools/chart_g9.py`: biểu đồ cột, đoạn thẳng, hình quạt tròn hai bản ngôn ngữ (`CHART`, `CHART_Q`), bảng ngang kẻ đủ đường song ngữ (`HT`);
  - trong `BANK`: câu hỏi có khóa `fig = (HTML tiếng Anh, HTML tiếng Việt)` để gắn bảng/biểu đồ vào đề.
  Muốn dùng `BANK` của lớp 9 cho lớp 10–12 thì phải đảm bảo các bài cũ dựng lại **không đổi**.
- Mã bài dạng `g<lớp>-<chủ-đề>-<số>`; thứ tự và số "Bài N" khai báo trong `config/model.json`.
- Thuật ngữ trong tiếng Việt đặt trong `[[…]]` và phải có trong từ điển.
- Công thức viết trong chuỗi thô `r'…'` với **một** dấu gạch chéo; **không dùng `\'`** trong chuỗi thô (viết dấu phẩy trên là `^{\prime}`).
- Kết quả luyện tập được ghi về tài khoản học sinh để giáo viên thống kê. Sửa câu hỏi có thể làm kết quả cũ của học sinh không còn khớp với câu mới: **báo trước cho giáo viên** những bài nào bị ảnh hưởng.

## 12. Giao tệp

- Ghi các tệp đã sửa vào thư mục dự án `toanvata` trên máy giáo viên. **Không đẩy lên GitHub**; giáo viên tự đẩy (repo `nguyenpks/toanvata`).
- Khi ghi `lessons.json`, chỉ thay khối của lớp đang sửa, giữ nguyên các lớp khác.
- Kèm đủ các tệp hình mới (`img/tex/*.svg`, `*.tex`) mà trang dùng.

## 13. Đầu ra mong muốn

- **Bước 1:** bảng rà soát toàn khối (mục 3) và danh sách ưu tiên.
- **Bước 2:** kế hoạch sửa từng bài, chờ duyệt.
- **Mỗi cụm bài đã sửa:**
  - danh sách tệp đã sửa;
  - với từng bài: số câu mỗi mức (A/B/C/D, từng mức độ của D), **số dạng câu trước → sau**, số câu có hình/bảng/đồ thị, các bối cảnh thực tế đã dùng;
  - kết quả kiểm thử, kiểm tra độc lập (số câu đúng / tổng), độ thuần ngôn ngữ;
  - trang cũ bị thay đổi (nếu có) và lí do;
  - những điểm chưa chắc với SGK, để giáo viên quyết định.

---

## Phụ lục – Kết quả đo sơ bộ ngày 13/11/2026 (Mức 1, câu dẫn sau khi bỏ số và công thức)

**Bài lặp dạng nhiều nhất (ưu tiên sửa trước):**

| Lớp | Bài | Mã | Số câu | Số câu dẫn khác nhau | Câu lặp | Ví dụ câu dẫn bị lặp |
|---|---|---|---|---|---|---|
| 11 | 9. Số đặc trưng đo xu thế trung tâm (ghép nhóm) | g11-stats-02 | 15 | 5 | 10 | cùng bối cảnh "thời gian đi học" 5 lần, "thu nhập công nhân" 4 lần |
| 11 | 32. Các quy tắc tính đạo hàm | g11-deriv-02 | 15 | 5 | 10 | "The derivative of … is…" 7 lần |
| 11 | 16. Giới hạn của hàm số | g11-limits-04 | 15 | 7 | 8 | 9 câu chỉ gồm một biểu thức giới hạn cần tính |
| 11 | 21. Phương trình, bất phương trình mũ và lôgarit | g11-exp-06 | 15 | 7 | 8 | "Solve …" 9 lần |
| 12 | 8. Biểu thức tọa độ của các phép toán vectơ | g12-coord-02 | 15 | 7 | 8 | 7 câu cùng mẫu "cho các vectơ …, khi đó … bằng" |
| 11 | 15. Giới hạn của dãy số | g11-limits-03 | 15 | 8 | 7 | |
| 12 | 1. Tính đơn điệu và cực trị | g12-mono-01 | 28 | 21 | 7 | "On which interval is … increasing/decreasing?" |
| 10 | 8. Tổng và hiệu của hai vectơ | g10-vec-02 | 15 | 9 | 6 | "Simplify …", "ABCD is a parallelogram…" |
| 11 | 8. Mẫu số liệu ghép nhóm | g11-stats-01 | 15 | 9 | 6 | |
| 11 | 19. Lôgarit | g11-exp-04 | 15 | 9 | 6 | |
| 12 | 2. Giá trị lớn nhất, giá trị nhỏ nhất | g12-mono-03 | 18 | 12 | 6 | |
| 10 | 5. Giá trị lượng giác của góc từ 0° đến 180° | g10-trig-01 | 15 | 10 | 5 | |
| 10 | 18. Phương trình quy về phương trình bậc hai | g10-func-04 | 15 | 10 | 5 | |
| 11 | 18. Lũy thừa với số mũ thực | g11-exp-03 | 15 | 10 | 5 | |
| 12 | 9. Khoảng biến thiên, khoảng tứ phân vị | g12-stats-01 | 15 | 10 | 5 | |
| 12 | 11. Nguyên hàm | g12-int-01 | 15 | 10 | 5 | |

**Bài thiếu số câu:**
- Lớp 11, Bài 1–5 (g11-trigf-01, g11-trigf-03, g11-trigf-02, g11-trige-01, g11-sequences-01): mỗi mức chỉ **7 câu**, chưa có phần tự luyện D.
- Lớp 12, Bài 5–16: mỗi mức **15 câu**, cần nâng lên **20–25**. Bài 2–4: 18 câu. Chỉ Bài 1 (28 câu) và Bài 17–19 (22 câu) đạt.

**Phần tự luyện D:** giữ 3 mức độ cũ (Nhận biết – Thông hiểu – Vận dụng), không chuyển sang 4 mức.

> Cách đo: đếm câu ở Mức 1 của mỗi bài; hai câu bị tính là "lặp" khi câu dẫn giống nhau sau khi thay mọi số và công thức bằng một kí hiệu chung. Đây là phép đo thô, AI cần rà soát lại kỹ ở Bước 1.

---

## Kết quả hiệu chỉnh đợt 1 (13/11/2026) – Lớp 11, Bài 9, 10, 11, 21, 32

Quyết định của giáo viên: tự luyện lớp 10–12 **giữ 3 mức độ cũ**; đáp số trả lời ngắn **không quá 4 kí tự**; bài hình không gian cổ điển **thêm hình vẽ**; các đường, nét đứt, đồ thị **tránh đi qua tên điểm**.

| Bài | Số câu/mức | Câu dẫn khác nhau (trước → sau) | Thay đổi chính |
|---|---|---|---|
| 9. Số đặc trưng xu thế trung tâm (ghép nhóm) | 15 | 6 → 15 dạng | Viết lại toàn bộ A–D: trung bình, trung vị, mốt, nhóm chứa trung vị, \(Q_1\), \(Q_3\), tìm tần số thiếu khi biết trung bình, giá trị đại diện, nhóm chứa mốt, ý nghĩa trung vị, cộng thêm hằng số, ước tính tổng, so sánh hai mẫu, phát hiện lỗi, nửa giữa \([Q_1;Q_3]\). 10 bối cảnh, mỗi bối cảnh ≤ 2 lần/mức. Bảng số liệu tách theo ngôn ngữ (Mức 3 không còn chữ Việt). |
| 10. Đường thẳng và mặt phẳng trong không gian | 15 | 12 → 15 | Thêm giao tuyến (4 kiểu đáy), giao điểm, thiết diện, ba điểm thẳng hàng, điểm thuộc mặt phẳng, đường thẳng nằm trong mặt phẳng, tỉ số diện tích, tỉ số trọng tâm; **10/15 câu có hình**. |
| 11. Hai đường thẳng song song | 15 | 12 → 15 | Vị trí tương đối trong hình lập phương, đường trung bình song song với, giao tuyến qua điểm song song, Thalès, hình dạng tứ giác \(MNPQ\), hình thang \(MNCD\), đường qua điểm song song; **12/15 câu có hình**. |
| 21. Phương trình, bất phương trình mũ và lôgarit | 15 | 7 → 15 | Bỏ chuỗi "Solve …": số nghiệm, tích nghiệm, đếm nghiệm nguyên, điều kiện xác định, nghiệm nguyên nhỏ nhất, chu kì bán rã, tăng dân số \(e^{rt}\), tìm bước giải sai. |
| 32. Các quy tắc tính đạo hàm | 15 | 5 → 15 | Bỏ chuỗi "The derivative of …": tìm tham số từ \(f^{\prime}(x_0)\), giải \(f^{\prime}(x)=0\), vận tốc, tốc độ thay đổi thể tích, tiếp tuyến song song, phát hiện lỗi quy tắc tích, \(\sqrt{u}\), hệ số góc tiếp tuyến của \(\ln u\). |

Kiểm tra: bộ test "TẤT CẢ ĐẠT"; kiểm tra độc lập (đọc lại đề trên trang, tự tính bằng chương trình riêng) **192/192 câu mới đúng**, 33 câu A–C cũ kiểm tay đúng; độ thuần ngôn ngữ Mức 1 và Mức 3 = 0; số thập phân đúng dấu theo ngôn ngữ.

Công cụ: `tools/sp_g11r.py` (ngân hàng mới, hàm `assemble`, `with_d`); `tools/mb_tikz3d.py` (nhãn điểm tránh mọi nét vẽ, kể cả nét không đi qua điểm đó, đường tròn, nhãn khác); `tools/freqtable.py` (thêm `lang='en'|'vi'`, mặc định giữ nguyên).

## Kết quả hiệu chỉnh đợt 2 (13/11/2026) – Lớp 11, Bài 1–5, 8, 15, 16, 19

Mọi bài nay có **15 câu/mức, 15 dạng khác nhau trong mỗi mức**; phần D gồm 8 dạng mới, không lặp dạng của A–C.

| Bài | Trước | Thay đổi chính | Câu có hình/bảng (mỗi mức) |
|---|---|---|---|
| 1. Giá trị lượng giác của góc lượng giác | 7 câu, không có D | Thêm D: góc phần tư của số đo lớn, đọc số đo từ điểm \(M\) trên đường tròn (có hình chiếu), dấu giá trị lượng giác, kim đồng hồ, rút gọn bằng góc liên quan, \(\sin\alpha\cos\alpha\) từ tổng, số điểm biểu diễn, hai điểm đối xứng (có hình) | 2 |
| 2. Công thức lượng giác | 7 câu | Thêm D: công thức cộng với bộ ba Pythagore, \(\tan(a\pm b)\), tích → tổng, tổng → tích, giá trị đúng của 15°/75°/105°/165°, rút gọn bằng công thức nhân đôi, đưa về \(R\sin(x+\varphi)\), bài tượng trên bệ (có hình) | 1 |
| 3. Hàm số lượng giác | 7 câu; A3 trùng dạng C6 | A3 thay bằng nhận biết hàm chẵn/lẻ. Thêm D: khoảng đồng biến, chu kì, nhận dạng hàm, giao điểm hai đồ thị, độ sâu mực nước (đều đọc từ đồ thị), so sánh nhờ tính đơn điệu, vòng quay, phép tịnh tiến đồ thị | 5 |
| 4. Phương trình lượng giác cơ bản | 7 câu | Thêm D: \(\sin/\cos(x+c)=\dots\), tổng nghiệm trên đoạn, \(\tan\) theo độ, điều kiện có nghiệm theo \(m\), nhận dạng phương trình từ điểm trên đường tròn, lò xo, \(\cot\), đọc nghiệm từ đồ thị | 2 |
| 5. Dãy số | 7 câu | Thêm D: công thức từ đồ thị điểm, que diêm (có hình), tổng triệt tiêu, số hạng lớn/nhỏ nhất, đếm số hạng âm, ao cá (truy hồi), tham số để dãy tăng, số nào là số hạng | 2 |
| 8. Mẫu số liệu ghép nhóm | Bảng lẫn hai thứ tiếng; bối cảnh "bóng đèn" 3 lần/mức | Viết lại toàn bộ 15 câu: đếm, nhóm có tần số lớn nhất, giá trị đại diện, đầu mút, tỉ lệ, tần số thiếu, phần trăm, số liệu thô, số nhóm cần, tần số tương đối thiếu, biểu đồ tần số (2 câu), lỗi ghép nhóm, gộp nhóm, so sánh hai lớp. Bảng/biểu đồ đúng ngôn ngữ của mức | 12–13 |
| 15. Giới hạn của dãy số | D lặp 7/8 dạng của A–C | D mới: tổng \(1+2+\dots+n\), tìm tham số, tìm công bội, căn chia đa thức, giới hạn vô cực, đọc từ đồ thị điểm, kẹp \((\sin n)/n\), dãy truy hồi | 1 |
| 16. Giới hạn của hàm số | D lặp 7/8 dạng | D mới: giới hạn một bên từ đồ thị có bước nhảy, từ đồ thị có tiệm cận, \(\sqrt{x^2+ax}-x\), \(x\to-\infty\) với căn, tìm \(a,b\), đa thức tại vô cực, bảng giá trị, \(|x-a|\) | 3 |
| 19. Lôgarit | D lặp 5/8 dạng; đáp số "10000" | D mới: tích \(\log_ab\cdot\log_bc\), dấu của lôgarit, điều kiện xác định, số năm gửi tiết kiệm, dùng bảng lôgarit, \(a^{k\log_ab}\), số chữ số của \(a^n\), độ pH. Câu dB mức 3 đổi thành 20 dB/50 dB (đáp số 1000) | 1 |

Kiểm tra: bộ test "TẤT CẢ ĐẠT"; kiểm tra độc lập `scripts/audit10.py` đọc đề, bảng **và tọa độ trong hình TikZ** rồi tự tính lại: **240/240 câu đúng**; Mức 3 không còn chữ Việt; số thập phân đúng dấu; mọi đáp số trả lời ngắn ≤ 4 kí tự.

Công cụ: `tools/sp_g11r2.py` (ngân hàng đợt 2), `tools/fig2d.py` (hình 2D: đường tròn lượng giác, đồ thị, biểu đồ tần số; mọi nhãn chọn chỗ không bị nét vẽ đi qua).

## Quét lớp 10 và lớp 12 (13/11/2026)

Kết quả quét 27 bài lớp 10 và 19 bài lớp 12 (Mức 1):
- Gần như mọi bài: phần D (tự luyện 8 câu) lặp lại dạng của A–C chỉ đổi số; nhiều bài còn lặp một dạng 2 lần ngay trong D (ví dụ lớp 12 Bài 8 có hai câu cộng vectơ và hai câu tích vô hướng).
- Hầu như không có câu kèm hình/bảng (trừ thống kê lớp 12); các bài hình học (vectơ lớp 10, không gian lớp 12) có 0 hình trong phần luyện tập.
- Lỗi trình bày: số thập phân dấu phẩy trong phần tiếng Anh (lớp 10 Bài 12, lớp 12 Bài 18–19…), bảng tần số lẫn hai thứ tiếng (lớp 12 Bài 9–10), "From Bài …" trong tiếng Anh, chữ Việt trong công thức hiển thị chung.

## Kết quả hiệu chỉnh lớp 12 – đợt 1 (13/11/2026): Bài 5, 6, 7, 8, 11, 12

Phần D mới (8 dạng/bài, khác A–C, `tools/sp_g12r.py`):

| Bài | Dạng mới ở phần D | Câu có hình |
|---|---|---|
| 5. Ứng dụng đạo hàm | cửa sổ nội tiếp nửa hình tròn, lon hình trụ, kéo dây điện qua sông, giá vé tối ưu, nồng độ thuốc, hai con tàu, chuồng chia ô, áp phích có lề | 5/8 |
| 6. Vectơ trong không gian | góc giữa hai vectơ trong hình lập phương, trọng tâm tứ diện/mặt, biểu diễn vectơ trong lăng trụ, độ dài tổng vectơ, công của lực, đẳng thức vectơ trong tứ diện, lực căng xích treo đèn, góc từ tích vô hướng | 6/8 |
| 7. Hệ trục Oxyz | đọc tọa độ đỉnh hình hộp, đối xứng qua mặt phẳng tọa độ, khoảng cách tới trục, \(\overrightarrow{OM}\) theo \(\vec i,\vec j,\vec k\), điểm trên trục cách đều, đường chéo căn phòng, tam giác vuông tại đâu, điểm chia đoạn | 1/8 |
| 8. Biểu thức tọa độ | góc (độ), tích vô hướng trong hình hộp, tìm \(m\) theo độ dài, vectơ ngược hướng, điều kiện góc tù, hệ \(\vec a\pm\vec b\), lực cân bằng, \(\cos\widehat{BAC}\) | 1/8 |
| 11. Nguyên hàm | đọc \(f\) từ đồ thị, lũy thừa căn, \(a^x\), \(\tan^2x\)…, rút gọn trước khi lấy nguyên hàm, chiều cao cây, từ \(f''\) về \(f\), khẳng định đúng | 1/8 |
| 12. Tích phân | tích phân từ đồ thị gấp khúc, nửa hình tròn, hàm lẻ, tìm cận \(m\), \(f(b)=f(a)+\int f'\), hàm cho hai công thức, đồ thị vận tốc, nhiệt độ trung bình | 3/8 |

Sửa chung toàn bộ lớp 10 và 12: dòng "Từ cần nhớ" ở Mức 1 thành từ chạm vào để xem tiếng Anh; "From Bài" → "From Lesson"; số thập phân trong phần tiếng Anh (cả phương án) dùng dấu chấm; bảng tần số mỗi mức chỉ một ngôn ngữ (`tabfix` trong `tools/mb_lib.py`); bỏ chữ Việt/Anh khỏi công thức hiển thị chung.

Kiểm tra: test lớp 10 và 12 "TẤT CẢ ĐẠT"; `scripts/audit11.py` (đọc đề và hình, tự tính lại) 144/144 câu đúng.

Đợt tiếp theo đề xuất: lớp 12 Bài 1–4 (đơn điệu, GTLN–GTNN, tiệm cận, khảo sát: cần đồ thị/bảng biến thiên), Bài 13–19; lớp 10 các bài vectơ (Bài 7–11, thêm hình), Bài 4–6, 16–21.

## Thư viện câu hỏi (13/11/2026)

Theo yêu cầu: câu bị thay ra khi hiệu chỉnh **không bỏ** mà lưu lại làm nguồn cho thư viện câu hỏi (sau này đổi qua lại giữa các câu cùng dạng).
- `tools/question_bank.py` gom mọi câu luyện tập của mọi bài (lớp 9–12) vào `data/question-bank/grade<lớp>/<mã-bài>.json`: câu đang dùng trên trang + câu đã thay ra (lấy lại từ phiên bản cũ trên GitHub, mốc `9dde968`, trước đợt hiệu chỉnh).
- Mỗi câu có: mức, mục (A/B/C/D…), loại (mcq/tf/short), `form` (khung dạng — câu cùng form đổi được cho nhau), đề EN/VI (kèm hình, bảng), phương án, đáp án, lời giải, trạng thái "đang dùng"/"đã thay ra".
- Câu đã vào thư viện không bao giờ bị xóa: chạy lại công cụ sau mỗi đợt hiệu chỉnh, câu mới thay ra tự được giữ.
- Các hàm sinh câu cũ (`sp_g11*.py`, `sp_g12*.py`, ví dụ `M5S`, `M8S12`) vẫn còn nguyên trong mã, có thể sinh thêm biến thể.
- Chạy: `python tools/question_bank.py` (trong kho git của dự án).

## Kết quả hiệu chỉnh lớp 12 – đợt 2 (13/11/2026): Bài 1–4

Phần D mới (`tools/sp_g12r2.py`), nhiều câu đọc đồ thị và bảng biến thiên (vẽ bằng TikZ):

| Bài | Dạng mới ở phần D | Câu có hình/bảng |
|---|---|---|
| 1. Đơn điệu và cực trị | khoảng nghịch biến từ đồ thị \(f'\), cực trị từ đồ thị \(f'\) (có nghiệm kép), giá trị cực đại/điểm cực tiểu từ bảng biến thiên, khoảng đồng biến từ đồ thị \(f\), hàm đồng biến trên \(\mathbb R\), tìm \(m\) để đạt cực trị tại \(x_0\), doanh số tăng khi nào, cực trị hàm mũ/lôgarit | 4/8 |
| 2. GTLN–GTNN | đọc từ đồ thị trên đoạn (mức 3: đáp án tại đầu mút), từ bảng biến thiên, hàm lượng giác, hàm có căn, tìm \(m\) theo GTLN/GTNN, hàm mũ/lôgarit trên đoạn, số khách lễ hội, \(M+m\) | 2/8 |
| 3. Tiệm cận | đọc tiệm cận từ đồ thị, đếm tiệm cận từ bảng biến thiên (cả trường hợp hai tiệm cận ngang), tìm \(m\) để không có tiệm cận đứng, hai tiệm cận ngang của \(\frac{kx+c}{\sqrt{x^2+s}}\), tìm \(a\) theo tiệm cận xiên, chi phí trung bình, diện tích hình chữ nhật tạo bởi tiệm cận và trục, khẳng định đúng | 2/8 |
| 4. Khảo sát hàm số | nhận dạng hàm bậc ba từ đồ thị, nhận dạng hàm phân thức từ đồ thị, dấu của \(a\), \(d\), điều kiện \(f(x)=m\) có 3 nghiệm, số nghiệm \(kf(x)+c=0\), diện tích tam giác ba điểm cực trị hàm trùng phương, nhận dạng hàm từ bảng biến thiên, số giao điểm | 6/8 |

Kiểm tra: test "TẤT CẢ ĐẠT"; `scripts/audit12.py` (đọc đồ thị và bảng biến thiên trong tệp TikZ, tự tính lại) 96/96 câu đúng.
