"""Week 15 · การดูงานเชิงวิชาการและอุตสาหกรรมคอมพิวเตอร์ — infographic 3 ภาพ"""
from _style import *  # noqa: F401,F403


def value_chain():
    """ห่วงโซ่คุณค่าอุตสาหกรรมคอมพิวเตอร์ 5 ชั้น"""
    fig, ax = canvas(12.6, 6.4, 15.0, 7.6)
    title(ax, "ห่วงโซ่คุณค่าอุตสาหกรรมคอมพิวเตอร์: ทุกแอปตั้งอยู่บน 5 ชั้นนี้")
    layers = [
        ("Services / Apps", "e-commerce, fintech, สมาร์ตฟาร์ม", "DevOps/SRE, security", "W12 · W14", ORANGE, ORANGE_T),
        ("Software / Platform", "OS, database, platform, AI model", "software, data, ML engineer", "W04 · W05 · W09", VIOLET, VIOLET_T),
        ("Cloud / Data Center", "พื้นที่ ไฟฟ้า ระบบเย็น compute/storage", "DC operations, network/cloud", "W06 · W07", BLUE, BLUE_T),
        ("Hardware / Electronics", "PCB, PCBA, เซิร์ฟเวอร์, อุปกรณ์ IoT", "embedded, hardware engineer", "W02 · W11", AQUA, AQUA_T),
        ("Semiconductor", "ออกแบบชิป ผลิตเวเฟอร์ ประกอบ-ทดสอบ", "chip design, verification, test", "W03", YELLOW, YELLOW_T),
    ]
    heads = [("ชั้น (layer)", 0.9), ("กิจกรรมหลัก", 3.75), ("งานของวิศวกรคอมพิวเตอร์", 8.0), ("เชื่อมสัปดาห์", 11.6)]
    for txt, x in heads:
        ax.text(x, 6.6, txt, fontsize=10.5, fontweight="bold", color=INK2)
    h, gap = 1.0, 0.18
    for i, (name, act, role, wk, edge, fill) in enumerate(layers):
        y = 5.25 - i * (h + gap)
        box(ax, 0.8, y, 12.9, h, "", fill, edge)
        box(ax, 0.8, y, 2.8, h, name, edge, edge, size=10.5, weight="bold", color="white")
        ax.text(3.75, y + h / 2, act, va="center", fontsize=10.5)
        ax.text(8.0, y + h / 2, role, va="center", fontsize=10.5)
        ax.text(11.6, y + h / 2, wk, va="center", fontsize=10.5, fontweight="bold", color=edge)
    arrow(ax, (0.4, 0.55), (0.4, 6.2), color=INK2, lw=2)
    ax.text(0.22, 3.4, "คุณค่าส่งต่อขึ้นไปถึงผู้ใช้", rotation=90, ha="center", va="center", fontsize=10, color=INK2)
    ax.text(14.3, 0.2, "ไทยเด่นชั้น Hardware/Electronics (เช่น PCBA) และกำลังขยายชั้น Data Center/Cloud",
            ha="right", fontsize=10, color=INK2)
    return fig


def observation_lenses():
    """กรอบสังเกต 6 มุมระหว่างดูงาน → หลักฐาน"""
    fig, ax = canvas(12.6, 6.6, 15.0, 7.8)
    title(ax, "กรอบสังเกต 6 มุม: จดสิ่งที่เห็นเป็นหลักฐาน แล้วโยงกลับหัวข้อรายวิชา")
    lenses = [
        ("Hardware", "ใช้อุปกรณ์อะไร?", "rack, server, GPU, ระบบเย็น", "W02 · W03 · W07", BLUE, BLUE_T),
        ("Software", "อะไรควบคุม/จัดการระบบ?", "virtualization, orchestration", "W04 · W07 · W14", VIOLET, VIOLET_T),
        ("Data", "เก็บ สำรอง เข้ารหัสอย่างไร?", "replication, backup, encryption", "W05 · W12", AQUA, AQUA_T),
        ("Network", "เชื่อมต่อภายใน/ภายนอกอย่างไร?", "fiber, switch, firewall", "W06 · W11", YELLOW, YELLOW_T),
        ("Security", "ป้องกันกายภาพ + ไซเบอร์?", "บัตร/biometric, CCTV, MFA", "W12 · W13", ORANGE, ORANGE_T),
        ("People / Process", "ใครทำ ทำงานอย่างไร?", "ทีม 24/7, ticket, change process", "W14 · W15", INK2, GRAY_T),
    ]
    cx, cy = 7.5, 3.55
    ax.add_patch(plt.Circle((cx, cy), 1.45, facecolor=GRAY_T, edgecolor=INK2, lw=1.8))
    ax.text(cx, cy + 0.45, "Site visit", ha="center", va="center", fontsize=13, fontweight="bold")
    ax.text(cx, cy - 0.25, "สังเกต → หลักฐาน\n→ เชื่อม CLO", ha="center", va="center", fontsize=10.5, color=INK2, linespacing=1.4)
    w, h = 4.6, 1.75
    spots = [(0.3, 5.0), (0.3, 2.7), (0.3, 0.4), (10.1, 5.0), (10.1, 2.7), (10.1, 0.4)]
    for (name, q, ev, wk, edge, fill), (x, y) in zip(lenses, spots):
        box(ax, x, y, w, h, "", fill, edge)
        ax.text(x + 0.2, y + h - 0.35, name, fontsize=12, fontweight="bold", color=edge, va="center")
        ax.text(x + w - 0.2, y + h - 0.35, wk, fontsize=10, color=edge, va="center", ha="right", fontweight="bold")
        ax.text(x + 0.2, y + 0.85, "ถาม: " + q, fontsize=10.5, va="center")
        ax.text(x + 0.2, y + 0.38, "หลักฐาน: " + ev, fontsize=10.5, va="center", color=INK2)
        side = x + w if x < cx else x
        arrow(ax, (side + (0.05 if x < cx else -0.05), y + h / 2), (cx + (-1.5 if x < cx else 1.5) * 0.92, cy + (y + h / 2 - cy) * 0.35),
              color=edge, style="-", lw=1.4)
    return fig


def career_roles():
    """บทบาทอาชีพ × สัปดาห์ที่เกี่ยวข้อง"""
    weeks = ["W02", "W03", "W05", "W06", "W07", "W09", "W10", "W11", "W12", "W14"]
    roles = [
        ("Embedded Engineer", ["W02", "W03", "W11"], AQUA),
        ("IoT Engineer", ["W06", "W11"], AQUA),
        ("Hardware / Chip Design", ["W03"], AQUA),
        ("Network Engineer", ["W06"], BLUE),
        ("Cloud Engineer", ["W07"], BLUE),
        ("DC Operations Engineer", ["W07"], BLUE),
        ("DevOps / SRE", ["W14"], VIOLET),
        ("Data Engineer", ["W05"], VIOLET),
        ("ML Engineer", ["W09", "W10", "W14"], VIOLET),
        ("Security Engineer", ["W12"], ORANGE),
    ]
    fig, ax = plt.subplots(figsize=(11.6, 6.0))
    ax.set_xlim(-0.6, len(weeks) - 0.4); ax.set_ylim(len(roles) - 0.4, -1.1)
    for j in range(len(weeks)):
        ax.axvline(j, color=GRID, lw=0.8, zorder=0)
    for i, (role, ws, col) in enumerate(roles):
        ax.axhline(i, color=GRID, lw=0.8, zorder=0)
        for w in ws:
            ax.scatter(weeks.index(w), i, s=260, color=col, zorder=3, edgecolor="white", linewidth=1.5)
    ax.set_xticks(range(len(weeks))); ax.set_xticklabels(weeks, fontsize=10.5)
    ax.xaxis.tick_top()
    ax.set_yticks(range(len(roles))); ax.set_yticklabels([r[0] for r in roles], fontsize=10.5)
    for s in ("left", "bottom", "top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(length=0)
    ax.set_title("บทบาทอาชีพวิศวกรคอมพิวเตอร์ กับสัปดาห์ที่ใช้ความรู้นั้น", loc="left", fontsize=12.5, fontweight="bold", pad=34)
    for k, (lab, col) in enumerate([("ฮาร์ดแวร์/ฝังตัว", AQUA), ("โครงสร้างพื้นฐาน", BLUE), ("ซอฟต์แวร์/ข้อมูล/AI", VIOLET), ("ความปลอดภัย", ORANGE)]):
        ax.scatter([], [], s=120, color=col, label=lab)
    ax.legend(loc="lower center", bbox_to_anchor=(0.45, -0.13), ncol=4, frameon=False, fontsize=10.5)
    return fig


if __name__ == "__main__":
    save(value_chain(), "w15-value-chain")
    save(observation_lenses(), "w15-observation-lenses")
    save(career_roles(), "w15-career-roles")
