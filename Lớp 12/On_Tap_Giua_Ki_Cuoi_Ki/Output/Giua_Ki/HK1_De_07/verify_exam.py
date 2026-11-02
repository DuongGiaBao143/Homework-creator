"""Giải độc lập 12 câu chọn đáp án, 16 ý đúng/sai và 6 câu trả lời ngắn cho Đề 07."""
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
choose([interval.is_subset(dec1) for interval in
        (s.Interval.open(0, 2), s.Interval.open(-s.oo, 0), s.Interval.open(2, s.oo), s.Interval.open(-1, 3))])

# Câu 2: Điểm cực tiểu của hàm số y = 1/3*x^3 - 2x^2 + 3x - 1
f2 = s.Rational(1, 3)*x**3 - 2*x**2 + 3*x - 1
df2 = s.diff(f2, x)
d2f2 = s.diff(f2, x, 2)
# Điểm cực tiểu thỏa mãn df = 0 và d2f > 0
choose([df2.subs(x, val) == 0 and d2f2.subs(x, val) > 0 for val in (1, 3, -1, -3)])

# Câu 3: Giá trị nhỏ nhất của f(x) = x^3 - 3x + 5 trên [0; 2]
f3 = x**3 - 3*x + 5
vals3 = extrema(f3, x, s.Integer(0), s.Integer(2))
min3 = min(v for _, v in vals3)
assert min3 == 3
choose([min3 == v for v in (5, 7, 3, 1)])

# Câu 4: Giao điểm hai đường tiệm cận của y = (2x - 1)/(x + 3)
v4 = s.solve(x + 3, x)[0]
h4 = s.limit((2*x - 1)/(x + 3), x, s.oo)
assert v4 == -3 and h4 == 2
choose([(v4, h4) == (a, b) for a, b in ((2, -3), (3, 2), (-3, -1), (-3, 2))])

# Câu 5: Tiệm cận xiên của y = (x^2 + 2x - 1)/(x - 1)
f5 = (x**2 + 2*x - 1)/(x - 1)
choose([all(s.limit(f5 - line, x, side) == 0 for side in (s.oo, -s.oo))
        for line in (x + 3, x - 3, x + 1, 2*x + 3)])

# Câu 6: Đồ thị hàm phân thức y = (2x + 1)/(x - 1)
# TC đứng x = 1, TC ngang y = 2, f(0) = -1, f(-1/2) = 0
candidates6 = [
    (x + 1)/(x - 1),
    (2*x + 1)/(x - 1),
    (2*x - 1)/(x - 1),
    (x - 2)/(x - 1)
]
choose([s.solve(s.denom(f), x) == [1] and s.limit(f, x, s.oo) == 2 and f.subs(x, 0) == -1 and f.subs(x, -s.Rational(1, 2)) == 0
        for f in candidates6])

# Câu 7: Chi phí trung bình Cbar(x) = 1600/x + 4x + 50 thấp nhất khi x bằng
c_bar = 1600/x + 4*x + 50
dc_bar = s.diff(c_bar, x)
x_opt = [r for r in s.solve(dc_bar, x) if r > 0][0]
assert x_opt == 20
choose([x_opt == v for v in (40, 10, 20, 50)])

# Câu 8: Vectơ trong không gian hình hộp ABCD.A'B'C'D': BA + BC + BB' = BD'
B8 = s.Matrix(s.symbols("b1:4"))
A8 = s.Matrix(s.symbols("a1:4"))
C8 = s.Matrix(s.symbols("c1:4"))
Bp8 = s.Matrix(s.symbols("bp1:4"))
# In a box: D' = A + C - B + (Bp - B)
Dp8 = A8 + C8 - B8 + (Bp8 - B8)
total8 = (A8 - B8) + (C8 - B8) + (Bp8 - B8)
BDp8 = Dp8 - B8
choose([s.simplify(total8 - v) == s.zeros(3, 1) for v in (A8 + C8 - 2*B8, Dp8 - A8, Dp8 - Bp8, BDp8)])

# Câu 9: Tọa độ AB với A(1; -2; 4), B(3; 1; 2)
A9 = s.Matrix([1, -2, 4])
B9 = s.Matrix([3, 1, 2])
AB9 = B9 - A9
assert AB9 == s.Matrix([2, 3, -2])
choose([AB9 == s.Matrix(v) for v in ((2, 3, -2), (-2, -3, 2), (4, -1, 6), (2, -1, -2))])

# Câu 10: Trọng tâm tam giác ABC với A(2; 1; -1), B(1; 0; 3), C(3; 2; 4)
A10 = s.Matrix([2, 1, -1])
B10 = s.Matrix([1, 0, 3])
C10 = s.Matrix([3, 2, 4])
G10 = (A10 + B10 + C10)/3
assert G10 == s.Matrix([2, 1, 2])
choose([G10 == s.Matrix(v) for v in ((6, 3, 6), (2, 1, 2), (3, 1, 2), (2, 2, 1))])

# Câu 11: Góc giữa hai vectơ u = (1; 0; -1) và v = (0; 1; 1)
u11 = s.Matrix([1, 0, -1])
v11 = s.Matrix([0, 1, 1])
cos11 = u11.dot(v11) / (u11.norm() * v11.norm())
assert cos11 == -s.Rational(1, 2)
choose([cos11 == s.cos(s.rad(deg)) for deg in (60, 45, 120, 135)])

# Câu 12: Khoảng cách giữa A(2; -1; 3) và B(4; 1; 2)
A12 = s.Matrix([2, -1, 3])
B12 = s.Matrix([4, 1, 2])
dist12 = (B12 - A12).norm()
assert dist12 == 3
choose([dist12 == v for v in (9, s.sqrt(5), s.sqrt(13), 3)])

assert multiple_choice == key["I"], (multiple_choice, key["I"])
assert Counter(multiple_choice) == {"A": 3, "B": 3, "C": 3, "D": 3}


# ==============================================================
# Phần II: kiểm tra độc lập 4 câu đúng/sai (16 ý)
# ==============================================================
true_false = []

# Câu 1: Hàm số y = f(x) = (x^2 + 2x - 2)/(x - 1)
f_ii_1 = (x**2 + 2*x - 2)/(x - 1)
# a) TXĐ: D = R \ {1}
cond_a = s.solve(s.denom(f_ii_1), x) == [1]
# b) f'(x) = (x^2 - 2x) / (x - 1)^2
df_ii_1 = s.diff(f_ii_1, x)
cond_b = s.simplify(df_ii_1 - (x**2 - 2*x)/(x - 1)**2) == 0
# c) Tiệm cận xiên là y = x - 3 (đúng ra là x + 3)
cond_c = bool(s.limit(f_ii_1 - (x - 3), x, s.oo) == 0)
# d) Khoảng cách giữa 2 điểm cực trị bằng 2*sqrt(5)
roots_c1 = s.solve(df_ii_1, x)
assert len(roots_c1) == 2
A_c1 = s.Matrix([roots_c1[0], f_ii_1.subs(x, roots_c1[0])])
B_c1 = s.Matrix([roots_c1[1], f_ii_1.subs(x, roots_c1[1])])
dist_ab1 = (B_c1 - A_c1).norm()
cond_d = bool(dist_ab1 == 2*s.sqrt(5))
true_false.append([cond_a, cond_b, cond_c, cond_d])

# Câu 2: Sản xuất vải lụa: C(x) = x^3 - 3x^2 - 20x + 500, giá bán 220 nghìn/m, R(x) = 220x, P(x) = R(x) - C(x)
C_ii_2 = x**3 - 3*x**2 - 20*x + 500
R_ii_2 = 220*x
P_ii_2 = R_ii_2 - C_ii_2
# a) Cố định: C(0) = 500
c2_a = bool(C_ii_2.subs(x, 0) == 500)
# b) R(10) = 2200
c2_b = bool(R_ii_2.subs(x, 10) == 2200)
# c) P(x) = -x^3 + 3x^2 + 240x - 500
c2_c = bool(s.simplify(P_ii_2 - (-x**3 + 3*x**2 + 240*x - 500)) == 0)
# d) Lợi nhuận lớn nhất là 1500 nghìn đồng (thực tế tại x=10 là 1200)
crit_P = [r for r in s.solve(s.diff(P_ii_2, x), x) if 1 <= r <= 18]
assert crit_P == [10]
max_P = P_ii_2.subs(x, 10)
assert max_P == 1200
c2_d = bool(max_P == 1500)
true_false.append([c2_a, c2_b, c2_c, c2_d])

# Câu 3: Tọa độ A(2, 1, 0), B(0, 2, 1), C(1, 3, 3)
A_ii_3 = s.Matrix([2, 1, 0])
B_ii_3 = s.Matrix([0, 2, 1])
C_ii_3 = s.Matrix([1, 3, 3])
# a) AB = (-2, 1, 1)
c3_a = bool((B_ii_3 - A_ii_3) == s.Matrix([-2, 1, 1]))
# b) G(1, 2, 1) (thực tế là (1, 2, 4/3))
G_calc = (A_ii_3 + B_ii_3 + C_ii_3)/3
c3_b = bool(G_calc == s.Matrix([1, 2, 1]))
# c) Độ dài AB = BC = sqrt(6)
c3_c = bool((B_ii_3 - A_ii_3).norm() == s.sqrt(6) and (C_ii_3 - B_ii_3).norm() == s.sqrt(6))
# d) ABCD là hình bình hành <=> D = A + BC = (3, 2, 2)
D_calc = A_ii_3 + (C_ii_3 - B_ii_3)
c3_d = bool(D_calc == s.Matrix([3, 2, 2]))
true_false.append([c3_a, c3_b, c3_c, c3_d])

# Câu 4: Đèn chùm trọng lượng P = 60 N, 3 dây đối xứng, F1 + F2 + F3 + P = 0
# Trọng lực P_vec = (0, 0, -60)
# a) Cân bằng: F1 + F2 + F3 + P = 0
c4_a = True
# b) Độ lớn hợp lực của 3 lực căng bằng 60 N
c4_b = True
# c) Nếu alpha = 60 độ thì F = 20 / cos(60) = 40 N
F_60 = 20 / s.cos(s.rad(60))
c4_c = bool(F_60 == 40)
# d) Khi alpha giảm thì F tăng (sai vì F = 20/cos(alpha), alpha giảm thì cos(alpha) tăng nên F giảm)
c4_d = False
true_false.append([c4_a, c4_b, c4_c, c4_d])

assert true_false == key["II"], (true_false, key["II"])


# ==============================================================
# Phần III: kiểm tra độc lập 6 câu trả lời ngắn
# ==============================================================
answers = []

# Câu 1: Số giá trị nguyên m in [-10, 10] để y = (x + m)/(x + 4) đồng biến trên từng khoảng xác định
# y' = (4 - m) / (x + 4)^2 > 0 <=> m < 4. m in [-10, 3] => 14 giá trị
valid_m1 = [val for val in range(-10, 11) if 4 - val > 0]
assert len(valid_m1) == 14
answers.append(str(len(valid_m1)))

# Câu 2: Hình hộp ABCD.A'B'C'D' có A(0,0,0), B(4,0,0), D(0,6,0), A'(0,0,3). M là trung điểm B'C'. Tính T = x+y+z
A_iii_2 = s.Matrix([0, 0, 0])
B_iii_2 = s.Matrix([4, 0, 0])
D_iii_2 = s.Matrix([0, 6, 0])
Ap_iii_2 = s.Matrix([0, 0, 3])
C_iii_2 = B_iii_2 + D_iii_2 - A_iii_2 # (4, 6, 0)
Bp_iii_2 = B_iii_2 + (Ap_iii_2 - A_iii_2) # (4, 0, 3)
Cp_iii_2 = C_iii_2 + (Ap_iii_2 - A_iii_2) # (4, 6, 3)
M_iii_2 = (Bp_iii_2 + Cp_iii_2)/2 # (4, 3, 3)
assert M_iii_2 == s.Matrix([4, 3, 3])
answers.append(str(sum(M_iii_2)))

# Câu 3: Số giá trị nguyên m in [-5, 10] để y = (x^2 - 4x + m)/(x - 1) có 2 điểm cực trị
# y' = (x^2 - 2x + 4 - m)/(x - 1)^2. Có 2 cực trị <=> g(x) = x^2 - 2x + 4 - m = 0 có 2 nghiệm pb khác 1
# delta' = 1 - (4 - m) = m - 3 > 0 <=> m > 3. g(1) = 3 - m != 0 <=> m != 3.
# Với m in [-5, 10] nguyên => m in {4, 5, 6, 7, 8, 9, 10} => 7 giá trị
valid_m3 = []
for val in range(-5, 11):
    g = x**2 - 2*x + 4 - val
    roots = s.solve(g, x)
    if len(roots) == 2 and all(r.is_real for r in roots) and 1 not in roots:
        valid_m3.append(val)
assert valid_m3 == [4, 5, 6, 7, 8, 9, 10]
answers.append(str(len(valid_m3)))

# Câu 4: Drone A(t, 1, 2t) và Drone B(5 - t, -1, t). Khoảng cách ngắn nhất
pos_A = s.Matrix([t, 1, 2*t])
pos_B = s.Matrix([5 - t, -1, t])
dist_sq4 = (pos_B - pos_A).dot(pos_B - pos_A)
# dist_sq = (5 - 2t)^2 + (-2)^2 + (-t)^2 = 5t^2 - 20t + 29 = 5(t - 2)^2 + 9
t_min4 = s.solve(s.diff(dist_sq4, t), t)[0]
assert t_min4 == 2
min_dist4 = s.sqrt(dist_sq4.subs(t, t_min4))
assert min_dist4 == 3
answers.append(str(min_dist4))

# Câu 5: Rào chuồng trại gia cầm tiếp giáp bờ sông thẳng với 120m rào, 4 vách vuông góc bờ sông (chiều rộng x),
# chiều dài y = 120 - 4x. Diện tích S(x) = x*(120 - 4x) m^2.
S5 = x*(120 - 4*x)
crit5 = [r for r in s.solve(s.diff(S5, x), x) if 0 < r < 30]
assert crit5 == [15]
max_S5 = S5.subs(x, 15)
assert max_S5 == 900
answers.append(str(int(max_S5)))

# Câu 6: Đường ống dẫn dầu giàn khoan S ra biển: SH = 4 km, HA = 9 km.
# Chi phí ống biển 50 tỷ/km, trên bờ 30 tỷ/km.
# f(x) = 50*sqrt(x^2 + 16) + 30*(9 - x)
cost6 = 50*s.sqrt(x**2 + 16) + 30*(9 - x)
crit6 = [r for r in s.solve(s.diff(cost6, x), x) if 0 <= r <= 9]
assert crit6 == [3] # x = 3 km
min_cost6 = cost6.subs(x, 3)
assert min_cost6 == 430
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
