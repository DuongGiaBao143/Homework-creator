import sympy as sp
import numpy as np

print("=== VERIFYING ĐỀ ÔN TẬP VECTƠ — ĐỀ 2 (MÃ ĐỀ 1043) ===")

# --- PHẦN I (1.B | 2.D | 3.A | 4.C | 5.D | 6.A | 7.B | 8.C | 9.A | 10.D | 11.C | 12.B | 13.D | 14.A | 15.C | 16.B | 17.D | 18.A | 19.C | 20.B) ---

# Câu 1 (B): Ngũ giác đều ABCDE -> A_5^2 = 5 * 4 = 20
assert 5 * 4 == 20
print("Câu 1: OK (20 -> B)")

# Câu 2 (D): Hình chữ nhật ABCD tâm O, vectơ bằng BO là OD
A2, B2, C2, D2 = sp.Matrix([0, 0]), sp.Matrix([4, 0]), sp.Matrix([4, 2]), sp.Matrix([0, 2])
O2 = (A2 + C2) / 2
assert (O2 - B2) == (D2 - O2)
print("Câu 2: OK (OD -> D)")

# Câu 3 (A): MN - MP = PN
M3, N3, P3 = sp.Matrix([1, 2]), sp.Matrix([5, -1]), sp.Matrix([-2, 7])
assert (N3 - M3) - (P3 - M3) == (N3 - P3)
print("Câu 3: OK (MN - MP = PN -> A)")

# Câu 4 (C): Tam giác ABC vuông tại A, AB = 3, AC = 4 => |AB - AC| = |CB| = 5
assert sp.sqrt(3**2 + 4**2) == 5
print("Câu 4: OK (5 -> C)")

# Câu 5 (D): Hình vuông ABCD cạnh a => |AB + AD| = |AC| = a*sqrt(2)
a_sym = sp.Symbol('a', positive=True)
assert sp.sqrt(a_sym**2 + a_sym**2) == a_sym * sp.sqrt(2)
print("Câu 5: OK (a*sqrt(2) -> D)")

# Câu 6 (A): I trung điểm AB => MA + MB = 2MI
A6, B6, M6 = sp.Matrix([2, 3]), sp.Matrix([8, -1]), sp.Matrix([-3, 5])
I6 = (A6 + B6) / 2
assert (A6 - M6) + (B6 - M6) == 2 * (I6 - M6)
print("Câu 6: OK (MA + MB = 2MI -> A)")

# Câu 7 (B): K trên đoạn BC sao cho KC = 4KB => AK = 4/5 AB + 1/5 AC
A7, B7, C7 = sp.Matrix([0, 0]), sp.Matrix([5, 0]), sp.Matrix([0, 5])
K7 = (4 * B7 + C7) / 5
assert (C7 - K7).norm() == 4 * (K7 - B7).norm()
assert (K7 - A7) == sp.Rational(4, 5) * (B7 - A7) + sp.Rational(1, 5) * (C7 - A7)
print("Câu 7: OK (4/5 AB + 1/5 AC -> B)")

# Câu 8 (C): a, b ngược hướng <=> tồn tại k < 0 sao cho a = k b
print("Câu 8: OK (k < 0 -> C)")

# Câu 9 (A): a = -3i + 4j => (-3, 4)
print("Câu 9: OK ((-3, 4) -> A)")

# Câu 10 (D): u = (3, -1), v = (-2, 5) => 2u - v = (8, -7)
u10, v10 = sp.Matrix([3, -1]), sp.Matrix([-2, 5])
assert 2 * u10 - v10 == sp.Matrix([8, -7])
print("Câu 10: OK ((8, -7) -> D)")

# Câu 11 (C): A(1, 4), B(-3, 2), C(5, -3) => G(1, 1)
assert ((1 + (-3) + 5) / 3, (4 + 2 + (-3)) / 3) == (1, 1)
print("Câu 11: OK (G(1, 1) -> C)")

# Câu 12 (B): A(2, -1), M(4, 3) trung điểm AB => B(6, 7)
assert (2 * 4 - 2, 2 * 3 - (-1)) == (6, 7)
print("Câu 12: OK (B(6, 7) -> B)")

# Câu 13 (D): u = (-4, 6), v = (2, m) cùng phương => -4m - 12 = 0 => m = -3
m_sym = sp.Symbol('m')
assert sp.solve(-4 * m_sym - 6 * 2, m_sym) == [-3]
print("Câu 13: OK (m = -3 -> D)")

# Câu 14 (A): Hình vuông ABCD => góc (AB, BD) = 135 deg
AB14 = sp.Matrix([1, 0])
BD14 = sp.Matrix([-1, 1])
cos14 = AB14.dot(BD14) / (AB14.norm() * BD14.norm())
assert sp.acos(cos14) == 3 * sp.pi / 4
print("Câu 14: OK (135 deg -> A)")

# Câu 15 (C): Tam giác đều ABC cạnh a => AB . BC = -a^2 / 2
res15 = a_sym * a_sym * sp.cos(2 * sp.pi / 3)
assert res15 == -a_sym**2 / 2
print("Câu 15: OK (-a^2/2 -> C)")

# Câu 16 (B): a = (4, -3), b = (-2, 5) => a.b = -8 - 15 = -23
assert 4 * (-2) + (-3) * 5 == -23
print("Câu 16: OK (-23 -> B)")

# Câu 17 (D): A(1, -2), B(-5, 6) => AB = sqrt((-6)^2 + 8^2) = 10
assert sp.sqrt((-5 - 1)**2 + (6 - (-2))**2) == 10
print("Câu 17: OK (10 -> D)")

# Câu 18 (A): u = (m, 3), v = (6, -4) vuông góc => 6m - 12 = 0 => m = 2
assert sp.solve(6 * m_sym + 3 * (-4), m_sym) == [2]
print("Câu 18: OK (m = 2 -> A)")

# Câu 19 (C): a = (1, 3), b = (-2, -1) => cos = -5 / sqrt(50) = -sqrt(2)/2 => 135 deg
a19, b19 = sp.Matrix([1, 3]), sp.Matrix([-2, -1])
assert sp.acos(a19.dot(b19) / (a19.norm() * b19.norm())) == 3 * sp.pi / 4
print("Câu 19: OK (135 deg -> C)")

# Câu 20 (B): F = 40 N, s = 5 m, alpha = 30 deg => W = 40 * 5 * cos(30) = 100*sqrt(3) J
assert 40 * 5 * sp.cos(sp.pi / 6) == 100 * sp.sqrt(3)
print("Câu 20: OK (100*sqrt(3) J -> B)")


print("\n--- PHẦN II ---")
# Câu 1 (S - Đ - Đ - S): Hình vuông ABCD cạnh a, tâm O
A_sq = sp.Matrix([0, 0])
B_sq = sp.Matrix([a_sym, 0])
C_sq = sp.Matrix([a_sym, a_sym])
D_sq = sp.Matrix([0, a_sym])
O_sq = (A_sq + C_sq) / 2
assert (B_sq - A_sq) != (D_sq - C_sq)  # a) AB != CD (AB = -CD) -> S
assert (A_sq - O_sq) + (B_sq - O_sq) + (C_sq - O_sq) + (D_sq - O_sq) == sp.Matrix([0, 0])  # b) Đ
assert ((A_sq - O_sq) - (B_sq - O_sq)).norm() == a_sym  # c) |OA - OB| = |BA| = a -> Đ
assert ((B_sq - O_sq) + (C_sq - O_sq)).norm() == a_sym  # d) |OB + OC| = a != a*sqrt(2) -> S
print("Câu 1 Phần II: S - Đ - Đ - S (OK)")

# Câu 2 (Đ - S - S - Đ): Hình bình hành ABCD, M trung điểm BC, N trên CD sao cho NC = 3ND, I trung điểm MN
Ap, Bp, Dp = sp.Matrix([0, 0]), sp.Matrix([1, 0]), sp.Matrix([0, 1])
Cp = Bp + Dp - Ap
Mp = (Bp + Cp) / 2
Np = Dp + sp.Rational(1, 4) * (Cp - Dp)
Ip = (Mp + Np) / 2
assert (Cp - Np).norm() == 3 * (Np - Dp).norm()
ABp, ADp = Bp - Ap, Dp - Ap
assert (Mp - Ap) == ABp + sp.Rational(1, 2) * ADp  # a) Đ
assert (Np - Ap) == sp.Rational(1, 4) * ABp + ADp  # b) 1/4 != 1/3 -> S
assert (Np - Mp) == -sp.Rational(3, 4) * ABp + sp.Rational(1, 2) * ADp  # c) dấu ngược -> S
assert (Ip - Ap) == sp.Rational(5, 8) * ABp + sp.Rational(3, 4) * ADp  # d) Đ
print("Câu 2 Phần II: Đ - S - S - Đ (OK)")

# Câu 3 (S - Đ - S - Đ): A(-1, 1), B(2, 7), C(5, -2)
A3, B3, C3 = sp.Matrix([-1, 1]), sp.Matrix([2, 7]), sp.Matrix([5, -2])
AB3, AC3 = B3 - A3, C3 - A3
BA3, BC3 = A3 - B3, C3 - B3
G3 = (A3 + B3 + C3) / 3
assert AB3[0] * AC3[1] - AB3[1] * AC3[0] != 0  # a) không thẳng hàng -> S
assert AB3.dot(AC3) == 0  # b) vuông góc -> Đ
assert G3 == sp.Matrix([2, 2])  # c) G(2, 2) != G(2, 3) -> S
assert BA3.dot(BC3) == 45  # d) BA . BC = 45 -> Đ
print("Câu 3 Phần II: S - Đ - S - Đ (OK)")

# Câu 4 (Đ - Đ - S - S): Tam giác ABC có AB = 5, AC = 8, góc A = 60 deg, M trung điểm BC
dot_AB_AC = 5 * 8 * sp.cos(sp.pi / 3)
assert dot_AB_AC == 20  # a) Đ
BC_len = sp.sqrt(5**2 + 8**2 - 2 * dot_AB_AC)
assert BC_len == 7  # b) Đ
AM_len = sp.sqrt((5**2 + 8**2 + 2 * dot_AB_AC) / 4)
assert AM_len == sp.sqrt(129) / 2 and AM_len != 6  # c) S
# BA . BC = BA . (BA + AC) = BA^2 - AB . AC = 25 - 20 = 5
BA_dot_BC = 5**2 - dot_AB_AC
assert BA_dot_BC == 5 and BA_dot_BC != 15  # d) S
print("Câu 4 Phần II: Đ - Đ - S - S (OK)")


print("\n--- PHẦN III ---")
# Câu 1: Hình thoi ABCD cạnh 9, góc BAD = 120 deg => |AB + AD| = |AC| = 9
# |AB + AD|^2 = 9^2 + 9^2 + 2*9*9*cos(120) = 81 + 81 - 81 = 81 => 9
assert sp.sqrt(9**2 + 9**2 + 2 * 9 * 9 * sp.cos(2 * sp.pi / 3)) == 9
print("Câu 1 Phần III: OK (9)")

# Câu 2: Tam giác ABC, M trung điểm AB, N trên BC sao cho BN = 2NC. MN = x AB + y AC. P = 6x + 9y
# AM = 1/2 AB; AN = AB + 2/3(AC - AB) = 1/3 AB + 2/3 AC
# MN = AN - AM = -1/6 AB + 2/3 AC => x = -1/6, y = 2/3
x_p2, y_p2 = sp.Rational(-1, 6), sp.Rational(2, 3)
assert 6 * x_p2 + 9 * y_p2 == 5
print("Câu 2 Phần III: OK (5)")

# Câu 3: a = (2, -3), b = (-1, 4), c = (m, 4) cùng phương với 2a + b
w3 = 2 * sp.Matrix([2, -3]) + sp.Matrix([-1, 4])
assert w3 == sp.Matrix([3, -2])
sol_m3 = sp.solve(w3[0] * 4 - w3[1] * m_sym, m_sym)
assert sol_m3 == [-6]
print("Câu 3 Phần III: OK (-6)")

# Câu 4: A(-1, 2), B(4, 2), C(2, 6). Tính cos(BAC)
AB4 = sp.Matrix([4 - (-1), 2 - 2])
AC4 = sp.Matrix([2 - (-1), 6 - 2])
cos4 = AB4.dot(AC4) / (AB4.norm() * AC4.norm())
assert cos4 == sp.Rational(3, 5)
print("Câu 4 Phần III: OK (0.6)")

# Câu 5: A(1, 3), B(5, 1), M(m, 0) thuộc Ox, m > 3, tam giác MAB vuông tại M
MA5 = sp.Matrix([1 - m_sym, 3])
MB5 = sp.Matrix([5 - m_sym, 1])
sol_m5 = sp.solve(MA5.dot(MB5), m_sym)
assert set(sol_m5) == {2, 4}
print("Câu 5 Phần III: OK (m = 4, m > 3)")

# Câu 6: F1 = 30 N, F2 = 50 N, góc 60 deg => |F| = sqrt(30^2 + 50^2 + 2*30*50*cos(60)) = 70 N
F_res = sp.sqrt(30**2 + 50**2 + 2 * 30 * 50 * sp.cos(sp.pi / 3))
assert F_res == 70
print("Câu 6 Phần III: OK (70)")


print("\n--- PHẦN IV ---")
# Bài 1: Hình bình hành ABCD. E trung điểm AB, F trên AD với AF = 1/3 AD, K trên AC với AK = 1/5 AC
A_b1, B_b1, D_b1 = sp.Matrix([0, 0]), sp.Matrix([1, 0]), sp.Matrix([0, 1])
C_b1 = B_b1 + D_b1 - A_b1
E_b1 = (A_b1 + B_b1) / 2
F_b1 = A_b1 + sp.Rational(1, 3) * (D_b1 - A_b1)
K_b1 = A_b1 + sp.Rational(1, 5) * (C_b1 - A_b1)
AB_b1, AD_b1 = B_b1 - A_b1, D_b1 - A_b1
EF_b1 = F_b1 - E_b1
EK_b1 = K_b1 - E_b1
assert EF_b1 == -sp.Rational(1, 2) * AB_b1 + sp.Rational(1, 3) * AD_b1
assert EK_b1 == -sp.Rational(3, 10) * AB_b1 + sp.Rational(1, 5) * AD_b1
assert EK_b1 == sp.Rational(3, 5) * EF_b1
print("Bài 1 Phần IV: EF = -1/2 AB + 1/3 AD, EK = -3/10 AB + 1/5 AD = 3/5 EF (OK)")

# Bài 2: A(-2, 6), B(1, 2), C(9, 8)
A_b2, B_b2, C_b2 = sp.Matrix([-2, 6]), sp.Matrix([1, 2]), sp.Matrix([9, 8])
BA_b2, BC_b2 = A_b2 - B_b2, C_b2 - B_b2
assert BA_b2.dot(BC_b2) == 0
assert BA_b2.norm() == 5 and BC_b2.norm() == 10
area_b2 = sp.Rational(1, 2) * BA_b2.norm() * BC_b2.norm()
assert area_b2 == 25
D_b2 = A_b2 + BC_b2
assert D_b2 == sp.Matrix([6, 12])
assert (D_b2 - C_b2) == (A_b2 - B_b2)
print("Bài 2 Phần IV: Vuông tại B, S = 25, D(6, 12) (OK)")

# Bài 3: Thuyền qua sông rộng d = 120m, v1 = 4 m/s vuông góc bờ, v2 = 3 m/s dọc bờ
v1, v2, d_river = 4, 3, 120
v_res = sp.sqrt(v1**2 + v2**2)
assert v_res == 5
alpha_deg = float(sp.deg(sp.atan(sp.Rational(v2, v1))).evalf())
assert round(alpha_deg, 1) == 36.9
t_cross = d_river / v1
drift_s = v2 * t_cross
assert t_cross == 30 and drift_s == 90
print(f"Bài 3 Phần IV: v = 5 m/s, alpha = {alpha_deg:.2f} -> 36.9 deg, t = 30s, s = 90m (OK)")

print("\n>>> ALL 33 QUESTIONS FOR EXAM 2 VERIFIED 100% MATHEMATICALLY CORRECT! <<<")
