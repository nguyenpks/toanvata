# DÀN Ý KHỐI LỚP 8 – Website "Toán và Tiếng Anh"

> **Trạng thái: GV cho soạn (26/11/2026), các điểm Q1–Q11 chưa trả lời – tạm theo đề xuất.** Đã soạn: **Bài 1–5 (Chương I)**.
> Tài liệu chuyên ngành: *Tài liệu hướng dẫn triển khai dạy học cấp THCS bằng tiếng Anh – Môn Toán – Khối 8* (Bộ GD&ĐT, Hà Nội 2026), gọi tắt **TLTA**. Số trang ghi theo mục lục TLTA.
> Sách giáo khoa: **Toán 8 – Kết nối tri thức với cuộc sống (KNTT)**, 2 tập. Thứ tự **39 bài, 10 chương** của TLTA **trùng khớp hoàn toàn** với KNTT (đã đối chiếu tên từng bài, xem bảng ở mục 1).

---

## 0. Quy ước chung (kế thừa quyết định đã duyệt ở khối 9)

- Bộ sách **KNTT**; cặp số, tọa độ dùng **dấu chấm phẩy** ở cả 3 mức: `A(−1; 2)`; chính tả tiếng Anh **Anh–Mỹ**; dùng *in one variable*.
- Mã bài `g8-<chủ-đề>-<số>`; tệp `content/grade8/<mã-bài>.py`.
- Mỗi bài: Từ vựng – Cụm từ tiếng Anh – Lý thuyết – 5 ví dụ (NB / TH ×2 / VT / V) – Tự luyện 3 mức ngôn ngữ, gồm A (3), B đúng/sai (2), C trả lời ngắn (2), D theo 4 mức nhận thức D1–D4 (3 câu mỗi mức).
- Viết tắt 4 mức độ: **NB** = Nhận biết, **TH** = Thông hiểu, **VT** = Vận dụng thấp, **V** = Vận dụng.
- Cấu trúc mỗi bài trong TLTA: *1. Key Vocabulary – 2. Useful Mathematical Expressions – 3. Worked Examples – 4. Worksheet*. Khai thác: mục 1 → **Từ vựng Toán học**; mục 2 → **Cụm từ tiếng Anh thường gặp**; mục 3–4 → dạng bài, tình huống thực tế (đổi số liệu, không chép nguyên).
- Ngoài phần 1, TLTA còn có:
  - **Part 2** – giáo án mẫu Bài 1 (tr. 149), Bài 33 (tr. 155);
  - **Part 3** – 7 đoạn giáo án (tr. 161–175): đơn thức, hiệu hai bình phương, nhận biết hình chữ nhật qua đường chéo, định lí đường trung bình, số liệu rời rạc – liên tục, phương trình bậc nhất một ẩn, trường hợp góc – góc → dùng cho phần Lý thuyết (cách phát biểu định nghĩa, định lí bằng tiếng Anh);
  - **Part 4** – 8 dự án nhỏ (từ tr. 177) → dùng làm tình huống cho mức **V**.
- Kiến thức nền ghi theo tên bài SGK lớp 7/8. Bài lớp 8 sẽ liên kết sang các bài lớp 9 đã có (ví dụ Bài 25 → lớp 9 Bài 4; Bài 28–29 → lớp 9 Bài 1–2).
- **Hình vẽ:** dùng hình/bảng **tĩnh** như lớp 9 Bài 26–32 (xem Q8). Tên điểm không bị đè, không bị đường cắt qua; góc vuông vẽ ô vuông.
- **Số thập phân:** Mức 1 dấu phẩy; Mức 2, 3 dấu chấm. **Tiền tệ:** TLTA dùng đô la (26 chỗ, ví dụ vé \$15, phòng gym \$50, thuê xe \$40/ngày) → đổi sang **đồng (VND)**, số liệu hợp giá Việt Nam.

---

## 1. Đối chiếu TLTA – SGK KNTT 8

| Ch. | SGK KNTT 8 | TLTA (tr.) | Bài | Khớp |
|---|---|---|---|---|
| I | Đa thức | Polynomials (6–21) | 1–5 | ✓ |
| II | Hằng đẳng thức đáng nhớ và ứng dụng | Algebraic Identities and Applications (22–34) | 6–9 | ✓ |
| III | Tứ giác | Quadrilaterals (35–55) | 10–14 | ✓ |
| IV | Định lí Thalès | Triangle Proportionality (Thales' Theorem) (56–71) | 15–17 | ✓ |
| V | Dữ liệu và biểu đồ | Data and Chart (72–83) | 18–20 | ✓ |
| VI | Phân thức đại số | Algebraic Fractions (84–96) | 21–24 | ✓ |
| VII | Phương trình bậc nhất và hàm số bậc nhất | Linear Equations and Linear Functions (97–112) | 25–29 | ✓ |
| VIII | Mở đầu về tính xác suất của biến cố | Probability (113–119) | 30–32 | ✓ |
| IX | Tam giác đồng dạng | Similar Triangles (120–140) | 33–37 | ✓ |
| X | Một số hình khối trong thực tiễn | Solid Shapes in Everyday Life (141–147) | 38–39 | ✓ |

- Các mục *Luyện tập chung*, *Bài tập cuối chương* của SGK không thành bài riêng; dạng bài của chúng được đưa vào mức VT, V của bài tương ứng.
- *Hoạt động thực hành trải nghiệm* của SGK Tập 1 gồm: công thức lãi kép (→ tình huống Bài 4, 7), tính toán đa thức và vẽ hình bằng GeoGebra (không đưa vào web), phân tích khí hậu Việt Nam (→ tình huống Bài 20).
- Đáp án TLTA có ở Ch. I–VII, IX, X; **không có đáp án Ch. VIII**. Mọi đáp án trên web đều tính lại bằng máy.

---

## CHƯƠNG I. ĐA THỨC
*Polynomials* · TLTA tr. 6–21 (có đáp án tr. 20) · Part 2: giáo án Bài 1 · Part 3: *Monomials* (tr. 161)

### Bài 1. Đơn thức — `g8-polynomials-01`
*Monomials*
- **NB:** nhận biết đơn thức (số, biến, tích của số và biến); chỉ ra hệ số, phần biến.
- **TH:** thu gọn đơn thức; tìm bậc; nhận biết đơn thức đồng dạng.
- **VT:** cộng, trừ đơn thức đồng dạng; tính giá trị đơn thức tại giá trị cho trước của biến.
- **V:** tìm đơn thức \(A\) thỏa \(A - xy^2z = 4xy^2z\); tình huống diện tích/thể tích viết dưới dạng đơn thức.
- **TLTA:** Lesson 1, tr. 7–9 (Example 1–3, Exercise 1–5); Part 2 – Lesson plan (tr. 149); Part 3 (tr. 161).
- **Thuật ngữ:** monomial, algebraic expression, product, variable, literal part, coefficient, exponent, degree, term, like terms, one-variable, multi-variable.
- **Cần biết trước:** biểu thức đại số, đa thức một biến (lớp 7).
- **Hình/bảng:** bảng "đơn thức – hệ số – phần biến – bậc".

### Bài 2. Đa thức — `g8-polynomials-02`
*Polynomials*
- **NB:** nhận biết đa thức, hạng tử; đa thức không; nhị thức, tam thức.
- **TH:** thu gọn đa thức; tìm bậc của đa thức.
- **VT:** tính giá trị đa thức (thu gọn trước khi thay số).
- **V:** đa thức biểu diễn chu vi, diện tích hình ghép; tìm các hạng tử có bậc cho trước.
- **TLTA:** Lesson 2, tr. 10–12 (Example 1–3, Exercise 1–3).
- **Thuật ngữ:** polynomial, constant term, zero polynomial, binomial, trinomial, simplified polynomial, degree of a polynomial.
- **Cần biết trước:** Bài 1.
- **Hình/bảng:** hình chữ nhật ghép có kích thước theo \(x, y\).

### Bài 3. Phép cộng và phép trừ đa thức — `g8-polynomials-03`
*Adding and Subtracting Polynomials*
- **NB:** quy tắc cộng, trừ hai đa thức (bỏ ngoặc, nhóm hạng tử đồng dạng).
- **TH:** tính \(A+B\), \(A-B\).
- **VT:** tìm đa thức \(M\) thỏa \(M + B = C\); tính \(M+N-P\); tìm bậc và giá trị của tổng, hiệu.
- **V:** tình huống doanh thu – chi phí – lợi nhuận viết dưới dạng đa thức.
- **TLTA:** Lesson 3, tr. 13–14 (Example 1–2, Exercise 1–4).
- **Thuật ngữ:** sum, difference, commutative property of addition, associative property of addition, remove brackets.
- **Cần biết trước:** Bài 2.
- **Hình/bảng:** không bắt buộc.

### Bài 4. Phép nhân đa thức — `g8-polynomials-04`
*Multiplying Polynomials*
- **NB:** quy tắc nhân đơn thức với đơn thức, đơn thức với đa thức, đa thức với đa thức.
- **TH:** thực hiện phép nhân, thu gọn kết quả.
- **VT:** rút gọn rồi tính giá trị biểu thức; chứng minh giá trị biểu thức không phụ thuộc vào biến.
- **V:** diện tích, thể tích hình hộp có kích thước là đa thức; tiền lãi gửi ngân hàng sau 2 kì (gắn với trải nghiệm *Công thức lãi kép*).
- **TLTA:** Lesson 4, tr. 15–17 (Example 1–3, Exercise 1–4).
- **Thuật ngữ:** commutative / associative property of multiplication, distributive property, expand, independent of the variables.
- **Cần biết trước:** Bài 3; lũy thừa cùng cơ số (lớp 7).
- **Hình/bảng:** mô hình diện tích \((a+b)(c+d)\) bằng hình chữ nhật chia ô.

### Bài 5. Phép chia đa thức cho đơn thức — `g8-polynomials-05`
*Dividing Polynomials by Monomials*
- **NB:** điều kiện để đơn thức \(A\) chia hết cho đơn thức \(B\); đa thức chia hết cho đơn thức.
- **TH:** chia đơn thức cho đơn thức, đa thức cho đơn thức.
- **VT:** tìm đa thức \(A\) biết \(A\cdot(-5x^2y^2)=\dots\); rút gọn biểu thức có phép chia.
- **V:** tìm chiều dài hình chữ nhật khi biết diện tích (đa thức) và chiều rộng (đơn thức).
- **TLTA:** Lesson 5, tr. 18–19 (Example 1–3, Exercise 1–4).
- **Thuật ngữ:** base, quotient, be divisible by, exact division.
- **Cần biết trước:** Bài 4.
- **Hình/bảng:** không bắt buộc.

---

## CHƯƠNG II. HẰNG ĐẲNG THỨC ĐÁNG NHỚ VÀ ỨNG DỤNG
*Algebraic Identities and Applications* · TLTA tr. 22–34 (có đáp án tr. 32) · Part 3: *Difference of Two Squares* (tr. 163)

### Bài 6. Hiệu hai bình phương. Bình phương của một tổng hay một hiệu — `g8-identities-01`
*Difference of Two Squares. Square of a Sum or a Difference*
- **NB:** nhận biết hằng đẳng thức; phát biểu \(a^2-b^2\), \((a+b)^2\), \((a-b)^2\) (bằng lời tiếng Anh theo Part 3).
- **TH:** khai triển; viết biểu thức dưới dạng bình phương hoặc tích.
- **VT:** tính nhanh (\(99^2\), \(101\cdot 99\)); rút gọn biểu thức.
- **V:** cho \(a^2+b^2=10\), \(ab=3\), tính \(a+b\), \(a-b\); diện tích lối đi quanh vườn hình vuông.
- **TLTA:** Lesson 6, tr. 23–25 (Example 1–4, Exercise 1–6); Part 3 (tr. 163).
- **Thuật ngữ:** identity, square, expand, left-hand side (LHS), right-hand side (RHS), difference of two squares, square of a sum, square of a difference.
- **Cần biết trước:** Bài 4.
- **Hình/bảng:** hình vuông cạnh \(a+b\) chia 4 phần (minh họa \((a+b)^2\)).

### Bài 7. Lập phương của một tổng. Lập phương của một hiệu — `g8-identities-02`
*Cube of a Sum or a Difference*
- **NB:** phát biểu \((a+b)^3\), \((a-b)^3\).
- **TH:** khai triển; viết biểu thức dưới dạng lập phương.
- **VT:** viết dưới dạng lập phương rồi tính giá trị (tại \(x=1{,}5\)); chứng minh biểu thức không phụ thuộc \(x\).
- **V:** chứng minh \((a+b)^3=a^3+b^3+3ab(a+b)\); thể tích khối lập phương tăng cạnh thêm \(x\) cm.
- **TLTA:** Lesson 7, tr. 26–27 (Example 1–3, Exercise 1–5).
- **Thuật ngữ:** cube, cube of a sum, cube of a difference.
- **Cần biết trước:** Bài 6.
- **Hình/bảng:** không bắt buộc.

### Bài 8. Tổng và hiệu hai lập phương — `g8-identities-03`
*Sum or Difference of Two Cubes*
- **NB:** phát biểu \(a^3+b^3\), \(a^3-b^3\).
- **TH:** khai triển tích \((a+b)(a^2-ab+b^2)\); viết tổng/hiệu hai lập phương thành tích.
- **VT:** rút gọn biểu thức dùng nhiều hằng đẳng thức.
- **V:** cho \(a+b=5\), \(ab=6\), tính \(a^3+b^3\); chứng minh \(a^3+b^3=(a+b)^3-3ab(a+b)\).
- **TLTA:** Lesson 8, tr. 28–29 (Example 1–3, Exercise 1–5).
- **Thuật ngữ:** sum of two cubes, difference of two cubes, write as a product.
- **Cần biết trước:** Bài 7.
- **Hình/bảng:** bảng tổng hợp 7 hằng đẳng thức đáng nhớ.

### Bài 9. Phân tích đa thức thành nhân tử — `g8-identities-04`
*Factoring Polynomials*
- **NB:** khái niệm phân tích đa thức thành nhân tử; ba phương pháp: đặt nhân tử chung, dùng hằng đẳng thức, nhóm hạng tử.
- **TH:** phân tích bằng từng phương pháp.
- **VT:** phối hợp các phương pháp; tìm \(x\) (ví dụ \(x^2-3x=0\)).
- **V:** tính nhanh giá trị biểu thức; phân tích \(x^2+5x+6\) (tách hạng tử – chỉ ở mức V, có gợi ý).
- **TLTA:** Lesson 9, tr. 30–31 (Example 1–2, Exercise 1–5).
- **Thuật ngữ:** factor (v), common factor, factor out, group terms.
- **Cần biết trước:** Bài 6–8.
- **Hình/bảng:** sơ đồ chọn phương pháp.

---

## CHƯƠNG III. TỨ GIÁC
*Quadrilaterals* · TLTA tr. 35–55 (có đáp án tr. 53) · Part 3: *Recognizing Rectangles Using Diagonals* (tr. 165) · Part 4: dự án *Designing a Quadrilateral Tiling for the School Courtyard* (tr. 181)

### Bài 10. Tứ giác — `g8-quadrilaterals-01`
*Quadrilaterals*
- **NB:** nhận biết tứ giác, tứ giác lồi; đỉnh, cạnh, đường chéo, hai đỉnh/cạnh/góc đối nhau.
- **TH:** định lí tổng các góc của tứ giác bằng \(360^\circ\).
- **VT:** tìm góc khi các góc tỉ lệ \(2:3:4:6\) hoặc cho bởi biểu thức theo \(x\).
- **V:** giải thích vì sao tứ giác không có 4 góc nhọn / 4 góc tù; góc tạo bởi hai tia phân giác; tứ giác có hai cặp cạnh kề bằng nhau.
- **TLTA:** Lesson 10, tr. 37–39 (Worked examples 1–2, Exercise 1–6).
- **Thuật ngữ:** quadrilateral, convex quadrilateral, vertex, side, interior angle, diagonal, consecutive vertices, opposite vertices / sides / angles.
- **Cần biết trước:** tổng ba góc của tam giác (lớp 7).
- **Hình/bảng:** tứ giác lồi và không lồi; đường chéo chia tứ giác thành hai tam giác.

### Bài 11. Hình thang cân — `g8-quadrilaterals-02`
*Isosceles Trapezoids*
- **NB:** nhận biết hình thang, hình thang cân, đáy, cạnh bên, đường cao.
- **TH:** tính chất: hai góc kề một cạnh bên bù nhau; hình thang cân có hai góc kề một đáy bằng nhau, hai cạnh bên bằng nhau, hai đường chéo bằng nhau.
- **VT:** tính các góc; dấu hiệu nhận biết (hai đường chéo bằng nhau).
- **V:** chứng minh tứ giác là hình thang cân; khung cầu đi bộ hình thang cân.
- **TLTA:** Lesson 11, tr. 40–42 (Worked examples 1–2, Exercise 1–6; bảng đọc kí hiệu \(\parallel\), \(\perp\)).
- **Thuật ngữ:** trapezoid, isosceles trapezoid, base, leg (of a trapezoid), height, base angle.
- **Cần biết trước:** Bài 10; hai đường thẳng song song (lớp 7).
- **Hình/bảng:** hình thang, hình thang cân có đường cao (góc vuông vẽ ô vuông).

### Bài 12. Hình bình hành — `g8-quadrilaterals-03`
*Parallelograms*
- **NB:** định nghĩa hình bình hành; các tính chất về cạnh, góc, đường chéo.
- **TH:** dấu hiệu nhận biết hình bình hành.
- **VT:** tính góc theo \(x\); chứng minh tứ giác là hình bình hành.
- **V:** chứng minh đồng quy; bệ nâng xe ô tô (giải thích vì sao sàn luôn song song mặt đất).
- **TLTA:** Lesson 12, tr. 43–45 (Worked examples 1–2, Exercise 1–7).
- **Thuật ngữ:** parallelogram, consecutive angles, midpoint, bisect, congruent segments, test for a parallelogram.
- **Cần biết trước:** Bài 10, 11; các trường hợp bằng nhau của tam giác (lớp 7).
- **Hình/bảng:** hình bình hành với hai đường chéo cắt nhau tại trung điểm.

### Bài 13. Hình chữ nhật — `g8-quadrilaterals-04`
*Rectangles*
- **NB:** định nghĩa, tính chất (hai đường chéo bằng nhau và cắt nhau tại trung điểm mỗi đường).
- **TH:** dấu hiệu nhận biết; đường trung tuyến ứng với cạnh huyền bằng nửa cạnh huyền.
- **VT:** chứng minh tứ giác là hình chữ nhật.
- **V:** kiểm tra khung cửa, sân bóng "có vuông không" bằng cách đo hai đường chéo (theo Part 3); dự án lát gạch sân trường.
- **TLTA:** Lesson 13, tr. 46–48 (Worked examples 1–2, Exercise 1–6); Part 3 (tr. 165).
- **Thuật ngữ:** rectangle, right angle, congruent diagonals, median, hypotenuse.
- **Cần biết trước:** Bài 12.
- **Hình/bảng:** hình chữ nhật và tam giác vuông với trung tuyến ứng với cạnh huyền.

### Bài 14. Hình thoi và hình vuông — `g8-quadrilaterals-05`
*Rhombi and Squares*
- **NB:** định nghĩa, tính chất hình thoi (hai đường chéo vuông góc, là phân giác các góc), hình vuông.
- **TH:** dấu hiệu nhận biết hình thoi, hình vuông.
- **VT:** tính cạnh, góc theo \(x\) (ví dụ \(WX=3x+5\), \(XY=5x-9\)); tính đoạn thẳng trên đường chéo hình vuông.
- **V:** chứng minh tứ giác là hình thoi/hình vuông qua phép đối xứng; thiết kế ô gạch lát (dự án Ch. III).
- **TLTA:** Lesson 14, tr. 49–52 (Worked examples 1–2, Exercise 1–6); Mini project Ch. III (tr. 181).
- **Thuật ngữ:** rhombus (pl. rhombi), square, congruent sides, adjacent sides, perpendicular, angle bisector.
- **Cần biết trước:** Bài 12, 13.
- **Hình/bảng:** hình thoi, hình vuông với đường chéo; sơ đồ quan hệ giữa các tứ giác.

---

## CHƯƠNG IV. ĐỊNH LÍ THALÈS
*Triangle Proportionality (Thales' Theorem)* · TLTA tr. 56–71 (có đáp án tr. 71) · Part 3: *The Triangle Midsegment Theorem* (tr. 168)

### Bài 15. Định lí Thalès trong tam giác — `g8-thales-01`
*The Triangle Proportionality Theorem*
- **NB:** tỉ số của hai đoạn thẳng; đoạn thẳng tỉ lệ; phát biểu định lí Thalès.
- **TH:** viết tỉ lệ thức từ hình; định lí Thalès đảo.
- **VT:** tính độ dài đoạn thẳng (ví dụ \(AD=6\), \(DB=4\), \(AE=7{,}5\)); chứng minh hai đường thẳng song song.
- **V:** đường thẳng song song với hai đáy hình thang; đo khoảng cách không đến được (bề rộng con sông).
- **TLTA:** Lesson 15, tr. 57–61 (Worked examples 1–2, Exercise 1–5, 7).
- **Thuật ngữ:** ratio, proportion, proportional segments, corresponding segments, Thales' theorem (Triangle Proportionality Theorem), converse, cross products.
- **Cần biết trước:** tỉ lệ thức (lớp 7); Bài 11.
- **Hình/bảng:** tam giác có \(DE\parallel BC\).

### Bài 16. Đường trung bình của tam giác — `g8-thales-02`
*Midsegments of Triangles*
- **NB:** định nghĩa đường trung bình; định lí đường trung bình.
- **TH:** tính độ dài; nhận biết trung điểm qua đường thẳng song song.
- **VT:** bài toán theo \(x\) (\(MN=2x+3\), \(KL=6x-2\)); chứng minh tứ giác là hình bình hành / hình chữ nhật.
- **V:** đo khoảng cách hai bờ hồ \(PQ\) qua trung điểm (Exercise 6); trọng tâm và đường song song.
- **TLTA:** Lesson 16, tr. 62–66 (Worked examples 1–2, Exercise 1–6); Part 3 (tr. 168).
- **Thuật ngữ:** midsegment of a triangle, endpoint, half the length, Triangle Midsegment Theorem.
- **Cần biết trước:** Bài 15.
- **Hình/bảng:** tam giác có đường trung bình; sơ đồ đo khoảng cách qua hồ.

### Bài 17. Tính chất đường phân giác của tam giác — `g8-thales-03`
*The Triangle-Angle-Bisector Theorem*
- **NB:** phát biểu tính chất \(\dfrac{BD}{DC}=\dfrac{AB}{AC}\).
- **TH:** tính tỉ số, độ dài đoạn thẳng.
- **VT:** chia cạnh đối diện theo tỉ số (\(AB=12\), \(AC=18\), \(BC=20\)); kiểm tra một đoạn có phải phân giác.
- **V:** mảnh đất tam giác chu vi 70 m, căng thước dây làm phân giác; chứng minh hệ thức với đường song song.
- **TLTA:** Lesson 17, tr. 67–70 (Worked examples 1–2, Exercise 1–7).
- **Thuật ngữ:** angle bisector (of a triangle), adjacent sides, divide in the ratio, auxiliary line, perimeter.
- **Cần biết trước:** Bài 15; tia phân giác (lớp 7).
- **Hình/bảng:** tam giác có phân giác \(AD\).

---

## CHƯƠNG V. DỮ LIỆU VÀ BIỂU ĐỒ
*Data and Charts* · TLTA tr. 72–83 (có đáp án tr. 82) · Part 3: *Continuous and Discrete Data* (tr. 170) · Part 4: *The Campus Data Detective* và *Data for a Better School* (tr. 185)

### Bài 18. Thu thập và phân loại dữ liệu — `g8-data-01`
*Collecting and Classifying Data*
- **NB:** phương pháp thu thập trực tiếp, gián tiếp; dữ liệu là số (số liệu), dữ liệu không là số.
- **TH:** phân biệt số liệu rời rạc, số liệu liên tục (đếm hay đo – theo Part 3); dữ liệu không là số có thể sắp thứ tự hay không.
- **VT:** chọn phương pháp thu thập phù hợp; đánh giá tính đại diện của mẫu.
- **V:** dự án *Campus Data Detective*: lập câu hỏi khảo sát (thời gian dùng điện thoại, thời gian xếp hàng ở căng tin), chọn cách thu thập, phân loại dữ liệu.
- **TLTA:** Lesson 18, tr. 73–75 (Example 1–2, Exercise 1–4); Part 3 (tr. 170); Mini project Ch. V (tr. 185).
- **Thuật ngữ:** collect data, classify data, direct / indirect method, quantitative (numerical) data, qualitative (non-numerical) data, discrete data, continuous data, representative, ordered.
- **Cần biết trước:** thu thập, phân loại dữ liệu (lớp 7).
- **Hình/bảng:** sơ đồ phân loại dữ liệu.

### Bài 19. Biểu diễn dữ liệu bằng bảng, biểu đồ — `g8-data-02`
*Representing Data with Tables and Charts*
- **NB:** bảng thống kê, biểu đồ tranh, biểu đồ cột, cột kép, đoạn thẳng, hình quạt tròn.
- **TH:** chọn loại biểu đồ phù hợp mục đích.
- **VT:** lập bảng từ dãy dữ liệu (câu lạc bộ R, S, M, A); chuyển bảng ↔ biểu đồ.
- **V:** chuyển dữ liệu phần trăm (400 học sinh, phương tiện đến trường) sang số lượng và biểu đồ hình quạt.
- **TLTA:** Lesson 19, tr. 76–78 (Example 1–2, Exercise 1–3).
- **Thuật ngữ:** statistical table, pictogram, column chart (bar chart), double column chart, line graph, pie chart.
- **Cần biết trước:** Bài 18; biểu đồ đoạn thẳng, hình quạt tròn (lớp 7).
- **Hình/bảng:** đủ 5 loại biểu đồ, song ngữ (dùng lại `tools/chart_g9.py`, thêm biểu đồ tranh và cột kép).

### Bài 20. Phân tích số liệu thống kê dựa vào biểu đồ — `g8-data-03`
*Analyzing Statistical Data Based on Charts*
- **NB:** đọc số liệu từ biểu đồ.
- **TH:** nhận xét xu hướng tăng, giảm; so sánh hai nhóm trên biểu đồ cột kép.
- **VT:** tính tổng, tỉ số phần trăm, mức tăng; phát hiện biểu đồ gây hiểu nhầm do chọn thang đo.
- **V:** doanh thu theo tháng (biểu đồ đoạn thẳng); khí hậu Việt Nam (trải nghiệm SGK); dự án *Data for a Better School*: đưa ra đề xuất có căn cứ.
- **TLTA:** Lesson 20, tr. 79–81 (Example 1, Exercise 1–3); Mini project (tr. 185–191).
- **Thuật ngữ:** analyze, interpret, trend, increase / decrease, scale, vertical axis, horizontal axis, misleading chart.
- **Cần biết trước:** Bài 19.
- **Hình/bảng:** biểu đồ cột kép, đoạn thẳng, hình quạt; cặp biểu đồ cùng dữ liệu khác thang đo.

---

## CHƯƠNG VI. PHÂN THỨC ĐẠI SỐ
*Algebraic Fractions* · TLTA tr. 84–96 (có đáp án cuối chương, mục lục không ghi trang) · Part 4: *Algebraic Fraction Poster Challenge* (tr. 192)

### Bài 21. Phân thức đại số — `g8-algfrac-01`
*Algebraic Fractions*
- **NB:** nhận biết phân thức, tử thức, mẫu thức.
- **TH:** điều kiện xác định; tính giá trị phân thức.
- **VT:** kiểm tra hai phân thức bằng nhau (nhân chéo).
- **V:** thời gian đi quãng đường 36 km với vận tốc \(x\) km/h viết dưới dạng phân thức (tình huống mở đầu SGK).
- **TLTA:** Lesson 21, tr. 85–87 (Example 1–2, Exercise 1–5).
- **Thuật ngữ:** algebraic fraction, numerator, denominator, defined, condition, equal algebraic fractions, substitute.
- **Cần biết trước:** Bài 2, 9; phân số (lớp 6).
- **Hình/bảng:** không bắt buộc.

### Bài 22. Tính chất cơ bản của phân thức đại số — `g8-algfrac-02`
*Fundamental Property of Algebraic Fractions*
- **NB:** phát biểu tính chất cơ bản; quy tắc đổi dấu.
- **TH:** rút gọn phân thức (phân tích tử, mẫu thành nhân tử).
- **VT:** quy đồng mẫu thức hai, ba phân thức; điền đa thức thích hợp.
- **V:** tìm lỗi sai khi "rút gọn" từng hạng tử (ví dụ \(\dfrac{x^2+2x}{3x^3+2x}=\dfrac{1}{3x}\)).
- **TLTA:** Lesson 22, tr. 88–90 (Example 1–2, Exercise 1–4).
- **Thuật ngữ:** fundamental property, simplify an algebraic fraction, common factor, common denominator, additional factor, bring to a common denominator, factorize.
- **Cần biết trước:** Bài 21.
- **Hình/bảng:** khung "3 bước quy đồng mẫu thức".

### Bài 23. Phép cộng và phép trừ phân thức đại số — `g8-algfrac-03`
*Addition and Subtraction of Algebraic Fractions*
- **NB:** quy tắc cộng, trừ cùng mẫu; phân thức đối.
- **TH:** cộng, trừ khác mẫu.
- **VT:** rút gọn biểu thức nhiều phép tính; tìm lỗi trong bài làm.
- **V:** thuyền đi xuôi 15 km rồi ngược 15 km, vận tốc dòng nước \(x\): tổng thời gian \(\dfrac{300}{100-x^2}\).
- **TLTA:** Lesson 23, tr. 91–92 (Example, Exercise 1–5).
- **Thuật ngữ:** add / subtract algebraic fractions, like denominators, unlike denominators, opposite algebraic fraction, simplify an expression.
- **Cần biết trước:** Bài 22.
- **Hình/bảng:** không bắt buộc.

### Bài 24. Phép nhân và phép chia phân thức đại số — `g8-algfrac-04`
*Multiplication and Division of Algebraic Fractions*
- **NB:** quy tắc nhân; phân thức nghịch đảo; quy tắc chia.
- **TH:** nhân, chia rồi rút gọn.
- **VT:** biến đổi biểu thức hữu tỉ nhiều phép tính.
- **V:** mô hình thu nhỏ bảng trưng bày theo tỉ lệ; vận tốc trung bình xe đạp; trả góp mua nhà (tình huống SGK).
- **TLTA:** Lesson 24, tr. 93–96 (Example 1–2, Exercise 1–4); Mini project Ch. VI (tr. 192).
- **Thuật ngữ:** product, quotient, reciprocal, cancel common factors.
- **Cần biết trước:** Bài 23.
- **Hình/bảng:** không bắt buộc.

---

## CHƯƠNG VII. PHƯƠNG TRÌNH BẬC NHẤT VÀ HÀM SỐ BẬC NHẤT
*Linear Equations and Linear Functions* · TLTA tr. 97–112 (có đáp án tr. 111) · Part 3: *Linear Equations in One Variable* (tr. 172) · Part 4: *Smart Choice* (tr. 195)

### Bài 25. Phương trình bậc nhất một ẩn — `g8-lineq-01`
*Linear Equations in One Variable*
- **NB:** nhận biết phương trình bậc nhất một ẩn \(ax+b=0\) (\(a\neq0\)); nghiệm \(x=-\dfrac{b}{a}\).
- **TH:** kiểm tra một số có là nghiệm; quy tắc chuyển vế, quy tắc nhân.
- **VT:** giải phương trình đưa được về \(ax+b=0\) (có ngoặc, có mẫu); tìm tham số để \(x=1\) là nghiệm.
- **V:** tổng ba số nguyên liên tiếp; giá vé sau khi dùng phiếu giảm giá.
- **TLTA:** Lesson 25, tr. 98–99 (Example 1–2, Exercise 1–7); Part 3 (tr. 172).
- **Thuật ngữ:** equation, linear equation in one variable, solution, solution set, solve, transpose (move a term to the other side).
- **Cần biết trước:** Bài 9; tìm \(x\) (lớp 6–7).
- **Hình/bảng:** không bắt buộc.

### Bài 26. Giải bài toán bằng cách lập phương trình — `g8-lineq-02`
*Solving Word Problems Using Equations*
- **NB:** các bước giải bài toán bằng cách lập phương trình.
- **TH:** chọn ẩn, đặt điều kiện, biểu diễn đại lượng theo ẩn.
- **VT:** bài toán số học, hình chữ nhật (chu vi 56 cm), chuyển động (xe khách – xe tải).
- **V:** năng suất (tổ may về sớm 1 ngày, làm thêm 20 áo); pha dung dịch (60% với 30% ra 300 g loại 50%); so sánh số truyện sau \(n\) tháng.
- **TLTA:** Lesson 26, tr. 100–101 (Example 1–2, Exercise 1–6).
- **Thuật ngữ:** unknown, condition, represent, set up an equation, check the answer.
- **Cần biết trước:** Bài 25.
- **Hình/bảng:** bảng phân tích đại lượng (vận tốc – thời gian – quãng đường).

### Bài 27. Khái niệm hàm số và đồ thị của hàm số — `g8-linfunc-01`
*Function and Graph of a Function*
- **NB:** khái niệm hàm số (cho bằng bảng, công thức); biến độc lập, biến phụ thuộc.
- **TH:** tính giá trị \(f(x)\); mặt phẳng tọa độ, tọa độ của điểm, góc phần tư.
- **VT:** xác định điểm trên mặt phẳng tọa độ; vẽ đồ thị hàm số cho bằng bảng.
- **V:** đọc thông tin từ đồ thị thực tế (nhiệt độ theo giờ, cước taxi).
- **TLTA:** Lesson 27, tr. 102–104 (Example 1–2, Exercise 1–4).
- **Thuật ngữ:** function, dependent / independent variable, coordinate plane, axis (pl. axes), origin, x-axis, y-axis, quadrant, coordinates, x-coordinate (abscissa), y-coordinate (ordinate), graph of a function.
- **Cần biết trước:** đại lượng tỉ lệ thuận, tỉ lệ nghịch (lớp 7).
- **Hình/bảng:** mặt phẳng tọa độ có 4 góc phần tư, các điểm \(A(-1; 2)\), \(B(3; 4)\)…

### Bài 28. Hàm số bậc nhất và đồ thị của hàm số bậc nhất — `g8-linfunc-02`
*Linear Function and Graph of a Linear Function*
- **NB:** nhận biết hàm số bậc nhất \(y=ax+b\) (\(a\neq0\)), hệ số \(a\), \(b\).
- **TH:** đồ thị là đường thẳng; vẽ đồ thị qua hai điểm (giao với hai trục).
- **VT:** tìm \(m\) để hàm số là bậc nhất / đồ thị đi qua điểm cho trước.
- **V:** chi phí phòng tập (phí đăng kí + phí hằng tháng), thuê xe theo ngày và số km, nhiệt độ lòng đất \(T=0{,}04h+15\).
- **TLTA:** Lesson 28, tr. 105–107 (Example 1–2, Exercise 1–4).
- **Thuật ngữ:** linear function, straight line, y-intercept, x-intercept, passes through.
- **Cần biết trước:** Bài 27.
- **Hình/bảng:** đồ thị \(y=2x+1\), \(y=-x+3\).

### Bài 29. Hệ số góc của đường thẳng — `g8-linfunc-03`
*Slope of a Line*
- **NB:** hệ số góc \(a\) của đường thẳng \(y=ax+b\); \(a>0\) thì góc tạo với trục \(Ox\) là góc nhọn, \(a<0\) là góc tù.
- **TH:** điều kiện hai đường thẳng song song, cắt nhau, trùng nhau.
- **VT:** tìm hàm số bậc nhất biết hệ số góc và một điểm; tìm \(m\) theo vị trí tương đối.
- **V:** dự án *Smart Choice*: so sánh hai gói dịch vụ bằng giao điểm hai đồ thị.
- **TLTA:** Lesson 29, tr. 108–110 (Example 1–2, Exercise 1–4); Mini project Ch. VII (tr. 195).
- **Thuật ngữ:** slope, acute angle, obtuse angle, relative position, parallel, intersect, coincide.
- **Cần biết trước:** Bài 28.
- **Hình/bảng:** ba vị trí tương đối của hai đường thẳng; góc tạo bởi đường thẳng và trục \(Ox\).

---

## CHƯƠNG VIII. MỞ ĐẦU VỀ TÍNH XÁC SUẤT CỦA BIẾN CỐ
*Probability* · TLTA tr. 113–119 (**không có đáp án**) · Part 4: *Build, Test and Improve a Probability Game* (tr. 199)

### Bài 30. Kết quả có thể và kết quả thuận lợi — `g8-probability-01`
*Possible Outcomes and Favorable Outcomes*
- **NB:** kết quả có thể, các kết quả đồng khả năng; biến cố; kết quả thuận lợi cho biến cố.
- **TH:** liệt kê kết quả có thể và kết quả thuận lợi (gieo xúc xắc, rút thẻ 1–12).
- **VT:** bài toán chọn sách theo thể loại, chọn chữ cái trong từ MATHEMATICS.
- **V:** gieo hai đồng xu, hai con xúc xắc (bảng cặp có thứ tự).
- **TLTA:** Lesson 30, tr. 114–115 (Example 1–2, Exercise 1–6).
- **Thuật ngữ:** possible outcome, favorable outcome, action, experiment, event, at random, list, occur, equally likely.
- **Cần biết trước:** làm quen với biến cố, xác suất (lớp 7).
- **Hình/bảng:** bảng 6 × 6 kết quả gieo hai xúc xắc.

### Bài 31. Cách tính xác suất của biến cố bằng tỉ số — `g8-probability-02`
*Calculating the Probability of an Event Using a Ratio*
- **NB:** công thức \(P(A)=\dfrac{\text{số kết quả thuận lợi}}{\text{số kết quả có thể}}\) khi các kết quả đồng khả năng.
- **TH:** tính xác suất với vòng quay 12 ô, túi bi màu.
- **VT:** thẻ đánh số 10–24, vòng quay may mắn nhiều mức điểm.
- **V:** tìm số sách ban đầu khi biết xác suất mới; tìm lỗi lập luận "3 màu nên \(P=\dfrac13\)".
- **TLTA:** Lesson 31, tr. 116–117 (Example 1–2, Exercise 1–7).
- **Thuật ngữ:** probability, ratio, total number of outcomes, spinner, prime number, perfect square.
- **Cần biết trước:** Bài 30.
- **Hình/bảng:** vòng quay chia ô đều (hình tĩnh).

### Bài 32. Mối liên hệ giữa xác suất thực nghiệm với xác suất và ứng dụng — `g8-probability-03`
*Experimental Probability, Probability and Applications*
- **NB:** xác suất thực nghiệm \(=\dfrac{\text{số lần xảy ra}}{\text{số lần thử}}\).
- **TH:** khi số lần thử lớn, xác suất thực nghiệm gần xác suất lí thuyết; ước lượng xác suất.
- **VT:** dự đoán số sản phẩm lỗi trong lô hàng; tỉ lệ ngày tắc đường.
- **V:** dự án *Probability Game*: thiết kế trò chơi, thử nghiệm, so sánh hai loại xác suất; dữ liệu gieo hai xúc xắc 100 lần → dự đoán 120 lần tiếp theo.
- **TLTA:** Lesson 32, tr. 118–119 (Example 1–2, Exercise 1–7); Mini project Ch. VIII (tr. 199).
- **Thuật ngữ:** experimental probability, trial, observation, frequency, relative frequency, estimate, predict, sample, defective.
- **Cần biết trước:** Bài 31.
- **Hình/bảng:** bảng kết quả thử nghiệm.

---

## CHƯƠNG IX. TAM GIÁC ĐỒNG DẠNG
*Similar Triangles* · TLTA tr. 120–140 (có đáp án tr. 139) · Part 2: giáo án Bài 33 · Part 3: *Angle-Angle Similarity* (tr. 174) · Part 4: *Campus Height Survey* (tr. 202)

### Bài 33. Hai tam giác đồng dạng — `g8-similar-01`
*Similar Triangles*
- **NB:** định nghĩa hai tam giác đồng dạng; kí hiệu \(\triangle ABC\backsim\triangle DEF\); tỉ số đồng dạng.
- **TH:** viết đúng thứ tự đỉnh tương ứng; tỉ số chu vi bằng tỉ số đồng dạng.
- **VT:** định lí: đường thẳng song song với một cạnh tạo ra tam giác đồng dạng; tính độ dài.
- **V:** chuỗi đường thẳng song song cắt hai cạnh (Exercise 7); tính chu vi tam giác đồng dạng.
- **TLTA:** Lesson 33, tr. 122–125 (Worked examples 1–2, Exercise 1–4, 7); Part 2 – Lesson plan (tr. 155).
- **Thuật ngữ:** similar triangles, corresponding vertices / angles / sides, proportional, similarity statement, scale factor.
- **Cần biết trước:** Bài 15.
- **Hình/bảng:** cặp tam giác đồng dạng cùng chiều, tam giác có \(NP\parallel LM\).

### Bài 34. Ba trường hợp đồng dạng của hai tam giác — `g8-similar-02`
*Proving Triangles Similar*
- **NB:** phát biểu ba trường hợp c.c.c, c.g.c, g.g.
- **TH:** chọn trường hợp phù hợp; viết kí hiệu đồng dạng.
- **VT:** chứng minh đồng dạng rồi tính cạnh (\(HJ=8\), \(HK=12\), \(LM=10\), \(LN=15\)).
- **V:** đo chiều cao vách đá bằng gương (định luật phản xạ); hệ thức với đường cao tam giác nhọn.
- **TLTA:** Lesson 34, tr. 126–129 (Worked examples 1–2, Exercise 1–5); Part 3 (tr. 174).
- **Thuật ngữ:** SSS / SAS / AA similarity, included angle.
- **Cần biết trước:** Bài 33.
- **Hình/bảng:** ba cặp tam giác minh họa ba trường hợp; sơ đồ đo bằng gương.

### Bài 35. Định lí Pythagore và ứng dụng — `g8-similar-03`
*The Pythagorean Theorem and Its Applications*
- **NB:** phát biểu định lí Pythagore, định lí đảo.
- **TH:** tính cạnh góc vuông, cạnh huyền; kiểm tra bộ ba độ dài có tạo thành tam giác vuông.
- **VT:** cạnh hình thoi từ hai đường chéo; tam giác cân biết đáy và đường cao; đường chéo hình chữ nhật.
- **V:** đường đi tắt chéo qua quảng trường 120 m × 90 m; tính \(AH, AB, AC\) khi biết \(BH=4\), \(CH=9\).
- **TLTA:** Lesson 35, tr. 130–132 (Worked examples 1–2, Exercise 1–7).
- **Thuật ngữ:** Pythagorean theorem, converse of the Pythagorean theorem, hypotenuse, leg, square root, longest side.
- **Cần biết trước:** căn bậc hai số học (lớp 7).
- **Hình/bảng:** tam giác vuông trên lưới ô vuông; quảng trường hình chữ nhật.

### Bài 36. Các trường hợp đồng dạng của hai tam giác vuông — `g8-similar-04`
*Similarity Criteria for Right Triangles*
- **NB:** hai tam giác vuông đồng dạng nếu có một góc nhọn bằng nhau / hai cạnh góc vuông tỉ lệ / cạnh huyền và cạnh góc vuông tỉ lệ.
- **TH:** chọn trường hợp, viết kí hiệu đồng dạng.
- **VT:** chứng minh \(AB^2=BH\cdot BC\); tính độ dài.
- **V:** dự án *Campus Height Survey*: đo cột cờ bằng bóng nắng; vị trí cột đỡ mái nhà; \(CM\perp DN\) trong hình vuông.
- **TLTA:** Lesson 36, tr. 133–135 (Worked examples 1–2, Exercise 1–6); Mini project Ch. IX (tr. 202).
- **Thuật ngữ:** similarity criterion, altitude, acute angle, hypotenuse-leg criterion.
- **Cần biết trước:** Bài 34, 35.
- **Hình/bảng:** tam giác vuông có đường cao ứng với cạnh huyền; sơ đồ đo bằng bóng nắng.

### Bài 37. Hình đồng dạng — `g8-similar-05`
*Similar Figures*
- **NB:** hình đồng dạng phối cảnh (tâm, tỉ số); hình đồng dạng.
- **TH:** dựng hình phóng to, thu nhỏ đoạn thẳng, tam giác từ một tâm.
- **VT:** tính \(OA'\), \(OB'\), \(OC'\) với tỉ số \(\dfrac32\); nhận biết hai hình đồng dạng.
- **V:** phóng to nhãn trang trí 12 cm × 8 cm lên rộng 21 cm; hình đồng dạng trong thực tế (bản đồ, mô hình).
- **TLTA:** Lesson 37, tr. 136–138 (Worked examples 1–2, Exercise 1–6).
- **Thuật ngữ:** similar figures, homothetic figures, center of dilation, scale factor, enlargement, reduction, corresponding lengths.
- **Cần biết trước:** Bài 33.
- **Hình/bảng:** tam giác và ảnh phóng to qua tâm \(O\).

---

## CHƯƠNG X. MỘT SỐ HÌNH KHỐI TRONG THỰC TIỄN
*Solid Shapes in Everyday Life* · TLTA tr. 141–147 (có đáp án tr. 147) · Part 4: *Pyramid Design Challenge* (tr. 177)

### Bài 38. Hình chóp tam giác đều — `g8-pyramids-01`
*Regular Triangular Pyramids*
- **NB:** nhận biết đỉnh, mặt đáy, cạnh đáy, cạnh bên, mặt bên, đường cao, trung đoạn.
- **TH:** \(S_{xq}=p\cdot d\) (\(p\): nửa chu vi đáy, \(d\): trung đoạn); \(V=\dfrac13 S\cdot h\).
- **VT:** tính diện tích xung quanh, thể tích (đáy cạnh 10 cm, cao 12 cm).
- **V:** gấp tam giác đều theo ba đường trung bình thành hình chóp; đèn trang trí hình chóp.
- **TLTA:** Lesson 38, tr. 142–144 (Worked example 1, Exercise 1–5).
- **Thuật ngữ:** regular triangular pyramid, apex, base, base edge, lateral edge, lateral face, height, foot of the height, slant height (of a pyramid), lateral area, base area, volume, semiperimeter.
- **Cần biết trước:** Bài 16, 35; hình lăng trụ đứng (lớp 7).
- **Hình/bảng:** hình chóp \(S.ABC\) có nét khuất đứt, trung đoạn; hình khai triển.

### Bài 39. Hình chóp tứ giác đều — `g8-pyramids-02`
*Regular Quadrilateral Pyramids*
- **NB:** nhận biết các yếu tố; đáy là hình vuông.
- **TH:** công thức \(S_{xq}\), \(S_{tp}\), \(V\).
- **VT:** tìm trung đoạn khi biết \(S_{xq}=96\ \text{cm}^2\), cạnh đáy 8 cm; diện tích toàn phần.
- **V:** dự án *Pyramid Design Challenge*: thiết kế hộp quà hình chóp, so sánh vật liệu và thể tích của hai phương án; kim tự tháp.
- **TLTA:** Lesson 39, tr. 145–146 (Worked examples 1–2, Exercise 1–3); Mini project (tr. 177).
- **Thuật ngữ:** regular quadrilateral pyramid (regular square pyramid), square base, total surface area.
- **Cần biết trước:** Bài 38.
- **Hình/bảng:** hình chóp \(S.ABCD\) có nét khuất đứt; hình khai triển.

---

## BẢNG TỔNG HỢP: KHÁC NHAU GIỮA TLTA VÀ SGK – ĐỀ XUẤT XỬ LÝ

Nguyên tắc: **kiến thức, kí hiệu theo SGK KNTT**; TLTA dùng cho tiếng Anh, dạng bài, tình huống.

| # | Nội dung | TLTA | SGK KNTT / web | Đề xuất xử lý |
|---|---|---|---|---|
| D1 | Tọa độ | `A(−1,2)` | `A(−1; 2)` | Dấu chấm phẩy ở mọi mức. |
| D2 | Số thập phân, tiền tệ | `0.5x²y`, `2.4x³y⁴`; 26 chỗ dùng đô la | `0,5`; đồng | Mức 1 dấu phẩy, Mức 2–3 dấu chấm; đổi sang VND. |
| D3 | Chính tả | Anh–Anh: favourable (36 lần), factorise (12), colour (5) | Web theo Anh–Mỹ | Đổi: favorable, factorize/factor, color. |
| D4 | Dấu nhân, dấu chia | `•`, `÷` | SGK: `.`, `:` | Mức 1 dùng `:` như SGK; Mức 2–3 dùng `÷` (Q10). Dấu nhân dùng \(\cdot\) ở mọi mức. |
| D5 | Bài 29 – đường thẳng vuông góc | Vocab *perpendicular*: "tích hai hệ số góc bằng −1"; câu hỏi "tìm m để hai đường thẳng vuông góc" | Không có trong Toán 8 KNTT | Không đưa vào (Q6). |
| D6 | Bài 35 – "simplest radical form" | Rút gọn căn (ví dụ \(4\sqrt2\)) | Biến đổi căn học ở lớp 9 (Bài 8–9) | Để đáp số dạng \(\sqrt{32}\) hoặc làm tròn (Q7). |
| D7 | Bài 9 – tách hạng tử | \(x^2+5x+6\) | SGK chỉ có 3 phương pháp | Chỉ ở mức V, có gợi ý. |
| D8 | Bài 32 – *relative frequency* | "tần suất" | Web lớp 9: "tần số tương đối" | Dùng "tần số tương đối" (Q5). |
| D9 | Bài 28 – *x-intercept*, *y-intercept* | "hoành độ gốc", "tung độ gốc" | Web đang dịch: "giao điểm với trục hoành / trục tung" | Giữ cách dịch của web; trong Bài 29, hệ số \(b\) gọi là "tung độ gốc" theo TLTA. |
| D10 | Bài 20 – *slope/steepness* | "độ dốc" của biểu đồ | Bài 29: slope = hệ số góc | Bài 20 chỉ dùng *steepness* (độ dốc), tránh trùng *slope*. |
| D11 | Thuật ngữ trùng chữ với web đã có | *midsegment* (web lớp 11: *midline of a triangle*); *column chart* (lớp 9: *bar chart*); *slant height* = trung đoạn (lớp 9: đường sinh); *leg* = cạnh bên hình thang (web lớp 11: *lateral edge* = cạnh bên); *Triangle Proportionality Theorem* (web lớp 11: *Thales' theorem*) | — | Từ khóa riêng có hậu tố, ví dụ "trung đoạn (hình chóp đều)", "cạnh bên (hình thang)" để bài lớp khác không bị gắn sai nghĩa (Q1–Q4). |
| D12 | Bài 37 – *dilation* | "phép phóng to hoặc thu nhỏ từ một tâm" | SGK: hình đồng dạng phối cảnh, tâm phối cảnh | Tiếng Việt theo SGK; không dạy "phép vị tự" như một phép biến hình. |
| D13 | Đáp án | Không có đáp án Ch. VIII | — | Mọi đáp án trên web đều tính lại bằng máy. |

### Lỗi phát hiện trong TLTA (không dùng nguyên văn)

| # | Vị trí | Lỗi | Sửa |
|---|---|---|---|
| E1 | Lesson 29, Example 2 | Đề cho tham số \(a\) (\(y=2ax-1\), \(y=(a+1)x-a\)) nhưng hỏi "find the value of **m**" | Hỏi theo \(a\). |
| E2 | Part 4, dự án *Pyramid Design Challenge* | Ghi "CHAPTER 1: POLYNOMIALS" | Nội dung là hình chóp đều → thuộc Ch. X. |
| E3 | Lesson 27, Key Vocabulary | "x-coordinate = hoành hộ" | **hoành độ**. |
| E4 | Lesson 7, Worked Examples | Hai ví dụ cùng đánh số "Example 2" | Đánh số lại 1–3. |
| E5 | Lesson 15 và Lesson 33, Worksheet | Đánh số nhảy (L15: Exercise 5 → 7; L33: Exercise 4 → 7) | Không ảnh hưởng nội dung; ghi số trang khi dẫn nguồn. |
| E6 | Lesson 1, Example 1 | Chữ thừa "s" trước \(\frac{5}{x}\) | Bỏ. |

Đã tính lại một số ví dụ, bài tập và đáp án TLTA (Bài 1, 2, 4, 10, 11, 12, 15, 16, 26, 31, 39): đều đúng. Khi soạn từng bài sẽ kiểm tra toàn bộ.

---

## NHỮNG ĐIỂM CẦN THẦY QUYẾT ĐỊNH

- **Q1 – *midsegment* hay *midline*.** TLTA 8 dùng *midsegment of a triangle*; web lớp 11 đang có *midline of a triangle*. Đề xuất: lớp 8 dùng *midsegment* (theo TLTA), ghi chú "also called *midline*".
- **Q2 – Tên định lí Thalès.** TLTA dùng *Triangle Proportionality Theorem*; web đang có *Thales' theorem*. Đề xuất: viết "Thales' theorem (Triangle Proportionality Theorem)" ở lần đầu, sau đó dùng *Thales' theorem*.
- **Q3 – *column chart* hay *bar chart*.** Lớp 9 trên web dùng *bar chart*. Đề xuất: lớp 8 dùng *column chart* theo TLTA, kèm "(bar chart)".
- **Q4 – *slant height*.** Hình chóp đều: trung đoạn; hình nón (lớp 9): đường sinh. Đề xuất: giữ cả hai, tách từ khóa như D11.
- **Q5 – *relative frequency*.** TLTA 8 dịch "tần suất". Đề xuất: dùng "tần số tương đối" cho thống nhất lớp 9.
- **Q6 – Hai đường thẳng vuông góc (Bài 29).** TLTA có, SGK KNTT 8 không có. Đề xuất: **bỏ**.
- **Q7 – Rút gọn căn (Bài 35).** Đề xuất: không yêu cầu rút gọn \(\sqrt{32}=4\sqrt2\) (lớp 9 mới học); đáp số chọn số đẹp hoặc làm tròn.
- **Q8 – Hình tương tác.** Lớp 9 đã chuyển sang hình tĩnh từ Bài 26. Đề xuất: lớp 8 **toàn bộ hình tĩnh**, kể cả đồ thị Bài 27–29.
- **Q9 – Nhịp soạn.** Đề xuất: soạn từ Bài 1, theo thứ tự, mỗi lần **4–5 bài** (theo chương).
- **Q10 – Dấu chia.** SGK viết \(A : B\), tiếng Anh viết \(A \div B\). Đề xuất: Mức 1 dùng ":", Mức 2–3 dùng "÷". Hay dùng ":" ở cả 3 mức cho đơn giản?
- **Q11 – Tên hình chóp tứ giác đều.** TLTA: *regular quadrilateral pyramid*; tiếng Anh thông dụng: *regular square pyramid*. Đề xuất: dùng tên TLTA, ghi chú tên còn lại.

---

## Kết quả soạn Bài 1–5 (26/11/2026) – Chương I. Đa thức

| Bài | Mã bài | Trang | Ví dụ (NB / TH / VT / V) | A / B / C | D1–D4 | Hình | Kiểm thử |
|---|---|---|---|---|---|---|---|
| 1 | `g8-polynomials-01` | `lessons/grade8/polynomials/monomials.html` | 5 (1 / 2 / 1 / 1) | 3 / 2 / 2 | 3 / 3 / 3 / 3 | — | đạt |
| 2 | `g8-polynomials-02` | `.../polynomials.html` | 5 (1 / 2 / 1 / 1) | 3 / 2 / 2 | 3 / 3 / 3 / 3 | — | đạt |
| 3 | `g8-polynomials-03` | `.../adding-subtracting-polynomials.html` | 5 (1 / 2 / 1 / 1) | 3 / 2 / 2 | 3 / 3 / 3 / 3 | — | đạt |
| 4 | `g8-polynomials-04` | `.../multiplying-polynomials.html` | 5 (1 / 2 / 1 / 1) | 3 / 2 / 2 | 3 / 3 / 3 / 3 | 1 (mô hình diện tích \((a+b)(c+d)\)) | đạt |
| 5 | `g8-polynomials-05` | `.../dividing-polynomials-by-monomials.html` | 5 (1 / 2 / 1 / 1) | 3 / 2 / 2 | 3 / 3 / 3 / 3 | — | đạt |

- Mỗi bài 19 câu × 3 mức ngôn ngữ, không câu nào trùng giữa các mức; làm đúng hết được điểm tuyệt đối ở cả 3 mức.
- Kiểm đáp án độc lập (`audit8`: đọc đề trên trang, tự phân tích công thức bằng bộ đa thức viết riêng, không dùng mã sinh câu): **285/285** câu đúng (254 câu tính tự động, 31 câu lí thuyết và bài toán thực tế kiểm bằng quy tắc riêng / đọc tay).
- Mức 1 không lẫn tiếng Anh, Mức 3 không lẫn tiếng Việt; Mức 1 dùng dấu phẩy thập phân và dấu chia ":" (theo SGK), Mức 2–3 dấu chấm và "÷" (đề xuất Q10).
- Ví dụ lấy từ TLTA Lesson 1–5 (đã đổi số liệu): đơn thức \(\dfrac34x^2y\cdot(-8)xy^3\); đa thức có hạng tử bậc cao nhất triệt tiêu; tìm đa thức \(M\); biểu thức không phụ thuộc vào biến; tìm thừa số \(A\cdot(-3xy^2)=\dots\). Bài toán thực tế: vườn có ao, diện tích các mặt chiếc hộp, lợi nhuận xưởng túi, thể tích bể nước, lãi kép 2 năm (trải nghiệm SGK), chiều dài hình chữ nhật.
- Công cụ mới: `tools/sp_g8.py` (ngân hàng câu hỏi Chương I, có lớp `Poly` tính đa thức bằng phân số). Thứ tự bài và số bài khai báo trong `config/model.json` (`lessonOrder` 10–50, `lessonNo` 1–5).
- Từ điển: các khóa dễ trùng với bài lớp khác có hậu tố "(lớp 8)" (đơn thức, đa thức, nhị thức, tam thức, hệ số tự do, đa thức không, tổng, biến, một biến, nhiều biến, chia hết cho, bỏ dấu ngoặc) để trang các lớp khác không đổi.

**Thuật ngữ mới (Bài 1–5)**

| Bài | Tiếng Anh | Tiếng Việt |
|---|---|---|
| g8-polynomials-01 | monomial; literal part; simplified monomial; like terms; degree of a monomial; one-variable; multi-variable; variable | đơn thức; phần biến; đơn thức thu gọn; đơn thức đồng dạng; bậc của đơn thức; một biến; nhiều biến; biến |
| g8-polynomials-02 | polynomial; simplified polynomial; degree of a polynomial; constant term; zero polynomial; binomial; trinomial | đa thức; đa thức thu gọn; bậc của đa thức; hệ số tự do; đa thức không; nhị thức; tam thức |
| g8-polynomials-03 | sum; commutative / associative property of addition; remove brackets | tổng; tính chất giao hoán / kết hợp của phép cộng; bỏ dấu ngoặc |
| g8-polynomials-04 | commutative / associative property of multiplication; independent of the variables | tính chất giao hoán / kết hợp của phép nhân; không phụ thuộc vào giá trị của biến |
| g8-polynomials-05 | be divisible by; exact division; dividend; divisor | chia hết cho; phép chia hết; đa thức bị chia; đơn thức chia |
