# 11 – KIỂM ĐỊNH THỦ CÔNG MỨC 2 VÀ MỨC 3 (Ưu tiên 1 – mục 7)

Ngày: 08/11/2026 · Dữ liệu: bản dựng sau khi sửa Ưu tiên 1 (xem `10_BAO_CAO_SUA_UU_TIEN_1.md`).

## 1. Phạm vi và cách làm

- **2.398/2.398 câu** luyện tập của Mức 2 và Mức 3 ở 79 bài đang mở (lớp 10: 832 = 2×416; lớp 11: 910 = 2×455; lớp 12: 656 = 2×328). Số câu khớp với số liệu trong `01_TONG_QUAN_KIEM_DINH.md`.
- Văn bản tiếng Việt, các phương án, khóa đáp án và lời giải được trích tự động từ HTML đã dựng. Mỗi câu được **giải lại độc lập bằng tay**, không dùng khóa của website và không dùng mô hình AI khác để xác nhận.
- Các câu hình học không gian (góc, khoảng cách, vectơ trong hình lập phương; mặt phẳng song song) được kiểm tra thêm bằng **tọa độ**. Các câu thống kê ghép nhóm được tính lại \(\bar x\), \(M_e\), \(M_o\), \(Q_1\), \(Q_3\), \(s^2\) theo công thức SGK KNTT. Các câu phương trình được thế nghiệm ngược lại.
- Lỗi tìm thấy đều được **truy ngược tới tệp nguồn** để biết là lỗi đơn lẻ hay lỗi của bộ sinh câu.
- **Không sửa nội dung** trong bước này (chờ chủ website đồng ý).

## 2. Kết quả tổng hợp

| | Lớp 10 | Lớp 11 | Lớp 12 | Cộng |
|---|---|---|---|---|
| Số câu đã giải | 832 | 910 | 656 | **2.398** |
| Khóa đáp án sai | 0 | 0 | 1 | **1** (M-108) |
| Câu có hơn một phương án đúng | 2 + nhóm "cận trên" | 0 | 1 | M-101, M-102, M-107 |
| Lời giải sai kiến thức / ngược nghĩa (khóa vẫn đúng) | 0 | 2 | 1 | M-104, M-105, M-106 |
| Các câu còn lại | đúng | đúng | đúng | |

Các lỗi đã sửa ở Ưu tiên 1 (M-001, M-003, M-007, M-008, T-001, T-002) được xác nhận **đúng ở cả Mức 2 và Mức 3**.

## 3. Lỗi toán học mới (bổ sung vào 05)

| Mã | Mức độ | Vị trí | Nội dung hiện tại | Vấn đề | Đề xuất sửa |
|---|---|---|---|---|---|
| **M-108** | **Critical** | 12 · B1 (`g12-mono-01`) Mức 3, tự luyện câu 25 (item 53) | "Cho \(f'(x)=(x+3)(x+1)\). Hàm số \(f\) đồng biến ở đâu?" – khóa a: \((-\infty,-3)\cup(-1,+\infty)\) | **Khóa sai.** \(f\) không đồng biến trên hợp hai khoảng: với \(f=\frac{x^3}{3}+2x^2+3x\) thì \(f(-3{,}5)\approx-0{,}29>f(-0{,}9)\approx-1{,}32\). SGK không cho viết "đồng biến trên \(K_1\cup K_2\)". Hai phương án b \((-1,+\infty)\) và c \((-\infty,-3)\) đều đúng. | Nguồn `tools/sp_g12.py`, hàm `m1_sign` (dòng 55–63): khi `neg=False` khóa luôn là phương án hợp. Sửa: khóa là một khoảng đơn (vd \((b;+\infty)\)), hoặc phương án "đồng biến trên mỗi khoảng \((-\infty;a)\) và \((b;+\infty)\)", và loại các nhiễu là khoảng con của khoảng đồng biến. Mức 1, Mức 2 hiện rơi vào `neg=True` nên đúng, nhưng lỗi sẽ xuất hiện với mọi tham số `neg=False`. |
| **M-101** | **High** | 10 · B12 (`g10-stats-01`), câu "Biết \(a\lt\sqrt n\lt b\), lấy \(\sqrt n\approx\ldots\) thì sai số tuyệt đối nhỏ hơn…" – **Mức 1 câu 14**, Mức 2 câu 21, Mức 3 câu 29 | Nhiễu cố định \(0{,}1\), \(0{,}005\) | Nhiễu \(0{,}1\) **luôn là một cận đúng**, nên mọi câu sinh ra đều có ≥ 2 phương án đúng. Ở Mức 2 (\(\sqrt2\approx1{,}41\), sai số thật \(0{,}0042\)) thì cả \(0{,}005\) cũng đúng (3 phương án đúng), và khóa \(0{,}01\) không còn là cận chặt nhất. **Lần kiểm định 07/11 đã bỏ sót câu này ở Mức 1.** | Nguồn `tools/sp_g10d.py`, hàm `e_sqrt` (dòng 195–200). Hỏi "ước lượng tốt nhất có thể suy ra từ \(a\lt\sqrt n\lt b\)" và chỉ dùng nhiễu nhỏ hơn khóa nhưng thật sự sai (vd \(0{,}001\)), hoặc đổi sang dạng trả lời ngắn. |
| **M-107** | **High** | 12 · B1 Mức 3 câu 1 (item 29) | "\(f(x)=-x^2-4x\) đồng biến trên khoảng nào?" a \((-2;+\infty)\), b \((-\infty;-4)\), c \((-4;0)\), d \((-\infty;-2)\) – khóa d | b \((-\infty;-4)\subset(-\infty;-2)\) nên **cũng đúng** (cùng dạng M-003) | `content/grade12/monotonicity-extrema.py` dòng 156: thay b bằng \((-4;+\infty)\) hoặc \((-3;-1)\) |
| **M-102** | Medium | 10 · B12: câu "Sai số tuyệt đối/tương đối **không vượt quá**…" (Mức 2 câu 17, 20; Mức 3 câu 25, 28) | Nhiễu gồm cả số lớn hơn khóa (vd \(0{,}1\); \(0{,}5\) khi khóa \(0{,}05\)) | Mọi số lớn hơn cận trên cũng là cận trên, nên về logic có nhiều phương án đúng | Hỏi "độ chính xác (cận trên nhỏ nhất)…" hoặc chỉ dùng nhiễu nhỏ hơn khóa. Nguồn `sp_g10d.py` `e_round_err` và câu sai số tương đối |
| **M-104** | Medium | 11 · B6 (`g11-sequences-02`) Mức 2 câu 4 | Lời giải: "Các hiệu là \(2,4,8\): **không đổi**." | Dịch ngược nghĩa ("not constant"). Lời giải khẳng định điều trái với kết luận | `content/grade11/arithmetic-progressions.py` dòng 52 (`tf4`): "…: không phải hằng số." |
| **M-105** | Medium | 12 · B7 (`g12-coord-01`) Mức 2 câu 5, Mức 3 câu 12 | "Điểm thuộc \((Oyz)\) có **tọa độ thứ ba** bằng 0", "Điểm thuộc \((Oxz)\) có tọa độ thứ ba bằng 0" | Sai kiến thức: thuộc \((Oyz)\) khi \(x=0\), thuộc \((Oxz)\) khi \(y=0\). Câu viết cứng, chỉ đúng với \((Oxy)\) ở Mức 1 | `content/grade12/coordinate-system-oxyz.py` dòng 69: sinh lời giải theo mặt phẳng |
| **M-106** | Medium | 11 · B10 (`g11-space-04`) Mức 2 câu 5 | Mệnh đề **sai** "Hai mặt phẳng phân biệt có một điểm chung thì chỉ có đúng một điểm chung"; lời giải: "Đây là một trong các tiên đề cơ bản." | Lời giải gợi ý mệnh đề đúng, mâu thuẫn với khóa "Sai" | `content/grade11/lines-planes-basics.py` dòng 61–62: viết lời giải riêng cho từng mệnh đề ("…thì có chung cả một đường thẳng") |
| M-103 | Low | 11 · B2 (`g11-trigf-03`) Mức 3 câu 12 | Phản ví dụ cho "\(\tan(a+b)=\tan a+\tan b\) mỗi khi hai vế xác định": \(a=b=\frac\pi4\) | Tại \(a=b=\frac\pi4\) vế trái \(\tan\frac\pi2\) không xác định, tức là vi phạm chính giả thiết | Dùng \(a=b=\frac\pi6\): \(\sqrt3\ne\frac{2}{\sqrt3}\) |

**Bổ sung vị trí cho lỗi Low đã có trong 05:**
- M-L08: thêm 12 · B3 Mức 3 câu 16.
- M-L09: thêm 10 · B15 Mức 2 câu 20 và Mức 3 câu 28 ("\(x^2\ge0\), \(\sqrt x\ge0\)" dùng chung).
- M-L10: thêm 11 · B7 Mức 3 câu 10 ("\(\frac{-2^{6}-1}{-2-1}\)", lẽ ra \((-2)^6\)), 12 · B17 Mức 3 câu 41 ("\(I--1\vec n\)").
- M-L11: thêm 10 · B27 Mức 2 câu 22 ("16.7") và 11 · B4 Mức 3 câu 9 ("-0.99", "1.01").
- M-L12: thêm 11 · B18 Mức 2 câu 21 ("\((\frac13)^1=\)"; lời giải nói về \(a^{-n}\)).
- M-L13/M-L14: lời giải Đ/S chung không khớp câu hỏi ở 11 · B10, B11, B22–B26, B29, B33; 12 · B11.

## 4. Lỗi sư phạm/ngôn ngữ mới (bổ sung vào 06, đều Low)

| Mã | Vị trí | Vấn đề | Đề xuất |
|---|---|---|---|
| P-101 | 10 · B5 Mức 2 câu 20, Mức 3 câu 28 | Đáp án để dạng chưa rút gọn \(\frac{12\sqrt2}{2}\), \(\frac{6\sqrt2}{2}\) | \(6\sqrt2\), \(3\sqrt2\) |
| P-102 | 10 · B9 tự luyện (Mức 2 câu 15, 17, 21; Mức 3 câu 23, 25, 29) | Lời giải dùng tên điểm mẫu \(A,B,C,I\) khác tên trong đề (đề "\(\overrightarrow{NB}=4\overrightarrow{NP}\)", lời giải "Từ \(\overrightarrow{AB}=4\overrightarrow{AC}\)…"); "\(\frac1{-2}\)" chưa rút gọn | Thay bằng tên điểm của đề |
| P-103 | 11 · B9 Mức 3 câu 28 | "tổng lượng điện **cả** các hộ" | "của các hộ" |
| P-104 | 11 · B12 tự luyện | "Trong ABCD, M, N…" thiếu "tứ diện"; "Trong một tứ diện, điểm \(M\in SA\)" không đặt tên tứ diện | Ghi rõ "tứ diện \(SABC\)"… |
| P-105 | 11 · B28 Mức 2 câu 5 | "Biến cố 'cả hai cùng bắn trúng' là \(A\cup B\)" nhưng \(A,B\) không được định nghĩa trong đề | Thêm "\(A\), \(B\): xạ thủ 1, 2 bắn trúng" |
| P-106 | 12 · B9 Mức 2 câu 21, Mức 3 câu 8, 29 | Nhiễu "Hiệu hai **mốt** đầu mút…" | "mốc" |
| P-107 | 12 · B10 Mức 3 câu 26 | "năng suất 500 tạ/ha" phi thực tế (lúa khoảng 50–70 tạ/ha) | Dùng số liệu thực tế |
| P-108 | 12 · B11 Mức 2 câu 2 | Đề tiếng Việt mở đầu bằng tiếng Anh "On \((0;+\infty)\): …" | "Trên \((0;+\infty)\): …" |
| P-109 | 12 · B15 Mức 2 câu 21 | Lời giải kết luận "song song" chỉ từ \([\vec u_1,\vec u_2]=\vec0\), không kiểm tra điểm để loại trường hợp trùng nhau | Thêm "và \(M_2\notin d_1\)" |

Ngoài ra, các nhóm lỗi đã ghi ở Mức 1 vẫn còn ở Mức 2–3 và chưa sửa: T-003 (`{,}`, `\lt b\gt…\lt /b\gt`, `\dfrac` hiện thô), P-03 (phương án tiếng Anh/in nghiêng như `\(increasing\)`, `\text{decreases on each interval}`, `\text{depends on the edge}`), T-011 (\(f‴\)) và P-L08 (định dạng sinh máy "1x", "2+1a", "x+0").

## 5. Đã sửa (08/11/2026, theo yêu cầu "Sửa 3 lỗi chặn")

| Mã | Sửa ở | Cách sửa | Kiểm tra lại |
|---|---|---|---|
| M-108 | `tools/sp_g12.py` `m1_sign` | Mỗi phương án là một khoảng đơn. Khi \(f'>0\) ngoài hai nghiệm, khóa là \((b;+\infty)\) và nhiễu là \((a;b)\), \((-\infty;b)\), \((a;+\infty)\). Lời giải nói rõ "đồng biến trên mỗi khoảng, không viết trên hợp". Có `assert` kiểm tra bằng số để chỉ đúng một phương án nằm trọn trong miền \(f'>0\). Câu hỏi đổi thành "đồng biến trên khoảng nào?". | Mức 1, 2, 3: mỗi câu có đúng 1 phương án đúng ✔ (Mức 3: \(f'=(x+3)(x+1)\), khóa \((-1;+\infty)\)) |
| M-101 | `tools/sp_g10d.py` `e_sqrt` (+ hàm `_sqrt_opts`) | Nhiễu \(0{,}001;\ 0{,}0005;\ 0{,}0001\) đều nhỏ hơn sai số thật \(|\sqrt n-a|\) (luôn > 0,002), nên đều sai. Có `assert` kiểm tra. | Mức 1 (sai số 0,0058), Mức 2 (0,0042), Mức 3 (0,0079): chỉ \(0{,}01\) đúng ✔ |
| M-107 | `content/grade12/monotonicity-extrema.py` dòng 156 | Phương án b \((-\infty;-4)\) đổi thành \((-3;-1)\) | Chỉ d \((-\infty;-2)\) đúng ✔ |

Sau khi dựng lại và chuẩn hóa LF, chỉ có 2 trang thay đổi so với bản trước (`approximate-numbers-errors.html`, `monotonicity-of-functions.html`). Số câu không đổi (2.595 trắc nghiệm, 486 đúng/sai; 2.398 câu ở Mức 2–3). Quét tĩnh: 0 lồng delimiter, 0 lệnh dính chữ, 0 khóa ngoài phương án, 0 phương án trùng. `build_all.py --check` hợp lệ. `test-lessons-g11.py 10`, `test-lessons-g11.py 12` và `test-mathjax.py` đều đạt.

**Chưa sửa:** M-102, M-103, M-104, M-105, M-106 và các lỗi Low P-101…P-109.

## 6. Ảnh hưởng tới kết luận

- Mức 2 và Mức 3 **không còn ở trạng thái "chưa kiểm định"**. Toàn bộ 3.597 câu (cả 3 mức) đã được giải lại thủ công.
- Phát hiện **thêm 1 lỗi Critical (M-108) và 2 lỗi High (M-101, M-107)**, và cả ba **đã được sửa, kiểm tra lại ngày 08/11** (mục 5). Website vẫn chưa được xếp "đạt chuẩn" vì còn M-002 (High), các lỗi Ưu tiên 2 và phần thiếu nội dung C-01…C-04.
- Điểm tổng 74,5/100 trong `01` được chấm ngày 07/11, trước khi sửa Ưu tiên 1 và trước khi có kết quả Mức 2–3. **Điểm chưa được chấm lại.**
