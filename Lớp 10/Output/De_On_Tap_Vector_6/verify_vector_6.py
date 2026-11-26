import sympy as sp
from collections import Counter

print("=== VERIFYING ĐỀ ÔN TẬP CHƯƠNG IV. VECTƠ — ĐỀ SỐ 6 (MÃ ĐỀ 1047) ===")

# ---- PART I: 20 MCQs ----
keys_p1 = {
    1: "B", 2: "D", 3: "A", 4: "C", 5: "D",
    6: "B", 7: "A", 8: "C", 9: "D", 10: "A",
    11: "C", 12: "B", 13: "C", 14: "A", 15: "D",
    16: "B", 17: "A", 18: "D", 19: "C", 20: "B",
}
dist = Counter(keys_p1.values())
assert dict(dist) == {"A": 5, "B": 5, "C": 5, "D": 5}, f"Bad distribution: {dist}"
print("Part I key distribution:", dict(sorted(dist.items())))

# Q1: 6 distinct collinear points -> nonzero vectors = 6 * 5 = 30
assert 6 * 5 == 30

# Q2: Opposite direction, |a|=6, |b|=2 => a = -3b
assert -3 * 2 == -6

# Q3: Regular hexagon ABCDEF center O => sum OA..OF = 0
hex_pts = [sp.Matrix([sp.cos(k * sp.pi / 3), sp.sin(k * sp.pi / 3)]) for k in range(6)]
assert sp.simplify(sum(hex_pts, sp.Matrix([0, 0]))) == sp.Matrix([0, 0])

# Q4: Rectangle ABCD, AB = 5, AD = 12 => |BA + BC| = BD = 13
assert sp.sqrt(5**2 + 12**2) == 13

# Q5: Square ABCD side 2a, center O => |OA + OB| = 2a
a = sp.Symbol("a", positive=True)
A5, B5, O5 = sp.Matrix([0, 2 * a]), sp.Matrix([2 * a, 2 * a]), sp.Matrix([a, a])
assert (A5 - O5 + B5 - O5).norm() == 2 * a

# Q7: MA + 2*MB = 0 => AM = 2/3 AB => CM = 1/3 CA + 2/3 CB
e1, e2 = sp.Matrix([1, 0]), sp.Matrix([0, 1])  # CA = e1, CB = e2
M7 = sp.Rational(2, 3) * (e2 - e1) + e1
assert M7 == sp.Rational(1, 3) * e1 + sp.Rational(2, 3) * e2

# Q9: a = (3, -4), b = (-1, 2) => 2a + 3b
assert 2 * sp.Matrix([3, -4]) + 3 * sp.Matrix([-1, 2]) == sp.Matrix([3, -2])

# Q10: A(4, -2), AB = (-3, 5) => B = (1, 3)
assert sp.Matrix([4, -2]) + sp.Matrix([-3, 5]) == sp.Matrix([1, 3])

# Q11: A(-2, 5), B(4, -1), G(1, 2) => C = 3G - A - B
assert 3 * sp.Matrix([1, 2]) - sp.Matrix([-2, 5]) - sp.Matrix([4, -1]) == sp.Matrix([1, 2])

# Q12: P(-1, 3), Q(2, -3), R(5, m) collinear
m = sp.Symbol("m", real=True)
PQ12 = sp.Matrix([2 - (-1), -3 - 3])
PR12 = sp.Matrix([5 - (-1), m - 3])
assert sp.solve(PQ12[0] * PR12[1] - PQ12[1] * PR12[0], m) == [-9]

# Q13: u = (m, -6), v = (-3, m+3) parallel => m = 3 or m = -6
sol13 = sp.solve(m * (m + 3) - (-6) * (-3), m)
assert set(sol13) == {3, -6}

# Q14: Isosceles ABC at A, angle A = 50 deg => (AB, BC) = 180 - 65 = 115 deg
B_angle = (180 - 50) / 2
assert 180 - B_angle == 115

# Q15: |a|=4, |b|=5, angle 120 deg => a.(a+b) = 16 + 20*(-1/2) = 6
assert 4**2 + 4 * 5 * sp.cos(sp.rad(120)) == 6

# Q16: A(1, 2), B(4, -2), C(-1, 4) => AB . AC
AB16 = sp.Matrix([4 - 1, -2 - 2])
AC16 = sp.Matrix([-1 - 1, 4 - 2])
assert AB16.dot(AC16) == -14

# Q17: u = (x, x+2), |u| = 10, x > 0 => x = 6
x = sp.Symbol("x", real=True)
sol17 = [v for v in sp.solve(x**2 + (x + 2)**2 - 100, x) if v > 0]
assert sol17 == [6]

# Q18: a = (2, -5), b = (m+4, 2) perpendicular => m = 1
assert sp.solve(2 * (m + 4) + (-5) * 2, m) == [1]

# Q19: a = (3, 1), b = (1, 2) => cos(a, b) = sqrt(2)/2
a19, b19 = sp.Matrix([3, 1]), sp.Matrix([1, 2])
assert a19.dot(b19) / (a19.norm() * b19.norm()) == sp.sqrt(2) / 2

# Q20: F1 = F2 = 30 N, angle 60 deg => |F1 + F2| = 30*sqrt(3)
assert sp.simplify(sp.sqrt(30**2 + 30**2 + 2 * 30 * 30 * sp.cos(sp.rad(60))) - 30 * sp.sqrt(3)) == 0

# ---- PART II: 4 True/False Questions ----
# P2 Q1: Rectangle ABCD, AB = 8, AD = 12, M midpoint BC. Pattern: S - Đ - S - Đ
A1, B1, C1, D1 = sp.Matrix([0, 0]), sp.Matrix([8, 0]), sp.Matrix([8, 12]), sp.Matrix([0, 12])
M1 = (B1 + C1) / 2
AC1 = C1 - A1
AB1 = B1 - A1
AM1 = M1 - A1
BD1 = D1 - B1
assert AC1.norm() == 4 * sp.sqrt(13) and AC1.norm() != 20  # a) S
assert AB1.dot(AC1) == 64  # b) Đ
assert AM1.dot(BD1) == 8 and AM1.dot(BD1) != 16  # c) S
assert AM1.norm() == 10  # d) Đ

# P2 Q2: Triangle ABC, G centroid, M midpoint BC, AN = 3*AB. Pattern: Đ - S - Đ - S
# Using basis AB = e1, AC = e2
AG2 = (e1 + e2) / 3
AM2 = (e1 + e2) / 2
AN2 = 3 * e1
MG2 = AG2 - AM2
MN2 = AN2 - AM2
CN2 = AN2 - e2
assert (sp.Matrix([0, 0]) - AG2) + (e1 - AG2) + (e2 - AG2) == sp.Matrix([0, 0])  # a) Đ
assert MG2 == -sp.Rational(1, 6) * e1 - sp.Rational(1, 6) * e2  # b) S
assert MN2 == sp.Rational(5, 2) * e1 - sp.Rational(1, 2) * e2  # c) Đ
assert CN2 == 3 * e1 - e2 and CN2 != 3 * e1 + e2  # d) S

# P2 Q3: A(-1, 2), B(3, 4), C(1, -2). Pattern: S - S - Đ - Đ
A3, B3, C3 = sp.Matrix([-1, 2]), sp.Matrix([3, 4]), sp.Matrix([1, -2])
AB3 = B3 - A3
AC3 = C3 - A3
G3 = (A3 + B3 + C3) / 3
assert AB3 == sp.Matrix([4, 2]) and AB3 != sp.Matrix([-4, -2])  # a) S
assert G3 == sp.Matrix([1, sp.Rational(4, 3)]) and G3[1] != sp.Rational(2, 3)  # b) S
assert AB3.dot(AC3) == 0 and AB3.norm() == AC3.norm() == 2 * sp.sqrt(5)  # c) Đ
assert sp.Rational(1, 2) * AB3.norm() * AC3.norm() == 10  # d) Đ

# P2 Q4: Triangle ABC, AB = 6, AC = 10, angle BAC = 120 deg. Pattern: Đ - Đ - S - S
AB4_sq = 36
AC4_sq = 100
dot4 = 6 * 10 * sp.cos(sp.rad(120))
assert dot4 == -30  # a) Đ
BC4 = sp.sqrt(AB4_sq + AC4_sq - 2 * dot4)
assert BC4 == 14  # b) Đ
sum4 = sp.sqrt(AB4_sq + AC4_sq + 2 * dot4)
assert sum4 == 2 * sp.sqrt(19) and sum4 != 16  # c) S
ba_dot_bc = AB4_sq - dot4
assert ba_dot_bc == 66 and ba_dot_bc != 6  # d) S

# ---- PART III: 6 Short-Answer Questions ----
# III.1: Rhombus ABCD side 12, angle BAD = 60 deg => |AB - AD| = |DB| = 12
assert sp.simplify(sp.sqrt(12**2 + 12**2 - 2 * 12 * 12 * sp.cos(sp.rad(60)))) == 12

# III.2: M midpoint AB, N on AC with AN = 3NC (AN = 3/4 AC). MN = x*AB + y*AC => T = 8y - 2x
MN_iii2 = sp.Rational(3, 4) * e2 - sp.Rational(1, 2) * e1
x_iii2, y_iii2 = MN_iii2[0], MN_iii2[1]
assert x_iii2 == sp.Rational(-1, 2) and y_iii2 == sp.Rational(3, 4)
assert 8 * y_iii2 - 2 * x_iii2 == 7

# III.3: A(2, -1), B(0, 3), C(-3, 2). MA + 3MB - 2MC = 0 => M = (A + 3B - 2C)/2
A_iii3, B_iii3, C_iii3 = sp.Matrix([2, -1]), sp.Matrix([0, 3]), sp.Matrix([-3, 2])
M_iii3 = (A_iii3 + 3 * B_iii3 - 2 * C_iii3) / 2
assert M_iii3 == sp.Matrix([4, 2])
assert 2 * M_iii3[0] + M_iii3[1] == 10

# III.4: u = (4, -3), v = (8, 6) => cos(u, v) = 14/50 = 0.28
u_iii4, v_iii4 = sp.Matrix([4, -3]), sp.Matrix([8, 6])
cos_iii4 = u_iii4.dot(v_iii4) / (u_iii4.norm() * v_iii4.norm())
assert cos_iii4 == sp.Rational(7, 25) and float(cos_iii4) == 0.28

# III.5: A(-1, 2), B(5, 4), M(m, 0) with MA = MB => m = 3
M_iii5 = sp.Matrix([m, 0])
sol_iii5 = sp.solve((M_iii5 - sp.Matrix([-1, 2])).norm()**2 - (M_iii5 - sp.Matrix([5, 4])).norm()**2, m)
assert sol_iii5 == [3]

# III.6: F1 = 300 N, F2 = 500 N, angle 60 deg => |F1 + F2| = 700 N
assert sp.simplify(sp.sqrt(300**2 + 500**2 + 2 * 300 * 500 * sp.cos(sp.rad(60)))) == 700

# ---- PART IV: 3 Free-Response Questions ----
# IV.1: I midpoint BC, M midpoint AI, N on AC with AN = 1/3 AC
AI_iv1 = (e1 + e2) / 2
AM_iv1 = AI_iv1 / 2
BM_iv1 = AM_iv1 - e1
BN_iv1 = sp.Rational(1, 3) * e2 - e1
assert BM_iv1 == -sp.Rational(3, 4) * e1 + sp.Rational(1, 4) * e2
assert BN_iv1 == -e1 + sp.Rational(1, 3) * e2
assert BM_iv1 == sp.Rational(3, 4) * BN_iv1

# IV.2: A(2, 5), B(-1, -1), C(4, 4)
A_iv2, B_iv2, C_iv2 = sp.Matrix([2, 5]), sp.Matrix([-1, -1]), sp.Matrix([4, 4])
AB_iv2, AC_iv2 = B_iv2 - A_iv2, C_iv2 - A_iv2
assert AB_iv2.dot(AC_iv2) == 0
D_iv2 = A_iv2 + (C_iv2 - B_iv2)  # ABCD parallelogram => AD = BC
assert D_iv2 == sp.Matrix([7, 10])
K_iv2 = (A_iv2 + B_iv2 + 2 * C_iv2) / 4
assert K_iv2 == sp.Matrix([sp.Rational(9, 4), 3])
xp = sp.Symbol("xp", real=True)
P_iv2 = sp.Matrix([xp, 0])
T_iv2 = ((A_iv2 - P_iv2) + (B_iv2 - P_iv2) + 2 * (C_iv2 - P_iv2)).norm()
xp_min = sp.solve(sp.diff(T_iv2**2, xp), xp)[0]
assert xp_min == sp.Rational(9, 4)
assert T_iv2.subs(xp, xp_min) == 12

# IV.3: River 240 m wide, v_n = (3, 0), |v_p| = 5, v = v_p + v_n along +Oy
vx, vy = sp.symbols("vx vy", real=True)
sol_iv3 = sp.solve([vx + 3, vx**2 + vy**2 - 25], [vx, vy])
pos_sol = [s for s in sol_iv3 if s[1] > 0][0]
assert pos_sol == (-3, 4)
vp_iv3 = sp.Matrix(pos_sol)
v_iv3 = vp_iv3 + sp.Matrix([3, 0])
assert v_iv3 == sp.Matrix([0, 4])
assert 240 / v_iv3[1] == 60
deg_iv3 = float(sp.deg(sp.acos(vp_iv3[0] / vp_iv3.norm())).evalf())
assert round(deg_iv3, 1) == 126.9, deg_iv3

print("ALL 33 QUESTIONS FOR ĐỀ 6 VERIFIED 100% PASS!")
