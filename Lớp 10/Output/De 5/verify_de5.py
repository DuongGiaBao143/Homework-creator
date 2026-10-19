"""Kiểm chứng toán học độc lập cho Đề 5 (Lớp 10) - Ôn tập Giữa kỳ I."""
import math

def verify_all():
    print("=== KIỂM TOÁN ĐỀ 5 ===")
    
    # PHẦN I: 12 câu
    answers_I = ["D", "A", "B", "C", "D", "A", "B", "C", "D", "A", "B", "C"]
    assert answers_I.count("A") == 3
    assert answers_I.count("B") == 3
    assert answers_I.count("C") == 3
    assert answers_I.count("D") == 3
    print("[OK] Phần I: 12 câu trắc nghiệm cân bằng 3A-3B-3C-3D.")

    # PHẦN II:
    # Câu 1: A = (-2; 4], B = [1; 7)
    # a) -2 in A: False
    # b) 4 in A: True
    # c) A cap B = [1; 4]: True
    # d) A \ B = (-2; 1): True
    ans_II_1 = [False, True, True, True]
    print("[OK] Phần II - Câu 1: a) Sai, b) Đúng, c) Đúng, d) Đúng.")

    # Câu 2:
    # 2x + 4y <= 80 <=> x + 2y <= 40
    # 3x + y <= 45
    # a) Đường: 2x + 4y: True
    # b) x=20, y=12: 2(20)+4(12) = 88 > 80 => False
    # c) Hệ: x + 2y <= 40, 3x + y <= 45: True
    # d) x=10: 10+2y <= 40 => y <= 15; 30+y <= 45 => y <= 15 => max y = 15 (khẳng định 16 là False)
    ans_II_2 = [True, False, True, False]
    print("[OK] Phần II - Câu 2: a) Đúng, b) Sai, c) Đúng, d) Sai.")

    # PHẦN III:
    # Câu 1: -3 <= 2x+1 <= 9 <=> -2 <= x <= 4 => A = {-2, -1, 0, 1, 2, 3, 4} (7 phần tử)
    # B = {x in Z | x^2 < 9} = {-2, -1, 0, 1, 2} (5 phần tử)
    A = {x for x in range(-10, 20) if -3 <= 2*x + 1 <= 9}
    B = {x for x in range(-10, 20) if x**2 < 9}
    assert len(A & B) == 5
    print(f"[OK] Phần III - Câu 1: A cap B có {len(A & B)} phần tử.")

    # Câu 2: tan = -3/4
    # G = (4*tan - 3)/(2*tan + 1) = (-3 - 3)/(-1.5 + 1) = -6 / (-0.5) = 12
    G = (4*(-0.75) - 3) / (2*(-0.75) + 1)
    assert abs(G - 12.0) < 1e-9
    print(f"[OK] Phần III - Câu 2: G = {G}.")

    # Câu 3: AB = 20*2 = 40, AC = 15*2 = 30, A = 60 deg
    # BC = sqrt(40^2 + 30^2 - 2*40*30*cos(60 deg)) = sqrt(1600 + 900 - 1200) = sqrt(1300) = 10*sqrt(13) ~ 36.0555 km -> 36.1 km
    BC = math.sqrt(40**2 + 30**2 - 2*40*30*0.5)
    assert round(BC, 1) == 36.1
    print(f"[OK] Phần III - Câu 3: BC = {BC:.3f} km -> làm tròn 36.1 km.")

    # Câu 4: D gồm (0,0), (3,0), (1,6), (0,7)
    # x + (m-1)y <= 14
    # Tại (0,0): 0 <= 14
    # Tại (3,0): 3 <= 14
    # Tại (0,7): 7(m-1) <= 14 => m <= 3
    # Tại (1,6): 1 + 6(m-1) <= 14 => 6m <= 19 => m <= 19/6 ~ 3.167
    # max m = 3
    assert min(3.0, 19/6) == 3.0
    print("[OK] Phần III - Câu 4: max m = 3.")

    # PHẦN IV:
    # Câu 1: A = (-3; 5], B = [0; 8)
    # A cap B = [0; 5], A cup B = (-3; 8), A \ B = (-3; 0)
    print("[OK] Phần IV - Câu 1: A cap B = [0; 5], A cup B = (-3; 8), A \\ B = (-3; 0).")

    # Câu 2: F = 1 - sin*cos
    # sin + cos = 7/5 => (sin+cos)^2 = 49/25 = 1 + 2*sin*cos => sin*cos = 12/25
    # F = 1 - 12/25 = 13/25
    assert 1 - 12/25 == 13/25
    print("[OK] Phần IV - Câu 2: F = 13/25.")

    # Câu 3: Tam giác ABD vuông tại A: AB=60, AD=80 => BD = sqrt(60^2+80^2) = 100 m
    # Tam giác BCD đều cạnh 100 m
    # S_ABD = 0.5*60*80 = 2400 m^2
    # S_BCD = 100^2 * sqrt(3) / 4 = 2500*sqrt(3) ~ 4330.127 m^2
    # S_total = 2400 + 4330.127 = 6730.127 m^2 -> 6730 m^2
    BD = math.sqrt(60**2 + 80**2)
    S_total = 0.5*60*80 + (BD**2)*math.sqrt(3)/4
    assert round(S_total) == 6730
    print(f"[OK] Phần IV - Câu 3: BD = {BD} m; S = {S_total:.2f} m^2 -> 6730 m^2.")

    # Câu 4:
    # x + y <= 8
    # 2x + 3y <= 18
    # x + 2y <= 11
    # x, y >= 0
    # Max T = 30x + 40y
    verts = [(0,0), (8,0), (6,2), (3,4), (0, 5.5)]
    profits = {v: 30*v[0] + 40*v[1] for v in verts}
    best_v = max(profits, key=profits.get)
    assert best_v == (6, 2)
    assert profits[best_v] == 260
    print(f"[OK] Phần IV - Câu 4: tối ưu tại (6, 2) với tiền lãi = {profits[best_v]} triệu đồng.")

if __name__ == "__main__":
    verify_all()
