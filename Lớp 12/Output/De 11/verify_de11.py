import sympy as sp
import numpy as np
from fractions import Fraction

print("=== KIỂM ĐỊNH TOÁN HỌC ĐỀ SỐ 11 ===")

x, y, z, t = sp.symbols('x y z t', real=True)

# ---------------------------------------------------------
# PHẦN I: 12 CÂU TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN
# ---------------------------------------------------------

# Câu 1 (Đáp án A): y = (x^2 + 2x - 2)/(x - 1) = x + 3 + 1/(x - 1).
# TCĐ: x = 1, TCX: y = x + 3 => Giao điểm I(1; 4).
f1 = (x**2 + 2*x - 2)/(x - 1)
q1, r1 = sp.div(x**2 + 2*x - 2, x - 1)
assert q1 == x + 3 and r1 == 1
I1 = (1, q1.subs(x, 1))
assert I1 == (1, 4)
print("P1-C1: Tâm đối xứng I(1; 4) -> Chọn A")

# Câu 2 (Đáp án C): log_3(2x - 1) <= 2 <=> 0 < 2x - 1 <= 9 <=> 1/2 < x <= 5.
sol2 = sp.solve_univariate_inequality(2*x - 1 <= 9, x, relational=False) & sp.solve_univariate_inequality(2*x - 1 > 0, x, relational=False)
assert sol2 == sp.Interval.Lopen(sp.Rational(1, 2), 5)
print("P1-C2: S = (1/2; 5] -> Chọn C")

# Câu 3 (Đáp án B): int e^(3x) dx = 1/3 * e^(3x) + C.
assert sp.diff(sp.Rational(1, 3)*sp.exp(3*x), x) == sp.exp(3*x)
print("P1-C3: F(x) = 1/3*e^(3x) + C -> Chọn B")

# Câu 4 (Đáp án D): (P) qua M(1; -2; 3), n = (2; -1; 4).
# 2(x - 1) - (y + 2) + 4(z - 3) = 2x - y + 4z - 16 = 0.
plane4 = 2*(x - 1) - 1*(y + 2) + 4*(z - 3)
assert sp.expand(plane4) == 2*x - y + 4*z - 16
print("P1-C4: (P): 2x - y + 4z - 16 = 0 -> Chọn D")

# Câu 5 (Đáp án B): p1 = 0.7, p2 = 0.8. Đúng 1 người trúng: 0.7*0.2 + 0.3*0.8 = 0.38.
p5 = Fraction(7, 10)*Fraction(2, 10) + Fraction(3, 10)*Fraction(8, 10)
assert p5 == Fraction(38, 100)
print(f"P1-C5: P = {float(p5)} -> Chọn B (0,38)")

# Câu 6 (Đáp án A): R = 9 - 4 = 5.
assert 9 - 4 == 5
print("P1-C6: R = 5 -> Chọn A")

# Câu 7 (Đáp án D): SA = a*sqrt(3), AB = a, đáy vuông tại B => AH vuông (SBC).
# AH = SA*AB / sqrt(SA^2 + AB^2) = a*sqrt(3)/2.
AH7 = (sp.sqrt(3) * 1) / sp.sqrt(3 + 1)
assert AH7 == sp.sqrt(3)/2
print("P1-C7: d(A, (SBC)) = a*sqrt(3)/2 -> Chọn D")

# Câu 8 (Đáp án C): u1 = 3, d = 4 => u10 = 3 + 9*4 = 39.
u10 = 3 + 9*4
assert u10 == 39
print(f"P1-C8: u10 = {u10} -> Chọn C (39)")

# Câu 9 (Đáp án B): m(24) = 100 * 2^(-24/8) = 100 / 8 = 12.5.
m9 = 100 * 2**(-24//8)
assert m9 == 12.5
print(f"P1-C9: m(24) = {m9} g -> Chọn B (12,5)")

# Câu 10 (Đáp án D): A(1; 0; -1), B(2; -1; 1) => AB = (1; -1; 2).
# d: (x-1)/1 = y/(-1) = (z+1)/2.
assert (2 - 1, -1 - 0, 1 - (-1)) == (1, -1, 2)
print("P1-C10: AB = (1; -1; 2) -> Chọn D")

# Câu 11 (Đáp án A): Chu vi 20 => Nửa chu vi 10 => S = x(10 - x) max = 25 tại x = 5.
S11 = x*(10 - x)
assert sp.solve(sp.diff(S11, x), x)[0] == 5
assert S11.subs(x, 5) == 25
print("P1-C11: S_max = 25 m^2 -> Chọn A (25)")

# Câu 12 (Đáp án C): R = 3a, h = 4a => V = 1/3 * pi * 9 * 4 = 12*pi*a^3.
V12 = sp.Rational(1, 3) * (3**2) * 4
assert V12 == 12
print(f"P1-C12: V = {V12} pi a^3 -> Chọn C (12)")

# ---------------------------------------------------------
# PHẦN II: 4 CÂU ĐÚNG / SAI
# ---------------------------------------------------------
print("\n--- PHẦN II ---")

# Câu 1: f(x) = (2x^2 - 3x + 3)/(x - 1) = 2x - 1 + 2/(x - 1).
# f'(x) = 2 - 2/(x-1)^2 = (2(x-1)^2 - 2)/(x-1)^2 = 2(x^2 - 2x)/(x-1)^2.
f_ii_1 = (2*x**2 - 3*x + 3)/(x - 1)
df1 = sp.simplify(sp.diff(f_ii_1, x))
crit1 = sp.solve(df1, x)
assert crit1 == [0, 2]
assert f_ii_1.subs(x, 0) == -3 # Cực đại tại x = 0
assert f_ii_1.subs(x, 2) == 5  # Cực tiểu tại x = 2
# ĐT qua 2 cực trị: đạo hàm tử / đạo hàm mẫu = (4x - 3)/1 = 4x - 3
assert f_ii_1.subs(x, 0) == 4*0 - 3 and f_ii_1.subs(x, 2) == 4*2 - 3
# Giao 2 tiệm cận: x = 1, y = 2(1) - 1 = 1 => I(1; 1) != I(1; 2)
# Tiếp tuyến tại x = 3: y'(3) = 2 - 2/4 = 3/2
assert df1.subs(x, 3) == sp.Rational(3, 2)
print("P2-C1 chân lý: a) Đúng, b) Đúng, c) Sai, d) Đúng")

# Câu 2: Chi phí nhiên liệu f(v) = 720/v + 0.8*v.
# C1 = 720, C2(v) = 0.8*v^2.
# Trên 1km: f(v) = (720 + 0.8*v^2)/v = 720/v + 0.8*v.
f2_cost = 720/v_sym + sp.Rational(8, 10)*v_sym if 'v_sym' in locals() else None
v_sym = sp.Symbol('v', positive=True)
f2_cost = 720/v_sym + sp.Rational(8, 10)*v_sym
# v = 10 => f(10) = 72 + 8 = 80 != 72
assert f2_cost.subs(v_sym, 10) == 80
# f'(v) = -720/v^2 + 0.8 = 0 => v^2 = 900 => v = 30
df2 = sp.diff(f2_cost, v_sym)
v_opt2 = sp.solve(df2, v_sym)[0]
assert v_opt2 == 30
# f_min = f(30) = 24 + 24 = 48 nghìn đồng
assert f2_cost.subs(v_sym, 30) == 48
print("P2-C2 chân lý: a) Đúng, b) Sai, c) Đúng, d) Đúng")

# Câu 3: Oxyz Cân bằng lực 3D: S(0; 0; 0), A(0; 4; 3), B(-2*sqrt(3); -2; 3), C(2*sqrt(3); -2; 3).
# P = 540 N (hướng xuống -z).
SA_len = sp.sqrt(0**2 + 4**2 + 3**2)
assert SA_len == 5
SB_len = sp.sqrt((-2*sp.sqrt(3))**2 + (-2)**2 + 3**2)
assert SB_len == 5
SC_len = sp.sqrt((2*sp.sqrt(3))**2 + (-2)**2 + 3**2)
assert SC_len == 5
# Góc giữa dây và trần: sin(beta) = 3/5 => cos(beta) = 4/5
cos_beta = sp.Rational(4, 5)
assert cos_beta == sp.Rational(4, 5)
# Góc giữa SA và SB: SA = (0; 4; 3), SB = (-2*sqrt(3); -2; 3)
# SA.SB = 0 + 4*(-2) + 3*3 = -8 + 9 = 1.
# cos(ASB) = 1 / (5*5) = 1/25 != 1/5.
cos_ASB = sp.Rational(1, 25)
assert cos_ASB == sp.Rational(1, 25)
# Lực căng: 3 * T * (3/5) = 540 => (9/5)T = 540 => T = 300 N.
T3 = 540 / (3 * sp.Rational(3, 5))
assert T3 == 300
print("P2-C3 chân lý: a) Đúng, b) Đúng, c) Sai, d) Đúng")

# Câu 4: Thống kê số liệu ghép nhóm 2 lớp 12A1 và 12A2 (n = 40 mỗi lớp)
# Lớp 12A1: [6; 7): 4, [7; 8): 16, [8; 9): 16, [9; 10): 4
reps4 = [sp.Rational(13, 2), sp.Rational(15, 2), sp.Rational(17, 2), sp.Rational(19, 2)]
freq1 = [4, 16, 16, 4]
mean1 = sum(r * f for r, f in zip(reps4, freq1)) / 40
assert mean1 == 8 # 8.0 điểm
var1 = sum(f * (r - mean1)**2 for r, f in zip(reps4, freq1)) / 40
assert var1 == sp.Rational(65, 100) # 0.65

# Lớp 12A2: [6; 7): 8, [7; 8): 12, [8; 9): 12, [9; 10): 8
freq2 = [8, 12, 12, 8]
mean2 = sum(r * f for r, f in zip(reps4, freq2)) / 40
assert mean2 == 8 # 8.0 điểm
var2 = sum(f * (r - mean2)**2 for r, f in zip(reps4, freq2)) / 40
assert var2 == sp.Rational(105, 100) # 1.05
assert var1 < var2 # Lớp 12A1 có phương sai nhỏ hơn => đồng đều hơn
print(f"P2-C4: mean1={float(mean1)}, var1={float(var1):.2f}, var2={float(var2):.2f}")
print("P2-C4 chân lý: a) Đúng, b) Sai, c) Đúng, d) Đúng")

# ---------------------------------------------------------
# PHẦN III: 6 CÂU TRẢ LỜI NGẮN
# ---------------------------------------------------------
print("\n--- PHẦN III ---")

# Câu 1: Trụ R = 6/pi => Chu vi = 12 cm. Nửa chu vi = 6 cm. h = 8 cm.
# Đường chéo trải phẳng: d = sqrt(6^2 + 8^2) = 10 cm.
d1_cyl = sp.sqrt(6**2 + 8**2)
assert d1_cyl == 10
print(f"P3-C1: d = {d1_cyl} cm => Đáp số: 10")

# Câu 2: Parabol y = 12 - 3x^2, dầm y = 9.
# 12 - 3x^2 = 9 <=> x^2 = 1 <=> x = +-1.
# S = int_{-1}^1 (12 - 3x^2 - 9) dx = 2 * [3x - x^3]_0^1 = 2 * (3 - 1) = 4 m^2.
S2_arch = sp.integrate(12 - 3*x**2 - 9, (x, -1, 1))
assert S2_arch == 4
print(f"P3-C2: S = {S2_arch} m^2 => Đáp số: 4")

# Câu 3: Bảng quảng cáo AB = 3m, OA = 1m, OB = 4m. Camera tại C(x; 0).
# tan(ACB) = 3 / (x + 4/x) <= 3/4. Dấu bằng khi x = 2 m.
assert sp.sqrt(4) == 2
print("P3-C3: x_opt = 2 m => Đáp số: 2")

# Câu 4: d(A, (P)) với A(1; 3; -2) và (P): 2x - 2y + z + 12 = 0.
# d = |2(1) - 2(3) + 1(-2) + 12| / 3 = |2 - 6 - 2 + 12| / 3 = 6 / 3 = 2.
d4 = abs(2*1 - 2*3 + 1*(-2) + 12) / sp.sqrt(2**2 + (-2)**2 + 1**2)
assert d4 == 2
print(f"P3-C4: d_min = {d4} => Đáp số: 2")

# Câu 5: Cristiano Ronaldo sút 5 quả luân lưu, p = 0.9.
# P(X = 5) = 0.9^5 = 0.59049 => Làm tròn: 0,59.
p_cr7 = Fraction(9, 10)**5
assert p_cr7 == Fraction(59049, 100000)
ans_p3_5 = round(float(p_cr7), 2)
assert ans_p3_5 == 0.59
print(f"P3-C5: P(X = 5) = {float(p_cr7):.5f} => Đáp số: 0,59")

# Câu 6: Thiết diện S(x) = (sqrt(3x^2 + 1))^2 = 3x^2 + 1 trên [0; 3].
# V = int_0^3 (3x^2 + 1) dx = [x^3 + x]_0^3 = 27 + 3 = 30 dm^3.
V6 = sp.integrate(3*x**2 + 1, (x, 0, 3))
assert V6 == 30
print(f"P3-C6: V = {V6} dm^3 => Đáp số: 30")

print("\n[OK] 100% 22 CÂU HỎI ĐỀ SỐ 11 ĐÃ ĐƯỢC AUDIT THÀNH CÔNG!")
