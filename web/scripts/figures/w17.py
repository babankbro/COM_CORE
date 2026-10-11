"""Week 17 · ทบทวนและสอบปลายภาค — infographic 2 ภาพ"""
import numpy as np

from _style import *  # noqa: F401,F403


def concept_map():
    """แผนผังความคิด W9–W15 รอบกรณีศึกษา smart classroom"""
    fig, ax = canvas(12.6, 7.4, 15.0, 8.8)
    title(ax, "แผนผังความคิดครึ่งหลัง (W9–W15): ทุกสัปดาห์มาบรรจบในระบบเดียว", y=8.45)
    nodes = [
        ("W9 AI/ML", "supervised · feature/label\noverfitting · NIST AI RMF", BLUE, BLUE_T),
        ("W10 GenAI/หุ่นยนต์", "token · embedding · RAG\nhallucination · sense-plan-act", VIOLET, VIOLET_T),
        ("W11 Embedded/IoT", "sensor/actuator · MQTT\ndevice–edge–cloud · TinyML", AQUA, AQUA_T),
        ("W12 Security", "CIA · encryption · MFA\nZero Trust · OWASP", ORANGE, ORANGE_T),
        ("W13 Ethics/IP", "ACM Code · PDPA\ncopyright · license · bias", YELLOW, YELLOW_T),
        ("W14 DevOps", "SDLC · Agile · CI/CD\nMLOps · Git workflow", BLUE, GRAY_T),
        ("W15 Industry", "value chain · PUE\n6 มุมสังเกต · career", VIOLET, GRAY_T),
    ]
    cx, cy, rx, ry = 7.5, 4.05, 5.35, 3.15
    w, h = 3.3, 1.45
    centers = []
    for k in range(len(nodes)):
        ang = np.pi / 2 - k * 2 * np.pi / len(nodes)
        centers.append((cx + rx * np.cos(ang), cy + ry * np.sin(ang)))
    links = [(0, 1, "LLM = DL"), (1, 2, "Physical AI"), (2, 3, "IoT security"),
             (3, 4, "PDPA"), (4, 5, "privacy by design"), (5, 6, "DevOps/SRE"), (6, 0, "GPU data center")]
    for a, b, lab in links:
        (x1, y1), (x2, y2) = centers[a], centers[b]
        ax.plot([x1, x2], [y1, y2], color=MUTED, lw=1.3, ls="--", zorder=1)
    for (x, y) in centers:
        ax.plot([cx, x], [cy, y], color=GRID, lw=2.2, zorder=0)
    ax.add_patch(plt.Circle((cx, cy), 1.25, facecolor="white", edgecolor=INK, lw=2, zorder=2))
    ax.text(cx, cy + 0.3, "Smart classroom", ha="center", va="center", fontsize=12, fontweight="bold", zorder=3)
    ax.text(cx, cy - 0.3, "กรณีศึกษาเดียว\nวิเคราะห์ครบทุกมิติ", ha="center", va="center", fontsize=10, color=INK2, zorder=3, linespacing=1.3)
    for (name, kw, edge, fill), (x, y) in zip(nodes, centers):
        box(ax, x - w / 2, y - h / 2, w, h, "", fill, edge)
        ax.text(x, y + 0.38, name, ha="center", va="center", fontsize=11.5, fontweight="bold", color=edge, zorder=4)
        ax.text(x, y - 0.25, kw, ha="center", va="center", fontsize=10, zorder=4, linespacing=1.35)
    for a, b, lab in links:
        (x1, y1), (x2, y2) = centers[a], centers[b]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        mx, my = mx + (mx - cx) * 0.14, my + (my - cy) * 0.14
        ax.text(mx, my, lab, ha="center", va="center", fontsize=9.5, color=INK2, zorder=5,
                bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor=GRID))
    return fig


def clo_matrix():
    """สัปดาห์ W9–W15 × CLO และ CLO ที่สอบปลายภาค"""
    weeks = ["W9 AI/ML", "W10 GenAI", "W11 IoT", "W12 Security", "W13 Ethics/IP", "W14 DevOps", "W15 Industry"]
    clo_map = [[1], [1, 4], [2, 4], [1, 4], [5], [3, 6], [4, 6]]
    clos = ["CLO1\nความรู้พื้นฐาน", "CLO2\nสถาปัตยกรรม\nHW–SW", "CLO3\nอัลกอริทึม/\nโปรแกรม", "CLO4\nเทคโนโลยี\nทันสมัย",
            "CLO5\nจริยธรรม/\nกฎหมาย/IP", "CLO6\nทีม/บริหาร\nโครงการ"]
    exam = {1, 2, 4, 5}
    fig, ax = plt.subplots(figsize=(11.0, 6.0))
    ax.set_xlim(-0.5, 5.5); ax.set_ylim(len(weeks) - 0.5, -0.5)
    for j in range(6):
        if j + 1 in exam:
            ax.add_patch(Rectangle((j - 0.45, -0.48), 0.9, len(weeks) - 0.04, facecolor=YELLOW_T, edgecolor="none", zorder=0))
    for i, cl in enumerate(clo_map):
        ax.axhline(i, color=GRID, lw=0.8, zorder=1)
        for c in cl:
            col = ORANGE if c in exam else MUTED
            ax.scatter(c - 1, i, s=300, color=col, zorder=3, edgecolor="white", linewidth=1.5)
    ax.set_xticks(range(6)); ax.set_xticklabels(clos, fontsize=10)
    ax.xaxis.tick_top()
    ax.set_yticks(range(len(weeks))); ax.set_yticklabels(weeks, fontsize=10.5)
    for s in ("left", "bottom", "top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(length=0)
    ax.set_title("สัปดาห์ 9–15 กับ CLO: คอลัมน์สีเหลือง = CLO ที่สอบปลายภาค (CLO1, 2, 4, 5)",
                 loc="left", fontsize=12.5, fontweight="bold", pad=62)
    ax.scatter([], [], s=140, color=ORANGE, label="วัดในข้อสอบปลายภาค")
    ax.scatter([], [], s=140, color=MUTED, label="วัดจากงานอื่น (โครงงาน/รายงานดูงาน)")
    ax.legend(loc="lower center", bbox_to_anchor=(0.45, -0.13), ncol=2, frameon=False, fontsize=10.5)
    return fig


if __name__ == "__main__":
    save(concept_map(), "w17-concept-map")
    save(clo_matrix(), "w17-clo-matrix")
