## คำถามนำ
คอมพิวเตอร์แปลง 0/1 ให้กลายเป็นการคำนวณและการตัดสินใจได้อย่างไร?

## ผลลัพธ์การเรียนรู้ย่อย
1. อธิบาย Boolean algebra และ logic gates
2. เชื่อมวงจรพื้นฐานกับ ALU/register/control unit
3. เปรียบเทียบ CPU, GPU, NPU และ RISC-V

## แก่นความรู้ที่ต้องเข้าใจ
- logic gate เป็นหน่วยเล็กที่สุดของการตัดสินใจเชิงดิจิทัล เมื่อนำมาประกอบกันจะเกิด adder, register และวงจรควบคุม
- fetch-decode-execute คือวงจรพื้นฐานของ processor: ดึงคำสั่ง แปลคำสั่ง แล้วดำเนินการ
- RISC-V เป็น ISA แบบเปิด ทำให้ผู้เรียนเห็นว่าชุดคำสั่งเป็นสัญญาระหว่างซอฟต์แวร์กับฮาร์ดแวร์

## เนื้อหาเรียนรู้
- เริ่มจากตารางความจริงของ AND, OR, XOR แล้วให้ผู้เรียนสร้าง half-adder จาก XOR และ AND เพื่อเห็นว่าการบวกเลขเริ่มจากตรรกะพื้นฐาน
- อธิบาย von Neumann architecture ด้วยเส้นทางข้อมูล: memory เก็บคำสั่งและข้อมูล, CPU มี ALU/control/register, bus เป็นทางสื่อสาร
- ปิดด้วย processor ยุค AI: GPU/NPU ไม่ได้แทน CPU แต่ทำหน้าที่เร่งงานเฉพาะ เช่น matrix multiplication และ inference

## 🧭 อธิบายเพิ่มเติม (ฉบับขยาย)

### 1. เกตตรรกะคือ "สวิตช์ไฟที่ตัดสินใจได้"
ทรานซิสเตอร์ในชิปทำหน้าที่คล้ายสวิตช์ เปิด = 1 ปิด = 0 เมื่อนำสวิตช์มาต่อกันแบบต่าง ๆ จะได้กฎการตัดสินใจง่าย ๆ ที่เรียกว่า logic gate
- **AND** เหมือนประตูนิรภัยที่ต้องใช้กุญแจ 2 ดอกพร้อมกัน ขาด 1 ดอกก็เปิดไม่ได้
- **OR** เหมือนไฟทางเดินที่มีสวิตช์ 2 จุด กดจุดใดก็สว่าง
- **NOT** เหมือนป้าย "ห้าม" กลับค่าทุกอย่าง
- **XOR** เหมือนไฟบันไดที่มีสวิตช์หัวและท้ายบันได ไฟติดเมื่อสวิตช์อยู่ต่างตำแหน่งกันเท่านั้น จึงใช้ตรวจว่า "สองค่าต่างกันไหม"

ในเกมของเรา เงื่อนไข `has_key and (not is_night or hp > 50)` ก็คือวงจร AND-OR-NOT ที่เขียนเป็นโค้ด คอมพิวเตอร์จึงตัดสินใจด้วยตรรกะเดียวกันทั้งในระดับวงจรและระดับโปรแกรม ตารางความจริงครบ 7 เกตและ universal gate อ่านได้ที่ [พื้นฐานวงจรตรรกะสู่การออกแบบชิป](/module/03/01)

### 2. ทำไม XOR กับ AND จึงบวกเลขได้
การบวกเลขฐานสองหนึ่งหลักมีเพียง 4 กรณี: 0+0=0, 0+1=1, 1+0=1 และ 1+1=10₂ (เขียน 0 ทด 1) ถ้าแยกผลออกเป็น 2 ส่วน
- หลักผลรวม **S** เป็น 1 เมื่อบิตต่างกัน = นิยามของ **XOR** พอดี
- ตัวทด **C** เป็น 1 เมื่อบิตเป็น 1 ทั้งคู่ = นิยามของ **AND** พอดี

วงจรนี้เรียกว่า **Half Adder** แต่ใช้ได้เฉพาะหลักขวาสุด เพราะหลักถัดไปต้องรับตัวทดจากหลักก่อนหน้าด้วย จึงต้องใช้ **Full Adder** ที่รับ 3 อินพุต (A, B, Cin) สร้างจาก Half Adder 2 ตัวกับ OR 1 ตัว

![แผนภาพวงจร Half Adder ที่ต่อ A และ B เข้า XOR ได้ S และเข้า AND ได้ C พร้อมตารางความจริง และ Full Adder ที่ต่อ Half Adder 2 ตัวกับเกต OR ได้ S = A XOR B XOR Cin และ Cout = AB + Cin(A XOR B)](/images/weeks/w03-adders.svg)

### 3. ตัวอย่างทีละขั้น: บวก 6 + 7 ด้วย 4-bit Ripple-Carry Adder
6 = 0110₂ และ 7 = 0111₂ นำ Full Adder 4 ตัวมาเรียงกัน บิตขวาสุด (LSB) เริ่มด้วย Cin = 0
1. **บิต 0:** A0=0, B0=1, Cin=0 → S0 = 1, carry ออก = 0
2. **บิต 1:** A1=1, B1=1, Cin=0 → S1 = 0, carry ออก = 1 (1+1 ต้องทด)
3. **บิต 2:** A2=1, B2=1, Cin=1 → S2 = 1, carry ออก = 1 (1+1+1 = 11₂)
4. **บิต 3:** A3=0, B3=0, Cin=1 → S3 = 1, carry ออก = 0
5. อ่านผลจากซ้ายไปขวา: S = 1101₂ = 8 + 4 + 0 + 1 = **13** และ Cout = 0 จึงไม่ overflow

![แผนภาพ Full Adder 4 ตัวเรียงจากบิต 0 ทางขวาไปบิต 3 ทางซ้าย บวก 0110 กับ 0111 แสดงค่า carry ที่ส่งต่อระหว่างบิตคือ 0, 1, 1 ได้ผลรวม 1101 เท่ากับ 13 และ Cout เท่ากับ 0](/images/weeks/w03-ripple-carry.svg)

ข้อสังเกต: carry ต้อง "วิ่งเป็นระลอก" ผ่านทุกบิต ถ้าเป็น 64 บิตก็ต้องรอ 64 ช่วง CPU จริงจึงใช้เทคนิค carry-lookahead เพื่อคำนวณ carry ล่วงหน้า และถ้าบวก 9 + 8 ใน 4 บิตจะได้ Cout = 1 คือผลเกิน 15 (overflow) ซึ่ง CPU ต้องตั้ง flag แจ้งโปรแกรม ทดลองโค้ดเดียวกันนี้ได้ใน Lab 03 ขั้นตอนที่ 5

### 4. จากวงจรบวกสู่ CPU: วงรอบ Fetch–Decode–Execute
เมื่อนำ adder และวงจรตรรกะอื่นมารวมกันจะได้ **ALU** เพิ่ม **register** สำหรับเก็บค่าชั่วคราว และ **control unit** สำหรับสั่งงาน ก็ได้ CPU ที่ทำงานตามคำสั่งในหน่วยความจำ เปรียบเหมือนพ่อครัวที่อ่านสูตรอาหารทีละบรรทัด: หยิบบรรทัดถัดไป (fetch) อ่านว่าให้ทำอะไร (decode) ลงมือทำ (execute) แล้วจดผลลงจาน (write back)

![แผนภาพ von Neumann แสดง CPU ที่มี Control Unit, ALU และ register PC IR x1 x2 x3 เชื่อมผ่าน bus กับหน่วยความจำที่เก็บทั้งคำสั่งและข้อมูล พร้อม 4 ขั้นของการรันคำสั่ง add x3, x1, x2 คือ fetch decode execute และ write back ได้ x3 เท่ากับ 13 และ PC เพิ่มขึ้น 4](/images/weeks/w03-fde-cycle.svg)

ตัวอย่างคำสั่ง RISC-V `add x3, x1, x2` เมื่อ x1 = 6 และ x2 = 7
1. **Fetch:** อ่านคำสั่งจากหน่วยความจำตำแหน่งที่ PC ชี้ (0x100) มาเก็บใน IR
2. **Decode:** control unit แปลว่าเป็นคำสั่งบวก ใช้ x1 และ x2 เป็นต้นทาง x3 เป็นปลายทาง
3. **Execute:** ALU คำนวณ 6 + 7 = 13 (ภายในคือ adder แบบเดียวกับข้อ 3 แต่กว้าง 32 หรือ 64 บิต)
4. **Write back:** เขียน 13 ลง x3 และเพิ่ม PC ทีละ 4 เพราะคำสั่ง RISC-V พื้นฐานยาว 32 บิต = 4 ไบต์

เนื่องจากคำสั่งและข้อมูลใช้ bus เดียวกัน CPU จึงอาจต้องรอหน่วยความจำ เรียกว่า **von Neumann bottleneck** ซึ่งเป็นเหตุผลที่มี cache และสถาปัตยกรรมแบบ Harvard ดูรายละเอียดที่ [สถาปัตยกรรม von Neumann และ Harvard](/module/03/02)

### 5. ตารางเปรียบเทียบสถาปัตยกรรมและหน่วยประมวลผล

| หัวข้อ | von Neumann | Harvard | Modified Harvard (ปัจจุบัน) |
|---|---|---|---|
| หน่วยความจำ | คำสั่งและข้อมูลอยู่รวมกัน | แยกหน่วยความจำคำสั่งกับข้อมูล | หน่วยความจำหลักรวม แต่แยก L1 cache คำสั่ง/ข้อมูล |
| Bus | ชุดเดียว | แยกสองชุด อ่านพร้อมกันได้ | แยกที่ระดับ cache |
| ข้อดี | ออกแบบง่าย ยืดหยุ่น | เร็ว คาดเดาเวลาได้ | ได้ทั้งความยืดหยุ่นและความเร็ว |
| พบใน | แนวคิดพื้นฐานของคอมพิวเตอร์ทั่วไป | ไมโครคอนโทรลเลอร์และ DSP จำนวนมาก | CPU ใน PC มือถือ และเซิร์ฟเวอร์ |

| หน่วยประมวลผล | จุดเด่น | เหมาะกับ |
|---|---|---|
| CPU | ยืดหยุ่น คำสั่งซับซ้อนได้ | OS, ลอจิกของเกม, งานทั่วไป |
| GPU | คอร์จำนวนมากทำงานขนาน | กราฟิก, train โมเดล |
| NPU/TPU | อาร์เรย์คูณ-บวกเมทริกซ์ (systolic array) | AI inference/training อย่างประหยัดไฟ |
| ASIC | ออกแบบเพื่องานเดียว เร็วและประหยัดที่สุด | งานเฉพาะ เช่น ถอดรหัสวิดีโอ |

### 6. ISA: สัญญาระหว่างซอฟต์แวร์กับฮาร์ดแวร์
ISA (Instruction Set Architecture) เหมือน "เมนูร้านอาหาร" ที่บอกว่าสั่งอะไรได้บ้าง ลูกค้า (คอมไพเลอร์/โปรแกรม) ไม่ต้องรู้ว่าครัวจัดเตาอย่างไร ขอแค่สั่งตามเมนู ส่วนร้าน (ผู้ผลิตชิป) จะปรับครัวให้เร็วขึ้นอย่างไรก็ได้ตราบที่เมนูเหมือนเดิม RISC-V เป็นเมนูแบบเปิดที่ใครก็นำไปทำชิปได้โดยไม่ต้องจ่ายค่าสิทธิ์ ISA จึงเหมาะกับการเรียนและนวัตกรรม ([เจาะลึกสถาปัตยกรรม RISC-V](/module/03/03)) ขณะที่ยุคหลังกฎของมัวร์หันไปใช้ตัวเร่งเฉพาะทางและ chiplet แทนการย่อทรานซิสเตอร์อย่างเดียว ([AI Accelerators](/module/03/04), [หัวข้อ 5](/module/03/05))

### สรุปสั้น
- logic gate คือหน่วยตัดสินใจที่เล็กที่สุด เงื่อนไข if ในโปรแกรมก็คือ Boolean logic แบบเดียวกัน
- Half Adder: S = A XOR B, C = A AND B · Full Adder = Half Adder 2 ตัว + OR
- Ripple-carry adder ส่ง carry ทีละบิต 6 + 7 = 0110₂ + 0111₂ = 1101₂ = 13 และ Cout = 1 หมายถึง overflow
- CPU ทำงานเป็นวงรอบ fetch → decode → execute → write back โดย PC ชี้คำสั่งถัดไป
- von Neumann ใช้หน่วยความจำและ bus ร่วมกันจึงมีคอขวด CPU ปัจจุบันจึงแยก cache คำสั่ง/ข้อมูล
- ISA คือสัญญาระหว่างซอฟต์แวร์กับฮาร์ดแวร์ RISC-V เป็น ISA แบบเปิด

## กิจกรรมในชั้นเรียน / ปฏิบัติการ
ใช้ Logisim หรือ simulator สร้าง half-adder/full-adder แล้วเขียนเงื่อนไขเกมที่ใช้ Boolean logic อย่างน้อย 3 เงื่อนไข

## คำถามตรวจความเข้าใจ
1. XOR ใช้ใน adder เพราะอะไร?
2. fetch-decode-execute มีขั้นตอนใดบ้าง?
3. RISC-V ต่างจาก ISA ปิดในเชิงการเรียนรู้และนวัตกรรมอย่างไร?

## ชิ้นงาน / หลักฐานการเรียนรู้
- สรุปแนวคิด 1 หน้า หรือ concept map ของสัปดาห์นี้
- ผลกิจกรรม/โค้ด/diagram ตามโจทย์ประจำสัปดาห์
- คำตอบสะท้อนคิด: วันนี้เข้าใจอะไรเพิ่ม และยังสงสัยอะไร

## Research เพิ่มเติมและแหล่งอ้างอิง
**หัวข้อวิจัยเสริม:** Digital logic, processor architecture และ RISC-V

- RISC-V เป็น open standard ISA ที่ดีสำหรับการสอน เพราะแยกชัดเจนระหว่าง instruction set กับ implementation ของ processor
- แนวโน้ม chiplet และ accelerator ทำให้บทเรียน CPU/GPU/NPU ควรเน้น trade-off: งานทั่วไป งานขนาน งาน AI และข้อจำกัดด้านพลังงาน/ความร้อน
- กิจกรรมควรพาผู้เรียนจาก truth table ไปสู่ adder/register แล้วเชื่อมกับ fetch-decode-execute เพื่อไม่ให้วงจรตรรกะดูแยกจาก processor จริง

**แหล่งอ้างอิงข้อมูล:**
- [RISC-V International](https://riscv.org/)
- [RISC-V Specifications](https://riscv.org/technical/specifications/)
- [The RISC-V Instruction Set Manual](https://github.com/riscv/riscv-isa-manual)

## แหล่งค้นคว้าเพิ่มเติม
- [RISC-V International](https://riscv.org/)
- [ACM/IEEE Computer Engineering Curricula 2016](https://www.acm.org/binaries/content/assets/education/ce2016-final-report.pdf)

---

## 🗓️ แผนการสอนประจำสัปดาห์ (Teaching Plan)

> [!abstract] สาระสำคัญ
> คอมพิวเตอร์ "คิด" ด้วยเลขฐานสอง (0/1) ผ่าน **เกตตรรก** ที่ประกอบเป็นวงจรเชิงผสม/เชิงลำดับ จนกลายเป็นหน่วยประมวลผลที่ทำงานตามวงรอบ fetch–decode–execute

### 🎯 วัตถุประสงค์การสอน (Learning Objectives)
1. ผู้เรียนสามารถอธิบายหลักการทำงานของวงจรตรรกะ (Logic Circuits) พื้นฐานได้ — *CLO2*
2. ผู้เรียนเข้าใจสถาปัตยกรรมไมโครโปรเซสเซอร์ โดยเฉพาะสถาปัตยกรรมแบบเปิด [RISC-V](/concept/risc-v) — *CLO2*
3. ผู้เรียนสามารถเปรียบเทียบ CPU, GPU, NPU และ TPU ได้ — *CLO2*

### 📝 สรุปเนื้อหาหัวข้อ (Topics Covered)
- พีชคณิตบูลีนและวงจรตรรกะพื้นฐาน ([Boolean Algebra และ Logic Gates](/concept/boolean-algebra-logic-gates))
- โครงสร้างและสถาปัตยกรรมไมโครโปรเซสเซอร์ ([von Neumann Architecture](/concept/von-neumann-architecture))
- สถาปัตยกรรม [RISC-V](/concept/risc-v) (Open Standard ISA)
- หน่วยประมวลผลยุคใหม่: GPU, NPU, TPU สำหรับ AI

### 📖 เนื้อหาโดยละเอียด
- **ระบบเลข:** ฐานสอง/ฐานสิบหก, two's complement
- **พีชคณิตบูลีน:** AND/OR/NOT/NAND/NOR/XOR, ตารางความจริง, การลดรูป K-map
- **วงจรเชิงผสม:** half/full adder, multiplexer, decoder; **วงจรเชิงลำดับ:** flip-flop, register, counter, clock
- **สถาปัตยกรรม:** [von Neumann Architecture](/concept/von-neumann-architecture), ALU + Control Unit + Registers, วงรอบ fetch–decode–execute, pipeline, cache
- **ประเภทหน่วยประมวลผล:** CPU (อเนกประสงค์), GPU (ขนาน), NPU/TPU (เร่ง AI), ASIC (เฉพาะงาน)

### 🔑 แนวคิดหลัก (Key Concepts)
[Boolean Algebra และ Logic Gates](/concept/boolean-algebra-logic-gates) · [von Neumann Architecture](/concept/von-neumann-architecture) · [RISC-V](/concept/risc-v) · [Chiplet](/concept/chiplet)

### 📈 แนวโน้มปัจจุบัน (2025–2026)
- **กฎของมัวร์ชะลอตัว:** ผลิตระดับ **2nm** เชิงพาณิชย์แต่ต้นทุนสูง (~30,000 USD/wafer ในปี 2026)
- **สถาปัตยกรรม [Chiplet](/concept/chiplet):** ใช้ชิปเล็ตหลายชิ้นเฉพาะทางต่อกันด้วย advanced packaging
- **ยุคตัวเร่ง AI (AI accelerators):** GPU ก้อนเดียวไม่ใช่ค่าเริ่มต้นอีกต่อไป ตลาดตัวเร่ง AI โตหลายแสนล้านดอลลาร์ภายในปี 2030 (เชื่อม [สัปดาห์ที่ 7: Data Center & Cloud Infrastructure](/module/07))

### 🧪 กิจกรรม/ปฏิบัติการ (OBE) — Lab 2
Lab 1 ชม. (จำลองวงจร Logisim) + Project 1 ชม. (เขียนเงื่อนไข/ตรรกะ (Game Logic) ของตัวเกม) — **Module 1: Foundation & Programming**
> อ้างอิงจากแผน 4 โมดูล: ดูรายละเอียดเต็มที่ [กิจกรรมปฏิบัติการและโครงงาน](/docs/labs-projects)

### ❓ คำถามทบทวน
1. แปลง 1101₂ และ 0x2F เป็นเลขฐานสิบ
2. เขียนตารางความจริง XOR และอธิบายการใช้งานใน adder
3. CPU, GPU, NPU เหมาะกับงานต่างกันอย่างไร

### 📚 อ้างอิง (References)
- Mano, M. M., & Ciletti, M. *Digital Design*. Pearson.
- Patterson, D. A., & Waterman, A. (2017). *The RISC-V Reader: An Open Architecture Atlas*. Strawberry Canyon.
- ACM/IEEE-CS. (2016). *CE2016* — Computer Architecture and Organization (CAO).
- HPCwire. *2026 Semiconductor Predictions: Here Come the AI Accelerators.* [hpcwire.com](https://www.hpcwire.com/2026/01/06/2026-semiconductor-predictions-here-come-the-ai-accelerators/)
- PatentPC. *The Future of Semiconductor Scaling: Beyond 2nm Chips.* [patentpc.com](https://patentpc.com/blog/the-future-of-semiconductor-scaling-beyond-2nm-chips-market-trends-growth-data)

---

## 📚 เนื้อหาเชิงลึกประจำสัปดาห์ (Deep Dive)

- [01. จาก Logic Gates สู่ Chip Design](/module/03/01)
- [02. สถาปัตยกรรม von Neumann vs Harvard](/module/03/02)
- [03. เจาะลึกสถาปัตยกรรม RISC-V](/module/03/03)
- [04. หน่วยเร่งประมวลผล AI (NPU และ TPU)](/module/03/04)
- [05. เทคโนโลยี Chiplet และยุค Post-Moore's Law](/module/03/05)
