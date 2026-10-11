---
type: lab
status: complete
course_code: EN-001-019
week: 6
clo: [CLO1, CLO4]
tags: [lab, week06, module2]
created: "2026-06-30"
updated: "2026-10-12"
---

# 🧪 Lab 06: เครือข่ายคอมพิวเตอร์และการสร้าง API

> **โมดูล:** Module 2 - Web Development (Mini-Project 2)
> **เวลาที่ใช้:** 2 ชั่วโมง (ในห้องปฏิบัติการ) + เวลาศึกษาด้วยตนเอง

## 🎯 จุดประสงค์การทดลอง (Objectives)
- ทดสอบ Ping/Traceroute และสร้าง API/Web Router (FastAPI/Express)
- ประยุกต์ใช้ความรู้จากภาคทฤษฎี (สัปดาห์ที่ 6) สู่การปฏิบัติจริง
- เสริมสร้างทักษะการทำงานกลุ่มผ่าน Mini-Project

## 🛠️ เครื่องมือที่ต้องใช้ (Prerequisites & Tools)
- เครื่องคอมพิวเตอร์และอินเทอร์เน็ต
- Python 3.10+ และ Flask (หรือ FastAPI), curl, Terminal/Command Prompt

---

## 🕒 ส่วนที่ 1: ทดสอบเครือข่ายด้วยคำสั่งพื้นฐาน (1 ชั่วโมง)

ทบทวนทฤษฎีก่อนทำแล็บที่ [[Week 06 - Computer Networks & Internet]] และ [[TCP-IP Model]]

> [!note] เปิดหน้าต่างคำสั่ง
> - **Windows:** กด `Win + R` พิมพ์ `cmd` แล้ว Enter (หรือใช้ PowerShell)
> - **Linux/macOS:** เปิดโปรแกรม Terminal
>
> ตัวเลขในตัวอย่าง Output ด้านล่างเป็นค่าสมมติ ผลของนักศึกษาจะแตกต่างไปตามเครือข่ายที่ใช้

### ขั้นตอนที่ 1: ดูการตั้งค่าเครือข่ายของเครื่องตัวเอง

| ระบบ | คำสั่ง |
| :--- | :--- |
| Windows | `ipconfig /all` |
| Linux | `ip a` และ `ip route` (ดู Gateway) |
| macOS | `ifconfig` และ `netstat -nr` (ดู Gateway) |

```output
Wireless LAN adapter Wi-Fi:
   Physical Address. . . . . . . . . : 3C-52-82-AB-CD-EF
   DHCP Enabled. . . . . . . . . . . : Yes
   IPv4 Address. . . . . . . . . . . : 192.168.1.10(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.1.1
   DHCP Server . . . . . . . . . . . : 192.168.1.1
   DNS Servers . . . . . . . . . . . : 8.8.8.8
```

**บันทึก:** MAC Address, IPv4 Address, Subnet Mask, Default Gateway, DNS Server และระบุว่า IP ที่ได้เป็น Private หรือ Public (เทียบกับช่วง RFC 1918)

### ขั้นตอนที่ 2: ทดสอบการเชื่อมต่อด้วย `ping`

```bash
# Windows (ส่ง 4 ครั้งโดยอัตโนมัติ)
ping 192.168.1.1
ping 8.8.8.8
ping google.com

# Linux/macOS (ต้องกำหนดจำนวนครั้งด้วย -c ไม่เช่นนั้นจะ ping ไม่หยุด กด Ctrl+C เพื่อหยุด)
ping -c 4 8.8.8.8
```

```output
Reply from 8.8.8.8: bytes=32 time=21ms TTL=117
...
Ping statistics for 8.8.8.8:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 20ms, Maximum = 22ms, Average = 21ms
```

**บันทึก:** ค่า Average RTT และ % Packet Loss ของแต่ละปลายทาง (Gateway, 8.8.8.8, google.com)

### ขั้นตอนที่ 3: ดูเส้นทางด้วย `tracert` / `traceroute`

```bash
tracert google.com        # Windows
traceroute google.com     # Linux/macOS (บางระบบต้องติดตั้งก่อน)
```

```output
Tracing route to google.com [142.250.199.14] over a maximum of 30 hops:
  1     1 ms     1 ms     1 ms  192.168.1.1
  2     5 ms     4 ms     6 ms  10.120.0.1
  3     *        *        *     Request timed out.
  4    20 ms    21 ms    20 ms  142.250.199.14
Trace complete.
```

**บันทึก:** จำนวน Hop ทั้งหมด, IP ของ Hop แรก (ตรงกับ Default Gateway หรือไม่), Hop ที่มีเวลาเพิ่มขึ้นมากที่สุด

### ขั้นตอนที่ 4: สอบถาม DNS ด้วย `nslookup` / `dig`

```bash
nslookup ksu.ac.th
nslookup google.com 1.1.1.1    # ระบุให้ถาม DNS ของ Cloudflare
dig google.com +short          # Linux/macOS
```

```output
Server:  one.one.one.one
Address:  1.1.1.1

Non-authoritative answer:
Name:    google.com
Addresses:  2404:6800:4001:80e::200e
          142.250.199.14
```

**บันทึก:** IP ของแต่ละโดเมน และเปรียบเทียบว่าถาม DNS Server ต่างกันได้ IP เหมือนกันหรือไม่

### ตารางบันทึกผล

| รายการ | ผลที่ได้ |
| :--- | :--- |
| IPv4 / Subnet Mask / Gateway / DNS | |
| MAC Address | |
| ping Gateway (Avg RTT / Loss) | |
| ping 8.8.8.8 (Avg RTT / Loss) | |
| จำนวน Hop ไป google.com | |
| IP ของ ksu.ac.th และ google.com | |

### คำถามท้ายส่วนที่ 1
1. IP ของเครื่องนักศึกษาเป็น Private หรือ Public? อยู่ในช่วงใดของ RFC 1918?
2. ทำไม RTT ไปยัง Default Gateway จึงต่ำกว่า RTT ไปยัง 8.8.8.8?
3. ถ้า `ping 8.8.8.8` สำเร็จ แต่ `ping google.com` ขึ้นว่าหาโฮสต์ไม่พบ ปัญหาน่าจะอยู่ที่บริการใด?
4. เครื่องหมาย `*` ใน tracert หมายความว่าอะไร และแปลว่าเครือข่ายเสียเสมอหรือไม่?
5. ค่าใดใน `ipconfig /all` ที่ได้มาจาก DHCP? อธิบายขั้นตอน DORA สั้น ๆ

---

## 🚀 ส่วนที่ 2: Mini-Project 2 — REST API ของระบบจัดการครุภัณฑ์ (1 ชั่วโมง + การบ้าน)

- **เป้าหมายสัปดาห์นี้:** สร้าง Backend API อย่างง่ายสำหรับ **Asset Management Web App** (ต่อยอดจากการออกแบบฐานข้อมูลใน [[Lab 05 - Database Design and SQL]])
- **โจทย์:** สร้าง REST API ที่มีอย่างน้อย `GET /assets`, `GET /assets/<id>` และ `POST /assets` แล้วทดสอบด้วย `curl` และเบราว์เซอร์

### พื้นฐาน: HTTP Methods และ Status Codes

| Method | ความหมาย | ตัวอย่าง |
| :--- | :--- | :--- |
| `GET` | อ่านข้อมูล (ไม่เปลี่ยนแปลงข้อมูล) | `GET /assets` ดูครุภัณฑ์ทั้งหมด |
| `POST` | สร้างข้อมูลใหม่ | `POST /assets` เพิ่มครุภัณฑ์ |
| `PUT` / `PATCH` | แก้ไขข้อมูล (ทั้งหมด / บางส่วน) | `PUT /assets/1` |
| `DELETE` | ลบข้อมูล | `DELETE /assets/1` |

| Status Code | ความหมาย | เกิดเมื่อ |
| :--- | :--- | :--- |
| **200 OK** | สำเร็จ | `GET` ได้ข้อมูลกลับมา |
| **201 Created** | สร้างข้อมูลใหม่สำเร็จ | `POST` เพิ่มครุภัณฑ์ได้ |
| **400 Bad Request** | คำขอไม่ถูกต้อง | ส่ง JSON ไม่ครบฟิลด์ |
| **404 Not Found** | ไม่พบทรัพยากร | ขอ `/assets/999` ที่ไม่มีอยู่ |
| **500 Internal Server Error** | เซิร์ฟเวอร์ผิดพลาด | โค้ดฝั่งเซิร์ฟเวอร์มี Bug หรือฐานข้อมูลล่ม |

> [!tip] จำกลุ่มของ Status Code
> 2xx = สำเร็จ, 3xx = เปลี่ยนเส้นทาง, 4xx = ฝั่ง **Client** ผิด, 5xx = ฝั่ง **Server** ผิด

### ขั้นตอนที่ 1: ติดตั้ง Flask

```bash
mkdir asset-app
cd asset-app
python -m venv venv
# Windows: venv\Scripts\activate   |   Linux/macOS: source venv/bin/activate
pip install flask
```

### ขั้นตอนที่ 2: เขียนไฟล์ `app.py`

```python
from flask import Flask, jsonify, request

app = Flask(__name__)
app.json.ensure_ascii = False   # แสดงภาษาไทยใน JSON ตรง ๆ (Flask 2.3 ขึ้นไป)

# ข้อมูลตัวอย่าง (สัปดาห์นี้เก็บในหน่วยความจำก่อน ภายหลังเชื่อมกับฐานข้อมูลจริง)
assets = [
    {"id": 1, "name": "Notebook Dell", "room": "EN-301", "status": "ใช้งาน"},
    {"id": 2, "name": "Projector Epson", "room": "EN-302", "status": "ซ่อม"},
]

@app.get("/assets")
def list_assets():
    return jsonify(assets), 200                     # 200 OK

@app.get("/assets/<int:asset_id>")
def get_asset(asset_id):
    for a in assets:
        if a["id"] == asset_id:
            return jsonify(a), 200
    return jsonify({"error": "asset not found"}), 404   # 404 Not Found

@app.post("/assets")
def create_asset():
    data = request.get_json(silent=True)
    if not data or "name" not in data:
        return jsonify({"error": "name is required"}), 400
    new = {
        "id": max((a["id"] for a in assets), default=0) + 1,
        "name": data["name"],
        "room": data.get("room", "-"),
        "status": data.get("status", "ใช้งาน"),
    }
    assets.append(new)
    return jsonify(new), 201                        # 201 Created

if __name__ == "__main__":
    # host="0.0.0.0" ให้เครื่องอื่นใน LAN (และ Docker ใน Lab 07) เข้าถึงได้
    app.run(host="0.0.0.0", port=5000, debug=True)
```

**อธิบายโค้ด:** `@app.get` / `@app.post` คือการผูก **Route** (เส้นทาง URL + Method) เข้ากับฟังก์ชัน, `jsonify()` แปลง Python dict/list เป็น JSON, ค่าที่สองใน `return` คือ Status Code, ส่วน `<int:asset_id>` คือ Path Parameter ที่ Flask แปลงเป็นตัวเลขให้

### ขั้นตอนที่ 3: รันและทดสอบ

```bash
python app.py
```

```output
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.1.10:5000
```

เปิดเบราว์เซอร์ไปที่ `http://localhost:5000/assets` จะเห็น JSON รายการครุภัณฑ์ จากนั้นเปิด Terminal อีกหน้าต่างแล้วทดสอบด้วย `curl` (ตัวเลือก `-i` ให้แสดง Status Code ใน Header)

```bash
curl -i http://localhost:5000/assets/1
curl -i http://localhost:5000/assets/999
curl -i -X POST http://localhost:5000/assets -H "Content-Type: application/json" -d "{\"name\": \"Printer HP\", \"room\": \"EN-303\"}"
```

```output
HTTP/1.1 200 OK
Content-Type: application/json
{"id": 1, "name": "Notebook Dell", "room": "EN-301", "status": "ใช้งาน"}

HTTP/1.1 404 NOT FOUND
{"error": "asset not found"}

HTTP/1.1 201 CREATED
{"id": 3, "name": "Printer HP", "room": "EN-303", "status": "ใช้งาน"}
```

> [!note] curl บน Windows PowerShell
> ใน PowerShell รุ่นเก่า คำว่า `curl` อาจเป็นชื่อย่อของ `Invoke-WebRequest` ให้พิมพ์ `curl.exe` แทน หรือรันคำสั่งใน `cmd` ถ้าไม่ได้ตั้ง `ensure_ascii = False` ภาษาไทยจะแสดงเป็นรหัส `ใ...` ซึ่งยังเป็น JSON ที่ถูกต้อง

> [!tip] ทางเลือก: FastAPI
> ถ้าทีมเลือก FastAPI (`pip install fastapi uvicorn`) ให้รันด้วย `uvicorn app:app --host 0.0.0.0 --port 5000` และเปิด `http://localhost:5000/docs` จะได้หน้าทดสอบ API (Swagger UI) อัตโนมัติ

### งานมอบหมายในทีม
- **Backend:** เพิ่ม `PUT /assets/<id>` และ `DELETE /assets/<id>` พร้อม Status Code ที่เหมาะสม
- **Database:** วางแผนเชื่อม API กับตารางจาก Lab 05 (เช่น SQLite)
- **Tester/Docs:** เขียนตารางทดสอบ (Method, URL, Body, Status ที่คาดหวัง, Status ที่ได้จริง) ไว้ใน README

### คำถามท้ายส่วนที่ 2
1. ทำไม `POST /assets` จึงควรตอบ `201` แทน `200`?
2. ถ้าเรียก `GET /assets/999` แล้วได้ `500` แทน `404` แสดงว่าโค้ดมีปัญหาอะไร?
3. API ของเรารันที่พอร์ต 5000 ใช้ Transport Protocol ใด และเกี่ยวข้องกับ OSI Layer ใดบ้าง?
4. เพื่อนในห้องแล็บเดียวกันจะเรียก API ของเราได้ต้องใช้ URL อะไร (อ้างอิง IP จากส่วนที่ 1)?

---

## 📝 เกณฑ์การส่งงานและการประเมิน (Deliverables & Rubric)
- ส่งรายงานความคืบหน้า (Progress Log) เป็นไฟล์ Markdown ผ่าน GitHub
- ส่งโค้ดต้นฉบับผ่าน Repository ของกลุ่ม
- ให้ฟีดแบ็กความสมบูรณ์โดยพิจารณาจากเกณฑ์ของ CLO1, CLO4

## 🔗 ลิงก์ที่เกี่ยวข้อง
- ⬅️ กลับไปยังสารบัญ Lab: [[_index|สารบัญ Lab]]
- 📚 กลับไปยังเนื้อหาสัปดาห์: [[Week 06]]
