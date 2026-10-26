import sympy as sp
import numpy as np

print("=== KIEM TRA TOAN BO 22 CAU HOI CHUYEN DE HAM SO ===")

# --- PHAN I ---
print("\n--- PHAN I ---")
# Cau 1: y = -x^3 + 3x^2 - 4. y' = -3x^2 + 6x = -3x(x-2) > 0 <=> 0 < x < 2. Chon B (0; 2).
x = sp.Symbol('x')
f1 = -x**3 + 3*x**2 - 4
df1 = sp.diff(f1, x)
print("Cau 1: df1 =", df1, "nghiem df1=0:", sp.solve(df1, x))

# Cau 2: y = x^3 - 3x + 2. Cuc dai tai x = -1, y = 4. Chon C (-1; 4).
f2 = x**3 - 3*x + 2
df2 = sp.diff(f2, x)
ddf2 = sp.diff(df2, x)
print("Cau 2: cuc dai tai x=-1, y=", f2.subs(x, -1), "ddf2(-1)=", ddf2.subs(x, -1))

# Cau 3: y = (2x - 3)/(x + 1). TCD x = -1. Chon A.

# Cau 4: y = (x^2 - 3x + 5)/(x - 2) = x - 1 + 3/(x-2). TCX y = x - 1. Chon C.
f4 = (x**2 - 3*x + 5)/(x - 2)
q, r = sp.div(x**2 - 3*x + 5, x - 2)
print("Cau 4: thuong =", q, "du =", r)

# Cau 5: f(x) = x^3 - 3x^2 - 9x + 5 tren [0; 4].
f5 = x**3 - 3*x**2 - 9*x + 5
vals5 = [f5.subs(x, 0), f5.subs(x, 3), f5.subs(x, 4)]
print("Cau 5: f(0)=", vals5[0], "f(3)=", vals5[1], "f(4)=", vals5[2], "min=", min(vals5)) # Chon D: -22

# Cau 6: y = (2x + 1)/(x - 1). Chon A.

# Cau 7: y = (2x^2 + 3x - 1)/(x + 1) = 2x + 1 - 2/(x+1). TCD: x = -1, TCX: y = 2x + 1 => I(-1; -1). Chon C.
q7, r7 = sp.div(2*x**2 + 3*x - 1, x + 1)
print("Cau 7: thuong =", q7, "du =", r7, "I = (-1, {})".format(q7.subs(x, -1)))

# Cau 8: y = x^3 - 3x^2 + 2. y' = 3x^2 - 6x = 9 <=> x^2 - 2x - 3 = 0 <=> x = -1 or x = 3.
# x = -1 => y = -2 => PTTT: y = 9x + 7.
# x = 3 => y = 2 => PTTT: y = 9x - 25.
# ca 2 tiep tuyen deu song song voi y = 9x - 14. Co 2 tiep tuyen. Chon D.

# Cau 9: y = 1/3 x^3 - m x^2 + (m+2)x - 5 dong bien tren R <=> Delta' <= 0 <=> m^2 - m - 2 <= 0 <=> -1 <= m <= 2. Chon A.

# Cau 10: f(x) = x^3 - 3x^2 + 1. 2f(x) - 1 = 0 <=> f(x) = 1/2.
# y_CD = f(0) = 1, y_CT = f(2) = -3. Vi -3 < 1/2 < 1 nen co 3 nghiem. Chon B.

# Cau 11: y = (x^2 - x + 1)/(x - 1). Cuc tri A(0; -1), B(2; 3). AB = sqrt(4 + 16) = 2*sqrt(5). Chon B.

# Cau 12: Thiet ke be ca day x, 2x, cao h. V = 2 x^2 h = 4 => h = 2/x^2.
# Gia day: 150k/m2, xung quanh: 100k/m2.
# Ta chon he so gia va V sao cho x nguyen dep:
# S_day = 2x^2, S_xq = 2(x + 2x)h = 6xh.
# Gia day = a (nghin/m2), gia xq = b (nghin/m2).
# Chi phi C(x) = a * 2x^2 + b * 6x * (V / (2x^2)) = 2a x^2 + 3bV / x.
# C'(x) = 4a x - 3bV / x^2 = 0 <=> x^3 = 3bV / (4a).
# Ta muon x = 2. Neu V = 16 m3, a = 150, b = 100:
# 3 * 100 * 16 / (4 * 150) = 4800 / 600 = 8 => x^3 = 8 => x = 2 m!
# Khi x = 2 m:
# Day: dai 4 m, rong 2 m, cao h = 16 / (2 * 4) = 2 m!
# Dien tich day = 8 m2 => Chi phi day = 8 * 150 = 1200 nghin = 1,2 trieu.
# Dien tich xq = 2 * (4 + 2) * 2 = 24 m2 => Chi phi xq = 24 * 100 = 2400 nghin = 2,4 trieu.
# Tong chi phi min = 1200 + 2400 = 3600 nghin dong = 3,6 trieu dong!
# Bon phuong an: A. 4,2 trieu dong. B. 4,8 trieu dong. C. 3,2 trieu dong. D. 3,6 trieu dong.
# Chon D!
# Vay phan bo Phan I:
# 1-B, 2-C, 3-A, 4-C, 5-D, 6-A, 7-C, 8-D, 9-A, 10-B, 11-B, 12-D
# Dem: A: 3 (3, 6, 9); B: 3 (1, 10, 11); C: 3 (2, 4, 7); D: 3 (5, 8, 12).
# DUNG CHUAN 3A - 3B - 3C - 3D!
print("Phan I dap an:", ["B", "C", "A", "C", "D", "A", "C", "D", "A", "B", "B", "D"])

# --- PHAN II ---
print("\n--- PHAN II ---")
# Cau 1: f(x) = x^3 - 3x^2 - 9x + 2.
# a) Dong bien tren (3; +inf) -> DUNG (vi f' > 0 tren (-inf; -1) va (3; +inf))
# b) Dat cuc tieu tai x = -1 -> SAI (dat cuc dai tai x = -1, cuc tieu tai x = 3)
# c) I(1; -9) la tam doi xung -> DUNG (x_uon = 1, y(1) = 1 - 3 - 9 + 2 = -9)
# d) Tiep tuyen tai I co he so goc nho nhat bang -12 -> DUNG (k(x) = 3x^2 - 6x - 9 = 3(x-1)^2 - 12 >= -12)
# Dap an: D - S - D - D.

# Cau 2: y = (x^2 - 2x + 2)/(x - 1) = x - 1 + 1/(x-1).
# a) TCD x = 1, TCX y = x - 1 -> DUNG
# b) Giao diem hai tiem can la I(1; 0) -> DUNG
# c) y_CT > y_CD -> DUNG (y_CT = y(2) = 2, y_CD = y(0) = -2 => 2 > -2)
# d) Khoang cach tu goc toa do O(0;0) den TCX bang 1 -> SAI (d(O, x-y-1=0) = 1/sqrt(2) = sqrt(2)/2)
# Dap an: D - D - D - S.

# Cau 3: Kinh te: p(x) = 150 - 0.5x, C(x) = 0.25x^2 + 30x + 1200.
# R(x) = 150x - 0.5x^2
# P(x) = R(x) - C(x) = -0.75x^2 + 120x - 1200.
# a) Doanh thu R(x) = 150x - 0.5x^2 -> DUNG
# b) Khi san xuat 40 san pham moi ngay, doanh nghiep bi lo -> SAI (P(40) = -0.75*1600 + 4800 - 1200 = 2400 > 0, lai 2,4 trieu)
# c) Loi nhuan lon nhat khi x = 80 -> DUNG (P' = -1.5x + 120 = 0 <=> x = 80)
# d) Loi nhuan lon nhat bang 3,6 trieu dong -> DUNG (P(80) = 3600 nghin = 3,6 trieu)
# Dap an: D - S - D - D.

# Cau 4: s(t) = -t^3 + 9t^2 + 21t (0 <= t <= 10).
# v(t) = -3t^2 + 18t + 21, a(t) = -6t + 18.
# a) Van toc ban dau v(0) = 21 m/s -> DUNG
# b) Khi a(t) = 0 thi van toc dat gia tri lon nhat -> DUNG (t = 3, v_max = 48 m/s)
# c) Van toc luon tang tren khoang (0; 7) -> SAI (van toc tang tren (0; 3) va giam tren (3; 7))
# d) Vat dung lai tai thoi diem t = 7 giay -> DUNG (v(t) = 0 <=> t = 7)
# Dap an: D - D - S - D.

# --- PHAN III ---
print("\n--- PHAN III ---")
# Cau 1: Cho y = (x^2 + 2x - 2)/(x - 1) = x + 3 + 1/(x - 1).
# TCD d1: x = 1, TCX d2: y = x + 3. Giao diem I(1; 4).
# Tiep tuyen tai M(x0, y0) bat ky tren do thi cat d1 tai A, cat d2 tai B.
# Tinh dien tich tam giac IAB:
x0 = sp.Symbol('x0')
y0 = x0 + 3 + 1/(x0 - 1)
dy0 = 1 - 1/(x0 - 1)**2
# PTTT: y = dy0 * (x - x0) + y0
# Cat d1: x = 1 => y_A = dy0 * (1 - x0) + y0 = (1 - 1/(x0-1)^2)*(1 - x0) + x0 + 3 + 1/(x0-1)
y_A = sp.simplify(dy0 * (1 - x0) + y0)
print("y_A =", y_A) # should be x0 + 3 - (x0 - 1) + 2/(x0-1) = 4 + 2/(x0 - 1)
# Cat d2: y = x + 3 => dy0 * (x - x0) + y0 = x + 3
# dy0 * (x - x0) + x0 + 3 + 1/(x0 - 1) = x + 3
# (dy0 - 1) * x = dy0 * x0 - x0 - 1/(x0 - 1)
# solve for x_B:
x_B = sp.simplify(sp.solve(dy0 * (x - x0) + y0 - (x + 3), x)[0])
y_B = sp.simplify(x_B + 3)
print("x_B =", x_B, "y_B =", y_B)
# Tọa độ I(1; 4)
# IA = (0, y_A - 4), IB = (x_B - 1, y_B - 4)
# Dien tich tam giac IAB trong mat phang Oxy:
# S = 1/2 * |x_IA * y_IB - y_IA * x_IB| = 1/2 * |0 - (y_A - 4)*(x_B - 1)|
S_IAB = sp.simplify(sp.Rational(1, 2) * sp.Abs((y_A - 4) * (x_B - 1)))
print("Dien tich S_IAB =", S_IAB) # Bang 2! Dien tich = 2!

# Cau 2: y = (x^2 - 2mx + 3m - 2)/(x - 1). Tim so gia tri nguyen cua m in [-20; 20] de dong bien tren tung khoang xac dinh.
# y' = (x^2 - 2x - m + 2)/(x - 1)^2.
# Dong bien <=> Delta' = 1 - (-m + 2) = m - 1 <= 0 <=> m <= 1.
# m in [-20; 1] => co 1 - (-20) + 1 = 22 gia tri.
print("Cau 2: So gia tri m nguyen =", 1 - (-20) + 1)

# Cau 3: Mang nuoc hinh thang can a = 20, 2 ben b = 20. Goc nghieng alpha (do) de dien tich lon nhat:
# alpha = 60 do. Ket qua = 60.
print("Cau 3: Goc alpha =", 60)

# Cau 4: Dat cap tu nha may A den dao C.
# Khoang cach tren bo: 9 - x, duoi bien: sqrt(x^2 + 6^2).
# Chi phi f(x) = 30(9 - x) + 50*sqrt(x^2 + 36).
# Min tai x = 4.5 km.
# Diem S cach tram A la 9 - 4.5 = 4.5 km.
# Ket qua: 4,5.
print("Cau 4: AS =", 4.5)

# Cau 5: Khoang cach ngan nhat giua 2 diem thuoc 2 nhanh cua (C): y = (x^2 + x + 1)/(x + 1) = x + 1/(x+1).
# TCD: x = -1, TCX: y = x. Tam doi xung I(-1; -1).
# Voi diem M tren nhanh trai (x1 < -1) va N tren nhanh phai (x2 > -1).
# Dat u = x + 1. Voi M: u1 < 0, voi N: u2 > 0.
# y = u - 1 + 1/u.
# Toa do theo I(-1; -1): X = x + 1 = u, Y = y - (-1) = y + 1 = u + 1/u.
# Khoang cach giua M va N: MN >= 2 * min IM (vi M va N doi xung qua I se dat min).
# IM^2 = X^2 + Y^2 = u^2 + (u + 1/u)^2 = u^2 + u^2 + 2 + 1/u^2 = 2u^2 + 1/u^2 + 2.
# Theo AM-GM: 2u^2 + 1/u^2 >= 2*sqrt(2), dau bang khi 2u^2 = 1/u^2 <=> u^4 = 1/2 <=> u^2 = 1/sqrt(2) = sqrt(2)/2.
# Khi do IM^2_min = 2*sqrt(2) + 2.
# Khoang cach MN_min = 2 * IM_min = 2 * sqrt(2*sqrt(2) + 2).
val_MN = 2 * np.sqrt(2 * np.sqrt(2) + 2)
print("Cau 5: MN_min =", val_MN, "lam tron hang phan tram:", round(val_MN, 2))
# Lam tron: 4.39!

# Cau 6: Bang quang cao treo tren tuong:
# Mep duoi cach mat dat 2,6 m, nguoi mat cao 1,6 m => h1 = 1 m.
# Bang cao 3 m => mep tren cach mat dat 5,6 m => h2 = 4 m.
# Nguoi dung cach tuong x (m). Goc nhin theta lon nhat khi tan theta = (4/x - 1/x)/(1 + 4/x^2) = 3/(x + 4/x) max <=> x = sqrt(1 * 4) = 2 m.
# Ket qua: 2.
print("Cau 6: x =", 2)
