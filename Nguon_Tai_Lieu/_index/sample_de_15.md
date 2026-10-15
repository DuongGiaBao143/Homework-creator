# NGUỒN THAM KHẢO TỰ ĐỘNG CHO ĐỀ SỐ 15 (ƯU TIÊN VẬN DỤNG CAO & THỰC TẾ 9+)

> **CHỈ THỊ BẮT BUỘC CHO AGENT (THEO GEMINI.MD):**
> 1. **Tuyệt đối không dùng hàm hợp $g(x)=f(u(x))$** hoặc tích phân hàm ẩn máy móc. Nếu trong đoạn trích có xuất hiện câu hàm hợp (do nằm chung trang PDF), hãy BỎ QUA câu đó và chỉ lấy câu Thực tế / Phân thức bậc 2 trên bậc 1 / Tối ưu.
> 2. **Khu vực I chứa ngữ liệu Vận dụng cao & Mô hình hóa thực tế**. Dùng để chế tác **4 câu Phần II (Đúng/Sai)**, ngữ liệu Phần III và 3 câu phân loại cuối Phần I.

> 3. **PHẦN III LÀ PHẦN CHẶN ĐIỂM: ít nhất 2/6 câu khó phải lấy hoặc chế tác từ đúng ba tài liệu ở Khu vực 0.** Giữ nút thắt/độ khó gốc; không giản lược thành bài thay công thức. Hai đoạn của cùng một bài chỉ tính là 1 câu. Mở trang PDF gốc để xác nhận dữ kiện/hình; ghi số câu, tên file, trang PDF và nút thắt vào hồ sơ nguồn, kiểm đủ ít nhất 2 câu trước khi xuất đề. Điểm VDC chỉ hỗ trợ chọn ngữ liệu, không xác nhận độ khó.

---

# KHU VỰC 0: NGUỒN BẮT BUỘC CHO ÍT NHẤT 2 CÂU KHÓ PHẦN III

- `Phương pháp tiếp cận bài toán thực tế trong đề thi THPT QG 2026 môn Toán.pdf`
- `Vận dụng cao.pdf`
- `Phương pháp trải phẳng giải một số bài toán ứng dụng thực tế – Đặng Việt Đông.pdf`

Các đoạn dưới đây là ứng viên tham khảo; đọc PDF gốc để chọn bài đầy đủ và đủ khó.

### Nguồn: `Phương pháp tiếp cận bài toán thực tế trong đề thi THPT QG 2026 môn Toán.pdf` (page_12) — `[VDC Score: 12.5]`
```text
1. Phương pháp tiếp cận bài toán thực tếtrong đềôn thi TNTHPT 2026
11
Bài toán 6. Một cái bểnước hình nón đểngược như hình vẽ, có chiều cao a cm, bán kính
đáy bằng b cm. Một vòi nước chảy vào bểsao cho sau mỗi giây chiều cao mực nước tăng
đều lên c cm cho đến khi đầy bể. Hãy tính tốc độtăng thểtích (m3/s) của nước tại thời
điểm cách một giây ngay trước khi bểđầy. (Kết quảlàm tròn đến hàng phần trăm).
Hình 6: Minh họa Bài toán 6
Lời giải.
1) Thiết lập các hàm theo thời gian t
Gọi t (giây) là thời gian nước chảy vào. Chiều cao mực nước tăng đều c cm/s nên tại
thời điểm t:
h(t) = c t
(cm)
Dựa vào tam giác đồng dạng, bán kính mặt nước r(t) tỉlệvới chiều cao:
r(t)
h(t) = b
a ⇒r(t) = b
a h(t) = bc
a t.
2) Xây dựng hàm thểtích V(t)
Thểtích khối nước hình nón là
V = 1
3πr2h.
Thay r(t) và h(t) vào, ta được:
V(t) = 1
3π
µbc
a t
¶2
(ct) = πb2c3
3a2 t3
(cm3).
3) Tính tốc độtăng thểtích
Tốc độtăng thểtích là đạo hàm của V(t) theo t:
V '(t) = πb2c3
a2
t2
(cm3/s).
Nguyễn Hoàng Vinh
Truờng THPT chuyên Lương ThếVinh, Đồng Nai
```

### Nguồn: `Phương pháp tiếp cận bài toán thực tế trong đề thi THPT QG 2026 môn Toán.pdf` (page_13) — `[VDC Score: 11.0]`
```text
1. Phương pháp tiếp cận bài toán thực tếtrong đềôn thi TNTHPT 2026
12
4) Xác định thời điểm cần tính
Bểđầy khi chiều cao nước đạt h = a:
c tfull = a ⇒tfull = a
c.
Thời điểm một giây trước khi bểđầy:
t0 = tfull -1 = a
c -1 = a-c
c
(s).
5) Tính giá trịcụthể
Thay t0 vào công thức V '(t):
V '(t0) = πb2c3
a2
³a-c
c
´2
= πb2c
a2 (a-c)2
(cm3/s).
Lưu ý: Nếu đềbài yêu cầu đơn vịm3/s thì nhân kết quảtrên với 10-6.
Bài toán 7. Một tên trộm đang cốgắng kéo thùng nữtrang qua một bức tường có độ
dày BC = 1 m; biết rằng tường cao 4 m và sợi dây được kéo theo đường gấp khúc ABCD có
độdài không đổi bằng 20 m, đoạn BF = 0,5 m. Trong khi kéo thì tên trộm luôn ghì đầu
dây theo một thanh vịn của cầu thang (đầu dây dịch chuyển theo phương AF). Biết rằng
thanh vịn cầu thang hợp với phương ngang một góc bằng 30◦. Khi hai chú cảnh sát xuất
hiện thì vịtrí A cách F khoảng 6 m và thùng D tiến vềphía E với tốc độ1 m/s. Hỏi đầu
dây A rời xa điểm F với tốc độbao nhiêu m/s? (Làm tròn kết quảđến hàng phần trăm).
Hình 7: Minh họa Bài toán 7
Lời giải. Đặt DE = x (m), AF = y (m). Ta có CD =
p
x2 +16 và 
AFB = 180◦-60◦= 120◦.
Suy ra
AB2 = y2 +0,52 -2· y·0,5·cos120◦= y2 +0,25+0,5y.
Ta có phương trình chiều dài dây:
AB +1+CD = 20 ⇔
q
y2 +0,5y+0,25+1+
p
x2 +16 = 20.
⇔
q
y2 +0,5y+0,25+
p
x2 +16 = 19
(∗)
Nguyễn Hoàng Vinh
Truờng THPT chuyên Lương ThếVinh, Đồng Nai
```

### Nguồn: `Vận dụng cao.pdf` (page_167) — `[VDC Score: 22.0]`
```text
CHƯƠNG I. XÁC SUẤT - THỰC TẾ- THỐNG KÊ - RỜI RẠC
Teacher2kkk | Học toán cùng GenZ
Câu 474. Một cây cầu có dạng cung OA của đồthịhàm sốy = 4,8sin x
9 và được mô tảtrong hệ
trục tọa độvới đơn vịtrục là mét như ởhình vẽ
Một xà lan chởkhối hàng hóa được xếp thành hình hộp chữnhật với chiều rộng của khối hàng hóa
đó là 9 m sao cho xà lan có thểđi qua được gầm cầu (trục Ox nằm trên mặt sàn của xà lan), để
đảm bảo an toàn thì vịtrí cao nhất của thùng hàng cách mép dưới cầu 70 cm (thẳng vịtrí cao nhất
hướng lên). Tính chiều cao tối đa của khối hàng hóa đó đểxà lan có thểđi qua được gầm cầu (làm
tròn đến hàng phần trăm)
Câu 475. Một mặt cắt ngang của một tòa nhà cao tầng như hình vẽ
Một chiếc thang từxe cứu hỏa lên đến mặt tường phía trước của tòa nhà phải vượt qua phần mái
che cao 10 m so với mặt đất và vùng mái này nhô ra 12 m so với tường. Giảsửđộcao từmặt sàn
đặt thang của xe cứu hỏa là 1,2 m. Độdài ngắn nhất của chiếc thang đểcác lính cứu hỏa có thể
thực hiện nhiệm vụnày bằng bao nhiêu? (làm tròn kết quảđến hàng phần mười)
Câu 476. Trận bóng đá giao hữu giữa đội tuyển Việt Nam và Singapore ởsân vận động MỹĐình
có sức chứa 60000 khán giả. Ban tổchức bán vé với giá mỗi vé là 100 nghìn đồng, sốkhán giảtrung
bình đến sân xem bóng đá là 24000 người. Qua thăm dò dư luận, người ta thấy rằng mỗi khi giá vé
giảm thêm 10 nghìn đồng, sẽcó thêm khoảng 3000 khán giả. Hỏi ban tổchức nên đặt giá vé là bao
nhiêu đểdoanh thu từtiền bán vé là lớn nhất với đơn vịtính giá vé là nghìn đồng?
BIÊN SOẠN: TRƯƠNG CÔNG ĐẠT
Tuyển tập VD - VDC trong các đềthi thửTHPTQG | 165
H
Ọ
C
T
O
Á
N
C
Ù
N
G
G
E
N
Z
+
-
×
÷
N
N∗
Z
Q
I
R
C
R
P̸
=
log
ln
∈
/∈
∀
∄
∃
∅
∨
∧
⊄
⊂
≡
≠
=
>
<
≥
≤
√
lim
sin
cos
tan
cot
⊥
∥
Ak
n
Ck
n
α
β
γ
δ
λ
π
ϕ
φ
ex
arcsin
arccos
arctan
±∞
∪
∩
y = f(x)
⇔
⇒
≈
|
µ
ω
τ
i2 = -1
P (A|B)
0
1
2
3
4
5
6
7
8
9
a2 +b2 = c2
Pn = n!
T2
K
EACHER
```

### Nguồn: `Vận dụng cao.pdf` (page_103) — `[VDC Score: 16.0]`
```text
CHƯƠNG I. XÁC SUẤT - THỰC TẾ- THỐNG KÊ - RỜI RẠC
Teacher2kkk | Học toán cùng GenZ
Câu 313. Trong giải Billiards carom ba băng cá nhân vô địch thếgiới lần thứ76 năm 2024 tổchức
tại Bình Thuận, bốn cơ thủT (Trần Thanh Lực), D (Dick Jaspers), E (Eddy Merckx), C (Cho
Myung-woo) đã giành được quyền vào bán kết. Bốn cơ thủđang tiếp tục hành trình chinh phục vị
trí cao nhất. Trận bán kết 1, cơ thủT sẽtranh tài với cơ thủD. Trận bán kết 2, cơ thủE sẽtranh
tài với cơ thủC. Trong trận chung kết, cơ thủgiành chiến thắng ởtrận bán kết 1 sẽtranh tài với cơ
thủgiành chiến thắng ởtrận bán kết 2, cơ thủgiành chiến thắng ởtrận chung kết này được gọi là
NHÀ VÔ ĐỊCH.
Gọi mX là sốđiểm hiện có của cơ thủX (X ∈{T;D;E;C}) theo cách tính điểm của Liên đoàn bi-a thế
giới - UMB (Union Mondiale de Billard). Nếu cơ thủX tranh tài với cơ thủY (X,Y ∈{T;D;E;C})
thì xác suất đểcơ thủX giành chiến thắng là
mX
mX +mY
(không có trận hòa). Tính xác suất để
cơ thủT (Trần Thanh Lực) trởthành NHÀ VÔ ĐỊCH; biết rằng mT = 246, mD = 426, mE = 287,
mC = 352. (làm tròn kết quảđến hàng phần trăm).
Câu 314. Người nghệsĩ vẽmột bông hoa không màu trên một miếng bìa hình vuông ABCD tâm
O bằng một đường cong kín (L) rồi tô màu đen phần bên ngoài đường cong này của hình vuông như
hình vẽ.
Nếu điểm M thuộc cạnh của hình vuông ABCD và tia OM cắt (L) tại điểm N thì MN = 2 dm.
Biết rằng AB = 8 dm. Phần được nghệsĩ tô màu đen có diện tích bằng bao nhiêu centimet vuông?
(làm tròn kết quảđến hàng đơn vị)
BIÊN SOẠN: TRƯƠNG CÔNG ĐẠT
Tuyển tập VD - VDC trong các đềthi thửTHPTQG | 101
H
Ọ
C
T
O
Á
N
C
Ù
N
G
G
E
N
Z
+
-
×
÷
N
N∗
Z
Q
I
R
C
R
P̸
=
log
ln
∈
/∈
∀
∄
∃
∅
∨
∧
⊄
⊂
≡
≠
=
>
<
≥
≤
√
lim
sin
cos
tan
cot
⊥
∥
Ak
n
Ck
n
α
β
γ
δ
λ
π
ϕ
φ
ex
arcsin
arccos
arctan
±∞
∪
∩
y = f(x)
⇔
⇒
≈
|
µ
ω
τ
i2 = -1
P (A|B)
0
1
2
3
4
5
6
7
8
9
a2 +b2 = c2
Pn = n!
T2
K
EACHER
```

### Nguồn: `Phương pháp trải phẳng giải một số bài toán ứng dụng thực tế – Đặng Việt Đông.pdf` (page_55) — `[VDC Score: 22.0]`
```text
Gv: Đặng Việt Đông Trường THPT Nho Quan A Phương pháp trải phẳng 
 
 
ĐT: 0978064165 - Email: dangvietdong.ninhbinh.vn@gmail.com - ID Tik Tok: dongpay | Trang 55 
Facebook: https://www.facebook.com/dongpay - Kênh Youtube: Thầy Đặng Việt Đông 
58,79609
58,8
l
cm
~=
~=
 
Câu 43. Có một cái cốc úp ngược như hình vẽ. Chiều cao của cốc là 30cm, bán kính đáy cốc là 3cm, bán 
kính miệng cốc là 5cm. Một con kiến đang đứng ở điểm A của miệng cốc dự định sẽ bò ba vòng 
quanh thân cốc để lên đến đáy cốc ở điểm B. Tính quãng đường ngắn nhất để con kiến có thể thực 
hiện được dự định của mình. (làm tròn kết quả đến hàng đơn vị) 
 
 
Lời giải 
Trả lời: 75 
Đặt 1
2
,,
r r h lần lượt là bán kính đáy cốc, miệng cốc và chiều cao của cốc, alpha là góc kí hiệu như trên 
hình vẽ. Ta “trải” ba lần mặt xung quanh cốc lên mặt phẳng sẽ được một hình quạt của một khuyên 
với cung nhỏ 
3
1

6
18
l BB
r
pi
pi
=
=
 và cung lớn 
3
2

6
30
l AA
r
pi
pi
=
=
. 
Con kiến muốn đi từ A tới B phải vòng 3 vòng quanh 
cốc. Đường đi ngắn nhất là đi theo đoạn AB3, Theo định lý Côsin ta có 
2
2
3
3
3
2
.
.cos3
AB
OA
OB
OAOB
 alpha 
=
+
-
 (1) với 
 · 
1
AOA
 alpha =
 
Độ dài 
2
2
2
1

2 226
AB
h
r
r
=
+
-
=
 
3
3

3
3 226

5
l BB
OB
OB
OB
OA
l AA
OB
BA
=
=
=
 => 
=
+
 
5 226
OA
OB
BA
 => 
=
+
=
```

### Nguồn: `Phương pháp trải phẳng giải một số bài toán ứng dụng thực tế – Đặng Việt Đông.pdf` (page_5) — `[VDC Score: 25.5]`
```text
Gv: Đặng Việt Đông Trường THPT Nho Quan A Phương pháp trải phẳng 
 
 
ĐT: 0978064165 - Email: dangvietdong.ninhbinh.vn@gmail.com - ID Tik Tok: dongpay | Trang 5 
Facebook: https://www.facebook.com/dongpay - Kênh Youtube: Thầy Đặng Việt Đông 
a) Tọa độ điểm 

0;8;0
D
. 
b) Tọa độ của giỏ hoa đối với hệ trục là 

1;2;1
M
. 
c) Công tắc đặt tại vị trí nằm chính giữa đoạn thẳng 
'
CC. Đoạn dây nối từ công tắc đến bóng đèn 
được men theo tường, khi đó đoạn dây ngắn nhất nối từ công tắc đến bóng đèn bằng là 15m 
d) Khi bật đèn sáng thì ảnh của giỏ hoa lên mặt đất tại vị trí K, khi đó tọa độ 

4;8;0
K
. (Xem 
bóng đèn và giỏ hoa có kích thước không đáng kể) 
Câu 4. 
Một mô hình có dạng hình hộp chữ nhật 
.
ABCD A B C D
'''' có các cạnh 
3,
4,
5
'
=
=
=
AB
BC
AA
. 
,
,
M N P lần lượt thuộc các cạnh 
,
,
BB CC DD
'
'
'. Tìm giá trị nhỏ nhất của AM
MN
NP
PA'
+
+
+
 là 
bao nhiêu? (làm tròn kết quả đến chữ số thập phân thứ nhất) 
Câu 5. 
Một mô hình có dạng hình lập phương 
. ''''
ABCD A B C D có cạnh bằng 1, M là trung điểm của AB
. Một con kiến đi từ M đến điểm N thuộc cạnh BC, từ điểm N đi thẳng tới điểm P thuộc cạnh 
'
CC, từ điểm P đi thẳng tới điểm 
'
D (điểm N, P thay đổi tùy hướng đi của con kiến). Quãng 
đường ngắn nhất để con kiến đi từ điểm M đến điểm 
'
D là 
 
Câu 6. 
Một cột nhà có dạng hình hộp chữ nhật ABCDEFGH có đáy là hình vuông cạnh 0,5 m và chiều 
cao 2,4 m. Một con kiến bò từ điểm A đến vị trị điểm F theo đường gấp khúc ANMF với 
M
GC
 Z 
 và N
HD
 Z 
 như hình vẽ. Tính quãng đường (mét) ngắn nhất mà con kiến cần bò (làm 
tròn đến hàng phần trăm)? 
 
 Câu 7. 
Một ngôi nhà hình lăng trụ đứng 
.
ABCD A B C D
'''' có đáy ABCD là hình thang vuông tại A và B, 

4
;
3,5
;
6
AB
AD
m
BC
m
BB
m
'
=
=
=
=
 (xem hình vẽ). Ở bức tường ADD A
'' người ta lắp một 
bóng điện cách cạnh A D
'
' một khoảng bằng ()
3 m và cách mặt sàn một khoảng bằng ()
3 m, còn ở 
bức tường BCC B'' người ta lắp một bóng điện cách cạnh B C
'' một khoảng bằng ()
3 m và cách mặt 
sàn một khoảng bằng 

2,5 m. Một bảng điều khiển được đặt tại bức tường A B C D
'''' cách cạnh 
A D
'
' một khoảng bằng ()
1 m và cao 

1,5 m so với mặt sàn. Người ta muốn nối dây điện từ bảng 
điều khiển men theo các bức tường (không mắc lên mái) đến 2 bóng điện trên. Hỏi cần tối thiểu bao 
nhiêu mét dây điện? (làm tròn kết quả đến hàng phần mười).
```

---

# KHU VỰC I: NGỮ LIỆU TRỌNG TÂM VẬN DỤNG CAO & TOÁN THỰC TẾ (DÙNG CHO PHẦN II & PHẦN III)

## Chủ đề VDC: `dang_ham_so_tiem_can_phan_thuc`
### Nguồn: `Vận dụng cao.pdf` (page_52) — `[VDC Score: 20.5]`
```text
CHƯƠNG I. XÁC SUẤT - THỰC TẾ- THỐNG KÊ - RỜI RẠC
Teacher2kkk | Học toán cùng GenZ
Câu 173. Hệthống định vịtoàn cầu GPS là một hệthống cho phép xác định vịtrí của một vật thể
trong không gian. Trong cùng một thời điểm vịtrí của một điểm M trong không gian sẽđược xác
định bởi bốn vệtinh cho trước nhờcác bộthu phát tín hiệu đặt trên các vệtinh. Giảsửtrong không
gian với hệtoạđộOxyz, có bốn vệtinh lần lượt đặt tại các điểm A(2;4;0), B (0;4;6), C (2;0;6),
D(-1;-2;-3) và vịtrí điểm M (a;b;c) thoảMA + MB + MC + MD nhỏnhất. Tính độdài MO.
(làm tròn kết quảđến hàng phần chục)
Câu 174. Một máy bay trình diễn có đường bay gắn với hệtrục Oxy được mô phỏng như hình vẽ.
Trục Ox gắn với mặt đất, đường bay có dạng là một phần của đồthịhàm phân thức bậc hai trên
bậc nhất f(x) có đường tiệm cận đứng x = 2. Điểm G là giao điểm của đường tiệm cận xiên của đồ
thịhàm f(x) và trục Ox được gọi là điểm giới hạn. Biết rằng máy bay xuất phát tại vịtrí A cách
gốc toạđộO một khoảng 2,5 đơn vịvà máy bay khi ởvịtrí cao nhất cách điểm xuất phát 1,5 đơn
vịtheo phương song song với trục Ox và cách mặt đất 4,5 đơn vị. Vịtrí máy bay tiếp đất cách điểm
giới hạn một khoảng bằng bao nhiêu?
Câu 175. Trong hệtrục toạđộOxy, cho đồthịhàm sốf(x) = x2 +x+1
x+1
(C) mô tảchuyển động
của hai tàu đánh cá A và B (đơn vịtrên mỗi trục toạđộtính bằng km). Biết quỹđạo chuyển động
của hai tàu luôn thuộc hai nhánh khác nhau của đồthị(C). Tính khoảng cách ngắn nhất (km) giữa
hai tàu đánh cá A và B (kết quảlàm tròn đến hàng phần trăm).
Câu 176. Chọn ngẫu nhiên bốn sốtựnhiên khác nhau từ70 sốnguyên dương đầu tiên. Xác suất
đểbốn sốđược chọn lập thành một cấp sốnhân có công bội nguyên là a
b (trong đó a, b là các sốtự
nhiên và nguyên tốcùng nhau). Khi đó hãy làm tròn đến hàng đơn vịsố105a
b
.
BIÊN SOẠN: TRƯƠNG CÔNG ĐẠT
Tuyển tập VD - VDC trong các đềthi thửTHPTQG | 50
H
Ọ
C
T
O
Á
N
C
Ù
N
G
G
E
N
Z
+
-
×
÷
N
N∗
Z
Q
I
R
C
R
P̸
=
log
ln
∈
/∈
∀
∄
∃
∅
∨
∧
⊄
⊂
≡
≠
=
>
<
≥
≤
√
lim
sin
cos
tan
cot
⊥
∥
Ak
n
Ck
n
α
β
γ
δ
λ
π
ϕ
φ
ex
arcsin
arccos
arctan
±∞
∪
∩
y = f(x)
⇔
⇒
≈
|
µ
ω
τ
i2 = -1
P (A|B)
0
1
2
3
4
5
6
7
8
9
a2 +b2 = c2
Pn = n!
T2
K
EACHER
```

### Nguồn: `Vận dụng cao.pdf` (page_573) — `[VDC Score: 16.0]`
```text
CHƯƠNG III. HÀM SỐ
Teacher2kkk | Học toán cùng GenZ
Câu 1327. Cho hàm sốf(x) = x3 -3x2 +3 có đồthịlà đường cong (C). Xét tất cảcác hàm sốbậc
hai có đồthịlà parabol với đỉnh I (-1;-1) và cắt (C) tại ba điểm phân biệt sao cho có ít nhất một
điểm với hoành độthuộc đoạn [1;3]. Giá trịlớn nhất của tổng tung độba điểm đó thuộc khoảng nào
dưới đây?
A
9
4; 11
4

.
B

-13
4;-11
4

.
C

-41
4;-39
4

.
D
35
4; 37
4

.
Câu 1328. Cho hàm sốy = x-1
x+2 có đồthị(C). Gọi I là giao điểm hai tiệm cận của (C)
A Hàm sốđồng biến trên R\{-2}.
B Hàm sốcó tâm đối xứng I (-2;1).
C Phương trình tiếp tuyến của đồthị(C) tại điểm x = 1 là y = x-1
3
.
D Xét tam giác đều ABI có hai đỉnh A, B thuộc (C), đoạn thẳng AB có độdài bằng 2
√
3.
Câu 1329. Cho hàm sốf(x) =

a-1
a -x

4-3x2
(a > 0). Gọi M, m lần lượt là giá trịcực đại
và giá trịcực tiểu của hàm số. Giá trịnhỏnhất của M -m bằng bao nhiêu? (làm tròn kết quảđến
hàng phần trăm)
Câu 1330. Có bao nhiêu giá trịnguyên m đểhàm sốy = mx4 + (m+3)x3 -

m2 +1

x + 2025m
đồng biến trên (1;+∞)?
A 9.
B 10.
C 11.
D 8.
Câu 1331. Cho hàm sốf(x) có f(1) = 3 và f'(1) = 2. Giá trịcủa lim
x→1
f2 (x)-9
x-1
bằng
A 12.
B 6.
C 2.
D 18.
Câu 1332. Xét các cấp sốcộng (an) có sốhạng đầu tiên a1 và công sai d đều là các sốnguyên
dương và thỏa mãn 2a8 = 227a8. Tìm giá trịnhỏnhất của a3.
Câu 1333. Cho hàm sốf(x) = x2 -3x+6
x-1
A Toạđộđiểm cực tiểu của đồthịhàm sốlà (a;b). Khi đó, a2 +b = 12.
B Tiệm cận xiên của đồthịhàm sốlà y = x-2.
C Gọi I là giao điểm hai đường tiệm cận của đồthịhàm số. Tiếp tuyến của đồthịhàm sốtại
điểm có hoành độx = 2 cắt hai đường tiệm cận tại A, B. Diện tích tam giác IAB bằng 12.
D Có tất cả9 giá trịnguyên m đểphương trình f(x) = m có hai điểm phân biệt x1, x2 thoảmãn
x1 < 2 < x2 < 15.
BIÊN SOẠN: TRƯƠNG CÔNG ĐẠT
Tuyển tập VD - VDC trong các đềthi thửTHPTQG | 1335
H
Ọ
C
T
O
Á
N
C
Ù
N
G
G
E
N
Z
+
-
×
÷
N
N∗
Z
Q
I
R
C
R
P̸
=
log
ln
∈
/∈
∀
∄
∃
∅
∨
∧
⊄
⊂
≡
≠
=
>
<
≥
≤
√
lim
sin
cos
tan
cot
⊥
∥
Ak
n
Ck
n
α
β
γ
δ
λ
π
ϕ
φ
ex
arcsin
arccos
arctan
±∞
∪
∩
y = f(x)
⇔
⇒
≈
|
µ
ω
τ
i2 = -1
P (A|B)
0
1
2
3
4
5
6
7
8
9
a2 +b2 = c2
Pn = n!
T2
K
EACHER
```

### Nguồn: `Chuyên đề ôn thi tốt nghiệp THPT năm 2026 môn Toán – Nguyễn Tiến Hà.pdf` (page_233) — `[VDC Score: 12.0]`
```text
CHUYÊN ĐỀ ÔN THI TN.THPT MÔN TOÁN 12 NĂM 2026-2027 
CHỦ ĐỀ 13 
 
 
ThS. Nguyễn Tiến Hà – Zalo: 0949.888.993 
 Trang 230 
NGUYỄN TIẾN HÀ
NGUYỄN TIẾN HÀ
Câu 86: Cho hàm số 

2
5
7
x
y
f x
x
x
e
=
=
-
+
. Xét tính đúng sai các khẳng định sau: 
a) ()
0
7
f
=
. 
b) Hàm số 

y
f x
=
 nghịch biến trên khoảng 
5
; 2

- vô cùng 

 và đồng biến trên khoảng 5;
2

+ vô cùng 

 
c) Giá trị nhỏ nhất và lớn nhất của hàm số 

y
f x
=
 trên đoạn [0;2]

 lần lượt là 7 và 3e. 
d) Đạo hàm của hàm số đã cho là 

2
5
x
f
x
x
e
'
=
-
. 
 
Câu 87: Cho hàm số ()
2
2
4
10
f x
x
x
x
=
-
+
-
. Xét tính đúng sai các khẳng định sau: 
a) Đạo hàm của hàm số là 

2
1
1
2
4
10
x
f
x
x
x
-
'
=
-
-
+
. 
b) Phương trình 

0
f
x
'
=
 có hai nghiệm là 
3
x =
; 
1
x =-. 
c) 

lim
x
f x
 -> + vô cùng 
=+ vô cùng và 

lim
x
f x
 -> - vô cùng 
=+ vô cùng. 
d) Giá trị nhỏ nhất của hàm số là 1. 
 
Câu 88: Cho hàm số 
2
ax
bx
c
y
mx
n
+
+
=
+
 có đồ thị như hình vẽ sau: 
 
Xét tính đúng sai các khẳng định sau: 
a) Hàm số đã cho nghịch biến trên khoảng (2;0)
-
. 
b) Đồ thị của hàm số đã cho có tiệm cận xiên 
1
y
x
=
+
. 
c) Gọi 
,  
A B là hai điểm cực trị của đồ thị hàm số đã cho, diện tích của tam giác OAB 
bằng 8. 
d) Một trục đối xứng của đồ thị đã cho là 

3
:
1 tan 8
d
y
x
pi
=
+
. 
 
Câu 89: Cho hàm số ()
2
2
1
x
f x
e
x
-
=
+
-. Xét tính đúng sai các khẳng định sau: 
a) ()
4
2
3
f
e-
=
+
, 
2
1
3
f
e
-
=
-
. 
b) 

2
2
x
f
x
e-
'
=-
+
. 
c) ()
0
f x =
 có đúng một nghiệm trên đoạn 
[1;2]
[-]
. 
d) Giá trị lớn nhất của hàm số ()
f x trên đoạn 
[1;2]
[-]
 bằng 
4
3
e
+
.
```

## Chủ đề VDC: `dang_ham_so_toi_uu_thuc_te`
### Nguồn: `Chuyên đề ôn thi tốt nghiệp THPT năm 2026 môn Toán – Nguyễn Tiến Hà.pdf` (page_399) — `[VDC Score: 21.5]`
```text
CHUYÊN ĐỀ ÔN THI TN.THPT MÔN TOÁN 12 NĂM 2026-2027 
CHỦ ĐỀ 18 
 
 
ThS. Nguyễn Tiến Hà – Zalo: 0949.888.993 
 Trang 396 
NGUYỄN TIẾN HÀ
NGUYỄN TIẾN HÀ
Câu 70: Một doanh nghiệp dự định sản xuất không quá 300 sản phầm. Nếu doanh nghiệp sản xuất x sản 
phẩm 
1
300
x
<=
<=
 thì doanh thu nhận được khi bán hết số sản phẩm đó là 

2
2
1312
F x
x
x
=-
+
, trong khi chi phí sản xuất bình quân cho một sản phẩm là 

2
40000
77
1000
G x
x
x
x
=
-
+
+
. Lợi nhuận thu được của doanh nghiệp đạt giá trị lớn nhất 
bằng bao nhiêu? 
 
Câu 71: Một doanh nghiệp dự định sản xuất không quá 400 sản phẩm. Nếu doanh nghiệp sản xuất x sản 
phẩm 
(1
400)
x
<=
<=
thì 
doanh 
thu 
nhận 
được 
khi 
bán 
hết 
số 
sản 
phẩm 
là 

3
2
1999
1001000
250000
F x
x
x
x
=
-
+
+
.Trong đó, chi phí vận hành máy móc cho mỗi sản 
phẩm 
là 
100000

3
1
2
x
G x
x
=
+
 
đồng. 
Tổng 
chi 
phí 
mua 
nguyên 
vật 
liệu 
là 
3

2
100000
50000
H x
x
x
=
+
-
 nhưng do doanh nghiệp mua với số lượng lớn nên được giảm 1% 
cho 200 sản phẩm đầu tiên doanh nghiệp sản xuất và giảm 2% cho sản phẩm tiếp theo. Doanh 
nghiệp cần sản xuất bao nhiêu sản phẩm để lợi nhuận thu được là lớn nhất?
 
 
Câu 72: Một trang trại rau sạch ở Đà Lạt mỗi ngày thu hoạch được 1 tấn rau. Mỗi ngày, nếu giá bán rau là 
30000 đồng/kg thì bán hết rau, nếu giá bán rau tăng 1000 đồng/kg thì số rau thừa tăng 20 kg. Số 
rau thừa này được thu mua hết để làm thức ăn chăn nuôi với giá 2000 đồng/kg. Hỏi để mỗi ngày 
thu được số tiền bán rau lớn nhất thì trang trại đó nên bán rau với giá bao nhiêu nghìn đồng? 
 
Câu 73: Chi phí xuất bản x cuốn tạp chí được cho bởi ()
2
8
2000
10
C x
x
x
=
-
+
 đồng. Chi phí phát hành 
cho mỗi cuốn là 4 nghìn đồng và 

T x
M x
x
=
 với ()
T x là tổng chi phí cho x cuốn tạp chí, 
được gọi là chi phí trung bình cho một cuốn tạp chí khi xuất bản x cuốn. Khi số lượng cuốn tạp 
chí phát hành cực lớn thì chi phí trung bình cho mỗi cuốn tạp chí 

M x sẽ tiệm cận với đường 
thẳng có phương trình dạng y
ax
b
=
+
. Tính 
68
3
800
P
a
b
=
+
+
. 
 
Câu 74: Một công ty chuyên sản xuất dụng cụ thể thao nhận được đơn đặt hàng sản xuất 9000 quả bóng 
rổ. Công ty có một số máy móc, mỗi máy có khả năng sản xuất 36 quả bóng rổ trong một giờ. 
```

### Nguồn: `Toán thực tế.pdf` (page_11) — `[VDC Score: 25.0]`
```text
Chuyên đềtoán thực tế
Nhóm Ba Đưòng Đồng Quy – 0889 971 004
10
TOÁN 12
TOÁN 12
TOÁN 12
Câu 2
(CT - THPTQG 2025). Nếu một doanh nghiệp sản xuất x sản phẩm trong
một tháng (x ∈N∗; 1 ⩽x ⩽4500) thì doanh thu nhận được khi bán hết sốsản phẩm đó
là F (x) = -0, 01x2 + 450x (nghìn đồng), trong khi chi phí sản xuất bình quân cho mỗi
sản phẩm là G (x) = 30000
x
+340 (nghìn đồng). Giảsửsốsản phẩm sản xuất ra luôn được
bán hết. Trong một tháng, doanh nghiệp đó cần sản xuất ít nhất bao nhiêu sản phẩm để
lợi nhuận thu được lớn hơn 100 triệu đồng?
KQ:
Câu 3
(CT - THPTQG 2026). Một công ty nông sản có công suất chếbiến không quá
180 tấn nguyên liệu một tháng. Nếu công ty chếbiến x tấn nguyên liệu trong một tháng
(1 ≤x ≤180) thì chi phí sản xuất và doanh thu lần lượt là C(x) = 0, 002x3 + 30x + 20
(triệu đồng) và R(x) = 90x (triệu đồng). Lợi nhuận lớn nhất mà công ty đạt được trong
một tháng là bao nhiêu triệu đồng?
KQ:
Câu 4
Một gia đình đan lưới đánh cá, mỗi ngày đan được x mét lưới
(1 ≤x ≤18). Tổng chi phí sản xuất x mét lưới, tính bằng nghìn đồng, cho bởi hàm chi phí
C(x) = x3 -3x2 -20x + 500. Giảsửgia đình làm nghềđan lưới bán hết sản phẩm mỗi
ngày với giá 220 nghìn đồng/mét. Gọi L(x) là lợi nhuận thu được khi bán x mét lưới. Hỏi
lợi nhuận tối đa của gia đình đan lưới trong một ngày (đơn vịtính nghìn đồng)?
KQ:
Câu 5
Nếu một doanh nghiệp sản xuất x sản phẩm trong một tháng
(x ∈N; 1 ≤x ≤300) thì doanh thu nhận được khi bán hết sốsản phẩm là
F(x) = x3 -1 999x2 + 1 001 000x + 250 000 (đồng). Trong đó, chi phí vận hành máy móc
bình quân cho mỗi sản phẩm khi sản xuất x sản phẩm là G(x) = 300 + 100
x
(nghìn đồng),
chi phí mua nguyên vật liệu đểsản xuất x sản phẩm là H(x) = 2x3 + 100 000x -50 000
(đồng). Doanh nghiệp cần sản xuất bao nhiêu sản phẩm đểlợi nhuận thu được là lớn
nhất?
KQ:
Câu 6
Một doanh nghiệp dựđịnh sản xuất không quá 180 sản phẩm. Nếu doanh
nghiệp sản xuất x sản phẩm (1 ≤x ≤180) thì giá bán của mỗi sản phẩm là
f(x) = 35840 -192x (nghìn đồng) và chi phí sản xuất bình quân trên một sản phẩm là
g(x) = 25,6x2-153,6x+3072+ 19200
x
(nghìn đồng). Biết rằng mức thuếtrên một sản phẩm
là 512 nghìn đồng. Hỏi doanh nghiệp cần sản xuất bao nhiêu sản phẩm đểlợi nhuận thu
được là
```

### Nguồn: `Tổng ôn.pdf` (page_218) — `[VDC Score: 20.5]`
```text
» Trang 218 
» Câu 5. Nhà máy A chuyên sản xuất một loại sản phẩm cho nhà máy B. Hai nhà máy thỏa thuận 
rằng, hằng tháng A cung cấp cho B số lượng sản phẩm theo đơn đặt hàng của B (tối đa 
100 tấn sản phẩm). Nếu số lượng đặt hàng là x tấn sản phẩm thì giá bán cho mỗi tấn 
sản phẩm là 

2
45
0 001
=
-,
P x
x (triệu đồng). Chi phí để A sản xuất x tấn sản phẩm 
trong một tháng là ()
100
30
=
+
C x
x triệu đồng (gồm 100 triệu đồng chi phí cố định và 
30 triệu đồng cho mỗi tấn sản phẩm). Khi đó: 
 
Mệnh đề 
Đúng 
Sai 
(a) Chi phí để A sản xuất 10 tấn sản phẩm trong một tháng là 500 triệu 
đồng. 
 
 
(b) Số tiền A thu được khi bán 10 tấn sản phẩm cho B là 449 triệu đồng. 
 
 
(c) 
Hàm số biểu thị lợi nhuận mà A thu được khi bán x tấn sản phẩm (
0
100
<=
<=
x
) cho B là 

3
0 001
15
100
=-
+
+
,
H x
x
x
. 
 
 
(d) Nhà máy A bán cho B khoảng 72 tấn sản phẩm mỗi tháng thì thu 
được lợi nhuận lớn nhất. (làm tròn kết quả đến hàng đơn vị) 
 
 
 Lời giải 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................
```

## Chủ đề VDC: `dang_mu_logarit_thuc_te`
### Nguồn: `Tổng ôn.pdf` (page_414) — `[VDC Score: 18.5]`
```text
» Trang 7 
để tiết kiệm mua ô tô. Hỏi sau ít nhất bao nhiêu năm thì anh A mua được ô tô giá 500 
triệu biết rằng anh A được gia đình hỗ trợ 32% giá trị chiếc xe? 
} Trả lời: 
1 
3 
 
 
» Câu 51. Một người gửi 60 triệu đồng vào ngân hàng với lãi suất 0 5
, % / tháng. Biết rằng nếu 
không rút tiền ra khỏi ngân hàng thì cứ sau mỗi tháng, số tiền lãi sẽ được nhập vào vốn 
ban đầu (hay gọi là lãi kép). Giả sử trong nhiều tháng liên tiếp kể từ khi gửi tiền, người 
đó không rút tiền ra và lãi suất không thay đổi. Hỏi từ tháng thứ mấy trờ đi, người đó 
có hơn 66 triệu đồng? 
} Trả lời: 
2 
0 
 
 
» Câu 52. Theo báo cáo của Chính phủ, dân số của nước ta tính đến tháng 12 năm 2018 là 95,93 
triệu người, nếu tỉ lệ tăng trưởng dân số trung bình hằng năm là 1 33
,
% thì dân số nước 
ta vào tháng 12 năm 2025 là bao nhiêu? (Tính theo đơn vị triệu người, làm tròn đến hàng 
đơn vị) 
} Trả lời: 
1 
0 
5 
 
» Câu 53. Trung bình sau mỗi năm sử dưng, giá trị còn lại của một chiếc ô tô giảm đi 
 so với 
năm trước đó. Giả sử một chiếc ô tô lúc mới mua là 800 triệu đồng. Hỏi sau ít nhất bao 
nhiêu năm sử dụng thì giá trị còn lại của chiếc ô tô đó nhỏ hơn 600 triệu đồng (làm tròn 
kết quả đến hàng đơn vị)? 
} Trả lời: 
5 
 
 
 
» Câu 54. Trong điều kiện nuôi cấy thích hợp, cứ 20 phút vi khuẩn E.Coli lại phân đôi một lần. 
Giả sử lúc đầu có 5 vi khuẩn và sau n phút (Z 
n
) có hơn 2.000 vi khuẩn. Giá trị nhỏ 
nhất của n là bao nhiêu? (làm tròn kết quả đến hàng đơn vị). 
} Trả lời: 
1 
7 
3 
 
» Câu 55. Dân số thế giới năm 2020 là khoảng 7 79
,
 tỉ người và tăng với tốc độ khoảng 1 05
,
%mỗi 
năm (theo danso.org). Giả sử tốc độ tăng này không đổi. Khi đó mô hình 

2020
7 79 1 0105
-
=
 × 
,
,
t
P t
 có thể dùng để ước tính dân số thế giới (theo đơn vị tỉ người) 
vào năm t. Theo mô hình này, vào năm nào dân số thế giới đạt 10 tỉ người? 
} Trả lời: 
2 
0 
4 
4 
» Câu 56. Một người gửi tiết kiệm một khoản tiền cố định theo thể thức lãi kép, kì hạn 1 tháng 
với lãi suất 6%/năm. Giả sử, trong nhiều tháng lãi suất không đổi và người đó không 
rút tiền ra. Sau ít nhất bao nhiêu tháng gửi tiết kiệm số tiền người đó rút được cả gốc 
và lãi vượt quá 1,1 lần số t
```

### Nguồn: `Tổng ôn.pdf` (page_102) — `[VDC Score: 14.0]`
```text
» Trang 102 
tính bằng giờ kể từ khi người đó tử vong và T là nhiệt độ cơ thể 
°F tại thời điểm 
đó.Tính vào lúc 11 giờ sáng, người đó đã tử vong bao nhiêu giờ (Làm tròn kết quả đến 
hàng phần trăm). 
 Lời giải 
} Trả lời: 
 
 
 
 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
» Câu 17. Sự tăng trưởng dân số dự kiến của một quốc gia từ năm 2025 có thể được mô hình hoá 
qua phương trình 
0 0052
307 5
=
,
, e
t
P
, trong đó P là dân số (tính bằng triệu) và t là thời 
gian (tính bằng năm), với 
25
=
t
 tương ứng với năm 2025. Theo mô hình tăng trưởng 
trên hãy xác định năm đầu tiên mà dân số của quốc gia đó vượt quá 430 triệu người? 
(Nguồn: Cục điều tra dân số Hoa Kỳ) 
 Lời giải 
} Trả lời: 
 
 
 
 
..................................................................................................................................................... 
..................................................................................................................................................... 
..........................
```

### Nguồn: `Liên trường THPT – Nghệ An.pdf` (page_4_ocr) — `[VDC Score: 19.0]`
```text
a) Giá trịcủa b bằng 12,5.
b) Thời gian ô tô đạt vận tốc tối đa cho phép là 5s.
e) Khoảng cách giữa ô tô và đuôi tàu sau 3s là 51,25m.
đ) Thời gian 6 tô bat kịp đuôi tàu ké từlúc ô tô bắt đầu tăng tốc là 15,75s.
PHAN III. Câu trắc nghiệm tra lời ngắn. Thi sinh trảlời từcâu 1 đến câu 6.
Câu 1. Trong một nhà máy cơ khí chếtạo,có một chỉtiết máy hình đĩa tròn có dạng như hình vẽ, nhận AB và
CD làm các trục đôi xứng. Dé tăng độbên cho chi tiét máy này người ta cân phủsơn cảhai mặt của chi tiét
máy.
Biệt
răng đường
tròn
lớn
có bán
kính
5dm,
các đường
tròn
nhỏđêu
có bán
kính
bang
2dm, AB = CD = 4dm và chi phí sơn là 82.000 đồng/m?. Chi phí đểsơn hoàn thiện chỉtiết máy đó là a (don
vịnghìn đồng) khi đó a bằng bao nhiêu (kết quảlàm tròn đến hàng đơn vị)?
N
i”
A. - -l~ "¬ J
J
| Cc
|
Câu 2. Cho hình lăng trụABC.A'B'C’', đáy là tam giác đều cạnh bằng 12, A'A= A'B=A'C và góc tạo
bởi cạnh bên và mặt phẳng đáy bằng 60°. Tính khoảng cách từtrung điểm Mctia CC' đến mặt phẳng
(A' BC) (kêt quảlàm tròn đên hang phân trăm).
Câu 3. Đểchuẩn bịcho đội tình nguyện hỗtrợy tếtại một vùng sâu vùng xa, một bệnh viên đa khoa đã chọn
ra 10 bác sỹgiỏi gồm 6 bác sỹnam trong đó có bác sỹAn và 4 bác sỹnữtrong đó có bác sỹBình. Đội tình
nguyện gồm 5 bác sỹvới yêu cầu như sau: có cảnam và nữ, sốbác sỹnữkhông ít hơn 2 người. Do yêu cầu về
chuyên môn bổtrợcho nhau nên nếu bác sỹAn tham gia thì bác sỹBình cũng phải tham gia, nhưng nếu bác sỹ
Bình tham gia thì bác sỹAn không nhất thiết phải tham gia. Hỏi có bao nhiêu cách thành lập đội tình nguyện
như trên?
Câu 4. Ong An vay ngân hàng 500 triệu đồng với lãi suất ngân hàng r = 0,6% trên tháng theo hình thức lãi
kép dé kinh doanh. Cuối tháng thứnhất sau khi vay, ông An bắt đầu hoàn nợbằng cách trảmột sốtiền cốđịnh
10 triệu đồng vào cuối mỗi tháng. Hỏi sau bao nhiêu tháng thì ông An trảhết nợ?
Câu 5. Một công ty muốn làm một đường ống dẫn từmột điểm A trên bờđến một điểm Œ trên một hòn đảo.
Hòn đảo cách bờbiên 6 km. Dé thực hiện, công ty dựđịnh xây dựng phân đường ông trên bờtừA đên B và
đường ông dưới nước từ đên Œ (hình vẽ).
C
ị6km
Ạ
To H
B——— 9km |
```

## Chủ đề VDC: `dang_tich_phan_dien_tich_the_tich`
### Nguồn: `Tổng ôn.pdf` (page_325) — `[VDC Score: 14.0]`
```text
» Trang 325 
Thể tích của khối chân đế bằng bao nhiêu centimét khối (không làm tròn kết quả các phép 
tính trung gian, chỉ làm tròn kết quả cuối cùng đến hàng phần mười)? 
 Lời giải 
} Trả lời: 
 
 
 
 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
» Câu 20. Một chậu nước hình bán cầu bằng nhôm có bán kính 
10
=
R
 (cm), đặt trong một khung 
hình hộp chữ nhật (hình 1). Trong chậu có chứa sẵn một khối nước hình chỏm cầu có 
chiều c
```

### Nguồn: `Tổng ôn.pdf` (page_543) — `[VDC Score: 19.0]`
```text
» Trang 136 
 
Khi đó: 
 
Mệnh đề 
Đúng 
Sai 
(a) Hình 1 khối 
H là một khối tròn xoay. 
 
X 
(b) Công thức tỉnh thể tích khối 
H là 

3
2
3
-
= tích phân 
d
V
S
x
x. 
 
X 
(c) Diện tích ()
S x được xác định bởi công thức ()

2
2 9
=
-
S x
x
. 
 
X 
(d) Thể tích của khối 
H bằng 144 (đơn vị thể tích). 
X 
 
» Câu 5. Bình chứa nhiên liệu của một chiếc máy bay phản lực được mô tả trong không gian là 
một khối tròn xoay thu được khi quay hình phẳng giới hạn bởi đồ thị hàm số 
2
1
2
8
=
-
y
x
x với 0
2
<=
<=

x
 và trục Ox quanh trục Ox (x tính theo đơn vị m). Thể 
tích của bình chứa bằng a
b
 m³ với a
b
 là phân số tối giản, 
 Z 
*
,a b
. Khi đó +
a
b bằng 
bao nhiêu? 
 
} Trả lời: 
3 
1 
 
 
» Câu 6. Một quả bóng bầu dục theo quy định được sử dụng trong giải bầu dục quốc gia có kích 
thước 28cm từ đầu này đến đầu kia và đường kính 17cm ở phần dày nhất (quy định 
cho phép thay đổi một chút về các kích thước này) (Nguồn: NFL). Hình dạng của một 
quả bóng bầu dục có kích thước nói trên có thể được tạo thành khi quay phần diện tích 
hình phẳng giới hạn bởi đồ thị hàm số 

2
=
+
+
f x
ax
bx
c, trục hoành và các đường 
thẳng 
4
24
=-
=
;
x
x
, trong đó x tính bằng centimet (cm). Thể tích (đơn vị: cm³, kết quả 
làm tròn đến hàng đơn vị) của quả bóng bầu dục có kích thước nói trên bằng bao nhiêu? 
 
} Trả lời: 
3 
3 
9 
0 
» Câu 7. Một nhà máy sản xuất một mẫu đồ chơi có dạng một chiếc mũ trùm lên một khối trụ. 
Cách thiết kế mẫu vật như sau: Lấy chân đế là một khối trụ có chiều cao 4 cm và bán 
kính bằng 10 cm. Phần có dạng chiếc mũ nói trên có bán kính đáy bằng bán kính hình
```

### Nguồn: `Ôn tập.pdf` (page_163) — `[VDC Score: 16.5]`
```text
Trang. 161 
MỘT SỐĐỀÔN THI TNTHPT
Câu 8. 
Tìm tập xác định của hàm số 

1
2
log
2
1
y
x
=
-
. 
A. 

1;
D =
+ vô cùng. 
B. 
1; 1
2
D
(
]
=(
]
(
]
. 
C. 
[
)
1;
D =
+ vô cùng. 
D. 
1; 1
2
D

=

. 
Câu 9. 
Trong không gian Oxyz, tính khoảng cách từ điểm 

1; 2;
3
M
-
 đến mặt phẳng 
():
2
2
2
0
P
x
y
z
+
-
-
=
. 
A. 11
3. 
B. 1
3. 
C. 3. 
D. 1. 
Câu 10. 
Tính diện tích hình phẳng giới hạn bởi các đồ thị 
2
2
y
x
x
=
-
 và 
2
y
x
x
=-
+
? 
A. 9
8. 
B. 6. 
C. 12. 
D. 10
3. 
Câu 11. 
Khi điều tra chi phí hàng tháng (đơn vị: triệu đồng) của 25 người còn độc thân ở độ tuổi 30 đến 
tuổi 35, người ta thu được mẫu số liệu sau: 
Chi phí 
[
)
5; 7
[
)
7; 9
[
)
9; 11
[
)
11; 13
[
)
13; 15
Số người 
5 
5 
7 
5 
3 
Tìm phương sai của mẫu số liệu ghép nhóm trên (làm tròn đến hàng phần trăm). 
A. 6,62. 
B. 6,13. 
C. 5,54. 
D. 5,82. 
Câu 12. 
Cho 

F x là một nguyên hàm của hàm số 

2
x
f
x
e
x
=
+
 thỏa mãn 

3
0
.
2
F
=
 Tìm 

F x. 
A. 

2
3.
2
x
F x
e
x
=
+
+
 
 
B. 

2
1
2
.
2
x
F x
e
x
=
+
-
 
C. 

2
5.
2
x
F x
e
x
=
+
+
 
 
D. 

2
1.
2
x
F x
e
x
=
+
+
 
PHẦN II. CÂU TRẮC NGHIỆM ĐÚNG SAI 
Câu 1. 
Một đại lý xăng dầu cần làm một cái bồn chứa dầu hình trụ 
bằng tôn có thể tích 16pi mét khối. Người ta muốn hình trụ được làm ra ít 
tốn nguyên vật liệu nhất có thể. 
Gọi,r h, V và S lần lượt là bán kính đáy, chiều cao, thể tích và diện 
tích toàn phần của cái bồn dầu hình trụ. 
Xét tính đúng sai các mệnh đề sau: 
Đúng
Sai 
a) Công thức để tìm thể tích bồn chứa dầu là 
2
V
r h
pi
=
[.] 

b) Diện tích toàn phần của bồn chứa dầu là 
2
8
2
S
r
r
pi
=
+

[.] 

c) 
5
0
2
S
r
'=
 <=> 
=
[.] 

d) Bồn chứa dầu hình trụ có diện tích bé nhất là 
2
73,4 m (làm tròn đến hàng phần 
chục)[.] 

Câu 2. 
Trong không gian Oxyz với đơn vị trên mỗi trục tọa độ là mét, mắt 
một người quan sát đặt ở vị trí 

2; 3;
4
M
-
 và vật cần quan sát đặt tại vị trí 

1; 0; 8
N -
. Một tấm bìa chắn đường truyền ánh sáng có dạng hình tròn tâm 

1; 2; 0
T
, bán kính bằng 3 và đặt trong mặt phẳng (Oxy).
```

## Chủ đề VDC: `dang_tich_phan_dong_hoc`
### Nguồn: `Toán thực tế.pdf` (page_133) — `[VDC Score: 13.5]`
```text
Chuyên đềtoán thực tế
Nhóm Ba Đưòng Đồng Quy – 0889 971 004
132
TOÁN 12
TOÁN 12
TOÁN 12
c
Năng lượng điện lưu trữđược kểtừthời điểm t = 1 đến thời điểm t = 5 nhỏhơn
15, 3 kWh.
d
Năng lượng điện lưu trữđược kểtừthời điểm t = 1 đến thời điểm t = 9 gấp hai
lần năng lượng điện lưu trữđược kểtừthời điểm t = 1 đến thời điểm t = 5.
Câu 2
Giảsửlợi nhuận biên (tính bằng triệu đồng) của một sản phẩm được mô hình
hóa bằng công thức P '(x) = -0,0008x + 10,4. Ởđây P(x) là lợi nhuận (tính bằng triệu
đồng) khi bán được x đơn vịsản phẩm.
a
Lợi nhuận khi bán được 50 sản phẩm đầu tiên là 519 triệu đồng.
b
Biết sựthay đổi của lợi nhuận khi doanh sốtăng từ50 lên a đơn vịsản phẩm lớn
hơn 517 triệu đồng, khi đó giá trịnhỏnhất của a là 101.
c
Lợi nhuận khi bán được x đơn vịsản phẩm được tính bằng công thức P(x) =
-0,0008x + 10,4x.
d
Sựthay đổi của lợi nhuận khi doanh sốtăng từ50 lên 55 đơn vịsản phẩm là 51,79
triệu đồng.
Câu 3
Những ngày giáp Tết Nguyên Đán cũng là dịp bước vào vụĐông Xuân, bà con
nông dân tích cực xuống đồng cấy lúa. Qua nghiên cứu một giống lúa mới, các nhà khoa
học nhận thấy một cây lúa tính từlúc được cấy bằng một cây mạvới chiều cao 20 cm có
tốc độtăng trưởng chiều cao cho bởi hàm sốv(t) = -0,1t3 + 1,1t2, trong đó t tính theo
tuần, v(t) tính bằng cm/tuần. Gọi h(t) là chiều cao của cây lúa ởtuần thứt (t ≥0).
a
h(t) = -1
40t4 + 11
30t3 + 20.
b
Giai đoạn tăng trưởng chiều cao của cây lúa kéo dài 12 tuần.
c
Vào thời điểm cây lúa phát triển nhanh nhất, chiều cao của cây đã lớn hơn 80 cm.
d
Chiều cao tối đa của cây lúa là 150 cm.
Câu 4
Mực nước trong hồchứa của nhà máy điện thủy triều thay đổi trong suốt một
ngày do nước chảy ra (khi thủy triều xuống) và nước chảy vào (khi thủy triều lên). Tốc độ
thay đổi của mực nước trong hồchứa được cho bởi hàm sốh'(t) =
1
216 (5t2 -120t + 480)
(mét/giờ), trong đó h(t) (mét) là mực nước trong hồchứa tại thời điểm t giờ(0 ≤t ≤24).
Tại thời điểm t = 0 giờ, mực nước trong hồchứa là 6 mét.
(Nguồn: A.Bigalk et al, Mathematik, Grundkrurs ma-1, Cornelsen 2016).
a
Giá trịcủa hàm sốh(t) bằng 6 tại t = 0.
b
h(t) =
5
648t3 -5
18t2 + 20
9 t + C (0 ≤t ≤24) với C là một hằng sốxác định.
c
Tại thời điểm t = 18 giờ, mực nước trong hồchứa là 1 mét.

```

### Nguồn: `Chuyên đề ôn thi tốt nghiệp THPT năm 2026 môn Toán – Nguyễn Tiến Hà.pdf` (page_258) — `[VDC Score: 21.0]`
```text
CHUYÊN ĐỀ ÔN THI TN.THPT MÔN TOÁN 12 NĂM 2026-2027 
CHỦ ĐỀ 14 
 
 
ThS. Nguyễn Tiến Hà – Zalo: 0949.888.993 
 Trang 255 
NGUYỄN TIẾN HÀ
NGUYỄN TIẾN HÀ
 
a)Vận tốc của đoàn tàu là 

3
2
4.10
/
v
t
m
s
-
=
. 
b) Sau 90 giây, đoàn tàu chuyển động với vận tốc 

58,32
/
km
h. 
c) Sau khi chuyển động đều một thời gian, đoàn tàu gặp một cây cầu có chiều dài 

486 m
. Khi đó đoàn tàu đi qua cây cầu đó trong thời gian 30 giây. 
d) Chiều dài của đoàn tàu là 

144
l
m
=
. 
Câu 43. Một xe ô tô đang chạy với tốc độ 72 km/h thì người lái xe bất ngờ phát hiện chướng ngại 
vật trên đường cách đó 50 mét. Người lái xe phản ứng một giây, sau đó đạp phanh khẩn 
cấp. Kể từ thời điểm này, ô tô chuyển động chậm dần đều với vận tốc ()
10
20
v t
t
=-
+
, 
trong đó t là thời gian tính bằng giây kể từ lúc đạp phanh. Gọi ()
s t là quãng đường xe ô 
tô đi được trong t kể từ lúc đạp phanh. 
a) Quãng đường ()
s t mà xe ô tô đi được trong thời gian t là một nguyên hàm của hàm số 

v t. 
b) ()
2
5
20
s t
t
t
=-
+
. 
c) Xe ô tô đó va vào chướng ngại vật ở trên đường. 
d) Thời gian kể từ lúc đạp phanh đến khi xe ô tô dừng hẳn là 2 giây. 
Câu 44. Một vật đang ở nhiệt độ 100 C
°
thì được đặt vào môi trường X có nhiệt độ 35 C
°
. Kể từ 
đó, nhiệt độ của vật giảm theo tốc độ 

2
130.
t
T
t
e-
'
=-
, trong đó 

T t là nhiệt độ tính 
theo C
°
 tại thời điểm t phút kể từ khi được đặt trong môi trường X. Khi đó: 
a) Nhiệt độ của vật tại thời điểm 
2
t =
 phút là ()

2
0
T t
T
t dt
'
= tích phân 
. 
b) Tốc độ giảm nhiệt độ của vật giảm dần theo thời gian. 
c) ()

2
0
T t
T
t dt
'
= tích phân 
 với ()
0
100
T
=
. 
d) ()
2
65.
35
t
T t
e-
=
+
. 
Câu 45. Giả sử lợi nhuận biên của một sản phẩm được mô hình hóa bằng công thức 

0,0008
10,4
P
x
x
'
=-
+
. Ở đây ()
P x là lợi nhuận khi bán được x đơn vị sản phẩm. 
a) Lợi nhuận khi bán được x đơn vị sản phẩm được tính bằng công thức: 

2
0,0008
10,4
P x
x
x
=-
+
. 
b) Lợi nhuận khi bán được 50 sản phẩm đầu tiên là 519 triệu đồng. 
c) Biết sự thay đổi của lợi nhuận khi doanh số tăng từ 50 lên a đơn vị sản phẩm lớn hơn 
517 triệu đồng, khi đó giá trị nhỏ nhất của a là 100. 
d) Sự thay đổi của lợi nhuận khi doanh số tăng từ 50 lên 55 đơn vị sản phẩm là 49,79 
triệu 
```

### Nguồn: `Ôn tập.pdf` (page_81) — `[VDC Score: 22.5]`
```text
Trang. 79 
CHỦĐỀ4. NGUYÊN HÀM VÀ TÍCH PHÂN
b) 

2 =- tích phân 
d
b
c
S
f x
x 
c) 

3 =- tích phân 
d
d
c
S
f x
x 
d) 

-
+
= tích phân 
 tích phân 
 tích phân 
d
d
d
b
d
a
c
H
c
b
S
f x
x
f x
x
f x
x 
Câu 3. Một người điều khiển ô tô đang ở đường dẫn muốn nhập làn vào đường cao tốc. Khi xe ô tô cách điểm 
nhập làn 200m, tốc độ của ô tô là 36
/
km h. Hai giây sau đó, ô tô bắt đầu tăng tốc với tốc độ 
0
=
+
 Z 
>

,(,
,
)
v t
at
b a b
R a
 trong đó t là thời gian tính bằng giây kể từ khi bắt đầu tăng tốc. Biết rằng ô tô 
nhập làn cao tốc sau 12 giây và duy trì sự tăng tốc đó trong 24 giây kể từ khi bắt đầu tăng tốc. 
a) Quãng đường ô tô đi được từ khi bắt đầu tăng tốc đến khi nhập làn là 180m. 
b) Giá trị của 
10
=
b
. 
c) Quãng đường ()
S t (đơn vị: mét) mà ô tô đi được trong thời gian t giây (0
24
<=<=
t
) kể từ khi tăng tốc 
được tính theo công thức 
24
0
= tích phân 

S t
v t dt. 
d) Sau 24 giây kể từ khi tăng tốc, tốc độ của ô tô không vượt quá tốc độ tối đa cho phép là 100
/
km h. 
Câu 4. Giả sử lợi nhuận biên (tính bằng triệu đồng) của một sản phẩm được mô hình hóa bằng công thức 

0 0008
10 4
'
=-
+
,
,
P x
x
. Ở đây ()
P x là lợi nhuận (tính bằng triệu đồng) khi bán được x đơn vị sản phẩm. 
a) Lợi nhuận khi bán được x đơn vị sản phẩm được tính bằng công thức ()
2
0 0008
10 4
=-
+
,
,
P x
x
x. 
b) Lợi nhuận khi bán được 50 sản phẩm đầu tiên là 519 triệu đồng. 
c) Biết sự thay đổi của lợi nhuận khi doanh số tăng từ 50 lên a đơn vị sản phẩm lớn hơn 517 triệu đồng, 
khi đó giá trị nhỏ nhất của a là 100. 
d) Sự thay đổi của lợi nhuận khi doanh số tăng từ 50 lên 55 đơn vị sản phẩm là 49 79
,
 triệu đồng. 
PHẦN III. Câu trắc nghiệm trả lời ngắn. 
Câu 1. Một ô tô đang di chuyển với tốc độ 20 m / s thì hãm phanh nên tốc độ
/
m s của xe thay đổi theo 
thời gian t được tính theo công thức ()

20
5
0
4
=
-
<=<=
.
v t
t
t
 Tính tốc độ trung bình của xe trong khoảng 
thời gian kể từ khi hãm phanh đến khi dừng hẳn. 
Câu 2. Tại một nhà máy, gọi ()
C x là tổng chi phí để sản xuất x tấn sản phẩm A trong một tháng. Khi đó, 
đạo hàm 

'
C x, gọi là chi phí cận biên, cho biết tốc độ tăng tổng chi phí theo lượng sản phẩm được sản 
xuất. Giả sử chi phí cận biên của nhà máy đượ
```

## Chủ đề VDC: `dang_oxyz_can_bang_luc_vat_ly`
### Nguồn: `Toán thực tế.pdf` (page_119) — `[VDC Score: 25.0]`
```text
Chuyên đềtoán thực tế
Nhóm Ba Đưòng Đồng Quy – 0889 971 004
118
TOÁN 12
TOÁN 12
TOÁN 12
Câu 35
Trong không gian Oxyz, một
vật được treo bằng ba sợi dây không dãn,
mỗi sợi dây có một đầu lần lượt được
gắn tại các điểm A(-2; -1; 0), B(2; -1; 0),
C(0; 4; 0), còn đầu kia được gắn với vật
tại điểm D(0; 0; -4) như hình vẽ(trong đó
mặt phẳng (Oxy) song song với mặt đất,
trục Oz hướng thẳng lên trên).
x
y
z
O
A
B
C
D
Biết rằng mỗi sợi dây được thiết kếđểchịu được lực căng tối đa là 15 N. Đểkhông dây
nào bịđứt thì trọng lượng tối đa của vật bằng bao nhiêu Newton (không làm tròn kết quả
các phép tính trung gian, chỉlàm tròn kết quảcuối cùng đến hàng phần mười)?
KQ:
Câu 36
Trạm không lưu sân bay Đà Nẵng xây
dựng hệtọa độOxyz (gốc O đặt tại Đà Nẵng) để
theo dõi vịtrí các chuyến bay. Lúc 6h máy bay A
xuất phát từĐà Nẵng đến TpHCM theo tia OA
lần lượt hợp với ba tia Ox; Oy; Oz các góc bằng
nhau với vận tốc 800 km/h.
x
y
z
x'
y'
O
A
B
Mười phút sau máy bay B đi Hà Nội theo tia OB hợp với ba tia Ox'; Oy'; Oz các góc
bằng nhau với vận tốc 900 km/h (hình vẽminh họa). Tính khoảng cách (đơn vịkm và làm
tròn đến hàng đơn vị) giữa hai máy bay A và B lúc 6h30 phút.
KQ:
Câu 37
Một kiến trúc sư đang thiết kếhệthống đèn
thảnghệthuật cho sảnh của một khách sạn. Cấu trúc
gồm một móc treo chính S gắn cốđịnh trên trần nhà. Từ
móc S, có ba sợi cáp thép treo ba bóng đèn giống nhau
tại các vịtrí A, B, C.
S
G
A
B
C
Thông sốkỹthuật được cho như sau: chiều dài ba sợi cáp đều bằng 2,4 m. Do cách
bốtrí nghệthuật bất đối xứng, góc tạo bởi các sợi cáp tại móc treo S là ’
ASB = 60◦,
’
BSC = 90◦, ’
CSA = 120◦. Đểgiúp dây điện và tăng độcứng vững, kiến trúc sư lắp thêm
một thanh trục cứng rỗng nối từđỉnh S đến trọng tâm G của tam giác ABC. Tính chiều
dài của thanh trục SG (làm tròn đến hàng phần trăm).
KQ:
```

### Nguồn: `Toán thực tế.pdf` (page_116) — `[VDC Score: 25.0]`
```text
Nhóm Ba Đưòng Đồng Quy – 0889 971 004
Chuyên đềtoán thực tế
115
TOÁN 12
TOÁN 12
TOÁN 12
Câu 28
Trong không gian Oxyz, một
vật được treo bằng ba sợi dây không dãn,
mỗi sợi dây có một đầu lần lượt được
gắn tại các điểm A(-2; -1; 0), B(2; -1; 0),
C(0; 4; 0), còn đầu kia được gắn với vật
tại điểm D(0; 0; -4) như hình vẽ(trong đó
mặt phẳng (Oxy) song song với mặt đất,
trục Oz hướng thẳng lên trên).
x
y
z
O
A
B
C
D
Biết rằng mỗi sợi dây được thiết kếđểchịu được lực căng tối đa là 15 N. Đểkhông dây
nào bịđứt thì trọng lượng tối đa của vật bằng bao nhiêu Newton (không làm tròn kết quả
các phép tính trung gian, chỉlàm tròn kết quảcuối cùng đến hàng phần mười)?
KQ:
Câu 29
Trạm không lưu sân bay Đà Nẵng xây
dựng hệtọa độOxyz (gốc O đặt tại Đà Nẵng) để
theo dõi vịtrí các chuyến bay. Lúc 6h máy bay A
xuất phát từĐà Nẵng đến TpHCM theo tia OA
lần lượt hợp với ba tia Ox; Oy; Oz các góc bằng
nhau với vận tốc 800 km/h.
x
y
z
x'
y'
O
A
B
Mười phút sau máy bay B đi Hà Nội theo tia OB hợp với ba tia Ox'; Oy'; Oz các góc
bằng nhau với vận tốc 900 km/h (hình vẽminh họa). Tính khoảng cách (đơn vịkm và làm
tròn đến hàng đơn vị) giữa hai máy bay A và B lúc 6h30 phút.
KQ:
Câu 30
Những căn lều gỗđược phác thảo dưới
dạng một hình lăng trụđứng tam giác OAB.O'A'B'
như trong hình dưới. Với hệtrục toạđộOxyz thểhiện
như hình (đơn vịđo lấy theo centimét), hai điểm A' và
B' có tọa độlần lượt là (240; 450; 0) và (120; 450; 300).
Mỗi căn nhà gỗcó chiều dài là a cm, chiều rộng là b
cm, mỗi cạnh bên của mặt tiền có độdài là c cm. Tính
a + b + c (làm tròn đến hàng đơn vị).
z
y
x
A'
O'
A
B
B'
O
KQ:
Câu 30
Hình bên dưới minh họa một cái lều hai mái là hai hình chữnhật giống nhau
trong không gian Oxyz. Biết các kích thước của mái lều là SA = 5m, AB = 10m, độcao
từS xuống mặt đất là 4m. Bạn An muốn trang trí chiếc lều bằng cách treo các sợi dây cờ
trang trí từcác góc lều O, A, B, C đến đuôi một chiếc đèn treo từvịtrí chính giữa của
SQ, cách SQ bằng 30cm. Hỏi tổng chiều dài sợi dây cờtrang trí tối thiểu bạn An cần mua
```

### Nguồn: `Toán thực tế.pdf` (page_86) — `[VDC Score: 23.5]`
```text
Nhóm Ba Đưòng Đồng Quy – 0889 971 004
Chuyên đềtoán thực tế
85
TOÁN 12
TOÁN 12
TOÁN 12
Câu 3
Có ba lực cùng tác động vào một cái bàn
như hình vẽ. Trong đó hai lực #»
F 1, #»
F 2 có giá nằm
trên mặt phẳng chứa mặt bàn, tạo với nhau một
góc 110◦và có độlớn lần lượt là 9 (N) và 4 (N), lực
#»
F 3 vuông góc với mặt bàn và có độlớn 7 (N). Độ
lớn hợp lực của ba lực trên là a (N), tìm giá trịcủa
a. (kết quảquy tròn vềsốnguyên).
#»
F 1
#»
F 3
#»
F 2
KQ:
Câu 4
Treo một vật nặng có trọng lượng 30
N bởi ba sợi dây giống hệt nhau, các sợi dây đôi
một tạo với nhau một góc 90◦(như hình vẽ). Gọi
#»
F 1; #»
F 2; #»
F 3 lần lượt là lực căng của ba sợi dây
nói trên. Độlớn của lực F1 bằng bao nhiêu? (làm
tròn kết quảđến hàng đơn vị).
KQ:
#»
P
#»
F 1
#»
F 2
#»
F 3
A
B
C
M
G
S
Câu 5
Nếu một vật có khối lượng m (kg) thì lực hấp dẫn #»
P của Trái Đất
tác dụng lên vật được xác định theo công thức #»
P = m#»g, trong đó #»g là gia
tốc rơi tựdo có độlớn g = 9,8 m/s2. Tính độlớn của lực hấp dẫn của Trái
Đất tác dụng lên một quảtáo có khối lượng 102 gam. Làm tròn kết quảđến
hàng đơn vị.
KQ:
m
#»g
#»
P
Câu 6
Cho biết công A (đơn vị: J) sinh bởi
lực #»
F tác dụng lên một vật được tính bằng công
thức A = #»
F · #»d, trong đó #»d là vectơ biểu thịđộ
dịch chuyển của vật (đơn vịcủa
#»d
 là m) khi
chịu tác dụng của lực #»
F.
#»
P
#»d
Một chiếc xe có khối lượng 1,5 tấn đang đi xuống trên một đoạn đường dốc có góc
nghiêng 5◦so với phương ngang. Tính công sinh bởi trọng lực #»P khi xe đi hết đoạn đường
dốc dài 30 m (làm tròn kết quảđến hàng đơn vị), biết rằng trọng lực #»
P được xác định bởi
công thức #»P = m#»g, với m (đơn vị: kg) là khối lượng của vật và #»g là gia tốc rơi tựdo có độ
lớn g = 9,8 m/s2. Làm tròn kết quảđến hàng chục.
KQ:
```

## Chủ đề VDC: `dang_oxyz_mat_cau`
### Nguồn: `Toán thực tế.pdf` (page_271) — `[VDC Score: 16.0]`
```text
Chuyên đềtoán thực tế
Nhóm Ba Đưòng Đồng Quy – 0889 971 004
270
TOÁN 12
TOÁN 12
TOÁN 12
Nếu mặt phẳng (P) cắt mặt cầu (S) theo thiết diện là một đường tròn C(H, r) thì
đường tròn (C) có bán kính r =
√
R2 -IH2.
II
BÀI TẬP ÁP DỤNG
1
Trắc nghiệm đúng sai
Câu 1
(MH-THPTQG2025). Các
thiên
thạch
có
đường kính lớn hơn 140m và có thểlại gần Trái Đất ở
khoảng cách nhỏhơn 7500000 km được coi là những
vật thểcó khảnăng va chạm gây nguy hiểm cho Trái
Đất. Đểtheo dõi những thiên thạch này, người ta
đã thiết lập các trạm quan sát các vật thểbay gần
Trái Đất.
6400km
6600km
A
B
M
N
O
Giảsửcó một hệthống quan sát có khảnăng theo dõi các vật thểởđộcao không vượt
quá 6600 km so với mực nước biển. Coi Trái Đất là khối cầu có bán kính 6400 km. Chọn
hệtrục tọa độOxyz trong không gian có gốc O tại tâm Trái Đất và đơn vịđộdài trên mỗi
trục tọa độlà 1000 km. Một thiên thạch (coi như một hạt) chuyển động với tốc độkhông
đổi theo một đường thẳng từđiểm M(6; 20; 0) đến điểm N(-6; -12; 16).
a
Đường thẳng MN có phương trình tham sốlà
{
|
{
|
{
x = 6 + 3t
y = 20 + 8t
z = -4t
, (t ∈R).
b
Vịtrí đầu tiên thiên thạch di chuyển vào phạm vi theo dõi của hệthống quan sát
là điểm A(-3; -4; 12).
c
Khoảng cách giữa vịtrí đầu tiên và vịtrí cuối cùng mà thiên thạch di chuyển
trong phạm vi theo dõi của hệthống quan sát là 18900 km (kết quảlàm tròn đến
hàng trăm theo đơn vịki-lô-mét).
d
Nếu thời gian di chuyển của thiên thạch trong phạm vi theo dõi của hệthống quan
sát là 3 phút thì thời gian nó di chuyển từM đến N là 6 phút.
Câu 2
Trong không gian Oxyz (đơn vịtrên mỗi trục là mét), một ngọn hải đăng được
đặt ởvịtrí I (10; 20; 30) với bán kính phủsáng là 3 km.
a
Phương trình mặt cầu mô tảranh giới bên ngoài của vùng phủsáng trên biển của
hải đăng là (x -10)2 + (y -20)2 + (z -30)2 = 3 0002.
b
Người đi biển ởvịtrí A (50; 20; 0) nhìn thấy được ánh sáng của ngọn hải đăng.
c
Người đi biển ởvịtrí B (4 030; 50; 40) nhìn thấy được ánh sáng của ngọn hải đăng.
d
Nếu hai người đi biển có thểnhìn thấy ánh sáng của ngọn hải đăng thì khoảng
cách giữa hai người đó không quá 6 km.
```

### Nguồn: `Toán thực tế.pdf` (page_287) — `[VDC Score: 23.5]`
```text
Chuyên đềtoán thực tế
Nhóm Ba Đưòng Đồng Quy – 0889 971 004
286
TOÁN 12
TOÁN 12
TOÁN 12
Câu 19
Trong không gian Oxyz, mỗi đơn vịtrên trục có độdài 10 km. Một trạm theo
dõi được đặt ởgốc tọa độvà có thểphát hiện được các vật thểcách nó một khoảng không
quá 30 km. Một vệtinh do thám di chuyển từvịtrí A(4; 2; 1) đến vịtrí B
Å
-1; -1
2; 7
2
ã
với vận tốc 80 km/h theo một đường thẳng. Thời gian mà vệtinh di chuyển trong phạm
vi phát hiện của trạm theo dõi bằng bao nhiêu phút (kết quảlàm tròn đến hàng phần
mười)?
KQ:
Câu 20
Trong không gian với hệtrục tọa độOxyz, một cánh tay robot được lập
trình đểgắp một chi tiết hình cầu có bán kính R = 1 đặt lên băng chuyền tại vịtrí
A(5; 0; 0). Trong không gian làm việc của robot có một chướng ngại vật là một mặt phẳng
(P): x + y + z -10 = 0. Đểtối ưu hóa năng lượng và thời gian, robot cần di chuyển đầu
gắp từvịtrí xuất phát O(0; 0; 0) đến điểm B trên mặt cầu chi tiết sao cho đường đi là
ngắn nhất và không va chạm với chướng ngại vật (P). Tính độdài đường đi ngắn nhất
mà robot cần thực hiện.
KQ:
Câu 21
Trong không gian Oxyz (đơn vịkm), Trái đất được mô phỏng là mặt cầu tâm
O bán kính R = 6 400 và đường xích đạo được xem là đường tròn giao tuyến giữa mặt
cầu mô phỏng trái đất và mặt phẳng (Oxy). Tại Bắc Cực I(0; 0; 6 400), Bộchỉhuy thiết
lập một “Vòm An Ninh”.Vùng an toàn này là một mặt cầu tâm I có bán kính quét là
Rq = 1 280
√
10. Bất kỳtàu nào đi vào biên giới của vùng này sẽđược bảo vệtuyệt đối.
Siêu điệp viên Alpha đang ẩn náu tại tọa độM(0; 5 120; 3 840). Anh nhận được mật lệnh:
Phải di chuyển từvịtrí hiện tại xuống đường Xích đạo đểkích hoạt thiết bịđịnh vị, sau
đó lập tức rút lui vềranh giới Vòm An Ninh tại điểm nhập K theo lộtrình ngắn nhất để
tàu thoát. Biết vận tốc di chuyển của Alpha là vA = 60 km/h. Cùng lúc đó, tàu truy kích
Beta đang phục kích tại vịtrí N(0; -6 400; 0). Ngay khi Alpha xuất phát, Beta tính toán
được chính xác điểm K và lao đến đểchặn đầu. Tàu Beta phải duy trì vận tốc tối thiểu
là bao nhiêu km/h đểcó thểchặn được Alpha trước lúc điệp viên này vào ranh giới vùng
an toàn? (xem vận tốc của Alpha và Beta là chuyển động đều và hai tàu di chuyển trên
mặt cầu. Làm tròn kết quảđến hàng phần chục)
KQ:
Câu 22

```

### Nguồn: `Toán thực tế.pdf` (page_275) — `[VDC Score: 20.5]`
```text
Chuyên đềtoán thực tế
Nhóm Ba Đưòng Đồng Quy – 0889 971 004
274
TOÁN 12
TOÁN 12
TOÁN 12
a
Ranh giới vùng phát sóng bên ngoài của đài kiểm soát không lưu trong không
gian là mặt cầu có bán kính bằng 300 km.
b
Phương trình mặt cầu đểmô tảranh giới bên ngoài vùng phát sóng của đài kiểm
soát không lưu trong không gian là x2 + y2 + z2 = 360 000.
c
Máy bay đang chuyển động theo đường thẳng d đến vịtrí điểm M
Ä
-500; 100; 100
√
11
ä
.
Vịtrí này nằm ngoài vùng kiểm soát không lưu của đài kiểm soát không lưu
sân bay.
d
Thời gian kểtừkhi đài kiểm soát không lưu phát hiện máy bay đến khi máy bay
ra khỏi vùng kiểm soát không lưu là 4
3 giờ.
Câu 11
Hải đăng là một ngọn tháp (nhà
hoặc khung) được thiết kếđểchiếu sáng
từmột hệthống đèn và thấu kính, hoặc
thời xưa là chiếu sáng bằng lửa, với mục
đích hỗtrợcho các hoa tiêu trên biển định
hướng và tìm đường. Vào năm 293 trước
Công nguyên, ngọn hải đăng đầu tiên đã
được người Phoenicia xây dựng trên hòn đảo
Pharos tại Alexandria.
Trong không gian với hệtọa độOxyz (đơn vịtrên mỗi trục là một mét), coi một phần mặt
biển được khảo sát là mặt phẳng (Oxy), trục Oz hướng lên trên vuông góc với mặt biển;
một ngọn hải đăng đỉnh cao 50 mét so với mực nước biển (Hình bên) biết đỉnh ởvịtrí
I(21; 35; 50), biết rằng ngọn hải đăng này được thiết kếvới bán kính phủsáng là 4km.
a
Phương trình mặt cầu đểmô tảranh giới của vùng phủsáng trên biển của ngọn
hải đăng trên là (x -21)2 + (y -35)2 + (z -50)2 = 16.
b
Người đi biển coi là một điểm ởvịtrí D(5121; 658; 0) thì có thểnhìn thấy được ánh
sáng của ngọn hải đăng trên.
c
Ngọn Hải đăng phủmột vùng sáng trên mặt biển thì bán kính vùng sáng này là
3999, 7 (làm tròn đến hàng phần mười của mét) giảsửyếu tốbịche khuất bởi địa
hình là không đáng kể.
d
Giảsửngười đi biển coi là một điểm từvịtrí D(5121; 658; 0) di chuyển theo đường
thẳng đến chân ngọn Hải đăng với tốc độ7 hải lý/giờ; biết một hải lý bằng 1852
mét thì mất 5, 27 phút (kết quảlàm tròn đến hàng phần trăm) đểđến điểm đầu
tiên nhìn thấy được ánh sáng ngọn Hải đăng trên.
Câu 12
Coi bềmặt trái đất là mặt cầu có bán kính 6 371 km. Chọn hệtrục tọa độOxyz
với gốc O tại tâm Trái Đất và đơn vịđộdài trên mỗi trục tọa độlà 6 371km. Giảsửtại
một thời điểm, 
```

## Chủ đề VDC: `dang_oxyz_cuc_tri_khoang_cach`
### Nguồn: `Vận dụng cao.pdf` (page_303) — `[VDC Score: 10.5]`
```text
CHƯƠNG II. HÌNH HỌC KHÔNG GIAN
Teacher2kkk | Học toán cùng GenZ
Câu 711. Cho khối chóp S.ABC có đáy là ∆ABC vuông tại B. Biết SA ⊥(ABC), AB =
√
2a,
BC =
√
6a, góc tạo bởi hai mặt phẳng (SAC) và (SBC) bằng 60◦. Thểtích của khối chóp S.ABC
bằng
A
√
3a3
3
.
B
√
3a3.
C
√
6a3.
D
√
6a3
3
.
Câu 712. Trong không gian với hệtrục toạđộOxyz, cho mặt cầu (S): (x-2)2 +(y +6)2 +z2 = 50
có tâm là I và điểm K (1;-3;0). Xét các điểm M thuộc (S) sao cho \
KMI lớn nhất. Khi đó, M luôn
thuộc mặt phẳng có phương trình dạng x+ay +bz +c = 0 với a, b, c là các sốnguyên. Giá trịcủa
a+b+c bằng
A 1.
B -10.
C -3.
D -13.
Câu 713. Cho hình nón (N) có góc ởđỉnh bằng 60◦, độdài đường sinh bằng a. Dãy hình cầu (S1),
(S2),..., (Sn),... thoảmãn (S1) tiếp xúc với mặt đáy và các đường sinh của hình nón (N); (Sn)
(n ≥2) tiếp xúc ngoài với

Sn-1

và tiếp xúc với các đường sinh của hình nón (N). Tính tổng thể
tích các khối cầu (S1), (S2),..., (Sn),... theo a.
A
πa3√
3
52
.
B 27πa3√
3
52
.
C πa3√
3
48
.
D 9πa3√
3
16
.
Câu 714. Cho hai đường thẳng d, ∆vuông góc và chéo nhau, có AB = a là đoạn vuông góc chung
(A ∈d; B ∈∆). Trên d và ∆lần lượt lấy hai điểm M, N sao cho AM = 2a, BN = 4a. Gọi I là tâm
mặt cầu ngoại tiếp tứdiện ABMN. Khoảng cách giữa hai đường thẳng AM và BI là
A
4a
√
17.
B
3a
√
15.
C 4a
5.
D 2a
√
2
3
.
Câu 715. Cho hình chóp S.ABC có AB = a, AC = a
√
3, SB > 2a và [
ABC = [
BAS = [
BCS = 90◦.
Biết sin của góc giữa đường thẳng SB và mặt phẳng (SAC) bằng
√
11
11. Tính thểtích khối chóp
S.ABC.
A
2a3√
3
9
.
B a3√
3
9
.
C a3√
6
6
.
D a3√
6
3
.
Câu 716. Cho hình hộp đứng ABCD.A'B'C'D' có đáy là hình thoi, \
BAD = 60◦và AA' = a. Gọi G
là trọng tâm của tam giác BCD. Biết khoảng cách từG đến mặt phẳng (A'BD) bằng a
√
21
21. Tính
thểtích khối hộp ABCD.A'B'C'D' theo a.
A
a3√
2
6
.
B a3√
3
6
.
C a3√
2
2
.
D a3√
3
2
.
Câu 717. Cho hình trụcó hai đáy là hình tròn tâm O và O', chiều cao h = a
√
3. Mặt phẳng đi qua
tâm O và tạo với OO' một góc 30◦, cắt hai đường tròn tâm O, O' tại bốn điểm là bốn đỉnh của một
hình thang có đáy lớn gấp đôi đáy nhỏvà diện tích bằng 3a2. Thểtích của khối trụđược giới hạn
bởi hình trụđã cho bằng
A
√
3πa3
12
.
B
√
3πa3
4
.
C
√
3πa3.
D
√
3πa3
3
.
BIÊN SOẠN: TRƯƠNG CÔNG ĐẠT
Tuy
```

### Nguồn: `Vận dụng cao.pdf` (page_297) — `[VDC Score: 10.5]`
```text
CHƯƠNG II. HÌNH HỌC KHÔNG GIAN
Teacher2kkk | Học toán cùng GenZ
Câu 663. Cho hình nón đỉnh S, góc ởđỉnh bằng 120◦, bán kính đáy R = 3a
√
3. Mặt phẳng (P) đi
qua đỉnh S cắt nón theo thiết diện là một tam giác. Khi diện tích thiết diện lớn nhất, góc giữa thiết
diện và mặt đáy của hình nón bằng
A 30◦.
B 90◦.
C 60◦.
D 45◦.
Câu 664. Cho hình chóp S.ABCD có ABCD là hình chữnhật tâm I cạnh AB = 3a, BC = 4a.
Hình chiếu của S trên mặt phẳng (ABCD) là trung điểm của ID. Biết rằng SB tạo với mặt phẳng
(ABCD) một góc 45◦. Diện tích mặt cầu ngoại tiếp hình chóp S.ABCD bằng
A
25π
2 a2.
B 125π
4
a2.
C 125π
2
a2.
D 4πa2.
Câu 665. Cho hình chóp S.ABCD có đáy ABCD là hình bình hành, trên cạnh SA lấy điểm M
và đặt SM
SA = x. Giá trịx đểmặt phẳng (MBC) chia khối chóp đã cho thành hai phần có thểtích
bằng nhau là
A x = 1
2.
B x =
√
5-1
2
.
C x =
√
5
3.
D x =
√
5-1
3
.
Câu 666. Cho lăng trụđứng ABC.A'B'C' có đáy là tam giác đều cạnh a. Giảsửd là một đường
thẳng thay đổi luôn đi qua C và d không nằm trong các mặt phẳng (ABC), (ACC'A'). Gọi MN là
đoạn vuông góc chung của hai đường thẳng AA' và d; M ∈d; N ∈AA'. Giá trịnhỏnhất của độdài
đoạn thẳng B'M là
A
a
2.
B a
√
3
3.
C
a
√
3-1

2
.
D a
√
3
6.
Câu 667. Cho khối hộp ABCD.A'B'C'D' có thểtích bằng 24. Gọi M là trung điểm BB',

MA'D

cắt BC tại K. Tính thểtích khối đa diện A'B'C'D'MKCD.
A 17.
B 12.
C 15.
D 18.
Câu 668. Cho khối lăng trụđứng ABC.A'B'C' có đáy ABC là tam giác vuông cân tại C, AB = 2a
và góc tạo bởi hai mặt phẳng (ABC'), (ABC) bằng 60◦. Gọi M, N lần lượt là trung điểm A'C' và
BC. Mặt phẳng (AMN) chia khối lăng trụthành hai phần. Thểtích của phần nhỏbằng
A
7
√
3a3
24
.
B
√
6a3
6
.
C 7
√
6a3
24
.
D
√
3a3
3
.
Câu 669. Cho hình chóp S.ABC có AB = BC = a, [
ABC = 120◦, [
SAB = [
SCB = 90◦và khoảng
cách từB đến mặt phẳng (SAC) bằng
2a
√
21. Thểtích hình chóp S.ABC bằng
A
a3√
5
10.
B a3√
5
2
.
C a3√
15
5
.
D a3√
15
10
.
Câu 670. Trong không gian với hệtoạđộOxyz, cho hai điểm A(0;1;2), B (2;1;-8). Từđiểm
M (-3;9;5) kẻđược bao nhiêu đường thẳng cắt mặt cầu đường kính AB tại hai điểm C, D thoả
mãn MC +MD = 24?
A Vô số.
B 1.
C 0.
D 2.
BIÊN SOẠN: TRƯƠNG CÔNG ĐẠT
Tuyển tập VD - VDC trong các đềthi thửTHPTQG | 562
H
Ọ
C
T
O
Á
N
C
Ù
N
```

### Nguồn: `Vận dụng cao.pdf` (page_198) — `[VDC Score: 4.0]`
```text
CHƯƠNG II. HÌNH HỌC KHÔNG GIAN
Teacher2kkk | Học toán cùng GenZ
Góc giữa hai mặt phẳng. Góc giữa hai mặt phẳng là góc giữa hai đường thẳng lần lượt vuông
góc với hai mặt phẳng đó.
• Định lí 1. GiảsửS là diện tích của đa giác (H) trong mặt phẳng (P) và S' là diện tích
hình chiếu (H') của (H) trên mặt phẳng (P ') thì S' = S cos
\
((P),(P '))
• Định lí 2. Diện tích hình chiếu của một hình phẳng bất kì bằng diện tích của hình đem
chiếu nhân với côsin của góc giữa mặt phẳng chứa hình đem chiếu và mặt phẳng chiếu.
Hai mặt phẳng vuông góc. Hai mặt phẳng (P), (Q) gọi là vuông góc với nhau, kí hiệu
(P) ⊥(Q), nếu góc giữa chúng bằng 90◦.
• Định lí 1. Nếu một mặt phẳng chứa một đường thẳng vuông góc với một mặt phẳng khác
thì hai mặt phẳng đó vuông góc với nhau.
• Định lí 2. Nếu hai mặt phẳng (P), (Q) vuông góc với nhau thì bất cứđường thẳng a nào
nằm trong mặt phẳng (P) mà vuông góc với giao tuyến của (P) và (Q) đều vuông góc với
mặt phẳng (Q).
• Hệquả1. Nếu hai mặt phẳng (P) và (Q) vuông góc với nhau và A là điểm thuộc (P) thì
đường thẳng a đi qua A và vuông góc với (Q) sẽnằm trong (P).
• Hệquả2. Nếu hai mặt phẳng cùng vuông góc với mặt phẳng thứba thì giao tuyến của
hai mặt phẳng (nếu có) cũng vuông góc với mặt phẳng thứba.
• Hệquả3. Qua đường thẳng a không vuông góc với mặt phẳng (Q) có duy nhất một mặt
phẳng (P) vuông góc với (Q).
Khoảng cách.
• Định nghĩa 1. Khoảng cách từđiểm M đến mặt phẳng (P) (hoặc đường thẳng ∆) là
khoảng cách giữa hai điểm M và H, trong đó H là hình chiếu của điểm M trên mặt phẳng
(P) (hoặc trên đường thẳng ∆).
• Định nghĩa 2. Khoảng cách giữa đường thẳng a và mặt phẳng (P) song song với a là
khoảng cách từmột điểm nào đó của a đến mặt phẳng (P).
• Định nghĩa 3. Khoảng cách giữa hai mặt phẳng song song là khoảng cách từmột điểm
bất kì của mặt phẳng này đến mặt phẳng kia.
• Định nghĩa 4. Khoảng cách giữa hai đường thẳng chéo nhau là độdài đoạn vuông góc
chung của hai đường thẳng đó.
Nhịdiện.
• Định nghĩa 1. Hình hợp bởi hai nửa mặt phẳng (P) và (Q) có chung bờa được gọi là một
nhịdiện. Hai nửa mặt phẳng (P) và (Q) gọi là hai mặt của nhịdiện. Đường thẳng a gọi là
cạnh của nhịdiện.
BIÊN SOẠN: TRƯƠNG CÔNG ĐẠT
Tuyển tập VD - VDC trong các đềthi thửT
```

## Chủ đề VDC: `dang_to_hop_quy_tac_dem`
### Nguồn: `Xác suất.pdf` (page_156) — `[VDC Score: 18.0]`
```text
S i e u G i o i: 40 | 44 
 
Tuyển chọn 248 bài xác suất thống kê hay và khó 
c) Chọn ngẫu nhiên trong thùng một hộp và từ hộp đó lấy ra hai sản phẩm để kiểm tra, xác suất để hai sản 
phẩm này đều tốt là 87
175. 
d) Chọn ngẫu nhiên trong thùng một hộp và từ hộp đó lấy ra hai sản phẩm để kiểm tra, giả sử hai sản phẩm 
đó đều tốt thì xác suất để hai sản phẩm đó thuộc hộp loại I là 52
87. 
Câu 219. [THPT Ngô Gia Tự - Vĩnh Phúc - Lần 1 năm 2025] Trong một kì thi tốt nghiệp trung học phổ 
thông, một tỉnh X có 80% học sinh lựa chọn tổ hợp A00 (gồm các môn Toán, Vật lí, Hoá học). Biết rằng, 
nếu một học sinh chọn tổ hợp A00 thì xác suất để học sinh đó đỗ đại học là 0,6; còn nếu một học sinh 
không chọn tổ hợp A00 thì xác suất để học sinh đó đỗ đại học là 0,7. Chọn ngẫu nhiên một học sinh của 
tỉnh X đã tốt nghiệp trung học phổ thông trong kì thi trên. Biết rằng học sinh này đã đỗ đại học. Tính xác 
suất để học sinh đó chọn tổ hợp A00. Kết quả làm tròn đến chữ số thập phân thứ 2 
Câu 220. [THPT Sáng Sơn - Vĩnh Phúc - Lần 1 năm 2025] Một kho hàng có 85% sản phẩm loại I và 
15% sản phẩm loại II, trong đó có 1% sản phẩm loại I bị hỏng, 4% sản phẩm loại II bị hỏng. Các sản 
phẩm có kích thước và hình dạng như nhau. Một khách hàng chọn ngẫu nhiên 1 sản phẩm. Xét các biến cố: 
A: “Khách hàng chọn được sản phẩm loại I”; 
B: “Khách hàng chọn được sản phẩm không bị hỏng”. 
a) ()
0,85.
P A =
 
b) (
|
)
0,99.
P B A =
 
c) ()
0,9855
P B =
. 
d) (
|
)
0,95
P A B =
. 
Câu 221. [THPT Sáng Sơn - Vĩnh Phúc - Lần 1 năm 2025] Trong 1000 hồ sơ của các thí sinh dự thi vào 
trường đại học Z có 600 hồ sơ của thí sinh tỉnh A và 400 thí sinh tỉnh B. Trong số thí sinh tỉnh A có 
25% trúng tuyển, tỉnh B có 65% không trúng tuyển. Rút ngẫu nhiên một hồ sơ được hồ sơ trúng tuyển. 
Xác suất để hồ sơ đó là của người tỉnh A bằng bao nhiêu (làm tròn kết quả đến hàng phần trăm)? 
Câu 222. [THPT Bình Xuyên - Vĩnh Phúc - Lần 1 năm 2025] Trong một căn phòng có 25 người họ 
Nguyễn và 14 người họ Lê, chọn ngẫu nhiên hai người trong phòng. Xác suất để hai người được chọn có 
cùng họ bằng 
A. 27.
741 
B. 7.
57 
C. 100.
247 
D. 391.
741 
Câu 223. [THPT Bình Xuyên - Vĩnh Phúc - Lần 1 năm 2025] Một bình đựng 50 
```

### Nguồn: `Tổng ôn.pdf` (page_556) — `[VDC Score: 14.0]`
```text
» Trang 149 
» Câu 18. Một nhóm gồm 11 học sinh trong đó có An, Bình, Cường tham gia một trò chơi đòi hỏi 
11 bạn phải xếp thành một vòng tròn. Tính xác suất để ba bạn An, Bình, Cường không 
có bạn nào xếp cạnh nhau (làm tròn kết quả đến hàng phần trăm). 
} Trả lời: 
0 
, 
4 
7 
» Câu 19. Một thầy giáo có 12 cuốn sách đôi một khác nhau, trong đó có 5 cuốn sách văn học, 4 
cuốn sách âm nhạc và 3 cuốn sách hội họa. Thầy lấy ngẫu nhiên ra 6 cuốn tặng cho 6 
học sinh, mỗi em một cuốn. Tính xác suất để sau khi tặng xong mỗi thể loại văn học, 
âm nhạc, hội họa đều còn lại ít nhất một cuốn (làm tròn kết quả đến hàng phần trăm). 
} Trả lời: 
0 
, 
8 
7 
» Câu 20. Gọi b là xác suất để bình phương của 3 phần tử được chọn lập thành một cấp số cộng. 
Tính 1
b
. Làm tròn kết quả đến hàng đơn vị. 
} Trả lời: 
6 
7 
7 
 
» Câu 21. Gọi S là tập hợp tất cả các số tự nhiên có 4 chữ số đôi một khác nhau và các chữ số 
thuộc tập 
1 2 3 4 5 6 7 8 9
;;;;;;;;
. Chọn ngẫu nhiên một số thuộc S, xác suất để số đó không 
có hai chữ số liên tiếp nào cùng chẵn bằng bao nhiêu (làm tròn kết quả đến hàng phần 
trăm)? 
} Trả lời: 
0 
, 
5 
2 
» Câu 22. Học sinh A thiết kế bảng điều khiển điện tử mở cửa phòng học của lớp mình. Bảng gồm 
10 nút, mỗi nút được ghi một số từ 0 đến 9 và không có hai nút nào được ghi cùng một 
số. Để mở cửa cần nhấn 3 nút liên tiếp khác nhau sao cho 3 số trên 3 nút theo thứ tự đã 
nhấn tạo thành một dãy số tăng và có tổng bằng 10. Học sinh B chỉ nhớ được chi tiết 3 
nút tạo thành dãy số tăng. Tính xác suất để B mở được cửa phòng học đó biết rằng nếu 
bấm sai 3 lần liên tiếp cửa sẽ tự động khóa lại (làm tròn kết quả đến hàng phần trăm). 
} Trả lời: 
0 
, 
1 
9 
» Câu 23. Cho đa giác đều 32 cạnh. Gọi S là tập hợp các tứ giác tạo thành có 4 đỉnh lấy từ các 
đỉnh của đa giác đều. Chọn ngẫu nhiên một phần tử của S. Xác suất để chọn được một 
hình chữ nhật bằng T. Tính 1
2
+
T
 (làm tròn kết quả đến hàng đơn vị)? 
} Trả lời: 
2 
 
 
 
» Câu 24. Trước kỳ thi học sinh giỏi, nhà trường tổ chức buổi gặp mặt 10 em học sinh trong đội 
tuyển. Biết các em có số thứ tự trong danh sách lập thành cấp số cộng. Các em ngồi 
ngẫu nhiên vào hai dãy bàn đối diện nhau, mỗi dãy có 5 ghế và m
```

### Nguồn: `GD&ĐT Ninh Bình.pdf` (page_3) — `[VDC Score: 19.5]`
```text
Trang 3/4 - Mã đề 0101 
 
Câu 3. 
Trong một dự án khảo sát địa chất thăm dò tài nguyên, các nhà khoa học phát hiện một túi khí 
tự nhiên trong lòng đất được xác định có dạng khối cầu ()
S, một lớp đá móng ngăn cách các 
địa tầng là mặt phẳng ()
P. Với hệ trục tọa độ Oxyz phù hợp (mặt đất nằm trên mặt phẳng 
Oxy, chiều dương trục Oz hướng lên trên), đơn vị trên mỗi trục là 10 m, mặt cầu ()
S có 
phương trình 
2
2
2
(
1)
(
2)
(
11)
25
x
y
z
-
+
-
+
+
=
, lớp đá móng ()
P được coi là một mặt phẳng có 
phương trình 2
2
22
0
x
y
z
-
+
+
=
. Để thực hiện việc thăm dò, các nhà khoa học đặt mũi khoan 
được định hướng bắt đầu từ vị trí 
(3;8;0)
A -
 và tiến tới liên tục theo phương của vectơ 
(4; 3; 7)
u =
--
. 
 a) Để tránh nguy cơ làm nứt gãy lớp đá móng ()
P dẫn đến rò rỉ khí áp suất cao, tiêu chuẩn kỹ 
thuật yêu cầu: Trong suốt thời gian mũi khoan di chuyển bên trong túi khí ()
S, khoảng cách từ 
mũi khoan đến lớp đá móng ()
P không được nhỏ hơn 5m. Quá trình khoan theo phương án 
này đã đáp ứng được tiêu chuẩn kỹ thuật đó. 
 b) Theo quỹ đạo chuyển động, mũi khoan sẽ đi xuyên qua túi khí ()
S tạo thành một đoạn 
đường ống có độ dài là 100m ngay trong lòng túi khí. 
 
 
c) Túi khí ()
S bị lớp đá móng ()
P chia thành hai phần có thể tích bằng nhau. 
d) Quỹ đạo của mũi khoan được mô tả bởi một phần đường thẳng d có phương trình chính tắc 
là 
3
8
4
3
7
x
y
z
-
+
=
=
-
-. 
Câu 4. 
Trên một đoạn đường thẳng, hai xe ô tô đang chạy ngược chiều nhau. Khi hai xe cách nhau 
110 m, hai người lái xe phát hiện ra nguy hiểm phía trước nên quyết định xử lí bằng cách đạp 
phanh để tránh va chạm. Kể từ lúc đạp phanh, xe 1 chuyển động chậm dần với gia tốc 
2
1()
4 (m/s)
a t
t
=-
 và xe 2 chuyển động chậm dần với gia tốc 
2
2()
3 (m/s)
a t
t
=-
 (trong đó t là 
thời gian tính bằng giây kể từ lúc người lái xe đó bắt đầu đạp phanh). Biết vận tốc của xe 1 và 
xe 2 ngay lúc phát hiện nguy hiểm lần lượt là 18 m/s và 24 m/s. 
 a) Giả sử người lái xe 1 đạp phanh ngay lập tức khi phát hiện ra nguy hiểm, quãng đường xe 1 
đi được kể từ lúc đạp phanh đến khi dừng hẳn là 40 m. 
 b) Giả sử người lái xe 2 đạp phanh ngay lập tức khi phát hiện ra nguy hiểm, kể từ lúc đạp 
phanh, xe 2 cần 4 giây để dừ
```

## Chủ đề VDC: `dang_xac_suat_co_dieu_kien_bayes`
### Nguồn: `Chuyên đề ôn thi tốt nghiệp THPT năm 2026 môn Toán – Nguyễn Tiến Hà.pdf` (page_283) — `[VDC Score: 16.5]`
```text
CHUYÊN ĐỀ ÔN THI TN.THPT MÔN TOÁN 12 NĂM 2026-2027 
CHỦ ĐỀ 15 
 
 
ThS. Nguyễn Tiến Hà – Zalo: 0949.888.993 
 Trang 280 
NGUYỄN TIẾN HÀ
NGUYỄN TIẾN HÀ
Câu 38. Các thí sinh tham dự một cuộc thi hoa khôi phải trải qua ba vòng thi: Vòng sơ khảo, Vòng bán kết 
và Vòng chung kết. Biết rằng, ban tổ chức sẽ chọn ra 50% thí sinh đã đăng kí để vào Vòng sơ khảo. 
Khi kết thúc vòng sơ khảo, ban tổ chức sẽ chọn ra 30% thí sinh của Vòng sơ khảo để vào Vòng bán 
kết. Khi kết thúc vòng bán kết, ban tổ chức sẽ chọn ra 20% thí sinh của Vòng bán kết để vào Vòng 
chung kết. Chọn ngẫu nhiên 1 thí sinh đăng kí tham dự cuộc thi hoa khôi. 
a) Xác suất để thí sinh được chọn lọt vào Vòng sơ khảo là 0,5. 
b) Xác suất để thí sinh được chọn lọt vào Vòng bán kết là 0,3. 
c) Xác suất thí sinh được chọn lọt vào Vòng chung kết là 0,03. 
d) Biết rà̀ng thí sinh được chọn không lọt vào Vòng chung kết, xác suất thí sinh đó lọt vào 
Vòng sơ khảo nhỏ hơn 0,49. 
Câu 39. Một nhà máy có hai phân xưởng cùng sản xuất một loại sản phẩm. Phân xưởng thứ nhất sản xuất 
60% và phân xưởng thứ hai sản xuất 40% tổng số sản phẩm của cả nhà máy. Tỉ lệ phế phẩm của 
từng phân xưởng lần lượt là 16% và 20%. Lấy ngẫu nhiên một sản phẩm trong kho hàng của nhà 
máy. 
a) Xác suất để sản phẩm đó do phân xưởng thứ nhất sản xuất là 0,6. 
b) Xác suất để lấy được phế phẩm bằng 0,176. 
c) Giả sử đã lấy được phế phẩm, xác suất phế phẩm đó do phân xưởng thứ nhất sản xuất 
bằng 0,55. 
d) Nếu lấy được sản phẩm tốt, khả năng sản phẩm đó do phân xưởng thứ hai sản xuất là 
cao hơn khả năng sản phẩm đó do phân xưởng thứ nhất sản xuất. 
Câu 40. Năm 2001, Cộng đồng Châu Âu có làm một đợt kiểm tra rất rộng rãi các con bò để phát hiện những 
con bò bị bệnh bò điên. Người ta tiến hành một loại xét nghiệm và cho kết quả như sau: Khi con bò 
bị bệnh bò điên thì xác suất để ra phản ứng dương tính trong xét nghiệm là 70%; còn khi con bò 
không bị bệnh thì xác suất để xảy ra phản ứng dương tính trong xét nghiệm đó là 10%. Biết rằng 
tỉ lệ bò bị mắc bệnh bò điên ở Hà Lan là 1,3 con trên 100000 con. Gọi X là biến cố một con bò bị 
bệnh bò điên, Y là biến cố một con bò phản ứng dương tính với xét nghiệm. 
a) 
0,91
P XY =
. 
 
b) ()
0,1000078
P Y =
```

### Nguồn: `Xác suất.pdf` (page_109) — `[VDC Score: 17.0]`
```text
S i e u G i o i: 109 | 116 
 
Tuyển chọn 248 bài xác suất thống kê hay và khó 
Câu 229. [THPT Vĩnh Yên - Vĩnh Phúc - Lần 1 năm 2025] 
 
Lời giải 
(a) Sai 
vì B và C tạo thành họ đầy đủ các biến cố nên ()

|
.
|
P A
P B P A B
P C P A C
=
+
 
(b) Đúng 
Gọi A là biến cố “Viên đạn trúng đích”. 
B là biến cố “ Xạ thủ loại I bắn”. 
C là biến cố “ Xạ thủ loại II bắn”. 
Ta có: 

2
8
0,2;
|
0.9;
0,8;
|
0.7
10
10
P B
P A B
P C
P A C
=
=
=
=
=
=
 
B và C tạo thành họ đầy đủ các biến cố nên ()

|
.
|
P A
P B P A B
P C P A C
=
+
 
0.2.0.9 0.8.0.7
0.74
=
+
=
 
(c) Sai 
vì 
iE tạo thành họ đầy đủ các biến cố nên 

1
1
2
2
.
|
.
|
.
|
o
o
P E
P E
P E E
P E
P E E
P E
P E E
=
+
+
 
(d) Sai 
Gọi E là biến cố “ Cả hai viên đạn đều bắn trúng đích” 
iE là biến cố “chọn được i xạ thủ loại I” 
Ta có: 

2
8
0
2
10
28;
|
0,7.0,7
0,49
45
o
C
P E
P E E
C
=
=
=
=
 

1
1
2
8
1
1
2
10
16;
|
0,9.0,7
0,63
45
C C
P E
P E E
C
=
=
=
=
 

2
2
2
2
2
10
1;
|
0,9.0,9
0,81
45
C
P E
P E E
C
=
=
=
=
 
Vì 
1
2
,
,
o
E E E tạo thành họ đầy đủ các biến cố nên ta có Xác suất để cả hai viên đạn đó trúng đích là: 

1
1
2
2
.
|
.
|
.
|
o
o
P E
P E
P E E
P E
P E E
P E
P E E
=
+
+
 
28
16
1
.0,49
.0.63
.0,81
0,5469
45
45
45
=
+
+
=
. 
Câu 230. [THPT Vĩnh Yên - Vĩnh Phúc - Lần 1 năm 2025] 
Lời giải 
Đáp số: 0,03 
Xét các biến cố: 
:
A “Người được chọn mắc bệnh X”; 
:
B “Người được chọn có phản ứng dương tính với xét nghiệm Y”. 
Khi đó, ()

0,002;
1 0,002
0,998;
P A
P A
=
= -
=

|
1;
|
0,06.
P B A
P B A
=
=
 
Theo công thức Bayes, ta có: 

|
0,002.1
|
0,03.
0,06188
.
|
.
|
P A P B A
P A B
P A P B A
P A P B A
=
=
~=
+
 
Câu 231. [THPT Yên Lạc 2 - Vĩnh Phúc - Lần 1 năm 2025] 
Lời giải 
 Đáp án: 0,54 
Gọi A là biến cố “người nghiện thuốc lá”, suy ra A là biến cố “người không nghiện thuốc lá” 
Gọi B là biến cố “người bị bệnh ung thư” 
Theo giả thiết ta có:
```

### Nguồn: `Xác suất.pdf` (page_99) — `[VDC Score: 17.0]`
```text
S i e u G i o i: 99 | 116 
 
Tuyển chọn 248 bài xác suất thống kê hay và khó 
Câu 201. [sở GD&ĐT Bắc Giang 2025] 
Lời giải 
 
a) Đ 
b) Đ 
c) S 
d) Đ 
 
Gọi A: “Người làm xét nghiệm có kết quả dương tính” 
B: “Người đó thực sự nhiễm virus” 
a) Do tỷ lệ người nhiễm virus trong cộng đồng là 

40
0,02
2%
2000
P B =
=
=
. Xác suất để người đó nhiễm 
virus là 2%. Mệnh đề đúng 
b) Ta có: 
81,2%
0,812
P A B =
=
 
Người làm xét nghiệm dương tính khi không thực sự nhiễm virus 

98,4%
0,984
P A B =
=
, suy ra 

1 0,984
0,016
1,6%
P A B = -
=
=
. Mệnh đề đúng 
c) Do đó 

(). 
(). 
0,02.0,812
0,98.0,016
0,03192
3,192%
P A
P B P A B
P B P A B
=
+
=
+
=
=
. Mệnh đề 
sai 
d) Theo công thức Bayes, ta có 
(). 
0,02.0,812

0,509

0,03192
P B P A B
P B A
P A
=
=
=
. Mệnh đề đúng 
Câu 202. [sở GD&ĐT Bắc Giang 2025] 
Lời giải: 
Đáp án: 0,44 
Xét các biến cố: 
:
A "Lấy được 1 chính phẩm từ thùng I sang thùng II"; 
:
B "Lấy được 1 chính phẩm từ thùng II". 
Khi đó, 
5
4
7
6
2

; ()
; 
; 
.
9
9
15
15
5
P A
P A
P B A
P B A
=
=
=
=
=
∣
∣
 
Theo công thức xác suất toàn phần, xác suất của biến cố B là: 
5 7
4 2

(). 
(). 
.
.
0,44.
9 15
9 5
P B
P A P B A
P A P B A
=
+
=
+
~=
∣
∣
 
Câu 203. [sở GD&ĐT Bắc Giang 2025] 
HD:
```

## Chủ đề VDC: `dang_thong_ke_do_phan_tan`
### Nguồn: `Chuyên đề ôn thi tốt nghiệp THPT năm 2026 môn Toán – Nguyễn Tiến Hà.pdf` (page_33) — `[VDC Score: 14.0]`
```text
CHUYÊN ĐỀ ÔN THI TN.THPT MÔN TOÁN 12 NĂM 2026-2027 
THỐNG KÊ 
 
 
ThS. Nguyễn Tiến Hà – Zalo: 0949.888.993 
 Trang 30 
NGUYỄN TIẾN HÀ
NGUYỄN TIẾN HÀ
Câu 54: Bảng dưới đây thống kê cân nặng của 45 học sinh lớp 10 tại một trường THPT 
 
Nhóm(Số cân nặng) 
Giá trị đại diện 
Tần số 
[40;44) 
42 
8 
[44;48) 
46 
12 
[48;52) 
50 
8 
[52;56) 
54 
10 
[56;62) 
58 
7 
 
 
45 
 
Khi đó độ lệch chuẩn của mẫu số liệu ghép nhóm trên là 
A. 1,15. 
B. 5,39. 
C. 2,15. 
D. 3,25. 
Câu 55: (SGD Phú Thọ) Hai mẫu số liệu ghép nhóm,
A B có bảng tần số ghép nhóm như sau: 
Nhóm A 
Nhóm 
)
[0;10 
)
[10;20 
)
[20;30 
)
[30;40 
)
[40;50 
Tần số 
8 
9 
5 
6 
2 
Nhóm B 
Nhóm 
)
[0,3;10,3
)
[10,3;20,3
)
[20,3;30,3 
)
[30,3;40,3 
)
[40,3;50,3 
Tần số 
16 
18 
10 
12 
4 
 
Gọi Delta 
 Delta 
,
A
B
Q
Q lần lượt là khoảng tứ phân vị của mẫu số liệu ghép nhóm,
A B. Phát biểu 
nào sau đây đúng? 
A. Delta 
= Delta 
2
B
A
Q
Q. 
B. Delta 
=
+ Delta 
0,3
B
A
Q
Q. C. Delta 
= Delta 
B
A
Q
Q. 
D. Delta 
=
 Delta 
0,3
B
A
Q
Q. 
 
Câu 56: (SGD Sơn La) Mẫu số liệu ghép nhóm thống kê mức lương của một công ty (đơn vị: triệu đồng) 
được cho trong bảng dưới đây. 
Nhóm 
(đơn vị: triệu đồng) 
)
[6;8 
)
[8;10 
)
[10;12 
)
[12;14 
)
[14;16 
 
Tần số 
6 
14 
18 
10 
2 
=50
n
 
Tứ phân vị thứ nhất của mẫu số liệu đã cho (làm tròn đến hàng phần trăm) là 
A. 8,81. 
B. 9,12. 
C. 8,96. 
D. 8,93. 
Câu 57: (SGD Hòa Bình) Mỗi ngày bác Hoa đều đi bộ để rèn luyện sức khỏe. Quãng đường đi bộ mỗi 
ngày (đơn vị: km) của bác Hoa trong 20 ngày được thống kê lại ở bảng sau: 
Quãng đường (km) 
[2,5;3,0) 
[3,0;3,5) 
[3,5;4,0) 
[4,0;4,5) 
[4,5;5,0) 
Số ngày 
3 
6 
5 
4 
2 
 
3 
9 
14 
18 
20 
Khoảng tứ phân vị của mẫu số liệu ghép nhóm (kết quả làm tròn đến hàng phần trăm) là 
A. 0,9. 
B. 0,96. 
C. 0,97. 
D. 0,8. 
 
Câu 58: (Cụm trường THPT Hải Dương) Dũng là học sinh rất giỏi chơi rubik, bạn có thể giải nhiều loại 
khối rubik khác nhau. Trong một lần luyện tập giải khối rubik 
3
3, bạn Dũng đã tự thống kê lại 
thời gian giải rubik trong 25 lần giải liên tiếp ở bảng sau: 
 
Thời gian giải rubik (giây) 
)
[8;10 
)
[10;12 
)
[12;14 
)
[14;16 
)
[16;18 
Số lần 
4 
6 
8 
4 
3 
Khoảng tứ phân vị của mẫu số liệu ghép nhóm bằng a
b, với a

```

### Nguồn: `GD&ĐT Ninh Bình.pdf` (page_2) — `[VDC Score: 16.5]`
```text
Trang 2/4 - Mã đề 0101 
 
Câu 8. 
Họ tất cả các nguyên hàm của hàm số 
sin
y
x
=
 là 
 
A. cos x
C
+
. 
 
B. sin x
C
-
+
. 
 C. sin x
C
+
. 
D. 
cos x
C
-
+
. 
Câu 9. 
Tập nghiệm của bất phương trình 
0,5
0,5
log
log
9
x >
 là 
 
A. 
;9
- vô cùng 
. 
 
B. 
0;9. 
 C. 
0;+ vô cùng. 
D. 
9;+ vô cùng. 
Câu 10. Một bác tài xế thống kê độ dài quãng đường (đơn vị: km) bác đã lái xe mỗi ngày trong một 
tháng (30 ngày) ở bảng số liệu ghép nhóm sau: 
 
Độ lệch chuẩn của mẫu số liệu ghép nhóm trên (kết quả làm tròn đến hàng phần trăm) bằng 
 
A. 3206,90. 
 
B. 56,63. 
C. 55,68. 
D. 55,67. 
Câu 11. Cho hàm số 

y
f x
=
 có đồ thị như hình vẽ dưới đây. Điểm cực tiểu của hàm số đã cho là 
 
 
A. 1. 
B. 2. 
C. 1
-. 
D. 4
-. 
Câu 12. Nếu khối lăng trụ 
.
ABC A B C
''' có thể tích bằng 60 thì khối chóp 
.
A ABC
'
 có thể tích bằng 
 
A. 60. 
 
B. 40. 
C. 180. 
D. 20. 
 
PHẦN II. Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng 
hoặc sai. 
Câu 1. 
Cho hàm số 

2
3
1
x
f x
x
+
=
-
 có đồ thị là đường cong ()
C. 
 
 
a) Có 2 tiếp tuyến của ()
C song song với đường thẳng 
:
5
3
d y
x
=-
-. 
 
b) Đồ thị hàm số 

y
f x
=
 có tiệm cận đứng là 
2
x =
 và tiệm cận ngang là 
1
y =. 
 
c) Hàm số 

y
f x
=
 nghịch biến trên 

1
\
. 
 
d) 

2
5
,
1
1
f
x
x
x
-
'
=
"!=
-
. 
Câu 2. 
Sói đồng cỏ Bắc Mỹ (coyote) là một loài động vật hoang dã phân bố chủ yếu ở Bắc Mỹ. Tại 
bang Oklahoma, Hoa Kỳ, 70% số coyote bị mắc một căn bệnh gọi là Ehrlichiosis. Người ta 
thực hiện xét nghiệm giúp phát hiện căn bệnh này. Kết quả xét nghiệm có thể là dương tính 
hoặc âm tính. Biết rằng nếu coyote bị bệnh, xác suất để xét nghiệm cho kết quả dương tính là 
97%; nếu coyote không bị bệnh, xác suất để xét nghiệm cho kết quả âm tính là 95%. Các bác 
sĩ thú y bắt ngẫu nhiên 1 con coyote ở Oklahoma và tiến hành xét nghiệm cho nó. 
 
a) Xác suất để con coyote bị bắt không bị bệnh và có kết quả xét nghiệm dương tính là 0,05. 
 
b) Xác suất để con coyote bị bắt có kết quả xét nghiệm âm tính là 30,6%. 
c) Giá trị dự đoán âm của xét nghiệm được định nghĩa là xác suất con coyote thực sự không bị 
bệnh biết rằng kết quả xét nghiệm của nó là âm tính. Giá trị dự đoán âm của xét nghi
```

### Nguồn: `Chuyên đề ôn thi tốt nghiệp THPT năm 2026 môn Toán – Nguyễn Tiến Hà.pdf` (page_563) — `[VDC Score: 19.0]`
```text
ĐỀ THI THỬ TN.THPT MÔN TOÁN 12 NĂM 2026-2027 
ĐỀ THI THỬ SỐ 10 
 
 
ThS. Nguyễn Tiến Hà – Zalo: 0949.888.993 
 Trang 560 
NGUYỄN TIẾN HÀ
NGUYỄN TIẾN HÀ
Câu 14: Trong không gian 
,
Oxyz xem mặt đất là mặt phẳng 
Oxy; trục Oz hướng lên. Tại cùng 
một thời điểm, một radar phát hiện một máy bay tại 

0;0;10
A
 bay theo hướng 

4;3;0
v =-

 không đổi và một xe tăng tại O di chuyển theo hướng 

3;4;0
u =

 không đổi. 
Sau 20 giây radar xác định được vị trí máy bay tại 
8;6;10
B -
 và xe tăng tại 
3
1
;
;0
20 5
E

 
a) Nếu máy bay và xe tăng tiếp tục giữ nguyên hướng và vận tốc không đổi thì 10 giây 
tiếp theo vị trí máy bay và xe tăng lần lượt là 
9
3
12;9;10,
;
;0
40 10
C
F

-

. 
b) Khoảng cách giữa máy bay và xe tăng sau 20 giây kể từ lúc radar phát hiện là 15km. 
c) Vận tốc trung bình của xe tăng trong 20 giây đầu tiên là 12,5 m/s. 
d) Một lúc sau, radar phát hiện máy bay vẫn giữa nguyên hướng bay ban đầu và cách A 
một khoảng 27 km, tốc độ máy bay lúc đó 1800 km/h, đồng thời xe tăng đang di chuyển 
theo hướng ban đầu và cách O một kilomet với tốc độ 60 km/h. Tốc độ thay đổi khoảng 
cách giữa máy bay và xe tăng lúc này là 1689 km/h. 
 
Câu 15: Cho 
hình 
chóp 
.
S ABC 
có 
tam 
giác 
ABC 
vuông 
tại 
,
3,
2,
B BC
BA
SA
=
=
 vuông góc với mặt phẳng 
ABC và 
2.
SA =
 
a) Thể tích khối chóp.
S ABC bằng 6. 
b) Khoảng cách từ C đến mặt phẳng 
SAB bằng 5. 
c) Số đo góc nhị diện 
,
,
S BC [A]

 bằng 
0
45. 
d) 
.
4.
SB AC =

 
 
Câu 16: Khảo sát chiều cao của 20 học sinh nam lớp 12A của một trường THPT X, người ta được 
kết quả thống kê trong bảng sau: 
 
Chiều cao 
[160;165)
[165;170)
[170;175) [175;180) [180;185) 
Số học sinh 
3 
5 
7 
4 
1 
 
a) Gọi 
1
2
20
;
;...;
x x
x là mẫu số liệu gốc gồm chiều cao của 20 học sinh trên được xếp theo 
thứ tự không giảm. Khi đó 
)
3
165;170
x
[
 Z [
 và 
)
9
170;175
x
[
 Z [
. 
b) Tứ phân vị thứ ba của mẫu số liệu ghép nhóm đã cho bằng 175. 
c) Khoảng tứ phân vị của mẫu số liệu ghép nhóm đã cho bằng 8,5. 
d) Chọn ngẫu nhiên một học sinh trong nhóm khảo sát nói trên, xác suất chọn được học 
sinh có chiều cao từ 175cm trở lên bằng 0,25. 
 
PHẦN III. (4,0 điểm) Câu trắc nghiệm trả lời ngắn. Thí sinh trả lời từ câu 17 đến câu 22. Ở 
mỗ
```

## Chủ đề VDC: `dang_hinh_khong_gian_goc_khoang_cach`
### Nguồn: `Ôn tập.pdf` (page_144) — `[VDC Score: 13.5]`
```text
Trang. 142 
CHỦĐỀ9. HÌNH HỌC KHÔNG GIAN
Câu 3. Cho hình chóp.
S ABCD có đáy ABCD là hình chữ nhật, cạnh SA vuông góc với mặt phẳng 

ABCD. Gọi 
,
H K lần lượt là hình chiếu vuông góc của điểm A lên cạnh SB và SC. 
a) SA vuông góc BD. 
b) BD vuông góc mặt phẳng 
SAC. 
c) AK vuông góc với mặt phẳng 
SCD. 
d) SC vuông góc mặt phẳng 
AHK. 
Câu 4. Cho hình chóp tứ giác đều có cạnh đáy bằng a, chiều cao bằng 2
a. Gọi M là trung điểm CD như 
hình vẽ. 
 
a) Đường thẳng SD là cạnh của nhị diện 
SAD và 
SCD. 
b) Góc nhị diện 

,
,

SAC
AC
ABCD
 là góc nhị diện vuông. 
c) Góc · 
SDO là góc phẳng nhị diệ[n]
,
,
S CD O. 
d) Số đo góc phẳng nhị diệ[n]
,
,
S CD O bằng 45°. 
PHẦN III. Câu trắc nghiệm trả lời ngắn. 
Câu 1. Cho hình chóp.S ABCD có đáy ABCD là hình bình hành tâm O. Gọi E là trung điểm SC. Gọi 
F là điểm trên đoạn BD sao cho 3
2
=
BF
BD và M là giao điểm của SB và 
AEF. Khi đó tỉ số 
SM
SB là a
b với,
 Z vô cùng 
a b
 và a
b là phân số tối giản. Tính 3 +
a
b. 
Câu 2. Cho hình chóp.S ABCD có đáy là hình bình hành. Gọi,I K lần lượt là trung điểm các cạnh 
,
BC CD và M là điểm trên cạnh SB sao cho
1
3
=
SM
SB
. Gọi N là gia điểm của MD và mặt phẳng 

SIK. Tính tỉ số ND
NM. 
Câu 3. Cho hình chóp.
S ABCD có đáy ABCD là hình bình hành. Gọi M là trung điểm cạnh BC, ()
 alpha là 
mặt phẳng qua 
,
A M và song song với SD. Mặt phẳng ()
 alpha cắt SB tại N, tính tỉ số SN
SB 
 Câu 4. Cho hình chóp.S ABC có M, 
3
=
SA
và Delta ABC vuông tại B có cạnh 
1
=
BC
, 
5
=
AC
. Tính 
theo a khoảng cách từ A đến 
SBC. (kết quả làm tròn đến hàng phần trăm) 
 Câu 5. Một cái hộp hình lập phương, bên trong nó đựng một mô hình đồ chơi có dạng hình chóp tứ giác đều 
mà đỉnh của hình chóp đó trùng với tâm của một mặt chiếc hộp, giả sử hình vuông đáy của hình chóp 
trùng với một mặt của chiếc hộp (mặt này cùng với mặt chứa đỉnh hình chóp là hai mặt đối nhau). Biết
```

### Nguồn: `Tổng ôn.pdf` (page_463) — `[VDC Score: 12.5]`
```text
» Trang 56 
» Câu 25. Cho hình chóp.S ABCD có đáy ABCD là hình vuông cạnh a, cạnh bên 
2
=
SA
a và 
vuông góc với mặt phẳng đáy. Gọi M là trung điểm cạnh SD. Tang của góc tạo bởi hai 
mặt phẳng 
AMC và 
SBC bằng bao nhiêu (làm tròn kết quả đến hàng phần trăm)? 
} Trả lời: 
0 
, 
8 
9 
» Câu 26. Cho tứ diện ABCD có 
3
=
=
=
=
AC
AD
BC
BD
, 
2
=
CD
x, 
 vuông góc 

ACD
BCD. Tìm giá trị 
của x để 
 vuông góc 

ABC
ABD (làm tròn kết quả đến hàng phần trăm). 
} Trả lời: 
1 
, 
7 
3 
» Câu 27. Cho hình lập phương 
''''
.
ABCD AB C D. Cosin của góc giữa hai mặt phẳng 
'
A BC và 
'
ABC
 bằng bao nhiêu? Viết kết quả dưới dạng thập phân, nếu có. 
} Trả lời: 
0 
, 
5 
 
» Câu 28. Cho hình lăng trụ đứng 
'''
.
ABC A B C có đáy ABC là tam giác cân với 
=
=
AB
AC
a và 
góc 
120
=
°
BAC
 và cạnh bên 
'=
BB
a. Gọi I là trung điểm của 
'
CC. Tính cosin của góc 
giữa hai mặt phẳng 
ABC và 
'
AB I (làm tròn kết quả đến hàng phần trăm). 
} Trả lời: 
0 
, 
5 
5 
» Câu 29. Cho hình chóp.S ABC có 
=
SA
a, 

 vuông góc 
SA
ABC, tam giác ABC vuông cân đỉnh A và 
2
=
BC
a
. Gọi 
,
M N lần lượt là trung điểm của 
,
SB SC. Cosin của góc giữa hai mặt 
phẳng 
MNA và 
ABC bằng bao nhiêu? 
} Trả lời: 
0 
, 
5 
8 
» Câu 30. Cho hình lăng trụ đứng 
'''
.
ABC A B C có 
=
=
AB
AC
a, góc 
120
=
°
BAC
, 
'=
AA
a. Gọi 
,
M N lần lượt là trung điểm của ''
B C và 
'
CC. Số đo góc giữa hai mặt phẳng 
AMN 
và 
ABC bằng bao nhiêu độ (làm tròn kết quả đến hàng phần mười)? 
} Trả lời: 
6 
4 
, 
3 
» Câu 31. Cho hình chóp.S ABCD có đáy là hình vuông ABCD cạnh a
, mặt bên SAB là tam giác đều và nằm trong mặt phẳng 
vuông góc với mặt phẳng 
ABCD. Gọi G là trọng tâm tam 
giác SAB và 
,
M N lần lượt là trung điểm của 
,
SC SD (tham 
khảo hình vẽ). 
Tính cosin của góc giữa hai mặt phẳng 
GMN và 
ABCD 
(làm tròn kết quả đến hàng phần trăm). 
} Trả lời: 
0 
, 
9 
6 
» Câu 32. Cho hình chóp.S ABCD có đáy là hình thang vuông tại A và D, 
2
=
=
=
,
AB
AD
a CD
a
. Gọi I là trung điểm cạnh AD, biết hai mặt phẳng 
SBI và 
SCI cùng vuông góc với 
đáy và thể tích khối chóp.S ABCD bằng 
3
3 15
5
a. Tính góc nhị diệ[n]

,
,
S BC D theo đơn 
vị độ. 
} Trả lời: 
6 
0 
 
 
----------------------------
```

### Nguồn: `Chuyên đề ôn thi tốt nghiệp THPT năm 2026 môn Toán – Nguyễn Tiến Hà.pdf` (page_599) — `[VDC Score: 21.5]`
```text
ĐỀ THI THỬ TN.THPT MÔN TOÁN 12 NĂM 2026-2027 
ĐỀ THI THỬ SỐ 18 
 
 
ThS. Nguyễn Tiến Hà – Zalo: 0949.888.993 
 Trang 596 
NGUYỄN TIẾN HÀ
NGUYỄN TIẾN HÀ
PHẦN III. (4,0 điểm) Câu trắc nghiệm trả lời ngắn. Thí sinh trả lời từ câu 17 đến câu 22. Ở 
mỗi câu thí sinh điền đáp án của câu đó. 
Câu 17: Một xưởng cơ khí nhận thiết kế một giá đỡ kim loại hình lăng trụ 
tam giác đều 
.
ABC A B C
'
'
' để trưng bày sản phẩm. Giá đỡ có các 
kích thước 
0,6
AB =
 mét; 
2
AA'=
 mét. Hai thanh kim loại chéo 
được gắn thêm để tăng độ chắc chắn cho giá đỡ: thanh AM nối A 
với trung điểm M của BC và thanh A B
'
. 
Xưởng cần tính khoảng cách nhỏ nhất giữa hai thanh chéo AM và 
A B
'
 để xem liệu việc thiết kế thêm hai chéo này có đủ khoảng trống 
để lắp thêm phụ kiện không? Hãy tính khoảng cách nhỏ nhất giữa 
hai thanh chéo AM và A B
'
. 
 
Câu 18: Vào năm 2020, dân số của một quốc gia là khoảng 97 triệu người và tốc độ tăng trưởng 
dân số là 0,91%. Nếu tốc độ tăng trường dân số này được giữ nguyên hằng năm, hãy ước 
tính dân số của quốc gia đó vào năm 2030. 
 
Câu 19: Hệ thống định vị cho phép xác định vị trí của một vật thể trong không gian. Trong cùng 
một thời điểm, vị trí của một điểm M trong không gian sẽ được xác định bởi bốn vệ tinh 
cho trước nhờ các bộ thu phát tín hiệu đặt trên các vệ tinh. Giả sử trong không gian với 
hệ tọa độ Oxyz, có bốn vệ tinh lần lượt đặt tại các điểm 
2;1;
2
A
-
, 
3;4;2
B
, 
0;5;6
C
, 

4;2;5
D
; vị trí 

;;
M a b c thỏa mãn 
 
  42
AM =
, 
 8
BM =, 
    106
CM =
, 
46
DM =
. 
Khoảng cách từ điểm M đến điểm B bằng bao nhiêu? 
 
Câu 20: Một cổng có hình dạng như hình vẽ với viền ngoài và trong là hai đường cong dạng 
parabol cùng trục đối xứng. 
 
Nhà trường dự định sơn mặt ngoài cổng với chi phí nhân công là 30.000 đồng/m2. Tính số 
tiền nhà trường trả cho nhân công. 
 
Câu 21: Một doanh nghiệp dự định sản xuất không quá 180 sản phẩm. Nếu doanh nghiệp sản 
xuất x sản phẩm 
1
180
x
<=
<=
 thì giá bán của mỗi sản phẩm là ()
35840
192
f x
x
=
-
 
và chi phí sản xuất bình quân trên một sản phẩm là 

2
19200
25,6
153,6
3072
g x
x
x
x
=
-
+
+
. Biết rằng mức thuế trên một sản phẩm là 512 
nghìn đồng. Hỏi doanh nghiệp cần sản xuất bao nhiêu sản phẩm để 
```

## Chủ đề VDC: `dang_trai_phang_hinh_khong_gian`
### Nguồn: `Phương pháp trải phẳng giải một số bài toán ứng dụng thực tế – Đặng Việt Đông.pdf` (page_10) — `[VDC Score: 22.0]`
```text
Gv: Đặng Việt Đông Trường THPT Nho Quan A Phương pháp trải phẳng 
 
 
ĐT: 0978064165 - Email: dangvietdong.ninhbinh.vn@gmail.com - ID Tik Tok: dongpay | Trang 10 
Facebook: https://www.facebook.com/dongpay - Kênh Youtube: Thầy Đặng Việt Đông 
(trừ đáy tiếp xúc mặt đất) thì tiểu cường luôn di chuyển 0,4 dm/s. Vì tiểu cường giỏi toán hình học 
không gian nên nó đã chọn con đường ngắn nhất để đi từ A đến B, hỏi thời gian tương ứng là bao 
nhiêu giây (làm tròn đến hàng phần chục)? 
 
Câu 19. Một ngôi nhà được thiết kế theo một khối hộp chữ nhật với chiều cao từ mặt nền đến mặt trần 
ABCD là 4m, phần trang trí trần nhà là một khối hộp chữ nhật 
.
ABCD PQRS, biết 

0,5
;
5;
4;
6
AP
m
AB
m AN
m BC
m
=
=
=
=
. Người ta cần hàn một đường gấp khúc bằng sắt NMR 
với M là điểm nằm trên mặt tường 
ADSP. Tìm độ dài ngắn nhất của đường gấp khúc NMR (kết 
quả làm tròn đến hàng phần chục). 
,
 
Câu 20. Cắt ba góc của một tam giác đều cạnh bằng 1 các đoạn bằng 
1
, 0
2

<
<

x
x
 phần còn lại là một tam 
giác đều bên ngoài là các hình chữ nhật, rồi gấp các hình chữ nhật lại tạo thành khối lăng trụ tam 
giác đều như hình vẽ. Tìm độ dài x để thể tích khối lăng trụ lớn nhất. (làm tròn kết quả đến chữ số 
thập phân thứ hai) 
 
Câu 21. Một con kiến bò từ điểm A (cố định) lên điểm B (linh động) trên đỉnh của bậc thang, rồi từ B đi 
xuống điểm C (cố định) như hình vẽ bên. Biết rằng một ô vuông gạch của cầu thang có độ dài các 
cạnh bằng 2 (cm). Gọi L là độ dài đường đi của con kiến. 
x
```

### Nguồn: `Phương pháp trải phẳng giải một số bài toán ứng dụng thực tế – Đặng Việt Đông.pdf` (page_4) — `[VDC Score: 20.5]`
```text
Gv: Đặng Việt Đông Trường THPT Nho Quan A Phương pháp trải phẳng 
 
 
ĐT: 0978064165 - Email: dangvietdong.ninhbinh.vn@gmail.com - ID Tik Tok: dongpay | Trang 4 
Facebook: https://www.facebook.com/dongpay - Kênh Youtube: Thầy Đặng Việt Đông 
B - BÀI TẬP 
DẠNG 1: TRẢI PHẲNG MÔ HÌNH CÓ DẠNG HÌNH CHÓP, HÌNH LĂNG TRỤ. 
Câu 1. 
Một khối gỗ hình hộp hình nhật có chiều dài, chiều rộng, chiều cao lần lượt là 30cm, 20cm và 
30cm (hình vẽ). Một con kiến xuất phát từ A muốn tới điểm B thì quãng đường ngắn nhất nó phải 
đi dài bao nhiêu cm? (làm tròn kết quả đến chữ số thập phân thứ nhất) 
 
Câu 2. 
Cho một cái hộp hình chữ nhật có kích thước ba cạnh lần lượt là 4cm, 6cm, 9cm như hình vẽ. 
 
Một con kiến ở vị trí A muốn đi đến vị trí B. Biết rằng con kiến chỉ có thể bò trên cạnh hay trên 
bề mặt của hình hộp đã cho. Gọi x cm là quãng đường ngắn nhất con kiến đi từ A đến B. Giá trị 
của x là bao nhiêu? (làm tròn kết quả đến chữ số thập phân thứ nhất) 
Câu 3. 
Một căn phòng hình hộp chữ nhật đặt trong hệ trục tọa độ Oxyz (như hình vẽ) đơn vị trên trục là 
m, biết
6;
AB
m
=
8;
BC
m
=
'
4
AA
m
=
. Người ta treo một cái đèn bóng tròn tại vị trí điểm 
'
A, có 
một giỏ hoa treo trong phòng, coi vị trí đặt giỏ hoa là 1 điểm M cách trần nhà 1m, cách mặt phẳng 
(
'
')
ADD A là 1m, cách mặt phẳng(
'
')
ABB A là 2m, với mặt phẳng 
ABCD là mặt nền nhà.
```

### Nguồn: `Phương pháp trải phẳng giải một số bài toán ứng dụng thực tế – Đặng Việt Đông.pdf` (page_56) — `[VDC Score: 22.0]`
```text
Gv: Đặng Việt Đông Trường THPT Nho Quan A Phương pháp trải phẳng 
 
 
ĐT: 0978064165 - Email: dangvietdong.ninhbinh.vn@gmail.com - ID Tik Tok: dongpay | Trang 56 
Facebook: https://www.facebook.com/dongpay - Kênh Youtube: Thầy Đặng Việt Đông 
Lại có 
1
1
1

2.
2

.
3 226
226
l BB
r
l BB
OB
OB
pi
pi
 alpha 
 alpha 
=
 => 
=
=
=
 
Thay vào công thức (1) có kết quả. 
74,6386
.
l
cm
~=
 
Câu 44. Một con kiến xuất phát từ A và đi hai vòng quanh hình nón cụt rồi dừng lại tại B như hình vẽ. Biết 
bán kính đáy lớn là 4cm và đáy nhỏ là 2cm, chiều cao 3cm. Quãng đường ngắn nhất con kiến 
đó phải đi là bao nhiêu cm? (làm tròn kết quả đến chữ số thập phân thứ hai). 
 
Lời giải 
Trả lời: 3,73 
Cắt hình nón cụt theo đường sinh AB rồi trải phẳng ta được hình vẽ với 
0
x >=
. 
 
Khi đó, quãng đường con kiến đi là S
AM
MB
=
+
. 
Ta có 
2
2
2(cm)
CD
AH
BH
=
+
=
 
 · 
 · 
 
 
 · 
0
0
2
2
2
2
2
2
2
2
2
2
2
2
2
tan
3
60
120
2
.
.cos
4
2
2
.
.cos
16
(2
)
4(2
)
12
2
4
12 (
0)
1
0
0
1
4
'
2
2
BAH
BAH
C
BM
BC
CM
BC CM
C
x
x
AM
AD
MD
AD MD
BAH
x
x
x
S
x
x
x
x
x
x
S
x
x
x
x
=
 => 
=
 => 
=
=
+
-
=
+
+
=
+
-
=
+
-
-
-
=
+
 => 
=
+
+
+
+
>=
+
 => 
=
+
>
">=
+
+
+
 
Vậy 

min
0
2
2 3
3,73
S
S
=
=
+
~=
```

## Chủ đề VDC: `dang_thuc_te_kinh_te_vi_mo`
### Nguồn: `Toán thực tế.pdf` (page_151) — `[VDC Score: 25.0]`
```text
Chuyên đềtoán thực tế
Nhóm Ba Đưòng Đồng Quy – 0889 971 004
150
TOÁN 12
TOÁN 12
TOÁN 12
vận tốc là v(t) = -2t
5 + 4 (km/h). Nếu coi thời điểm ban đầu t = 0 là lúc cá bắt đầu bơi
vào dòng sông thì khoảng cách xa nhất mà con cá có thểbơi được là bao nhiêu km?
KQ:
Câu 6
Một vật chuyển động với gia tốc được cho bởi hàm sốa(t) = 5 cos t m/s2. Lúc
bắt đầu chuyển động vật có vận tốc 2,5 m/s. Tính gia tốc của vật (đơn vịm/s2) tại thời
điểm vận tốc đạt giá trịlớn nhất trong π (s) đầu tiên.
KQ:
Câu 7
Khi nghiên cứu dịch sốt xuất huyết ởmột địa phương, các chuyên gia y tếước
tính rằng tại ngày thứm có F(m) người mắc bệnh (sau khi đã làm tròn đến chữsốhàng
đơn vị). Biết rằng tốc độlan truyền bệnh là F '(m) =
150
2m + 1 và ngày đầu tiên (m = 0)
người ta phát hiện ra 50 bệnh nhân. Hãy xác định sốngười mắc bệnh ởngày thứ10.
KQ:
Câu 8
Một gia đình sản xuất chiếu cói ởNga Sơn mỗi ngày sản xuất được x chiếc
chiếu (0 ≤x ≤20). Chi phí biên đểsản xuất x chiếc chiếu (tính bằng nghìn đồng) cho
bởi hàm sốsau C'(x) = 3x2 -4x + 10. Biết rằng chi phí cốđịnh ban đầu đểsản xuất là
500 nghìn đồng. Giảsửgia đình này bán hết chiếu mỗi ngày với giá 270 nghìn đồng/chiếc
chiếu. Tính lợi nhuận tối đa theo đơn vịnghìn đồng mà gia đình đó thu được?
KQ:
Câu 9
Một hồnước bịô nhiễm được xửlí bằng một chất diệt khuẩn. Tốc độphát
triển của sốlượng vi khuẩn sống sót được mô hình bởi B'(t) = -
3 000
(1 + 0,2t)2, t ≥0 với B(t)
là sốlượng vi khuẩn trên mỗi ml nước và t là sốngày tính từkhi hồnước được xửlí. Biết
sốlượng vi khuẩn ban đầu là 10 000 con/ml nước. Sửdụng mô hình này xác định lượng vi
khuẩn sau 5 ngày.
Cho biết
Z
(ax + b)n dx = 1
a
(ax + b)n+1
n + 1
+ C.
KQ:
Câu 10
Người ta thay nước mới cho một bểbơi có dạng hình hộp chữnhật có độsâu là
h1 = 280 cm. Giảsửh(t) là chiều cao (tính bằng cm) của mực nước bơm được tại thời điểm
t giây, biết rằng tốc độtăng của chiều cao mực nước tại giây thứt là h'(t) =
1
500
3√t + 3 + 3
và lúc đầu hồbơi không có nước. Hỏi sau bao nhiêu giây thì nước bơm được 3
4 độsâu của
hồbơi? (làm tròn kết quảđến hàng đơn vị).
Cho biết
Z
(ax + b)ndx = 1
a
(ax + b)n+1
n + 1
+ C.
KQ:
Câu 11
Trong một dịch cúm, tốc độtăng sốtrường hợp mắc bệnh của một thành phố
được ước lượng bởi ˙N(t
```

### Nguồn: `Vận dụng cao.pdf` (page_68) — `[VDC Score: 23.5]`
```text
CHƯƠNG I. XÁC SUẤT - THỰC TẾ- THỐNG KÊ - RỜI RẠC
Teacher2kkk | Học toán cùng GenZ
Câu 222. Nhà bác An được mô tảnhư hình vẽ
Trong đó phần thân nhà là hình hộp chữnhật ABCD.EFGH. Ngôi nhà được lợp ngói hai mái là
hai hình chữnhật PEHQ và PFGQ, biết tam giác EFP là tam giác cân tại P. Gọi T là trung điểm
của cạnh DC. Các kích thước của nhà lần lượt là AB = 6 m, AE = 5 m, AD = 8 m, QT = 7 m. Xét
trục tọa độOxyz sao cho gốc tọa độlà điểm O thuộc đoạn AD sao cho OA = 2 m và các trục tọa
độtương ứng là các trục Ox, Oy, Oz. Khi đó,
A A(2;0;0).
B -→
AC = (6;6;0).
C Bác An muốn lắp một chiếc đèn lồng tại vịtrí trung điểm của FG và đầu nguồn đặt tại vịtrí
O. Bác ấy thiết kếđường dây điện nối từO đến K sau đó nối đến chiếc đèn lồng. Độdài đoạn
dây điện nối tối thiểu bằng 5+2
√
10 m.
D Mái nhà bác An được lợp bằng ngói đất nung Đất Việt, giá tiền mỗi viên ngói là 11.000 đồng
và đểlợp được 1 m2 diện tích mái cần 22 viên ngói. Sốtiền cần bỏra đểmua ngói lợp mái
nhà là 13.960.000 đồng (không kểhao phí do việc cắt ghép các viên ngói, kết quảlàm tròn đến
hàng nghìn).
Câu 223. Mỗi tuần, một cửa hàng bán điện thoại di động trung bình bán được 1000 điện thoại A
với giá 14 triệu đồng một cái. Biết rằng, nếu cứgiảm giá 500 nghìn đồng/cái, sốlượng điện thoại A
bán ra sẽtăng thêm khoảng 100 cái mỗi tuần. Biết rằng nếu bán x cái điện thoại A thì giá mỗi cái
là p(x) (triệu đồng) và hàm chi phí hằng tuần là C(x) = 12000-3x (triệu đồng). Đểlợi nhuận là lớn
nhất, cửa hàng nên bán mỗi cái điện thoại A với giá bao nhiêu (triệu đồng)?
Câu 224. Có 10 cái hộp khác nhau được đánh sốtừ1 đến 10 và 10 viên bi giống nhau. Gọi T là số
cách sắp xếp 10 viên bi vào 10 hộp (mỗi hộp không nhất thiết có bi) sao cho tổng sốviên bi trong
các hộp số1, 2, 3 là sốchẵn, còn tổng các viên bi trong các hộp 8, 9, 10 là sốlẻ. Giá trịcủa
T
100
bằng bao nhiêu?
BIÊN SOẠN: TRƯƠNG CÔNG ĐẠT
Tuyển tập VD - VDC trong các đềthi thửTHPTQG | 66
H
Ọ
C
T
O
Á
N
C
Ù
N
G
G
E
N
Z
+
-
×
÷
N
N∗
Z
Q
I
R
C
R
P̸
=
log
ln
∈
/∈
∀
∄
∃
∅
∨
∧
⊄
⊂
≡
≠
=
>
<
≥
≤
√
lim
sin
cos
tan
cot
⊥
∥
Ak
n
Ck
n
α
β
γ
δ
λ
π
ϕ
φ
ex
arcsin
arccos
arctan
±∞
∪
∩
y = f(x)
⇔
⇒
≈
|
µ
ω
τ
i2 = -1
P (A|B)
0
1
2
3
4
5
6
7
8
9
a2 +b2 = c2
Pn = n!
T2
K
EACHER
```

### Nguồn: `Toán thực tế.pdf` (page_135) — `[VDC Score: 25.0]`
```text
Chuyên đềtoán thực tế
Nhóm Ba Đưòng Đồng Quy – 0889 971 004
134
TOÁN 12
TOÁN 12
TOÁN 12
b
Nhiệt độmiếng thịt tính từthời điểm được lấy khỏi ngăn đá là T(t) = 7e-0,35t -11
(◦C).
c
Tính từlúc lấy thịt ra khỏi ngăn đá, cần 3,44 giờđểmiếng thịt nướng được rã đông
(làm tròn kết quảđến hàng phần trăm của giờ).
d
Tính từlúc lấy thịt ra khỏi ngăn đá, nhiệt độcủa miếng thịt vào khoảng 0◦C sau
36 phút (làm tròn kết quảđến hàng đơn vịcủa phút).
Câu 10
Tại một khu di tích vào ngày lễhội hàng năm, tốc độthay đổi lượng khách
tham quan được biểu diễn bằng hàm sốQ'(t) = 4t3 -72t2 + 288t, trong đó t tính bằng giờ
(0 ≤t ≤13), Q'(t) tính bằng khách/giờ(Nguồn: R. Larson and B. Edwards, Calculus 10e,
Cengage). Sau 2 giờđã có 500 người có mặt.
a
Lượng khách tham quan được biểu diễn bởi hàm sốQ(t) = t4 -24t3 + 144t2.
b
Sau 5 giờlượng khách tham quan là 1325 người.
c
Lượng khách tham quan lớn nhất là 1296 người.
d
Tốc độthay đổi lượng khách tham quan lớn nhất tại thời điểm t = 6.
Câu 11
Giảsửrằng khi được t năm tuổi, một máy công nghiệp A tạo ra doanh thu với
tốc độR'(t) = 588 -3t2 (triệu đồng/năm), thời điểm t = 0 tính từlúc máy A bắt đầu hoạt
động. Biết rằng chi phí biên cho vận hành và bảo trì là C'(t) = 48+12t2 (triệu đồng/năm),
ởđây C(t) là chi phí vận hành và bảo trì của máy A khi đó được t năm tuổi.
a
Doanh thu sau 10 năm của máy A là
Z 10
0
 588 -3t2 dt (triệu đồng).
b
Tổng chi phí vận hành và bảo trì của máy A trong 6 năm là 1 152 (triệu đồng).
c
Tuổi thọhữu ích của một máy là sốnăm T trước khi lợi nhuận (bằng doanh thu
trừchi phí) mà nó tạo ra bắt đầu giảm. Tuổi thọhữu ích của máy A này là 8 năm.
d
Lợi nhuận do máy A tạo ra trong suốt thời gian tuổi thọhữu ích của nó là 2 180
(triệu đồng).
Câu 12
Một bồn chứa nước đang chứa 200 lít nước. Người ta bắt đầu bơm nước vào
bồn qua một đường ống. Tại thời điểm t (phút), tốc độdòng chảy của nước vào bồn được
xác định bởi hàm sốv(t) = 6t2 + 8t (lít/phút). Gọi V (t) là thểtích nước có trong bồn tại
thời điểm t.
a
Tốc độdòng chảy của nước vào bồn tại thời điểm t = 5 (phút) là 190 (lít/phút).
b
Tốc độdòng chảy tăng theo thời gian.
c
Hàm sốthểtích V (t) là một nguyên hàm của hàm tốc độdòng chảy v(t) và có dạng
tổng quát là V (t) = 6t3 + 
```

## Chủ đề VDC: `dang_quy_hoach_tuyen_tinh`
### Nguồn: `Tổng ôn.pdf` (page_57) — `[VDC Score: 17.0]`
```text
» Trang 57 
 
1. Bài toán tối ưu (Quy hoạch tuyến tính). 
▶ Bài toán: 
Tìm giá trị lớn nhất, nhỏ nhất của biểu thức 
,
T x y
ax
by
=
+
 với 
;x y nghiệm 
đúng một hệ bất phương trình bậc nhất hai ẩn cho trước. 
≫ Bước ⑴: Xác định miền nghiệm của hệ bất phương trình đã cho. Kết quả thường 
được miền nghiệm S là đa giác. 
≫ Bước ⑵: Tính giá trị của F tương ứng với 
;x y là tọa độ của các đỉnh của đa giác. 
≫ Bước ⑶: Kết luận: 
 Giá trị lớn nhất của F là số lớn nhất trong các giá trị tìm được. 
 Giá trị nhỏ nhất của F là số nhỏ nhất trong các giá trị tìm được. 
2. Luyện tập 
» Câu 1. Một hộ nông dân dự định trồng đậu và cà trên diện tích 8 ha. Nếu trồng đậu thì cần 
20 công và thu 3 triệu đồng trên diện tích mỗi ha, nếu trồng cà thì cần 30 công và thu 
4 triệu đồng trên diện tích mỗi ha. Số tiền thu về lớn nhất là bao nhiêu triệu đồng? Biết 
rằng tổng số công không quá 180. 
 Lời giải 
} Trả lời: 
 
 
 
 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..............................................................
```

### Nguồn: `Chuyên đề ôn thi tốt nghiệp THPT năm 2026 môn Toán – Nguyễn Tiến Hà.pdf` (page_510) — `[VDC Score: 11.5]`
```text
CHUYÊN ĐỀ ÔN THI TN.THPT MÔN TOÁN 12 NĂM 2026-2027 
CHỦ ĐỀ 22 
 
 
ThS. Nguyễn Tiến Hà – Zalo: 0949.888.993 
 Trang 507 
NGUYỄN TIẾN HÀ
NGUYỄN TIẾN HÀ
lượng loại vi khuẩn B, biết rằng tốc độ tăng trưởng của mỗi loài ở mọi thời điểm là như 
nhau? 
 
Câu 49. Áp suất không khí P theo công thức 
0.ekx
P
P
=
 
mmHg, trong đó x là độ cao, 
0
760
P =
 

mmHg là áp suất không khí so với mực nước biển 
0
x =
, k là hệ số suy giảm. Biết rằng 
ở độ cao 1000 m thì áp suất không khí là 672,71 
mmHg. Biết áp suất không khí ở đỉnh 
S của một ngọn núi là 

g
530,2
mmH
3
. Tính độ cao của ngọn núi đó. 
---------------------------------- 
 
DẠNG 4. TOÁN ỨNG DỤNG HỆ BẤT PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN 
(Câu 49-60) 
 
Câu 50. Bác Quân là chủ một trang trại, bác dự định trồng cà phê và ca cao trên một mảnh đất có 
diện tích 8 ha. Biết rằng, trên mỗi ha, nếu trồng cà phê thì cần 20 ngày công và thu được 9 
triệu đồng, nếu trồng ca cao thì cần 30 ngày công và thu được 12 triệu đồng. Bác Quân xác 
định đầu tư không quá 180 ngày công. Biết rằng, bác Quân cần trồng m ha cà phê và n 
ha ca cao sẽ thu được nhiều tiền nhất. Giá trị 
.
m n bằng bao nhiêu? 
 
Câu 51. Một cửa hàng gạo tháng này cần nhập hai loại gạo là gạo loại I và gạo loại II. Số tiền chi 
cho việc nhập hai loại gạo này không quá 100 triệu đồng. Gạo loại I mua vào với giá 30 
triệu đồng/ tấn, lợi nhuận dự kiến là 2 triệu đồng/tấn. Gạo loại II nhập vào với giá 40 triệu 
đồng/tấn và lợi nhuận dự kiến là 2,5 triệu đồng/tấn. Cửa hàng ước tính doanh số bán ra 
một tháng của hai loại gạo này không quá 3 tấn. Hỏi cửa hàng có thể lãi nhiều nhất là bao 
nhiêu khi kinh doanh hai loại gạo này? 
 
Câu 52. Một nhà máy sản xuất hai loại thức ăn gia súc: loại A và loại B. Để sản xuất 1 tấn thức ăn 
loại A cần 3 tấn nguyên liệu X, 2 tấn nguyên liệu Y và 1 tấn phụ gia. Để sản xuất 1 tấn 
thức ăn loại B cần 2 tấn nguyên liệu X, 4 tấn nguyên liệu Y và 3 tấn phụ gia. Nhà máy có 
tối đa 120 tấn nguyên liệu X, 160 tấn nguyên liệu Y và 80 tấn phụ gia. Biết rằng lợi nhuận 
thu được từ mỗi tấn thức ăn loại A là 20 triệu đồng và từ loại B là 30 triệu đồng. Lợi nhuận 
nhà máy thu được lớn nhất là bao nhiêu? 
 
Câu 53. Bác Hai có một mảnh đất rộng 6 ha. B
```

### Nguồn: `Tổng ôn.pdf` (page_1) — `[VDC Score: 2.0]`
```text
» Trang 1 
Mục Lục 
♻ Chủ đề 01. PHƯƠNG TRÌNH – BẤT PHƯƠNG TRÌNH...............................................Trang 2 
♻ Chủ đề 02. DÃY SỐ – CẤP SỐ...........................................................................................Trang 20 
♻ Chủ đề 03. BÀI TOÁN TIẾT KIỆM...................................................................................Trang 42 
♻ Chủ đề 04. QUY HOẠCH TUYẾN TÍNH.........................................................................Trang 57 
♻ Chủ đề 05. ĐẠI SỐ TỔ HỢP..............................................................................................Trang 74 
♻ Chủ đề 06. HÀM SỐ MŨ – HÀM SỐ LOGARIT...........................................................Trang 91 
♻ Chủ đề 07. GÓC TRONG KHÔNG GIAN (ĐT-ĐT+ĐT-MP)....................................Trang 113 
♻ Chủ đề 08. GÓC NHỊ DIỆN..............................................................................................Trang 130 
♻ Chủ đề 09. KHOẢNG CÁCH...........................................................................................Trang 142 
♻ Chủ đề 10. MÔ HÌNH VECTƠ TRONG KHÔNG GIAN...........................................Trang 170 
♻ Chủ đề 11. MÔ HÌNH ĐƯỜNG THẲNG-MẶT PHẲNG-MẶT CẦU.....................Trang 189 
♻ Chủ đề 12. MÔ HÌNH HÀM SỐ BẬC HAI và BẬC BA..............................................Trang 213 
♻ Chủ đề 13. MÔ HÌNH HÀM SỐ PHÂN THỨC và LƯỢNG GIÁC..........................Trang 235 
♻ Chủ đề 14. ỨNG DỤNG TÍCH PHÂN TRONG THỰC TẾ........................................Trang 252 
♻ Chủ đề 15. ỨNG DỤNG TÍCH PHÂN TRONG CHUYỂN ĐỘNG..........................Trang 271 
♻ Chủ đề 16. ỨNG DỤNG TÍCH PHÂN TÍNH DIỆN TÍCH........................................Trang 291 
♻ Chủ đề 17. ỨNG DỤNG TÍCH PHÂN TÍNH THỂ TÍCH...........................................Trang 311 
♻ Chủ đề 18. XÁC SUẤT.......................................................................................................Trang 334 
♻ Chủ đề 19. Ý NGHĨA CƠ HỌC TRONG ĐẠO HÀM.................................................Trang 383 
♻ Chủ đề 20. CÁC BÀI TOÁN KHÁC................................................................................Trang 397
```

## Chủ đề VDC: `dang_thuc_te_toc_do_bien_thien`
### Nguồn: `Chuyên đề ôn thi tốt nghiệp THPT năm 2026 môn Toán – Nguyễn Tiến Hà.pdf` (page_383) — `[VDC Score: 14.0]`
```text
CHUYÊN ĐỀ ÔN THI TN.THPT MÔN TOÁN 12 NĂM 2026-2027 
CHỦ ĐỀ 17 
 
 
ThS. Nguyễn Tiến Hà – Zalo: 0949.888.993 
 Trang 380 
NGUYỄN TIẾN HÀ
NGUYỄN TIẾN HÀ
Câu 125. Công ty Sơn X cần làm những hộp hình trụ có thể tích 5 lít. 
 
 
 
Giả thiết rằng vật liệu và chi phí dùng để sản xuất các mặt của hộp là như nhau. Tính bán 
kính r của đáy hộp để chi phí là bé nhất (đơn vị là cm và làm tròn đến hàng phần trăm). 
 
Câu 126. Một bể chứa nước có mặt đáy và miệng bể đều là hình chữ nhật nằm trên 2 mặt phẳng 
song song với nhau, miệng bể có chiều ngang 15m và chiều dài 24m, đáy bể có kích thước 
 
15
12
m
m. Độ sâu của bể nước (tính từ miệng đến đáy) là 6m, mặt cắt vuông góc với 
chiều ngang của bể có hình dạng là hình thang cân (như hình vẽ). 
 
 
 
Lúc đầu bể không có nước, người ta sử dụng một máy bơm để bơm nước vào bể với tốc độ 
3
50m trong một phút. Vào lúc mực nước đúng 5m thì tốc độ dâng lên của mực nước trong 
bể là bao nhiêu m trên một phút (kết quả làm tròn đến hàng phần trăm)? 
 
 
```

### Nguồn: `Chuyên đề ôn thi tốt nghiệp THPT năm 2026 môn Toán – Nguyễn Tiến Hà.pdf` (page_604) — `[VDC Score: 5.5]`
```text
ĐỀ THI THỬ TN.THPT MÔN TOÁN 12 NĂM 2026-2027 
ĐỀ THI THỬ SỐ 19 
 
 
ThS. Nguyễn Tiến Hà – Zalo: 0949.888.993 
 Trang 601 
NGUYỄN TIẾN HÀ
NGUYỄN TIẾN HÀ
Lúc đầu bể không có nước, người ta sử dụng một máy bơm để bơm nước vào bể với tốc độ 
3
50m trong một phút. Vào lúc mực nước đúng 5m thì tốc độ dâng lên của mực nước trong 
bể là bao nhiêu m trên một phút? 
 
Câu 21: Một mô hình khối tròn xoay có trục là đường thẳng MN, khi ta cắt khối tròn xoay đó bởi 
một mặt phẳng đi qua trục của khối tròn xoay thì ta được mặt cắt có dạng như hình vẽ 
dưới đây. 
 
 
 
 
Biết 
20cm
MN =
, ABCD là hình chữ nhật có 
16cm,
32cm
AB
AD
=
=
, hai cung APD 
và BQC là một phần của các đường parabol với đỉnh lần lượt là 
,
P Q và 
8 cm
PQ =
. 
Tính thể tích của mô hình đó theo đơn vị 
3
cm. 
 
 
```

---

# KHU VỰC II: NGỮ LIỆU NỀN TẢNG & VẬN DỤNG (DÙNG CHO PHẦN I - TRẮC NGHIỆM 12 CÂU)

## Chủ đề: `dang_ham_so_don_dieu`
### Nguồn: `Vận dụng cao.pdf` (page_328)
```text
CHƯƠNG III. HÀM SỐ
Teacher2kkk | Học toán cùng GenZ
Hàm sốđơn điệu
Định nghĩa.
Cho hàm sốy = f(x) có tập xác định D, với K ⊂D là khoảng, đoạn hoặc nửa khoảng.
- Hàm sốy = f(x) gọi là đồng biến (tăng) trên K, nếu ∀x1,x2 ∈K, x1 < x2 ⇒f (x1) < f (x2)
- Hàm sốy = f(x) gọi là nghịch biến (giảm) trên K, nếu ∀x1,x2 ∈K, x1 < x2 ⇒f (x1) > f (x2)
Một hàm sốđồng biến hoặc nghịch biến trên K thì ta nói hàm sốđó đơn điệu trên K.
Tính đơn điệu và dấu của đạo hàm.
Định lí 1.
Giảsửhàm sốf có đạo hàm trên khoảng K. Khi đó,
- Nếu f đồng biến trên K thì f'(x) ≥0 với mọi x ∈K.
- Nếu f nghịch biến trên K thì f'(x) ≤0 với mọi x ∈K.
Định lí 2.
Giảsửhàm sốf có đạo hàm trên khoảng K. Khi đó,
- Nếu f'(x) > 0 với mọi x ∈K thì f đồng biến (tăng) trên K.
- Nếu f'(x) < 0 với mọi x ∈K thì f nghịch biến (giảm) trên K.
- Nếu f'(x) = 0 với mọi x ∈K thì f có giá trịkhông đổi trên K.
Chú ý: Nếu f'(x) ≥0 với mọi x ∈K (hoặc f'(x) ≤0 với mọi x ∈K) và phương trình f'(x) = 0
chỉcó một sốhữu hạn nghiệm trên K thì f đồng biến (hoặc nghịch biến) trên K.
Định lí ”Ghép trục”
Hàm sốf (u(x)) biến thiên cùng chiều với u(x) trong những khoảng mà f(u) đồng biến, ngược
chiều với u(x) trong những khoảng mà f(u) nghịch biến.
Bài tập 1. Xét tính đơn điệu của các hàm sốsau:
A f(x) = x3 -3x.
B f(x) = x-1
x+1.
C f(x) =
q
4x2 +1-2x.
D f(x) = 3x+|x|
x
.
Bài tập 2. Cho hàm sốy = f (x) có bảng biến thiên như sau:
x
f(x)
-∞
-4
0
+∞
-∞
-∞
1
-1
-1
+∞
+∞
Xét tính đơn điệu của hàm sốg(x) = f

f2(x)

.
BIÊN SOẠN: TRƯƠNG CÔNG ĐẠT
Tuyển tập V
```

### Nguồn: `Chuyên đề ôn thi tốt nghiệp THPT năm 2026 môn Toán – Nguyễn Tiến Hà.pdf` (page_192)
```text
CHUYÊN ĐỀ ÔN THI TN.THPT MÔN TOÁN 12 NĂM 2026-2027 
CHỦ ĐỀ 12 
 
 
ThS. Nguyễn Tiến Hà – Zalo: 0949.888.993 
 Trang 189 
NGUYỄN TIẾN HÀ
NGUYỄN TIẾN HÀ
Câu 20: (ĐTK - BGD 2019) Cho hàm số 

=
y
f x có đồ thị như hình vẽ bên. Hàm số đã cho đồng biến 
trên khoảng nào dưới đây? 
 
A. 
0;1. 
B. 
- vô cùng -
;
1. 
C. 
-1;1. 
D. 
-1;0. 
Câu 21: (ĐỀ TN.THPT 2017 - MĐ104) Cho hàm số 

=
y
f x có bảng xét dấu đạo hàm như sau 
 
Mệnh đề nào dưới đây đúng? 
A. Hàm số đồng biến trên khoảng 
-2;0. 
B. Hàm số đồng biến trên khoảng 
- vô cùng;0. 
C. Hàm số nghịch biến trên khoảng 
0;2. 
D. Hàm số nghịch biến trên khoảng 

- vô cùng -
;
2. 
Câu 22: (ĐỀ TN.THPT 2019 - MĐ103) Cho hàm số ()
f x có đạo hàm 

'
=
-
2
1
f
x
x x
, "
 Z R 
x
. Số 
điểm cực trị của hàm số đã cho là 
A. 2. 
B. 0. 
C. 1. 
D. 3. 
Câu 23: (ĐỀ TN.THPT 2017 - MĐ104) Hàm số 
+
=
+
2
3
1
x
y
x
 có bao nhiêu điểm cực trị? 
A. 3. 
B. 0. 
C. 2. 
D. 1. 
Câu 24: (ĐỀ TN.THPT 2019 - MĐ104) Cho hàm số ()
f x có đạo hàm 

'
=
+
"
 Z R 
2
1,
f
x
x x
x
. Số 
điểm cực trị của hàm số đã cho là 
A. 0. 
B. 1. 
C. 2. 
D. 3. 
Câu 25: (ĐTK - BGD 2019) Cho hàm số ()
f x có đạo hàm 

'
=
-
+
"
 Z 
3
1
2
,
f
x
x x
x
x
R. Số điểm 
cực trị của hàm số đã cho là 
A. 3. 
B. 2. 
C. 5. 
D. 1. 
Câu 26: (ĐỀ TN.THPT 2017 - MĐ101) Đồ thị của hàm số 
=
-
-
+
3
2
3
9
1
y
x
x
x
 có hai điểm cực trị 
A và B. Điểm nào dưới đây thuộc đường thẳng AB ? 
A. 
(1;0)
P
. 
B. 
-
(0;
1)
M
. 
C. 
-
(1;
10)
N
. 
D. 
-
(1;10)
Q
. 
Câu 27: (ĐỀ TN.THPT 2017 - MĐ102) Cho hàm s
```

## Chủ đề: `dang_ham_so_cuc_tri`
### Nguồn: `Vận dụng cao.pdf` (page_417)
```text
CHƯƠNG III. HÀM SỐ
Teacher2kkk | Học toán cùng GenZ
Câu 443. Cho hàm sốy = f(x) có đạo hàm liên tục trên R. Biết f(-7) < 0 và đồthịf'(x) như
hình vẽ.
Hàm sốg(x) =
6f

-x4 +2x2 -7

-4x6 +12x2 có tối đa bao nhiêu điểm cực trị?
A 5.
B 9.
C 7.
D 3.
Câu 444. Cho hàm sốy = f(x) có đồthịnhư hình vẽ.
Có tất cảbao nhiêu giá trịnguyên của tham sốm đểphương trình f
√
x+4+
√
4-x-m

+2 = 0
có nghiệm trong khoảng (-4;4)?
Câu 445. Có bao nhiêu giá trịnguyên m đểphương trình (x-1)log

e-x +m+2023

= x -2 có
hai nghiệm thực phân biệt?
A 2023.
B 2024.
C 10.
D 11.
Câu 446. Xét các sốthực x, y thỏa mãn 2x2+y2+1 ≤

x2 +y2 -2x+2

4x. Giá trịlớn nhất của biểu
thức P =
8x+4
2x-y +1 bằng
BIÊN SOẠN: TRƯƠNG CÔNG ĐẠT
Tuyển tập VD - VDC trong các đềthi thửTHPTQG | 1179
H
Ọ
C
T
O
Á
N
C
Ù
N
G
G
E
N
Z
+
-
×
÷
N
N∗
Z
Q
I
R
C
R
P̸
=
log
ln
∈
/∈
∀
∄
∃
∅
∨
∧
⊄
⊂
≡
≠
=
>
<
≥
≤
√
lim
sin
cos
tan
cot
⊥
∥
Ak
n
Ck
n
α
β
γ
δ
λ
π
ϕ
φ
ex
arcsin
arccos
arctan
±∞
∪
∩
y = f(x)
⇔
⇒
≈
|
µ
ω
τ
i2 = -1
P (A|B)
0
1
2
3
4
5
6
7
8
9
a2 +b2 = c2
Pn = n!
T2
K
EACHER
```

### Nguồn: `Chuyên đề ôn thi tốt nghiệp THPT năm 2026 môn Toán – Nguyễn Tiến Hà.pdf` (page_218)
```text
CHUYÊN ĐỀ ÔN THI TN.THPT MÔN TOÁN 12 NĂM 2026-2027 
CHỦ ĐỀ 13 
 
 
ThS. Nguyễn Tiến Hà – Zalo: 0949.888.993 
 Trang 215 
NGUYỄN TIẾN HÀ
NGUYỄN TIẾN HÀ
Câu 33: Cho hàm số 
+
+
=
+
2
ax
bx
c
y
mx
n
 có đồ thị như hình vẽ sau: 
Xét tính đúng sai các khẳng định sau: 
a) Hàm số đã cho nghịch biến trên khoảng 
-2;0. 
b) Đồ thị của hàm số đã cho có tiệm cận xiên 
=
+1
y
x
. 
c) Gọi,
A B là hai điểm cực trị của hàm số đã cho, diện tích 
của tam giác OAB bằng 8. 
d) Một trục đối xứng của đồ thị đã cho là 

pi
=
+
3
1 tan
.
8
y
x
 
Câu 34: Cho hàm số ()=
-sin2
f x
x
x. Xét tính đúng sai các khẳng định sau: 
a) 

pi
pi
pi
pi

-
=-
=

,
2
2
f
f
. 
b) 

'
=
-
1
cos2
f
x
x. 
c) Phương trình 

'
=0
f
x
 trên đoạn 
[pipi]

[-]

;
2
 có tập nghiệm là 
pipi
pi

{
{
{
{
=-

{
{
{
{

5
;
;
6 6
6
T
. 
d) Tổng giá trị lớn nhất và nhỏ nhất của hàm số trên đoạn 
[pipi]

[-]

;
2
 bằng pi+
3
3
2. 
Câu 35: Cho hàm số 
-
+
=
-
2
2
2
1
x
x
y
x
. Xét tính đúng sai các khẳng định sau: 
a) Hàm số đã cho được viết lại 
=
-
+
-
1
1
1
y
x
x
. 
b) Phương trình '=0
y
 có hai nghiệm 
=
1
2
x
 và 
=
2
0
x
. 
c) Hàm số đã cho nghịch biến trên khoảng 
0;2. 
d) Đồ thị của hàm số là hình vẽ dưới đây:
```

## Chủ đề: `dang_ham_so_gtln_gtnn`
### Nguồn: `Chuyên đề ôn thi tốt nghiệp THPT năm 2026 môn Toán – Nguyễn Tiến Hà.pdf` (page_343)
```text
CHUYÊN ĐỀ ÔN THI TN.THPT MÔN TOÁN 12 NĂM 2026-2027 
CHỦ ĐỀ 16 
 
 
ThS. Nguyễn Tiến Hà – Zalo: 0949.888.993 
 Trang 340 
NGUYỄN TIẾN HÀ
NGUYỄN TIẾN HÀ
0
:
20
x
d
y
t
z
{
=
{=
{=
{
. Vì địa hình phức tạp, người ta chọn điểm 

15;10;15
A
 để làm điểm trung 
chuyển dầu từ mặt đất đến đường ống này. 
Xét tính đúng sai của các mệnh đề sau: 
a) Đường thẳng d nằm trên mặt phẳng 
Oyz. 
b) Điểm đối xứng với A qua mặt phẳng 
Oxy có tọa độ 

15;
10;15
A'-
-
. 
c) Do thực tế công việc, người ta cần xác định vị trí điểm 
0;;20
B
b
 thuộc đường ống và vị 
trí điểm 

;;0
C m n
 thuộc mặt đất sao cho tổng độ dài các đoạn đường 
,
,
AB BC AC nhỏ 
nhất. Ta có m
n
b
+
+
= 200
7. 
d) Giá trị nhỏ nhất của tổng độ dài các đoạn đường 
,
,
AB BC AC làm tròn đến hàng phần 
chục bằng 45,5 m. 
Câu 99: Một căn phòng có dạng là một hình hộp chữ nhật, được mô hình hóa và gắn hệ trục tọa độ 
Oxyz như hình vẽ sau: 
 
Người ta thiết kế một công tắc điện tại điểm 

0;2;2
M
 và một bóng đèn để chiếu sáng căn 
phòng tại điểm P là trung điểm của A B
'
', biết 

6;5;4
C '
. 
Xét tính đúng sai của các mệnh đề sau: 
a) Điểm M thuộc mặt phẳng 
ADD'. 
b) Tọa độ điểm P là 
3;0;5
P
. 
c) Mặt phẳng 
PCD' có một vec tơ pháp tuyến 

10;
6;15
n =
-

. 
d)N là điểm di dộng trên đoạn 
'
AA. Dây cấp điện cho bóng đèn được đấu từ công tắc điện 
tại vị trí M kéo đến điểm N rồi nối đến bóng đèn. Độ dài dây cấp điện tối thiểu bằng 29 
Câu 100: Trong không gian với hệ tọa độ 
,
Oxyz mỗi đơn vị trên trục có độ dài 10
.
km Một trạm 
```

### Nguồn: `THPT Nguyễn Thị DIệu.pdf` (page_2)
```text
Mã đề 1001 
Trang 2/4 
Câu 9. Cho hình hộp 
.
ABCDA B C D
''''. Chọn đẳng thức sai? 
 
 
A. AB
AC
BC
+
=
. 
B. BC
BA
BD
+
=
. C. AB
AD
AA
AC
'
'
+
+
=
. D. AD
D C
AC
'
'
+
=
. 
Câu 10. Trong không gian Oxyz, mặt phẳng ()
 alpha đi qua điểm 

;;
A -1 2 4 và nhận vectơ 

;
;
n =
-
1
2 3 làm 
vectơ pháp tuyến có phương trình là 
 
A. x
y
z
-+
+
-
=
2
4
7
0. 
B. x
y
z
-+
+
+
=
2
4
7
0. 
C. x
y
z
-
+
-
=
2
3
7
0. D. x
y
z
-
+
+
=
2
3
7
0. 
Câu 11. Trong không gian Oxyz, cho đường thẳng 
: x
y
z
d
-
-
=
=
-
4
3
1
2
3
. Hỏi trong các vectơ sau, vectơ 
nào là vectơ chỉ phương của d ? 
 
A. 

;
;
u =
-
-
3
0
4
3. 
B. 

;;
u = -
4
1 2 3. 
C. 

;;
u =
1
1 2 3. 
D. 

;;
u =
2
0 4 3. 
Câu 12. Cho cấp số cộng 
n
u
 với số hạng đầu tiên là u =
1
4 và công sai d = 8. Số hạng u20 của cấp số 
cộng đã cho bằng 
 
A. 156. 
B. 165. 
C. 245. 
D. 12. 
PHẦN II. Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng 
hoặc sai. 
Câu 1. Một vật chuyển động với vận tốc ()
 
 
t
t
t
v t
t
{
+
-
= {
>
{
2
3
2
1
0
2
15
2
neáu
neáu
 (đơn vị m/s) 
 
a) Vận tốc của vật tại thời điểm t = 3 giây bằng 

m/s
32
. 
 
b) Gia tốc của vật tại thời điểm t = 3 là 
2
m/s
0
 
 
c) Quãng đường vật đi được trong 1 giây đầu tiên được xác định bởi công thức 
()d
s
v t
t
= tích phân 
1
1
0
. 
 
d) Quãng đường vật đi được trong khoảng thời gian 4 giây đầu tiên bằng s =
2
76 mét. 
Câu 2. Trong không gian Oxyz (đơn vị độ dài trên mỗi trục là 1 kilomet), một trạm phát sóng điện thoại 
của nh
```

## Chủ đề: `dang_ham_so_do_thi_bbt`
### Nguồn: `Tổng ôn.pdf` (page_219)
```text
» Trang 219 
» Câu 6. Một phần đường chạy của tàu lượn siêu tốc khi gắn hệ trục tọa độ Oxy được mô phỏng 
ở hình 2. Biết đường chạy của nó có dạng đồ thị hàm số bậc ba 

3
2
=
=
+
+
+
y
f x
ax
bx
cx
d (0
90
<=
<=
x
); tàu lượn xuất phát từ điểm A đồng thời đi qua 
các điểm B, C, D (như hình vẽ). Coi trục Ox là mặt đất, đơn vị trên mỗi trục tọa độ tính 
bằng mét. 
 
Khi đó: 
 
Mệnh đề 
Đúng 
Sai 
(a) Phương trình ()
30
=
f x
 có 3 nghiệm phân biệt 
0
50
80
=
=
=
,
,
x
x
x
. 
 
 
(b) Ta có ()

30
50
80
+
=
-
-
f x
ax x
x
 với a là hằng số thực. 
 
 
(c) Đạo hàm 

2
1
13
8
500
75
3
'
=-
+
-
f
x
x
x
. 
 
 
(d) Vị trí cao nhất của tàu lượn bằng 39,9 m (làm tròn kết quả đến hàng phần 
mười). 
 
 
 Lời giải 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................
```

### Nguồn: `Chuyên đề ôn thi tốt nghiệp THPT năm 2026 môn Toán – Nguyễn Tiến Hà.pdf` (page_205)
```text
CHUYÊN ĐỀ ÔN THI TN.THPT MÔN TOÁN 12 NĂM 2026-2027 
CHỦ ĐỀ 12 
 
 
ThS. Nguyễn Tiến Hà – Zalo: 0949.888.993 
 Trang 202 
NGUYỄN TIẾN HÀ
NGUYỄN TIẾN HÀ
 
A. Phương trình '=0
y
 có đúng ba nghiệm thực phân biệt. 
B. Phương trình '=0
y
 có đúng hai nghiệm thực phân biệt. 
C. Phương trình '=0
y
 có đúng một nghiệm thực. 
D. Phương trình '=0
y
 vô nghiệm trên tập số thực. 
Câu 99: (ĐỀ TN.THPT 2021 - MĐ104) Đồ thị hàm số 
=-
+
-
3
2
2
3
5
y
x
x
cắt trục tung tại điểm có 
tung độ bằng 
A. -5. 
B. 0. 
C. -1. 
D. 2. 
Câu 100: 
(ĐỀ TN.THPT 2021 - MĐ103) Đồ thị hàm số 
=-
+
-
3
2
2
1
y
x
x
 cắt trục tung tại điểm 
có tung độ bằng 
A. 3. 
B. 1. 
C. -1. 
D. 0. 
Câu 101: 
(ĐỀ TN.THPT 2021 - MĐ102) Đồ thị của hàm số 
=-
-
+
4
2
2
3
y
x
x
 cắt trục tung tại 
điểm có tung độ bằng 
A. 1. 
B. 0. 
C. 2. 
D. 3. 
Câu 102: 
(ĐỀ TN.THPT 2021 - MĐ101) Đồ thị của hàm số 
=-
+
-
4
2
4
3
y
x
x
 cắt trục tung tại 
điểm có tung độ bằng 
A. 0. 
B. 3. 
C. 1. 
D. -3. 
Câu 103: 
(ĐỀ TN.THPT 2020 - MĐ103) Số giao điểm của đồ thị hàm số 
=-
+
3
3
y
x
x với trục 
hoành là 
A. 2. 
B. 0. 
C. 3. 
D. 1. 
Câu 104: 
(ĐỀ TN.THPT 2017 - MĐ103) Cho hàm số 

=
-
+
2
2
1
y
x
x
 có đồ thị ()
C. Mệnh đề 
nào dưới đây đúng? 
A. ()
C cắt trục hoành tại hai điểm. 
B. ()
C cắt trục hoành tại một điểm. 
C. ()
C không cắt trục hoành. 
D. ()
C cắt trục hoành tại ba điểm. 
Câu 105: 
(ĐỀ TN.THPT 2020 - MĐ104) Số giao điểm của đồ thị hàm số 
=-
+
3
5
y
x
x với trục 
hoành là 
A. 3. 
B. 2. 
C. 0. 
D. 1. 
Câu 106: 
(ĐỀ TN.THPT 2020 - MĐ
```

## Chủ đề: `dang_mu_logarit_phuong_trinh_bpt`
### Nguồn: `Chuyên đề ôn thi tốt nghiệp THPT năm 2026 môn Toán – Nguyễn Tiến Hà.pdf` (page_239)
```text
CHUYÊN ĐỀ ÔN THI TN.THPT MÔN TOÁN 12 NĂM 2026-2027 
CHỦ ĐỀ 13 
 
 
ThS. Nguyễn Tiến Hà – Zalo: 0949.888.993 
 Trang 236 
NGUYỄN TIẾN HÀ
NGUYỄN TIẾN HÀ
Câu 106. Cho hàm số ()

=
+
2
log
4
f x
x
. Xét tính đúng sai các mệnh đề sau: 
a) Tập xác định của hàm số đã cho chứa đúng 4 số nguyên âm. 
b) Phương trình ()

=
+
-
2
2
log
2
16
f x
x
x
có nghiệm duy nhất là 
=4
x
. 
c) Hàm số ()

=-
+
2
.ln1024
g x
x
f x
 đạt giá trị nhỏ nhất tại 
=1
x
. 
d) Đường thẳng 
=
-1
y
x
 cắt đồ thị hàm số 

=
y
f x tại duy nhất một điểm. 
Câu 107. Cho hàm số ()=
-
2
ln
2
f x
x
x, 

"
 Z 
+ vô cùng 
0,
x
. Xét tính đúng sai các mệnh đề sau: 
a) Tổng giá trị lớn nhất và nhỏ nhất của hàm số 

2
1;e
 là -
-
5
ln2
2
. 
b) Hàm số 

=
y
f x có hai điểm cực trị. 
c) Hàm số luôn đồng biến trên tập xác định. 
d) ()

=-
=
-
2
4
1
2;
2
2
f
f e
e. 
Câu 108. Cho hàm số ()

=
-
+
2
1
2
log
5
4
f x
x
x
. Xét tính đúng sai các mệnh đề sau: 
a) Hàm số 

=
y
f x có tập xác định 

]
[
=- vô cùng 
 
+ vô cùng 
]

[
;1
4;
D
. 
b) Hàm số 

=
y
f x có đạo hàm 

-
'
=
-
+
2
5
2
5
4 ln2
x
f
x
x
x
. 
c) Hàm số 

=
y
f x đồng biến trên khoảng 

- vô cùng 

5
; 2. 
d) Bất phương trình ()>0
f x
 có đúng 4 nghiệm nguyên. 
Câu 109. Cho hàm số ()=
-
ln
2
x
f x
x
. Xét tính đúng sai các mệnh đề sau: 
a) Tập xác định của hàm là 

=
+ vô cùng 
0;
D
. 
b) ()

=-
=-
1
1
;
2
2
e
f
f e
. 
c) Nghiệm của phương trình 

'
=0
f
x
 trên đoạ[n]

1;e là 
=2
x
. 
d) Giá trị lớn nhất của hàm số ()
f x trên đoạ[n]

1;e bằng -1
2. 
Câu 110. Cho hàm
```

### Nguồn: `Vận dụng cao.pdf` (page_447)
```text
CHƯƠNG III. HÀM SỐ
Teacher2kkk | Học toán cùng GenZ
Câu 622. Cho hàm sốy = f(x) có đạo hàm liên tục trên R, f(0) = 3 và đồthịf'(x) như hình vẽ.
Có bao nhiêu giá trịnguyên m đểhàm sốg(x) =
2f(x)+x2 -2mx+2m
 đồng biến trên (0;1)?
Câu 623. Có bao nhiêu cặp sốnguyên (x;y) thoảmãn
x2 +y2 +7x
x
> log2
x2 +y2
x
+
 x2 +y2
x
!log2 3
Câu 624. Gọi S là tập các sốnguyên dương a đểbất phương trình 6x + 2a+2 < 4.3x + 2x+a có ít
nhất 1 và không quá 10 nghiệm nguyên. Tổng các phần tửcủa S bằng
A 204.
B 201.
C 205.
D 208.
Câu 625. Cho a, b, c là các sốthực thoảmãn điều kiện a > 1, b > 0, c > 0 và bất phương trình
ax2 (b+4c)2x+3 ≥1 có tập nghiệm là R. Biết rằng biểu thức P = 16a
3 + 1
b + 1
c đạt giá trịnhỏnhất
tại a = m, b = n, c = p. Khi đó, tổng m+n+p bằng
Câu 626. Có bao nhiêu giá trịnguyên m ∈(-2023;2023) đểhàm sốy =
ln

x2 +x+m

+x
 đồng
biến trên khoảng (-1;3)?
Câu 627. Xét các sốthực dương a, b thoảmãn log2 (a+b) = log3

a2 +b2
. Khi đó a3 + b3 có thể
nhận nhiều nhất bao nhiêu giá trịnguyên?
Câu 628. Có bao nhiêu sốnguyên m ∈(-2023;2023) đểhàm sốy = x2 -2m|x-m+6| + 1 có ba
điểm cực trị?
BIÊN SOẠN: TRƯƠNG CÔNG ĐẠT
Tuyển tập VD - VDC trong các đềthi thửTHPTQG | 1209
H
Ọ
C
T
O
Á
N
C
Ù
N
G
G
E
N
Z
+
-
×
÷
N
N∗
Z
Q
I
R
C
R
P̸
=
log
ln
∈
/∈
∀
∄
∃
∅
∨
∧
⊄
⊂
≡
≠
=
>
<
≥
≤
√
lim
sin
cos
tan
cot
⊥
∥
Ak
n
Ck
n
α
β
γ
δ
λ
π
ϕ
φ
ex
arcsin
arccos
arctan
±∞
∪
∩
y = f(x)
⇔
⇒
≈
|
µ
ω
τ
i2 = -1
P (A|B)
0
1
2
3
4
5
6
7
8
9
a2 +b2 = c2
Pn = n!
T2
K
EACHER
```

## Chủ đề: `dang_mu_logarit_tham_so`
### Nguồn: `Chuyên đề ôn thi tốt nghiệp THPT năm 2026 môn Toán – Nguyễn Tiến Hà.pdf` (page_58)
```text
CHUYÊN ĐỀ ÔN THI TN.THPT MÔN TOÁN 12 NĂM 2026-2027 
MŨ-LOGARIT 
 
 
ThS. Nguyễn Tiến Hà – Zalo: 0949.888.993 
 Trang 55 
NGUYỄN TIẾN HÀ
NGUYỄN TIẾN HÀ
A. 
8
7
-
. 
B. 1
7. 
C. 4
7. 
D. 
4
21
-
. 
Câu 45: (THPT Lê Văn Hưu) Cho phương trình 

2
3
4
8
2
log
1
2
log
4
log
4
x
x
x
+
+
=
-
+
+
. Tổng các nghiệm của phương trình trên bằng 
A. 4
2 6
+
. 
B. 
4
-. 
C. 4
2 6
-
. 
D. 2
2 3
-
. 
Câu 46: (THPT Cổ Loa – Hà Nội) Tổng tất cả các nghiệm của phương trình 
2019
2018
2019
2018
2
.3
3
.2
6
2
.3
x
x
x
+
=
+
 bằng 
A. 1. 
B. 536. 
C. 4037. 
D. 5. 
Câu 47: (Chuyên Bắc Giang) Số nghiệm của phương trình 

2
0,5
2 log
5
6
1
0
x
x
[x]
-
-
+
+
=

 
A. 1. 
B. 0. 
C. 3. 
D. 2. 
Câu 48: (THPT 
Quảng 
Xương 
- 
Thanh 
Hóa) 
Số nghiệm của phương trình 
2
2
4
log
3
2
12
x
x
x
+
=
-
+
 bằng 
A. 0. 
B. 1. 
C. 2. 
D. 3. 
Câu 49: (THPT Thị Xã Quảng Trị) Phương trình 

3
2
log
4
4
1
log
1
x
x
x
x
-
+
-
=
-
 có tất 
cả bao nhiêu nghiệm thực? 
A. 2. 
B. 1. 
C. 0. 
D. 3. 
Câu 50: (HKI THPT Bình Dương) Số nghiệm của phương trình 
1
1
6
2
3
6
0
x
x
x
+
+
-
-
+
=
 là 
A. 0. 
B. 3. 
C. 2. 
D. 1. 
Câu 51: (THPT Lý Thánh Tông) Bất phương trình

3
3
log
3
1 < log
7
x
x
-
+
 có bao nhiêu 
nghiệm nguyên? 
A. 1. 
B. 2. 
C. 3. 
D. 0. 
Câu 52: (THPT Nông Cống 2 - Thanh Hóa) Tập nghiệm của bất phương trình 
2
3
9
0
x
x
--
<
 
chứa bao nhiêu số nguyên? 
A. 3. 
B. 2. 
C. 0. 
D. 1. 
Câu 53: (THPT Sơn Tây - Hà Nội) Tập nghiệm của bất phương trình 
1
2
2
3
1
log
log
0
1
x
x

-)
<=

(
+

 là 
A. 
)
;
1
3;
[
- vô cùng -

```

### Nguồn: `Chuyên đề ôn thi tốt nghiệp THPT năm 2026 môn Toán – Nguyễn Tiến Hà.pdf` (page_240)
```text
CHUYÊN ĐỀ ÔN THI TN.THPT MÔN TOÁN 12 NĂM 2026-2027 
CHỦ ĐỀ 13 
 
 
ThS. Nguyễn Tiến Hà – Zalo: 0949.888.993 
 Trang 237 
NGUYỄN TIẾN HÀ
NGUYỄN TIẾN HÀ
d) Hàm số đã cho có giá trị cực tiểu bằng 0. 
Câu 112. Cho hàm số ()=
-
+
1
2log.
f x
x
x
x
 Xét tính đúng sai các mệnh đề sau: 
a) Hàm số 

=
y
f x có tập xác định là 
+ vô cùng 
0;
. 
b) Đạo hàm của hàm số ()
f x là 

'
=+
+
2
1
2
1
,
f
x
x
x
 với mọi 

 Z 
+ vô cùng 
0;
.
x
 
c) Hàm số 

=
y
f x luôn thỏa mãn hệ thức 

()=-

1
,
f
f x
x
 với mọi 

 Z 
+ vô cùng 
0;
.
x
 
d) Tổng các nghiệm thuộc đoạn 
[pi]

0;2
 của phương trình 

+
+
=

(
+

1
cos
3
0
sin
3
f
x
f
x
 
bằng pi × 
3
2
 
Câu 113. Cho hàm số 

=
=
-
2
ln 4
y
f x
ex
x
. Xét tính đúng sai các mệnh đề sau: 
a) ()=3
f e
. 
b) Hàm số có tập xác định là 

=

0; 4
D
e. 
c) Phương trình 

'
=0
f
x
 có một nghiệm 
=2
x
e. 
d) Giá trị lớn nhất của hàm số đã cho trên đoạ[n]

1; 3e có dạng 
+
ln2
a
b thì +=4
a
b
. 
Câu 114. Cho hàm số ()

=
+
2
3
log
4
f x
x
. Xét tính đúng sai các mệnh đề sau: 
a) Phương trình ()=
f x
m luôn có hai nghiệm phân biệt với mọi giá trị của tham số m. 
b) ()=
1
4
f
. 
c) Phương trình ()=4
f x
 có một nghiệm duy nhất 
=1
x
. 
d) Hàm số ()
f x xác định với mọi số thực x. 
Câu 115. Cho hàm số 

-
=
=
-
9
7
log
5
x
y
f x
x
 có đồ thị là ()
C. Xét tính đúng sai các mệnh đề sau: 
a) Đồ thị ()
C có hai tiệm cận đứng. 
b) Tập xác định của hàm số là 

=- vô cùng 
 
+ vô cùng 
;5
7;
D
. 
c) Đồ thị ()
C có một đường tiệm cận ngang. 
d) Gọi 

;
,
;
M
N
N
N

```

## Chủ đề: `dang_phuong_trinh_luong_giac`
### Nguồn: `Chuyên đề ôn thi tốt nghiệp THPT năm 2026 môn Toán – Nguyễn Tiến Hà.pdf` (page_6)
```text
CHUYÊN ĐỀ ÔN THI TN.THPT MÔN TOÁN 12 NĂM 2026-2027 
PTLG 
 
 
ThS. Nguyễn Tiến Hà – Zalo: 0949.888.993 
 Trang 3 
NGUYỄN TIẾN HÀ
NGUYỄN TIẾN HÀ
PHẦN 1. PHƯƠNG TRÌNH LƯỢNG GIÁC CƠ BẢN 
Câu 1: (Đề TN.THPT 2025 BGD - MĐ 0102) Tập nghiệm của phương trình sin
1
x =
 là 
A. 
2
2
S
k
k
pi
pi

{
{
{
{
=
+
 Z 

{
{
{
{

'
∣
. 
B. 
2
S
k
k
pi
pi

{
{
{
{
=
+
 Z 

{
{
{
{

'
∣
. 
C. 

2
S
k
k
pi
=
 Z '
∣
. 
D. 

S
k
k
pi
=
 Z '
∣
. 
Câu 2: (Đề TN.THPT 2025 BGD - MĐ 0103) Tập nghiệm của phương trình sin
0
x =
 là 
A. 
 
2
S
k
k
pi
pi

{
{
{
{
=
+
 Z 

{
{
{
{

Z
∣
. 
B. 

Z
S
k
k
pi
=
 Z 
∣
. 
C. 
2
 
2
S
k
k
pi
pi

{
{
{
{
=
+
 Z 

{
{
{
{

Z
∣
. 
D. 

Z
2
S
k
k
pi
=
 Z 
∣
. 
Câu 3: (Chuyên Lê Quý Đôn-Vũng Tàu) Tất cả các nghiệm của phương trình sin 2
0
x =
 là 
A. 

x
k
k
pi
=
 Z '. 
 
B. 

2
k
x
k
pi
=
 Z '. 
C. 

4
2
k
x
k
pi
pi
=
+
 Z '. 
D. 

2
x
k
k
pi
pi
=
+
 Z '. 
Câu 4: (Chuyên Thăng Long - Lâm Đồng) Nghiệm của phương trình 2sin
1
0
x +
=
 là 
A. 
7
2;
2.
6
6
x
k
x
k
pi
pi
pi
pi
=
+
=
+
 
B. 
7
2;
2.
6
6
x
k
x
k
pi
pi
pi
pi
=-
+
=
+
 
C. 
2;
2.
8
x
k
x
k
pi
pi
pi
pi
=
+
=
+
 
D. 
5
2;
2.
6
6
x
k
x
k
pi
pi
pi
pi
=-
+
=
+
 
Câu 5: (THPT Cao Nguyên) Nghiệm của phương trình sin
1
2
x =
 là 
A. 
2
x
k
pi
pi
=
+
. 
B. 
2
x
k pi
=
. 
C. 
2
2
x
k
pi
pi
=
+
. 
D. 
4
x
k
pi
pi
=
+
. 
Câu 6: (THPT Việt Đức - Hà Nội) Phương trình sin
sin
x
 alpha 
=
 có họ nghiệm là 
A. 
2,
x
k
k
 alpha 
pi
= 
+
 Z '. 
B. 
,
x
k
k
 alpha 
pi
=
+
 Z '. 
C. 
2
,
2
x
k
k
x
k
 alpha 
pi
pi
 alpha 
pi
[
=
+
[
 
```

### Nguồn: `Chuyên đề ôn thi tốt nghiệp THPT năm 2026 môn Toán – Nguyễn Tiến Hà.pdf` (page_566)
```text
ĐỀ THI THỬ TN.THPT MÔN TOÁN 12 NĂM 2026-2027 
ĐỀ THI THỬ SỐ 11 
 
 
ThS. Nguyễn Tiến Hà – Zalo: 0949.888.993 
 Trang 563 
NGUYỄN TIẾN HÀ
NGUYỄN TIẾN HÀ
Câu 7: Cho hình chóp.
S ABC, biết 

SA
ABC
 vuông góc 
 và tam giác ABC vuông tại A. Đường thẳng 
AB vuông góc với mặt phẳng nào sau đây? 
 
A. 
SAB. 
B. 
SAC. 
C. 
SBC. 
D. 
ABC. 
Câu 8: Hai xạ thủA và B cùng bắn súng một cách độc lập. Xác suất bắn trúng bia của hai xạ thủ 
A và B lần lượt bằng 1
3 và 2
5. Xác suất để cả hai xạ thủA và B cùng bắn trúng bia là 
A. 13
15. 
B. 11
15. 
C. 3
5. 
D. 2
15. 
Câu 9: Từ một hộp gồm 13 quả cầu cân đối và đồng chất, trong đó có 8 quả cầu màu trắng và 5 
quả cầu màu đen. Lấy ngẫu nhiên đồng thời 2 quả cầu từ hộp. Tính xác suất lấy được 2 
quả cầu cùng màu. 
A. 3.
13 
B. 20.
39 
C. 19.
39 
D. 17.
39 
Câu 10: Đạo hàm của hàm số 
=
-
+
3
2
1
1
3
y
x
x
 là 
A. 
=
-
2
2.
y
x
x 
B. 
=
-
+
2
2
1.
y
x
x
 C. 
=
-
3
2.
y
x
x 
D. 
=
-
2
1
2.
3
y
x
x. 
Câu 11: Tiếp tuyến của đồ thị hàm số 
=
+
-
2
4
5
y
x
x
 tại điểm có hoành độ bằng 1 là 
A. 
=
+
6
1.
y
x
 
B. 
=
+
6
6.
y
x
 
C. 
=
-
6
1.
y
x
 
D. 
=
-
6
6.
y
x
 
Câu 12: Khảo sát thời gian tự học bài ở nhà của học sinh khối 12 ở trường X, ta thu được bảng sau: 
 
Thời gian [0;30) [30;60) [60;90) [90;120) [120;150) 
Số học sinh
 75 
 125 
 250 
 82 
 18 
Phương sai của mẫu số liệu ghép nhóm là 
A. 874. 
B. 875. 
C. 873. 
D. 872. 
 
PHẦN II. Câu trắc nghiệm đúng sai. Thí sinh trả lời từ câu 13 đến câu 16. Trong mỗi ý a), b), 
c), d) ở mỗi câu, thí sin
```

## Chủ đề: `dang_nguyen_ham_tich_phan_co_ban`
### Nguồn: `Tổng ôn.pdf` (page_515)
```text
» Trang 108 
dài có xu hướng bay với tốc độ 
min
v
 để làm giảm tiêu hao năng lượng xuống còn tối 
thiểu 
24
=
min
E
J. Khi đó: 
 
Mệnh đề 
Đúng 
Sai 
(a) 
39
=
min
v
 km/h. 
X 
 
(b) 
Năng 
lượng 
tiêu 
hao 
của 
con 
vẹt 
được 
tính 
bởi 

471 51
0 31
=
+
,
,
E v
v
J
v
 
 
X 
(c) Năng lượng tiêu hao khi con vẹt bay với vận tốc là 36 km/h bằng 
25 56
,
J (làm tròn kết quả đến hàng phần trăm của J). 
X 
 
(d) 
Biết rằng sau 1 giờ quan sát con vẹt đi được quãng đường 22 km, tốc 
độ bay của con vẹt được tại thời điểm 1 giờ quan sát được xác định 
thông qua phương trình 
4
=
+
v
t
b(km/h). Năng lượng tiêu hao của 
con vẹt tại thời điểm bắt đầu quan sát nhỏ hơn 

30 J. 
X 
 
» Câu 9. Một nhà bán lẻ nhận được một lô hàng gạo nặng 10000 kg, sẽ được sử dụng hết trong 
vòng 5 tháng với tốc độ tiêu thụ đều đặn là 2000kg mỗi tháng. Biết rằng chi phí lưu 
trữ là 1000đồng cho mỗi kg mỗi tháng. Khi đó: 
 
Mệnh đề 
Đúng 
Sai 
(a) Số kg gạo còn trong kho sau t tháng là 10000
2000
-
t (0
5
<=<=
t
). 
X 
 
(b) 
Gọi ()
S t (đơn vị: nghìn đồng) là tổng chi phí lưu trữ trong t tháng, 
khi đó ()
2
10000
1000
=
-
S t
t
t. 
X 
 
(c) Chi phí lưu trữ trong 5 tháng là 25 triệu đồng. 
X 
 
(d) 
Biết rằng nhà bán lẻ mua gạo với giá 12000 đồng/kg và lúc ban đầu 
bán với giá 18000 đồng/kg, giá bán gạo mỗi tháng được mô phỏng 
theo hàm 

G t (nghìn đồng/kg) thì tốc độ thay đổi giá bán gạo được 
tính theo công thức 

2
3
'
=
-
G t
t
(nghìn đồng/tháng) (0
5
<=<=
t
). Sau 5 
tháng nhà bán lẻ đó c
```

### Nguồn: `Chuyên đề ôn thi tốt nghiệp THPT năm 2026 môn Toán – Nguyễn Tiến Hà.pdf` (page_593)
```text
ĐỀ THI THỬ TN.THPT MÔN TOÁN 12 NĂM 2026-2027 
ĐỀ THI THỬ SỐ 17 
 
 
ThS. Nguyễn Tiến Hà – Zalo: 0949.888.993 
 Trang 590 
NGUYỄN TIẾN HÀ
NGUYỄN TIẾN HÀ
Người ta căng hai sợi dây cáp phát sáng vào hai đường chéo của hình hộp là A C
'
 và BD'
. Giá sợi dây cáp là 100 nghìn đồng/mét. 
a) Tọa độ các điểm 
0;10;0
B
, 
20;10;0
C
, 

0;0;5
A'
, 

20;0;5
D'
. 
b) Tổng số tiền cần để mua hai sợi dây cáp phát sáng nói trên là 2613nghìn đồng. 
c) Mặt phẳng 
A BC
'
 có phương trình là: 
2
10
0
y
z
+
-
=
. 
d) Trên dây A C
'
 một điểm sáng M chuyển động đều từ A' đến C với vận tốc 3
/
m
s. 
Đồng thời, trên dây BD', điểm sáng N chuyển động đều từ B đến D' với vận tốc 
2
/
m
s. Tính từ khi hai điểm sáng bắt đầu chuyển động đến khi có ít nhất một điểm sáng 
về đích thì khoảng cách nhỏ nhất giữa hai điểm sáng M và N bằng 3,77m. 
 
Câu 14: Một lon sữa cho trẻ em được lấy ra khỏi tủ lạnh và đặt trên bàn để rã đông. Nhiệt độ của 
lon sữa tại thời điểm lấy ra khỏi tủ lạnh là 
4 C
-°
, và sau t giờ, tốc độ tăng nhiệt độ của 
lon sữa được cho bởi công thức 

0,35
7.
t
T
t
e-
'
=
(
/
C
°
giờ) cho đến khi lon sữa đạt nhiệt độ 
môi trường là 10 C
°
. 
a) Sau 2 giờ, tốc độ thay đổi nhiệt độ của lon sữa bằng 3,48
/
C
°
giờ. 
b) Nhiệt độ của lon sữa tính từ thời điểm lấy ra khỏi tủ lạnh cho đến khi lon sữa đạt nhiệt 
độ môi trường được tính bởi công thức ()
0,35
20.
t
T t
e-
=-
. 
c) Thời gian để lon sữa đạt nhiệt độ môi trường là 3,44 giờ. 
d) Ngay sau khi đạt nhiệt độ môi trường, lon sữa được đưa vào m
```

## Chủ đề: `dang_oxyz_vecto_toa_do_diem`
### Nguồn: `Vận dụng cao.pdf` (page_317)
```text
CHƯƠNG II. HÌNH HỌC KHÔNG GIAN
Teacher2kkk | Học toán cùng GenZ
Câu 801. Cho hình chóp đều S.ABCD có SA = AB = 4
√
2. Gọi M là trung điểm của AB, G là
trọng tâm tam giác SAB
A -→
SA+-→
SB = -→
SC +-→
SD.
B -→
DS = -2--→
DM +3--→
DG.
C Nếu chọn hệtọa độOxyz sao cho O là tâm hình vuông ABCD, B thuộc tia Ox, C thuộc tia
Oy, S thuộc tia Oz. Điểm E(a;b;c) thuộc mặt phẳng (SBD) sao cho C, E, G thẳng hàng. Khi
đó, a+b+c = 2.
D Nếu chọn hệtọa độOxyz sao cho O là tâm hình vuông ABCD, B thuộc tia Ox, C thuộc tia
Oy, S thuộc tia Oz. Điểm F(x;y;z) thuộc mặt phẳng (SAC) sao cho FG+FB nhỏnhất. Khi
đó, x+y +z = -1.
Câu 802. Trong không gian với hệtrục tọa độOxyz, cho hai điểm A(3;-1;4) và B(-2;2;3). Các
điểm M, N thay đổi sao cho M luôn thuộc mặt phẳng (Oxy) và --→
MN = (-2;-2;1).
A Hình chiếu vuông góc của A xuống mặt phẳng (Oxy) có tọa độ(0;1;4).
B Điểm D(a;b;c) là điểm thỏa mãn --→
BD = --→
NM. Khi đó, a+b+c = 1.
C Điểm C thuộc mặt phẳng (Oxy) thỏa mãn A, B, C thẳng hàng. Khi đó, 3-→
CA = 4--→
CB.
D Giá trịnhỏnhất của AM +MN +NB bằng 12.
Câu 803. Trong không gian với hệtọa độOxyz, cho hai điểm A(5;0;2) và B(5;10;4). Các điểm M,
N di động trên mặt phẳng (Oxy) sao cho độdài MN bằng 2. Tổng AM +BN có giá trịnhỏnhất
là bao nhiêu?
HƯỚNG ĐẾN KỲTHI HSG - ĐGTD - ĐGNL - THPTQG
2 0 2 7
BIÊN SOẠN: TRƯƠNG CÔNG ĐẠT
Tuyển tập VD - VDC trong các đềthi thửTHPTQG | 582
H
Ọ
C
T
O
Á
N
C
Ù
N
G
G
E
N
Z
+
-
×
÷
N
N∗
Z
Q
I
R
C
R
P̸
=
log
ln
∈
/∈
∀
∄
∃
∅
∨
∧
⊄
⊂
≡
≠
=
>
<
≥
≤
√
lim
sin
cos
tan
cot
⊥
∥
Ak
n
C
```

### Nguồn: `Vận dụng cao.pdf` (page_188)
```text
CHƯƠNG II. HÌNH HỌC KHÔNG GIAN
Teacher2kkk | Học toán cùng GenZ
Bài tập 1. Trong không gian Oxyz, cho các điểm A(1;2;1), B (2;-1;3), C (-3;2;5) và D(4;5;-6)
A Chứng minh rằng A, B, C, D là các đỉnh của một tứdiện.
B Tính diện tích tam giác ABC.
C Tính thểtích của tứdiện ABCD và độdài đường cao kẻtừD của tứdiện.
D Tìm tọa độcác đỉnh còn lại của hình hộp dựng trên ba cạnh AB, AC, AD và tính thểtích
hình hộp đó.
Bài tập 2. Cho vectơ -→u tùy ý khác -→0. Tính giá trịbiểu thức cos2 -→u,-→i

+cos2 -→u,-→j

+cos2 -→u,-→k

.
Bài tập 3. Cho A(1;-2;-1), B (3;-2;-3), C (-4;4;-2) và D(3;2;-4). Viết phương trình mặt
phẳng (P) đi qua C, D và thỏa mãn d(A,(P)) = 2d(B,(P)).
Bài tập 4. Cho điểm M (1;2;3). Viết phương trình của mặt phẳng đi qua M, theo thứtựcắt các
trục tọa độOx, Oy, Oz tại A, B, C sao cho
A M là trọng tâm tam giác ABC.
B M là trực tâm tam giác ABC.
Bài tập 5. Trong không gian Oxyz, cho (P): 3x-y +2z -5 = 0 và (Q): x+3y -2z +3 = 0.
A Viết phương trình đường thẳng ∆là giao tuyến của (P) và (Q).
B Tìm tọa độđiểm H là hình chiếu của M(2;3;-5) trên ∆.
C Tìm tọa độđiểm K đối xứng với M qua ∆.
Bài tập 6. Cho mặt phẳng (P): 2x-2y-z-4 = 0 và mặt cầu (S): x2 +y2 +z2 -2x-4y -6z -11 = 0.
Chứng minh rằng mặt phẳng (P) cắt mặt cầu (S) theo một đường tròn. Xác định tâm và bán kính
của đường tròn đó.
Bài tập 7. Viết phương trình mặt cầu chứa đường tròn (ω):
{
|
{
|
{
(x-3)2 +(y -4)2 +z2 = 36
4x+y -z -9 = 0
và đi
qua điểm M (7;-3;1).
Bài tập 8. Viết phương trình mặt cầu đi qua hai đường 
```

## Chủ đề: `dang_oxyz_mat_phang_duong_thang`
### Nguồn: `Vận dụng cao.pdf` (page_273)
```text
CHƯƠNG II. HÌNH HỌC KHÔNG GIAN
Teacher2kkk | Học toán cùng GenZ
Câu 484. Cho hai mặt cầu (S1) và (S2) đồng tâm I, có bán kính lần lượt là R1 = 2 và R2 =
√
10.
Xét tứdiện ABCD có hai đỉnh A, B nằm trên (S1) và hai đỉnh C, D nằm trên (S2). Thểtích lớn
nhất của khối tứdiện ABCD bằng
Câu 485. Trong không gian với hệtoạđộOxyz, cho điểm N (2;3;4). Một mặt cầu bất kì đi qua O
và N cắt các trục toạđộOx, Oy, Oz lần lượt tại A,B,C̸ ≡O. Biết rằng khi mặt cầu thay đổi nhưng
vẫn thoảđềbài, trọng tâm G của tam giác ABC luôn nằm trên một mặt phẳng cốđịnh. Mặt phẳng
cốđịnh này chắn các trục toạđộthành một tứdiện, thểtích của khối tứdiện đó bằng
Câu 486. Tứdiện ABCD có ABC là tam giác đều. Góc giữa hai mặt phẳng (BCD) và (ABC) là
60◦. Hình cầu tâm O bán kính bằng 1 tiếp xúc AB, AC và mặt phẳng (BCD). Gọi H là hình chiếu
vuông góc của D trên mặt phẳng (ABC), H nằm trong tam giác ABC. Biết rằng O thuộc đường
thẳng DH và DH = AB
2. Tính thểtích tứdiện ABCD.
Câu 487. Trong không gian với hệtoạđộOxyz, cho hai điểm A(2;-1;-1), B (0;1;-2) và mặt
phẳng (P): 2x+y -2z -2 = 0. Điểm M thuộc mặt phẳng (P) sao cho \
AMB lớn nhất thì giá trịcủa
cos \
AMB bằng
Câu 488. Cho khối lăng trụABC.A'B'C', khoảng cách từC đến BB' bằng
√
5; khoảng cách từA
đến BB', CC' lần lượt bằng 1 và 2. Hình chiếu vuông góc của A trên mặt phẳng

A'B'C'
là trung
điểm M của B'C' và A'M =
√
15
3. Thểtích của khối lăng trụđã cho bằng
Câu 489. Cho hình chóp S.ABC có SA = 2
√
3a
3
và SA vuông góc với mặt phẳng (ABC). Đáy
ABC có BC = a
```

### Nguồn: `THCS-THPT Nguyễn Khuyến.pdf` (page_3_ocr)
```text
PHAN II. CÂU TRAC NGHIEM DUNG SAI
Caul.
Cho hamsé y= f (x) =In (x-1)+ 2%,
Xét tính đúng sai các mệnh đềsau:
Đúng
Sai
a) Tập xác định của ham sốlà 2 =[1; +00).
LTD
|
b) Phương trình y'=0 có tập nghiệm là S =BỊ
JErlliri
c) Hàm sốf(x) có giá trịbé nhất trên đoạn [2; 4] bằng In2+6 khi x=3.
| if) TE |
d) Bắt phương trình f(x) > 2x có tập nghiệm là (2; +00).
ee
Cau 2.
Trong không gian với hệtọa độÓxyz, các vecto đơn vi trên các trục Ox, Ov, Oz lần lượt là 7, 7, k š
độdài mỗi vectơ đơn vịbằng Imét, cho điểm A(12; —8; 4). Một vật, coi như một chất điểm, chuyển
động thang từ4 hướng tới điểm B. Tốc độcủa vat tai thời điểm ¿ giây là v(t) = at +240 (m/s) trong
đó a là hằng sốdương và 0</<8. Biết rằng sau 3 giây ké từthời điểm ban dau, vật đi được quãng
đường 738m.
Gọi u = (c: đ; e) là vectơ đơn vịcùng hướng với AB. Biết cosin của góc giữa # với các vectơ
i, j, k lần lượt là = a 5
a
7
Xét tinh đúng sai các mệnh dé sau:
Đúng
Sai
9)
a)c==.
[sẽ
77
|HH|
b) Phương trình đường thẳng 4B là " == -=
==
Pees
nẽẼ8. 1ã ng
d) Giảsửsau 6 giây kểtừthời điểm ban dau, vật đến điểm Ö8(x;: y;:z„). Khi đó
x, >450.
a
x
s
Câu 3.
Một đại lý chuyên cung cap các loại Sơn nước đã trang tri một phân trên
yy
banner quảng cáo của mình theo một cách khá đặc biệt. Ban dau họthiét kê
22
một hình giới hạn bởi parabol (P) có đỉnh S và đường thang nằm ngang AB;
22
trong đó SO = AB =4 m với O là trung điểm AB.
Gi" 24
Họtiến hành sơn 3 màu khác nhau lên hình phẳng này theo cách sau:
⁄
`
e Phan trên là phần kẻsọc được sơn với
```

## Chủ đề: `dang_xac_suat_co_dien_to_hop`
### Nguồn: `LTT 7-10.pdf` (page_4)
```text
a) Chu vi của chiếc đèn là 36 cm
π
. 
b) 
1
2
3
|
| 24 N
+
+
=

F
F
F
. 
c) Khi độ dài của ba sợi dây càng tăng (
18 inch
>
l
) thì độ lớn các lực căng F giảm nhưng không 
vượt quá 9 N. 
d) Chiều dài tối thiểu của mỗi sợi dây để lực căng mỗi sợi không vượt quá 24 N là 13,5 2 inch. 
Câu 4. Ba bạn An, Bình, Cường tham gia trò chơi lập team cho game X, mỗi bạn 1 team gồm 4 nhân 
vật. Máy tính chia ngẫu nhiên cho 3 bạn 9 nhân vật khác nhau (mỗi bạn nhận 3 nhân vật). Sau khi 
thực hiện chia các nhân vật xong, máy tính sẽ chọn ngẫu nhiên cho mỗi bạn 1 đội trưởng từ 7 nhân 
vật khác có thể làm đội trưởng (gồm 2 nhân vật tên J, 2 nhân vật tên S và 3 nhân vật tên T) theo thứ 
tự cho ba bạn An, Bình và Cường. 
a) Số cách chia 9 nhân vật cho 3 bạn là 
3
3
3
9
6
3
C
C
C
⋅
⋅
. 
b) Số cách chia 7 đội trưởng cho ba bạn là 210. 
c) Xác suất để An nhận đội trưởng J là 2
7. 
d) Xác suất để Bình nhận đội trưởng J là 2
7. 
PHẦN III: TRẮC NGHIỆM TRẢ LỜI NGẮN. (Thí sinh trả lời câu hỏi từ câu 1 đến câu 6, mỗi 
câu trả lời đúng được 0,5 điểm). 
Câu 1. Trong quá trình thi công mạng lưới viễn thông, cáp quang được kéo ra từ một cuộn cáp lớn 
để mắc lên các cột điện dọc theo tuyến đường. Khi tháo, cáp được trải ra khỏi cuộn theo từng lớp có 
bán kính không đổi. Biết rằng xe kéo cáp di chuyển với vận tốc đều là 2 m/s. Hãy tính tốc độ góc 
(tốc độ quay, tính bằng rad/s) của cuộn cáp tại thời điểm đoạn cáp đang được tháo ra thuộc lớp có 
bán kính 0,5 m.
```

### Nguồn: `Tổng ôn.pdf` (page_351)
```text
» Trang 351 
» Câu 29. Chọn ngẫu nhiên 2 số từ tập 

1 2 3
19 20
=
;;;...;
;
S
. Xác suất để chọn được 2 số mà tích 
của chúng là một số chính phương bằng a. Tính 220
a
. 
 Lời giải 
} Trả lời: 
 
 
 
 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
..................................................................................................................................................... 
» Câu 30. Cho tập 

1 2 3 4 5 6
=
;;;;;
A
. Gọi S là tập hợp các tam giác có độ dài ba cạ
```

## Chủ đề: `dang_xac_suat_doc_lap_xung_khac`
### Nguồn: `Chuyên đề ôn thi tốt nghiệp THPT năm 2026 môn Toán – Nguyễn Tiến Hà.pdf` (page_514)
```text
CHUYÊN ĐỀ ÔN THI TN.THPT MÔN TOÁN 12 NĂM 2026-2027 
CHỦ ĐỀ 22 
 
 
ThS. Nguyễn Tiến Hà – Zalo: 0949.888.993 
 Trang 511 
NGUYỄN TIẾN HÀ
NGUYỄN TIẾN HÀ
c) Xác suất để bạn An được 2 điểm phần trắc nghiệm đúng sai là 1.
32 
d) Xác suất để bạn An được 3 điểm phần trắc nghiệm đúng sai là 9.
128 
 
Câu 71. Một người vừa gieo một con xúc xắc để ghi lại số chấm xuất hiện, sau đó người này tiếp tục 
chọn ngẫu nhiên một lá bài từ bộ bài 52 lá. 
a) Gọi A là biến cố: “Số chấm của xúc xắc bằng 6”, khi đó: 
1

6
P A =
. 
b) Gọi B là biến cố: “Chọn được một lá bài cơ”, khi đó: 
3

13
P B =
 
c) Xác suất để “số chấm trên con xúc xắc là 6 và chọn được một lá bài cơ” bằng: 1.
24 
d) Xác suất để số chấm trên con xúc xắc và số của lá bài là giống nhau bằng: 1.
13 
 
Câu 72. Khảo sát tại một trường THPT cho thấy tỷ lệ học sinh thích bóng đá là 65%, thích bóng 
rổ là 30% và thích cả hai môn này là 20%. Chọn ngẫu nhiên một học sinh trong trường. 
Các mệnh đề sau đúng hay sai? 
a) Xác suất để chọn được học sinh thích cả bóng đá và bóng rổ là 0,2. 
b) Xác suất để chọn được học sinh chỉ thích một trong hai môn bóng đá hoặc bóng rổ là 
0,95. 
c) Xác suất để chọn được học sinh thích ít nhất một trong hai môn bóng đá và bóng rổ là 
0,75. 
d) Xác suất để chọn được học sinh thích bóng đá là 0,65. 
 
Câu 73. Có hai hộp chứa các tấm thẻ. Hộp I chứa 8 tấm thẻ màu vàng được đánh số từ 1 đến 8, 
hộp II chứa 9 tấm thẻ màu đỏ được đánh số từ 1 đến 9. Lấy ngẫu nhiên từ mỗi hộp một 
tấm thẻ. 
a) Số phần tử của khôn
```

### Nguồn: `Chuyên đề ôn thi tốt nghiệp THPT năm 2026 môn Toán – Nguyễn Tiến Hà.pdf` (page_277)
```text
CHUYÊN ĐỀ ÔN THI TN.THPT MÔN TOÁN 12 NĂM 2026-2027 
CHỦ ĐỀ 15 
 
 
ThS. Nguyễn Tiến Hà – Zalo: 0949.888.993 
 Trang 274 
NGUYỄN TIẾN HÀ
NGUYỄN TIẾN HÀ
 
Xác suất để Huy chọn được 
a) Một bóng đèn màu vàng là 0,6. 
b) Một bóng đèn không hỏng, biết nó màu trắng là 0,97. 
c) Một bóng đèn không hỏng, biết nó màu vàng là 0,98. 
d) Một bóng đèn không hỏng là 0,974. 
Câu 17. Một công ty truyền thông đấu thầu hai dự án. Khả năng thắng thầu của dự án thứ nhất là 0,6 và 
dự án thứ hai là 0,5. Khả năng thắng thầu cả hai dự án là 0,4. Gọi,
A B lần lượt là biến cố thắng 
thầu dự án thứ nhất và dự án thứ hai. 
a) A và B là hai biến cố độc lập. 
b) Xác suất công ty thắng thầu đúng một dự án là 0,3. 
c) Biết công ty thắng thầu dự án thứ nhất, xác suất công ty thắng thầu dự án thứ hai là 
0,4. 
d) Biết công ty không thắng thầu dự án thứ nhất, xác suất công ty thắng thầu dự án thứ 
hai là 0,25. 
Câu 18. Một nhà máy có hai phân xưởng A và B tương ứng làm ra 60% và 40% sản phẩm của nhà máy. Tỉ 
lệ phế phẩm của hai phân xưởng A và B lần lượt là 1% và 2%. Chọn ngẫu nhiên một sản phẩm của 
nhà máy. 
 
a) Nếu sản phẩm chọn ra thuộc phân xưởng A thì xác suất để nó không là phế phẩm là 
0,98. 
b) Xác suất để sản phẩm chọn ra là phế phẩm và thuộc phân xưởng A là 0,006. 
c) Xác suất để sản phẩm chọn ra là phế phẩm là 0,014. 
d) Nếu sản phẩm chọn ra là phế phẩm thì xác suất để nó thuộc phân xưởng A là 4
7. 
Câu 19. Một túi chứa ba đồng xu công bằng và một đồng xu có hai mặt ngửa. Một đồng xu được chọn 
n
```

## Chủ đề: `dang_thong_ke_trung_vi_mot`
### Nguồn: `Ôn tập.pdf` (page_57)
```text
Trang. 55 
CHƯƠNG III. CÁC SỐĐẶC TRƯNG ĐO MỨC ĐỘPHÂN TÁN CỦA MẪU SỐLIỆU GHÉP NHÓM
 
a) Chiều cao trung bình của mỗi cây do hai bạn Hùng và Vương trồng không bằng nhau. 
b) Khoảng biến thiên của cả hai mẫu số liệu trên là 20. 
c) Khoảng tứ phân vị của mẫu số liệu ở bảng 1 là 5,5. 
d) Chiều cao của các cây mà bạn Vương trồng đồng đều hơn các cây mà bạn Hùng trồng. 
Câu 3: Điểm kiểm tra giữa học kì I môn Toán của 2 nhóm học sinh được cho trong 2 bảng sau: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Khi đó: 
a) Khoảng biến thiên cuả hai mẫu số liệu đã cho ở hai bảng trên là 6. 
b) Khoảng tứ phân vị cuả mẫu số liệu đã cho ở bảng nhóm học sinh 1 xấp xỉ là 5,8. 
c) Điểm kiểm tra trung bình của hai nhóm học sinh trên là xấp xỉ bằng nhau. 
d) Điểm kiểm tra của nhóm học sinh 1 đồng đều hơn của nhóm học sinh 2. 
Câu 4: Bảng sau thống kê tổng lượng mưa (đơn vị: mm) đo được vào tháng 7 từ năm 2002 đến 2021 tại một trạm quan 
trắc đặt ở Cà Mau. 
 
Các mệnh đề sau đúng hay sai? 
a) Cỡ mẫu là n = 20 
b) Khoảng biến thiên của mẫu số liệu trên là R = 357,9 mm 
c) Tứ phân vị thứ nhất của mẫu số liệu là 
1
254,9
Q =
 
d) Khoảng tứ phân vị của mẫu số liệu trên là 
162,35
Q
 Delta =
 
PHẦN III. Câu trắc nghiệm trả lời ngắn. 
Câu 1: Cho bảng số liệu về khối lượng của 30 củ khoai tây thu hoạch từ một thửa ruộng như dưới đây. 
ượng (gam)
[70;80)
[80;90)
[90;100)
[100;110)
[110;120)
3
6
12
6
3
 Khoảng tứ phân vị của mẫu số liệu ghép nhóm là bao nhiêu?
```

### Nguồn: `Chuyên đề ôn thi tốt nghiệp THPT năm 2026 môn Toán – Nguyễn Tiến Hà.pdf` (page_30)
```text
CHUYÊN ĐỀ ÔN THI TN.THPT MÔN TOÁN 12 NĂM 2026-2027 
THỐNG KÊ 
 
 
ThS. Nguyễn Tiến Hà – Zalo: 0949.888.993 
 Trang 27 
NGUYỄN TIẾN HÀ
NGUYỄN TIẾN HÀ
Câu 36: (THPT Triệu Sơn 1 - Thanh Hóa) Thống kê lợi nhuận hàng tháng (đơn vị: triệu đồng) trong 
20 tháng của một nhà đầu tư được cho như sau: 
Lợi nhuận 
)
[10;20 
)
[20;30 
)
[30;40 
)
[40;50 
)
[50;60 
Số tháng 
2 
4 
8 
4 
2 
Độ lệch chuẩn của mẫu số liệu trên là S. Chọn khẳng định đúng nhất trong 4 khẳng định 
sau: 
A. 
=9,95
S
. 
B. 
~=109,5
S
. 
C. 
=11,95
S
. 
D. 
~=10,95
S
. 
Câu 37: (Chuyên KHTN Hà Nội) Thống kê độ tuổi tập thể dục thể thao hàng ngày trong một cụm dân 
cư có bảng số liệu sau: 
Độ tuổi 
)
[10;20 
)
[20;30 
)
[30;40 
)
[40;50 
)
[50;60 
Số người 
10
6 
15 
19 
25 
Tính phương sai của mẫu số liệu trên (kết quả làm tròn đến hàng phần trăm). 
A. 189,66. 
B. 13,68. 
C. 187,13. 
D. 187,03. 
Câu 38: Thống kê lợi nhuận hằng tháng (đợn vị: triệu đồng) trong 20 tháng của hai nhà đầu tư được cho 
như sau: 
Lợi nhuận 
)
[10;15 
)
[15;20 
)
[20;25 
)
[25;30 
)
[30;35 
Số tháng 
4 
5
1 
7 
3 
Bảng 1. Lợi nhuận hằng tháng của nhà đầu tư A 
Lợi nhuận 
)
[500;510 
)
[510;520 
)
[520;530 
)
[530;540 
)
[540;550 
Số tháng 
3 
5
2 
6 
4 
Bảng 2. Lợi nhuận hằng tháng của nhà đầu tư B 
Phát biểu nào sau đây sai? 
A. Lợi nhuận trung bình một tháng của nhà đầu tư A là 22,5 triệu đồng. 
B. Độ lệch chuẩn của số tiền thu được hằng tháng của nhà đầu tư A nhỏ hơn nhà đầu tư 
B. 
C. Độ lệch chuẩn của số tiền thu được hằng tháng của h
```

## Chủ đề: `dang_hinh_khong_gian_the_tich`
### Nguồn: `Đề Thanh Hoá.pdf` (page_1)
```text
Trang 1/4 - Mã đề 1101 
SỞ GIÁO DỤC VÀ ĐÀO TẠO 
THANH HÓA 
 
 ĐỀ CHÍNH THỨC 
 Mã đề: 1101 
 
KHẢO SÁT CHẤT LƯỢNG HỌC SINH LỚP 12 
(LẦN 1) NĂM HỌC 2025 - 2026 
 
MÔN KHẢO SÁT: TOÁN 
Thời gian làm bài: 90 phút (không kể thời gian phát đề) 
(Đề có 04 trang) 
Họ, tên thí sinh:....................................................; Số báo danh:.................................................. 
 Chữ ký của giám thị 1:........................................; Chữ ký của giám thị 2:................................. 
PHẦN I. Thí sinh trả lời từ câu 1 đến câu 12. Mỗi câu hỏi thí sinh chỉ chọn một phương án. 
Câu 1. Thời gian truy cập Internet trong một buổi tối của một nhóm học sinh được cho trong bảng 
sau 
 Thời gian (phút) 
9 5 12 5
[,;
,) 
12 5 15 5
[
,;
,) 
15 5 18 5
[
,;
,) 
18 5 21 5
[
,;
,) 
21 5 24 5
[
,;
,) 
 Số học sinh 
3 
12 
15 
24 
2 
Tính trung vị của mẫu số liệu ghép nhóm này. 
 
A. 18,1. 
B. 18,5. 
C. 15,6. 
D. 17,2. 
Câu 2. Cho khối chóp tam giác.S ABC có chiều cao bằng 3, đáy là tam giác ABC có diện tích 
bằng 10. Thể tích khối chóp.S ABC bằng 
 
A. 2. 
B. 30. 
C. 15. 
D. 10. 
Câu 3. Cho lăng trụ đứng 
.
ABC A B C
' ' '. Đáy là tam giác ABC vuông cân tại B (Hình minh họa 
bên). Khi đó góc giữa vectơ AB

 và vectơ 
' '
A C

 bằng bao nhiêu? 
 
A. 45°. 
B. 60°. 
 
 C. 135°. 
D. 90°. 
 
 
 
Câu 4. Tập nghiệm của phương trình 

3
3
2
1
1
log
log
x
x
-
=
-
 là 
 
A. 
{ }
0
=
S
. 
B. 

2
= -
S
. 
C. 
{ }
2
S =
. 
D. S = ∅. 
Câu 5. Cho cấp số nhân 
n
u
 với 
1
2
=
u
 và côn
```

### Nguồn: `Chuyên đề ôn thi tốt nghiệp THPT năm 2026 môn Toán – Nguyễn Tiến Hà.pdf` (page_86)
```text
CHUYÊN ĐỀ ÔN THI TN.THPT MÔN TOÁN 12 NĂM 2026-2027 
THỂ TÍCH 
 
 
ThS. Nguyễn Tiến Hà – Zalo: 0949.888.993 
 Trang 83 
NGUYỄN TIẾN HÀ
NGUYỄN TIẾN HÀ
Câu 72. (THPT Cẩm Giàng - Hải Dương) Cho hình lăng trụ đứng 
.
ABC A B C
'
'
' có đáy ABC 
là tam giác vuông tại A, AC
a
=
, · 
60
ACB =
°. Đường thẳng BC ' tạo với 
ACC A
'' một 
góc 30°. Tính thể tích V của khối trụ 
.
ABC A B C
'
'
'. 
 
A. 
3 6
V
a
=
. 
B. 
3 3
3
a
V =
. 
C. 
3
3
V
a
=
. 
D. 
3 3
V
a
=
. 
Câu 73. (THPT Lý Nhân Tông) Cho khối lăng trụ đứng tam giác 
.
ABC A B C
'
'
' có đáy là một 
tam giác vuông tại A. Cho 
2
AC
AB
a
=
=
, góc giữa AC ' và mặt phẳng 
ABC bằng 
30°.Tính thể tích khối lăng trụ 
.
ABC A B C
'
'
'. 
 
A. 
3
2
3
3
a
. 
B. 
3 3
3
a
. 
C. 
3
3
a
. 
D. 
3
4
3
3
a
. 
Câu 74. (THPT Lương Thế Vinh - Hà Nội) Cho hình lăng trụ đứng 
.
ABC A B C
'
'
' có đáy ABC 
là tam giác vuông tại A, biết AB
a
=
, 
2
AC
a
=
 và 
3
A B
a
'
=
. Tính thể tích của khối 
lăng trụ 
.
ABC A B C
'
'
'. 
 
A. 
3
2 2
3
a. 
B. 
3
5
3
a. 
C. 
3
5a. 
D. 
3
2 2a. 
Câu 75. (THPT Tô Hiến Thành - Thanh Hóa) Cho khối lăng trụ đứng tam giác 
.
ABC A B C
'
'
' 
có đáy là một tam giác vuông cân tại A, 
2
AC
AB
a
=
=
, góc giữa AC ' và mặt phẳng 

ABC bằng 30°. Thể tích khối lăng trụ 
.
ABC A B C
'
'
' là 
 
A. 
3
2
3
3
a
. 
B. 
3
4
3
3
a
. 
C. 
3
4
3
9
a
. 
D. 
3
4
3
3
a
. 
A'
C'
B'
A
C
B
A'
C'
B'
A
C
B
A'
C'
B'
A
C
B
A'
C'
B'
A
C
B
```

## Chủ đề: `dang_cap_so_cong_cap_so_nhan`
### Nguồn: `chuyên môn số 08 – Cà Mau .pdf` (page_1)
```text
Trang 1/4 - Mã đề 0101 
 
SỞ GIÁO DỤC VÀ ĐÀO TẠO 
CÀ MAU 
 
ĐỀ THI CHÍNH THỨC 
(Đề thi có 04 trang) 
KỲ THI THỬ TỐT NGHIỆP THPT NĂM 2026 
CỤM CHUYÊN MÔN SỐ 08 
MÔN: TOÁN 
Ngày thi: 23/5/2026 
Thời gian làm bài: 90 phút, không kể thời gian phát đề 
Họ, tên thí sinh:.......................................................................... 
Số báo danh:............................................................................... 
Mã đề thi 0101 
PHẦN I. Thí sinh trả lời từ câu 1 đến câu 12. Mỗi câu hỏi thí sinh chỉ chọn một phương án. 
Câu 1. Cho cấp số cộng 
n
u
có số hạng đầu 
1
5
u = - và công sai 
3
d =
. Số 97 là số hạng thứ mấy của cấp số 
cộng? 
 
A. 34. 
B. 20. 
C. 35. 
D. 36. 
Câu 2. Cho hàm số 
ax
b
y
cx
d
+
=
+
 (với 
0;
0
c
ad
bc
!=
-
!=
) có đồ thị như hình dưới đây. 
 
Tiệm cận ngang của đồ thị hàm số là 
 
A. 
1
y =. 
B. 
1
y = -. 
C. 
1
x = -. 
D. 
1
x =. 
Câu 3. Trong không gian với hệ tọa độ Oxyz, cho hai điểm 

2;1; 2
A
-
 và 

4;3;4
B -
. Tọa độ trung điểm M 
của đoạn AB là: 
 
A. 
2;4;2
-
. 
B. 
8;2; 8
-
-
. 
C. 
1;2;1
-
. 
D. 
6;2;6
-
. 
Câu 4. Cho hình lập phương 
. '
'
'
'
ABCD A B C D (minh họa như hình bên). Mệnh đề nào sau đây sai? 
 
 
A. 
'
'
AB
AD
AA
AC
+
+
=
. B. AC
AB
AD
=
+
. 
C. AB
CD
=
. 
 
D. AB
CD
=
. 
Câu 5. Cho hàm số 

y
f x
=
 có đồ thị là đường cong trong hình bên. Hàm số đã cho nghịch biến trên khoảng 
nào dưới đây? 
 
 
A. 
0;+ vô cùng. 
B. 
; 1
- vô cùng -
. 
C. 
0;1. 
D. 
1;0.
-
 
Câu 6. Thể tích khối tròn xoay tạo thành khi cho h
```

### Nguồn: `Ninh Bình lần 3.pdf` (page_1)
```text
Mã đề 0101 - Trang 1/4 
SỞ GIÁO DỤC VÀ ĐÀO TẠO 
TỈNH NINH BÌNH 
 
 
 
MÃ ĐỀ: 0101 
ĐỀ KHẢO SÁT, ĐÁNH GIÁ 
CHẤT LƯỢNG GIÁO DỤC LỚP 12 THPT 
LẦN THỨ BA - NĂM HỌC 2025-2026 
MÔN THI: TOÁN - THPT, GDTX 
 (Thời gian làm bài: 90 phút) 
 
Đề thi khảo sát gồm 04 trang. 
Họ và tên học sinh:……………………………………… 
Số báo danh:………….……………………..…………… 
 
PHẦN I. Thí sinh trả lời từ câu 1 đến câu 12. Mỗi câu hỏi thí sinh chỉ chọn một phương án. 
Câu 1: Hàm số 

ln
F x
x
=
 là nguyên hàm của hàm số nào dưới đây trên khoảng 
0;+ vô cùng ? 
A. 

1
2026
f x
x
=
-
. 
B. 

1
f
x
x
=-
. 
C. 

1
f x
x
=
. 
D. 

1
2026
f
x
x
=
+
. 
Câu 2: Nghiệm của phương trình 

0
3
cot 3
45
3
x -
=
 
là 
A. 
0
0
25
180,
x
k
k
=
+
 Z 
. 
B. 
0
0
35
60,
x
k
k
=
+
 Z 
. 
C. 
0
0
30
60,
x
k
k
=
+
 Z 
. 
D. 
0
0
60
180,
x
k
k
=
+
 Z 
. 
Câu 3: Cho hàm số 

f x liên tục trên đoạn [,]
a b. Biết 
()d
2026
b
a
f x
x =
 tích phân 
, giá trị của 2 ()d
a
b
f x
x
 tích phân 
 là 
A. 4052
-
. 
B. 4052. 
C. 1013. 
D. 1013
-
. 
Câu 4: Nghiệm của phương trình 

4
log
1
3
x-
=
 là 
A. 
68
x =
. 
B. 
65
x =
. 
C. 
66
x =
. 
D. 
63
x =
. 
Câu 5: Cho hàm số 

y
f x
=
 liên tục trên đoạ[n]
1;5
-
 và có đồ thị như hình vẽ. Gọi M và m lần lượt là 
giá trị lớn nhất và nhỏ nhất của hàm số đã cho trê[n]
1;5
-
. Giá trị của M
m
-
 bằng 
 
A. 1. 
B. 4. 
C. 6. 
D. 5. 
Câu 6: Trong không gian với hệ trục tọa độ Oxyz, cho đường thẳng 
3
4
1
:
2
5
3
x
y
z
d
-
-
+
=
=
. Vectơ nào dưới 
đây là một vectơ chỉ phương của d ? 
A. 

2
2;4; 1
u =
-
. 
B. 

1

```
