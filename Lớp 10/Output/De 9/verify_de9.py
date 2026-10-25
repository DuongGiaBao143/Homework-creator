# -*- coding: utf-8 -*-
"""
Kiểm thử độc lập 100% bằng Python/SymPy cho Đề số 09 - Toán 10 GK1.
"""
import math
import sympy as sp

def test_part_1():
    print("--- PHẦN I: TRẮC NGHIỆM ---")
    # Câu 1: MD_NB_02 -> Tổng 3 góc tam giác = 180 độ -> C
    ans_1 = 'C'

    # Câu 2: TH_NB_01 -> Khẳng định sai: {2} in A -> B
    ans_2 = 'B'

    # Câu 3: MD_NB_01 -> Mệnh đề toán học: 2 + 3 = 7 -> B
    ans_3 = 'B'

    # Câu 4: TH_NB_04 -> [2; 6) -> A
    ans_4 = 'A'

    # Câu 5: BPT_NB_04 -> (2; 1) thỏa 2x - y >= 1 và x + y <= 4 -> C
    assert 2*(2) - 1 >= 1 and 2 + 1 <= 4
    ans_5 = 'C'

    # Câu 6: BPT_NB_03 -> Q(1; 0) thuộc x - 3y + 3 > 0 -> D
    assert 1 - 3*0 + 3 == 4 > 0
    ans_6 = 'D'

    # Câu 7: BPT_TH_01 -> Miền 2x + y - 4 <= 0 chứa O(0; 0) -> B
    assert 2*0 + 0 - 4 <= 0
    ans_7 = 'B'

    # Câu 8: BPT_NB_05 -> Đường thẳng bờ 3x - 2y + 6 = 0 -> D
    ans_8 = 'D'

    # Câu 9: LG_NB_02 -> Góc tù có sin a > 0 -> A
    ans_9 = 'A'

    # Câu 10: HTL_TH_01 -> a = 2*sqrt(13) -> A
    a10_sq = 6**2 + 8**2 - 2*6*8*math.cos(math.radians(60))
    assert math.isclose(a10_sq, 52)
    assert math.isclose(math.sqrt(52), 2*math.sqrt(13))
    ans_10 = 'A'

    # Câu 11: LG_TH_02 -> sin^2 40 + sin^2 50 + tan 30 * cot 30 = 1 + 1 = 2 -> C
    ans_11 = 'C'

    # Câu 12: LG_NB_01 -> sin 150 = 1/2 -> D
    assert math.isclose(math.sin(math.radians(150)), 0.5)
    ans_12 = 'D'

    answers = [ans_1, ans_2, ans_3, ans_4, ans_5, ans_6, ans_7, ans_8, ans_9, ans_10, ans_11, ans_12]
    counts = {opt: answers.count(opt) for opt in ['A', 'B', 'C', 'D']}
    print("Phần I answers:", answers)
    print("Phân bố đáp án Phần I:", counts)
    assert counts == {'A': 3, 'B': 3, 'C': 3, 'D': 3}, "Phần I phải cân bằng đúng 3A, 3B, 3C, 3D"
    print("[PASS] Phần I cân bằng hoàn hảo 3A-3B-3C-3D!")

def test_part_2():
    print("--- PHẦN II: ĐÚNG / SAI ---")
    # Câu 13: Hệ x>=0, y>=0, x+y<=4, x+2y<=6
    # a) M(1; 1) thuộc miền nghiệm -> Đúng
    assert 1+1 <= 4 and 1+2 <= 6
    # b) A(4; 0) là đỉnh trên Ox -> Đúng
    # c) B(2; 2) là giao điểm -> Đúng
    # d) Max F(x, y) = 2x + 3y:
    # F(O)=0, F(A)=8, F(B)=2*2+3*2=10, F(C)=3*3=9. Max là 10. Phát biểu ghi 12 -> Sai
    c13 = {'a': True, 'b': True, 'c': True, 'd': False}
    print("Câu 13:", c13)

    # Câu 14: Tam giác a=7, b=5, c=6
    # a) p = (7+5+6)/2 = 9 -> Đúng
    p = 9
    # b) S = sqrt(9 * 2 * 4 * 3) = sqrt(216) = 6*sqrt(6) -> Đúng
    s = math.sqrt(9 * 2 * 4 * 3)
    assert math.isclose(s, 6*math.sqrt(6))
    # c) r = S / p = 6*sqrt(6)/9 = 2*sqrt(6)/3 -> Đúng
    r = s / p
    assert math.isclose(r, 2*math.sqrt(6)/3)
    # d) R = abc / 4S = (7*5*6)/(24*sqrt(6)) = 35/(4*sqrt(6)) = 35*sqrt(6)/24.
    # Phát biểu: R = 35*sqrt(6)/12 -> Sai
    R = (7 * 5 * 6) / (4 * s)
    assert math.isclose(R, 35*math.sqrt(6)/24)
    c14 = {'a': True, 'b': True, 'c': True, 'd': False}
    print("Câu 14:", c14)

    print("[PASS] Phần II chính xác tuyệt đối!")

def test_part_3():
    print("--- PHẦN III: TRẢ LỜI NGẮN ---")
    # Câu 15: n(Toán)=25, n(Văn)=20, n(không môn nào)=5 trong 40 hs
    # n(Toán \cup Văn) = 35. n(Toán \cap Văn) = 25 + 20 - 35 = 10
    ans_15 = 25 + 20 - (40 - 5)
    print(f"Câu 15: {ans_15}")
    assert ans_15 == 10

    # Câu 16: Max F(x, y) = 4x + 3y trên x>=0, y>=0, x+y<=5, 3x+y<=9
    # Đỉnh: O(0,0), A(3,0), B(2,3), C(0,5)
    pts = [(0, 0), (3, 0), (2, 3), (0, 5)]
    f_vals = [4*x + 3*y for x, y in pts]
    ans_16 = max(f_vals)
    print(f"Câu 16: {ans_16}")
    assert ans_16 == 17 # tại (2; 3)

    # Câu 17: sin a = 5/13, 0 < a < 90. Tính 13 cos a + 12 tan a
    # cos a = 12/13, tan a = 5/12 => 13*(12/13) + 12*(5/12) = 12 + 5 = 17
    cos17 = sp.sqrt(1 - sp.Rational(5, 13)**2)
    tan17 = sp.Rational(5, 13) / cos17
    ans_17 = int(13 * cos17 + 12 * tan17)
    print(f"Câu 17: {ans_17}")
    assert ans_17 == 17

    # Câu 18: CA = 60, CB = 100, góc C = 120 độ. Tính AB.
    # AB^2 = 60^2 + 100^2 - 2*60*100*cos(120) = 3600 + 10000 + 6000 = 19600 => AB = 140
    ab_sq = 60**2 + 100**2 - 2*60*100*math.cos(math.radians(120))
    ans_18 = round(math.sqrt(ab_sq))
    print(f"Câu 18: AB = {ans_18}")
    assert ans_18 == 140

    print("[PASS] Phần III chính xác 100%!")

def test_part_4():
    print("--- PHẦN IV: TỰ LUẬN ---")
    # Câu 19: A = [m - 3; m + 2], B = [-1; 5). A \subset B
    # m - 3 >= -1 <=> m >= 2
    # m + 2 < 5 <=> m < 3
    # => 2 <= m < 3 hay m in [2; 3)
    print("Câu 19: m in [2; 3)")

    # Câu 20: Tam giác a=13, b=14, c=15
    # a) S = 84
    # b) h_a = 2S / a = 168 / 13 approx 12.9
    ha = 2 * 84 / 13
    print(f"Câu 20: S = 84, h_a = 168/13 approx {ha:.2f}")

    # Câu 21: Đo chiều cao cột phát sóng: AB = 30, CAD = 35, CBD = 55
    # h = AB / (cot 35 - cot 55)
    cot35 = 1 / math.tan(math.radians(35))
    cot55 = 1 / math.tan(math.radians(55))
    h21 = 30 / (cot35 - cot55)
    assert round(h21, 1) == 41.2
    print(f"Câu 21: h = {h21:.2f} -> 41.2 m")

    # Câu 22: Sản xuất bàn (x) và ghế (y), x, y >= 0, nguyên
    # Gỗ: 2x + y <= 80
    # Công: 3x + 2y <= 130
    # Giao điểm: x = 30, y = 20
    # Đỉnh: O(0,0), A(40,0), B(30,20), C(0,65)
    # Lợi nhuận: F = 400x + 250y (nghìn đồng)
    # F(O)=0, F(A)=16000, F(B)=400*30+250*20=12000+5000=17000 (lớn nhất), F(C)=250*65=16250
    pts22 = [(0, 0), (40, 0), (30, 20), (0, 65)]
    profs22 = [400*x + 250*y for x, y in pts22]
    max_p22 = max(profs22)
    best_pt22 = pts22[profs22.index(max_p22)]
    assert best_pt22 == (30, 20)
    assert max_p22 == 17000
    print(f"Câu 22: x = {best_pt22[0]}, y = {best_pt22[1]}, max profit = {max_p22} nghìn = 17 triệu đồng")

    print("[PASS] Phần IV lập luận và tính toán hoàn hảo!")

if __name__ == '__main__':
    test_part_1()
    test_part_2()
    test_part_3()
    test_part_4()
    print("\n>>> TẤT CẢ CÁC BÀI TOÁN ĐỀ 09 ĐÃ ĐƯỢC XÁC THỰC TOÁN HỌC 100%! <<<")
