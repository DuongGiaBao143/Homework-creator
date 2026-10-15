import sympy as sp
import math
from fractions import Fraction

print("=== VERIFY DE 7 ===")

# PHAN I
# Cau 1: y = (x^2 - 2mx + m^2 + m - 2)/(x - m) = x - m + (m - 2)/(x - m)
# Co 2 cuc tri <=> m > 2.
# x1, x2 = m - sqrt(m-2), m + sqrt(m-2). Duong thang qua 2 cuc tri: y = 2x - 2m.
# AB^2 = (x2-x1)^2 + (y2-y1)^2 = 5*(x2-x1)^2 = 20*(m-2).
# AB <= 2*sqrt(15) <=> 20*(m-2) <= 60 <=> m - 2 <= 3 <=> m <= 5.
# Ket hop m > 2, m in Z => m in {3, 4, 5} -> 3 gia tri.
m_vals_c1 = [m for m in range(-10, 11) if m > 2 and 20*(m - 2) <= 60]
print("P1 C1 (m values):", m_vals_c1, "Count:", len(m_vals_c1))

# Cau 2: log_2(x - 1) + log_2(9 - x) >= 3
# DK: 1 < x < 9. (x-1)(9-x) >= 8 <=> x^2 - 10x + 17 <= 0
x_vals_c2 = [x for x in range(2, 9) if (x - 1)*(9 - x) >= 8]
print("P1 C2 (x values):", x_vals_c2, "Count:", len(x_vals_c2))

# Cau 3: f(x) + x*f'(x) = 4x^3 - 6x^2 + 2x + 1 => (x*f(x))' = 4x^3 - 6x^2 + 2x + 1
x = sp.Symbol('x')
xf = sp.integrate(4*x**3 - 6*x**2 + 2*x + 1, x) # x^4 - 2x^3 + x^2 + x
f_x = sp.simplify(xf / x)
I_c3 = sp.integrate(f_x, (x, 0, 2))
print("P1 C3: f(x) =", f_x, "I =", I_c3)

# Cau 4: (P): x - y - 2z + 4 = 0, Delta: (x-4)/2 = (y+2)/(-1) = (z-4)/1, A(2, -1, 3)
t = sp.Symbol('t')
N = [4 + 2*t, -2 - t, 4 + t]
A = [2, -1, 3]
M = [2*N[i] - A[i] for i in range(3)]
eq_P = M[0] - M[1] - 2*M[2] + 4
t_sol = sp.solve(eq_P, t)[0]
N_pt = [n.subs(t, t_sol) for n in N]
AN = [N_pt[i] - A[i] for i in range(3)]
print("P1 C4: t =", t_sol, "AN =", AN, "u = (-2)*AN =", [-2*v for v in AN])

# Cau 5: Bayes xe buyt (0.4, muon 0.06), xe dap dien (0.6, muon 0.02)
p_muon = Fraction(4, 10)*Fraction(6, 100) + Fraction(6, 100)*Fraction(2, 10)
p_buyt_given_muon = (Fraction(4, 10)*Fraction(6, 100)) / p_muon
print("P1 C5: P(B|M) =", p_buyt_given_muon)

# Cau 6: Thong ke ghep nhom phuong sai
# [4;6):6, [6;8):12, [8;10):10, [10;12):8, [12;14):4
mid = [5, 7, 9, 11, 13]
freq = [6, 12, 10, 8, 4]
n_tot = sum(freq)
mean_c6 = sum(m*f for m, f in zip(mid, freq)) / n_tot
var_c6 = sum(f*(m - mean_c6)**2 for m, f in zip(mid, freq)) / n_tot
print(f"P1 C6: N={n_tot}, mean={mean_c6}, var={var_c6:.2f}")

# Cau 7: f(x) = (x^2 - 5x + 7)*e^x tren [0; 3]
f7 = (x**2 - 5*x + 7)*sp.exp(x)
df7 = sp.factor(sp.diff(f7, x))
vals7 = {v: sp.simplify(f7.subs(x, v)) for v in [0, 1, 2, 3]}
print("P1 C7: df7 =", df7, "vals =", vals7)

# Cau 8: Dien tich hinh phang y = x^2 - 4x + 3 va y = x - 1
S_c8 = sp.integrate((x - 1) - (x**2 - 4*x + 3), (x, 1, 4))
print("P1 C8: S =", S_c8)

# Cau 9: (P): 2x - y + 2z - 16 = 0, A(1,2,1), B(4,-1,4), T = 2MA^2 + MB^2 min
# I = (2A + B)/3 = (2, 1, 2)
# Hinh chieu cua I(2,1,2) len (P): (2+2k, 1-k, 2+2k) -> 2(2+2k) - (1-k) + 2(2+2k) - 16 = 0 => 9k - 9 = 0 => k = 1 => M(4, 0, 4)
print("P1 C9: M = (4, 0, 4), a+b+c = 8")

# Cau 10: CSC u2 + u5 = 24, u3*u4 = 135, d > 0
u1, d = sp.symbols('u1 d', real=True)
sol10 = sp.solve([2*u1 + 5*d - 24, (u1 + 2*d)*(u1 + 3*d) - 135], (u1, d))
for u1_v, d_v in sol10:
    if d_v > 0:
        S10 = 10*u1_v + 45*d_v
        print("P1 C10: u1 =", u1_v, "d =", d_v, "S10 =", S10)

# Cau 11: A(2,-1,1), B(4,3,-1), C(1,2,4), D(5,4,6) -> P(3,1,0), Q(3,3,5) -> PQ = sqrt(29)
P_11 = [(2+4)//2, (-1+3)//2, (1-1)//2]
Q_11 = [(1+5)//2, (2+4)//2, (4+6)//2]
PQ_sq = sum((P_11[i]-Q_11[i])**2 for i in range(3))
print("P1 C11: P=", P_11, "Q=", Q_11, "PQ^2=", PQ_sq)

# Cau 12: 6 K12, 5 K11, 4 K10. Chon 4 du 3 khoi va K12 > K10
p_c12 = Fraction(math.comb(6, 2) * math.comb(5, 1) * math.comb(4, 1), math.comb(15, 4))
print("P1 C12: P =", p_c12)

print("\n=== PHAN II ===")
# Cau 1: Doanh nghiệp sản xuất thiết bị điện tử (lấy cảm hứng từ Tổng ôn.pdf trang 572 Câu 1)
# Hàm giá bán p(x) = -x^2 + 9x + 162 (triệu đồng/ngàn sản phẩm), chi phí C(x) = 2x^3 - 15x^2 + 60x + 80 (triệu đồng)
# Hoặc hàm lợi nhuận L(x) = R(x) - C(x):
# Let's check: R(x) = x*p(x) = -x^3 + 9x^2 + 162x
# C(x) = 54x + 100 => L(x) = -x^3 + 9x^2 + 108x - 100
# L'(x) = -3x^2 + 18x + 108 = -3(x^2 - 6x - 36) -> Để nghiệm nguyên đẹp:
# Chọn L'(x) = -3(x - 8)(x + 2) = -3(x^2 - 6x - 16) = -3x^2 + 18x + 48
# Khi đó L(x) = -x^3 + 9x^2 + 48x - 100:
# R(x) = x*p(x) với p(x) = 120 - x^2 + 9x => R(x) = -x^3 + 9x^2 + 120x
# C(x) = 72x + 100 => L(x) = -x^3 + 9x^2 + 48x - 100!
L = -x**3 + 9*x**2 + 48*x - 100
dL = sp.diff(L, x)
print("P2 C1: dL =", sp.factor(dL), "L(8) =", L.subs(x, 8), "L(6) =", L.subs(x, 6))

# Cau 2: Khảo sát 600 học sinh (Nguồn: Xác suất.pdf trang 135 Câu 95 THPT Nguyễn Gia Thiều)
# 400 học sinh trả lời "Thích học Toán" (P(T) = 2/3), 200 học sinh "Không thích" (P(~T) = 1/3)
# Tỉ lệ "Giỏi Toán" trong nhóm thích là 75% (P(G|T) = 0.75), trong nhóm không thích là 15% (P(G|~T) = 0.15)
P_T = Fraction(400, 600)
P_nT = Fraction(200, 600)
P_G_T = Fraction(75, 100)
P_G_nT = Fraction(15, 100)
P_G = P_T * P_G_T + P_nT * P_G_nT
P_T_given_G = (P_T * P_G_T) / P_G
print("P2 C2: P(T)=", P_T, "P(G)=", float(P_G), "P(T|G)=", P_T_given_G, float(P_T_given_G))

# Cau 3: Mức cường độ âm 2 loa A và B (Nguồn: Tổng ôn.pdf trang 8 Câu 44)
# L = 10 * log10(I / 10^-12) (dB).
# Loa A có L_A = 80 dB => I_A = 10^-4 W/m^2.
# Loa B có L_B = 90 dB => I_B = 10^-3 W/m^2.
# Khi bật cả 2 loa: I = I_A + I_B = 1.1 * 10^-3 W/m^2 => L = 10 * log10(1.1 * 10^9) = 90 + 10*log10(1.1) ≈ 90.41 dB!
I_A = 10**(80/10 - 12)
I_B = 10**(90/10 - 12)
L_both = 10 * math.log10((I_A + I_B) / 1e-12)
print(f"P2 C3: I_A={I_A:.1e}, I_B={I_B:.1e}, L_both={L_both:.2f} dB")

# Cau 4: Khinh khí cầu & 3 vệ tinh Oxyz (Nguồn: Tổng ôn.pdf trang 483 Câu 23)
# Vệ tinh A(1; 2; 6), B(4; 6; 18), C(3; 10; 18) hoặc chuyển động máy bay Câu 22!
# Hãy kiểm tra bài Khinh khí cầu tọa độ gọn:
# Khinh khí cầu M(x; y; z) có cao độ z = 5 (km).
# Ba trạm vệ tinh/radar đặt tại A(1; 2; 6), B(4; 6; 17), C(3; 10; 9).
# Giả sử vị trí thực của M là M(4; 6; 5):
# MA = sqrt((4-1)^2 + (6-2)^2 + (5-6)^2) = sqrt(9 + 16 + 1) = sqrt(26)
# Để MA, MB, MC đều nguyên đẹp:
# Chọn M(4; 5; 5):
# A(1; 1; 5) -> MA = sqrt(3^2 + 4^2 + 0) = 5 km
# B(4; 11; 13) -> MB = sqrt(0 + 6^2 + 8^2) = 10 km
# C(16; 5; 10) -> MC = sqrt(12^2 + 0 + 5^2) = 13 km
# Hãy kiểm tra hệ phương trình với z_M = 5:
x_m, y_m = sp.symbols('x_m y_m', real=True)
eq1 = (x_m - 1)**2 + (y_m - 1)**2 + (5 - 5)**2 - 25
eq2 = (x_m - 4)**2 + (y_m - 11)**2 + (5 - 13)**2 - 100
eq3 = (x_m - 16)**2 + (y_m - 5)**2 + (5 - 10)**2 - 169
sol_M = sp.solve([eq1, eq2, eq3], (x_m, y_m))
print("P2 C4 (Khinh khi cau M):", sol_M, "OM =", math.sqrt(4**2 + 5**2 + 5**2))

print("\n=== PHAN III ===")
# Cau 1: Cây sào ngăn góc hồ qua cọc K cách AB 1m, cách AC 8m (Nguồn: Tổng ôn.pdf trang 572 Câu 2)
# Đặt HQ = x > 0 => AQ = x + 1, AP = 8*(x + 1)/x
# PQ^2 = (x + 1)^2 + 64*(x + 1)^2 / x^2 = (x + 1)^2 * (1 + 64/x^2)
f_sao = (x + 1)**2 * (1 + 64/x**2)
df_sao = sp.diff(f_sao, x)
x_sao = [r for r in sp.solve(df_sao, x) if r.is_real and r > 0][0]
min_PQ = sp.sqrt(f_sao.subs(x, x_sao))
print(f"P3 C1 (Cay sao): x_opt = {x_sao}, min_PQ = {min_PQ} ≈ {float(min_PQ):.2f}")

# Cau 2: Chậu cây đặt trên giá đỡ 4 chân S(0;0;30), A(30;0;0), B(0;30;0), C(-30;0;0), D(0;-30;0), P = 80 N (Nguồn: Vận dụng cao.pdf trang 82 Câu 265)
# Bốn chân đối xứng nên độ lớn 4 lực bằng nhau: |F1| = |F2| = |F3| = |F4| = F.
# Vector SA = (30, 0, -30) => cos(góc giữa F_i và Oz) = 30 / (30*sqrt(2)) = 1/sqrt(2).
# Tổng hình chiếu lên trục thẳng đứng: 4 * F * (1/sqrt(2)) = 80 => 2*sqrt(2)*F = 80 => F = 20*sqrt(2) ≈ 28.28 N!
# Nếu hỏi bình phương độ lớn hoặc chọn S(0;0;40), A(30;0;0)... (tam giác 3-4-5):
# S(0; 0; 40), A(30; 0; 0), B(0; 30; 0), C(-30; 0; 0), D(0; -30; 0) -> SA = sqrt(30^2 + 40^2) = 50 cm!
# Khi đó cos(theta) = 40/50 = 4/5.
# 4 * F * (4/5) = 80 => (16/5)*F = 80 => F = 25 (N) nguyên đẹp 100%!!
print("P3 C2 (Gia do chau cay 30-40-50): F = 80 * 5 / 16 =", 80 * 5 // 16)

# Cau 3: Khu đất hình Elip trục lớn 10m (a=5), trục bé 8m (b=4), nội tiếp hình chữ nhật xây bể cá (Nguồn: Vận dụng cao.pdf trang 82 Câu 263)
# Diện tích elip S_E = pi * a * b = 20*pi.
# Hình chữ nhật nội tiếp có diện tích lớn nhất là S_max = 2*a*b = 40 m^2.
# Chi phí xây bể cá 800 ngàn/m^2, trồng hoa (phần còn lại) 900 ngàn/m^2:
# Vì chi phí bể cá RẺ hơn trồng hoa (800 < 900), tổng chi phí T = 800*S_hcn + 900*(20*pi - S_hcn) = 18000*pi - 100*S_hcn
# đạt NHỎ NHẤT khi S_hcn đạt LỚN NHẤT = 40 m^2!
# Khi đó T_min = (18000*pi - 4000) ngàn đồng = 18*pi - 4 ≈ 52.55 triệu đồng!
T_min_c3 = 18 * math.pi - 4
print(f"P3 C3 (Elip be ca): S_hcn_max = 40, T_min = {T_min_c3:.2f} trieu dong")

# Cau 4: Tia laser đặt tại A(6; 3; 4) chiếu vào tường (Oyz) tạo với trục Ox góc 45 độ (Nguồn: Toán thực tế.pdf trang 259 Câu 56)
# Hình chiếu vuông góc của A(6; 3; 4) lên (Oyz) là H(0; 3; 4) với AH = 6 m và OH = sqrt(3^2 + 4^2) = 5 m.
# Tia sáng AM tạo với Ox (tức AH) một góc 45 độ => Tam giác AHM vuông cân tại H => HM = AH * tan(45) = 6 m.
# Vậy M thuộc đường tròn tâm H(0; 3; 4), bán kính R = 6 m trên mặt phẳng (Oyz).
# Khoảng cách lớn nhất từ M đến gốc tọa độ O(0; 0; 0) là: OM_max = OH + R = 5 + 6 = 11 m! Nguyên đẹp 100%!
print("P3 C4 (Tia laser Oxyz): OH = 5, R = 6, OM_max =", 5 + 6)

# Cau 5: Xác suất kiểm tra sản phẩm / Trò chơi xúc xắc hoặc hộp bi qua 2 bước
# Hộp I có 4 bi đỏ, 6 bi xanh; Hộp II có 7 bi đỏ, 3 bi xanh.
# Tung một đồng xu cân đối: nếu sấp thì lấy 2 bi từ Hộp I, nếu ngửa thì lấy 2 bi từ Hộp II.
# Biết 2 bi lấy ra đều màu đỏ, tính xác suất để 2 bi đó được lấy từ Hộp II (dạng a/b tối giản, tính a+b).
p_2red_I = Fraction(math.comb(4, 2), math.comb(10, 2)) # 6/45
p_2red_II = Fraction(math.comb(7, 2), math.comb(10, 2)) # 21/45
p_II_given_2red = p_2red_II / (p_2red_I + p_2red_II) # 21/27 = 7/9 -> a+b = 16
print("P3 C5: P(II | 2 red) =", p_II_given_2red, "a+b =", p_II_given_2red.numerator + p_II_given_2red.denominator)

# Cau 6: Logo hình con cá giới hạn bởi 2 Parabol (Nguồn: Vận dụng cao.pdf trang 154 Câu 440)
# Hai parabol đối xứng qua trục Ox: P1: y = -1/4*x^2 + 4 và P2: y = 1/4*x^2 - 4, với x chạy từ -4 đến 6 (từ đầu cá x=-4 qua nút giao x=4 đến đuôi cá x=6)!
# Giao điểm của P1 và P2: 1/4*x^2 - 4 = 0 <=> x = -4 và x = 4.
# Thân cá: x in [-4; 4], Đuôi cá: x in [4; 6].
# Tổng diện tích Logo: S = int_{-4}^{4} 2*(4 - x^2/4) dx + int_{4}^{6} 2*(x^2/4 - 4) dx
S_than = sp.integrate(2*(4 - x**2/4), (x, -4, 4))
S_duoi = sp.integrate(2*(x**2/4 - 4), (x, 4, 6))
S_logo = S_than + S_duoi
print(f"P3 C6 (Logo con ca): S_than={S_than}, S_duoi={S_duoi}, S_logo={S_logo} ≈ {float(S_logo):.1f}")
