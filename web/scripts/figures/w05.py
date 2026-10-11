"""Infographic สัปดาห์ที่ 5: ฐานข้อมูลและการจัดการข้อมูลขนาดใหญ่
รัน: python scripts/make_week_figures.py 05
ตัวเลขในภาพ SQL pipeline คำนวณจริงด้วย sqlite3 จากข้อมูลนักศึกษา 15 คนชุดเดียวกับ Lab 05
"""
import sqlite3

import numpy as np
from _style import *  # noqa: F401,F403

STUDENTS = [  # (student_id, first_name, faculty, gpa) จาก student.csv ใน Lab 05
    ("65010001", "สมชาย", "วิศวกรรมศาสตร์", 3.25), ("65010002", "สมหญิง", "วิศวกรรมศาสตร์", 3.80),
    ("65010003", "มานี", "วิทยาศาสตร์", 3.45), ("65010004", "ปิติ", "วิทยาศาสตร์", 2.75),
    ("65010005", "ชูใจ", "บริหารธุรกิจ", 3.10), ("65010006", "วีระ", "บริหารธุรกิจ", 2.40),
    ("65010007", "กานดา", "วิศวกรรมศาสตร์", 3.55), ("65010008", "ธนา", "วิศวกรรมศาสตร์", 2.95),
    ("65010009", "นภา", "วิทยาศาสตร์", 3.90), ("65010010", "อนันต์", "บริหารธุรกิจ", 3.00),
    ("65010011", "พรทิพย์", "บริหารธุรกิจ", 3.65), ("65010012", "ณัฐพล", "วิศวกรรมศาสตร์", 2.60),
    ("65010013", "สุดา", "วิศวกรรมศาสตร์", 3.35), ("65010014", "กิตติ", "วิทยาศาสตร์", 3.70),
    ("65010015", "อรุณี", "วิทยาศาสตร์", 2.85),
]


# ---------------------------------------------------------------- 1. ER diagram
def er_diagram():
    fig, ax = canvas(10.4, 4.9, 13, 6.2)
    title(ax, "ER Diagram ระบบลงทะเบียน: M:N แตกเป็น 1:N สองเส้นผ่านตารางเชื่อม", y=5.85)

    def entity(x, y, name, cols, edge, fill, w=3.0):
        rh = 0.46
        h = rh * (len(cols) + 1) + 0.1
        ax.add_patch(Rectangle((x, y - h), w, h, facecolor="white", edgecolor=edge, linewidth=1.6))
        ax.add_patch(Rectangle((x, y - rh - 0.05), w, rh + 0.05, facecolor=edge, edgecolor=edge))
        ax.text(x + w / 2, y - rh / 2 - 0.02, name, ha="center", va="center", fontsize=12, fontweight="bold", color="white")
        for i, (key, col) in enumerate(cols):
            cy = y - rh * (i + 1.5) - 0.07
            if key:
                kc = YELLOW if key == "PK" else VIOLET
                bw = 0.62 if len(key) <= 2 else 1.0
                ax.add_patch(FancyBboxPatch((x + 0.12, cy - 0.15), bw, 0.3, boxstyle="round,pad=0.01,rounding_size=0.05",
                                            facecolor=YELLOW_T if key == "PK" else VIOLET_T, edgecolor=kc, linewidth=1))
                ax.text(x + 0.12 + bw / 2, cy, key, ha="center", va="center", fontsize=9.5,
                        fontweight="bold", color="#8a5d00" if key == "PK" else VIOLET)
            ax.text(x + (1.25 if any(len(k) > 2 for k, _ in cols) else 0.9), cy, col, va="center", fontsize=10.5, fontweight="bold" if key == "PK" else "normal")
        return h

    top = 5.0
    entity(0.2, top, "Student", [("PK", "student_id"), ("", "first_name"), ("", "faculty"), ("", "gpa")], BLUE, BLUE_T)
    entity(5.0, top, "Enrollment", [("PK FK", "student_id"), ("PK FK", "course_id"), ("", "grade")], VIOLET, VIOLET_T)
    entity(9.8, top, "Course", [("PK", "course_id"), ("", "title"), ("", "credits")], AQUA, AQUA_T)

    # เส้นความสัมพันธ์ 1:N
    yl = top - 0.46 * 1.5 - 0.07
    for (x1, x2, lab1, labn, c) in [(3.2, 5.0, "1", "N", BLUE), (9.8, 8.0, "1", "N", AQUA)]:
        ax.plot([x1, x2], [yl, yl], color=c, linewidth=2)
        sgn = 1 if x2 > x1 else -1
        ax.text(x1 + sgn * 0.18, yl + 0.13, lab1, fontsize=11, fontweight="bold", color=c, ha="center")
        ax.text(x2 - sgn * 0.18, yl + 0.13, labn, fontsize=11, fontweight="bold", color=c, ha="center")
        # ขาไก่ (crow's foot) ด้าน N
        for dy in (-0.16, 0, 0.16):
            ax.plot([x2 - sgn * 0.3, x2], [yl, yl + dy], color=c, linewidth=1.4)
    ax.text(4.1, yl - 0.75, "ลงได้\nหลายวิชา", ha="center", fontsize=9.5, color=INK2)
    ax.text(8.9, yl - 0.75, "มีผู้เรียน\nหลายคน", ha="center", fontsize=9.5, color=INK2)

    # คำอธิบายด้านล่าง
    notes = [
        (YELLOW_T, YELLOW, "PK", "ระบุแถวไม่ซ้ำ ห้ามว่าง (NOT NULL)"),
        (VIOLET_T, VIOLET, "FK", "ต้องอ้างค่าที่มีจริงในตารางแม่ (referential integrity)"),
    ]
    for i, (f, e, k, t) in enumerate(notes):
        y = 1.35 - i * 0.55
        ax.add_patch(FancyBboxPatch((0.25, y - 0.15), 0.62, 0.3, boxstyle="round,pad=0.01,rounding_size=0.05",
                                    facecolor=f, edgecolor=e, linewidth=1))
        ax.text(0.56, y, k, ha="center", va="center", fontsize=9.5, fontweight="bold", color="#8a5d00" if k == "PK" else VIOLET)
        ax.text(1.05, y, t, va="center", fontsize=10.5, color=INK2)
    ax.text(7.2, 1.35, "Enrollment ใช้ PK ผสม (student_id, course_id)", va="center", fontsize=10.5, color=INK2)
    ax.text(7.2, 0.8, "→ คนเดิมลงวิชาเดิมซ้ำไม่ได้ และเก็บ grade ของคู่นั้น", va="center", fontsize=10.5, color=INK2)
    save(fig, "w05-er-diagram")


# ---------------------------------------------------------------- 2. SQL logical order
def sql_pipeline():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE students (student_id TEXT PRIMARY KEY, first_name TEXT, faculty TEXT, gpa REAL)")
    conn.executemany("INSERT INTO students VALUES (?, ?, ?, ?)", STUDENTS)
    n_from = conn.execute("SELECT COUNT(*) FROM students").fetchone()[0]
    n_where = conn.execute("SELECT COUNT(*) FROM students WHERE gpa >= 3.0").fetchone()[0]
    n_groups = conn.execute("SELECT COUNT(DISTINCT faculty) FROM students WHERE gpa >= 3.0").fetchone()[0]
    sql = ("SELECT faculty, COUNT(*) AS n, ROUND(AVG(gpa), 2) AS avg_gpa FROM students "
           "WHERE gpa >= 3.0 GROUP BY faculty HAVING COUNT(*) >= 3 ORDER BY avg_gpa DESC")
    having_rows = conn.execute(sql).fetchall()
    final = conn.execute(sql + " LIMIT 2").fetchall()
    conn.close()

    fig, ax = canvas(10.4, 5.4, 13, 6.8)
    title(ax, "SQL เขียนเรียงแบบหนึ่ง แต่ฐานข้อมูลประมวลผลอีกลำดับหนึ่ง", y=6.45)
    stages = [
        ("1 FROM", "students", f"{n_from} แถว", BLUE_T, BLUE),
        ("2 WHERE", "gpa >= 3.0", f"{n_where} แถว", BLUE_T, BLUE),
        ("3 GROUP BY", "faculty", f"{n_groups} กลุ่ม", VIOLET_T, VIOLET),
        ("4 HAVING", "COUNT(*)\n>= 3", f"{len(having_rows)} กลุ่ม", VIOLET_T, VIOLET),
        ("5 SELECT", "faculty,\nn, avg_gpa", "คำนวณคอลัมน์", AQUA_T, AQUA),
        ("6 ORDER BY", "avg_gpa\nDESC", "เรียงใหม่", YELLOW_T, YELLOW),
        ("7 LIMIT", "2", f"{len(final)} แถว", ORANGE_T, ORANGE),
    ]
    w, gap, x0, y0, h = 1.7, 0.13, 0.12, 3.55, 1.95
    for i, (head, arg, out, fill, edge) in enumerate(stages):
        x = x0 + i * (w + gap)
        box(ax, x, y0, w, h, "", fill, edge)
        hc = "#8a5d00" if edge == YELLOW else edge
        ax.text(x + w / 2, y0 + h - 0.35, head, ha="center", fontsize=10.5, fontweight="bold", color=hc)
        ax.text(x + w / 2, y0 + h / 2 - 0.05, arg, ha="center", va="center", fontsize=9.5, color=INK2)
        ax.text(x + w / 2, y0 + 0.32, out, ha="center", fontsize=10.5, fontweight="bold")
        if i < len(stages) - 1:
            arrow(ax, (x + w - 0.02, y0 + h / 2), (x + w + gap + 0.02, y0 + h / 2), color=MUTED)
    ax.text(0.12, 3.05, "WHERE กรอง \"แถว\" ก่อนจัดกลุ่ม · HAVING กรอง \"กลุ่ม\" หลังรวมค่า · ตามมาตรฐาน alias จาก SELECT ใช้ใน WHERE ไม่ได้",
            fontsize=10, color=INK2)

    # ตารางผลลัพธ์
    ax.text(0.12, 2.45, "ผลลัพธ์ (รันจริงกับข้อมูล 15 คนของ Lab 05)", fontsize=11, fontweight="bold")
    cols = [("faculty", 3.2), ("n", 1.0), ("avg_gpa", 1.5)]
    tx, ty, rh = 0.12, 2.0, 0.46
    x = tx
    for name, cw in cols:
        ax.add_patch(Rectangle((x, ty - rh), cw, rh, facecolor=BLUE, edgecolor="white"))
        ax.text(x + 0.12, ty - rh / 2, name, va="center", fontsize=10.5, color="white", fontweight="bold")
        x += cw
    for r, row in enumerate(final):
        x = tx
        for (name, cw), v in zip(cols, row):
            y = ty - rh * (r + 2)
            ax.add_patch(Rectangle((x, y), cw, rh, facecolor="white" if r % 2 == 0 else GRAY_T, edgecolor=GRID))
            ax.text(x + 0.12, y + rh / 2, f"{v:.2f}" if isinstance(v, float) else str(v), va="center", fontsize=10.5)
            x += cw
    dropped = [r[0] for r in having_rows][len(final):]
    msg = f"กลุ่มที่ผ่าน HAVING แต่ถูก LIMIT ตัด: {', '.join(dropped)}" if dropped else "ไม่มีกลุ่มถูก LIMIT ตัด"
    ax.text(6.3, 1.55, msg, fontsize=10, color=INK2)
    ax.text(6.3, 1.05, "ลำดับการเขียน: SELECT → FROM → WHERE →", fontsize=10, color=MUTED)
    ax.text(6.3, 0.62, "GROUP BY → HAVING → ORDER BY → LIMIT", fontsize=10, color=MUTED)
    save(fig, "w05-sql-pipeline")
    return final


# ---------------------------------------------------------------- 3. Database families
def db_families():
    fig, ax = canvas(10.4, 5.6, 13, 7)
    title(ax, "เลือกฐานข้อมูลตาม \"รูปร่างของข้อมูล\" และ \"คำถามที่จะถาม\"", y=6.65)
    cols = [
        ("Relational (SQL)", BLUE, BLUE_T),
        ("NoSQL (Document)", ORANGE, ORANGE_T),
        ("Vector Database", VIOLET, VIOLET_T),
    ]
    rows = [
        ("รูปข้อมูล", ["ตาราง แถว/คอลัมน์\nschema ตายตัว", "เอกสาร JSON\nฟิลด์ยืดหยุ่น", "embedding\nเวกเตอร์หลายร้อยมิติ"]),
        ("ถามว่า", ["\"ตรงเงื่อนไขไหม\"\nWHERE / JOIN", "\"ขอเอกสารของ id นี้\"\nfind({...})", "\"อะไรความหมายใกล้สุด\"\ntop-k similarity"]),
        ("จุดแข็ง", ["ACID ความถูกต้อง\nความสัมพันธ์ชัด", "ขยายแนวนอน\nรับข้อมูลเยอะเร็ว", "semantic search\nหัวใจของ RAG"]),
        ("ตัวอย่าง", ["SQLite · PostgreSQL\nMySQL", "MongoDB\nFirestore", "pgvector · Milvus\nPinecone"]),
    ]
    lw, cw, x0 = 1.6, 3.55, 0.15
    yh = 4.95
    for j, (name, c, t) in enumerate(cols):
        x = x0 + lw + 0.1 + j * (cw + 0.12)
        box(ax, x, yh, cw, 1.15, "", t, c)
        ax.text(x + 0.18, yh + 0.57, name, va="center", fontsize=11.5, fontweight="bold", color=c)
        ix, iy = x + cw - 1.05, yh + 0.2  # ไอคอนเล็ก
        if j == 0:
            for r in range(3):
                for k in range(3):
                    ax.add_patch(Rectangle((ix + k * 0.28, iy + r * 0.25), 0.28, 0.25, facecolor="white" if r < 2 else c,
                                           edgecolor=c, linewidth=1))
        elif j == 1:
            ax.text(ix + 0.42, iy + 0.38, "{ }", ha="center", va="center", fontsize=17, fontweight="bold", color=c)
        else:
            rng = np.random.default_rng(5)
            for ang in rng.uniform(0.2, 1.4, 4):
                arrow(ax, (ix + 0.05, iy + 0.02), (ix + 0.05 + 0.75 * np.cos(ang), iy + 0.02 + 0.7 * np.sin(ang)),
                      color=c, lw=1.2)
    rh = 1.08
    for i, (rname, cells) in enumerate(rows):
        y = yh - 0.12 - (i + 1) * rh
        box(ax, x0, y, lw, rh - 0.1, rname, GRAY_T, MUTED, 11, "bold")
        for j, (name, c, t) in enumerate(cols):
            x = x0 + lw + 0.1 + j * (cw + 0.12)
            ax.add_patch(FancyBboxPatch((x, y), cw, rh - 0.1, boxstyle="round,pad=0.02,rounding_size=0.06",
                                        facecolor="white", edgecolor=t, linewidth=1.5))
            ax.text(x + cw / 2, y + (rh - 0.1) / 2, cells[j], ha="center", va="center", fontsize=10, color=INK2)
    ax.text(x0, 0.12, "ระบบจริงมักใช้ร่วมกัน (polyglot): SQL เก็บคะแนน · Document เก็บ log · Vector ค้นเอกสารให้ chatbot",
            fontsize=10, color=INK2)
    save(fig, "w05-db-families")


if __name__ == "__main__":
    er_diagram()
    sql_pipeline()
    db_families()
