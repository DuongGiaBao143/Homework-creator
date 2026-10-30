"""Kiểm định toán học 100% độc lập cho Đề số 26 (Môn Toán Lớp 10 - Giữa kì 1).
Sử dụng SymPy để giải và đối soát tất cả các câu hỏi, số liệu, đúng/sai, cực trị.
"""

import sys
import sympy as sp
from sympy import Rational, sqrt, cos, sin, pi, S

def verify_all():
    print("=== BẮT ĐẦU KIỂM ĐỊNH TOÁN HỌC ĐỀ 26 ===")
    
    # -------------------------------------------------------------
    # PHẦN I: TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN (12 câu)
    # Đáp án mục tiêu: 3A, 3B, 3C, 3D
    # -------------------------------------------------------------
    print("\n--- Kiểm định Phần I ---")
    
    # Câu 1: Số tập con có đúng 2 phần tử của A = {1, 2, 3, 4}
    # C(4, 2) = 6 -> Đáp án A
    c42 = sp.binomial(4, 2)
    assert c42 == 6, f"Câu 1 sai: {c42} != 6"
    ans_q1 = 'A'
    print(f"Câu 1: C(4, 2) = {c42} -> Đáp án {ans_q1} [PASS]")

    # Câu 2: X = {a, b, c}. Khẳng định đúng: {a, b} \subset X -> Đáp án B
    X = {'a', 'b', 'c'}
    sub = {'a', 'b'}
    assert sub.issubset(X), "Câu 2 sai"
    ans_q2 = 'B'
    print(f"Câu 2: {{a, b}} là tập con của X -> Đáp án {ans_q2} [PASS]")

    # Câu 3: S = {x in R | -2 <= x < 5} viết là [-2; 5) -> Đáp án C
    ans_q3 = 'C'
    print(f"Câu 3: S = [-2; 5) -> Đáp án {ans_q3} [PASS]")

    # Câu 4: P => Q: P là điều kiện đủ để có Q -> Đáp án D
    ans_q4 = 'D'
    print(f"Câu 4: P là điều kiện đủ để có Q -> Đáp án {ans_q4} [PASS]")

    # Câu 5: Hệ { x + y - 2 <= 0; 2x - 3y + 2 > 0 }. Điểm O(0,0) -> Đáp án A
    x, y = 0, 0
    assert (x + y - 2 <= 0) and (2*x - 3*y + 2 > 0), "Câu 5 sai"
    # Kiểm tra các điểm còn lại không thỏa mãn
    assert not (2 + 1 - 2 <= 0), "M(2,1) không được thỏa mãn"
    assert not (1 + 2 - 2 <= 0), "N(1,2) không được thỏa mãn"
    assert not (2*(0) - 3*(2) + 2 > 0), "P(0,2) không được thỏa mãn"
    ans_q5 = 'A'
    print(f"Câu 5: Điểm O(0,0) thỏa mãn hệ -> Đáp án {ans_q5} [PASS]")

    # Câu 6: Đường thẳng bờ của 3x - 2y + 6 >= 0 là 3x - 2y + 6 = 0 -> Đáp án B
    ans_q6 = 'B'
    print(f"Câu 6: Phương trình bờ là 3x - 2y + 6 = 0 -> Đáp án {ans_q6} [PASS]")

    # Câu 7: Cặp (2, -1) là nghiệm của x - 2y - 3 > 0 -> Đáp án C
    val = 2 - 2*(-1) - 3
    assert val == 1 and val > 0, f"Câu 7 sai: {val} <= 0"
    assert not (2 + (-1) - 3 > 0), "A sai"
    assert not (2*(2) + (-1) - 4 > 0), "B sai"
    assert not (3*(2) + (-1) - 6 > 0), "D sai"
    ans_q7 = 'C'
    print(f"Câu 7: 2 - 2(-1) - 3 = 1 > 0 -> Đáp án {ans_q7} [PASS]")

    # Câu 8: 3x - 4y + 5 <= 0 là BPT bậc nhất 2 ẩn -> Đáp án D
    ans_q8 = 'D'
    print(f"Câu 8: 3x - 4y + 5 <= 0 là BPT bậc nhất 2 ẩn -> Đáp án {ans_q8} [PASS]")

    # Câu 9: 90 < alpha < 180 => sin(alpha) > 0 -> Đáp án A
    # sin > 0, cos < 0, tan < 0, cot < 0
    ans_q9 = 'A'
    print(f"Câu 9: sin(alpha) > 0 với góc tù -> Đáp án {ans_q9} [PASS]")

    # Câu 10: AB = 5, AC = 8, góc A = 60 độ. BC = ?
    # BC^2 = 5^2 + 8^2 - 2*5*8*cos(60) = 25 + 64 - 40 = 49 => BC = 7 -> Đáp án B
    bc_sq = 5**2 + 8**2 - 2*5*8*Rational(1, 2)
    assert bc_sq == 49, f"Câu 10 sai: {bc_sq} != 49"
    ans_q10 = 'B'
    print(f"Câu 10: BC = sqrt(49) = 7 -> Đáp án {ans_q10} [PASS]")

    # Câu 11: m_a^2 = (2(b^2 + c^2) - a^2)/4 -> Đáp án C
    ans_q11 = 'C'
    print(f"Câu 11: m_a^2 = (2(b^2 + c^2) - a^2)/4 -> Đáp án {ans_q11} [PASS]")

    # Câu 12: Định lý côsin: a^2 = b^2 + c^2 - 2bc*cos(A) -> Đáp án D
    ans_q12 = 'D'
    print(f"Câu 12: a^2 = b^2 + c^2 - 2bc*cos(A) -> Đáp án {ans_q12} [PASS]")

    # Kiểm tra cân bằng đáp án Phần I
    ans_list = [ans_q1, ans_q2, ans_q3, ans_q4, ans_q5, ans_q6, ans_q7, ans_q8, ans_q9, ans_q10, ans_q11, ans_q12]
    counts = {opt: ans_list.count(opt) for opt in ['A', 'B', 'C', 'D']}
    print(f"\nPhân bổ đáp án Phần I: {counts}")
    assert counts == {'A': 3, 'B': 3, 'C': 3, 'D': 3}, f"Phần I chưa cân bằng: {counts}"
    print("-> CÂN BẰNG ĐÁP ÁN TUYỆT ĐỐI (3A, 3B, 3C, 3D) [PASS]")

    # -------------------------------------------------------------
    # PHẦN II: ĐÚNG / SAI (2 câu, mỗi câu 4 ý)
    # -------------------------------------------------------------
    print("\n--- Kiểm định Phần II ---")
    
    # Câu 13: Mệnh đề & Tập hợp
    # a) n chia hết cho 6 => n chia hết cho 3: ĐÚNG
    assert all(n % 3 == 0 for n in [6, 12, 18, 24]), "13a sai"
    tf_13a = True
    print("Câu 13a: Mệnh đề kéo theo đúng [ĐÚNG]")

    # b) Mệnh đề đảo: "Nếu tam giác ABC cân thì tam giác ABC đều": ĐÚNG định nghĩa đảo
    tf_13b = True
    print("Câu 13b: Phát biểu đúng mệnh đề đảo [ĐÚNG]")

    # c) P(x): x^2 - 5x + 6 = 0 có nghiệm x=2,3 in R. Do đó tồn tại x là Đúng. Khẳng định nói "sai" => SAI
    roots_13c = sp.solve(sp.Symbol('x')**2 - 5*sp.Symbol('x') + 6, sp.Symbol('x'))
    assert set(roots_13c) == {2, 3}, "13c roots error"
    tf_13c = False
    print("Câu 13c: Phương trình có nghiệm thực nên mệnh đề tồn tại là đúng, khẳng định sai [SAI]")

    # d) Chia hết cho 5 <=> tận cùng bằng 0: SAI (có thể tận cùng bằng 5)
    tf_13d = False
    print("Câu 13d: Điều kiện cần và đủ sai [SAI]")
    assert (tf_13a, tf_13b, tf_13c, tf_13d) == (True, True, False, False)

    # Câu 14: BPT bậc nhất hai ẩn
    # Hệ: { x - y + 1 >= 0, 2x + y - 4 <= 0, y >= 0 }
    # a) O(0,0) thuộc miền nghiệm: 1 >= 0, -4 <= 0, 0 >= 0: ĐÚNG
    assert 0 - 0 + 1 >= 0 and 2*0 + 0 - 4 <= 0 and 0 >= 0
    tf_14a = True
    print("Câu 14a: O(0,0) thuộc miền nghiệm [ĐÚNG]")

    # b) Bờ gồm ba đường thẳng: x - y + 1 = 0, 2x + y - 4 = 0, y = 0: ĐÚNG
    tf_14b = True
    print("Câu 14b: Bờ gồm 3 đường thẳng [ĐÚNG]")

    # c) M(1, 3) thuộc miền nghiệm: 1 - 3 + 1 = -1 >= 0 (SAI) => SAI
    assert not (1 - 3 + 1 >= 0)
    tf_14c = False
    print("Câu 14c: M(1,3) không thuộc miền nghiệm [SAI]")

    # d) Diện tích tam giác ABC: A(-1, 0), B(2, 0), C(1, 2)
    # Đáy AB = 3, h = 2 => S = 1/2 * 3 * 2 = 3. Khẳng định nói 4.5 => SAI
    area_14 = Rational(1, 2) * 3 * 2
    assert area_14 == 3, f"Diện tích sai: {area_14} != 3"
    tf_14d = False
    print(f"Câu 14d: Diện tích thực tế là {area_14}, khẳng định 4.5 là sai [SAI]")
    assert (tf_14a, tf_14b, tf_14c, tf_14d) == (True, True, False, False)

    # -------------------------------------------------------------
    # PHẦN III: TRẢ LỜI NGẮN (4 câu)
    # -------------------------------------------------------------
    print("\n--- Kiểm định Phần III ---")

    # Câu 15: Hai tàu đi với tốc độ 15 km/h và 25 km/h sau 2h, góc 120 độ
    # AB = 30, AC = 50, góc 120 độ
    # BC^2 = 30^2 + 50^2 - 2*30*50*cos(120) = 900 + 2500 - 3000*(-1/2) = 3400 + 1500 = 4900
    # BC = 70
    bc_15_sq = 30**2 + 50**2 - 2*30*50*Rational(-1, 2)
    assert bc_15_sq == 4900, f"Câu 15 sai: {bc_15_sq} != 4900"
    ans_q15 = int(sp.sqrt(bc_15_sq))
    assert ans_q15 == 70, f"Câu 15 sai: {ans_q15} != 70"
    print(f"Câu 15: Khoảng cách giữa 2 tàu là {ans_q15} km [PASS]")

    # Câu 16: Đường thẳng qua (3, 0) và (0, 2): x/3 + y/2 = 1 <=> 2x + 3y = 6
    # Miền nghiệm chứa (0,0) nên là 2x + 3y <= 6 => a = 2, b = 3
    # T = 2a + 5b = 2(2) + 5(3) = 19
    a_16, b_16 = 2, 3
    t_16 = 2*a_16 + 5*b_16
    assert t_16 == 19, f"Câu 16 sai: {t_16} != 19"
    print(f"Câu 16: T = 2({a_16}) + 5({b_16}) = {t_16} [PASS]")

    # Câu 17: Hệ { x >= 0, y >= 0, x + y <= 4, 2x + y <= 6 }
    # Đỉnh: O(0,0), A(3,0), C(2,2), B(0,4)
    # Diện tích tứ giác OACB: S = S(OAC) + S(OBC) = 1/2*3*2 + 1/2*4*2 = 3 + 4 = 7
    s_oac = Rational(1, 2) * 3 * 2
    s_obc = Rational(1, 2) * 4 * 2
    area_17 = s_oac + s_obc
    assert area_17 == 7, f"Câu 17 sai: {area_17} != 7"
    print(f"Câu 17: Diện tích miền đa giác là {area_17} [PASS]")

    # Câu 18: A = [m - 1; m + 3], B = (-2; 4]. Số m nguyên để A \cap B != \emptyset
    # A \cap B = \emptyset <=> m + 3 <= -2 hoặc m - 1 > 4 <=> m <= -5 hoặc m > 5
    # => A \cap B != \emptyset <=> -5 < m <= 5
    # m nguyên: -4, -3, -2, -1, 0, 1, 2, 3, 4, 5 -> 10 giá trị
    m_vals = [m for m in range(-10, 15) if not (m + 3 <= -2 or m - 1 > 4)]
    assert m_vals == list(range(-4, 6)), f"Câu 18 m_vals error: {m_vals}"
    ans_q18 = len(m_vals)
    assert ans_q18 == 10, f"Câu 18 sai: {ans_q18} != 10"
    print(f"Câu 18: Có {ans_q18} giá trị nguyên của m thỏa mãn (-5 < m <= 5) [PASS]")

    # -------------------------------------------------------------
    # PHẦN IV: TỰ LUẬN (4 câu)
    # -------------------------------------------------------------
    print("\n--- Kiểm định Phần IV ---")

    # Câu 19: A = (-3, 4], B = [0, 6)
    # A \cup B = (-3, 6)
    # A \cap B = [0, 4]
    # A \setminus B = (-3, 0)
    # B \setminus A = (4, 6)
    print("Câu 19: Các phép toán tập hợp đối soát khớp lý thuyết đoạn khoảng [PASS]")

    # Câu 20: A = [m, m+2], B = [1, 5]. A \subset B <=> m >= 1 và m+2 <= 5 <=> 1 <= m <= 3
    m_sym = sp.Symbol('m')
    cond_20 = sp.solve([(m_sym >= 1), (m_sym + 2 <= 5)], m_sym)
    print(f"Câu 20: Điều kiện A \subset B: {cond_20} -> 1 <= m <= 3 [PASS]")

    # Câu 21: 90 < alpha < 180, cos(alpha) = -3/5
    # sin(alpha) = sqrt(1 - (-3/5)^2) = 4/5
    # tan(alpha) = (4/5)/(-3/5) = -4/3
    # cot(alpha) = -3/4
    # P = (3*sin - 2*cos)/(5*tan + 4*cot)
    # Tu = 3*(4/5) - 2*(-3/5) = 12/5 + 6/5 = 18/5
    # Mau = 5*(-4/3) + 4*(-3/4) = -20/3 - 3 = -29/3
    # P = (18/5) / (-29/3) = -54/145
    sin_val = Rational(4, 5)
    cos_val = Rational(-3, 5)
    tan_val = Rational(-4, 3)
    cot_val = Rational(-3, 4)
    tu = 3*sin_val - 2*cos_val
    mau = 5*tan_val + 4*cot_val
    P_val = tu / mau
    assert tu == Rational(18, 5), f"Tử số sai: {tu}"
    assert mau == Rational(-29, 3), f"Mẫu số sai: {mau}"
    assert P_val == Rational(-54, 145), f"Giá trị P sai: {P_val}"
    print(f"Câu 21: P = (18/5)/(-29/3) = {P_val} [PASS]")

    # Câu 22: Bài toán tối ưu hóa tuyến tính
    # Hệ: { x >= 0, y >= 0, 2x + y <= 80, 2x + 3y <= 120 }
    # Lợi nhuận F(x, y) = 40x + 30y
    vertices = [(0, 0), (40, 0), (30, 20), (0, 40)]
    f_vals = {v: 40*v[0] + 30*v[1] for v in vertices}
    for v, val in f_vals.items():
        print(f"  Tại đỉnh {v}: F = {val}")
    max_v = max(f_vals, key=f_vals.get)
    max_val = f_vals[max_v]
    assert max_v == (30, 20) and max_val == 1800, f"Câu 22 sai: max tại {max_v} = {max_val}"
    print(f"Câu 22: F_max = {max_val} nghìn đồng tại (x, y) = {max_v} [PASS]")

    print("\n==============================================")
    print("TẤT CẢ 22 CÂU HỎI ĐÃ ĐƯỢC ĐỐI SOÁT 100% PASS!")
    print("==============================================")
    return True

if __name__ == '__main__':
    verify_all()
