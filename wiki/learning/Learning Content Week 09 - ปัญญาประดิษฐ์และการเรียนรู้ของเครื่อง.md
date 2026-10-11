---
type: learning
status: complete
week: 9
source_week: "Week 09 - AI & Machine Learning Foundations"
tags: [learning, week09, en-001-019]
created: "2026-08-03"
updated: "2026-10-12"
---

# Learning Content Week 09: ปัญญาประดิษฐ์และการเรียนรู้ของเครื่อง

> ใช้คู่กับ [[Week 09 - AI & Machine Learning Foundations]] สำหรับอ่านก่อนเรียน ทบทวนหลังเรียน และเตรียมกิจกรรมปฏิบัติการ

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

## 🧭 อธิบายเพิ่มเติม (ฉบับขยาย)

ส่วนนี้ขยายความจากเนื้อหาหลักด้วยภาพเปรียบเทียบในชีวิตประจำวันและตัวอย่างคำนวณด้วยมือ อ่านคู่กับหัวข้อเจาะลึก [หัวข้อ 1](/module/09/01) (แนวคิดพื้นฐาน AI/ML), [หัวข้อ 2](/module/09/02) (Neural Networks), [หัวข้อ 3](/module/09/03) (Deep Learning), [หัวข้อ 4](/module/09/04) (วงจรชีวิตข้อมูล), [หัวข้อ 5](/module/09/05) (MLOps) และใบงาน [Lab 09](/lab/09)

### 1. AI, ML, DL และ GenAI: วงกลมซ้อนกัน 4 ชั้น

ให้นึกถึง "ตุ๊กตาแม่ลูกดก" (Matryoshka) ตัวใหญ่สุดคือ **AI** ทุกระบบที่ทำงานซึ่งปกติต้องใช้ปัญญามนุษย์ รวมถึงระบบที่เขียนกฎด้วยมือ (rule-based) ข้างในคือ **Machine Learning** ที่เรียนรู้ pattern จากข้อมูลแทนการเขียนกฎ ข้างในอีกชั้นคือ **Deep Learning** ซึ่งใช้ neural network หลายชั้นเรียน feature เอง และชั้นในสุดที่กำลังเป็นกระแสคือ **Generative AI** ที่ "สร้าง" ข้อมูลใหม่ เช่น LLM ซึ่งจะเรียนต่อในสัปดาห์ที่ 10

![แผนภาพวงกลมซ้อนกันสี่ชั้น AI ครอบ Machine Learning ครอบ Deep Learning ครอบ Generative AI พร้อมนิยามและตัวอย่างของแต่ละชั้น](/images/weeks/w09-ai-ml-dl.svg)

ข้อสังเกตสำคัญ: ทุก DL เป็น ML แต่ไม่ใช่ทุก ML เป็น DL เช่น Linear Regression ใน [Lab 09](/lab/09) เป็น ML ที่ไม่ใช่ deep learning และระบบไฟจราจรที่เขียน `if` ตามเวลาก็เป็น "AI แบบกฎ" ที่ไม่ได้เรียนรู้อะไรจากข้อมูลเลย

### 2. สามวิธีเรียนรู้: เปรียบกับการเรียนของนักศึกษา

- **Supervised learning** เหมือนทำแบบฝึกหัดที่ **มีเฉลย** ท้ายเล่ม: ทุกตัวอย่างมีคำตอบ (label) โมเดลปรับตัวจนตอบตรงเฉลย แล้วนำไปตอบข้อใหม่ที่ไม่เคยเห็น
- **Unsupervised learning** เหมือนได้กองรูปภาพที่ **ไม่มีป้ายชื่อ** แล้วจัดเป็นกอง ๆ ตามความคล้าย เช่น k-means จัดกลุ่มลูกค้า หรือหาค่าเซนเซอร์ที่ผิดปกติ
- **Reinforcement learning** เหมือนหัดขี่จักรยาน: ไม่มีใครบอกคำตอบทุกขั้น แต่ได้ **reward/penalty** จากผลการกระทำ (ล้ม = ลบ, ทรงตัวได้ = บวก) จึงค่อย ๆ หากลยุทธ์ที่ได้รางวัลรวมมากสุด

![กราฟสามช่องเปรียบเทียบ supervised ที่มี label และเส้นแบ่ง unsupervised ที่ k-means หากลุ่มเอง และ reinforcement ที่ reward เฉลี่ยเพิ่มขึ้นเมื่อลองมากขึ้น](/images/weeks/w09-learning-types.svg)

| ประเด็น | Supervised | Unsupervised | Reinforcement |
|---|---|---|---|
| ข้อมูลที่ใช้ | feature + label | feature อย่างเดียว | state, action, reward |
| คำถามที่ตอบ | "สิ่งนี้คืออะไร/เท่าไร" | "ข้อมูลแบ่งเป็นกลุ่มอย่างไร" | "ควรทำอะไรต่อ" |
| ตัวอย่างงาน | กรองสแปม, ทำนายอุณหภูมิ | จัดกลุ่มลูกค้า, หา anomaly | เกม, หุ่นยนต์เดิน, ควบคุมแอร์ |
| อัลกอริทึมตัวอย่าง | Linear/Logistic Regression, Decision Tree | k-means, PCA, Isolation Forest | Q-learning, policy gradient |
| วัดผลด้วย | accuracy, F1, MAE/RMSE | ความแน่นของกลุ่ม, ตรวจโดยผู้เชี่ยวชาญ | reward สะสม |

### 3. Worked example: นิวรอน 1 ตัวเรียนรู้ 1 รอบ

หัวข้อ 2 แสดง forward pass แล้ว ตัวอย่างนี้ไปต่ออีกขั้น คือ **ปรับ weight** ด้วย gradient descent ให้เห็นว่า "การเรียนรู้" คือการเปลี่ยนตัวเลขให้ loss ลดลง โจทย์: ควรเปิดพัดลมไหม? input (สเกล 0–1) คืออุณหภูมิ $x_1 = 0.8$ และความชื้น $x_2 = 0.6$ คำตอบจริง $y = 1$ (ควรเปิด) เริ่มต้น $w = [1.5,\ 0.5]$, $b = -1.0$, learning rate $= 1.0$

1. **Weighted sum:** $z = (1.5)(0.8) + (0.5)(0.6) - 1.0 = 1.2 + 0.3 - 1.0 = 0.5$
2. **Activation (sigmoid):** $\hat{y} = \dfrac{1}{1 + e^{-0.5}} \approx 0.622$ แปลว่าโมเดล "ค่อนข้างเห็นด้วย" ว่าควรเปิด
3. **Loss (squared error):** $(y - \hat{y})^2 = (1 - 0.622)^2 \approx 0.143$
4. **Gradient (chain rule):** $\dfrac{\partial L}{\partial z} = 2(\hat{y} - y)\,\hat{y}(1 - \hat{y}) \approx -0.177$ แล้ว $\dfrac{\partial L}{\partial w_i} = \dfrac{\partial L}{\partial z}\,x_i$
5. **Update:** $w_i \leftarrow w_i - \eta \dfrac{\partial L}{\partial w_i}$ ได้ $w \approx [1.642,\ 0.606]$, $b \approx -0.823$
6. **ตรวจผล:** คำนวณใหม่ได้ $\hat{y} \approx 0.702$ และ loss ลดจาก 0.143 เหลือ $\approx 0.089$

![แผนภาพนิวรอนหนึ่งตัว input สองค่าคูณ weight รวมกับ bias เป็น z เท่ากับ 0.5 ผ่าน sigmoid ได้ 0.622 พร้อมผลหลังปรับ weight หนึ่งรอบและกราฟ sigmoid](/images/weeks/w09-neuron.svg)

**ข้อสังเกต:** gradient $\partial L/\partial z$ เป็นค่าลบ (ควรเพิ่ม $z$) การลบ $\eta \cdot$ gradient ออกจาก weight จึงทำให้ weight **เพิ่มขึ้น** และ $\hat{y}$ ขยับเข้าใกล้ 1 การ train จริงทำซ้ำแบบนี้หลายพันรอบกับข้อมูลหลายตัวอย่าง นี่คือแก่นของ backpropagation ใน [หัวข้อ 2](/module/09/02)

### 4. วัดว่าโมเดล regression ดีแค่ไหน: MAE, MSE, RMSE

สมมติโมเดลทำนายอุณหภูมิห้อง 4 ชั่วโมง ค่าจริง $y = [30, 32, 31, 35]$ ค่าทำนาย $\hat{y} = [31, 31, 33, 34]$ error $e = y - \hat{y} = [-1, 1, -2, 1]$

- MAE $= (1 + 1 + 2 + 1)/4 = 1.25$ °C (ผิดเฉลี่ยกี่องศา อ่านง่ายสุด)
- MSE $= (1 + 1 + 4 + 1)/4 = 1.75$ °C² (ยกกำลังสอง ลงโทษ error ใหญ่หนักกว่า)
- RMSE $= \sqrt{1.75} \approx 1.32$ °C (กลับมาเป็นหน่วยเดิม แต่ยังไวต่อ error ใหญ่)

ห้ามนำ error มาบวกตรง ๆ เพราะค่าบวกและลบหักล้างกัน (ในตัวอย่างนี้ผลรวม $= -1$ ดูเหมือนดีเกินจริง) วิธีคำนวณและ gradient descent ของเส้นตรงฝึกต่อใน [Lab 09](/lab/09)

### 5. จาก notebook สู่ระบบจริง: MLOps เหมือนครัวร้านอาหาร

การทำโมเดลใน notebook เหมือน "ทำอาหารจานเดียวที่บ้าน" ส่วน MLOps คือ "ครัวร้านอาหาร" ที่ต้องมีสูตรมาตรฐาน (pipeline), จดว่าใช้วัตถุดิบล็อตไหน (data/model versioning), ชิมก่อนเสิร์ฟ (evaluation), เสิร์ฟทีละโต๊ะก่อนเปิดเต็มร้าน (canary deployment) และฟังเสียงลูกค้าตลอด (monitoring) เมื่อวัตถุดิบเปลี่ยน เช่น ฤดูกาลเปลี่ยนทำให้ข้อมูลเซนเซอร์เปลี่ยน (data drift) ก็ต้องปรับสูตรใหม่ (retrain) รายละเอียดอยู่ใน [หัวข้อ 4](/module/09/04) และ [หัวข้อ 5](/module/09/05)

### สรุปสั้น

- AI ⊃ ML ⊃ DL ⊃ GenAI ทุกชั้นในเป็นส่วนหนึ่งของชั้นนอก ไม่ใช่กลับกัน
- Supervised มี label, unsupervised ไม่มี label, reinforcement เรียนจาก reward
- นิวรอน: $z = \sum w_i x_i + b$ แล้วผ่าน activation เช่น sigmoid $\sigma(z) = 1/(1+e^{-z})$
- การเรียนรู้ = ปรับ $w, b$ ทีละน้อยในทิศที่ทำให้ loss ลด (gradient descent)
- Regression วัดด้วย MAE/MSE/RMSE ส่วน classification วัดด้วย accuracy/precision/recall/F1
- โมเดลที่ดีใน notebook ยังไม่พอ ต้องมี MLOps เพื่อ version, deploy, monitor และ retrain

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

> กลับ [[Learning Content Index]] · ดูแผนสัปดาห์ที่ 9: [[Week 09 - AI & Machine Learning Foundations]]
