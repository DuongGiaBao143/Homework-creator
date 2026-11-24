#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Build pipeline for Grade 10 Review Exam: Chương IV. Vectơ — Đề số 4 (Mã đề 1045).
Generates standalone student exam PDF (3 pages) and teacher answer key PDF (2 pages),
audits pagination, and exports copies to Grade 10 teaching folders.
"""

import re
import shutil
import subprocess
from pathlib import Path
import pymupdf

OUT_DIR = Path(r"d:\Tao_De\Lớp 10\Output\De_On_Tap_Vector_4")
TEX_PATH = OUT_DIR / "De_On_Tap_Vector_4.tex"
FULL_PDF = OUT_DIR / "De_On_Tap_Vector_4.pdf"
EXAM_PDF = OUT_DIR / "De_On_Tap_Vector_4_Exam.pdf"
ANS_PDF = OUT_DIR / "De_On_Tap_Vector_4_Ans.pdf"

EXPORT_TARGETS = [
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\Vector\De_On_Tap_Vector_4.pdf"), "exam"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\Vector\Ans\De_On_Tap_Vector_4_Ans.pdf"), "ans"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương IV\Đề ôn tập Chương 4 - Vectơ (Đề 4).pdf"), "exam"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương IV\Ans\Đề ôn tập Chương 4 - Vectơ (Đề 4 - Đáp án).pdf"), "ans"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương IV\Ans\Đề ôn tập Chương 4 - Vectơ (Đề 4 - có đáp án).pdf"), "full"),
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
  \lfoot{\small\textit{\color{gray!60!black}Đáp án Đề ôn tập Chương IV. Vectơ (Đề số 4) — Toán 10 KNTT}}
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
  \coordinate (D) at (0,0);
  \coordinate (A) at (0,2);
  \coordinate (B) at (2,2);
  \coordinate (C) at (4,0);
  \coordinate (M) at (2,0);
  \draw[thick, ink] (D) -- (A) -- (B) -- (C) -- cycle;
  \draw[dashed, gray!75] (B) -- (M);
  \draw[gray!75] (0,0.28) -- (0.28,0.28) -- (0.28,0);
  \draw[gray!75] (0,1.72) -- (0.28,1.72) -- (0.28,2);
  \node[above left, font=\scriptsize] at (A) {$A$};
  \node[above right, font=\scriptsize] at (B) {$B$};
  \node[below right, font=\scriptsize] at (C) {$C$};
  \node[below left, font=\scriptsize] at (D) {$D$};
  \node[below, font=\scriptsize] at (M) {$M$};
  \fill[ink] (M) circle (1.8pt);
\end{tikzpicture}"""

TIKZ_P3_Q6 = r"""\begin{tikzpicture}[scale=0.45, >=Stealth]
  \coordinate (O) at (0,0);
  \coordinate (F1) at (2.5,0);
  \coordinate (F2) at (-2.0, 3.464);
  \coordinate (F) at (0.5, 3.464);
  \draw[->, very thick, accent] (O) -- (F1) node[below right, font=\scriptsize] {$\vec{F}_1$};
  \draw[->, very thick, accent] (O) -- (F2) node[left, font=\scriptsize] {$\vec{F}_2$};
  \draw[dashed, gray!65] (F1) -- (F) -- (F2);
  \draw[->, line width=1.1pt, ink] (O) -- (F) node[above right, font=\scriptsize] {$\vec{F}$};
  \pic[draw, angle radius=0.4cm, "$120^\circ$", angle eccentricity=1.65, font=\tiny] {angle = F1--O--F2};
  \node[below left, font=\scriptsize] at (O) {$O$};
\end{tikzpicture}"""

TIKZ_P4_B3 = r"""\begin{tikzpicture}[scale=0.58, >=Stealth]
  \fill[gray!20] (-2.3,2.2) rectangle (2.3,2.42);
  \draw[thick] (-2.3,2.2) -- (2.3,2.2);
  \coordinate (A) at (-1.9, 2.2);
  \coordinate (B) at (1.9, 2.2);
  \coordinate (O) at (0, 1.10);
  \draw[thick, ink] (A) -- (O) node[midway, below left, font=\tiny] {$T_1$};
  \draw[thick, ink] (B) -- (O) node[midway, below right, font=\tiny] {$T_2$};
  \draw[->, very thick, accent] (O) -- (0, -0.25) node[right, font=\tiny] {$\vec{P}$};
  \fill[ink] (O) circle (1.8pt);
  \node[below left, font=\tiny] at (-0.06, 1.05) {$O$};
  \fill[accent!80!black] (-0.25, -0.25) rectangle (0.25, -0.65);
  \node[font=\tiny, white] at (0, -0.45) {$P$};
  \pic[draw, angle radius=0.28cm, "$120^\circ$", angle eccentricity=1.55, font=\tiny] {angle = B--O--A};
  \node[below, font=\tiny] at (-1.15, 2.2) {$30^\circ$};
  \node[below, font=\tiny] at (1.15, 2.2) {$30^\circ$};
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
    \textbf{ĐỀ ÔN TẬP SỐ 4}
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
        \textbf{1045}
    \end{minipage}}
\end{minipage}
\vspace{0.05cm}

\parttitle{PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn}
\textit{Thí sinh trả lời từ câu 1 đến câu 20. Mỗi câu hỏi thí sinh chỉ chọn một phương án.}
\begin{enumerate}
\item Cho tứ giác lồi $ABCD$. Có bao nhiêu vectơ khác vectơ-không có điểm đầu và điểm cuối là các đỉnh của tứ giác đã cho?
\four{$6$.}{$8$.}{$12$.}{$16$.}

\item Cho lục giác đều $ABCDEF$ tâm $O$. Vectơ nào sau đây \textbf{ngược hướng} với vectơ $\vec{OA}$?
\four{$\vec{EF}$.}{$\vec{DO}$.}{$\vec{CB}$.}{$\vec{OD}$.}

\item Cho năm điểm bất kì $A, B, C, D, E$. Tổng vectơ $\vec{AB} - \vec{CB} + \vec{CD} - \vec{ED}$ bằng
\four{$\vec{AE}$.}{$\vec{EA}$.}{$\vec{AD}$.}{$\vec{0}$.}

\item Cho hình chữ nhật $ABCD$ có $AB = 6$, $AD = 8$. Độ dài của vectơ $\vec{u} = \vec{AB} - \vec{AD}$ bằng
\four{$14$.}{$10$.}{$2$.}{$2\sqrt{7}$.}

\item Cho tam giác đều $ABC$ có cạnh bằng $2a$. Độ dài của vectơ $\vec{v} = \vec{AB} + \vec{AC}$ bằng
\four{$a\sqrt{3}$.}{$4a$.}{$3a$.}{$2a\sqrt{3}$.}

\item Cho hình bình hành $ABCD$ tâm $O$. Với điểm $M$ bất kì, khẳng định nào sau đây đúng?
\two{$\vec{MA} + \vec{MB} + \vec{MC} + \vec{MD} = 4\vec{MO}$.}{$\vec{MA} + \vec{MC} = \vec{MO}$.}{$\vec{MB} + \vec{MD} = 4\vec{MO}$.}{$\vec{OA} + \vec{OB} = \vec{OC} + \vec{OD}$.}

\item Cho tam giác $ABC$ có $M$ là trung điểm của cạnh $BC$. Đẳng thức vectơ nào sau đây đúng?
\two{$\vec{AM} = \vec{AB} + \vec{AC}$.}{$\vec{AM} = \dfrac{1}{2}\vec{AB} - \dfrac{1}{2}\vec{AC}$.}{$\vec{AM} = \dfrac{1}{2}\vec{AB} + \dfrac{1}{2}\vec{AC}$.}{$\vec{AM} = 2\vec{AB} + 2\vec{AC}$.}

\item Cho hai vectơ $\vec{a}, \vec{b}$ đều khác vectơ-không và $\vec{a} = -3\vec{b}$. Phát biểu nào sau đây đúng?
\two{$\vec{a}$ và $\vec{b}$ cùng hướng và $|\vec{a}| = 3|\vec{b}|$.}{$\vec{a}$ và $\vec{b}$ ngược hướng và $|\vec{a}| = 3|\vec{b}|$.}{$\vec{a}$ và $\vec{b}$ ngược hướng và $|\vec{b}| = 3|\vec{a}|$.}{$\vec{a}$ và $\vec{b}$ không cùng phương.}

\item Trong mặt phẳng tọa độ $Oxy$, cho $\vec{u} = (2; -5)$ và $\vec{v} = (-1; 3)$. Tọa độ của vectơ $\vec{w} = 3\vec{u} + 2\vec{v}$ là
\four{$(8; -21)$.}{$(1; -2)$.}{$(4; -21)$.}{$(4; -9)$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A(3; -2)$ và $B(-1; 6)$. Tọa độ trung điểm $I$ của đoạn thẳng $AB$ là
\four{$I(1; 2)$.}{$I(2; 4)$.}{$I(-2; 4)$.}{$I(2; -4)$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hình bình hành $ABCD$ có $A(1; 1)$, $B(4; 3)$ và $D(2; -2)$. Tọa độ đỉnh $C$ là
\four{$C(3; 0)$.}{$C(5; 4)$.}{$C(5; 0)$.}{$C(-1; -4)$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$ có $A(2; 5)$, $B(-1; 1)$ và trọng tâm $G(1; 2)$. Tọa độ đỉnh $C$ là
\four{$C(0; 4)$.}{$C(2; 4)$.}{$C(1; 0)$.}{$C(2; 0)$.}
\pagebreak

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{a} = (3; m - 1)$ và $\vec{b} = (-6; 4)$. Giá trị của $m$ để $\vec{a}$ và $\vec{b}$ cùng phương là
\four{$m = 3$.}{$m = -1$.}{$m = 1$.}{$m = -3$.}

\item Cho tam giác $ABC$ vuông tại $A$ có góc $\widehat{B} = 30^\circ$. Góc giữa hai vectơ $\vec{BA}$ và $\vec{CB}$ bằng
\four{$150^\circ$.}{$30^\circ$.}{$60^\circ$.}{$120^\circ$.}

\item Cho hình vuông $ABCD$ cạnh $a$. Tích vô hướng $\vec{AB} \cdot \vec{BD}$ bằng
\four{$a^2$.}{$a^2\sqrt{2}$.}{$-a^2$.}{$-a^2\sqrt{2}$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{u} = (-2; 4)$ và $\vec{v} = (5; 3)$. Giá trị của tích vô hướng $\vec{u} \cdot \vec{v}$ bằng
\four{$-22$.}{$2$.}{$22$.}{$-2$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho điểm $M(-5; 12)$. Khoảng cách từ gốc tọa độ $O$ đến điểm $M$ bằng
\four{$17$.}{$7$.}{$\sqrt{119}$.}{$13$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{x} = (m; -2)$ và $\vec{y} = (3; m + 5)$. Giá trị của $m$ để $\vec{x} \perp \vec{y}$ là
\four{$m = 10$.}{$m = -10$.}{$m = 2$.}{$m = -2$.}

\item Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{a} = (1; 0)$ và $\vec{b} = (-1; \sqrt{3})$. Góc giữa hai vectơ $\vec{a}$ và $\vec{b}$ bằng
\four{$60^\circ$.}{$120^\circ$.}{$150^\circ$.}{$30^\circ$.}

\item Một công nhân dùng một lực $\vec{F}$ không đổi có độ lớn $60\text{ N}$ kéo một thùng hàng trượt đi $8\text{ m}$ trên sàn ngang theo phương hợp với hướng của lực kéo một góc $45^\circ$. Công sinh bởi lực $\vec{F}$ bằng
\four{$480\text{ J}$.}{$240\text{ J}$.}{$240\sqrt{2}\text{ J}$.}{$240\sqrt{3}\text{ J}$.}
\end{enumerate}

\vspace{3pt}
\parttitle{PHẦN II. Câu trắc nghiệm đúng sai}
\textit{Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.}
\begin{enumerate}
\item Cho hình thang vuông $ABCD$ vuông tại $A$ và $D$, có $AB = AD = a$, $CD = 2a$. Gọi $M$ là trung điểm của cạnh $CD$ (như hình vẽ bên).
\par\noindent\begin{minipage}[t]{0.72\linewidth}
\begin{enumerate}
    \item Hai vectơ $\vec{AB}$ và $\vec{CD}$ cùng hướng.
    \item Tứ giác $ABMD$ là hình vuông cạnh $a$.
    \item Độ dài của vectơ $\vec{AC} - \vec{AB}$ bằng $2a$.
    \item Tích vô hướng $\vec{AB} \cdot \vec{AC} = 2a^2$.
\end{enumerate}
\end{minipage}\hfill
\begin{minipage}[t]{0.26\linewidth}\raggedleft\vspace{-6pt}
""" + TIKZ_P2_Q1 + r"""
\end{minipage}

\item Cho tam giác $ABC$ có trọng tâm $G$, $M$ là trung điểm của cạnh $BC$, và $E$ là điểm trên cạnh $AB$ sao cho $AE = \dfrac{1}{3}AB$.
\begin{enumerate}
    \item $\vec{CE} = \dfrac{1}{3}\vec{AB} - \vec{AC}$.
    \item $\vec{MG} = \dfrac{1}{6}\vec{AB} + \dfrac{1}{6}\vec{AC}$.
    \item $\vec{EG} = \dfrac{1}{3}\vec{AC}$.
    \item Hai đường thẳng $EG$ và $BC$ song song với nhau.
\end{enumerate}

\item Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A(0; -2)$, $B(3; 2)$ và $C(7; -1)$.
\begin{enumerate}
    \item Tọa độ của vectơ $\vec{BC} = (-4; 3)$.
    \item Tam giác $ABC$ là tam giác vuông cân tại $B$.
    \item Diện tích của tam giác $ABC$ bằng $\dfrac{25}{2}$.
    \item Điểm $D$ để tứ giác $ABCD$ là hình vuông có tọa độ là $D(4; -6)$.
\end{enumerate}

\item Cho tam giác $ABC$ có $AB = 3$, $AC = 4$ và góc $\widehat{BAC} = 120^\circ$.
\begin{enumerate}
    \item Tích vô hướng $\vec{AB} \cdot \vec{AC} = -6$.
    \item Độ dài cạnh $BC$ bằng $5$.
    \item Độ dài của vectơ $\vec{u} = \vec{AB} + \vec{AC}$ bằng $5$.
    \item Độ dài của vectơ $\vec{v} = 2\vec{AB} - \vec{AC}$ bằng $2\sqrt{19}$.
\end{enumerate}
\end{enumerate}

\pagebreak
\parttitle{PHẦN III. Câu trắc nghiệm trả lời ngắn}
\textit{Thí sinh trả lời từ câu 1 đến câu 6. Mỗi câu thí sinh điền kết quả vào ô tương ứng.}
\begin{enumerate}
\item Cho hình thoi $ABCD$ có cạnh bằng $10$ và góc $\widehat{ABC} = 60^\circ$. Tính độ dài của vectơ $\vec{u} = \vec{AB} + \vec{AD}$. \answerbox

\item Cho tam giác $ABC$ có trọng tâm $G$, $M$ là điểm trên đoạn thẳng $BC$ sao cho $MB = 3MC$. Biết $\vec{GM} = x\vec{AB} + y\vec{AC}$ với $x, y \in \mathbb{R}$. Tính giá trị biểu thức $P = 12y - 12x$. \answerbox

\item Trong mặt phẳng tọa độ $Oxy$, cho $A(2; -1)$, $B(-1; 3)$ và $C(4; 5)$. Tìm tung độ của đỉnh $D$ sao cho tứ giác $ABCD$ là hình bình hành. \answerbox

\item Trong mặt phẳng $Oxy$, cho $A(1; 1)$, $B(4; 5)$ và $C(5; -2)$. Tính giá trị biểu thức $\vec{AB} \cdot \vec{AC} + |\vec{BC}|^2$. \answerbox

\item Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A(-1; 2)$ và $B(5; 4)$. Điểm $M(x_M; 0)$ nằm trên trục $Ox$ sao cho góc $\widehat{AMB} = 90^\circ$ (với $x_M > 2$). Tính giá trị của $x_M$.\answerbox

\item \begin{minipage}[t]{0.70\linewidth}
Một vật nặng chịu tác dụng đồng thời của hai lực kéo $\vec{F}_1$ và $\vec{F}_2$ cùng đặt tại điểm $O$ và hợp với nhau một góc $120^\circ$ (như hình vẽ bên). Biết độ lớn hai lực lần lượt là $|\vec{F}_1| = 50\text{ N}$ và $|\vec{F}_2| = 80\text{ N}$. Tính độ lớn của hợp lực $\vec{F} = \vec{F}_1 + \vec{F}_2$ (đơn vị: N).\answerbox
\end{minipage}\hfill
\begin{minipage}[t]{0.28\linewidth}\raggedleft\vspace{-6pt}
""" + TIKZ_P3_Q6 + r"""
\end{minipage}
\end{enumerate}

\vspace{3pt}
\parttitle{PHẦN IV. Tự luận}
\textit{Thí sinh trình bày bài làm và các bước suy luận cho các bài toán sau:}

\vspace{4pt}
\textbf{Bài 1 (1,0 điểm).} Cho tam giác $ABC$. Gọi $M$ là trung điểm của cạnh $AB$, $N$ là điểm trên cạnh $BC$ sao cho $NB = 2NC$, và $P$ là điểm trên đường thẳng $AC$ sao cho $C$ là trung điểm của đoạn thẳng $AP$.
\begin{enumerate}[label=\alph*), leftmargin=0.6cm, itemsep=2pt]
    \item (0,5 điểm) Hãy phân tích các vectơ $\vec{MN}$ và $\vec{MP}$ theo hai vectơ $\vec{AB}$ và $\vec{AC}$.
    \item (0,5 điểm) Từ kết quả câu a), hãy chứng minh rằng ba điểm $M, N, P$ thẳng hàng.
\end{enumerate}

\vspace{6pt}
\textbf{Bài 2 (1,0 điểm).} Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$ có ba đỉnh $A(1; 4)$, $B(-2; 0)$ và $C(6; 4)$.
\begin{enumerate}[label=\alph*), leftmargin=0.6cm, itemsep=2pt]
    \item (0,5 điểm) Chứng minh tam giác $ABC$ cân tại $A$ và tìm tọa độ chân đường cao $H$ kẻ từ $A$ xuống $BC$.
    \item (0,5 điểm) Tìm tọa độ điểm $M$ thuộc trục hoành $Ox$ sao cho $|\vec{MA} + \vec{MB} + \vec{MC}|$ đạt giá trị nhỏ nhất, và tính giá trị nhỏ nhất đó.
\end{enumerate}

\vspace{6pt}
\textbf{Bài 3 (1,0 điểm).} Một chiếc đèn chùm nặng $P = 120\text{ N}$ được treo cân bằng ở chính giữa hai dây cáp đối xứng $OA, OB$ gắn vào trần nhà nằm ngang. Biết hai dây hợp với nhau một góc $120^\circ$ (mỗi dây hợp với trần nhà góc $30^\circ$, như hình vẽ bên).
\par\noindent\begin{minipage}[t]{0.68\linewidth}
\begin{enumerate}[label=\alph*), leftmargin=0.6cm, itemsep=2pt]
    \item (0,5 điểm) Viết phương trình vectơ biểu diễn trạng thái cân bằng tại điểm treo $O$ và tính độ lớn lực căng $T$ của mỗi dây cáp $OA, OB$.
    \item (0,5 điểm) Nếu thay đổi chiều dài dây sao cho hai dây vuông góc với nhau tại $O$ (mỗi dây hợp với trần nhà góc $45^\circ$), tính độ lớn lực căng $T'$ của mỗi dây lúc này (làm tròn đến hàng phần mười) và nhận xét về sự thay đổi lực căng dây.
\end{enumerate}
\end{minipage}\hfill
\begin{minipage}[t]{0.30\linewidth}\raggedleft\vspace{-12pt}
""" + TIKZ_P4_B3 + r"""
\end{minipage}
""")

    # ==================== ĐÁP ÁN & HƯỚNG DẪN GIẢI ====================
    parts.append(r"""\newpage
\pagestyle{dapan}
\setcounter{page}{1}

\begin{center}
  {\Large\bfseries\color{ink} BẢNG ĐÁP ÁN TỔNG HỢP}\\[2pt]
  {\small\color{gray!75!black} Đề ôn tập Toán 10 — Chương IV. Vectơ — Đề số 4 (Mã đề 1045)}
\end{center}
\vspace{1pt}

\noindent\textbf{PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (20 câu)}
\vspace{1.5pt}

\begin{center}
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|C{0.95cm}|}
\hline
\textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{7} & \textbf{8} & \textbf{9} & \textbf{10} \\ \hline
\textbf{C} & \textbf{D} & \textbf{A} & \textbf{B} & \textbf{D} & \textbf{A} & \textbf{C} & \textbf{B} & \textbf{D} & \textbf{A} \\ \hline
\hline
\textbf{11} & \textbf{12} & \textbf{13} & \textbf{14} & \textbf{15} & \textbf{16} & \textbf{17} & \textbf{18} & \textbf{19} & \textbf{20} \\ \hline
\textbf{C} & \textbf{D} & \textbf{B} & \textbf{A} & \textbf{C} & \textbf{B} & \textbf{D} & \textbf{A} & \textbf{B} & \textbf{C} \\ \hline
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
\textbf{3} & \textbf{S} & \textbf{Đ} & \textbf{Đ} & \textbf{S} \\ \hline
\textbf{4} & \textbf{Đ} & \textbf{S} & \textbf{S} & \textbf{Đ} \\ \hline
\end{tabular}
\end{minipage}\hfill
\begin{minipage}[t]{0.40\linewidth}
\textbf{PHẦN III. Trả lời ngắn}\\[1.5pt]
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|c|c|c|c|}
\hline
\textbf{Câu} & \textbf{Đáp số} & \textbf{Câu} & \textbf{Đáp số} \\ \hline
\textbf{1} & $10$ & \textbf{4} & $50$ \\ \hline
\textbf{2} & $6$  & \textbf{5} & $3$ \\ \hline
\textbf{3} & $1$  & \textbf{6} & $70$ \\ \hline
\end{tabular}
\end{minipage}

\vspace{5pt}
\noindent\textbf{PHẦN IV. Đáp số tự luận:}\\[2pt]
- \textbf{Bài 1:} a) $\vec{MN} = -\dfrac{1}{6}\vec{AB} + \dfrac{2}{3}\vec{AC}$; $\vec{MP} = -\dfrac{1}{2}\vec{AB} + 2\vec{AC}$. b) $\vec{MP} = 3\vec{MN} \Rightarrow M, N, P$ thẳng hàng.\\
- \textbf{Bài 2:} a) $AB = AC = 5$; $H(2; 2)$. b) $M\left(\dfrac{5}{3}; 0\right)$, GTNN bằng $8$.\\
- \textbf{Bài 3:} a) $\vec{T}_1 + \vec{T}_2 + \vec{P} = \vec{0}$; $T = 120\text{ N}$. b) $T' = 60\sqrt{2} \approx 84{,}9\text{ N}$ (lực căng giảm khi góc giữa hai dây giảm).

\vspace{4pt}
\begin{center}
  {\large\bfseries\color{ink} HƯỚNG DẪN GIẢI CHI TIẾT}
\end{center}
\vspace{1pt}

\begin{multicols}{2}
\raggedcolumns
\small

\textbf{\color{accent}PHẦN I. TRẮC NGHIỆM}

\textbf{Câu 1.} Tứ giác có $4$ đỉnh. Số vectơ khác $\vec{0}$: $A_4^2 = 4 \times 3 = 12$. Chọn \textbf{C}.

\textbf{Câu 2.} Trong lục giác đều $ABCDEF$ tâm $O$, hai điểm $A, D$ đối xứng qua tâm $O$, nên $\vec{OD}$ cùng phương nhưng ngược chiều với $\vec{OA}$. Chọn \textbf{D}.

\textbf{Câu 3.} $\vec{AB} - \vec{CB} + \vec{CD} - \vec{ED} = (\vec{AB} + \vec{BC}) + (\vec{CD} + \vec{DE}) = \vec{AC} + \vec{CE} = \vec{AE}$. Chọn \textbf{A}.

\textbf{Câu 4.} $\vec{u} = \vec{AB} - \vec{AD} = \vec{DB} \Rightarrow |\vec{u}| = BD = \sqrt{6^2 + 8^2} = 10$. Chọn \textbf{B}.

\textbf{Câu 5.} Gọi $M$ là trung điểm $BC$, ta có $\vec{v} = 2\vec{AM}$. Tam giác đều cạnh $2a$ có đường cao $AM = \dfrac{2a\sqrt{3}}{2} = a\sqrt{3} \Rightarrow |\vec{v}| = 2a\sqrt{3}$. Chọn \textbf{D}.

\textbf{Câu 6.} $O$ là trung điểm $AC$ và $BD$ nên $\vec{MA} + \vec{MC} = 2\vec{MO}$ và $\vec{MB} + \vec{MD} = 2\vec{MO}$. Cộng lại được $4\vec{MO}$. Chọn \textbf{A}.

\textbf{Câu 7.} $M$ là trung điểm $BC \Rightarrow \vec{AM} = \dfrac{1}{2}\vec{AB} + \dfrac{1}{2}\vec{AC}$. Chọn \textbf{C}.

\textbf{Câu 8.} Với $k = -3 < 0$, vectơ $\vec{a} = -3\vec{b}$ ngược hướng với $\vec{b}$ và $|\vec{a}| = |-3||\vec{b}| = 3|\vec{b}|$. Chọn \textbf{B}.

\textbf{Câu 9.} $\vec{w} = 3(2; -5) + 2(-1; 3) = (6 - 2; -15 + 6) = (4; -9)$. Chọn \textbf{D}.

\textbf{Câu 10.} $x_I = \dfrac{3 + (-1)}{2} = 1$; $y_I = \dfrac{-2 + 6}{2} = 2 \Rightarrow I(1; 2)$. Chọn \textbf{A}.

\textbf{Câu 11.} $ABCD$ là hình bình hành $\Leftrightarrow \vec{DC} = \vec{AB} = (3; 2) \Rightarrow C = (2 + 3; -2 + 2) = (5; 0)$. Chọn \textbf{C}.

\textbf{Câu 12.} $x_C = 3x_G - x_A - x_B = 3 - 2 + 1 = 2$; $y_C = 3y_G - y_A - y_B = 6 - 5 - 1 = 0 \Rightarrow C(2; 0)$. Chọn \textbf{D}.

\textbf{Câu 13.} Hai vectơ cùng phương $\Leftrightarrow 3(4) - (-6)(m - 1) = 0 \Leftrightarrow 12 + 6m - 6 = 0 \Leftrightarrow m = -1$. Chọn \textbf{B}.

\textbf{Câu 14.} Góc $(\vec{BA}, \vec{BC}) = \widehat{B} = 30^\circ \Rightarrow (\vec{BA}, \vec{CB}) = 180^\circ - 30^\circ = 150^\circ$. Chọn \textbf{A}.

\textbf{Câu 15.} $\vec{AB} \cdot \vec{BD} = a \cdot a\sqrt{2} \cdot \cos 135^\circ = -a^2$. Chọn \textbf{C}.

\textbf{Câu 16.} $\vec{u} \cdot \vec{v} = (-2)(5) + 4(3) = -10 + 12 = 2$. Chọn \textbf{B}.

\textbf{Câu 17.} $OM = \sqrt{(-5)^2 + 12^2} = \sqrt{169} = 13$. Chọn \textbf{D}.

\textbf{Câu 18.} $\vec{x} \perp \vec{y} \Leftrightarrow 3m - 2(m + 5) = 0 \Leftrightarrow m - 10 = 0 \Leftrightarrow m = 10$. Chọn \textbf{A}.

\textbf{Câu 19.} $\cos(\vec{a}, \vec{b}) = \dfrac{1(-1) + 0(\sqrt{3})}{1 \cdot 2} = -\dfrac{1}{2} \Rightarrow (\vec{a}, \vec{b}) = 120^\circ$. Chọn \textbf{B}.

\textbf{Câu 20.} $A = 60 \cdot 8 \cdot \cos 45^\circ = 480 \cdot \dfrac{\sqrt{2}}{2} = 240\sqrt{2}\text{ J}$. Chọn \textbf{C}.

\columnbreak

\textbf{\color{accent}PHẦN II. ĐÚNG / SAI}

\textbf{Câu 1.}
a) $\vec{AB}$ cùng hướng $\vec{DC}$ nên ngược hướng với $\vec{CD} \Rightarrow$ \textbf{Sai}.\\
b) $AB \parallel MD$, $AB = MD = a$, $\widehat{A} = \widehat{D} = 90^\circ$ và $AB = AD = a \Rightarrow ABMD$ là hình vuông cạnh $a \Rightarrow$ \textbf{Đúng}.\\
c) $\vec{AC} - \vec{AB} = \vec{BC}$. Trong $\triangle BMC$ vuông tại $M$ ($BM = MC = a$), $BC = a\sqrt{2} \ne 2a \Rightarrow$ \textbf{Sai}.\\
d) $\vec{AB} \cdot \vec{AC} = \vec{AB} \cdot (\vec{AD} + \vec{DC}) = 0 + a \cdot 2a = 2a^2 \Rightarrow$ \textbf{Đúng}.

\textbf{Câu 2.}
a) $\vec{CE} = \vec{AE} - \vec{AC} = \dfrac{1}{3}\vec{AB} - \vec{AC} \Rightarrow$ \textbf{Đúng}.\\
b) $\vec{MG} = \vec{AG} - \vec{AM} = \dfrac{1}{3}(\vec{AB}+\vec{AC}) - \dfrac{1}{2}(\vec{AB}+\vec{AC}) = -\dfrac{1}{6}\vec{AB} - \dfrac{1}{6}\vec{AC} \Rightarrow$ \textbf{Sai}.\\
c) $\vec{EG} = \vec{AG} - \vec{AE} = \left(\dfrac{1}{3}\vec{AB} + \dfrac{1}{3}\vec{AC}\right) - \dfrac{1}{3}\vec{AB} = \dfrac{1}{3}\vec{AC} \Rightarrow$ \textbf{Đúng}.\\
d) Vì $\vec{EG} = \dfrac{1}{3}\vec{AC}$ nên $EG \parallel AC$, không song song với $BC \Rightarrow$ \textbf{Sai}.

\textbf{Câu 3.}
a) $\vec{BC} = (7 - 3; -1 - 2) = (4; -3) \ne (-4; 3) \Rightarrow$ \textbf{Sai}.\\
b) $\vec{BA} = (-3; -4)$, $\vec{BC} = (4; -3) \Rightarrow \vec{BA}\cdot\vec{BC} = -12 + 12 = 0$ và $BA = BC = 5 \Rightarrow \triangle ABC$ vuông cân tại $B \Rightarrow$ \textbf{Đúng}.\\
c) $S_{\triangle ABC} = \dfrac{1}{2} BA \cdot BC = \dfrac{1}{2} \cdot 5 \cdot 5 = \dfrac{25}{2} \Rightarrow$ \textbf{Đúng}.\\
d) $ABCD$ là hình vuông $\Leftrightarrow \vec{AD} = \vec{BC} = (4; -3) \Rightarrow D = (4; -5) \ne (4; -6) \Rightarrow$ \textbf{Sai}.

\textbf{Câu 4.}
a) $\vec{AB} \cdot \vec{AC} = 3 \cdot 4 \cdot \cos 120^\circ = 12 \cdot \left(-\dfrac{1}{2}\right) = -6 \Rightarrow$ \textbf{Đúng}.\\
b) $BC^2 = AB^2 + AC^2 - 2\vec{AB}\cdot\vec{AC} = 9 + 16 - 2(-6) = 37 \Rightarrow BC = \sqrt{37} \ne 5 \Rightarrow$ \textbf{Sai}.\\
c) $|\vec{u}|^2 = AB^2 + AC^2 + 2\vec{AB}\cdot\vec{AC} = 9 + 16 - 12 = 13 \Rightarrow |\vec{u}| = \sqrt{13} \ne 5 \Rightarrow$ \textbf{Sai}.\\
d) $|\vec{v}|^2 = 4AB^2 + AC^2 - 4\vec{AB}\cdot\vec{AC} = 36 + 16 + 24 = 76 \Rightarrow |\vec{v}| = \sqrt{76} = 2\sqrt{19} \Rightarrow$ \textbf{Đúng}.

\textbf{\color{accent}PHẦN III. TRẢ LỜI NGẮN}

\textbf{Câu 1.} Hình thoi $ABCD$ có $\widehat{ABC} = 60^\circ \Rightarrow \widehat{BAD} = 120^\circ$. $|\vec{u}|^2 = 10^2 + 10^2 + 2\cdot 10\cdot 10\cos 120^\circ = 100 \Rightarrow |\vec{u}| = \mathbf{10}$.

\textbf{Câu 2.} $\vec{MB} = -3\vec{MC} \Rightarrow \vec{AM} = \dfrac{1}{4}\vec{AB} + \dfrac{3}{4}\vec{AC}$. Do đó $\vec{GM} = \vec{AM} - \vec{AG} = -\dfrac{1}{12}\vec{AB} + \dfrac{5}{12}\vec{AC} \Rightarrow P = 12\left(\dfrac{5}{12}\right) - 12\left(-\dfrac{1}{12}\right) = \mathbf{6}$.

\textbf{Câu 3.} $\vec{AD} = \vec{BC} = (5; 2) \Rightarrow y_D = y_A + 2 = -1 + 2 = \mathbf{1}$.

\textbf{Câu 4.} $\vec{AB} = (3; 4)$, $\vec{AC} = (4; -3)$, $\vec{BC} = (1; -7)$. Ta có $\vec{AB}\cdot\vec{AC} + |\vec{BC}|^2 = (12 - 12) + (1 + 49) = \mathbf{50}$.

\textbf{Câu 5.} $\vec{MA} = (-1 - x_M; 2)$, $\vec{MB} = (5 - x_M; 4)$. $\vec{MA}\cdot\vec{MB} = 0 \Leftrightarrow (x_M + 1)(x_M - 5) + 8 = 0 \Leftrightarrow x_M^2 - 4x_M + 3 = 0 \Leftrightarrow x_M = 1$ (loại) hoặc $x_M = \mathbf{3}$ (nhận).

\textbf{Câu 6.} $|\vec{F}|^2 = 50^2 + 80^2 + 2\cdot 50\cdot 80\cos 120^\circ = 2500 + 6400 - 4000 = 4900 \Rightarrow |\vec{F}| = \mathbf{70}\text{ N}$.

\textbf{\color{accent}PHẦN IV. TỰ LUẬN}

\textbf{Bài 1.}
a) Ta có $\vec{AM} = \dfrac{1}{2}\vec{AB}$. Do $NB = 2NC \Rightarrow \vec{NB} = -2\vec{NC} \Rightarrow \vec{AN} = \dfrac{1}{3}\vec{AB} + \dfrac{2}{3}\vec{AC}$.\\
Suy ra $\vec{MN} = \vec{AN} - \vec{AM} = -\dfrac{1}{6}\vec{AB} + \dfrac{2}{3}\vec{AC}$.\\
Vì $C$ là trung điểm $AP \Rightarrow \vec{AP} = 2\vec{AC}$, suy ra $\vec{MP} = \vec{AP} - \vec{AM} = -\dfrac{1}{2}\vec{AB} + 2\vec{AC}$.\\
b) Nhận thấy $\vec{MP} = 3\left(-\dfrac{1}{6}\vec{AB} + \dfrac{2}{3}\vec{AC}\right) = 3\vec{MN}$. Vậy hai vectơ $\vec{MP}, \vec{MN}$ cùng phương, suy ra ba điểm $M, N, P$ thẳng hàng.

\textbf{Bài 2.}
a) Ta có $AB = \sqrt{(-2-1)^2 + (0-4)^2} = 5$; $AC = \sqrt{(6-1)^2 + (4-4)^2} = 5$. Vậy $AB = AC = 5$, chứng tỏ $\triangle ABC$ cân tại $A$.\\
Do $\triangle ABC$ cân tại $A$ nên chân đường cao $H$ cũng là trung điểm $BC$: $H\left(\dfrac{-2+6}{2}; \dfrac{0+4}{2}\right) = H(2; 2)$.\\
b) Gọi $G$ là trọng tâm $\triangle ABC$: $G\left(\dfrac{1-2+6}{3}; \dfrac{4+0+4}{3}\right) = G\left(\dfrac{5}{3}; \dfrac{8}{3}\right)$.\\
Ta có $|\vec{MA} + \vec{MB} + \vec{MC}| = |3\vec{MG}| = 3MG$. Biểu thức nhỏ nhất khi $M \in Ox$ là hình chiếu vuông góc của $G$ lên $Ox$, tức $M\left(\dfrac{5}{3}; 0\right)$. Giá trị nhỏ nhất bằng $3 \cdot \dfrac{8}{3} = 8$.

\textbf{Bài 3.}
a) Trạng thái cân bằng: $\vec{T}_1 + \vec{T}_2 + \vec{P} = \vec{0}$.\\
Do tính đối xứng nên $T_1 = T_2 = T$. Chiếu phương trình lên phương thẳng đứng hướng lên: $T\sin 30^\circ + T\sin 30^\circ = P \Leftrightarrow 2T \cdot \dfrac{1}{2} = 120 \Leftrightarrow T = 120\text{ N}$.\\
b) Khi hai dây vuông góc (góc với trần là $45^\circ$): $2T'\sin 45^\circ = 120 \Leftrightarrow T'\sqrt{2} = 120 \Leftrightarrow T' = 60\sqrt{2} \approx 84{,}9\text{ N}$.\\
Nhận xét: Khi góc giữa hai dây giảm từ $120^\circ$ xuống $90^\circ$ (dây dốc đứng hơn), lực căng mỗi dây giảm từ $120\text{ N}$ xuống còn khoảng $84{,}9\text{ N}$.

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

    print("[3/4] Splitting into De_On_Tap_Vector_4_Exam.pdf and De_On_Tap_Vector_4_Ans.pdf...")
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

    print("\nBUILD COMPLETE FOR ĐỀ ÔN TẬP VECTƠ SỐ 4!")


if __name__ == "__main__":
    main()
