"""สร้าง infographic ประกอบตัวอย่างโจทย์คำนวณ (ข้อสอบชุดที่ 2–3) → public/images/calc/*.svg
รัน: python scripts/make_calc_figures.py   (ต้องมีฟอนต์ Prompt ในเครื่อง)
ตั้ง PREVIEW_DIR=<โฟลเดอร์> เพื่อบันทึก PNG ไว้ตรวจดู
ตัวเลขทุกค่าในภาพคำนวณจากโค้ดในไฟล์นี้ เพื่อให้ตรงกับเฉลยใน content/calc-examples.md
"""
import math
import os
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle

OUT = Path(__file__).resolve().parent.parent / "public" / "images" / "calc"
OUT.mkdir(parents=True, exist_ok=True)
PREVIEW = os.environ.get("PREVIEW_DIR")

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
    fig.savefig(OUT / f"{name}.svg", bbox_inches="tight", pad_inches=0.15)
    if PREVIEW:
        fig.savefig(Path(PREVIEW) / f"{name}.png", dpi=80, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    print("saved", name)


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


# ======================================================== 1. เลขฐาน
def base_division():
    """บันไดหารสั้นด้วย 2 สำหรับ 25 (ชุด 2) และ 77 (ชุด 3)"""
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.2))
    for ax, n, label, color, tint in [(axes[0], 25, "ชุดที่ 2 · 5.1", BLUE, BLUE_T), (axes[1], 77, "ชุดที่ 3 · 5.2", VIOLET, VIOLET_T)]:
        steps, q = [], n
        while q > 0:
            steps.append((q, q // 2, q % 2))
            q //= 2
        rows = len(steps)
        ax.set_xlim(0, 6); ax.set_ylim(-1.6, rows + 0.9); ax.axis("off")
        ax.text(0.1, rows + 0.45, f"{label}  แปลง {n} เป็นฐานสอง", fontsize=12.5, fontweight="bold")
        for i, (a, qq, r) in enumerate(steps):
            y = rows - 1 - i
            ax.text(1.0, y + 0.1, f"{a} ÷ 2", ha="right", fontsize=11.5)
            ax.text(1.25, y + 0.1, f"= {qq}", fontsize=11.5, color=INK2)
            box(ax, 3.1, y - 0.12, 0.7, 0.62, str(r), tint, color, 13, "bold")
            ax.text(4.0, y + 0.1, "เศษ", fontsize=10, color=MUTED)
        arrow(ax, (4.75, rows - 0.6), (4.75, -0.1), color=ORANGE, lw=2.2)
        ax.text(5.0, rows / 2 - 0.4, "อ่านเศษ\nจากล่าง\nขึ้นบน", fontsize=10, color=ORANGE, va="center")
        result = bin(n)[2:]
        box(ax, 0.3, -1.45, 5.2, 0.85, f"{n} = {result}₂", "#ffffff", color, 14, "bold")
    save(fig, "base-division")


def base_place_value():
    """ค่าประจำหลัก (binary→decimal) และการจับกลุ่ม 4 บิต (binary→hex)"""
    fig = plt.figure(figsize=(10.4, 6.4))
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 13); ax.set_ylim(0, 8); ax.axis("off")
    ax.text(0.3, 7.5, "ฐานสอง → ฐานสิบ: คูณแต่ละบิตด้วยค่าประจำหลัก 2ⁿ แล้วบวก", fontsize=12.5, fontweight="bold")
    for row, bits, tag, color, tint in [(0, "101101", "ชุดที่ 2 · 5.3", BLUE, BLUE_T), (1, "111001", "ชุดที่ 3 · 5.3", VIOLET, VIOLET_T)]:
        y = 6.2 - row * 1.75
        ax.text(0.3, y + 0.25, tag, fontsize=10.5, color=INK2)
        n = len(bits)
        for i, b in enumerate(bits):
            p = n - 1 - i
            x = 2.1 + i * 1.05
            ax.text(x + 0.45, y + 0.82, f"2{'⁰¹²³⁴⁵⁶⁷'[p]} = {2**p}", ha="center", fontsize=8.5, color=MUTED)
            box(ax, x, y, 0.9, 0.62, b, tint if b == "1" else GRAY_T, color if b == "1" else MUTED, 13, "bold")
        terms = [2 ** (n - 1 - i) for i, b in enumerate(bits) if b == "1"]
        ax.text(8.6, y + 0.25, " + ".join(map(str, terms)) + f" = {int(bits, 2)}", fontsize=12, fontweight="bold")
    ax.plot([0.3, 12.7], [2.95, 2.95], color=GRID, linewidth=1)
    ax.text(0.3, 2.25, "ฐานสอง → ฐานสิบหก: แบ่งทีละ 4 บิตจากขวา แล้วแปลงแต่ละกลุ่ม (8 4 2 1)", fontsize=12.5, fontweight="bold")
    for col, bits, tag, color, tint in [(0, "10101111", "ชุดที่ 2 · 5.5", BLUE, BLUE_T), (1, "11011010", "ชุดที่ 3 · 5.5", VIOLET, VIOLET_T)]:
        x0 = 0.4 + col * 6.4
        ax.text(x0, 1.6, tag, fontsize=10.5, color=INK2)
        for g in range(2):
            nib = bits[g * 4:(g + 1) * 4]
            gx = x0 + g * 2.55
            box(ax, gx, 0.75, 2.35, 0.6, nib, tint, color, 13, "bold")
            v = int(nib, 2)
            ax.text(gx + 1.175, 0.38, f"{v} → {format(v, 'X')}", ha="center", fontsize=11, color=INK2)
        ax.text(x0 + 5.25, 1.0, f"= 0x{int(bits, 2):X}", fontsize=13, fontweight="bold", color=color)
    save(fig, "base-place-value")


# ======================================================== 2. เกตตรรกะ
def logic_gates():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 4.8), gridspec_kw={"width_ratios": [1, 1.25]})
    # ตารางความจริง NOR / NAND
    a.set_xlim(0, 6); a.set_ylim(0, 6); a.axis("off")
    a.text(0.1, 5.6, "ตารางค่าความจริง (6.1)", fontsize=12.5, fontweight="bold")
    heads = ["A", "B", "NOR\n(ชุด 2)", "NAND\n(ชุด 3)"]
    xs = [0.4, 1.4, 2.6, 4.2]
    for x, h in zip(xs, heads):
        a.text(x + 0.45, 4.75, h, ha="center", va="center", fontsize=10.5, fontweight="bold", color=INK2)
    for r, (A, B) in enumerate([(0, 0), (0, 1), (1, 0), (1, 1)]):
        y = 3.75 - r * 0.95
        nor, nand = int(not (A or B)), int(not (A and B))
        for x, v, kind in [(xs[0], A, None), (xs[1], B, None), (xs[2], nor, BLUE), (xs[3], nand, VIOLET)]:
            if kind is None:
                a.text(x + 0.45, y + 0.3, str(v), ha="center", va="center", fontsize=12.5)
            else:
                tint = BLUE_T if kind == BLUE else VIOLET_T
                box(a, x, y, 0.9, 0.6, str(v), tint if v else "#ffffff", kind, 12.5, "bold")
    a.text(0.1, -0.05, "NOR = 1 เฉพาะเมื่ออินพุตเป็น 0 ทั้งคู่ · NAND = 0 เฉพาะเมื่อเป็น 1 ทั้งคู่", fontsize=9.5, color=INK2)
    # การหาค่านิพจน์ทีละขั้น
    b.set_xlim(0, 8); b.set_ylim(0, 6); b.axis("off")
    b.text(0.1, 5.6, "หาค่านิพจน์ทีละขั้น (6.3)", fontsize=12.5, fontweight="bold")
    s2 = [("ชุด 2: A=0, B=1, C=1", INK2), ("A OR B = 0 OR 1 = 1", BLUE), ("NOT C = NOT 1 = 0", BLUE), ("Y = 1 AND 0 = 0", BLUE)]
    s3 = [("ชุด 3: A=1, B=1, C=0", INK2), ("A AND B = 1", VIOLET), ("NOT(A AND B) = 0", VIOLET), ("Y = 0 OR C = 0 OR 0 = 0", VIOLET)]
    for col, steps, tint in [(0, s2, BLUE_T), (1, s3, VIOLET_T)]:
        x = 0.0 + col * 4.05
        for i, (t, c) in enumerate(steps):
            y = 4.55 - i * 1.1
            if i == 0:
                b.text(x + 1.85, y + 0.25, t, ha="center", fontsize=10.5, fontweight="bold", color=c)
            else:
                box(b, x, y, 3.9, 0.65, t, tint if i == 3 else "#ffffff", c, 9.5, "bold" if i == 3 else "normal")
                arrow(b, (x + 1.85, y + 1.1), (x + 1.85, y + 0.68))
    save(fig, "logic-gates")


# ======================================================== 3. Big-O
def bigo_counts():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 4.4))
    n = 1024
    lin, binc = n, int(math.floor(math.log2(n))) + 1
    a.barh([1, 0], [lin, binc], color=[ORANGE, BLUE], height=0.55)
    a.set_yticks([1, 0], ["Linear Search\nO(n)", "Binary Search\nO(log n)"])
    a.text(lin, 1, f"  {lin:,} ครั้ง", va="center", fontweight="bold")
    a.text(binc, 0, f"  {binc} ครั้ง (≈ log₂1024 = 10)", va="center", fontweight="bold")
    a.set_xlim(0, 1500); a.set_xlabel("จำนวนการเปรียบเทียบกรณีแย่ที่สุด")
    a.set_title("ชุด 2 · 9.2  ข้อมูลเรียงแล้ว 1,024 ตัว", loc="left", fontweight="bold")
    # ชุด 3 log scale
    n3 = 10_000
    nlogn, n2 = n3 * 13.3, n3 ** 2
    b.bar([0, 1, 2], [n3, nlogn, n2], color=[AQUA, BLUE, ORANGE], width=0.6)
    b.set_yscale("log"); b.set_ylim(1e3, 1e9)
    b.set_xticks([0, 1, 2], ["O(n)", "O(n log n)", "O(n²)"])
    for x, v in zip([0, 1, 2], [n3, nlogn, n2]):
        b.text(x, v * 1.6, f"{v:,.0f}", ha="center", fontweight="bold", fontsize=10.5)
    b.set_title("ชุด 3 · 9.2  n = 10,000 (แกนตั้งแบบลอการิทึม)", loc="left", fontweight="bold")
    b.text(-0.35, 4e8, f"n² มากกว่า n log n\n≈ {n2 / nlogn:,.0f} เท่า", ha="left", va="top", fontsize=10.5, color=INK2)
    ygrid(b)
    save(fig, "bigo-counts")


# ======================================================== 4. PUE และพลังงาน
def pue_bars():
    fig, ax = plt.subplots(figsize=(10.4, 4.6))
    cases = [
        ("ชุด 2 · 14.2\nก่อนปรับปรุง", 1600, 2400, BLUE),
        ("ชุด 2 · 14.3\nPUE = 1.2", 1600, 1.2 * 1600, BLUE),
        ("ชุด 3 · 14.2\nPUE = 1.6", 500, 1.6 * 500, VIOLET),
    ]
    for i, (lab, it, total, c) in enumerate(cases):
        ax.bar(i, it, color=c, width=0.55)
        ax.bar(i, total - it, bottom=it, color=YELLOW, width=0.55)
        ax.text(i, it / 2, f"IT\n{it:,.0f} kW", ha="center", va="center", color="#ffffff", fontweight="bold", fontsize=10.5)
        ax.text(i, it + (total - it) / 2, f"ส่วนอื่น\n{total - it:,.0f} kW", ha="center", va="center", fontsize=9.5)
        ax.text(i, total + 70, f"รวม {total:,.0f} kW\nPUE = {total / it:.2g}", ha="center", fontweight="bold", fontsize=10.5)
    ax.set_xticks(range(3), [c[0] for c in cases])
    ax.set_ylim(0, 3200); ax.set_ylabel("กิโลวัตต์ (kW)")
    ax.annotate("", xy=(0.78, 2140), xytext=(0.28, 2140), arrowprops=dict(arrowstyle="-|>", color=AQUA, lw=2))
    ax.text(0.5, 3080, "ลดลง 2,400 − 1,920\n= 480 kW (20%)", ha="center", va="top", color=AQUA, fontweight="bold", fontsize=10)
    ax.text(2.55, 2500, "PUE = พลังงานรวม ÷ พลังงาน IT\nพลังงานรวม = PUE × IT\nส่วนอื่น (cooling, ไฟ) = รวม − IT",
            fontsize=10, color=INK2, va="top", ha="left",
            bbox=dict(boxstyle="round,pad=0.5", facecolor=GRAY_T, edgecolor=MUTED))
    ax.set_xlim(-0.6, 3.9)
    ygrid(ax)
    save(fig, "pue-bars")


def pue_daily_cost():
    fig, ax = plt.subplots(figsize=(10.4, 2.9)); ax.set_xlim(0, 13); ax.set_ylim(0, 3.2); ax.axis("off")
    ax.text(0.1, 2.85, "ชุด 3 · 14.3  จากกำลังไฟ (kW) สู่พลังงานต่อวัน (kWh) และค่าไฟ", fontsize=12.5, fontweight="bold")
    kw, h, rate = 800, 24, 4
    kwh = kw * h
    items = [(f"กำลังไฟรวม\n{kw} kW", VIOLET_T, VIOLET), (f"× {h} ชั่วโมง", "#ffffff", MUTED),
             (f"พลังงาน\n{kwh:,} kWh/วัน", YELLOW_T, YELLOW), (f"× {rate} บาท/kWh", "#ffffff", MUTED),
             (f"ค่าไฟ\n{kwh * rate:,} บาท/วัน", AQUA_T, AQUA)]
    x = 0.1
    widths = [2.4, 1.9, 2.6, 2.0, 2.7]
    for (t, fill, edge), w in zip(items, widths):
        box(ax, x, 0.85, w, 1.35, t, fill, edge, 11.5, "bold")
        if x + w < 12:
            arrow(ax, (x + w + 0.02, 1.52), (x + w + 0.2, 1.52))
        x += w + 0.22
    ax.text(0.1, 0.25, "kW คืออัตราการใช้พลังงาน (กำลังไฟ) · kWh = kW × ชั่วโมง คือปริมาณพลังงาน (หน่วยที่การไฟฟ้าคิดเงิน)",
            fontsize=9.8, color=INK2)
    save(fig, "pue-daily-cost")


# ======================================================== 5. เวลาไฟกะพริบ ESP32
def led_timeline():
    fig, (a, b) = plt.subplots(2, 1, figsize=(10.4, 5.6), gridspec_kw={"hspace": 0.75})
    # ชุด 2 22.3: blink(L, t) มี sleep ครั้งเดียว t = 0.2(i+1)
    pins2 = [5, 17, 16, 4]
    t = 0.0
    for i, p in enumerate(pins2):
        d = round(0.2 * (i + 1), 2)
        a.broken_barh([(t, d)], (len(pins2) - 1 - i - 0.35, 0.7), facecolors=BLUE)
        a.text(t + d / 2, len(pins2) - 1 - i, f"{d:g} s", ha="center", va="center", color="#ffffff", fontsize=9.5, fontweight="bold")
        t += d
    a.set_yticks(range(len(pins2)), [f"GPIO {p}" for p in reversed(pins2)])
    a.set_xlim(0, 2.3); a.set_xlabel("เวลา (วินาที)")
    a.axvline(t, color=ORANGE, linestyle="--", linewidth=1.5)
    a.text(t + 0.03, 3.25, f"ครบ 1 รอบ = {t:g} s", color=ORANGE, fontweight="bold")
    a.set_title("ชุด 2 · 22.3  blink(L, t) มี sleep ครั้งเดียว → เวลาต่อดวง = t = 0.2 × (i+1)", loc="left", fontweight="bold")
    # ชุด 3 22.3: leds[::2] = GPIO 2, 16, 5 ดวงละ 0.3 s แล้ว sleep(1)
    pins = [2, 4, 16, 17, 5]
    chosen = pins[::2]
    t = 0.0
    for p in chosen:
        row = pins.index(p)
        b.broken_barh([(t, 0.3)], (len(pins) - 1 - row - 0.35, 0.7), facecolors=VIOLET)
        t += 0.3
    b.broken_barh([(t, 1.0)], (-0.85, 0.5), facecolors=GRAY_T, edgecolor=MUTED)
    b.text(t + 0.5, -0.6, "sleep(1)", ha="center", va="center", fontsize=9.5)
    t += 1.0
    b.set_yticks(range(len(pins)), [f"GPIO {p}" + ("  ✓" if p in chosen else "") for p in reversed(pins)])
    b.set_ylim(-1, len(pins) - 0.4); b.set_xlim(0, 2.3); b.set_xlabel("เวลา (วินาที)")
    b.axvline(t, color=ORANGE, linestyle="--", linewidth=1.5)
    b.text(t + 0.03, 3.6, f"ครบ 1 รอบ = 3×0.3 + 1 = {t:g} s", color=ORANGE, fontweight="bold")
    b.set_title("ชุด 3 · 22.3  leds[::2] เลือก index 0, 2, 4 → GPIO 2, 16, 5", loc="left", fontweight="bold")
    save(fig, "led-timeline")


def led_toggle():
    fig, ax = plt.subplots(figsize=(10.4, 2.6)); ax.set_xlim(0, 13); ax.set_ylim(0, 3); ax.axis("off")
    ax.text(0.1, 2.65, "ชุด 3 · 22.2  led.value(not led.value()) วน 5 รอบ (เริ่มต้นดับ)", fontsize=12.5, fontweight="bold")
    state = 0
    box(ax, 0.1, 0.9, 1.6, 1.1, "เริ่ม\nดับ", GRAY_T, MUTED, 11)
    for i in range(5):
        state ^= 1
        x = 2.1 + i * 2.05
        arrow(ax, (x - 0.38, 1.45), (x - 0.05, 1.45))
        box(ax, x, 0.9, 1.6, 1.1, f"รอบ {i + 1}\n{'ติด' if state else 'ดับ'}", YELLOW_T if state else GRAY_T,
            YELLOW if state else MUTED, 11, "bold" if i == 4 else "normal")
        ax.text(x + 0.8, 0.62, f"t = {0.4 * (i + 1):.1f} s", ha="center", fontsize=9, color=MUTED)
    ax.text(0.1, 0.12, "สลับ 5 ครั้ง (จำนวนคี่) → จบที่สถานะตรงข้ามกับตอนเริ่ม = ติด · เวลารวม 5 × 0.4 = 2.0 s", fontsize=10, color=INK2)
    save(fig, "led-toggle")


# ======================================================== 6. รอบเวลาและจำนวนข้อมูล
def rows_and_timeout():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 4.0), gridspec_kw={"width_ratios": [1.15, 1]})
    intervals = [10, 30, 60]
    per_hour = [3600 // s for s in intervals]
    per_day = [86400 // s for s in intervals]
    cols = [MUTED, MUTED, BLUE]
    a.bar(range(3), per_day, color=cols, width=0.55)
    for i, (h, d) in enumerate(zip(per_hour, per_day)):
        a.text(i, d + 200, f"{d:,} แถว/วัน\n({h} แถว/ชม.)", ha="center", fontsize=10, fontweight="bold" if i == 2 else "normal")
    a.set_xticks(range(3), [f"sleep({s})" for s in intervals])
    a.set_ylim(0, 11500); a.set_ylabel("แถวต่อวัน")
    a.set_title("ชุด 2 · 25.1  แถวที่ appendRow บันทึก", loc="left", fontweight="bold"); ygrid(a)
    a.text(2.4, 9800, "แถว/ชม. = 3,600 ÷ วินาทีต่อรอบ\nแถว/วัน = 86,400 ÷ วินาทีต่อรอบ", ha="right", va="top", fontsize=9.5, color=INK2)
    # timeout
    b.set_xlim(0, 10); b.set_ylim(0, 6); b.axis("off")
    b.set_title("ชุด 2 · 23.1  รอ Wi-Fi แบบมี timeout", loc="left", fontweight="bold")
    box(b, 0.3, 4.2, 9.4, 1.0, "for i in range(20):  ...  sleep(0.5)", BLUE_T, BLUE, 11, "bold")
    box(b, 0.3, 2.6, 9.4, 1.0, "รอได้สูงสุด 20 × 0.5 = 10 วินาที แล้วออกจากลูป", "#ffffff", BLUE, 11)
    box(b, 0.3, 0.6, 9.4, 1.4, "while not wlan.isconnected():\nถ้าเชื่อมต่อไม่ได้ → ค้างตลอดไป", ORANGE_T, ORANGE, 10.5)
    arrow(b, (5, 4.2), (5, 3.62))
    save(fig, "rows-timeout")


# ======================================================== 7. I2C รวมไบต์ + ตัดสินใจ
def i2c_bytes():
    fig, ax = plt.subplots(figsize=(10.4, 4.8)); ax.set_xlim(0, 13); ax.set_ylim(0, 6.2); ax.axis("off")
    ax.text(0.1, 5.8, "value = data[0] | (data[1] << 8)  — Little-endian: ไบต์ต่ำมาก่อน", fontsize=12.5, fontweight="bold")
    cases = [("ชุด 2 · 24.3", [0xA0, 0x01], BLUE, BLUE_T), ("ชุด 3 · 24.3 UVA", [0xFF, 0x00], VIOLET, VIOLET_T),
             ("ชุด 3 · 24.3 UVB", [0x00, 0x02], VIOLET, VIOLET_T)]
    for r, (tag, data, c, tint) in enumerate(cases):
        y = 4.4 - r * 1.75
        lo, hi = data
        v = lo | (hi << 8)
        ax.text(0.1, y + 0.3, tag, fontsize=10.5, color=INK2)
        box(ax, 2.2, y, 1.6, 0.7, f"0x{lo:02X}", GRAY_T, MUTED, 12, "bold")
        ax.text(3.0, y - 0.28, "data[0] ไบต์ต่ำ", ha="center", fontsize=8.5, color=MUTED)
        box(ax, 4.0, y, 1.6, 0.7, f"0x{hi:02X}", GRAY_T, MUTED, 12, "bold")
        ax.text(4.8, y - 0.28, "data[1] ไบต์สูง", ha="center", fontsize=8.5, color=MUTED)
        arrow(ax, (5.75, y + 0.35), (6.4, y + 0.35), color=c)
        box(ax, 6.5, y, 1.25, 0.7, f"{hi:02X}", tint, c, 12, "bold")
        box(ax, 7.8, y, 1.25, 0.7, f"{lo:02X}", tint, c, 12, "bold")
        ax.text(7.13, y + 0.85, "<< 8", ha="center", fontsize=8.5, color=c)
        ax.text(9.3, y + 0.35, f"= 0x{v:04X} = {v:,}", va="center", fontsize=13, fontweight="bold", color=c)
    ax.text(0.1, 0.05, "ตรวจคำตอบ: ค่าฐานสิบ = data[1] × 256 + data[0]  เช่น 1 × 256 + 160 = 416", fontsize=10, color=INK2)
    save(fig, "i2c-bytes")


def sensor_decision():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 4.6))
    for ax in (a, b):
        ax.set_xlim(0, 10); ax.set_ylim(0, 7); ax.axis("off")
    # ชุด 2
    a.set_title("ชุด 2 · 24.4  t = 33.0, h = 85", loc="left", fontweight="bold")
    box(a, 1.0, 5.2, 8, 1.0, "t > 35  or  h > 80 ?", YELLOW_T, YELLOW, 12, "bold")
    box(a, 0.4, 3.2, 4.1, 1.2, "t > 35 → 33 > 35\nเท็จ (False)", GRAY_T, MUTED, 10.5)
    box(a, 5.5, 3.2, 4.1, 1.2, "h > 80 → 85 > 80\nจริง (True)", BLUE_T, BLUE, 10.5, "bold")
    arrow(a, (3.5, 5.2), (2.5, 4.42)); arrow(a, (6.5, 5.2), (7.5, 4.42))
    box(a, 1.5, 0.9, 7, 1.3, "False or True = True\n→ led.on()  LED ติด", AQUA_T, AQUA, 12, "bold")
    arrow(a, (5, 3.2), (5, 2.22))
    # ชุด 3
    h_, t_ = 60, 31
    heat = t_ + 0.1 * h_
    b.set_title(f"ชุด 3 · 24.4  t = {t_}, h = {h_}", loc="left", fontweight="bold")
    box(b, 0.8, 5.5, 8.4, 0.95, f"heat = t + 0.1h = {t_} + {0.1 * h_:g} = {heat:g}", VIOLET_T, VIOLET, 12, "bold")
    box(b, 0.3, 3.6, 2.9, 1.2, "heat ≥ 38 ?\nเท็จ", GRAY_T, MUTED, 10.5)
    box(b, 3.55, 3.6, 2.9, 1.2, "heat ≥ 35 ?\nจริง ✓", BLUE_T, BLUE, 10.5, "bold")
    box(b, 6.8, 3.6, 2.9, 1.2, "else\n(ไม่ถึง)", GRAY_T, MUTED, 10.5)
    arrow(b, (5, 5.5), (5, 4.82))
    box(b, 2.2, 1.1, 5.6, 1.3, "เข้า elif → blink(led)\nLED กะพริบ", AQUA_T, AQUA, 12, "bold")
    arrow(b, (5, 3.6), (5, 2.42))
    b.text(0.3, 0.3, "if-elif-else ตรวจจากบนลงล่าง ทำแค่กิ่งแรกที่เป็นจริง", fontsize=9.5, color=INK2)
    save(fig, "sensor-decision")


# ======================================================== 8. Linear regression
def regression_residuals():
    xs, ys = np.array([1, 2, 3, 4]), np.array([3, 5, 6, 9])
    m, c = 2, 1
    pred = m * xs + c
    e = ys - pred
    mse = float(np.mean(e ** 2))
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 4.4), gridspec_kw={"width_ratios": [1.2, 1]})
    xx = np.linspace(0, 10.5, 50)
    a.plot(xx, m * xx + c, color=BLUE, label="ŷ = 2x + 1")
    a.scatter(xs, ys, s=55, color=INK, zorder=3, label="ข้อมูลจริง")
    for x, y, p in zip(xs, ys, pred):
        if y != p:
            a.plot([x, x], [y, p], color=ORANGE, linewidth=2.5)
            a.annotate(f"e = {y} − {p} = {y - p}", (x, (y + p) / 2), (x + 0.4, (y + p) / 2 - 1.2), color=ORANGE,
                       fontweight="bold", arrowprops=dict(arrowstyle="-", color=ORANGE))
    a.scatter([10], [21], s=80, color=AQUA, zorder=3)
    a.annotate("x = 10 → ŷ = 21 (26.1)", (10, 21), (4.2, 20), fontweight="bold", arrowprops=dict(arrowstyle="-", color=MUTED))
    a.set_xlim(0, 10.8); a.set_ylim(0, 23); a.set_xlabel("x"); a.set_ylabel("y")
    a.legend(frameon=False, loc="upper left"); ygrid(a)
    a.set_title("ชุด 2 · 26  ค่าคลาดเคลื่อน e = y − ŷ", loc="left", fontweight="bold")
    b.set_xlim(0, 10); b.set_ylim(0, 7); b.axis("off")
    b.text(0.2, 6.5, "ตารางคำนวณ MSE และ RMSE", fontsize=12, fontweight="bold")
    headers = ["x", "y", "ŷ", "e", "e²"]
    for j, h in enumerate(headers):
        b.text(1.0 + j * 1.8, 5.7, h, ha="center", fontweight="bold", color=INK2)
    for i, (x, y, p, ee) in enumerate(zip(xs, ys, pred, e)):
        for j, v in enumerate([x, y, p, ee, ee ** 2]):
            b.text(1.0 + j * 1.8, 5.0 - i * 0.65, str(v), ha="center", color=ORANGE if (j >= 3 and ee != 0) else INK)
    b.plot([0.3, 9.6], [2.25, 2.25], color=GRID)
    box(b, 0.3, 0.9, 9.3, 1.1, f"MSE = Σe² / N = {int(np.sum(e ** 2))}/4 = {mse:g}", BLUE_T, BLUE, 12, "bold")
    box(b, 0.3, -0.35, 9.3, 1.0, f"RMSE = √MSE = √{mse:g} = {math.sqrt(mse):g}", AQUA_T, AQUA, 12, "bold")
    b.set_ylim(-0.5, 7)
    save(fig, "regression-residuals")


def gradient_step():
    xs, ys = np.array([0, 1, 2, 3]), np.array([1, 3, 4, 8])
    m, c, lr = 2.0, 1.0, 0.05
    N = len(xs)
    e = (m * xs + c) - ys
    gm, gc = float(np.sum(2 * e * xs) / N), float(np.sum(2 * e) / N)
    m2, c2 = m - lr * gm, c - lr * gc
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 4.4), gridspec_kw={"width_ratios": [1.1, 1]})
    xx = np.linspace(-0.2, 3.4, 30)
    a.plot(xx, m * xx + c, color=MUTED, linestyle="--", label=f"ก่อน: ŷ = {m:g}x + {c:g}")
    a.plot(xx, m2 * xx + c2, color=VIOLET, label=f"หลัง 1 รอบ: ŷ = {m2:g}x + {c2:g}")
    a.scatter(xs, ys, s=55, color=INK, zorder=3)
    for x, y, ee in zip(xs, ys, e):
        p = m * x + c
        if ee:
            a.plot([x, x], [y, p], color=ORANGE, linewidth=2.5)
            a.text(x - 0.08 if x == 3 else x + 0.08, (y + p) / 2, f"e = ŷ − y = {ee:+g}", color=ORANGE, fontsize=10,
                   fontweight="bold", ha="right" if x == 3 else "left")
    a.set_xlabel("x"); a.set_ylabel("y"); a.legend(frameon=False, loc="upper left"); ygrid(a)
    a.set_title("ชุด 3 · 26  ปรับเส้นด้วย Gradient Descent", loc="left", fontweight="bold")
    b.set_xlim(0, 10); b.set_ylim(0, 7.2); b.axis("off")
    b.text(0.2, 6.8, "คำนวณ 1 รอบ (lr = 0.05)", fontsize=12, fontweight="bold")
    lines = [
        ("e = ŷ − y = (0, 0, 1, −1)  →  MSE = 2/4 = 0.5", GRAY_T, MUTED),
        (f"grad_m = (2/N)·Σ e·x = (2/4)(0+0+2−3) = {gm:g}", VIOLET_T, VIOLET),
        (f"grad_c = (2/N)·Σ e = (2/4)(0+0+1−1) = {gc:g}", VIOLET_T, VIOLET),
        (f"m = 2 − 0.05 × ({gm:g}) = {m2:g}", AQUA_T, AQUA),
        (f"c = 1 − 0.05 × {gc:g} = {c2:g}", AQUA_T, AQUA),
    ]
    for i, (t, fill, edge) in enumerate(lines):
        box(b, 0.2, 5.6 - i * 1.15, 9.6, 0.85, t, fill, edge, 10.5, "bold" if i >= 3 else "normal")
    save(fig, "gradient-step")


# ======================================================== 9. YOLO: confidence และ IoU
def iou_conf():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 4.6))
    # IoU
    a.set_xlim(0, 12); a.set_ylim(0, 10); a.set_aspect("equal"); a.axis("off")
    a.set_title("ชุด 3 · 27.2  IoU = พื้นที่ซ้อนทับ ÷ พื้นที่รวม", loc="left", fontweight="bold")
    # วาดตามสเกล (1 ช่อง = 2 หน่วย): A = 10×8 = 80, B = 6×10 = 60, ซ้อนทับ = 5×8 = 40 → พื้นที่รวม = 100
    a.add_patch(Rectangle((1, 2.2), 5, 4, facecolor=BLUE_T, edgecolor=BLUE, linewidth=2))
    a.add_patch(Rectangle((3.5, 2.2), 3, 5, facecolor=ORANGE_T, edgecolor=ORANGE, linewidth=2, alpha=0.8))
    a.add_patch(Rectangle((3.5, 2.2), 2.5, 4, facecolor=VIOLET, edgecolor=VIOLET, alpha=0.6))
    a.text(4.75, 4.2, "ซ้อนทับ\n5×8 = 40", ha="center", va="center", color="#ffffff", fontweight="bold", fontsize=10)
    a.text(2.25, 4.2, "A\n10×8\n= 80", ha="center", va="center", color=BLUE, fontweight="bold", fontsize=10)
    a.text(6.7, 6.8, "B = 6×10 = 60", color=ORANGE, fontweight="bold", fontsize=10)
    a.text(6, 0.9, "IoU = 40 / 100 = 0.4", ha="center", fontsize=13, fontweight="bold")
    a.text(6, 0.1, "พื้นที่รวม = A + B − ซ้อนทับ = 80 + 60 − 40 = 100", ha="center", fontsize=9.5, color=INK2)
    # confidence threshold
    dets = [("person", 0.91), ("person", 0.38), ("chair", 0.55)]
    thr = 0.4
    cols = [AQUA if s >= thr else GRAY_T for _, s in dets]
    b.barh(range(3), [s for _, s in dets], color=cols, edgecolor=[AQUA if s >= thr else MUTED for _, s in dets], height=0.55)
    b.set_yticks(range(3), [f"{n} {s:.2f}" for n, s in dets]); b.invert_yaxis()
    b.axvline(thr, color=ORANGE, linestyle="--")
    b.text(thr + 0.01, 2.5, f"conf = {thr}", color=ORANGE, fontweight="bold")
    for i, (_, s) in enumerate(dets):
        b.text(s + 0.02, i, "พิมพ์ ✓" if s >= thr else "ถูกตัด ✗", va="center", fontweight="bold",
               color=AQUA if s >= thr else MUTED)
    b.set_xlim(0, 1.15); b.set_xlabel("ความเชื่อมั่น (confidence)")
    b.set_title("ชุด 3 · 27.1  กล่องที่ผ่านเกณฑ์ conf", loc="left", fontweight="bold")
    save(fig, "iou-conf")


def data_split():
    fig, ax = plt.subplots(figsize=(10.4, 2.4)); ax.set_xlim(0, 1000); ax.set_ylim(0, 2); ax.axis("off")
    ax.text(0, 1.75, "ชุด 3 · 28.2  validation_split = 0.2 กับภาพ 1,000 ภาพ", fontsize=12.5, fontweight="bold")
    ax.add_patch(Rectangle((0, 0.55), 800, 0.8, facecolor=BLUE, edgecolor="none"))
    ax.add_patch(Rectangle((800, 0.55), 200, 0.8, facecolor=ORANGE, edgecolor="none"))
    ax.text(400, 0.95, "ฝึก (training) 1,000 × 0.8 = 800 ภาพ", ha="center", va="center", color="#ffffff", fontweight="bold")
    ax.text(900, 0.95, "ตรวจสอบ 200", ha="center", va="center", color="#ffffff", fontweight="bold")
    ax.text(0, 0.15, "ชุดตรวจสอบไม่ถูกใช้ปรับน้ำหนัก ใช้วัด val_accuracy เพื่อดู overfitting และให้ EarlyStopping ตัดสินใจ", fontsize=10, color=INK2)
    save(fig, "data-split")


if __name__ == "__main__":
    base_division()
    base_place_value()
    logic_gates()
    bigo_counts()
    pue_bars()
    pue_daily_cost()
    led_timeline()
    led_toggle()
    rows_and_timeout()
    i2c_bytes()
    sensor_decision()
    regression_residuals()
    gradient_step()
    iou_conf()
    data_split()
