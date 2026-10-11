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

---

## 🗓️ แผนการสอนประจำสัปดาห์ (Teaching Plan)

> [!abstract] สาระสำคัญ
> คอมพิวเตอร์ทำงานเป็น **ชั้น (layers)**: ฮาร์ดแวร์ ↔ เฟิร์มแวร์/ระบบปฏิบัติการ ↔ ซอฟต์แวร์ประยุกต์ สัปดาห์นี้ยังเน้นแนวโน้มสำคัญคือ Edge Computing และ Green Computing

### 🎯 วัตถุประสงค์การสอน (Learning Objectives)
1. ผู้เรียนเข้าใจความสัมพันธ์และการทำงานร่วมกันระหว่างฮาร์ดแวร์และซอฟต์แวร์ — *CLO1*
2. ผู้เรียนรู้จักสถาปัตยกรรม [Edge Computing](/concept/edge-computing) และความสำคัญต่อระบบปัจจุบัน — *CLO1*
3. ผู้เรียนเข้าใจแนวคิด Green Computing และการประหยัดพลังงานในระบบคอมพิวเตอร์ — *CLO1*

### 📝 สรุปเนื้อหาหัวข้อ (Topics Covered)
- วิวัฒนาการของ Hardware และ Software Ecosystems
- สถาปัตยกรรม Edge Computing และความแตกต่างจาก Cloud Computing
- Green Computing: การออกแบบเพื่อความยั่งยืนและประหยัดพลังงาน

### 📖 เนื้อหาโดยละเอียด
- **องค์ประกอบฮาร์ดแวร์:** หน่วยประมวลผล (CPU/GPU/NPU — ดู [สัปดาห์ที่ 3: Digital Logic & Modern Processors](/module/03)), หน่วยความจำ (RAM/ROM), หน่วยเก็บข้อมูล (SSD/HDD), I/O, บัส
- **ลำดับชั้นหน่วยความจำ (memory hierarchy):** register → cache → RAM → storage (เร็ว–แพง–เล็ก → ช้า–ถูก–ใหญ่)
- **ประเภทซอฟต์แวร์:** ระบบ (OS, drivers, utilities) vs ประยุกต์
- **ระบบปฏิบัติการ (OS):** จัดการกระบวนการ/หน่วยความจำ/ไฟล์/อุปกรณ์ เป็นตัวกลางระหว่างโปรแกรมกับฮาร์ดแวร์
- **โอเพนซอร์ส vs proprietary:** โมเดลลิขสิทธิ์ เชื่อม [สัปดาห์ที่ 13: Computer Ethics & Intellectual Property](/module/13)

### 🔑 แนวคิดหลัก (Key Concepts)
[Edge Computing](/concept/edge-computing) · ดูธีม [Green Computing และความยั่งยืน](/docs/theme-green), [Edge Computing และระบบกระจาย](/docs/theme-edge)

### 📈 แนวโน้มปัจจุบัน (2025–2026)
- **Heterogeneous computing:** ชิปรวม CPU+GPU+NPU บนแพ็กเกจเดียวเพื่อรองรับ on-device AI
- **คอนเทนเนอร์/เวอร์ชวลไลเซชัน:** ซอฟต์แวร์ deploy ผ่าน container (Docker) และคลาวด์ (เชื่อม [สัปดาห์ที่ 7: Data Center & Cloud Infrastructure](/module/07))
- **Green IT:** ประสิทธิภาพพลังงานกลายเป็นข้อกำหนดออกแบบ ไม่ใช่ทางเลือก

### 🧪 กิจกรรม/ปฏิบัติการ (OBE) — Lab 1
Lab 1 ชม. (ตรวจสอบสเปกฮาร์ดแวร์) + Project 1 ชม. (ทำระบบ Save/Load และเขียนโค้ดอ่านเขียนไฟล์) — **Module 1: Foundation & Programming**
> อ้างอิงจากแผน 4 โมดูล: ดูรายละเอียดเต็มที่ [กิจกรรมปฏิบัติการและโครงงาน](/docs/labs-projects)

### ❓ คำถามทบทวน
1. เรียงลำดับชั้นหน่วยความจำจากเร็วไปช้า พร้อมเหตุผล
2. OS ทำหน้าที่อะไรบ้าง 4 อย่าง
3. Edge Computing ต่างจาก Cloud Computing อย่างไร

### 📚 อ้างอิง (References)
- Patterson, D. A., & Hennessy, J. L. (2020). *Computer Organization and Design RISC-V Edition*. Morgan Kaufmann.
- Silberschatz, A., Galvin, P., & Gagne, G. *Operating System Concepts* (10th ed.). Wiley.
- Edge AI and Vision Alliance. *Key Trends Shaping the Semiconductor Industry in 2026.* [edge-ai-vision.com](https://www.edge-ai-vision.com/2026/04/key-trends-shaping-the-semiconductor-industry-in-2026/)

---

## 📚 เนื้อหาเชิงลึกประจำสัปดาห์ (Deep Dive)

- [01. สถาปัตยกรรมฮาร์ดแวร์สมัยใหม่ (Deep Dive)](/module/02/01)
- [02. ระบบปฏิบัติการและ Containers](/module/02/02)
- [03. สถาปัตยกรรม Edge Computing](/module/02/03)
- [04. การปฏิบัติเพื่อ Green Computing](/module/02/04)
- [05. Heterogeneous Computing (CPU + GPU + NPU)](/module/02/05)
