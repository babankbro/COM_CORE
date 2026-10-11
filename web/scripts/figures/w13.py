"""Week 13 · จริยธรรมทางคอมพิวเตอร์และทรัพย์สินทางปัญญา — infographic 3 ภาพ"""
from _style import *  # noqa: F401,F403


def ethics_decision_flow():
    """ขั้นตอนตัดสินใจเชิงจริยธรรม 6 ขั้น (ACM Code + PDPA)"""
    fig, ax = canvas(11.6, 5.6, 14.5, 7.0)
    title(ax, "ขั้นตอนตัดสินใจเชิงจริยธรรม: จากข้อเท็จจริงถึงการตัดสินใจที่ตรวจสอบได้")
    steps = [
        ("1  ข้อเท็จจริง", "ระบบทำอะไร เก็บข้อมูลอะไร\nใครได้ประโยชน์ / ใครเสี่ยง", BLUE, BLUE_T),
        ("2  ระบุประเด็น", "privacy · bias · ความโปร่งใส\nความรับผิดชอบ · IP", VIOLET, VIOLET_T),
        ("3  เทียบ ACM Code", "1.1 public good · 1.2 avoid harm\n1.4 fair · 1.6 privacy", AQUA, AQUA_T),
        ("4  ตรวจกฎหมาย", "PDPA: ฐานกฎหมาย / ข้อมูลอ่อนไหว\nลิขสิทธิ์ · license", YELLOW, YELLOW_T),
        ("5  สร้างทางเลือก", "อย่างน้อย 3 ทาง\nเลือกทางที่ intrusive น้อยสุด", ORANGE, ORANGE_T),
        ("6  บันทึกและทบทวน", "เขียนเหตุผล ใครรับผิดชอบ\nกำหนดวันทบทวนซ้ำ", BLUE, GRAY_T),
    ]
    w, h = 4.0, 2.05
    xs = [0.4, 5.25, 10.1]
    ys = [3.9, 0.9]
    pos = [(xs[0], ys[0]), (xs[1], ys[0]), (xs[2], ys[0]), (xs[2], ys[1]), (xs[1], ys[1]), (xs[0], ys[1])]
    for (head, body, edge, fill), (x, y) in zip(steps, pos):
        box(ax, x, y, w, h, "", fill, edge)
        ax.text(x + 0.2, y + h - 0.38, head, fontsize=12, fontweight="bold", color=edge, va="center")
        ax.text(x + 0.2, y + 0.75, body, fontsize=10.5, color=INK, va="center", linespacing=1.5)
    for i in range(2):
        arrow(ax, (pos[i][0] + w + 0.05, ys[0] + h / 2), (pos[i + 1][0] - 0.05, ys[0] + h / 2))
    arrow(ax, (xs[2] + w / 2, ys[0] - 0.05), (xs[2] + w / 2, ys[1] + h + 0.05))
    for i in (3, 4):
        arrow(ax, (pos[i][0] - 0.05, ys[1] + h / 2), (pos[i + 1][0] + w + 0.05, ys[1] + h / 2))
    ax.text(7.25, 0.35, "ถ้าทุกทางเลือกยังละเมิดสิทธิหรือผิดกฎหมาย → ไม่ทำ / ยกระดับให้ผู้มีอำนาจตัดสินใจ (ACM 2.3, 3.1)",
            ha="center", fontsize=10, color=INK2)
    return fig


def ip_types_grid():
    """เปรียบเทียบทรัพย์สินทางปัญญา 4 ประเภท (บริบทกฎหมายไทย)"""
    fig, ax = canvas(12.8, 6.6, 15.6, 8.0)
    title(ax, "ทรัพย์สินทางปัญญา 4 ประเภทที่วิศวกรคอมพิวเตอร์ต้องแยกให้ออก (กฎหมายไทย)")
    cols = [
        ("ลิขสิทธิ์\nCopyright", BLUE, BLUE_T),
        ("สิทธิบัตร\nPatent", ORANGE, ORANGE_T),
        ("เครื่องหมายการค้า\nTrademark", AQUA, AQUA_T),
        ("ความลับทางการค้า\nTrade secret", VIOLET, VIOLET_T),
    ]
    rows = [
        ("คุ้มครองอะไร", ["การแสดงออกของความคิด\n(ไม่คุ้มครองไอเดีย/อัลกอริทึม)", "การประดิษฐ์ที่ใหม่ มีขั้นสูงขึ้น\nและใช้ในอุตสาหกรรมได้",
                         "ชื่อ/โลโก้ที่บ่งบอก\nแหล่งที่มาของสินค้า-บริการ", "ข้อมูลที่มีมูลค่า\nเพราะยังเป็นความลับ"]),
        ("ตัวอย่าง\nในงานคอมพิวเตอร์", ["source code, UI, คู่มือ,\nรูปภาพ, รายงาน", "วงจร/อุปกรณ์ IoT ใหม่\n(โปรแกรมล้วนจดไม่ได้)",
                                     "ชื่อแอป ไอคอน\nชื่อทีม/ผลิตภัณฑ์", "โค้ดฝั่ง server\nmodel weight · สูตร ranking"]),
        ("ได้สิทธิอย่างไร", ["อัตโนมัติเมื่อสร้างสรรค์\n(ไม่ต้องจดทะเบียน)", "ต้องยื่นคำขอ\nและได้รับอนุมัติ",
                            "จดทะเบียน\nกับกรมทรัพย์สินทางปัญญา", "ไม่ต้องจด แต่ต้องมี\nมาตรการรักษาความลับ (NDA)"]),
        ("อายุคุ้มครอง", ["ตลอดชีวิตผู้สร้างสรรค์\n+ 50 ปี", "20 ปีนับจากวันยื่น\n(อนุสิทธิบัตร ≤ 10 ปี)",
                         "10 ปี ต่ออายุได้\nครั้งละ 10 ปี", "ตราบที่ยังรักษา\nความลับไว้ได้"]),
        ("กฎหมายไทย", ["พ.ร.บ.ลิขสิทธิ์\nพ.ศ. 2537", "พ.ร.บ.สิทธิบัตร\nพ.ศ. 2522", "พ.ร.บ.เครื่องหมายการค้า\nพ.ศ. 2534",
                       "พ.ร.บ.ความลับทางการค้า\nพ.ศ. 2545"]),
    ]
    x0, lw, cw, gap = 0.2, 2.5, 3.1, 0.1
    top, hh, rh = 7.1, 0.95, 1.12
    for j, (name, edge, fill) in enumerate(cols):
        x = x0 + lw + gap + j * (cw + gap)
        box(ax, x, top - hh, cw, hh, name, edge, edge, size=11, weight="bold", color="white")
    for i, (label, cells) in enumerate(rows):
        y = top - hh - gap - (i + 1) * rh + 0.0 - i * gap
        box(ax, x0, y, lw, rh, label, GRAY_T, MUTED, size=10.5, weight="bold")
        for j, txt in enumerate(cells):
            x = x0 + lw + gap + j * (cw + gap)
            box(ax, x, y, cw, rh, txt, cols[j][2], cols[j][1], size=10)
    return fig


def license_spectrum():
    """สเปกตรัม software license: permissive ↔ copyleft ↔ proprietary"""
    fig, ax = canvas(12.4, 5.8, 15.0, 7.0)
    title(ax, "สเปกตรัม Software License: ยิ่งไปทางขวา ยิ่งมีข้อผูกมัดเมื่อแจกจ่ายต่อ")
    arrow(ax, (0.4, 5.95), (14.6, 5.95), color=INK2, lw=2)
    ax.text(0.4, 6.15, "เงื่อนไขน้อย", fontsize=10, color=INK2)
    ax.text(14.6, 6.15, "เงื่อนไขมาก / ปิด", fontsize=10, color=INK2, ha="right")
    zones = [
        ("Permissive", AQUA, AQUA_T, [("MIT · BSD", "เก็บ copyright\n+ license notice"),
                                     ("Apache-2.0", "notice + แจ้งไฟล์ที่แก้\n+ ให้สิทธิ patent")]),
        ("Weak copyleft", YELLOW, YELLOW_T, [("LGPL-3.0", "แก้ตัว library ต้องเปิด\nลิงก์ใช้ในงานปิดได้"),
                                            ("MPL-2.0", "copyleft ระดับไฟล์\nไฟล์ที่แก้ต้องเปิด")]),
        ("Strong copyleft", ORANGE, ORANGE_T, [("GPL-3.0", "แจกจ่ายงานดัดแปลง\nต้องเปิด source ด้วย GPL"),
                                              ("AGPL-3.0", "ให้บริการผ่านเครือข่าย\nก็ต้องเปิด source")]),
        ("Proprietary", VIOLET, VIOLET_T, [("EULA เชิงพาณิชย์", "ใช้ตามสัญญา\nห้ามแก้ / แจกต่อ"),
                                          ("Freeware", "ใช้ฟรี แต่ไม่ได้\nsource code")]),
    ]
    zw, gap = 3.4, 0.27
    for k, (zname, edge, fill, cards) in enumerate(zones):
        x = 0.4 + k * (zw + gap)
        box(ax, x, 0.35, zw, 5.2, "", fill, edge)
        ax.text(x + zw / 2, 5.1, zname, ha="center", va="center", fontsize=12, fontweight="bold", color=edge)
        for c, (lic, cond) in enumerate(cards):
            y = 2.75 - c * 2.25
            box(ax, x + 0.2, y, zw - 0.4, 1.95, "", "white", edge)
            ax.text(x + zw / 2, y + 1.5, lic, ha="center", va="center", fontsize=11.5, fontweight="bold")
            ax.text(x + zw / 2, y + 0.68, cond, ha="center", va="center", fontsize=10, color=INK2, linespacing=1.4)
    return fig


if __name__ == "__main__":
    save(ethics_decision_flow(), "w13-ethics-decision-flow")
    save(ip_types_grid(), "w13-ip-types")
    save(license_spectrum(), "w13-license-spectrum")
