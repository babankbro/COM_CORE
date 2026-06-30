---
type: chapter
status: complete
week: 3
clo: [CLO2]
tags: [curriculum, week03, logic, processor, risc-v, cpu, gpu, npu]
created: "2026-06-30"
updated: "2026-06-30"
---

# สัปดาห์ที่ 3: วงจรตรรกะและหน่วยประมวลผล

> [!abstract] สาระสำคัญ
> คอมพิวเตอร์ "คิด" ด้วยเลขฐานสอง (0/1) ผ่าน **เกตตรรก** ที่ประกอบเป็นวงจรเชิงผสม/เชิงลำดับ จนกลายเป็นหน่วยประมวลผลที่ทำงานตามวงรอบ fetch–decode–execute

## 🎯 วัตถุประสงค์การสอน (Learning Objectives)
1. ผู้เรียนสามารถอธิบายหลักการทำงานของวงจรตรรกะ (Logic Circuits) พื้นฐานได้ — *CLO2*
2. ผู้เรียนเข้าใจสถาปัตยกรรมไมโครโปรเซสเซอร์ โดยเฉพาะสถาปัตยกรรมแบบเปิด [[RISC-V]] — *CLO2*
3. ผู้เรียนสามารถเปรียบเทียบ CPU, GPU, NPU และ TPU ได้ — *CLO2*

## 📝 สรุปเนื้อหาหัวข้อ (Topics Covered)
- พีชคณิตบูลีนและวงจรตรรกะพื้นฐาน ([[Boolean Algebra และ Logic Gates]])
- โครงสร้างและสถาปัตยกรรมไมโครโปรเซสเซอร์ ([[von Neumann Architecture]])
- สถาปัตยกรรม [[RISC-V]] (Open Standard ISA)
- หน่วยประมวลผลยุคใหม่: GPU, NPU, TPU สำหรับ AI

## 📖 เนื้อหาโดยละเอียด
- **ระบบเลข:** ฐานสอง/ฐานสิบหก, two's complement
- **พีชคณิตบูลีน:** AND/OR/NOT/NAND/NOR/XOR, ตารางความจริง, การลดรูป K-map
- **วงจรเชิงผสม:** half/full adder, multiplexer, decoder; **วงจรเชิงลำดับ:** flip-flop, register, counter, clock
- **สถาปัตยกรรม:** [[von Neumann Architecture]], ALU + Control Unit + Registers, วงรอบ fetch–decode–execute, pipeline, cache
- **ประเภทหน่วยประมวลผล:** CPU (อเนกประสงค์), GPU (ขนาน), NPU/TPU (เร่ง AI), ASIC (เฉพาะงาน)

## 🔑 แนวคิดหลัก (Key Concepts)
[[Boolean Algebra และ Logic Gates]] · [[von Neumann Architecture]] · [[RISC-V]] · [[Chiplet]]

## 📈 แนวโน้มปัจจุบัน (2025–2026)
- **กฎของมัวร์ชะลอตัว:** ผลิตระดับ **2nm** เชิงพาณิชย์แต่ต้นทุนสูง (~30,000 USD/wafer ในปี 2026)
- **สถาปัตยกรรม [[Chiplet]]:** ใช้ชิปเล็ตหลายชิ้นเฉพาะทางต่อกันด้วย advanced packaging
- **ยุคตัวเร่ง AI (AI accelerators):** GPU ก้อนเดียวไม่ใช่ค่าเริ่มต้นอีกต่อไป ตลาดตัวเร่ง AI โตหลายแสนล้านดอลลาร์ภายในปี 2030 (เชื่อม [[Week 07 - Data Center & Cloud Infrastructure]])

## 🧪 กิจกรรม/ปฏิบัติการ (OBE) — Lab 2
Lab 1 ชม. (จำลองวงจร Logisim) + Project 1 ชม. (สร้างฟังก์ชันตรรกะประมวลผลข้อมูล) — **Module 1: Foundation & Programming**
> อ้างอิงจากแผน 4 โมดูล: ดูรายละเอียดเต็มที่ [[กิจกรรมปฏิบัติการและโครงงาน]]

## ❓ คำถามทบทวน
1. แปลง 1101₂ และ 0x2F เป็นเลขฐานสิบ
2. เขียนตารางความจริง XOR และอธิบายการใช้งานใน adder
3. CPU, GPU, NPU เหมาะกับงานต่างกันอย่างไร

## 📚 อ้างอิง (References)
- Mano, M. M., & Ciletti, M. *Digital Design*. Pearson.
- Patterson, D. A., & Waterman, A. (2017). *The RISC-V Reader: An Open Architecture Atlas*. Strawberry Canyon.
- ACM/IEEE-CS. (2016). *CE2016* — Computer Architecture and Organization (CAO).
- HPCwire. *2026 Semiconductor Predictions: Here Come the AI Accelerators.* [hpcwire.com](https://www.hpcwire.com/2026/01/06/2026-semiconductor-predictions-here-come-the-ai-accelerators/)
- PatentPC. *The Future of Semiconductor Scaling: Beyond 2nm Chips.* [patentpc.com](https://patentpc.com/blog/the-future-of-semiconductor-scaling-beyond-2nm-chips-market-trends-growth-data)

## 🔗 นำทาง
⬅️ [[Week 02 - Hardware & Software Ecosystems]] · ➡️ [[Week 04 - Algorithms & Programming Paradigms]]
