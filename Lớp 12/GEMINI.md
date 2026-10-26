# Điều phối tạo đề Toán lớp 12

## Chọn nhánh trước khi làm

| Yêu cầu | Thư mục và quy trình |
|---|---|
| Ôn thi THPTQG, tốt nghiệp THPT, đề tổng hợp 2027 | `On_Thi_THPTQG/GEMINI.md` |
| Ôn một chuyên đề/chương, giữa kì, cuối kì | `On_Tap_Giua_Ki_Cuoi_Ki/GEMINI.md` |

- Khi tiếp tục một đề có sẵn, theo nhánh đang chứa đề đó.
- Khi chỉ nói “tạo đề lớp 12” mà chưa rõ mục tiêu, hỏi ngắn để chọn nhánh trước khi tạo đề.
- Mỗi nhánh có `Nguon_Tai_Lieu/` và `Output/` riêng. Chỉ mục nằm tại `Nguon_Tai_Lieu/_index/` của chính nhánh đó.
- Quy tắc THPTQG 12 câu nhiều lựa chọn + 4 đúng/sai + 6 trả lời ngắn, quota nguồn câu khó và xuất bản PRIVATE theo số đề thuộc nhánh `On_Thi_THPTQG`.
- Đề chuyên đề, giữa kì, cuối kì theo nội dung đã học, ma trận và thời lượng được giao; số đề được quản lý riêng.
- Công cụ quét RAG hiện có nằm tại `On_Thi_THPTQG/scripts/index_tai_lieu.py`. Dùng `--source-dir` để quét kho riêng của nhánh học kì; xem lệnh trong `README.md`.

Các PDF đề/đáp án đã xuất bản tại `D:\Document\Dạy học\Đề ko đáp án\PRIVATE` vẫn giữ vị trí cũ. Xem [README](README.md) để biết cấu trúc mới.
