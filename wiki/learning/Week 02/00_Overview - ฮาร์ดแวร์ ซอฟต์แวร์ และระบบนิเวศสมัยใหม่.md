---
type: learning
status: complete
week: 2
source_week: "Week 02 - Hardware & Software Ecosystems"
tags: [learning, week02, en-001-019]
created: "2026-08-03"
updated: "2026-08-03"
---

# Learning Content Week 02: ฮาร์ดแวร์ ซอฟต์แวร์ และระบบนิเวศสมัยใหม่

> ใช้คู่กับ [[Week 02 - Hardware & Software Ecosystems]] สำหรับอ่านก่อนเรียน ทบทวนหลังเรียน และเตรียมกิจกรรมปฏิบัติการ

## คำถามนำ
โปรแกรมหนึ่งตัวทำงานผ่านชั้นฮาร์ดแวร์ ซอฟต์แวร์ และระบบปฏิบัติการอย่างไร?

## ผลลัพธ์การเรียนรู้ย่อย
1. อธิบายลำดับชั้น hardware-firmware-OS-application
2. เข้าใจ CPU/GPU/NPU, หน่วยความจำ, storage และ I/O
3. เชื่อม edge computing กับ green computing

## แก่นความรู้ที่ต้องเข้าใจ
- คอมพิวเตอร์ทำงานเป็นชั้น: hardware ให้ทรัพยากร, OS จัดการทรัพยากร, application แก้ปัญหาผู้ใช้
- memory hierarchy คือการแลกเปลี่ยนระหว่างความเร็ว ราคา และขนาด ตั้งแต่ register/cache/RAM/storage
- edge computing ย้ายการประมวลผลเข้าใกล้แหล่งข้อมูล ส่วน green computing ทำให้การออกแบบระบบต้องคิดเรื่องพลังงานตั้งแต่ต้น

## เนื้อหาเรียนรู้
- ให้เริ่มจากคำสั่งง่าย ๆ เช่นเปิดไฟล์หรือกดปุ่มในเกม แล้วตามรอยว่าคำสั่งเดินทางผ่าน application, system call, OS, driver, storage และ CPU อย่างไร
- เปรียบเทียบ CPU, GPU และ NPU ด้วยชนิดงาน: CPU เหมาะงานทั่วไปและควบคุมลำดับ, GPU เหมาะงานขนาน, NPU เหมาะ inference ของ AI บนอุปกรณ์
- โยงไปยังการออกแบบที่รับผิดชอบ: ถ้าระบบ AI ประมวลผลบน edge ได้ จะลด latency และลดการส่งข้อมูลบางส่วนขึ้น cloud แต่ต้องคุมพลังงาน ความร้อน และการอัปเดตซอฟต์แวร์ให้ดี

## กิจกรรมในชั้นเรียน / ปฏิบัติการ
ให้ผู้เรียนตรวจสเปกเครื่องตนเอง แล้วอธิบายว่า CPU, RAM, storage และ GPU/NPU ส่งผลต่อการเรียนเขียนโปรแกรม/AI อย่างไร

## คำถามตรวจความเข้าใจ
1. ทำไม cache เร็วกว่า RAM แต่มีขนาดเล็กกว่า?
2. OS ทำหน้าที่ใดระหว่างโปรแกรมกับฮาร์ดแวร์?
3. edge computing ช่วยลด latency ได้อย่างไร?

## ชิ้นงาน / หลักฐานการเรียนรู้
- สรุปแนวคิด 1 หน้า หรือ concept map ของสัปดาห์นี้
- ผลกิจกรรม/โค้ด/diagram ตามโจทย์ประจำสัปดาห์
- คำตอบสะท้อนคิด: วันนี้เข้าใจอะไรเพิ่ม และยังสงสัยอะไร

## Research เพิ่มเติมและแหล่งอ้างอิง
**หัวข้อวิจัยเสริม:** Hardware/software ecosystem, edge และพลังงาน

- ระบบสมัยใหม่มี heterogeneous computing: CPU ทำงานทั่วไป, GPU/NPU เร่งงานขนานและ AI inference ทำให้ผู้เรียนต้องอ่านสเปกเครื่องมากกว่าแค่ความเร็ว CPU
- Edge computing ลด latency และลดการส่งข้อมูลขึ้น cloud แต่เพิ่มโจทย์ด้าน update, security, observability และพลังงานของอุปกรณ์ปลายทาง
- Green computing ควรเชื่อมกับการเลือก hardware, power profile, sleep mode และการออกแบบ workload ไม่ใช่พูดเฉพาะการประหยัดไฟทั่วไป

**แหล่งอ้างอิงข้อมูล:**
- [ACM/IEEE Computer Engineering Curricula 2016](https://www.acm.org/binaries/content/assets/education/ce2016-final-report.pdf)
- [NIST Edge Computing definition and reference architecture](https://www.nist.gov/publications/fog-computing-conceptual-model)
- [The Green Grid](https://www.thegreengrid.org/home)

## แหล่งค้นคว้าเพิ่มเติม
- [ACM/IEEE Computer Engineering Curricula 2016](https://www.acm.org/binaries/content/assets/education/ce2016-final-report.pdf)
- [ACM/IEEE-CS/AAAI Computer Science Curricula 2023](https://dl.acm.org/doi/book/10.1145/3664191)

> กลับ [[Learning Content Index]] · ดูแผนสัปดาห์ที่ 2: [[Week 02 - Hardware & Software Ecosystems]]
