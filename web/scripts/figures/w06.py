"""Infographic สัปดาห์ที่ 6: เครือข่ายคอมพิวเตอร์และอินเทอร์เน็ต
1) w06-layer-stack   OSI 7 ชั้น ↔ TCP/IP 4 ชั้น พร้อม PDU และตัวอย่าง protocol/อุปกรณ์
2) w06-request-journey  ลำดับ DNS → TCP → TLS → HTTP เมื่อเปิดเว็บหนึ่งหน้า พร้อมเวลารวม
3) w06-nat           Private IP หลัง NAT ออกอินเทอร์เน็ตด้วย Public IP เดียว + ขนาดช่วง RFC 1918
"""
from _style import *  # noqa: F401,F403


# ---------------------------------------------------------------- 1
def layer_stack():
    fig, ax = canvas(11.6, 6.6, xlim=14.2, ylim=8.6)
    title(ax, "OSI 7 ชั้น เทียบ TCP/IP 4 ชั้น: แต่ละชั้นห่อข้อมูลเป็นหน่วย (PDU) ต่างกัน", x=0.1, y=8.25)

    osi = [  # (เลขชั้น, ชื่อ, PDU, ตัวอย่าง)
        (7, "Application", "Data", "HTTP/HTTPS · DNS · DHCP"),
        (6, "Presentation", "Data", "เข้ารหัส/แปลงรูปแบบ (TLS, JPEG)"),
        (5, "Session", "Data", "เปิด–คุม–ปิดการสนทนา"),
        (4, "Transport", "Segment / Datagram", "TCP · UDP · หมายเลขพอร์ต"),
        (3, "Network", "Packet", "IP · ICMP (ping) · Router"),
        (2, "Data Link", "Frame", "Ethernet · Wi-Fi · MAC · Switch"),
        (1, "Physical", "Bits", "สาย UTP · ใยแก้ว · คลื่นวิทยุ"),
    ]
    tcpip = [("Application", 7, 5, BLUE, BLUE_T), ("Transport", 4, 4, AQUA, AQUA_T),
             ("Internet", 3, 3, YELLOW, YELLOW_T), ("Link\n(Network Access)", 2, 1, VIOLET, VIOLET_T)]
    color_of = {}
    for name, top, bot, c, t in tcpip:
        for n in range(bot, top + 1):
            color_of[n] = (c, t)

    h, gap, y0 = 0.86, 0.12, 0.5
    ypos = {n: y0 + (n - 1) * (h + gap) for n in range(1, 8)}
    x_osi, w_osi = 1.0, 2.9
    x_tcp, w_tcp = 4.2, 2.5
    x_pdu, w_pdu = 7.0, 2.4
    x_ex = 9.7

    hy = ypos[7] + h + 0.18
    for x, txt in [(x_osi + w_osi / 2, "OSI (แบบอ้างอิง)"), (x_tcp + w_tcp / 2, "TCP/IP (ใช้จริง)"),
                   (x_pdu + w_pdu / 2, "PDU"), (x_ex + 2.1, "ตัวอย่าง protocol / อุปกรณ์")]:
        ax.text(x, hy, txt, ha="center", fontsize=10.5, fontweight="bold", color=INK2)

    for n, name, pdu, ex in osi:
        c, t = color_of[n]
        y = ypos[n]
        box(ax, x_osi, y, w_osi, h, "", t, c)
        ax.text(x_osi + 0.25, y + h / 2, str(n), ha="center", va="center", fontsize=12, fontweight="bold", color=c)
        ax.text(x_osi + 0.55, y + h / 2, name, va="center", fontsize=11)
        box(ax, x_pdu, y, w_pdu, h, pdu, "white", c, size=10.5)
        ax.text(x_ex, y + h / 2, ex, va="center", fontsize=10, color=INK2)

    for name, top, bot, c, t in tcpip:
        yb, yt = ypos[bot], ypos[top] + h
        box(ax, x_tcp, yb, w_tcp, yt - yb, name, t, c, size=11, weight="bold", color=c)

    # ลูกศร encapsulation / decapsulation
    arrow(ax, (0.45, ypos[7] + h), (0.45, ypos[1]), color=ORANGE, lw=2)
    ax.text(0.2, (ypos[7] + ypos[1] + h) / 2, "ผู้ส่ง: เติม header ทีละชั้น (encapsulation)",
            rotation=90, ha="center", va="center", fontsize=9.5, color=ORANGE)
    arrow(ax, (13.95, ypos[1]), (13.95, ypos[7] + h), color=AQUA, lw=2)
    ax.text(13.65, (ypos[7] + ypos[1] + h) / 2, "ผู้รับ: แกะ header ทีละชั้น (decapsulation)",
            rotation=90, ha="center", va="center", fontsize=9.5, color=AQUA)
    save(fig, "w06-layer-stack")


# ---------------------------------------------------------------- 2
def request_journey():
    rtt_dns, rtt_srv = 10, 20  # ms (ค่าสมมติ)
    steps = [  # (ผู้ส่ง, ผู้รับ, ข้อความ, สี)
        ("B", "D", "1) DNS query: game.example.ac.th = ?  (UDP 53)", VIOLET),
        ("D", "B", "DNS answer: 203.0.113.10", VIOLET),
        ("B", "S", "2) TCP SYN  → พอร์ต 443", AQUA),
        ("S", "B", "SYN-ACK", AQUA),
        ("B", "S", "ACK + 3) TLS ClientHello", YELLOW),
        ("S", "B", "TLS ServerHello + ใบรับรอง (certificate)", YELLOW),
        ("B", "S", "TLS Finished + 4) HTTP GET /", BLUE),
        ("S", "B", "HTTP 200 OK + HTML", BLUE),
    ]
    phases = [("DNS", rtt_dns, VIOLET), ("TCP handshake", rtt_srv, AQUA),
              ("TLS 1.3 handshake", rtt_srv, YELLOW), ("HTTP request/response", rtt_srv, BLUE)]
    total = sum(p[1] for p in phases)

    fig, ax = canvas(11.4, 7.4, xlim=13, ylim=9.4)
    title(ax, "เปิดเว็บหนึ่งหน้า: DNS → TCP → TLS → HTTP (เวลาไหลจากบนลงล่าง)", y=9.05)
    lanes = {"B": (1.6, "Browser\n(เครื่องเรา)", BLUE), "D": (5.4, "DNS Resolver", VIOLET),
             "S": (10.6, "Web Server\n203.0.113.10", ORANGE)}
    ytop, ybot = 7.6, 2.55
    for x, label, c in lanes.values():
        box(ax, x - 1.05, ytop, 2.1, 0.85, label, "white", c, size=10.5, weight="bold")
        ax.plot([x, x], [ybot, ytop], color=GRID, lw=2, zorder=0)
    dy = (ytop - 0.7 - ybot) / (len(steps) - 1)
    for i, (a, b, msg, c) in enumerate(steps):
        y = ytop - 0.7 - i * dy
        xa, xb = lanes[a][0], lanes[b][0]
        arrow(ax, (xa, y), (xb, y), color=c, lw=1.8)
        mid = 7.9 if {a, b} == {"B", "S"} else (xa + xb) / 2
        ax.text(mid, y + 0.1, msg, ha="center", va="bottom", fontsize=9.8, color=INK,
                bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none"))

    # แถบเวลาแยกตามช่วง
    ax.text(0.3, 1.85, f"เวลาก่อนได้ HTML (สมมติ RTT ถึง DNS = {rtt_dns} ms, ถึงเซิร์ฟเวอร์ = {rtt_srv} ms)",
            fontsize=10.5, fontweight="bold")
    x, scale = 0.3, 12.3 / total
    for name, ms, c in phases:
        w = ms * scale
        ax.add_patch(Rectangle((x, 0.75), w, 0.7, facecolor=c, edgecolor="white", linewidth=2))
        ax.text(x + w / 2, 1.1, f"{name}\n{ms} ms", ha="center", va="center", fontsize=9.8, color="white",
                fontweight="bold")
        x += w
    ax.text(12.6, 0.4, f"รวม ≈ {total} ms = {len(phases)} รอบไป–กลับ", ha="right", fontsize=10.5, color=INK2)
    save(fig, "w06-request-journey")


# ---------------------------------------------------------------- 3
def nat():
    fig, ax = canvas(11.6, 6.6, xlim=14, ylim=8.2)
    title(ax, "Private IP ใช้ซ้ำได้ในทุกบ้าน · Router ทำ NAT ให้ออกเน็ตด้วย Public IP เดียว", y=7.85)

    # LAN
    ax.add_patch(FancyBboxPatch((0.3, 2.9), 4.6, 4.3, boxstyle="round,pad=0.02,rounding_size=0.15",
                                facecolor=BLUE_T, edgecolor=BLUE, linewidth=1.5, linestyle="--"))
    ax.text(2.6, 6.85, "เครือข่ายบ้าน 192.168.1.0/24 (Private)", ha="center", fontsize=10.5, fontweight="bold", color=BLUE)
    hosts = [("PC", "192.168.1.10", 51000), ("มือถือ", "192.168.1.11", 52000), ("โน้ตบุ๊ก", "192.168.1.12", 53000)]
    pub_ip, pub_ports = "203.0.113.5", [40001, 40002, 40003]
    for i, (n, ip, port) in enumerate(hosts):
        y = 5.75 - i * 1.0
        box(ax, 0.6, y, 3.4, 0.75, f"{n}  {ip}", "white", BLUE, size=10)
        arrow(ax, (4.0, y + 0.37), (5.6, 4.85), color=BLUE, lw=1.2)

    box(ax, 5.6, 4.1, 2.6, 1.5, "Router + NAT", ORANGE_T, ORANGE, size=11, weight="bold")
    ax.text(6.9, 3.8, "ด้านใน 192.168.1.1", ha="center", fontsize=9.5, color=INK2)
    ax.text(6.9, 5.8, f"ด้านนอก {pub_ip}", ha="center", fontsize=9.5, color=ORANGE, fontweight="bold")
    arrow(ax, (8.2, 4.85), (10.0, 4.85), color=ORANGE, lw=2)

    ax.add_patch(FancyBboxPatch((10.0, 3.9), 3.7, 1.9, boxstyle="round,pad=0.02,rounding_size=0.4",
                                facecolor=GRAY_T, edgecolor=MUTED, linewidth=1.5))
    ax.text(11.85, 5.2, "อินเทอร์เน็ต (Public)", ha="center", fontsize=10.5, fontweight="bold")
    ax.text(11.85, 4.5, "เห็นแค่ " + pub_ip, ha="center", fontsize=10, color=INK2)

    # ตาราง NAT
    tx, ty = 5.2, 0.55
    ax.text(tx, 3.05, "ตาราง NAT (PAT) ใน Router", fontsize=10.5, fontweight="bold")
    cols = [("ภายใน (IP:พอร์ต)", 3.3), ("ภายนอก (IP:พอร์ต)", 3.3)]
    rows = [(f"{ip}:{p}", f"{pub_ip}:{q}") for (_, ip, p), q in zip(hosts, pub_ports)]
    rh = 0.55
    x = tx
    for (hdr, w) in cols:
        ax.add_patch(Rectangle((x, ty + rh * 3), w, rh, facecolor=ORANGE, edgecolor="white"))
        ax.text(x + w / 2, ty + rh * 3.5, hdr, ha="center", va="center", fontsize=9.8, color="white", fontweight="bold")
        x += w
    for r, (a, b) in enumerate(rows):
        y = ty + rh * (2 - r)
        for j, (val, (_, w)) in enumerate(zip((a, b), cols)):
            ax.add_patch(Rectangle((tx + j * 3.3, y), w, rh, facecolor="white" if r % 2 else ORANGE_T, edgecolor=GRID))
            ax.text(tx + j * 3.3 + w / 2, y + rh / 2, val, ha="center", va="center", fontsize=9.8)

    # ช่วง Private RFC 1918 (จำนวนที่อยู่คำนวณจาก prefix)
    ranges = [("10.0.0.0/8", 8), ("172.16.0.0/12", 12), ("192.168.0.0/16", 16)]
    ax.text(0.3, 2.35, "ช่วง Private (RFC 1918)", fontsize=10.5, fontweight="bold")
    for i, (cidr, p) in enumerate(ranges):
        y = 1.65 - i * 0.6
        ax.text(0.3, y, cidr, fontsize=10, color=BLUE, fontweight="bold")
        ax.text(2.55, y, f"{2 ** (32 - p):,} ที่อยู่", fontsize=10, color=INK2)
    ax.text(11.85, 3.0, f"IPv4 ทั้งหมด 2³² = {2 ** 32:,}\nไม่พอทุกอุปกรณ์ → NAT / IPv6", ha="center",
            fontsize=9.8, color=INK2)
    save(fig, "w06-nat")


if __name__ == "__main__":
    layer_stack()
    request_journey()
    nat()
