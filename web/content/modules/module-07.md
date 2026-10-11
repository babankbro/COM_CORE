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

## 🧭 อธิบายเพิ่มเติม (ฉบับขยาย)

### 1. Data center คือ "โรงงานที่ห้ามหยุดเดินเครื่อง"
ให้นึกถึงโรงพยาบาลขนาดใหญ่: มีห้องผ่าตัด (เซิร์ฟเวอร์ = **compute**) ห้องเก็บเวชระเบียน (**storage**) ทางเดินและลิฟต์เชื่อมทุกแผนก (**network** แบบ spine-leaf) ไฟฟ้าสำรองและเครื่องปั่นไฟ (**UPS + generator**) แอร์ควบคุมอุณหภูมิ (**cooling**) และ รปภ. คุมการเข้าออก (**physical security**) ทุกส่วนต้องมีของสำรอง (**redundancy** เช่นแนวคิด N+1 คือมีอุปกรณ์เกินความต้องการอย่างน้อย 1 ชุด) เพื่อให้ระบบยังทำงานแม้ชิ้นใดชิ้นหนึ่งเสีย

ตัวเลขที่ใช้วัดความต่อเนื่องคือ **availability** ลองคำนวณเวลาหยุดต่อปี (1 ปี = 8,760 ชั่วโมง):
- 99.9% → หยุดได้ 0.1% × 8,760 = **8.76 ชั่วโมง/ปี**
- 99.99% → หยุดได้ 0.01% × 8,760 = 0.876 ชั่วโมง ≈ **52.6 นาที/ปี**

"เพิ่มเลข 9 อีกหนึ่งตัว" ทำให้เวลาหยุดลดลง 10 เท่า แต่ต้นทุนของระบบสำรองเพิ่มขึ้นมาก นี่คือ trade-off ที่วิศวกรต้องตัดสินใจ อ่านองค์ประกอบเพิ่มที่ [หัวข้อ 1](/module/07/01)

### 2. VM กับ Container: บ้านเดี่ยว vs ห้องในคอนโด
**VM** เหมือนบ้านเดี่ยวหลายหลังบนที่ดินแปลงเดียว แต่ละหลังมีฐานราก ระบบไฟ และประปาของตัวเอง (= **Guest OS** เต็มชุด) จึงแยกขาดจากกันดี แต่หนักและสร้างช้า **Container** เหมือนห้องในคอนโดที่ใช้โครงสร้างอาคาร ลิฟต์ และระบบน้ำร่วมกัน (= แชร์ **kernel** ของ Host OS) แต่ละห้องมีเฟอร์นิเจอร์ของตัวเอง (= libraries และแอป) จึงเบาและย้ายเข้าออกได้เร็ว

![ภาพเทียบชั้นซอฟต์แวร์ ฝั่ง VM มี hardware hypervisor แล้วแต่ละ VM มี guest OS bins/libs และแอปของตัวเอง ฝั่ง container มี hardware host OS kernel ที่ใช้ร่วมกัน container engine แล้วแต่ละ container มีเพียง bins/libs และแอป](/images/weeks/w07-vm-vs-container.svg)

| ประเด็น | Virtual Machine | Container |
| :--- | :--- | :--- |
| สิ่งที่จำลอง | ทั้งเครื่อง (hardware เสมือน) | เฉพาะสภาพแวดล้อมของ process |
| OS | มี Guest OS ของตัวเองทุกเครื่อง | แชร์ kernel ของ Host OS |
| ขนาดโดยทั่วไป | ระดับ GB | ระดับ MB ถึงร้อย MB |
| เวลาเริ่มทำงาน | ระดับนาที | ระดับวินาที |
| การแยกความปลอดภัย | แยกขาดสูงกว่า | แยกระดับ process (ต้องตั้งค่าให้ดี) |
| เหมาะกับ | รัน OS ต่างชนิด, งานที่ต้องแยกขาด | microservices, CI/CD, deploy ซ้ำได้เหมือนเดิม |

ลำดับงาน Docker ที่ต้องจำ: **Dockerfile** (สูตร) → `docker build` → **image** (แม่พิมพ์ที่อ่านอย่างเดียว) → `docker run` → **container** (ชิ้นงานที่กำลังทำงาน) ส่วน **Kubernetes** เปรียบเหมือนผู้จัดการร้านที่สั่งว่า "ต้องมีพ่อครัว 3 คนเสมอ" ถ้าคนหนึ่งป่วย (pod ล่ม) ก็หาคนใหม่มาแทนเองทันที (self-healing) และเพิ่มคนเมื่อลูกค้าเยอะ (scaling) ดูตัวอย่าง Dockerfile และ YAML ที่ [หัวข้อ 2](/module/07/02) แล้วลงมือจริงใน [Lab 07](/lab/07)

### 3. กรณีศึกษา: จะเอา Asset Management Web App ของทีมขึ้นคลาวด์แบบไหน
- **ทางเลือก IaaS:** เช่า VM แล้วติดตั้ง Ubuntu, Python, ฐานข้อมูลเอง → ควบคุมได้มากที่สุด แต่ต้องอัปเดต OS และดูแลความปลอดภัยเอง
- **ทางเลือก PaaS:** ส่ง container หรือโค้ดขึ้นแพลตฟอร์ม → ทีมดูแลแค่แอปและข้อมูล เหมาะกับโครงงานที่มีเวลาจำกัด
- **ทางเลือก SaaS:** ใช้ Google Sheets ทำทะเบียนครุภัณฑ์ → เร็วที่สุด แต่ปรับแต่งตามความต้องการเฉพาะได้น้อย

ไม่ว่าเลือกแบบใด **ข้อมูลและสิทธิ์ผู้ใช้เป็นความรับผิดชอบของเราเสมอ** ถ้าข้อมูลเป็นข้อมูลส่วนบุคคลหรือข้อมูลราชการที่กฎหมายกำหนดให้เก็บในประเทศ ควรพิจารณา private หรือ sovereign cloud ([หัวข้อ 3](/module/07/03))

![ตาราง shared responsibility เจ็ดชั้นตั้งแต่ข้อมูลจนถึงอาคาร แสดงว่า on-premises ผู้ใช้ดูแลทั้ง 7 ชั้น IaaS ดูแล 4 ชั้น PaaS ดูแล 2 ชั้น และ SaaS ดูแลเพียงข้อมูลและสิทธิ์ผู้ใช้](/images/weeks/w07-responsibility.svg)

### 4. PUE ทีละขั้น (โจทย์ใหม่ ไม่ซ้ำกับหัวข้อ 4)
ศูนย์ข้อมูลของมหาวิทยาลัยมีอุปกรณ์ IT ใช้ **400 kW** และไฟรวมทั้งอาคาร **560 kW** ค่าไฟ 4 บาท/kWh ทำงานตลอดปี (8,760 ชั่วโมง)
1. PUE = 560 ÷ 400 = **1.4** · DCiE = 400 ÷ 560 ≈ **71.4%**
2. Non-IT = 560 − 400 = **160 kW** (= (1.4 − 1) × 400)
3. ค่าไฟส่วน Non-IT ต่อปี = 160 × 8,760 × 4 = **5,606,400 บาท**
4. ถ้าปรับระบบทำความเย็นจน PUE = 1.1 → Total = 440 kW, Non-IT = 40 kW ประหยัด 120 kW × 8,760 × 4 = **4,204,800 บาท/ปี**

ข้อคิด: ยิ่งงาน AI ทำให้ rack หนึ่งตู้กินไฟ 40–100 kW ค่า PUE ที่ต่างกันเพียง 0.1 ก็เป็นเงินจำนวนมาก จึงมีการใช้ **liquid cooling** ([หัวข้อ 4](/module/07/04)) และออกแบบระดับ **hyperscale** ที่ทำ automation ทุกอย่าง ([หัวข้อ 5](/module/07/05))

![กราฟแท่งซ้อนแสดงกำลังไฟ IT คงที่ 1,000 kW และส่วน Non-IT ที่ PUE 2.0 1.8 1.5 1.2 และ 1.05 ซึ่งลดจาก 1,000 kW เหลือ 50 kW พร้อมค่า DCiE ของแต่ละกรณี](/images/weeks/w07-pue-bars.svg)

### สรุปสั้น
- Data center = compute + storage + network + power + cooling + security และต้องมี redundancy
- availability 99.9% ≈ 8.76 ชม./ปี · 99.99% ≈ 52.6 นาที/ปี
- VM มี Guest OS ของตัวเอง · Container แชร์ kernel จึงเบาและเริ่มเร็ว
- Dockerfile → build → image → run → container · Kubernetes ดูแลจำนวน replica, self-healing, scaling
- IaaS ดูแลมากสุด → PaaS → SaaS ดูแลน้อยสุด แต่ข้อมูลเป็นของเราเสมอ
- PUE = Total ÷ IT (≥ 1, ยิ่งต่ำยิ่งดี) · Non-IT = (PUE − 1) × IT · คิดค่าไฟต้องแปลง kW เป็น kWh ก่อน

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
