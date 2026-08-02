---
type: learning
status: complete
week: 10
source_week: "Week 10 - Generative AI & Modern Robotics"
tags: [learning, week10, en-001-019]
created: "2026-08-03"
updated: "2026-08-03"
---

# Learning Content Week 10: Generative AI และวิทยาการหุ่นยนต์

> ใช้คู่กับ [[Week 10 - Generative AI & Modern Robotics]] สำหรับอ่านก่อนเรียน ทบทวนหลังเรียน และเตรียมกิจกรรมปฏิบัติการ

## คำถามนำ
Generative AI จากซอฟต์แวร์จะเชื่อมกับการลงมือทำในโลกจริงผ่านหุ่นยนต์ได้อย่างไร?

## ผลลัพธ์การเรียนรู้ย่อย
1. เข้าใจ token, embedding, prompt, LLM และ RAG
2. อธิบาย agentic AI และ sense-plan-act
3. วิเคราะห์ความเสี่ยงของ generative AI และ robotics

## แก่นความรู้ที่ต้องเข้าใจ
- LLM ทำนาย token ถัดไปจากบริบทขนาดใหญ่ จึงสร้างข้อความ โค้ด และคำอธิบายได้ แต่ไม่ได้รับประกันว่าถูกเสมอ
- RAG ลดปัญหาความรู้ไม่ทันสมัยด้วยการค้นเอกสารที่เกี่ยวข้องแล้วส่งเข้า prompt
- หุ่นยนต์ใช้วงจร sense-plan-act และเมื่อนำ LLM/AI เข้าไปช่วยวางแผน ต้องคุม safety และ verification เข้มขึ้น

## เนื้อหาเรียนรู้
- สอน LLM แบบไม่ลงคณิตหนัก: ข้อความถูกแปลงเป็น token, model ใช้บริบทเพื่อคาดการณ์, embedding ช่วยแทนความหมายในเชิงเวกเตอร์
- อธิบาย agentic AI ด้วยงานหลายขั้นตอน เช่นวางแผน ค้นข้อมูล เรียกเครื่องมือ เขียนไฟล์ และตรวจผล แต่ต้องมีขอบเขตสิทธิ์และ human oversight
- เชื่อม robotics: sensor รับโลกจริง, planner ตัดสินใจ, actuator ลงมือทำ ความผิดพลาดของ AI จึงอาจกลายเป็นความเสี่ยงทางกายภาพ

## กิจกรรมในชั้นเรียน / ปฏิบัติการ
ให้ผู้เรียนออกแบบ prompt + retrieval source สำหรับผู้ช่วยตอบคำถามรายวิชา แล้วระบุ guardrails อย่างน้อย 3 ข้อ

## คำถามตรวจความเข้าใจ
1. RAG ต่างจากการถาม LLM ตรง ๆ อย่างไร?
2. agentic AI ต้องมี control อะไร?
3. ความเสี่ยงของ AI ในหุ่นยนต์ต่างจาก chatbot อย่างไร?

## ชิ้นงาน / หลักฐานการเรียนรู้
- สรุปแนวคิด 1 หน้า หรือ concept map ของสัปดาห์นี้
- ผลกิจกรรม/โค้ด/diagram ตามโจทย์ประจำสัปดาห์
- คำตอบสะท้อนคิด: วันนี้เข้าใจอะไรเพิ่ม และยังสงสัยอะไร

## Research เพิ่มเติมและแหล่งอ้างอิง
**หัวข้อวิจัยเสริม:** Generative AI, RAG, agents และ governance

- NIST Generative AI Profile เป็น companion ของ AI RMF สำหรับความเสี่ยงเฉพาะ GenAI เช่น hallucination, misuse, synthetic content และ data/IP risk
- RAG ควรถูกสอนเป็น system pattern ที่รวม retrieval, ranking, prompt construction และ evaluation ไม่ใช่แค่เรียก LLM
- Agentic AI ต้องเพิ่ม guardrails เช่น tool permission, audit log, human approval, sandboxing และ failure recovery โดยเฉพาะเมื่อเชื่อมกับ robotics

**แหล่งอ้างอิงข้อมูล:**
- [NIST AI RMF Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
- [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [pgvector documentation](https://github.com/pgvector/pgvector)

## แหล่งค้นคว้าเพิ่มเติม
- [NIST AI RMF Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
- [pgvector: Vector similarity search for PostgreSQL](https://github.com/pgvector/pgvector)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

> กลับ [[Learning Content Index]] · ดูแผนสัปดาห์ที่ 10: [[Week 10 - Generative AI & Modern Robotics]]
