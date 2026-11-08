import os
import subprocess
import pymupdf
import shutil

OUT_DIR = r"d:\Tao_De\Lớp 10\Output\De_Cuong_Vector"
EXPORT_DIR = r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\Vector"

def generate_tex(exam_pages=4, ans_pages=4):
    tex = r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage[vietnamese]{babel}
\usepackage[margin=1.3cm,top=0.8cm,bottom=1.0cm,includehead,includefoot,headheight=18pt,headsep=6pt,footskip=16pt]{geometry}
\usepackage{amsmath,amssymb,array,tabularx,enumitem,fancyhdr,tikz,xcolor,needspace}
\usetikzlibrary{calc,angles,quotes,arrows.meta,babel,patterns}
\definecolor{ink}{RGB}{30,55,70}

\newcommand{\headerQuote}{%
  \ifcase\value{page}\relax
    \or Math gives us hope that every problem has a solution% Trang 1
    \or Math + You = Champion% Trang 2
    \or Where Frustration Becomes Inspiration% Trang 3
    \or Turning Confusion into Clarity% Trang 4
    \or Don't be an X, be a Y of mathematics% Trang 5
    \or Don't get mad. Learn to add% Trang 6
    \or The only way to learn mathematics is to do mathematics% Trang 7
    \or Small steps every day lead to big results% Trang 8
    \or Every expert was once a beginner% Trang 9
    \or Success is the sum of small efforts repeated daily% Trang 10
    \or Mathematics is the music of reason% Trang 11
    \or Believe you can and you're halfway there% Trang 12
    \else Math gives us hope that every problem has a solution%
  \fi
}
\pagestyle{fancy}\fancyhf{}
\lhead{\small\textit{\headerQuote}}
\rhead{\small\textit{Người biên soạn: Dương Gia Bảo}}
\rfoot{\small Trang \thepage/""" + str(exam_pages) + r"""}
\renewcommand{\headrulewidth}{0.4pt}
\fancypagestyle{dapan}{%
  \fancyhf{}%
  \lhead{\small\textit{\headerQuote}}%
  \rhead{\small\textit{Người biên soạn: Dương Gia Bảo}}%
  \rfoot{\small Trang \the\numexpr\value{page}-""" + str(exam_pages) + r"""\relax/""" + str(ans_pages) + r"""}%
  \renewcommand{\headrulewidth}{0.4pt}%
}
\setlength{\headheight}{18pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\setlength{\tabcolsep}{2pt}
\renewcommand{\arraystretch}{1.05}
\newcommand{\parttitle}[1]{\par\vspace{2pt}\needspace{2\baselineskip}{\large\bfseries\color{ink}#1}\par\nopagebreak\vspace{1pt}}
\newcommand{\answerbox}{\hfill\textit{Đáp số:}\ \fbox{\rule{0pt}{8.5pt}\hspace{2.2cm}}}
\setlist[enumerate,1]{label=\textbf{Câu \arabic*.},leftmargin=1.1cm,labelsep=.15cm,itemsep=1.8pt,topsep=1pt,parsep=0pt}
\setlist[enumerate,2]{label=\alph*),leftmargin=.55cm,itemsep=1.5pt,topsep=0.2pt,parsep=0pt}

\begin{document}
% =========================================================================
% TRANG 1: TIÊU ĐỀ + CHỦ ĐỀ 1 (CÂU 1 - 6) + CHỦ ĐỀ 2 (CÂU 7 - 12)
% =========================================================================
\noindent
\begin{minipage}[c]{0.38\textwidth}
    \centering
    \textbf{LÀM TOÁN ĐỂ HẠNH PHÚC}\\[-2pt]
    \rule{3.2cm}{0.6pt}\\[2pt]
    \textbf{ĐỀ CƯƠNG ÔN TẬP}
\end{minipage}\hfill
\begin{minipage}[c]{0.58\textwidth}
    \centering
    \textbf{ĐỀ CƯƠNG ÔN TẬP CHƯƠNG IV -- VECTƠ}\\
    \textbf{NĂM HỌC 2026 -- 2027}\\[1pt]
    \textbf{CHUYÊN ĐỀ: 50 CÂU TRẢ LỜI NGẮN}\\
    \textbf{Môn: TOÁN -- Khối lớp 10}\\
    \textit{\small (Chương trình GDPT 2018 -- SGK Kết nối tri thức với cuộc sống)}
\end{minipage}

\vspace{0.08cm}
\noindent
\begin{minipage}[b]{0.78\textwidth}
    \textbf{Họ và tên:}\dotfill\textbf{SBD:}\makebox[3.5cm]{\dotfill}
\end{minipage}\hfill
\begin{minipage}[b]{0.20\textwidth}
    \hfill
    \setlength{\fboxrule}{0.8pt}%
    \fbox{\begin{minipage}{2.3cm}
        \centering
        \textbf{\small Tài liệu}\\
        \textbf{LƯU HÀNH}
    \end{minipage}}
\end{minipage}

\vspace{0.1cm}
\textit{\textbf{Lưu ý:} Học sinh trả lời từ Câu 1 đến Câu 50. Điền kết quả (dưới dạng số nguyên, phân số tối giản hoặc số thập phân theo yêu cầu) vào ô đáp số tương ứng.}

\parttitle{CHỦ ĐỀ 1. CÁC KHÁI NIỆM MỞ ĐẦU (CÂU 1 -- 6)}

\begin{enumerate}
\item Cho ngũ giác đều $ABCDE$ tâm $O$. Có bao nhiêu vectơ khác vectơ $\vec{0}$ có điểm đầu và điểm cuối là hai đỉnh phân biệt của ngũ giác $ABCDE$?
\answerbox

\item Cho hình lục giác đều $ABCDEF$ có tâm $O$. Có tất cả bao nhiêu vectơ khác vectơ $\vec{0}$ có điểm đầu và điểm cuối là các điểm thuộc tập hợp $\{A, B, C, D, E, F, O\}$?
\answerbox

\item Cho hình lục giác đều $ABCDEF$ tâm $O$. Có bao nhiêu vectơ khác $\vec{AB}$ có điểm đầu và điểm cuối lấy từ tập hợp $\{A, B, C, D, E, F, O\}$ mà bằng với vectơ $\vec{AB}$?
\answerbox

\item Cho tam giác đều $ABC$ có cạnh bằng $6\text{ cm}$. Gọi $M$ và $N$ lần lượt là trung điểm của các cạnh $AB$ và $AC$. Tính độ dài của vectơ $\vec{MN}$ (theo đơn vị xentimét).
\answerbox

\item Cho hình vuông $ABCD$ có cạnh bằng $4\sqrt{2}\text{ cm}$. Gọi $O$ là giao điểm của hai đường chéo $AC$ và $BD$. Tính độ dài của vectơ $\vec{OA}$ (theo đơn vị xentimét).
\answerbox

\item Cho hình chữ nhật $ABCD$. Gọi $M, N, P, Q$ lần lượt là trung điểm của các cạnh $AB, BC, CD, DA$. Có bao nhiêu vectơ khác vectơ $\vec{0}$ có điểm đầu và điểm cuối thuộc tập hợp $\{A, B, C, D, M, N, P, Q\}$ cùng phương với vectơ $\vec{AB}$?
\answerbox

\parttitle{CHỦ ĐỀ 2. TỔNG VÀ HIỆU CỦA HAI VECTƠ (CÂU 7 -- 16)}

\item Cho hình chữ nhật $ABCD$ có $AB = 6$ và $AD = 8$. Tính độ dài của vectơ $\vec{u} = \vec{AB} + \vec{AD}$.
\answerbox

\item Cho hình thoi $ABCD$ có cạnh bằng $5$ và góc $\widehat{BAD} = 60^\circ$. Tính độ dài của vectơ $\vec{v} = \vec{AB} - \vec{AD}$.
\answerbox

\item Cho tam giác đều $ABC$ có cạnh bằng $2\sqrt{3}$. Gọi $H$ là trung điểm của cạnh $BC$. Tính độ dài của vectơ $\vec{w} = \vec{AB} + \vec{AC}$.
\answerbox

\item Cho tam giác đều $ABC$ có độ dài cạnh bằng $8$. Tính độ dài của vectơ hiệu $\vec{AB} - \vec{AC}$.
\answerbox

\item Cho hình vuông $ABCD$ có cạnh bằng $6$. Tính giá trị của $|\vec{AB} + \vec{AC} + \vec{AD}|^2$.
\answerbox

\item Cho tam giác $ABC$ vuông tại $A$ có $AB = 3$ và $AC = 4$. Tính độ dài của vectơ $\vec{u} = \vec{AB} - \vec{CA}$.
\answerbox

\end{enumerate}

\newpage

% =========================================================================
% TRANG 2: TIẾP CHỦ ĐỀ 2 (CÂU 13 - 16) + CHỦ ĐỀ 3 (CÂU 17 - 25)
% =========================================================================
\begin{enumerate}[resume]
\item Hai lực $\vec{F}_1$ và $\vec{F}_2$ cùng tác dụng vào một chất điểm tại điểm $O$, có phương vuông góc với nhau. Biết độ lớn của các lực lần lượt là $|\vec{F}_1| = 30\text{ N}$ và $|\vec{F}_2| = 40\text{ N}$. Tính độ lớn của hợp lực $\vec{F} = \vec{F}_1 + \vec{F}_2$ tác dụng lên chất điểm (theo đơn vị Niutơn).
\answerbox

\item Hai lực $\vec{F}_1$ và $\vec{F}_2$ có cùng độ lớn bằng $50\text{ N}$, cùng tác dụng vào một vật tại điểm $O$ và tạo với nhau một góc bằng $120^\circ$. Tính độ lớn của hợp lực tác dụng lên vật (theo đơn vị Niutơn).
\answerbox

\item Một chiếc ca nô chuyển động thẳng đều trên sông từ bến $A$ sang bờ đối diện. Vận tốc riêng của ca nô đối với dòng nước là $v_1 = 20\text{ km/h}$ hướng vuông góc với dòng chảy, vận tốc dòng nước chảy xuôi dòng dọc theo bờ là $v_2 = 15\text{ km/h}$. Tính độ lớn vận tốc thực tế của ca nô so với bờ sông (theo đơn vị km/h).
\answerbox

\item Cho bốn điểm phân biệt $A, B, C, D$. Rút gọn biểu thức vectơ $\vec{u} = \vec{AB} - \vec{CB} + \vec{CD} - \vec{AD}$. Hỏi độ dài của vectơ $\vec{u}$ bằng bao nhiêu?
\answerbox

\parttitle{CHỦ ĐỀ 3. TÍCH CỦA MỘT VECTƠ VỚI MỘT SỐ (CÂU 17 -- 28)}

\item Cho đoạn thẳng $AB$ có độ dài bằng $12\text{ cm}$. Điểm $M$ thuộc đoạn thẳng $AB$ sao cho $AM = 3MB$. Đặt $\vec{AM} = k \vec{AB}$. Tìm giá trị của số thực $k$ (viết dưới dạng số thập phân).
\answerbox

\item Cho tam giác $ABC$ có trọng tâm $G$. Biết rằng $\vec{AB} + \vec{AC} = k \vec{AG}$. Tìm giá trị của số thực $k$.
\answerbox

\item Cho tam giác $ABC$. Gọi $M$ là điểm trên cạnh $BC$ sao cho $BM = 2MC$. Phân tích vectơ $\vec{AM}$ theo hai vectơ $\vec{AB}$ và $\vec{AC}$ dưới dạng $\vec{AM} = x \vec{AB} + y \vec{AC}$. Tính giá trị của biểu thức $P = 3x + 6y$.
\answerbox

\item Cho hình bình hành $ABCD$. Gọi $I$ là trung điểm của cạnh $CD$. Phân tích vectơ $\vec{AI}$ theo hai vectơ $\vec{a} = \vec{AB}$ và $\vec{b} = \vec{AD}$ dưới dạng $\vec{AI} = m\vec{a} + n\vec{b}$. Tính giá trị biểu thức $T = 2m + 4n$.
\answerbox

\item Cho tam giác $ABC$ có trọng tâm $G$. Lấy điểm $M$ thỏa mãn $\vec{AM} = \frac{2}{3}\vec{AB}$ và điểm $N$ trên cạnh $AC$ thỏa mãn $\vec{AN} = k \vec{AC}$. Biết ba điểm $M, G, N$ thẳng hàng và $k$ được viết dưới dạng phân số tối giản $\frac{a}{b}$ ($a, b \in \mathbb{N}^*$). Tính giá trị của $a + b$.
\answerbox

\item Cho tam giác $ABC$. Gọi $I$ là điểm thỏa mãn hệ thức vectơ $\vec{IA} + 3\vec{IB} = \vec{0}$. Tính tỉ số độ dài $\dfrac{IA}{IB}$.
\answerbox

\item Cho tam giác $ABC$ đều có cạnh bằng $6\text{ cm}$. Tập hợp các điểm $M$ thỏa mãn đẳng thức $|2\vec{MA} + \vec{MB} + \vec{MC}| = 12$ là một đường tròn có bán kính $R$ bằng bao nhiêu xentimét?
\answerbox

\item Cho đoạn thẳng $AB$ có độ dài bằng $8\text{ cm}$. Gọi $I$ là trung điểm của đoạn thẳng $AB$. Tập hợp các điểm $M$ thỏa mãn đẳng thức $|\vec{MA} + \vec{MB}| = 10$ là một đường tròn có đường kính bằng bao nhiêu xentimét?
\answerbox

\item Cho tam giác $ABC$ có trọng tâm $G$. Với điểm $O$ bất kì, ta luôn có hệ thức $\vec{OA} + \vec{OB} + \vec{OC} = k \vec{OG}$. Tìm giá trị của hằng số $k$.
\answerbox

\end{enumerate}

\newpage

% =========================================================================
% TRANG 3: TIẾP CHỦ ĐỀ 3 (CÂU 26 - 28) + CHỦ ĐỀ 4 (CÂU 29 - 38)
% =========================================================================
\begin{enumerate}[resume]
\item Một chiếc đèn trang trí có trọng lượng $P = 60\text{ N}$ được treo cân bằng vào trần nhà nhờ hai sợi dây cáp đối xứng $OA$ và $OB$. Biết hai sợi dây cáp hợp với nhau một góc bằng $120^\circ$ và độ lớn lực căng của hai sợi dây là như nhau ($|\vec{T}_1| = |\vec{T}_2|$). Tính độ lớn lực căng $T_1$ của mỗi sợi dây (theo đơn vị Niutơn).
\answerbox

\item Ba lực $\vec{F}_1, \vec{F}_2, \vec{F}_3$ cùng tác dụng vào một chất điểm tại điểm $O$ và vật ở trạng thái cân bằng ($\vec{F}_1 + \vec{F}_2 + \vec{F}_3 = \vec{0}$). Biết rằng hai lực $\vec{F}_1, \vec{F}_2$ vuông góc với nhau và có độ lớn lần lượt là $|\vec{F}_1| = 12\text{ N}$, $|\vec{F}_2| = 16\text{ N}$. Tính độ lớn của lực $\vec{F}_3$ (theo đơn vị Niutơn).
\answerbox

\item Cho tam giác $ABC$ vuông tại $A$ có $AB = 3$ và $AC = 4$. Tính giá trị của $|\vec{AB} + 2\vec{AC}|^2$.
\answerbox

\parttitle{CHỦ ĐỀ 4. VECTƠ TRONG MẶT PHẲNG TOẠ ĐỘ (CÂU 29 -- 38)}

\item Trong mặt phẳng toạ độ $Oxy$, cho vectơ $\vec{u} = 3\vec{i} - 5\vec{j}$ (với $\vec{i}, \vec{j}$ là hai vectơ đơn vị trên các trục $Ox, Oy$). Gọi $(x_0; y_0)$ là toạ độ của vectơ $\vec{u}$. Tính giá trị của biểu thức $T = 2x_0 + 3y_0$.
\answerbox

\item Trong mặt phẳng toạ độ $Oxy$, cho hai điểm $A(-2; 5)$ và $B(4; -3)$. Tính độ dài của vectơ $\vec{AB}$.
\answerbox

\item Trong mặt phẳng toạ độ $Oxy$, cho hai vectơ $\vec{a} = (2; -4)$ và $\vec{b} = (-3; 1)$. Gọi $\vec{u} = 3\vec{a} - 2\vec{b}$. Tính tổng hoành độ và tung độ của vectơ $\vec{u}$.
\answerbox

\item Trong mặt phẳng toạ độ $Oxy$, cho tam giác $ABC$ có $A(1; 3)$, $B(-2; 4)$ và trọng tâm $G(2; 1)$. Tìm toạ độ đỉnh $C(x_C; y_C)$ và tính giá trị của $x_C + y_C$.
\answerbox

\item Trong mặt phẳng toạ độ $Oxy$, cho ba điểm $A(-1; 2)$, $B(3; 5)$ và $C(5; 1)$. Tìm toạ độ đỉnh $D(x_D; y_D)$ để tứ giác $ABCD$ là một hình bình hành. Tính giá trị của tích $x_D \cdot y_D$.
\answerbox

\item Trong mặt phẳng toạ độ $Oxy$, cho hai vectơ $\vec{u} = (m - 1; 2)$ và $\vec{v} = (3; m)$ (với $m$ là tham số thực). Tìm giá trị nguyên dương của $m$ để hai vectơ $\vec{u}$ và $\vec{v}$ cùng phương.
\answerbox

\item Trong mặt phẳng toạ độ $Oxy$, cho ba điểm $A(1; 2)$, $B(3; 6)$ và $C(m; 10)$ (với $m$ là tham số thực). Tìm giá trị của $m$ để ba điểm $A, B, C$ thẳng hàng.
\answerbox

\item Trong mặt phẳng toạ độ $Oxy$, cho hai điểm $A(2; 4)$ và $B(-1; 1)$. Điểm $M(x_0; 0)$ thuộc trục hoành $Ox$ sao cho ba điểm $A, B, M$ thẳng hàng. Tìm giá trị của hoành độ $x_0$.
\answerbox

\item Trong mặt phẳng toạ độ $Oxy$, cho hai điểm $A(1; -2)$ và $B(7; 4)$. Điểm $M(x_M; y_M)$ thuộc đoạn thẳng $AB$ thỏa mãn $AM = 2 MB$. Tính giá trị của $x_M + y_M$.
\answerbox

\item Trong bản đồ quy hoạch một khu đô thị gắn với hệ trục toạ độ $Oxy$ (đơn vị trên các trục tính bằng kilômét), ba công trình công cộng lần lượt đặt tại $A(1; 3)$, $B(5; 2)$ và $C(3; 7)$. Người ta xây dựng một trung tâm điều hành dịch vụ tại trọng tâm $G$ của tam giác $ABC$. Tính khoảng cách từ trung tâm $G$ đến gốc toạ độ $O$ (theo đơn vị kilômét).
\answerbox

\end{enumerate}

\newpage

% =========================================================================
% TRANG 4: CHỦ ĐỀ 5 (CÂU 39 - 50)
% =========================================================================
\parttitle{CHỦ ĐỀ 5. TÍCH VÔ HƯỚNG CỦA HAI VECTƠ VÀ BÀI TẬP CUỐI CHƯƠNG (CÂU 39 -- 50)}

\begin{enumerate}[resume]
\item Cho tam giác đều $ABC$ có độ dài cạnh bằng $6$. Tính giá trị của tích vô hướng $\vec{AB} \cdot \vec{AC}$.
\answerbox

\item Cho hình thoi $ABCD$ có cạnh bằng $4$ và góc $\widehat{BAD} = 120^\circ$. Tính giá trị của tích vô hướng $\vec{AB} \cdot \vec{AD}$.
\answerbox

\item Trong mặt phẳng toạ độ $Oxy$, cho hai vectơ $\vec{a} = (3; -2)$ và $\vec{b} = (4; 5)$. Tính giá trị của tích vô hướng $\vec{a} \cdot \vec{b}$.
\answerbox

\item Trong mặt phẳng toạ độ $Oxy$, cho hai vectơ $\vec{u} = (2; 1)$ và $\vec{v} = (3; -1)$. Tính góc giữa hai vectơ $\vec{u}$ và $\vec{v}$ (theo đơn vị độ).
\answerbox

\item Trong mặt phẳng toạ độ $Oxy$, cho hai vectơ $\vec{a} = (m - 1; 3)$ và $\vec{b} = (2; -4)$ (với $m$ là tham số thực). Tìm giá trị của $m$ để hai vectơ $\vec{a}$ và $\vec{b}$ vuông góc với nhau.
\answerbox

\item Trong mặt phẳng toạ độ $Oxy$, cho ba điểm $A(1; 2)$, $B(-2; 1)$ và $C(m; 5)$ (với $m$ là tham số thực). Tìm giá trị của $m$ để tam giác $ABC$ vuông tại $A$.
\answerbox

\item Một công nhân kéo một xe hàng trên quãng đường thẳng dài $s = 20\text{ m}$ trên mặt sàn phẳng nằm ngang bằng một lực $\vec{F}$ có độ lớn $150\text{ N}$. Hướng của lực kéo hợp với phương chuyển động một góc $\alpha = 60^\circ$. Tính công sinh bởi lực kéo $\vec{F}$ (theo đơn vị Jun - $\text{J}$).
\answerbox

\item Một kiện hàng có khối lượng $m = 5\text{ kg}$ trượt từ đỉnh xuống chân một dốc trượt dài $l = 10\text{ m}$ nghiêng một góc $30^\circ$ so với mặt đất nằm ngang. Lấy gia tốc trọng trường $g = 10\text{ m/s}^2$. Tính công của trọng lực tác dụng lên kiện hàng trong suốt quá trình trượt từ đỉnh xuống chân dốc (theo đơn vị Jun - $\text{J}$).
\answerbox

\item Trong mặt phẳng toạ độ $Oxy$, cho tam giác $ABC$ có $A(1; 3)$, $B(-1; 1)$ và $C(4; 1)$. Gọi $H(x_H; y_H)$ là trực tâm của tam giác $ABC$. Tính giá trị của $x_H + y_H$.
\answerbox

\item Trong mặt phẳng toạ độ $Oxy$, cho tam giác $ABC$ có ba đỉnh $A(1; 7)$, $B(5; 5)$ và $C(-2; -2)$. Gọi $I(x_I; y_I)$ là tâm đường tròn ngoại tiếp của tam giác $ABC$. Tính giá trị của biểu thức $P = x_I + 2y_I$.
\answerbox

\item Cho hình thang vuông $ABCD$ vuông tại $A$ và $D$ có đáy nhỏ $AB = 3$, đáy lớn $CD = 6$, chiều cao $AD = 4$. Tính giá trị của tích vô hướng $\vec{AC} \cdot \vec{BD}$.
\answerbox

\item Trong mặt phẳng toạ độ $Oxy$, cho hai điểm $A(1; 3)$ và $B(4; 2)$. Điểm $M(x_0; 0)$ di động trên trục hoành $Ox$. Tìm giá trị của hoành độ $x_0$ để biểu thức $T = |\vec{MA} + 2\vec{MB}|$ đạt giá trị nhỏ nhất.
\answerbox

\end{enumerate}

% =========================================================================
% TRANG 5 (ĐÁP ÁN TRANG 1/4): BẢNG ĐÁP ÁN 50 CÂU + LỜI GIẢI CHỦ ĐỀ 1
% =========================================================================
\newpage
\pagestyle{dapan}

\parttitle{BẢNG ĐÁP ÁN 50 CÂU TRẢ LỜI NGẮN}

\begin{center}
\begin{tabular}{|c|c||c|c||c|c||c|c||c|c|}
\hline
\textbf{Câu} & \textbf{Đáp số} & \textbf{Câu} & \textbf{Đáp số} & \textbf{Câu} & \textbf{Đáp số} & \textbf{Câu} & \textbf{Đáp số} & \textbf{Câu} & \textbf{Đáp số} \\
\hline\hline
\textbf{1} & $20$ & \textbf{11} & $288$ & \textbf{21} & $5$ & \textbf{31} & $-2$ & \textbf{41} & $2$ \\
\hline
\textbf{2} & $42$ & \textbf{12} & $5$ & \textbf{22} & $3$ & \textbf{32} & $3$ & \textbf{42} & $45^\circ$ \\
\hline
\textbf{3} & $3$ & \textbf{13} & $50$ & \textbf{23} & $3$ & \textbf{33} & $-2$ & \textbf{43} & $7$ \\
\hline
\textbf{4} & $3$ & \textbf{14} & $50$ & \textbf{24} & $10$ & \textbf{34} & $3$ & \textbf{44} & $0$ \\
\hline
\textbf{5} & $4$ & \textbf{15} & $25$ & \textbf{25} & $3$ & \textbf{35} & $5$ & \textbf{45} & $1500$ \\
\hline
\textbf{6} & $14$ & \textbf{16} & $0$ & \textbf{26} & $60$ & \textbf{36} & $-2$ & \textbf{46} & $250$ \\
\hline
\textbf{7} & $10$ & \textbf{17} & $0{,}75$ & \textbf{27} & $20$ & \textbf{37} & $7$ & \textbf{47} & $5$ \\
\hline
\textbf{8} & $5$ & \textbf{18} & $3$ & \textbf{28} & $73$ & \textbf{38} & $5$ & \textbf{48} & $5$ \\
\hline
\textbf{9} & $6$ & \textbf{19} & $5$ & \textbf{29} & $-9$ & \textbf{39} & $18$ & \textbf{49} & $-2$ \\
\hline
\textbf{10} & $8$ & \textbf{20} & $5$ & \textbf{30} & $10$ & \textbf{40} & $-8$ & \textbf{50} & $3$ \\
\hline
\end{tabular}
\end{center}

\vspace{0.15cm}
\parttitle{HƯỚNG DẪN GIẢI CHI TIẾT TỪNG CHỦ ĐỀ}

\noindent\textbf{\large Chủ đề 1. Các khái niệm mở đầu}
\begin{itemize}[leftmargin=1.5em, itemsep=2.5pt]
    \item \textbf{Câu 1:} Một vectơ khác $\vec{0}$ được xác định bởi 2 đỉnh phân biệt có thứ tự. Số vectơ là chỉnh hợp $A_5^2 = 5 \times 4 = 20$.
    \item \textbf{Câu 2:} Tập hợp gồm 6 đỉnh và tâm $O$, tổng cộng $7$ điểm phân biệt. Số vectơ khác $\vec{0}$ là $A_7^2 = 7 \times 6 = 42$.
    \item \textbf{Câu 3:} Các vectơ có cùng độ dài, cùng phương và cùng hướng với $\vec{AB}$ trong hình lục giác đều $ABCDEF$ tâm $O$ gồm: $\vec{FO}, \vec{OC}, \vec{ED}$. Do đó có $3$ vectơ khác $\vec{AB}$ thỏa mãn.
    \item \textbf{Câu 4:} $MN$ là đường trung bình của tam giác đều $ABC \Rightarrow MN = \frac{1}{2}BC = \frac{1}{2} \cdot 6 = 3\text{ cm}$. Độ dài $|\vec{MN}| = MN = 3$.
    \item \textbf{Câu 5:} Đường chéo hình vuông $AC = 4\sqrt{2} \cdot \sqrt{2} = 8\text{ cm}$. Do $O$ là trung điểm $AC$ nên $OA = \frac{1}{2}AC = 4\text{ cm} \Rightarrow |\vec{OA}| = 4$.
    \item \textbf{Câu 6:} Đường thẳng $AB$ chứa 3 điểm $A, M, B \Rightarrow A_3^2 = 6$ vectơ. Đoạn $QP$ song song $AB$ chứa 2 điểm $Q, P \Rightarrow A_2^2 = 2$ vectơ. Đường thẳng $CD$ song song $AB$ chứa 3 điểm $D, P, C \Rightarrow A_3^2 = 6$ vectơ. Tổng số vectơ cùng phương với $\vec{AB}$ là: $6 + 2 + 6 = 14$.
\end{itemize}

\vspace{0.2cm}
\begin{center}
\begin{tikzpicture}[scale=0.85]
    % Minh hoạ lục giác đều Câu 3
    \foreach \i in {0,60,120,180,240,300} {
        \coordinate (P\i) at (\i:1.8);
    }
    \coordinate (O) at (0,0);
    \draw[thick, ink] (P0) -- (P60) -- (P120) -- (P180) -- (P240) -- (P300) -- cycle;
    \draw[dashed, gray!60] (P0) -- (P180) (P60) -- (P240) (P120) -- (P300);
    \fill[ink] (O) circle (2pt) node[below right, font=\footnotesize] {$O$};
    \node[right, font=\footnotesize\bfseries] at (P0) {$B$};
    \node[above right, font=\footnotesize\bfseries] at (P60) {$A$};
    \node[above left, font=\footnotesize\bfseries] at (P120) {$F$};
    \node[left, font=\footnotesize\bfseries] at (P180) {$E$};
    \node[below left, font=\footnotesize\bfseries] at (P240) {$D$};
    \node[below right, font=\footnotesize\bfseries] at (P300) {$C$};
    % Vẽ các vectơ bằng nhau
    \draw[-{Latex[length=2.5mm]}, line width=1.3pt, red!80!black] (P60) -- (P0) node[midway, right, font=\footnotesize] {$\vec{AB}$};
    \draw[-{Latex[length=2.5mm]}, line width=1.3pt, blue!80!black] (P120) -- (O);
    \draw[-{Latex[length=2.5mm]}, line width=1.3pt, blue!80!black] (O) -- (P300);
    \draw[-{Latex[length=2.5mm]}, line width=1.3pt, blue!80!black] (P180) -- (P240);
    \node[font=\footnotesize\itshape\color{ink}] at (0,-2.3) {Minh họa Câu 3: Ba vectơ cùng hướng và cùng độ dài bằng $\vec{AB}$ là $\vec{FO}, \vec{OC}, \vec{ED}$};
\end{tikzpicture}
\end{center}

\newpage

% =========================================================================
% TRANG 6 (ĐÁP ÁN TRANG 2/4): LỜI GIẢI CHỦ ĐỀ 2 (CÂU 7 - 16)
% =========================================================================
\noindent\textbf{\large Chủ đề 2. Tổng và hiệu của hai vectơ}
\begin{itemize}[leftmargin=1.5em, itemsep=2.5pt]
    \item \textbf{Câu 7:} Theo quy tắc hình chữ nhật, $\vec{AB} + \vec{AD} = \vec{AC}$. Độ dài $|\vec{u}| = AC = \sqrt{AB^2 + AD^2} = \sqrt{6^2 + 8^2} = 10$.
    \item \textbf{Câu 8:} Theo quy tắc hiệu, $\vec{AB} - \vec{AD} = \vec{DB}$. Vì tam giác $ABD$ có $AB = AD = 5$ và $\widehat{BAD} = 60^\circ$ nên tam giác $ABD$ đều $\Rightarrow DB = 5 \Rightarrow |\vec{v}| = 5$.
    \item \textbf{Câu 9:} Gọi $H$ là trung điểm cạnh $BC$, theo quy tắc trung điểm ta có $\vec{AB} + \vec{AC} = 2\vec{AH}$. Chiều cao tam giác đều $AH = \frac{2\sqrt{3} \cdot \sqrt{3}}{2} = 3 \Rightarrow |\vec{w}| = 2 AH = 6$.
    \item \textbf{Câu 10:} $\vec{AB} - \vec{AC} = \vec{CB} \Rightarrow |\vec{AB} - \vec{AC}| = CB = 8$.
    \item \textbf{Câu 11:} Vì $\vec{AB} + \vec{AD} = \vec{AC}$ nên $\vec{AB} + \vec{AC} + \vec{AD} = 2\vec{AC}$. Đường chéo $AC = 6\sqrt{2}$. Do đó $|2\vec{AC}|^2 = 4 AC^2 = 4 \cdot 72 = 288$.
    \item \textbf{Câu 12:} $\vec{AB} - \vec{CA} = \vec{AB} + \vec{AC}$. Vì tam giác vuông tại $A$, dựng hình chữ nhật $ABDC$ thì $\vec{AB} + \vec{AC} = \vec{AD}$, $|\vec{u}| = AD = \sqrt{3^2 + 4^2} = 5$.
    \item \textbf{Câu 13:} Do hai lực $\vec{F}_1 \perp \vec{F}_2$ nên độ lớn hợp lực là: $|\vec{F}| = \sqrt{F_1^2 + F_2^2} = \sqrt{30^2 + 40^2} = 50\text{ N}$.
    \item \textbf{Câu 14:} Hợp lực $F = \sqrt{F_1^2 + F_2^2 + 2F_1 F_2 \cos 120^\circ} = \sqrt{50^2 + 50^2 + 2 \cdot 50 \cdot 50 \cdot (-0{,}5)} = 50\text{ N}$.
    \item \textbf{Câu 15:} Vận tốc thực tế $\vec{v} = \vec{v}_1 + \vec{v}_2$. Do hai vận tốc vuông góc: $v = \sqrt{v_1^2 + v_2^2} = \sqrt{20^2 + 15^2} = 25\text{ km/h}$.
    \item \textbf{Câu 16:} $\vec{u} = (\vec{AB} - \vec{CB}) + (\vec{CD} - \vec{AD}) = (\vec{AB} + \vec{BC}) + (\vec{CD} + \vec{DA}) = \vec{AC} + \vec{CA} = \vec{0} \Rightarrow |\vec{u}| = 0$.
\end{itemize}

\vspace{0.25cm}
\begin{center}
\begin{tikzpicture}[scale=0.9]
    % Hình Câu 13 & 14: Hợp lực
    \coordinate (O) at (0,0);
    \draw[-{Latex[length=2.5mm]}, line width=1.3pt, blue!80!black] (O) -- (3,0) node[below=2pt, font=\footnotesize\bfseries] {$\vec{F}_1 (30\text{ N})$};
    \draw[-{Latex[length=2.5mm]}, line width=1.3pt, blue!80!black] (O) -- (0,4) node[left=2pt, font=\footnotesize\bfseries] {$\vec{F}_2 (40\text{ N})$};
    \draw[dashed, gray] (3,0) -- (3,4) -- (0,4);
    \draw[-{Latex[length=3mm]}, line width=1.5pt, red!80!black] (O) -- (3,4) node[above right=1pt, font=\footnotesize\bfseries] {$\vec{F} = \vec{F}_1 + \vec{F}_2 (50\text{ N})$};
    \fill[black] (O) circle (2.5pt) node[below left] {$O$};
    \node[font=\footnotesize\itshape\color{ink}] at (1.5,-0.8) {Hình 1: Hợp lực của hai lực vuông góc (Câu 13)};

    \begin{scope}[xshift=7cm]
        \coordinate (O2) at (0,0);
        \draw[-{Latex[length=2.5mm]}, line width=1.3pt, blue!80!black] (O2) -- (3,0) node[below=2pt, font=\footnotesize\bfseries] {$\vec{F}_1 (50\text{ N})$};
        \draw[-{Latex[length=2.5mm]}, line width=1.3pt, blue!80!black] (O2) -- (-1.5, 2.598) node[above left=1pt, font=\footnotesize\bfseries] {$\vec{F}_2 (50\text{ N})$};
        \draw[dashed, gray] (3,0) -- (1.5, 2.598) -- (-1.5, 2.598);
        \draw[-{Latex[length=3mm]}, line width=1.5pt, red!80!black] (O2) -- (1.5, 2.598) node[above=2pt, font=\footnotesize\bfseries] {$\vec{F} (50\text{ N})$};
        \draw (0.6,0) arc (0:120:0.6);
        \node[font=\footnotesize] at (0.3, 0.7) {$120^\circ$};
        \fill[black] (O2) circle (2.5pt) node[below left] {$O$};
        \node[font=\footnotesize\itshape\color{ink}] at (0.8,-0.8) {Hình 2: Hợp lực của hai lực góc $120^\circ$ (Câu 14)};
    \end{scope}
\end{tikzpicture}
\end{center}

\newpage

% =========================================================================
% TRANG 7 (ĐÁP ÁN TRANG 3/4): LỜI GIẢI CHỦ ĐỀ 3 (CÂU 17 - 28)
% =========================================================================
\noindent\textbf{\large Chủ đề 3. Tích của một vectơ với một số}
\begin{itemize}[leftmargin=1.5em, itemsep=2.5pt]
    \item \textbf{Câu 17:} Do $M$ nằm giữa $A$ và $B$ và $AM = 3MB \Rightarrow AM = \frac{3}{4}AB$. Hai vectơ $\vec{AM}$ và $\vec{AB}$ cùng hướng nên $k = \frac{3}{4} = 0{,}75$.
    \item \textbf{Câu 18:} Gọi $M$ là trung điểm $BC$, ta có $\vec{AB} + \vec{AC} = 2\vec{AM} = 2 \cdot \left(\frac{3}{2}\vec{AG}\right) = 3\vec{AG} \Rightarrow k = 3$.
    \item \textbf{Câu 19:} $\vec{AM} = \vec{AB} + \frac{2}{3}\vec{BC} = \vec{AB} + \frac{2}{3}(\vec{AC} - \vec{AB}) = \frac{1}{3}\vec{AB} + \frac{2}{3}\vec{AC} \Rightarrow x = \frac{1}{3}, y = \frac{2}{3}$. Do đó $P = 3x + 6y = 1 + 4 = 5$.
    \item \textbf{Câu 20:} $\vec{AI} = \vec{AD} + \vec{DI} = \vec{AD} + \frac{1}{2}\vec{AB} = \frac{1}{2}\vec{a} + \vec{b} \Rightarrow m = \frac{1}{2}, n = 1 \Rightarrow T = 2m + 4n = 5$.
    \item \textbf{Câu 21:} Biểu diễn qua $\vec{AB}, \vec{AC}$: $\vec{AM} = \frac{2}{3}\vec{AB}$, $\vec{AG} = \frac{1}{3}\vec{AB} + \frac{1}{3}\vec{AC}$, $\vec{AN} = k \vec{AC}$. Ta có $\vec{GM} = \frac{1}{3}\vec{AB} - \frac{1}{3}\vec{AC}$, $\vec{GN} = -\frac{1}{3}\vec{AB} + \left(k - \frac{1}{3}\right)\vec{AC}$. Để $M, G, N$ thẳng hàng thì $\vec{GN} = -\vec{GM} \Rightarrow k - \frac{1}{3} = \frac{1}{3} \Rightarrow k = \frac{2}{3}$. Vậy $a = 2, b = 3 \Rightarrow a + b = 5$.
    \item \textbf{Câu 22:} $\vec{IA} + 3\vec{IB} = \vec{0} \Rightarrow \vec{IA} = -3\vec{IB} \Rightarrow IA = 3IB \Rightarrow \dfrac{IA}{IB} = 3$.
    \item \textbf{Câu 23:} Gọi $I$ là điểm thỏa mãn $2\vec{IA} + \vec{IB} + \vec{IC} = \vec{0}$ ($I$ là trung điểm của đoạn thẳng nối $A$ và trung điểm cạnh $BC$). Khi đó $|2\vec{MA} + \vec{MB} + \vec{MC}| = |4\vec{MI}| = 4MI = 12 \Rightarrow MI = 3\text{ cm}$. Bán kính đường tròn $R = 3$.
    \item \textbf{Câu 24:} Gọi $I$ là trung điểm của $AB$, $|\vec{MA} + \vec{MB}| = |2\vec{MI}| = 10 \Leftrightarrow MI = 5$. Tập hợp là đường tròn bán kính $R = 5\text{ cm} \Rightarrow$ đường kính $d = 2R = 10\text{ cm}$.
    \item \textbf{Câu 25:} $\vec{OA} + \vec{OB} + \vec{OC} = 3\vec{OG} + (\vec{GA} + \vec{GB} + \vec{GC}) = 3\vec{OG} \Rightarrow k = 3$.
    \item \textbf{Câu 26:} Do hai sợi dây cáp đối xứng, góc giữa mỗi sợi dây và phương thẳng đứng là $\frac{120^\circ}{2} = 60^\circ$. Điều kiện cân bằng theo phương thẳng đứng: $2 T_1 \cos 60^\circ = P \Rightarrow 2 T_1 \cdot 0{,}5 = 60 \Rightarrow T_1 = 60\text{ N}$.
    \item \textbf{Câu 27:} Vì vật cân bằng nên $\vec{F}_1 + \vec{F}_2 + \vec{F}_3 = \vec{0} \Rightarrow \vec{F}_3 = -(\vec{F}_1 + \vec{F}_2) \Rightarrow |\vec{F}_3| = \sqrt{F_1^2 + F_2^2} = \sqrt{12^2 + 16^2} = 20\text{ N}$.
    \item \textbf{Câu 28:} $|\vec{AB} + 2\vec{AC}|^2 = AB^2 + 4 AC^2 + 4\vec{AB}\cdot\vec{AC} = 3^2 + 4 \cdot 4^2 + 0 = 9 + 64 = 73$.
\end{itemize}

\vspace{0.25cm}
\begin{center}
\begin{tikzpicture}[scale=0.95]
    % Minh hoạ bài toán Câu 26 treo đèn
    \draw[thick, gray!70] (-2.5,2.6) -- (2.5,2.6);
    \fill[pattern=north east lines, pattern color=gray!50] (-2.5,2.6) rectangle (2.5,2.8);
    \coordinate (O) at (0,0);
    \coordinate (A) at (-1.5,2.6);
    \coordinate (B) at (1.5,2.6);
    \draw[line width=1.2pt, ink] (O) -- (A) node[midway, left=2pt, font=\footnotesize] {$\vec{T}_1$};
    \draw[line width=1.2pt, ink] (O) -- (B) node[midway, right=2pt, font=\footnotesize] {$\vec{T}_2$};
    \draw[-{Latex[length=2.5mm]}, line width=1.3pt, red!80!black] (O) -- (0,-1.8) node[right=2pt, font=\footnotesize\bfseries] {$\vec{P} (60\text{ N})$};
    \draw[dashed, gray] (O) -- (0,2.6);
    \draw (-0.3,0.5) arc (120:60:0.6);
    \node[font=\footnotesize] at (0, 0.9) {$120^\circ$};
    \fill[black] (O) circle (2.5pt) node[below right=1pt, font=\footnotesize] {$O$};
    \node[font=\footnotesize\itshape\color{ink}] at (0,-2.3) {Minh họa Câu 26: Hệ cân bằng tĩnh học hai sợi dây cáp đối xứng treo đèn chùm};
\end{tikzpicture}
\end{center}

\newpage

% =========================================================================
% TRANG 8 (ĐÁP ÁN TRANG 4/4): LỜI GIẢI CHỦ ĐỀ 4 (CÂU 29 - 38) & CHỦ ĐỀ 5 (CÂU 39 - 50)
% =========================================================================
\noindent\textbf{\large Chủ đề 4. Vectơ trong mặt phẳng toạ độ}
\begin{itemize}[leftmargin=1.5em, itemsep=1.8pt]
    \item \textbf{Câu 29:} Vectơ $\vec{u} = (3; -5) \Rightarrow x_0 = 3, y_0 = -5 \Rightarrow T = 2(3) + 3(-5) = 6 - 15 = -9$.
    \item \textbf{Câu 30:} $\vec{AB} = (4 - (-2); -3 - 5) = (6; -8) \Rightarrow |\vec{AB}| = \sqrt{6^2 + (-8)^2} = 10$.
    \item \textbf{Câu 31:} $\vec{u} = 3(2; -4) - 2(-3; 1) = (6 + 6; -12 - 2) = (12; -14)$. Tổng hoành độ và tung độ là $12 + (-14) = -2$.
    \item \textbf{Câu 32:} $x_C = 3x_G - x_A - x_B = 3(2) - 1 - (-2) = 7$; $y_C = 3y_G - y_A - y_B = 3(1) - 3 - 4 = -4$. Suy ra $x_C + y_C = 7 + (-4) = 3$.
    \item \textbf{Câu 33:} $ABCD$ là hình bình hành $\Leftrightarrow \vec{AD} = \vec{BC} \Leftrightarrow (x_D + 1; y_D - 2) = (2; -4) \Rightarrow x_D = 1, y_D = -2$. Tích $x_D \cdot y_D = 1 \cdot (-2) = -2$.
    \item \textbf{Câu 34:} Hai vectơ cùng phương $\Leftrightarrow (m - 1)m - 2 \cdot 3 = 0 \Leftrightarrow m^2 - m - 6 = 0 \Leftrightarrow m = 3$ hoặc $m = -2$. Do $m$ nguyên dương nên $m = 3$.
    \item \textbf{Câu 35:} $\vec{AB} = (2; 4)$, $\vec{AC} = (m - 1; 8)$. Ba điểm thẳng hàng $\Leftrightarrow \frac{m - 1}{2} = \frac{8}{4} = 2 \Rightarrow m = 5$.
    \item \textbf{Câu 36:} $\vec{AB} = (-3; -3)$, $\vec{AM} = (x_0 - 2; -4)$. Thẳng hàng $\Leftrightarrow \frac{x_0 - 2}{-3} = \frac{-4}{-3} \Rightarrow x_0 - 2 = -4 \Rightarrow x_0 = -2$.
    \item \textbf{Câu 37:} $\vec{AM} = 2\vec{MB} \Leftrightarrow x_M = \frac{x_A + 2x_B}{3} = \frac{1 + 14}{3} = 5$; $y_M = \frac{y_A + 2y_B}{3} = \frac{-2 + 8}{3} = 2$. Do đó $x_M + y_M = 5 + 2 = 7$.
    \item \textbf{Câu 38:} Toạ độ trọng tâm $G\left(\frac{1+5+3}{3}; \frac{3+2+7}{3}\right) = (3; 4)$. Khoảng cách $OG = \sqrt{3^2 + 4^2} = 5\text{ km}$.
\end{itemize}

\vspace{0.15cm}
\noindent\textbf{\large Chủ đề 5. Tích vô hướng của hai vectơ và bài tập cuối chương}
\begin{itemize}[leftmargin=1.5em, itemsep=1.8pt]
    \item \textbf{Câu 39:} $\vec{AB} \cdot \vec{AC} = AB \cdot AC \cdot \cos 60^\circ = 6 \cdot 6 \cdot 0{,}5 = 18$.
    \item \textbf{Câu 40:} $\vec{AB} \cdot \vec{AD} = AB \cdot AD \cdot \cos 120^\circ = 4 \cdot 4 \cdot (-0{,}5) = -8$.
    \item \textbf{Câu 41:} $\vec{a} \cdot \vec{b} = 3 \cdot 4 + (-2) \cdot 5 = 12 - 10 = 2$.
    \item \textbf{Câu 42:} $\cos(\vec{u}, \vec{v}) = \frac{2 \cdot 3 + 1 \cdot (-1)}{\sqrt{2^2 + 1^2} \sqrt{3^2 + (-1)^2}} = \frac{5}{\sqrt{5}\sqrt{10}} = \frac{1}{\sqrt{2}} \Rightarrow (\vec{u}, \vec{v}) = 45^\circ$.
    \item \textbf{Câu 43:} $\vec{a} \perp \vec{b} \Leftrightarrow 2(m - 1) + 3(-4) = 0 \Leftrightarrow 2m - 14 = 0 \Leftrightarrow m = 7$.
    \item \textbf{Câu 44:} $\vec{AB} = (-3; -1)$, $\vec{AC} = (m - 1; 3)$. $\triangle ABC$ vuông tại $A \Leftrightarrow \vec{AB} \cdot \vec{AC} = 0 \Leftrightarrow -3(m - 1) - 3 = 0 \Leftrightarrow -3m = 0 \Leftrightarrow m = 0$.
    \item \textbf{Câu 45:} Công thực hiện: $A = F \cdot s \cdot \cos \alpha = 150 \cdot 20 \cdot \cos 60^\circ = 3000 \cdot 0{,}5 = 1500\text{ J}$.
    \item \textbf{Câu 46:} Độ lớn trọng lực $P = mg = 5 \cdot 10 = 50\text{ N}$. Chiều cao dốc $h = l \sin 30^\circ = 10 \cdot 0{,}5 = 5\text{ m}$. Công của trọng lực $A = P \cdot h = 50 \cdot 5 = 250\text{ J}$.
    \item \textbf{Câu 47:} $\vec{BC} = (5; 0)$, $\vec{AC} = (3; -2)$. $H(x; y)$ là trực tâm $\Rightarrow \begin{cases} \vec{AH} \cdot \vec{BC} = 0 \\ \vec{BH} \cdot \vec{AC} = 0 \end{cases} \Leftrightarrow \begin{cases} 5(x - 1) = 0 \\ 3(x + 1) - 2(y - 1) = 0 \end{cases} \Rightarrow \begin{cases} x = 1 \\ y = 4 \end{cases} \Rightarrow x_H + y_H = 5$.
    \item \textbf{Câu 48:} Gọi $I(x; y)$ là tâm ngoại tiếp tam giác $ABC$. Thử lại với $I(1; 2)$: $IA^2 = 0^2 + 5^2 = 25$, $IB^2 = 4^2 + 3^2 = 25$, $IC^2 = (-3)^2 + (-4)^2 = 25$. Vậy $I(1; 2)$ chính xác là tâm ngoại tiếp. Biểu thức $P = x_I + 2y_I = 1 + 2(2) = 5$.
    \item \textbf{Câu 49:} Gắn hệ toạ độ với gốc tại $D(0; 0) \Rightarrow C(6; 0), A(0; 4), B(3; 4)$. Khi đó $\vec{AC} = (6; -4)$, $\vec{BD} = (-3; -4)$. Tích vô hướng $\vec{AC} \cdot \vec{BD} = 6(-3) + (-4)(-4) = -18 + 16 = -2$.
    \item \textbf{Câu 50:} Gọi $I$ là điểm thỏa mãn $\vec{IA} + 2\vec{IB} = \vec{0} \Rightarrow I\left(\frac{1+2 \cdot 4}{3}; \frac{3+2 \cdot 2}{3}\right) = \left(3; \frac{7}{3}\right)$. Khi đó $|\vec{MA} + 2\vec{MB}| = |3\vec{MI}| = 3 MI$. Khoảng cách $MI$ ngắn nhất khi $M$ là hình chiếu vuông góc của $I$ lên trục hoành $Ox \Rightarrow x_0 = x_I = 3$.
\end{itemize}

\end{document}
"""
    return tex

if __name__ == "__main__":
    tex_path = os.path.join(OUT_DIR, "De_Cuong_Vector.tex")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(generate_tex(4, 4))
    print("Created TeX file:", tex_path)
    
    cmd = ["pdflatex", "-interaction=nonstopmode", "De_Cuong_Vector.tex"]
    for run in range(2):
        proc = subprocess.run(cmd, cwd=OUT_DIR, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Run {run+1} finished with exit code {proc.returncode}")
        
    pdf_full = os.path.join(OUT_DIR, "De_Cuong_Vector.pdf")
    doc = pymupdf.open(pdf_full)
    total_pages = len(doc)
    print(f"Total pages generated: {total_pages}")
    
    exam_pdf = os.path.join(OUT_DIR, "De_Cuong.pdf")
    ans_pdf = os.path.join(OUT_DIR, "De_Cuong_Ans.pdf")
    
    # Trang 1-4 là Đề (4 trang)
    doc_exam = pymupdf.open()
    doc_exam.insert_pdf(doc, from_page=0, to_page=3)
    doc_exam.save(exam_pdf, garbage=4, deflate=True)
    doc_exam.close()
    
    # Trang 5-8 là Đáp án (4 trang)
    doc_ans = pymupdf.open()
    doc_ans.insert_pdf(doc, from_page=4, to_page=total_pages - 1)
    doc_ans.save(ans_pdf, garbage=4, deflate=True)
    doc_ans.close()
    
    print(f"Split PDF successfully:")
    print(f" - Exam: {exam_pdf} (Pages: {len(pymupdf.open(exam_pdf))})")
    print(f" - Ans: {ans_pdf} (Pages: {len(pymupdf.open(ans_pdf))})")
    
    os.makedirs(os.path.join(EXPORT_DIR, "Ans"), exist_ok=True)
    dest_exam = os.path.join(EXPORT_DIR, "De_Cuong_Vector.pdf")
    dest_ans = os.path.join(EXPORT_DIR, "Ans", "De_Cuong_Vector.pdf")
    shutil.copy2(exam_pdf, dest_exam)
    shutil.copy2(ans_pdf, dest_ans)
    
    shutil.copy2(exam_pdf, r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\De_Cuong_Vector.pdf")
    os.makedirs(r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\Ans", exist_ok=True)
    shutil.copy2(ans_pdf, r"D:\Document\Dạy học\Dạy lớp 10\Ôn tập\Ans\De_Cuong_Vector.pdf")
    
    print("Exported successfully to all target directories!")
