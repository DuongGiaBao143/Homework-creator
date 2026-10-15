"""
Script vẽ 6 hình minh họa toán học chính xác (2D/3D) cho Đề 7 bằng matplotlib + PIL tight crop.
Tuyệt đối không lộ đáp án trên hình, chỉ hiển thị đúng dữ kiện đề bài cho.
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from PIL import Image, ImageChops

OUT_DIR = r"d:\Tao_De\Output\De 7\images"
os.makedirs(OUT_DIR, exist_ok=True)

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["mathtext.fontset"] = "cm"

NAVY = "#1B365D"
TEAL = "#008080"
ORANGE = "#E06A3B"
GRAY = "#6C757D"
LIGHT_TEAL = "#B2DFDB"
LIGHT_ORANGE = "#FFE0B2"


def save_tight(fig, path, pad=12):
    fig.savefig(path, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    im = Image.open(path).convert("RGB")
    bg = Image.new("RGB", im.size, (255, 255, 255))
    diff = ImageChops.difference(im, bg)
    bbox = diff.getbbox()
    if bbox:
        l, u, r, b = bbox
        l = max(0, l - pad)
        u = max(0, u - pad)
        r = min(im.width, r + pad)
        b = min(im.height, b + pad)
        im.crop((l, u, r, b)).save(path)


# 1. PHẦN II CÂU 4: Khinh khí cầu M(z=5) & 3 vệ tinh A, B, C trong Oxyz
def plot_p2_c4():
    fig = plt.figure(figsize=(5.5, 4.6))
    ax = fig.add_subplot(111, projection="3d")

    A = np.array([1, 1, 5])
    B = np.array([4, 11, 13])
    C = np.array([16, 5, 10])
    M = np.array([4, 5, 5])  # vẽ vị trí minh họa trên mặt phẳng độ cao z=5, không ghi lộ tọa độ (4;5;5)

    # Mặt phẳng độ cao z = 5
    xx, yy = np.meshgrid(np.linspace(0, 17, 10), np.linspace(0, 13, 10))
    zz = np.full_like(xx, 5.0)
    ax.plot_surface(xx, yy, zz, color=LIGHT_TEAL, alpha=0.25)

    for P, name, dist_lbl, offset in [
        (A, "A(1; 1; 5)", "5 km", (-1.5, -1.8, 0.8)),
        (B, "B(4; 11; 13)", "10 km", (-2.0, 0.5, 0.7)),
        (C, "C(16; 5; 10)", "13 km", (-3.5, 0.6, 0.8)),
    ]:
        ax.scatter(*P, color=NAVY, s=45, zorder=5)
        ax.text(P[0]+offset[0], P[1]+offset[1], P[2]+offset[2], name, fontsize=9, fontweight="bold", color=NAVY)
        ax.plot([M[0], P[0]], [M[1], P[1]], [M[2], P[2]], "--", color=ORANGE, lw=1.6)

    ax.scatter(*M, color=ORANGE, s=75, marker="^", zorder=6, label="Khinh khí cầu M (z = 5)")
    ax.text(M[0]+0.6, M[1]-1.2, M[2]-1.1, "M(x; y; 5)", fontsize=9.5, fontweight="bold", color=ORANGE)

    ax.set_xlabel("x (km)", fontsize=8.5, labelpad=2)
    ax.set_ylabel("y (km)", fontsize=8.5, labelpad=2)
    ax.set_zlabel("z (km)", fontsize=8.5, labelpad=2)
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 13)
    ax.set_zlim(0, 15)
    ax.view_init(elev=22, azim=-52)
    ax.legend(loc="upper left", fontsize=8)
    save_tight(fig, os.path.join(OUT_DIR, "phan2_cau4_khinhkhicau_oxyz.png"))


# 2. PHẦN III CÂU 1: Cây sào ngăn góc hồ đi qua cọc K(1m, 8m)
def plot_p3_c1():
    fig, ax = plt.subplots(figsize=(5.0, 4.2))
    # Bờ AC nằm ngang (trục x), bờ AB thẳng đứng (trục y)
    ax.fill_between([0, 14], 0, 11, color="#E0F7FA", alpha=0.45, label="Mặt hồ")
    ax.plot([0, 14], [0, 0], color=NAVY, lw=2.5)
    ax.plot([0, 0], [0, 11], color=NAVY, lw=2.5)

    # Cọc K cách AB 1m (x_K?), cách bờ AB (trục tung? Không, theo đề: H là hình chiếu của K xuống AC, HQ = x, AQ = x+1 => AH = 1, KH = 8 => K cách AB là 1m, cách AC là 8m nếu vẽ AC thẳng đứng, AB nằm ngang; hoặc vẽ rõ khoảng cách 1m và 8m)
    # Để trực quan nhất: bờ AC nằm ngang, bờ AB thẳng đứng -> AH = 8m? Không: nếu AQ = x+1 với HQ = x thì AH = 1m (tức khoảng cách từ K đến bờ AB là 1m), KH = 8m (khoảng cách từ K đến bờ AC là 8m).
    # Vẽ tỉ lệ đẹp để dễ nhìn:
    x_K, y_K = 2.0, 5.0
    x_Q = 7.0
    y_P = y_K * x_Q / (x_Q - x_K)

    # Vùng thả bèo tam giác APQ
    ax.fill([0, x_Q, 0], [0, 0, y_P], color=LIGHT_TEAL, alpha=0.65)
    # Cây sào PQ
    ax.plot([x_Q, 0], [0, y_P], color=ORANGE, lw=2.8, label="Cây sào PQ")

    # Cọc K và hình chiếu
    ax.plot([x_K, x_K], [0, y_K], "--", color=GRAY, lw=1.3)
    ax.plot([0, x_K], [y_K, y_K], "--", color=GRAY, lw=1.3)
    ax.scatter([x_K], [y_K], color=NAVY, s=55, zorder=5)

    ax.text(-0.6, -0.6, "A", fontsize=11, fontweight="bold", color=NAVY)
    ax.text(x_Q, -0.7, "Q", fontsize=11, fontweight="bold", color=NAVY)
    ax.text(-0.7, y_P, "P", fontsize=11, fontweight="bold", color=NAVY)
    ax.text(x_K-0.2, -0.7, "H", fontsize=10.5, fontweight="bold", color=NAVY)
    ax.text(x_K+0.25, y_K+0.25, "Cọc K", fontsize=10, fontweight="bold", color=NAVY)

    ax.text(x_K/2 - 0.3, y_K + 0.3, "1 m", fontsize=9.5, color=NAVY, fontweight="bold")
    ax.text(x_K + 0.25, y_K/2, "8 m", fontsize=9.5, color=NAVY, fontweight="bold")
    ax.text(10.2, -0.8, "Bờ AC", fontsize=10, fontweight="bold", color=NAVY)
    ax.text(-2.3, 9.2, "Bờ AB", fontsize=10, fontweight="bold", color=NAVY)
    ax.text(1.1, 1.8, "Khu thả bèo", fontsize=9.5, color=TEAL, fontweight="bold")

    ax.set_xlim(-2.6, 13.0)
    ax.set_ylim(-1.2, 10.5)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.legend(loc="upper right", fontsize=9)
    save_tight(fig, os.path.join(OUT_DIR, "phan3_cau1_caysao_ho.png"))


# 3. PHẦN III CÂU 2: Giá đỡ chậu cây 4 chân S(0;0;40) và A,B,C,D trên Oxy
def plot_p3_c2():
    fig = plt.figure(figsize=(4.8, 4.1))
    ax = fig.add_subplot(111, projection="3d")

    S = np.array([0, 0, 40])
    pts = {
        "A(30;0;0)": np.array([30, 0, 0]),
        "B(0;30;0)": np.array([0, 30, 0]),
        "C(-30;0;0)": np.array([-30, 0, 0]),
        "D(0;-30;0)": np.array([0, -30, 0]),
    }

    # Mặt đất Oxy
    base_poly = [pts["A(30;0;0)"], pts["B(0;30;0)"], pts["C(-30;0;0)"], pts["D(0;-30;0)"]]
    ax.add_collection3d(Poly3DCollection([base_poly], facecolors=LIGHT_TEAL, edgecolors=GRAY, linewidths=1.0, alpha=0.25))

    # Trục Oz
    ax.plot([0, 0], [0, 0], [0, 48], "--", color=GRAY, lw=1.2)
    ax.scatter(0, 0, 0, color=GRAY, s=25)
    ax.text(2, 2, 1, "O", fontsize=9, color=GRAY, fontweight="bold")

    for lbl, P in pts.items():
        ax.plot([S[0], P[0]], [S[1], P[1]], [S[2], P[2]], color=NAVY, lw=2.2)
        ax.scatter(*P, color=NAVY, s=40)
        vec = (P - S) * 0.35
        ax.quiver(S[0], S[1], S[2], vec[0], vec[1], vec[2], color=TEAL, lw=1.8, arrow_length_ratio=0.22)

    ax.text(24, -14, 0, "A(30;0;0)", fontsize=8, fontweight="bold", color=NAVY)
    ax.text(-6, 32, 0, "B(0;30;0)", fontsize=8, fontweight="bold", color=NAVY)
    ax.text(-42, -6, 0, "C(-30;0;0)", fontsize=8, fontweight="bold", color=NAVY)
    ax.text(-8, -39, 0, "D(0;-30;0)", fontsize=8, fontweight="bold", color=NAVY)

    # Điểm đặt S và trọng lực P = 80N
    ax.scatter(*S, color=ORANGE, s=65, zorder=6)
    ax.quiver(0, 0, 40, 0, 0, -18, color=ORANGE, lw=2.4, arrow_length_ratio=0.22)
    ax.text(2, 2, 42.5, "S(0; 0; 40)", fontsize=9, fontweight="bold", color=NAVY)
    ax.text(3, 4, 21, r"$\vec{P}\ (80\ \mathrm{N})$", fontsize=8.5, fontweight="bold", color=ORANGE)

    ax.set_xlim(-38, 38)
    ax.set_ylim(-38, 38)
    ax.set_zlim(0, 48)
    ax.set_xlabel("x (cm)", fontsize=8)
    ax.set_ylabel("y (cm)", fontsize=8)
    ax.set_zlabel("z (cm)", fontsize=8)
    ax.view_init(elev=22, azim=-40)
    save_tight(fig, os.path.join(OUT_DIR, "phan3_cau2_giado_chaucay.png"))


# 4. PHẦN III CÂU 3: Khu đất hình Elip (2a=10m, 2b=8m) nội tiếp bể cá hình chữ nhật
def plot_p3_c3():
    fig, ax = plt.subplots(figsize=(5.0, 3.8))
    a, b = 5.0, 4.0
    theta = np.linspace(0, 2*np.pi, 400)
    xe, ye = a * np.cos(theta), b * np.sin(theta)

    ax.fill(xe, ye, color=LIGHT_ORANGE, alpha=0.55, label="Trồng hoa")
    ax.plot(xe, ye, color=NAVY, lw=2.2)

    xr = a * np.cos(np.pi/4)
    yr = b * np.sin(np.pi/4)
    rect_x = [-xr, xr, xr, -xr, -xr]
    rect_y = [-yr, -yr, yr, yr, -yr]
    ax.fill(rect_x, rect_y, color=LIGHT_TEAL, alpha=0.8, label="Bể cá HCN")
    ax.plot(rect_x, rect_y, color=TEAL, lw=2.0)

    # Trục tọa độ Oxy mũi tên chuẩn SGK (không khung viền, không grid)
    ax.annotate("", xy=(6.2, 0), xytext=(-6.0, 0),
                arrowprops=dict(arrowstyle="-|>,head_width=0.25,head_length=0.45", lw=1.3, color="black"))
    ax.annotate("", xy=(0, 5.1), xytext=(0, -4.9),
                arrowprops=dict(arrowstyle="-|>,head_width=0.25,head_length=0.45", lw=1.3, color="black"))
    ax.text(6.25, -0.4, r"$x$", fontsize=11, color="black")
    ax.text(0.2, 5.0, r"$y$", fontsize=11, color="black")
    ax.text(-0.45, -0.45, r"$O$", fontsize=10, color="black")

    ax.text(5.15, -0.45, "5", fontsize=9.5, fontweight="bold", color=NAVY)
    ax.text(-5.65, -0.45, "-5", fontsize=9.5, fontweight="bold", color=NAVY)
    ax.text(0.2, 4.15, "4", fontsize=9.5, fontweight="bold", color=NAVY)
    ax.text(0.2, -4.50, "-4", fontsize=9.5, fontweight="bold", color=NAVY)
    ax.text(0, 0.35, "Bể cá cảnh", fontsize=9.5, fontweight="bold", color=TEAL, ha="center",
            bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.85))

    ax.set_xlim(-6.3, 6.6)
    ax.set_ylim(-5.1, 5.4)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.legend(loc="upper right", fontsize=8.5, framealpha=0.9)
    save_tight(fig, os.path.join(OUT_DIR, "phan3_cau3_elip_beca.png"))


# 5. PHẦN III CÂU 4: Tia laser từ A(6;3;4) tạo góc 45 độ với Ox chiếu lên tường (Oyz)
def plot_p3_c4():
    pass  # Vẽ trực tiếp bằng TikZ vector trong LaTeX


# 6. PHẦN III CÂU 6: Logo hình con cá giới hạn bởi 2 Parabol (không grid, trục mũi tên Oxy sạch sẽ)
def plot_p3_c6():
    fig, ax = plt.subplots(figsize=(5.4, 3.9))
    x = np.linspace(-4, 6, 400)
    y1 = 4 - x**2 / 4.0
    y2 = x**2 / 4.0 - 4

    ax.fill_between(x, y1, y2, where=(x <= 4), color=LIGHT_TEAL, alpha=0.75, label="Thân cá")
    ax.fill_between(x, y1, y2, where=(x >= 4), color=LIGHT_ORANGE, alpha=0.80, label="Đuôi cá")

    ax.plot(x, y1, color=NAVY, lw=2.2, label=r"$y = 4 - \frac{1}{4}x^2$")
    ax.plot(x, y2, color=ORANGE, lw=2.2, label=r"$y = \frac{1}{4}x^2 - 4$")

    # Vẽ mắt cá trang trí
    ax.scatter([-2.2], [1.1], color=NAVY, s=42, zorder=5)

    # Trục mũi tên Oxy chuẩn SGK, không kẻ lưới grid gây rối
    ax.annotate("", xy=(7.1, 0), xytext=(-5.0, 0),
                arrowprops=dict(arrowstyle="-|>,head_width=0.25,head_length=0.45", lw=1.3, color="black"))
    ax.annotate("", xy=(0, 5.6), xytext=(0, -5.6),
                arrowprops=dict(arrowstyle="-|>,head_width=0.25,head_length=0.45", lw=1.3, color="black"))
    ax.text(7.15, -0.45, r"$x$", fontsize=11, color="black")
    ax.text(0.25, 5.45, r"$y$", fontsize=11, color="black")
    ax.text(-0.5, -0.55, r"$O$", fontsize=10, color="black")

    ax.plot([6, 6], [-5, 5], "--", color=GRAY, lw=1.3)

    for xv, lbl, dy in [(-4, "-4", -0.65), (4, "4", -0.65), (6, "6", -0.65)]:
        ax.scatter([xv], [0], color=NAVY, s=26, zorder=5)
        ax.text(xv, dy, lbl, fontsize=9.5, fontweight="bold", color=NAVY, ha="center",
                bbox=dict(boxstyle="round,pad=0.1", fc="white", ec="none", alpha=0.85))
    ax.text(-0.45, 4.05, "4", fontsize=9.5, fontweight="bold", color=NAVY, ha="right",
            bbox=dict(boxstyle="round,pad=0.1", fc="white", ec="none", alpha=0.85))
    ax.text(-0.45, -4.25, "-4", fontsize=9.5, fontweight="bold", color=NAVY, ha="right",
            bbox=dict(boxstyle="round,pad=0.1", fc="white", ec="none", alpha=0.85))

    ax.set_xlim(-5.3, 7.6)
    ax.set_ylim(-5.9, 6.0)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.legend(loc="upper left", fontsize=8, framealpha=0.92)
    save_tight(fig, os.path.join(OUT_DIR, "phan3_cau6_logo_conca.png"))


if __name__ == "__main__":
    plot_p3_c3()
    plot_p3_c6()
    print("[OK] Đã tạo xong hình plot 2D sạch sẽ (không grid) cho Đề 7!")

