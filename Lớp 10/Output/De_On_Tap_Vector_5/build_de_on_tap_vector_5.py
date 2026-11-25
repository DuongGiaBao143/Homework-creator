#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Build pipeline for Grade 10 Review Exam: Chương IV. Vectơ — Đề số 5 (Mã đề 1046).
Generates standalone student exam PDF (3 pages) and teacher answer key PDF (2 pages),
audits pagination, and exports copies to Grade 10 teaching folders.
"""

import re
import shutil
import subprocess
from pathlib import Path
import pymupdf

OUT_DIR = Path(r"d:\Tao_De\Lớp 10\Output\De_On_Tap_Vector_5")
TEX_PATH = OUT_DIR / "De_On_Tap_Vector_5.tex"
FULL_PDF = OUT_DIR / "De_On_Tap_Vector_5.pdf"
EXAM_PDF = OUT_DIR / "De_On_Tap_Vector_5_Exam.pdf"
ANS_PDF = OUT_DIR / "De_On_Tap_Vector_5_Ans.pdf"

EXPORT_TARGETS = [
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\Vector\De_On_Tap_Vector_5.pdf"), "exam"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\Vector\Ans\De_On_Tap_Vector_5_Ans.pdf"), "ans"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương IV\Đề ôn tập Chương 4 - Vectơ (Đề 5).pdf"), "exam"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương IV\Ans\Đề ôn tập Chương 4 - Vectơ (Đề 5 - Đáp án).pdf"), "ans"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương IV\Ans\Đề ôn tập Chương 4 - Vectơ (Đề 5 - có đáp án).pdf"), "full"),
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
  \lfoot{\small\textit{\color{gray!60!black}Đáp án Đề ôn tập Chương IV. Vectơ (Đề số 5) — Toán 10 KNTT}}
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
  \coordinate (A) at (0,0);
  \coordinate (B) at (2.4,0);
  \coordinate (C) at (0,3.2);
  \coordinate (M) at (1.2,1.6);
  \draw[thick, ink] (A) -- (B) -- (C) -- cycle;
  \draw[dashed, gray!75] (A) -- (M);
  \draw[gray!75] (0,0.3) -- (0.3,0.3) -- (0.3,0);
  \fill[ink] (M) circle (2pt);
  \node[below left, font=\scriptsize] at (A) {$A$};
  \node[below right, font=\scriptsize] at (B) {$B$};
  \node[above left, font=\scriptsize] at (C) {$C$};
  \node[above right, font=\scriptsize] at (M) {$M$};
\end{tikzpicture}"""

TIKZ_P3_Q6 = r"""\begin{tikzpicture}[scale=0.58, >=Stealth]
  \draw[thick, gray!80] (-0.3,0) -- (3.9,0);
  \foreach \x in {0.0, 0.4, 0.8, 1.2, 1.6, 2.0, 2.4, 2.8, 3.2, 3.6} {
    \draw[gray!55] (\x, 0) -- (\x-0.18, -0.18);
  }
  \fill[accent!18] (0.2, 0.02) rectangle (1.4, 0.72);
  \draw[thick, ink] (0.2, 0.02) rectangle (1.4, 0.72);
  \coordinate (P) at (1.4, 0.37);
  \coordinate (H) at (3.6, 0.37);
  \coordinate (F) at (2.75, 2.71);
  \draw[->, dashed, ink!75] (P) -- (H);
  \draw[->, very thick, accent] (P) -- (F) node[above right, font=\scriptsize] {$\vec{F}$};
  \pic[draw, angle radius=0.42cm, "$60^\circ$", angle eccentricity=1.65, font=\tiny] {angle = H--P--F};
\end{tikzpicture}"""

TIKZ_P4_B3 = r"""\begin{tikzpicture}[scale=0.62, >=Stealth]
  \coordinate (O) at (0,0);
  \coordinate (A) at (1.5,0);
  \coordinate (B) at (2.75, 2.165);
  \coordinate (E) at (3.4,0);
  \coordinate (N) at (0,2.5);
  \draw[->, gray!70] (-0.25,0) -- (E) node[below, font=\tiny] {$x$ (Đông)};
  \draw[->, gray!70] (0,-0.25) -- (N) node[left, font=\tiny] {$y$ (Bắc)};
  \draw[->, very thick, ink] (O) -- (A) node[midway, below, font=\tiny] {$300\text{ m}$};
  \draw[->, very thick, ink] (A) -- (B) node[midway, below right, font=\tiny] {$500\text{ m}$};
  \draw[->, dashed, thick, accent] (O) -- (B);
  \pic[draw, angle radius=0.35cm, "$60^\circ$", angle eccentricity=1.65, font=\tiny] {angle = E--A--B};
  \fill[ink] (O) circle (1.6pt);
  \fill[ink] (A) circle (1.6pt);
  \fill[ink] (B) circle (1.6pt);
  \node[below left, font=\tiny] at (O) {$O$};
  \node[below, font=\tiny] at (1.5, -0.05) {$A$};
  \node[above right, font=\tiny] at (B) {$B$};
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
    \textbf{ĐỀ ÔN TẬP SỐ 5}
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
        \textbf{1046}
    \end{minipage}}
\end{minipage}
\vspace{0.05cm}

\parttitle{PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn}
\textit{Thí sinh trả lời từ câu 1 đến câu 20. Mỗi câu hỏi thí sinh chỉ chọn một phương án.}
\begin{enumerate}
\item Cho tam giác $ABC$ có $M, N, P$ lần lượt là trung điểm của $AB, BC, CA$. Từ sáu điểm $A, B, C, M, N, P$ có thể lập được bao nhiêu vectơ khác vectơ-không cùng phương với $\vec{BC}$?
\four{$8$.}{$6$.}{$4$.}{$10$.}

\item Cho hình bình hành $ABCD$ tâm $O$. Khẳng định nào sau đây \textbf{sai}?
\four{$\vec{AB} = \vec{DC}$.}{$\vec{OA} + \vec{OC} = \vec{0}$.}{$\vec{AD} = \vec{CB}$.}{$\vec{OB} = \vec{DO}$.}

\item Cho bốn điểm bất kì $A, B, C, D$. Biểu thức vectơ $\vec{AC} - \vec{BC} + \vec{BD}$ bằng
\four{$\vec{DA}$.}{$\vec{AD}$.}{$\vec{CD}$.}{$\vec{0}$.}

\item Cho hình thoi $ABCD$ có cạnh bằng $a$ và góc $\widehat{BCD} = 60^\circ$. Độ dài của vectơ $\vec{CB} + \vec{CD}$ bằng
\four{$a$.}{$2a$.}{$\dfrac{a\sqrt{3}}{2}$.}{$a\sqrt{3}$.}

\item Cho tam giác $ABC$ vuông cân tại $A$ có cạnh huyền $BC = 2a$. Độ dài của vectơ $\vec{AB} + \vec{AC}$ là
\four{$2a$.}{$a\sqrt{2}$.}{$4a$.}{$a$.}

\item Cho tam giác $ABC$ có trọng tâm $G$ và một điểm $M$ bất kì trong mặt phẳng. Đẳng thức nào sau đây đúng?
\two{$\vec{MA} + \vec{MB} + \vec{MC} = \vec{MG}$.}{$\vec{MA} + \vec{MB} + \vec{MC} = 2\vec{MG}$.}{$\vec{MA} + \vec{MB} + \vec{MC} = 3\vec{GM}$.}{$\vec{MA} + \vec{MB} + \vec{MC} = 3\vec{MG}$.}

\item Cho đoạn thẳng $AB$ và điểm $K$ nằm trên đường thẳng $AB$ thỏa mãn $2\vec{KA} + 3\vec{KB} = \vec{0}$. Khẳng định nào sau đây đúng?
\four{$\vec{AK} = \dfrac{2}{5}\vec{AB}$.}{$\vec{AK} = \dfrac{3}{5}\vec{AB}$.}{$\vec{AK} = -\dfrac{3}{5}\vec{AB}$.}{$\vec{AK} = \dfrac{3}{2}\vec{AB}$.}

\item Cho tam giác $ABC$ có trọng tâm $G$. Phân tích vectơ $\vec{BG}$ theo hai vectơ $\vec{BA}$ và $\vec{BC}$ ta được
\two{$\vec{BG} = \dfrac{1}{2}\vec{BA} + \dfrac{1}{2}\vec{BC}$.}{$\vec{BG} = \dfrac{2}{3}\vec{BA} + \dfrac{1}{3}\vec{BC}$.}{$\vec{BG} = \dfrac{1}{3}\vec{BA} + \dfrac{1}{3}\vec{BC}$.}{$\vec{BG} = \dfrac{1}{3}\vec{BA} + \dfrac{2}{3}\vec{BC}$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho $\vec{u} = 5\vec{i} - \vec{j}$ và $\vec{v} = (-2; 3)$. Tọa độ của vectơ $\vec{a} = \vec{u} - 2\vec{v}$ là
\four{$(9; -7)$.}{$(1; 5)$.}{$(9; 5)$.}{$(1; -7)$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $M(-3; 5)$ và $N(1; -1)$. Tọa độ của vectơ $\vec{NM}$ là
\four{$(4; -6)$.}{$(-4; 6)$.}{$(-2; 4)$.}{$(-1; 2)$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A(-2; 3)$ và $B(4; -5)$. Tọa độ trung điểm $I$ của đoạn thẳng $AB$ là
\four{$I(3; -4)$.}{$I(2; -2)$.}{$I(-3; 4)$.}{$I(1; -1)$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A(1; 2)$, $B(m; 6)$ và $C(-1; -2)$. Giá trị của tham số $m$ để ba điểm $A, B, C$ thẳng hàng là
\four{$m = 1$.}{$m = -3$.}{$m = 3$.}{$m = 2$.}
\pagebreak

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{a} = (4; -2)$ và $\vec{b} = (m + 1; 3)$. Giá trị của $m$ để $\vec{a}$ cùng phương với $\vec{b}$ là
\four{$m = 5$.}{$m = -7$.}{$m = -5$.}{$m = 7$.}

\item Cho tam giác $ABC$ vuông tại $A$ có $\widehat{C} = 40^\circ$. Góc giữa hai vectơ $\vec{CA}$ và $\vec{BC}$ bằng
\four{$40^\circ$.}{$50^\circ$.}{$130^\circ$.}{$140^\circ$.}

\item Cho tam giác đều $ABC$ có cạnh bằng $2a$ và $H$ là trung điểm của cạnh $BC$. Tích vô hướng $\vec{AB} \cdot \vec{AH}$ bằng
\four{$3a^2$.}{$a^2\sqrt{3}$.}{$6a^2$.}{$2a^2$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{u} = (3; -5)$ và $\vec{v} = (2; 4)$. Giá trị của tích vô hướng $\vec{u} \cdot (\vec{u} - \vec{v})$ là
\four{$20$.}{$14$.}{$48$.}{$-14$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A(2; -3)$ và $B(-4; 5)$. Độ dài đoạn thẳng $AB$ bằng
\four{$8$.}{$10$.}{$\sqrt{10}$.}{$14$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{x} = (m; 4)$ và $\vec{y} = (m - 3; -1)$. Tổng tất cả các giá trị của $m$ để $\vec{x} \perp \vec{y}$ bằng
\four{$-3$.}{$-4$.}{$4$.}{$3$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{a} = (1; \sqrt{3})$ và $\vec{b} = (-1; \sqrt{3})$. Góc giữa hai vectơ $\vec{a}$ và $\vec{b}$ bằng
\four{$30^\circ$.}{$45^\circ$.}{$60^\circ$.}{$120^\circ$.}

\item Một ô tô kéo một rơ-moóc đi được quãng đường $50\text{ m}$ trên mặt phẳng nằm ngang với lực kéo có độ lớn $2000\text{ N}$, hướng của lực kéo hợp với phương chuyển động một góc $60^\circ$. Công của lực kéo thực hiện được bằng
\four{$50\text{ kJ}$.}{$100\text{ kJ}$.}{$50\sqrt{3}\text{ kJ}$.}{$25\text{ kJ}$.}
\end{enumerate}

\parttitle{PHẦN II. Câu trắc nghiệm đúng sai}
\textit{Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.}
\begin{enumerate}
\item Cho tam giác $ABC$ vuông tại $A$ có $AB = 6$, $AC = 8$ và $M$ là trung điểm của cạnh $BC$ (xem hình vẽ bên).
\par\noindent\begin{minipage}[t]{0.73\linewidth}
\begin{enumerate}
    \item Độ dài cạnh huyền $BC = 10$.
    \item Độ dài vectơ tổng $|\vec{AB} + \vec{AC}| = 14$.
    \item Tích vô hướng $\vec{BA} \cdot \vec{BC} = 48$.
    \item Độ dài của vectơ $|2\vec{AB} - \vec{AC}| = 4\sqrt{13}$.
\end{enumerate}
\end{minipage}\hfill
\begin{minipage}[t]{0.25\linewidth}\raggedleft\vspace{-10pt}
""" + TIKZ_P2_Q1 + r"""
\end{minipage}

\item Cho hình bình hành $ABCD$. Gọi $I$ là trung điểm của cạnh $CD$ và điểm $K$ thuộc đường chéo $BD$ sao cho $BK = \dfrac{1}{3}BD$.
\begin{enumerate}
    \item $\vec{AI} = \vec{AB} + \dfrac{1}{2}\vec{AD}$.
    \item $\vec{AK} = \dfrac{2}{3}\vec{AB} + \dfrac{1}{3}\vec{AD}$.
    \item $\vec{IK} = \dfrac{1}{6}\vec{AB} - \dfrac{2}{3}\vec{AD}$.
    \item Ba điểm $A, K, I$ thẳng hàng.
\end{enumerate}

\item Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A(1; 5)$, $B(-2; 1)$ và $C(4; -3)$.
\begin{enumerate}
    \item Độ dài đoạn thẳng $AB = 5$.
    \item Tọa độ trung điểm $M$ của đoạn thẳng $AC$ là $M\!\left(\dfrac{5}{2}; 1\right)$.
    \item Tam giác $ABC$ vuông tại $B$.
    \item Tọa độ điểm $D$ sao cho tứ giác $ABCD$ là hình bình hành là $D(7; 2)$.
\end{enumerate}

\item Cho hình thoi $ABCD$ cạnh $2a$ có $\widehat{BAD} = 60^\circ$.
\begin{enumerate}
    \item Góc giữa hai vectơ $\vec{AB}$ và $\vec{BC}$ bằng $120^\circ$.
    \item Tích vô hướng $\vec{AB} \cdot \vec{AD} = 4a^2$.
    \item Độ dài vectơ tổng $|\vec{AB} + \vec{AD}| = 2a\sqrt{3}$.
    \item Tích vô hướng $\vec{AC} \cdot \vec{BD} = 0$.
\end{enumerate}
\end{enumerate}
\pagebreak

\parttitle{PHẦN III. Câu trắc nghiệm trả lời ngắn}
\textit{Thí sinh trả lời từ câu 1 đến câu 6.}
\begin{enumerate}
\item Cho tam giác đều $ABC$ có cạnh bằng $4\sqrt{3}$. Tính độ dài của vectơ $\vec{u} = \vec{AB} + \vec{AC}$. \answerbox

\item Cho hình bình hành $ABCD$. Gọi $M$ là trung điểm của cạnh $BC$ và điểm $N$ nằm trên cạnh $CD$ thỏa mãn $CN = 2ND$. Biết rằng $\vec{MN} = x\vec{AB} + y\vec{AD}$. Tính giá trị biểu thức $T = 4y - 6x$. \answerbox

\item Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A(3; -1)$, $B(-1; 2)$ và $C(3; 5)$. Điểm $D(x_D; y_D)$ thỏa mãn đẳng thức $\vec{DA} + 2\vec{DB} + \vec{DC} = \vec{0}$. Tính giá trị $T = x_D + 2y_D$. \answerbox

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{a} = (3; 4)$ và $\vec{b} = (4; 3)$. Tính $\cos(\vec{a}, \vec{b})$ (viết kết quả dưới dạng số thập phân). \answerbox

\item Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A(1; 2)$, $B(6; 2)$ và điểm $C(m; 0)$ với $m > 3$. Tìm giá trị của $m$ sao cho tam giác $ABC$ vuông tại $C$. \answerbox

\item Một người kéo một xe trượt trên mặt đất nằm ngang đi được một đoạn $25\text{ m}$ bằng một lực $\vec{F}$ không đổi có độ lớn $120\text{ N}$, phương của lực hợp với phương chuyển động nằm ngang một góc $60^\circ$ (như hình vẽ). Tính công $A$ (đơn vị: Jun) do lực $\vec{F}$ thực hiện.
\par\noindent\begin{minipage}[c]{0.68\linewidth}
\answerbox
\end{minipage}\hfill
\begin{minipage}[c]{0.30\linewidth}\raggedleft
""" + TIKZ_P3_Q6 + r"""
\end{minipage}
\end{enumerate}

\parttitle{PHẦN IV. Câu tự luận}
\textit{Thí sinh trình bày lời giải chi tiết từ Bài 1 đến Bài 3.}

\textbf{Bài 1. (1,0 điểm)} Cho hình bình hành $ABCD$. Gọi $I$ là trung điểm của cạnh $AD$, điểm $K$ thuộc cạnh $AB$ sao cho $AK = \dfrac{1}{4}AB$ và điểm $E$ thuộc đường chéo $AC$ sao cho $AE = \dfrac{1}{6}AC$.
\begin{enumerate}[label=\alph*), leftmargin=0.6cm, itemsep=2pt]
    \item (0,5 điểm) Hãy biểu diễn hai vectơ $\vec{IE}$ và $\vec{IK}$ theo hai vectơ $\vec{AB}$ và $\vec{AD}$.
    \item (0,5 điểm) Chứng minh rằng ba điểm $I, E, K$ thẳng hàng.
\end{enumerate}

\textbf{Bài 2. (1,0 điểm)} Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A(1; 2)$, $B(5; 0)$ và $C(3; 6)$.
\begin{enumerate}[label=\alph*), leftmargin=0.6cm, itemsep=2pt]
    \item (0,5 điểm) Chứng minh tam giác $ABC$ vuông cân tại $A$ và tìm tọa độ điểm $D$ sao cho tứ giác $ABDC$ là hình vuông.
    \item (0,5 điểm) Tìm tọa độ điểm $N$ nằm trên trục tung $Oy$ sao cho độ dài vectơ $\vec{NA} + \vec{NB} + \vec{NC}$ đạt giá trị nhỏ nhất. Tính giá trị nhỏ nhất đó.
\end{enumerate}

\textbf{Bài 3. (1,0 điểm)} Một người đi bộ xuất phát từ vị trí $O$, đi thẳng $300\text{ m}$ theo hướng chính Đông đến vị trí $A$, sau đó đổi hướng đi thẳng thêm $500\text{ m}$ theo hướng chếch $60^\circ$ về phía Bắc so với hướng Đông để tới vị trí $B$ (như hình vẽ). Chọn hệ trục tọa độ $Oxy$ có gốc $O$ tại điểm xuất phát, tia $Ox$ trùng với hướng Đông và tia $Oy$ trùng với hướng Bắc (đơn vị trên mỗi trục tính bằng mét).
\par\noindent\begin{minipage}[t]{0.66\linewidth}
\begin{enumerate}[label=\alph*), leftmargin=0.6cm, itemsep=2pt]
    \item (0,5 điểm) Tìm tọa độ các vectơ $\vec{OA}$, $\vec{AB}$ và $\vec{OB}$ trong hệ trục tọa độ đã chọn.
    \item (0,5 điểm) Tính khoảng cách từ điểm xuất phát $O$ đến điểm đến $B$ và xác định góc hợp bởi hướng đi thẳng từ $O$ tới $B$ với hướng Đông (làm tròn kết quả góc đến hàng phần mười của độ).
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
  {\small\color{gray!75!black} Đề ôn tập Toán 10 — Chương IV. Vectơ — Đề số 5 (Mã đề 1046)}
\end{center}
\vspace{1pt}

\noindent\textbf{PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (20 câu)}
\vspace{1.5pt}

\begin{center}
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|}
\hline
\textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{7} & \textbf{8} & \textbf{9} & \textbf{10} \\ \hline
\textbf{A} & \textbf{C} & \textbf{B} & \textbf{D} & \textbf{A} & \textbf{D} & \textbf{B} & \textbf{C} & \textbf{A} & \textbf{B} \\ \hline
\hline
\textbf{11} & \textbf{12} & \textbf{13} & \textbf{14} & \textbf{15} & \textbf{16} & \textbf{17} & \textbf{18} & \textbf{19} & \textbf{20} \\ \hline
\textbf{D} & \textbf{C} & \textbf{B} & \textbf{D} & \textbf{A} & \textbf{C} & \textbf{B} & \textbf{D} & \textbf{C} & \textbf{A} \\ \hline
\end{tabular}
\end{center}

\vspace{1pt}
\noindent\begin{minipage}[t]{0.58\linewidth}
\textbf{PHẦN II. Câu trắc nghiệm đúng/sai}\\[1.5pt]
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|c|c|c|c|c|}
\hline
\textbf{Câu} & \textbf{a)} & \textbf{b)} & \textbf{c)} & \textbf{d)} \\ \hline
\textbf{1} & \textbf{Đ} & \textbf{S} & \textbf{S} & \textbf{Đ} \\ \hline
\textbf{2} & \textbf{S} & \textbf{Đ} & \textbf{Đ} & \textbf{S} \\ \hline
\textbf{3} & \textbf{Đ} & \textbf{Đ} & \textbf{S} & \textbf{S} \\ \hline
\textbf{4} & \textbf{S} & \textbf{S} & \textbf{Đ} & \textbf{Đ} \\ \hline
\end{tabular}
\end{minipage}\hfill
\begin{minipage}[t]{0.40\linewidth}
\textbf{PHẦN III. Trả lời ngắn}\\[1.5pt]
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|c|c|c|c|}
\hline
\textbf{Câu} & \textbf{Đáp số} & \textbf{Câu} & \textbf{Đáp số} \\ \hline
\textbf{1} & $12$   & \textbf{4} & $0{,}96$ \\ \hline
\textbf{2} & $6$    & \textbf{5} & $5$ \\ \hline
\textbf{3} & $5$    & \textbf{6} & $1500$ \\ \hline
\end{tabular}
\end{minipage}

\vspace{5pt}
\noindent\textbf{PHẦN IV. Đáp số tự luận:}\\[2pt]
- \textbf{Bài 1:} a) $\vec{IE} = \dfrac{1}{6}\vec{AB} - \dfrac{1}{3}\vec{AD}$; $\vec{IK} = \dfrac{1}{4}\vec{AB} - \dfrac{1}{2}\vec{AD}$. b) $\vec{IK} = \dfrac{3}{2}\vec{IE} \Rightarrow I, E, K$ thẳng hàng.\\
- \textbf{Bài 2:} a) $AB = AC = 2\sqrt{5}$, $\vec{AB}\cdot\vec{AC}=0$; $D(7; 4)$. b) $N\!\left(0; \dfrac{8}{3}\right)$, GTNN bằng $9$.\\
- \textbf{Bài 3:} a) $\vec{OA} = (300; 0)$, $\vec{AB} = (250; 250\sqrt{3})$, $\vec{OB} = (550; 250\sqrt{3})$. b) $OB = 700\text{ m}$; góc $\approx 38{,}2^\circ$.

\vspace{4pt}
\begin{center}
  {\large\bfseries\color{ink} HƯỚNG DẪN GIẢI CHI TIẾT}
\end{center}
\vspace{1pt}

\begin{multicols}{2}
\raggedcolumns
\small

\textbf{\color{accent}PHẦN I. TRẮC NGHIỆM}

\textbf{Câu 1.} Trên đường thẳng $BC$ có $3$ điểm $B, N, C$ tạo được $3\times 2 = 6$ vectơ khác $\vec{0}$ cùng phương với $\vec{BC}$. Đường trung bình $MP \parallel BC$ có $2$ vectơ $\vec{MP}, \vec{PM}$. Tổng cộng $6 + 2 = 8$ vectơ. Chọn \textbf{A}.

\textbf{Câu 2.} Hai vectơ $\vec{AD}$ và $\vec{CB}$ ngược hướng nên $\vec{AD} = -\vec{CB} \neq \vec{CB}$. Chọn \textbf{C}.

\textbf{Câu 3.} $\vec{AC} - \vec{BC} + \vec{BD} = (\vec{AC} + \vec{CB}) + \vec{BD} = \vec{AB} + \vec{BD} = \vec{AD}$. Chọn \textbf{B}.

\textbf{Câu 4.} $\vec{CB} + \vec{CD} = \vec{CA}$. Hình thoi $ABCD$ có $\widehat{BCD} = 60^\circ$ nên $\triangle BCD$ đều cạnh $a$, suy ra đường cao từ $C$ bằng $\dfrac{a\sqrt{3}}{2}$ và $CA = a\sqrt{3}$. Chọn \textbf{D}.

\textbf{Câu 5.} Gọi $M$ là trung điểm $BC$, ta có $|\vec{AB} + \vec{AC}| = 2AM$. Vì $\triangle ABC$ vuông tại $A$ nên trung tuyến $AM = \dfrac{BC}{2} = a \Rightarrow 2AM = 2a$. Chọn \textbf{A}.

\textbf{Câu 6.} Với $G$ là trọng tâm $\triangle ABC$, mọi điểm $M$ đều thỏa mãn $\vec{MA} + \vec{MB} + \vec{MC} = 3\vec{MG}$. Chọn \textbf{D}.

\textbf{Câu 7.} $2\vec{KA} + 3\vec{KB} = \vec{0} \Leftrightarrow 2\vec{KA} + 3(\vec{KA} + \vec{AB}) = \vec{0} \Leftrightarrow 5\vec{AK} = 3\vec{AB} \Leftrightarrow \vec{AK} = \dfrac{3}{5}\vec{AB}$. Chọn \textbf{B}.

\textbf{Câu 8.} Với trọng tâm $G$, $\vec{BG} = \dfrac{1}{3}(\vec{BA} + \vec{BC}) = \dfrac{1}{3}\vec{BA} + \dfrac{1}{3}\vec{BC}$. Chọn \textbf{C}.

\textbf{Câu 9.} $\vec{u} = (5; -1) \Rightarrow \vec{a} = (5; -1) - 2(-2; 3) = (9; -7)$. Chọn \textbf{A}.

\textbf{Câu 10.} $\vec{NM} = (x_M - x_N; y_M - y_N) = (-3 - 1; 5 - (-1)) = (-4; 6)$. Chọn \textbf{B}.

\textbf{Câu 11.} $x_I = \dfrac{-2 + 4}{2} = 1$; $y_I = \dfrac{3 - 5}{2} = -1 \Rightarrow I(1; -1)$. Chọn \textbf{D}.

\textbf{Câu 12.} $\vec{AB} = (m - 1; 4)$, $\vec{AC} = (-2; -4)$. Thẳng hàng $\Leftrightarrow (m - 1)(-4) - 4(-2) = 0 \Leftrightarrow m - 1 = 2 \Leftrightarrow m = 3$. Chọn \textbf{C}.

\textbf{Câu 13.} $\vec{a} \parallel \vec{b} \Leftrightarrow 4\cdot 3 - (-2)(m + 1) = 0 \Leftrightarrow 12 + 2m + 2 = 0 \Leftrightarrow m = -7$. Chọn \textbf{B}.

\textbf{Câu 14.} $(\vec{CA}, \vec{BC}) = 180^\circ - (\vec{CA}, \vec{CB}) = 180^\circ - 40^\circ = 140^\circ$. Chọn \textbf{D}.

\textbf{Câu 15.} $AH = a\sqrt{3}$, góc $\widehat{BAH} = 30^\circ$. Vậy $\vec{AB}\cdot\vec{AH} = 2a\cdot a\sqrt{3}\cdot\cos 30^\circ = 3a^2$. Chọn \textbf{A}.

\textbf{Câu 16.} $\vec{u} - \vec{v} = (1; -9) \Rightarrow \vec{u}\cdot(\vec{u} - \vec{v}) = 3\cdot 1 + (-5)(-9) = 3 + 45 = 48$. Chọn \textbf{C}.

\textbf{Câu 17.} $\vec{AB} = (-6; 8) \Rightarrow AB = \sqrt{(-6)^2 + 8^2} = 10$. Chọn \textbf{B}.

\textbf{Câu 18.} $\vec{x}\perp\vec{y} \Leftrightarrow m(m - 3) - 4 = 0 \Leftrightarrow m^2 - 3m - 4 = 0 \Leftrightarrow m \in \{-1; 4\}$. Tổng $m_1 + m_2 = 3$. Chọn \textbf{D}.

\textbf{Câu 19.} $\cos(\vec{a}, \vec{b}) = \dfrac{-1 + 3}{2\cdot 2} = \dfrac{1}{2} \Rightarrow (\vec{a}, \vec{b}) = 60^\circ$. Chọn \textbf{C}.

\textbf{Câu 20.} $A = F\cdot d\cdot \cos 60^\circ = 2000\cdot 50\cdot \dfrac{1}{2} = 50\,000\text{ J} = 50\text{ kJ}$. Chọn \textbf{A}.

\textbf{\color{accent}PHẦN II. ĐÚNG / SAI}

\textbf{Câu 1.}
a) $BC = \sqrt{6^2 + 8^2} = 10$ (\textbf{Đ}).
b) $|\vec{AB} + \vec{AC}| = 2AM = BC = 10 \neq 14$ (\textbf{S}).
c) $\vec{BA}\cdot\vec{BC} = BA\cdot BC\cdot\cos\widehat{B} = 6\cdot 10\cdot \dfrac{6}{10} = 36 \neq 48$ (\textbf{S}).
d) $|2\vec{AB} - \vec{AC}|^2 = 4AB^2 + AC^2 = 4(36) + 64 = 208 \Rightarrow |2\vec{AB} - \vec{AC}| = 4\sqrt{13}$ (\textbf{Đ}).

\textbf{Câu 2.}
a) $\vec{AI} = \vec{AD} + \vec{DI} = \dfrac{1}{2}\vec{AB} + \vec{AD}$ (\textbf{S}).
b) $\vec{AK} = \vec{AB} + \dfrac{1}{3}\vec{BD} = \vec{AB} + \dfrac{1}{3}(\vec{AD} - \vec{AB}) = \dfrac{2}{3}\vec{AB} + \dfrac{1}{3}\vec{AD}$ (\textbf{Đ}).
c) $\vec{IK} = \vec{AK} - \vec{AI} = \left(\dfrac{2}{3} - \dfrac{1}{2}\right)\vec{AB} + \left(\dfrac{1}{3} - 1\right)\vec{AD} = \dfrac{1}{6}\vec{AB} - \dfrac{2}{3}\vec{AD}$ (\textbf{Đ}).
d) $\dfrac{1/2}{2/3} \neq \dfrac{1}{1/3}$ nên $A, K, I$ không thẳng hàng (\textbf{S}).

\textbf{Câu 3.}
a) $\vec{AB} = (-3; -4) \Rightarrow AB = 5$ (\textbf{Đ}).
b) $M\left(\dfrac{1+4}{2}; \dfrac{5-3}{2}\right) = \left(\dfrac{5}{2}; 1\right)$ (\textbf{Đ}).
c) $\vec{BA} = (3; 4)$, $\vec{BC} = (6; -4) \Rightarrow \vec{BA}\cdot\vec{BC} = 18 - 16 = 2 \neq 0$ (\textbf{S}).
d) $\vec{AB} = \vec{DC} \Rightarrow D = C - \vec{AB} = (4 - (-3); -3 - (-4)) = (7; 1) \neq (7; 2)$ (\textbf{S}).

\textbf{Câu 4.}
a) $(\vec{AB}, \vec{BC}) = (\vec{DC}, \vec{BC}) = \widehat{BAD} = 60^\circ$ (\textbf{S}).
b) $\vec{AB}\cdot\vec{AD} = 2a\cdot 2a\cdot\cos 60^\circ = 2a^2$ (\textbf{S}).
c) $|\vec{AB} + \vec{AD}|^2 = 4a^2 + 4a^2 + 2(2a^2) = 12a^2 \Rightarrow |\vec{AB} + \vec{AD}| = 2a\sqrt{3}$ (\textbf{Đ}).
d) Hai đường chéo hình thoi vuông góc nên $\vec{AC}\cdot\vec{BD} = 0$ (\textbf{Đ}).

\textbf{\color{accent}PHẦN III. TRẢ LỜI NGẮN}

\textbf{Câu 1.} Gọi $M$ là trung điểm $BC$. $|\vec{AB} + \vec{AC}| = 2AM = 2\cdot \dfrac{4\sqrt{3}\cdot\sqrt{3}}{2} = \mathbf{12}$.

\textbf{Câu 2.} $\vec{AM} = \vec{AB} + \dfrac{1}{2}\vec{AD}$; $\vec{AN} = \dfrac{1}{3}\vec{AB} + \vec{AD} \Rightarrow \vec{MN} = -\dfrac{2}{3}\vec{AB} + \dfrac{1}{2}\vec{AD}$. Vậy $T = 4\left(\dfrac{1}{2}\right) - 6\left(-\dfrac{2}{3}\right) = 2 + 4 = \mathbf{6}$.

\textbf{Câu 3.} Từ $\vec{DA} + 2\vec{DB} + \vec{DC} = \vec{0} \Rightarrow D = \dfrac{A + 2B + C}{4} = \left(\dfrac{3 - 2 + 3}{4}; \dfrac{-1 + 4 + 5}{4}\right) = (1; 2) \Rightarrow T = 1 + 2(2) = \mathbf{5}$.

\textbf{Câu 4.} $\cos(\vec{a}, \vec{b}) = \dfrac{3\cdot 4 + 4\cdot 3}{5\cdot 5} = \dfrac{24}{25} = \mathbf{0{,}96}$.

\textbf{Câu 5.} $\vec{CA} = (1 - m; 2)$, $\vec{CB} = (6 - m; 2)$. $\vec{CA}\cdot\vec{CB} = 0 \Leftrightarrow (1 - m)(6 - m) + 4 = 0 \Leftrightarrow m^2 - 7m + 10 = 0 \Leftrightarrow m = 2$ (loại) hoặc $m = \mathbf{5}$.

\textbf{Câu 6.} $A = F\cdot d\cdot\cos 60^\circ = 120\cdot 25\cdot \dfrac{1}{2} = \mathbf{1500}\text{ J}$.

\textbf{\color{accent}PHẦN IV. TỰ LUẬN}

\textbf{Bài 1.}
a) Ta có $\vec{AI} = \dfrac{1}{2}\vec{AD}$, $\vec{AK} = \dfrac{1}{4}\vec{AB}$, và $\vec{AE} = \dfrac{1}{6}\vec{AC} = \dfrac{1}{6}\vec{AB} + \dfrac{1}{6}\vec{AD}$.\\
Suy ra $\vec{IE} = \vec{AE} - \vec{AI} = \dfrac{1}{6}\vec{AB} - \dfrac{1}{3}\vec{AD}$; $\vec{IK} = \vec{AK} - \vec{AI} = \dfrac{1}{4}\vec{AB} - \dfrac{1}{2}\vec{AD}$.\\
b) Nhận thấy $\vec{IK} = \dfrac{3}{2}\left(\dfrac{1}{6}\vec{AB} - \dfrac{1}{3}\vec{AD}\right) = \dfrac{3}{2}\vec{IE}$. Do hai vectơ $\vec{IK}$ và $\vec{IE}$ cùng phương nên ba điểm $I, E, K$ thẳng hàng.

\textbf{Bài 2.}
a) Ta có $\vec{AB} = (4; -2)$, $\vec{AC} = (2; 4) \Rightarrow \vec{AB}\cdot\vec{AC} = 4\cdot 2 + (-2)\cdot 4 = 0$ và $AB = AC = \sqrt{4^2 + (-2)^2} = 2\sqrt{5}$. Vậy $\triangle ABC$ vuông cân tại $A$.\\
Để $ABDC$ là hình vuông thì $\vec{CD} = \vec{AB} = (4; -2) \Rightarrow D = (3 + 4; 6 - 2) = (7; 4)$.\\
b) Gọi $G$ là trọng tâm $\triangle ABC$: $G\left(\dfrac{1 + 5 + 3}{3}; \dfrac{2 + 0 + 6}{3}\right) = G\left(3; \dfrac{8}{3}\right)$.\\
Ta có $|\vec{NA} + \vec{NB} + \vec{NC}| = |3\vec{NG}| = 3NG$. Do $N \in Oy$, $NG$ nhỏ nhất khi $N$ là hình chiếu vuông góc của $G$ lên $Oy$, tức $N\!\left(0; \dfrac{8}{3}\right)$. Giá trị nhỏ nhất bằng $3 \cdot 3 = 9$.

\textbf{Bài 3.}
a) $\vec{OA} = (300; 0)$.\\
$\vec{AB} = (500\cos 60^\circ; 500\sin 60^\circ) = (250; 250\sqrt{3})$.\\
$\vec{OB} = \vec{OA} + \vec{AB} = (550; 250\sqrt{3})$.\\
b) $OB = \sqrt{550^2 + (250\sqrt{3})^2} = \sqrt{302500 + 187500} = \sqrt{490000} = 700\text{ m}$.\\
Gọi $\alpha$ là góc hợp bởi $\vec{OB}$ với tia $Ox$ (hướng Đông): $\cos\alpha = \dfrac{550}{700} = \dfrac{11}{14} \Rightarrow \alpha \approx 38{,}2^\circ$.

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

    print("[3/4] Splitting into De_On_Tap_Vector_5_Exam.pdf and De_On_Tap_Vector_5_Ans.pdf...")
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

    print("\nBUILD COMPLETE FOR ĐỀ ÔN TẬP VECTƠ SỐ 5!")


if __name__ == "__main__":
    main()
