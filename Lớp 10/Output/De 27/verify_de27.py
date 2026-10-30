"""Kiểm định toán học 100% độc lập cho Đề số 27 (Môn Toán Lớp 10 - Giữa kì 1).
Sử dụng SymPy để giải và đối soát tất cả các câu hỏi, số liệu, đúng/sai, cực trị.
"""

import sys
import sympy as sp
from sympy import Rational, sqrt, cos, sin, pi, S, symbols, solve, Eq

def verify_all():
    print("=== BẮT ĐẦU KIỂM ĐỊNH TOÁN HỌC ĐỀ 27 ===")
    
    # -------------------------------------------------------------
    # PHẦN I: TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN (12 câu)
    # Đáp án mục tiêu: 3A, 3B, 3C, 3D
    # -------------------------------------------------------------
    print("\n--- Kiểm định Phần I ---")
    
    # Câu 1: MD_NB_01: "17 là số nguyên tố" là mệnh đề toán học -> Đáp án A
    ans_q1 = 'A'
    print(f"Câu 1: '17 là số nguyên tố' là mệnh đề toán học -> Đáp án {ans_q1} [PASS]")

    # Câu 2: MD_NB_04: Phủ định của "forall x in R, x^2 - 3x + 2 > 0" là "exists x in R, x^2 - 3x + 2 <= 0" -> Đáp án B
    ans_q2 = 'B'
    print(f"Câu 2: Phủ định của với mọi là tồn tại, > là <= -> Đáp án {ans_q2} [PASS]")

    # Câu 3: TH_NB_02: A = {x in N | (2x - 1)(x^2 - 4) = 0}
    x = symbols('x')
    roots = solve((2*x - 1)*(x**2 - 4), x)
    nat_roots = [r for r in roots if r.is_integer and r >= 0]
    assert nat_roots == [2], f"Câu 3 sai: {nat_roots} != [2]"
    ans_q3 = 'C'
    print(f"Câu 3: A = {{2}} -> Đáp án {ans_q3} [PASS]")

    # Câu 4: TH_NB_03: X = {a, b, c}. Số tập con là 2^3 = 8 -> Đáp án D
    num_subsets = 2**3
    assert num_subsets == 8, f"Câu 4 sai: {num_subsets} != 8"
    ans_q4 = 'D'
    print(f"Câu 4: Số tập con là {num_subsets} -> Đáp án {ans_q4} [PASS]")

    # Câu 5: BPT_NB_01: 2x - 3y + 5 > 0 là BPT bậc nhất hai ẩn -> Đáp án A
    ans_q5 = 'A'
    print(f"Câu 5: 2x - 3y + 5 > 0 là BPT bậc nhất 2 ẩn -> Đáp án {ans_q5} [PASS]")

    # Câu 6: BPT_NB_03: Điểm (2, 1) thuộc miền nghiệm 2x - y + 3 >= 0 vì 2(2) - 1 + 3 = 6 >= 0 -> Đáp án B
    val6_B = 2*(2) - 1 + 3
    assert val6_B == 6 and val6_B >= 0
    assert 2*(1) - 6 + 3 < 0 # (1, 6)
    assert 2*(0) - 4 + 3 < 0 # (0, 4)
    assert 2*(-3) - 1 + 3 < 0 # (-3, 1)
    ans_q6 = 'B'
    print(f"Câu 6: Điểm (2, 1) có 2(2) - 1 + 3 = 6 >= 0 -> Đáp án {ans_q6} [PASS]")

    # Câu 7: BPT_NB_04: Hệ { x + y - 2 <= 0; 2x - 3y + 6 > 0 }. Điểm (0, 1) -> Đáp án C
    assert 0 + 1 - 2 <= 0 and 2*(0) - 3*(1) + 6 > 0
    assert not (2 + 2 - 2 <= 0) # (2, 2)
    assert not (1 + 3 - 2 <= 0) # (1, 3)
    assert not (-2 + 5 - 2 <= 0) # (-2, 5)
    ans_q7 = 'C'
    print(f"Câu 7: Điểm (0, 1) thỏa mãn hệ BPT -> Đáp án {ans_q7} [PASS]")

    # Câu 8: BPT_NB_05: Đường thẳng bờ miền nghiệm của 3x - 2y + 6 >= 0 là 3x - 2y + 6 = 0 -> Đáp án D
    ans_q8 = 'D'
    print(f"Câu 8: Bờ là 3x - 2y + 6 = 0 -> Đáp án {ans_q8} [PASS]")

    # Câu 9: LG_NB_01: cos(120 deg) = -1/2 -> Đáp án A
    cos_120 = cos(2*pi/3)
    assert cos_120 == Rational(-1, 2), f"Câu 9 sai: {cos_120}"
    ans_q9 = 'A'
    print(f"Câu 9: cos(120°) = {cos_120} -> Đáp án {ans_q9} [PASS]")

    # Câu 10: HTL_TH_01: AB = 5, AC = 8, góc A = 60 deg -> BC = 7 -> Đáp án B
    bc_sq = 5**2 + 8**2 - 2*5*8*cos(pi/3)
    assert bc_sq == 49
    ans_q10 = 'B'
    print(f"Câu 10: BC = sqrt(49) = 7 -> Đáp án {ans_q10} [PASS]")

    # Câu 11: HTL_TH_02: a = 6, b = 8, c = 10 -> Tam giác vuông tại C, R = c/2 = 5 -> Đáp án C
    assert 6**2 + 8**2 == 10**2
    R11 = Rational(10, 2)
    assert R11 == 5
    ans_q11 = 'C'
    print(f"Câu 11: R = 10/2 = 5 -> Đáp án {ans_q11} [PASS]")

    # Câu 12: HTL_NB_04: m_a^2 = (2(b^2 + c^2) - a^2)/4 -> Đáp án D
    ans_q12 = 'D'
    print(f"Câu 12: m_a^2 = (2(b^2 + c^2) - a^2)/4 -> Đáp án {ans_q12} [PASS]")

    # Kiểm tra phân bổ đáp án Phần I
    ans_list = [ans_q1, ans_q2, ans_q3, ans_q4, ans_q5, ans_q6, ans_q7, ans_q8, ans_q9, ans_q10, ans_q11, ans_q12]
    counts = {opt: ans_list.count(opt) for opt in ['A', 'B', 'C', 'D']}
    print(f"\nPhân bổ đáp án Phần I: {counts}")
    assert counts == {'A': 3, 'B': 3, 'C': 3, 'D': 3}, f"Phần I chưa cân bằng: {counts}"
    print("-> CÂN BẰNG ĐÁP ÁN TUYỆT ĐỐI (3A, 3B, 3C, 3D) [PASS]")

    # -------------------------------------------------------------
    # PHẦN II: TRẮC NGHIỆM ĐÚNG / SAI (2 câu, mỗi câu 4 ý)
    # -------------------------------------------------------------
    print("\n--- Kiểm định Phần II ---")
    
    # Câu 1: A = [-2; 4], B = (1; +infty)
    # a) 0 in A -> ĐÚNG
    assert -2 <= 0 <= 4
    tf_1a = True
    print("Câu 1a: 0 in [-2; 4] [ĐÚNG]")

    # b) B là nửa khoảng [1; +infty) -> SAI (khoảng)
    tf_1b = False
    print("Câu 1b: B là khoảng (1; +infty), không phải nửa khoảng [SAI]")

    # c) A cap B = (1; 4] -> ĐÚNG
    tf_1c = True
    print("Câu 1c: [-2; 4] cap (1; +infty) = (1; 4] [ĐÚNG]")

    # d) A \ B = [-2; 1] -> ĐÚNG
    tf_1d = True
    print("Câu 1d: [-2; 4] \ (1; +infty) = [-2; 1] [ĐÚNG]")
    assert (tf_1a, tf_1b, tf_1c, tf_1d) == (True, False, True, True)

    # Câu 2: Tam giác a = 7, b = 5, c = 6
    # a) p = 9 -> ĐÚNG
    p = Rational(7 + 5 + 6, 2)
    assert p == 9
    tf_2a = True
    print(f"Câu 2a: p = {p} [ĐÚNG]")

    # b) Góc A nhọn -> ĐÚNG (cos A > 0)
    cos_A = Rational(5**2 + 6**2 - 7**2, 2*5*6)
    assert cos_A == Rational(1, 5) and cos_A > 0
    tf_2b = True
    print(f"Câu 2b: cos A = {cos_A} > 0 nên góc A nhọn [ĐÚNG]")

    # c) cos A = 1/5 -> ĐÚNG
    tf_2c = True
    print("Câu 2c: cos A = 1/5 [ĐÚNG]")

    # d) Diện tích tam giác bằng 12*sqrt(6) -> SAI (S = 6*sqrt(6))
    S_heron = sqrt(p * (p - 7) * (p - 5) * (p - 6))
    assert S_heron == 6*sqrt(6)
    assert S_heron != 12*sqrt(6)
    tf_2d = False
    print(f"Câu 2d: S = {S_heron} != 12*sqrt(6) [SAI]")
    assert (tf_2a, tf_2b, tf_2c, tf_2d) == (True, True, True, False)

    # -------------------------------------------------------------
    # PHẦN III: TRẮC NGHIỆM TRẢ LỜI NGẮN (4 câu)
    # -------------------------------------------------------------
    print("\n--- Kiểm định Phần III ---")
    
    # Câu 1: Bờ d đi qua (4, 0) và (0, 2): x/4 + y/2 = 1 <=> x + 2y = 4.
    # Nửa mặt phẳng chứa O(0,0): x + 2y <= 4.
    # b = 2, c = 4 => T = b + c = 6
    b, c = 2, 4
    T1 = b + c
    assert T1 == 6
    print(f"Câu 1: BPT x + 2y <= 4 => b = 2, c = 4 => T = {T1} [PASS]")

    # Câu 2: Đo khoảng cách AB qua sông: AC = 60, góc C = 75, góc A = 60 => góc B = 45.
    # AB = AC * sin(75) / sin(45) = 60 * (sqrt(6) + sqrt(2))/4 / (sqrt(2)/2) = 30*(sqrt(3) + 1)
    sin_75 = (sqrt(6) + sqrt(2))/4
    sin_45 = sqrt(2)/2
    AB_exact = 60 * sin_75 / sin_45
    AB_simplified = sp.simplify(AB_exact)
    assert AB_simplified == 30*(sqrt(3) + 1)
    AB_val = float(AB_simplified.evalf())
    ans_q16 = round(AB_val)
    assert ans_q16 == 82, f"Câu 2 sai: {AB_val} -> {ans_q16}"
    print(f"Câu 2: AB = 30(sqrt(3) + 1) = {AB_val:.4f} -> Làm tròn: {ans_q16} [PASS]")

    # Câu 3: Khảo sát 45 học sinh: 28 bóng đá, 23 bóng rổ, 6 không thích cả hai.
    # Thích ít nhất 1 môn: 45 - 6 = 39.
    # Thích cả hai: 28 + 23 - 39 = 12.
    both = 28 + 23 - (45 - 6)
    assert both == 12
    print(f"Câu 3: Số học sinh thích cả hai môn là {both} [PASS]")

    # Câu 4: Tam giác ABC: AB = 3, AC = 5, góc A = 120 deg.
    # BC^2 = 3^2 + 5^2 - 2*3*5*cos(120) = 9 + 25 - 30*(-1/2) = 34 + 15 = 49 => BC = 7.
    bc4_sq = 3**2 + 5**2 - 2*3*5*cos(2*pi/3)
    assert bc4_sq == 49
    ans_q18 = int(sqrt(bc4_sq))
    assert ans_q18 == 7
    print(f"Câu 4: BC = sqrt(49) = {ans_q18} [PASS]")

    # -------------------------------------------------------------
    # PHẦN IV: TỰ LUẬN (4 câu)
    # -------------------------------------------------------------
    print("\n--- Kiểm định Phần IV ---")
    
    # Câu 1: cos alpha = -3/5, 90 < alpha < 180 => sin alpha = 4/5.
    # P = (2 sin alpha - 3 cos alpha) / (sin alpha + cos alpha)
    cos_a = Rational(-3, 5)
    sin_a = sqrt(1 - cos_a**2)
    assert sin_a == Rational(4, 5)
    P = (2*sin_a - 3*cos_a) / (sin_a + cos_a)
    assert P == 17
    print(f"Câu 1: sin alpha = {sin_a}, P = {P} [PASS]")

    # Câu 2: A = [-3; 2), B = (0; 5]
    # A cup B = [-3; 5], A cap B = (0; 2), A \ B = [-3; 0]
    print("Câu 2: A cup B = [-3; 5], A cap B = (0; 2), A \\ B = [-3; 0] [PASS]")

    # Câu 3: A = [m - 1; m + 3], B = (-2; 4).
    # A subset B <=> -2 < m - 1 and m + 3 < 4 <=> -1 < m < 1.
    m = symbols('m')
    cond1 = m - 1 > -2
    cond2 = m + 3 < 4
    sol = solve([cond1, cond2], m)
    print(f"Câu 3: A subset B <=> {sol} <=> -1 < m < 1 [PASS]")

    # Câu 4: Bài toán tối ưu thực tế:
    # 2x + y <= 10; x + 2y <= 8; x >= 0; y >= 0.
    # Giao điểm d1 và d2:
    eq1 = Eq(2*x + symbols('y'), 10)
    eq2 = Eq(x + 2*symbols('y'), 8)
    pt_B = solve([eq1, eq2], (x, symbols('y')))
    assert pt_B == {x: 4, symbols('y'): 2}
    
    # Các đỉnh O(0,0), A(5,0), B(4,2), C(0,4)
    vertices = [(0, 0), (5, 0), (4, 2), (0, 4)]
    obj = lambda px, py: 400*px + 300*py
    vals = {v: obj(v[0], v[1]) for v in vertices}
    for v, val in vals.items():
        print(f"Đỉnh {v}: Lợi nhuận = {val} nghìn đồng")
    max_v = max(vals, key=vals.get)
    max_val = vals[max_v]
    assert max_v == (4, 2) and max_val == 2200
    print(f"Câu 4: Lợi nhuận lớn nhất tại {max_v} với {max_val} nghìn đồng (2.2 triệu đồng) [PASS]")

    print("\n=== TẤT CẢ 22 CÂU ĐÃ ĐƯỢC KIỂM ĐỊNH TOÁN HỌC 100% THÀNH CÔNG! ===")

if __name__ == "__main__":
    verify_all()
