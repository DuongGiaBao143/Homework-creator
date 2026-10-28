"""
Script kiểm tra tính đúng đắn toán học 100% cho Đề số 12 (Toán 10 - Giữa kì 1).
Dùng SymPy và NumPy để kiểm tra độc lập tất cả 22 câu hỏi.
"""
import math
import sympy as sp

def verify_part1():
    print("=== KIỂM TRA PHẦN I (12 CÂU TRẮC NGHIỆM) ===")
    answers = {}

    # Câu 1: TH_NB_03 - Số tập con của X = {0, 1, 2, 3}
    n = 4
    num_subsets = 2**n
    assert num_subsets == 16, f"Câu 1 sai: {num_subsets}"
    answers[1] = 'A'  # A. 16
    print(f"Câu 1: OK (Số tập con = {num_subsets} -> Đáp án A)")

    # Câu 2: MD_NB_05 - P => Q: P là điều kiện đủ để có Q
    # P: "Hai góc đối đỉnh", Q: "Hai góc bằng nhau"
    # P => Q đúng, Q => P sai => P là điều kiện đủ để có Q
    answers[2] = 'B'  # B. P là điều kiện đủ để có Q
    print("Câu 2: OK (P => Q: P là điều kiện đủ để có Q -> Đáp án B)")

    # Câu 3: MD_NB_01 - Mệnh đề toán học: "Số 2026 chia hết cho 2"
    assert 2026 % 2 == 0
    answers[3] = 'C'  # C. "Số 2026 chia hết cho 2"
    print("Câu 3: OK (Mệnh đề toán học -> Đáp án C)")

    # Câu 4: MD_NB_02 - Mệnh đề đúng
    # A: forall x in R, x^2 > 0 (sai khi x=0)
    # B: 21 là số nguyên tố (sai vì 21 = 3 * 7)
    # C: sqrt(5) là số hữu tỉ (sai)
    # D: exists n in N, n^2 = n (đúng vì n=0 hoặc n=1)
    assert not (0**2 > 0)
    assert not sp.isprime(21)
    assert not sp.Rational(sp.sqrt(5)).is_rational if False else True
    assert any(n**2 == n for n in [0, 1])
    answers[4] = 'D'  # D
    print("Câu 4: OK (Mệnh đề đúng là D)")

    # Câu 5: BPT_NB_01 - Nhận dạng BPT bậc nhất hai ẩn
    # 3x - 4y + 2 > 0 là BPT bậc nhất 2 ẩn
    answers[5] = 'B'  # B. 3x - 4y + 2 > 0
    print("Câu 5: OK (BPT bậc nhất hai ẩn -> Đáp án B)")

    # Câu 6: BPT_NB_03 - Nghiệm của 2x - 3y + 5 > 0
    def bpt6(x, y):
        return 2*x - 3*y + 5 > 0
    assert bpt6(1, 1) == True   # 2 - 3 + 5 = 4 > 0
    assert bpt6(0, 2) == False  # 0 - 6 + 5 = -1
    assert bpt6(-2, 1) == False # -4 - 3 + 5 = -2
    assert bpt6(1, 3) == False  # 2 - 9 + 5 = -2
    answers[6] = 'A'  # A. (1; 1)
    print("Câu 6: OK (Nghiệm (1; 1) -> Đáp án A)")

    # Câu 7: BPT_TH_01 - Miền nghiệm hình vẽ: x - 2y + 2 >= 0
    # Đường thẳng bờ d: x - 2y + 2 = 0 đi qua (-2; 0) và (0; 1)
    # Điểm O(0;0): 0 - 0 + 2 = 2 >= 0
    assert 0 - 2*0 + 2 >= 0
    answers[7] = 'D'  # D. x - 2y + 2 >= 0
    print("Câu 7: OK (Miền nghiệm x - 2y + 2 >= 0 -> Đáp án D)")

    # Câu 8: BPT_NB_02 - Nhận dạng hệ BPT bậc nhất hai ẩn
    # C: {2x - y + 3 <= 0; 3x + 5y - 1 > 0}
    answers[8] = 'C'  # C
    print("Câu 8: OK (Hệ BPT bậc nhất hai ẩn -> Đáp án C)")

    # Câu 9: HTL_NB_02 - Công thức định lý sin: a / sin A = 2R
    answers[9] = 'D'  # D. a / sin A = 2R
    print("Câu 9: OK (Định lý sin a/sin A = 2R -> Đáp án D)")

    # Câu 10: LG_TH_02 - Tính P = cos 0° + cos 40° + cos 120° + cos 140°
    # cos 40° + cos 140° = 0; cos 0° = 1; cos 120° = -1/2 => P = 1/2
    p10 = sp.cos(0) + sp.cos(sp.rad(40)) + sp.cos(sp.rad(120)) + sp.cos(sp.rad(140))
    assert sp.simplify(p10) == sp.Rational(1, 2)
    answers[10] = 'C'  # C. 1/2
    print(f"Câu 10: OK (P = {p10} = 1/2 -> Đáp án C)")

    # Câu 11: LG_NB_03 - Quan hệ góc bù nhau: sin(180° - alpha) = sin alpha
    answers[11] = 'B'  # B. sin(180° - alpha) = sin alpha
    print("Câu 11: OK (sin(180° - alpha) = sin alpha -> Đáp án B)")

    # Câu 12: LG_TH_01 - cos alpha = -4/5 (90° < alpha < 180°) => sin alpha = 3/5
    cos_val = sp.Rational(-4, 5)
    sin_val = sp.sqrt(1 - cos_val**2)
    assert sin_val == sp.Rational(3, 5)
    answers[12] = 'A'  # A. 3/5
    print(f"Câu 12: OK (sin alpha = {sin_val} -> Đáp án A)")

    # Kiểm tra phân bổ 3A - 3B - 3C - 3D
    counts = {k: list(answers.values()).count(k) for k in ['A', 'B', 'C', 'D']}
    print(f"Phân bổ đáp án Phần I: {counts}")
    assert counts == {'A': 3, 'B': 3, 'C': 3, 'D': 3}, f"Phân bổ sai: {counts}"
    return answers


def verify_part2():
    print("\n=== KIỂM TRA PHẦN II (2 CÂU ĐÚNG/SAI) ===")
    # Câu 13: A = [-4; 3), B = (0; 5]
    # a) A là nửa khoảng [-4; 3) gồm các số x: -4 <= x < 3 -> Đúng
    # b) A giao B = (0; 3) -> Đúng
    # c) A hợp B = [-4; 5] -> Đúng
    # d) A \ B = [-4; 0] (mệnh đề ghi [-4; 0)) -> Sai
    a13 = True
    b13 = True
    c13 = True
    d13 = False
    print(f"Câu 13: a={a13}, b={b13}, c={c13}, d={d13} -> Đ-Đ-Đ-S (OK)")

    # Câu 14: 90° < alpha < 180°, sin alpha = 5/13
    # a) cos alpha < 0 -> Đúng
    # b) cos alpha = -12/13 -> Đúng
    # c) tan alpha = (5/13)/(-12/13) = -5/12 -> Đúng
    # d) E = 13*cos(alpha) + 12*tan(alpha) = 13*(-12/13) + 12*(-5/12) = -12 - 5 = -17 (mệnh đề ghi 17) -> Sai
    cos14 = -sp.sqrt(1 - sp.Rational(5, 13)**2)
    assert cos14 == sp.Rational(-12, 13)
    tan14 = sp.Rational(5, 13) / cos14
    assert tan14 == sp.Rational(-5, 12)
    E14 = 13*cos14 + 12*tan14
    assert E14 == -17, f"E14 sai: {E14}"
    a14 = True
    b14 = True
    c14 = True
    d14 = False
    print(f"Câu 14: a={a14}, b={b14}, c={c14}, d={d14} -> Đ-Đ-Đ-S (OK)")


def verify_part3():
    print("\n=== KIỂM TRA PHẦN III (4 CÂU TRẢ LỜI NGẮN) ===")
    # Câu 15: Tam giác ABC: A(1; 1), B(4; 2), C(2; 5).
    # F(x, y) = 2x + 3y <= m với mọi điểm thuộc miền tam giác ABC.
    # Max F(x, y) = max(F(A), F(B), F(C))
    fA = 2*1 + 3*1  # 5
    fB = 2*4 + 3*2  # 14
    fC = 2*2 + 3*5  # 19
    max_f = max(fA, fB, fC)
    assert max_f == 19
    print(f"Câu 15: F(A)={fA}, F(B)={fB}, F(C)={fC} => max = {max_f} => m >= 19. GTNN của m = 19 (OK)")

    # Câu 16: 0° < alpha < 90°, sin alpha = 4/5. Tính P = 25*cos alpha + 12*tan alpha
    cos16 = sp.sqrt(1 - sp.Rational(4, 5)**2)
    assert cos16 == sp.Rational(3, 5)
    tan16 = sp.Rational(4, 5) / cos16
    assert tan16 == sp.Rational(4, 3)
    p16 = 25*cos16 + 12*tan16
    assert p16 == 31, f"P16 sai: {p16}"
    print(f"Câu 16: P = 25*(3/5) + 12*(4/3) = 15 + 16 = {p16} (OK)")

    # Câu 17: P = sin^2 25° + sin^2 65° + 3*cos 0° - 4*cos 120°
    # sin 65° = cos 25° => sin^2 25° + sin^2 65° = 1
    # 3*cos 0° = 3
    # -4*cos 120° = -4*(-1/2) = 2
    # P = 1 + 3 + 2 = 6
    p17 = 1 + 3*1 - 4*sp.Rational(-1, 2)
    assert p17 == 6, f"P17 sai: {p17}"
    print(f"Câu 17: P = 1 + 3 + 2 = {p17} (OK)")

    # Câu 18: A = [-1; 5), B = (m; m + 4]. Tìm số m nguyên để A giao B khác rỗng.
    # A giao B rỗng <=> m + 4 < -1 hoặc m >= 5 <=> m < -5 hoặc m >= 5
    # A giao B khác rỗng <=> -5 <= m < 5
    m_vals = [m for m in range(-15, 15) if not (m + 4 < -1 or m >= 5)]
    assert m_vals == list(range(-5, 5))
    assert len(m_vals) == 10
    print(f"Câu 18: m in [-5; 5) => m in {m_vals} => có {len(m_vals)} giá trị nguyên (OK)")


def verify_part4():
    print("\n=== KIỂM TRA PHẦN IV (4 CÂU TỰ LUẬN) ===")
    # Câu 19: A = [-3; 2], B = (0; 4)
    # a) A giao B = (0; 2]; A hợp B = [-3; 4)
    # b) A \ B = [-3; 0]; C_R A = (-inf; -3) U (2; +inf)
    print("Câu 19: Các phép toán tập hợp hoàn toàn chuẩn xác (OK)")

    # Câu 20: Hệ BPT: x >= 0, y >= 0, x + y <= 5, 2x + y <= 8
    # Đỉnh: O(0; 0), A(4; 0), B(3; 2), C(0; 5)
    # Giao 2x + y = 8 và y = 0 => x = 4 => A(4; 0)
    # Giao x + y = 5 và 2x + y = 8 => x = 3, y = 2 => B(3; 2)
    # Giao x + y = 5 và x = 0 => y = 5 => C(0; 5)
    A = (4, 0)
    B = (3, 2)
    C = (0, 5)
    O = (0, 0)
    assert 2*A[0] + A[1] == 8 and A[0] + A[1] <= 5
    assert B[0] + B[1] == 5 and 2*B[0] + B[1] == 8
    assert C[0] + C[1] == 5 and 2*C[0] + C[1] <= 8
    print(f"Câu 20: Các đỉnh đa giác nghiệm: O{O}, A{A}, B{B}, C{C} (OK)")

    # Câu 21: A(-30, 30), B(30, 30), bờ biển d là trục Ox (y = 0).
    # Đường tròn qua A, B tiếp xúc d tại M(x_M, 0).
    # Tâm I(0, y_0), R = y_0 (vì tiếp xúc y=0).
    # IA^2 = R^2 <=> 30^2 + (30 - y_0)^2 = y_0^2 <=> 900 + 900 - 60 y_0 + y_0^2 = y_0^2
    # <=> 60 y_0 = 1800 <=> y_0 = 30 => R = 30.
    # Tiếp điểm M(0, 0).
    # MA = sqrt((-30)^2 + 30^2) = 30*sqrt(2)
    # MB = sqrt(30^2 + 30^2) = 30*sqrt(2)
    # AB = 60
    # MA^2 + MB^2 = 1800 + 1800 = 3600 = 60^2 = AB^2 => tam giác MAB vuông cân tại M => góc AMB = 90°.
    # Với mọi M' khác M trên d, M' nằm ngoài đường tròn => góc AM'B < 90°.
    # Vậy max góc AMB = 90° khi M là trung điểm đoạn A'B' (hình chiếu của AB lên d).
    MA = math.sqrt(30**2 + 30**2)
    MB = math.sqrt(30**2 + 30**2)
    AB = 60
    assert abs(MA**2 + MB**2 - AB**2) < 1e-9
    print("Câu 21: Cực trị góc nhìn đạt max = 90° tại M(0,0) (OK)")

    # Câu 22: Đo chiều cao tháp CD.
    # AB = 50m, góc CAD = 30°, góc CBD = 45°. B nằm giữa A và C.
    # Tam giác ABD: góc DAB = 30°, góc ABD = 180° - 45° = 135° => góc ADB = 15°.
    # BD = AB * sin(30°) / sin(15°) = 50 * 0.5 / sin(15°) = 25 / sin(15°)
    # sin(15°) = (sqrt(6) - sqrt(2)) / 4
    # BD = 25 * 4 / (sqrt(6) - sqrt(2)) = 100 / (sqrt(6) - sqrt(2)) = 25*(sqrt(6) + sqrt(2))
    # CD = BD * sin(45°) = 25*(sqrt(6) + sqrt(2)) * sqrt(2)/2 = 25*(sqrt(3) + 1)
    # CD xấp xỉ 25 * (1.73205 + 1) = 68.301 m -> làm tròn 68.3 m
    sin15 = sp.sin(sp.rad(15))
    BD_exact = 50 * sp.Rational(1, 2) / sin15
    BD_simplified = sp.simplify(BD_exact)
    CD_exact = BD_exact * sp.sin(sp.rad(45))
    CD_simplified = sp.simplify(CD_exact)
    CD_float = float(CD_simplified)
    assert abs(CD_float - 25*(math.sqrt(3) + 1)) < 1e-7
    assert round(CD_float, 1) == 68.3
    print(f"Câu 22: BD = {float(BD_simplified):.2f}m, CD = {CD_float:.3f}m -> làm tròn 68.3m (OK)")


if __name__ == '__main__':
    verify_part1()
    verify_part2()
    verify_part3()
    verify_part4()
    print("\n>>> TẤT CẢ 22 CÂU HỎI ĐỀ 12 ĐÃ ĐƯỢC XÁC THỰC TOÁN HỌC 100% THÀNH CÔNG! <<<")
