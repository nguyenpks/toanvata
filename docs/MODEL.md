# Mô hình bài học dùng chung cho mọi khối lớp (1–12)

**Một mô hình – nhiều lớp.** Bài học = *nội dung* (theo từng lớp) + *mô hình* (một nơi duy nhất).

| Muốn đổi… | Sửa ở đâu | Rồi chạy |
|---|---|---|
| Số mục, thứ tự, tên mục (EN/VI), mục nào ẩn ở Mức 1 | `config/model.json` → `sections` | `python tools/build_all.py` |
| Cấp học, lớp thuộc cấp nào, màu, mô tả (cả trang chủ) | `config/model.json` → `stages` | không cần dựng lại (trang tự đọc) |
| Ngoại lệ cho riêng một cấp/lớp (ẩn mục) | `hideSections` trong `stages` hoặc `gradeOverrides` | `build_all.py` |
| Tên 3 mức học, tên các ô thông tin đầu bài | `levels`, `meta` | `build_all.py` |
| Khung HTML của trang bài, CSS/JS nạp vào | `config/page-template.html`, `page` trong `model.json` | `build_all.py` |
| Giao diện/hành vi bài (màu, nút, chấm bài, 3 mức) | `css/lesson-kit-v2.css`, `js/lesson-kit-v2.js` | không cần (các bài nạp chung) |

## Thêm nội dung một lớp
```
python tools/new_lesson.py g5-fractions-01 "Fractions" "Phân số" "Number Sense" "Số học"
# điền nội dung trong content/grade5/g5-fractions-01.py (xem content/_TEMPLATE.py)
python tools/build_all.py
```
Lớp suy ra từ mã bài (`g5-` = lớp 5). Bài tự được ghi vào `lessons.json` đúng lớp, đúng thứ tự (`order`), đúng thư mục `lessons/grade5/...`.

## Quy tắc
- Nội dung **không** chứa số mục, tên mục, số lớp hay khung trang. Tiêu đề phụ viết `<h3>5.1 …` sẽ tự đánh số lại theo mô hình.
- Mục không bắt buộc mà bài không có nội dung thì bị bỏ qua; mục `required` thiếu thì dựng báo lỗi rõ ràng.
- `levels` của một mục: `[1,2,3]` hiện ở mọi mức (mặc định), `[2,3]` ẩn ở Mức 1, các tổ hợp khác dùng lớp `lv-only-…`.
- Mỗi lần sửa mô hình, chạy `python tools/build_all.py --check` để kiểm tra rồi `python tools/build_all.py`.
- Bài mẫu cũ chưa chuyển (`g11-functions-01`) được giữ nguyên trong `lessons.json` cho đến khi viết lại bằng mô hình mới.

## Ví dụ đã chuyển
- Lớp 10: 3 bài (`content/grade10/`). Lớp 12: 7 bài (`content/grade12/`). Cách soạn chi tiết: `docs/HUONG-DAN-SOAN-BAI.md`.
