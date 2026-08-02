---
type: learning
status: complete
week: 12
source_week: "Week 12 - Cybersecurity & Trust Architecture"
tags: [learning, week12, en-001-019]
created: "2026-08-03"
updated: "2026-08-03"
---

# Learning Content Week 12: Cybersecurity และ Zero Trust

> ใช้คู่กับ [[Week 12 - Cybersecurity & Trust Architecture]] สำหรับอ่านก่อนเรียน ทบทวนหลังเรียน และเตรียมกิจกรรมปฏิบัติการ

## คำถามนำ
เราจะปกป้องระบบที่กระจายบน cloud, IoT และ AI ได้อย่างไร?

## ผลลัพธ์การเรียนรู้ย่อย
1. อธิบาย CIA triad และ threat พื้นฐาน
2. เข้าใจ least privilege, MFA, encryption และ secure coding
3. อธิบาย Zero Trust และ OWASP Top 10

## แก่นความรู้ที่ต้องเข้าใจ
- CIA triad คือ confidentiality, integrity, availability เป็นกรอบแรกในการคิดความปลอดภัย
- Zero Trust ย้ายจากการเชื่อใจเครือข่ายภายใน ไปสู่การตรวจสอบ identity, device, context และ policy ทุกครั้ง
- OWASP Top 10 เป็นเอกสาร awareness สำหรับความเสี่ยงเว็บแอปที่นักพัฒนาควรรู้

## เนื้อหาเรียนรู้
- เริ่มจาก incident สมมุติ เช่นเว็บแอปถูก SQL injection แล้วให้ผู้เรียนแยกว่า CIA ด้านใดเสียหายและควรป้องกันที่ชั้นใด
- อธิบาย defense-in-depth: ไม่มีมาตรการเดียวพอ ต้องรวม authentication, authorization, encryption, logging, backup และ patching
- NIST SP 800-207 ช่วยให้สอน Zero Trust เป็นสถาปัตยกรรม ไม่ใช่ผลิตภัณฑ์: ทุก request ต้องประเมินความเสี่ยงตาม policy ก่อนให้เข้าถึง resource

## กิจกรรมในชั้นเรียน / ปฏิบัติการ
ให้ผู้เรียนทำ threat model ของ IoT dashboard ในโครงงาน แล้วกำหนด control อย่างน้อย 5 รายการ

## คำถามตรวจความเข้าใจ
1. CIA triad แต่ละข้อมีตัวอย่างอะไร?
2. Zero Trust ต่างจาก perimeter security อย่างไร?
3. OWASP Top 10 ช่วยนักพัฒนาอย่างไร?

## ชิ้นงาน / หลักฐานการเรียนรู้
- สรุปแนวคิด 1 หน้า หรือ concept map ของสัปดาห์นี้
- ผลกิจกรรม/โค้ด/diagram ตามโจทย์ประจำสัปดาห์
- คำตอบสะท้อนคิด: วันนี้เข้าใจอะไรเพิ่ม และยังสงสัยอะไร

## Research เพิ่มเติมและแหล่งอ้างอิง
**หัวข้อวิจัยเสริม:** Zero Trust, OWASP และ secure design

- NIST SP 800-207 อธิบาย Zero Trust เป็นสถาปัตยกรรมที่ย้ายจุดเน้นจาก network perimeter ไปที่ users, assets และ resources
- OWASP Top 10 เป็น awareness baseline สำหรับนักพัฒนาเว็บ และควรโยงกับ secure coding เช่น access control, injection และ cryptographic failures
- สำหรับระบบ AI/IoT ควรเพิ่ม OWASP LLM risks และ device security เพราะ attack surface ขยายจากเว็บไปยัง prompt, model, vector store และ sensor/device

**แหล่งอ้างอิงข้อมูล:**
- [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
- [OWASP Top 10 Web Application Security Risks](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

## แหล่งค้นคว้าเพิ่มเติม
- [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
- [OWASP Top 10 Web Application Security Risks](https://owasp.org/www-project-top-ten/)

> กลับ [[Learning Content Index]] · ดูแผนสัปดาห์ที่ 12: [[Week 12 - Cybersecurity & Trust Architecture]]
