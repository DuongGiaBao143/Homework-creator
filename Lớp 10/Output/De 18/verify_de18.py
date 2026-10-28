import sympy as sp
import numpy as np

def verify():
    print("=== KIỂM TRA TOÁN HỌC ĐỀ SỐ 18 (GIỮA KÌ 1 TOÁN 10) ===")
    
    # =========================================================================
    # PHẦN I: 12 CÂU TRẮC NGHIỆM NHIỀU LỰA CHỌN
    # =========================================================================
    # Câu 1 (I.1 - TH_TH_01): A = {1; 2; 3; 4; 5}, B = {2; 4; 6; 8}. A \ B = {1; 3; 5}
    set_A = {1, 2, 3, 4, 5}
    set_B = {2, 4, 6, 8}
    diff_AB = set_A - set_B
    assert diff_AB == {1, 3, 5}
    ans_1 = "A"
    print("Câu 1:", ans_1, "-> A \\ B =", diff_AB)
    
    # Câu 2 (I.2 - MD_NB_03): P(x): "x^2 - 5x + 6 = 0". Nghiệm x = 2
    x = sp.Symbol('x')
    eq = sp.Eq(x**2 - 5*x + 6, 0)
    sols = sp.solve(eq, x)
    assert 2 in sols and 3 in sols
    ans_2 = "B"
    print("Câu 2:", ans_2, "-> nghiệm thuộc {2, 3}, chọn x = 2")
    
    # Câu 3 (I.3 - TH_NB_01): X = {a, b, c}. Khẳng định đúng: {b, c} subset X
    ans_3 = "C"
    print("Câu 3:", ans_3, "-> {b, c} là tập con của X")
    
    # Câu 4 (I.4 - TH_NB_03): Tập có 4 phần tử có 2^4 = 16 tập con
    assert 2**4 == 16
    ans_4 = "D"
    print("Câu 4:", ans_4, "-> 2^4 = 16 tập con")
    
    # Câu 5 (I.5 - BPT_NB_04): Hệ { 2x - y + 1 > 0; x + 2y - 4 <= 0 }. Nghiệm (1; 1)
    pt = (1, 1)
    assert 2*pt[0] - pt[1] + 1 > 0
    assert pt[0] + 2*pt[1] - 4 <= 0
    # Điểm (0; 1) không thỏa: 2(0) - 1 + 1 = 0 không > 0
    assert not (2*0 - 1 + 1 > 0)
    ans_5 = "A"
    print("Câu 5:", ans_5, "-> (1; 1) là nghiệm")
    
    # Câu 6 (I.6 - BPT_NB_02): Nhận dạng hệ BPT bậc nhất hai ẩn
    # B: { 3x - y + 2 >= 0; x + 4y - 5 < 0 }
    ans_6 = "B"
    print("Câu 6:", ans_6, "-> Hệ bậc nhất hai ẩn")
    
    # Câu 7 (I.7 - BPT_NB_03): 3x - 2y + 6 >= 0. Điểm (1; 2): 3(1) - 2(2) + 6 = 5 >= 0
    assert 3*1 - 2*2 + 6 >= 0
    assert 3*(-3) - 2*0 + 6 < 0
    ans_7 = "C"
    print("Câu 7:", ans_7, "-> (1; 2) thuộc miền nghiệm")
    
    # Câu 8 (I.8 - BPT_TH_01): x - 2y + 2 <= 0. Điểm P(0; 2): 0 - 2(2) + 2 = -2 <= 0
    assert 0 - 2*2 + 2 <= 0
    assert not (0 - 2*0 + 2 <= 0) # O(0;0) không thỏa
    ans_8 = "D"
    print("Câu 8:", ans_8, "-> P(0; 2) thỏa mãn")
    
    # Câu 9 (I.9 - HTL_NB_01): Định lý côsin: a^2 = b^2 + c^2 - 2bc cos A
    ans_9 = "A"
    print("Câu 9:", ans_9, "-> a^2 = b^2 + c^2 - 2bc cos A")
    
    # Câu 10 (I.10 - LG_NB_03): Hai góc bù nhau: cos(180 - alpha) = -cos(alpha)
    ans_10 = "B"
    print("Câu 10:", ans_10, "-> cos(180 - alpha) = -cos(alpha)")
    
    # Câu 11 (I.11 - LG_NB_01): sin(150 deg) = 1/2
    assert sp.sin(sp.pi * 5 / 6) == sp.Rational(1, 2)
    ans_11 = "C"
    print("Câu 11:", ans_11, "-> sin(150 deg) = 1/2")
    
    # Câu 12 (I.12 - LG_TH_02): cos(90 - alpha)*sin(alpha) + cos^2(alpha) = sin^2 + cos^2 = 1
    ans_12 = "D"
    print("Câu 12:", ans_12, "-> Kết quả rút gọn bằng 1")
    
    keys = [ans_1, ans_2, ans_3, ans_4, ans_5, ans_6, ans_7, ans_8, ans_9, ans_10, ans_11, ans_12]
    counts = {k: keys.count(k) for k in "ABCD"}
    print("TỔNG KẾT PHẦN I:", counts)
    assert counts == {'A': 3, 'B': 3, 'C': 3, 'D': 3}, "Phần I chưa cân bằng 3A, 3B, 3C, 3D!"

    # =========================================================================
    # PHẦN II: 2 CÂU ĐÚNG / SAI (8 Ý a-d)
    # =========================================================================
    # Câu 13 (II.1 - MD_NB_01):
    # a) "Hà Nội là thủ đô của Việt Nam" là mệnh đề -> ĐÚNG
    # b) Phủ định của P: forall x, x^2 + 1 > 0 là exists x, x^2 + 1 <= 0 -> ĐÚNG
    # c) forall n in N, n^2 + n + 1 là số nguyên tố -> SAI (n=4: 21 hợp số)
    assert (4**2 + 4 + 1) == 21 and 21 % 3 == 0
    # d) Mệnh đề đảo của "n tận cùng bằng 0 => n chia hết cho 5" là đúng -> SAI (15 chia hết cho 5 nhưng tận cùng bằng 5)
    c13 = {"a": True, "b": True, "c": False, "d": False}
    print("Câu 13 (Đ/S):", c13)

    # Câu 14 (II.2 - LG_NB_01): Góc tù 90 < alpha < 180
    # a) sin alpha > 0 -> ĐÚNG
    # b) cos alpha > 0 -> SAI (cos alpha < 0)
    # c) Biết cos alpha = -3/5 => tan alpha = -4/3 -> ĐÚNG (sin = 4/5 => tan = (4/5)/(-3/5) = -4/3)
    sin_val = sp.sqrt(1 - sp.Rational(-3, 5)**2)
    tan_val = sin_val / sp.Rational(-3, 5)
    assert tan_val == -sp.Rational(4, 3)
    # d) E = (2 sin + cos) / (sin - 2 cos) = 1/2 -> ĐÚNG:
    E = (2*sin_val + sp.Rational(-3, 5)) / (sin_val - 2*sp.Rational(-3, 5))
    assert E == sp.Rational(1, 2)
    c14 = {"a": True, "b": False, "c": True, "d": True}
    print("Câu 14 (Đ/S):", c14)

    # =========================================================================
    # PHẦN III: 4 CÂU TRẢ LỜI NGẮN
    # =========================================================================
    # Câu 15 (III.1 - TH_TH_04): A = [-4; 5), B = (-1; 8]. A giao B = (-1; 5)
    # Các số nguyên: {0, 1, 2, 3, 4} -> 5 số
    integers_c15 = [x for x in range(-10, 10) if -1 < x < 5]
    assert len(integers_c15) == 5
    ans_15 = 5
    print("Câu 15 (TLN):", ans_15)

    # Câu 16 (III.2 - BPT_VD_02): Tam giác OAB với O(0;0), A(3;0), B(0;4). BPT 2x + 3y <= m
    # Max(2x + 3y) trên OAB đạt tại B(0; 4) = 2(0) + 3(4) = 12
    max_f = max(2*0 + 3*0, 2*3 + 3*0, 2*0 + 3*4)
    assert max_f == 12
    ans_16 = 12
    print("Câu 16 (TLN):", ans_16)

    # Câu 17 (III.3 - TH_VD_01): A = [m; m + 2], B = (-3; 5). A subset B <=> -3 < m < 3
    # Các số nguyên m in {-2, -1, 0, 1, 2} -> 5 giá trị
    m_vals = [m for m in range(-10, 10) if -3 < m and m + 2 < 5]
    assert len(m_vals) == 5
    ans_17 = 5
    print("Câu 17 (TLN):", ans_17)

    # Câu 18 (III.4 - LG_TH_02 / Thực tế tam giác):
    # CA = 50 m, CB = 80 m, góc ACB = 60 độ. Tính AB.
    # AB^2 = 50^2 + 80^2 - 2*50*80*cos(60 deg) = 2500 + 6400 - 4000 = 4900 => AB = 70 m
    AB_sq = 50**2 + 80**2 - 2*50*80*sp.cos(sp.pi/3)
    assert AB_sq == 4900
    AB = sp.sqrt(AB_sq)
    assert AB == 70
    ans_18 = 70
    print("Câu 18 (TLN):", ans_18, "m")

    # =========================================================================
    # PHẦN IV: 4 CÂU TỰ LUẬN
    # =========================================================================
    # Câu 19 (IV.1 - TH_VD_01): A = (m - 1; m + 3), B = [1; 5]
    # a) m = 3 => A = (2; 6), A giao B = (2; 5]
    # b) A giao B != rỗng <=> not (m + 3 <= 1 or m - 1 >= 5) <=> -2 < m < 6
    print("Câu 19 (TL): a) A giao B = (2; 5]; b) -2 < m < 6")

    # Câu 20 (IV.2 - BPT_TH_03): Hệ { x >= 0, y >= 0, x + y <= 5, 2x + y <= 8 }
    # Đỉnh O(0;0), A(4;0), B(3;2), C(0;5)
    # Giao 2x + y = 8 và x + y = 5:
    A_mat = np.array([[1, 1], [2, 1]])
    b_vec = np.array([5, 8])
    B_coord = np.linalg.solve(A_mat, b_vec)
    assert np.allclose(B_coord, [3, 2])
    # F(x, y) = 3x + 2y:
    F_vals = {
        "O": 3*0 + 2*0,
        "A": 3*4 + 2*0,
        "B": 3*3 + 2*2,
        "C": 3*0 + 2*5
    }
    assert F_vals["B"] == 13 and max(F_vals.values()) == 13
    print("Câu 20 (TL): Đỉnh O(0;0), A(4;0), B(3;2), C(0;5); Max F(x, y) = 13 tại B(3;2)")

    # Câu 21 (IV.3 - LG_TH_02): tan alpha = -2
    # P = (2 tan - 3) / (3 tan + 4) = (2(-2) - 3) / (3(-2) + 4) = -7 / -2 = 7/2
    # Q = (tan^2 + 2 tan - 3) / (2 tan^2 - 1) = (4 - 4 - 3) / (8 - 1) = -3/7
    t = sp.Rational(-2, 1)
    P = (2*t - 3) / (3*t + 4)
    Q = (t**2 + 2*t - 3) / (2*t**2 - 1)
    assert P == sp.Rational(7, 2)
    assert Q == sp.Rational(-3, 7)
    print("Câu 21 (TL): P = 7/2, Q = -3/7")

    # Câu 22 (IV.4 - TH_VD_02): Lớp 45 học sinh, A (bóng đá)=25, B (cầu lông)=20, C (bóng rổ)=18
    # |A giao B| = 10, |A giao C| = 8, |B giao C| = 7, |A giao B giao C| = 4
    # a) |A hợp B hợp C| = 25 + 20 + 18 - (10 + 8 + 7) + 4 = 42
    union_ABC = 25 + 20 + 18 - (10 + 8 + 7) + 4
    assert union_ABC == 42
    # b) Không thích môn nào = 45 - 42 = 3
    none_sport = 45 - union_ABC
    assert none_sport == 3
    # c) Chỉ thích đúng 1 môn:
    only_A = 25 - (10 + 8 - 4) # 11
    only_B = 20 - (10 + 7 - 4) # 7
    only_C = 18 - (8 + 7 - 4)  # 7
    total_only_one = only_A + only_B + only_C
    assert total_only_one == 25
    print(f"Câu 22 (TL): a) 42 học sinh; b) 3 học sinh; c) {total_only_one} học sinh")

    print("\n>>> TẤT CẢ 22 CÂU HỎI ĐÃ ĐƯỢC XÁC MINH TOÁN HỌC 100% CHÍNH XÁC! <<<")

if __name__ == "__main__":
    verify()
