"""Infographic สัปดาห์ที่ 1: ภาพรวมวิศวกรรมคอมพิวเตอร์ (CE/CS/SE/IT/IS, CE2016, วิวัฒนาการ)
รัน: python scripts/make_week_figures.py 01
"""
from _style import *  # noqa: F401,F403


# ---------------------------------------------------------------- 1. ขอบเขต 5 สาขา
def disciplines():
    """ตารางเชิงแนวคิด: แต่ละสาขาเน้นชั้นใดของระบบ (ดัดแปลงแนวคิดจาก ACM CC2005)"""
    layers = [  # บนลงล่าง: องค์กร -> วงจร
        "องค์กร & กระบวนการธุรกิจ",
        "บริการ & โครงสร้างพื้นฐานไอที",
        "ซอฟต์แวร์ประยุกต์ & กระบวนการพัฒนา",
        "อัลกอริทึม & ทฤษฎีการคำนวณ",
        "OS · ระบบฝังตัว · เครือข่าย",
        "สถาปัตยกรรม & ฮาร์ดแวร์ดิจิทัล",
        "วงจร & อิเล็กทรอนิกส์",
    ]
    fields = ["CE", "CS", "SE", "IT", "IS"]
    # 2 = แกนหลัก, 1 = เกี่ยวข้อง, 0 = น้อย
    level = [
        [0, 0, 1, 1, 2],
        [1, 0, 1, 2, 1],
        [1, 1, 2, 1, 1],
        [1, 2, 1, 0, 0],
        [2, 1, 1, 1, 0],
        [2, 1, 0, 0, 0],
        [2, 0, 0, 0, 0],
    ]
    colors = [BLUE, VIOLET, AQUA, ORANGE, YELLOW]
    tints = [BLUE_T, VIOLET_T, AQUA_T, ORANGE_T, YELLOW_T]
    n = len(layers)
    x0, cw, rh = 4.6, 1.55, 0.62
    fig, ax = canvas(10.4, 6.3, 13, n * rh + 2.2)
    title(ax, "แต่ละสาขาคอมพิวเตอร์ \"ยืน\" อยู่ชั้นไหนของระบบ")
    top = n * rh + 0.75
    for j, f in enumerate(fields):
        box(ax, x0 + j * cw + 0.06, top, cw - 0.12, 0.5, f, colors[j], colors[j], size=12, weight="bold", color="white")
    for i, name in enumerate(layers):
        y = top - (i + 1) * rh
        ax.text(x0 - 0.15, y + rh / 2 - 0.03, name, ha="right", va="center", fontsize=10.5, color=INK2)
        for j in range(len(fields)):
            lv = level[i][j]
            fill = colors[j] if lv == 2 else tints[j] if lv == 1 else GRAY_T
            ax.add_patch(Rectangle((x0 + j * cw + 0.06, y + 0.05), cw - 0.12, rh - 0.1, facecolor=fill, edgecolor="white"))
            if lv == 2:
                ax.text(x0 + j * cw + cw / 2, y + rh / 2 - 0.03, "แกนหลัก", ha="center", va="center", fontsize=9.5, color="white")
    # ลูกศรบอกทิศทางชั้น
    ax.annotate("", xy=(12.6, top - 0.1), xytext=(12.6, top - n * rh + 0.1),
                arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=1.5))
    ax.text(12.75, top - 0.2, "ใกล้คน/องค์กร", fontsize=9.5, color=INK2, va="top")
    ax.text(12.75, top - n * rh + 0.2, "ใกล้ฟิสิกส์", fontsize=9.5, color=INK2, va="bottom")
    ly = 0.2
    for k, (fill, lab) in enumerate([(BLUE, "แกนหลัก"), (BLUE_T, "เกี่ยวข้อง"), (GRAY_T, "แตะน้อย")]):
        ax.add_patch(Rectangle((x0 + k * 2.4, ly), 0.4, 0.3, facecolor=fill, edgecolor=MUTED, lw=0.6))
        ax.text(x0 + k * 2.4 + 0.5, ly + 0.15, lab, va="center", fontsize=10)
    ax.text(0.1, ly + 0.15, "ภาพเชิงแนวคิด (ไม่ใช่ข้อกำหนด)", fontsize=9.5, color=MUTED, va="center")
    ax.set_xlim(0, 14.2)
    save(fig, "w01-disciplines")


# ---------------------------------------------------------------- 2. ชั่วโมงแกน CE2016
def ce2016_hours():
    ka = [  # (รหัส, ชื่อไทย, core hours ตาม CE2016)
        ("CAO", "สถาปัตยกรรมและการจัดองค์กรคอมพิวเตอร์", 60),
        ("CAE", "วงจรและอิเล็กทรอนิกส์", 50),
        ("DIG", "การออกแบบดิจิทัล", 50),
        ("SWD", "การออกแบบซอฟต์แวร์", 45),
        ("ESY", "ระบบฝังตัว", 40),
        ("SPE", "วิศวกรรมระบบและโครงงาน", 35),
        ("CAL", "อัลกอริทึมเชิงคำนวณ", 30),
        ("SGP", "การประมวลผลสัญญาณ", 30),
        ("NWK", "เครือข่ายคอมพิวเตอร์", 20),
        ("PPP", "การเตรียมสู่วิชาชีพ", 20),
        ("SEC", "ความมั่นคงสารสนเทศ", 20),
        ("SRM", "การจัดการทรัพยากรระบบ", 20),
    ]
    hw = {"CAO", "CAE", "DIG", "ESY", "SGP"}
    total = sum(h for _, _, h in ka)
    hw_total = sum(h for c, _, h in ka if c in hw)
    fig, ax = plt.subplots(figsize=(10.4, 5.6))
    ys = list(range(len(ka)))[::-1]
    for y, (code, th, h) in zip(ys, ka):
        c = BLUE if code in hw else AQUA
        ax.barh(y, h, color=c, height=0.66)
        ax.text(h + 0.8, y, f"{h}", va="center", fontsize=10.5, color=INK)
        ax.text(-1.2, y, f"CE-{code}  {th}", va="center", ha="right", fontsize=10.5, color=INK2)
    ax.set_yticks([]); ax.set_xlim(0, 72)
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("ชั่วโมงแกน (core hours) ขั้นต่ำ", fontsize=10.5)
    ax.xaxis.grid(True, color=GRID, lw=0.8); ax.set_axisbelow(True)
    ax.set_title(f"CE2016: 12 knowledge areas รวม {total} ชั่วโมงแกน", loc="left", fontsize=12.5, fontweight="bold", x=-0.62)
    ax.text(36, 1.6, f"ฝั่งฮาร์ดแวร์/สัญญาณ {hw_total} ชม. ({hw_total / total:.0%})", color=BLUE, fontsize=10.5)
    ax.text(36, 0.6, f"ฝั่งซอฟต์แวร์/ระบบ/วิชาชีพ {total - hw_total} ชม. ({(total - hw_total) / total:.0%})", color=AQUA, fontsize=10.5)
    save(fig, "w01-ce2016-hours")


# ---------------------------------------------------------------- 3. เส้นเวลาวิวัฒนาการ
def timeline():
    ev = [  # (ปี, หัวข้อ, รายละเอียด, ยุค)
        (1946, "ENIAC", "หลอดสุญญากาศ\n~18,000 ดวง", 0),
        (1947, "ทรานซิสเตอร์", "Bell Labs", 1),
        (1958, "วงจรรวม IC", "รวมวงจร\nบนชิปเดียว", 2),
        (1971, "Intel 4004", "CPU บนชิปเดียว\n2,300 ตัว", 2),
        (1981, "IBM PC", "คอมพิวเตอร์\nส่วนบุคคล", 2),
        (2007, "สมาร์ตโฟน", "SoC + มือถือ\n+ อินเทอร์เน็ต", 3),
        (2016, "Google TPU", "ชิปเร่ง AI\nใน data center", 3),
        (2017, "NPU ในมือถือ", "on-device AI", 3),
        (2022, "ChatGPT", "LLM สู่ผู้ใช้ทั่วไป", 4),
        (2025, "Agentic AI", "AI วางแผน\nและลงมือทำเอง", 4),
    ]
    era = [("หลอดสุญญากาศ", ORANGE, ORANGE_T), ("ทรานซิสเตอร์", YELLOW, YELLOW_T),
           ("IC/ไมโครโปรเซสเซอร์", BLUE, BLUE_T), ("มือถือ & ตัวเร่ง AI", AQUA, AQUA_T),
           ("Generative/Agentic AI", VIOLET, VIOLET_T)]
    fig, ax = canvas(13.6, 5.0, len(ev) * 1.65 + 0.4, 6.4)
    title(ax, "วิวัฒนาการ: จากห้องเครื่องคำนวณสู่ AI ที่ลงมือทำเอง (ระยะห่างไม่เป็นสัดส่วนเวลา)")
    yl = 3.0
    ax.plot([0.3, len(ev) * 1.65 + 0.1], [yl, yl], color=MUTED, lw=2, zorder=1)
    for i, (yr, head, sub, e) in enumerate(ev):
        x = 1.05 + i * 1.65
        c, t = era[e][1], era[e][2]
        ax.scatter([x], [yl], s=110, color=c, zorder=3, edgecolor="white", linewidth=1.5)
        up = i % 2 == 0
        y1 = yl + (0.55 if up else -0.55)
        ax.plot([x, x], [yl, y1], color=c, lw=1.2)
        ax.text(x, yl + (0.25 if up else -0.25) * -1, str(yr), ha="center", va="center",
                fontsize=10, color=INK2, fontweight="bold")
        by = y1 + (0.05 if up else -1.55)
        box(ax, x - 0.78, by, 1.56, 1.5, None, t, c)
        ax.text(x, by + 1.2, head, ha="center", va="center", fontsize=10, fontweight="bold")
        ax.text(x, by + 0.55, sub, ha="center", va="center", fontsize=9.5, color=INK2, linespacing=1.15)
    for k, (name, c, t) in enumerate(era):
        ax.add_patch(Rectangle((0.3 + k * 3.3, 0.08), 0.35, 0.28, facecolor=c, edgecolor=c))
        ax.text(0.75 + k * 3.3, 0.22, name, va="center", fontsize=9.5)
    save(fig, "w01-timeline")


if __name__ == "__main__":
    disciplines()
    ce2016_hours()
    timeline()
