# QUY TẮC MẶC ĐỊNH DỰ ÁN TẠO ĐỀ TOÁN (THPTQG 2025 - 2027)

Bất cứ khi nào người dùng:
- Yêu cầu **tạo đề mới** (ví dụ: "tạo đề 7", "sinh đề 8") $\implies$ **Chạy từ Pha 0 đến Pha 4** (tự động đọc Kho Tài Liệu Nguồn tại `d:\Tao_De\Nguon_Tai_Lieu` để tổng hợp câu hỏi và tạo file `.tex` mới).
- Hoặc cung cấp một đề thi Toán có sẵn (file `.tex`, mã nguồn LaTeX, hoặc yêu cầu xử lý đề như "xử lý đề 4", "quăng đề vào") $\implies$ **Chạy từ Pha 1 đến Pha 4**.

**TỰ ĐỘNG CHẠY TOÀN DIỆN (theo skill `pipeline-de-toan`), KHÔNG CHỜ NGƯỜI DÙNG PHẢI PROMPT NHẮC TỪNG BƯỚC:**

---

### QUY CHUẨN HEADLINE & HEADNOTE BẮT BUỘC TRONG TẤT CẢ CÁC ĐỀ:
1. **Headline (Tiêu đề đầu đề & Header trang):** `HƯỚNG TỚI THPTQG 2027`
2. **Headnote / Thông tin tác giả:** `Người biên soạn: Dương Gia Bảo`
3. **Cấu hình chuẩn LaTeX (`fancyhdr` & Tiêu đề):**
   ```latex
   \pagestyle{fancy}
   \fancyhf{}
   \lhead{\small\textbf{HƯỚNG TỚI THPTQG 2027}}
   \rhead{\small\textit{Người biên soạn: Dương Gia Bảo}}
   \rfoot{\small Trang \thepage}
   \renewcommand{\headrulewidth}{0.4pt}
   ```
   Khối tiêu đề đầu trang (2 cột chuẩn đề thi Sở GD&ĐT + dòng `Họ và tên:... SBD:...` kèm khung `Mã đề thi 000<số_đề>` thay cho line ngang, không lặp lại tên người biên soạn vì đã có ở headnote):
   ```latex
   \noindent
   \begin{minipage}[t]{0.40\textwidth}
       \centering
       \textbf{HƯỚNG TỚI THPTQG 2027}\\[-2pt]
       \rule{3.2cm}{0.6pt}\\[4pt]
       \textbf{ĐỀ CHÍNH THỨC}
   \end{minipage}\hfill
   \begin{minipage}[t]{0.58\textwidth}
       \centering
       \textbf{ĐỀ THI KHẢO SÁT CHẤT LƯỢNG}\\
       \textbf{ĐỀ SỐ <số_đề>}\\
       \textbf{Môn thi: TOÁN}\\
       \textit{\small Thời gian làm bài: 90 phút, không kể thời gian phát đề}
   \end{minipage}

   \vspace{0.2cm}
   \noindent
   \begin{minipage}[b]{0.78\textwidth}
       \textbf{Họ và tên:}\dotfill\textbf{SBD:}\makebox[3.5cm]{\dotfill}
   \end{minipage}\hfill
   \begin{minipage}[b]{0.20\textwidth}
       \hfill
       \setlength{\fboxrule}{0.8pt}%
       \fbox{\begin{minipage}{2.3cm}
           \centering
           \textbf{\small Mã đề thi}\\
           \textbf{000<số_đề>}
       \end{minipage}}
   \end{minipage}
   \vspace{0.2cm}
   ```

---

### QUY TRÌNH XỬ LÝ CHI TIẾT (PHA 0 $\to$ PHA 4):

0. **Pha 0: Tự động Tổng hợp & Tạo Đề mới từ Kho Tài Liệu Nguồn Local RAG (Thay thế hoàn toàn bước dùng web NotebookLM)**
   - Tất cả tài liệu nguồn của người dùng (`.pdf`, `.docx`, `.tex`, `.md`, `.txt`) được đặt trong thư mục `d:\Tao_De\Nguon_Tai_Lieu`.
   - Khi người dùng yêu cầu tạo Đề số `<số_đề>` mới mà chưa có file `.tex`:
     + Chạy lệnh `python "d:\Tao_De\scripts\index_tai_lieu.py" --exam <số_đề>` để tự động quét kho tài liệu nguồn, phân loại theo chuyên đề và trích xuất ngữ liệu tham khảo vào `d:\Tao_De\Nguon_Tai_Lieu\_index\sample_de_<số_đề>.md`.
     + Đọc ngữ liệu tham khảo vừa trích xuất kết hợp với cấu trúc các đề trước (`De 1`..`De 6`) để tổng hợp bộ 22 câu hỏi mới (Phần I: 12 câu, Phần II: 4 câu Đúng/Sai, Phần III: 6 câu Trả lời ngắn), không trùng lặp với các đề cũ, loại bỏ ngay từ đầu dạng toán hàm hợp $g(x)=f(u(x))$.
     + Dùng Python (`SymPy`) tính toán và thiết kế bộ số liệu chuẩn xác 100% trước khi ghi ra file `d:\Tao_De\De <số_đề>\De <số_đề>.tex`.

1. **Pha 1: Audit & Giải độc lập bằng Python (SymPy/NumPy)**
   - Không tin tưởng đáp án/lời giải có sẵn của file gốc.
   - Giải lại 100% tất cả các câu: Phần I (12 câu), Phần II (4 câu - 16 ý), Phần III (6 câu).
   - Phát hiện và sửa sạch các lỗi ảo giác AI (chia cho 0, tích phân phân kỳ, ép số vô lý, sai nhãn Đúng/Sai, số liệu lẻ không nguyên).

2. **Pha 2: Quét Hàm Hợp, Chuẩn hóa theo Chương trình GDPT 2018 & Nâng độ khó**
   - **KIỂM TRA & LOẠI BỎ TRIỆT ĐỂ DẠNG TOÁN HÀM HỢP:**
     + Quét toàn bộ đề thi, phát hiện bất kỳ câu nào liên quan đến **hàm hợp dạng $g(x) = f(u(x))$**, $f(f(x))$, cực trị/đơn điệu/số nghiệm hàm hợp từ đồ thị hoặc bảng biến thiên cho trước.
     + **NẾU CÓ $\implies$ LẬP TỨC THAY BẰNG BÀI KHÁC** theo chuẩn GDPT 2018 (ưu tiên: hàm phân thức bậc 2 trên bậc 1 $y = \dfrac{ax^2+bx+c}{dx+e}$, ứng dụng thực tế giải tích, hoặc Oxyz).
     + Loại bỏ hoàn toàn tích phân hàm ẩn máy móc vô nghĩa.
   - **Bổ sung / thay thế bằng các dạng toán trọng tâm mới mức độ Vận dụng cao (9+):**
     + Hàm phân thức bậc 2 trên bậc 1 $y = \dfrac{ax^2+bx+c}{dx+e}$ (tiệm cận đứng & tiệm cận xiên, cực trị, tâm đối xứng, tiếp tuyến, tam giác tạo bởi các tiệm cận).
     + Tối ưu hóa giải tích thực tế (chi phí, dung tích, góc nhìn camera, tốc độ biến thiên liên quan).
     + Xác suất có điều kiện, công thức Bayes đảo nhiều vòng.
     + Oxyz thực tế (cân bằng lực 3D, cực trị khoảng cách, phản xạ tia sáng, quỹ đạo drone/vệ tinh/radar).
     + Thống kê mẫu số liệu ghép nhóm và các số đo độ phân tán (tứ phân vị, phương sai, độ lệch chuẩn).
   - **RÀNG BUỘC BẮT BUỘC CHO PHẦN III — PHẦN PHÂN LOẠI, CHẶN ĐIỂM:**
     + Trong 6 câu trả lời ngắn, **tổng cộng ít nhất 2 câu khó phải lấy hoặc chế tác từ một hay nhiều tài liệu trong đúng ba file sau**:
       1. `Phương pháp tiếp cận bài toán thực tế trong đề thi THPT QG 2026 môn Toán.pdf`
       2. `Vận dụng cao.pdf`
       3. `Phương pháp trải phẳng giải một số bài toán ứng dụng thực tế – Đặng Việt Đông.pdf`
     + Đọc **Khu vực 0** của `sample_de_<số_đề>.md` và mở trang PDF gốc tương ứng để chọn ít nhất 2 bài toán độc lập, xác nhận đề bài đầy đủ, dữ kiện và hình vẽ. Hai đoạn trích của cùng một bài chỉ tính là **1 câu**.
     + **Giữ nút thắt và độ khó gốc khi chế tác**: phải có bước tự mô hình hóa, phối hợp nhiều điều kiện, lựa chọn đường đi/cấu hình hoặc lập luận tối ưu. Không biến câu khó thành bài thay số trực tiếp, lấy đạo hàm một hàm mục tiêu đã cho sẵn hoặc tính một tích phân đã thiết lập sẵn. Tên tài liệu và `vdc_score` không tự chứng minh độ khó.
     + Hình minh họa không được giải hộ bước then chốt: nếu tự tìm cách trải phẳng là phần phân loại của bài, chỉ vẽ hình không gian/ngữ cảnh, không đưa sẵn toàn bộ hình trải phẳng cùng đường ngắn nhất.
     + Các câu còn lại ưu tiên ba tài liệu trên và ngữ liệu Vận dụng/Vận dụng cao khác; sắp xếp Phần III theo độ khó tăng dần. Tiếp tục loại bỏ hàm hợp, tích phân hàm ẩn máy móc và dạng không phù hợp GDPT 2018.
     + **Trước khi xuất PDF**, ghi đối chiếu câu Phần III với **tên file nguồn chính xác, trang PDF, số câu gốc nếu có và nút thắt tạo độ khó** vào `De <số_đề>/nguon_de<số_đề>.md`. Kiểm đếm ít nhất **2 câu độc lập từ ba file chỉ định**; nếu chưa đủ hoặc đã giản lược mất độ khó, chọn/thay câu cho đạt rồi mới nghiệm thu.
     + Ràng buộc này áp dụng từ **đề 13 trở đi**; giữ nguyên đề 1–12, trừ khi người dùng yêu cầu sửa một đề cụ thể.
   - Cân bằng đáp án Phần I: Phân bố đều $3\text{A} - 3\text{B} - 3\text{C} - 3\text{D}$.
   - Đồng bộ 3 phần: Đề bài & 4 phương án $\longleftrightarrow$ Bảng đáp án $\longleftrightarrow$ Hướng dẫn giải chi tiết.

3. **Pha 3: Tự động Sinh & Chèn Hình Minh Họa (Chuẩn Kép: Có Màu Đẹp Khi Chiếu Màn Hình + Phân Biệt 100% Khi In Trắng Đen)**
   - **QUY TẮC SỐ 1 — CÓ MÀU KHI CHIẾU GIẢNG BÀI & KHÔNG PHỤ THUỘC MÀU KHI IN TRẮNG ĐEN:**
     + **Trên hình vẽ (`TikZ` & Python 2D):** **VẪN VẼ CÓ MÀU SẮC HÀI HÒA** (`blue!55!black`, `teal`, `orange!85!red`,...) để người dạy chiếu file lên màn hình giảng trực tiếp dễ nhìn, sinh động; **ĐỒNG THỜI kết hợp họa tiết gạch chéo (`pattern=north east lines` / `hatch="///"`), tô đậm, tô nhạt, để trắng** giữa các miền khác nhau.
     + **Trong lời văn đề bài:** Khi đã vẽ hình ra, **CẤM TUYỆT ĐỐI đề cập đến màu sắc** để chỉ các phần trên hình (cấm viết *"phần tô màu đỏ"*, *"đường màu xanh"*, *"miền màu cam"*). Chỉ được mô tả bằng các đặc điểm nhận diện được bằng mắt thường cả khi in trắng đen: **`phần gạch chéo`**, **`phần tô đậm`**, **`phần để trắng`**,...
     + **CẤM dùng hộp chú giải màu (`legend` phân biệt bằng màu sắc)**.
   - **QUY TẮC SỐ 2 — KHÔNG CHÚ THÍCH PHƯƠNG TRÌNH LÊN ĐƯỜNG CONG ĐỒ THỊ VÀ KHÔNG GHI TỌA ĐỘ LÊN ĐIỂM:**
     + Đối với các bài toán đồ thị / diện tích hình phẳng (như bài 2 Parabol cắt nhau): Khi đề bài đã cho sẵn các phương trình hàm số và hình vẽ đồ thị chính xác kèm các mốc tọa độ trên trục rồi, **TUYỆT ĐỐI KHÔNG chú thích đường cong nào ứng với phương trình nào lên hình vẽ** — học sinh bắt buộc phải tự nhận diện đồ thị (dựa vào bề lõm, giao điểm, hệ số $a$).
     + Đối với các bài toán Hình học / $Oxyz$: Vì đề bài đã nêu rõ tọa độ các điểm, trên hình vẽ **CHỈ GHI TÊN ĐIỂM NGẮN GỌN (`$A, B, C, D, S, M, H, O$`)**, **TUYỆT ĐỐI KHÔNG GHI KÈM BỘ TỌA ĐỘ `(x; y; z)` LÊN HÌNH**, luôn bật nền trắng lót dưới chữ (`fill=white, inner sep=1pt`) và kiểm tra tọa độ chiếu 2D để các điểm không đè lên trục $Oz$.
   - **QUY TẮC SỐ 3 — TỐI ƯU HÓA GÓC NHÌN & CHIẾN LƯỢC TRỰC QUAN HÓA (CHỐNG ĐÈ NÉT, KHÔNG BÓ HẸP):**
     + Khi vẽ hình trong không gian (Hình học không gian / $Oxyz$), **CẤM TUYỆT ĐỐI** để các đường thẳng, đoạn thẳng, vectơ hoặc trục tọa độ bị chiếu dốc đứng, ép sát nhau thành một bó hẹp hoặc đè lên nhau làm mất tính trực quan và rối mắt.
     + **Ưu tiên trực quan hóa trên mặt phẳng 2D khi bài toán quy về đồng phẳng:** Nếu các đối tượng chính trong bài toán cùng nằm trên một mặt phẳng (ví dụ: gốc tọa độ $O$ và đường thẳng quỹ đạo $d$; điểm và đường thẳng; mặt cắt thiết diện; tam giác phẳng $OMA$), **ƯU TIÊN VISUALIZE TRÊN MẶT PHẲNG 2D** để thể hiện rõ góc vuông, khoảng cách ngắn nhất, chiều chuyển động một cách thông thoáng, học sinh nhìn vào nhận diện được ngay bản chất hình học.
     + **Khi bắt buộc vẽ phối cảnh 3D:** Phải **xoay camera (thử nghiệm và căn chỉnh các vectơ cơ sở $x, y, z$ trong TikZ)** sao cho các đường thẳng, đoạn thẳng và các trục tọa độ tách biệt rõ ràng, tạo thành các góc mở rộng thoáng đãng, nhìn thấy rõ các góc vuông và điểm đặc trưng, không bị trùng nét hay đè chữ.
   - **Phân loại chiến lược tạo hình minh họa (Kết hợp Phương án 1 & Phương án 2):**
     + **Các bài toán Hình học không gian / Hệ tọa độ $Oxyz$ / Hình học phẳng / Đường cong Giải tích 2D (Parabol, Elip, diện tích hình phẳng):** **ƯU TIÊN DÙNG `TikZ` VECTOR TRỰC TIẾP TRONG LATEX (`\usetikzlibrary{arrows.meta,calc,patterns}`) HOẶC PYTHON 2D SẠCH SẼ (2 tia mũi tên $Ox, Oy$, tắt `ax.grid`).**
       * **CẤM TUYỆT ĐỐI** dùng `projection="3d"` (`mpl_toolkits.mplot3d`) của `matplotlib` với hộp xám 3D và lưới `grid` dày đặc gây khuất trục $Oxyz$.
     + **Các bài toán Xác suất / Thống kê / Lãi suất / Ngữ cảnh thực tế phi hình học:** Tạo hình minh họa bằng AI hoặc bỏ qua nếu không cần thiết.
     + **ĐẶC QUY TẮC — BÀI TOÁN BÓNG ĐÁ (SÚT PHẠT ĐỀN, GHI BÀN, THI ĐẤU):** Bất cứ khi nào đề thi xuất hiện câu hỏi liên quan đến chủ đề bóng đá (sút phạt đền, penalty, ghi bàn,...), hình minh họa đi kèm **BẮT BUỘC LIÊN QUAN ĐẾN CRISTIANO RONALDO (CR7)** (sử dụng kho ảnh lưu tại d:\Tao_De\resources\cr7 như dáng nhảy SIUUU, ăn mừng cúp C1,...). Đặt cạnh đề bài bằng minipage một cách thẩm mỹ, kích thích cảm hứng học tập của học sinh.
   - **Giới hạn số lượng hình ở Phần II:** Ở Phần II (4 câu Đúng/Sai), **chỉ tạo và chèn tối đa 1–2 hình minh họa mỗi đề**, không tràn lan ở mọi câu.
   - **Quy chuẩn kích thước & vị trí chèn ảnh (Đặt bên phải đề bài bằng `minipage`):**
     + Đặt nằm bên phải của đề bài bằng cấu trúc `minipage` (`0.55\linewidth` cho đề bài và `0.42\linewidth` cho hình vẽ với `\resizebox{\linewidth}{!}{\begin{tikzpicture}...\end{tikzpicture}}`):
       ```latex
       \item \begin{minipage}[t]{0.55\linewidth}
       <Nội dung đề bài (và các ý a, b, c, d nếu ở Phần II)>
       \end{minipage}\hfill
       \begin{minipage}[t]{0.42\linewidth}
       \vspace{-0.4\baselineskip}
       \centering
       \resizebox{\linewidth}{!}{%
       \begin{tikzpicture}[>=Stealth, line join=round, line cap=round,
           x={(-0.52cm,-0.38cm)}, y={(1cm,0cm)}, z={(0cm,1cm)}]
           ...
       \end{tikzpicture}%
       }
       \end{minipage}
       ```
   - **LƯU Ý:** **Tuyệt đối không chèn ảnh cũ tái sử dụng sai lệch nội dung.**

4. **Pha 4: Biên dịch pdflatex, Tách Đề & Đáp án, và Xuất bản**
   - Thêm `\usepackage{graphicx}` vào preamble (nếu có hình ảnh).
   - Biên dịch bằng `pdflatex -interaction=nonstopmode`.
   - Xử lý triệt để overfull hbox nếu có, đảm bảo layout đẹp mắt, không tràn lề.
   - Đảm bảo `BẢNG ĐÁP ÁN TỔNG HỢP` và `HƯỚNG DẪN GIẢI CHI TIẾT` bắt đầu ở trang mới (`\newpage`).
   - **Tự động Tách Đề bài và Đáp án thành 2 file PDF riêng biệt bằng Python (`pypdf`):**
     + **File Đề bài** (chỉ gồm đề thi từ đầu đến hết Phần III, không có đáp án): Lưu thành `<số_đề>.pdf` vào thư mục:
       `D:\Document\Dạy học\Đề ko đáp án\PRIVATE\<số_đề>.pdf`
     + **File Đáp án & Lời giải** (từ `BẢNG ĐÁP ÁN TỔNG HỢP` và `HƯỚNG DẪN GIẢI CHI TIẾT` đến hết): Lưu thành `<số_đề>.pdf` vào thư mục:
       `D:\Document\Dạy học\Đề ko đáp án\PRIVATE\Ans\<số_đề>.pdf`
   - Trình bày bảng tổng hợp nghiệm thu ngắn gọn, súc tích cho người dùng kèm liên kết kiểm tra các file đã xuất bản.
