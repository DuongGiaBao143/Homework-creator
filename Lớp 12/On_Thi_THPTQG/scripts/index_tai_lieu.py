"""
Script bóc tách & lập chỉ mục Kho Tài Liệu Nguồn (Local RAG) cho Pipeline Tạo Đề Toán.
- Hỗ trợ chạy SONG SONG đa nhân (`ProcessPoolExecutor`) khi bóc tách hàng loạt file .pdf, .docx, .tex, .md, .txt.
- Tự động nhận diện trang PDF scan ảnh (không có text layer) và chạy OCR (`PyMuPDF` + `Tesseract vie+eng`) song song.
- Hỗ trợ Incremental Index (Chỉ quét 1 lần): Lưu trạng thái (mtime, size) của từng file trong catalog.json.
- [UPGRADED] Chấm điểm VDC Thực tế (VDC & Real-world Scoring) + Loại bỏ Hàm hợp/Hàm ẩn cũ theo chuẩn GEMINI.md.
"""
import os
import re
import json
import logging
import zipfile
import random
import hashlib
import argparse
import xml.etree.ElementTree as ET
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed

# Cấu hình đường dẫn tessdata trong môi trường conda taode
DEFAULT_TESSDATA = r"D:\Anaconda\envs\taode\share\tessdata"
if os.path.isdir(DEFAULT_TESSDATA) and not os.environ.get("TESSDATA_PREFIX"):
    os.environ["TESSDATA_PREFIX"] = DEFAULT_TESSDATA

try:
    import pymupdf
    HAS_PYMUPDF = True
except ImportError:
    HAS_PYMUPDF = False
    from pypdf import PdfReader
    logging.getLogger("pypdf").setLevel(logging.ERROR)

BASE_DIR = Path(__file__).resolve().parents[1]
SOURCE_DIR = BASE_DIR / "Nguon_Tai_Lieu"
INDEX_DIR = SOURCE_DIR / "_index"
CATALOG_PATH = INDEX_DIR / "catalog.json"
CHUNKS_PATH = INDEX_DIR / "extracted_chunks.jsonl"
SUPPORTED_EXTS = {".pdf", ".docx", ".tex", ".md", ".txt"}
PART3_HARD_SOURCES = (
    "Phương pháp tiếp cận bài toán thực tế trong đề thi THPT QG 2026 môn Toán.pdf",
    "Vận dụng cao.pdf",
    "Phương pháp trải phẳng giải một số bài toán ứng dụng thực tế – Đặng Việt Đông.pdf",
)

# ==============================================================================
# BỘ TỪ KHÓA CHUYÊN ĐỀ (ĐÃ LOẠI BỎ HÀM HỢP & TÍCH PHÂN HÀM ẨN CŨ THEO GEMINI.MD)
# ==============================================================================
TOPIC_KEYWORDS = {
    # 1. HÀM SỐ & ỨNG DỤNG ĐẠO HÀM
    "dang_ham_so_don_dieu": [
        "xét tính đơn điệu", "khoảng đồng biến", "khoảng nghịch biến", "tìm m để hàm số đồng biến",
        "tìm m để hàm số nghịch biến", "đơn điệu trên khoảng", "đơn điệu trên R", "bảng biến thiên đơn điệu",
        "bảng xét dấu đạo hàm", "đồng biến trên từng khoảng xác định"
    ],
    "dang_ham_so_cuc_tri": [
        "điểm cực trị", "điểm cực đại", "điểm cực tiểu", "giá trị cực đại", "giá trị cực tiểu",
        "số điểm cực trị", "cực trị hàm bậc ba", "cực trị hàm phân thức",
        "tam giác cực trị", "đường thẳng đi qua hai điểm cực trị", "điểm cực trị nằm về hai phía",
        "khoảng cách giữa hai điểm cực trị"
    ],
    "dang_ham_so_gtln_gtnn": [
        "giá trị lớn nhất", "giá trị nhỏ nhất", "GTLN", "GTNN", "tìm max min trên đoạn",
        "tìm max min trên khoảng", "bất phương trình nghiệm đúng với mọi x", "bất phương trình có nghiệm",
        "cô lập tham số m", "tổng giá trị lớn nhất và giá trị nhỏ nhất", "nồng độ thuốc cao nhất trong máu"
    ],
    "dang_ham_so_tiem_can_phan_thuc": [
        "tiệm cận đứng", "tiệm cận ngang", "tiệm cận xiên", "số đường tiệm cận",
        "tiệm cận chứa tham số m", "giao điểm hai đường tiệm cận", "tam giác tạo bởi tiệm cận",
        "tâm đối xứng của đồ thị", "trục đối xứng của đồ thị", "khoảng cách từ tâm đối xứng đến tiếp tuyến",
        "tích khoảng cách từ M đến hai đường tiệm cận", "tổng khoảng cách từ M đến hai tiệm cận",
        "chi phí trung bình tiệm cận", "nồng độ chất khử trùng không vượt ngưỡng"
    ],
    "dang_ham_so_do_thi_bbt": [
        "nhận dạng đồ thị", "đọc bảng biến thiên", "số giao điểm", "phương trình hoành độ giao điểm",
        "tương giao đồ thị", "tâm đối xứng đồ thị", "xác định dấu các hệ số a b c d",
        "tiếp tuyến song song", "hệ số góc tiếp tuyến lớn nhất", "đường cong Agnesi",
        "mô phỏng lát cắt ngọn đồi hồ nước", "đường trượt nước công viên", "tàu lượn siêu tốc"
    ],
    "dang_ham_so_toi_uu_thuc_te": [
        "bài toán tối ưu", "chi phí nhỏ nhất", "lợi nhuận lớn nhất", "diện tích tôn nhỏ nhất",
        "thể tích bể chứa lớn nhất", "cắt góc tạo hộp", "kích thước tối ưu",
        "chi phí nhiên liệu tàu chạy trên sông", "kéo cáp qua sông", "xây cầu bắc qua sông",
        "cây sào ngăn góc hồ thả bèo", "chiều dài cầu thang ngắn nhất qua hàng rào", "xe cứu hỏa vươn thang qua mái che",
        "ô tô đi qua hành lang chữ L vào gara", "cắt khúc gỗ hình trụ thành thanh dầm", "trang sách căn lề diện tích in lớn nhất",
        "cường độ chiếu sáng tối ưu", "góc nhìn bức tranh thuận lợi nhất", "định luật Poiseuille sức cản mạch máu",
        "lắp đặt đường ống nước", "chi phí xây dựng đáy bể và mặt bên"
    ],

    # 2. MŨ, LOGARIT & PHƯƠNG TRÌNH LƯỢNG GIÁC
    "dang_mu_logarit_bien_doi": [
        "rút gọn biểu thức mũ", "tính giá trị logarit", "đổi cơ số logarit",
        "tập xác định hàm số mũ", "tập xác định hàm số logarit", "đạo hàm hàm số mũ", "đạo hàm logarit",
        "đồ thị hàm số mũ và logarit đối xứng qua y = x"
    ],
    "dang_mu_logarit_phuong_trinh_bpt": [
        "phương trình mũ", "phương trình logarit", "bất phương trình mũ", "bất phương trình logarit",
        "đặt ẩn phụ phương trình mũ", "đặt ẩn phụ logarit", "phương pháp logarit hóa", "nghiệm nguyên",
        "đưa về cùng cơ số", "tổng bình phương các nghiệm", "số nghiệm nguyên thuộc đoạn"
    ],
    "dang_mu_logarit_tham_so": [
        "phương trình mũ chứa tham số", "bất phương trình logarit chứa tham số",
        "tìm m để phương trình có 2 nghiệm", "tích các nghiệm", "tổng các nghiệm", "nghiệm thuộc khoảng",
        "bất phương trình mũ nghiệm đúng với mọi x thuộc đoạn"
    ],
    "dang_mu_logarit_thuc_te": [
        "lãi suất ngân hàng", "lãi kép gửi định kỳ", "rút tiền hàng tháng", "tăng trưởng dân số",
        "độ pH hóa học", "cường độ âm decibel", "chu kỳ bán rã", "nhân đôi tài sản",
        "vay trả góp hàng tháng", "lạm phát thực tế", "khấu hao giá trị ô tô", "định tuổi cổ vật Cacbon C14",
        "nuôi cấy vi khuẩn E.Coli phân đôi", "mô hình tăng trưởng logistic", "sức chứa tối đa của hồ cá",
        "định luật làm mát Newton", "ước lượng thời gian tử vong pháp y", "đường cong học tập",
        "công thức Shannon tốc độ truyền tin SNR", "độ chấn động Richter động đất", "áp suất không khí theo độ cao"
    ],
    "dang_phuong_trinh_luong_giac": [
        "phương trình lượng giác", "nghiệm phương trình sin", "nghiệm phương trình cos",
        "nghiệm phương trình tan", "nghiệm phương trình cot", "số nghiệm thuộc khoảng đoạn",
        "tổng các nghiệm lượng giác", "mực nước thủy triều lên xuống", "số giờ có ánh sáng mặt trời",
        "trò chơi đánh đu Hội Lim", "dao động điều hòa", "huyết áp tâm thu tâm trương",
        "quỹ đạo đạn pháo góc bắn", "định luật khúc xạ ánh sáng", "các pha của Mặt Trăng"
    ],

    # 3. NGUYÊN HÀM & TÍCH PHÂN (ƯU TIÊN THỰC TẾ, HÌNH HỌC & ĐỘNG HỌC)
    "dang_nguyen_ham_tich_phan_co_ban": [
        "tìm nguyên hàm", "họ nguyên hàm", "nguyên hàm thỏa mãn điều kiện", "tính tích phân",
        "tích phân phân nhánh", "tích phân đường gấp khúc", "tốc độ thay đổi", "nguyên hàm thực tế"
    ],
    "dang_tich_phan_dien_tich_the_tich": [
        "diện tích hình phẳng", "hình phẳng giới hạn bởi", "thể tích khối tròn xoay",
        "quay quanh trục Ox", "quay quanh trục Oy", "thể tích vật thể thiết diện", "S(x) tích phân",
        "viên gạch hoa bốn cánh parabol", "cổng chào parabol", "thiết kế logo hình con cá",
        "vòm hầm chui bê tông", "khúc gỗ cắt hình nêm", "đồng hồ cát parabol", "phần giao nhau của hai ống trụ vuông góc",
        "chỏm cầu", "hồ lô trang trí", "bồn nước hình trụ đặt nằm ngang", "diện tích miền gạch chéo"
    ],
    "dang_tich_phan_dong_hoc": [
        "chuyển động gia tốc biến thiên", "vận tốc từ gia tốc", "quãng đường từ vận tốc",
        "độ dời", "chuyển động hãm phanh", "tên lửa thử nghiệm", "vật thể cất cánh",
        "thời gian phản ứng trước khi đạp phanh", "ô tô nhập làn đường cao tốc", "đồ thị vận tốc theo thời gian",
        "lưu lượng nước bơm vào bể", "chi phí cận biên", "lợi nhuận biên", "hiệu suất bơm máu của tim"
    ],

    # 4. HÌNH HỌC KHÔNG GIAN TOẠ ĐỘ OXYZ & VECTƠ 3D
    "dang_oxyz_vecto_toa_do_diem": [
        "tọa độ vectơ", "tích vô hướng", "tích có hướng", "trọng tâm tam giác",
        "tọa độ đỉnh hình hộp", "vectơ cùng phương", "vectơ vuông góc", "độ dài đoạn thẳng",
        "quy tắc hình hộp", "quy tắc trọng tâm tứ diện", "ba vectơ đồng phẳng",
        "hình chiếu vuông góc lên trục tọa độ", "hình chiếu lên mặt phẳng tọa độ", "điểm đối xứng"
    ],
    "dang_oxyz_can_bang_luc_vat_ly": [
        "hợp lực của ba lực", "cân bằng lực trong không gian", "đèn chùm treo bốn đoạn xích",
        "giá đỡ ba chân máy quay phim", "chậu cây đặt trên giá đỡ bốn chân", "cần cẩu kéo khung sắt ô tô",
        "lực căng dây cáp", "trọng lực phân bố đều", "công sinh bởi trọng lực trên dốc nghiêng",
        "lực tĩnh điện trong điện trường", "máy tập cáp chéo Cable Crossover", "ba sợi dây không dãn"
    ],
    "dang_oxyz_mat_cau": [
        "phương trình mặt cầu", "tâm và bán kính mặt cầu", "mặt cầu tiếp xúc mặt phẳng",
        "mặt cầu ngoại tiếp", "đường tròn giao tuyến", "bán kính đường tròn giao tuyến", "tiếp tuyến từ A đến mặt cầu",
        "vùng phủ sóng trạm thu phát", "radar kiểm soát không lưu", "thiên thạch bay gần Trái Đất",
        "định vị GPS từ 3 vệ tinh", "định vị từ 4 vệ tinh", "bán kính phủ sóng"
    ],
    "dang_oxyz_mat_phang_duong_thang": [
        "phương trình mặt phẳng", "vectơ pháp tuyến", "phương trình đường thẳng", "vectơ chỉ phương",
        "phương trình tham số", "phương trình chính tắc", "góc giữa hai mặt phẳng",
        "góc giữa đường thẳng và mặt phẳng", "khoảng cách từ điểm đến mặt phẳng",
        "phương trình mặt phẳng theo đoạn chắn", "đường vuông góc chung", "góc cất cánh máy bay",
        "độ dốc mái nhà", "tia sáng laser chiếu lên tường", "mũi khoan xuyên khối gỗ"
    ],
    "dang_oxyz_cuc_tri_khoang_cach": [
        "khoảng cách nhỏ nhất Oxyz", "MA^2 + kMB^2 nhỏ nhất", "điểm M thuộc mặt phẳng sao cho min",
        "khoảng cách giữa hai đường thẳng chéo nhau", "đoạn vuông góc chung", "tâm tỉ cự trong không gian",
        "MA + MB nhỏ nhất trên mặt phẳng", "con cá bơi chạm đáy hồ", "chim bói cá phóng xuống mặt nước",
        "phản xạ tia sáng", "độ dài ngắn nhất của đoạn thẳng MN", "khoảng cách lớn nhất đến mặt phẳng"
    ],
    "dang_oxyz_mo_hinh_hoa_thuc_te": [
        "mô hình drone Oxyz", "mô hình flycam", "đài ra-đa theo dõi máy bay", "mái che vòm sân vận động",
        "kết cấu dây cáp treo", "khoảng cách ngắn nhất giữa 2 thiết bị bay",
        "vận tốc máy bay có gió hướng Đông Bắc", "tên lửa đánh chặn mục tiêu", "bóng của mái nhà trên màn chắn",
        "camera quan sát nhà kho", "quỹ đạo ném bóng rổ 3D", "cú xe đạp chổng ngược Ibrahimovic"
    ],

    # 5. XÁC SUẤT, ĐẠI SỐ TỔ HỢP VÀ THỐNG KÊ GHÉP NHÓM
    "dang_to_hop_quy_tac_dem": [
        "quy tắc cộng", "quy tắc nhân", "hoán vị vòng quanh", "chỉnh hợp", "tổ hợp",
        "xếp người vào dãy ghế", "không có hai phần tử nào đứng cạnh nhau", "ngồi đối diện nhau",
        "đếm số tam giác tứ giác từ đa giác đều", "tam giác vuông tam giác tù nội tiếp đường tròn",
        "đường đi trên lưới ô vuông", "quân xe trên bàn cờ vua", "quân mã di chuyển trên bàn cờ",
        "tô màu các cạnh hình vuông"
    ],
    "dang_xac_suat_co_dien_to_hop": [
        "xác suất cổ điển", "không gian mẫu", "biến cố", "chọn ngẫu nhiên",
        "tổng các chữ số chia hết cho 3", "tổng bình phương chia hết cho 4", "tích các chữ số",
        "ba số lập thành cấp số cộng", "bốn số lập thành cấp số nhân", "chọn đề thi có đủ 3 mức độ"
    ],
    "dang_xac_suat_doc_lap_xung_khac": [
        "biến cố độc lập", "biến cố xung khắc", "xác suất ít nhất một",
        "hai người cùng bắn súng", "xung đột biến cố", "hệ thống mạch điện nối tiếp song song",
        "động cơ hoạt động độc lập", "tô bừa trắc nghiệm đúng sai", "thi đấu thể thao 3 thắng 2",
        "xác suất thắng chung cuộc", "bắn cung tính điểm vòng 8 9 10"
    ],
    "dang_xac_suat_co_dieu_kien_bayes": [
        "xác suất có điều kiện", "P(A|B)", "công thức xác suất toàn phần", "công thức Bayes",
        "xét nghiệm y tế", "độ nhạy", "độ đặc hiệu", "dương tính giả", "kiểm định phế phẩm dây chuyền",
        "sơ đồ hình cây", "chuyển bi giữa hai hộp", "phần mềm lọc tin nhắn rác quảng cáo",
        "phát hiện đạo văn AI", "chặn số điện thoại lừa đảo", "xét nghiệm 2 tầng độc lập",
        "đồng xu cân bằng và đồng xu thiên lệch", "khảo sát dự đoán hành vi mua hàng"
    ],
    "dang_xac_suat_nang_cao_euler": [
        "chia kẹo Euler", "bài toán derangements", "mất vị trí", "trò chơi bốc bóng bốc thẻ",
        "bắn súng lặp vô hạn", "cấp số nhân lùi vô hạn trong xác suất",
        "xích Markov chuyển trạng thái", "định tuyến gói tin kênh A kênh B", "chọn phương tiện đi làm theo tháng",
        "trò chơi cá ngựa gieo xúc xắc", "kỳ vọng của biến ngẫu nhiên rời rạc"
    ],
    "dang_thong_ke_trung_vi_mot": [
        "mẫu số liệu ghép nhóm", "tần số ghép nhóm", "giá trị đại diện",
        "số trung bình ghép nhóm", "trung vị Me ghép nhóm", "mốt Mo ghép nhóm", "nhóm chứa trung vị",
        "tần số tích lũy", "biểu đồ tần số tương đối ghép nhóm"
    ],
    "dang_thong_ke_do_phan_tan": [
        "khoảng biến thiên ghép nhóm", "khoảng tứ phân vị", "tứ phân vị Q1 Q2 Q3",
        "phương sai", "độ lệch chuẩn", "đánh giá mức độ phân tán",
        "so sánh độ đồng đều giữa hai mẫu", "mức độ rủi ro đầu tư"
    ],

    # 6. HÌNH HỌC KHÔNG GIAN CỔ ĐIỂN, TRẢI PHẲNG VÀ DÃY SỐ - CẤP SỐ
    "dang_hinh_khong_gian_goc_khoang_cach": [
        "góc giữa hai đường thẳng", "góc giữa đường thẳng và mặt phẳng", "góc giữa hai mặt phẳng",
        "khoảng cách từ điểm đến mặt phẳng", "khoảng cách giữa hai đường thẳng chéo nhau",
        "góc nhị diện", "số đo góc nhị diện", "tứ diện vuông", "thanh kim loại chéo"
    ],
    "dang_hinh_khong_gian_the_tich": [
        "thể tích khối chóp", "thể tích khối lăng trụ", "thể tích khối hộp chữ nhật",
        "thể tích khối nón", "thể tích khối trụ", "thể tích khối cầu", "tỉ số thể tích",
        "chóp có cạnh bên vuông góc với đáy", "chóp có mặt bên vuông góc với đáy", "chóp đều",
        "thể tích khối chóp cụt đều", "lật ngược bình hình nón chứa nước", "thả bi cầu vào cốc nước tràn ra"
    ],
    "dang_trai_phang_hinh_khong_gian": [
        "phương pháp trải phẳng", "quãng đường ngắn nhất trên bề mặt", "con kiến bò trên mặt hình hộp",
        "con kiến bò quanh hình nón", "con kiến bò quanh hình trụ", "quấn dây đèn LED quanh cột trụ",
        "quấn dây đèn quanh kim tự tháp", "quấn dây quanh cây thông Noel", "con thằn lằn bò trên tường",
        "khai triển mặt xung quanh hình nón thành hình quạt", "trải phẳng lăng trụ"
    ],
    "dang_cap_so_cong_cap_so_nhan": [
        "cấp số cộng", "công sai d", "số hạng tổng quát u_n", "tổng n số hạng S_n",
        "cấp số nhân", "công bội q", "tổng cấp số nhân lùi vô hạn",
        "xếp ghế hội trường nhà hát", "xếp hộp sữa hình tháp", "giá khoan giếng theo mét sâu",
        "bài toán hạt thóc trên bàn cờ vua", "quả bóng cao su nảy lên chạm đất", "tam giác Sierpinski"
    ],

    # 7. MÔ HÌNH HÓA KINH TẾ, QUY HOẠCH TUYẾN TÍNH & TỐC ĐỘ BIẾN THIÊN
    "dang_thuc_te_kinh_te_vi_mo": [
        "hàm chi phí", "hàm doanh thu", "hàm lợi nhuận", "hàm giá",
        "chi phí biên", "doanh thu biên", "thuế xả thải", "hạn ngạch sản xuất", "lợi nhuận ròng sau thuế",
        "chi phí sản xuất bình quân", "hàm cầu tuyến tính", "giảm giá bán tăng số lượng tiêu thụ",
        "tối ưu số máy móc sản xuất và chi phí giám sát", "tối ưu số lô hàng nhập kho",
        "thuế phụ thu tối đa hóa doanh thu nhà nước", "hàm sản xuất Cobb-Douglas", "bán buffet hải sản"
    ],
    "dang_quy_hoach_tuyen_tinh": [
        "quy hoạch tuyến tính", "hệ bất phương trình bậc nhất hai ẩn", "miền nghiệm đa giác",
        "tối ưu hóa nguồn lực sản xuất", "bài toán khẩu phần dinh dưỡng protein lipid",
        "phân bổ diện tích trồng trọt", "phân bổ giờ máy và nhân công", "lợi nhuận lớn nhất trên miền đa giác"
    ],
    "dang_thuc_te_toc_do_bien_thien": [
        "tốc độ biến thiên liên hệ", "Related Rates", "tốc độ thay đổi diện tích",
        "bóng của đĩa tròn", "nguồn sáng điểm chiếu bóng", "tốc độ dâng lên của mực nước",
        "cái thang trượt dọc theo bức tường", "hai thùng hàng nối qua ròng rọc",
        "tốc độ thay đổi khoảng cách giữa hai phương tiện", "tốc độ tan chảy của lớp băng trên quả cầu"
    ]
}

# ==============================================================================
# CẤU HÌNH ƯU TIÊN VẬN DỤNG CAO (VDC) & THỰC TẾ (REAL-WORLD) THEO GEMINI.MD
# ==============================================================================
# Các chủ đề bắt buộc lấy ở mức Vận dụng cao (9+) cho Phần II và Phần III
VDC_CORE_TOPICS = {
    "dang_ham_so_tiem_can_phan_thuc",
    "dang_ham_so_toi_uu_thuc_te",
    "dang_thuc_te_kinh_te_vi_mo",
    "dang_quy_hoach_tuyen_tinh",
    "dang_thuc_te_toc_do_bien_thien",
    "dang_mu_logarit_thuc_te",
    "dang_tich_phan_dien_tich_the_tich",
    "dang_tich_phan_dong_hoc",
    "dang_oxyz_can_bang_luc_vat_ly",
    "dang_oxyz_cuc_tri_khoang_cach",
    "dang_oxyz_mo_hinh_hoa_thuc_te",
    "dang_oxyz_mat_cau",
    "dang_xac_suat_co_dieu_kien_bayes",
    "dang_xac_suat_nang_cao_euler",
    "dang_to_hop_quy_tac_dem",
    "dang_trai_phang_hinh_khong_gian",
    "dang_hinh_khong_gian_goc_khoang_cach",
    "dang_thong_ke_do_phan_tan",
}

# Tín hiệu nhận diện bài toán Thực tế / Vận dụng cao chất lượng
REAL_WORLD_BOOST_KEYWORDS = [
    "thực tế", "chi phí", "lợi nhuận", "doanh thu", "ngắn nhất", "nhỏ nhất", "lớn nhất",
    "tối ưu", "thiết kế", "xây dựng", "bể chứa", "vận tốc", "gia tốc", "quãng đường",
    "flycam", "drone", "vệ tinh", "ra đa", "radar", "máy bay", "tàu", "ô tô",
    "lực căng", "hợp lực", "trọng lượng", "dây cáp", "con kiến", "trải phẳng",
    "xét nghiệm", "dương tính", "phế phẩm", "xác suất có điều kiện", "bayes",
    "triệu đồng", "nghìn đồng", "mét khối", "lãi suất", "dân số", "vi khuẩn",
    "trả lời ngắn", "kq:", "trả lời:", "làm tròn"
]

# Các mẫu câu CẤM hoặc HẠN CHẾ theo GEMINI.md (Hàm hợp g(x)=f(u(x)), Tích phân hàm ẩn máy móc, trang lý thuyết suông)
BANNED_OR_PENALIZED_PATTERNS = [
    r"f\s*\(\s*\|x\|\s*\)",
    r"f\s*\(\s*x\s*[\+\-]\s*\d+\s*\)",
    r"f\s*\(\s*f\s*\(",
    r"f'\s*\(\s*x\s*\)\s*f''\s*\(\s*x\s*\)",
    r"phương trình vi phân bernoulli",
    r"nhân tử tích phân",
    r"lý thuyết cần nhớ",
    r"bảng giá trị lượng giác một số góc đặc biệt"
]


MATHTYPE_SYMBOL_MAP = {
    0xf028: '(', 0xf029: ')', 0xf02b: '+', 0xf02d: '-', 0xf03d: '=',
    0xf03c: '<', 0xf03e: '>', 0xf02f: '/', 0xf03a: ':', 0xf03b: ';',
    0xf05b: '[', 0xf05d: ']', 0xf07b: '{', 0xf07d: '}',
    0xf0e9: '[', 0xf0ea: '[', 0xf0eb: '[',
    0xf0f9: ']', 0xf0fa: ']', 0xf0fb: ']',
    0xf0e6: '(', 0xf0e7: '(', 0xf0e8: '(',
    0xf0f6: ')', 0xf0f7: ')', 0xf0f8: ')',
    0xf0ec: '{', 0xf0ed: '{', 0xf0ee: '{', 0xf0ef: '{',
    0xf0fc: '}', 0xf0fd: '}', 0xf0fe: '}',
    0xf8f1: '{', 0xf8f2: '{', 0xf8f3: '{', 0xf8f4: '|',
    0xf0a2: "'", 0x2032: "'", 0x2212: '-',
    0xf070: 'pi', 0xf0a5: ' vô cùng ', 0xf0b0: '°',
    0xf0a3: '<=', 0xf0b3: '>=', 0xf0b9: '!=', 0xf0bb: '~=',
    0xf0de: ' => ', 0xf0db: ' <=> ', 0xf0ae: ' -> ',
    0xf0b7: ' · ', 0xf0d7: ' × ', 0xf0f2: ' tích phân ',
    0xf0a1: ' R ', 0xf0ce: ' Z ', 0xf057: ' Omega ',
    0xf044: ' Delta ', 0xf05e: ' vuông góc ', 0xf0d8: ' góc ',
    0xf055: ' hợp ', 0xf0c7: ' giao ',
    0xf061: ' alpha ', 0xf062: ' beta ', 0xf06f: ' omega ',
    0xf063: '[ ]', 0xf040: ' ', 0xf075: '', 0xf072: ''
}

VNI_COMMON_MAP = {
    "Nguyeãn Tieán Haø": "Nguyễn Tiến Hà",
    "Nguyeãn": "Nguyễn", "Tieán": "Tiến", "Haø": "Hà",
    "phöông trình": "phương trình", "baát phöông trình": "bất phương trình",
    "heä phöông trình": "hệ phương trình",
    "löôïng giaùc": "lượng giác", "cô baûn": "cơ bản",
    "ñaïo haøm": "đạo hàm", "nguyeân haøm": "nguyên hàm", "tích phaân": "tích phân",
    "ñoà thò": "đồ thị", "haøm soá": "hàm số", "hàm soá": "hàm số",
    "bieán thieân": "biến thiên", "ñoàng bieán": "đồng biến", "nghòch bieán": "nghịch biến",
    "cöïc trò": "cực trị", "cöïc ñaïi": "cực đại", "cöïc tieåu": "cực tiểu",
    "giaù trò": "giá trị", "lôùn nhaát": "lớn nhất", "nhoû nhaát": "nhỏ nhất",
    "tieäm caän": "tiệm cận", "ñöùng": "đứng", "xieân": "xiên",
    "khoaûng": "khoảng", "ñoaïn": "đoạn", "taäp xaùc ñònh": "tập xác định",
    "dieän tích": "diện tích", "theå tích": "thể tích", "hình phaúng": "hình phẳng",
    "xaùc suaát": "xác suất", "toå hôïp": "tổ hợp",
    "maët phaúng": "mặt phẳng", "ñöôøng thaúng": "đường thẳng", "khoaûng caùch": "khoảng cách",
    "toïa ñoä": "tọa độ", "vectô": "vectơ", "maët caàu": "mặt cầu",
    "tam giaùc": "tam giác", "töù dieän": "tứ diện", "hình choùp": "hình chóp",
    "hình laêng truï": "hình lăng trụ", "hình hoäp": "hình hộp",
    "caáp soá coäng": "cấp số cộng", "caáp soá nhaân": "cấp số nhân",
    "phöông sai": "phương sai", "ñoä leäch chuaån": "độ lệch chuẩn",
    "trung vò": "trung vị", "moát": "mốt", "töù phaân vò": "tứ phân vị",
    "nghieäm": "nghiệm", "coù": "có", "baèng": "bằng", "ñöôïc": "được",
    "ñuùng": "đúng"
}


def clean_mathtype_symbols(text: str) -> str:
    """Lọc và chuẩn hóa các ký hiệu lỗi font MathType, Symbol, VNI sang ký tự toán học chuẩn."""
    if not text:
        return ""

    for vni_k, vni_v in VNI_COMMON_MAP.items():
        if vni_k in text:
            text = text.replace(vni_k, vni_v)

    text = re.sub(r'[\uf0e9\uf0ea\uf0eb]+', '[', text)
    text = re.sub(r'[\uf0f9\uf0fa\uf0fb]+', ']', text)
    text = re.sub(r'[\uf0e6\uf0e7\uf0e8]+', '(', text)
    text = re.sub(r'[\uf0f6\uf0f7\uf0f8]+', ')', text)
    text = re.sub(r'[\uf0ec\uf0ed\uf0ee\uf0ef\uf8f1\uf8f2\uf8f3]+', '{', text)
    text = re.sub(r'[\uf0fc\uf0fd\uf0fe]+', '}', text)

    res = []
    for ch in text:
        code = ord(ch)
        if code in MATHTYPE_SYMBOL_MAP:
            res.append(MATHTYPE_SYMBOL_MAP[code])
        elif 0xf020 <= code <= 0xf07e:
            res.append(chr(code - 0xf000))
        elif 0xf000 <= code <= 0xf8ff:
            res.append(" ")
        else:
            res.append(ch)
    cleaned = "".join(res)

    cleaned = re.sub(r'([\-0-9a-zA-Z\+;\.e\u03c0]+(?:;[\-0-9a-zA-Z\+;\.e\u03c0]+)?)\s*(?:\[\s*\])+', r'[\1]', cleaned)
    cleaned = re.sub(r'\[\s*\n\s*\]', '', cleaned)
    cleaned = re.sub(r'\(\s*\n\s*\)', '', cleaned)
    cleaned = re.sub(r'\{\s*\n\s*\}', '', cleaned)
    cleaned = re.sub(r'^\s*(\[\]|\(\)|\{\})\s*\.?$', '', cleaned, flags=re.MULTILINE)

    cleaned = re.sub(r'[ \t]+', ' ', cleaned)
    cleaned = re.sub(r' +([,;:.\)\]])', r'\1', cleaned)
    cleaned = re.sub(r'([\(\[]) +', r'\1', cleaned)
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
    return cleaned


def classify_topics(text: str) -> list[str]:
    lower = text.lower()
    matched = [
        topic for topic, kws in TOPIC_KEYWORDS.items()
        if any(kw.lower() in lower for kw in kws)
    ]
    return matched or ["general"]


def compute_vdc_score(chunk: dict) -> float:
    """
    Chấm điểm độ 'Chất' (Vận dụng cao & Thực tế chuẩn GDPT 2018) cho từng đoạn văn bản:
    - Cộng điểm lớn nếu nguồn nằm trong các file Vận dụng cao, Toán thực tế, Trải phẳng, Xác suất.
    - Cộng điểm theo mật độ từ khóa thực tế/tối ưu và cấu trúc câu hỏi Phần II (Đúng/Sai), Phần III (Trả lời ngắn).
    - Phạt nặng nếu chứa Hàm hợp g(x)=f(u(x)), Tích phân hàm ẩn máy móc, hoặc chỉ toàn công thức lý thuyết suông.
    """
    text = chunk.get("text", "")
    lower = text.lower()
    src = chunk.get("source", "").lower()
    score = 1.0

    # 1. Điểm thưởng theo Nguồn tài liệu VIP
    if any(k in src for k in ["vận dụng cao", "toán thực tế", "trải phẳng", "xác suất", "sáng kiến", "vdc"]):
        score += 6.0
    elif "chuyên đề" in src or "tổng ôn" in src:
        score += 2.5

    # 2. Điểm thưởng theo mật độ từ khóa Thực tế & Tối ưu
    rw_hits = sum(1 for kw in REAL_WORLD_BOOST_KEYWORDS if kw in lower)
    score += min(rw_hits * 1.5, 12.0)

    # 3. Điểm thưởng nếu là Câu hỏi Phần II (Đúng/Sai a, b, c, d) hoặc Phần III (Trả lời ngắn)
    if re.search(r"\ba\)\s+.*\bb\)\s+.*\bc\)\s+", lower, flags=re.DOTALL):
        score += 3.5
    if any(k in lower for k in ["phần iii", "trả lời ngắn", "kq:", "trả lời:", "làm tròn đến", "làm tròn kết quả"]):
        score += 4.0

    # 4. Điểm thưởng nếu chứa câu hỏi thực sự (Câu 1, Câu 2...)
    if re.search(r"\bcâu\s+\d+", lower):
        score += 2.0
    else:
        score -= 3.0  # Trang chỉ có lý thuyết/công thức không có bài tập

    # 5. Phạt nặng các mẫu câu vi phạm GEMINI.md (Hàm hợp, Tích phân hàm ẩn cũ, Bảng lý thuyết)
    for pat in BANNED_OR_PENALIZED_PATTERNS:
        if re.search(pat, lower):
            score -= 10.0

    return round(max(0.1, score), 2)


def get_keywords_hash() -> str:
    payload = {
        "kw": TOPIC_KEYWORDS,
        "boost": REAL_WORLD_BOOST_KEYWORDS,
        "banned": BANNED_OR_PENALIZED_PATTERNS
    }
    raw = json.dumps(payload, sort_keys=True, ensure_ascii=False)
    return hashlib.md5(raw.encode("utf-8")).hexdigest()


def print_topic_distribution(chunks: list[dict]):
    print("\n" + "=" * 84)
    print("THỐNG KÊ PHÂN BỐ CÁC CHUYÊN ĐỀ & SỐ LƯỢNG ĐOẠN VDC CHẤT LƯỢNG CAO (SCORE >= 8.0):")
    print("=" * 84)
    topic_counts = {t: 0 for t in TOPIC_KEYWORDS}
    vdc_counts = {t: 0 for t in TOPIC_KEYWORDS}
    topic_counts["general"] = 0

    for ch in chunks:
        sc = ch.get("vdc_score", compute_vdc_score(ch))
        for t in ch.get("topics", []):
            topic_counts[t] = topic_counts.get(t, 0) + 1
            if sc >= 8.0:
                vdc_counts[t] = vdc_counts.get(t, 0) + 1

    idx = 1
    for t in TOPIC_KEYWORDS:
        cnt = topic_counts.get(t, 0)
        v_cnt = vdc_counts.get(t, 0)
        tag = "[VDC CORE]" if t in VDC_CORE_TOPICS else "          "
        print(f" {idx:2d}. {t:<38} {tag}: {cnt:4d} đoạn (VDC thực tế: {v_cnt:4d})")
        idx += 1
    print(f" -- Khác (general)                                : {topic_counts.get('general', 0):4d} đoạn")
    print("=" * 84 + "\n")


def extract_pdf(file_path: Path, rel_path: str) -> list[dict]:
    chunks = []
    if os.path.isdir(DEFAULT_TESSDATA):
        os.environ["TESSDATA_PREFIX"] = DEFAULT_TESSDATA

    if HAS_PYMUPDF:
        try:
            doc = pymupdf.open(str(file_path))
            for i in range(len(doc)):
                page = doc[i]
                txt = (page.get_text() or "").strip()
                is_ocr = False
                if len(txt) <= 40:
                    try:
                        tp = page.get_textpage_ocr(language="vie+eng", dpi=200, full=True)
                        txt = (page.get_text(textpage=tp) or "").strip()
                        is_ocr = True
                    except Exception as ocr_err:
                        print(f"[WARN] Lỗi OCR {rel_path} trang {i+1}: {ocr_err}")
                if len(txt) > 40:
                    chunks.append({
                        "source": rel_path,
                        "location": f"page_{i+1}" + ("_ocr" if is_ocr else ""),
                        "text": txt
                    })
            doc.close()
        except Exception as e:
            print(f"[WARN] Lỗi đọc PDF (PyMuPDF) {rel_path}: {e}")
    else:
        try:
            reader = PdfReader(str(file_path))
            for i, page in enumerate(reader.pages):
                txt = (page.extract_text() or "").strip()
                if len(txt) > 40:
                    chunks.append({
                        "source": rel_path,
                        "location": f"page_{i+1}",
                        "text": txt
                    })
        except Exception as e:
            print(f"[WARN] Lỗi đọc PDF {rel_path}: {e}")
    return chunks


def extract_docx(file_path: Path, rel_path: str) -> list[dict]:
    chunks = []
    try:
        with zipfile.ZipFile(file_path) as zf:
            xml_content = zf.read("word/document.xml")
        tree = ET.fromstring(xml_content)
        paragraphs = []
        for elem in tree.iter():
            if elem.tag.endswith("}p"):
                texts = [t.text for t in elem.iter() if t.tag.endswith("}t") and t.text]
                line = "".join(texts).strip()
                if line:
                    paragraphs.append(line)
        step = 15
        for idx in range(0, len(paragraphs), step):
            block = "\n".join(paragraphs[idx:idx + step]).strip()
            if len(block) > 40:
                chunks.append({
                    "source": rel_path,
                    "location": f"para_{idx+1}_{min(idx+step, len(paragraphs))}",
                    "text": block
                })
    except Exception as e:
        print(f"[WARN] Lỗi đọc DOCX {rel_path}: {e}")
    return chunks


def extract_text_file(file_path: Path, rel_path: str) -> list[dict]:
    chunks = []
    try:
        content = file_path.read_text(encoding="utf-8", errors="ignore")
        blocks = re.split(r"(?=\\item|\bCâu\s+\d+)", content)
        if len(blocks) <= 2:
            blocks = [content[i:i+2000] for i in range(0, len(content), 2000)]
        for i, b in enumerate(blocks):
            b = b.strip()
            if len(b) > 40:
                chunks.append({
                    "source": rel_path,
                    "location": f"block_{i+1}",
                    "text": b[:2500]
                })
    except Exception as e:
        print(f"[WARN] Lỗi đọc file text {rel_path}: {e}")
    return chunks


def process_single_file(file_path_str: str, rel_path: str) -> tuple[str, list[dict]]:
    """Worker chạy song song trên từng tiến trình để bóc tách (hoặc OCR) 1 file."""
    f = Path(file_path_str)
    ext = f.suffix.lower()
    if ext == ".pdf":
        c = extract_pdf(f, rel_path)
    elif ext == ".docx":
        c = extract_docx(f, rel_path)
    else:
        c = extract_text_file(f, rel_path)
    for item in c:
        item["text"] = clean_mathtype_symbols(item["text"])
        item["topics"] = classify_topics(item["text"])
        item["vdc_score"] = compute_vdc_score(item)
    return rel_path, c


def sync_index(force_reindex: bool = False, max_workers: int | None = None, reclassify: bool = False) -> list[dict]:
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    INDEX_DIR.mkdir(parents=True, exist_ok=True)

    current_keywords_hash = get_keywords_hash()
    old_keywords_hash = ""
    old_catalog = {}
    old_chunks_by_source = {}

    if not force_reindex and CATALOG_PATH.exists() and CHUNKS_PATH.exists():
        try:
            cat_data = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
            old_keywords_hash = cat_data.get("keywords_hash", "")
            for item in cat_data.get("files", []):
                old_catalog[item["file"]] = item
            for line in CHUNKS_PATH.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    ch = json.loads(line)
                    old_chunks_by_source.setdefault(ch["source"], []).append(ch)
        except Exception:
            old_catalog = {}
            old_chunks_by_source = {}

    keywords_changed = bool(old_keywords_hash != current_keywords_hash)
    if keywords_changed or reclassify:
        print("[TOPIC & VDC SCORE UPDATE] Đang cập nhật lại nhãn chuyên đề và chấm điểm VDC Thực tế...")

    current_files = sorted([
        p for p in SOURCE_DIR.rglob("*")
        if p.is_file() and p.suffix.lower() in SUPPORTED_EXTS and "_index" not in p.parts
    ])

    files_to_scan = []
    file_meta = {}
    chunks_by_rel = {}
    reused_count = 0

    for f in current_files:
        rel_path = str(f.relative_to(SOURCE_DIR))
        stat = f.stat()
        mtime = round(stat.st_mtime, 2)
        size = stat.st_size
        file_meta[rel_path] = (f, mtime, size)

        cached = old_catalog.get(rel_path)
        if (
            not force_reindex
            and cached
            and cached.get("mtime") == mtime
            and cached.get("size") == size
            and cached.get("num_chunks", 0) > 0
        ):
            c_list = old_chunks_by_source.get(rel_path, [])
            for item in c_list:
                item["text"] = clean_mathtype_symbols(item.get("text", ""))
                if keywords_changed or reclassify or "vdc_score" not in item:
                    item["topics"] = classify_topics(item.get("text", ""))
                    item["vdc_score"] = compute_vdc_score(item)
            chunks_by_rel[rel_path] = c_list
            reused_count += 1
        else:
            files_to_scan.append((str(f), rel_path))

    scanned_count = len(files_to_scan)
    if scanned_count > 0:
        workers = max_workers or min(scanned_count, max(1, (os.cpu_count() or 4) - 2))
        if scanned_count == 1 or workers == 1:
            for f_str, rel_path in files_to_scan:
                _, c = process_single_file(f_str, rel_path)
                chunks_by_rel[rel_path] = c
                print(f"  -> [1/1] Xong: {rel_path} ({len(c)} đoạn)")
        else:
            print(f"[PARALLEL OCR/EXTRACT] Đang chạy song song trên {workers} luồng để xử lý {scanned_count} file...")
            done_files = 0
            with ProcessPoolExecutor(max_workers=workers) as executor:
                futures = [executor.submit(process_single_file, f_str, rel_path) for f_str, rel_path in files_to_scan]
                for fut in as_completed(futures):
                    rel_path, c = fut.result()
                    chunks_by_rel[rel_path] = c
                    done_files += 1
                    print(f"  -> [{done_files}/{scanned_count}] Xong: {rel_path} ({len(c)} đoạn)")

    new_catalog = []
    all_chunks = []
    for f in current_files:
        rel_path = str(f.relative_to(SOURCE_DIR))
        _, mtime, size = file_meta[rel_path]
        c = chunks_by_rel.get(rel_path, [])
        all_chunks.extend(c)
        new_catalog.append({
            "file": rel_path,
            "type": f.suffix.lower(),
            "mtime": mtime,
            "size": size,
            "num_chunks": len(c)
        })

    should_rewrite = (
        force_reindex
        or scanned_count > 0
        or keywords_changed
        or reclassify
        or len(new_catalog) != len(old_catalog)
        or not CATALOG_PATH.exists()
    )

    if should_rewrite:
        CATALOG_PATH.write_text(json.dumps({
            "keywords_hash": current_keywords_hash,
            "total_files": len(new_catalog),
            "total_chunks": len(all_chunks),
            "files": new_catalog
        }, ensure_ascii=False, indent=2), encoding="utf-8")

        with CHUNKS_PATH.open("w", encoding="utf-8") as out:
            for idx, ch in enumerate(all_chunks):
                ch["chunk_id"] = idx
                out.write(json.dumps(ch, ensure_ascii=False) + "\n")

        reasons = []
        if scanned_count > 0:
            reasons.append(f"xử lý mới {scanned_count} file")
        if keywords_changed or reclassify:
            reasons.append("chấm điểm VDC & phân loại lại theo chuẩn GEMINI.md")
        if reused_count > 0:
            reasons.append(f"tái sử dụng {reused_count} file cũ")
        print(f"[INDEX] Hoàn tất ({', '.join(reasons)}) -> Tổng: {len(all_chunks)} phân đoạn.")
    else:
        print(f"[CACHE HIT] Đọc trực tiếp từ chỉ mục có sẵn ({len(new_catalog)} file, {len(all_chunks)} phân đoạn).")

    return all_chunks


def weighted_sample_vdc(rng: random.Random, pool: list[dict], k: int, prefer_vdc: bool = True) -> list[dict]:
    """
    Lấy mẫu k phần tử không hoàn lại nhưng ƯU TIÊN MẠNH các đoạn có vdc_score cao (nằm trong file VDC, Toán thực tế, Trải phẳng).
    Loại bỏ các đoạn bị phạt điểm (chứa hàm hợp hoặc chỉ có lý thuyết suông).
    """
    if not pool:
        return []

    # Lọc bỏ các đoạn bị phạt nặng (vdc_score <= 1.0) nếu trong pool có đủ câu tốt
    clean_pool = [c for c in pool if c.get("vdc_score", 1.0) > 1.5]
    if len(clean_pool) >= k:
        pool = clean_pool

    if prefer_vdc:
        # Sắp xếp giảm dần theo vdc_score và chỉ lấy trong Top 35% đoạn chất nhất (tối thiểu 12 đoạn để đảm bảo đa dạng giữa các đề)
        sorted_pool = sorted(pool, key=lambda x: x.get("vdc_score", 1.0), reverse=True)
        top_n = max(k * 4, min(len(sorted_pool), max(12, int(len(sorted_pool) * 0.35))))
        candidates = sorted_pool[:top_n]
    else:
        candidates = list(pool)

    selected = []
    available = list(candidates)
    for _ in range(min(k, len(available))):
        # Trọng số bậc 2 theo vdc_score để câu thực tế/VDC có xác suất trúng áp đảo
        weights = [(c.get("vdc_score", 1.0) ** 2) if prefer_vdc else 1.0 for c in available]
        chosen = rng.choices(available, weights=weights, k=1)[0]
        selected.append(chosen)
        available.remove(chosen)

    return selected


def sample_part3_hard_sources(chunks: list[dict], rng: random.Random) -> list[dict]:
    selected = []
    for source in PART3_HARD_SOURCES:
        pool = [c for c in chunks if Path(c["source"]).name == source and c.get("vdc_score", 1.0) > 1.5]
        selected.extend(weighted_sample_vdc(rng, pool, k=2, prefer_vdc=True))
    if len(selected) < 2:
        raise ValueError("Không đủ 2 đoạn ngữ liệu từ ba tài liệu bắt buộc cho Phần III; cần bổ sung/kiểm tra chỉ mục trước khi tạo mẫu đề.")
    return selected


def sample_for_new_exam(exam_num: int, per_topic: int = 2, force_reindex: bool = False, reclassify: bool = False):
    all_chunks = sync_index(force_reindex=force_reindex, reclassify=reclassify)
    if not all_chunks:
        print(f"[INFO] Thư mục {SOURCE_DIR} hiện chưa có file tài liệu nào.")
        return

    rng = random.Random(exam_num * 2027)
    vdc_sampled = {}
    base_sampled = {}

    for topic in TOPIC_KEYWORDS:
        pool = [c for c in all_chunks if topic in c.get("topics", [])]
        if not pool:
            continue
        if topic in VDC_CORE_TOPICS:
            # Với các chủ đề VDC & Thực tế: Bốc 3 đoạn mỗi chủ đề và ép lấy từ nhóm điểm VDC cao nhất!
            vdc_sampled[topic] = weighted_sample_vdc(rng, pool, k=per_topic + 1, prefer_vdc=True)
        else:
            # Với các chủ đề nền tảng (cho Phần I): Bốc 2 đoạn nhưng vẫn lọc sạch lý thuyết suông & hàm hợp
            base_sampled[topic] = weighted_sample_vdc(rng, pool, k=per_topic, prefer_vdc=False)

    hard_sampled = sample_part3_hard_sources(all_chunks, rng) if exam_num >= 13 else []
    out_file = INDEX_DIR / f"sample_de_{exam_num}.md"
    lines = [
        f"# NGUỒN THAM KHẢO TỰ ĐỘNG CHO ĐỀ SỐ {exam_num} (ƯU TIÊN VẬN DỤNG CAO & THỰC TẾ 9+)\n",
        "> **CHỈ THỊ BẮT BUỘC CHO AGENT (THEO GEMINI.MD):**",
        "> 1. **Tuyệt đối không dùng hàm hợp $g(x)=f(u(x))$** hoặc tích phân hàm ẩn máy móc. Nếu trong đoạn trích có xuất hiện câu hàm hợp (do nằm chung trang PDF), hãy BỎ QUA câu đó và chỉ lấy câu Thực tế / Phân thức bậc 2 trên bậc 1 / Tối ưu.",
        "> 2. **Khu vực I chứa ngữ liệu Vận dụng cao & Mô hình hóa thực tế**. Dùng để chế tác **4 câu Phần II (Đúng/Sai)**, ngữ liệu Phần III và 3 câu phân loại cuối Phần I.\n",
    ]

    if hard_sampled:
        lines.extend([
            "> 3. **PHẦN III LÀ PHẦN CHẶN ĐIỂM: ít nhất 2/6 câu khó phải lấy hoặc chế tác từ đúng ba tài liệu ở Khu vực 0.** Giữ nút thắt/độ khó gốc; không giản lược thành bài thay công thức. Hai đoạn của cùng một bài chỉ tính là 1 câu. Mở trang PDF gốc để xác nhận dữ kiện/hình; ghi số câu, tên file, trang PDF và nút thắt vào hồ sơ nguồn, kiểm đủ ít nhất 2 câu trước khi xuất đề. Điểm VDC chỉ hỗ trợ chọn ngữ liệu, không xác nhận độ khó.\n",
            "---\n",
            "# KHU VỰC 0: NGUỒN BẮT BUỘC CHO ÍT NHẤT 2 CÂU KHÓ PHẦN III\n",
            *[f"- `{source}`" for source in PART3_HARD_SOURCES],
            "\nCác đoạn dưới đây là ứng viên tham khảo; đọc PDF gốc để chọn bài đầy đủ và đủ khó.\n",
        ])
        for it in hard_sampled:
            lines.append(f"### Nguồn: `{it['source']}` ({it['location']}) — `[VDC Score: {it['vdc_score']}]`")
            lines.extend(["```text", clean_mathtype_symbols(it["text"]), "```\n"])

    lines.extend([
        "---\n",
        "# KHU VỰC I: NGỮ LIỆU TRỌNG TÂM VẬN DỤNG CAO & TOÁN THỰC TẾ (DÙNG CHO PHẦN II & PHẦN III)\n",
    ])

    for topic, items in vdc_sampled.items():
        lines.append(f"## Chủ đề VDC: `{topic}`")
        for it in items:
            sc = it.get("vdc_score", 0)
            lines.append(f"### Nguồn: `{it['source']}` ({it['location']}) — `[VDC Score: {sc}]`")
            lines.append("```text")
            # Nâng giới hạn lên 2200 ký tự cho các đoạn VDC để không bị cắt cụt đề bài toán thực tế dài!
            lines.append(clean_mathtype_symbols(it["text"][:2200]))
            lines.append("```\n")

    lines.append("---\n")
    lines.append("# KHU VỰC II: NGỮ LIỆU NỀN TẢNG & VẬN DỤNG (DÙNG CHO PHẦN I - TRẮC NGHIỆM 12 CÂU)\n")

    for topic, items in base_sampled.items():
        lines.append(f"## Chủ đề: `{topic}`")
        for it in items:
            lines.append(f"### Nguồn: `{it['source']}` ({it['location']})")
            lines.append("```text")
            lines.append(clean_mathtype_symbols(it["text"][:1500]))
            lines.append("```\n")

    out_file.write_text("\n".join(lines), encoding="utf-8")
    print(f"[OK] Đã trích xuất ngữ liệu ƯU TIÊN VDC cho Đề {exam_num} tại: {out_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--exam", type=int, default=None, help="Số thứ tự đề cần lấy mẫu ngữ liệu từ chỉ mục có sẵn")
    parser.add_argument("--reindex", action="store_true", help="Ép quét lại toàn bộ kho tài liệu từ đầu")
    parser.add_argument("--reclassify", action="store_true", help="Ép phân loại và chấm điểm VDC lại toàn bộ các đoạn")
    parser.add_argument("--workers", type=int, default=None, help="Số luồng chạy song song")
    parser.add_argument("--source-dir", type=Path, help="Quét kho nguồn riêng; ghi _index ngay trong kho đó, không lấy mẫu đề THPTQG")
    args = parser.parse_args()

    if args.source_dir is not None:
        if args.exam is not None:
            parser.error("--exam chỉ dùng với kho THPTQG mặc định; kho học kì cần chọn ngữ liệu theo phạm vi riêng.")
        if not args.source_dir.is_dir():
            parser.error(f"Kho nguồn không tồn tại hoặc không phải thư mục: {args.source_dir}")
        SOURCE_DIR = args.source_dir.resolve()
        INDEX_DIR = SOURCE_DIR / "_index"
        CATALOG_PATH = INDEX_DIR / "catalog.json"
        CHUNKS_PATH = INDEX_DIR / "extracted_chunks.jsonl"

    if args.exam is not None:
        sample_for_new_exam(args.exam, force_reindex=args.reindex, reclassify=args.reclassify)
    else:
        chunks = sync_index(force_reindex=args.reindex, max_workers=args.workers, reclassify=args.reclassify)
        print_topic_distribution(chunks)
