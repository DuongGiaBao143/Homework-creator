"""Kiểm độc lập kết quả toán học của đề 01; không đưa lời giải vào bản đáp án."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import re

import sympy as s

folder = Path(__file__).resolve().parent
tex = (folder / "De 1.tex").read_text(encoding="utf-8")
x, y, m = s.symbols("x y m", real=True)
results = {}


def choice(number, truths):
    assert sum(bool(value) for value in truths) == 1, (number, truths)
    results[f"I.{number}"] = "ABCD"[list(map(bool, truths)).index(True)]


def same(a, b):
    return s.simplify(a - b) == 0


alpha = s.pi * s.Rational(2, 3)
choice(1, [s.sin(alpha) < 0, s.cos(alpha) < 0, s.tan(alpha) > 0, s.cot(alpha) > 0])
# Câu hỏi/cầu khiến/cảm thán không phải mệnh đề; phương án D có giá trị chân lý.
choice(2, [False, False, False, s.isprime(17)])
choice(3, [s.Poly(expr, x, y).total_degree() == 1 for expr in (2*x-3*y-5, x*x+y-1, x*y-4, x+y*y)])
choice(4, [False, frozenset({1}) in {1, 2, 3}, {1} < {1, 2, 3}, 4 in {1, 2, 3}])
a, b, c = s.Integer(5), s.Integer(6), s.Integer(8)
cosA = (b*b+c*c-a*a)/(2*b*c)
sinA = s.sqrt(1-cosA*cosA)
choice(5, [same(a*a, value) for value in (b*b+c*c-2*b*c*cosA, b*b+c*c+2*b*c*cosA, b*b+c*c-2*b*c*sinA, b*b+c*c-2*a*b*cosA)])
choice(6, [px+2*py > 4 for px, py in ((0, 2), (2, 1), (1, 1), (1, 2))])
choice(7, [False, x in (x+2-5).free_symbols, False, False])
choice(8, [same(s.sin(5*s.pi/6), value) for value in (-s.Rational(1, 2), s.sqrt(3)/2, s.Rational(1, 2), -s.sqrt(3)/2)])
systems = ((x*x+y-4, x-y-1), (x+y-4, 2*x-y-1), (x*y-4, x+y-1), (x+y-4, x+y*y-1))
choice(9, [all(s.Poly(expr, x, y).total_degree() == 1 for expr in system) for system in systems])
subsets = [subset for size in range(4) for subset in combinations((2, 5, 8), size)]
choice(10, [len(subsets) == value for value in (8, 3, 6, 9)])
p = (a+b+c)/2
area = s.sqrt(p*(p-a)*(p-b)*(p-c))
cosC = (a*a+b*b-c*c)/(2*a*b)
sinC = s.sqrt(1-cosC*cosC)
choice(11, [same(area, value) for value in (a*b*cosC/2, a*b*sinC, b*c*sinC/2, a*b*sinC/2)])
choice(12, [px >= 0 and py >= 0 and px+py <= 4 and px+2*py >= 4 for px, py in ((-1, 3), (3, 2), (1, 2), (0, 1))])
key = "BDACADBCBADC"
assert "".join(results[f"I.{i}"] for i in range(1, 13)) == key
assert Counter(key) == dict.fromkeys("ABCD", 3)
assert "Đáp án&" + "&".join(key) + r"\\\hline" in tex

# Hai giới hạn độc lập; kiểm tất cả phương án nguyên có thể đáp ứng giới hạn chi phí.
feasible = lambda px, py: px >= 0 and py >= 0 and 40*px+30*py <= 600 and 2*px+3*py <= 42
equivalent = all(feasible(px, py) == (px >= 0 and py >= 0 and 4*px+3*py <= 60 and 2*px+3*py <= 42)
                 for px in range(-1, 22) for py in range(-1, 22))
max_fruit = max(py for py in range(21) if feasible(9, py))
tf1 = [40*9+30*8 == 600, feasible(9, 9), equivalent, max_fruit == 7]
assert tf1 == [True, False, True, False] and max_fruit == 8
results["II.1"] = tf1
A, B = s.Interval(-2, 4, right_open=True), s.Interval(1, 6, left_open=True)
tf2 = [bool(A.contains(-2)), bool(s.FiniteSet(4).is_subset(A)), A.intersect(B) == s.Interval(1, 4, right_open=True), B-A == s.Interval(4, 6)]
assert tf2 == [True, False, False, True]
results["II.2"] = tf2

cos_alpha = -s.Rational(3, 5)
sin_alpha = s.sqrt(1-cos_alpha*cos_alpha)
short1 = s.simplify(7*(sin_alpha+2*cos_alpha)/(sin_alpha-cos_alpha))
assert short1 == -2 and sin_alpha-cos_alpha != 0
results["III.1"] = short1
A = {n for n in range(-50, 51) if -3 <= 2*n+1 < 12}
B = {n for n in range(-50, 51) if n*n <= 9}
assert A == set(range(-2, 6)) and B == set(range(-3, 4)) and len(A | B) == 9
results["III.2"] = len(A | B)
distance, above_instrument = s.symbols("d h", positive=True)
solution = s.solve([above_instrument-distance*s.tan(s.pi/3), above_instrument-(distance+40)*s.tan(s.pi/6)], (distance, above_instrument))
height = s.simplify(solution[above_instrument]+s.Rational(3, 2))
assert solution[distance] == 20 and height == 20*s.sqrt(3)+s.Rational(3, 2)
assert round(float(height), 1) == 36.1
results["III.3"] = round(float(height), 1)


def vertices(inequalities):
    points = set()
    for first, second in combinations(inequalities, 2):
        for point in s.solve([first, second], (x, y), dict=True):
            if x in point and y in point and all(expr.subs(point) <= 0 for expr in inequalities):
                points.add((point[x], point[y]))
    return points


D = vertices([-x, -y, x+y-4, 2*x+y-6])
assert D == {(0, 0), (3, 0), (2, 2), (0, 4)}
parameter_range = s.reduce_inequalities([(m-1)*px+2*py <= 8 for px, py in D], m)
assert parameter_range == (m <= 3)
assert all(2*px+2*py <= 8 for px, py in D)
results["III.4"] = 3

A, B = s.Interval(-s.oo, 3), s.Interval(-1, 5, right_open=True)
written1 = [A.intersect(B), A.union(B), A-B]
assert written1 == [s.Interval(-1, 3), s.Interval(-s.oo, 5, right_open=True), s.Interval(-s.oo, -1, right_open=True)]
results["IV.1"] = written1
t = s.symbols("t", real=True)
assert s.trigsimp((1-s.cos(t)**2)/(s.sin(t)*s.cos(t))-s.tan(t)) == 0
sin_alpha = s.Rational(5, 13)
cos_alpha = -s.sqrt(1-sin_alpha**2)
assert cos_alpha == -s.Rational(12, 13) and sin_alpha/cos_alpha == -s.Rational(5, 12)
results["IV.2"] = -s.Rational(5, 12)

diagonal = s.sqrt(80**2+60**2)
triangle_ADC = diagonal**2*s.sin(s.pi/3)*s.sin(s.pi/4)/(2*s.sin(5*s.pi/12))
area_total = s.simplify(80*60/2+triangle_ADC)
# Kiểm chéo bằng tọa độ và công thức diện tích đa giác, không dùng lại công thức sin.
d_x = s.simplify(100/(s.sqrt(3)+1))
land = [(0, 0), (64, -48), (100, 0), (d_x, s.sqrt(3)*d_x)]
shoelace = s.simplify(abs(sum(px*qy-py*qx for (px, py), (qx, qy) in zip(land, land[1:]+land[:1])))/2)
assert diagonal == 100 and same(shoelace, area_total)
assert same(area_total, 9900-2500*s.sqrt(3)) and round(float(area_total)) == 5570
results["IV.3"] = 5570

region = vertices([-x, -y, 2*x+y-20, x+2*y-16])
assert region == {(0, 0), (10, 0), (8, 4), (0, 8)}
gains = {(px, py): 300000*px+250000*py for px, py in region}
assert max(gains, key=gains.get) == (8, 4) and gains[(8, 4)] == 3400000
integer_gains = {(px, py): 300000*px+250000*py for px in range(11) for py in range(9)
                 if 2*px+py <= 20 and px+2*py <= 16}
assert [point for point, value in integer_gains.items() if value == max(integer_gains.values())] == [(8, 4)]
results["IV.4"] = "8 lô A; 4 lô B; 3.400.000 đồng"
assert len(results) == 22
assert tex.count(r"\answerbox") == 5  # Định nghĩa lệnh và bốn chỗ điền đáp số.
assert "HƯỚNG DẪN GIẢI" not in tex
print("[OK] 22 câu và 8 ý đúng/sai; 3A-3B-3C-3D; đầu mút, dấu lượng giác, tham số, hình học và tối ưu nguyên.")
for question, result in results.items():
    print(question, result)
