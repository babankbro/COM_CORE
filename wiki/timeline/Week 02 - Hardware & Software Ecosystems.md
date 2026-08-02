---
type: chapter
status: complete
week: 2
clo: [CLO1]
tags: [curriculum, week02, hardware, software, edge, green-computing]
created: "2026-06-30"
updated: "2026-06-30"
---

# สัปดาห์ที่ 2: ฮาร์ดแวร์ ซอฟต์แวร์ และระบบนิเวศสมัยใหม่

> [!abstract] สาระสำคัญ
> คอมพิวเตอร์ทำงานเป็น **ชั้น (layers)**: ฮาร์ดแวร์ ↔ เฟิร์มแวร์/ระบบปฏิบัติการ ↔ ซอฟต์แวร์ประยุกต์ สัปดาห์นี้ยังเน้นแนวโน้มสำคัญคือ Edge Computing และ Green Computing

## 🎯 วัตถุประสงค์การสอน (Learning Objectives)
1. ผู้เรียนเข้าใจความสัมพันธ์และการทำงานร่วมกันระหว่างฮาร์ดแวร์และซอฟต์แวร์ — *CLO1*
2. ผู้เรียนรู้จักสถาปัตยกรรม [[Edge Computing|Edge Computing]] และความสำคัญต่อระบบปัจจุบัน — *CLO1*
3. ผู้เรียนเข้าใจแนวคิด Green Computing และการประหยัดพลังงานในระบบคอมพิวเตอร์ — *CLO1*

## 📝 สรุปเนื้อหาหัวข้อ (Topics Covered)
- วิวัฒนาการของ Hardware และ Software Ecosystems
- สถาปัตยกรรม Edge Computing และความแตกต่างจาก Cloud Computing
- Green Computing: การออกแบบเพื่อความยั่งยืนและประหยัดพลังงาน

## 📖 เนื้อหาโดยละเอียด
- **องค์ประกอบฮาร์ดแวร์:** หน่วยประมวลผล (CPU/GPU/NPU — ดู [[Week 03 - Digital Logic & Modern Processors]]), หน่วยความจำ (RAM/ROM), หน่วยเก็บข้อมูล (SSD/HDD), I/O, บัส
- **ลำดับชั้นหน่วยความจำ (memory hierarchy):** register → cache → RAM → storage (เร็ว–แพง–เล็ก → ช้า–ถูก–ใหญ่)
- **ประเภทซอฟต์แวร์:** ระบบ (OS, drivers, utilities) vs ประยุกต์
- **ระบบปฏิบัติการ (OS):** จัดการกระบวนการ/หน่วยความจำ/ไฟล์/อุปกรณ์ เป็นตัวกลางระหว่างโปรแกรมกับฮาร์ดแวร์
- **โอเพนซอร์ส vs proprietary:** โมเดลลิขสิทธิ์ เชื่อม [[Week 13 - Computer Ethics & Intellectual Property]]

## 🔑 แนวคิดหลัก (Key Concepts)
[[Edge Computing]] · ดูธีม [[Green Computing และความยั่งยืน]], [[Edge Computing และระบบกระจาย]]

## 📈 แนวโน้มปัจจุบัน (2025–2026)
- **Heterogeneous computing:** ชิปรวม CPU+GPU+NPU บนแพ็กเกจเดียวเพื่อรองรับ on-device AI
- **คอนเทนเนอร์/เวอร์ชวลไลเซชัน:** ซอฟต์แวร์ deploy ผ่าน container (Docker) และคลาวด์ (เชื่อม [[Week 07 - Data Center & Cloud Infrastructure]])
- **Green IT:** ประสิทธิภาพพลังงานกลายเป็นข้อกำหนดออกแบบ ไม่ใช่ทางเลือก

## 🧪 กิจกรรม/ปฏิบัติการ (OBE) — Lab 1
Lab 1 ชม. (ตรวจสอบสเปกฮาร์ดแวร์) + Project 1 ชม. (ทำระบบ Save/Load และเขียนโค้ดอ่านเขียนไฟล์) — **Module 1: Foundation & Programming**
> อ้างอิงจากแผน 4 โมดูล: ดูรายละเอียดเต็มที่ [[กิจกรรมปฏิบัติการและโครงงาน]]

## ❓ คำถามทบทวน
1. เรียงลำดับชั้นหน่วยความจำจากเร็วไปช้า พร้อมเหตุผล
2. OS ทำหน้าที่อะไรบ้าง 4 อย่าง
3. Edge Computing ต่างจาก Cloud Computing อย่างไร

## 📚 อ้างอิง (References)
- Patterson, D. A., & Hennessy, J. L. (2020). *Computer Organization and Design RISC-V Edition*. Morgan Kaufmann.
- Silberschatz, A., Galvin, P., & Gagne, G. *Operating System Concepts* (10th ed.). Wiley.
- Edge AI and Vision Alliance. *Key Trends Shaping the Semiconductor Industry in 2026.* [edge-ai-vision.com](https://www.edge-ai-vision.com/2026/04/key-trends-shaping-the-semiconductor-industry-in-2026/)

## 🔗 นำทาง
⬅️ [[Week 01 - Introduction to CE & IT]] · ➡️ [[Week 03 - Digital Logic & Modern Processors]]