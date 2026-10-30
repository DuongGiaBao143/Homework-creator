# Hồ sơ nguồn Đề số 26 - Ôn thi Giữa kì 1 Toán 10

- **Thời gian làm bài:** 90 phút.
- **Cấu trúc:** 12 Trắc nghiệm (I) + 2 Đúng/Sai (II) + 4 Trả lời ngắn (III) + 4 Tự luận (IV).
- **Ma trận áp dụng:** `config/giua_ki_1.json` (Mã ma trận: `giua_ki_1_ba_mach`, Blueprint Quota & Skill Pool GDPT 2018 đầy đủ 3 chương: Mệnh đề - Tập hợp, BPT bậc nhất hai ẩn, Hệ thức lượng).
- **Kiểm định giải độc lập:** [verify_de26.py](verify_de26.py) đã pass 100% assertions bằng SymPy.
- **Xác thực ma trận:** `check_exam.py --exam 26` đạt chuẩn [OK].

---

## Bảng đối chiếu 22 câu hỏi

| Câu | Phần | Mạch kiến thức | Mức độ | Mã Skill | Nguồn Dataset & Trang | Nguồn SGK KNTT & Trang |
| :---: | :---: | :--- | :---: | :---: | :--- | :--- |
| **1** | I | `menh_de_tap_hop` | NB | `TH_NB_03` | de-kiem-tra-theo-bai-hoc-chu-de-menh-de-va-tap-hop.pdf (tr.20) | SGK Tập 1 (tr.6) |
| **2** | I | `menh_de_tap_hop` | NB | `TH_NB_01` | de-kiem-tra-theo-bai-hoc-chu-de-phuong-phap-toa-do-trong-mat-phang.pdf (tr.122) | SGK Tập 1 (tr.6) |
| **3** | I | `menh_de_tap_hop` | NB | `TH_NB_04` | chuyen-de-vecto-mon-toan-10-chuong-trinh-moi-phan-nhat-linh.pdf (tr.142) | SGK Tập 1 (tr.6) |
| **4** | I | `menh_de_tap_hop` | NB | `MD_NB_05` | phuong-phap-giai-toan-va-bai-tap-chuyen-de-menh-de-va-tap-hop-toan-10.pdf (tr.26) | SGK Tập 1 (tr.6) |
| **5** | I | `bpt_hai_an` | NB | `BPT_NB_04` | de-kiem-tra-theo-bai-hoc-chu-de-bpt-va-he-bpt-bac-nhat-hai-an.pdf (tr.36) | SGK Tập 1 (tr.23) |
| **6** | I | `bpt_hai_an` | NB | `BPT_NB_05` | toan-thuc-te-he-bat-phuong-trinh-bac-nhat-hai-an-dang-viet-dong.pdf (tr.151) | SGK Tập 1 (tr.23) |
| **7** | I | `bpt_hai_an` | NB | `BPT_NB_03` | de-kiem-tra-theo-bai-hoc-chu-de-bpt-va-he-bpt-bac-nhat-hai-an.pdf (tr.65) | SGK Tập 1 (tr.23) |
| **8** | I | `bpt_hai_an` | NB | `BPT_NB_01` | toan-thuc-te-he-bat-phuong-trinh-bac-nhat-hai-an-dang-viet-dong.pdf (tr.7) | SGK Tập 1 (tr.23) |
| **9** | I | `he_thuc_luong` | NB | `LG_NB_02` | chuyen-de-toan-10-chuong-he-thuc-luong-trong-tam-giac-va-ung-dung.pdf (tr.80) | SGK Tập 1 (tr.34) |
| **10** | I | `he_thuc_luong` | TH | `HTL_TH_01` | chuyen-de-toan-10-chuong-he-thuc-luong-trong-tam-giac-va-ung-dung.pdf (tr.39) | SGK Tập 1 (tr.34) |
| **11** | I | `he_thuc_luong` | NB | `HTL_NB_04` | chuyen-de-he-thuc-luong-trong-tam-giac-mon-toan-10-chuong-trinh-moi.pdf (tr.90) | SGK Tập 1 (tr.34) |
| **12** | I | `he_thuc_luong` | NB | `HTL_NB_01` | chuyen-de-he-thuc-luong-trong-tam-giac-mon-toan-10-chuong-trinh-moi.pdf (tr.1) | SGK Tập 1 (tr.34) |
| **13** | II | `menh_de_tap_hop` | Mixed | `MD_NB_05` | de-kiem-tra-theo-bai-hoc-chu-de-menh-de-va-tap-hop.pdf (tr.1) | SGK Tập 1 (tr.6) |
| **14** | II | `bpt_hai_an` | Mixed | `BPT_NB_01` | toan-thuc-te-he-bat-phuong-trinh-bac-nhat-hai-an-dang-viet-dong.pdf (tr.44) | SGK Tập 1 (tr.23) |
| **15** | III | `he_thuc_luong` | VD | `HTL_VD_01` | chuyen-de-toan-10-chuong-he-thuc-luong-trong-tam-giac-va-ung-dung.pdf (tr.86) | SGK Tập 1 (tr.34) |
| **16** | III | `bpt_hai_an` | TH | `BPT_TH_01` | de-kiem-tra-theo-bai-hoc-chu-de-bpt-va-he-bpt-bac-nhat-hai-an.pdf (tr.4) | SGK Tập 1 (tr.23) |
| **17** | III | `bpt_hai_an` | TH | `BPT_TH_03` | chuyen-de-bpt-va-he-bpt-bac-nhat-hai-an-toan-10-dinh-huong-cau-truc-moi.pdf (tr.46) | SGK Tập 1 (tr.23) |
| **18** | III | `menh_de_tap_hop` | VD | `TH_VD_01` | Ngân hàng câu hỏi ôn tập chương mệnh đề và tập hợp Toán 10 – Lê Minh Kha.pdf (tr.87) | SGK Tập 1 (tr.6) |
| **19** | IV | `menh_de_tap_hop` | TH | `TH_TH_01` | phuong-phap-giai-toan-va-bai-tap-chuyen-de-menh-de-va-tap-hop-toan-10.pdf (tr.36) | SGK Tập 1 (tr.6) |
| **20** | IV | `menh_de_tap_hop` | VD | `TH_VD_01` | Ngân hàng câu hỏi ôn tập chương mệnh đề và tập hợp Toán 10 – Lê Minh Kha.pdf (tr.136) | SGK Tập 1 (tr.6) |
| **21** | IV | `he_thuc_luong` | TH | `LG_TH_01` | chuyen-de-he-thuc-luong-trong-tam-giac-mon-toan-10-chuong-trinh-moi.pdf (tr.13) | SGK Tập 1 (tr.34) |
| **22** | IV | `bpt_hai_an` | VD | `BPT_VD_01` | toan-thuc-te-he-bat-phuong-trinh-bac-nhat-hai-an-dang-viet-dong.pdf (tr.48) | SGK Tập 1 (tr.23) |
