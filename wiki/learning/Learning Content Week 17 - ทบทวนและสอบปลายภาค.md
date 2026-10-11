---
type: learning
status: complete
week: 17
source_week: "Week 17 - Final Examination"
tags: [learning, week17, en-001-019]
created: "2026-08-03"
updated: "2026-10-12"
---

# Learning Content Week 17: ทบทวนและสอบปลายภาค

> ใช้คู่กับ [[Week 17 - Final Examination]] สำหรับอ่านก่อนเรียน ทบทวนหลังเรียน และเตรียมกิจกรรมปฏิบัติการ

## คำถามนำ
ผู้เรียนสามารถอธิบายระบบคอมพิวเตอร์สมัยใหม่ตั้งแต่ AI, IoT, security ถึงจริยธรรมได้ครบวงจรหรือไม่?

## ผลลัพธ์การเรียนรู้ย่อย
1. ทบทวนหลังกลางภาคและภาพรวมทั้งรายวิชา
2. ฝึกวิเคราะห์กรณีศึกษา AI/IoT/security/ethics
3. เตรียมสอบปลายภาคตาม CLO1, CLO2, CLO4, CLO5

## แก่นความรู้ที่ต้องเข้าใจ
- ครึ่งหลังของรายวิชาเน้นระบบอัจฉริยะ: AI/ML, GenAI, IoT, cybersecurity, ethics และ DevOps
- ข้อสอบปลายภาคมักเชื่อมหลายมิติ เช่นระบบ IoT ใช้ AI ต้องมี database, network, security และ PDPA
- คำตอบที่ดีควรมีทั้งหลักการ ตัวอย่าง และการประเมิน trade-off

## เนื้อหาเรียนรู้
- ให้ผู้เรียนทำ case study เดียว เช่น smart classroom แล้ววิเคราะห์ครบ: sensor, MQTT, database, model, dashboard, Zero Trust, PDPA และ ethics
- ทบทวนคำศัพท์ด้วยการจับคู่: RAG-vector database, MQTT-IoT, Zero Trust-identity, PUE-data center, CI/CD-DevOps
- เตรียมสอบด้วยคำถามอัตนัยสั้น: อธิบาย trade-off และเสนอ mitigation มากกว่าท่องนิยาม

## 🧭 อธิบายเพิ่มเติม (ฉบับขยาย)

### 1) มองครึ่งหลังเป็น "ระบบเดียว"
ครึ่งหลังของรายวิชาเหมือนการประกอบร่างหุ่นยนต์หนึ่งตัว: AI/ML (W9) คือสมอง, GenAI และหุ่นยนต์ (W10) คือความสามารถสื่อสารและเคลื่อนไหว, ระบบฝังตัว/IoT (W11) คือประสาทสัมผัสและแขนขา, security (W12) คือระบบภูมิคุ้มกัน, จริยธรรม/IP (W13) คือมโนธรรม, DevOps (W14) คือวิธีสร้างและดูแลให้ทำงานต่อเนื่อง และการดูงาน (W15) คือการเห็นหุ่นยนต์ตัวจริงในโรงงาน ข้อสอบกรณีศึกษาจึงมักให้ระบบหนึ่งระบบ แล้วถามข้ามหลายสัปดาห์พร้อมกัน

![แผนผังความคิดครึ่งหลังของรายวิชา มีกรณีศึกษา smart classroom อยู่ตรงกลาง และสัปดาห์ 9 ถึง 15 ล้อมรอบพร้อมคำสำคัญ เช่น RAG, MQTT, Zero Trust, PDPA และ CI/CD รวมทั้งเส้นเชื่อมระหว่างสัปดาห์](/images/weeks/w17-concept-map.svg)

### 2) แผนที่การอ่านสอบรายสัปดาห์ (W9–W15) พร้อมข้อฝึก
**W9 AI & ML** — ต้องแยก AI ⊃ ML ⊃ Deep Learning, supervised/unsupervised/reinforcement, feature กับ label, overfitting และ NIST AI RMF (Govern, Map, Measure, Manage)
- ข้อฝึก: ระบบทายว่านักศึกษาจะสอบผ่านจากเวลาเข้าเรียนและคะแนนเก็บ เป็น learning แบบใด feature/label คืออะไร
- ข้อฝึก: train accuracy 99% แต่ test 70% แปลว่าอะไร แก้อย่างไร

**W10 GenAI & Robotics** — token, embedding, prompt, LLM, RAG (ค้นเอกสาร → ใส่ใน prompt → ตอบ), Agentic AI, hallucination, sense-plan-act
- ข้อฝึก: chatbot ตอบระเบียบมหาวิทยาลัยผิด ควรใช้ RAG อย่างไร และ vector database ช่วยตรงไหน
- ข้อฝึก: หุ่นยนต์ส่งของหลบสิ่งกีดขวาง อธิบายด้วย sense-plan-act

**W11 Embedded & IoT** — microcontroller vs microprocessor, sensor/actuator, device–edge–cloud, MQTT (broker, topic, publish/subscribe, QoS), CoAP, Zigbee, TinyML
- ข้อฝึก: ออกแบบ topic MQTT สำหรับวัดอุณหภูมิ 3 ห้อง และบอกว่าใครเป็น publisher/subscriber
- ข้อฝึก: เมื่อใดควรประมวลผลที่ edge แทน cloud (latency, bandwidth, privacy)

**W12 Cybersecurity** — CIA triad, symmetric vs asymmetric, hashing, MFA, defense-in-depth, Zero Trust (never trust, always verify), OWASP Top 10, deepfake
- ข้อฝึก: ระบุว่าเหตุการณ์ "ฐานข้อมูลถูกเข้ารหัสเรียกค่าไถ่" กระทบ CIA ข้อใด และเสนอ mitigation 3 ข้อ
- ข้อฝึก: Zero Trust ต่างจากการเชื่อใจทุกอย่างใน LAN อย่างไร

**W13 Ethics & IP** — ACM Code, bias/transparency/accountability, ลิขสิทธิ์ vs สิทธิบัตร vs เครื่องหมายการค้า vs ความลับทางการค้า, permissive vs copyleft, PDPA (controller/processor, ข้อมูลอ่อนไหว, consent, 72 ชั่วโมง)
- ข้อฝึก: ใช้ library GPL-3.0 ในแอปที่จะขาย ต้องทำอะไร
- ข้อฝึก: ระบบสแกนใบหน้าเข้าหอพัก มีประเด็น PDPA อะไรบ้าง

**W14 DevOps** — SDLC 6 ขั้น, Waterfall vs Agile, DevOps loop, CI vs Continuous Delivery vs Continuous Deployment, Git workflow, MLOps
- ข้อฝึก: เรียงขั้นตอน branch → PR → CI → review → merge → deploy และบอกว่าขั้นใดตรวจอะไร
- ข้อฝึก: ทำไม model ที่ deploy แล้วต้อง monitor data drift

**W15 Industry** — value chain 5 ชั้น, data center (Tier, PUE, redundancy), กรอบสังเกต 6 มุม, evidence vs opinion, บทบาทอาชีพ
- ข้อฝึก: PUE = 1.5 แปลว่าอะไร (พลังงานรวมเป็น 1.5 เท่าของพลังงาน IT)

![ตารางจับคู่สัปดาห์ 9 ถึง 15 กับ CLO1 ถึง CLO6 โดยไฮไลต์ CLO1, CLO2, CLO4 และ CLO5 ที่วัดในข้อสอบปลายภาค](/images/weeks/w17-clo-matrix.svg)

### 3) ตารางคู่คำที่มักสับสน
| คู่คำ | ต่างกันอย่างไร | สัปดาห์ |
|---|---|---|
| ML vs Deep Learning | DL เป็น ML ที่ใช้ neural network หลายชั้น เรียน feature เอง | W9 |
| Fine-tuning vs RAG | fine-tuning ปรับน้ำหนัก model; RAG ดึงความรู้ภายนอกตอนตอบ ไม่แก้ model | W10 |
| MQTT vs HTTP | MQTT publish/subscribe ผ่าน broker เบา; HTTP request/response | W11 |
| Encryption vs Hashing | encryption ถอดกลับได้ด้วย key; hashing ทางเดียว ใช้ตรวจความถูกต้อง/เก็บรหัสผ่าน | W12 |
| Copyright vs Patent | copyright อัตโนมัติ คุ้มครองการแสดงออก; patent ต้องจด คุ้มครองการประดิษฐ์ | W13 |
| Controller vs Processor | controller ตัดสินใจวัตถุประสงค์; processor ทำตามคำสั่ง | W13 |
| Continuous Delivery vs Deployment | delivery รอคนอนุมัติขึ้น prod; deployment ขึ้นอัตโนมัติ | W14 |

### 4) โครงคำตอบกรณีศึกษา (ใช้ได้เกือบทุกข้อ)
ตัวอย่างโจทย์: *"มหาวิทยาลัยต้องการ smart classroom ที่นับจำนวนคนด้วยกล้อง + AI แล้วปรับแอร์ผ่าน IoT จงวิเคราะห์"*
1. **Architecture:** กล้อง/ESP32 → edge model นับคน → MQTT → server + database → dashboard → actuator สั่งแอร์
2. **Data flow:** ระบุว่าข้อมูลใดเป็นข้อมูลส่วนบุคคล (ภาพใบหน้า) และลดให้เหลือเพียง "จำนวนคน" ที่ edge
3. **Risk:** model นับผิดเมื่อแสงน้อย (W9), อุปกรณ์ IoT ใช้รหัสผ่านเริ่มต้น (W11–W12), เก็บภาพเกินจำเป็น (W13)
4. **Mitigation:** ทดสอบหลายสภาพแสง, MQTT over TLS + ยืนยันตัวตนอุปกรณ์, ประมวลผลที่ edge ไม่ส่งภาพขึ้น cloud, ติดป้ายแจ้งและกำหนดระยะเวลาเก็บ
5. **Trade-off + operation:** edge ประหยัด bandwidth และเป็นส่วนตัวกว่าแต่ต้องดูแลอุปกรณ์หลายตัว จึงใช้ CI/CD และ monitoring ช่วย (W14)

คำตอบที่ได้คะแนนดีมี "หลักการ + ตัวอย่างจากโจทย์ + trade-off" ไม่ใช่การท่องนิยามเพียงอย่างเดียว อ่านกลยุทธ์ข้อสอบและข้อผิดพลาดที่พบบ่อยใน [แนวทางเตรียมสอบ](/exam-prep) และทบทวนเนื้อหาย่อย เช่น [หัวข้อ 2 ของสัปดาห์ 14](/module/14/02) และ [หัวข้อ 5 ของสัปดาห์ 13](/module/13/05)

### 5) แผนทบทวน 5 วันก่อนสอบ
| วัน | ทบทวน | งานที่ต้องได้ |
|---|---|---|
| 1 | W9–W10 | ตารางเปรียบเทียบประเภท learning + อธิบาย RAG เป็นแผนภาพ |
| 2 | W11 | วาด device–edge–cloud และออกแบบ topic MQTT |
| 3 | W12–W13 | ตาราง CIA กับภัยคุกคาม + ตาราง IP 4 ประเภท + PDPA |
| 4 | W14–W15 | วาด CI/CD pipeline + DevOps loop + สูตร PUE |
| 5 | รวม | ทำกรณีศึกษา 1 ข้อแบบจับเวลา ใช้โครงคำตอบ 5 ขั้น |

### สรุปสั้น
- ข้อสอบปลายภาควัด CLO1, CLO2, CLO4 และ CLO5 เน้นเนื้อหาหลังกลางภาค
- อ่านเป็นระบบเดียว: AI + IoT + security + ethics + DevOps เชื่อมกันเสมอ
- จำคู่คำที่สับสนให้แม่น เช่น RAG vs fine-tuning, encryption vs hashing, controller vs processor
- ตอบกรณีศึกษาด้วย architecture → data flow → risk → mitigation → trade-off
- ทุกคำตอบควรมีตัวอย่างจากโจทย์และเหตุผล ไม่ใช่เพียงนิยาม

## กิจกรรมในชั้นเรียน / ปฏิบัติการ
จัด mock exam แบบกรณีศึกษา 1 หน้า แล้วให้ผู้เรียนตอบเป็น architecture + risk + mitigation ภายในเวลาจำกัด

## คำถามตรวจความเข้าใจ
1. AI/IoT/security/ethics เชื่อมกันในระบบเดียวอย่างไร?
2. กรณีศึกษาแบบใดต้องคิดถึง PDPA?
3. คำตอบเชิงวิศวกรรมควรมี trade-off อะไรบ้าง?

## ชิ้นงาน / หลักฐานการเรียนรู้
- สรุปแนวคิด 1 หน้า หรือ concept map ของสัปดาห์นี้
- ผลกิจกรรม/โค้ด/diagram ตามโจทย์ประจำสัปดาห์
- คำตอบสะท้อนคิด: วันนี้เข้าใจอะไรเพิ่ม และยังสงสัยอะไร

## Research เพิ่มเติมและแหล่งอ้างอิง
**หัวข้อวิจัยเสริม:** Final integration research

- ข้อสอบปลายภาคควรวัดการบูรณาการ AI, IoT, security, cloud และ ethics ผ่าน case study มากกว่าการจำคำจำกัดความ
- ใช้ NIST AI RMF, NIST Zero Trust, MQTT และ PDPA เป็นแกนสร้างโจทย์ smart system เช่น smart classroom หรือ AI-enabled IoT dashboard
- คำตอบที่ดีควรมี architecture, data flow, risk analysis, mitigation และ ethical/legal consideration

**แหล่งอ้างอิงข้อมูล:**
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
- [MQTT.org](https://mqtt.org/)
- [MDES: Personal Data Protection Act B.E. 2562](https://mdes.go.th/law/detail/3577-Personal-Data-Protection-Act-B-E--2562--2019-)

## แหล่งค้นคว้าเพิ่มเติม
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
- [MQTT.org: The Standard for IoT Messaging](https://mqtt.org/)
- [MDES: Personal Data Protection Act B.E. 2562](https://mdes.go.th/law/detail/3577-Personal-Data-Protection-Act-B-E--2562--2019-)

> กลับ [[Learning Content Index]] · ดูแผนสัปดาห์ที่ 17: [[Week 17 - Final Examination]]
