"""Tạo mã XeLaTeX đề giữa kì I số 07 (HK1_De_07) và ghi đáp án JSON."""
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent

KEY = {
    "I": ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B", "C", "D"],
    "II": [
        [True, True, False, True],
        [True, True, True, False],
        [True, False, True, True],
        [True, True, True, False]
    ],
    "III": ["14", "10", "7", "3", "900", "430"]
}

(BASE / "dap_an.json").write_text(json.dumps(KEY, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"[BUILD] Đã cập nhật dap_an.json thành công!")
