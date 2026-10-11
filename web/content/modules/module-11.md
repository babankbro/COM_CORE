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

## 🧭 อธิบายเพิ่มเติม (ฉบับขยาย)

ส่วนนี้ขยายความจากหัวข้อเจาะลึก ([หัวข้อ 1](/module/11/01) ถึง [หัวข้อ 5](/module/11/05)) ด้วยภาพเปรียบเทียบในชีวิตประจำวันและตัวอย่างไล่ตามข้อมูลจริงหนึ่งค่า ตั้งแต่ sensor จนขึ้น dashboard เพื่อเตรียมพร้อมสำหรับ [Lab 11](/lab/11)

### 1. ภาพใหญ่: ระบบ IoT เหมือนระบบประสาทของร่างกาย

- **Sensor = ปลายประสาท** รับรู้อุณหภูมิ แสง หรือการเคลื่อนไหว แล้วแปลงเป็นสัญญาณไฟฟ้า ส่วน **actuator = กล้ามเนื้อ** เช่น รีเลย์ มอเตอร์ หรือ buzzer ที่ลงมือทำตามคำสั่ง
- **MCU = ไขสันหลัง** ตอบสนองแบบ reflex ได้ทันทีโดยไม่ต้องรอสมอง เช่น อุณหภูมิเกิน 40 °C ก็ตัดรีเลย์เองเลย
- **Edge/Fog gateway = สมองส่วนท้องถิ่น** สรุปข้อมูล กรองค่าผิดปกติ และตัดสินใจเร็วด้วย TinyML ก่อนส่งต่อ (ดู [Edge Computing](/concept/edge-computing) และ [TinyML และ Edge AI](/concept/tinyml-edge-ai))
- **Cloud และ application = สมองใหญ่** เก็บประวัติระยะยาว วิเคราะห์แนวโน้ม และแสดงผลให้มนุษย์ตัดสินใจ

![แผนภาพสถาปัตยกรรม IoT 4 ชั้น ได้แก่ Perception, Network, Edge/Fog และ Application & Cloud โดยข้อมูล sensor ไหลจากซ้ายไปขวา คำสั่งควบคุมไหลย้อนกลับ และมีแถบ security ครอบทุกชั้น](/images/weeks/w11-iot-layers.svg)

ข้อคิดสำคัญคือ "ข้อมูลไหลขึ้น คำสั่งไหลลง" และ security ต้องอยู่ทุกชั้น ไม่ได้อยู่แค่ที่ cloud

### 2. MCU คืออะไรในมุมฮาร์ดแวร์ และอ่าน sensor อย่างไร

MCU เป็น "คอมพิวเตอร์ทั้งเครื่องในชิปเดียว" ส่วน MPU เป็น "สมองที่ต้องต่ออวัยวะภายนอก" (RAM, storage) จึงต้องมี OS อย่าง Linux และใช้พลังงานมากกว่า

![ผังบล็อกเปรียบเทียบโมดูล ESP32 ที่รวม CPU, SRAM, วิทยุ Wi-Fi/Bluetooth และ peripheral ไว้ในชิปเดียว กับบอร์ด Raspberry Pi ที่ใช้ SoC แบบ MPU ต่อ RAM, microSD และ I/O ภายนอก](/images/weeks/w11-mcu-mpu.svg)

วิธีที่ MCU คุยกับ sensor มี 3 แบบหลัก:
- **GPIO แบบ digital** อ่านได้แค่ 0/1 เช่น PIR หรือปุ่มกด
- **ADC** แปลงแรงดัน analog เป็นตัวเลข ADC ของ ESP32 ละเอียด 12-bit จึงได้ค่า 0–4095 (แรงดันเข้าห้ามเกิน 3.3 V)
- **Bus สื่อสาร** เช่น [I2C Bus](/concept/i2c-bus) ใช้สายเพียง 2 เส้น (SDA ข้อมูล, SCL สัญญาณนาฬิกา) ต่อ sensor หลายตัวพ่วงกันได้ โดยแต่ละตัวมี address ของตัวเอง เช่น BME280 ใช้ 0x76 หรือ 0x77

**Polling กับ interrupt** ต่างกันเหมือน "เดินไปเปิดตู้จดหมายทุก 5 นาที" กับ "ติดกริ่งให้บุรุษไปรษณีย์กดเมื่อของมาถึง" polling เขียนง่ายแต่เปลือง CPU และพลังงาน ส่วน interrupt ตอบสนองทันทีและให้ MCU เข้า sleep ระหว่างรอได้

### 3. MQTT แบบเห็นภาพ: กระดานประกาศที่มีบรรณารักษ์คอยแจก

ลองนึกถึงห้องสมุดที่มีบรรณารักษ์ (broker) คนหนึ่ง ใครมีข่าว (publisher) ก็ส่งให้บรรณารักษ์พร้อมระบุหมวด (topic) ใครสนใจหมวดไหน (subscriber) ก็ลงชื่อไว้ บรรณารักษ์จะถ่ายสำเนาส่งให้ทุกคนที่ลงชื่อ ผู้ส่งกับผู้รับจึงไม่ต้องรู้จักหรือรู้ IP ของกัน

![แผนภาพ MQTT แสดง ESP32 สองตัว publish ไปยัง broker แล้ว broker ส่งต่อให้ dashboard ที่ subscribe ด้วย building5/+/temperature และแอปที่ subscribe ด้วย building5/EN301/# พร้อม topic tree ที่บอกว่า wildcard แต่ละแบบจับ topic ใดได้](/images/weeks/w11-mqtt-pubsub.svg)

ฟีเจอร์ 3 อย่างที่ทำให้ระบบจาก demo กลายเป็นระบบใช้งานจริง:
- **Retained message** = "ป้ายประกาศล่าสุดที่ติดค้างไว้" broker เก็บข้อความ retained ล่าสุดของแต่ละ topic ไว้ 1 ข้อความ ผู้ subscribe ใหม่จะได้ค่าล่าสุดทันทีโดยไม่ต้องรอรอบถัดไป
- **Last Will and Testament (LWT)** = "จดหมายสั่งเสีย" อุปกรณ์ฝากไว้ตอน CONNECT ถ้าหลุดแบบไม่บอกลา broker จะประกาศแทน เช่น `building5/EN301/status = offline`
- **Keep alive** = "สัญญาโทรเช็กชื่อ" ถ้า broker ไม่ได้ยินอะไรจาก client นานเกิน 1.5 เท่าของช่วง keep alive จะถือว่าหลุดและส่ง LWT

### 4. ตัวอย่างไล่ข้อมูล 1 ค่า: sensor → MQTT → dashboard

สถานการณ์: ESP32 ห้อง EN301 อ่านอุณหภูมิจาก BME280 ทุก 10 วินาที แล้วส่งขึ้น broker Mosquitto ในเครือข่ายภาควิชา

| ขั้น | เกิดอะไรขึ้น | รายละเอียดที่ควรสังเกต |
|---|---|---|
| 1 | MCU อ่าน BME280 ผ่าน I2C ที่ address 0x76 | ได้ค่าดิบแล้วแปลงเป็น 27.5 °C ตามสูตรชดเชย (compensation) ของ datasheet |
| 2 | จัดรูป payload | ส่งเป็นข้อความ `27.5` หรือ JSON `{"t":27.5,"ts":1760241600}` ถ้าต้องการ timestamp |
| 3 | PUBLISH ไปที่ `building5/EN301/temperature` ด้วย QoS 1, retain = true | ตาม MQTT 3.1.1 แพ็กเก็ตนี้ยาวเพียง 37 byte (header 2 + ความยาวชื่อ topic 2 + ชื่อ topic 27 + packet ID 2 + payload 4) |
| 4 | Broker ตอบ PUBACK | ถ้าไม่ได้ PUBACK (เช่น Wi-Fi หลุด) client ส่งซ้ำพร้อม flag DUP จึงอาจเกิดข้อมูลซ้ำได้ |
| 5 | Broker ส่งต่อให้ dashboard ที่ subscribe `building5/+/temperature` ด้วย QoS 0 | QoS ที่ใช้จริงขาไปผู้รับ = ค่าที่ต่ำกว่าระหว่าง QoS ตอน publish กับ QoS ตอน subscribe จึงเหลือ QoS 0 |
| 6 | Dashboard แสดงค่า และเก็บลงฐานข้อมูล time-series | ใช้ `ts` ตัดค่าซ้ำจาก QoS 1 ได้ และค่า retained ทำให้หน้าจอที่เพิ่งเปิดเห็น 27.5 ทันที |

บทเรียนจากตัวอย่างนี้: ความน่าเชื่อถือต้องออกแบบทั้งเส้นทาง การตั้ง QoS 2 ฝั่ง publisher จะไม่ช่วยถ้าผู้รับ subscribe ด้วย QoS 0

### 5. ตารางเปรียบเทียบ: เลือก QoS ให้เหมาะกับงาน

| QoS | การรับประกัน | แพ็กเก็ตต่อ 1 ข้อความ | ข้อเสีย | เหมาะกับ |
|---|---|---|---|---|
| 0 | at most once (อาจหาย) | PUBLISH (1) | ข้อมูลหายได้เมื่อเครือข่ายไม่เสถียร | ค่า sensor ที่ส่งถี่ เช่น อุณหภูมิทุก 10 วินาที |
| 1 | at least once (อาจซ้ำ) | PUBLISH, PUBACK (2) | ผู้รับต้องรับมือข้อมูลซ้ำ | แจ้งเตือน, คำสั่งที่ทำซ้ำได้โดยไม่เสียหาย |
| 2 | exactly once | PUBLISH, PUBREC, PUBREL, PUBCOMP (4) | ช้าที่สุด ใช้ทรัพยากรมากที่สุด | คำสั่งที่ซ้ำแล้วเสียหาย เช่น ตัดยอดเงิน หรือนับจำนวนชิ้นงาน |

ส่วนการเลือกว่าจะประมวลผลที่ไหน ([หัวข้อ 4](/module/11/04)): ถ้าต้องตอบสนองในระดับมิลลิวินาทีหรือข้อมูลเป็นภาพ/เสียงปริมาณมาก ให้ทำบนอุปกรณ์หรือ edge ถ้าต้องดูแนวโน้มข้ามหลายอาคารหรือฝึกโมเดลใหม่ ให้ทำบน cloud

### สรุปสั้น

- IoT = Perception → Network → Edge/Fog → Application & Cloud ข้อมูลไหลขึ้น คำสั่งไหลลง และ security ต้องมีทุกชั้น
- MCU รวม CPU, หน่วยความจำ และ I/O ในชิปเดียว เหมาะกับงานควบคุม real-time ที่ใช้แบตเตอรี่ ส่วน MPU เหมาะกับ gateway ที่ต้องรัน Linux
- อ่าน sensor ได้ 3 ทาง: GPIO, ADC (ESP32 = 12-bit) และ bus เช่น I2C ที่ใช้ address แยกอุปกรณ์
- MQTT แยกผู้ส่งกับผู้รับด้วย broker และ topic โดย `+` แทน 1 ระดับ ส่วน `#` แทนทุกระดับที่เหลือ
- Retained, LWT และ keep alive ทำให้ dashboard รู้ทั้ง "ค่าล่าสุด" และ "อุปกรณ์ยังออนไลน์หรือไม่"
- QoS ที่ใช้จริงถูกจำกัดด้วยค่าที่ต่ำกว่าระหว่างฝั่ง publish กับฝั่ง subscribe

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
