---
type: chapter
status: complete
week: 11
clo: [CLO2, CLO4]
tags: [curriculum, week11, embedded, iot, edge-ai, tinyml, risc-v]
created: "2026-06-30"
updated: "2026-06-30"
---

# สัปดาห์ที่ 11: ระบบฝังตัวและอินเทอร์เน็ตของสรรพสิ่ง

> [!abstract] สาระสำคัญ
> ระบบฝังตัวคือคอมพิวเตอร์เฉพาะงานที่ฝังในอุปกรณ์ ทำงานเรียลไทม์ ใช้ทรัพยากร/พลังงานจำกัด เป็นรากฐานของ **IoT** และปัจจุบันรวมเข้ากับ AI ที่ขอบเครือข่าย ([[TinyML และ Edge AI]])

## 🎯 วัตถุประสงค์การสอน (Learning Objectives)
1. ผู้เรียนออกแบบ/พัฒนาโปรแกรมสำหรับระบบฝังตัวขั้นพื้นฐานได้ — *CLO2*
2. ผู้เรียนเข้าใจสถาปัตยกรรมเครือข่าย IoT — *CLO2*
3. ผู้เรียนประยุกต์ใช้เซนเซอร์ร่วมกับ IoT Platform ได้ — *CLO4*

## 📝 สรุปเนื้อหาหัวข้อ (Topics Covered)
- สถาปัตยกรรมและการเขียนโปรแกรมไมโครคอนโทรลเลอร์ (MCU)
- โครงสร้าง IoT (Sensors → Edge processing → Cloud backend)
- โปรโตคอล IoT (MQTT, CoAP, Zigbee)
- กรณีศึกษา: สมาร์ทโฮม, เกษตรอัจฉริยะ, โรงงานอัจฉริยะ

## 📖 เนื้อหาโดยละเอียด
- **MCU:** CPU + หน่วยความจำ + I/O บนชิปเดียว (ESP32, Arduino/AVR, STM32)
- **คุณลักษณะ:** เรียลไทม์, ข้อจำกัดพลังงาน/หน่วยความจำ, ความน่าเชื่อถือสูง
- **I/O:** เซนเซอร์ (อุณหภูมิ/แสง/การเคลื่อนไหว) และแอกชูเอเตอร์ (มอเตอร์/รีเลย์)
- **IoT architecture:** อุปกรณ์ → เกตเวย์ → เครือข่าย ([[Week 06 - Computer Networks & Internet]]) → คลาวด์ ([[Week 07 - Data Center & Cloud Infrastructure]])

## 🔑 แนวคิดหลัก (Key Concepts)
[[TinyML และ Edge AI]] · [[RISC-V]] · [[Edge Computing]]

## 📈 แนวโน้มปัจจุบัน (2025–2026)
- **Edge AI & TinyML:** MCU รันโมเดล ML แบบเบาในเครื่อง ~70% ของงาน AI จะประมวลผลบนอุปกรณ์ขอบ; โมเดล MobileNetV3/EfficientNet-Lite/YOLO-Nano
- **[[RISC-V]] มาแรง:** คาดมีคอร์ในตลาด >2 หมื่นล้านคอร์ ปี 2025 เช่น ESP32‑C6 (RISC‑V + Wi‑Fi 6)
- **ตลาดโต:** ชิป Edge AI ~7 พันล้านดอลลาร์ (2025) → ~57 พันล้าน (2030); ระบบฝังตัวรวม ~103 พันล้าน (2024) → >169 พันล้าน (2030)
- **ความปลอดภัย IoT:** จำนวนอุปกรณ์มหาศาลเพิ่มพื้นผิวโจมตี (เชื่อม [[Week 12 - Cybersecurity & Trust Architecture]])

## 🧪 กิจกรรม/ปฏิบัติการ (OBE) — Lab 8
Lab 1 ชม. (การส่งข้อมูลผ่าน MQTT) + Project 1 ชม. (เขียนโค้ดรับส่งข้อมูลเซนเซอร์ขึ้น Dashboard) — **Module 3: IoT & Smart Systems**
> อ้างอิงจากแผน 4 โมดูล: ดูรายละเอียดเต็มที่ [[กิจกรรมปฏิบัติการและโครงงาน]]

## ❓ คำถามทบทวน
1. ระบบฝังตัวต่างจากคอมพิวเตอร์ทั่วไปอย่างไร 3 ข้อ
2. TinyML/Edge AI มีข้อดีอะไรเทียบกับการประมวลผลบนคลาวด์
3. วาดสถาปัตยกรรม IoT จากเซนเซอร์ถึงคลาวด์

## 📚 อ้างอิง (References)
- Marwedel, P. (2021). *Embedded System Design* (4th ed.). Springer.
- ACM/IEEE-CS CE2016 — Systems Resource Management & Embedded Systems.
- Livewire. *Latest Trends in Embedded Systems 2025.* [livewireindia.com](https://livewireindia.com/blog/latest-trends-in-embedded-systems-2025-ai-iot-edge-computing-smart-devices/)
- Evolute. *10 Embedded Systems Development Technology Trends in 2026.* [evolute.in](https://www.evolute.in/blog/10-embedded-systems-development-technology-trends-in-2026-driving-the-next-wave-of-smart-electronics/)

## 🔗 นำทาง
⬅️ [[Week 10 - Generative AI & Modern Robotics]] · ➡️ [[Week 12 - Cybersecurity & Trust Architecture]]
