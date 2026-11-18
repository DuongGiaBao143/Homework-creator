#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build pipeline for English version of Grade 10 Review Exam #3: Chapter IV. Vectors (Toán 10 KNTT), Code 1044-EN.
Generates standalone English student exam PDF (3 pages), answer key PDF (2 pages), and combined PDF,
audits pagination, and exports to Grade 10 teaching folders.
"""

import re
import shutil
import subprocess
from pathlib import Path
import pymupdf

BASE_DIR = Path(r"d:\Tao_De\Lớp 10\Output\De_On_Tap_Vector_3")
OUT_DIR = BASE_DIR
TEX_PATH = OUT_DIR / "De_On_Tap_Vector_3_EN.tex"
FULL_PDF = OUT_DIR / "De_On_Tap_Vector_3_EN.pdf"
EXAM_PDF = OUT_DIR / "De_On_Tap_Vector_3_EN_Exam.pdf"
ANS_PDF = OUT_DIR / "De_On_Tap_Vector_3_EN_Ans.pdf"

EXPORT_TARGETS = [
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\Vector\De_On_Tap_Vector_3_EN.pdf"), "exam"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\Vector\Ans\De_On_Tap_Vector_3_EN_Ans.pdf"), "ans"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương IV\Đề ôn tập Chương 4 - Vectơ (Đề 3 - English).pdf"), "exam"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương IV\Ans\Đề ôn tập Chương 4 - Vectơ (Đề 3 - English - Đáp án).pdf"), "ans"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương IV\Ans\Đề ôn tập Chương 4 - Vectơ (Đề 3 - English - có đáp án).pdf"), "full"),
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
        lines.append(f"    \\or {q}% Page {i}")
    lines.append(f"    \\else {QUOTES[0]}%")
    lines.append(r"  \fi")
    lines.append(r"}")
    return "\n".join(lines)


PREAMBLE = r"""\documentclass[10pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage[vietnamese,english]{babel}
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
\rhead{\small\textbf{\color{ink}Compiled by: Dương Gia Bảo}}
\lfoot{}
\rfoot{\small Page \thepage/__EXAM_PAGES__}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}

\fancypagestyle{dapan}{
  \fancyhf{}
  \lhead{\footnotesize\textit{\color{gray!70!black}\headerQuote}}
  \rhead{\small\textbf{\color{ink}Compiled by: Dương Gia Bảo}}
  \lfoot{\small\textit{\color{gray!60!black}Answer Key — Grade 10 Math Review (Chapter IV: Vectors — Test 3)}}
  \rfoot{\small Page \thepage/__ANS_PAGES__}
  \renewcommand{\headrulewidth}{0.4pt}
  \renewcommand{\footrulewidth}{0pt}
}

\newcommand{\parttitle}[1]{\par\vspace{3.5pt}\needspace{3\baselineskip}{\large\bfseries\color{ink}#1}\par\nopagebreak\vspace{2pt}}
\newcommand{\four}[4]{\par\noindent\begin{tabularx}{\linewidth}{@{}*{4}{>{\raggedright\arraybackslash}X}@{}}\textbf{A.} #1&\textbf{B.} #2&\textbf{C.} #3&\textbf{D.} #4\end{tabularx}}
\newcommand{\two}[4]{\par\noindent\begin{tabularx}{\linewidth}{@{}*{2}{>{\raggedright\arraybackslash}X}@{}}\textbf{A.} #1&\textbf{B.} #2\\[3.8pt]\textbf{C.} #3&\textbf{D.} #4\end{tabularx}}
\newcommand{\one}[4]{\par\noindent\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X@{}}\textbf{A.} #1\\[4pt]\textbf{B.} #2\\[4pt]\textbf{C.} #3\\[4pt]\textbf{D.} #4\end{tabularx}}
\newcommand{\answerbox}{\hfill\mbox{\textit{Answer:}\ \fbox{\rule{0pt}{7.5pt}\hspace{1.8cm}}}}

\setlist[enumerate,1]{label=\textbf{Question \arabic*.},leftmargin=2.1cm,labelsep=.15cm,itemsep=1.2pt,topsep=1.2pt,parsep=0pt}
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

    # ==================== EXAM ====================
    parts.append(r"""\noindent
\begin{minipage}[c]{0.38\textwidth}
    \centering
    \textbf{DO MATH TO BE HAPPY}\\[-2pt]
    \rule{3.2cm}{0.6pt}\\[2pt]
    \textbf{OFFICIAL REVIEW TEST}
\end{minipage}\hfill
\begin{minipage}[c]{0.52\textwidth}
    \centering
    \textbf{GRADE 10 MATH REVIEW — CHAPTER IV. VECTORS (TEST 3)}\\[1pt]
    \textbf{ACADEMIC YEAR 2026 -- 2027}\\[1pt]
    \textbf{Subject: MATHEMATICS -- Grade 10}\\
    \textit{\small Time allowed: 90 minutes (excluding distribution time)}
\end{minipage}

\vspace{0.05cm}
\noindent
\begin{minipage}[b]{0.78\textwidth}
    \textbf{Full Name:}\dotfill\textbf{ID:}\makebox[3.5cm]{\dotfill}
\end{minipage}\hfill
\begin{minipage}[b]{0.20\textwidth}
    \hfill
    \setlength{\fboxrule}{0.8pt}%
    \fbox{\begin{minipage}{2.3cm}
        \centering
        \textbf{\small Test Code}\\
        \textbf{1044-EN}
    \end{minipage}}
\end{minipage}
\vspace{0.05cm}

\parttitle{PART I. Multiple-Choice Questions}
\textit{Answer Questions 1 to 20. Choose only one correct option for each question.}
\begin{enumerate}
\item Given a parallelogram $ABCD$ with center $O$. How many nonzero vectors are collinear (parallel) with $\vec{AB}$ and have both initial and terminal points at the vertices of parallelogram $ABCD$?
\four{$2$.}{$6$.}{$8$.}{$4$.}

\item Given a regular hexagon $ABCDEF$ with center $O$. Which of the following vectors is equal to $\vec{AB}$?
\four{$\vec{CF}$.}{$\vec{OC}$.}{$\vec{DE}$.}{$\vec{OF}$.}

\item For any four points $M, N, P, Q$, which of the following vector equations is always true?
\two{$\vec{MN} + \vec{PQ} = \vec{MQ} + \vec{NP}$.}{$\vec{MN} - \vec{MP} = \vec{NP}$.}{$\vec{MN} + \vec{PQ} = \vec{MQ} + \vec{PN}$.}{$\vec{MN} + \vec{NQ} = \vec{QM}$.}

\item Let $ABC$ be a right triangle at $A$ with $AB = 3$ and $AC = 4$. What is the magnitude of the vector $\vec{u} = \vec{AB} - \vec{AC}$?
\four{$5$.}{$7$.}{$1$.}{$\sqrt{7}$.}

\item Let $ABCD$ be a rhombus with side length $a$ and $\widehat{ABC} = 60^\circ$. What is the magnitude of the vector $\vec{v} = \vec{BA} + \vec{BC}$?
\four{$a$.}{$a\sqrt{3}$.}{$a\sqrt{2}$.}{$2a$.}

\item Let $G$ be the centroid of triangle $ABC$ and $O$ be any point in the plane. Which of the following statements is true?
\two{$\vec{OA} + \vec{OB} + \vec{OC} = \vec{OG}$.}{$\vec{OA} + \vec{OB} + \vec{OC} = 2\vec{OG}$.}{$\vec{GB} + \vec{GC} = \vec{GA}$.}{$\vec{OA} + \vec{OB} + \vec{OC} = 3\vec{OG}$.}

\item Given line segment $AB$ and a point $M$ lying on segment $AB$ such that $MA = 3MB$. Which of the following vector equations is correct?
\two{$\vec{AM} = \dfrac{3}{4}\vec{AB}$.}{$\vec{AM} = \dfrac{1}{4}\vec{AB}$.}{$\vec{AM} = -\dfrac{3}{4}\vec{AB}$.}{$\vec{AM} = \dfrac{4}{3}\vec{AB}$.}

\item Given a parallelogram $ABCD$, let $M$ be the midpoint of side $BC$. Expressing vector $\vec{AM}$ in terms of $\vec{AB}$ and $\vec{AD}$ gives
\two{$\vec{AM} = \dfrac{1}{2}\vec{AB} + \vec{AD}$.}{$\vec{AM} = \vec{AB} - \dfrac{1}{2}\vec{AD}$.}{$\vec{AM} = \vec{AB} + \dfrac{1}{2}\vec{AD}$.}{$\vec{AM} = \dfrac{1}{2}\vec{AB} + \dfrac{1}{2}\vec{AD}$.}

\item In the Cartesian coordinate plane $Oxy$, given point $A(2, -1)$ and vector $\vec{u} = -3\vec{i} + 4\vec{j}$. What are the coordinates of vector $\vec{v} = \vec{OA} + \vec{u}$?
\four{$(5, -5)$.}{$(1, -3)$.}{$(-1, -5)$.}{$(-1, 3)$.}

\item In the coordinate plane $Oxy$, given two vectors $\vec{a} = (1, -2)$ and $\vec{b} = (-3, 5)$. What are the coordinates of vector $\vec{c} = 2\vec{a} - \vec{b}$?
\four{$(5, -9)$.}{$(-1, 1)$.}{$(5, 1)$.}{$(-5, 9)$.}

\item In the coordinate plane $Oxy$, given triangle $ABC$ with $A(1, 4)$, $B(-3, 2)$, and $C(5, -3)$. What are the coordinates of the centroid $G$ of triangle $ABC$?
\four{$G(3, 3)$.}{$G(1, 1)$.}{$G(1, 3)$.}{$G(-1, 1)$.}

\item In the coordinate plane $Oxy$, given three points $A(-1, 2)$, $B(2, -4)$, and $C(m, 4)$. For what value of parameter $m$ are points $A, B, C$ collinear?
\four{$m = 2$.}{$m = 0$.}{$m = -2$.}{$m = -4$.}
\pagebreak

\item In the coordinate plane $Oxy$, given two vectors $\vec{u} = (m, -4)$ and $\vec{v} = (-3, 6)$. For what value of $m$ are vectors $\vec{u}$ and $\vec{v}$ parallel (collinear)?
\four{$m = 2$.}{$m = -2$.}{$m = 8$.}{$m = -8$.}

\item Let $ABC$ be an isosceles right triangle at $A$. What is the angle between the vectors $\vec{AB}$ and $\vec{BC}$?
\four{$45^\circ$.}{$90^\circ$.}{$60^\circ$.}{$135^\circ$.}

\item Let $ABC$ be an equilateral triangle with side length $a$. What is the dot product $\vec{AB} \cdot \vec{AC}$?
\four{$a^2$.}{$\dfrac{a^2}{2}$.}{$-\dfrac{a^2}{2}$.}{$\dfrac{a^2\sqrt{3}}{2}$.}

\item In the coordinate plane $Oxy$, given two vectors $\vec{a} = (2, -1)$ and $\vec{b} = (3, 4)$. What is the value of $\vec{a} \cdot (\vec{a} + \vec{b})$?
\four{$2$.}{$5$.}{$7$.}{$13$.}

\item In the coordinate plane $Oxy$, given two points $A(1, -2)$ and $B(-5, 6)$. What is the length of segment $AB$?
\four{$10$.}{$100$.}{$2\sqrt{13}$.}{$14$.}

\item In the coordinate plane $Oxy$, given two vectors $\vec{u} = (m + 1, 3)$ and $\vec{v} = (2, -4)$. For what value of $m$ is $\vec{u} \perp \vec{v}$?
\four{$m = -5$.}{$m = 7$.}{$m = -7$.}{$m = 5$.}

\item In the coordinate plane $Oxy$, given two vectors $\vec{x} = (1, \sqrt{3})$ and $\vec{y} = (\sqrt{3}, 1)$. What is the angle between $\vec{x}$ and $\vec{y}$?
\four{$60^\circ$.}{$30^\circ$.}{$45^\circ$.}{$120^\circ$.}

\item A person pushes a cart over a distance of $20\text{ m}$ using a constant force $\vec{F}$ of magnitude $80\text{ N}$ making an angle of $30^\circ$ with the direction of motion. What is the work $W$ done by force $\vec{F}$?
\four{$1600\text{ J}$.}{$800\text{ J}$.}{$800\sqrt{3}\text{ J}$.}{$1600\sqrt{3}\text{ J}$.}
\end{enumerate}

\vspace{3pt}
\parttitle{PART II. True/False Questions}
\textit{Answer Questions 1 to 4. For each statement a), b), c), d) in every question, indicate whether it is True or False.}
\begin{enumerate}
\item Given an equilateral triangle $ABC$ with side length $a$, $M$ is the midpoint of side $BC$, and $G$ is the centroid of triangle $ABC$ (as shown in the figure).
\par\noindent\begin{minipage}[t]{0.72\linewidth}
\begin{enumerate}
    \item The magnitude of vector $\vec{AG}$ is $\dfrac{a\sqrt{3}}{3}$.
    \item The vector equality $\vec{AB} + \vec{AC} = 3\vec{AG}$ is true.
    \item The dot product is $\vec{GA} \cdot \vec{GB} = \dfrac{a^2}{6}$.
    \item The magnitude of vector $\vec{GB} - \vec{GC}$ is $a$.
\end{enumerate}
\end{minipage}\hfill
\begin{minipage}[t]{0.26\linewidth}\raggedleft\vspace{-6pt}
""" + TIKZ_P2_Q1 + r"""
\end{minipage}

\item Given triangle $ABC$. Let $M$ be the midpoint of side $BC$ and $N$ be a point on segment $AC$ such that $3NA = 2NC$ (ratio $NA : NC = 2 : 3$).
\begin{enumerate}
    \item Vector $\vec{AM}$ can be expressed as $\vec{AM} = \dfrac{1}{2}\vec{AB} - \dfrac{1}{2}\vec{AC}$.
    \item Vector $\vec{AN}$ can be expressed as $\vec{AN} = \dfrac{2}{3}\vec{AC}$.
    \item Vector $\vec{BN}$ can be expressed as $\vec{BN} = -\vec{AB} + \dfrac{2}{5}\vec{AC}$.
    \item Vector $\vec{MN}$ can be expressed as $\vec{MN} = -\dfrac{1}{2}\vec{AB} - \dfrac{1}{10}\vec{AC}$.
\end{enumerate}

\item In the coordinate plane $Oxy$, given three points $A(1, 2)$, $B(4, 6)$, and $C(9, 6)$.
\begin{enumerate}
    \item Point $D$, symmetric to $A$ across $B$, has coordinates $D(7, 10)$.
    \item Triangle $ABC$ is an isosceles right triangle at $B$.
    \item The length of segment $AC$ is $4\sqrt{5}$.
    \item The dot product is $\vec{AB} \cdot \vec{AC} = 20$.
\end{enumerate}

\item Given rectangle $ABCD$ with $AB = 6$ and $AD = 8$.
\begin{enumerate}
    \item The dot product is $\vec{AC} \cdot \vec{BD} = 0$.
    \item The dot product is $\vec{AB} \cdot \vec{AC} = 36$.
    \item The magnitude of vector $\vec{AC} + \vec{BD}$ is $16$.
    \item The magnitude of vector $\vec{AB} + \vec{AC}$ is $14$.
\end{enumerate}
\end{enumerate}

\pagebreak
\parttitle{PART III. Short-Answer Questions}
\textit{Answer Questions 1 to 6. Write your final answer in the corresponding box.}
\begin{enumerate}
\item Given triangle $ABC$ with $AB = 5$, $AC = 8$, and $\widehat{BAC} = 60^\circ$. Find the magnitude of vector $\vec{u} = \vec{AB} - \vec{AC}$.\answerbox

\item Given triangle $ABC$. Let $M$ be the midpoint of side $BC$ and $I$ be the midpoint of segment $AM$. Given that $\vec{BI} = x\vec{AB} + y\vec{AC}$ where $x, y \in \mathbb{R}$, calculate $P = 8y - 4x$.\answerbox

\item In the coordinate plane $Oxy$, given parallelogram $ABCD$ with $A(-1, 3)$, $B(2, 5)$, and $C(4, 1)$. Let $D(x_D, y_D)$ be the fourth vertex; calculate $T = 4x_D - 5y_D$.\answerbox

\item In the coordinate plane $Oxy$, given three points $A(1, 2)$, $B(4, 6)$, and $C(-2, 6)$. Find the value of $\cos \widehat{BAC}$ (express your answer as an exact decimal).\answerbox

\item In the coordinate plane $Oxy$, given vectors $\vec{a} = (2, 2)$, $\vec{b} = (-1, 3)$, and $\vec{c} = (5, 1)$. Find the value of the real parameter $k$ such that $\vec{u} = \vec{a} + k\vec{b}$ is orthogonal to $\vec{c}$.\answerbox

\item \begin{minipage}[t]{0.70\linewidth}
A worker pulls a crate across a horizontal floor with a rope making an angle of $30^\circ$ above the horizontal (as shown in the figure). Given a constant pulling force of magnitude $F = 40\sqrt{3}\text{ N}$ and a straight-line displacement of $s = 15\text{ m}$, calculate the mechanical work $W$ done by force $\vec{F}$ (in Joules).\answerbox
\end{minipage}\hfill
\begin{minipage}[t]{0.28\linewidth}\raggedleft\vspace{-6pt}
""" + TIKZ_P3_Q6 + r"""
\end{minipage}
\end{enumerate}

\vspace{3pt}
\parttitle{PART IV. Free-Response Problems}
\textit{Show complete reasoning and step-by-step solutions for the following problems:}

\vspace{4pt}
\textbf{Problem 1 (1.0 point).} Given triangle $ABC$. Let $I$ be the midpoint of side $BC$, $K$ be the midpoint of segment $AI$, and $D$ be a point on side $AC$ such that $AD = \dfrac{1}{3}AC$.
\begin{enumerate}[label=\alph*), leftmargin=0.6cm, itemsep=2pt]
    \item (0.5 point) Express vectors $\vec{BK}$ and $\vec{BD}$ in terms of $\vec{AB}$ and $\vec{AC}$.
    \item (0.5 point) Using the results from part a), prove that points $B, K, D$ are collinear.
\end{enumerate}

\vspace{6pt}
\textbf{Problem 2 (1.0 point).} In the coordinate plane $Oxy$, given triangle $ABC$ with vertices $A(-2, 6)$, $B(6, 2)$, and $C(-3, -1)$.
\begin{enumerate}[label=\alph*), leftmargin=0.6cm, itemsep=2pt]
    \item (0.5 point) Find the coordinates of point $M$ on the $x$-axis ($Ox$) that minimizes $|\vec{MA} + \vec{MB}|$, and determine that minimum value.
    \item (0.5 point) Find the coordinates of the circumcenter $I$ of triangle $ABC$.
\end{enumerate}

\vspace{6pt}
\textbf{Problem 3 (1.0 point).} Two tugboats simultaneously pull a large ship at point $O$ with pulling forces $\vec{F}_1$ and $\vec{F}_2$ of magnitudes $F_1 = 5000\text{ N}$ and $F_2 = 8000\text{ N}$, respectively, making an angle of $120^\circ$ with each other (as shown in the figure).
\par\noindent\begin{minipage}[t]{0.70\linewidth}
\begin{enumerate}[label=\alph*), leftmargin=0.6cm, itemsep=2pt]
    \item (0.5 point) Express the resultant force vector $\vec{F}$ in terms of $\vec{F}_1, \vec{F}_2$ and compute its magnitude $|\vec{F}|$ acting on the ship.
    \item (0.5 point) Choose a coordinate system $Oxy$ such that the positive $x$-axis ($Ox$) aligns with $\vec{F}_1$ (as shown). Find the coordinates of $\vec{F}_1, \vec{F}_2, \vec{F}$ and determine the angle $\alpha$ between $\vec{F}$ and $\vec{F}_1$ (round to one decimal place in degrees).
\end{enumerate}
\end{minipage}\hfill
\begin{minipage}[t]{0.28\linewidth}\raggedleft\vspace{-15pt}
""" + TIKZ_P4_B3 + r"""
\end{minipage}
""")

    # ==================== ANSWER KEY & SOLUTIONS ====================
    parts.append(r"""\newpage
\pagestyle{dapan}
\setcounter{page}{1}

\begin{center}
  {\Large\bfseries\color{ink} COMPREHENSIVE ANSWER KEY}\\[2pt]
  {\small\color{gray!75!black} Grade 10 Math Review — Chapter IV. Vectors (Test 3 — Code 1044-EN)}
\end{center}
\vspace{1pt}

\noindent\textbf{PART I. Multiple-Choice Questions (20 questions)}
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
\textbf{PART II. True/False Questions}\\[1.5pt]
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|c|c|c|c|c|}
\hline
\textbf{Q} & \textbf{a)} & \textbf{b)} & \textbf{c)} & \textbf{d)} \\ \hline
\textbf{1} & \textbf{T} & \textbf{T} & \textbf{F} & \textbf{T} \\ \hline
\textbf{2} & \textbf{F} & \textbf{F} & \textbf{T} & \textbf{T} \\ \hline
\textbf{3} & \textbf{T} & \textbf{F} & \textbf{T} & \textbf{F} \\ \hline
\textbf{4} & \textbf{F} & \textbf{T} & \textbf{T} & \textbf{F} \\ \hline
\end{tabular}
\end{minipage}\hfill
\begin{minipage}[t]{0.40\linewidth}
\textbf{PART III. Short-Answer Questions}\\[1.5pt]
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|c|c|c|c|}
\hline
\textbf{Q} & \textbf{Answer} & \textbf{Q} & \textbf{Answer} \\ \hline
\textbf{1} & $7$ & \textbf{4} & $0.28$ \\ \hline
\textbf{2} & $5$ & \textbf{5} & $6$ \\ \hline
\textbf{3} & $9$ & \textbf{6} & $900$ \\ \hline
\end{tabular}
\end{minipage}

\vspace{5pt}
\noindent\textbf{PART IV. Free-Response Summary:}\\[2pt]
- \textbf{Problem 1:} a) $\vec{BK} = -\dfrac{3}{4}\vec{AB} + \dfrac{1}{4}\vec{AC}$; $\vec{BD} = -\vec{AB} + \dfrac{1}{3}\vec{AC}$. b) $\vec{BK} = \dfrac{3}{4}\vec{BD} \Rightarrow B, K, D$ are collinear.\\
- \textbf{Problem 2:} a) $M(2, 0)$, minimum value is $8$. b) Circumcenter $I(1, 2)$.\\
- \textbf{Problem 3:} a) $\vec{F} = \vec{F}_1 + \vec{F}_2$, $|\vec{F}| = 7000\text{ N}$. b) $\vec{F}_1 = (5000, 0)$, $\vec{F}_2 = (-4000, 4000\sqrt{3})$, $\vec{F} = (1000, 4000\sqrt{3})$, $\alpha \approx 81.8^\circ$.

\vspace{2pt}
\begin{center}
  {\large\bfseries\color{ink} DETAILED SOLUTIONS}
\end{center}
\vspace{0pt}

\begin{multicols}{2}
\raggedcolumns
\small

\textbf{\color{accent}PART I. MULTIPLE-CHOICE}

\textbf{Question 1.} The nonzero vectors collinear with $\vec{AB}$ formed by the vertices of parallelogram $ABCD$ are $\vec{AB}, \vec{BA}, \vec{CD}, \vec{DC}$ ($4$ vectors). Choice \textbf{D}.

\textbf{Question 2.} In regular hexagon $ABCDEF$ with center $O$, segment $AB$ is parallel, identically oriented, and equal in length to $OC$, so $\vec{AB} = \vec{OC}$. Choice \textbf{B}.

\textbf{Question 3.} $\vec{MN} + \vec{PQ} = (\vec{MQ} + \vec{QN}) + (\vec{PN} + \vec{NQ}) = \vec{MQ} + \vec{PN} + (\vec{QN} + \vec{NQ}) = \vec{MQ} + \vec{PN}$. Choice \textbf{C}.

\textbf{Question 4.} $\vec{u} = \vec{AB} - \vec{AC} = \vec{CB} \Rightarrow |\vec{u}| = BC = \sqrt{3^2 + 4^2} = 5$. Choice \textbf{A}.

\textbf{Question 5.} $\vec{v} = \vec{BA} + \vec{BC} = \vec{BD}$. Since $ABCD$ is a rhombus of side $a$ with $\widehat{ABC} = 60^\circ$, $\triangle ABC$ is equilateral ($AC = a$), and diagonal $BD = 2 \cdot \dfrac{a\sqrt{3}}{2} = a\sqrt{3}$. Choice \textbf{B}.

\textbf{Question 6.} For centroid $G$ of $\triangle ABC$ and any point $O$: $\vec{OA} + \vec{OB} + \vec{OC} = 3\vec{OG} + (\vec{GA} + \vec{GB} + \vec{GC}) = 3\vec{OG}$. Choice \textbf{D}.

\textbf{Question 7.} $M$ lies on segment $AB$ with $MA = 3MB \Rightarrow AM = \dfrac{3}{4}AB$ and $\vec{AM}$ has the same direction as $\vec{AB}$, so $\vec{AM} = \dfrac{3}{4}\vec{AB}$. Choice \textbf{A}.

\textbf{Question 8.} $\vec{AM} = \vec{AB} + \vec{BM} = \vec{AB} + \dfrac{1}{2}\vec{BC} = \vec{AB} + \dfrac{1}{2}\vec{AD}$. Choice \textbf{C}.

\textbf{Question 9.} $\vec{OA} = (2, -1)$, $\vec{u} = (-3, 4) \Rightarrow \vec{v} = (2 - 3, -1 + 4) = (-1, 3)$. Choice \textbf{D}.

\textbf{Question 10.} $\vec{c} = 2(1, -2) - (-3, 5) = (2 + 3, -4 - 5) = (5, -9)$. Choice \textbf{A}.

\textbf{Question 11.} $x_G = \dfrac{1 - 3 + 5}{3} = 1$, $y_G = \dfrac{4 + 2 - 3}{3} = 1 \Rightarrow G(1, 1)$. Choice \textbf{B}.

\textbf{Question 12.} $\vec{AB} = (3, -6)$, $\vec{AC} = (m + 1, 2)$. Collinear $\Leftrightarrow 3(2) - (-6)(m + 1) = 0 \Leftrightarrow 6m + 12 = 0 \Leftrightarrow m = -2$. Choice \textbf{C}.

\textbf{Question 13.} $\vec{u} \parallel \vec{v} \Leftrightarrow 6m - (-4)(-3) = 0 \Leftrightarrow 6m = 12 \Leftrightarrow m = 2$. Choice \textbf{A}.

\textbf{Question 14.} Since $\triangle ABC$ is right isosceles at $A$, $\widehat{B} = 45^\circ$. Thus $(\vec{AB}, \vec{BC}) = 180^\circ - 45^\circ = 135^\circ$. Choice \textbf{D}.

\textbf{Question 15.} $\vec{AB} \cdot \vec{AC} = a \cdot a \cdot \cos 60^\circ = \dfrac{a^2}{2}$. Choice \textbf{B}.

\textbf{Question 16.} $\vec{a} + \vec{b} = (5, 3) \Rightarrow \vec{a} \cdot (\vec{a} + \vec{b}) = 2(5) + (-1)(3) = 7$. Choice \textbf{C}.

\textbf{Question 17.} $\vec{AB} = (-6, 8) \Rightarrow AB = \sqrt{(-6)^2 + 8^2} = 10$. Choice \textbf{A}.

\textbf{Question 18.} $\vec{u} \perp \vec{v} \Leftrightarrow 2(m + 1) + 3(-4) = 0 \Leftrightarrow 2m - 10 = 0 \Leftrightarrow m = 5$. Choice \textbf{D}.

\textbf{Question 19.} $\cos(\vec{x}, \vec{y}) = \dfrac{1\sqrt{3} + \sqrt{3}\cdot 1}{\sqrt{1+3}\sqrt{3+1}} = \dfrac{2\sqrt{3}}{4} = \dfrac{\sqrt{3}}{2} \Rightarrow (\vec{x}, \vec{y}) = 30^\circ$. Choice \textbf{B}.

\textbf{Question 20.} $W = F \cdot s \cdot \cos 30^\circ = 80 \cdot 20 \cdot \dfrac{\sqrt{3}}{2} = 800\sqrt{3}\text{ J}$. Choice \textbf{C}.

\columnbreak

\textbf{\color{accent}PART II. TRUE / FALSE}

\textbf{Question 1.}
a) Median $AM = \dfrac{a\sqrt{3}}{2} \Rightarrow |\vec{AG}| = \dfrac{2}{3}AM = \dfrac{a\sqrt{3}}{3} \Rightarrow$ \textbf{True}.\\
b) $\vec{AB} + \vec{AC} = 2\vec{AM} = 2 \cdot \dfrac{3}{2}\vec{AG} = 3\vec{AG} \Rightarrow$ \textbf{True}.\\
c) $(\vec{GA}, \vec{GB}) = 120^\circ$, $GA = GB = \dfrac{a\sqrt{3}}{3} \Rightarrow \vec{GA}\cdot\vec{GB} = \dfrac{a^2}{3}\cos 120^\circ = -\dfrac{a^2}{6} \ne \dfrac{a^2}{6} \Rightarrow$ \textbf{False}.\\
d) $|\vec{GB} - \vec{GC}| = |\vec{CB}| = a \Rightarrow$ \textbf{True}.

\textbf{Question 2.}
a) Since $M$ is the midpoint of $BC$, $\vec{AM} = \dfrac{1}{2}\vec{AB} + \dfrac{1}{2}\vec{AC} \Rightarrow$ \textbf{False}.\\
b) Since $N$ lies on $AC$ with $3NA = 2NC$, $AN = \dfrac{2}{5}AC \Rightarrow \vec{AN} = \dfrac{2}{5}\vec{AC} \ne \dfrac{2}{3}\vec{AC} \Rightarrow$ \textbf{False}.\\
c) $\vec{BN} = \vec{AN} - \vec{AB} = -\vec{AB} + \dfrac{2}{5}\vec{AC} \Rightarrow$ \textbf{True}.\\
d) $\vec{MN} = \vec{AN} - \vec{AM} = \dfrac{2}{5}\vec{AC} - \left(\dfrac{1}{2}\vec{AB} + \dfrac{1}{2}\vec{AC}\right) = -\dfrac{1}{2}\vec{AB} - \dfrac{1}{10}\vec{AC} \Rightarrow$ \textbf{True}.

\textbf{Question 3.}
a) $B$ is the midpoint of $AD \Rightarrow D = 2B - A = (7, 10) \Rightarrow$ \textbf{True}.\\
b) $\vec{AB} = (3, 4)$, $\vec{BC} = (5, 0)$. Although $BA = BC = 5$, $\vec{AB} \cdot \vec{BC} = 15 \ne 0$, so $\angle B \ne 90^\circ \Rightarrow$ \textbf{False}.\\
c) $\vec{AC} = (8, 4) \Rightarrow AC = \sqrt{64 + 16} = \sqrt{80} = 4\sqrt{5} \Rightarrow$ \textbf{True}.\\
d) $\vec{AB} \cdot \vec{AC} = 3(8) + 4(4) = 40 \ne 20 \Rightarrow$ \textbf{False}.

\textbf{Question 4.} Place axes at $A(0, 0), B(6, 0), C(6, 8), D(0, 8)$.\\
a) $\vec{AC} = (6, 8)$, $\vec{BD} = (-6, 8) \Rightarrow \vec{AC} \cdot \vec{BD} = -36 + 64 = 28 \ne 0 \Rightarrow$ \textbf{False}.\\
b) $\vec{AB} \cdot \vec{AC} = 6(6) + 0(8) = 36 \Rightarrow$ \textbf{True}.\\
c) $\vec{AC} + \vec{BD} = (0, 16) = 2\vec{AD} \Rightarrow |\vec{AC} + \vec{BD}| = 16 \Rightarrow$ \textbf{True}.\\
d) $\vec{AB} + \vec{AC} = (12, 8) \Rightarrow |\vec{AB} + \vec{AC}| = \sqrt{144 + 64} = 4\sqrt{13} \ne 14 \Rightarrow$ \textbf{False}.

\textbf{\color{accent}PART III. SHORT-ANSWER}

\textbf{Question 1.} $|\vec{u}| = |\vec{CB}| = BC = \sqrt{5^2 + 8^2 - 2\cdot 5\cdot 8\cos 60^\circ} = \sqrt{49} = \mathbf{7}$.

\textbf{Question 2.} $\vec{AI} = \dfrac{1}{2}\vec{AM} = \dfrac{1}{4}(\vec{AB} + \vec{AC})$. Hence $\vec{BI} = \vec{AI} - \vec{AB} = -\dfrac{3}{4}\vec{AB} + \dfrac{1}{4}\vec{AC}$. Thus $x = -\dfrac{3}{4}, y = \dfrac{1}{4} \Rightarrow P = 8\left(\dfrac{1}{4}\right) - 4\left(-\dfrac{3}{4}\right) = 2 + 3 = \mathbf{5}$.

\textbf{Question 3.} $\vec{AD} = \vec{BC} = (2, -4) \Rightarrow D = (1, -1)$. Thus $T = 4(1) - 5(-1) = \mathbf{9}$.

\textbf{Question 4.} $\vec{AB} = (3, 4)$, $\vec{AC} = (-3, 4)$. $\cos\widehat{BAC} = \dfrac{-9 + 16}{5 \cdot 5} = \dfrac{7}{25} = \mathbf{0.28}$.

\textbf{Question 5.} $\vec{u} = (2 - k, 2 + 3k)$. $\vec{u} \perp \vec{c} \Leftrightarrow 5(2 - k) + 1(2 + 3k) = 0 \Leftrightarrow 12 - 2k = 0 \Rightarrow k = \mathbf{6}$.

\textbf{Question 6.} $W = F \cdot s \cdot \cos 30^\circ = 40\sqrt{3} \cdot 15 \cdot \dfrac{\sqrt{3}}{2} = \mathbf{900}\text{ J}$.

\textbf{\color{accent}PART IV. FREE-RESPONSE}

\textbf{Problem 1.}
a) Since $I$ is the midpoint of $BC \Rightarrow \vec{AI} = \dfrac{1}{2}(\vec{AB} + \vec{AC})$.\\
Since $K$ is the midpoint of $AI \Rightarrow \vec{AK} = \dfrac{1}{2}\vec{AI} = \dfrac{1}{4}\vec{AB} + \dfrac{1}{4}\vec{AC}$.\\
Hence $\vec{BK} = \vec{AK} - \vec{AB} = -\dfrac{3}{4}\vec{AB} + \dfrac{1}{4}\vec{AC}$.\\
Since $AD = \dfrac{1}{3}AC \Rightarrow \vec{AD} = \dfrac{1}{3}\vec{AC}$, so $\vec{BD} = \vec{AD} - \vec{AB} = -\vec{AB} + \dfrac{1}{3}\vec{AC}$.\\
b) We see $\vec{BK} = \dfrac{3}{4}\left(-\vec{AB} + \dfrac{1}{3}\vec{AC}\right) = \dfrac{3}{4}\vec{BD}$.\\
Since $\vec{BK}$ and $\vec{BD}$ are parallel, points $B, K, D$ are collinear.

\textbf{Problem 2.}
a) Let $M(x, 0) \in Ox$. Then $\vec{MA} = (-2 - x, 6)$ and $\vec{MB} = (6 - x, 2)$.\\
Thus $\vec{MA} + \vec{MB} = (4 - 2x, 8) \Rightarrow |\vec{MA} + \vec{MB}| = \sqrt{(4 - 2x)^2 + 64} \ge 8$.\\
Equality holds when $4 - 2x = 0 \Leftrightarrow x = 2$. Thus $M(\mathbf{2}, \mathbf{0})$ and the minimum value is $\mathbf{8}$.\\
b) Let the circumcenter be $I(a, b)$. Then $IA^2 = IB^2 = IC^2$:\\
$\begin{cases} (a + 2)^2 + (b - 6)^2 = (a - 6)^2 + (b - 2)^2 \\ (a - 6)^2 + (b - 2)^2 = (a + 3)^2 + (b + 1)^2 \end{cases} \Leftrightarrow \begin{cases} 16a - 8b = 0 \\ -18a - 6b = -30 \end{cases}$\\
$\Leftrightarrow \begin{cases} b = 2a \\ 3a + b = 5 \end{cases} \Leftrightarrow \begin{cases} a = 1 \\ b = 2 \end{cases}$. Hence the circumcenter is $I(\mathbf{1}, \mathbf{2})$.

\textbf{Problem 3.}
a) The resultant force acting on the ship is $\vec{F} = \vec{F}_1 + \vec{F}_2$.\\
Its magnitude is $|\vec{F}| = \sqrt{F_1^2 + F_2^2 + 2F_1 F_2 \cos 120^\circ}$\\
$= \sqrt{5000^2 + 8000^2 + 2\cdot 5000\cdot 8000\cdot \left(-\dfrac{1}{2}\right)} = 1000\sqrt{49} = \mathbf{7000}\text{ N}$.\\
b) With $Ox$ along $\vec{F}_1$, we have $\vec{F}_1 = (\mathbf{5000}, \mathbf{0})$.\\
Since $(\vec{F}_1, \vec{F}_2) = 120^\circ$, $\vec{F}_2 = (8000\cos 120^\circ, 8000\sin 120^\circ) = (\mathbf{-4000}, \mathbf{4000\sqrt{3}})$.\\
Therefore $\vec{F} = \vec{F}_1 + \vec{F}_2 = (\mathbf{1000}, \mathbf{4000\sqrt{3}})$.\\
The angle $\alpha$ between $\vec{F}$ and $\vec{F}_1$ satisfies $\cos\alpha = \dfrac{\vec{F} \cdot \vec{F}_1}{|\vec{F}||\vec{F}_1|} = \dfrac{1000 \cdot 5000}{7000 \cdot 5000} = \dfrac{1}{7} \Rightarrow \alpha \approx \mathbf{81.8}^\circ$.

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
        if "COMPREHENSIVE ANSWER KEY" in txt:
            doc.close()
            return i
    doc.close()
    raise RuntimeError("Could not locate Answer Key start page in compiled PDF!")


def audit_pagination(exam_pdf: Path, ans_pdf: Path):
    doc_exam = pymupdf.open(exam_pdf)
    print(f"\n=== AUDIT ENGLISH EXAM PDF ({len(doc_exam)} pages) ===")
    for pno, page in enumerate(doc_exam, start=1):
        txt = page.get_text("text")
        qs = re.findall(r"Question\s+(\d+)\.", txt)
        probs = re.findall(r"Problem\s+(\d+)", txt)
        rect = page.rect
        max_y = 0
        for d in page.get_drawings():
            max_y = max(max_y, d["rect"].y1)
        print(f"  Page {pno:2d}: Qs={qs} | Probs={probs} | max_y={max_y:.1f}/{rect.height:.1f}pt")
    doc_exam.close()

    doc_ans = pymupdf.open(ans_pdf)
    print(f"\n=== AUDIT ENGLISH ANS PDF ({len(doc_ans)} pages) ===")
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

    print("[3/4] Splitting into De_On_Tap_Vector_3_EN_Exam.pdf and De_On_Tap_Vector_3_EN_Ans.pdf...")
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

    print("[4/4] Exporting English PDFs to Grade 10 teaching folders...")
    src_map = {"exam": EXAM_PDF, "ans": ANS_PDF, "full": FULL_PDF}
    for dst, kind in EXPORT_TARGETS:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_map[kind], dst)
        print(f"  Copied -> {dst}")

    print("\nBUILD COMPLETE FOR ENGLISH VERSION (TEST 3)!")


if __name__ == "__main__":
    main()
