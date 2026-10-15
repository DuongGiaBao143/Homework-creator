import sympy as sp
from fractions import Fraction as F
from math import comb

x, t, u = sp.symbols('x t u', real=True)
print("=== AUDIT DE 14 ===")

# ---------- PHAN I ----------
# C1 (B): y=(x^2-1)/(x^2-4x+3) -> 2 tiem can (x=3, y=1)
f = (x**2 - 1)/(x**2 - 4*x + 3)
assert sp.simplify(f - (x + 1)/(x - 3)) == 0
assert sp.limit(f, x, sp.oo) == 1 and sp.limit(f, x, 3, '+') == sp.oo and sp.limit(f, x, 1) == -1
# C2 (D): 2^(x^2-3x)<16 -> -1<x<4 -> 4 so nguyen
ints = [k for k in range(-10, 10) if k**2 - 3*k < 4]; assert ints == [0, 1, 2, 3]
# C3 (A): int_0^1 x e^x = 1
assert sp.simplify(sp.integrate(x*sp.exp(x), (x, 0, 1))) == 1
# C4 (C): mp qua A(1;0;0),B(0;2;0),C(0;0;3) : 6x+3y+2z-6=0
for p in [(1, 0, 0), (0, 2, 0), (0, 0, 3)]:
    assert 6*p[0] + 3*p[1] + 2*p[2] - 6 == 0
# C5 (D): P(tong 8 | it nhat mot mat 6)=2/11
S6 = [(i, j) for i in range(1, 7) for j in range(1, 7) if 6 in (i, j)]
assert F(len([p for p in S6 if sum(p) == 8]), len(S6)) == F(2, 11)
# C6 (B): phuong sai 50
reps = [15, 25, 35]; fr = [5, 10, 5]; m = F(sum(r*f_ for r, f_ in zip(reps, fr)), 20); assert m == 25
assert sum(f_*(r - m)**2 for r, f_ in zip(reps, fr))/20 == 50
# C7 (A): tu dien deu canh a: V = a^3 sqrt2/12
P0 = sp.Matrix([0, 0, 0]); P1 = sp.Matrix([1, 0, 0]); P2 = sp.Matrix([sp.Rational(1, 2), sp.sqrt(3)/2, 0])
P3 = sp.Matrix([sp.Rational(1, 2), sp.sqrt(3)/6, sp.sqrt(6)/3])
for a_, b_ in [(P0, P1), (P0, P2), (P0, P3), (P1, P2), (P1, P3), (P2, P3)]:
    assert sp.simplify((a_ - b_).norm() - 1) == 0
Vt = sp.Abs(sp.Matrix.hstack(P1 - P0, P2 - P0, P3 - P0).det())/6
assert sp.simplify(Vt - sp.sqrt(2)/12) == 0
# C8 (C): u1=5,d=3, S20 = 670
assert sum(5 + 3*k for k in range(20)) == 670
# C9 (A): 90*1.012^10 ~ 101.4
assert round(90*1.012**10, 1) == 101.4
# C10 (D): goc (1;1;0),(0;1;1) = 60 do
assert sp.acos(sp.Rational(1, 2)) == sp.pi/3
# C11 (C): rao 200 m dua tuong -> S max 5000
y = sp.symbols('y', positive=True)
Sx = y*(200 - 2*y); assert sp.solve(sp.diff(Sx, y), y) == [50] and Sx.subs(y, 50) == 5000
# C12 (B): cau R=3 -> 36 pi
assert sp.Rational(4, 3)*3**3 == 36
print("PHAN I OK: B D A C D B A C A D C B")

# ---------- PHAN II ----------
# C1: cap dien: f(t)=3t+5*sqrt(16+(10-t)^2)
ft = 3*t + 5*sp.sqrt(16 + (10 - t)**2)
sol = sp.solve(sp.diff(ft, t), t); assert sol == [7]
assert ft.subs(t, 7) == 46
assert abs(float(ft.subs(t, 0)) - 53.85) < 0.01 and float(ft.subs(t, 0)) != 50
assert ft.subs(t, 10) == 50 and ft.subs(t, 7) < ft.subs(t, 10)
print("P2-C1: a)D b)S c)D d)D")
# C2: mat cau x^2+y^2+z^2-2x+4y-4z-16=0, (P) 2x-2y+z+4=0
Ic = (1, -2, 2); R2 = 1 + 4 + 4 + 16; assert R2 == 25
dI = abs(2*1 - 2*(-2) + 2 + 4)/sp.sqrt(9); assert dI == 4
rc = sp.sqrt(25 - dI**2); assert rc == 3 and dI < 5  # cat, khong tiep xuc
assert sp.pi*rc**2 == 9*sp.pi
print("P2-C2: a)D b)D c)S d)S")
# C3: 3 nha cung cap A50% B30% C20% loi 1% 2% 3%
pA, pB, pC = F(50, 100), F(30, 100), F(20, 100)
l = pA*F(1, 100) + pB*F(2, 100) + pC*F(3, 100); assert l == F(17, 1000)
assert pA*F(1, 100)/l < F(3, 10)
assert pB*F(2, 100)/l == pC*F(3, 100)/l
two = 1 - (1 - l)**2; assert round(float(two), 4) == 0.0337
print("P2-C3: a)S b)D c)D d)S")
# C4: v=6t-t^2
v = 6*t - t**2
assert sp.solve(sp.diff(v, t), t) == [3] and v.subs(t, 3) == 9
assert sp.integrate(v, (t, 0, 6)) == 36
assert sp.diff(v, t, 1).subs(t, 4) == -2
assert sp.integrate(v, (t, 0, 3)) == 18
print("P2-C4: a)S b)D c)S d)D")

# ---------- PHAN III ----------
# C1: goc (SBC),(SCD) = 60
n1 = sp.Matrix([1, 0, 1]); n2 = sp.Matrix([0, -1, -1])
assert sp.acos(abs(n1.dot(n2))/(n1.norm()*n2.norm())) == sp.pi/3
# C2: V quay y=x, y=x^2 quanh Ox
V = sp.pi*sp.integrate(x**2 - x**4, (x, 0, 1)); assert V == 2*sp.pi/15
assert round(float(V), 2) == 0.42
# C3: thang qua goc hanh lang 8 va 1
th = sp.symbols('th', positive=True)
L = 8/sp.sin(th) + 1/sp.cos(th)
thm = sp.nsolve(sp.diff(L, th), th, 1.0)
assert abs(float(L.subs(th, thm)) - 5*sp.sqrt(5).evalf()) < 1e-6
assert round(float(5*sp.sqrt(5)), 1) == 11.2
# C4: doi xung A(1;2;3) qua 2x+y-2z+11=0
Ap = sp.Matrix([1, 2, 3]); nP = sp.Matrix([2, 1, -2])
val = 2*1 + 2 - 2*3 + 11; assert val == 9
Ar = Ap - 2*val/nP.dot(nP)*nP; assert list(Ar) == [-3, 0, 7] and sum(Ar) == 4
# C5: CR7 6 qua, p=0.9, P(X>=5)
p5 = comb(6, 5)*F(9, 10)**5*F(1, 10) + F(9, 10)**6; assert round(float(p5), 2) == 0.89
# C6: dV/dt=18pi, r=3 -> dr/dt = 0.5
r_ = 3; drdt = sp.Rational(18)*sp.pi/(4*sp.pi*r_**2); assert drdt == sp.Rational(1, 2)
print("PHAN III OK: 60 | 0,42 | 11,2 | 4 | 0,89 | 0,5")
print("[OK] DE 14 AUDIT 100%")
