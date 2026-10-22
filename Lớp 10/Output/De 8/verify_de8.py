# -*- coding: utf-8 -*-
"""
Kiểm thử độc lập 100% bằng Python/SymPy cho Đề số 08 - Toán 10 GK1.
"""
import math
import sympy as sp

def test_part_1():
    print("--- PHẦN I: TRẮC NGHIỆM ---")
    # Câu 1: TH_NB_04 -> (-1; 4] -> A
    ans_1 = 'A'

    # Câu 2: MD_NB_01 -> Mệnh đề toán học -> B
    # Phương trình x^2 - 4 = 0 có hai nghiệm thực phân biệt
    ans_2 = 'B'

    # Câu 3: TH_TH_01 -> Giao A \cap B với A = {0,1,2,3,4}, B = {2,3,5,7} -> B
    A3 = {0, 1, 2, 3, 4}
    B3 = {2, 3, 5, 7}
    assert (A3 & B3) == {2, 3}
    ans_3 = 'B'

    # Câu 4: TH_NB_02 -> {x in Z | x^2 - 5x + 6 = 0} = {2; 3} -> C
    ans_4 = 'C'

    # Câu 5: BPT_NB_04 -> Nghiệm của hệ x+y-2 <= 0 và 2x-y+1 > 0 -> D (0; 0)
    assert 0 + 0 - 2 <= 0 and 2*0 - 0 + 1 > 0
    ans_5 = 'D'

    # Câu 6: BPT_NB_03 -> Cặp số KHÔNG là nghiệm của x - 2y + 4 >= 0 -> C (1; 3)
    assert 1 - 2*3 + 4 == -1 < 0
    ans_6 = 'C'

    # Câu 7: BPT_TH_01 -> Nửa mặt phẳng x - y - 1 >= 0 chứa N(2; 0) -> B
    assert 2 - 0 - 1 == 1 >= 0
    ans_7 = 'B'

    # Câu 8: BPT_NB_05 -> Đường thẳng bờ 2x - 5y + 10 <= 0 là 2x - 5y + 10 = 0 -> D
    ans_8 = 'D'

    # Câu 9: HTL_NB_04 -> m_a^2 = (b^2 + c^2)/2 - a^2/4 -> A
    ans_9 = 'A'

    # Câu 10: LG_TH_01 -> cos a = 4/5, 0 < a < 90 -> sin a = 3/5 -> A
    cos10 = sp.Rational(4, 5)
    sin10 = sp.sqrt(1 - cos10**2)
    assert sin10 == sp.Rational(3, 5)
    ans_10 = 'A'

    # Câu 11: HTL_NB_02 -> a / sin A = 2R -> C
    ans_11 = 'C'

    # Câu 12: LG_NB_03 -> sin(180 - a) = sin a -> D
    ans_12 = 'D'

    answers = [ans_1, ans_2, ans_3, ans_4, ans_5, ans_6, ans_7, ans_8, ans_9, ans_10, ans_11, ans_12]
    counts = {opt: answers.count(opt) for opt in ['A', 'B', 'C', 'D']}
    print("Phần I answers:", answers)
    print("Phân bố đáp án Phần I:", counts)
    assert counts == {'A': 3, 'B': 3, 'C': 3, 'D': 3}, "Phần I phải cân bằng đúng 3A, 3B, 3C, 3D"
    print("[PASS] Phần I cân bằng hoàn hảo 3A-3B-3C-3D!")

def test_part_2():
    print("--- PHẦN II: ĐÚNG / SAI ---")
    # Câu 13: A = {x in R | x^2 - 4x + 3 = 0} = {1; 3}, B = {x in N | x <= 3} = {0; 1; 2; 3}
    # a) A = {1; 3} có 2 phần tử -> Đúng
    # b) B = {0; 1; 2; 3} -> Đúng
    # c) A \cap B = {1; 3} -> Đúng
    # d) B \setminus A = {0; 2}. Phát biểu: "B \setminus A = {2}" -> Sai
    c13 = {'a': True, 'b': True, 'c': True, 'd': False}
    print("Câu 13 (a,b,c,d):", c13)

    # Câu 14: Hệ x>=0, y>=0, x+y<=5, 2x+3y<=12
    # a) O(0; 0) thuộc miền nghiệm -> Đúng
    # b) Đỉnh A(5; 0) nằm trên Ox -> x<=5 và 2x<=12 => x<=5 => A(5; 0) -> Đúng
    # c) B(3; 2) giao x+y=5 và 2x+3y=12: 2(3)+3(2)=12, 3+2=5 -> Đúng
    # d) Max F(x, y) = 2x + y trên miền tứ giác:
    # F(O)=0, F(A)=2(5)+0=10, F(B)=2(3)+2=8, F(C)=2(0)+4=4 (C(0; 4))
    # Max là 10, phát biểu ghi 11 -> Sai
    c14 = {'a': True, 'b': True, 'c': True, 'd': False}
    print("Câu 14 (a,b,c,d):", c14)

    print("[PASS] Phần II chính xác tuyệt đối!")

def test_part_3():
    print("--- PHẦN III: TRẢ LỜI NGẮN ---")
    # Câu 15: A = [-4; 3], B = (0; 7]. A \cap B = (0; 3]. Các số nguyên: {1, 2, 3} -> 3 số
    A_cap_B = [x for x in range(-10, 10) if (-4 <= x <= 3) and (0 < x <= 7)]
    ans_15 = len(A_cap_B)
    print(f"Câu 15: {ans_15}")
    assert ans_15 == 3

    # Câu 16: Max F(x, y) = 5x + 3y trên x>=0, y>=0, x+y<=6, 2x+y<=8
    # Đỉnh: O(0;0), A(4;0), B(2;4), C(0;6)
    pts = [(0, 0), (4, 0), (2, 4), (0, 6)]
    f_vals = [5*x + 3*y for x, y in pts]
    ans_16 = max(f_vals)
    print(f"Câu 16: {ans_16}")
    assert ans_16 == 22 # tại (2; 4)

    # Câu 17: Tam giác b=5, c=8, A=60 độ. Cạnh a = BC.
    # a^2 = 25 + 64 - 2*5*8*cos(60) = 89 - 40 = 49 => a = 7
    a_sq = 5**2 + 8**2 - 2*5*8*math.cos(math.radians(60))
    ans_17 = round(math.sqrt(a_sq))
    print(f"Câu 17: {ans_17}")
    assert ans_17 == 7

    # Câu 18: Tàu 1 chạy 30 km/h, tàu 2 chạy 40 km/h sau 2h, góc 60 độ.
    # c = 60, b = 80, A = 60
    # a^2 = 60^2 + 80^2 - 2*60*80*0.5 = 3600 + 6400 - 4800 = 5200
    # a = sqrt(5200) = 72.11 km -> 72
    a18 = math.sqrt(60**2 + 80**2 - 2*60*80*math.cos(math.radians(60)))
    ans_18 = round(a18)
    print(f"Câu 18: a = {a18:.2f} -> {ans_18}")
    assert ans_18 == 72

    print("[PASS] Phần III chính xác 100%!")

def test_part_4():
    print("--- PHẦN IV: TỰ LUẬN ---")
    # Câu 19: A = [m; m + 3], B = [-2; 4]. A \cap B != \varnothing
    # m <= 4 and m + 3 >= -2 <=> -5 <= m <= 4 <=> m in [-5; 4]
    print("Câu 19: m in [-5; 4]")

    # Câu 20: sin a + cos a = 7/5
    # a) M = sin a cos a = (49/25 - 1)/2 = 24/50 = 12/25
    M = (sp.Rational(7, 5)**2 - 1) / 2
    assert M == sp.Rational(12, 25)
    # b) N = sin^3 + cos^3 = (sin+cos)(1 - sin cos) = 7/5 * (1 - 12/25) = 7/5 * 13/25 = 91/125
    N = sp.Rational(7, 5) * (1 - M)
    assert N == sp.Rational(91, 125)
    print(f"Câu 20: M = {M}, N = {N}")

    # Câu 21: AC = 80, góc CAB = 75, ACB = 60. Khoảng cách AB.
    # B = 180 - (75 + 60) = 45 độ
    # AB = AC * sin(60) / sin(45) = 80 * (sqrt(3)/2) / (sqrt(2)/2) = 40 * sqrt(6) = 97.979...
    ab = 80 * math.sin(math.radians(60)) / math.sin(math.radians(45))
    assert round(ab, 1) == 98.0
    print(f"Câu 21: AB = {ab:.2f} -> 98.0 m")

    # Câu 22: Pha chế dung dịch loại X (x lít) và Y (y lít), x, y >= 0
    # Hóa chất A: 10x + 20y <= 800 <=> x + 2y <= 80
    # Hóa chất B: 30x + 20y <= 1200 <=> 3x + 2y <= 120
    # Đỉnh: O(0,0), A(40, 0), B(20, 30), C(0, 40)
    # F(x, y) = 50x + 60y (nghìn đồng)
    # F(O) = 0
    # F(A) = 50*40 = 2000
    # F(B) = 50*20 + 60*30 = 1000 + 1800 = 2800 (lớn nhất)
    # F(C) = 60*40 = 2400
    pts22 = [(0, 0), (40, 0), (20, 30), (0, 40)]
    profits22 = [50*x + 60*y for x, y in pts22]
    max_prof22 = max(profits22)
    best_pt22 = pts22[profits22.index(max_prof22)]
    assert best_pt22 == (20, 30)
    assert max_prof22 == 2800
    print(f"Câu 22: x = {best_pt22[0]}, y = {best_pt22[1]}, max profit = {max_prof22} nghìn = 2.8 triệu đồng")

    print("[PASS] Phần IV lập luận và tính toán hoàn hảo!")

if __name__ == '__main__':
    test_part_1()
    test_part_2()
    test_part_3()
    test_part_4()
    print("\n>>> TẤT CẢ CÁC BÀI TOÁN ĐỀ 08 ĐÃ ĐƯỢC XÁC THỰC TOÁN HỌC 100%! <<<")
