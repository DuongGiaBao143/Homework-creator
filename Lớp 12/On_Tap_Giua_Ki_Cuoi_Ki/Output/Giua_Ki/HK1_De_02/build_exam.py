"""Tạo mã XeLaTeX đề ôn giữa kì I số 02 (HK1_De_02)."""
from pathlib import Path

BASE = Path(__file__).resolve().parent

tex_content = r"""% !TeX program = xelatex
\documentclass[12pt,a4paper]{article}
\usepackage{fontspec}
\setmainfont{Times New Roman}[Path=C:/Windows/Fonts/,UprightFont=times.ttf,BoldFont=timesbd.ttf,ItalicFont=timesi.ttf,BoldItalicFont=timesbi.ttf]
\usepackage{amsmath,amssymb,amsfonts}
\usepackage[left=1.5cm,right=1.5cm,top=1.5cm,bottom=1.7cm,headheight=17pt]{geometry}
\usepackage{enumitem,array,graphicx,tikz,fancyhdr,needspace}
\usetikzlibrary{arrows.meta,calc,patterns}
\newcommand{\soDe}{2}
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
\newcommand{\loigiai}[1]{\par\medskip\Needspace{3\baselineskip}\noindent\textbf{#1}\par\nobreak}
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
\item Cho hàm số $y=-x^3+3x^2-1$. Hàm số đồng biến trên khoảng nào sau đây?
\bonpa{$(0;2)$.}{$(-\infty;0)$.}{$(2;+\infty)$.}{$(-2;0)$.}

\item Điểm cực tiểu của đồ thị hàm số $y=x^3-3x+2$ là
\bonpa{$(-1;4)$.}{$(1;0)$.}{$(1;2)$.}{$(0;2)$.}

\item Giá trị nhỏ nhất của hàm số $f(x)=x^3-3x^2-9x+1$ trên đoạn $[-2;2]$ bằng
\bonpa{$-1$.}{$6$.}{$-21$.}{$-20$.}

\item Các đường tiệm cận đứng và tiệm cận ngang của đồ thị hàm số $y=\dfrac{3x+2}{x-1}$ lần lượt là
\bonpa{$x=-1$ và $y=3$.}{$x=3$ và $y=1$.}{$x=1$ và $y=-3$.}{$x=1$ và $y=3$.}

\item Đường tiệm cận xiên của đồ thị hàm số $y=\dfrac{2x^2-3x+5}{x-2}$ có phương trình là
\bonpa{$y=2x+1$.}{$y=2x-1$.}{$y=2x+5$.}{$y=x+1$.}

\Needspace{7\baselineskip}
\item Đường cong trong hình bên là đồ thị của hàm số nào dưới đây?
\par\nobreak\smallskip
\begin{minipage}[c]{0.60\linewidth}
\bonpa{$y=-x^3+3x^2+2$.}{$y=x^3-3x^2+2$.}{$y=x^3-3x+2$.}{$y=x^3+3x^2+2$.}
\end{minipage}\hfill
\begin{minipage}[c]{0.36\linewidth}\centering
\begin{tikzpicture}[x=0.72cm,y=0.53cm,>=Stealth]
\draw[->] (-1.8,0)--(3.6,0) node[right] {$x$};
\draw[->] (0,-3.2)--(0,3.5) node[above] {$y$};
\draw[dashed,gray] (2,0)--(2,-2)--(0,-2);
\draw[very thick,blue!60!black,domain=-1.05:3.15,samples=100] plot (\x,{\x*\x*\x-3*\x*\x+2});
\fill (0,2) circle (1.6pt);\fill (2,-2) circle (1.6pt);
\node[below left,fill=white,inner sep=1pt] at (0,0) {$O$};
\node[left,fill=white,inner sep=1pt] at (0,2) {$2$};
\node[left,fill=white,inner sep=1pt] at (0,-2) {$-2$};
\node[above,fill=white,inner sep=1pt] at (2,0) {$2$};
\end{tikzpicture}
\end{minipage}

\item Theo một nghiên cứu y học, số lượng vi khuẩn trong một môi trường nuôi cấy sau $t$ giờ được ước lượng bởi công thức
$N(t)=-t^3+9t^2+120$ với $0\le t\le8$. Sau bao nhiêu giờ kể từ khi bắt đầu nuôi cấy thì số lượng vi khuẩn đạt giá trị lớn nhất?
\bonpa{$t=3$ giờ.}{$t=4$ giờ.}{$t=6$ giờ.}{$t=8$ giờ.}
\end{enumerate}

\begin{enumerate}[start=8]
\item Cho tứ diện $S.ABC$. Gọi $M$ là trung điểm của cạnh $BC$. Khẳng định nào sau đây đúng?
\bonpa{$\overrightarrow{SB}+\overrightarrow{SC}=\overrightarrow{SM}$.}{$\overrightarrow{SB}+\overrightarrow{SC}=3\overrightarrow{SM}$.}{$\overrightarrow{SB}-\overrightarrow{SC}=2\overrightarrow{SM}$.}{$\overrightarrow{SB}+\overrightarrow{SC}=2\overrightarrow{SM}$.}

\item Trong không gian $Oxyz$, cho vectơ $\vec u=2\vec i-3\vec k+\vec j$. Tọa độ của vectơ $\vec u$ là
\bonpa{$(2;1;-3)$.}{$(2;-3;1)$.}{$(-3;2;1)$.}{$(1;2;-3)$.}

\item Trong không gian $Oxyz$, cho điểm $M(3;-2;5)$. Tọa độ hình chiếu vuông góc của điểm $M$ lên mặt phẳng $(Oxy)$ là
\bonpa{$(0;0;5)$.}{$(3;-2;0)$.}{$(3;0;5)$.}{$(0;-2;5)$.}

\item Trong không gian $Oxyz$, cho hai điểm $A(2;1;-1)$ và $B(0;3;-2)$. Độ dài đoạn thẳng $AB$ bằng
\bonpa{$\sqrt5$.}{$9$.}{$3$.}{$\sqrt{13}$.}

\item Trong không gian $Oxyz$, cho hai vectơ $\vec a=(1;2;-2)$ và $\vec b=(2;-1;4)$. Tích vô hướng $\vec a\cdot\vec b$ bằng
\bonpa{$8$.}{$4$.}{$-4$.}{$-8$.}
\end{enumerate}

\section*{\large PHẦN II. Câu trắc nghiệm đúng hoặc sai}
\textit{Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d), chọn đúng hoặc sai.}
\begin{enumerate}
\Needspace{9\baselineskip}
\item Cho hàm số $f(x)=\dfrac{x^2-x+1}{x-1}$, xác định trên $\mathbb R\setminus\{1\}$.
\begin{enumerate}
\item $f'(x)=\dfrac{x(x-2)}{(x-1)^2}$.
\item Hàm số nghịch biến trên khoảng $(0;2)$.
\item Đồ thị hàm số có đường tiệm cận xiên là $y=x$.
\item Khoảng cách giữa hai điểm cực trị của đồ thị hàm số bằng $2\sqrt5$.
\end{enumerate}

\Needspace{10\baselineskip}
\item Một công ty sản xuất đồ gia dụng sản xuất $x$ chiếc quạt hơi nước mỗi ngày ($1\le x\le120$). Tổng chi phí sản xuất mỗi ngày (tính bằng triệu đồng) được cho bởi hàm số $C(x)=x^2-40x+1600$. Chi phí sản xuất trung bình cho mỗi chiếc quạt là $\bar C(x)=\dfrac{C(x)}{x}$ (triệu đồng/chiếc). Giả sử công ty bán hết số quạt sản xuất được mỗi ngày với giá bán cố định là $80$ triệu đồng/chiếc.
\begin{enumerate}
\item Chi phí sản xuất trung bình cho mỗi chiếc quạt là $\bar C(x)=x-40+\dfrac{1600}{x}$ (triệu đồng/chiếc).
\item Chi phí trung bình cho mỗi chiếc quạt nhỏ nhất khi mỗi ngày sản xuất $40$ chiếc quạt.
\item Biểu thức lợi nhuận thu được mỗi ngày là $P(x)=-x^2+120x-1600$ (triệu đồng).
\item Lợi nhuận lớn nhất của công ty đạt được khi sản xuất $40$ chiếc quạt mỗi ngày.
\end{enumerate}
\end{enumerate}

\begin{enumerate}[start=3]
\Needspace{8\baselineskip}
\item Trong không gian $Oxyz$, cho ba điểm $A(2;-1;1)$, $B(0;1;2)$ và $C(3;0;-1)$.
\begin{enumerate}
\item $\overrightarrow{AB}=(-2;2;1)$.
\item Độ dài đoạn thẳng $AB$ bằng $3$.
\item Tam giác $ABC$ là tam giác vuông tại $A$.
\item Tọa độ điểm $D$ để tứ giác $ABCD$ là hình bình hành là $D(5;-2;-2)$.
\end{enumerate}

\Needspace{9\baselineskip}
\item Một bóng đèn có trọng lượng $P=60\text{ N}$ được treo cố định tại điểm $O$ nhờ ba sợi dây cáp không dãn gắn vào trần nhà tại ba điểm $A,B,C$. Trong hệ trục tọa độ $Oxyz$ (gốc tại $O$, trục $Oz$ hướng thẳng đứng lên trên, đơn vị trên các trục là mét), lực tác dụng lên bóng đèn gồm trọng lực $\vec P=(0;0;-60)$ và ba lực căng $\vec F_1=(10;20;20)$, $\vec F_2=(-10;20;20)$, $\vec F_3=(0;-40;20)$ (đơn vị newton, N).
\begin{enumerate}
\item Độ lớn của lực căng $\vec F_1$ bằng $30\text{ N}$.
\item Hai lực căng $\vec F_1$ và $\vec F_2$ có độ lớn bằng nhau.
\item Tích vô hướng $\vec F_1\cdot\vec F_2=0$.
\item Dưới tác dụng của trọng lực $\vec P$ và ba lực căng $\vec F_1,\vec F_2,\vec F_3$, bóng đèn ở trạng thái cân bằng.
\end{enumerate}
\end{enumerate}

\section*{\large PHẦN III. Câu trắc nghiệm trả lời ngắn}
\textit{Thí sinh trả lời từ câu 1 đến câu 6. Ghi kết quả vào các ô trả lời; dùng dấu phẩy cho phần thập phân.}
\begin{enumerate}
\item Có bao nhiêu giá trị nguyên của tham số $m$ thuộc đoạn $[-5;5]$ để hàm số
$y=\dfrac{x+3m}{x-2}$ nghịch biến trên từng khoảng xác định của nó?
\otraloi

\item Trong không gian $Oxyz$, cho hình hộp $ABCD.A'B'C'D'$ biết
$A(1;0;1)$, $B(2;1;2)$, $D(1;-1;3)$ và $A'(4;2;-1)$.
Biết tọa độ đỉnh $C'(a;b;c)$, tính giá trị của biểu thức $a+b+c$.
\otraloi
\end{enumerate}

\newpage
\begin{enumerate}[start=3]
\item Một người thợ gò tôn muốn làm một chiếc thùng hình hộp chữ nhật không nắp có đáy là hình vuông. Tổng diện tích tôn để làm thùng (gồm một mặt đáy và bốn mặt bên, bỏ qua các mép hàn) bằng $108\text{ dm}^2$. Thể tích lớn nhất của chiếc thùng đó bằng bao nhiêu $\text{dm}^3$?
\begin{center}
\begin{tikzpicture}[x=0.45cm,y=0.45cm,>=Stealth]
\draw[thick] (0,0)--(5,0)--(7,1.8)--(7,4.8)--(5,3)--(0,3)--cycle;
\draw[thick] (5,0)--(5,3);
\draw[thick] (0,3)--(2,4.8)--(7,4.8);
\draw[dashed] (0,0)--(2,1.8)--(7,1.8);
\draw[dashed] (2,1.8)--(2,4.8);
\draw[<->] (0,-0.6)--(5,-0.6) node[midway,below] {$x$};
\draw[<->] (5.4,-0.4)--(7.4,1.4) node[midway,below right] {$x$};
\draw[<->] (7.6,1.8)--(7.6,4.8) node[midway,right] {$h$};
\node[font=\small] at (3.5,1.5) {Thùng không nắp};
\end{tikzpicture}
\end{center}
\otraloi

\item Trong không gian $Oxyz$ với đơn vị đo là mét, hai chiếc drone $A$ và $B$ xuất phát cùng lúc tại thời điểm $t=0$ và chuyển động thẳng đều. Vị trí của drone $A$ tại thời điểm $t$ giây ($0\le t\le5$) là $A_t(t;2t;3t+1)$. Vị trí của drone $B$ tại thời điểm $t$ giây là $B_t(4-t;4+t;t+4)$. Khoảng cách nhỏ nhất giữa hai drone trong khoảng thời gian trên bằng bao nhiêu mét? \textit{Làm tròn kết quả đến hàng phần mười.}
\otraloi

\item Cho hàm số $y=x^3-3mx^2+2$ với $m>0$. Đồ thị hàm số có hai điểm cực trị $A$ và $B$. Tìm giá trị của $m$ để diện tích tam giác $OAB$ bằng $8$ (với $O$ là gốc tọa độ).
\otraloi

\item Một nhà máy nước $A$ và một kho hóa chất $B$ nằm cùng một phía bờ sông thẳng $HK$. Khoảng cách từ nhà máy $A$ đến bờ sông là $AH=3\text{ km}$, khoảng cách từ kho $B$ đến bờ sông là $BK=5\text{ km}$, và $HK=6\text{ km}$. Người ta cần đặt một trạm bơm $M$ trên đoạn bờ sông $HK$ để lắp đặt đường ống dẫn nước từ sông tới nhà máy $A$ và kho $B$. Tổng chiều dài đường ống dẫn $L=MA+MB$ ngắn nhất bằng bao nhiêu kilômét?
\begin{center}
\begin{tikzpicture}[x=0.8cm,y=0.45cm,>=Stealth]
\draw[thick,blue!70!black] (-1,0)--(7.5,0) node[right,black] {Bờ sông};
\draw[thick] (0,3) node[above left] {$A$}--(0,0) node[below] {$H$};
\draw[thick] (6,5) node[above right] {$B$}--(6,0) node[below] {$K$};
\draw[thick,red!80!black] (0,3)--(2.25,0) node[below,black] {$M$}--(6,5);
\fill (0,3) circle (2pt);\fill (6,5) circle (2pt);\fill (2.25,0) circle (2pt);
\node[left] at (0,1.5) {$3\text{ km}$};
\node[right] at (6,2.5) {$5\text{ km}$};
\draw[<->] (0,-1.2)--(6,-1.2) node[midway,below] {$HK = 6\text{ km}$};
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
Đáp án & A & B & C & D & A & B & C & D & A & B & C & D \\\hline
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
\begin{tabular}{|c|c|c|c|c|c|c|}\hline
Câu & 1 & 2 & 3 & 4 & 5 & 6\\\hline
Đáp án & 6 & 9 & 108 & 2,2 & 4 & 10 \\\hline
\end{tabular}
\end{center}

\textbf{Thang điểm dùng cho đề ôn tập:}
\begin{itemize}[leftmargin=*,itemsep=3pt]
\item Phần I: mỗi câu đúng $0{,}25$ điểm; tối đa $3$ điểm.
\item Phần II: mỗi câu có 4 ý. Đúng 1, 2, 3, 4 ý lần lượt được $0{,}1$; $0{,}25$; $0{,}5$; $1$ điểm. Tối đa $4$ điểm.
\item Phần III: mỗi câu đúng $0{,}5$ điểm; tối đa $3$ điểm.
\end{itemize}
\textbf{Phạm vi:} Bài 1–5 (ứng dụng đạo hàm và khảo sát hàm số), Bài 6–8 (vectơ và tọa độ trong không gian).
Tổng điểm $10$; thời gian $90$ phút.

\newpage
\begin{center}\Large\textbf{HƯỚNG DẪN GIẢI CHI TIẾT}\end{center}
\section*{\large Phần I}
\loigiai{Câu 1. Chọn A.}
$y'=-3x^2+6x=-3x(x-2)>0\Leftrightarrow 0<x<2$. Hàm số đồng biến trên $(0;2)$.

\loigiai{Câu 2. Chọn B.}
$y'=3x^2-3=0\Leftrightarrow x=\pm1$. Ta có $y''(1)=6>0$ và $y(1)=0$, nên điểm cực tiểu của đồ thị là $(1;0)$.

\loigiai{Câu 3. Chọn C.}
$f'(x)=3x^2-6x-9=0\Leftrightarrow x=-1$ hoặc $x=3$. Vì $-1\in[-2;2]$ nên tính $f(-2)=-1$, $f(-1)=6$, $f(2)=-21$. Do đó $\min_{[-2;2]}f(x)=-21$.

\loigiai{Câu 4. Chọn D.}
$\lim_{x\to1^+}\frac{3x+2}{x-1}=+\infty\Rightarrow x=1$ là TCĐ; $\lim_{x\to\pm\infty}\frac{3x+2}{x-1}=3\Rightarrow y=3$ là TCN.

\loigiai{Câu 5. Chọn A.}
$\frac{2x^2-3x+5}{x-2}=2x+1+\frac{7}{x-2}\to 2x+1$ khi $x\to\pm\infty$. Tiệm cận xiên là $y=2x+1$.

\loigiai{Câu 6. Chọn B.}
Đồ thị hàm đa thức bậc ba có hệ số $a>0$, cực đại tại $(0;2)$, cực tiểu tại $(2;-2)$. Hàm $y=x^3-3x^2+2$ thỏa mãn đầy đủ các đặc điểm trên.

\loigiai{Câu 7. Chọn C.}
$N'(t)=-3t^2+18t=0\Leftrightarrow t=6\in[0;8]$. Vì $N(0)=120$, $N(6)=228$, $N(8)=184$ nên số lượng vi khuẩn đạt lớn nhất sau $t=6$ giờ.

\loigiai{Câu 8. Chọn D.}
Với $M$ là trung điểm cạnh $BC$, theo quy tắc trung điểm trong không gian: $\overrightarrow{SB}+\overrightarrow{SC}=2\overrightarrow{SM}$.

\loigiai{Câu 9. Chọn A.}
$\vec u=2\vec i+\vec j-3\vec k$ có tọa độ $(2;1;-3)$.

\loigiai{Câu 10. Chọn B.}
Hình chiếu vuông góc của điểm $M(3;-2;5)$ lên mặt phẳng tọa độ $(Oxy)$ là $(3;-2;0)$.

\loigiai{Câu 11. Chọn C.}
$\overrightarrow{AB}=(-2;2;-1)\Rightarrow AB=\sqrt{(-2)^2+2^2+(-1)^2}=\sqrt9=3$.

\loigiai{Câu 12. Chọn D.}
$\vec a\cdot\vec b=1\cdot2+2\cdot(-1)+(-2)\cdot4=2-2-8=-8$.

\newpage
\section*{\large Phần II}
\loigiai{Câu 1. a) Đúng; b) Sai; c) Đúng; d) Đúng.}
Viết $f(x)=x+\dfrac{1}{x-1}$.
\begin{enumerate}[label=\alph*),leftmargin=*,itemsep=2pt]
\item $f'(x)=1-\dfrac{1}{(x-1)^2}=\dfrac{x(x-2)}{(x-1)^2}$ với mọi $x\ne1$.
\item $f'(x)<0$ trên từng khoảng $(0;1)$ và $(1;2)$. Do không xác định tại $x=1$ nên hàm số không nghịch biến trên khoảng $(0;2)$.
\item $\lim_{x\to\pm\infty}[f(x)-x]=\lim_{x\to\pm\infty}\dfrac{1}{x-1}=0\Rightarrow y=x$ là tiệm cận xiên.
\item Hai điểm cực trị là $A(0;-1)$ và $B(2;3)\Rightarrow AB=\sqrt{2^2+4^2}=2\sqrt5$.
\end{enumerate}

\loigiai{Câu 2. a) Đúng; b) Đúng; c) Đúng; d) Sai.}
\begin{enumerate}[label=\alph*),leftmargin=*,itemsep=2pt]
\item $\bar C(x)=\dfrac{C(x)}{x}=x-40+\dfrac{1600}{x}$ (triệu đồng/chiếc).
\item $\bar C'(x)=1-\dfrac{1600}{x^2}=0\Leftrightarrow x=40\in[1;120]$. Chi phí trung bình nhỏ nhất tại $x=40$.
\item Lợi nhuận mỗi ngày: $P(x)=80x-C(x)=-x^2+120x-1600$ (triệu đồng).
\item $P(x)$ đạt giá trị lớn nhất tại đỉnh parabol $x=60$ chiếc quạt (khi đó $P(60)=2000$ triệu đồng), không phải $x=40$.
\end{enumerate}

\loigiai{Câu 3. a) Đúng; b) Đúng; c) Sai; d) Đúng.}
\begin{enumerate}[label=\alph*),leftmargin=*,itemsep=2pt]
\item $\overrightarrow{AB}=(0-2;1-(-1);2-1)=(-2;2;1)$.
\item $AB=|\overrightarrow{AB}|=\sqrt{(-2)^2+2^2+1^2}=3$.
\item $\overrightarrow{AC}=(1;1;-2)\Rightarrow\overrightarrow{AB}\cdot\overrightarrow{AC}=(-2)(1)+2(1)+1(-2)=-2\ne0$. Tam giác $ABC$ không vuông tại $A$.
\item $ABCD$ là hình bình hành $\Leftrightarrow\overrightarrow{OD}=\overrightarrow{OC}-\overrightarrow{AB}=(3-(-2);0-2;-1-1)=(5;-2;-2)$.
\end{enumerate}

\loigiai{Câu 4. a) Đúng; b) Đúng; c) Sai; d) Đúng.}
\begin{enumerate}[label=\alph*),leftmargin=*,itemsep=2pt]
\item $|\vec F_1|=\sqrt{10^2+20^2+20^2}=\sqrt{900}=30$ N.
\item $|\vec F_2|=\sqrt{(-10)^2+20^2+20^2}=30\text{ N}=|\vec F_1|$.
\item $\vec F_1\cdot\vec F_2=10(-10)+20(20)+20(20)=700\ne0$.
\item Tổng các lực: $\vec F_1+\vec F_2+\vec F_3+\vec P=(0;0;60)+(0;0;-60)=\vec0$. Bóng đèn ở trạng thái cân bằng.
\end{enumerate}

\newpage
\section*{\large Phần III}
\loigiai{Câu 1. Đáp án: 6.}
Tập xác định: $D=\mathbb R\setminus\{2\}$. Đạo hàm:
\[
y'=\frac{1\cdot(-2)-3m\cdot1}{(x-2)^2}=\frac{-2-3m}{(x-2)^2}.
\]
Hàm số nghịch biến trên từng khoảng xác định khi $-2-3m<0\Leftrightarrow m>-\dfrac{2}{3}$.
Với $m\in[-5;5]$ và $m\in\mathbb Z$, ta có $m\in\{0;1;2;3;4;5\}$, gồm $6$ giá trị nguyên.

\loigiai{Câu 2. Đáp án: 9.}
Theo quy tắc hình hộp: $\overrightarrow{AC'}=\overrightarrow{AB}+\overrightarrow{AD}+\overrightarrow{AA'}$.\\
Ta có $\overrightarrow{AB}=(1;1;1)$, $\overrightarrow{AD}=(0;-1;2)$, $\overrightarrow{AA'}=(3;2;-2)$.\\
Suy ra $\overrightarrow{AC'}=(1+0+3;1-1+2;1+2-2)=(4;2;1)$.\\
Tọa độ đỉnh $C'=A+\overrightarrow{AC'}=(1+4;0+2;1+1)=(5;2;2)$. Do đó $a+b+c=5+2+2=9$.

\loigiai{Câu 3. Đáp án: 108.}
Gọi cạnh đáy hình vuông là $x$ ($x>0$, dm) và chiều cao thùng là $h$ ($h>0$, dm).\\
Diện tích tôn: $S=x^2+4xh=108\implies h=\dfrac{108-x^2}{4x}$ ($0<x<\sqrt{108}$).\\
Thể tích thùng: $V(x)=x^2 h=\dfrac{1}{4}(108x-x^3)$.\\
Đạo hàm: $V'(x)=\dfrac{1}{4}(108-3x^2)=0\Leftrightarrow x=6\in(0;\sqrt{108})$.\\
Thể tích lớn nhất: $V(6)=\dfrac{1}{4}(108\cdot6-6^3)=108\text{ dm}^3$.

\loigiai{Câu 4. Đáp án: 2,2.}
Vectơ nối vị trí hai chiếc drone: $\overrightarrow{A_t B_t}=(4-2t;4-t;3-2t)$.\\
Bình phương khoảng cách:
\[
d^2(t)=(4-2t)^2+(4-t)^2+(3-2t)^2=9t^2-36t+41=9(t-2)^2+5\ge5.
\]
Dấu bằng xảy ra khi $t=2\in[0;5]$. Khoảng cách nhỏ nhất $d_{\min}=\sqrt5\approx2{,}236$ m, làm tròn đến hàng phần mười được $2{,}2$.

\newpage
\loigiai{Câu 5. Đáp án: 4.}
Đạo hàm $y'=3x^2-6mx=3x(x-2m)=0\Leftrightarrow x=0$ hoặc $x=2m$ (vì $m>0$).\\
Tọa độ hai điểm cực trị: $A(0;2)$ và $B(2m;-4m^3+2)$.\\
Vì $A\in Oy$ nên $OA=2$. Khoảng cách từ $B$ đến trục $Oy$ là $d(B,Oy)=|x_B|=2m$.\\
Diện tích tam giác: $S_{\Delta OAB}=\dfrac{1}{2}\cdot OA\cdot d(B,Oy)=\dfrac{1}{2}\cdot 2\cdot 2m=2m$.\\
Theo bài ra: $S_{\Delta OAB}=8\Leftrightarrow 2m=8\Leftrightarrow m=4$.

\loigiai{Câu 6. Đáp án: 10.}
Gọi $x$ là khoảng cách từ $H$ đến $M$ ($0\le x\le6$, km), suy ra $KM=6-x$.\\
Độ dài $MA=\sqrt{x^2+3^2}=\sqrt{x^2+9}$; $MB=\sqrt{(6-x)^2+5^2}=\sqrt{(6-x)^2+25}$.\\
Lấy điểm $A'$ đối xứng với $A$ qua bờ sông $HK$, khi đó $A'H=3$ km và $MA=MA'$.\\
Tổng chiều dài $MA+MB=MA'+MB\ge A'B$.\\
Dấu bằng xảy ra khi ba điểm $A',M,B$ thẳng hàng.\\
Từ $A'$ kẻ đường vuông góc với đường kéo dài $BK$ tại $E$, ta có tam giác vuông $A'EB$:\\
$A'E=HK=6$ km, $BE=BK+HA'=5+3=8$ km.\\
Độ dài $A'B=\sqrt{A'E^2+BE^2}=\sqrt{6^2+8^2}=\sqrt{100}=10$ km.\\
Khi đó $\dfrac{HM}{KM}=\dfrac{AH}{BK}=\dfrac{3}{5}\implies x=2{,}25\text{ km}\in[0;6]$.\\
Vậy tổng chiều dài đường ống dẫn nước ngắn nhất là $10\text{ km}$.
\end{document}
"""

(BASE / "De_giua_ki_1_02.tex").write_text(tex_content, encoding="utf-8")
print("[BUILD] Đã tạo thành công De_giua_ki_1_02.tex tinh gọn 9 trang chuẩn.")
