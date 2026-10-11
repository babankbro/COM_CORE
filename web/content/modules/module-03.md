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
