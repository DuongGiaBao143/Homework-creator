# Hồ sơ nguồn Đề số 10 - Ôn thi Giữa kì 1 Toán 10

- **Thời gian làm bài:** 90 phút.
- **Cấu trúc:** 12 Trắc nghiệm (Phần I) + 2 Đúng/Sai (Phần II) + 4 Trả lời ngắn (Phần III) + 4 Tự luận (Phần IV).
- **Ma trận áp dụng:** `config/giua_ki_1.json` (Blueprint Quota & Skill Pool 43 kỹ năng GDPT 2018).
- **Mã ma trận:** `giua_ki_1_ba_mach`.
- **Kiểm định giải độc lập:** [verify_de10.py](verify_de10.py) đã pass 100% assertions bằng SymPy/NumPy.
- **Xác thực ma trận & hồ sơ:** `python scripts/check_exam.py --exam 10` đạt chuẩn `[OK]`.

---

## Bảng đối chiếu 22 câu hỏi

| Câu | Phần | Mạch kiến thức | Mức độ | Mã Skill | Nguồn Dataset & Trang | Nguồn SGK KNTT & Trang |
| :---: | :---: | :--- | :---: | :---: | :--- | :--- |
| **1** | I | `menh_de_tap_hop` | NB | `TH_NB_04` | chuyen-de-phuong-phap-toa-do-trong-mat-phang (tr.69) | SGK Tập 1 (tr.6) |
| **2** | I | `menh_de_tap_hop` | NB | `MD_NB_01` | pp-giai-toan-va-bai-tap-menh-de-va-tap-hop (tr.74) | SGK Tập 1 (tr.6) |
| **3** | I | `menh_de_tap_hop` | TH | `TH_TH_02` | bo-de-kiem-tra-theo-bai-hoc-toan-10-hk1 (tr.21) | SGK Tập 1 (tr.6) |
| **4** | I | `menh_de_tap_hop` | NB | `MD_NB_05` | pp-giai-toan-va-bai-tap-menh-de-va-tap-hop (tr.6) | SGK Tập 1 (tr.6) |
| **5** | I | `bpt_hai_an` | NB | `BPT_NB_04` | chuyen-de-bpt-va-he-bpt-dinh-huong-moi (tr.2) | SGK Tập 1 (tr.23) |
| **6** | I | `bpt_hai_an` | NB | `BPT_NB_03` | chuyen-de-bpt-va-he-bpt-dinh-huong-moi (tr.81) | SGK Tập 1 (tr.23) |
| **7** | I | `bpt_hai_an` | NB | `BPT_NB_05` | de-kiem-tra-theo-bai-hoc-chu-de-bpt (tr.53) | SGK Tập 1 (tr.23) |
| **8** | I | `bpt_hai_an` | TH | `BPT_TH_01` | chuyen-de-bpt-va-he-bpt-dinh-huong-moi (tr.132) | SGK Tập 1 (tr.23) |
| **9** | I | `he_thuc_luong` | NB | `LG_NB_01` | de-kiem-tra-theo-bai-hoc-he-thuc-luong (tr.3) | SGK Tập 1 (tr.34) |
| **10** | I | `he_thuc_luong` | TH | `LG_TH_02` | de-kiem-tra-theo-bai-hoc-he-thuc-luong (tr.12) | SGK Tập 1 (tr.34) |
| **11** | I | `he_thuc_luong` | NB | `LG_NB_03` | chuyen-de-toan-10-he-thuc-luong-va-ung-dung (tr.89) | SGK Tập 1 (tr.34) |
| **12** | I | `he_thuc_luong` | NB | `HTL_NB_01` | chuyen-de-toan-10-he-thuc-luong-va-ung-dung (tr.85) | SGK Tập 1 (tr.34) |
| **13** | II | `menh_de_tap_hop` | Mixed | `TH_NB_03` | pp-giai-toan-va-bai-tap-menh-de-va-tap-hop (tr.67) | SGK Tập 1 (tr.6) |
| **14** | II | `he_thuc_luong` | Mixed | `HTL_NB_01` | chuyen-de-he-thuc-luong-chuong-trinh-moi (tr.31) | SGK Tập 1 (tr.34) |
| **15** | III | `menh_de_tap_hop` | TH | `TH_TH_02` | pp-giai-toan-va-bai-tap-menh-de-va-tap-hop (tr.16) | SGK Tập 1 (tr.6) |
| **16** | III | `bpt_hai_an` | VD | `BPT_VD_03` | chuyen-de-bpt-va-he-bpt-dinh-huong-moi (tr.80) | SGK Tập 1 (tr.23) |
| **17** | III | `he_thuc_luong` | TH | `HTL_TH_01` | chuyen-de-toan-10-he-thuc-luong-va-ung-dung (tr.39) | SGK Tập 1 (tr.34) |
| **18** | III | `he_thuc_luong` | VD | `HTL_VD_03` | chuyen-de-he-thuc-luong-chuong-trinh-moi (tr.44) | SGK Tập 1 (tr.34) |
| **19** | IV | `menh_de_tap_hop` | TH | `TH_TH_05` | de-kiem-tra-theo-bai-hoc-menh-de (tr.48) | SGK Tập 1 (tr.6) |
| **20** | IV | `he_thuc_luong` | TH | `LG_TH_02` | chuyen-de-he-thuc-luong-chuong-trinh-moi (tr.66) | SGK Tập 1 (tr.34) |
| **21** | IV | `he_thuc_luong` | VD | `HTL_VD_01` | chuyen-de-he-thuc-luong-chuong-trinh-moi (tr.22) | SGK Tập 1 (tr.34) |
| **22** | IV | `bpt_hai_an` | VD | `BPT_VD_01` | toan-thuc-te-he-bat-phuong-trinh (tr.152) | SGK Tập 1 (tr.23) |
