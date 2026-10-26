import os, sys, pypdf, pymupdf
for n in (13, 14):
    src = rf"d:\Tao_De\Lớp 12\On_Thi_THPTQG\Output\De {n}\De {n}.pdf"
    r = pypdf.PdfReader(src)
    idx = next(i for i, p in enumerate(r.pages) if "BẢNG ĐÁP ÁN TỔNG HỢP" in (p.extract_text() or ""))
    ex = r"D:\Document\Dạy học\Đề ko đáp án\PRIVATE"
    an = os.path.join(ex, "Ans"); os.makedirs(an, exist_ok=True)
    w = pypdf.PdfWriter(); [w.add_page(r.pages[i]) for i in range(idx)]
    w.write(os.path.join(ex, f"{n}.pdf"))
    w = pypdf.PdfWriter(); [w.add_page(r.pages[i]) for i in range(idx, len(r.pages))]
    w.write(os.path.join(an, f"{n}.pdf"))
    print(n, "exam pages:", idx, "answer pages:", len(r.pages) - idx)
    doc = pymupdf.open(src)
    for pno in range(idx):
        doc[pno].get_pixmap(dpi=70).save(rf"d:\Tao_De\Lớp 12\On_Thi_THPTQG\Output\De {n}\prev_{pno+1}.png")
