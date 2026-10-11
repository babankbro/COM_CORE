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

## 🧭 อธิบายเพิ่มเติม (ฉบับขยาย)

### 1) SDLC, Agile และ DevOps: สามคำที่มักถูกใช้ปนกัน
**SDLC** คือ "ขั้นตอน" ที่ระบบทุกระบบต้องผ่าน (วิเคราะห์ → ออกแบบ → พัฒนา → ทดสอบ → นำไปใช้ → บำรุงรักษา) ส่วน **Waterfall** และ **Agile** คือ "วิธีจัดลำดับ" ขั้นตอนเหล่านั้น เปรียบเหมือนการสร้างตึกกับการทำอาหารให้ลูกค้าชิม: สร้างตึกต้องออกแบบให้เสร็จก่อนเทเสาเข็ม (Waterfall) แต่ร้านอาหารปรับสูตรได้ทุกวันจากเสียงลูกค้า (Agile) ส่วน **DevOps** ขยายแนวคิด Agile ไปถึงฝั่งปฏิบัติการ ให้ทีมเดียวกันรับผิดชอบตั้งแต่เขียนโค้ดจนระบบรันอยู่จริง

![เปรียบเทียบ Waterfall ที่เรียงขั้นตอนเป็นขั้นบันไดตั้งแต่วิเคราะห์ requirement ถึงบำรุงรักษา กับ Agile ที่วนรอบ sprint planning, build และ test, review และ retrospective โดยดึงงานจาก product backlog](/images/weeks/w14-sdlc-vs-agile.svg)

| มิติ | Waterfall | Agile (Scrum) | DevOps |
|---|---|---|---|
| หน่วยงาน | phase ทั้งโครงการ | sprint 1–4 สัปดาห์ | การเปลี่ยนแปลงเล็ก ๆ ต่อเนื่อง |
| ส่งมอบ | ครั้งเดียวตอนท้าย | ทุกสิ้น sprint | ได้หลายครั้งต่อวัน |
| รับมือ requirement เปลี่ยน | ยาก ต้องย้อน phase | ปรับ backlog ทุก sprint | feedback จาก monitoring |
| จุดเน้น | เอกสารและแผน | ทีม + ผู้ใช้ + ซอฟต์แวร์ที่ใช้ได้ | automation + ownership ร่วม |
| เหมาะกับ | งานที่มีมาตรฐานกำกับชัด | ผลิตภัณฑ์ที่ต้องทดลอง | บริการที่รันตลอดเวลา |

ในโครงงานรายวิชา ทีมสามารถผสมกันได้: วางแผนภาพรวมแบบ SDLC (requirement และ architecture ให้ชัดก่อน) แล้วพัฒนาเป็นรอบสั้นแบบ Agile และใช้ CI/CD ช่วยตรวจทุกการเปลี่ยนแปลง

### 2) CI กับ CD ต่างกันตรงไหน
**Continuous Integration (CI)** คือการรวมโค้ดเข้ากิ่งหลักบ่อย ๆ และให้เครื่องรัน build + test อัตโนมัติทุกครั้ง เหมือนมี "ด่านตรวจ" ที่ไม่เคยเหนื่อย ส่วน **Continuous Delivery** คือทำให้ทุกเวอร์ชันที่ผ่าน CI พร้อมขึ้นระบบจริงได้ตลอดเวลา โดยยังมีคนกดอนุมัติ และ **Continuous Deployment** คือขึ้น production อัตโนมัติเลยเมื่อผ่านทุกด่าน

![CI/CD pipeline เริ่มจาก git push หรือ pull request ผ่าน build, test, สร้าง artifact เป็น Docker image, deploy ไป staging และ production แล้ว monitor หาก test ไม่ผ่านจะบล็อก merge และหากระบบผิดปกติจะ rollback](/images/weeks/w14-cicd-pipeline.svg)

### 3) ตัวอย่างเดินทางของหนึ่งฟีเจอร์: branch → PR → CI → deploy
สมมติทีมทำระบบ AI Object Detection (Module 4) และต้องการเพิ่มฟีเจอร์ "แสดง confidence ของผลทำนายบน dashboard"
1. **Issue:** เปิด issue #42 พร้อม acceptance criteria เช่น "แสดง confidence เป็นเปอร์เซ็นต์ทศนิยม 1 ตำแหน่ง และถ้าต่ำกว่า 50% ให้แสดงสีเทา"
2. **Branch:** `git switch -c feature/42-show-confidence` แยกงานออกจาก `main` ไม่กระทบเพื่อน
3. **Commit:** แก้ API ให้คืน `{"class": "dog", "confidence": 0.89}` เขียน unit test ว่าค่าอยู่ในช่วง 0–1 แล้ว commit ด้วยข้อความที่อ่านรู้เรื่อง เช่น `feat: return confidence from /predict (#42)`
4. **Pull Request:** push แล้วเปิด PR อธิบายว่าแก้อะไร ทดสอบอย่างไร แนบภาพหน้าจอ
5. **CI:** GitHub Actions รัน lint + `pytest` อัตโนมัติ ถ้ามี test ล้มเหลว PR จะขึ้นเครื่องหมายแดงและไม่ควร merge
6. **Review:** เพื่อนในทีมอย่างน้อย 1 คนอ่านโค้ด ถามคำถาม ขอให้แก้ จนผ่าน
7. **Merge + CD:** merge เข้า `main` แล้ว pipeline build Docker image และ deploy ไป staging ให้ทีมลองใช้ จากนั้นจึงขึ้น production (ในรายวิชาอาจเป็นเพียง demo server)
8. **Monitor + release:** ติดตาม log และ error หลัง deploy ถ้าผิดปกติให้ rollback ไปเวอร์ชันก่อนหน้า แล้วติด tag เช่น `v1.2.0` เมื่อนิ่ง

ข้อสังเกต: ทุกขั้นทิ้ง "หลักฐาน" ไว้ใน repository (issue, commit, PR, ผล CI) ซึ่งเป็นหลักฐานการทำงานเป็นทีมที่ใช้ตอบคำถามในวันนำเสนอได้ทันที

### 4) DevOps เป็นวงจร ไม่ใช่เส้นตรง
![DevOps infinity loop ฝั่ง Dev ประกอบด้วย Plan, Code, Build, Test และฝั่ง Ops ประกอบด้วย Release, Deploy, Operate, Monitor แล้ววนกลับไป Plan](/images/weeks/w14-devops-loop.svg)

ข้อมูลจาก Monitor (เช่น latency สูงขึ้นหลัง deploy หรือ model ทายผิดบ่อยขึ้นเมื่อแสงเปลี่ยน) ต้องย้อนกลับไปเป็นงานใน Plan รอบถัดไป นี่คือเหตุผลที่ **MLOps** ต่อยอดจาก DevOps: นอกจากโค้ดแล้ว ยังต้อง version ทั้ง data และ model และเฝ้าดู data drift ด้วย ([หัวข้อ 4](/module/14/04))

### 5) จาก idea เป็น backlog ของ capstone
- **Requirement → User story:** "ในฐานะเจ้าหน้าที่ ฉันต้องการเห็นจำนวนคนในห้องแบบ real-time เพื่อปรับแอร์"
- **Acceptance criteria:** เขียนแบบตรวจได้ เช่น "อัปเดตทุก ≤ 5 วินาที ความคลาดเคลื่อน ≤ 1 คนในการทดสอบ 20 ภาพ"
- **Architecture:** กล้อง/ESP32 → MQTT → API + model → database → dashboard (เชื่อม W5, W6, W11)
- **Definition of Done:** โค้ดผ่าน CI, มี test, มีคนรีวิว, อัปเดต README
อ่านเพิ่มที่ [หัวข้อ 3](/module/14/03) และ [หัวข้อ 5](/module/14/05) แล้วลงมือใน [Lab 14](/lab/14)

### สรุปสั้น
- SDLC คือขั้นตอน ส่วน Waterfall/Agile คือวิธีจัดลำดับขั้นตอน
- DevOps = วัฒนธรรม + automation + feedback loop ไม่ใช่แค่เครื่องมือ deploy
- CI ตรวจทุก commit อัตโนมัติ, Continuous Delivery พร้อม deploy แต่รอคนอนุมัติ, Continuous Deployment ขึ้นเองอัตโนมัติ
- ทุกฟีเจอร์ควรเดินทาง issue → branch → commit → PR → CI → review → merge → deploy → monitor
- acceptance criteria ที่วัดได้ช่วยให้ทีมตกลงกันได้ว่า "เสร็จ" คืออะไร
- เตรียมสอบ: ดู [แนวทางเตรียมสอบ](/exam-prep)

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
