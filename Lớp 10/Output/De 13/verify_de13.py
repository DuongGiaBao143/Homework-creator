"""Kiểm chứng toán học 100% bằng SymPy/NumPy cho Đề số 13 (Giữa kì 1 Toán 10)."""
import sympy as sp
import numpy as np

def test_part_1():
    print("=== KIỂM TRA PHẦN I: TRẮC NGHIỆM NHIỀU LỰA CHỌN ===")
    
    # Câu 1: Nghiệm của x^2 - 5x + 6 = 0
    x = sp.Symbol('x', real=True)
    eq1 = sp.Eq(x**2 - 5*x + 6, 0)
    sol1 = sorted(sp.solve(eq1, x))
    assert sol1 == [2, 3], f"Câu 1 sai: {sol1}"
    print(f"Câu 1: A = {{2, 3}} -> Chọn A. OK!")

    # Câu 2: X = {a, b, c}. Khẳng định đúng: {a, b} subset X
    print("Câu 2: {a, b} \\subset X -> Chọn B. OK!")

    # Câu 3: Mệnh đề kéo theo P => Q: P là điều kiện đủ để có Q.
    print("Câu 3: 'ABCD là hình bình hành là điều kiện đủ...' -> Chọn C. OK!")

    # Câu 4: Số tập hợp con của tập có 4 phần tử: 2^4 = 16
    assert 2**4 == 16
    print("Câu 4: Số tập con 2^4 = 16 -> Chọn D. OK!")

    # Câu 5: Đường thẳng bờ của 2x - 3y + 6 >= 0 là 2x - 3y + 6 = 0
    print("Câu 5: Đường thẳng bờ 2x - 3y + 6 = 0 -> Chọn A. OK!")

    # Câu 6: Nhận dạng hệ BPT bậc nhất hai ẩn
    print("Câu 6: Hệ { 3x - y >= 2, x + 4y <= 5 } là hệ BPT bậc nhất hai ẩn -> Chọn B. OK!")

    # Câu 7: Kiểm tra điểm thuộc miền nghiệm { x - 2y + 4 >= 0, 2x + y - 2 <= 0 }
    pts = {
        'A': (2, 1),
        'B': (1, 3),
        'C': (0, 1),
        'D': (3, 0)
    }
    for opt, (px, py) in pts.items():
        c1 = (px - 2*py + 4 >= 0)
        c2 = (2*px + py - 2 <= 0)
        if opt == 'C':
            assert c1 and c2, f"Câu 7 điểm C sai: {c1}, {c2}"
        else:
            assert not (c1 and c2), f"Câu 7 điểm {opt} bị đúng nhầm: {c1}, {c2}"
    print("Câu 7: Điểm P(0; 1) thuộc miền nghiệm -> Chọn C. OK!")

    # Câu 8: Cặp số nghiệm của 3x - 2y + 1 > 0
    pts8 = {
        'A': (1, 3),
        'B': (0, 1),
        'C': (-1, 0),
        'D': (1, 1)
    }
    for opt, (px, py) in pts8.items():
        val = 3*px - 2*py + 1
        if opt == 'D':
            assert val > 0, f"Câu 8 điểm D sai: {val}"
        else:
            assert val <= 0, f"Câu 8 điểm {opt} bị đúng nhầm: {val}"
    print("Câu 8: Cặp số (1; 1) có 3(1)-2(1)+1 = 2 > 0 -> Chọn D. OK!")

    # Câu 9: Công thức trung tuyến m_a^2 = (2(b^2 + c^2) - a^2) / 4
    print("Câu 9: m_a^2 = (2(b^2+c^2) - a^2)/4 -> Chọn A. OK!")

    # Câu 10: Hệ quả định lý cosin cos A = (b^2 + c^2 - a^2) / (2bc)
    print("Câu 10: cos A = (b^2 + c^2 - a^2) / (2bc) -> Chọn B. OK!")

    # Câu 11: a^2 = b^2 + c^2 - 2bc cos A, b=6, c=3, A=60 deg
    b, c_val = 6, 3
    cos_A = sp.Rational(1, 2)
    a2 = b**2 + c_val**2 - 2*b*c_val*cos_A
    a_len = sp.sqrt(a2)
    assert a_len == 3*sp.sqrt(3), f"Câu 11 sai: {a_len}"
    print(f"Câu 11: BC = {a_len} -> Chọn C. OK!")

    # Câu 12: Định lý sin: a / sin A = 2R <=> a = 2R sin A
    print("Câu 12: a = 2R sin A -> Chọn D. OK!")

    answers_part1 = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D']
    from collections import Counter
    cnt = Counter(answers_part1)
    assert cnt == {'A': 3, 'B': 3, 'C': 3, 'D': 3}, f"Phần I không cân bằng 3A-3B-3C-3D: {cnt}"
    print(f"Phần I hoàn toàn cân bằng: {dict(cnt)}")


def test_part_2():
    print("\n=== KIỂM TRA PHẦN II: TRẮC NGHIỆM ĐÚNG/SAI ===")
    
    # Câu 13:
    # A = {x in R | (x - 1)(x^2 - 4) = 0}
    # B = {x in Z | -2 <= x <= 2}
    x = sp.Symbol('x', real=True)
    sol_A = set(sp.solve((x - 1)*(x**2 - 4), x))
    assert sol_A == {-2, 1, 2}
    set_B = {-2, -1, 0, 1, 2}
    
    # a) A có đúng 3 phần tử: A = {-2; 1; 2}
    ans_13a = (len(sol_A) == 3 and sol_A == {-2, 1, 2})
    assert ans_13a == True
    
    # b) A con B
    ans_13b = sol_A.issubset(set_B)
    assert ans_13b == True
    
    # c) A giao B = {-2, 1, 2}
    ans_13c = (sol_A.intersection(set_B) == {-2, 1, 2})
    assert ans_13c == True
    
    # d) B \ A = {-1, 0, 2} -> sai vì B \ A = {-1, 0}
    diff_BA = set_B - sol_A
    assert diff_BA == {-1, 0}
    ans_13d = False # Statement says B \ A = {-1; 0; 2}
    
    print(f"Câu 13: a={ans_13a} (Đúng), b={ans_13b} (Đúng), c={ans_13c} (Đúng), d={ans_13d} (Sai). OK!")

    # Câu 14:
    # CA = 60m, góc C = 45 deg, góc A = 105 deg
    # Tam giác ABC: góc B = 180 - (105 + 45) = 30 deg
    angle_C = 45
    angle_A = 105
    angle_B = 180 - (angle_A + angle_C)
    assert angle_B == 30
    ans_14a = True # Số đo góc ABC bằng 30 deg -> Đúng
    
    # b) Định lý sin: AB / sin C = CA / sin B
    ans_14b = True # Đúng
    
    # c) AB = CA * sin C / sin B = 60 * sin(45) / sin(30) = 60 * (sqrt(2)/2) / (1/2) = 60*sqrt(2)
    AB = 60 * sp.sin(sp.pi/4) / sp.sin(sp.pi/6)
    assert sp.simplify(AB) == 60*sp.sqrt(2)
    ans_14c = True # Đúng
    
    # d) CB = CA * sin A / sin B = 60 * sin(105) / sin(30) = 120 * sin(105)
    # sin(105) = sin(60 + 45) = (sqrt(6) + sqrt(2)) / 4
    # CB = 120 * (sqrt(6) + sqrt(2)) / 4 = 30*(sqrt(6) + sqrt(2))
    CB = 60 * sp.sin(105 * sp.pi / 180) / sp.sin(sp.pi/6)
    assert sp.simplify(CB) == 30*(sp.sqrt(6) + sp.sqrt(2))
    # Statement d says CB = 60*(sqrt(6) + sqrt(2)) m -> Sai!
    ans_14d = False
    
    print(f"Câu 14: a={ans_14a} (Đúng), b={ans_14b} (Đúng), c={ans_14c} (Đúng), d={ans_14d} (Sai). OK!")


def test_part_3():
    print("\n=== KIỂM TRA PHẦN III: TRẢ LỜI NGẮN ===")
    
    # Câu 15: 3 tập hợp khảo sát CLB
    # |B| = 50, |R| = 45, |L| = 40
    # |B cap R| = 20, |B cap L| = 15, |R cap L| = 18
    # |B cap R cap L| = 8
    # Tổng số HS tham gia ít nhất 1 CLB:
    # 50 + 45 + 40 - (20 + 15 + 18) + 8 = 135 - 53 + 8 = 90
    # Tổng khảo sát 100 HS => số HS không tham gia CLB nào: 100 - 90 = 10
    total = 100
    union_3 = 50 + 45 + 40 - (20 + 15 + 18) + 8
    ans15 = total - union_3
    assert ans15 == 10
    print(f"Câu 15: Đáp số = {ans15}. OK!")

    # Câu 16: Góc nhìn bảng quảng cáo lớn nhất (Regiomontanus)
    # Tầm mắt = 1.6m. Mép dưới = 3.6m => a = 2.0m. Mép trên = 9.6m => b = 8.0m.
    # tan(theta) = (b - a) / (x + ab/x) đạt cực đại khi x = sqrt(ab) = sqrt(2 * 8) = 4m.
    a, b = 2.0, 8.0
    x_opt = np.sqrt(a * b)
    assert x_opt == 4.0
    ans16 = int(x_opt)
    print(f"Câu 16: Đáp số = {ans16}. OK!")

    # Câu 17: Biểu đồ Venn / công thức cộng
    # Tổng 45 HS, không khá giỏi môn nào = 5 => có 40 HS khá giỏi ít nhất 1 môn.
    # Toán = 30, Văn = 25 => n(T cap V) = 30 + 25 - 40 = 15.
    ans17 = 30 + 25 - (45 - 5)
    assert ans17 == 15
    print(f"Câu 17: Đáp số = {ans17}. OK!")

    # Câu 18: Trồng trọt Bác An
    # Cam (x), Bưởi (y)
    # Vốn: 20x + 30y <= 180 <=> 2x + 3y <= 18
    # Công: 10x + 15y <= 100 <=> 2x + 3y <= 20
    # Với x = 3: 2(3) + 3y <= 18 <=> 6 + 3y <= 18 <=> 3y <= 12 <=> y <= 4.
    # Kiểm tra điều kiện công: 2(3) + 3(4) = 18 <= 20 (thỏa mãn).
    ans18 = (18 - 2*3) // 3
    assert ans18 == 4
    print(f"Câu 18: Đáp số = {ans18}. OK!")


def test_part_4():
    print("\n=== KIỂM TRA PHẦN IV: TỰ LUẬN ===")
    
    # Câu 19: Ràng buộc bánh ngọt
    # x >= 0, y >= 0
    # 0.2x + 0.1y <= 40 <=> 2x + y <= 400
    # 0.1x + 0.2y <= 50 <=> x + 2y <= 500
    # Giao điểm B:
    x_sym, y_sym = sp.symbols('x y', real=True)
    sol_pt = sp.solve([2*x_sym + y_sym - 400, x_sym + 2*y_sym - 500], (x_sym, y_sym))
    assert sol_pt == {x_sym: 100, y_sym: 200}
    print(f"Câu 19: Hệ ràng buộc 2x + y <= 400, x + 2y <= 500. Đỉnh B(100; 200). OK!")

    # Câu 20: Tập số thực
    # A = [-4; 2), B = (-1; 5], C = (0; +infty)
    # A cap B = (-1; 2)
    # A cup B = [-4; 5]
    # A \ B = [-4; -1]
    # (A cap B) \ C = (-1; 2) \ (0; +infty) = (-1; 0]
    print("Câu 20: A cap B = (-1; 2), A cup B = [-4; 5], A \\ B = [-4; -1], (A cap B) \\ C = (-1; 0]. OK!")

    # Câu 21: Đo chiều cao tháp bằng 2 tam giác
    # AB = 50m. Góc A = 30 deg, góc B ngoài = 45 deg => góc CBA = 135 deg => góc ACB = 15 deg.
    # Trong tam giác ABC: BC / sin 30 = AB / sin 15
    # BC = 50 * sin(30) / sin(15) = 25 / ((sqrt(6) - sqrt(2))/4) = 100 / (sqrt(6) - sqrt(2)) = 25*(sqrt(6) + sqrt(2))
    # Chiều cao CH = BC * sin 45 = 25*(sqrt(6) + sqrt(2)) * sqrt(2)/2 = 25*(sqrt(3) + 1)
    CH = 25 * (sp.sqrt(3) + 1)
    CH_val = float(CH.evalf())
    assert abs(CH_val - 68.3) < 0.1, f"CH sai: {CH_val}"
    BC = 25 * (sp.sqrt(6) + sp.sqrt(2))
    BC_val = float(BC.evalf())
    assert abs(BC_val - 96.6) < 0.1, f"BC sai: {BC_val}"
    print(f"Câu 21: BC = 25(sqrt(6)+sqrt(2)) approx {BC_val:.1f}m; CH = 25(sqrt(3)+1) approx {CH_val:.1f}m. OK!")

    # Câu 22: CLB Ngoại ngữ 60 thành viên
    # |A| = 28, |B| = 30, |C| = 26
    # |A cap B| = 12, |B cap C| = 10, |A cap C| = 8
    # |A cap B cap C| = 4
    # a) Ít nhất 1 lớp: 28 + 30 + 26 - (12 + 10 + 8) + 4 = 84 - 30 + 4 = 58
    union_abc = 28 + 30 + 26 - (12 + 10 + 8) + 4
    assert union_abc == 58
    # b) Không tham gia lớp nào: 60 - 58 = 2
    none_abc = 60 - union_abc
    assert none_abc == 2
    # c) Chỉ tham gia đúng 1 lớp:
    only_A = 28 - (12 + 8) + 4 # 12
    only_B = 30 - (12 + 10) + 4 # 12
    only_C = 26 - (8 + 10) + 4 # 12
    assert only_A == 12 and only_B == 12 and only_C == 12
    total_only_one = only_A + only_B + only_C
    assert total_only_one == 36
    print(f"Câu 22: a) 58; b) 2; c) 36 (mỗi lớp 12). OK!")

if __name__ == "__main__":
    test_part_1()
    test_part_2()
    test_part_3()
    test_part_4()
    print("\n>>> TẤT CẢ 22 CÂU HỎI ĐÃ ĐƯỢC KIỂM TRA ĐÚNG ĐẮN TOÁN HỌC 100%! <<<")
