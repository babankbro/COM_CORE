---
type: learning
status: complete
week: 6
source_week: "Week 06 - Computer Networks & Internet"
tags: [learning, week06, en-001-019]
created: "2026-08-03"
updated: "2026-08-03"
---

# Learning Content Week 06: เครือข่ายคอมพิวเตอร์และอินเทอร์เน็ต

> ใช้คู่กับ [[Week 06 - Computer Networks & Internet]] สำหรับอ่านก่อนเรียน ทบทวนหลังเรียน และเตรียมกิจกรรมปฏิบัติการ

## คำถามนำ
ข้อมูลเดินทางจากเครื่องเราไปยังบริการบนอินเทอร์เน็ตผ่านชั้นใดบ้าง?

## ผลลัพธ์การเรียนรู้ย่อย
1. อธิบาย OSI/TCP-IP model
2. รู้จัก IP, TCP/UDP, DNS, HTTP/HTTPS และ subnet
3. เข้าใจ latency, edge network และ cloud-native networking

## แก่นความรู้ที่ต้องเข้าใจ
- TCP/IP เป็นกรอบคิดหลักของอินเทอร์เน็ต แบ่งบทบาทตั้งแต่ link, internet, transport ถึง application
- TCP เน้นความครบถ้วนและลำดับข้อมูล ส่วน UDP ลด overhead เหมาะกับงาน real-time บางประเภท
- IPv6 ตาม RFC 8200 เป็นมาตรฐานสำคัญสำหรับพื้นที่ address และการเติบโตของอินเทอร์เน็ต

## เนื้อหาเรียนรู้
- สอนด้วยการเปิดเว็บหนึ่งหน้า: DNS แปลงชื่อโดเมนเป็น IP, TCP/TLS สร้างการเชื่อมต่อ, HTTP ส่ง request/response, router ส่ง packet ผ่านหลายเครือข่าย
- ให้ผู้เรียนเห็นว่าเครือข่ายไม่ใช่แค่สายหรือ Wi-Fi แต่รวม protocol, addressing, routing, security และ performance
- โยง cloud-native: microservices จำนวนมากต้องสื่อสารกันผ่าน network ภายใน cluster ดังนั้น latency, retry, timeout และ observability กลายเป็นหัวข้อวิศวกรรมสำคัญ

## กิจกรรมในชั้นเรียน / ปฏิบัติการ
ใช้ ping, tracert/traceroute และ nslookup ตรวจเส้นทางไปยังเว็บหนึ่ง แล้วอธิบายผลด้วย TCP/IP model

## คำถามตรวจความเข้าใจ
1. DNS ทำหน้าที่อะไร?
2. TCP กับ UDP ต่างกันอย่างไร?
3. IPv6 แก้ข้อจำกัดสำคัญใดของ IPv4?

## ชิ้นงาน / หลักฐานการเรียนรู้
- สรุปแนวคิด 1 หน้า หรือ concept map ของสัปดาห์นี้
- ผลกิจกรรม/โค้ด/diagram ตามโจทย์ประจำสัปดาห์
- คำตอบสะท้อนคิด: วันนี้เข้าใจอะไรเพิ่ม และยังสงสัยอะไร

## Research เพิ่มเติมและแหล่งอ้างอิง
**หัวข้อวิจัยเสริม:** Internet standards, Wi-Fi 7 และ 5G-Advanced

- IETF RFC 8200 เป็นแหล่งหลักสำหรับ IPv6 ใช้สอนว่ามาตรฐานอินเทอร์เน็ตเกิดจาก consensus และ interoperability
- IEEE 802.11be-2024 หรือ Wi-Fi 7 เพิ่มเป้าหมาย throughput สูงมากและปรับ PHY/MAC เพื่อรองรับงาน latency ต่ำ เหมาะเชื่อมกับ real-time/edge applications
- 3GPP Release 18 เป็นจุดเริ่มของ 5G-Advanced มีแนวทางใช้ AI/ML ในเครือข่ายและเพิ่มความสามารถของ mobile network

**แหล่งอ้างอิงข้อมูล:**
- [IETF RFC 8200: IPv6 Specification](https://datatracker.ietf.org/doc/html/rfc8200)
- [IEEE 802.11be-2024](https://standards.ieee.org/ieee/802.11be/7516/)
- [3GPP Release 18 overview](https://www.3gpp.org/specifications-technologies/releases/release-18)

## แหล่งค้นคว้าเพิ่มเติม
- [IETF RFC 8200 IPv6 Specification](https://datatracker.ietf.org/doc/html/rfc8200)
- [Cloud Native Computing Foundation](https://www.cncf.io/)

> กลับ [[Learning Content Index]] · ดูแผนสัปดาห์ที่ 6: [[Week 06 - Computer Networks & Internet]]
