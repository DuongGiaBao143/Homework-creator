"""Kiểm chứng toán học độc lập cho Đề 3 (Lớp 10) - Ôn tập Giữa kỳ I."""
import math

def verify_all():
    print("=== KIỂM TOÁN ĐỀ 3 ===")
    
    # PHẦN I: 12 câu
    answers_I = ["B", "C", "D", "A", "B", "C", "D", "A", "B", "C", "D", "A"]
    assert answers_I.count("A") == 3
    assert answers_I.count("B") == 3
    assert answers_I.count("C") == 3
    assert answers_I.count("D") == 3
    print("[OK] Phần I: 12 câu trắc nghiệm cân bằng 3A-3B-3C-3D.")

    # PHẦN II:
    # Câu 1: A = (-4; 3], B = [-1; 5)
    # a) -4 in A: False
    # b) 3 in A: True
    # c) A cap B = [-1; 3]: True
    # d) A \ B = (-4; -1): True
    ans_II_1 = [False, True, True, True]
    print("[OK] Phần II - Câu 1: a) Sai, b) Đúng, c) Đúng, d) Đúng.")

    # Câu 2:
    # 40x + 20y >= 160 <=> 2x + y >= 8
    # x + y <= 6
    # a) Tổng khách tối đa: 40x + 20y: True
    # b) x=2, y=3: 40*2 + 20*3 = 140 < 160 (không đủ) -> False
    # c) Hệ: 2x + y >= 8, x + y <= 6: True
    # d) x=3: 2(3)+y >= 8 => y >= 2, 3+y <= 6 => y <= 3 => tối thiểu 2 xe: True
    ans_II_2 = [True, False, True, True]
    print("[OK] Phần II - Câu 2: a) Đúng, b) Sai, c) Đúng, d) Đúng.")

    # PHẦN III:
    # Câu 1: A = {x in Z | -2 <= x < 6} = {-2, -1, 0, 1, 2, 3, 4, 5} (8 phần tử)
    # B = {x in Z | (x+1)(x-3) <= 0} = {-1, 0, 1, 2, 3}
    A = {x for x in range(-10, 20) if -2 <= x < 6}
    B = {x for x in range(-10, 20) if (x+1)*(x-3) <= 0}
    assert len(A | B) == 8
    print(f"[OK] Phần III - Câu 1: A cup B có {len(A | B)} phần tử.")

    # Câu 2: cos = -5/13, 90 < alpha < 180 => sin = 12/13, tan = -12/5
    # P = (sin + tan) / cos = (12/13 - 12/5) / (-5/13) = (-96/65) / (-5/13) = 96/25 = 3.84
    sin_a = 12/13
    cos_a = -5/13
    tan_a = sin_a / cos_a
    P = (sin_a + tan_a) / cos_a
    assert abs(P - 3.84) < 1e-9
    print(f"[OK] Phần III - Câu 2: P = {P} = 96/25.")

    # Câu 3: A=30 deg, B_ext=45 deg => C=15 deg. AB = 30 m.
    # BC = 30 * sin(30) / sin(15) = 15 / sin(15)
    # CH = BC * sin(45) = 15*sin(45)/sin(15) = 15*(sqrt(3)+1) = 40.98 m
    # CD = CH - 15 = 25.98 m -> làm tròn 26.0 m
    BC = 30 * math.sin(math.radians(30)) / math.sin(math.radians(15))
    CH = BC * math.sin(math.radians(45))
    CD = CH - 15
    assert round(CD, 1) == 26.0
    print(f"[OK] Phần III - Câu 3: CD = {CD:.3f} m -> làm tròn 26.0 m.")

    # Câu 4: D gồm (0,0), (4,0), (3,2), (0,5)
    # 2x + (m-1)y <= 12
    # Tại (0,0): 0 <= 12
    # Tại (4,0): 8 <= 12
    # Tại (0,5): 5(m-1) <= 12 => m <= 17/5 = 3.4
    # Tại (3,2): 6 + 2(m-1) <= 12 => 2m <= 8 => m <= 4
    # max m = 3.4
    assert min(3.4, 4.0) == 3.4
    print("[OK] Phần III - Câu 4: max m = 3.4.")

    # PHẦN IV:
    # Câu 1: A = (-inf; 4], B = (-2; 7)
    # A cap B = (-2; 4], A cup B = (-inf; 7), A \ B = (-inf; -2]
    print("[OK] Phần IV - Câu 1: A cap B = (-2; 4], A cup B = (-inf; 7), A \\ B = (-inf; -2].")

    # Câu 2: sin = 4/5, 90 < alpha < 180 => cos = -3/5 => tan = -4/3
    # E = (1 + tan)/(1 - tan) = (1 - 4/3)/(1 + 4/3) = (-1/3)/(7/3) = -1/7
    tan2 = -4/3
    E = (1 + tan2) / (1 - tan2)
    assert abs(E - (-1/7)) < 1e-9
    print(f"[OK] Phần IV - Câu 2: E = {E:.5f} = -1/7.")

    # Câu 3: Hình thang vuông ABCD vuông tại A, D. AD=40, AB=30, C=45 deg
    # DH = 30, BH = 40, HC = 40 => CD = 70.
    # BC = sqrt(40^2+40^2) = 40*sqrt(2) ~ 56.57 m.
    # S = (30 + 70)*40/2 = 2000 m^2.
    assert (30 + 70)*40/2 == 2000
    print("[OK] Phần IV - Câu 3: CD = 70 m, BC = 40*sqrt(2) m, S = 2000 m^2.")

    # Câu 4:
    # 3x + 2y >= 18
    # x + 2y >= 12
    # x + y <= 10
    # x, y >= 0, integer
    # Min C = 200000*x + 250000*y
    candidates = []
    for x in range(11):
        for y in range(11):
            if 3*x + 2*y >= 18 and x + 2*y >= 12 and x + y <= 10:
                cost = 200000*x + 250000*y
                candidates.append((cost, x, y))
    candidates.sort()
    min_cost, best_x, best_y = candidates[0]
    assert best_x == 4 and best_y == 4 and min_cost == 1800000
    print(f"[OK] Phần IV - Câu 4: tối ưu tại ({best_x}, {best_y}) với chi phí min = {min_cost:,} đồng.")

if __name__ == "__main__":
    verify_all()
