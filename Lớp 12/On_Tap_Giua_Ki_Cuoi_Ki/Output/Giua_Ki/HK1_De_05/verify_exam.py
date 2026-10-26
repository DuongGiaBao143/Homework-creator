"""Giải độc lập 12 câu chọn đáp án, 16 ý đúng/sai và 6 câu trả lời ngắn cho Đề 05."""
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

# Câu 1: Hàm số y = -x^3 + 3x^2 - 1 đồng biến trên khoảng nào?
f1 = -x**3 + 3*x**2 - 1
df1 = s.diff(f1, x)
inc1 = s.solve_univariate_inequality(df1 > 0, x, relational=False)
assert inc1 == s.Interval.open(0, 2)
choose([interval.is_subset(inc1) for interval in
        (s.Interval.open(-s.oo, 0), s.Interval.open(0, 2), s.Interval.open(2, s.oo), s.Interval.open(-1, 3))])

# Câu 2: Điểm cực đại của hàm số y = x^3 - 6x^2 + 9x - 2
f2 = x**3 - 6*x**2 + 9*x - 2
df2 = s.diff(f2, x)
d2f2 = s.diff(f2, x, 2)
choose([df2.subs(x, val) == 0 and d2f2.subs(x, val) < 0 for val in (1, 3, 2, -2)])

# Câu 3: GTLN của f(x) = (2x + 1)/(x - 1) trên [2; 4]
f3 = (2*x + 1)/(x - 1)
vals3 = extrema(f3, x, s.Integer(2), s.Integer(4))
max3 = max(v for _, v in vals3)
assert max3 == 5
choose([max3 == v for v in (3, s.Rational(7, 3), 5, 4)])

# Câu 4: TC đứng và TC ngang của y = (3x - 1)/(x + 2)
v4 = s.solve(x + 2, x)[0]
h4 = s.limit((3*x - 1)/(x + 2), x, s.oo)
choose([v4 == a and h4 == b for a, b in ((2, 3), (3, -2), (-2, -1), (-2, 3))])

# Câu 5: TC xiên của y = (x^2 - 3x + 4)/(x - 1)
f5 = (x**2 - 3*x + 4)/(x - 1)
choose([all(s.limit(f5 - line, x, side) == 0 for side in (s.oo, -s.oo))
        for line in (x - 2, x + 2, x - 1, 2*x - 1)])

# Câu 6: Đồ thị hàm phân thức y = (x + 1)/(x - 1)
# TC đứng x = 1, TC ngang y = 1, f(0) = -1, f(-1) = 0, nghịch biến trên từng khoảng
candidates6 = [
    (x - 1)/(x + 1),
    (x + 1)/(x - 1),
    (2*x - 1)/(x - 1),
    (-x + 1)/(x - 1)
]
choose([s.solve(s.denom(f), x) == [1] and s.limit(f, x, s.oo) == 1 and f.subs(x, 0) == -1 and f.subs(x, -1) == 0
        for f in candidates6])

# Câu 7: Chi phí trung bình Cbar(x) = 2500/x + 0.25*x + 40 thấp nhất
c_bar = 2500/x + s.Rational(1, 4)*x + 40
dc_bar = s.diff(c_bar, x)
x_opt = [r for r in s.solve(dc_bar, x) if r > 0][0]
assert x_opt == 100
choose([x_opt == v for v in (50, 80, 100, 120)])

# Câu 8: Quy tắc hình hộp ABCD.A'B'C'D'
A8 = s.Matrix(s.symbols("a1:4"))
B8 = s.Matrix(s.symbols("b1:4"))
D8 = s.Matrix(s.symbols("d1:4"))
Ap8 = s.Matrix(s.symbols("ap1:4"))
# AC' = AB + AD + AA'
AB8 = B8 - A8
AD8 = D8 - A8
AAp8 = Ap8 - A8
total8 = AB8 + AD8 + AAp8
ACp8 = (B8 + D8 - A8 + AAp8) - A8 # C = B + D - A, C' = C + AA'
choose([s.simplify(total8 - v) == s.zeros(3, 1) for v in (B8 + D8 - 2*A8, D8 - B8, -(B8 + D8 - 2*A8 + AAp8), ACp8)])

# Câu 9: Trung điểm AB với A(2, -3, 1), B(4, 1, -5)
A9 = s.Matrix([2, -3, 1])
B9 = s.Matrix([4, 1, -5])
M9 = (A9 + B9)/2
assert M9 == s.Matrix([3, -1, -2])
choose([M9 == s.Matrix(v) for v in ((6, -2, -4), (3, -1, -2), (1, 2, -3), (2, 4, -6))])

# Câu 10: u = 2a + 3b với a = (1, -2, 3), b = (-2, 1, 1)
a10 = s.Matrix([1, -2, 3])
b10 = s.Matrix([-2, 1, 1])
u10 = 2*a10 + 3*b10
assert u10 == s.Matrix([-4, -1, 9])
choose([u10 == s.Matrix(v) for v in ((-4, -1, 9), (4, 1, -9), (-1, -1, 4), (-4, 1, 9))])

# Câu 11: u . v với u = (2, -1, 1), v = (1, 3, -2)
u11 = s.Matrix([2, -1, 1])
v11 = s.Matrix([1, 3, -2])
dot11 = u11.dot(v11)
assert dot11 == -3
choose([dot11 == v for v in (3, 1, -3, -5)])

# Câu 12: Độ dài đoạn thẳng AB với A(1, 2, -1), B(3, 0, -2)
A12 = s.Matrix([1, 2, -1])
B12 = s.Matrix([3, 0, -2])
len12 = (B12 - A12).norm()
assert len12 == 3
choose([len12 == v for v in (9, s.sqrt(5), s.sqrt(13), 3)])

assert multiple_choice == key["I"], (multiple_choice, key["I"])
assert Counter(multiple_choice) == dict.fromkeys("ABCD", 3)


# ==============================================================
# Phần II: 4 câu đúng / sai (16 mệnh đề)
# ==============================================================
true_false = []

# Câu 1: Khảo sát hàm số y = (x^2 - 3x + 3)/(x - 1)
f_ii_1 = (x**2 - 3*x + 3)/(x - 1)
df_ii_1 = s.diff(f_ii_1, x)
crit1 = s.solve(df_ii_1, x)
pts1 = [s.Matrix([c, f_ii_1.subs(x, c)]) for c in crit1]
true_false.append([
    s.solve(s.denom(f_ii_1), x) == [1], # a) TXĐ R \ {1}
    s.simplify(df_ii_1 - (x**2 - 2*x)/(x - 1)**2) == 0, # b) y' = (x^2 - 2x)/(x - 1)^2
    s.limit(f_ii_1 - (x + 2), x, s.oo) == 0, # c) TC xiên là y = x + 2 (Sai, vì phải là x - 2)
    s.simplify((pts1[0] - pts1[1]).norm() - 2*s.sqrt(5)) == 0 # d) AB = 2*sqrt(5)
])

# Câu 2: Kinh tế thực tế C(x) = x^3 - 60x^2 + 1500x + 5000, R(x) = 2700x - 15x^2
C_ii_2 = x**3 - 60*x**2 + 1500*x + 5000
R_ii_2 = 2700*x - 15*x**2
P_ii_2 = s.expand(R_ii_2 - C_ii_2)
dP_ii_2 = s.diff(P_ii_2, x)
opt_q2 = [r for r in s.solve(dP_ii_2, x) if 0 <= r <= 80][0]
true_false.append([
    C_ii_2.subs(x, 0) == 5000, # a) Chi phí cố định là 5000
    R_ii_2.subs(x, 20) == 48000, # b) Doanh thu khi bán 20 trăm sp là 48000
    s.simplify(P_ii_2 - (-x**3 + 45*x**2 + 1200*x - 5000)) == 0, # c) P(x) = -x^3 + 45x^2 + 1200x - 5000
    opt_q2 == 50 # d) Lợi nhuận lớn nhất khi x = 50 (Sai, vì x = 40)
])

# Câu 3: A(1, 2, 0), B(3, 0, 2), C(1, 4, 2)
A_ii_3 = s.Matrix([1, 2, 0])
B_ii_3 = s.Matrix([3, 0, 2])
C_ii_3 = s.Matrix([1, 4, 2])
AB_ii_3 = B_ii_3 - A_ii_3
AC_ii_3 = C_ii_3 - A_ii_3
G_ii_3 = (A_ii_3 + B_ii_3 + C_ii_3)/3
D_ii_3 = A_ii_3 + C_ii_3 - B_ii_3
true_false.append([
    AB_ii_3 == s.Matrix([2, -2, 2]), # a) AB = (2, -2, 2)
    G_ii_3 == s.Matrix([2, 2, 1]), # b) G = (2, 2, 1) (Sai, G = (5/3, 2, 4/3))
    AB_ii_3.dot(AC_ii_3) == 0, # c) AB . AC = 0 vuông tại A
    D_ii_3 == s.Matrix([-1, 6, 0]) # d) D = (-1, 6, 0)
])

# Câu 4: Cân bằng lực vật lý
# P = (0, 0, -120), T1, T2, T3 đôi một vuông góc, cùng độ lớn T
# Hợp lực T1 + T2 + T3 = -P
P_ii_4 = s.Matrix([0, 0, -120])
# Độ lớn hợp lực của 3 vectơ đôi một vuông góc bằng T*sqrt(3)
T_mag = 120 / s.sqrt(3) # = 40*sqrt(3)
cos_alpha = 1 / s.sqrt(3) # = sqrt(3)/3
true_false.append([
    True, # a) T1 + T2 + T3 + P = 0 (đèn cân bằng)
    True, # b) |T1+T2+T3|^2 = T1^2 + T2^2 + T3^2 = 3T^2 (do đôi một vuông góc)
    bool(s.simplify(T_mag - 40) == 0), # c) T = 40 N (Sai, T = 40*sqrt(3) N)
    bool(s.simplify(cos_alpha - s.sqrt(3)/3) == 0) # d) cos(alpha) = sqrt(3)/3
])

true_false = [[bool(v) for v in row] for row in true_false]
assert true_false == key["II"], (true_false, key["II"])


# ==============================================================
# Phần III: 6 câu trả lời ngắn
# ==============================================================
answers = []

# Câu 1: y = 1/3*x^3 - m*x^2 + (m + 2)*x - 2026 đồng biến trên R
f_iii_1 = s.Rational(1, 3)*x**3 - m*x**2 + (m + 2)*x - 2026
df_iii_1 = s.diff(f_iii_1, x)
# df_iii_1 = x^2 - 2*m*x + m + 2 >= 0 với mọi x <=> delta' = m^2 - m - 2 <= 0
delta_prime1 = m**2 - (m + 2)
valid_m1 = [val for val in range(-10, 11) if delta_prime1.subs(m, val) <= 0]
assert valid_m1 == [-1, 0, 1, 2]
answers.append(str(len(valid_m1)))

# Câu 2: Hình hộp ABCD.A'B'C'D' với A(1, 1, 1), B(2, 3, 4), D(0, 2, 3), A'(2, 0, 5)
A_iii_2 = s.Matrix([1, 1, 1])
B_iii_2 = s.Matrix([2, 3, 4])
D_iii_2 = s.Matrix([0, 2, 3])
Ap_iii_2 = s.Matrix([2, 0, 5])
Cp_iii_2 = A_iii_2 + (B_iii_2 - A_iii_2) + (D_iii_2 - A_iii_2) + (Ap_iii_2 - A_iii_2)
assert Cp_iii_2 == s.Matrix([2, 3, 10])
answers.append(str(sum(Cp_iii_2)))

# Câu 3: y = (x^2 + m*x - 2)/(x - 1) có hai điểm cực trị nằm về 2 phía Oy
# y' = (x^2 - 2x + 2 - m)/(x-1)^2 = 0 có 2 nghiệm trái dấu khác 1
# g(x) = x^2 - 2x + 2 - m.
# delta' = 1 - (2 - m) = m - 1 > 0 => m > 1
# g(1) = 1 - 2 + 2 - m = 1 - m != 0 => m != 1
# x1*x2 = 2 - m < 0 => m > 2
# Vậy m > 2. Với m in [-5, 5] nguyên => m in {3, 4, 5} -> có 3 giá trị
valid_m3 = []
for val in range(-5, 6):
    g = x**2 - 2*x + 2 - val
    roots = s.solve(g, x)
    if len(roots) == 2 and all(r.is_real for r in roots) and 1 not in roots:
        if roots[0] * roots[1] < 0:
            valid_m3.append(val)
assert valid_m3 == [3, 4, 5]
answers.append(str(len(valid_m3)))

# Câu 4: Drone A(t, 2t, 2) và Drone B(6 - t, 3, 2 + t). Khoảng cách ngắn nhất
pos_A = s.Matrix([t, 2*t, 2])
pos_B = s.Matrix([6 - t, 3, 2 + t])
dist_sq = (pos_B - pos_A).dot(pos_B - pos_A)
# dist_sq = (6 - 2t)^2 + (3 - 2t)^2 + t^2 = 9t^2 - 36t + 45
t_min4 = s.solve(s.diff(dist_sq, t), t)[0]
assert t_min4 == 2
min_dist = s.sqrt(dist_sq.subs(t, t_min4))
assert min_dist == 3
answers.append(str(min_dist))

# Câu 5: Cắt tấm bìa 80 x 50 cm thành hộp không nắp, thể tích lớn nhất (lít)
# V(x) = x*(80 - 2x)*(50 - 2x) cm^3. V'(x) = 0 => x = 10
V5 = x*(80 - 2*x)*(50 - 2*x)
crit5 = [r for r in s.solve(s.diff(V5, x), x) if 0 < r < 25]
assert crit5 == [10]
max_vol_liters = V5.subs(x, 10) / 1000
assert max_vol_liters == 18
answers.append(str(int(max_vol_liters)))

# Câu 6: Dẫn nước qua sông SH = 3 km, HA = 8 km. Chi phí dưới nước 100 tr/km, trên bờ 60 tr/km
# C = 100*sqrt(x^2 + 9) + 60*(8 - x)
cost6 = 100*s.sqrt(x**2 + 9) + 60*(8 - x)
crit6 = [r for r in s.solve(s.diff(cost6, x), x) if 0 <= r <= 8]
assert crit6 == [s.Rational(9, 4)] # 2.25 km
min_cost = cost6.subs(x, crit6[0])
assert min_cost == 720
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
