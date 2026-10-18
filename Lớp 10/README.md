# Local RAG tạo đề Toán lớp 10

**90 phút — 12 trắc nghiệm + 2 đúng/sai + 4 trả lời ngắn + 4 tự luận.**

Bộ này làm tương tự lớp 12: lập chỉ mục tài liệu local, tìm ngữ liệu có dẫn nguồn, rồi agent viết đề, giải độc lập và xuất PDF. SGK quyết định phạm vi; dataset cung cấp bài tập. Không cần API key, không gửi tài liệu lên mạng.

## Chạy ngay

Mở PowerShell trong thư mục này:

```powershell
# Lập/cập nhật chỉ mục; lần đầu OCR cả hai SGK scan
.\rag.ps1

# Lấy ngữ liệu cho đủ 22 vị trí theo ma trận giữa kỳ I, seed ngẫu nhiên
.\rag.ps1 --exam 1

# Tìm nguồn bài tập hoặc kiến thức SGK
.\rag.ps1 --query "lợi nhuận hàm số bậc hai" --topic ham_so_bac_hai --role dataset
.\rag.ps1 --query "định nghĩa xác suất cổ điển" --role sgk

# Tái lập một mẫu hoặc trích xuất lại từ đầu khi thực sự cần
.\rag.ps1 --exam 2 --seed 2027
.\rag.ps1 --reindex
```

Hoặc nhắn agent: **“Tạo đề lớp 10 số 1 theo GEMINI.md.”** Agent phải hoàn tất cả đề, đáp án, lời giải và kiểm tra PDF; lệnh `--exam` một mình chỉ tạo ngữ liệu tham khảo.

`rag.ps1` dùng môi trường sẵn có `D:\Anaconda\envs\taode\python.exe`. Nếu chạy Python khác, cần PyMuPDF trong `requirements.txt` và Tesseract data `vie`, `eng`; môi trường hiện tại đã có. Có thể gọi trực tiếp `python scripts/index_tai_lieu.py` với cùng các tham số.

## Các thư mục/file

```text
Lớp 10/
├── Nguon_Tai_Lieu/    # Tài liệu gốc đưa vào đây
│   ├── dataset/       # Bài tập tham khảo
│   ├── sgk/           # SGK làm chuẩn nội dung
│   └── Đề thi/        # Đề mẫu để đối chiếu sườn
├── config/            # Phạm vi SGK, cấu trúc đề và ma trận
├── ma_tran/           # Phân tích và nguồn căn cứ ma trận
├── scripts/           # Công cụ RAG, kiểm đề, tách PDF
├── templates/         # Khung đề LaTeX
├── Output/            # Đề đã soạn, đáp án và PDF
└── _index/            # Chỉ mục, mẫu nguồn và danh sách nguồn cần rà
```

Thêm tài liệu lớp 10 vào đúng nhánh trong `Nguon_Tai_Lieu/`, rồi chạy lại `rag.ps1`. `GEMINI.md` vẫn là hướng dẫn chính chứa ma trận và toàn bộ pipeline. Ba JSON cấu hình dùng chung cho các công cụ nằm trong `config/`; đường dẫn nguồn và ma trận bên trong vẫn tính từ thư mục `Lớp 10/`.

| Đường dẫn | Nội dung |
|---|---|
| `Nguon_Tai_Lieu/dataset/` | Tài liệu bài tập gốc; không sửa khi lập chỉ mục |
| `Nguon_Tai_Lieu/sgk/` | Hai tập SGK gốc, chuẩn nội dung |
| `config/curriculum.json` | 13 mạch kiến thức, trang SGK, từ khóa và dấu hiệu cần rà |
| `config/exam_structure.json` | Cấu trúc 12 + 2 + 4 + 4, 90 phút; chọn ma trận đang áp dụng |
| `config/giua_ki_1.json` | Chủ đề, kỹ năng và mức độ của 22 vị trí, dùng chung cho lấy mẫu và kiểm hồ sơ |
| `_index/rag.sqlite3` | Nội dung từng trang, nguồn, OCR, nhãn và chỉ mục tìm kiếm FTS5 |
| `_index/catalog.json` | Thống kê, SHA-256 nguồn, cache và bản trùng |
| `_index/review.md` | Nguồn cần rà phạm vi và trang bị chặn |
| `_index/sample_de_N.md` | Ma trận bắt buộc, 3 nhóm SGK và 22 trang bài tập gán theo từng dạng |
| `Output/De N/` | Đề, hồ sơ nguồn, kiểm toán, PDF đầy đủ và hai bản tách |
| `scripts/` | Lập chỉ mục, kiểm hồ sơ, tách PDF và kiểm thử |
| `templates/de_mau.tex` | Khung LaTeX để viết đề |

Chỉ mục dùng **SQLite FTS5/BM25**, tìm từ khóa tiếng Việt có/không dấu; chưa có embedding hay LLM local tự sinh lời giải. Đây là cơ chế truy xuất tương tự bộ lớp 12, thêm SGK đối chiếu và kiểm soát phạm vi. Không cài vector database hay tải model.

## Giới hạn cần hiểu đúng

- Mỗi đoạn là một trang PDF, không phải một câu hoàn chỉnh. Bài có thể nối trang; công thức OCR, bảng và hình cần mở PDF kiểm tra.
- Khoảng trang SGK được đối chiếu từ mục lục của đúng hai bản scan hiện tại. Trang PDF = trang in + 1; thay bản SGK phải cập nhật `config/curriculum.json`.
- Lọc từ khóa và nhãn chủ đề là bước hỗ trợ, có thể bỏ sót hoặc chặn nhầm. Có nhãn SGK cùng chủ đề không chứng minh câu hỏi hợp lệ; agent vẫn phải kiểm tra kiến thức và cách giải từng câu.
- File trùng theo SHA-256 chỉ được trích xuất một lần; tất cả bản gốc vẫn giữ nguyên. File lỗi OCR làm lệnh thất bại và giữ cache đã đọc thành công để chạy tiếp lần sau.
- Cache dựa trên SHA-256 nội dung, không chỉ thời gian sửa file. Các bản cập nhật chủ đề được áp dụng lại mà không cần OCR. Hỗ trợ PDF, TXT, MD, TEX; tài liệu khác cần chuyển sang PDF trước.
- Bộ này chưa tạo đề hoàn chỉnh chỉ bằng nút chạy: bước viết, giải độc lập và duyệt PDF nằm trong quy trình agent ở `GEMINI.md`.

## Kiểm tra project

Ma trận giữa kỳ I được phân tích tại [ma_tran/phan_tich_giua_ki_1.md](ma_tran/phan_tich_giua_ki_1.md), kèm [22 vị trí câu hỏi](config/giua_ki_1.json). `GEMINI.md` tập trung ma trận và pipeline Pha 0–4; `--exam` tự đọc ma trận đang chọn và chỉ lấy ba mạch mệnh đề–tập hợp, BPT hai ẩn, hệ thức lượng. Chỉ mục cả năm vẫn giữ để tra cứu.

Các dạng bài được đổi thứ tự **trong cùng một phần**, giữ đủ từng dạng, chủ đề và mức độ. Hồ sơ `nguon_deN.json` có `matrix_id`; mỗi câu ghi `number` theo đề thực tế và `matrix_slot` theo mã dạng bài gốc (ví dụ câu 1 phần I dùng dạng I.6: `"section":"I", "number":1, "matrix_slot":"I.6"`). Nếu không ghi `matrix_slot`, bộ kiểm hiểu là giữ thứ tự gốc. Nguồn phải đi theo dạng bài khi đổi số câu; mẫu Markdown gán nguồn theo mã dạng bài gốc.

Bộ kiểm đối chiếu `topic`, `level` theo dạng bài được ánh xạ, cấm lặp/bỏ dạng hoặc chuyển sang phần khác; câu đúng/sai phải đủ `statements` a–d và mức độ từng ý. Theo yêu cầu người dùng, không kiểm tính điểm hoặc quy tắc chấm điểm. Kiểm hồ sơ không thay thế đọc câu hỏi/lời giải thực tế để xác nhận đúng kỹ năng và độ khó.

```powershell
& 'D:\Anaconda\envs\taode\python.exe' -B -m unittest discover -s scripts -p 'test_*.py'
```

Khi đã có một đề, kiểm hồ sơ và tách PDF:

```powershell
& 'D:\Anaconda\envs\taode\python.exe' -B scripts/check_exam.py --exam 1
& 'D:\Anaconda\envs\taode\python.exe' -B scripts/split_pdf.py --exam 1 --answer-start 6
```

`6` chỉ minh họa tham số, phải thay bằng trang bắt đầu đáp án thực tế. Mọi đầu ra ở lớp 10; không đụng thư mục xuất bản của lớp 12.
