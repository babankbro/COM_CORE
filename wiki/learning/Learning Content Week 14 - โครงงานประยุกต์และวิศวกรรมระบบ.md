---
type: learning
status: complete
week: 14
source_week: "Week 14 - Applied System Engineering & DevOps"
tags: [learning, week14, en-001-019]
created: "2026-08-03"
updated: "2026-08-03"
---

# Learning Content Week 14: โครงงานประยุกต์และวิศวกรรมระบบ

> ใช้คู่กับ [[Week 14 - Applied System Engineering & DevOps]] สำหรับอ่านก่อนเรียน ทบทวนหลังเรียน และเตรียมกิจกรรมปฏิบัติการ

## คำถามนำ
จะนำความรู้ทั้งรายวิชามาประกอบเป็นระบบที่สร้าง ทดสอบ และส่งมอบได้อย่างไร?

## ผลลัพธ์การเรียนรู้ย่อย
1. เข้าใจ SDLC, Agile, DevOps และ CI/CD
2. ออกแบบ architecture ของ capstone project
3. เชื่อม version control, testing, deployment และ monitoring

## แก่นความรู้ที่ต้องเข้าใจ
- SDLC ทำให้การพัฒนาระบบมีขั้นตอนตั้งแต่ requirement ถึง maintenance
- DevOps ลดช่องว่างระหว่างการพัฒนาและการปฏิบัติการด้วย automation, feedback และ ownership ร่วม
- CI/CD ทำให้ build-test-deploy ทำซ้ำได้และลดความเสี่ยงจากการส่งงานแบบ manual

## เนื้อหาเรียนรู้
- ให้ผู้เรียนแตกโครงงานเป็น requirement, architecture, backlog, task และ acceptance criteria เพื่อเปลี่ยนไอเดียเป็นแผนงาน
- สอน Git workflow ขั้นต่ำ: issue/task, branch, commit, pull request/review และ release tag เพื่อให้ทีมทำงานร่วมกันได้
- เชื่อม cloud-native: container ทำให้ส่งมอบ environment ได้ชัด ส่วน pipeline ช่วยให้ทุก commit ผ่าน test ก่อน deploy

## กิจกรรมในชั้นเรียน / ปฏิบัติการ
สร้าง CI/CD pipeline เบื้องต้นที่รัน lint/test และ deploy demo หรือ build artifact ของโครงงาน

## คำถามตรวจความเข้าใจ
1. Agile ต่างจาก waterfall อย่างไร?
2. CI กับ CD ต่างกันอย่างไร?
3. acceptance criteria ช่วยลดปัญหาอะไรในทีม?

## ชิ้นงาน / หลักฐานการเรียนรู้
- สรุปแนวคิด 1 หน้า หรือ concept map ของสัปดาห์นี้
- ผลกิจกรรม/โค้ด/diagram ตามโจทย์ประจำสัปดาห์
- คำตอบสะท้อนคิด: วันนี้เข้าใจอะไรเพิ่ม และยังสงสัยอะไร

## Research เพิ่มเติมและแหล่งอ้างอิง
**หัวข้อวิจัยเสริม:** DevOps, CI/CD และ cloud-native delivery

- DevOps ควรถูกสอนเป็น culture + automation + feedback loop ไม่ใช่แค่เครื่องมือ deploy
- CI/CD ควรมีขั้นตอนขั้นต่ำคือ version control, automated build, automated test, artifact, deploy และ rollback plan
- Cloud-native delivery เชื่อม Docker/Kubernetes/CNCF กับ observability และ security เช่น secret management, image scanning และ least privilege

**แหล่งอ้างอิงข้อมูล:**
- [Cloud Native Computing Foundation](https://www.cncf.io/)
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/concepts/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

## แหล่งค้นคว้าเพิ่มเติม
- [Docker Docs: What is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- [Kubernetes Docs: Concepts](https://kubernetes.io/docs/concepts/)
- [Cloud Native Computing Foundation](https://www.cncf.io/)

> กลับ [[Learning Content Index]] · ดูแผนสัปดาห์ที่ 14: [[Week 14 - Applied System Engineering & DevOps]]
