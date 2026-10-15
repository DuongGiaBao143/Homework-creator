# Nguồn và kiểm toán đề 12

Đề được biên soạn mới từ các mô-típ trong `../Nguon_Tai_Lieu/_index/sample_de_12.md`. Số liệu, cách hỏi và lời giải được thiết kế lại rồi giải độc lập bằng `verify_de12.py`; không sao chép đáp án nguồn. Theo yêu cầu người dùng, không đối chiếu nội dung với 11 đề trước.

| Câu | Ngữ liệu tham khảo trong mẫu đề 12 | Nội dung chế tác |
|---|---|---|
| I.1 | Ôn tập.pdf, trang PDF 23 | Đơn điệu của phân thức, xét đúng miền xác định |
| I.2 | Ôn tập.pdf, trang PDF 8 | Phương trình logarit có điều kiện |
| I.3 | Nguyễn Tiến Hà, trang PDF 260 | Tích phân đa thức xác định |
| I.4 | Nguyễn Tiến Hà, trang PDF 329 | Mặt phẳng và vectơ pháp tuyến |
| I.5 | Xác suất.pdf, trang PDF 129 | Chọn hai vật không hoàn lại |
| I.6 | Nguyễn Tiến Hà, trang PDF 26 | Trung vị mẫu số liệu ghép nhóm |
| I.7 | Nguyễn Tiến Hà, trang PDF 12 | Phương trình lượng giác cơ bản |
| I.8 | LTT 7-10.pdf, trang PDF 6 | Cấp số nhân |
| I.9 | Tổng ôn.pdf, trang PDF 199 | Mặt cầu và mặt phẳng tiếp xúc |
| I.10 | Vận dụng cao.pdf, trang PDF 573 (Khu vực I) | Đếm tham số nguyên cho phân thức có hai nghiệm |
| I.11 | Toán thực tế.pdf, trang PDF 89 (Khu vực I) | Cân bằng lực và giới hạn chịu lực dây treo |
| I.12 | Xác suất.pdf, trang PDF 129 (Khu vực I) | Bayes kết hợp lấy bi không hoàn lại |
| II.1 | Vận dụng cao.pdf, trang PDF 573 (Khu vực I) | Phân thức bậc hai/bậc nhất, diện tích tiếp tuyến, giới hạn hai nghiệm |
| II.2 | Xác suất.pdf, trang PDF 129 và Nguyễn Tiến Hà, trang PDF 283 (Khu vực I) | Phế phẩm hai phân xưởng và hai lần kiểm tra độc lập có điều kiện |
| II.3 | Toán thực tế.pdf, trang PDF 282 (Khu vực I) | Drone, khoảng cách cực tiểu và thời gian trong vùng radar |
| II.4 | Nguyễn Tiến Hà, trang PDF 32 (Khu vực I) | Phương sai, tứ phân vị và hiệu chỉnh tuyến tính |
| III.1 | Toán thực tế.pdf, trang PDF 65 (Khu vực I) | Ước lượng tham số bán hàng, tối ưu lợi nhuận quảng cáo |
| III.2 | Nguyễn Tiến Hà, trang PDF 383 (Khu vực I) | Bể hình thang, lưu lượng biến thiên và tốc độ dâng nước |
| III.3 | Phương pháp trải phẳng – Đặng Việt Đông.pdf, trang PDF 38 (Khu vực I) | Đường ngắn nhất qua tường có bề dày và độ cao |
| III.4 | Toán thực tế.pdf, trang PDF 224 (Khu vực I) | Tối ưu tổng độ dài qua mặt phẳng bằng phản xạ |
| III.5 | Toán thực tế.pdf, trang PDF 213 (Khu vực I) | Khôi phục cạnh mặt cắt parabol rồi tích phân diện tích |
| III.6 | Toán thực tế.pdf, trang PDF 135 (Khu vực I) | Tối ưu thời gian khai thác máy với doanh thu và chi phí biên |

Tên “Nguyễn Tiến Hà” trong bảng là file `Chuyên đề ôn thi tốt nghiệp THPT năm 2026 môn Toán – Nguyễn Tiến Hà.pdf`. Số trang là vị trí trang trong PDF, có thể khác số trang in trên tài liệu. Hình minh họa được vẽ mới bằng TikZ theo số liệu đề; không dùng ảnh đồ thị cũ.

Lưu ý mô hình: III.1 sử dụng số lượng thực theo hàm bán hàng; III.3 tường kéo dài vô hạn để loại bỏ đường vòng qua đầu tường; II.2 chỉ giả định độc lập khi đã biết trạng thái lỗi của linh kiện. Seed chọn ngữ liệu không bảo đảm các đề khác nhau tuyệt đối.

## Nghiệm thu ngày 14/10/2026

- Kiểm toán độc lập bằng SymPy: 12 câu Phần I, 16 ý của 4 câu Phần II và 6 câu Phần III đều qua kiểm tra; bảng đáp án đồng bộ với kết quả kiểm toán.
- Phần I có đúng 3A, 3B, 3C, 3D. Đề không chứa hàm hợp hoặc tích phân hàm ẩn máy móc.
- Biên dịch pdflatex thành công: bản đầy đủ 12 trang, không có overfull hay lỗi lệnh LaTeX; đã xem render toàn bộ 12 trang và bản trắng đen của 3 trang chứa hình.
- `12.pdf`: 5 trang đề, kiểm tra đủ 22 câu và không có bảng đáp án/lời giải. `12_Ans.pdf`: 7 trang gồm bảng đáp án và lời giải chi tiết.
- Đã xuất sang `D:\Document\Dạy học\Đề ko đáp án\PRIVATE\12.pdf` và `PRIVATE\Ans\12.pdf`; đọc lại hai bản xuất, xác nhận số trang và SHA-256 khớp bản trong thư mục đề.
- Không đối chiếu với 11 đề trước theo yêu cầu người dùng; chưa in thử trên giấy.
