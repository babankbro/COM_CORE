---
type: chapter
status: complete
week: 7
clo: [CLO2, CLO4]
tags: [curriculum, week07, data-center, cloud, pue, liquid-cooling]
created: "2026-06-30"
updated: "2026-06-30"
---

# สัปดาห์ที่ 7: ศูนย์ข้อมูลและโครงสร้างพื้นฐานระดับคลาวด์

> [!abstract] สาระสำคัญ
> ศูนย์ข้อมูล (Data Center) คือโรงงานประมวลผลของยุคดิจิทัล รวมเซิร์ฟเวอร์/สตอเรจ/เครือข่าย/ไฟฟ้า/ระบายความร้อน ให้บริการคลาวด์และ AI ต่อเนื่อง 24/7 การมาของ AI เปลี่ยนการออกแบบศูนย์ข้อมูลอย่างสิ้นเชิง

## 🎯 วัตถุประสงค์การสอน (Learning Objectives)
1. ผู้เรียนเข้าใจสถาปัตยกรรมศูนย์ข้อมูลและการจำลองเสมือน (Virtualization/Containerization) — *CLO2*
2. ผู้เรียนรู้จักแนวคิด Sovereign Cloud และอธิปไตยของข้อมูล — *CLO2*
3. ผู้เรียนเข้าใจการบริหารพลังงาน/ความร้อนใน Data Center ระดับ Hyperscale ([[PUE]], [[Liquid Cooling]]) — *CLO4*

## 📝 สรุปเนื้อหาหัวข้อ (Topics Covered)
- สถาปัตยกรรมศูนย์ข้อมูล + Virtualization/Containerization (Docker, Kubernetes)
- Public vs Private Cloud; Sovereign Cloud
- การจัดการความร้อน/พลังงานยุค AI ([[Liquid Cooling]], [[PUE]])

## 📖 เนื้อหาโดยละเอียด
- **องค์ประกอบ:** racks/servers, storage, networking, UPS/generator, ระบบทำความเย็น, การควบคุมการเข้าถึง
- **ตัวชี้วัด:** [[PUE]] = พลังงานรวม ÷ พลังงาน IT (ยิ่งใกล้ 1 ยิ่งดี); Tier I–IV; SLA
- **ความสัมพันธ์กับคลาวด์:** เป็นโครงสร้างพื้นฐานของ IaaS/PaaS/SaaS (เชื่อม [[Week 06 - Computer Networks & Internet]])
- **Hyperscale vs Edge data center**

## 🔑 แนวคิดหลัก (Key Concepts)
[[PUE]] · [[Liquid Cooling]]

## 📈 แนวโน้มปัจจุบัน (2025–2026)
- **ภาระงาน AI ดันความหนาแน่นพุ่ง:** rack เดิม 10–20 kW ไม่พอ คลัสเตอร์ AI เกิน 100 kW มุ่งสู่ 300 kW+; คาดแตะ ~370 kW ในปี 2026
- **[[Liquid Cooling]] เป็นสิ่งจำเป็น:** ตลาด liquid cooling สำหรับ AI โตจาก ~3.2 พันล้าน (2025) สู่ ~17.8 พันล้านดอลลาร์ (2036)
- **พลังงานคือข้อจำกัดหลัก:** การใช้ไฟของบริษัท AI ชั้นนำอาจเพิ่มจาก ~118 TWh (2024) เป็น ~295 TWh (2030) — เชื่อมความยั่งยืนใน [[Week 13 - Computer Ethics & Intellectual Property]]
- ลด [[PUE]] จาก ~1.50 (อากาศ) เหลือ ~1.05 (immersion) ลดพลังงานรวม ~30%

## 🧪 กิจกรรม/ปฏิบัติการ (OBE)
Lab 1 ชม. (ทดลองใช้ Cloud/Docker เบื้องต้น) + Project 1 ชม. (Deploy เว็บแอปพลิเคชันขึ้นเซิร์ฟเวอร์) — **Module 2: Web Dev**
> อ้างอิงจากแผน 4 โมดูล: ดูรายละเอียดเต็มที่ [[กิจกรรมปฏิบัติการและโครงงาน]]
