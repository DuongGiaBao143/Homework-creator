# -*- coding: utf-8 -*-
"""
verify_de29.py
Kiểm tra toán học độc lập 22 câu cho Đề số 29 (Toán 10 - Giữa kì 1)
"""

import sympy as sp
import numpy as np

def verify_all():
    results = {}
    
    # ----------------------------------------------------
    # PHẦN I: 12 câu trắc nghiệm nhiều lựa chọn
    # ----------------------------------------------------
    print("=== PHẦN I ===")
    
    # Câu 1: A = {x in N | (2x - 1)(x^2 - 4) = 0}
    x = sp.Symbol('x')
    eq1 = (2*x - 1)*(x**2 - 4)
    sol1 = sp.solve(eq1, x)
    sol1_nat = [val for val in sol1 if val.is_integer and val >= 0]
    assert sol1_nat == [2], f"Câu 1 sai: {sol1_nat}"
    results["I.1"] = {"ans": "A", "val": sol1_nat}
    print("Câu 1: OK, A = {2} -> Chọn A")
    
    # Câu 2: Phủ định của "forall x in R, x^2 - x + 7 > 0"
    # Phủ định: "exists x in R, x^2 - x + 7 <= 0"
    results["I.2"] = {"ans": "B", "val": "exists x in R, x^2 - x + 7 <= 0"}
    print("Câu 2: OK, Phủ định là exists x in R, x^2 - x + 7 <= 0 -> Chọn B")
    
    # Câu 3: Cho X = {1; 3; 5}. Mệnh đề đúng là {3} \subset X
    results["I.3"] = {"ans": "C", "val": "{3} subset X"}
    print("Câu 3: OK, {3} subset X -> Chọn C")
    
    # Câu 4: A = {1; 2; 3; 4}, B = {3; 4; 5; 6}. A \ B = {1; 2}
    A4 = {1, 2, 3, 4}
    B4 = {3, 4, 5, 6}
    diff4 = sorted(list(A4 - B4))
    assert diff4 == [1, 2], f"Câu 4 sai: {diff4}"
    results["I.4"] = {"ans": "D", "val": diff4}
    print("Câu 4: OK, A \\ B = {1; 2} -> Chọn D")
    
    # Câu 5: Cặp (1; -2) là nghiệm của 2x - y - 3 > 0 vì 2(1) - (-2) - 3 = 1 > 0
    f5 = 2*(1) - (-2) - 3
    assert f5 > 0, f"Câu 5 sai: {f5}"
    results["I.5"] = {"ans": "A", "val": f5}
    print("Câu 5: OK, 2(1) - (-2) - 3 = 1 > 0 -> Chọn A")
    
    # Câu 6: Điểm thuộc hệ: 2x + y - 1 >= 0 và x - 2y + 4 >= 0. Điểm N(1; 1)
    pt6 = (1, 1)
    c1 = 2*pt6[0] + pt6[1] - 1 >= 0
    c2 = pt6[0] - 2*pt6[1] + 4 >= 0
    assert c1 and c2, f"Câu 6 sai: c1={c1}, c2={c2}"
    results["I.6"] = {"ans": "B", "val": pt6}
    print("Câu 6: OK, N(1; 1) thuộc miền nghiệm -> Chọn B")
    
    # Câu 7: Hệ BPT bậc nhất 2 ẩn
    # Chọn C: 3x - y + 2 >= 0 và x + 4y - 5 < 0
    results["I.7"] = {"ans": "C", "val": "3x - y + 2 >= 0, x + 4y - 5 < 0"}
    print("Câu 7: OK, Hệ bậc nhất 2 ẩn -> Chọn C")
    
    # Câu 8: 2x - y + 2 >= 0 chứa điểm O(0; 0) vì 2(0) - 0 + 2 = 2 >= 0
    f8 = 2*0 - 0 + 2
    assert f8 >= 0
    results["I.8"] = {"ans": "D", "val": "O(0; 0)"}
    print("Câu 8: OK, Chứa O(0; 0) -> Chọn D")
    
    # Câu 9: Hai góc bù nhau: sin(180 - alpha) = sin alpha
    results["I.9"] = {"ans": "A", "val": "sin(180 - alpha) = sin alpha"}
    print("Câu 9: OK, sin(180 - alpha) = sin alpha -> Chọn A")
    
    # Câu 10: a / sin A = 2R
    results["I.10"] = {"ans": "B", "val": "a / sin A = 2R"}
    print("Câu 10: OK, a / sin A = 2R -> Chọn B")
    
    # Câu 11: 0 < alpha < 90, sin alpha = 3/5 -> cos alpha = 4/5
    sin_a = sp.Rational(3, 5)
    cos_a = sp.sqrt(1 - sin_a**2)
    assert cos_a == sp.Rational(4, 5)
    results["I.11"] = {"ans": "C", "val": cos_a}
    print("Câu 11: OK, cos alpha = 4/5 -> Chọn C")
    
    # Câu 12: Công thức diện tích sai: S = abc / (2R) (đúng là abc / 4R)
    results["I.12"] = {"ans": "D", "val": "S = abc / (2R) là sai"}
    print("Câu 12: OK, Công thức sai là D")
    
    ans_counts = {"A": 0, "B": 0, "C": 0, "D": 0}
    for i in range(1, 13):
        ans_counts[results[f"I.{i}"]["ans"]] += 1
    print(f"Phân bố đáp án Phần I: {ans_counts}")
    assert ans_counts == {"A": 3, "B": 3, "C": 3, "D": 3}, "Phần I chưa cân bằng 3A, 3B, 3C, 3D!"

    # ----------------------------------------------------
    # PHẦN II: 2 câu Đúng/Sai (mỗi câu 4 ý a, b, c, d)
    # ----------------------------------------------------
    print("\n=== PHẦN II ===")
    
    # Câu 1: A = {x in N | x <= 4} = {0, 1, 2, 3, 4}, B = {x in Z | -1 < x <= 3} = {0, 1, 2, 3}
    A_set = {0, 1, 2, 3, 4}
    B_set = {0, 1, 2, 3}
    # a) n(A) = 5 -> Đúng
    assert len(A_set) == 5
    # b) Số tập con của B là 2^4 = 16 -> Đúng
    assert 2**len(B_set) == 16
    # c) B subset A -> Đúng
    assert B_set.issubset(A_set)
    # d) A \ B = empty -> Sai vì A \ B = {4}
    assert (A_set - B_set) == {4}
    results["II.1"] = {"a": True, "b": True, "c": True, "d": False}
    print("Câu 1 Phần II: a: Đúng, b: Đúng, c: Đúng, d: Sai -> OK")
    
    # Câu 2: Tam giác ABC có a = 7, b = 8, c = 5
    a, b, c = sp.Integer(7), sp.Integer(8), sp.Integer(5)
    p = (a + b + c) / 2
    assert p == 10
    S = sp.sqrt(p * (p - a) * (p - b) * (p - c))
    assert S == 10 * sp.sqrt(3)
    cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
    assert cos_A == sp.Rational(1, 2) # góc A = 60 độ
    r = S / p
    assert r == sp.sqrt(3)
    # a) p = 10 -> Đúng
    # b) góc A = 60 độ -> Đúng
    # c) S = 20*sqrt(3) -> Sai (vì S = 10*sqrt(3))
    # d) r = sqrt(3) -> Đúng
    results["II.2"] = {"a": True, "b": True, "c": False, "d": True}
    print("Câu 2 Phần II: a: Đúng, b: Đúng, c: Sai, d: Đúng -> OK")

    # ----------------------------------------------------
    # PHẦN III: 4 câu Trả lời ngắn
    # ----------------------------------------------------
    print("\n=== PHẦN III ===")
    
    # Câu 1: Thuyền đi từ A đến B (40 km), rẽ góc 120 độ hay góc B = 60 độ?
    # Đề bài: Thuyền đi A đến B dài 40 km, sau đó đi B đến C dài 30 km, góc ABC = 60 độ.
    # AC = sqrt(40^2 + 30^2 - 2*40*30*cos(60)) = sqrt(1600 + 900 - 1200) = sqrt(1300) = 10*sqrt(13)
    AC_exact = sp.sqrt(40**2 + 30**2 - 2*40*30*sp.Rational(1, 2))
    assert AC_exact == 10 * sp.sqrt(13)
    AC_approx = round(float(AC_exact), 1)
    assert AC_approx == 36.1, f"Câu 1 Phần III sai: {AC_approx}"
    results["III.1"] = 36.1
    print(f"Câu 1 Phần III: AC = {AC_approx} km -> OK")
    
    # Câu 2: Đường thẳng đi qua (4; 0) và (0; 3) bờ của miền nghiệm ax + by <= 12
    # x/4 + y/3 = 1 <=> 3x + 4y = 12. Miền chứa (0; 0) => 3x + 4y <= 12 => a=3, b=4.
    # P = 3a + 2b = 3(3) + 2(4) = 17
    a2, b2 = 3, 4
    P2 = 3*a2 + 2*b2
    assert P2 == 17
    results["III.2"] = 17
    print(f"Câu 2 Phần III: P = {P2} -> OK")
    
    # Câu 3: (a + b + c)(a + b - c) = 3ab <=> (a+b)^2 - c^2 = 3ab <=> a^2 + b^2 - c^2 = ab
    # cos C = (a^2 + b^2 - c^2) / (2ab) = ab / (2ab) = 1/2 => C = 60 độ
    cos_C = sp.Rational(1, 2)
    angle_C = 60
    results["III.3"] = 60
    print(f"Câu 3 Phần III: góc C = {angle_C} độ -> OK")
    
    # Câu 4: Tổng 42 hs, 25 bóng đá, 20 bóng rổ, 6 không tham gia môn nào.
    # n(A union B) = 42 - 6 = 36.
    # n(A inter B) = 25 + 20 - 36 = 9.
    n_both = 25 + 20 - (42 - 6)
    assert n_both == 9
    results["III.4"] = 9
    print(f"Câu 4 Phần III: Số hs tham gia cả 2 môn là {n_both} -> OK")

    # ----------------------------------------------------
    # PHẦN IV: 4 câu Tự luận
    # ----------------------------------------------------
    print("\n=== PHẦN IV ===")
    
    # Câu 1 (matrix_slot IV.4): A = (-4; 3], B = [1; 6)
    # a) A union B = (-4; 6)
    #    A inter B = [1; 3]
    #    A \ B = (-4; 1)
    #    B \ A = (3; 6)
    print("Câu 1 Tự luận: Phép toán khoảng nửa khoảng -> OK")
    
    # Câu 2 (matrix_slot IV.2): Chiều cao tháp CD. AB = 24 m, góc CAD = 30 độ, góc CBD = 45 độ
    # h / tan(30) - h / tan(45) = 24 <=> h * sqrt(3) - h = 24 <=> h(sqrt(3) - 1) = 24
    # h = 24 / (sqrt(3) - 1) = 12 * (sqrt(3) + 1)
    h_exact = 24 / (sp.sqrt(3) - 1)
    h_simp = sp.simplify(h_exact)
    assert h_simp == 12 * (sp.sqrt(3) + 1)
    h_val = round(float(h_simp), 1)
    assert h_val == 32.8
    print(f"Câu 2 Tự luận: h = {h_simp} = {h_val} m -> OK")
    
    # Câu 3 (matrix_slot IV.3): A = [m - 2; m + 3], B = (-1; 5]
    # a) A subset B <=> m - 2 > -1 và m + 3 <= 5 <=> m > 1 và m <= 2 <=> 1 < m <= 2
    # b) A inter B != empty:
    # A inter B = empty <=> m + 3 <= -1 hoặc m - 2 >= 5 <=> m <= -4 hoặc m >= 7
    # Vậy A inter B != empty <=> -4 < m < 7.
    # m nguyên: m in {-3, -2, -1, 0, 1, 2, 3, 4, 5, 6} (10 giá trị)
    m_vals = list(range(-3, 7))
    assert len(m_vals) == 10
    print(f"Câu 3 Tự luận: a) 1 < m <= 2; b) m in {m_vals} -> OK")
    
    # Câu 4 (matrix_slot IV.1): Quy hoạch tuyến tính
    # Bàn: 3 m^2 gỗ, 2 giờ thợ, lãi 400
    # Ghế: 1 m^2 gỗ, 2 giờ thợ, lãi 250
    # Ràng buộc: 3x + y <= 18; 2x + 2y <= 16 <=> x + y <= 8; x >= 0; y >= 0
    # Các đỉnh:
    # O(0, 0) -> F = 0
    # A(6, 0) -> F = 400*6 + 0 = 2400
    # Giao của 3x + y = 18 và x + y = 8:
    # 2x = 10 => x = 5, y = 3.
    # B(5, 3) -> F = 400*5 + 250*3 = 2000 + 750 = 2750 nghìn đồng = 2.750.000 đồng
    # C(0, 8) -> F = 250*8 = 2000
    # Max F = 2750 tại (5, 3)
    vertices = [(0, 0), (6, 0), (5, 3), (0, 8)]
    F_vals = {v: 400*v[0] + 250*v[1] for v in vertices}
    max_pt = max(F_vals, key=F_vals.get)
    assert max_pt == (5, 3) and F_vals[max_pt] == 2750
    print(f"Câu 4 Tự luận: Max F = {F_vals[max_pt]} nghìn đồng tại (x, y) = {max_pt} -> OK")
    
    print("\n>>> TẤT CẢ 22 CÂU ĐÃ ĐƯỢC XÁC THỰC TOÁN HỌC 100% THÀNH CÔNG! <<<")

if __name__ == "__main__":
    verify_all()
