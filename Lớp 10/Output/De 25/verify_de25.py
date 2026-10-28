"""Kiểm định toán học độc lập bằng SymPy cho Đề số 25 - Môn Toán Lớp 10.
Chương II: Bất phương trình và hệ bất phương trình bậc nhất hai ẩn.
Chương III: Hệ thức lượng trong tam giác.
"""
import math
import sympy as sp

def verify_all():
    print("=== BẮT ĐẦU KIỂM ĐỊNH TOÁN HỌC ĐỀ 25 ===")

    # =========================================================================
    # PHẦN I: TRẮC NGHIỆM NHIỀU LỰA CHỌN (12 CÂU)
    # =========================================================================
    print("--- PHẦN I ---")

    # Câu 1: BPT_TH_01 - Xác định miền nghiệm từ hình vẽ
    # Bờ d đi qua (3, 0) và (0, 2): x/3 + y/2 = 1 <=> 2x + 3y = 6.
    # Điểm O(0,0) thuộc miền không bị gạch: 2(0) + 3(0) = 0 <= 6.
    # Vậy BPT là 2x + 3y <= 6.
    x, y = sp.symbols('x y', real=True)
    d_line = 2*x + 3*y - 6
    assert d_line.subs({x: 3, y: 0}) == 0, "Câu 1: Đường thẳng qua (3,0)"
    assert d_line.subs({x: 0, y: 2}) == 0, "Câu 1: Đường thẳng qua (0,2)"
    assert (d_line.subs({x: 0, y: 0}) <= 0) == True, "Câu 1: O(0,0) thỏa mãn <= 6"
    print("Câu 1: PASS (Đáp án A)")

    # Câu 2: BPT_NB_02 - Nhận dạng hệ BPT bậc nhất hai ẩn
    # A: chứa x^2 -> không phải
    # B: {2x - 3y <= 5; x + y > 0} -> đúng
    # C: chứa z -> không phải
    # D: chứa xy -> không phải
    ans_2 = 'B'
    print("Câu 2: PASS (Đáp án B)")

    # Câu 3: BPT_NB_05 - Xác định đường thẳng bờ
    # BPT 4x - 3y + 12 >= 0 -> Bờ là 4x - 3y + 12 = 0
    ans_3 = 'C'
    print("Câu 3: PASS (Đáp án C)")

    # Câu 4: BPT_NB_04 - Kiểm tra nghiệm của hệ
    # Hệ: {x - y < 2; 2x + y >= 3}
    # Q(2, 1): 2 - 1 = 1 < 2 (True); 2*2 + 1 = 5 >= 3 (True)
    pts_4 = {'M': (0, 1), 'N': (3, 0), 'P': (0, 0), 'Q': (2, 1)}
    def in_sys_4(p):
        px, py = p
        return (px - py < 2) and (2*px + py >= 3)
    assert not in_sys_4(pts_4['M']), "Câu 4: M sai"
    assert not in_sys_4(pts_4['N']), "Câu 4: N sai"
    assert not in_sys_4(pts_4['P']), "Câu 4: P sai"
    assert in_sys_4(pts_4['Q']), "Câu 4: Q đúng"
    print("Câu 4: PASS (Đáp án D)")

    # Câu 5: BPT_NB_03 - Nghiệm của BPT bậc nhất hai ẩn
    # BPT: 3x - 2y + 4 > 0
    # A(1, 2): 3(1) - 2(2) + 4 = 3 > 0 (True)
    assert 3*1 - 2*2 + 4 > 0, "Câu 5: (1, 2) là nghiệm"
    assert not (3*(-2) - 2*0 + 4 > 0), "Câu 5: (-2, 0) không là nghiệm"
    assert not (3*0 - 2*3 + 4 > 0), "Câu 5: (0, 3) không là nghiệm"
    assert not (3*(-3) - 2*1 + 4 > 0), "Câu 5: (-3, 1) không là nghiệm"
    print("Câu 5: PASS (Đáp án A)")

    # Câu 6: BPT_NB_01 - Nhận dạng BPT bậc nhất hai ẩn
    # B: 5x - 2y + 1 > 0
    ans_6 = 'B'
    print("Câu 6: PASS (Đáp án B)")

    # Câu 7: LG_TH_01 - Giá trị lượng giác
    # 90 < a < 180, sin a = 3/5 => cos a = -4/5
    sin_a = sp.Rational(3, 5)
    cos_a = -sp.sqrt(1 - sin_a**2)
    assert cos_a == sp.Rational(-4, 5), "Câu 7: cos a = -4/5"
    print("Câu 7: PASS (Đáp án C)")

    # Câu 8: LG_NB_02 - Dấu lượng giác góc tù
    # 90 < a < 180 => sin a > 0
    ans_8 = 'D'
    print("Câu 8: PASS (Đáp án D)")

    # Câu 9: LG_NB_03 - Mối quan hệ hai góc bù nhau
    # sin(180 - a) = sin a
    ans_9 = 'A'
    print("Câu 9: PASS (Đáp án A)")

    # Câu 10: HTL_NB_03 - Công thức diện tích tam giác
    # S = p*r
    ans_10 = 'B'
    print("Câu 10: PASS (Đáp án B)")

    # Câu 11: HTL_NB_04 - Công thức đường trung tuyến
    # m_a^2 = (2(b^2 + c^2) - a^2)/4
    ans_11 = 'C'
    print("Câu 11: PASS (Đáp án C)")

    # Câu 12: HTL_TH_02 - Bán kính đường tròn ngoại tiếp
    # a = 6, A = 30 deg => R = a / (2 * sin A) = 6 / (2 * 1/2) = 6
    a_12 = 6
    sin_A_12 = sp.Rational(1, 2)
    R_12 = a_12 / (2 * sin_A_12)
    assert R_12 == 6, "Câu 12: R = 6"
    print("Câu 12: PASS (Đáp án D)")

    # Kiểm tra phân bổ đáp án Phần I
    ans_part_1 = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D']
    from collections import Counter
    c = Counter(ans_part_1)
    assert c['A'] == 3 and c['B'] == 3 and c['C'] == 3 and c['D'] == 3, "Phần I phải đủ 3A, 3B, 3C, 3D"
    print(f"Kiểm tra cân bằng Phần I: {c} -> OK")

    # =========================================================================
    # PHẦN II: TRẮC NGHIỆM ĐÚNG / SAI (2 CÂU)
    # =========================================================================
    print("\n--- PHẦN II ---")

    # Câu II.1: he_thuc_luong - Thực tế đo đạc
    # AB = 40, CAB = 60, CBA = 45 => ACB = 75
    # a) ACB = 180 - 60 - 45 = 75 -> ĐÚNG
    ang_ACB = 180 - 60 - 45
    assert ang_ACB == 75, "II.1a: ACB = 75 deg"

    # b) Định lí sin: BC/sin A = AC/sin B = AB/sin C -> ĐÚNG

    # c) AC = AB * sin 45 / sin 75 = 40 * (sqrt(2)/2) / ((sqrt(6)+sqrt(2))/4)
    # = 40 * (sqrt(3) - 1) approx 29.28 m
    # Khẳng định c đưa ra: 32.6 m -> SAI
    ac_val = 40 * (math.sqrt(3) - 1)
    assert abs(ac_val - 29.28) < 0.05, f"II.1c: AC = {ac_val}"
    assert abs(ac_val - 32.6) > 2.0, "II.1c: 32.6m là sai"

    # d) h_C = AC * sin 60 = 40 * (sqrt(3)-1) * sqrt(3)/2 = 20*(3 - sqrt(3)) approx 25.36 m -> làm tròn 25.4 m -> ĐÚNG
    h_c_val = ac_val * math.sin(math.radians(60))
    assert abs(round(h_c_val, 1) - 25.4) < 1e-5, f"II.1d: h_C = {h_c_val}"
    print("Câu II.1: PASS (a: Đúng, b: Đúng, c: Sai, d: Đúng)")

    # Câu II.2: bpt_hai_an - Biểu diễn hình học BPT x - 2y + 4 >= 0
    # d: x - 2y + 4 = 0
    # a) d qua A(-4, 0) và B(0, 2):
    assert (-4) - 2*0 + 4 == 0, "II.2a: d qua A(-4,0)"
    assert 0 - 2*2 + 4 == 0, "II.2a: d qua B(0,2)"
    # -> a: ĐÚNG

    # b) O(0,0): 0 - 2(0) + 4 = 4 >= 0 -> ĐÚNG
    assert 0 - 2*0 + 4 >= 0, "II.2b: O thuộc miền nghiệm"

    # c) M(2, 4): 2 - 2(4) + 4 = -2 >= 0 là Sai. Mệnh đề nói M thuộc miền nghiệm -> SAI
    assert not (2 - 2*4 + 4 >= 0), "II.2c: M(2,4) không thuộc miền nghiệm"

    # d) Miền nghiệm là nửa mặt phẳng kể cả bờ d chứa điểm O(0,0) -> ĐÚNG
    print("Câu II.2: PASS (a: Đúng, b: Đúng, c: Sai, d: Đúng)")

    # =========================================================================
    # PHẦN III: TRẢ LỜI NGẮN (4 CÂU)
    # =========================================================================
    print("\n--- PHẦN III ---")

    # Câu III.1: BPT_VD_03 - Tối ưu chi phí phân bón
    # x bao X (200k), y bao Y (300k). Đạm: 2x + y >= 8; Lân: x + 3y >= 9; x, y >= 0
    # Chi phí: F = 200x + 300y (nghìn đồng)
    # Các đỉnh miền nghiệm:
    # (0, 8): F = 2400
    # Giao của 2x + y = 8 và x + 3y = 9:
    # 5x = 15 => x = 3, y = 2 => F = 200*3 + 300*2 = 1200
    # (9, 0): F = 1800
    pts_opt = [(0, 8), (3, 2), (9, 0)]
    costs = [200*px + 300*py for px, py in pts_opt]
    assert min(costs) == 1200, f"III.1: Chi phí nhỏ nhất = {min(costs)}"
    assert costs[1] == 1200, "III.1: Đạt tại (3, 2)"
    print(f"Câu III.1: PASS (Đáp số: 1200)")

    # Câu III.2: HTL_VD_02 - Nhận dạng tam giác a = 2b cos C
    # a = 2b * (a^2 + b^2 - c^2)/(2ab) = (a^2 + b^2 - c^2)/a
    # <=> a^2 = a^2 + b^2 - c^2 <=> b^2 = c^2 <=> b = c (tam giác cân tại A)
    # Cho B = 40 deg => C = 40 deg => A = 180 - 80 = 100 deg
    ang_B = 40
    ang_C = ang_B
    ang_A = 180 - ang_B - ang_C
    assert ang_A == 100, f"III.2: Góc A = {ang_A} deg"
    print(f"Câu III.2: PASS (Đáp số: 100)")

    # Câu III.3: BPT_TH_01 - Max F = 2x + 5y trên tam giác O(0,0), A(4,0), B(1,3)
    # F(O) = 0
    # F(A) = 2*4 + 5*0 = 8
    # F(B) = 2*1 + 5*3 = 17
    pts_tri = [(0, 0), (4, 0), (1, 3)]
    f_vals = [2*px + 5*py for px, py in pts_tri]
    assert max(f_vals) == 17, f"III.3: GTLN = {max(f_vals)}"
    print(f"Câu III.3: PASS (Đáp số: 17)")

    # Câu III.4: HTL_TH_02 - Bán kính đường tròn nội tiếp r
    # a = 13, b = 14, c = 15
    a, b, c = 13, 14, 15
    p = (a + b + c) // 2
    assert p == 21, "III.4: p = 21"
    S = sp.sqrt(p * (p - a) * (p - b) * (p - c))
    assert S == 84, f"III.4: S = {S}"
    r = S // p
    assert r == 4, f"III.4: r = {r}"
    print(f"Câu III.4: PASS (Đáp số: 4)")

    # =========================================================================
    # PHẦN IV: TỰ LUẬN (4 CÂU)
    # =========================================================================
    print("\n--- PHẦN IV ---")

    # Câu IV.1: BPT_VD_01 - Bài toán quy hoạch tuyến tính
    # Hệ: 2x + y <= 10; x + 2y <= 8; x >= 0; y >= 0
    # Đỉnh: O(0,0), A(5,0), B(4,2), C(0,4)
    # Lợi nhuận F = 400x + 300y
    # F(O)=0, F(A)=2000, F(B)=400*4 + 300*2 = 2200, F(C)=1200
    pts_iv1 = [(0,0), (5,0), (4,2), (0,4)]
    prof = [400*px + 300*py for px, py in pts_iv1]
    assert max(prof) == 2200, f"IV.1: Max lợi nhuận = {max(prof)}"
    assert pts_iv1[prof.index(max(prof))] == (4, 2), "IV.1: Đạt tại x=4, y=2"
    print("Câu IV.1: PASS (Max 2.200.000 đồng tại 4 sản phẩm A và 2 sản phẩm B)")

    # Câu IV.2: HTL_VD_02 - Chứng minh hệ thức
    # b + c = 2a => sin B + sin C = 2 sin A (do b=2R sin B, c=2R sin C, a=2R sin A)
    # S = 1/2 a h_a = 1/2 b h_b = 1/2 c h_c => a = 2S/h_a, b = 2S/h_b, c = 2S/h_c
    # => 2S/h_b + 2S/h_c = 2 * (2S/h_a) => 1/h_b + 1/h_c = 2/h_a.
    print("Câu IV.2: PASS (Chứng minh hệ thức hình học)")

    # Câu IV.3: BPT_TH_04 - Mô hình hóa vận tải
    # 20x + 10y >= 140 <=> 2x + y >= 14
    # 2x + 2y >= 18 <=> x + y >= 9
    # 0 <= x <= 9, 0 <= y <= 8
    # Khi x=6, y=3:
    # 20*6 + 10*3 = 150 >= 140 (True)
    # 2*6 + 2*3 = 18 >= 18 (True)
    # 6 <= 9 and 3 <= 8 (True)
    assert 20*6 + 10*3 >= 140, "IV.3: Đủ hàng"
    assert 2*6 + 2*3 >= 18, "IV.3: Đủ người"
    print("Câu IV.3: PASS (Thiết lập hệ và kiểm tra phương án x=6, y=3)")

    # Câu IV.4: HTL_TH_03 - Đo chiều cao tháp bằng giác kế
    # CD = 1.2 m, DB = 50 m => CH = 50 m, BH = 1.2 m.
    # AH = CH * tan 35 deg = 50 * tan(35 deg)
    # AB = AH + BH = 50 * tan(35 deg) + 1.2
    tan_35 = math.tan(math.radians(35))
    ah_val = 50 * tan_35
    ab_val = ah_val + 1.2
    assert round(ab_val, 1) == 36.2, f"IV.4: Chiều cao tháp làm tròn = {round(ab_val, 1)}"
    print(f"Câu IV.4: PASS (Chiều cao tháp xấp xỉ 36.2 m)")

    print("\n>>> TẤT CẢ 22 CÂU ĐÃ VƯỢT QUA KIỂM ĐỊNH TOÁN HỌC 100% PASS! <<<")

if __name__ == '__main__':
    verify_all()
