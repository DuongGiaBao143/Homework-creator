import math
import sympy as sp

def stats_grouped(bounds, freqs):
    """Tính toán toàn bộ số đặc trưng của mẫu số liệu ghép nhóm."""
    n = sum(freqs)
    k = len(freqs)
    R = bounds[-1][1] - bounds[0][0]
    mids = [(a + b) / 2 for a, b in bounds]
    x_bar = sum(f * c for f, c in zip(freqs, mids)) / n
    var = sum(f * (c - x_bar) ** 2 for f, c in zip(freqs, mids)) / n
    sd = math.sqrt(var)

    # Tứ phân vị Q1, Q2, Q3
    cum = []
    s = 0
    for f in freqs:
        s += f
        cum.append(s)

    def calc_q(p):
        target = p * n / 4.0
        for i in range(k):
            if cum[i] >= target:
                u = bounds[i][0]
                h = bounds[i][1] - bounds[i][0]
                C = cum[i - 1] if i > 0 else 0
                ni = freqs[i]
                return u + (target - C) / ni * h, i
        return None, -1

    q1, idx1 = calc_q(1)
    q2, idx2 = calc_q(2)
    q3, idx3 = calc_q(3)
    dq = q3 - q1
    return {
        "n": n, "R": R, "x_bar": x_bar, "var": var, "sd": sd,
        "Q1": q1, "idx1": idx1, "Q2": q2, "idx2": idx2, "Q3": q3, "idx3": idx3,
        "delta_Q": dq
    }

def verify_all():
    print("=== KIỂM TRA VÀ TÍNH TOÁN 50 CÂU - ĐỀ SỐ 2 ===")
    res = {}

    # -------------------------------------------------------------
    # CHƯƠNG III: CÂU 1 - 15
    # -------------------------------------------------------------
    # Câu 1: Lý thuyết khoảng biến thiên và khoảng tứ phân vị -> B (không bị ảnh hưởng ngoại lệ)
    res[1] = {"ans": "B"}

    # Câu 2: Quãng đường đi bộ bác Mạnh
    b2 = [(2.7, 3.0), (3.0, 3.3), (3.3, 3.6), (3.6, 3.9), (3.9, 4.2)]
    f2 = [3, 6, 5, 3, 3]
    st2 = stats_grouped(b2, f2)
    res[2] = {"ans": "C", "R": round(st2["R"], 2)} # 1.5

    # Câu 3: s^2 = 16.81 => s = 4.1
    res[3] = {"ans": "A", "s": math.sqrt(16.81)}

    # Câu 4: Đại lượng C là tổng tần số các nhóm trước nhóm chứa Q_k
    res[4] = {"ans": "D"}

    # Câu 5: Chiều cao 40 HS: [150;155):4, [155;160):9, [160;165):15, [165;170):8, [170;175):4
    b5 = [(150, 155), (155, 160), (160, 165), (165, 170), (170, 175)]
    f5 = [4, 9, 15, 8, 4]
    st5 = stats_grouped(b5, f5)
    # idx1 = 1 => nhóm [155; 160)
    res[5] = {"ans": "B", "idx1": st5["idx1"], "group": b5[st5["idx1"]]}

    # Câu 6: Bảng khảo sát BĐS 500 khách hàng
    b6 = [(10, 14), (14, 18), (18, 22), (22, 26), (26, 30)]
    f6 = [75, 105, 197, 80, 43]
    st6 = stats_grouped(b6, f6)
    res[6] = {"Q1": round(st6["Q1"], 4), "Q3": round(st6["Q3"], 4), "delta_Q": round(st6["delta_Q"], 1)}

    # Câu 7: Phương sai mẫu đi bộ bác Mạnh (Câu 2)
    res[7] = {"x_bar": round(st2["x_bar"], 4), "var": round(st2["var"], 2)}

    # Câu 8: Điểm thi thử 40 HS: [5;6):4, [6;7):10, [7;8):14, [8;9):8, [9;10):4
    b8 = [(5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]
    f8 = [4, 10, 14, 8, 4]
    st8 = stats_grouped(b8, f8)
    res[8] = {"x_bar": round(st8["x_bar"], 4), "var": round(st8["var"], 4), "sd": round(st8["sd"], 2)}

    # Câu 9: Tìm x, y biết n = 50, x_bar = 17.3
    # [5;10):6 (7.5), [10;15):x (12.5), [15;20):18 (17.5), [20;25):y (22.5), [25;30):4 (27.5)
    # 6 + x + 18 + y + 4 = 50 => x + y = 22
    # 6*7.5 + 12.5x + 18*17.5 + 22.5y + 4*27.5 = 50 * 17.3 = 865
    # 45 + 315 + 110 + 12.5x + 22.5y = 865 => 470 + 12.5x + 22.5y = 865 => 12.5x + 22.5y = 395
    # Thay y = 22 - x => 12.5x + 22.5(22 - x) = 395 => 495 - 10x = 395 => 10x = 100 => x = 10, y = 12.
    # T = 2x + y = 20 + 12 = 32.
    x_sym, y_sym = sp.symbols('x y')
    sol9 = sp.solve([x_sym + y_sym + 28 - 50, (6*7.5 + 12.5*x_sym + 18*17.5 + 22.5*y_sym + 4*27.5)/50 - 17.3], (x_sym, y_sym))
    res[9] = {"x": int(sol9[x_sym]), "y": int(sol9[y_sym]), "T": int(2*sol9[x_sym] + sol9[y_sym])}

    # Câu 10: Tuổi thọ pin 60 bóng đèn LED: [10;12):8, [12;14):15, [14;16):22, [16;18):10, [18;20):5
    b10 = [(10, 12), (12, 14), (14, 16), (16, 18), (18, 20)]
    f10 = [8, 15, 22, 10, 5]
    st10 = stats_grouped(b10, f10)
    res[10] = {"Q1": round(st10["Q1"], 4), "Q3": round(st10["Q3"], 4), "delta_Q": round(st10["delta_Q"], 2)}

    # Câu 11: Mức lương 80 SV: [8;10):12, [10;12):24, [12;14):28, [14;16):12, [16;18):4
    b11 = [(8, 10), (10, 12), (12, 14), (14, 16), (16, 18)]
    f11 = [12, 24, 28, 12, 4]
    st11 = stats_grouped(b11, f11)
    res[11] = {"Q3": round(st11["Q3"], 2)} # 60 - 36 = 24; 12 + 24/28 * 2 = 12 + 12/7 ≈ 13.71

    # Câu 12: Máy I đường kính: [20.0;20.2):6, [20.2;20.4):10, [20.4;20.6):10, [20.6;20.8):6 (n=32)
    b12 = [(20.0, 20.2), (20.2, 20.4), (20.4, 20.6), (20.6, 20.8)]
    f12 = [6, 10, 10, 6]
    st12 = stats_grouped(b12, f12)
    # var = (6*0.09 + 10*0.01 + 10*0.01 + 6*0.09)/32 = 1.28/32 = 0.04 => s_I = 0.2
    # s_II = 0.25 => s_II / s_I = 1.25 exact!
    res[12] = {"var_I": round(st12["var"], 4), "s_I": round(st12["sd"], 4), "ratio": round(0.25 / st12["sd"], 2)}

    # Câu 13: Tốc độ 50 xe: [40;50):5, [50;60):12, [60;70):20, [70;80):10, [80;90):3
    b13 = [(40, 50), (50, 60), (60, 70), (70, 80), (80, 90)]
    f13 = [5, 12, 20, 10, 3]
    st13 = stats_grouped(b13, f13)
    res[13] = {"x_bar": st13["x_bar"], "var": round(st13["var"], 2)}

    # Câu 14: Khoảng tứ phân vị với độ dài nhóm không đều
    # [0;2):5, [2;4):11, [4;8):16, [8;12):8 (n=40)
    b14 = [(0, 2), (2, 4), (4, 8), (8, 12)]
    f14 = [5, 11, 16, 8]
    st14 = stats_grouped(b14, f14)
    # n/4=10 => nhóm [2;4): Q1 = 2 + (10-5)/11 * 2 = 2 + 10/11 = 32/11 ≈ 2.9091
    # 3n/4=30 => nhóm [4;8): Q3 = 4 + (30-16)/16 * 4 = 4 + 14/16 * 4 = 4 + 3.5 = 7.5
    # delta_Q = 7.5 - 32/11 = 50.5/11 = 101/22 ≈ 4.59
    res[14] = {"Q1": round(st14["Q1"], 4), "Q3": st14["Q3"], "delta_Q": round(st14["delta_Q"], 2)}

    # Câu 15: Lượng mưa 24 tháng: [50;100):4, [100;150):6, [150;200):8, [200;250):4, [250;300):2
    b15 = [(50, 100), (100, 150), (150, 200), (200, 250), (250, 300)]
    f15 = [4, 6, 8, 4, 2]
    st15 = stats_grouped(b15, f15)
    res[15] = {"x_bar": round(st15["x_bar"], 2), "var": round(st15["var"], 2), "sd": round(st15["sd"], 1)}

    # -------------------------------------------------------------
    # CHƯƠNG IV: CÂU 16 - 50
    # -------------------------------------------------------------
    x = sp.Symbol('x', real=True, positive=True)
    t = sp.Symbol('t', real=True)

    # Trắc nghiệm 16 - 30
    res[16] = {"ans": "B", "check": str(sp.integrate(x**3 - 2/x**2 + 1, x))}
    res[17] = {"ans": "A", "check": str(sp.integrate(sp.cos(3*x - 1) + 1/sp.cos(x)**2, x))}
    res[18] = {"ans": "C", "check": str(sp.simplify(sp.integrate(sp.sin(x)**2, x)))}
    res[19] = {"ans": "D", "check": str(sp.diff(sp.exp(2*x) + x**2, x))}
    F20 = sp.integrate(sp.exp(x) + 2*x, x)
    # F(0) = 1 + C = 3 => C = 2 => F(1) = e + 1 + 2 = e + 3
    res[20] = {"ans": "B", "val": "e + 3"}
    res[21] = {"ans": "B", "val": 5 - 9} # -4
    res[22] = {"ans": "A", "val": 3*6 - 2*(-2)} # 22
    I23 = sp.integrate(abs(t - 1), (t, 0, 3))
    res[23] = {"ans": "C", "val": str(I23)} # 5/2
    I24 = sp.integrate(t * sp.exp(t**2), (t, 0, 1))
    res[24] = {"ans": "A", "val": str(sp.simplify(I24))} # (e - 1)/2
    I25 = sp.integrate(sp.log(x), (x, 1, sp.E))
    res[25] = {"ans": "D", "val": str(I25)} # 1
    S26 = sp.integrate((t + 2) - t**2, (t, -1, 2))
    res[26] = {"ans": "B", "val": str(S26)} # 9/2
    V27 = sp.integrate(sp.sqrt(3)/4 * t**2, (t, 0, 2))
    res[27] = {"ans": "C", "val": str(V27)} # 2*sqrt(3)/3
    V28 = sp.pi * sp.integrate((2*t)**2 - (t**2)**2, (t, 0, 2))
    res[28] = {"ans": "A", "val": str(V28)} # 64*pi/15
    v29 = 2 + sp.integrate(6*t, (t, 0, 4))
    res[29] = {"ans": "D", "val": int(v29)} # 50
    V30 = sp.integrate(3*t**2 + 4, (t, 0, 3))
    res[30] = {"ans": "C", "val": int(V30)} # 39

    # Trả lời ngắn 31 - 50
    # Câu 31: f'(x) = 3/(2*sqrt(x)) + 2x, f(1) = 5 => f(x) = x^(3/2) + x^2 + 3 => f(4) = 8 + 16 + 3 = 27
    f31 = sp.integrate(sp.Rational(3,2)/sp.sqrt(x) + 2*x, x)
    C31 = 5 - f31.subs(x, 1)
    val31 = (f31 + C31).subs(x, 4)
    res[31] = {"val": int(val31)}

    # Câu 32: f(x) = (x^2 + 2x + 4)/(x + 1) = x + 1 + 3/(x+1). F(0)=1 => F(x)=x^2/2 + x + 3ln(x+1) + 1
    # F(1) = 1/2 + 1 + 3ln2 + 1 = 5/2 + 3ln2 => a/b + c ln2 => a=5, b=2, c=3 => a+b+c = 10
    F32 = sp.integrate((t**2 + 2*t + 4)/(t + 1), (t, 0, 1)) + 1
    res[32] = {"expr": str(sp.simplify(F32)), "a": 5, "b": 2, "c": 3, "sum": 10}

    # Câu 33: \int (2x+3)ln x dx = (x^2+3x)ln x - x^2/2 - 3x + C
    # => (x^2+3x)ln x - a/b x^2 - c x + C => a=1, b=2, c=3 => a+b+c = 6
    I33 = sp.integrate((2*x + 3)*sp.log(x), x)
    res[33] = {"expr": str(sp.expand(I33)), "a": 1, "b": 2, "c": 3, "sum": 6}

    # Câu 34: f(x) = cos(x)*sin^4(x), F(0) = 0 => F(x) = sin^5(x)/5 => F(pi/2) = 1/5 = 0.2
    F34 = sp.integrate(sp.cos(t)*sp.sin(t)**4, (t, 0, sp.pi/2))
    res[34] = {"val": float(F34), "exact": str(F34)}

    # Câu 35: f(x) = 2x (x<1), 3x^2-1 (x>=1). \int_0^2 f(x) dx = \int_0^1 2x dx + \int_1^2 (3x^2-1) dx
    I35 = sp.integrate(2*t, (t, 0, 1)) + sp.integrate(3*t**2 - 1, (t, 1, 2))
    res[35] = {"val": int(I35)} # 1 + (8-2 - (1-1)) = 7

    # Câu 36: \int_1^e sqrt(1 + 3 ln x)/x dx. Đặt u = sqrt(1+3ln x) => u^2 = 1+3ln x => 2u du = 3/x dx
    # x=1->u=1, x=e->u=2. I = 2/3 \int_1^2 u^2 du = 2/9 [u^3]_1^2 = 2/9 * 7 = 14/9 => a+b = 23
    I36 = sp.integrate(sp.sqrt(1 + 3*sp.log(x))/x, (x, 1, sp.E))
    res[36] = {"exact": str(I36), "a": 14, "b": 9, "sum": 23}

    # Câu 37: \int_0^pi (x + 1)sin x dx = [-(x+1)cos x]_0^pi + \int_0^pi cos x dx = (pi+1) + 1 + 0 = pi + 2
    I37 = sp.integrate((t + 1)*sp.sin(t), (t, 0, sp.pi))
    res[37] = {"expr": str(I37), "a": 1, "b": 2, "sum_sq": 1**2 + 2**2} # 5

    # Câu 38: \int_0^1 (3x+5)/((x+1)(x+2)) dx.
    # (3x+5)/((x+1)(x+2)) = 2/(x+1) + 1/(x+2)
    # = [2 ln|x+1| + ln|x+2|]_0^1 = (2 ln 2 + ln 3) - (2 ln 1 + ln 2) = ln 2 + ln 3
    # a = 1, b = 1 => T = a + 2b = 3
    I38 = sp.integrate((3*t + 5)/((t + 1)*(t + 2)), (t, 0, 1))
    res[38] = {"expr": str(sp.simplify(I38)), "a": 1, "b": 1, "T": 3}

    # Câu 39: \int_0^{ln 2} e^x / (e^x + 1) dx = [ln(e^x + 1)]_0^{ln 2} = ln 3 - ln 2 = ln(3/2) => a+b=5
    I39 = sp.integrate(sp.exp(t)/(sp.exp(t) + 1), (t, 0, sp.log(2)))
    res[39] = {"expr": str(sp.simplify(I39)), "a": 3, "b": 2, "sum": 5}

    # Câu 40: \int_1^m (3x^2 - 4/x^2) dx = [x^3 + 4/x]_1^m = (m^3 + 4/m) - (1 + 4) = 10
    # Wait, solve for clean integer m! If m = 2: 2^3 + 4/2 - 5 = 8 + 2 - 5 = 5!
    # So set right-hand side = 5 => m^3 + 4/m - 5 = 5 => m^3 + 4/m = 10 => m = 2!
    # Check if any other positive root: g(m) = m^3 + 4/m, g'(m) = 3m^2 - 4/m^2 = 0 => m^4 = 4/3 => m ≈ 1.074
    # On (1.074, inf) g is strictly increasing; at m=1, g(1)=5 < 10. For m > 1, m=2 is the unique root > 1?
    # Check m in (1, 1.074): g(1)=5, g(1.074) = 1.24 + 3.72 = 4.96 < 10! So for m > 1 (or any m > 0.4), wait at m=0.4, 4/0.4=10.
    # Better condition: "Tìm số thực m > 1 thỏa mãn \int_1^m (3x^2 - 4/x^2) dx = 5".
    m_sym = sp.Symbol('m', positive=True)
    I40_eq = sp.integrate(3*x**2 - 4/x**2, (x, 1, m_sym)) - 5
    sol40 = sp.solve(I40_eq, m_sym)
    res[40] = {"eq": str(I40_eq), "sols": [float(s.evalf()) for s in sol40 if s.is_real]}

    # Câu 41: T(t) = 25 + 4t - 1/3 t^2, 0 <= t <= 12. Nhiệt độ trung bình = 1/12 \int_0^12 T(t) dt
    I41 = sp.integrate(25 + 4*t - sp.Rational(1, 3)*t**2, (t, 0, 12)) / 12
    res[41] = {"avg_T": float(I41), "exact": str(I41)} # 25 + 24 - 16 = 33

    # Câu 42: P'(x) = 18 - 0.04x. Lợi nhuận tăng thêm từ 50 lên 100 tấn: \int_50^100 (18 - 0.04x) dx
    I42 = sp.integrate(18 - sp.Rational(4, 100)*t, (t, 50, 100))
    res[42] = {"val": float(I42)} # [18x - 0.02 x^2]_50^100 = (1800 - 200) - (900 - 50) = 1600 - 850 = 750

    # Câu 43: Bồn 3000 lít bị rò rỉ tốc độ 160 - 2t (lít/phút). Lượng chảy ra trong 15 phút:
    # \int_0^15 (160 - 2t) dt = [160t - t^2]_0^15 = 2400 - 225 = 2175. Còn lại: 3000 - 2175 = 825 lít.
    leak43 = sp.integrate(160 - 2*t, (t, 0, 15))
    res[43] = {"leak": int(leak43), "remain": int(3000 - leak43)}

    # Câu 44: v(t) = 3t^2 (0<=t<=2), 12 - 2(t-2) = 16 - 2t (2<t<=6).
    s44 = sp.integrate(3*t**2, (t, 0, 2)) + sp.integrate(16 - 2*t, (t, 2, 6))
    res[44] = {"s": int(s44)} # 8 + [16t - t^2]_2^6 = 8 + (96-36 - (32-4)) = 8 + (60 - 28) = 40

    # Câu 45: y = x^2 - 4x + 3 và y = x - 1. Giao điểm: x^2 - 5x + 4 = 0 => x=1, x=4.
    # S = \int_1^4 |x^2 - 5x + 4| dx = 9/2 = 4.5
    S45 = sp.integrate(-(t**2 - 5*t + 4), (t, 1, 4))
    res[45] = {"S": float(S45), "exact": str(S45)}

    # Câu 46: Cổng parabol AB = 4m, GH = 4m, cửa chữ nhật rộng CD = 2.2m (AC = BD = 0.9m)
    # Hệ trục O là trung điểm AB: A(-2;0), B(2;0), G(0;4). Parabol y = 4 - x^2.
    # Cửa có x = -1.1 và x = 1.1 => Chiều cao cửa: y(1.1) = 4 - 1.1^2 = 4 - 1.21 = 2.79 m.
    # Diện tích toàn cổng: \int_{-2}^2 (4 - x^2) dx = 32/3 m^2.
    # Diện tích 2 cánh cửa chữ nhật: 2.2 * 2.79 = 6.138 m^2.
    # Diện tích hoa văn: 32/3 - 6.138 ≈ 10.6667 - 6.138 = 4.5287 => 4.53 m^2.
    S_gate = float(sp.integrate(4 - t**2, (t, -2, 2)))
    S_door = 2.2 * (4 - 1.1**2)
    S_decor = S_gate - S_door
    res[46] = {"S_gate": round(S_gate, 4), "h_door": 4 - 1.1**2, "S_door": round(S_door, 4), "S_decor": round(S_decor, 2)}

    # Câu 47: Thiết diện chữ nhật kích thước x và sqrt(9 - x^2), 0 <= x <= 3.
    # V = \int_0^3 x sqrt(9 - x^2) dx = [-1/3 (9 - x^2)^(3/2)]_0^3 = 0 - (-1/3 * 27) = 9
    V47 = sp.integrate(t * sp.sqrt(9 - t**2), (t, 0, 3))
    res[47] = {"V": int(V47)}

    # Câu 48: Chậu cây quay y = sqrt(x) + 2 từ x=0 đến x=4 quanh Ox.
    # V = pi \int_0^4 (sqrt(x) + 2)^2 dx = pi \int_0^4 (x + 4 sqrt(x) + 4) dx
    # = pi [x^2/2 + 8/3 x^(3/2) + 4x]_0^4 = pi (8 + 64/3 + 16) = pi (24 + 64/3) = 136*pi/3
    # Với pi = 3.1416 => V ≈ 142.419 => 142.4 dm^3.
    V48_exact = sp.pi * sp.integrate((sp.sqrt(x) + 2)**2, (x, 0, 4))
    V48_num = float(V48_exact.subs(sp.pi, 3.1416))
    res[48] = {"exact": str(V48_exact), "num": round(V48_num, 1)}

    # Câu 49: Chi tiết máy quay y = x^2 - 4x + 5, x=1, x=4 quanh Ox.
    V49_exact = sp.pi * sp.integrate((t**2 - 4*t + 5)**2, (t, 1, 4))
    V49_num = float(V49_exact.subs(sp.pi, 3.1416))
    res[49] = {"exact": str(V49_exact), "num_round": round(V49_num)}

    # Câu 50: Bể/chỏm cầu: Quay phần hình phẳng giới hạn bởi y = sqrt(25 - x^2), y=0, x=2, x=5 quanh Ox.
    # V = pi \int_2^5 (25 - x^2) dx = pi [25x - x^3/3]_2^5 = pi ((125 - 125/3) - (50 - 8/3)) = pi (75 - 117/3) = pi (75 - 39) = 36 pi.
    # Hỏi V/pi = 36! Số nguyên siêu đẹp!
    V50_div_pi = sp.integrate(25 - t**2, (t, 2, 5))
    res[50] = {"V_div_pi": int(V50_div_pi)}

    for i in range(1, 51):
        print(f"Câu {i:2d}: {res[i]}")
    return res

if __name__ == '__main__':
    verify_all()
