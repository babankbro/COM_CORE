"""Infographic สัปดาห์ที่ 3: วงจรตรรกะและหน่วยประมวลผล
รัน: python scripts/make_week_figures.py 03
"""
from _style import *  # noqa: F401,F403


def XOR(a, b): return a ^ b
def AND(a, b): return a & b
def OR(a, b): return a | b


def half_adder(a, b):
    return XOR(a, b), AND(a, b)


def full_adder(a, b, cin):
    s1, c1 = half_adder(a, b)
    s, c2 = half_adder(s1, cin)
    return s, OR(c1, c2)


def wire(ax, pts, color=INK2, lw=1.5):
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=color, lw=lw, solid_capstyle="round")


# ---------------------------------------------------------------- 1. Half adder -> Full adder
def adders():
    fig, ax = canvas(10.4, 5.4, 13.4, 7.0)
    title(ax, "จากเกตสู่การบวก: Half Adder = XOR + AND · Full Adder = Half Adder 2 ตัว + OR")
    # --- half adder (ซ้าย)
    ax.text(0.3, 5.95, "Half Adder (บวก 2 บิต)", fontsize=11.5, fontweight="bold", color=BLUE)
    ax.text(0.3, 5.0, "A", fontsize=12, fontweight="bold", va="center")
    ax.text(0.3, 4.6, "B", fontsize=12, fontweight="bold", va="center")
    box(ax, 2.0, 4.35, 1.4, 0.9, "XOR", BLUE_T, BLUE, size=11.5, weight="bold")
    box(ax, 2.0, 2.55, 1.4, 0.9, "AND", ORANGE_T, ORANGE, size=11.5, weight="bold")
    wire(ax, [(0.65, 5.0), (2.0, 5.0)])                  # A -> XOR
    wire(ax, [(0.65, 4.6), (2.0, 4.6)])                  # B -> XOR
    wire(ax, [(1.0, 5.0), (1.0, 3.2), (2.0, 3.2)])       # A -> AND
    wire(ax, [(1.5, 4.6), (1.5, 2.8), (2.0, 2.8)])       # B -> AND
    for p in [(1.0, 5.0), (1.5, 4.6)]:
        ax.scatter(*p, s=22, color=INK2, zorder=4)
    arrow(ax, (3.4, 4.8), (4.2, 4.8), color=BLUE); ax.text(4.3, 4.8, "S (Sum)", va="center", fontsize=11, color=BLUE)
    arrow(ax, (3.4, 3.0), (4.2, 3.0), color=ORANGE); ax.text(4.3, 3.0, "C (Carry)", va="center", fontsize=11, color=ORANGE)
    # ตารางความจริง (คำนวณจากฟังก์ชัน)
    tx, ty = 0.6, 1.95
    cols = [INK, INK, BLUE, ORANGE]
    for j, h in enumerate(["A", "B", "S", "C"]):
        ax.text(tx + j * 0.8, ty, h, ha="center", fontsize=10.5, fontweight="bold", color=cols[j])
    for i, (a, b) in enumerate([(0, 0), (0, 1), (1, 0), (1, 1)]):
        s, c = half_adder(a, b)
        for j, v in enumerate([a, b, s, c]):
            ax.text(tx + j * 0.8, ty - 0.42 - i * 0.37, str(v), ha="center", fontsize=10.5,
                    color=cols[j], fontweight="bold" if (a, b) == (1, 1) else "normal")
    ax.text(3.9, 0.9, "1 + 1 = 10₂\n→ S = 0, C = 1", fontsize=10, color=INK2, va="center")
    # --- full adder (ขวา)
    ax.plot([6.0, 6.0], [0.2, 6.2], color=GRID, lw=1.2)
    ax.text(6.4, 5.95, "Full Adder (บวก 2 บิต + carry เข้า)", fontsize=11.5, fontweight="bold", color=VIOLET)
    for lab, y in [("A", 4.95), ("B", 4.25), ("Cin", 2.6)]:
        ax.text(6.4, y, lab, va="center", fontsize=11.5, fontweight="bold")
        wire(ax, [(7.1, y), (7.6, y)])
    box(ax, 7.6, 3.95, 1.5, 1.3, "Half\nAdder 1", BLUE_T, BLUE, size=10.5)
    box(ax, 9.9, 2.25, 1.5, 1.3, "Half\nAdder 2", BLUE_T, BLUE, size=10.5)
    box(ax, 11.9, 4.3, 0.9, 0.8, "OR", AQUA_T, AQUA, size=11, weight="bold")
    wire(ax, [(7.6, 2.6), (9.9, 2.6)])                                # Cin -> HA2
    wire(ax, [(9.1, 4.25), (9.5, 4.25), (9.5, 3.25), (9.9, 3.25)])    # S1 -> HA2
    ax.text(9.2, 3.65, "S1", fontsize=10, color=BLUE)
    wire(ax, [(9.1, 4.95), (11.9, 4.95)])                             # C1 -> OR
    ax.text(10.4, 5.1, "C1", fontsize=10, color=ORANGE)
    wire(ax, [(11.4, 3.2), (11.65, 3.2), (11.65, 4.5), (11.9, 4.5)])  # C2 -> OR
    ax.text(11.55, 3.75, "C2", fontsize=10, color=ORANGE, ha="right")
    arrow(ax, (11.4, 2.6), (12.3, 2.6), color=BLUE)
    ax.text(12.4, 2.6, "S", va="center", fontsize=11.5, color=BLUE, fontweight="bold")
    arrow(ax, (12.8, 4.7), (13.2, 4.7), color=ORANGE)
    ax.text(12.6, 5.35, "Cout", ha="center", fontsize=11, color=ORANGE, fontweight="bold")
    rows = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
    ones = sum(full_adder(*r)[1] for r in rows)
    ax.text(6.4, 1.3, f"ตรวจครบ {len(rows)} กรณี: Cout = 1 ใน {ones} กรณี (มีบิต 1 ตั้งแต่ 2 ตัว)", fontsize=10, color=INK2)
    ax.text(6.4, 0.7, "S = A ⊕ B ⊕ Cin   ·   Cout = AB + Cin(A ⊕ B)", fontsize=10.5, color=VIOLET, fontweight="bold")
    save(fig, "w03-adders")


# ---------------------------------------------------------------- 2. Ripple-carry 6 + 7
def ripple_carry(x=6, y=7, width=4):
    a = [(x >> i) & 1 for i in range(width)]
    b = [(y >> i) & 1 for i in range(width)]
    carry, cins, sums = 0, [], []
    for i in range(width):
        cins.append(carry)
        s, carry = full_adder(a[i], b[i], carry)
        sums.append(s)
    total = sum(s << i for i, s in enumerate(sums)) + (carry << width)
    xb, yb = format(x, "04b"), format(y, "04b")
    fig, ax = canvas(10.4, 4.6, 13, 6.0)
    title(ax, f"4-bit Ripple-Carry Adder: {x} + {y} = {xb}₂ + {yb}₂ = {total}  (carry วิ่งจากขวาไปซ้าย)")
    xs = [10.6 - i * 2.9 for i in range(width)]  # บิต 0 อยู่ขวาสุด
    for i in range(width):
        x0 = xs[i]
        ax.text(x0 + 0.35, 4.75, f"A{i}={a[i]}", ha="center", fontsize=10.5, fontweight="bold", color=BLUE)
        ax.text(x0 + 1.25, 4.75, f"B{i}={b[i]}", ha="center", fontsize=10.5, fontweight="bold", color=VIOLET)
        arrow(ax, (x0 + 0.35, 4.6), (x0 + 0.35, 3.75), color=BLUE)
        arrow(ax, (x0 + 1.25, 4.6), (x0 + 1.25, 3.75), color=VIOLET)
        hot = cins[i] == 1
        box(ax, x0, 2.35, 1.6, 1.4, f"FA บิต {i}", YELLOW_T if hot else AQUA_T, YELLOW if hot else AQUA, size=11, weight="bold")
        arrow(ax, (x0 + 0.8, 2.35), (x0 + 0.8, 1.45), color=INK)
        ax.text(x0 + 0.8, 1.05, f"S{i} = {sums[i]}", ha="center", fontsize=11, fontweight="bold")
        src = x0 + 2.9 if i > 0 else x0 + 2.3
        arrow(ax, (src, 3.05), (x0 + 1.6, 3.05), color=ORANGE, lw=1.8)
        ax.text((src + x0 + 1.6) / 2, 3.25, f"c={cins[i]}", ha="center", fontsize=10, color=ORANGE, fontweight="bold")
    ax.text(xs[0] + 1.75, 2.6, "Cin = 0", fontsize=9.5, color=ORANGE)
    arrow(ax, (xs[-1], 3.05), (xs[-1] - 0.7, 3.05), color=ORANGE, lw=1.8)
    ax.text(xs[-1] - 0.45, 2.45, f"Cout\n= {carry}", ha="center", fontsize=10, color=ORANGE, fontweight="bold")
    s_str = "".join(str(s) for s in reversed(sums))
    ax.text(0.2, 0.3, f"อ่านผลจากซ้าย (MSB) ไปขวา (LSB): Cout {carry} · S = {s_str}₂ = {int(s_str, 2)}"
            "   ·   กล่องสีเหลือง = มี carry เข้า", fontsize=10.5, color=INK2)
    save(fig, "w03-ripple-carry")


# ---------------------------------------------------------------- 3. von Neumann + fetch-decode-execute
def fde_cycle():
    regs = {"x1": 6, "x2": 7}
    pc = 0x100
    x3 = regs["x1"] + regs["x2"]
    fig, ax = canvas(10.4, 6.2, 13.2, 7.6)
    title(ax, "von Neumann + วงรอบ Fetch–Decode–Execute ของคำสั่ง RISC-V  add x3, x1, x2")
    box(ax, 0.2, 1.5, 6.4, 5.3, None, GRAY_T, MUTED)
    ax.text(0.45, 6.45, "CPU", fontsize=12, fontweight="bold", color=INK2)
    box(ax, 0.5, 4.75, 2.7, 1.3, "Control Unit\n(ถอดรหัสคำสั่ง)", VIOLET_T, VIOLET, size=10.5)
    box(ax, 3.6, 4.75, 2.7, 1.3, "ALU\n(คำนวณ/ตรรกะ)", ORANGE_T, ORANGE, size=10.5)
    ax.text(0.55, 4.3, "Registers", fontsize=10.5, fontweight="bold", color=BLUE, va="center")
    reg_rows = [("PC", f"0x{pc:X} → 0x{pc + 4:X}"), ("IR", "add x3,x1,x2"), ("x1", str(regs["x1"])),
                ("x2", str(regs["x2"])), ("x3", f"0 → {x3}")]
    for i, (r, v) in enumerate(reg_rows):
        col, row = i % 2, i // 2
        bx, by = 0.5 + col * 2.95, 3.4 - row * 0.62
        box(ax, bx, by, 2.8, 0.5, None, BLUE_T, BLUE)
        ax.text(bx + 0.15, by + 0.25, r, va="center", fontsize=10, fontweight="bold", color=BLUE)
        ax.text(bx + 0.7, by + 0.25, v, va="center", fontsize=10)
    box(ax, 9.0, 1.5, 4.0, 5.3, None, YELLOW_T, YELLOW)
    ax.text(9.2, 6.45, "Memory (คำสั่ง + ข้อมูลร่วมกัน)", fontsize=10.5, fontweight="bold", color=INK2)
    mem = [(f"0x{pc:X}", "add x3, x1, x2", True), (f"0x{pc + 4:X}", "คำสั่งถัดไป", False),
           ("…", "…", False), ("0x2000", "ข้อมูล เช่น คะแนน", False)]
    for i, (addr, val, hl) in enumerate(mem):
        by = 5.55 - i * 0.85
        box(ax, 9.25, by, 3.5, 0.65, None, ORANGE_T if hl else "white", ORANGE if hl else YELLOW)
        ax.text(9.4, by + 0.32, addr, va="center", fontsize=10, color=INK2, fontweight="bold")
        ax.text(10.5, by + 0.32, val, va="center", fontsize=10)
    ax.add_patch(Rectangle((6.6, 3.7), 2.4, 0.5, facecolor=GRAY_T, edgecolor=MUTED))
    ax.text(7.8, 3.95, "Bus", ha="center", va="center", fontsize=10.5, fontweight="bold", color=INK2)
    arrow(ax, (6.65, 4.4), (8.95, 4.4), color=MUTED, style="<|-|>")
    ax.text(7.8, 4.65, "ทางเดียวกัน\n= คอขวด", ha="center", fontsize=9.5, color=MUTED, va="bottom")
    steps = [("1 Fetch", f"อ่านคำสั่งที่ PC=0x{pc:X} → IR", BLUE),
             ("2 Decode", "CU แปล: x1 + x2 เก็บที่ x3", VIOLET),
             ("3 Execute", f"ALU: {regs['x1']} + {regs['x2']} = {x3}", ORANGE),
             ("4 Write back", f"x3 ← {x3} · PC ← PC + 4", AQUA)]
    for k, (h, d, c) in enumerate(steps):
        bx = 0.2 + k * 3.25
        box(ax, bx, 0.2, 3.05, 1.05, None, "white", c)
        ax.text(bx + 0.15, 0.95, h, fontsize=10.5, fontweight="bold", color=c, va="center")
        ax.text(bx + 0.15, 0.5, d, fontsize=9.5, color=INK2, va="center")
        if k < 3:
            arrow(ax, (bx + 3.05, 0.72), (bx + 3.25, 0.72), color=MUTED)
    ax.text(7.8, 2.2, "↺ วนซ้ำ\nทุกคำสั่ง", ha="center", fontsize=9.5, color=MUTED)
    save(fig, "w03-fde-cycle")


if __name__ == "__main__":
    adders()
    ripple_carry()
    fde_cycle()
