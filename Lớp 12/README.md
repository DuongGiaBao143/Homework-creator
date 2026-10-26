# Tạo đề Toán lớp 12

```text
Lớp 12/
├── On_Thi_THPTQG/
│   ├── GEMINI.md
│   ├── Nguon_Tai_Lieu/_index/
│   ├── Output/                  # Đề 1–16 và Demo
│   ├── scripts/
│   ├── templates/
│   └── resources/
└── On_Tap_Giua_Ki_Cuoi_Ki/
    ├── GEMINI.md
    ├── Nguon_Tai_Lieu/          # Chuyen_De, Giua_Ki, Cuoi_Ki, _index
    ├── Output/                  # Chuyen_De, Giua_Ki, Cuoi_Ki
    └── scripts/                 # Kiểm tra đề chuyên đề hiện có
```

| Nhánh | Dùng khi | Quy trình |
|---|---|---|
| `On_Thi_THPTQG` | Tạo đề tổng hợp ôn thi THPTQG 2027 | [Quy tắc THPTQG](On_Thi_THPTQG/GEMINI.md) |
| `On_Tap_Giua_Ki_Cuoi_Ki` | Tạo phiếu/đề chuyên đề, ôn giữa kì hoặc cuối kì | [Quy tắc ôn tập học kì](On_Tap_Giua_Ki_Cuoi_Ki/GEMINI.md) |

Toàn bộ kho 49 nguồn và RAG 3.563 đoạn hiện có nằm trong nhánh THPTQG. `De_HamSo` được chuyển nguyên bộ sang `On_Tap_Giua_Ki_Cuoi_Ki/Output/Chuyen_De/De_HamSo/`; script kiểm tra chuyển cùng sang nhánh đó. Nội dung và định dạng cũ của đề vẫn được giữ nguyên.

## Quét RAG

Chạy từ `D:\Tao_De\Lớp 12`. Dùng Python có PyMuPDF hoặc pypdf; môi trường hiện có là `D:\Anaconda\envs\taode\python.exe`.

```powershell
# Kho THPTQG; mặc định chỉ xử lý tài liệu mới/thay đổi.
& 'D:\Anaconda\envs\taode\python.exe' -B -X utf8 '.\On_Thi_THPTQG\scripts\index_tai_lieu.py' --workers 2

# Kho chuyên đề/giữa kì/cuối kì, chỉ mục riêng trong chính kho này.
& 'D:\Anaconda\envs\taode\python.exe' -B -X utf8 '.\On_Thi_THPTQG\scripts\index_tai_lieu.py' --source-dir '.\On_Tap_Giua_Ki_Cuoi_Ki\Nguon_Tai_Lieu' --workers 2

# Lấy mẫu ngữ liệu cho đề THPTQG mới, ví dụ đề 17.
& 'D:\Anaconda\envs\taode\python.exe' -B -X utf8 '.\On_Thi_THPTQG\scripts\index_tai_lieu.py' --exam 17
```

`--exam` dành cho pipeline THPTQG. Với kho học kì, chọn ngữ liệu từ `extracted_chunks.jsonl` theo đúng chủ đề và phạm vi rồi lập ma trận của đề. Kho học kì ban đầu chưa có tài liệu nguồn; có thể tham khảo các trang phù hợp trong kho THPTQG và ghi rõ nguồn.

Ví dụ giao việc: “Tạo đề THPTQG 17”; “Tạo đề ôn chuyên đề đạo hàm cho học sinh mức 6–7 điểm”; “Tạo đề ôn giữa kì 1 lớp 12 theo ma trận đính kèm”.

## Kiểm tra công cụ

```powershell
& 'D:\Anaconda\envs\taode\python.exe' -B -X utf8 -m unittest discover -s '.\On_Thi_THPTQG\scripts' -p 'test_*.py' -v
```

Kiểm tra template cần XeLaTeX trên PATH. Chạy công cụ cũ bằng đường dẫn mới trong nhánh THPTQG. Nhật ký di chuyển và hash trước khi cập nhật đường dẫn nằm tại [bảng kê tổ chức](../.file-organization/lop12_split_2026-10-26/README.md).
