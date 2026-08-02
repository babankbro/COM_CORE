---
type: learning
status: complete
week: 5
source_week: "Week 05 - Database & Data Management"
tags: [learning, week05, en-001-019]
created: "2026-08-03"
updated: "2026-08-03"
---

# Learning Content Week 05: ฐานข้อมูลและการจัดการข้อมูลขนาดใหญ่

> ใช้คู่กับ [[Week 05 - Database & Data Management]] สำหรับอ่านก่อนเรียน ทบทวนหลังเรียน และเตรียมกิจกรรมปฏิบัติการ

## คำถามนำ
ข้อมูลควรถูกจัดเก็บอย่างไรให้ค้นหา เชื่อมโยง และนำไปใช้กับ AI ได้?

## ผลลัพธ์การเรียนรู้ย่อย
1. เข้าใจ relational database และ SQL
2. อธิบาย key, ER diagram, normalization และ ACID
3. รู้จัก vector database สำหรับ semantic search/RAG

## แก่นความรู้ที่ต้องเข้าใจ
- ฐานข้อมูลเชิงสัมพันธ์จัดข้อมูลเป็นตารางและความสัมพันธ์ ทำให้ลดความซ้ำซ้อนและ query ได้ชัดเจน
- SQL เป็นภาษากลางสำหรับถามข้อมูล เช่น SELECT, JOIN, WHERE, GROUP BY
- vector database เก็บ embedding เพื่อค้นหาความหมาย ไม่ใช่แค่คำตรงตัว จึงสำคัญกับ RAG และ LLM

## เนื้อหาเรียนรู้
- เริ่มด้วยกรณีระบบนักศึกษา: ตาราง Student, Course, Enrollment ช่วยให้เห็น primary key และ foreign key ชัดกว่าอธิบายเชิงนิยามอย่างเดียว
- ACID คือหลักที่ทำให้ธุรกรรมเชื่อถือได้ เช่นการโอนเงินหรือบันทึกคะแนนต้องครบ ถูกต้อง แยกจากกัน และไม่หายเมื่อระบบล่ม
- เชื่อมสู่ยุค AI: embedding เปลี่ยนข้อความเป็นเวกเตอร์ แล้วค้นหาด้วย similarity search เช่น cosine distance เพื่อดึงเอกสารที่เกี่ยวข้องให้ LLM ตอบ

## กิจกรรมในชั้นเรียน / ปฏิบัติการ
ออกแบบ ER diagram ของระบบเกม/ร้านค้าเล็ก ๆ แล้วเขียน SQL อย่างน้อย 3 คำสั่ง รวม SELECT แบบ JOIN

## คำถามตรวจความเข้าใจ
1. primary key กับ foreign key ต่างกันอย่างไร?
2. normalization ช่วยลดปัญหาใด?
3. vector search ต่างจาก keyword search อย่างไร?

## ชิ้นงาน / หลักฐานการเรียนรู้
- สรุปแนวคิด 1 หน้า หรือ concept map ของสัปดาห์นี้
- ผลกิจกรรม/โค้ด/diagram ตามโจทย์ประจำสัปดาห์
- คำตอบสะท้อนคิด: วันนี้เข้าใจอะไรเพิ่ม และยังสงสัยอะไร

## Research เพิ่มเติมและแหล่งอ้างอิง
**หัวข้อวิจัยเสริม:** Database, vector search และ AI-ready data

- Vector database เพิ่มความสามารถ semantic search จาก embedding จึงควรสอนคู่กับ SQL/NoSQL เพื่อให้ผู้เรียนเห็นว่าข้อมูลสำหรับ AI มีทั้ง structured และ unstructured
- pgvector แสดงแนวทาง practical ว่า relational database อย่าง PostgreSQL สามารถเก็บ vector และทำ similarity search ร่วมกับข้อมูลตารางเดิมได้
- SQL Server 2025 เพิ่ม vector data type อย่างเป็นทางการ สะท้อนว่า vector กลายเป็น capability ในฐานข้อมูลหลัก ไม่ใช่เครื่องมือเฉพาะทางเท่านั้น

**แหล่งอ้างอิงข้อมูล:**
- [pgvector: Open-source vector similarity search for Postgres](https://github.com/pgvector/pgvector)
- [Microsoft Learn: Vectors in SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/ai/vectors?view=sql-server-ver17)
- [Microsoft Learn: Vector data type](https://learn.microsoft.com/en-us/sql/t-sql/data-types/vector-data-type?view=sql-server-ver17)

## แหล่งค้นคว้าเพิ่มเติม
- [pgvector: Vector similarity search for PostgreSQL](https://github.com/pgvector/pgvector)
- [Microsoft Learn: SQL Server vector search](https://learn.microsoft.com/en-us/sql/sql-server/ai/vectors?view=sql-server-ver17)

> กลับ [[Learning Content Index]] · ดูแผนสัปดาห์ที่ 5: [[Week 05 - Database & Data Management]]
