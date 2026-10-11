"""สไตล์กลางของ infographic รายสัปดาห์ (ใช้ร่วมกับ scripts/figures/wXX.py)
ภาพบันทึกที่ public/images/weeks/<name>.svg · ตั้ง PREVIEW_DIR เพื่อบันทึก PNG ไว้ตรวจดู
"""
import os
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle  # noqa: E402,F401

OUT = Path(__file__).resolve().parents[2] / "public" / "images" / "weeks"
OUT.mkdir(parents=True, exist_ok=True)
PREVIEW = os.environ.get("PREVIEW_DIR")

# พาเลตเดียวกับ infographic หน้าโจทย์คำนวณ
BLUE, ORANGE, AQUA, YELLOW, VIOLET = "#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#4a3aa7"
INK, INK2, MUTED, GRID, SURFACE = "#0b0b0b", "#52514e", "#8a8984", "#e4e3df", "#ffffff"
BLUE_T, ORANGE_T, AQUA_T, YELLOW_T, VIOLET_T, GRAY_T = "#dbe8f8", "#fce3d8", "#d3f1e6", "#fbecc8", "#e4e1f4", "#f1f0ec"

plt.rcParams.update({
    "font.family": ["Prompt", "DejaVu Sans"],
    "font.size": 11,
    "text.color": INK,
    "axes.edgecolor": MUTED,
    "axes.labelcolor": INK2,
    "xtick.color": INK2,
    "ytick.color": INK2,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": False,
    "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE,
    "svg.fonttype": "path",
    "lines.linewidth": 2,
})


def save(fig, name):
    """บันทึก public/images/weeks/<name>.svg (ชื่อควรขึ้นต้นด้วย wXX-)"""
    fig.savefig(OUT / f"{name}.svg", bbox_inches="tight", pad_inches=0.15)
    if PREVIEW:
        fig.savefig(Path(PREVIEW) / f"{name}.png", dpi=80, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    print("saved", name)


def canvas(w=10.4, h=5.0, xlim=13, ylim=6.5):
    """ผืนวาดแบบไม่มีแกน สำหรับแผนภาพกล่อง-ลูกศร"""
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, xlim); ax.set_ylim(0, ylim); ax.axis("off")
    return fig, ax


def ygrid(ax):
    ax.yaxis.grid(True, color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)


def box(ax, x, y, w, h, text, fill, edge, size=11, weight="normal", color=INK):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.06",
                                facecolor=fill, edgecolor=edge, linewidth=1.5))
    if text:
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=size, fontweight=weight, color=color)


def arrow(ax, p, q, color=MUTED, style="-|>", lw=1.5, ls="-"):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=style, mutation_scale=14, color=color, linewidth=lw, linestyle=ls))


def title(ax, text, x=0.1, y=None, size=12.5):
    ax.text(x, y if y is not None else ax.get_ylim()[1] - 0.35, text, fontsize=size, fontweight="bold")
