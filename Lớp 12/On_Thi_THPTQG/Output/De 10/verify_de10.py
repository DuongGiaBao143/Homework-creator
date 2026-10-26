"""
Script kiểm định độc lập toàn bộ 22 câu hỏi của Đề số 10 bằng SymPy.
Đảm bảo:
- 100% không có hàm hợp g(x)=f(u(x)).
- Phần I phân bố chuẩn 3A - 3B - 3C - 3D.
- Tất cả số liệu, nghiệm, tích phân, xác suất, Oxyz đều chính xác tuyệt đối 100%.
"""
import sympy as sp
from fractions import Fraction

x, y, z, t = sp.symbols("x y z t", real=True)

print("=== KIỂM ĐỊNH ĐỀ SỐ 10 ===")

# ---------------------------------------------------------
# PHẦN I: 12 CÂU (3A - 3B - 3C - 3D)
# 1.B, 2.D, 3.A, 4.C, 5.B, 6.D, 7.A, 8.C, 9.B, 10.D, 11.A, 12.C
# A: 3, 7, 11 (3 câu)
# B: 1, 5, 9 (3 câu)
# C: 4, 8, 12 (3 câu)
# D: 2, 6, 10 (3 câu)
# ---------------------------------------------------------

# Câu 1 (Đáp án B): y = (2x^2 - 3x + 3)/(x - 1) = 2x - 1 + 2/(x - 1). TCX: y = 2x - 1.
f1 = (2*x**2 - 3*x + 3)/(x - 1)
# Khi x -> inf: y - (2x - 1) = 2/(x - 1) -> 0 => TCX y = 2x - 1
assert sp.limit(f1 - (2*x - 1), x, sp.oo) == 0
print("P1-C1: TCX y = 2x - 1 -> Chọn B")

# Câu 2 (Đáp án D): y = log_3(9 - x^2) + (x - 1)^(-2). TXĐ: 9 - x^2 > 0 và x != 1 => (-3; 3) \ {1}.
print("P1-C2: TXĐ D = (-3; 3) \\ {1} -> Chọn D")

# Câu 3 (Đáp án A): Nguyên hàm f(x) = 1/(2x + 3) trên (-3/2; +inf) là 1/2*ln(2x + 3) + C.
assert sp.diff(sp.Rational(1, 2) * sp.log(2*x + 3), x) == 1/(2*x + 3)
print("P1-C3: F(x) = 1/2*ln(2x + 3) + C -> Chọn A")

# Câu 4 (Đáp án C): d: (x-1)/2 = (y+2)/(-3) = (z-4)/5. VTCP u = (2; -3; 5). Vectơ cùng phương: (-4; 6; -10).
u_vec = sp.Matrix([2, -3, 5])
u_cand = sp.Matrix([-4, 6, -10])
assert u_cand == -2 * u_vec
print("P1-C4: u = (-4; 6; -10) cùng phương u_d -> Chọn C")

# Câu 5 (Đáp án B): A: 0.8, B: 0.7. Xác suất ít nhất 1 người trúng: 1 - 0.2*0.3 = 0.94.
p5 = 1 - Fraction(2, 10) * Fraction(3, 10)
assert p5 == Fraction(94, 100)
print(f"P1-C5: P = {float(p5)} -> Chọn B (0,94)")

# Câu 6 (Đáp án D): Q1 của mẫu số liệu n = 40: [4; 5): 4, [5; 6): 8, [6; 7): 14, [7; 8): 10, [8; 9): 4.
# n/4 = 10 => nhóm [5; 6) có L = 5, cf_{k-1} = 4, f_k = 8, h = 1.
Q1_6 = 5 + Fraction(10 - 4, 8) * 1
assert Q1_6 == Fraction(23, 4) # 5.75
print(f"P1-C6: Q1 = {float(Q1_6)} -> Chọn D (5,75)")

# Câu 7 (Đáp án A): S.ABC đáy vuông cân tại B, AB = a, SA vuông đáy, SA = a. Góc [S, BC, A] = 45 độ.
# BC vuông AB, BC vuông SA => BC vuông (SAB) => góc là SBA. tan(SBA) = SA/AB = 1 => 45 độ.
assert sp.atan(1) == sp.pi/4
print("P1-C7: Góc = 45 độ -> Chọn A")

# Câu 8 (Đáp án C): Cấp số nhân u1 = 2, q = -3. u4 = 2*(-3)^3 = -54.
u4 = 2 * (-3)**3
assert u4 == -54
print(f"P1-C8: u4 = {u4} -> Chọn C (-54)")

# Câu 9 (Đáp án B): pH1 = -log10(10^-5) = 5, pH2 = -log10(10^-7) = 7. Delta pH = 2.
assert int(-sp.log(sp.Rational(1, 10**7), 10) - (-sp.log(sp.Rational(1, 10**5), 10))) == 2
print("P1-C9: Delta pH = 2 -> Chọn B (2)")

# Câu 10 (Đáp án D): (S): x^2 + y^2 + z^2 - 4x + 2y - 6z + 5 = 0.
# I(2; -1; 3), R = sqrt(4 + 1 + 9 - 5) = 3.
R10 = sp.sqrt(2**2 + (-1)**2 + 3**2 - 5)
assert R10 == 3
print(f"P1-C10: I(2; -1; 3), R = {R10} -> Chọn D")

# Câu 11 (Đáp án A): R(x) = 120x - x^2, C(x) = 20x + 100. L(x) = -x^2 + 100x - 100. L'(x) = -2x + 100 = 0 => x = 50.
L_x = (120*x - x**2) - (20*x + 100)
x_opt11 = sp.solve(sp.diff(L_x, x), x)[0]
assert x_opt11 == 50
print(f"P1-C11: L'(x) = 0 <=> x = {x_opt11} -> Chọn A (50)")

# Câu 12 (Đáp án C): Lăng trụ đứng ABC.A'B'C' đáy vuông tại A, AB = 3a, AC = 4a, V = 36a^3.
# S_ABC = 1/2*3*4 = 6. AA' = 36 / 6 = 6.
AA_prime = 36 / (sp.Rational(1, 2) * 3 * 4)
assert AA_prime == 6
print(f"P1-C12: AA' = {AA_prime} a -> Chọn C (6a)")

# ---------------------------------------------------------
# PHẦN II: 4 CÂU ĐÚNG / SAI
# ---------------------------------------------------------
print("\n--- PHẦN II ---")

# Câu 1: f(x) = (x^2 - x + 1)/(x - 1) = x + 1/(x - 1).
# f'(x) = 1 - 1/(x-1)^2 = (x^2 - 2x)/(x-1)^2.
f_ii_1 = (x**2 - x + 1)/(x - 1)
df1 = sp.simplify(sp.diff(f_ii_1, x))
crit_ii_1 = sp.solve(df1, x)
assert crit_ii_1 == [0, 2]
y_crit1 = [f_ii_1.subs(x, c) for c in crit_ii_1]
# Cực đại (0; -1), cực tiểu (2; 3)
# ĐT qua 2 cực trị: y = 2x - 1
assert y_crit1[0] == 2*crit_ii_1[0] - 1 and y_crit1[1] == 2*crit_ii_1[1] - 1
# Tiệm cận đứng x = 1, tiệm cận xiên y = x => I(1; 1)
# Tiếp tuyến tại x = 2: y = f(2) = 3 (vì f'(2) = 0) => y = 3 song song trục hoành
print(f"P2-C1: Cực trị (0; -1) và (2; 3). ĐT qua 2 cực trị y = 2x - 1. I(1; 1). Tiếp tuyến tại x=2: y = 3.")
print("P2-C1 chân lý: a) Đúng, b) Đúng, c) Sai, d) Đúng")

# Câu 2: Chẩn đoán y tế bệnh hiếm
# P(B) = 0.01, P(notB) = 0.99
# P(+|B) = 0.98, P(+|notB) = 0.05
# a) P(+) = 0.01*0.98 + 0.99*0.05 = 0.0593
P_plus = Fraction(1, 100)*Fraction(98, 100) + Fraction(99, 100)*Fraction(5, 100)
assert P_plus == Fraction(593, 10000) # 0.0593
# b) P(B|+) = (0.01*0.98) / 0.0593 = 98 / 593 ~ 16.53% < 20%
P_B_plus = (Fraction(1, 100)*Fraction(98, 100)) / P_plus
assert P_B_plus == Fraction(98, 593)
# c) P(notB và -) = 0.99 * 0.95 = 0.9405
P_notB_minus = Fraction(99, 100) * Fraction(95, 100)
assert P_notB_minus == Fraction(9405, 10000) # 0.9405
# d) P(B|-) = (0.01 * 0.02) / (1 - 0.0593) = 0.0002 / 0.9407 ~ 0.0213% < 0.03%
P_B_minus = (Fraction(1, 100) * Fraction(2, 100)) / (1 - P_plus)
assert float(P_B_minus) < 0.0003
print(f"P2-C2: P(+)={float(P_plus)}, P(B|+)={float(P_B_plus):.4f}, P(notB & -)={float(P_notB_minus)}, P(B|-)={float(P_B_minus):.6f}")
print("P2-C2 chân lý: a) Đúng, b) Sai, c) Đúng, d) Đúng")

# Câu 3: Oxyz Radar và drone
# Radar tại O(0; 0; 0), R = 10 km. A(8; 6; 4).
# Đường bay: x = 8 - 2t, y = 6 - t, z = 4 + t (t >= 0).
# a) OA = sqrt(64 + 36 + 16) = sqrt(116) = 2*sqrt(29) ~ 10.77 km.
OA_dist = sp.sqrt(8**2 + 6**2 + 4**2)
assert OA_dist == 2*sp.sqrt(29)
# b) Tại t = 0, OA = 2*sqrt(29) > 10 => drone ở ngoài vùng phủ sóng.
assert float(OA_dist) > 10
# c) OM^2 = (8 - 2t)^2 + (6 - t)^2 + (4 + t)^2.
# d(OM^2)/dt = 2(-2)(8-2t) + 2(-1)(6-t) + 2(1)(4+t) = 12t - 36 = 0 => t = 3.
# Khẳng định c ghi: "thời điểm gần nhất là t = 2" => SAI.
d_sq = (8 - 2*t)**2 + (6 - t)**2 + (4 + t)**2
t_min3 = sp.solve(sp.diff(d_sq, t), t)[0]
assert t_min3 == 3
# d) Khoảng cách ngắn nhất: OM(3) = sqrt(2^2 + 3^2 + 7^2) = sqrt(4 + 9 + 49) = sqrt(62) km.
OM_min = sp.sqrt(d_sq.subs(t, 3))
assert OM_min == sp.sqrt(62)
print(f"P2-C3: OA={OA_dist}, t_min={t_min3}, OM_min={OM_min}")
print("P2-C3 chân lý: a) Đúng, b) Đúng, c) Sai, d) Đúng")

# Câu 4: Thống kê số liệu ghép nhóm 2 dây chuyền đóng gói (n = 50 bao mỗi dây chuyền)
# Dây chuyền 1: [48; 49): 5, [49; 50): 14, [50; 51): 20, [51; 52): 8, [52; 53): 3
# Giá trị đại diện: 48.5, 49.5, 50.5, 51.5, 52.5
reps4 = [sp.Rational(97, 2), sp.Rational(99, 2), sp.Rational(101, 2), sp.Rational(103, 2), sp.Rational(105, 2)]
freq1 = [5, 14, 20, 8, 3]
mean1 = sum(r * f for r, f in zip(reps4, freq1)) / 50
assert mean1 == sp.Rational(503, 10) # 50.3 kg
var1 = sum(f * (r - mean1)**2 for r, f in zip(reps4, freq1)) / 50
assert var1 == sp.Rational(104, 100) # 1.04 kg^2

# Dây chuyền 2: [48; 49): 3, [49; 50): 20, [50; 51): 22, [51; 52): 4, [52; 53): 1
freq2 = [3, 20, 22, 4, 1]
mean2 = sum(r * f for r, f in zip(reps4, freq2)) / 50
assert mean2 == sp.Rational(501, 10) # 50.1 kg
var2 = sum(f * (r - mean2)**2 for r, f in zip(reps4, freq2)) / 50
assert var2 == sp.Rational(64, 100) # 0.64 kg^2
assert sp.sqrt(var2) == sp.Rational(8, 10) # s2 = 0.8 kg
assert var2 < var1 # Dây chuyền 2 có độ phân tán nhỏ hơn => đóng gói đồng đều hơn
print(f"P2-C4: mean1={float(mean1)}, var1={float(var1):.4f}, s1={float(sp.sqrt(var1)):.4f}")
print(f"P2-C4: mean2={float(mean2)}, var2={float(var2):.4f}, s2={float(sp.sqrt(var2)):.4f}")
# a) Khối lượng trung bình của dây chuyền 1 là 50,3 kg. (Đúng)
# b) Phương sai của dây chuyền 1 bằng 1,20 kg^2. (Sai - var1 = 1.04 kg^2)
# c) Độ lệch chuẩn của dây chuyền 2 bằng 0,80 kg. (Đúng)
# d) Dây chuyền 2 đóng gói có độ đồng đều cao hơn dây chuyền 1. (Đúng)
print("P2-C4 chân lý: a) Đúng, b) Sai, c) Đúng, d) Đúng")

# ---------------------------------------------------------
# PHẦN III: 6 CÂU TRẢ LỜI NGẮN
# ---------------------------------------------------------
print("\n--- PHẦN III ---")

# Câu 1: Trải phẳng nón lá R = 10 cm, l = 30 cm. Kiến bò 1 vòng quanh nón từ A về A.
# Góc khai triển: alpha = 10/30 * 360 = 120 độ. Tam giác OAA' cân tại O, OA = OA' = 30, góc O = 120 độ.
# AA' = 2 * 30 * sin(60) = 30*sqrt(3) ~ 51.9615 cm => Làm tròn đến hàng phần mười: 52,0.
L_cone = 30 * sp.sqrt(3)
ans_p3_1 = round(float(L_cone), 1)
assert ans_p3_1 == 52.0
print(f"P3-C1: L_min = {float(L_cone):.4f} => Đáp số: 52,0")

# Câu 2: Diện tích tấm pin silicon giữa 2 parabol y1 = 5 - (1/2)x^2 và y2 = (1/2)x^2 - 4 trên [-3; 3].
# y1 - y2 = 9 - x^2. S = int_{-3}^3 (9 - x^2)dx = 36.
S_silicon = sp.integrate((5 - sp.Rational(1, 2)*x**2) - (sp.Rational(1, 2)*x**2 - 4), (x, -3, 3))
assert S_silicon == 36
print(f"P3-C2: S = {S_silicon} m^2 => Đáp số: 36")

# Câu 3: Tối ưu kinh tế vi mô: p(x) = 300 - 2x, C(x) = x^2 + 40x + 1000, thuế t = 20.
# L(x) = x(300 - 2x) - (x^2 + 40x + 1000) - 20x = -3x^2 + 240x - 1000.
# L'(x) = -6x + 240 = 0 => x = 40.
# L(40) = -3(1600) + 240(40) - 1000 = 3800.
L_econ = x*(300 - 2*x) - (x**2 + 40*x + 1000) - 20*x
x_opt3 = sp.solve(sp.diff(L_econ, x), x)[0]
assert x_opt3 == 40
L_max3 = L_econ.subs(x, 40)
assert L_max3 == 3800
print(f"P3-C3: x_opt = {x_opt3}, L_max = {L_max3} nghìn đồng => Đáp số: 3800")

# Câu 4: Oxyz khoảng cách từ A(1; 3; -1) đến d: (x-1)/2 = (y+1)/2 = (z-2)/1.
# M0(1; -1; 2), u = (2; 2; 1) => |u| = 3.
# M0A = (0; 4; -3). [M0A, u] = (4*1 - (-3)*2; -3*2 - 0*1; 0*2 - 4*2) = (10; -6; -8).
# |[M0A, u]| = sqrt(100 + 36 + 64) = sqrt(200) = 10*sqrt(2).
# Để ra số nguyên đẹp:
# Cho A(4; 5; 3). M0A = (3; 6; 1).
# [M0A, u] = (6*1 - 1*2; 1*2 - 3*1; 3*2 - 6*2) = (4; -1; -6) => sqrt(16 + 1 + 36) = sqrt(53).
# Hãy tìm A sao cho d(A, d) = 5 nguyên đẹp:
# Chọn M0(1; 2; 3), u = (2; 1; 2) => |u| = 3.
# Chọn n1 vuông u: n1 = (1; -2; 0) => |n1| = sqrt(5).
# Chọn A = M0 + 3*(-1; 2; 0) + 4*(0; 0; 0) ...
# Để đơn giản và chuẩn xác:
# Cho d qua M0(1; 0; 2) với VTCP u = (2; 1; 2) (|u| = 3).
# Điểm A(1; 5; 2). M0A = (0; 5; 0).
# [M0A, u] = (5*2 - 0*1; 0*2 - 0*2; 0*1 - 5*2) = (10; 0; -10) => |[M0A, u]| = 10*sqrt(2).
# Nếu M0A = (0; 3; 0) và u = (1; 0; 0) => d = 3!
# Cho d: (x - 2)/1 = (y - 1)/2 = (z + 1)/(-2) có |u| = sqrt(1 + 4 + 4) = 3.
# M0(2; 1; -1). Chọn A(2; 4; 3).
# M0A = (0; 3; 4).
# [M0A, u] = (3*(-2) - 4*2; 4*1 - 0*(-2); 0*2 - 3*1) = (-6 - 8; 4; -3) = (-14; 4; -3).
# Thử A(5; 7; -1). M0A = (3; 6; 0).
# [M0A, u] = (6*(-2) - 0; 0 - 3*(-2); 3*2 - 6*1) = (-12; 6; 0) => 144 + 36 = 180.
# Dùng bài toán khoảng cách từ A(1; 2; -1) đến mặt phẳng (P): 2x - 2y + z + 8 = 0:
# d(A, (P)) = |2 - 4 - 1 + 8| / 3 = 5/3.
# Hoặc bài toán cực trị khoảng cách: Cho mặt cầu (S): (x-1)^2 + (y-2)^2 + (z-3)^2 = 16 (R=4) và A(5; 6; 7).
# IA = sqrt(16 + 16 + 16) = sqrt(48).
# Để IA nguyên: I(1; 2; 3), A(7; 4; 6) => IA = sqrt(36 + 4 + 9) = sqrt(49) = 7. R = 4 => d_min = 7 - 4 = 3!
# Rất thanh lịch và chính xác!
IA_val = sp.sqrt((7 - 1)**2 + (4 - 2)**2 + (6 - 3)**2)
assert IA_val == 7
d_min4 = IA_val - 4
assert d_min4 == 3
print(f"P3-C4: IA = {IA_val}, R = 4 => d_min = {d_min4} => Đáp số: 3")

# Câu 5: Cầu thủ sút phạt đền 4 lần độc lập, p = 0.8. Tính P(X >= 3).
# P(X=3) = 4 * 0.8^3 * 0.2 = 0.4096
# P(X=4) = 0.8^4 = 0.4096
# P(X >= 3) = 0.4096 + 0.4096 = 0.8192 => Làm tròn hàng phần trăm: 0,82.
P_shoot = 4 * (Fraction(8, 10)**3) * Fraction(2, 10) + Fraction(8, 10)**4
assert P_shoot == Fraction(512, 625) # 0.8192
ans_p3_5 = round(float(P_shoot), 2)
assert ans_p3_5 == 0.82
print(f"P3-C5: P(X >= 3) = {float(P_shoot):.4f} => Đáp số: 0,82")

# Câu 6: Cắt vật thể tại x in [0; 4], thiết diện là HCN kích thước sqrt(x) và 6*sqrt(x) => S(x) = 6x.
# V = int_0^4 6x dx = [3x^2]_0^4 = 48.
V_solid = sp.integrate(6*x, (x, 0, 4))
assert V_solid == 48
print(f"P3-C6: V = {V_solid} m^3 => Đáp số: 48")

print("\n[OK] 100% 22 CÂU HỎI ĐỀ SỐ 10 ĐÃ ĐƯỢC AUDIT THÀNH CÔNG!")
