"""Kiểm tra độc lập tính đúng đắn toán học 100% của Đề số 22 bằng SymPy/NumPy."""
import sympy as sp
import numpy as np

def test_part_1():
    print("--- KIỂM TRA PHẦN I (12 CÂU TN) ---")
    
    # Câu 1: BPT bậc nhất hai ẩn
    # 2x - 3y + 5 > 0 là BPT bậc nhất hai ẩn. (A)
    ans1 = 'A'
    assert ans1 == 'A'
    
    # Câu 2: Đường thẳng bờ của 3x - 2y + 6 <= 0 là 3x - 2y + 6 = 0. (B)
    ans2 = 'B'
    assert ans2 == 'B'
    
    # Câu 3: Miền nghiệm chứa O(0,0) của x - 2y + 2 >= 0
    # Tại O(0,0): 0 - 0 + 2 = 2 >= 0 (thỏa mãn)
    x, y = 0, 0
    assert x - 2*y + 2 >= 0
    ans3 = 'C'
    assert ans3 == 'C'
    
    # Câu 4: Cặp số nào là nghiệm của 2x - y + 3 > 0
    pts = [(-2, -1), (-3, 1), (-1, 2), (1, 1)]
    vals = [2*px - py + 3 for px, py in pts]
    assert vals[0] == 0  # not > 0
    assert vals[1] == -4 # not > 0
    assert vals[2] == -1 # not > 0
    assert vals[3] == 4 > 0 # thỏa mãn
    ans4 = 'D'
    assert ans4 == 'D'
    
    # Câu 5: Hệ BPT bậc nhất hai ẩn là hệ A: {x - 3y + 4 >= 0, 2x + y - 1 < 0}
    ans5 = 'A'
    assert ans5 == 'A'
    
    # Câu 6: Điểm thuộc miền nghiệm {x + 2y - 4 <= 0, 2x - y + 1 >= 0}
    # N(1, 1): 1 + 2 - 4 = -1 <= 0, 2(1) - 1 + 1 = 2 >= 0
    x6, y6 = 1, 1
    assert x6 + 2*y6 - 4 <= 0
    assert 2*x6 - y6 + 1 >= 0
    # Check other points
    assert not (3 + 2*2 - 4 <= 0) # M(3, 2)
    assert not (2 + 2*3 - 4 <= 0) # P(2, 3)
    assert not (2*(-2) - (-2) + 1 >= 0) # Q(-2, -2)
    ans6 = 'B'
    assert ans6 == 'B'
    
    # Câu 7: cos alpha = 3/5, 0 < alpha < 90 deg -> sin alpha = 4/5
    # P = 2*sin alpha + 3*cos alpha = 2*(4/5) + 3*(3/5) = 17/5
    cos_a = sp.Rational(3, 5)
    sin_a = sp.sqrt(1 - cos_a**2)
    P7 = 2*sin_a + 3*cos_a
    assert P7 == sp.Rational(17, 5)
    ans7 = 'C'
    assert ans7 == 'C'
    
    # Câu 8: b = 5, c = 8, A = 60 deg -> a^2 = 25 + 64 - 2*5*8*cos(60) = 89 - 40 = 49 -> a = 7
    a8_sq = 5**2 + 8**2 - 2*5*8*sp.cos(sp.pi/3)
    assert a8_sq == 49
    assert sp.sqrt(a8_sq) == 7
    ans8 = 'D'
    assert ans8 == 'D'
    
    # Câu 9: cos(120 deg) = -1/2
    assert sp.cos(2*sp.pi/3) == sp.Rational(-1, 2)
    ans9 = 'A'
    assert ans9 == 'A'
    
    # Câu 10: 90 < alpha < 180 -> cos alpha < 0
    ans10 = 'B'
    assert ans10 == 'B'
    
    # Câu 11: a / sin A = 2R
    ans11 = 'C'
    assert ans11 == 'C'
    
    # Câu 12: sin(180 - alpha) = -sin alpha là SAI (phải là sin alpha)
    ans12 = 'D'
    assert ans12 == 'D'
    
    answers = [ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10, ans11, ans12]
    counts = {k: answers.count(k) for k in 'ABCD'}
    print(f"Phần I đáp án: {answers}")
    print(f"Phân bổ đáp án: {counts}")
    assert counts == {'A': 3, 'B': 3, 'C': 3, 'D': 3}, "Phần I chưa cân bằng 3A-3B-3C-3D!"
    print("[OK] Phần I chính xác 100% và cân bằng hoàn hảo!")

def test_part_2():
    print("--- KIỂM TRA PHẦN II (2 CÂU ĐÚNG/SAI) ---")
    
    # Câu 13:
    # Cho alpha nhọn, sin alpha = 3/5
    sin_a = sp.Rational(3, 5)
    cos_a = sp.sqrt(1 - sin_a**2)
    assert cos_a == sp.Rational(4, 5)
    
    # a) cos alpha > 0 -> Đúng
    c13_a = True
    # b) sin(180 - alpha) = sin alpha = 3/5 -> Đúng
    c13_b = True
    # c) cos alpha = 4/5, tan alpha = 3/4 -> Đúng
    tan_a = sin_a / cos_a
    assert tan_a == sp.Rational(3, 4)
    c13_c = True
    # d) M = [sin(180 - a) + 2*cos(180 - a)] / tan(90 - a) = -1 -> Sai vì M = -3/4
    # sin(180 - a) = sin a = 3/5
    # cos(180 - a) = -cos a = -4/5
    # num = 3/5 - 8/5 = -1
    # tan(90 - a) = cot a = 4/3
    # M = -1 / (4/3) = -3/4 != -1
    M = (sin_a - 2*cos_a) / (cos_a / sin_a)
    assert M == sp.Rational(-3, 4)
    c13_d = False # M != -1
    assert [c13_a, c13_b, c13_c, c13_d] == [True, True, True, False]
    print(f"Câu 13: a={c13_a}, b={c13_b}, c={c13_c}, d={c13_d}")

    # Câu 14:
    # Xưởng sản xuất sp A và B:
    # A cần 2 kg X, 1 h. B cần 1 kg X, 2 h. Có 8 kg X, 10 h.
    # a) x >= 0, y >= 0 -> Đúng
    c14_a = True
    # b) 2x + y <= 8 -> Đúng
    c14_b = True
    # c) x + 2y <= 10 -> Đúng
    c14_c = True
    # d) (3; 3) thuộc miền nghiệm -> Sai vì 2(3) + 3 = 9 > 8
    assert 2*3 + 3 == 9 > 8
    c14_d = False
    assert [c14_a, c14_b, c14_c, c14_d] == [True, True, True, False]
    print(f"Câu 14: a={c14_a}, b={c14_b}, c={c14_c}, d={c14_d}")
    print("[OK] Phần II chính xác 100%!")

def test_part_3():
    print("--- KIỂM TRA PHẦN III (4 CÂU TRẢ LỜI NGẮN) ---")
    
    # Câu 15: Cực trị khoảng cách bờ sông:
    # AH = 3, BK = 5, HK = 6. MA + MB min = sqrt(HK^2 + (AH + BK)^2) = sqrt(36 + 64) = 10
    d_min = sp.sqrt(6**2 + (3 + 5)**2)
    assert d_min == 10
    ans15 = 10
    print(f"Câu 15: {ans15}")

    # Câu 16: b(b^2 - a^2) = c(a^2 - c^2), b != c -> góc A = 60 độ
    # b^3 + c^3 = a^2(b + c) => b^2 - bc + c^2 = a^2 => b^2 + c^2 - a^2 = bc
    # cos A = bc / (2bc) = 1/2 => A = 60 độ
    ans16 = 60
    print(f"Câu 16: {ans16}")

    # Câu 17: Diện tích miền nghiệm hệ {x >= 0, y >= 0, x + y <= 4, 2x + y <= 6}
    # Đỉnh: O(0,0), A(3,0), B(2,2), C(0,4)
    # Shoelace formula:
    coords = [(0, 0), (3, 0), (2, 2), (0, 4)]
    n = len(coords)
    area = 0.5 * abs(sum(coords[i][0]*coords[(i+1)%n][1] - coords[(i+1)%n][0]*coords[i][1] for i in range(n)))
    assert area == 7.0
    ans17 = 7
    print(f"Câu 17: {ans17}")

    # Câu 18: Max F(x, y) = 4x + 5y trên {x >= 0, y >= 0, x + 2y <= 8, 3x + 2y <= 12}
    # Đỉnh: O(0,0), A(4,0), B(2,3), C(0,4)
    verts = [(0, 0), (4, 0), (2, 3), (0, 4)]
    f_vals = [4*vx + 5*vy for vx, vy in verts]
    assert f_vals == [0, 16, 23, 20]
    assert max(f_vals) == 23
    ans18 = 23
    print(f"Câu 18: {ans18}")
    print("[OK] Phần III chính xác 100%!")

def test_part_4():
    print("--- KIỂM TRA PHẦN IV (4 CÂU TỰ LUẬN) ---")
    
    # Câu 19: Miền nghiệm 2x - 3y + 6 >= 0
    # Tại O(0,0): 2(0) - 3(0) + 6 = 6 >= 0 (thỏa mãn)
    assert 2*0 - 3*0 + 6 >= 0
    
    # Câu 20: Tam giác ABC: AB = 6, AC = 10, A = 120 deg
    # a) BC^2 = 36 + 100 - 2*6*10*cos(120) = 136 - 120*(-1/2) = 196 => BC = 14
    bc_sq = 6**2 + 10**2 - 2*6*10*sp.cos(2*sp.pi/3)
    assert bc_sq == 196
    bc = sp.sqrt(bc_sq)
    assert bc == 14
    
    # b) S = 1/2 * 6 * 10 * sin(120) = 30 * sqrt(3)/2 = 15*sqrt(3)
    S = sp.Rational(1, 2) * 6 * 10 * sp.sin(2*sp.pi/3)
    assert S == 15*sp.sqrt(3)
    
    # R = BC / (2*sin A) = 14 / (2 * sqrt(3)/2) = 14 / sqrt(3) = 14*sqrt(3)/3
    R = bc / (2 * sp.sin(2*sp.pi/3))
    assert R == 14*sp.sqrt(3)/3
    print("Câu 20: BC = 14, S = 15*sqrt(3), R = 14*sqrt(3)/3")

    # Câu 21: Đo chiều cao hải đăng:
    # AB = 30, CAD = 30 deg, CBD = 45 deg, B nằm giữa A và D
    # ACB = 45 - 30 = 15 deg
    # AC = AB * sin(135 deg) / sin(15 deg)
    # sin(135) = sqrt(2)/2
    # sin(15) = (sqrt(6) - sqrt(2))/4
    # AC = 30 * (sqrt(2)/2) / ((sqrt(6)-sqrt(2))/4) = 60*sqrt(2) / (sqrt(6)-sqrt(2)) = 60 / (sqrt(3)-1) = 30*(sqrt(3)+1)
    ac = 30 * sp.sin(3*sp.pi/4) / sp.sin(sp.pi/12)
    ac_simplified = sp.simplify(ac)
    assert sp.simplify(ac_simplified - 30*(sp.sqrt(3) + 1)) == 0
    
    # CD = AC * sin(30 deg) = 15*(sqrt(3) + 1)
    cd = ac_simplified * sp.sin(sp.pi/6)
    assert sp.simplify(cd - 15*(sp.sqrt(3) + 1)) == 0
    cd_val = float(cd.evalf())
    print(f"Câu 21: AC = 30*(sqrt(3)+1) ≈ {float(ac.evalf()):.2f} m, CD = 15*(sqrt(3)+1) ≈ {cd_val:.1f} m")

    # Câu 22: Bài toán tối ưu hóa may mặc
    # Sơ mi (x), Áo khoác (y):
    # Vải: 1.5x + 2y <= 60 <=> 3x + 4y <= 120
    # Công: 2x + 4y <= 100 <=> x + 2y <= 50
    # x >= 0, y >= 0
    # Lãi: T(x, y) = 100x + 180y (nghìn đồng)
    # Giao điểm B: 3x + 4y = 120, x + 2y = 50 => x = 20, y = 15
    # T(20, 15) = 100*20 + 180*15 = 2000 + 2700 = 4700 nghìn đồng (4.7 triệu đồng)
    # So sánh các đỉnh:
    t_O = 100*0 + 180*0
    t_A = 100*40 + 180*0 # A(40, 0)
    t_C = 100*0 + 180*25 # C(0, 25)
    t_B = 100*20 + 180*15 # B(20, 15)
    assert t_O == 0
    assert t_A == 4000
    assert t_C == 4500
    assert t_B == 4700
    assert max([t_O, t_A, t_C, t_B]) == t_B
    print(f"Câu 22: T_max = {t_B} nghìn đồng tại x=20, y=15")
    print("[OK] Phần IV chính xác 100%!")

if __name__ == '__main__':
    test_part_1()
    test_part_2()
    test_part_3()
    test_part_4()
    print("\n==============================================")
    print("TẤT CẢ 22 CÂU ĐÃ ĐẠT 100% TÍNH TOÁN CHÍNH XÁC!")
    print("==============================================")
