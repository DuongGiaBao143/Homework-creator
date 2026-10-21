# Phân tích sườn và ma trận đề giữa kỳ I — Toán 10

## Kết luận để dùng khi tạo đề

**Chọn đề Xuân Trường, mã 1101, làm sườn chính** vì đúng cấu trúc người dùng đã chốt: **12 trắc nghiệm + 2 đúng/sai + 4 trả lời ngắn + 4 tự luận; 90 phút**. Nội dung tập trung vào ba mạch:

1. Mệnh đề và tập hợp.
2. Bất phương trình, hệ bất phương trình bậc nhất hai ẩn.
3. Giá trị lượng giác và hệ thức lượng trong tam giác.

Đề mới nên giữ kiểu nhiệm vụ, phạm vi và nhịp khó của sườn này, thay ngữ cảnh/số liệu và giải lại độc lập. Không chỉ đổi vài con số, cũng không lấy ngẫu nhiên cả 13 chủ đề của chương trình lớp 10.

Đây là **sườn đề xuất có căn cứ**, không phải một ma trận chung chính thức áp dụng cho cả 20 PDF. Các trường có tiến độ, số câu tự luận và cách chấm khác nhau.

## Đã đọc những gì và giới hạn của kết quả

- Khảo sát văn bản toàn bộ **20 PDF, 530 trang**; trích xuất văn bản và OCR các trang ít/không có lớp chữ.
- Phân tích phần câu hỏi của **đề/mã đầu đại diện từng file**, không xem nhiều mã hoán vị là các mẫu độc lập. Các sách có nhiều đề không được tính thành một “đề chung” duy nhất.
- Đọc và xem hình trực tiếp ma trận Nguyễn Trãi trang PDF 10, đặc tả trang 11–13; ma trận Quế Sơn trang 7, đặc tả trang 8–11.
- Đọc sâu đề Xuân Trường trang 1–3 và biểu điểm tự luận trang 8–9; đối chiếu Nguyễn Văn Cừ trang 1–3. Kiểm tra riêng Việt Đức và Duy Tân bằng OCR; xem ảnh các trang quyết định phạm vi/cấu trúc.
- Chưa kiểm toán toàn bộ đáp án và lời giải của 530 trang. Nhãn mức độ gán cho sườn đề xuất là phân tích chuyên môn, không phải dữ liệu học sinh làm thử.

Danh mục tên file chính xác, trang đã phân tích và SHA-256 nằm trong [nguon_tham_khao.json](</D:/Tao_De/Lớp 10/ma_tran/nguon_tham_khao.json>). Không tìm được prompt cộng đồng phù hợp sau hai lượt tìm; phân tích dưới đây bám trực tiếp tài liệu người dùng cung cấp.

## Các sườn trong thư mục không đồng nhất

Các số dưới đây lần lượt là **trắc nghiệm / đúng-sai / trả lời ngắn / tự luận**, đếm theo câu lớn của đề đầu đại diện. Một câu tự luận có a), b) vẫn là một câu lớn.

| Tài liệu/trường | Cấu trúc đại diện | Điểm cần lưu ý |
|---|---:|---|
| Bộ ôn SGK thống nhất, 31 trang | 12 / 2 / 4 / 3 | Lời dẫn đúng/sai ghi 4 nhưng đề đầu thực tế có 2 câu |
| Bộ ôn Lê Minh Kha, 191 trang | 12 / 2 / 4 / 3 | Đề đầu lặp lại nội dung Nguyễn Trãi; lời giải từ trang PDF 66 |
| Bộ ôn Ngô Đức Tài, 152 trang | 12 / 2 / 4 / 3 | Có cả cuối kỳ; khối cuối kỳ bắt đầu trang PDF 68 |
| Đông Thái | 12 / 4 / 0 / 3 | Không có phần trả lời ngắn |
| Gia Bình 1 | 12 / 2 / 4 / 3 | Có vectơ |
| Lục Nam | 12 / 2 / 4 / 3 | Có cả hàm số và vectơ |
| Lý Tự Trọng | 12 / 2 / 4 / 3 | Ba mạch chính, tự luận có hình thực tế |
| Ngô Gia Tự 1 | 12 / 3 / 4 / 3 | Có 3 câu đúng/sai; tự luận 2 điểm |
| Nguyễn Công Trứ | 12 / 4 / 2 / 4 | Đảo số lượng giữa đúng/sai và trả lời ngắn |
| Nguyễn Du | 12 / 2 / 4 / 3 | Có vectơ nhập môn |
| Nhữ Văn Lan | 12 / 2 / 4 / 3 | Có phiếu làm bài xen giữa các mã đề |
| **Xuân Trường** | **12 / 2 / 4 / 4** | **Khớp cấu trúc; phần I chia đều ba mạch** |
| Việt Đức | 12 / 2 / 4 / 2 | Chỉ mệnh đề–tập hợp và bất phương trình; chưa có hệ thức lượng |
| Chuyên Vị Thanh | 24 / 4 / 0 / 0 | 60 phút; có hàm số bậc hai |
| Duy Tân | 12 / 2 / 4 / 3 | Đề scan; ba mạch chính |
| Nguyễn Thái Bình | 12 / 2 / 4 / 3 | Cơ cấu điểm 3–2–2–3 |
| Nguyễn Trãi | 12 / 2 / 4 / 3 | Có ma trận, đặc tả; một số mã câu trong đặc tả lệch vị trí thực tế |
| **Nguyễn Văn Cừ** | **12 / 2 / 4 / 4** | **Khớp cấu trúc nhưng có vectơ, phân bố nội dung khác Xuân Trường** |
| Quế Sơn | 12 / 2 / 4 / 3 | Có ma trận; cần đối chiếu lại phân bố chủ đề với câu hỏi thực tế |
| Lê Thị Hồng Gấm | 12 / 4 / 4 / 0 | Không có tự luận trong đề đầu |

Vì có đề chép lại trong sách và nhiều mã hoán vị, không dùng số trang hay số file xuất hiện để suy ra tần suất thống kê của một dạng toán.

## Ma trận quan sát được ở sườn Xuân Trường

Nguồn: [đề Xuân Trường](</D:/Tao_De/Lớp 10/Nguon_Tai_Lieu/Đề thi/giữa kì/de-giua-hoc-ky-1-toan-10-nam-2025-2026-truong-thpt-xuan-truong-ninh-binh.pdf>), mã 1101, trang PDF 1–3; biểu điểm tự luận trang 8–9.

| Mạch kiến thức | Phần I | Phần II | Phần III | Phần IV |
|---|---|---|---|---|
| Mệnh đề–tập hợp | C4, C5, C8, C11 | C2: phép toán tập hợp/khoảng | C1: số phần tử | C1: giao hai khoảng |
| Bất phương trình hai ẩn | C2, C7, C10, C12 | C1: mô hình chi phí/ủng hộ | C3: tham số, đúng với mọi điểm của miền nghiệm | C4: mô hình sản xuất, lập hệ và tối ưu |
| Lượng giác–tam giác | C1, C3, C6, C9 | Không có | C2: hải đăng; C4: tính lượng giác | C2: tính/biến đổi lượng giác; C3: diện tích hình thang thực tế |

Ba đặc trưng đáng giữ:

- **Phần I kiểm nền rộng:** mỗi mạch có 4 câu; chủ yếu nhận biết khái niệm, công thức, dấu và kiểm tra một nghiệm.
- **Độ phân loại nằm ở thao tác và mô hình:** phần III có bài tham số trên miền đa giác; phần IV có hình ghép và bài toán tối ưu sản xuất.
- **Hai mảng ứng dụng có vai trò rõ:** hệ bất phương trình dùng ràng buộc tài nguyên/lợi nhuận; hệ thức lượng dùng đo gián tiếp/diện tích. Tập hợp xuất hiện cả lý thuyết và thao tác với khoảng.

Biểu điểm tự luận gốc là **0,5 – 1,0 – 0,5 – 1,0**, tổng 3 điểm. Câu hình thực tế nhiều bước chỉ có 0,5 điểm, trong khi câu lượng giác gồm hai ý có 1 điểm. Có thể giữ dạng câu nhưng cân lại trọng số khi tạo đề mới.

Đề [Nguyễn Văn Cừ](</D:/Tao_De/Lớp 10/Nguon_Tai_Lieu/Đề thi/giữa kì/de-giua-ky-1-toan-10-nam-2025-2026-truong-thpt-nguyen-van-cu-hai-phong.pdf>) cũng đúng 12+2+4+4, nhưng phần I có vectơ; tự luận là tập hợp, biểu diễn hệ, tham số tập hợp và chiều cao tam giác, với điểm **1–1–0,5–0,5**. Vì vậy cùng số câu không đồng nghĩa cùng ma trận nội dung.

## Hai ma trận có sẵn cho biết gì?

| Nguồn | Mệnh đề–tập hợp | BPT/hệ BPT | Lượng giác–tam giác | Mức độ ghi trong bảng |
|---|---:|---:|---:|---|
| [Nguyễn Trãi, trang PDF 10](</D:/Tao_De/Lớp 10/Nguon_Tai_Lieu/Đề thi/giữa kì/de-giua-ky-1-toan-10-nam-2025-2026-truong-thpt-nguyen-trai-da-nang.pdf>) | 4,0 điểm | 3,0 điểm | 3,0 điểm | Biết 40% – Hiểu 30% – Vận dụng 30% |
| [Quế Sơn, trang PDF 7](</D:/Tao_De/Lớp 10/Nguon_Tai_Lieu/Đề thi/giữa kì/de-giua-ky-1-toan-10-nam-2025-2026-truong-thpt-que-son-da-nang.pdf>) | 3,5 điểm | 2,0 điểm | 4,5 điểm | Biết 40% – Hiểu 30% – Vận dụng 30% |

Hai bảng cùng dùng cơ cấu **3 điểm nhiều lựa chọn + 2 điểm đúng/sai + 2 điểm trả lời ngắn + 3 điểm tự luận**, nhưng đều chỉ có **3 câu tự luận**. Ta có thể tham khảo tỷ trọng mức độ và tổng điểm từng phần, không bê nguyên số câu.

**Có lỗi lệch giữa bảng và đề thực tế:** bảng Quế Sơn gán một câu trả lời ngắn cho tập hợp, nhưng cả bốn câu ngắn của đề mã 101 trang 2 đều là lượng giác/tam giác. Tính theo câu thực tế và thang điểm trang 5 cho tỷ trọng chủ đề **30%–20%–50%**, khác **35%–20%–45%** ở bảng. Đặc tả còn lệch số thứ tự một số câu ngắn. Vì vậy khi tạo đề mới phải cộng lại từ câu thực tế, không tin tuyệt đối bảng có sẵn.

## Ma trận đề xuất cho project

Đây là bản thiết kế mới tổng hợp từ sườn Xuân Trường và tỷ trọng mức độ của hai bảng trên; **không phải bản chép nguyên của trường nào**.

### Phân bố chủ đề và dạng câu

| Mạch kiến thức | TN nhiều lựa chọn | Đúng/sai | Trả lời ngắn | Tự luận | Điểm tối đa | Tỷ trọng |
|---|---:|---:|---:|---:|---:|---:|
| Mệnh đề–tập hợp | 4 câu | 1 câu × 4 ý | 1 câu | 1 câu × 0,5đ | **3,0** | **30%** |
| BPT/hệ BPT bậc nhất hai ẩn | 4 câu | 1 câu × 4 ý | 1 câu | 1 câu × 1đ | **3,5** | **35%** |
| Giá trị lượng giác, hệ thức lượng trong tam giác | 4 câu | 0 | 2 câu | 2 câu: 0,5đ + 1đ | **3,5** | **35%** |
| **Tổng** | **12 câu / 3đ** | **2 câu / 2đ** | **4 câu / 2đ** | **4 câu / 3đ** | **10,0** | **100%** |

So với Xuân Trường, đổi điểm tự luận từ **0,5–1–0,5–1** thành **0,5–0,5–1–1** để dành đủ điểm cho câu hình thực tế; tổng điểm mạch lượng giác–tam giác vẫn giữ nguyên. Các tỷ trọng chủ đề trên là điểm của sườn mới theo cơ cấu 3–2–2–3, không khẳng định đó là bảng ma trận được trường Xuân Trường công bố.

### Phân bố mức độ

| Dạng | Biết | Hiểu | Vận dụng | Tổng điểm thiết kế |
|---|---|---|---|---:|
| 12 câu nhiều lựa chọn | 12 câu = 3đ | — | — | 3,0 |
| 8 ý đúng/sai | 4 ý = 1đ | 4 ý = 1đ | — | 2,0 |
| 4 câu trả lời ngắn | — | 2 câu = 1đ | 2 câu = 1đ | 2,0 |
| 4 câu tự luận | — | 2 câu = 1đ | 2 câu = 2đ | 3,0 |
| **Tổng** | **4đ / 40%** | **3đ / 30%** | **3đ / 30%** | **10,0** |

**Quy ước khi đọc bảng:** để phân bổ mức độ, mỗi ý đúng/sai mang trọng số thiết kế 0,25 điểm. Cách chấm thực tế có thể khác: Việt Đức trang 5 và Duy Tân trang 4 chấm theo số ý đúng **0,1 / 0,25 / 0,5 / 1**. Với chấm lũy tiến, không được cộng 0,25 điểm cho từng ý vào bài làm. Tỷ lệ 40/30/30 lúc đó là ngân sách đánh giá của ma trận, không phải phép tách điểm bài làm theo từng ý. Khi xuất đề phải ghi rõ cách chấm được dùng.

Nhãn mức độ phải đi cùng yêu cầu thao tác: nhận ra công thức là Biết; dùng và giải thích quan hệ quen thuộc là Hiểu; tự lập mô hình, phối hợp điều kiện hoặc tìm tham số/cực trị là Vận dụng. Không gắn nhãn Vận dụng chỉ vì đề có tên công ty hay bối cảnh thực tế.

### Bản đặc tả 22 vị trí

Các vị trí dưới đây là **mã dạng bài tham chiếu**, không khóa số câu trên đề. Được hoán đổi thứ tự trong cùng phần, giữ đủ mỗi dạng đúng một lần cùng chủ đề, kỹ năng và mức độ; không chuyển sang phần khác. Hồ sơ nguồn ghi `matrix_slot` để ánh xạ số câu thực tế về mã dạng bài gốc; khi thiếu trường này, bộ kiểm hiểu là giữ thứ tự gốc. Nguồn và trang đối chiếu phải đi theo dạng bài khi đổi số. Không cần sửa ma trận chỉ để hoán đổi. Mỗi dạng có nguồn đối chiếu cụ thể trong [giua_ki_1.json](</D:/Tao_De/Lớp 10/config/giua_ki_1.json>).

| Vị trí | Nội dung cần kiểm tra | Mức độ | Điểm tối đa |
|---|---|---|---:|
| I.1 | Nhận biết một phát biểu là mệnh đề | Biết | 0,25 |
| I.2 | Mệnh đề chứa biến hoặc tính đúng/sai đơn giản | Biết | 0,25 |
| I.3 | Ký hiệu thuộc, tập con | Biết | 0,25 |
| I.4 | Tập con, số phần tử hoặc phép toán đơn giản | Biết | 0,25 |
| I.5 | Nhận dạng BPT bậc nhất hai ẩn | Biết | 0,25 |
| I.6 | Thay tọa độ kiểm tra nghiệm BPT | Biết | 0,25 |
| I.7 | Nhận dạng hệ BPT bậc nhất hai ẩn | Biết | 0,25 |
| I.8 | Điểm thuộc/không thuộc miền nghiệm hệ | Biết | 0,25 |
| I.9 | Dấu giá trị lượng giác theo khoảng góc | Biết | 0,25 |
| I.10 | Hệ thức hai góc bù nhau | Biết | 0,25 |
| I.11 | Định lý sin/côsin | Biết | 0,25 |
| I.12 | Công thức diện tích tam giác | Biết | 0,25 |
| II.1 | Một ngữ cảnh tập hợp; a,b nhận biết, c,d thao tác với tập hợp/khoảng | 2 ý Biết + 2 ý Hiểu | 1,0 |
| II.2 | Một ngữ cảnh BPT; a,b đọc mô hình, c,d lập/kiểm ràng buộc | 2 ý Biết + 2 ý Hiểu | 1,0 |
| III.1 | Đếm số phần tử/số nguyên trong tập hợp có điều kiện | Hiểu | 0,5 |
| III.2 | Tính hoặc biến đổi giá trị lượng giác, kiểm dấu/điều kiện | Hiểu | 0,5 |
| III.3 | Tham số để BPT đúng trên toàn bộ miền đa giác hoặc nhiệm vụ tối ưu tương đương | Vận dụng | 0,5 |
| III.4 | Đo gián tiếp khoảng cách/chiều cao, tự xác định đại lượng cần tìm | Vận dụng | 0,5 |
| IV.1 | Phép toán hai tập hợp/khoảng và biểu diễn trục số | Hiểu | 0,5 |
| IV.2 | Trình bày phép biến đổi lượng giác có điều kiện | Hiểu | 0,5 |
| IV.3 | Hình thực tế cần phân chia/phối hợp nhiều tam giác | Vận dụng | 1,0 |
| IV.4 | Lập hệ ràng buộc sản xuất, tối ưu tuyến tính và kết luận | Vận dụng | 1,0 |

Tổng có **22 câu lớn**; khi tách 8 ý đúng/sai, có **28 đơn vị phân bổ ở cấp câu/ý đúng-sai**. Các ý nhỏ của tự luận không được tính thành câu lớn riêng.

Nhịp thời gian dự kiến: phần I 15 phút, phần II 12 phút, phần III 18 phút, phần IV 40 phút, kiểm tra 5 phút. Đây là mục tiêu thiết kế để thử nghiệm, chưa phải thời gian làm bài được đo với học sinh.

## Cách dùng cùng SGK và Local RAG

Với sườn này, phạm vi là **bài 1–6 của SGK tập 1**: trang in 5–45, tương ứng trang PDF 6–46 trong bản scan hiện có. Các trang cuối chương nằm trong khoảng tham chiếu, không chỉ các trang mở đầu bài.

Chỉ truy xuất ba mã chủ đề:

```powershell
.\rag.ps1 --query "mệnh đề tập hợp khoảng số nguyên" --topic menh_de_tap_hop --role dataset
.\rag.ps1 --query "miền nghiệm hệ bất phương trình tối ưu sản xuất" --topic bpt_hai_an --role dataset
.\rag.ps1 --query "định lý sin cosin đo chiều cao diện tích" --topic he_thuc_luong --role dataset
```

**Ma trận đã được tích hợp vào pipeline.** `config/exam_structure.json` chọn file ma trận qua trường `matrix`; lệnh `--exam N` tự đọc và lấy ngữ liệu cho 22 vị trí trong ba mạch. Bộ kiểm hồ sơ dùng cùng đặc tả để kiểm chủ đề, mức độ và đủ a–d. `GEMINI.md` chứa ma trận cùng pipeline Pha 0–4. Theo yêu cầu người dùng, các bảng điểm phía trên chỉ giữ làm dữ liệu phân tích, không được dùng để kiểm tính/chấm điểm.

Khi tạo đề mới theo sườn này:

1. Đọc `config/giua_ki_1.json`, lập bảng 22 vị trí trước khi viết câu hỏi.
2. Mỗi câu chọn nguồn dataset, đối chiếu đúng bài/trang SGK và lưu hồ sơ nguồn.
3. Giữ cách lập luận của câu phân loại; chọn dữ kiện mới để có nghiệm, hình và đáp số hợp lý.
4. Với bài sản xuất, xác định biến nguyên hay biến liên tục theo đơn vị thực tế; không tối ưu liên tục rồi tự làm tròn số sản phẩm.
5. Câu đúng/sai có cùng một ngữ cảnh, đủ a–d và mức độ của từng ý; tính/chấm điểm hiện được bỏ qua theo yêu cầu người dùng.
6. Giải độc lập, kiểm đủ 12 đáp án, 8 ý đúng/sai, 4 câu ngắn, 4 câu tự luận; đối chiếu từng vị trí với ma trận và chạy `scripts/check_exam.py`.
7. Chỉ xuất PDF sau khi đúng phạm vi, cấu trúc, mức độ và kiểm toán lời giải. Chưa tạo đề hay PDF mới trong lượt phân tích này.

Nếu muốn bám riêng Việt Đức, phải dùng sườn hai mạch và chuyển/thiết kế lại phần tự luận cho đủ 4 câu theo yêu cầu; không lấy tỷ trọng ba mạch của báo cáo này áp vào đề đó.


## Nâng cấp: Chuyển đổi sang Ma trận Khung phân bổ (Blueprint Quota) và Ngân hàng Dạng bài (Skill Pool)

Nhằm giải quyết triệt để vấn đề sườn cố định (fixed question slots) ở phiên bản ban đầu:
- **Hạn chế cũ:** Mỗi vị trí câu hỏi trên đề bị khóa cứng vào một kỹ năng đơn lẻ của đề Xuân Trường 1101 (ví dụ I.1 luôn là nhận biết mệnh đề, I.6 luôn là thay tọa độ kiểm tra nghiệm, II.1 luôn là tập hợp, II.2 luôn là BPT, Hệ thức lượng không bao giờ được xuất hiện ở Đúng/Sai). Điều này làm các đề sinh ra bị đơn điệu, không phản ánh được tính đa dạng của đề thi thực tế.
- **Kiến trúc mới:**
  1. **Khung phân bổ tỷ lệ (Blueprint Quota):** Cố định số câu theo chuẩn 12 + 2 + 4 + 4 (90 phút) và tỷ lệ mức độ/chủ đề trên 3 mạch kiến thức. Cho phép Phần II Đúng/Sai chọn linh hoạt 2 trong 3 mạch kiến thức (bao gồm cả Hệ thức lượng trong tam giác).
  2. **Ngân hàng Dạng bài (Skill Pool GDPT 2018):** Xây dựng 43 dạng bài / yêu cầu cần đạt chi tiết cho cả 3 mạch theo SGK Kết nối tri thức (Bài 1 đến Bài 6). Khi tạo đề, hệ thống bốc ngẫu nhiên dạng bài từ Skill Pool theo seed, giúp mỗi đề thi mang một diện mạo mới mẻ, phong phú và bao quát toàn diện chương trình.
  3. **Bộ kiểm hồ sơ linh hoạt:** `check_exam.py` hỗ trợ cả mã `skill_id` mới và mã `matrix_slot` cũ, bảo đảm tương thích ngược 100% với các đề đã biên soạn trước đó (Đề 1 đến Đề 5).
