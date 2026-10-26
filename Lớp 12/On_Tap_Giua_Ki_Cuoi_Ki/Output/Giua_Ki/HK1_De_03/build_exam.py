"""Tạo mã XeLaTeX và đáp án cho Đề ôn giữa kì I số 03."""
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent

KEY = {
    "I": [
        "B", "A", "C", "D", "A", "C", "D", "B", "C", "D", "A", "B"
    ],
    "II": [
        [True, False, True, True],
        [True, True, True, False],
        [True, True, False, True],
        [True, True, False, True]
    ],
    "III": [
        "12",
        "14",
        "1",
        "3",
        "108",
        "2"
    ]
}

(BASE / "dap_an.json").write_text(json.dumps(KEY, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

latex_content = r"""% !TeX program = xelatex
\documentclass[12pt,a4paper]{article}
\usepackage{fontspec}
\setmainfont{Times New Roman}[Path=C:/Windows/Fonts/,UprightFont=times.ttf,BoldFont=timesbd.ttf,ItalicFont=timesi.ttf,BoldItalicFont=timesbi.ttf]
\usepackage{amsmath,amssymb,amsfonts}
\usepackage[left=1.5cm,right=1.5cm,top=1.5cm,bottom=1.7cm,headheight=17pt]{geometry}
\usepackage{enumitem,array,graphicx,tikz,fancyhdr,needspace}
\usetikzlibrary{arrows.meta,calc,patterns}
\newcommand{\soDe}{3}
\newcommand{\soTrangDe}{4}
\newcommand{\maDe}{\ifnum\soDe<1000 0\fi\ifnum\soDe<100 0\fi\ifnum\soDe<10 0\fi\soDe}
\pagestyle{fancy}
\fancyhf{}
\lhead{\small\textbf{ÔN TẬP GIỮA KÌ I}}
\rhead{\small\textit{Biên soạn: Dương Gia Bảo}}
\rfoot{\small Trang \thepage/\soTrangDe\ - Mã đề: \maDe}
\renewcommand{\headrulewidth}{0.4pt}
\fancypagestyle{answers}{\rfoot{\small Trang \thepage\ - Mã đề: \maDe}}
\fancypagestyle{firstpage}{\fancyhead{}\renewcommand{\headrulewidth}{0pt}}
\setlength{\parindent}{0pt}
\setlength{\parskip}{3pt}
\setlength{\emergencystretch}{1em}
\setlist[enumerate,1]{label=\textbf{Câu \arabic*:},leftmargin=*,itemsep=8pt,topsep=5pt}
\setlist[enumerate,2]{label=\alph*),leftmargin=*,itemsep=3pt,topsep=3pt}
\newcommand{\bonpa}[4]{\par\nobreak\smallskip\nobreak\noindent
\begin{tabular}{@{}p{0.47\linewidth}p{0.47\linewidth}@{}}
\textbf{A.} #1 & \textbf{B.} #2\\[8pt]
\textbf{C.} #3 & \textbf{D.} #4\end{tabular}}
\newcommand{\loigiai}[1]{\par\medskip\Needspace{4\baselineskip}\noindent\textbf{#1}\par\nobreak}
\newcommand{\otraloi}{\par\nobreak\smallskip\noindent\textit{Trả lời:}\quad\fbox{\rule{0pt}{11pt}\makebox[0.3cm]{}}\,\fbox{\rule{0pt}{11pt}\makebox[0.3cm]{}}\,\fbox{\rule{0pt}{11pt}\makebox[0.3cm]{}}\,\fbox{\rule{0pt}{11pt}\makebox[0.3cm]{}}}
\begin{document}
\thispagestyle{firstpage}
\noindent
\begin{minipage}[t]{0.35\textwidth}
    \centering
    {\fontsize{13}{15}\selectfont\textbf{ÔN TẬP GIỮA KÌ I}}\\[5pt]
    \textit{Biên soạn: Dương Gia Bảo}\\[6pt]
    \setlength{\fboxrule}{0.8pt}%
    \setlength{\fboxsep}{5pt}%
    \fbox{\begin{minipage}{0.83\linewidth}
        \centering
        {\fontsize{13}{15}\selectfont\textbf{ĐỀ ÔN TẬP}\\[2pt]\textbf{CHƯƠNG I VÀ II}}\\[5pt]
        \textit{(Đề thi gồm có \ifnum\soTrangDe<10 0\fi\soTrangDe\ trang)}
    \end{minipage}}
\end{minipage}\hfill
\begin{minipage}[t]{0.63\textwidth}
    \centering
    {\fontsize{13}{15}\selectfont\textbf{ÔN TẬP KIỂM TRA GIỮA KÌ I}\\[2pt]
    \textbf{NĂM HỌC 2026 - 2027}}\\[6pt]
    {\fontsize{14}{16}\selectfont\textbf{Môn: TOÁN - Lớp 12 (ĐỀ SỐ \soDe)}}\\[5pt]
    {\fontsize{11.5}{13}\selectfont\textit{Thời gian làm bài: 90 phút, không kể thời gian giao đề}}\\[6pt]
    \setlength{\fboxrule}{0.8pt}%
    \setlength{\fboxsep}{6pt}%
    \fbox{\makebox[3cm]{\fontsize{14}{16}\selectfont\textbf{Mã đề: \maDe}}}
\end{minipage}
\par\vspace{3pt}
\hrule height 0.6pt
\vspace{4pt}
\noindent\textit{Họ và tên học sinh:}\dotfill\hspace{1cm}\textit{Lớp:}\makebox[3.5cm]{\dotfill}
\par\vspace{3pt}
\hrule height 0.6pt
\vspace{4pt}

\vspace{3pt}
\section*{\large PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn}
\textit{Thí sinh trả lời từ câu 1 đến câu 12. Mỗi câu chỉ chọn một phương án.}
\begin{enumerate}
\item Cho hàm số $y=-x^3+3x^2-4$. Hàm số đã cho đồng biến trên khoảng nào dưới đây?
\bonpa{$(-\infty;0)$.}{$(0;2)$.}{$(2;+\infty)$.}{$(-1;1)$.}

\item Điểm cực tiểu của hàm số $y=x^3-3x^2-9x+2$ là
\bonpa{$x=3$.}{$x=-1$.}{$x=-25$.}{$x=7$.}

\item Giá trị nhỏ nhất của hàm số $f(x)=\dfrac{x-2}{x+1}$ trên đoạn $[0;3]$ bằng
\bonpa{$\dfrac{1}{4}$.}{$0$.}{$-2$.}{$1$.}

\item Đường tiệm cận đứng của đồ thị hàm số $y=\dfrac{3x-1}{x-2}$ có phương trình là
\bonpa{$x=3$.}{$y=3$.}{$y=2$.}{$x=2$.}

\item Đường tiệm cận xiên của đồ thị hàm số $y=\dfrac{2x^2-3x+2}{x-1}$ có phương trình là
\bonpa{$y=2x-1$.}{$y=2x+1$.}{$y=x-1$.}{$y=2x$.}

\item Đường cong trong hình bên là đồ thị của hàm số nào dưới đây?
\par\nobreak\smallskip
\begin{minipage}[c]{0.60\linewidth}
\bonpa{$y=\dfrac{x^2+x+1}{x+1}$.}{$y=\dfrac{-x^2+x-1}{x-1}$.}{$y=\dfrac{x^2-x+1}{x-1}$.}{$y=\dfrac{x^2-2x+2}{x-1}$.}
\end{minipage}\hfill
\begin{minipage}[c]{0.38\linewidth}\centering
\begin{tikzpicture}[x=0.55cm,y=0.40cm,>=Stealth]
\draw[->] (-2.2,0)--(3.6,0) node[right] {$x$};
\draw[->] (0,-3.4)--(0,3.9) node[above] {$y$};
\draw[dashed,gray] (1,-3.2)--(1,3.6);
\draw[dashed,gray] (-1.8,-1.8)--(3.2,3.2);
\draw[dashed,gray] (2,0)--(2,3)--(0,3);
\draw[very thick,blue!65!black,domain=-1.8:0.7,samples=70] plot (\x,{(\x*\x-\x+1)/(\x-1)});
\draw[very thick,blue!65!black,domain=1.3:3.2,samples=70] plot (\x,{(\x*\x-\x+1)/(\x-1)});
\fill (0,-1) circle (1.5pt);\fill (2,3) circle (1.5pt);
\node[above left,fill=white,inner sep=0.5pt] at (0,0) {$O$};
\node[below left,fill=white,inner sep=0.5pt] at (0,-1) {$-1$};
\node[below,fill=white,inner sep=0.5pt] at (1,0) {$1$};
\node[below,fill=white,inner sep=0.5pt] at (2,0) {$2$};
\node[left,fill=white,inner sep=0.5pt] at (0,3) {$3$};
\end{tikzpicture}
\end{minipage}
\end{enumerate}

\newpage
\begin{enumerate}[start=7]
\item Một doanh nghiệp sản xuất một loại sản phẩm. Chi phí trung bình cho mỗi sản phẩm khi sản xuất $x$ sản phẩm ($x\ge1$, $x$ là số nguyên) được cho bởi $C(x)=\dfrac{2x^2+50}{x}$ (nghìn đồng/sản phẩm). Để chi phí trung bình trên mỗi sản phẩm là thấp nhất thì doanh nghiệp cần sản xuất bao nhiêu sản phẩm?
\bonpa{$10$.}{$25$.}{$2$.}{$5$.}

\item Cho hình hộp $ABCD.A'B'C'D'$. Vectơ $\overrightarrow{AB}+\overrightarrow{AD}+\overrightarrow{AA'}$ bằng
\bonpa{$\overrightarrow{AC}$.}{$\overrightarrow{AC'}$.}{$\overrightarrow{CA'}$.}{$\overrightarrow{BD'}$.}

\item Trong không gian $Oxyz$, cho vectơ $\vec a=2\vec i-3\vec j+\vec k$. Tọa độ của vectơ $\vec a$ là
\bonpa{$(-3;2;1)$.}{$(2;1;-3)$.}{$(2;-3;1)$.}{$(-2;3;-1)$.}

\item Trong không gian $Oxyz$, cho hai vectơ $\vec u=(1;2;-1)$ và $\vec v=(-2;1;3)$. Tích vô hướng $\vec u\cdot\vec v$ bằng
\bonpa{$3$.}{$7$.}{$1$.}{$-3$.}

\item Trong không gian $Oxyz$, cho hai điểm $M(1;-1;2)$ và $N(3;1;3)$. Độ dài đoạn thẳng $MN$ bằng
\bonpa{$3$.}{$9$.}{$\sqrt5$.}{$\sqrt{13}$.}

\item Trong không gian $Oxyz$, cho tam giác $ABC$ với $A(2;1;-3)$, $B(0;-2;5)$ và $C(4;4;1)$. Tọa độ trọng tâm $G$ của tam giác $ABC$ là
\bonpa{$(6;3;3)$.}{$(2;1;1)$.}{$(1;2;1)$.}{$(2;-1;1)$.}
\end{enumerate}

\section*{\large PHẦN II. Câu trắc nghiệm đúng hoặc sai}
\textit{Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d), chọn đúng hoặc sai.}
\begin{enumerate}
\Needspace{8\baselineskip}
\item Cho hàm số $f(x)=\dfrac{x^2-3x+6}{x-2}$ xác định trên $\mathbb R\setminus\{2\}$.
\begin{enumerate}
\item $f'(x)=\dfrac{x(x-4)}{(x-2)^2}$ với mọi $x\ne2$.
\item Hàm số nghịch biến trên khoảng $(0;4)$.
\item Đồ thị hàm số có tiệm cận xiên là đường thẳng $y=x-1$.
\item Khoảng cách giữa hai điểm cực trị của đồ thị hàm số bằng $4\sqrt5$.
\end{enumerate}
\end{enumerate}

\newpage
\begin{enumerate}[start=2]
\Needspace{9\baselineskip}
\item Một công ty du lịch tổ chức tour tham quan với số lượng khách đăng ký $x$ thỏa mãn $20\le x\le120$ ($x$ là số nguyên). Giá vé cho mỗi khách hàng là $p(x)=1500-5x$ (nghìn đồng). Tổng chi phí tổ chức tour gồm chi phí cố định 12 triệu đồng và chi phí phục vụ $300$ nghìn đồng cho mỗi khách: $C(x)=300x+12000$ (nghìn đồng).
\begin{enumerate}
\item Doanh thu của công ty thu được từ tour du lịch là $R(x)=-5x^2+1500x$ (nghìn đồng).
\item Lợi nhuận của chuyến du lịch được tính bởi công thức $P(x)=-5x^2+1200x-12000$ (nghìn đồng).
\item Lợi nhuận của công ty đạt giá trị lớn nhất khi có đúng $120$ khách đăng ký tham gia tour.
\item Lợi nhuận lớn nhất mà công ty thu được từ chuyến du lịch là $50$ triệu đồng.
\end{enumerate}

\Needspace{9\baselineskip}
\item Trong không gian $Oxyz$, cho ba điểm $A(2;1;-1)$, $B(0;3;1)$ và $C(4;5;3)$.
\begin{enumerate}
\item Tọa độ của vectơ $\overrightarrow{AB}$ là $(-2;2;2)$.
\item Độ dài đoạn thẳng $AC$ bằng $6$.
\item Tam giác $ABC$ vuông tại đỉnh $A$.
\item Tọa độ điểm $D$ để tứ giác $ABCD$ là hình bình hành là $D(6;3;1)$.
\end{enumerate}

\Needspace{9\baselineskip}
\item Một chiếc đèn chùm trang trí có khối lượng $m=6$ kg được treo giữ thăng bằng bởi ba sợi dây cáp nhẹ có chiều dài bằng nhau xuất phát từ điểm buộc đèn $S$ đến ba điểm neo $A,B,C$ trên trần nhà phẳng nằm ngang. Chọn hệ tọa độ $Oxyz$ có mặt phẳng $(Oxy)$ trùng với trần nhà, trục $Oz$ hướng thẳng đứng xuống dưới, gia tốc trọng trường $g=10\text{ m/s}^2$. Trọng lực tác dụng lên đèn là $\vec P=(0;0;60)$ (đơn vị N). Vị trí điểm buộc đèn là $S(0;0;4)$ (đơn vị mét). Ba điểm neo có tọa độ $A(0;3;0)$, $B\left(-\dfrac{3\sqrt3}{2};-\dfrac{3}{2};0\right)$, $C\left(\dfrac{3\sqrt3}{2};-\dfrac{3}{2};0\right)$.
\begin{enumerate}
\item Trọng lực tác dụng lên đèn có độ lớn bằng $60$ N.
\item Chiều dài của mỗi sợi dây cáp từ điểm neo đến điểm buộc đèn bằng $5$ m.
\item Độ lớn lực căng của mỗi sợi dây cáp bằng $30$ N.
\item Lực căng dây $\vec T_1$ từ $S$ đến $A$ tác dụng lên đèn có tọa độ là $(0;15;-20)$.
\end{enumerate}
\end{enumerate}

\section*{\large PHẦN III. Câu trắc nghiệm trả lời ngắn}
\textit{Thí sinh trả lời từ câu 1 đến câu 6. Ghi kết quả vào các ô trả lời; dùng dấu phẩy cho phần thập phân.}
\begin{enumerate}
\item Có bao nhiêu giá trị nguyên của tham số $m$ thuộc đoạn $[-10;10]$ để hàm số $y=\dfrac{x+3m}{x+6}$ đồng biến trên từng khoảng xác định của nó?
\otraloi

\item Trong không gian $Oxyz$, cho hình hộp $ABCD.A'B'C'D'$ có $A(1;0;1)$, $B(2;1;2)$, $D(1;3;0)$ và $A'(3;2;4)$. Biết đỉnh $C'$ có tọa độ $(a;b;c)$, tính giá trị của biểu thức $a+b+c$.
\otraloi
\end{enumerate}

\newpage
\begin{enumerate}[start=3]
\item Cho hàm số $y=x^3-3mx^2+4m^3$ với $m>0$. Đồ thị hàm số có hai điểm cực trị $A$ và $B$. Tìm giá trị của tham số $m$ để khoảng cách giữa hai điểm cực trị bằng $2\sqrt5$.
\otraloi

\item Trong không gian $Oxyz$ (đơn vị trên các trục tính bằng kilômét), tại cùng một thời điểm, hai thiết bị bay không người lái xuất phát và chuyển động thẳng đều. Vị trí của thiết bị thứ nhất sau $t$ giờ ($0\le t\le4$) là $A_t(t;2t;2t-1)$ và vị trí của thiết bị thứ hai là $B_t(3t-2;3t-4;4)$. Khoảng cách ngắn nhất giữa hai thiết bị trong khoảng thời gian trên bằng bao nhiêu kilômét?
\otraloi

\item Một bể chứa nước dạng hình hộp chữ nhật không nắp có thể tích bằng $288\text{ m}^3$. Đáy bể là hình chữ nhật có chiều dài gấp đôi chiều rộng. Chi phí xây dựng cho mỗi mét vuông đáy bể và thành bể (gồm 4 mặt bên) là như nhau, bằng $500$ nghìn đồng/m$^2$. Chi phí xây dựng thấp nhất của bể chứa đó bằng bao nhiêu triệu đồng?
\otraloi

\item Một người đang ở vị trí $A$ trên bờ biển thẳng, cần đến một hòn đảo ở vị trí $B$ cách bờ biển $6$ km. Gọi $C$ là hình chiếu vuông góc của $B$ lên bờ biển, biết khoảng cách $AC=12$ km. Người đó chạy bộ dọc theo bờ biển từ $A$ đến điểm $M$ (nằm giữa $A$ và $C$) với vận tốc $10$ km/h, sau đó chèo thuyền thẳng từ $M$ đến $B$ với vận tốc $6$ km/h. Thời gian ngắn nhất để người đó di chuyển từ $A$ đến $B$ bằng bao nhiêu giờ?
\par\smallskip
\begin{center}
\begin{tikzpicture}[x=0.55cm,y=0.55cm,>=Stealth]
\fill[blue!7] (-0.5,-0.2) rectangle (13.5,-2.5);
\draw[very thick,brown!65!black] (-0.5,0)--(13.5,0) node[right,black,font=\small] {Bờ biển};
\node[blue!75!black,font=\small] at (6,-1.3) {Biển};
\coordinate (A) at (0,0);
\coordinate (C) at (12,0);
\coordinate (M) at (7.5,0);
\coordinate (B) at (12,-2.2);
\fill (A) circle (1.8pt) node[above] {$A$};
\fill (C) circle (1.8pt) node[above] {$C$};
\fill (M) circle (1.8pt) node[above] {$M$};
\fill (B) circle (1.8pt) node[below right] {$B$ (Đảo)};
\draw[thick,red!80!black,->] (A)--(M);
\draw[thick,red!80!black,dashed,->] (M)--(B);
\draw[dashed,gray] (C)--(B);
\draw (11.6,0)--(11.6,-0.4)--(12,-0.4);
\draw[<->] (0,0.6)--(12,0.6) node[midway,above,font=\small] {$12\text{ km}$};
\draw[<->] (12.4,0)--(12.4,-2.2) node[midway,right,font=\small] {$6\text{ km}$};
\end{tikzpicture}
\end{center}
\otraloi
\end{enumerate}
\begin{center}\textbf{---------------- HẾT ----------------}\end{center}

\newpage\pagestyle{answers}
\begin{center}\Large\textbf{BẢNG ĐÁP ÁN TỔNG HỢP}\end{center}
\textbf{Phần I. Trắc nghiệm nhiều phương án lựa chọn}
\begin{center}
\renewcommand{\arraystretch}{1.5}
\begin{tabular}{|c|*{12}{c|}}\hline
Câu & 1&2&3&4&5&6&7&8&9&10&11&12\\\hline
Đáp án & B & A & C & D & A & C & D & B & C & D & A & B \\\hline
\end{tabular}
\end{center}

\textbf{Phần II. Đúng hoặc sai}
\begin{center}
\renewcommand{\arraystretch}{1.4}
\begin{tabular}{|c|c|c|c|c|}\hline
Câu & a) & b) & c) & d)\\\hline
1 & Đ & S & Đ & Đ\\\hline
2 & Đ & Đ & Đ & S\\\hline
3 & Đ & Đ & S & Đ\\\hline
4 & Đ & Đ & S & Đ\\\hline
\end{tabular}
\end{center}

\textbf{Phần III. Trả lời ngắn}
\begin{center}
\renewcommand{\arraystretch}{1.5}
\begin{tabular}{|c|*{6}{c|}}\hline
Câu & 1 & 2 & 3 & 4 & 5 & 6\\\hline
Đáp án & 12 & 14 & 1 & 3 & 108 & 2\\\hline
\end{tabular}
\end{center}

\newpage
\begin{center}\Large\textbf{HƯỚNG DẪN GIẢI CHI TIẾT}\end{center}

\section*{PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn}

\loigiai{Câu 1: Chọn B.}
Tập xác định: $D=\mathbb R$. Ta có $y'=-3x^2+6x=-3x(x-2)$.\\
Xét dấu $y'$: $y'>0\iff 0<x<2$; $y'<0\iff x<0$ hoặc $x>2$.\\
Vậy hàm số đồng biến trên khoảng $(0;2)$.

\loigiai{Câu 2: Chọn A.}
Tập xác định: $D=\mathbb R$. Đạo hàm $y'=3x^2-6x-9=3(x^2-2x-3)=3(x+1)(x-3)$.\\
$y'=0\iff x=-1$ hoặc $x=3$.\\
Đạo hàm cấp hai: $y''=6x-6$.\\
Tại $x=3$, $y''(3)=12>0$ nên hàm số đạt cực tiểu tại $x=3$.\\
Tại $x=-1$, $y''(-1)=-12<0$ nên hàm số đạt cực đại tại $x=-1$.

\loigiai{Câu 3: Chọn C.}
Hàm số liên tục trên đoạn $[0;3]$. Đạo hàm $f'(x)=\dfrac{1\cdot1-(-2)\cdot1}{(x+1)^2}=\dfrac{3}{(x+1)^2}>0$ với mọi $x\in[0;3]$.\\
Do đó hàm số đồng biến trên đoạn $[0;3]$.\\
Giá trị nhỏ nhất là $\min_{[0;3]}f(x)=f(0)=\dfrac{0-2}{0+1}=-2$.

\loigiai{Câu 4: Chọn D.}
Ta có $\lim_{x\to2^+}\dfrac{3x-1}{x-2}=+\infty$ và $\lim_{x\to2^-}\dfrac{3x-1}{x-2}=-\infty$.\\
Do đó đường thẳng $x=2$ là tiệm cận đứng của đồ thị hàm số.

\loigiai{Câu 5: Chọn A.}
Thực hiện phép chia đa thức:
\[ y=\dfrac{2x^2-3x+2}{x-1}=\dfrac{(2x-1)(x-1)+1}{x-1}=2x-1+\dfrac{1}{x-1} \]
Vì $\lim_{x\to\pm\infty}[y-(2x-1)]=\lim_{x\to\pm\infty}\dfrac{1}{x-1}=0$, nên đường tiệm cận xiên của đồ thị là $y=2x-1$.

\loigiai{Câu 6: Chọn C.}
Đồ thị hàm số có tiệm cận đứng $x=1$ và cắt trục tung tại điểm $(0;-1)$.\\
Trong các hàm số đã cho:
- Hàm số $y=\dfrac{x^2+x+1}{x+1}$ có tiệm cận đứng $x=-1$ (loại A).
- Hàm số $y=\dfrac{-x^2+x-1}{x-1}$ có đồ thị cắt $Oy$ tại điểm $(0;1)$ (loại B).
- Hàm số $y=\dfrac{x^2-x+1}{x-1}=x+\dfrac{1}{x-1}$ có tiệm cận đứng $x=1$, tiệm cận xiên $y=x$, đạo hàm $y'=1-\dfrac{1}{(x-1)^2}=0\iff x=0$ hoặc $x=2$. Điểm cực đại là $(0;-1)$, điểm cực tiểu là $(2;3)$, hoàn toàn khớp với hình vẽ.
- Hàm số $y=\dfrac{x^2-2x+2}{x-1}$ cắt $Oy$ tại $(0;-2)$ (loại D).

\loigiai{Câu 7: Chọn D.}
Với $x\ge1$, ta có $C(x)=2x+\dfrac{50}{x}$.\\
Áp dụng bất đẳng thức Cauchy cho hai số dương $2x$ và $\dfrac{50}{x}$:
\[ C(x)=2x+\dfrac{50}{x}\ge2\sqrt{2x\cdot\dfrac{50}{x}}=2\sqrt{100}=20 \]
Dấu bằng xảy ra khi $2x=\dfrac{50}{x}\iff x^2=25\iff x=5$ (do $x\ge1$).\\
Vậy để chi phí trung bình thấp nhất, doanh nghiệp cần sản xuất $5$ sản phẩm.

\loigiai{Câu 8: Chọn B.}
Theo quy tắc hình bình hành ở đáy $ABCD$: $\overrightarrow{AB}+\overrightarrow{AD}=\overrightarrow{AC}$.\\
Theo quy tắc hình bình hành trong mặt phẳng chéo $(ACC'A')$: $\overrightarrow{AC}+\overrightarrow{AA'}=\overrightarrow{AC'}$.\\
Vậy $\overrightarrow{AB}+\overrightarrow{AD}+\overrightarrow{AA'}=\overrightarrow{AC'}$.

\loigiai{Câu 9: Chọn C.}
Trong hệ tọa độ $Oxyz$, với $\vec a=2\vec i-3\vec j+\vec k$, theo định nghĩa tọa độ vectơ ta có $\vec a=(2;-3;1)$.

\loigiai{Câu 10: Chọn D.}
Tích vô hướng của hai vectơ:
\[ \vec u\cdot\vec v=1\cdot(-2)+2\cdot1+(-1)\cdot3=-2+2-3=-3 \]

\loigiai{Câu 11: Chọn A.}
Ta có $\overrightarrow{MN}=(3-1;1-(-1);3-2)=(2;2;1)$.\\
Độ dài đoạn thẳng $MN$ là $MN=|\overrightarrow{MN}|=\sqrt{2^2+2^2+1^2}=\sqrt{4+4+1}=\sqrt9=3$.

\loigiai{Câu 12: Chọn B.}
Tọa độ trọng tâm $G$ của tam giác $ABC$ là:
\[ x_G=\dfrac{2+0+4}{3}=2,\quad y_G=\dfrac{1+(-2)+4}{3}=1,\quad z_G=\dfrac{-3+5+1}{3}=1 \]
Vậy $G(2;1;1)$.

\section*{PHẦN II. Câu trắc nghiệm đúng hoặc sai}

\loigiai{Câu 1:}
a) \textbf{Đúng.} Ta có:
\[ f'(x)=\dfrac{(2x-3)(x-2)-(x^2-3x+6)\cdot1}{(x-2)^2}=\dfrac{2x^2-7x+6-x^2+3x-6}{(x-2)^2}=\dfrac{x^2-4x}{(x-2)^2}=\dfrac{x(x-4)}{(x-2)^2} \]
với mọi $x\ne2$.\\
b) \textbf{Sai.} Phương trình $f'(x)=0\iff x=0$ hoặc $x=4$. Trên khoảng $(0;4)$, đạo hàm $f'(x)<0$ với mọi $x\ne2$, nhưng hàm số không xác định tại $x=2$. Do đó hàm số nghịch biến trên từng khoảng $(0;2)$ và $(2;4)$, khẳng định nghịch biến trên cả khoảng $(0;4)$ là sai.\\
c) \textbf{Đúng.} Ta có $f(x)=x-1+\dfrac{4}{x-2}$.\\
Vì $\lim_{x\to\pm\infty}[f(x)-(x-1)]=\lim_{x\to\pm\infty}\dfrac{4}{x-2}=0$, nên đường tiệm cận xiên của đồ thị là $y=x-1$.\\
d) \textbf{Đúng.} Điểm cực đại của đồ thị là $M(0;-3)$, điểm cực tiểu là $N(4;5)$. Khoảng cách giữa hai điểm cực trị là:
\[ MN=\sqrt{(4-0)^2+(5-(-3))^2}=\sqrt{16+64}=\sqrt{80}=4\sqrt5 \]

\loigiai{Câu 2:}
a) \textbf{Đúng.} Doanh thu khi bán $x$ vé là $R(x)=x\cdot p(x)=x(1500-5x)=-5x^2+1500x$ (nghìn đồng).\\
b) \textbf{Đúng.} Lợi nhuận thu được là:
\[ P(x)=R(x)-C(x)=(-5x^2+1500x)-(300x+12000)=-5x^2+1200x-12000\text{ (nghìn đồng)} \]
c) \textbf{Đúng.} Xét hàm lợi nhuận $P(x)=-5x^2+1200x-12000$ trên đoạn $[20;120]$. Đạo hàm $P'(x)=-10x+1200=0\iff x=120$. Vì hệ số $a=-5<0$, hàm số đạt giá trị lớn nhất tại đỉnh $x=120$ khách.\\
d) \textbf{Sai.} Lợi nhuận lớn nhất tương ứng là $P(120)=-5(120)^2+1200(120)-12000=60000$ nghìn đồng, tức là $60$ triệu đồng (chứ không phải $50$ triệu đồng).

\loigiai{Câu 3:}
a) \textbf{Đúng.} $\overrightarrow{AB}=(0-2;3-1;1-(-1))=(-2;2;2)$.\\
b) \textbf{Đúng.} $\overrightarrow{AC}=(4-2;5-1;3-(-1))=(2;4;4)$, suy ra $AC=\sqrt{2^2+4^2+4^2}=\sqrt{4+16+16}=\sqrt{36}=6$.\\
c) \textbf{Sai.} Tích vô hướng $\overrightarrow{AB}\cdot\overrightarrow{AC}=(-2)\cdot2+2\cdot4+2\cdot4=-4+8+8=12\ne0$. Do đó tam giác $ABC$ không vuông tại $A$.\\
d) \textbf{Đúng.} Tứ giác $ABCD$ là hình bình hành khi và chỉ khi $\overrightarrow{AD}=\overrightarrow{BC}\iff D=A+C-B$. Ta có:
$x_D=2+4-0=6$, $y_D=1+5-3=3$, $z_D=-1+3-1=1$, tức $D(6;3;1)$.

\loigiai{Câu 4:}
a) \textbf{Đúng.} Độ lớn trọng lực là $|\vec P|=mg=6\cdot10=60$ N.\\
b) \textbf{Đúng.} Chiều dài sợi cáp $SA$ là độ dài đoạn thẳng $SA$:
$\overrightarrow{SA}=(0-0;3-0;0-4)=(0;3;-4)\implies SA=\sqrt{0^2+3^2+(-4)^2}=5$ m.\\
Tương tự $SB=SC=5$ m.\\
c) \textbf{Sai.} Gọi $T$ là độ lớn lực căng của mỗi sợi cáp. Ta có $\vec T_1=\dfrac{T}{5}(0;3;-4)$, $\vec T_2=\dfrac{T}{5}\left(-\dfrac{3\sqrt3}{2};-\dfrac{3}{2};-4\right)$, $\vec T_3=\dfrac{T}{5}\left(\dfrac{3\sqrt3}{2};-\dfrac{3}{2};-4\right)$.\\
Tổng các lực căng là $\vec T_1+\vec T_2+\vec T_3=\left(0;0;3\cdot\dfrac{-4T}{5}\right)=\left(0;0;-\dfrac{12T}{5}\right)$.\\
Đèn ở trạng thái cân bằng nên:
\[ \vec T_1+\vec T_2+\vec T_3+\vec P=\vec 0\iff -\dfrac{12T}{5}+60=0\iff T=25\text{ N} \]
Vậy độ lớn lực căng bằng $25$ N (không phải $30$ N).\\
d) \textbf{Đúng.} Với $T=25$ N, tọa độ lực căng $\vec T_1$ là:
\[ \vec T_1=\dfrac{25}{5}(0;3;-4)=5(0;3;-4)=(0;15;-20) \]

\section*{PHẦN III. Câu trắc nghiệm trả lời ngắn}

\loigiai{Câu 1: Đáp án 12.}
Tập xác định: $D=\mathbb R\setminus\{-6\}$. Đạo hàm:
\[ y'=\dfrac{1\cdot6-3m\cdot1}{(x+6)^2}=\dfrac{6-3m}{(x+6)^2} \]
Hàm số đồng biến trên từng khoảng xác định khi và chỉ khi $y'>0$ với mọi $x\ne-6\iff 6-3m>0\iff m<2$.\\
Vì $m\in\mathbb Z$ và $m\in[-10;10]$, nên $m\in\{-10;-9;-8;\dots;0;1\}$.\\
Số giá trị nguyên của $m$ là $1-(-10)+1=12$.

\loigiai{Câu 2: Đáp án 14.}
Trong hình hộp $ABCD.A'B'C'D'$, ta có đẳng thức vectơ:
\[ \overrightarrow{AC'}=\overrightarrow{AB}+\overrightarrow{AD}+\overrightarrow{AA'} \]
Ta có $\overrightarrow{AB}=(1;1;1)$, $\overrightarrow{AD}=(0;3;-1)$, $\overrightarrow{AA'}=(2;2;3)$.\\
Suy ra $\overrightarrow{AC'}=(1+0+2;1+3+2;1+(-1)+3)=(3;6;3)$.\\
Tọa độ đỉnh $C'$ là $C'=A+\overrightarrow{AC'}=(1+3;0+6;1+3)=(4;6;4)$.\\
Do đó $a=4,b=6,c=4\implies a+b+c=4+6+4=14$.

\loigiai{Câu 3: Đáp án 1.}
Tập xác định: $D=\mathbb R$. Đạo hàm $y'=3x^2-6mx=3x(x-2m)$.\\
Vì $m>0$ nên $y'=0\iff x=0$ hoặc $x=2m$.\\
Tọa độ hai điểm cực trị của đồ thị là $A(0;4m^3)$ và $B(2m;0)$.\\
Khoảng cách giữa hai điểm cực trị là:
\[ AB^2=(2m-0)^2+(0-4m^3)^2=4m^2+16m^6 \]
Theo bài ra, $AB=2\sqrt5\iff AB^2=20$, suy ra:
\[ 16m^6+4m^2-20=0\iff 4m^6+m^2-5=0 \]
Đặt $u=m^2>0$, phương trình trở thành $4u^3+u-5=0\iff (u-1)(4u^2+4u+5)=0$.\\
Vì $4u^2+4u+5=(2u+1)^2+4>0$ với mọi $u$, nên phương trình có nghiệm duy nhất $u=1$.\\
Với $u=1\implies m^2=1\implies m=1$ (do $m>0$).

\loigiai{Câu 4: Đáp án 3.}
Vectơ nối vị trí hai thiết bị sau thời gian $t$ là:
\[ \overrightarrow{A_tB_t}=(3t-2-t;3t-4-2t;4-(2t-1))=(2t-2;t-4;5-2t) \]
Bình phương khoảng cách giữa hai thiết bị là:
\[ d^2(t)=(2t-2)^2+(t-4)^2+(5-2t)^2=4t^2-8t+4+t^2-8t+16+4t^2-20t+25=9t^2-36t+45 \]
Biến đổi tam thức bậc hai:
\[ d^2(t)=9(t^2-4t+5)=9(t-2)^2+9 \]
Với $0\le t\le4$, giá trị nhỏ nhất của $d^2(t)$ đạt được tại thời điểm $t=2$ giờ, khi đó $\min d^2(t)=9$.\\
Vậy khoảng cách ngắn nhất giữa hai thiết bị là $\sqrt9=3$ km.

\loigiai{Câu 5: Đáp án 108.}
Gọi chiều rộng đáy bể là $x$ (m, $x>0$), khi đó chiều dài đáy là $2x$ (m).\\
Thể tích của bể là $V=2x^2\cdot h=288\text{ m}^3\implies$ chiều cao của bể là $h=\dfrac{288}{2x^2}=\dfrac{144}{x^2}$ (m).\\
Diện tích đáy bể là $S_{\text{đáy}}=2x^2$ (m$^2$).\\
Diện tích 4 mặt thành bể xung quanh là $S_{\text{xq}}=2(x+2x)h=6xh=6x\cdot\dfrac{144}{x^2}=\dfrac{864}{x}$ (m$^2$).\\
Tổng diện tích bề mặt cần xây (đáy và 4 mặt bên) là:
\[ S(x)=2x^2+\dfrac{864}{x}\quad (x>0) \]
Xét hàm số $S(x)$ trên khoảng $(0;+\infty)$: $S'(x)=4x-\dfrac{864}{x^2}$.\\
Cho $S'(x)=0\iff 4x^3=864\iff x^3=216\iff x=6$ (m).\\
Bảng biến thiên cho thấy $S(x)$ đạt giá trị nhỏ nhất tại $x=6$.\\
Diện tích xây dựng nhỏ nhất là:
\[ S_{\min}=S(6)=2\cdot6^2+\dfrac{864}{6}=72+144=216\text{ m}^2 \]
Đơn giá xây dựng là $500$ nghìn đồng/m$^2$ $= 0{,}5$ triệu đồng/m$^2$.\\
Chi phí xây dựng thấp nhất là: $216\times0{,}5=108$ triệu đồng.

\loigiai{Câu 6: Đáp án 2.}
Đặt khoảng cách $MC=x$ (km) với $0\le x\le12$. Khi đó khoảng cách $AM=12-x$ (km).\\
Tam giác $BCM$ vuông tại $C$ có $BC=6$ km, $MC=x$ km nên:
\[ MB=\sqrt{MC^2+BC^2}=\sqrt{x^2+36}\text{ (km)} \]
Thời gian chạy bộ dọc bờ biển từ $A$ đến $M$ với vận tốc $10$ km/h là $t_1=\dfrac{12-x}{10}$ (giờ).\\
Thời gian chèo thuyền từ $M$ đến $B$ với vận tốc $6$ km/h là $t_2=\dfrac{\sqrt{x^2+36}}{6}$ (giờ).\\
Tổng thời gian di chuyển từ $A$ đến $B$ là:
\[ T(x)=\dfrac{12-x}{10}+\dfrac{\sqrt{x^2+36}}{6}\quad (0\le x\le12) \]
Đạo hàm:
\[ T'(x)=-\dfrac{1}{10}+\dfrac{x}{6\sqrt{x^2+36}} \]
Cho $T'(x)=0\iff 6\sqrt{x^2+36}=10x\iff 3\sqrt{x^2+36}=5x\iff 9(x^2+36)=25x^2$ (với $x>0$)\\
$\iff 16x^2=324\iff x^2=\dfrac{81}{4}\iff x=\dfrac{9}{2}=4{,}5$ km.\\
Tính giá trị tại điểm tới hạn và hai đầu mút của đoạn $[0;12]$:
- $T(4{,}5)=\dfrac{12-4{,}5}{10}+\dfrac{\sqrt{4{,}5^2+36}}{6}=\dfrac{7{,}5}{10}+\dfrac{7{,}5}{6}=0{,}75+1{,}25=2$ giờ.
- $T(0)=\dfrac{12}{10}+\dfrac{\sqrt{36}}{6}=1{,}2+1=2{,}2$ giờ.
- $T(12)=0+\dfrac{\sqrt{144+36}}{6}=\dfrac{\sqrt{180}}{6}=\sqrt5\approx2{,}236$ giờ.
So sánh các giá trị, thời gian ngắn nhất để người đó di chuyển từ $A$ đến $B$ là $2$ giờ (đạt được khi người đó chạy bộ đến điểm $M$ cách $C$ một đoạn $4{,}5$ km rồi chèo thuyền sang đảo).
\end{document}
"""

(BASE / "De_giua_ki_1_03.tex").write_text(latex_content.strip() + "\n", encoding="utf-8")
print("[BUILD] Đã tạo De_giua_ki_1_03.tex và dap_an.json thành công!")
