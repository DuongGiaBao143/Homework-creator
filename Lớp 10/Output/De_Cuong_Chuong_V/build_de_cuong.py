"""Soạn hai bản LaTeX cho đề cương Chương V, Toán 10."""
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP, localcontext
from fractions import Fraction as F
from pathlib import Path
from statistics import median


def viet(value, digits=None):
    value = F(value)
    with localcontext() as ctx:
        ctx.prec = 40
        number = Decimal(value.numerator) / Decimal(value.denominator)
        if digits is not None:
            number = number.quantize(Decimal(10) ** -digits, rounding=ROUND_HALF_UP)
        return format(number, "f").replace(".", "{,}")


def avg(values):
    return F(sum(values), len(values))


def variance(values):
    mean = avg(values)
    return sum((x - mean) ** 2 for x in values) / len(values)


def quartiles(values):
    values = sorted(map(F, values))
    mid = len(values) // 2
    return median(values[:mid]), median(values), median(values[-mid:])


def iqr(values):
    lo, _, hi = quartiles(values)
    return hi - lo


def outliers(values):
    lo, _, hi = quartiles(values)
    fence = F(3, 2) * (hi - lo)
    return [x for x in values if x < lo - fence or x > hi + fence]


def deviation(values, digits):
    value = variance(values)
    with localcontext() as ctx:
        ctx.prec = 40
        return viet((Decimal(value.numerator) / value.denominator).sqrt(), digits)


def mode(values):
    counts = Counter(values)
    modes = [x for x, f in counts.items() if f == max(counts.values())]
    assert len(modes) == 1
    return modes[0]


def sample(*values):
    return "$" + r";\ ".join(str(x) for x in values) + "$"


def frequencies(values, counts):
    return (r"\(\begin{array}{c|" + "c" * len(values)
            + r"}\text{Giá trị}&" + "&".join(map(str, values))
            + r"\\\hline\text{Tần số}&" + "&".join(map(str, counts))
            + r"\end{array}\)")


def expand(values, counts):
    return [x for x, count in zip(values, counts, strict=True) for _ in range(count)]


questions = []


def add(question, answer, reason, digits=None):
    answer = answer if isinstance(answer, str) else viet(answer, digits)
    questions.append((question, answer, reason))


# Bài 12
add(r"Chiều dài chính xác của một đoạn dây là $18{,}762$ m. Người đo ghi $18{,}8$ m. Tính sai số tuyệt đối của số ghi được (m).",
    abs(F("18.8") - F("18.762")), r"$|18{,}762-18{,}8|=0{,}038$.")
add(r"Một phép đo cho kết quả $24{,}36\pm0{,}04$ cm. Tìm cận dưới của chiều dài thật (cm).",
    F("24.36") - F("0.04"), r"$24{,}36-0{,}04=24{,}32$.")
add(r"Một thùng hàng có khối lượng $8{,}25\pm0{,}06$ kg. Tìm cận trên của khối lượng thật (kg).",
    F("8.25") + F("0.06"), r"$8{,}25+0{,}06=8{,}31$.")
add(r"Quy tròn số $56{,}7856$ đến hàng phần trăm.",
    F("56.7856"), r"Chữ số hàng phần nghìn là $5$ nên tăng chữ số hàng phần trăm từ $8$ lên $9$.", 2)
add(r"Quy tròn số $48\,746$ đến hàng trăm.",
    48700, r"Chữ số hàng chục là $4$ nên giữ nguyên chữ số hàng trăm.")
add(r"Khi quy tròn một độ dài đến hàng phần mười của mét, sai số tuyệt đối không vượt quá bao nhiêu mét?",
    F("0.1") / 2, r"Nửa đơn vị của hàng làm tròn là $0{,}1/2=0{,}05$.")
add(r"Giá trị chính xác là $201$ m, số gần đúng là $200$ m. Tính sai số tương đối theo phần trăm, lấy sai số tuyệt đối chia cho độ lớn của số gần đúng.",
    abs(201 - 200) * F(100, 200), r"$\dfrac{|201-200|}{200}\cdot100=0{,}5$.")
add(r"Biết khối lượng $12{,}5$ kg có độ chính xác $0{,}05$ kg. Tính cận trên của sai số tương đối theo phần trăm bằng tỉ số giữa độ chính xác và số gần đúng.",
    F("0.05") / F("12.5") * 100, r"$\dfrac{0{,}05}{12{,}5}\cdot100=0{,}4$.")
add(r"Số $a=347\,562$ có độ chính xác $d=240$. Viết số quy tròn của $a$ theo quy tắc chọn hàng thấp nhất có đơn vị lớn hơn $d$.",
    348000, r"$100<240<1000$, nên quy tròn đến hàng nghìn.")
add(r"Một sân hình chữ nhật có chiều dài $20\pm0{,}2$ m và chiều rộng $12\pm0{,}1$ m. Tính cận trên của diện tích sân (m$^2$).",
    (20 + F("0.2")) * (12 + F("0.1")), r"Hai độ dài đều dương. Cận trên là $20{,}2\cdot12{,}1=244{,}42$.")

# Bài 13
data = [7, 12, 9, 8, 14]
add(r"Tính số trung bình của mẫu " + sample(*data) + ".", avg(data), r"$50/5=10$.")
data = [18, 11, 14, 22, 12]
add(r"Tính trung vị của mẫu " + sample(*data) + ".", median(data), r"Thứ tự tăng dần là $11;12;14;18;22$, giá trị giữa bằng $14$.")
data = [14, 7, 9, 21, 15, 10]
add(r"Tính trung vị của mẫu " + sample(*data) + ".", median(data), r"Hai giá trị giữa là $10$ và $14$, lấy trung bình được $12$.")
data = [3, 7, 3, 4, 7, 3, 9, 4]
add(r"Tìm mốt của mẫu " + sample(*data) + ".", mode(data), r"Giá trị $3$ xuất hiện $3$ lần, nhiều nhất.")
values, counts = [1, 2, 3, 4], [2, 3, 4, 1]
add(r"Tính số trung bình của mẫu cho bởi bảng tần số sau. " + frequencies(values, counts),
    avg(expand(values, counts)), r"$\dfrac{1\cdot2+2\cdot3+3\cdot4+4\cdot1}{10}=2{,}4$.")
values, counts = [2, 4, 6, 9], [3, 2, 4, 1]
add(r"Tính trung vị của mẫu cho bởi bảng tần số sau. " + frequencies(values, counts),
    median(expand(values, counts)), r"Các vị trí thứ $5$ và $6$ lần lượt là $4$ và $6$, nên trung vị bằng $5$.")
values, counts = [10, 15, 20, 25], [4, 6, 3, 2]
add(r"Tìm mốt của mẫu cho bởi bảng tần số sau. " + frequencies(values, counts),
    mode(expand(values, counts)), r"Tần số lớn nhất là $6$, ứng với giá trị $15$.")
data = [3, 5, 6, 8, 10, 11, 15]
add(r"Tìm tứ phân vị thứ nhất $Q_1$ của mẫu " + sample(*data) + ".", quartiles(data)[0],
    r"Bỏ trung vị $8$, nửa dưới là $3;5;6$ nên $Q_1=5$.")
data = [2, 4, 7, 9, 10, 13, 17, 21]
add(r"Tìm tứ phân vị thứ ba $Q_3$ của mẫu " + sample(*data) + ".", quartiles(data)[2],
    r"Nửa trên là $10;13;17;21$ nên $Q_3=(13+17)/2=15$.")
add(r"Mẫu số liệu gồm $6;8;10;x;14$ có số trung bình bằng $10$. Tìm $x$.",
    5 * 10 - sum([6, 8, 10, 14]), r"Tổng mẫu bằng $50$, tổng bốn giá trị đã biết bằng $38$.")
add(r"Một lớp có $40$ học sinh. Điểm trung bình cả lớp là $7{,}6$. Trong đó, $25$ học sinh nam có điểm trung bình là $7{,}36$. Tính điểm trung bình của $15$ học sinh nữ.",
    (40 * F("7.6") - 25 * F("7.36")) / 15, r"Tổng điểm của các bạn nữ là $40\cdot7{,}6-25\cdot7{,}36=120$, chia $15$ được $8$.")
add(r"Một mẫu có $10$ giá trị, số trung bình đang ghi là $18$. Kiểm tra thấy một giá trị $26$ bị nhập nhầm thành $16$. Tính số trung bình sau khi sửa.",
    F(10 * 18 + 26 - 16, 10), r"Tổng đúng là $180-16+26=190$.")
add(r"Chín thời gian đi học (phút) đã sắp theo thứ tự không giảm là $12;15;15;18;x;22;24;25;28$, có trung vị $20$. Thêm một quan sát $21$ phút. Tính trung vị của mẫu mới (phút).",
    median(map(F, [12, 15, 15, 18, 20, 22, 24, 25, 28, 21])), r"$x=20$. Sau khi thêm $21$, hai giá trị giữa là $20$ và $21$, trung vị bằng $20{,}5$.")
add(r"Mẫu đã sắp tăng dần $2;5;7;9;12;14;x;20;25$ có $Q_3=18$. Tìm $x$.",
    2 * 18 - 20, r"Nửa trên là $14;x;20;25$ nên $(x+20)/2=18$, suy ra $x=16$.")
add(r"Một cửa hàng bán áo cỡ S, M, L lần lượt được $14$, $23$, $17$ chiếc trong tuần. Cỡ nào là mốt của mẫu dữ liệu về cỡ áo?",
    r"\text{M}", r"Cỡ M có tần số $23$, lớn nhất trong ba cỡ.")

# Bài 14
data = [14, 26, 11, 18, 23, 19]
add(r"Tính khoảng biến thiên của mẫu " + sample(*data) + ".", max(data) - min(data), r"$26-11=15$.")
data = [2, 5, 6, 8, 11, 12, 15]
add(r"Tính khoảng tứ phân vị của mẫu " + sample(*data) + ".", iqr(data), r"$Q_1=5$, $Q_3=12$, hiệu bằng $7$.")
data = [2, 4, 6, 8, 10]
add(r"Tính phương sai $s^2$ của mẫu " + sample(*data) + ".", variance(data), r"$\bar x=6$, tổng bình phương độ lệch là $40$, chia $5$ được $8$.")
data = [9, 9, 13, 13]
add(r"Tính độ lệch chuẩn $s$ của mẫu " + sample(*data) + ".", deviation(data, 0), r"$\bar x=11$, mỗi bình phương độ lệch bằng $4$, nên $s=\sqrt4=2$.")
data = [12, 14, 16, 16, 17]
add(r"Tính độ lệch chuẩn $s$ của mẫu " + sample(*data) + r". Làm tròn đến hàng phần trăm.",
    deviation(data, 2), r"$\bar x=15$, $s^2=(9+1+1+1+4)/5=3{,}2$, nên $s\approx1{,}79$.")
values, counts = [0, 1, 2, 3], [1, 3, 3, 1]
add(r"Tính phương sai của mẫu cho bởi bảng tần số sau. " + frequencies(values, counts),
    variance(expand(values, counts)), r"$\bar x=1{,}5$, tổng bình phương độ lệch có tính tần số bằng $6$, chia $8$ được $0{,}75$.")
data = [2, 5, 6, 7, 8, 8, 9, 10, 30]
add(r"Mẫu " + sample(*data) + r" có đúng một giá trị ngoại lệ theo quy tắc $1{,}5\Delta_Q$. Tìm giá trị đó.",
    outliers(data)[0], r"$Q_1=5{,}5$, $Q_3=9{,}5$, cận trên bằng $15{,}5$. Chỉ $30$ nằm ngoài hai cận.")
data = [2, 3, 10, 11, 12, 13, 13, 14, 15, 25, 28]
add(r"Mẫu " + sample(*data) + r" có bao nhiêu quan sát ngoại lệ theo quy tắc $1{,}5\Delta_Q$?",
    len(outliers(data)), r"$Q_1=10$, $Q_3=15$, hai cận là $2{,}5$ và $22{,}5$. Ngoại lệ là $2;25;28$.")
add(r"Một mẫu có $Q_1=20$ và $Q_3=28$. Tính cận trên dùng để phát hiện giá trị ngoại lệ.",
    28 + F(3, 2) * (28 - 20), r"$28+1{,}5(28-20)=40$.")
add(r"Một mẫu có $Q_1=12$ và $Q_3=18$. Tính cận dưới dùng để phát hiện giá trị ngoại lệ.",
    12 - F(3, 2) * (18 - 12), r"$12-1{,}5(18-12)=3$.")
add(r"Mẫu đã sắp tăng dần $7;9;11;14;x$ có khoảng biến thiên $13$. Tìm $x$.",
    7 + 13, r"$x-7=13$, nên $x=20$.")
add(r"Mẫu đã sắp tăng dần $3;5;6;9;11;x;17;20$ có khoảng tứ phân vị $9$. Tìm $x$.",
    int(2 * (9 + F(5 + 6, 2)) - 17), r"$Q_1=5{,}5$, $Q_3=14{,}5$, nên $(x+17)/2=14{,}5$ và $x=12$.")
add(r"Một mẫu gồm $4;4;4;4;4$. Tính độ lệch chuẩn của mẫu.",
    deviation([4] * 5, 0), r"Mọi giá trị bằng số trung bình nên $s^2=0$ và $s=0$.")
add(r"Hai máy đóng gói có cùng khối lượng trung bình mỗi gói. Độ lệch chuẩn của máy 1 là $1{,}6$ g, của máy 2 là $2{,}1$ g. Theo độ lệch chuẩn, máy số mấy đóng gói đồng đều hơn?",
    1, r"Máy 1 có độ lệch chuẩn nhỏ hơn.")
add(r"Điểm kiểm tra của năm học sinh là $6;7;8;9;x$. Biết điểm trung bình bằng $8$. Tính phương sai của mẫu.",
    variance([6, 7, 8, 9, 5 * 8 - 6 - 7 - 8 - 9]), r"$x=10$. Tổng bình phương độ lệch là $4+1+0+1+4=10$, chia $5$ được $2$.")

# Bài tập tổng hợp
add(r"Điểm của $8$ học sinh có trung bình $7{,}5$. Sau khi thêm một học sinh, trung bình của $9$ em là $7{,}6$. Tính điểm của học sinh được thêm.",
    9 * F("7.6") - 8 * F("7.5"), r"$9\cdot7{,}6-8\cdot7{,}5=8{,}4$.")
add(r"Mẫu đã sắp tăng dần $3;7;9;13;15;18;x$ có số trung bình bằng trung vị. Tìm $x$.",
    7 * 13 - sum([3, 7, 9, 13, 15, 18]), r"Trung vị là $13$. Tổng mẫu bằng $91$, tổng sáu số đã biết bằng $65$, suy ra $x=26$.")
data = [5, 6, 7, 7, 8, 9, 30]
add(r"Từ mẫu " + sample(*data) + r", bỏ quan sát ngoại lệ theo quy tắc $1{,}5\Delta_Q$. Tính số trung bình của mẫu còn lại.",
    avg([x for x in data if x not in outliers(data)]), r"$Q_1=6$, $Q_3=9$, cận trên $13{,}5$. Bỏ $30$, trung bình còn lại là $42/6=7$.")
add(r"Khối lượng của bốn mẫu vật (gam) là $10;14;x;y$ với $x<y$. Mẫu số liệu có số trung bình $15$ và phương sai $13$. Tìm $y$.",
    20, r"$x+y=36$ và $(x-15)^2+(y-15)^2=26$. Do đó $(y-x)^2=2\cdot26-(36-30)^2=16$. Từ $y-x=4$ suy ra $y=20$.")
add(r"Một mẫu thời gian tính bằng phút có phương sai $0{,}04$ phút$^2$. Tính độ lệch chuẩn của mẫu theo đơn vị giây.",
    12, r"$s=\sqrt{0{,}04}=0{,}2$ phút, tức $12$ giây.")
data = [8, 9, 10, 10, 11, 12]
add(r"Mẫu thời gian chờ ban đầu là " + sample(*data) + r" phút. Mỗi thời gian tăng thêm $3$ phút. Tính phương sai của mẫu mới, làm tròn đến hàng phần trăm.",
    variance([x + 3 for x in data]), r"Cộng cùng một số vào mọi giá trị giữ nguyên độ lệch quanh trung bình. $s^2=10/6\approx1{,}67$.", 2)
add(r"Điểm của hai nhóm là $5;7;7;9$ và $6;6;8;8$. Tính phương sai của nhóm thứ nhất trừ phương sai của nhóm thứ hai.",
    variance([5, 7, 7, 9]) - variance([6, 6, 8, 8]), r"Cả hai trung bình đều bằng $7$. Phương sai lần lượt là $2$ và $1$.")
add(r"Mẫu $8;9;11;14;18$ có một giá trị bị nhập sai. Sau khi sửa giá trị $18$, số trung bình tăng đúng $0{,}8$. Tính khoảng biến thiên của mẫu đã sửa.",
    18 + F("0.8") * 5 - 8, r"Giá trị đúng là $18+5\cdot0{,}8=22$. Khoảng biến thiên là $22-8=14$.")
values, counts = [2, 3, 4, 5, 6], [4, 6, 20 - 4 - 6 - 3 - 2, 3, 2]
add(r"Số ca làm trong tuần của $20$ nhân viên được cho bởi bảng tần số sau. Tính khoảng tứ phân vị của mẫu (ca). "
    + frequencies(values, [4, 6, "m", 3, 2]),
    iqr(expand(values, counts)), r"$m=5$. Trong mẫu đã sắp xếp, $Q_1=(3+3)/2=3$ và $Q_3=(4+5)/2=4{,}5$.")
add(r"Mẫu $10;12;14;16$ có số trung bình $\bar x$. Thêm một quan sát bằng $\bar x$ vào mẫu. Tính phương sai của mẫu mới.",
    variance([10, 12, 13, 14, 16]), r"$\bar x=13$ giữ nguyên. Tổng bình phương độ lệch bằng $20$, chia $5$ được $4$.")

assert len(questions) == 50
assert quartiles([2, 5, 6, 8, 11, 12, 15]) == (5, 8, 12)
assert outliers([2, 3, 10, 11, 12, 13, 13, 14, 15, 25, 28]) == [2, 25, 28]
assert variance([10, 12, 13, 14, 16]) == 4
assert avg([10, 14, 16, 20]) == 15 and variance([10, 14, 16, 20]) == 13

PREAMBLE = r"""
\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage[vietnamese]{babel}
\usepackage[margin=1.45cm,includeheadfoot,headheight=18pt,headsep=7pt,footskip=18pt]{geometry}
\usepackage{amsmath,amssymb,array,fancyhdr,tikz,xcolor}
\definecolor{ink}{RGB}{30,55,70}
\definecolor{gridline}{RGB}{218,228,233}
\pagestyle{fancy}
\fancyhf{}
\lhead{\small\bfseries LÀM TOÁN ĐỂ HẠNH PHÚC}
\rhead{\small\itshape Người biên soạn: Dương Gia Bảo}
\rfoot{\small Trang \thepage}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\newcommand{\banner}[1]{\par\medskip{\large\bfseries\color{ink}#1}\par\smallskip}
\newcommand{\grid}[1]{%
  \begin{tikzpicture}
    \draw[step=5mm,gridline,line width=.25pt] (0,0) grid (\linewidth,#1);
    \draw[gridline,line width=.5pt] (0,0) rectangle (\linewidth,#1);
  \end{tikzpicture}}
\newcommand{\question}[2]{%
  \begin{minipage}{\linewidth}
    \textbf{Câu #1.} #2\par\smallskip
    \grid{2.5cm}\par\nobreak\smallskip
    \hfill\textit{Đáp số:}\ \fbox{\rule{0pt}{10pt}\hspace{2.75cm}}\par
  \end{minipage}\par}
\newcommand{\solution}[3]{%
  \begin{minipage}{\linewidth}
    \textbf{Câu #1.}\ \textbf{Đáp số} \(\boxed{#2}\).\quad #3
  \end{minipage}\par\medskip}
\begin{document}
"""

chapters = {0: "Bài 12. Số gần đúng và sai số",
            10: "Bài 13. Các số đặc trưng đo xu thế trung tâm",
            25: "Bài 14. Các số đặc trưng đo độ phân tán",
            40: "Bài tập tổng hợp Chương V"}


def title(heading):
    return (r"\begin{center}{\LARGE\bfseries\color{ink}" + heading
            + r"}\\[4pt]{\large\bfseries TOÁN 10 \enspace|\enspace CHƯƠNG V}"
            + r"\\[4pt]Các số đặc trưng của mẫu số liệu không ghép nhóm\end{center}" + "\n")


def render(answers=False):
    body = [PREAMBLE, title("ĐÁP ÁN VÀ HƯỚNG DẪN" if answers else "ĐỀ CƯƠNG ÔN TẬP")]
    if not answers:
        body += [r"\textbf{Họ và tên:} \dotfill\quad \textbf{Lớp:} \makebox[2.8cm]{\dotfill}" "\n",
                 r"\par\smallskip 50 câu trả lời ngắn. Ghi một đáp số cho mỗi câu. "
                 r"Phương sai chia cho $n$. Khi $n$ lẻ, bỏ trung vị chung trước khi lấy trung vị hai nửa." "\n"]
    for index, (question, answer, reason) in enumerate(questions):
        if answers:
            if index in chapters:
                body.append(r"\banner{" + chapters[index] + "}\n")
            body.append(r"\solution{" + f"{index + 1}" + "}{" + answer + "}{" + reason + "}\n")
        else:
            if index % 5 == 0:
                if index:
                    body.append(r"\newpage" "\n")
                chapter = chapters[max(start for start in chapters if start <= index)]
                body.append(r"\banner{" + chapter + "}\n")
            else:
                body.append(r"\vfill" "\n")
            body.append(r"\question{" + f"{index + 1}" + "}{" + question + "}\n")
    return "".join(body) + r"\end{document}" + "\n"


if __name__ == "__main__":
    directory = Path(__file__).resolve().parent
    for name, answers in (("De_Cuong_Chuong_V", False), ("De_Cuong_Chuong_V_Ans", True)):
        (directory / f"{name}.tex").write_text(render(answers), encoding="utf-8")
