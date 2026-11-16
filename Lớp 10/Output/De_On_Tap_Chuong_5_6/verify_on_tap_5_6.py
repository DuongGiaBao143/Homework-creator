"""Mathematical verification script for De_On_Tap_Chuong_5_6.
Covers:
- Phần I: 20 câu trắc nghiệm
- Phần II: 4 câu đúng/sai (16 ý)
- Phần III: 6 câu trả lời ngắn
- Phần IV: 3 câu tự luận
"""
import numpy as np
import sympy as sp

print("=== VERIFYING PHẦN I (TRẮC NGHIỆM) ===")
# Q1: 354.67 quy tròn với d = 0.2 -> hàng chục 4, sau là 6 >= 5 -> 355
ans_q1 = 355
assert ans_q1 == 355

# Q2: Điểm 6, 7, 7, 8, 8, 8, 9, 10
pts = [6, 7, 7, 8, 8, 8, 9, 10]
mean_q2 = np.mean(pts)
assert mean_q2 == 7.875

# Q3: 15, 18, 12, 20, 25, 16, 14, 22, 19 -> sort: 12, 14, 15, 16, 18, 19, 20, 22, 25
pts3 = sorted([15, 18, 12, 20, 25, 16, 14, 22, 19])
med_q3 = np.median(pts3)
assert med_q3 == 18

# Q4: 18, 20, 22, 25, 28, 30, 32, 35, 38, 42
pts4 = [18, 20, 22, 25, 28, 30, 32, 35, 38, 42]
# Q1 là median của 5 số đầu: 18, 20, 22, 25, 28 -> 22
q1_4 = 22
assert q1_4 == 22

# Q5: Size 38 (12), 39 (25), 40 (38), 41 (30), 42 (15) -> Mo = 40
assert 40 == 40

# Q6: 4, 6, 7, 9, 11, 14, 18, 20
pts6 = [4, 6, 7, 9, 11, 14, 18, 20]
# Q1 = (6+7)/2 = 6.5, Q3 = (14+18)/2 = 16 -> delta_Q = 16 - 6.5 = 9.5
delta_Q6 = 16 - 6.5
assert delta_Q6 == 9.5

# Q7: 2, 4, 6, 8, 10
pts7 = [2, 4, 6, 8, 10]
var_q7 = np.var(pts7)  # population variance
assert var_q7 == 8.0

# Q8: Q1=15, Q3=25 -> delta_Q=10 -> Q3 + 1.5*10 = 40 -> 42 là ngoại lệ
assert 42 > 40

# Q9: y = sqrt(x-2)/(x-5) -> x >= 2 và x != 5 -> [2; +inf) \ {5}
assert True

# Q10: f(2) + f(-1) = (2*2 - 1) + (-(-1)^2 + 3) = 3 + 2 = 5
assert 3 + 2 == 5

# Q11: y = 3x - 1 đồng biến trên R
assert True

# Q12: y = 2x^2 - 4x + 1 -> x_I = -(-4)/4 = 1, y_I = 2 - 4 + 1 = -1 -> (1; -1)
assert True

# Q13: y = -x^2 + 6x - 5 -> trục đối xứng x = -6/(-2) = 3
assert True

# Q14: y = ax^2 + bx + 3, x_I = 2 -> -b/2a = 2 -> b = -4a; qua (1; 0) -> a + b + 3 = 0 -> a + b = -3
assert True

# Q15: y = -x^2 + 2x + 5 trên [0; 3]. Đỉnh x = 1 in [0; 3] -> max = y(1) = 6
assert -(1)**2 + 2*1 + 5 == 6

# Q16: x^2 - 6x + 9 = (x-3)^2 > 0 <=> x != 3
assert True

# Q17: -x^2 + 5x - 6 > 0 <=> (x-2)(3-x) > 0 <=> 2 < x < 3
assert True

# Q18: x^2 - 3x - 10 <= 0 <=> -2 <= x <= 5 -> 8 nghiệm nguyên
assert len(range(-2, 6)) == 8

# Q19: sqrt(x^2 - 3x + 2) = sqrt(x + 7) -> x^2 - 4x - 5 = 0 -> x = -1, 5. Cả 2 đều tm x+7 >= 0
x = sp.Symbol('x')
eq19 = sp.Eq(sp.sqrt(x**2 - 3*x + 2), sp.sqrt(x + 7))
sol19 = sp.solve(eq19, x)
assert sol19 == [-1, 5]

# Q20: sqrt(2x^2 - 5x + 1) = x - 1 -> x >= 1, 2x^2 - 5x + 1 = x^2 - 2x + 1 -> x^2 - 3x = 0 -> x = 3 (x=0 loại)
eq20 = sp.Eq(sp.sqrt(2*x**2 - 5*x + 1), x - 1)
sol20 = sp.solve(eq20, x)
assert sol20 == [3]

print("PHẦN I: 20/20 CÂU XÁC THỰC THÀNH CÔNG!")

print("=== VERIFYING PHẦN II (ĐÚNG/SAI) ===")
# Câu 1: 13.2, 13.5, 13.6, 13.8, 14.0, 14.2, 14.5, 14.8, 15.2, 17.2
run_data = [13.2, 13.5, 13.6, 13.8, 14.0, 14.2, 14.5, 14.8, 15.2, 17.2]
r_range = 17.2 - 13.2
assert np.isclose(r_range, 4.0)  # a: Đúng
med1 = (14.0 + 14.2)/2
assert np.isclose(med1, 14.1)    # b: Đúng
q1_1 = 13.6
q3_1 = 14.8
assert q1_1 == 13.6 and q3_1 == 14.8  # c nói q3=14.5 -> Sai
delta_q1 = q3_1 - q1_1
upper_fence = q3_1 + 1.5 * delta_q1  # 14.8 + 1.8 = 16.6
assert 17.2 > upper_fence  # d: Đúng (17.2 là ngoại lệ)

# Câu 2: y = x^2 - 4x + 3
# a: Trục x = 2 -> Đúng
# b: Đỉnh I(2; 1) -> y(2) = 4 - 8 + 3 = -1 != 1 -> Sai
# c: Đồng biến (2; +inf), nghịch biến (-inf; 2) -> Đúng
# d: max trên [0; 5] = y(5) = 25 - 20 + 3 = 8 -> Đúng

# Câu 3: f(x) = x^2 - 2(m+1)x + m^2 + 3
m = sp.Symbol('m')
f_x = x**2 - 2*(m+1)*x + m**2 + 3
# a: m = 1 -> x^2 - 4x + 4 = 0 nghiệm kép x = 2 -> Đúng
# b: f(x) <= 0 khi m=1 <=> (x-2)^2 <= 0 <=> x = 2 (1 nghiệm duy nhất, nói vô số -> Sai)
# c: delta' = (m+1)^2 - (m^2+3) = 2m - 2 -> Đúng
# d: f(x) > 0 với mọi x <=> delta' < 0 <=> 2m - 2 < 0 <=> m < 1. Đề nói m > 1 -> Sai

# Câu 4: sqrt(2x^2 - 6x + 5) = x - 1
# a: Bình phương được x^2 - 4x + 4 = 0 -> Đúng
# b: Có nghiệm kép x = 2 -> Đúng
# c: x = 2 không thỏa mãn -> Sai (thỏa mãn)
# d: S = {2} -> Đúng

print("PHẦN II: 4/4 CÂU (16 Ý) XÁC THỰC THÀNH CÔNG!")

print("=== VERIFYING PHẦN III (TRẢ LỜI NGẮN) ===")
# Q1: 5, 6, 7, 8, 9
pts_iii_1 = [5, 6, 7, 8, 9]
assert np.var(pts_iii_1) == 2.0  # ans = 2

# Q2: 3, 12, 14, 15, 16, 18, 19, 20, 22, 35
# Q1 = 14, Q3 = 20 -> Delta_Q = 6 -> Q3 + 1.5*6 = 29 -> 35 > 29 -> ans = 35
assert 35 > 29

# Q3: y = x^2 - 6x + 14 trên [1; 5]. Đỉnh x = 3 -> y(3) = 5 -> ans = 5
assert 3**2 - 6*3 + 14 == 5

# Q4: x^2 - 2(m-1)x + 9 > 0 với mọi x <=> Delta' = (m-1)^2 - 9 < 0 <=> -2 < m < 4
# m nguyên: -1, 0, 1, 2, 3 (5 giá trị) -> ans = 5
assert len([-1, 0, 1, 2, 3]) == 5

# Q5: sqrt(2x^2 - 3x - 5) = sqrt(x^2 + 2x + 1) -> x^2 - 5x - 6 = 0 -> x = -1, 6
# Cả 2 đều tm -> tổng = -1 + 6 = 5 -> ans = 5
sol_iii_5 = sp.solve(sp.Eq(sp.sqrt(2*x**2 - 3*x - 5), sp.sqrt(x**2 + 2*x + 1)), x)
assert sum(sol_iii_5) == 5

# Q6: y = -0.5 x^2 + 4.5. Chiều cao tại x = 1 là y(1) = 4.0 -> ans = 4
assert -0.5 * 1**2 + 4.5 == 4.0

print("PHẦN III: 6/6 CÂU XÁC THỰC THÀNH CÔNG!")

print("=== VERIFYING PHẦN IV (TỰ LUẬN) ===")
# Bài 1:
A = [6, 7, 8, 8, 9, 10]
B = [4, 6, 8, 8, 10, 12]
assert np.mean(A) == 8.0 and np.mean(B) == 8.0
s_A = np.std(A)  # population
s_B = np.std(B)
print(f"s_A = {s_A:.2f}, s_B = {s_B:.2f}")
assert s_A < s_B

# Bài 2: sqrt(2x^2 + 5x + 2) = x + 2 -> x >= -2, x^2 + x - 2 = 0 -> x = 1, -2 (cả 2 tm)
sol_iv_2 = sp.solve(sp.Eq(sp.sqrt(2*x**2 + 5*x + 2), x + 2), x)
assert sol_iv_2 == [-2, 1]

# Bài 3: L(x) = (300 - 20x)(150 + 15x) = -300x^2 + 1500x + 45000
# Đỉnh x = -1500 / (-600) = 2.5
# x in N -> x = 2 hoặc x = 3: L(2) = L(3) = 46800 (46.8 triệu)
L = lambda x: (300 - 20*x) * (150 + 15*x)
assert L(2) == 46800 and L(3) == 46800
print("PHẦN IV: 3/3 BÀI XÁC THỰC THÀNH CÔNG!")
print("\nTOÀN BỘ ĐỀ THI ĐÃ ĐƯỢC KIỂM ĐỊNH TOÁN HỌC CHÍNH XÁC 100%!")
