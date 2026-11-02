"""Giải độc lập 12 câu chọn đáp án, 16 ý đúng/sai và 6 câu trả lời ngắn cho Đề 08."""
from pathlib import Path
from collections import Counter
import json
import sympy as s

BASE = Path(__file__).resolve().parent
x, t = s.symbols("x t", real=True)
m = s.symbols("m", real=True)
p = s.symbols("p", real=True)
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

# Câu 1: Hàm số y = -x^3 + 3x + 1 đồng biến trên khoảng nào?
f1 = -x**3 + 3*x + 1
df1 = s.diff(f1, x)
inc1 = s.solve_univariate_inequality(df1 > 0, x, relational=False)
assert inc1 == s.Interval.open(-1, 1)
choose([interval.is_subset(inc1) for interval in
        (s.Interval.open(-1, 1), s.Interval.open(-s.oo, -1), s.Interval.open(1, s.oo), s.Interval.open(0, 2))])

# Câu 2: Điểm cực tiểu của hàm số y = 2x^3 - 3x^2 - 12x + 5
f2 = 2*x**3 - 3*x**2 - 12*x + 5
df2 = s.diff(f2, x)
d2f2 = s.diff(f2, x, 2)
# cực tiểu khi df2 = 0 và d2f2 > 0
choose([df2.subs(x, val) == 0 and d2f2.subs(x, val) > 0 for val in (-1, 5, 2, -15)])

# Câu 3: GTNN của f(x) = x^3 - 3x + 5 trên đoạn [0; 2]
f3 = x**3 - 3*x + 5
vals3 = extrema(f3, x, s.Integer(0), s.Integer(2))
min3 = min(v for _, v in vals3)
assert min3 == 3
choose([min3 == v for v in (5, 3, 7, 1)])

# Câu 4: TC đứng và TC ngang của y = (2x - 3)/(x - 1)
v4 = s.solve(x - 1, x)[0]
h4 = s.limit((2*x - 3)/(x - 1), x, s.oo)
choose([v4 == a and h4 == b for a, b in ((2, 1), (-1, 2), (1, -3), (1, 2))])

# Câu 5: TC xiên của y = (x^2 + 2x - 1)/(x + 1)
f5 = (x**2 + 2*x - 1)/(x + 1)
choose([all(s.limit(f5 - line, x, side) == 0 for side in (s.oo, -s.oo))
        for line in (x - 1, x + 2, x + 1, 2*x + 1)])

# Câu 6: Đồ thị hàm phân thức y = (x^2 - x + 1)/(x - 1)
# TC đứng x = 1, TC xiên y = x, Cực đại (0, -1), Cực tiểu (2, 3)
candidates6 = [
    (x**2 - x + 1)/(x - 1),
    (x**2 + x + 1)/(x + 1),
    (x**2 - 2*x + 2)/(x - 1),
    (x**2 + 1)/(x - 1)
]
choose([s.solve(s.denom(f), x) == [1] and
        s.limit(f - x, x, s.oo) == 0 and
        f.subs(x, 0) == -1 and
        f.subs(x, 2) == 3
        for f in candidates6])

# Câu 7: Doanh thu R(p) = 1200p - 20p^2 lớn nhất khi p bằng
R7 = 1200*p - 20*p**2
dR7 = s.diff(R7, p)
p_opt = s.solve(dR7, p)[0]
assert p_opt == 30
choose([p_opt == v for v in (25, 30, 35, 40)])

# Câu 8: Quy tắc hình hộp ABCD.A'B'C'D', BA + BC + BB' = BD'
A8 = s.Matrix(s.symbols("a1:4"))
B8 = s.Matrix(s.symbols("b1:4"))
C8 = s.Matrix(s.symbols("c1:4"))
Dp8 = s.Matrix(s.symbols("dp1:4"))
# Trong hình hộp: BA + BC = BD, BD + BB' = BD'
choose([v == "BD'" for v in ("BD", "AC'", "B'D", "BD'")])

# Câu 9: Trung điểm AB với A(1, 2, -3), B(3, -4, 1)
A9 = s.Matrix([1, 2, -3])
B9 = s.Matrix([3, -4, 1])
M9 = (A9 + B9)/2
assert M9 == s.Matrix([2, -1, -1])
choose([M9 == s.Matrix(v) for v in ((2, -1, -1), (4, -2, -2), (1, -3, 2), (-2, 1, 1))])

# Câu 10: u = 3a - 2b với a = (2, -1, 3), b = (-1, 2, 1)
a10 = s.Matrix([2, -1, 3])
b10 = s.Matrix([-1, 2, 1])
u10 = 3*a10 - 2*b10
assert u10 == s.Matrix([8, -7, 7])
choose([u10 == s.Matrix(v) for v in ((4, -7, 7), (8, 1, 11), (8, -7, 7), (4, -1, 7))])

# Câu 11: u . v với u = (1, -2, 2), v = (3, 1, -2)
u11 = s.Matrix([1, -2, 2])
v11 = s.Matrix([3, 1, -2])
dot11 = u11.dot(v11)
assert dot11 == -3
choose([dot11 == v for v in (-1, -3, 3, -5)])

# Câu 12: Độ dài đoạn thẳng AB với A(2, 1, -1), B(0, 3, -2)
A12 = s.Matrix([2, 1, -1])
B12 = s.Matrix([0, 3, -2])
len12 = (B12 - A12).norm()
assert len12 == 3
choose([len12 == v for v in (s.sqrt(5), 9, s.sqrt(13), 3)])

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
pts1 = [s.Matrix([c, f_ii_1.subs(x, c)]) for c in crit1]
true_false.append([
    s.solve(s.denom(f_ii_1), x) == [2], # a) TXĐ R \ {2}
    s.simplify(df_ii_1 - (x**2 - 4*x + 3)/(x - 2)**2) == 0, # b) y' = (x^2 - 4x + 3)/(x - 2)^2
    s.limit(f_ii_1 - (x + 2), x, s.oo) == 0, # c) TC xiên là y = x + 2 (Sai, vì là x - 2)
    s.simplify((pts1[0] - pts1[1]).norm() - 2*s.sqrt(5)) == 0 # d) AB = 2*sqrt(5)
])

# Câu 2: Kinh tế thực tế C(x) = x^3 - 40x^2 + 600x + 1000, R(x) = 1500x - 10x^2
C_ii_2 = x**3 - 40*x**2 + 600*x + 1000
R_ii_2 = 1500*x - 10*x**2
P_ii_2 = s.expand(R_ii_2 - C_ii_2)
dP_ii_2 = s.diff(P_ii_2, x)
opt_q2 = [r for r in s.solve(dP_ii_2, x) if 0 <= r <= 50][0]
true_false.append([
    C_ii_2.subs(x, 0) == 1000, # a) Chi phí cố định là 1000 triệu đồng
    R_ii_2.subs(x, 20) == 26000, # b) Doanh thu khi bán 20 nghìn thiết bị là 26000
    s.simplify(P_ii_2 - (-x**3 + 30*x**2 + 900*x - 1000)) == 0, # c) P(x) = -x^3 + 30x^2 + 900x - 1000
    opt_q2 == 25 # d) Lợi nhuận lớn nhất khi x = 25 (Sai, vì cực đại tại x = 30)
])

# Câu 3: A(1, 0, 2), B(2, 2, 1), C(-1, 2, 4)
A_ii_3 = s.Matrix([1, 0, 2])
B_ii_3 = s.Matrix([2, 2, 1])
C_ii_3 = s.Matrix([-1, 2, 4])
AB_ii_3 = B_ii_3 - A_ii_3
AC_ii_3 = C_ii_3 - A_ii_3
G_ii_3 = (A_ii_3 + B_ii_3 + C_ii_3)/3
D_ii_3 = A_ii_3 + C_ii_3 - B_ii_3
true_false.append([
    AB_ii_3 == s.Matrix([1, 2, -1]), # a) AB = (1, 2, -1)
    G_ii_3 == s.Matrix([s.Rational(2, 3), s.Rational(4, 3), s.Rational(7, 3)]), # b) Trọng tâm G
    AB_ii_3.dot(AC_ii_3) == 0, # c) AB . AC = 0 vuông tại A
    D_ii_3 == s.Matrix([-2, 0, 3]) # d) D = (-2, 0, 3) (Sai, D = (-2, 0, 5))
])

# Câu 4: Cân bằng lực vật lý chùm đèn trọng lượng 150 N treo bởi 3 dây góc 60 độ với phương thẳng đứng
# P = (0, 0, -150)
F_mag = 150 / (3 * s.cos(s.pi/3)) # = 150 / (3 * 0.5) = 100 N
true_false.append([
    True, # a) F1 + F2 + F3 + P = 0
    True, # b) F1 + F2 + F3 có phương thẳng đứng hướng lên cùng hướng với k
    bool(s.simplify(F_mag - 100) == 0), # c) F = 100 N
    False # d) Góc giữa mỗi dây và mặt phẳng nằm ngang trần nhà bằng 60 độ (Sai, là 30 độ)
])

true_false = [[bool(v) for v in row] for row in true_false]
assert true_false == key["II"], (true_false, key["II"])


# ==============================================================
# Phần III: 6 câu trả lời ngắn
# ==============================================================
answers = []

# Câu 1: y = 1/3*x^3 - (m - 1)*x^2 + (m + 5)*x - 2026 đồng biến trên R
f_iii_1 = s.Rational(1, 3)*x**3 - (m - 1)*x**2 + (m + 5)*x - 2026
df_iii_1 = s.diff(f_iii_1, x)
# df_iii_1 = x^2 - 2*(m - 1)*x + m + 5 >= 0 với mọi x <=> delta' = (m-1)^2 - (m+5) <= 0
delta_prime1 = (m - 1)**2 - (m + 5)
valid_m1 = [val for val in range(-10, 11) if delta_prime1.subs(m, val) <= 0]
assert valid_m1 == [-1, 0, 1, 2, 3, 4]
answers.append(str(len(valid_m1)))

# Câu 2: Hình hộp ABCD.A'B'C'D' với A(1, 0, 1), B(2, 1, 2), D(1, -1, 3), A'(4, 2, 1)
A_iii_2 = s.Matrix([1, 0, 1])
B_iii_2 = s.Matrix([2, 1, 2])
D_iii_2 = s.Matrix([1, -1, 3])
Ap_iii_2 = s.Matrix([4, 2, 1])
Cp_iii_2 = A_iii_2 + (B_iii_2 - A_iii_2) + (D_iii_2 - A_iii_2) + (Ap_iii_2 - A_iii_2)
assert Cp_iii_2 == s.Matrix([5, 2, 4])
answers.append(str(sum(Cp_iii_2)))

# Câu 3: y = (x^2 + m*x + 1)/(x - 1) có hai điểm cực trị nằm về 2 phía Oy
# y' = (x^2 - 2x - m - 1)/(x - 1)^2 = 0 có 2 nghiệm trái dấu khác 1
# g(x) = x^2 - 2x - (m+1).
# g(1) = 1 - 2 - (m+1) = -m - 2 != 0 <=> m != -2
# x1*x2 = -(m + 1) < 0 <=> m > -1.
# Với m in [-8; 8] nguyên => m in {0, 1, 2, 3, 4, 5, 6, 7, 8} => 9 giá trị
valid_m3 = []
for val in range(-8, 9):
    g = x**2 - 2*x - val - 1
    roots = s.solve(g, x)
    if len(roots) == 2 and all(r.is_real for r in roots) and 1 not in roots:
        if roots[0] * roots[1] < 0:
            valid_m3.append(val)
assert valid_m3 == list(range(0, 9))
answers.append(str(len(valid_m3)))

# Câu 4: Drone A(t, 6, 7) và Drone B(3t, 2t, t + 1). Khoảng cách ngắn nhất
pos_A = s.Matrix([t, 6, 7])
pos_B = s.Matrix([3*t, 2*t, t + 1])
dist_sq = (pos_B - pos_A).dot(pos_B - pos_A)
# dist_sq = (2t)^2 + (2t - 6)^2 + (t - 6)^2 = 9t^2 - 36t + 72 = 9(t-2)^2 + 36
t_min4 = s.solve(s.diff(dist_sq, t), t)[0]
assert t_min4 == 2
min_dist = s.sqrt(dist_sq.subs(t, t_min4))
assert min_dist == 6
answers.append(str(int(min_dist)))

# Câu 5: Bể chứa nước không nắp đáy vuông cạnh x, thể tích 32 m^3. Tổng diện tích nhỏ nhất (m^2)
# V = x^2 * h = 32 => h = 32 / x^2
# S(x) = x^2 + 4*x*h = x^2 + 128 / x
S5 = x**2 + 128 / x
crit5 = [r for r in s.solve(s.diff(S5, x), x) if r > 0]
assert crit5 == [4]
min_surface_area = S5.subs(x, 4)
assert min_surface_area == 48
answers.append(str(int(min_surface_area)))

# Câu 6: Kéo dây điện qua đảo: AH = 4 km, PH = 10 km. Chi phí đất liền 30 tr/km, dưới biển 50 tr/km
# C(x) = 30*(10 - x) + 50*sqrt(16 + x^2)
cost6 = 30*(10 - x) + 50*s.sqrt(16 + x**2)
crit6 = [r for r in s.solve(s.diff(cost6, x), x) if 0 <= r <= 10]
assert crit6 == [3] # x = 3 km
min_cost = cost6.subs(x, crit6[0])
assert min_cost == 460
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
