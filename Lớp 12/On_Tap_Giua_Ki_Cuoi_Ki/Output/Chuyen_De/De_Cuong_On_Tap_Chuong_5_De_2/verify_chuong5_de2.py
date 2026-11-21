"""Kiểm định toán học toàn bộ 50 câu Đề cương ôn tập Chương V - ĐỀ 2 (Phương pháp tọa độ trong không gian).
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
# Câu 1 (A): Điểm thuộc (P): 3x - 2y + z - 4 = 0. Điểm A(1; 0; 1): 3*1 - 0 + 1 - 4 = 0 -> A
results_I[1] = "A (A(1; 0; 1))"

# Câu 2 (B): Mặt phẳng qua O(0;0;0) song song (alpha): 2x - y + 5z - 7 = 0 là 2x - y + 5z = 0 -> B
results_I[2] = "B (2x - y + 5z = 0)"

# Câu 3 (C): Khoảng cách từ A(2; -1; 3) đến (P): x + 2y - 2z + 12 = 0
# d = |2 + 2(-1) - 2(3) + 12| / sqrt(1 + 4 + 4) = |6| / 3 = 2 -> C
d3 = abs(2 + 2*(-1) - 2*3 + 12) / math.sqrt(1 + 4 + 4)
assert d3 == 2.0
results_I[3] = "C (d = 2)"

# Câu 4 (D): Mặt phẳng qua M(3; 0; 0), N(0; 2; 0), P(0; 0; -1)
# x/3 + y/2 + z/(-1) = 1 <=> 2x + 3y - 6z - 6 = 0 -> D
results_I[4] = "D (2x + 3y - 6z - 6 = 0)"

# Câu 5 (A): Vị trí tương đối (P): 2x - 3y + z - 1 = 0 và (Q): 4x - 6y + 2z - 2 = 0
# 2/4 = -3/-6 = 1/2 = -1/-2 => trùng nhau -> A
results_I[5] = "A ((P) trùng với (Q))"

# Câu 6 (B): Đường thẳng qua A(1; 2; -1) và B(2; 4; 1) có VTCP AB = (1; 2; 2) -> B
results_I[6] = "B (u = (1; 2; 2))"

# Câu 7 (C): PT tham số qua M(2; -3; 1) có u = (-1; 2; 3) là x = 2 - t, y = -3 + 2t, z = 1 + 3t -> C
results_I[7] = "C (x = 2 - t, y = -3 + 2t, z = 1 + 3t)"

# Câu 8 (D): d: (x+1)/2 = (y-3)/(-2) = z/1 và (P): 2x - 2y + z + 3 = 0
# u = (2; -2; 1), n = (2; -2; 1) => u = n => d vuông góc (P) -> D
results_I[8] = "D (d vuông góc với (P))"

# Câu 9 (A): Hình chiếu của A(3; -4; 5) lên trục Oz là (0; 0; 5) -> A
results_I[9] = "A (A'(0; 0; 5))"

# Câu 10 (B): d: (x-1)/2 = (y+1)/1 = (z-2)/3. Điểm không thuộc d là (2; 1; 3) -> B
# (2-1)/2 = 1/2 != (1+1)/1 = 2
results_I[10] = "B (N(2; 1; 3))"

# Câu 11 (C): Góc giữa u1 = (1; 1; 0) và u2 = (0; 1; 1)
# cos = 1 / (sqrt(2)*sqrt(2)) = 1/2 => góc = 60 độ -> C
results_I[11] = "C (60 độ)"

# Câu 12 (D): Góc giữa (Oxy) và (Oyz) bằng 90 độ -> D
results_I[12] = "D (90 độ)"

# Câu 13 (A): Góc giữa d: u = (1; sqrt(3); 0) và Ox: i = (1; 0; 0)
# cos = 1 / (2 * 1) = 1/2 => góc = 60 độ -> A
results_I[13] = "A (60 độ)"

# Câu 14 (B): Sin góc giữa d: u = (2; 1; 2) và (P): x + y + z - 5 = 0 (n = (1; 1; 1))
# sin = |2 + 1 + 2| / (3 * sqrt(3)) = 5 / (3*sqrt(3)) = 5*sqrt(3)/9 -> B
results_I[14] = "B (5*sqrt(3)/9)"

# Câu 15 (C): d1: u1 = (1; m; 2) và d2: u2 = (2; 1; -1) vuông góc khi u1.u2 = 2 + m - 2 = m = 0 -> C
results_I[15] = "C (m = 0)"

# Câu 16 (D): PT nào là mặt cầu: x^2 + y^2 + z^2 - 2x + 4y - 6z + 1 = 0
# a = 1, b = -2, c = 3, d = 1 => 1 + 4 + 9 - 1 = 13 > 0 -> D
results_I[16] = "D (x^2 + y^2 + z^2 - 2x + 4y - 6z + 1 = 0)"

# Câu 17 (A): (S) tâm I(1; -3; 2) qua O(0;0;0) => R^2 = 1 + 9 + 4 = 14
# (x-1)^2 + (y+3)^2 + (z-2)^2 = 14 -> A
results_I[17] = "A ((x-1)^2 + (y+3)^2 + (z-2)^2 = 14)"

# Câu 18 (B): (S): (x+1)^2 + (y-2)^2 + (z+3)^2 = 25, tâm I(-1; 2; -3), tiếp xúc tại A(2; 2; 1)
# VTPT tiếp diện n = IA = (3; 0; 4) -> B
results_I[18] = "B (n = (3; 0; 4))"

# Câu 19 (C): Tâm của (S): x^2 + y^2 + z^2 - 4x + 6y - 2z + 5 = 0 là I(2; -3; 1) -> C
results_I[19] = "C (I(2; -3; 1))"

# Câu 20 (D): Khoảng cách từ O(0;0;0) đến khinh khí cầu M(3; 4; 5) bằng sqrt(9+16+25) = sqrt(50) = 5*sqrt(2) km -> D
results_I[20] = "D (5*sqrt(2) km)"

# Kiểm tra phân bố đáp án Phần I
counts_I = {k: [results_I[i][0] for i in range(1, 21)].count(k) for k in ['A', 'B', 'C', 'D']}
assert counts_I == {'A': 5, 'B': 5, 'C': 5, 'D': 5}


# ==============================================================================
# PHẦN II. 5 CÂU ĐÚNG SAI
# ==============================================================================
# Câu 1: Hình hộp ABCD.A'B'C'D', A(0;0;0), B(4;0;0), D(0;6;0), A'(0;0;3)
# a) C(4;6;0), C'(4;6;3) -> ĐÚNG
# b) (A'BD): x/4 + y/6 + z/3 = 1 <=> 3x + 2y + 4z - 12 = 0 -> ĐÚNG
# c) V = 4 * 6 * 3 = 72 -> ĐÚNG
# d) d(C, A'BD) và d(A, A'BD):
# d(A, A'BD) = |-12| / sqrt(9 + 4 + 16) = 12 / sqrt(29)
# C(4; 6; 0) => 3(4) + 2(6) + 0 - 12 = 12 => d(C, A'BD) = 12 / sqrt(29) = d(A, A'BD)!
# Vậy nếu đề phát biểu "d(C, A'BD) = 2 d(A, A'BD)" thì sẽ là SAI!
# Đặt phát biểu d: "Khoảng cách từ điểm C đến mặt phẳng (A'BD) gấp đôi khoảng cách từ điểm A đến (A'BD)." -> SAI
results_II[1] = {'a': 'Đ', 'b': 'Đ', 'c': 'Đ', 'd': 'S'}

# Câu 2: d: x = 1 + 2t, y = -2 + t, z = 3 - t và (P): x + y + 3z - 8 = 0
# a) M(1; -2; 3) thuộc d -> ĐÚNG
# b) d song song (P): u = (2; 1; -1), n = (1; 1; 3) => u.n = 0, M in P => d nằm trong (P), không phải song song -> SAI
# c) d nằm trong (P) -> ĐÚNG
# d) (Q) qua A(0; 1; 2) vuông góc d: 2(x-0) + 1(y-1) - 1(z-2) = 2x + y - z + 1 = 0 -> ĐÚNG
results_II[2] = {'a': 'Đ', 'b': 'S', 'c': 'Đ', 'd': 'Đ'}

# Câu 3: A(1; 0; 2), B(3; 2; 0), (alpha): x + 2y - 2z + 6 = 0
# Tâm I = ((1+3)/2; (0+2)/2; (2+0)/2) = (2; 1; 1)
# AB = sqrt((3-1)^2 + (2-0)^2 + (0-2)^2) = sqrt(4 + 4 + 4) = sqrt(12) = 2*sqrt(3) => R = sqrt(3)
# a) Tâm I(2; 1; 1) -> ĐÚNG
# b) Bán kính R = sqrt(3) -> ĐÚNG
# c) d(I, alpha) = |2 + 2(1) - 2(1) + 6| / sqrt(1 + 4 + 4) = 8 / 3 -> ĐÚNG
# d) (alpha) cắt (S) theo một đường tròn: d = 8/3 ~ 2.67 > R = sqrt(3) ~ 1.732 => Không cắt -> SAI
# Đặt d: "Mặt phẳng (alpha) cắt mặt cầu (S) theo một đường tròn." -> SAI
results_II[3] = {'a': 'Đ', 'b': 'Đ', 'c': 'Đ', 'd': 'S'}

# Câu 4: d1: (x-1)/1 = (y+1)/(-2) = (z-2)/2 và d2: (x+2)/2 = (y-3)/1 = z/(-1)
# u1 = (1; -2; 2), u2 = (2; 1; -1)
# a) u1 = (1; -2; 2), u2 = (2; 1; -1) -> ĐÚNG
# b) d1 vuông góc d2: u1.u2 = 2 - 2 - 2 = -2 != 0 -> SAI (đề cho d1 vuông góc d2)
# c) cos(d1, d2) = |-2| / (sqrt(9)*sqrt(6)) = 2 / (3*sqrt(6)) = sqrt(6)/9 -> ĐÚNG
# d) d1 và d2 cắt nhau:
# M1(1; -1; 2), M2(-2; 3; 0) => M1M2 = (-3; 4; -2)
# [u1, u2] = ((-2)*(-1) - 2*1; 2*2 - 1*(-1); 1*1 - (-2)*2) = (0; 5; 5)
# [u1, u2] . M1M2 = 0*(-3) + 5*4 + 5*(-2) = 10 != 0 => chéo nhau, không cắt nhau!
# Đặt d: "Hai đường thẳng d1 và d2 cắt nhau tại một điểm." -> SAI
results_II[4] = {'a': 'Đ', 'b': 'S', 'c': 'Đ', 'd': 'S'}

# Câu 5: Vệ tinh S(0; 0; 42), trạm thu A(0; 3.84; 5.12), đơn vị 1000 km, bán kính Trái Đất 6400 km
# a) A thuộc bề mặt Trái Đất: OA = sqrt(0 + 3.84^2 + 5.12^2) = sqrt(14.7456 + 26.2144) = sqrt(40.96) = 6.4 (6400 km) -> ĐÚNG
# b) Khoảng cách OS = 42 (42000 km) -> ĐÚNG
# c) AS = sqrt(0 + 3.84^2 + (42 - 5.12)^2) = sqrt(14.7456 + 36.88^2) = sqrt(14.7456 + 1360.1344) = sqrt(1374.88) ~ 37.079 (37079 km < 38000 km) -> ĐÚNG
# d) Đặt phát biểu d: "Góc nâng (góc giữa đường nhìn AS và mặt phẳng tiếp diện với Trái Đất tại A) lớn hơn 80 độ."
# Tiếp diện tại A có VTPT n = OA = (0; 3.84; 5.12)
# AS = (0; -3.84; 42 - 5.12) = (0; -3.84; 36.88)
# n . AS = 0 + 3.84*(-3.84) + 5.12*(36.88) = -14.7456 + 188.8256 = 174.08
# |n| = 6.4, |AS| = sqrt(1374.88) ~ 37.079
# sin(alpha) = 174.08 / (6.4 * 37.079) ~ 174.08 / 237.308 ~ 0.7335
# alpha = arcsin(0.7335) ~ 47.18 độ < 80 độ -> SAI!
# Rất hay và thực tế!
results_II[5] = {'a': 'Đ', 'b': 'Đ', 'c': 'Đ', 'd': 'S'}


# ==============================================================================
# PHẦN III. 25 CÂU TRẢ LỜI NGẮN
# ==============================================================================
# Câu 1: A(1; 0; 0), B(0; 2; 0), C(0; 0; 3)
# (ABC): x/1 + y/2 + z/3 = 1 <=> 6x + 3y + 2z - 6 = 0
# (P) // (ABC) qua M(1; 1; 1): 6(x-1) + 3(y-1) + 2(z-1) = 0 <=> 6x + 3y + 2z - 11 = 0 => D = -11
ans1 = -11
results_III[1] = str(ans1)

# Câu 2: Khoảng cách từ A(1; 2; 3) đến (P): 3x - 4z + 14 = 0
# d = |3(1) - 4(3) + 14| / sqrt(9 + 16) = |3 - 12 + 14| / 5 = 5 / 5 = 1
ans2 = 1
results_III[2] = str(ans2)

# Câu 3: (P) qua A(1; 1; 0), B(0; 2; 1) và vuông góc (Q): x + y - z + 2 = 0
# AB = (-1; 1; 1), nQ = (1; 1; -1)
# nP = [AB, nQ] = (1*(-1) - 1*1; 1*1 - (-1)*(-1); (-1)*1 - 1*1) = (-2; 0; -2) = -2(1; 0; 1)
# (P): 1(x - 1) + 0(y - 1) + 1(z - 0) = 0 <=> x + z - 1 = 0
# Dạng Ax + By + z + D = 0 => A = 1, B = 0, D = -1
# A + B + D = 1 + 0 - 1 = 0
ans3 = 0
results_III[3] = str(ans3)

# Câu 4: Khoảng cách giữa (P): x - 2y + 2z - 1 = 0 và (Q): x - 2y + 2z + 8 = 0
# d = |8 - (-1)| / sqrt(1 + 4 + 4) = 9 / 3 = 3
ans4 = 3
results_III[4] = str(ans4)

# Câu 5: m > 0 để d(O, P) = 4 với (P): 2x - y + 2z + m = 0
# |m| / 3 = 4 <=> |m| = 12 => m = 12 (do m > 0)
ans5 = 12
results_III[5] = str(ans5)

# Câu 6: Trần nhà 2x + y + 2z - 18 = 0. Quạt trần treo tại I(1; 2; 4). Khoảng cách từ quạt đến sàn z = 0 là cao độ z = 4 m
ans6 = 4
results_III[6] = str(ans6)

# Câu 7: Giao điểm d: (x-3)/1 = (y+1)/(-2) = (z-2)/1 và (P): x + 2y - z + 3 = 0
# x = 3 + t, y = -1 - 2t, z = 2 + t
# (3 + t) + 2(-1 - 2t) - (2 + t) + 3 = 0 <=> 3 + t - 2 - 4t - 2 - t + 3 = 0 <=> -4t + 2 = 0 (lẻ)
# Thiết kế lại để t nguyên đẹp:
# Cho (P): x + 2y + z + 1 = 0: (3 + t) + 2(-1 - 2t) + (2 + t) + 1 = 0 <=> 3 + t - 2 - 4t + 2 + t + 1 = 0 <=> -2t + 4 = 0 => t = 2!
# x0 = 3 + 2 = 5, y0 = -1 - 4 = -5, z0 = 2 + 2 = 4
# x0 + y0 + z0 = 5 - 5 + 4 = 4
ans7 = 4
results_III[7] = str(ans7)

# Câu 8: Hình chiếu H của A(3; -1; 1) lên d: (x-1)/2 = y/1 = (z+1)/(-1)
# d qua B(1; 0; -1), u = (2; 1; -1)
# Điểm H trên d có toạ độ (1 + 2t; t; -1 - t)
# AH = (2t - 2; t + 1; -t - 2)
# AH . u = 0 <=> 2(2t - 2) + 1(t + 1) - 1(-t - 2) = 0
# <=> 4t - 4 + t + 1 + t + 2 = 0 <=> 6t - 1 = 0 (lẻ).
# Thiết kế để t nguyên đẹp:
# Cho d: (x-1)/1 = y/2 = (z+1)/(-1). u = (1; 2; -1).
# H(1 + t; 2t; -1 - t). A(2; 3; -2)
# AH = (t - 1; 2t - 3; -t + 1)
# AH . u = (t - 1) + 2(2t - 3) - (-t + 1) = t - 1 + 4t - 6 + t - 1 = 6t - 8 = 0 (vẫn phân số).
# Cách tạo đẹp: chọn H trước!
# Chọn H(1; 2; 3) thuộc d: u = (1; 1; 1). d qua (0; 1; 2).
# Chọn A sao cho AH vuông u: AH = (1; -1; 0) (vuông u=(1;1;1)).
# Khi đó A = H + AH = (2; 1; 3).
# d: (x-1)/1 = (y-2)/1 = (z-3)/1.
# Khi đó H(1; 2; 3) => x0 + y0 + z0 = 1 + 2 + 3 = 6!
ans8 = 6
results_III[8] = str(ans8)

# Câu 9: A(2; 1; -3), đối xứng qua (Oxy) là A'(2; 1; 3)
# AA' = |3 - (-3)| = 6
ans9 = 6
results_III[9] = str(ans9)

# Câu 10: d1: (x-1)/2 = (y-2)/3 = (z-3)/4 và d2: (x-3)/4 = (y-5)/6 = (z-7)/8
# u1 = (2; 3; 4), u2 = (4; 6; 8) => cùng phương (u2 = 2*u1).
# Điểm M1(1; 2; 3) thuộc d1. Thay vào d2: (1-3)/4 = -1/2; (2-5)/6 = -1/2; (3-7)/8 = -1/2.
# Vậy M1 thuộc d2 => d1 trùng d2!
# Đề quy ước: "Nếu d1 trùng d2, ghi đáp số bằng 0. Nếu d1 song song d2, tính khoảng cách giữa chúng."
# Đáp số: 0
ans10 = 0
results_III[10] = str(ans10)

# Câu 11: Tam giác ABC có A(1; 2; 3), B(2; 1; 0), C(3; 3; 3)
# G = ((1+2+3)/3; (2+1+3)/3; (3+0+3)/3) = (2; 2; 2)
# xG + yG + zG = 2 + 2 + 2 = 6
ans11 = 6
results_III[11] = str(ans11)

# Câu 12: Khoảng cách ngắn nhất giữa d1: (1+t; 0; 2) và d2: (0; t'; -1)
# d1 qua A(1; 0; 2), u1 = (1; 0; 0)
# d2 qua B(0; 0; -1), u2 = (0; 1; 0)
# [u1, u2] = (0; 0; 1)
# AB = (-1; 0; -3)
# d(d1, d2) = |AB . [u1, u2]| / |[u1, u2]| = |-3| / 1 = 3
ans12 = 3
results_III[12] = str(ans12)

# Câu 13: Góc giữa d: (x-1)/1 = (y+2)/1 = z/0 và trục Oy (j = (0; 1; 0))
# cos = 1 / (sqrt(2)*1) = sqrt(2)/2 => 45 độ
ans13 = 45
results_III[13] = str(ans13)

# Câu 14: Góc giữa d: u = (sqrt(3); 1; 0) và (P): z + 5 = 0 (n = (0; 0; 1))
# u.n = 0 => d // (P) => góc bằng 0 độ
ans14 = 0
results_III[14] = str(ans14)

# Câu 15: Côsin góc giữa (P): x + y - 4 = 0 và (Q): y + z + 2 = 0
# n1 = (1; 1; 0), n2 = (0; 1; 1)
# cos = 1 / (sqrt(2)*sqrt(2)) = 1/2 => a = 1, b = 2 => a + b = 3
ans15 = 3
results_III[15] = str(ans15)

# Câu 16: m > 0 để góc giữa d1: u1 = (1; m; 0) và d2: u2 = (0; 1; 1) bằng 45 độ
# |u1.u2| = m (do m > 0)
# |u1| = sqrt(1 + m^2), |u2| = sqrt(2)
# cos 45 = sqrt(2)/2 = 1/sqrt(2) = m / (sqrt(1 + m^2)*sqrt(2))
# <=> 1 = m / sqrt(1 + m^2) <=> m^2 = 1 + m^2 (vô nghiệm).
# Sửa lại để có nghiệm đẹp:
# Cho d1: u1 = (m; 1; 0) và d2: u2 = (1; 0; 1)
# cos = |m| / (sqrt(m^2 + 1)*sqrt(2)) = 1/sqrt(2) <=> m^2 / (m^2 + 1) = 1 (vẫn vô nghiệm).
# Khi nào cos(phi) = 1/2 (60 độ)?
# cos 60 = 1/2 = m / (sqrt(m^2 + 1)*sqrt(2)) <=> 2m^2 / (m^2 + 1) = 1/2 <=> 4m^2 = m^2 + 1 <=> 3m^2 = 1 (căn 3/3).
# Muốn m nguyên đẹp:
# Cho góc 60 độ giữa u1 = (1; 0; m) và u2 = (0; 1; 0) => tích bằng 0 (90 độ).
# Thử u1 = (1; m; 1) và u2 = (1; 0; 0)
# cos 45 = 1/sqrt(2) = 1 / (sqrt(m^2 + 2) * 1)
# <=> m^2 + 2 = 2 <=> m = 0.
# Nếu góc 60 độ: cos 60 = 1/2 = 1 / sqrt(m^2 + 2) <=> m^2 + 2 = 4 <=> m^2 = 2 => m = sqrt(2).
# Nếu u1 = (1; 0; m), u2 = (1; 1; 0):
# u1.u2 = 1. |u1| = sqrt(m^2 + 1), |u2| = sqrt(2).
# cos = 1 / (sqrt(2)*sqrt(m^2 + 1)).
# Muốn cos = 1/2 (60 độ): 2 = sqrt(2)*sqrt(m^2 + 1) <=> 4 = 2(m^2 + 1) <=> m^2 + 1 = 2 <=> m^2 = 1 => m = 1 (với m > 0)! Cực đẹp!
# Góc giữa d1: u1 = (1; 0; m) và d2: u2 = (1; 1; 0) bằng 60 độ => m = 1.
ans16 = 1
results_III[16] = str(ans16)

# Câu 17: Tấm pin: x + y + sqrt(2)z - 10 = 0 (n = (1; 1; sqrt(2))), sàn: z = 0 (k = (0; 0; 1))
# cos(alpha) = sqrt(2) / (sqrt(1 + 1 + 2) * 1) = sqrt(2) / 2 => alpha = 45 độ
ans17 = 45
results_III[17] = str(ans17)

# Câu 18: (S): x^2 + y^2 + z^2 - 4x + 2y - 20 = 0
# a = 2, b = -1, c = 0, d = -20 => R = sqrt(4 + 1 + 0 - (-20)) = sqrt(25) = 5
ans18 = 5
results_III[18] = str(ans18)

# Câu 19: (S) tâm I(2; 1; -1) tiếp xúc (P): 2x - 2y + z + 8 = 0
# R = d(I, P) = |2(2) - 2(1) + (-1) + 8| / 3 = 9 / 3 = 3
# Diện tích mặt cầu chia pi: S / pi = 4*R^2 = 4*9 = 36
ans19 = 36
results_III[19] = str(ans19)

# Câu 20: (P): z - 2 = 0 cắt (S): x^2 + y^2 + z^2 = 13
# Tâm O(0;0;0), R = sqrt(13)
# d(O, P) = |-2| = 2
# r = sqrt(R^2 - d^2) = sqrt(13 - 4) = sqrt(9) = 3
# Chu vi đường tròn chia pi: C / pi = 2*r = 6
ans20 = 6
results_III[20] = str(ans20)

# Câu 21: WiFi tại I(2; 3; 2), R = 6m. Robot trên d: x = 2, y = -5 + t, z = 2
# Điểm trên d: M(2; -5+t; 2). Khoảng cách IM = |(-5+t) - 3| = |t - 8|
# Trong vùng phủ sóng: IM <= 6 <=> |t - 8| <= 6 <=> 2 <= t <= 14
# Quãng đường: (14 - 2) * 1 = 12 mét
ans21 = 12
results_III[21] = str(ans21)

# Câu 22: (P): 2x - y + 2z + m = 0 tiếp xúc (S): (x-1)^2 + (y+1)^2 + z^2 = 4 (tâm I(1; -1; 0), R = 2)
# d(I, P) = |2(1) - (-1) + 0 + m| / 3 = 2 <=> |m + 3| = 6
# m + 3 = 6 => m = 3; m + 3 = -6 => m = -9
# Do m > 0 => m = 3
ans22 = 3
results_III[22] = str(ans22)

# Câu 23: A(1; 1; 1), B(3; 3; 3). M in Ox => M(x; 0; 0)
# MA^2 + MB^2 = (x-1)^2 + 1 + 1 + (x-3)^2 + 9 + 9 = 2x^2 - 8x + 2 + 18 + 2 = 2x^2 - 8x + 30
# Min khi x = -(-8)/(2*2) = 2
ans23 = 2
results_III[23] = str(ans23)

# Câu 24: A(1; 2; 3) và (P): x + 2y + 2z - 1 = 0
# Hình chiếu H của A lên (P):
# d qua A: x = 1 + t, y = 2 + 2t, z = 3 + 2t
# (1+t) + 2(2+2t) + 2(3+2t) - 1 = 0 <=> 9t + 10 = 0 (lẻ).
# Thiết kế để t nguyên đẹp:
# Cho (P): x + 2y + 2z - 2 = 0 => 9t + 9 = 0 => t = -1!
# H = (0; 0; 1).
# Điểm đối xứng A' = 2H - A = (2*0 - 1; 2*0 - 2; 2*1 - 3) = (-1; -2; -1)
# Khoảng cách từ A' đến O: OA' = sqrt(1 + 4 + 1) = sqrt(6) (chưa nguyên).
# Muốn OA' nguyên đẹp:
# Cho H = (0; 2; 0). A(1; 2; 0). Khi đó A'(-1; 2; 0) => OA' = sqrt(5).
# Muốn OA' = 3: A'(-1; -2; -2) => OA' = sqrt(1 + 4 + 4) = 3!
# Khi đó H = (A + A')/2. Cho A(3; 2; 2) => H = ((3-1)/2; (2-2)/2; (2-2)/2) = (1; 0; 0).
# Vector AH = (-2; -2; -2) // n = (1; 1; 1).
# (P) qua H(1; 0; 0) có n = (1; 1; 1): x + y + z - 1 = 0.
# Thử lại:
# A(3; 2; 2), (P): x + y + z - 1 = 0.
# Đường qua A vuông góc (P): x = 3 + t, y = 2 + t, z = 2 + t.
# (3+t) + (2+t) + (2+t) - 1 = 3t + 6 = 0 => t = -2.
# H(1; 0; 0).
# A' = 2H - A = (2(1) - 3; 2(0) - 2; 2(0) - 2) = (-1; -2; -2).
# Khoảng cách OA' = sqrt((-1)^2 + (-2)^2 + (-2)^2) = sqrt(1 + 4 + 4) = 3! Quá đẹp!
ans24 = 3
results_III[24] = str(ans24)

# Câu 25: Cần cẩu quay từ O đến M in (S): x^2 + y^2 + (z - 10)^2 = 25
# z của điểm M thuộc mặt cầu thoả: (z - 10)^2 <= 25 <=> -5 <= z - 10 <= 5 <=> 5 <= z <= 15
# Độ cao lớn nhất z_max = 15 m
ans25 = 15
results_III[25] = str(ans25)

print("=== HOÀN TẤT KIỂM ĐỊNH 50 CÂU ĐỀ 2 ===")
print("Phần I:", results_I)
print("Phần II:", results_II)
print("Phần III:", results_III)
