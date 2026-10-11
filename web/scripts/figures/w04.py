"""Infographic สัปดาห์ที่ 4: อัลกอริทึมและการเขียนโปรแกรม
รัน: python scripts/make_week_figures.py 04
ตัวเลขทุกค่าในภาพคำนวณจากโค้ดในไฟล์นี้
"""
import math

import numpy as np
from _style import *  # noqa: F401,F403


# ---------------------------------------------------------------- 1. จากปัญหาสู่โค้ดที่ตรวจแล้ว
def problem_to_code():
    """การคิดเชิงคำนวณ 4 ขั้น → pseudocode → โค้ด (AI ช่วยได้) → ทดสอบ → Big-O"""
    fig, ax = canvas(10.4, 5.6, 13, 7)
    title(ax, "จากปัญหา \"หาคะแนนสูงสุด\" สู่โค้ดที่ตรวจแล้ว", y=6.6)

    ax.text(0.1, 5.95, "① คิดเชิงคำนวณ (Computational Thinking)", fontsize=11, color=BLUE, fontweight="bold")
    pillars = [
        ("Decomposition", "แยกเป็น: รับรายชื่อ\n→ เทียบ → แสดงผล"),
        ("Pattern", "\"เทียบกับค่าที่ดีที่สุด\"\nซ้ำทุกคน"),
        ("Abstraction", "สนใจแค่ตัวเลขคะแนน\nตัดชื่อ/สีเสื้อทิ้ง"),
        ("Algorithm", "best = ตัวแรก\nวนเทียบ มากกว่าก็แทน"),
    ]
    w, gap, x0, y0 = 2.85, 0.33, 0.15, 4.0
    xs4 = [x0 + i * (w + gap) for i in range(4)]
    for i, (head, body) in enumerate(pillars):
        x = xs4[i]
        box(ax, x, y0, w, 1.7, "", BLUE_T, BLUE)
        ax.text(x + w / 2, y0 + 1.35, head, ha="center", fontsize=11.5, fontweight="bold", color=BLUE)
        ax.text(x + w / 2, y0 + 0.62, body, ha="center", va="center", fontsize=10, color=INK2)
        if i < 3:
            arrow(ax, (x + w + 0.02, y0 + 0.85), (x + w + gap - 0.02, y0 + 0.85), color=BLUE)

    # ลูกศรลงสู่แถวล่าง (ขวาสุด)
    arrow(ax, (xs4[3] + w / 2, y0 - 0.05), (xs4[3] + w / 2, 3.0), color=MUTED)

    ax.text(0.1, 3.3, "② แทนอัลกอริทึม แล้วสร้างและตรวจโค้ด (ไหลจากขวาไปซ้าย)", fontsize=11,
            color=ORANGE, fontweight="bold")
    yb = 1.2
    row = [  # (คอลัมน์, หัว, เนื้อหา, สีพื้น, สีขอบ)
        (3, "Pseudocode", "FOR s IN scores:\nIF s > best: best = s", ORANGE_T, ORANGE),
        (2, "โค้ด Python", "AI ช่วยแปลงได้\nแต่เราต้องอ่านทุกบรรทัด", VIOLET_T, VIOLET),
        (1, "ทดสอบ (test)", "max([3,9,4]) == 9\nลิสต์ว่าง? ค่าติดลบ?", AQUA_T, AQUA),
        (0, "วิเคราะห์ Big-O", "n คน → เทียบ n − 1 ครั้ง\n→ O(n)", YELLOW_T, YELLOW),
    ]
    for k, (col, head, body, fill, edge) in enumerate(row):
        x = xs4[col]
        box(ax, x, yb, w, 1.75, "", fill, edge)
        hc = "#9a6a00" if edge == YELLOW else edge
        ax.text(x + w / 2, yb + 1.38, head, ha="center", fontsize=11, fontweight="bold", color=hc)
        ax.text(x + w / 2, yb + 0.62, body, ha="center", va="center", fontsize=10, color=INK2)
        if k < 3:
            arrow(ax, (x - 0.02, yb + 0.88), (x - gap + 0.02, yb + 0.88), color=edge)

    # วงย้อนกลับเมื่อ test ไม่ผ่าน: จาก "ทดสอบ" กลับไป "โค้ด"
    ax.annotate("", xy=(xs4[2] + w / 2, yb - 0.03), xytext=(xs4[1] + w / 2, yb - 0.03),
                arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.5, ls="--",
                                connectionstyle="arc3,rad=0.3", mutation_scale=14))
    ax.text((xs4[1] + xs4[2] + w) / 2, 0.05, "ไม่ผ่าน → กลับไปแก้โค้ด / ถาม AI ใหม่พร้อม error",
            ha="center", fontsize=10, color=ORANGE)
    save(fig, "w04-problem-to-code")


# ---------------------------------------------------------------- 2. Big-O growth
def bigo_growth():
    funcs = [
        ("O(1)", lambda n: np.ones_like(n), AQUA),
        ("O(log n)", lambda n: np.log2(n), BLUE),
        ("O(n)", lambda n: n, VIOLET),
        ("O(n log n)", lambda n: n * np.log2(n), YELLOW),
        ("O(n²)", lambda n: n ** 2, ORANGE),
    ]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.6, 4.6), gridspec_kw=dict(width_ratios=[1, 1.15], wspace=0.42))

    n = np.linspace(1, 40, 400)
    ymax = 220
    for name, f, c in funcs:
        y = f(n)
        a1.plot(n, np.minimum(y, ymax * 1.2), color=c)
        if y[-1] <= ymax:
            ly = {"O(log n)": y[-1] + 9, "O(1)": y[-1] - 2}.get(name, y[-1])
            a1.text(41, ly, name, color=c, fontsize=10.5, va="center", fontweight="bold")
        else:
            xi = n[np.argmax(y > ymax)]
            a1.text(xi - 0.5, ymax - 12, name, color=c, fontsize=10.5, ha="right", fontweight="bold")
    a1.set_xlim(1, 40); a1.set_ylim(0, ymax)
    a1.set_xlabel("ขนาดข้อมูล n"); a1.set_ylabel("จำนวนขั้นโดยประมาณ")
    a1.set_title("n เล็ก: เส้นเริ่มแยกกันเร็วมาก", fontsize=12, fontweight="bold", loc="left")
    ygrid(a1)

    N = 1_000_000
    ops_per_sec = 1e8  # สมมติเครื่องทำได้ราว 10^8 ขั้นต่อวินาที
    vals = [(name, float(f(np.array([N], dtype=float))[0]), c) for name, f, c in funcs]
    steps = [v[1] for v in vals]
    a2.barh(range(len(vals)), steps, color=[v[2] for v in vals], height=0.6)
    a2.set_xscale("log"); a2.set_xlim(0.5, 1e19)
    a2.set_yticks(range(len(vals))); a2.set_yticklabels([v[0] for v in vals], fontsize=11)
    a2.invert_yaxis()

    def fmt_time(sec):
        if sec < 1e-3:
            return f"{sec * 1e6:.2g} µs"
        if sec < 1:
            return f"{sec * 1e3:.3g} ms"
        if sec < 3600:
            return f"{sec:.3g} วินาที"
        return f"≈ {sec / 3600:.3g} ชั่วโมง"

    for i, s in enumerate(steps):
        sup = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
        lab = f"{s:,.0f} ขั้น" if s < 1e9 else f"10{str(round(math.log10(s))).translate(sup)} ขั้น"
        a2.text(s * 1.8, i, f"{lab}  ({fmt_time(s / ops_per_sec)})", va="center", fontsize=10, color=INK2)
    a2.set_xlabel("จำนวนขั้น (สเกล log)")
    a2.set_title(f"n = {N:,}: ต่างกันระดับ µs ถึงชั่วโมง", fontsize=12, fontweight="bold", loc="left")
    a2.xaxis.grid(True, color=GRID, linewidth=0.8); a2.set_axisbelow(True)
    fig.text(0.53, -0.05, "เวลาในวงเล็บสมมติว่าเครื่องทำได้ 10⁸ ขั้น/วินาที", fontsize=9.5, color=MUTED)
    save(fig, "w04-bigo-growth")


# ---------------------------------------------------------------- 3. Binary search trace
def binary_trace():
    data = [12, 25, 31, 47, 58, 63, 77, 84, 90, 99]  # ลิสต์เดียวกับ Lab 04
    target = 77
    trace, low, high = [], 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        trace.append((low, high, mid))
        if data[mid] == target:
            break
        if data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    linear_steps = data.index(target) + 1

    rows = len(trace)
    H = rows * 1.25 + 2.4
    fig, ax = canvas(10.4, 0.8 * H, 13, H)
    top = H
    title(ax, f"Binary search หา {target} ในลิสต์ที่เรียงแล้ว (n = {len(data)})", y=top - 0.4)
    cw, x0 = 0.66, 0.15
    for i in range(len(data)):
        ax.text(x0 + i * cw + cw / 2, top - 1.05, f"[{i}]", ha="center", fontsize=9.5, color=MUTED)
    for r, (lo, hi, mid) in enumerate(trace):
        y = top - 2.0 - r * 1.25
        for i, v in enumerate(data):
            inside = lo <= i <= hi
            fill, edge = (BLUE_T, BLUE) if inside else (GRAY_T, GRID)
            if i == mid:
                fill, edge = (AQUA_T, AQUA) if v == target else (YELLOW_T, YELLOW)
            box(ax, x0 + i * cw + 0.04, y, cw - 0.08, 0.72, str(v), fill, edge, 10.5,
                "bold" if i == mid else "normal", INK if inside else MUTED)
        v = data[mid]
        if v == target:
            msg, col = f"data[{mid}] = {v} → พบแล้ว!", AQUA
        elif v < target:
            msg, col = f"data[{mid}] = {v} < {target} → ทิ้งครึ่งซ้าย (low = {mid + 1})", INK2
        else:
            msg, col = f"data[{mid}] = {v} > {target} → ทิ้งครึ่งขวา (high = {mid - 1})", INK2
        tx = x0 + len(data) * cw + 0.3
        ax.text(tx, y + 0.45, f"รอบ {r + 1}: low={lo}  high={hi}  mid={mid}", fontsize=10.5, fontweight="bold")
        ax.text(tx, y + 0.02, msg, fontsize=10.5, color=col)
    yb = 0.2
    box(ax, x0, yb, 6.1, 0.75, f"Binary: เปรียบเทียบ {rows} ครั้ง · O(log n)", AQUA_T, AQUA, 11, "bold")
    box(ax, x0 + 6.4, yb, 6.3, 0.75, f"Linear: ต้องดู {linear_steps} ตัว · O(n)", ORANGE_T, ORANGE, 11, "bold")
    save(fig, "w04-binary-search-trace")


if __name__ == "__main__":
    problem_to_code()
    bigo_growth()
    binary_trace()
