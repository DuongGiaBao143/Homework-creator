#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Build pipeline for Grade 10 Review Exam: Chương IV. Vectơ — Đề số 6 (Mã đề 1047).
Generates standalone student exam PDF (3 pages) and teacher answer key PDF (2 pages),
audits pagination, and exports copies to Grade 10 teaching folders.
"""

import re
import shutil
import subprocess
from pathlib import Path
import pymupdf

OUT_DIR = Path(r"d:\Tao_De\Lớp 10\Output\De_On_Tap_Vector_6")
TEX_PATH = OUT_DIR / "De_On_Tap_Vector_6.tex"
FULL_PDF = OUT_DIR / "De_On_Tap_Vector_6.pdf"
EXAM_PDF = OUT_DIR / "De_On_Tap_Vector_6_Exam.pdf"
ANS_PDF = OUT_DIR / "De_On_Tap_Vector_6_Ans.pdf"

EXPORT_TARGETS = [
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\Vector\De_On_Tap_Vector_6.pdf"), "exam"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\Vector\Ans\De_On_Tap_Vector_6_Ans.pdf"), "ans"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương IV\Đề ôn tập Chương 4 - Vectơ (Đề 6).pdf"), "exam"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương IV\Ans\Đề ôn tập Chương 4 - Vectơ (Đề 6 - Đáp án).pdf"), "ans"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương IV\Ans\Đề ôn tập Chương 4 - Vectơ (Đề 6 - có đáp án).pdf"), "full"),
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
  \lfoot{\small\textit{\color{gray!60!black}Đáp án Đề ôn tập Chương IV. Vectơ (Đề số 6) — Toán 10 KNTT}}
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

TIKZ_P2_Q1 = r"""\begin{tikzpicture}[scale=0.62, >=Stealth]
  \coordinate (A) at (0,0);
  \coordinate (B) at (2.0,0);
  \coordinate (C) at (2.0,2.8);
  \coordinate (D) at (0,2.8);
  \coordinate (M) at (2.0,1.4);
  \draw[thick, ink] (A) -- (B) -- (C) -- (D) -- cycle;
  \draw[dashed, gray!75] (A) -- (C);
  \draw[dashed, accent!80] (A) -- (M);
  \draw[gray!75] (0,0.28) -- (0.28,0.28) -- (0.28,0);
  \fill[ink] (M) circle (2pt);
  \node[below left, font=\scriptsize] at (A) {$A$};
  \node[below right, font=\scriptsize] at (B) {$B$};
  \node[above right, font=\scriptsize] at (C) {$C$};
  \node[above left, font=\scriptsize] at (D) {$D$};
  \node[right, font=\scriptsize] at (M) {$M$};
\end{tikzpicture}"""

TIKZ_P3_Q6 = r"""\begin{tikzpicture}[scale=0.56, >=Stealth]
  \fill[accent!18] (-0.35,-0.25) rectangle (0.35,0.25);
  \draw[thick, ink] (-0.35,-0.25) rectangle (0.35,0.25);
  \coordinate (O) at (0.35,0);
  \coordinate (F1) at (2.35,0);
  \coordinate (F2) at (1.95, 2.77);
  \draw[->, very thick, ink] (O) -- (F1) node[below, font=\scriptsize] {$\vec{F}_1$};
  \draw[->, very thick, accent] (O) -- (F2) node[above left, font=\scriptsize] {$\vec{F}_2$};
  \pic[draw, angle radius=0.45cm, "$60^\circ$", angle eccentricity=1.65, font=\tiny] {angle = F1--O--F2};
\end{tikzpicture}"""

TIKZ_P4_B3 = r"""\begin{tikzpicture}[scale=0.62, >=Stealth]
  \fill[cyan!8] (-1.8,0) rectangle (2.3,2.0);
  \draw[thick, gray!80] (-1.8,0) -- (2.3,0);
  \draw[thick, gray!80] (-1.8,2.0) -- (2.3,2.0);
  \coordinate (O) at (0,0);
  \coordinate (B) at (0,2.0);
  \coordinate (Vn) at (1.125,0);
  \coordinate (Vp) at (-1.125,1.5);
  \coordinate (V) at (0,1.5);
  \draw[->, gray!70] (O) -- (2.25,0) node[below, font=\tiny] {$x$ (Đông)};
  \draw[->, gray!70] (O) -- (0,2.55) node[above, font=\tiny] {$y$ (Bắc)};
  \draw[->, very thick, accent] (O) -- (Vn) node[below, font=\tiny] {$\vec{v}_n$};
  \draw[->, very thick, ink] (O) -- (Vp) node[midway, below left, font=\tiny] {$\vec{v}_p$};
  \draw[->, very thick, ink!75!cyan] (O) -- (V) node[right, font=\tiny] {$\vec{v}$};
  \draw[dashed, gray!65] (Vp) -- (V) -- (Vn);
  \draw[<->, gray!75] (2.05,0) -- (2.05,2.0) node[midway, right, font=\tiny] {$240\text{ m}$};
  \fill[ink] (O) circle (1.6pt);
  \fill[ink] (B) circle (1.6pt);
  \node[below left, font=\tiny] at (O) {$A \equiv O$};
  \node[above left, font=\tiny] at (B) {$B$};
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
    \textbf{ĐỀ ÔN TẬP SỐ 6}
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
        \textbf{1047}
    \end{minipage}}
\end{minipage}
\vspace{0.05cm}

\parttitle{PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn}
\textit{Thí sinh trả lời từ câu 1 đến câu 20. Mỗi câu hỏi thí sinh chỉ chọn một phương án.}
\begin{enumerate}
\item Cho $6$ điểm phân biệt nằm trên cùng một đường thẳng. Số vectơ khác vectơ-không có điểm đầu và điểm cuối là $2$ trong $6$ điểm đã cho là
\four{$15$.}{$30$.}{$12$.}{$36$.}

\item Cho hai vectơ $\vec{a}$ và $\vec{b}$ khác vectơ-không và ngược hướng với nhau, biết $|\vec{a}| = 6$ và $|\vec{b}| = 2$. Khẳng định nào sau đây đúng?
\four{$\vec{a} = 3\vec{b}$.}{$\vec{a} = -\dfrac{1}{3}\vec{b}$.}{$\vec{b} = 3\vec{a}$.}{$\vec{a} = -3\vec{b}$.}

\item Cho lục giác đều $ABCDEF$ tâm $O$. Tổng vectơ $\vec{OA} + \vec{OB} + \vec{OC} + \vec{OD} + \vec{OE} + \vec{OF}$ bằng
\four{$\vec{0}$.}{$2\vec{AD}$.}{$6\vec{OA}$.}{$\vec{AB}$.}

\item Cho hình chữ nhật $ABCD$ có $AB = 5$ và $AD = 12$. Độ dài của vectơ $\vec{BA} + \vec{BC}$ bằng
\four{$17$.}{$7$.}{$13$.}{$\sqrt{119}$.}

\item Cho hình vuông $ABCD$ có cạnh bằng $2a$ và tâm $O$. Độ dài của vectơ $\vec{OA} + \vec{OB}$ bằng
\four{$a$.}{$a\sqrt{2}$.}{$2a\sqrt{2}$.}{$2a$.}

\item Cho tam giác $ABC$. Gọi $I$ và $K$ lần lượt là trung điểm của các cạnh $AB$ và $AC$. Mệnh đề nào sau đây đúng?
\four{$\vec{IK} = 2\vec{BC}$.}{$\vec{IK} = \dfrac{1}{2}\vec{BC}$.}{$\vec{IK} = -\dfrac{1}{2}\vec{BC}$.}{$\vec{IK} = \dfrac{1}{3}\vec{BC}$.}

\item Cho tam giác $ABC$ và điểm $M$ thỏa mãn $\vec{MA} + 2\vec{MB} = \vec{0}$. Đẳng thức nào sau đây đúng?
\two{$\vec{CM} = \dfrac{1}{3}\vec{CA} + \dfrac{2}{3}\vec{CB}$.}{$\vec{CM} = \dfrac{2}{3}\vec{CA} + \dfrac{1}{3}\vec{CB}$.}{$\vec{CM} = \dfrac{1}{3}\vec{CA} - \dfrac{2}{3}\vec{CB}$.}{$\vec{CM} = -\dfrac{1}{3}\vec{CA} + \dfrac{2}{3}\vec{CB}$.}

\item Cho hình bình hành $ABCD$ tâm $O$. Điểm $M$ thỏa mãn $\vec{MA} + \vec{MB} + \vec{MC} + \vec{MD} = \vec{AB}$. Khẳng định nào sau đây đúng?
\four{$\vec{OM} = \dfrac{1}{4}\vec{AB}$.}{$\vec{MO} = \dfrac{1}{2}\vec{AB}$.}{$\vec{MO} = \dfrac{1}{4}\vec{AB}$.}{$\vec{MO} = -\dfrac{1}{4}\vec{AB}$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{a} = (3; -4)$ và $\vec{b} = (-1; 2)$. Tọa độ của vectơ $\vec{c} = 2\vec{a} + 3\vec{b}$ là
\four{$(9; -14)$.}{$(5; -2)$.}{$(-3; 2)$.}{$(3; -2)$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho điểm $A(4; -2)$ và vectơ $\vec{AB} = (-3; 5)$. Tọa độ của điểm $B$ là
\four{$B(1; 3)$.}{$B(7; -7)$.}{$B(-1; -3)$.}{$B(-7; 7)$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$ có $A(-2; 5)$, $B(4; -1)$ và trọng tâm $G(1; 2)$. Tọa độ đỉnh $C$ là
\four{$C(3; 6)$.}{$C(-1; 2)$.}{$C(1; 2)$.}{$C(1; 6)$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $P(-1; 3)$, $Q(2; -3)$ và $R(5; m)$. Giá trị của tham số $m$ để ba điểm $P, Q, R$ thẳng hàng là
\four{$m = 9$.}{$m = -9$.}{$m = -3$.}{$m = 15$.}
\pagebreak

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{u} = (m; -6)$ và $\vec{v} = (-3; m + 3)$. Tất cả các giá trị của $m$ để $\vec{u}$ cùng phương với $\vec{v}$ là
\four{$m = 3$.}{$m = -3$ hoặc $m = 6$.}{$m = 3$ hoặc $m = -6$.}{$m = -6$.}

\item Cho tam giác $ABC$ cân tại $A$ có $\widehat{A} = 50^\circ$. Góc giữa hai vectơ $\vec{AB}$ và $\vec{BC}$ bằng
\four{$115^\circ$.}{$65^\circ$.}{$50^\circ$.}{$130^\circ$.}

\item Cho hai vectơ $\vec{a}, \vec{b}$ thỏa mãn $|\vec{a}| = 4$, $|\vec{b}| = 5$ và $(\vec{a}, \vec{b}) = 120^\circ$. Giá trị của $\vec{a} \cdot (\vec{a} + \vec{b})$ bằng
\four{$26$.}{$16$.}{$-10$.}{$6$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$ có $A(1; 2)$, $B(4; -2)$ và $C(-1; 4)$. Giá trị của tích vô hướng $\vec{AB} \cdot \vec{AC}$ bằng
\four{$14$.}{$-14$.}{$2$.}{$-2$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho vectơ $\vec{u} = (x; x + 2)$ với $x > 0$. Biết $|\vec{u}| = 10$, giá trị của $x$ bằng
\four{$6$.}{$8$.}{$5$.}{$4$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{a} = (2; -5)$ và $\vec{b} = (m + 4; 2)$. Giá trị của $m$ để $\vec{a} \perp \vec{b}$ là
\four{$m = -1$.}{$m = 5$.}{$m = -9$.}{$m = 1$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{a} = (3; 1)$ và $\vec{b} = (1; 2)$. Giá trị của $\cos(\vec{a}, \vec{b})$ bằng
\four{$\dfrac{1}{2}$.}{$\dfrac{\sqrt{3}}{2}$.}{$\dfrac{\sqrt{2}}{2}$.}{$\dfrac{1}{\sqrt{5}}$.}

\item Hai lực $\vec{F}_1$ và $\vec{F}_2$ có cùng điểm đặt, cùng độ lớn bằng $30\text{ N}$ và hợp với nhau một góc $60^\circ$. Độ lớn của hợp lực $\vec{F} = \vec{F}_1 + \vec{F}_2$ bằng
\four{$30\text{ N}$.}{$30\sqrt{3}\text{ N}$.}{$60\text{ N}$.}{$30\sqrt{2}\text{ N}$.}
\end{enumerate}

\parttitle{PHẦN II. Câu trắc nghiệm đúng sai}
\textit{Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.}
\begin{enumerate}
\item Cho hình chữ nhật $ABCD$ có $AB = 8$, $AD = 12$ và $M$ là trung điểm của cạnh $BC$ (xem hình vẽ bên).
\par\noindent\begin{minipage}[t]{0.73\linewidth}
\begin{enumerate}
    \item Độ dài đường chéo $AC = 20$.
    \item Tích vô hướng $\vec{AB} \cdot \vec{AC} = 64$.
    \item Tích vô hướng $\vec{AM} \cdot \vec{BD} = 16$.
    \item Độ dài đoạn thẳng $AM = 10$.
\end{enumerate}
\end{minipage}\hfill
\begin{minipage}[t]{0.25\linewidth}\raggedleft\vspace{-10pt}
""" + TIKZ_P2_Q1 + r"""
\end{minipage}

\item Cho tam giác $ABC$. Gọi $G$ là trọng tâm của tam giác $ABC$, $M$ là trung điểm của cạnh $BC$, và điểm $N$ thỏa mãn $\vec{AN} = 3\vec{AB}$.
\begin{enumerate}
    \item $\vec{GA} + \vec{GB} + \vec{GC} = \vec{0}$.
    \item $\vec{MG} = \dfrac{1}{6}\vec{AB} + \dfrac{1}{6}\vec{AC}$.
    \item $\vec{MN} = \dfrac{5}{2}\vec{AB} - \dfrac{1}{2}\vec{AC}$.
    \item $\vec{CN} = 3\vec{AB} + \vec{AC}$.
\end{enumerate}

\item Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$ có $A(-1; 2)$, $B(3; 4)$ và $C(1; -2)$.
\begin{enumerate}
    \item Tọa độ vectơ $\vec{AB} = (-4; -2)$.
    \item Trọng tâm $G$ của tam giác $ABC$ có tọa độ là $G\!\left(1; \dfrac{2}{3}\right)$.
    \item Tam giác $ABC$ vuông cân tại $A$.
    \item Diện tích tam giác $ABC$ bằng $10$.
\end{enumerate}

\item Cho tam giác $ABC$ có $AB = 6$, $AC = 10$ và $\widehat{BAC} = 120^\circ$.
\begin{enumerate}
    \item Tích vô hướng $\vec{AB} \cdot \vec{AC} = -30$.
    \item Độ dài cạnh $BC = 14$.
    \item Độ dài vectơ $\vec{AB} + \vec{AC}$ bằng $16$.
    \item Tích vô hướng $\vec{BA} \cdot \vec{BC} = 6$.
\end{enumerate}
\end{enumerate}
\pagebreak

\parttitle{PHẦN III. Câu trắc nghiệm trả lời ngắn}
\textit{Thí sinh trả lời từ câu 1 đến câu 6.}
\begin{enumerate}
\item Cho hình thoi $ABCD$ có cạnh bằng $12$ và $\widehat{BAD} = 60^\circ$. Tính độ dài của vectơ $\vec{u} = \vec{AB} - \vec{AD}$. \answerbox

\item Cho tam giác $ABC$. Gọi $M$ là trung điểm của cạnh $AB$ và điểm $N$ nằm trên cạnh $AC$ sao cho $AN = 3NC$. Biết rằng $\vec{MN} = x\vec{AB} + y\vec{AC}$. Tính giá trị biểu thức $T = 8y - 2x$. \answerbox

\item Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A(2; -1)$, $B(0; 3)$ và $C(-3; 2)$. Điểm $M(x_M; y_M)$ thỏa mãn đẳng thức $\vec{MA} + 3\vec{MB} - 2\vec{MC} = \vec{0}$. Tính giá trị $T = 2x_M + y_M$. \answerbox

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{u} = (4; -3)$ và $\vec{v} = (8; 6)$. Tính $\cos(\vec{u}, \vec{v})$ (viết kết quả dưới dạng số thập phân). \answerbox

\item Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A(-1; 2)$, $B(5; 4)$ và điểm $M(m; 0)$. Tìm giá trị của $m$ sao cho $MA = MB$. \answerbox

\item Hai tàu kéo một xà lan trên mặt nước bằng hai lực $\vec{F}_1$ và $\vec{F}_2$ cùng nằm trong mặt phẳng nằm ngang, có độ lớn lần lượt là $F_1 = 300\text{ N}$ và $F_2 = 500\text{ N}$, hợp với nhau một góc $60^\circ$ (như hình vẽ). Tính độ lớn của hợp lực $\vec{F} = \vec{F}_1 + \vec{F}_2$ (đơn vị: Newton).
\par\noindent\begin{minipage}[c]{0.68\linewidth}
\answerbox
\end{minipage}\hfill
\begin{minipage}[c]{0.30\linewidth}\raggedleft
""" + TIKZ_P3_Q6 + r"""
\end{minipage}
\end{enumerate}

\parttitle{PHẦN IV. Câu tự luận}
\textit{Thí sinh trình bày lời giải chi tiết từ Bài 1 đến Bài 3.}

\textbf{Bài 1. (1,0 điểm)} Cho tam giác $ABC$. Gọi $I$ là trung điểm của cạnh $BC$, $M$ là trung điểm của đoạn thẳng $AI$, và điểm $N$ thuộc cạnh $AC$ sao cho $NC = 2NA$.
\begin{enumerate}[label=\alph*), leftmargin=0.6cm, itemsep=2pt]
    \item (0,5 điểm) Hãy biểu diễn hai vectơ $\vec{BM}$ và $\vec{BN}$ theo hai vectơ $\vec{AB}$ và $\vec{AC}$.
    \item (0,5 điểm) Chứng minh rằng ba điểm $B, M, N$ thẳng hàng.
\end{enumerate}

\textbf{Bài 2. (1,0 điểm)} Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A(2; 5)$, $B(-1; -1)$ và $C(4; 4)$.
\begin{enumerate}[label=\alph*), leftmargin=0.6cm, itemsep=2pt]
    \item (0,5 điểm) Chứng minh tam giác $ABC$ vuông tại $A$ và tìm tọa độ điểm $D$ sao cho tứ giác $ABCD$ là hình bình hành.
    \item (0,5 điểm) Tìm tọa độ điểm $P$ nằm trên trục hoành $Ox$ sao cho biểu thức $T = |\vec{PA} + \vec{PB} + 2\vec{PC}|$ đạt giá trị nhỏ nhất, và tính giá trị nhỏ nhất đó.
\end{enumerate}

\textbf{Bài 3. (1,0 điểm)} Một chiếc phà muốn đi thẳng qua một con sông rộng $240\text{ m}$ (vuông góc với hai bờ sông song song) từ bến $A$ ở bờ Nam sang bến $B$ ở bờ Bắc. Biết nước sông chảy theo hướng từ Tây sang Đông với vận tốc $\vec{v}_n$ có độ lớn $v_n = 3\text{ m/s}$, còn vận tốc thực của phà khi nước đứng yên có độ lớn $v_p = 5\text{ m/s}$ theo vectơ $\vec{v}_p$. Chọn hệ trục tọa độ $Oxy$ gắn với mặt đất có gốc $O \equiv A$, tia $Ox$ hướng về phía Đông và tia $Oy$ hướng về phía Bắc (đơn vị trên trục vận tốc là $\text{m/s}$, xem hình vẽ).
\par\noindent\begin{minipage}[t]{0.66\linewidth}
\begin{enumerate}[label=\alph*), leftmargin=0.6cm, itemsep=2pt]
    \item (0,5 điểm) Để phà đi thẳng theo hướng $AB$ (trùng tia $Oy$), vận tốc tổng hợp $\vec{v} = \vec{v}_p + \vec{v}_n$ phải cùng hướng với tia $Oy$. Hãy tìm tọa độ của vectơ $\vec{v}_p$ và vectơ $\vec{v}$ trong hệ trục $Oxy$.
    \item (0,5 điểm) Tính thời gian để phà sang đến bến $B$ và xác định góc hợp bởi hướng mũi phà (vectơ $\vec{v}_p$) với hướng chảy của dòng nước (tia $Ox$, làm tròn kết quả góc đến hàng phần mười của độ).
\end{enumerate}
\end{minipage}\hfill
\begin{minipage}[t]{0.32\linewidth}\raggedleft\vspace{-10pt}
""" + TIKZ_P4_B3 + r"""
\end{minipage}
""")

    # ==================== ĐÁP ÁN & HƯỚNG DẪN GIẢI ====================
    parts.append(r"""\newpage
\pagestyle{dapan}
\setcounter{page}{1}

\begin{center}
  {\Large\bfseries\color{ink} BẢNG ĐÁP ÁN TỔNG HỢP}\\[2pt]
  {\small\color{gray!75!black} Đề ôn tập Toán 10 — Chương IV. Vectơ — Đề số 6 (Mã đề 1047)}
\end{center}
\vspace{1pt}

\noindent\textbf{PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (20 câu)}
\vspace{1.5pt}

\begin{center}
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|}
\hline
\textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{7} & \textbf{8} & \textbf{9} & \textbf{10} \\ \hline
\textbf{B} & \textbf{D} & \textbf{A} & \textbf{C} & \textbf{D} & \textbf{B} & \textbf{A} & \textbf{C} & \textbf{D} & \textbf{A} \\ \hline
\hline
\textbf{11} & \textbf{12} & \textbf{13} & \textbf{14} & \textbf{15} & \textbf{16} & \textbf{17} & \textbf{18} & \textbf{19} & \textbf{20} \\ \hline
\textbf{C} & \textbf{B} & \textbf{C} & \textbf{A} & \textbf{D} & \textbf{B} & \textbf{A} & \textbf{D} & \textbf{C} & \textbf{B} \\ \hline
\end{tabular}
\end{center}

\vspace{1pt}
\noindent\begin{minipage}[t]{0.58\linewidth}
\textbf{PHẦN II. Câu trắc nghiệm đúng/sai}\\[1.5pt]
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|c|c|c|c|c|}
\hline
\textbf{Câu} & \textbf{a)} & \textbf{b)} & \textbf{c)} & \textbf{d)} \\ \hline
\textbf{1} & \textbf{S} & \textbf{Đ} & \textbf{S} & \textbf{Đ} \\ \hline
\textbf{2} & \textbf{Đ} & \textbf{S} & \textbf{Đ} & \textbf{S} \\ \hline
\textbf{3} & \textbf{S} & \textbf{S} & \textbf{Đ} & \textbf{Đ} \\ \hline
\textbf{4} & \textbf{Đ} & \textbf{Đ} & \textbf{S} & \textbf{S} \\ \hline
\end{tabular}
\end{minipage}\hfill
\begin{minipage}[t]{0.40\linewidth}
\textbf{PHẦN III. Trả lời ngắn}\\[1.5pt]
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|c|c|c|c|}
\hline
\textbf{Câu} & \textbf{Đáp số} & \textbf{Câu} & \textbf{Đáp số} \\ \hline
\textbf{1} & $12$ & \textbf{4} & $0{,}28$ \\ \hline
\textbf{2} & $7$  & \textbf{5} & $3$ \\ \hline
\textbf{3} & $10$ & \textbf{6} & $700$ \\ \hline
\end{tabular}
\end{minipage}

\vspace{5pt}
\noindent\textbf{PHẦN IV. Đáp số tự luận:}\\[2pt]
- \textbf{Bài 1:} a) $\vec{BM} = -\dfrac{3}{4}\vec{AB} + \dfrac{1}{4}\vec{AC}$; $\vec{BN} = -\vec{AB} + \dfrac{1}{3}\vec{AC}$. b) $\vec{BM} = \dfrac{3}{4}\vec{BN} \Rightarrow B, M, N$ thẳng hàng.\\
- \textbf{Bài 2:} a) $\vec{AB}\cdot\vec{AC} = 0$; $D(7; 10)$. b) $P\!\left(\dfrac{9}{4}; 0\right)$, GTNN bằng $12$.\\
- \textbf{Bài 3:} a) $\vec{v}_p = (-3; 4)\text{ m/s}$, $\vec{v} = (0; 4)\text{ m/s}$. b) $t = 60\text{ s}$; góc $\approx 126{,}9^\circ$.

\vspace{4pt}
\begin{center}
  {\large\bfseries\color{ink} HƯỚNG DẪN GIẢI CHI TIẾT}
\end{center}
\vspace{1pt}

\begin{multicols}{2}
\raggedcolumns
\small

\textbf{\color{accent}PHẦN I. TRẮC NGHIỆM}

\textbf{Câu 1.} Số vectơ khác $\vec{0}$ tạo bởi $2$ trong $6$ điểm là $A_6^2 = 6 \times 5 = 30$. Chọn \textbf{B}.

\textbf{Câu 2.} Vì $\vec{a}, \vec{b}$ ngược hướng và $|\vec{a}| = 3|\vec{b}|$ nên $\vec{a} = -3\vec{b}$. Chọn \textbf{D}.

\textbf{Câu 3.} Nhóm các cặp vectơ đối qua tâm $O$: $(\vec{OA} + \vec{OD}) + (\vec{OB} + \vec{OE}) + (\vec{OC} + \vec{OF}) = \vec{0}$. Chọn \textbf{A}.

\textbf{Câu 4.} $\vec{BA} + \vec{BC} = \vec{BD} \Rightarrow |\vec{BA} + \vec{BC}| = BD = \sqrt{5^2 + 12^2} = 13$. Chọn \textbf{C}.

\textbf{Câu 5.} Gọi $M$ là trung điểm $AB \Rightarrow |\vec{OA} + \vec{OB}| = 2OM = 2a$. Chọn \textbf{D}.

\textbf{Câu 6.} $IK$ là đường trung bình $\triangle ABC$ nên $\vec{IK} = \dfrac{1}{2}\vec{BC}$. Chọn \textbf{B}.

\textbf{Câu 7.} $\vec{MA} + 2\vec{MB} = \vec{0} \Leftrightarrow \vec{CM} = \dfrac{1}{3}\vec{CA} + \dfrac{2}{3}\vec{CB}$. Chọn \textbf{A}.

\textbf{Câu 8.} $O$ là tâm $ABCD \Rightarrow \vec{MA} + \vec{MB} + \vec{MC} + \vec{MD} = 4\vec{MO} = \vec{AB} \Rightarrow \vec{MO} = \dfrac{1}{4}\vec{AB}$. Chọn \textbf{C}.

\textbf{Câu 9.} $\vec{c} = 2(3; -4) + 3(-1; 2) = (6 - 3; -8 + 6) = (3; -2)$. Chọn \textbf{D}.

\textbf{Câu 10.} $B = A + \vec{AB} = (4 - 3; -2 + 5) = (1; 3)$. Chọn \textbf{A}.

\textbf{Câu 11.} $C = 3G - A - B = (3 - (-2) - 4; 6 - 5 - (-1)) = (1; 2)$. Chọn \textbf{C}.

\textbf{Câu 12.} $\vec{PQ} = (3; -6)$, $\vec{PR} = (6; m - 3)$. Thẳng hàng $\Leftrightarrow 3(m - 3) + 36 = 0 \Leftrightarrow m = -9$. Chọn \textbf{B}.

\textbf{Câu 13.} $\vec{u} \parallel \vec{v} \Leftrightarrow m(m + 3) - 18 = 0 \Leftrightarrow m^2 + 3m - 18 = 0 \Leftrightarrow m \in \{3; -6\}$. Chọn \textbf{C}.

\textbf{Câu 14.} $\triangle ABC$ cân tại $A$ có $\widehat{B} = \dfrac{180^\circ - 50^\circ}{2} = 65^\circ \Rightarrow (\vec{AB}, \vec{BC}) = 180^\circ - 65^\circ = 115^\circ$. Chọn \textbf{A}.

\textbf{Câu 15.} $\vec{a}\cdot(\vec{a} + \vec{b}) = |\vec{a}|^2 + |\vec{a}||\vec{b}|\cos 120^\circ = 16 + 4\cdot 5\left(-\dfrac{1}{2}\right) = 6$. Chọn \textbf{D}.

\textbf{Câu 16.} $\vec{AB} = (3; -4)$, $\vec{AC} = (-2; 2) \Rightarrow \vec{AB}\cdot\vec{AC} = -6 - 8 = -14$. Chọn \textbf{B}.

\textbf{Câu 17.} $|\vec{u}| = 10 \Leftrightarrow x^2 + (x + 2)^2 = 100 \Leftrightarrow x^2 + 2x - 48 = 0 \Leftrightarrow x = 6$ (do $x > 0$). Chọn \textbf{A}.

\textbf{Câu 18.} $\vec{a} \perp \vec{b} \Leftrightarrow 2(m + 4) - 10 = 0 \Leftrightarrow 2m - 2 = 0 \Leftrightarrow m = 1$. Chọn \textbf{D}.

\textbf{Câu 19.} $\cos(\vec{a}, \vec{b}) = \dfrac{3\cdot 1 + 1\cdot 2}{\sqrt{10}\cdot\sqrt{5}} = \dfrac{5}{5\sqrt{2}} = \dfrac{\sqrt{2}}{2}$. Chọn \textbf{C}.

\textbf{Câu 20.} $|\vec{F}| = \sqrt{30^2 + 30^2 + 2\cdot 30\cdot 30\cos 60^\circ} = 30\sqrt{3}\text{ N}$. Chọn \textbf{B}.

\textbf{\color{accent}PHẦN II. ĐÚNG / SAI}

\textbf{Câu 1.}
a) $AC = \sqrt{8^2 + 12^2} = 4\sqrt{13} \neq 20$ (\textbf{S}).
b) $\vec{AB}\cdot\vec{AC} = \vec{AB}\cdot(\vec{AB} + \vec{AD}) = AB^2 + 0 = 64$ (\textbf{Đ}).
c) $\vec{AM} = \vec{AB} + \dfrac{1}{2}\vec{AD}$, $\vec{BD} = \vec{AD} - \vec{AB} \Rightarrow \vec{AM}\cdot\vec{BD} = -64 + 72 = 8 \neq 16$ (\textbf{S}).
d) $AM = \sqrt{AB^2 + BM^2} = \sqrt{8^2 + 6^2} = 10$ (\textbf{Đ}).

\textbf{Câu 2.}
a) Theo tính chất trọng tâm, $\vec{GA} + \vec{GB} + \vec{GC} = \vec{0}$ (\textbf{Đ}).
b) $\vec{MG} = \vec{AG} - \vec{AM} = \left(\dfrac{1}{3} - \dfrac{1}{2}\right)(\vec{AB} + \vec{AC}) = -\dfrac{1}{6}\vec{AB} - \dfrac{1}{6}\vec{AC}$ (\textbf{S}).
c) $\vec{MN} = \vec{AN} - \vec{AM} = 3\vec{AB} - \dfrac{1}{2}\vec{AB} - \dfrac{1}{2}\vec{AC} = \dfrac{5}{2}\vec{AB} - \dfrac{1}{2}\vec{AC}$ (\textbf{Đ}).
d) $\vec{CN} = \vec{AN} - \vec{AC} = 3\vec{AB} - \vec{AC}$ (\textbf{S}).

\textbf{Câu 3.}
a) $\vec{AB} = (3 - (-1); 4 - 2) = (4; 2) \neq (-4; -2)$ (\textbf{S}).
b) $G = \left(\dfrac{-1 + 3 + 1}{3}; \dfrac{2 + 4 - 2}{3}\right) = \left(1; \dfrac{4}{3}\right)$ (\textbf{S}).
c) $\vec{AB} = (4; 2)$, $\vec{AC} = (2; -4) \Rightarrow \vec{AB}\cdot\vec{AC} = 0$ và $AB = AC = 2\sqrt{5}$ (\textbf{Đ}).
d) $S_{\triangle ABC} = \dfrac{1}{2}AB\cdot AC = \dfrac{1}{2}(2\sqrt{5})^2 = 10$ (\textbf{Đ}).

\textbf{Câu 4.}
a) $\vec{AB}\cdot\vec{AC} = 6\cdot 10\cdot\cos 120^\circ = -30$ (\textbf{Đ}).
b) $BC = \sqrt{6^2 + 10^2 - 2(-30)} = \sqrt{196} = 14$ (\textbf{Đ}).
c) $|\vec{AB} + \vec{AC}| = \sqrt{36 + 100 + 2(-30)} = \sqrt{76} = 2\sqrt{19} \neq 16$ (\textbf{S}).
d) $\vec{BA}\cdot\vec{BC} = (-\vec{AB})\cdot(\vec{AC} - \vec{AB}) = AB^2 - \vec{AB}\cdot\vec{AC} = 36 - (-30) = 66$ (\textbf{S}).

\textbf{\color{accent}PHẦN III. TRẢ LỜI NGẮN}

\textbf{Câu 1.} $|\vec{AB} - \vec{AD}| = |\vec{DB}| = DB$. Vì $\widehat{BAD} = 60^\circ$ nên $\triangle ABD$ đều cạnh $12 \Rightarrow DB = \mathbf{12}$.

\textbf{Câu 2.} $\vec{MN} = \vec{AN} - \vec{AM} = -\dfrac{1}{2}\vec{AB} + \dfrac{3}{4}\vec{AC}$. Vậy $T = 8\left(\dfrac{3}{4}\right) - 2\left(-\dfrac{1}{2}\right) = 6 + 1 = \mathbf{7}$.

\textbf{Câu 3.} $(1 + 3 - 2)M = A + 3B - 2C \Rightarrow 2M = (8; 4) \Rightarrow M(4; 2) \Rightarrow T = 2(4) + 2 = \mathbf{10}$.

\textbf{Câu 4.} $\cos(\vec{u}, \vec{v}) = \dfrac{4\cdot 8 + (-3)\cdot 6}{5\cdot 10} = \dfrac{14}{50} = \mathbf{0{,}28}$.

\textbf{Câu 5.} $MA^2 = MB^2 \Leftrightarrow (m + 1)^2 + 4 = (m - 5)^2 + 16 \Leftrightarrow 12m = 36 \Leftrightarrow m = \mathbf{3}$.

\textbf{Câu 6.} $|\vec{F}| = \sqrt{300^2 + 500^2 + 2\cdot 300\cdot 500\cos 60^\circ} = \sqrt{490\,000} = \mathbf{700}\text{ N}$.

\textbf{\color{accent}PHẦN IV. TỰ LUẬN}

\textbf{Bài 1.}
a) $\vec{AM} = \dfrac{1}{2}\vec{AI} = \dfrac{1}{4}\vec{AB} + \dfrac{1}{4}\vec{AC} \Rightarrow \vec{BM} = \vec{AM} - \vec{AB} = -\dfrac{3}{4}\vec{AB} + \dfrac{1}{4}\vec{AC}$.\\
Vì $NC = 2NA \Rightarrow \vec{AN} = \dfrac{1}{3}\vec{AC} \Rightarrow \vec{BN} = \vec{AN} - \vec{AB} = -\vec{AB} + \dfrac{1}{3}\vec{AC}$.\\
b) Ta có $\vec{BM} = \dfrac{3}{4}\left(-\vec{AB} + \dfrac{1}{3}\vec{AC}\right) = \dfrac{3}{4}\vec{BN}$. Hai vectơ $\vec{BM}, \vec{BN}$ cùng phương nên $B, M, N$ thẳng hàng.

\textbf{Bài 2.}
a) $\vec{AB} = (-3; -6)$, $\vec{AC} = (2; -1) \Rightarrow \vec{AB}\cdot\vec{AC} = -6 + 6 = 0 \Rightarrow \triangle ABC$ vuông tại $A$.\\
$ABCD$ là hình bình hành $\Leftrightarrow \vec{AD} = \vec{BC} = (5; 5) \Rightarrow D = (2 + 5; 5 + 5) = (7; 10)$.\\
b) Gọi $K$ là điểm thỏa mãn $\vec{KA} + \vec{KB} + 2\vec{KC} = \vec{0}$:\\
$K = \dfrac{A + B + 2C}{4} = \left(\dfrac{2 - 1 + 8}{4}; \dfrac{5 - 1 + 8}{4}\right) = \left(\dfrac{9}{4}; 3\right)$.\\
Khi đó $T = |\vec{PA} + \vec{PB} + 2\vec{PC}| = |4\vec{PK}| = 4PK$. Vì $P \in Ox$, $PK$ nhỏ nhất khi $P$ là hình chiếu vuông góc của $K$ lên $Ox$, tức $P\!\left(\dfrac{9}{4}; 0\right)$. GTNN bằng $4 \cdot 3 = 12$.

\textbf{Bài 3.}
a) Vận tốc dòng nước: $\vec{v}_n = (3; 0)$. Đặt $\vec{v}_p = (x; y)$ với $x^2 + y^2 = 5^2 = 25$ ($y > 0$).\\
Ta có $\vec{v} = \vec{v}_p + \vec{v}_n = (x + 3; y)$. Để $\vec{v}$ cùng hướng với tia $Oy$ thì $x + 3 = 0 \Rightarrow x = -3$, suy ra $y = \sqrt{25 - 9} = 4$. Vậy $\vec{v}_p = (-3; 4)\text{ m/s}$ và $\vec{v} = (0; 4)\text{ m/s}$.\\
b) Thời gian phà sang sông: $t = \dfrac{240}{4} = 60\text{ s}$ ($1$ phút).\\
Góc $\alpha$ hợp bởi $\vec{v}_p = (-3; 4)$ và tia $Ox$ ($\vec{i} = (1; 0)$): $\cos\alpha = \dfrac{-3}{5} = -0{,}6 \Rightarrow \alpha \approx 126{,}9^\circ$.

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

    print("[3/4] Splitting into De_On_Tap_Vector_6_Exam.pdf and De_On_Tap_Vector_6_Ans.pdf...")
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

    print("\nBUILD COMPLETE FOR ĐỀ ÔN TẬP VECTƠ SỐ 6!")


if __name__ == "__main__":
    main()
