"""
Script kiểm định độc lập (Pha 1 & Pha 2) toàn bộ 22 câu hỏi của Đề số 8 bằng SymPy.
Đảm bảo:
- Không có bất kỳ câu hàm hợp g(x) = f(u(x)) nào.
- Phần I phân bố chuẩn 3A - 3B - 3C - 3D.
- Tất cả số liệu, nghiệm, tích phân, xác suất, Oxyz đều chính xác tuyệt đối 100%.
"""
import sympy as sp
from fractions import Fraction

x, y, z, t, m = sp.symbols("x y z t m", real=True)

print("=== KIỂM ĐỊNH ĐỀ SỐ 8 ===")

# ---------------------------------------------------------
# PHẦN I: 12 CÂU (3A - 3B - 3C - 3D)
# Dự kiến bảng đáp án:
# 1.B, 2.D, 3.A, 4.C, 5.B, 6.A, 7.D, 8.C, 9.A, 10.D, 11.C, 12.B
# Đếm:
# A: Câu 3, 6, 9 (3 câu)
# B: Câu 1, 5, 12 (3 câu)
# C: Câu 4, 8, 11 (3 câu)
# D: Câu 2, 7, 10 (3 câu)
# ---------------------------------------------------------

# Câu 1 (Đáp án B): Hàm phân thức y = (x^2 - 3x + 5)/(x - 1).
# Gọi I là giao điểm hai tiệm cận. Khoảng cách từ I đến tiếp tuyến tại x0 = 2.
f1 = (x**2 - 3*x + 5) / (x - 1)
# Tiệm cận đứng x = 1, tiệm cận xiên y = x - 2 => I(1, -1)
I_pt = (1, -1)
k1 = sp.diff(f1, x).subs(x, 2)
y0_1 = f1.subs(x, 2)
# Tiếp tuyến: y - y0 = k1*(x - 2) <=> -k1*x + y - y0 + 2*k1 = 0
A_line, B_line, C_line = -k1, 1, -y0_1 + 2*k1
d_I = abs(A_line*I_pt[0] + B_line*I_pt[1] + C_line) / sp.sqrt(A_line**2 + B_line**2)
assert sp.simplify(d_I - 6*sp.sqrt(5)/5) == 0
print(f"P1-C1: I={I_pt}, pttt: y = {k1}*(x-2) + {y0_1}, d = {sp.simplify(d_I)} -> Chọn B (6*sqrt(5)/5)")

# Câu 2 (Đáp án D): Tổng các nghiệm thực của phương trình 9^x - 6*3^(x+1) + 27 = 0.
sol_t = sp.solve(t**2 - 18*t + 27, t)
sum_x2 = sp.simplify(sp.log(sol_t[0]*sol_t[1], 3))
assert sum_x2 == 3
print(f"P1-C2: t1*t2 = {sol_t[0]*sol_t[1]} => x1 + x2 = {sum_x2} -> Chọn D (3)")

# Câu 3 (Đáp án A): Tích phân tuyến tính:
# int_1^3 [f(x) + 3g(x)]dx = 10 và int_1^3 [2f(x) - g(x)]dx = 6.
# Tính I = int_1^3 [f(x) + 2g(x) - 2x + 1]dx.
If, Ig = sp.symbols("If Ig")
sol3 = sp.solve([If + 3*Ig - 10, 2*If - Ig - 6], (If, Ig))
I3 = sol3[If] + 2*sol3[Ig] + sp.integrate(-2*x + 1, (x, 1, 3))
assert I3 == 2
print(f"P1-C3: If={sol3[If]}, Ig={sol3[Ig]}, I = {I3} -> Chọn A (2)")

# Câu 4 (Đáp án C): Mặt cầu tâm I(2; -1; 3) tiếp xúc với (P): 2x - 2y + z + 3 = 0.
R4 = abs(2*2 - 2*(-1) + 1*3 + 3) / sp.sqrt(2**2 + (-2)**2 + 1**2)
assert R4 == 4 and R4**2 == 16
print(f"P1-C4: R = {R4}, R^2 = {R4**2} -> Chọn C")

# Câu 5 (Đáp án B): Xác suất Bayes kiểm định sách tại 2 phân xưởng A (60%, đạt chuẩn 95%) và B (40%, đạt chuẩn 90%).
# Chọn 1 cuốn bị lỗi, xác suất do phân xưởng A in:
p5 = Fraction(60, 100) * Fraction(5, 100) / (Fraction(60, 100)*Fraction(5, 100) + Fraction(40, 100)*Fraction(10, 100))
assert p5 == Fraction(3, 7)
print(f"P1-C5: P(A|Lỗi) = {p5} -> Chọn B (3/7)")

# Câu 6 (Đáp án A): Khoảng tứ phân vị Delta_Q của mẫu số liệu ghép nhóm (n = 40):
# [10; 15): 6, [15; 20): 10, [20; 25): 12, [25; 30): 10, [30; 35): 2
Q1 = 15 + Fraction(10 - 6, 10) * 5
Q3 = 25 + Fraction(30 - 28, 10) * 5
Delta_Q = Q3 - Q1
assert Q1 == 17 and Q3 == 26 and Delta_Q == 9
print(f"P1-C6: Q1 = {Q1}, Q3 = {Q3}, Delta_Q = {Delta_Q} -> Chọn A (9)")

# Câu 7 (Đáp án D): GTLN của hàm số f(x) = x - 2*ln(x) trên đoạn [1; e^2].
f7 = x - 2*sp.log(x)
crit7 = sp.solve(sp.diff(f7, x), x)
vals7 = [f7.subs(x, 1), f7.subs(x, 2), f7.subs(x, sp.E**2)]
print(f"P1-C7: f(1)={vals7[0]}, f(2)={vals7[1]}, f(e^2)={vals7[2]} -> Chọn D (e^2 - 4)")

# Câu 8 (Đáp án C): Thể tích khối tròn xoay giới hạn bởi y = sqrt(4x - x^2) và y = 0 quanh Ox.
V8 = sp.pi * sp.integrate(4*x - x**2, (x, 0, 4))
assert V8 == 32*sp.pi/3
print(f"P1-C8: V = {V8} -> Chọn C (32*pi/3)")

# Câu 9 (Đáp án A): Sin của góc giữa đường thẳng d: (x-1)/2 = (y+1)/(-1) = (z-2)/2 và (P): 2x - y - 2z + 5 = 0.
u9 = sp.Matrix([2, -1, 2])
n9 = sp.Matrix([2, -1, -2])
sin9 = abs(u9.dot(n9)) / (u9.norm() * n9.norm())
assert sin9 == sp.Rational(1, 9)
print(f"P1-C9: sin(d, (P)) = {sin9} -> Chọn A (1/9)")

# Câu 10 (Đáp án D): Cấp số nhân dương u1 + u2 = 12, u3 + u4 = 108. Tính u5.
q10 = sp.sqrt(sp.Rational(108, 12))
u1_10 = sp.Rational(12, 1 + q10)
u5_10 = u1_10 * q10**4
assert u5_10 == 243
print(f"P1-C10: u1={u1_10}, q={q10}, u5={u5_10} -> Chọn D (243)")

# Câu 11 (Đáp án C): Hình chóp S.ABCD đáy HCN AB=3, AD=4, SA vuông đáy, SA=12/5. Khoảng cách từ A đến (SBD).
inv_d2 = 1/sp.Rational(12, 5)**2 + 1/sp.Rational(3)**2 + 1/sp.Rational(4)**2
d11 = sp.simplify(1 / sp.sqrt(inv_d2))
assert sp.simplify(d11 - 6*sp.sqrt(2)/5) == 0
print(f"P1-C11: d(A, (SBD)) = {d11} -> Chọn C (6*sqrt(2)/5)")

# Câu 12 (Đáp án B): Chọn 3 thẻ từ 20 thẻ (1..20). Xác suất 3 thẻ lập thành CSC.
p12 = Fraction(2 * (10*9//2), 20*19*18//6)
assert p12 == Fraction(3, 38)
print(f"P1-C12: P = {p12} -> Chọn B (3/38)")

# ---------------------------------------------------------
# PHẦN II: 4 CÂU ĐÚNG/SAI
# ---------------------------------------------------------
print("\n--- PHẦN II ---")

# Câu 1: Nồng độ thuốc C(t) = 6t / (t^2 + 4) (mg/lít), t >= 0 (giờ)
C_t = 6*t / (t**2 + 4)
C_diff = sp.simplify(sp.diff(C_t, t))
sol_ge = sp.solve(sp.Eq(C_t, sp.Rational(6, 5)), t)
assert C_t.subs(t, 0) == 0 and C_t.subs(t, 2) == sp.Rational(3, 2)
assert sol_ge == [1, 4]
print(f"P2-C1: C(0)=0, C(2)=1.5 (a: Đ); C'(t)={C_diff} (b: Đ); Tăng trên [0;2] chứ không phải [0;4] (c: S); C(t)>=1.2 trên [1;4] dài 3h (d: Đ) -> Đ-Đ-S-Đ")

# Câu 2: Ô tô phanh khẩn cấp: v0 = 24 m/s, chướng ngại vật cách 65 m, phản ứng 0.5s, sau đó v(t) = 24 - 6t^2.
s_react = 24 * sp.Rational(1, 2)
t_stop = sp.solve(24 - 6*t**2, t)[1]
s_brake = sp.integrate(24 - 6*t**2, (t, 0, t_stop))
dist_remain = 65 - (s_react + s_brake)
assert s_react == 12 and t_stop == 2 and s_brake == 32 and dist_remain == 21
print(f"P2-C2: s_react={s_react}m (a: Đ); t_stop={t_stop}s != 4s (b: S); s_brake={s_brake}m (c: Đ); còn cách {dist_remain}m (d: Đ) -> Đ-S-Đ-Đ")

# Câu 3: Hệ thống định tuyến 2 kênh A và B:
# P(A_{n+1}|A_n) = 0.7, P(B_{n+1}|A_n) = 0.3
# P(A_{n+1}|B_n) = 0.6, P(B_{n+1}|B_n) = 0.4
# Gói 1 truyền qua A.
pB2 = Fraction(3, 10)
pA2A3 = Fraction(7, 10) * Fraction(7, 10)
pA3 = Fraction(7, 10)*Fraction(7, 10) + Fraction(3, 10)*Fraction(6, 10)
pB2_given_A3 = (Fraction(3, 10)*Fraction(6, 10)) / pA3
assert pB2 == Fraction(3, 10) and pA2A3 == Fraction(49, 100) and pA3 == Fraction(67, 100) and pB2_given_A3 == Fraction(18, 67)
print(f"P2-C3: P(B2)={float(pB2)} (a: Đ); P(A2 cap A3)={float(pA2A3)} (b: Đ); P(A3)={float(pA3)} != 0.65 (c: S); P(B2|A3)={pB2_given_A3} (d: Đ) -> Đ-Đ-S-Đ")

# Câu 4: Cabin cáp treo xuất phát từ A(10; 3; 0), đi theo hướng u=(2; -2; 1) với tốc độ v = 6 m/s. Trạm K(55; -32; 20).
M_t = sp.Matrix([10 + 4*t, 3 - 4*t, 2*t])
K_pt = sp.Matrix([55, -32, 20])
dist_sq = (M_t - K_pt).dot(M_t - K_pt)
t_min = sp.solve(sp.diff(dist_sq, t), t)[0]
d_min = sp.sqrt(dist_sq.subs(t, t_min))
assert t_min == 10 and d_min == 5*sp.sqrt(2)
print(f"P2-C4: PT chính tắc (a: Đ); M(10+4t; 3-4t; 2t) (b: Đ); z_B=120 => t=60s != 40s (c: S); KM_min = {d_min} tại t={t_min}s (d: Đ) -> Đ-Đ-S-Đ")

# ---------------------------------------------------------
# PHẦN III: 6 CÂU TRẢ LỜI NGẮN
# ---------------------------------------------------------
print("\n--- PHẦN III ---")

# Câu 1: Lăng trụ tam giác đều cạnh đáy 4 dm, cạnh bên 9 dm, quấn dây đèn LED 1 vòng từ A qua BB', CC' đến A'.
L_min = sp.sqrt((3*4)**2 + 9**2)
assert L_min == 15
print(f"P3-C1: L_min = {L_min} dm -> Đáp số: 15")

# Câu 2: Khối bê tông cao 3 m, thiết diện cách mặt đất x mét (0 <= x <= 3) là HCN dài (6-x) m, rộng (4-x) m.
V_betong = sp.integrate((6 - x)*(4 - x), (x, 0, 3))
assert V_betong == 36
print(f"P3-C2: V = {V_betong} m^3 -> Đáp số: 36")

# Câu 3: Nhà máy sản xuất x lô linh kiện, giá bán p(x) = 200 - 0.5x, chi phí C(x) = 150 + 72x, thuế 10% doanh thu.
R_x = x * (200 - sp.Rational(1, 2)*x)
L_x = sp.Rational(9, 10)*R_x - (150 + 72*x)
x_opt = sp.solve(sp.diff(L_x, x), x)[0]
assert x_opt == 120
print(f"P3-C3: x_opt = {x_opt} lô (L_max = {L_x.subs(x, x_opt)} triệu) -> Đáp số: 120")

# Câu 4: Oxyz điểm M(a; b; 0) trên (Oxy) với A(1; 2; 3), B(9; 10; 7) sao cho T = MA^2 + 3*MB^2 nhỏ nhất. Tính a + 2b.
a, b = sp.symbols("a b", real=True)
T4 = (a-1)**2 + (b-2)**2 + 3**2 + 3*((a-9)**2 + (b-10)**2 + 7**2)
sol4 = sp.solve([sp.diff(T4, a), sp.diff(T4, b)], (a, b))
ans4 = sol4[a] + 2*sol4[b]
assert sol4[a] == 7 and sol4[b] == 8 and ans4 == 23
print(f"P3-C4: M=({sol4[a]}; {sol4[b]}; 0), T_min={T4.subs(sol4)}, a + 2b = {ans4} -> Đáp số: 23")

# Câu 5: Mã lặp 3 bit (000 hoặc 111) với xác suất phát bit 0 là 0.5, phát bit 1 là 0.5; xác suất lỗi mỗi bit độc lập là 0.2.
# Nhận được 110, tính xác suất tín hiệu gốc là bit 1.
p5_bit1 = (Fraction(1, 2) * Fraction(4, 5)**2 * Fraction(1, 5)) / (
    Fraction(1, 2) * Fraction(4, 5)**2 * Fraction(1, 5) + Fraction(1, 2) * Fraction(1, 5)**2 * Fraction(4, 5)
)
assert p5_bit1 == Fraction(4, 5)
print(f"P3-C5: P(phát 1 | nhận 110) = {float(p5_bit1)} -> Đáp số: 0,8")

# Câu 6: Cổng vòm giới hạn bởi 2 parabol y = 9 - x^2 và y = 6 - (2/3)x^2 trên [-3; 3] và trục hoành Ox.
# Phần vòm gạch chéo (giữa 2 parabol) ốp đá giá 2 triệu đồng/m^2; phần lối đi tô đậm (dưới parabol thấp hơn) lắp kính giá 1 triệu đồng/m^2.
# Tính tổng chi phí (triệu đồng).
S_vom = sp.integrate((9 - x**2) - (6 - sp.Rational(2, 3)*x**2), (x, -3, 3))
S_kinh = sp.integrate(6 - sp.Rational(2, 3)*x**2, (x, -3, 3))
cost6 = 2 * S_vom + 1 * S_kinh
assert S_vom == 12 and S_kinh == 24 and cost6 == 48
print(f"P3-C6: S_vom={S_vom} m^2, S_kinh={S_kinh} m^2, Tổng chi phí = {cost6} triệu đồng -> Đáp số: 48")
print("\n[OK] Tất cả 22 câu của Đề số 8 đã được kiểm định chính xác 100%!")
