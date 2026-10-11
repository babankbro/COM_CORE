## คำถามนำ
ทำไมการคิดเชิงอัลกอริทึมยังสำคัญ แม้มี AI ช่วยเขียนโค้ด?

## ผลลัพธ์การเรียนรู้ย่อย
1. ออกแบบขั้นตอนแก้ปัญหาด้วย decomposition และ abstraction
2. เขียน pseudocode/flowchart สำหรับปัญหาง่าย
3. วิเคราะห์ Big-O เบื้องต้นและใช้ AI assistant อย่างรับผิดชอบ

## แก่นความรู้ที่ต้องเข้าใจ
- algorithm คือขั้นตอนชัดเจน มีอินพุต เอาต์พุต และจบได้ ไม่ใช่แค่โค้ดในภาษาใดภาษาหนึ่ง
- Big-O ช่วยคิดว่าเมื่อข้อมูลใหญ่ขึ้น โปรแกรมจะช้าลงอย่างไร
- AI assistant ช่วยเร่งงานเขียนโค้ดได้ แต่ผู้เรียนยังต้องตรวจตรรกะ ทดสอบ และรับผิดชอบผลลัพธ์

## เนื้อหาเรียนรู้
- ให้เริ่มจากปัญหาในชีวิตประจำวัน เช่นหาคะแนนสูงสุดในรายชื่อ แล้วแปลงเป็น decomposition, pseudocode และ flowchart
- เปรียบเทียบ linear search กับ binary search เพื่อให้เห็นว่าอัลกอริทึมต่างกันทำให้ประสิทธิภาพต่างกัน แม้คำตอบสุดท้ายเหมือนกัน
- สาธิตการใช้ AI ช่วยเขียนโค้ดอย่างถูกวิธี: เขียนโจทย์ให้ชัด ขอ test cases ขออธิบาย complexity แล้วผู้เรียนต้องรันและตรวจเอง

## กิจกรรมในชั้นเรียน / ปฏิบัติการ
ให้ผู้เรียนเขียน pseudocode ของ mini game loop แล้วให้ AI ช่วยแปลงเป็น Python พร้อมอธิบายว่าต้องตรวจส่วนใดก่อนส่ง

## คำถามตรวจความเข้าใจ
1. O(n) ต่างจาก O(n²) อย่างไร?
2. flowchart ช่วยก่อนเขียนโค้ดอย่างไร?
3. ข้อควรระวัง 2 ข้อเมื่อใช้ AI assistant คืออะไร?

## ชิ้นงาน / หลักฐานการเรียนรู้
- สรุปแนวคิด 1 หน้า หรือ concept map ของสัปดาห์นี้
- ผลกิจกรรม/โค้ด/diagram ตามโจทย์ประจำสัปดาห์
- คำตอบสะท้อนคิด: วันนี้เข้าใจอะไรเพิ่ม และยังสงสัยอะไร

## Research เพิ่มเติมและแหล่งอ้างอิง
**หัวข้อวิจัยเสริม:** Algorithms, programming และ AI coding assistants

- CS2023 วาง software development fundamentals และ algorithmic foundations เป็น competency หลัก ซึ่งใช้ยืนยันว่า AI assistant ไม่ได้แทนความเข้าใจอัลกอริทึม
- ผู้เรียนควรฝึกอ่าน code ที่ AI สร้างด้วย test case และ complexity analysis เพราะความถูกต้องของ syntax ไม่เท่ากับความถูกต้องของ algorithm
- จริยธรรมการใช้ AI ในงานเขียนโค้ดควรผูกกับ attribution, academic integrity, privacy ของ code/data และความรับผิดชอบต่อ bug

**แหล่งอ้างอิงข้อมูล:**
- [ACM/IEEE-CS/AAAI Computer Science Curricula 2023](https://dl.acm.org/doi/book/10.1145/3664191)
- [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics)
- [GitHub Copilot documentation](https://docs.github.com/en/copilot)

## แหล่งค้นคว้าเพิ่มเติม
- [ACM/IEEE-CS/AAAI Computer Science Curricula 2023](https://dl.acm.org/doi/book/10.1145/3664191)
- [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics)

---

## 🗓️ แผนการสอนประจำสัปดาห์ (Teaching Plan)

> [!abstract] สาระสำคัญ
> **อัลกอริทึม** คือลำดับขั้นตอนแก้ปัญหาที่ชัดเจนและสิ้นสุดได้ ส่วน **โปรแกรม** คืออัลกอริทึมที่เขียนด้วยภาษาที่เครื่องเข้าใจ ทักษะแกนคือ "การคิดเชิงคำนวณ (computational thinking)"

### 🎯 วัตถุประสงค์การสอน (Learning Objectives)
1. ผู้เรียนเข้าใจแนวคิดและสามารถออกแบบอัลกอริทึมพื้นฐานเพื่อแก้ปัญหาได้ — *CLO3*
2. ผู้เรียนรู้จักกระบวนทัศน์การเขียนโปรแกรม (Programming Paradigms) แบบต่าง ๆ — *CLO3*
3. ผู้เรียนสามารถประยุกต์ใช้ AI Assistant ในการเขียนโปรแกรมได้อย่างมีประสิทธิภาพและรับผิดชอบ — *CLO3*

### 📝 สรุปเนื้อหาหัวข้อ (Topics Covered)
- แนวคิดอัลกอริทึมและโครงสร้างข้อมูลเบื้องต้น; ความซับซ้อน [Big-O Notation](/concept/big-o-notation)
- กระบวนทัศน์การเขียนโปรแกรม (Procedural, Object-Oriented, Functional)
- การทำงานร่วมกับ AI ในการเขียนโค้ด (GitHub Copilot, Cursor)
- แนวคิด [Agentic AI](/concept/agentic-ai) ในการจัดการ/เขียนโปรแกรมอัตโนมัติ

### 📖 เนื้อหาโดยละเอียด
- **การคิดเชิงคำนวณ:** decomposition, pattern recognition, abstraction, algorithm design
- **การแทนอัลกอริทึม:** ผังงาน (flowchart), รหัสเทียม (pseudocode)
- **โครงสร้างควบคุม:** ลำดับ, เงื่อนไข (if/else), วนซ้ำ (for/while)
- **ประสิทธิภาพ:** [Big-O Notation](/concept/big-o-notation) เช่น O(1), O(n), O(n²) — เปรียบเทียบอัลกอริทึมค้นหา/จัดเรียง

### 🔑 แนวคิดหลัก (Key Concepts)
[Big-O Notation](/concept/big-o-notation) · [Agentic AI](/concept/agentic-ai)

### 📈 แนวโน้มปัจจุบัน (2025–2026)
- **AI ช่วยเขียนโค้ด** โตจาก ~550 ล้าน เป็น ~4 พันล้านดอลลาร์ในปีเดียว โมเดลตีความทั้ง codebase ได้ — แต่ผู้เรียนยังต้อง **เข้าใจอัลกอริทึมเพื่อตรวจสอบ/แก้ไขโค้ดที่ AI สร้าง**
- Python ครองอันดับภาษายอดนิยมสำหรับผู้เริ่มต้นและงาน AI/data
- ประเด็นความซื่อสัตย์ทางวิชาการในการใช้ AI (เชื่อม [สัปดาห์ที่ 13: Computer Ethics & Intellectual Property](/module/13))

### 🧪 กิจกรรม/ปฏิบัติการ (OBE) — Lab 3–4
Lab 1 ชม. (วิเคราะห์ Big-O/Flowchart) + Project 1 ชม. (สรุป นำเสนอ และสาธิตการเล่นเกม) — **Module 1: Foundation & Programming**
> อ้างอิงจากแผน 4 โมดูล: ดูรายละเอียดเต็มที่ [กิจกรรมปฏิบัติการและโครงงาน](/docs/labs-projects)

### ❓ คำถามทบทวน
1. คุณสมบัติของอัลกอริทึมที่ดีมีอะไรบ้าง
2. เขียน pseudocode หาค่ามากสุดในลิสต์ พร้อมระบุ Big-O
3. ทำไมการเข้าใจอัลกอริทึมยังจำเป็นแม้มี AI ช่วยเขียนโค้ด

### 📚 อ้างอิง (References)
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms (CLRS)* (4th ed.). MIT Press.
- ACM/IEEE-CS CC2020 — Software Development Fundamentals (SDF).
- instinctools. *AI Trends 2026.* [instinctools.com](https://www.instinctools.com/blog/ai-trends/)

---

## 📚 เนื้อหาเชิงลึกประจำสัปดาห์ (Deep Dive)

- [01. การคิดเชิงคำนวณแบบเจาะลึก (Computational Thinking)](/module/04/01)
- [02. การวิเคราะห์ความซับซ้อนของอัลกอริทึม (Big-O Notation)](/module/04/02)
- [03. การเขียนโปรแกรมเชิงวัตถุกับเชิงฟังก์ชัน (OOP vs Functional Programming)](/module/04/03)
- [04. ทำงานคู่กับผู้ช่วยเขียนโค้ด AI (AI Coding Assistants)](/module/04/04)
- [05. ระบบควบคุมเวอร์ชันและการทำงานพร้อมกัน (Version Control และ Concurrency)](/module/04/05)
