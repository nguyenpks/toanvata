# Hướng dẫn soạn, thêm và sửa nội dung bài học (mọi khối lớp)

## 1. Ba nơi cần nhớ
| Nơi | Chứa gì | Khi nào sửa |
|---|---|---|
| `content/grade<lớp>/*.py` | **Nội dung** bài học (chữ, công thức, bài tập) | Thêm bài, sửa nội dung một bài |
| `data/vocab.json` (qua `ensure_vocab` trong bài) | Từ vựng và chú thích khi bấm vào thuật ngữ | Thêm thuật ngữ mới |
| `config/model.json` | **Mô hình chung**: các mục của bài, tên mục, cấp học, màu, khung trang | Muốn đổi cách mọi bài của mọi lớp trông như thế nào |

**Không bao giờ sửa trực tiếp file trong `lessons/**/*.html` và `lessons.json`.** Hai nơi này do máy sinh ra, lần dựng sau sẽ ghi đè.

## 2. Thêm một bài mới (ví dụ lớp 7)
1. Mở Terminal trong thư mục dự án và tạo tệp nội dung trống:
   ```
   python tools/new_lesson.py g7-integers-01 "Integers" "Số nguyên" "Number Sense" "Số học"
   ```
   Tham số: mã bài, tên EN, tên VI, chủ đề EN, chủ đề VI. Mã bài phải bắt đầu `g<lớp>-` (lớp 1–12); lớp, thư mục `lessons/grade7/...` và mục trong `lessons.json` đều tự suy ra từ mã.
2. Mở `content/grade7/g7-integers-01.py` và thay phần chữ mẫu bằng nội dung thật (xem mục 4). Tham khảo bài hoàn chỉnh: `content/grade10/sets-and-intervals.py`.
3. Dựng lại:
   ```
   python tools/build_all.py
   ```
   Chỉ dựng một lớp: `python tools/build_all.py 7`.
4. Xem thử: `python -m http.server 8000` rồi mở http://localhost:8000 (chip "Lớp 7" tự sáng lên khi lớp có bài).

`order=` trong `lesson(...)` là thứ tự bài trong lớp (10, 20, 30…). Muốn chèn giữa hai bài, dùng số ở giữa (ví dụ 15).

## 3. Sửa nội dung bài đã có
1. Mở đúng tệp trong `content/grade<lớp>/` (tìm theo tên bài hoặc mã `LID`/`build('g10-sets-01', ...)`).
2. Sửa chữ, công thức, đáp án, thêm hoặc bớt câu hỏi.
3. Chạy `python tools/build_all.py` (hoặc `python tools/build_all.py 10`) rồi tải lại trang.

Các chỉnh sửa thường gặp:
- **Sửa đáp án một câu**: đổi chữ cái đáp án (`'b'`) hoặc đáp số trong lệnh `MCQ/TF/SHORT` của câu đó, và sửa lời giải đi kèm.
- **Thêm câu hỏi**: thêm một `MCQ(...)` / `TF(...)` / `SHORT(...)` vào danh sách tương ứng, đánh số tiếp theo.
- **Thêm ví dụ**: thêm `examples += EXAMPLE(4, ...)`.
- **Đổi mô tả hoặc từ khóa hiện ở danh sách bài**: sửa `description_vi=` và `tags_vi=` ở lệnh `lesson(...)` cuối tệp. Với 11 bài đã có từ trước, dữ liệu này nằm trong `content/catalog-vi.json`; thêm `description_vi`/`tags_vi` vào bài thì sẽ ưu tiên giá trị trong bài.

## 4. Quy ước viết nội dung
- Mỗi đoạn là cặp **(tiếng Anh, tiếng Việt)**: `T('English', 'Tiếng Việt')`. Danh sách là danh sách các cặp.
- **Thuật ngữ** trong tiếng Việt đặt trong `[[...]]`, ví dụ `[[tập hợp]]`; bấm vào sẽ hiện từ tiếng Anh. Thuật ngữ phải có trong từ vựng. Muốn hiện chữ khác với từ khóa: `[[đoạn|đoạn (chứa hai đầu mút)]]`.
- **Công thức**: viết trong chuỗi thô `r'...'` với **một** dấu gạch chéo: `r'\(a\in A\)'`. Công thức riêng dòng: `M(r'...')`.
- **Tiêu đề phụ** trong lý thuyết viết `<h3>5.1 ...`; số đầu tự đổi theo số mục thật của mô hình.
- **Mức 1** chỉ có tiếng Việt: câu tiếng Việt không chứa chữ tiếng Anh trong ngoặc (dùng `[[ ]]` để hiện từ Anh khi bấm). **Mức 3** chỉ có tiếng Anh: câu tiếng Anh không lẫn tiếng Việt.
- Thêm từ vựng mới ở đầu tệp:
  ```python
  ensure_vocab([
      ('v-region', 'region', 'vùng', 'Tập hợp và khoảng', 'Write a number in each region.', ''),
  ])
  load_vocab()
  ```
  (id, từ Anh, nghĩa Việt, chủ đề, câu ví dụ tiếng Anh, ký hiệu). Từ đã có sẽ được bỏ qua, nên chạy nhiều lần không sao.
- Các hàm có sẵn: `T`, `TI`, `BOX`, `UL`, `M`, `VOC`, `EXAMPLE`, `MCQ` (đáp án `'a'..'d'`; `raw=True` khi phương án là chữ), `TF` (`'true'/'false'`), `SHORT` (kiểu `number` hoặc `interval`), `REVEAL`, `FIG`, `TABLE`; thêm `TBL`, `venn2` trong `tools/mb_extra.py`.

## 4b. Đồ thị, hình học, hình 3D và bài tập riêng từng mức
- **Đồ thị tương tác**: `GRAPH({...})`; **hình học phẳng** dựng bằng quan hệ thật: `GEO({...})`; **hình không gian**: `GEO3D({...})`. Chép cấu hình mẫu từ `demo/graph-demo.html` (sinh bằng `python tools/make_graph_demo.py`) hoặc từ các bài lớp 11. Mô tả đầy đủ: `docs/GRAPH.md`.
- **Bài tập mỗi mức một bộ**: dùng `LEVEL_PRACTICE(titles, {1: S1, 2: S2, 3: S3})`. Ba bộ phải cùng dạng, cùng số nhóm và số câu, nhưng khác số liệu; mỗi mức chỉ thấy và chỉ được tính điểm bộ của mình. Xem `content/grade11/graphs-of-functions.py`.
- Chạy kiểm thử trước khi giao: `python tests/test-lessons-g11.py 11` (đổi số cuối cho lớp khác), `node tests/test-graph-core.js`.
- Trong chuỗi thô `r'...'`, **không** viết `\'` (sẽ để lại gạch chéo thừa). Viết dấu phẩy trên của đạo hàm bằng `′` (ví dụ `f′(x)`) hoặc đặt chuỗi trong `r"..."` rồi dùng `'` bình thường.

## 5. Đổi mô hình cho tất cả các lớp
Mở `config/model.json`, sửa rồi chạy `python tools/build_all.py --check` và `python tools/build_all.py`.
- **Đổi tên một mục**: sửa `en`, `vi`, `toc` của mục đó trong `sections`.
- **Đổi thứ tự mục**: đổi vị trí các khối trong `sections` (số mục tự đánh lại).
- **Thêm mục mới** (ví dụ "Thử thách"): thêm `{ "key": "extra", "type": "html", "en": "Challenge", "vi": "Thử thách", "toc": ["Challenge", "Thử thách"] }`. Bài nào có biến `extra = '...'` và truyền `extra=extra` vào `lesson(...)` thì hiện mục này, bài khác bỏ qua.
- **Ẩn một mục ở Mức 1**: đặt `"levels": [2, 3]`.
- **Ẩn mục cho cả tiểu học**: thêm tên khóa vào `hideSections` của cấp `th` trong `stages`. Cho riêng một lớp: `gradeOverrides`.
- **Đổi giao diện** (màu, nút, kiểu chấm bài): sửa `css/lesson-kit-v2.css` và `js/lesson-kit-v2.js`; không cần dựng lại.

## 6. Lỗi thường gặp
| Thông báo | Nguyên nhân | Cách xử lý |
|---|---|---|
| `thiếu mục bắt buộc "theory"` | Bài thiếu một mục `required` | Thêm nội dung cho mục đó |
| `Mã bài phải bắt đầu g<lớp>-` | Mã bài sai dạng | Dùng `g7-ten-chu-de-01` |
| `id bài học bị trùng` | Hai bài cùng mã | Đổi mã một bài |
| Công thức hiện `\\(` | Dùng hai dấu gạch trong chuỗi thô | Chỉ dùng một dấu: `r'\(x\)'` |
| Thuật ngữ `[[abc]]` hiện nguyên | Chưa khai báo trong từ vựng | Thêm vào `ensure_vocab` |
| Sửa xong không thấy đổi | Chưa chạy `build_all.py` hoặc trình duyệt giữ bộ nhớ đệm | Chạy lại, rồi Ctrl+F5 |
