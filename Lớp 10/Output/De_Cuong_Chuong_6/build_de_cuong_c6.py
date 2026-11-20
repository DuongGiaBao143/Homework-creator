#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Build pipeline for Grade 10 Review Worksheet: Chương VI. Hàm số, đồ thị và ứng dụng (Toán 10 KNTT).
50 questions total: 20 Multiple-Choice (ABCD) + 30 Short-Answer (with large grid boxes \oli{}).
"""

import re
import shutil
import subprocess
from pathlib import Path
import pymupdf

OUT_DIR = Path(r"d:\Tao_De\Lớp 10\Output\De_Cuong_Chuong_6")
TEX_PATH = OUT_DIR / "De_Cuong_Chuong_6.tex"
FULL_PDF = OUT_DIR / "De_Cuong_Chuong_6.pdf"
EXAM_PDF = OUT_DIR / "De_Cuong.pdf"
ANS_PDF = OUT_DIR / "De_Cuong_Ans.pdf"

EXPORT_TARGETS = [
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\Chương VI\De_Cuong_Chuong_6.pdf"), "exam"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\Chương VI\De_Cuong_Chuong_6_Ans.pdf"), "ans"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương VI\Đề cương ôn tập Chương 6 (50 câu).pdf"), "exam"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương VI\Ans\Đề cương ôn tập Chương 6 (50 câu) - Đáp án.pdf"), "ans"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương VI\Ans\Đề cương ôn tập Chương 6 (50 câu) có đáp án.pdf"), "full"),
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


def build_header_quote_macro(max_pages: int = 40) -> str:
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
\usetikzlibrary{calc,angles,quotes,arrows.meta,babel}

\definecolor{ink}{RGB}{30,55,70}
\definecolor{accent}{RGB}{18,82,112}

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
  \lfoot{\small\textit{\color{gray!60!black}Đáp án Đề cương Ôn tập Chương VI (50 câu) — Toán 10 KNTT}}
  \rfoot{\small Trang \thepage/__ANS_PAGES__}
  \renewcommand{\headrulewidth}{0.4pt}
  \renewcommand{\footrulewidth}{0pt}
}

\newcommand{\chapterbanner}[2]{%
  \par\vspace{3pt}\noindent
  \begin{tikzpicture}
    \node[draw=accent, fill=accent!6, rounded corners=4pt, inner xsep=10pt, inner ysep=6pt, text width=\dimexpr\linewidth-20.8pt\relax, line width=0.8pt] {%
      {\large\bfseries\color{ink}#1}\\[2pt]
      {\small\color{gray!75!black}#2}%
    };
  \end{tikzpicture}\par\nopagebreak\vspace{5pt}
}

\newcommand{\parttitle}[1]{\par\vspace{3pt}\needspace{3\baselineskip}{\normalsize\bfseries\color{accent}#1}\par\nopagebreak\vspace{2pt}}
\newcommand{\four}[4]{\par\nopagebreak\vspace{1.5pt}\noindent\begin{tabularx}{\linewidth}{@{}*{4}{>{\raggedright\arraybackslash}X}@{}}\textbf{A.} #1&\textbf{B.} #2&\textbf{C.} #3&\textbf{D.} #4\end{tabularx}}
\newcommand{\two}[4]{\par\nopagebreak\vspace{1.5pt}\noindent\begin{tabularx}{\linewidth}{@{}*{2}{>{\raggedright\arraybackslash}X}@{}}\textbf{A.} #1&\textbf{B.} #2\\[3.8pt]\textbf{C.} #3&\textbf{D.} #4\end{tabularx}}

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
"""

TIKZ_P2_Q4 = r"""\begin{tikzpicture}[scale=0.45, >=Stealth]
  \draw[step=1, color=gray!22, line width=0.2pt] (-4.5,-1.5) grid (5.5,5.5);
  \draw[->, line width=0.6pt] (-4.8,0) -- (5.8,0) node[below, font=\scriptsize] {$x$};
  \draw[->, line width=0.6pt] (0,-1.8) -- (0,5.8) node[right, font=\scriptsize] {$y$};
  \node[above right, font=\scriptsize] at (0,0) {$O$};
  \draw[dashed, gray!70, line width=0.4pt] (-4,0) -- (-4,-1) -- (0,-1);
  \draw[dashed, gray!70, line width=0.4pt] (-1,0) -- (-1,5) -- (0,5);
  \draw[dashed, gray!70, line width=0.4pt] (3,0) -- (3,1) -- (0,1);
  \draw[dashed, gray!70, line width=0.4pt] (5,0) -- (5,4) -- (0,4);
  \draw[accent, line width=1.25pt] (-4,-1) -- (-1,5) -- (3,1) -- (5,4);
  \foreach \x/\y in {-4/-1, -1/5, 3/1, 5/4} {
    \fill[accent] (\x,\y) circle (2.6pt);
  }
  \node[above, font=\scriptsize] at (-4,0) {$-4$};
  \node[below, font=\scriptsize] at (-1,0) {$-1$};
  \node[below, font=\scriptsize] at (3,0) {$3$};
  \node[below, font=\scriptsize] at (5,0) {$5$};
  \node[right, font=\scriptsize] at (0,-1) {$-1$};
  \node[left, font=\scriptsize] at (0,1) {$1$};
  \node[left, font=\scriptsize] at (0,4) {$4$};
  \node[right, font=\scriptsize] at (0,5) {$5$};
\end{tikzpicture}"""

TIKZ_P2_Q9 = r"""\begin{tikzpicture}[scale=0.48, >=Stealth]
  \draw[step=1, color=gray!22, line width=0.2pt] (-3.5,-1.5) grid (2.5,4.8);
  \draw[->, line width=0.6pt] (-3.8,0) -- (2.8,0) node[below, font=\scriptsize] {$x$};
  \draw[->, line width=0.6pt] (0,-1.8) -- (0,5.0) node[right, font=\scriptsize] {$y$};
  \node[below right, font=\scriptsize] at (0,0) {$O$};
  \draw[dashed, gray!70] (-1,0) -- (-1,4) -- (0,4);
  \draw[dashed, gray!70] (-1,-1.5) -- (-1,4.8);
  \draw[thick, accent, domain=-3.3:1.3, samples=100] plot (\x, {-(\x)^2 - 2*(\x) + 3});
  \fill[accent] (-1,4) circle (2.4pt) node[above left, font=\scriptsize] {$I(-1;4)$};
  \fill[ink] (-3,0) circle (2pt) node[below left, font=\scriptsize] {$-3$};
  \fill[ink] (1,0) circle (2pt) node[below right, font=\scriptsize] {$1$};
  \fill[ink] (0,3) circle (2pt) node[above right, font=\scriptsize] {$3$};
  \node[right, font=\scriptsize] at (0,4) {$4$};
  \node[below, font=\scriptsize] at (-1,0) {$-1$};
\end{tikzpicture}"""

TIKZ_P2_Q30 = r"""\begin{tikzpicture}[scale=0.38, >=Stealth]
  \fill[cyan!8] (-1,0) rectangle (13,5.2);
  \draw[thick, ink] (-1,0) -- (13,0);
  \coordinate (H) at (0,0);
  \coordinate (A) at (0,4);
  \coordinate (M) at (3,0);
  \coordinate (B) at (12,0);
  \draw[dashed, gray!80] (A) -- (H);
  \draw[line width=1.3pt, accent] (B) -- (M) -- (A);
  \fill[ink] (A) circle (3pt) node[above, font=\scriptsize] {Đảo $A$};
  \fill[ink] (H) circle (2.5pt) node[below, font=\scriptsize] {$H$};
  \fill[accent] (M) circle (2.8pt) node[below, font=\scriptsize] {$M$};
  \fill[ink] (B) circle (2.8pt) node[below, font=\scriptsize] {Trạm $B$};
  \node[left, font=\scriptsize] at (0,2) {$4\text{ km}$};
  \node[above, font=\scriptsize, accent] at (1.5,0) {$x$};
  \draw[<->, gray!80!black] (0,-1.1) -- (12,-1.1) node[midway, below, font=\scriptsize] {$12\text{ km}$};
  \draw (0.5,0) -- (0.5,0.5) -- (0,0.5);
\end{tikzpicture}"""


def side_by_side(text_tex: str, tikz_tex: str, text_ratio: float = 0.62) -> str:
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


def get_mcq_list():
    # (section_header_or_None, text_tex, options_tex, break_before_bool)
    return [
        (r"\parttitle{Bài 15. Hàm số và đồ thị}",
         r"Tập xác định $D$ của hàm số $y = \dfrac{\sqrt{x + 2}}{x^2 - 1}$ là",
         r"\two{$(-2; +\infty) \setminus \{1\}$.}{$[-2; +\infty) \setminus \{1\}$.}{$[-2; +\infty) \setminus \{-1; 1\}$.}{$\mathbb{R} \setminus \{-1; 1\}$.}",
         False),
        (None,
         r"Điểm nào sau đây thuộc đồ thị hàm số $y = \dfrac{2x - 1}{\sqrt{x + 3}}$?",
         r"\four{$M\left(1; \dfrac{1}{2}\right)$.}{$N(-3; 0)$.}{$P(6; 3)$.}{$Q(1; 1)$.}",
         False),
        (None,
         r"Cho hàm số $f(x) = \begin{cases} 3x - 2 & \text{khi } x \ge 2 \\ x^2 + 1 & \text{khi } x < 2 \end{cases}$. Giá trị của biểu thức $P = f(4) + f(-1)$ bằng",
         r"\four{$10$.}{$8$.}{$14$.}{$12$.}",
         False),
        (None,
         r"Cho hàm số $y = f(x)$ có đồ thị là đường gấp khúc đi qua các điểm $A(-3; 1)$, $B(-1; 4)$, $C(2; 0)$, $D(5; 3)$. Hàm số nghịch biến trên khoảng nào sau đây?",
         r"\four{$(-3; -1)$.}{$(-1; 2)$.}{$(2; 5)$.}{$(-3; 2)$.}",
         False),
        (None,
         r"Tập giá trị của hàm số $y = 4 - \sqrt{9 - x^2}$ là",
         r"\four{$[0; 3]$.}{$[0; 4]$.}{$(-\infty; 4]$.}{$[1; 4]$.}",
         False),
        (r"\parttitle{Bài 16. Hàm số bậc hai}",
         r"Tọa độ đỉnh $I$ của parabol $(P): y = -2x^2 + 8x - 3$ là",
         r"\four{$I(-2; -27)$.}{$I(2; 5)$.}{$I(4; -3)$.}{$I(2; 13)$.}",
         False),
        (None,
         r"Hàm số bậc hai $y = 3x^2 - 6x + 4$ đồng biến trên khoảng nào sau đây?",
         r"\four{$(1; +\infty)$.}{$(-\infty; 1)$.}{$(-1; +\infty)$.}{$(-\infty; 2)$.}",
         False),
        (None,
         r"Parabol $(P): y = x^2 - 5x + 6$ cắt trục hoành tại hai điểm phân biệt $A, B$. Độ dài đoạn thẳng $AB$ bằng",
         r"\four{$5$.}{$6$.}{$1$.}{$2$.}",
         False),
        (None,
         r"Cho parabol $(P): y = ax^2 + bx + c$ ($a \ne 0$) quay bề lõm lên trên, có đỉnh $I(-1; -4)$ và cắt trục tung tại điểm có tung độ bằng $-3$. Khẳng định nào sau đây đúng?",
         r"\two{$a > 0,\; b < 0,\; c < 0$.}{$a > 0,\; b > 0,\; c < 0$.}{$a < 0,\; b > 0,\; c < 0$.}{$a > 0,\; b > 0,\; c > 0$.}",
         False),
        (None,
         r"Giá trị lớn nhất của hàm số $y = x^2 - 2x - 3$ trên đoạn $[0; 4]$ bằng",
         r"\four{$-4$.}{$-3$.}{$1$.}{$5$.}",
         False),
        (None,
         r"Biết parabol $(P): y = x^2 + bx + c$ có trục đối xứng $x = 3$ và đi qua điểm $M(1; 0)$. Giá trị của tổng $b + c$ bằng",
         r"\four{$-1$.}{$1$.}{$-11$.}{$11$.}",
         True),
        (r"\parttitle{Bài 17. Dấu của tam thức bậc hai}",
         r"Tam thức bậc hai nào sau đây nhận giá trị dương với mọi $x \in \mathbb{R}$?",
         r"\two{$f(x) = x^2 - 4x + 4$.}{$f(x) = -x^2 + 4x - 5$.}{$f(x) = x^2 - 4x + 5$.}{$f(x) = x^2 - 5x + 4$.}",
         False),
        (None,
         r"Cho tam thức bậc hai $f(x) = -2x^2 + 5x - 2$. Tập hợp tất cả các giá trị của $x$ để $f(x) > 0$ là",
         r"\two{$\left(-\infty; \dfrac{1}{2}\right) \cup (2; +\infty)$.}{$\left[\dfrac{1}{2}; 2\right]$.}{$(-\infty; 2)$.}{$\left(\dfrac{1}{2}; 2\right)$.}",
         False),
        (None,
         r"Tập nghiệm $S$ của bất phương trình $3x^2 - 7x + 2 \ge 0$ là",
         r"\two{$\left(-\infty; \dfrac{1}{3}\right] \cup [2; +\infty)$.}{$\left[\dfrac{1}{3}; 2\right]$.}{$\left(-\infty; \dfrac{1}{3}\right) \cup (2; +\infty)$.}{$\left(\dfrac{1}{3}; 2\right)$.}",
         False),
        (None,
         r"Số nghiệm nguyên của bất phương trình $x^2 - 4x - 5 < 0$ là",
         r"\four{$7$.}{$6$.}{$5$.}{$4$.}",
         False),
        (None,
         r"Tất cả các giá trị của tham số $m$ để tam thức $f(x) = x^2 - 2mx + m + 2$ luôn dương với mọi $x \in \mathbb{R}$ là",
         r"\two{$m \in [-1; 2]$.}{$m \in (-1; 2)$.}{$m \in (-\infty; -1) \cup (2; +\infty)$.}{$m \in (-2; 1)$.}",
         False),
        (r"\parttitle{Bài 18. Phương trình quy về phương trình bậc hai}",
         r"Tập nghiệm của phương trình $\sqrt{x^2 + 3x - 2} = \sqrt{1 + x}$ là",
         r"\four{$\{1\}$.}{$\{-3\}$.}{$\{-3; 1\}$.}{$\varnothing$.}",
         False),
        (None,
         r"Số nghiệm thực của phương trình $\sqrt{2x^2 - 4x + 9} = x + 1$ là",
         r"\four{$0$.}{$1$.}{$3$.}{$2$.}",
         False),
        (None,
         r"Tổng các nghiệm thực của phương trình $\sqrt{x^2 - 4x + 3} = x - 3$ bằng",
         r"\four{$4$.}{$1$.}{$3$.}{$0$.}",
         False),
        (None,
         r"Tích tất cả các nghiệm thực của phương trình $\sqrt{3x^2 - 6x + 1} = \sqrt{2x^2 - 3x - 1}$ bằng",
         r"\four{$1$.}{$2$.}{$-2$.}{$3$.}",
         False),
    ]


def get_short_questions():
    # (section_header_or_None, text_tex, oli_height, break_before_bool)
    return [
        # Chủ đề 1: Bài 15 (Q1 - Q6)
        (r"\chapterbanner{PHẦN II. CÂU TRẢ LỜI NGẮN (30 CÂU)}{(Học sinh tính toán, trình bày lời giải chi tiết vào ô li bên dưới và điền kết quả vào ô Đáp số)}"
         + "\n" + r"\parttitle{Chủ đề 1. Hàm số và đồ thị (Bài 15)}",
         r"Tập xác định của hàm số $y = \sqrt{6 - x} + \dfrac{2x}{\sqrt{x + 2}}$ chứa bao nhiêu số nguyên?\answerbox",
         "4.5cm", True),
        (None,
         r"Có bao nhiêu giá trị nguyên của tham số $m \in [-5; 10]$ để hàm số $y = \sqrt{x - m + 1} + \dfrac{1}{\sqrt{2m + 5 - x}}$ xác định trên nửa khoảng $[2; 6)$?\answerbox",
         "4.5cm", False),
        (None,
         r"Cho hàm số $f(x) = \begin{cases} 3x - 5 & \text{khi } x \ge 3 \\ \sqrt{7 - x} & \text{khi } -2 \le x < 3 \\ x^2 + 4 & \text{khi } x < -2 \end{cases}$. Tính giá trị biểu thức $T = f(5) + f(-2) + f(-3)$.\answerbox",
         "4.5cm", False),

        # Page break -> Q4, Q5, Q6
        (None,
         side_by_side(
             r"Cho hàm số $y = f(x)$ xác định trên đoạn $[-4; 5]$ có đồ thị là đường gấp khúc như hình vẽ bên. Gọi $M, m$ lần lượt là giá trị lớn nhất, nhỏ nhất của hàm số trên đoạn $[-4; 5]$, và $(a; b)$ là khoảng mà hàm số nghịch biến. Tính giá trị của $M + m + a + b$.\answerbox",
             TIKZ_P2_Q4, text_ratio=0.56),
         "5.0cm", True),
        (None,
         r"Giá cước của một hãng taxi quy định như sau: $1\text{ km}$ đầu tiên (mở cửa) có giá $15\,000$ đồng; từ trên $1\text{ km}$ đến $15\text{ km}$ có giá $14\,000$ đồng/km; từ trên $15\text{ km}$ trở đi có giá $11\,000$ đồng/km. Một hành khách đi quãng đường $20\text{ km}$ phải trả bao nhiêu nghìn đồng?\answerbox",
         "5.0cm", False),
        (None,
         r"Có bao nhiêu giá trị nguyên của tham số $m \in [-6; 6]$ để hàm số bậc nhất $y = (m^2 - 9)x + 3m - 1$ nghịch biến trên $\mathbb{R}$?\answerbox",
         "5.0cm", False),

        # Page break -> Chủ đề 2 (Bài 16): Q7, Q8, Q9
        (r"\parttitle{Chủ đề 2. Hàm số bậc hai và ứng dụng thực tế (Bài 16)}",
         r"Cho parabol $(P): y = 3x^2 - 12x + 7$ có đỉnh $I(x_I; y_I)$. Tính giá trị biểu thức $P = x_I - 2y_I$.\answerbox",
         "5.0cm", True),
        (None,
         r"Parabol $(P): y = ax^2 + bx + c$ ($a \ne 0$) có đỉnh $I(1; -4)$ và đi qua điểm $A(3; 0)$. Tính giá trị của $a + 2b + 3c$.\answerbox",
         "5.0cm", False),
        (None,
         side_by_side(
             r"Cho hàm số bậc hai $y = ax^2 + bx + c$ ($a \ne 0$) có đồ thị là parabol như hình vẽ bên. Tính giá trị của biểu thức $2a - b + c$.\answerbox",
             TIKZ_P2_Q9, text_ratio=0.58),
         "5.0cm", False),

        # Page break -> Q10, Q11, Q12
        (None,
         r"Tìm giá trị của tham số $m$ để đường thẳng $d: y = 3x + m$ cắt parabol $(P): y = x^2 - x + 2$ tại hai điểm phân biệt $A, B$ sao cho trung điểm $I$ của đoạn thẳng $AB$ có tung độ bằng $8$.\answerbox",
         "5.5cm", True),
        (None,
         r"Tìm giá trị nguyên lớn nhất của tham số $m$ để hàm số $y = x^2 - 2(m + 1)x + 5$ đồng biến trên khoảng $(3; +\infty)$.\answerbox",
         "5.5cm", False),
        (None,
         r"Một cổng chào hình parabol có chiều cao là $9\text{ m}$ và bề rộng chân cổng ở mặt đất là $6\text{ m}$. Hỏi tại độ cao $5\text{ m}$ so với mặt đất, bề rộng của cổng bằng bao nhiêu mét?\answerbox",
         "5.5cm", False),

        # Page break -> Q13, Q14, Q15
        (None,
         r"Một quả bóng được ném xiên từ độ cao $1{,}5\text{ m}$ theo quỹ đạo parabol $h(x) = -0{,}05x^2 + x + 1{,}5$ (m), với $x$ là khoảng cách theo phương ngang (tính theo mét). Độ cao lớn nhất mà quả bóng đạt được bằng bao nhiêu mét?\answerbox",
         "5.5cm", True),
        (None,
         r"Một rạp chiếu phim bán vé với giá $100$ nghìn đồng/vé thì mỗi suất chiếu bán được $120$ vé. Qua khảo sát, cứ mỗi lần giảm giá bán $5$ nghìn đồng/vé thì số vé bán được tăng thêm $10$ vé. Rạp nên đặt giá vé bao nhiêu nghìn đồng để doanh thu của mỗi suất chiếu đạt cao nhất?\answerbox",
         "5.5cm", False),
        (None,
         r"Một người thợ có $120\text{ m}$ lưới thép muốn rào thành hai chuồng trại hình chữ nhật bằng nhau nằm sát cạnh nhau (chung một vách ngăn ở giữa, và tận dụng một bức tường dài có sẵn làm cạnh sau không cần rào). Tổng diện tích lớn nhất của hai chuồng trại có thể rào được là bao nhiêu $\text{m}^2$?\answerbox",
         "5.5cm", False),

        # Page break -> Chủ đề 3 (Bài 17): Q16, Q17, Q18
        (r"\parttitle{Chủ đề 3. Dấu của tam thức bậc hai và bất phương trình (Bài 17)}",
         r"Tính tổng tất cả các nghiệm nguyên của bất phương trình $-x^2 + 3x + 10 \ge 0$.\answerbox",
         "5.5cm", True),
        (None,
         r"Hệ bất phương trình $\begin{cases} x^2 - 6x + 5 \le 0 \\ x^2 - 4x + 3 > 0 \end{cases}$ có bao nhiêu nghiệm nguyên?\answerbox",
         "5.5cm", False),
        (None,
         r"Có bao nhiêu số nguyên $x \in [-5; 10]$ là nghiệm của bất phương trình $\dfrac{x^2 - 5x + 4}{x^2 - 16} \le 0$?\answerbox",
         "5.5cm", False),

        # Page break -> Q19, Q20, Q21
        (None,
         r"Có bao nhiêu giá trị nguyên của tham số $m$ để bất phương trình $(m - 1)x^2 - 2(m - 1)x + 3 > 0$ nghiệm đúng với mọi $x \in \mathbb{R}$?\answerbox",
         "5.5cm", True),
        (None,
         r"Tìm giá trị nguyên lớn nhất của tham số $m$ để bất phương trình $x^2 - 6x + m \le 0$ nghiệm đúng với mọi $x \in [1; 4]$.\answerbox",
         "5.5cm", False),
        (None,
         r"Có bao nhiêu giá trị nguyên của tham số $m \in [-10; 10]$ để bất phương trình $\dfrac{x^2 - 2x + m}{x^2 + 2x + 5} > 0$ nghiệm đúng với mọi $x \in \mathbb{R}$?\answerbox",
         "5.5cm", False),

        # Page break -> Q22, Q23, Chủ đề 4 Q24
        (None,
         r"Một công ty sản xuất $x$ chiếc xe đạp điện mỗi tháng, biết tổng doanh thu là $R(x) = -0{,}5x^2 + 60x$ và tổng chi phí là $C(x) = 20x + 600$ (đơn vị: triệu đồng). Để công ty có lợi nhuận hàng tháng đạt ít nhất $150$ triệu đồng thì số lượng xe $x$ phải nằm trong đoạn $[a; b]$. Tính $b - a$.\answerbox",
         "5.0cm", True),
        (None,
         r"Một tấm biển quảng cáo hình chữ nhật có chu vi là $28\text{ m}$. Để diện tích tấm biển không nhỏ hơn $40\text{ m}^2$ và chiều dài lớn hơn chiều rộng, chiều rộng $x$ (m) phải thuộc nửa khoảng $[a; b)$. Tính giá trị của $a + b$.\answerbox",
         "5.0cm", False),
        (r"\parttitle{Chủ đề 4. Phương trình quy về phương trình bậc hai (Bài 18)}",
         r"Tìm tổng các nghiệm thực của phương trình $\sqrt{3x^2 - 6x + 4} = \sqrt{2x^2 - x - 2}$.\answerbox",
         "5.0cm", False),

        # Page break -> Q25, Q26, Q27
        (None,
         r"Tìm nghiệm lớn nhất của phương trình $\sqrt{2x^2 + 3x - 5} = \sqrt{x^2 + 5x + 10}$.\answerbox",
         "5.5cm", True),
        (None,
         r"Tìm nghiệm thực của phương trình $\sqrt{2x^2 - 7x - 11} = x - 3$.\answerbox",
         "5.5cm", False),
        (None,
         r"Tính tổng bình phương tất cả các nghiệm thực của phương trình $\sqrt{5x^2 - 13x + 10} = 2x - 2$.\answerbox",
         "5.5cm", False),

        # Page break -> Q28, Q29, Q30 (TikZ)
        (None,
         r"Tính tổng tất cả các nghiệm thực của phương trình $x^2 - 4x - 5\sqrt{x^2 - 4x + 5} + 9 = 0$.\answerbox",
         "5.5cm", True),
        (None,
         r"Có bao nhiêu giá trị nguyên của tham số $m \in [-8; 8]$ để phương trình $\sqrt{x^2 - 4x + 13} = x + m$ có nghiệm thực?\answerbox",
         "5.5cm", False),
        (None,
         side_by_side(
             r"Một hòn đảo $A$ cách bờ biển thẳng một khoảng $AH = 4\text{ km}$. Một trạm phát điện đặt tại điểm $B$ trên bờ biển cách chân đường vuông góc $H$ một đoạn $HB = 12\text{ km}$ (như hình vẽ bên). Người ta kéo dây cáp từ $B$ dọc bờ biển đến điểm $M$ nằm giữa $B$ và $H$, rồi kéo cáp ngầm từ $M$ ra đảo $A$. Biết tổng chiều dài dây cáp sử dụng là $14\text{ km}$. Hỏi điểm $M$ cách $H$ bao nhiêu kilômét?\answerbox",
             TIKZ_P2_Q30, text_ratio=0.56),
         "5.0cm", False),
    ]


def generate_tex(exam_pages_str: str = "XX", ans_pages_str: str = "YY") -> str:
    preamble = PREAMBLE.replace("__HEADER_QUOTE__", build_header_quote_macro(40))
    preamble = preamble.replace("__EXAM_PAGES__", exam_pages_str)
    preamble = preamble.replace("__ANS_PAGES__", ans_pages_str)

    parts = [preamble, r"\begin{document}"]

    # Top Banner + PART I
    parts.append(r"""\chapterbanner{ĐỀ CƯƠNG ÔN TẬP CHƯƠNG VI: HÀM SỐ, ĐỒ THỊ VÀ ỨNG DỤNG}{Môn Toán 10 — Kết nối tri thức với cuộc sống \quad|\quad Tổng cộng: 50 câu (20 Trắc nghiệm + 30 Trả lời ngắn)}

\parttitle{PHẦN I. CÂU TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN (20 CÂU)}
\textit{Thí sinh khoanh tròn vào chữ cái đứng trước phương án trả lời đúng nhất.}""")

    mcqs = get_mcq_list()
    in_enum = False
    for idx, (sec, qtxt, opts, brk) in enumerate(mcqs):
        if brk or sec:
            if in_enum:
                parts.append(r"\end{enumerate}")
                in_enum = False
            if brk:
                parts.append(r"\newpage")
            if sec:
                parts.append(sec)
        if not in_enum:
            parts.append(r"\begin{enumerate}" if idx == 0 else r"\begin{enumerate}[resume*]")
            in_enum = True
        parts.append(rf"""\needspace{{4\baselineskip}}\item {qtxt}
{opts}""")
    if in_enum:
        parts.append(r"\end{enumerate}")

    # PART II (30 Short-Answer with grid boxes)
    short_qs = get_short_questions()
    in_enum = False
    for idx, (sec, qtxt, oli_h, brk) in enumerate(short_qs):
        if brk or sec:
            if in_enum:
                parts.append(r"\end{enumerate}")
                in_enum = False
            if brk:
                parts.append(r"\newpage")
            if sec:
                parts.append(sec)
        if not in_enum:
            parts.append(r"\begin{enumerate}" if idx == 0 else r"\begin{enumerate}[resume*]")
            in_enum = True
        parts.append(rf"\item {qtxt}" + "\n" + rf"\oli{{{oli_h}}}")
    if in_enum:
        parts.append(r"\end{enumerate}")

    # ==================== ĐÁP ÁN & HƯỚNG DẪN GIẢI ====================
    parts.append(r"""\newpage
\pagestyle{dapan}
\setcounter{page}{1}

\begin{center}
  {\Large\bfseries\color{ink} BẢNG ĐÁP ÁN TỔNG HỢP (50 CÂU)}\\[2pt]
  {\small\color{gray!75!black} Đề cương Ôn tập Chương VI: Hàm số, Đồ thị và Ứng dụng — Toán 10 KNTT}
\end{center}
\vspace{2pt}

\noindent\textbf{PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (20 câu)}
\vspace{1.5pt}
\begin{center}
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|}
\hline
\textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{7} & \textbf{8} & \textbf{9} & \textbf{10} \\ \hline
\textbf{C} & \textbf{A} & \textbf{D} & \textbf{B} & \textbf{D} & \textbf{B} & \textbf{A} & \textbf{C} & \textbf{B} & \textbf{D} \\ \hline
\hline
\textbf{11} & \textbf{12} & \textbf{13} & \textbf{14} & \textbf{15} & \textbf{16} & \textbf{17} & \textbf{18} & \textbf{19} & \textbf{20} \\ \hline
\textbf{A} & \textbf{C} & \textbf{D} & \textbf{A} & \textbf{C} & \textbf{B} & \textbf{A} & \textbf{D} & \textbf{C} & \textbf{B} \\ \hline
\end{tabular}
\end{center}

\vspace{3pt}
\noindent\textbf{PHẦN II. Câu trắc nghiệm trả lời ngắn (30 câu)}
\vspace{1.5pt}
\begin{center}
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|C{0.8cm}|C{1.4cm}||C{0.8cm}|C{1.4cm}||C{0.8cm}|C{1.4cm}||C{0.8cm}|C{1.4cm}||C{0.8cm}|C{1.4cm}|}
\hline
\textbf{Câu} & \textbf{Đáp số} & \textbf{Câu} & \textbf{Đáp số} & \textbf{Câu} & \textbf{Đáp số} & \textbf{Câu} & \textbf{Đáp số} & \textbf{Câu} & \textbf{Đáp số} \\ \hline
\textbf{1}  & $8$      & \textbf{7}  & $12$     & \textbf{13} & $6{,}5$  & \textbf{19} & $3$   & \textbf{25} & $5$  \\ \hline
\textbf{2}  & $3$      & \textbf{8}  & $-12$    & \textbf{14} & $80$     & \textbf{20} & $5$   & \textbf{26} & $5$  \\ \hline
\textbf{3}  & $26$     & \textbf{9}  & $3$      & \textbf{15} & $1200$   & \textbf{21} & $9$   & \textbf{27} & $13$ \\ \hline
\textbf{4}  & $6$      & \textbf{10} & $2$      & \textbf{16} & $12$     & \textbf{22} & $20$  & \textbf{28} & $6$  \\ \hline
\textbf{5}  & $266$    & \textbf{11} & $2$      & \textbf{17} & $2$      & \textbf{23} & $11$  & \textbf{29} & $10$ \\ \hline
\textbf{6}  & $5$      & \textbf{12} & $4$      & \textbf{18} & $5$      & \textbf{24} & $5$   & \textbf{30} & $3$  \\ \hline
\end{tabular}
\end{center}

\vspace{4pt}
\begin{center}
  {\large\bfseries\color{ink} HƯỚNG DẪN GIẢI CHI TIẾT}
\end{center}
\vspace{1pt}

\begin{multicols}{2}
\raggedcolumns
\footnotesize

\textbf{\color{accent}PHẦN I. TRẮC NGHIỆM (20 CÂU)}

\textbf{Câu 1.} ĐK: $x + 2 \ge 0 \Leftrightarrow x \ge -2$ và $x^2 - 1 \ne 0 \Leftrightarrow x \ne \pm 1$. Chọn \textbf{C}.

\textbf{Câu 2.} Thay $x = 1 \Rightarrow y = \dfrac{2(1)-1}{\sqrt{1+3}} = \dfrac{1}{2}$. Chọn \textbf{A}.

\textbf{Câu 3.} $f(4) = 3(4) - 2 = 10$; $f(-1) = (-1)^2 + 1 = 2 \Rightarrow P = 12$. Chọn \textbf{D}.

\textbf{Câu 4.} Từ $B(-1; 4)$ đến $C(2; 0)$, khi $x$ tăng thì $y$ giảm nên hàm nghịch biến trên $(-1; 2)$. Chọn \textbf{B}.

\textbf{Câu 5.} Với $x \in [-3; 3]$, $0 \le \sqrt{9 - x^2} \le 3 \Rightarrow 1 \le 4 - \sqrt{9 - x^2} \le 4$. Chọn \textbf{D}.

\textbf{Câu 6.} $x_I = -\dfrac{8}{2(-2)} = 2$, $y_I = -2(4) + 16 - 3 = 5 \Rightarrow I(2; 5)$. Chọn \textbf{B}.

\textbf{Câu 7.} $a = 3 > 0$, trục đối xứng $x = 1 \Rightarrow$ đồng biến trên $(1; +\infty)$. Chọn \textbf{A}.

\textbf{Câu 8.} $x^2 - 5x + 6 = 0 \Leftrightarrow x = 2$ hoặc $x = 3 \Rightarrow AB = |3 - 2| = 1$. Chọn \textbf{C}.

\textbf{Câu 9.} Bề lõm lên $\Rightarrow a > 0$; $x_I = -\dfrac{b}{2a} = -1 \Rightarrow b = 2a > 0$; cắt $Oy$ tại $-3 \Rightarrow c = -3 < 0$. Chọn \textbf{B}.

\textbf{Câu 10.} Đỉnh $x = 1 \in [0; 4]$. $y(0) = -3, y(1) = -4, y(4) = 5 \Rightarrow \max = 5$. Chọn \textbf{D}.

\textbf{Câu 11.} $-\dfrac{b}{2} = 3 \Rightarrow b = -6$; qua $M(1; 0) \Rightarrow 1 - 6 + c = 0 \Rightarrow c = 5 \Rightarrow b + c = -1$. Chọn \textbf{A}.

\textbf{Câu 12.} $x^2 - 4x + 5 = (x - 2)^2 + 1 > 0\ \forall x \in \mathbb{R}$. Chọn \textbf{C}.

\textbf{Câu 13.} $-2x^2 + 5x - 2 > 0$ có $a = -2 < 0$ và hai nghiệm $\dfrac{1}{2}; 2 \Rightarrow x \in \left(\dfrac{1}{2}; 2\right)$. Chọn \textbf{D}.

\textbf{Câu 14.} $3x^2 - 7x + 2 = 0 \Leftrightarrow x = \dfrac{1}{3}$ hoặc $x = 2 \Rightarrow S = \left(-\infty; \dfrac{1}{3}\right] \cup [2; +\infty)$. Chọn \textbf{A}.

\textbf{Câu 15.} $x^2 - 4x - 5 < 0 \Leftrightarrow -1 < x < 5 \Rightarrow x \in \{0; 1; 2; 3; 4\}$ ($5$ nghiệm). Chọn \textbf{C}.

\textbf{Câu 16.} $a = 1 > 0$, yêu cầu $\Delta' = m^2 - m - 2 < 0 \Leftrightarrow -1 < m < 2$. Chọn \textbf{B}.

\textbf{Câu 17.} Bình phương: $x^2 + 3x - 2 = 1 + x \Leftrightarrow x^2 + 2x - 3 = 0 \Leftrightarrow x = 1$ hoặc $x = -3$. Thử lại $x = -3$ làm $1 + x = -2 < 0$ (loại), nhận $x = 1$. Chọn \textbf{A}.

\textbf{Câu 18.} ĐK $x \ge -1$. Bình phương: $2x^2 - 4x + 9 = x^2 + 2x + 1 \Leftrightarrow x^2 - 6x + 8 = 0 \Leftrightarrow x = 2; 4$ ($2$ nghiệm). Chọn \textbf{D}.

\textbf{Câu 19.} ĐK $x \ge 3$. Bình phương: $x^2 - 4x + 3 = x^2 - 6x + 9 \Leftrightarrow 2x = 6 \Leftrightarrow x = 3$ (nhận). Chọn \textbf{C}.

\textbf{Câu 20.} Bình phương: $x^2 - 3x + 2 = 0 \Leftrightarrow x = 1$ hoặc $x = 2$. Thử $x = 1$ cho $3 - 6 + 1 = -2 < 0$ (loại); thử $x = 2$ nhận. Vậy có duy nhất $x = 2$. Chọn \textbf{B}.

\columnbreak

\textbf{\color{accent}PHẦN II. TRẢ LỜI NGẮN (30 CÂU)}

\textbf{Câu 1.} ĐK: $-2 < x \le 6 \Rightarrow x \in \{-1; 0; 1; 2; 3; 4; 5; 6\}$ ($8$ số).

\textbf{Câu 2.} ĐK: $x \ge m - 1$ và $x < 2m + 5$. Để xác định trên $[2; 6)$: $m - 1 \le 2$ và $2m + 5 \ge 6 \Leftrightarrow 0{,}5 \le m \le 3 \Rightarrow m \in \{1; 2; 3\}$ ($3$ giá trị).

\textbf{Câu 3.} $f(5) = 10$, $f(-2) = \sqrt{9} = 3$, $f(-3) = 9 + 4 = 13 \Rightarrow T = 26$.

\textbf{Câu 4.} Từ đồ thị: $M = 5, m = -1$, nghịch biến trên $(-1; 3) \Rightarrow a = -1, b = 3 \Rightarrow 5 - 1 - 1 + 3 = 6$.

\textbf{Câu 5.} $15 + 14 \times 14 + 5 \times 11 = 15 + 196 + 55 = 266$ (nghìn đồng).

\textbf{Câu 6.} Hàm bậc nhất nghịch biến khi $m^2 - 9 < 0 \Leftrightarrow -3 < m < 3 \Rightarrow \{-2; -1; 0; 1; 2\}$ ($5$ giá trị).

\textbf{Câu 7.} $x_I = 2, y_I = 3(4) - 24 + 7 = -5 \Rightarrow P = 2 - 2(-5) = 12$.

\textbf{Câu 8.} $(P): y = a(x - 1)^2 - 4$. Qua $A(3; 0) \Rightarrow 4a - 4 = 0 \Rightarrow a = 1 \Rightarrow y = x^2 - 2x - 3 \Rightarrow a + 2b + 3c = 1 - 4 - 9 = -12$.

\textbf{Câu 9.} Đỉnh $I(-1; 4)$, qua $(0; 3) \Rightarrow y = -(x + 1)^2 + 4 = -x^2 - 2x + 3 \Rightarrow 2(-1) - (-2) + 3 = 3$.

\textbf{Câu 10.} $x^2 - 4x + 2 - m = 0 \Rightarrow x_I = 2$. $I \in d \Rightarrow y_I = 6 + m = 8 \Rightarrow m = 2$ ($\Delta' = 4 > 0$, thỏa).

\textbf{Câu 11.} $a = 1 > 0$, đồng biến trên $(3; +\infty) \Leftrightarrow x_I = m + 1 \le 3 \Leftrightarrow m \le 2 \Rightarrow m_{\max} = 2$.

\textbf{Câu 12.} Chọn trục tọa độ với đỉnh $(0; 9)$, qua $(\pm 3; 0) \Rightarrow y = -x^2 + 9$. Với $y = 5 \Rightarrow x^2 = 4 \Rightarrow x = \pm 2 \Rightarrow$ bề rộng $4\text{ m}$.

\textbf{Câu 13.} Đỉnh $x = -\dfrac{1}{2(-0{,}05)} = 10 \Rightarrow h_{\max} = h(10) = -5 + 10 + 1{,}5 = 6{,}5\text{ m}$.

\textbf{Câu 14.} Gọi số lần giảm $5$ nghìn là $x$: $R(x) = (100 - 5x)(120 + 10x) = -50x^2 + 400x + 12000$. Đạt cực đại tại $x = 4 \Rightarrow$ giá vé $100 - 20 = 80$ nghìn đồng.

\textbf{Câu 15.} Gọi chiều rộng $x \Rightarrow$ dài $120 - 3x$. $S(x) = -3x^2 + 120x$, đạt cực đại tại $x = 20 \Rightarrow S_{\max} = 20 \times 60 = 1200\text{ m}^2$.

\textbf{Câu 16.} $-2 \le x \le 5 \Rightarrow$ tổng $(-2) + (-1) + \dots + 5 = 12$.

\textbf{Câu 17.} $[1; 5] \cap ((-\infty; 1) \cup (3; +\infty)) = (3; 5] \Rightarrow x \in \{4; 5\}$ ($2$ nghiệm).

\textbf{Câu 18.} ĐK $x \ne \pm 4$. Rút gọn $\dfrac{x - 1}{x + 4} \le 0 \Leftrightarrow -4 < x \le 1 \Rightarrow \{-3; -2; -1; 0; 1\}$ ($5$ số).

\textbf{Câu 19.} $m = 1 \Rightarrow 3 > 0$ (đúng $\forall x$). $m \ne 1$: $m - 1 > 0$ và $\Delta' = (m-1)(m-4) < 0 \Leftrightarrow 1 < m < 4$. Vậy $m \in \{1; 2; 3\}$ ($3$ giá trị).

\textbf{Câu 20.} $m \le -x^2 + 6x\ \forall x \in [1; 4]$. Trên $[1; 4]$, $\min(-x^2 + 6x) = 5$ (tại $x=1$) $\Rightarrow m \le 5 \Rightarrow 5$.

\textbf{Câu 21.} Mẫu $x^2 + 2x + 5 > 0\ \forall x$. Tử $> 0\ \forall x \Leftrightarrow 1 - m < 0 \Leftrightarrow m > 1 \Rightarrow \{2;\dots;10\}$ ($9$ giá trị).

\textbf{Câu 22.} $L(x) = -0{,}5x^2 + 40x - 600 \ge 150 \Leftrightarrow x^2 - 80x + 1500 \le 0 \Leftrightarrow 30 \le x \le 50 \Rightarrow 50 - 30 = 20$.

\textbf{Câu 23.} $x(14 - x) \ge 40 \Leftrightarrow 4 \le x \le 10$. Điều kiện rộng $<$ dài $\Leftrightarrow x < 7 \Rightarrow [4; 7) \Rightarrow 4 + 7 = 11$.

\textbf{Câu 24.} $x^2 - 5x + 6 = 0 \Leftrightarrow x = 2; 3$ (cả hai thỏa ĐK) $\Rightarrow 2 + 3 = 5$.

\textbf{Câu 25.} $x^2 - 2x - 15 = 0 \Leftrightarrow x = 5$ hoặc $x = -3$ (cả hai thỏa ĐK) $\Rightarrow$ lớn nhất là $5$.

\textbf{Câu 26.} ĐK $x \ge 3$. Bình phương: $x^2 - x - 20 = 0 \Leftrightarrow x = 5$ (nhận) hoặc $x = -4$ (loại).

\textbf{Câu 27.} ĐK $x \ge 1$. Bình phương: $x^2 - 5x + 6 = 0 \Leftrightarrow x = 2; 3$ (nhận cả hai) $\Rightarrow 2^2 + 3^2 = 13$.

\textbf{Câu 28.} Đặt $t = \sqrt{x^2 - 4x + 5} \ge 1 \Rightarrow t^2 - 5t + 4 = 0 \Leftrightarrow t = 1$ ($x=2$) hoặc $t = 4$ ($x^2 - 4x - 11 = 0$, tổng 2 nghiệm $= 4$). Tổng tất cả các nghiệm $= 2 + 4 = 6$.

\textbf{Câu 29.} ĐK $x \ge -m$. Bình phương: $(2m + 4)x = 13 - m^2$. Cần $m \ne -2$ và $x + m = \dfrac{(m+2)^2 + 9}{2(m+2)} \ge 0 \Leftrightarrow m > -2 \Rightarrow \{-1; 0; \dots; 8\}$ ($10$ giá trị).

\textbf{Câu 30.} Đặt $MH = x$ ($0 \le x \le 12$). Ta có $\sqrt{x^2 + 16} + 12 - x = 14 \Leftrightarrow \sqrt{x^2 + 16} = x + 2 \Leftrightarrow 4x = 12 \Leftrightarrow x = 3\text{ km}$.

\end{multicols}
\end{document}
""")

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
        if "BẢNG ĐÁP ÁN TỔNG HỢP" in txt:
            doc.close()
            return i
    doc.close()
    raise RuntimeError("Could not locate Answer Key start page in compiled PDF!")


def audit_pagination(exam_pdf: Path, ans_pdf: Path):
    doc_exam = pymupdf.open(exam_pdf)
    print(f"\n=== AUDIT EXAM PDF ({len(doc_exam)} pages) ===")
    for pno, page in enumerate(doc_exam, start=1):
        txt = page.get_text("text")
        qs = re.findall(r"Câu\s+(\d+)\.", txt)
        rect = page.rect
        max_y = 0
        for d in page.get_drawings():
            max_y = max(max_y, d["rect"].y1)
        print(f"  Page {pno:2d}: Qs={qs} | max_y={max_y:.1f}/{rect.height:.1f}pt")
    doc_exam.close()

    doc_ans = pymupdf.open(ans_pdf)
    print(f"\n=== AUDIT ANS PDF ({len(doc_ans)} pages) ===")
    for pno, page in enumerate(doc_ans, start=1):
        rect = page.rect
        max_y = 0
        for d in page.get_drawings():
            max_y = max(max_y, d["rect"].y1)
        print(f"  Page {pno:2d}: max_y={max_y:.1f}/{rect.height:.1f}pt")
    doc_ans.close()


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
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

    TEX_PATH.write_text(generate_tex(str(exam_pages), str(ans_pages)), encoding="utf-8")
    run_pdflatex()
    run_pdflatex()

    ans_start2 = find_ans_start_page(FULL_PDF)
    doc = pymupdf.open(FULL_PDF)
    total2 = len(doc)
    assert ans_start2 == exam_pages and total2 == total_pages, f"Page counts shifted: {ans_start2}/{total2}"

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

    audit_pagination(EXAM_PDF, ANS_PDF)

    print("[4/4] Exporting PDFs to Grade 10 teaching folders...")
    src_map = {"exam": EXAM_PDF, "ans": ANS_PDF, "full": FULL_PDF}
    for dst, kind in EXPORT_TARGETS:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_map[kind], dst)
        print(f"  Copied -> {dst}")

    print("\nBUILD COMPLETE FOR ĐỀ CƯƠNG CHƯƠNG VI (50 CÂU)!")


if __name__ == "__main__":
    main()
