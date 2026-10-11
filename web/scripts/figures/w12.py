"""Infographic สัปดาห์ที่ 12: Cybersecurity และ Zero Trust
รัน: python scripts/make_week_figures.py 12
"""
from _style import *  # noqa: F401,F403


def _card(ax, x, y, w, h, head, color, tint, attacks, controls):
    box(ax, x, y, w, h, "", tint, color)
    ax.text(x + w / 2, y + h - 0.35, head, ha="center", fontsize=12, fontweight="bold", color=color)
    ax.text(x + 0.18, y + h - 0.85, "ภัยคุกคาม", fontsize=10, fontweight="bold", color=ORANGE)
    for i, a in enumerate(attacks):
        ax.text(x + 0.18, y + h - 1.25 - i * 0.38, "✗ " + a, fontsize=10, color=INK)
    yc = y + h - 1.35 - len(attacks) * 0.38
    ax.text(x + 0.18, yc, "มาตรการป้องกัน", fontsize=10, fontweight="bold", color=AQUA)
    for i, c in enumerate(controls):
        ax.text(x + 0.18, yc - 0.4 - i * 0.38, "✓ " + c, fontsize=10, color=INK)


def cia_triad():
    """CIA triad: สามมุม พร้อมตัวอย่างการโจมตีและมาตรการป้องกัน"""
    fig, ax = canvas(12, 7.0, xlim=14, ylim=8.6)
    title(ax, "CIA Triad: ถามทุกครั้งว่าเหตุการณ์นี้ทำให้ด้านไหนเสียหาย", y=8.25)
    A, B, C = (7.0, 6.9), (4.75, 2.7), (9.25, 2.7)
    ax.add_patch(plt.Polygon([A, B, C], closed=True, facecolor=GRAY_T, edgecolor=MUTED, linewidth=1.5))
    ax.text(7.0, 4.1, "ข้อมูลและ\nระบบ", ha="center", va="center", fontsize=12, fontweight="bold", color=INK2)
    for (x, y), lab, col in [(A, "C", BLUE), (B, "I", VIOLET), (C, "A", AQUA)]:
        ax.add_patch(plt.Circle((x, y), 0.42, facecolor=col, edgecolor="white", linewidth=2, zorder=3))
        ax.text(x, y, lab, ha="center", va="center", fontsize=15, fontweight="bold", color="white", zorder=4)
    _card(ax, 0.2, 4.55, 4.0, 3.35, "Confidentiality · ความลับ", BLUE, BLUE_T,
          ["ดักฟังข้อมูล (sniffing/MITM)", "SQL injection ดึงตารางผู้ใช้"],
          ["เข้ารหัส AES / TLS", "least privilege + MFA"])
    _card(ax, 0.2, 0.15, 4.0, 3.35, "Integrity · ความถูกต้อง", VIOLET, VIOLET_T,
          ["แก้ค่า sensor ระหว่างทาง", "ปลอมเฟิร์มแวร์ / ไฟล์"],
          ["hash / HMAC ตรวจการแก้ไข", "digital signature, validate input"])
    _card(ax, 9.8, 0.15, 4.0, 3.35, "Availability · พร้อมใช้", AQUA, AQUA_T,
          ["DDoS ยิง broker/เว็บ", "ransomware เข้ารหัสข้อมูล"],
          ["rate limit, CDN, redundancy", "backup 3-2-1 ที่แยก offline"])
    box(ax, 9.8, 4.55, 4.0, 3.35, "", SURFACE, GRID)
    ax.text(10.0, 7.5, "วิธีใช้กรอบนี้", fontsize=11.5, fontweight="bold")
    tips = ["1) ระบุทรัพย์สิน (asset)", "2) ถามว่า C, I หรือ A เสีย", "3) เลือก control ให้ตรงด้าน",
            "4) วางหลายชั้น", "    (defense-in-depth)", "หนึ่งเหตุการณ์อาจกระทบ", "มากกว่าหนึ่งด้าน"]
    for i, t in enumerate(tips):
        ax.text(10.0, 7.0 - i * 0.38, t, fontsize=10, color=INK2 if i < 5 else ORANGE)
    save(fig, "w12-cia-triad")


def _key(ax, x, y, color, label):
    ax.add_patch(plt.Circle((x, y), 0.17, facecolor="white", edgecolor=color, linewidth=2.2, zorder=3))
    ax.plot([x + 0.17, x + 0.62], [y, y], color=color, linewidth=2.2, zorder=3)
    ax.plot([x + 0.5, x + 0.5], [y, y - 0.14], color=color, linewidth=2.2, zorder=3)
    ax.text(x + 0.78, y, label, va="center", fontsize=10, color=color)


def crypto_keys():
    """Symmetric (กุญแจเดียวกัน) เทียบ Asymmetric (คู่กุญแจ) และการใช้ร่วมกันใน TLS"""
    fig, ax = canvas(12, 6.6, xlim=14, ylim=8.2)
    title(ax, "Symmetric เทียบ Asymmetric: ใช้กุญแจดอกไหนล็อก ดอกไหนเปิด", y=7.85)

    def lane(y, head, color, tint, k1, k2, c1, c2, note):
        ax.text(0.2, y + 2.0, head, fontsize=12, fontweight="bold", color=color)
        box(ax, 0.2, y, 2.0, 1.1, "Alice\nข้อความ \"สวัสดี\"", GRAY_T, MUTED, size=10)
        box(ax, 3.0, y, 2.1, 1.1, "เข้ารหัส\n" + c1, tint, color, size=10)
        box(ax, 6.0, y, 2.2, 1.1, "ciphertext\n7f3a9c...e1", SURFACE, INK2, size=10)
        box(ax, 9.1, y, 2.1, 1.1, "ถอดรหัส\n" + c2, tint, color, size=10)
        box(ax, 12.0, y, 1.8, 1.1, "Bob\n\"สวัสดี\"", GRAY_T, MUTED, size=10)
        for a, b in [(2.2, 3.0), (5.1, 6.0), (8.2, 9.1), (11.2, 12.0)]:
            arrow(ax, (a + 0.03, y + 0.55), (b - 0.03, y + 0.55), color=INK2)
        _key(ax, 3.4, y + 1.45, k1[1], k1[0])
        _key(ax, 9.5, y + 1.45, k2[1], k2[0])
        ax.text(0.2, y - 0.4, note, fontsize=10, color=INK2)

    lane(4.55, "1 · Symmetric (AES): กุญแจลับดอกเดียวกันทั้งสองฝั่ง", BLUE, BLUE_T,
         ("กุญแจลับ K", BLUE), ("กุญแจลับ K", BLUE), "AES ด้วย K", "AES ด้วย K",
         "เร็วมาก เหมาะกับข้อมูลปริมาณมาก · ปัญหา: จะส่ง K ให้ Bob อย่างปลอดภัยได้อย่างไร?")
    lane(1.5, "2 · Asymmetric (RSA/ECC): คู่กุญแจของ Bob", VIOLET, VIOLET_T,
         ("public key ของ Bob", AQUA), ("private key ของ Bob", ORANGE), "ด้วย public", "ด้วย private",
         "ใครก็ล็อกได้ แต่ Bob คนเดียวเปิดได้ · ช้ากว่า · ลายเซ็นดิจิทัลใช้กลับด้าน: sign ด้วย private, verify ด้วย public")
    box(ax, 0.2, 0.05, 13.6, 0.6, "ใน HTTPS/TLS ใช้ร่วมกัน: asymmetric ยืนยันตัวตน (certificate) และตกลงกุญแจ → symmetric เข้ารหัสข้อมูลจริง",
        YELLOW_T, YELLOW, size=10.5)
    save(fig, "w12-crypto-keys")


def zero_trust():
    """Perimeter (castle-and-moat) เทียบ Zero Trust (ตรวจทุก request ผ่าน PDP/PEP)"""
    fig, ax = canvas(12, 6.4, xlim=14, ylim=8)
    title(ax, "Perimeter security เทียบ Zero Trust (NIST SP 800-207)", y=7.65)
    # perimeter
    ax.text(0.2, 7.0, "แบบเดิม: ปราสาทและคูน้ำ", fontsize=11.5, fontweight="bold", color=ORANGE)
    ax.add_patch(FancyBboxPatch((0.4, 1.3), 5.6, 4.9, boxstyle="round,pad=0.02,rounding_size=0.3",
                                facecolor=ORANGE_T, edgecolor=ORANGE, linewidth=3))
    ax.text(3.2, 5.8, "เครือข่ายภายใน = เชื่อใจ", ha="center", fontsize=10.5, color=ORANGE)
    nodes = {"พนักงาน": (1.0, 4.4), "เว็บเซิร์ฟเวอร์": (3.6, 4.4), "ฐานข้อมูล": (3.6, 2.0), "IoT": (1.0, 2.0)}
    for t, (x, y) in nodes.items():
        box(ax, x, y, 1.9, 0.75, t, SURFACE, MUTED, size=10)
    box(ax, 0.0, 3.25, 0.8, 0.7, "FW", INK2, INK2, size=10, color="white", weight="bold")
    ax.text(0.4, 0.75, "ผู้โจมตีผ่าน firewall ได้ครั้งเดียว", fontsize=10, color=INK)
    ax.text(0.4, 0.3, "→ เคลื่อนที่ด้านข้าง (lateral movement) ได้ทั่ว", fontsize=10, color=ORANGE)
    for p, q in [((1.95, 2.75), (3.6, 2.4)), ((1.95, 2.75), (1.95, 4.4)), ((2.9, 4.8), (3.6, 4.8))]:
        arrow(ax, p, q, color=ORANGE, ls="--", lw=1.6)
    # zero trust
    ax.text(7.2, 7.0, "Zero Trust: ไม่เชื่อใจโดยปริยาย ตรวจทุก request", fontsize=11.5, fontweight="bold", color=AQUA)
    box(ax, 7.2, 3.7, 1.9, 1.3, "Subject\nผู้ใช้ + อุปกรณ์", BLUE_T, BLUE, size=10)
    box(ax, 9.7, 3.7, 1.5, 1.3, "PEP\nด่านตรวจ", AQUA_T, AQUA, size=10, weight="bold")
    box(ax, 11.8, 4.55, 2.0, 0.75, "Resource A", SURFACE, AQUA, size=10)
    box(ax, 11.8, 3.4, 2.0, 0.75, "Resource B", SURFACE, AQUA, size=10)
    arrow(ax, (9.1, 4.35), (9.7, 4.35), color=INK2, lw=2)
    arrow(ax, (11.2, 4.5), (11.8, 4.9), color=AQUA, lw=2)
    arrow(ax, (11.2, 4.2), (11.8, 3.8), color=AQUA, lw=2)
    box(ax, 9.2, 5.6, 2.6, 1.0, "PDP\nPolicy Engine + Admin", VIOLET_T, VIOLET, size=10, weight="bold")
    arrow(ax, (10.45, 5.05), (10.45, 5.55), color=VIOLET, style="<->")
    sig = ["identity + MFA", "สภาพอุปกรณ์ (patch, EDR)", "บริบท: เวลา/ที่ตั้ง/พฤติกรรม", "threat intel · log"]
    box(ax, 7.2, 0.6, 6.6, 2.35, "", GRAY_T, GRID)
    ax.text(7.4, 2.6, "สัญญาณที่ PDP ใช้ตัดสิน (ทุกครั้ง ทุก session)", fontsize=10.5, fontweight="bold")
    for i, s in enumerate(sig):
        ax.text(7.5 + (i % 2) * 3.2, 2.05 - (i // 2) * 0.5, "• " + s, fontsize=10)
    ax.text(7.4, 0.85, "ให้สิทธิ์น้อยที่สุด (least privilege) และแยก resource เป็นส่วนย่อย", fontsize=10, color=AQUA)
    arrow(ax, (10.5, 2.95), (10.5, 3.65), color=MUTED, ls="--")
    save(fig, "w12-zero-trust")


if __name__ == "__main__":
    cia_triad()
    crypto_keys()
    zero_trust()
