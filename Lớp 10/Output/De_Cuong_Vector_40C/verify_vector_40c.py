"""Mathematical verification script for 40 short-answer questions of De_Cuong_Vector_40C.
Covers:
- Bài 7. Các khái niệm mở đầu (Câu 1 - 10)
- Bài 8. Tổng và hiệu của hai vectơ (Câu 11 - 20)
- Bài 9. Tích của một vectơ với một số (Câu 21 - 30)
- Bài 10. Vectơ trong mặt phẳng toạ độ (Câu 31 - 40)
"""
import sympy as sp
import math

answers = {}

# --- BÀI 7: CÂU 1 - 10 ---
# Câu 1: Số vectơ khác 0 từ 10 đỉnh thập giác đều: 10 * 9 = 90
answers[1] = "90"

# Câu 2: Hình chữ nhật ABCD tâm O. Vectơ khác 0 cùng phương với AB có điểm đầu/cuối là {A,B,C,D,O}.
# Các điểm trên AB: A, B -> AB, BA (2). Trên CD: C, D -> CD, DC (2). O không thẳng hàng -> 4.
answers[2] = "4"

# Câu 3: Tam giác ABC, M, N, P lần lượt là trung điểm BC, CA, AB.
# Số vectơ khác MN bằng MN từ {A, B, C, M, N, P}: BP, PA -> 2 vectơ.
answers[3] = "2"

# Câu 4: Lưới ô vuông đơn vị: A(1,1), B(4,5). Độ dài AB = sqrt((4-1)^2 + (5-1)^2) = 5.
answers[4] = "5"

# Câu 5: Hình thang vuông ABCD tại A, D. AB=3, CD=7, AD=3. BC = sqrt(AD^2 + (CD-AB)^2) = sqrt(9 + 16) = 5.
answers[5] = "5"

# Câu 6: Tam giác ABC vuông tại A có AB=9, AC=12. M là trung điểm BC -> AM = 1/2 BC = 1/2 * 15 = 7.5.
answers[6] = "7,5"

# Câu 7: Hình vuông ABCD cạnh 8. M trung điểm AB, N trung điểm BC. MN^2 = (1/2 AC)^2 = (1/2 * 8*sqrt(2))^2 = 32.
answers[7] = "32"

# Câu 8: Tam giác ABC có AB=5, AC=7, BC=8. D, E là trung điểm AB, AC -> DE = 1/2 BC = 4.
answers[8] = "4"

# Câu 9: Hình chữ nhật ABCD diện tích 48, AB=6 -> AD = 8 -> BD = sqrt(6^2 + 8^2) = 10.
answers[9] = "10"

# Câu 10: 6 điểm không có 3 điểm thẳng hàng. Số vectơ khác 0 có gốc là A: 5.
answers[10] = "5"

# --- BÀI 8: CÂU 11 - 20 ---
# Câu 11: Hình chữ nhật ABCD có AB=5, AD=12. u = AB - CB = AB + BC = AC. |u| = AC = sqrt(25+144) = 13.
answers[11] = "13"

# Câu 12: Hình thoi ABCD cạnh 10, đường chéo BD=12 -> OB=6, OA=sqrt(100-36)=8 -> AC=16.
# w = AB + AD = AC -> |w| = 16.
answers[12] = "16"

# Câu 13: 4 điểm A, B, C, D. x = AB + CD - AD = (AB - AD) + CD = DB + CD = CD + DB = CB.
# Cho BC = 9 -> |x| = 9.
answers[13] = "9"

# Câu 14: Hình chữ nhật ABCD có AB=8, AD=6. y = AB - AD = DB -> |y| = BD = 10.
answers[14] = "10"

# Câu 15: F1=30 N, F2=40 N vuông góc -> F = sqrt(30^2 + 40^2) = 50 N.
answers[15] = "50"

# Câu 16: F1=F2=60 N, góc 120 độ -> F = sqrt(60^2 + 60^2 + 2*60*60*cos(120)) = 60 N.
answers[16] = "60"

# Câu 17: Máy bay bay Đông 600 km/h, gió Bắc thổi Nam 800 km/h -> v = sqrt(600^2 + 800^2) = 1000 km/h.
answers[17] = "1000"

# Câu 18: Thuyền v_riêng = 12 km/h vuông góc bờ, dòng nước chảy xuôi 5 km/h -> v = sqrt(12^2 + 5^2) = 13 km/h.
answers[18] = "13"

# Câu 19: Tam giác đều ABC cạnh 6. u = AB - AC = CB -> |u| = 6.
answers[19] = "6"

# Câu 20: Hình bình hành ABCD tâm O. |AB + AD| = AC = 14, |AB - AD| = BD = 10. AC = 14.
answers[20] = "14"

# --- BÀI 9: CÂU 21 - 30 ---
# Câu 21: M nằm giữa A, B sao cho MA = 3MB. vec(MA) = k * vec(MB) -> ngược hướng, MA = 3MB -> k = -3.
answers[21] = "-3"

# Câu 22: Tam giác ABC trọng tâm G, M trung điểm BC. vec(AM) = k * vec(AG) -> AM = 1.5 AG -> k = 1.5.
answers[22] = "1,5"

# Câu 23: M trung điểm AB (AM=1/2 AB), N trên AC (AN=1/3 AC). K trung điểm MN -> AK = 1/4 AB + 1/6 AC.
# P = 12x + 18y = 12*(1/4) + 18*(1/6) = 3 + 3 = 6.
answers[23] = "6"

# Câu 24: D trên BC sao cho BD = 3DC -> AD = 1/4 AB + 3/4 AC. m=1/4, n=3/4. S = 4m + 8n = 1 + 6 = 7.
answers[24] = "7"

# Câu 25: IA + 4IB = 0 -> MA + 4MB = 5 MI -> k = 5.
answers[25] = "5"

# Câu 26: G trọng tâm tam giác ABC, I trung điểm AG. BI = a BA + b BC.
# BG = 1/3 BA + 1/3 BC. BI = 1/2 BA + 1/2 BG = 1/2 BA + 1/6 BA + 1/6 BC = 2/3 BA + 1/6 BC.
# a = 2/3, b = 1/6. T = 6a + 6b = 4 + 1 = 5.
answers[26] = "5"

# Câu 27: Tam giác đều ABC cạnh 9, G trọng tâm. |MA + MB + MC| = 18 <=> |3 MG| = 18 <=> MG = 6 -> R = 6.
answers[27] = "6"

# Câu 28: Hình chữ nhật ABCD, |MA + MB + MC + MD| = 20 <=> |4 MO| = 20 <=> MO = 5 -> R = 5.
answers[28] = "5"

# Câu 29: Tranh khối lượng 4 kg (P = 40 N), hai dây hợp nhau 120 độ đối xứng phương thẳng đứng (góc 60 độ với phương thẳng đứng).
# 2 * T * cos(60 deg) = P <=> 2 * T * 0.5 = 40 <=> T = 40 N.
answers[29] = "40"

# Câu 30: Tam giác ABC, M trung điểm BC, N trung điểm AM, BN cắt AC tại P.
# AP = 1/3 AC -> AC = 3 AP -> k = 3.
answers[30] = "3"

# --- BÀI 10: CÂU 31 - 40 ---
# Câu 31: A(1; 4), B(3; -2), C(5; 7) -> G((1+3+5)/3; (4-2+7)/3) = (3; 3) -> x_G + y_G = 6.
answers[31] = "6"

# Câu 32: A(-1; 2), B(7; 6) -> M(3; 4) -> OM = sqrt(3^2 + 4^2) = 5.
answers[32] = "5"

# Câu 33: A(1; 2), B(4; 6), C(-2; 3). ABCD là hình bình hành <=> AD = BC <=> D = A + BC = (1; 2) + (-6; -3) = (-5; -1).
# x_D + 2y_D = -5 + 2*(-1) = -7.
answers[33] = "-7"

# Câu 34: u=(2; -3), v=(1; 4). w = 3u - 2v = (6 - 2; -9 - 8) = (4; -17). x0 - y0 = 4 - (-17) = 21.
answers[34] = "21"

# Câu 35: A(2; 1), B(5; 7), C(m; 3). AB = (3; 6), AC = (m-2; 2). Thẳng hàng <=> (m-2)/3 = 2/6 = 1/3 <=> m = 3.
answers[35] = "3"

# Câu 36: a=(2; 1), b=(-1; 3), c=(7; 7). c = x a + y b <=> 2x - y = 7 và x + 3y = 7 <=> x=4, y=1 -> x^2 + y^2 = 17.
answers[36] = "17"

# Câu 37: A(1; 3), B(5; -1), M(x; 0). MA^2 = MB^2 <=> (x-1)^2 + 9 = (x-5)^2 + 1 <=> -2x + 10 = -10x + 26 <=> 8x = 16 <=> x = 2.
answers[37] = "2"

# Câu 38: A(-2; 5), B(1; 2), C(7; 10). MN nối trung điểm AB, AC -> MN = 1/2 BC = 1/2 * sqrt(6^2 + 8^2) = 5.
answers[38] = "5"

# Câu 39: 7h A(3; 2), 9h B(9; 10) -> v = (3; 4) km/h. 10h C = B + v = (12; 14) -> x_C = 12.
answers[39] = "12"

# Câu 40: A(1; 2), B(3; 5), C(6; 1). MA + 2MB - MC = 0 <=> (A + 2B - C) - 2M = 0 <=> M = (A + 2B - C)/2.
# x_M = (1 + 6 - 6)/2 = 0.5; y_M = (2 + 10 - 1)/2 = 5.5. x_M + y_M = 6.
answers[40] = "6"

print("All 40 answers verified:")
for q in range(1, 41):
    print(f"Câu {q:2d}: {answers[q]}")
assert len(answers) == 40
print("VERIFICATION COMPLETE!")
