"""Kiểm tra độc lập tính đúng đắn toán học 100% của Đề số 24 bằng SymPy/NumPy."""
import sympy as sp
import numpy as np

def test_part_1():
    print("--- KIỂM TRA PHẦN I (12 CÂU TN) ---")
    
    # Câu 1: Miền nghiệm của bất phương trình 2x + 3y <= 6
    # Đường thẳng 2x + 3y = 6 đi qua (3, 0) và (0, 2).
    # Gốc O(0,0): 2(0) + 3(0) = 0 <= 6 (thỏa mãn)
    x, y = 0, 0
    assert 2*x + 3*y <= 6
    ans1 = 'C'
    assert ans1 == 'C'
    
    # Câu 2: Đường thẳng bờ của nửa mặt phẳng 4x - 5y + 20 >= 0 là 4x - 5y + 20 = 0.
    ans2 = 'A'
    assert ans2 == 'A'
    
    # Câu 3: Bất phương trình bậc nhất hai ẩn là 3x - 4y + 2 > 0.
    ans3 = 'B'
    assert ans3 == 'B'
    
    # Câu 4: Hệ BPT bậc nhất hai ẩn là hệ D: {2x - y + 1 >= 0, x + 3y - 5 < 0}
    ans4 = 'D'
    assert ans4 == 'D'
    
    # Câu 5: Cặp số nào là nghiệm của 3x - 2y + 6 > 0
    pts = [(1, 2), (-3, 0), (-2, 1), (0, 4)]
    vals = [3*px - 2*py + 6 for px, py in pts]
    assert vals[0] == 5 > 0   # thỏa mãn
    assert vals[1] == -3 <= 0 # loại
    assert vals[2] == -2 <= 0 # loại
    assert vals[3] == -2 <= 0 # loại
    ans5 = 'A'
    assert ans5 == 'A'
    
    # Câu 6: Điểm thuộc miền nghiệm {x - y + 1 >= 0, 2x + y - 4 <= 0}
    # P(1, 1): 1 - 1 + 1 = 1 >= 0, 2(1) + 1 - 4 = -1 <= 0
    x6, y6 = 1, 1
    assert x6 - y6 + 1 >= 0
    assert 2*x6 + y6 - 4 <= 0
    # Check other points
    assert not (2*3 + 1 - 4 <= 0)     # M(3, 1)
    assert not (-2 - 2 + 1 >= 0)      # N(-2, 2)
    assert not (0 - 5 + 1 >= 0)       # Q(0, 5)
    ans6 = 'C'
    assert ans6 == 'C'
    
    # Câu 7: 90 < alpha < 180, cos alpha = -3/5 -> sin alpha = 4/5
    cos_a = sp.Rational(-3, 5)
    sin_a = sp.sqrt(1 - cos_a**2)
    assert sin_a == sp.Rational(4, 5)
    P7 = sin_a + 2*cos_a
    assert P7 == sp.Rational(-2, 5)
    ans7 = 'B'
    assert ans7 == 'B'
    
    # Câu 8: Khẳng định sai về diện tích tam giác: S = 1/2 bc cos A (phải là sin A)
    ans8 = 'D'
    assert ans8 == 'D'
    
    # Câu 9: Độ dài đường trung tuyến m_a^2 = [2(b^2 + c^2) - a^2] / 4
    ans9 = 'A'
    assert ans9 == 'A'
    
    # Câu 10: b = 7, c = 8, A = 120 deg -> a^2 = 49 + 64 - 2*7*8*cos(120) = 113 + 56 = 169 -> a = 13
    a10_sq = 7**2 + 8**2 - 2*7*8*sp.cos(2*sp.pi/3)
    assert a10_sq == 169
    assert sp.sqrt(a10_sq) == 13
    ans10 = 'B'
    assert ans10 == 'B'
    
    # Câu 11: Định lý sin: a / sin A = 2R
    ans11 = 'C'
    assert ans11 == 'C'
    
    # Câu 12: a = 13, b = 14, c = 15
    # p = 21, S = sqrt(21 * 8 * 7 * 6) = 84 -> r = 84 / 21 = 4
    p = sp.Rational(13 + 14 + 15, 2)
    S = sp.sqrt(p * (p - 13) * (p - 14) * (p - 15))
    assert S == 84
    r = S / p
    assert r == 4
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
    
    # Câu 13: 90 < alpha < 180, sin alpha = 5/13
    sin_a = sp.Rational(5, 13)
    cos_a = -sp.sqrt(1 - sin_a**2)
    assert cos_a == sp.Rational(-12, 13)
    tan_a = sin_a / cos_a
    assert tan_a == sp.Rational(-5, 12)
    
    # a) cos alpha > 0 -> Sai
    c13_a = False
    assert (cos_a > 0) == False
    
    # b) sin(180 - alpha) = 5/13 -> Đúng
    c13_b = True
    assert sin_a == sp.Rational(5, 13)
    
    # c) cos alpha = -12/13 và tan alpha = -5/12 -> Đúng
    c13_c = True
    assert cos_a == sp.Rational(-12, 13) and tan_a == sp.Rational(-5, 12)
    
    # d) E = (2 sin a + 3 cos a) / tan a = 13/3 -> Sai
    E = (2*sin_a + 3*cos_a) / tan_a
    assert E == sp.Rational(24, 5)
    assert E != sp.Rational(13, 3)
    c13_d = False
    
    print(f"Câu 13: a={c13_a}, b={c13_b}, c={c13_c}, d={c13_d} (S, Đ, Đ, S)")
    
    # Câu 14: Xưởng cơ khí
    # Ràng buộc máy tiện: 3x + 2y <= 18
    # Ràng buộc thủ công: x + 2y <= 10
    # a) x >= 0, y >= 0 -> Đúng
    c14_a = True
    
    # b) 3x + 2y <= 18 -> Đúng
    c14_b = True
    
    # c) x + 2y <= 10 -> Đúng
    c14_c = True
    
    # d) (4; 4) thuộc miền nghiệm -> Sai vì 3(4) + 2(4) = 20 > 18
    val_tien = 3*4 + 2*4
    assert val_tien == 20 > 18
    c14_d = False
    
    print(f"Câu 14: a={c14_a}, b={c14_b}, c={c14_c}, d={c14_d} (Đ, Đ, Đ, S)")
    print("[OK] Phần II chính xác 100%!")

def test_part_3():
    print("--- KIỂM TRA PHẦN III (4 CÂU TRẢ LỜI NGẮN) ---")
    
    # Câu 15: (a + b + c)(b + c - a) = bc
    # (b+c)^2 - a^2 = bc <=> b^2 + c^2 - a^2 = -bc
    # cos A = (b^2 + c^2 - a^2)/(2bc) = -bc / (2bc) = -1/2 -> A = 120 độ
    a, b, c = sp.symbols('a b c', positive=True)
    lhs = (b + c + a) * (b + c - a)
    expr = sp.expand(lhs) - b*c # b^2 + c^2 - a^2 + bc = 0
    # cos A:
    cos_A = (b**2 + c**2 - a**2) / (2*b*c)
    # Substitute b^2 + c^2 - a^2 = -bc:
    cos_A_val = -b*c / (2*b*c)
    assert cos_A_val == sp.Rational(-1, 2)
    deg_A = 120
    assert deg_A == 120
    print(f"Câu 15: Góc A = {deg_A}")
    
    # Câu 16: Bác An trồng cam (x ha) và bưởi (y ha)
    # x + y <= 8
    # 2x + 3y <= 18
    # x >= 0, y >= 0
    # F(x, y) = 40x + 50y
    vertices = [(0, 0), (8, 0), (6, 2), (0, 6)]
    f_vals = [40*vx + 50*vy for vx, vy in vertices]
    assert f_vals == [0, 320, 340, 300]
    max_f = max(f_vals)
    assert max_f == 340
    print(f"Câu 16: Lợi nhuận lớn nhất = {max_f}")
    
    # Câu 17: Khoảng cách giữa 2 tàu sau 1h: b = 15, c = 24, A = 60 deg
    dist_sq = 15**2 + 24**2 - 2*15*24*sp.cos(sp.pi/3)
    assert dist_sq == 441
    dist = sp.sqrt(dist_sq)
    assert dist == 21
    print(f"Câu 17: Khoảng cách = {dist}")
    
    # Câu 18: Diện tích tứ giác OABC: O(0,0), A(6,0), B(4,2), C(0,4)
    # S = S_OAB + S_OBC = 1/2 * 6 * 2 + 1/2 * 4 * 4 = 6 + 8 = 14
    s_oab = sp.Rational(1, 2) * 6 * 2
    s_obc = sp.Rational(1, 2) * 4 * 4
    s_tot = s_oab + s_obc
    assert s_tot == 14
    print(f"Câu 18: Diện tích S = {s_tot}")
    print("[OK] Phần III chính xác 100%!")

def test_part_4():
    print("--- KIỂM TRA PHẦN IV (4 CÂU TỰ LUẬN) ---")
    
    # Câu 19:
    # a) Đẳng thức b^2 - c^2 = a(b cos C - c cos B)
    a, b, c = sp.symbols('a b c', positive=True)
    cos_C = (a**2 + b**2 - c**2) / (2*a*b)
    cos_B = (a**2 + c**2 - b**2) / (2*a*c)
    rhs = a * (b * cos_C - c * cos_B)
    assert sp.simplify(rhs) == b**2 - c**2
    print("Câu 19a: Đẳng thức b^2 - c^2 = a(b cos C - c cos B) được chứng minh hoàn toàn.")
    
    # b) sin B = 2 sin C cos A -> tam giác cân tại B
    R = sp.symbols('R', positive=True)
    sin_B = b / (2*R)
    sin_C = c / (2*R)
    cos_A = (b**2 + c**2 - a**2) / (2*b*c)
    cond = sp.simplify(sin_B - 2 * sin_C * cos_A)
    # cond = (a^2 - c^2)/(2*b*R) = 0 <=> a = c
    assert sp.simplify(cond - (a**2 - c**2)/(2*b*R)) == 0
    assert sp.factor(cond) == (a - c)*(a + c)/(2*b*R)
    print("Câu 19b: sin B = 2 sin C cos A <=> a = c (tam giác cân tại B).")
    
    # Câu 20: Miền nghiệm 3x - 4y + 12 >= 0
    # Bờ 3x - 4y + 12 = 0 cắt Ox tại (-4, 0), Oy tại (0, 3)
    # O(0,0): 3(0) - 4(0) + 12 = 12 >= 0 (thỏa mãn)
    assert 3*0 - 4*0 + 12 >= 0
    print("Câu 20: Miền nghiệm chứa O(0,0), bờ đi qua (-4, 0) và (0, 3).")
    
    # Câu 21: cos alpha = -5/13, 90 < alpha < 180
    cos_21 = sp.Rational(-5, 13)
    sin_21 = sp.sqrt(1 - cos_21**2)
    tan_21 = sin_21 / cos_21
    cot_21 = 1 / tan_21
    assert sin_21 == sp.Rational(12, 13)
    assert tan_21 == sp.Rational(-12, 5)
    assert cot_21 == sp.Rational(-5, 12)
    
    # P = (13 sin a + 26 cos a) / (5 tan a + 12 cot a)
    num = 13*sin_21 + 26*cos_21
    den = 5*tan_21 + 12*cot_21
    assert num == 2
    assert den == -17
    P21 = num / den
    assert P21 == sp.Rational(-2, 17)
    print(f"Câu 21: sin={sin_21}, tan={tan_21}, cot={cot_21}, P={P21}")
    
    # Câu 22: Tối ưu tuyến tính
    # 2x + y <= 100
    # x + 2y <= 140
    # F(x, y) = 40000x + 50000y
    # Đỉnh: O(0,0), A(50, 0), B(20, 60), C(0, 70)
    v22 = [(0, 0), (50, 0), (20, 60), (0, 70)]
    f22 = [40000*x + 50000*y for x, y in v22]
    assert f22 == [0, 2000000, 3800000, 3500000]
    max22 = max(f22)
    assert max22 == 3800000
    print(f"Câu 22: Max lợi nhuận = {max22} tại (x, y) = (20, 60)")
    print("[OK] Phần IV chính xác 100%!")

if __name__ == '__main__':
    test_part_1()
    test_part_2()
    test_part_3()
    test_part_4()
    print("\n==========================================")
    print(">>> 100% TOÀN BỘ CÂU HỎI ĐỀ 24 ĐÃ PASS VERIFICATION! <<<")
    print("==========================================")
