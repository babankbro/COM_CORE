## คำถามนำ
วิศวกรคอมพิวเตอร์ควรตัดสินใจอย่างไรเมื่อเทคโนโลยีกระทบสิทธิ ความเป็นส่วนตัว และสังคม?

## ผลลัพธ์การเรียนรู้ย่อย
1. ใช้กรอบจริยธรรมในการวิเคราะห์กรณีศึกษา
2. เข้าใจ privacy, bias, accountability และ transparency
3. รู้จัก PDPA, copyright, license และ open source

## แก่นความรู้ที่ต้องเข้าใจ
- จริยธรรมคอมพิวเตอร์ไม่ได้ถามแค่ว่าทำได้ไหม แต่ถามว่าควรทำไหม ใครได้ประโยชน์ ใครรับความเสี่ยง และใครรับผิดชอบ
- ACM Code of Ethics ให้กรอบเรื่อง public good, avoiding harm, honesty, privacy และ professional responsibility
- PDPA กำหนดหลักการคุ้มครองข้อมูลส่วนบุคคล รวมถึงบทบาท data controller และ data processor

## เนื้อหาเรียนรู้
- ให้เริ่มจากกรณี AI ตรวจจับใบหน้าในห้องเรียน แล้วถามเรื่อง consent, purpose limitation, data retention, bias และทางเลือกที่ intrusive น้อยกว่า
- อธิบายทรัพย์สินทางปัญญาผ่านงานนักศึกษา: source code, dataset, model weight, prompt, image และ report มีสิทธิและ license ต่างกัน
- โยง open source: การใช้ library ไม่ได้แปลว่าทำอะไรก็ได้ ต้องอ่าน license และให้ attribution ตามเงื่อนไข

## กิจกรรมในชั้นเรียน / ปฏิบัติการ
อภิปรายกรณีศึกษา generative AI ใช้สร้างงานส่งรายวิชา แล้วให้ผู้เรียนเขียน policy การใช้ AI ที่ยุติธรรมและตรวจสอบได้

## คำถามตรวจความเข้าใจ
1. public good ใน ACM Code ใช้ตัดสินใจอย่างไร?
2. ข้อมูลส่วนบุคคลตาม PDPA คืออะไร?
3. open source license สำคัญต่อโครงงานอย่างไร?

## ชิ้นงาน / หลักฐานการเรียนรู้
- สรุปแนวคิด 1 หน้า หรือ concept map ของสัปดาห์นี้
- ผลกิจกรรม/โค้ด/diagram ตามโจทย์ประจำสัปดาห์
- คำตอบสะท้อนคิด: วันนี้เข้าใจอะไรเพิ่ม และยังสงสัยอะไร

## Research เพิ่มเติมและแหล่งอ้างอิง
**หัวข้อวิจัยเสริม:** Ethics, PDPA, UNESCO AI Ethics และ EU AI Act

- ACM Code of Ethics ใช้เป็นฐานอภิปรายว่าผู้พัฒนาระบบต้องคำนึงถึง public good, avoiding harm, privacy, honesty และ professional competence
- PDPA ไทยนิยามข้อมูลส่วนบุคคลและบทบาท data controller/data processor ใช้เชื่อมกับกรณีเก็บภาพ เสียง sensor หรือข้อมูลนักศึกษา
- UNESCO AI Ethics และ EU AI Act ช่วยให้เห็นทิศทางสากลของ AI governance: human rights, transparency, fairness, human oversight และ risk-based regulation

**แหล่งอ้างอิงข้อมูล:**
- [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics)
- [MDES: Personal Data Protection Act B.E. 2562](https://mdes.go.th/law/detail/3577-Personal-Data-Protection-Act-B-E--2562--2019-)
- [UNESCO Recommendation on the Ethics of AI](https://www.unesco.org/en/artificial-intelligence/recommendation-ethics)
- [European Commission: AI Act enters into force](https://commission.europa.eu/news-and-media/news/ai-act-enters-force-2024-08-01_en)

## แหล่งค้นคว้าเพิ่มเติม
- [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics)
- [MDES: Personal Data Protection Act B.E. 2562](https://mdes.go.th/law/detail/3577-Personal-Data-Protection-Act-B-E--2562--2019-)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

---

## 🗓️ แผนการสอนประจำสัปดาห์ (Teaching Plan)

> [!abstract] สาระสำคัญ
> จริยธรรมทางคอมพิวเตอร์ว่าด้วย "สิ่งที่ควร/ไม่ควรทำ" เมื่อใช้/พัฒนาเทคโนโลยี และทรัพย์สินทางปัญญา (IP) คุ้มครองผลงานสร้างสรรค์ ทั้งสองมีประเด็นใหม่จาก AI และข้อมูลส่วนบุคคล ([PDPA](/concept/pdpa))

### 🎯 วัตถุประสงค์การสอน (Learning Objectives)
1. ผู้เรียนตระหนักถึงประเด็นจริยธรรมที่เกี่ยวกับเทคโนโลยีและ AI — *CLO5*
2. ผู้เรียนเข้าใจประเภทของทรัพย์สินทางปัญญาด้านซอฟต์แวร์ — *CLO5*
3. ผู้เรียนวิเคราะห์กรณีศึกษาด้านความเป็นส่วนตัวและจริยธรรมได้ — *CLO5*

### 📝 สรุปเนื้อหาหัวข้อ (Topics Covered)
- จริยธรรมยุคดิจิทัลและ AI (AI Ethics, Algorithmic Bias, ความโปร่งใส)
- ทรัพย์สินทางปัญญา (ลิขสิทธิ์, สิทธิบัตร, เครื่องหมายการค้า)
- ใบอนุญาตซอฟต์แวร์ open-source vs proprietary
- กฎหมายคุ้มครองข้อมูลส่วนบุคคล ([PDPA](/concept/pdpa), GDPR)

### 📖 เนื้อหาโดยละเอียด — จริยธรรม
- ประเด็นคลาสสิก: privacy, digital divide, เสรีภาพการแสดงออก, อาชญากรรมคอมพิวเตอร์
- จรรยาบรรณวิชาชีพ: **ACM Code of Ethics**, IEEE Code of Ethics; กรอบ PAPA (Privacy, Accuracy, Property, Accessibility)
- จริยธรรม AI: bias & fairness, transparency & explainability, human oversight, accountability

### 📖 เนื้อหาโดยละเอียด — ทรัพย์สินทางปัญญา (บริบทไทย)
- พ.ร.บ.ลิขสิทธิ์ พ.ศ. 2537 คุ้มครอง source code/โปรแกรม แต่ **ไม่คุ้มครองอัลกอริทึม AI หรือผลงานที่ AI สร้างเองโดยอัตโนมัติ**; AI เป็น "เครื่องมือ" ร่วมกับมนุษย์อาจเข้าเกณฑ์
- พ.ร.บ.สิทธิบัตร พ.ศ. 2522 ไม่ให้สิทธิบัตรแก่วิธีการทางคณิตศาสตร์/ซอฟต์แวร์ (อยู่ระหว่างทบทวนตาม WIPO/TRIPS)
- [PDPA](/concept/pdpa) บังคับใช้เต็มรูปแบบตั้งแต่กลางปี 2565 เป็นเสาหลักการกำกับข้อมูลยุค AI

### 🔑 แนวคิดหลัก (Key Concepts)
[PDPA](/concept/pdpa) · ดูธีม [การกำกับดูแล จริยธรรม และกฎหมาย](/docs/theme-governance)

### 📈 แนวโน้มปัจจุบัน (2025–2026)
- **UNESCO Recommendation on the Ethics of AI:** แนวทางจริยธรรม AI ฉบับแรกระดับโลก รับรองโดย 193 ประเทศ วาง 10 หลักการ (do no harm, fairness, sustainability, human oversight, transparency, accountability ฯลฯ)
- **EU AI Act** + UNESCO กำหนดทิศทางกำกับ AI ทั่วโลก
- คดีละเมิดลิขสิทธิ์จาก generative AI เป็นที่ถกเถียงมากขึ้นในไทยและสากล

### 🧪 กิจกรรม/ปฏิบัติการ (OBE)
Lab 1 ชม. (อภิปราย Bias และจริยธรรม AI) + Project 1 ชม. (ดึงสตรีมภาพจากกล้องและทำ Object Detection เบื้องต้น) — **Module 4: Computer Vision**
> อ้างอิงจากแผน 4 โมดูล: ดูรายละเอียดเต็มที่ [กิจกรรมปฏิบัติการและโครงงาน](/docs/labs-projects)

---

## 📚 เนื้อหาเชิงลึกประจำสัปดาห์ (Deep Dive)

- [01. จริยธรรมยุคดิจิทัลและ AI Ethics](/module/13/01)
- [02. จรรยาบรรณวิชาชีพคอมพิวเตอร์](/module/13/02)
- [03. ทรัพย์สินทางปัญญา ลิขสิทธิ์ สิทธิบัตร](/module/13/03)
- [04. ใบอนุญาตซอฟต์แวร์ Open Source vs Proprietary](/module/13/04)
- [05. กฎหมายคุ้มครองข้อมูลส่วนบุคคล PDPA และ GDPR](/module/13/05)
