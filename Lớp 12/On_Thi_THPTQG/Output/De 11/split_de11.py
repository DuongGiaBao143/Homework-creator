import os
import pypdf

src_pdf = r"d:\Tao_De\Lớp 12\On_Thi_THPTQG\Output\De 11\De 11.pdf"
dest_exam_dir = r"D:\Document\Dạy học\Đề ko đáp án\PRIVATE"
dest_ans_dir = r"D:\Document\Dạy học\Đề ko đáp án\PRIVATE\Ans"

os.makedirs(dest_exam_dir, exist_ok=True)
os.makedirs(dest_ans_dir, exist_ok=True)

dest_exam_pdf = os.path.join(dest_exam_dir, "11.pdf")
dest_ans_pdf = os.path.join(dest_ans_dir, "11.pdf")

reader = pypdf.PdfReader(src_pdf)
total_pages = len(reader.pages)
print(f"Tổng số trang file gốc: {total_pages}")

split_idx = -1
for i, page in enumerate(reader.pages):
    text = page.extract_text() or ""
    if "BẢNG ĐÁP ÁN TỔNG HỢP" in text:
        split_idx = i
        break

if split_idx == -1:
    raise ValueError("Không tìm thấy trang BẢNG ĐÁP ÁN TỔNG HỢP!")

print(f"Trang bắt đầu đáp án (0-indexed): {split_idx} (Trang {split_idx + 1} thực tế)")

# 1. Xuất file Đề thi (từ trang 0 đến split_idx - 1)
writer_exam = pypdf.PdfWriter()
for i in range(split_idx):
    writer_exam.add_page(reader.pages[i])

with open(dest_exam_pdf, "wb") as f_out:
    writer_exam.write(f_out)

print(f"[OK] Đã xuất file Đề thi ({split_idx} trang) tới: {dest_exam_pdf}")

# 2. Xuất file Đáp án & Hướng dẫn giải chi tiết (từ split_idx đến hết)
writer_ans = pypdf.PdfWriter()
for i in range(split_idx, total_pages):
    writer_ans.add_page(reader.pages[i])

with open(dest_ans_pdf, "wb") as f_out:
    writer_ans.write(f_out)

print(f"[OK] Đã xuất file Đáp án & Lời giải ({total_pages - split_idx} trang) tới: {dest_ans_pdf}")
