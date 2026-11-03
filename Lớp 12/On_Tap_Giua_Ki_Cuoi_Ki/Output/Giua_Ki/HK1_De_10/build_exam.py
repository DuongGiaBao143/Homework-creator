"""Tạo mã XeLaTeX đề giữa kì I số 10 (HK1_De_10) và ghi đáp án JSON."""
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent

KEY = {
    "I": ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B", "C", "D"],
    "II": [
        [True, True, True, False],
        [True, True, True, False],
        [True, True, True, False],
        [True, True, True, False]
    ],
    "III": ["6", "16", "12", "550", "54", "690"]
}

(BASE / "dap_an.json").write_text(json.dumps(KEY, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"[BUILD] Đã cập nhật dap_an.json thành công!")
