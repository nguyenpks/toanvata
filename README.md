# TOÁN VÀ TIẾNG ANH – Toán thật dễ, Tiếng Anh thật hay

Website tĩnh: HTML, CSS, JavaScript thuần, MathJax (nạp từ CDN, cần Internet), LocalStorage.

## Cấu trúc thư mục
```
toanvata/
├─ index.html          (khung trang, điều hướng theo #/)
├─ lessons.json        (danh mục bài học)
├─ css/  style.css, lesson.css
├─ js/   app.js, art.js (hình nền), progress.js, lesson-bridge.js, mathjax-config.js
├─ data/ vocab.json    (từ vựng mẫu)
├─ lessons/grade10|11|12/<chủ đề>/*.html   (bài mẫu kiểm thử)
├─ config/ model.json (MÔ HÌNH DUY NHẤT), page-template.html
├─ content/grade1…12/*.py (chỉ nội dung bài), catalog-vi.json, _TEMPLATE.py
├─ js/ mb-graph-core.js, mb-graph.js (đồ thị/hình vẽ JSXGraph) · css/mb-graph.css · demo/graph-demo.html · tests/
├─ tools/ mb_model.py (bộ dựng), build_all.py, new_lesson.py, mb_lib.py, mb_std.py, mb_extra.py
└─ docs/ HUONG-DAN-SOAN-BAI.md (cách soạn/sửa nội dung), GRAPH.md (đồ thị và hình vẽ), MODEL.md, INTEGRATION.md (quy chuẩn cho AI số 2)
```

## Chạy website (Windows)
Không mở trực tiếp index.html (trình duyệt chặn đọc JSON). Chạy máy chủ tĩnh:
1. Cài Python, mở Terminal trong thư mục `toanvata`.
2. Gõ: `python -m http.server 8000`
3. Mở trình duyệt: http://localhost:8000

(Hoặc dùng tiện ích Live Server trong VS Code.)

## Danh sách kiểm tra chức năng
- [ ] Trang chủ hiện đủ: hero, 3 cấp học (Tiểu học, THCS, THPT), phương pháp, lộ trình, tiến độ, footer; có hình Toán học nền chìm
- [ ] Menu hoạt động; trên điện thoại và máy tính bảng có nút ☰
- [ ] Tìm kiếm ở header trả kết quả đúng; từ khóa lạ hiện thông báo không tìm thấy
- [ ] Lọc theo lớp và chủ đề ở Chương trình học
- [ ] Mở bài học, breadcrumb đúng, Bài trước/Bài tiếp theo đúng
- [ ] Công thức hiển thị bằng MathJax
- [ ] Bấm "Đánh dấu đã hoàn thành" thì Tổng quan và Tiến độ cập nhật; chưa bấm thì không tính
- [ ] Nút "Tôi đã học xong bài này" trong bài học cũng cập nhật (qua postMessage)
- [ ] Từ vựng: tìm kiếm và lọc chủ đề
- [ ] Thêm một mục vào lessons.json thì danh sách tự có bài mới
- [ ] Mở id sai (#/lesson/abc) hiện thông báo không tìm thấy

## Lưu ý
- Dữ liệu trong lessons.json, data/vocab.json và 3 bài trong lessons/ là **mẫu kiểm thử kỹ thuật**, không phải nội dung chính thức.
- Tiến độ chỉ lưu trên trình duyệt hiện tại.

## Giao diện (cập nhật)
- Bảng màu xanh lá lấy từ ảnh mẫu của nhóm: xanh chủ đạo #046B4D, xanh đậm #00503A, xanh nhạt #86E0BD.
- Tên biến màu (--blue, --mint, --lavender…) được giữ nguyên để bài học cũ không bị lỗi, nhưng giá trị nay là các sắc xanh lá. Hồng và vàng nhạt chỉ dùng cho báo sai và ghi chú.
- Chuyển động: hiện dần khi đổi trang, thẻ trượt lên lần lượt, thanh tiến độ chạy đầy, menu điện thoại trượt kèm lớp mờ. Tự tắt nếu thiết bị bật chế độ giảm chuyển động.

## Tên và ngôn ngữ hiển thị
- Tên website (logo góc trên): **TOÁN VÀ TIẾNG ANH**, dòng dưới: *Toán thật dễ, Tiếng Anh thật hay*. Tên danh mục bài, mô tả và chủ đề trên trang đều bằng tiếng Việt.
