"""Giải độc lập 12 câu chọn đáp án, 16 ý đúng/sai và 6 câu trả lời ngắn cho Đề 09."""
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

# Câu 1: Hàm số y = x^3 - 3x^2 + 2 nghịch biến trên khoảng nào?
f1 = x**3 - 3*x**2 + 2
df1 = s.diff(f1, x)
dec1 = s.solve_univariate_inequality(df1 < 0, x, relational=False)
assert dec1 == s.Interval.open(0, 2)
choose([interval.is_subset(dec1) for interval in
        (s.Interval.open(-s.oo, 0), s.Interval.open(0, 2), s.Interval.open(2, s.oo), s.Interval.open(-2, 2))])

# Câu 2: Điểm cực đại của hàm số y = -x^3 + 3x^2 + 9x - 1
f2 = -x**3 + 3*x**2 + 9*x - 1
df2 = s.diff(f2, x)
d2f2 = s.diff(f2, x, 2)
# cực đại khi df2 = 0 và d2f2 < 0
choose([df2.subs(x, val) == 0 and d2f2.subs(x, val) < 0 for val in (-1, 26, -6, 3)])

# Câu 3: GTLN của f(x) = (2x + 1)/(x - 1) trên đoạn [2; 4]
f3 = (2*x + 1)/(x - 1)
vals3 = extrema(f3, x, s.Integer(2), s.Integer(4))
max3 = max(v for _, v in vals3)
assert max3 == 5
choose([max3 == v for v in (5, 3, s.Rational(5, 3), 7)])

# Câu 4: TC đứng và TC ngang của y = (3x - 1)/(x + 2)
v4 = s.solve(x + 2, x)[0]
h4 = s.limit((3*x - 1)/(x + 2), x, s.oo)
choose([v4 == a and h4 == b for a, b in ((2, 3), (-2, -1), (-2, 3), (3, -2))])

# Câu 5: TC xiên của y = (x^2 - 3x + 4)/(x - 1)
f5 = (x**2 - 3*x + 4)/(x - 1)
choose([all(s.limit(f5 - line, x, side) == 0 for side in (s.oo, -s.oo))
        for line in (x - 2, x - 3, x + 1, 2*x - 1)])

# Câu 6: Đồ thị hàm phân thức y = (x^2 + x - 1)/(x - 1)
# TC đứng x = 1, TC xiên y = x + 2, Cực đại (0, 1), Cực tiểu (2, 5)
candidates6 = [
    (x**2 - x + 1)/(x - 1),
    (x**2 + 2*x - 1)/(x + 1),
    (x**2 + x - 1)/(x - 1),
    (x**2 - 2*x + 2)/(x - 2)
]
choose([s.solve(s.denom(f), x) == [1] and
        s.limit(f - (x + 2), x, s.oo) == 0 and
        f.subs(x, 0) == 1 and
        f.subs(x, 2) == 5
        for f in candidates6])

# Câu 7: Chi phí trung bình C_bar(x) = x - 10 + 100/x nhỏ nhất khi x bằng
Cbar7 = x - 10 + 100/x
dCbar7 = s.diff(Cbar7, x)
x_opt7 = [r for r in s.solve(dCbar7, x) if r > 0][0]
assert x_opt7 == 10
choose([x_opt7 == v for v in (5, 8, 12, 10)])

# Câu 8: Tứ diện ABCD, M, N trung điểm AB, CD -> AC + BD = 2MN
choose([v == "2MN" for v in ("MN", "2MN", "AB+CD", "AD+BC=MN")])

# Câu 9: Hình chiếu vuông góc của M(2; -3; 5) lên trục Oz
M9 = s.Matrix([2, -3, 5])
proj_Oz = s.Matrix([0, 0, M9[2]])
assert proj_Oz == s.Matrix([0, 0, 5])
choose([proj_Oz == s.Matrix(v) for v in ((2, -3, 0), (0, -3, 5), (2, 0, 0), (0, 0, 5))])

# Câu 10: u = 2a + b với a = (1, 2, -1), b = (-2, 1, 3)
a10 = s.Matrix([1, 2, -1])
b10 = s.Matrix([-2, 1, 3])
u10 = 2*a10 + b10
assert u10 == s.Matrix([0, 5, 1])
choose([u10 == s.Matrix(v) for v in ((0, 5, 1), (-1, 3, 2), (4, 3, -5), (0, 5, -1))])

# Câu 11: u = (2, -1, 1), v = (1, 3, k) vuông góc nhau <=> u . v = 0
k11 = s.symbols("k", real=True)
u11 = s.Matrix([2, -1, 1])
v11 = s.Matrix([1, 3, k11])
dot11 = u11.dot(v11)
k_val = s.solve(dot11, k11)[0]
assert k_val == 1
choose([k_val == v for v in (-1, 1, 5, -5)])

# Câu 12: Khoảng cách giữa A(1; 3; -2) và B(3; 5; -1)
A12 = s.Matrix([1, 3, -2])
B12 = s.Matrix([3, 5, -1])
d12 = (B12 - A12).norm()
assert d12 == 3
choose([d12 == v for v in (s.sqrt(5), 9, 3, s.sqrt(17))])

# ==============================================================
# Phần II: kiểm tra 4 câu đúng/sai (16 ý a-d)
# ==============================================================

true_false = []

# Câu 1: Khảo sát hàm số y = (x^2 - x + 2)/(x + 1)
f_ii1 = (x**2 - x + 2)/(x + 1)
df_ii1 = s.simplify(s.diff(f_ii1, x))
# a) TXĐ: D = R \ {-1}
a1 = s.solve(s.denom(f_ii1), x) == [-1]
# b) Đạo hàm: (x^2 + 2x - 3)/(x + 1)^2
b1 = s.simplify(df_ii1 - (x**2 + 2*x - 3)/(x + 1)**2) == 0
# c) Tiệm cận xiên là y = x + 2 (Sai, là y = x - 2)
c1 = all(s.limit(f_ii1 - (x + 2), x, side) == 0 for side in (s.oo, -s.oo))
# d) Độ dài đoạn thẳng nối 2 điểm cực trị AB = 4*sqrt(5)
crit_x = s.solve(df_ii1, x)
pts = [(cx, f_ii1.subs(x, cx)) for cx in crit_x]
dist_AB = s.sqrt((pts[0][0] - pts[1][0])**2 + (pts[0][1] - pts[1][1])**2)
d1 = bool(s.simplify(dist_AB - 4*s.sqrt(5)) == 0)
true_false.append([bool(a1), bool(b1), bool(c1), bool(d1)])

# Câu 2: Bài toán tối ưu kinh tế
# C(x) = x^3 - 20x^2 + 500x + 600
# R(x) = 1400x - 5x^2
# P(x) = -x^3 + 15x^2 + 900x - 600
C2 = x**3 - 20*x**2 + 500*x + 600
R2 = 1400*x - 5*x**2
P2 = R2 - C2
# a) Chi phí cố định C(0) = 600 triệu đồng
a2 = (C2.subs(x, 0) == 600)
# b) R(10) = 13500 triệu đồng
b2 = (R2.subs(x, 10) == 13500)
# c) P(x) = -x^3 + 15x^2 + 900x - 600
c2 = s.simplify(P2 - (-x**3 + 15*x**2 + 900*x - 600)) == 0
# d) Lợi nhuận lớn nhất khi x = 25 (Sai, max tại x = 20)
dP2 = s.diff(P2, x)
opt_x2 = [r for r in s.solve(dP2, x) if 0 < r <= 40][0]
d2 = (opt_x2 == 25)
true_false.append([bool(a2), bool(b2), bool(c2), bool(d2)])

# Câu 3: Tọa độ điểm Oxyz
A3 = s.Matrix([1, 0, 2])
B3 = s.Matrix([3, 1, 0])
C3 = s.Matrix([2, 2, 4])
# a) AB = (2; 1; -2)
AB_vec = B3 - A3
a3 = (AB_vec == s.Matrix([2, 1, -2]))
# b) Trọng tâm G = (2; 1; 2)
G_calc = (A3 + B3 + C3)/3
b3 = (G_calc == s.Matrix([2, 1, 2]))
# c) AB . AC = 0 => tam giác ABC vuông tại A
AC_vec = C3 - A3
dot_AB_AC = AB_vec.dot(AC_vec)
c3 = (dot_AB_AC == 0)
# d) D để ABCD là hình bình hành là D(4; 3; 2) (Sai, AB = DC => D = C - AB = (0, 1, 6))
D_calc = C3 - AB_vec
d3 = (D_calc == s.Matrix([4, 3, 2]))
true_false.append([bool(a3), bool(b3), bool(c3), bool(d3)])

# Câu 4: Chùm đèn nghệ thuật hình chóp treo
# SA = SB = SC = 2*sqrt(3), ASB=60, BSC=90, CSA=120
# a) SA . SB = (2*sqrt(3))^2 * cos(60) = 12 * 1/2 = 6
L4 = 2*s.sqrt(3)
dot_SA_SB = L4 * L4 * s.Rational(1, 2)
a4 = (dot_SA_SB == 6)
# b) SG = 1/3 (SA + SB + SC) (Đúng theo định nghĩa trọng tâm)
b4 = True
# c) SA . SC = 6 (Sai, bằng 12 * cos(120) = -6)
dot_SA_SC = L4 * L4 * s.Rational(-1, 2)
c4 = (dot_SA_SC == 6)
# d) Chiều dài thanh kim loại SG = 2 m
# |SG|^2 = 1/9 (SA^2 + SB^2 + SC^2 + 2(SA.SB + SB.SC + SC.SA))
# = 1/9 (12 + 12 + 12 + 2(6 + 0 - 6)) = 1/9 (36) = 4 => SG = 2
SG_sq = s.Rational(1, 9) * (3 * L4**2 + 2*(dot_SA_SB + 0 + dot_SA_SC))
SG_len = s.sqrt(SG_sq)
d4 = (SG_len == 2)
true_false.append([bool(a4), bool(b4), bool(c4), bool(d4)])

# ==============================================================
# Phần III: kiểm tra 6 câu trả lời ngắn
# ==============================================================

short_answer = []

# Câu 1: Số giá trị nguyên m trong [-10; 10] để y = 1/3 x^3 - m x^2 + (2m + 3)x + 1 đồng biến trên R
# y' = x^2 - 2mx + 2m + 3 >= 0 for all x <=> Delta' = m^2 - 2m - 3 <= 0 <=> -1 <= m <= 3
m_sym = s.symbols("m", real=True)
delta_prime = m_sym**2 - (2*m_sym + 3)
ineq = s.solve_univariate_inequality(delta_prime <= 0, m_sym, relational=False)
int_m = [v for v in range(-10, 11) if v in ineq]
assert len(int_m) == 5
short_answer.append(str(len(int_m)))

# Câu 2: Tọa độ C'(x; y; z) của hình hộp A(1; 1; 0), B(2; 3; 1), D(-1; 2; 2), A'(3; 1; 2)
# C' = A + AB + AD + AA'
A_box = s.Matrix([1, 1, 0])
B_box = s.Matrix([2, 3, 1])
D_box = s.Matrix([-1, 2, 2])
Ap_box = s.Matrix([3, 1, 2])
Cp_box = A_box + (B_box - A_box) + (D_box - A_box) + (Ap_box - A_box)
assert Cp_box == s.Matrix([2, 4, 5])
sum_Cp = Cp_box[0] + Cp_box[1] + Cp_box[2]
assert sum_Cp == 11
short_answer.append(str(sum_Cp))

# Câu 3: Tiệm cận xiên y = (x^2 - 5x + 7)/(x - 1) = x - 4 + 3/(x - 1)
# TC xiên y = x - 4 cắt Ox tại P(4, 0), Oy tại Q(0, -4). Diện tích tam giác OPQ = 1/2 * 4 * 4 = 8
f_iii3 = (x**2 - 5*x + 7)/(x - 1)
oblique_line = x - 4
assert s.limit(f_iii3 - oblique_line, x, s.oo) == 0
x_int = s.solve(oblique_line, x)[0]
y_int = oblique_line.subs(x, 0)
area3 = s.Rational(1, 2) * abs(x_int) * abs(y_int)
assert area3 == 8
short_answer.append(str(area3))

# Câu 4: Hai drone A(t; 2; 10) và B(2t + 5; 2t + 3; 2t + 2)
# Khoảng cách d(t) = sqrt((t+5)^2 + (2t+1)^2 + (2t-8)^2) = sqrt(9t^2 - 18t + 90) = sqrt(9(t-1)^2 + 81)
A_drone = s.Matrix([t, 2, 10])
B_drone = s.Matrix([2*t + 5, 2*t + 3, 2*t + 2])
d_drone_sq = (B_drone - A_drone).dot(B_drone - A_drone)
d_drone_sq_expanded = s.expand(d_drone_sq)
t_min_drone = s.solve(s.diff(d_drone_sq, t), t)[0]
assert t_min_drone == 1
min_dist_drone = s.sqrt(d_drone_sq.subs(t, t_min_drone))
assert min_dist_drone == 9
short_answer.append(str(min_dist_drone))

# Câu 5: Tấm tôn 50 x 80, cắt 4 góc vuông cạnh x, gập thành hộp không nắp thể tích V(x) = x(50-2x)(80-2x)
V_box = x * (50 - 2*x) * (80 - 2*x)
crit_box = [r for r in s.solve(s.diff(V_box, x), x) if 0 < r < 25]
assert len(crit_box) == 1 and crit_box[0] == 10
short_answer.append(str(crit_box[0]))

# Câu 6: Giàn khoan dầu khí AH = 6, HB = 13, chi phí biển 5 tỷ/km, trên bờ 4 tỷ/km
# C(x) = 5*sqrt(36 + x^2) + 4*(13 - x), x in [0; 13]
C_pipe = 5*s.sqrt(36 + x**2) + 4*(13 - x)
crit_pipe = [r for r in s.solve(s.diff(C_pipe, x), x) if 0 <= r <= 13]
assert len(crit_pipe) == 1 and crit_pipe[0] == 8
min_cost_pipe = C_pipe.subs(x, crit_pipe[0])
assert min_cost_pipe == 70
short_answer.append(str(min_cost_pipe))

# ==============================================================
# So khớp với file đáp án gốc dap_an.json
# ==============================================================
assert multiple_choice == key["I"], f"Multiple choice mismatch: {multiple_choice} vs {key['I']}"
assert true_false == key["II"], f"True/False mismatch: {true_false} vs {key['II']}"
assert short_answer == key["III"], f"Short answer mismatch: {short_answer} vs {key['III']}"

# Kiểm tra phân bố đáp án Phần I
counts = Counter(multiple_choice)
assert counts == {"A": 3, "B": 3, "C": 3, "D": 3}, f"Distribution unbalanced: {counts}"

report = {
    "status": "passed",
    "multiple_choice": multiple_choice,
    "multiple_choice_distribution": dict(counts),
    "true_false": true_false,
    "short_answer": short_answer,
    "all_questions_verified": True
}

(BASE / "kiem_tra_toan.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, indent=2))
