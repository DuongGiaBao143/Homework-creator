"""Kiểm các ranh giới có thể làm lọt nội dung hoặc ghi đè ngữ liệu cũ."""
from contextlib import redirect_stdout
from io import StringIO
import json
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch

import index_tai_lieu as rag
from check_exam import validate_exam
from split_pdf import validate_boundary


CONFIG = json.loads((rag.BASE_DIR / "config/curriculum.json").read_text(encoding="utf-8"))


def copy_rules(root):
    for name in ("config/curriculum.json", "config/exam_structure.json", "config/giua_ki_1.json"):
        target = root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes((rag.BASE_DIR / name).read_bytes())


def valid_manifest(root):
    import hashlib
    copy_rules(root)
    structure = json.loads((root / "config/exam_structure.json").read_text(encoding="utf-8"))
    matrix = rag.load_matrix(root, structure)
    with rag.connect(root) as conn:
        for topic in matrix["allowed_topics"]:
            for role in ("dataset", "sgk"):
                source = f"Nguon_Tai_Lieu/{role}/{topic}.txt"
                path = root / source
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(topic, encoding="utf-8")
                digest = hashlib.sha256(path.read_bytes()).hexdigest()
                conn.execute("INSERT INTO documents VALUES (?,?,?,?,?)", (source, digest, role, "{}", "[]"))
                conn.execute("INSERT INTO chunks(source,page,text,method,topics) VALUES (?,?,?,?,?)",
                             (source, 1, topic, "text", json.dumps([topic])))
    questions = []
    for slot in matrix["questions"]:
        question = {key: slot[key] for key in ("section", "number", "topic", "level")}
        question.update(dataset_source=f"Nguon_Tai_Lieu/dataset/{slot['topic']}.txt", dataset_page=1,
                        sgk_source=f"Nguon_Tai_Lieu/sgk/{slot['topic']}.txt", sgk_page=1, scope_reason="Phương pháp theo bài SGK đã đối chiếu")
        if "statements" in slot:
            question["statements"] = [{"id": s["id"], "level": s["level"]} for s in slot["statements"]]
        questions.append(question)
    folder = root / "Output/De 1"
    folder.mkdir(parents=True)
    data = {"exam": 1, "duration_minutes": 90, "matrix_id": matrix["id"], "questions": questions}
    return folder / "nguon_de1.json", data


class RagTest(unittest.TestCase):
    def test_scope_filter(self):
        self.assertFalse(rag.blocked_reasons("Phương sai của mẫu số liệu không ghép nhóm", CONFIG))
        self.assertFalse(rag.blocked_reasons("Mẫu sốliệu khôngghép nhóm", CONFIG))
        for text in ("Mẫu số liệu ghép nhóm", "Dùng đạo hàm để tối ưu parabol", "Công thức Bayes",
                     "Xác suất có điều kiện", "Hai biến cố độc lập", "Hệ tọa độ Oxyz"):
            with self.subTest(text=text):
                self.assertTrue(rag.blocked_reasons(text, CONFIG))

    def test_sgk_ranges_and_ocr_glued_words(self):
        source = CONFIG["books"]["2"]
        self.assertEqual(rag.sgk_anchor(source, 12, CONFIG), (["ham_so_bac_hai"], 11))
        self.assertEqual(rag.sgk_anchor(source, 20, CONFIG), (["tam_thuc_bac_hai"], 19))
        self.assertEqual(rag.sgk_anchor(source, 1, CONFIG), ([], 0))
        self.assertIn("ham_so_bac_hai", rag.classify("Hàm sốbậc hai và đồthị parabol", "test.pdf", CONFIG))

    def test_search_filters_and_unaccented_query(self):
        with tempfile.TemporaryDirectory(dir=rag.BASE_DIR / "scripts") as temporary:
            root = Path(temporary)
            with rag.connect(root) as conn:
                for source, review in (("Nguon_Tai_Lieu/dataset/ok.pdf", "[]"), ("Nguon_Tai_Lieu/dataset/toan-11.pdf", '["toan-11"]')):
                    conn.execute("INSERT INTO documents VALUES (?,?,?,?,?)", (source, "hash", "dataset", "{}", review))
                for source, blocked in (("Nguon_Tai_Lieu/dataset/ok.pdf", "[]"), ("Nguon_Tai_Lieu/dataset/toan-11.pdf", "[]"), ("Nguon_Tai_Lieu/dataset/ok.pdf", '["đạo hàm"]')):
                    cur = conn.execute("INSERT INTO chunks(source,page,text,method,topics,blocked) VALUES (?,?,?,?,?,?)",
                                       (source, 1, "Lợi nhuận hàm số bậc hai", "text", '["ham_so_bac_hai"]', blocked))
                    conn.execute("INSERT INTO chunks_fts(rowid,terms) VALUES (?,?)", (cur.lastrowid, rag.fold("Lợi nhuận hàm số bậc hai")))
                rows = rag.search(conn, "loi nhuan", topic="ham_so_bac_hai", role="dataset")
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0]["source"], "Nguon_Tai_Lieu/dataset/ok.pdf")

    def test_cache_content_hash_dedup_and_removed_source(self):
        with tempfile.TemporaryDirectory(dir=rag.BASE_DIR / "scripts") as temporary, redirect_stdout(StringIO()):
            root = Path(temporary)
            for folder in ("dataset", "sgk"):
                (root / "Nguon_Tai_Lieu" / folder).mkdir(parents=True)
            (root / "config").mkdir()
            (root / "config/curriculum.json").write_text(json.dumps(CONFIG), encoding="utf-8")
            source = root / "Nguon_Tai_Lieu/dataset/a.txt"
            source.write_text("Hàm số bậc hai và đồ thị parabol. " * 5, encoding="utf-8")
            (root / "Nguon_Tai_Lieu/dataset/a (1).txt").write_bytes(source.read_bytes())
            (root / "Nguon_Tai_Lieu/sgk/book.txt").write_text("Mệnh đề và tập hợp. " * 5, encoding="utf-8")
            first = rag.sync_index(root, workers=1)
            self.assertEqual((first["physical_files"], first["unique_files"]), (3, 2))
            with patch.object(rag, "extract_file", side_effect=AssertionError("Cache must avoid extraction")):
                self.assertEqual(rag.sync_index(root, workers=1)["cache_hits"], 2)
            source.write_text("Hàm số bậc hai và đồ thị parabol. " * 4, encoding="utf-8")
            # The edited original and the formerly identical copy are now two distinct documents.
            self.assertEqual(rag.sync_index(root, workers=1)["extracted_files_this_run"], 2)
            source.unlink()
            rag.sync_index(root, workers=1)
            with rag.connect(root) as conn:
                self.assertIsNone(conn.execute("SELECT source FROM documents WHERE source='Nguon_Tai_Lieu/dataset/a.txt'").fetchone())

    def test_failed_extract_keeps_existing_cache(self):
        with tempfile.TemporaryDirectory(dir=rag.BASE_DIR / "scripts") as temporary, redirect_stdout(StringIO()):
            root = Path(temporary)
            for folder in ("dataset", "sgk"):
                (root / "Nguon_Tai_Lieu" / folder).mkdir(parents=True)
            (root / "config").mkdir()
            (root / "config/curriculum.json").write_text(json.dumps(CONFIG), encoding="utf-8")
            (root / "Nguon_Tai_Lieu/sgk/book.txt").write_text("Hàm số bậc hai và đồ thị parabol. " * 3, encoding="utf-8")
            rag.sync_index(root, workers=1)
            (root / "Nguon_Tai_Lieu/sgk/book.txt").write_text("Nội dung mới chưa đọc được", encoding="utf-8")
            with patch.object(rag, "extract_file", side_effect=RuntimeError("OCR failed")):
                with self.assertRaisesRegex(RuntimeError, "chưa lấy mẫu"):
                    rag.sync_index(root, workers=1)
            with rag.connect(root) as conn:
                self.assertIn("parabol", conn.execute("SELECT text FROM chunks").fetchone()[0])

    def test_shortage_does_not_overwrite_sample(self):
        with tempfile.TemporaryDirectory(dir=rag.BASE_DIR / "scripts") as temporary:
            root = Path(temporary)
            copy_rules(root)
            with rag.connect(root):
                pass
            target = root / "_index/sample_de_1.md"
            target.write_text("Giữ mẫu cũ", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Thiếu SGK"):
                rag.sample_for_new_exam(root, 1)
            self.assertEqual(target.read_text(encoding="utf-8"), "Giữ mẫu cũ")

    def test_structure_rejects_old_12_4_6(self):
        with tempfile.TemporaryDirectory(dir=rag.BASE_DIR / "scripts") as temporary:
            root = Path(temporary)
            copy_rules(root)
            folder = root / "Output/De 1"
            folder.mkdir(parents=True)
            questions = [{"section": section, "number": i} for section, count in (("I", 12), ("II", 4), ("III", 6)) for i in range(1, count + 1)]
            (folder / "nguon_de1.json").write_text(json.dumps({"exam": 1, "duration_minutes": 90, "questions": questions}), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "IV=4"):
                validate_exam(root, 1)

    def test_valid_exam_manifest_and_stale_source(self):
        with tempfile.TemporaryDirectory(dir=rag.BASE_DIR / "scripts") as temporary, redirect_stdout(StringIO()):
            root = Path(temporary)
            path, data = valid_manifest(root)
            path.write_text(json.dumps(data), encoding="utf-8")
            self.assertEqual(validate_exam(root, 1), {"I": 12, "II": 2, "III": 4, "IV": 4})
            (root / "Nguon_Tai_Lieu/dataset/menh_de_tap_hop.txt").write_text("Nguồn đã thay đổi", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Nguồn đã thay đổi"):
                validate_exam(root, 1)

    def test_manifest_allows_reordering_within_every_section(self):
        with tempfile.TemporaryDirectory(dir=rag.BASE_DIR / "scripts") as temporary, redirect_stdout(StringIO()):
            root = Path(temporary)
            path, data = valid_manifest(root)
            for section in ("I", "II", "III", "IV"):
                questions = [q for q in data["questions"] if q["section"] == section]
                for q in questions:
                    q["matrix_slot"] = f"{section}.{q['number']}"
                    q["number"] = len(questions) + 1 - q["number"]
            path.write_text(json.dumps(data), encoding="utf-8")
            self.assertEqual(validate_exam(root, 1), {"I": 12, "II": 2, "III": 4, "IV": 4})
            data["questions"][0]["level"] = "VD"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "mức độ không khớp ma trận"):
                validate_exam(root, 1)

    def test_manifest_rejects_duplicate_cross_section_and_unknown_slots(self):
        with tempfile.TemporaryDirectory(dir=rag.BASE_DIR / "scripts") as temporary:
            root = Path(temporary)
            path, original = valid_manifest(root)
            for reference in ("I.2", "IV.1", "I.13", "II.0", "", None, 1, []):
                with self.subTest(reference=reference):
                    data = json.loads(json.dumps(original))
                    data["questions"][0]["matrix_slot"] = reference
                    path.write_text(json.dumps(data), encoding="utf-8")
                    with self.assertRaisesRegex(ValueError, "ma trận"):
                        validate_exam(root, 1)

    def test_manifest_rejects_wrong_topic_level_and_true_false(self):
        with tempfile.TemporaryDirectory(dir=rag.BASE_DIR / "scripts") as temporary:
            root = Path(temporary)
            path, original = valid_manifest(root)
            cases = ("all_sets", "outside_scope", "wrong_level", "wrong_statement", "missing_statement", "wrong_matrix")
            for case in cases:
                with self.subTest(case=case):
                    data = json.loads(json.dumps(original))
                    if case == "all_sets":
                        for q in data["questions"]:
                            q["topic"] = "menh_de_tap_hop"
                    elif case == "outside_scope":
                        data["questions"][0]["topic"] = "xac_suat"
                    elif case == "wrong_level":
                        data["questions"][0]["level"] = "VD"
                    elif case == "wrong_statement":
                        data["questions"][12]["statements"][0]["level"] = "VD"
                    elif case == "missing_statement":
                        data["questions"][12]["statements"].pop()
                    else:
                        data["matrix_id"] = "wrong"
                    path.write_text(json.dumps(data), encoding="utf-8")
                    with self.assertRaisesRegex(ValueError, "ma trận"):
                        validate_exam(root, 1)

    def test_sample_uses_matrix_slots_and_preserves_seed(self):
        with tempfile.TemporaryDirectory(dir=rag.BASE_DIR / "scripts") as temporary, redirect_stdout(StringIO()):
            root = Path(temporary)
            copy_rules(root)
            structure = json.loads((root / "config/exam_structure.json").read_text(encoding="utf-8"))
            matrix = rag.load_matrix(root, structure)

            def fake_search(conn, query, topic=None, role=None, limit=6):
                base = matrix["allowed_topics"].index(topic) * 100
                return [{"id": base + n, "source": f"Nguon_Tai_Lieu/{role}/{topic}.pdf", "page": n, "book_page": n if role == "sgk" else None,
                         "text": f"Nội dung {topic} trang {n}", "method": "text", "role": role, "topics": [topic], "blocked": []}
                        for n in range(1, 2 if role == "sgk" else 41)]

            with patch.object(rag, "search", side_effect=fake_search) as retrieval:
                target = rag.sample_for_new_exam(root, 1, seed=17)
                before = target.read_bytes()
                rag.sample_for_new_exam(root, 1, seed=17)
                self.assertEqual(target.read_bytes(), before)
                self.assertEqual({call.kwargs["topic"] for call in retrieval.call_args_list}, set(matrix["allowed_topics"]))
            text = target.read_text(encoding="utf-8")
            self.assertIn(matrix["id"], text)
            self.assertIn("Seed: `17`", text)
            self.assertEqual(text.count("### SGK:"), 3)
            self.assertEqual(text.count("### DATASET:"), 22)
            blueprint = re.findall(r"^\| ([IV]+\.\d+) \|", text, re.MULTILINE)
            self.assertEqual(len(blueprint), 22)
            assigned = re.findall(r"ngữ liệu cho dạng bài ([IV]+\.\d+) trong ma trận", text)
            self.assertEqual(set(assigned), {f"{q['section']}.{q['number']}" for q in matrix["questions"]})
            self.assertEqual(len(assigned), 22)
            self.assertEqual(set(blueprint), set(assigned))
            self.assertFalse(target.with_suffix(".json").exists())

    def test_invalid_matrix_does_not_overwrite_sample(self):
        with tempfile.TemporaryDirectory(dir=rag.BASE_DIR / "scripts") as temporary:
            root = Path(temporary)
            copy_rules(root)
            (root / "_index").mkdir()
            target = root / "_index/sample_de_1.md"
            target.write_text("Mẫu đã có", encoding="utf-8")
            file = root / "config/giua_ki_1.json"
            matrix = json.loads(file.read_text(encoding="utf-8"))
            matrix["questions"].pop()
            file.write_text(json.dumps(matrix), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Ma trận"):
                rag.sample_for_new_exam(root, 1)
            self.assertEqual(target.read_text(encoding="utf-8"), "Mẫu đã có")

    def test_pdf_split_boundary(self):
        validate_boundary(["PHẦN I. Đề bài", "BẢNG ĐÁP ÁN TỔNG HỢP", "Lời giải"], 2)
        for start in (1, 3, 4):
            with self.assertRaises(ValueError):
                validate_boundary(["Đề", "BẢNG ĐÁP ÁN TỔNG HỢP", "Lời giải"], start)


if __name__ == "__main__":
    unittest.main()
