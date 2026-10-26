"""Giải độc lập 12 câu chọn đáp án, 16 ý đúng/sai và 6 câu trả lời ngắn."""
from pathlib import Path
from collections import Counter
import json
import sympy as s

BASE = Path(__file__).resolve().parent
x, t = s.symbols("x t", real=True)
m = s.symbols("m", positive=True)
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


# Phần I: kiểm tra riêng từng phương án nhiễu.
f = x**3 - 3*x**2 + 2
decreasing = s.solve_univariate_inequality(s.diff(f, x) < 0, x, relational=False)
choose([interval.is_subset(decreasing) for interval in
        (s.Interval.open(0, 2), s.Interval.open(-s.oo, 0), s.Interval.open(2, s.oo), s.S.Reals)])
f = -x**3 + 3*x + 1
choose([s.diff(f, x).subs(x, a) == 0 and s.diff(f, x, 2).subs(x, a) < 0 and f.subs(x, a) == b
        for a, b in ((-1, -1), (1, 1), (1, 3), (-1, 3))])
value = max(v for _, v in extrema(x**3-3*x, x, s.Integer(-2), s.Integer(1)))
choose([value == v for v in (0, 2, -2, 4)])
vertical = s.solve(x+3, x)[0]
assert s.limit((2*x-1)/(x+3), x, vertical, dir="+") == -s.oo
horizontal = s.limit((2*x-1)/(x+3), x, s.oo)
choose([vertical == a and horizontal == b for a, b in ((3, 2), (-3, -2), (2, -3), (-3, 2))])
f = (x*x+1)/(x-1)
choose([all(s.limit(f-line, x, side) == 0 for side in (s.oo, -s.oo))
        for line in (x+1, x-1, 2*x+1, s.Integer(1))])
choose([p.subs(x, 0) == 0 and p.subs(x, -1) == 2 and p.subs(x, 1) == -2
        and s.diff(p, x).subs(x, -1) == 0 and s.LC(s.Poly(p, x)) > 0
        for p in (-x**3+3*x, x**3-3*x, x**3+3*x, x**3-3*x+1)])
values = extrema(-t**3+6*t*t+15, t, s.Integer(0), s.Integer(5))
best_time = max(values, key=lambda pair: pair[1])[0]
choose([best_time == v for v in (1, 2, 3, 4)])
A = s.Matrix(s.symbols("a1:4")); B = s.Matrix(s.symbols("b1:4"))
C = s.Matrix(s.symbols("c1:4")); D = s.Matrix(s.symbols("d1:4"))
total = (B-A)+(C-B)+(D-C)
choose([s.simplify(total-v) == s.zeros(3, 1) for v in (C-A, D-B, D-A, A-D)])
AB = s.Matrix([4, 0, -1])-s.Matrix([1, -2, 3])
choose([AB == s.Matrix(v) for v in ((5, -2, 2), (3, 2, -4), (-3, -2, 4), (3, -2, -4))])
dot = s.Matrix([2, -1, 3]).dot(s.Matrix([1, 2, -1]))
choose([dot == v for v in (3, 0, -1, -3)])
length = s.Matrix([1, 2, -2]).norm()
choose([length == v for v in (s.sqrt(5), 5, 3, 9)])
midpoint = (s.Matrix([0, 2, 1])+s.Matrix([4, -2, 3]))/2
choose([midpoint == s.Matrix(v) for v in ((2, 0, 2), (4, 0, 4), (2, -2, 1), (-2, 2, -1))])
assert multiple_choice == key["I"], (multiple_choice, key["I"])
assert Counter(multiple_choice) == dict.fromkeys("ABCD", 3)

# Phần II: tính từng mệnh đề thay vì dùng nhãn đã cho.
true_false = []
f = (x*x-2*x+2)/(x-1)
df = s.diff(f, x)
critical = s.solve(df, x)
points = [s.Matrix([a, f.subs(x, a)]) for a in critical]
true_false.append([s.simplify(df-x*(x-2)/(x-1)**2) == 0,
                   s.Interval.open(0, 1).is_subset(s.solve_univariate_inequality(df > 0, x, relational=False)),
                   s.limit(f-(x-1), x, s.oo) == 0,
                   s.simplify((points[0]-points[1]).norm()-2*s.sqrt(2)) == 0])
revenue = x*(500-2*x)
profit = s.expand(revenue-(100*x+6000))
best_quantity = max(range(201), key=lambda n: profit.subs(x, n))
true_false.append([s.expand(revenue+2*x*x-500*x) == 0,
                   s.expand(profit+2*x*x-400*x+6000) == 0,
                   best_quantity == 125,
                   500-2*best_quantity == 300 and profit.subs(x, best_quantity) == 14000])
A, B, C = map(s.Matrix, ([1, 0, 2], [3, 2, 0], [-1, 2, 4]))
AB, AC = B-A, C-A
true_false.append([AB == s.Matrix([2, 2, -2]), (A+B+C)/3 == s.Matrix([1, 2, 2]),
                   AB.dot(AC) == 0, A+C-B == s.Matrix([-3, 0, 6])])
F1, F2, P = map(s.Matrix, ([30, 0, 40], [-30, 0, 40], [0, 0, -80]))
true_false.append([F1+F2 == s.zeros(3, 1), F1.norm() == 50, F1.dot(F2) == 700,
                   F1+F2+P == s.zeros(3, 1)])
true_false = [[bool(v) for v in row] for row in true_false]
assert true_false == key["II"], (true_false, key["II"])

# Phần III: cực trị trên miền hợp lệ, hình hộp và khoảng cách đồng thời.
answers = []
parameter = s.symbols("parameter", real=True)
df = s.factor(s.diff((x+parameter)/(x-2), x))
assert s.simplify(df*(x-2)**2) == -parameter-2
answers.append(str(sum(bool(df.subs({parameter: n, x: 0}) > 0) for n in range(-7, 8))))
A, B, D, Ap = map(s.Matrix, ([1, 1, 0], [3, 1, 1], [0, 3, 1], [2, 0, 4]))
Cp = A+(B-A)+(D-A)+(Ap-A)
assert Cp == s.Matrix([3, 2, 6])
answers.append(str(sum(Cp)))
volume = x*(40-2*x)*(25-2*x)
volume_candidates = extrema(volume, x, s.Integer(0), s.Rational(25, 2))
best_cut, best_volume = max(volume_candidates, key=lambda pair: pair[1])
assert best_cut == 5 and 0 < best_cut < s.Rational(25, 2)
answers.append(str(best_volume))
At, Bt = s.Matrix([3*t, t, 2]), s.Matrix([12-t, 4+t, 8])
distance_squared = s.expand((Bt-At).dot(Bt-At))
best_time, minimum_squared = min(extrema(distance_squared, t, s.Integer(0), s.Integer(5)), key=lambda pair: pair[1])
assert best_time == 3 and minimum_squared == 52
answers.append(f"{float(s.sqrt(minimum_squared)):.1f}".replace(".", ","))
f = x**3-3*m*x+2
roots = s.solve(s.diff(f, x), x)
extreme_points = [s.Matrix([r, f.subs(x, r)]) for r in roots]
delta = extreme_points[0]-extreme_points[1]
equation = s.factor(delta.dot(delta)-(2*s.sqrt(34))**2)
parameters = [r for r in s.solve(equation, m) if r.is_real and bool(r > 0)]
assert len(parameters) == 1
answers.append(str(parameters[0]))
cost = 60*(8-x)+100*s.sqrt(x*x+9)
cost_candidates = extrema(cost, x, s.Integer(0), s.Integer(8))
best_cable, best_cost = min(cost_candidates, key=lambda pair: float(pair[1]))
assert best_cable == s.Rational(9, 4) and best_cost == 720
answers.append(str(best_cost))
assert answers == key["III"], (answers, key["III"])
assert all(len(a) <= 4 for a in answers)

source = (BASE / "De_giua_ki_1_01.tex").read_text(encoding="utf-8")
for outside_scope in ("nguyên hàm", "tích phân", "xác suất", "thống kê", "mặt cầu", "phương trình mặt phẳng", "phương trình đường thẳng", "logarit"):
    assert outside_scope not in source.lower(), outside_scope
report = {"status": "passed", "multiple_choice": multiple_choice, "true_false": true_false,
          "short_answers": answers, "checked": {"multiple_choice": 12, "true_false_statements": 16, "short_answers": 6},
          "scope": "Bài 1–8 theo ảnh; ứng dụng đạo hàm và vectơ/tọa độ trong không gian",
          "note": "Kiểm tra toán học bằng SymPy; kiểm tra PDF, bố cục và số trang thực hiện riêng."}
(BASE / "kiem_tra_toan.json").write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, indent=2))
