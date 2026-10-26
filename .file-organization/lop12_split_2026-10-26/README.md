# Tách hai nhánh lớp 12 — 26/10/2026

- Phạm vi: `D:\Tao_De\Lớp 12`, theo yêu cầu tách ôn thi THPTQG 2027 và ôn chuyên đề/giữa kì/cuối kì.
- [files.csv](files.csv): 295 file ban đầu, đường dẫn nguồn/đích, dung lượng, thời gian sửa UTC và SHA-256 trước khi chỉnh đường dẫn.
- [moves.csv](moves.csv): kế hoạch di chuyển 8 mục ở gốc vào `On_Thi_THPTQG`, chuyển riêng bộ `De_HamSo` và script kiểm tra sang nhánh học kì.
- [operations.jsonl](operations.jsonl): các thao tác hoàn tất/thất bại được ghi khi thực hiện. Move thư mục Output bị dừng sau khi chuyển một phần do thuộc tính/quyền Windows; đã tiếp tục từng file sau khi kiểm tra hash và đích. Chỉ dọn các thư mục nguồn đã rỗng.
- Cả 295 file đã khớp SHA-256 và thời gian sửa sau di chuyển, trước bước cập nhật đường dẫn. Các chỉnh sửa mã nguồn/tài liệu sau đó được theo dõi riêng trong Git và báo cáo kiểm tra.
- [verification.json](verification.json): kiểm tra đủ 295 file, 284 file giữ nguyên nội dung, 11 file mã/tài liệu cập nhật cho đường dẫn/công cụ, 49 tham chiếu ảnh LaTeX hợp lệ, RAG THPT đủ 49 nguồn/3.563 đoạn và 6 bài kiểm tra đều đạt. Kiểm tra XeLaTeX chạy với cấu hình MiKTeX của tài khoản Windows.
- Giữ nguyên tất cả PDF/ảnh/tệp nguồn đề đã phát hành và các file tại PRIVATE. Không xóa file tài liệu hoặc gộp file trùng.

Để lần lại vị trí cũ, tra cột `Source` và `Destination` trong `files.csv`. Khi cần hoàn tác một file, kiểm tra hash và xung đột đích trước khi di chuyển ngược; các file có chỉnh đường dẫn cần phục hồi nội dung từ Git tương ứng.
