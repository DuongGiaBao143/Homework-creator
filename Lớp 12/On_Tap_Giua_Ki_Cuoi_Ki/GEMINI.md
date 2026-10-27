# Ôn chuyên đề, giữa kì và cuối kì Toán 12

## Mục tiêu và phạm vi

Nhánh này phục vụ dạy học theo chương/chuyên đề và ôn kiểm tra định kì. Trước khi tạo đề, xác định chuyên đề hoặc kì kiểm tra, phạm vi kiến thức đã học, mức học sinh, thời lượng, cấu trúc và thang điểm từ yêu cầu/ma trận người dùng đưa.

- Chỉ hỏi thông tin còn thiếu có ảnh hưởng đến nội dung hoặc cấu trúc. Có thể dùng cấu trúc của đề mẫu/ma trận đã cung cấp.
- Nếu chưa có mẫu/ma trận và người dùng không chỉ định cấu trúc, đề xuất cấu trúc phù hợp với phạm vi và thời lượng trước khi chốt đề.
- Chọn câu trong phạm vi đã học; độ khó theo nhóm học sinh. Các đề ôn cùng chuyên đề được phép tập trung vào một mạch kiến thức.
- Quy định 12 + 4 + 6, ít nhất hai câu khó từ ba tài liệu bắt buộc và header “HƯỚNG TỚI THPTQG 2027” thuộc nhánh THPTQG; nhánh này dùng tiêu đề chuyên đề/kì kiểm tra được giao.

## Lưu nguồn và đầu ra

- Tài liệu dùng chung với nhánh THPTQG tại `../Nguon_Tai_Lieu/`; giữ tên gốc có ý nghĩa, không sao chép thành kho riêng.
- Một RAG chung tại `../Nguon_Tai_Lieu/_index/`. Công cụ: `../scripts/index_tai_lieu.py`.
- Khi tạo đề, chạy công cụ với `--mode hoc-ki --exam <số> --topics <các nhãn thuộc phạm vi> --output <thư mục đề>/ngu_lieu_rag.md` để tự bốc ngữ liệu từ kho chung. Ví dụ Bài 1–8 có trong `../README.md`.
- Mở từng trang PDF được bốc để chọn bài đúng phạm vi; một trang có thể gồm nhiều bài và nhãn chỉ là gợi ý. Ghi đúng tên file, trang và số câu trong hồ sơ nguồn.
- Đầu ra: `Output/Chuyen_De/<tên chuyên đề hoặc mã đề>/`, `Output/Giua_Ki/<học kì và mã đề>/`, `Output/Cuoi_Ki/<học kì và mã đề>/`.
- Mỗi đề giữ chung mã nguồn `.tex`, PDF gộp, `De_thi.pdf`, `Dap_an.pdf`, script kiểm tra và hồ sơ nguồn. Tách tên/thư mục để các đề ôn không ghi đè nhau.
- Bộ `Output/Chuyen_De/De_HamSo/` và `scripts/verify_chuyen_de_ham_so.py` được chuyển từ cấu trúc cũ; chỉ sửa nội dung khi người dùng yêu cầu.

## Quy trình tạo đề

1. Chốt phạm vi, lập ma trận theo nội dung, mức độ, dạng câu và điểm. Bảo đảm tổng điểm, thời lượng khớp yêu cầu.
2. Chạy RAG chung để bốc theo các nhãn thuộc phạm vi; đọc `ngu_lieu_rag.md` rồi mở trang nguồn để xác nhận từng bài đầy đủ dữ kiện/hình và đúng kiến thức đã học. Khi chế tác bài, giữ bối cảnh và đơn vị hợp lý.
3. Giải độc lập từng câu, kiểm tra đáp án, các ý đúng/sai, điều kiện xác định và làm tròn. Lưu script kiểm tra khi có tính toán đáng kể.
4. Dùng Times New Roman 12pt/XeLaTeX cho đề mới; có thể tham khảo bố cục và macro `\bonpa` trong `../On_Thi_THPTQG/templates/de_mau.tex`, giữ khoảng cách hai hàng đáp án 8pt. Điều chỉnh tiêu đề, thời gian và các phần theo ma trận riêng.
   - Bài cực trị/tối ưu trong bối cảnh thực tế bắt buộc có hình minh họa hoặc sơ đồ dữ kiện; ví dụ kéo cáp, rào đất, đóng hộp, thiết kế bể. Vẽ đúng các điểm, quan hệ và kích thước đã cho; không cho sẵn vị trí tối ưu hoặc bước giải then chốt. Xem quy tắc chung tại `../AGENTS.md`.
5. Đáp án và lời giải bắt đầu ở trang mới; tách PDF đề/đáp án. Render để kiểm tra chữ, hình, ngắt trang, không lộ lời giải trong đề.
6. Ghi phạm vi, ma trận/thang điểm, nguồn (file/trang/câu) và kết quả kiểm tra vào hồ sơ của đề. Báo rõ phần chưa kiểm chứng.

Ảnh và đồ thị cần rõ khi in trắng đen; dùng nét/họa tiết thay cho chỉ dẫn chỉ dựa vào màu. Đề mới mang tiêu đề như “ÔN TẬP CHUYÊN ĐỀ: …”, “ÔN TẬP GIỮA KÌ I” hoặc “ÔN TẬP CUỐI KÌ II”; ghi biên soạn Dương Gia Bảo.

Mặc định lưu bản hoàn chỉnh trong `Output/` của nhánh này.
Khi xuất bản phục vụ giảng dạy:
- **Đề thi giữa kì:** Xuất bản vào `D:\Document\Dạy học\Dạy lớp 12\Ôn GK` với bản đề bài duy nhất `<số_đề>.pdf` và bản đáp án `Ans\<số_đề>.pdf` (không sinh file trùng lặp mang tên mã đề).
- **Chuyên đề / Cuối kì hoặc xuất riêng:** Khi cần lưu trữ thêm vào PRIVATE, dùng `D:\Document\Dạy học\Đề ko đáp án\PRIVATE\Lop12_Giua_Ki_Cuoi_Ki\<loại>\<mã đề>\`. Các file đánh số ở PRIVATE gốc thuộc bộ THPTQG hiện có.
