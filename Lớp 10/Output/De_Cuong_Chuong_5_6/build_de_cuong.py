import os
import re
import shutil
import subprocess
from pathlib import Path
import pymupdf

OUT_DIR = Path(r"d:\Tao_De\Lớp 10\Output\De_Cuong_Chuong_5_6")
TEX_PATH = OUT_DIR / "De_Cuong_Chuong_5_6.tex"
FULL_PDF = OUT_DIR / "De_Cuong_Chuong_5_6.pdf"
EXAM_PDF = OUT_DIR / "De_Cuong.pdf"
ANS_PDF = OUT_DIR / "De_Cuong_Ans.pdf"

EXPORT_TARGETS = [
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Đề cương ôn tập Chương 5 và 6.pdf"), "exam"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Đề cương ôn tập Chương 5 và 6 (Đáp án).pdf"), "ans"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương V - VI\Đề cương ôn tập Chương 5 và 6.pdf"), "exam"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương V - VI\Đề cương ôn tập Chương 5 và 6 (Đáp án).pdf"), "ans"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương V - VI\De_Cuong_Chuong_5_6.pdf"), "exam"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương V - VI\De_Cuong_Chuong_5_6_Ans.pdf"), "ans"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\Chương V - VI\De_Cuong_Chuong_5_6.pdf"), "exam"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\Chương V - VI\De_Cuong_Chuong_5_6_Ans.pdf"), "ans"),
]

QUOTES = [
    r"Mathematics is about understanding, not just numbers",
    r"The essence of mathematics lies in its freedom",
    r"Pure mathematics is the poetry of logical ideas",
    r"In mathematics, asking good questions matters most",
    r"Everything around you is built on mathematics",
    r"Mathematics is the queen of the sciences",
    r"Stay with tough problems a little bit longer",
    r"Math gives us hope that every problem has a solution",
    r"Success is the sum of small daily efforts",
    r"Think deeply, check carefully, solve cleanly",
    r"Genius is 1\% inspiration and 99\% perspiration",
    r"Practice makes perfect — keep solving!",
]


def build_header_quote_macro(max_pages: int = 45) -> str:
    lines = [r"\newcommand{\headerQuote}{%", r"  \ifcase\numexpr\value{page}-1\relax"]
    lines.append(f"    {QUOTES[0]}%")
    for i in range(1, max_pages):
        q = QUOTES[i % len(QUOTES)]
        lines.append(f"  \\or {q}%")
    lines.append(r"  \else Practice makes perfect — keep solving!%")
    lines.append(r"  \fi")
    lines.append(r"}")
    return "\n".join(lines)


PREAMBLE = r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage[vietnamese]{babel}
\usepackage[margin=1.3cm,top=0.8cm,bottom=1.0cm,includehead,includefoot,headheight=18pt,headsep=6pt,footskip=16pt]{geometry}
\usepackage{amsmath,amssymb,array,tabularx,enumitem,fancyhdr,tikz,xcolor,needspace,multicol}
\usetikzlibrary{calc,angles,quotes,arrows.meta,babel,patterns}

\definecolor{ink}{RGB}{30,55,70}
\definecolor{accent}{RGB}{18,82,112}
\definecolor{gridline}{RGB}{185,212,224}
\definecolor{gridborder}{RGB}{115,160,180}

\setlength{\parindent}{0pt}
\setlength{\parskip}{2pt}

__HEADER_QUOTE__

\pagestyle{fancy}
\fancyhf{}
\lhead{\footnotesize\textit{\color{gray!70!black}\headerQuote}}
\rhead{\small\textbf{\color{ink}Người biên soạn: Dương Gia Bảo}}
\lfoot{}
\rfoot{\small Trang \thepage/__EXAM_PAGES__}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}

\fancypagestyle{dapan}{
  \fancyhf{}
  \lhead{\footnotesize\textit{\color{gray!70!black}\headerQuote}}
  \rhead{\small\textbf{\color{ink}Người biên soạn: Dương Gia Bảo}}
  \lfoot{\small\textit{\color{gray!60!black}Đáp án Đề cương Ôn tập Chương V \& VI — Toán 10 KNTT}}
  \rfoot{\small Trang \thepage/__ANS_PAGES__}
  \renewcommand{\headrulewidth}{0.4pt}
  \renewcommand{\footrulewidth}{0pt}
}

\newcommand{\chapterbanner}[2]{%
  \par\vspace{4pt}\noindent
  \begin{tikzpicture}
    \node[draw=accent, fill=accent!6, rounded corners=4pt, inner xsep=10pt, inner ysep=6pt, text width=\dimexpr\linewidth-20.8pt\relax, line width=0.8pt] {%
      {\large\bfseries\color{ink}#1}\\[2pt]
      {\small\color{gray!75!black}#2}%
    };
  \end{tikzpicture}\par\nopagebreak\vspace{5pt}
}

\newcommand{\parttitle}[1]{\par\vspace{3pt}\needspace{3\baselineskip}{\normalsize\bfseries\color{accent}#1}\par\nopagebreak\vspace{2pt}}
\newcommand{\answerbox}{%
  {\unskip\nobreak\hfil\penalty50\hskip1.2em\hbox{}\nobreak\hfil
  \mbox{\textit{Đáp số:}\ \fbox{\rule{0pt}{8.5pt}\hspace{2.2cm}}}%
  \parfillskip=0pt\finalhyphendemerits=0\par}%
}

\setlist[enumerate,1]{label=\textbf{Câu \arabic*.},leftmargin=1.15cm,labelsep=.15cm,itemsep=2pt,topsep=2pt,parsep=0pt}

\newcommand{\oli}[1]{%
  \par\nopagebreak\vspace{2.5pt}\noindent
  \begin{tikzpicture}
    \draw[step=0.5cm, color=cyan!25!gray!25, line width=0.25pt] (0,0) grid (\linewidth, #1);
    \draw[color=cyan!50!gray!45, line width=0.45pt, rounded corners=2pt] (0,0) rectangle (\linewidth, #1);
    \node[anchor=north west, font=\scriptsize\itshape\color{gray!75}, inner sep=3pt] at (0, #1) {Bài làm:};
  \end{tikzpicture}\par\vspace{3.5pt}
}

\newcolumntype{C}[1]{>{\centering\arraybackslash}m{#1}}
\newcolumntype{Y}{>{\centering\arraybackslash}X}
"""

TIKZ_Q26 = r"""\begin{tikzpicture}[scale=0.56, >=stealth]
  \draw[step=1, color=gray!22, line width=0.2pt] (-3.5,-2.5) grid (4.5,4.5);
  \draw[->, line width=0.6pt] (-3.8,0) -- (5.0,0) node[below, font=\scriptsize] {$x$};
  \draw[->, line width=0.6pt] (0,-2.8) -- (0,5.0) node[right, font=\scriptsize] {$y$};
  \node[below right, font=\scriptsize] at (0,0) {$O$};
  % dashed projections
  \draw[dashed, gray!70, line width=0.4pt] (-3,0) -- (-3,1) -- (0,1);
  \draw[dashed, gray!70, line width=0.4pt] (-1,0) -- (-1,4) -- (0,4);
  \draw[dashed, gray!70, line width=0.4pt] (2,0) -- (2,-2) -- (0,-2);
  \draw[dashed, gray!70, line width=0.4pt] (4,0) -- (4,3) -- (0,3);
  % polyline
  \draw[accent, line width=1.25pt] (-3,1) -- (-1,4) -- (2,-2) -- (4,3);
  \foreach \x/\y in {-3/1, -1/4, 2/-2, 4/3} {
    \fill[accent] (\x,\y) circle (2.8pt);
  }
  % tick labels avoiding graph overlaps
  \node[below, font=\scriptsize] at (-3,0) {$-3$};
  \node[below, font=\scriptsize] at (-1,0) {$-1$};
  \node[above, font=\scriptsize] at (2,0) {$2$};
  \node[below, font=\scriptsize] at (4,0) {$4$};
  \node[left, font=\scriptsize] at (0,-2) {$-2$};
  \node[left, font=\scriptsize] at (0,1) {$1$};
  \node[right, font=\scriptsize] at (0,3) {$3$};
  \node[right, font=\scriptsize] at (0,4) {$4$};
\end{tikzpicture}"""

TIKZ_Q37 = r"""\begin{tikzpicture}[scale=0.52, >=stealth]
  \draw[step=1, color=gray!20, line width=0.2pt] (-2,-4.5) grid (4,2);
  \draw[->, line width=0.6pt] (-2.3,0) -- (4.3,0) node[below left, font=\scriptsize] {$x$};
  \draw[->, line width=0.6pt] (0,-4.7) -- (0,2.3) node[below right, font=\scriptsize] {$y$};
  \node[below left, font=\scriptsize] at (0,0) {$O$};
  \draw[dashed, gray!70, line width=0.4pt] (1,0) -- (1,-4) -- (0,-4);
  \draw[accent, line width=1.2pt, domain=-1.55:3.55, smooth, samples=60] plot (\x, {\x*\x - 2*\x - 3});
  \fill[accent] (1,-4) circle (2.8pt) node[below right, font=\scriptsize, black] {$I$};
  \fill[accent] (-1,0) circle (2.4pt);
  \fill[accent] (3,0) circle (2.4pt);
  \fill[accent] (0,-3) circle (2.4pt);
  \node[below left, font=\scriptsize] at (-1,0) {$-1$};
  \node[above, font=\scriptsize] at (1,0) {$1$};
  \node[below right, font=\scriptsize] at (3,0) {$3$};
  \node[left, font=\scriptsize] at (0,-3) {$-3$};
  \node[left, font=\scriptsize] at (0,-4) {$-4$};
\end{tikzpicture}"""

TIKZ_Q67 = r"""\begin{tikzpicture}[scale=0.58]
  \coordinate (A) at (0,2.8);
  \coordinate (B) at (0,0);
  \coordinate (M) at (2.1,0);
  \coordinate (C) at (5.0,0);
  % Sea background hint
  \fill[cyan!8] (-0.5,0) rectangle (5.4,3.1);
  \draw[line width=0.9pt, accent] (-0.5,0) -- (5.4,0);
  \draw (B) -- (A);
  \draw[dashed, red!75!black, line width=0.9pt] (A) -- (M);
  \draw[line width=1.3pt, orange!80!black] (M) -- (C);
  % right angle
  \draw (0,0.35) -- (0.35,0.35) -- (0.35,0);
  \fill (A) circle (2.4pt) node[above, font=\scriptsize] {$A$ (Hải đăng)};
  \fill (B) circle (2.4pt) node[below, font=\scriptsize] {$B$};
  \fill (M) circle (2.4pt) node[below, font=\scriptsize] {$M$};
  \fill (C) circle (2.4pt) node[below, font=\scriptsize] {$C$};
  \node[left, font=\scriptsize] at (0,1.4) {$4\text{ km}$};
  \node[below, font=\scriptsize] at (2.5,-0.55) {Bờ biển $BC = 7\text{ km}$};
\end{tikzpicture}"""

TIKZ_Q68 = r"""\begin{tikzpicture}[scale=0.56]
  \coordinate (A) at (0,2.4);
  \coordinate (H) at (0,0);
  \coordinate (M) at (2.4,0);
  \coordinate (B) at (5.2,0);
  \fill[cyan!8] (-0.4,0) rectangle (5.6,2.4);
  \draw[line width=0.8pt, accent] (-0.4,2.4) -- (5.6,2.4);
  \draw[line width=0.8pt, accent] (-0.4,0) -- (5.6,0);
  \draw (H) -- (A);
  \draw[dashed, red!75!black, line width=0.95pt] (A) -- (M);
  \draw[line width=1.3pt, orange!80!black] (M) -- (B);
  \draw (0,0.35) -- (0.35,0.35) -- (0.35,0);
  \fill (A) circle (2.4pt) node[above, font=\scriptsize] {$A$};
  \fill (H) circle (2.4pt) node[below, font=\scriptsize] {$H$};
  \fill (M) circle (2.4pt) node[below, font=\scriptsize] {$M$};
  \fill (B) circle (2.4pt) node[below, font=\scriptsize] {$B$};
  \node[left, font=\scriptsize] at (0,1.2) {$3\text{ km}$};
  \node[below, font=\scriptsize] at (2.6,-0.55) {$HB = 8\text{ km}$};
\end{tikzpicture}"""

TIKZ_Q70 = r"""\begin{tikzpicture}[scale=0.43, >=stealth]
  \draw[->] (-4.6,0) -- (5.2,0) node[below, font=\scriptsize] {$x$};
  \draw[->] (0,-0.4) -- (0,9.7) node[right, font=\scriptsize] {$y$};
  \draw[accent, line width=1.15pt, domain=-4:4, smooth, samples=50] plot (\x, {8 - 0.5*\x*\x});
  \fill[accent!10, draw=red!75!black, line width=0.9pt] (-2,0) rectangle (2,6);
  \node[below, font=\scriptsize] at (-2,0) {$M$};
  \node[below, font=\scriptsize] at (2,0) {$N$};
  \node[above right, font=\scriptsize] at (2,6) {$P$};
  \node[above left, font=\scriptsize] at (-2,6) {$Q$};
  \node[below, font=\scriptsize] at (-4,0) {$-4$};
  \node[below, font=\scriptsize] at (4,0) {$4$};
  \node[above right, font=\scriptsize] at (0,8) {$8$};
\end{tikzpicture}"""

TIKZ_ANS_Q18 = r"""\begin{tikzpicture}[scale=0.70]
  \draw[->, line width=0.6pt] (1.0,0) -- (9.3,0);
  \foreach \x in {1.8, 3.6, 4.8, 5.2, 5.6, 6.8, 8.5} {
    \draw (\x,0.08) -- (\x,-0.08);
  }
  \fill[cyan!15, draw=accent, line width=0.8pt] (4.8,0.4) rectangle (5.6,0.9);
  \draw[line width=1.1pt, red!75!black] (5.2,0.4) -- (5.2,0.9);
  \draw[dashed] (3.6,0.65) -- (4.8,0.65);
  \draw[dashed] (5.6,0.65) -- (6.8,0.65);
  \draw (3.6,0.45) -- (3.6,0.85);
  \draw (6.8,0.45) -- (6.8,0.85);
  \fill[red] (1.8,0.65) circle (2.5pt) node[above=2pt, font=\scriptsize] {$1{,}8$ (Bất thường)};
  \fill[red] (8.5,0.65) circle (2.5pt) node[above=2pt, font=\scriptsize] {$8{,}5$ (Bất thường)};
  \node[below, font=\scriptsize] at (1.8,-0.1) {$1{,}8$};
  \node[below, font=\scriptsize] at (3.6,-0.1) {$3{,}6$};
  \node[below, font=\scriptsize] at (4.8,-0.1) {$4{,}8$};
  \node[below, font=\scriptsize] at (5.6,-0.1) {$5{,}6$};
  \node[below, font=\scriptsize] at (6.8,-0.1) {$6{,}8$};
  \node[below, font=\scriptsize] at (8.5,-0.1) {$8{,}5$};
\end{tikzpicture}"""

TIKZ_ANS_Q69 = r"""\begin{tikzpicture}[scale=0.45, >=stealth]
  \draw[->] (-6,0) -- (6,0) node[below, font=\scriptsize] {$x$};
  \draw[->] (0,-0.8) -- (0,8.2) node[right, font=\scriptsize] {$y$};
  \draw[accent, line width=1.2pt] (5,0) arc (0:180:5);
  \draw[red!75!black, line width=0.9pt, domain=-5.5:2.5] plot (\x, {\x + 5}) node[right, font=\scriptsize] {$m=5$};
  \draw[orange!85!black, line width=0.9pt, dashed, domain=-5.5:1.2] plot (\x, {\x + 7.07}) node[right, font=\scriptsize] {$m=5\sqrt{2}$};
  \fill[accent] (-5,0) circle (2.4pt) node[below, font=\scriptsize] {$-5$};
  \fill[accent] (5,0) circle (2.4pt) node[below, font=\scriptsize] {$5$};
  \fill[accent] (0,5) circle (2.4pt) node[below right, font=\scriptsize] {$5$};
\end{tikzpicture}"""


def side_by_side(text_tex: str, tikz_tex: str, text_ratio: float = 0.65) -> str:
    fig_ratio = round(0.97 - text_ratio, 2)
    return (
        f"\\begin{{minipage}}[t]{{{text_ratio}\\linewidth}}\n"
        f"{text_tex}\n"
        f"\\end{{minipage}}\\hfill\n"
        f"\\begin{{minipage}}[t]{{{fig_ratio}\\linewidth}}\n"
        f"\\vspace{{-6pt}}\\centering\n"
        f"{tikz_tex}\n"
        f"\\end{{minipage}}"
    )


def get_questions():
    # Tuple structure: (section_header_or_None, text_tex, oli_height, break_before_bool)
    qs = [
        # ==================== CHƯƠNG V: CÂU 1 - 20 ====================
        (r"\parttitle{Chủ đề 1. Số gần đúng và sai số (Bài 12)}",
         r"Dân số của một tỉnh theo số liệu thống kê được làm tròn với độ chính xác $d = 300$ là $\bar{a} = 148\,372 \pm 300$ (người). Hãy viết số quy tròn của số gần đúng $a = 148\,372$.\answerbox",
         "3.0cm", False),
        (None,
         r"Cho số gần đúng $a = 24{,}7684$ với độ chính xác $d = 0{,}02$. Hãy viết số quy tròn của số gần đúng $a$.\answerbox",
         "3.0cm", False),
        (None,
         r"Một mảnh đất hình chữ nhật có chiều dài và chiều rộng đo được lần lượt là $x = 12 \pm 0{,}1\text{ (m)}$ và $y = 5 \pm 0{,}1\text{ (m)}$. Khi đó diện tích đúng $\bar{S}$ của mảnh đất thỏa mãn $\bar{S} \in [m; n]$. Tính giá trị của $n - m$.\answerbox",
         "3.0cm", False),
        (None,
         r"Một nhóm học sinh đo chiều cao của một tháp truyền hình được kết quả $h = 80 \pm 0{,}4\text{ (m)}$. Sai số tương đối tối đa của phép đo trên bằng bao nhiêu phần trăm (chỉ viết số, không ghi kí hiệu $\%$)?\answerbox",
         "3.0cm", False),

        # Page break after Q4 -> Q5, Q6, Q7
        (None,
         r"Một học sinh viết giá trị gần đúng của phân số $\dfrac{5}{8}$ là $0{,}6$. Tính sai số tuyệt đối của số gần đúng này.\answerbox",
         "5.5cm", True),
        (r"\parttitle{Chủ đề 2. Các số đặc trưng đo xu thế trung tâm (Bài 13)}",
         r"Điểm kiểm tra $15$ phút môn Toán của $8$ học sinh tổ 1 lần lượt là: $7;\; 8;\; 6;\; 9;\; x;\; 8;\; 7;\; 9$. Biết điểm trung bình của cả tổ là $7{,}75$. Tìm giá trị của $x$.\answerbox",
         "5.5cm", False),
        (None,
         r"""Thống kê thời gian tự học mỗi ngày (đơn vị: giờ) của $40$ học sinh lớp 10A thu được bảng tần số sau:
\begin{center}
\vspace{-4pt}
\begin{tabular}{|l|C{1.1cm}|C{1.1cm}|C{1.1cm}|C{1.1cm}|C{1.1cm}|}
\hline
\textbf{Số giờ} & $1$ & $2$ & $3$ & $4$ & $5$ \\ \hline
\textbf{Số học sinh} & $4$ & $10$ & $16$ & $8$ & $2$ \\ \hline
\end{tabular}
\vspace{-4pt}
\end{center}
Tính thời gian tự học trung bình mỗi ngày của một học sinh lớp 10A (đơn vị: giờ).\answerbox""",
         "5.5cm", False),

        # Page break -> Q8, Q9, Q10
        (None,
         r"Thời gian chạy cự li $100\text{ m}$ (đơn vị: giây) của $10$ vận động viên lần lượt được ghi lại như sau: $11{,}8;\; 12{,}4;\; 11{,}5;\; 13{,}0;\; 12{,}1;\; 11{,}9;\; 12{,}6;\; 12{,}2;\; 11{,}7;\; 12{,}8$. Tìm trung vị $M_e$ của mẫu số liệu trên.\answerbox",
         "5.5cm", True),
        (None,
         r"""Khảo sát số lỗi chính tả trong một bài viết văn của $35$ học sinh, giáo viên thu được bảng thống kê sau:
\begin{center}
\vspace{-4pt}
\begin{tabular}{|l|C{1.0cm}|C{1.0cm}|C{1.0cm}|C{1.0cm}|C{1.0cm}|C{1.0cm}|}
\hline
\textbf{Số lỗi} & $0$ & $1$ & $2$ & $3$ & $4$ & $5$ \\ \hline
\textbf{Số bài viết} & $5$ & $8$ & $9$ & $7$ & $4$ & $2$ \\ \hline
\end{tabular}
\vspace{-4pt}
\end{center}
Tìm trung vị $M_e$ của mẫu số liệu trên.\answerbox""",
         "5.5cm", False),
        (None,
         r"Cho mẫu số liệu thống kê sản lượng chè (tạ) thu hoạch trong $11$ ngày của một nông trại: $24;\; 19;\; 32;\; 27;\; 21;\; 35;\; 29;\; 25;\; 30;\; 22;\; 28$. Tìm tứ phân vị thứ ba $Q_3$ của mẫu số liệu trên.\answerbox",
         "5.5cm", False),

        # Page break -> Q11, Q12, Q13
        (None,
         r"Điểm thi học kì môn Tiếng Anh của $12$ học sinh được thống kê như sau: $6{,}5;\; 7{,}0;\; 5{,}5;\; 8{,}0;\; 7{,}5;\; 6{,}0;\; 8{,}5;\; 9{,}0;\; 7{,}0;\; 6{,}5;\; 8{,}0;\; 7{,}5$. Tính giá trị của $Q_1 + Q_3$, với $Q_1, Q_3$ lần lượt là tứ phân vị thứ nhất và thứ ba của mẫu số liệu.\answerbox",
         "5.5cm", True),
        (None,
         r"""Một cửa hàng thống kê cỡ giày thể thao nam đã bán trong một tháng theo bảng sau:
\begin{center}
\vspace{-4pt}
\begin{tabular}{|l|C{1.0cm}|C{1.0cm}|C{1.0cm}|C{1.0cm}|C{1.0cm}|C{1.0cm}|}
\hline
\textbf{Cỡ giày} & $37$ & $38$ & $39$ & $40$ & $41$ & $42$ \\ \hline
\textbf{Số đôi bán được} & $3$ & $7$ & $14$ & $18$ & $6$ & $2$ \\ \hline
\end{tabular}
\vspace{-4pt}
\end{center}
Gọi $M_o$ là mốt và $\bar{x}$ là số trung bình cộng của mẫu số liệu trên. Tính $M_o + \bar{x}$.\answerbox""",
         "5.5cm", False),
        (r"\parttitle{Chủ đề 3. Các số đặc trưng đo độ phân tán (Bài 14)}",
         r"Nhiệt độ trung bình $12$ tháng trong năm (đơn vị: $^\circ\text{C}$) tại một địa phương lần lượt là: $16{,}5;\; 17{,}4;\; 20{,}2;\; 23{,}8;\; 27{,}5;\; 29{,}2;\; 29{,}6;\; 28{,}9;\; 27{,}6;\; 24{,}8;\; 21{,}4;\; 18{,}1$. Tìm khoảng biến thiên $R$ của mẫu số liệu trên.\answerbox",
         "5.0cm", False),

        # Page break -> Q14, Q15, Q16
        (None,
         r"Cho mẫu số liệu: $4;\; 9;\; 6;\; 12;\; 8;\; 5;\; 15;\; 7;\; 10;\; 11$. Tính khoảng tứ phân vị $\Delta_Q$ của mẫu số liệu đã cho.\answerbox",
         "5.5cm", True),
        (None,
         r"Năng suất lúa (tạ/ha) của $5$ thửa ruộng thí nghiệm lần lượt là: $21;\; 24;\; 26;\; 22;\; 27$. Tính phương sai $s^2$ của mẫu số liệu trên.\answerbox",
         "5.5cm", False),
        (None,
         r"""Điểm kiểm tra môn Vật lí của một nhóm $25$ học sinh được cho trong bảng tần số sau:
\begin{center}
\vspace{-4pt}
\begin{tabular}{|l|C{1.1cm}|C{1.1cm}|C{1.1cm}|C{1.1cm}|C{1.1cm}|}
\hline
\textbf{Điểm} & $6$ & $7$ & $8$ & $9$ & $10$ \\ \hline
\textbf{Số học sinh} & $3$ & $6$ & $7$ & $6$ & $3$ \\ \hline
\end{tabular}
\vspace{-4pt}
\end{center}
Tính độ lệch chuẩn $s$ của mẫu số liệu trên.\answerbox""",
         "5.5cm", False),

        # Page break -> Q17, Q18, Q19, Q20 (4 items at 4.5cm? Let's do 4 items at 4.5cm or 2 pages of 2? Actually 4 items x 4.5cm = 24.5cm fits nicely! Wait: let's make Q17-20 super roomy with 4 items at 4.5cm)
        (None,
         r"Cho mẫu số liệu về thời gian hoàn thành một bài tập (phút) của $9$ học sinh: $8;\; 10;\; 9;\; 11;\; 10;\; 12;\; 9;\; 24;\; 11$. Theo quy tắc $1{,}5\Delta_Q$, các giá trị lớn hơn ngưỡng $M = Q_3 + 1{,}5\Delta_Q$ là giá trị bất thường. Tìm giá trị ngưỡng $M$.\answerbox",
         "4.5cm", True),
        (None,
         r"Kiểm tra chiều dài (cm) của $11$ sản phẩm trên một dây chuyền thu được kết quả: $1{,}8;\; 4{,}5;\; 4{,}8;\; 5{,}0;\; 5{,}1;\; 5{,}2;\; 5{,}3;\; 5{,}4;\; 5{,}6;\; 5{,}8;\; 8{,}5$. Mẫu số liệu trên có bao nhiêu giá trị bất thường?\answerbox",
         "4.5cm", False),
        (None,
         r"Cho mẫu số liệu $X$ gồm các giá trị $x_1, x_2, \dots, x_n$ có phương sai $s_X^2 = 9$ và khoảng tứ phân vị $\Delta_Q(X) = 6$. Xét mẫu số liệu $Y$ gồm các giá trị $y_i = 2x_i + 5$ ($i = 1, 2, \dots, n$). Tính tổng $s_Y^2 + \Delta_Q(Y)$.\answerbox",
         "4.5cm", False),
        (None,
         r"Hai nhóm học sinh cùng tham gia một kì thi thử, mỗi nhóm có $10$ học sinh. Nhóm A có điểm trung bình $\bar{x}_1 = 28$ và phương sai $s_1^2 = 4$; nhóm B có điểm trung bình $\bar{x}_2 = 32$ và phương sai $s_2^2 = 6$. Tính phương sai $s^2$ của mẫu số liệu gộp gồm cả $20$ học sinh.\answerbox",
         "4.5cm", False),

        # ==================== CHƯƠNG VI: CÂU 21 - 70 ====================
        # New chapter on fresh page! Banner + Q21, Q22, Q23, Q24 -> wait banner takes ~2.2cm, so 3 items or 4 with 4.0cm! Let's put 3 items (Q21, Q22, Q23) at 5.5cm!
        (r"\chapterbanner{PHẦN II. CHƯƠNG VI: HÀM SỐ, ĐỒ THỊ VÀ ỨNG DỤNG}{(Từ Câu 21 đến Câu 70 — gồm Bài 15, Bài 16, Bài 17, Bài 18 và Bài tập cuối chương VI)}"
         + "\n" + r"\parttitle{Chủ đề 1. Hàm số và đồ thị (Bài 15)}",
         r"Tập xác định của hàm số $y = \sqrt{5-x} + \dfrac{x+1}{\sqrt{x+3}}$ có bao nhiêu giá trị nguyên?\answerbox",
         "5.5cm", True),
        (None,
         r"Biết tập xác định của hàm số $y = \dfrac{\sqrt{x+4}}{x^2-5x+6}$ có dạng $D = [a; +\infty)\setminus\{b; c\}$ ($a, b, c \in \mathbb{R}$). Tính $a + b + c$.\answerbox",
         "5.5cm", False),
        (None,
         r"Có bao nhiêu giá trị nguyên của tham số $m \in [-10; 10]$ để hàm số $y = \sqrt{x - m + 2} + \dfrac{1}{\sqrt{2m + 7 - x}}$ xác định trên nửa khoảng $[1; 5)$?\answerbox",
         "5.5cm", False),

        # Page break -> Q24, Q25, Q26 (Q26 has side-by-side TikZ)
        (None,
         r"Cho hàm số $f(x) = \begin{cases} 2x^2 - 1 & \text{khi } x < 1 \\ \sqrt{x+3} & \text{khi } 1 \le x \le 6 \\ \dfrac{x+2}{x-4} & \text{khi } x > 6 \end{cases}$. Tính giá trị biểu thức $T = f(-2) + f(1) + f(10)$.\answerbox",
         "5.5cm", True),
        (None,
         r"Biết đồ thị hàm số $y = \dfrac{ax+b}{x-1}$ đi qua hai điểm $A(2; 5)$ và $B(0; -1)$. Tính $a^2 + b^2$.\answerbox",
         "5.5cm", False),
        (None,
         side_by_side(
             r"Cho hàm số $y = f(x)$ xác định trên đoạn $[-3; 4]$ có đồ thị là đường gấp khúc như hình vẽ bên. Biết hàm số nghịch biến trên khoảng $(a; b)$, đạt giá trị lớn nhất bằng $M$ và giá trị nhỏ nhất bằng $m$ trên đoạn $[-3; 4]$. Tính giá trị của $a + b + M + m$.\answerbox",
             TIKZ_Q26, text_ratio=0.58),
         "5.0cm", False),

        # Page break -> Q27, Q28, Q29, Q30
        (None,
         r"Giá cước một hãng taxi quy định như sau: giá mở cửa cho $0{,}5\text{ km}$ đầu tiên là $10\,000$ đồng; từ trên $0{,}5\text{ km}$ đến $20\text{ km}$ tính $14\,000$ đồng/km; từ trên $20\text{ km}$ tính $12\,000$ đồng/km. Một hành khách đi quãng đường $25\text{ km}$ phải trả bao nhiêu nghìn đồng?\answerbox",
         "4.0cm", True),
        (None,
         r"Giá điện sinh hoạt của một hộ gia đình được tính theo bậc thang như sau: $50\text{ kWh}$ đầu tiên có giá $1\,800$ đồng/kWh; từ kWh thứ $51$ đến thứ $100$ có giá $2\,000$ đồng/kWh; từ kWh thứ $101$ trở lên có giá $2\,400$ đồng/kWh. Trong tháng, hộ gia đình đó phải trả tổng cộng $310\,000$ đồng tiền điện. Hỏi gia đình đó đã tiêu thụ bao nhiêu kWh điện?\answerbox",
         "4.0cm", False),
        (None,
         r"Có bao nhiêu giá trị nguyên của tham số $m \in [-5; 5]$ để hàm số bậc nhất $y = (m^2 - 4)x + 2m - 1$ đồng biến trên $\mathbb{R}$?\answerbox",
         "4.0cm", False),
        (None,
         r"Một xe khách xuất phát lúc $6$ giờ sáng để đi quãng đường dài $240\text{ km}$. Trong $2$ giờ đầu xe chạy với vận tốc $50\text{ km/h}$, sau đó dừng nghỉ $30$ phút, rồi tiếp tục chạy nốt quãng đường còn lại với vận tốc $70\text{ km/h}$. Hỏi xe đến nơi lúc mấy giờ (viết dạng số thập phân, ví dụ $10$ giờ $15$ phút ghi là $10{,}25$)?\answerbox",
         "4.0cm", False),

        # Page break -> Topic 2: Q31, Q32, Q33, Q34
        (r"\parttitle{Chủ đề 2. Hàm số bậc hai và ứng dụng thực tế (Bài 16)}",
         r"Gọi $I(x_I; y_I)$ là tọa độ đỉnh của parabol $(P): y = 2x^2 - 8x + 5$. Tính $2x_I - y_I$.\answerbox",
         "4.5cm", True),
        (None,
         r"Parabol $(P): y = ax^2 + bx + c$ ($a \ne 0$) có đỉnh $I(2; -1)$ và đi qua điểm $M(0; 3)$. Tính $a + b + c$.\answerbox",
         "4.5cm", False),
        (None,
         r"Parabol $(P): y = ax^2 + bx + c$ đi qua ba điểm $A(0; -2)$, $B(1; 1)$ và $C(-1; -1)$. Tính $a^2 + b^2 + c^2$.\answerbox",
         "4.5cm", False),
        (None,
         r"Gọi $M$ và $m$ lần lượt là giá trị lớn nhất và giá trị nhỏ nhất của hàm số $y = x^2 - 4x + 1$ trên đoạn $[0; 5]$. Tính $M - m$.\answerbox",
         "4.5cm", False),

        # Page break -> Q35, Q36, Q37 (TikZ)
        (None,
         r"Tìm giá trị lớn nhất của tham số $m$ để hàm số $y = -x^2 + 2(m-1)x + 3$ nghịch biến trên khoảng $(2; +\infty)$.\answerbox",
         "6.0cm", True),
        (None,
         r"Tìm giá trị của tham số $m$ để đường thẳng $d: y = 2x + m$ cắt parabol $(P): y = x^2 - 4x + 5$ tại hai điểm phân biệt $A, B$ sao cho $x_A^2 + x_B^2 = 22$.\answerbox",
         "6.0cm", False),
        (None,
         side_by_side(
             r"Cho hàm số bậc hai $y = ax^2 + bx + c$ ($a \ne 0$) có đồ thị là parabol như hình vẽ bên. Tính giá trị của biểu thức $2a + 3b - c$.\answerbox",
             TIKZ_Q37, text_ratio=0.60),
         "5.5cm", False),

        # Page break -> Q38, Q39, Q40, Q41
        (None,
         r"Một cổng chào có dạng hình parabol chiều cao $8\text{ m}$ và bề rộng chân cổng là $8\text{ m}$. Một xe tải có bề rộng $4\text{ m}$ đi qua chính giữa cổng. Tính giới hạn chiều cao $h_0$ (đơn vị: mét) tại mép ngoài của xe sao cho xe có chiều cao $h < h_0$ thì đi qua được cổng mà không chạm vòm cổng.\answerbox",
         "3.5cm", True),
        (None,
         r"Một quả bóng được đá lên từ mặt đất với độ cao $h$ (mét) sau thời gian $t$ (giây) được mô tả bởi công thức $h(t) = -5t^2 + 20t$. Tìm độ cao lớn nhất (đơn vị: mét) mà quả bóng đạt được.\answerbox",
         "3.5cm", False),
        (None,
         r"Một người nông dân có $80\text{ m}$ lưới rào để rào $3$ cạnh của một mảnh vườn hình chữ nhật giáp với một bức tường có sẵn (bức tường làm cạnh thứ tư). Diện tích lớn nhất của mảnh vườn có thể rào được là bao nhiêu $\text{m}^2$?\answerbox",
         "3.5cm", False),
        (None,
         r"Một khách sạn có $60$ phòng cho thuê. Nếu giá thuê mỗi phòng là $400$ nghìn đồng/đêm thì tất cả các phòng đều được thuê hết. Biết rằng cứ tăng giá thuê thêm $20$ nghìn đồng/đêm thì số phòng cho thuê giảm đi $2$ phòng. Khách sạn nên đặt giá thuê bao nhiêu nghìn đồng/đêm để doanh thu đạt lớn nhất?\answerbox",
         "3.5cm", False),

        # Page break -> Q42, Q43, Q44, Q45
        (None,
         r"Một cửa hàng bán giày nhập một mẫu giày với giá vốn $300$ nghìn đồng/đôi. Nếu bán với giá $500$ nghìn đồng/đôi thì mỗi tháng bán được $120$ đôi. Chủ cửa hàng nhận thấy nếu giảm giá bán mỗi đôi đi $10$ nghìn đồng thì số lượng bán ra mỗi tháng tăng thêm $12$ đôi. Cửa hàng cần bán với giá bao nhiêu nghìn đồng/đôi để thu được lợi nhuận hàng tháng lớn nhất?\answerbox",
         "3.5cm", True),
        (None,
         r"Một cây cầu treo có hai trụ tháp cao $100\text{ m}$ so với mặt cầu và khoảng cách giữa hai trụ tháp là $400\text{ m}$. Dây cáp chính có dạng parabol nhận đường thẳng đi qua tâm cầu làm trục đối xứng và điểm thấp nhất của dây cáp chạm mặt cầu tại chính giữa nhịp cầu. Tính độ dài (đơn vị: mét) của thanh giằng thẳng đứng nối từ mặt cầu lên dây cáp tại vị trí cách chân trụ tháp $100\text{ m}$.\answerbox",
         "3.5cm", False),
        (None,
         r"Tàu $A$ đang ở vị trí cách cảng $O$ một khoảng $50\text{ km}$ về phía Bắc và chạy thẳng về hướng Nam với vận tốc $40\text{ km/h}$. Cùng lúc đó, tàu $B$ xuất phát từ cảng $O$ và chạy thẳng về hướng Đông với vận tốc $30\text{ km/h}$. Khoảng cách ngắn nhất giữa hai tàu trong quá trình di chuyển bằng bao nhiêu kilômét?\answerbox",
         "3.5cm", False),
        (None,
         r"Tìm giá trị dương của tham số $m$ để parabol $y = x^2 - 2mx + m + 2$ cắt trục hoành tại hai điểm phân biệt $A, B$ thỏa mãn độ dài $AB = 4$.\answerbox",
         "3.5cm", False),

        # Page break -> Topic 3: Q46, Q47, Q48, Q49
        (r"\parttitle{Chủ đề 3. Dấu của tam thức bậc hai và bất phương trình bậc hai (Bài 17)}",
         r"Có bao nhiêu giá trị nguyên của tham số $m$ để phương trình $|x^2 - 6x + 5| = m$ có đúng $4$ nghiệm thực phân biệt?\answerbox",
         "4.5cm", True),
        (None,
         r"Bất phương trình $x^2 - 5x - 14 \le 0$ có bao nhiêu nghiệm nguyên?\answerbox",
         "4.5cm", False),
        (None,
         r"Tính tổng tất cả các nghiệm nguyên của bất phương trình $-2x^2 + 7x + 15 > 0$.\answerbox",
         "4.5cm", False),
        (None,
         r"Tập xác định của hàm số $y = \sqrt{-x^2 + 6x - 5} + \dfrac{1}{\sqrt{x - 2}}$ chứa bao nhiêu số nguyên?\answerbox",
         "4.5cm", False),

        # Page break -> Q50, Q51, Q52, Q53
        (None,
         r"Hệ bất phương trình $\begin{cases} x^2 - 3x - 10 \le 0 \\ x^2 - 4 > 0 \end{cases}$ có bao nhiêu nghiệm nguyên?\answerbox",
         "4.5cm", True),
        (None,
         r"Có bao nhiêu giá trị nguyên của tham số $m$ để $x^2 + (m - 1)x + m + 2 > 0$ với mọi $x \in \mathbb{R}$?\answerbox",
         "4.5cm", False),
        (None,
         r"Có bao nhiêu giá trị nguyên của tham số $m$ để bất phương trình $mx^2 - 4mx + 3m + 4 \ge 0$ nghiệm đúng với mọi $x \in \mathbb{R}$?\answerbox",
         "4.5cm", False),
        (None,
         r"Có bao nhiêu số nguyên $x \in [-10; 10]$ là nghiệm của bất phương trình $\dfrac{x^2 - 4x + 3}{x^2 - 9} \le 0$?\answerbox",
         "4.5cm", False),

        # Page break -> Q54, Q55, Q56, Q57
        (None,
         r"Có bao nhiêu giá trị nguyên của tham số $m$ để phương trình $x^2 - 4mx + 3m^2 + 2m + 3 = 0$ vô nghiệm?\answerbox",
         "4.5cm", True),
        (None,
         r"Bất phương trình $|x^2 - 3x - 4| \le x + 1$ có bao nhiêu nghiệm nguyên?\answerbox",
         "4.5cm", False),
        (None,
         r"Tìm giá trị nguyên nhỏ nhất của tham số $m$ để bất phương trình $x^2 - 4x + m > 0$ nghiệm đúng với mọi $x \in [1; 4]$.\answerbox",
         "4.5cm", False),
        (None,
         r"Một vật được ném thẳng đứng lên cao từ mặt đất với độ cao $h(t) = 25t - 5t^2$ (mét), trong đó $t$ (giây) là thời gian kể từ lúc ném. Khoảng thời gian (đơn vị: giây) mà vật ở độ cao từ $20\text{ m}$ trở lên bằng bao nhiêu?\answerbox",
         "4.5cm", False),

        # Page break -> Q58, Q59, Q60
        (None,
         r"Một doanh nghiệp sản xuất và bán $x$ sản phẩm mỗi tháng có hàm doanh thu là $R(x) = -2x^2 + 180x$ và hàm chi phí là $C(x) = 40x + 2000$ (đơn vị: triệu đồng). Hỏi mỗi tháng doanh nghiệp cần sản xuất ít nhất bao nhiêu sản phẩm để không bị lỗ (doanh thu lớn hơn hoặc bằng chi phí)?\answerbox",
         "6.0cm", True),
        (None,
         r"Một mảnh vườn hình chữ nhật có chu vi $40\text{ m}$. Người ta làm một lối đi rộng $1\text{ m}$ xung quanh sát $4$ cạnh bên trong vườn, phần diện tích đất còn lại ở giữa dùng để trồng hoa. Biết chiều rộng $x$ (m) của mảnh vườn không vượt quá $10\text{ m}$ và diện tích trồng hoa phải đạt ít nhất $48\text{ m}^2$. Tìm giá trị nhỏ nhất của chiều rộng $x$ (đơn vị: mét).\answerbox",
         "6.0cm", False),
        (None,
         r"Có bao nhiêu giá trị nguyên của tham số $m \in [-10; 10]$ sao cho bất phương trình $\dfrac{x^2 + (m-1)x + 1}{x^2 + x + 1} \le 3$ nghiệm đúng với mọi $x \in \mathbb{R}$?\answerbox",
         "6.0cm", False),

        # Page break -> Topic 4: Q61, Q62, Q63, Q64
        (r"\parttitle{Chủ đề 4. Phương trình quy về phương trình bậc hai \& Tổng hợp (Bài 18)}",
         r"Tìm nghiệm của phương trình $\sqrt{2x^2 - 5x} = \sqrt{x^2 - 4}$.\answerbox",
         "4.5cm", True),
        (None,
         r"Tính tích tất cả các nghiệm thực của phương trình $\sqrt{3x^2 - 4x + 2} = \sqrt{2x^2 + x - 2}$.\answerbox",
         "4.5cm", False),
        (None,
         r"Tìm nghiệm của phương trình $\sqrt{2x^2 - 5x + 1} = x - 1$.\answerbox",
         "4.5cm", False),
        (None,
         r"Tính tổng tất cả các nghiệm thực của phương trình $\sqrt{2x^2 - 12x + 19} = x - 2$.\answerbox",
         "4.5cm", False),

        # Page break -> Q65, Q66, Q67 (TikZ)
        (None,
         r"Tính tổng bình phương tất cả các nghiệm thực của phương trình $x^2 - 4x + \sqrt{x^2 - 4x + 5} - 7 = 0$.\answerbox",
         "5.5cm", True),
        (None,
         r"Có bao nhiêu giá trị nguyên của tham số $m \in [-10; 10]$ để phương trình $\sqrt{x^2 - 2x + 5} = x + m$ có nghiệm thực?\answerbox",
         "5.5cm", False),
        (None,
         side_by_side(
             r"Một người ở trạm hải đăng $A$ cách bờ biển thẳng một khoảng $AB = 4\text{ km}$ ($B \in \text{bờ}$), muốn đi tới điểm $C$ trên bờ biển cách $B$ một khoảng $BC = 7\text{ km}$. Người đó chèo thuyền từ $A$ đến điểm $M$ thuộc đoạn $BC$ với vận tốc $3\text{ km/h}$, rồi đi bộ dọc bờ biển từ $M$ đến $C$ với vận tốc $5\text{ km/h}$. Biết tổng thời gian đi từ $A$ đến $C$ là $2$ giờ $28$ phút. Tính độ dài đoạn $BM$ (đơn vị: km).\answerbox",
             TIKZ_Q67, text_ratio=0.62),
         "6.0cm", False),

        # Page break -> Q68 (TikZ), Q69, Q70 (TikZ)
        (None,
         side_by_side(
             r"Người ta cần mắc một đường dây cáp quang từ điểm $A$ bên này bờ sông đến điểm $B$ ở bên kia bờ sông thẳng. Chiếu vuông góc $A$ xuống bờ bên kia được điểm $H$ với $AH = 3\text{ km}$ và đoạn bờ sông $HB = 8\text{ km}$. Chọn điểm $M$ trên đoạn $HB$ để đi dây dưới nước từ $A$ đến $M$ với chi phí $5$ tỉ đồng/km và đi dây trên cạn từ $M$ đến $B$ với chi phí $3$ tỉ đồng/km. Biết tổng kinh phí thực hiện bằng $37$ tỉ đồng và để thuận tiện thi công cần $HM > 2\text{ km}$. Tính khoảng cách $HM$ (km).\answerbox",
             TIKZ_Q68, text_ratio=0.63),
         "4.0cm", True),
        (None,
         r"Tìm tổng tất cả các giá trị nguyên của tham số $m$ để đường thẳng $y = x + m$ cắt đồ thị hàm số $y = \sqrt{25 - x^2}$ tại hai điểm phân biệt.\answerbox",
         "4.5cm", False),
        (None,
         side_by_side(
             r"Một cổng chào có dạng một phần parabol chiều cao $8\text{ m}$ và bề rộng chân cổng $8\text{ m}$. Người ta dựng một khung thép hình chữ nhật $MNPQ$ nội tiếp trong cổng sao cho cạnh $MN$ nằm trên mặt đất còn hai đỉnh $P, Q$ nằm trên vòm parabol. Khi chu vi của hình chữ nhật $MNPQ$ đạt giá trị lớn nhất thì diện tích của $MNPQ$ bằng bao nhiêu $\text{m}^2$?\answerbox",
             TIKZ_Q70, text_ratio=0.64),
         "4.0cm", False),
    ]
    assert len(qs) == 70, f"Expected 70 questions, got {len(qs)}"
    return qs


def get_answer_table_and_solutions():
    answers = [
        (1, "148000"), (2, "24,8"), (3, "3,4"), (4, "0,5"), (5, "0,025"),
        (6, "8"), (7, "2,85"), (8, "12,15"), (9, "2"), (10, "30"),
        (11, "14,5"), (12, "79,46"), (13, "13,1"), (14, "5"), (15, "5,2"),
        (16, "1,2"), (17, "15,25"), (18, "2"), (19, "48"), (20, "9"),
        (21, "8"), (22, "1"), (23, "5"), (24, "11"), (25, "5"),
        (26, "3"), (27, "343"), (28, "150"), (29, "6"), (30, "10,5"),
        (31, "7"), (32, "0"), (33, "9"), (34, "9"), (35, "3"),
        (36, "-2"), (37, "-1"), (38, "6"), (39, "20"), (40, "800"),
        (41, "500"), (42, "450"), (43, "25"), (44, "30"), (45, "3"),
        (46, "3"), (47, "10"), (48, "9"), (49, "3"), (50, "3"),
        (51, "7"), (52, "5"), (53, "4"), (54, "3"), (55, "4"),
        (56, "5"), (57, "3"), (58, "20"), (59, "6"), (60, "9"),
        (61, "4"), (62, "4"), (63, "3"), (64, "8"), (65, "24"),
        (66, "11"), (67, "3"), (68, "4"), (69, "18"), (70, "24"),
    ]

    # Build 5-column x 14-row answer summary table
    rows = []
    for r in range(14):
        cells = []
        for c in range(5):
            idx = r + c * 14
            num, val = answers[idx]
            cells.append(f"\\textbf{{{num}}} & {val}")
        rows.append(" & ".join(cells) + r" \\ \hline")

    table_tex = (
        r"\begin{center}" + "\n"
        r"\renewcommand{\arraystretch}{1.28}" + "\n"
        r"\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|}" + "\n"
        r"\hline" + "\n"
        r"\textbf{Câu} & \textbf{Đáp án} & \textbf{Câu} & \textbf{Đáp án} & \textbf{Câu} & \textbf{Đáp án} & \textbf{Câu} & \textbf{Đáp án} & \textbf{Câu} & \textbf{Đáp án} \\ \hline" + "\n"
        + "\n".join(rows) + "\n"
        r"\end{tabular}" + "\n"
        r"\end{center}"
    )

    sols = [
        # Chương V: 1 - 20
        r"\textbf{Câu 1.} Độ chính xác $d = 300$ có chữ số khác $0$ đầu tiên ở hàng trăm nên ta quy tròn $a = 148\,372$ đến hàng nghìn, thu được số quy tròn là $\mathbf{148000}$.",
        r"\textbf{Câu 2.} Độ chính xác $d = 0{,}02$ ở hàng phần trăm nên ta quy tròn $a = 24{,}7684$ đến hàng phần chục, thu được số quy tròn là $\mathbf{24{,}8}$.",
        r"\textbf{Câu 3.} Ta có $11{,}9 \le \bar{x} \le 12{,}1$ và $4{,}9 \le \bar{y} \le 5{,}1 \Rightarrow 58{,}31 \le \bar{S} = \bar{x}\bar{y} \le 61{,}71$. Suy ra $m = 58{,}31;\; n = 61{,}71 \Rightarrow n - m = \mathbf{3{,}4}$.",
        r"\textbf{Câu 4.} Sai số tương đối $\delta_h = \dfrac{\Delta_h}{h} \le \dfrac{0{,}4}{80} = 0{,}005 = \mathbf{0{,}5}\%$.",
        r"\textbf{Câu 5.} Sai số tuyệt đối: $\Delta = \left|\dfrac{5}{8} - 0{,}6\right| = |0{,}625 - 0{,}6| = \mathbf{0{,}025}$.",
        r"\textbf{Câu 6.} Ta có $\bar{x} = \dfrac{7+8+6+9+x+8+7+9}{8} = \dfrac{54+x}{8} = 7{,}75 \Rightarrow 54 + x = 62 \Rightarrow x = \mathbf{8}$.",
        r"\textbf{Câu 7.} Thời gian tự học trung bình: $\bar{x} = \dfrac{1\cdot 4 + 2\cdot 10 + 3\cdot 16 + 4\cdot 8 + 5\cdot 2}{40} = \dfrac{114}{40} = \mathbf{2{,}85}$ giờ.",
        r"\textbf{Câu 8.} Sắp xếp theo thứ tự không giảm ($n=10$): $11{,}5$; $11{,}7$; $11{,}8$; $11{,}9$; $12{,}1$; $12{,}2$; $12{,}4$; $12{,}6$; $12{,}8$; $13{,}0$. Trung vị $M_e = \dfrac{12{,}1 + 12{,}2}{2} = \mathbf{12{,}15}$.",
        r"\textbf{Câu 9.} Cỡ mẫu $n = 35$ là số lẻ nên $M_e$ là giá trị thứ $18$. Cộng dồn tần số: lỗi $0$ ($5$ bài), lỗi $1$ ($13$ bài), lỗi $2$ ($22$ bài). Giá trị thứ $18$ là $\mathbf{2}$.",
        r"\textbf{Câu 10.} Sắp xếp $11$ số: $19$; $21$; $22$; $24$; $25$; $27$; $28$; $29$; $30$; $32$; $35$. Trung vị $Q_2 = 27$. Nửa trên gồm $28$; $29$; $30$; $32$; $35 \Rightarrow Q_3 = \mathbf{30}$.",
        r"\textbf{Câu 11.} Sắp xếp $12$ số: $5{,}5$; $6{,}0$; $6{,}5$; $6{,}5$; $7{,}0$; $7{,}0$; $7{,}5$; $7{,}5$; $8{,}0$; $8{,}0$; $8{,}5$; $9{,}0$. Nửa dưới ($6$ số) cho $Q_1 = \dfrac{6{,}5+6{,}5}{2} = 6{,}5$; nửa trên ($6$ số) cho $Q_3 = \dfrac{8{,}0+8{,}0}{2} = 8{,}0$. Suy ra $Q_1 + Q_3 = \mathbf{14{,}5}$.",
        r"\textbf{Câu 12.} Cỡ giày có tần số lớn nhất ($18$) là $M_o = 40$. Tổng số đôi $n = 50$, $\bar{x} = \dfrac{111 + 266 + 546 + 720 + 246 + 84}{50} = \dfrac{1973}{50} = 39{,}46 \Rightarrow M_o + \bar{x} = \mathbf{79{,}46}$.",
        r"\textbf{Câu 13.} $x_{\max} = 29{,}6$; $x_{\min} = 16{,}5 \Rightarrow R = 29{,}6 - 16{,}5 = \mathbf{13{,}1}$.",
        r"\textbf{Câu 14.} Sắp xếp: $4$; $5$; $6$; $7$; $8$; $9$; $10$; $11$; $12$; $15$ ($n=10$). Ta có $Q_1 = 6$; $Q_3 = 11 \Rightarrow \Delta_Q = 11 - 6 = \mathbf{5}$.",
        r"\textbf{Câu 15.} $\bar{x} = \dfrac{21+24+26+22+27}{5} = 24$. Phương sai $s^2 = \dfrac{9 + 0 + 4 + 4 + 9}{5} = \dfrac{26}{5} = \mathbf{5{,}2}$.",
        r"\textbf{Câu 16.} Mẫu có $n = 25$, đối xứng quanh $\bar{x} = 8$. Ta có $s^2 = \dfrac{3\cdot 4 + 6\cdot 1 + 7\cdot 0 + 6\cdot 1 + 3\cdot 4}{25} = \dfrac{36}{25} = 1{,}44 \Rightarrow s = \mathbf{1{,}2}$.",
        r"\textbf{Câu 17.} Sắp xếp ($n=9$): $8$; $9$; $9$; $10$; $10$; $11$; $11$; $12$; $24$. Có $Q_2 = 10$, $Q_1 = 9$, $Q_3 = \dfrac{11+12}{2} = 11{,}5 \Rightarrow \Delta_Q = 2{,}5 \Rightarrow M = 11{,}5 + 1{,}5\cdot 2{,}5 = \mathbf{15{,}25}$.",
        r"\textbf{Câu 18.} Sắp xếp ($n=11$): $Q_2 = 5{,}2$, nửa dưới $1{,}8$; $4{,}5$; $4{,}8$; $5{,}0$; $5{,}1 \Rightarrow Q_1 = 4{,}8$; nửa trên $5{,}3$; $5{,}4$; $5{,}6$; $5{,}8$; $8{,}5 \Rightarrow Q_3 = 5{,}6$. Khi đó $\Delta_Q = 0{,}8$, ngưỡng $[3{,}6; 6{,}8]$. Có $\mathbf{2}$ giá trị bất thường là $1{,}8$ và $8{,}5$.\par\noindent\begin{minipage}{\linewidth}\centering\vspace{3pt}" + TIKZ_ANS_Q18 + r"\vspace{2pt}\end{minipage}",
        r"\textbf{Câu 19.} Khi biến đổi tuyến tính $y_i = ax_i + b$ ta có $s_Y^2 = a^2 s_X^2 = 2^2\cdot 9 = 36$ và $\Delta_Q(Y) = |a|\Delta_Q(X) = 2\cdot 6 = 12$. Vậy $s_Y^2 + \Delta_Q(Y) = 36 + 12 = \mathbf{48}$.",
        r"\textbf{Câu 20.} Trung bình chung $\bar{x} = \dfrac{10\cdot 28 + 10\cdot 32}{20} = 30$. Áp dụng $\sum (x_i - \bar{x})^2 = n_1[s_1^2 + (\bar{x}_1 - \bar{x})^2] + n_2[s_2^2 + (\bar{x}_2 - \bar{x})^2] = 10(4 + 4) + 10(6 + 4) = 180 \Rightarrow s^2 = \dfrac{180}{20} = \mathbf{9}$.",

        # Chương VI: 21 - 70
        r"\textbf{Câu 21.} Điều kiện $\begin{cases} 5 - x \ge 0 \\ x + 3 > 0 \end{cases} \Leftrightarrow -3 < x \le 5$. Các số nguyên: $-2, -1, 0, 1, 2, 3, 4, 5$. Có $\mathbf{8}$ giá trị.",
        r"\textbf{Câu 22.} Điều kiện $\begin{cases} x + 4 \ge 0 \\ x^2 - 5x + 6 \ne 0 \end{cases} \Leftrightarrow x \ge -4;\; x \notin \{2; 3\}$. Vậy $a = -4,\; b = 2,\; c = 3 \Rightarrow a + b + c = \mathbf{1}$.",
        r"\textbf{Câu 23.} TXĐ của hàm số là $D = [m - 2; 2m + 7)$. Để hàm số xác định trên $[1; 5)$ cần $m - 2 \le 1$ và $2m + 7 \ge 5 \Leftrightarrow -1 \le m \le 3$. Có $\mathbf{5}$ giá trị nguyên ($-1, 0, 1, 2, 3$).",
        r"\textbf{Câu 24.} $f(-2) = 2(-2)^2 - 1 = 7$; $f(1) = \sqrt{1+3} = 2$; $f(10) = \dfrac{10+2}{10-4} = 2$. Tổng $T = 7 + 2 + 2 = \mathbf{11}$.",
        r"\textbf{Câu 25.} Thay $B(0; -1) \Rightarrow \dfrac{b}{-1} = -1 \Rightarrow b = 1$. Thay $A(2; 5) \Rightarrow \dfrac{2a+1}{1} = 5 \Rightarrow a = 2$. Suy ra $a^2 + b^2 = \mathbf{5}$.",
        r"\textbf{Câu 26.} Từ đồ thị, hàm số nghịch biến trên $(-1; 2) \Rightarrow a = -1,\; b = 2$; trên $[-3; 4]$ có $M = 4$ (tại $x=-1$), $m = -2$ (tại $x=2$). Vậy $a + b + M + m = -1 + 2 + 4 - 2 = \mathbf{3}$.",
        r"\textbf{Câu 27.} Tiền cước cho $25\text{ km}$: $10 + (20 - 0{,}5)\cdot 14 + (25 - 20)\cdot 12 = 10 + 273 + 60 = \mathbf{343}$ nghìn đồng.",
        r"\textbf{Câu 28.} $100\text{ kWh}$ đầu hết $50\cdot 1800 + 50\cdot 2000 = 190\,000$ đồng. Số kWh ở bậc 3 là $\dfrac{310\,000 - 190\,000}{2400} = 50\text{ kWh}$. Tổng tiêu thụ: $\mathbf{150}\text{ kWh}$.",
        r"\textbf{Câu 29.} Hàm số bậc nhất đồng biến trên $\mathbb{R} \Leftrightarrow m^2 - 4 > 0 \Leftrightarrow m > 2$ hoặc $m < -2$. Với $m \in [-5; 5] \cap \mathbb{Z} \Rightarrow m \in \{-5, -4, -3, 3, 4, 5\}$ ($\mathbf{6}$ giá trị).",
        r"\textbf{Câu 30.} $2\text{ h}$ đầu đi được $100\text{ km}$. Còn $140\text{ km}$ đi hết $\dfrac{140}{70} = 2\text{ h}$. Cộng thêm $0{,}5\text{ h}$ nghỉ $\Rightarrow$ tổng thời gian $4{,}5\text{ h}$. Xe đến nơi lúc $6 + 4{,}5 = \mathbf{10{,}5}$ giờ.",
        r"\textbf{Câu 31.} Đỉnh $I$ có $x_I = -\dfrac{b}{2a} = 2;\; y_I = 2(2)^2 - 8(2) + 5 = -3 \Rightarrow 2x_I - y_I = 4 - (-3) = \mathbf{7}$.",
        r"\textbf{Câu 32.} $(P)$ có đỉnh $I(2; -1) \Rightarrow y = a(x-2)^2 - 1$. Qua $M(0; 3) \Rightarrow 4a - 1 = 3 \Rightarrow a = 1 \Rightarrow y = x^2 - 4x + 3$. Tổng $a + b + c = 1 - 4 + 3 = \mathbf{0}$.",
        r"\textbf{Câu 33.} Qua $A(0; -2) \Rightarrow c = -2$. Hệ $\begin{cases} a + b - 2 = 1 \\ a - b - 2 = -1 \end{cases} \Rightarrow a = 2,\; b = 1$. Khi đó $a^2 + b^2 + c^2 = 4 + 1 + 4 = \mathbf{9}$.",
        r"\textbf{Câu 34.} Đỉnh $x_I = 2 \in [0; 5]$. Tính $y(0) = 1,\; y(2) = -3,\; y(5) = 6 \Rightarrow M = 6,\; m = -3 \Rightarrow M - m = \mathbf{9}$.",
        r"\textbf{Câu 35.} Vì $a = -1 < 0$ và $x_I = m - 1$ nên hàm số nghịch biến trên $(m - 1; +\infty)$. Yêu cầu bài toán $\Leftrightarrow m - 1 \le 2 \Leftrightarrow m \le 3 \Rightarrow m_{\max} = \mathbf{3}$.",
        r"\textbf{Câu 36.} PTHĐGĐ: $x^2 - 6x + 5 - m = 0$ có $\Delta' = 4 + m > 0 \Leftrightarrow m > -4$. Ta có $x_A^2 + x_B^2 = (x_A + x_B)^2 - 2x_Ax_B = 36 - 2(5 - m) = 26 + 2m = 22 \Rightarrow m = \mathbf{-2}$ (thỏa mãn).",
        r"\textbf{Câu 37.} Từ đồ thị, $(P)$ có đỉnh $I(1; -4)$ và qua $(0; -3) \Rightarrow y = (x-1)^2 - 4 = x^2 - 2x - 3$. Vậy $a = 1,\; b = -2,\; c = -3 \Rightarrow 2a + 3b - c = 2 - 6 + 3 = \mathbf{-1}$.",
        r"\textbf{Câu 38.} Chọn hệ trục $Oxy$ với gốc $O$ ở chân chính giữa cổng: $(P): y = -\dfrac{1}{2}x^2 + 8$ (qua $(0;8)$ và $(\pm 4; 0)$). Tại mép xe rộng $4\text{ m}$ ứng với $x = \pm 2 \Rightarrow h_0 = y(2) = -\dfrac{1}{2}(4) + 8 = \mathbf{6}\text{ m}$.",
        r"\textbf{Câu 39.} Parabol $h(t) = -5t^2 + 20t$ có $a = -5 < 0$, đỉnh tại $t = -\dfrac{20}{2(-5)} = 2 \Rightarrow h_{\max} = h(2) = \mathbf{20}\text{ m}$.",
        r"\textbf{Câu 40.} Gọi chiều rộng hai cạnh vuông góc tường là $y$ ($0 < y < 40$), cạnh song song là $80 - 2y$. Diện tích $S(y) = -2y^2 + 80y$ đạt cực đại tại đỉnh $y = 20 \Rightarrow S_{\max} = \mathbf{800}\text{ m}^2$.",
        r"\textbf{Câu 41.} Gọi giá thuê là $p$ (nghìn đồng/đêm). Số phòng thuê là $60 - 2\cdot \dfrac{p - 400}{20} = 100 - 0{,}1p$. Doanh thu $R(p) = -0{,}1p^2 + 100p$ đạt GTLN tại đỉnh $p = \dfrac{-100}{2(-0{,}1)} = \mathbf{500}$ nghìn đồng.",
        r"\textbf{Câu 42.} Gọi số lần giảm $10$ nghìn là $k$: giá bán $500 - 10k$, lãi mỗi đôi $200 - 10k$, số lượng $120 + 12k$. Lợi nhuận $L(k) = (200 - 10k)(120 + 12k) = -120k^2 + 1200k + 24000$, đạt GTLN tại $k = 5 \Rightarrow$ giá bán $= 500 - 50 = \mathbf{450}$ nghìn đồng.",
        r"\textbf{Câu 43.} Chọn $O$ tại điểm thấp nhất chính giữa cầu: $(P): y = ax^2$ đi qua $(200; 100) \Rightarrow a = \dfrac{100}{200^2} = \dfrac{1}{400}$. Vị trí cách trụ tháp $100\text{ m}$ có hoành độ $|x| = 200 - 100 = 100 \Rightarrow y = \dfrac{100^2}{400} = \mathbf{25}\text{ m}$.",
        r"\textbf{Câu 44.} Chọn $O$ là gốc tọa độ: $A(0; 50 - 40t),\; B(30t; 0)$. Bình phương khoảng cách $AB^2 = (30t)^2 + (50 - 40t)^2 = 2500t^2 - 4000t + 2500$, nhỏ nhất tại $t = 0{,}8\text{ h}$ với $AB_{\min}^2 = 900 \Rightarrow AB_{\min} = \mathbf{30}\text{ km}$.",
        r"\textbf{Câu 45.} $x^2 - 2mx + m + 2 = 0$ có $\Delta' = m^2 - m - 2 > 0$. Ta có $AB^2 = (x_1 - x_2)^2 = (x_1+x_2)^2 - 4x_1x_2 = 4m^2 - 4(m+2) = 16 \Leftrightarrow m^2 - m - 6 = 0 \Rightarrow m = 3$ hoặc $m = -2$. Vì $m > 0$ nên $m = \mathbf{3}$.",
        r"\textbf{Câu 46.} Đồ thị $y = |x^2 - 6x + 5|$ thu được bằng cách giữ nguyên phần trên $Ox$ và lấy đối xứng phần dưới $Ox$ (đỉnh $(3; -4)$ thành $(3; 4)$). Đường thẳng $y = m$ cắt đồ thị tại $4$ điểm phân biệt $\Leftrightarrow 0 < m < 4 \Rightarrow m \in \{1; 2; 3\}$ ($\mathbf{3}$ giá trị).",
        r"\textbf{Câu 47.} $x^2 - 5x - 14 \le 0 \Leftrightarrow -2 \le x \le 7$. Số nghiệm nguyên: $7 - (-2) + 1 = \mathbf{10}$.",
        r"\textbf{Câu 48.} $-2x^2 + 7x + 15 > 0 \Leftrightarrow -\dfrac{3}{2} < x < 5$. Các nghiệm nguyên: $-1, 0, 1, 2, 3, 4$, tổng bằng $\mathbf{9}$.",
        r"\textbf{Câu 49.} Điều kiện: $\begin{cases} -x^2 + 6x - 5 \ge 0 \\ x - 2 > 0 \end{cases} \Leftrightarrow \begin{cases} 1 \le x \le 5 \\ x > 2 \end{cases} \Leftrightarrow 2 < x \le 5$. Các số nguyên: $3, 4, 5$ ($\mathbf{3}$ số).",
        r"\textbf{Câu 50.} BPT (1) $\Leftrightarrow -2 \le x \le 5$; BPT (2) $\Leftrightarrow x < -2$ hoặc $x > 2$. Giao lại được $2 < x \le 5$, có $\mathbf{3}$ nghiệm nguyên ($3, 4, 5$).",
        r"\textbf{Câu 51.} Hệ số $a = 1 > 0$, yêu cầu $\Leftrightarrow \Delta = (m - 1)^2 - 4(m + 2) < 0 \Leftrightarrow m^2 - 6m - 7 < 0 \Leftrightarrow -1 < m < 7$. Có $\mathbf{7}$ giá trị nguyên ($0, 1, \dots, 6$).",
        r"\textbf{Câu 52.} TH1: $m = 0 \Rightarrow 4 \ge 0$ (đúng $\forall x \in \mathbb{R}$, nhận). TH2: $m > 0$ và $\Delta' = 4m^2 - m(3m + 4) \le 0 \Leftrightarrow 0 < m \le 4$. Kết hợp $0 \le m \le 4 \Rightarrow$ có $\mathbf{5}$ giá trị nguyên ($0, 1, 2, 3, 4$).",
        r"\textbf{Câu 53.} ĐKXĐ: $x \ne \pm 3$. Rút gọn thành $\dfrac{x - 1}{x + 3} \le 0 \Leftrightarrow -3 < x \le 1$ (đều khác $\pm 3$). Các số nguyên thỏa mãn: $-2, -1, 0, 1$ ($\mathbf{4}$ số).",
        r"\textbf{Câu 54.} Phương trình vô nghiệm $\Leftrightarrow \Delta' = 4m^2 - (3m^2 + 2m + 3) < 0 \Leftrightarrow m^2 - 2m - 3 < 0 \Leftrightarrow -1 < m < 3$. Có $\mathbf{3}$ giá trị nguyên ($0, 1, 2$).",
        r"\textbf{Câu 55.} BPT $\Leftrightarrow \begin{cases} x + 1 \ge 0 \\ -x - 1 \le x^2 - 3x - 4 \le x + 1 \end{cases} \Leftrightarrow \begin{cases} x \ge -1 \\ x^2 - 2x - 3 \ge 0 \\ x^2 - 4x - 5 \le 0 \end{cases} \Leftrightarrow x = -1$ hoặc $3 \le x \le 5$. Nghiệm nguyên: $-1, 3, 4, 5$ ($\mathbf{4}$ nghiệm).",
        r"\textbf{Câu 56.} $m > -x^2 + 4x\;\forall x \in [1; 4]$. Trên $[1; 4]$, parabol $g(x) = -x^2 + 4x$ đạt GTLN tại đỉnh $x = 2$ bằng $4$. Vậy $m > 4 \Rightarrow m_{\min} = \mathbf{5}$.",
        r"\textbf{Câu 57.} $25t - 5t^2 \ge 20 \Leftrightarrow t^2 - 5t + 4 \le 0 \Leftrightarrow 1 \le t \le 4$. Khoảng thời gian: $4 - 1 = \mathbf{3}$ giây.",
        r"\textbf{Câu 58.} $R(x) \ge C(x) \Leftrightarrow -2x^2 + 140x - 2000 \ge 0 \Leftrightarrow x^2 - 70x + 1000 \le 0 \Leftrightarrow 20 \le x \le 50$. Cần sản xuất ít nhất $\mathbf{20}$ sản phẩm.",
        r"\textbf{Câu 59.} Nửa chu vi là $20\text{ m}$, chiều dài $20 - x$. Kích thước phần trồng hoa: $(x - 2)(18 - x) \ge 48 \Leftrightarrow x^2 - 20x + 84 \le 0 \Leftrightarrow 6 \le x \le 14$. Kết hợp $x \le 10 \Rightarrow x_{\min} = \mathbf{6}\text{ m}$.",
        r"\textbf{Câu 60.} Vì $x^2 + x + 1 > 0\;\forall x$, nhân chéo được $2x^2 + (4 - m)x + 2 \ge 0\;\forall x \Leftrightarrow \Delta = (4 - m)^2 - 16 \le 0 \Leftrightarrow 0 \le m \le 8$. Có $\mathbf{9}$ giá trị nguyên.",
        r"\textbf{Câu 61.} Bình phương hai vế: $2x^2 - 5x = x^2 - 4 \Leftrightarrow x^2 - 5x + 4 = 0 \Leftrightarrow x = 1$ hoặc $x = 4$. Thử lại: $x = 1$ cho $x^2 - 4 = -3 < 0$ (loại); $x = 4$ thỏa mãn $\sqrt{12} = \sqrt{12}$. Nghiệm $x = \mathbf{4}$.",
        r"\textbf{Câu 62.} Bình phương hai vế: $3x^2 - 4x + 2 = 2x^2 + x - 2 \Leftrightarrow x^2 - 5x + 4 = 0 \Leftrightarrow x = 1$ hoặc $x = 4$. Thử lại cả hai đều thỏa mãn. Tích bằng $1 \cdot 4 = \mathbf{4}$.",
        r"\textbf{Câu 63.} Bình phương: $2x^2 - 5x + 1 = (x - 1)^2 \Leftrightarrow x^2 - 3x = 0 \Leftrightarrow x = 0$ hoặc $x = 3$. Thử lại: $x = 0 \Rightarrow VP = -1 < 0$ (loại); $x = 3$ thỏa mãn $\sqrt{4} = 2$. Nghiệm $x = \mathbf{3}$.",
        r"\textbf{Câu 64.} Bình phương: $2x^2 - 12x + 19 = (x - 2)^2 \Leftrightarrow x^2 - 8x + 15 = 0 \Leftrightarrow x = 3$ hoặc $x = 5$. Thử lại đều thỏa mãn ($VP > 0$). Tổng bằng $3 + 5 = \mathbf{8}$.",
        r"\textbf{Câu 65.} Đặt $t = \sqrt{x^2 - 4x + 5} \ge 1 \Rightarrow t^2 - 5 + t - 7 = 0 \Leftrightarrow t^2 + t - 12 = 0 \Rightarrow t = 3$. Khi đó $x^2 - 4x - 4 = 0$ ($\Delta' = 8 > 0$). Theo Vi-ét: $x_1^2 + x_2^2 = 4^2 - 2(-4) = \mathbf{24}$.",
        r"\textbf{Câu 66.} Điều kiện $x + m \ge 0$ và bình phương được $(2m + 2)x = 5 - m^2$. Với $m = -1$ vô nghiệm; với $m \ne -1$, $x = \dfrac{5 - m^2}{2(m + 1)}$, khi đó $x + m = \dfrac{m^2 + 2m + 5}{2(m + 1)} \ge 0 \Leftrightarrow m > -1$. Trong $[-10; 10]$ có $\mathbf{11}$ số nguyên ($0, 1, \dots, 10$).",
        r"\textbf{Câu 67.} Đặt $BM = x$ ($0 \le x \le 7$). Ta có $\dfrac{\sqrt{16 + x^2}}{3} + \dfrac{7 - x}{5} = \dfrac{37}{15} \Leftrightarrow 5\sqrt{16 + x^2} = 3x + 16$. Bình phương hai vế được $16x^2 - 96x + 144 = 0 \Leftrightarrow 16(x - 3)^2 = 0 \Rightarrow x = \mathbf{3}\text{ km}$.",
        r"\textbf{Câu 68.} Đặt $HM = x$ ($2 < x \le 8$). Có $5\sqrt{9 + x^2} + 3(8 - x) = 37 \Leftrightarrow 5\sqrt{9 + x^2} = 3x + 13 \Rightarrow 8x^2 - 39x + 28 = 0 \Leftrightarrow x = 4$ hoặc $x = \dfrac{7}{8}$ (loại vì $HM > 2$). Vậy $HM = \mathbf{4}\text{ km}$.",
        r"\textbf{Câu 69.} Đồ thị $y = \sqrt{25 - x^2}$ là nửa đường tròn tâm $O(0; 0)$, $R = 5$ phía trên $Ox$. Đường thẳng $y = x + m$ cắt nửa đường tròn tại $2$ điểm phân biệt khi đi qua $(-5; 0)$ ($m = 5$) cho đến dưới tiếp tuyến $d(O, d) = \dfrac{|m|}{\sqrt{2}} = 5 \Leftrightarrow 5 \le m < 5\sqrt{2} \approx 7{,}07$. Vậy $m \in \{5; 6; 7\}$, tổng bằng $\mathbf{18}$.\par\noindent\begin{minipage}{\linewidth}\centering\vspace{3pt}" + TIKZ_ANS_Q69 + r"\vspace{2pt}\end{minipage}",
        r"\textbf{Câu 70.} Chọn gốc tọa độ $O$ chính giữa chân cổng, parabol $y = 8 - \dfrac{1}{2}x^2$. Đặt $M(-t; 0), N(t; 0)$ với $0 < t < 4 \Rightarrow P\left(t; 8 - \dfrac{1}{2}t^2\right)$. Chu vi $C = 2\left(2t + 8 - \dfrac{1}{2}t^2\right) = -t^2 + 4t + 16$, đạt GTLN tại đỉnh $t = 2 \in (0; 4)$. Khi đó đáy $MN = 4\text{ m}$, chiều cao $NP = 6\text{ m} \Rightarrow S_{MNPQ} = 4 \cdot 6 = \mathbf{24}\text{ m}^2$.",
    ]
    assert len(sols) == 70, f"Expected 70 solutions, got {len(sols)}"
    return table_tex, sols


def generate_tex(exam_pages_str: str = "XX", ans_pages_str: str = "YY") -> str:
    questions = get_questions()
    table_tex, sols = get_answer_table_and_solutions()

    preamble = PREAMBLE.replace("__HEADER_QUOTE__", build_header_quote_macro(45))
    preamble = preamble.replace("__EXAM_PAGES__", exam_pages_str)
    preamble = preamble.replace("__ANS_PAGES__", ans_pages_str)

    parts = [preamble, r"\begin{document}"]

    # Title banner (Page 1)
    parts.append(r"""\begin{center}
  {\Large\bfseries\color{ink} ĐỀ CƯƠNG ÔN TẬP TOÁN 10 — CHƯƠNG V \& CHƯƠNG VI}\\[3pt]
  {\small\color{gray!75!black} \textit{Hình thức: 70 câu trả lời ngắn (20 câu Thống kê + 50 câu Hàm số, đồ thị \& ứng dụng) — Sách Kết nối tri thức}}
\end{center}
\vspace{2pt}""")

    parts.append(r"""\chapterbanner{PHẦN I. CHƯƠNG V: CÁC SỐ ĐẶC TRƯNG CỦA MẪU SỐ LIỆU KHÔNG GHÉP NHÓM}{(Từ Câu 1 đến Câu 20 — gồm Bài 12, Bài 13, Bài 14 và Bài tập cuối chương V)}""")

    enum_started = False
    for idx, (section_hdr, text_tex, oli_h, brk) in enumerate(questions, start=1):
        if section_hdr:
            if enum_started:
                parts.append(r"\end{enumerate}")
                if brk:
                    parts.append(r"\newpage")
                parts.append(section_hdr)
                parts.append(r"\begin{enumerate}[resume*]")
            else:
                if brk:
                    parts.append(r"\newpage")
                parts.append(section_hdr)
                parts.append(r"\begin{enumerate}")
                enum_started = True
        else:
            if brk:
                parts.append(r"\newpage")
            if not enum_started:
                parts.append(r"\begin{enumerate}")
                enum_started = True
        parts.append(f"\\item {text_tex}\n\\oli{{{oli_h}}}")
    if enum_started:
        parts.append(r"\end{enumerate}")

    # Answer section starts on a clean new page with reset counter and dapan pagestyle
    parts.append(r"""
\newpage
\pagestyle{dapan}
\setcounter{page}{1}
\begin{center}
  {\Large\bfseries\color{ink} BẢNG ĐÁP ÁN \& HƯỚNG DẪN GIẢI CHI TIẾT}\\[3pt]
  {\small\color{gray!75!black} Đề cương ôn tập Toán 10 — Chương V \& Chương VI (70 câu trả lời ngắn)}
\end{center}
\vspace{2pt}
""")
    parts.append(table_tex)
    parts.append(r"\vspace{4pt}")
    parts.append(r"\setlength{\columnsep}{16pt}")
    parts.append(r"\parttitle{HƯỚNG DẪN GIẢI CHI TIẾT CHƯƠNG V (CÂU 1 – CÂU 20)}")
    parts.append(r"\begin{multicols}{2}")
    parts.append(r"\small\sloppy")
    for s in sols[:20]:
        parts.append(s + r"\par\vspace{3pt}")
    parts.append(r"\end{multicols}")

    parts.append(r"\parttitle{HƯỚNG DẪN GIẢI CHI TIẾT CHƯƠNG VI (CÂU 21 – CÂU 70)}")
    parts.append(r"\begin{multicols}{2}")
    parts.append(r"\small\sloppy")
    for s in sols[20:]:
        parts.append(s + r"\par\vspace{3pt}")
    parts.append(r"\end{multicols}")
    parts.append(r"\end{document}")
    return "\n\n".join(parts)


def run_pdflatex():
    cmd = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", TEX_PATH.name]
    res = subprocess.run(cmd, cwd=OUT_DIR, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if res.returncode != 0:
        log_txt = res.stdout.decode("utf-8", errors="replace")
        raise RuntimeError(f"pdflatex failed!\n{log_txt[-2500:]}")


def find_ans_start_page(pdf_path: Path) -> int:
    doc = pymupdf.open(pdf_path)
    for i, page in enumerate(doc):
        txt = page.get_text("text")
        if "148000" in txt and "79,46" in txt and "343" in txt:
            doc.close()
            return i
    doc.close()
    raise RuntimeError("Could not locate Answer Key start page in compiled PDF!")


def audit_pagination(exam_pdf: Path):
    doc = pymupdf.open(exam_pdf)
    print(f"\n=== AUDIT EXAM PDF ({len(doc)} pages) ===")
    all_ok = True
    seen_qs = []
    for pno, page in enumerate(doc, start=1):
        txt = page.get_text("text")
        qs = re.findall(r"Câu\s+(\d+)\.", txt)
        bl_count = txt.count("Bài làm:")
        # Check bottom-most y coordinate of drawings / text
        rect = page.rect
        max_y = 0
        for d in page.get_drawings():
            max_y = max(max_y, d["rect"].y1)
        status = "OK" if len(qs) == bl_count else "MISMATCH!"
        if len(qs) != bl_count:
            all_ok = False
        seen_qs.extend([int(q) for q in qs])
        print(f"  Page {pno:2d}: Qs={qs} | grids={bl_count} | max_y={max_y:.1f}/{rect.height:.1f}pt [{status}]")
    doc.close()
    expected = list(range(1, 71))
    if seen_qs != expected:
        missing = set(expected) - set(seen_qs)
        raise RuntimeError(f"Question numbering mismatch! Missing={missing}")
    if not all_ok:
        raise RuntimeError("Some question text was split across pages from its grid box!")
    print("Pagination check PASSED: 70 questions, 0 split boxes!")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    # Pass 1: initial compile to discover exact exam_pages and total_pages
    TEX_PATH.write_text(generate_tex("XX", "YY"), encoding="utf-8")
    print("[1/4] Pass 1 pdflatex...")
    run_pdflatex()

    ans_start = find_ans_start_page(FULL_PDF)
    doc = pymupdf.open(FULL_PDF)
    total_pages = len(doc)
    doc.close()

    exam_pages = ans_start
    ans_pages = total_pages - exam_pages
    print(f"[2/4] Detected exam_pages={exam_pages}, ans_pages={ans_pages} (total={total_pages}). Updating footers...")

    # Pass 2 & 3: inject exact total page counts and compile twice for references/footers
    TEX_PATH.write_text(generate_tex(str(exam_pages), str(ans_pages)), encoding="utf-8")
    run_pdflatex()
    run_pdflatex()

    # Re-verify split point didn't shift
    ans_start2 = find_ans_start_page(FULL_PDF)
    doc = pymupdf.open(FULL_PDF)
    total2 = len(doc)
    assert ans_start2 == exam_pages and total2 == total_pages, f"Page counts shifted: {ans_start2}/{total2}"

    # Split into Exam and Answer Key PDFs
    print("[3/4] Splitting into De_Cuong.pdf and De_Cuong_Ans.pdf...")
    exam_doc = pymupdf.open()
    exam_doc.insert_pdf(doc, from_page=0, to_page=exam_pages - 1)
    exam_doc.save(EXAM_PDF)
    exam_doc.close()

    ans_doc = pymupdf.open()
    ans_doc.insert_pdf(doc, from_page=exam_pages, to_page=total_pages - 1)
    ans_doc.save(ANS_PDF)
    ans_doc.close()
    doc.close()

    audit_pagination(EXAM_PDF)

    print("[4/4] Exporting PDFs to Grade 10 teaching folders...")
    for dst, kind in EXPORT_TARGETS:
        dst.parent.mkdir(parents=True, exist_ok=True)
        src = EXAM_PDF if kind == "exam" else ANS_PDF
        shutil.copy2(src, dst)
        print(f"  Copied -> {dst}")

    print("\nBUILD COMPLETE!")


if __name__ == "__main__":
    main()
