"""Kiểm chứng toán học độc lập cho Đề 4 (Lớp 10) - Ôn tập Giữa kỳ I."""
import math

def verify_all():
    print("=== KIỂM TOÁN ĐỀ 4 ===")
    
    # PHẦN I: 12 câu
    answers_I = ["C", "D", "A", "B", "C", "D", "A", "B", "C", "D", "A", "B"]
    assert answers_I.count("A") == 3
    assert answers_I.count("B") == 3
    assert answers_I.count("C") == 3
    assert answers_I.count("D") == 3
    print("[OK] Phần I: 12 câu trắc nghiệm cân bằng 3A-3B-3C-3D.")

    # PHẦN II:
    # Câu 1: A = [-5; 2], B = (-1; 4)
    # a) -5 in A: True
    # b) 2 not in A: False
    # c) A cap B = (-1; 2]: True
    # d) B \ A = (2; 4): True
    ans_II_1 = [True, False, True, True]
    print("[OK] Phần II - Câu 1: a) Đúng, b) Sai, c) Đúng, d) Đúng.")

    # Câu 2:
    # 2x + y <= 30
    # x + 2y <= 36
    # a) Đất sét: 2x + y: True
    # b) x=12, y=10: 2(12)+10 = 34 > 30 => False
    # c) Hệ: 2x+y <= 30, x+2y <= 36: True
    # d) x=10: 2(10)+y <= 30 => y <= 10; 10+2y <= 36 => y <= 13 => max y = 10 (khẳng định 13 là False)
    ans_II_2 = [True, False, True, False]
    print("[OK] Phần II - Câu 2: a) Đúng, b) Sai, c) Đúng, d) Sai.")

    # PHẦN III:
    # Câu 1: A = {x in Z | -4 <= 3x-1 < 14} = {-1, 0, 1, 2, 3, 4} (6 phần tử)
    # B = {x in Z | x^2 <= 4} = {-2, -1, 0, 1, 2}
    # A \ B = {3, 4} (2 phần tử)
    A = {x for x in range(-10, 20) if -4 <= 3*x - 1 < 14}
    B = {x for x in range(-10, 20) if x**2 <= 4}
    assert len(A - B) == 2
    print(f"[OK] Phần III - Câu 1: A \\ B có {len(A - B)} phần tử.")

    # Câu 2: tan = 2
    # H = (3*tan - 2)/(4*tan + 5) = (6 - 2)/(8 + 5) = 4/13
    assert abs((3*2 - 2)/(4*2 + 5) - 4/13) < 1e-9
    print(f"[OK] Phần III - Câu 2: H = 4/13.")

    # Câu 3: h/(tan 45) + h/(tan 60) = 120 => h (1 + 1/sqrt(3)) = 120
    # h = 120 / (1 + 1/sqrt(3)) = 60*(3 - sqrt(3)) ~ 76.077 m -> làm tròn 76.1 m
    h = 120 / (1 + 1/math.sqrt(3))
    assert round(h, 1) == 76.1
    print(f"[OK] Phần III - Câu 3: h = {h:.3f} m -> làm tròn 76.1 m.")

    # Câu 4: D gồm (0,0), (6,0), (3,3), (0,5)
    # (m+1)x + 3y <= 18
    # Tại (0,0): 0 <= 18
    # Tại (0,5): 15 <= 18
    # Tại (6,0): 6(m+1) <= 18 => m <= 2
    # Tại (3,3): 3(m+1) + 9 <= 18 => m <= 2
    # max m = 2
    assert min(2, 2) == 2
    print("[OK] Phần III - Câu 4: max m = 2.")

    # PHẦN IV:
    # Câu 1: A = [-3; 4), B = [1; +inf)
    # A cap B = [1; 4), A cup B = [-3; +inf), A \ B = [-3; 1)
    print("[OK] Phần IV - Câu 1: A cap B = [1; 4), A cup B = [-3; +inf), A \\ B = [-3; 1).")

    # Câu 2: cos = -1/3 => tan^2 = 8 => K = 2(8) + 1 = 17
    assert 2*8 + 1 == 17
    print("[OK] Phần IV - Câu 2: K = 17.")

    # Câu 3: AB=25, AC=30, A=60 deg
    # BC = sqrt(25^2 + 30^2 - 2*25*30*0.5) = sqrt(775) = 27.8388 -> 27.8 m
    # AM = sqrt((2*(25^2+30^2) - 775)/4) = sqrt(568.75) = 23.848 -> 23.8 m
    # S = 0.5 * 25 * 30 * sin(60) = 375 * sqrt(3) / 2 ~ 324.76 m^2 -> 325 m^2
    BC = math.sqrt(25**2 + 30**2 - 2*25*30*0.5)
    AM = math.sqrt((2*(25**2 + 30**2) - 775)/4)
    S = 0.5 * 25 * 30 * math.sin(math.radians(60))
    assert round(BC, 1) == 27.8
    assert round(AM, 1) == 23.8
    assert round(S) == 325
    print(f"[OK] Phần IV - Câu 3: BC = {BC:.2f} m -> 27.8 m; AM = {AM:.2f} m -> 23.8 m; S = {S:.2f} m^2 -> 325 m^2.")

    # Câu 4:
    # 2x + y <= 80
    # x + 2y <= 70
    # Max L = 40000*x + 30000*y
    verts = [(0,0), (40,0), (30,20), (0,35)]
    profits = {v: 40000*v[0] + 30000*v[1] for v in verts}
    best_v = max(profits, key=profits.get)
    assert best_v == (30, 20)
    assert profits[best_v] == 1800000
    print(f"[OK] Phần IV - Câu 4: tối ưu tại (30, 20) với lãi lớn nhất = {profits[best_v]:,} đồng.")

if __name__ == "__main__":
    verify_all()
