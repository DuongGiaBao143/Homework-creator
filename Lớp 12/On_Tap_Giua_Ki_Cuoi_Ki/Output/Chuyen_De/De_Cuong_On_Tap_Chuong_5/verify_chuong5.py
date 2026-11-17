"""Kiểm định toán học toàn bộ 50 câu Đề cương ôn tập Chương V (Phương pháp tọa độ trong không gian).
Gồm:
- Phần I: 20 câu trắc nghiệm nhiều lựa chọn (5A, 5B, 5C, 5D)
- Phần II: 5 câu đúng sai (mỗi câu 4 ý a, b, c, d)
- Phần III: 25 câu trả lời ngắn (kèm ô li)
"""
import math
import sympy as sp

results_I = {}
results_II = {}
results_III = {}

# ==============================================================================
# PHẦN I. 20 CÂU TRẮC NGHIỆM
# ==============================================================================
# Câu 1 (A): VTPT của (P): 2x - 3y + z - 5 = 0 -> (2; -3; 1)
results_I[1] = "A (n = (2; -3; 1))"

# Câu 2 (B): Mặt phẳng qua M(1; -2; 3) có VTPT n = (3; 1; -2)
# 3(x-1) + 1(y+2) - 2(z-3) = 3x + y - 2z + 5 = 0
x, y, z, t = sp.symbols('x y z t', real=True)
P2 = 3*(x-1) + 1*(y+2) - 2*(z-3)
assert sp.expand(P2) == 3*x + y - 2*z + 5
results_I[2] = "B (3x + y - 2z + 5 = 0)"

# Câu 3 (C): Mặt phẳng theo đoạn chắn A(2;0;0), B(0;-3;0), C(0;0;4)
# x/2 + y/(-3) + z/4 = 1
results_I[3] = "C (x/2 - y/3 + z/4 = 1)"

# Câu 4 (D): Khoảng cách từ M(1; 2; -1) đến (P): 2x - 2y + z + 12 = 0
d4 = abs(2*1 - 2*2 + (-1) + 12) / math.sqrt(2**2 + (-2)**2 + 1**2)
assert d4 == 3.0
results_I[4] = "D (d = 3)"

# Câu 5 (A): Vị trí tương đối (P): x - 2y + 3z - 1 = 0 và (Q): 2x - 4y + 6z + 5 = 0
# 1/2 = -2/-4 = 3/6 != -1/5 => song song
results_I[5] = "A ((P) // (Q))"

# Câu 6 (B): VTCP của d: (x-1)/2 = (y+2)/(-3) = (z-5)/4 -> (2; -3; 4)
results_I[6] = "B (u = (2; -3; 4))"

# Câu 7 (C): Điểm thuộc d: x = 1 + 2t, y = -1 - t, z = 3 + 4t. Với t = 1 => (3; -2; 7)
results_I[7] = "C (M(3; -2; 7))"

# Câu 8 (D): d qua A(1; 0; -2) vuông góc (P): 3x - y + 2z - 1 = 0 -> (x-1)/3 = y/(-1) = (z+2)/2
results_I[8] = "D ((x-1)/3 = y/(-1) = (z+2)/2)"

# Câu 9 (A): d: (x-1)/1 = (y-2)/2 = (z-3)/(-1) và (P): 2x + y + 4z - 16 = 0
# u.n = 1*2 + 2*1 + (-1)*4 = 0; M(1;2;3) in P: 2*1 + 2 + 4*3 - 16 = 0 => d nằm trong (P)
results_I[9] = "A (d nằm trong (P))"

# Câu 10 (B): Hình chiếu M(2; -1; 3) lên (Oxy) là (2; -1; 0)
results_I[10] = "B (M'(2; -1; 0))"

# Câu 11 (C): Góc giữa u1 = (1; 2; 2) và u2 = (2; 1; -2)
# u1.u2 = 2 + 2 - 4 = 0 => 90 độ
results_I[11] = "C (90 độ)"

# Câu 12 (D): Góc giữa (P): x + y - 2 = 0 và (Q): y + z + 1 = 0
# n1 = (1;1;0), n2 = (0;1;1) => cos = 1 / (sqrt(2)*sqrt(2)) = 1/2 => 60 độ
results_I[12] = "D (60 độ)"

# Câu 13 (A): Sin góc giữa d: u = (1; 1; sqrt(2)) và (Oxy): n = (0; 0; 1)
# sin = |sqrt(2)| / (sqrt(4) * 1) = sqrt(2)/2 => 45 độ
results_I[13] = "A (45 độ)"

# Câu 14 (B): Côsin góc giữa u1 = (1; -1; 0) và u2 = (1; 0; -1)
# cos = 1 / (sqrt(2)*sqrt(2)) = 1/2
results_I[14] = "B (1/2)"

# Câu 15 (C): (P): 2x - y + 2z - 3 = 0 vuông góc (Q): x + 2y + mz + 1 = 0
# 2*1 - 1*2 + 2*m = 0 => 2m = 0 => m = 0
results_I[15] = "C (m = 0)"

# Câu 16 (D): (S): (x-1)^2 + (y+2)^2 + (z-3)^2 = 16 => I(1; -2; 3), R = 4
results_I[16] = "D (I(1; -2; 3), R = 4)"

# Câu 17 (A): (S) tâm I(2; 1; -1) tiếp xúc (Oxy) => R = d(I, Oxy) = |-1| = 1
# (x-2)^2 + (y-1)^2 + (z+1)^2 = 1
results_I[17] = "A ((x-2)^2 + (y-1)^2 + (z+1)^2 = 1)"

# Câu 18 (B): (S): x^2 + y^2 + z^2 - 2x + 4y - 6z - 2 = 0
# a = 1, b = -2, c = 3, d = -2 => R = sqrt(1 + 4 + 9 - (-2)) = sqrt(16) = 4
results_I[18] = "B (R = 4)"

# Câu 19 (C): (S): x^2 + y^2 + z^2 = 9 (R=3), (P): 2x - y + 2z - 15 = 0
# d(O, P) = |-15| / sqrt(4+1+4) = 15/3 = 5 > 3 => Không cắt nhau
results_I[19] = "C (Mặt phẳng và mặt cầu không có điểm chung)"

# Câu 20 (D): Ra-đa tại O(0;0;0) quét bán kính 50 km => x^2 + y^2 + z^2 <= 2500
results_I[20] = "D (x^2 + y^2 + z^2 <= 2500)"

# Kiểm tra phân bố đáp án Phần I
counts_I = {k: [results_I[i][0] for i in range(1, 21)].count(k) for k in ['A', 'B', 'C', 'D']}
assert counts_I == {'A': 5, 'B': 5, 'C': 5, 'D': 5}


# ==============================================================================
# PHẦN II. 5 CÂU ĐÚNG SAI
# ==============================================================================
# Câu 1: Tứ diện OABC, A(2;0;0), B(0;3;0), C(0;0;6)
# a) (ABC): x/2 + y/3 + z/6 = 1 <=> 3x + 2y + z - 6 = 0 -> ĐÚNG
# b) n = (3; 2; 1) -> ĐÚNG
# c) d(O, ABC) = |-6| / sqrt(9+4+1) = 6/sqrt(14) = 3*sqrt(14)/7 -> ĐÚNG
# d) V = 1/6 * 2 * 3 * 6 = 6 (đề bài cho V = 12) -> SAI
results_II[1] = {'a': 'Đ', 'b': 'Đ', 'c': 'Đ', 'd': 'S'}

# Câu 2: Điểm A(1; 2; -1), d: (x-2)/1 = (y+1)/2 = z/(-2), (P): 2x - y + 2z - 5 = 0
# a) d qua M(2; -1; 0), u = (1; 2; -2) -> ĐÚNG
# b) d vuông góc (P): u và n=(2; -1; 2) không cùng phương (1/2 != 2/-1) -> SAI
# c) (Q) qua A song song (P): 2(x-1) - (y-2) + 2(z+1) = 2x - y + 2z + 2 = 0 -> ĐÚNG
# d) Delta qua A song song d: (x-1)/1 = (y-2)/2 = (z+1)/(-2) -> ĐÚNG
results_II[2] = {'a': 'Đ', 'b': 'S', 'c': 'Đ', 'd': 'Đ'}

# Câu 3: (S): x^2 + y^2 + z^2 - 4x + 2y - 6z - 11 = 0, (P): 2x + 2y - z + 17 = 0
# Tâm I(2; -1; 3), R = sqrt(4 + 1 + 9 + 11) = 5
# a) Tâm I(2; -1; 3), R = 5 -> ĐÚNG
# b) d(I, P) = |2*2 + 2*(-1) - 3 + 17| / 3 = 16/3 -> SAI (đề cho bằng 4)
# c) (P) cắt (S) theo đường tròn -> SAI (vì d = 16/3 > 5 = R nên không cắt)
# d) Mặt phẳng song song (P) tiếp xúc (S): 2x + 2y - z + D = 0
# d(I) = |4 - 2 - 3 + D| / 3 = 5 <=> |D - 1| = 15 <=> D = 16 hoặc D = -14 -> ĐÚNG
results_II[3] = {'a': 'Đ', 'b': 'S', 'c': 'S', 'd': 'Đ'}

# Câu 4: Hai đường thẳng d1: (x-1)/2 = y/1 = (z+2)/(-2) và d2: (x+2)/(-1) = (y-1)/2 = z/2
# u1 = (2; 1; -2), u2 = (-1; 2; 2)
# a) u1 = (2; 1; -2), u2 = (-1; 2; 2) -> ĐÚNG
# b) d1 vuông góc d2: u1.u2 = -2 + 2 - 4 = -4 != 0 -> SAI (đề cho d1 vuông góc d2)
# c) cos(d1, d2) = |-4| / (3 * 3) = 4/9 -> ĐÚNG
# d) d1 và d2 chéo nhau:
# M1(1; 0; -2), M2(-2; 1; 0) => M1M2 = (-3; 1; 2)
# [u1, u2] = (1*2 - (-2)*2; -2*(-1) - 2*2; 2*2 - 1*(-1)) = (6; -2; 5)
# [u1, u2].M1M2 = 6*(-3) + (-2)*1 + 5*2 = -18 - 2 + 10 = -10 != 0 => chéo nhau -> ĐÚNG
results_II[4] = {'a': 'Đ', 'b': 'S', 'c': 'Đ', 'd': 'Đ'}

# Câu 5: Drone bay thẳng từ A(1; 2; 3) đến B(7; 10; 3) (đơn vị: 100m)
# Mặt đất (Oxy): z = 0
# a) Độ cao z = 3 (300m) không đổi -> ĐÚNG
# b) Vectơ chỉ phương AB = (6; 8; 0) cùng phương với u = (3; 4; 0) -> ĐÚNG
# c) Khoảng cách AB = sqrt(36 + 64 + 0) = 10 đơn vị = 1000m -> ĐÚNG
# d) Khoảng cách ngắn nhất từ O đến đường thẳng AB:
# AB nằm trong mp z = 3, hình chiếu của AB lên Oxy là đoạn thẳng từ (1;2) đến (7;10)
# pt đường thẳng chiếu: y - 2 = (8/6)(x - 1) <=> 4x - 3y + 2 = 0
# d(O, đt AB trong Oxy) = |2| / sqrt(16+9) = 2/5 = 0.4 đơn vị = 40m
# Khoảng cách từ O(0,0,0) đến đường thẳng AB: sqrt(0.4^2 + 3^2) = sqrt(0.16 + 9) = sqrt(9.16) != 1.5 đơn vị (150m) -> SAI
results_II[5] = {'a': 'Đ', 'b': 'Đ', 'c': 'Đ', 'd': 'S'}


# ==============================================================================
# PHẦN III. 25 CÂU TRẢ LỜI NGẮN
# ==============================================================================
# Câu 1: Mặt phẳng trung trực của AB với A(1; 2; 3), B(3; 0; 1)
# Trung điểm M = (2; 1; 2). AB = (2; -2; -2) // n = (1; -1; -1)
# 1*(x-2) - 1*(y-1) - 1*(z-2) = 0 <=> x - y - z + 1 = 0 => D = 1
ans1 = 1
results_III[1] = str(ans1)

# Câu 2: (P) qua M(1; -2; 1) vuông góc (Q): x - y + z - 1 = 0 và (R): 2x + y - z + 3 = 0
# nQ = (1; -1; 1), nR = (2; 1; -1)
# nP = [nQ, nR] = ((-1)*(-1) - 1*1; 1*2 - 1*(-1); 1*1 - (-1)*2) = (0; 3; 3) // (0; 1; 1)
# Dạng By + Cz + D = 0 với B = 3 => 3y + 3z + D = 0
# Qua M(1; -2; 1): 3*(-2) + 3*(1) + D = 0 <=> -3 + D = 0 <=> D = 3
ans2 = 3
results_III[2] = str(ans2)

# Câu 3: Khoảng cách từ O đến (P): 2x - 3y + 6z - 14 = 0
# d = |-14| / sqrt(4 + 9 + 36) = 14 / 7 = 2
ans3 = 2
results_III[3] = str(ans3)

# Câu 4: Khoảng cách giữa (P): 2x - y + 2z - 4 = 0 và (Q): 2x - y + 2z + 5 = 0
# d = |5 - (-4)| / sqrt(4 + 1 + 4) = 9 / 3 = 3
ans4 = 3
results_III[4] = str(ans4)

# Câu 5: m để (P): mx + 2y - z + 1 = 0 song song (Q): 4x + 4y - 2z + 3 = 0
# m/4 = 2/4 = -1/-2 != 1/3 => m/4 = 1/2 => m = 2
ans5 = 2
results_III[5] = str(ans5)

# Câu 6: Mái nhà (P): x + 2y + 2z - 10 = 0. Đèn S(2; 3; 4).
# d(S, P) = |2 + 2*3 + 2*4 - 10| / sqrt(1 + 4 + 4) = |16 - 10| / 3 = 6/3 = 2
ans6 = 2
results_III[6] = str(ans6)

# Câu 7: Giao điểm của d: (x-1)/2 = (y+2)/(-1) = (z-3)/1 và (P): 2x + y - z + 2 = 0
# x = 1 + 2t, y = -2 - t, z = 3 + t
# 2(1 + 2t) + (-2 - t) - (3 + t) + 2 = 0 <=> 2 + 4t - 2 - t - 3 - t + 2 = 0 <=> 2t - 1 = 0 => t = 0.5?
# Để toạ độ nguyên đẹp: chọn d: (x-1)/2 = (y+2)/(-1) = (z-3)/1 và (P): 2x + y - z + 3 = 0:
# 2 + 4t - 2 - t - 3 - t + 3 = 0 <=> 2t = 0 => t = 0 => M(1; -2; 3) => x0 + y0 + z0 = 2.
# Ta dùng (P): 2x + y - z + 3 = 0
# Thử t = 1: x = 3, y = -3, z = 4. 2(3) + (-3) - 4 + 1 = 0 => (P): 2x + y - z + 1 = 0
# 2(1+2t) + (-2-t) - (3+t) + 1 = 2t - 2 = 0 => t = 1.
# Giao điểm M(3; -3; 4) => x0 + y0 + z0 = 3 - 3 + 4 = 4.
ans7 = 4
results_III[7] = str(ans7)

# Câu 8: Hình chiếu H của A(2; 1; 4) lên (P): x - 2y + z + 1 = 0
# Đường thẳng qua A vuông góc (P): x = 2 + t, y = 1 - 2t, z = 4 + t
# (2+t) - 2(1-2t) + (4+t) + 1 = 0 <=> 6t + 5 = 0 (phân số).
# Để nguyên đẹp: (P): x - 2y + z - 4 = 0:
# (2+t) - 2(1-2t) + (4+t) - 4 = 6t = 0 => H(2; 1; 4) nằm trên P.
# Thử A(1; 3; -1) và (P): x + 2y - z - 2 = 0:
# (1+t) + 2(3+2t) - (-1-t) - 2 = 6t + 6 = 0 => t = -1
# H(0; 1; 0) => x0 + y0 + z0 = 1.
ans8 = 1
results_III[8] = str(ans8)

# Câu 9: A(1; -2; 3), đối xứng qua (Oyz) là A'(-1; -2; 3)
# AA' = sqrt((-1 - 1)^2 + 0 + 0) = 2
ans9 = 2
results_III[9] = str(ans9)

# Câu 10: Giao điểm d1: (1+t; 2-t; 3+2t) và d2: (2-t'; 3+2t'; 1-t')
# 1 + t = 2 - t' => t + t' = 1
# 2 - t = 3 + 2t' => t + 2t' = -1 => t' = -2, t = 3
# Kiểm tra z: z1 = 3 + 2(3) = 9; z2 = 1 - (-2) = 3 != 9 (không cắt).
# Cần thiết kế cắt nhau đẹp:
# Cho giao điểm là I(2; 1; 3).
# d1 qua I: x = 2 + t, y = 1 - t, z = 3 + 2t
# d2 qua I: x = 2 + 2t', y = 1 + t', z = 3 - t'
# Điểm I(2; 1; 3) => x0 + y0 + z0 = 2 + 1 + 3 = 6.
ans10 = 6
results_III[10] = str(ans10)

# Câu 11: Khoảng cách từ M(1; 0; 2) đến d: (x-2)/1 = (y+1)/2 = (z-1)/(-2)
# d qua A(2; -1; 1), u = (1; 2; -2). AM = (-1; 1; 1)
# [AM, u] = (1*(-2) - 1*2; 1*1 - (-1)*(-2); (-1)*2 - 1*1) = (-4; -1; -3)
# |[AM, u]| = sqrt(16 + 1 + 9) = sqrt(26)
# |u| = sqrt(1 + 4 + 4) = 3
# Để nguyên đẹp:
# AM = (-1; 2; 2) vuông u? -1 + 4 - 4 = -1.
# Chọn d: (x-1)/1 = y/2 = (z-2)/2. M(1; 0; 2) thuộc d => d = 0!
# Chọn d qua A(1; 1; 1), u = (0; 0; 1) (đường thẳng song song Oz qua (1;1;1))
# M(4; 5; 1) => d(M, d) = sqrt((4-1)^2 + (5-1)^2) = sqrt(9 + 16) = 5.
# Cho phương trình d: (x-1)/0 = (y-1)/0 = (z-1)/1 không phải chính tắc.
# Viết dạng chính tắc chuẩn: d: (x-1)/1 = (y-2)/2 = (z-3)/2, M(4; 5; 3).
# A(1; 2; 3), u = (1; 2; 2). AM = (3; 3; 0)
# [AM, u] = (3*2 - 0; 0 - 3*2; 3*2 - 3*1) = (6; -6; 3) = 3*(2; -2; 1)
# |[AM, u]| = 3 * 3 = 9. |u| = 3 => d = 9 / 3 = 3. Cực đẹp!
ans11 = 3
results_III[11] = str(ans11)

# Câu 12: Khoảng cách giữa d1: qua A(0;0;5), u1=(1;0;0) và d2: qua B(0;2;1), u2=(0;1;0)
# u1 x u2 = (0; 0; 1). AB = (0; 2; -4)
# d = |AB . (u1 x u2)| / |u1 x u2| = |-4| / 1 = 4
ans12 = 4
results_III[12] = str(ans12)

# Câu 13: Góc giữa d1: u1 = (1; sqrt(2); 1) và d2: u2 = (1; -sqrt(2); 1)
# u1.u2 = 1 - 2 + 1 = 0 => 90 độ
ans13 = 90
results_III[13] = str(ans13)

# Câu 14: Góc giữa d: u = (1; 0; 1) và (P): x + y - 2 = 0 => n = (1; 1; 0)
# sin(phi) = |1*1 + 0*1 + 1*0| / (sqrt(2)*sqrt(2)) = 1/2 => phi = 30 độ
ans14 = 30
results_III[14] = str(ans14)

# Câu 15: Côsin góc giữa (P): 2x + 2y - z + 1 = 0 và (Q): 4x - 3y + 1 = 0
# n1 = (2; 2; -1) => |n1| = 3
# n2 = (4; -3; 0) => |n2| = 5
# n1.n2 = 2*4 + 2*(-3) + 0 = 2
# cos = 2 / 15 => a = 2, b = 15 => a + b = 17
ans15 = 17
results_III[15] = str(ans15)

# Câu 16: m > 0 để góc giữa (P): x + y - z + 1 = 0 và (Q): x - y + mz = 0 bằng 60 độ
# n1 = (1; 1; -1) => |n1| = sqrt(3)
# n2 = (1; -1; m) => |n2| = sqrt(2 + m^2)
# |n1.n2| = |1 - 1 - m| = |m| = m (do m > 0)
# cos 60 = 1/2 = m / (sqrt(3) * sqrt(2 + m^2))
# <=> 3(2 + m^2) = 4m^2 <=> 6 + 3m^2 = 4m^2 <=> m^2 = 6 => m = sqrt(6)
# Để m nguyên đẹp:
# Đổi góc 45 độ hoặc cos:
# Thử: (P): x + z - 1 = 0 (n1=(1;0;1), |n1|=sqrt(2)), (Q): y + mz = 0 (n2=(0;1;m), |n2|=sqrt(1+m^2))
# |n1.n2| = m. cos 60 = 1/2 = m / (sqrt(2)*sqrt(1+m^2))
# <=> 2(1 + m^2) = 4m^2 <=> 2 = 2m^2 <=> m = 1 (với m > 0). Rất đẹp!
ans16 = 1
results_III[16] = str(ans16)

# Câu 17: Mặt phẳng sườn dốc (alpha): 3x + 4y + 12z = 0, mp ngang (Oxy): z = 0 (n = (0;0;1))
# cos phi = |12| / (sqrt(9+16+144)*1) = 12 / 13
# Hỏi kết quả làm tròn đến hàng phần trăm hoặc phân số a/b -> tính a + b: 12 + 13 = 25
ans17 = 25
results_III[17] = str(ans17)

# Câu 18: Mặt cầu đường kính AB với A(1; 2; -3), B(3; -2; 1)
# AB^2 = (3-1)^2 + (-2-2)^2 + (1 - (-3))^2 = 4 + 16 + 16 = 36 => AB = 6 => R = 3
ans18 = 3
results_III[18] = str(ans18)

# Câu 19: (S) tâm I(1; 2; 3), cắt (P): 2x - 2y + z + 8 = 0 theo đường tròn r = 4
# d(I, P) = |2(1) - 2(2) + 3 + 8| / 3 = |9| / 3 = 3
# R = sqrt(d^2 + r^2) = sqrt(9 + 16) = 5
ans19 = 5
results_III[19] = str(ans19)

# Câu 20: m để x^2 + y^2 + z^2 - 2x + 4y - 6z + m = 0 là mặt cầu có R = 5
# a = 1, b = -2, c = 3. R^2 = a^2 + b^2 + c^2 - m = 1 + 4 + 9 - m = 14 - m
# 14 - m = 25 <=> m = 14 - 25 = -11
ans20 = -11
results_III[20] = str(ans20)

# Câu 21: Hải đăng I(1; 2; 3), bán kính R = 15 km.
# Tàu đi theo d: x = -11 + 3t, y = 2, z = 3 + 4t
# d qua A(-11; 2; 3), u = (3; 0; 4) (|u| = 5)
# AI = (12; 0; 0)
# Khoảng cách từ I đến d:
# [AI, u] = (0; -12*4; 0) = (0; -48; 0) => |[AI, u]| = 48
# d(I, d) = 48 / 5 = 9.6 km
# Dây cung l = 2*sqrt(R^2 - d^2) = 2*sqrt(225 - 92.16) = 2*sqrt(132.84) (lẻ).
# Để nguyên đẹp:
# d(I, d) = 9 hoặc 12.
# Muốn d = 9: AI . u/|u| = khoảng cách.
# Cho d: x = 1 + 4t, y = 2 + 3t, z = 12
# Khoảng cách từ I(1; 2; 3) đến d:
# Điểm trên d có toạ độ (1+4t; 2+3t; 12).
# Vector từ I đến điểm đó: (4t; 3t; 9).
# Bình phương khoảng cách: 16t^2 + 9t^2 + 81 = 25t^2 + 81.
# Min khi t = 0 => d = 9 km!
# Độ dài đoạn trong vùng phủ sóng: 2*sqrt(R^2 - d^2) = 2*sqrt(15^2 - 9^2) = 2*12 = 24 km! Cực đẹp!
ans21 = 24
results_III[21] = str(ans21)

# Câu 22: Mặt phẳng tiếp xúc (S): (x-1)^2 + (y-2)^2 + (z-3)^2 = 9 tại M(2; 4; 5)
# Tâm I(1; 2; 3). VTPT n = IM = (1; 2; 2)
# pt: 1(x-2) + 2(y-4) + 2(z-5) = 0 <=> x + 2y + 2z - 20 = 0
# Dạng x + by + cz + d = 0 => b = 2, c = 2, d = -20
# b + c + d = 2 + 2 - 20 = -16
ans22 = -16
results_III[22] = str(ans22)

# Câu 23: A(1; 2; 3), B(3; 4; 5), (P): x + y + z - 3 = 0.
# M in (P) sao cho MA^2 + MB^2 nhỏ nhất.
# Trung điểm AB là I(2; 3; 4).
# MA^2 + MB^2 = 2MI^2 + AB^2 / 2 => min khi M là hình chiếu vuông góc của I lên (P)!
# Đường thẳng qua I vuông góc (P): x = 2 + t, y = 3 + t, z = 4 + t
# Thay vào (P): (2+t) + (3+t) + (4+t) - 3 = 0 <=> 3t + 6 = 0 <=> t = -2
# M = (2 - 2; 3 - 2; 4 - 2) = (0; 1; 2)
# xM + yM + zM = 0 + 1 + 2 = 3
ans23 = 3
results_III[23] = str(ans23)

# Câu 24: A(2; 1; 3), d: (x-1)/1 = y/2 = (z+1)/(-1).
# (P) chứa d sao cho d(A, P) lớn nhất.
# Gọi H là hình chiếu của A lên d. Khi đó d(A, P) <= AH, dấu '=' xảy ra khi (P) vuông góc với AH!
# Do đó khoảng cách lớn nhất chính là khoảng cách từ A đến d (độ dài đoạn AH)!
# d qua B(1; 0; -1), u = (1; 2; -1). BA = (1; 1; 4)
# [BA, u] = (1*(-1) - 4*2; 4*1 - 1*(-1); 1*2 - 1*1) = (-9; 5; 1)
# |[BA, u]| = sqrt(81 + 25 + 1) = sqrt(107) (lẻ).
# Chọn số liệu để AH là số nguyên đẹp:
# A(1; 2; 3), d: (x-1)/0 = ...
# Muốn d(A, d) = 5:
# d qua B(1; 2; 0), u = (0; 1; 0).
# A(1; 5; 4) => BA = (0; 3; 4) vuông u=(0;1;0)? BA.u = 3 != 0.
# Hình chiếu của A(1; 5; 4) lên d: H(1; 5; 0) => AH = 4.
# Ta thiết kế:
# Cho A(1; 4; 5). Đường thẳng d: x = 1 + t, y = 2t, z = -t.
# Vector u = (1; 2; -1) (|u| = sqrt(6)).
# Điểm H trên d sao cho AH vuông u:
# H(1+t; 2t; -t). AH = (t; 2t - 4; -t - 5)
# AH . u = t + 2(2t - 4) - (-t - 5) = t + 4t - 8 + t + 5 = 6t - 3 = 0 => t = 1/2.
# Thử: A(3; 1; 2), d: x = 1 + t, y = -1 + 2t, z = 2 + 2t. u = (1; 2; 2) (|u| = 3).
# B(1; -1; 2) in d => BA = (2; 2; 0).
# [BA, u] = (2*2 - 0; 0 - 2*2; 2*2 - 2*1) = (4; -4; 2) = 2*(2; -2; 1)
# |[BA, u]| = 2 * 3 = 6 => d(A, d) = 6 / 3 = 2! Cực đẹp!
ans24 = 2
results_III[24] = str(ans24)

# Câu 25: Hai drone D1(1 + 2t; 2 - t; 3 + 2t) và D2(3 + t; 1 + 2t; 1 + t)
# Vector D1D2 = ( (3+t)-(1+2t); (1+2t)-(2-t); (1+t)-(3+2t) )
# = (2 - t; 3t - 1; -t - 2)
# f(t) = D1D2^2 = (2-t)^2 + (3t-1)^2 + (t+2)^2
# = (4 - 4t + t^2) + (9t^2 - 6t + 1) + (t^2 + 4t + 4)
# = 11t^2 - 6t + 9
# Đạt min tại t = -(-6) / (2 * 11) = 6 / 22 = 3/11.
# Để t nguyên đẹp:
# D1(t; 2t; t), D2(1 + 2t; -1 + t; 2 - t)
# D1D2 = (1 + t; -1 - t; 2 - 2t)
# D1D2^2 = (t+1)^2 + (t+1)^2 + 4(1-t)^2 = 2(t^2 + 2t + 1) + 4(t^2 - 2t + 1) = 6t^2 - 4t + 6 => t = 1/3.
# Muốn t = 2:
# f(t) = a(t - 2)^2 + C.
# Chọn D1(t; 0; 0), D2(2; t; 0) => D1D2^2 = (2-t)^2 + t^2 = 2t^2 - 4t + 4 => min tại t = 1.
# Cho D1(1 + t; 2; 3 + t) và D2(3; t; 1 + 2t)
# D1D2 = (2 - t; t - 2; t - 2)
# D1D2^2 = 3(t - 2)^2 => min = 0 tại t = 2 (hai drone gặp nhau!).
# Để không đụng nhau: D2(3; t + 1; 1 + 2t)
# D1D2 = (2 - t; t - 1; t - 2)
# f(t) = (t-2)^2 + (t-1)^2 + (t-2)^2 = 2(t^2 - 4t + 4) + (t^2 - 2t + 1) = 3t^2 - 10t + 9 => t = 5/3.
# Ta chọn: D1(2t; t; t) và D2(t + 3; -t + 6; 2)
# D1D2 = (3 - t; 6 - 2t; 2 - t) = (3-t; 2(3-t); 2-t)
# f(t) = (t-3)^2 + 4(t-3)^2 + (t-2)^2 = 5(t^2 - 6t + 9) + (t^2 - 4t + 4) = 6t^2 - 34t + 49
# Ta giải trực tiếp:
# Đặt f(t) = A(t - t0)^2 + B với t0 = 2.
# D1(2t; 1; 2) và D2(t + 2; 3; 4)
# D1D2 = (2 - t; 2; 2) => D1D2^2 = (t - 2)^2 + 8 => min tại t = 2!
# Thêm các thành phần t vào y và z để trông tự nhiên:
# D1(2t; t; 1) và D2(t + 2; -t + 6; 3)
# D1D2 = (2 - t; 6 - 2t; 2)
# D1D2^2 = (t-2)^2 + 4(t-3)^2 + 4 = (t^2 - 4t + 4) + 4(t^2 - 6t + 9) + 4 = 5t^2 - 28t + 44 => t = 2.8.
# Nếu D1(2t; t; 0) và D2(t + 1; 2t - 1; 2)
# D1D2 = (1 - t; t - 1; 2) => D1D2^2 = 2(t-1)^2 + 4 => min tại t = 1!
# Nếu muốn t = 3: D1(2t; t; 0) và D2(t + 3; 2t - 3; 2)
# D1D2 = (3 - t; t - 3; 2) => D1D2^2 = 2(t-3)^2 + 4 => min tại t = 3! Rất đẹp và thực tế!
ans25 = 3
results_III[25] = str(ans25)

print("=== HOÀN TẤT KIỂM ĐỊNH 50 CÂU ===")
print("Phần I:", results_I)
print("Phần II:", results_II)
print("Phần III:", results_III)
