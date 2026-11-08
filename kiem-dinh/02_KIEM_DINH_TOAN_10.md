# 02 – KIỂM ĐỊNH TOÁN 10

> **Cập nhật 08/11/2026:** M-001, M-003, M-007, M-008, T-001, T-002 đã chuyển sang **Đã sửa · Đã kiểm tra lại** – xem `10_BAO_CAO_SUA_UU_TIEN_1.md`. Kiểm định thủ công Mức 2–3 (08/11) và các lỗi mới phát hiện (M-101…M-108, P-101…P-109): xem ``11_KIEM_DINH_MUC_2_3.md``. Nội dung bên dưới giữ nguyên như lúc kiểm định (07/11/2026).

Phạm vi: 27 bài đang mở. Mỗi bài: lý thuyết, 5–7 ví dụ, toàn bộ câu luyện tập **Mức 1** (416 câu) đã được đọc và tính lại độc lập. Mức 2–3 (832 câu): **chỉ quét tự động**, chưa giải tay. Bài khóa `g10-sets-02`, `g10-algebra-01`: chưa kiểm định.

Trạng thái theo quy ước: **Đã kiểm định** · **Phát hiện lỗi** (chưa sửa) · Chưa có bài nào ở trạng thái "Đã sửa"/"Đã kiểm tra lại" vì chưa được phép sửa.

| Bài | Mã | Câu Mức 1 | Trạng thái | Lỗi (xem 05/06/07) | Nhận xét |
|---|---|---:|---|---|---|
| 1. Mệnh đề | g10-logic-01 | 15 | Đã kiểm định – lỗi nhẹ | M-L11, P-02 | Định nghĩa, bảng phủ định, lượng từ đúng; Q13 đếm lại: chỉ (4) đúng ✔ |
| 2. Tập hợp và các phép toán | g10-sets-01 | 21 | **Phát hiện lỗi Critical** | **M-001**, P-03, P-L01, P-L02 | Câu 18 khóa sai ở cả 3 mức; phần còn lại đúng (Ví dụ 7 ba tập: 21 ✔) |
| 3. BPT bậc nhất hai ẩn | g10-ineq2-01 | 15 | Phát hiện lỗi High | **M-002**, T-002, P-03, M-L10 | Q15 đếm 13 cặp ✔; câu 2 vỡ công thức |
| 4. Hệ BPT bậc nhất hai ẩn | g10-ineq-sys-01 | 15 | Phát hiện lỗi | M-011, P-01, P-06, T-003 | Q11 \(384/11\) ✔, Ví dụ 5 \(24{,}8\) ✔ |
| 5. GTLG góc 0°–180° | g10-trig-01 | 15 | Đã kiểm định – lỗi nhẹ | M-L01 | Bảng giá trị đúng |
| 6. Hệ thức lượng trong tam giác | g10-trig-02 | 15 | **Đạt** | — | 13-14-15: \(S=84,r=4,R=\frac{65}8\) ✔; \(AT=20\sqrt6\) ✔ |
| 7. Khái niệm mở đầu về vectơ | g10-vec-01 | 15 | Đạt – lỗi nhẹ | M-L03 | Kiểm tra vectơ lục giác đều bằng tọa độ ✔ |
| 8. Tổng và hiệu hai vectơ | g10-vec-02 | 15 | Đạt – lỗi nhẹ | P-L10 | |
| 9. Tích vectơ với một số | g10-vec-03 | 15 | Phát hiện lỗi Medium | M-009 | |
| 10. Vectơ trong mặt phẳng tọa độ | g10-vec-04 | 15 | Đạt – lỗi nhẹ | M-L10 | |
| 11. Tích vô hướng | g10-vec-05 | 15 | Đạt – lỗi nhẹ | M-L04 | góc \(81{,}87^\circ\) ✔ |
| 12. Số gần đúng và sai số | g10-stats-01 | 15 | **Đạt** | — | Quy tắc quy tròn đúng SGK |
| 13. Số đặc trưng xu thế trung tâm | g10-stats-02 | 15 | **Đạt** | — | Tứ phân vị theo cách SGK ✔ |
| 14. Số đặc trưng độ phân tán | g10-stats-03 | 15 | **Đạt** | — | 15 câu tính lại phương sai, \(\Delta_Q\), ngoại lai ✔ |
| 15. Hàm số | g10-func-01 | 15 | Đạt – lỗi nhẹ | M-L09 | Giá điện bậc thang ✔ |
| 16. Hàm số bậc hai | g10-func-02 | 15 | **Phát hiện lỗi High** | **M-003** | Câu 9 có 2 đáp án đúng |
| 17. Dấu tam thức bậc hai | g10-func-03 | 15 | **Đạt** | — | |
| 18. PT quy về PT bậc hai | g10-func-04 | 15 | Đạt | P-07 (chưa xác minh) | Mọi nghiệm ngoại lai được loại đúng |
| 19. Phương trình đường thẳng | g10-coord-01 | 15 | **Đạt** | — | |
| 20. Vị trí tương đối, góc, khoảng cách | g10-coord-02 | 16 | Phát hiện lỗi High (kỹ thuật) | **T-001**, M-L05 | Câu 1 phương án là mã HTML |
| 21. Đường tròn | g10-coord-03 | 15 | Phát hiện lỗi High (kỹ thuật) | **T-001**, **T-002** | Câu 1, 2 không đọc được; toán học đúng |
| 22. Ba đường conic | g10-coord-04 | 18 | Đạt | P-07, P-L08 | Tiêu cự, \(MF_1, MF_2\) kiểm tra lại ✔ |
| 23. Quy tắc đếm | g10-comb-01 | 15 | Phát hiện lỗi Medium (kỹ thuật) | T-003 | Q13: 105 số chẵn ✔ |
| 24. Hoán vị, chỉnh hợp, tổ hợp | g10-comb-02 | 16 | Phát hiện lỗi Medium (kỹ thuật) | T-003 | \(C_{35}^5, C_{45}^6\) ✔ |
| 25. Nhị thức Newton | g10-comb-03 | 15 | Phát hiện lỗi Medium (kỹ thuật) | T-003 | |
| 26. Biến cố, xác suất cổ điển | g10-prob-01 | 15 | Đạt – lỗi nhẹ | P-01 | \(P=\frac{9139}{407253}\) ✔ |
| 27. Thực hành tính xác suất | g10-prob-02 | 15 | Đạt – lỗi nhẹ | P-06, T-003 | |

**Thống kê lớp 10:** 27/27 bài đã kiểm định (Mức 1). Bài đạt không lỗi đáng kể: 8. Bài có lỗi Critical: 1 (Bài 2). Bài có lỗi High: 4 (Bài 3, 16, 20, 21). Câu Mức 1 có lỗi toán học: 2/416.

**Đánh giá riêng lớp 10:** Lý thuyết chuẩn xác và đầy đủ theo 27 bài KNTT; ví dụ chọn lọc tốt. Cần sửa ngay M-001, M-003, M-002 và các câu không đọc được ở Bài 20, 21.
