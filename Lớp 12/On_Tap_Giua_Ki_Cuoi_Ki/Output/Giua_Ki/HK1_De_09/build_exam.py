"""Tạo mã XeLaTeX đề giữa kì I số 09 (HK1_De_09) và ghi đáp án JSON."""
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent

KEY = {
    "I": ["B", "D", "A", "C", "A", "C", "D", "B", "D", "A", "B", "C"],
    "II": [
        [True, True, False, True],
        [True, True, True, False],
        [True, True, True, False],
        [True, True, False, True]
    ],
    "III": ["5", "11", "8", "9", "10", "70"]
}

(BASE / "dap_an.json").write_text(json.dumps(KEY, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"[BUILD] Đã cập nhật dap_an.json thành công!")
