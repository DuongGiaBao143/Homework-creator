#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build pipeline for Grade 10 Review Exam #3: Chương IV. Vectơ (Toán 10 KNTT), Mã đề 1044.
Generates standalone student exam PDF (3 pages) and teacher answer key PDF (2 pages),
audits pagination, and exports copies to Grade 10 teaching folders.
"""

import re
import shutil
import subprocess
from pathlib import Path
import pymupdf

BASE_DIR = Path(r"d:\Tao_De\Lớp 10\Output\De_On_Tap_Vector_3")
OUT_DIR = BASE_DIR
TEX_PATH = OUT_DIR / "De_On_Tap_Vector_3.tex"
FULL_PDF = OUT_DIR / "De_On_Tap_Vector_3.pdf"
EXAM_PDF = OUT_DIR / "De_On_Tap_Vector_3_Exam.pdf"
ANS_PDF = OUT_DIR / "De_On_Tap_Vector_3_Ans.pdf"

EXPORT_TARGETS = [
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\Vector\De_On_Tap_Vector_3.pdf"), "exam"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\Vector\Ans\De_On_Tap_Vector_3_Ans.pdf"), "ans"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương IV\Đề ôn tập Chương 4 - Vectơ (Đề 3).pdf"), "exam"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương IV\Ans\Đề ôn tập Chương 4 - Vectơ (Đề 3 - Đáp án).pdf"), "ans"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương IV\Ans\Đề ôn tập Chương 4 - Vectơ (Đề 3 - có đáp án).pdf"), "full"),
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
\usetikzlibrary{calc,angles,quotes,arrows.meta,babel}

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
  \lfoot{\small\textit{\color{gray!60!black}Đáp án Đề ôn tập Chương IV. Vectơ (Đề 3) — Toán 10 KNTT}}
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

TIKZ_P2_Q1 = r"""\begin{tikzpicture}[scale=0.65, >=Stealth]
  \coordinate (B) at (0,0);
  \coordinate (C) at (3,0);
  \coordinate (A) at (1.5, 2.598);
  \coordinate (M) at (1.5, 0);
  \coordinate (G) at (1.5, 0.866);
  \draw[thick, ink] (A) -- (B) -- (C) -- cycle;
  \draw[dashed, gray!70] (A) -- (M);
  \draw[dashed, gray!70] (B) -- (G) -- (C);
  \fill[ink] (G) circle (1.8pt);
  \node[above, font=\scriptsize] at (A) {$A$};
  \node[below left, font=\scriptsize] at (B) {$B$};
  \node[below right, font=\scriptsize] at (C) {$C$};
  \node[below, font=\tiny] at (M) {$M$};
  \node[above right, font=\scriptsize] at (G) {$G$};
\end{tikzpicture}"""

TIKZ_P3_Q6 = r"""\begin{tikzpicture}[scale=0.55, >=Stealth]
  \draw[thick, gray!80!black] (-0.3,0) -- (4.2,0);
  \foreach \x in {0.0,0.4,...,4.0} {
    \draw[gray!60] (\x,0) -- (\x-0.18,-0.18);
  }
  \fill[accent!15] (0.5,0) rectangle (2.1,1.0);
  \draw[thick, ink] (0.5,0) rectangle (2.1,1.0);
  \node[font=\scriptsize, ink] at (1.3, 0.5) {$m$};
  \coordinate (P) at (2.1, 0.65);
  \coordinate (H) at (4.1, 0.65);
  \coordinate (Fend) at (3.85, 1.66);
  \draw[dashed, gray!70] (P) -- (H);
  \draw[->, very thick, accent] (P) -- (Fend) node[above right, font=\scriptsize] {$\vec{F}$};
  \draw[ink!80] ($(P)+(0.75,0)$) arc (0:30:0.75);
  \node[font=\tiny] at ($(P)+(1.32,0.22)$) {$30^\circ$};
  \draw[->, thick, ink] (0.8, 1.35) -- (2.3, 1.35) node[midway, above, font=\tiny] {$\vec{s}$};
\end{tikzpicture}"""

TIKZ_P4_B3 = r"""\begin{tikzpicture}[scale=0.58, >=Stealth]
  \coordinate (O) at (0,0);
  \coordinate (F1) at (1.75, 0);
  \coordinate (F2) at (-1.4, 2.425);
  \coordinate (F) at (0.35, 2.425);
  \draw[->, thin, gray!80!black] (-2.0, 0) -- (2.5, 0) node[right, font=\tiny] {$x$};
  \draw[->, thin, gray!80!black] (0, -0.5) -- (0, 2.9) node[above, font=\tiny] {$y$};
  \fill[ink!85] (-0.35,-0.22) -- (0.25,-0.22) -- (0.45,0) -- (0.25,0.22) -- (-0.35,0.22) -- cycle;
  \draw[->, very thick, accent] (O) -- (F1) node[below, font=\scriptsize] {$\vec{F}_1$};
  \draw[->, very thick, accent] (O) -- (F2) node[above left, font=\scriptsize] {$\vec{F}_2$};
  \draw[dashed, gray!60] (F1) -- (F) -- (F2);
  \draw[->, line width=1.1pt, ink] (O) -- (F) node[above right, font=\scriptsize] {$\vec{F}$};
  \draw[ink!80] (0.42,0) arc (0:120:0.42);
  \node[font=\tiny] at (0.95, 0.34) {$120^\circ$};
  \node[below left, font=\tiny] at (O) {$O$};
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
    \textbf{ĐỀ ÔN TẬP TOÁN 10 — CHƯƠNG IV. VECTƠ (ĐỀ SỐ 3)}\\[1pt]
    \textbf{NĂM HỌC 2026 -- 2027}\\[1pt]
    \textbf{Môn: TOÁN -- Khối lớp 10}\\
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
        \textbf{1044}
    \end{minipage}}
\end{minipage}
\vspace{0.05cm}

\parttitle{PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn}
\textit{Thí sinh trả lời từ câu 1 đến câu 20. Mỗi câu hỏi thí sinh chỉ chọn một phương án.}
\begin{enumerate}
\item Cho hình bình hành $ABCD$ tâm $O$. Có bao nhiêu vectơ khác vectơ-không cùng phương với vectơ $\vec{AB}$ và có điểm đầu, điểm cuối là các đỉnh của hình bình hành $ABCD$?
\four{$2$.}{$6$.}{$8$.}{$4$.}

\item Cho lục giác đều $ABCDEF$ tâm $O$. Vectơ nào sau đây bằng với vectơ $\vec{AB}$?
\four{$\vec{CF}$.}{$\vec{OC}$.}{$\vec{DE}$.}{$\vec{OF}$.}

\item Cho bốn điểm bất kì $M, N, P, Q$. Đẳng thức vectơ nào sau đây luôn đúng?
\two{$\vec{MN} + \vec{PQ} = \vec{MQ} + \vec{NP}$.}{$\vec{MN} - \vec{MP} = \vec{NP}$.}{$\vec{MN} + \vec{PQ} = \vec{MQ} + \vec{PN}$.}{$\vec{MN} + \vec{NQ} = \vec{QM}$.}

\item Cho tam giác $ABC$ vuông tại $A$ có $AB = 3$ và $AC = 4$. Độ dài của vectơ $\vec{u} = \vec{AB} - \vec{AC}$ bằng
\four{$5$.}{$7$.}{$1$.}{$\sqrt{7}$.}

\item Cho hình thoi $ABCD$ cạnh bằng $a$ và $\widehat{ABC} = 60^\circ$. Độ dài của vectơ $\vec{v} = \vec{BA} + \vec{BC}$ bằng
\four{$a$.}{$a\sqrt{3}$.}{$a\sqrt{2}$.}{$2a$.}

\item Cho tam giác $ABC$ có $G$ là trọng tâm và $O$ là một điểm bất kì trong mặt phẳng. Khẳng định nào sau đây đúng?
\two{$\vec{OA} + \vec{OB} + \vec{OC} = \vec{OG}$.}{$\vec{OA} + \vec{OB} + \vec{OC} = 2\vec{OG}$.}{$\vec{GB} + \vec{GC} = \vec{GA}$.}{$\vec{OA} + \vec{OB} + \vec{OC} = 3\vec{OG}$.}

\item Cho đoạn thẳng $AB$ và điểm $M$ nằm trên đoạn $AB$ sao cho $MA = 3MB$. Đẳng thức vectơ nào sau đây đúng?
\two{$\vec{AM} = \dfrac{3}{4}\vec{AB}$.}{$\vec{AM} = \dfrac{1}{4}\vec{AB}$.}{$\vec{AM} = -\dfrac{3}{4}\vec{AB}$.}{$\vec{AM} = \dfrac{4}{3}\vec{AB}$.}

\item Cho hình bình hành $ABCD$, gọi $M$ là trung điểm của cạnh $BC$. Phân tích vectơ $\vec{AM}$ theo hai vectơ $\vec{AB}$ và $\vec{AD}$ ta được
\two{$\vec{AM} = \dfrac{1}{2}\vec{AB} + \vec{AD}$.}{$\vec{AM} = \vec{AB} - \dfrac{1}{2}\vec{AD}$.}{$\vec{AM} = \vec{AB} + \dfrac{1}{2}\vec{AD}$.}{$\vec{AM} = \dfrac{1}{2}\vec{AB} + \dfrac{1}{2}\vec{AD}$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho điểm $A(2; -1)$ và vectơ $\vec{u} = -3\vec{i} + 4\vec{j}$. Tọa độ của vectơ $\vec{v} = \vec{OA} + \vec{u}$ là
\four{$(5; -5)$.}{$(1; -3)$.}{$(-1; -5)$.}{$(-1; 3)$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{a} = (1; -2)$ và $\vec{b} = (-3; 5)$. Tọa độ của vectơ $\vec{c} = 2\vec{a} - \vec{b}$ là
\four{$(5; -9)$.}{$(-1; 1)$.}{$(5; 1)$.}{$(-5; 9)$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$ có $A(1; 4)$, $B(-3; 2)$ và $C(5; -3)$. Tọa độ trọng tâm $G$ của tam giác $ABC$ là
\four{$G(3; 3)$.}{$G(1; 1)$.}{$G(1; 3)$.}{$G(-1; 1)$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A(-1; 2)$, $B(2; -4)$ và $C(m; 4)$. Giá trị của tham số $m$ để ba điểm $A, B, C$ thẳng hàng là
\four{$m = 2$.}{$m = 0$.}{$m = -2$.}{$m = -4$.}
\pagebreak

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{u} = (m; -4)$ và $\vec{v} = (-3; 6)$. Giá trị của $m$ để hai vectơ $\vec{u}$ và $\vec{v}$ cùng phương là
\four{$m = 2$.}{$m = -2$.}{$m = 8$.}{$m = -8$.}

\item Cho tam giác $ABC$ vuông cân tại $A$. Góc giữa hai vectơ $\vec{AB}$ và $\vec{BC}$ bằng
\four{$45^\circ$.}{$90^\circ$.}{$60^\circ$.}{$135^\circ$.}

\item Cho tam giác đều $ABC$ có cạnh bằng $a$. Tích vô hướng $\vec{AB} \cdot \vec{AC}$ bằng
\four{$a^2$.}{$\dfrac{a^2}{2}$.}{$-\dfrac{a^2}{2}$.}{$\dfrac{a^2\sqrt{3}}{2}$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{a} = (2; -1)$ và $\vec{b} = (3; 4)$. Giá trị của biểu thức $\vec{a} \cdot (\vec{a} + \vec{b})$ bằng
\four{$2$.}{$5$.}{$7$.}{$13$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A(1; -2)$ và $B(-5; 6)$. Độ dài đoạn thẳng $AB$ bằng
\four{$10$.}{$100$.}{$2\sqrt{13}$.}{$14$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{u} = (m + 1; 3)$ và $\vec{v} = (2; -4)$. Giá trị của $m$ để $\vec{u} \perp \vec{v}$ là
\four{$m = -5$.}{$m = 7$.}{$m = -7$.}{$m = 5$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{x} = (1; \sqrt{3})$ và $\vec{y} = (\sqrt{3}; 1)$. Góc giữa hai vectơ $\vec{x}$ và $\vec{y}$ bằng
\four{$60^\circ$.}{$30^\circ$.}{$45^\circ$.}{$120^\circ$.}

\item Một người kéo một chiếc xe đẩy đi quãng đường $20\text{ m}$ bằng một lực $\vec{F}$ không đổi có độ lớn $80\text{ N}$, hướng của lực hợp với hướng chuyển động một góc $30^\circ$. Công $A$ sinh bởi lực $\vec{F}$ bằng
\four{$1600\text{ J}$.}{$800\text{ J}$.}{$800\sqrt{3}\text{ J}$.}{$1600\sqrt{3}\text{ J}$.}
\end{enumerate}

\vspace{3pt}
\parttitle{PHẦN II. Câu trắc nghiệm đúng sai}
\textit{Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.}
\begin{enumerate}
\item Cho tam giác đều $ABC$ có cạnh bằng $a$, $M$ là trung điểm cạnh $BC$ và $G$ là trọng tâm của tam giác $ABC$ (như hình vẽ bên).
\par\noindent\begin{minipage}[t]{0.72\linewidth}
\begin{enumerate}
    \item Độ dài của vectơ $\vec{AG}$ bằng $\dfrac{a\sqrt{3}}{3}$.
    \item Đẳng thức vectơ $\vec{AB} + \vec{AC} = 3\vec{AG}$ là đúng.
    \item Tích vô hướng $\vec{GA} \cdot \vec{GB} = \dfrac{a^2}{6}$.
    \item Độ dài của vectơ $\vec{GB} - \vec{GC}$ bằng $a$.
\end{enumerate}
\end{minipage}\hfill
\begin{minipage}[t]{0.26\linewidth}\raggedleft\vspace{-6pt}
""" + TIKZ_P2_Q1 + r"""
\end{minipage}

\item Cho tam giác $ABC$. Gọi $M$ là trung điểm của cạnh $BC$ và $N$ là điểm nằm trên đoạn thẳng $AC$ sao cho $3NA = 2NC$ (tỉ số $NA : NC = 2 : 3$).
\begin{enumerate}
    \item Vectơ $\vec{AM}$ được biểu diễn là $\vec{AM} = \dfrac{1}{2}\vec{AB} - \dfrac{1}{2}\vec{AC}$.
    \item Vectơ $\vec{AN}$ được biểu diễn là $\vec{AN} = \dfrac{2}{3}\vec{AC}$.
    \item Vectơ $\vec{BN}$ được biểu diễn là $\vec{BN} = -\vec{AB} + \dfrac{2}{5}\vec{AC}$.
    \item Vectơ $\vec{MN}$ được biểu diễn là $\vec{MN} = -\dfrac{1}{2}\vec{AB} - \dfrac{1}{10}\vec{AC}$.
\end{enumerate}

\item Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A(1; 2)$, $B(4; 6)$ và $C(9; 6)$.
\begin{enumerate}
    \item Điểm $D$ đối xứng với $A$ qua $B$ có tọa độ là $D(7; 10)$.
    \item Tam giác $ABC$ là tam giác vuông cân tại $B$.
    \item Độ dài đoạn thẳng $AC$ bằng $4\sqrt{5}$.
    \item Tích vô hướng $\vec{AB} \cdot \vec{AC} = 20$.
\end{enumerate}

\item Cho hình chữ nhật $ABCD$ có $AB = 6$ và $AD = 8$.
\begin{enumerate}
    \item Tích vô hướng $\vec{AC} \cdot \vec{BD} = 0$.
    \item Tích vô hướng $\vec{AB} \cdot \vec{AC} = 36$.
    \item Độ dài của vectơ $\vec{AC} + \vec{BD}$ bằng $16$.
    \item Độ dài của vectơ $\vec{AB} + \vec{AC}$ bằng $14$.
\end{enumerate}
\end{enumerate}

\pagebreak
\parttitle{PHẦN III. Câu trắc nghiệm trả lời ngắn}
\textit{Thí sinh trả lời từ câu 1 đến câu 6. Mỗi câu thí sinh điền kết quả vào ô tương ứng.}
\begin{enumerate}
\item Cho tam giác $ABC$ có $AB = 5$, $AC = 8$ và $\widehat{BAC} = 60^\circ$. Tính độ dài vectơ $\vec{u} = \vec{AB} - \vec{AC}$.\answerbox

\item Cho tam giác $ABC$ có $M$ là trung điểm cạnh $BC$ và $I$ là trung điểm đoạn thẳng $AM$. Biết rằng $\vec{BI} = x\vec{AB} + y\vec{AC}$ với $x, y \in \mathbb{R}$. Tính giá trị của biểu thức $P = 8y - 4x$.\answerbox

\item Trong mặt phẳng tọa độ $Oxy$, cho hình bình hành $ABCD$ có $A(-1; 3)$, $B(2; 5)$ và $C(4; 1)$. Biết đỉnh thứ tư là $D(x_D; y_D)$, hãy tính giá trị của biểu thức $T = 4x_D - 5y_D$.\answerbox

\item Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A(1; 2)$, $B(4; 6)$ và $C(-2; 6)$. Tính giá trị của $\cos \widehat{BAC}$ (viết kết quả dưới dạng số thập phân).\answerbox

\item Trong mặt phẳng tọa độ $Oxy$, cho các vectơ $\vec{a} = (2; 2)$, $\vec{b} = (-1; 3)$ và $\vec{c} = (5; 1)$. Tìm giá trị của tham số thực $k$ để vectơ $\vec{u} = \vec{a} + k\vec{b}$ vuông góc với vectơ $\vec{c}$.\answerbox

\item \begin{minipage}[t]{0.70\linewidth}
Một người kéo một thùng hàng trên sàn nằm ngang bằng sợi dây hợp với phương ngang một góc $30^\circ$ (như hình vẽ bên). Biết lực kéo không đổi có độ lớn $F = 40\sqrt{3}\text{ N}$ và thùng hàng dịch chuyển thẳng một quãng đường $s = 15\text{ m}$. Tính công cơ học $A$ sinh bởi lực kéo $\vec{F}$ (đơn vị: J).\answerbox
\end{minipage}\hfill
\begin{minipage}[t]{0.28\linewidth}\raggedleft\vspace{-6pt}
""" + TIKZ_P3_Q6 + r"""
\end{minipage}
\end{enumerate}

\vspace{3pt}
\parttitle{PHẦN IV. Tự luận}
\textit{Thí sinh trình bày bài làm và các bước suy luận cho các bài toán sau:}

\vspace{4pt}
\textbf{Bài 1 (1,0 điểm).} Cho tam giác $ABC$. Gọi $I$ là trung điểm của cạnh $BC$, $K$ là trung điểm của đoạn thẳng $AI$, và $D$ là điểm nằm trên cạnh $AC$ sao cho $AD = \dfrac{1}{3}AC$.
\begin{enumerate}[label=\alph*), itemsep=2pt]
    \item (0,5 điểm) Hãy phân tích các vectơ $\vec{BK}$ và $\vec{BD}$ theo hai vectơ $\vec{AB}$ và $\vec{AC}$.
    \item (0,5 điểm) Từ kết quả câu a), hãy chứng minh rằng ba điểm $B, K, D$ thẳng hàng.
\end{enumerate}

\vspace{6pt}
\textbf{Bài 2 (1,0 điểm).} Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$ có ba đỉnh $A(-2; 6)$, $B(6; 2)$ và $C(-3; -1)$.
\begin{enumerate}[label=\alph*), itemsep=2pt]
    \item (0,5 điểm) Tìm tọa độ điểm $M$ thuộc trục hoành $Ox$ sao cho $|\vec{MA} + \vec{MB}|$ đạt giá trị nhỏ nhất, và tính giá trị nhỏ nhất đó.
    \item (0,5 điểm) Tìm tọa độ tâm $I$ của đường tròn ngoại tiếp tam giác $ABC$.
\end{enumerate}

\vspace{6pt}
\textbf{Bài 3 (1,0 điểm).} Hai tàu lai dắt cùng kéo một con tàu lớn tại điểm $O$ bằng hai lực kéo $\vec{F}_1$ và $\vec{F}_2$ có độ lớn lần lượt là $F_1 = 5000\text{ N}$ và $F_2 = 8000\text{ N}$, hợp với nhau một góc $120^\circ$ (như hình vẽ bên).
\par\noindent\begin{minipage}[t]{0.70\linewidth}
\begin{enumerate}[label=\alph*), itemsep=2pt]
    \item (0,5 điểm) Biểu diễn vectơ hợp lực $\vec{F}$ theo $\vec{F}_1, \vec{F}_2$ và tính độ lớn $|\vec{F}|$ của hợp lực tác dụng lên con tàu.
    \item (0,5 điểm) Chọn hệ trục tọa độ $Oxy$ sao cho tia $Ox$ trùng với hướng của $\vec{F}_1$ (như hình vẽ). Tìm tọa độ của các vectơ $\vec{F}_1, \vec{F}_2, \vec{F}$ và tính góc $\alpha$ hợp bởi hợp lực $\vec{F}$ và lực kéo $\vec{F}_1$ (làm tròn đến hàng phần mười độ).
\end{enumerate}
\end{minipage}\hfill
\begin{minipage}[t]{0.28\linewidth}\raggedleft\vspace{-15pt}
""" + TIKZ_P4_B3 + r"""
\end{minipage}
""")

    # ==================== ĐÁP ÁN & HƯỚNG DẪN GIẢI ====================
    parts.append(r"""\newpage
\pagestyle{dapan}
\setcounter{page}{1}

\begin{center}
  {\Large\bfseries\color{ink} BẢNG ĐÁP ÁN TỔNG HỢP}\\[2pt]
  {\small\color{gray!75!black} Đề ôn tập Toán 10 — Chương IV. Vectơ (Đề số 3 — Mã đề 1044)}
\end{center}
\vspace{1pt}

\noindent\textbf{PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (20 câu)}
\vspace{1.5pt}

\begin{center}
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|}
\hline
\textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{7} & \textbf{8} & \textbf{9} & \textbf{10} \\ \hline
\textbf{D} & \textbf{B} & \textbf{C} & \textbf{A} & \textbf{B} & \textbf{D} & \textbf{A} & \textbf{C} & \textbf{D} & \textbf{A} \\ \hline
\hline
\textbf{11} & \textbf{12} & \textbf{13} & \textbf{14} & \textbf{15} & \textbf{16} & \textbf{17} & \textbf{18} & \textbf{19} & \textbf{20} \\ \hline
\textbf{B} & \textbf{C} & \textbf{A} & \textbf{D} & \textbf{B} & \textbf{C} & \textbf{A} & \textbf{D} & \textbf{B} & \textbf{C} \\ \hline
\end{tabular}
\end{center}

\vspace{1pt}
\noindent\begin{minipage}[t]{0.58\linewidth}
\textbf{PHẦN II. Câu trắc nghiệm đúng/sai}\\[1.5pt]
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|c|c|c|c|c|}
\hline
\textbf{Câu} & \textbf{a)} & \textbf{b)} & \textbf{c)} & \textbf{d)} \\ \hline
\textbf{1} & \textbf{Đ} & \textbf{Đ} & \textbf{S} & \textbf{Đ} \\ \hline
\textbf{2} & \textbf{S} & \textbf{S} & \textbf{Đ} & \textbf{Đ} \\ \hline
\textbf{3} & \textbf{Đ} & \textbf{S} & \textbf{Đ} & \textbf{S} \\ \hline
\textbf{4} & \textbf{S} & \textbf{Đ} & \textbf{Đ} & \textbf{S} \\ \hline
\end{tabular}
\end{minipage}\hfill
\begin{minipage}[t]{0.40\linewidth}
\textbf{PHẦN III. Trả lời ngắn}\\[1.5pt]
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|c|c|c|c|}
\hline
\textbf{Câu} & \textbf{Đáp số} & \textbf{Câu} & \textbf{Đáp số} \\ \hline
\textbf{1} & $7$ & \textbf{4} & $0{,}28$ \\ \hline
\textbf{2} & $5$ & \textbf{5} & $6$ \\ \hline
\textbf{3} & $9$ & \textbf{6} & $900$ \\ \hline
\end{tabular}
\end{minipage}

\vspace{5pt}
\noindent\textbf{PHẦN IV. Đáp số tự luận:}\\[2pt]
- \textbf{Bài 1:} a) $\vec{BK} = -\dfrac{3}{4}\vec{AB} + \dfrac{1}{4}\vec{AC}$; $\vec{BD} = -\vec{AB} + \dfrac{1}{3}\vec{AC}$. b) $\vec{BK} = \dfrac{3}{4}\vec{BD} \Rightarrow B, K, D$ thẳng hàng.\\
- \textbf{Bài 2:} a) $M(2; 0)$, giá trị nhỏ nhất bằng $8$. b) Tâm đường tròn ngoại tiếp $I(1; 2)$.\\
- \textbf{Bài 3:} a) $\vec{F} = \vec{F}_1 + \vec{F}_2$, $|\vec{F}| = 7000\text{ N}$. b) $\vec{F}_1 = (5000; 0)$, $\vec{F}_2 = (-4000; 4000\sqrt{3})$, $\vec{F} = (1000; 4000\sqrt{3})$, $\alpha \approx 81{,}8^\circ$.

\vspace{4pt}
\begin{center}
  {\large\bfseries\color{ink} HƯỚNG DẪN GIẢI CHI TIẾT}
\end{center}
\vspace{1pt}

\begin{multicols}{2}
\raggedcolumns
\small

\textbf{\color{accent}PHẦN I. TRẮC NGHIỆM}

\textbf{Câu 1.} Các vectơ khác $\vec{0}$ cùng phương với $\vec{AB}$ tạo từ các đỉnh hình bình hành $ABCD$ là $\vec{AB}, \vec{BA}, \vec{CD}, \vec{DC}$. Có $4$ vectơ. Chọn \textbf{D}.

\textbf{Câu 2.} Trong lục giác đều $ABCDEF$ tâm $O$, cạnh $AB$ song song, cùng hướng và bằng $OC$ nên $\vec{AB} = \vec{OC}$. Chọn \textbf{B}.

\textbf{Câu 3.} $\vec{MN} + \vec{PQ} = (\vec{MQ} + \vec{QN}) + (\vec{PN} + \vec{NQ}) = \vec{MQ} + \vec{PN} + (\vec{QN} + \vec{NQ}) = \vec{MQ} + \vec{PN}$. Chọn \textbf{C}.

\textbf{Câu 4.} $\vec{u} = \vec{AB} - \vec{AC} = \vec{CB} \Rightarrow |\vec{u}| = BC = \sqrt{3^2 + 4^2} = 5$. Chọn \textbf{A}.

\textbf{Câu 5.} $\vec{v} = \vec{BA} + \vec{BC} = \vec{BD}$. Vì $ABCD$ là hình thoi cạnh $a$, $\widehat{ABC} = 60^\circ$ nên $\triangle ABC$ đều, $AC = a$, đường chéo $BD = 2 \cdot \dfrac{a\sqrt{3}}{2} = a\sqrt{3}$. Chọn \textbf{B}.

\textbf{Câu 6.} Với trọng tâm $G$ của $\triangle ABC$ và điểm $O$ bất kì: $\vec{OA} + \vec{OB} + \vec{OC} = 3\vec{OG} + (\vec{GA} + \vec{GB} + \vec{GC}) = 3\vec{OG}$. Chọn \textbf{D}.

\textbf{Câu 7.} $M$ thuộc đoạn $AB$ và $MA = 3MB \Rightarrow AM = \dfrac{3}{4}AB$ và $\vec{AM}$ cùng hướng $\vec{AB}$ nên $\vec{AM} = \dfrac{3}{4}\vec{AB}$. Chọn \textbf{A}.

\textbf{Câu 8.} $\vec{AM} = \vec{AB} + \vec{BM} = \vec{AB} + \dfrac{1}{2}\vec{BC} = \vec{AB} + \dfrac{1}{2}\vec{AD}$. Chọn \textbf{C}.

\textbf{Câu 9.} $\vec{OA} = (2; -1)$, $\vec{u} = (-3; 4) \Rightarrow \vec{v} = (2 - 3; -1 + 4) = (-1; 3)$. Chọn \textbf{D}.

\textbf{Câu 10.} $\vec{c} = 2(1; -2) - (-3; 5) = (2 + 3; -4 - 5) = (5; -9)$. Chọn \textbf{A}.

\textbf{Câu 11.} $x_G = \dfrac{1 - 3 + 5}{3} = 1$, $y_G = \dfrac{4 + 2 - 3}{3} = 1 \Rightarrow G(1; 1)$. Chọn \textbf{B}.

\textbf{Câu 12.} $\vec{AB} = (3; -6)$, $\vec{AC} = (m + 1; 2)$. Thẳng hàng $\Leftrightarrow 3 \cdot 2 - (-6)(m + 1) = 0 \Leftrightarrow 6m + 12 = 0 \Leftrightarrow m = -2$. Chọn \textbf{C}.

\textbf{Câu 13.} $\vec{u}, \vec{v}$ cùng phương $\Leftrightarrow 6m - (-4)(-3) = 0 \Leftrightarrow 6m = 12 \Leftrightarrow m = 2$. Chọn \textbf{A}.

\textbf{Câu 14.} $\triangle ABC$ vuông cân tại $A \Rightarrow \widehat{B} = 45^\circ$. Góc $(\vec{AB}, \vec{BC}) = 180^\circ - 45^\circ = 135^\circ$. Chọn \textbf{D}.

\textbf{Câu 15.} $\vec{AB} \cdot \vec{AC} = a \cdot a \cdot \cos 60^\circ = \dfrac{a^2}{2}$. Chọn \textbf{B}.

\textbf{Câu 16.} $\vec{a} + \vec{b} = (5; 3) \Rightarrow \vec{a} \cdot (\vec{a} + \vec{b}) = 2(5) + (-1)(3) = 7$. Chọn \textbf{C}.

\textbf{Câu 17.} $\vec{AB} = (-6; 8) \Rightarrow AB = \sqrt{(-6)^2 + 8^2} = 10$. Chọn \textbf{A}.

\textbf{Câu 18.} $\vec{u} \perp \vec{v} \Leftrightarrow 2(m + 1) + 3(-4) = 0 \Leftrightarrow 2m - 10 = 0 \Leftrightarrow m = 5$. Chọn \textbf{D}.

\textbf{Câu 19.} $\cos(\vec{x}, \vec{y}) = \dfrac{1\sqrt{3} + \sqrt{3}\cdot 1}{\sqrt{1+3}\sqrt{3+1}} = \dfrac{2\sqrt{3}}{4} = \dfrac{\sqrt{3}}{2} \Rightarrow (\vec{x}, \vec{y}) = 30^\circ$. Chọn \textbf{B}.

\textbf{Câu 20.} $A = F \cdot s \cdot \cos 30^\circ = 80 \cdot 20 \cdot \dfrac{\sqrt{3}}{2} = 800\sqrt{3}\text{ J}$. Chọn \textbf{C}.

\columnbreak

\textbf{\color{accent}PHẦN II. ĐÚNG / SAI}

\textbf{Câu 1.}
a) Trung tuyến $AM = \dfrac{a\sqrt{3}}{2} \Rightarrow |\vec{AG}| = \dfrac{2}{3}AM = \dfrac{a\sqrt{3}}{3} \Rightarrow$ \textbf{Đúng}.\\
b) $\vec{AB} + \vec{AC} = 2\vec{AM} = 2 \cdot \dfrac{3}{2}\vec{AG} = 3\vec{AG} \Rightarrow$ \textbf{Đúng}.\\
c) $(\vec{GA}, \vec{GB}) = 120^\circ$, $GA = GB = \dfrac{a\sqrt{3}}{3} \Rightarrow \vec{GA}\cdot\vec{GB} = \dfrac{a^2}{3}\cos 120^\circ = -\dfrac{a^2}{6} \ne \dfrac{a^2}{6} \Rightarrow$ \textbf{Sai}.\\
d) $|\vec{GB} - \vec{GC}| = |\vec{CB}| = a \Rightarrow$ \textbf{Đúng}.

\textbf{Câu 2.}
a) $M$ là trung điểm $BC \Rightarrow \vec{AM} = \dfrac{1}{2}\vec{AB} + \dfrac{1}{2}\vec{AC} \Rightarrow$ \textbf{Sai}.\\
b) $N$ trên đoạn $AC$ và $3NA = 2NC \Rightarrow AN = \dfrac{2}{5}AC \Rightarrow \vec{AN} = \dfrac{2}{5}\vec{AC} \ne \dfrac{2}{3}\vec{AC} \Rightarrow$ \textbf{Sai}.\\
c) $\vec{BN} = \vec{AN} - \vec{AB} = -\vec{AB} + \dfrac{2}{5}\vec{AC} \Rightarrow$ \textbf{Đúng}.\\
d) $\vec{MN} = \vec{AN} - \vec{AM} = \dfrac{2}{5}\vec{AC} - \left(\dfrac{1}{2}\vec{AB} + \dfrac{1}{2}\vec{AC}\right) = -\dfrac{1}{2}\vec{AB} - \dfrac{1}{10}\vec{AC} \Rightarrow$ \textbf{Đúng}.

\textbf{Câu 3.}
a) $B$ là trung điểm $AD \Rightarrow D = 2B - A = (7; 10) \Rightarrow$ \textbf{Đúng}.\\
b) $\vec{AB} = (3; 4)$, $\vec{BC} = (5; 0)$. Tuy $BA = BC = 5$ nhưng $\vec{AB} \cdot \vec{BC} = 15 \ne 0$ nên không vuông tại $B \Rightarrow$ \textbf{Sai}.\\
c) $\vec{AC} = (8; 4) \Rightarrow AC = \sqrt{64 + 16} = \sqrt{80} = 4\sqrt{5} \Rightarrow$ \textbf{Đúng}.\\
d) $\vec{AB} \cdot \vec{AC} = 3(8) + 4(4) = 40 \ne 20 \Rightarrow$ \textbf{Sai}.

\textbf{Câu 4.} Chọn hệ trục $A(0; 0), B(6; 0), C(6; 8), D(0; 8)$.\\
a) $\vec{AC} = (6; 8)$, $\vec{BD} = (-6; 8) \Rightarrow \vec{AC} \cdot \vec{BD} = -36 + 64 = 28 \ne 0 \Rightarrow$ \textbf{Sai}.\\
b) $\vec{AB} \cdot \vec{AC} = 6(6) + 0(8) = 36 \Rightarrow$ \textbf{Đúng}.\\
c) $\vec{AC} + \vec{BD} = (0; 16) = 2\vec{AD} \Rightarrow |\vec{AC} + \vec{BD}| = 16 \Rightarrow$ \textbf{Đúng}.\\
d) $\vec{AB} + \vec{AC} = (12; 8) \Rightarrow |\vec{AB} + \vec{AC}| = \sqrt{144 + 64} = 4\sqrt{13} \ne 14 \Rightarrow$ \textbf{Sai}.

\textbf{\color{accent}PHẦN III. TRẢ LỜI NGẮN}

\textbf{Câu 1.} $|\vec{u}| = |\vec{CB}| = BC = \sqrt{5^2 + 8^2 - 2\cdot 5\cdot 8\cos 60^\circ} = \sqrt{49} = \mathbf{7}$.

\textbf{Câu 2.} $\vec{AI} = \dfrac{1}{2}\vec{AM} = \dfrac{1}{4}(\vec{AB} + \vec{AC})$. Suy ra $\vec{BI} = \vec{AI} - \vec{AB} = -\dfrac{3}{4}\vec{AB} + \dfrac{1}{4}\vec{AC}$. Vậy $x = -\dfrac{3}{4}, y = \dfrac{1}{4} \Rightarrow P = 8\left(\dfrac{1}{4}\right) - 4\left(-\dfrac{3}{4}\right) = 2 + 3 = \mathbf{5}$.

\textbf{Câu 3.} $\vec{AD} = \vec{BC} = (2; -4) \Rightarrow D = (1; -1)$. Vậy $T = 4(1) - 5(-1) = \mathbf{9}$.

\textbf{Câu 4.} $\vec{AB} = (3; 4)$, $\vec{AC} = (-3; 4)$. $\cos\widehat{BAC} = \dfrac{-9 + 16}{5 \cdot 5} = \dfrac{7}{25} = \mathbf{0{,}28}$.

\textbf{Câu 5.} $\vec{u} = (2 - k; 2 + 3k)$. $\vec{u} \perp \vec{c} \Leftrightarrow 5(2 - k) + 1(2 + 3k) = 0 \Leftrightarrow 12 - 2k = 0 \Rightarrow k = \mathbf{6}$.

\textbf{Câu 6.} $A = F \cdot s \cdot \cos 30^\circ = 40\sqrt{3} \cdot 15 \cdot \dfrac{\sqrt{3}}{2} = \mathbf{900}\text{ J}$.

\textbf{\color{accent}PHẦN IV. TỰ LUẬN}

\textbf{Bài 1.}
a) Vì $I$ là trung điểm $BC \Rightarrow \vec{AI} = \dfrac{1}{2}(\vec{AB} + \vec{AC})$.\\
$K$ là trung điểm $AI \Rightarrow \vec{AK} = \dfrac{1}{2}\vec{AI} = \dfrac{1}{4}\vec{AB} + \dfrac{1}{4}\vec{AC}$.\\
Suy ra $\vec{BK} = \vec{AK} - \vec{AB} = -\dfrac{3}{4}\vec{AB} + \dfrac{1}{4}\vec{AC}$.\\
Vì $AD = \dfrac{1}{3}AC \Rightarrow \vec{AD} = \dfrac{1}{3}\vec{AC}$, suy ra $\vec{BD} = \vec{AD} - \vec{AB} = -\vec{AB} + \dfrac{1}{3}\vec{AC}$.\\
b) Ta có $\vec{BK} = \dfrac{3}{4}\left(-\vec{AB} + \dfrac{1}{3}\vec{AC}\right) = \dfrac{3}{4}\vec{BD}$.\\
Hai vectơ $\vec{BK}$ và $\vec{BD}$ cùng phương nên ba điểm $B, K, D$ thẳng hàng.

\textbf{Bài 2.}
a) Gọi $M(x; 0) \in Ox$. Ta có $\vec{MA} = (-2 - x; 6)$, $\vec{MB} = (6 - x; 2)$.\\
Suy ra $\vec{MA} + \vec{MB} = (4 - 2x; 8) \Rightarrow |\vec{MA} + \vec{MB}| = \sqrt{(4 - 2x)^2 + 64} \ge 8$.\\
Dấu bằng xảy ra khi $4 - 2x = 0 \Leftrightarrow x = 2$. Vậy $M(\mathbf{2}; \mathbf{0})$ và giá trị nhỏ nhất là $\mathbf{8}$.\\
b) Gọi tâm đường tròn ngoại tiếp là $I(a; b)$. Ta có $IA^2 = IB^2 = IC^2$:\\
$\begin{cases} (a + 2)^2 + (b - 6)^2 = (a - 6)^2 + (b - 2)^2 \\ (a - 6)^2 + (b - 2)^2 = (a + 3)^2 + (b + 1)^2 \end{cases} \Leftrightarrow \begin{cases} 16a - 8b = 0 \\ -18a - 6b = -30 \end{cases}$\\
$\Leftrightarrow \begin{cases} b = 2a \\ 3a + b = 5 \end{cases} \Leftrightarrow \begin{cases} a = 1 \\ b = 2 \end{cases}$. Vậy tâm ngoại tiếp là $I(\mathbf{1}; \mathbf{2})$.

\textbf{Bài 3.}
a) Hợp lực tác dụng lên con tàu là $\vec{F} = \vec{F}_1 + \vec{F}_2$.\\
Độ lớn hợp lực: $|\vec{F}| = \sqrt{F_1^2 + F_2^2 + 2F_1 F_2 \cos 120^\circ}$\\
$= \sqrt{5000^2 + 8000^2 + 2\cdot 5000\cdot 8000\cdot \left(-\dfrac{1}{2}\right)} = 1000\sqrt{49} = \mathbf{7000}\text{ N}$.\\
b) Với $Ox$ trùng hướng $\vec{F}_1$, ta có $\vec{F}_1 = (\mathbf{5000}; \mathbf{0})$.\\
Vì $(\vec{F}_1, \vec{F}_2) = 120^\circ$ nên $\vec{F}_2 = (8000\cos 120^\circ; 8000\sin 120^\circ) = (\mathbf{-4000}; \mathbf{4000\sqrt{3}})$.\\
Suy ra $\vec{F} = \vec{F}_1 + \vec{F}_2 = (\mathbf{1000}; \mathbf{4000\sqrt{3}})$.\\
Góc $\alpha$ giữa $\vec{F}$ và $\vec{F}_1$: $\cos\alpha = \dfrac{\vec{F} \cdot \vec{F}_1}{|\vec{F}||\vec{F}_1|} = \dfrac{1000 \cdot 5000}{7000 \cdot 5000} = \dfrac{1}{7} \Rightarrow \alpha \approx \mathbf{81{,}8}^\circ$.

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

    print("[3/4] Splitting into De_On_Tap_Vector_3_Exam.pdf and De_On_Tap_Vector_3_Ans.pdf...")
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

    print("\nBUILD COMPLETE FOR ĐỀ ÔN TẬP VECTƠ SỐ 3!")


if __name__ == "__main__":
    main()
