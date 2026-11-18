#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build pipeline for Grade 10 Review Exam #2: Chương IV. Vectơ (Toán 10 KNTT, Mã đề 1043).
Generates standalone student exam PDF (3 pages) and teacher answer key PDF (2 pages),
audits pagination, and exports copies to Grade 10 teaching folders.
"""

import re
import shutil
import subprocess
from pathlib import Path
import pymupdf

BASE_DIR = Path(r"d:\Tao_De\Lớp 10\Output\De_On_Tap_Vector_2")
OUT_DIR = BASE_DIR
TEX_PATH = OUT_DIR / "De_On_Tap_Vector_2.tex"
FULL_PDF = OUT_DIR / "De_On_Tap_Vector_2.pdf"
EXAM_PDF = OUT_DIR / "De_On_Tap_Vector_2_Exam.pdf"
ANS_PDF = OUT_DIR / "De_On_Tap_Vector_2_Ans.pdf"

EXPORT_TARGETS = [
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\Vector\De_On_Tap_Vector_2.pdf"), "exam"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\Vector\Ans\De_On_Tap_Vector_2_Ans.pdf"), "ans"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương IV\Đề ôn tập Chương 4 - Vectơ (Đề 2).pdf"), "exam"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương IV\Ans\Đề ôn tập Chương 4 - Vectơ (Đề 2 - Đáp án).pdf"), "ans"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương IV\Ans\Đề ôn tập Chương 4 - Vectơ (Đề 2 - có đáp án).pdf"), "full"),
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
  \lfoot{\small\textit{\color{gray!60!black}Đáp án Đề ôn tập Chương IV. Vectơ (Đề số 2) — Toán 10 KNTT}}
  \rfoot{\small Trang \thepage/__ANS_PAGES__}
  \renewcommand{\headrulewidth}{0.4pt}
  \renewcommand{\footrulewidth}{0pt}
}

\newcommand{\parttitle}[1]{\par\vspace{3.5pt}\needspace{3\baselineskip}{\large\bfseries\color{ink}#1}\par\nopagebreak\vspace{2pt}}
\newcommand{\four}[4]{\par\noindent\begin{tabularx}{\linewidth}{@{}*{4}{>{\raggedright\arraybackslash}X}@{}}\textbf{A.} #1&\textbf{B.} #2&\textbf{C.} #3&\textbf{D.} #4\end{tabularx}}
\newcommand{\two}[4]{\par\noindent\begin{tabularx}{\linewidth}{@{}*{2}{>{\raggedright\arraybackslash}X}@{}}\textbf{A.} #1&\textbf{B.} #2\\[3.8pt]\textbf{C.} #3&\textbf{D.} #4\end{tabularx}}
\newcommand{\one}[4]{\par\noindent\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X@{}}\textbf{A.} #1\\[4pt]\textbf{B.} #2\\[4pt]\textbf{C.} #3\\[4pt]\textbf{D.} #4\end{tabularx}}
\newcommand{\answerbox}{\unskip\nobreak\hfil\penalty50\hskip6pt\hbox{}\nobreak\hfill\mbox{\textit{Đáp số:}\ \fbox{\rule{0pt}{7.5pt}\hspace{1.8cm}}}}

\setlist[enumerate,1]{label=\textbf{Câu \arabic*.},leftmargin=1.1cm,labelsep=.1cm,itemsep=1.2pt,topsep=1.2pt,parsep=0pt}
\setlist[enumerate,2]{label=\alph*),leftmargin=.55cm,itemsep=1.5pt,topsep=0.2pt,parsep=0pt}
\newcolumntype{C}[1]{>{\centering\arraybackslash}m{#1}}
"""

TIKZ_P2_Q1 = r"""\begin{tikzpicture}[scale=0.60, >=Stealth]
  \coordinate (A) at (0,2.2);
  \coordinate (B) at (2.2,2.2);
  \coordinate (C) at (2.2,0);
  \coordinate (D) at (0,0);
  \coordinate (O) at (1.1,1.1);
  \draw[thick, ink] (A) -- (B) -- (C) -- (D) -- cycle;
  \draw[dashed, gray!70] (A) -- (C);
  \draw[dashed, gray!70] (B) -- (D);
  \draw[gray!70] (0,0.28) -- (0.28,0.28) -- (0.28,0);
  \fill[ink] (O) circle (1.6pt);
  \node[above left, font=\scriptsize] at (A) {$A$};
  \node[above right, font=\scriptsize] at (B) {$B$};
  \node[below right, font=\scriptsize] at (C) {$C$};
  \node[below left, font=\scriptsize] at (D) {$D$};
  \node[above=1pt, font=\tiny] at (O) {$O$};
\end{tikzpicture}"""

TIKZ_P3_Q6 = r"""\begin{tikzpicture}[scale=0.35, >=Stealth]
  \coordinate (O) at (0,0);
  \coordinate (F1) at (3.2,0);
  \coordinate (F2) at (2.5, 4.33);
  \coordinate (F) at (5.7, 4.33);
  \draw[->, very thick, accent] (O) -- (F1) node[below, font=\scriptsize] {$\vec{F}_1$};
  \draw[->, very thick, accent] (O) -- (F2) node[above left, font=\scriptsize] {$\vec{F}_2$};
  \draw[dashed, gray!60] (F1) -- (F) -- (F2);
  \draw[->, line width=1.1pt, ink] (O) -- (F) node[above right, font=\scriptsize] {$\vec{F}$};
  \draw[ink!80] (0.95,0) arc (0:60:0.95);
  \node[font=\tiny] at (18:1.85) {$60^\circ$};
  \fill[ink] (O) circle (2.2pt);
  \node[below left, font=\scriptsize] at (O) {$O$};
\end{tikzpicture}"""

TIKZ_P4_B3 = r"""\begin{tikzpicture}[scale=0.50, >=Stealth]
  \fill[gray!18] (-0.5,-0.16) rectangle (4.0,0);
  \fill[gray!18] (-0.5,2.8) rectangle (4.0,2.96);
  \draw[thick, ink] (-0.5,0) -- (4.0,0);
  \draw[thick, ink] (-0.5,2.8) -- (4.0,2.8);
  \coordinate (A) at (0.6, 0);
  \coordinate (B) at (0.6, 2.8);
  \coordinate (C) at (2.7, 2.8);
  \coordinate (V1) at (0.6, 1.6);
  \coordinate (V2) at (1.8, 0);
  \coordinate (V) at (1.8, 1.6);
  \draw[dashed, gray!70] (A) -- (B);
  \draw[dashed, ink!70] (A) -- (C);
  \draw[gray!60] (0.6,0.28) -- (0.88,0.28) -- (0.88,0);
  \draw[->, very thick, accent] (A) -- (V1) node[left, font=\scriptsize] {$\vec{v}_1$};
  \draw[->, very thick, accent] (A) -- (V2) node[below=2pt, font=\scriptsize] {$\vec{v}_2$};
  \draw[dashed, gray!60] (V1) -- (V) -- (V2);
  \draw[->, line width=1.1pt, ink] (A) -- (V) node[right, font=\scriptsize] {$\vec{v}$};
  \pic[draw, angle radius=0.45cm, "$\alpha$", angle eccentricity=1.45, font=\tiny] {angle = V--A--V1};
  \fill[ink] (A) circle (1.8pt) node[below left, font=\tiny] {$A$};
  \fill[ink] (B) circle (1.8pt) node[above, font=\tiny] {$B$};
  \fill[ink] (C) circle (1.8pt) node[above, font=\tiny] {$C$};
  \node[left, font=\tiny, gray!50!black] at (0.55, 2.15) {$d$};
  \node[above, font=\tiny, gray!50!black] at (1.65, 2.94) {$s$};
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
    \textbf{ĐỀ ÔN TẬP SỐ 2}
\end{minipage}\hfill
\begin{minipage}[c]{0.52\textwidth}
    \centering
    \textbf{ĐỀ ÔN TẬP TOÁN 10 — CHƯƠNG IV. VECTƠ}\\[1pt]
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
        \textbf{1043}
    \end{minipage}}
\end{minipage}
\vspace{0.05cm}

\parttitle{PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn}
\textit{Thí sinh trả lời từ câu 1 đến câu 20. Mỗi câu hỏi thí sinh chỉ chọn một phương án.}
\begin{enumerate}
\item Cho ngũ giác đều $ABCDE$ tâm $O$. Số vectơ khác vectơ-không có điểm đầu và điểm cuối là các đỉnh của ngũ giác đã cho bằng
\four{$10$.}{$20$.}{$25$.}{$15$.}

\item Cho hình chữ nhật $ABCD$ tâm $O$. Vectơ nào sau đây bằng với vectơ $\vec{BO}$?
\four{$\vec{DO}$.}{$\vec{OB}$.}{$\vec{OA}$.}{$\vec{OD}$.}

\item Cho bốn điểm bất kì $M, N, P, Q$. Đẳng thức vectơ nào sau đây đúng?
\two{$\vec{MN} - \vec{MP} = \vec{PN}$.}{$\vec{MN} + \vec{PQ} = \vec{MQ}$.}{$\vec{MN} - \vec{PN} = \vec{PM}$.}{$\vec{MN} + \vec{NP} + \vec{PQ} = \vec{QM}$.}

\item Cho tam giác $ABC$ vuông tại $A$ có $AB = 3$, $AC = 4$. Độ dài của vectơ $\vec{u} = \vec{AB} - \vec{AC}$ bằng
\four{$7$.}{$1$.}{$5$.}{$\sqrt{7}$.}

\item Cho hình vuông $ABCD$ cạnh $a$. Độ dài của vectơ $\vec{v} = \vec{AB} + \vec{AD}$ bằng
\four{$a$.}{$2a$.}{$\dfrac{a\sqrt{2}}{2}$.}{$a\sqrt{2}$.}

\item Cho đoạn thẳng $AB$ và điểm $I$ là trung điểm của $AB$. Với mọi điểm $M$ bất kì, đẳng thức nào sau đây đúng?
\two{$\vec{MA} + \vec{MB} = 2\vec{MI}$.}{$\vec{MA} + \vec{MB} = \vec{MI}$.}{$\vec{MA} - \vec{MB} = 2\vec{MI}$.}{$\vec{IA} + \vec{IB} = 2\vec{AB}$.}

\item Cho tam giác $ABC$. Gọi $K$ là điểm thuộc đoạn thẳng $BC$ sao cho $KC = 4KB$. Đẳng thức nào sau đây đúng?
\two{$\vec{AK} = \dfrac{1}{5}\vec{AB} + \dfrac{4}{5}\vec{AC}$.}{$\vec{AK} = \dfrac{4}{5}\vec{AB} + \dfrac{1}{5}\vec{AC}$.}{$\vec{AK} = \dfrac{3}{4}\vec{AB} + \dfrac{1}{4}\vec{AC}$.}{$\vec{AK} = \dfrac{4}{5}\vec{AB} - \dfrac{1}{5}\vec{AC}$.}

\item Cho hai vectơ $\vec{a}$ và $\vec{b}$ đều khác vectơ-không. Hai vectơ $\vec{a}$ và $\vec{b}$ ngược hướng với nhau khi và chỉ khi
\two{$\vec{a} \cdot \vec{b} = 0$.}{$|\vec{a}| = |\vec{b}|$.}{Tồn tại số thực $k < 0$ sao cho $\vec{a} = k\vec{b}$.}{Tồn tại số thực $k > 0$ sao cho $\vec{a} = k\vec{b}$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho vectơ $\vec{a} = -3\vec{i} + 4\vec{j}$. Tọa độ của vectơ $\vec{a}$ là
\four{$(-3; 4)$.}{$(4; -3)$.}{$(3; -4)$.}{$(-3; -4)$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{u} = (3; -1)$ và $\vec{v} = (-2; 5)$. Tọa độ của vectơ $\vec{w} = 2\vec{u} - \vec{v}$ là
\four{$(4; -7)$.}{$(8; 3)$.}{$(4; 3)$.}{$(8; -7)$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$ có $A(1; 4)$, $B(-3; 2)$ và $C(5; -3)$. Tọa độ trọng tâm $G$ của tam giác $ABC$ là
\four{$G(3; 3)$.}{$G(1; -1)$.}{$G(1; 1)$.}{$G(-1; 1)$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho điểm $A(2; -1)$ và điểm $M(4; 3)$ là trung điểm của đoạn thẳng $AB$. Tọa độ của điểm $B$ là
\four{$B(3; 1)$.}{$B(6; 7)$.}{$B(2; 4)$.}{$B(6; 5)$.}
\pagebreak

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{u} = (-4; 6)$ và $\vec{v} = (2; m)$. Hai vectơ $\vec{u}$ và $\vec{v}$ cùng phương khi và chỉ khi
\four{$m = 3$.}{$m = -\dfrac{4}{3}$.}{$m = 12$.}{$m = -3$.}

\item Cho hình vuông $ABCD$ tâm $O$. Góc giữa hai vectơ $\vec{AB}$ và $\vec{BD}$ bằng
\four{$135^\circ$.}{$45^\circ$.}{$90^\circ$.}{$60^\circ$.}

\item Cho tam giác đều $ABC$ cạnh $a$. Giá trị của tích vô hướng $\vec{AB} \cdot \vec{BC}$ bằng
\four{$\dfrac{a^2}{2}$.}{$\dfrac{a^2\sqrt{3}}{2}$.}{$-\dfrac{a^2}{2}$.}{$-\dfrac{a^2\sqrt{3}}{2}$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{a} = (4; -3)$ và $\vec{b} = (-2; 5)$. Giá trị của tích vô hướng $\vec{a} \cdot \vec{b}$ bằng
\four{$7$.}{$-23$.}{$-7$.}{$23$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A(1; -2)$ và $B(-5; 6)$. Độ dài đoạn thẳng $AB$ bằng
\four{$14$.}{$2\sqrt{7}$.}{$5$.}{$10$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{u} = (m; 3)$ và $\vec{v} = (6; -4)$. Hai vectơ $\vec{u}$ và $\vec{v}$ vuông góc với nhau khi và chỉ khi
\four{$m = 2$.}{$m = -2$.}{$m = -9$.}{$m = \dfrac{1}{2}$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{a} = (1; 3)$ và $\vec{b} = (-2; -1)$. Góc giữa hai vectơ $\vec{a}$ và $\vec{b}$ bằng
\four{$45^\circ$.}{$120^\circ$.}{$135^\circ$.}{$60^\circ$.}

\item Một lực $\vec{F}$ không đổi có độ lớn $40\text{ N}$ tác dụng lên một vật làm vật dịch chuyển một đoạn $5\text{ m}$ theo hướng hợp với hướng của lực $\vec{F}$ một góc $30^\circ$. Công $A$ sinh bởi lực $\vec{F}$ bằng
\four{$100\text{ J}$.}{$100\sqrt{3}\text{ J}$.}{$200\text{ J}$.}{$200\sqrt{3}\text{ J}$.}
\end{enumerate}

\vspace{3pt}
\parttitle{PHẦN II. Câu trắc nghiệm đúng sai}
\textit{Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.}
\begin{enumerate}
\item Cho hình vuông $ABCD$ cạnh $a$ và có tâm $O$ (như hình vẽ bên).
\par\noindent\begin{minipage}[t]{0.72\linewidth}
\begin{enumerate}
    \item $\vec{AB} = \vec{CD}$.
    \item $\vec{OA} + \vec{OB} + \vec{OC} + \vec{OD} = \vec{0}$.
    \item Độ dài của vectơ $\vec{v} = \vec{OA} - \vec{OB}$ bằng $a$.
    \item Độ dài của vectơ $\vec{w} = \vec{OB} + \vec{OC}$ bằng $a\sqrt{2}$.
\end{enumerate}
\end{minipage}\hfill
\begin{minipage}[t]{0.26\linewidth}\raggedleft\vspace{-6pt}
""" + TIKZ_P2_Q1 + r"""
\end{minipage}

\item Cho hình bình hành $ABCD$. Gọi $M$ là trung điểm của cạnh $BC$, $N$ là điểm trên cạnh $CD$ sao cho $NC = 3ND$, và $I$ là trung điểm của đoạn thẳng $MN$.
\begin{enumerate}
    \item $\vec{AM} = \vec{AB} + \dfrac{1}{2}\vec{AD}$.
    \item $\vec{AN} = \dfrac{1}{3}\vec{AB} + \vec{AD}$.
    \item $\vec{MN} = \dfrac{3}{4}\vec{AB} - \dfrac{1}{2}\vec{AD}$.
    \item $\vec{AI} = \dfrac{5}{8}\vec{AB} + \dfrac{3}{4}\vec{AD}$.
\end{enumerate}

\item Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A(-1; 1)$, $B(2; 7)$ và $C(5; -2)$.
\begin{enumerate}
    \item Ba điểm $A, B, C$ thẳng hàng.
    \item Hai vectơ $\vec{AB}$ và $\vec{AC}$ vuông góc với nhau.
    \item Trọng tâm $G$ của tam giác $ABC$ có tọa độ là $G(2; 3)$.
    \item Tích vô hướng $\vec{BA} \cdot \vec{BC} = 45$.
\end{enumerate}

\item Cho tam giác $ABC$ có $AB = 5$, $AC = 8$ và góc $\widehat{BAC} = 60^\circ$. Gọi $M$ là trung điểm của cạnh $BC$.
\begin{enumerate}
    \item Tích vô hướng $\vec{AB} \cdot \vec{AC} = 20$.
    \item Độ dài cạnh $BC$ bằng $7$.
    \item Độ dài đường trung tuyến $AM$ bằng $6$.
    \item Tích vô hướng $\vec{BA} \cdot \vec{BC} = 15$.
\end{enumerate}
\end{enumerate}

\pagebreak
\parttitle{PHẦN III. Câu trắc nghiệm trả lời ngắn}
\textit{Thí sinh trả lời từ câu 1 đến câu 6. Mỗi câu thí sinh điền kết quả vào ô tương ứng.}
\begin{enumerate}
\item Cho hình thoi $ABCD$ có cạnh bằng $9$ và góc $\widehat{BAD} = 120^\circ$. Tính độ dài của vectơ $\vec{u} = \vec{AB} + \vec{AD}$.\answerbox

\item Cho tam giác $ABC$. Gọi $M$ là trung điểm cạnh $AB$ và $N$ là điểm trên cạnh $BC$ sao cho $BN = 2NC$. Biết rằng $\vec{MN} = x\vec{AB} + y\vec{AC}$ với $x, y \in \mathbb{R}$. Tính giá trị của biểu thức $P = 6x + 9y$.\answerbox

\item Trong mặt phẳng tọa độ $Oxy$, cho các vectơ $\vec{a} = (2; -3)$, $\vec{b} = (-1; 4)$ và $\vec{c} = (m; 4)$. Tìm giá trị của tham số $m$ để vectơ $\vec{c}$ cùng phương với vectơ $\vec{w} = 2\vec{a} + \vec{b}$.\answerbox

\item Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$ có $A(-1; 2)$, $B(4; 2)$ và $C(2; 6)$. Tính giá trị của $\cos\widehat{BAC}$ (viết kết quả dưới dạng số thập phân).\answerbox

\item Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A(1; 3)$ và $B(5; 1)$. Biết điểm $M(m; 0)$ thuộc trục hoành $Ox$ (với $m > 3$) sao cho tam giác $MAB$ vuông tại $M$. Tìm giá trị của $m$.\answerbox

\item \begin{minipage}[t]{0.70\linewidth}
Hai lực $\vec{F}_1$ và $\vec{F}_2$ cùng tác dụng lên một chất điểm tại $O$, hợp với nhau một góc $60^\circ$ (như hình vẽ bên). Biết độ lớn của hai lực lần lượt là $F_1 = 30\text{ N}$ và $F_2 = 50\text{ N}$. Tính độ lớn của hợp lực $\vec{F} = \vec{F}_1 + \vec{F}_2$ (đơn vị: N).\answerbox
\end{minipage}\hfill
\begin{minipage}[t]{0.28\linewidth}\raggedleft\vspace{-6pt}
""" + TIKZ_P3_Q6 + r"""
\end{minipage}
\end{enumerate}

\vspace{3pt}
\parttitle{PHẦN IV. Tự luận}
\textit{Thí sinh trình bày bài làm và các bước suy luận cho các bài toán sau:}

\vspace{4pt}
\textbf{Bài 1 (1,0 điểm).} Cho hình bình hành $ABCD$. Gọi $E$ là trung điểm của cạnh $AB$, $F$ là điểm trên cạnh $AD$ sao cho $AF = \dfrac{1}{3}AD$, và $K$ là điểm trên đường chéo $AC$ sao cho $AK = \dfrac{1}{5}AC$.
\begin{enumerate}[label=\alph*), itemsep=2pt]
    \item (0,5 điểm) Hãy phân tích các vectơ $\vec{EF}$ và $\vec{EK}$ theo hai vectơ $\vec{AB}$ và $\vec{AD}$.
    \item (0,5 điểm) Từ kết quả câu a), hãy chứng minh ba điểm $E, K, F$ thẳng hàng.
\end{enumerate}

\vspace{6pt}
\textbf{Bài 2 (1,0 điểm).} Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A(-2; 6)$, $B(1; 2)$ và $C(9; 8)$.
\begin{enumerate}[label=\alph*), itemsep=2pt]
    \item (0,5 điểm) Chứng minh tam giác $ABC$ vuông tại $B$ và tính diện tích của tam giác $ABC$.
    \item (0,5 điểm) Tìm tọa độ điểm $D$ sao cho tứ giác $ABCD$ là một hình chữ nhật.
\end{enumerate}

\vspace{6pt}
\textbf{Bài 3 (1,0 điểm).} Một chiếc thuyền máy chuyển động thẳng qua một con sông rộng $d = 120\text{ m}$ có hai bờ song song (như hình vẽ bên). Vận tốc riêng của thuyền so với nước là $\vec{v}_1$ có hướng vuông góc với bờ sông và độ lớn $v_1 = 4\text{ m/s}$. Dòng nước chảy song song với bờ sông với vận tốc $\vec{v}_2$ có độ lớn $v_2 = 3\text{ m/s}$.
\par\noindent\begin{minipage}[t]{0.68\linewidth}
\begin{enumerate}[label=\alph*), itemsep=2pt]
    \item (0,5 điểm) Viết phương trình vectơ biểu diễn vận tốc thực tế $\vec{v}$ của thuyền qua $\vec{v}_1, \vec{v}_2$ và tính độ lớn vận tốc thực tế $v = |\vec{v}|$ của thuyền.
    \item (0,5 điểm) Tính góc lệch $\alpha$ giữa hướng đi thực tế của thuyền so với phương vuông góc với bờ sông (làm tròn đến hàng phần mười của độ) và tính quãng đường $s$ thuyền bị nước cuốn trôi theo chiều dòng chảy khi sang đến bờ bên kia.
\end{enumerate}
\end{minipage}\hfill
\begin{minipage}[t]{0.30\linewidth}\raggedleft\vspace{-10pt}
""" + TIKZ_P4_B3 + r"""
\end{minipage}
""")

    # ==================== ĐÁP ÁN & HƯỚNG DẪN GIẢI ====================
    parts.append(r"""\newpage
\pagestyle{dapan}
\setcounter{page}{1}

\begin{center}
  {\Large\bfseries\color{ink} BẢNG ĐÁP ÁN TỔNG HỢP}\\[2pt]
  {\small\color{gray!75!black} Đề ôn tập Toán 10 — Chương IV. Vectơ — Đề số 2 (Mã đề 1043)}
\end{center}
\vspace{1pt}

\noindent\textbf{PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (20 câu)}
\vspace{1.5pt}

\begin{center}
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|}
\hline
\textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{7} & \textbf{8} & \textbf{9} & \textbf{10} \\ \hline
\textbf{B} & \textbf{D} & \textbf{A} & \textbf{C} & \textbf{D} & \textbf{A} & \textbf{B} & \textbf{C} & \textbf{A} & \textbf{D} \\ \hline
\hline
\textbf{11} & \textbf{12} & \textbf{13} & \textbf{14} & \textbf{15} & \textbf{16} & \textbf{17} & \textbf{18} & \textbf{19} & \textbf{20} \\ \hline
\textbf{C} & \textbf{B} & \textbf{D} & \textbf{A} & \textbf{C} & \textbf{B} & \textbf{D} & \textbf{A} & \textbf{C} & \textbf{B} \\ \hline
\end{tabular}
\end{center}

\vspace{1pt}
\noindent\begin{minipage}[t]{0.58\linewidth}
\textbf{PHẦN II. Câu trắc nghiệm đúng/sai}\\[1.5pt]
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|c|c|c|c|c|}
\hline
\textbf{Câu} & \textbf{a)} & \textbf{b)} & \textbf{c)} & \textbf{d)} \\ \hline
\textbf{1} & \textbf{S} & \textbf{Đ} & \textbf{Đ} & \textbf{S} \\ \hline
\textbf{2} & \textbf{Đ} & \textbf{S} & \textbf{S} & \textbf{Đ} \\ \hline
\textbf{3} & \textbf{S} & \textbf{Đ} & \textbf{S} & \textbf{Đ} \\ \hline
\textbf{4} & \textbf{Đ} & \textbf{Đ} & \textbf{S} & \textbf{S} \\ \hline
\end{tabular}
\end{minipage}\hfill
\begin{minipage}[t]{0.40\linewidth}
\textbf{PHẦN III. Trả lời ngắn}\\[1.5pt]
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|c|c|c|c|}
\hline
\textbf{Câu} & \textbf{Đáp số} & \textbf{Câu} & \textbf{Đáp số} \\ \hline
\textbf{1} & $9$     & \textbf{4} & $0{,}6$ \\ \hline
\textbf{2} & $5$     & \textbf{5} & $4$ \\ \hline
\textbf{3} & $-6$    & \textbf{6} & $70$ \\ \hline
\end{tabular}
\end{minipage}

\vspace{5pt}
\noindent\textbf{PHẦN IV. Đáp số tự luận:}\\[2pt]
- \textbf{Bài 1:} a) $\vec{EF} = -\dfrac{1}{2}\vec{AB} + \dfrac{1}{3}\vec{AD}$; $\vec{EK} = -\dfrac{3}{10}\vec{AB} + \dfrac{1}{5}\vec{AD}$. b) $\vec{EK} = \dfrac{3}{5}\vec{EF} \Rightarrow E, K, F$ thẳng hàng.\\
- \textbf{Bài 2:} a) $\vec{BA}\cdot\vec{BC} = 0 \Rightarrow \triangle ABC$ vuông tại $B$, $S_{\triangle ABC} = 25$. b) $D(6; 12)$.\\
- \textbf{Bài 3:} a) $\vec{v} = \vec{v}_1 + \vec{v}_2$, $v = 5\text{ m/s}$. b) $\alpha \approx 36{,}9^\circ$, $s = 90\text{ m}$.

\vspace{4pt}
\begin{center}
  {\large\bfseries\color{ink} HƯỚNG DẪN GIẢI CHI TIẾT}
\end{center}
\vspace{1pt}

\begin{multicols}{2}
\raggedcolumns
\small

\textbf{\color{accent}PHẦN I. TRẮC NGHIỆM}

\textbf{Câu 1.} Ngũ giác có $5$ đỉnh. Số vectơ khác $\vec{0}$ tạo bởi hai đỉnh phân biệt là $A_5^2 = 5 \times 4 = 20$. Chọn \textbf{B}.

\textbf{Câu 2.} Trong hình chữ nhật $ABCD$, tâm $O$ là trung điểm $BD$ nên $\vec{BO}$ và $\vec{OD}$ cùng hướng và có cùng độ dài, suy ra $\vec{BO} = \vec{OD}$. Chọn \textbf{D}.

\textbf{Câu 3.} Theo quy tắc hiệu hai vectơ chung gốc: $\vec{MN} - \vec{MP} = \vec{PN}$. Chọn \textbf{A}.

\textbf{Câu 4.} Ta có $\vec{u} = \vec{AB} - \vec{AC} = \vec{CB}$. Vì $\triangle ABC$ vuông tại $A$ nên $BC = \sqrt{3^2 + 4^2} = 5$. Chọn \textbf{C}.

\textbf{Câu 5.} Theo quy tắc hình bình hành: $\vec{AB} + \vec{AD} = \vec{AC}$. Đường chéo hình vuông cạnh $a$ là $AC = a\sqrt{2}$. Chọn \textbf{D}.

\textbf{Câu 6.} Vì $I$ là trung điểm $AB$, theo tính chất trung điểm với điểm $M$ bất kì ta có $\vec{MA} + \vec{MB} = 2\vec{MI}$. Chọn \textbf{A}.

\textbf{Câu 7.} Vì $K$ thuộc đoạn $BC$ và $KC = 4KB$ nên $BK = \dfrac{1}{5}BC \Rightarrow \vec{BK} = \dfrac{1}{5}\vec{BC}$. Suy ra $\vec{AK} = \vec{AB} + \dfrac{1}{5}(\vec{AC} - \vec{AB}) = \dfrac{4}{5}\vec{AB} + \dfrac{1}{5}\vec{AC}$. Chọn \textbf{B}.

\textbf{Câu 8.} Hai vectơ khác $\vec{0}$ ngược hướng khi và chỉ khi tồn tại số thực $k < 0$ sao cho $\vec{a} = k\vec{b}$. Chọn \textbf{C}.

\textbf{Câu 9.} Vectơ $\vec{a} = -3\vec{i} + 4\vec{j}$ có tọa độ là $(-3; 4)$. Chọn \textbf{A}.

\textbf{Câu 10.} $\vec{w} = 2(3; -1) - (-2; 5) = (6 + 2; -2 - 5) = (8; -7)$. Chọn \textbf{D}.

\columnbreak

\textbf{Câu 11.} Trọng tâm $G$: $x_G = \dfrac{1 - 3 + 5}{3} = 1$, $y_G = \dfrac{4 + 2 - 3}{3} = 1 \Rightarrow G(1; 1)$. Chọn \textbf{C}.

\textbf{Câu 12.} Vì $M$ là trung điểm $AB$: $x_B = 2x_M - x_A = 8 - 2 = 6$, $y_B = 2y_M - y_A = 6 - (-1) = 7 \Rightarrow B(6; 7)$. Chọn \textbf{B}.

\textbf{Câu 13.} Hai vectơ $\vec{u}, \vec{v}$ cùng phương khi $(-4)m - 6 \cdot 2 = 0 \Leftrightarrow -4m = 12 \Leftrightarrow m = -3$. Chọn \textbf{D}.

\textbf{Câu 14.} Hình vuông $ABCD$ có $\widehat{ABD} = 45^\circ$. Góc giữa $\vec{AB}$ và $\vec{BD}$ là $180^\circ - 45^\circ = 135^\circ$. Chọn \textbf{A}.

\textbf{Câu 15.} Vì $\triangle ABC$ đều cạnh $a$ nên $(\vec{AB}, \vec{BC}) = 120^\circ \Rightarrow \vec{AB} \cdot \vec{BC} = a \cdot a \cdot \cos 120^\circ = -\dfrac{a^2}{2}$. Chọn \textbf{C}.

\textbf{Câu 16.} $\vec{a} \cdot \vec{b} = 4(-2) + (-3)(5) = -8 - 15 = -23$. Chọn \textbf{B}.

\textbf{Câu 17.} $\vec{AB} = (-6; 8) \Rightarrow AB = \sqrt{(-6)^2 + 8^2} = \sqrt{100} = 10$. Chọn \textbf{D}.

\textbf{Câu 18.} $\vec{u} \perp \vec{v} \Leftrightarrow 6m + 3(-4) = 0 \Leftrightarrow 6m = 12 \Leftrightarrow m = 2$. Chọn \textbf{A}.

\textbf{Câu 19.} $\cos(\vec{a}, \vec{b}) = \dfrac{1(-2) + 3(-1)}{\sqrt{1^2+3^2}\sqrt{(-2)^2+(-1)^2}} = \dfrac{-5}{\sqrt{50}} = -\dfrac{\sqrt{2}}{2} \Rightarrow (\vec{a}, \vec{b}) = 135^\circ$. Chọn \textbf{C}.

\textbf{Câu 20.} $A = F \cdot s \cdot \cos 30^\circ = 40 \cdot 5 \cdot \dfrac{\sqrt{3}}{2} = 100\sqrt{3}\text{ J}$. Chọn \textbf{B}.

\end{multicols}
\newpage
\begin{multicols}{2}
\raggedcolumns
\small

\textbf{\color{accent}PHẦN II. ĐÚNG / SAI}

\textbf{Câu 1.}
a) Hai vectơ $\vec{AB}$ và $\vec{CD}$ ngược hướng nên $\vec{AB} = -\vec{CD} \ne \vec{CD} \Rightarrow$ \textbf{Sai}.\\
b) Vì $O$ là trung điểm $AC$ và $BD$ nên $\vec{OA} + \vec{OC} = \vec{0}$ và $\vec{OB} + \vec{OD} = \vec{0}$, suy ra tổng bằng $\vec{0} \Rightarrow$ \textbf{Đúng}.\\
c) $\vec{v} = \vec{OA} - \vec{OB} = \vec{BA} \Rightarrow |\vec{v}| = BA = a \Rightarrow$ \textbf{Đúng}.\\
d) Hai đường chéo hình vuông vuông góc và bằng nhau nên $\vec{OB} \perp \vec{OC}$, $OB = OC = \dfrac{a\sqrt{2}}{2} \Rightarrow |\vec{OB} + \vec{OC}| = \sqrt{OB^2 + OC^2} = a \ne a\sqrt{2} \Rightarrow$ \textbf{Sai}.

\textbf{Câu 2.}
a) $\vec{AM} = \vec{AB} + \vec{BM} = \vec{AB} + \dfrac{1}{2}\vec{BC} = \vec{AB} + \dfrac{1}{2}\vec{AD} \Rightarrow$ \textbf{Đúng}.\\
b) Vì $NC = 3ND$ trên $CD$ nên $DN = \dfrac{1}{4}DC \Rightarrow \vec{AN} = \vec{AD} + \dfrac{1}{4}\vec{AB} \ne \dfrac{1}{3}\vec{AB} + \vec{AD} \Rightarrow$ \textbf{Sai}.\\
c) $\vec{MN} = \vec{AN} - \vec{AM} = -\dfrac{3}{4}\vec{AB} + \dfrac{1}{2}\vec{AD} \ne \dfrac{3}{4}\vec{AB} - \dfrac{1}{2}\vec{AD} \Rightarrow$ \textbf{Sai}.\\
d) $I$ là trung điểm $MN$ nên $\vec{AI} = \dfrac{1}{2}(\vec{AM} + \vec{AN}) = \dfrac{1}{2}\left(\dfrac{5}{4}\vec{AB} + \dfrac{3}{2}\vec{AD}\right) = \dfrac{5}{8}\vec{AB} + \dfrac{3}{4}\vec{AD} \Rightarrow$ \textbf{Đúng}.

\textbf{Câu 3.}
a) $\vec{AB} = (3; 6)$, $\vec{AC} = (6; -3)$. Vì $3(-3) - 6(6) = -45 \ne 0$ nên $A, B, C$ không thẳng hàng $\Rightarrow$ \textbf{Sai}.\\
b) $\vec{AB} \cdot \vec{AC} = 3(6) + 6(-3) = 0 \Rightarrow \vec{AB} \perp \vec{AC} \Rightarrow$ \textbf{Đúng}.\\
c) $x_G = \dfrac{-1+2+5}{3} = 2$, $y_G = \dfrac{1+7-2}{3} = 2 \Rightarrow G(2; 2) \ne G(2; 3) \Rightarrow$ \textbf{Sai}.\\
d) $\vec{BA} = (-3; -6)$, $\vec{BC} = (3; -9) \Rightarrow \vec{BA} \cdot \vec{BC} = -9 + 54 = 45 \Rightarrow$ \textbf{Đúng}.

\textbf{Câu 4.}
a) $\vec{AB} \cdot \vec{AC} = 5 \cdot 8 \cdot \cos 60^\circ = 20 \Rightarrow$ \textbf{Đúng}.\\
b) $BC^2 = AB^2 + AC^2 - 2\vec{AB}\cdot\vec{AC} = 25 + 64 - 40 = 49 \Rightarrow BC = 7 \Rightarrow$ \textbf{Đúng}.\\
c) $AM^2 = \dfrac{AB^2 + AC^2 + 2\vec{AB}\cdot\vec{AC}}{4} = \dfrac{25 + 64 + 40}{4} = \dfrac{129}{4} \Rightarrow AM = \dfrac{\sqrt{129}}{2} \ne 6 \Rightarrow$ \textbf{Sai}.\\
d) $\vec{BA} \cdot \vec{BC} = \vec{BA} \cdot (\vec{BA} + \vec{AC}) = BA^2 - \vec{AB}\cdot\vec{AC} = 25 - 20 = 5 \ne 15 \Rightarrow$ \textbf{Sai}.

\textbf{\color{accent}PHẦN III. TRẢ LỜI NGẮN}

\textbf{Câu 1.} $\vec{AB} + \vec{AD} = \vec{AC}$. Vì $\widehat{BAD} = 120^\circ$ nên $\widehat{ABC} = 60^\circ$; lại có $BA = BC = 9$ nên $\triangle ABC$ đều $\Rightarrow |\vec{u}| = AC = \mathbf{9}$.

\textbf{Câu 2.} $\vec{AM} = \dfrac{1}{2}\vec{AB}$, $\vec{AN} = \vec{AB} + \dfrac{2}{3}\vec{BC} = \dfrac{1}{3}\vec{AB} + \dfrac{2}{3}\vec{AC}$. Suy ra $\vec{MN} = \vec{AN} - \vec{AM} = -\dfrac{1}{6}\vec{AB} + \dfrac{2}{3}\vec{AC}$. Vậy $P = 6\left(-\dfrac{1}{6}\right) + 9\left(\dfrac{2}{3}\right) = -1 + 6 = \mathbf{5}$.

\textbf{Câu 3.} $\vec{w} = 2(2; -3) + (-1; 4) = (3; -2)$. Để $\vec{c} = (m; 4)$ cùng phương với $\vec{w}$ thì $3 \cdot 4 - (-2)m = 0 \Leftrightarrow 2m = -12 \Leftrightarrow m = \mathbf{-6}$.

\textbf{Câu 4.} $\vec{AB} = (5; 0)$, $\vec{AC} = (3; 4)$. Khi đó $\cos\widehat{BAC} = \dfrac{5 \cdot 3 + 0 \cdot 4}{5 \cdot \sqrt{3^2+4^2}} = \dfrac{15}{25} = \mathbf{0{,}6}$.

\textbf{Câu 5.} $\vec{MA} = (1-m; 3)$, $\vec{MB} = (5-m; 1)$. $\triangle MAB$ vuông tại $M \Leftrightarrow (1-m)(5-m) + 3 = 0 \Leftrightarrow m^2 - 6m + 8 = 0 \Leftrightarrow m = 2$ hoặc $m = 4$. Do $m > 3$ nên $m = \mathbf{4}$.

\textbf{Câu 6.} Ta có:\\
$|\vec{F}| = \sqrt{F_1^2 + F_2^2 + 2F_1 F_2 \cos 60^\circ} = \sqrt{30^2 + 50^2 + 30 \cdot 50} = \sqrt{4900} = \mathbf{70}\text{ N}$.

\textbf{\color{accent}PHẦN IV. TỰ LUẬN}

\textbf{Bài 1.}
a) Ta có $\vec{AE} = \dfrac{1}{2}\vec{AB}$, $\vec{AF} = \dfrac{1}{3}\vec{AD}$ nên:
$$\vec{EF} = \vec{AF} - \vec{AE} = -\dfrac{1}{2}\vec{AB} + \dfrac{1}{3}\vec{AD}.$$
Trong hình bình hành $ABCD$, $\vec{AC} = \vec{AB} + \vec{AD} \Rightarrow \vec{AK} = \dfrac{1}{5}\vec{AC} = \dfrac{1}{5}\vec{AB} + \dfrac{1}{5}\vec{AD}$.\\
Suy ra $\vec{EK} = \vec{AK} - \vec{AE} = \left(\dfrac{1}{5} - \dfrac{1}{2}\right)\vec{AB} + \dfrac{1}{5}\vec{AD} = -\dfrac{3}{10}\vec{AB} + \dfrac{1}{5}\vec{AD}$.\\
b) Nhận thấy $\vec{EK} = \dfrac{3}{5}\left(-\dfrac{1}{2}\vec{AB} + \dfrac{1}{3}\vec{AD}\right) = \dfrac{3}{5}\vec{EF}$.\\
Do đó hai vectơ $\vec{EK}$ và $\vec{EF}$ cùng phương, suy ra ba điểm $E, K, F$ thẳng hàng.

\textbf{Bài 2.}
a) Ta có $\vec{BA} = (-3; 4)$ và $\vec{BC} = (8; 6)$.\\
Suy ra $\vec{BA} \cdot \vec{BC} = (-3)(8) + 4(6) = -24 + 24 = 0 \Rightarrow BA \perp BC$.\\
Vậy $\triangle ABC$ vuông tại $B$.\\
Độ dài các cạnh: $BA = \sqrt{(-3)^2 + 4^2} = 5$, $BC = \sqrt{8^2 + 6^2} = 10$.\\
Diện tích tam giác $ABC$: $S_{\triangle ABC} = \dfrac{1}{2} BA \cdot BC = \dfrac{1}{2} \cdot 5 \cdot 10 = \mathbf{25}$.\\
b) Vì $\triangle ABC$ vuông tại $B$, tứ giác $ABCD$ là hình chữ nhật khi và chỉ khi $\vec{AD} = \vec{BC}$.\\
Gọi $D(x; y)$, ta có $\vec{AD} = (x + 2; y - 6) = (8; 6) \Leftrightarrow \begin{cases} x + 2 = 8 \\ y - 6 = 6 \end{cases} \Leftrightarrow \begin{cases} x = 6 \\ y = 12 \end{cases}$.\\
Vậy tọa độ điểm cần tìm là $D(6; 12)$.

\textbf{Bài 3.}
a) Phương trình vectơ vận tốc thực tế của thuyền: $\vec{v} = \vec{v}_1 + \vec{v}_2$.\\
Vì $\vec{v}_1 \perp \vec{v}_2$ nên độ lớn vận tốc thực tế của thuyền là:
$$v = |\vec{v}| = \sqrt{v_1^2 + v_2^2} = \sqrt{4^2 + 3^2} = 5\text{ m/s}.$$
b) Trong tam giác vuông tạo bởi $\vec{v}_1$ và $\vec{v}$, ta có $\tan\alpha = \dfrac{v_2}{v_1} = \dfrac{3}{4} \Rightarrow \alpha \approx 36{,}9^\circ$.\\
Thời gian thuyền qua sông là $t = \dfrac{d}{v_1} = \dfrac{120}{4} = 30\text{ s}$.\\
Quãng đường thuyền bị trôi dạt theo dòng chảy là $s = v_2 \cdot t = 3 \cdot 30 = 90\text{ m}$.

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

    print("[3/4] Splitting into De_On_Tap_Vector_2_Exam.pdf and De_On_Tap_Vector_2_Ans.pdf...")
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

    print("\nBUILD COMPLETE FOR ĐỀ ÔN TẬP VECTƠ — ĐỀ 2!")


if __name__ == "__main__":
    main()
