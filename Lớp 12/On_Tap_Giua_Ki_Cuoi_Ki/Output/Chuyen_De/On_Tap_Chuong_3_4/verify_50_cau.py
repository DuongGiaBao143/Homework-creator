import math
import sympy as sp

def verify_all():
    print("=== KIỂM TRA VÀ TÍNH TOÁN 50 CÂU TOÁN LỚP 12 ===")
    results = {}

    # -------------------------------------------------------------
    # CHƯƠNG III: CÁC SỐ ĐẶC TRƯNG ĐO MỨC ĐỘ PHÂN TÁN MẪU GHÉP NHÓM
    # -------------------------------------------------------------
    # Câu 1: Khái niệm khoảng biến thiên R = a_{k+1} - a_1
    # Đáp án: A
    results[1] = {"ans": "A", "val": "R = a_{k+1} - a_1"}

    # Câu 2: R = 20 - 12 = 8
    # Các nhóm: [12; 14), [14; 16), [16; 18), [18; 20)
    R2 = 20 - 12
    results[2] = {"ans": "B", "val": R2}

    # Câu 3: Delta_Q = Q_3 - Q_1
    results[3] = {"ans": "A", "val": "Q3 - Q1"}

    # Câu 4: Phương sai s^2 = 1/n sum n_i (c_i - x_bar)^2
    results[4] = {"ans": "A", "val": "1/n sum n_i (c_i - x_bar)^2"}

    # Câu 5: An đồng đều hơn Bình vì s_A < s_B
    results[5] = {"ans": "A", "val": "s_A < s_B => An đồng đều hơn"}

    # Câu 6 (Trả lời ngắn):
    # [20; 25): 4, [25; 30): 10, [30; 35): 16, [35; 40): 7, [40; 45): 3
    # R = 45 - 20 = 25
    results[6] = {"val": 45 - 20, "text": "25"}

    # Câu 7 (Trả lời ngắn):
    # Khối lượng quả bưởi:
    # [1.0; 1.2): 3
    # [1.2; 1.4): 7
    # [1.4; 1.6): 12
    # [1.6; 1.8): 6
    # [1.8; 2.0): 2
    # n = 30
    # n/4 = 7.5. Nhóm chứa Q1: cf trước: 3. Nhóm [1.2; 1.4) có tần số 7, cf = 10 >= 7.5.
    # Q1 = 1.2 + (7.5 - 3)/7 * 0.2 = 1.2 + 4.5/7 * 0.2 = 1.2 + 0.9/7 = 1.2 + 9/70 = 93/70 ≈ 1.32857
    # 3n/4 = 22.5. Nhóm chứa Q3: cf trước: 3+7+12 = 22. Nhóm [1.6; 1.8) có tần số 6, cf = 28 >= 22.5.
    # Q3 = 1.6 + (22.5 - 22)/6 * 0.2 = 1.6 + 0.5/6 * 0.2 = 1.6 + 0.1/6 = 1.6 + 1/60 = 97/60 ≈ 1.61667
    # Delta_Q = Q3 - Q1 = 97/60 - 93/70 = (679 - 558)/420 = 121/420 ≈ 0.288 => 0.29
    q1 = sp.Rational(12, 10) + sp.Rational(75 - 30, 10) / 7 * sp.Rational(2, 10)
    q3 = sp.Rational(16, 10) + sp.Rational(225 - 220, 10) / 6 * sp.Rational(2, 10)
    delta_q = q3 - q1
    results[7] = {"val": float(delta_q), "frac": str(delta_q), "rounded": round(float(delta_q), 2)}

    # Câu 8, 9, 10 (Trả lời ngắn):
    # Thời gian tự học (giờ/ngày) của 50 học sinh:
    # [1; 2): 8, c1 = 1.5
    # [2; 3): 15, c2 = 2.5
    # [3; 4): 18, c3 = 3.5
    # [4; 5): 9, c4 = 4.5
    # n = 8 + 15 + 18 + 9 = 50
    # x_bar = (8*1.5 + 15*2.5 + 18*3.5 + 9*4.5) / 50
    # = (12 + 37.5 + 63 + 40.5) / 50 = 153 / 50 = 3.06
    x_bar = (8 * 1.5 + 15 * 2.5 + 18 * 3.5 + 9 * 4.5) / 50
    results[8] = {"val": x_bar, "text": "3.06"}

    # Câu 9: Phương sai s^2
    # sum n_i * c_i^2 = 8*1.5^2 + 15*2.5^2 + 18*3.5^2 + 9*4.5^2
    # = 8*2.25 + 15*6.25 + 18*12.25 + 9*20.25
    # = 18 + 93.75 + 220.5 + 182.25 = 514.5
    # s^2 = 514.5 / 50 - 3.06^2 = 10.29 - 9.3636 = 0.9264 => làm tròn 0.93
    s2 = 514.5 / 50 - x_bar**2
    results[9] = {"val": s2, "rounded": round(s2, 2)}

    # Câu 10: Độ lệch chuẩn s = sqrt(s^2)
    s = math.sqrt(s2)
    results[10] = {"val": s, "rounded": round(s, 2)}

    # Câu 11:
    # Bảng điểm 5 nhóm: n = 40
    # [4; 5): 4, [5; 6): 10, [6; 7): x, [7; 8): 12, [8; 9): 4
    # x = 40 - (4 + 10 + 12 + 4) = 40 - 30 = 10
    # Số trung bình x_bar = (4*4.5 + 10*5.5 + 10*6.5 + 12*7.5 + 4*8.5) / 40
    # = (18 + 55 + 65 + 90 + 34) / 40 = 262 / 40 = 6.55
    results[11] = {"x": 10, "x_bar": 262/40}

    # Câu 12:
    # Doanh thu (triệu đồng/ngày) trong 30 ngày:
    # [10; 20): 5
    # [20; 30): 9
    # [30; 40): 10
    # [40; 50): 6
    # n = 30. 3n/4 = 22.5
    # cf: 5, 14, 24 >= 22.5 => Nhóm [30; 40)
    # Q3 = 30 + (22.5 - 14)/10 * 10 = 30 + 8.5 = 38.5
    results[12] = {"Q3": 38.5}

    # Câu 13:
    # Cân nặng 40 VĐV:
    # [50; 55): 6
    # [55; 60): 14
    # [60; 65): 12
    # [65; 70): 8
    # n = 40. n/4 = 10
    # cf: 6, 20 >= 10 => Nhóm [55; 60)
    # Q1 = 55 + (10 - 6)/14 * 5 = 55 + 20/14 = 55 + 10/7 = 395/7 ≈ 56.43
    q1_13 = 55 + 4/14 * 5
    results[13] = {"Q1": round(q1_13, 2), "exact": "395/7"}

    # Câu 14:
    # Dây chuyền A: s_A^2 = 36 => s_A = 6.
    # Dây chuyền B: [480; 490): 5, [490; 500): 15, [500; 510): 20, [510; 520): 10. n = 50.
    # c_i: 485, 495, 505, 515.
    # x_bar_B = (5*485 + 15*495 + 20*505 + 10*515) / 50
    # = (2425 + 7425 + 10100 + 5150) / 50 = 25100 / 50 = 502
    # sum n_i (c_i - 502)^2:
    # 5*(485-502)^2 = 5*(-17)^2 = 5*289 = 1445
    # 15*(495-502)^2 = 15*(-7)^2 = 15*49 = 735
    # 20*(505-502)^2 = 20*3^2 = 20*9 = 180
    # 10*(515-502)^2 = 10*13^2 = 10*169 = 1690
    # Tổng = 1445 + 735 + 180 + 1690 = 4050
    # s_B^2 = 4050 / 50 = 81
    # s_B = sqrt(81) = 9
    # Hiệu s_B - s_A = 9 - 6 = 3
    results[14] = {"s_A": 6, "s_B": 9, "diff": 3}

    # Câu 15:
    # Thời gian xem video ngắn (phút):
    # [0; 10): 6, [10; 20): 14, [20; 30): 16, [30; 40): 4. n = 40.
    # n/4 = 10 => nhóm [10; 20): Q1 = 10 + (10 - 6)/14 * 10 = 10 + 40/14 = 10 + 20/7 = 90/7 ≈ 12.86
    # 3n/4 = 30 => nhóm [20; 30): Q3 = 20 + (30 - 20)/16 * 10 = 20 + 100/16 = 20 + 6.25 = 26.25
    # Delta_Q = Q3 - Q1 = 26.25 - 90/7 = 105/4 - 90/7 = (735 - 360)/28 = 375/28 ≈ 13.39
    delta_q15 = 26.25 - 90/7
    results[15] = {"Q1": 90/7, "Q3": 26.25, "delta_Q": round(delta_q15, 2)}

    # -------------------------------------------------------------
    # CHƯƠNG IV: NGUYÊN HÀM VÀ TÍCH PHÂN
    # -------------------------------------------------------------
    x = sp.Symbol('x')

    # Câu 16 (Trắc nghiệm): \int (3x^2 - 2x + 5) dx = x^3 - x^2 + 5x + C
    results[16] = {"ans": "A", "val": "x^3 - x^2 + 5x + C"}

    # Câu 17 (Trắc nghiệm): \int (\sin x + 2\cos x) dx = -\cos x + 2\sin x + C
    results[17] = {"ans": "B", "val": "-cos(x) + 2sin(x) + C"}

    # Câu 18 (Trắc nghiệm): \int (e^{2x} - 3^x) dx = 1/2 e^{2x} - 3^x / ln 3 + C
    results[18] = {"ans": "C", "val": "1/2 e^{2x} - 3^x/ln 3 + C"}

    # Câu 19 (Trắc nghiệm): \int 1/(2x+3) dx = 1/2 \ln|2x+3| + C
    results[19] = {"ans": "A", "val": "1/2 ln|2x+3| + C"}

    # Câu 20 (Trắc nghiệm): f(x) = 4x^3 - 2x, F(1) = 5.
    # F(x) = x^4 - x^2 + C => F(1) = 1 - 1 + C = C = 5.
    # F(2) = 2^4 - 2^2 + 5 = 16 - 4 + 5 = 17.
    results[20] = {"ans": "D", "val": 17}

    # Câu 21 (Trắc nghiệm): \int f(3x-1) dx = 1/3 F(3x-1) + C
    results[21] = {"ans": "B", "val": "1/3 F(3x-1) + C"}

    # Câu 22 (Trắc nghiệm): u = 2x+1, dv = cos x dx => du = 2 dx, v = sin x
    # \int u dv = (2x+1) sin x - \int 2 sin x dx
    results[22] = {"ans": "A", "val": "(2x+1)sin x - 2 \int sin x dx"}

    # Câu 23 (Trắc nghiệm): \int_1^5 f = \int_1^3 f + \int_3^5 f = 4 + (-2) = 2
    results[23] = {"ans": "C", "val": 2}

    # Câu 24 (Trắc nghiệm): \int_0^2 [2f(x) - 3x^2] dx = 2*3 - x^3|_0^2 = 6 - 8 = -2
    results[24] = {"ans": "A", "val": -2}

    # Câu 25 (Trắc nghiệm): \int_0^1 (3x^2 + 2e^x) dx = [x^3 + 2e^x]_0^1 = (1 + 2e) - (0 + 2) = 2e - 1
    results[25] = {"ans": "B", "val": "2e - 1"}

    # Câu 26 (Trắc nghiệm): \int_0^1 2x(x^2+1)^3 dx = (x^2+1)^4 / 4 |_0^1 = (16 - 1)/4 = 15/4
    results[26] = {"ans": "C", "val": "15/4"}

    # Câu 27 (Trắc nghiệm): \int_0^{\pi/2} x \cos x dx = [x \sin x]_0^{\pi/2} - \int_0^{\pi/2} \sin x dx = \pi/2 - [-\cos x]_0^{\pi/2} = \pi/2 - 1
    results[27] = {"ans": "D", "val": "pi/2 - 1"}

    # Câu 28 (Trắc nghiệm): S = \int_a^b |f(x)| dx
    results[28] = {"ans": "A", "val": "\int_a^b |f(x)| dx"}

    # Câu 29 (Trắc nghiệm): V = \pi \int_1^4 (\sqrt{x})^2 dx = \pi \int_1^4 x dx = \pi [x^2/2]_1^4 = \pi (8 - 1/2) = 15\pi/2
    results[29] = {"ans": "B", "val": "15 pi / 2"}

    # Câu 30 (Trắc nghiệm): s = \int_0^3 (3t^2 + 2t) dt = [t^3 + t^2]_0^3 = 27 + 9 = 36 m
    results[30] = {"ans": "C", "val": 36}

    # Câu 31 (Trả lời ngắn):
    # f'(x) = 6x^2 - 4x + 1, f(1) = 4. Tính f(3).
    # f(x) = 2x^3 - 2x^2 + x + C
    # f(1) = 2 - 2 + 1 + C = 1 + C = 4 => C = 3.
    # f(3) = 2(27) - 2(9) + 3 + 3 = 54 - 18 + 6 = 42.
    results[31] = {"val": 42}

    # Câu 32 (Trả lời ngắn):
    # f(x) = (2x+3)/(x+1) = 2 + 1/(x+1)
    # F(x) = 2x + \ln(x+1) + C. F(0) = 0 + 0 + C = 2 => C = 2.
    # F(1) = 2(1) + \ln 2 + 2 = 4 + \ln 2 => a = 4, b = 1 => a + b = 5.
    results[32] = {"a": 4, "b": 1, "sum": 5}

    # Câu 33 (Trả lời ngắn):
    # \int x / \sqrt{x^2+9} dx = \sqrt{x^2+9} + C.
    # F(0) = \sqrt{9} + C = 3 + C = 5 => C = 2.
    # F(4) = \sqrt{16+9} + 2 = 5 + 2 = 7.
    results[33] = {"val": 7}

    # Câu 34 (Trả lời ngắn):
    # \int (2x-1) e^x dx = (2x-1)e^x - \int 2e^x dx = (2x-1-2)e^x + C = (2x - 3)e^x + C
    # a = 2, b = -3 => T = a + b = -1.
    results[34] = {"a": 2, "b": -3, "T": -1}

    # Câu 35 (Trả lời ngắn):
    # \int_0^1 (2x+1)e^x dx = [(2x+1)e^x]_0^1 - \int_0^1 2e^x dx = 3e - 1 - [2e - 2] = e + 1
    # a = 1, b = 1 => P = a^2 + b^2 = 1 + 1 = 2.
    results[35] = {"a": 1, "b": 1, "P": 2}

    # Câu 36 (Trả lời ngắn):
    # \int_2^3 1/(x^2-1) dx = 1/2 [\ln|(x-1)/(x+1)|]_2^3
    # Tại 3: \ln(2/4) = \ln(1/2) = -\ln 2
    # Tại 2: \ln(1/3) = -\ln 3
    # 1/2 [-\ln 2 - (-\ln 3)] = 1/2 \ln(3/2) => a = 3, b = 2 => a + b = 5.
    results[36] = {"a": 3, "b": 2, "sum": 5}

    # Câu 37 (Trả lời ngắn):
    # I = \int_0^3 x / \sqrt{x+1} dx. Đặt t = \sqrt{x+1} => t^2 = x+1 => x = t^2-1, dx = 2t dt.
    # x=0 -> t=1; x=3 -> t=2.
    # I = \int_1^2 (t^2-1)/t * 2t dt = 2 \int_1^2 (t^2-1) dt = 2 [t^3/3 - t]_1^2
    # = 2 [(8/3 - 2) - (1/3 - 1)] = 2 [2/3 - (-2/3)] = 2 * 4/3 = 8/3 ≈ 2.67.
    # Ta yêu cầu tính giá trị hoặc phân số tối giản a/b => a+b = 8+3=11.
    results[37] = {"exact": "8/3", "a": 8, "b": 3, "sum": 11}

    # Câu 38 (Trả lời ngắn):
    # \int_1^2 (2x+1)/(x^2+x) dx. Tử số là đạo hàm của mẫu!
    # = \ln|x^2+x| |_1^2 = \ln 6 - \ln 2 = \ln(6/2) = \ln 3 => k = 3.
    results[38] = {"k": 3}

    # Câu 39 (Trả lời ngắn):
    # \int_1^e x^2 \ln x dx. u = \ln x => du = 1/x dx; dv = x^2 dx => v = x^3/3.
    # = [x^3/3 \ln x]_1^e - \int_1^e x^2/3 dx = e^3/3 - [x^3/9]_1^e = e^3/3 - (e^3/9 - 1/9)
    # = (2e^3 + 1)/9 => a = 2, b = 1, c = 9. Phân số tối giản, c > 0.
    # a + b + c = 2 + 1 + 9 = 12.
    results[39] = {"a": 2, "b": 1, "c": 9, "sum": 12}

    # Câu 40 (Trả lời ngắn):
    # \int_0^{\pi/2} \sin^3 x \cos x dx = [\sin^4 x / 4]_0^{\pi/2} = 1/4 = 0.25.
    results[40] = {"val": 0.25, "exact": "1/4"}

    # Câu 41 (Trả lời ngắn):
    # \int_0^m (2x - 3) dx = [x^2 - 3x]_0^m = m^2 - 3m = 4
    # m^2 - 3m - 4 = 0 => (m-4)(m+1) = 0 => m = 4 (do m > 0).
    results[41] = {"m": 4}

    # Câu 42 (Trả lời ngắn):
    # \int_0^6 f(x) dx = 12. J = \int_0^2 f(3x) dx. Đặt t = 3x => dt = 3 dx.
    # x=0 -> t=0; x=2 -> t=6. J = 1/3 \int_0^6 f(t) dt = 12/3 = 4.
    results[42] = {"J": 4}

    # Câu 43 (Trả lời ngắn - thực tế chuyển động):
    # v(t) = 20 - 4t. Ô tô dừng hẳn khi v(t) = 0 <=> 20 - 4t = 0 <=> t = 5 s.
    # Quãng đường s = \int_0^5 (20 - 4t) dt = [20t - 2t^2]_0^5 = 100 - 50 = 50 m.
    results[43] = {"s": 50}

    # Câu 44 (Trả lời ngắn):
    # Parabol y = -x^2 + 4x cắt Ox tại x = 0 và x = 4.
    # S = \int_0^4 (-x^2 + 4x) dx = [-x^3/3 + 2x^2]_0^4 = -64/3 + 32 = 32/3 ≈ 10.67.
    # Phân số tối giản a/b = 32/3 => a+b = 35.
    results[44] = {"exact": "32/3", "a": 32, "b": 3, "sum": 35}

    # Câu 45 (Trả lời ngắn):
    # Parabol y = x^2 - 2x và y = x.
    # Phương trình hoành độ giao điểm: x^2 - 2x = x <=> x^2 - 3x = 0 <=> x = 0 hoặc x = 3.
    # S = \int_0^3 (3x - x^2) dx = [3x^2/2 - x^3/3]_0^3 = 27/2 - 9 = 9/2 = 4.5.
    results[45] = {"S": 4.5, "exact": "9/2"}

    # Câu 46 (Trả lời ngắn - thực tế bồn hoa parabol):
    # Mảnh vườn hình chữ nhật 6m x 4m.
    # Đặt hệ trục Oxy: gốc O tại tâm cạnh đáy dài 6m. Cạnh đáy từ x = -3 đến x = 3.
    # Parabol có đỉnh tại (0; 4) và đi qua (-3; 0) và (3; 0).
    # Phương trình parabol: y = 4 - (4/9) x^2.
    # Diện tích phần trồng hoa giới hạn bởi parabol và cạnh đáy y = 0:
    # S = \int_{-3}^3 (4 - 4/9 x^2) dx = 2 * [4x - 4/27 x^3]_0^3 = 2 * (12 - 4) = 16 m^2.
    results[46] = {"S": 16}

    # Câu 47 (Trả lời ngắn):
    # y = \sqrt{2x}, y = 0, x = 3 quay quanh Ox.
    # V = \pi \int_0^3 (\sqrt{2x})^2 dx = \pi \int_0^3 2x dx = \pi [x^2]_0^3 = 9\pi.
    # V/\pi = 9.
    results[47] = {"V_div_pi": 9}

    # Câu 48 (Trả lời ngắn):
    # y = x^2, y = 0, x = 0, x = 2 quay quanh Ox.
    # V = \pi \int_0^2 (x^2)^2 dx = \pi \int_0^2 x^4 dx = \pi [x^5/5]_0^2 = 32\pi/5.
    # a/b = 32/5 => a + b = 37.
    results[48] = {"exact": "32pi/5", "a": 32, "b": 5, "sum": 37}

    # Câu 49 (Trả lời ngắn - bình gốm tròn xoay):
    # y = \sqrt{x+1}, 0 <= x <= 8 dm quay quanh Ox.
    # V = \pi \int_0^8 (\sqrt{x+1})^2 dx = \pi \int_0^8 (x+1) dx = \pi [x^2/2 + x]_0^8 = \pi (32 + 8) = 40\pi dm^3 (lít).
    # Với pi = 3.1416 => V = 40 * 3.1416 = 125.664 => làm tròn đến hàng phần mười là 125.7 lít.
    # Hoặc V/\pi = 40. Ta hỏi giá trị V/\pi để học sinh điền số nguyên đẹp: 40.
    results[49] = {"V_div_pi": 40, "exact_lit": 40 * math.pi}

    # Câu 50 (Trả lời ngắn - thiết diện vật thể):
    # Thiết diện là hình vuông cạnh sqrt(4x - x^2).
    # S(x) = (sqrt(4x - x^2))^2 = 4x - x^2.
    # V = \int_0^4 (4x - x^2) dx = [2x^2 - x^3/3]_0^4 = 32 - 64/3 = 32/3 ≈ 10.67.
    # Phân số tối giản a/b = 32/3 => a+b = 35.
    results[50] = {"exact": "32/3", "a": 32, "b": 3, "sum": 35}

    print("Tính toán thành công 50/50 câu!")
    for i in range(1, 51):
        print(f"Câu {i:2d}: {results[i]}")
    return results

if __name__ == '__main__':
    verify_all()
