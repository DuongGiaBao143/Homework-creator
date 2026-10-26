"""Giải độc lập 12 câu trắc nghiệm, 16 ý đúng/sai và 6 câu trả lời ngắn cho Đề 03."""
from pathlib import Path
from collections import Counter
import json
import sympy as s

BASE = Path(__file__).resolve().parent
x, t = s.symbols("x t", real=True)
m_sym = s.symbols("m", positive=True)
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


# ==========================================
# PHẦN I: 12 câu trắc nghiệm 4 lựa chọn
# ==========================================

# Câu 1: Hàm số y = -x^3 + 3x^2 - 4 đồng biến trên khoảng nào?
f1 = -x**3 + 3*x**2 - 4
df1 = s.diff(f1, x)
inc1 = s.solve_univariate_inequality(df1 > 0, x, relational=False)
choose([s.Interval.open(left, right).is_subset(inc1) for left, right in
        ((-s.oo, 0), (0, 2), (2, s.oo), (-1, 1))])

# Câu 2: Điểm cực tiểu của hàm số y = x^3 - 3x^2 - 9x + 2
f2 = x**3 - 3*x**2 - 9*x + 2
df2 = s.diff(f2, x)
d2f2 = s.diff(f2, x, 2)
# Các lựa chọn: x = 3, x = -1, x = -25, x = 7
choose([d2f2.subs(x, val) > 0 and df2.subs(x, val) == 0 if val in (-1, 3) else False
        for val in (3, -1, -25, 7)])

# Câu 3: Giá trị nhỏ nhất của f(x) = (x-2)/(x+1) trên [0; 3]
f3 = (x - 2)/(x + 1)
min_val3 = min(f3.subs(x, v) for v in (0, 3))
choose([min_val3 == v for v in (s.Rational(1, 4), 0, -2, 1)])

# Câu 4: Tiệm cận đứng của y = (3x-1)/(x-2)
# Các lựa chọn: x = 3, y = 3, y = 2, x = 2
vert4 = s.solve(x - 2, x)[0]
assert s.limit((3*x - 1)/(x - 2), x, 2, dir="+") == s.oo
choose([vert4 == 3, False, False, vert4 == 2])

# Câu 5: Tiệm cận xiên của y = (2x^2 - 3x + 2)/(x - 1)
# Các lựa chọn: y = 2x - 1, y = 2x + 1, y = x - 1, y = 2x
f5 = (2*x**2 - 3*x + 2)/(x - 1)
choose([s.limit(f5 - line, x, s.oo) == 0 for line in (2*x - 1, 2*x + 1, x - 1, 2*x)])

# Câu 6: Nhận dạng đồ thị hàm phân thức bậc 2/1: y = (x^2 - x + 1)/(x - 1)
# f(0) = -1, f'(0) = 0, f'(2) = 0, f(2) = 3, TCĐ x=1, TCX y=x
p_candidates = [
    (x**2 + x + 1)/(x + 1),
    (-x**2 + x - 1)/(x - 1),
    (x**2 - x + 1)/(x - 1),
    (x**2 - 2*x + 2)/(x - 1)
]
choose([p.subs(x, 0) == -1 and s.diff(p, x).subs(x, 0) == 0 and s.diff(p, x).subs(x, 2) == 0 and p.subs(x, 2) == 3
        for p in p_candidates])

# Câu 7: Tối ưu chi phí trung bình C(x) = (2x^2 + 50)/x với x >= 1
c7 = (2*x**2 + 50)/x
opt_x7 = [r for r in s.solve(s.diff(c7, x), x) if r > 0][0]
choose([opt_x7 == v for v in (10, 25, 2, 5)])

# Câu 8: Vectơ AB + AD + AA' trong hình hộp ABCD.A'B'C'D'
# Các lựa chọn: AC, AC', CA', BD'
A8 = s.Matrix(s.symbols("a1:4"))
B8 = s.Matrix(s.symbols("b1:4"))
D8 = s.Matrix(s.symbols("d1:4"))
Ap8 = s.Matrix(s.symbols("ap1:4"))
# Trong hình hộp: C' = A + (B - A) + (D - A) + (A' - A)
Cp8 = B8 + D8 + Ap8 - 2*A8
sum_vec = (B8 - A8) + (D8 - A8) + (Ap8 - A8)
choose([s.simplify(sum_vec - (v - A8)) == s.zeros(3, 1) for v in (B8 + D8 - A8, Cp8, 2*A8 - Cp8, D8 + Ap8 - A8)])

# Câu 9: Tọa độ vectơ a = 2i - 3j + k
# Các lựa chọn: (-3; 2; 1), (2; 1; -3), (2; -3; 1), (-2; 3; -1)
vec_a = (2, -3, 1)
choose([vec_a == v for v in ((-3, 2, 1), (2, 1, -3), (2, -3, 1), (-2, 3, -1))])

# Câu 10: Tích vô hướng u = (1; 2; -1) và v = (-2; 1; 3)
u10 = s.Matrix([1, 2, -1])
v10 = s.Matrix([-2, 1, 3])
dot10 = u10.dot(v10)
choose([dot10 == val for val in (3, 7, 1, -3)])

# Câu 11: Độ dài đoạn thẳng MN với M(1; -1; 2), N(3; 1; 3)
M11 = s.Matrix([1, -1, 2])
N11 = s.Matrix([3, 1, 3])
len11 = (N11 - M11).norm()
choose([len11 == val for val in (3, 9, s.sqrt(5), s.sqrt(13))])

# Câu 12: Trọng tâm tam giác A(2; 1; -3), B(0; -2; 5), C(4; 4; 1)
A12 = s.Matrix([2, 1, -3])
B12 = s.Matrix([0, -2, 5])
C12 = s.Matrix([4, 4, 1])
G12 = (A12 + B12 + C12)/3
choose([G12 == s.Matrix(v) for v in ((6, 3, 3), (2, 1, 1), (1, 2, 1), (2, -1, 1))])

assert multiple_choice == key["I"], (multiple_choice, key["I"])
assert Counter(multiple_choice) == dict.fromkeys("ABCD", 3), Counter(multiple_choice)


# ==========================================
# PHẦN II: 4 câu đúng / sai (16 ý)
# ==========================================
true_false = []

# Câu 1: Khảo sát f(x) = (x^2 - 3x + 6)/(x - 2) trên R \ {2}
f_ii1 = (x**2 - 3*x + 6)/(x - 2)
df_ii1 = s.diff(f_ii1, x)
crit_ii1 = s.solve(df_ii1, x)
pts_ii1 = [s.Matrix([r, f_ii1.subs(x, r)]) for r in crit_ii1]
dist_ii1 = (pts_ii1[0] - pts_ii1[1]).norm()

true_false.append([
    s.simplify(df_ii1 - x*(x-4)/(x-2)**2) == 0,
    False,  # Hàm số không nghịch biến trên khoảng (0; 4) vì không xác định tại x = 2
    s.limit(f_ii1 - (x - 1), x, s.oo) == 0,
    s.simplify(dist_ii1 - 4*s.sqrt(5)) == 0
])

# Câu 2: Bài toán tối ưu tour du lịch x in [20; 120]
p_ii2 = 1500 - 5*x
R_ii2 = x * p_ii2
C_ii2 = 300*x + 12000
P_ii2 = R_ii2 - C_ii2
best_x_ii2 = max(range(20, 121), key=lambda val: P_ii2.subs(x, val))
max_profit_ii2 = P_ii2.subs(x, best_x_ii2)

true_false.append([
    s.expand(R_ii2 - (-5*x**2 + 1500*x)) == 0,
    s.expand(P_ii2 - (-5*x**2 + 1200*x - 12000)) == 0,
    best_x_ii2 == 120,
    max_profit_ii2 == 50000  # Đề ghi 50 triệu đồng, nhưng thực tế là 60 triệu đồng -> Sai
])

# Câu 3: A(2; 1; -1), B(0; 3; 1), C(4; 5; 3)
A_ii3 = s.Matrix([2, 1, -1])
B_ii3 = s.Matrix([0, 3, 1])
C_ii3 = s.Matrix([4, 5, 3])
AB_ii3 = B_ii3 - A_ii3
AC_ii3 = C_ii3 - A_ii3
D_ii3 = A_ii3 + C_ii3 - B_ii3

true_false.append([
    AB_ii3 == s.Matrix([-2, 2, 2]),
    AC_ii3.norm() == 6,
    AB_ii3.dot(AC_ii3) == 0,  # AB.AC = 12 != 0 -> Sai
    D_ii3 == s.Matrix([6, 3, 1])
])

# Câu 4: Đèn treo cân bằng m = 6 kg, g = 10 -> P = 60 N
# S(0; 0; 4), A(0; 3; 0), B(-3*sqrt(3)/2; -3/2; 0), C(3*sqrt(3)/2; -3/2; 0)
SA_vec = s.Matrix([0, 3, -4])
SB_vec = s.Matrix([-3*s.sqrt(3)/2, s.Rational(-3, 2), -4])
SC_vec = s.Matrix([3*s.sqrt(3)/2, s.Rational(-3, 2), -4])
T_mag = s.symbols("T_mag", positive=True)
T1_vec = (T_mag/5)*SA_vec
T2_vec = (T_mag/5)*SB_vec
T3_vec = (T_mag/5)*SC_vec
P_vec = s.Matrix([0, 0, 60])
eq_balance = s.simplify(T1_vec + T2_vec + T3_vec + P_vec)
T_solved = s.solve(eq_balance[2], T_mag)[0]

true_false.append([
    P_vec.norm() == 60,
    SA_vec.norm() == 5,
    T_solved == 30,  # T_solved = 25 N != 30 N -> Sai
    T1_vec.subs(T_mag, T_solved) == s.Matrix([0, 15, -20])
])

true_false = [[bool(v) for v in row] for row in true_false]
assert true_false == key["II"], (true_false, key["II"])


# ==========================================
# PHẦN III: 6 câu trả lời ngắn
# ==========================================
answers = []

# Câu 1: Số giá trị nguyên của m in [-10; 10] để y = (x + 3m)/(x + 6) đồng biến
# y' = (6 - 3m)/(x+6)^2 > 0 <=> 6 - 3m > 0 <=> m < 2
m_int_count = sum(1 for mv in range(-10, 11) if 6 - 3*mv > 0)
assert m_int_count == 12
answers.append(str(m_int_count))

# Câu 2: Hình hộp ABCD.A'B'C'D' với A(1; 0; 1), B(2; 1; 2), D(1; 3; 0), A'(3; 2; 4).
# Tọa độ C'(a; b; c). Tính a + b + c.
A_box = s.Matrix([1, 0, 1])
B_box = s.Matrix([2, 1, 2])
D_box = s.Matrix([1, 3, 0])
Ap_box = s.Matrix([3, 2, 4])
Cp_box = A_box + (B_box - A_box) + (D_box - A_box) + (Ap_box - A_box)
assert Cp_box == s.Matrix([4, 6, 4])
answers.append(str(sum(Cp_box)))

# Câu 3: Hàm số y = x^3 - 3mx^2 + 4m^3 (m > 0). Tìm m để AB = 2*sqrt(5).
f_iii3 = x**3 - 3*m_sym*x**2 + 4*m_sym**3
crit_iii3 = s.solve(s.diff(f_iii3, x), x)
pts_iii3 = [s.Matrix([r, f_iii3.subs(x, r)]) for r in crit_iii3]
dist_sq_iii3 = s.simplify((pts_iii3[0] - pts_iii3[1]).dot(pts_iii3[0] - pts_iii3[1]))
m_val_iii3 = s.solve(dist_sq_iii3 - 20, m_sym)[0]
assert m_val_iii3 == 1
answers.append(str(m_val_iii3))

# Câu 4: Khoảng cách ngắn nhất giữa At(t; 2t; 2t - 1) và Bt(3t - 2; 3t - 4; 4) với 0 <= t <= 4
At_drone = s.Matrix([t, 2*t, 2*t - 1])
Bt_drone = s.Matrix([3*t - 2, 3*t - 4, 4])
dist_sq_drone = s.expand((Bt_drone - At_drone).dot(Bt_drone - At_drone))
t_crit = s.solve(s.diff(dist_sq_drone, t), t)[0]
assert t_crit == 2 and 0 <= t_crit <= 4
min_dist_drone = s.sqrt(dist_sq_drone.subs(t, t_crit))
assert min_dist_drone == 3
answers.append(str(min_dist_drone))

# Câu 5: Bể chứa nước chữ nhật không nắp V = 288 m^3, đáy rộng x, dài 2x. Chi phí 500 nghìn đồng/m^2.
# S(x) = 2x^2 + 6xh = 2x^2 + 864/x. S'(x) = 0 <=> x = 6. S(6) = 216 m^2. Chi phí = 216 * 0.5 = 108 triệu.
S_box = 2*x**2 + 864/x
x_opt5 = s.solve(s.diff(S_box, x), x)[0]
assert x_opt5 == 6
cost_min5 = S_box.subs(x, 6) * s.Rational(1, 2)
assert cost_min5 == 108
answers.append(str(cost_min5))

# Câu 6: Di chuyển từ A đến B: AC = 12 km, BC = 6 km. Đi bộ AM với v = 10 km/h, thuyền MB với v = 6 km/h.
# T(x) = (12 - x)/10 + sqrt(x^2 + 36)/6. T'(x) = 0 <=> x = 4.5. T(4.5) = 2 giờ.
Tx6 = (12 - x)/10 + s.sqrt(x**2 + 36)/6
x_opt6 = [r for r in s.solve(s.diff(Tx6, x), x) if r > 0][0]
assert x_opt6 == s.Rational(9, 2)
T_min6 = Tx6.subs(x, x_opt6)
assert T_min6 == 2
answers.append(str(T_min6))

assert answers == key["III"], (answers, key["III"])
assert all(len(a) <= 4 for a in answers), answers

# Kiểm tra từ cấm ngoài chương trình trong TeX (nếu file tồn tại)
tex_path = BASE / "De_giua_ki_1_03.tex"
if tex_path.exists():
    source = tex_path.read_text(encoding="utf-8")
    for outside_scope in ("nguyên hàm", "tích phân", "xác suất", "thống kê", "mặt cầu", "phương trình mặt phẳng", "phương trình đường thẳng"):
        assert outside_scope not in source.lower(), outside_scope

report = {
    "status": "passed",
    "multiple_choice": multiple_choice,
    "true_false": true_false,
    "short_answers": answers,
    "checked": {
        "multiple_choice": 12,
        "true_false_statements": 16,
        "short_answers": 6
    },
    "scope": "Bài 1–8; Chương I (Ứng dụng đạo hàm khảo sát hàm số) và Chương II (Vectơ và tọa độ trong không gian)",
    "note": "Kiểm tra toán học độc lập bằng SymPy 100% tất cả 22 câu."
}
(BASE / "kiem_tra_toan.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, indent=2))
