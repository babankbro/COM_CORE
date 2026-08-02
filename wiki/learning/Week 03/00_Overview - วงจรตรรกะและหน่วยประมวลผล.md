---
type: learning
status: complete
week: 3
source_week: "Week 03 - Digital Logic & Modern Processors"
tags: [learning, week03, en-001-019]
created: "2026-08-03"
updated: "2026-08-03"
---

# Learning Content Week 03: วงจรตรรกะและหน่วยประมวลผล

> ใช้คู่กับ [[Week 03 - Digital Logic & Modern Processors]] สำหรับอ่านก่อนเรียน ทบทวนหลังเรียน และเตรียมกิจกรรมปฏิบัติการ

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

> กลับ [[Learning Content Index]] · ดูแผนสัปดาห์ที่ 3: [[Week 03 - Digital Logic & Modern Processors]]
