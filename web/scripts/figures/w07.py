"""Infographic สัปดาห์ที่ 7: ศูนย์ข้อมูลและโครงสร้างพื้นฐานระดับคลาวด์
1) w07-vm-vs-container   ชั้นซอฟต์แวร์ของ VM เทียบ Container
2) w07-responsibility    ตาราง Shared Responsibility: On-prem / IaaS / PaaS / SaaS
3) w07-pue-bars          แท่งซ้อน IT + Non-IT ที่ PUE ต่าง ๆ (IT คงที่ 1,000 kW)
"""
from _style import *  # noqa: F401,F403


# ---------------------------------------------------------------- 1
def vm_vs_container():
    fig, ax = canvas(11.2, 5.0, xlim=14, ylim=6.4)
    title(ax, "VM จำลองทั้งเครื่อง (มี Guest OS ของตัวเอง) · Container แชร์ kernel ของ Host OS", y=6.05)

    def stack(x0, heading, layers, apps, guest, note, c):
        W = 6.2
        ax.text(x0 + W / 2, 5.2, heading, ha="center", fontsize=12, fontweight="bold", color=c)
        y = 0.9
        for name, fill, edge in layers:
            box(ax, x0, y, W, 0.7, name, fill, edge, size=10.5)
            y += 0.8
        bw, gap = (W - 0.3) / 3, 0.15
        for i in range(3):
            bx = x0 + i * (bw + gap)
            yy = y
            if guest:
                box(ax, bx, yy, bw, 0.7, "Guest OS", ORANGE_T, ORANGE, size=10)
                yy += 0.8
            box(ax, bx, yy, bw, 0.7, "Bins/Libs", YELLOW_T, YELLOW, size=10)
            yy += 0.8
            box(ax, bx, yy, bw, 0.7, apps[i], BLUE_T, BLUE, size=10, weight="bold")
        ax.text(x0 + W / 2, 0.3, note, ha="center", fontsize=10, color=INK2)

    stack(0.3, "Virtual Machine (VM)",
          [("Hardware (CPU · RAM · Disk · NIC)", GRAY_T, MUTED),
           ("Hypervisor (เช่น KVM, VMware ESXi)", VIOLET_T, VIOLET)],
          ["App A", "App B", "App C"], True,
          "แยกขาดสูง · ขนาดระดับ GB · บูตระดับนาที", VIOLET)
    stack(7.5, "Container",
          [("Hardware (CPU · RAM · Disk · NIC)", GRAY_T, MUTED),
           ("Host OS + Linux kernel (ใช้ร่วมกัน)", AQUA_T, AQUA),
           ("Container Engine (Docker / containerd)", VIOLET_T, VIOLET)],
          ["App A", "App B", "App C"], False,
          "เบา · ขนาดระดับ MB · เริ่มระดับวินาที", AQUA)
    ax.plot([7.1, 7.1], [0.6, 5.5], color=GRID, lw=1.5)
    save(fig, "w07-vm-vs-container")


# ---------------------------------------------------------------- 2
def responsibility():
    layers = ["ข้อมูลและสิทธิ์ผู้ใช้", "แอปพลิเคชัน", "Runtime / Middleware", "ระบบปฏิบัติการ (OS)",
              "Virtualization", "Server · Storage · Network", "อาคาร · ไฟฟ้า · ความเย็น"]
    # จำนวนชั้นบนสุดที่ "ผู้ใช้" ดูแล (ตามตารางในหัวข้อที่ 3)
    models = [("On-premises", 7), ("IaaS", 4), ("PaaS", 2), ("SaaS", 1)]
    fig, ax = canvas(11.0, 6.0, xlim=13, ylim=7.6)
    title(ax, "ใครดูแลชั้นใด? ยิ่งขยับไปทาง SaaS ผู้ให้บริการยิ่งรับไปมาก", y=7.25)
    x0, cw, rh, y0 = 3.6, 2.25, 0.72, 0.9
    for j, (m, n_user) in enumerate(models):
        x = x0 + j * cw
        ax.text(x + cw / 2, y0 + rh * 7 + 0.25, m, ha="center", fontsize=11.5, fontweight="bold")
        for i, layer in enumerate(layers):
            y = y0 + rh * (6 - i)
            user = i < n_user
            ax.add_patch(Rectangle((x + 0.05, y + 0.04), cw - 0.1, rh - 0.08,
                                   facecolor=BLUE if user else ORANGE_T, edgecolor="white"))
            ax.text(x + cw / 2, y + rh / 2, "ผู้ใช้" if user else "ผู้ให้บริการ", ha="center", va="center",
                    fontsize=10, color="white" if user else ORANGE, fontweight="bold" if user else "normal")
        ax.text(x + cw / 2, y0 - 0.35, f"ผู้ใช้ดูแล {n_user}/{len(layers)} ชั้น", ha="center",
                fontsize=10, color=INK2)
    for i, layer in enumerate(layers):
        ax.text(x0 - 0.15, y0 + rh * (6 - i) + rh / 2, layer, ha="right", va="center", fontsize=10.5)
    save(fig, "w07-responsibility")


# ---------------------------------------------------------------- 3
def pue_bars():
    it = 1000  # kW
    pues = [2.0, 1.8, 1.5, 1.2, 1.05]
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    ygrid(ax)
    xs = range(len(pues))
    totals = [p * it for p in pues]
    non_it = [t - it for t in totals]
    ax.bar(xs, [it] * len(pues), color=BLUE, width=0.55, label="IT (เซิร์ฟเวอร์ · storage · network)")
    ax.bar(xs, non_it, bottom=[it] * len(pues), color=ORANGE, width=0.55, label="Non-IT (ความเย็น · UPS · แสงสว่าง)")
    for x, p, t, n in zip(xs, pues, totals, non_it):
        ax.text(x, t + 30, f"รวม {t:,.0f} kW\nDCiE {100 / p:.0f}%", ha="center", va="bottom", fontsize=10)
        if n >= 120:
            ax.text(x, it + n / 2, f"{n:,.0f}", ha="center", va="center", color="white", fontsize=10.5,
                    fontweight="bold")
        else:
            ax.text(x + 0.33, it + n / 2, f"{n:,.0f}", ha="left", va="center", color=ORANGE, fontsize=10.5,
                    fontweight="bold")
        ax.text(x, it / 2, f"{it:,}", ha="center", va="center", color="white", fontsize=10.5)
    ax.set_xticks(list(xs))
    ax.set_xticklabels([f"PUE {p:g}" for p in pues], fontsize=11)
    ax.set_ylabel("กำลังไฟฟ้า (kW)")
    ax.set_ylim(0, max(totals) * 1.22)
    ax.set_title("IT เท่ากันที่ 1,000 kW · Non-IT = (PUE − 1) × IT · PUE ยิ่งใกล้ 1 ยิ่งดี",
                 fontsize=12.5, fontweight="bold", loc="left")
    ax.legend(frameon=False, fontsize=10, loc="upper right")
    save(fig, "w07-pue-bars")


if __name__ == "__main__":
    vm_vs_container()
    responsibility()
    pue_bars()
