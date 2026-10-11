สวัสดีนักศึกษาทุกคน เข้าสู่สัปดาห์ที่ 14 ของรายวิชา ซึ่งในสัปดาห์นี้เราจะมาศึกษาภาพรวมและแก่นสำคัญของ **วิศวกรรมระบบ (Systems Engineering)** และแนวคิดที่กำลังขับเคลื่อนวงการไอทีในปัจจุบันอย่าง **DevOps** 

## บทบาทของวิศวกรรมระบบ (Systems Engineering)
ในการพัฒนาซอฟต์แวร์หรือระบบคอมพิวเตอร์ขนาดใหญ่ การเขียนโปรแกรม (Coding) เป็นเพียงส่วนหนึ่งของโครงสร้างทั้งหมด วิศวกรรมระบบคือศาสตร์ที่ว่าด้วยการมองระบบแบบองค์รวม (Holistic View) โดยพิจารณาถึงทุกองค์ประกอบที่ทำงานร่วมกัน ครอบคลุมตั้งแต่การเก็บและวิเคราะห์ความต้องการ (Requirements Analysis), การออกแบบสถาปัตยกรรม (Architecture Design), การบูรณาการส่วนประกอบต่างๆ (Integration), การรักษาความปลอดภัย (Security) ไปจนถึงการบำรุงรักษา (Maintenance) วิศวกรรมระบบทำให้เรามั่นใจได้ว่าระบบที่ถูกสร้างขึ้นมาจะตอบโจทย์ทางธุรกิจและมีความเสถียรภาพสูงในระยะยาว

## การก้าวผ่านขีดจำกัดด้วยวัฒนธรรม DevOps
ในอดีต กระบวนการทำงานระหว่าง "ทีมพัฒนา" (Development - Dev) และ "ทีมปฏิบัติการ" (Operations - Ops) มักจะถูกแยกขาดจากกันอย่างชัดเจน (Silo) ซึ่งก่อให้เกิดปัญหาความล่าช้า ข้อมูลตกหล่น และข้อขัดแย้งเมื่อถึงเวลาต้องนำซอฟต์แวร์ขึ้นสู่ระบบการใช้งานจริง (Production)

**DevOps** จึงถือกำเนิดขึ้น ไม่ใช่ในฐานะเครื่องมือทางเทคโนโลยีเพียงอย่างเดียว แต่เป็น "วัฒนธรรมองค์กร" และ "แนวปฏิบัติ" ที่ต้องการทลายกำแพงระหว่างสองทีม โดยมีเสาหลักที่สำคัญคือ:
- **Collaboration:** การสร้างความร่วมมือและการสื่อสารที่ไร้รอยต่อ
- **Automation:** การพึ่งพาระบบอัตโนมัติในทุกมิติ ทั้งการทดสอบ (Testing) และการส่งมอบซอฟต์แวร์ (Deployment)
- **Continuous Integration / Continuous Delivery (CI/CD):** กลไกที่ทำให้เราสามารถอัปเดตแอปพลิเคชันได้วันละหลายสิบครั้งโดยที่ระบบไม่ล่ม
- **Monitoring & Feedback Loop:** การเฝ้าระวังประสิทธิภาพการทำงานของระบบอย่างเรียลไทม์ และนำข้อมูลนั้นกลับมาพัฒนาต่อยอด

## สาระสำคัญในสัปดาห์นี้
เพื่อให้นักศึกษามองเห็นภาพตั้งแต่เริ่มต้นจนจบกระบวนการ เราจะเจาะลึกใน 5 หัวข้อย่อยดังนี้:
1. **วงจรการพัฒนาระบบ (SDLC):** ทำความเข้าใจรากฐานของการสร้างซอฟต์แวร์
2. **แนวคิด Agile และ DevOps:** สัมผัสถึงปรัชญาความคล่องตัวในการทำงานยุคใหม่
3. **กระบวนการ CI/CD:** สถาปัตยกรรมการส่งมอบอัตโนมัติเบื้องหลังบริษัทยักษ์ใหญ่
4. **MLOps และ AIOps:** การผนวกรวมปัญญาประดิษฐ์ (AI) เข้ากับงานฝั่งปฏิบัติการ
5. **การเตรียมโครงงานประยุกต์ Capstone:** การรวบรวมองค์ความรู้ทั้งหมดเพื่อเตรียมพร้อมสำหรับโปรเจกต์จบการศึกษา

สัปดาห์นี้จะเป็นกุญแจสำคัญที่เชื่อมโยงความรู้เชิงทฤษฎีในห้องเรียน เข้ากับมาตรฐานการทำงานจริงในระดับอุตสาหกรรม (Production Level) ขอให้นักศึกษาทุกคนเตรียมตัวให้พร้อมครับ!

---


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

---

## 🗓️ แผนการสอนประจำสัปดาห์ (Teaching Plan)

> [!abstract] สาระสำคัญ
> สัปดาห์บูรณาการ — นำความรู้ทุกหัวข้อมาประกอบเป็นระบบจริงผ่านวงจรการพัฒนา (SDLC), แนวคิด Agile/DevOps และ CI/CD เพื่อเตรียมความพร้อมโครงงานปลายภาค

### 🎯 วัตถุประสงค์การสอน (Learning Objectives)
1. ผู้เรียนเข้าใจวงจรการพัฒนาระบบซอฟต์แวร์/ฮาร์ดแวร์สมัยใหม่ — *CLO6*
2. ผู้เรียนรู้จักแนวคิด DevOps และกระบวนการ CI/CD — *CLO6*
3. ผู้เรียนนำความรู้ทั้งหมดมาประยุกต์ออกแบบโครงงานปลายภาคได้ — *CLO3*

### 📝 สรุปเนื้อหาหัวข้อ (Topics Covered)
- วงจรการพัฒนาระบบ (SDLC)
- วิศวกรรมระบบร่วมสมัย: Agile และ DevOps
- Continuous Integration & Continuous Deployment (CI/CD)
- การระดมสมองและเตรียมโครงงานปลายภาค (Capstone Preparation)

### 📖 เนื้อหาโดยละเอียด
- **SDLC:** วิเคราะห์ → ออกแบบ → พัฒนา → ทดสอบ → นำไปใช้ → บำรุงรักษา
- **Agile/DevOps:** วงรอบสั้น, การทำงานร่วม dev+ops, อัตโนมัติ
- **CI/CD:** integrate–build–test–deploy อัตโนมัติ; เชื่อมกับการจัดการเวอร์ชัน (Git)
- บูรณาการกับทุกสัปดาห์: เลือกเทคโนโลยีจาก [ฐานข้อมูล](/module/05), [IoT](/module/11), [AI](/module/10) มาประกอบเป็นโครงงาน

### 🔑 แนวคิดหลัก (Key Concepts)
[MLOps](/concept/mlops) (ส่วนขยายของ DevOps สำหรับ ML)

### 📈 แนวโน้มปัจจุบัน (2025–2026)
- DevOps ผสาน AI (AIOps) และ MLOps เพื่อ deploy โมเดล/บริการอัตโนมัติ
- เครื่องมือ AI ช่วยทั้งวงจร SDLC (สร้างโค้ด/เทสต์/รีวิว)

### 🧪 กิจกรรม/ปฏิบัติการ (OBE)
Lab 1 ชม. (สร้าง CI/CD Pipeline ขั้นต้น) + Project 1 ชม. (เชื่อมระบบ CV เข้ากับ Web/IoT Dashboard เดิม) — **Module 4: Computer Vision**
> อ้างอิงจากแผน 4 โมดูล: ดูรายละเอียดเต็มที่ [กิจกรรมปฏิบัติการและโครงงาน](/docs/labs-projects)

---

## 📚 เนื้อหาเชิงลึกประจำสัปดาห์ (Deep Dive)

- [01. วงจรการพัฒนาระบบ SDLC (Software Development Life Cycle)](/module/14/01)
- [02. แนวคิด Agile และ DevOps: วิวัฒนาการสู่การส่งมอบซอฟต์แวร์ยุคใหม่](/module/14/02)
- [03. กระบวนการ CI/CD: หัวใจหลักของระบบอัตโนมัติ](/module/14/03)
- [04. MLOps และ AIOps: เมื่อปัญญาประดิษฐ์มาบรรจบกับปฏิบัติการ](/module/14/04)
- [05. การเตรียมโครงงานประยุกต์ (Capstone Project)](/module/14/05)
