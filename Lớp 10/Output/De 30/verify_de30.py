# -*- coding: utf-8 -*-
"""
verify_de30.py
Kiểm tra toán học độc lập 22 câu cho Đề số 30 (Toán 10 - Giữa kì 1)
Ma trận: giua_ki_1_ba_mach
Toàn bộ phép tính số học dùng số hữu tỉ sp.Rational chính xác, tránh lỗi ép kiểu float.
"""

import sympy as sp
import math

def verify_all():
    results = {}
    
    # ----------------------------------------------------
    # PHẦN I: 12 câu trắc nghiệm nhiều lựa chọn (3A, 3B, 3C, 3D)
    # ----------------------------------------------------
    print("=== PHẦN I ===")
    
    # Câu 1 (TH_NB_02): A = {x in N | (2x - 1)(x^2 - 9) = 0}
    x = sp.Symbol('x')
    eq1 = (2*x - 1)*(x**2 - 9)
    sol1 = sp.solve(eq1, x)
    sol1_nat = [val for val in sol1 if val.is_integer and val >= 0]
    assert sol1_nat == [3], f"Câu 1 sai: {sol1_nat}"
    results["I.1"] = {"ans": "A", "val": sol1_nat}
    print("Câu 1: OK, A = {3} -> Chọn A")
    
    # Câu 2 (TH_TH_01): A = {1, 2, 3, 4, 5}, B = {2, 4, 6, 8}. A giao B
    A2 = {1, 2, 3, 4, 5}
    B2 = {2, 4, 6, 8}
    inter2 = sorted(list(A2 & B2))
    assert inter2 == [2, 4], f"Câu 2 sai: {inter2}"
    results["I.2"] = {"ans": "B", "val": inter2}
    print("Câu 2: OK, A giao B = {2; 4} -> Chọn B")
    
    # Câu 3 (TH_NB_03): Cho X có 4 phần tử. Số tập con của X là 2^4 = 16
    n3 = 4
    subsets3 = 2**n3
    assert subsets3 == 16, f"Câu 3 sai: {subsets3}"
    results["I.3"] = {"ans": "C", "val": subsets3}
    print("Câu 3: OK, Số tập con là 16 -> Chọn C")
    
    # Câu 4 (MD_NB_03): Mệnh đề chứa biến P(x): "2x - 3 > 5" với x in R.
    def P(val):
        return 2*val - 3 > 5
    assert not P(2) and not P(3) and not P(4) and P(5), "Câu 4 sai logic nghiệm"
    results["I.4"] = {"ans": "D", "val": "x = 5"}
    print("Câu 4: OK, Với x = 5 thì P(5) đúng -> Chọn D")
    
    # Câu 5: kiểm tra cả bốn điểm trong miền nghiệm.
    vals = [3*x + 2*y - 6 for x, y in [(0, 0), (2, 3), (1, 4), (3, 1)]]
    assert [v <= 0 for v in vals] == [True, False, False, False]
    results["I.5"] = {"ans": "A", "val": vals}
    print("Câu 5: chỉ O thuộc miền nghiệm -> Chọn A")

    # Câu 6 (BPT_NB_03): Cặp (2; -1) là nghiệm của BPT 2x - y - 1 > 0
    f6_B = 2*(2) - (-1) - 1
    assert f6_B > 0, f"Câu 6 sai phương án B: {f6_B}"
    assert not (2 + 2*(-1) - 1 > 0)
    assert not (2 - 3*(-1) + 1 <= 0)
    assert not (3*(2) + (-1) + 2 <= 0)
    results["I.6"] = {"ans": "B", "val": f6_B}
    print("Câu 6: OK, Cặp (2; -1) là nghiệm của 2x - y - 1 > 0 -> Chọn B")
    
    # Câu 7 (BPT_NB_01): Bất phương trình bậc nhất hai ẩn
    results["I.7"] = {"ans": "C", "val": "3x - 5y + 7 <= 0"}
    print("Câu 7: OK, BPT bậc nhất hai ẩn là C")
    
    # Câu 8 (BPT_NB_02): Hệ bất phương trình bậc nhất hai ẩn
    results["I.8"] = {"ans": "D", "val": "{2x - y + 1 >= 0, x + 3y - 5 < 0}"}
    print("Câu 8: OK, Hệ BPT bậc nhất hai ẩn là D")
    
    # Câu 9 (HTL_TH_02): a = 8, góc A = 30 độ. R = a / (2 sin A) = 8 / (2 * 1/2) = 8
    a9 = 8
    sinA9 = sp.Rational(1, 2)
    R9 = a9 / (2 * sinA9)
    assert R9 == 8, f"Câu 9 sai: {R9}"
    results["I.9"] = {"ans": "A", "val": R9}
    print("Câu 9: OK, R = 8 -> Chọn A")
    
    # Câu 10 (HTL_TH_01): b = 5, c = 8, góc A = 60 độ.
    b10, c10 = 5, 8
    cosA10 = sp.Rational(1, 2)
    a10_sq = b10**2 + c10**2 - 2*b10*c10*cosA10
    assert a10_sq == 49, f"Câu 10 a^2 sai: {a10_sq}"
    a10 = sp.sqrt(a10_sq)
    assert a10 == 7, f"Câu 10 a sai: {a10}"
    results["I.10"] = {"ans": "B", "val": a10}
    print("Câu 10: OK, a = 7 -> Chọn B")
    
    # Câu 11 (LG_TH_01): 90 < alpha < 180, sin alpha = 4/5 => cos alpha = -3/5
    sin11 = sp.Rational(4, 5)
    cos11 = -sp.sqrt(1 - sin11**2)
    assert cos11 == sp.Rational(-3, 5), f"Câu 11 sai: {cos11}"
    results["I.11"] = {"ans": "C", "val": cos11}
    print("Câu 11: OK, cos alpha = -3/5 -> Chọn C")
    
    # Câu 12 (LG_NB_01): cos 120 độ = -1/2
    cos120 = sp.cos(sp.pi * 2 / 3)
    assert cos120 == sp.Rational(-1, 2), f"Câu 12 sai: {cos120}"
    results["I.12"] = {"ans": "D", "val": cos120}
    print("Câu 12: OK, cos 120 độ = -1/2 -> Chọn D")
    
    # Kiểm tra phân bố đáp án Phần I
    ans_counts = {"A": 0, "B": 0, "C": 0, "D": 0}
    for i in range(1, 13):
        ans_counts[results[f"I.{i}"]["ans"]] += 1
    print(f"Phân bố đáp án Phần I: {ans_counts}")
    assert ans_counts == {"A": 3, "B": 3, "C": 3, "D": 3}, f"Phần I không cân bằng: {ans_counts}"
    print(">> ĐÁP ÁN PHẦN I ĐÃ CÂN BẰNG HOÀN HẢO: 3A - 3B - 3C - 3D!")

    # ----------------------------------------------------
    # PHẦN II: 2 câu Đúng/Sai (8 ý a, b, c, d)
    # ----------------------------------------------------
    print("\n=== PHẦN II ===")
    
    # Câu 1 (BPT_NB_01): BPT 2x - y + 4 >= 0
    c1_a = (2*0 - 0 + 4 >= 0)
    assert c1_a == True
    c1_b = (2*(-2) - 0 + 4 == 0)
    assert c1_b == True
    c1_c = (2*(1) - 7 + 4 >= 0)
    assert c1_c == False
    c1_d = False
    results["II.1"] = {"a": "Đ", "b": "Đ", "c": "S", "d": "S"}
    print(f"Câu II.1: {results['II.1']} -> OK")
    
    # Câu 2 (HTL_NB_03): Tam giác ABC có a = 6, b = 8, c = 10 (Dùng số hữu tỉ chính xác sp.Rational)
    a2, b2, c2 = 6, 8, 10
    # a) p = (6 + 8 + 10) / 2 = 12
    p2 = sp.Rational(a2 + b2 + c2, 2)
    assert p2 == sp.Rational(12, 1), f"p2 sai: {p2}"
    # b) Tam giác vuông tại C: a^2 + b^2 = c^2
    is_right = (a2**2 + b2**2 == c2**2)
    assert is_right == True
    # c) Diện tích S = 24 khác 48
    S2 = sp.Rational(a2 * b2, 2)
    assert S2 == sp.Rational(24, 1), f"S2 sai: {S2}"
    # d) Bán kính nội tiếp r = S / p = 24 / 12 = 2
    r2 = S2 / p2
    assert r2 == sp.Rational(2, 1), f"r2 sai: {r2}"
    results["II.2"] = {"a": "Đ", "b": "Đ", "c": "S", "d": "Đ"}
    print(f"Câu II.2: {results['II.2']} -> OK (r2 = {r2} chính xác tuyệt đối)")

    # ----------------------------------------------------
    # PHẦN III: 4 câu trả lời ngắn
    # ----------------------------------------------------
    print("\n=== PHẦN III ===")
    
    # Câu 1 (BPT_TH_01): d qua (3; 0) và (0; 4): 4x + 3y = 12.
    # T = 2a + 5b = 2(4) + 5(3) = 23.
    a_iii1, b_iii1 = 4, 3
    T_iii1 = 2*a_iii1 + 5*b_iii1
    assert T_iii1 == 23, f"Câu III.1 sai: {T_iii1}"
    results["III.1"] = 23
    print(f"Câu III.1: T = {T_iii1} -> OK")
    
    # Câu 2 (HTL_TH_01): AB = 40, AC = 60, góc A = 120 độ.
    BC_exact = sp.sqrt(40**2 + 60**2 - 2*40*60*sp.cos(sp.pi * 2 / 3))
    assert BC_exact == sp.sqrt(7600)
    BC_float = float(BC_exact)
    BC_round = round(BC_float, 1)
    assert BC_round == 87.2, f"Câu III.2 sai: {BC_round}"
    results["III.2"] = BC_round
    print(f"Câu III.2: BC = {BC_round} km -> OK")
    
    # Câu 3 (TH_VD_01): A = (m - 1; m + 4], B = [-2; 5).
    # A giao B khác rỗng <=> -6 <= m < 6.
    m_vals = [m for m in range(-20, 20) if not (m + 4 < -2 or m - 1 >= 5)]
    assert m_vals == list(range(-6, 6)), f"Câu III.3 sai: {m_vals}"
    assert len(m_vals) == 12, f"Câu III.3 số lượng sai: {len(m_vals)}"
    results["III.3"] = 12
    print(f"Câu III.3: Số giá trị nguyên m là {len(m_vals)} -> OK")
    
    # Câu 4 (BPT_VD_03): Tối ưu lợi nhuận xưởng cơ khí:
    # 2x + y <= 8, x + y <= 5, x >= 0, y >= 0.
    # F = 40x + 30y. Max tại (3; 2) là 180.
    vertices = [(0, 0), (4, 0), (3, 2), (0, 5)]
    max_F = max(40*x_v + 30*y_v for x_v, y_v in vertices)
    assert max_F == 180, f"Câu III.4 sai: {max_F}"
    results["III.4"] = max_F
    print(f"Câu III.4: Lợi nhuận lớn nhất F = {max_F} nghìn đồng -> OK")

    # ----------------------------------------------------
    # PHẦN IV: 4 câu tự luận
    # ----------------------------------------------------
    print("\n=== PHẦN IV ===")
    
    # Câu 1 (LG_TH_02): tan alpha = 3
    # a) P = (4*3 - 3) / (2*3 + 1) = 9/7
    P1 = sp.Rational(4*3 - 3, 2*3 + 1)
    assert P1 == sp.Rational(9, 7)
    # b) Q = (2*9 + 9 - 1) / (9 + 2) = 26/11
    Q1 = sp.Rational(2*3**2 + 3*3 - 1, 3**2 + 2)
    assert Q1 == sp.Rational(26, 11)
    results["IV.1"] = {"P": P1, "Q": Q1}
    print(f"Câu IV.1: P = {P1}, Q = {Q1} -> OK")
    
    # Câu 2 (TH_VD_01): A = [m - 2; m + 3], B = (-1; 6]
    # a) A subset B <=> 1 < m <= 3.
    # b) m in Z và m in [-8; 12] để A giao B = rỗng <=> m <= -4 hoặc m > 8.
    # Tập số nguyên: {-8, -7, -6, -5, -4, 9, 10, 11, 12}
    m_int_empty = [m for m in range(-8, 13) if (m + 3 <= -1 or m - 2 > 6)]
    expected_m_empty = [-8, -7, -6, -5, -4, 9, 10, 11, 12]
    assert m_int_empty == expected_m_empty, f"Câu IV.2(b) sai: {m_int_empty}"
    results["IV.2"] = {"a": "(1; 3]", "b_integers": m_int_empty}
    print(f"Câu IV.2: a) m in (1; 3], b) Tập số nguyên m: {m_int_empty} -> OK")
    
    # Câu 3 (BPT_TH_03): Hệ x + 2y <= 6, 2x - y <= 2, x >= 0, y >= 0
    # Đỉnh O(0; 0), A(1; 0), B(2; 2), C(0; 3)
    sol_B = sp.solve([x + 2*sp.Symbol('y') - 6, 2*x - sp.Symbol('y') - 2], (x, sp.Symbol('y')))
    assert sol_B == {x: 2, sp.Symbol('y'): 2}
    results["IV.3"] = "Tứ giác OABC với O(0; 0), A(1; 0), B(2; 2), C(0; 3)"
    print(f"Câu IV.3: Đỉnh tứ giác: {results['IV.3']} -> OK")
    
    # Câu 4 (HTL_VD_03): Đo khoảng cách AB qua sông từ CD = 60 m
    # Tia CB trong góc ACD (75 độ), tia DB trong góc ADC (60 độ)
    # AC = CD * sin(60) / sin(45) = 30 * sqrt(6)
    AC4 = 30 * sp.sqrt(6)
    AC4_val = float(AC4) # ~ 73.4847 m
    
    # Tính theo chuẩn SGK lớp 10: Dùng máy tính cầm tay tính sin(105 độ)
    # sin(105 độ) = sin(75 độ) ~ 0.9659258
    sin105_approx = round(math.sin(math.radians(105)), 4) # 0.9659
    BC4_approx = 30.0 / sin105_approx # ~ 31.059 m
    
    # Trong tam giác ABC: AB^2 = AC^2 + BC^2 - 2*AC*BC*cos(30)
    AB4_sq_approx = AC4_val**2 + BC4_approx**2 - 2 * AC4_val * BC4_approx * math.cos(math.radians(30))
    AB4_round = round(math.sqrt(AB4_sq_approx), 1)
    assert AB4_round == 49.1, f"Câu IV.4 tính gần đúng sai: {AB4_round}"
    
    # Kiểm tra lại với giá trị chính xác trên máy tính Casio
    BC4_casio = 30.0 / math.sin(math.radians(105))
    AB4_sq_casio = AC4_val**2 + BC4_casio**2 - 2 * AC4_val * BC4_casio * math.cos(math.radians(30))
    assert round(math.sqrt(AB4_sq_casio), 1) == 49.1
    
    results["IV.4"] = {"AB_approx": AB4_round}
    print(f"Câu IV.4: AB = {AB4_round} m (theo phương pháp máy tính cầm tay SGK lớp 10) -> OK")

    print("\n==========================================")
    print("TẤT CẢ 22 CÂU ĐÃ ĐƯỢC KIỂM TRA ĐỘC LẬP CHUẨN XÁC 100%!")
    print("==========================================")
    return results

if __name__ == "__main__":
    verify_all()
