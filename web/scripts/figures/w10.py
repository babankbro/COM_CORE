"""Infographic สัปดาห์ที่ 10: next-token probability, RAG pipeline, agent loop vs sense-plan-act
รัน: python scripts/make_week_figures.py 10
"""
import numpy as np

from _style import *  # noqa: F401,F403


def softmax(logits, T=1.0):
    z = np.asarray(logits, dtype=float) / T
    e = np.exp(z - z.max())
    return e / e.sum()


def cosine(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))


# ------------------------------------------------------------ 1. LLM ทำนาย token ถัดไป
def next_token():
    tokens = ["ไฟฉาย", "สวิตช์", "หน้าต่าง", "ตู้เย็น"]
    logits = [2.5, 1.8, 1.0, -0.5]
    temps = [(0.5, BLUE), (1.0, VIOLET), (1.5, ORANGE)]
    fig, ax = plt.subplots(figsize=(10.4, 4.9)); ygrid(ax)
    xs = np.arange(len(tokens)); bw = 0.26
    for j, (T, col) in enumerate(temps):
        p = softmax(logits, T)
        bars = ax.bar(xs + (j - 1) * bw, p, bw * 0.92, color=col, label=f"T = {T}")
        for rect, v in zip(bars, p):
            ax.text(rect.get_x() + rect.get_width() / 2, v + 0.012, f"{v:.2f}",
                    ha="center", fontsize=9.5, color=col)
    ax.set_xticks(xs)
    ax.set_xticklabels([f"{t}\nlogit = {l}" for t, l in zip(tokens, logits)], fontsize=10.5)
    ax.set_ylabel("ความน่าจะเป็น (softmax)")
    ax.set_ylim(0, 0.92)
    ax.legend(frameon=False, fontsize=10.5, title="temperature", title_fontsize=10)
    ax.set_title("บริบท: \"ไฟในห้องแล็บดับ ฉันจึงเปิด ...\" → LLM ให้ความน่าจะเป็นแก่ token ถัดไป",
                 fontsize=12, fontweight="bold", loc="left")
    ax.text(3.45, 0.62, "T ต่ำ = มั่นใจ/ตอบซ้ำได้\nT สูง = หลากหลาย/เพี้ยนง่าย",
            ha="right", fontsize=10, color=INK2)
    save(fig, "w10-next-token")


# ------------------------------------------------------------ 2. RAG pipeline
def rag_pipeline():
    fig, ax = canvas(11.6, 5.8, 14, 7)
    title(ax, "RAG = ค้นเอกสาร (Retrieval) → แนบเข้า prompt (Augmented) → ให้ LLM ตอบ (Generation)", y=6.6)
    # แถวบน: indexing (ทำล่วงหน้า)
    ax.text(0.2, 5.75, "① Indexing (ทำล่วงหน้า)", fontsize=11, fontweight="bold", color=AQUA)
    top = [("เอกสารรายวิชา\nPDF / เว็บ", GRAY_T, MUTED), ("แบ่ง chunk\n200–500 token", AQUA_T, AQUA),
           ("embedding\nmodel → เวกเตอร์", AQUA_T, AQUA), ("Vector DB\n(pgvector ฯลฯ)", YELLOW_T, YELLOW)]
    for i, (t, f, e) in enumerate(top):
        x = 0.3 + i * 3.0
        box(ax, x, 4.55, 2.4, 1.0, t, f, e, 10.5)
        if i:
            arrow(ax, (x - 0.58, 5.05), (x - 0.02, 5.05))
    # แถวล่าง: query (ทุกครั้งที่ถาม)
    ax.text(0.2, 3.55, "② Query (ทุกครั้งที่ถาม)", fontsize=11, fontweight="bold", color=BLUE)
    q = [("คำถาม\n\"ห้องแล็บเปิดกี่โมง\"", BLUE_T, BLUE), ("embedding\nของคำถาม", BLUE_T, BLUE),
         ("ค้น top-k ด้วย\ncosine similarity", YELLOW_T, YELLOW), ("prompt =\nคำสั่ง + context\n+ คำถาม", VIOLET_T, VIOLET),
         ("LLM", ORANGE_T, ORANGE), ("คำตอบ\n+ อ้างอิงแหล่ง", AQUA_T, AQUA)]
    xs = [0.3, 2.65, 5.0, 7.45, 9.9, 11.55]
    ws = [2.05, 2.0, 2.15, 2.1, 1.2, 2.15]
    for (t, f, e), x, w in zip(q, xs, ws):
        box(ax, x, 2.2, w, 1.15, t, f, e, 10)
    for i in range(len(xs) - 1):
        arrow(ax, (xs[i] + ws[i] + 0.02, 2.78), (xs[i + 1] - 0.02, 2.78))
    arrow(ax, (9.7, 4.5), (6.1, 3.4), color=YELLOW, ls="--")
    ax.text(6.9, 4.2, "ดึง chunk ที่ใกล้ที่สุด", fontsize=9.5, color="#9a6a00", ha="right")
    # ตารางคะแนนจากตัวอย่างของเล่น 3 มิติ
    qv = [0.9, 0.1, 0.2]
    chunks = [("A: เวลาเปิดห้องแล็บ 8:30–16:30", [0.8, 0.2, 0.1]),
              ("C: กำหนดการสอบกลางภาค", [0.3, 0.2, 0.9]),
              ("B: กฎการยืมบอร์ด ESP32", [0.2, 0.9, 0.3])]
    scored = sorted(((cosine(qv, v), n, v) for n, v in chunks), reverse=True)
    box(ax, 0.3, 0.1, 13.4, 1.75, "", GRAY_T, GRID)
    ax.text(0.5, 1.55, f"ตัวอย่างของเล่น: เวกเตอร์คำถาม q = {qv}  (ของจริงมีหลายร้อยมิติ)",
            fontsize=10, fontweight="bold", color=INK2, va="center")
    for i, (s, n, v) in enumerate(scored):
        y = 1.1 - i * 0.4
        ax.add_patch(Rectangle((7.3, y - 0.13), 3.6 * s, 0.26, color=YELLOW if i == 0 else GRID))
        ax.text(0.5, y, f"{n}   v = {v}", fontsize=10, va="center", color=INK if i == 0 else INK2)
        ax.text(7.3 + 3.6 * s + 0.1, y, f"cos = {s:.3f}" + ("  ← top-1" if i == 0 else ""),
                fontsize=10, va="center", fontweight="bold" if i == 0 else "normal")
    save(fig, "w10-rag-pipeline")


# ------------------------------------------------------------ 3. Agent loop vs Sense-Plan-Act
def loops():
    fig, axes = plt.subplots(1, 2, figsize=(11.6, 5.4))

    def cycle(ax, name, color, tint, steps, center_text, note):
        ax.set_xlim(0, 7); ax.set_ylim(0, 7); ax.axis("off")
        ax.text(3.5, 6.75, name, ha="center", fontsize=12.5, fontweight="bold", color=color)
        pos = [(3.5, 5.4), (5.75, 3.4), (3.5, 1.4), (1.25, 3.4)]
        for (x, y), (t, f, e) in zip(pos, steps):
            box(ax, x - 1.1, y - 0.5, 2.2, 1.0, t, f, e, 10.5)
        conn = [((4.65, 5.3), (5.6, 3.95)), ((5.6, 2.85), (4.65, 1.5)),
                ((2.35, 1.5), (1.4, 2.85)), ((1.4, 3.95), (2.35, 5.3))]
        for p, q in conn:
            arrow(ax, p, q, color=color, lw=1.8)
        ax.text(3.5, 3.4, center_text, ha="center", va="center", fontsize=10.5, color=INK2)
        ax.text(3.5, 0.3, note, ha="center", va="center", fontsize=10, color=ORANGE)

    cycle(axes[0], "Agentic AI: วงจร ReAct", VIOLET, VIOLET_T,
          [("บริบท\nเป้าหมาย + ผลก่อนหน้า", GRAY_T, MUTED), ("คิด + วางแผน\n(LLM)", VIOLET_T, VIOLET),
           ("เรียก tool\nค้น / คำนวณ / ไฟล์", YELLOW_T, YELLOW), ("สังเกตผล\n(observation)", BLUE_T, BLUE)],
          "วนจนงานเสร็จ\nหรือครบจำนวนรอบ\n→ ตอบผู้ใช้",
          "guardrail: สิทธิ์น้อยที่สุด · log · คนอนุมัติงานเสี่ยง")
    cycle(axes[1], "Physical AI: วงจร Sense–Plan–Act", AQUA, AQUA_T,
          [("Sense\nกล้อง LiDAR IMU", BLUE_T, BLUE), ("Perceive\nเข้าใจสภาพแวดล้อม", AQUA_T, AQUA),
           ("Plan\nเลือกเส้นทาง/ท่าทาง", VIOLET_T, VIOLET), ("Act\nมอเตอร์ ล้อ แขนกล", ORANGE_T, ORANGE)],
          "โลกจริงเปลี่ยน\nต้องวนหลายสิบ\nครั้งต่อวินาที",
          "safety: ปุ่มหยุดฉุกเฉิน · จำกัดความเร็ว/แรง · ทดสอบใน simulation")
    fig.tight_layout(w_pad=1.5)
    save(fig, "w10-agent-robot-loops")


if __name__ == "__main__":
    next_token()
    rag_pipeline()
    loops()
