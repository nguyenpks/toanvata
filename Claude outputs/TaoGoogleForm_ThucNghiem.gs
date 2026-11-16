/**
 * TẠO 4 GOOGLE FORM KIỂM TRA THỰC NGHIỆM (Toán 10 và Toán 11, mỗi khối đề A và đề B)
 * Cách dùng: dán toàn bộ vào script.google.com (Dự án mới) -> chọn hàm taoFormThucNghiem -> Chạy -> Cấp quyền.
 * Sau khi học sinh làm xong: chạy hàm tongHopDiem để lập bảng điểm trước - sau và thống kê.
 */
var CFG = {
 "10A": {
  "grade": 10,
  "ver": "A",
  "topic": "Vectơ (Bài 7–11)",
  "vi": [
   {
    "stem": "Cho vectơ a = (6, 8). Độ dài của vectơ a là:",
    "opts": [
     "14",
     "10",
     "100",
     "48"
    ],
    "ans": 1
   },
   {
    "stem": "Trung điểm của đoạn thẳng AB với A(2, 4) và B(6, 10) có tọa độ là:",
    "opts": [
     "(8, 14)",
     "(2, 3)",
     "(4, 6)",
     "(4, 7)"
    ],
    "ans": 3
   },
   {
    "stem": "Cho ABCD là hình bình hành (các đại lượng dưới đây đều là vectơ). Khi đó AB + AD bằng:",
    "opts": [
     "AC",
     "BD",
     "CA",
     "DB"
    ],
    "ans": 0
   },
   {
    "stem": "Cho a = (2, −1) và b = (3, 5). Tọa độ của vectơ 2a + b là:",
    "opts": [
     "(5, 4)",
     "(1, −7)",
     "(7, 3)",
     "(7, −3)"
    ],
    "ans": 2
   },
   {
    "stem": "Cho a = (m, 3) và b = (2, 4). Hai vectơ a và b vuông góc với nhau khi m bằng:",
    "opts": [
     "6",
     "−2",
     "2",
     "−6"
    ],
    "ans": 3
   },
   {
    "stem": "Góc giữa hai vectơ a = (1, 0) và b = (1, 1) bằng:",
    "opts": [
     "30°",
     "45°",
     "60°",
     "90°"
    ],
    "ans": 1
   },
   {
    "stem": "Tam giác ABC có A(0, 0), B(6, 0), C(0, 9). Tọa độ trọng tâm G của tam giác là:",
    "opts": [
     "(3; 4,5)",
     "(6; 9)",
     "(2; 3)",
     "(2; 4,5)"
    ],
    "ans": 2
   },
   {
    "stem": "Cho hình bình hành ABCD có A(1, 1), B(3, 2), C(5, 5). Tọa độ đỉnh D là:",
    "opts": [
     "(3, 4)",
     "(7, 6)",
     "(1, 2)",
     "(3, 2)"
    ],
    "ans": 0
   },
   {
    "stem": "Hai vectơ a = (2, m) và b = (1, 3) cùng phương khi m bằng:",
    "opts": [
     "3",
     "6",
     "2/3",
     "−6"
    ],
    "ans": 1
   },
   {
    "stem": "Gọi I là trung điểm của đoạn thẳng AB và M là điểm bất kì (các đại lượng dưới đây đều là vectơ). Khi đó MA + MB bằng:",
    "opts": [
     "MI",
     "2IM",
     "AB",
     "2MI"
    ],
    "ans": 3
   },
   {
    "stem": "Gọi G là trọng tâm của tam giác ABC (các đại lượng dưới đây đều là vectơ). Khi đó GA + GB + GC bằng:",
    "opts": [
     "3GA",
     "GA",
     "vectơ-không",
     "AG"
    ],
    "ans": 2
   },
   {
    "stem": "Cho a = (1, 2) và b = (2, 2). Độ dài của vectơ a + b là:",
    "opts": [
     "5",
     "7",
     "25",
     "1"
    ],
    "ans": 0
   },
   {
    "stem": "Cho |a| = 3, |b| = 4 và góc giữa hai vectơ a, b bằng 60°. Tích vô hướng a · b bằng:",
    "opts": [
     "12",
     "6√3",
     "3",
     "6"
    ],
    "ans": 3
   },
   {
    "stem": "Cho hai vectơ bằng nhau (x + 1; 3) = (4; y − 2). Giá trị của x + y là:",
    "opts": [
     "7",
     "8",
     "9",
     "3"
    ],
    "ans": 1
   },
   {
    "stem": "Hai vectơ a và b khác vectơ-không thỏa mãn a · b = −|a|·|b|. Góc giữa a và b bằng:",
    "opts": [
     "180°",
     "0°",
     "90°",
     "135°"
    ],
    "ans": 0
   }
  ],
  "en": [
   {
    "stem": "The English term \"opposite vector\" means:",
    "opts": [
     "vectơ-không",
     "vectơ bằng nhau",
     "vectơ đối",
     "vectơ cùng hướng"
    ],
    "ans": 2
   },
   {
    "stem": "Which English term means \"vectơ đơn vị\"?",
    "opts": [
     "zero vector",
     "unit vector",
     "opposite vector",
     "position vector"
    ],
    "ans": 1
   },
   {
    "stem": "Given A(1, 2) and B(4, 6). The coordinates of vector AB are:",
    "opts": [
     "(5, 8)",
     "(−3, −4)",
     "(4, 3)",
     "(3, 4)"
    ],
    "ans": 3
   },
   {
    "stem": "Given a = (2, 3) and b = (4, −1). The dot product a · b equals:",
    "opts": [
     "5",
     "11",
     "−5",
     "(8, −3)"
    ],
    "ans": 0
   },
   {
    "stem": "A force of 8 N moves an object 5 m along a straight line. The angle between the force and the displacement is 60°. The work done by the force is:",
    "opts": [
     "40 J",
     "34.6 J",
     "20 J",
     "10 J"
    ],
    "ans": 2
   }
  ]
 },
 "10B": {
  "grade": 10,
  "ver": "B",
  "topic": "Vectơ (Bài 7–11)",
  "vi": [
   {
    "stem": "Cho vectơ a = (5, 12). Độ dài của vectơ a là:",
    "opts": [
     "17",
     "169",
     "13",
     "60"
    ],
    "ans": 2
   },
   {
    "stem": "Trung điểm của đoạn thẳng AB với A(−2, 6) và B(8, 2) có tọa độ là:",
    "opts": [
     "(3, 4)",
     "(6, 8)",
     "(5, −2)",
     "(−5, 2)"
    ],
    "ans": 0
   },
   {
    "stem": "Cho MNPQ là hình bình hành (các đại lượng dưới đây đều là vectơ). Khi đó MN + MQ bằng:",
    "opts": [
     "NQ",
     "PM",
     "QN",
     "MP"
    ],
    "ans": 3
   },
   {
    "stem": "Cho a = (1, 3) và b = (4, −2). Tọa độ của vectơ 3a + b là:",
    "opts": [
     "(5, 1)",
     "(7, 7)",
     "(−1, 11)",
     "(7, 1)"
    ],
    "ans": 1
   },
   {
    "stem": "Cho a = (m, 5) và b = (3, 6). Hai vectơ a và b vuông góc với nhau khi m bằng:",
    "opts": [
     "−10",
     "10",
     "−2,5",
     "2,5"
    ],
    "ans": 0
   },
   {
    "stem": "Góc giữa hai vectơ a = (1, 0) và b = (1, √3) bằng:",
    "opts": [
     "30°",
     "45°",
     "60°",
     "90°"
    ],
    "ans": 2
   },
   {
    "stem": "Tam giác ABC có A(0, 0), B(3, 0), C(0, 12). Tọa độ trọng tâm G của tam giác là:",
    "opts": [
     "(1,5; 6)",
     "(1; 4)",
     "(3; 12)",
     "(1; 6)"
    ],
    "ans": 1
   },
   {
    "stem": "Cho hình bình hành ABCD có A(0, 2), B(2, 3), C(5, 6). Tọa độ đỉnh D là:",
    "opts": [
     "(7, 7)",
     "(3, 3)",
     "(1, 2)",
     "(3, 5)"
    ],
    "ans": 3
   },
   {
    "stem": "Hai vectơ a = (4, m) và b = (2, 5) cùng phương khi m bằng:",
    "opts": [
     "5",
     "2,5",
     "10",
     "−10"
    ],
    "ans": 2
   },
   {
    "stem": "Gọi K là trung điểm của đoạn thẳng CD và O là điểm bất kì (các đại lượng dưới đây đều là vectơ). Khi đó OC + OD bằng:",
    "opts": [
     "2OK",
     "OK",
     "2KO",
     "CD"
    ],
    "ans": 0
   },
   {
    "stem": "Gọi G là trọng tâm của tam giác MNP (các đại lượng dưới đây đều là vectơ). Khi đó GM + GN + GP bằng:",
    "opts": [
     "3GM",
     "vectơ-không",
     "GM",
     "MG"
    ],
    "ans": 1
   },
   {
    "stem": "Cho a = (2, 5) và b = (3, 7). Độ dài của vectơ a + b là:",
    "opts": [
     "17",
     "169",
     "7",
     "13"
    ],
    "ans": 3
   },
   {
    "stem": "Cho |a| = 4, |b| = 5 và góc giữa hai vectơ a, b bằng 60°. Tích vô hướng a · b bằng:",
    "opts": [
     "10",
     "20",
     "10√3",
     "9"
    ],
    "ans": 0
   },
   {
    "stem": "Cho hai vectơ bằng nhau (x − 2; 5) = (1; y + 1). Giá trị của x + y là:",
    "opts": [
     "6",
     "8",
     "7",
     "5"
    ],
    "ans": 2
   },
   {
    "stem": "Hai vectơ a và b khác vectơ-không thỏa mãn a · b = |a|·|b|. Góc giữa a và b bằng:",
    "opts": [
     "180°",
     "90°",
     "45°",
     "0°"
    ],
    "ans": 3
   }
  ],
  "en": [
   {
    "stem": "The English term \"zero vector\" means:",
    "opts": [
     "vectơ đối",
     "vectơ-không",
     "vectơ đơn vị",
     "số không"
    ],
    "ans": 1
   },
   {
    "stem": "Which English term means \"ba điểm thẳng hàng\"?",
    "opts": [
     "collinear vectors",
     "midpoint",
     "collinear points",
     "centroid"
    ],
    "ans": 2
   },
   {
    "stem": "Given A(2, −1) and B(6, 2). The coordinates of vector AB are:",
    "opts": [
     "(4, 3)",
     "(8, 1)",
     "(−4, −3)",
     "(3, 4)"
    ],
    "ans": 0
   },
   {
    "stem": "Given a = (5, 2) and b = (3, −4). The dot product a · b equals:",
    "opts": [
     "23",
     "−7",
     "(15, −8)",
     "7"
    ],
    "ans": 3
   },
   {
    "stem": "A force of 6 N moves an object 10 m along a straight line. The angle between the force and the displacement is 60°. The work done by the force is:",
    "opts": [
     "60 J",
     "30 J",
     "52 J",
     "15 J"
    ],
    "ans": 1
   }
  ]
 },
 "11A": {
  "grade": 11,
  "ver": "A",
  "topic": "Dãy số – Cấp số cộng – Cấp số nhân",
  "vi": [
   {
    "stem": "Dãy số (uₙ) có số hạng tổng quát uₙ = 3n − 2. Giá trị của u₅ là:",
    "opts": [
     "15",
     "13",
     "17",
     "11"
    ],
    "ans": 1
   },
   {
    "stem": "Dãy số (uₙ) xác định bởi u₁ = 2 và uₙ₊₁ = uₙ + 3. Giá trị của u₄ là:",
    "opts": [
     "14",
     "8",
     "9",
     "11"
    ],
    "ans": 3
   },
   {
    "stem": "Dãy số nào sau đây là dãy số giảm?",
    "opts": [
     "uₙ = 1/n",
     "uₙ = n²",
     "uₙ = 2n",
     "uₙ = (−1)ⁿ"
    ],
    "ans": 0
   },
   {
    "stem": "Cấp số cộng có số hạng đầu u₁ = 5 và công sai d = 3. Số hạng thứ mười u₁₀ là:",
    "opts": [
     "35",
     "30",
     "32",
     "27"
    ],
    "ans": 2
   },
   {
    "stem": "Cấp số cộng có u₃ = 11 và u₇ = 23. Công sai d bằng:",
    "opts": [
     "4",
     "12",
     "2",
     "3"
    ],
    "ans": 3
   },
   {
    "stem": "Cấp số nhân có số hạng đầu u₁ = 2 và công bội q = 3. Số hạng thứ năm u₅ là:",
    "opts": [
     "486",
     "162",
     "30",
     "54"
    ],
    "ans": 1
   },
   {
    "stem": "Cấp số nhân có u₁ = 1 và q = 2. Tổng của 4 số hạng đầu là:",
    "opts": [
     "16",
     "8",
     "15",
     "31"
    ],
    "ans": 2
   },
   {
    "stem": "Dãy số nào sau đây là cấp số cộng?",
    "opts": [
     "2, 5, 8, 11, …",
     "1, 2, 4, 8, …",
     "1, 3, 6, 10, …",
     "2, 4, 8, 14, …"
    ],
    "ans": 0
   },
   {
    "stem": "Dãy số nào sau đây là cấp số nhân?",
    "opts": [
     "3, 6, 9, 12, …",
     "3, 6, 12, 24, …",
     "1, 4, 9, 16, …",
     "2, 3, 5, 8, …"
    ],
    "ans": 1
   },
   {
    "stem": "Cấp số cộng (uₙ) có u₅ = 17 và công sai d = 3. Số hạng đầu u₁ là:",
    "opts": [
     "2",
     "8",
     "20",
     "5"
    ],
    "ans": 3
   },
   {
    "stem": "Cho cấp số cộng 3, 7, 11, … Số 43 là số hạng thứ mấy của cấp số cộng này?",
    "opts": [
     "10",
     "12",
     "11",
     "14"
    ],
    "ans": 2
   },
   {
    "stem": "Cấp số nhân (uₙ) có u₂ = 6 và u₃ = 18. Công bội q bằng:",
    "opts": [
     "3",
     "12",
     "2",
     "1/3"
    ],
    "ans": 0
   },
   {
    "stem": "Dãy số nào sau đây là dãy số bị chặn?",
    "opts": [
     "uₙ = n²",
     "uₙ = 2ⁿ",
     "uₙ = 3n + 1",
     "uₙ = (−1)ⁿ"
    ],
    "ans": 3
   },
   {
    "stem": "Cấp số cộng có u₁ = 1 và d = 2. Tổng của 20 số hạng đầu là:",
    "opts": [
     "420",
     "400",
     "800",
     "200"
    ],
    "ans": 1
   },
   {
    "stem": "Ba số 2, x, 10 theo thứ tự lập thành cấp số cộng. Giá trị của x là:",
    "opts": [
     "6",
     "5",
     "8",
     "20"
    ],
    "ans": 0
   }
  ],
  "en": [
   {
    "stem": "The English term \"common difference\" means:",
    "opts": [
     "công bội",
     "tỉ số",
     "công sai",
     "số hạng đầu"
    ],
    "ans": 2
   },
   {
    "stem": "Which English term means \"cấp số nhân\"?",
    "opts": [
     "arithmetic sequence",
     "geometric sequence",
     "finite sequence",
     "bounded sequence"
    ],
    "ans": 1
   },
   {
    "stem": "A bank account has 100 million VND with compound interest of 10% per year. After 2 years (no withdrawals), the balance is:",
    "opts": [
     "120 million VND",
     "110 million VND",
     "122 million VND",
     "121 million VND"
    ],
    "ans": 3
   },
   {
    "stem": "An arithmetic sequence has u₁ = 2 and d = 3. The sum of the first 10 terms is:",
    "opts": [
     "155",
     "310",
     "145",
     "150"
    ],
    "ans": 0
   },
   {
    "stem": "The numbers 2, x, 18 are consecutive terms of a geometric sequence with x > 0. The value of x is:",
    "opts": [
     "10",
     "9",
     "6",
     "36"
    ],
    "ans": 2
   }
  ]
 },
 "11B": {
  "grade": 11,
  "ver": "B",
  "topic": "Dãy số – Cấp số cộng – Cấp số nhân",
  "vi": [
   {
    "stem": "Dãy số (uₙ) có số hạng tổng quát uₙ = 4n − 3. Giá trị của u₆ là:",
    "opts": [
     "24",
     "25",
     "21",
     "17"
    ],
    "ans": 2
   },
   {
    "stem": "Dãy số (uₙ) xác định bởi u₁ = 3 và uₙ₊₁ = uₙ + 4. Giá trị của u₄ là:",
    "opts": [
     "15",
     "19",
     "12",
     "16"
    ],
    "ans": 0
   },
   {
    "stem": "Dãy số nào sau đây là dãy số giảm?",
    "opts": [
     "uₙ = n + 3",
     "uₙ = 2ⁿ",
     "uₙ = (−1)ⁿ · n",
     "uₙ = 8 − n"
    ],
    "ans": 3
   },
   {
    "stem": "Cấp số cộng có số hạng đầu u₁ = 7 và công sai d = 4. Số hạng thứ mười u₁₀ là:",
    "opts": [
     "47",
     "43",
     "40",
     "36"
    ],
    "ans": 1
   },
   {
    "stem": "Cấp số cộng có u₂ = 9 và u₆ = 25. Công sai d bằng:",
    "opts": [
     "4",
     "5",
     "16",
     "3"
    ],
    "ans": 0
   },
   {
    "stem": "Cấp số nhân có số hạng đầu u₁ = 5 và công bội q = 2. Số hạng thứ năm u₅ là:",
    "opts": [
     "160",
     "50",
     "80",
     "25"
    ],
    "ans": 2
   },
   {
    "stem": "Cấp số nhân có u₁ = 2 và q = 3. Tổng của 4 số hạng đầu là:",
    "opts": [
     "54",
     "80",
     "26",
     "160"
    ],
    "ans": 1
   },
   {
    "stem": "Dãy số nào sau đây là cấp số cộng?",
    "opts": [
     "1, 2, 4, 8, …",
     "3, 5, 8, 12, …",
     "2, 4, 7, 11, …",
     "3, 7, 11, 15, …"
    ],
    "ans": 3
   },
   {
    "stem": "Dãy số nào sau đây là cấp số nhân?",
    "opts": [
     "2, 6, 10, 14, …",
     "1, 4, 9, 16, …",
     "2, 6, 18, 54, …",
     "1, 3, 6, 10, …"
    ],
    "ans": 2
   },
   {
    "stem": "Cấp số cộng (uₙ) có u₅ = 19 và công sai d = 4. Số hạng đầu u₁ là:",
    "opts": [
     "3",
     "4",
     "7",
     "23"
    ],
    "ans": 0
   },
   {
    "stem": "Cho cấp số cộng 5, 8, 11, … Số 38 là số hạng thứ mấy của cấp số cộng này?",
    "opts": [
     "11",
     "12",
     "13",
     "10"
    ],
    "ans": 1
   },
   {
    "stem": "Cấp số nhân (uₙ) có u₂ = 5 và u₃ = 20. Công bội q bằng:",
    "opts": [
     "15",
     "5",
     "1/4",
     "4"
    ],
    "ans": 3
   },
   {
    "stem": "Dãy số nào sau đây là dãy số bị chặn?",
    "opts": [
     "uₙ = 2 + (−1)ⁿ",
     "uₙ = n + 5",
     "uₙ = 4ⁿ",
     "uₙ = n²"
    ],
    "ans": 0
   },
   {
    "stem": "Cấp số cộng có u₁ = 3 và d = 2. Tổng của 20 số hạng đầu là:",
    "opts": [
     "420",
     "880",
     "440",
     "220"
    ],
    "ans": 2
   },
   {
    "stem": "Ba số 4, x, 14 theo thứ tự lập thành cấp số cộng. Giá trị của x là:",
    "opts": [
     "8",
     "10",
     "18",
     "9"
    ],
    "ans": 3
   }
  ],
  "en": [
   {
    "stem": "The English term \"common ratio\" means:",
    "opts": [
     "công sai",
     "công bội",
     "tỉ lệ tăng trưởng",
     "số hạng đầu"
    ],
    "ans": 1
   },
   {
    "stem": "Which English term means \"cấp số cộng\"?",
    "opts": [
     "geometric sequence",
     "infinite sequence",
     "arithmetic sequence",
     "bounded sequence"
    ],
    "ans": 2
   },
   {
    "stem": "A bank account has 50 million VND with compound interest of 20% per year. After 2 years (no withdrawals), the balance is:",
    "opts": [
     "72 million VND",
     "70 million VND",
     "60 million VND",
     "75 million VND"
    ],
    "ans": 0
   },
   {
    "stem": "An arithmetic sequence has u₁ = 3 and d = 2. The sum of the first 10 terms is:",
    "opts": [
     "240",
     "110",
     "21",
     "120"
    ],
    "ans": 3
   },
   {
    "stem": "The numbers 4, x, 36 are consecutive terms of a geometric sequence with x > 0. The value of x is:",
    "opts": [
     "20",
     "12",
     "16",
     "144"
    ],
    "ans": 1
   }
  ]
 }
};

var PART1 = 'PHẦN I. BÀI TOÁN BẰNG TIẾNG VIỆT (Câu 1–15)';
var PART2 = 'PHẦN II. THUẬT NGỮ VÀ BÀI TOÁN BẰNG TIẾNG ANH (Câu 16–20)';
var F_MA = 'Mã học sinh';
var F_LAN = 'Lần làm bài';
var LAN_TRUOC = 'Trước thực nghiệm';
var LAN_SAU = 'Sau thực nghiệm';
var LETTERS = ['A', 'B', 'C', 'D'];

function taoFormThucNghiem() {
  var ss = SpreadsheetApp.create('Thực nghiệm sư phạm – Bảng tổng hợp');
  var props = PropertiesService.getScriptProperties();
  var linkSheet = ss.getSheets()[0];
  linkSheet.setName('Link_form');
  linkSheet.appendRow(['Khối', 'Đề', 'Link cho học sinh', 'Link chỉnh sửa', 'Mã form']);
  Object.keys(CFG).forEach(function (k) {
    var c = CFG[k];
    var form = FormApp.create('Toán ' + c.grade + ' – ' + c.topic + ' – Bài kiểm tra Đề ' + c.ver);
    form.setIsQuiz(true);
    form.setCollectEmail(false);
    form.setShowLinkToRespondAgain(false);
    form.setProgressBar(true);
    form.setDescription('Thời gian làm bài: 25 phút. Gồm 20 câu trắc nghiệm, mỗi câu 0,5 điểm (tối đa 10 điểm): 15 câu bằng tiếng Việt và 5 câu bằng tiếng Anh. ' +
      'Mỗi câu chỉ có một đáp án đúng. Không dùng tài liệu, không tra từ điển. Điền đúng Mã học sinh để ghép điểm trước – sau.');
    form.setConfirmationMessage('Em đã nộp bài. Cảm ơn em!');

    form.addTextItem().setTitle('Họ và tên').setRequired(true);
    form.addTextItem().setTitle('Lớp').setRequired(true);
    form.addTextItem().setTitle(F_MA).setHelpText('Mã do giáo viên cấp, ví dụ: 10A1-05. Mỗi học sinh dùng cùng một mã cho cả hai lần làm.').setRequired(true);
    form.addMultipleChoiceItem().setTitle(F_LAN).setChoiceValues([LAN_TRUOC, LAN_SAU]).setRequired(true);

    var n = 0;
    form.addSectionHeaderItem().setTitle(PART1);
    c.vi.forEach(function (q) { n++; addQ(form, n, q); });
    form.addSectionHeaderItem().setTitle(PART2);
    c.en.forEach(function (q) { n++; addQ(form, n, q); });

    form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());
    props.setProperty('form_' + k, form.getId());
    linkSheet.appendRow([c.grade, c.ver, form.getPublishedUrl(), form.getEditUrl(), form.getId()]);
  });
  props.setProperty('ss_id', ss.getId());
  Logger.log('Bảng tổng hợp: ' + ss.getUrl());
  Logger.log('Mở sheet "Link_form" trong bảng tổng hợp để lấy link 4 form.');
}

function addQ(form, n, q) {
  var item = form.addMultipleChoiceItem();
  item.setTitle('Câu ' + n + '. ' + q.stem);
  item.setChoices(q.opts.map(function (t, i) {
    return item.createChoice(LETTERS[i] + '. ' + t, i === q.ans);
  }));
  item.setPoints(0.5);
  item.setRequired(true);
}

/** Lập bảng điểm trước – sau cho từng khối và thống kê (trung bình, độ lệch chuẩn, p-value, kích thước hiệu ứng). */
function tongHopDiem() {
  var props = PropertiesService.getScriptProperties();
  var ss = SpreadsheetApp.openById(props.getProperty('ss_id'));
  [10, 11].forEach(function (grade) {
    var rec = {};   // ma -> {ten, lop, truoc, sau, de}
    ['A', 'B'].forEach(function (ver) {
      var form = FormApp.openById(props.getProperty('form_' + grade + ver));
      form.getResponses().forEach(function (r) {
        var ma = '', ten = '', lop = '', lan = '';
        r.getItemResponses().forEach(function (ir) {
          var t = ir.getItem().getTitle();
          if (t === F_MA) ma = String(ir.getResponse()).trim().toUpperCase();
          else if (t === 'Họ và tên') ten = String(ir.getResponse()).trim();
          else if (t === 'Lớp') lop = String(ir.getResponse()).trim();
          else if (t === F_LAN) lan = String(ir.getResponse());
        });
        if (!ma) return;
        var score = 0;
        r.getGradableItemResponses().forEach(function (g) { score += (g.getScore() || 0); });
        if (!rec[ma]) rec[ma] = { ten: ten, lop: lop, truoc: '', sau: '', de: '' };
        if (lan === LAN_TRUOC) { rec[ma].truoc = score; rec[ma].de = ver; }
        else if (lan === LAN_SAU) { rec[ma].sau = score; }
      });
    });
    var name = 'Khoi_' + grade;
    var sh = ss.getSheetByName(name);
    if (sh) ss.deleteSheet(sh);
    sh = ss.insertSheet(name);
    var full = [], missing = [];
    Object.keys(rec).sort().forEach(function (ma) {
      var x = rec[ma];
      if (x.truoc !== '' && x.sau !== '') full.push([ma, x.ten, x.lop, x.de, x.truoc, x.sau]);
      else missing.push([ma, x.ten, x.lop, x.truoc, x.sau]);
    });
    sh.getRange(1, 1, 1, 7).setValues([['Mã HS', 'Họ tên', 'Lớp', 'Đề làm trước', 'Điểm trước', 'Điểm sau', 'Chênh lệch']]).setFontWeight('bold');
    var n = full.length;
    if (n > 0) {
      sh.getRange(2, 1, n, 6).setValues(full);
      var f = [];
      for (var i = 0; i < n; i++) f.push(['=F' + (i + 2) + '-E' + (i + 2)]);
      sh.getRange(2, 7, n, 1).setFormulas(f);
      var e = 'E2:E' + (n + 1), g = 'F2:F' + (n + 1), h = 'G2:G' + (n + 1), d = 'D2:D' + (n + 1);
      var S = [
        ['THỐNG KÊ', ''],
        ['Số học sinh có đủ hai điểm (N)', '=COUNT(' + e + ')'],
        ['Điểm trung bình trước', '=ROUND(AVERAGE(' + e + '),2)'],
        ['Điểm trung bình sau', '=ROUND(AVERAGE(' + g + '),2)'],
        ['Độ lệch chuẩn trước', '=ROUND(STDEV(' + e + '),2)'],
        ['Độ lệch chuẩn sau', '=ROUND(STDEV(' + g + '),2)'],
        ['Chênh lệch trung bình (sau − trước)', '=ROUND(AVERAGE(' + h + '),2)'],
        ['Giá trị p (t ghép cặp, hai phía)', '=IF(COUNT(' + e + ')>1,TEXT(T.TEST(' + e + ',' + g + ',2,1),"0.0000"),"")'],
        ['Kích thước hiệu ứng d (chênh lệch TB / ĐLC chênh lệch)', '=IF(STDEV(' + h + ')>0,ROUND(AVERAGE(' + h + ')/STDEV(' + h + '),2),"")'],
        ['Tỉ lệ học sinh tăng điểm', '=TEXT(COUNTIF(' + h + ',">0")/COUNT(' + h + '),"0%")'],
        ['Tỉ lệ học sinh giữ nguyên', '=TEXT(COUNTIF(' + h + ',0)/COUNT(' + h + '),"0%")'],
        ['Tỉ lệ học sinh giảm điểm', '=TEXT(COUNTIF(' + h + ',"<0")/COUNT(' + h + '),"0%")'],
        ['Chênh lệch TB – nhóm làm đề A trước', '=IFERROR(ROUND(AVERAGEIF(' + d + ',"A",' + h + '),2),"")'],
        ['Chênh lệch TB – nhóm làm đề B trước', '=IFERROR(ROUND(AVERAGEIF(' + d + ',"B",' + h + '),2),"")']
      ];
      sh.getRange(1, 9, S.length, 2).setValues(S.map(function (r) { return [r[0], '']; }));
      for (var k = 1; k < S.length; k++) sh.getRange(k + 1, 10).setFormula(S[k][1]);
      sh.getRange(1, 9).setFontWeight('bold');
      sh.setColumnWidth(9, 380);
      // Biểu đồ cột: trung bình trước/sau
      var chart = sh.newChart().setChartType(Charts.ChartType.COLUMN)
        .addRange(sh.getRange('I3:J4'))
        .setPosition(17, 9, 0, 0)
        .setOption('title', 'Điểm trung bình trước và sau thực nghiệm – Toán ' + grade)
        .setOption('legend', { position: 'none' })
        .setOption('vAxis', { minValue: 0, maxValue: 10 })
        .build();
      sh.insertChart(chart);
    }
    if (missing.length) {
      var r0 = n + 4;
      sh.getRange(r0, 1).setValue('Học sinh thiếu một trong hai điểm (không đưa vào thống kê)').setFontWeight('bold');
      sh.getRange(r0 + 1, 1, 1, 5).setValues([['Mã HS', 'Họ tên', 'Lớp', 'Điểm trước', 'Điểm sau']]).setFontWeight('bold');
      sh.getRange(r0 + 2, 1, missing.length, 5).setValues(missing);
    }
    sh.setFrozenRows(1);
  });
  Logger.log('Đã lập bảng điểm: ' + ss.getUrl());
}
