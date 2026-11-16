#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build pipeline for Grade 10 Review Exam 2: Chapters 5 & 6 (Toán 10 KNTT).
Generates standalone exam PDF and answer key PDF, audits pagination,
and exports copies to Grade 10 teaching folders.
"""

import os
import re
import shutil
import subprocess
from pathlib import Path
import pymupdf

BASE_DIR = Path(r"d:\Tao_De\Lớp 10\Output\De_On_Tap_Chuong_5_6_De_2")
OUT_DIR = BASE_DIR
TEX_PATH = OUT_DIR / "De_On_Tap_Chuong_5_6_De_2.tex"
FULL_PDF = OUT_DIR / "De_On_Tap_Chuong_5_6_De_2.pdf"
EXAM_PDF = OUT_DIR / "De_On_Tap_De_2.pdf"
ANS_PDF = OUT_DIR / "De_On_Tap_De_2_Ans.pdf"

EXPORT_TARGETS = [
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\Chương V - VI\De_On_Tap_Chuong_5_6_De_2.pdf"), "exam"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\Chương V - VI\De_On_Tap_Chuong_5_6_De_2_Ans.pdf"), "ans"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương V - VI\Đề ôn tập Chương 5 và 6 - Đề 2.pdf"), "exam"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương V - VI\Đề ôn tập Chương 5 và 6 - Đề 2 (Đáp án).pdf"), "ans"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương V - VI\Đề ôn tập Chương 5 và 6 - Đề 2 có đáp án.pdf"), "full"),
]

QUOTES = [
    "Math gives us hope that every problem has a solution",
    "Math + You = Champion",
    "Where Frustration Becomes Inspiration",
    "Turning Confusion into Clarity",
    "Don't be an X, be a Y of mathematics",
    "Don't get mad. Learn to add",
    "The only way to learn mathematics is to do mathematics",
    "Small steps every day lead to big results",
    "Every expert was once a beginner",
    "Success is the sum of small efforts repeated daily",
    "Mathematics is the music of reason",
    "Believe you can and you're halfway there",
]


def build_header_quote_macro(max_p: int = 30) -> str:
    lines = [r"\newcommand{\headerQuote}{%", r"  \ifcase\value{page}\relax"]
    for i in range(1, max_p + 1):
        q = QUOTES[(i - 1) % len(QUOTES)]
        lines.append(f"    \\or {q}% Trang {i}")
    lines.append(f"    \\else {QUOTES[0]}%")
    lines.append(r"  \fi")
    lines.append(r"}")
    return "\n".join(lines)


PREAMBLE = r"""\documentclass[10pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage[vietnamese]{babel}
\usepackage[margin=1.3cm,top=0.75cm,bottom=1.0cm,includehead,includefoot,headheight=18pt,headsep=5pt,footskip=16pt]{geometry}
\usepackage{amsmath,amssymb,array,tabularx,enumitem,fancyhdr,tikz,xcolor,needspace,multicol}
\usetikzlibrary{calc,angles,quotes,arrows.meta,babel,patterns}

\definecolor{ink}{RGB}{30,55,70}
\definecolor{accent}{RGB}{18,82,112}

\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}

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
  \lfoot{\small\textit{\color{gray!60!black}Đáp án Đề ôn tập Chương V \& VI (Đề 2) — Toán 10 KNTT}}
  \rfoot{\small Trang \thepage/__ANS_PAGES__}
  \renewcommand{\headrulewidth}{0.4pt}
  \renewcommand{\footrulewidth}{0pt}
}

\newcommand{\parttitle}[1]{\par\vspace{3.5pt}\needspace{3\baselineskip}{\large\bfseries\color{ink}#1}\par\nopagebreak\vspace{2pt}}
\newcommand{\four}[4]{\par\noindent\begin{tabularx}{\linewidth}{@{}*{4}{>{\raggedright\arraybackslash}X}@{}}\textbf{A.} #1&\textbf{B.} #2&\textbf{C.} #3&\textbf{D.} #4\end{tabularx}}
\newcommand{\two}[4]{\par\noindent\begin{tabularx}{\linewidth}{@{}*{2}{>{\raggedright\arraybackslash}X}@{}}\textbf{A.} #1&\textbf{B.} #2\\[3.8pt]\textbf{C.} #3&\textbf{D.} #4\end{tabularx}}
\newcommand{\one}[4]{\par\noindent\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X@{}}\textbf{A.} #1\\[4pt]\textbf{B.} #2\\[4pt]\textbf{C.} #3\\[4pt]\textbf{D.} #4\end{tabularx}}
\newcommand{\answerbox}{\hfill\mbox{\textit{Đáp số:}\ \fbox{\rule{0pt}{7.5pt}\hspace{1.8cm}}}}

\setlist[enumerate,1]{label=\textbf{Câu \arabic*.},leftmargin=1.1cm,labelsep=.1cm,itemsep=1.2pt,topsep=1.2pt,parsep=0pt}
\setlist[enumerate,2]{label=\alph*),leftmargin=.55cm,itemsep=1.5pt,topsep=0.2pt,parsep=0pt}
\newcolumntype{C}[1]{>{\centering\arraybackslash}m{#1}}
"""

TIKZ_P2_Q2 = r"""\begin{tikzpicture}[scale=0.52, >=Stealth]
  \draw[step=1, color=gray!25, line width=0.25pt] (-2,-1.5) grid (4.5,4.8);
  \draw[->, line width=0.6pt] (-2.2,0) -- (4.8,0) node[below, font=\scriptsize] {$x$};
  \draw[->, line width=0.6pt] (0,-1.7) -- (0,5.0) node[right, font=\scriptsize] {$y$};
  \node[below left, font=\scriptsize] at (0,0) {$O$};
  \draw[dashed, gray!70] (1,0) -- (1,4) -- (0,4);
  \draw[dashed, gray!70] (1,-1.5) -- (1,4.8);
  \draw[thick, accent, domain=-1.4:3.4, samples=100] plot (\x, {-(\x)^2 + 2*(\x) + 3});
  \fill[accent] (1,4) circle (2.2pt) node[above, font=\scriptsize] {$I(1;4)$};
  \fill[ink] (-1,0) circle (2pt) node[below left, font=\scriptsize] {$-1$};
  \fill[ink] (3,0) circle (2pt) node[below right, font=\scriptsize] {$3$};
  \fill[ink] (0,3) circle (2pt) node[left, font=\scriptsize] {$3$};
  \node[left, font=\scriptsize] at (0,4) {$4$};
  \node[below, font=\scriptsize] at (1,0) {$1$};
\end{tikzpicture}"""

TIKZ_P3_Q6 = r"""\begin{tikzpicture}[scale=0.48, >=Stealth]
  \draw[->, line width=0.6pt] (-0.5,0) -- (5.0,0) node[below, font=\tiny] {$t\text{ (s)}$};
  \draw[->, line width=0.6pt] (0,-0.4) -- (0,4.8) node[right, font=\tiny] {$h\text{ (m)}$};
  \node[below left, font=\tiny] at (0,0) {$O$};
  \draw[dashed, gray!70] (2,0) -- (2,4) -- (0,4);
  \draw[thick, domain=0:4, samples=80, accent] plot (\x, {-(\x)^2 + 4*(\x)});
  \fill[accent] (2,4) circle (2.2pt) node[above, font=\tiny] {$4\text{ m}$};
  \fill[ink] (4,0) circle (2pt) node[below, font=\tiny] {$4$};
  \node[below, font=\tiny] at (2,0) {$2$};
  \node[left, font=\tiny] at (0,4) {$4$};
  \draw[line width=0.5pt, gray!60] (-0.5,0) -- (4.8,0);
\end{tikzpicture}"""


def generate_tex(exam_pages_str: str = "XX", ans_pages_str: str = "YY") -> str:
    preamble = PREAMBLE.replace("__HEADER_QUOTE__", build_header_quote_macro(30))
    preamble = preamble.replace("__EXAM_PAGES__", exam_pages_str)
    preamble = preamble.replace("__ANS_PAGES__", ans_pages_str)

    parts = [preamble, r"\begin{document}"]

    # ==================== ĐỀ THI ====================
    parts.append(r"""\noindent
\begin{minipage}[c]{0.38\textwidth}
    \centering
    \textbf{LÀM TOÁN ĐỂ HẠNH PHÚC}\\[-2pt]
    \rule{3.2cm}{0.6pt}\\[2pt]
    \textbf{ĐỀ ÔN TẬP CHÍNH THỨC}
\end{minipage}\hfill
\begin{minipage}[c]{0.52\textwidth}
    \centering
    \textbf{ĐỀ ÔN TẬP TOÁN 10 — CHƯƠNG V \& CHƯƠNG VI}\\[1pt]
    \textbf{NĂM HỌC 2026 -- 2027}\\[1pt]
    \textbf{ĐỀ SỐ 2 — Môn: TOÁN -- Khối lớp 10}\\
    \textit{\small Thời gian làm bài: 90 phút (không kể thời gian phát đề)}
\end{minipage}

\vspace{0.05cm}
\noindent
\begin{minipage}[b]{0.78\textwidth}
    \textbf{Họ và tên:}\dotfill\textbf{SBD:}\makebox[3.5cm]{\dotfill}
\end{minipage}\hfill
\begin{minipage}[b]{0.20\textwidth}
    \hfill
    \setlength{\fboxrule}{0.8pt}%
    \fbox{\begin{minipage}{2.3cm}
        \centering
        \textbf{\small Mã đề}\\
        \textbf{1057}
    \end{minipage}}
\end{minipage}
\vspace{0.05cm}

\parttitle{PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn}
\textit{Thí sinh trả lời từ câu 1 đến câu 20. Mỗi câu hỏi thí sinh chỉ chọn một phương án.}
\begin{enumerate}
\item Cho số gần đúng $b = 12\,548{,}63$. Hãy viết số quy tròn của số $b$ đến hàng chục.
\four{$12\,550$.}{$12\,540$.}{$12\,500$.}{$12\,549$.}

\item Cho số đúng $\bar{a} = 2{,}5$ và số gần đúng $a = 2{,}52$. Sai số tuyệt đối $\Delta_a$ của số gần đúng $a$ là
\four{$-0{,}02$.}{$0{,}02$.}{$0{,}04$.}{$0{,}2$.}

\item Điểm kiểm tra môn Toán của $6$ học sinh lần lượt là: $7;\ 8;\ 8;\ 9;\ 9;\ 10$. Số trung bình cộng của mẫu số liệu trên bằng
\four{$8{,}0$.}{$8{,}25$.}{$8{,}5$.}{$8{,}75$.}

\item Số cuốn sách đọc được trong một tháng của $7$ bạn học sinh là: $2;\ 3;\ 4;\ 5;\ 6;\ 8;\ 10$. Trung vị của mẫu số liệu trên bằng
\four{$4$.}{$6$.}{$5{,}5$.}{$5$.}

\item Cho mẫu số liệu về số điểm tốt đạt được trong tuần của $8$ học sinh: $4;\ 6;\ 7;\ 8;\ 10;\ 12;\ 13;\ 15$. Tứ phân vị thứ nhất $Q_1$ của mẫu số liệu là
\four{$6{,}5$.}{$7{,}0$.}{$6{,}0$.}{$7{,}5$.}

\item Một giáo viên thống kê số lỗi chính tả trong bài tập làm văn của học sinh lớp 10:
$$\begin{array}{|c|c|c|c|c|c|}
\hline
\text{Số lỗi} & 0 & 1 & 2 & 3 & 4 \\ \hline
\text{Số học sinh} & 10 & 18 & 15 & 6 & 2 \\ \hline
\end{array}$$
Mốt của mẫu số liệu trên bằng
\four{$18$.}{$1$.}{$2$.}{$0$.}

\item Nhiệt độ cao nhất trong ngày (đơn vị: $^\circ\text{C}$) trong một tuần tại một địa phương được ghi lại: $28;\ 29;\ 31;\ 32;\ 34;\ 35;\ 36$. Khoảng biến thiên của mẫu số liệu trên bằng
\four{$7^\circ\text{C}$.}{$9^\circ\text{C}$.}{$8^\circ\text{C}$.}{$6^\circ\text{C}$.}

\item Một mẫu số liệu có tứ phân vị thứ nhất $Q_1 = 12$ và tứ phân vị thứ ba $Q_3 = 22$. Trong các giá trị sau, giá trị nào là một giá trị ngoại lệ của mẫu số liệu?
\four{$15$.}{$30$.}{$35$.}{$39$.}

\item Tập xác định $D$ của hàm số $y = \dfrac{\sqrt{3 - x}}{x - 1}$ là
\four{$(-\infty; 3] \setminus \{1\}$.}{$(-\infty; 3) \setminus \{1\}$.}{$[3; +\infty) \setminus \{1\}$.}{$(-\infty; 1) \cup (1; 3)$.}

\item Cho hàm số $f(x) = \begin{cases} x^2 + 1 & \text{khi } x \ge 2 \\ 3x - 2 & \text{khi } x < 2 \end{cases}$. Giá trị của biểu thức $P = f(3) - f(0)$ bằng
\four{$8$.}{$12$.}{$10$.}{$6$.}

\item Hàm số nào sau đây nghịch biến trên khoảng $(-\infty; 1)$?
\four{$y = 2x - 3$.}{$y = -x^2 + 2x + 1$.}{$y = x^2 - 2x + 3$.}{$y = -x^2 + 4$.}

\item Tọa độ đỉnh $I$ của parabol $(P): y = -x^2 + 4x - 3$ là
\four{$I(2; -3)$.}{$I(-2; -15)$.}{$I(1; 0)$.}{$I(2; 1)$.}
\pagebreak

\item Trục đối xứng của parabol $y = 3x^2 - 12x + 7$ là đường thẳng có phương trình
\four{$x = 2$.}{$x = -2$.}{$y = 2$.}{$x = 4$.}

\item Biết parabol $(P): y = ax^2 + bx - 1$ có đỉnh $I(1; -2)$. Giá trị của biểu thức $a - b$ bằng
\four{$-1$.}{$3$.}{$-3$.}{$1$.}

\item Giá trị nhỏ nhất của hàm số $y = x^2 - 4x + 7$ trên đoạn $[0; 3]$ bằng
\four{$7$.}{$4$.}{$3$.}{$2$.}

\item Tam thức bậc hai nào sau đây nhận giá trị âm với mọi $x \in \mathbb{R}$?
\four{$f(x) = x^2 - 2x + 3$.}{$f(x) = -x^2 + 4x - 4$.}{$f(x) = -x^2 + 3x - 2$.}{$f(x) = -x^2 + 2x - 5$.}

\item Tập nghiệm của bất phương trình $x^2 - 5x + 4 \le 0$ là
\four{$[1; 4]$.}{$(1; 4)$.}{$(-\infty; 1] \cup [4; +\infty)$.}{$(-\infty; 1) \cup (4; +\infty)$.}

\item Số nghiệm nguyên của bất phương trình $-x^2 + 7x - 10 \ge 0$ là
\four{$3$.}{$4$.}{$5$.}{$2$.}

\item Tập nghiệm của phương trình $\sqrt{x^2 - 2x - 3} = \sqrt{x + 1}$ là
\four{$\{4\}$.}{$\{-1\}$.}{$\{-1; 4\}$.}{$\varnothing$.}

\item Số nghiệm thực của phương trình $\sqrt{3x^2 - 9x + 1} = x - 2$ là
\four{$2$.}{$0$.}{$3$.}{$1$.}
\end{enumerate}

\vspace{3pt}
\parttitle{PHẦN II. Câu trắc nghiệm đúng sai}
\textit{Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.}
\begin{enumerate}
\item Điểm kiểm tra học kì môn Toán (thang điểm 10) của $10$ học sinh được ghi lại như sau:
$$5{,}5;\quad 6{,}0;\quad 6{,}5;\quad 7{,}0;\quad 7{,}5;\quad 7{,}5;\quad 8{,}0;\quad 8{,}5;\quad 9{,}0;\quad 9{,}5.$$
\begin{enumerate}
    \item Khoảng biến thiên của mẫu số liệu trên bằng $4{,}0$.
    \item Số trung bình cộng của mẫu số liệu là $\bar{x} = 7{,}5$.
    \item Trung vị của mẫu số liệu là $M_e = 7{,}25$.
    \item Khoảng tứ phân vị của mẫu số liệu là $\Delta_Q = 1{,}5$.
\end{enumerate}

\item Cho hàm số bậc hai $y = f(x) = -x^2 + 2x + 3$ có đồ thị là parabol $(P)$ như hình vẽ bên.
\par\noindent\begin{minipage}[t]{0.70\linewidth}
\begin{enumerate}
    \item Parabol $(P)$ có bề lõm quay xuống dưới và có đỉnh $I(1; 4)$.
    \item Trục đối xứng của parabol $(P)$ là đường thẳng $x = 1$.
    \item Hàm số đồng biến trên khoảng $(1; +\infty)$ và nghịch biến trên khoảng $(-\infty; 1)$.
    \item Bất phương trình $f(x) \ge 0$ có tập nghiệm là đoạn $[-1; 3]$.
\end{enumerate}
\end{minipage}\hfill
\begin{minipage}[t]{0.28\linewidth}\raggedleft\vspace{-4pt}
""" + TIKZ_P2_Q2 + r"""
\end{minipage}

\item Cho tam thức bậc hai $f(x) = x^2 - 2(m - 1)x + 2m + 1$ với $m$ là tham số thực.
\begin{enumerate}
    \item Khi $m = 3$, phương trình $f(x) = 0$ có hai nghiệm thực phân biệt.
    \item Biệt thức thu gọn $\Delta'$ của tam thức bậc hai $f(x)$ là $\Delta' = m^2 - 4m$.
    \item Khi $m = 0$, tam thức $f(x) > 0$ với mọi $x \in \mathbb{R}$.
    \item Tam thức $f(x) > 0$ với mọi $x \in \mathbb{R}$ khi và chỉ khi $0 < m < 4$.
\end{enumerate}

\item Cho phương trình chứa căn bậc hai: $\sqrt{3x^2 - 4x - 1} = \sqrt{2x^2 - 2x + 2}$.
\begin{enumerate}
    \item Bình phương hai vế của phương trình ta thu được phương trình bậc hai $x^2 - 2x - 3 = 0$.
    \item Phương trình bậc hai $x^2 - 2x - 3 = 0$ có hai nghiệm là $x = -1$ và $x = 3$.
    \item Cả hai giá trị $x = -1$ và $x = 3$ đều thỏa mãn phương trình ban đầu.
    \item Tổng tất cả các nghiệm của phương trình đã cho bằng $-2$.
\end{enumerate}
\end{enumerate}

\pagebreak
\parttitle{PHẦN III. Câu trắc nghiệm trả lời ngắn}
\textit{Thí sinh trả lời từ câu 1 đến câu 6. Mỗi câu thí sinh điền kết quả vào ô tương ứng.}
\begin{enumerate}
\item Cho mẫu số liệu: $5;\ 8;\ 9;\ 12;\ 14;\ 16;\ 18;\ 22$. Tính khoảng tứ phân vị $\Delta_Q$ của mẫu số liệu trên.\answerbox

\item Cho mẫu số liệu: $5;\ 15;\ 16;\ 18;\ 20;\ 21;\ 24;\ 25;\ 28;\ 45$, có $Q_1 = 16$ và $Q_3 = 25$. Tìm giá trị ngoại lệ duy nhất trong mẫu số liệu trên.\answerbox

\item Tìm giá trị lớn nhất của hàm số bậc hai $y = -x^2 + 4x + 5$ trên đoạn $[0; 4]$. \answerbox

\item Có bao nhiêu giá trị nguyên của tham số $m \in [-10; 10]$ để bất phương trình $x^2 - 2mx + m + 6 > 0$ nghiệm đúng với mọi $x \in \mathbb{R}$?\answerbox

\item Tính tổng tất cả các nghiệm thực của phương trình $\sqrt{3x^2 - 7x - 2} = x - 1$.\answerbox

\item \begin{minipage}[t]{0.70\linewidth}
Một quả bóng được sút lên từ mặt đất, quỹ đạo của quả bóng chuyển động theo đường parabol $h(t) = -t^2 + 4t$, trong đó $t$ là thời gian tính bằng giây ($0 \le t \le 4$), $h(t)$ là độ cao của quả bóng so với mặt đất tính bằng mét (như hình vẽ bên). Hỏi sau khi sút, quả bóng đạt độ cao lớn nhất bằng bao nhiêu mét?\answerbox
\end{minipage}\hfill
\begin{minipage}[t]{0.28\linewidth}\raggedleft\vspace{-6pt}
""" + TIKZ_P3_Q6 + r"""
\end{minipage}
\end{enumerate}

\vspace{3pt}
\parttitle{PHẦN IV. Tự luận}
\textit{Thí sinh trình bày bài làm và các bước suy luận cho các bài toán sau:}

\vspace{4pt}
\textbf{Bài 1 (1,0 điểm).} Để kiểm tra mức độ tiêu thụ nhiên liệu (đơn vị: lít/100 km) của hai dòng xe ô tô X và Y trong cùng điều kiện thử nghiệm, kỹ sư ghi lại số liệu sau $6$ lần chạy:
\begin{itemize}[leftmargin=1.5em, itemsep=1.5pt]
    \item Dòng xe X: $6{,}8;\ 7{,}0;\ 7{,}2;\ 7{,}2;\ 7{,}4;\ 7{,}6$.
    \item Dòng xe Y: $6{,}2;\ 6{,}6;\ 7{,}2;\ 7{,}2;\ 7{,}8;\ 8{,}2$.
\end{itemize}
\begin{enumerate}[label=\alph*), itemsep=2pt]
    \item (0,5 điểm) Tính số trung bình cộng và phương sai của mức tiêu thụ nhiên liệu ở mỗi dòng xe (làm tròn phương sai đến hàng phần trăm).
    \item (0,5 điểm) Dựa vào các số đặc trưng đo độ phân tán, hãy nhận xét xem dòng xe nào có mức tiêu thụ nhiên liệu ổn định hơn?
\end{enumerate}

\vspace{6pt}
\textbf{Bài 2 (1,0 điểm).} Giải phương trình chứa căn bậc hai sau:
$$\sqrt{2x^2 - 3x - 5} = x - 1.$$

\vspace{6pt}
\textbf{Bài 3 (1,0 điểm).} Một bác nông dân có $60\text{ m}$ lưới thép B40 dùng để rào một mảnh vườn hình chữ nhật tiếp giáp với một bờ sông thẳng (bờ sông đóng vai trò là một cạnh tự nhiên, không cần rào lưới).
\begin{enumerate}[label=\alph*), itemsep=2pt]
    \item (0,5 điểm) Gọi $x$ (mét) là chiều rộng của mảnh vườn rào vuông góc với bờ sông ($0 < x < 30$). Hãy lập hàm số $S(x)$ biểu diễn diện tích mảnh vườn theo $x$.
    \item (0,5 điểm) Bác nông dân cần rào mảnh vườn có chiều rộng $x$ bằng bao nhiêu mét để diện tích thu được là lớn nhất? Diện tích lớn nhất đó bằng bao nhiêu mét vuông?
\end{enumerate}
""")

    # ==================== ĐÁP ÁN & HƯỚNG DẪN GIẢI ====================
    parts.append(r"""\newpage
\pagestyle{dapan}
\setcounter{page}{1}

\begin{center}
  {\Large\bfseries\color{ink} BẢNG ĐÁP ÁN TỔNG HỢP}\\[2pt]
  {\small\color{gray!75!black} Đề ôn tập Toán 10 — Chương V \& Chương VI — Đề số 2 (Mã đề 1057)}
\end{center}
\vspace{1pt}

\noindent\textbf{PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (20 câu)}
\vspace{1.5pt}

\begin{center}
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|}
\hline
\textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{7} & \textbf{8} & \textbf{9} & \textbf{10} \\ \hline
\textbf{A} & \textbf{B} & \textbf{C} & \textbf{D} & \textbf{A} & \textbf{B} & \textbf{C} & \textbf{D} & \textbf{A} & \textbf{B} \\ \hline
\hline
\textbf{11} & \textbf{12} & \textbf{13} & \textbf{14} & \textbf{15} & \textbf{16} & \textbf{17} & \textbf{18} & \textbf{19} & \textbf{20} \\ \hline
\textbf{C} & \textbf{D} & \textbf{A} & \textbf{B} & \textbf{C} & \textbf{D} & \textbf{A} & \textbf{B} & \textbf{C} & \textbf{D} \\ \hline
\end{tabular}
\end{center}

\vspace{1pt}
\noindent\begin{minipage}[t]{0.58\linewidth}
\textbf{PHẦN II. Câu trắc nghiệm đúng/sai}\\[1.5pt]
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|c|c|c|c|c|}
\hline
\textbf{Câu} & \textbf{a)} & \textbf{b)} & \textbf{c)} & \textbf{d)} \\ \hline
\textbf{1} & \textbf{Đ} & \textbf{Đ} & \textbf{S} & \textbf{S} \\ \hline
\textbf{2} & \textbf{Đ} & \textbf{Đ} & \textbf{S} & \textbf{Đ} \\ \hline
\textbf{3} & \textbf{S} & \textbf{Đ} & \textbf{S} & \textbf{Đ} \\ \hline
\textbf{4} & \textbf{Đ} & \textbf{Đ} & \textbf{Đ} & \textbf{S} \\ \hline
\end{tabular}
\end{minipage}\hfill
\begin{minipage}[t]{0.40\linewidth}
\textbf{PHẦN III. Trả lời ngắn}\\[1.5pt]
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|c|c|c|c|}
\hline
\textbf{Câu} & \textbf{Đáp số} & \textbf{Câu} & \textbf{Đáp số} \\ \hline
\textbf{1} & $8{,}5$ & \textbf{4} & $4$ \\ \hline
\textbf{2} & $45$    & \textbf{5} & $3$ \\ \hline
\textbf{3} & $9$     & \textbf{6} & $4$ \\ \hline
\end{tabular}
\end{minipage}

\vspace{5pt}
\noindent\textbf{PHẦN IV. Đáp số tự luận:}\\[2pt]
- \textbf{Bài 1:} a) Xe X: $\bar{x}_X = 7{,}20$; $s_X^2 \approx 0{,}07$. Xe Y: $\bar{x}_Y = 7{,}20$; $s_Y^2 \approx 0{,}45$.\\
\phantom{- \textbf{Bài 1:}} b) Dòng xe X có mức tiêu thụ nhiên liệu ổn định hơn vì có phương sai nhỏ hơn ($0{,}07 < 0{,}45$).\\
- \textbf{Bài 2:} Tập nghiệm $S = \{3\}$ (loại nghiệm ngoại lai $x = -2$).\\
- \textbf{Bài 3:} a) $S(x) = -2x^2 + 60x\ (\text{m}^2)$. b) Chiều rộng $x = 15\text{ m}$; diện tích lớn nhất $S_{\max} = 450\text{ m}^2$.

\vspace{4pt}
\begin{center}
  {\large\bfseries\color{ink} HƯỚNG DẪN GIẢI CHI TIẾT}
\end{center}
\vspace{1pt}

\begin{multicols}{2}
\raggedcolumns
\small

\textbf{\color{accent}PHẦN I. TRẮC NGHIỆM}

\textbf{Câu 1.} Hàng chục là chữ số $4$, đứng sau là $8 \ge 5$ nên quy tròn thành $12\,550$. Chọn \textbf{A}.

\textbf{Câu 2.} Sai số tuyệt đối $\Delta_a = |2{,}5 - 2{,}52| = 0{,}02$. Chọn \textbf{B}.

\textbf{Câu 3.} $\bar{x} = \dfrac{7 + 8 + 8 + 9 + 9 + 10}{6} = \dfrac{51}{6} = 8{,}5$. Chọn \textbf{C}.

\textbf{Câu 4.} Mẫu có $7$ giá trị sắp thứ tự, trung vị là số ở chính giữa $x_4 = 5$. Chọn \textbf{D}.

\textbf{Câu 5.} Nửa dưới gồm $4$ giá trị đầu: $4;\ 6;\ 7;\ 8$. Tứ phân vị $Q_1 = \dfrac{6 + 7}{2} = 6{,}5$. Chọn \textbf{A}.

\textbf{Câu 6.} Tần số lớn nhất là $18$ ứng với số lỗi là $1$, nên $M_o = 1$. Chọn \textbf{B}.

\textbf{Câu 7.} Khoảng biến thiên $R = 36 - 28 = 8^\circ\text{C}$. Chọn \textbf{C}.

\textbf{Câu 8.} $\Delta_Q = 22 - 12 = 10$. Rào trên là $Q_3 + 1{,}5\Delta_Q = 22 + 15 = 37$. Do $39 > 37$ nên $39$ là giá trị ngoại lệ. Chọn \textbf{D}.

\textbf{Câu 9.} Điều kiện: $3 - x \ge 0 \Leftrightarrow x \le 3$ và $x - 1 \ne 0 \Leftrightarrow x \ne 1$. Vậy $D = (-\infty; 3] \setminus \{1\}$. Chọn \textbf{A}.

\textbf{Câu 10.} $f(3) = 3^2 + 1 = 10$; $f(0) = 3(0) - 2 = -2$. Do đó $P = 10 - (-2) = 12$. Chọn \textbf{B}.

\textbf{Câu 11.} Hàm số $y = x^2 - 2x + 3$ có $a = 1 > 0$ và đỉnh $x = 1$, do đó nghịch biến trên khoảng $(-\infty; 1)$. Chọn \textbf{C}.

\textbf{Câu 12.} Tọa độ đỉnh: $x_I = -\dfrac{4}{2(-1)} = 2$; $y_I = -(2)^2 + 4(2) - 3 = 1 \Rightarrow I(2; 1)$. Chọn \textbf{D}.

\textbf{Câu 13.} Trục đối xứng $x = -\dfrac{-12}{2(3)} = 2$. Chọn \textbf{A}.

\textbf{Câu 14.} Đỉnh $x = -\dfrac{b}{2a} = 1 \Rightarrow b = -2a$. Parabol qua $I(1; -2) \Rightarrow a + b - 1 = -2 \Rightarrow a + b = -1$. Do đó $a - 2a = -1 \Rightarrow a = 1 \Rightarrow b = -2$. Vậy $a - b = 1 - (-2) = 3$. Chọn \textbf{B}.

\textbf{Câu 15.} Parabol có đỉnh $x_I = 2 \in [0; 3]$. Ta có $y(0) = 7$, $y(2) = 3$, $y(3) = 4$. Vậy giá trị nhỏ nhất bằng $3$. Chọn \textbf{C}.

\textbf{Câu 16.} $f(x) = -x^2 + 2x - 5$ có $a = -1 < 0$ và $\Delta' = 1 - 5 = -4 < 0$ nên $f(x) < 0$ với mọi $x \in \mathbb{R}$. Chọn \textbf{D}.

\textbf{Câu 17.} $x^2 - 5x + 4 \le 0 \Leftrightarrow 1 \le x \le 4 \Rightarrow S = [1; 4]$. Chọn \textbf{A}.

\textbf{Câu 18.} $-x^2 + 7x - 10 \ge 0 \Leftrightarrow x^2 - 7x + 10 \le 0 \Leftrightarrow 2 \le x \le 5$. Các nghiệm nguyên là $2; 3; 4; 5$ ($4$ nghiệm). Chọn \textbf{B}.

\textbf{Câu 19.} $x^2 - 2x - 3 = x + 1 \Leftrightarrow x^2 - 3x - 4 = 0 \Leftrightarrow x = -1$ hoặc $x = 4$. Cả hai nghiệm đều thỏa $x + 1 \ge 0$. Vậy $S = \{-1; 4\}$. Chọn \textbf{C}.

\textbf{Câu 20.} Điều kiện $x \ge 2$. Bình phương: $3x^2 - 9x + 1 = x^2 - 4x + 4 \Leftrightarrow 2x^2 - 5x - 3 = 0 \Leftrightarrow x = 3$ (nhận) hoặc $x = -1/2$ (loại). Vậy có $1$ nghiệm. Chọn \textbf{D}.

\columnbreak

\textbf{\color{accent}PHẦN II. ĐÚNG / SAI}

\textbf{Câu 1.}
a) $R = 9{,}5 - 5{,}5 = 4{,}0 \Rightarrow$ \textbf{Đúng}.\\
b) Tổng điểm $= 75{,}0 \Rightarrow \bar{x} = 7{,}5 \Rightarrow$ \textbf{Đúng}.\\
c) Mẫu có $10$ số, hai số chính giữa là $x_5 = 7{,}5$ và $x_6 = 7{,}5 \Rightarrow M_e = 7{,}5 \ne 7{,}25 \Rightarrow$ \textbf{Sai}.\\
d) Nửa dưới: $5{,}5;\ 6{,}0;\ 6{,}5;\ 7{,}0;\ 7{,}5 \Rightarrow Q_1 = 6{,}5$. Nửa trên: $7{,}5;\ 8{,}0;\ 8{,}5;\ 9{,}0;\ 9{,}5 \Rightarrow Q_3 = 8{,}5$. Vậy $\Delta_Q = 8{,}5 - 6{,}5 = 2{,}0 \ne 1{,}5 \Rightarrow$ \textbf{Sai}.

\textbf{Câu 2.}
a) Hệ số $a = -1 < 0$ nên bề lõm quay xuống; đỉnh $I(1; 4) \Rightarrow$ \textbf{Đúng}.\\
b) Trục đối xứng $x = 1 \Rightarrow$ \textbf{Đúng}.\\
c) $a < 0$ nên đồng biến trên $(-\infty; 1)$ và nghịch biến trên $(1; +\infty) \Rightarrow$ \textbf{Sai}.\\
d) Parabol cắt $Ox$ tại $(-1; 0)$ và $(3; 0)$, phần đồ thị nằm trên trục hoành ứng với $x \in [-1; 3] \Rightarrow$ \textbf{Đúng}.

\textbf{Câu 3.}
a) Khi $m = 3$, $f(x) = x^2 - 4x + 7$ có $\Delta' = 4 - 7 = -3 < 0$, phương trình vô nghiệm $\Rightarrow$ \textbf{Sai}.\\
b) $\Delta' = (m - 1)^2 - (2m + 1) = m^2 - 2m + 1 - 2m - 1 = m^2 - 4m \Rightarrow$ \textbf{Đúng}.\\
c) Khi $m = 0$, $f(x) = x^2 + 2x + 1 = (x + 1)^2 \ge 0$, bằng $0$ tại $x = -1$ nên không dương với mọi $x \Rightarrow$ \textbf{Sai}.\\
d) Tam thức có $a = 1 > 0$, để $f(x) > 0\ \forall x \in \mathbb{R} \Leftrightarrow \Delta' < 0 \Leftrightarrow m^2 - 4m < 0 \Leftrightarrow 0 < m < 4 \Rightarrow$ \textbf{Đúng}.

\textbf{Câu 4.}
a) Bình phương: $3x^2 - 4x - 1 = 2x^2 - 2x + 2 \Leftrightarrow x^2 - 2x - 3 = 0 \Rightarrow$ \textbf{Đúng}.\\
b) Phương trình $x^2 - 2x - 3 = 0$ có $a - b + c = 0 \Rightarrow x = -1$ hoặc $x = 3 \Rightarrow$ \textbf{Đúng}.\\
c) Với $x = -1$: hai vế bằng $\sqrt{6} > 0$; với $x = 3$: hai vế bằng $\sqrt{14} > 0$. Cả hai đều là nghiệm $\Rightarrow$ \textbf{Đúng}.\\
d) Tổng các nghiệm là $(-1) + 3 = 2 \ne -2 \Rightarrow$ \textbf{Sai}.

\textbf{\color{accent}PHẦN III. TRẢ LỜI NGẮN}

\textbf{Câu 1.} Mẫu có $8$ số. Nửa dưới $5;\ 8;\ 9;\ 12 \Rightarrow Q_1 = 8{,}5$. Nửa trên $14;\ 16;\ 18;\ 22 \Rightarrow Q_3 = 17{,}0$. Khoảng tứ phân vị $\Delta_Q = 17{,}0 - 8{,}5 = \mathbf{8{,}5}$.

\textbf{Câu 2.} $\Delta_Q = 25 - 16 = 9$. Rào trên: $Q_3 + 1{,}5\Delta_Q = 25 + 13{,}5 = 38{,}5$. Do $45 > 38{,}5$ nên giá trị ngoại lệ duy nhất là $\mathbf{45}$.

\textbf{Câu 3.} Đỉnh $x_I = 2 \in [0; 4]$. $y(2) = 9$. Tại hai mút: $y(0) = 5$, $y(4) = 5$. Vậy giá trị lớn nhất là $\mathbf{9}$.

\textbf{Câu 4.} Bất phương trình nghiệm đúng với mọi $x \in \mathbb{R} \Leftrightarrow \Delta' < 0 \Leftrightarrow m^2 - m - 6 < 0 \Leftrightarrow -2 < m < 3$. Các giá trị nguyên là $m \in \{-1; 0; 1; 2\}$ ($4$ giá trị). Đáp số: $\mathbf{4}$.

\textbf{Câu 5.} Điều kiện $x \ge 1$. Bình phương: $3x^2 - 7x - 2 = x^2 - 2x + 1 \Leftrightarrow 2x^2 - 5x - 3 = 0 \Leftrightarrow x = 3$ (nhận) hoặc $x = -1/2$ (loại). Tổng nghiệm là $\mathbf{3}$.

\textbf{Câu 6.} Hàm $h(t) = -t^2 + 4t$ có đỉnh tại $t = 2 \in [0; 4]$. Độ cao lớn nhất: $h(2) = -(2)^2 + 4(2) = \mathbf{4}\text{ m}$.

\textbf{\color{accent}PHẦN IV. TỰ LUẬN}

\textbf{Bài 1.}
a) Dòng xe X:\\
$\bar{x}_X = \dfrac{6{,}8 + 7{,}0 + 7{,}2 + 7{,}2 + 7{,}4 + 7{,}6}{6} = \mathbf{7{,}20}\text{ lít/100km}$.\\
$s_X^2 = \dfrac{(-0{,}4)^2 + (-0{,}2)^2 + 0^2 + 0^2 + 0{,}2^2 + 0{,}4^2}{6} = \dfrac{0{,}40}{6} \approx \mathbf{0{,}07}$.\\
Dòng xe Y:\\
$\bar{x}_Y = \dfrac{6{,}2 + 6{,}6 + 7{,}2 + 7{,}2 + 7{,}8 + 8{,}2}{6} = \mathbf{7{,}20}\text{ lít/100km}$.\\
$s_Y^2 = \dfrac{(-1{,}0)^2 + (-0{,}6)^2 + 0^2 + 0^2 + 0{,}6^2 + 1{,}0^2}{6} = \dfrac{2{,}72}{6} \approx \mathbf{0{,}45}$.\\
b) Mặc dù mức tiêu thụ trung bình của cả hai dòng xe bằng nhau ($\bar{x} = 7{,}20$), nhưng phương sai của dòng xe X nhỏ hơn dòng xe Y ($0{,}07 < 0{,}45$), chứng tỏ mức tiêu thụ nhiên liệu của dòng xe X ổn định và đồng đều hơn.

\textbf{Bài 2.}
Điều kiện: $x - 1 \ge 0 \Leftrightarrow x \ge 1$.\\
Bình phương hai vế:\\
$2x^2 - 3x - 5 = (x - 1)^2$\\
$\Leftrightarrow 2x^2 - 3x - 5 = x^2 - 2x + 1$\\
$\Leftrightarrow x^2 - x - 6 = 0 \Leftrightarrow \begin{cases} x = 3 & \text{(thỏa mãn } x \ge 1) \\ x = -2 & \text{(loại vì } -2 < 1). \end{cases}$\\
Vậy tập nghiệm của phương trình là $S = \{3\}$.

\textbf{Bài 3.}
a) Do bờ sông đóng vai trò là một cạnh chiều dài, nên tổng độ dài của hai cạnh chiều rộng và một cạnh chiều dài còn lại là $60\text{ m}$.\\
Chiều dài của mảnh vườn là: $60 - 2x$ (m).\\
Hàm số biểu diễn diện tích mảnh vườn theo $x$ là:\\
$S(x) = x(60 - 2x) = \mathbf{-2x^2 + 60x}\ (\text{m}^2)$.\\
b) Hàm số $S(x) = -2x^2 + 60x$ là hàm số bậc hai có hệ số $a = -2 < 0$, đồ thị là parabol có bề lõm quay xuống dưới nên đạt giá trị lớn nhất tại đỉnh:\\
$x = -\dfrac{60}{2(-2)} = 15\text{ m}$ (thỏa mãn $0 < x < 30$).\\
Diện tích lớn nhất thu được là:\\
$S(15) = -2(15)^2 + 60(15) = \mathbf{450}\text{ m}^2$.\\
Vậy bác nông dân nên rào chiều rộng $15\text{ m}$ để đạt diện tích lớn nhất là $450\text{ m}^2$.

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
        bais = re.findall(r"Bài\s+(\d+)", txt)
        rect = page.rect
        max_y = 0
        for d in page.get_drawings():
            max_y = max(max_y, d["rect"].y1)
        print(f"  Page {pno:2d}: Qs={qs} | Bais={bais} | max_y={max_y:.1f}/{rect.height:.1f}pt")
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

    print("[3/4] Splitting into De_On_Tap_De_2.pdf and De_On_Tap_De_2_Ans.pdf...")
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

    print("\nBUILD COMPLETE FOR ĐỀ SỐ 2!")


if __name__ == "__main__":
    main()
