"""Kiểm toán độc lập bản demo: 22 câu, 16 ý Đ/S và quota nguồn Phần III."""
from collections import Counter
from pathlib import Path
import re
import sympy as s

R = s.Rational
x, t, d, u, v = s.symbols('x t d u v', real=True)
answers = list('CADBACBDCBDA')
assert Counter(answers) == dict.fromkeys('ABCD', 3)

# I.1-I.9: nghiệm, miền xác định, tích phân, hình học, tổ hợp và thống kê.
assert s.solve_univariate_inequality(2*x+1 > 9, x, relational=False) == s.Interval.open(4, s.oo)
assert s.diff(x**3-3*x**2, x) == 3*x**2-6*x
assert s.diff(x**3-3*x**2, x).subs(x, 1) < 0
assert s.integrate(s.sin(x), (x, 0, s.pi)) == 2
assert s.Matrix([2, -3, 1]).dot(s.Matrix([1, 1, 8])) == 7
assert R(5*3+10*5+5*7, 20) == 5
assert R(7, 10)*R(4, 10)/(1-R(3, 10)*R(6, 10)) == R(14, 41)
assert s.binomial(4, 2)*s.binomial(5, 1)/s.binomial(9, 3) == R(5, 14)
assert 81*R(1, 3)**3 == 3
assert s.Matrix([4-1, 6-2, -1-(-1)]).norm() == 5

# I.10: hai tiếp tuyến song song, không chỉ đếm nghiệm đạo hàm.
f = (x*x+2)/(x-1)
roots = s.solve(s.diff(f, x)+2, x)
assert roots == [0, 2]
intercepts = [s.simplify(f.subs(x, q)+2*q) for q in roots]
assert intercepts == [-2, 10]
assert abs(intercepts[1]-intercepts[0])/s.sqrt(5) == 12/s.sqrt(5)
assert R(9, 3)+2 == 5
point_farthest = -2*s.Matrix([1, 2, 2])/3
assert point_farthest.norm() == 2
assert abs(s.Matrix([1, 2, 2]).dot(point_farthest)-9)/3 == 5
profit_i12 = x*(30-x/10)-(5*x+200)
assert s.solve(s.diff(profit_i12, x), x) == [125]
assert s.diff(profit_i12, x).subs(x, 100) > 0
assert max((profit_i12.subs(x, q), q) for q in range(1, 101))[1] == 100
print('Phan I:', ' '.join(answers), '| 3A-3B-3C-3D')

# II.1: chi phí bình quân phải nhân với số sản phẩm.
price = 60-x/10
avg_cost = x*x/100-x/5+20+100/x
total_cost = s.expand(x*avg_cost)
net = s.expand(x*price-total_cost)
assert total_cost == x**3/100-x*x/5+20*x+100
assert net == -x**3/100+x*x/10+40*x-100
assert s.solve(s.diff(net, x), x) == [-R(100, 3), 40]
assert max((net.subs(x, q), q) for q in range(1, 81)) == (1020, 40)
ii1 = [True, True, False, True]

# II.2: thời gian trong vùng radar, t >= 0.
M = s.Matrix([-5+2*t, -1+t, 2])
I = s.Matrix([1, -1, 2])
dist2 = s.expand((M-I).dot(M-I))
assert dist2 == 5*t*t-24*t+36
assert s.solve(s.diff(dist2, t), t) == [R(12, 5)]
assert dist2.subs(t, R(12, 5)) == R(36, 5)
entry, leave = s.solve(dist2-9, t)
assert (entry, leave, leave-entry) == (R(9, 5), 3, R(6, 5))
ii2 = [False, True, True, False]

# II.3: độc lập có điều kiện, xét 'ít nhất một' khác 'cả hai'.
prior = R(1, 10)
single = prior*R(4, 5)+(1-prior)*R(1, 5)
both = prior*R(4, 5)**2+(1-prior)*R(1, 5)**2
any_alarm = prior*(1-R(1, 5)**2)+(1-prior)*(1-R(4, 5)**2)
assert (single, both, any_alarm) == (R(13, 50), R(1, 10), R(21, 50))
assert prior*(1-R(1, 5)**2)/any_alarm == R(8, 35)
assert prior*R(4, 5)**2/both == R(16, 25)
ii3 = [False, True, False, True]

# II.4: quãng đường từ diện tích dưới đồ thị vận tốc.
first = s.integrate(3*t, (t, 0, 2))
last = s.integrate(9-R(3, 2)*t, (t, 2, 6))
assert first == 6 and first+last == 18
assert first+s.integrate(9-R(3, 2)*t, (t, 2, 4)) == 15
distance = first+s.integrate(9-R(3, 2)*u, (u, 2, t))
time_three_quarters = 6-s.sqrt(6)
assert 2 < time_three_quarters < 6
assert s.simplify(distance.subs(t, time_three_quarters)) == R(27, 2)
truth = [ii1, ii2, ii3, [True, False, False, True]]
for i, row in enumerate(truth, 1):
    print(f'Phan II cau {i}:', ['D' if a else 'S' for a in row])

# III.1: tìm hai tần số rồi mới tính phương sai.
a, b = s.symbols('a b', integer=True)
freq = s.solve([a+b-30, 4+3*a+5*b+42-172], [a, b])
assert freq == {a: 12, b: 18}
variance = R(4+9*12+25*18+49*6, 40)-R(43, 10)**2
assert variance == R(291, 100)

# III.2: Bayes theo hai nhánh chung kết; việc T thắng bán kết triệt tiêu.
t_win_semi = R(3, 8)
e_win_semi = R(4, 10)
joint_e = t_win_semi*e_win_semi*R(3, 7)
joint_c = t_win_semi*(1-e_win_semi)*R(3, 9)
assert joint_e/(joint_e+joint_c) == R(6, 13)

# III.3: dựng hàm độ dài từ mái che, xét cực trị và hai đầu miền d > 0.
ladder = (8+d)*s.sqrt(1+36/d**2)
d_star = (s.Integer(288))**R(1, 3)
assert s.simplify(s.diff(ladder**2, d).subs(d, d_star)) == 0
assert s.simplify(s.diff(ladder**2, d)-2*(d+8)*(d**3-288)/d**3) == 0
ladder_min = s.simplify(ladder.subs(d, d_star))
closed_ladder = (8**R(2, 3)+6**R(2, 3))**R(3, 2)
assert abs(float(ladder_min-closed_ladder)) < 1e-10
assert round(float(ladder_min), 1) == 19.7
assert s.limit(ladder, d, 0, dir='+') == s.oo and s.limit(ladder, d, s.oo) == s.oo

# III.4: quan hệ hai độ dài biến thiên, kiểm tra thêm bằng sai phân thời gian.
y = s.symbols('y', real=True)
ab = s.sqrt(y*y+y+1)
cd = 14-ab
x_de = s.sqrt(cd**2-16)
ab_now, cd_now, x_now = ab.subs(y, 4), cd.subs(y, 4), x_de.subs(y, 4)
assert ab_now == s.sqrt(21) and cd_now > 4 and x_now > 0
dy_dt = s.simplify((x_now/cd_now)*2*ab_now/9)
assert round(float(dy_dt), 2) == 0.92
assert abs(float(s.diff(x_de, y).subs(y, 4)*dy_dt)+1) < 1e-10
delta = 1e-5
x_next = float(x_now)-delta
ab_next = 14-(x_next*x_next+16)**0.5
y_next = (-1+(4*ab_next*ab_next-3)**0.5)/2
assert abs((y_next-4)/delta-float(dy_dt)) < 1e-4

# III.5: cận dưới toàn cục, đạt được ở hai điểm đối xứng; không ép hai hoành độ tùy tiện.
S = s.symbols('S', positive=True)
bound = S*S+(S+4/S)**2
assert s.expand(bound) == 2*S*S+8+16/S**2
S_star = 8**R(1, 4)
min_distance2 = s.simplify(bound.subs(S, S_star))
assert min_distance2 == 8+8*s.sqrt(2)
q = 2**(-R(1, 4))
A = s.Matrix([-1+q, -1+q+1/q])
B = s.Matrix([-1-q, -1-q-1/q])
boat_f = (x*x+x+1)/(x+1)
assert s.simplify(boat_f.subs(x, A[0])-A[1]) == 0
assert s.simplify(boat_f.subs(x, B[0])-B[1]) == 0
assert s.simplify((A-B).dot(A-B)-min_distance2) == 0
assert round(float(s.sqrt(min_distance2)), 2) == 4.39
for p in [R(1, 4), R(1, 2), 1, 2, 3]:
    for r in [R(1, 4), R(1, 2), 1, 2, 3]:
        assert float((p+r)**2+(p+r+1/p+1/r)**2) >= float(min_distance2)-1e-10

# III.6: đường thẳng trên hình trải phẳng đi ra ngoài các mặt được phép.
Lmin = 4*s.sqrt(2)+2*s.sqrt(10)
assert round(float(Lmin), 1) == 12.0
assert R(10*4, 2+4) > 4  # giao với BC nằm ngoài cạnh: không dùng sqrt(136).
assert R(1, 2)+R(1, 10) < 1  # Cauchy cho đoạn nối hai cạnh trung gian.
for n in [R(i, 4) for i in range(17)]:
    for p in [R(i, 4) for i in range(9)]:
        actual = s.sqrt(16+n*n)+s.sqrt((4-n)**2+p*p)+s.sqrt(36+(2-p)**2)
        assert float(actual-Lmin) >= -1e-10
assert s.sqrt(16+4**2)+s.sqrt(0)+s.sqrt(36+2**2) == Lmin
short = ['2,91', '0,46', '19,7', '0,92', '4,39', '12,0']
print('Phan III:', short)

base = Path(__file__).resolve().parent
if (base/'Demo.tex').exists():
    tex = (base/'Demo.tex').read_text(encoding='utf-8')
    exam, solutions = tex.split('% BAT DAU DAP AN', 1)
    parts = re.split(r'\\section\*\{\\large PHẦN [IVX]+\.', exam)[1:]
    def count_items(part):
        depth = total = 0
        for line in part.splitlines():
            if line.startswith(r'\item') and depth == 1:
                total += 1
            depth += line.count(r'\begin{enumerate}')-line.count(r'\end{enumerate}')
        assert depth == 0
        return total
    assert [count_items(p) for p in parts] == [12, 4, 6]
    assert len(re.findall(r'\\item', parts[1])) == 20
    assert ' & '.join(answers) in solutions
    assert ' & '.join(short) in solutions
    for i, row in enumerate(truth, 1):
        assert str(i)+' & '+' & '.join('Đ' if a else 'S' for a in row) in solutions
    assert not any(word in exam.lower() for word in ['hàm hợp', 'tích phân hàm ẩn', 'màu đỏ', 'màu xanh'])
    manifest = (base/'nguon_demo.md').read_text(encoding='utf-8')
    allowed = ['Phương pháp tiếp cận bài toán thực tế trong đề thi THPT QG 2026 môn Toán.pdf',
               'Vận dụng cao.pdf', 'Phương pháp trải phẳng giải một số bài toán ứng dụng thực tế – Đặng Việt Đông.pdf']
    source_rows = [line for line in manifest.splitlines() if line.startswith('| III.')]
    assert len(source_rows) == 6
    qualified = [line for line in source_rows if any(f'`{name}`' in line for name in allowed)]
    assert len(qualified) == 5
    assert all(any(f'`{name}`' in line for line in qualified) for name in allowed)
    print('Cau truc 12+4+6; 5/6 cau Phan III tu nhom nguon bat buoc, du ca ba tai lieu.')
print('[OK] Toan bo 22 cau va 16 y D/S da qua kiem toan doc lap.')
