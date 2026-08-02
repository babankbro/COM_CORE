---
type: learning
status: complete
week: 9
source_week: "Week 09 - AI & Machine Learning Foundations"
tags: [learning, week09, en-001-019]
created: "2026-08-03"
updated: "2026-08-03"
---

# Learning Content Week 09: ปัญญาประดิษฐ์และการเรียนรู้ของเครื่อง

> ใช้คู่กับ [[Week 09 - AI & Machine Learning Foundations]] สำหรับอ่านก่อนเรียน ทบทวนหลังเรียน และเตรียมกิจกรรมปฏิบัติการ

## คำถามนำ
เครื่องเรียนรู้จากข้อมูลได้อย่างไร และทำไมการนำโมเดลไปใช้จริงต้องมี MLOps?

## ผลลัพธ์การเรียนรู้ย่อย
1. แยก AI, ML และ deep learning
2. เข้าใจ supervised/unsupervised/reinforcement learning
3. อธิบาย lifecycle ของโมเดลและ MLOps

## แก่นความรู้ที่ต้องเข้าใจ
- ML คือการสร้างโมเดลจากข้อมูลเพื่อทำนายหรือจัดกลุ่ม โดยไม่ได้เขียนกฎทุกข้อด้วยมือ
- คุณภาพข้อมูลส่งผลต่อคุณภาพโมเดลโดยตรง เพราะโมเดลเรียนรู้ pattern รวมถึง bias จากข้อมูล
- MLOps ทำให้การฝึก ประเมิน deploy และ monitor โมเดลเป็นกระบวนการที่ตรวจสอบซ้ำได้

## เนื้อหาเรียนรู้
- เริ่มจากโจทย์จำแนกผลไม้ด้วยน้ำหนักและสี แล้วอธิบาย feature, label, training data, model และ prediction
- เปรียบเทียบ supervised learning กับ unsupervised learning: แบบแรกมีคำตอบให้เรียน แบบหลังหาโครงสร้างหรือกลุ่มในข้อมูล
- NIST AI RMF ช่วยให้มอง AI ไม่ใช่แค่ความแม่นยำ แต่รวม validity, safety, security, fairness, accountability และ governance

## กิจกรรมในชั้นเรียน / ปฏิบัติการ
ใช้ dataset เล็ก ๆ ฝึก classification model แล้วบันทึก feature, metric, error case และข้อจำกัดของข้อมูล

## คำถามตรวจความเข้าใจ
1. training กับ inference ต่างกันอย่างไร?
2. bias เกิดได้จากจุดใดของ lifecycle?
3. ทำไมต้อง monitor โมเดลหลัง deploy?

## ชิ้นงาน / หลักฐานการเรียนรู้
- สรุปแนวคิด 1 หน้า หรือ concept map ของสัปดาห์นี้
- ผลกิจกรรม/โค้ด/diagram ตามโจทย์ประจำสัปดาห์
- คำตอบสะท้อนคิด: วันนี้เข้าใจอะไรเพิ่ม และยังสงสัยอะไร

## Research เพิ่มเติมและแหล่งอ้างอิง
**หัวข้อวิจัยเสริม:** AI/ML lifecycle และ AI risk

- NIST AI RMF เสนอกรอบ Govern, Map, Measure, Manage เพื่อจัดการความเสี่ยง AI ตลอด lifecycle ไม่ใช่ดูแค่ accuracy
- หัวข้อ MLOps ควรเน้น data quality, model versioning, evaluation, deployment, monitoring และ feedback loop
- ให้ผู้เรียนเชื่อม bias, hallucination, robustness และ privacy เข้ากับขั้นตอนข้อมูล/โมเดล/การนำไปใช้จริง

**แหล่งอ้างอิงข้อมูล:**
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST AI RMF 1.0 PDF](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf)
- [Google Cloud: MLOps architecture and lifecycle](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)

## แหล่งค้นคว้าเพิ่มเติม
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [ACM/IEEE-CS/AAAI Computer Science Curricula 2023](https://dl.acm.org/doi/book/10.1145/3664191)

> กลับ [[Learning Content Index]] · ดูแผนสัปดาห์ที่ 9: [[Week 09 - AI & Machine Learning Foundations]]
