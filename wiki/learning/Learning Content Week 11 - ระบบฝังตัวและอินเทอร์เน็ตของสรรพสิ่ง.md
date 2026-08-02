---
type: learning
status: complete
week: 11
source_week: "Week 11 - Embedded Systems & IoT"
tags: [learning, week11, en-001-019]
created: "2026-08-03"
updated: "2026-08-03"
---

# Learning Content Week 11: ระบบฝังตัวและอินเทอร์เน็ตของสรรพสิ่ง

> ใช้คู่กับ [[Week 11 - Embedded Systems & IoT]] สำหรับอ่านก่อนเรียน ทบทวนหลังเรียน และเตรียมกิจกรรมปฏิบัติการ

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

> กลับ [[Learning Content Index]] · ดูแผนสัปดาห์ที่ 11: [[Week 11 - Embedded Systems & IoT]]
