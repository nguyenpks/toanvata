# DÀN Ý KHỐI LỚP 9 – Website "Toán và Tiếng Anh"

> **Trạng thái: ĐÃ DUYỆT (12/11/2026).** Soạn lần lượt theo thứ tự bài, mỗi lần 4 bài. Đã soạn: Bài 1–8.
> Tài liệu chuyên ngành: *Tài liệu hướng dẫn triển khai dạy học cấp THCS bằng tiếng Anh – Môn Toán – Khối 9* (Bộ GD&ĐT, Hà Nội 2026), gọi tắt **TLTA**. Số trang ghi theo mục lục TLTA.
> Sách giáo khoa: **Toán 9 – Kết nối tri thức với cuộc sống (KNTT)**. Thứ tự 32 bài, 10 chương của TLTA trùng khớp hoàn toàn với KNTT (xem điểm cần quyết định Q1).


## Quyết định của giáo viên (12/11/2026)

| # | Quyết định |
|---|---|
| Q1 | Bộ sách **Kết nối tri thức với cuộc sống**. |
| Q2 | Cặp số, tọa độ, khoảng dùng dấu **chấm phẩy** ở cả 3 mức: `(2; 0)`, `[a; b)`. |
| Q3 | Chính tả tiếng Anh **Anh–Mỹ** (center, meter, favorable, factorize, rationalize…). |
| Q4 | Bài 12 dùng thuật ngữ **góc nâng, góc hạ** (angle of elevation, angle of depression). |
| Q5 | *sphere* → hình cầu; *surface of a sphere* → mặt cầu; *solid sphere / ball* → hình cầu (khối). |
| Q6 | Bài 26: **giữ** biến cố đối \(P(\overline{A})=1-P(A)\) (đặt ở mục mở rộng, có thể dùng ở câu mức Vận dụng). |
| Q7 | Dùng *in one variable* thay cho *in one unknown*. |
| Q8 | Bài 6: **đưa vào** biểu diễn tập nghiệm trên trục số. |
| Q9 | Bài 9: giữ công thức khối lượng tương đối tính, **có giải thích ngắn**. |
| Q10 | Soạn từ Bài 1, lần lượt theo thứ tự, **4 bài mỗi lần**. |

## 0. Quy ước chung

- Mã bài `g9-<chủ-đề>-<số>`; tệp `content/grade9/<mã-bài>.py`, tạo bằng `python tools/new_lesson.py`.
- Cấu trúc mỗi phần trong TLTA: *1. Key Vocabulary – 2. Useful Mathematical Expressions – 3. Worked Examples – 4. Worksheet*. Khai thác: mục 1 → **Từ vựng Toán học**; mục 2 → **Cụm từ tiếng Anh thường gặp**; mục 3–4 → dạng bài, tình huống thực tế (đổi số liệu, không chép nguyên).
- Ngoài phần 1, TLTA còn có: **Part 2** – giáo án mẫu Bài 11, Bài 15; **Part 3** – đoạn giáo án *phương pháp thế* (Ch.1) và *bất phương trình bậc nhất hai ẩn* (thuộc lớp 10, không dùng); **Part 4** – 6 dự án nhỏ (Ch. 1, 4, 5, 8, 9, 10) → dùng làm tình huống cho mức **Vận dụng**.
- Kiến thức nền ghi theo tên bài SGK lớp 8/9. Website hiện **chưa có bài lớp 6–8**, nên mục "Cần biết trước" chỉ ghi tên, chưa liên kết được.
- Viết tắt 4 mức độ: **NB** = Nhận biết, **TH** = Thông hiểu, **VT** = Vận dụng thấp, **V** = Vận dụng.

---

## CHƯƠNG I. PHƯƠNG TRÌNH VÀ HỆ HAI PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN
*Linear Equations and Systems of Linear Equations in Two Variables* · TLTA tr. 5–13 (có đáp án tr. 12)

### Bài 1. Khái niệm phương trình và hệ hai phương trình bậc nhất hai ẩn — `g9-systems-01`
*Linear Equations and Systems of Linear Equations in Two Variables*
- **NB:** nhận biết phương trình bậc nhất hai ẩn $ax+by=c$ (a, b không đồng thời bằng 0), hệ hai phương trình bậc nhất hai ẩn; chỉ ra hệ số a, b, c.
- **TH:** kiểm tra một cặp số có là nghiệm của phương trình/hệ; viết nghiệm tổng quát; biết tập nghiệm biểu diễn bởi một đường thẳng.
- **VT:** tìm m để cặp số cho trước là nghiệm; vẽ đường thẳng biểu diễn tập nghiệm trên mặt phẳng tọa độ.
- **V:** lập hệ phương trình mô tả tình huống thực tế (chu vi mảnh vườn, mua vé hai loại).
- **TLTA:** Lesson 1, tr. 6–7 (vocab, expressions, Example 1–2, Exercise 1–4).
- **Thuật ngữ:** linear equation in two variables, coefficient, ordered pair, solution, general solution, geometric representation, line, system of two linear equations in two variables.
- **Cần biết trước:** phương trình bậc nhất một ẩn (lớp 8); mặt phẳng tọa độ, đồ thị hàm số bậc nhất $y=ax+b$ (lớp 8).
- **Hình/bảng:** đồ thị tương tác — đường thẳng $ax+by=c$, rê điểm để kiểm tra nghiệm.

### Bài 2. Giải hệ hai phương trình bậc nhất hai ẩn — `g9-systems-02`
*Solving Systems of Linear Equations in Two Variables*
- **NB:** nêu các bước của phương pháp thế, phương pháp cộng đại số.
- **TH:** giải hệ đơn giản bằng phương pháp thế/cộng; nhận ra hệ có nghiệm duy nhất, vô nghiệm, vô số nghiệm.
- **VT:** giải hệ có hệ số phân số/thập phân; dùng máy tính cầm tay để tìm nghiệm.
- **V:** tìm hệ số (đường thẳng đi qua hai điểm); hệ quy về bậc nhất bằng đặt ẩn phụ đơn giản; bài toán mua bán.
- **TLTA:** Lesson 2, tr. 8–9; Part 3 – *Substitution Method* (tr. 130).
- **Thuật ngữ:** substitution method, elimination method, unique solution, no solution, infinitely many solutions, intersect, parallel, coincide.
- **Cần biết trước:** Bài 1.
- **Hình/bảng:** đồ thị tương tác hai đường thẳng (cắt nhau / song song / trùng nhau) ứng với ba trường hợp số nghiệm.

### Bài 3. Giải bài toán bằng cách lập hệ phương trình — `g9-systems-03`
*Solving Word Problems Using Systems of Equations*
- **NB:** nêu các bước giải bài toán bằng cách lập hệ phương trình.
- **TH:** chọn ẩn, đặt điều kiện, biểu diễn các đại lượng theo ẩn.
- **VT:** giải bài toán quen thuộc: tổng – hiệu, mua bán, năng suất, chuyển động.
- **V:** bài toán nhiều dữ kiện, phải đối chiếu điều kiện (dự án *The Smart Plan Choice* – chọn gói cước).
- **TLTA:** Lesson 3, tr. 10–11; Mini project Ch.1 (tr. 135).
- **Thuật ngữ:** unknown, condition, represent, respectively, system of equations, check the answer.
- **Cần biết trước:** Bài 2.
- **Hình/bảng:** bảng phân tích đại lượng (ẩn – biểu thức – phương trình).

---

## CHƯƠNG II. PHƯƠNG TRÌNH VÀ BẤT PHƯƠNG TRÌNH BẬC NHẤT MỘT ẨN
*Linear Equations and Linear Inequalities in One Variable* · TLTA tr. 14–23 (có đáp án tr. 22)

### Bài 4. Phương trình quy về phương trình bậc nhất một ẩn — `g9-lineq-01`
*Equations Reducible to Linear Equations in One Variable*
- **NB:** nhận biết phương trình tích; tìm điều kiện xác định của phương trình chứa ẩn ở mẫu.
- **TH:** giải phương trình tích $(ax+b)(cx+d)=0$; nêu các bước giải phương trình chứa ẩn ở mẫu.
- **VT:** phân tích thành nhân tử rồi giải; giải phương trình chứa ẩn ở mẫu, loại nghiệm không thỏa điều kiện xác định.
- **V:** bài toán thực tế dẫn đến phương trình chứa ẩn ở mẫu (năng suất, vận tốc).
- **TLTA:** Lesson 4, tr. 15–17.
- **Thuật ngữ:** product equation, factor (v), Zero-Product Property, denominator, common denominator, restriction / condition for the equation to be defined, extraneous root (*đề xuất bổ sung*).
- **Cần biết trước:** phân tích đa thức thành nhân tử, phân thức đại số (lớp 8).
- **Hình/bảng:** không cần hình; khung "4 bước".

### Bài 5. Bất đẳng thức và tính chất — `g9-lineq-02`
*Inequalities and Their Properties*
- **NB:** nhận biết bất đẳng thức, vế trái, vế phải; các kí hiệu $<, >, \le, \ge$.
- **TH:** phát biểu tính chất bắc cầu, liên hệ với phép cộng, phép nhân (số dương / số âm).
- **VT:** dùng tính chất để so sánh hai biểu thức, chứng minh bất đẳng thức đơn giản.
- **V:** chứng minh bất đẳng thức nhiều bước; tình huống so sánh chi phí.
- **TLTA:** Lesson 5, tr. 18–19.
- **Thuật ngữ:** inequality, left-hand side (LHS), right-hand side (RHS), inequality sign, transitive property, same direction, opposite direction.
- **Cần biết trước:** thứ tự trên tập số thực (lớp 7).
- **Hình/bảng:** trục số minh họa tính chất bắc cầu.

### Bài 6. Bất phương trình bậc nhất một ẩn — `g9-lineq-03`
*Linear Inequalities in One Variable*
- **NB:** nhận biết bất phương trình bậc nhất một ẩn; kiểm tra một số có là nghiệm.
- **TH:** giải bất phương trình $ax+b>0$ (và các dạng $<,\le,\ge$).
- **VT:** giải bất phương trình đưa được về dạng bậc nhất; biểu diễn tập nghiệm.
- **V:** bài toán thực tế (số tiền tối đa, số sản phẩm tối thiểu), tìm nghiệm nguyên lớn nhất/nhỏ nhất.
- **TLTA:** Lesson 6, tr. 20–21.
- **Thuật ngữ:** linear inequality in one variable, solution, solve an inequality, at most, at least.
- **Cần biết trước:** Bài 5.
- **Hình/bảng:** trục số tương tác biểu diễn tập nghiệm. *(SGK KNTT 9 không bắt buộc biểu diễn tập nghiệm trên trục số — xem Q8.)*

---

## CHƯƠNG III. CĂN BẬC HAI VÀ CĂN BẬC BA
*Square Roots and Cube Roots* · TLTA tr. 24–39 (không có đáp án)

### Bài 7. Căn bậc hai và căn thức bậc hai — `g9-roots-01`
*Square Roots and Square Root Expressions*
- **NB:** định nghĩa căn bậc hai, căn bậc hai số học; nhận biết căn thức bậc hai, biểu thức lấy căn.
- **TH:** tìm điều kiện xác định của $\sqrt{A}$; áp dụng $\sqrt{A^2}=|A|$.
- **VT:** tính, so sánh căn bậc hai; dùng máy tính và làm tròn kết quả.
- **V:** rút gọn biểu thức dạng $\sqrt{(a-b)^2}$ có điều kiện; tình huống thực tế (cạnh hình vuông, quãng đường rơi tự do).
- **TLTA:** Lesson 7, tr. 25–28.
- **Thuật ngữ:** square root, principal square root, opposite numbers, non-negative, square root expression, radicand, to be defined, absolute value, identity, simplify, round to two decimal places.
- **Cần biết trước:** số vô tỉ, căn bậc hai số học (lớp 7); hằng đẳng thức (lớp 8).
- **Hình/bảng:** không bắt buộc.

### Bài 8. Khai căn bậc hai với phép nhân và phép chia — `g9-roots-02`
*Square Roots of Products and Quotients*
- **NB:** phát biểu $\sqrt{AB}=\sqrt{A}\cdot\sqrt{B}$ ($A,B\ge 0$), $\sqrt{\dfrac{A}{B}}=\dfrac{\sqrt{A}}{\sqrt{B}}$ ($A\ge0, B>0$).
- **TH:** áp dụng theo hai chiều để tính.
- **VT:** rút gọn biểu thức chứa căn có điều kiện của biến.
- **V:** tình huống vật lí (công suất – hiệu điện thế – điện trở), đường chéo hình chữ nhật.
- **TLTA:** Lesson 8, tr. 29–32.
- **Thuật ngữ:** take the square root, product, quotient, the rule holds when…, strictly positive, perfect square, common factor.
- **Cần biết trước:** Bài 7.
- **Hình/bảng:** không bắt buộc.

### Bài 9. Biến đổi đơn giản và rút gọn biểu thức chứa căn thức bậc hai — `g9-roots-03`
*Simplifying Expressions Containing Square Roots*
- **NB:** nhận biết các phép đưa thừa số ra ngoài/vào trong dấu căn, khử mẫu, trục căn thức ở mẫu.
- **TH:** thực hiện từng phép biến đổi đơn giản.
- **VT:** rút gọn biểu thức phối hợp nhiều phép biến đổi; so sánh không dùng máy tính.
- **V:** bài toán rút gọn nhiều bước với biến; tình huống thực tế (xem Q9).
- **TLTA:** Lesson 9, tr. 33–36.
- **Thuật ngữ:** take a factor out of / into the root sign, clear the fraction inside the root, rationalize the denominator, conjugate expression, numerator, denominator, difference of two squares.
- **Cần biết trước:** Bài 8.
- **Hình/bảng:** không cần.

### Bài 10. Căn bậc ba và căn thức bậc ba — `g9-roots-04`
*Cube Roots and Cube Root Expressions*
- **NB:** định nghĩa căn bậc ba; mọi số thực có đúng một căn bậc ba.
- **TH:** tính căn bậc ba của số (kể cả số âm, phân số); $(\sqrt[3]{A})^3=\sqrt[3]{A^3}=A$.
- **VT:** dùng máy tính, làm tròn; tìm điều kiện/giá trị của căn thức bậc ba.
- **V:** tình huống thể tích hình lập phương (tìm cạnh khi biết thể tích).
- **TLTA:** Lesson 10, tr. 37–39.
- **Thuật ngữ:** cube root, index of the root, cube root expression, cube (n/v), edge, unit cube, volume, unique, estimate to the nearest…
- **Cần biết trước:** Bài 7; thể tích hình lập phương (lớp 6–7).
- **Hình/bảng:** hình lập phương vẽ tĩnh (TikZ → SVG, cạnh khuất nét đứt).

---

## CHƯƠNG IV. HỆ THỨC LƯỢNG TRONG TAM GIÁC VUÔNG
*Right Triangle Trigonometry* · TLTA tr. 40–47 (có đáp án tr. 47); giáo án mẫu Bài 11 tr. 119

### Bài 11. Tỉ số lượng giác của góc nhọn — `g9-trig-01`
*Trigonometric Ratios of Acute Angles*
- **NB:** nhận biết cạnh đối, cạnh kề, cạnh huyền; định nghĩa sin, cos, tan, cot.
- **TH:** tính tỉ số lượng giác khi biết độ dài cạnh; giá trị của góc đặc biệt 30°, 45°, 60°; tỉ số lượng giác của hai góc phụ nhau.
- **VT:** dùng máy tính tìm tỉ số lượng giác / tìm góc (độ, phút), làm tròn.
- **V:** dựng góc khi biết một tỉ số lượng giác; so sánh tỉ số lượng giác.
- **TLTA:** Lesson 11, tr. 41–43; Part 2 – Lesson plan Bài 11 (tr. 119).
- **Thuật ngữ:** right triangle, hypotenuse, opposite side, adjacent side, trigonometric ratio, sine, cosine, tangent, cotangent, complementary angles, degree, minute, round to.
- **Cần biết trước:** tam giác vuông, định lí Pythagore, tam giác đồng dạng (lớp 8).
- **Hình/bảng:** tam giác vuông tương tác (kéo góc, xem các tỉ số đổi); bảng giá trị góc đặc biệt.

### Bài 12. Một số hệ thức giữa cạnh, góc trong tam giác vuông và ứng dụng — `g9-trig-02`
*Relationships Between Sides and Angles in a Right Triangle*
- **NB:** phát biểu hệ thức cạnh góc vuông = cạnh huyền × sin góc đối = cạnh huyền × cos góc kề; = cạnh góc vuông kia × tan góc đối = × cot góc kề.
- **TH:** áp dụng tính cạnh, góc.
- **VT:** giải tam giác vuông; đo chiều cao, khoảng cách.
- **V:** bài toán nhiều bước (hai góc nhìn, đo khoảng cách qua sông – dự án *Measure the Unreachable*).
- **TLTA:** Lesson 12, tr. 44–46; Mini project Ch.4 (tr. 138).
- **Thuật ngữ:** leg, solve a right triangle, angle of elevation, angle of depression, angle of inclination, horizontal, vertical, round to the nearest tenth / degree.
- **Cần biết trước:** Bài 11.
- **Hình/bảng:** hình tương tác (thang dựa tường, nhìn lên đỉnh tháp); hình tĩnh cho bài thực tế.

---

## CHƯƠNG V. ĐƯỜNG TRÒN
*Circles* · TLTA tr. 48–62 (không có đáp án); giáo án mẫu Bài 15 tr. 122

### Bài 13. Mở đầu về đường tròn — `g9-circles-01`
*Introduction to Circles*
- **NB:** định nghĩa đường tròn, tâm, bán kính; vị trí của điểm với đường tròn.
- **TH:** tính đối xứng của đường tròn (tâm đối xứng, trục đối xứng).
- **VT:** xác định vị trí điểm bằng so sánh khoảng cách với bán kính; chứng minh các điểm cùng thuộc một đường tròn.
- **V:** tình huống thực tế (phạm vi phủ sóng, vòng tưới nước).
- **TLTA:** Lesson 13, tr. 49–51 — **chỉ lấy phần phù hợp** (xem D6).
- **Thuật ngữ:** circle, center, radius, diameter, lie on / inside / outside the circle, center of symmetry, axis of symmetry.
- **Cần biết trước:** đường trung trực, tam giác cân (lớp 7).
- **Hình/bảng:** hình tương tác kéo điểm M, hiện $OM$ so với $R$.

### Bài 14. Cung và dây của một đường tròn — `g9-circles-02`
*Arcs and Chords of a Circle*
- **NB:** nhận biết dây, đường kính, góc ở tâm, cung nhỏ, cung lớn, nửa đường tròn.
- **TH:** đường kính là dây lớn nhất; số đo cung nhỏ bằng góc ở tâm chắn cung đó; số đo cung lớn = 360° − cung nhỏ.
- **VT:** tính số đo cung, góc ở tâm; tính độ dài dây trong trường hợp đơn giản.
- **V:** chứng minh, so sánh dây; tình huống (bánh xe, đồng hồ).
- **TLTA:** Lesson 14, tr. 52–53.
- **Thuật ngữ:** chord, diameter, arc, minor arc, major arc, semicircle, central angle, intercepted arc, measure of an arc, endpoints.
- **Cần biết trước:** Bài 13; bất đẳng thức tam giác (lớp 7).
- **Hình/bảng:** hình tương tác kéo điểm trên đường tròn, hiện góc ở tâm và số đo cung.

### Bài 15. Độ dài của cung tròn. Diện tích hình quạt tròn và hình vành khuyên — `g9-circles-03`
*Arc Length, Sectors and Annuli*
- **NB:** nêu công thức độ dài cung $l=\dfrac{\pi R n}{180}$, diện tích hình quạt $S=\dfrac{\pi R^2 n}{360}$, diện tích hình vành khuyên $S=\pi(R^2-r^2)$.
- **TH:** tính trực tiếp theo công thức.
- **VT:** bài toán ngược (biết độ dài cung → tìm bán kính / góc); làm tròn theo yêu cầu.
- **V:** tình huống thực tế (lối đi quanh vườn, chi phí lát gạch, quạt giấy).
- **TLTA:** Lesson 15, tr. 54–56; Part 2 – Lesson plan Bài 15 (tr. 122); Mini project Ch.5 (tr. 142).
- **Thuật ngữ:** arc length, circumference, sector, sector area, annulus (pl. annuli), concentric circles.
- **Cần biết trước:** Bài 14; chu vi, diện tích hình tròn (lớp 6–7).
- **Hình/bảng:** hình quạt tương tác (kéo góc ở tâm); hình vành khuyên tĩnh.

### Bài 16. Vị trí tương đối của đường thẳng và đường tròn — `g9-circles-04`
*Relative Positions of a Line and a Circle*
- **NB:** ba vị trí tương đối (cắt nhau, tiếp xúc, không giao nhau) và hệ thức giữa $d$ và $R$; tiếp tuyến, tiếp điểm.
- **TH:** dấu hiệu nhận biết tiếp tuyến; tính chất hai tiếp tuyến cắt nhau.
- **VT:** xác định vị trí tương đối; tính độ dài tiếp tuyến, độ dài dây bằng định lí Pythagore.
- **V:** chứng minh tiếp tuyến; bài toán thực tế (con đường cạnh công viên tròn).
- **TLTA:** Lesson 16, tr. 57–59.
- **Thuật ngữ:** secant, tangent, point of tangency, intersect, distance from a point to a line, perpendicular, tangent segments.
- **Cần biết trước:** Bài 13, 14; định lí Pythagore (lớp 8).
- **Hình/bảng:** hình tương tác kéo đường thẳng lại gần/xa tâm, hiện $d$ so với $R$.

### Bài 17. Vị trí tương đối của hai đường tròn — `g9-circles-05`
*Relative Positions of Two Circles*
- **NB:** các vị trí tương đối: cắt nhau, tiếp xúc ngoài, tiếp xúc trong, ngoài nhau, đựng nhau (đồng tâm).
- **TH:** liên hệ giữa đoạn nối tâm $d$ với $R+r$ và $R-r$.
- **VT:** xác định vị trí tương đối, tìm bán kính để hai đường tròn tiếp xúc.
- **V:** bài toán thực tế (hai đài phun nước, bánh răng).
- **TLTA:** Lesson 17, tr. 60–62.
- **Thuật ngữ:** distance between the centers, intersecting circles, externally tangent, internally tangent, disjoint circles, concentric circles.
- **Cần biết trước:** Bài 16.
- **Hình/bảng:** hình tương tác kéo tâm thứ hai, hiện vị trí và hệ thức.

---

## CHƯƠNG VI. HÀM SỐ $y=ax^2\ (a\neq0)$. PHƯƠNG TRÌNH BẬC HAI MỘT ẨN
*Quadratic Function and Quadratic Equation* · TLTA tr. 63–79 (không có đáp án)

### Bài 18. Hàm số $y=ax^2\ (a\neq0)$ — `g9-quadratic-01`
*The Function $y=ax^2\ (a\neq0)$*
- **NB:** nhận biết hàm số $y=ax^2$; lập bảng giá trị.
- **TH:** đồ thị là parabol đỉnh $O$, nhận $Oy$ làm trục đối xứng; nằm trên trục hoành khi $a>0$, dưới khi $a<0$.
- **VT:** vẽ đồ thị; tìm $a$ khi biết một điểm thuộc đồ thị; tìm điểm có tung độ/hoành độ cho trước.
- **V:** tình huống thực tế ($s=4{,}9t^2$, $S=\pi r^2$, cổng parabol).
- **TLTA:** Lesson 18, tr. 64–67.
- **Thuật ngữ:** function, coefficient, table of values, plot a point, curve, parabola, vertex, axis of symmetry, symmetric about, abscissa, ordinate.
- **Cần biết trước:** hàm số và đồ thị (lớp 8).
- **Hình/bảng:** đồ thị tương tác (thanh trượt $a$); bảng giá trị ngang.

### Bài 19. Phương trình bậc hai một ẩn — `g9-quadratic-02`
*Quadratic Equations in One Variable*
- **NB:** nhận biết phương trình bậc hai, các hệ số $a,b,c$; công thức biệt thức $\Delta$, $\Delta'$.
- **TH:** giải phương trình khuyết hạng tử; giải bằng công thức nghiệm, công thức nghiệm thu gọn.
- **VT:** giải bằng máy tính cầm tay; giải phương trình hệ số thập phân, có làm tròn.
- **V:** tìm điều kiện của tham số để phương trình có nghiệm / vô nghiệm (mức đơn giản); bài toán thực tế.
- **TLTA:** Lesson 19, tr. 68–71.
- **Thuật ngữ:** quadratic equation in one variable, unknown, coefficient, incomplete equation, complete the square, discriminant, two distinct roots, double root, no real roots, reduced discriminant.
- **Cần biết trước:** Bài 4; hằng đẳng thức (lớp 8).
- **Hình/bảng:** sơ đồ quyết định theo dấu của $\Delta$.

### Bài 20. Định lí Viète và ứng dụng — `g9-quadratic-03`
*Viète's Theorem and Its Applications*
- **NB:** phát biểu định lí Viète: $x_1+x_2=-\dfrac{b}{a}$, $x_1x_2=\dfrac{c}{a}$.
- **TH:** tính tổng, tích các nghiệm không giải phương trình (khi $\Delta\ge0$); nhẩm nghiệm khi $a+b+c=0$ hoặc $a-b+c=0$.
- **VT:** tìm hai số biết tổng và tích; tính giá trị biểu thức đối xứng của nghiệm.
- **V:** bài toán thực tế (kích thước hình chữ nhật biết chu vi, diện tích).
- **TLTA:** Lesson 20, tr. 72–75.
- **Thuật ngữ:** Viète's theorem, sum of the roots, product of the roots, solve by inspection, the remaining root, without solving the equation.
- **Cần biết trước:** Bài 19.
- **Hình/bảng:** không cần.

### Bài 21. Giải bài toán bằng cách lập phương trình — `g9-quadratic-04`
*Solving Problems by Setting Up Equations*
- **NB:** nêu các bước giải bài toán bằng cách lập phương trình.
- **TH:** chọn ẩn, đặt điều kiện, biểu diễn đại lượng theo ẩn.
- **VT:** bài toán diện tích, năng suất, chuyển động dẫn đến phương trình bậc hai.
- **V:** bài toán xuôi/ngược dòng, tăng trưởng phần trăm qua hai năm.
- **TLTA:** Lesson 21, tr. 76–79.
- **Thuật ngữ:** set up an equation, let x be…, suitable condition, express … in terms of x, satisfy the condition, be rejected, downstream, upstream, current, increase/decrease by.
- **Cần biết trước:** Bài 19, 20; Bài 3.
- **Hình/bảng:** bảng phân tích đại lượng.

---

## CHƯƠNG VII. TẦN SỐ VÀ TẦN SỐ TƯƠNG ĐỐI
*Frequency and Relative Frequency* · TLTA tr. 80–89 (không có đáp án)

### Bài 22. Bảng tần số và biểu đồ tần số — `g9-frequency-01`
*Frequency Tables and Frequency Charts*
- **NB:** nhận biết tần số, bảng tần số.
- **TH:** lập bảng tần số từ dãy dữ liệu.
- **VT:** vẽ biểu đồ tần số dạng cột, dạng đoạn thẳng; đọc biểu đồ.
- **V:** nhận xét, rút ra kết luận từ dữ liệu thực tế (chỉ số chất lượng không khí, chiều cao HS).
- **TLTA:** Lesson 22, tr. 81–83.
- **Thuật ngữ:** data value, observation, frequency, frequency table, frequency chart (bar chart, line graph), horizontal axis, vertical axis.
- **Cần biết trước:** thu thập, biểu diễn dữ liệu (lớp 6–8).
- **Hình/bảng:** bảng tần số ngang kẻ đủ đường; biểu đồ cột, đoạn thẳng có tiêu đề, đơn vị.

### Bài 23. Bảng tần số tương đối và biểu đồ tần số tương đối — `g9-frequency-02`
*Relative Frequency Tables and Relative Frequency Charts*
- **NB:** định nghĩa tần số tương đối $f=\dfrac{m}{n}\cdot100\%$.
- **TH:** lập bảng tần số tương đối.
- **VT:** vẽ biểu đồ tần số tương đối dạng cột, dạng hình quạt tròn.
- **V:** so sánh hai mẫu có cỡ mẫu khác nhau (vì sao dùng tần số tương đối).
- **TLTA:** Lesson 23, tr. 84–86.
- **Thuật ngữ:** relative frequency, relative frequency table, relative frequency chart, pie chart, percentage, sample size, proportion.
- **Cần biết trước:** Bài 22; tỉ số phần trăm (lớp 6).
- **Hình/bảng:** bảng ngang; biểu đồ cột, hình quạt tròn.

### Bài 24. Bảng tần số, tần số tương đối ghép nhóm và biểu đồ — `g9-frequency-03`
*Grouped Frequency and Relative Frequency Tables and Charts*
- **NB:** nhận biết mẫu số liệu ghép nhóm, nhóm $[a;b)$, độ dài nhóm.
- **TH:** lập bảng tần số, tần số tương đối ghép nhóm.
- **VT:** vẽ biểu đồ tần số tương đối ghép nhóm dạng cột và dạng đoạn thẳng.
- **V:** chọn cách chia nhóm, nhận xét dữ liệu thực tế (thời gian đến trường).
- **TLTA:** Lesson 24, tr. 87–89.
- **Thuật ngữ:** grouped data, class interval, class width, lower/upper boundary, grouped frequency table, grouped relative frequency table, grouped relative frequency chart.
- **Cần biết trước:** Bài 23.
- **Hình/bảng:** bảng ghép nhóm ngang; biểu đồ cột liền nhau, biểu đồ đoạn thẳng qua trung điểm nhóm.

---

## CHƯƠNG VIII. XÁC SUẤT CỦA BIẾN CỐ TRONG MỘT SỐ MÔ HÌNH XÁC SUẤT ĐƠN GIẢN
*Probability* · TLTA tr. 90–96 (không có đáp án)

### Bài 25. Phép thử ngẫu nhiên và không gian mẫu — `g9-probability-01`
*Random Experiments and Sample Spaces*
- **NB:** nhận biết phép thử ngẫu nhiên, kết quả có thể, không gian mẫu $\Omega$.
- **TH:** liệt kê không gian mẫu của phép thử đơn giản (tung đồng xu, gieo xúc xắc, rút thẻ).
- **VT:** mô tả không gian mẫu của phép thử hai bước bằng bảng hoặc sơ đồ cây.
- **V:** tình huống thực tế (chọn món ăn – đồ uống, mã bảo mật gồm chữ và số).
- **TLTA:** Lesson 25, tr. 91–92.
- **Thuật ngữ:** random experiment, outcome, sample space, coin toss, die / dice, ordered pair, tree diagram.
- **Cần biết trước:** xác suất thực nghiệm (lớp 6–8).
- **Hình/bảng:** sơ đồ cây (tĩnh); bảng hai chiều 6 × 6.

### Bài 26. Xác suất của biến cố liên quan tới phép thử — `g9-probability-02`
*Probability of Events Related to a Random Experiment*
- **NB:** nhận biết biến cố, kết quả thuận lợi, các kết quả đồng khả năng.
- **TH:** công thức $P(A)=\dfrac{n(A)}{n(\Omega)}$; tính xác suất phép thử một bước.
- **VT:** tính xác suất phép thử hai bước (hai xúc xắc, hai vòng quay).
- **V:** dùng xác suất để ra quyết định (trò chơi ở hội chợ trường – dự án *Data, Chance and Decision Making*).
- **TLTA:** Lesson 26, tr. 93–96; Mini project Ch.8 (tr. 147).
- **Thuật ngữ:** event, favorable outcome, equally likely outcomes, probability, fair (coin/die).
- **Cần biết trước:** Bài 25.
- **Hình/bảng:** bảng không gian mẫu tô màu kết quả thuận lợi (tương tác).

---

## CHƯƠNG IX. ĐƯỜNG TRÒN NGOẠI TIẾP VÀ ĐƯỜNG TRÒN NỘI TIẾP
*Circumcircle and Incircle* · TLTA tr. 97–109 (không có đáp án)

### Bài 27. Góc nội tiếp — `g9-inscribed-01`
*Inscribed Angles*
- **NB:** nhận biết góc nội tiếp, cung bị chắn.
- **TH:** số đo góc nội tiếp bằng nửa số đo cung bị chắn; các góc nội tiếp cùng chắn một cung thì bằng nhau; góc nội tiếp chắn nửa đường tròn là góc vuông.
- **VT:** tính góc, chứng minh hai góc bằng nhau.
- **V:** chứng minh nhiều bước; tình huống (vị trí đặt camera nhìn sân khấu dưới cùng một góc).
- **TLTA:** Lesson 27, tr. 98–100.
- **Thuật ngữ:** inscribed angle, vertex, intercepted arc, subtend, angles subtended by the same arc, semicircle.
- **Cần biết trước:** Bài 14.
- **Hình/bảng:** hình tương tác kéo đỉnh góc trên cung, số đo góc không đổi.

### Bài 28. Đường tròn ngoại tiếp và đường tròn nội tiếp của một tam giác — `g9-inscribed-02`
*Circumcircle and Incircle of a Triangle*
- **NB:** nhận biết đường tròn ngoại tiếp, nội tiếp tam giác; tâm là giao ba đường trung trực / ba đường phân giác.
- **TH:** tâm đường tròn ngoại tiếp tam giác vuông là trung điểm cạnh huyền; tam giác đều cạnh $a$: $R=\dfrac{a\sqrt3}{3}$, $r=\dfrac{a\sqrt3}{6}$.
- **VT:** tính bán kính trong tam giác vuông, tam giác đều.
- **V:** tình huống (đặt đèn chiếu cách đều ba điểm; bồn hoa tròn lớn nhất trong sân tam giác).
- **TLTA:** Lesson 28, tr. 101–103.
- **Thuật ngữ:** circumcircle, circumcenter, circumradius, incircle, incenter, inradius, perpendicular bisector, angle bisector, equidistant.
- **Cần biết trước:** đường trung trực, tia phân giác, các đường đồng quy (lớp 7); Bài 13.
- **Hình/bảng:** hình tương tác kéo đỉnh tam giác, hai đường tròn cập nhật theo.

### Bài 29. Tứ giác nội tiếp — `g9-inscribed-03`
*Cyclic Quadrilaterals*
- **NB:** nhận biết tứ giác nội tiếp.
- **TH:** tổng hai góc đối bằng 180°; đường tròn ngoại tiếp hình chữ nhật, hình vuông (tâm, bán kính).
- **VT:** tính góc trong tứ giác nội tiếp; tính bán kính đường tròn ngoại tiếp hình chữ nhật, hình vuông.
- **V:** chứng minh tứ giác nội tiếp; dự án *Smart Circular Theater & Garden*.
- **TLTA:** Lesson 29, tr. 104–106; Mini project Ch.9 (tr. 151).
- **Thuật ngữ:** cyclic quadrilateral, opposite angles, supplementary angles, circumcircle, circumradius, converse.
- **Cần biết trước:** Bài 27.
- **Hình/bảng:** hình tương tác kéo một đỉnh trên đường tròn, tổng hai góc đối luôn 180°.

### Bài 30. Đa giác đều — `g9-inscribed-04`
*Regular Polygons*
- **NB:** nhận biết đa giác đều; hình phẳng có dạng đa giác đều trong thực tế.
- **TH:** phép quay; các phép quay giữ nguyên tam giác đều, hình vuông, lục giác đều.
- **VT:** tính góc ở tâm $\dfrac{360^\circ}{n}$, góc trong; xác định các phép quay giữ nguyên đa giác đều.
- **V:** tính cạnh, chu vi, diện tích đa giác đều nội tiếp (lục giác đều); tình huống trang trí, hoa văn.
- **TLTA:** Lesson 30, tr. 107–109.
- **Thuật ngữ:** polygon, regular polygon, vertex/vertices, interior angle, central angle, rotation, center of rotation, angle of rotation, map … onto itself.
- **Cần biết trước:** Bài 28.
- **Hình/bảng:** đa giác đều tương tác (thanh trượt $n$, nút quay $\dfrac{360^\circ}{n}$).

---

## CHƯƠNG X. MỘT SỐ HÌNH KHỐI TRONG THỰC TIỄN
*Solid Shapes in Everyday Life* · TLTA tr. 110–116 (có đáp án tr. 117)

### Bài 31. Hình trụ và hình nón — `g9-solids-01`
*Cylinders and Cones*
- **NB:** nhận biết hình trụ, hình nón và các yếu tố: đáy, bán kính đáy, chiều cao, đường sinh, đỉnh.
- **TH:** công thức $S_{xq}=2\pi rh$, $V=\pi r^2h$ (hình trụ); $S_{xq}=\pi rl$, $V=\dfrac13\pi r^2h$ (hình nón).
- **VT:** tính diện tích, thể tích; tính đường sinh bằng định lí Pythagore.
- **V:** tình huống (bồn nước, nón lá, mũ sinh nhật cuộn từ hình quạt); dự án *Curved-Surface Design*.
- **TLTA:** Lesson 31, tr. 111–113; Mini project Ch.10 (tr. 155).
- **Thuật ngữ:** cylinder, cone, base, radius of the base, height, lateral surface, lateral area, volume, generatrix / generating line, slant height, vertex, net, rotate.
- **Cần biết trước:** Bài 15; diện tích hình tròn (lớp 6–7).
- **Hình/bảng:** hình trụ, hình nón vẽ tĩnh (TikZ → SVG, nét khuất đứt); hình khai triển.

### Bài 32. Hình cầu — `g9-solids-02`
*Spheres*
- **NB:** nhận biết hình cầu, mặt cầu, tâm, bán kính; mặt cắt của hình cầu là hình tròn.
- **TH:** công thức $S=4\pi R^2$, $V=\dfrac43\pi R^3$.
- **VT:** tính diện tích mặt cầu, thể tích hình cầu, nửa hình cầu.
- **V:** bài toán kết hợp (viên bi trong hộp hình trụ, bồn chứa hình trụ + bán cầu).
- **TLTA:** Lesson 32, tr. 114–116.
- **Thuật ngữ:** sphere, surface of a sphere, solid sphere / ball, center, radius, diameter, hemisphere, plane, cross-section, great circle, surface area.
- **Cần biết trước:** Bài 31.
- **Hình/bảng:** hình cầu vẽ tĩnh (đường xích đạo khuất nét đứt), mặt cắt.

---

## BẢNG TỔNG HỢP: KHÁC NHAU GIỮA TLTA VÀ SGK – ĐỀ XUẤT XỬ LÝ

Nguyên tắc: **kiến thức, ký hiệu theo SGK KNTT**; TLTA dùng cho tiếng Anh, dạng bài, tình huống.

| # | Nội dung | TLTA | SGK KNTT | Đề xuất xử lý |
|---|---|---|---|---|
| D1 | Ký hiệu góc, vuông góc, tập số | `∠ABC`, `⟂`, `x ∈ R` | $\widehat{ABC}$, $\perp$, $\mathbb{R}$ | Dùng ký hiệu SGK ở cả 3 mức ngôn ngữ. |
| D2 | Cặp số, tọa độ, khoảng | Dùng lẫn `(2,0)` và `(1; 3)`; khoảng `[a, b)` | `(2; 0)`, `[a; b)` | Dùng dấu chấm phẩy ở mọi mức (Q2). |
| D3 | Số thập phân | `3.14`, `4.9t²` | `3,14` | Mức 1: dấu phẩy; Mức 2, 3: dấu chấm (theo prompt). |
| D4 | Tiền tệ | Đô la (`$750`, `$60`…) | đồng | Đổi sang đồng (VND) ở cả 3 mức, số liệu phù hợp giá Việt Nam. |
| D5 | Chính tả tiếng Anh | Lẫn Anh–Anh và Anh–Mỹ (center 116 lần / center 17; meter 72 / metre 14; favourable, factorise, rationalise) | — | Dùng **Anh–Mỹ** (Q3). |
| D6 | Bài 13 | Vocab gồm cả tangent, secant, inscribed angle, sector, circumference | Bài 13 chỉ gồm: đường tròn, vị trí điểm – đường tròn, tính đối xứng | Chỉ đưa thuật ngữ đúng bài; chuyển tangent/secant → Bài 16, inscribed angle → Bài 27, sector → Bài 15. |
| D7 | Bài 15 | Ví dụ mở đầu cuộn hình quạt thành hình nón (slant height) | Hình nón học ở Bài 31 | Chuyển tình huống "hình quạt → mũ hình nón" sang Bài 31. |
| D8 | Bài 26 | Biến cố đối, $P(\overline{A})=1-P(A)$ | Không có ở lớp 9 (học ở lớp 10) | Giữ ở mục mở rộng (Q6). |
| D9 | Bài 24 | "histogram" | Biểu đồ tần số (tương đối) ghép nhóm dạng cột | Dùng "grouped frequency chart / histogram" song song, tiếng Việt theo SGK. |
| D10 | Bài 30 | "order of rotational symmetry" | "phép quay giữ nguyên đa giác đều" | Diễn đạt theo SGK; không dạy khái niệm "bậc đối xứng quay". |
| D11 | Định lí Viète | Viết lẫn "Viete" / "Viète" | Viète | Thống nhất **Viète**. |
| D12 | Bài tập "IGCSE-style", "AS/A-level-inspired" (Bài 16, 17) | Tham số $\lvert k-3\rvert$, công thức dây tổng quát, hai dây song song | Vượt mức cơ bản | Chỉ chọn lọc làm câu mức **V**; bỏ phần biện luận tham số phức tạp. |
| D13 | Part 3 – *Linear Inequality in Two Variables* | Có trong TLTA lớp 9 | Thuộc Toán 10 KNTT (Bài 3) | Không đưa vào lớp 9 (đã có bài lớp 10 trên web). |
| D14 | Đáp án | Chỉ có đáp án Ch. 1, 2, 4, 10 | — | Mọi đáp án trên web đều tính lại bằng máy. |

### Lỗi phát hiện trong TLTA (không dùng nguyên văn)

| # | Vị trí | Lỗi | Sửa |
|---|---|---|---|
| E1 | Lesson 1, Key Vocabulary | Nói $(2;0)$ và $\left(x;\dfrac{2-x}{3}\right)$ là nghiệm của $x+3y=3$ | Sai: thực ra là nghiệm của $x+3y=2$. |
| E2 | Lesson 3, Key Vocabulary | "system of equations = phương trình" | Đúng là **hệ phương trình**. |
| E3 | Đáp án Ch. 1 (Ex 4) | Ghi "Cost of a bagel: $3" hai lần | Thiếu giá lon nước cam (đúng là 2 đô la). |
| E5 | Lesson 6, Worked Example 1b | Khai triển \((x+1)(2x-1)=2x^2+x-2\), ra \(x\le\dfrac94\) | Đúng là \(2x^2+x-1\), nghiệm \(x\le2\) (đã sửa ở Ví dụ 4 Bài 6). |
| E4 | Lesson 29, Exercise 6b | "A và C nằm cùng phía đối với BD" trong tứ giác lồi | Mâu thuẫn: tứ giác lồi thì A, C khác phía BD. Không dùng câu này. |

---

## NHỮNG ĐIỂM ĐÃ HỎI GIÁO VIÊN (đã có quyết định ở đầu tệp)

- **Q1 – Bộ sách.** Prompt chưa ghi tên bộ sách, và thầy chưa gửi kèm mục lục SGK. Tôi **giả định Kết nối tri thức** vì 32 bài của TLTA trùng khớp hoàn toàn với mục lục KNTT. Nếu trường dùng Cánh diều hay Chân trời sáng tạo thì cần lập lại dàn ý.
- **Q2 – Dấu phân cách tọa độ ở Mức 2, 3.** Tiếng Anh thường viết `(2, 0)`. Đề xuất: dùng `(2; 0)` ở **mọi** mức cho khớp SGK, vì công thức LaTeX dùng chung. Thầy đồng ý không?
- **Q3 – Chuẩn chính tả tiếng Anh.** Chọn Anh–Anh (center, metre, favourable, factorise — chiếm đa số trong TLTA) hay Anh–Mỹ (center, meter…)? Cần thống nhất với phần lớp 10–12 đã có trên web.
- **Q4 – "góc nâng / góc hạ" (Bài 12).** TLTA dịch *angle of elevation / depression* là "góc nâng / góc hạ". Tôi chưa chắc SGK KNTT 9 có dùng hai thuật ngữ này. Đề xuất: giữ tiếng Anh, tiếng Việt diễn đạt "góc tạo bởi tia nhìn và phương nằm ngang". Thầy kiểm tra giúp SGK.
- **Q5 – "sphere" (Bài 32).** TLTA dịch sphere = "mặt cầu / hình cầu". Đề xuất: *sphere* → hình cầu; *surface of a sphere* → mặt cầu; *solid sphere / ball* → hình cầu (khối). Thầy duyệt cách gán này?
- **Q6 – Biến cố đối (Bài 26).** Bỏ hẳn, hay giữ ở mục "Mở rộng" (không có trong bài tập chấm điểm)?
- **Q7 – Thuật ngữ "unknown" và "variable".** TLTA dùng *quadratic equation in one unknown*. Đề xuất: dùng *in one variable* cho thống nhất với Bài 1, 4, 6 và từ điển lớp 10. Thầy đồng ý không?
- **Q8 – Trục số ở Bài 6.** Biểu diễn tập nghiệm bất phương trình trên trục số: đưa vào như hình minh họa (không bắt buộc), hay bỏ hẳn?
- **Q9 – Tình huống công thức khối lượng tương đối tính (Bài 9).** TLTA dùng $m=\dfrac{m_0}{\sqrt{1-\frac{v^2}{c^2}}}$. Đề xuất: chỉ dùng ở mức **V** dạng "thay số rồi tính", có giải thích ngắn. Giữ hay bỏ?
- **Q10 – Thứ tự soạn.** Đề xuất soạn theo cụm chương: Ch. I (3 bài) → Ch. II → … Mỗi lần giao 2–3 bài để thầy kiểm tra. Thầy muốn bắt đầu từ chương nào?

## Kết quả soạn Bài 1–4 (12/11/2026)

| Bài | Mã bài | Ví dụ (NB / TH / VT / V) | Luyện tập A / B / C (mỗi mức ngôn ngữ) | Tự luyện D1–D4 (mỗi mức ngôn ngữ) | Hình vẽ | Kiểm thử |
|---|---|---|---|---|---|---|
| 1 | `g9-systems-01` | 5 (1 / 2 / 1 / 1) | 3 / 2 / 2 | 3 / 3 / 3 / 3 | 3 hình (đường thẳng biểu diễn tập nghiệm, hai đường thẳng cắt nhau) | đạt |
| 2 | `g9-systems-02` | 5 (1 / 2 / 1 / 1) | 3 / 2 / 2 | 3 / 3 / 3 / 3 | 2 hình (hai đường thẳng cắt nhau, song song) + bảng số nghiệm | đạt |
| 3 | `g9-systems-03` | 5 (1 / 1 / 2 / 1) | 3 / 2 / 2 | 3 / 3 / 3 / 3 | bảng các dạng bài | đạt |
| 4 | `g9-lineq-01` | 5 (1 / 2 / 1 / 1) | 3 / 2 / 2 | 3 / 3 / 3 / 3 | — | đạt |

Mỗi bài có 19 câu cho mỗi mức ngôn ngữ (ba bộ cùng dạng, khác số liệu, không trùng câu). Câu hỏi sinh bằng `tools/sp_g9.py`; đáp án tính bằng phân số và tự kiểm (thay nghiệm, đối chiếu điều kiện xác định).

### Thuật ngữ mới đã thêm vào từ điển chung (`data/vocab.json`)

| Bài | Tiếng Anh | Tiếng Việt | Câu ví dụ | Nguồn |
|---|---|---|---|---|
| g9-systems-01 | linear equation in two variables | phương trình bậc nhất hai ẩn | x + 3y = 2 is a linear equation in two variables. | TLTA Ch.1 L1, tr. 6–7 |
| g9-systems-01 | ordered pair | cặp số | The ordered pair (2; 0) is a solution of x + 3y = 2. | TLTA Ch.1 L1, tr. 6–7 |
| g9-systems-01 | general solution | nghiệm tổng quát | The general solution of 2x − y = 1 is (x; 2x − 1). | TLTA Ch.1 L1, tr. 6–7 |
| g9-systems-01 | coordinate plane | mặt phẳng tọa độ | Graph the solutions on the coordinate plane. | TLTA Ch.1 L1, tr. 6–7 |
| g9-systems-01 | line | đường thẳng | The solutions of a linear equation in two variables form a line. | TLTA Ch.1 L1, tr. 6–7 |
| g9-systems-01 | geometric representation | biểu diễn hình học | The geometric representation of the solutions is a line. | TLTA Ch.1 L1, tr. 6–7 |
| g9-systems-01 | system of two linear equations in two variables | hệ hai phương trình bậc nhất hai ẩn | x + y = 2 and x + 3y = 2 form a system of two linear equations in two variables. | TLTA Ch.1 L1, tr. 6–7 |
| g9-systems-01 | system of equations | hệ phương trình | Solve the system of equations. | TLTA Ch.1 L1, tr. 6–7 |
| g9-systems-01 | solve a system | giải hệ phương trình | To solve a system means to find all its solutions. | TLTA Ch.1 L1, tr. 6–7 |
| g9-systems-01 | infinitely many solutions | vô số nghiệm | Any linear equation in two variables has infinitely many solutions. | TLTA Ch.1 L1, tr. 6–7 |
| g9-systems-01 | solution of an equation | nghiệm của phương trình | (1; 1) is a solution of the equation 2x − y = 1. | TLTA Ch.1 L1, tr. 6–7 |
| g9-systems-01 | solution set | tập nghiệm | The solution set is represented by a line. | TLTA Ch.1 L1, tr. 6–7 |
| g9-systems-01 | intersect | cắt nhau | If two lines intersect at one point, the system has a unique solution. | TLTA Ch.1 L1, tr. 6–7 |
| g9-systems-01 | coincide | trùng nhau | If two lines coincide, the system has infinitely many solutions. | TLTA Ch.1 L1, tr. 6–7 |
| g9-systems-02 | substitution method | phương pháp thế | To solve by the substitution method, we express x in terms of y. | TLTA Ch.1 L2, tr. 8–9; Part 3 (tr. 130) |
| g9-systems-02 | elimination method | phương pháp cộng đại số | Use the elimination method: add the two equations to eliminate y. | TLTA Ch.1 L2, tr. 8–9; Part 3 (tr. 130) |
| g9-systems-02 | unique solution | nghiệm duy nhất | If two lines intersect at one point, the system has a unique solution. | TLTA Ch.1 L2, tr. 8–9; Part 3 (tr. 130) |
| g9-systems-02 | eliminate (a variable) | khử ẩn | Subtract the equations to eliminate x. | TLTA Ch.1 L2, tr. 8–9; Part 3 (tr. 130) |
| g9-systems-02 | express … in terms of … | biểu diễn theo | Express y in terms of x. | TLTA Ch.1 L2, tr. 8–9; Part 3 (tr. 130) |
| g9-systems-02 | calculator | máy tính cầm tay | Check your answer with a calculator. | TLTA Ch.1 L2, tr. 8–9; Part 3 (tr. 130) |
| g9-systems-02 | opposite numbers | hai số đối nhau | The coefficients of y are opposite numbers, so add the equations. | TLTA Ch.1 L2, tr. 8–9; Part 3 (tr. 130) |
| g9-systems-03 | unknown | ẩn số | Let x and y be the unknowns. | TLTA Ch.1 L3, tr. 10–11; Mini project Ch.1 |
| g9-systems-03 | condition for the unknowns | điều kiện của ẩn | The condition for the unknowns is x > y > 0. | TLTA Ch.1 L3, tr. 10–11; Mini project Ch.1 |
| g9-systems-03 | set up a system of equations | lập hệ phương trình | Use the given information to set up a system of equations. | TLTA Ch.1 L3, tr. 10–11; Mini project Ch.1 |
| g9-systems-03 | respectively | lần lượt | Let x and y be the numbers of students in class A and class B, respectively. | TLTA Ch.1 L3, tr. 10–11; Mini project Ch.1 |
| g9-systems-03 | exceed (the plan) | vượt mức | Workshop A exceeded the plan by 15%. | TLTA Ch.1 L3, tr. 10–11; Mini project Ch.1 |
| g9-systems-03 | word problem | bài toán thực tế | Solve the word problem by setting up a system of equations. | TLTA Ch.1 L3, tr. 10–11; Mini project Ch.1 |
| g9-lineq-01 | linear equation in one variable | phương trình bậc nhất một ẩn | A linear equation in one variable has the form ax + b = 0 (a ≠ 0). | TLTA Ch.2 L4, tr. 15–17 |
| g9-lineq-01 | product equation | phương trình tích | (x + 1)(x − 1) = 0 is a product equation. | TLTA Ch.2 L4, tr. 15–17 |
| g9-lineq-01 | Zero-Product Property | tính chất tích bằng 0 | By the Zero-Product Property, if A · B = 0 then A = 0 or B = 0. | TLTA Ch.2 L4, tr. 15–17 |
| g9-lineq-01 | common factor | nhân tử chung | Take out the common factor x + 1. | TLTA Ch.2 L4, tr. 15–17 |
| g9-lineq-01 | denominator | mẫu thức | In (x + 1)/(x − 1), x − 1 is the denominator. | TLTA Ch.2 L4, tr. 15–17 |
| g9-lineq-01 | common denominator | mẫu thức chung | The common denominator of 1/(x − 1) and 1/(x + 1) is (x + 1)(x − 1). | TLTA Ch.2 L4, tr. 15–17 |
| g9-lineq-01 | equation with the variable in the denominator | phương trình chứa ẩn ở mẫu | 1/(x − 2) + 3 = (x − 3)/(2 − x) has the variable in the denominator. | TLTA Ch.2 L4, tr. 15–17 |
| g9-lineq-01 | condition for the equation to be defined (restriction) | điều kiện xác định | The restriction of (x + 1)/(x − 1) is x ≠ 1. | TLTA Ch.2 L4, tr. 15–17 |
| g9-lineq-01 | clear the denominators | khử mẫu | Multiply both sides by the common denominator to clear the denominators. | TLTA Ch.2 L4, tr. 15–17 |
| g9-lineq-01 | downstream | xuôi dòng | The boat goes 36 km downstream. | TLTA Ch.2 L4, tr. 15–17 |
| g9-lineq-01 | upstream | ngược dòng | Going upstream, the boat is slower. | TLTA Ch.2 L4, tr. 15–17 |
| g9-lineq-01 | speed in still water | vận tốc riêng | Find the speed of the boat in still water. | TLTA Ch.2 L4, tr. 15–17 |

### Ghi chú khi soạn

- Từ "nghiệm" và "vận tốc" trong từ điển chung đang gắn với "zero (root)" và "velocity" (dùng cho lớp 11–12). Ở câu hỏi lớp 9, chú thích tiếng Anh được đổi thành "solution" và "speed".
- Hình vẽ là hình tĩnh vẽ bằng LaTeX (theo hệ thống hiện hành của website), không phải hình kéo thả tương tác.
- Bài 4 không đặt bài trước bắt buộc (kiến thức nền là phân tích nhân tử, phân thức của lớp 8).

## Kết quả soạn Bài 5–8 (12/11/2026)

| Bài | Mã bài | Ví dụ (NB / TH / VT / V) | A / B / C | D1–D4 | Hình vẽ | Kiểm thử |
|---|---|---|---|---|---|---|
| 5 | `g9-lineq-02` | 5 (1 / 2 / 1 / 1) | 3 / 2 / 2 | 3 / 3 / 3 / 3 | — | đạt |
| 6 | `g9-lineq-03` | 5 (1 / 2 / 1 / 1) | 3 / 2 / 2 | 3 / 3 / 3 / 3 | 4 trục số (chấm đặc / chấm rỗng) | đạt |
| 7 | `g9-roots-01` | 5 (1 / 2 / 1 / 1) | 3 / 2 / 2 | 3 / 3 / 3 / 3 | — | đạt |
| 8 | `g9-roots-02` | 5 (1 / 2 / 1 / 1) | 3 / 2 / 2 | 3 / 3 / 3 / 3 | — | đạt |

Hình vẽ: nhãn điểm trên hình tọa độ được đặt tự động theo hướng vuông góc với các đường thẳng đi qua điểm (`sp_g9.auto_labels`), không bị đè hay bị cắt; trục số đặt nhãn đầu mút dưới chấm, bỏ vạch chia trùng.

### Thuật ngữ mới (Bài 5–8)

| Bài | Tiếng Anh | Tiếng Việt | Câu ví dụ | Nguồn |
|---|---|---|---|---|
| g9-lineq-02 | inequality | bất đẳng thức | An inequality is a statement comparing two expressions, such as a < b. | TLTA Ch.2 L5, tr. 18–19 |
| g9-lineq-02 | left-hand side (LHS) | vế trái | In the inequality a < b, a is the left-hand side. | TLTA Ch.2 L5, tr. 18–19 |
| g9-lineq-02 | right-hand side (RHS) | vế phải | In the inequality a < b, b is the right-hand side. | TLTA Ch.2 L5, tr. 18–19 |
| g9-lineq-02 | same direction | cùng chiều | a < b and c < d are inequalities of the same direction. | TLTA Ch.2 L5, tr. 18–19 |
| g9-lineq-02 | opposite direction | ngược chiều | a < b and c > d are inequalities of the opposite direction. | TLTA Ch.2 L5, tr. 18–19 |
| g9-lineq-02 | inequality sign | dấu bất đẳng thức | When multiplying by a negative number, reverse the inequality sign. | TLTA Ch.2 L5, tr. 18–19 |
| g9-lineq-02 | reverse the inequality sign | đổi chiều bất đẳng thức | Multiply by −2 and reverse the inequality sign. | TLTA Ch.2 L5, tr. 18–19 |
| g9-lineq-03 | inequality (with a variable) | bất phương trình | 3x − 1 < 5 is an inequality in the variable x. | TLTA Ch.2 L6, tr. 20–21 |
| g9-lineq-03 | linear inequality in one variable | bất phương trình bậc nhất một ẩn | 3x − 1 < 0 is a linear inequality in one variable. | TLTA Ch.2 L6, tr. 20–21 |
| g9-lineq-03 | solution of an inequality | nghiệm của bất phương trình | x = 0 is a solution of the inequality 3x − 6 < 0. | TLTA Ch.2 L6, tr. 20–21 |
| g9-lineq-03 | solve an inequality | giải bất phương trình | Solve the following inequalities. | TLTA Ch.2 L6, tr. 20–21 |
| g9-lineq-03 | move a term to the other side | chuyển vế | Move −2 to the right-hand side and change its sign. | TLTA Ch.2 L6, tr. 20–21 |
| g9-roots-01 | principal square root | căn bậc hai số học | The principal square root of 81 is 9, written √81 = 9. | TLTA Ch.3 L7, tr. 25–28 |
| g9-roots-01 | square root expression | căn thức bậc hai | √(2x + 1) is a square root expression. | TLTA Ch.3 L7, tr. 25–28 |
| g9-roots-01 | radicand | biểu thức lấy căn | The radicand of √(5 − 2x) is 5 − 2x. | TLTA Ch.3 L7, tr. 25–28 |
| g9-roots-01 | non-negative | không âm | √A is defined only when A is non-negative. | TLTA Ch.3 L7, tr. 25–28 |
| g9-roots-01 | identity | hằng đẳng thức | Apply the identity √(A²) = |A|. | TLTA Ch.3 L7, tr. 25–28 |
| g9-roots-01 | round to two decimal places | làm tròn đến chữ số thập phân thứ hai | Rounding to two decimal places, √11.1 ≈ 3.33. | TLTA Ch.3 L7, tr. 25–28 |
| g9-roots-01 | perfect square | số chính phương | 49 is a perfect square: 49 = 7². | TLTA Ch.3 L7, tr. 25–28 |
| g9-roots-02 | take the square root | khai căn bậc hai | Take the square root of each factor. | TLTA Ch.3 L8, tr. 29–32 |
| g9-roots-02 | product | tích | The square root of a product equals the product of the square roots. | TLTA Ch.3 L8, tr. 29–32 |
| g9-roots-02 | the rule holds when … | quy tắc đúng khi | The rule √(AB) = √A·√B holds when A ≥ 0 and B ≥ 0. | TLTA Ch.3 L8, tr. 29–32 |
| g9-roots-02 | strictly positive | dương | The denominator B must be strictly positive: B > 0. | TLTA Ch.3 L8, tr. 29–32 |
| g9-roots-02 | take out of the root sign | đưa ra ngoài dấu căn | √(25a²b²) = 5|ab|: take 5|ab| out of the root sign. | TLTA Ch.3 L8, tr. 29–32 |

## Kết quả soạn Bài 9–11 (12/11/2026)

Tên các mức (cả 11 bài): **Nhận biết – Thông hiểu – Vận dụng thấp – Vận dụng**.

| Bài | Mã bài | Ví dụ (NB / TH / VT / V) | A / B / C | D1–D4 | Hình vẽ | Kiểm thử |
|---|---|---|---|---|---|---|
| 9 | `g9-roots-03` | 5 (1 / 2 / 1 / 1) | 3 / 2 / 2 | 3 / 3 / 3 / 3 | — | đạt |
| 10 | `g9-roots-04` | 5 (1 / 2 / 1 / 1) | 3 / 2 / 2 | 3 / 3 / 3 / 3 | — | đạt |
| 11 | `g9-trig-01` | 5 (1 / 2 / 1 / 1) | 3 / 2 / 2 | 3 / 3 / 3 / 3 | 2 (tam giác vuông có góc α; bài cái cây – góc nâng 40°) | đạt |

- Kiểm đáp án độc lập (tính lại bằng số thực từ đề, không dùng mã sinh câu): 171 câu tự luyện/luyện tập của Bài 9–11, 0 câu sai (6 câu lời văn kiểm tay).
- Ví dụ Bài 9 mức Vận dụng: công thức khối lượng tương đối tính, có giải thích ngắn (theo Q9).
- Bài 11: tên điểm đặt theo phân giác ngoài của đỉnh tam giác, không bị cạnh cắt; số đo góc ghi bằng chữ α hoặc 40°.

**Thuật ngữ mới**

| Bài | Tiếng Anh | Tiếng Việt | Câu ví dụ | Nguồn |
|---|---|---|---|---|
| g9-roots-03 | bring into the root sign | đưa vào trong dấu căn | 4√3 = √(16·3) = √48. | TLTA Ch.3 L9 |
| g9-roots-03 | rationalize the denominator | trục căn thức ở mẫu | 1/√5 = √5/5. | TLTA Ch.3 L9 |
| g9-roots-03 | conjugate expression | biểu thức liên hợp | The conjugate of √5 − 2 is √5 + 2. | TLTA Ch.3 L9 |
| g9-roots-03 | like radicals | căn thức đồng dạng | 2√3 and −5√3 are like radicals. | TLTA Ch.3 L9 |
| g9-roots-03 | simplify an expression | rút gọn biểu thức | Simplify 2√3 − √75. | TLTA Ch.3 L9 |
| g9-roots-04 | cube root | căn bậc ba | The cube root of −27 is −3. | TLTA Ch.3 L10 |
| g9-roots-04 | index (of a root) | chỉ số của căn | In ∛a, 3 is the index. | TLTA Ch.3 L10 |
| g9-roots-04 | cube root expression | căn thức bậc ba | ∛(2x + 5) is a cube root expression. | TLTA Ch.3 L10 |
| g9-roots-04 | cube (of a number) | lập phương (của một số) | The cube of 4 is 64. | TLTA Ch.3 L10 |
| g9-roots-04 | volume | thể tích | The volume of a cube with edge a is a³. | TLTA Ch.3 L10 |
| g9-trig-01 | trigonometric ratio | tỉ số lượng giác | sin, cos, tan, cot are trigonometric ratios. | TLTA Ch.4 L11 |
| g9-trig-01 | opposite side / adjacent side | cạnh đối / cạnh kề | For angle B, AC is opposite, AB is adjacent. | TLTA Ch.4 L11 |
| g9-trig-01 | hypotenuse | cạnh huyền | The hypotenuse is opposite the right angle. | TLTA Ch.4 L11 |
| g9-trig-01 | right triangle | tam giác vuông | ABC is a right triangle with the right angle at A. | TLTA Ch.4 L11 |
| g9-trig-01 | angle of elevation / depression | góc nâng / góc hạ | The angle of elevation of the sun is 40°. | TLTA Ch.4 L11 (Q4) |
