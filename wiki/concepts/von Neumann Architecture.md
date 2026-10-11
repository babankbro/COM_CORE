---
type: concept
status: complete
source_chapters: [Week 03]
first_appearance: "Week 03 - Digital Logic & Modern Processors"
tags: [concept, architecture, processor]
created: "2026-06-30"
updated: "2026-10-12"
---

# von Neumann Architecture (สถาปัตยกรรมฟอน นอยมันน์)

## Definition
แบบจำลองพื้นฐานของคอมพิวเตอร์ที่เก็บ **ทั้งคำสั่งและข้อมูลไว้ในหน่วยความจำเดียวกัน** ประกอบด้วยหน่วยควบคุม (Control Unit), หน่วยคำนวณตรรก (ALU), หน่วยความจำ และ I/O ทำงานตามวงรอบ fetch–decode–execute

## Course Context
เป็นแกนของหัวข้อหน่วยประมวลผล ([[Week 03 - Digital Logic & Modern Processors]]) ใช้เป็นฐานเปรียบเทียบกับสถาปัตยกรรมขนาน (GPU) และตัวเร่ง AI (NPU/TPU); "von Neumann bottleneck" อธิบายข้อจำกัดด้านแบนด์วิดท์หน่วยความจำ

## ส่วนประกอบของ CPU และวงรอบ Fetch–Decode–Execute
**ส่วนประกอบหลัก**
- **Control Unit (CU):** ดึงคำสั่ง ถอดรหัส และส่งสัญญาณควบคุมให้ส่วนอื่นทำงาน
- **ALU:** คำนวณทางคณิตศาสตร์และตรรกะ
- **Registers:** PC (address คำสั่งถัดไป), IR (คำสั่งปัจจุบัน), MAR (address ที่จะอ่าน/เขียน), MDR (ข้อมูลที่อ่าน/เขียน), ACC/general-purpose (ผลการคำนวณ)
- **Buses:** Address bus (ส่ง address), Data bus (ส่งข้อมูล/คำสั่ง), Control bus (สัญญาณ Read/Write/Clock)

**ขั้นตอนวงรอบ**
1. **Fetch:** MAR ← PC → อ่านหน่วยความจำได้ MDR → IR ← MDR → PC ← PC + 1
2. **Decode:** Control Unit ถอดรหัสคำสั่งใน IR
3. **Execute:** ALU คำนวณ หรืออ่าน/เขียนข้อมูลในหน่วยความจำ
4. **Write-back:** เก็บผลลง register หรือหน่วยความจำ แล้ววนกลับไป Fetch

เนื่องจากการดึงคำสั่งและการอ่าน/เขียนข้อมูลใช้บัสเดียวกัน จึงเกิด von Neumann bottleneck ดูตัวอย่างการไล่โปรแกรม LOAD/ADD/STORE ทีละขั้นในเนื้อหาสัปดาห์ [[Week 03 - Digital Logic & Modern Processors]]

## อ้างอิง
- Patterson, D. A., & Hennessy, J. L. *Computer Organization and Design.* Morgan Kaufmann.
