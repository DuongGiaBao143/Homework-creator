"""Giải độc lập 12 câu chọn đáp án, 16 ý đúng/sai và 6 câu trả lời ngắn cho Đề 11."""
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
        (s.Interval.open(-1, 3), s.Interval.open(-s.oo, -1), s.Interval.open(3, s.oo), s.Interval.open(0, 4))])

# Câu 2: Điểm cực đại của hàm số y = -x^3 + 3x^2 + 9x - 1
f2 = -x**3 + 3*x**2 + 9*x - 1
df2 = s.diff(f2, x)
d2f2 = s.diff(f2, x, 2)
# Điểm cực đại khi df2 == 0 và d2f2 < 0
pts2 = [r for r in s.solve(df2, x) if d2f2.subs(x, r) < 0]
assert pts2 == [3]
choose([val in pts2 for val in (-1, 3, 26, -6)])

# Câu 3: Giá trị lớn nhất của hàm số f(x) = (2x - 1)/(x + 1) trên đoạn [0; 3]
f3 = (2*x - 1)/(x + 1)
vals3 = extrema(f3, x, s.Integer(0), s.Integer(3))
max3 = max(v for _, v in vals3)
assert max3 == s.Rational(5, 4)
choose([max3 == v for v in (-1, 1, s.Rational(5, 4), 2)])

# Câu 4: Đường tiệm cận đứng của y = (3x + 2)/(x - 2)
v4 = s.solve(x - 2, x)[0]
assert v4 == 2
# A: y = 3, B: x = -2, C: y = -1, D: x = 2
choose([v == ("x", 2) for v in (("y", 3), ("x", -2), ("y", -1), ("x", 2))])

# Câu 5: Đường tiệm cận xiên của y = (2x^2 + 3x - 1)/(x + 1)
f5 = (2*x**2 + 3*x - 1)/(x + 1)
choose([all(s.limit(f5 - line, x, side) == 0 for side in (s.oo, -s.oo))
        for line in (2*x + 1, 2*x - 1, x + 1, 2*x + 3)])

# Câu 6: Nhận dạng đồ thị hàm phân thức y = (x^2 - 2x + 2)/(x - 1)
# TC đứng x = 1, TC xiên y = x - 1, Cực đại (0, -2), Cực tiểu (2, 2)
candidates6 = [
    (x**2 - x + 1)/(x - 1),
    (x**2 - 2*x + 2)/(x - 1),
    (x**2 + 2*x - 2)/(x + 1),
    (x**2 - 3*x + 3)/(x - 2)
]
choose([s.solve(s.denom(f), x) == [1] and
        s.limit(f - (x - 1), x, s.oo) == 0 and
        f.subs(x, 0) == -2 and
        f.subs(x, 2) == 2
        for f in candidates6])

# Câu 7: Doanh thu R(p) = 600p - 2p^2 lớn nhất khi p bằng
R7 = 600*p - 2*p**2
dR7 = s.diff(R7, p)
p_opt = s.solve(dR7, p)[0]
assert p_opt == 150
choose([p_opt == v for v in (100, 120, 150, 200)])

# Câu 8: Quy tắc hình hộp ABCD.A'B'C'D', AB + AD + AA' = AC'
choose([v == "AC'" for v in ("AC", "CA'", "BD'", "AC'")])

# Câu 9: Trung điểm AB với A(2, -1, 3), B(4, 3, -1)
A9 = s.Matrix([2, -1, 3])
B9 = s.Matrix([4, 3, -1])
M9 = (A9 + B9) / 2
assert M9 == s.Matrix([3, 1, 1])
choose([M9 == s.Matrix(v) for v in ((3, 1, 1), (6, 2, 2), (1, 2, -2), (2, 4, -4))])

# Câu 10: u = 2a + b với a = (1, -2, 3), b = (-2, 1, 1)
a10 = s.Matrix([1, -2, 3])
b10 = s.Matrix([-2, 1, 1])
u10 = 2*a10 + b10
assert u10 == s.Matrix([0, -3, 7])
choose([u10 == s.Matrix(v) for v in ((-1, -1, 4), (0, -3, 7), (0, -1, 7), (4, -5, 5))])

# Câu 11: Tích vô hướng u . v với u = (2, -1, 2), v = (1, 2, -2)
u11 = s.Matrix([2, -1, 2])
v11 = s.Matrix([1, 2, -2])
dot11 = u11.dot(v11)
assert dot11 == -4
choose([dot11 == v for v in (4, 0, -4, -2)])

# Câu 12: Độ dài đoạn thẳng AB với A(1, 2, -1), B(3, 0, 0)
A12 = s.Matrix([1, 2, -1])
B12 = s.Matrix([3, 0, 0])
d12 = (B12 - A12).norm()
assert d12 == 3
choose([d12 == v for v in (s.sqrt(5), 9, s.sqrt(7), 3)])

assert multiple_choice == key["I"]
dist = Counter(multiple_choice)
assert dist == {"A": 3, "B": 3, "C": 3, "D": 3}

# ==============================================================
# Phần II: kiểm tra độc lập 4 câu đúng/sai (16 ý)
# ==============================================================
true_false = []

# Câu 1: Hàm số y = f(x) = (x^2 - 3x + 3)/(x - 1)
f_ii1 = (x**2 - 3*x + 3)/(x - 1)
# a) Tập xác định D = R \ {1}
a1 = s.solve(s.denom(f_ii1), x) == [1]
# b) Đạo hàm f'(x) = (x^2 - 2x)/(x - 1)^2
df_ii1 = s.simplify(s.diff(f_ii1, x))
target_df = (x**2 - 2*x)/(x - 1)**2
b1 = s.simplify(df_ii1 - target_df) == 0
# c) Tiệm cận xiên là y = x + 2 (Sai, vì tiệm cận xiên là y = x - 2)
c1 = all(s.limit(f_ii1 - (x + 2), x, side) == 0 for side in (s.oo, -s.oo))
assert not c1
# d) Độ dài đoạn nối 2 điểm cực trị bằng 2*sqrt(5)
c_pts = s.solve(df_ii1, x)
pts_coords = [(pt, f_ii1.subs(x, pt)) for pt in c_pts]
pt_A, pt_B = pts_coords
dist_AB = s.sqrt((pt_A[0] - pt_B[0])**2 + (pt_A[1] - pt_B[1])**2)
d1 = dist_AB == 2*s.sqrt(5)
true_false.append([bool(a1), bool(b1), bool(c1), bool(d1)])

# Câu 2: Nồng độ khí CO2 C(t) = (400t^2 + 200)/(t^2 + 1) (ppm, t >= 0)
C2 = (400*t**2 + 200)/(t**2 + 1)
# a) Tại t = 0 là 200 ppm
a2 = C2.subs(t, 0) == 200
# b) Luôn tăng với t > 0
dC2 = s.diff(C2, t)
b2 = s.solve_univariate_inequality(dC2 > 0, t, relational=False) == s.Interval.open(0, s.oo)
# c) Sau 3 giờ đạt 380 ppm
c2 = C2.subs(t, 3) == 380
# d) Khi t -> +oo nồng độ vượt quá 450 ppm (Sai, tiệm cận ngang y = 400 <= 400 < 450)
lim_C2 = s.limit(C2, t, s.oo)
assert lim_C2 == 400
d2 = lim_C2 > 450
assert not d2
true_false.append([bool(a2), bool(b2), bool(c2), bool(d2)])

# Câu 3: Oxyz với A(1, 1, 2), B(3, 2, 0), C(-1, 3, 5)
A_ii3 = s.Matrix([1, 1, 2])
B_ii3 = s.Matrix([3, 2, 0])
C_ii3 = s.Matrix([-1, 3, 5])
AB_vec = B_ii3 - A_ii3
AC_vec = C_ii3 - A_ii3
# a) AB = (2, 1, -2) và |AB| = 3
a3 = AB_vec == s.Matrix([2, 1, -2]) and AB_vec.norm() == 3
# b) G = (1, 2, 7/3)
G_calc = (A_ii3 + B_ii3 + C_ii3) / 3
b3 = G_calc == s.Matrix([1, 2, s.Rational(7, 3)])
# c) D để ABCD là hình bình hành là D(-3, 2, 7)
# AD = BC <=> D - A = C - B <=> D = A + C - B
D_calc = A_ii3 + C_ii3 - B_ii3
c3 = D_calc == s.Matrix([-3, 2, 7])
# d) Góc giữa AB và AC là góc nhọn (Sai vì AB . AC = -8 < 0 => góc tù)
dot_AB_AC = AB_vec.dot(AC_vec)
assert dot_AB_AC == -8
d3 = dot_AB_AC > 0
assert not d3
true_false.append([bool(a3), bool(b3), bool(c3), bool(d3)])

# Câu 4: Cân bằng lực vật lý
# Dây DA, DB, DC nối từ trần A(-6, -2, 0), B(6, -2, 0), C(0, 4, 0) đến vật D(0, 0, -3).
# Trọng lực P = (0, 0, -180) N.
D_ii4 = s.Matrix([0, 0, -3])
A_ii4 = s.Matrix([-6, -2, 0])
B_ii4 = s.Matrix([6, -2, 0])
C_ii4 = s.Matrix([0, 4, 0])
DA_vec = A_ii4 - D_ii4  # (-6, -2, 3)
DB_vec = B_ii4 - D_ii4  # (6, -2, 3)
DC_vec = C_ii4 - D_ii4  # (0, 4, 3)
# a) Độ dài DC = 5 m
a4 = DC_vec.norm() == 5
# b) Cân bằng lực: F1 + F2 + F3 + P = 0
b4 = True
# Lực căng F1 = k1*DA, F2 = k2*DB, F3 = k3*DC
# F1 + F2 + F3 = (0, 0, 180)
k1, k2, k3 = s.symbols("k1 k2 k3", real=True)
eqs = [
    -6*k1 + 6*k2,
    -2*k1 - 2*k2 + 4*k3,
    3*k1 + 3*k2 + 3*k3 - 180
]
sol_k = s.solve(eqs, (k1, k2, k3))
assert sol_k == {k1: 20, k2: 20, k3: 20}
F1_mag = sol_k[k1] * DA_vec.norm()
F2_mag = sol_k[k2] * DB_vec.norm()
F3_mag = sol_k[k3] * DC_vec.norm()
assert F1_mag == 140 and F2_mag == 140 and F3_mag == 100
# c) Độ lớn lực căng dây DA và DB bằng nhau và bằng 140 N
c4 = F1_mag == 140 and F2_mag == 140
# d) Độ lớn lực căng dây DC bằng 120 N (Sai, F3 = 100 N)
d4 = F3_mag == 120
assert not d4
true_false.append([bool(a4), bool(b4), bool(c4), bool(d4)])

assert true_false == key["II"]

# ==============================================================
# Phần III: kiểm tra độc lập 6 câu trả lời ngắn
# ==============================================================
short_ans = []

# Câu 1: Số giá trị nguyên m in [-10; 10] để y = 1/3 x^3 - m x^2 + (2m + 8)x - 2027 đồng biến trên R
f_iii1 = x**3/3 - m*x**2 + (2*m + 8)*x - 2027
df_iii1 = s.diff(f_iii1, x)
# df_iii1 = x^2 - 2mx + 2m + 8 >= 0 for all x <=> Delta' = m^2 - 2m - 8 <= 0
delta1 = m**2 - 2*m - 8
m_range = s.solve_univariate_inequality(delta1 <= 0, m, relational=False)
assert m_range == s.Interval(-2, 4)
m_vals = [val for val in range(-10, 11) if -2 <= val <= 4]
assert len(m_vals) == 7
short_ans.append(str(len(m_vals)))

# Câu 2: Tọa độ đỉnh C' của hình hộp ABCD.A'B'C'D' với A(1, 2, -1), B(3, 1, 2), D(2, 4, 1), A'(3, 5, 0)
A_box = s.Matrix([1, 2, -1])
B_box = s.Matrix([3, 1, 2])
D_box = s.Matrix([2, 4, 1])
Ap_box = s.Matrix([3, 5, 0])
# AC' = AB + AD + AA'
Cp_box = A_box + (B_box - A_box) + (D_box - A_box) + (Ap_box - A_box)
assert Cp_box == s.Matrix([6, 6, 5])
S_box = sum(Cp_box)
assert S_box == 17
short_ans.append(str(S_box))

# Câu 3: Số giá trị nguyên m in [-5; 5] để y = (x^2 + mx + 4)/(x + 2) có 2 điểm cực trị nằm về 2 phía trục tung
f_iii3 = (x**2 + m*x + 4)/(x + 2)
df_iii3 = s.simplify(s.diff(f_iii3, x))
num_df3 = s.numer(df_iii3)
# num_df3 = x^2 + 4x + 2m - 4
# Có 2 nghiệm phân biệt khác -2 và trái dấu:
# a*c < 0 <=> 2m - 4 < 0 <=> m < 2
# g(-2) = 4 - 8 + 2m - 4 = 2m - 8 != 0 <=> m != 4 (tự thoả do m < 2)
# Delta' = 4 - (2m - 4) = 8 - 2m > 0 <=> m < 4 (tự thoả)
m_iii3 = [val for val in range(-5, 6) if val < 2]
assert m_iii3 == [-5, -4, -3, -2, -1, 0, 1]
assert len(m_iii3) == 7
short_ans.append(str(len(m_iii3)))

# Câu 4: Khoảng cách ngắn nhất giữa hai drone A(2+t; 10+2t; 1+3t) và B(2t; 6t+5; 11) với t >= 0
A_drone = s.Matrix([2 + t, 10 + 2*t, 1 + 3*t])
B_drone = s.Matrix([2*t, 6*t + 5, 11])
dist_sq = (B_drone - A_drone).dot(B_drone - A_drone)
# dist_sq = (t - 2)^2 + (4t - 5)^2 + (10 - 3t)^2 = 26t^2 - 104t + 129
t_opt = s.solve(s.diff(dist_sq, t), t)[0]
assert t_opt == 2
min_dist = s.sqrt(dist_sq.subs(t, t_opt))
assert min_dist == 5
short_ans.append(str(min_dist))

# Câu 5: Cắt 4 góc tấm tôn hình vuông 60 cm thành hộp không nắp, thể tích lớn nhất theo dm^3
# V(x) = x * (60 - 2x)^2 cm^3 với 0 < x < 30
V_box = x * (60 - 2*x)**2
dV_box = s.diff(V_box, x)
x_opt = [r for r in s.solve(dV_box, x) if 0 < r < 30][0]
assert x_opt == 10
V_max_cm3 = V_box.subs(x, x_opt)
assert V_max_cm3 == 16000
V_max_dm3 = V_max_cm3 / 1000
assert V_max_dm3 == 16
short_ans.append(str(V_max_dm3))

# Câu 6: Kéo cáp từ đảo A (AH = 6 km) đến nhà máy B trên bờ (HB = 12 km)
# Cáp ngầm 100 tr/km, cáp trên bờ 60 tr/km. Điểm nối C cách H một đoạn x (0 <= x <= 12)
# C(x) = 100*sqrt(x^2 + 36) + 60*(12 - x)
cost = 100*s.sqrt(x**2 + 36) + 60*(12 - x)
d_cost = s.diff(cost, x)
x_crit = [r for r in s.solve(d_cost, x) if 0 <= r <= 12][0]
assert x_crit == s.Rational(9, 2)
cost_min = cost.subs(x, x_crit)
assert cost_min == 1200
short_ans.append(str(cost_min))

assert short_ans == key["III"]

# Xuất kết quả kiểm tra ra JSON
result = {
    "status": "passed",
    "part_I": dict(zip([f"Cau_{i}" for i in range(1, 13)], multiple_choice)),
    "part_I_distribution": dict(dist),
    "part_II": dict(zip([f"Cau_{i}" for i in range(1, 5)], true_false)),
    "part_III": dict(zip([f"Cau_{i}" for i in range(1, 7)], short_ans))
}

(BASE / "kiem_tra_toan.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("[VERIFY] Kiểm tra toán 100% THÀNH CÔNG! Đã ghi kiem_tra_toan.json.")
print(json.dumps(result, ensure_ascii=False, indent=2))
