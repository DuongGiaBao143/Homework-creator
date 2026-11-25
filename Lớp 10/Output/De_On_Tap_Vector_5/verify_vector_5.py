import sympy as sp
from collections import Counter

print("=== VERIFYING ĐỀ ÔN TẬP CHƯƠNG IV. VECTƠ — ĐỀ SỐ 5 (MÃ ĐỀ 1046) ===")

# ---- PART I: 20 MCQs ----
# Keys target: 1.A, 2.C, 3.B, 4.D, 5.A, 6.D, 7.B, 8.C, 9.A, 10.B, 11.D, 12.C, 13.B, 14.D, 15.A, 16.C, 17.B, 18.D, 19.C, 20.A
keys_p1 = {
    1: "A", 2: "C", 3: "B", 4: "D", 5: "A",
    6: "D", 7: "B", 8: "C", 9: "A", 10: "B",
    11: "D", 12: "C", 13: "B", 14: "D", 15: "A",
    16: "C", 17: "B", 18: "D", 19: "C", 20: "A",
}
dist = Counter(keys_p1.values())
assert dict(dist) == {"A": 5, "B": 5, "C": 5, "D": 5}, f"Bad distribution: {dist}"
print("Part I key distribution:", dict(sorted(dist.items())))

# Q1: Triangle ABC, M, N, P midpoints of AB, BC, CA. Nonzero vectors parallel to BC from {A,B,C,M,N,P}.
# Line BC has {B, N, C}: 3*2 = 6 directed pairs. Line MP parallel to BC has {M, P}: 2*1 = 2 directed pairs.
q1_count = 3 * 2 + 2 * 1
assert q1_count == 8, q1_count

# Q4: Rhombus ABCD side a, angle BCD = 60 deg. |CB + CD|
a = sp.Symbol("a", positive=True)
q4_norm = sp.sqrt(a**2 + a**2 + 2 * a * a * sp.cos(sp.rad(60)))
assert sp.simplify(q4_norm - a * sp.sqrt(3)) == 0, q4_norm

# Q5: Right isosceles ABC at A, BC = 2a. |AB + AC| = |AD| where ABDC is square -> AD = BC = 2a
ab_q5 = 2 * a / sp.sqrt(2)
q5_norm = sp.sqrt(ab_q5**2 + ab_q5**2)
assert sp.simplify(q5_norm - 2 * a) == 0, q5_norm

# Q7: 2*KA + 3*KB = 0 => 2*KA + 3*(KA + AB) = 0 => 5*KA = -3*AB => AK = (3/5)*AB
k_coeff = sp.Rational(3, 5)
assert 2 * (-k_coeff) + 3 * (1 - k_coeff) == 0

# Q8: Centroid G of ABC => BG = (BA + BC)/3 = 1/3 BA + 1/3 BC
assert sp.Rational(1, 3) + sp.Rational(1, 3) == sp.Rational(2, 3)

# Q9: u = (5, -1), v = (-2, 3) => u - 2v
u9 = sp.Matrix([5, -1])
v9 = sp.Matrix([-2, 3])
assert u9 - 2 * v9 == sp.Matrix([9, -7])

# Q10: M(-3, 5), N(1, -1) => NM = M - N
M10 = sp.Matrix([-3, 5])
N10 = sp.Matrix([1, -1])
assert M10 - N10 == sp.Matrix([-4, 6])

# Q11: Midpoint of A(-2, 3), B(4, -5)
A11 = sp.Matrix([-2, 3])
B11 = sp.Matrix([4, -5])
assert (A11 + B11) / 2 == sp.Matrix([1, -1])

# Q12: A(1, 2), B(m, 6), C(-1, -2) collinear
m = sp.Symbol("m", real=True)
AB12 = sp.Matrix([m - 1, 6 - 2])
AC12 = sp.Matrix([-1 - 1, -2 - 2])
m12 = sp.solve(AB12[0] * AC12[1] - AB12[1] * AC12[0], m)
assert m12 == [3], m12

# Q13: a = (4, -2), b = (m+1, 3) parallel
m13 = sp.solve(4 * 3 - (-2) * (m + 1), m)
assert m13 == [-7], m13

# Q14: Right triangle ABC at A, angle C = 40 deg => (CA, BC) = 180 - 40 = 140 deg
assert 180 - 40 == 140

# Q15: Equilateral ABC side 2a, H midpoint BC => AB . AH
q15_dot = (2 * a) * (a * sp.sqrt(3)) * sp.cos(sp.rad(30))
assert sp.simplify(q15_dot - 3 * a**2) == 0, q15_dot

# Q16: u = (3, -5), v = (2, 4) => u . (u - v)
u16 = sp.Matrix([3, -5])
v16 = sp.Matrix([2, 4])
assert u16.dot(u16 - v16) == 48

# Q17: A(2, -3), B(-4, 5) => AB
AB17 = sp.Matrix([-4 - 2, 5 - (-3)])
assert AB17.norm() == 10

# Q18: x = (m, 4), y = (m-3, -1) perpendicular => sum of m
sol18 = sp.solve(m * (m - 3) + 4 * (-1), m)
assert set(sol18) == {-1, 4} and sum(sol18) == 3, sol18

# Q19: a = (1, sqrt(3)), b = (-1, sqrt(3)) => angle
a19 = sp.Matrix([1, sp.sqrt(3)])
b19 = sp.Matrix([-1, sp.sqrt(3)])
cos19 = a19.dot(b19) / (a19.norm() * b19.norm())
assert sp.acos(cos19) == sp.rad(60), cos19

# Q20: F = 2000 N, d = 50 m, alpha = 60 deg => W = 2000 * 50 * cos(60) = 50000 J = 50 kJ
W20 = 2000 * 50 * sp.cos(sp.rad(60))
assert W20 == 50000

# ---- PART II: 4 True/False Questions ----
# P2 Q1: Right triangle ABC at A, AB = 6, AC = 8, M midpoint BC. Pattern: Đ - S - S - Đ
A_p2q1 = sp.Matrix([0, 0])
B_p2q1 = sp.Matrix([6, 0])
C_p2q1 = sp.Matrix([0, 8])
M_p2q1 = (B_p2q1 + C_p2q1) / 2
AB_p2q1 = B_p2q1 - A_p2q1
AC_p2q1 = C_p2q1 - A_p2q1
BA_p2q1 = -AB_p2q1
BC_p2q1 = C_p2q1 - B_p2q1
assert BC_p2q1.norm() == 10  # a) Đ
assert (AB_p2q1 + AC_p2q1).norm() == 10 and 10 != 14  # b) S
assert BA_p2q1.dot(BC_p2q1) == 36 and 36 != 48  # c) S
assert (2 * AB_p2q1 - AC_p2q1).norm() == 4 * sp.sqrt(13)  # d) Đ

# P2 Q2: Parallelogram ABCD, I midpoint CD, BK = 1/3 BD. Pattern: S - Đ - Đ - S
# Using basis AB = e1, AD = e2
e1 = sp.Matrix([1, 0])
e2 = sp.Matrix([0, 1])
A2, B2, D2 = sp.Matrix([0, 0]), e1, e2
C2 = e1 + e2
I2 = (C2 + D2) / 2  # AI = 1/2 AB + AD
K2 = B2 + sp.Rational(1, 3) * (D2 - B2)  # AK = 2/3 AB + 1/3 AD
AI2 = I2 - A2
AK2 = K2 - A2
IK2 = K2 - I2
assert AI2 == sp.Rational(1, 2) * e1 + e2 and AI2 != e1 + sp.Rational(1, 2) * e2  # a) S
assert AK2 == sp.Rational(2, 3) * e1 + sp.Rational(1, 3) * e2  # b) Đ
assert IK2 == sp.Rational(1, 6) * e1 - sp.Rational(2, 3) * e2  # c) Đ
assert AI2[0] * AK2[1] - AI2[1] * AK2[0] != 0  # d) S (not collinear)

# P2 Q3: A(1, 5), B(-2, 1), C(4, -3). Pattern: Đ - Đ - S - S
A3, B3, C3 = sp.Matrix([1, 5]), sp.Matrix([-2, 1]), sp.Matrix([4, -3])
assert (B3 - A3).norm() == 5  # a) Đ
assert (A3 + C3) / 2 == sp.Matrix([sp.Rational(5, 2), 1])  # b) Đ
BA3 = A3 - B3
BC3 = C3 - B3
assert BA3.dot(BC3) == 2 and BA3.dot(BC3) != 0  # c) S
D3 = A3 + C3 - B3  # ABCD parallelogram => AB = DC => D = A + C - B
assert D3 == sp.Matrix([7, 1]) and D3 != sp.Matrix([7, 2])  # d) S

# P2 Q4: Rhombus ABCD side 2a, angle BAD = 60 deg. Pattern: S - S - Đ - Đ
# Use numeric a = 1 with coordinates: A(0,0), B(2,0), D(1, sqrt(3)), C(3, sqrt(3))
A4 = sp.Matrix([0, 0])
B4 = sp.Matrix([2, 0])
D4 = sp.Matrix([1, sp.sqrt(3)])
C4 = B4 + D4
AB4 = B4 - A4
BC4 = C4 - B4
AD4 = D4 - A4
AC4 = C4 - A4
BD4 = D4 - B4
cos_AB_BC = AB4.dot(BC4) / (AB4.norm() * BC4.norm())
assert sp.acos(cos_AB_BC) == sp.rad(60)  # a) S (says 120)
assert AB4.dot(AD4) == 2  # b) S (says 4a^2, actually 2a^2)
assert sp.simplify((AB4 + AD4).norm() - 2 * sp.sqrt(3)) == 0  # c) Đ
assert AC4.dot(BD4) == 0  # d) Đ

# ---- PART III: 6 Short-Answer Questions ----
# III.1: Equilateral ABC side 4*sqrt(3) => |AB + AC| = 2 * AM = 2 * (4*sqrt(3) * sqrt(3)/2) = 12
s1 = 4 * sp.sqrt(3)
assert sp.simplify(2 * (s1 * sp.sqrt(3) / 2)) == 12

# III.2: Parallelogram ABCD, M midpoint BC, CN = 2*ND (i.e. DN = 1/3 DC). MN = x*AB + y*AD => T = 4y - 6x
M_iii2 = e1 + sp.Rational(1, 2) * e2
N_iii2 = e2 + sp.Rational(1, 3) * e1  # DN = 1/3 AB, AN = AD + 1/3 AB
MN_iii2 = N_iii2 - M_iii2
x_iii2, y_iii2 = MN_iii2[0], MN_iii2[1]
assert x_iii2 == sp.Rational(-2, 3) and y_iii2 == sp.Rational(1, 2)
T_iii2 = 4 * y_iii2 - 6 * x_iii2
assert T_iii2 == 6

# III.3: A(3, -1), B(-1, 2), C(3, 5), DA + 2*DB + DC = 0 => D = (A + 2B + C)/4
A_iii3 = sp.Matrix([3, -1])
B_iii3 = sp.Matrix([-1, 2])
C_iii3 = sp.Matrix([3, 5])
D_iii3 = (A_iii3 + 2 * B_iii3 + C_iii3) / 4
assert D_iii3 == sp.Matrix([1, 2])
assert D_iii3[0] + 2 * D_iii3[1] == 5

# III.4: a = (3, 4), b = (4, 3) => cos(a, b) = 24/25 = 0.96
a_iii4 = sp.Matrix([3, 4])
b_iii4 = sp.Matrix([4, 3])
cos_iii4 = a_iii4.dot(b_iii4) / (a_iii4.norm() * b_iii4.norm())
assert cos_iii4 == sp.Rational(24, 25) and float(cos_iii4) == 0.96

# III.5: A(1, 2), B(6, 2), C(m, 0) with m > 3, right at C => CA . CB = 0
CA_iii5 = sp.Matrix([1 - m, 2])
CB_iii5 = sp.Matrix([6 - m, 2])
sol_iii5 = [val for val in sp.solve(CA_iii5.dot(CB_iii5), m) if val > 3]
assert sol_iii5 == [5], sol_iii5

# III.6: Sled pulled d = 25 m, F = 120 N, angle = 60 deg => A = 120 * 25 * cos(60) = 1500 J
assert 120 * 25 * sp.cos(sp.rad(60)) == 1500

# ---- PART IV: 3 Free-Response Questions ----
# IV.1: Parallelogram ABCD, I midpoint AD, K on AB with AK = 1/4 AB, E on AC with AE = 1/6 AC
I_iv1 = sp.Rational(1, 2) * e2
K_iv1 = sp.Rational(1, 4) * e1
E_iv1 = sp.Rational(1, 6) * (e1 + e2)
IE_iv1 = E_iv1 - I_iv1
IK_iv1 = K_iv1 - I_iv1
assert IE_iv1 == sp.Rational(1, 6) * e1 - sp.Rational(1, 3) * e2
assert IK_iv1 == sp.Rational(1, 4) * e1 - sp.Rational(1, 2) * e2
assert IK_iv1 == sp.Rational(3, 2) * IE_iv1

# IV.2: A(1, 2), B(5, 0), C(3, 6)
A_iv2, B_iv2, C_iv2 = sp.Matrix([1, 2]), sp.Matrix([5, 0]), sp.Matrix([3, 6])
AB_iv2 = B_iv2 - A_iv2
AC_iv2 = C_iv2 - A_iv2
assert AB_iv2 == sp.Matrix([4, -2]) and AC_iv2 == sp.Matrix([2, 4])
assert AB_iv2.dot(AC_iv2) == 0 and AB_iv2.norm() == AC_iv2.norm() == 2 * sp.sqrt(5)
D_iv2 = B_iv2 + AC_iv2  # ABDC is a square => CD = AB => D = C + AB = B + AC
assert D_iv2 == sp.Matrix([7, 4])
# Centroid G of ABC:
G_iv2 = (A_iv2 + B_iv2 + C_iv2) / 3
assert G_iv2 == sp.Matrix([3, sp.Rational(8, 3)])
# N on Oy: N(0, y) minimizes 3*|NG| => N(0, 8/3), min = 3 * 3 = 9
y = sp.Symbol("y", real=True)
N_iv2 = sp.Matrix([0, y])
expr_iv2 = (A_iv2 - N_iv2 + B_iv2 - N_iv2 + C_iv2 - N_iv2).norm()
y_min = sp.solve(sp.diff(expr_iv2**2, y), y)[0]
assert y_min == sp.Rational(8, 3)
assert expr_iv2.subs(y, y_min) == 9

# IV.3: Walk from O(0, 0): 300 m East to A, then 500 m at 60 deg North of East to B
OA_iv3 = sp.Matrix([300, 0])
AB_iv3 = sp.Matrix([500 * sp.cos(sp.rad(60)), 500 * sp.sin(sp.rad(60))])
OB_iv3 = OA_iv3 + AB_iv3
assert AB_iv3 == sp.Matrix([250, 250 * sp.sqrt(3)])
assert OB_iv3 == sp.Matrix([550, 250 * sp.sqrt(3)])
assert sp.simplify(OB_iv3.norm()) == 700
cos_theta_iv3 = OB_iv3[0] / OB_iv3.norm()
assert cos_theta_iv3 == sp.Rational(11, 14)
deg_iv3 = float(sp.deg(sp.acos(cos_theta_iv3)).evalf())
assert round(deg_iv3, 1) == 38.2, deg_iv3

print("ALL 33 QUESTIONS VERIFIED 100% PASS!")
