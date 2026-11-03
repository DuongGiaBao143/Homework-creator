"""Tạo mã XeLaTeX đề giữa kì I số 12 (HK1_De_12) và ghi đáp án JSON."""
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent

KEY = {
    "I": ["A", "B", "C", "D", "B", "A", "C", "D", "A", "B", "D", "C"],
    "II": [
        [True, True, False, True],
        [True, True, True, False],
        [True, True, True, False],
        [True, True, True, False]
    ],
    "III": ["6", "15", "14", "3", "18", "920"]
}

(BASE / "dap_an.json").write_text(json.dumps(KEY, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"[BUILD] Đã cập nhật dap_an.json thành công!")
