# Nguồn và RAG dùng chung cho lớp 12 — 26/10/2026

Theo chỉnh lại của người dùng: tất cả nguồn dùng chung cho các loại đề lớp 12; chỉ tách quy trình và đầu ra của THPTQG và chuyên đề/giữa kì/cuối kì.

- Kho nguồn duy nhất: `D:\Tao_De\Lớp 12\Nguon_Tai_Lieu\`.
- Công cụ chung: `D:\Tao_De\Lớp 12\scripts\index_tai_lieu.py`.
- [moves.csv](moves.csv): kế hoạch chuyển kho nguồn và hai script từ nhánh THPTQG về gốc lớp 12; lưu bộ chỉ mục học kì trống trong `retired_school_index/`.
- [files.csv](files.csv): 69 file được di chuyển, dung lượng, thời gian sửa UTC và SHA-256 ban đầu.
- [operations.jsonl](operations.jsonl): thao tác thực tế và kết quả kiểm tra hash/thời gian sau di chuyển, trước khi cập nhật mã và chỉ mục.
- Bộ chỉ mục học kì cũ chỉ gồm hai file chỉ mục trống và ba `.gitkeep`, không có PDF nguồn. Lưu lại để có thể lần theo lịch sử, không xóa nội dung.
- File `Hoàng xuân Nhàn.pdf` do người dùng thêm cũng được chuyển nguyên vẹn về kho chung và quét vào RAG.
- Thêm chế độ bốc ngữ liệu theo chủ đề cho đề học kì, dùng cùng kho và cùng chỉ mục; giữ chế độ `--exam` cũ cho THPTQG.
- Không chỉnh nội dung các PDF đề, đáp án hay tài liệu gốc. Cập nhật các hướng dẫn và hồ sơ nguồn để chỉ tới vị trí mới.
- [verification.json](verification.json): kho chung 50 nguồn/3.705 đoạn, 142 trang từ nguồn mới, 8 bài kiểm tra RAG đạt; thử CLI học kì đã bốc 16 trang không lặp theo 8 nhãn đã chọn. Tất cả PDF đầu ra hiện có giữ nguyên hash. Nhãn theo trang vẫn cần kiểm tra lại từng bài trên PDF.
