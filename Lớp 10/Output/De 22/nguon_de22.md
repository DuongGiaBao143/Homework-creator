# Hồ sơ nguồn Đề số 22 - Ôn thi Giữa kì 1 Toán 10

- **Thời gian làm bài:** 90 phút.
- **Cấu trúc:** 12 Trắc nghiệm (I) + 2 Đúng/Sai (II) + 4 Trả lời ngắn (III) + 4 Tự luận (IV).
- **Ma trận áp dụng:** `config/giua_ki_1_chuong2_3.json` (Giới hạn Chương II: BPT & Hệ BPT bậc nhất hai ẩn và Chương III: Hệ thức lượng trong tam giác).
- **Kiểm định giải độc lập:** [verify_de22.py](verify_de22.py) đã pass 100% assertions bằng SymPy/NumPy.
- **Xác thực ma trận:** `check_exam.py --exam 22` đạt chuẩn [OK].

---

## Bảng đối chiếu 22 câu hỏi

| Câu | Phần | Mạch kiến thức | Mức độ | Mã Skill | Nguồn Dataset & Trang | Nguồn SGK KNTT & Trang |
| :---: | :---: | :--- | :---: | :---: | :--- | :--- |
| **1** | I | `bpt_hai_an` | NB | `BPT_NB_01` | toan-thuc-te-he-bat-phuong-trinh-bac-nhat-hai-an-dang-viet-dong.pdf (tr.14) | SGK Tập 1 (tr.23) |
| **2** | I | `bpt_hai_an` | NB | `BPT_NB_05` | de-kiem-tra-theo-bai-hoc-chu-de-bpt-va-he-bpt-bac-nhat-hai-an.pdf (tr.54) | SGK Tập 1 (tr.23) |
| **3** | I | `bpt_hai_an` | TH | `BPT_TH_01` | chuyen-de-bpt-va-he-bpt-bac-nhat-hai-an-toan-10-dinh-huong-cau-truc-moi.pdf (tr.57) | SGK Tập 1 (tr.23) |
| **4** | I | `bpt_hai_an` | NB | `BPT_NB_03` | de-kiem-tra-theo-bai-hoc-chu-de-bpt-va-he-bpt-bac-nhat-hai-an.pdf (tr.42) | SGK Tập 1 (tr.23) |
| **5** | I | `bpt_hai_an` | NB | `BPT_NB_02` | toan-thuc-te-he-bat-phuong-trinh-bac-nhat-hai-an-dang-viet-dong.pdf (tr.113) | SGK Tập 1 (tr.23) |
| **6** | I | `bpt_hai_an` | NB | `BPT_NB_04` | chuyen-de-bpt-va-he-bpt-bac-nhat-hai-an-toan-10-dinh-huong-cau-truc-moi.pdf (tr.86) | SGK Tập 1 (tr.23) |
| **7** | I | `he_thuc_luong` | TH | `LG_TH_02` | chuyen-de-toan-10-chuong-he-thuc-luong-trong-tam-giac-va-ung-dung.pdf (tr.2) | SGK Tập 1 (tr.34) |
| **8** | I | `he_thuc_luong` | TH | `HTL_TH_01` | chuyen-de-toan-10-chuong-he-thuc-luong-trong-tam-giac-va-ung-dung.pdf (tr.40) | SGK Tập 1 (tr.34) |
| **9** | I | `he_thuc_luong` | NB | `LG_NB_01` | chuyen-de-he-thuc-luong-trong-tam-giac-mon-toan-10-chuong-trinh-moi.pdf (tr.69) | SGK Tập 1 (tr.34) |
| **10** | I | `he_thuc_luong` | NB | `LG_NB_02` | chuyen-de-he-thuc-luong-trong-tam-giac-mon-toan-10-chuong-trinh-moi.pdf (tr.49) | SGK Tập 1 (tr.34) |
| **11** | I | `he_thuc_luong` | NB | `HTL_NB_02` | chuyen-de-he-thuc-luong-trong-tam-giac-mon-toan-10-chuong-trinh-moi.pdf (tr.107) | SGK Tập 1 (tr.34) |
| **12** | I | `he_thuc_luong` | NB | `LG_NB_03` | chuyen-de-he-thuc-luong-trong-tam-giac-mon-toan-10-chuong-trinh-moi.pdf (tr.154) | SGK Tập 1 (tr.34) |
| **13** | II | `he_thuc_luong` | Mixed | `LG_NB_03` | chuyen-de-he-thuc-luong-trong-tam-giac-mon-toan-10-chuong-trinh-moi.pdf (tr.50) | SGK Tập 1 (tr.34) |
| **14** | II | `bpt_hai_an` | Mixed | `BPT_TH_04` | toan-thuc-te-he-bat-phuong-trinh-bac-nhat-hai-an-dang-viet-dong.pdf (tr.51) | SGK Tập 1 (tr.23) |
| **15** | III | `he_thuc_luong` | VD | `HTL_VD_03` | de-kiem-tra-theo-bai-hoc-chu-de-he-thuc-luong-trong-tam-giac.pdf (tr.58) | SGK Tập 1 (tr.34) |
| **16** | III | `he_thuc_luong` | VD | `HTL_VD_02` | chuyen-de-he-thuc-luong-trong-tam-giac-mon-toan-10-chuong-trinh-moi.pdf (tr.25) | SGK Tập 1 (tr.34) |
| **17** | III | `bpt_hai_an` | TH | `BPT_TH_01` | chuyen-de-bpt-va-he-bpt-bac-nhat-hai-an-toan-10-dinh-huong-cau-truc-moi.pdf (tr.87) | SGK Tập 1 (tr.23) |
| **18** | III | `bpt_hai_an` | TH | `BPT_TH_03` | chuyen-de-bpt-va-he-bpt-bac-nhat-hai-an-toan-10-dinh-huong-cau-truc-moi.pdf (tr.41) | SGK Tập 1 (tr.23) |
| **19** | IV | `bpt_hai_an` | TH | `BPT_TH_02` | chuyen-de-bpt-va-he-bpt-bac-nhat-hai-an-toan-10-dinh-huong-cau-truc-moi.pdf (tr.96) | SGK Tập 1 (tr.23) |
| **20** | IV | `he_thuc_luong` | TH | `HTL_TH_01` | de-kiem-tra-theo-bai-hoc-chu-de-he-thuc-luong-trong-tam-giac.pdf (tr.40) | SGK Tập 1 (tr.34) |
| **21** | IV | `he_thuc_luong` | VD | `HTL_VD_01` | chuyen-de-he-thuc-luong-trong-tam-giac-mon-toan-10-chuong-trinh-moi.pdf (tr.48) | SGK Tập 1 (tr.34) |
| **22** | IV | `bpt_hai_an` | VD | `BPT_VD_01` | toan-thuc-te-he-bat-phuong-trinh-bac-nhat-hai-an-dang-viet-dong.pdf (tr.167) | SGK Tập 1 (tr.23) |
