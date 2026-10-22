# Hồ sơ nguồn Đề số 07 - Ôn thi Giữa kì 1 Toán 10

- **Thời gian làm bài:** 90 phút.
- **Cấu trúc:** 12 Trắc nghiệm (I) + 2 Đúng/Sai (II) + 4 Trả lời ngắn (III) + 4 Tự luận (IV).
- **Ma trận áp dụng:** `config/giua_ki_1.json` (Blueprint Quota & Skill Pool 43 kỹ năng GDPT 2018).
- **Kiểm định giải độc lập:** [verify_de7.py](verify_de7.py) đã pass 100% assertions bằng SymPy/NumPy.
- **Xác thực ma trận:** `check_exam.py --exam 7` đạt `[OK]`.

---

## Bảng đối chiếu 22 câu hỏi

| Câu | Phần | Mạch kiến thức | Mức độ | Mã Skill | Nguồn Dataset & Trang | Nguồn SGK KNTT & Trang |
| :---: | :---: | :--- | :---: | :---: | :--- | :--- |
| **1** | I | `menh_de_tap_hop` | NB | `MD_NB_01` | de-kiem-tra-theo-bai-hoc-chu-de-menh-de-va-tap-hop (tr.53) | SGK Tập 1 (tr.6) |
| **2** | I | `menh_de_tap_hop` | NB | `MD_NB_02` | de-kiem-tra-theo-bai-hoc-chu-de-menh-de-va-tap-hop (tr.20) | SGK Tập 1 (tr.6) |
| **3** | I | `menh_de_tap_hop` | NB | `TH_NB_03` | pp-giải-mệnh-đề-tập-hợp (tr.83) | SGK Tập 1 (tr.6) |
| **4** | I | `menh_de_tap_hop` | TH | `TH_TH_01` | pp-giải-mệnh-đề-tập-hợp (tr.89) | SGK Tập 1 (tr.6) |
| **5** | I | `bpt_hai_an` | NB | `BPT_NB_01` | toan-thuc-te-he-bat-phuong-trinh (tr.33) | SGK Tập 1 (tr.23) |
| **6** | I | `bpt_hai_an` | NB | `BPT_NB_02` | toan-thuc-te-he-bat-phuong-trinh (tr.114) | SGK Tập 1 (tr.23) |
| **7** | I | `bpt_hai_an` | NB | `BPT_NB_03` | chuyen-de-bpt-va-he-bpt-toan-10-dinh-huong (tr.23) | SGK Tập 1 (tr.23) |
| **8** | I | `bpt_hai_an` | TH | `BPT_TH_01` | chuyen-de-bpt-va-he-bpt-toan-10-dinh-huong (tr.132) | SGK Tập 1 (tr.23) |
| **9** | I | `he_thuc_luong` | NB | `LG_NB_01` | chuyen-de-he-thuc-luong-chuong-trinh-moi (tr.51) | SGK Tập 1 (tr.34) |
| **10** | I | `he_thuc_luong` | NB | `HTL_NB_01` | chuyen-de-he-thuc-luong-chuong-trinh-moi (tr.144) | SGK Tập 1 (tr.34) |
| **11** | I | `he_thuc_luong` | TH | `LG_TH_01` | de-kiem-tra-theo-bai-hoc-chu-de-he-thuc-luong (tr.6) | SGK Tập 1 (tr.34) |
| **12** | I | `he_thuc_luong` | TH | `LG_TH_02` | chuyen-de-he-thuc-luong-chuong-trinh-moi (tr.88) | SGK Tập 1 (tr.34) |
| **13** | II | `menh_de_tap_hop` | Mixed | `TH_TH_01` | pp-giải-mệnh-đề-tập-hợp (tr.89) | SGK Tập 1 (tr.6) |
| **14** | II | `he_thuc_luong` | Mixed | `HTL_TH_03` | chuyen-de-toan-10-he-thuc-luong-va-ung-dung (tr.54) | SGK Tập 1 (tr.34) |
| **15** | III | `menh_de_tap_hop` | TH | `TH_TH_04` | ngan-hang-cau-hoi-le-minh-kha (tr.87) | SGK Tập 1 (tr.6) |
| **16** | III | `bpt_hai_an` | VD | `BPT_VD_03` | toan-thuc-te-he-bat-phuong-trinh (tr.170) | SGK Tập 1 (tr.23) |
| **17** | III | `he_thuc_luong` | TH | `HTL_TH_02` | chuyen-de-toan-10-he-thuc-luong-va-ung-dung (tr.92) | SGK Tập 1 (tr.34) |
| **18** | III | `he_thuc_luong` | VD | `HTL_VD_01` | chuyen-de-toan-10-he-thuc-luong-va-ung-dung (tr.68) | SGK Tập 1 (tr.34) |
| **19** | IV | `menh_de_tap_hop` | VD | `TH_VD_01` | ngan-hang-cau-hoi-le-minh-kha (tr.84) | SGK Tập 1 (tr.6) |
| **20** | IV | `he_thuc_luong` | TH | `LG_TH_02` | chuyen-de-toan-10-he-thuc-luong-va-ung-dung (tr.3) | SGK Tập 1 (tr.34) |
| **21** | IV | `he_thuc_luong` | VD | `HTL_VD_01` | de-kiem-tra-theo-bai-hoc-chu-de-he-thuc-luong (tr.47) | SGK Tập 1 (tr.34) |
| **22** | IV | `bpt_hai_an` | VD | `BPT_VD_01` | toan-thuc-te-he-bat-phuong-trinh (tr.171) | SGK Tập 1 (tr.23) |
