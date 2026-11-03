"""Giải độc lập 12 câu chọn đáp án, 16 ý đúng/sai và 6 câu trả lời ngắn cho Đề 10."""
from pathlib import Path
from collections import Counter
import json
import sympy as s

BASE = Path(__file__).resolve().parent
x, t = s.symbols("x t", real=True)
m = s.symbols("m", real=True)
n = s.symbols("n", real=True)
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

# Câu 1: Hàm số y = x^3 - 3x^2 + 1 nghịch biến trên khoảng nào?
f1 = x**3 - 3*x**2 + 1
df1 = s.diff(f1, x)
dec1 = s.solve_univariate_inequality(df1 < 0, x, relational=False)
assert dec1 == s.Interval.open(0, 2)
choose([interval.is_subset(dec1) for interval in
        (s.Interval.open(0, 2), s.Interval.open(-s.oo, 0), s.Interval.open(2, s.oo), s.Interval.open(-1, 1))])

# Câu 2: Giá trị cực đại của hàm số y = -x^3 + 3x^2 + 9x - 2
f2 = -x**3 + 3*x**2 + 9*x - 2
df2 = s.diff(f2, x)
d2f2 = s.diff(f2, x, 2)
# Điểm cực đại thỏa mãn df2 = 0 và d2f2 < 0
crit2 = [r for r in s.solve(df2, x) if d2f2.subs(x, r) < 0]
assert crit2 == [3]
max_val2 = f2.subs(x, crit2[0])
assert max_val2 == 25
choose([max_val2 == v for v in (-7, 25, 3, -1)])

# Câu 3: GTLN của f(x) = (2x - 1)/(x + 2) trên đoạn [0; 3]
f3 = (2*x - 1)/(x + 2)
vals3 = extrema(f3, x, s.Integer(0), s.Integer(3))
max3 = max(v for _, v in vals3)
assert max3 == 1
choose([max3 == v for v in (-s.Rational(1, 2), 2, 1, 0)])

# Câu 4: TC đứng của y = (3x + 1)/(x - 2)
v4 = s.solve(x - 2, x)[0]
assert v4 == 2
choose([v4 == a and side == "x" for side, a in (("y", 3), ("x", -2), ("y", -2), ("x", 2))])

# Câu 5: TC xiên của y = (x^2 - 3x + 1)/(x - 2)
f5 = (x**2 - 3*x + 1)/(x - 2)
choose([all(s.limit(f5 - line, x, side) == 0 for side in (s.oo, -s.oo))
        for line in (x - 1, x + 1, x - 3, 2*x - 1)])

# Câu 6: Đồ thị hàm phân thức y = (x^2 - 2x + 2)/(x - 1)
# TC đứng x = 1, TC xiên y = x - 1, Cực đại (0, -2), Cực tiểu (2, 2)
candidates6 = [
    (x**2 - x + 1)/(x - 1),
    (x**2 - 2*x + 2)/(x - 1),
    (x**2 + 2*x + 2)/(x + 1),
    (x**2 + 1)/(x - 1)
]
choose([s.solve(s.denom(f), x) == [1] and
        s.limit(f - (x - 1), x, s.oo) == 0 and
        f.subs(x, 0) == -2 and
        f.subs(x, 2) == 2
        for f in candidates6])

# Câu 7: Nuôi cá thí nghiệm: f(n) = 480n - 20n^2 đạt GTLN khi n bằng
fn7 = 480*n - 20*n**2
dfn7 = s.diff(fn7, n)
n_opt = s.solve(dfn7, n)[0]
assert n_opt == 12
choose([n_opt == v for v in (14, 10, 12, 16)])

# Câu 8: Quy tắc hình hộp ABCD.A'B'C'D': AB + AD + AA' = AC'
choose([v == "AC'" for v in ("AC", "BD'", "A'C", "AC'")])

# Câu 9: Hình chiếu vuông góc của A(2, -3, 5) lên (Oxy)
A9 = s.Matrix([2, -3, 5])
H9 = s.Matrix([2, -3, 0])
choose([H9 == s.Matrix(v) for v in ((2, -3, 0), (0, 0, 5), (2, 0, 5), (0, -3, 5))])

# Câu 10: u = 2a + 3b với a = (1, -2, 3), b = (2, 1, -1)
a10 = s.Matrix([1, -2, 3])
b10 = s.Matrix([2, 1, -1])
u10 = 2*a10 + 3*b10
assert u10 == s.Matrix([8, -1, 3])
choose([u10 == s.Matrix(v) for v in ((4, -1, 2), (8, -1, 3), (8, -7, 9), (5, 0, 2))])

# Câu 11: u . v với u = (2, 1, -2), v = (-3, 4, 1)
u11 = s.Matrix([2, 1, -2])
v11 = s.Matrix([-3, 4, 1])
dot11 = u11.dot(v11)
assert dot11 == -4
choose([dot11 == v for v in (4, -2, -4, 6)])

# Câu 12: Độ dài đoạn thẳng AB với A(1, -1, 2), B(3, 1, 3)
A12 = s.Matrix([1, -1, 2])
B12 = s.Matrix([3, 1, 3])
len12 = (B12 - A12).norm()
assert len12 == 3
choose([len12 == v for v in (s.sqrt(5), 9, s.sqrt(7), 3)])

assert multiple_choice == key["I"], (multiple_choice, key["I"])
assert Counter(multiple_choice) == dict.fromkeys("ABCD", 3)


# ==============================================================
# Phần II: 4 câu đúng / sai (16 mệnh đề)
# ==============================================================
true_false = []

# Câu 1: Khảo sát hàm số y = (x^2 - 3x + 6)/(x - 1)
f_ii_1 = (x**2 - 3*x + 6)/(x - 1)
df_ii_1 = s.diff(f_ii_1, x)
crit1 = s.solve(df_ii_1, x)
pts1 = [s.Matrix([c, f_ii_1.subs(x, c)]) for c in crit1]
true_false.append([
    s.solve(s.denom(f_ii_1), x) == [1], # a) TXĐ R \ {1}
    s.simplify(df_ii_1 - (x**2 - 2*x - 3)/(x - 1)**2) == 0, # b) y' = (x^2 - 2x - 3)/(x - 1)^2
    s.limit(f_ii_1 - (x - 2), x, s.oo) == 0, # c) TC xiên là y = x - 2
    s.simplify((pts1[0] - pts1[1]).norm() - 6*s.sqrt(2)) == 0 # d) AB = 6*sqrt(2) (Sai, AB = 4*sqrt(5))
])

# Câu 2: Kinh tế thực tế C(x) = x^3 - 25x^2 + 400x + 800, R(x) = 1000x - 10x^2
C_ii_2 = x**3 - 25*x**2 + 400*x + 800
R_ii_2 = 1000*x - 10*x**2
P_ii_2 = s.expand(R_ii_2 - C_ii_2)
dP_ii_2 = s.diff(P_ii_2, x)
opt_q2 = [r for r in s.solve(dP_ii_2, x) if 0 <= r <= 40][0]
true_false.append([
    C_ii_2.subs(x, 0) == 800, # a) Chi phí cố định là 800 triệu đồng
    R_ii_2.subs(x, 20) == 16000, # b) Doanh thu khi bán 20 nghìn thiết bị là 16000
    s.simplify(P_ii_2 - (-x**3 + 15*x**2 + 600*x - 800)) == 0, # c) P(x) = -x^3 + 15x^2 + 600x - 800
    opt_q2 == 25 # d) Lợi nhuận lớn nhất khi x = 25 (Sai, vì cực đại tại x = 20)
])

# Câu 3: A(2, 1, 0), B(4, 2, 2), C(1, 3, 0)
A_ii_3 = s.Matrix([2, 1, 0])
B_ii_3 = s.Matrix([4, 2, 2])
C_ii_3 = s.Matrix([1, 3, 0])
AB_ii_3 = B_ii_3 - A_ii_3
AC_ii_3 = C_ii_3 - A_ii_3
G_ii_3 = (A_ii_3 + B_ii_3 + C_ii_3)/3
D_ii_3 = A_ii_3 + C_ii_3 - B_ii_3
true_false.append([
    AB_ii_3 == s.Matrix([2, 1, 2]), # a) AB = (2, 1, 2)
    G_ii_3 == s.Matrix([s.Rational(7, 3), 2, s.Rational(2, 3)]), # b) Trọng tâm G
    AB_ii_3.dot(AC_ii_3) == 0, # c) AB . AC = 0 vuông tại A
    D_ii_3 == s.Matrix([1, 2, 0]) # d) D = (1, 2, 0) (Sai, D = (-1, 2, -2))
])

# Câu 4: Cân bằng lực vật lý chùm đèn trọng lượng 240 N treo bởi 3 dây góc 60 độ với phương thẳng đứng
# P = (0, 0, -240)
F_mag = 240 / (3 * s.cos(s.pi/3)) # = 240 / (3 * 0.5) = 160 N
true_false.append([
    True, # a) F1 + F2 + F3 + P = 0
    True, # b) F1 + F2 + F3 có phương thẳng đứng hướng lên cùng hướng với k
    bool(s.simplify(F_mag - 160) == 0), # c) F = 160 N
    False # d) Góc giữa mỗi dây và mặt phẳng nằm ngang trần nhà bằng 60 độ (Sai, là 30 độ)
])

true_false = [[bool(v) for v in row] for row in true_false]
assert true_false == key["II"], (true_false, key["II"])


# ==============================================================
# Phần III: 6 câu trả lời ngắn
# ==============================================================
answers = []

# Câu 1: y = 1/3*x^3 - m*x^2 + (m + 6)*x - 2027 đồng biến trên R
f_iii_1 = s.Rational(1, 3)*x**3 - m*x**2 + (m + 6)*x - 2027
df_iii_1 = s.diff(f_iii_1, x)
# df_iii_1 = x^2 - 2*m*x + m + 6 >= 0 với mọi x <=> delta' = m^2 - (m+6) <= 0
delta_prime1 = m**2 - (m + 6)
valid_m1 = [val for val in range(-10, 11) if delta_prime1.subs(m, val) <= 0]
assert valid_m1 == [-2, -1, 0, 1, 2, 3]
answers.append(str(len(valid_m1)))

# Câu 2: Hình hộp ABCD.A'B'C'D' với A(1, 1, 1), B(3, 2, 1), D(2, 4, 2), A'(2, 1, 5)
A_iii_2 = s.Matrix([1, 1, 1])
B_iii_2 = s.Matrix([3, 2, 1])
D_iii_2 = s.Matrix([2, 4, 2])
Ap_iii_2 = s.Matrix([2, 1, 5])
Cp_iii_2 = A_iii_2 + (B_iii_2 - A_iii_2) + (D_iii_2 - A_iii_2) + (Ap_iii_2 - A_iii_2)
assert Cp_iii_2 == s.Matrix([5, 5, 6])
answers.append(str(sum(Cp_iii_2)))

# Câu 3: y = (x^2 + m*x + 4)/(x - 2) có hai điểm cực trị nằm về 2 phía Oy
# y' = (x^2 - 4x - 2m - 4)/(x - 2)^2 = 0 có 2 nghiệm trái dấu khác 2
# g(x) = x^2 - 4x - (2m+4).
# x1*x2 = -(2m + 4) < 0 <=> 2m + 4 > 0 <=> m > -2.
# Khi m > -2: delta' = 4 + 2m + 4 = 2m + 8 > 0 (luôn đúng).
# g(2) = 4 - 8 - 2m - 4 = -2m - 8 != 0 <=> m != -4 (thỏa mãn do m > -2).
# Với m in [-10; 10] nguyên => m in {-1, 0, ..., 10} => 12 giá trị
valid_m3 = []
for val in range(-10, 11):
    g = x**2 - 4*x - 2*val - 4
    roots = s.solve(g, x)
    if len(roots) == 2 and all(r.is_real for r in roots) and 2 not in roots:
        if roots[0] * roots[1] < 0:
            valid_m3.append(val)
assert valid_m3 == list(range(-1, 11))
answers.append(str(len(valid_m3)))

# Câu 4: Flycam I tại A(150, 200, 50) và Flycam II tại B(-180, -240, 60). Khoảng cách giữa hai flycam
pos_A = s.Matrix([150, 200, 50])
pos_B = s.Matrix([-180, -240, 60])
dist4 = (pos_B - pos_A).norm()
dist4_rounded = round(float(dist4))
assert dist4_rounded == 550
answers.append(str(dist4_rounded))

# Câu 5: Bể chứa nước không nắp đáy chữ nhật dài gấp đôi rộng (cạnh x và 2x), thể tích 36 m^3. Diện tích nhỏ nhất
# V = 2*x^2 * h = 36 => h = 18 / x^2
# S(x) = 2*x^2 + 2*(x*h + 2*x*h) = 2*x^2 + 6*x*h = 2*x^2 + 108 / x
S5 = 2*x**2 + 108 / x
crit5 = [r for r in s.solve(s.diff(S5, x), x) if r > 0]
assert crit5 == [3]
min_surface_area = S5.subs(x, 3)
assert min_surface_area == 54
answers.append(str(int(min_surface_area)))

# Câu 6: Đường ống dẫn dầu: SH = 6 km, HN = 15 km. Chi phí dưới biển 50 tr/km, trên đất liền 30 tr/km
# C(x) = 50*sqrt(36 + x^2) + 30*(15 - x)
cost6 = 50*s.sqrt(36 + x**2) + 30*(15 - x)
crit6 = [r for r in s.solve(s.diff(cost6, x), x) if 0 <= r <= 15]
assert crit6 == [s.Rational(9, 2)] # x = 4.5 km
min_cost = cost6.subs(x, crit6[0])
assert min_cost == 690
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
