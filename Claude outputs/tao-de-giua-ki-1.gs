/**
 * Tạo 3 bài kiểm tra Google Forms (Toán 10, 11, 12 – giữa học kì I).
 * Cách dùng: script.google.com → Dự án mới → dán toàn bộ tệp này → chọn hàm taoTatCa → Chạy → cấp quyền.
 * Kết quả: 3 biểu mẫu dạng bài kiểm tra (tự chấm, có lời giải), mỗi biểu mẫu có một Google Sheets nhận câu trả lời.
 * Đường link gửi học sinh hiện trong Nhật ký thực thi và trong bảng tính "Danh sách link đề giữa kì I".
 */
const DE = [
 {
  "title": "Toán 10 – Kiểm tra giữa học kì I (Kết nối tri thức)",
  "desc": "Phạm vi: Bài 1 – Bài 6 (Mệnh đề và tập hợp; Bất phương trình và hệ bất phương trình bậc nhất hai ẩn; Hệ thức lượng trong tam giác). 20 câu, mỗi câu 1 điểm.",
  "items": [
   {
    "t": "Câu 1. Mệnh đề phủ định của mệnh đề \"∀x ∈ ℝ, x² + 1 > 0\" là:",
    "o": [
     "∀x ∈ ℝ, x² + 1 < 0",
     "∀x ∈ ℝ, x² + 1 ≤ 0",
     "∃x ∈ ℝ, x² + 1 < 0",
     "∃x ∈ ℝ, x² + 1 ≤ 0"
    ],
    "c": 3,
    "e": "Phủ định của ∀ là ∃, phủ định của \">\" là \"≤\".",
    "h": "Bài 1 · Thông hiểu"
   },
   {
    "t": "Câu 2. Mệnh đề nào sau đây là mệnh đề đúng?",
    "o": [
     "∀x ∈ ℝ, x² > 0.",
     "Nếu a > b thì a² > b².",
     "∃x ∈ ℕ, x² = 2.",
     "Nếu tam giác ABC đều thì tam giác ABC cân."
    ],
    "c": 3,
    "e": "a = 1, b = −2 cho thấy B sai; x² = 2 không có nghiệm tự nhiên; x = 0 làm D sai.",
    "h": "Bài 1 · Thông hiểu"
   },
   {
    "t": "Câu 3. Cho mệnh đề P ⇒ Q: \"Nếu n chia hết cho 6 thì n chia hết cho 3\" (n ∈ ℕ). Mệnh đề đảo Q ⇒ P và tính đúng sai của nó là:",
    "o": [
     "\"Nếu n không chia hết cho 6 thì n không chia hết cho 3\" – mệnh đề sai",
     "\"n chia hết cho 3 khi và chỉ khi n chia hết cho 6\" – mệnh đề đúng",
     "\"Nếu n chia hết cho 3 thì n chia hết cho 6\" – mệnh đề đúng",
     "\"Nếu n chia hết cho 3 thì n chia hết cho 6\" – mệnh đề sai"
    ],
    "c": 3,
    "e": "Đảo của P ⇒ Q là Q ⇒ P. Với n = 3: chia hết cho 3 nhưng không chia hết cho 6, nên mệnh đề đảo sai.",
    "h": "Bài 1 · Thông hiểu"
   },
   {
    "t": "Câu 4. Cho A = [−2; 3) và B = (1; 5]. Tập hợp A ∩ B là:",
    "o": [
     "(1; 3)",
     "[1; 3)",
     "(1; 3]",
     "[−2; 5]"
    ],
    "c": 0,
    "e": "Giao là phần chung: 1 < x < 3.",
    "h": "Bài 2 · Thông hiểu"
   },
   {
    "t": "Câu 5. Cho A = {1; 2; 3; 4} và B = {2; 4; 6}. Tập hợp A \\ B là:",
    "o": [
     "{6}",
     "{1; 3; 6}",
     "{1; 3}",
     "{2; 4}"
    ],
    "c": 2,
    "e": "A \\ B gồm các phần tử thuộc A nhưng không thuộc B.",
    "h": "Bài 2 · Thông hiểu"
   },
   {
    "t": "Câu 6. Tập hợp {a; b; c} có bao nhiêu tập con (kể cả tập rỗng và chính nó)?",
    "o": [
     "3",
     "7",
     "6",
     "8"
    ],
    "c": 3,
    "e": "Tập có n phần tử có 2ⁿ tập con: 2³ = 8.",
    "h": "Bài 2 · Thông hiểu"
   },
   {
    "t": "Câu 7. Lớp 10A có 40 học sinh, trong đó 25 em thích Toán, 20 em thích Tiếng Anh và 8 em không thích môn nào trong hai môn này. Số học sinh thích cả hai môn là:",
    "o": [
     "5",
     "13",
     "17",
     "12"
    ],
    "c": 1,
    "e": "Số em thích ít nhất một môn: 40 − 8 = 32. Thích cả hai: 25 + 20 − 32 = 13.",
    "h": "Bài 2 · Vận dụng"
   },
   {
    "t": "Câu 8. Cho A = (−∞; m] và B = (2; +∞). Điều kiện của m để A ∩ B ≠ ∅ là:",
    "o": [
     "m ≤ 2",
     "m > 2",
     "m ≥ 2",
     "m < 2"
    ],
    "c": 1,
    "e": "Khi m = 2 thì A ∩ B = ∅ (B không chứa 2). Cần m > 2.",
    "h": "Bài 2 · Vận dụng"
   },
   {
    "t": "Câu 9. Cặp số nào sau đây là nghiệm của bất phương trình 2x − y + 3 > 0?",
    "o": [
     "(−1; 2)",
     "(−2; 1)",
     "(0; 0)",
     "(−3; 0)"
    ],
    "c": 2,
    "e": "Thay (0; 0): 3 > 0 đúng. Các cặp còn lại cho −2, −1, −3.",
    "h": "Bài 3 · Thông hiểu"
   },
   {
    "t": "Câu 10. Điểm nào sau đây thuộc miền nghiệm của bất phương trình x + y ≤ 4?",
    "o": [
     "(5; 0)",
     "(1; 2)",
     "(2; 3)",
     "(3; 2)"
    ],
    "c": 1,
    "e": "1 + 2 = 3 ≤ 4; các điểm còn lại cho tổng bằng 5.",
    "h": "Bài 3 · Thông hiểu"
   },
   {
    "t": "Câu 11. Điểm nào sau đây thuộc miền nghiệm của hệ bất phương trình x + y ≤ 2; x − y ≥ 0; y ≥ 0?",
    "o": [
     "(0; 1)",
     "(1; 0)",
     "(2; 1)",
     "(1; −1)"
    ],
    "c": 1,
    "e": "(1; 0) thỏa cả ba bất phương trình.",
    "h": "Bài 4 · Thông hiểu"
   },
   {
    "t": "Câu 12. Giá trị lớn nhất của F = 3x + 2y trên miền nghiệm của hệ x ≥ 0; y ≥ 0; x + y ≤ 5; x ≤ 3 là:",
    "o": [
     "13",
     "10",
     "9",
     "15"
    ],
    "c": 0,
    "e": "Các đỉnh (0;0), (3;0), (3;2), (0;5) cho F = 0; 9; 13; 10. Lớn nhất là 13.",
    "h": "Bài 4 · Vận dụng"
   },
   {
    "t": "Câu 13. Một xưởng làm bàn và ghế. Mỗi bàn cần 2 giờ công, mỗi ghế cần 1 giờ công; mỗi ngày có tối đa 10 giờ công và làm không quá 6 ghế. Lãi mỗi bàn 300 nghìn đồng, mỗi ghế 200 nghìn đồng. Lãi lớn nhất trong một ngày là:",
    "o": [
     "1,2 triệu đồng",
     "2,0 triệu đồng",
     "1,8 triệu đồng",
     "1,5 triệu đồng"
    ],
    "c": 2,
    "e": "Hệ 2x + y ≤ 10, y ≤ 6, x, y ≥ 0. Đỉnh (0;0), (5;0), (2;6), (0;6) cho lãi 0; 1,5; 1,8; 1,2 triệu.",
    "h": "Bài 4 · Vận dụng"
   },
   {
    "t": "Câu 14. Giá trị của sin 150° là:",
    "o": [
     "1/2",
     "√3/2",
     "−√3/2",
     "−1/2"
    ],
    "c": 0,
    "e": "sin 150° = sin(180° − 30°) = sin 30° = 1/2.",
    "h": "Bài 5 · Thông hiểu"
   },
   {
    "t": "Câu 15. Cho α là góc tù và sin α = 3/5. Giá trị của cos α là:",
    "o": [
     "4/5",
     "3/4",
     "−3/4",
     "−4/5"
    ],
    "c": 3,
    "e": "cos²α = 1 − 9/25 = 16/25; góc tù nên cos α < 0.",
    "h": "Bài 5 · Thông hiểu"
   },
   {
    "t": "Câu 16. Giá trị của biểu thức tan 30° · tan 60° + cos 120° là:",
    "o": [
     "1/2",
     "−1/2",
     "0",
     "3/2"
    ],
    "c": 0,
    "e": "tan 30° · tan 60° = 1; cos 120° = −1/2.",
    "h": "Bài 5 · Thông hiểu"
   },
   {
    "t": "Câu 17. Tam giác ABC có b = 3, c = 5, góc A = 120°. Độ dài cạnh a là:",
    "o": [
     "49",
     "7",
     "√19",
     "√34"
    ],
    "c": 1,
    "e": "a² = 9 + 25 − 2·3·5·cos 120° = 34 + 15 = 49.",
    "h": "Bài 6 · Thông hiểu"
   },
   {
    "t": "Câu 18. Tam giác ABC có a = 6 và góc A = 30°. Bán kính đường tròn ngoại tiếp tam giác là:",
    "o": [
     "12",
     "3",
     "6",
     "3√3"
    ],
    "c": 2,
    "e": "a / sin A = 2R ⇒ 6 / (1/2) = 2R ⇒ R = 6.",
    "h": "Bài 6 · Thông hiểu"
   },
   {
    "t": "Câu 19. Diện tích tam giác có ba cạnh 5, 6, 7 là:",
    "o": [
     "12√6",
     "36",
     "6√6",
     "6√2"
    ],
    "c": 2,
    "e": "Công thức Heron: p = 9, S = √(9·4·3·2) = √216 = 6√6.",
    "h": "Bài 6 · Vận dụng"
   },
   {
    "t": "Câu 20. Để đo khoảng cách từ điểm A trên bờ sông đến cái cây C ở bờ bên kia, người ta lấy điểm B cùng bờ với A, AB = 100 m, đo được góc CAB = 60° và góc CBA = 75°. Khoảng cách AC xấp xỉ:",
    "o": [
     "136,6 m",
     "122,5 m",
     "70,7 m",
     "193,2 m"
    ],
    "c": 0,
    "e": "Góc C = 45°. Định lí sin: AC = 100 · sin 75° / sin 45° ≈ 136,6 m.",
    "h": "Bài 6 · Vận dụng"
   }
  ]
 },
 {
  "title": "Toán 11 – Kiểm tra giữa học kì I (Kết nối tri thức)",
  "desc": "Phạm vi: Bài 1 – Bài 6 (Hàm số lượng giác và phương trình lượng giác; Dãy số; Cấp số cộng). 20 câu, mỗi câu 1 điểm.",
  "items": [
   {
    "t": "Câu 1. Góc 135° có số đo bằng radian là:",
    "o": [
     "3π/4",
     "5π/6",
     "3π/5",
     "2π/3"
    ],
    "c": 0,
    "e": "135 · π/180 = 3π/4.",
    "h": "Bài 1 · Thông hiểu"
   },
   {
    "t": "Câu 2. Cho π/2 < α < π và sin α = 4/5. Giá trị của tan α là:",
    "o": [
     "3/4",
     "−3/4",
     "4/3",
     "−4/3"
    ],
    "c": 3,
    "e": "cos α = −3/5 (góc ở góc phần tư thứ II), tan α = sin α / cos α = −4/3.",
    "h": "Bài 1 · Thông hiểu"
   },
   {
    "t": "Câu 3. Một bánh xe quay đều 3 vòng mỗi giây. Sau 2 giây, một điểm trên vành bánh xe quay được góc bao nhiêu radian?",
    "o": [
     "6π",
     "3π",
     "24π",
     "12π"
    ],
    "c": 3,
    "e": "2 giây quay 6 vòng; mỗi vòng 2π rad.",
    "h": "Bài 1 · Thông hiểu"
   },
   {
    "t": "Câu 4. Công thức nào sau đây đúng?",
    "o": [
     "cos(a − b) = cos a − cos b",
     "cos(a − b) = cos a cos b + sin a sin b",
     "cos(a − b) = sin a cos b − cos a sin b",
     "cos(a − b) = cos a cos b − sin a sin b"
    ],
    "c": 1,
    "e": "Công thức cộng: cos(a − b) = cos a cos b + sin a sin b.",
    "h": "Bài 2 · Thông hiểu"
   },
   {
    "t": "Câu 5. Giá trị của sin 75° là:",
    "o": [
     "(√3 + 1)/2",
     "(√6 − √2)/4",
     "(√6 + √2)/4",
     "(√3 + √2)/4"
    ],
    "c": 2,
    "e": "sin 75° = sin(45° + 30°) = (√2/2)(√3/2) + (√2/2)(1/2).",
    "h": "Bài 2 · Thông hiểu"
   },
   {
    "t": "Câu 6. Cho sin α = 1/3 với 0 < α < π/2. Giá trị của sin 2α là:",
    "o": [
     "2/3",
     "4√2/9",
     "2√2/9",
     "7/9"
    ],
    "c": 1,
    "e": "cos α = 2√2/3; sin 2α = 2 sin α cos α = 4√2/9.",
    "h": "Bài 2 · Vận dụng"
   },
   {
    "t": "Câu 7. Chu kì tuần hoàn của hàm số y = sin 2x là:",
    "o": [
     "4π",
     "π",
     "2π",
     "π/2"
    ],
    "c": 1,
    "e": "Chu kì của sin(ax) là 2π/|a|.",
    "h": "Bài 3 · Thông hiểu"
   },
   {
    "t": "Câu 8. Hàm số nào sau đây là hàm số chẵn?",
    "o": [
     "y = cot x",
     "y = tan x",
     "y = sin x",
     "y = cos x"
    ],
    "c": 3,
    "e": "cos(−x) = cos x.",
    "h": "Bài 3 · Thông hiểu"
   },
   {
    "t": "Câu 9. Tập xác định của hàm số y = tan x là:",
    "o": [
     "x ≠ π/2 + kπ, k ∈ ℤ",
     "x ≠ kπ, k ∈ ℤ",
     "x ≠ π/2 + k2π, k ∈ ℤ",
     "x ≠ k2π, k ∈ ℤ"
    ],
    "c": 0,
    "e": "tan x xác định khi cos x ≠ 0.",
    "h": "Bài 3 · Thông hiểu"
   },
   {
    "t": "Câu 10. Giá trị lớn nhất của hàm số y = 3 sin x − 1 là:",
    "o": [
     "2",
     "4",
     "−4",
     "3"
    ],
    "c": 0,
    "e": "−1 ≤ sin x ≤ 1 ⇒ y ≤ 3 − 1 = 2.",
    "h": "Bài 3 · Thông hiểu"
   },
   {
    "t": "Câu 11. Nghiệm của phương trình sin x = 1/2 là:",
    "o": [
     "x = π/6 + kπ",
     "x = π/6 + k2π hoặc x = 5π/6 + k2π",
     "x = ±π/6 + k2π",
     "x = ±π/3 + k2π"
    ],
    "c": 1,
    "e": "sin x = sin(π/6).",
    "h": "Bài 4 · Thông hiểu"
   },
   {
    "t": "Câu 12. Phương trình cos x = 0 có nghiệm là:",
    "o": [
     "x = kπ",
     "x = k2π",
     "x = π/2 + k2π",
     "x = π/2 + kπ"
    ],
    "c": 3,
    "e": "cos x = 0 tại các điểm π/2 + kπ.",
    "h": "Bài 4 · Thông hiểu"
   },
   {
    "t": "Câu 13. Số nghiệm của phương trình 2cos x + 1 = 0 trên đoạn [0; 2π] là:",
    "o": [
     "2",
     "1",
     "4",
     "3"
    ],
    "c": 0,
    "e": "cos x = −1/2 ⇒ x = 2π/3 hoặc x = 4π/3 trên đoạn đã cho.",
    "h": "Bài 4 · Vận dụng"
   },
   {
    "t": "Câu 14. Nghiệm của phương trình tan(x − π/4) = 1 là:",
    "o": [
     "x = π/2 + k2π",
     "x = kπ",
     "x = π/2 + kπ",
     "x = π/4 + kπ"
    ],
    "c": 2,
    "e": "x − π/4 = π/4 + kπ.",
    "h": "Bài 4 · Vận dụng"
   },
   {
    "t": "Câu 15. Độ cao (mét) của một cabin đu quay sau t phút là h(t) = 50 + 40 sin(πt/30). Lần đầu tiên (t > 0) cabin ở độ cao 70 m là sau:",
    "o": [
     "5 phút",
     "25 phút",
     "15 phút",
     "10 phút"
    ],
    "c": 0,
    "e": "sin(πt/30) = 1/2 ⇒ πt/30 = π/6 ⇒ t = 5.",
    "h": "Bài 4 · Vận dụng"
   },
   {
    "t": "Câu 16. Cho dãy số uₙ = 2n − 1. Số hạng thứ 5 của dãy là:",
    "o": [
     "11",
     "10",
     "9",
     "5"
    ],
    "c": 2,
    "e": "u₅ = 2·5 − 1 = 9.",
    "h": "Bài 5 · Thông hiểu"
   },
   {
    "t": "Câu 17. Dãy số nào sau đây là dãy số tăng?",
    "o": [
     "uₙ = 5 − 2n",
     "uₙ = (−1)ⁿ",
     "uₙ = 1/n",
     "uₙ = 3n + 1"
    ],
    "c": 3,
    "e": "uₙ₊₁ − uₙ = 3 > 0.",
    "h": "Bài 5 · Thông hiểu"
   },
   {
    "t": "Câu 18. Cấp số cộng có u₁ = 3 và công sai d = 4. Số hạng u₁₀ là:",
    "o": [
     "40",
     "39",
     "35",
     "43"
    ],
    "c": 1,
    "e": "u₁₀ = u₁ + 9d = 3 + 36.",
    "h": "Bài 6 · Thông hiểu"
   },
   {
    "t": "Câu 19. Cấp số cộng có u₁ = 2 và d = 3. Tổng 20 số hạng đầu S₂₀ là:",
    "o": [
     "1220",
     "590",
     "610",
     "630"
    ],
    "c": 2,
    "e": "S₂₀ = 20/2 · (2·2 + 19·3) = 10 · 61.",
    "h": "Bài 6 · Vận dụng"
   },
   {
    "t": "Câu 20. Một hội trường có 15 hàng ghế; hàng đầu có 20 ghế, mỗi hàng sau nhiều hơn hàng trước 2 ghế. Hội trường có tất cả bao nhiêu ghế?",
    "o": [
     "480",
     "300",
     "510",
     "540"
    ],
    "c": 2,
    "e": "S₁₅ = 15/2 · (2·20 + 14·2) = 7,5 · 68 = 510.",
    "h": "Bài 6 · Vận dụng"
   }
  ]
 },
 {
  "title": "Toán 12 – Kiểm tra giữa học kì I (Kết nối tri thức)",
  "desc": "Phạm vi: Bài 1 – Bài 5 (Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số). 20 câu, mỗi câu 1 điểm.",
  "items": [
   {
    "t": "Câu 1. Hàm số y = x³ − 3x + 2 nghịch biến trên khoảng nào?",
    "o": [
     "(1; +∞)",
     "(−∞; +∞)",
     "(−1; 1)",
     "(−∞; −1)"
    ],
    "c": 2,
    "e": "y′ = 3x² − 3 < 0 ⇔ −1 < x < 1.",
    "h": "Bài 1 · Thông hiểu"
   },
   {
    "t": "Câu 2. Khẳng định nào đúng về hàm số y = (2x + 1)/(x − 1)?",
    "o": [
     "Nghịch biến trên ℝ",
     "Đồng biến trên từng khoảng (−∞; 1) và (1; +∞)",
     "Nghịch biến trên từng khoảng (−∞; 1) và (1; +∞)",
     "Đồng biến trên ℝ"
    ],
    "c": 2,
    "e": "y′ = −3/(x − 1)² < 0 với mọi x ≠ 1.",
    "h": "Bài 1 · Thông hiểu"
   },
   {
    "t": "Câu 3. Hàm số y = x³ − 3x² + 1 đạt cực đại tại:",
    "o": [
     "x = 2",
     "x = 1",
     "x = −2",
     "x = 0"
    ],
    "c": 3,
    "e": "y′ = 3x² − 6x = 0 ⇔ x = 0 hoặc x = 2; y′ đổi dấu từ + sang − tại x = 0.",
    "h": "Bài 1 · Thông hiểu"
   },
   {
    "t": "Câu 4. Giá trị cực tiểu của hàm số y = x⁴ − 2x² + 3 là:",
    "o": [
     "1",
     "2",
     "3",
     "−1"
    ],
    "c": 1,
    "e": "y′ = 4x³ − 4x; cực tiểu tại x = ±1, y = 1 − 2 + 3 = 2.",
    "h": "Bài 1 · Thông hiểu"
   },
   {
    "t": "Câu 5. Tất cả giá trị của m để hàm số y = x³ − 3mx² + 3x + 1 đồng biến trên ℝ là:",
    "o": [
     "m ≤ −1 hoặc m ≥ 1",
     "m ≥ 1",
     "−1 < m < 1",
     "−1 ≤ m ≤ 1"
    ],
    "c": 3,
    "e": "y′ = 3x² − 6mx + 3 ≥ 0 với mọi x ⇔ Δ′ = 9m² − 9 ≤ 0.",
    "h": "Bài 1 · Vận dụng"
   },
   {
    "t": "Câu 6. Giá trị lớn nhất của hàm số y = x³ − 3x + 1 trên đoạn [0; 2] là:",
    "o": [
     "1",
     "2",
     "−1",
     "3"
    ],
    "c": 3,
    "e": "y(0) = 1, y(1) = −1, y(2) = 3.",
    "h": "Bài 2 · Thông hiểu"
   },
   {
    "t": "Câu 7. Giá trị nhỏ nhất của hàm số y = x + 4/x trên khoảng (0; +∞) là:",
    "o": [
     "4",
     "2",
     "5",
     "0"
    ],
    "c": 0,
    "e": "y′ = 1 − 4/x² = 0 ⇔ x = 2; y(2) = 4.",
    "h": "Bài 2 · Thông hiểu"
   },
   {
    "t": "Câu 8. Từ một tấm bìa hình vuông cạnh 12 cm, người ta cắt ở bốn góc bốn hình vuông bằng nhau cạnh x cm rồi gấp thành hộp không nắp. Thể tích lớn nhất của hộp là:",
    "o": [
     "100 cm³",
     "108 cm³",
     "128 cm³",
     "144 cm³"
    ],
    "c": 2,
    "e": "V = x(12 − 2x)², 0 < x < 6; V′ = 0 ⇔ x = 2; V(2) = 128.",
    "h": "Bài 2 · Vận dụng"
   },
   {
    "t": "Câu 9. Lợi nhuận của một cơ sở khi bán x trăm sản phẩm là P(x) = −x² + 40x − 100 (triệu đồng). Để lợi nhuận lớn nhất, cơ sở cần bán:",
    "o": [
     "2000 sản phẩm",
     "1000 sản phẩm",
     "300 sản phẩm",
     "4000 sản phẩm"
    ],
    "c": 0,
    "e": "P′(x) = −2x + 40 = 0 ⇔ x = 20 (trăm sản phẩm).",
    "h": "Bài 2 · Vận dụng"
   },
   {
    "t": "Câu 10. Tiệm cận đứng của đồ thị hàm số y = (2x − 1)/(x + 3) là:",
    "o": [
     "x = −3",
     "x = 3",
     "x = 1/2",
     "y = 2"
    ],
    "c": 0,
    "e": "Mẫu bằng 0 tại x = −3, tử khác 0.",
    "h": "Bài 3 · Thông hiểu"
   },
   {
    "t": "Câu 11. Tiệm cận ngang của đồ thị hàm số y = (3x + 1)/(x − 2) là:",
    "o": [
     "x = 2",
     "y = 2",
     "y = 3",
     "y = −1/2"
    ],
    "c": 2,
    "e": "Giới hạn của y khi x → ±∞ bằng 3.",
    "h": "Bài 3 · Thông hiểu"
   },
   {
    "t": "Câu 12. Tiệm cận xiên của đồ thị hàm số y = (x² + x + 1)/(x − 1) là:",
    "o": [
     "y = x + 1",
     "y = x + 2",
     "y = x",
     "y = x − 2"
    ],
    "c": 1,
    "e": "x² + x + 1 = (x − 1)(x + 2) + 3 nên y = x + 2 + 3/(x − 1).",
    "h": "Bài 3 · Thông hiểu"
   },
   {
    "t": "Câu 13. Đồ thị hàm số y = (x + 1)/(x² − 1) có tổng số đường tiệm cận đứng và tiệm cận ngang là:",
    "o": [
     "3",
     "1",
     "2",
     "4"
    ],
    "c": 2,
    "e": "y = 1/(x − 1) với x ≠ −1: chỉ có tiệm cận đứng x = 1 (tại x = −1 không có tiệm cận) và tiệm cận ngang y = 0.",
    "h": "Bài 3 · Vận dụng"
   },
   {
    "t": "Câu 14. Đồ thị hàm số y = x³ − 3x + 2 cắt trục tung tại điểm:",
    "o": [
     "(0; −2)",
     "(0; 2)",
     "(2; 0)",
     "(1; 0)"
    ],
    "c": 1,
    "e": "Thay x = 0.",
    "h": "Bài 4 · Thông hiểu"
   },
   {
    "t": "Câu 15. Tâm đối xứng của đồ thị hàm số y = (x + 1)/(x − 2) là điểm:",
    "o": [
     "I(2; −1)",
     "I(1; 2)",
     "I(−2; 1)",
     "I(2; 1)"
    ],
    "c": 3,
    "e": "Tâm đối xứng là giao của tiệm cận đứng x = 2 và tiệm cận ngang y = 1.",
    "h": "Bài 4 · Thông hiểu"
   },
   {
    "t": "Câu 16. Số giao điểm của đồ thị hàm số y = x³ − 3x với đường thẳng y = 1 là:",
    "o": [
     "3",
     "2",
     "0",
     "1"
    ],
    "c": 0,
    "e": "Giá trị cực đại 2 và cực tiểu −2; đường thẳng y = 1 nằm giữa nên cắt 3 điểm.",
    "h": "Bài 4 · Vận dụng"
   },
   {
    "t": "Câu 17. Tất cả giá trị của m để phương trình x³ − 3x + 2 = m có ba nghiệm phân biệt là:",
    "o": [
     "m > 4",
     "0 < m < 4",
     "0 ≤ m ≤ 4",
     "m < 0"
    ],
    "c": 1,
    "e": "Hàm số có giá trị cực đại 4 (tại x = −1) và cực tiểu 0 (tại x = 1).",
    "h": "Bài 4 · Vận dụng"
   },
   {
    "t": "Câu 18. Một vật chuyển động theo quy luật s(t) = t³ − 6t² + 9t (mét, t tính bằng giây). Vận tốc của vật tại thời điểm t = 2 là:",
    "o": [
     "2 m/s",
     "−3 m/s",
     "3 m/s",
     "0 m/s"
    ],
    "c": 1,
    "e": "v(t) = s′(t) = 3t² − 12t + 9; v(2) = −3.",
    "h": "Bài 5 · Thông hiểu"
   },
   {
    "t": "Câu 19. Số dân của một thị trấn sau t năm là N(t) = 1000 + 30t² − t³ (người), 0 ≤ t ≤ 30. Tốc độ tăng dân số N′(t) lớn nhất tại thời điểm:",
    "o": [
     "t = 5",
     "t = 20",
     "t = 30",
     "t = 10"
    ],
    "c": 3,
    "e": "N′(t) = 60t − 3t² đạt lớn nhất tại t = 10.",
    "h": "Bài 5 · Vận dụng"
   },
   {
    "t": "Câu 20. Chi phí sản xuất x sản phẩm là C(x) = x² + 100 (nghìn đồng). Để chi phí trung bình mỗi sản phẩm nhỏ nhất, cần sản xuất:",
    "o": [
     "10 sản phẩm",
     "100 sản phẩm",
     "20 sản phẩm",
     "5 sản phẩm"
    ],
    "c": 0,
    "e": "Chi phí trung bình C(x)/x = x + 100/x nhỏ nhất khi x = 10.",
    "h": "Bài 5 · Vận dụng"
   }
  ]
 }
];

function taoTatCa() {
  const tong = SpreadsheetApp.create('Danh sách link đề giữa kì I');
  const sh = tong.getActiveSheet();
  sh.appendRow(['Khối', 'Link gửi học sinh', 'Link chỉnh sửa', 'Bảng tính câu trả lời']);
  DE.forEach(function (de) {
    const form = FormApp.create(de.title);
    form.setDescription(de.desc)
        .setIsQuiz(true)
        .setCollectEmail(false)
        .setLimitOneResponsePerUser(false)
        .setProgressBar(true)
        .setConfirmationMessage('Em đã nộp bài. Bấm "Xem điểm" để xem kết quả và lời giải.');
    form.addTextItem().setTitle('Họ và tên').setRequired(true);
    form.addTextItem().setTitle('Lớp').setRequired(true);
    de.items.forEach(function (q) {
      const it = form.addMultipleChoiceItem();
      it.setTitle(q.t).setHelpText(q.h).setPoints(1).setRequired(true);
      it.setChoices(q.o.map(function (o, i) { return it.createChoice(o, i === q.c); }));
      it.setFeedbackForCorrect(FormApp.createFeedback().setText('Đúng. ' + q.e).build());
      it.setFeedbackForIncorrect(FormApp.createFeedback().setText('Đáp án: ' + q.o[q.c] + '. ' + q.e).build());
    });
    const ss = SpreadsheetApp.create('Câu trả lời – ' + de.title);
    form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());
    sh.appendRow([de.title, form.getPublishedUrl(), form.getEditUrl(), ss.getUrl()]);
    Logger.log(de.title + '\n  Gửi học sinh: ' + form.getPublishedUrl() + '\n  Chỉnh sửa: ' + form.getEditUrl());
  });
  Logger.log('Bảng tổng hợp link: ' + tong.getUrl());
}
