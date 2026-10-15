import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Ellipse
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from PIL import Image

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

NAVY = '#1B365D'
TEAL = '#008080'
ORANGE = '#E85D04'
RED = '#D62828'
GRAY = '#6C757D'

# 1. Fix De 6 P3 C3: Two robots on Ox and Oy with large bold labels
fig, ax = plt.subplots(figsize=(5.4, 4.2), dpi=300)
ax.annotate('', xy=(7.5, 0), xytext=(-0.8, 0), arrowprops=dict(arrowstyle='->', lw=2.2, color=NAVY))
ax.annotate('', xy=(0, 5.2), xytext=(0, -0.8), arrowprops=dict(arrowstyle='->', lw=2.2, color=NAVY))
ax.text(7.3, -0.55, '$x$ (m)', fontsize=12, fontweight='bold', color=NAVY)
ax.text(-0.95, 4.9, '$y$ (m)', fontsize=12, fontweight='bold', color=NAVY)
ax.text(-0.45, -0.45, '$O$', fontsize=12, fontweight='bold', color=NAVY)

ax.add_patch(Rectangle((3.5, -0.22), 0.7, 0.44, facecolor=TEAL, edgecolor=NAVY, lw=1.8, zorder=5))
ax.annotate('', xy=(2.1, 0.35), xytext=(3.8, 0.35), arrowprops=dict(arrowstyle='->', lw=2.2, color=TEAL))
ax.text(3.85, -0.68, '$A(6-2t;\\,0)$', fontsize=11.5, fontweight='bold', color=TEAL, ha='center')
ax.plot(6, 0, 'o', color=NAVY, markersize=6, zorder=5)
ax.text(6.0, 0.28, '$x(0)=6$', fontsize=10.5, fontweight='bold', color=NAVY, ha='center')

ax.add_patch(Rectangle((-0.22, 2.2), 0.44, 0.65, facecolor=ORANGE, edgecolor=NAVY, lw=1.8, zorder=5))
ax.annotate('', xy=(-0.42, 4.1), xytext=(-0.42, 2.5), arrowprops=dict(arrowstyle='->', lw=2.2, color=ORANGE))
ax.text(0.38, 2.5, '$B(0;\\,2e^t-2)$', fontsize=11.5, fontweight='bold', color=ORANGE, va='center')

ax.plot([3.85, 0], [0, 2.52], '--', color=RED, lw=2.2, zorder=4)
ax.text(2.1, 1.45, '$d(t)$', fontsize=12, fontweight='bold', color=RED)

ax.set_xlim(-1.1, 7.8)
ax.set_ylim(-1.0, 5.5)
ax.set_aspect('equal')
ax.axis('off')
plt.savefig(r'd:\Tao_De\Output\De 6\images\phan3_cau3_hairobot_oxy.png', dpi=300, bbox_inches='tight', pad_inches=0.05, facecolor='white')
plt.close(fig)

# 2. Fix De 6 P3 C4: Light cone S(0,0,12), disk R=2 so label does not overlap disk
fig, ax = plt.subplots(figsize=(5.5, 4.4), dpi=300)
ax.plot([0, 0], [0, 12.8], color=NAVY, lw=2.2, zorder=2)
ax.plot(0, 12, 'o', color=NAVY, markersize=10, zorder=6)
ax.text(0.45, 12.0, '$S(0;\\,0;\\,12)$', fontsize=12, fontweight='bold', color=NAVY, va='center')

# Shadow ellipse on Oxy (z=0)
shadow = Ellipse((0, 0), width=8.0, height=2.2, facecolor='#FAD7A0', edgecolor=ORANGE, lw=2.4, alpha=0.55, zorder=1)
ax.add_patch(shadow)
ax.plot(0, 0, 'o', color=GRAY, markersize=6, zorder=3)
ax.text(0, -0.55, 'Bóng $S(t)$ trên $(Oxy)$', fontsize=11.5, fontweight='bold', color=ORANGE, ha='center')

# Moving disk at z(t)
disk = Ellipse((0, 6), width=4.0, height=1.1, facecolor='#76D7C4', edgecolor=NAVY, lw=2.2, alpha=0.85, zorder=4)
ax.add_patch(disk)
ax.plot(0, 6, 'o', color=NAVY, markersize=6, zorder=5)
ax.plot([0, 2.0], [6, 6], '-', color=RED, lw=2.0, zorder=5)
ax.text(1.0, 6.22, '$R=2$', fontsize=10.5, fontweight='bold', color=RED, ha='center')
ax.text(2.18, 5.85, '$C(0;\\,0;\\,z(t))$', fontsize=11.5, fontweight='bold', color=TEAL, va='center')

# Light rays
for rx in [-4.0, -2.8, 2.8, 4.0]:
    ax.plot([0, rx], [12, 0], '--', color=GRAY, lw=1.5, zorder=1)

ax.set_xlim(-4.6, 5.2)
ax.set_ylim(-1.4, 13.2)
ax.axis('off')
plt.savefig(r'd:\Tao_De\Output\De 6\images\phan3_cau4_nonanhsang.png', dpi=300, bbox_inches='tight', pad_inches=0.05, facecolor='white')
plt.close(fig)

# 3. Fix De 6 P3 C6: 3D solid with clean non-overlapping ticks
fig = plt.figure(figsize=(5.6, 4.6), dpi=300)
ax = fig.add_subplot(111, projection='3d')
xs = np.linspace(0, 2, 60)
bs = xs * np.exp(xs) - xs**2
hs = 2 * np.exp(-xs)

ax.plot(xs, np.zeros_like(xs), np.zeros_like(xs), color=NAVY, lw=2.2)
ax.plot(xs, bs, np.zeros_like(xs), color=TEAL, lw=2.6, label='$b(x) = xe^x - x^2$')
ax.plot(xs, np.zeros_like(xs), hs, color=ORANGE, lw=2.6, label='$h(x) = 2e^{-x}$')
ax.plot(xs, bs, hs, '--', color=GRAY, lw=1.4)

for xv in [0.4, 0.85, 1.3, 1.75, 2.0]:
    bv = xv * np.exp(xv) - xv**2
    hv = 2 * np.exp(-xv)
    verts = [[(xv, 0, 0), (xv, bv, 0), (xv, 0, hv)]]
    poly = Poly3DCollection(verts, facecolor=TEAL, edgecolor=NAVY, lw=1.5, alpha=0.35)
    ax.add_collection3d(poly)

ax.set_xticks([0, 0.5, 1.0, 1.5, 2.0])
ax.set_yticks([0, 3, 6, 9])
ax.set_zticks([0, 0.5, 1.0, 1.5, 2.0])
ax.set_xlabel('$x$', fontsize=11, labelpad=-2)
ax.set_ylabel('$b(x)$', fontsize=11, labelpad=-2)
ax.set_zlabel('$h(x)$', fontsize=11, labelpad=-2)
ax.tick_params(labelsize=9, pad=0)
ax.view_init(elev=22, azim=-55)
ax.legend(loc='upper left', fontsize=9.5, framealpha=0.9)
plt.savefig(r'd:\Tao_De\Output\De 6\images\phan3_cau6_thietdien_3d.png', dpi=300, bbox_inches='tight', pad_inches=0.05, facecolor='white')
plt.close(fig)

# Auto-crop whitespace around all PNG plots across De 4, 5, 6
for d in [4, 5, 6]:
    img_dir = rf'd:\Tao_De\Output\De {d}\images'
    for fname in os.listdir(img_dir):
        if fname.endswith('.png'):
            fpath = os.path.join(img_dir, fname)
            im = Image.open(fpath).convert('RGB')
            arr = np.array(im)
            mask = np.any(arr < 248, axis=-1)
            coords = np.argwhere(mask)
            if len(coords) > 0:
                y0, x0 = coords.min(axis=0)
                y1, x1 = coords.max(axis=0) + 1
                pad = 14
                left = max(0, int(x0) - pad)
                top = max(0, int(y0) - pad)
                right = min(im.width, int(x1) + pad)
                bottom = min(im.height, int(y1) + pad)
                im_cropped = im.crop((left, top, right, bottom))
                im_cropped.save(fpath)
                print(f'Cropped {fpath}: {im.size} -> {im_cropped.size}')
