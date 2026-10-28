"""Kiểm cấu trúc và hồ sơ nguồn; không chứng nhận đáp án hoặc nội dung toán học."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path

from index_tai_lieu import BASE_DIR, connect, load_matrix


def validate_exam(root, exam):
    structure = json.loads((root / "config/exam_structure.json").read_text(encoding="utf-8-sig"))
    curriculum = json.loads((root / "config/curriculum.json").read_text(encoding="utf-8-sig"))
    path = root / "Output" / f"De {exam}" / f"nguon_de{exam}.json"
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    matrix_id = data.get("matrix_id")
    if matrix_id == "giua_ki_1_chuong2_3":
        matrix = json.loads((root / "config/giua_ki_1_chuong2_3.json").read_text(encoding="utf-8-sig"))
    else:
        matrix = load_matrix(root, structure)
    if data.get("exam") != exam or data.get("duration_minutes") != structure["duration_minutes"]:
        raise ValueError("Sai số đề hoặc thời lượng.")
    questions = data.get("questions", [])
    expected = {(section["id"], number) for section in structure["sections"] for number in range(1, section["count"] + 1)}
    actual = [(q.get("section"), q.get("number")) for q in questions]
    if len(actual) != len(expected) or set(actual) != expected or any(type(q.get("number")) is not int for q in questions):
        raise ValueError("Hồ sơ phải đủ, không lặp: I=12, II=2, III=4, IV=4.")
    if data.get("matrix_id") != matrix["id"]:
        raise ValueError("Hồ sơ thiếu hoặc sai mã ma trận đang áp dụng.")
    slots = {f"{q['section']}.{q['number']}": q for q in matrix.get("questions", [])}
    pool_by_id = {s["id"]: s for s in matrix.get("skill_pool", [])}
    assigned = set()
    for question in questions:
        label = f"{question['section']}.{question['number']}"
        topic = question.get("topic")
        level = question.get("level")
        skill_id = question.get("skill_id") or question.get("skill_code")

        # Mode A: New flexible skill_pool validation
        if skill_id is not None:
            if topic not in matrix["allowed_topics"]:
                raise ValueError(f"{label}: chủ đề không khớp ma trận ({topic}).")
            if skill_id not in pool_by_id:
                raise ValueError(f"{label}: mã kỹ năng '{skill_id}' không tồn tại trong skill_pool của ma trận.")
            skill_def = pool_by_id[skill_id]
            if question["section"] not in skill_def.get("applicable_sections", [question["section"]]):
                raise ValueError(f"{label}: dạng bài {skill_id} không áp dụng cho phần {question['section']} của ma trận.")
            if topic != skill_def["topic"]:
                raise ValueError(f"{label}: chủ đề không khớp dạng bài trong ma trận ({skill_def['topic']}).")
            if question["section"] == "II":
                if level != "mixed":
                    raise ValueError(f"{label}: Phần II phải có level='mixed' theo ma trận.")
                items = question.get("statements", [])
                if len(items) != 4 or {s.get("id") for s in items} != set("abcd"):
                    raise ValueError(f"{label}: a–d hoặc mức độ từng ý không khớp ma trận.")
                if any(s.get("level") not in {"NB", "TH", "VD"} for s in items):
                    raise ValueError(f"{label}: mức độ từng ý đúng/sai không khớp ma trận.")
            elif level != skill_def["level"]:
                raise ValueError(f"{label}: mức độ không khớp dạng bài trong ma trận ({skill_def['level']}).")

        # Mode B: Slot-based validation (matrix_slot or default baseline slots)
        else:
            reference = question["matrix_slot"] if "matrix_slot" in question else label
            if not isinstance(reference, str) or reference not in slots:
                raise ValueError(f"{label}: mã dạng bài trong ma trận không hợp lệ.")
            slot = slots[reference]
            if slot["section"] != question["section"]:
                raise ValueError(f"{label}: chỉ được hoán đổi dạng bài trong cùng phần của ma trận.")
            if reference in assigned:
                raise ValueError(f"{label}: lặp dạng bài {reference} trong ma trận.")
            assigned.add(reference)
            if topic != slot["topic"]:
                raise ValueError(f"{label}: chủ đề không khớp ma trận ({slot['topic']}).")
            if level != slot["level"]:
                raise ValueError(f"{label}: mức độ không khớp ma trận ({slot['level']}).")
            if "statements" in slot:
                items = question.get("statements", [])
                if len(items) != 4 or {(s.get("id"), s.get("level")) for s in items} != {(s["id"], s["level"]) for s in slot["statements"]}:
                    raise ValueError(f"{label}: a–d hoặc mức độ từng ý không khớp ma trận.")

    # Global exam check
    exam_topics = {q["topic"] for q in questions}
    if not set(matrix["allowed_topics"]).issubset(exam_topics):
        raise ValueError(f"Đề thi phải bao phủ đủ các mạch kiến thức theo ma trận: {set(matrix['allowed_topics'])}.")

    sec2_topics = [q["topic"] for q in questions if q["section"] == "II"]
    if len(sec2_topics) == 2 and sec2_topics[0] == sec2_topics[1]:
        raise ValueError("Phần II phải chọn 2 chủ đề khác nhau theo ma trận để đảm bảo độ bao quát.")
    checked_sources = set()
    with connect(root) as conn:
        for question in questions:
            label = f"{question['section']}.{question['number']}"
            topic = question.get("topic")
            reason = question.get("scope_reason")
            if topic not in curriculum["topics"] or not isinstance(reason, str) or not reason.strip():
                raise ValueError(f"{label}: thiếu chủ đề/căn cứ phạm vi.")
            for role in ("dataset", "sgk"):
                source, page = question.get(f"{role}_source"), question.get(f"{role}_page")
                if type(page) is not int or page < 1:
                    raise ValueError(f"{label}: trang {role} phải là số nguyên từ 1.")
                document = conn.execute("SELECT * FROM documents WHERE source=? AND role=?", (source, role)).fetchone()
                row = conn.execute("SELECT * FROM chunks WHERE source=? AND page=?", (source, page)).fetchone()
                if document is None or row is None or document["review"] != "[]" or row["blocked"] != "[]" or topic not in json.loads(row["topics"]):
                    raise ValueError(f"{label}: nguồn {role} chưa hợp lệ/cùng chủ đề: {source}, trang {page}.")
                if source not in checked_sources:
                    file = root / source
                    if not file.resolve().is_relative_to(root.resolve()) or hashlib.sha256(file.read_bytes()).hexdigest() != document["sha256"]:
                        raise ValueError(f"Nguồn đã thay đổi, lập lại chỉ mục: {source}")
                    checked_sources.add(source)
    counts = dict(Counter(q["section"] for q in questions))
    print(f"[OK] {path}: {counts}; {structure['duration_minutes']} phút; đúng ma trận {matrix['id']}; nguồn và trang hợp lệ.")
    print("[LIMIT] Không kiểm tính điểm hoặc xác nhận độ khó thực tế; vẫn phải đọc PDF gốc, giải độc lập và duyệt bố cục.")
    return counts


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exam", type=int, required=True)
    args = parser.parse_args()
    if args.exam < 1:
        parser.error("Số đề phải lớn hơn 0")
    validate_exam(BASE_DIR, args.exam)
