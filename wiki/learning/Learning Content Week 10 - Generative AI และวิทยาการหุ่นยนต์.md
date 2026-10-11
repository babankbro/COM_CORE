---
type: learning
status: complete
week: 10
source_week: "Week 10 - Generative AI & Modern Robotics"
tags: [learning, week10, en-001-019]
created: "2026-08-03"
updated: "2026-10-12"
---

# Learning Content Week 10: Generative AI และวิทยาการหุ่นยนต์

> ใช้คู่กับ [[Week 10 - Generative AI & Modern Robotics]] สำหรับอ่านก่อนเรียน ทบทวนหลังเรียน และเตรียมกิจกรรมปฏิบัติการ

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

## 🧭 อธิบายเพิ่มเติม (ฉบับขยาย)

ส่วนนี้เดินตามเส้นทางของ "หนึ่งคำถาม" ตั้งแต่ถูกตัดเป็น token จนกลายเป็นคำตอบ การกระทำของ agent และการเคลื่อนไหวของหุ่นยนต์ อ่านคู่กับหัวข้อเจาะลึก [หัวข้อ 1](/module/10/01) (GenAI และ LLM), [หัวข้อ 2](/module/10/02) (RAG), [หัวข้อ 3](/module/10/03) (Agentic AI), [หัวข้อ 4](/module/10/04) (Physical AI), [หัวข้อ 5](/module/10/05) (ข้อจำกัดและความเสี่ยง) และใบงาน [Lab 10](/lab/10)

### 1. LLM คือ "ระบบเติมคำอัตโนมัติขั้นสูง"

ลองนึกถึงแป้นพิมพ์มือถือที่เดาคำถัดไปให้เรา LLM ทำสิ่งเดียวกันแต่ในระดับที่ใหญ่กว่ามาก มันเคยอ่านข้อความจำนวนมหาศาลระหว่าง pre-training จึงเรียนรู้ว่าหลังบริบทหนึ่ง token ใดมักตามมา ขั้นตอนการตอบหนึ่งครั้งคือ

1. **Tokenize:** ตัดข้อความเป็น token (คำ ส่วนของคำ หรือตัวอักษร) ภาษาไทยไม่เว้นวรรคระหว่างคำ tokenizer หลายตัวจึงมักใช้ token ต่อประโยคมากกว่าภาษาอังกฤษ (ขึ้นกับแต่ละโมเดล ควรตรวจด้วย tokenizer ของผู้ให้บริการ)
2. **Embed:** แปลงแต่ละ token เป็นเวกเตอร์ ("พิกัดความหมาย") คำที่ความหมายใกล้กันจะอยู่ใกล้กันในปริภูมิเวกเตอร์
3. **Transformer + self-attention:** ให้แต่ละ token "มอง" token อื่นในบริบท เพื่อเข้าใจว่าคำไหนเกี่ยวกับคำไหน
4. **ทำนาย:** ได้คะแนนดิบ (logits) ของทุก token ในคลังคำ แปลงเป็นความน่าจะเป็นด้วย softmax แล้วเลือก token ถัดไป
5. **วนซ้ำ:** ต่อ token ที่เลือกเข้ากับบริบท แล้วทำนายตัวต่อไปจนจบคำตอบ

ตัวอย่าง บริบท *"ไฟในห้องแล็บดับ ฉันจึงเปิด ..."* สมมติ logits ของ ไฟฉาย, สวิตช์, หน้าต่าง, ตู้เย็น เป็น 2.5, 1.8, 1.0, −0.5 ความน่าจะเป็นจาก softmax $p_i = e^{z_i/T} / \sum_j e^{z_j/T}$ ที่ temperature $T = 1.0$ คือ 0.57, 0.28, 0.13, 0.03 เมื่อลด $T$ เป็น 0.5 "ไฟฉาย" ได้ถึง 0.77 (ตอบแน่นอนขึ้น) แต่ถ้าเพิ่มเป็น 1.5 "ตู้เย็น" ซึ่งไม่สมเหตุสมผลจะได้ 0.06 (หลากหลายขึ้นแต่เพี้ยนง่ายขึ้น)

![กราฟแท่งความน่าจะเป็นของ token ถัดไปสี่ตัว ไฟฉาย สวิตช์ หน้าต่าง ตู้เย็น ที่ temperature 0.5 1.0 และ 1.5 แสดงว่า temperature สูงทำให้การกระจายแบนลง](/images/weeks/w10-next-token.svg)

ประเด็นสำคัญ: LLM เลือกคำที่ "น่าจะตามมา" ไม่ใช่คำที่ "ถูกต้องตามความจริง" จึงเกิด **hallucination** ได้ แม้ภาษาจะลื่นไหลและมั่นใจ

### 2. Worked example: RAG ทีละขั้น ด้วยเวกเตอร์ 3 มิติ

เปรียบ LLM ธรรมดาเป็นนักเขียนที่ตอบจากความจำ ส่วน RAG คือการให้ **บรรณารักษ์** (retriever) ไปหยิบหน้าหนังสือที่เกี่ยวข้องมาวางบนโต๊ะก่อน นักเขียนจึงตอบโดยอ้างอิงเอกสารได้ โจทย์: นักศึกษาถาม *"ห้องแล็บเปิดกี่โมง"* คลังเอกสารมี 3 chunk (เวกเตอร์ของเล่น 3 มิติ ของจริงมีหลายร้อยถึงหลายพันมิติ)

| chunk | เนื้อหา | เวกเตอร์ $v$ |
|---|---|---|
| A | เวลาเปิดห้องแล็บ 8:30–16:30 | [0.8, 0.2, 0.1] |
| B | กฎการยืมบอร์ด ESP32 | [0.2, 0.9, 0.3] |
| C | กำหนดการสอบกลางภาค | [0.3, 0.2, 0.9] |

เวกเตอร์คำถาม $q = [0.9, 0.1, 0.2]$ ใช้ cosine similarity $\cos\theta = \dfrac{q \cdot v}{\lVert q \rVert\,\lVert v \rVert}$

- $\lVert q \rVert = \sqrt{0.81 + 0.01 + 0.04} = \sqrt{0.86} \approx 0.927$
- กับ A: $q \cdot v = 0.72 + 0.02 + 0.02 = 0.76$, $\lVert v \rVert = \sqrt{0.69} \approx 0.831$ ได้ $\cos \approx 0.76 / (0.927 \times 0.831) \approx 0.987$
- กับ C: $q \cdot v = 0.27 + 0.02 + 0.18 = 0.47$, $\lVert v \rVert = \sqrt{0.94} \approx 0.970$ ได้ $\cos \approx 0.523$
- กับ B: $q \cdot v = 0.18 + 0.09 + 0.06 = 0.33$ ได้ $\cos \approx 0.367$

ดังนั้น top-1 คือ chunk A จากนั้นประกอบ prompt เป็น *คำสั่ง ("ตอบจากเอกสารที่ให้เท่านั้น ถ้าไม่มีให้ตอบว่าไม่ทราบ และอ้างอิงแหล่ง") + context (chunk A) + คำถาม* แล้วส่งให้ LLM

![แผนภาพ RAG สองแถว แถวบนคือ indexing แบ่ง chunk ทำ embedding เก็บใน vector database แถวล่างคือ query ทำ embedding ของคำถาม ค้น top-k ด้วย cosine similarity ประกอบ prompt ส่งให้ LLM พร้อมคะแนน cosine ของสาม chunk](/images/weeks/w10-rag-pipeline.svg)

ในระบบจริงขั้นค้นหานี้ทำโดย vector database เช่น pgvector ที่ค้นได้เร็วแม้มีหลายล้าน chunk (โค้ดทดลองค้นด้วย cosine อยู่ใน [หัวข้อ 2](/module/10/02))

**งบ token (context window):** ถ้าโมเดลรับได้ 8,000 token ใช้ system prompt 300 + คำถาม 50 + top-3 chunk × 400 = 1,200 และกันที่ไว้ให้คำตอบ 1,000 รวม 2,550 token ยังเหลือ 5,450 token การดึง chunk มากเกินไปจึงไม่ใช่แค่เปลืองเงิน แต่อาจล้น context window และเพิ่มข้อมูลรบกวนได้

### 3. Agent และหุ่นยนต์: วงจรที่ "ลงมือทำ"

**Agentic AI** เปรียบได้กับ "เด็กฝึกงานที่เก่งแต่ยังต้องมีพี่เลี้ยง" มันคิดแผน (reason) เรียกเครื่องมือ (act) เช่น ค้นเว็บ คำนวณ อ่าน/เขียนไฟล์ แล้วดูผล (observe) ก่อนตัดสินใจขั้นต่อไป วนแบบนี้จนงานเสร็จหรือครบจำนวนรอบสูงสุด (รูปแบบ ReAct ใน [หัวข้อ 3](/module/10/03)) ส่วน **หุ่นยนต์** เหมือนคนขับรถที่ต้องมองถนน (sense) ตีความสิ่งที่เห็น (perceive) ตัดสินใจ (plan) และหมุนพวงมาลัย (act) ซ้ำหลายสิบครั้งต่อวินาที เพราะโลกจริงเปลี่ยนตลอด

![แผนภาพวงจรสองวง ซ้ายคือวงจร ReAct ของ agentic AI บริบท คิดวางแผน เรียก tool สังเกตผล ขวาคือวงจร sense perceive plan act ของหุ่นยนต์ พร้อม guardrail และ safety ของแต่ละแบบ](/images/weeks/w10-agent-robot-loops.svg)

| ประเด็น | Chatbot (LLM ตรง ๆ) | RAG | Agentic AI | Physical AI / หุ่นยนต์ |
|---|---|---|---|---|
| แหล่งความรู้ | ความจำจาก training | เอกสารที่ค้นมา + LLM | LLM + ผลจาก tool | sensor + โมเดล + แผนที่ |
| ผลลัพธ์ | ข้อความ | ข้อความพร้อมอ้างอิง | การกระทำในระบบดิจิทัล | การเคลื่อนไหวในโลกจริง |
| ความเสี่ยงหลัก | hallucination, ข้อมูลเก่า | ค้นผิด chunk, prompt injection ในเอกสาร | ใช้ tool ผิด/เกินสิทธิ์ | อุบัติเหตุ บาดเจ็บ ทรัพย์สินเสียหาย |
| การควบคุม | ตรวจทานคำตอบ | ประเมิน retrieval, บังคับอ้างอิง | least privilege, log, human approval | e-stop, จำกัดความเร็ว/แรง, simulation |

ความผิดพลาดของ chatbot คือ "ข้อความผิด" ซึ่งแก้ไขได้ แต่ความผิดพลาดของหุ่นยนต์อาจเป็น "แรงที่ผิด" ซึ่งย้อนกลับไม่ได้ ระดับการควบคุมจึงต้องเข้มขึ้นตามผลกระทบ ใน [Lab 10](/lab/10) ผู้เรียนเรียก LLM API ผ่าน proxy server แทนการฝัง API key ลงในบอร์ด ESP32 ซึ่งเป็น guardrail ด้านความปลอดภัยพื้นฐานแบบหนึ่ง

### สรุปสั้น

- LLM ทำนาย token ถัดไปซ้ำ ๆ ด้วย softmax ของ logits ภาษาที่ลื่นไหลไม่ได้รับประกันความถูกต้อง
- Temperature ต่ำ = ตอบแน่นอน ซ้ำได้, temperature สูง = หลากหลายแต่เพี้ยนง่าย
- Embedding แทนความหมายเป็นเวกเตอร์ และวัดความคล้ายด้วย cosine similarity (1 = ทิศเดียวกัน)
- RAG = indexing (chunk → embedding → vector DB) + query (ค้น top-k → ประกอบ prompt → LLM ตอบพร้อมอ้างอิง)
- Agent วน คิด → เรียก tool → สังเกตผล ต้องมี least privilege, audit log และ human approval
- หุ่นยนต์วน sense → perceive → plan → act ความผิดพลาดมีผลทางกายภาพ จึงต้องมี e-stop และทดสอบใน simulation ก่อน

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

> กลับ [[Learning Content Index]] · ดูแผนสัปดาห์ที่ 10: [[Week 10 - Generative AI & Modern Robotics]]
