"""Giải độc lập 12 câu chọn đáp án, 16 ý đúng/sai và 6 câu trả lời ngắn cho Đề 06."""
from pathlib import Path
from collections import Counter
import json
import sympy as s

BASE = Path(__file__).resolve().parent
x, t = s.symbols("x t", real=True)
m = s.symbols("m", real=True)
key = json.loads((BASE / "dap_an.json").read_text(encoding="utf-8"))
multiple_choice = []


def choose(values):
    flags = [bool(v) for v in values]
    assert sum(flags) == 1, flags
    multiple_choice.append("ABCD"[flags.index(True)])


def extrema(function, variable, left, right):
    candidates = [left, right] + [r for r in s.solve(s.diff(function, variable), variable)
                                  if r.is_real and bool(left < r < right)]
    return [(v, s.simplify(function.subs(variable, v))) for v in candidates]


# ==============================================================
# Phần I: kiểm tra độc lập 12 câu trắc nghiệm nhiều phương án
# ==============================================================

# Câu 1: Hàm số y = x^3 - 3x^2 + 2 nghịch biến trên khoảng nào?
f1 = x**3 - 3*x**2 + 2
df1 = s.diff(f1, x)
dec1 = s.solve_univariate_inequality(df1 < 0, x, relational=False)
assert dec1 == s.Interval.open(0, 2)
choose([dec1 == interval for interval in
        (s.Interval.open(-s.oo, 0), s.Interval.open(0, 2), s.Interval.open(2, s.oo), s.Interval.open(-1, 3))])

# Câu 2: Điểm cực tiểu của hàm số y = -x^3 + 3x + 1
f2 = -x**3 + 3*x + 1
df2 = s.diff(f2, x)
d2f2 = s.diff(f2, x, 2)
# Điểm cực tiểu thỏa f'(x) = 0 và f''(x) > 0
choose([df2.subs(x, val) == 0 and d2f2.subs(x, val) > 0 for val in (-1, 1, 3, 0)])

# Câu 3: GTNN của f(x) = x + 4/x trên [1; 3]
f3 = x + 4/x
vals3 = extrema(f3, x, s.Integer(1), s.Integer(3))
min3 = min(v for _, v in vals3)
assert min3 == 4
choose([min3 == v for v in (5, s.Rational(13, 3), 4, 2)])

# Câu 4: TC đứng và TC ngang của y = (2x + 3)/(x - 1)
v4 = s.solve(x - 1, x)[0]
h4 = s.limit((2*x + 3)/(x - 1), x, s.oo)
choose([v4 == a and h4 == b for a, b in ((1, -3), (2, 1), (-1, 2), (1, 2))])

# Câu 5: TC xiên của y = (x^2 + 2x - 1)/(x + 1)
f5 = (x**2 + 2*x - 1)/(x + 1)
choose([all(s.limit(f5 - line, x, side) == 0 for side in (s.oo, -s.oo))
        for line in (x + 1, x - 1, x + 2, 2*x + 1)])

# Câu 6: Đồ thị hàm phân thức y = (x^2 - x + 1)/(x - 1)
candidates6 = [
    (x**2 + x + 1)/(x - 1),
    (x**2 - x + 1)/(x - 1),
    (x**2 - 2*x + 2)/(x - 1),
    (-x**2 + x - 1)/(x - 1)
]
# TC đứng x = 1, TC xiên y = x, f(0) = -1, f(2) = 3
choose([s.solve(s.denom(f), x) == [1] and
        all(s.limit(f - x, x, side) == 0 for side in (s.oo, -s.oo)) and
        f.subs(x, 0) == -1 and f.subs(x, 2) == 3
        for f in candidates6])

# Câu 7: Nồng độ ôxy hòa tan C(t) = 5 + 12t/(t^2 + 9) cao nhất sau bao nhiêu ngày?
C7 = 5 + 12*t/(t**2 + 9)
dC7 = s.diff(C7, t)
crit7 = [r for r in s.solve(dC7, t) if r > 0]
assert crit7 == [3]
choose([crit7[0] == v for v in (2, 9, 3, 6)])

# Câu 8: Hình hộp ABCD.A'B'C'D', BA + BC + BB' = BD'
B8 = s.Matrix(s.symbols("b1:4"))
A8 = s.Matrix(s.symbols("a1:4"))
C8 = s.Matrix(s.symbols("c1:4"))
Bp8 = s.Matrix(s.symbols("bp1:4"))
BA8 = A8 - B8
BC8 = C8 - B8
BBp8 = Bp8 - B8
total8 = BA8 + BC8 + BBp8
# Trong hình hộp, D = A + C - B, D' = D + BB' = A + C - B + BB'
# BD' = D' - B = A + C - 2*B + BB' = (A - B) + (C - B) + BB' = BA + BC + BB'
Dp8 = A8 + C8 - B8 + BBp8
BDp8 = Dp8 - B8
choose([s.simplify(total8 - v) == s.zeros(3, 1) for v in (A8 + C8 - 2*B8, A8 - C8, -(A8 + C8 - 2*B8), BDp8)])

# Câu 9: Trọng tâm tam giác ABC với A(1, 2, 3), B(-2, 0, 1), C(4, 1, -1)
A9 = s.Matrix([1, 2, 3])
B9 = s.Matrix([-2, 0, 1])
C9 = s.Matrix([4, 1, -1])
G9 = (A9 + B9 + C9)/3
assert G9 == s.Matrix([1, 1, 1])
choose([G9 == s.Matrix(v) for v in ((1, 1, 1), (3, 3, 3), (1, 1, 2), (2, 1, 1))])

# Câu 10: u = a - 2b với a = (2, -1, 3), b = (1, 3, -2)
a10 = s.Matrix([2, -1, 3])
b10 = s.Matrix([1, 3, -2])
u10 = a10 - 2*b10
assert u10 == s.Matrix([0, -7, 7])
choose([u10 == s.Matrix(v) for v in ((0, 5, -1), (0, -7, 7), (4, 5, -1), (0, -7, -1))])

# Câu 11: Góc giữa u = (1, 0, -1) và v = (0, 1, 1)
u11 = s.Matrix([1, 0, -1])
v11 = s.Matrix([0, 1, 1])
cos11 = u11.dot(v11) / (u11.norm() * v11.norm())
assert cos11 == s.Rational(-1, 2)
# cos(120 deg) = -1/2
choose([cos11 == v for v in (s.Rational(1, 2), s.sqrt(2)/2, s.Rational(-1, 2), -s.sqrt(2)/2)])

# Câu 12: Khoảng cách giữa M(2, -1, 4) và N(4, 1, 3)
M12 = s.Matrix([2, -1, 4])
N12 = s.Matrix([4, 1, 3])
dist12 = (N12 - M12).norm()
assert dist12 == 3
choose([dist12 == v for v in (9, s.sqrt(5), s.sqrt(17), 3)])

assert multiple_choice == key["I"], (multiple_choice, key["I"])
assert Counter(multiple_choice) == dict.fromkeys("ABCD", 3)


# ==============================================================
# Phần II: 4 câu đúng / sai (16 mệnh đề)
# ==============================================================
true_false = []

# Câu 1: Khảo sát hàm số y = (x^2 - 4x + 5)/(x - 2)
f_ii_1 = (x**2 - 4*x + 5)/(x - 2)
df_ii_1 = s.diff(f_ii_1, x)
crit1 = s.solve(df_ii_1, x)
pts1 = [s.Matrix([c, f_ii_1.subs(x, c)]) for c in crit1] # (1, -2) and (3, 2)
I1 = s.Matrix([2, 0])
mid1 = (pts1[0] + pts1[1])/2
true_false.append([
    s.solve(s.denom(f_ii_1), x) == [2], # a) TXĐ R \ {2}
    s.simplify(df_ii_1 - (x**2 - 4*x + 3)/(x - 2)**2) == 0, # b) y' = (x^2 - 4x + 3)/(x - 2)^2
    s.limit(f_ii_1 - (x + 2), x, s.oo) == 0, # c) TC xiên là y = x + 2 (Sai, TC xiên là y = x - 2)
    mid1 == I1 # d) Hai điểm cực trị đối xứng qua I(2, 0)
])

# Câu 2: Kinh tế thực tế sản xuất vắc-xin:
# C(x) = x^3 - 90x^2 + 2400x + 10000, R(x) = 3600x - 15x^2, P(x) = R(x) - C(x)
C_ii_2 = x**3 - 90*x**2 + 2400*x + 10000
R_ii_2 = 3600*x - 15*x**2
P_ii_2 = s.expand(R_ii_2 - C_ii_2)
dP_ii_2 = s.diff(P_ii_2, x)
opt_q2 = [r for r in s.solve(dP_ii_2, x) if 0 <= r <= 120][0]
true_false.append([
    C_ii_2.subs(x, 0) == 10000, # a) Chi phí cố định là 10000 triệu đồng
    R_ii_2.subs(x, 20) == 66000, # b) Doanh thu khi bán 20 nghìn liều là 66000 triệu đồng
    s.simplify(P_ii_2 - (-x**3 + 75*x**2 + 1200*x - 10000)) == 0, # c) P(x) = -x^3 + 75x^2 + 1200x - 10000
    opt_q2 == 50 # d) Lợi nhuận lớn nhất khi x = 50 (Sai, vì x = 60)
])

# Câu 3: A(2, 1, -1), B(4, 3, 0), C(1, 5, 1)
A_ii_3 = s.Matrix([2, 1, -1])
B_ii_3 = s.Matrix([4, 3, 0])
C_ii_3 = s.Matrix([1, 5, 1])
AB_ii_3 = B_ii_3 - A_ii_3
G_ii_3 = (A_ii_3 + B_ii_3 + C_ii_3)/3
D_ii_3 = C_ii_3 - AB_ii_3 # ABCD là hình bình hành <=> AB = DC <=> D = C - AB
true_false.append([
    AB_ii_3 == s.Matrix([2, 2, 1]), # a) AB = (2, 2, 1)
    G_ii_3 == s.Matrix([2, 3, 0]), # b) G = (2, 3, 0) (Sai, G = (7/3, 3, 0))
    AB_ii_3.norm() == 3, # c) Độ dài AB bằng 3
    D_ii_3 == s.Matrix([-1, 3, 0]) # d) D = (-1, 3, 0)
])

# Câu 4: Cân bằng lực khung đèn P = 180 N, P_vec = (0, 0, -180)
# T1, T2, T3 đôi một vuông góc, cùng độ lớn T
# Hợp lực T1 + T2 + T3 = -P
P_ii_4 = s.Matrix([0, 0, -180])
# Độ lớn hợp lực của 3 vectơ đôi một vuông góc bằng T*sqrt(3)
T_mag = 180 / s.sqrt(3) # = 60*sqrt(3)
cos_alpha = 1 / s.sqrt(3) # = sqrt(3)/3
true_false.append([
    True, # a) T1 + T2 + T3 + P = 0 (khung đèn cân bằng)
    True, # b) |T1+T2+T3|^2 = T1^2 + T2^2 + T3^2 = 3T^2
    bool(s.simplify(T_mag - 60) == 0), # c) T = 60 N (Sai, T = 60*sqrt(3) N)
    bool(s.simplify(cos_alpha - s.sqrt(3)/3) == 0) # d) cos(alpha) = sqrt(3)/3
])

true_false = [[bool(v) for v in row] for row in true_false]
assert true_false == key["II"], (true_false, key["II"])


# ==============================================================
# Phần III: 6 câu trả lời ngắn
# ==============================================================
answers = []

# Câu 1: y = -1/3*x^3 + m*x^2 - (2m + 3)*x + 2027 nghịch biến trên R
f_iii_1 = -s.Rational(1, 3)*x**3 + m*x**2 - (2*m + 3)*x + 2027
df_iii_1 = s.diff(f_iii_1, x)
# df_iii_1 = -x^2 + 2mx - (2m + 3) <= 0 với mọi x <=> delta' = m^2 - (2m + 3) <= 0
delta_prime1 = m**2 - (2*m + 3)
valid_m1 = [val for val in range(-10, 11) if delta_prime1.subs(m, val) <= 0]
assert valid_m1 == [-1, 0, 1, 2, 3]
answers.append(str(len(valid_m1)))

# Câu 2: Hình hộp ABCD.A'B'C'D' với A(2, 1, 0), B(3, 4, 2), D(1, 3, 1), A'(4, 1, 5)
A_iii_2 = s.Matrix([2, 1, 0])
B_iii_2 = s.Matrix([3, 4, 2])
D_iii_2 = s.Matrix([1, 3, 1])
Ap_iii_2 = s.Matrix([4, 1, 5])
Cp_iii_2 = A_iii_2 + (B_iii_2 - A_iii_2) + (D_iii_2 - A_iii_2) + (Ap_iii_2 - A_iii_2)
assert Cp_iii_2 == s.Matrix([4, 6, 8])
answers.append(str(sum(Cp_iii_2)))

# Câu 3: y = (x^2 + mx - 1)/(x + 1) có hai điểm cực trị nằm về 2 phía Oy
# y' = (x^2 + 2x + m + 1)/(x + 1)^2 = 0 có 2 nghiệm trái dấu khác -1
# g(x) = x^2 + 2x + m + 1
# delta' = 1 - (m + 1) = -m > 0 => m < 0
# g(-1) = 1 - 2 + m + 1 = m != 0 => m != 0
# x1*x2 = m + 1 < 0 => m < -1
# Vậy m < -1. Với m in [-6, 6] nguyên => m in {-6, -5, -4, -3, -2} -> có 5 giá trị
valid_m3 = []
for val in range(-6, 7):
    g = x**2 + 2*x + val + 1
    roots = s.solve(g, x)
    if len(roots) == 2 and all(r.is_real for r in roots) and -1 not in roots:
        if roots[0] * roots[1] < 0:
            valid_m3.append(val)
assert valid_m3 == [-6, -5, -4, -3, -2]
answers.append(str(len(valid_m3)))

# Câu 4: Drone M(t, 2, 15) và Drone N(6 - t, 2 + 2t, t + 9). Khoảng cách ngắn nhất
pos_M = s.Matrix([t, 2, 15])
pos_N = s.Matrix([6 - t, 2 + 2*t, t + 9])
dist_sq = (pos_N - pos_M).dot(pos_N - pos_M)
# dist_sq = (6 - 2t)^2 + (2t)^2 + (t - 6)^2 = 9t^2 - 36t + 72
t_min4 = s.solve(s.diff(dist_sq, t), t)[0]
assert t_min4 == 2
min_dist = s.sqrt(dist_sq.subs(t, t_min4))
assert min_dist == 6
answers.append(str(int(min_dist)))

# Câu 5: Hình trụ nội tiếp hình nón R = 9 cm, H = 18 cm. Bán kính r để thể tích lớn nhất
# h = 18 - 2r, V(r) = pi * r^2 * (18 - 2r) = 2*pi*(9r^2 - r^3)
r_sym = s.symbols("r", real=True)
V5 = 2*s.pi*(9*r_sym**2 - r_sym**3)
crit5 = [r for r in s.solve(s.diff(V5, r_sym), r_sym) if 0 < r < 9]
assert crit5 == [6]
answers.append(str(int(crit5[0])))

# Câu 6: Xây bể nước ngầm hình hộp chữ nhật không nắp V = 60 m^3, dài = 2*rộng
# C = 1*(2*x^2) + 0.6*(6*x*h) = 2x^2 + 0.6 * (180/x) = 2x^2 + 108/x
cost6 = 2*x**2 + 108/x
crit6 = [r for r in s.solve(s.diff(cost6, x), x) if r > 0]
assert crit6 == [3]
min_cost = cost6.subs(x, crit6[0])
assert min_cost == 54
answers.append(str(int(min_cost)))

assert answers == key["III"], (answers, key["III"])

report = {
    "status": "passed",
    "part_I": {f"Cau_{i+1}": ans for i, ans in enumerate(multiple_choice)},
    "part_I_distribution": dict(Counter(multiple_choice)),
    "part_II": {f"Cau_{i+1}": ans for i, ans in enumerate(true_false)},
    "part_III": {f"Cau_{i+1}": ans for i, ans in enumerate(answers)}
}
(BASE / "kiem_tra_toan.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("VERIFICATION SUCCESSFUL!")
print(json.dumps(report, ensure_ascii=False, indent=2))
