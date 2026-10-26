# Demo header và font đề 16

Bản thử ngày 26/10/2026, chờ duyệt trước khi áp dụng cho cả bộ.

- `De_16_demo.pdf`: chỉ đề bài, 5 trang, mã 0016.
- `De_16_header.png`: ảnh xem nhanh header.
- `De_16_demo.tex`: nguồn riêng, biên dịch bằng XeLaTeX (font Times New Roman của Windows).
- Nội dung 22 câu và hình vẽ giữ nguyên nguồn `../../De 16/De 16.tex`; chỉ thay font, header, footer và cách ngắt dòng.
- Chữ văn bản Times New Roman 12pt; công thức giữ font Computer Modern (cùng kiểu nét toán với KaTeX trong mẫu).

Biên dịch trong thư mục này: `xelatex -interaction=nonstopmode -halt-on-error -no-shell-escape De_16_demo.tex`.

Kiểm tra: so sánh nguyên văn thân LaTeX với đề 16 (chỉ đổi đường dẫn ảnh), đủ thứ tự 12+4+6 câu, không lộ đáp án, số trang/header/footer khớp, nhúng đủ Times New Roman thường/đậm/nghiêng, không tràn lề hoặc thiếu ký tự; đã xem bản render cả 5 trang. Chưa kiểm tra in giấy và không giải lại nội dung toán trong lần chỉnh định dạng này.

Chưa thay bản đề 16 chính thức, file đáp án hoặc các đề khác. Mọi bản phát hành trong thư mục PRIVATE giữ nguyên.
