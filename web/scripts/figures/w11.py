"""Infographic สัปดาห์ที่ 11: ระบบฝังตัวและ IoT
รัน: python scripts/make_week_figures.py 11
"""
from _style import *  # noqa: F401,F403


def iot_layers():
    """สถาปัตยกรรม IoT 4 ชั้น: Perception → Network → Edge/Fog → Application & Cloud"""
    fig, ax = canvas(12, 5.6, xlim=14, ylim=7)
    title(ax, "สถาปัตยกรรม IoT 4 ชั้น: ข้อมูลไหลขึ้น · คำสั่งไหลกลับ", y=6.6)
    cols = [
        ("1 · Perception", "อุปกรณ์ปลายทาง", ["sensor: อุณหภูมิ/แสง/PIR", "actuator: รีเลย์/มอเตอร์", "MCU เช่น ESP32", "อ่านผ่าน GPIO/ADC/I2C"], BLUE, BLUE_T),
        ("2 · Network", "ท่อขนส่งข้อมูล", ["PAN: BLE, Zigbee", "WLAN: Wi-Fi", "LPWAN: LoRa, NB-IoT", "ขนด้วย MQTT / CoAP"], VIOLET, VIOLET_T),
        ("3 · Edge / Fog", "เกตเวย์ใกล้อุปกรณ์", ["กรอง/รวมข้อมูล", "TinyML ตัดสินใจเร็ว", "buffer เมื่อเน็ตหลุด", "แปลงโปรโตคอล"], AQUA, AQUA_T),
        ("4 · Application & Cloud", "ประมวลผลและแสดงผล", ["MQTT broker", "ฐานข้อมูล time-series", "analytics / ML", "dashboard · แอปมือถือ"], ORANGE, ORANGE_T),
    ]
    w, gap, x0 = 2.95, 0.5, 0.3
    for i, (head, sub, items, edge, tint) in enumerate(cols):
        x = x0 + i * (w + gap)
        box(ax, x, 1.75, w, 4.1, "", tint, edge)
        ax.text(x + w / 2, 5.45, head, ha="center", fontsize=11.5, fontweight="bold", color=edge)
        ax.text(x + w / 2, 5.0, sub, ha="center", fontsize=10.5, color=INK2)
        for j, it in enumerate(items):
            ax.text(x + 0.2, 4.35 - j * 0.6, "• " + it, fontsize=10.5, va="center")
        if i < 3:
            xa, xb = x + w + 0.04, x + w + gap - 0.04
            arrow(ax, (xa, 4.0), (xb, 4.0), color=INK2, lw=2)
            arrow(ax, (xb, 2.6), (xa, 2.6), color=ORANGE, lw=1.6, ls="--")
    ax.text(0.3, 1.3, "→ ข้อมูล sensor ไหลขึ้น (telemetry)", fontsize=10.5, color=INK2)
    ax.text(5.2, 1.3, "⇠ คำสั่งควบคุมไหลกลับ (command) เช่น สั่งเปิดพัดลม", fontsize=10.5, color=ORANGE)
    box(ax, 0.3, 0.2, 13.3, 0.75, "Security ต้องมีทุกชั้น: secure boot · TLS · username/password หรือ certificate · ACL ราย topic · OTA update",
        GRAY_T, MUTED, size=10.5)
    save(fig, "w11-iot-layers")


def mqtt_pubsub():
    """MQTT publish/subscribe ผ่าน broker + topic tree กับ wildcard + และ #"""
    fig, ax = canvas(12, 7.2, xlim=14, ylim=9)
    title(ax, "MQTT: ผู้ส่งกับผู้รับไม่รู้จักกัน ทุกข้อความผ่าน broker ด้วยชื่อ topic", y=8.6)
    box(ax, 0.2, 6.4, 3.4, 1.2, "ESP32 ห้อง EN301\n(publisher)", BLUE_T, BLUE, size=10.5)
    box(ax, 0.2, 4.7, 3.4, 1.2, "ESP32 ห้อง EN302\n(publisher)", BLUE_T, BLUE, size=10.5)
    box(ax, 5.5, 5.0, 3.0, 2.3, "Broker\n(Mosquitto)\nจับคู่ topic\nแล้วกระจายต่อ", VIOLET_T, VIOLET, size=11, weight="bold")
    box(ax, 10.8, 6.4, 3.0, 1.2, "Dashboard\n(subscriber)", AQUA_T, AQUA, size=10.5)
    box(ax, 10.8, 4.7, 3.0, 1.2, "แอปผู้ดูแลห้อง EN301\n(subscriber)", AQUA_T, AQUA, size=10.5)
    arrow(ax, (3.65, 7.0), (5.45, 6.6), color=BLUE, lw=2)
    arrow(ax, (3.65, 5.3), (5.45, 5.6), color=BLUE, lw=2)
    ax.text(3.7, 7.35, "PUBLISH\nbuilding5/EN301/temperature", fontsize=9.5, color=BLUE, va="bottom")
    ax.text(3.7, 4.55, "PUBLISH\nbuilding5/EN302/temperature", fontsize=9.5, color=BLUE, va="top")
    arrow(ax, (8.55, 6.6), (10.75, 7.0), color=AQUA, lw=2)
    arrow(ax, (8.55, 5.6), (10.75, 5.3), color=AQUA, lw=2)
    ax.text(8.6, 7.35, "SUBSCRIBE\nbuilding5/+/temperature", fontsize=9.5, color=AQUA, va="bottom")
    ax.text(8.6, 4.55, "SUBSCRIBE\nbuilding5/EN301/#", fontsize=9.5, color=AQUA, va="top")
    # topic tree
    ax.add_patch(Rectangle((0.2, 0.15), 13.6, 3.35, facecolor=GRAY_T, edgecolor=GRID))
    ax.text(0.4, 3.15, "Topic tree (คั่นระดับด้วย / )", fontsize=11.5, fontweight="bold")
    root = (0.6, 1.7)
    box(ax, root[0], root[1] - 0.3, 1.9, 0.6, "building5", SURFACE, INK2, size=10.5)
    rooms = [("EN301", 2.45), ("EN302", 0.95)]
    leaves = {"EN301": [("temperature", 2.85, "+ และ #"), ("humidity", 2.05, "# เท่านั้น")],
              "EN302": [("temperature", 0.95, "+ เท่านั้น")]}
    for r, ry in rooms:
        box(ax, 3.4, ry - 0.3, 1.5, 0.6, r, SURFACE, INK2, size=10.5)
        arrow(ax, (root[0] + 1.9, root[1]), (3.4, ry), color=MUTED, style="-")
        for leaf, ly, tag in leaves[r]:
            box(ax, 5.8, ly - 0.28, 2.0, 0.56, leaf, SURFACE, INK2, size=10.5)
            arrow(ax, (4.9, ry), (5.8, ly), color=MUTED, style="-")
            ax.text(8.0, ly, "ตรงกับ " + tag, fontsize=10, va="center", color=INK2)
    ax.text(10.5, 2.75, "+  แทน 1 ระดับพอดี", fontsize=10.5, color=AQUA, fontweight="bold")
    ax.text(10.5, 2.25, "#  แทนระดับนี้และทุกระดับลูก", fontsize=10.5, color=VIOLET, fontweight="bold")
    ax.text(10.5, 1.8, "    (ต้องอยู่ท้าย filter)", fontsize=10, color=INK2)
    ax.text(10.5, 1.2, "building5/+ ไม่ตรงกับ", fontsize=10, color=ORANGE)
    ax.text(10.5, 0.75, "topic ที่มี 3 ระดับ", fontsize=10, color=ORANGE)
    save(fig, "w11-mqtt-pubsub")


def mcu_vs_mpu():
    """MCU (ESP32) รวมทุกอย่างในชิป เทียบ MPU (Raspberry Pi) ที่ต้องพึ่งชิปภายนอก"""
    fig, ax = canvas(12, 6.2, xlim=14, ylim=7.6)
    title(ax, "MCU เทียบ MPU: คอมพิวเตอร์ทั้งเครื่องในชิปเดียว กับ สมองที่ต้องต่ออวัยวะภายนอก", y=7.25, size=12)
    # MCU side
    ax.add_patch(FancyBboxPatch((0.2, 1.9), 6.4, 4.75, boxstyle="round,pad=0.02,rounding_size=0.1",
                                facecolor=SURFACE, edgecolor=BLUE, linewidth=1.5, linestyle="--"))
    ax.text(0.4, 6.3, "โมดูล ESP32-WROOM (MCU)", fontsize=11.5, fontweight="bold", color=BLUE)
    box(ax, 0.45, 2.15, 4.4, 3.85, "", BLUE_T, BLUE)
    ax.text(2.65, 5.7, "ชิป ESP32 (SoC)", ha="center", fontsize=10.5, fontweight="bold", color=BLUE)
    box(ax, 0.65, 4.5, 2.0, 0.95, "CPU Xtensa\ndual-core 240 MHz", SURFACE, BLUE, size=9.5)
    box(ax, 2.75, 4.5, 1.9, 0.95, "SRAM 520 KB\n+ ROM", SURFACE, BLUE, size=9.5)
    box(ax, 0.65, 3.4, 3.9, 0.85, "วิทยุ Wi-Fi 2.4 GHz + Bluetooth", SURFACE, BLUE, size=9.5)
    box(ax, 0.65, 2.35, 3.9, 0.85, "GPIO · ADC 12-bit · I2C · SPI · UART · PWM", SURFACE, BLUE, size=9.5)
    box(ax, 5.05, 3.4, 1.35, 1.3, "SPI Flash\n4 MB\n(โปรแกรม)", GRAY_T, MUTED, size=9.5)
    arrow(ax, (4.85, 4.05), (5.05, 4.05), color=MUTED, style="<->")
    # MPU side
    ax.add_patch(FancyBboxPatch((7.3, 1.9), 6.5, 4.75, boxstyle="round,pad=0.02,rounding_size=0.1",
                                facecolor=SURFACE, edgecolor=ORANGE, linewidth=1.5, linestyle="--"))
    ax.text(7.5, 6.3, "บอร์ด Raspberry Pi (MPU)", fontsize=11.5, fontweight="bold", color=ORANGE)
    box(ax, 9.4, 3.6, 2.35, 1.6, "SoC: CPU ARM\nCortex-A หลายคอร์\n+ GPU · GHz", ORANGE_T, ORANGE, size=9.5)
    ext = [("RAM ภายนอก\n(GB)", 7.55, 4.9), ("microSD\n(ระบบปฏิบัติการ)", 7.55, 2.3),
           ("Wi-Fi / USB /\nEthernet", 12.0, 4.9), ("GPIO header\n(ไม่มี ADC)", 12.0, 2.3)]
    for t, x, y in ext:
        box(ax, x, y, 1.6, 1.05, t, GRAY_T, MUTED, size=9.5)
        left = x < 9
        p = (x + 1.6, y + 0.52) if left else (x, y + 0.52)
        q = (9.4, 4.4) if left else (11.75, 4.4)
        arrow(ax, p, q, color=MUTED, style="<->")
    rows = [("ระบบปฏิบัติการ", "bare-metal / FreeRTOS", "Linux เต็มรูปแบบ"),
            ("เวลาบูต · พลังงาน", "ระดับ ms · deep sleep ระดับ µA", "หลายวินาที · หลายวัตต์"),
            ("เหมาะกับงาน", "อ่าน sensor/ควบคุม real-time ใช้แบตเตอรี่", "gateway, กล้อง+AI, เว็บเซิร์ฟเวอร์")]
    for i, (k, a, b) in enumerate(rows):
        y = 1.4 - i * 0.55
        ax.text(0.3, y, k, fontsize=10, fontweight="bold", color=INK2, va="center")
        ax.text(2.6, y, a, fontsize=10, color=BLUE, va="center")
        ax.text(8.2, y, b, fontsize=10, color=ORANGE, va="center")
    save(fig, "w11-mcu-mpu")


if __name__ == "__main__":
    iot_layers()
    mqtt_pubsub()
    mcu_vs_mpu()
