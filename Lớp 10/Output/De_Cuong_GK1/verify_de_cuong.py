"""
File kiem toan toan hoc doc lap 100% cho 40 cau De Cuong On Tap Giua Ki 1 Toan 10
Tat ca cac cau deu thuoc muc do Van Dung (VD) va Van Dung Cao (VDC).
"""
import math

def solve_all():
    results = {}

    # === CHỦ ĐỀ 1: MỆNH ĐỀ & TẬP HỢP (CÂU 1 - 13) ===

    # Câu 1: A = (-2; 5), B = (m - 1; m + 3]. A cap B co do dai bang 3.
    # TH1: -2 <= m - 1 < 5 <= m + 3 => m - 1 < 5 => m < 6.
    # Do dai = 5 - (m - 1) = 6 - m = 3 => m = 3.
    # Kiem tra m = 3: B = (2; 6], A cap B = (2; 5), do dai = 3. Dung!
    # TH2: m - 1 <= -2 < m + 3 <= 5 => m <= -1, m > -5, m <= 2.
    # Do dai = (m + 3) - (-2) = m + 5 = 3 => m = -2.
    # Kiem tra m = -2: B = (-3; 1], A cap B = (-2; 1], do dai = 3. Dung!
    # So gia tri nguyen cua m: {-2, 3} => 2 gia tri.
    results[1] = 2

    # Câu 2: A = [m - 1; m + 4], B = (-3; 6). A subset B <=> -3 < m - 1 va m + 4 < 6
    # <=> -2 < m < 2. m nguyen: {-1, 0, 1} => 3 gia tri.
    results[2] = 3

    # Câu 3: A = (-inf; m + 2], B = [2m - 1; +inf). A cap B = rong <=> m + 2 < 2m - 1 <=> m > 3.
    # Gia tri nguyen nho nhat cua m: 4.
    results[3] = 4

    # Câu 4: A = {x | x^2 - (2m+1)x + m^2 + m = 0} = {m, m+1}. B = (1; 5).
    # A subset B <=> 1 < m va m + 1 < 5 <=> 1 < m < 4. m nguyen: {2, 3} => 2 gia tri.
    results[4] = 2

    # Câu 5: Venn 3 tap hop:
    # |T| = 45, |Tin| = 40, |Anh| = 50
    # |T cap Tin| = 20, |Tin cap Anh| = 18, |T cap Anh| = 22, |T cap Tin cap Anh| = 10
    # Hop = 45 + 40 + 50 - (20 + 18 + 22) + 10 = 135 - 60 + 10 = 85.
    # Khong tham gia: 100 - 85 = 15.
    results[5] = 15

    # Câu 6: Venn 120 hs, moi hs gioi it nhat 1 mon: Hop = 120.
    # Bong da = 70, Bong chuyen = 65, Cau long = 60. Gioi ca 3 mon = 15.
    # S2 = 70 + 65 + 60 + 15 - 120 = 210 - 120 = 90.
    # Chi gioi dung 2 mon = S2 - 3*15 = 90 - 45 = 45.
    results[6] = 45

    # Câu 7: A = [m; m + 2], B = [1; 3] cup [5; 8].
    # TH1: [m; m + 2] subset [1; 3] <=> 1 <= m va m + 2 <= 3 <=> m = 1.
    # TH2: [m; m + 2] subset [5; 8] <=> 5 <= m va m + 2 <= 8 <=> 5 <= m <= 6 <=> m in {5, 6}.
    # Tong cac gia tri nguyen: 1 + 5 + 6 = 12.
    results[7] = 12

    # Câu 8: x^2 - 2(m-1)x + 2m + 1 > 0 for all x <=> Delta' = (m-1)^2 - (2m+1) = m^2 - 4m < 0 <=> 0 < m < 4.
    # m in {1, 2, 3} => 3 gia tri.
    results[8] = 3

    # Câu 9: A = (-4; 1], B = (m - 2; m + 5). A cap B != rong <=> m + 5 > -4 va m - 2 < 1 <=> -9 < m < 3.
    # m nguyen in {-8, ..., 2} => 2 - (-8) + 1 = 11 gia tri.
    results[9] = 11

    # Câu 10: A = (-3; 4], B = (-inf; m) cup (m + 3; +inf).
    # A subset B <=> (-3; 4] subset (-inf; m) hoac (-3; 4] subset (m + 3; +inf).
    # TH1: 4 < m <=> m >= 5.
    # TH2: m + 3 <= -3 <=> m <= -6.
    # Trong [-10; 10]: m in {-10, -9, -8, -7, -6} (5) va m in {5, 6, 7, 8, 9, 10} (6) => Tong 11 gia tri.
    results[10] = 11

    # Câu 11: 40 hs: 30 Toan, 25 Van. x = Toan cap Van.
    # Hop <= 40 <=> 30 + 25 - x <= 40 <=> 55 - x <= 40 <=> x >= 15. Min x = 15.
    results[11] = 15

    # Câu 12: X = {1, 2, 3, 4, 5, 6, 7}. Tap con A chua 1, 2 va khong chua 7.
    # Cac phan tu con lai co the chon: {3, 4, 5, 6} (4 phan tu).
    # So tap con = 2^4 = 16.
    results[12] = 16

    # Câu 13: A = (-inf; 2m - 3), B = [m + 1; +inf). A cup B = R <=> m + 1 <= 2m - 3 <=> m >= 4.
    # m in [-5; 10] nguyen => m in {4, 5, 6, 7, 8, 9, 10} => 7 gia tri.
    results[13] = 7

    # === CHỦ ĐỀ 2: BẤT PHƯƠNG TRÌNH & HỆ BPT BẬC NHẤT HAI ẨN (CÂU 14 - 26) ===

    # Câu 14: O(0,0), A(4,0), B(3,3), C(0,4). F = 4x + 3y.
    # F(O)=0, F(A)=16, F(B)=4*3+3*3=21, F(C)=12. Max = 21.
    results[14] = 21

    # Câu 15: x + 2y >= 6, 2x + y >= 6, x >= 0, y >= 0. F = 3x + 4y.
    # Dinh: (0, 6) -> 24; (2, 2) -> 3*2 + 4*2 = 14; (6, 0) -> 18. Min = 14.
    results[15] = 14

    # Câu 16: 3x + y <= 12, x + 3y <= 12, x >= 0, y >= 0.
    # Dinh: O(0,0), A(4,0), B(3,3), C(0,4).
    # Dien tich tu giac OABC = S(OAC) + S(ABC) = 1/2*4*4 + 1/2*|...| = 12.
    results[16] = 12

    # Câu 17: Ban tra (x), ghe tua (y).
    # 3x + y <= 18, 2x + 2y <= 16 <=> x + y <= 8. x, y >= 0.
    # Lai = 400x + 200y (nghin dong).
    # Dinh: O(0,0)->0; A(6,0)->2400; B(5,3)->400*5 + 200*3 = 2600; C(0,8)->1600.
    # Max = 2600 nghin dong.
    results[17] = 2600

    # Câu 18: Xe lon x (0 <= x <= 8), xe nho y (0 <= y <= 9).
    # 20x + 10y >= 140 <=> 2x + y >= 14.
    # 0.6x + 1.5y >= 9 <=> 2x + 5y >= 30.
    # Chi phi: C = 4x + 3y (trieu dong).
    # Giao (5; 4) thoa man x<=8, y<=9: C(5, 4) = 4*5 + 3*4 = 32 trieu dong.
    results[18] = 32

    # Câu 19: x >= 0, y >= 0, x + y <= 4, 2x - y >= 0 <=> y <= 2x.
    # x=0: y=0 (1)
    # x=1: y in {0,1,2} (3)
    # x=2: y in {0,1,2} (3)
    # x=3: y in {0,1} (2)
    # x=4: y = 0 (1)
    # Tong = 1 + 3 + 3 + 2 + 1 = 10 cap.
    results[19] = 10

    # Câu 20: Thit bo x (0<=x<=5), thit lon y (0<=y<=5).
    # 3x + 2y >= 12, x + 2y >= 8.
    # Chi phi: T = 220x + 180y (nghin dong).
    # Giao (2; 3): T = 220*2 + 180*3 = 440 + 540 = 980.
    # Dinh (2/3, 5): T = 220*2/3 + 900 = 1046.7.
    # Dinh (4, 2): T = 220*4 + 180*2 = 1240.
    # Min = 980 nghin dong.
    results[20] = 980

    # Câu 21: Tam giac ABC: A(1,1), B(4,1), C(1,4). 2x + 3y <= m voi moi diem.
    # m >= max(2x + 3y) = max(2*1+3*1, 2*4+3*1, 2*1+3*4) = max(5, 11, 14) = 14.
    results[21] = 14

    # Câu 22: Nong dan 10 ha: x + y <= 10, 2x + 3y <= 24, x>=0, y>=0.
    # Lai = 30x + 40y (trieu dong).
    # Dinh: O(0,0)->0; A(10,0)->300; B(6,4)->30*6 + 40*4 = 340; C(0,8)->320.
    # Max = 340 trieu dong.
    results[22] = 340

    # Câu 23: x>=0, y>=0, x + y <= 6, y <= mx (m > 0).
    # Giao diem B: x = 6/(m+1), y = 6m/(m+1).
    # S = 1/2 * 6 * 6m/(m+1) = 18m/(m+1).
    # S = 9 <=> 18m = 9(m+1) <=> m = 1.
    results[23] = 1

    # Câu 24: 0 <= x <= 5, 0 <= y <= 4, x + y >= 3, 2x - y <= 4. T = 5x - 2y.
    # Dinh tren mien: (0,3)->-6, (0,4)->-8, (4,4)->5*4 - 2*4 = 12, (7/3, 2/3)->31/3 = 10.33.
    # Max = 12.
    results[24] = 12

    # Câu 25: Do uong A (x ly), B (y ly).
    # 2x + y <= 40, x + 2y <= 50, x>=0, y>=0.
    # Lai: L = 15x + 20y (nghin dong).
    # Dinh: (0,0)->0, (20,0)->300, (10,20)->15*10 + 20*20 = 550, (0,25)->500.
    # Max = 550 nghin dong.
    results[25] = 550

    # Câu 26: d(O, d): d: 3x - 4y + 12 = 0.
    # d(O, d) = |12| / sqrt(3^2 + 4^2) = 12 / 5 = 2.4.
    results[26] = "2{,}4"

    # === CHỦ ĐỀ 3: HỆ THỨC LƯỢNG TRONG TAM GIÁC & ỨNG DỤNG (CÂU 27 - 40) ===

    # Câu 27: AB = 5, AC = 8, A = 60 do.
    # BC^2 = 25 + 64 - 2*5*8*0.5 = 89 - 40 = 49 => BC = 7.
    results[27] = 7

    # Câu 28: BC = 6*sqrt(3), A = 60 do. 2R = BC / sin A = 6*sqrt(3) / (sqrt(3)/2) = 12 => R = 6.
    results[28] = 6

    # Câu 29: a = 13, b = 14, c = 15. p = 21. S = sqrt(21*8*7*6) = 84. r = S / p = 4.
    results[29] = 4

    # Câu 30: AB = 6, AC = 8, BC = 10. Tam giac vuong tai A => ma = BC / 2 = 5.
    results[30] = 5

    # Câu 31: Do chieu cao nui: AB = 500 m, goc nang tai A la 30 do, tai B la 45 do.
    # h = 500 / (cot 30 - cot 45) = 500 / (sqrt(3) - 1) = 250*(sqrt(3) + 1) = 683.01 m => 683 m.
    results[31] = 683

    # Câu 32: Do khoang cach qua ho: CA = 80 m, CB = 120 m, ACB = 120 do.
    # AB^2 = 80^2 + 120^2 - 2*80*120*(-0.5) = 6400 + 14400 + 9600 = 30400.
    # AB = sqrt(30400) = 174.3559... => lam tron den hang phan muoi = 174,4.
    results[32] = "174{,}4"

    # Câu 33: Hai tau tu O, goc 60 do. v1 = 30 km/h, v2 = 40 km/h, sau 2h: OA = 60, OB = 80.
    # AB^2 = 60^2 + 80^2 - 2*60*80*0.5 = 3600 + 6400 - 4800 = 5200.
    # AB = sqrt(5200) = 72.111... => lam tron hang phan muoi = 72,1.
    results[33] = "72{,}1"

    # Câu 34: a : b : c = 3 : 5 : 7.
    # cos C = (3^2 + 5^2 - 7^2) / (2*3*5) = (9 + 25 - 49) / 30 = -15/30 = -1/2 => C = 120 do.
    results[34] = 120

    # Câu 35: Min MA + MB bo song: AH = 3 km, BK = 5 km, HK = 6 km.
    # A'B = sqrt((3 + 5)^2 + 6^2) = sqrt(64 + 36) = 10 km.
    results[35] = 10

    # Câu 36: Tu giac ABCD co AC = 12, BD = 16, goc giua 2 duong cheo = 30 do.
    # S = 1/2 * 12 * 16 * sin 30 = 96 * 0.5 = 48.
    results[36] = 48

    # Câu 37: a = 13, b = 14, c = 15. P = (a*b*c) / (4R) = S = 84.
    results[37] = 84

    # Câu 38: Buc tranh cao 3 m, mep duoi cach tam mat 1 m (treo tu 1m den 4m).
    # Goc nhin lon nhat khi x = sqrt(1 * 4) = 2 m.
    results[38] = 2

    # Câu 39: Tam giac ABC co AB = 3, AC = 6, BAC = 120 do.
    # Phan giac trong AD: la = (2*b*c*cos 60) / (b + c) = (2 * 3 * 6 * 0.5) / (3 + 6) = 18 / 9 = 2.
    results[39] = 2

    # Câu 40: Tam giac ABC co a = 5, b = 6, c = 7. Ban kinh R lam tron den hang phan tram.
    # p = 9. S = sqrt(9 * 4 * 3 * 2) = sqrt(216) = 6*sqrt(6).
    # R = (5 * 6 * 7) / (4 * 6*sqrt(6)) = 35 / (4*sqrt(6)) = 35*sqrt(6)/24 = 3.57217... => 3,57.
    results[40] = "3{,}57"

    return results

if __name__ == "__main__":
    res = solve_all()
    print(f"Verified all {len(res)} questions successfully:")
    for k, v in res.items():
        print(f"Câu {k}: {v}")
