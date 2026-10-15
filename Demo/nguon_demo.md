# Hồ sơ nguồn bản demo phân loại

Bản demo để xem trước, không thay thế hoặc xuất bản đè lên đề 1–14. Ngữ liệu được lấy qua script local RAG với seed 15, lưu tại `Nguon_Tai_Lieu/_index/sample_de_15.md`. Đây không phải đề số 15 chính thức.

## Phần III

| Câu | File nguồn | Trang PDF / bài gốc | Nút thắt giữ lại hoặc bổ sung |
|---|---|---|---|
| III.1 | `Chuyên đề ôn thi tốt nghiệp THPT năm 2026 môn Toán – Nguyễn Tiến Hà.pdf` | 33, chuyên đề phương sai ghép nhóm | Chế tác: suy ra hai tần số từ cỡ mẫu và trung bình trước khi tính phương sai. |
| III.2 | `Vận dụng cao.pdf` | 103, Câu 313 | Mô hình hai nhánh chung kết; chế tác thêm điều kiện đã biết T vô địch, phải tính xác suất hậu nghiệm thay vì xác suất E thắng bán kết. |
| III.3 | `Vận dụng cao.pdf` | 167, Câu 475 | Tự dựng hàm độ dài thang vượt mái che; phân biệt cao độ điểm tựa và độ cao mái; kiểm tra tối ưu toàn miền. Đổi số liệu thành 7 m, 8 m, 1 m. |
| III.4 | `Phương pháp tiếp cận bài toán thực tế trong đề thi THPT QG 2026 môn Toán.pdf` | 13–14, Bài toán 7 | Góc 120 độ trong định lí cosin, quan hệ dây không dãn, hai biến chuyển động, dấu vận tốc và không làm tròn trung gian. Đổi bối cảnh thành kéo vật, dây 15 m, BF=1 m, AF=4 m. |
| III.5 | `Vận dụng cao.pdf` | 52, Câu 175 | Tối ưu đồng thời hai điểm trên hai nhánh; dùng hai bất đẳng thức và chứng minh điều kiện dấu bằng có thể đạt đồng thời. Giữ đường cong của bài gốc. |
| III.6 | `Phương pháp trải phẳng giải một số bài toán ứng dụng thực tế – Đặng Việt Đông.pdf` | 5, Câu 5 | Chế tác từ đường đi qua ba mặt: đổi lập phương thành hộp 6×4×2, AM=2 để đường thẳng trải phẳng không hợp lệ. Phải xét biên, chứng minh cận dưới và cấu hình đạt được. |

Đủ **5/6 câu từ nhóm ba tài liệu bắt buộc**, thuộc đủ cả ba file; các bài là năm bài độc lập. Trang gốc III.2–III.6 đã được mở và xem hình/render để xác nhận công thức, cấu hình và dữ kiện. Hai trang 13–14 của tài liệu tiếp cận chỉ phục vụ **một** câu III.4, không đếm thành hai câu.

Phần III được thiết kế với hai câu mở đầu ở mức vận dụng và bốn câu sau cần lập luận mô hình/tối ưu. Độ khó là đánh giá biên soạn, chưa được hiệu chuẩn bằng học sinh làm thử. Không đưa sẵn hình trải phẳng trong đề, không ghi nhãn mức khó hoặc gợi ý lời giải trên đề thi.

## Các phần còn lại

- Phần I: phương trình/bất phương trình logarit, đơn điệu, tích phân, Oxyz, thống kê, xác suất, cấp số nhân; ba câu cuối phối hợp tiếp tuyến, cực trị khoảng cách và ràng buộc công suất.
- Phần II: mô-típ chi phí bình quân/lợi nhuận từ `Toán thực tế.pdf` trang 11; radar từ trang 271–287; kiểm tra linh kiện độc lập có điều kiện từ nhóm xác suất/Bayes; vận tốc và quãng đường từ `Ôn tập.pdf` trang 81. Số liệu và khẳng định được thiết kế mới, không sử dụng đáp án nguồn.
- Phần I cân bằng 3A, 3B, 3C, 3D; toàn bộ 22 câu và 16 ý Đ/S được giải độc lập bằng `verify_demo.py`.
- Hình được vẽ mới bằng TikZ; hình không gian giữ vị trí N,P tổng quát, không vẽ cấu hình tối ưu hoặc hình trải phẳng giải hộ câu cuối.

## Nghiệm thu bản xem trước

- Kiểm toán độc lập đủ 22 câu và 16 ý Đ/S; quota nguồn Phần III được kiểm tra trong hồ sơ.
- Biên dịch thành công, không có overfull; đã xem bản render toàn bộ 11 trang và kiểm tra hình dưới dạng trắng đen.
- `De_demo.pdf`: 5 trang đề, đủ 12+4+6 câu, không có bảng đáp án hay lời giải.
- `Dap_an_demo.pdf`: 6 trang bảng đáp án và lời giải; `Demo.pdf`: bản đầy đủ 11 trang.
- Các file lưu riêng trong `D:\Tao_De\Demo`; chưa xuất vào thư mục đề chính thức PRIVATE và chưa hiệu chuẩn độ khó bằng học sinh làm thử.
