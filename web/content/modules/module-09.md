## คำถามนำ
เครื่องเรียนรู้จากข้อมูลได้อย่างไร และทำไมการนำโมเดลไปใช้จริงต้องมี MLOps?

## ผลลัพธ์การเรียนรู้ย่อย
1. แยก AI, ML และ deep learning
2. เข้าใจ supervised/unsupervised/reinforcement learning
3. อธิบาย lifecycle ของโมเดลและ MLOps

## แก่นความรู้ที่ต้องเข้าใจ
- ML คือการสร้างโมเดลจากข้อมูลเพื่อทำนายหรือจัดกลุ่ม โดยไม่ได้เขียนกฎทุกข้อด้วยมือ
- คุณภาพข้อมูลส่งผลต่อคุณภาพโมเดลโดยตรง เพราะโมเดลเรียนรู้ pattern รวมถึง bias จากข้อมูล
- MLOps ทำให้การฝึก ประเมิน deploy และ monitor โมเดลเป็นกระบวนการที่ตรวจสอบซ้ำได้

## เนื้อหาเรียนรู้
- เริ่มจากโจทย์จำแนกผลไม้ด้วยน้ำหนักและสี แล้วอธิบาย feature, label, training data, model และ prediction
- เปรียบเทียบ supervised learning กับ unsupervised learning: แบบแรกมีคำตอบให้เรียน แบบหลังหาโครงสร้างหรือกลุ่มในข้อมูล
- NIST AI RMF ช่วยให้มอง AI ไม่ใช่แค่ความแม่นยำ แต่รวม validity, safety, security, fairness, accountability และ governance

## กิจกรรมในชั้นเรียน / ปฏิบัติการ
ใช้ dataset เล็ก ๆ ฝึก classification model แล้วบันทึก feature, metric, error case และข้อจำกัดของข้อมูล

## คำถามตรวจความเข้าใจ
1. training กับ inference ต่างกันอย่างไร?
2. bias เกิดได้จากจุดใดของ lifecycle?
3. ทำไมต้อง monitor โมเดลหลัง deploy?

## ชิ้นงาน / หลักฐานการเรียนรู้
- สรุปแนวคิด 1 หน้า หรือ concept map ของสัปดาห์นี้
- ผลกิจกรรม/โค้ด/diagram ตามโจทย์ประจำสัปดาห์
- คำตอบสะท้อนคิด: วันนี้เข้าใจอะไรเพิ่ม และยังสงสัยอะไร

## Research เพิ่มเติมและแหล่งอ้างอิง
**หัวข้อวิจัยเสริม:** AI/ML lifecycle และ AI risk

- NIST AI RMF เสนอกรอบ Govern, Map, Measure, Manage เพื่อจัดการความเสี่ยง AI ตลอด lifecycle ไม่ใช่ดูแค่ accuracy
- หัวข้อ MLOps ควรเน้น data quality, model versioning, evaluation, deployment, monitoring และ feedback loop
- ให้ผู้เรียนเชื่อม bias, hallucination, robustness และ privacy เข้ากับขั้นตอนข้อมูล/โมเดล/การนำไปใช้จริง

**แหล่งอ้างอิงข้อมูล:**
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST AI RMF 1.0 PDF](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf)
- [Google Cloud: MLOps architecture and lifecycle](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)

## แหล่งค้นคว้าเพิ่มเติม
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [ACM/IEEE-CS/AAAI Computer Science Curricula 2023](https://dl.acm.org/doi/book/10.1145/3664191)

---

## 🗓️ แผนการสอนประจำสัปดาห์ (Teaching Plan)

> [!abstract] สาระสำคัญ
> AI คือระบบที่ทำงานซึ่งปกติต้องใช้ปัญญามนุษย์ หัวใจปัจจุบันคือ **Machine Learning (ML)** — เรียนรู้รูปแบบจากข้อมูล โดยเฉพาะ Deep Learning สัปดาห์นี้ปูพื้นก่อนเข้าสู่ Generative AI ในสัปดาห์ถัดไป

### 🎯 วัตถุประสงค์การสอน (Learning Objectives)
1. ผู้เรียนอธิบายแนวคิดพื้นฐานของ AI และ Machine Learning ได้ — *CLO1*
2. ผู้เรียนรู้จักขั้นตอนการสร้างและฝึกสอนโมเดล (Model Training) — *CLO1*
3. ผู้เรียนเข้าใจแนวคิด [MLOps](/concept/mlops) และความสำคัญในการนำโมเดลไปใช้งานจริง — *CLO1*

### 📝 สรุปเนื้อหาหัวข้อ (Topics Covered)
- พื้นฐาน AI และ ML (Supervised, Unsupervised, Reinforcement Learning)
- Deep Learning และโครงข่ายประสาทเทียม (Neural Networks) เบื้องต้น
- [MLOps](/concept/mlops): พัฒนา → ทดสอบ → จัดเก็บ → นำขึ้นระบบจริง (Deployment)

### 📖 เนื้อหาโดยละเอียด
- **ระดับของ AI:** narrow AI (เฉพาะงาน) vs general AI (สมมุติฐาน)
- **สาขา ML:** supervised, unsupervised, reinforcement learning
- **Deep Learning:** neural networks, การฝึกด้วยข้อมูลปริมาณมาก ใช้ GPU/NPU (เชื่อม [สัปดาห์ที่ 3: Digital Logic & Modern Processors](/module/03))
- **วงจรชีวิตข้อมูล:** ข้อมูล → ฝึก → ประเมิน → deploy → ตรวจสอบ ([MLOps](/concept/mlops))
- **ข้อจำกัด:** อคติ (bias), การหลอน (hallucination), ความต้องการข้อมูล/พลังงาน

### 🔑 แนวคิดหลัก (Key Concepts)
[MLOps](/concept/mlops) · [RAG และ LLM](/concept/rag-llm) · [Agentic AI](/concept/agentic-ai) · ดูธีม [ปัญญาประดิษฐ์เป็นแรงขับเคลื่อนข้ามศาสตร์](/docs/theme-ai)

### 📈 แนวโน้มปัจจุบัน (2025–2026)
- โมเดลเฉพาะทาง (domain-specific foundation models) + on-device AI มาแทนโมเดลยักษ์อเนกประสงค์
- AI-ready data และ MLOps เป็นปัจจัยชี้ขาดความสำเร็จของการนำ AI ไปใช้จริง

### 🧪 กิจกรรม/ปฏิบัติการ (OBE)
Lab 1 ชม. (ทดลองรัน ML Model ง่ายๆ) + Project 1 ชม. (วางแผนสถาปัตยกรรม IoT) — **Module 3: IoT & Smart Systems**
> อ้างอิงจากแผน 4 โมดูล: ดูรายละเอียดเต็มที่ [กิจกรรมปฏิบัติการและโครงงาน](/docs/labs-projects)

---

## 📚 เนื้อหาเชิงลึกประจำสัปดาห์ (Deep Dive)

- [01. แนวคิดพื้นฐานของ AI และ Machine Learning (AI & Machine Learning Fundamentals)](/module/09/01)
- [02. โครงข่ายประสาทเทียม (Artificial Neural Networks)](/module/09/02)
- [03. การเรียนรู้เชิงลึกเบื้องต้น (Introduction to Deep Learning)](/module/09/03)
- [04. วงจรชีวิตของข้อมูลในระบบ AI (Data Lifecycle in AI Systems)](/module/09/04)
- [05. หลักการของ MLOps และการนำโมเดลไปใช้งานจริง (MLOps & Model Deployment)](/module/09/05)
