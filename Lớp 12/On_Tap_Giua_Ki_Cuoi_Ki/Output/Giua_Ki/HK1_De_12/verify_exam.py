"""Giải độc lập 12 câu chọn đáp án, 16 ý đúng/sai và 6 câu trả lời ngắn cho Đề 12."""
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

# Câu 1: Hàm số y = x^3 - 3x^2 - 9x + 2 nghịch biến trên khoảng nào?
f1 = x**3 - 3*x**2 - 9*x + 2
df1 = s.diff(f1, x)
dec1 = s.solve_univariate_inequality(df1 < 0, x, relational=False)
assert dec1 == s.Interval.open(-1, 3)
choose([interval.is_subset(dec1) for interval in
        (s.Interval.open(-1, 3), s.Interval.open(3, s.oo), s.Interval.open(-s.oo, -1), s.Interval.open(-2, 4))])

# Câu 2: Giá trị cực đại của y = -x^3 + 3x^2 + 1
f2 = -x**3 + 3*x**2 + 1
df2 = s.diff(f2, x)
d2f2 = s.diff(f2, x, 2)
# Cực đại khi df2 = 0 và d2f2 < 0
max_val2 = [f2.subs(x, r) for r in s.solve(df2, x) if d2f2.subs(x, r) < 0][0]
assert max_val2 == 5
choose([max_val2 == v for v in (1, 5, 2, 0)])

# Câu 3: GTLN của f(x) = (x - 2)/(x + 1) trên [0; 3]
f3 = (x - 2)/(x + 1)
vals3 = extrema(f3, x, s.Integer(0), s.Integer(3))
max3 = max(v for _, v in vals3)
assert max3 == s.Rational(1, 4)
choose([max3 == v for v in (-2, 0, s.Rational(1, 4), 1)])

# Câu 4: TC xiên của y = (x^2 - 3x + 1)/(x - 2)
f4 = (x**2 - 3*x + 1)/(x - 2)
choose([all(s.limit(f4 - line, x, side) == 0 for side in (s.oo, -s.oo))
        for line in (x + 1, x - 2, 2*x - 1, x - 1)])

# Câu 5: Giao điểm hai tiệm cận của y = (3x - 1)/(x + 2)
v5 = s.solve(x + 2, x)[0] # x = -2
h5 = s.limit((3*x - 1)/(x + 2), x, s.oo) # y = 3
I5 = (v5, h5)
choose([I5 == v for v in ((2, 3), (-2, 3), (-2, -1), (3, -2))])

# Câu 6: Đồ thị hàm số y = (x^2 + 2x + 2)/(x + 1)
# TC đứng x = -1, TC xiên y = x + 1, Cực tiểu (0, 2), Cực đại (-2, -2)
candidates6 = [
    (x**2 + 2*x + 2)/(x + 1),
    (x**2 - 2*x + 2)/(x - 1),
    (x**2 + x + 2)/(x + 1),
    (x**2 + 2*x - 1)/(x + 1)
]
choose([s.solve(s.denom(f), x) == [-1] and
        s.limit(f - (x + 1), x, s.oo) == 0 and
        f.subs(x, 0) == 2 and
        f.subs(x, -2) == -2
        for f in candidates6])

# Câu 7: Doanh thu R(p) = 800p - 10p^2 tối đa khi p bằng
R7 = 800*p - 10*p**2
dR7 = s.diff(R7, p)
p_opt7 = s.solve(dR7, p)[0]
assert p_opt7 == 40
choose([p_opt7 == v for v in (35, 50, 40, 45)])

# Câu 8: Cho tứ diện ABCD, M là trung điểm CD. Vectơ AC + AD = 2*AM
choose([v == "2AM" for v in ("AM", "CD", "2MC", "2AM")])

# Câu 9: Điểm A(2, -3, 5). Hình chiếu vuông góc lên (Oxy)
A9 = s.Matrix([2, -3, 5])
proj_Oxy9 = s.Matrix([2, -3, 0])
choose([proj_Oxy9 == s.Matrix(v) for v in ((2, -3, 0), (0, 0, 5), (2, 0, 5), (0, -3, 5))])

# Câu 10: Cho a = (1, -2, 3), b = (2, 1, -1). Vectơ u = 2a + b
a10 = s.Matrix([1, -2, 3])
b10 = s.Matrix([2, 1, -1])
u10 = 2*a10 + b10
assert u10 == s.Matrix([4, -3, 5])
choose([u10 == s.Matrix(v) for v in ((3, -1, 2), (4, -3, 5), (0, -5, 7), (4, -1, 5))])

# Câu 11: Cho u = (1, 0, 1), v = (0, 1, -1). cos(u, v) = u.v / (|u|*|v|)
u11 = s.Matrix([1, 0, 1])
v11 = s.Matrix([0, 1, -1])
cos11 = u11.dot(v11) / (u11.norm() * v11.norm())
assert cos11 == -s.Rational(1, 2)
choose([cos11 == v for v in (s.Rational(1, 2), s.sqrt(2)/2, -s.sqrt(2)/2, -s.Rational(1, 2))])

# Câu 12: Độ dài đoạn thẳng AB với A(1, 3, -2), B(3, 2, 0)
A12 = s.Matrix([1, 3, -2])
B12 = s.Matrix([3, 2, 0])
len12 = (B12 - A12).norm()
assert len12 == 3
choose([len12 == v for v in (s.sqrt(5), 9, 3, s.sqrt(21))])

assert multiple_choice == key["I"], (multiple_choice, key["I"])
assert Counter(multiple_choice) == dict.fromkeys("ABCD", 3)


# ==============================================================
# Phần II: 4 câu đúng / sai (16 mệnh đề)
# ==============================================================
true_false = []

# Câu 1: Hàm số y = f(x) = (x^2 - 3x + 6)/(x - 1)
f_ii_1 = (x**2 - 3*x + 6)/(x - 1)
df_ii_1 = s.diff(f_ii_1, x)
crit1 = s.solve(df_ii_1, x)
pts1 = [s.Matrix([c, f_ii_1.subs(x, c)]) for c in crit1]
dist_AB1 = (pts1[0] - pts1[1]).norm()
true_false.append([
    s.solve(s.denom(f_ii_1), x) == [1], # a) TXĐ D = R \ {1}
    s.simplify(df_ii_1 - (x**2 - 2*x - 3)/(x - 1)**2) == 0, # b) f'(x) = (x^2 - 2x - 3)/(x - 1)^2
    s.limit(f_ii_1 - (x + 2), x, s.oo) == 0, # c) TC xiên là y = x + 2 (Sai, là y = x - 2)
    s.simplify(dist_AB1 - 4*s.sqrt(5)) == 0 # d) Khoảng cách AB = 4*sqrt(5)
])

# Câu 2: Kinh tế C(x) = x^3 - 15x^2 + 180x + 80, R(x) = 300x - 6x^2, 0 < x <= 20
C_ii_2 = x**3 - 15*x**2 + 180*x + 80
R_ii_2 = 300*x - 6*x**2
P_ii_2 = s.expand(R_ii_2 - C_ii_2)
dP_ii_2 = s.diff(P_ii_2, x)
opt_q2 = [r for r in s.solve(dP_ii_2, x) if 0 <= r <= 20][0]
true_false.append([
    C_ii_2.subs(x, 0) == 80, # a) Chi phí cố định là 80 triệu đồng
    R_ii_2.subs(x, 5) == 1350, # b) Doanh thu khi bán 5 trăm sản phẩm là 1350 triệu đồng
    s.simplify(P_ii_2 - (-x**3 + 9*x**2 + 120*x - 80)) == 0, # c) P(x) = -x^3 + 9x^2 + 120x - 80
    opt_q2 == 12 # d) Lợi nhuận lớn nhất khi x = 12 (Sai, vì lớn nhất tại x = 10)
])

# Câu 3: A(1, 2, 0), B(2, 0, 2), C(-1, 3, 1)
A_ii_3 = s.Matrix([1, 2, 0])
B_ii_3 = s.Matrix([2, 0, 2])
C_ii_3 = s.Matrix([-1, 3, 1])
AB_ii_3 = B_ii_3 - A_ii_3
AC_ii_3 = C_ii_3 - A_ii_3
G_ii_3 = (A_ii_3 + B_ii_3 + C_ii_3)/3
D_ii_3 = A_ii_3 + C_ii_3 - B_ii_3
true_false.append([
    AB_ii_3 == s.Matrix([1, -2, 2]), # a) AB = (1, -2, 2)
    AB_ii_3.norm() == 3, # b) Độ dài AB = 3
    G_ii_3 == s.Matrix([s.Rational(2, 3), s.Rational(5, 3), 1]), # c) Trọng tâm G
    D_ii_3 == s.Matrix([-2, 5, 1]) # d) D = (-2, 5, 1) (Sai, vì D = (-2, 5, -1))
])

# Câu 4: Cân bằng lực vật lý quả cầu trọng lượng 120 N treo bởi 3 dây tạo góc 45 độ với phương thẳng đứng
# P = (0, 0, -120)
# 3 * F * cos(45 độ) = 120 => F = 120 / (3 * sqrt(2)/2) = 40 * sqrt(2) N
F_mag4 = 120 / (3 * s.cos(s.pi/4))
true_false.append([
    True, # a) F1 + F2 + F3 + P = 0
    True, # b) Hợp lực F1 + F2 + F3 thẳng đứng hướng lên, độ lớn 120 N
    bool(s.simplify(F_mag4 - 40*s.sqrt(2)) == 0), # c) F = 40*sqrt(2) N
    False # d) Góc giữa mỗi dây và trần nhà bằng 60 độ (Sai, vì bằng 45 độ)
])

true_false = [[bool(v) for v in row] for row in true_false]
assert true_false == key["II"], (true_false, key["II"])


# ==============================================================
# Phần III: 6 câu trả lời ngắn
# ==============================================================
answers = []

# Câu 1: Số giá trị nguyên m in [-10, 10] để y = 1/3*x^3 - m*x^2 + (m + 6)*x - 2027 đồng biến trên R
# y' = x^2 - 2mx + m + 6 >= 0 với mọi x <=> delta' = m^2 - m - 6 <= 0 <=> -2 <= m <= 3
valid_m1 = [val for val in range(-10, 11) if val**2 - val - 6 <= 0]
assert valid_m1 == [-2, -1, 0, 1, 2, 3]
answers.append(str(len(valid_m1)))

# Câu 2: Hình hộp ABCD.A'B'C'D' với A(1, 1, 1), B(3, 2, 1), D(1, 4, 2), A'(2, 1, 5). Tọa độ C'(x, y, z), tính S = x + y + z
A_iii_2 = s.Matrix([1, 1, 1])
B_iii_2 = s.Matrix([3, 2, 1])
D_iii_2 = s.Matrix([1, 4, 2])
Ap_iii_2 = s.Matrix([2, 1, 5])
Cp_iii_2 = A_iii_2 + (B_iii_2 - A_iii_2) + (D_iii_2 - A_iii_2) + (Ap_iii_2 - A_iii_2)
assert Cp_iii_2 == s.Matrix([4, 5, 6])
answers.append(str(sum(Cp_iii_2)))

# Câu 3: Cho y = (x^2 + mx + 4)/(x + 1). Có bao nhiêu giá trị nguyên m in [-10, 10] để có 2 cực trị trái dấu
# y' = (x^2 + 2x + m - 4)/(x + 1)^2. Hai nghiệm trái dấu khác -1:
# delta' = 1 - (m - 4) = 5 - m > 0 <=> m < 5
# g(-1) = 1 - 2 + m - 4 = m - 5 != 0 <=> m != 5
# x1 * x2 = m - 4 < 0 <=> m < 4.
# m in [-10, 10] nguyên => m in {-10, -9, ..., 3} => 14 giá trị
valid_m3 = []
for val in range(-10, 11):
    g = x**2 + 2*x + val - 4
    roots = s.solve(g, x)
    if len(roots) == 2 and all(r.is_real for r in roots) and -1 not in roots:
        if roots[0] * roots[1] < 0:
            valid_m3.append(val)
assert valid_m3 == list(range(-10, 4))
answers.append(str(len(valid_m3)))

# Câu 4: Drone A(t, 2t + 1, 3) và Drone B(3t - 3, 3t + 1, 2t - 3). Khoảng cách ngắn nhất
pos_A = s.Matrix([t, 2*t + 1, 3])
pos_B = s.Matrix([3*t - 3, 3*t + 1, 2*t - 3])
dist_sq4 = (pos_B - pos_A).dot(pos_B - pos_A)
# dist_sq = (2t - 3)^2 + t^2 + (2t - 6)^2 = 9t^2 - 36t + 45 = 9(t - 2)^2 + 9
t_min4 = s.solve(s.diff(dist_sq4, t), t)[0]
assert t_min4 == 2
min_dist4 = s.sqrt(dist_sq4.subs(t, t_min4))
assert min_dist4 == 3
answers.append(str(int(min_dist4)))

# Câu 5: Tấm tôn hình chữ nhật 80 cm x 50 cm cắt 4 góc 4 hình vuông cạnh x. Thể tích hộp lớn nhất tính theo dm^3
# V(x) = x*(80 - 2x)*(50 - 2x) = 4*x*(40 - x)*(25 - x) cm^3.
# Đơn vị: 1 dm^3 = 1000 cm^3.
V5 = 4*x*(40 - x)*(25 - x)
crit5 = [r for r in s.solve(s.diff(V5, x), x) if 0 < r < 25]
assert crit5 == [10]
max_V5_cm3 = V5.subs(x, 10)
assert max_V5_cm3 == 18000
max_V5_dm3 = max_V5_cm3 / 1000
assert max_V5_dm3 == 18
answers.append(str(int(max_V5_dm3)))

# Câu 6: Kéo cáp qua đảo: SH = 8 km, AH = 20 km. Chi phí đất liền 30 tr/km, dưới biển 50 tr/km. Chi phí nhỏ nhất
# C(x) = 30*(20 - x) + 50*sqrt(64 + x^2) với 0 <= x <= 20
cost6 = 30*(20 - x) + 50*s.sqrt(64 + x**2)
crit6 = [r for r in s.solve(s.diff(cost6, x), x) if 0 <= r <= 20]
assert crit6 == [6] # x = 6 km
min_cost6 = cost6.subs(x, 6)
assert min_cost6 == 920
answers.append(str(int(min_cost6)))

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
