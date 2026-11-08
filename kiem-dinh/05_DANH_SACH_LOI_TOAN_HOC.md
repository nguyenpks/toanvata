# 05 – DANH SÁCH LỖI TOÁN HỌC

> **Cập nhật 08/11/2026:** M-001, M-003, M-007, M-008, T-001, T-002 đã chuyển sang **Đã sửa · Đã kiểm tra lại** – xem `10_BAO_CAO_SUA_UU_TIEN_1.md`. Kiểm định thủ công Mức 2–3 (08/11) và các lỗi mới phát hiện (M-101…M-108, P-101…P-109): xem ``11_KIEM_DINH_MUC_2_3.md``. Nội dung bên dưới giữ nguyên như lúc kiểm định (07/11/2026).

Phạm vi: lý thuyết, ví dụ và câu luyện tập **Mức 1** của 79 bài đang mở; các lỗi có nguồn gốc ở bộ sinh câu đã được kiểm tra thêm ở Mức 2–3.
Quy ước: "Vị trí" ghi theo số thứ tự câu hiển thị trên trang (Mức 1). Trích dẫn giữ nguyên kí hiệu LaTeX như trong mã.

Tổng: **2 Critical · 4 High · 5 Medium · 14 Low**.

---

## A. CRITICAL

### M-001 · Đáp án sai: phần bù của một khoảng
| Trường | Nội dung |
|---|---|
| Khối lớp | 10 |
| Chương | I. Mệnh đề và tập hợp |
| Bài học | Bài 2. Tập hợp và các phép toán trên tập hợp (`g10-sets-01`) |
| Vị trí | Luyện tập, nhóm F, câu 18 – **cả 3 mức** |
| Nội dung hiện tại | Mức 1: "Tìm phần bù của \([0,2]\) trong \(\mathbb{R}\)." – khóa **b** \((-\infty,0]\cup[2,+\infty)\). Mức 2: phần bù của \((-3,0]\) – khóa **c** \((-\infty,-3)\cup[0,+\infty)\). Mức 3: phần bù của \((-3,1]\) – khóa **d** \((-\infty,-3)\cup[1,+\infty)\) |
| Vấn đề | Khóa đáp án là tập "lấy đầu mút giống khoảng gốc", trong khi phần bù phải **đảo** tính đóng/mở ở mỗi đầu mút. Lời giải hiển thị ("một đầu mút thuộc phần bù đúng khi nó không thuộc khoảng đã cho") mâu thuẫn với chính khóa đáp án. Học sinh làm đúng bị chấm sai. |
| Mức độ | **Critical** |
| Căn cứ | \(0\in[0,2]\Rightarrow 0\notin C_{\mathbb R}[0,2]\). Đúng: \(C_{\mathbb R}[0,2]=(-\infty,0)\cup(2,+\infty)\) (phương án c, Mức 1); \(C_{\mathbb R}(-3,0]=(-\infty,-3]\cup(0,+\infty)\) (phương án a, Mức 2); \(C_{\mathbb R}(-3,1]=(-\infty,-3]\cup(1,+\infty)\) (phương án b, Mức 3). Nguyên nhân: `tools/sp_g10.py` dòng 154–161, hàm `s_comp` tính biến `true=(a, not ac, b, not bc)` nhưng không dùng; phương án đúng (chỉ số 0) lại là `cp(a, ac, b, bc)`. Lệnh `assert` chỉ kiểm tra công thức, không kiểm tra phương án. |
| Đề xuất | Sửa `opts = [cp(*true)] + [cp(a, ac, b, bc), cp(a, not ac, b, bc), cp(a, ac, b, not bc)]`, dựng lại bài, thêm kiểm thử "phương án đúng thỏa mãn định nghĩa" |
| Nội dung sửa | Mức 1: khóa đổi thành **c** \((-\infty,0)\cup(2,+\infty)\); Mức 2: **a**; Mức 3: **b** (thứ tự phương án sẽ thay đổi sau khi dựng lại) |

### M-007 · Câu hỏi không có phương án đúng (nhãn biến cố bị tráo)
| Trường | Nội dung |
|---|---|
| Khối lớp | 11 |
| Chương | VIII. Các quy tắc tính xác suất |
| Bài học | Bài 28. Biến cố hợp, biến cố giao, biến cố độc lập (`g11-prob-01`) |
| Vị trí | Luyện tập, nhóm A, câu 1 – **cả 3 mức** |
| Nội dung hiện tại | Mức 1: "Gieo một con xúc xắc. \(A\): "at least 3", \(B\): "số chấm không nhỏ hơn 3". Biến cố \(A\cap B\) là…" – khóa \(\{4;6\}\). Mức 2: \(A\): "at most 3", \(B\): "số chấm không lớn hơn 3" – khóa \(\{1;3\}\). Mức 3: \(A\): "not 1 or 3", \(B\): "khác 1 và 3" – khóa \(\{2;5\}\) |
| Vấn đề | Theo đề hiển thị, \(A\) và \(B\) là cùng một biến cố nên \(A\cap B=B\) (ví dụ Mức 1: \(\{3;4;5;6\}\)) – **không có trong 4 phương án**. Nhãn của \(A\) là tiếng Anh của \(B\) (lọt tiếng Anh vào Mức 1). |
| Mức độ | **Critical** |
| Căn cứ | Mã `content/grade11/union-intersection-independence.py` dòng 83 giải nén `(A, B, ae, av, be, bv) = P['sets']`, trong khi dữ liệu dòng 106, 109… xếp theo thứ tự `(ae, be, av, bv)` ('even number', 'at least 3', 'số chấm chẵn', 'số chấm không nhỏ hơn 3'). |
| Đề xuất | Sửa dòng 83 thành `(A, B, ae, be, av, bv) = P['sets']`, dựng lại |
| Nội dung sửa | Mức 1: "\(A\): "số chấm chẵn", \(B\): "số chấm không nhỏ hơn 3". Biến cố \(A\cap B\) là…" – đáp án \(\{4;6\}\) (giữ khóa) |

---

## B. HIGH

### M-002 · Thiếu điều kiện "miền nghiệm là đa giác"
| Trường | Nội dung |
|---|---|
| Khối / Chương / Bài | 10 · II. BPT và hệ BPT bậc nhất hai ẩn · Bài 3 (`g10-ineq2-01`) |
| Vị trí | Ví dụ 5 (phần Phân tích) và mục Tổng kết, ý 4 |
| Nội dung hiện tại | "Biểu thức bậc nhất đạt giá trị lớn nhất tại một đỉnh của miền." / "Biểu thức bậc nhất đạt giá trị lớn nhất, nhỏ nhất tại đỉnh của miền." |
| Vấn đề | Phát biểu tổng quát sai khi miền không bị chặn (vd. miền \(x\ge0,y\ge0\), \(F=x+y\) không có GTLN). Bài 4 (`g10-ineq-sys-01`) đã nêu đúng điều kiện nhưng Bài 3 thì không. |
| Mức độ | **High** (thiếu điều kiện áp dụng định lí) |
| Căn cứ | SGK KNTT 10, Bài 4: GTLN/GTNN của \(F=ax+by\) trên **miền đa giác** đạt tại một đỉnh |
| Nội dung sửa | "Nếu miền nghiệm là một **đa giác** (miền bị chặn) thì biểu thức \(F=ax+by\) đạt giá trị lớn nhất và nhỏ nhất tại các đỉnh của đa giác đó." |

### M-003 · Câu trắc nghiệm có hai phương án đúng
| Trường | Nội dung |
|---|---|
| Khối / Chương / Bài | 10 · VI. Hàm số, đồ thị và ứng dụng · Bài 16. Hàm số bậc hai (`g10-func-02`) |
| Vị trí | Luyện tập Mức 1, nhóm D, câu 9 |
| Nội dung hiện tại | "Hàm số \(y=3x^2+12x+12\)…" khóa **b** "nghịch biến trên \((-\infty;-2)\), đồng biến trên \((-2;+\infty)\)"; phương án **c** "đồng biến trên \((2;+\infty)\)" |
| Vấn đề | Phương án c cũng đúng vì \((2;+\infty)\subset(-2;+\infty)\). Học sinh chọn c bị chấm sai. (Mức 2, 3 của cùng họ câu đã kiểm tra: không mắc lỗi này – lỗi xuất hiện do số ngẫu nhiên.) |
| Mức độ | **High** |
| Nội dung sửa | Thay c bằng "đồng biến trên \((-\infty;-2)\)"; bổ sung ràng buộc trong bộ sinh câu: các phương án nhiễu về khoảng đơn điệu không được là tập con của khoảng đúng |

### M-004 · Lập luận về chu kì không hợp lệ
| Trường | Nội dung |
|---|---|
| Khối / Chương / Bài | 11 · I. Hàm số lượng giác và PT lượng giác · Bài 3. Hàm số lượng giác (`g11-trigf-02`) |
| Vị trí | Ví dụ 4 "Chu kì của một tổng" |
| Nội dung hiện tại | "Chu kì chung phải là bội của cả hai. Các bội chung của \(\pi\) và \(\dfrac{2\pi}{3}\) là \(2\pi,4\pi,\dots\); nhỏ nhất là \(2\pi\)… Ứng viên nhỏ hơn không đúng: với \(T=\pi\)… Đáp số: The period is \(2\pi\)." |
| Vấn đề | (1) Khẳng định "chu kì của tổng phải là bội chung của các chu kì" là sai trong trường hợp tổng quát (phản ví dụ: \(\sin x+(-\sin x)=0\) có mọi số dương là chu kì). (2) Chỉ loại \(T=\pi\) không đủ loại mọi \(T\in(0;2\pi)\). Kết luận đúng nhưng **phương pháp chứng minh sai** – dạy học sinh một quy tắc không đúng. |
| Mức độ | **High** (sai phương pháp) |
| Căn cứ | Chứng minh chặt cần tính độc lập tuyến tính của \(\sin 2x,\cos 3x\) – vượt chương trình; SGK chỉ yêu cầu nhận biết hàm tuần hoàn |
| Nội dung sửa | Đổi đề: "Chứng tỏ \(f(x+2\pi)=f(x)\) với mọi \(x\), tức \(y=\sin2x+\cos3x\) là hàm số tuần hoàn." Bỏ câu "chu kì chung phải là bội của cả hai"; nếu giữ khẳng định "chu kì là \(2\pi\)", ghi rõ "(chứng minh \(2\pi\) là số dương nhỏ nhất nằm ngoài chương trình)". Đáp số viết tiếng Việt. |

### M-008 · Mất dấu phẩy trên làm sai bản chất câu hỏi (quy tắc hình hộp)
| Trường | Nội dung |
|---|---|
| Khối / Chương / Bài | 12 · II. Vectơ và hệ trục tọa độ trong không gian · Bài 6 (`g12-vec-01`) |
| Vị trí | Luyện tập nhóm A, câu 1 – **cả 3 mức** |
| Nội dung hiện tại | "Trong hình lập phương, \(\overrightarrow{AB}+\overrightarrow{AD}+\overrightarrow{AA}=\)…" – khóa \(\overrightarrow{AC}\); lời giải "Quy tắc hình hộp." (Mức 2/3: \(\overrightarrow{CB}+\overrightarrow{CD}+\overrightarrow{CC}\)…) |
| Vấn đề | \(\overrightarrow{AA}=\vec0\) nên đề hiển thị chỉ kiểm tra quy tắc hình bình hành; lời giải "quy tắc hình hộp" sai; học sinh biết quy tắc hình hộp sẽ tìm \(\overrightarrow{AC'}\) và không thấy. |
| Mức độ | **High** |
| Căn cứ | `content/grade12/vectors-in-space.py` dòng 65–66: hàm `nm` chỉ lấy 2 kí tự đầu của chuỗi `"AA'"`, `"AC'"`, làm rơi dấu ′ |
| Nội dung sửa | "\(\overrightarrow{AB}+\overrightarrow{AD}+\overrightarrow{AA'}=\)…" – đáp án \(\overrightarrow{AC'}\) |

---

## C. MEDIUM

| Mã | Lớp · Bài | Vị trí | Nội dung hiện tại | Vấn đề | Nội dung sửa |
|---|---|---|---|---|---|
| M-006 | 11 · Bài 25 (`g11-perp-04`) | Mức 1, câu 11, lời giải | "…một mặt chứa một đường thẳng vuông góc với mặt kia (ví dụ \(SA\), \(BC\), \(CD\), \(BD\))" | \(BC,CD,BD\) nằm trong \((ABCD)\), không vuông góc với \((ABCD)\): lời giải chứa khẳng định sai (đáp án d vẫn đúng) | "Đáp án d. \((SAD)\) chứa \(SA\perp(ABCD)\) nên \((SAD)\perp(ABCD)\)." |
| M-009 | 10 · Bài 9 (`g10-vec-03`) | Lý thuyết 5.3, Tổng kết | "\(A,B,C\) thẳng hàng \(\iff\overrightarrow{AB}=k\overrightarrow{AC}\) với số \(k\) nào đó" | Thiếu điều kiện \(A\ne C\) (ba điểm phân biệt); khi \(A\equiv C\) mệnh đề "⇐" vẫn đúng nhưng "⇒" thì sai với \(B\ne A\) | "Ba điểm **phân biệt** \(A,B,C\) thẳng hàng \(\iff\) có số \(k\ne0\) để \(\overrightarrow{AB}=k\overrightarrow{AC}\)." |
| M-010 | 12 · Bài 15 (`g12-coord-04`) | Mức 1, câu 14, lời giải | "\([\vec u_1,\vec u_2]=(0;0;0)\), \([\vec u_1,\vec u_2]\cdot\overrightarrow{M_1M_2}=0\)" → "song song" | Điều kiện nêu ra cũng đúng khi hai đường **trùng nhau**; lời giải không phân biệt được (bảng lý thuyết dùng đúng \([\vec u_1,\overrightarrow{M_1M_2}]\ne\vec0\)) | "…\([\vec u_1,\vec u_2]=\vec0\) và \(M_2(2;0;3)\notin d_1\) (hay \([\vec u_1,\overrightarrow{M_1M_2}]\ne\vec0\)) nên song song." |
| M-011 | 10 · Bài 4 (`g10-ineq-sys-01`) | Ví dụ 5 | Tìm GTNN của \(F=4x+5y\) trên miền **không bị chặn** chỉ bằng so sánh 3 đỉnh | Ngay mục 5.3 vừa cảnh báo miền không bị chặn có thể không có GTNN, nhưng ví dụ không giải thích vì sao ở đây GTNN tồn tại | Thêm: "Vì \(x,y\ge0\) và hệ số của \(F\) dương nên \(F\) tăng khi đi xa gốc; GTNN đạt tại một đỉnh của miền." |
| M-012 | 11 · Bài 31 (`g11-deriv-01`) | Hình minh họa 5.3 | "y = \|x\| có **góc nhọn** tại 0" | Đồ thị \(y=|x|\) tạo **góc vuông** tại O; "góc nhọn" là thuật ngữ sai (ý là "điểm gãy") | "Đồ thị \(y=|x|\) bị **gãy** tại O…" |

---

## D. LOW

| Mã | Lớp · Bài | Vị trí | Vấn đề | Đề xuất |
|---|---|---|---|---|
| M-L01 | 10 · Bài 5 (`g10-trig-01`) | 5.3 | \(\tan\alpha\cdot\cot\alpha=1\) và \(\sin(90^\circ-\alpha)=\cos\alpha\) nêu không kèm điều kiện | Thêm "\((\alpha\ne0^\circ,90^\circ,180^\circ)\)", "\((0^\circ\le\alpha\le90^\circ)\)" |
| M-L02 | 11 · Bài 1 (`g11-trigf-01`) | 5.4 | \(\tan\alpha\cdot\cot\alpha=1\) không kèm điều kiện | Thêm "\((\sin\alpha\cos\alpha\ne0)\)" |
| M-L03 | 10 · Bài 7 (`g10-vec-01`) | 5.1 | "Vectơ-không … cùng hướng với mọi vectơ" nêu như tính chất | Ghi "**Quy ước**: vectơ-không cùng phương, cùng hướng với mọi vectơ" |
| M-L04 | 10 · Bài 11 (`g10-vec-05`) | 5.2 "Dấu của tích vô hướng" | "\(\vec a\cdot\vec b>0\): góc nhọn" – thực ra góc thuộc \([0^\circ;90^\circ)\), có thể bằng \(0^\circ\) | "góc nhọn hoặc bằng \(0^\circ\)" |
| M-L05 | 10 · Bài 20 (`g10-coord-02`) | 5.1 | "\(k_1k_2=-1\)" không nêu điều kiện hai đường có hệ số góc | Thêm "(khi cả hai đường thẳng đều có hệ số góc)" |
| M-L06 | 12 · Bài 11 (`g12-int-01`) | Bảng nguyên hàm | \(\int x^\alpha dx\) không nêu miền (\(x>0\) khi \(\alpha\) không nguyên) | Thêm chú thích miền |
| M-L07 | 11 · Bài 19 (`g11-exp-04`) | Từ vựng, 5.1 | Dùng số \(e\approx2{,}718\) mà không định nghĩa | Thêm \(e=\lim\left(1+\frac1n\right)^n\) |
| M-L08 | 12 · Bài 3 (`g12-deriv-app-01`) | Lỗi thường gặp | Dẫn ví dụ \(y=\arctan x\) – ngoài chương trình THPT | Thay bằng \(y=\dfrac{3x}{\sqrt{x^2+1}}\) (đã có ở câu 16) |
| M-L09 | 10 · Bài 15 (`g10-func-01`) | Mức 1 câu 13, câu 1 (lời giải) | Lời giải chèn ý không liên quan ("\(x^2\ge0\)", "mẫu khác 0") | Viết lời giải riêng cho từng câu |
| M-L10 | 10 · Bài 3, 4, 10, 11; 11 · Bài 31 | Nhiều lời giải | Viết "\(-2\cdot-2\)", "\(2\cdot6--4\cdot-3\)", "\(1+-5\)" thiếu ngoặc số âm | Viết \((-2)\cdot(-2)\)… |
| M-L11 | 10 · Bài 1 (`g10-logic-01`) | Ví dụ 2 | "\(\sqrt2>1.4\)" dùng dấu chấm thập phân | "\(1{,}4\)" |
| M-L12 | 11 · Bài 18, 19 | Mức 1 câu 10, 15; Q3, Q11 | Câu sinh máy suy biến: "\(4^{1}=\)…", "\(\sqrt[4]{x^{1}}\)", phương án "\(2+1a\)", "\(1\cdot2a\)" | Lọc tham số tầm thường trong bộ sinh câu |
| M-L13 | 11 · Bài 30 | Mức 1 câu 4 | Lời giải "Công thức nhân chỉ đúng cho biến cố độc lập" không trả lời câu hỏi | Ghi phép tính \(0{,}5\cdot0{,}4=0{,}2\) |
| M-L14 | 12 · Bài 16, 17 (và nhiều bài) | Lời giải "Kiểm tra … có bằng 0 không" | Lời giải lặp ý, không đưa phép tính | Ghi phép tính cụ thể |

---

## E. Nội dung đã kiểm tra và xác nhận ĐÚNG (trích)

Không phát hiện sai ở: các định nghĩa mệnh đề, tập hợp, khoảng; bảng giá trị lượng giác \(0^\circ\)–\(180^\circ\); định lí côsin, sin, Heron, \(S=pr=\frac{abc}{4R}\); toàn bộ công thức vectơ phẳng/không gian, tích vô hướng, tích có hướng; phương trình đường thẳng, đường tròn, ba đường conic (tiêu điểm, \(b^2=a^2\mp c^2\)); quy tắc đếm, \(P_n,A_n^k,C_n^k\), nhị thức Newton; công thức cộng/nhân đôi/hạ bậc/biến đổi tích–tổng; họ nghiệm 4 PT lượng giác cơ bản; CSC, CSN, tổng CSN lùi vô hạn; giới hạn dãy, hàm, liên tục, định lí giá trị trung gian; lũy thừa, lôgarit, hàm mũ–lôgarit, PT/BPT mũ–lôgarit; quan hệ song song, vuông góc, khoảng cách, thể tích (kể cả chóp cụt); xác suất cổ điển, công thức cộng, nhân; đạo hàm (định nghĩa, bảng, quy tắc, cấp hai); đơn điệu, cực trị (2 điều kiện đủ), GTLN–GTNN, tiệm cận, khảo sát; nguyên hàm, tích phân, diện tích, thể tích; phương trình mặt phẳng, đường thẳng, mặt cầu, công thức góc; số trung bình, trung vị, mốt, tứ phân vị, phương sai (không ghép nhóm và ghép nhóm); xác suất có điều kiện, toàn phần, Bayes.
Tỉ lệ câu Mức 1 có lỗi toán học (khóa sai / không có đáp án đúng / hai đáp án đúng / đề sai bản chất): **4/1.199 ≈ 0,33 %**. Tuy nhiên 3 trong 4 lỗi là lỗi hệ thống, lặp lại ở mọi mức.
