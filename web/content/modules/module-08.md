## คำถามนำ
เราจะเชื่อมความรู้สัปดาห์ 1-7 เป็นภาพระบบเดียวได้อย่างไร?

## ผลลัพธ์การเรียนรู้ย่อย
1. ทบทวน CE ecosystem ตั้งแต่ hardware ถึง cloud
2. ฝึกแก้โจทย์วิเคราะห์ ไม่ใช่จำคำศัพท์
3. เตรียมสอบกลางภาคตาม CLO1-CLO3

## แก่นความรู้ที่ต้องเข้าใจ
- หัวข้อก่อนกลางภาคเรียงจากภาพรวมสาขา → hardware/software → logic/processor → programming → database → network → cloud
- โจทย์ที่ดีมักให้สถานการณ์ระบบหนึ่ง แล้วถามให้แยกองค์ประกอบ ออกแบบข้อมูล หรืออธิบาย trade-off
- การทบทวนควรทำเป็น concept map และ practice problems มากกว่าการอ่านซ้ำอย่างเดียว

## เนื้อหาเรียนรู้
- ให้ผู้เรียนเลือกโครงงานเกม/web app ที่ทำมา แล้ว map ว่าใช้ความรู้จากสัปดาห์ใดบ้าง เช่น logic อยู่ใน game rule, database อยู่ใน save/load, network อยู่ใน API
- ทบทวนด้วยโจทย์ผสม: ออกแบบ ER diagram, เขียน pseudocode, คำนวณเลขฐาน, อธิบาย TCP/UDP และคำนวณ PUE
- ให้ผู้เรียนทำ one-page cheat sheet เชิงแนวคิด แม้ใช้ไม่ได้ในสอบ แต่กระบวนการสรุปจะเผยช่องว่างความเข้าใจ

## กิจกรรมในชั้นเรียน / ปฏิบัติการ
จัด peer review: นักศึกษาแลกกันอธิบาย concept map แล้วเพื่อนตั้งคำถาม 3 ข้อ

## คำถามตรวจความเข้าใจ
1. สัปดาห์ 1-7 เชื่อมกันเป็นระบบอย่างไร?
2. หัวข้อใดใช้ใน project มากที่สุด?
3. ข้อสอบแบบกรณีศึกษาควรเริ่มวิเคราะห์จากอะไร?

## ชิ้นงาน / หลักฐานการเรียนรู้
- สรุปแนวคิด 1 หน้า หรือ concept map ของสัปดาห์นี้
- ผลกิจกรรม/โค้ด/diagram ตามโจทย์ประจำสัปดาห์
- คำตอบสะท้อนคิด: วันนี้เข้าใจอะไรเพิ่ม และยังสงสัยอะไร

## Research เพิ่มเติมและแหล่งอ้างอิง
**หัวข้อวิจัยเสริม:** Midterm integration research

- การสอบกลางภาคควรใช้โจทย์บูรณาการจากมาตรฐาน CE/CS เช่น ให้ผู้เรียนอธิบายระบบหนึ่งตั้งแต่ hardware, software, algorithm, database, network ถึง cloud
- ใช้ ACM/IEEE outcome language เป็นแนวทางออกข้อสอบ: explain, apply, design, evaluate ไม่ใช่ถามจำคำศัพท์อย่างเดียว
- ควรมีข้อสอบที่ตรวจทั้ง concept map และ problem solving เช่น ER diagram, pseudocode, subnet/TCP reasoning และ PUE calculation

**แหล่งอ้างอิงข้อมูล:**
- [ACM/IEEE Computer Engineering Curricula 2016](https://www.acm.org/binaries/content/assets/education/ce2016-final-report.pdf)
- [ACM/IEEE-CS/AAAI Computer Science Curricula 2023](https://dl.acm.org/doi/book/10.1145/3664191)
- [ACM Curricula Recommendations](https://www.acm.org/education/curricula-recommendations)

## แหล่งค้นคว้าเพิ่มเติม
- [ACM/IEEE Computer Engineering Curricula 2016](https://www.acm.org/binaries/content/assets/education/ce2016-final-report.pdf)
- [ACM/IEEE-CS/AAAI Computer Science Curricula 2023](https://dl.acm.org/doi/book/10.1145/3664191)

---

## 🗓️ แผนการสอนประจำสัปดาห์ (Teaching Plan)

> [!abstract] สาระสำคัญ
> ประเมินผลสัปดาห์ที่ 1–7 (น้ำหนัก 20% — ดู [การวัดและประเมินผล](/docs/assessment)) ครอบคลุม CLO1–CLO3

### 🎯 วัตถุประสงค์
1. ประเมินความรู้/ความเข้าใจของผู้เรียนในเนื้อหาสัปดาห์ที่ 1–7
2. ทบทวนความสัมพันธ์ของระบบตั้งแต่ฮาร์ดแวร์ ซอฟต์แวร์ เครือข่าย และศูนย์ข้อมูล

### 📝 ขอบเขตการสอบ (Topics Covered)
- [W1 ภาพรวม CE/IS/IT](/module/01)
- [W2 ฮาร์ดแวร์/ซอฟต์แวร์](/module/02)
- [W3 วงจรตรรก/หน่วยประมวลผล](/module/03)
- [W4 อัลกอริทึม/โปรแกรม](/module/04)
- [W5 ฐานข้อมูล](/module/05)
- [W6 เครือข่าย/อินเทอร์เน็ต](/module/06)
- [W7 ศูนย์ข้อมูล/คลาวด์](/module/07)

### 📋 รูปแบบข้อสอบ
ปรนัย (ความเข้าใจหลักการ) + อัตนัยประยุกต์ (เช่น ออกแบบ ER diagram, เขียน SQL/pseudocode, คำนวณเลขฐาน/PUE)

### 📚 อ้างอิง (References)
- เนื้อหาการบรรยายและสื่อการสอนสัปดาห์ที่ 1–7
- เกณฑ์การประเมิน: [การวัดและประเมินผล](/docs/assessment)

---

## 📚 เนื้อหาเชิงลึกประจำสัปดาห์ (Deep Dive)

- [01. ทบทวนภาพรวมวิศวกรรมคอมพิวเตอร์และระบบนิเวศ](/module/08/01)
- [02. ทบทวนสถาปัตยกรรมฮาร์ดแวร์และหน่วยประมวลผล](/module/08/02)
- [03. ทบทวนอัลกอริทึมและกระบวนทัศน์การเขียนโปรแกรม](/module/08/03)
- [04. ทบทวนระบบฐานข้อมูลและการจัดการข้อมูล](/module/08/04)
- [05. ทบทวนเครือข่ายคอมพิวเตอร์และศูนย์ข้อมูล](/module/08/05)
