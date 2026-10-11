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

---

## 🗓️ แผนการสอนประจำสัปดาห์ (Teaching Plan)

> [!abstract] สาระสำคัญ
> ฐานข้อมูลคือระบบจัดเก็บ/จัดการข้อมูลอย่างมีโครงสร้าง โมเดลหลักคือ **เชิงสัมพันธ์ (relational)** ที่ใช้ตารางและ SQL ปัจจุบันมี [Vector Database](/concept/vector-database) เป็นหมวดใหม่สำหรับงาน AI

### 🎯 วัตถุประสงค์การสอน (Learning Objectives)
1. ผู้เรียนเข้าใจหลักการของฐานข้อมูลเชิงสัมพันธ์ (Relational) และไม่เชิงสัมพันธ์ (NoSQL) — *CLO3*
2. ผู้เรียนรู้จักแนวคิด Big Data และการจัดการข้อมูลขนาดใหญ่ — *CLO3*
3. ผู้เรียนเข้าใจความสำคัญและสถาปัตยกรรมของ [Vector Database](/concept/vector-database) ในยุค AI — *CLO3*

### 📝 สรุปเนื้อหาหัวข้อ (Topics Covered)
- ฐานข้อมูลเชิงสัมพันธ์และภาษา SQL
- NoSQL และ Big Data Analytics
- [Vector Database](/concept/vector-database) (เช่น Pinecone, Milvus) สำหรับ [LLM/RAG](/concept/rag-llm)

### 📖 เนื้อหาโดยละเอียด
- **DBMS:** ตัวกลางระหว่างผู้ใช้/แอปกับข้อมูล (MySQL, PostgreSQL, SQLite, Oracle)
- **โมเดลเชิงสัมพันธ์:** ตาราง/แถว/คอลัมน์, primary/foreign key, ER diagram, normalization
- **SQL:** `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `JOIN`, `WHERE`, `GROUP BY`
- **ACID:** Atomicity, Consistency, Isolation, Durability
- **SQL vs NoSQL:** โครงสร้างชัด vs ยืดหยุ่น/ขยายแนวนอน (document, key-value, graph)

### 🔑 แนวคิดหลัก (Key Concepts)
[Vector Database](/concept/vector-database) · [RAG และ LLM](/concept/rag-llm)

### 📈 แนวโน้มปัจจุบัน (2025–2026)
- **ฐานข้อมูลเวกเตอร์** รองรับ RAG/semantic search/ความจำของ AI agents — ตลาด ~3.2 พันล้านดอลลาร์ในปี 2025 โต ~24%/ปี
- **เวกเตอร์กลายเป็น "ชนิดข้อมูล":** ฐานข้อมูลหลักผนวกเข้าไป เช่น **SQL Server 2025** เพิ่มชนิด `VECTOR` + DiskANN; กำลังร่างส่วนขยาย ANSI SQL
- **Hybrid search:** ผสม vector + keyword + metadata + graph เป็นมาตรฐานใหม่

### 🧪 กิจกรรม/ปฏิบัติการ (OBE) — Lab 5
Lab 1 ชม. (ออกแบบ ER และ SQL) + Project 1 ชม. (ต่อฐานข้อมูล SQLite กับ Python/Node.js) — **Module 2: Web Dev**
> อ้างอิงจากแผน 4 โมดูล: ดูรายละเอียดเต็มที่ [กิจกรรมปฏิบัติการและโครงงาน](/docs/labs-projects)

### ❓ คำถามทบทวน
1. primary key กับ foreign key ต่างกันอย่างไร
2. เขียน SQL ดึงนักศึกษาเกรดเฉลี่ย > 3.00 เรียงมากไปน้อย
3. vector database เหมาะกับงาน AI แบบใด

### 📚 อ้างอิง (References)
- Silberschatz, A., Korth, H. F., & Sudarshan, S. (2019). *Database System Concepts* (7th ed.). McGraw-Hill.
- Elmasri, R., & Navathe, S. *Fundamentals of Database Systems*. Pearson.
- VentureBeat. *6 data predictions for 2026: the future of vector databases.* [venturebeat.com](https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026)
- MyTechMantra. *SQL Server 2025 Native Vector Search.* [mytechmantra.com](https://www.mytechmantra.com/sql-server/sql-server-2025-native-vector-search-the-complete-guide-to-building-ai-ready-databases/)

---

## 📚 เนื้อหาเชิงลึกประจำสัปดาห์ (Deep Dive)

- [01. กลไกเบื้องหลังระบบจัดการฐานข้อมูลเชิงสัมพันธ์ (RDBMS Internals)](/module/05/01)
- [02. การขยายระบบด้วยฐานข้อมูล NoSQL (Scaling with NoSQL)](/module/05/02)
- [03. แนวคิดเบื้องหลังฐานข้อมูลเวกเตอร์ (Vector Database)](/module/05/03)
- [04. สถาปัตยกรรมข้อมูลขนาดใหญ่และ Data Pipeline (Big Data Architecture)](/module/05/04)
- [05. ความปลอดภัยของข้อมูลและความเป็นส่วนตัว (Data Privacy and Security)](/module/05/05)
