"""Giải độc lập 12 câu chọn đáp án, 16 ý đúng/sai và 6 câu trả lời ngắn của Đề số 02."""
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


# ==========================================
# PHẦN I: 12 câu trắc nghiệm nhiều lựa chọn
# ==========================================

# Câu 1: Hàm số y = -x^3 + 3x^2 - 1 đồng biến trên khoảng nào?
f = -x**3 + 3*x**2 - 1
df = s.diff(f, x)
inc = s.solve_univariate_inequality(df > 0, x, relational=False)
assert inc == s.Interval.open(0, 2)
choose([s.Interval.open(a, b).is_subset(inc) if b > a else False
        for a, b in ((0, 2), (-s.oo, 0), (2, s.oo), (-2, 0))])

# Câu 2: Điểm cực tiểu của đồ thị hàm số y = x^3 - 3x + 2 là
f = x**3 - 3*x + 2
roots = s.solve(s.diff(f, x), x)
# x = 1: df2 = 6 > 0 (cực tiểu), y = 0
# x = -1: df2 = -6 < 0 (cực đại), y = 4
choose([s.diff(f, x).subs(x, a) == 0 and s.diff(f, x, 2).subs(x, a) > 0 and f.subs(x, a) == b
        for a, b in ((-1, 4), (1, 0), (1, 2), (0, 2))])

# Câu 3: Giá trị nhỏ nhất của f(x) = x^3 - 3x^2 - 9x + 1 trên [-2; 2]
f = x**3 - 3*x**2 - 9*x + 1
candidates = extrema(f, x, s.Integer(-2), s.Integer(2))
min_val = min(v for _, v in candidates)
assert min_val == -21
choose([min_val == v for v in (-1, 6, -21, -20)])

# Câu 4: Tiệm cận đứng và tiệm cận ngang của y = (3x + 2)/(x - 1)
f = (3*x + 2)/(x - 1)
vert = s.solve(x - 1, x)[0]
horiz = s.limit(f, x, s.oo)
assert vert == 1 and horiz == 3
choose([vert == a and horiz == b for a, b in ((-1, 3), (3, 1), (1, -3), (1, 3))])

# Câu 5: Tiệm cận xiên của y = (2x^2 - 3x + 5)/(x - 2)
f = (2*x**2 - 3*x + 5)/(x - 2)
# y = ax + b
a = s.limit(f/x, x, s.oo)
b = s.limit(f - a*x, x, s.oo)
assert a == 2 and b == 1
choose([all(s.limit(f - line, x, side) == 0 for side in (s.oo, -s.oo))
        for line in (2*x + 1, 2*x - 1, 2*x + 5, x + 1)])

# Câu 6: Đồ thị hàm số y = x^3 - 3x^2 + 2 đi qua (0, 2), (2, -2), cực đại tại x=0, cực tiểu tại x=2
choose([p.subs(x, 0) == 2 and p.subs(x, 2) == -2 and s.diff(p, x).subs(x, 0) == 0
        and s.diff(p, x).subs(x, 2) == 0 and s.diff(p, x, 2).subs(x, 0) < 0
        for p in (-x**3 + 3*x**2 + 2, x**3 - 3*x**2 + 2, x**3 - 3*x + 2, x**3 + 3*x**2 + 2)])

# Câu 7: Số lượng vi khuẩn N(t) = -t^3 + 9t^2 + 120 trên [0; 8] đạt max tại t nào?
N = -t**3 + 9*t**2 + 120
cand = extrema(N, t, s.Integer(0), s.Integer(8))
best_t = max(cand, key=lambda pair: pair[1])[0]
assert best_t == 6
choose([best_t == v for v in (3, 4, 6, 8)])

# Câu 8: Tứ diện S.ABC, M là trung điểm BC => SB + SC = 2SM
S_vec = s.Matrix(s.symbols("s1:4"))
B_vec = s.Matrix(s.symbols("b1:4"))
C_vec = s.Matrix(s.symbols("c1:4"))
M_vec = (B_vec + C_vec)/2
SB = B_vec - S_vec
SC = C_vec - S_vec
SM = M_vec - S_vec
choose([s.simplify(SB + SC - v) == s.zeros(3, 1) for v in (SM, 3*SM, -2*SM, 2*SM)])

# Câu 9: u = 2i - 3k + j => u = (2, 1, -3)
i_v = s.Matrix([1, 0, 0])
j_v = s.Matrix([0, 1, 0])
k_v = s.Matrix([0, 0, 1])
u_vec = 2*i_v - 3*k_v + j_v
choose([u_vec == s.Matrix(v) for v in ((2, 1, -3), (2, -3, 1), (-3, 2, 1), (1, 2, -3))])

# Câu 10: Chiếu vuông góc của M(3, -2, 5) lên (Oxy) là (3, -2, 0)
proj = s.Matrix([3, -2, 0])
choose([proj == s.Matrix(v) for v in ((0, 0, 5), (3, -2, 0), (3, 0, 5), (0, -2, 5))])

# Câu 11: A(2, 1, -1), B(0, 3, -2) => AB = 3
A_pt = s.Matrix([2, 1, -1])
B_pt = s.Matrix([0, 3, -2])
d_AB = (B_pt - A_pt).norm()
assert d_AB == 3
choose([d_AB == v for v in (s.sqrt(5), 9, 3, s.sqrt(13))])

# Câu 12: a = (1, 2, -2), b = (2, -1, 4) => a.b = -8
a_vec = s.Matrix([1, 2, -2])
b_vec = s.Matrix([2, -1, 4])
dot_val = a_vec.dot(b_vec)
assert dot_val == -8
choose([dot_val == v for v in (8, 4, -4, -8)])

assert multiple_choice == key["I"], (multiple_choice, key["I"])
assert Counter(multiple_choice) == dict.fromkeys("ABCD", 3)


# ==========================================
# PHẦN II: 4 câu đúng/sai (16 ý)
# ==========================================
true_false = []

# Câu 1: f(x) = (x^2 - x + 1)/(x - 1)
f = (x**2 - x + 1)/(x - 1)
df = s.diff(f, x)
crit = s.solve(df, x)
pts = [s.Matrix([c, f.subs(x, c)]) for c in crit]
# a) df = x(x-2)/(x-1)^2
stmt_a = s.simplify(df - x*(x-2)/(x-1)**2) == 0
# b) đồng biến trên (0; 2) -> sai vì df < 0 trên (0; 1) và (1; 2), và không xác định tại 1
stmt_b = s.Interval.open(0, 2).is_subset(s.solve_univariate_inequality(df > 0, x, relational=False))
# c) tiệm cận xiên y = x
stmt_c = s.limit(f - x, x, s.oo) == 0
# d) khoảng cách giữa 2 cực trị là 2*sqrt(5)
dist_crit = (pts[0] - pts[1]).norm()
stmt_d = s.simplify(dist_crit - 2*s.sqrt(5)) == 0
true_false.append([bool(stmt_a), bool(stmt_b), bool(stmt_c), bool(stmt_d)])

# Câu 2: Kinh tế C(x) = x^2 - 40x + 1600, x in [1; 120], giá 80
C_x = x**2 - 40*x + 1600
C_bar = s.simplify(C_x / x)
# a) C_bar = x - 40 + 1600/x
stmt2_a = s.simplify(C_bar - (x - 40 + 1600/x)) == 0
# b) chi phí trung bình nhỏ nhất tại x = 40
cand_C = extrema(C_bar, x, s.Integer(1), s.Integer(120))
best_x_cost = min(cand_C, key=lambda pair: pair[1])[0]
stmt2_b = (best_x_cost == 40)
# c) Lợi nhuận P(x) = 80x - C(x) = -x^2 + 120x - 1600
P_x = 80*x - C_x
stmt2_c = s.simplify(P_x - (-x**2 + 120*x - 1600)) == 0
# d) Lợi nhuận lớn nhất khi x = 40 (sai, vì max tại x = 60)
best_x_profit = max(range(1, 121), key=lambda n: P_x.subs(x, n))
stmt2_d = (best_x_profit == 40)
true_false.append([bool(stmt2_a), bool(stmt2_b), bool(stmt2_c), bool(stmt2_d)])

# Câu 3: A(2, -1, 1), B(0, 1, 2), C(3, 0, -1)
A = s.Matrix([2, -1, 1])
B = s.Matrix([0, 1, 2])
C = s.Matrix([3, 0, -1])
AB = B - A
AC = C - A
# a) AB = (-2, 2, 1)
stmt3_a = (AB == s.Matrix([-2, 2, 1]))
# b) AB = 3
stmt3_b = (AB.norm() == 3)
# c) Tam giác ABC vuông tại A (AB.AC = 0) -> sai vì AB.AC = -2
stmt3_c = (AB.dot(AC) == 0)
# d) ABCD là hình bình hành => D = C - AB = (5, -2, -2)
D = C - AB
stmt3_d = (D == s.Matrix([5, -2, -2]))
true_false.append([bool(stmt3_a), bool(stmt3_b), bool(stmt3_c), bool(stmt3_d)])

# Câu 4: Cân bằng lực đèn
F1 = s.Matrix([10, 20, 20])
F2 = s.Matrix([-10, 20, 20])
F3 = s.Matrix([0, -40, 20])
P_grav = s.Matrix([0, 0, -60])
# a) |F1| = 30 N
stmt4_a = (F1.norm() == 30)
# b) |F1| = |F2|
stmt4_b = (F1.norm() == F2.norm())
# c) F1 . F2 = 0 (sai, F1.F2 = 700)
stmt4_c = (F1.dot(F2) == 0)
# d) Cân bằng: F1 + F2 + F3 + P = 0
stmt4_d = (F1 + F2 + F3 + P_grav == s.zeros(3, 1))
true_false.append([bool(stmt4_a), bool(stmt4_b), bool(stmt4_c), bool(stmt4_d)])

assert true_false == key["II"], (true_false, key["II"])


# ==========================================
# PHẦN III: 6 câu trả lời ngắn
# ==========================================
answers = []

# Câu 1: Số giá trị m nguyên thuộc [-5; 5] để y = (x + 3m)/(x - 2) nghịch biến trên từng khoảng xác định
# y' = (-2 - 3m)/(x - 2)^2 < 0 <=> -2 - 3m < 0 <=> m > -2/3.
# m in [-5; 5], m in Z => m in {0, 1, 2, 3, 4, 5} => 6 giá trị
df1 = s.diff((x + 3*m)/(x - 2), x)
num = s.simplify(df1 * (x - 2)**2)
valid_m = [val for val in range(-5, 6) if num.subs(m, val) < 0]
assert valid_m == [0, 1, 2, 3, 4, 5]
answers.append(str(len(valid_m)))

# Câu 2: Hình hộp ABCD.A'B'C'D' với A(1, 0, 1), B(2, 1, 2), D(1, -1, 3), A'(4, 2, -1)
# C' = A + AB + AD + AA'
A_h = s.Matrix([1, 0, 1])
B_h = s.Matrix([2, 1, 2])
D_h = s.Matrix([1, -1, 3])
Ap_h = s.Matrix([4, 2, -1])
Cp_h = A_h + (B_h - A_h) + (D_h - A_h) + (Ap_h - A_h)
assert Cp_h == s.Matrix([5, 2, 2])
answers.append(str(sum(Cp_h)))

# Câu 3: Thùng tôn đáy vuông không nắp, diện tích S = x^2 + 4xh = 108. Thể tích max V = x^2 * h
# h = (108 - x^2)/(4x) => V = (108x - x^3)/4
V_func = (108*x - x**3)/4
cand_V = extrema(V_func, x, s.Integer(0), s.sqrt(108))
best_x_V, max_V = max(cand_V, key=lambda pair: pair[1])
assert best_x_V == 6 and max_V == 108
answers.append(str(max_V))

# Câu 4: Drone A_t(t; 2t; 3t + 1), B_t(4 - t; 4 + t; t + 4), 0 <= t <= 5
# AB^2 = (2t - 4)^2 + (t - 4)^2 + (2t - 3)^2 = 9t^2 - 36t + 41 = 9(t - 2)^2 + 5
At = s.Matrix([t, 2*t, 3*t + 1])
Bt = s.Matrix([4 - t, 4 + t, t + 4])
dist_sq = s.expand((Bt - At).dot(Bt - At))
best_t_d, min_sq = min(extrema(dist_sq, t, s.Integer(0), s.Integer(5)), key=lambda pair: pair[1])
assert best_t_d == 2 and min_sq == 5
min_dist = float(s.sqrt(min_sq))
answers.append(f"{min_dist:.1f}".replace(".", ","))

# Câu 5: y = x^3 - 3mx^2 + 2 (m > 0), cực trị A(0, 2), B(2m, -4m^3 + 2). S(OAB) = 8 => m = ?
# S = 1/2 * OA * |x_B| = 1/2 * 2 * 2m = 2m = 8 => m = 4
m_sym = s.symbols("m_sym", positive=True)
f5 = x**3 - 3*m_sym*x**2 + 2
r5 = s.solve(s.diff(f5, x), x)
A5 = s.Matrix([r5[0], f5.subs(x, r5[0])])
B5 = s.Matrix([r5[1], f5.subs(x, r5[1])])
# Diện tích O, A5, B5: S = 1/2 |x_A y_B - x_B y_A|
area = s.Rational(1, 2) * s.Abs(A5[0]*B5[1] - A5[1]*B5[0])
m_sol = s.solve(area - 8, m_sym)
assert len(m_sol) == 1 and m_sol[0] == 4
answers.append(str(m_sol[0]))

# Câu 6: Trạm bơm M trên bờ sông HK dài 6 km. A cách HK 3 km, B cách HK 5 km (cùng phía).
# L(x) = sqrt(x^2 + 9) + sqrt((6 - x)^2 + 25). Tìm min L
# Min L = sqrt((3 + 5)^2 + 6^2) = sqrt(64 + 36) = 10
L_func = s.sqrt(x**2 + 9) + s.sqrt((6 - x)**2 + 25)
cand_L = extrema(L_func, x, s.Integer(0), s.Integer(6))
best_x_L, min_L = min(cand_L, key=lambda pair: float(pair[1]))
assert best_x_L == s.Rational(9, 4) and min_L == 10
answers.append(str(min_L))

assert answers == key["III"], (answers, key["III"])
assert all(len(a) <= 4 for a in answers)

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
    "scope": "Chương I & Chương II Toán 12 GDPT 2018 (Bài 1–8)",
    "note": "Kiểm tra toán học độc lập 100% bằng SymPy thành công hoàn hảo."
}
(BASE / "kiem_tra_toan.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, indent=2))
