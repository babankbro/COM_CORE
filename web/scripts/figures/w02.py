"""Infographic สัปดาห์ที่ 2: ฮาร์ดแวร์ ซอฟต์แวร์ และระบบนิเวศสมัยใหม่
รัน: python scripts/make_week_figures.py 02
"""
import numpy as np

from _style import *  # noqa: F401,F403


# ---------------------------------------------------------------- 1. ชั้นของระบบ + เส้นทางคำสั่ง Save
def layers():
    stack = [  # (ชื่อชั้น, ตัวอย่าง, สีเข้ม, สีอ่อน) จากบนลงล่าง
        ("ผู้ใช้", "กดปุ่ม Save ในเกม", INK2, GRAY_T),
        ("Application", "เกม Python, เบราว์เซอร์, VS Code", BLUE, BLUE_T),
        ("Library / Runtime", "Python interpreter, open(), json", BLUE, BLUE_T),
        ("OS kernel", "system call · process · ไฟล์", VIOLET, VIOLET_T),
        ("Device driver", "ไดรเวอร์ SSD, GPU, Wi-Fi", VIOLET, VIOLET_T),
        ("Firmware", "UEFI/BIOS, firmware ในตัว SSD", ORANGE, ORANGE_T),
        ("Hardware", "CPU · GPU/NPU · RAM · SSD · I/O", ORANGE, ORANGE_T),
    ]
    n = len(stack)
    rh = 0.78
    fig, ax = canvas(10.4, 6.6, 13, n * rh + 1.4)
    title(ax, "ระบบคอมพิวเตอร์เป็นชั้น: คำสั่ง \"Save\" เดินทางลงไปถึงฮาร์ดแวร์แล้วย้อนกลับ")
    top = n * rh + 0.45
    for i, (name, ex, c, t) in enumerate(stack):
        y = top - (i + 1) * rh
        box(ax, 0.2, y + 0.06, 6.9, rh - 0.12, None, t, c)
        ax.text(0.45, y + rh / 2, name, va="center", fontsize=11.5, fontweight="bold", color=c)
        ax.text(3.0, y + rh / 2, ex, va="center", fontsize=10.5, color=INK2)
    # คำอธิบายสี: กลุ่มซอฟต์แวร์ / ฮาร์ดแวร์
    for k, (lab, c, t) in enumerate([("ซอฟต์แวร์ประยุกต์", BLUE, BLUE_T), ("ซอฟต์แวร์ระบบ", VIOLET, VIOLET_T), ("ฮาร์ดแวร์ + เฟิร์มแวร์", ORANGE, ORANGE_T)]):
        ax.add_patch(Rectangle((0.3 + k * 2.6, 0.05), 0.35, 0.28, facecolor=t, edgecolor=c))
        ax.text(0.75 + k * 2.6, 0.19, lab, va="center", fontsize=9.5, color=c)
    # เส้นทางลง/ขึ้น
    steps = ["1 เรียก save()", "2 open()/write()", "3 system call", "4 สั่งไดรเวอร์", "5 คำสั่ง NVMe", "6 เขียนลง flash"]
    xd, xu = 7.7, 11.9
    for i, s in enumerate(steps):
        y0 = top - (i + 1) * rh + rh / 2
        y1 = y0 - rh
        arrow(ax, (xd, y0 - 0.05), (xd, y1 + 0.05), color=BLUE, lw=1.8)
        ax.text(xd + 0.15, (y0 + y1) / 2, s, ha="left", va="center", fontsize=9.5, color=BLUE)
    yb = top - n * rh + rh / 2
    yt = top - rh / 2
    arrow(ax, (xu, yb), (xu, yt), color=AQUA, lw=1.8, ls="--")
    ax.text(xu + 0.12, (yb + yt) / 2, "ผลลัพธ์\n\"บันทึกแล้ว\"\nย้อนกลับขึ้น", va="center", fontsize=9.5, color=AQUA)
    ax.plot([xd, xu], [yb, yb], color=MUTED, lw=1.2, ls=":")
    ax.set_xlim(0, 13.8)
    save(fig, "w02-layers")


# ---------------------------------------------------------------- 2. memory hierarchy + latency
def human(sec):
    """แปลงวินาทีเป็นหน่วยเวลาที่คนเข้าใจ"""
    for unit, s in [("ปี", 365 * 86400), ("เดือน", 30 * 86400), ("วัน", 86400), ("ชม.", 3600), ("นาที", 60)]:
        if sec >= s:
            return f"≈ {sec / s:.1f} {unit}".replace(".0 ", " ")
    return f"≈ {sec:g} วินาที"


def memory_latency():
    levels = [  # (ชื่อ, latency ns โดยประมาณ, ความจุทั่วไป)
        ("Register", 0.3, "ไม่กี่ร้อยไบต์"),
        ("L1 cache", 1, "32–64 KB/คอร์"),
        ("L2 cache", 4, "0.5–2 MB/คอร์"),
        ("L3 cache", 15, "8–64 MB"),
        ("RAM (DRAM)", 100, "8–64 GB"),
        ("SSD (NVMe)", 100_000, "0.5–4 TB"),
        ("HDD", 10_000_000, "1–20 TB"),
    ]
    cols = [VIOLET, BLUE, BLUE, BLUE, AQUA, YELLOW, ORANGE]
    fig, ax = plt.subplots(figsize=(10.4, 5.2))
    ys = np.arange(len(levels))[::-1]
    for y, (name, ns, cap), c in zip(ys, levels, cols):
        ax.barh(y, ns, color=c, height=0.62, left=0.1)
        ax.text(ns * 1.4, y, (f"{ns:,.0f}" if ns >= 1 else f"{ns:g}") + f" ns   (ถ้า 1 ns = 1 วินาที → {human(ns)})", va="center", fontsize=10, color=INK)
        ax.text(0.06, y, f"{name}\n{cap}", va="center", ha="right", fontsize=10, color=INK2, linespacing=1.1)
    ax.set_xscale("log"); ax.set_xlim(0.1, 1e12)
    ax.set_yticks([]); ax.spines["left"].set_visible(False)
    ax.set_xticks([1, 1e3, 1e6, 1e9]); ax.set_xticklabels(["1 ns", "1 µs", "1 ms", "1 s"])
    ax.xaxis.grid(True, color=GRID, lw=0.8); ax.set_axisbelow(True)
    ratio = levels[4][1] / levels[1][1]
    ax.set_title(f"ลำดับชั้นหน่วยความจำ: ยิ่งลงล่างยิ่งใหญ่และถูก แต่ช้าลงหลายเท่า (RAM ช้ากว่า L1 ≈ {ratio:.0f} เท่า)",
                 loc="left", fontsize=12, fontweight="bold", x=-0.17)
    ax.text(1.0, -0.13, "ค่า latency เป็นลำดับขนาดโดยประมาณ แกนนอนเป็น log scale", ha="right", fontsize=9.5, color=MUTED, transform=ax.transAxes)
    save(fig, "w02-memory-latency")


# ---------------------------------------------------------------- 3. CPU vs GPU vs NPU
def cpu_gpu_npu():
    fig, ax = canvas(10.4, 5.6, 13.2, 7.0)
    title(ax, "CPU · GPU · NPU: ออกแบบต่างกันเพราะงานต่างกัน")
    panels = [
        ("CPU", BLUE, BLUE_T, "คอร์ใหญ่ไม่กี่คอร์ + cache ใหญ่", "งานทั่วไป ลำดับซับซ้อน\nif/else เยอะ · OS · เกมลอจิก"),
        ("GPU", AQUA, AQUA_T, "คอร์เล็กหลายพันคอร์", "งานขนานเหมือนกันจำนวนมาก\nกราฟิก · train โมเดล"),
        ("NPU", VIOLET, VIOLET_T, "อาร์เรย์ตัวคูณ-บวก (MAC)", "คูณเมทริกซ์ของ AI\ninference ประหยัดไฟบนเครื่อง"),
    ]
    pw = 4.1
    for k, (name, c, t, arch, use) in enumerate(panels):
        x0 = 0.2 + k * (pw + 0.25)
        box(ax, x0, 0.25, pw, 6.0, None, "white", c)
        box(ax, x0 + 0.15, 5.55, pw - 0.3, 0.55, name, c, c, size=12.5, weight="bold", color="white")
        gx, gy, gw, gh = x0 + 0.35, 2.45, pw - 0.7, 2.9  # พื้นที่วาดชิป
        ax.add_patch(Rectangle((gx, gy), gw, gh, facecolor=GRAY_T, edgecolor=MUTED, lw=1))
        if name == "CPU":
            for i in range(2):
                for j in range(2):
                    box(ax, gx + 0.15 + j * 1.0, gy + 1.55 - i * 1.25, 0.85, 1.05, "core", t, c, size=9.5)
            box(ax, gx + 2.25, gy + 0.3, gw - 2.4, 2.3, "cache\nใหญ่", YELLOW_T, YELLOW, size=10)
        elif name == "GPU":
            nx, ny = 12, 9
            for i in range(ny):
                for j in range(nx):
                    ax.add_patch(Rectangle((gx + 0.12 + j * (gw - 0.24) / nx, gy + 0.12 + i * (gh - 0.24) / ny),
                                           (gw - 0.24) / nx * 0.78, (gh - 0.24) / ny * 0.72, facecolor=c, edgecolor="none"))
        else:
            m = 5
            sx, sy = (gw - 0.7) / m, (gh - 0.7) / m
            for i in range(m):
                for j in range(m):
                    ax.add_patch(Rectangle((gx + 0.45 + j * sx, gy + 0.15 + i * sy), sx * 0.7, sy * 0.7, facecolor=t, edgecolor=c))
            for i in range(m):
                arrow(ax, (gx + 0.05, gy + 0.15 + i * sy + sy * 0.35), (gx + 0.42, gy + 0.15 + i * sy + sy * 0.35), color=c, lw=1)
            ax.text(gx + gw / 2 + 0.2, gy + gh - 0.18, "ข้อมูลไหลผ่านเป็นจังหวะ", ha="center", fontsize=9.5, color=c)
        ax.text(x0 + pw / 2, 2.05, arch, ha="center", va="center", fontsize=10.5, fontweight="bold", color=c)
        ax.text(x0 + pw / 2, 1.1, use, ha="center", va="center", fontsize=10, color=INK2, linespacing=1.3)
    save(fig, "w02-cpu-gpu-npu")


if __name__ == "__main__":
    layers()
    memory_latency()
    cpu_gpu_npu()
