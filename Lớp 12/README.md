# Tạo đề Toán lớp 12

Nguồn tài liệu và RAG dùng chung cho THPTQG, chuyên đề, giữa kì và cuối kì. Hai nhánh tách quy trình và đầu ra.

```text
Lớp 12/
├── Nguon_Tai_Lieu/              # Tất cả nguồn lớp 12
│   └── _index/                 # Chỉ mục dùng chung
├── scripts/
│   ├── index_tai_lieu.py        # Quét và bốc ngữ liệu cho cả hai nhánh
│   └── test_index_tai_lieu.py
├── On_Thi_THPTQG/
│   ├── GEMINI.md
│   ├── Output/                 # Đề 1–16 và Demo
│   ├── scripts/                # Công cụ trình bày/xuất đề THPTQG
│   ├── templates/
│   └── resources/
└── On_Tap_Giua_Ki_Cuoi_Ki/
    ├── GEMINI.md
    ├── Output/                 # Chuyen_De, Giua_Ki, Cuoi_Ki
    └── scripts/                # Kiểm tra đề chuyên đề hiện có
```

| Nhánh | Quy trình |
|---|---|
| Ôn thi THPTQG 2027 | [Quy tắc THPTQG](On_Thi_THPTQG/GEMINI.md) |
| Chuyên đề, giữa kì, cuối kì | [Quy tắc ôn tập học kì](On_Tap_Giua_Ki_Cuoi_Ki/GEMINI.md) |

## Chạy công cụ

Chạy từ `D:\Tao_De\Lớp 12`. Môi trường Python hiện có: `D:\Anaconda\envs\taode\python.exe`.

```powershell
# Quét kho chung; chỉ xử lý tài liệu mới/thay đổi.
& 'D:\Anaconda\envs\taode\python.exe' -B -X utf8 '.\scripts\index_tai_lieu.py' --workers 2

# Tự bốc ngữ liệu cho đề THPTQG 17.
& 'D:\Anaconda\envs\taode\python.exe' -B -X utf8 '.\scripts\index_tai_lieu.py' --exam 17
```

Lệnh `--exam` giữ cách hoạt động cũ: dùng seed theo số đề, bốc ngữ liệu theo các chuyên đề và ghi `Nguon_Tai_Lieu/_index/sample_de_<số>.md`. Quy tắc nguồn khó từ đề 13 áp dụng cho chế độ THPTQG.

Để bốc cho giữa kì/chuyên đề/cuối kì, dùng `--mode hoc-ki`, chọn các nhãn kiến thức và file đầu ra mới trong thư mục của đề. Ví dụ cho Bài 1–8, đề giữa kì tiếp theo:

```powershell
& 'D:\Anaconda\envs\taode\python.exe' -B -X utf8 '.\scripts\index_tai_lieu.py' `
  --mode hoc-ki --exam 2 `
  --topics dang_ham_so_don_dieu dang_ham_so_cuc_tri dang_ham_so_gtln_gtnn `
    dang_ham_so_tiem_can_phan_thuc dang_ham_so_do_thi_bbt dang_ham_so_toi_uu_thuc_te `
    dang_oxyz_vecto_toa_do_diem dang_oxyz_can_bang_luc_vat_ly `
  --output '.\On_Tap_Giua_Ki_Cuoi_Ki\Output\Giua_Ki\HK1_De_02\ngu_lieu_rag.md'
```

- `--topics` nhận các nhãn có trong trợ giúp `--help`. Chế độ học kì bắt buộc có phạm vi và đích xuất rõ ràng; không áp quota nguồn khó THPTQG.
- Script lọc trang theo nhãn, bốc ngữ liệu và ghi tên nguồn/trang; không tự soạn xong câu hỏi hoặc tạo PDF. Sau khi bốc, đọc trang nguồn, chọn đúng bài trong phạm vi rồi biên soạn, giải kiểm tra và xuất đề theo quy trình của nhánh.
- Một trang có thể chứa nhiều bài và nhãn chưa bao quát hết nội dung. Luôn kiểm tra từng bài trên PDF gốc; không coi bộ lọc là bằng chứng tự động rằng mọi bài trên trang đều đúng phạm vi.
- Hồ sơ ngữ liệu học kì không được ghi đè hoặc đặt trong kho nguồn, để tránh lẫn giữa tài liệu gốc và đầu ra.
- Thêm tài liệu mới vào `Nguon_Tai_Lieu/`, chạy quét chung một lần là cả hai nhánh dùng được.

## Kiểm tra và hồ sơ tổ chức

```powershell
& 'D:\Anaconda\envs\taode\python.exe' -B -X utf8 -m unittest discover -s '.\scripts' -p 'test_*.py' -v
& 'D:\Anaconda\envs\taode\python.exe' -B -X utf8 -m unittest discover -s '.\On_Thi_THPTQG\scripts' -p 'test_*.py' -v
```

Kiểm tra template cần XeLaTeX trên PATH. `De_HamSo` ở `On_Tap_Giua_Ki_Cuoi_Ki/Output/Chuyen_De/`; các đề đã phát hành và bản PRIVATE giữ nguyên nội dung.

Hồ sơ [tách hai nhánh ban đầu](../.file-organization/lop12_split_2026-10-26/README.md) và [đưa nguồn/RAG về dùng chung](../.file-organization/lop12_shared_sources_2026-10-26/README.md) lưu đường dẫn, hash và kết quả kiểm tra. Chỉ mục học kì trống trước đây được lưu trong hồ sơ tổ chức, không còn là kho nguồn hoạt động.
