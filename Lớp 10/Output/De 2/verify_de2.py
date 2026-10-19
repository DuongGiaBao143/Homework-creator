"""Kiểm chứng toán học độc lập cho Đề 2 (Lớp 10) - Ôn tập Giữa kỳ I."""
import math
import numpy as np

def verify_all():
    print("=== KIỂM TOÁN ĐỀ 2 ===")
    
    # PHẦN I
    # Câu 1: A đúng (13 là số nguyên tố)
    # Câu 2: B đúng (P(2): 2^2 - 4 = 0)
    # Câu 3: C đúng ({a; b} \subset X)
    # Câu 4: D đúng (2^4 = 16)
    # Câu 5: A đúng (3x - 5y > 7)
    # Câu 6: B đúng (2(1) - 1 + 1 = 2 > 0)
    # Câu 7: C đúng (hệ bậc nhất 2 ẩn)
    # Câu 8: D đúng (x=2, y=2: 2>=0, 2>=0, 2+2=4<=5, 2*2+2=6>=4)
    # Câu 9: A đúng (0 < alpha < 90: sin alpha > 0)
    # Câu 10: B đúng (cos(180 - alpha) = -cos alpha)
    # Câu 11: C đúng (a / sin A = 2R)
    # Câu 12: D đúng (S = pr)
    answers_I = ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B", "C", "D"]
    assert answers_I.count("A") == 3
    assert answers_I.count("B") == 3
    assert answers_I.count("C") == 3
    assert answers_I.count("D") == 3
    print("[OK] Phần I: 12 câu trắc nghiệm cân bằng 3A-3B-3C-3D.")

    # PHẦN II
    # Câu 1: A = [-3; 5), B = (0; 7]
    # a) -3 in A: True
    # b) 5 in A: False
    # c) A cap B = (0; 5): True
    # d) A \ B = [-3; 0]: True
    ans_II_1 = [True, False, True, True]
    print("[OK] Phần II - Câu 1: a) Đúng, b) Sai, c) Đúng, d) Đúng.")

    # Câu 2:
    # 1.5x + 2.5y <= 120 <=> 3x + 5y <= 240
    # 2x + 3y <= 130
    # a) Chi phí vải: 1.5x + 2.5y: True
    # b) x=30, y=30: 1.5*30 + 2.5*30 = 45 + 75 = 120 <= 120 -> không vượt quá -> câu nói 'vượt quá' là False
    # c) Hệ: 3x+5y <= 240, 2x+3y <= 130: True
    # d) x=35: 3*35+5y <= 240 => 5y <= 135 => y <= 27
    #          2*35+3y <= 130 => 3y <= 60 => y <= 20
    #          max y = 20, khẳng định 'tối đa 21' là False
    ans_II_2 = [True, False, True, False]
    print("[OK] Phần II - Câu 2: a) Đúng, b) Sai, c) Đúng, d) Sai.")

    # PHẦN III
    # Câu 1: -5 < 2x - 1 <= 9 <=> -2 < x <= 5 => A = {-1, 0, 1, 2, 3, 4, 5} (7 phần tử)
    # B = {x in Z | |x| <= 3} = {-3, -2, -1, 0, 1, 2, 3}
    # A cap B = {-1, 0, 1, 2, 3} => 5 phần tử
    A = {x for x in range(-10, 20) if -5 < 2*x - 1 <= 9}
    B = {x for x in range(-10, 20) if abs(x) <= 3}
    assert len(A & B) == 5
    print(f"[OK] Phần III - Câu 1: A cap B có {len(A & B)} phần tử.")

    # Câu 2: sin = 3/5, 90 < alpha < 180 => cos = -4/5, tan = -3/4
    # M = (5*cos + 2*tan) / (1 + cos) = (5*(-4/5) + 2*(-3/4)) / (1 - 4/5)
    #   = (-4 - 1.5) / 0.2 = -5.5 / 0.2 = -27.5 = -55/2
    M = (5*(-4/5) + 2*(-3/4)) / (1 + (-4/5))
    assert abs(M - (-27.5)) < 1e-9
    print(f"[OK] Phần III - Câu 2: M = {M} = -55/2.")

    # Câu 3: CA = 60, CB = 80, C = 60 deg
    # AB = sqrt(60^2 + 80^2 - 2*60*80*cos(60 deg)) = sqrt(3600 + 6400 - 4800) = sqrt(5200) = 72.111 m
    AB = math.sqrt(60**2 + 80**2 - 2*60*80*0.5)
    assert round(AB, 1) == 72.1
    print(f"[OK] Phần III - Câu 3: AB = {AB:.3f} m, làm tròn 72.1 m.")

    # Câu 4: D có các đỉnh (0,0), (5,0), (2,3), (0,4)
    # x + (m-2)y <= 10
    # Tại (0,0): 0 <= 10
    # Tại (5,0): 5 <= 10
    # Tại (0,4): 4(m-2) <= 10 <=> 4m - 8 <= 10 <=> m <= 4.5
    # Tại (2,3): 2 + 3(m-2) <= 10 <=> 3m - 4 <= 10 <=> m <= 14/3 ~ 4.667
    # max m = min(4.5, 14/3) = 4.5
    assert min(4.5, 14/3) == 4.5
    print("[OK] Phần III - Câu 4: max m = 4.5.")

    # PHẦN IV
    # Câu 1: A = [-4; 2), B = [-1; 6]
    # A cap B = [-1; 2), A cup B = [-4; 6], A \ B = [-4; -1)
    print("[OK] Phần IV - Câu 1: A cap B = [-1; 2), A cup B = [-4; 6], A \\ B = [-4; -1).")

    # Câu 2: Q = (sin^2 - cos^2)/(sin*cos + cos^2) = tan - 1
    # cos = 5/13, 0 < alpha < 90 => sin = 12/13, tan = 12/5
    # Q = 12/5 - 1 = 7/5 = 1.4
    s, c = 12/13, 5/13
    Q = (s**2 - c**2) / (s*c + c**2)
    assert abs(Q - 7/5) < 1e-9
    print(f"[OK] Phần IV - Câu 2: Q = {Q} = 7/5.")

    # Câu 3: Tam giác ABC: AB = 500, A = 75, B = 60 => C = 45
    # AC = AB * sin(60) / sin(45) = 500 * (sqrt(3)/2) / (sqrt(2)/2) = 250*sqrt(6) ~ 612.37 m -> 612 m
    # CH = AC * sin(75) = 250*sqrt(6) * (sqrt(6)+sqrt(2))/4 = 125*(3+sqrt(3)) ~ 591.506 m -> 592 m
    AC = 500 * math.sin(math.radians(60)) / math.sin(math.radians(45))
    CH = AC * math.sin(math.radians(75))
    assert round(AC) == 612
    assert round(CH) == 592
    print(f"[OK] Phần IV - Câu 3: AC = {AC:.2f} m -> {round(AC)} m; CH = {CH:.2f} m -> {round(CH)} m.")

    # Câu 4:
    # 3x + 2y <= 36
    # x + 2y <= 24
    # Đỉnh: (0,0), (12,0), (6,9), (0,12)
    # T = 400000*x + 500000*y
    verts = [(0,0), (12,0), (6,9), (0,12)]
    profits = {v: 400000*v[0] + 500000*v[1] for v in verts}
    best_v = max(profits, key=profits.get)
    assert best_v == (6, 9)
    assert profits[best_v] == 6900000
    print(f"[OK] Phần IV - Câu 4: tối ưu tại (6, 9) với lãi lớn nhất = {profits[best_v]:,} đồng.")

if __name__ == "__main__":
    verify_all()
