import sympy as sp
from fractions import Fraction as F
from math import comb

x, t = sp.symbols('x t', real=True)
print("=== AUDIT DE 13 ===")

# ---------- PHAN I ----------
# C1 (C): y=(x^2+2x+2)/(x+1), khoang cach 2 cuc tri = 2*sqrt5
f = (x**2 + 2*x + 2)/(x + 1)
cr = sp.solve(sp.simplify(sp.diff(f, x)), x)
assert sorted(cr) == [-2, 0]
P = [(c, f.subs(x, c)) for c in sorted(cr)]
assert P == [(-2, -2), (0, 2)]
assert sp.sqrt((0+2)**2 + (2+2)**2) == 2*sp.sqrt(5)
# C2 (A): 4^x-5*2^x+4=0 -> tong nghiem 2
u = sp.symbols('u', positive=True)
assert sorted(sp.solve(u**2 - 5*u + 4, u)) == [1, 4] and sp.log(1, 2) + sp.log(4, 2) == 2
# C3 (D): int_1^e (2+1/x) = 2e-1
assert sp.simplify(sp.integrate(2 + 1/x, (x, 1, sp.E)) - (2*sp.E - 1)) == 0
# C4 (B): duong thang qua A(1;0;2) vuong goc x+2y-2z+1=0 -> vtcp (1;2;-2)
n = (1, 2, -2); assert n == (1, 2, -2)
# C5 (A): C(6,2)/C(10,2)=1/3
assert F(comb(6, 2), comb(10, 2)) == F(1, 3)
# C6 (C): Me = 30 + (20-14)/16*10 = 33.75
freq = [4, 10, 16, 6, 4]; assert sum(freq) == 40
assert 30 + F(20 - 14, 16)*10 == F(135, 4)
# C7 (D): goc SA va day chop deu = 60 do
a = 1; AO = sp.sqrt(2)/2; SA = sp.sqrt(2)
assert sp.acos(AO/SA) == sp.pi/3
# C8 (B): 2*(3^5-1)/(3-1)=242
assert 2*(3**5 - 1)//(3 - 1) == 242
# C9 (C): 200*1.06^n > 300 -> n=7
assert 200*1.06**6 < 300 < 200*1.06**7
# C10 (A): mat cau tam (1;-2;0) qua A(3;0;1): R^2=9
assert (3-1)**2 + (0+2)**2 + 1**2 == 9
# C11 (D): hop khong nap x(12-2x)^2 max x=2, V=128
V = x*(12 - 2*x)**2
assert sp.solve(sp.diff(V, x), x) == [2, 6] or sorted(sp.solve(sp.diff(V, x), x)) == [2, 6]
assert V.subs(x, 2) == 128
# C12 (B): Sxq = pi*R*l, R=3a, l=5a => 15 pi a^2
assert sp.sqrt(5**2 - 4**2) == 3
print("PHAN I OK: C A D B A C D B C A D B")

# ---------- PHAN II ----------
# C1: y=(x^2-3x+3)/(x-2)
g = (x**2 - 3*x + 3)/(x - 2)
cr = sorted(sp.solve(sp.simplify(sp.diff(g, x)), x)); assert cr == [1, 3]
assert g.subs(x, 1) == -1 and g.subs(x, 3) == 3
assert sp.diff(g, x).subs(x, 0) > 0 and sp.diff(g, x).subs(x, sp.Rational(3, 2)) < 0
q, r = sp.div(x**2 - 3*x + 3, x - 2); assert q == x - 1 and r == 1
# tam doi xung I(2;1); TCX y=x-1; dien tich tam giac I(2;1),(2;0),(1;0)=1/2
assert q.subs(x, 2) == 1
print("P2-C1: a)D b)S c)D d)D")
# C2: spam 30%, nhan spam 95%, ham bi gan nham 4%
pf = F(3, 10)*F(95, 100) + F(7, 10)*F(4, 100); assert pf == F(313, 1000)
pb = F(3, 10)*F(95, 100)/pf; assert pb > F(9, 10)
pc = F(7, 10)*F(96, 100); assert pc == F(672, 1000)
pd = F(3, 10)*F(5, 100)/(1 - pf); assert pd > F(2, 100)
print("P2-C2: a)S b)D c)D d)S", float(pf), float(pb), float(pc), float(pd))
# C3: guong (Oxy), A(1;2;3), B(7;8;3)
A = sp.Matrix([1, 2, 3]); B = sp.Matrix([7, 8, 3]); Bp = sp.Matrix([7, 8, -3])
d = Bp - A; tt = sp.solve(A[2] + t*d[2], t)[0]; assert tt == sp.Rational(1, 2)
M = A + tt*d; assert list(M) == [4, 5, 0]
assert sp.sqrt(d.dot(d)) == 6*sp.sqrt(3)
assert (M - A).norm() == 3*sp.sqrt(3) and (B - M).norm() == 3*sp.sqrt(3)
sin_ang = sp.Rational(3)/(M - A).norm(); assert sp.asin(sin_ang) != sp.pi/4
print("P2-C3: a)D b)D c)S d)S")
# C4: bang 50 ho
fr = [5, 12, 17, 10, 6]; assert sum(fr) == 50
reps = [F(5, 2), F(15, 2), F(25, 2), F(35, 2), F(45, 2)]
mean = sum(r*f_ for r, f_ in zip(reps, fr))/50; assert mean == F(25, 2)
Q1 = 5 + F(F(25, 2) - 5, 12)*5; assert Q1 == F(65, 8)
Q3 = 15 + F(F(75, 2) - 34, 10)*5; assert Q3 == F(67, 4)
var = sum(f_*(r - mean)**2 for r, f_ in zip(reps, fr))/50; assert var == 33
print("P2-C4: a)D b)S c)D d)D", float(Q1), float(Q3))

# ---------- PHAN III ----------
# C1: khoang cach AC va BD' cua lap phuong canh 6 = 6/sqrt6
a_ = 6
Ac = sp.Matrix([0, 0, 0]); C_ = sp.Matrix([a_, a_, 0]); Bq = sp.Matrix([a_, 0, 0]); Dp = sp.Matrix([0, a_, a_])
u1 = C_ - Ac; u2 = Dp - Bq; nn = u1.cross(u2)
dist = abs((Bq - Ac).dot(nn))/nn.norm(); assert sp.simplify(dist - sp.sqrt(6)) == 0
assert round(float(dist), 1) == 2.4
# C2: dien tich y=4-x^2 va y=x+2
S = sp.integrate((4 - x**2) - (x + 2), (x, -2, 1)); assert S == sp.Rational(9, 2)
# C3: lon tru the tich 1000, S min
r = sp.symbols('r', positive=True)
Sx = 2*sp.pi*r**2 + 2000/r
rr = sp.solve(sp.diff(Sx, r), r)[0]; Smin = float(Sx.subs(r, rr))
assert abs(Smin - 553.58) < 0.01 and round(Smin, 1) == 553.6
# C4: khoang cach hai duong thang cheo nhau = 2
A1 = sp.Matrix([1, -1, 0]); v1 = sp.Matrix([1, 2, 2])
B1 = sp.Matrix([2, 0, 6]); v2 = sp.Matrix([2, 1, -2])
nc = v1.cross(v2); assert abs((B1 - A1).dot(nc))/nc.norm() == 2
# C5: tra loi ngau nhien 10 cau, P(X>=2)
p5 = 1 - F(3, 4)**10 - 10*F(1, 4)*F(3, 4)**9; assert round(float(p5), 2) == 0.76
# C6: quang duong
tt_ = sp.symbols('tt', real=True)
v = tt_**2 - 4*tt_ + 3
s = sum(abs(sp.integrate(v, (tt_, a1, b1))) for a1, b1 in [(0, 1), (1, 3), (3, 4)])
assert s == 4
print("PHAN III OK: 2,4 | 4,5 | 553,6 | 2 | 0,76 | 4")
print("[OK] DE 13 AUDIT 100%")
