"""Week 14 · โครงงานประยุกต์และวิศวกรรมระบบ DevOps — infographic 3 ภาพ"""
import numpy as np

from _style import *  # noqa: F401,F403


def sdlc_vs_agile():
    """Waterfall (SDLC แบบลำดับขั้น) เทียบกับวงรอบ Sprint ของ Agile"""
    fig, ax = canvas(12.4, 6.0, 15.0, 7.2)
    title(ax, "SDLC แบบ Waterfall เทียบกับ Agile: ส่งมอบครั้งเดียวตอนท้าย vs ส่งมอบทุกวงรอบ")
    # ---- ซ้าย: Waterfall
    ax.text(0.3, 6.25, "Waterfall", fontsize=12.5, fontweight="bold", color=BLUE)
    phases = ["วิเคราะห์ requirement", "ออกแบบ", "พัฒนา", "ทดสอบ", "นำไปใช้", "บำรุงรักษา"]
    w, h = 2.6, 0.62
    for i, p in enumerate(phases):
        x, y = 0.3 + i * 0.85, 5.35 - i * 0.82
        box(ax, x, y, w, h, p, BLUE_T, BLUE, size=10.5)
        if i < len(phases) - 1:
            arrow(ax, (x + w - 0.3, y - 0.02), (x + w - 0.3, y - 0.18), color=BLUE)
    ax.text(0.3, 0.55, "เหมาะเมื่อ requirement นิ่ง เช่น ระบบที่มีมาตรฐานกำกับ\nเปลี่ยนกลางทางมีต้นทุนสูง · ผู้ใช้เห็นงานตอนท้าย",
            fontsize=10, color=INK2, linespacing=1.5)
    ax.plot([7.55, 7.55], [0.4, 6.4], color=GRID, lw=1.5)
    # ---- ขวา: Agile sprint loop
    ax.text(7.9, 6.25, "Agile (Scrum)", fontsize=12.5, fontweight="bold", color=AQUA)
    box(ax, 7.9, 4.6, 2.0, 1.2, "Product\nbacklog", YELLOW_T, YELLOW, size=10.5, weight="bold")
    cx, cy, r = 12.15, 3.7, 1.75
    t = np.linspace(0, 2 * np.pi, 200)
    ax.plot(cx + r * np.cos(t), cy + r * np.sin(t), color=AQUA, lw=2.2)
    for ang in (45, 135, 225, 315):
        a = np.radians(ang)
        ax.annotate("", xy=(cx + r * np.cos(a + 0.12), cy + r * np.sin(a + 0.12)),
                    xytext=(cx + r * np.cos(a), cy + r * np.sin(a)),
                    arrowprops=dict(arrowstyle="-|>", color=AQUA, lw=2, mutation_scale=16))
    stages = [(90, "Sprint planning"), (180, "Build + test"), (270, "Review / demo"), (0, "Retrospective")]
    for ang, lab in stages:
        a = np.radians(ang)
        bx, by = cx + r * np.cos(a), cy + r * np.sin(a)
        box(ax, bx - 0.95, by - 0.3, 1.9, 0.6, lab, AQUA_T, AQUA, size=10)
    ax.text(cx, cy + 0.2, "Sprint", ha="center", fontsize=12, fontweight="bold", color=AQUA)
    ax.text(cx, cy - 0.35, "1–4 สัปดาห์", ha="center", fontsize=10, color=INK2)
    arrow(ax, (9.95, 5.0), (11.1, 5.25), color=YELLOW)
    box(ax, 8.1, 1.15, 2.2, 0.75, "Increment\nที่ใช้งานได้", BLUE_T, BLUE, size=10)
    arrow(ax, (10.45, 2.45), (9.6, 1.95), color=BLUE)
    ax.text(7.9, 0.55, "ส่งมอบทุก sprint · รับ feedback เร็ว · ปรับ backlog ได้ตลอด",
            fontsize=10, color=INK2)
    return fig


def cicd_pipeline():
    """CI/CD pipeline: push → build → test → artifact → staging → production → monitor"""
    fig, ax = canvas(12.6, 5.0, 15.0, 6.0)
    title(ax, "CI/CD Pipeline: ทุก commit ต้องผ่านด่านอัตโนมัติก่อนถึงผู้ใช้")
    stages = [
        ("git push\n/ PR", GRAY_T, MUTED),
        ("Build\nติดตั้ง deps", BLUE_T, BLUE),
        ("Test\nlint + unit", BLUE_T, BLUE),
        ("Artifact\nDocker image", BLUE_T, BLUE),
        ("Deploy\nstaging", AQUA_T, AQUA),
        ("Deploy\nproduction", ORANGE_T, ORANGE),
        ("Monitor\nlog · metric", VIOLET_T, VIOLET),
    ]
    w, h, gap, y = 1.75, 1.15, 0.32, 2.35
    xs = [0.3 + i * (w + gap) for i in range(len(stages))]
    for (lab, fill, edge), x in zip(stages, xs):
        box(ax, x, y, w, h, lab, fill, edge, size=10.5)
    for i in range(len(stages) - 1):
        arrow(ax, (xs[i] + w + 0.03, y + h / 2), (xs[i + 1] - 0.03, y + h / 2))
    # วงเล็บช่วง CI / CD
    def bracket(x1, x2, yb, text, color):
        ax.plot([x1, x1, x2, x2], [yb - 0.15, yb, yb, yb - 0.15], color=color, lw=2)
        ax.text((x1 + x2) / 2, yb + 0.22, text, ha="center", fontsize=10.5, fontweight="bold", color=color)
    bracket(xs[1], xs[3] + w, 3.85, "CI: integrate บ่อย ๆ + ทดสอบอัตโนมัติ", BLUE)
    bracket(xs[4], xs[5] + w, 3.85, "CD: ส่งมอบอัตโนมัติ", ORANGE)
    ax.text(xs[5] + w / 2 - 0.1, 4.75, "Delivery = กดอนุมัติก่อนขึ้น prod\nDeployment = ขึ้น prod อัตโนมัติ",
            ha="center", fontsize=10, color=INK2, linespacing=1.4)
    # เส้นทางล้มเหลว
    ax.annotate("", xy=(xs[0] + w / 2, y - 0.05), xytext=(xs[2] + w / 2, y - 0.05),
                arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.8, ls="--",
                                connectionstyle="arc3,rad=-0.45", mutation_scale=14))
    ax.text(xs[1] + w / 2, 0.4, "ไม่ผ่าน → บล็อก merge\nแจ้งผู้พัฒนาให้แก้", ha="center",
            fontsize=10, color=ORANGE, linespacing=1.4)
    ax.annotate("", xy=(xs[4] + w / 2, y - 0.05), xytext=(xs[6] + w / 2, y - 0.05),
                arrowprops=dict(arrowstyle="-|>", color=VIOLET, lw=1.8, ls="--",
                                connectionstyle="arc3,rad=-0.4", mutation_scale=14))
    ax.text(xs[5] + w / 2, 0.4, "ผิดปกติ → rollback\nเป็นเวอร์ชันก่อนหน้า", ha="center",
            fontsize=10, color=VIOLET, linespacing=1.4)
    return fig


def devops_loop():
    """DevOps infinity loop 8 ขั้น"""
    fig, ax = canvas(12.0, 6.0, 14.0, 7.0)
    title(ax, "DevOps Loop: Dev กับ Ops เป็นวงเดียวกัน ไม่ใช่ส่งงานข้ามกำแพง")
    a, cx, cy, sy = 5.6, 7.0, 4.0, 1.2
    for lo, hi, col in ((np.pi / 2, 3 * np.pi / 2, BLUE), (-np.pi / 2, np.pi / 2, ORANGE)):
        t = np.linspace(lo, hi, 300)
        den = 1 + np.sin(t) ** 2
        ax.plot(cx + a * np.cos(t) / den, cy + a * np.sin(t) * np.cos(t) / den * sy, color=col, lw=3, alpha=0.75)

    def pt(tt):
        d = 1 + np.sin(tt) ** 2
        return cx + a * np.cos(tt) / d, cy + a * np.sin(tt) * np.cos(tt) / d * sy

    for k in np.linspace(0, 2 * np.pi, 9)[:-1] + 0.25:  # หัวลูกศรบอกทิศ
        p, q = pt(k), pt(k + 0.04)
        ax.annotate("", xy=q, xytext=p, arrowprops=dict(arrowstyle="-|>", color=INK2, lw=1.2, mutation_scale=13))
    stages = [
        (0.66, "Plan", BLUE), (0.88, "Code", BLUE), (1.12, "Build", BLUE), (1.34, "Test", BLUE),
        (1.66, "Release", ORANGE), (1.88, "Deploy", ORANGE), (0.12, "Operate", ORANGE), (0.34, "Monitor", ORANGE),
    ]
    for frac, lab, col in stages:
        x, y = pt(frac * np.pi)
        fill = BLUE_T if col == BLUE else ORANGE_T
        box(ax, x - 0.72, y - 0.28, 1.44, 0.56, lab, fill, col, size=11, weight="bold")
    ax.text(cx - 3.25, cy, "Dev", ha="center", va="center", fontsize=15, fontweight="bold", color=BLUE)
    ax.text(cx + 3.25, cy, "Ops", ha="center", va="center", fontsize=15, fontweight="bold", color=ORANGE)
    ax.text(cx, 0.95, "Plan: issue/backlog · Code: Git branch + PR · Build: Docker · Test: pytest/lint",
            ha="center", fontsize=10, color=INK2)
    ax.text(cx, 0.45, "Release: tag/version · Deploy: CD · Operate: container/cloud · Monitor: log/metric/alert → กลับไป Plan",
            ha="center", fontsize=10, color=INK2)
    return fig


if __name__ == "__main__":
    save(sdlc_vs_agile(), "w14-sdlc-vs-agile")
    save(cicd_pipeline(), "w14-cicd-pipeline")
    save(devops_loop(), "w14-devops-loop")
