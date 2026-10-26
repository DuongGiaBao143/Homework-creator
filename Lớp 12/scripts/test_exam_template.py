"""Kiểm tra mã đề, số trang và footer của template XeLaTeX lớp 12."""
from pathlib import Path
import subprocess
import tempfile
import unittest

from pypdf import PdfReader


class ExamTemplateTest(unittest.TestCase):
    def test_rendered_codes_and_answer_footer(self):
        template = (Path(__file__).resolve().parents[1] / "templates" / "de_mau.tex").read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory(prefix="exam-template-") as work:
            work = Path(work)
            for number in (1, 16, 100, 1000, 9999):
                with self.subTest(number=number):
                    source = template.replace(r"\newcommand{\soDe}{1}", rf"\newcommand{{\soDe}}{{{number}}}")
                    source = source.replace(r"\end{document}", r"\newpage\pagestyle{answers} Đáp án.\end{document}")
                    tex = work / f"exam_{number}.tex"
                    tex.write_text(source, encoding="utf-8")
                    result = subprocess.run(
                        ["xelatex", "-interaction=nonstopmode", "-halt-on-error", "-no-shell-escape", tex.name],
                        cwd=work, capture_output=True,
                    )
                    self.assertEqual(result.returncode, 0, result.stdout.decode(errors="replace")[-3000:])
                    pdf = PdfReader(tex.with_suffix(".pdf"))
                    self.assertEqual(len(pdf.pages), 2)
                    first, answers = (page.extract_text() for page in pdf.pages)
                    self.assertIn(f"Mã đề: {number:04d}", first)
                    self.assertIn("01 trang", first)
                    self.assertIn(f"Trang 1/1 - Mã đề: {number:04d}", first)
                    self.assertIn(f"Trang 2 - Mã đề: {number:04d}", answers)
                    self.assertNotIn("2/1", answers)
                    log = tex.with_suffix(".log").read_text(errors="replace")
                    for error in ("Overfull", "Missing character", "Undefined control sequence", "LaTeX Error"):
                        self.assertNotIn(error, log)


if __name__ == "__main__":
    unittest.main()
