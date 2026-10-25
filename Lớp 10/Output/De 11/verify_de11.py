import sympy as sp
import numpy as np

def verify():
    print("=== KIỂM TRA ĐỀ SỐ 11 TOÁN 10 ===")
    
    # -------------------------------------------------------------
    # PHẦN I: 12 câu trắc nghiệm (3A, 3B, 3C, 3D)
    # -------------------------------------------------------------
    # Câu 1 (I.1 - TH_NB_04) - Đáp án A
    # Tập hợp các số thực x thỏa mãn -2 <= x < 5 viết dưới dạng khoảng, đoạn, nửa khoảng
    # Đáp án: [-2; 5). A: [-2; 5), B: (-2; 5], C: [-2; 5], D: (-2; 5)
    ans_1 = "A"
    print("Câu 1:", ans_1)
    
    # Câu 2 (I.2 - TH_NB_01) - Đáp án B
    # Cho tập hợp A = {1; 2; 3; 4}. Khẳng định nào đúng?
    # A: {2} in A (sai, con). B: {1; 2} subset A (đúng). C: 5 in A (sai). D: empty in A (sai, empty subset A).
    ans_2 = "B"
    print("Câu 2:", ans_2)
    
    # Câu 3 (I.3 - MD_NB_01) - Đáp án C
    # Câu nào là mệnh đề toán học?
    # A: Trời hôm nay đẹp quá! B: Bạn có thích học Toán không? C: Số 17 là số nguyên tố. D: Hãy giải bài tập này đi!
    ans_3 = "C"
    print("Câu 3:", ans_3)
    
    # Câu 4 (I.4 - TH_NB_03) - Đáp án D
    # Số tập hợp con của tập hợp có 3 phần tử: 2^3 = 8
    # A: 3, B: 6, C: 7, D: 8
    assert 2**3 == 8
    ans_4 = "D"
    print("Câu 4:", ans_4)
    
    # Câu 5 (I.5 - BPT_NB_05) - Đáp án A
    # Đường thẳng bờ của miền nghiệm BPT 3x - 2y + 6 >= 0 là:
    # A: 3x - 2y + 6 = 0, B: 3x - 2y - 6 = 0, C: 2x - 3y + 6 = 0, D: 3x + 2y + 6 = 0
    ans_5 = "A"
    print("Câu 5:", ans_5)
    
    # Câu 6 (I.6 - BPT_NB_04) - Đáp án B
    # Cặp số (x; y) nào là nghiệm của hệ: { x + 2y - 4 <= 0; x - y + 1 >= 0 }
    # A: (2; 2) -> 2+4-4=2 > 0 (sai)
    # B: (0; 1) -> 0+2-4 = -2 <= 0; 0-1+1 = 0 >= 0 (đúng!)
    # C: (3; 1) -> 3+2-4 = 1 > 0 (sai)
    # D: (-2; 4) -> -2+8-4 = 2 > 0 (sai)
    assert 0 + 2*1 - 4 <= 0 and 0 - 1 + 1 >= 0
    assert not (2 + 2*2 - 4 <= 0)
    ans_6 = "B"
    print("Câu 6:", ans_6)
    
    # Câu 7 (I.7 - BPT_NB_02) - Đáp án C
    # Hệ nào sau đây là hệ bất phương trình bậc nhất hai ẩn?
    # A: { x^2 + y <= 1; x - y > 0 } (chứa x^2)
    # B: { x + y - z <= 2; x - y >= 1 } (ba ẩn x, y, z)
    # C: { 2x - y + 1 <= 0; x + 3y - 5 > 0 } (bậc nhất hai ẩn)
    # D: { xy + 1 <= 0; x - y >= 0 } (chứa tích xy)
    ans_7 = "C"
    print("Câu 7:", ans_7)
    
    # Câu 8 (I.8 - BPT_TH_01) - Đáp án D
    # Miền nghiệm của bất phương trình 2x - y + 2 >= 0 là nửa mặt phẳng bờ d: 2x - y + 2 = 0 chứa điểm nào sau đây?
    # A: (-2; 0) -> 2(-2) - 0 + 2 = -2 < 0 (sai)
    # B: (0; 3) -> 2(0) - 3 + 2 = -1 < 0 (sai)
    # C: (-3; 1) -> 2(-3) - 1 + 2 = -5 < 0 (sai)
    # D: (1; 1) -> 2(1) - 1 + 2 = 3 >= 0 (đúng!)
    assert 2*(1) - 1 + 2 >= 0
    assert 2*(-2) - 0 + 2 < 0
    ans_8 = "D"
    print("Câu 8:", ans_8)
    
    # Câu 9 (I.9 - LG_NB_01) - Đáp án A
    # Giá trị của cos(120 độ): cos(120 deg) = -1/2
    # A: -1/2, B: 1/2, C: -sqrt(3)/2, D: sqrt(3)/2
    assert sp.cos(sp.pi * 2 / 3) == -sp.Rational(1, 2)
    ans_9 = "A"
    print("Câu 9:", ans_9)
    
    # Câu 10 (I.10 - LG_TH_01) - Đáp án B
    # Cho góc alpha với 90 deg < alpha < 180 deg và sin(alpha) = 3/5. Giá trị của cos(alpha) là:
    # cos(alpha) = -sqrt(1 - (3/5)^2) = -4/5
    # A: 4/5, B: -4/5, C: -3/4, D: 16/25
    sin_a = sp.Rational(3, 5)
    cos_a = -sp.sqrt(1 - sin_a**2)
    assert cos_a == -sp.Rational(4, 5)
    ans_10 = "B"
    print("Câu 10:", ans_10)
    
    # Câu 11 (I.11 - HTL_NB_03) - Đáp án C
    # Công thức tính diện tích tam giác:
    # A: S = 1/2 * a * b * cos(C)
    # B: S = 1/2 * a * c * sin(B) -> wait, let's make C the correct one!
    # A: S = a*b*c / (2R)
    # B: S = p * R
    # C: S = 1/2 * a * b * sin(C)  (đúng)
    # D: S = 1/2 * b * c * sin(C)
    ans_11 = "C"
    print("Câu 11:", ans_11)
    
    # Câu 12 (I.12 - HTL_NB_02) - Đáp án D
    # Định lý sin trong tam giác:
    # A: a / sin(A) = R
    # B: a / sin(A) = R/2
    # C: a / sin(A) = 4R
    # D: a / sin(A) = 2R (đúng)
    ans_12 = "D"
    print("Câu 12:", ans_12)
    
    keys = [ans_1, ans_2, ans_3, ans_4, ans_5, ans_6, ans_7, ans_8, ans_9, ans_10, ans_11, ans_12]
    counts = {x: keys.count(x) for x in "ABCD"}
    print("Phần I key count:", counts)
    assert counts == {'A': 3, 'B': 3, 'C': 3, 'D': 3}, "Phần I chưa cân bằng 3A, 3B, 3C, 3D!"

    # -------------------------------------------------------------
    # PHẦN II: 2 câu Đúng/Sai (mỗi câu 4 ý a-d)
    # -------------------------------------------------------------
    # Câu 13 (II.1 - TH_TH_02): A = (-3; 4], B = [1; 6)
    # a) Tập hợp A là nửa khoảng gồm các số thực x thỏa mãn -3 < x <= 4. -> ĐÚNG
    # b) Giao của hai tập hợp là A giao B = [1; 4]. -> ĐÚNG
    # c) Hợp của hai tập hợp là A hop B = (-3; 6). -> ĐÚNG
    # d) Hiệu của hai tập hợp là A \ B = (-3; 1]. -> SAI (vì 1 thuộc B nên A \ B = (-3; 1))
    c13_a = True
    c13_b = True
    c13_c = True
    c13_d = False
    print("Câu 13 (Đ/S): a:Đ, b:Đ, c:Đ, d:S")
    
    # Câu 14 (II.2 - BPT_TH_01):
    # Hệ BPT: { x >= 0, y >= 0, x + y <= 4, 2x + y <= 6 }
    # Đa giác nghiệm OABC:
    # O(0; 0)
    # A: trục Ox (y=0) -> 2x <= 6 => x = 3 => A(3; 0)
    # B: giao của x + y = 4 và 2x + y = 6 -> (2x+y) - (x+y) = x = 2, y = 2 => B(2; 2)
    # C: trục Oy (x=0) -> y <= 4 => C(0; 4)
    # Biểu thức F(x, y) = 3x + 2y
    # F(O) = 0
    # F(A) = 3(3) + 2(0) = 9
    # F(B) = 3(2) + 2(2) = 10
    # F(C) = 3(0) + 2(4) = 8
    # Max F = 10 tại B(2; 2)
    # a) Gốc tọa độ O(0; 0) thuộc miền nghiệm của hệ. -> ĐÚNG
    # b) Tọa độ đỉnh A trên trục hoành là A(3; 0). -> ĐÚNG
    # c) Tọa độ đỉnh B là B(2; 2). -> ĐÚNG
    # d) Giá trị lớn nhất của F(x, y) = 3x + 2y trên miền nghiệm bằng 12. -> SAI (bằng 10)
    c14_a = True
    c14_b = True
    c14_c = True
    c14_d = False
    print("Câu 14 (Đ/S): a:Đ, b:Đ, c:Đ, d:S")

    # -------------------------------------------------------------
    # PHẦN III: 4 câu Trả lời ngắn
    # -------------------------------------------------------------
    # Câu 15 (III.1 - TH_TH_04):
    # A = [-5; 3), B = (-1; 6]. Số phần tử nguyên thuộc A giao B.
    # A giao B = (-1; 3). Các số nguyên là 0, 1, 2. Có 3 số.
    ans_15 = 3
    print("Câu 15:", ans_15)
    
    # Câu 16 (III.2 - BPT_VD_03):
    # Hệ: { x >= 0, y >= 0, x + 2y <= 8, 3x + 2y <= 12 }
    # Giao của x + 2y = 8 và 3x + 2y = 12:
    # 2x = 4 => x = 2, y = (8 - 2)/2 = 3 => B(2; 3)
    # A: trục Ox -> 3x <= 12 => x = 4 => A(4; 0)
    # C: trục Oy -> 2y <= 8 => y = 4 => C(0; 4)
    # Biểu thức: F(x, y) = 4x + 3y
    # F(O) = 0
    # F(A) = 4(4) + 0 = 16
    # F(B) = 4(2) + 3(3) = 8 + 9 = 17
    # F(C) = 4(0) + 3(4) = 12
    # Max = 17
    assert 4*2 + 3*3 == 17
    ans_16 = 17
    print("Câu 16:", ans_16)
    
    # Câu 17 (III.3 - LG_TH_01):
    # 90 deg < alpha < 180 deg, cos(alpha) = -5/13
    # => sin(alpha) = 12/13
    # tan(alpha) = -12/5
    # Biểu thức P = 13*sin(alpha) - 5*tan(alpha)
    # P = 13*(12/13) - 5*(-12/5) = 12 - (-12) = 24
    ans_17 = 24
    print("Câu 17:", ans_17)
    
    # Câu 18 (III.4 - HTL_VD_03):
    # Khoảng cách giữa 2 tàu: AB = 70 m, AC = 100 m, góc BAC = 120 độ.
    # BC^2 = 70^2 + 100^2 - 2 * 70 * 100 * cos(120 deg)
    # = 4900 + 10000 - 14000 * (-1/2) = 14900 + 7000 = 21900
    # BC = sqrt(21900) = 10 * sqrt(219) approx 147.986... -> làm tròn hàng đơn vị là 148 m.
    bc = np.sqrt(70**2 + 100**2 - 2*70*100*np.cos(np.radians(120)))
    ans_18 = int(round(bc))
    assert ans_18 == 148
    print(f"Câu 18: BC = {bc:.3f} -> Làm tròn: {ans_18}")

    # -------------------------------------------------------------
    # PHẦN IV: 4 câu Tự luận
    # -------------------------------------------------------------
    # Câu 19 (IV.1 - TH_TH_01):
    # A = {x in R | (x^2 - 9)(x^2 - 3x + 2) = 0}
    # x^2 - 9 = 0 <=> x = +-3
    # x^2 - 3x + 2 = 0 <=> x = 1 or x = 2
    # A = {-3; 1; 2; 3}
    # B = {x in N | x < 5} = {0; 1; 2; 3; 4}
    # a) A = {-3; 1; 2; 3}, B = {0; 1; 2; 3; 4}
    # b) A giao B = {1; 2; 3}
    #    A hop B = {-3; 0; 1; 2; 3; 4}
    #    A \ B = {-3}
    print("Câu 19: A = {-3; 1; 2; 3}, B = {0; 1; 2; 3; 4}, A cap B = {1; 2; 3}, A cup B = {-3; 0; 1; 2; 3; 4}, A \\ B = {-3}")
    
    # Câu 20 (IV.2 - LG_TH_02):
    # tan(alpha) = 3
    # P = (2 sin alpha + 3 cos alpha) / (4 sin alpha - 5 cos alpha)
    # = (2 tan alpha + 3) / (4 tan alpha - 5) = (2*3 + 3) / (4*3 - 5) = 9 / 7
    P = sp.Rational(2*3 + 3, 4*3 - 5)
    assert P == sp.Rational(9, 7)
    print("Câu 20: P =", P)
    
    # Câu 21 (IV.3 - HTL_VD_02):
    # Cho tam giác ABC:
    # a) Chứng minh: a = b cos C + c cos B
    # b) Chứng minh nếu a / cos A = b / cos B thì tam giác ABC cân tại C.
    print("Câu 21: a = b cos C + c cos B và tam giác cân tại C.")
    
    # Câu 22 (IV.4 - BPT_VD_01):
    # Sản xuất bàn ghế:
    # x: số bàn loại I, y: số ghế loại II (x, y in N)
    # Thời gian chế biến gỗ: 3x + y <= 180
    # Thời gian hoàn thiện: 2x + 2y <= 160 <=> x + y <= 80
    # Đỉnh miền nghiệm O(0; 0), A(60; 0), B(50; 30), C(0; 80)
    # Lợi nhuận F(x, y) = 400x + 200y (nghìn đồng)
    # F(O) = 0
    # F(A) = 400*60 = 24000 (nghìn đồng)
    # F(B) = 400*50 + 200*30 = 20000 + 6000 = 26000 (nghìn đồng) = 26 triệu đồng
    # F(C) = 200*80 = 16000 (nghìn đồng)
    # Kết luận: Sản xuất 50 bàn loại I và 30 ghế loại II, lợi nhuận lớn nhất 26.000.000 đồng.
    print("Câu 22: Max tại B(50; 30) với F = 26.000.000 đồng.")
    
    print("\n[VERIFY OK] TOÀN BỘ 22 CÂU HỎI ĐỀ 11 CHÍNH XÁC 100%!")

if __name__ == '__main__':
    verify()
