"""Tách PDF đã duyệt vào Output lớp 10; không xuất sang kho lớp 12."""
import argparse
from pathlib import Path
import shutil

import pymupdf
from index_tai_lieu import BASE_DIR, fold


def validate_boundary(texts, answer_start):
    if not 2 <= answer_start <= len(texts):
        raise ValueError("Trang đáp án phải nằm sau phần đề và không vượt số trang.")
    starts = [i + 1 for i, text in enumerate(texts) if "bangdapantonghop" in fold(text).replace(" ", "")]
    if not starts or starts[0] != answer_start:
        raise ValueError("Trang chỉ định chưa khớp trang đầu BẢNG ĐÁP ÁN TỔNG HỢP; kiểm tra PDF.")


EXPORT_DIR = Path(r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\GK")


def split_pdf(root, exam, answer_start, force=False):
    folder = root / "Output" / f"De {exam}"
    source = folder / f"De {exam}.pdf"
    targets = [folder / f"{exam}.pdf", folder / f"{exam}_Ans.pdf"]
    if any(path.exists() for path in targets):
        if force:
            for p in targets:
                p.unlink(missing_ok=True)
        else:
            raise FileExistsError("Bản tách đã tồn tại; dùng --force (-f) để ghi đè hoặc di chuyển bản cũ trước khi xuất lại.")
    with pymupdf.open(source) as document:
        validate_boundary([page.get_text() for page in document], answer_start)
        ranges = [(0, answer_start - 2), (answer_start - 1, len(document) - 1)]
        staged = []
        try:
            for target, (first, last) in zip(targets, ranges):
                temporary = target.with_suffix(".pdf.tmp")
                with pymupdf.open() as part:
                    part.insert_pdf(document, from_page=first, to_page=last)
                    part.save(temporary, garbage=4, deflate=True)
                staged.append(temporary)
                with pymupdf.open(temporary) as check:
                    if len(check) != last - first + 1:
                        raise ValueError(f"Sai số trang đầu ra: {target}")
            for temporary, target in zip(staged, targets):
                temporary.rename(target)
        finally:
            for temporary in staged:
                temporary.unlink(missing_ok=True)

    # Xuất bản sang thư mục dạy học GK lớp 10
    if EXPORT_DIR.exists():
        ans_dir = EXPORT_DIR / "Ans"
        ans_dir.mkdir(parents=True, exist_ok=True)
        export_exam = EXPORT_DIR / f"{exam}.pdf"
        export_ans = ans_dir / f"{exam}.pdf"
        shutil.copy2(targets[0], export_exam)
        shutil.copy2(targets[1], export_ans)
        print(f"[EXPORT] Đề bài: {export_exam}")
        print(f"[EXPORT] Đáp án: {export_ans}")

    print("[OK] " + "\n[OK] ".join(map(str, targets)))
    return targets


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exam", type=int, required=True)
    parser.add_argument("--answer-start", type=int, required=True, help="Trang đầu đáp án, đếm theo PDF từ 1")
    parser.add_argument("--force", "-f", action="store_true", help="Ghi đè file PDF tách cũ nếu đã tồn tại")
    args = parser.parse_args()
    if args.exam < 1:
        parser.error("Số đề phải lớn hơn 0")
    split_pdf(BASE_DIR, args.exam, args.answer_start, force=args.force)
