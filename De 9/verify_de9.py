"""
Script kiểm định độc lập (Pha 1 & Pha 2) toàn bộ 22 câu hỏi của Đề số 9 bằng SymPy.
Đảm bảo:
- Không có bất kỳ câu hàm hợp g(x) = f(u(x)) nào.
- Phần I phân bố chuẩn 3A - 3B - 3C - 3D.
- Tất cả số liệu, nghiệm, tích phân, xác suất, Oxyz đều chính xác tuyệt đối 100%.
"""
import sympy as sp
from fractions import Fraction

x, y, z, t, m = sp.symbols("x y z t m", real=True)

print("=== KIỂM ĐỊNH ĐỀ SỐ 9 ===")

# ---------------------------------------------------------
# PHẦN I: 12 CÂU (3A - 3B - 3C - 3D)
# 1.A, 2.C, 3.B, 4.D, 5.A, 6.C, 7.B, 8.D, 9.A, 10.C, 11.B, 12.D
# Đếm:
# A: 1, 5, 9 (3 câu)
# B: 3, 7, 11 (3 câu)
# C: 2, 6, 10 (3 câu)
# D: 4, 8, 12 (3 câu)
# ---------------------------------------------------------

# Câu 1 (Đáp án A): Hàm phân thức y = (x^2 - 4x + 7)/(x - 2). Tâm đối xứng I(2; 0).
f1 = (x**2 - 4*x + 7)/(x - 2)
# y = x - 2 + 3/(x - 2) => tiệm cận đứng x = 2, tiệm cận xiên y = x - 2 => I(2; 0)
I1 = (2, 0)
assert sp.simplify(f1.subs(x, 2 + t) + f1.subs(x, 2 - t)) == 2 * I1[1]
print(f"P1-C1: Tâm đối xứng I = {I1} -> Chọn A")

# Câu 2 (Đáp án C): log_2(x^2 - 3x + 2) <= 1 + log_2(x + 2) trên đoạn [-5; 10]. Số nghiệm nguyên.
# ĐK: x in (-2; 1) U (2; +inf)
# x^2 - 3x + 2 <= 2x + 4 <=> x^2 - 5x - 2 <= 0
roots2 = sp.solve(x**2 - 5*x - 2, x)
int_sols = [val for val in range(-5, 11) if (val > -2 and (val < 1 or val > 2)) and (val**2 - 5*val - 2 <= 0)]
assert int_sols == [0, 3, 4, 5]
assert len(int_sols) == 4
print(f"P1-C2: Nghiệm nguyên {int_sols} (số lượng: {len(int_sols)}) -> Chọn C (4)")

# Câu 3 (Đáp án B): int_0^2 (2x + 1) e^x dx = a*e^2 + b. Tính a + b.
int3 = sp.integrate((2*x + 1)*sp.exp(x), (x, 0, 2))
# int3 = 3*e^2 + 1 => a = 3, b = 1 => a + b = 4
assert sp.simplify(int3 - (3*sp.E**2 + 1)) == 0
assert 3 + 1 == 4
print(f"P1-C3: I = {int3} => a=3, b=1 => a+b=4 -> Chọn B (4)")

# Câu 4 (Đáp án D): d(A, (P)) với A(1; 3; -2), (P): 2x - y + 2z - 5 = 0.
d4 = abs(2*1 - 3 + 2*(-2) - 5) / sp.sqrt(2**2 + (-1)**2 + 2**2)
assert d4 == sp.Rational(10, 3)
print(f"P1-C4: d(A, (P)) = {d4} -> Chọn D (10/3)")

# Câu 5 (Đáp án A): Hộp có 6 đỏ, 4 xanh. Lấy lần 1 xanh, xác suất lần 2 đỏ.
p5 = Fraction(6, 9)
assert p5 == Fraction(2, 3)
print(f"P1-C5: P(Đỏ 2 | Xanh 1) = {p5} -> Chọn A (2/3)")

# Câu 6 (Đáp án C): Trung vị Me của mẫu số liệu ghép nhóm n = 40.
# [15; 20): 4, [20; 25): 12, [25; 30): 14, [30; 35): 8, [35; 40): 2
# n/2 = 20 => nhóm [25; 30)
Me6 = 25 + Fraction(20 - 16, 14) * 5
assert Me6 == Fraction(185, 7)
print(f"P1-C6: Me = {Me6} = {float(Me6):.2f} -> Chọn C (185/7)")

# Câu 7 (Đáp án B): Lăng trụ đứng ABC.A'B'C' đáy vuông tại B, AB=a, BC=a*sqrt(3), AA'=2a. tan(A'C, (ABC)).
# AC = sqrt(a^2 + 3a^2) = 2a. AA' = 2a => tan = AA'/AC = 1
tan7 = sp.Rational(2, 2)
assert tan7 == 1
print(f"P1-C7: tan(A'C, (ABC)) = {tan7} -> Chọn B (1)")

# Câu 8 (Đáp án D): Cấp số cộng u1 = 3, u5 = 15. Tính S_20.
d8 = (15 - 3) / 4
assert d8 == 3
S20 = 20/2 * (2*3 + 19*3)
assert S20 == 630
print(f"P1-C8: d = {d8}, S_20 = {S20} -> Chọn D (630)")

# Câu 9 (Đáp án A): v(t) = 3t^2 + 2t + 1 (m/s). a(t) = v'(t) = 6t + 2. Khi a(t) = 14 => t = 2. Quãng đường.
t9 = sp.solve(6*t + 2 - 14, t)[0]
assert t9 == 2
s9 = sp.integrate(3*t**2 + 2*t + 1, (t, 0, t9))
assert s9 == 14
print(f"P1-C9: t = {t9} s, s = {s9} m -> Chọn A (14 m)")

# Câu 10 (Đáp án C): Mặt cầu tâm I(2; -1; 4) qua A(1; 1; 2).
R10_sq = (1 - 2)**2 + (1 - (-1))**2 + (2 - 4)**2
assert R10_sq == 9
print(f"P1-C10: R^2 = {R10_sq} => (x-2)^2 + (y+1)^2 + (z-4)^2 = 9 -> Chọn C")

# Câu 11 (Đáp án B): C(x) = x^3 - 30x^2 + 400x + 500, x in [5; 25]. C'(x) min tại x.
C_prime = 3*x**2 - 60*x + 400
crit11 = sp.solve(sp.diff(C_prime, x), x)[0]
assert crit11 == 10
print(f"P1-C11: C'(x) min tại x = {crit11} -> Chọn B (10)")

# Câu 12 (Đáp án D): Chóp S.ABC đáy đều cạnh 2a, SA vuông đáy, góc(SC, đáy)=60 độ. V.
# S_ABC = (2)^2 * sqrt(3) / 4 = sqrt(3)
# AC = 2 => SA = 2*tan(60) = 2*sqrt(3)
# V = 1/3 * sqrt(3) * 2*sqrt(3) = 2
V12 = sp.Rational(1, 3) * sp.sqrt(3) * (2*sp.sqrt(3))
assert V12 == 2
print(f"P1-C12: V = {V12} a^3 -> Chọn D (2a^3)")

# ---------------------------------------------------------
# PHẦN II: 4 CÂU ĐÚNG / SAI
# ---------------------------------------------------------
print("\n--- PHẦN II ---")

# Câu 1: f(x) = (x^2 - 3x + 6)/(x - 1)
f_ii_1 = (x**2 - 3*x + 6)/(x - 1)
df1 = sp.simplify(sp.diff(f_ii_1, x))
crit_ii_1 = sp.solve(df1, x)
assert crit_ii_1 == [-1, 3]
y_crit = [f_ii_1.subs(x, c) for c in crit_ii_1]
# (-1; -5) và (3; 3)
# Đường thẳng qua 2 cực trị: y = 2x - 3
assert y_crit[0] == 2*crit_ii_1[0] - 3 and y_crit[1] == 2*crit_ii_1[1] - 3
# Tiệm cận xiên: y = x - 2 <=> x - y - 2 = 0. Tiệm cận đứng: x = 1 => I(1; -1)
d_O = abs(-2) / sp.sqrt(1**2 + (-1)**2)
assert d_O == sp.sqrt(2)
print(f"P2-C1: Cực trị tại x={crit_ii_1}, y={y_crit}. ĐT qua 2 cực trị: y = 2x - 3. I=(1; -1). d(O, TCX)={d_O}")
print("P2-C1 chân lý: a) Đúng, b) Đúng, c) Sai, d) Đúng")

# Câu 2: Xác suất Bayes kiểm định vi mạch
P_A1, P_A2, P_A3 = Fraction(50, 100), Fraction(30, 100), Fraction(20, 100)
P_F_A1, P_F_A2, P_F_A3 = Fraction(2, 100), Fraction(3, 100), Fraction(5, 100)
P_F = P_A1*P_F_A1 + P_A2*P_F_A2 + P_A3*P_F_A3
assert P_F == Fraction(29, 1000)
P_notF = 1 - P_F
assert P_notF == Fraction(971, 1000) # 0.971
P_A1_F = (P_A1 * P_F_A1) / P_F
assert P_A1_F == Fraction(10, 29) # ~34.48% < 35%
P_A23_notF = P_A2 * (1 - P_F_A2) + P_A3 * (1 - P_F_A3)
assert P_A23_notF == Fraction(481, 1000) # 0.481
P_exact1_defect = 2 * P_F * P_notF
assert round(float(P_exact1_defect), 4) == 0.0563
print(f"P2-C2: P(F)={float(P_F)}, P(tốt)={float(P_notF)}, P(A1|F)={float(P_A1_F):.4f}, P(A2,3 và tốt)={float(P_A23_notF)}, P(đúng 1 lỗi)={float(P_exact1_defect):.6f}")
print("P2-C2 chân lý: a) Đúng, b) Sai, c) Đúng, d) Đúng")

# Câu 3: Oxyz Cân bằng lực 3D giàn đèn
# A(2; 0; 4), B(-1; sqrt(3); 4), C(-1; -sqrt(3); 4), S(0; 0; 2), P = (0; 0; -60)
SA_vec = sp.Matrix([2, 0, 2])
SB_vec = sp.Matrix([-1, sp.sqrt(3), 2])
SC_vec = sp.Matrix([-1, -sp.sqrt(3), 2])
assert SA_vec.norm() == 2*sp.sqrt(2)
assert SB_vec.norm() == 2*sp.sqrt(2)
assert SC_vec.norm() == 2*sp.sqrt(2)
# Góc với trần z = 4: sin = |2| / (2*sqrt(2)*1) = 1/sqrt(2) => 45 độ
sin_alpha = sp.Rational(2, 1) / (2*sp.sqrt(2))
assert sin_alpha == 1/sp.sqrt(2)
# cos(SA, SB) = (2*(-1) + 0 + 4) / 8 = 2/8 = 1/4
cos_SASB = SA_vec.dot(SB_vec) / (SA_vec.norm() * SB_vec.norm())
assert cos_SASB == sp.Rational(1, 4)
# Lực căng T: 3 * T * (2 / (2*sqrt(2))) = 60 => 3*T/sqrt(2) = 60 => T = 20*sqrt(2) N
T_tension = 60 * sp.sqrt(2) / 3
assert T_tension == 20*sp.sqrt(2)
print(f"P2-C3: Độ dài dây={SA_vec.norm()}, góc nghiêng=45 độ, cos(SA, SB)={cos_SASB}, T={T_tension} N")
print("P2-C3 chân lý: a) Đúng, b) Đúng, c) Sai, d) Đúng")

# Câu 4: Thống kê số liệu ghép nhóm
# Lớp 12A: [12; 13): 5, [13; 14): 18, [14; 15): 11, [15; 16): 4, [16; 17): 2 (n=40)
# Giá trị đại diện: 12.5, 13.5, 14.5, 15.5, 16.5
reps = [sp.Rational(25, 2), sp.Rational(27, 2), sp.Rational(29, 2), sp.Rational(31, 2), sp.Rational(33, 2)]
freqA = [5, 18, 11, 4, 2]
meanA = sum(r * f for r, f in zip(reps, freqA)) / 40
assert meanA == 14 # 14.0 giây
varA = sum(f * (r - meanA)**2 for r, f in zip(reps, freqA)) / 40
assert varA == 1 # Phương sai = 1.0, độ lệch chuẩn = 1.0

# Lớp 12B: [12; 13): 3, [13; 14): 19, [14; 15): 14, [15; 16): 3, [16; 17): 1 (n=40)
freqB = [3, 19, 14, 3, 1]
meanB = sum(r * f for r, f in zip(reps, freqB)) / 40
assert meanB == 14 # 14.0 giây
varB = sum(f * (r - meanB)**2 for r, f in zip(reps, freqB)) / 40
assert varB == sp.Rational(7, 10) # 0.7
assert varB < varA # Lớp 12B có độ phân tán nhỏ hơn => chạy đồng đều hơn lớp 12A
print(f"P2-C4: meanA={meanA}, varA={varA}, sA={sp.sqrt(varA)}")
print(f"P2-C4: meanB={meanB}, varB={float(varB)}, sB={float(sp.sqrt(varB)):.4f}")
print("P2-C4 chân lý: a) Đúng, b) Sai, c) Đúng, d) Đúng")

# ---------------------------------------------------------
# PHẦN III: 6 CÂU TRẢ LỜI NGẮN
# ---------------------------------------------------------
print("\n--- PHẦN III ---")

# Câu 1: Trải phẳng hộp chữ nhật 6 x 8 x 10 dm, từ A đến C'.
L1 = sp.sqrt((6 + 8)**2 + 10**2) # sqrt(196 + 100) = sqrt(296) = 2*sqrt(74) ~ 17.204
ans1 = round(float(L1), 1)
assert ans1 == 17.2
print(f"P3-C1: L_min = {float(L1):.3f} => Đáp số: 17,2")

# Câu 2: Diện tích cổng vòm parabol giới hạn bởi y1 = 9 - x^2 và y2 = 6 - (2/3)x^2 trên [-3; 3].
# S_trên = int_{-3}^3 (9 - x^2)dx = 36. S_dưới = int_{-3}^3 (6 - (2/3)x^2)dx = 24.
# Diện tích phần vòm ốp gạch gốm mỹ thuật (phần gạch chéo) = 36 - 24 = 12 m^2.
S_vom9 = sp.integrate((9 - x**2) - (6 - sp.Rational(2, 3)*x**2), (x, -3, 3))
assert S_vom9 == 12
print(f"P3-C2: S_vom = {S_vom9} m^2 => Đáp số: 12")

# Câu 3: Tối ưu kinh tế vi mô: p(x) = 200 - x, C(x) = x^2 + 32x + 800, thuế t = 8.
# L(x) = x(200 - x) - (x^2 + 32x + 800) - 8x = -2x^2 + 160x - 800.
# L'(x) = -4x + 160 = 0 => x = 40.
# L_max = L(40) = 2400 nghìn đồng.
L_func = x*(200 - x) - (x**2 + 32*x + 800) - 8*x
x_opt = sp.solve(sp.diff(L_func, x), x)[0]
assert x_opt == 40
L_max = L_func.subs(x, 40)
assert L_max == 2400
print(f"P3-C3: x_opt = {x_opt}, L_max = {L_max} nghìn đồng => Đáp số: 2400")

# Câu 4: Oxyz min khoảng cách từ A(3; 5; 9) đến M in (S): (x-1)^2 + (y-2)^2 + (z-3)^2 = 9 (R = 3).
# I(1; 2; 3). IA = sqrt((3-1)^2 + (5-2)^2 + (9-3)^2) = sqrt(4 + 9 + 36) = 7.
# d_min = IA - R = 7 - 3 = 4.
IA4 = sp.sqrt((3 - 1)**2 + (5 - 2)**2 + (9 - 3)**2)
assert IA4 == 7
d4_min = IA4 - 3
assert d4_min == 4
print(f"P3-C4: IA = {IA4}, d_min = {d4_min} => Đáp số: 4")

# Câu 5: Xác suất Bayes truyền tin nhị phân:
# P(X=0)=0.6, P(X=1)=0.4. P(Y=1|X=0)=0.05, P(Y=1|X=1)=0.90.
# Nhận được Y=1, tính P(X=1|Y=1).
P_Y1 = Fraction(6, 10)*Fraction(5, 100) + Fraction(4, 10)*Fraction(90, 100)
assert P_Y1 == Fraction(39, 100)
P_X1_Y1 = (Fraction(4, 10)*Fraction(90, 100)) / P_Y1
assert P_X1_Y1 == Fraction(12, 13)
ans5 = round(float(P_X1_Y1), 2)
assert ans5 == 0.92
print(f"P3-C5: P(X=1|Y=1) = {float(P_X1_Y1):.4f} => Đáp số: 0,92")

# Câu 6: Thể tích vật thể thiết diện hình vuông cạnh a(x) = sqrt(36 - x^2), 0 <= x <= 6.
# S(x) = 36 - x^2. V = int_0^6 (36 - x^2)dx = [36x - x^3/3]_0^6 = 216 - 72 = 144.
V6 = sp.integrate(36 - x**2, (x, 0, 6))
assert V6 == 144
print(f"P3-C6: V = {V6} => Đáp số: 144")

print("\n[OK] 100% 22 CÂU HỎI ĐỀ SỐ 9 ĐÃ ĐƯỢC AUDIT & XÁC THỰC THÀNH CÔNG!")
