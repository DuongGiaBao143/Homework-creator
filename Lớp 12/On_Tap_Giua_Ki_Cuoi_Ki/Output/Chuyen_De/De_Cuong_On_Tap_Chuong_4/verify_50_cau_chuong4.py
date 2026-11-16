"""Kiểm định toán học toàn bộ 50 câu Đề cương ôn tập Chương IV (Nguyên hàm và Tích phân)."""
import math
import sympy as sp

x, t = sp.symbols("x t", real=True)
m = sp.Symbol("m", positive=True)

results = {}

# ==============================================================================
# PHẦN I. 20 CÂU TRẮC NGHIỆM
# ==============================================================================
# Câu 1: Định nghĩa nguyên hàm F'(x) = f(x) -> B
results[1] = "B (F'(x) = f(x))"

# Câu 2: Nguyen ham f(x) = 4x^3 + 3x^2 - 2
f2 = 4 * x**3 + 3 * x**2 - 2
F2 = sp.integrate(f2, x)
assert sp.simplify(F2 - (x**4 + x**3 - 2 * x)) == 0
results[2] = f"D ({F2} + C)"

# Câu 3: Nguyen ham f(x) = 3/x + sqrt(x) tren (0, +inf)
x_pos = sp.Symbol("x", positive=True)
f3 = 3 / x_pos + sp.sqrt(x_pos)
F3 = sp.integrate(f3, x_pos)
assert sp.simplify(F3 - (3 * sp.log(x_pos) + sp.Rational(2, 3) * x_pos**(sp.Rational(3, 2)))) == 0
results[3] = "A (3 ln x + 2/3 x sqrt(x) + C)"

# Câu 4: Nguyen ham 1/sin^2(x) - 3 cos(x)
f4 = 1 / sp.sin(x)**2 - 3 * sp.cos(x)
F4_expected = -sp.cot(x) - 3 * sp.sin(x)
assert sp.simplify(sp.diff(F4_expected, x) - f4) == 0
results[4] = "C (-cot x - 3 sin x + C)"

# Câu 5: Nguyen ham 2^x + 3 e^x
f5 = 2**x + 3 * sp.exp(x)
F5_expected = 2**x / sp.log(2) + 3 * sp.exp(x)
assert sp.simplify(sp.diff(F5_expected, x) - f5) == 0
results[5] = "A (2^x / ln 2 + 3 e^x + C)"

# Câu 6: f(x) = 6x^2 - 4x + 1, F(0) = 3 -> F(2)
F6 = sp.integrate(6 * x**2 - 4 * x + 1, x) + 3
val6 = F6.subs(x, 2)
assert val6 == 13
results[6] = f"D (F(2) = {val6})"

# Câu 7: v(0) = 0, a(t) = 4t + 2 -> v(3)
v7 = sp.integrate(4 * t + 2, (t, 0, 3))
assert v7 == 24
results[7] = f"B (v(3) = {v7})"

# Câu 8: F(a) = 7, F(b) = -3 -> F(b) - F(a) = -10
assert -3 - 7 == -10
results[8] = "C (-10)"

# Câu 9: int_{-1}^5 = 12, int_{-1}^2 = 5 -> int_2^5 = 7
assert 12 - 5 == 7
results[9] = "A (7)"

# Câu 10: int 5f + 3g = 5*4 + 3*(-1) = 17
assert 5 * 4 + 3 * (-1) == 17
results[10] = "D (17)"

# Câu 11: int_0^1 (4x^3 + 3 e^x) dx
I11 = sp.integrate(4 * x**3 + 3 * sp.exp(x), (x, 0, 1))
assert sp.simplify(I11 - (3 * sp.E - 2)) == 0
results[11] = f"B ({I11})"

# Câu 12: int_0^(pi/4) (2 cos 2x + 1) dx
I12 = sp.integrate(2 * sp.cos(2 * x) + 1, (x, 0, sp.pi / 4))
assert sp.simplify(I12 - (1 + sp.pi / 4)) == 0
results[12] = f"C ({I12})"

# Câu 13: int_{-1}^2 |2x| dx
I13 = sp.integrate(-2 * x, (x, -1, 0)) + sp.integrate(2 * x, (x, 0, 2))
assert I13 == 5
results[13] = f"A ({I13})"

# Câu 14: int_1^2 (2/x) dx
I14 = sp.integrate(2 / x, (x, 1, 2))
assert sp.simplify(I14 - sp.log(4)) == 0
results[14] = "B (ln 4)"

# Câu 15: Cong thuc dien tich giua hai do thi -> D
results[15] = "D (int_a^b |f(x) - g(x)| dx)"

# Câu 16: S gioi han boi y = 4 - x^2 va Ox
S16 = sp.integrate(4 - x**2, (x, -2, 2))
assert S16 == sp.Rational(32, 3)
results[16] = f"C ({S16})"

# Câu 17: S gioi han boi y = x^2 - 1 va y = 1 - x^2
S17 = sp.integrate((1 - x**2) - (x**2 - 1), (x, -1, 1))
assert S17 == sp.Rational(8, 3)
results[17] = f"B ({S17})"

# Câu 18: V vat the [0, 2], thiet dien hinh vuong canh sqrt(3x+1)
V18 = sp.integrate(3 * x + 1, (x, 0, 2))
assert V18 == 8
results[18] = f"A ({V18})"

# Câu 19: Quay y = e^x, Ox, x=0, x=1 quanh Ox
V19 = sp.pi * sp.integrate(sp.exp(2 * x), (x, 0, 1))
assert sp.simplify(V19 - sp.pi * (sp.E**2 - 1) / 2) == 0
results[19] = f"D ({sp.factor(V19)})"

# Câu 20: Luong nuoc Q(t) = 3t^2 + 2t tu t=1 den t=4
W20 = sp.integrate(3 * t**2 + 2 * t, (t, 1, 4))
assert W20 == 78
results[20] = f"C ({W20})"


# ==============================================================================
# PHẦN II. 30 CÂU TRẢ LỜI NGẮN (CÂU 21 - 50)
# ==============================================================================
# Nhóm 1: Bài 11 (Câu 21 - 30)
F21 = sp.integrate(3 * x**2 - 8 * x + 5, x)
C21 = 6 - F21.subs(x, 1)
ans21 = (F21 + C21).subs(x, 4)
assert ans21 == 24
results[21] = str(ans21)

F22 = sp.integrate(2 * x_pos + 6 / sp.sqrt(x_pos), x_pos)
C22 = 10 - F22.subs(x_pos, 1)
ans22 = (F22 + C22).subs(x_pos, 9)
assert ans22 == 114
results[22] = str(ans22)

F23 = sp.integrate((2 * x_pos**2 - x_pos + 3) / x_pos, x_pos)
C23 = 4 - F23.subs(x_pos, 1)
val23 = sp.simplify((F23 + C23).subs(x_pos, sp.E))
c23 = sp.simplify(val23 - (sp.E**2 - sp.E))
assert c23 == 7
results[23] = str(c23)

F24 = sp.integrate(4 * sp.sin(x) + 2 * sp.cos(x), x)
C24 = 3 - F24.subs(x, 0)
ans24 = (F24 + C24).subs(x, sp.pi)
assert ans24 == 11
results[24] = str(ans24)

F25 = sp.tan(x) - x
C25 = 2 - F25.subs(x, 0)
val25 = sp.simplify((F25 + C25).subs(x, sp.pi / 4))
assert sp.simplify(val25 - (3 - sp.pi / 4)) == 0
ans25 = 3 + 4
assert ans25 == 7
results[25] = str(ans25)

F26 = sp.integrate(sp.exp(x) * (2 + sp.exp(-x)), x)
C26 = 5 - F26.subs(x, 0)
val26 = sp.simplify((F26 + C26).subs(x, sp.log(3)))
assert sp.simplify(val26 - (9 + sp.log(3))) == 0
ans26 = 9 + 3
assert ans26 == 12
results[26] = str(ans26)

f27 = sp.integrate(3 * x**2 - 4 * x + 2, x)
C27 = 11 - f27.subs(x, 2)
ans27 = (f27 + C27).subs(x, 3)
assert ans27 == 22
results[27] = str(ans27)

h28 = sp.integrate(sp.Rational(3, 2) * t + 20, t) + 45
ans28 = h28.subs(t, 6)
assert ans28 == 192
results[28] = str(ans28)

C_cost = sp.integrate(sp.Rational(6, 100) * x**2 - sp.Rational(12, 10) * x + 15, x) + 80
ans29 = C_cost.subs(x, 20)
assert ans29 == 300
results[29] = str(ans29)

v30 = sp.integrate(-10, t) + 20
h30 = sp.integrate(v30, t) + 25
t_peak = sp.solve(v30, t)[0]
ans30 = h30.subs(t, t_peak)
assert ans30 == 45
results[30] = str(ans30)

# Nhóm 2: Bài 12 (Câu 31 - 40)
A31, B31 = sp.symbols("A B")
sol31 = sp.solve([2 * A31 + B31 - 19, A31 - B31 - 2], (A31, B31))
ans31 = 3 * sol31[A31] + 4 * sol31[B31]
assert ans31 == 41
results[31] = str(ans31)

I32 = sp.integrate((2 * x + 5) / (x + 1), (x, 0, 2))
assert sp.simplify(I32 - (4 + 3 * sp.log(3))) == 0
ans32 = 4**2 + 3**2
assert ans32 == 25
results[32] = str(ans32)

I33 = sp.integrate((x_pos**2 + 3 * sp.sqrt(x_pos)) / sp.sqrt(x_pos), (x_pos, 1, 4))
assert I33 == sp.Rational(107, 5)
assert float(I33) == 21.4
results[33] = "21,4"

I34 = sp.integrate(2 * sp.sin(x) + 3 * sp.cos(x) - 1, (x, 0, sp.pi / 2))
assert sp.simplify(I34 - (5 - sp.pi / 2)) == 0
ans34 = 5 + 2
assert ans34 == 7
results[34] = str(ans34)

I35 = sp.integrate(-(x**2 - 2 * x), (x, 0, 2)) + sp.integrate(x**2 - 2 * x, (x, 2, 3))
assert I35 == sp.Rational(8, 3)
ans35 = 8 + 3
assert ans35 == 11
results[35] = str(ans35)

I36 = sp.integrate(x**2 + 3, (x, -1, 2)) + sp.integrate(4 * x - 1, (x, 2, 4))
assert I36 == 34
results[36] = str(I36)

eq37 = sp.integrate(3 * x**2 - 4 * x + 4, (x, 0, m)) - 8
sol37 = sp.solve(eq37, m)
assert sol37 == [2]
results[37] = "2"

S38 = (
    sp.integrate(t**2 - 4 * t + 3, (t, 0, 1))
    + sp.integrate(-(t**2 - 4 * t + 3), (t, 1, 3))
    + sp.integrate(t**2 - 4 * t + 3, (t, 3, 4))
)
assert S38 == 4
results[38] = str(S38)

# Câu 39: v(t) gấp khúc O(0,0) - A(10,15) - B(25,15) - C(30,10)
S39 = sp.Rational(1, 2) * 10 * 15 + 15 * 15 + sp.Rational(15 + 10, 2) * 5
assert S39 == sp.Rational(725, 2)
assert float(S39) == 362.5
results[39] = "362,5"

E40 = sp.integrate(12 + 6 * t - sp.Rational(3, 4) * t**2, (t, 0, 6))
assert E40 == 126
results[40] = str(E40)

# Nhóm 3: Bài 13 (Câu 41 - 50)
S41 = sp.integrate(x**3 - 4 * x, (x, -2, 0)) + sp.integrate(-(x**3 - 4 * x), (x, 0, 2))
assert S41 == 8
results[41] = str(S41)

pts42 = sp.solve((x**2 - 4 * x + 5) - (-x + 5), x)
assert pts42 == [0, 3]
S42 = sp.integrate((-x + 5) - (x**2 - 4 * x + 5), (x, 0, 3))
assert S42 == sp.Rational(9, 2)
results[42] = "4,5"

# Câu 43: S1 = 11 tren [-2,1] phia tren Ox, S2 = 6 tren [1,4] phia duoi Ox
int_f43 = 11 - 6
I43 = 2 * int_f43 + 3 * (4 - (-2))
assert I43 == 28
results[43] = str(I43)

# Câu 44: y = 1/6 x^2 va y = -1/6 x^2 + 2x
pts44 = sp.solve(sp.Rational(1, 6) * x**2 - (-sp.Rational(1, 6) * x**2 + 2 * x), x)
assert pts44 == [0, 6]
S44 = sp.integrate((-sp.Rational(1, 6) * x**2 + 2 * x) - sp.Rational(1, 6) * x**2, (x, 0, 6))
assert S44 == 12
results[44] = str(S44)

# Câu 45: Hầm parabol rộng 12m, cao 9m -> y = 9 - 1/4 x^2 trên [-6, 6]
S45 = sp.integrate(9 - sp.Rational(1, 4) * x**2, (x, -6, 6))
assert S45 == 72
cost45 = S45 * sp.Rational(1, 2)
assert cost45 == 36
results[45] = str(cost45)

# Câu 46: Tam giác vuông cân cạnh huyền 2 sqrt(x^2 + 2x) -> S(x) = x^2 + 2x
V46 = sp.integrate(x**2 + 2 * x, (x, 1, 4))
assert V46 == 36
results[46] = str(V46)

# Câu 47: Tam giác đều cạnh 6 - 2x trên [0, 3]
V47 = sp.integrate(sp.sqrt(3) / 4 * (6 - 2 * x)**2, (x, 0, 3))
assert sp.simplify(V47 - 9 * sp.sqrt(3)) == 0
results[47] = "9"

# Câu 48: Quay y = sqrt(x^3 + 1), Ox, [0, 2] -> V / pi
V48_over_pi = sp.integrate(x**3 + 1, (x, 0, 2))
assert V48_over_pi == 6
results[48] = str(V48_over_pi)

# Câu 49: Quay y = x + 1, Ox, [0, 3] -> V / pi
V49_over_pi = sp.integrate((x + 1)**2, (x, 0, 3))
assert V49_over_pi == 21
results[49] = str(V49_over_pi)

# Câu 50: Quay y = 4 - 1/9 x^2 trên [-3, 3] quanh Ox
V50 = sp.pi * sp.integrate((4 - sp.Rational(1, 9) * x**2)**2, (x, -3, 3))
V50_exact = float(V50.evalf())
V50_31416 = float((V50 / sp.pi).evalf()) * 3.1416
V50_314 = float((V50 / sp.pi).evalf()) * 3.14
print(f"[CHECK C50] V/pi = {V50/sp.pi} = {float((V50/sp.pi).evalf())}")
print(f"[CHECK C50] math.pi -> {V50_exact:.6f} -> round={round(V50_exact)}")
print(f"[CHECK C50] 3.1416  -> {V50_31416:.6f} -> round={round(V50_31416)}")
print(f"[CHECK C50] 3.14    -> {V50_314:.6f} -> round={round(V50_314)}")
assert round(V50_exact) == 255
assert round(V50_31416) == 255
assert round(V50_314) == 255
results[50] = "255"

# Kiểm tra phân bố A/B/C/D trong Phần I
mc_letters = [results[i][0] for i in range(1, 21)]
counts = {k: mc_letters.count(k) for k in ["A", "B", "C", "D"]}
print("Phan bo dap an Phan I:", counts)
assert counts == {"A": 5, "B": 5, "C": 5, "D": 5}

print("\n=== TONG HOP DAP AN 50 CAU DA KIEM DINH ===")
for k in range(1, 51):
    print(f"Cau {k:02d}: {results[k]}")
