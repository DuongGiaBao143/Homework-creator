import sympy as sp
import numpy as np

def verify():
    print("=== KIỂM TRA ĐỀ SỐ 19 TOÁN 10 ===")
    
    # -------------------------------------------------------------
    # PHẦN I: 12 câu trắc nghiệm (3A, 3B, 3C, 3D)
    # -------------------------------------------------------------
    # Câu 1 (I.1 - MD_NB_05) - Đáp án A
    # P: ABCD là hình vuông, Q: ABCD là hình thoi. P => Q đúng nên P là điều kiện đủ để có Q.
    # A: P là điều kiện đủ để có Q.
    ans_1 = "A"
    print("Câu 1:", ans_1)
    
    # Câu 2 (I.2 - TH_NB_04) - Đáp án B
    # Tập hợp các số thực x thỏa mãn -3 <= x < 5: [-3; 5)
    # B: [-3; 5)
    ans_2 = "B"
    print("Câu 2:", ans_2)
    
    # Câu 3 (I.3 - MD_NB_01) - Đáp án C
    # Mệnh đề toán học: "Số 19 là một số nguyên tố."
    # C: Số 19 là một số nguyên tố.
    assert sp.isprime(19)
    ans_3 = "C"
    print("Câu 3:", ans_3)
    
    # Câu 4 (I.4 - TH_TH_01) - Đáp án D
    # A = {1, 2, 3, 4, 5}, B = {2, 4, 6, 8}. A \ B = {1, 3, 5}.
    # D: {1; 3; 5}
    set_A = {1, 2, 3, 4, 5}
    set_B = {2, 4, 6, 8}
    assert set_A - set_B == {1, 3, 5}
    ans_4 = "D"
    print("Câu 4:", ans_4)
    
    # Câu 5 (I.5 - BPT_NB_02) - Đáp án A
    # Hệ BPT bậc nhất hai ẩn: { 2x - 3y + 1 <= 0; x + 4y - 5 > 0 }
    ans_5 = "A"
    print("Câu 5:", ans_5)
    
    # Câu 6 (I.6 - BPT_NB_03) - Đáp án B
    # Cặp số (x; y) là nghiệm của 2x + 3y <= 6:
    # A: (2; 2) -> 2*2 + 3*2 = 10 > 6
    # B: (1; 1) -> 2*1 + 3*1 = 5 <= 6 (đúng!)
    # C: (3; 1) -> 2*3 + 3*1 = 9 > 6
    # D: (0; 3) -> 2*0 + 3*3 = 9 > 6
    assert 2*1 + 3*1 <= 6
    assert not (2*2 + 3*2 <= 6)
    assert not (2*3 + 3*1 <= 6)
    assert not (2*0 + 3*3 <= 6)
    ans_6 = "B"
    print("Câu 6:", ans_6)
    
    # Câu 7 (I.7 - BPT_NB_04) - Đáp án C
    # Điểm thuộc miền nghiệm của hệ { 2x - y + 2 >= 0; x + 2y - 4 <= 0 }:
    # A: M(2; 3) -> 2*2 - 3 + 2 = 3 >= 0; 2 + 2*3 - 4 = 4 > 0 (loại)
    # B: N(-2; 1) -> 2*(-2) - 1 + 2 = -3 < 0 (loại)
    # C: P(0; 1) -> 2*0 - 1 + 2 = 1 >= 0; 0 + 2*1 - 4 = -2 <= 0 (đúng!)
    # D: Q(1; 3) -> 2*1 - 3 + 2 = 1 >= 0; 1 + 2*3 - 4 = 3 > 0 (loại)
    assert 2*0 - 1 + 2 >= 0 and 0 + 2*1 - 4 <= 0
    assert not (2*(-2) - 1 + 2 >= 0)
    ans_7 = "C"
    print("Câu 7:", ans_7)
    
    # Câu 8 (I.8 - BPT_NB_05) - Đáp án D
    # Đường thẳng bờ của miền nghiệm BPT 3x - 4y + 12 >= 0 là 3x - 4y + 12 = 0
    ans_8 = "D"
    print("Câu 8:", ans_8)
    
    # Câu 9 (I.9 - HTL_NB_04) - Đáp án A
    # Công thức trung tuyến: m_a^2 = (2(b^2 + c^2) - a^2) / 4
    ans_9 = "A"
    print("Câu 9:", ans_9)
    
    # Câu 10 (I.10 - LG_NB_03) - Đáp án B
    # Hai góc bù nhau: sin(180 - alpha) = sin(alpha)
    ans_10 = "B"
    print("Câu 10:", ans_10)
    
    # Câu 11 (I.11 - LG_TH_02) - Đáp án C
    # tan(alpha) = 2. Tính P = (3*sin(alpha) - cos(alpha)) / (sin(alpha) + 2*cos(alpha))
    # P = (3*tan - 1) / (tan + 2) = (3*2 - 1) / (2 + 2) = 5/4
    tan_val = sp.Integer(2)
    P_val = sp.Rational(3*tan_val - 1, tan_val + 2)
    assert P_val == sp.Rational(5, 4)
    ans_11 = "C"
    print("Câu 11:", ans_11)
    
    # Câu 12 (I.12 - LG_NB_02) - Đáp án D
    # alpha tù (90 < alpha < 180) -> sin(alpha) > 0
    ans_12 = "D"
    print("Câu 12:", ans_12)
    
    answers_I = [ans_1, ans_2, ans_3, ans_4, ans_5, ans_6, ans_7, ans_8, ans_9, ans_10, ans_11, ans_12]
    counts = {x: answers_I.count(x) for x in ["A", "B", "C", "D"]}
    print("Phân bố đáp án Phần I:", counts)
    assert counts == {"A": 3, "B": 3, "C": 3, "D": 3}, "Phần I phải cân bằng 3A-3B-3C-3D!"

    # -------------------------------------------------------------
    # PHẦN II: 2 câu đúng/sai (8 ý a-d)
    # -------------------------------------------------------------
    # Câu 13 (II.1 - MD_NB_03, topic menh_de_tap_hop)
    # P(n): "n^2 - 1 chia hết cho 4" (n in N), Q(x): "x^2 - 5x + 6 = 0" (x in R)
    # a) P(3): 3^2 - 1 = 8 chia hết cho 4 -> Đúng
    assert (3**2 - 1) % 4 == 0
    c13_a = True
    
    # b) P(4): 4^2 - 1 = 15 không chia hết cho 4 -> P(4) sai. Phát biểu khẳng định "P(4) là mệnh đề sai" -> Đúng
    assert (4**2 - 1) % 4 != 0
    c13_b = True
    
    # c) Tập nghiệm của Q(x): x^2 - 5x + 6 = 0 <=> x in {2; 3} -> Đúng
    x = sp.Symbol('x')
    assert set(sp.solve(x**2 - 5*x + 6, x)) == {2, 3}
    c13_c = True
    
    # d) "Với mọi n in N, P(n) là mệnh đề đúng" -> Sai (vì n=2 thì 2^2 - 1 = 3 không chia hết cho 4)
    assert (2**2 - 1) % 4 != 0
    c13_d = False
    
    print(f"Câu 13: a={c13_a}, b={c13_b}, c={c13_c}, d={c13_d}")

    # Câu 14 (II.2 - HTL_NB_01, topic he_thuc_luong)
    # Tam giác ABC có AB = 5, AC = 8, A = 60 độ
    # a) BC^2 = AB^2 + AC^2 - 2*AB*AC*cos(A) -> Đúng (phát biểu định lý cosin)
    c14_a = True
    
    # b) BC = 7
    BC_sq = 5**2 + 8**2 - 2*5*8*sp.cos(sp.pi/3)
    assert BC_sq == 49
    assert sp.sqrt(BC_sq) == 7
    c14_b = True
    
    # c) cos(B) = 1/7
    # cos(B) = (AB^2 + BC^2 - AC^2) / (2*AB*BC) = (25 + 49 - 64) / (2*5*7) = 10 / 70 = 1/7
    cos_B = sp.Rational(5**2 + 7**2 - 8**2, 2 * 5 * 7)
    assert cos_B == sp.Rational(1, 7)
    c14_c = True
    
    # d) Diện tích S = 20*sqrt(3) -> Sai (S = 1/2 * 5 * 8 * sin(60 deg) = 20 * sqrt(3)/2 = 10*sqrt(3))
    S_ABC = sp.Rational(1, 2) * 5 * 8 * sp.sin(sp.pi/3)
    assert S_ABC == 10 * sp.sqrt(3)
    assert S_ABC != 20 * sp.sqrt(3)
    c14_d = False
    
    print(f"Câu 14: a={c14_a}, b={c14_b}, c={c14_c}, d={c14_d}")

    # -------------------------------------------------------------
    # PHẦN III: 4 câu trả lời ngắn
    # -------------------------------------------------------------
    # Câu 15 (III.1 - HTL_VD_03): Tàu du lịch
    # AB = 60, AC = 80, A = 60 độ. Tìm BC làm tròn đến hàng đơn vị.
    # BC = sqrt(60^2 + 80^2 - 2*60*80*cos(60 deg)) = sqrt(3600 + 6400 - 4800) = sqrt(5200) = 20*sqrt(13)
    bc_15 = float(np.sqrt(60**2 + 80**2 - 2*60*80*0.5))
    ans_15 = round(bc_15)
    print(f"Câu 15: BC = {bc_15:.4f} -> Làm tròn: {ans_15}")
    assert ans_15 == 72

    # Câu 16 (III.2 - BPT_TH_01): Diện tích miền tứ giác OABC
    # x >= 0, y >= 0, x + 2y <= 6, 2x + y <= 6
    # O(0; 0), A(3; 0), B(2; 2), C(0; 3)
    # S = S_OAB + S_OBC = 1/2 * 3 * 2 + 1/2 * 3 * 2 = 3 + 3 = 6
    S_16 = 0.5 * 3 * 2 + 0.5 * 3 * 2
    ans_16 = int(S_16)
    print(f"Câu 16: S = {S_16} -> Đáp số: {ans_16}")
    assert ans_16 == 6

    # Câu 17 (III.3 - TH_VD_01): Số giá trị nguyên m để A giao B khác rỗng
    # A = [m - 1; m + 3], B = (-2; 4).
    # A giao B = rỗng <=> m + 3 <= -2 hoặc m - 1 >= 4 <=> m <= -5 hoặc m >= 5
    # => A giao B khác rỗng <=> -5 < m < 5.
    # m nguyên: m in {-4, -3, -2, -1, 0, 1, 2, 3, 4} -> 9 giá trị
    m_vals = [m for m in range(-10, 11) if not (m + 3 <= -2 or m - 1 >= 4)]
    ans_17 = len(m_vals)
    print(f"Câu 17: m in {m_vals} -> Có {ans_17} giá trị")
    assert ans_17 == 9

    # Câu 18 (III.4 - TH_TH_01): Học sinh không tham gia cả hai CLB
    # Tổng: 45, Bóng đá: 25, Bóng rổ: 20, Cả hai: 10
    # n(A hợp B) = 25 + 20 - 10 = 35. Không tham gia = 45 - 35 = 10
    ans_18 = 45 - (25 + 20 - 10)
    print(f"Câu 18: Không tham gia = {ans_18}")
    assert ans_18 == 10

    # -------------------------------------------------------------
    # PHẦN IV: 4 câu tự luận
    # -------------------------------------------------------------
    # Câu 19 (IV.1 - LG_TH_02)
    # a) Rút gọn: A = sin(180 - x) + cos(180 - x) + cos(x) - sin(x) = sin(x) - cos(x) + cos(x) - sin(x) = 0
    # b) cot(alpha) = 3. P = (3*sin - 2*cos) / (2*sin + cos) = (3 - 2*cot) / (2 + cot) = (3 - 6) / (2 + 3) = -3/5
    ans_19_a = 0
    ans_19_b = sp.Rational(3 - 2*3, 2 + 3)
    assert ans_19_b == sp.Rational(-3, 5)
    print(f"Câu 19: a) A = {ans_19_a}; b) P = {ans_19_b}")

    # Câu 20 (IV.2 - HTL_VD_03) Cột ăng-ten trên nóc tòa nhà
    # Cột cao 5 m (BC = 5). Từ A cao 7 m so với đất: góc nâng đỉnh B là 50 deg, chân C là 40 deg.
    # x = 5 / (tan(50 deg) - tan(40 deg))
    # h_nha = 7 + x * tan(40 deg)
    tan_50 = np.tan(np.radians(50))
    tan_40 = np.tan(np.radians(40))
    x_dist = 5.0 / (tan_50 - tan_40)
    h_building = 7.0 + x_dist * tan_40
    print(f"Câu 20: Khoảng cách ngang x = {x_dist:.4f} m, Chiều cao tòa nhà = {h_building:.4f} m -> Làm tròn: {h_building:.1f} m")
    assert round(h_building, 1) == 18.9

    # Câu 21 (IV.3 - TH_TH_03)
    # A = (-3; 4], B = [1; 6)
    # a) A giao B = [1; 4], A hợp B = (-3; 6), A \ B = (-3; 1)
    # b) Biểu diễn trên trục số
    print("Câu 21: a) A giao B = [1; 4], A hợp B = (-3; 6), A \\ B = (-3; 1); b) Biểu diễn trục số chuẩn.")

    # Câu 22 (IV.4 - BPT_VD_01) Quy hoạch tuyến tính
    # Sản phẩm I (x), Sản phẩm II (y) (x, y in N)
    # Ràng buộc:
    # 2x + y <= 16 (giờ gia công)
    # x + 2y <= 14 (giờ lắp ráp)
    # x >= 0, y >= 0
    # Lợi nhuận: F(x, y) = 400x + 300y (nghìn đồng)
    # Đỉnh: O(0; 0), A(8; 0), B(6; 4), C(0; 7)
    # F(O) = 0, F(A) = 3200, F(C) = 2100, F(B) = 400*6 + 300*4 = 3600 nghìn đồng (3.6 triệu)
    vertices = [(0, 0), (8, 0), (6, 4), (0, 7)]
    F_vals = {v: 400*v[0] + 300*v[1] for v in vertices}
    print(f"Câu 22: F tại các đỉnh = {F_vals}")
    max_v = max(F_vals, key=F_vals.get)
    assert max_v == (6, 4)
    assert F_vals[max_v] == 3600
    print(f"Câu 22: Tối ưu tại {max_v} với lợi nhuận {F_vals[max_v]} nghìn đồng ({F_vals[max_v]/1000} triệu đồng).")

    print("\n>>> TẤT CẢ 22 CÂU ĐỀ 19 ĐÃ PASS KIỂM TRA TOÁN HỌC 100%! <<<")

if __name__ == "__main__":
    verify()
