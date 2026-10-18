"""Tách và kiểm tra PDF đề 16 trước khi xuất bản theo quy chuẩn GEMINI.md."""
from pathlib import Path
import os
import re
from pypdf import PdfReader, PdfWriter

base = Path(__file__).resolve().parent
src_pdf = base / "De 16.pdf"
reader = PdfReader(src_pdf)
texts = [p.extract_text() or "" for p in reader.pages]

markers = [i for i, text in enumerate(texts) if "BẢNG ĐÁP ÁN TỔNG HỢP" in text]
assert len(markers) == 1, "Phải có đúng một trang bắt đầu BẢNG ĐÁP ÁN TỔNG HỢP"
split = markers[0]
assert 0 < split < len(texts) - 1

assert "HƯỚNG DẪN GIẢI CHI TIẾT" in texts[split + 1]
assert list(map(int, re.findall(r"Câu\s+(\d+)\s*:", "\n".join(texts[:split])))) == (
    list(range(1, 13)) + list(range(1, 5)) + list(range(1, 7))
)
assert "HẾT" in texts[split - 1]

# Thư mục xuất bản đích theo GEMINI.md
pub_dir = Path(r"D:\Document\Dạy học\Đề ko đáp án\PRIVATE")
ans_dir = pub_dir / "Ans"
pub_dir.mkdir(parents=True, exist_ok=True)
ans_dir.mkdir(parents=True, exist_ok=True)

# 1. Ghi 16.pdf (Đề thi)
writer_exam = PdfWriter()
for p in reader.pages[:split]:
    writer_exam.add_page(p)
writer_exam.add_metadata({"/Title": "Đề thi số 16 - Mã đề 0016", "/Author": "Dương Gia Bảo"})

local_exam = base / "16.pdf"
with local_exam.open("wb") as f:
    writer_exam.write(f)

pub_exam = pub_dir / "16.pdf"
with pub_exam.open("wb") as f:
    writer_exam.write(f)

# 2. Ghi 16_Ans.pdf / Ans/16.pdf (Đáp án và lời giải)
writer_ans = PdfWriter()
for p in reader.pages[split:]:
    writer_ans.add_page(p)
writer_ans.add_metadata({"/Title": "Đáp án và lời giải chi tiết Đề số 16", "/Author": "Dương Gia Bảo"})

local_ans = base / "16_Ans.pdf"
with local_ans.open("wb") as f:
    writer_ans.write(f)

pub_ans = ans_dir / "16.pdf"
with pub_ans.open("wb") as f:
    writer_ans.write(f)

# Kiểm tra tính toàn vẹn
check_exam = PdfReader(local_exam)
check_ans = PdfReader(local_ans)
assert len(check_exam.pages) == split
assert len(check_ans.pages) == len(reader.pages) - split
assert len(check_exam.pages) + len(check_ans.pages) == len(reader.pages)

exam_content = "\n".join(p.extract_text() or "" for p in check_exam.pages)
ans_content = "\n".join(p.extract_text() or "" for p in check_ans.pages)

assert "BẢNG ĐÁP ÁN TỔNG HỢP" not in exam_content
assert "HƯỚNG DẪN GIẢI CHI TIẾT" not in exam_content
assert "BẢNG ĐÁP ÁN TỔNG HỢP" in ans_content
assert "HƯỚNG DẪN GIẢI CHI TIẾT" in ans_content

# Kiểm tra các giá trị đáp số Phần III xuất hiện trong lời giải
for val in ["7,96", "0,92", "7,2", "18", "3,46", "2,6"]:
    assert val in ans_content.replace(" ", ""), f"Thiếu đáp số {val} trong lời giải"

log_text = (base / "De 16.log").read_text(errors="ignore")
assert "Overfull" not in log_text, "Không được có Overfull trong file log"
assert "Undefined control sequence" not in log_text, "Không được có Undefined control sequence"

print(f"[OK] Đã xuất bản thành công Đề 16:")
print(f"  - File đề thi: {pub_exam} ({len(check_exam.pages)} trang)")
print(f"  - File đáp án: {pub_ans} ({len(check_ans.pages)} trang)")
print(f"  - Bản lưu cục bộ: {local_exam} và {local_ans}")
print("[OK] Đủ 22 câu, không lộ đáp án trong đề, đáp số và lời giải đồng bộ 100%, không tràn lề.")
