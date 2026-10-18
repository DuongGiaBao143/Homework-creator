from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.edgecolor'] = '#1A365D'
plt.rcParams['axes.linewidth'] = 1.0

NAVY = '#1A365D'
TEAL = '#0D9488'
TEAL_LIGHT = '#99F6E4'
ORANGE = '#EA580C'
ORANGE_LIGHT = '#FED7AA'
GRAY = '#64748B'
GRAY_LIGHT = '#E2E8F0'

# 1. Đề 6 - Phần II - Câu 4: Quỹ đạo 2 Drone trong Oxyz (Chỉ vẽ giả thiết A0, B0 và hướng bay, không lộ đáp số)
def plot_de6_p2_c4():
    fig = plt.figure(figsize=(5.4, 3.6), dpi=300)
    ax = fig.add_subplot(111, projection='3d')
    
    t = np.linspace(0, 2.0, 100)
    xA, yA, zA = 1 + 2*t, 2 + t, 5 - t
    xB, yB, zB = 10 - t, -5 + 4*t, 2 + 2*t
    
    ax.plot(xA, yA, zA, color=TEAL, lw=2.3, label=r'Quỹ đạo Drone $A$')
    ax.plot(xB, yB, zB, color=ORANGE, lw=2.3, label=r'Quỹ đạo Drone $B$')
    
    ax.scatter([1], [2], [5], color=TEAL, s=40)
    ax.text(0.4, 2.2, 5.3, r'$A_0(1;2;5)$', fontsize=8.5, color=NAVY, fontweight='bold')
    ax.scatter([10], [-5], [2], color=ORANGE, s=40)
    ax.text(9.2, -5.5, 1.1, r'$B_0(10;-5;2)$', fontsize=8.5, color=NAVY, fontweight='bold')
    
    # Generic distance segment at some t
    t0 = 1.1
    At = (1 + 2*t0, 2 + t0, 5 - t0)
    Bt = (10 - t0, -5 + 4*t0, 2 + 2*t0)
    ax.scatter([At[0], Bt[0]], [At[1], Bt[1]], [At[2], Bt[2]], color=NAVY, s=25)
    ax.plot([At[0], Bt[0]], [At[1], Bt[1]], [At[2], Bt[2]], color='#DC2626', lw=1.5, ls='--', label=r'Khoảng cách $d(t)$')
    
    ax.set_xlabel('$x$ (m)', fontsize=8.5, labelpad=-2)
    ax.set_ylabel('$y$ (m)', fontsize=8.5, labelpad=-2)
    ax.set_zlabel('$z$ (m)', fontsize=8.5, labelpad=-2)
    ax.tick_params(labelsize=7)
    ax.view_init(elev=22, azim=-55)
    ax.legend(loc='upper left', fontsize=8)
    plt.tight_layout()
    plt.savefig(r'd:\Tao_De\Lớp 12\Output\De 6\images\phan2_cau4_haidrone_3d.png', dpi=300, bbox_inches='tight')
    plt.close()

# 2. Đề 6 - Phần III - Câu 1: Bể chứa hình hộp chữ nhật không nắp (rộng x, dài 2x, cao h)
def plot_de6_p3_c1():
    fig = plt.figure(figsize=(5.0, 3.3), dpi=300)
    ax = fig.add_subplot(111, projection='3d')
    
    L, W, H = 8, 4, 4.2
    v = np.array([
        [0, 0, 0], [L, 0, 0], [L, W, 0], [0, W, 0],
        [0, 0, H], [L, 0, H], [L, W, H], [0, W, H]
    ])
    base = [[v[0], v[1], v[2], v[3]]]
    sides = [
        [v[0], v[1], v[5], v[4]],
        [v[1], v[2], v[6], v[5]],
        [v[2], v[3], v[7], v[6]],
        [v[3], v[0], v[4], v[7]]
    ]
    ax.add_collection3d(Poly3DCollection(base, facecolors=ORANGE_LIGHT, edgecolors=NAVY, linewidths=1.5, alpha=0.75))
    ax.add_collection3d(Poly3DCollection(sides, facecolors=TEAL_LIGHT, edgecolors=NAVY, linewidths=1.3, alpha=0.4))
    
    ax.text(L/2, -0.9, 0, r'Chiều dài $2x$', fontsize=9.5, color=NAVY, fontweight='bold', ha='center')
    ax.text(L+0.6, W/2, 0, r'Rộng $x$', fontsize=9.5, color=NAVY, fontweight='bold', va='center')
    ax.text(L+0.4, W+0.3, H/2, r'Cao $h$', fontsize=9.5, color=ORANGE, fontweight='bold')
    ax.text(L/2, W/2, H/2, r'$V = 128\mathrm{\ m}^3$', fontsize=9.5, color=NAVY, fontweight='bold', ha='center')
    
    ax.set_xlim(-1, 9.5)
    ax.set_ylim(-1, 5.5)
    ax.set_zlim(0, 5)
    ax.set_box_aspect([2, 1.1, 1])
    ax.axis('off')
    ax.view_init(elev=24, azim=-52)
    plt.tight_layout()
    plt.savefig(r'd:\Tao_De\Lớp 12\Output\De 6\images\phan3_cau1_bechua_3d.png', dpi=300, bbox_inches='tight')
    plt.close()

# 3. Đề 6 - Phần III - Câu 2: Hình chóp S.ABCD đáy hình vuông cạnh 6, SA vuông góc đáy
def plot_de6_p3_c2():
    fig, ax = plt.subplots(figsize=(4.6, 3.4), dpi=300)
    A = np.array([0.0, 0.0])
    D = np.array([3.2, 0.0])
    B = np.array([-1.3, -1.2])
    C = B + D - A
    S = np.array([0.0, 3.1])
    
    for p1, p2 in [(A, B), (A, D), (S, A), (B, D)]:
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=NAVY, lw=1.4, ls='--')
    for p1, p2 in [(S, B), (S, C), (S, D), (B, C), (C, D)]:
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=NAVY, lw=1.8)
        
    ax.plot([S[0], C[0]], [S[1], C[1]], color=TEAL, lw=2.2)
    ax.plot([B[0], D[0]], [B[1], D[1]], color=ORANGE, lw=2.0, ls='--')
    
    ra_size = 0.25
    ax.plot([0, ra_size, ra_size], [ra_size, ra_size, 0], color=NAVY, lw=1.0)
    
    pts = {'A': (A, (-0.32, 0.12)), 'B': (B, (-0.35, -0.2)), 'C': (C, (0.15, -0.25)),
           'D': (D, (0.15, 0.05)), 'S': (S, (-0.1, 0.18))}
    for name, (pt, offset) in pts.items():
        ax.plot(pt[0], pt[1], 'o', color=NAVY, markersize=4.5)
        ax.text(pt[0]+offset[0], pt[1]+offset[1], f'${name}$', fontsize=10.5, color=NAVY, fontweight='bold')
        
    ax.text(-0.4, 1.55, r'$h$', fontsize=10, color=TEAL, fontweight='bold')
    ax.text(0.35, -1.45, r'$a = 6$', fontsize=9.5, color=NAVY)
    
    ax.set_aspect('equal')
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(r'd:\Tao_De\Lớp 12\Output\De 6\images\phan3_cau2_hinhchop.png', dpi=300, bbox_inches='tight')
    plt.close()

# 4. Đề 6 - Phần III - Câu 3: Hai robot trên trục Ox, Oy
def plot_de6_p3_c3():
    fig, ax = plt.subplots(figsize=(5.0, 3.3), dpi=300)
    ax.grid(True, linestyle=':', color=GRAY_LIGHT)
    
    ax.annotate('', xy=(6.8, 0), xytext=(-0.8, 0), arrowprops=dict(arrowstyle='->', color=NAVY, lw=1.6))
    ax.annotate('', xy=(0, 4.3), xytext=(0, -0.6), arrowprops=dict(arrowstyle='->', color=NAVY, lw=1.6))
    ax.text(6.5, -0.42, r'$x\mathrm{\ (m)}$', fontsize=9.5, color=NAVY, fontweight='bold')
    ax.text(-0.55, 4.0, r'$y\mathrm{\ (m)}$', fontsize=9.5, color=NAVY, fontweight='bold')
    ax.text(-0.35, -0.35, r'$O$', fontsize=9.5, color=NAVY, fontweight='bold')
    
    xA, yB = 4.2, 2.1
    ax.plot(6, 0, 'o', color=GRAY, markersize=4.5)
    ax.text(5.6, 0.22, r'$x(0)=6$', fontsize=8, color=GRAY)
    
    rectA = patches.FancyBboxPatch((xA-0.35, -0.22), 0.7, 0.44, boxstyle='round,pad=0.05', facecolor=TEAL, edgecolor=NAVY, lw=1.4, zorder=4)
    ax.add_patch(rectA)
    ax.annotate('', xy=(xA-1.2, 0), xytext=(xA-0.4, 0), arrowprops=dict(arrowstyle='->', color=TEAL, lw=2))
    ax.text(xA-0.6, -0.58, r'$A(6-2t;\; 0)$', fontsize=9, color=NAVY, fontweight='bold')
    
    rectB = patches.FancyBboxPatch((-0.25, yB-0.3), 0.5, 0.6, boxstyle='round,pad=0.05', facecolor=ORANGE, edgecolor=NAVY, lw=1.4, zorder=4)
    ax.add_patch(rectB)
    ax.annotate('', xy=(0, yB+1.1), xytext=(0, yB+0.35), arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2))
    ax.text(0.4, yB-0.1, r'$B(0;\; 2e^t-2)$', fontsize=9, color=NAVY, fontweight='bold')
    
    ax.plot([xA, 0], [0, yB], color='#DC2626', lw=1.8, ls='--', zorder=3)
    ax.text(xA/2 + 0.15, yB/2 + 0.15, r'$d(t)$', fontsize=9.5, color='#DC2626', fontweight='bold')
    
    ax.set_xlim(-1.0, 7.1)
    ax.set_ylim(-0.8, 4.5)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(r'd:\Tao_De\Lớp 12\Output\De 6\images\phan3_cau3_hairobot_oxy.png', dpi=300, bbox_inches='tight')
    plt.close()

# 5. Đề 6 - Phần III - Câu 4: Nguồn sáng S(0,0,12) chiếu bóng đĩa tròn xuống mặt đất Oxy
def plot_de6_p3_c4():
    fig = plt.figure(figsize=(5.0, 3.6), dpi=300)
    ax = fig.add_subplot(111, projection='3d')
    
    theta = np.linspace(0, 2*np.pi, 100)
    x_disk, y_disk = 2 * np.cos(theta), 2 * np.sin(theta)
    z_disk = np.full_like(theta, 6.0)
    
    x_sh, y_sh = 4 * np.cos(theta), 4 * np.sin(theta)
    z_sh = np.zeros_like(theta)
    
    verts_disk = [list(zip(x_disk, y_disk, z_disk))]
    verts_sh = [list(zip(x_sh, y_sh, z_sh))]
    ax.add_collection3d(Poly3DCollection(verts_disk, facecolors=TEAL, edgecolors=NAVY, linewidths=1.5, alpha=0.65))
    ax.add_collection3d(Poly3DCollection(verts_sh, facecolors=ORANGE_LIGHT, edgecolors=ORANGE, linewidths=1.5, alpha=0.55))
    
    for ang in np.linspace(0, 2*np.pi, 8, endpoint=False):
        ax.plot([0, 4*np.cos(ang)], [0, 4*np.sin(ang)], [12, 0], color=GRAY, lw=0.9, ls='--')
        
    ax.plot([0, 0], [0, 0], [0, 13], color=NAVY, lw=1.6)
    ax.scatter([0, 0, 0], [0, 0, 0], [12, 6, 0], color=NAVY, s=35, zorder=5)
    
    ax.text(0.3, 0.3, 12.2, r'$S(0;0;12)$', fontsize=9, color=NAVY, fontweight='bold')
    ax.text(2.1, 0, 6.2, r'$C(0;0;z(t)),\; R=2$', fontsize=8.5, color=TEAL, fontweight='bold')
    ax.text(2.2, -2.5, 0.3, r'Bóng $S(t)$ trên $(Oxy)$', fontsize=8.5, color=ORANGE, fontweight='bold')
    
    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-4.5, 4.5)
    ax.set_zlim(0, 13)
    ax.view_init(elev=20, azim=-45)
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(r'd:\Tao_De\Lớp 12\Output\De 6\images\phan3_cau4_nonanhsang.png', dpi=300, bbox_inches='tight')
    plt.close()

# 6. Đề 6 - Phần III - Câu 6: Thiết diện tam giác vuông từ x=0 đến x=2
def plot_de6_p3_c6():
    fig = plt.figure(figsize=(5.4, 3.5), dpi=300)
    ax = fig.add_subplot(111, projection='3d')
    
    x_vals = np.linspace(0, 2, 100)
    b_vals = x_vals * np.exp(x_vals) - x_vals**2
    h_vals = 2 * np.exp(-x_vals)
    
    ax.plot(x_vals, np.zeros_like(x_vals), np.zeros_like(x_vals), color=NAVY, lw=2)
    ax.plot(x_vals, b_vals, np.zeros_like(x_vals), color=TEAL, lw=2, label=r'$b(x) = xe^x - x^2$')
    ax.plot(x_vals, np.zeros_like(x_vals), h_vals, color=ORANGE, lw=2, label=r'$h(x) = 2e^{-x}$')
    ax.plot(x_vals, b_vals, h_vals, color=GRAY, lw=1.2, ls='--')
    
    for xv in [0.4, 0.8, 1.2, 1.6, 2.0]:
        bv = xv * np.exp(xv) - xv**2
        hv = 2 * np.exp(-xv)
        tri = [[[xv, 0, 0], [xv, bv, 0], [xv, 0, hv]]]
        col = TEAL_LIGHT if xv < 1.5 else ORANGE_LIGHT
        ax.add_collection3d(Poly3DCollection(tri, facecolors=col, edgecolors=NAVY, linewidths=1.2, alpha=0.55))
        
    ax.set_xlabel(r'$x$', fontsize=9, labelpad=-2)
    ax.set_ylabel(r'$b(x)$', fontsize=9, labelpad=-2)
    ax.set_zlabel(r'$h(x)$', fontsize=9, labelpad=-2)
    ax.tick_params(labelsize=7)
    ax.view_init(elev=24, azim=-58)
    ax.legend(loc='upper left', fontsize=8)
    plt.tight_layout()
    plt.savefig(r'd:\Tao_De\Lớp 12\Output\De 6\images\phan3_cau6_thietdien_3d.png', dpi=300, bbox_inches='tight')
    plt.close()

# 7. Đề 4 - Phần II - Câu 4: Mái che sân tennis hình chóp S.ABCD trong Oxyz (Không lộ tọa độ H)
def plot_de4_p2_c4():
    fig = plt.figure(figsize=(5.2, 3.5), dpi=300)
    ax = fig.add_subplot(111, projection='3d')
    
    A, B, C, D = np.array([0, 0, 0]), np.array([8, 0, 0]), np.array([8, 10, 0]), np.array([0, 10, 0])
    S, H = np.array([4, 5, 8]), np.array([4, 5, 0])
    
    base = [[A, B, C, D]]
    ax.add_collection3d(Poly3DCollection(base, facecolors=TEAL_LIGHT, edgecolors=NAVY, linewidths=1.3, alpha=0.35))
    
    faces = [[S, A, B], [S, B, C], [S, C, D], [S, D, A]]
    ax.add_collection3d(Poly3DCollection(faces, facecolors=ORANGE_LIGHT, edgecolors=NAVY, linewidths=1.4, alpha=0.3))
    
    ax.plot([S[0], H[0]], [S[1], H[1]], [S[2], H[2]], color='#DC2626', lw=1.6, ls='--')
    ax.scatter([S[0], H[0]], [S[1], H[1]], [S[2], H[2]], color='#DC2626', s=28)
    
    ax.text(4, 5, 8.5, r'$S(4;5;8)$', fontsize=8.5, color=NAVY, fontweight='bold')
    ax.text(4.3, 5, 0.4, r'$H$', fontsize=8.5, color='#DC2626', fontweight='bold')
    ax.text(0, -1, 0, r'$A(0;0;0)$', fontsize=7.5, color=NAVY)
    ax.text(8.2, 0, 0, r'$B(8;0;0)$', fontsize=7.5, color=NAVY)
    ax.text(8.2, 10, 0, r'$C(8;10;0)$', fontsize=7.5, color=NAVY)
    ax.text(-1.5, 10, 0, r'$D(0;10;0)$', fontsize=7.5, color=NAVY)
    
    ax.set_xlim(-1, 9.5)
    ax.set_ylim(-1, 11.5)
    ax.set_zlim(0, 9.5)
    ax.set_xlabel('$x$', fontsize=8, labelpad=-2)
    ax.set_ylabel('$y$', fontsize=8, labelpad=-2)
    ax.set_zlabel('$z$', fontsize=8, labelpad=-2)
    ax.tick_params(labelsize=7)
    ax.view_init(elev=22, azim=-50)
    plt.tight_layout()
    plt.savefig(r'd:\Tao_De\Lớp 12\Output\De 4\images\phan2_cau4_maiche_oxyz.png', dpi=300, bbox_inches='tight')
    plt.close()

# 8. Đề 4 - Phần III - Câu 1: Thùng đựng rác không nắp đáy vuông cạnh x, cao h
def plot_de4_p3_c1():
    fig = plt.figure(figsize=(4.6, 3.2), dpi=300)
    ax = fig.add_subplot(111, projection='3d')
    
    W, H = 4, 4.5
    v = np.array([
        [0, 0, 0], [W, 0, 0], [W, W, 0], [0, W, 0],
        [0, 0, H], [W, 0, H], [W, W, H], [0, W, H]
    ])
    base = [[v[0], v[1], v[2], v[3]]]
    sides = [
        [v[0], v[1], v[5], v[4]],
        [v[1], v[2], v[6], v[5]],
        [v[2], v[3], v[7], v[6]],
        [v[3], v[0], v[4], v[7]]
    ]
    ax.add_collection3d(Poly3DCollection(base, facecolors=ORANGE_LIGHT, edgecolors=NAVY, linewidths=1.5, alpha=0.8))
    ax.add_collection3d(Poly3DCollection(sides, facecolors=TEAL_LIGHT, edgecolors=NAVY, linewidths=1.3, alpha=0.4))
    
    ax.text(W/2, -0.7, 0, r'Cạnh đáy $x$', fontsize=9, color=NAVY, fontweight='bold', ha='center')
    ax.text(W+0.4, W/2, 0, r'$x$', fontsize=9.5, color=NAVY, fontweight='bold')
    ax.text(W+0.3, W+0.3, H/2, r'$h$', fontsize=9.5, color=ORANGE, fontweight='bold')
    ax.text(W/2, W/2, H/2, r'$V = 0,162\mathrm{\ m}^3$', fontsize=8.5, color=NAVY, fontweight='bold', ha='center')
    
    ax.set_xlim(-1, 5.5)
    ax.set_ylim(-1, 5.5)
    ax.set_zlim(0, 5.2)
    ax.set_box_aspect([1, 1, 1.1])
    ax.axis('off')
    ax.view_init(elev=23, azim=-48)
    plt.tight_layout()
    plt.savefig(r'd:\Tao_De\Lớp 12\Output\De 4\images\phan3_cau1_thungrac_3d.png', dpi=300, bbox_inches='tight')
    plt.close()

# 9. Đề 5 - Phần II - Câu 4: Mái vòm nhà thi đấu hình chóp S.ABCD trong Oxyz (Không lộ tọa độ H)
def plot_de5_p2_c4():
    fig = plt.figure(figsize=(5.2, 3.5), dpi=300)
    ax = fig.add_subplot(111, projection='3d')
    
    A, B, C, D = np.array([0, 0, 0]), np.array([4, 0, 0]), np.array([4, 6, 0]), np.array([0, 6, 0])
    S, H = np.array([2, 3, 5]), np.array([2, 3, 0])
    
    base = [[A, B, C, D]]
    ax.add_collection3d(Poly3DCollection(base, facecolors=TEAL_LIGHT, edgecolors=NAVY, linewidths=1.3, alpha=0.35))
    
    faces = [[S, A, B], [S, B, C], [S, C, D], [S, D, A]]
    ax.add_collection3d(Poly3DCollection(faces, facecolors=ORANGE_LIGHT, edgecolors=NAVY, linewidths=1.4, alpha=0.3))
    
    ax.plot([S[0], H[0]], [S[1], H[1]], [S[2], H[2]], color='#DC2626', lw=1.6, ls='--')
    ax.scatter([S[0], H[0]], [S[1], H[1]], [S[2], H[2]], color='#DC2626', s=28)
    
    ax.text(2, 3, 5.4, r'$S(2;3;5)$', fontsize=8.5, color=NAVY, fontweight='bold')
    ax.text(2.2, 3, 0.3, r'$H$', fontsize=8.5, color='#DC2626', fontweight='bold')
    ax.text(0, -0.6, 0, r'$A(0;0;0)$', fontsize=7.5, color=NAVY)
    ax.text(4.2, 0, 0, r'$B(4;0;0)$', fontsize=7.5, color=NAVY)
    ax.text(4.2, 6, 0, r'$C(4;6;0)$', fontsize=7.5, color=NAVY)
    ax.text(-0.8, 6, 0, r'$D(0;6;0)$', fontsize=7.5, color=NAVY)
    
    ax.set_xlim(-0.8, 5.0)
    ax.set_ylim(-0.8, 7.0)
    ax.set_zlim(0, 6.0)
    ax.set_xlabel('$x$', fontsize=8, labelpad=-2)
    ax.set_ylabel('$y$', fontsize=8, labelpad=-2)
    ax.set_zlabel('$z$', fontsize=8, labelpad=-2)
    ax.tick_params(labelsize=7)
    ax.view_init(elev=22, azim=-50)
    plt.tight_layout()
    plt.savefig(r'd:\Tao_De\Lớp 12\Output\De 5\images\phan2_cau4_maivom_oxyz.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    plot_de6_p2_c4()
    plot_de6_p3_c1()
    plot_de6_p3_c2()
    plot_de6_p3_c3()
    plot_de6_p3_c4()
    plot_de6_p3_c6()
    plot_de4_p2_c4()
    plot_de4_p3_c1()
    plot_de5_p2_c4()
    print("Refined plots generated without leaking any answers!")
