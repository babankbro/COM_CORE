"""Infographic สัปดาห์ที่ 8: ทบทวนสอบกลางภาค (สัปดาห์ 1–7)
1) w08-concept-map   ผังเชื่อมสัปดาห์ 1–7 รอบ "ระบบเกม/เว็บแอปหนึ่งระบบ"
2) w08-subnet        แยกบิต /26 และแบ่ง 192.168.10.0/24 เป็น 4 subnet
3) w08-search-steps  จำนวนครั้งเปรียบเทียบ (worst case) Linear O(n) vs Binary O(log n)
"""
import math

import numpy as np

from _style import *  # noqa: F401,F403


# ---------------------------------------------------------------- 1
def concept_map():
    fig, ax = canvas(11.6, 7.2, xlim=14, ylim=9.0)
    title(ax, "สัปดาห์ 1–7 คือชั้นต่าง ๆ ของระบบเดียวกัน (ตัวอย่าง: เกม/เว็บแอปของโครงงาน)", y=8.65)
    cx, cy = 7.0, 4.2
    box(ax, cx - 1.9, cy - 0.6, 3.8, 1.2, "ระบบเกม / เว็บแอป\nของโครงงาน", GRAY_T, INK2, size=11.5, weight="bold")
    nodes = [  # (สัปดาห์, หัวเรื่อง, คำสำคัญ, สี, เติม, x, y)
        ("W1", "ภาพรวม CE", "CE/CS/IT · ACM/IEEE · AI", INK2, GRAY_T, 7.0, 7.4),
        ("W2", "Hardware + Software", "CPU/GPU/NPU · OS · memory", BLUE, BLUE_T, 11.6, 6.3),
        ("W3", "Logic + Processor", "เลขฐาน · Boolean · ISA", VIOLET, VIOLET_T, 11.6, 2.1),
        ("W4", "Algorithm + Program", "pseudocode · Big-O · OOP", AQUA, AQUA_T, 7.0, 0.9),
        ("W5", "Database", "ER · SQL · 3NF · ACID", YELLOW, YELLOW_T, 2.4, 2.1),
        ("W6", "Network", "TCP/IP · DNS · subnet", ORANGE, ORANGE_T, 2.4, 6.3),
        ("W7", "Data Center + Cloud", "Docker · IaaS/PaaS/SaaS · PUE", BLUE, BLUE_T, 2.4, 4.2),
    ]
    W, H = 3.6, 1.15
    pos = {}
    for wk, head, keys, c, t, x, y in nodes:
        box(ax, x - W / 2, y - H / 2, W, H, "", t, c)
        ax.text(x, y + 0.2, f"{wk}  {head}", ha="center", va="center", fontsize=10.8, fontweight="bold", color=c)
        ax.text(x, y - 0.25, keys, ha="center", va="center", fontsize=9.8, color=INK2)
        pos[wk] = (x, y)

    def edge(a, b, label, lx, ly):
        (xa, ya), (xb, yb) = a, b
        arrow(ax, (xa, ya), (xb, yb), color=MUTED, lw=1.3)
        ax.text(lx, ly, label, ha="center", va="center", fontsize=9.5, color=INK2,
                bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none"))

    # จากแต่ละสัปดาห์เข้าหาศูนย์กลาง (ปลายลูกศรอยู่ที่ขอบกล่องกลาง)
    targets = {"W1": (cx, cy + 0.62), "W2": (cx + 1.9, cy + 0.4), "W3": (cx + 1.9, cy - 0.4),
               "W4": (cx, cy - 0.62), "W5": (cx - 1.9, cy - 0.45), "W6": (cx - 1.9, cy + 0.45),
               "W7": (cx - 1.9, cy)}
    starts = {"W1": (7.0, 7.4 - H / 2), "W2": (11.6 - W / 2, 6.3 - 0.3), "W3": (11.6 - W / 2, 2.1 + 0.3),
              "W4": (7.0, 0.9 + H / 2), "W5": (2.4 + W / 2, 2.1 + 0.3), "W6": (2.4 + W / 2, 6.3 - 0.3),
              "W7": (2.4 + W / 2, 4.2)}
    labels = {"W1": ("มองภาพรวมเป็นชั้น", 7.0, 6.2), "W2": ("รันบนเครื่องจริง", 10.0, 5.35),
              "W3": ("คำสั่งทำงานระดับวงจร", 10.0, 3.0), "W4": ("กติกาเกม = อัลกอริทึม", 7.0, 2.3),
              "W5": ("save/load คะแนน", 4.2, 3.0), "W6": ("เรียก API ผ่านเน็ต", 4.2, 5.4),
              "W7": ("deploy", 4.65, 4.45)}
    for wk in targets:
        arrow(ax, starts[wk], targets[wk], color=MUTED, lw=1.3)
        t, lx, ly = labels[wk]
        ax.text(lx, ly, t, ha="center", va="center", fontsize=9.5, color=INK2,
                bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none"))
    # ความเชื่อมโยงข้ามสัปดาห์
    arrow(ax, (11.6, 2.1 + H / 2), (11.6, 6.3 - H / 2), color=VIOLET, lw=1.3, ls="--")
    ax.text(12.15, 4.2, "logic สร้าง\nCPU", ha="left", va="center", fontsize=9.5, color=VIOLET)
    arrow(ax, (2.4, 6.3 - H / 2), (2.4, 4.2 + H / 2), color=ORANGE, lw=1.3, ls="--")
    ax.text(0.15, 5.25, "network\nเชื่อม cloud", ha="left", va="center", fontsize=9.5, color=ORANGE)
    save(fig, "w08-concept-map")


# ---------------------------------------------------------------- 2
def subnet():
    prefix, base = 26, "192.168.10"
    host_bits = 32 - prefix
    size = 2 ** host_bits
    fig, ax = canvas(11.4, 5.6, xlim=14, ylim=7.0)
    title(ax, f"อ่าน /{prefix} ให้เป็น: mask · จำนวน host · ช่วงที่อยู่", y=6.65)

    # 32 บิต
    bw = 13.4 / 32
    ax.text(0.3, 5.75, f"32 บิต = network {prefix} บิต (1) + host {host_bits} บิต (0)", fontsize=10.5,
            fontweight="bold")
    for i in range(32):
        net = i < prefix
        ax.add_patch(Rectangle((0.3 + i * bw, 4.85), bw, 0.6, facecolor=BLUE if net else ORANGE,
                               edgecolor="white", linewidth=1))
        ax.text(0.3 + i * bw + bw / 2, 5.15, "1" if net else "0", ha="center", va="center", fontsize=9.5,
                color="white")
    octets = []
    for o in range(4):
        bits = "".join("1" if o * 8 + k < prefix else "0" for k in range(8))
        octets.append(int(bits, 2))
        ax.text(0.3 + (o * 8 + 4) * bw, 4.5, str(octets[-1]), ha="center", fontsize=10.5, fontweight="bold",
                color=INK2)
    mask = ".".join(map(str, octets))
    ax.text(0.3, 3.85, f"mask = {mask}   ·   ที่อยู่ต่อ subnet = 2^{host_bits} = {size}   ·   "
            f"host ที่ใช้ได้ = {size} − 2 = {size - 2}", fontsize=10.5)

    # แบ่ง /24 เป็น 4 ซับเน็ต
    ax.text(0.3, 3.1, f"แบ่ง {base}.0/24 เป็น {256 // size} subnet ขนาด /{prefix}", fontsize=10.5,
            fontweight="bold")
    fills = [(BLUE, BLUE_T), (AQUA, AQUA_T), (VIOLET, VIOLET_T), (YELLOW, YELLOW_T)]
    sw = 13.4 / (256 // size)
    for k in range(256 // size):
        start = k * size
        x = 0.3 + k * sw
        c, t = fills[k]
        box(ax, x + 0.05, 1.3, sw - 0.1, 1.45, "", t, c)
        ax.text(x + sw / 2, 2.42, f"{base}.{start}/{prefix}", ha="center", fontsize=10.5, fontweight="bold", color=c)
        ax.text(x + sw / 2, 1.98, f"network .{start} · broadcast .{start + size - 1}", ha="center", fontsize=9.6)
        ax.text(x + sw / 2, 1.56, f"host .{start + 1} – .{start + size - 2}", ha="center", fontsize=9.6,
                color=INK2)
    ax.text(0.3, 0.75, "สูตร: host ที่ใช้ได้ = 2^(32 − prefix) − 2   (ลบ network address และ broadcast address)",
            fontsize=10, color=INK2)
    save(fig, "w08-subnet")


# ---------------------------------------------------------------- 3
def search_steps():
    ns = [10, 100, 1_000, 10_000, 1_000_000]
    linear = ns
    binary = [math.floor(math.log2(n)) + 1 for n in ns]
    fig, ax = plt.subplots(figsize=(10.4, 4.8))
    ygrid(ax)
    x = np.arange(len(ns))
    w = 0.36
    ax.bar(x - w / 2, linear, w, color=ORANGE, label="Linear search · O(n)")
    ax.bar(x + w / 2, binary, w, color=BLUE, label="Binary search · O(log n) (ข้อมูลต้องเรียงแล้ว)")
    ax.set_yscale("log")
    for xi, a, b in zip(x, linear, binary):
        ax.text(xi - w / 2, a * 1.25, f"{a:,}", ha="center", fontsize=10, color=ORANGE)
        ax.text(xi + w / 2, b * 1.25, f"{b}", ha="center", fontsize=10, color=BLUE, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels([f"n = {n:,}" for n in ns], fontsize=10.5)
    ax.set_ylabel("ครั้งที่เปรียบเทียบ (กรณีแย่สุด, สเกล log)")
    ax.set_ylim(1, max(linear) * 12)
    ax.set_title("ข้อมูลเพิ่ม 1,000 เท่า: Linear ช้าลง 1,000 เท่า แต่ Binary เพิ่มแค่ ~10 ครั้ง",
                 fontsize=12.5, fontweight="bold", loc="left")
    ax.legend(frameon=False, fontsize=10, loc="upper left")
    save(fig, "w08-search-steps")


if __name__ == "__main__":
    concept_map()
    subnet()
    search_steps()
