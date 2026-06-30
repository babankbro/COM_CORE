---
type: chapter
status: complete
week: 12
clo: [CLO1, CLO4]
tags: [curriculum, week12, security, zero-trust, owasp, cryptography]
created: "2026-06-30"
updated: "2026-06-30"
---

# สัปดาห์ที่ 12: ความปลอดภัยและสถาปัตยกรรมความน่าเชื่อถือ

> [!abstract] สาระสำคัญ
> ความปลอดภัยไซเบอร์มุ่งปกป้องระบบ/ข้อมูลตามหลัก [[CIA Triad]] ภัยคุกคามปัจจุบันรุนแรงขึ้นและถูกขับเคลื่อนด้วย AI ทั้งฝ่ายโจมตีและฝ่ายป้องกัน แนวทาง [[Zero-Trust Architecture]] เป็นมาตรฐานใหม่

## 🎯 วัตถุประสงค์การสอน (Learning Objectives)
1. ผู้เรียนเข้าใจหลักการพื้นฐานด้านความปลอดภัยไซเบอร์ ([[CIA Triad]]) — *CLO1*
2. ผู้เรียนเข้าใจสถาปัตยกรรม [[Zero-Trust Architecture]] ในองค์กรยุคใหม่ — *CLO1*
3. ผู้เรียนตระหนักถึง Digital Provenance เพื่อตรวจสอบที่มาของข้อมูลในยุคที่ AI สร้างเนื้อหาปลอมได้ — *CLO4*

## 📝 สรุปเนื้อหาหัวข้อ (Topics Covered)
- หลักความปลอดภัย ([[CIA Triad]]: Confidentiality, Integrity, Availability)
- วิทยาการรหัสลับเบื้องต้น (Cryptography)
- [[Zero-Trust Architecture]]: "ไม่เชื่อใจใคร ตรวจสอบทุกครั้ง"
- Digital Provenance & Watermarking: ตรวจสอบสื่อ/ซอฟต์แวร์ที่สร้างโดย AI (Deepfakes)

## 📖 เนื้อหาโดยละเอียด
- **หลักการ:** [[CIA Triad]], least privilege, defense in depth
- **ภัยคุกคาม:** มัลแวร์/แรนซัมแวร์, ฟิชชิง, social engineering, DDoS, SQL injection, MITM
- **กลไกป้องกัน:** การเข้ารหัส, MFA/2FA, ไฟร์วอลล์, IDS/IPS, การสำรองข้อมูล, IAM, patching
- **กรอบมาตรฐาน:** NIST CSF, ISO/IEC 27001, **OWASP Top 10**

## 🔑 แนวคิดหลัก (Key Concepts)
[[CIA Triad]] · [[Zero-Trust Architecture]] · ดูธีม [[ความปลอดภัยและสถาปัตยกรรมความน่าเชื่อถือ (ธีม)]]

## 📈 แนวโน้มปัจจุบัน (2025–2026)
- **ภัยที่ขับเคลื่อนด้วย AI:** ~87% ระบุว่าช่องโหว่ที่เกี่ยวกับ AI โตเร็วที่สุดในปี 2025
- **แรนซัมแวร์ยังครองอันดับ:** double-extortion (ขโมย+เข้ารหัส) เป็นมาตรฐาน
- **[[Zero-Trust Architecture]] เป็นกระแสหลัก:** ~96% ขององค์กรสนับสนุน
- **OWASP Top 10 for LLM:** เพิ่มความเสี่ยงเฉพาะ AI เช่น prompt injection, vector/embedding weaknesses (เชื่อม [[Week 10 - Generative AI & Modern Robotics]])

## 🧪 กิจกรรม/ปฏิบัติการ (OBE) — Lab 9
Lab 1 ชม. (เทคนิคเข้ารหัสผ่าน/ความปลอดภัย) + Project 1 ชม. (ประยุกต์ใช้ความปลอดภัยในระบบ IoT + นำเสนอ) — **Module 3: IoT & Smart Systems**
> อ้างอิงจากแผน 4 โมดูล: ดูรายละเอียดเต็มที่ [[กิจกรรมปฏิบัติการและโครงงาน]]

## ❓ คำถามทบทวน
1. อธิบาย CIA triad พร้อมตัวอย่างการละเมิดแต่ละด้าน
2. Zero Trust ต่างจากการป้องกันแบบ "ขอบเขตเครือข่าย" เดิมอย่างไร
3. ยกความเสี่ยงใน OWASP Top 10 for LLM มา 2 ข้อ

## 📚 อ้างอิง (References)
- Stallings, W. (2022). *Cryptography and Network Security* (8th ed.). Pearson.
- NIST. *SP 800-207, Zero Trust Architecture.*
- World Economic Forum. *Global Cybersecurity Outlook 2026.* [reports.weforum.org](https://reports.weforum.org/docs/WEF_Global_Cybersecurity_Outlook_2026.pdf)
- OWASP Foundation. *OWASP Top 10 & Top 10 for LLM.* [owasp.org](https://owasp.org/)
- Trend Micro. *2025 Cyber Risk Report.* [trendmicro.com](https://www.trendmicro.com/vinfo/us/security/news/threat-landscape/trend-2025-cyber-risk-report)

## 🔗 นำทาง
⬅️ [[Week 11 - Embedded Systems & IoT]] · ➡️ [[Week 13 - Computer Ethics & Intellectual Property]]
