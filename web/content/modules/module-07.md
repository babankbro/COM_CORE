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

---

## 🗓️ แผนการสอนประจำสัปดาห์ (Teaching Plan)

> [!abstract] สาระสำคัญ
> ศูนย์ข้อมูล (Data Center) คือโรงงานประมวลผลของยุคดิจิทัล รวมเซิร์ฟเวอร์/สตอเรจ/เครือข่าย/ไฟฟ้า/ระบายความร้อน ให้บริการคลาวด์และ AI ต่อเนื่อง 24/7 การมาของ AI เปลี่ยนการออกแบบศูนย์ข้อมูลอย่างสิ้นเชิง

### 🎯 วัตถุประสงค์การสอน (Learning Objectives)
1. ผู้เรียนเข้าใจสถาปัตยกรรมศูนย์ข้อมูลและการจำลองเสมือน (Virtualization/Containerization) — *CLO2*
2. ผู้เรียนรู้จักแนวคิด Sovereign Cloud และอธิปไตยของข้อมูล — *CLO2*
3. ผู้เรียนเข้าใจการบริหารพลังงาน/ความร้อนใน Data Center ระดับ Hyperscale ([PUE](/concept/pue), [Liquid Cooling](/concept/liquid-cooling)) — *CLO4*

### 📝 สรุปเนื้อหาหัวข้อ (Topics Covered)
- สถาปัตยกรรมศูนย์ข้อมูล + Virtualization/Containerization (Docker, Kubernetes)
- Public vs Private Cloud; Sovereign Cloud
- การจัดการความร้อน/พลังงานยุค AI ([Liquid Cooling](/concept/liquid-cooling), [PUE](/concept/pue))

### 📖 เนื้อหาโดยละเอียด
- **องค์ประกอบ:** racks/servers, storage, networking, UPS/generator, ระบบทำความเย็น, การควบคุมการเข้าถึง
- **ตัวชี้วัด:** [PUE](/concept/pue) = พลังงานรวม ÷ พลังงาน IT (ยิ่งใกล้ 1 ยิ่งดี); Tier I–IV; SLA
- **ความสัมพันธ์กับคลาวด์:** เป็นโครงสร้างพื้นฐานของ IaaS/PaaS/SaaS (เชื่อม [สัปดาห์ที่ 6: Computer Networks & Internet](/module/06))
- **Hyperscale vs Edge data center**

### 🔑 แนวคิดหลัก (Key Concepts)
[PUE](/concept/pue) · [Liquid Cooling](/concept/liquid-cooling)

### 📈 แนวโน้มปัจจุบัน (2025–2026)
- **ภาระงาน AI ดันความหนาแน่นพุ่ง:** rack เดิม 10–20 kW ไม่พอ คลัสเตอร์ AI เกิน 100 kW มุ่งสู่ 300 kW+; คาดแตะ ~370 kW ในปี 2026
- **[Liquid Cooling](/concept/liquid-cooling) เป็นสิ่งจำเป็น:** ตลาด liquid cooling สำหรับ AI โตจาก ~3.2 พันล้าน (2025) สู่ ~17.8 พันล้านดอลลาร์ (2036)
- **พลังงานคือข้อจำกัดหลัก:** การใช้ไฟของบริษัท AI ชั้นนำอาจเพิ่มจาก ~118 TWh (2024) เป็น ~295 TWh (2030) — เชื่อมความยั่งยืนใน [สัปดาห์ที่ 13: Computer Ethics & Intellectual Property](/module/13)
- ลด [PUE](/concept/pue) จาก ~1.50 (อากาศ) เหลือ ~1.05 (immersion) ลดพลังงานรวม ~30%

### 🧪 กิจกรรม/ปฏิบัติการ (OBE)
Lab 1 ชม. (ทดลองใช้ Cloud/Docker เบื้องต้น) + Project 1 ชม. (Deploy เว็บแอปพลิเคชันขึ้นเซิร์ฟเวอร์) — **Module 2: Web Dev**
> อ้างอิงจากแผน 4 โมดูล: ดูรายละเอียดเต็มที่ [กิจกรรมปฏิบัติการและโครงงาน](/docs/labs-projects)

---

## 📚 เนื้อหาเชิงลึกประจำสัปดาห์ (Deep Dive)

- [01. สถาปัตยกรรมศูนย์ข้อมูลและการจำลองเสมือน (Data Center Architecture and Virtualization)](/module/07/01)
- [02. เทคโนโลยีคอนเทนเนอร์ Docker และ Kubernetes (Container Technology)](/module/07/02)
- [03. รูปแบบการให้บริการคลาวด์ (Cloud Service Models): Public, Private, และ Sovereign](/module/07/03)
- [04. การจัดการความร้อนและพลังงานในศูนย์ข้อมูลยุค AI](/module/07/04)
- [05. การประมวลผลระดับ Hyperscale (Hyperscale Computing)](/module/07/05)
