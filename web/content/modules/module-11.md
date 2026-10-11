## คำถามนำ
อุปกรณ์ขนาดเล็กสื่อสารกับ cloud และ dashboard ได้อย่างไร?

## ผลลัพธ์การเรียนรู้ย่อย
1. เข้าใจ embedded system, sensor, actuator และ microcontroller
2. อธิบาย IoT architecture แบบ device-edge-cloud
3. ใช้ MQTT publish/subscribe เป็นรูปแบบสื่อสาร

## แก่นความรู้ที่ต้องเข้าใจ
- embedded system คือคอมพิวเตอร์ที่ฝังอยู่ในอุปกรณ์เพื่อทำงานเฉพาะ เช่นอ่าน sensor และควบคุม actuator
- IoT รวม device, connectivity, backend, dashboard และ security เข้าด้วยกัน
- MQTT เป็น protocol แบบ publish/subscribe ที่เบา เหมาะกับอุปกรณ์และเครือข่ายจำกัด

## เนื้อหาเรียนรู้
- เริ่มด้วยวงจร sensor → microcontroller → network → server → dashboard แล้วถามว่าข้อมูลผิดพลาดหรือหลุดได้ที่จุดใดบ้าง
- อธิบาย MQTT ผ่านบทบาท broker, publisher, subscriber, topic และ QoS เพื่อให้ผู้เรียนเห็นว่าการส่งข้อมูล sensor ไม่จำเป็นต้องเป็น request/response เสมอไป
- โยง TinyML และ edge AI: บางงาน เช่นตรวจจับเสียงหรือภาพเบื้องต้น สามารถทำบนอุปกรณ์เพื่อลด latency และลดข้อมูลที่ส่งออก

## กิจกรรมในชั้นเรียน / ปฏิบัติการ
ต่อ ESP32/Arduino อ่านค่า sensor แล้วส่งค่าแบบจำลองผ่าน MQTT topic ไปยัง dashboard หรือ broker local

## คำถามตรวจความเข้าใจ
1. sensor กับ actuator ต่างกันอย่างไร?
2. MQTT broker ทำหน้าที่อะไร?
3. ทำไม IoT ต้องคิดเรื่องพลังงานและ security ตั้งแต่ต้น?

## ชิ้นงาน / หลักฐานการเรียนรู้
- สรุปแนวคิด 1 หน้า หรือ concept map ของสัปดาห์นี้
- ผลกิจกรรม/โค้ด/diagram ตามโจทย์ประจำสัปดาห์
- คำตอบสะท้อนคิด: วันนี้เข้าใจอะไรเพิ่ม และยังสงสัยอะไร

## Research เพิ่มเติมและแหล่งอ้างอิง
**หัวข้อวิจัยเสริม:** Embedded systems, IoT และ MQTT

- MQTT เป็น OASIS standard แบบ lightweight publish/subscribe เหมาะกับ IoT เพราะรองรับอุปกรณ์และเครือข่ายที่มี resource จำกัด
- การสอน IoT ควรแยก device, connectivity, broker/backend, storage, dashboard และ security control เพื่อให้ผู้เรียนเห็น architecture ครบ
- QoS, retained messages, topic design และ authentication เป็นรายละเอียดที่ช่วยยกระดับจาก demo sensor ไปสู่ระบบที่เชื่อถือได้

**แหล่งอ้างอิงข้อมูล:**
- [MQTT.org: The Standard for IoT Messaging](https://mqtt.org/)
- [OASIS MQTT Version 5.0 Standard](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html)
- [Eclipse Mosquitto MQTT broker](https://mosquitto.org/)

## แหล่งค้นคว้าเพิ่มเติม
- [MQTT.org: The Standard for IoT Messaging](https://mqtt.org/)
- [ACM/IEEE Computer Engineering Curricula 2016](https://www.acm.org/binaries/content/assets/education/ce2016-final-report.pdf)

---

## 🗓️ แผนการสอนประจำสัปดาห์ (Teaching Plan)

> [!abstract] สาระสำคัญ
> ระบบฝังตัวคือคอมพิวเตอร์เฉพาะงานที่ฝังในอุปกรณ์ ทำงานเรียลไทม์ ใช้ทรัพยากร/พลังงานจำกัด เป็นรากฐานของ **IoT** และปัจจุบันรวมเข้ากับ AI ที่ขอบเครือข่าย ([TinyML และ Edge AI](/concept/tinyml-edge-ai))

### 🎯 วัตถุประสงค์การสอน (Learning Objectives)
1. ผู้เรียนออกแบบ/พัฒนาโปรแกรมสำหรับระบบฝังตัวขั้นพื้นฐานได้ — *CLO2*
2. ผู้เรียนเข้าใจสถาปัตยกรรมเครือข่าย IoT — *CLO2*
3. ผู้เรียนประยุกต์ใช้เซนเซอร์ร่วมกับ IoT Platform ได้ — *CLO4*

### 📝 สรุปเนื้อหาหัวข้อ (Topics Covered)
- สถาปัตยกรรมและการเขียนโปรแกรมไมโครคอนโทรลเลอร์ (MCU)
- โครงสร้าง IoT (Sensors → Edge processing → Cloud backend)
- โปรโตคอล IoT (MQTT, CoAP, Zigbee)
- กรณีศึกษา: สมาร์ทโฮม, เกษตรอัจฉริยะ, โรงงานอัจฉริยะ

### 📖 เนื้อหาโดยละเอียด
- **MCU:** CPU + หน่วยความจำ + I/O บนชิปเดียว (ESP32, Arduino/AVR, STM32)
- **คุณลักษณะ:** เรียลไทม์, ข้อจำกัดพลังงาน/หน่วยความจำ, ความน่าเชื่อถือสูง
- **I/O:** เซนเซอร์ (อุณหภูมิ/แสง/การเคลื่อนไหว) และแอกชูเอเตอร์ (มอเตอร์/รีเลย์)
- **IoT architecture:** อุปกรณ์ → เกตเวย์ → เครือข่าย ([สัปดาห์ที่ 6: Computer Networks & Internet](/module/06)) → คลาวด์ ([สัปดาห์ที่ 7: Data Center & Cloud Infrastructure](/module/07))

### 🔑 แนวคิดหลัก (Key Concepts)
[TinyML และ Edge AI](/concept/tinyml-edge-ai) · [RISC-V](/concept/risc-v) · [Edge Computing](/concept/edge-computing)

### 📈 แนวโน้มปัจจุบัน (2025–2026)
- **Edge AI & TinyML:** MCU รันโมเดล ML แบบเบาในเครื่อง ~70% ของงาน AI จะประมวลผลบนอุปกรณ์ขอบ; โมเดล MobileNetV3/EfficientNet-Lite/YOLO-Nano
- **[RISC-V](/concept/risc-v) มาแรง:** คาดมีคอร์ในตลาด >2 หมื่นล้านคอร์ ปี 2025 เช่น ESP32‑C6 (RISC‑V + Wi‑Fi 6)
- **ตลาดโต:** ชิป Edge AI ~7 พันล้านดอลลาร์ (2025) → ~57 พันล้าน (2030); ระบบฝังตัวรวม ~103 พันล้าน (2024) → >169 พันล้าน (2030)
- **ความปลอดภัย IoT:** จำนวนอุปกรณ์มหาศาลเพิ่มพื้นผิวโจมตี (เชื่อม [สัปดาห์ที่ 12: Cybersecurity & Trust Architecture](/module/12))

### 🧪 กิจกรรม/ปฏิบัติการ (OBE) — Lab 8
Lab 1 ชม. (การส่งข้อมูลผ่าน MQTT) + Project 1 ชม. (เขียนโค้ดรับส่งข้อมูลเซนเซอร์ขึ้น Dashboard) — **Module 3: IoT & Smart Systems**
> อ้างอิงจากแผน 4 โมดูล: ดูรายละเอียดเต็มที่ [กิจกรรมปฏิบัติการและโครงงาน](/docs/labs-projects)

### ❓ คำถามทบทวน
1. ระบบฝังตัวต่างจากคอมพิวเตอร์ทั่วไปอย่างไร 3 ข้อ
2. TinyML/Edge AI มีข้อดีอะไรเทียบกับการประมวลผลบนคลาวด์
3. วาดสถาปัตยกรรม IoT จากเซนเซอร์ถึงคลาวด์

### 📚 อ้างอิง (References)
- Marwedel, P. (2021). *Embedded System Design* (4th ed.). Springer.
- ACM/IEEE-CS CE2016 — Systems Resource Management & Embedded Systems.
- Livewire. *Latest Trends in Embedded Systems 2025.* [livewireindia.com](https://livewireindia.com/blog/latest-trends-in-embedded-systems-2025-ai-iot-edge-computing-smart-devices/)
- Evolute. *10 Embedded Systems Development Technology Trends in 2026.* [evolute.in](https://www.evolute.in/blog/10-embedded-systems-development-technology-trends-in-2026-driving-the-next-wave-of-smart-electronics/)

---

## 📚 เนื้อหาเชิงลึกประจำสัปดาห์ (Deep Dive)

- [01. สถาปัตยกรรมและการเขียนโปรแกรมไมโครคอนโทรลเลอร์](/module/11/01)
- [02. โครงสร้าง IoT และเครือข่าย (IoT Architecture and Networking)](/module/11/02)
- [03. โปรโตคอล IoT: MQTT, CoAP และ Zigbee](/module/11/03)
- [04. TinyML และ Edge AI เบื้องต้น (Introduction to TinyML and Edge AI)](/module/11/04)
- [05. กรณีศึกษาเชิงเปรียบเทียบ: สมาร์ทโฮม (Smart Home) และ โรงงานอัจฉริยะ (Smart Factory)](/module/11/05)
