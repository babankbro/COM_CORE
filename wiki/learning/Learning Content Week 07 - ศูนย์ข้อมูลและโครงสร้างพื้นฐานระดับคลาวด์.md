---
type: learning
status: complete
week: 7
source_week: "Week 07 - Data Center & Cloud Infrastructure"
tags: [learning, week07, en-001-019]
created: "2026-08-03"
updated: "2026-08-03"
---

# Learning Content Week 07: ศูนย์ข้อมูลและโครงสร้างพื้นฐานระดับคลาวด์

> ใช้คู่กับ [[Week 07 - Data Center & Cloud Infrastructure]] สำหรับอ่านก่อนเรียน ทบทวนหลังเรียน และเตรียมกิจกรรมปฏิบัติการ

## คำถามนำ
บริการ cloud และ AI ต้องพึ่งพา data center อย่างไร?

## ผลลัพธ์การเรียนรู้ย่อย
1. อธิบายองค์ประกอบ data center
2. เข้าใจ virtualization, containerization, Docker/Kubernetes
3. ใช้ PUE เป็นตัวชี้วัดพลังงาน

## แก่นความรู้ที่ต้องเข้าใจ
- data center รวม compute, storage, network, power, cooling และ physical security เพื่อให้บริการต่อเนื่อง
- container ช่วยแพ็กแอปกับ dependencies ให้รันได้สม่ำเสมอหลาย environment ส่วน Kubernetes ช่วยจัดการ workload จำนวนมาก
- PUE คือพลังงานรวมของ data center หารด้วยพลังงาน IT ยิ่งใกล้ 1 ยิ่งมีประสิทธิภาพ

## เนื้อหาเรียนรู้
- เริ่มจากการเปรียบเทียบ server ห้องหนึ่งกับ hyperscale data center: สิ่งที่เพิ่มขึ้นคือ reliability, redundancy, cooling, monitoring และ automation
- อธิบาย container ด้วยภาพกล่องซอฟต์แวร์: ไม่ใช่ VM เต็มเครื่อง แต่เป็น process ที่แยกสภาพแวดล้อมและแชร์ kernel จึงเบากว่า
- เชื่อมกับ AI: workload ที่ใช้ GPU จำนวนมากทำให้ rack density และความร้อนสูงขึ้น การออกแบบพลังงานและ liquid cooling จึงกลายเป็นประเด็นวิศวกรรมหลัก

## กิจกรรมในชั้นเรียน / ปฏิบัติการ
ทดลองรันแอปง่าย ๆ ด้วย Docker แล้วคำนวณ PUE จากโจทย์ตัวอย่าง 3 กรณี

## คำถามตรวจความเข้าใจ
1. container ต่างจาก VM อย่างไร?
2. Kubernetes ช่วยจัดการอะไร?
3. PUE 1.8 กับ 1.2 บอกอะไรเกี่ยวกับ data center?

## ชิ้นงาน / หลักฐานการเรียนรู้
- สรุปแนวคิด 1 หน้า หรือ concept map ของสัปดาห์นี้
- ผลกิจกรรม/โค้ด/diagram ตามโจทย์ประจำสัปดาห์
- คำตอบสะท้อนคิด: วันนี้เข้าใจอะไรเพิ่ม และยังสงสัยอะไร

## Research เพิ่มเติมและแหล่งอ้างอิง
**หัวข้อวิจัยเสริม:** Cloud native, containers, Kubernetes และ PUE

- Docker อธิบาย container ว่าเป็นการ package code กับ dependencies ให้รันสม่ำเสมอในหลาย environment เหมาะใช้สอนก่อนขึ้น Kubernetes
- Kubernetes เป็น platform สำหรับจัดการ containerized workloads และ services แบบ declarative/automation เหมาะกับบทเรียน DevOps และ cloud infrastructure
- The Green Grid PUE ใช้เป็น metric มาตรฐานของ data center energy efficiency และเชื่อมกับการเพิ่มขึ้นของ AI workload ได้ดี

**แหล่งอ้างอิงข้อมูล:**
- [Docker Docs: What is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- [Kubernetes Documentation: Concepts](https://kubernetes.io/docs/concepts/)
- [The Green Grid: PUE Comprehensive Examination](https://www.thegreengrid.org/en/resources/library-and-tools/20-PUE%3A-A-Comprehensive-Examination-of-the-Metric)

## แหล่งค้นคว้าเพิ่มเติม
- [Docker Docs: What is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- [Kubernetes Docs: Concepts](https://kubernetes.io/docs/concepts/)
- [The Green Grid: PUE Comprehensive Examination](https://www.thegreengrid.org/en/resources/library-and-tools/20-PUE%3A-A-Comprehensive-Examination-of-the-Metric)

> กลับ [[Learning Content Index]] · ดูแผนสัปดาห์ที่ 7: [[Week 07 - Data Center & Cloud Infrastructure]]
