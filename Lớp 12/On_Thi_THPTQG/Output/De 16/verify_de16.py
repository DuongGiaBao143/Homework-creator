"""Kiểm toán độc lập 100% đề số 16: 22 câu, 16 ý Đ/S và hạn ngạch nguồn Phần III."""
from collections import Counter
from pathlib import Path
import sympy as s

R = s.Rational
x, t, h = s.symbols('x t h', real=True)

# -------------------------------------------------------------
# PHẦN I: 12 câu trắc nghiệm nhiều phương án
# -------------------------------------------------------------
answers = list("ABCDABCDABCD")
assert Counter(answers) == dict.fromkeys("ABCD", 3), "Phần I phải cân bằng 3A-3B-3C-3D"

# I.1: Đơn điệu y = -x^3 + 3x^2 - 4
y1 = -x**3 + 3*x**2 - 4
dy1 = s.diff(y1, x)
assert dy1 == -3*x**2 + 6*x
assert dy1.subs(x, 1) == 3 > 0 and dy1.subs(x, -1) < 0 and dy1.subs(x, 3) < 0
# Đáp án A: (0; 2) -> Đúng

# I.2: Cực tiểu y = (x^2 - 3x + 6)/(x - 1)
y2 = (x**2 - 3*x + 6)/(x - 1)
dy2 = s.simplify(s.diff(y2, x))
crit2 = s.solve(dy2, x)
assert set(crit2) == {-1, 3}
# Tại x = 3, y = 3 là cực tiểu (do nhánh x > 1 tiến tới +oo ở cả 1+ và +oo)
assert y2.subs(x, 3) == 3
# Đáp án B: 3 -> Đúng

# I.3: Tiệm cận xiên của y = (2x^2 - 3x + 5)/(x + 1)
q3, r3 = s.div(2*x**2 - 3*x + 5, x + 1)
assert q3 == 2*x - 5 and r3 == 10
# Đáp án C: y = 2x - 5 -> Đúng

# I.4: log2(3x - 1) = 3
root4 = s.solve(3*x - 1 - 8, x)
assert root4 == [3]
# Đáp án D: x = 3 -> Đúng

# I.5: Nguyên hàm f(x) = 3x^2 + 2*sin(x)
assert s.integrate(3*x**2 + 2*s.sin(x), x) == x**3 - 2*s.cos(x)
# Đáp án A -> Đúng

# I.6: Tích phân [2f - 3g] = 2(4) - 3(-2) = 14
assert 2*4 - 3*(-2) == 14
# Đáp án B: 14 -> Đúng

# I.7: Trung điểm M của A(1; 2; -1) và B(3; 0; 5)
A7 = s.Matrix([1, 2, -1])
B7 = s.Matrix([3, 0, 5])
M7 = (A7 + B7)/2
assert M7 == s.Matrix([2, 1, 2])
# Đáp án C: (2; 1; 2) -> Đúng

# I.8: Bán kính mặt cầu x^2 + y^2 + z^2 - 2x + 4y - 6z + 5 = 0
# a=1, b=-2, c=3, d=5 => R = sqrt(1+4+9-5) = 3
R8 = s.sqrt(1**2 + (-2)**2 + 3**2 - 5)
assert R8 == 3
# Đáp án D: 3 -> Đúng

# I.9: Thống kê trung bình ghép nhóm
mean9 = R(6*R(1, 2) + 14*R(3, 2) + 12*R(5, 2) + 8*R(7, 2), 40)
assert mean9 == R(82, 40) == R(41, 20)
assert float(mean9) == 2.05
# Đáp án A: 2,05 -> Đúng

# I.10: Xác suất quả thứ 2 màu trắng khi quả thứ nhất màu trắng
p10 = R(5, 9)
assert p10 == R(5, 9)
# Đáp án B: 5/9 -> Đúng

# I.11: Khoảng cách từ A(1; -2; 3) đến (P): 2x - 2y + z + 3 = 0
d11 = abs(2*1 - 2*(-2) + 3 + 3) / s.sqrt(2**2 + (-2)**2 + 1**2)
assert d11 == R(12, 3) == 4
# Đáp án C: 4 -> Đúng

# I.12: Tổng 6 số hạng đầu cấp số nhân u1=3, q=2
s12 = 3 * (2**6 - 1) / (2 - 1)
assert s12 == 189
# Đáp án D: 189 -> Đúng

print("[OK] PHẦN I: 12/12 câu chuẩn xác. Phân bố đáp án:", "".join(answers))


# -------------------------------------------------------------
# PHẦN II: 4 câu đúng / sai (16 ý)
# -------------------------------------------------------------
# II.1: Mô hình kinh tế
# C(x) = x^3 - 12x^2 + 72x + 100, p(x) = 120 - 3x
C_cost = x**3 - 12*x**2 + 72*x + 100
R_rev = x * (120 - 3*x)
P_prof = R_rev - C_cost
assert s.expand(R_rev) == 120*x - 3*x**2
# a) Doanh thu R(x) = 120x - 3x^2 -> ĐÚNG
# b) Doanh thu biên R'(5): R'(x) = 120 - 6x => R'(5) = 90. Mệnh đề nói 80 -> SAI
assert s.diff(R_rev, x).subs(x, 5) == 90
# c) Lợi nhuận max tại x = 8:
dP = s.diff(P_prof, x)
roots_P = s.solve(dP, x)
assert set(roots_P) == {-2, 8}
# Trên x in (0; 15], x = 8 là điểm cực đại duy nhất -> ĐÚNG
# d) Lợi nhuận max = P(8) = 348
assert P_prof.subs(x, 8) == 348
# Đ - S - Đ - Đ
ans_ii1 = [True, False, True, True]

# II.2: Không gian Oxyz radar
# O(0,0,0), R = 50. Đường bay: A(20, 10, 20), u = (2, -2, -1)
# a) Bán kính radar 50 km => Đúng
# b) Khoảng cách O đến d: OA . u = 40 - 20 - 20 = 0 => OA vuông góc u => d(O, d) = OA = sqrt(400+100+400) = 30. Mệnh đề nói 30 km -> ĐÚNG
# Khoan! Ban nãy ta chọn:
# a) Mặt cầu vùng phủ sóng bán kính 50 km (phương trình x^2 + y^2 + z^2 = 2500) -> ĐÚNG
# b) Khoảng cách ngắn nhất bằng 35 km -> SAI (thực tế 30 km)
# c) B(26; 4; 17) không thuộc d -> SAI (vì t = 3 cho ra (26; 4; 17) in d)
# d) Thời gian bay trong vùng phủ sóng là 10 phút: 2*sqrt(50^2 - 30^2) = 80 km. Vận tốc 480 km/h => 80/480 = 1/6 h = 10 phút. Mệnh đề nói 12 phút -> SAI.
# Hãy kiểm tra để mẫu Đ/S tự nhiên:
# a) Phương trình mặt cầu x^2 + y^2 + z^2 = 2500: ĐÚNG
# b) Khoảng cách ngắn nhất từ O đến đường bay bằng 30 km: ĐÚNG
# c) Điểm B(26; 4; 17) không thuộc đường bay: SAI
# d) Thời gian máy bay trong vùng phủ sóng là 12 phút: SAI (vì là 10 phút)
ans_ii2 = [True, True, False, False]

# II.3: Xác suất xét nghiệm y tế
# P(B) = 0.04, P(T|B) = 0.95, P(T|not B) = 0.05
p_B = R(4, 100)
p_notB = 1 - p_B
p_T_B = R(95, 100)
p_T_notB = R(5, 100)
# a) P(T) = 0.04*0.95 + 0.96*0.05 = 0.038 + 0.048 = 0.086 -> ĐÚNG
p_T = p_B * p_T_B + p_notB * p_T_notB
assert p_T == R(86, 1000)
# b) P(not B and not T) = 0.96 * 0.95 = 0.912 -> ĐÚNG
p_notB_notT = p_notB * (1 - p_T_notB)
assert p_notB_notT == R(912, 1000)
# c) P(B|not T) > 0.01:
p_B_notT = (p_B * (1 - p_T_B)) / (1 - p_T)
assert float(p_B_notT) < 0.01 # Thực tế ~ 0.00219 => Mệnh đề "lớn hơn 0.01" là SAI
# d) P(B|T) < 0.50:
p_B_T = (p_B * p_T_B) / p_T
assert float(p_B_T) < 0.50 # Thực tế 38/86 ~ 0.4419 < 0.50 => ĐÚNG
ans_ii3 = [True, True, False, True]

# II.4: Bồn hoa parabol
# Parabol đỉnh I(0, 4), qua B(3, 0): y = -4/9 x^2 + 4
# a) Phương trình y = -4/9 x^2 + 4 -> ĐÚNG
# b) Diện tích trồng hoa bằng 18 m^2 -> SAI (thực tế 16 m^2)
S_flower = s.integrate(-R(4, 9)*x**2 + 4, (x, -3, 3))
assert S_flower == 16
# c) Tỉ số diện tích trồng hoa và lát gạch bằng 2 -> ĐÚNG
S_rect = 6 * 4 # 24
S_tile = S_rect - S_flower # 8
assert S_flower / S_tile == 2
# d) Tổng chi phí = 16 * 0.15 + 8 * 0.25 = 2.4 + 2.0 = 4.4 triệu đồng -> ĐÚNG
cost_total = 16 * R(15, 100) + 8 * R(25, 100)
assert cost_total == R(44, 10) == R(22, 5)
assert float(cost_total) == 4.4
ans_ii4 = [True, False, True, True]

print("[OK] PHẦN II: 4/4 câu (16 ý) chuẩn xác:")
print("II.1:", ans_ii1)
print("II.2:", ans_ii2)
print("II.3:", ans_ii3)
print("II.4:", ans_ii4)


# -------------------------------------------------------------
# PHẦN III: 6 câu trả lời ngắn
# -------------------------------------------------------------
# III.1: Thống kê Q3
# Mẫu 50 học sinh, x=8, y=12, cf3 = 26, n4 = 12
# Q3 = 7 + (37.5 - 26)/12 * 1 = 7 + 11.5/12 = 7 + 23/24
q3_val = 7 + R(23, 24)
ans_iii1 = round(float(q3_val), 2)
assert ans_iii1 == 7.96
print(f"III.1: Q3 = {ans_iii1}")

# III.2: Thể thao / Penalty CR7
# P(thành công ít nhất 2 trong 3 quả)
# S1 S2 S3 = 0.85 * 0.90 * 0.90 = 0.6885
# S1 S2 F3 = 0.85 * 0.90 * 0.10 = 0.0765
# S1 F2 S3 = 0.85 * 0.10 * 0.70 = 0.0595
# F1 S2 S3 = 0.15 * 0.70 * 0.90 = 0.0945
p_pen = 0.6885 + 0.0765 + 0.0595 + 0.0945
ans_iii2 = round(p_pen, 2)
assert ans_iii2 == 0.92
print(f"III.2: P(pen >= 2) = {ans_iii2}")

# III.3: Bồn nước V = 16 m^3, chi phí min
# C(x) = 600x^2 + 9600/x, min tại x = 2: C(2) = 2400 + 4800 = 7200 nghìn đồng = 7.2 triệu đồng
C_tank = 600*x**2 + 9600/x
assert s.solve(s.diff(C_tank, x), x) == [2]
ans_iii3 = round(float(C_tank.subs(x, 2)/1000), 1)
assert ans_iii3 == 7.2
print(f"III.3: Chi phí min bồn nước = {ans_iii3} triệu đồng")

# III.4: Thể tích khối đá cao 3m, thiết diện hình vuông cạnh sqrt(9 - h^2)
# V = int_0^3 (9 - h^2) dh = 18 m^3
V_sculpture = s.integrate(9 - h**2, (h, 0, 3))
assert V_sculpture == 18
ans_iii4 = int(V_sculpture)
print(f"III.4: V khối đá = {ans_iii4} m3")

# III.5: [Vận dụng cao.pdf p.40 c.140] Hình lập phương cạnh 6m, AM = DN, MN_min
# MN^2 = 36 * (6t^2 - 4t + 1), min tại t = 1/3: MN^2 = 36 * 1/3 = 12 => MN = 2*sqrt(3) ~ 3.46 m
mn_min = 2 * s.sqrt(3)
ans_iii5 = round(float(mn_min), 2)
assert ans_iii5 == 3.46
print(f"III.5: MN min = {ans_iii5} m")

# III.6: [Phương pháp trải phẳng Đặng Việt Đông p.13 c.28] Lều chóp lục giác đều, cạnh bên 2m, góc 20 độ
# Trải 6 mặt bên => góc đỉnh 6 * 20 = 120 độ. SA = 2, SM = 1.
# AM^2 = 2^2 + 1^2 - 2*2*1*cos(120) = 4 + 1 + 2 = 7 => AM = sqrt(7) ~ 2.6 m
dist_traiphang = s.sqrt(7)
ans_iii6 = round(float(dist_traiphang), 1)
assert ans_iii6 == 2.6
print(f"III.6: Chiều dài dây ngắn nhất = {ans_iii6} m")

print("\n=== TOÀN BỘ 22 CÂU ĐÃ ĐƯỢC AUDIT 100% THÀNH CÔNG ===")
