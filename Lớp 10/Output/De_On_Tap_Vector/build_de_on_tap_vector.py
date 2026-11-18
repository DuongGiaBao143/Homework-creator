#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build pipeline for Grade 10 Review Exam: Chương IV. Vectơ (Toán 10 KNTT).
Generates standalone student exam PDF (3 pages) and teacher answer key PDF (2 pages),
audits pagination, and exports copies to Grade 10 teaching folders.
"""

import os
import re
import shutil
import subprocess
from pathlib import Path
import pymupdf

BASE_DIR = Path(r"d:\Tao_De\Lớp 10\Output\De_On_Tap_Vector")
OUT_DIR = BASE_DIR
TEX_PATH = OUT_DIR / "De_On_Tap_Vector.tex"
FULL_PDF = OUT_DIR / "De_On_Tap_Vector.pdf"
EXAM_PDF = OUT_DIR / "De_On_Tap_Vector_Exam.pdf"
ANS_PDF = OUT_DIR / "De_On_Tap_Vector_Ans.pdf"

EXPORT_TARGETS = [
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\Vector\De_On_Tap_Vector.pdf"), "exam"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\Vector\Ans\De_On_Tap_Vector_Ans.pdf"), "ans"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương IV\Đề ôn tập Chương 4 - Vectơ.pdf"), "exam"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương IV\Ans\Đề ôn tập Chương 4 - Vectơ (Đáp án).pdf"), "ans"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương IV\Ans\Đề ôn tập Chương 4 - Vectơ có đáp án.pdf"), "full"),
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
  \lfoot{\small\textit{\color{gray!60!black}Đáp án Đề ôn tập Chương IV. Vectơ — Toán 10 KNTT}}
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

TIKZ_P2_Q1 = r"""\begin{tikzpicture}[scale=0.55, >=Stealth]
  \coordinate (A) at (0,0);
  \coordinate (B) at (2, 1.155);
  \coordinate (C) at (4,0);
  \coordinate (D) at (2, -1.155);
  \coordinate (O) at (2,0);
  \draw[thick, ink] (A) -- (B) -- (C) -- (D) -- cycle;
  \draw[dashed, gray!70] (A) -- (C);
  \draw[dashed, gray!70] (B) -- (D);
  \node[left, font=\scriptsize] at (A) {$A$};
  \node[above, font=\scriptsize] at (B) {$B$};
  \node[right, font=\scriptsize] at (C) {$C$};
  \node[below, font=\scriptsize] at (D) {$D$};
  \node[above right, font=\tiny] at (O) {$O$};
  \pic[draw, angle radius=0.35cm, "$60^\circ$", angle eccentricity=1.7, font=\tiny] {angle = D--A--B};
\end{tikzpicture}"""

TIKZ_P3_Q6 = r"""\begin{tikzpicture}[scale=0.32, >=Stealth]
  \coordinate (O) at (0,0);
  \coordinate (F1) at (6,0);
  \coordinate (F2) at (0,8);
  \coordinate (F) at (6,8);
  \draw[->, very thick, accent] (O) -- (F1) node[below, font=\scriptsize] {$\vec{F}_1$};
  \draw[->, very thick, accent] (O) -- (F2) node[left, font=\scriptsize] {$\vec{F}_2$};
  \draw[dashed, gray!60] (F1) -- (F) -- (F2);
  \draw[->, line width=1.1pt, ink] (O) -- (F) node[above right, font=\scriptsize] {$\vec{F}$};
  \draw[gray!70] (0.6,0) -- (0.6,0.6) -- (0,0.6);
  \node[below left, font=\scriptsize] at (O) {$O$};
\end{tikzpicture}"""

TIKZ_P4_B3 = r"""\begin{tikzpicture}[scale=0.46, >=Stealth]
  \fill[gray!20] (-1.8,2.0) rectangle (3.2,2.2);
  \draw[thick] (-1.8,2.0) -- (3.2,2.0);
  \coordinate (A) at (-0.6, 2.0);
  \coordinate (B) at (1.8, 2.0);
  \coordinate (O) at (0.6, 0.4);
  \draw[thick, ink] (A) -- (O) node[midway, left, font=\tiny] {$T_1$};
  \draw[thick, ink] (B) -- (O) node[midway, right, font=\tiny] {$T_2$};
  \draw[->, very thick, accent] (O) -- (0.6, -0.6) node[right, font=\tiny] {$\vec{P}$};
  \fill[ink] (O) circle (1.8pt) node[below left, font=\tiny] {$O$};
  \fill[accent!80!black] (0.38, -0.6) rectangle (0.82, -1.0);
  \node[font=\tiny, white] at (0.6, -0.8) {$m$};
  \draw[dashed, gray!70] (A) -- +(0,-0.5);
  \draw[dashed, gray!70] (B) -- +(0,-0.5);
  \node[below, font=\tiny] at (-0.2, 2.0) {$30^\circ$};
  \node[below, font=\tiny] at (1.4, 2.0) {$60^\circ$};
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
        \textbf{1042}
    \end{minipage}}
\end{minipage}
\vspace{0.05cm}

\parttitle{PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn}
\textit{Thí sinh trả lời từ câu 1 đến câu 20. Mỗi câu hỏi thí sinh chỉ chọn một phương án.}
\begin{enumerate}
\item Cho lục giác đều $ABCDEF$ tâm $O$. Có bao nhiêu vectơ khác vectơ-không có điểm đầu và điểm cuối là các đỉnh của lục giác đều?
\four{$36$.}{$15$.}{$30$.}{$12$.}

\item Cho hình bình hành $ABCD$ tâm $O$. Vectơ nào sau đây bằng với vectơ $\vec{AB}$?
\four{$\vec{DC}$.}{$\vec{CD}$.}{$\vec{BA}$.}{$\vec{OC}$.}

\item Cho bốn điểm bất kì $A, B, C, D$. Khẳng định nào sau đây luôn đúng?
\two{$\vec{AB} + \vec{CD} = \vec{AC} + \vec{DB}$.}{$\vec{AB} + \vec{BC} = \vec{CA}$.}{$\vec{AB} - \vec{AC} = \vec{BC}$.}{$\vec{AB} + \vec{BC} + \vec{CD} = \vec{AD}$.}

\item Cho tam giác đều $ABC$ cạnh bằng $a$. Độ dài của vectơ $\vec{u} = \vec{AB} + \vec{AC}$ bằng
\four{$a$.}{$a\sqrt{3}$.}{$2a$.}{$\dfrac{a\sqrt{3}}{2}$.}

\item Cho hình vuông $ABCD$ cạnh $a$. Độ dài của vectơ $\vec{v} = \vec{AB} - \vec{AD}$ bằng
\four{$a\sqrt{2}$.}{$2a$.}{$a$.}{$\dfrac{a\sqrt{2}}{2}$.}

\item Cho tam giác $ABC$ có trọng tâm $G$ và $M$ là trung điểm của cạnh $BC$. Đẳng thức vectơ nào sau đây đúng?
\four{$\vec{GA} + \vec{GB} + \vec{GC} = 3\vec{0}$.}{$\vec{AG} = \dfrac{1}{2}\vec{AM}$.}{$\vec{AG} = 2\vec{GM}$.}{$\vec{GB} + \vec{GC} = 2\vec{GA}$.}

\item Cho tam giác $ABC$. Gọi $M$ là điểm trên cạnh $BC$ sao cho $MB = 2MC$. Đẳng thức nào sau đây đúng?
\four{$\vec{AM} = \dfrac{2}{3}\vec{AB} + \dfrac{1}{3}\vec{AC}$.}{$\vec{AM} = \dfrac{1}{3}\vec{AB} + \dfrac{2}{3}\vec{AC}$.}{$\vec{AM} = \dfrac{1}{2}\vec{AB} + \dfrac{1}{2}\vec{AC}$.}{$\vec{AM} = \dfrac{1}{3}\vec{AB} - \dfrac{2}{3}\vec{AC}$.}

\item Cho ba điểm phân biệt $A, B, C$. Điều kiện cần và đủ để ba điểm $A, B, C$ thẳng hàng là
\two{$\vec{AB} = \vec{AC}$.}{$|\vec{AB}| = |\vec{AC}|$.}{$\vec{AB} + \vec{AC} = \vec{0}$.}{Tồn tại số thực $k \ne 0$ sao cho $\vec{AB} = k\vec{AC}$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho vectơ $\vec{u} = 2\vec{i} - 5\vec{j}$. Tọa độ của vectơ $\vec{u}$ là
\four{$(-5; 2)$.}{$(2; 5)$.}{$(2; -5)$.}{$(-2; 5)$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A(-1; 3)$ và $B(4; 1)$. Tọa độ của vectơ $\vec{AB}$ là
\four{$(3; 4)$.}{$(5; -2)$.}{$(-5; 2)$.}{$(3; -2)$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A(2; 4)$ và $B(-4; 2)$. Tọa độ trung điểm $M$ của đoạn thẳng $AB$ là
\four{$M(-1; 3)$.}{$M(3; 3)$.}{$M(-2; 6)$.}{$M(1; -3)$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A(1; 2)$, $B(3; 5)$, $C(5; 2)$. Tọa độ điểm $D$ để tứ giác $ABCD$ là hình bình hành là
\four{$D(7; 5)$.}{$D(-1; 5)$.}{$D(3; 1)$.}{$D(3; -1)$.}
\pagebreak

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{a} = (2; -3)$ và $\vec{b} = (m; 6)$. Hai vectơ $\vec{a}$ và $\vec{b}$ cùng phương khi và chỉ khi
\four{$m = 4$.}{$m = -4$.}{$m = -9$.}{$m = 9$.}

\item Cho tam giác đều $ABC$. Góc giữa hai vectơ $\vec{AB}$ và $\vec{BC}$ bằng
\four{$60^\circ$.}{$30^\circ$.}{$120^\circ$.}{$150^\circ$.}

\item Cho hình vuông $ABCD$ cạnh $a$. Tích vô hướng $\vec{AB} \cdot \vec{AC}$ bằng
\four{$a^2$.}{$a^2\sqrt{2}$.}{$\dfrac{a^2\sqrt{2}}{2}$.}{$2a^2$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{u} = (3; -2)$ và $\vec{v} = (4; 5)$. Giá trị của tích vô hướng $\vec{u} \cdot \vec{v}$ bằng
\four{$22$.}{$-2$.}{$14$.}{$2$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho điểm $A(-3; 4)$. Độ dài của vectơ $\vec{OA}$ bằng
\four{$7$.}{$5$.}{$1$.}{$\sqrt{7}$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{x} = (2; m)$ và $\vec{y} = (3; -6)$. Hai vectơ $\vec{x}$ và $\vec{y}$ vuông góc với nhau khi và chỉ khi
\four{$m = -1$.}{$m = 4$.}{$m = 1$.}{$m = 0$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{a} = (1; 2)$ và $\vec{b} = (-2; 1)$. Góc giữa hai vectơ $\vec{a}$ và $\vec{b}$ bằng
\four{$90^\circ$.}{$0^\circ$.}{$45^\circ$.}{$180^\circ$.}

\item Một lực $\vec{F}$ có độ lớn $50\text{ N}$ tác dụng lên một vật làm vật dịch chuyển quãng đường $10\text{ m}$ theo hướng hợp với hướng của lực $\vec{F}$ một góc $60^\circ$. Công $A$ sinh bởi lực $\vec{F}$ bằng
\four{$500\text{ J}$.}{$250\sqrt{3}\text{ J}$.}{$500\sqrt{3}\text{ J}$.}{$250\text{ J}$.}
\end{enumerate}

\vspace{3pt}
\parttitle{PHẦN II. Câu trắc nghiệm đúng sai}
\textit{Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.}
\begin{enumerate}
\item Cho hình thoi $ABCD$ có tâm $O$, cạnh bằng $a$ và góc $\widehat{BAD} = 60^\circ$ (như hình vẽ bên).
\par\noindent\begin{minipage}[t]{0.72\linewidth}
\begin{enumerate}
    \item Tam giác $ABD$ là tam giác đều cạnh $a$.
    \item Độ dài của vectơ $\vec{u} = \vec{AB} + \vec{AD}$ bằng $a\sqrt{2}$.
    \item Độ dài của vectơ $\vec{v} = \vec{AB} - \vec{AD}$ bằng $a$.
    \item Đẳng thức vectơ $\vec{AO} + \vec{CO} = \vec{AC}$ là đúng.
\end{enumerate}
\end{minipage}\hfill
\begin{minipage}[t]{0.26\linewidth}\raggedleft\vspace{-6pt}
""" + TIKZ_P2_Q1 + r"""
\end{minipage}

\item Cho tam giác $ABC$. Gọi $M$ là trung điểm cạnh $AB$, $N$ là điểm trên cạnh $AC$ sao cho $AN = 2NC$, và $G$ là trọng tâm của tam giác $ABC$.
\begin{enumerate}
    \item Vectơ $\vec{CM}$ được biểu diễn là $\vec{CM} = \dfrac{1}{2}\vec{CA} - \vec{CB}$.
    \item Vectơ $\vec{BN}$ được biểu diễn là $\vec{BN} = \dfrac{2}{3}\vec{AC} - \vec{AB}$.
    \item Vectơ $\vec{AG}$ được biểu diễn là $\vec{AG} = \dfrac{1}{3}\vec{AB} + \dfrac{1}{3}\vec{AC}$.
    \item Ba điểm $M, G, C$ không thẳng hàng.
\end{enumerate}

\item Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A(-2; 1)$, $B(2; 4)$ và $C(5; 0)$.
\begin{enumerate}
    \item Tọa độ của các vectơ $\vec{AB} = (4; 3)$ và $\vec{AC} = (7; -1)$.
    \item Ba điểm $A, B, C$ không thẳng hàng và tạo thành một tam giác.
    \item Trọng tâm $G$ của tam giác $ABC$ có tọa độ là $G\left(\dfrac{5}{3}; \dfrac{7}{3}\right)$.
    \item Tích vô hướng $\vec{AB} \cdot \vec{AC} = 25$.
\end{enumerate}

\item Cho tam giác $ABC$ vuông cân tại $A$ có $AB = AC = 4$. Gọi $M$ là trung điểm của cạnh $BC$.
\begin{enumerate}
    \item Tích vô hướng $\vec{BA} \cdot \vec{BC} = 8$.
    \item Độ dài của vectơ $\vec{AM}$ bằng $4$.
    \item Tích vô hướng $\vec{AM} \cdot \vec{BC} = 0$.
    \item Độ dài của vectơ $\vec{u} = \vec{AB} + 2\vec{AC}$ bằng $4\sqrt{5}$.
\end{enumerate}
\end{enumerate}

\pagebreak
\parttitle{PHẦN III. Câu trắc nghiệm trả lời ngắn}
\textit{Thí sinh trả lời từ câu 1 đến câu 6. Mỗi câu thí sinh điền kết quả vào ô tương ứng.}
\begin{enumerate}
\item Cho hình chữ nhật $ABCD$ có $AB = 6$, $AD = 8$. Tính độ dài của vectơ $\vec{u} = \vec{AB} + \vec{AD}$.\answerbox

\item Cho tam giác $ABC$. Gọi $I$ là điểm trên cạnh $BC$ sao cho $IB = 3IC$. Biết rằng $\vec{AI} = x\vec{AB} + y\vec{AC}$ với $x, y \in \mathbb{R}$. Hãy tính giá trị của biểu thức $P = 4x + 8y$.\answerbox

\item Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A(1; -2)$, $B(3; 2)$ và $C(m; 6)$. Tìm giá trị của tham số $m$ để ba điểm $A, B, C$ thẳng hàng.\answerbox

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{a} = (2; 1)$ và $\vec{b} = (3; -1)$. Tính góc giữa hai vectơ $\vec{a}$ và $\vec{b}$ (theo đơn vị độ).\answerbox

\item Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A(2; 4)$, $B(1; 1)$ và $C(k; 0)$. Tìm giá trị của $k$ để tam giác $ABC$ vuông tại $B$.\answerbox

\item \begin{minipage}[t]{0.70\linewidth}
Hai chiếc tàu kéo cùng tác dụng lực kéo lên một chiếc xà lan tại điểm $O$. Tàu thứ nhất tác dụng một lực kéo $\vec{F}_1$ có độ lớn $6000\text{ N}$, tàu thứ hai tác dụng một lực kéo $\vec{F}_2$ có độ lớn $8000\text{ N}$. Biết rằng hai lực $\vec{F}_1$ và $\vec{F}_2$ có phương vuông góc với nhau ($\vec{F}_1 \perp \vec{F}_2$ như hình vẽ bên). Tính độ lớn của hợp lực $\vec{F} = \vec{F}_1 + \vec{F}_2$ tác dụng lên chiếc xà lan (đơn vị: N).\answerbox
\end{minipage}\hfill
\begin{minipage}[t]{0.28\linewidth}\raggedleft\vspace{-6pt}
""" + TIKZ_P3_Q6 + r"""
\end{minipage}
\end{enumerate}

\vspace{3pt}
\parttitle{PHẦN IV. Tự luận}
\textit{Thí sinh trình bày bài làm và các bước suy luận cho các bài toán sau:}

\vspace{4pt}
\textbf{Bài 1 (1,0 điểm).} Cho tam giác $ABC$. Gọi $M$ là trung điểm của cạnh $AB$, $N$ là điểm trên cạnh $AC$ sao cho $AN = \dfrac{1}{3}AC$, và $P$ là điểm trên đường thẳng $BC$ sao cho $B$ là trung điểm của đoạn thẳng $PC$.
\begin{enumerate}[label=\alph*), itemsep=2pt]
    \item (0,5 điểm) Hãy phân tích vectơ $\vec{MN}$ theo hai vectơ $\vec{AB}$ và $\vec{AC}$.
    \item (0,5 điểm) Phân tích vectơ $\vec{MP}$ theo hai vectơ $\vec{AB}$ và $\vec{AC}$, từ đó chứng minh ba điểm $M, N, P$ thẳng hàng.
\end{enumerate}

\vspace{6pt}
\textbf{Bài 2 (1,0 điểm).} Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$ có ba đỉnh $A(-1; 2)$, $B(3; 4)$ và $C(2; -1)$.
\begin{enumerate}[label=\alph*), itemsep=2pt]
    \item (0,5 điểm) Tính chu vi của tam giác $ABC$ (làm tròn kết quả đến hàng phần mười).
    \item (0,5 điểm) Tìm tọa độ trực tâm $H$ của tam giác $ABC$.
\end{enumerate}

\vspace{6pt}
\textbf{Bài 3 (1,0 điểm).} Một vật có khối lượng $m = 10\text{ kg}$ (trọng lực $\vec{P}$ có độ lớn $P = 100\text{ N}$) được giữ cân bằng bởi hai sợi dây nhẹ không dãn $OA$ và $OB$ gắn vào trần nhà nằm ngang. Hai sợi dây tạo với trần nhà các góc lần lượt là $30^\circ$ và $60^\circ$ (như hình vẽ bên).
\par\noindent\begin{minipage}[t]{0.70\linewidth}
\begin{enumerate}[label=\alph*), itemsep=2pt]
    \item (0,5 điểm) Hãy biểu diễn điều kiện cân bằng của điểm treo $O$ dưới dạng đẳng thức vectơ giữa trọng lực $\vec{P}$ và các lực căng dây $\vec{T}_1, \vec{T}_2$.
    \item (0,5 điểm) Tính độ lớn lực căng $T_1$ của sợi dây $OA$ và lực căng $T_2$ của sợi dây $OB$ (làm tròn kết quả đến hàng phần mười nếu cần).
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
  {\small\color{gray!75!black} Đề ôn tập Toán 10 — Chương IV. Vectơ (Mã đề 1042)}
\end{center}
\vspace{1pt}

\noindent\textbf{PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (20 câu)}
\vspace{1.5pt}

\begin{center}
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|}
\hline
\textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{7} & \textbf{8} & \textbf{9} & \textbf{10} \\ \hline
\textbf{C} & \textbf{A} & \textbf{D} & \textbf{B} & \textbf{A} & \textbf{C} & \textbf{B} & \textbf{D} & \textbf{C} & \textbf{B} \\ \hline
\hline
\textbf{11} & \textbf{12} & \textbf{13} & \textbf{14} & \textbf{15} & \textbf{16} & \textbf{17} & \textbf{18} & \textbf{19} & \textbf{20} \\ \hline
\textbf{A} & \textbf{D} & \textbf{B} & \textbf{C} & \textbf{A} & \textbf{D} & \textbf{B} & \textbf{C} & \textbf{A} & \textbf{D} \\ \hline
\end{tabular}
\end{center}

\vspace{1pt}
\noindent\begin{minipage}[t]{0.58\linewidth}
\textbf{PHẦN II. Câu trắc nghiệm đúng/sai}\\[1.5pt]
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|c|c|c|c|c|}
\hline
\textbf{Câu} & \textbf{a)} & \textbf{b)} & \textbf{c)} & \textbf{d)} \\ \hline
\textbf{1} & \textbf{Đ} & \textbf{S} & \textbf{Đ} & \textbf{S} \\ \hline
\textbf{2} & \textbf{S} & \textbf{Đ} & \textbf{Đ} & \textbf{S} \\ \hline
\textbf{3} & \textbf{Đ} & \textbf{Đ} & \textbf{S} & \textbf{Đ} \\ \hline
\textbf{4} & \textbf{S} & \textbf{S} & \textbf{Đ} & \textbf{Đ} \\ \hline
\end{tabular}
\end{minipage}\hfill
\begin{minipage}[t]{0.40\linewidth}
\textbf{PHẦN III. Trả lời ngắn}\\[1.5pt]
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|c|c|c|c|}
\hline
\textbf{Câu} & \textbf{Đáp số} & \textbf{Câu} & \textbf{Đáp số} \\ \hline
\textbf{1} & $10$ & \textbf{4} & $45$ \\ \hline
\textbf{2} & $7$  & \textbf{5} & $4$ \\ \hline
\textbf{3} & $5$  & \textbf{6} & $10000$ \\ \hline
\end{tabular}
\end{minipage}

\vspace{5pt}
\noindent\textbf{PHẦN IV. Đáp số tự luận:}\\[2pt]
- \textbf{Bài 1:} a) $\vec{MN} = -\dfrac{1}{2}\vec{AB} + \dfrac{1}{3}\vec{AC}$. b) $\vec{MP} = \dfrac{3}{2}\vec{AB} - \vec{AC} = -3\vec{MN} \Rightarrow M, N, P$ thẳng hàng.\\
- \textbf{Bài 2:} a) Chu vi tam giác $ABC$: $2\sqrt{5} + \sqrt{26} + 3\sqrt{2} \approx 13{,}8$. b) Trực tâm $H\left(\dfrac{2}{3}; \dfrac{5}{3}\right)$.\\
- \textbf{Bài 3:} a) $\vec{T}_1 + \vec{T}_2 + \vec{P} = \vec{0}$. b) Lực căng dây: $T_1 = 50\text{ N}$; $T_2 = 50\sqrt{3}\text{ N} \approx 86{,}6\text{ N}$.

\vspace{4pt}
\begin{center}
  {\large\bfseries\color{ink} HƯỚNG DẪN GIẢI CHI TIẾT}
\end{center}
\vspace{1pt}

\begin{multicols}{2}
\raggedcolumns
\small

\textbf{\color{accent}PHẦN I. TRẮC NGHIỆM}

\textbf{Câu 1.} Lục giác có $6$ đỉnh. Số vectơ khác $\vec{0}$ có điểm đầu và cuối là các đỉnh là $A_6^2 = 6 \times 5 = 30$. Chọn \textbf{C}.

\textbf{Câu 2.} Trong hình bình hành $ABCD$, hai cạnh đối $AB$ và $DC$ song song và cùng độ dài, chiều từ $A \to B$ cùng chiều $D \to C$ nên $\vec{AB} = \vec{DC}$. Chọn \textbf{A}.

\textbf{Câu 3.} Theo quy tắc ba điểm mở rộng: $\vec{AB} + \vec{BC} + \vec{CD} = \vec{AC} + \vec{CD} = \vec{AD}$. Chọn \textbf{D}.

\textbf{Câu 4.} Gọi $M$ là trung điểm $BC$, ta có $\vec{AB} + \vec{AC} = 2\vec{AM}$. Vì $\triangle ABC$ đều cạnh $a$ nên trung tuyến $AM = \dfrac{a\sqrt{3}}{2} \Rightarrow |\vec{u}| = 2 \cdot \dfrac{a\sqrt{3}}{2} = a\sqrt{3}$. Chọn \textbf{B}.

\textbf{Câu 5.} Ta có $\vec{AB} - \vec{AD} = \vec{DB}$. Vì $ABCD$ là hình vuông cạnh $a$ nên độ dài đường chéo $DB = a\sqrt{2}$. Chọn \textbf{A}.

\textbf{Câu 6.} Vì $G$ là trọng tâm và $M$ là trung điểm $BC$, ta có $AG = \dfrac{2}{3}AM \Rightarrow AG = 2GM$. Do $\vec{AG}$ và $\vec{GM}$ cùng hướng nên $\vec{AG} = 2\vec{GM}$. Chọn \textbf{C}.

\textbf{Câu 7.} Vì $M$ thuộc đoạn $BC$ và $MB = 2MC$ nên $\vec{MB} = -2\vec{MC} \Leftrightarrow \vec{AB} - \vec{AM} = -2(\vec{AC} - \vec{AM}) \Leftrightarrow 3\vec{AM} = \vec{AB} + 2\vec{AC} \Leftrightarrow \vec{AM} = \dfrac{1}{3}\vec{AB} + \dfrac{2}{3}\vec{AC}$. Chọn \textbf{B}.

\textbf{Câu 8.} Ba điểm phân biệt $A, B, C$ thẳng hàng khi và chỉ khi hai vectơ $\vec{AB}$ và $\vec{AC}$ cùng phương, tức tồn tại số thực $k \ne 0$ sao cho $\vec{AB} = k\vec{AC}$. Chọn \textbf{D}.

\textbf{Câu 9.} Vectơ $\vec{u} = 2\vec{i} - 5\vec{j}$ có tọa độ là $(2; -5)$. Chọn \textbf{C}.

\textbf{Câu 10.} $\vec{AB} = (4 - (-1); 1 - 3) = (5; -2)$. Chọn \textbf{B}.

\textbf{Câu 11.} Tọa độ trung điểm $M$ của $AB$: $x_M = \dfrac{2 + (-4)}{2} = -1$; $y_M = \dfrac{4 + 2}{2} = 3 \Rightarrow M(-1; 3)$. Chọn \textbf{A}.

\textbf{Câu 12.} Tứ giác $ABCD$ là hình bình hành khi $\vec{AD} = \vec{BC} \Leftrightarrow (x_D - 1; y_D - 2) = (5 - 3; 2 - 5) = (2; -3) \Rightarrow x_D = 3, y_D = -1 \Rightarrow D(3; -1)$. Chọn \textbf{D}.

\textbf{Câu 13.} Hai vectơ $\vec{a}$ và $\vec{b}$ cùng phương khi $2(6) - (-3)m = 0 \Leftrightarrow 12 + 3m = 0 \Leftrightarrow m = -4$. Chọn \textbf{B}.

\textbf{Câu 14.} Vì $\triangle ABC$ đều nên góc $\widehat{B} = 60^\circ$. Góc giữa hai vectơ $\vec{AB}$ và $\vec{BC}$ là góc bù với $\widehat{B}$: $(\vec{AB}, \vec{BC}) = 180^\circ - 60^\circ = 120^\circ$. Chọn \textbf{C}.

\textbf{Câu 15.} Đường chéo hình vuông $AC = a\sqrt{2}$, góc $\widehat{BAC} = 45^\circ$. Do đó $\vec{AB} \cdot \vec{AC} = AB \cdot AC \cdot \cos 45^\circ = a \cdot a\sqrt{2} \cdot \dfrac{\sqrt{2}}{2} = a^2$. Chọn \textbf{A}.

\textbf{Câu 16.} $\vec{u} \cdot \vec{v} = 3(4) + (-2)(5) = 12 - 10 = 2$. Chọn \textbf{D}.

\textbf{Câu 17.} $|\vec{OA}| = \sqrt{(-3)^2 + 4^2} = \sqrt{25} = 5$. Chọn \textbf{B}.

\textbf{Câu 18.} $\vec{x} \perp \vec{y} \Leftrightarrow 2(3) + m(-6) = 0 \Leftrightarrow 6 - 6m = 0 \Leftrightarrow m = 1$. Chọn \textbf{C}.

\textbf{Câu 19.} Ta có $\vec{a} \cdot \vec{b} = 1(-2) + 2(1) = 0 \Rightarrow \vec{a} \perp \vec{b} \Rightarrow (\vec{a}, \vec{b}) = 90^\circ$. Chọn \textbf{A}.

\textbf{Câu 20.} $A = |\vec{F}| \cdot s \cdot \cos 60^\circ = 50 \cdot 10 \cdot 0{,}5 = 250\text{ J}$. Chọn \textbf{D}.

\columnbreak

\textbf{\color{accent}PHẦN II. ĐÚNG / SAI}

\textbf{Câu 1.}
a) Hình thoi có $AB = AD = a$ và $\widehat{BAD} = 60^\circ$ nên tam giác $ABD$ đều cạnh $a \Rightarrow$ \textbf{Đúng}.\\
b) $\vec{AB} + \vec{AD} = \vec{AC}$. Tam giác $ABD$ đều nên $BD = a$, đường cao $AO = \dfrac{a\sqrt{3}}{2} \Rightarrow AC = 2AO = a\sqrt{3} \ne a\sqrt{2} \Rightarrow$ \textbf{Sai}.\\
c) $\vec{AB} - \vec{AD} = \vec{DB} \Rightarrow |\vec{v}| = BD = a \Rightarrow$ \textbf{Đúng}.\\
d) Vì $O$ là trung điểm $AC$ nên $\vec{AO} + \vec{CO} = \vec{0} \ne \vec{AC} \Rightarrow$ \textbf{Sai}.

\textbf{Câu 2.}
a) Vì $M$ là trung điểm $AB$ nên $\vec{CM} = \dfrac{1}{2}(\vec{CA} + \vec{CB}) \ne \dfrac{1}{2}\vec{CA} - \vec{CB} \Rightarrow$ \textbf{Sai}.\\
b) $\vec{BN} = \vec{AN} - \vec{AB} = \dfrac{2}{3}\vec{AC} - \vec{AB} \Rightarrow$ \textbf{Đúng}.\\
c) Với $G$ là trọng tâm $\triangle ABC$, $\vec{AG} = \dfrac{1}{3}(\vec{AB} + \vec{AC}) = \dfrac{1}{3}\vec{AB} + \dfrac{1}{3}\vec{AC} \Rightarrow$ \textbf{Đúng}.\\
d) Do $M$ là trung điểm $AB$ nên $CM$ là trung tuyến của $\triangle ABC$. Trọng tâm $G$ luôn nằm trên đường trung tuyến $CM$, do đó $M, G, C$ thẳng hàng $\Rightarrow$ \textbf{Sai}.

\textbf{Câu 3.}
a) $\vec{AB} = (2 - (-2); 4 - 1) = (4; 3)$; $\vec{AC} = (5 - (-2); 0 - 1) = (7; -1) \Rightarrow$ \textbf{Đúng}.\\
b) Do $\dfrac{4}{7} \ne \dfrac{3}{-1}$ nên hai vectơ không cùng phương, ba điểm $A, B, C$ tạo thành tam giác $\Rightarrow$ \textbf{Đúng}.\\
c) Trọng tâm: $x_G = \dfrac{-2+2+5}{3} = \dfrac{5}{3}$; $y_G = \dfrac{1+4+0}{3} = \dfrac{5}{3} \Rightarrow G\left(\dfrac{5}{3}; \dfrac{5}{3}\right) \ne G\left(\dfrac{5}{3}; \dfrac{7}{3}\right) \Rightarrow$ \textbf{Sai}.\\
d) $\vec{AB} \cdot \vec{AC} = 4(7) + 3(-1) = 28 - 3 = 25 \Rightarrow$ \textbf{Đúng}.

\textbf{Câu 4.}
a) $\triangle ABC$ vuông cân tại $A \Rightarrow \widehat{B} = 45^\circ$, $BC = 4\sqrt{2}$. Ta có $\vec{BA} \cdot \vec{BC} = BA \cdot BC \cdot \cos 45^\circ = 4 \cdot 4\sqrt{2} \cdot \dfrac{\sqrt{2}}{2} = 16 \ne 8 \Rightarrow$ \textbf{Sai}.\\
b) Tam giác vuông cân tại $A$ nên $AM = \dfrac{BC}{2} = 2\sqrt{2} \ne 4 \Rightarrow$ \textbf{Sai}.\\
c) Vì tam giác cân tại $A$ nên trung tuyến $AM$ đồng thời là đường cao, do đó $AM \perp BC \Rightarrow \vec{AM} \cdot \vec{BC} = 0 \Rightarrow$ \textbf{Đúng}.\\
d) $|\vec{u}|^2 = \vec{AB}^2 + 4\vec{AB}\cdot\vec{AC} + 4\vec{AC}^2 = 16 + 0 + 4(16) = 80 \Rightarrow |\vec{u}| = \sqrt{80} = 4\sqrt{5} \Rightarrow$ \textbf{Đúng}.

\textbf{\color{accent}PHẦN III. TRẢ LỜI NGẮN}

\textbf{Câu 1.} $\vec{AB} + \vec{AD} = \vec{AC}$. Do đó $|\vec{u}| = AC = \sqrt{AB^2 + AD^2} = \sqrt{6^2 + 8^2} = \mathbf{10}$.

\textbf{Câu 2.} $\vec{IB} = -3\vec{IC} \Leftrightarrow \vec{AB} - \vec{AI} = -3(\vec{AC} - \vec{AI}) \Leftrightarrow 4\vec{AI} = \vec{AB} + 3\vec{AC} \Leftrightarrow \vec{AI} = \dfrac{1}{4}\vec{AB} + \dfrac{3}{4}\vec{AC}$. Do đó $x = \dfrac{1}{4}, y = \dfrac{3}{4} \Rightarrow P = 4\left(\dfrac{1}{4}\right) + 8\left(\dfrac{3}{4}\right) = 1 + 6 = \mathbf{7}$.

\textbf{Câu 3.} $\vec{AB} = (2; 4)$, $\vec{AC} = (m - 1; 8)$. Ba điểm thẳng hàng khi $\dfrac{m - 1}{2} = \dfrac{8}{4} = 2 \Rightarrow m - 1 = 4 \Rightarrow m = \mathbf{5}$.

\textbf{Câu 4.} $\vec{a} \cdot \vec{b} = 2(3) + 1(-1) = 5$. Ta có $|\vec{a}| = \sqrt{4+1} = \sqrt{5}$, $|\vec{b}| = \sqrt{9+1} = \sqrt{10}$. Suy ra $\cos(\vec{a}, \vec{b}) = \dfrac{5}{\sqrt{5}\sqrt{10}} = \dfrac{1}{\sqrt{2}} = \dfrac{\sqrt{2}}{2} \Rightarrow (\vec{a}, \vec{b}) = \mathbf{45}^\circ$.

\textbf{Câu 5.} $\vec{BA} = (1; 3)$, $\vec{BC} = (k - 1; -1)$. Tam giác vuông tại $B \Leftrightarrow \vec{BA} \cdot \vec{BC} = 0 \Leftrightarrow 1(k - 1) + 3(-1) = 0 \Leftrightarrow k - 4 = 0 \Rightarrow k = \mathbf{4}$.

\textbf{Câu 6.} Vì $\vec{F}_1 \perp \vec{F}_2$ nên độ lớn hợp lực là $|\vec{F}| = \sqrt{|\vec{F}_1|^2 + |\vec{F}_2|^2} = \sqrt{6000^2 + 8000^2} = \mathbf{10000}\text{ N}$.

\textbf{\color{accent}PHẦN IV. TỰ LUẬN}

\textbf{Bài 1.}
a) Ta có: $\vec{MN} = \vec{AN} - \vec{AM}$.\\
Vì $M$ là trung điểm $AB \Rightarrow \vec{AM} = \dfrac{1}{2}\vec{AB}$.\\
Vì $AN = \dfrac{1}{3}AC \Rightarrow \vec{AN} = \dfrac{1}{3}\vec{AC}$.\\
Vậy $\vec{MN} = \mathbf{-\dfrac{1}{2}\vec{AB} + \dfrac{1}{3}\vec{AC}}$.\\
b) Vì $B$ là trung điểm $PC$ nên $\vec{PB} = \vec{BC} = \vec{AC} - \vec{AB}$.\\
Suy ra $\vec{AP} = \vec{AB} + \vec{BP} = \vec{AB} - \vec{PB} = \vec{AB} - (\vec{AC} - \vec{AB}) = 2\vec{AB} - \vec{AC}$.\\
Do đó $\vec{MP} = \vec{AP} - \vec{AM} = (2\vec{AB} - \vec{AC}) - \dfrac{1}{2}\vec{AB} = \mathbf{\dfrac{3}{2}\vec{AB} - \vec{AC}}$.\\
Nhận thấy $\vec{MP} = -3\left(-\dfrac{1}{2}\vec{AB} + \dfrac{1}{3}\vec{AC}\right) = -3\vec{MN}$.\\
Vậy hai vectơ $\vec{MP}$ và $\vec{MN}$ cùng phương, suy ra ba điểm $M, N, P$ thẳng hàng.

\textbf{Bài 2.}
a) Độ dài các cạnh:\\
$AB = \sqrt{(3 - (-1))^2 + (4 - 2)^2} = \sqrt{16 + 4} = \sqrt{20} = 2\sqrt{5} \approx 4{,}47$.\\
$BC = \sqrt{(2 - 3)^2 + (-1 - 4)^2} = \sqrt{1 + 25} = \sqrt{26} \approx 5{,}10$.\\
$AC = \sqrt{(2 - (-1))^2 + (-1 - 2)^2} = \sqrt{9 + 9} = \sqrt{18} = 3\sqrt{2} \approx 4{,}24$.\\
Chu vi tam giác $ABC$: $P = 2\sqrt{5} + \sqrt{26} + 3\sqrt{2} \approx \mathbf{13{,}8}$.\\
b) Gọi trực tâm là $H(x; y)$. Ta có $\vec{AH} = (x + 1; y - 2)$, $\vec{BC} = (-1; -5)$ và $\vec{BH} = (x - 3; y - 4)$, $\vec{AC} = (3; -3)$.\\
$H$ là trực tâm $\triangle ABC \Leftrightarrow \begin{cases} \vec{AH} \cdot \vec{BC} = 0 \\ \vec{BH} \cdot \vec{AC} = 0 \end{cases}$\\
$\Leftrightarrow \begin{cases} -1(x + 1) - 5(y - 2) = 0 \\ 3(x - 3) - 3(y - 4) = 0 \end{cases} \Leftrightarrow \begin{cases} -x - 5y + 9 = 0 \\ 3x - 3y + 3 = 0 \end{cases}$\\
$\Leftrightarrow \begin{cases} x + 5y = 9 \\ x - y = -1 \end{cases} \Leftrightarrow \begin{cases} x = \dfrac{2}{3} \\ y = \dfrac{5}{3} \end{cases}$.\\
Vậy trực tâm của tam giác $ABC$ là $H\left(\mathbf{\dfrac{2}{3}}; \mathbf{\dfrac{5}{3}}\right)$.

\textbf{Bài 3.}
a) Các lực tác dụng lên điểm treo $O$ gồm: trọng lực $\vec{P}$ của vật và hai lực căng dây $\vec{T}_1, \vec{T}_2$.\\
Để hệ ở trạng thái cân bằng thì tổng hợp lực tác dụng lên $O$ bằng vectơ-không:\\
$$\mathbf{\vec{T}_1 + \vec{T}_2 + \vec{P} = \vec{0}}.$$
b) Chọn hệ trục tọa độ $Oxy$ với trục hoành nằm ngang hướng sang phải và trục tung hướng thẳng đứng lên trên.\\
Ta có $\vec{P} = (0; -100)$ (vì độ lớn $P = 100\text{ N}$).\\
Hai sợi dây tạo với trần nhà góc $30^\circ$ và $60^\circ$ nên:\\
$\vec{T}_1 = (-T_1 \cos 30^\circ;\ T_1 \sin 30^\circ) = \left(-\dfrac{\sqrt{3}}{2}T_1;\ \dfrac{1}{2}T_1\right)$,\\
$\vec{T}_2 = (T_2 \cos 60^\circ;\ T_2 \sin 60^\circ) = \left(\dfrac{1}{2}T_2;\ \dfrac{\sqrt{3}}{2}T_2\right)$.\\
Từ điều kiện cân bằng $\vec{T}_1 + \vec{T}_2 = -\vec{P} = (0; 100)$, ta có hệ:\\
$\begin{cases} -\dfrac{\sqrt{3}}{2}T_1 + \dfrac{1}{2}T_2 = 0 \\[4pt] \dfrac{1}{2}T_1 + \dfrac{\sqrt{3}}{2}T_2 = 100 \end{cases} \Leftrightarrow \begin{cases} T_2 = T_1\sqrt{3} \\[4pt] \dfrac{1}{2}T_1 + \dfrac{\sqrt{3}}{2}(T_1\sqrt{3}) = 100 \end{cases}$\\
$\Leftrightarrow 2T_1 = 100 \Leftrightarrow \mathbf{T_1 = 50\text{ N}}$.\\
Suy ra $\mathbf{T_2 = 50\sqrt{3}\text{ N}} \approx \mathbf{86{,}6\text{ N}}$.

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

    print("[3/4] Splitting into De_On_Tap_Vector_Exam.pdf and De_On_Tap_Vector_Ans.pdf...")
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

    print("\nBUILD COMPLETE FOR ĐỀ ÔN TẬP VECTƠ!")


if __name__ == "__main__":
    main()
