"""Giải độc lập 22 câu, 16 ý Đ/S; kiểm tra cấu trúc LaTeX khi đã có bản đề."""
from collections import Counter
from pathlib import Path
import re
import sympy as s

x, t, h, m = s.symbols('x t h m', real=True)
R = s.Rational
answers = ['B', 'D', 'A', 'C', 'D', 'B', 'A', 'C', 'A', 'D', 'B', 'C']
assert Counter(answers) == dict.fromkeys('ABCD', 3)

# Phần I: xét miền xác định, nghiệm và các phương án nhiễu.
f = (x*x - 2*x + 5)/(x-1)
df = s.factor(s.diff(f, x))
assert df == (x-3)*(x+1)/(x-1)**2
assert df.subs(x, 4) > 0 and df.subs(x, 2) < 0 and df.subs(x, 0) < 0
assert s.solve((x-1)*(x+1)-8, x) == [-3, 3]
assert 3 > 1 and s.log(3-1, 2) + s.log(3+1, 2) == 3
assert s.integrate(3*x*x-2*x+1, (x, 0, 2)) == 6
normal = s.Matrix([1, 2, -1])
assert normal.dot(s.Matrix([2, -1, 3])) + 3 == 0
assert R(s.binomial(5, 2), s.binomial(8, 2)) == R(5, 14)
assert 20 + (R(30, 2)-12)*R(10, 12) == R(45, 2)
assert s.sin(s.pi/6) == R(1, 2) and s.sin(5*s.pi/6) == R(1, 2)
assert 2*3**4 == 162
assert abs(2*1-(-1)+2*2+2)/s.sqrt(4+1+4) == 3
f10 = x+1+4/(x-2)
assert s.simplify(f10.subs(x, t+2) - (t+3+4/t)) == 0
assert s.solve(s.diff(t+3+4/t, t), t) == [-2, 2]
valid_m = []
for value in range(-3, 11):
    roots = s.solve((x+1-value)*(x-2)+4, x)
    if len(roots) == 2 and all(root.is_real and root != 2 for root in roots):
        valid_m.append(value)
assert valid_m == [-3, -2, 8, 9, 10]
L = s.symbols('L', positive=True)
tension = 90*L/(3*s.sqrt(L**2-R(3, 5)**2))
assert s.simplify(tension.subs(L, R(3, 4))) == 50
assert s.diff(tension, L).subs(L, 1) < 0
p_a_rr = R(4, 6)*R(3, 5)
p_b_rr = R(2, 6)*R(1, 5)
assert p_a_rr/(p_a_rr+p_b_rr) == R(6, 7)
print('Phan I:', ' '.join(answers), '| 3A-3B-3C-3D')

# Phần II - Câu 1: phân thức, tiếp tuyến, hai nghiệm nằm trong khoảng.
g = (x*x-4*x+8)/(x-2)
assert s.div(x*x-4*x+8, x-2) == (x-2, 4)
assert s.solve(s.diff(g, x), x) == [0, 4]
A0, B0 = s.Matrix([0, g.subs(x, 0)]), s.Matrix([4, g.subs(x, 4)])
assert (B0-A0).norm() == 4*s.sqrt(5)
tangent = s.expand(g.subs(x, 3) + s.diff(g, x).subs(x, 3)*(x-3))
assert tangent == 14-3*x
vertical_intersection = s.Matrix([2, tangent.subs(x, 2)])
oblique_x = s.solve(tangent-(x-2), x)[0]
oblique_intersection = s.Matrix([oblique_x, oblique_x-2])
I = s.Matrix([2, 0])
triangle = abs(s.Matrix.hstack(vertical_intersection-I, oblique_intersection-I).det())/2
assert triangle == 8
valid_ii1 = []
for value in range(-10, 21):
    roots = s.solve(x*x-4*x+8-value*(x-2), x)
    if len(roots) == 2 and all(root.is_real and 2 < root < 8 for root in roots):
        valid_ii1.append(value)
assert valid_ii1 == [5, 6]
ii1 = [False, True, True, False]

# Phần II - Câu 2: độc lập có điều kiện, không giả định độc lập vô điều kiện.
prior_a = R(2, 5)
p_d_a, p_d_b = R(1, 50), R(1, 20)
p_d = prior_a*p_d_a+(1-prior_a)*p_d_b
p_a_d = prior_a*p_d_a/p_d
pp = p_d*R(9, 10)**2+(1-p_d)*R(1, 10)**2
posterior = p_d*R(9, 10)**2/pp
assert p_d == R(19, 500) and p_a_d == R(4, 19)
assert pp == R(101, 2500) and posterior == R(1539, 2020)
ii2 = [p_d == R(38, 1000), p_a_d == R(6, 19), pp == R(344, 10000), posterior > R(3, 4)]
assert ii2 == [True, False, False, True]

# Phần II - Câu 3: chuyển động thật trong Oxyz, t >= 0.
position = s.Matrix([-7, -10, -2]) + t*s.Matrix([2, 2, 1])
dist2 = s.expand(position.dot(position))
assert s.expand(dist2-(9*(t-4)**2+9)) == 0
assert s.sqrt(dist2.subs(t, 0)) == 3*s.sqrt(17)
assert s.solve(s.diff(dist2, t), t) == [4]
assert position.subs(t, 4) == s.Matrix([1, -2, 2])
entry, leave = s.solve(dist2-25, t)
assert (entry, leave) == (R(8, 3), R(16, 3))
assert leave-entry == R(8, 3)
radius_for_four_minutes = s.sqrt(9+9*2**2)
assert radius_for_four_minutes == 3*s.sqrt(5) and radius_for_four_minutes > 6
ii3 = [True, True, False, False]

# Phần II - Câu 4: thống kê ghép nhóm, biến đổi tuyến tính.
freq = [5, 10, 20, 10, 5]
reps = [49, 51, 53, 55, 57]
N = sum(freq)
mean = sum(a*b for a, b in zip(freq, reps))/s.Integer(N)
variance = sum(a*(b-mean)**2 for a, b in zip(freq, reps))/N
q1 = 50+(R(N, 4)-5)*R(2, 10)
q3 = 54+(R(3*N, 4)-35)*R(2, 10)
assert (mean, variance, q1, q3) == (53, R(24, 5), R(103, 2), R(109, 2))
new_reps = [R(1, 2)*v+R(53, 2) for v in reps]
new_mean = sum(a*b for a, b in zip(freq, new_reps))/s.Integer(N)
new_var = sum(a*(b-new_mean)**2 for a, b in zip(freq, new_reps))/N
assert new_mean == mean and new_var == variance/4
assert s.sqrt(new_var)/s.sqrt(variance) == R(1, 2)
ii4 = [True, False, True, True]
truth = [ii1, ii2, ii3, ii4]
for i, row in enumerate(truth, 1):
    print(f'Phan II cau {i}:', ['D' if v else 'S' for v in row])

# Phần III: kiểm tra các tối ưu trên đúng miền thực tế và làm tròn cuối cùng.
advertising = s.symbols('a', nonnegative=True)
base_sales = 200-40*2
profit = R(3, 10)*(base_sales+40*s.log(1+advertising))-advertising
assert base_sales == 120
assert s.solve(s.diff(profit, advertising), advertising) == [11]
assert s.diff(profit, advertising, 2).subs(advertising, 11) < 0
max_profit = profit.subs(advertising, 11)
assert abs(float(max_profit)-(25+12*float(s.log(12)))) < 1e-10
assert round(float(max_profit), 1) == 54.8

volume = s.integrate(6*(4+2*x), (x, 0, h))
inflow_volume = s.integrate(6*x+12, (x, 0, t))
times = s.solve(inflow_volume-volume.subs(h, 2), t)
time = next(v for v in times if v >= 0)
rate = s.simplify((6*time+12)/s.diff(volume, h).subs(h, 2))
assert time == -2+2*s.sqrt(7) and rate == s.sqrt(7)/4
assert round(float(rate), 2) == 0.66

developed_width = 4+3+2+3+3
shortest_wall_path = s.sqrt(developed_width**2+6**2)
assert developed_width == 15 and shortest_wall_path == 3*s.sqrt(29)
# Đường thẳng nối hai điểm trên hình trải phẳng đi lần lượt qua đủ 5 dải mặt.
fold_positions = [4, 7, 9, 12]
assert all(0 < p < developed_width for p in fold_positions)
assert round(float(shortest_wall_path), 1) == 16.2

n = s.Matrix([2, -1, 2])
A, B = s.Matrix([2, 1, 3]), s.Matrix([5, 1, 0])
assert n.dot(A) == n.dot(B) == 9
reflected_A = A-2*n.dot(A)/n.dot(n)*n
assert reflected_A == s.Matrix([-2, 3, -1])
contact = (reflected_A+B)/2
assert n.dot(contact) == 0
min_cable = (B-reflected_A).norm()
assert min_cable == 3*s.sqrt(6)
assert s.simplify((contact-A).norm()+(contact-B).norm()-min_cable) == 0
assert round(float(min_cable), 1) == 7.3

a, b, c = s.symbols('a b c')
side = a*h*h+b*h+c
coeff = s.solve([side.subs(h, 0)-10, side.subs(h, 4)-6, s.diff(side, h).subs(h, 4)], [a, b, c])
side = s.factor(side.subs(coeff))
assert side.subs(h, 8) == 10 and s.expand(side-(h*h-8*h+40)/4) == 0
building_volume = s.integrate(side**2, (h, 0, 8))
assert building_volume == R(2208, 5) and float(building_volume) == 441.6

net = s.integrate((500-4*x*x)-(68+8*x*x), (x, 0, t))-400
assert s.expand(net) == -4*t**3+432*t-400
critical = [v for v in s.solve(s.diff(net, t), t) if 0 <= v <= 8]
assert critical == [6]
assert max(net.subs(t, v) for v in [0, 8]+critical) == 1328
short = ['54,8', '0,66', '16,2', '7,3', '441,6', '1328']
print('Phan III:', short)

tex_path = Path(__file__).with_name('De 12.tex')
if tex_path.exists():
    tex = tex_path.read_text(encoding='utf-8')
    exam, solutions = tex.split('% BAT DAU DAP AN', 1)
    parts = re.split(r'\\section\*\{\\large PHẦN [IVX]+\.', exam)[1:]
    assert len(parts) == 3
    def top_items(part):
        depth, result = 0, []
        for line in part.splitlines():
            if line.startswith(r'\item') and depth == 1:
                result.append(line)
            depth += line.count(r'\begin{enumerate}')-line.count(r'\end{enumerate}')
        assert depth == 0
        return result
    assert [len(top_items(p)) for p in parts] == [12, 4, 6]
    assert len(re.findall(r'\\begin\{enumerate\}\[label=\\alph\*', parts[1])) == 4
    assert len(re.findall(r'\\item', parts[1])) == 20
    assert r'\textbf{0012}' in tex and r'\textbf{ĐỀ SỐ 12}' in tex
    assert tex.count(r'\newpage') >= 2
    assert ' & '.join(answers) in solutions
    for i, row in enumerate(truth, 1):
        assert str(i)+' & '+' & '.join('Đ' if v else 'S' for v in row) in solutions
    assert ' & '.join(short) in solutions
    assert not any(word in exam.lower() for word in ['hàm hợp', 'tích phân hàm ẩn', 'màu đỏ', 'màu xanh', 'màu cam'])
    assert 'g(x)=f(' not in exam and 'f(f(' not in exam
    print('LaTeX: du 12 + 4 + 6 cau; bang dap an dong bo; khong ham hop.')
print('[OK] Kiem toan doc lap 22 cau va 16 y D/S thanh cong.')
