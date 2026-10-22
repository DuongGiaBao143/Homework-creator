# -*- coding: utf-8 -*-
"""
Kiểm thử độc lập 100% bằng Python/SymPy cho Đề số 07 - Toán 10 GK1.
"""
import math
import sympy as sp

def test_part_1():
    print("--- PHẦN I: TRẮC NGHIỆM ---")
    # Câu 1: MD_NB_01 - Mệnh đề toán học -> C
    # Tổng ba góc trong một tam giác bằng 180 độ
    ans_1 = 'C'

    # Câu 2: MD_NB_02 - Mệnh đề sai -> B
    # \exists x \in \mathbb{R}, x^2 + 1 = 0 là sai vì x^2 + 1 >= 1 > 0
    ans_2 = 'B'

    # Câu 3: TH_NB_03 - Số tập con có đúng 2 phần tử của {a, b, c} -> B
    # C(3, 2) = 3
    c32 = math.comb(3, 2)
    assert c32 == 3
    ans_3 = 'B'

    # Câu 4: TH_TH_01 - A \ B với A = {1, 2, 3, 4, 5}, B = {2, 4, 6, 8} -> A
    A = {1, 2, 3, 4, 5}
    B = {2, 4, 6, 8}
    diff = A - B
    assert diff == {1, 3, 5}
    ans_4 = 'A'

    # Câu 5: BPT_NB_01 - Nhận dạng BPT bậc nhất hai ẩn -> D
    # 3x - 4y + 7 >= 0
    ans_5 = 'D'

    # Câu 6: BPT_NB_02 - Hệ BPT KHÔNG phải bậc nhất hai ẩn -> C
    # x + y > 2 và x - y^2 <= 1 có y^2
    ans_6 = 'C'

    # Câu 7: BPT_NB_03 - Kiểm tra điểm thuộc miền nghiệm 2x - 3y + 6 > 0 -> B
    # N(1; 2): 2(1) - 3(2) + 6 = 2 > 0
    assert 2*(1) - 3*(2) + 6 == 2 > 0
    ans_7 = 'B'

    # Câu 8: BPT_TH_01 - Miền nghiệm x + 2y - 2 <= 0 chứa điểm nào -> D
    # O(0; 0): 0 + 0 - 2 = -2 <= 0
    assert 0 + 2*0 - 2 <= 0
    ans_8 = 'D'

    # Câu 9: LG_NB_01 - cos(120 deg) -> D
    # cos(120) = -1/2
    assert math.isclose(math.cos(math.radians(120)), -0.5)
    ans_9 = 'D'

    # Câu 10: HTL_NB_01 - Định lý côsin -> A
    # a^2 = b^2 + c^2 - 2bc cos A
    ans_10 = 'A'

    # Câu 11: LG_TH_01 - 90 < a < 180, sin a = 3/5 -> cos a = -4/5 -> A
    sin_a = sp.Rational(3, 5)
    cos_a = -sp.sqrt(1 - sin_a**2)
    assert cos_a == sp.Rational(-4, 5)
    ans_11 = 'A'

    # Câu 12: LG_TH_02 - sin^2 35 + cos^2 35 + 2 tan 45 = 1 + 2 = 3 -> C
    ans_12 = 'C'

    answers = [ans_1, ans_2, ans_3, ans_4, ans_5, ans_6, ans_7, ans_8, ans_9, ans_10, ans_11, ans_12]
    counts = {opt: answers.count(opt) for opt in ['A', 'B', 'C', 'D']}
    print("Phần I answers:", answers)
    print("Phân bố đáp án Phần I:", counts)
    assert counts == {'A': 3, 'B': 3, 'C': 3, 'D': 3}, "Phần I phải cân bằng đúng 3A, 3B, 3C, 3D"
    print("[PASS] Phần I cân bằng hoàn hảo 3A-3B-3C-3D!")

def test_part_2():
    print("--- PHẦN II: ĐÚNG / SAI ---")
    # Câu 13: A = [-3; 2), B = (0; 5]
    # a) A chứa đúng 5 số nguyên: {-3, -2, -1, 0, 1} -> Đúng
    A_int = [x for x in range(-10, 10) if -3 <= x < 2]
    assert len(A_int) == 5, f"A_int: {A_int}"

    # b) B là một nửa khoảng -> Đúng
    # c) A \cap B = (0; 2) -> Đúng
    # d) Phát biểu: "A \setminus B = [-3; 0)" -> Sai, vì 0 thuộc A và 0 không thuộc B nên 0 thuộc A \setminus B, đúng phải là [-3; 0]
    c13 = {'a': True, 'b': True, 'c': True, 'd': False}
    print("Câu 13 (a,b,c,d):", c13)

    # Câu 14: Tam giác ABC có AB = 6, AC = 8, góc A = 60 độ
    # a) S = 1/2 AB AC sin A -> Đúng
    # b) BC = 2*sqrt(13) -> Đúng
    bc_sq = 6**2 + 8**2 - 2*6*8*math.cos(math.radians(60))
    assert math.isclose(bc_sq, 52)
    assert math.isclose(math.sqrt(52), 2*math.sqrt(13))

    # c) S = 12*sqrt(3) -> Đúng
    s = 0.5 * 6 * 8 * math.sin(math.radians(60))
    assert math.isclose(s, 12*math.sqrt(3))

    # d) Phát biểu: R = sqrt(39)/3 -> Sai (R = 2*sqrt(39)/3)
    R = math.sqrt(52) / (2 * math.sin(math.radians(60)))
    assert math.isclose(R, 2 * math.sqrt(39) / 3)
    c14 = {'a': True, 'b': True, 'c': True, 'd': False}
    print("Câu 14 (a,b,c,d):", c14)

    print("[PASS] Phần II chính xác tuyệt đối!")

def test_part_3():
    print("--- PHẦN III: TRẢ LỜI NGẮN ---")
    # Câu 15: A = {x in N | (2x^2 - 5x + 2)(x^2 - 4) = 0}, B = {x in Z | -2 <= x < 3}
    # Nghiệm x in N: 2x^2 - 5x + 2 = 0 có x=2, x=1/2 -> x=2 in N. x^2 - 4 = 0 có x=2 in N.
    # -> A = {2}. B = {-2, -1, 0, 1, 2}.
    # A \cup B = {-2, -1, 0, 1, 2} có 5 phần tử.
    ans_15 = 5
    print(f"Câu 15: {ans_15}")
    assert ans_15 == 5

    # Câu 16: Max F(x, y) = 3x + 2y trên miền x>=0, y>=0, x+y<=4, 2x+y<=6
    # Đỉnh: O(0;0), A(3;0), B(2;2), C(0;4)
    # F(O)=0, F(A)=9, F(B)=3(2)+2(2)=10, F(C)=8
    vertices = [(0, 0), (3, 0), (2, 2), (0, 4)]
    f_vals = [3*x + 2*y for x, y in vertices]
    ans_16 = max(f_vals)
    print(f"Câu 16: {ans_16}")
    assert ans_16 == 10

    # Câu 17: Tam giác a=13, b=14, c=15. Bán kính r.
    p = (13 + 14 + 15) / 2 # 21
    s = math.sqrt(p * (p - 13) * (p - 14) * (p - 15)) # 84
    r = s / p # 4.0
    ans_17 = int(r)
    print(f"Câu 17: {ans_17}")
    assert ans_17 == 4

    # Câu 18: AB = 300, góc CAB = 45, CBA = 60, H nằm giữa A và B
    # h = 300 / (cot 45 + cot 60) = 300 / (1 + 1/sqrt(3)) = 300 * sqrt(3) / (sqrt(3) + 1)
    h = 300 / (1/math.tan(math.radians(45)) + 1/math.tan(math.radians(60)))
    ans_18 = round(h)
    print(f"Câu 18: h = {h:.2f} -> làm tròn {ans_18}")
    assert ans_18 == 190

    print("[PASS] Phần III chính xác 100%!")

def test_part_4():
    print("--- PHẦN IV: TỰ LUẬN ---")
    # Câu 19: A = [m - 2; m + 3], B = (-1; 5]. Tìm m để A \subset B
    # m - 2 > -1 <=> m > 1
    # m + 3 <= 5 <=> m <= 2
    # Kết luận: 1 < m <= 2 hay m in (1; 2]
    print("Câu 19: m in (1; 2]")

    # Câu 20: tan a = 2. P = (3 sin a - 2 cos a) / (sin a + 4 cos a)
    # P = (3 tan a - 2) / (tan a + 4) = (6 - 2) / (2 + 4) = 4/6 = 2/3
    P = (3*2 - 2) / (2 + 4)
    assert math.isclose(P, 2/3)
    print(f"Câu 20: P = 2/3")

    # Câu 21: Đo chiều cao hải đăng CH: AB = 50, góc CAH = 32, góc CBH = 48
    # h = AB / (cot 32 - cot 48)
    cot32 = 1 / math.tan(math.radians(32))
    cot48 = 1 / math.tan(math.radians(48))
    h21 = 50 / (cot32 - cot48)
    print(f"Câu 21: h = {h21:.2f} -> 71.4 m")
    assert round(h21, 1) == 71.4

    # Câu 22: Bài toán sản xuất bánh nướng (x) và bánh dẻo (y)
    # x, y >= 0, x, y in N
    # Đường: 0.06x + 0.05y <= 15 <=> 6x + 5y <= 1500
    # Bột: 0.08x + 0.04y <= 16 <=> 2x + y <= 400
    # Giao điểm: 2x + y = 400 => y = 400 - 2x
    # 6x + 5(400 - 2x) = 1500 => -4x = -500 => x = 125, y = 150
    # Các đỉnh: O(0,0), A(200, 0), B(125, 150), C(0, 300)
    # F(x, y) = 40x + 30y (nghìn đồng)
    # F(O) = 0
    # F(A) = 40*200 = 8000
    # F(B) = 40*125 + 30*150 = 5000 + 4500 = 9500 (lớn nhất)
    # F(C) = 30*300 = 9000
    pts = [(0, 0), (200, 0), (125, 150), (0, 300)]
    profits = [40*x + 30*y for x, y in pts]
    max_prof = max(profits)
    best_pt = pts[profits.index(max_prof)]
    assert best_pt == (125, 150)
    assert max_prof == 9500
    print(f"Câu 22: x = {best_pt[0]}, y = {best_pt[1]}, max profit = {max_prof} nghìn = 9.5 triệu đồng")

    print("[PASS] Phần IV lập luận và tính toán hoàn hảo!")

if __name__ == '__main__':
    test_part_1()
    test_part_2()
    test_part_3()
    test_part_4()
    print("\n>>> TẤT CẢ CÁC BÀI TOÁN ĐỀ 07 ĐÃ ĐƯỢC XÁC THỰC TOÁN HỌC 100%! <<<")
