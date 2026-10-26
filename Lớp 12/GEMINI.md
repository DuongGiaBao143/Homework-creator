# Điều phối tạo đề Toán lớp 12

## Chọn nhánh trước khi làm

| Yêu cầu | Thư mục và quy trình |
|---|---|
| Ôn thi THPTQG, tốt nghiệp THPT, đề tổng hợp 2027 | `On_Thi_THPTQG/GEMINI.md` |
| Ôn một chuyên đề/chương, giữa kì, cuối kì | `On_Tap_Giua_Ki_Cuoi_Ki/GEMINI.md` |

- Khi tiếp tục một đề có sẵn, theo nhánh đang chứa đề đó.
- Khi chỉ nói “tạo đề lớp 12” mà chưa rõ mục tiêu, hỏi ngắn để chọn nhánh trước khi tạo đề.
- Nguồn dùng chung cho mọi loại đề lớp 12: `Nguon_Tai_Lieu/`, với một chỉ mục tại `Nguon_Tai_Lieu/_index/`. Hai nhánh chỉ tách quy trình và `Output/`.
- Quy tắc THPTQG 12 câu nhiều lựa chọn + 4 đúng/sai + 6 trả lời ngắn, quota nguồn câu khó và xuất bản PRIVATE theo số đề thuộc nhánh `On_Thi_THPTQG`.
- Đề chuyên đề, giữa kì, cuối kì theo nội dung đã học, ma trận và thời lượng được giao; số đề được quản lý riêng.
- Công cụ chung là `scripts/index_tai_lieu.py`: quét tài liệu mới/thay đổi, phân loại và bốc ngữ liệu theo số đề. Mặc định `--exam` dùng quy trình THPTQG; thêm `--mode hoc-ki --topics ... --output ...` để bốc theo phạm vi cho chuyên đề/giữa kì/cuối kì. Xem lệnh trong `README.md`.
- Script xuất ngữ liệu tham khảo Markdown; bước biên soạn câu hỏi, giải kiểm tra và xuất PDF thực hiện tiếp theo quy trình của nhánh.

Các PDF đề/đáp án đã xuất bản tại `D:\Document\Dạy học\Đề ko đáp án\PRIVATE` vẫn giữ vị trí cũ. Xem [README](README.md) để biết cấu trúc mới.
