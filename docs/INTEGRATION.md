# Quy chuẩn tích hợp bài học (dành cho AI số 2)

AI số 2 chỉ cần tạo **file bài học HTML** và **thêm một mục vào `lessons.json`**. Không sửa `index.html`, `js/`, `css/style.css`.

## 1. Mục trong lessons.json
`lessons.json` là một **mảng** các đối tượng. Giữ nguyên tên và kiểu trường:

| Trường | Kiểu | Ghi chú |
|---|---|---|
| id | string | Duy nhất, dạng `g10-algebra-01` |
| grade | number | Từ 1 đến 12 (số, không đặt trong ngoặc kép). Tiểu học: 1–5; THCS: 6–9; THPT: 10–12 |
| category | string | Chủ đề, ví dụ `Algebra` |
| title | string | Tên bài (tiếng Anh) |
| description | string | Mô tả ngắn |
| level | string | `Beginner`, `Intermediate` hoặc `Advanced` |
| estimatedMinutes | number | Số phút |
| prerequisites | array of string | Danh sách `id` bài cần học trước, có thể rỗng `[]` |
| path | string | Đường dẫn file bài học **tính từ thư mục gốc website** |
| tags | array of string | Từ khóa tìm kiếm |

Thứ tự trong mảng quyết định thứ tự bài trước/sau trong cùng một lớp.

## 2. Đường dẫn và thư mục
`lessons/grade<1…12>/<category-viet-thuong>/<ten-file>.html`
Ví dụ: `lessons/grade10/algebra/introduction.html`. Đường dẫn trong `path` phải khớp chính xác tên file.

## 3. Khung file bài học
Sao chép một bài mẫu trong `lessons/` và chỉ đổi nội dung trong `<article>`. Bắt buộc giữ:
- `<body data-lesson-id="...">` trùng `id` trong lessons.json
- `css/lesson.css` (đường dẫn tương đối, từ `lessons/gradeX/cat/` là `../../../css/lesson.css`)
- `js/mathjax-config.js` và dòng nạp MathJax
- Hai script cuối trang: `js/progress.js`, `js/lesson-bridge.js`

## 4. Công thức Toán
Trong dòng: `\( ... \)`. Riêng dòng: `\[ ... \]`. Không dùng `$...$`.

## 5. Ghi nhận hoàn thành
Bài học **không tự ghi hoàn thành**. Nút "Tôi đã học xong bài này" (từ `lesson-bridge.js`) và nút trên trang cha chỉ hoạt động khi học sinh bấm.
- Trong iframe: bài gửi `postMessage({type:'mathbridge:lesson-complete', lessonId}, location.origin)`. Trang cha chỉ nhận khi đúng origin, đúng iframe và đúng `lessonId` đang mở.
- Mở bài riêng: ghi thẳng LocalStorage khóa `mathbridge_progress`, chỉ khi cùng origin với website.
- **Giới hạn:** bài học đặt ở tên miền khác (khác origin) sẽ không gửi được thông điệp và không dùng chung LocalStorage. Mọi bài phải nằm trong cùng website. Mở bằng `file://` không dùng được `postMessage` đúng cách; hãy dùng máy chủ tĩnh.

## 6. Kiểm tra trước khi bàn giao
JSON hợp lệ, `id` không trùng, `path` mở được, công thức hiển thị, nút hoàn thành chạy được.

## 7. Bổ sung của AI số 2 (không thay đổi quy chuẩn ở trên)
- Thêm hai file dùng chung: `css/lesson-kit.css` (lớp có tiền tố `mbl-`) và `js/lesson-kit.js`. Bài học nạp `lesson-kit.css` sau `lesson.css`, và `lesson-kit.js` **giữa** `progress.js` và `lesson-bridge.js`.
- `lesson-kit.js` không dùng LocalStorage và không ghi hoàn thành; nó chỉ chấm câu hỏi, hiện/ẩn lời giải và tự đặt chiều cao iframe (vì `app.js` chỉ đặt chiều cao một lần lúc tải).
- Đáp án nằm trong thuộc tính `data-answer` của mã nguồn trang: học sinh biết xem mã nguồn vẫn thấy được. Chấp nhận ở mức bài luyện tập, không dùng để thi.

## 8. Ba mức ngôn ngữ trong bài học (AI số 2)
- Mức 1: toàn tiếng Việt; thuật ngữ đặt trong ngoặc kép (`<abbr class="mbl-term" data-en="set">“tập hợp”</abbr>`), rê chuột/chạm/Tab hiện từ tiếng Anh. Đề bài tập trộn từ tiếng Anh (`<span class="mx">`). Mức 2: tiếng Anh kèm bản dịch (`.en` + `.vi`). Mức 3: chỉ tiếng Anh.
- Mở khóa lần lượt: hoàn thành bài tập của mức hiện tại (làm hết các câu chấm điểm, đạt từ 80%) thì mở mức kế tiếp. Mỗi lần đổi mức, bài tập được làm mới.
- Trạng thái mở khóa chỉ nằm trong bộ nhớ trang, **không** lưu LocalStorage (để không phá khóa `mathbridge_progress`). Tải lại trang thì quay về Mức 1. Muốn lưu lâu dài cần AI số 1 bổ sung khóa chung.

## Lưu ý về màu (cập nhật)
Các biến CSS trong `css/lesson.css` giữ nguyên tên nhưng giá trị đã đổi sang tông xanh lá. Khi vẽ SVG, dùng #046B4D (nét, điểm), #D5F3E4 (tô nhạt), #86E0BD (nhấn), #123428 (chữ).

## 9. Ba mức học tập v2 – áp dụng cho mọi bài mới từ lớp 12 (thay thế mục 8 cho bài mới)
Theo quy định Phần III–V. Bài mới nạp `css/lesson-kit-v2.css` (sau `lesson.css`) và `js/lesson-kit-v2.js` (giữa `progress.js` và `lesson-bridge.js`). **Không nạp cùng lúc bản v1 và v2.**
- **Lưu mức học:** LocalStorage khóa `mathbridge_learning_mode`, giá trị `level1` | `level2` | `level3`. Không có khóa nào khác. Chưa có thiết lập chung của AI số 1, nên khóa này do `lesson-kit-v2.js` tạo và đọc; nếu AI số 1 bổ sung sau, dùng đúng khóa này.
- **Chuyển mức tự do, không khóa, không làm mới bài tập:** đổi mức không xóa bài đã nhập, không đổi đáp án/điểm, giữ vị trí đang đọc, thanh chọn mức luôn nằm trong tầm nhìn.
- **Mức 1:** chỉ `.vi`; thuật ngữ quan trọng in đậm `<b class="mbl-term" tabindex="0" data-en="Function">Hàm số</b>`; rê chuột / chạm / focus bàn phím hiện tooltip chỉ gồm từ tiếng Anh; không có ngoặc đơn hay chú thích tiếng Anh.
- **Mức 2:** `.en` + nút `🌐 VI` cho từng khối `.tx`; bản dịch `.vi` nền pastel, ẩn mặc định, bấm lần nữa để ẩn, các khối độc lập.
- **Mức 3:** chỉ `.en`; không có nút dịch, bản dịch hay tooltip; nút chức năng bằng tiếng Anh (Check Answer, Show Solution, Hide Solution, Try Again, Submit, Your Score, Correct, Incorrect, Complete Lesson). Thanh điều hướng của nền tảng vẫn là tiếng Việt.
- **Cách viết bài:** dùng `tools/mb_lib.py`. Mỗi đoạn viết một lần dạng `T(en, vi)`; thuật ngữ trong tiếng Việt viết `[[tiệm cận đứng]]`, thư viện tra `data/vocab.json` để gắn từ tiếng Anh duy nhất (lỗi nếu thuật ngữ chưa có). Công thức nằm ngoài khối ngôn ngữ nên ba mức dùng chung. Chạy `python tools/g12_asymptotes.py` để tạo lại bài mẫu.
- Bài lớp 10 `g10-sets-01` đã được chuyển từ bộ v1 sang bộ v2 (cùng id, cùng đường dẫn). Bộ v1 (`lesson-kit.css/js`) không còn bài nào dùng nhưng vẫn giữ trong thư mục, chưa xóa.

## 10. Phát âm tiếng Anh (bài v2)
- **Bấm thuật ngữ:** Mức 1 – bấm/chạm/nhấn Enter vào thuật ngữ in đậm: hiện tooltip và đọc từ tiếng Anh. Mức 2 và 3 – bấm từ in đậm ở mục Từ vựng (có biểu tượng 🔊) để nghe.
- **Đọc cả câu:** Mức 2 và 3 – nút 🔊 cạnh mỗi đoạn tiếng Anh; bấm lần nữa để dừng. Mức 1 không có nút này (nội dung tiếng Việt).
- **Công thức được đọc thành lời:** `mb_lib.say_text()` đổi \( … \) thành tiếng Anh (vd. `\frac{a}{b}` → "a over b", `f'(x)` → "f prime of x", `x^2` → "x squared") và lưu ở thuộc tính `data-say` của đoạn. Có thể sửa cách đọc bằng cách chỉnh `speak_math()`.
- **Công nghệ:** Web Speech API (giọng en-US có sẵn trên thiết bị, tốc độ 0,9). Chất lượng phụ thuộc giọng đọc của hệ điều hành/trình duyệt; thiết bị không hỗ trợ thì các nút 🔊 tự ẩn. Muốn phát âm thống nhất tuyệt đối, cần ghi âm sẵn file âm thanh (chưa làm).

## 11. Ba cấp học và trang chủ (cập nhật theo yêu cầu)
- Trang chủ chia ba cấp: Tiểu học (lớp 1–5), Trung học cơ sở (lớp 6–9), Trung học phổ thông (lớp 10–12). Khai báo `STAGES` ở đầu `js/app.js`. Lớp chưa có bài hiện nhãn "sắp có". Trang Chương trình học có bộ lọc Cấp học và Khối lớp (`#/courses?stage=th|thcs|thpt` hoặc `?grade=N`).
- Đã bỏ mục "Thuật ngữ Toán học" khỏi trang chủ (trang `#/vocab` và menu vẫn giữ).
- Hình Toán học nền chìm (đồ thị, hình không gian, công thức) sinh bằng `python tools/make_art.py` vào `js/art.js`; chỉnh độ đậm trong `css/style.css` (`.home-art svg`, `.hero-art svg`, `.stage-art`).
- Lưu ý: đợt này có sửa `index.html`, `js/app.js`, `css/style.css` theo yêu cầu trực tiếp của người dùng (trái với quy ước ban đầu cho AI số 2).

## Công cụ sinh bài lớp 10 (cập nhật)
- `tools/mb_std.py`: hàm `build(..., grade=12)` và `ENTRY(..., grade=12)` nay nhận tham số `grade`; mặc định 12 nên các bài lớp 12 không đổi.
- `tools/mb_extra.py`: `TBL` (bảng), `FIGR` (hình có sẵn nhãn), `venn2` (biểu đồ Venn hai tập), `reorder` (sắp xếp bài trong lessons.json).
- `tools/g10_vocab.py`: từ vựng bổ sung của lớp 10 (ghi vào `data/vocab.json`).
- `tools/g10_sets01.py`, `g10_sets02.py`, `g10_algebra01.py`, `g10_finalize.py`: sinh các bài lớp 10. Chạy từ thư mục `tools/`: `python g10_sets01.py` rồi `python g10_finalize.py`.
- Cú pháp thuật ngữ trong bản tiếng Việt: `[[chữ hiển thị|khóa]]`, khóa là cột `vi` trong `vocab.json`.

## Hiển thị bằng tiếng Việt (cập nhật)
- Tên hiển thị của website là **ToánvàTA**. Các khóa kỹ thuật (`mathbridge_progress`, `mathbridge_learning_mode`, `mathbridge:lesson-complete`) giữ nguyên để không mất tiến độ đã lưu.
- Trong `lessons.json`, giá trị của `title`, `description`, `category` và `tags` được viết bằng **tiếng Việt** (tên trường và kiểu dữ liệu không đổi). Nội dung song ngữ nằm trong từng bài học, chọn bằng ba mức học.
- Khi thêm bài mới: thêm một mục vào `CATALOG` trong `tools/vi_catalog.py`, rồi chạy `python vi_catalog.py` trong thư mục `tools`. Hàm `build()` cũng tự áp dụng danh mục này.

## 12. Mô hình bài học dùng chung (mọi khối lớp)
Bố cục bài học nằm ở `config/model.json` và `config/page-template.html`; nội dung từng lớp nằm ở `content/grade<lớp>/*.py`. Dựng tất cả: `python tools/build_all.py`. Hướng dẫn: `docs/MODEL.md`, `docs/HUONG-DAN-SOAN-BAI.md`.
- Các script `tools/g10_*.py`, `tools/g12_*.py`, `tools/vi_catalog.py`, `tools/g10_finalize.py` đã được thay bằng `content/` và `config/model.json`; kết quả 11 bài hiện có **giống hệt từng byte** trước khi chuyển.
- Tiêu đề, chủ đề, mô tả, từ khóa trong `lessons.json` hiển thị bằng tiếng Việt (`catalog.language = "vi"` trong `model.json`).
- AI số 2 thêm bài mới bằng `python tools/new_lesson.py ...`, không tạo script sinh bài riêng và không sửa trực tiếp HTML.

## 13. Đồ thị, hình vẽ và bài tập theo mức (lớp 11 trở đi)
- Mọi đồ thị và hình vẽ Toán học dùng `GRAPH`, `GEO`, `GEO3D` (JSXGraph, `docs/GRAPH.md`); **không** tự vẽ SVG/Canvas thủ công cho hình cần chính xác toán học. Quan hệ vuông góc, song song, phân giác, tiếp tuyến phải dựng bằng bước hình học thật (`perpendicular`, `parallel`, `bisector`, `tangent`...), không vẽ theo cảm tính.
- Đồ thị phải ngắt nhánh tại tiệm cận và điểm gián đoạn (lõi `mb-graph-core.js` đã lo); khi có tiệm cận hãy khai báo `asymptotes` để hiện đường nét đứt.
- Bài tập của ba mức là **ba bộ khác nhau, cùng dạng** (`LEVEL_PRACTICE`), không dịch lại cùng một câu. Phần lý thuyết và ví dụ dùng chung cho cả ba mức.
- Mỗi bài lớp 11 có ghi chú kiểm tra số liệu (assert) ở đầu tệp nội dung; bài mới nên làm tương tự.
