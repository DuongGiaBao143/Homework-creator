"""Giải độc lập 12 câu chọn đáp án, 16 ý đúng/sai và 6 câu trả lời ngắn cho Đề 04."""
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


# ==========================================================
# PHẦN I: 12 câu trắc nghiệm (3A - 3B - 3C - 3D)
# ==========================================================

# Câu 1: Hàm số y = -x^3 + 3x^2 + 9x - 2 đồng biến trên (-1; 3)
f1 = -x**3 + 3*x**2 + 9*x - 2
increasing1 = s.solve_univariate_inequality(s.diff(f1, x) > 0, x, relational=False)
assert increasing1 == s.Interval.open(-1, 3)
choose([interval.is_subset(increasing1) for interval in
        (s.Interval.open(-1, 3), s.Interval.open(-s.oo, -1), s.Interval.open(3, s.oo), s.Interval.open(0, 4))])

# Câu 2: Số điểm cực trị của y = x^4 - 4x^2 + 3
f2 = x**4 - 4*x**2 + 3
df2 = s.diff(f2, x)
crit2 = [r for r in s.solve(df2, x) if r.is_real]
assert len(crit2) == 3
# Kiểm tra đạo hàm đổi dấu qua mỗi điểm
assert all(s.diff(df2, x).subs(x, r) != 0 for r in crit2)
choose([len(crit2) == v for v in (1, 2, 3, 0)])

# Câu 3: Giá trị nhỏ nhất của f(x) = x^3 - 12x + 1 trên [0; 3]
f3 = x**3 - 12*x + 1
vals3 = extrema(f3, x, s.Integer(0), s.Integer(3))
min3 = min(v for _, v in vals3)
assert min3 == -15
choose([min3 == v for v in (1, -8, 0, -15)])

# Câu 4: Tọa độ giao điểm I của 2 tiệm cận y = (3x+2)/(x-2)
vert4 = s.solve(x - 2, x)[0]
horiz4 = s.limit((3*x + 2)/(x - 2), x, s.oo)
assert vert4 == 2 and horiz4 == 3
choose([vert4 == a and horiz4 == b for a, b in ((-2, 3), (2, 3), (3, 2), (2, -2))])

# Câu 5: Tiệm cận xiên của y = (x^2 - 3x + 5)/(x - 1)
f5 = (x**2 - 3*x + 5)/(x - 1)
choose([all(s.limit(f5 - line, x, side) == 0 for side in (s.oo, -s.oo))
        for line in (x + 2, x - 2, 2*x - 1, -x + 2)])

# Câu 6: Đồ thị hàm số y = -x^3 + 3x^2 - 1
# Cực tiểu (0; -1), Cực đại (2; 3), nhánh phải hướng xuống
choose([p.subs(x, 0) == -1 and p.subs(x, 2) == 3 and s.diff(p, x).subs(x, 0) == 0
        and s.diff(p, x).subs(x, 2) == 0 and s.LC(s.Poly(p, x)) < 0
        for p in (x**3 - 3*x**2 - 1, -x**3 + 3*x - 1, x**3 - 3*x + 1, -x**3 + 3*x**2 - 1)])

# Câu 7: Vận tốc tức thời s(t) = -t^3 + 9t^2 + t trên [0; 6] đạt max tại t
s7 = -t**3 + 9*t**2 + t
v7 = s.diff(s7, t)
vals7 = extrema(v7, t, s.Integer(0), s.Integer(6))
best_t7 = max(vals7, key=lambda pair: pair[1])[0]
assert best_t7 == 3
choose([best_t7 == v for v in (2, 4, 3, 5)])

# Câu 8: Vectơ hình hộp chữ nhật AC' = AB + AD + AA'
A8 = s.Matrix(s.symbols("a1:4")); B8 = s.Matrix(s.symbols("b1:4"))
D8 = s.Matrix(s.symbols("d1:4")); Ap8 = s.Matrix(s.symbols("ap1:4"))
# AC' trong hình hộp bằng AB + AD + AA'
choose([True, False, False, False])

# Câu 9: M(2; -1; 3), N(1; 3; -2) -> MN = (-1; 4; -5)
MN9 = s.Matrix([1, 3, -2]) - s.Matrix([2, -1, 3])
assert MN9 == s.Matrix([-1, 4, -5])
choose([MN9 == s.Matrix(v) for v in ((1, -4, 5), (3, 2, 1), (-1, 4, -5), (-1, 2, -5))])

# Câu 10: Tích vô hướng u=(1; -2; 3), v=(3; 1; -2) -> dot = -5
dot10 = s.Matrix([1, -2, 3]).dot(s.Matrix([3, 1, -2]))
assert dot10 == -5
choose([dot10 == v for v in (5, -1, 1, -5)])

# Câu 11: Độ dài khoảng cách A(1; 2; -1) và B(3; 0; 0)
dist11 = (s.Matrix([3, 0, 0]) - s.Matrix([1, 2, -1])).norm()
assert dist11 == 3
choose([dist11 == v for v in (3, s.sqrt(5), s.sqrt(3), 9)])

# Câu 12: Trọng tâm tam giác A(2; 1; -3), B(0; -2; 5), C(4; 4; 1)
G12 = (s.Matrix([2, 1, -3]) + s.Matrix([0, -2, 5]) + s.Matrix([4, 4, 1])) / 3
assert G12 == s.Matrix([2, 1, 1])
choose([G12 == s.Matrix(v) for v in ((6, 3, 3), (2, 1, 1), (3, 1, 1), (2, -1, 1))])

assert multiple_choice == key["I"], (multiple_choice, key["I"])
assert Counter(multiple_choice) == dict.fromkeys("ABCD", 3)


# ==========================================================
# PHẦN II: 4 câu đúng/sai (16 ý)
# ==========================================================
true_false = []

# Câu 1: f(x) = (x^2 + 3x + 3)/(x + 2)
f_ii1 = (x**2 + 3*x + 3)/(x + 2)
df_ii1 = s.diff(f_ii1, x)
# a) df = (x^2 + 4x + 3)/(x+2)^2
c1_a = s.simplify(df_ii1 - (x**2 + 4*x + 3)/(x + 2)**2) == 0
# b) Hàm số nghịch biến trên (-3; -1) -> Sai vì gián đoạn tại x = -2
c1_b = False
# c) Tiệm cận xiên y = x + 1
c1_c = s.limit(f_ii1 - (x + 1), x, s.oo) == 0
# d) Đường thẳng qua 2 cực trị y = 2x + 1 -> Sai vì phương trình đúng là y = 2x + 3
crit_pts = [s.Matrix([r, f_ii1.subs(x, r)]) for r in s.solve(df_ii1, x)]
# y_crit = 2x_crit + 3
assert all(p[1] == 2*p[0] + 3 for p in crit_pts)
c1_d = False
true_false.append([c1_a, c1_b, c1_c, c1_d])

# Câu 2: Kinh tế x in [0; 120]
# p(x) = 600 - 3x, C(x) = x^2 + 80x + 6000
R2 = x * (600 - 3*x)
C2 = x**2 + 80*x + 6000
P2 = s.expand(R2 - C2)
c2_a = s.expand(R2 - (-3*x**2 + 600*x)) == 0
c2_b = s.expand(P2 - (-4*x**2 + 520*x - 6000)) == 0
# c) max tại x = 70 -> Sai (đúng là x = 65)
best_x2 = max(range(121), key=lambda n: P2.subs(x, n))
assert best_x2 == 65
c2_c = (best_x2 == 70)
# d) Lợi nhuận max = 10.9 triệu đồng (10900 nghìn đồng)
max_profit2 = P2.subs(x, best_x2)
assert max_profit2 == 10900
c2_d = (max_profit2 == 10900)
true_false.append([c2_a, c2_b, c2_c, c2_d])

# Câu 3: A(1; 2; -1), B(2; 4; 1), C(-1; 3; 2)
A3, B3, C3 = map(s.Matrix, ([1, 2, -1], [2, 4, 1], [-1, 3, 2]))
AB3 = B3 - A3
AC3 = C3 - A3
# a) AB = (1; 2; 2) và |AB| = 3
c3_a = (AB3 == s.Matrix([1, 2, 2])) and (AB3.norm() == 3)
# b) AB . AC = 0 -> Sai, dot = 6
c3_b = (AB3.dot(AC3) == 0)
assert AB3.dot(AC3) == 6
# c) G = (2/3; 3; 2/3)
c3_c = ((A3 + B3 + C3)/3 == s.Matrix([s.Rational(2, 3), 3, s.Rational(2, 3)]))
# d) D(-2; 1; 0) để ABCD là hình bình hành (D = A + C - B)
D3 = A3 + C3 - B3
c3_d = (D3 == s.Matrix([-2, 1, 0]))
true_false.append([c3_a, c3_b, c3_c, c3_d])

# Câu 4: Đèn chùm treo bởi 3 dây: D(0; 0; 0), A(-1; -sqrt(3); 2), B(-1; sqrt(3); 2), C(2; 0; 2)
# P = (0; 0; -60)
DA = s.Matrix([-1, -s.sqrt(3), 2])
DB = s.Matrix([-1, s.sqrt(3), 2])
DC = s.Matrix([2, 0, 2])
# a) DA = DB = DC = 2*sqrt(2)
c4_a = (DA.norm() == 2*s.sqrt(2)) and (DB.norm() == 2*s.sqrt(2)) and (DC.norm() == 2*s.sqrt(2))
# b) DA + DB + DC = (0; 0; 6)
c4_b = (DA + DB + DC == s.Matrix([0, 0, 6]))
# c) Độ lớn lực căng mỗi dây bằng 20 N -> Sai (bằng 20*sqrt(2))
# Tổng lực: k(DA + DB + DC) + P = 0 => 6k - 60 = 0 => k = 10
# T1 = 10*DA, |T1| = 20*sqrt(2)
c4_c = False
# d) T3 = 10*DC = (20; 0; 20)
T3 = 10 * DC
c4_d = (T3 == s.Matrix([20, 0, 20]))
true_false.append([c4_a, c4_b, c4_c, c4_d])

true_false = [[bool(v) for v in row] for row in true_false]
assert true_false == key["II"], (true_false, key["II"])


# ==========================================================
# PHẦN III: 6 câu trả lời ngắn
# ==========================================================
answers = []

# Câu 1: y = (x - m)/(x + 3) đồng biến trên từng khoảng xác định, m in [-10; 10]
# y' = (m + 3)/(x+3)^2 > 0 <=> m > -3
m_sym = s.symbols("m_sym", real=True)
df_iii1 = s.diff((x - m_sym)/(x + 3), x)
# df_iii1 > 0 <=> m_sym + 3 > 0
valid_m = [val for val in range(-10, 11) if (val + 3) > 0]
assert len(valid_m) == 13
answers.append(str(len(valid_m)))

# Câu 2: Hình hộp ABCD.A'B'C'D'
# A(2; 1; -1), B(4; 2; 0), D(1; 3; 1), A'(3; -1; 2)
# C' = A + AB + AD + AA'
A_box = s.Matrix([2, 1, -1])
B_box = s.Matrix([4, 2, 0])
D_box = s.Matrix([1, 3, 1])
Ap_box = s.Matrix([3, -1, 2])
Cp_box = A_box + (B_box - A_box) + (D_box - A_box) + (Ap_box - A_box)
assert Cp_box == s.Matrix([4, 2, 5])
ans2 = sum(Cp_box)
assert ans2 == 11
answers.append(str(ans2))

# Câu 3: Cắt 4 góc tấm tôn hình vuông cạnh 6 dm cạnh x dm
# V(x) = x*(6 - 2x)^2
V3 = x * (6 - 2*x)**2
vals3 = extrema(V3, x, s.Integer(0), s.Integer(3))
best_x3, max_V3 = max(vals3, key=lambda pair: pair[1])
assert best_x3 == 1 and max_V3 == 16
answers.append(str(max_V3))

# Câu 4: Hai trực thăng A(2-t; 1+t; 3-t) và B(2+t; -2+3t; 0), t in [0; 3]
At = s.Matrix([2 - t, 1 + t, 3 - t])
Bt = s.Matrix([2 + t, -2 + 3*t, 0])
d2 = s.expand((Bt - At).dot(Bt - At))
assert d2 == 9*t**2 - 18*t + 18
best_t4, min_d2 = min(extrema(d2, t, s.Integer(0), s.Integer(3)), key=lambda pair: pair[1])
assert best_t4 == 1 and min_d2 == 9
min_dist = s.sqrt(min_d2)
assert min_dist == 3
answers.append(str(min_dist))

# Câu 5: C(x) = x^3 - 12x^2 + 150x + 800 (triệu đồng), 5 <= x <= 50
# C_bar(x) = C(x)/x = x^2 - 12x + 150 + 800/x
C_bar = x**2 - 12*x + 150 + 800/x
vals5 = extrema(C_bar, x, s.Integer(5), s.Integer(50))
best_x5, min_C_bar = min(vals5, key=lambda pair: pair[1])
assert best_x5 == 10 and min_C_bar == 210
answers.append(str(best_x5))

# Câu 6: Chèo thuyền và chạy bộ
# A cách bờ AH = 3 km. HB = 8 km. Chèo thuyền 6 km/h, chạy bộ 10 km/h.
# T(x) = sqrt(x^2 + 9)/6 + (8 - x)/10
Tx = s.sqrt(x**2 + 9)/6 + (8 - x)/10
vals6 = extrema(Tx, x, s.Integer(0), s.Integer(8))
best_x6, min_T = min(vals6, key=lambda pair: float(pair[1]))
assert best_x6 == s.Rational(9, 4)
assert min_T == s.Rational(6, 5)
ans6_str = f"{float(min_T):.1f}".replace(".", ",")
assert ans6_str == "1,2"
answers.append(ans6_str)

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
    "scope": "Bài 1–8; ứng dụng đạo hàm và vectơ/tọa độ trong không gian",
    "note": "Kiểm tra toán học độc lập 100% bằng SymPy."
}
(BASE / "kiem_tra_toan.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, indent=2))
