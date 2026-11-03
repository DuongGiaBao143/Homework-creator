"""Tạo mã XeLaTeX đề giữa kì I số 11 (HK1_De_11) và ghi đáp án JSON."""
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent

KEY = {
    "I": ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B", "C", "D"],
    "II": [
        [True, True, False, True],
        [True, True, True, False],
        [True, True, True, False],
        [True, True, True, False]
    ],
    "III": ["7", "17", "7", "5", "16", "1200"]
}

(BASE / "dap_an.json").write_text(json.dumps(KEY, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"[BUILD] Đã cập nhật dap_an.json thành công!")
