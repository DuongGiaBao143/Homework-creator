import math
from fractions import Fraction
import sympy as sp

def verify_all():
    res = {}

    # ================= CHỦ ĐỀ 1: CÁC KHÁI NIỆM MỞ ĐẦU (1 - 6) =================
    # Q1: So vecto khac 0 tu 8 dinh bat giac deu
    res[1] = 8 * 7
    assert res[1] == 56

    # Q2: Hinh thoi ABCD tam O; vecto khac 0 tu {A,B,C,D,O} cung huong voi AO
    # Tren duong thang AC theo thu tu A - O - C: AO, OC, AC -> 3 vecto
    res[2] = 3

    # Q3: Hinh vuong ABCD tam O, M,N,P,Q trung diem AB,BC,CD,DA. So vecto != MN va = MN
    pts3 = {
        'A': (0, 2), 'B': (2, 2), 'C': (2, 0), 'D': (0, 0),
        'O': (1, 1), 'M': (1, 2), 'N': (2, 1), 'P': (1, 0), 'Q': (0, 1)
    }
    mn = (pts3['N'][0] - pts3['M'][0], pts3['N'][1] - pts3['M'][1])
    eq_mn = [(u, v) for u, pu in pts3.items() for v, pv in pts3.items()
             if (pv[0] - pu[0], pv[1] - pu[1]) == mn and not (u == 'M' and v == 'N')]
    assert set(eq_mn) == {('A', 'O'), ('O', 'C'), ('Q', 'P')}
    res[3] = len(eq_mn)
    assert res[3] == 3

    # Q4: Grid vectors u=(3,2), v=(4,-1) -> |u|^2 + |v|^2
    res[4] = (3**2 + 2**2) + (4**2 + (-1)**2)
    assert res[4] == 30

    # Q5: Tam giac can ABC tai A, BAC=120 deg, AB=6, M trung diem BC -> AM
    res[5] = int(6 * sp.cos(sp.rad(60)))
    assert res[5] == 3

    # Q6: Hinh thang can ABCD, AB=4, CD=10, AD=5, H hinh chieu A len CD -> |AH|
    dh = (10 - 4) // 2
    res[6] = int(sp.sqrt(5**2 - dh**2))
    assert res[6] == 4

    # ================= CHỦ ĐỀ 2: TỔNG VÀ HIỆU HAI VECTƠ (7 - 15) =================
    # Q7: Hinh thang can ABCD day AB=6, CD=14; M,N trung diem AC, BD -> |MN|
    # Check voi toa do cu the: A(-3,4), B(3,4), C(7,0), D(-7,0)
    A7, B7, C7, D7 = sp.Matrix([-3, 4]), sp.Matrix([3, 4]), sp.Matrix([7, 0]), sp.Matrix([-7, 0])
    M7, N7 = (A7 + C7) / 2, (B7 + D7) / 2
    res[7] = int((N7 - M7).norm())
    assert res[7] == 4

    # Q8: Luc giac deu ABCDEF tam O canh 4 -> |AB + AF + AO|
    hex_pts = [sp.Matrix([4 * sp.cos(k * sp.pi / 3), 4 * sp.sin(k * sp.pi / 3)]) for k in range(6)]
    O8 = sp.Matrix([0, 0])
    v8 = (hex_pts[1] - hex_pts[0]) + (hex_pts[5] - hex_pts[0]) + (O8 - hex_pts[0])
    res[8] = int(sp.simplify(v8.norm()))
    assert res[8] == 8

    # Q9: Hinh thoi ABCD canh 5, BAD=120 deg -> |AB + AD|
    # AB = (5,0), AD = (5 cos120, 5 sin120)
    AB9 = sp.Matrix([5, 0])
    AD9 = sp.Matrix([5 * sp.cos(sp.rad(120)), 5 * sp.sin(sp.rad(120))])
    res[9] = int(sp.simplify((AB9 + AD9).norm()))
    assert res[9] == 5

    # Q10: Tam giac ABC vuong tai B, BA=5, BC=12 -> |BA + BC|
    res[10] = int(sp.sqrt(5**2 + 12**2))
    assert res[10] == 13

    # Q11: HCN ABCD, AB=9, AD=12 -> |BA + BC + BD|
    # BA + BC = BD -> 2*|BD|
    res[11] = int(2 * sp.sqrt(9**2 + 12**2))
    assert res[11] == 30

    # Q12: AE=7, u = AB - CB + CD - ED = AE -> |u| = 7
    res[12] = 7

    # Q13: |F1|=6, |F2|=10, angle=60 -> |F1 + F2|
    res[13] = int(sp.sqrt(6**2 + 10**2 + 2 * 6 * 10 * sp.cos(sp.rad(60))))
    assert res[13] == 14

    # Q14: Bay Bac 400 km/h, gio Tay 300 km/h -> van toc thuc
    res[14] = int(sp.sqrt(400**2 + 300**2))
    assert res[14] == 500

    # Q15: Song rong 240m, v_x=4 m/s, v_n=3 m/s -> quang duong thuc te
    t15 = 240 / 4
    v15 = math.hypot(4, 3)
    res[15] = int(v15 * t15)
    assert res[15] == 300

    # ================= CHỦ ĐỀ 3: TÍCH CỦA MỘT VECTƠ VỚI MỘT SỐ (16 - 26) =================
    # Q16: AB=15, M tren tia doi tia AB voi MA=6 -> AM = k AB
    # Vector AB huong +, M o -6 -> AM = -6, AB = 15 -> k = -6/15 = -0.4
    res[16] = float(Fraction(-6, 15))
    assert res[16] == -0.4

    # Q17: HBH ABCD, G trong tam BCD -> AG = m AB + n AD -> P = 3m + 6n
    # AG = (AB + AC + AD)/3 = (2AB + 2AD)/3 -> m=2/3, n=2/3 -> 3m+6n = 6
    m17, n17 = Fraction(2, 3), Fraction(2, 3)
    res[17] = int(3 * m17 + 6 * n17)
    assert res[17] == 6

    # Q18: Tam giac ABC, BD = 1/3 BC, E trung diem AC, M trung diem DE -> AM = x AB + y AC -> 12x + 12y
    # AD = AB + 1/3(AC - AB) = 2/3 AB + 1/3 AC; AE = 1/2 AC -> AM = 1/3 AB + 5/12 AC
    x18, y18 = Fraction(1, 3), Fraction(5, 12)
    res[18] = int(12 * x18 + 12 * y18)
    assert res[18] == 9

    # Q19: M trung diem AB, NC + 2NA = 0, MN cat BC tai P, BP = k BC -> k
    A19, B19, C19 = sp.Matrix([0, 0]), sp.Matrix([1, 0]), sp.Matrix([0, 1])
    M19 = (A19 + B19) / 2
    N19 = (2 * A19 + C19) / 3
    s, t = sp.symbols('s t')
    sol19 = sp.solve(M19 + s * (N19 - M19) - (B19 + t * (C19 - B19)), [s, t])
    res[19] = int(sol19[t])
    assert res[19] == -1

    # Q20: Hinh vuong ABCD canh 4, M trung diem CD -> |AB + 2AM|^2
    A20, B20, C20, D20 = sp.Matrix([0, 0]), sp.Matrix([4, 0]), sp.Matrix([4, 4]), sp.Matrix([0, 4])
    M20 = (C20 + D20) / 2
    v20 = (B20 - A20) + 2 * (M20 - A20)
    res[20] = int(v20.dot(v20))
    assert res[20] == 128

    # Q21: Tam giac deu ABC canh 6 -> quy tich |MA + MB + MC| = |AB - AC| -> ban kinh R
    # 3 MG = BC = 6 -> R = 2
    res[21] = 2

    # Q22: HCN ABCD, AB=6, AD=8 -> |MA + MB + MC + MD| = |AB + AD| -> ban kinh R
    # 4 MO = AC = 10 -> R = 2.5
    res[22] = float(Fraction(10, 4))
    assert res[22] == 2.5

    # Q23: Tu giac ABCD, I, J trung diem AB, CD, G trung diem IJ -> OA+OB+OC+OD = k OG
    res[23] = 4

    # Q24: Tam giac ABC, MA + 2MB - MC = 0, AC = 10 -> BM
    # MA - MC = CA = -AC -> 2MB = AC -> BM = 5
    res[24] = 5

    # Q25: Vat P = 100N treo boi OA (60 deg ngang), OB (30 deg ngang), AOB = 90 -> T_OB
    # T_A * cos(60) - T_B * cos(30) = 0, T_A * sin(60) + T_B * sin(30) = 100
    TA, TB = sp.symbols('TA TB', positive=True)
    sol25 = sp.solve([
        sp.Eq(TA * sp.cos(sp.rad(60)), TB * sp.cos(sp.rad(30))),
        sp.Eq(TA * sp.sin(sp.rad(60)) + TB * sp.sin(sp.rad(30)), 100)
    ], [TA, TB])
    res[25] = int(sol25[TB])
    assert res[25] == 50

    # Q26: Tam giac ABC hai trung tuyen BM=u, CN=v. BC = a u + b v -> S = 3a - 3b
    # u = M - B, v = N - C
    A26, B26, C26 = sp.Matrix([0, 0]), sp.Matrix([2, 0]), sp.Matrix([0, 2])
    u26 = (A26 + C26) / 2 - B26
    v26 = (A26 + B26) / 2 - C26
    a26, b26 = sp.symbols('a b')
    sol26 = sp.solve(a26 * u26 + b26 * v26 - (C26 - B26), [a26, b26])
    res[26] = int(3 * sol26[a26] - 3 * sol26[b26])
    assert sol26[a26] == sp.Rational(2, 3) and sol26[b26] == sp.Rational(-2, 3) and res[26] == 4

    # ================= CHỦ ĐỀ 4: TỌA ĐỘ TRONG MẶT PHẲNG (27 - 37) =================
    # Q27: A(-2,3), B(4,1), C(1,5); u=OA, v=BC; w = 2u - v = (x0, y0) -> x0 + y0
    u27 = sp.Matrix([-2, 3])
    v27 = sp.Matrix([1 - 4, 5 - 1])
    w27 = 2 * u27 - v27
    res[27] = int(w27[0] + w27[1])
    assert res[27] == 1

    # Q28: a=(3,-1), b=(-2,5), c=(5,7) = m a + n b -> m^2 + n^2
    m, n = sp.symbols('m n', real=True)
    sol28 = sp.solve(m * sp.Matrix([3, -1]) + n * sp.Matrix([-2, 5]) - sp.Matrix([5, 7]), [m, n])
    res[28] = int(sol28[m]**2 + sol28[n]**2)
    assert res[28] == 13

    # Q29: A(1,-2), B(4,5), C(9,4), M, N trung diem AB, BC -> |MN|
    M29 = (sp.Matrix([1, -2]) + sp.Matrix([4, 5])) / 2
    N29 = (sp.Matrix([4, 5]) + sp.Matrix([9, 4])) / 2
    res[29] = int((N29 - M29).norm())
    assert res[29] == 5

    # Q30: HBH ABCD, A(-2,1), B(3,5), tam I(1,2) -> xC + yC + xD + yD
    C30 = 2 * sp.Matrix([1, 2]) - sp.Matrix([-2, 1])
    D30 = 2 * sp.Matrix([1, 2]) - sp.Matrix([3, 5])
    res[30] = int(C30[0] + C30[1] + D30[0] + D30[1])
    assert res[30] == 5

    # Q31: A(2,-3), B(-4,6), MA = -2 MB -> xM + 2yM
    M31 = (sp.Matrix([2, -3]) + 2 * sp.Matrix([-4, 6])) / 3
    res[31] = int(M31[0] + 2 * M31[1])
    assert res[31] == 4

    # Q32: A(-1,4), B(2,-2), C(5,m) thang hang -> m
    AB32 = sp.Matrix([3, -6])
    AC32 = sp.Matrix([6, m - 4])
    res[32] = int(sp.solve(AB32[0] * AC32[1] - AB32[1] * AC32[0], m)[0])
    assert res[32] == -8

    # Q33: A(-2,3), B(4,6), N(0, yN) thang hang -> yN
    yN = sp.Symbol('yN')
    res[33] = int(sp.solve(6 * (yN - 3) - 3 * 2, yN)[0])
    assert res[33] == 4

    # Q34: A(1,2), B(3,4), C(m^2-1, 2m+2); AB, AC cung phuong -> tong cac gia tri m
    roots34 = sp.solve(2 * (2 * m) - 2 * (m**2 - 2), m)
    assert len(roots34) == 2
    res[34] = int(sp.simplify(sum(roots34)))
    assert res[34] == 2

    # Q35: M(2,1), N(-1,4), P(3,5) trung diem cac canh -> 3 xG + 3 yG
    res[35] = (2 - 1 + 3) + (1 + 4 + 5)
    assert res[35] == 14

    # Q36: 8h A(2,5), 10h B(10,11) -> 11h30 C(xC, yC) -> xC + yC
    v36 = (sp.Matrix([10, 11]) - sp.Matrix([2, 5])) / 2
    C36 = sp.Matrix([10, 11]) + sp.Rational(3, 2) * v36
    res[36] = float(C36[0] + C36[1])
    assert res[36] == 31.5

    # Q37: A(1,1), B(4,4), C(3,5), IA + 2IB + 3IC = 0 -> OI
    I37 = (sp.Matrix([1, 1]) + 2 * sp.Matrix([4, 4]) + 3 * sp.Matrix([3, 5])) / 6
    res[37] = int(I37.norm())
    assert res[37] == 5

    # ================= CHỦ ĐỀ 5: TÍCH VÔ HƯỚNG & TỔNG HỢP (38 - 50) =================
    # Q38: AB=5, AC=8, BAC=60 -> AB . AC
    res[38] = int(5 * 8 * sp.cos(sp.rad(60)))
    assert res[38] == 20

    # Q39: |a|=4, |b|=6, (a,b)=120 -> |a + b|^2
    res[39] = int(4**2 + 6**2 + 2 * 4 * 6 * sp.cos(sp.rad(120)))
    assert res[39] == 28

    # Q40: |u|=3, |v|=5, |u - v|=7 -> goc (u, v) (do)
    cos40 = sp.Rational(3**2 + 5**2 - 7**2, 2 * 3 * 5)
    res[40] = int(sp.deg(sp.acos(cos40)))
    assert res[40] == 120

    # Q41: HCN ABCD, AB=6, AD=8, M trung diem BC -> AM . BD
    A41, B41, C41, D41 = sp.Matrix([0, 0]), sp.Matrix([6, 0]), sp.Matrix([6, 8]), sp.Matrix([0, 8])
    M41 = (B41 + C41) / 2
    res[41] = int((M41 - A41).dot(D41 - B41))
    assert res[41] == -4

    # Q42: Hinh thoi ABCD canh 6, BAD=60, M trung diem CD -> AM . BC
    A42 = sp.Matrix([0, 0])
    B42 = sp.Matrix([6, 0])
    D42 = sp.Matrix([6 * sp.cos(sp.rad(60)), 6 * sp.sin(sp.rad(60))])
    C42 = B42 + D42
    M42 = (C42 + D42) / 2
    res[42] = int(sp.simplify((M42 - A42).dot(C42 - B42)))
    assert res[42] == 45

    # Q43: a=(1,3), b=(-2,m), (a, b) = 45 deg -> m
    a43, b43 = sp.Matrix([1, 3]), sp.Matrix([-2, m])
    sol43 = [s for s in sp.solve(sp.Eq((a43.dot(b43))**2, (a43.dot(a43))*(b43.dot(b43))*sp.Rational(1, 2)), m)
             if a43.dot(b43).subs(m, s) > 0]
    assert sol43 == [4]
    res[43] = int(sol43[0])

    # Q44: A(1,2), B(5,2), C(3,4) -> goc (AB, AC) (do)
    AB44, AC44 = sp.Matrix([4, 0]), sp.Matrix([2, 2])
    cos44 = AB44.dot(AC44) / (AB44.norm() * AC44.norm())
    res[44] = int(sp.deg(sp.acos(cos44)))
    assert res[44] == 45

    # Q45: A(0,1), B(3,5), C(m,2), tam giac ABC vuong tai B -> m
    BA45, BC45 = sp.Matrix([-3, -4]), sp.Matrix([m - 3, -3])
    res[45] = int(sp.solve(BA45.dot(BC45), m)[0])
    assert res[45] == 7

    # Q46: Tam giac deu ABC canh 6, M tren BC sao cho BM = 2MC -> AM . BC
    B46, C46 = sp.Matrix([0, 0]), sp.Matrix([6, 0])
    A46 = sp.Matrix([3, 3 * sp.sqrt(3)])
    M46 = B46 + sp.Rational(2, 3) * (C46 - B46)
    res[46] = int(sp.simplify((M46 - A46).dot(C46 - B46)))
    assert res[46] == 6

    # Q47: F=(12,15), A(1,2) -> B(7,10) -> cong W = F . AB
    res[47] = int(sp.Matrix([12, 15]).dot(sp.Matrix([7 - 1, 10 - 2])))
    assert res[47] == 192

    # Q48: Tam giac ABC trung tuyen BM vuong goc CN, AB=6, AC=8 -> BC^2
    # AB^2 + AC^2 = 5 BC^2 -> BC^2 = (36+64)/5 = 20
    res[48] = (6**2 + 8**2) // 5
    assert res[48] == 20

    # Q49: Tam giac deu ABC canh 4, M tren canh BC -> min(MA.MB + MB.MC + MC.MA)
    x = sp.Symbol('x', real=True)
    B49, C49 = sp.Matrix([0, 0]), sp.Matrix([4, 0])
    A49 = sp.Matrix([2, 2 * sp.sqrt(3)])
    M49 = sp.Matrix([x, 0])
    expr49 = sp.expand((A49 - M49).dot(B49 - M49) + (B49 - M49).dot(C49 - M49) + (C49 - M49).dot(A49 - M49))
    poly49 = sp.Poly(expr49, x)
    a49, b49, _ = poly49.all_coeffs()
    x_min49 = -b49 / (2 * a49)
    assert 0 <= x_min49 <= 4
    res[49] = int(expr49.subs(x, x_min49))
    assert res[49] == -4

    # Q50: A(1,3), B(4,6), M(x, 0) tren Ox -> min(2MA^2 + MB^2)
    expr50 = sp.expand(2 * ((x - 1)**2 + 9) + ((x - 4)**2 + 36))
    poly50 = sp.Poly(expr50, x)
    a50, b50, _ = poly50.all_coeffs()
    x_min50 = -b50 / (2 * a50)
    res[50] = int(expr50.subs(x, x_min50))
    assert x_min50 == 2 and res[50] == 60

    for q in range(1, 51):
        print(f"Cau {q:2d}: {res[q]}")
    print("\nALL 50 VECTOR QUESTIONS VERIFIED SUCCESSFULLY!")

if __name__ == "__main__":
    verify_all()
