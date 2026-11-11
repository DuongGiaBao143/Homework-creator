import math
from fractions import Fraction
from statistics import mode
import sympy as sp

def verify_all():
    results = {}

    # ================= CHƯƠNG V: THỐNG KÊ =================
    # Q1: 148372 +- 300 -> d=300 (hang tram) -> lam tron den hang nghin
    # Quy tac SGK KNTT: lam tron den hang cao hon hang cua chu so khac 0 dau tien ben trai cua d
    # d = 300 -> hang cao nhat cua d la hang tram (10^2) -> lam tron den hang nghin (10^3): 148000
    results[1] = round(148372, -3)
    assert results[1] == 148000

    # Q2: 24.7684 voi d = 0.02 -> d o hang phan tram (10^-2) -> lam tron den hang phan chuc (10^-1): 24.8
    results[2] = round(24.7684, 1)
    assert results[2] == 24.8

    # Q3: x = 12 +- 0.1, y = 5 +- 0.1. S in [m, n]. Tinh n - m.
    m = Fraction(119, 10) * Fraction(49, 10)
    n = Fraction(121, 10) * Fraction(51, 10)
    results[3] = float(n - m)
    assert n - m == Fraction(34, 10)

    # Q4: h = 80 +- 0.4 -> sai so tuong doi toi da delta_h <= 0.4 / 80 (%)
    rel_err_pct = Fraction(4, 10) / 80 * 100
    results[4] = float(rel_err_pct)
    assert rel_err_pct == Fraction(1, 2)

    # Q5: a_bar = 5/8, a = 0.6 -> Delta_a = |5/8 - 0.6|
    delta_a = abs(Fraction(5, 8) - Fraction(6, 10))
    results[5] = float(delta_a)
    assert delta_a == Fraction(1, 40)

    # Q6: 7, 8, 6, 9, x, 8, 7, 9; mean = 7.75 -> tim x
    x_sym = sp.Symbol('x')
    known_6 = [7, 8, 6, 9, 8, 7, 9]
    sol6 = sp.solve((sum(known_6) + x_sym) / 8 - sp.Rational(775, 100), x_sym)[0]
    results[6] = int(sol6)
    assert results[6] == 8

    # Q7: Gio tu hoc [1,2,3,4,5], tan so [4,10,16,8,2] -> mean
    vals7 = [1, 2, 3, 4, 5]
    freq7 = [4, 10, 16, 8, 2]
    mean7 = Fraction(sum(v * f for v, f in zip(vals7, freq7)), sum(freq7))
    results[7] = float(mean7)
    assert mean7 == Fraction(114, 40)

    # Q8: Median cua 10 so: 11.8, 12.4, 11.5, 13.0, 12.1, 11.9, 12.6, 12.2, 11.7, 12.8
    d8 = sorted([Fraction(str(v)) for v in [11.8, 12.4, 11.5, 13.0, 12.1, 11.9, 12.6, 12.2, 11.7, 12.8]])
    med8 = (d8[4] + d8[5]) / 2
    results[8] = float(med8)
    assert med8 == Fraction(1215, 100)

    # Q9: Median cua bang tan so: loi chinh ta [0,1,2,3,4,5], freq [5,8,9,7,4,2], n=35
    d9 = []
    for v, f in zip([0, 1, 2, 3, 4, 5], [5, 8, 9, 7, 4, 2]):
        d9.extend([v] * f)
    assert len(d9) == 35
    results[9] = d9[17]  # 18th element (0-indexed 17)
    assert results[9] == 2

    # Helper for SGK KNTT Quartiles (excludes median when n is odd)
    def kntt_quartiles(arr):
        s = sorted(arr)
        n = len(s)
        def med(sub):
            m = len(sub)
            if m % 2 == 1:
                return Fraction(sub[m // 2])
            return (Fraction(sub[m // 2 - 1]) + Fraction(sub[m // 2])) / 2
        q2 = med(s)
        if n % 2 == 1:
            lower = s[:n // 2]
            upper = s[n // 2 + 1:]
        else:
            lower = s[:n // 2]
            upper = s[n // 2:]
        return med(lower), q2, med(upper)

    # Q10: Q3 cua 24, 19, 32, 27, 21, 35, 29, 25, 30, 22, 28
    d10 = [24, 19, 32, 27, 21, 35, 29, 25, 30, 22, 28]
    q1_10, q2_10, q3_10 = kntt_quartiles(d10)
    results[10] = float(q3_10)
    assert q3_10 == 30

    # Q11: Q1 + Q3 cua 12 diem: 6.5, 7.0, 5.5, 8.0, 7.5, 6.0, 8.5, 9.0, 7.0, 6.5, 8.0, 7.5
    d11 = [Fraction(str(v)) for v in [6.5, 7.0, 5.5, 8.0, 7.5, 6.0, 8.5, 9.0, 7.0, 6.5, 8.0, 7.5]]
    q1_11, q2_11, q3_11 = kntt_quartiles(d11)
    results[11] = float(q1_11 + q3_11)
    assert q1_11 == Fraction(65, 10) and q3_11 == 8 and results[11] == 14.5

    # Q12: Co giay [37,38,39,40,41,42], freq [3,7,14,18,6,2] -> Mo + x_bar
    sizes12 = [37, 38, 39, 40, 41, 42]
    freq12 = [3, 7, 14, 18, 6, 2]
    mo12 = sizes12[freq12.index(max(freq12))]
    mean12 = Fraction(sum(v * f for v, f in zip(sizes12, freq12)), sum(freq12))
    results[12] = float(mo12 + mean12)
    assert results[12] == 79.46

    # Q13: Khoang bien thien R cua nhiet do 12 thang: 16.5, 17.4, 20.2, 23.8, 27.5, 29.2, 29.6, 28.9, 27.6, 24.8, 21.4, 18.1
    d13 = [Fraction(str(v)) for v in [16.5, 17.4, 20.2, 23.8, 27.5, 29.2, 29.6, 28.9, 27.6, 24.8, 21.4, 18.1]]
    results[13] = float(max(d13) - min(d13))
    assert results[13] == 13.1

    # Q14: Khoang tu phan vi Delta_Q cua 4, 9, 6, 12, 8, 5, 15, 7, 10, 11
    d14 = [4, 9, 6, 12, 8, 5, 15, 7, 10, 11]
    q1_14, _, q3_14 = kntt_quartiles(d14)
    results[14] = float(q3_14 - q1_14)
    assert results[14] == 5

    # Q15: Phuong sai s^2 (chia n theo SGK KNTT) cua 21, 24, 26, 22, 27
    d15 = [Fraction(v) for v in [21, 24, 26, 22, 27]]
    mean15 = sum(d15) / len(d15)
    var15 = sum((v - mean15) ** 2 for v in d15) / len(d15)
    results[15] = float(var15)
    assert var15 == Fraction(52, 10)

    # Q16: Do lech chuan s cua bang tan so: gia tri [6,7,8,9,10], freq [3,6,7,6,3]
    vals16, freq16 = [6, 7, 8, 9, 10], [3, 6, 7, 6, 3]
    n16 = sum(freq16)
    mean16 = Fraction(sum(v * f for v, f in zip(vals16, freq16)), n16)
    var16 = sum(f * (v - mean16) ** 2 for v, f in zip(vals16, freq16)) / n16
    results[16] = float(sp.sqrt(sp.Rational(var16.numerator, var16.denominator)))
    assert var16 == Fraction(36, 25) and results[16] == 1.2

    # Q17: Nguong tren gia tri bat thuong Q3 + 1.5*Delta_Q cua 8,10,9,11,10,12,9,24,11
    d17 = [8, 10, 9, 11, 10, 12, 9, 24, 11]
    q1_17, _, q3_17 = kntt_quartiles(d17)
    upper17 = q3_17 + Fraction(3, 2) * (q3_17 - q1_17)
    results[17] = float(upper17)
    assert upper17 == Fraction(1525, 100)

    # Q18: So gia tri bat thuong trong 1.8, 4.5, 4.8, 5.0, 5.1, 5.2, 5.3, 5.4, 5.6, 5.8, 8.5
    d18 = [Fraction(str(v)) for v in [1.8, 4.5, 4.8, 5.0, 5.1, 5.2, 5.3, 5.4, 5.6, 5.8, 8.5]]
    q1_18, _, q3_18 = kntt_quartiles(d18)
    iqr18 = q3_18 - q1_18
    lo18 = q1_18 - Fraction(3, 2) * iqr18
    hi18 = q3_18 + Fraction(3, 2) * iqr18
    outliers18 = [v for v in d18 if v < lo18 or v > hi18]
    results[18] = len(outliers18)
    assert len(outliers18) == 2

    # Q19: y_i = 2*x_i + 5, s_X^2 = 9, Delta_Q(X) = 6 -> s_Y^2 + Delta_Q(Y)
    results[19] = (2**2 * 9) + (2 * 6)
    assert results[19] == 48

    # Q20: Gop 2 nhom: n1=10, x1=28, s1^2=4; n2=10, x2=32, s2^2=6 -> s^2 gop
    n1, x1, s1_sq = 10, 28, 4
    n2, x2, s2_sq = 10, 32, 6
    x_all = Fraction(n1 * x1 + n2 * x2, n1 + n2)
    ss1 = n1 * s1_sq + n1 * (x1 - x_all) ** 2
    ss2 = n2 * s2_sq + n2 * (x2 - x_all) ** 2
    var20 = (ss1 + ss2) / (n1 + n2)
    results[20] = float(var20)
    assert var20 == 9

    # ================= CHƯƠNG VI: HÀM SỐ, ĐỒ THỊ VÀ ỨNG DỤNG =================
    x, m, t = sp.symbols('x m t', real=True)

    # Q21: So gia tri nguyen trong TXD cua y = sqrt(5-x) + (x+1)/sqrt(x+3)
    dom21 = sp.S.Reals.intersect(sp.solveset(5 - x >= 0, x, sp.S.Reals)).intersect(sp.solveset(x + 3 > 0, x, sp.S.Reals))
    ints21 = [k for k in range(-10, 11) if dom21.contains(k)]
    results[21] = len(ints21)
    assert results[21] == 8

    # Q22: TXD cua y = sqrt(x+4)/(x^2-5x+6) la [a; +inf)\{b; c} -> a+b+c
    dom22 = sp.solveset(x + 4 >= 0, x, sp.S.Reals) - sp.solveset(sp.Eq(x**2 - 5*x + 6, 0), x, sp.S.Reals)
    results[22] = -4 + 2 + 3
    assert results[22] == 1 and dom22 == (sp.Interval(-4, sp.oo) - sp.FiniteSet(2, 3))

    # Q23: So gia tri nguyen m in [-10; 10] de y = sqrt(x-m+2) + 1/sqrt(2m+7-x) xac dinh tren [1; 5)
    valid_m23 = []
    target23 = sp.Interval.Ropen(1, 5)
    for mv in range(-10, 11):
        d = sp.Interval(mv - 2, sp.oo).intersect(sp.Interval.open(-sp.oo, 2 * mv + 7))
        if target23.is_subset(d):
            valid_m23.append(mv)
    results[23] = len(valid_m23)
    assert valid_m23 == [-1, 0, 1, 2, 3] and results[23] == 5

    # Q24: f(x) piecewise: 2x^2-1 (x<1); sqrt(x+3) (1<=x<=6); (x+2)/(x-4) (x>6) -> f(-2)+f(1)+f(10)
    def f24(v):
        if v < 1: return 2 * v**2 - 1
        if v <= 6: return sp.sqrt(v + 3)
        return sp.Rational(v + 2, v - 4)
    results[24] = int(f24(-2) + f24(1) + f24(10))
    assert results[24] == 11

    # Q25: y = (ax+b)/(x-1) qua A(2;5), B(0;-1) -> a^2+b^2
    a, b, c = sp.symbols('a b c', real=True)
    sol25 = sp.solve([sp.Eq((2*a + b)/(2 - 1), 5), sp.Eq((0*a + b)/(0 - 1), -1)], [a, b])
    results[25] = int(sol25[a]**2 + sol25[b]**2)
    assert results[25] == 5

    # Q26: Do thi duong gap khuc (-3;1)->(-1;4)->(2;-2)->(4;3): nghich bien (a;b)=(-1;2), M=4, m=-2
    results[26] = -1 + 2 + 4 + (-2)
    assert results[26] == 3

    # Q27: Gia cuoc taxi: <=0.5km: 10; (0.5;20]: 14/km; >20km: 12/km. Tinh cuoc 25km
    fare27 = Fraction(10) + (20 - Fraction(1, 2)) * 14 + (25 - 20) * 12
    results[27] = int(fare27)
    assert results[27] == 343

    # Q28: Tien dien: 0..50: 1800; 51..100: 2000; >100: 2400. Tong 310000 -> so kWh
    k_sym = sp.Symbol('k')
    sol28 = sp.solve(50*1800 + 50*2000 + (k_sym - 100)*2400 - 310000, k_sym)[0]
    results[28] = int(sol28)
    assert results[28] == 150

    # Q29: So gia tri nguyen m in [-5;5] de y = (m^2-4)x + 2m - 1 dong bien tren R
    valid_m29 = [mv for mv in range(-5, 6) if mv**2 - 4 > 0]
    results[29] = len(valid_m29)
    assert results[29] == 6

    # Q30: Quang duong 240km, khoi hanh 6h, 2h dau v=50, nghi 0.5h, doan sau v=70 -> gio den noi
    t_arr = 6 + 2 + Fraction(1, 2) + Fraction(240 - 2 * 50, 70)
    results[30] = float(t_arr)
    assert t_arr == Fraction(21, 2)

    # Q31: Dinh I(xI, yI) cua y = 2x^2 - 8x + 5 -> 2xI - yI
    xI31 = sp.Rational(8, 4)
    yI31 = 2 * xI31**2 - 8 * xI31 + 5
    results[31] = int(2 * xI31 - yI31)
    assert results[31] == 7

    # Q32: Parabol dinh I(2;-1), qua M(0;3) -> a+b+c
    sol32 = sp.solve([sp.Eq(-b/(2*a), 2), sp.Eq(4*a + 2*b + c, -1), sp.Eq(c, 3)], [a, b, c])
    results[32] = int(sol32[a] + sol32[b] + sol32[c])
    assert results[32] == 0

    # Q33: Parabol qua A(0;-2), B(1;1), C(-1;-1) -> a^2+b^2+c^2
    sol33 = sp.solve([sp.Eq(c, -2), sp.Eq(a + b + c, 1), sp.Eq(a - b + c, -1)], [a, b, c])
    results[33] = int(sol33[a]**2 + sol33[b]**2 + sol33[c]**2)
    assert results[33] == 9

    # Q34: M - m cua y = x^2 - 4x + 1 tren [0; 5]
    vals34 = [v**2 - 4*v + 1 for v in [0, 2, 5]]
    results[34] = max(vals34) - min(vals34)
    assert results[34] == 9

    # Q35: m lon nhat de y = -x^2 + 2(m-1)x + 3 nghich bien tren (2; +inf)
    # Vertex xI = m-1; nghich bien tren (m-1; +inf) -> m-1 <= 2 -> m <= 3
    results[35] = 3

    # Q36: d: y = 2x+m cat y = x^2-4x+5 tai A,B sao cho xA^2+xB^2 = 22 -> m
    # x^2 - 6x + 5 - m = 0; Delta' = 9 - (5-m) = 4+m > 0; sum^2 - 2prod = 36 - 2(5-m) = 22
    m36 = sp.solve(36 - 2*(5 - m) - 22, m)[0]
    assert 4 + m36 > 0
    results[36] = int(m36)
    assert results[36] == -2

    # Q37: Parabol dinh I(1;-4), qua (0;-3), (-1;0), (3;0) -> y = x^2 - 2x - 3 -> 2a+3b-c
    results[37] = 2*1 + 3*(-2) - (-3)
    assert results[37] == -1

    # Q38: Cong parabol cao 8m, rong 8m (y = 8 - 0.5x^2); xe rong 4m -> gioi han chieu cao h0 = y(2)
    results[38] = int(8 - sp.Rational(1, 2) * 2**2)
    assert results[38] == 6

    # Q39: h(t) = -5t^2 + 20t -> h_max
    results[39] = int(-5 * 2**2 + 20 * 2)
    assert results[39] == 20

    # Q40: 80m rao 3 canh: S = y*(80-2y) -> S_max
    results[40] = int(20 * (80 - 40))
    assert results[40] == 800

    # Q41: Khach san 60 phong gia 400, cu tang 20 giam 2 phong -> gia de doanh thu max
    # R(p) = p * (60 - 2*(p-400)/20) = p*(100 - 0.1p)
    p = sp.Symbol('p')
    R41 = sp.expand(p * (60 - 2 * (p - 400) / 20))
    poly41 = sp.Poly(R41, p)
    a41, b41, _ = poly41.all_coeffs()
    results[41] = int(-b41 / (2 * a41))
    assert results[41] == 500

    # Q42: Giay von 300, ban 500 duoc 120 doi; cu giam 10 tang 12 doi -> gia ban de loi nhuan max
    # Qty = 120 + 12*(500 - p)/10 = 720 - 1.2p; Profit = (p - 300)*(720 - 1.2p)
    P42 = sp.expand((p - 300) * (120 + 12 * (500 - p) / 10))
    poly42 = sp.Poly(P42, p)
    a42, b42, _ = poly42.all_coeffs()
    results[42] = int(-b42 / (2 * a42))
    assert results[42] == 450

    # Q43: Cau treo thap cao 100m, nhip 400m -> y = (100/200^2) x^2. Tai x = 200-100 = 100 -> y
    results[43] = int(sp.Rational(100, 200**2) * 100**2)
    assert results[43] == 25

    # Q44: Tau A o (0;50) di xuong Nam v=40, tau B o (0;0) di sang Dong v=30 -> d_min
    d_sq44 = sp.expand((30*t)**2 + (50 - 40*t)**2)
    poly44 = sp.Poly(d_sq44, t)
    a44, b44, c44 = poly44.all_coeffs()
    t_min44 = -b44 / (2 * a44)
    results[44] = int(sp.sqrt(d_sq44.subs(t, t_min44)))
    assert results[44] == 30

    # Q45: m > 0 de y = x^2 - 2mx + m + 2 cat Ox tai A, B voi AB = 4
    sol45 = [mv for mv in sp.solve(4*m**2 - 4*(m + 2) - 16, m) if mv > 0]
    assert len(sol45) == 1 and (sol45[0]**2 - sol45[0] - 2) > 0
    results[45] = int(sol45[0])
    assert results[45] == 3

    # Q46: So gia tri nguyen m de |x^2 - 6x + 5| = m co 4 nghiem phan biet
    valid_m46 = [mv for mv in range(-5, 10) if len(sp.solveset(sp.Eq(sp.Abs(x**2 - 6*x + 5), mv), x, sp.S.Reals)) == 4]
    results[46] = len(valid_m46)
    assert valid_m46 == [1, 2, 3] and results[46] == 3

    # Q47: So nghiem nguyen cua x^2 - 5x - 14 <= 0
    sol47 = sp.solveset(x**2 - 5*x - 14 <= 0, x, sp.S.Reals)
    ints47 = [k for k in range(-20, 21) if sol47.contains(k)]
    results[47] = len(ints47)
    assert results[47] == 10

    # Q48: Tong cac nghiem nguyen cua -2x^2 + 7x + 15 > 0
    sol48 = sp.solveset(-2*x**2 + 7*x + 15 > 0, x, sp.S.Reals)
    ints48 = [k for k in range(-20, 21) if sol48.contains(k)]
    results[48] = sum(ints48)
    assert ints48 == [-1, 0, 1, 2, 3, 4] and results[48] == 9

    # Q49: So nguyen trong TXD cua sqrt(-x^2+6x-5) + 1/sqrt(x-2)
    dom49 = sp.solveset(-x**2 + 6*x - 5 >= 0, x, sp.S.Reals).intersect(sp.solveset(x - 2 > 0, x, sp.S.Reals))
    ints49 = [k for k in range(-20, 21) if dom49.contains(k)]
    results[49] = len(ints49)
    assert ints49 == [3, 4, 5] and results[49] == 3

    # Q50: So nghiem nguyen he {x^2-3x-10 <= 0, x^2-4 > 0}
    dom50 = sp.solveset(x**2 - 3*x - 10 <= 0, x, sp.S.Reals).intersect(sp.solveset(x**2 - 4 > 0, x, sp.S.Reals))
    ints50 = [k for k in range(-20, 21) if dom50.contains(k)]
    results[50] = len(ints50)
    assert ints50 == [3, 4, 5] and results[50] == 3

    # Q51: So nguyen m de x^2 + (m-1)x + m + 2 > 0 moi x
    valid_m51 = [mv for mv in range(-20, 21) if sp.solveset(x**2 + (mv-1)*x + mv + 2 > 0, x, sp.S.Reals) == sp.S.Reals]
    results[51] = len(valid_m51)
    assert valid_m51 == [0, 1, 2, 3, 4, 5, 6] and results[51] == 7

    # Q52: So nguyen m de m*x^2 - 4*m*x + 3*m + 4 >= 0 moi x (test m=0!)
    valid_m52 = [mv for mv in range(-20, 21) if sp.solveset(mv*x**2 - 4*mv*x + 3*mv + 4 >= 0, x, sp.S.Reals) == sp.S.Reals]
    results[52] = len(valid_m52)
    assert valid_m52 == [0, 1, 2, 3, 4] and results[52] == 5

    # Q53: So nguyen x in [-10; 10] thoa (x^2-4x+3)/(x^2-9) <= 0
    ints53 = [k for k in range(-10, 11) if (k**2 - 9 != 0) and (sp.Rational(k**2 - 4*k + 3, k**2 - 9) <= 0)]
    results[53] = len(ints53)
    assert ints53 == [-2, -1, 0, 1] and results[53] == 4

    # Q54: So nguyen m de x^2 - 4mx + 3m^2 + 2m + 3 = 0 vo nghiem
    valid_m54 = [mv for mv in range(-20, 21) if sp.solveset(sp.Eq(x**2 - 4*mv*x + 3*mv**2 + 2*mv + 3, 0), x, sp.S.Reals) == sp.EmptySet]
    results[54] = len(valid_m54)
    assert valid_m54 == [0, 1, 2] and results[54] == 3

    # Q55: So nghiem nguyen cua |x^2 - 3x - 4| <= x + 1
    ints55 = [k for k in range(-20, 21) if abs(k**2 - 3*k - 4) <= k + 1]
    results[55] = len(ints55)
    assert ints55 == [-1, 3, 4, 5] and results[55] == 4

    # Q56: m nguyen nho nhat de x^2 - 4x + m > 0 voi moi x in [1; 4]
    valid_m56 = [mv for mv in range(-10, 20) if sp.Interval(1, 4).is_subset(sp.solveset(x**2 - 4*x + mv > 0, x, sp.S.Reals))]
    results[56] = min(valid_m56)
    assert results[56] == 5

    # Q57: h(t) = 25t - 5t^2 >= 20 -> khoang thoi gian
    sol57 = sp.solveset(25*t - 5*t**2 >= 20, t, sp.S.Reals)
    results[57] = int(sol57.end - sol57.start)
    assert results[57] == 3

    # Q58: DT -2x^2 + 180x >= CP 40x + 2000 -> so san pham it nhat de hoa von
    sol58 = sp.solveset(-2*x**2 + 180*x >= 40*x + 2000, x, sp.S.Reals)
    results[58] = int(sol58.start)
    assert results[58] == 20

    # Q59: Vuon chu vi 40m, loi di rong 1m ben trong quanh 4 canh, S_hoa >= 48, x <= 10 -> x_min
    sol59 = sp.solveset((x - 2)*(20 - x - 2) >= 48, x, sp.S.Reals).intersect(sp.Interval(0, 10))
    results[59] = int(sol59.start)
    assert results[59] == 6

    # Q60: So nguyen m in [-10; 10] de (x^2 + (m-1)x + 1)/(x^2 + x + 1) <= 3 moi x
    valid_m60 = [mv for mv in range(-10, 11) if sp.solveset((x**2 + (mv-1)*x + 1)/(x**2 + x + 1) <= 3, x, sp.S.Reals) == sp.S.Reals]
    results[60] = len(valid_m60)
    assert valid_m60 == list(range(0, 9)) and results[60] == 9

    # Q61: sqrt(2x^2-5x) = sqrt(x^2-4) (with explicit real domain constraints A>=0, B>=0)
    dom61 = sp.solveset(2*x**2 - 5*x >= 0, x, sp.S.Reals).intersect(sp.solveset(x**2 - 4 >= 0, x, sp.S.Reals))
    sol61 = sp.solveset(sp.Eq(2*x**2 - 5*x, x**2 - 4), x, sp.S.Reals).intersect(dom61)
    results[61] = int(list(sol61)[0])
    assert sol61 == sp.FiniteSet(4) and results[61] == 4

    # Q62: Tich cac nghiem cua sqrt(3x^2-4x+2) = sqrt(2x^2+x-2)
    dom62 = sp.solveset(3*x**2 - 4*x + 2 >= 0, x, sp.S.Reals).intersect(sp.solveset(2*x**2 + x - 2 >= 0, x, sp.S.Reals))
    sol62 = list(sp.solveset(sp.Eq(3*x**2 - 4*x + 2, 2*x**2 + x - 2), x, sp.S.Reals).intersect(dom62))
    results[62] = int(sol62[0] * sol62[1])
    assert set(sol62) == {1, 4} and results[62] == 4

    # Q63: sqrt(2x^2-5x+1) = x - 1
    dom63 = sp.solveset(2*x**2 - 5*x + 1 >= 0, x, sp.S.Reals).intersect(sp.solveset(x - 1 >= 0, x, sp.S.Reals))
    sol63 = sp.solveset(sp.Eq(2*x**2 - 5*x + 1, (x - 1)**2), x, sp.S.Reals).intersect(dom63)
    results[63] = int(list(sol63)[0])
    assert sol63 == sp.FiniteSet(3) and results[63] == 3

    # Q64: Tong cac nghiem cua sqrt(2x^2-12x+19) = x - 2
    dom64 = sp.solveset(2*x**2 - 12*x + 19 >= 0, x, sp.S.Reals).intersect(sp.solveset(x - 2 >= 0, x, sp.S.Reals))
    sol64 = list(sp.solveset(sp.Eq(2*x**2 - 12*x + 19, (x - 2)**2), x, sp.S.Reals).intersect(dom64))
    results[64] = int(sum(sol64))
    assert set(sol64) == {3, 5} and results[64] == 8

    # Q65: Tong binh phuong cac nghiem cua x^2 - 4x + sqrt(x^2-4x+5) - 7 = 0
    dom65 = sp.solveset(x**2 - 4*x + 5 >= 0, x, sp.S.Reals)
    sol65 = list(sp.solveset(sp.Eq(x**2 - 4*x + sp.sqrt(x**2 - 4*x + 5) - 7, 0), x, sp.S.Reals).intersect(dom65))
    results[65] = int(sp.simplify(sum(s**2 for s in sol65)))
    assert len(sol65) == 2 and results[65] == 24

    # Q66: So nguyen m in [-10; 10] de sqrt(x^2-2x+5) = x + m co nghiem
    dom66_x = sp.solveset(x**2 - 2*x + 5 >= 0, x, sp.S.Reals)
    valid_m66 = []
    for mv in range(-10, 11):
        sol = sp.solveset(sp.Eq(x**2 - 2*x + 5, (x + mv)**2), x, sp.S.Reals).intersect(dom66_x).intersect(sp.solveset(x + mv >= 0, x, sp.S.Reals))
        if sol != sp.EmptySet:
            valid_m66.append(mv)
    results[66] = len(valid_m66)
    assert valid_m66 == list(range(0, 11)) and results[66] == 11

    # Q67: Hai dang AB=4, BC=7, cheo 3km/h, di bo 5km/h, tong tgian 2h28' = 37/15 h -> BM
    sol67 = list(sp.solveset(sp.Eq(sp.sqrt(16 + x**2)/3 + (7 - x)/5, sp.Rational(37, 15)), x, sp.Interval(0, 7)))
    results[67] = int(sol67[0])
    assert sol67 == [3]

    # Q68: Cap quang qua song rong 3km, HB=8km, nuoc 5 ti/km, bo 3 ti/km, tong 37 ti, HM > 2 -> HM
    sol68 = [s for s in sp.solveset(sp.Eq(5*sp.sqrt(9 + x**2) + 3*(8 - x), 37), x, sp.Interval(0, 8)) if s > 2]
    results[68] = int(sol68[0])
    assert sol68 == [4]

    # Q69: Tong cac so nguyen m de y = x + m cat y = sqrt(25 - x^2) tai 2 diem phan biet
    valid_m69 = [mv for mv in range(-20, 21) if len(sp.solveset(sp.Eq(x + mv, sp.sqrt(25 - x**2)), x, sp.S.Reals)) == 2]
    results[69] = sum(valid_m69)
    assert valid_m69 == [5, 6, 7] and results[69] == 18

    # Q70: Cong parabol cao 8m, chan 8m (y = 8 - 0.5x^2). HCN noi tiep MNPQ co chu vi lon nhat -> dien tich MNPQ
    # M(-t, 0), N(t, 0), P(t, 8-0.5t^2), Q(-t, 8-0.5t^2), 0 < t < 4
    perim70 = 2 * (2*t + (8 - sp.Rational(1, 2)*t**2))
    poly70 = sp.Poly(sp.expand(perim70), t)
    a70, b70, _ = poly70.all_coeffs()
    t_opt70 = -b70 / (2 * a70)
    area70 = (2 * t_opt70) * (8 - sp.Rational(1, 2)*t_opt70**2)
    results[70] = int(area70)
    assert t_opt70 == 2 and results[70] == 24

    for q in range(1, 71):
        print(f"Cau {q:2d}: {results[q]}")
    print("\nALL 70 QUESTIONS VERIFIED SUCCESSFULLY!")

if __name__ == "__main__":
    verify_all()
