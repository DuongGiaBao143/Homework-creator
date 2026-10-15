"""Kiểm tra quota nguồn Phần III mà không sửa chỉ mục hay mẫu đề đang dùng."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
import random
import tempfile
import unittest
from unittest.mock import patch

import index_tai_lieu as index


def chunk(source, page=1, score=12):
    return dict(source=source, location=f"page_{page}", text=f"Câu {page}. Bài toán tối ưu có đầy đủ dữ kiện.",
                topics=["dang_ham_so_toi_uu_thuc_te"], vdc_score=score)


class Part3SourcesTest(unittest.TestCase):
    def test_exact_sources_and_seed(self):
        chunks = [chunk(source, page) for source in index.PART3_HARD_SOURCES for page in range(1, 9)]
        chunks += [chunk("Toán thực tế.pdf", score=1000), chunk("Bản sao Vận dụng cao.pdf", score=1000)]
        chunks += [chunk(index.PART3_HARD_SOURCES[0], 99, score=0.1)]
        first = index.sample_part3_hard_sources(chunks, random.Random(13*2027))
        again = index.sample_part3_hard_sources(chunks, random.Random(13*2027))
        self.assertEqual(first, again)
        self.assertEqual(len(first), 6)
        self.assertEqual({c["source"] for c in first}, set(index.PART3_HARD_SOURCES))
        self.assertEqual(len({(c["source"], c["location"]) for c in first}), 6)
        self.assertTrue(all(c["vdc_score"] > 1.5 for c in first))

    def test_quota_is_shared_by_three_files(self):
        only_one_source = [chunk(index.PART3_HARD_SOURCES[1], page) for page in (1, 2)]
        self.assertEqual(len(index.sample_part3_hard_sources(only_one_source, random.Random(1))), 2)
        nested_sources = [chunk(str(Path("chuyen_de") / index.PART3_HARD_SOURCES[2]), page) for page in (1, 2)]
        self.assertEqual(len(index.sample_part3_hard_sources(nested_sources, random.Random(1))), 2)

    def test_shortage_does_not_overwrite_existing_sample(self):
        chunks = [chunk(index.PART3_HARD_SOURCES[0]), chunk("Toán thực tế.pdf", score=1000)]
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent) as tmp:
            self.assertEqual(Path(tmp).resolve().parent, Path(__file__).resolve().parent)
            target = Path(tmp)/"sample_de_13.md"
            target.write_text("Mẫu cũ phải được giữ nguyên", encoding="utf-8")
            with patch.object(index, "INDEX_DIR", Path(tmp)), patch.object(index, "sync_index", return_value=chunks):
                with self.assertRaisesRegex(ValueError, "Không đủ 2"):
                    index.sample_for_new_exam(13)
            self.assertEqual(target.read_text(encoding="utf-8"), "Mẫu cũ phải được giữ nguyên")

    def test_real_index_output_and_existing_exam_compatibility(self):
        chunks = [json.loads(line) for line in index.CHUNKS_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent) as tmp, patch.object(index, "INDEX_DIR", Path(tmp)), \
                patch.object(index, "sync_index", return_value=chunks), redirect_stdout(StringIO()):
            self.assertEqual(Path(tmp).resolve().parent, Path(__file__).resolve().parent)
            index.sample_for_new_exam(13)
            sample = (Path(tmp)/"sample_de_13.md").read_text(encoding="utf-8")
            self.assertIn("ít nhất 2/6 câu khó", sample)
            reserved = sample.split("# KHU VỰC 0:", 1)[1].split("# KHU VỰC I:", 1)[0]
            for source in index.PART3_HARD_SOURCES:
                self.assertEqual(reserved.count(f"### Nguồn: `{source}`"), 2)
            self.assertIn("KHU VỰC II:", sample)
            index.sample_for_new_exam(12)
            old_sample = (Path(tmp)/"sample_de_12.md").read_text(encoding="utf-8")
            self.assertNotIn("KHU VỰC 0:", old_sample)
            self.assertNotIn("ít nhất 2/6 câu khó", old_sample)


if __name__ == "__main__":
    unittest.main()
