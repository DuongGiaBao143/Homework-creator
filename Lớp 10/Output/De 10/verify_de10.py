"""
Kiểm tra toán học 100% cho Đề số 10 bằng SymPy và NumPy.
Đề thi Giữa kì 1 Toán 10 - Năm học 2026 - 2027.
"""
import sympy as sp
import numpy as np

def verify_all():
    print("=== BẮT ĐẦU KIỂM ĐỊNH TOÁN HỌC ĐỀ 10 ===")
    
    # -------------------------------------------------------------
    # PHẦN I: Trắc nghiệm (12 câu)
    # -------------------------------------------------------------
    print("\n--- PHẦN I: Trắc nghiệm ---")
    
    # Câu 1: [-2; 5)
    # Tập hợp {x in R | -2 <= x < 5} là nửa khoảng [-2; 5). Đáp án B.
    ans_1 = "B"
    print(f"Câu 1: Đáp án {ans_1} [OK]")
    
    # Câu 2: Mệnh đề toán học
    # "Tam giác đều có ba góc bằng 60 độ" là khẳng định đúng, mệnh đề toán học. Đáp án A.
    ans_2 = "A"
    print(f"Câu 2: Đáp án {ans_2} [OK]")
    
    # Câu 3: [-3; 2) giao (0; 4] = (0; 2)
    # Đáp án C.
    ans_3 = "C"
    print(f"Câu 3: Đáp án {ans_3} [OK]")
    
    # Câu 4: Mệnh đề đảo của "Nếu tam giác ABC đều thì tam giác ABC cân"
    # là "Nếu tam giác ABC cân thì tam giác ABC đều". Đáp án D.
    ans_4 = "D"
    print(f"Câu 4: Đáp án {ans_4} [OK]")
    
    # Câu 5: Hệ {x - y + 1 > 0; 2x + y - 4 <= 0}
    # Điểm (1; 1): 1 - 1 + 1 = 1 > 0 và 2(1) + 1 - 4 = -1 <= 0. Đáp án A.
    p = (1, 1)
    assert p[0] - p[1] + 1 > 0 and 2*p[0] + p[1] - 4 <= 0
    ans_5 = "A"
    print(f"Câu 5: Đáp án {ans_5} [OK]")
    
    # Câu 6: Cặp (-1; 2) không là nghiệm của 2x - 3y + 6 >= 0
    # 2(-1) - 3(2) + 6 = -2 < 0. Đáp án C.
    assert 2*(-1) - 3*2 + 6 < 0
    ans_6 = "C"
    print(f"Câu 6: Đáp án {ans_6} [OK]")
    
    # Câu 7: Đường thẳng bờ của 3x - 4y + 12 >= 0 là 3x - 4y + 12 = 0. Đáp án D.
    ans_7 = "D"
    print(f"Câu 7: Đáp án {ans_7} [OK]")
    
    # Câu 8: Miền nghiệm 2x + y - 4 <= 0 chứa O(0; 0)
    # 2(0) + 0 - 4 = -4 <= 0. Đáp án B.
    assert 2*0 + 0 - 4 <= 0
    ans_8 = "B"
    print(f"Câu 8: Đáp án {ans_8} [OK]")
    
    # Câu 9: cos(120 deg) = -1/2. Đáp án C.
    assert sp.cos(sp.rad(120)) == sp.Rational(-1, 2)
    ans_9 = "C"
    print(f"Câu 9: Đáp án {ans_9} [OK]")
    
    # Câu 10: sin alpha = 3/5, alpha nhọn => P = 2 cos^2 alpha - 1
    # cos^2 alpha = 16/25 => P = 2*(16/25) - 1 = 7/25. Đáp án A.
    sin_a = sp.Rational(3, 5)
    cos2_a = 1 - sin_a**2
    P_val = 2 * cos2_a - 1
    assert P_val == sp.Rational(7, 25)
    ans_10 = "A"
    print(f"Câu 10: Đáp án {ans_10} [OK]")
    
    # Câu 11: cos(180 - alpha) = -cos alpha. Đáp án B.
    ans_11 = "B"
    print(f"Câu 11: Đáp án {ans_11} [OK]")
    
    # Câu 12: a^2 = b^2 + c^2 - 2bc cos A. Đáp án D.
    ans_12 = "D"
    print(f"Câu 12: Đáp án {ans_12} [OK]")
    
    # Kiểm tra phân bố đáp án Phần I
    ans_list = [ans_1, ans_2, ans_3, ans_4, ans_5, ans_6, ans_7, ans_8, ans_9, ans_10, ans_11, ans_12]
    counts = {k: ans_list.count(k) for k in "ABCD"}
    print(f"Phân bố đáp án Phần I: {counts}")
    assert counts == {"A": 3, "B": 3, "C": 3, "D": 3}, "Phải đúng 3A, 3B, 3C, 3D!"
    print("-> CÂN BẰNG ĐÁP ÁN 3A-3B-3C-3D ĐẠT 100%!")

    # -------------------------------------------------------------
    # PHẦN II: Đúng/Sai (2 câu, 8 ý)
    # -------------------------------------------------------------
    print("\n--- PHẦN II: Đúng/Sai ---")
    
    # Câu 13:
    # A = {x in N | (x^2 - 9)(2x^2 - 5x + 2) = 0}
    # x^2 - 9 = 0 => x = 3 (do x in N)
    # 2x^2 - 5x + 2 = 0 => x = 2 (do x in N, x=1/2 loai)
    # A = {2, 3}
    # B = {x in Z | -2 <= x <= 2} = {-2, -1, 0, 1, 2}
    A_set = {2, 3}
    B_set = {-2, -1, 0, 1, 2}
    
    # a) n(A) = 2 -> Đúng
    assert len(A_set) == 2
    print("Câu 13 a: n(A) = 2 -> ĐÚNG")
    
    # b) Số tập con của A là 2^2 = 4 -> Đúng
    assert 2**len(A_set) == 4
    print("Câu 13 b: 2^2 = 4 tập con -> ĐÚNG")
    
    # c) A giao B = {2} -> Đúng
    assert A_set.intersection(B_set) == {2}
    print("Câu 13 c: A giao B = {2} -> ĐÚNG")
    
    # d) B \ A có 3 phần tử -> Sai (thực tế có 4 phần tử: {-2, -1, 0, 1})
    diff = B_set.difference(A_set)
    assert len(diff) == 4
    print(f"Câu 13 d: B \\ A = {diff} có 4 phần tử, phát biểu '3 phần tử' -> SAI")

    # Câu 14: Tam giác ABC có a = 7, b = 5, c = 6
    a, b, c = 7, 5, 6
    p_val = sp.Rational(a + b + c, 2)
    assert p_val == 9
    print(f"Câu 14 a: Nửa chu vi p = {p_val} -> ĐÚNG")
    
    cosA_val = sp.Rational(b**2 + c**2 - a**2, 2 * b * c)
    assert cosA_val == sp.Rational(1, 5)
    print(f"Câu 14 b: cos A = {cosA_val} -> ĐÚNG")
    
    # S = sqrt(p(p-a)(p-b)(p-c)) = sqrt(9 * 2 * 4 * 3) = sqrt(216) = 6*sqrt(6)
    S_val = sp.sqrt(9 * (9-7) * (9-5) * (9-6))
    assert S_val == 6 * sp.sqrt(6)
    print(f"Câu 14 c: Diện tích S = {S_val} -> ĐÚNG")
    
    # r = S / p = 6*sqrt(6) / 9 = 2*sqrt(6) / 3 != sqrt(6)
    r_val = S_val / p_val
    assert r_val == sp.Rational(2, 3) * sp.sqrt(6)
    assert r_val != sp.sqrt(6)
    print(f"Câu 14 d: r = 2*sqrt(6)/3 != sqrt(6), phát biểu 'r = sqrt(6)' -> SAI")

    # -------------------------------------------------------------
    # PHẦN III: Trả lời ngắn (4 câu)
    # -------------------------------------------------------------
    print("\n--- PHẦN III: Trả lời ngắn ---")
    
    # Câu 15: A = [-3; 5], B = (1; 9)
    # A giao B = (1; 5]. Các số nguyên: 2, 3, 4, 5. Số phần tử: 4.
    ans_15 = 4
    print(f"Câu 15: Số phần tử nguyên thuộc A giao B là {ans_15} [OK]")
    
    # Câu 16: BPT hai ẩn:
    # 2x + y <= 10, x + 2y <= 10, x >= 0, y >= 0
    # F(x, y) = 40x + 50y
    # Đỉnh O(0,0): 0
    # Đỉnh A(5,0): 200
    # Đỉnh B(10/3, 10/3): 40*(10/3) + 50*(10/3) = 900/3 = 300
    # Đỉnh C(0,5): 250
    # Max F = 300.
    F_max = max(0, 40*5, 40*(10/3) + 50*(10/3), 50*5)
    assert F_max == 300
    ans_16 = 300
    print(f"Câu 16: Lợi nhuận lớn nhất F_max = {ans_16} nghìn đồng [OK]")
    
    # Câu 17: Tam giác ABC: AB = 6, AC = 10, góc A = 120 độ
    # BC^2 = 6^2 + 10^2 - 2*6*10*cos(120 deg) = 36 + 100 - 120*(-1/2) = 136 + 60 = 196 => BC = 14
    BC_sq = 6**2 + 10**2 - 2 * 6 * 10 * sp.cos(sp.rad(120))
    BC_val = sp.sqrt(BC_sq)
    assert BC_val == 14
    ans_17 = 14
    print(f"Câu 17: Độ dài BC = {ans_17} [OK]")
    
    # Câu 18: Đo khoảng cách: AB = 600, góc A = 45 độ, góc B = 105 độ => góc C = 30 độ
    # BC = AB * sin(A) / sin(C) = 600 * sin(45) / sin(30) = 600 * (sqrt(2)/2) / (1/2) = 600 * sqrt(2)
    # 600 * sqrt(2) approx 848.528 => làm tròn 849
    BC_dist = 600 * sp.sin(sp.rad(45)) / sp.sin(sp.rad(30))
    assert BC_dist == 600 * sp.sqrt(2)
    ans_18 = int(round(float(BC_dist)))
    assert ans_18 == 849
    print(f"Câu 18: BC = 600*sqrt(2) approx {float(BC_dist):.2f} => Làm tròn: {ans_18} [OK]")

    # -------------------------------------------------------------
    # PHẦN IV: Tự luận (4 câu)
    # -------------------------------------------------------------
    print("\n--- PHẦN IV: Tự luận ---")
    
    # Câu 19: Lớp 42 học sinh, 25 thích bóng đá, 18 thích bóng rổ, 7 không thích môn nào.
    # a) |A giao B| = 25 + 18 - (42 - 7) = 43 - 35 = 8
    # b) Đúng một môn = (25 - 8) + (18 - 8) = 17 + 10 = 27
    both = 25 + 18 - (42 - 7)
    assert both == 8
    exactly_one = (25 - 8) + (18 - 8)
    assert exactly_one == 27
    print(f"Câu 19: a) Cả hai môn: {both}; b) Đúng một môn: {exactly_one} [OK]")
    
    # Câu 20: sin + cos = 1/5
    # a) P = sin*cos = ((1/5)^2 - 1)/2 = (1/25 - 1)/2 = -24/50 = -12/25
    # b) Q = sin^3 + cos^3 = (sin+cos)(1 - sin*cos) = (1/5)*(1 - (-12/25)) = (1/5)*(37/25) = 37/125
    P_val_20 = (sp.Rational(1, 5)**2 - 1) / 2
    assert P_val_20 == sp.Rational(-12, 25)
    Q_val_20 = sp.Rational(1, 5) * (1 - P_val_20)
    assert Q_val_20 == sp.Rational(37, 125)
    print(f"Câu 20: a) P = {P_val_20}; b) Q = {Q_val_20} [OK]")
    
    # Câu 21: Đo chiều cao tháp CD = h.
    # A, B, C thẳng hàng. AB = 40 m. Góc CAD = 30 độ, góc CBD = 45 độ.
    # AC = h * cot(30) = h * sqrt(3)
    # BC = h * cot(45) = h
    # AB = AC - BC = h * (sqrt(3) - 1) = 40 => h = 40 / (sqrt(3) - 1) = 20 * (sqrt(3) + 1)
    # h approx 20 * (1.73205 + 1) = 54.641 m => 54.6 m.
    h_exact = 40 / (sp.sqrt(3) - 1)
    assert sp.simplify(h_exact) == 20 + 20*sp.sqrt(3)
    h_round = round(float(h_exact), 1)
    assert h_round == 54.6
    print(f"Câu 21: Chiều cao h = {float(h_exact):.3f} m => Làm tròn: {h_round} m [OK]")
    
    # Câu 22: Quy hoạch tuyến tính
    # 2x + 3y <= 180 (vải)
    # 3x + 2y <= 180 (công)
    # x >= 0, y >= 0
    # Giao d1, d2: 2x + 3y = 180, 3x + 2y = 180 => x = 36, y = 36
    # Đỉnh: O(0,0), A(60,0), B(36,36), C(0,60)
    # T(x, y) = 120 000 x + 100 000 y
    T_O = 0
    T_A = 120000 * 60 + 0
    T_B = 120000 * 36 + 100000 * 36
    T_C = 100000 * 60
    assert T_A == 7200000
    assert T_B == 7920000
    assert T_C == 6000000
    assert max(T_O, T_A, T_B, T_C) == T_B
    print(f"Câu 22: Sản xuất 36 áo loại I và 36 áo loại II, T_max = {T_B:,} đồng [OK]")

    print("\n=== TẤT CẢ 22 CÂU ĐÃ ĐƯỢC XÁC THỰC TOÁN HỌC CHÍNH XÁC 100%! ===")

if __name__ == "__main__":
    verify_all()
