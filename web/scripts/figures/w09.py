"""Infographic สัปดาห์ที่ 9: AI / ML / DL, รูปแบบการเรียนรู้ 3 แบบ, นิวรอนเทียม 1 ตัว
รัน: python scripts/make_week_figures.py 09
"""
import numpy as np
from matplotlib.patches import Circle

from _style import *  # noqa: F401,F403


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


# ------------------------------------------------------------ 1. AI ⊃ ML ⊃ DL ⊃ GenAI
def ai_ml_dl():
    fig, ax = canvas(10.4, 5.6, 13, 7)
    title(ax, "AI ⊃ Machine Learning ⊃ Deep Learning ⊃ Generative AI", y=6.6)
    levels = [  # (ชื่อ, รัศมี, สีเส้น, สีพื้น, ตัวอย่าง)
        ("AI", 3.0, BLUE, BLUE_T, "ระบบกฎ (rule-based), ค้นหาเส้นทาง A*, หมากรุกยุคแรก"),
        ("Machine Learning", 2.25, AQUA, AQUA_T, "Linear Regression, Decision Tree, k-means"),
        ("Deep Learning", 1.5, VIOLET, VIOLET_T, "CNN จำภาพ, แปลงเสียงเป็นข้อความ"),
        ("Generative AI", 0.95, ORANGE, ORANGE_T, "LLM (ChatGPT, Claude), สร้างภาพ (diffusion)"),
    ]
    cx, base = 3.3, 0.25
    for name, r, edge, fill, _ in levels:
        ax.add_patch(Circle((cx, base + r), r, facecolor=fill, edgecolor=edge, linewidth=1.8))
    # ป้ายชื่อวางในช่องว่างระหว่างขอบบนของวงนอกกับวงใน
    for i, (name, r, edge, _, _) in enumerate(levels):
        top = base + 2 * r
        if i + 1 < len(levels):
            y = (top + base + 2 * levels[i + 1][1]) / 2
        else:
            y = base + r
        ax.text(cx, y, name, ha="center", va="center", fontsize=11.5 if i < 3 else 9.5,
                fontweight="bold", color=edge)
    defs = ["ระบบที่ทำงานซึ่งปกติต้องใช้ปัญญามนุษย์",
            "เรียนรู้ pattern จากข้อมูล แทนการเขียนกฎเอง",
            "neural network หลายชั้น เรียน feature เอง",
            "สร้างข้อมูลใหม่ (ข้อความ ภาพ โค้ด)"]
    for i, ((name, r, edge, fill, ex), d) in enumerate(zip(levels, defs)):
        y = 5.35 - i * 1.4
        box(ax, 7.0, y, 5.8, 1.15, "", fill, edge)
        ax.text(7.15, y + 0.82, f"{name}", fontsize=10.5, fontweight="bold", color=edge, va="center")
        ax.text(7.15, y + 0.55, d, fontsize=10, color=INK, va="center")
        ax.text(7.15, y + 0.22, "เช่น " + ex, fontsize=9.5, color=INK2, va="center")
        ring_y = base + 2 * r - 0.08
        arrow(ax, (cx + 0.9, ring_y), (6.95, y + 0.58), color=edge, lw=1.1, style="-")
    save(fig, "w09-ai-ml-dl")


# ------------------------------------------------------------ 2. รูปแบบการเรียนรู้ 3 แบบ
def learning_types():
    rng = np.random.default_rng(9)
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.6))
    # (ก) supervised: 2 คลาสมี label + เส้นแบ่งจาก perceptron learning rule
    a = rng.normal([2, 2], 0.6, (25, 2))
    b = rng.normal([4.2, 4.0], 0.6, (25, 2))
    X = np.vstack([a, b]); y = np.r_[np.zeros(25), np.ones(25)]
    w, bias = np.zeros(2), 0.0
    for _ in range(50):
        for xi, yi in zip(X, y):
            pred = 1.0 if xi @ w + bias >= 0 else 0.0
            w += 0.1 * (yi - pred) * xi
            bias += 0.1 * (yi - pred)
    acc = np.mean(((X @ w + bias) >= 0) == y)
    ax = axes[0]
    ax.scatter(*a.T, color=BLUE, s=28, label="label = แมว")
    ax.scatter(*b.T, color=ORANGE, s=28, marker="s", label="label = หมา")
    xs = np.linspace(0, 6.5, 2)
    ax.plot(xs, -(w[0] * xs + bias) / w[1], color=INK2, ls="--", lw=1.6)
    ax.set_xlim(0, 6.5); ax.set_ylim(0, 6.5)
    ax.set_title("Supervised: มีคำตอบ (label)", fontsize=12, fontweight="bold", color=BLUE)
    ax.text(6.3, 6.1, "เรียนเส้นแบ่ง (เส้นประ)\n" f"train accuracy = {acc:.0%}", fontsize=9.5, color=INK2, ha="right", va="top")
    ax.legend(loc="lower right", fontsize=9.5, frameon=False)
    ax.set_xlabel("feature 1"); ax.set_ylabel("feature 2")
    # (ข) unsupervised: ไม่มี label → k-means (k = 3) เขียนเองด้วย numpy
    centers_true = np.array([[1.5, 4.6], [4.8, 4.4], [3.2, 1.4]])
    P = np.vstack([rng.normal(c, 0.55, (20, 2)) for c in centers_true])
    C = P[[0, 20, 40]].copy()
    for _ in range(10):
        lab = np.argmin(((P[:, None, :] - C[None]) ** 2).sum(-1), axis=1)
        C = np.array([P[lab == k].mean(0) for k in range(3)])
    ax = axes[1]
    for k, col in enumerate([AQUA, VIOLET, YELLOW]):
        ax.scatter(*P[lab == k].T, color=col, s=28)
        ax.scatter(*C[k], color=INK, marker="X", s=110)
    ax.set_xlim(0, 6.5); ax.set_ylim(0, 6.5)
    ax.set_title("Unsupervised: ไม่มี label", fontsize=12, fontweight="bold", color=AQUA)
    ax.text(0.2, 6.0, "k-means หากลุ่มเอง (X = จุดศูนย์กลาง)", fontsize=9.5, color=INK2)
    ax.set_xlabel("feature 1")
    # (ค) reinforcement: agent เลือก 3 ทางเลือกแบบ ε-greedy (ε = 0.1) รางวัลเฉลี่ยเพิ่มตามประสบการณ์
    true_p = np.array([0.2, 0.5, 0.8]); Q = np.zeros(3); N = np.zeros(3)
    rewards = []
    for _ in range(400):
        act = int(rng.integers(3)) if rng.random() < 0.1 else int(np.argmax(Q))
        r = float(rng.random() < true_p[act])
        N[act] += 1
        Q[act] += (r - Q[act]) / N[act]
        rewards.append(r)
    win = 40
    avg = np.convolve(rewards, np.ones(win) / win, mode="valid")
    ax = axes[2]; ygrid(ax)
    ax.plot(np.arange(len(avg)) + win, avg, color=VIOLET)
    ax.axhline(true_p.max(), color=MUTED, ls=":", lw=1.4)
    ax.text(390, 0.08, f"เส้นจุด = reward สูงสุดที่เป็นไปได้ ({true_p.max():.1f})", fontsize=9.5, color=MUTED, ha="right")
    ax.set_ylim(0, 1.05); ax.set_xlim(0, 400)
    ax.set_title("Reinforcement: ลองผิดลองถูก", fontsize=12, fontweight="bold", color=VIOLET)
    ax.set_xlabel("จำนวนครั้งที่ลอง"); ax.set_ylabel(f"reward เฉลี่ย ({win} ครั้งล่าสุด)")
    fig.tight_layout(w_pad=2.2)
    save(fig, "w09-learning-types")


# ------------------------------------------------------------ 3. นิวรอน: weighted sum + sigmoid + gradient descent 1 รอบ
def neuron():
    x = np.array([0.8, 0.6]); w = np.array([1.5, 0.5]); b = -1.0; y = 1.0; lr = 1.0
    z = x @ w + b; yh = sigmoid(z); loss = (y - yh) ** 2
    dz = 2 * (yh - y) * yh * (1 - yh)          # dLoss/dz (chain rule)
    w2 = w - lr * dz * x; b2 = b - lr * dz
    yh2 = sigmoid(x @ w2 + b2); loss2 = (y - yh2) ** 2

    fig = plt.figure(figsize=(11.5, 5.4))
    ax = fig.add_axes([0, 0, 0.66, 1]); ax.set_xlim(0, 10.6); ax.set_ylim(0, 7.5); ax.axis("off")
    title(ax, "นิวรอน 1 ตัว: ควรเปิดพัดลมไหม? (คำตอบจริง y = 1)", y=6.9)
    for lab, xv, wv, yy in [("x₁ อุณหภูมิ\n(สเกล 0–1)", x[0], w[0], 5.0),
                            ("x₂ ความชื้น\n(สเกล 0–1)", x[1], w[1], 3.2)]:
        box(ax, 0.2, yy - 0.5, 1.9, 1.0, lab, BLUE_T, BLUE, 10)
        ax.text(1.15, yy - 0.8, f"= {xv}", ha="center", fontsize=10.5, fontweight="bold", color=BLUE)
        arrow(ax, (2.15, yy), (4.25, 3.9 + (yy - 4.1) * 0.25), color=BLUE)
        ax.text(2.5, yy + (0.12 if yy > 4 else 0.38), f"w = {wv}", fontsize=10.5, color=INK2, fontweight="bold")
    box(ax, 0.2, 0.95, 1.9, 0.75, "bias b", YELLOW_T, YELLOW, 10.5)
    ax.text(1.15, 0.6, f"= {b}", ha="center", fontsize=10.5, fontweight="bold", color="#9a6a00")
    arrow(ax, (2.15, 1.35), (4.4, 3.3), color=YELLOW)
    ax.add_patch(Circle((5.0, 3.9), 0.75, facecolor=VIOLET_T, edgecolor=VIOLET, linewidth=1.8))
    ax.text(5.0, 3.9, "Σ", ha="center", va="center", fontsize=22, color=VIOLET)
    ax.text(5.0, 5.55, f"z = {w[0]}·{x[0]} + {w[1]}·{x[1]} − {abs(b)}\n= {z:.2f}",
            ha="center", va="center", fontsize=10.5, color=VIOLET)
    arrow(ax, (5.78, 3.9), (6.6, 3.9), color=VIOLET)
    box(ax, 6.65, 3.35, 1.55, 1.1, "σ(z)\nsigmoid", AQUA_T, AQUA, 10.5)
    arrow(ax, (8.25, 3.9), (8.75, 3.9), color=AQUA)
    ax.text(8.8, 4.15, f"ŷ = {yh:.3f}", fontsize=12, fontweight="bold", color=AQUA, va="center")
    ax.text(8.8, 3.6, f"loss = (y − ŷ)²\n= {loss:.3f}", fontsize=10, color=INK2, va="top")
    box(ax, 3.6, 0.2, 6.9, 1.35, "", ORANGE_T, ORANGE)
    ax.text(3.75, 1.2, f"gradient descent 1 รอบ (learning rate = {lr:g}) ปรับ w, b ให้ loss ลด",
            fontsize=10.5, fontweight="bold", color=ORANGE, va="center")
    ax.text(3.75, 0.6, f"w → [{w2[0]:.3f}, {w2[1]:.3f}], b → {b2:.3f}  ⇒  ŷ = {yh2:.3f}, loss = {loss2:.3f}",
            fontsize=10, color=INK, va="center")
    a2 = fig.add_axes([0.72, 0.17, 0.26, 0.62]); ygrid(a2)
    zz = np.linspace(-6, 6, 200)
    a2.plot(zz, sigmoid(zz), color=AQUA)
    a2.scatter([z], [yh], color=ORANGE, zorder=3, s=40)
    a2.annotate(f"z = {z:.1f} → {yh:.3f}", (z, yh), (0.9, 0.25), fontsize=10, color=ORANGE,
                arrowprops=dict(arrowstyle="-", color=ORANGE, lw=1))
    a2.axhline(0.5, color=MUTED, ls=":", lw=1)
    a2.set_title("σ(z) = 1 / (1 + e⁻ᶻ)", fontsize=11.5, fontweight="bold")
    a2.set_xlabel("z (weighted sum)"); a2.set_ylim(-0.03, 1.03)
    save(fig, "w09-neuron")


if __name__ == "__main__":
    ai_ml_dl()
    learning_types()
    neuron()
