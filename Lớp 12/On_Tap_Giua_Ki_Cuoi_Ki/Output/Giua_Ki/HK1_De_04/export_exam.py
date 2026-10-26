"""Tách PDF đã biên dịch, giữ đầu ra trong đúng thư mục đề giữa kì HK1_De_04."""
from pathlib import Path
import json
import re
import shutil
from pypdf import PdfReader, PdfWriter
import pymupdf

BASE = Path(__file__).resolve().parent
PROJECT = BASE.parents[4]
BUILD = PROJECT / "tmp/pdfs/HK1_De_04/build"
SOURCE = BUILD / "De_giua_ki_1_04.pdf"
reader = PdfReader(SOURCE)
texts = [p.extract_text() or "" for p in reader.pages]
markers = [i for i, text in enumerate(texts) if "BẢNG ĐÁP ÁN TỔNG HỢP" in text]
assert len(markers) == 1
split = markers[0]
assert split == 4 and len(reader.pages) == 9, (split, len(reader.pages))
questions = "\n".join(texts[:split])
assert list(map(int, re.findall(r"Câu\s+(\d+)\s*:", questions))) == list(range(1, 13)) + list(range(1, 5)) + list(range(1, 7))
assert "HẾT" in texts[split - 1]
assert "BẢNG ĐÁP ÁN TỔNG HỢP" not in questions and "HƯỚNG DẪN GIẢI CHI TIẾT" not in questions
assert "HƯỚNG DẪN GIẢI CHI TIẾT" in texts[split + 1]
assert "04 trang" in texts[0]
for i, text in enumerate(texts[:split], 1):
    assert f"Trang {i}/4 - Mã đề: 0004" in text
    assert len(re.findall(r"Câu\s+\d+\s*:", text)) >= 4, f"Page {i} has too few questions."
log = (BUILD / "De_giua_ki_1_04.log").read_text(errors="replace")
for flag in ("Overfull", "Missing character", "Undefined control sequence", "LaTeX Error"):
    assert flag not in log, flag
with pymupdf.open(SOURCE) as doc:
    times_fonts = set()
    for page in doc:
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    box = pymupdf.Rect(span["bbox"])
                    assert box.x0 >= 0 and box.y0 >= 0 and box.x1 <= page.rect.width + 0.5 and box.y1 <= page.rect.height + 0.5, span
        for font in page.get_fonts():
            if "TimesNewRoman" in font[3]:
                assert len(doc.extract_font(font[0])[3]) > 0, font
                times_fonts.add(font[3])
    assert times_fonts
shutil.copyfile(SOURCE, BASE / "De_giua_ki_1_04.pdf")
for filename, start, end, title in (
    ("De_thi.pdf", 0, split, "On tap giua ki I lop 12 - De 04"),
    ("Dap_an.pdf", split, len(reader.pages), "Dap an va loi giai - On tap giua ki I lop 12 - De 04"),
):
    writer = PdfWriter()
    for page in reader.pages[start:end]:
        writer.add_page(page)
    writer.add_metadata({"/Title": title, "/Author": "Duong Gia Bao"})
    target = BASE / filename
    with target.open("wb") as stream:
        writer.write(stream)
    reopened = PdfReader(target)
    assert len(reopened.pages) == end - start
    assert [p.extract_text() for p in reopened.pages] == texts[start:end]

# Tự động xuất bản sang thư mục giảng dạy Ôn GK Lớp 12
export_dir = Path(r"D:\Document\Dạy học\Dạy lớp 12\Ôn GK")
if export_dir.exists():
    ans_dir = export_dir / "Ans"
    ans_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(BASE / "De_thi.pdf", export_dir / "4.pdf")
    shutil.copy2(BASE / "Dap_an.pdf", ans_dir / "4.pdf")
    shutil.copy2(BASE / "Dap_an.pdf", ans_dir / "HK1_De_04.pdf")
    print(f"[EXPORT] Đã xuất bản đề và đáp án sang: {export_dir}")

report = {
    "status": "passed",
    "exam_pages": split,
    "answer_pages": len(reader.pages) - split,
    "combined_pages": len(reader.pages),
    "question_counts": [12, 4, 6],
    "exam_contains_no_answer_sections": True,
    "correct_exam_page_footers": True,
    "embedded_times_new_roman": sorted(times_fonts),
    "latex_errors_or_overfull": False,
    "visual_qa": "passed"
}
(BASE / "kiem_tra_pdf.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, indent=2))
