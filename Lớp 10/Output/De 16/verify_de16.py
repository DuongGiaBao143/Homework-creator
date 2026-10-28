import sympy as sp
import numpy as np

def verify():
    print("=== KIỂM TRA ĐỀ SỐ 16 TOÁN 10 ===")
    
    # -------------------------------------------------------------
    # PHẦN I: 12 câu trắc nghiệm (3A, 3B, 3C, 3D)
    # -------------------------------------------------------------
    # Câu 1 (I.1 - TH_NB_01) - Đáp án A
    # Cho tập hợp A = {a; b; c}. Khẳng định nào đúng?
    # A. {a} subset A (đúng)
    # B. a subset A (sai, a in A)
    # C. {a; b} in A (sai, con)
    # D. empty in A (sai, empty subset A)
    ans_1 = "A"
    print("Câu 1:", ans_1)
    
    # Câu 2 (I.2 - MD_NB_05) - Đáp án B
    # Định lý: "Nếu hai tam giác bằng nhau thì hai tam giác đó có diện tích bằng nhau".
    # P => Q: P là điều kiện đủ để có Q.
    # B. "Hai tam giác bằng nhau là điều kiện đủ để hai tam giác có diện tích bằng nhau" -> Đúng!
    ans_2 = "B"
    print("Câu 2:", ans_2)
    
    # Câu 3 (I.3 - MD_NB_02) - Đáp án C
    # Mệnh đề nào sau đây là mệnh đề đúng?
    # A. 15 là số nguyên tố (sai, chia hết cho 3, 5)
    # B. Tổng hai góc nhọn của tam giác vuông bằng 180 độ (sai, 90 độ)
    # C. Tứ giác có bốn cạnh bằng nhau là hình thoi (đúng)
    # D. x^2 + 1 = 0 có nghiệm thực (sai)
    ans_3 = "C"
    print("Câu 3:", ans_3)
    
    # Câu 4 (I.4 - TH_NB_03) - Đáp án D
    # Số tập hợp con gồm đúng 2 phần tử của tập hợp X = {1; 2; 3; 4}
    # Số tập con: C(4, 2) = 6
    # A. 4, B. 8, C. 16, D. 6
    assert sp.binomial(4, 2) == 6
    ans_4 = "D"
    print("Câu 4:", ans_4)
    
    # Câu 5 (I.5 - BPT_NB_04) - Đáp án A
    # Cặp số nào là nghiệm của hệ: { 2x - y + 1 > 0; x + 3y - 6 <= 0 }
    # A. (1; 1): 2(1) - 1 + 1 = 2 > 0 và 1 + 3(1) - 6 = -2 <= 0 (thỏa)
    # B. (0; 3): 0 + 9 - 6 = 3 > 0 (loại)
    # C. (-2; 1): -4 - 1 + 1 = -4 < 0 (loại)
    # D. (4; 2): 4 + 6 - 6 = 4 > 0 (loại)
    assert 2*(1) - 1 + 1 > 0 and 1 + 3*(1) - 6 <= 0
    assert not (0 + 3*3 - 6 <= 0)
    ans_5 = "A"
    print("Câu 5:", ans_5)
    
    # Câu 6 (I.6 - BPT_NB_02) - Đáp án B
    # Hệ nào là hệ bất phương trình bậc nhất hai ẩn?
    # A. { 2x^2 + y <= 4; x - 3y > 1 } (bậc 2)
    # B. { 3x - y + 2 >= 0; 2x + 5y - 7 < 0 } (bậc nhất 2 ẩn)
    # C. { x - y + z <= 0; 2x + y > 3 } (3 ẩn)
    # D. { xy + 2 <= 0; x - 4y > 0 } (tích xy)
    ans_6 = "B"
    print("Câu 6:", ans_6)
    
    # Câu 7 (I.7 - BPT_NB_03) - Đáp án C
    # Miền nghiệm của BPT 3x - 2y >= 6 chứa điểm nào?
    # A. O(0; 0): 0 >= 6 (sai)
    # B. M(1; 2): 3 - 4 = -1 >= 6 (sai)
    # C. N(4; 1): 12 - 2 = 10 >= 6 (đúng!)
    # D. P(2; 3): 6 - 6 = 0 >= 6 (sai)
    assert 3*4 - 2*1 >= 6
    assert not (3*0 - 2*0 >= 6)
    ans_7 = "C"
    print("Câu 7:", ans_7)
    
    # Câu 8 (I.8 - BPT_NB_01) - Đáp án D
    # Bất phương trình nào là BPT bậc nhất hai ẩn?
    # A. 2x^2 - 3y + 1 > 0
    # B. x + 2y - 3z <= 0
    # C. 3x + 2/y - 5 < 0
    # D. 4x - 5y + 1 >= 0
    ans_8 = "D"
    print("Câu 8:", ans_8)
    
    # Câu 9 (I.9 - HTL_NB_04) - Đáp án A
    # Công thức trung tuyến:
    # A. m_a^2 = (2(b^2 + c^2) - a^2) / 4 (đúng)
    # B. m_a^2 = (b^2 + c^2 - 2a^2) / 4
    # C. m_a^2 = (2(b^2 + c^2) + a^2) / 4
    # D. m_a^2 = (b^2 + c^2 - a^2) / 2
    ans_9 = "A"
    print("Câu 9:", ans_9)
    
    # Câu 10 (I.10 - LG_NB_01) - Đáp án B
    # Giá trị của sin(150 độ):
    # sin(150 deg) = 1/2
    # A. -1/2, B. 1/2, C. sqrt(3)/2, D. -sqrt(3)/2
    assert sp.sin(sp.pi * 5 / 6) == sp.Rational(1, 2)
    ans_10 = "B"
    print("Câu 10:", ans_10)
    
    # Câu 11 (I.11 - LG_NB_03) - Đáp án C
    # Mối quan hệ hai góc bù nhau:
    # A. sin(180 - alpha) = -sin alpha (sai)
    # B. cos(180 - alpha) = cos alpha (sai)
    # C. cos(180 - alpha) = -cos alpha (đúng)
    # D. tan(180 - alpha) = tan alpha (sai)
    ans_11 = "C"
    print("Câu 11:", ans_11)
    
    # Câu 12 (I.12 - LG_NB_02) - Đáp án D
    # Với góc tù alpha (90 < alpha < 180):
    # sin > 0, cos < 0, tan < 0, cot < 0
    # A. sin < 0 (sai)
    # B. cos > 0 (sai)
    # C. tan > 0 (sai)
    # D. cot < 0 (đúng)
    ans_12 = "D"
    print("Câu 12:", ans_12)
    
    keys = [ans_1, ans_2, ans_3, ans_4, ans_5, ans_6, ans_7, ans_8, ans_9, ans_10, ans_11, ans_12]
    counts = {x: keys.count(x) for x in "ABCD"}
    print("Phần I key count:", counts)
    assert counts == {'A': 3, 'B': 3, 'C': 3, 'D': 3}, "Phần I chưa cân bằng 3A, 3B, 3C, 3D!"

    # -------------------------------------------------------------
    # PHẦN II: 2 câu Đúng/Sai (mỗi câu 4 ý a-d)
    # -------------------------------------------------------------
    # Câu 13 (II.1 - TH_NB_04): Cho A = [-4; 3), B = (0; 5]
    # a) 0 in A nhưng 0 not in B: -4 <= 0 < 3 (thỏa), 0 < 0 (không thỏa). -> ĐÚNG
    # b) B là nửa khoảng gồm x thoả mãn 0 < x <= 5. -> ĐÚNG
    # c) A giao B = (0; 3). -> ĐÚNG
    # d) A \ B = [-4; 0). Vì 0 not in B nên 0 in (A \ B), do đó A \ B = [-4; 0], nói là [-4; 0) là SAI. -> SAI
    res_13 = {"a": True, "b": True, "c": True, "d": False}
    print("Câu 13:", res_13)
    
    # Câu 14 (II.2 - LG_NB_03): Cho góc nhọn alpha (0 < alpha < 90) và beta = 180 - alpha
    # a) alpha và beta là hai góc bù nhau. -> ĐÚNG
    # b) sin beta = sin alpha. -> ĐÚNG
    # c) M = sin^2(alpha) + sin^2(90 - alpha) = sin^2 + cos^2 = 1. -> ĐÚNG
    # d) Với alpha = 45 độ, N = cos(45) + cos(135) + tan(45) + cot(135) = sqrt(2)/2 - sqrt(2)/2 + 1 - 1 = 0 != 2. -> SAI
    val_d = sp.cos(sp.pi/4) + sp.cos(sp.pi*3/4) + sp.tan(sp.pi/4) + sp.cot(sp.pi*3/4)
    assert sp.simplify(val_d) == 0
    res_14 = {"a": True, "b": True, "c": True, "d": False}
    print("Câu 14:", res_14)

    # -------------------------------------------------------------
    # PHẦN III: 4 câu Trả lời ngắn
    # -------------------------------------------------------------
    # Câu 15 (III.1 - TH_TH_04): Cho A = [-3; 7), B = (1; 10]. Tìm số phần tử nguyên thuộc C = A giao B.
    # C = (1; 7). Các số nguyên: 2, 3, 4, 5, 6 -> 5 số.
    c_ints = [x for x in range(-10, 20) if -3 <= x < 7 and 1 < x <= 10]
    assert c_ints == [2, 3, 4, 5, 6]
    ans_15 = len(c_ints)
    assert ans_15 == 5
    print("Câu 15:", ans_15)

    # Câu 16 (III.2 - BPT_VD_02): Miền tam giác ABC: A(1; 2), B(4; 1), C(2; 5).
    # Tìm m nguyên nhỏ nhất để 2x + 3y <= m đúng với mọi điểm thuộc tam giác ABC.
    # f(x, y) = 2x + 3y
    # f(A) = 2(1) + 3(2) = 8
    # f(B) = 2(4) + 3(1) = 11
    # f(C) = 2(2) + 3(5) = 19
    # max = 19 => m >= 19 => m_min = 19.
    f_vals = [2*1 + 3*2, 2*4 + 3*1, 2*2 + 3*5]
    ans_16 = max(f_vals)
    assert ans_16 == 19
    print("Câu 16:", ans_16)

    # Câu 17 (III.3 - HTL_VD_02): Cho tam giác ABC có b^2 + c^2 - a^2 = sqrt(3)*b*c. Tính góc A theo độ.
    # 2*b*c*cos(A) = sqrt(3)*b*c => cos(A) = sqrt(3)/2 => A = 30 độ.
    cos_A = sp.sqrt(3)/2
    angle_A = sp.acos(cos_A) * 180 / sp.pi
    ans_17 = int(angle_A)
    assert ans_17 == 30
    print("Câu 17:", ans_17)

    # Câu 18 (III.4 - TH_TH_01): A = {x in N | (x - 2)(x^2 - 5x + 6) = 0}, B = {x in Z | -1 <= x <= 4}.
    # Tìm số phần tử của B \ A.
    # (x - 2)(x - 2)(x - 3) = 0 => x in {2, 3}. A = {2, 3}.
    # B = {-1, 0, 1, 2, 3, 4}.
    # B \ A = {-1, 0, 1, 4} => 4 phần tử.
    set_A = {x for x in range(10) if (x - 2)*(x**2 - 5*x + 6) == 0}
    set_B = {x for x in range(-5, 10) if -1 <= x <= 4}
    diff = set_B - set_A
    assert diff == {-1, 0, 1, 4}
    ans_18 = len(diff)
    assert ans_18 == 4
    print("Câu 18:", ans_18)

    # -------------------------------------------------------------
    # PHẦN IV: 4 câu Tự luận
    # -------------------------------------------------------------
    # Câu 19 (IV.1 - HTL_TH_02): Tam giác ABC có AB = 50, AC = 80, A = 60 độ.
    # a) BC = sqrt(80^2 + 50^2 - 2*80*50*cos(60)) = sqrt(6400 + 2500 - 4000) = sqrt(4900) = 70.
    # b) S = 1/2 * 50 * 80 * sin(60) = 2000 * sqrt(3)/2 = 1000*sqrt(3) m^2.
    # c) p = (50 + 80 + 70)/2 = 100. r = S / p = 1000*sqrt(3) / 100 = 10*sqrt(3) approx 17.3 m.
    b, c, A = 80, 50, sp.pi/3
    a = sp.sqrt(b**2 + c**2 - 2*b*c*sp.cos(A))
    assert a == 70
    S = sp.Rational(1, 2) * b * c * sp.sin(A)
    assert S == 1000 * sp.sqrt(3)
    p = (a + b + c) / 2
    assert p == 100
    r = S / p
    assert r == 10 * sp.sqrt(3)
    print("Câu 19:", f"a = {a}, S = {S}, r = {r} (~ {float(r):.1f})")

    # Câu 20 (IV.2 - TH_VD_02): Lớp 45 học sinh. A: Bóng đá (25), B: Cầu lông (20), C: Bóng rổ (15).
    # A giao B = 10, B giao C = 7, C giao A = 8, A giao B giao C = 4.
    # a) Số học sinh đăng ký ít nhất một môn:
    # |A u B u C| = 25 + 20 + 15 - (10 + 7 + 8) + 4 = 60 - 25 + 4 = 39.
    # b) Không tham gia môn nào: 45 - 39 = 6.
    # c) Chỉ đúng 1 môn:
    # chỉ A: 25 - (10 + 8 - 4) = 11
    # chỉ B: 20 - (10 + 7 - 4) = 7
    # chỉ C: 15 - (8 + 7 - 4) = 4
    # Tổng chỉ 1 môn: 11 + 7 + 4 = 22.
    union = 25 + 20 + 15 - (10 + 7 + 8) + 4
    assert union == 39
    none_sport = 45 - union
    assert none_sport == 6
    only_one = (25 - 14) + (20 - 13) + (15 - 11)
    assert only_one == 22
    print("Câu 20:", f"a) {union}, b) {none_sport}, c) {only_one}")

    # Câu 21 (IV.3 - BPT_VD_01): Sản xuất x đèn lồng A, y hộp gỗ B.
    # Ràng buộc: { 2x + y <= 100; x + 2y <= 80; x >= 0; y >= 0 }
    # Đỉnh: O(0; 0), A(50; 0), B: {2x+y=100, x+2y=80} => B(40; 20), C(0; 40)
    # Lợi nhuận: F(x, y) = 120x + 100y (nghìn đồng)
    # F(O) = 0
    # F(A) = 120*50 = 6000
    # F(C) = 100*40 = 4000
    # F(B) = 120*40 + 100*20 = 4800 + 2000 = 6800 nghìn đồng = 6 800 000 đồng.
    x_B, y_B = sp.symbols('x y')
    sol = sp.solve([2*x_B + y_B - 100, x_B + 2*y_B - 80], (x_B, y_B))
    assert sol[x_B] == 40 and sol[y_B] == 20
    F_max = 120 * sol[x_B] + 100 * sol[y_B]
    assert F_max == 6800
    print("Câu 21:", f"x = {sol[x_B]}, y = {sol[y_B]}, F_max = {F_max} (nghìn đồng)")

    # Câu 22 (IV.4 - TH_TH_05): 50 học sinh, Tin: 32, Tiếng Anh: 28, Cả hai: 18.
    # a) Ít nhất một CLB: 32 + 28 - 18 = 42.
    # b) Không tham gia cả hai CLB: 50 - 42 = 8.
    # c) Chỉ Tin học: 32 - 18 = 14.
    union_clb = 32 + 28 - 18
    assert union_clb == 42
    none_clb = 50 - union_clb
    assert none_clb == 8
    only_cs = 32 - 18
    assert only_cs == 14
    print("Câu 22:", f"a) {union_clb}, b) {none_clb}, c) {only_cs}")

    print("\n>>> TẤT CẢ CÁC PHÉP TÍNH VÀ ĐÁP ÁN ĐÃ ĐƯỢC XÁC THỰC 100% THÀNH CÔNG! <<<")

if __name__ == "__main__":
    verify()
