import re
import shutil
import subprocess
from pathlib import Path
import pymupdf

OUT_DIR = Path(r"d:\Tao_De\Lớp 10\Output\De_Cuong_Vector_40C")
TEX_PATH = OUT_DIR / "De_Cuong_Vector_40C.tex"
FULL_PDF = OUT_DIR / "De_Cuong_Vector_40C.pdf"
EXAM_PDF = OUT_DIR / "De_Cuong.pdf"
ANS_PDF = OUT_DIR / "De_Cuong_Ans.pdf"

EXPORT_TARGETS = [
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương IV\Đề cương ôn tập Chương 4 - Vectơ (40 câu).pdf"), "exam"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương IV\Ans\Đề cương ôn tập Chương 4 - Vectơ (40 câu) - Đáp án.pdf"), "ans"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\BTVN\Chương IV\Ans\Đề cương ôn tập Chương 4 - Vectơ (40 câu) có đáp án.pdf"), "full"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\Vector\De_Cuong_Vector_40C.pdf"), "exam"),
    (Path(r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\Vector\Ans\De_Cuong_Vector_40C_Ans.pdf"), "ans"),
]

QUOTES = [
    r"Math gives us hope that every problem has a solution",
    r"Mathematics is about understanding, not just numbers",
    r"The essence of mathematics lies in its freedom",
    r"Pure mathematics is the poetry of logical ideas",
    r"In mathematics, asking good questions matters most",
    r"Everything around you is built on mathematics",
    r"Mathematics is the queen of the sciences",
    r"Stay with tough problems a little bit longer",
    r"Success is the sum of small daily efforts",
    r"Think deeply, check carefully, solve cleanly",
    r"Genius is 1\% inspiration and 99\% perspiration",
    r"Practice makes perfect — keep solving!",
    r"Math + You = Champion",
    r"Where Frustration Becomes Inspiration",
    r"Turning Confusion into Clarity",
    r"Don't get mad. Learn to add",
    r"The only way to learn mathematics is to do mathematics",
    r"Small steps every day lead to big results",
    r"Every expert was once a beginner",
    r"Mathematics is the music of reason",
]


def build_header_quote_macro(max_pages: int = 30) -> str:
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
  \lfoot{\small\textit{\color{gray!60!black}Đáp án Đề cương Ôn tập Chương IV (Bài 7 – 10) — Toán 10 KNTT}}
  \rfoot{\small Trang \thepage/__ANS_PAGES__}
  \renewcommand{\headrulewidth}{0.4pt}
  \renewcommand{\footrulewidth}{0pt}
}

\newcommand{\chapterbanner}[2]{%
  \par\vspace{3pt}\noindent
  \begin{tikzpicture}
    \node[draw=accent, fill=accent!6, rounded corners=4pt, inner xsep=10pt, inner ysep=5pt, text width=\dimexpr\linewidth-20.8pt\relax, line width=0.8pt] {%
      {\large\bfseries\color{ink}#1}\\[2pt]
      {\small\color{gray!75!black}#2}%
    };
  \end{tikzpicture}\par\nopagebreak\vspace{4pt}
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
"""

TIKZ_Q4 = r"""\begin{tikzpicture}[scale=0.55, >=Stealth]
  \draw[step=1, color=gray!35, line width=0.35pt] (0,0) grid (6,6);
  \draw[->, accent, line width=1.3pt] (1,1) -- (4,5);
  \fill[accent] (1,1) circle (2.5pt) node[below left, font=\scriptsize] {$A$};
  \fill[accent] (4,5) circle (2.5pt) node[above right, font=\scriptsize] {$B$};
  \node[above left, font=\scriptsize, accent] at (2.5,3.2) {$\vec{u}$};
  \draw[<->, gray!80!black, line width=0.5pt] (0,-0.4) -- (1,-0.4) node[midway, below, font=\scriptsize] {$1$};
\end{tikzpicture}"""

TIKZ_Q5 = r"""\begin{tikzpicture}[scale=0.55, >=Stealth]
  \coordinate (A) at (0,3);
  \coordinate (D) at (0,0);
  \coordinate (C) at (7,0);
  \coordinate (B) at (3,3);
  \draw[thick] (A) -- (B) -- (C) -- (D) -- cycle;
  \draw[dashed, gray] (B) -- (3,0) node[below, font=\scriptsize] {$H$};
  \draw[->, red!75!black, line width=1.2pt] (B) -- (C);
  \fill[ink] (A) circle (2pt) node[above left, font=\scriptsize] {$A$};
  \fill[ink] (B) circle (2pt) node[above right, font=\scriptsize] {$B$};
  \fill[ink] (C) circle (2pt) node[below right, font=\scriptsize] {$C$};
  \fill[ink] (D) circle (2pt) node[below left, font=\scriptsize] {$D$};
  \node[above, font=\scriptsize] at (1.5,3) {$3$};
  \node[left, font=\scriptsize] at (0,1.5) {$3$};
  \node[below, font=\scriptsize] at (3.5,0) {$7$};
\end{tikzpicture}"""

TIKZ_Q12 = r"""\begin{tikzpicture}[scale=0.32, >=Stealth]
  \coordinate (A) at (0,8);
  \coordinate (B) at (6,0);
  \coordinate (C) at (0,-8);
  \coordinate (D) at (-6,0);
  \coordinate (O) at (0,0);
  \draw[thick] (A) -- (B) -- (C) -- (D) -- cycle;
  \draw[dashed, gray] (A) -- (C);
  \draw[dashed, gray] (D) -- (B);
  \fill[ink] (A) circle (2.5pt) node[above, font=\scriptsize] {$A$};
  \fill[ink] (B) circle (2.5pt) node[right, font=\scriptsize] {$B$};
  \fill[ink] (C) circle (2.5pt) node[below, font=\scriptsize] {$C$};
  \fill[ink] (D) circle (2.5pt) node[left, font=\scriptsize] {$D$};
  \fill[ink] (O) circle (2pt) node[above right, font=\scriptsize] {$O$};
  \node[above right, font=\scriptsize] at (3,4) {$10$};
  \node[below, font=\scriptsize] at (3,0) {$6$};
\end{tikzpicture}"""

TIKZ_Q29 = r"""\begin{tikzpicture}[scale=0.55, >=Stealth]
  \coordinate (O) at (0,3.5);
  \coordinate (A) at (-2,0);
  \coordinate (B) at (2,0);
  \draw[thick, fill=gray!15] (-2.5,-2.2) rectangle (2.5,0);
  \draw[line width=1.1pt, accent] (O) -- (A) node[midway, left, font=\scriptsize] {$\vec{T}_1$};
  \draw[line width=1.1pt, accent] (O) -- (B) node[midway, right, font=\scriptsize] {$\vec{T}_2$};
  \draw[dashed, gray!80] (O) -- (0,-0.5);
  \fill[red!75!black] (O) circle (2.5pt) node[above, font=\scriptsize] {Đinh};
  \fill[ink] (A) circle (2pt);
  \fill[ink] (B) circle (2pt);
  \node[font=\scriptsize] at (0,-1.1) {Tranh ($4\text{ kg}$)};
  \draw[->, line width=1.2pt, red!75!black] (0,-1.1) -- (0,-2.6) node[right, font=\scriptsize] {$\vec{P}$};
  \draw[gray!70] (-0.8,2.3) arc[start angle=240, end angle=300, radius=1.4];
  \node[font=\scriptsize, gray!90!black] at (0,2.1) {$120^\circ$};
\end{tikzpicture}"""


def build_questions():
    def q_with_fig(text_main: str, fig_code: str, text_ratio: float = 0.65) -> str:
        fig_ratio = round(0.96 - text_ratio, 2)
        return (
            r"\noindent\begin{minipage}[t]{" + f"{text_ratio:.2f}" + r"\linewidth}" + "\n"
            + text_main + "\n"
            r"\end{minipage}\hfill" + "\n"
            r"\begin{minipage}[t]{" + f"{fig_ratio:.2f}" + r"\linewidth}\raggedleft" + "\n"
            + fig_code + "\n"
            r"\end{minipage}"
        )

    # (section_hdr, text_tex, oli_h, brk)
    # Exactly 2 questions per page across all 20 pages!
    questions = [
        # ==================== TRANG 1: CÂU 1 - 2 ====================
        (r"\parttitle{CHỦ ĐỀ 1. CÁC KHÁI NIỆM MỞ ĐẦU (Bài 7 — Câu 1 đến Câu 10)}",
         r"Cho thập giác đều $A_1A_2\ldots A_{10}$ có $10$ đỉnh. Có bao nhiêu vectơ khác vectơ $\vec{0}$ có điểm đầu và điểm cuối là các đỉnh của thập giác đều đã cho?\answerbox",
         "8.0cm", False),
        (None,
         r"Cho hình chữ nhật $ABCD$ có tâm $O$. Có bao nhiêu vectơ khác vectơ $\vec{0}$ cùng phương với vectơ $\vec{AB}$ mà có điểm đầu và điểm cuối là các điểm thuộc tập hợp $\{A, B, C, D, O\}$?\answerbox",
         "8.0cm", False),

        # ==================== TRANG 2: CÂU 3 - 4 ====================
        (None,
         r"Cho tam giác $ABC$. Gọi $M, N, P$ lần lượt là trung điểm của các cạnh $BC, CA, AB$. Có bao nhiêu vectơ khác vectơ $\vec{MN}$ bằng vectơ $\vec{MN}$ mà có điểm đầu và điểm cuối là các điểm thuộc tập hợp $\{A, B, C, M, N, P\}$?\answerbox",
         "9.0cm", True),
        (None,
         q_with_fig(
             r"Cho lưới ô vuông gồm các hình vuông đơn vị có cạnh bằng $1$ (như hình vẽ bên). Hai điểm $A, B$ là hai mắt lưới. Tính độ dài của vectơ $\vec{u} = \vec{AB}$.\answerbox",
             TIKZ_Q4, text_ratio=0.62),
         "8.0cm", False),

        # ==================== TRANG 3: CÂU 5 - 6 ====================
        (None,
         q_with_fig(
             r"Cho hình thang vuông $ABCD$ vuông tại $A$ và $D$ có đáy nhỏ $AB = 3\text{ cm}$, đáy lớn $CD = 7\text{ cm}$ và cạnh bên $AD = 3\text{ cm}$ (như hình vẽ bên). Tính độ dài của vectơ $\vec{BC}$ (theo đơn vị xentimét).\answerbox",
             TIKZ_Q5, text_ratio=0.62),
         "8.0cm", True),
        (None,
         r"Cho tam giác $ABC$ vuông tại $A$ có $AB = 9\text{ cm}$ và $AC = 12\text{ cm}$. Gọi $M$ là trung điểm của cạnh huyền $BC$. Tính độ dài của vectơ $\vec{AM}$ (theo đơn vị xentimét).\answerbox",
         "9.0cm", False),

        # ==================== TRANG 4: CÂU 7 - 8 ====================
        (None,
         r"Cho hình vuông $ABCD$ có cạnh bằng $8\text{ cm}$. Gọi $M$ là trung điểm của cạnh $AB$ và $N$ là trung điểm của cạnh $BC$. Tính bình phương độ dài của vectơ $\vec{MN}$ (tức tính $|\vec{MN}|^2$).\answerbox",
         "9.0cm", True),
        (None,
         r"Cho tam giác $ABC$ có ba cạnh $AB = 5$, $AC = 7$ và $BC = 8$. Gọi $D, E$ lần lượt là trung điểm của các cạnh $AB$ và $AC$. Tính độ dài của vectơ $\vec{DE}$.\answerbox",
         "9.0cm", False),

        # ==================== TRANG 5: CÂU 9 - 10 ====================
        (None,
         r"Cho hình chữ nhật $ABCD$ có diện tích bằng $48\text{ cm}^2$ và cạnh $AB = 6\text{ cm}$. Tính độ dài của vectơ đường chéo $\vec{BD}$ (theo đơn vị xentimét).\answerbox",
         "9.0cm", True),
        (None,
         r"Cho $6$ điểm phân biệt $A, B, C, D, E, F$ trong đó không có ba điểm nào thẳng hàng. Có bao nhiêu vectơ khác vectơ $\vec{0}$ có điểm đầu là điểm $A$ và điểm cuối là một trong các điểm còn lại?\answerbox",
         "9.0cm", False),

        # ==================== TRANG 6: CÂU 11 - 12 ====================
        (r"\parttitle{CHỦ ĐỀ 2. TỔNG VÀ HIỆU CỦA HAI VECTƠ (Bài 8 — Câu 11 đến Câu 20)}",
         r"Cho hình chữ nhật $ABCD$ có $AB = 5$ và $AD = 12$. Tính độ dài của vectơ hiệu $\vec{u} = \vec{AB} - \vec{CB}$.\answerbox",
         "8.0cm", True),
        (None,
         q_with_fig(
             r"Cho hình thoi $ABCD$ có cạnh bằng $10\text{ cm}$ và đường chéo $BD = 12\text{ cm}$ (như hình vẽ bên). Tính độ dài của vectơ tổng $\vec{w} = \vec{AB} + \vec{AD}$ (theo đơn vị xentimét).\answerbox",
             TIKZ_Q12, text_ratio=0.68),
         "7.5cm", False),

        # ==================== TRANG 7: CÂU 13 - 14 ====================
        (None,
         r"Cho bốn điểm phân biệt $A, B, C, D$ thỏa mãn đoạn thẳng $BC$ có độ dài bằng $9\text{ cm}$. Tính độ dài của vectơ tổng $\vec{x} = \vec{AB} + \vec{CD} - \vec{AD}$ (theo đơn vị xentimét).\answerbox",
         "9.0cm", True),
        (None,
         r"Cho hình chữ nhật $ABCD$ có $AB = 8$ và $AD = 6$. Tính độ dài của vectơ hiệu $\vec{y} = \vec{AB} - \vec{AD}$.\answerbox",
         "9.0cm", False),

        # ==================== TRANG 8: CÂU 15 - 16 ====================
        (None,
         r"Hai lực đồng quy $\vec{F}_1$ và $\vec{F}_2$ cùng tác dụng vào một chất điểm tại điểm $O$, có phương vuông góc với nhau và có độ lớn lần lượt là $F_1 = 30\text{ N}$ và $F_2 = 40\text{ N}$. Tính độ lớn của hợp lực $\vec{F} = \vec{F}_1 + \vec{F}_2$ (theo đơn vị Niutơn).\answerbox",
         "9.0cm", True),
        (None,
         r"Hai lực $\vec{F}_1$ và $\vec{F}_2$ có cùng độ lớn bằng $60\text{ N}$, cùng tác dụng vào một vật tại điểm $O$. Biết góc giữa hai vectơ lực bằng $120^\circ$. Tính độ lớn của hợp lực $\vec{F} = \vec{F}_1 + \vec{F}_2$ tác dụng lên vật (theo đơn vị Niutơn).\answerbox",
         "9.0cm", False),

        # ==================== TRANG 9: CÂU 17 - 18 ====================
        (None,
         r"Một máy bay chuyển động đều về hướng Đông với vận tốc riêng là $600\text{ km/h}$. Cùng lúc đó có một luồng gió thổi từ hướng Bắc về hướng Nam với vận tốc $800\text{ km/h}$. Tính tốc độ thực tế của máy bay so với mặt đất (theo đơn vị $\text{km/h}$).\answerbox",
         "9.0cm", True),
        (None,
         r"Một chiếc ca nô chuyển động thẳng đều vượt qua một con sông có hai bờ song song với vận tốc đối với dòng nước là $12\text{ km/h}$ theo phương vuông góc với bờ. Vận tốc của dòng nước chảy xuôi dòng là $5\text{ km/h}$. Tính độ lớn vận tốc của ca nô đối với bờ sông (theo đơn vị $\text{km/h}$).\answerbox",
         "9.0cm", False),

        # ==================== TRANG 10: CÂU 19 - 20 ====================
        (None,
         r"Cho tam giác đều $ABC$ có cạnh bằng $6\text{ cm}$. Gọi $M$ là trung điểm của cạnh $BC$. Tính độ dài của vectơ $\vec{u} = \vec{AB} - \vec{AC}$ (theo đơn vị xentimét).\answerbox",
         "9.0cm", True),
        (None,
         r"Cho hình bình hành $ABCD$ có tâm $O$. Biết rằng độ dài của vectơ tổng $|\vec{AB} + \vec{AD}| = 14$ và độ dài của vectơ hiệu $|\vec{AB} - \vec{AD}| = 10$. Tính độ dài của đường chéo $AC$.\answerbox",
         "9.0cm", False),

        # ==================== TRANG 11: CÂU 21 - 22 ====================
        (r"\parttitle{CHỦ ĐỀ 3. TÍCH CỦA MỘT VECTƠ VỚI MỘT SỐ (Bài 9 — Câu 21 đến Câu 30)}",
         r"Cho đoạn thẳng $AB$. Điểm $M$ nằm giữa hai điểm $A$ và $B$ sao cho $MA = 3MB$. Biết $\vec{MA} = k\vec{MB}$ với $k$ là một số thực. Tìm giá trị của $k$.\answerbox",
         "8.5cm", True),
        (None,
         r"Cho tam giác $ABC$ có trọng tâm $G$. Gọi $M$ là trung điểm của cạnh $BC$. Biết vectơ $\vec{AM} = k\vec{AG}$ với $k$ là số thực. Tìm giá trị của $k$.\answerbox",
         "8.5cm", False),

        # ==================== TRANG 12: CÂU 23 - 24 ====================
        (None,
         r"Cho tam giác $ABC$. Gọi $M$ là trung điểm của cạnh $AB$ và điểm $N$ thuộc cạnh $AC$ sao cho $AN = \dfrac{1}{3}AC$. Gọi $K$ là trung điểm của đoạn thẳng $MN$. Khi phân tích vectơ $\vec{AK}$ theo hai vectơ $\vec{AB}$ và $\vec{AC}$ dưới dạng $\vec{AK} = x\vec{AB} + y\vec{AC}$, hãy tính giá trị biểu thức $P = 12x + 18y$.\answerbox",
         "9.0cm", True),
        (None,
         r"Cho tam giác $ABC$. Lấy điểm $D$ thuộc cạnh $BC$ sao cho $BD = 3DC$. Phân tích vectơ $\vec{AD}$ theo hai vectơ $\vec{AB}$ và $\vec{AC}$ dưới dạng $\vec{AD} = m\vec{AB} + n\vec{AC}$. Tính giá trị của biểu thức $S = 4m + 8n$.\answerbox",
         "9.0cm", False),

        # ==================== TRANG 13: CÂU 25 - 26 ====================
        (None,
         r"Cho đoạn thẳng $AB$. Điểm $I$ thỏa mãn hệ thức vectơ $\vec{IA} + 4\vec{IB} = \vec{0}$. Với mọi điểm $M$ bất kì, ta luôn có $\vec{MA} + 4\vec{MB} = k\vec{MI}$. Tìm giá trị của số thực $k$.\answerbox",
         "9.0cm", True),
        (None,
         r"Cho tam giác $ABC$ có trọng tâm $G$. Gọi $I$ là trung điểm của đoạn thẳng $AG$. Phân tích vectơ $\vec{BI}$ theo hai vectơ $\vec{BA}$ và $\vec{BC}$ dưới dạng $\vec{BI} = a\vec{BA} + b\vec{BC}$. Tính giá trị biểu thức $T = 6a + 6b$.\answerbox",
         "9.0cm", False),

        # ==================== TRANG 14: CÂU 27 - 28 ====================
        (None,
         r"Cho tam giác đều $ABC$ có cạnh bằng $9\text{ cm}$ và trọng tâm $G$. Tập hợp các điểm $M$ thỏa mãn đẳng thức $|\vec{MA} + \vec{MB} + \vec{MC}| = 18\text{ cm}$ là một đường tròn có bán kính $R$. Tính bán kính $R$ (theo đơn vị xentimét).\answerbox",
         "9.0cm", True),
        (None,
         r"Cho hình chữ nhật $ABCD$ có $AB = 6\text{ cm}$ và $BC = 8\text{ cm}$. Gọi $O$ là giao điểm của hai đường chéo $AC$ và $BD$. Tập hợp các điểm $M$ thỏa mãn đẳng thức $|\vec{MA} + \vec{MB} + \vec{MC} + \vec{MD}| = 20\text{ cm}$ là một đường tròn bán kính $R$. Tính bán kính $R$ (theo đơn vị xentimét).\answerbox",
         "9.0cm", False),

        # ==================== TRANG 15: CÂU 29 - 30 ====================
        (None,
         q_with_fig(
             r"Một bức tranh có khối lượng $m = 4\text{ kg}$ (trọng lượng $P = 40\text{ N}$) được treo cân bằng trên tường nhờ hai sợi dây nhẹ không dãn có cùng chiều dài gắn vào đinh treo. Hai sợi dây hợp với nhau một góc bằng $120^\circ$ và đối xứng qua phương thẳng đứng (như hình vẽ bên). Tính độ lớn lực căng $T$ của mỗi sợi dây (theo đơn vị Niutơn).\answerbox",
             TIKZ_Q29, text_ratio=0.65),
         "7.5cm", True),
        (None,
         r"Cho tam giác $ABC$. Gọi $M$ là trung điểm của cạnh $BC$ và $N$ là trung điểm của đoạn thẳng $AM$. Đường thẳng $BN$ cắt cạnh $AC$ tại điểm $P$. Biết rằng $\vec{AC} = k\vec{AP}$ với $k$ là một số thực. Tìm giá trị của $k$.\answerbox",
         "8.5cm", False),

        # ==================== TRANG 16: CÂU 31 - 32 ====================
        (r"\parttitle{CHỦ ĐỀ 4. VECTƠ TRONG MẶT PHẲNG TỌA ĐỘ (Bài 10 — Câu 31 đến Câu 40)}",
         r"Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$ có $A(1; 4)$, $B(3; -2)$ và $C(5; 7)$. Gọi $G(x_G; y_G)$ là tọa độ trọng tâm của tam giác $ABC$. Tính giá trị của tổng $x_G + y_G$.\answerbox",
         "8.5cm", True),
        (None,
         r"Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A(-1; 2)$ và $B(7; 6)$. Gọi $M$ là trung điểm của đoạn thẳng $AB$. Tính khoảng cách $OM$ từ điểm $M$ đến gốc tọa độ $O$.\answerbox",
         "8.5cm", False),

        # ==================== TRANG 17: CÂU 33 - 34 ====================
        (None,
         r"Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A(1; 2)$, $B(4; 6)$ và $C(-2; 3)$. Tìm tọa độ đỉnh $D(x_D; y_D)$ sao cho tứ giác $ABCD$ là hình bình hành. Tính giá trị của biểu thức $x_D + 2y_D$.\answerbox",
         "9.0cm", True),
        (None,
         r"Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{u} = (2; -3)$ và $\vec{v} = (1; 4)$. Vectơ $\vec{w} = 3\vec{u} - 2\vec{v}$ có tọa độ là $(x_0; y_0)$. Tính giá trị của hiệu $x_0 - y_0$.\answerbox",
         "9.0cm", False),

        # ==================== TRANG 18: CÂU 35 - 36 ====================
        (None,
         r"Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A(2; 1)$, $B(5; 7)$ và $C(m; 3)$ với $m$ là tham số thực. Tìm giá trị của $m$ để ba điểm $A, B, C$ thẳng hàng.\answerbox",
         "9.0cm", True),
        (None,
         r"Trong mặt phẳng tọa độ $Oxy$, cho hai vectơ $\vec{a} = (2; 1)$ và $\vec{b} = (-1; 3)$. Biết rằng vectơ $\vec{c} = (7; 7)$ được biểu diễn dưới dạng $\vec{c} = x\vec{a} + y\vec{b}$. Tính giá trị của $x^2 + y^2$.\answerbox",
         "9.0cm", False),

        # ==================== TRANG 19: CÂU 37 - 38 ====================
        (None,
         r"Trong mặt phẳng tọa độ $Oxy$, cho hai điểm $A(1; 3)$ và $B(5; -1)$. Điểm $M(x_M; 0)$ thuộc trục hoành $Ox$ sao cho tam giác $MAB$ cân tại đỉnh $M$. Tính giá trị của $x_M$.\answerbox",
         "9.0cm", True),
        (None,
         r"Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$ có $A(-2; 5)$, $B(1; 2)$ và $C(7; 10)$. Gọi $M, N$ lần lượt là trung điểm của các cạnh $AB$ và $AC$. Tính độ dài đoạn thẳng $MN$.\answerbox",
         "9.0cm", False),

        # ==================== TRANG 20: CÂU 39 - 40 ====================
        (None,
         r"Một ca nô chuyển động thẳng đều trên mặt biển gắn với hệ trục tọa độ $Oxy$ (đơn vị trên mỗi trục là kilômét). Lúc $7$ giờ sáng ca nô ở vị trí $A(3; 2)$, đến $9$ giờ sáng ca nô ở vị trí $B(9; 10)$. Nếu giữ nguyên vận tốc và hướng đi, đến $10$ giờ sáng cùng ngày ca nô ở vị trí $C(x_C; y_C)$. Tính giá trị của hoành độ $x_C$.\answerbox",
         "9.0cm", True),
        (None,
         r"Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A(1; 2)$, $B(3; 5)$ và $C(6; 1)$. Điểm $M(x_M; y_M)$ thỏa mãn đẳng thức vectơ $\vec{MA} + 2\vec{MB} - \vec{MC} = \vec{0}$. Tính giá trị của tổng $x_M + y_M$.\answerbox",
         "9.0cm", False),
    ]

    assert len(questions) == 40, f"Expected 40 questions, got {len(questions)}"
    return questions


def build_answers():
    # 4 columns x 10 rows:
    # Col 1: Q1 - Q10 (Chủ đề 1)
    # Col 2: Q11 - Q20 (Chủ đề 2)
    # Col 3: Q21 - Q30 (Chủ đề 3)
    # Col 4: Q31 - Q40 (Chủ đề 4)
    ans_map = {
        1: "90", 2: "4", 3: "2", 4: "5", 5: "5", 6: "7,5", 7: "32", 8: "4", 9: "10", 10: "5",
        11: "13", 12: "16", 13: "9", 14: "10", 15: "50", 16: "60", 17: "1000", 18: "13", 19: "6", 20: "14",
        21: "-3", 22: "1,5", 23: "6", 24: "7", 25: "5", 26: "5", 27: "6", 28: "5", 29: "40", 30: "3",
        31: "6", 32: "5", 33: "-7", 34: "21", 35: "3", 36: "17", 37: "2", 38: "5", 39: "12", 40: "6",
    }

    rows = []
    for r in range(1, 11):
        q1 = r
        q2 = r + 10
        q3 = r + 20
        q4 = r + 30
        row_str = (
            f"\\textbf{{{q1}}} & {ans_map[q1]} & "
            f"\\textbf{{{q2}}} & {ans_map[q2]} & "
            f"\\textbf{{{q3}}} & {ans_map[q3]} & "
            f"\\textbf{{{q4}}} & {ans_map[q4]} \\\\"
        )
        rows.append(row_str)

    table_tex = (
        r"\begin{center}" + "\n"
        r"\renewcommand{\arraystretch}{1.12}" + "\n"
        r"\begin{tabular}{|C{1.1cm}|C{2.0cm}|C{1.1cm}|C{2.0cm}|C{1.1cm}|C{2.0cm}|C{1.1cm}|C{2.0cm}|}" + "\n"
        r"\hline" + "\n"
        r"\textbf{Câu} & \textbf{Đáp án} & \textbf{Câu} & \textbf{Đáp án} & "
        r"\textbf{Câu} & \textbf{Đáp án} & \textbf{Câu} & \textbf{Đáp án} \\ \hline" + "\n"
        + " \\hline\n".join(rows) + " \\hline\n"
        r"\end{tabular}" + "\n"
        r"\end{center}"
    )

    sols = [
        # Q1 - Q10
        r"\textbf{Câu 1.} Mỗi cách chọn $2$ đỉnh có thứ tự từ $10$ đỉnh tạo thành một vectơ khác $\vec{0}$. Số vectơ là $A_{10}^2 = 10 \cdot 9 = \mathbf{90}$.",
        r"\textbf{Câu 2.} Đường thẳng $AB$ chứa $A, B \Rightarrow \vec{AB}, \vec{BA}$ ($2$ vectơ). Đường thẳng $CD$ chứa $C, D \Rightarrow \vec{CD}, \vec{DC}$ ($2$ vectơ). Tâm $O$ không nằm trên $AB, CD$. Vậy có $2 + 2 = \mathbf{4}$ vectơ.",
        r"\textbf{Câu 3.} Do $MN$ là đường trung bình của $\triangle ABC$ nên $\vec{MN} = \vec{BP} = \vec{PA}$. Vậy có $\mathbf{2}$ vectơ khác $\vec{MN}$ bằng nó.",
        r"\textbf{Câu 4.} Vectơ $\vec{AB}$ có độ dời ngang bằng $3$ và độ dời dọc bằng $4$. Độ dài $|\vec{u}| = \sqrt{3^2 + 4^2} = \mathbf{5}$.",
        r"\textbf{Câu 5.} Kẻ $BH \perp CD$ tại $H \Rightarrow DH = AB = 3\text{ cm} \Rightarrow HC = 7 - 3 = 4\text{ cm}$. Tam giác vuông $BHC$ có $BH = AD = 3\text{ cm} \Rightarrow BC = \sqrt{3^2 + 4^2} = \mathbf{5}\text{ cm}$.",
        r"\textbf{Câu 6.} Cạnh huyền $BC = \sqrt{9^2 + 12^2} = 15\text{ cm}$. Trung tuyến ứng với cạnh huyền $AM = \dfrac{1}{2}BC = \mathbf{7{,}5}\text{ cm}$.",
        r"\textbf{Câu 7.} Tam giác $ABC$ vuông cân có $AC = 8\sqrt{2}\text{ cm} \Rightarrow MN = \dfrac{1}{2}AC = 4\sqrt{2}\text{ cm}$. Do đó $|\vec{MN}|^2 = (4\sqrt{2})^2 = \mathbf{32}$.",
        r"\textbf{Câu 8.} $DE$ là đường trung bình của $\triangle ABC$ ứng với đáy $BC \Rightarrow DE = \dfrac{1}{2}BC = \dfrac{1}{2}\cdot 8 = \mathbf{4}$.",
        r"\textbf{Câu 9.} Cạnh $AD = \dfrac{48}{6} = 8\text{ cm}$. Đường chéo $BD = \sqrt{AB^2 + AD^2} = \sqrt{6^2 + 8^2} = \mathbf{10}\text{ cm}$.",
        r"\textbf{Câu 10.} Với điểm đầu cố định là $A$, có $5$ cách chọn điểm cuối trong các điểm còn lại. Vậy có $\mathbf{5}$ vectơ.",

        # Q11 - Q20
        r"\textbf{Câu 11.} $\vec{u} = \vec{AB} - \vec{CB} = \vec{AB} + \vec{BC} = \vec{AC} \Rightarrow |\vec{u}| = AC = \sqrt{5^2 + 12^2} = \mathbf{13}$.",
        r"\textbf{Câu 12.} Theo quy tắc hình bình hành: $\vec{AB} + \vec{AD} = \vec{AC}$. Giao điểm hai đường chéo $O$ cho $OB = 6\text{ cm} \Rightarrow OA = \sqrt{10^2 - 6^2} = 8\text{ cm} \Rightarrow AC = 16\text{ cm}$. Vậy $|\vec{w}| = \mathbf{16}$.",
        r"\textbf{Câu 13.} $\vec{x} = (\vec{AB} - \vec{AD}) + \vec{CD} = \vec{DB} + \vec{CD} = \vec{CD} + \vec{DB} = \vec{CB} \Rightarrow |\vec{x}| = BC = \mathbf{9}\text{ cm}$.",
        r"\textbf{Câu 14.} $\vec{y} = \vec{AB} - \vec{AD} = \vec{DB} \Rightarrow |\vec{y}| = BD = \sqrt{8^2 + 6^2} = \mathbf{10}$.",
        r"\textbf{Câu 15.} Hai lực vuông góc nên độ lớn hợp lực là $F = \sqrt{F_1^2 + F_2^2} = \sqrt{30^2 + 40^2} = \mathbf{50}\text{ N}$.",
        r"\textbf{Câu 16.} $F = \sqrt{60^2 + 60^2 + 2\cdot 60\cdot 60\cdot \cos 120^\circ} = \sqrt{3600 + 3600 - 3600} = \mathbf{60}\text{ N}$.",
        r"\textbf{Câu 17.} Vận tốc máy bay và vận tốc gió vuông góc nhau, vận tốc thực tế $v = \sqrt{600^2 + 800^2} = \mathbf{1000}\text{ km/h}$.",
        r"\textbf{Câu 18.} Vận tốc ca nô đối với bờ là hợp của hai vận tốc vuông góc: $v = \sqrt{12^2 + 5^2} = \mathbf{13}\text{ km/h}$.",
        r"\textbf{Câu 19.} $\vec{u} = \vec{AB} - \vec{AC} = \vec{CB} \Rightarrow |\vec{u}| = CB = \mathbf{6}\text{ cm}$.",
        r"\textbf{Câu 20.} $\vec{AB} + \vec{AD} = \vec{AC} \Rightarrow AC = |\vec{AB} + \vec{AD}| = \mathbf{14}$.",

        # Q21 - Q30
        r"\textbf{Câu 21.} Vì $M$ nằm giữa $A$ và $B$ nên $\vec{MA}$ và $\vec{MB}$ ngược hướng. Từ $MA = 3MB \Rightarrow \vec{MA} = -3\vec{MB} \Rightarrow k = \mathbf{-3}$.",
        r"\textbf{Câu 22.} $G$ là trọng tâm $\Rightarrow AG = \dfrac{2}{3}AM \Rightarrow AM = \dfrac{3}{2}AG \Rightarrow \vec{AM} = 1{,}5\vec{AG} \Rightarrow k = \mathbf{1{,}5}$.",
        r"\textbf{Câu 23.} $\vec{AK} = \dfrac{1}{2}(\vec{AM} + \vec{AN}) = \dfrac{1}{4}\vec{AB} + \dfrac{1}{6}\vec{AC} \Rightarrow x = \dfrac{1}{4},\; y = \dfrac{1}{6} \Rightarrow P = 12\left(\dfrac{1}{4}\right) + 18\left(\dfrac{1}{6}\right) = \mathbf{6}$.",
        r"\textbf{Câu 24.} Ta có $\vec{AD} = \dfrac{1}{4}\vec{AB} + \dfrac{3}{4}\vec{AC} \Rightarrow m = \dfrac{1}{4},\; n = \dfrac{3}{4}$. Vậy $S = 4\left(\dfrac{1}{4}\right) + 8\left(\dfrac{3}{4}\right) = 1 + 6 = \mathbf{7}$.",
        r"\textbf{Câu 25.} $\vec{MA} + 4\vec{MB} = 5\vec{MI} + (\vec{IA} + 4\vec{IB}) = 5\vec{MI} \Rightarrow k = \mathbf{5}$.",
        r"\textbf{Câu 26.} $\vec{BG} = \dfrac{1}{3}\vec{BA} + \dfrac{1}{3}\vec{BC}$. Do $I$ là trung điểm $AG$ nên $\vec{BI} = \dfrac{1}{2}(\vec{BA} + \vec{BG}) = \dfrac{2}{3}\vec{BA} + \dfrac{1}{6}\vec{BC} \Rightarrow a = \dfrac{2}{3},\; b = \dfrac{1}{6} \Rightarrow T = 6\left(\dfrac{2}{3}\right) + 6\left(\dfrac{1}{6}\right) = 4 + 1 = \mathbf{5}$.",
        r"\textbf{Câu 27.} Ta có $|\vec{MA} + \vec{MB} + \vec{MC}| = |3\vec{MG}| = 3MG = 18\text{ cm} \Leftrightarrow MG = 6\text{ cm}$. Vậy bán kính đường tròn $R = \mathbf{6}\text{ cm}$.",
        r"\textbf{Câu 28.} $|\vec{MA} + \vec{MB} + \vec{MC} + \vec{MD}| = |4\vec{MO}| = 4MO = 20\text{ cm} \Leftrightarrow MO = 5\text{ cm}$. Vậy bán kính đường tròn $R = \mathbf{5}\text{ cm}$.",
        r"\textbf{Câu 29.} Gọi góc hợp bởi mỗi dây với phương thẳng đứng là $60^\circ$. Điều kiện cân bằng lực: $2T\cos 60^\circ = P \Leftrightarrow 2T \cdot 0{,}5 = 40 \Leftrightarrow T = \mathbf{40}\text{ N}$.",
        r"\textbf{Câu 30.} Kẻ $MK \parallel BP$ ($K \in AC$) được $P$ là trung điểm của $CK$ và $AK$. Do đó $AP = PK = KC \Rightarrow AC = 3AP \Rightarrow k = \mathbf{3}$.",

        # Q31 - Q40
        r"\textbf{Câu 31.} $x_G = \dfrac{1 + 3 + 5}{3} = 3$, $y_G = \dfrac{4 - 2 + 7}{3} = 3 \Rightarrow x_G + y_G = 3 + 3 = \mathbf{6}$.",
        r"\textbf{Câu 32.} Trung điểm $M$ có tọa độ $M(3; 4) \Rightarrow OM = \sqrt{3^2 + 4^2} = \mathbf{5}$.",
        r"\textbf{Câu 33.} $ABCD$ là hình bình hành $\Leftrightarrow \vec{AD} = \vec{BC} \Leftrightarrow (x_D - 1; y_D - 2) = (-6; -3) \Leftrightarrow D(-5; -1)$. Vậy $x_D + 2y_D = -5 + 2(-1) = \mathbf{-7}$.",
        r"\textbf{Câu 34.} $\vec{w} = (3\cdot 2 - 2\cdot 1;\; 3(-3) - 2\cdot 4) = (4; -17) \Rightarrow x_0 - y_0 = 4 - (-17) = \mathbf{21}$.",
        r"\textbf{Câu 35.} $\vec{AB} = (3; 6)$, $\vec{AC} = (m - 2; 2)$. Ba điểm thẳng hàng $\Leftrightarrow \dfrac{m - 2}{3} = \dfrac{2}{6} = \dfrac{1}{3} \Leftrightarrow m - 2 = 1 \Leftrightarrow m = \mathbf{3}$.",
        r"\textbf{Câu 36.} Ta có hệ $2x - y = 7$ và $x + 3y = 7 \Leftrightarrow x = 4,\; y = 1 \Rightarrow x^2 + y^2 = 4^2 + 1^2 = \mathbf{17}$.",
        r"\textbf{Câu 37.} $MA^2 = MB^2 \Leftrightarrow (x_M - 1)^2 + 9 = (x_M - 5)^2 + 1 \Leftrightarrow 8x_M = 16 \Leftrightarrow x_M = \mathbf{2}$.",
        r"\textbf{Câu 38.} $MN$ là đường trung bình của $\triangle ABC \Rightarrow MN = \dfrac{1}{2}BC = \dfrac{1}{2}\sqrt{(7 - 1)^2 + (10 - 2)^2} = \dfrac{1}{2}\sqrt{100} = \mathbf{5}$.",
        r"\textbf{Câu 39.} Trong $2\text{ h}$ ca nô đi vectơ $\vec{AB} = (6; 8) \Rightarrow$ vận tốc $\vec{v} = (3; 4)\text{ km/h}$. Thêm $1\text{ h}$ đến $10\text{h}$, tọa độ $C = B + \vec{v} = (9 + 3; 10 + 4) = (12; 14) \Rightarrow x_C = \mathbf{12}$.",
        r"\textbf{Câu 40.} $\vec{MA} + 2\vec{MB} - \vec{MC} = \vec{0} \Leftrightarrow \vec{OM} = \dfrac{\vec{OA} + 2\vec{OB} - \vec{OC}}{2}$. Tọa độ $x_M = \dfrac{1 + 6 - 6}{2} = 0{,}5$; $y_M = \dfrac{2 + 10 - 1}{2} = 5{,}5 \Rightarrow x_M + y_M = \mathbf{6}$.",
    ]
    assert len(sols) == 40, f"Expected 40 solutions, got {len(sols)}"
    return table_tex, sols


def generate_tex(exam_pages_str: str = "XX", ans_pages_str: str = "YY") -> str:
    questions = build_questions()
    table_tex, sols = build_answers()

    preamble = PREAMBLE.replace("__HEADER_QUOTE__", build_header_quote_macro(40))
    preamble = preamble.replace("__EXAM_PAGES__", exam_pages_str)
    preamble = preamble.replace("__ANS_PAGES__", ans_pages_str)

    parts = [preamble, r"\begin{document}"]

    parts.append(r"""\begin{center}
  {\Large\bfseries\color{ink} ĐỀ CƯƠNG ÔN TẬP CHƯƠNG IV — VECTƠ (40 CÂU)}\\[3pt]
  {\small\color{gray!75!black} \textit{Hình thức: 40 câu trả lời ngắn (Bài 7, 8, 9, 10 — Sách Kết nối tri thức với cuộc sống)}}
\end{center}
\vspace{2pt}""")

    parts.append(r"""\chapterbanner{ÔN TẬP KIẾN THỨC TRỌNG TÂM: BÀI 7 ĐẾN BÀI 10}{(Học sinh trình bày tóm tắt các bước giải vào khung ô li và điền đáp số cuối cùng vào ô tương ứng)}""")

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

    parts.append(r"""
\newpage
\pagestyle{dapan}
\setcounter{page}{1}
\begin{center}
  {\Large\bfseries\color{ink} BẢNG ĐÁP ÁN \& HƯỚNG DẪN GIẢI CHI TIẾT}\\[3pt]
  {\small\color{gray!75!black} Đề cương ôn tập Toán 10 — Chương IV: Vectơ (Bài 7, 8, 9, 10 — 40 câu trả lời ngắn)}
\end{center}
\vspace{2pt}
""")
    parts.append(table_tex)
    parts.append(r"\vspace{2pt}")
    parts.append(r"\setlength{\columnsep}{16pt}")
    parts.append(r"\parttitle{HƯỚNG DẪN GIẢI CHI TIẾT (CÂU 1 – CÂU 40)}")
    parts.append(r"\begin{multicols}{2}")
    parts.append(r"\small\sloppy")
    for s in sols:
        parts.append(r"\needspace{2\baselineskip}" + s + r"\par\vspace{2.5pt}")
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
        if "BẢNG ĐÁP ÁN" in txt or ("1000" in txt and "-3" in txt and "7,5" in txt):
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
    expected = list(range(1, 41))
    if seen_qs != expected:
        missing = set(expected) - set(seen_qs)
        raise RuntimeError(f"Question numbering mismatch! Missing={missing}")
    if not all_ok:
        raise RuntimeError("Some question text was split across pages from its grid box!")
    print("Pagination check PASSED: 40 questions, 0 split boxes!")


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

    audit_pagination(EXAM_PDF)

    print("[4/4] Exporting PDFs to Grade 10 teaching folders...")
    src_map = {"exam": EXAM_PDF, "ans": ANS_PDF, "full": FULL_PDF}
    for dst, kind in EXPORT_TARGETS:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_map[kind], dst)
        print(f"  Copied -> {dst}")

    print("\nBUILD COMPLETE!")


if __name__ == "__main__":
    main()
