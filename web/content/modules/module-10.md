## คำถามนำ
Generative AI จากซอฟต์แวร์จะเชื่อมกับการลงมือทำในโลกจริงผ่านหุ่นยนต์ได้อย่างไร?

## ผลลัพธ์การเรียนรู้ย่อย
1. เข้าใจ token, embedding, prompt, LLM และ RAG
2. อธิบาย agentic AI และ sense-plan-act
3. วิเคราะห์ความเสี่ยงของ generative AI และ robotics

## แก่นความรู้ที่ต้องเข้าใจ
- LLM ทำนาย token ถัดไปจากบริบทขนาดใหญ่ จึงสร้างข้อความ โค้ด และคำอธิบายได้ แต่ไม่ได้รับประกันว่าถูกเสมอ
- RAG ลดปัญหาความรู้ไม่ทันสมัยด้วยการค้นเอกสารที่เกี่ยวข้องแล้วส่งเข้า prompt
- หุ่นยนต์ใช้วงจร sense-plan-act และเมื่อนำ LLM/AI เข้าไปช่วยวางแผน ต้องคุม safety และ verification เข้มขึ้น

## เนื้อหาเรียนรู้
- สอน LLM แบบไม่ลงคณิตหนัก: ข้อความถูกแปลงเป็น token, model ใช้บริบทเพื่อคาดการณ์, embedding ช่วยแทนความหมายในเชิงเวกเตอร์
- อธิบาย agentic AI ด้วยงานหลายขั้นตอน เช่นวางแผน ค้นข้อมูล เรียกเครื่องมือ เขียนไฟล์ และตรวจผล แต่ต้องมีขอบเขตสิทธิ์และ human oversight
- เชื่อม robotics: sensor รับโลกจริง, planner ตัดสินใจ, actuator ลงมือทำ ความผิดพลาดของ AI จึงอาจกลายเป็นความเสี่ยงทางกายภาพ

## กิจกรรมในชั้นเรียน / ปฏิบัติการ
ให้ผู้เรียนออกแบบ prompt + retrieval source สำหรับผู้ช่วยตอบคำถามรายวิชา แล้วระบุ guardrails อย่างน้อย 3 ข้อ

## คำถามตรวจความเข้าใจ
1. RAG ต่างจากการถาม LLM ตรง ๆ อย่างไร?
2. agentic AI ต้องมี control อะไร?
3. ความเสี่ยงของ AI ในหุ่นยนต์ต่างจาก chatbot อย่างไร?

## ชิ้นงาน / หลักฐานการเรียนรู้
- สรุปแนวคิด 1 หน้า หรือ concept map ของสัปดาห์นี้
- ผลกิจกรรม/โค้ด/diagram ตามโจทย์ประจำสัปดาห์
- คำตอบสะท้อนคิด: วันนี้เข้าใจอะไรเพิ่ม และยังสงสัยอะไร

## Research เพิ่มเติมและแหล่งอ้างอิง
**หัวข้อวิจัยเสริม:** Generative AI, RAG, agents และ governance

- NIST Generative AI Profile เป็น companion ของ AI RMF สำหรับความเสี่ยงเฉพาะ GenAI เช่น hallucination, misuse, synthetic content และ data/IP risk
- RAG ควรถูกสอนเป็น system pattern ที่รวม retrieval, ranking, prompt construction และ evaluation ไม่ใช่แค่เรียก LLM
- Agentic AI ต้องเพิ่ม guardrails เช่น tool permission, audit log, human approval, sandboxing และ failure recovery โดยเฉพาะเมื่อเชื่อมกับ robotics

**แหล่งอ้างอิงข้อมูล:**
- [NIST AI RMF Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
- [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [pgvector documentation](https://github.com/pgvector/pgvector)

## แหล่งค้นคว้าเพิ่มเติม
- [NIST AI RMF Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
- [pgvector: Vector similarity search for PostgreSQL](https://github.com/pgvector/pgvector)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

---

## 🗓️ แผนการสอนประจำสัปดาห์ (Teaching Plan)

> [!abstract] สาระสำคัญ
> โมเดลภาษาขนาดใหญ่ (LLM) ขับเคลื่อน **Generative AI** และล่าสุดคือ **[Agentic AI](/concept/agentic-ai)** ที่ลงมือทำงานได้เอง พร้อมการผสาน AI เข้ากับหุ่นยนต์ในโลกจริง (Physical AI)

### 🎯 วัตถุประสงค์การสอน (Learning Objectives)
1. ผู้เรียนเข้าใจหลักการเบื้องต้นของ Generative AI และ [LLM](/concept/rag-llm) — *CLO1*
2. ผู้เรียนอธิบายการประยุกต์ AI ในโลกจริงผ่านแนวคิด Physical AI ได้ — *CLO1*
3. ผู้เรียนตระหนักถึงวิวัฒนาการของหุ่นยนต์ฮิวแมนนอยด์และการสั่งการผ่านโมเดล AI — *CLO4*

### 📝 สรุปเนื้อหาหัวข้อ (Topics Covered)
- Generative AI และสถาปัตยกรรม Transformer เบื้องต้น (เบื้องหลัง ChatGPT, Claude)
- Physical AI: นำ AI จากซอฟต์แวร์สู่การควบคุมเครื่องจักรกลจริง
- หุ่นยนต์ฮิวแมนนอยด์, ระบบขับเคลื่อนอัตโนมัติ และวิศวกรรมการควบคุม
- การทำงานร่วมกันระหว่าง Hardware, Sensors และ AI Models

### 📖 เนื้อหาโดยละเอียด
- **LLM/Generative AI:** token, prompt, embedding (เชื่อม [Vector Database](/concept/vector-database)); สร้างข้อความ/ภาพ/โค้ด
- **[Agentic AI](/concept/agentic-ai):** ตัวแทนที่วางแผนและลงมือทำงานหลายขั้นตอน
- **หุ่นยนต์ (robotics):** วงจร sense–plan–act; ผสาน AI กับการควบคุมการเคลื่อนไหว
- **ความเสี่ยง:** bias, hallucination, ความต้องการพลังงาน/ข้อมูล (เชื่อม [สัปดาห์ที่ 7: Data Center & Cloud Infrastructure](/module/07), [สัปดาห์ที่ 13: Computer Ethics & Intellectual Property](/module/13))

### 🔑 แนวคิดหลัก (Key Concepts)
[Agentic AI](/concept/agentic-ai) · [RAG และ LLM](/concept/rag-llm) · ดูธีม [ปัญญาประดิษฐ์เป็นแรงขับเคลื่อนข้ามศาสตร์](/docs/theme-ai)

### 📈 แนวโน้มปัจจุบัน (2025–2026)
- **Agentic AI คือคลื่นลูกใหญ่:** เปลี่ยนจาก "ผู้ช่วยตอบคำถาม" เป็น "ตัวแทนที่ลงมือทำ"; ~79% ขององค์กรเริ่มนำมาใช้
- **เม็ดเงินมหาศาล:** การใช้จ่าย generative AI ระดับองค์กรพุ่งจาก 2.3 พันล้าน (2023) เป็น ~37 พันล้านดอลลาร์ (2025)
- **หุ่นยนต์ + LLM:** หุ่นยนต์ใช้นโยบายควบคุมด้วยภาษา (language-conditioned); หุ่นยนต์ฮิวแมนนอยด์เข้าสู่สายการผลิตมากขึ้น

### 🧪 กิจกรรม/ปฏิบัติการ (OBE) — Lab 7
Lab 1 ชม. (เรียกใช้งาน GenAI API) + Project 1 ชม. (ต่อวงจรบอร์ด ESP32/Arduino และเซนเซอร์) — **Module 3: IoT & Smart Systems**
> อ้างอิงจากแผน 4 โมดูล: ดูรายละเอียดเต็มที่ [กิจกรรมปฏิบัติการและโครงงาน](/docs/labs-projects)

### ❓ คำถามทบทวน
1. "Agentic AI" ต่างจากแชตบอตทั่วไปอย่างไร
2. Physical AI คืออะไร ยกตัวอย่าง
3. ยกความเสี่ยงของ generative AI 2 ข้อ พร้อมแนวทางลด

### 📚 อ้างอิง (References)
- Siegwart, R., Nourbakhsh, I. R., & Scaramuzza, D. (2011). *Introduction to Autonomous Mobile Robots* (2nd ed.). MIT Press.
- Kersai. *AI Breakthroughs in 2026: The Year of Agentic AI.* [kersai.com](https://kersai.com/ai-breakthroughs-in-2026/)
- arXiv. *The 2025 AI Agent Index.* [arxiv.org](https://arxiv.org/pdf/2602.17753)
- The Innovation Mode. *2026 Technology Innovation Trends.* [theinnovationmode.com](https://theinnovationmode.com/the-innovation-blog/2026-innovation-trends)

---

## 📚 เนื้อหาเชิงลึกประจำสัปดาห์ (Deep Dive)

- [01. หลักการทำงานของ Generative AI และ LLM (Generative AI & Large Language Models)](/module/10/01)
- [02. การประยุกต์ใช้ RAG (Retrieval-Augmented Generation)](/module/10/02)
- [03. Agentic AI: ตัวแทนที่ทำงานอัตโนมัติ (AI Agents)](/module/10/03)
- [04. Physical AI และหุ่นยนต์ฮิวแมนนอยด์ (Physical AI & Humanoid Robots)](/module/10/04)
- [05. ข้อจำกัดและความท้าทายของการใช้ Generative AI (Limitations & Risks of Generative AI)](/module/10/05)
