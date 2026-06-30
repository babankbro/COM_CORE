import os
import shutil

base_dir = r"d:\work\KSU\COM_CORE\wiki\labs"

modules = [
    "Module 1 - Foundation & Programming",
    "Module 2 - Web Development",
    "Module 3 - IoT & Smart Systems",
    "Module 4 - Computer Vision"
]

for m in modules:
    os.makedirs(os.path.join(base_dir, m), exist_ok=True)

lab_data = [
    # Module 1
    (modules[0], "Lab 01 - IDE Setup and Project Planning.md", 1, "การตั้งค่าเครื่องมือ IDE (Python) และวางแผน Mini-Project 1", 
     "ติดตั้ง Python, VS Code, Git และวางแผนทำ Automated Data Processor", "CLO1, CLO4"),
    (modules[0], "Lab 02 - Hardware Specs and Data Extraction.md", 2, "สำรวจสเปกฮาร์ดแวร์และเขียนโค้ดดึงข้อมูลระบบ",
     "ใช้ Python ดึงข้อมูล OS/Hardware และอ่าน/เขียนไฟล์ (I/O)", "CLO1, CLO3"),
    (modules[0], "Lab 03 - Logic Circuit and Data Processing.md", 3, "วงจรตรรกะและการประมวลผลข้อมูล",
     "จำลองวงจรด้วย Logisim และเขียนฟังก์ชัน Python เชิงตรรกะเบื้องต้น", "CLO2, CLO3"),
    (modules[0], "Lab 04 - Algorithm Flowchart and Module 1 Presentation.md", 4, "อัลกอริทึมและสรุป Mini-Project 1",
     "วิเคราะห์ Big-O วาด Flowchart และนำเสนอ Automated Data Processor", "CLO3, CLO6"),
     
    # Module 2
    (modules[1], "Lab 05 - Database Design and SQL.md", 5, "การออกแบบฐานข้อมูลเชิงสัมพันธ์",
     "ออกแบบ ER Diagram สร้างตาราง SQLite และดึงข้อมูลไปใช้ใน Python", "CLO3"),
    (modules[1], "Lab 06 - Network Simulation and API Router.md", 6, "เครือข่ายคอมพิวเตอร์และการสร้าง API",
     "ทดสอบ Ping/Traceroute และสร้าง API/Web Router (FastAPI/Express)", "CLO1, CLO4"),
    (modules[1], "Lab 07 - Cloud Deployment and Docker.md", 7, "สถาปัตยกรรมคลาวด์และการ Deploy",
     "บรรจุเว็บแอปด้วย Docker และทดลอง Deploy บน Cloud", "CLO2, CLO4"),
     
    # Module 3
    (modules[2], "Lab 09 - ML Basics and IoT Architecture.md", 9, "พื้นฐาน ML และสถาปัตยกรรม IoT",
     "รัน Linear Regression ง่ายๆ และวางผังสถาปัตยกรรม Smart Environment Monitor", "CLO1, CLO4"),
    (modules[2], "Lab 10 - GenAI API and ESP32 Sensors.md", 10, "GenAI และฮาร์ดแวร์ไมโครคอนโทรลเลอร์",
     "ดึง API ของ LLM มาใช้ และต่อวงจร ESP32/Arduino ร่วมกับเซนเซอร์", "CLO1, CLO4"),
    (modules[2], "Lab 11 - MQTT Data Transmission.md", 11, "การรับส่งข้อมูลผ่านโปรโตคอล MQTT",
     "เขียนโค้ด ESP32 ส่งข้อมูลไป Web Dashboard และรับกลับ", "CLO2, CLO4"),
    (modules[2], "Lab 12 - Security Implementation and Module 3 Presentation.md", 12, "ความปลอดภัยไซเบอร์และนำเสนอ IoT",
     "ทดสอบเพิ่มการเข้ารหัสข้อมูล / นำเสนอ Smart Environment Monitor", "CLO4, CLO5, CLO6"),
     
    # Module 4
    (modules[3], "Lab 13 - AI Bias and Object Detection.md", 13, "จริยธรรม AI และพื้นฐานวิทัศน์คอมพิวเตอร์",
     "วิเคราะห์อคติใน AI และดึงสตรีมภาพกล้องมาทำ Object Detection", "CLO4, CLO5"),
    (modules[3], "Lab 14 - CI-CD Pipeline and System Integration.md", 14, "การบูรณาการระบบและ DevOps",
     "ทดลองทำ CI/CD เบื้องต้น และผสาน CV เข้ากับ Web หรือ IoT ของเดิม", "CLO4, CLO6"),
    (modules[3], "Lab 15 - Final Integration and Presentation Prep.md", 15, "การเตรียมนำเสนอโครงงานประยุกต์รวม",
     "ปรับแต่งระบบ (Fine-tuning) และจัดทำสไลด์การดูงาน+ผลงาน Capstone", "CLO4, CLO6")
]

template = """---
type: lab
status: complete
course_code: EN-001-019
week: {week}
clo: [{clo}]
tags: [lab, week{week_padded}, {module_slug}]
created: "2026-06-30"
updated: "2026-06-30"
---

# 🧪 Lab {week_padded}: {title}

> **โมดูล:** {module_name} (Mini-Project {module_num})
> **เวลาที่ใช้:** 2 ชั่วโมง (ในห้องปฏิบัติการ) + เวลาศึกษาด้วยตนเอง

## 🎯 จุดประสงค์การทดลอง (Objectives)
- {desc}
- ประยุกต์ใช้ความรู้จากภาคทฤษฎี (สัปดาห์ที่ {week}) สู่การปฏิบัติจริง
- เสริมสร้างทักษะการทำงานกลุ่มผ่าน Mini-Project

## 🛠️ เครื่องมือที่ต้องใช้ (Prerequisites & Tools)
- เครื่องคอมพิวเตอร์และอินเทอร์เน็ต
- ซอฟต์แวร์/อุปกรณ์ประจำโมดูล

---

## 🕒 ส่วนที่ 1: ทฤษฎีประยุกต์ประจำสัปดาห์ (1 ชั่วโมง)

*(คำอธิบายขั้นตอนการทดลองเพื่อความเข้าใจกลไกหลักของสัปดาห์ เช่น การเขียนโค้ดตามแบบทดสอบ หรือการตั้งค่าระบบพื้นฐาน)*

1. ขั้นตอนที่ 1
2. ขั้นตอนที่ 2
3. บันทึกผลการสังเกต

---

## 🚀 ส่วนที่ 2: งานพัฒนา Mini-Project (1 ชั่วโมง + การบ้าน)

*(เชื่อมโยงความรู้ที่ได้จากส่วนที่ 1 นำไปประยุกต์ต่อยอดในโปรเจกต์กลุ่มระดับโมดูล)*

- **เป้าหมายสัปดาห์นี้:** นำสิ่งที่เรียนไปพัฒนาฟีเจอร์สำหรับ Mini-Project ประจำโมดูล
- **โจทย์:** (เช่น ออกแบบฐานข้อมูลสำหรับเว็บ, เพิ่มเซนเซอร์ให้กับบอร์ด เป็นต้น)
- มอบหมายงานภายในทีม

---

## 📝 เกณฑ์การส่งงานและการประเมิน (Deliverables & Rubric)
- ส่งรายงานความคืบหน้า (Progress Log) เป็นไฟล์ Markdown ผ่าน GitHub
- ส่งโค้ดต้นฉบับผ่าน Repository ของกลุ่ม
- ให้ฟีดแบ็กความสมบูรณ์โดยพิจารณาจากเกณฑ์ของ {clo}

## 🔗 ลิงก์ที่เกี่ยวข้อง
- ⬅️ กลับไปยังสารบัญ Lab: [[_index|สารบัญ Lab]]
- 📚 กลับไปยังเนื้อหาสัปดาห์: [[Week {week_padded}]]
"""

for mod, filename, week, title, desc, clo in lab_data:
    module_num = mod.split(" ")[1]
    module_slug = "module" + module_num
    content = template.format(
        week=week,
        week_padded=f"{week:02d}",
        clo=clo,
        module_slug=module_slug,
        module_name=mod,
        module_num=module_num,
        title=title,
        desc=desc
    )
    
    filepath = os.path.join(base_dir, mod, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Create _index.md
index_content = """---
type: meta
title: "Lab & Mini-Projects Index"
updated: "2026-06-30T12:00:00"
---

# 🧪 สารบัญใบงานปฏิบัติการ (Labs) & Mini-Projects

วิชานี้ใช้สถาปัตยกรรม 4 โมดูล (4 Mini-Projects) โดยแบ่งตามโฟลเดอร์ดังนี้:

## 🟩 Module 1: The Foundation & Programming (W1 - W4)
**เป้าหมาย:** สร้างโปรแกรมจัดการข้อมูลขนาดเล็ก (Automated Data Processor)
- [[Lab 01 - IDE Setup and Project Planning]]
- [[Lab 02 - Hardware Specs and Data Extraction]]
- [[Lab 03 - Logic Circuit and Data Processing]]
- [[Lab 04 - Algorithm Flowchart and Module 1 Presentation]]

## 🟦 Module 2: Web Development & Infrastructure (W5 - W7)
**เป้าหมาย:** สร้างแอปพลิเคชันผ่านเว็บเชื่อมฐานข้อมูล (Asset Management Web App)
- [[Lab 05 - Database Design and SQL]]
- [[Lab 06 - Network Simulation and API Router]]
- [[Lab 07 - Cloud Deployment and Docker]]

## 🟧 Module 3: IoT & Smart Systems (W9 - W12)
**เป้าหมาย:** ระบบเซนเซอร์และแผงควบคุมอัจฉริยะ (Smart Environment Monitor)
- [[Lab 09 - ML Basics and IoT Architecture]]
- [[Lab 10 - GenAI API and ESP32 Sensors]]
- [[Lab 11 - MQTT Data Transmission]]
- [[Lab 12 - Security Implementation and Module 3 Presentation]]

## 🟪 Module 4: Computer Vision & System Integration (W13 - W15)
**เป้าหมาย:** ตรวจจับวัตถุและบูรณาการผลงาน (AI Object Detection System)
- [[Lab 13 - AI Bias and Object Detection]]
- [[Lab 14 - CI-CD Pipeline and System Integration]]
- [[Lab 15 - Final Integration and Presentation Prep]]

*(อ้างอิง: [[กิจกรรมปฏิบัติการและโครงงาน]] และตารางหลักใน [[Timeline & Curriculum Map]])*
"""

with open(os.path.join(base_dir, '_index.md'), 'w', encoding='utf-8') as f:
    f.write(index_content)
