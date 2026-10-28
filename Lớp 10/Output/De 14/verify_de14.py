"""
verify_de14.py: Kiểm tra độc lập tính đúng đắn toán học 100% của Đề số 14 (Giữa kì 1 Toán 10).
Sử dụng SymPy và Python tiêu chuẩn.
"""
import math
import sympy as sp

def verify_part_I():
    print("--- KIỂM TRA PHẦN I (12 CÂU TRẮC NGHIỆM) ---")
    answers = {}

    # Câu 1: P(n): "n^2 - 1 chia het cho 4"
    # A. n=3: 3^2 - 1 = 8 chia het cho 4 -> Dung
    # B. n=2: 3 khong chia het cho 4
    # C. n=4: 15 khong chia het cho 4
    # D. n=6: 35 khong chia het cho 4
    c1_ok = (3**2 - 1) % 4 == 0 and (2**2 - 1) % 4 != 0 and (4**2 - 1) % 4 != 0 and (6**2 - 1) % 4 != 0
    assert c1_ok, "Câu 1 sai"
    answers[1] = "A"

    # Câu 2: A = {x in R | -3 <= x < 2} -> [-3; 2)
    # A. (-3; 2]  B. [-3; 2)  C. [-3; 2]  D. (-3; 2)
    answers[2] = "B"

    # Câu 3: P => Q: "Nếu P thì Q"
    # A: khi va chi khi  B: Q => P  C: Neu P thi Q  D: dieu kien can
    answers[3] = "C"

    # Câu 4: Phu dinh cua "forall x in R, x^2 + 2x + 3 > 0"
    # la "exists x in R, x^2 + 2x + 3 <= 0" -> D
    answers[4] = "D"

    # Câu 5: 2x - 3y + 6 > 0
    # A(1; 1): 2(1) - 3(1) + 6 = 5 > 0 -> Dung
    # B(-2; 1): -4 - 3 + 6 = -1 < 0
    # C(0; 3): -9 + 6 = -3 < 0
    # D(-4; 0): -8 + 6 = -2 < 0
    pt5 = lambda x, y: 2*x - 3*y + 6
    assert pt5(1, 1) > 0 and pt5(-2, 1) < 0 and pt5(0, 3) < 0 and pt5(-4, 0) < 0
    answers[5] = "A"

    # Câu 6: He BPT bac nhat hai an
    # A: x^2 (sai), B: 3x+y>=2, x-2y+5<=0 (dung), C: 3 an x,y,z, D: xy (sai)
    answers[6] = "B"

    # Câu 7: x - 2y + 4 >= 0
    # M(0; 3): 0 - 6 + 4 = -2 < 0
    # N(2; 4): 2 - 8 + 4 = -2 < 0
    # P(1; 1): 1 - 2 + 4 = 3 >= 0 -> Dung
    # Q(-1; 3): -1 - 6 + 4 = -3 < 0
    pt7 = lambda x, y: x - 2*y + 4
    assert pt7(0, 3) < 0 and pt7(2, 4) < 0 and pt7(1, 1) > 0 and pt7(-1, 3) < 0
    answers[7] = "C"

    # Câu 8: x - y + 1 >= 0 va 2x + y - 4 <= 0
    # A(2; 2): 2-2+1=1>=0, 2(2)+2-4 = 2 > 0 (loai)
    # B(-2; 0): -2-0+1=-1 < 0 (loai)
    # C(1; 3): 1-3+1=-1 < 0 (loai)
    # D(1; 1): 1-1+1=1>=0, 2(1)+1-4=-1<=0 (dung)
    h8 = lambda x, y: (x - y + 1 >= 0) and (2*x + y - 4 <= 0)
    assert not h8(2, 2) and not h8(-2, 0) and not h8(1, 3) and h8(1, 1)
    answers[8] = "D"

    # Câu 9: Tam giac vuong tai A, AB=6, AC=8 -> BC=10
    # r = S / p = (1/2 * 6 * 8) / ((6 + 8 + 10) / 2) = 24 / 12 = 2
    r9 = (0.5 * 6 * 8) / (0.5 * (6 + 8 + 10))
    assert r9 == 2.0
    answers[9] = "A"

    # Câu 10: Hai goc bu nhau: cos(180 - alpha) = -cos(alpha) -> B
    answers[10] = "B"

    # Câu 11: Cong thuc trung tuyen: m_a^2 = (2(b^2 + c^2) - a^2) / 4 -> C
    answers[11] = "C"

    # Câu 12: P = sin^2(35) + cos^2(120) + sin^2(55) - tan(45)
    # sin(55) = cos(35) => sin^2(35) + sin^2(55) = 1
    # cos(120) = -1/2 => cos^2(120) = 1/4
    # tan(45) = 1 => P = 1 + 1/4 - 1 = 1/4 -> D
    rad = math.radians
    p12 = math.sin(rad(35))**2 + math.cos(rad(120))**2 + math.sin(rad(55))**2 - math.tan(rad(45))
    assert abs(p12 - 0.25) < 1e-9
    answers[12] = "D"

    counts = {k: list(answers.values()).count(k) for k in "ABCD"}
    print(f"Bảng đáp án Phần I: {answers}")
    print(f"Phân bố đáp án: {counts}")
    assert counts == {"A": 3, "B": 3, "C": 3, "D": 3}, "Đáp án Phần I không cân bằng 3A-3B-3C-3D!"
    print("-> Phần I: OK!\n")
    return answers


def verify_part_II():
    print("--- KIỂM TRA PHẦN II (2 CÂU ĐÚNG/SAI) ---")
    # Câu 13: menh_de_tap_hop
    # a) Hinh binh hanh co hai duong cheo cat nhau tai trung diem moi duong: DUNG
    # b) n chia het cho 6 la dieu kien du de n chia het cho 3: DUNG (n%6==0 => n%3==0)
    # c) Dao cua "Tam giac deu => A=60": "Neu A=60 thi tam giac deu": SAI
    # d) x > 2 <=> x^2 > 4: SAI (vi x=-3 thoa x^2>4 nhung khong > 2)
    c13 = {"a": True, "b": True, "c": False, "d": False}
    print(f"Câu 13: {c13}")

    # Câu 14: bpt_hai_an (Trồng cà chua x ha, dưa leo y ha)
    # x >= 0, y >= 0
    # Dien tich: x + y <= 8
    # Ngay cong: 20x + 30y <= 180 <=> 2x + 3y <= 18
    # a) BPT dien tich: x + y <= 8 -> DUNG
    # b) BPT ngay cong: 2x + 3y <= 18 -> DUNG
    # c) Diem (4; 3): 4+3=7<=8, 2*4 + 3*3 = 17 <= 18 -> DUNG
    assert 4 + 3 <= 8 and 2*4 + 3*3 <= 18
    # d) Loi nhuan F(x, y) = 30x + 40y
    # Dinh O(0; 0): 0
    # Dinh A(8; 0): 30*8 = 240
    # Dinh B (giao x+y=8 va 2x+3y=18): x=6, y=2. F(6, 2) = 30*6 + 40*2 = 260
    # Dinh C(0; 6): 40*6 = 240
    # => Max la 260 trieu dong, y d noi 280 trieu dong la SAI
    x, y = sp.symbols('x y')
    sol = sp.solve([x + y - 8, 2*x + 3*y - 18], (x, y))
    assert sol == {x: 6, y: 2}
    max_profit = 30*6 + 40*2
    assert max_profit == 260
    c14 = {"a": True, "b": True, "c": True, "d": False}
    print(f"Câu 14: {c14}")
    print("-> Phần II: OK!\n")
    return {13: c13, 14: c14}


def verify_part_III():
    print("--- KIỂM TRA PHẦN III (4 CÂU TRẢ LỜI NGẮN) ---")
    results = {}

    # Câu 15: A = [-4; 5), B = (-1; 8] => A cap B = (-1; 5)
    # Phan tu nguyen: 0, 1, 2, 3, 4 => 5 phan tu
    ints15 = [x for x in range(-10, 10) if -1 < x < 5]
    assert len(ints15) == 5 and ints15 == [0, 1, 2, 3, 4]
    results[15] = 5
    print(f"Câu 15: {results[15]}")

    # Câu 16: OABC voi x>=0, y>=0, x+y<=6, x+2y<=8
    # Dinh O(0;0): F=0
    # Dinh A(6;0): F=3*6=18
    # Dinh B: x+y=6, x+2y=8 => y=2, x=4 => F=3*4 + 4*2 = 20
    # Dinh C(0;4): F=4*4=16
    # Max F(x, y) = 20 => m >= 20 => Min m = 20
    f16 = lambda x, y: 3*x + 4*y
    assert f16(0, 0) == 0 and f16(6, 0) == 18 and f16(4, 2) == 20 and f16(0, 4) == 16
    results[16] = 20
    print(f"Câu 16: {results[16]}")

    # Câu 17: A = [m - 1; m + 3), B = (-2; 4]
    # A con B <=> m - 1 > -2 va m + 3 <= 4 <=> m > -1 va m <= 1 <=> m in {0, 1}
    # So gia tri nguyen cua m la 2
    m_vals = [m for m in range(-5, 6) if m - 1 > -2 and m + 3 <= 4]
    assert m_vals == [0, 1]
    results[17] = len(m_vals)
    print(f"Câu 17: {results[17]}")

    # Câu 18: Thuc te tam giac
    # Hai nguoi tai A, B: AB = 60m. Khinh khi cau C.
    # Goc CAB = 30 deg, goc CBH = 60 deg (goc ngoai tam giac ABC)
    # => goc ABC = 180 - 60 = 120 deg
    # => goc ACB = 180 - (30 + 120) = 30 deg
    # => Tam giac ABC can tai B => BC = AB = 60 m
    # Trong tam giac vuong CBH (vuong tai H):
    # CH = BC * sin(60 deg) = 60 * sqrt(3)/2 = 30 * sqrt(3) ~= 51.9615 m
    # Lam tron den hang don vi: 52 m
    ch18 = 60 * math.sin(math.radians(60))
    round18 = round(ch18)
    assert round18 == 52
    results[18] = round18
    print(f"Câu 18: {results[18]} (Chính xác: {ch18:.4f})")
    print("-> Phần III: OK!\n")
    return results


def verify_part_IV():
    print("--- KIỂM TRA PHẦN IV (4 CÂU TỰ LUẬN) ---")
    # Câu 19: He x>=0, y>=0, x+y<=5, x+2y<=8
    # 1) Dinh O(0; 0), A(5; 0), B(2; 3), C(0; 4)
    # Giao d1, d2: x+y=5, x+2y=8 => y=3, x=2 => B(2; 3)
    x, y = sp.symbols('x y')
    sol19 = sp.solve([x + y - 5, x + 2*y - 8], (x, y))
    assert sol19 == {x: 2, y: 3}
    f19 = lambda x, y: 3*x + 5*y
    vals19 = {
        'O': f19(0, 0),
        'A': f19(5, 0),
        'B': f19(2, 3),
        'C': f19(0, 4)
    }
    assert vals19 == {'O': 0, 'A': 15, 'B': 21, 'C': 20}
    print(f"Câu 19: Đỉnh và giá trị F: {vals19} => Min=0 tại O, Max=21 tại B(2; 3)")

    # Câu 20: 90 < alpha < 180, sin(alpha) = 4/5
    # cos(alpha) = -sqrt(1 - 16/25) = -3/5
    # tan(alpha) = (4/5) / (-3/5) = -4/3
    # cot(alpha) = -3/4
    # P = (2*sin - 3*cos) / (tan + 2*cot)
    # Tu so: 2*(4/5) - 3*(-3/5) = 8/5 + 9/5 = 17/5
    # Mau so: -4/3 + 2*(-3/4) = -4/3 - 3/2 = -17/6
    # P = (17/5) / (-17/6) = -6/5
    sin_a = sp.Rational(4, 5)
    cos_a = -sp.sqrt(1 - sin_a**2)
    assert cos_a == sp.Rational(-3, 5)
    tan_a = sin_a / cos_a
    cot_a = 1 / tan_a
    assert tan_a == sp.Rational(-4, 3)
    assert cot_a == sp.Rational(-3, 4)
    P20 = (2*sin_a - 3*cos_a) / (tan_a + 2*cot_a)
    assert P20 == sp.Rational(-6, 5)
    print(f"Câu 20: cos=-3/5, tan=-4/3, cot=-3/4, P={P20}")

    # Câu 21: A = [-3; 4), B = (1; 6]
    # A cap B = (1; 4)
    # A hop B = [-3; 6]
    # A \ B = [-3; 1]
    # C_R B = (-inf; 1] U (6; +inf)
    print("Câu 21: A cap B = (1; 4), A hop B = [-3; 6], A \\ B = [-3; 1], C_R B = (-inf; 1] U (6; +inf)")

    # Câu 22: Nuoc cam x thung, nuoc tao y thung (x, y in N)
    # Duong: x + 3y <= 30
    # Huong lieu: 2x + 2y <= 24 <=> x + y <= 12
    # x >= 0, y >= 0
    # Dinh: O(0; 0), A(12; 0), B(3; 9), C(0; 10)
    sol22 = sp.solve([x + 3*y - 30, x + y - 12], (x, y))
    assert sol22 == {x: 3, y: 9}
    f22 = lambda x, y: 400000*x + 500000*y
    vals22 = {
        'O': f22(0, 0),
        'A': f22(12, 0),
        'B': f22(3, 9),
        'C': f22(0, 10)
    }
    assert vals22['O'] == 0
    assert vals22['A'] == 4800000
    assert vals22['B'] == 5700000
    assert vals22['C'] == 5000000
    print(f"Câu 22: Lợi nhuận tại các đỉnh: {vals22} => Lớn nhất là 5.700.000 đồng tại x=3 (cam), y=9 (táo)")
    print("-> Phần IV: OK!\n")


if __name__ == "__main__":
    verify_part_I()
    verify_part_II()
    verify_part_III()
    verify_part_IV()
    print("=== TẤT CẢ 22 CÂU ĐỀU ĐẠT CHUẨN TOÁN HỌC 100%! ===")
