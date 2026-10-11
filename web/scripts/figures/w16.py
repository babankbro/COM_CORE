"""Week 16 · นำเสนอโครงงานประยุกต์ — infographic 2 ภาพ"""
from _style import *  # noqa: F401,F403


def storyline():
    """โครงเรื่องนำเสนอ 10 นาทีแบบ Gantt + หลักฐานที่ต้องโชว์"""
    segs = [
        ("1 Problem", 1.0, "ภาพ/ตัวเลขของปัญหาจริง", BLUE),
        ("2 Users & requirement", 1.0, "user story + acceptance criteria", BLUE),
        ("3 Architecture", 1.5, "diagram HW · SW · data · network · security", VIOLET),
        ("4 Key implementation", 1.5, "โค้ด/วงจรสำคัญ 1–2 จุด + commit history", AQUA),
        ("5 Live demo", 2.0, "demo สด + วิดีโอสำรอง (fallback)", AQUA),
        ("6 Testing & result", 1.5, "ตาราง test, accuracy, latency", ORANGE),
        ("7 Limitation", 0.75, "ข้อจำกัด ความเสี่ยง PDPA/bias", ORANGE),
        ("8 Next step", 0.75, "สิ่งที่จะทำต่อ + สรุป 1 ประโยค", ORANGE),
    ]
    fig, ax = plt.subplots(figsize=(12.0, 5.6))
    t = 0.0
    for i, (name, dur, ev, col) in enumerate(segs):
        ax.barh(i, dur, left=t, height=0.62, color=col, edgecolor="white", linewidth=1.5)
        ax.text(t + dur + 0.12, i, ev, va="center", fontsize=10.5, color=INK2)
        ax.text(t + dur / 2, i, f"{dur:g}", va="center", ha="center", fontsize=10, color="white", fontweight="bold")
        t += dur
    ax.set_yticks(range(len(segs))); ax.set_yticklabels([s[0] for s in segs], fontsize=10.5)
    ax.invert_yaxis()
    ax.set_xlim(0, 15.2); ax.set_xticks(range(0, 11)); ax.set_xlabel("นาที (รวม 10 นาที แล้วต่อด้วย Q&A)", fontsize=10.5)
    ax.xaxis.grid(True, color=GRID, linewidth=0.8); ax.set_axisbelow(True)
    ax.spines["left"].set_visible(False); ax.tick_params(axis="y", length=0)
    ax.set_title("โครงเรื่องนำเสนอโครงงาน 10 นาที: แต่ละช่วงต้องมีหลักฐานอะไร", loc="left", fontsize=12.5, fontweight="bold")
    handles = [Rectangle((0, 0), 1, 1, color=c) for c in (BLUE, VIOLET, AQUA, ORANGE)]
    ax.legend(handles, ["requirement evidence", "architecture evidence", "implementation evidence", "evaluation evidence"],
              loc="upper center", bbox_to_anchor=(0.45, -0.16), ncol=4, frameon=False, fontsize=10)
    return fig


def qa_framework():
    """สูตรตอบคำถาม 5 ขั้น + กรณีไม่รู้คำตอบ"""
    fig, ax = canvas(12.4, 4.6, 15.0, 5.6)
    title(ax, "ตอบคำถามกรรมการแบบมืออาชีพ: 5 ขั้นใน 60–90 วินาที")
    steps = [
        ("1 ฟังให้จบ", "จดคีย์เวิร์ด\nไม่ขัดจังหวะ", BLUE, BLUE_T),
        ("2 ทวนคำถาม", "\"ถามเรื่อง ... ใช่ไหมครับ\"\nกันตอบผิดประเด็น", VIOLET, VIOLET_T),
        ("3 ตอบตรง 1 ประโยค", "ให้คำตอบก่อน\nแล้วค่อยขยาย", AQUA, AQUA_T),
        ("4 ยกหลักฐาน", "ชี้สไลด์/log/ตัวเลข\nหรือ commit จริง", YELLOW, YELLOW_T),
        ("5 ข้อจำกัด + ทางต่อ", "trade-off ที่เลือก\nและแผนปรับปรุง", ORANGE, ORANGE_T),
    ]
    w, h, gap = 2.65, 2.2, 0.32
    for i, (head, body, edge, fill) in enumerate(steps):
        x = 0.3 + i * (w + gap)
        box(ax, x, 2.1, w, h, "", fill, edge)
        ax.text(x + w / 2, 2.1 + h - 0.42, head, ha="center", va="center", fontsize=11.5, fontweight="bold", color=edge)
        ax.text(x + w / 2, 2.1 + 0.8, body, ha="center", va="center", fontsize=10.5, linespacing=1.45)
        if i < len(steps) - 1:
            arrow(ax, (x + w + 0.03, 2.1 + h / 2), (x + w + gap - 0.03, 2.1 + h / 2))
    box(ax, 0.3, 0.35, 14.5, 1.3, "", GRAY_T, MUTED)
    ax.text(0.6, 1.0, "ถ้าไม่รู้คำตอบ: ยอมรับตรง ๆ → บอกว่าจะหาคำตอบอย่างไร (ทดลอง/อ่านเอกสาร) → เสนอส่งคำตอบภายหลัง\n"
            "ห้ามเดา · ห้ามโยนให้เพื่อนโดยไม่ทวน · ทุกคนในทีมต้องอธิบายส่วนของตัวเองได้ (rubric: การทำงานเป็นทีม + การตอบคำถาม)",
            va="center", fontsize=10.5, linespacing=1.6)
    return fig


if __name__ == "__main__":
    save(storyline(), "w16-storyline")
    save(qa_framework(), "w16-qa-framework")
