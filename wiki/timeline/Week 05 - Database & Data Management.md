---
type: chapter
status: complete
week: 5
clo: [CLO3]
tags: [curriculum, week05, database, sql, nosql, vector-database]
created: "2026-06-30"
updated: "2026-06-30"
---

# สัปดาห์ที่ 5: ฐานข้อมูลและการจัดการข้อมูลขนาดใหญ่

> [!abstract] สาระสำคัญ
> ฐานข้อมูลคือระบบจัดเก็บ/จัดการข้อมูลอย่างมีโครงสร้าง โมเดลหลักคือ **เชิงสัมพันธ์ (relational)** ที่ใช้ตารางและ SQL ปัจจุบันมี [[Vector Database]] เป็นหมวดใหม่สำหรับงาน AI

## 🎯 วัตถุประสงค์การสอน (Learning Objectives)
1. ผู้เรียนเข้าใจหลักการของฐานข้อมูลเชิงสัมพันธ์ (Relational) และไม่เชิงสัมพันธ์ (NoSQL) — *CLO3*
2. ผู้เรียนรู้จักแนวคิด Big Data และการจัดการข้อมูลขนาดใหญ่ — *CLO3*
3. ผู้เรียนเข้าใจความสำคัญและสถาปัตยกรรมของ [[Vector Database]] ในยุค AI — *CLO3*

## 📝 สรุปเนื้อหาหัวข้อ (Topics Covered)
- ฐานข้อมูลเชิงสัมพันธ์และภาษา SQL
- NoSQL และ Big Data Analytics
- [[Vector Database]] (เช่น Pinecone, Milvus) สำหรับ [[RAG และ LLM|LLM/RAG]]

## 📖 เนื้อหาโดยละเอียด
- **DBMS:** ตัวกลางระหว่างผู้ใช้/แอปกับข้อมูล (MySQL, PostgreSQL, SQLite, Oracle)
- **โมเดลเชิงสัมพันธ์:** ตาราง/แถว/คอลัมน์, primary/foreign key, ER diagram, normalization
- **SQL:** `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `JOIN`, `WHERE`, `GROUP BY`
- **ACID:** Atomicity, Consistency, Isolation, Durability
- **SQL vs NoSQL:** โครงสร้างชัด vs ยืดหยุ่น/ขยายแนวนอน (document, key-value, graph)

## 🔑 แนวคิดหลัก (Key Concepts)
[[Vector Database]] · [[RAG และ LLM]]

## 📈 แนวโน้มปัจจุบัน (2025–2026)
- **ฐานข้อมูลเวกเตอร์** รองรับ RAG/semantic search/ความจำของ AI agents — ตลาด ~3.2 พันล้านดอลลาร์ในปี 2025 โต ~24%/ปี
- **เวกเตอร์กลายเป็น "ชนิดข้อมูล":** ฐานข้อมูลหลักผนวกเข้าไป เช่น **SQL Server 2025** เพิ่มชนิด `VECTOR` + DiskANN; กำลังร่างส่วนขยาย ANSI SQL
- **Hybrid search:** ผสม vector + keyword + metadata + graph เป็นมาตรฐานใหม่

## 🧪 กิจกรรม/ปฏิบัติการ (OBE) — Lab 5
Lab 1 ชม. (ออกแบบ ER และ SQL) + Project 1 ชม. (ต่อฐานข้อมูล SQLite กับ Python/Node.js) — **Module 2: Web Dev**
> อ้างอิงจากแผน 4 โมดูล: ดูรายละเอียดเต็มที่ [[กิจกรรมปฏิบัติการและโครงงาน]]

## ❓ คำถามทบทวน
1. primary key กับ foreign key ต่างกันอย่างไร
2. เขียน SQL ดึงนักศึกษาเกรดเฉลี่ย > 3.00 เรียงมากไปน้อย
3. vector database เหมาะกับงาน AI แบบใด

## 📚 อ้างอิง (References)
- Silberschatz, A., Korth, H. F., & Sudarshan, S. (2019). *Database System Concepts* (7th ed.). McGraw-Hill.
- Elmasri, R., & Navathe, S. *Fundamentals of Database Systems*. Pearson.
- VentureBeat. *6 data predictions for 2026: the future of vector databases.* [venturebeat.com](https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026)
- MyTechMantra. *SQL Server 2025 Native Vector Search.* [mytechmantra.com](https://www.mytechmantra.com/sql-server/sql-server-2025-native-vector-search-the-complete-guide-to-building-ai-ready-databases/)

## 🔗 นำทาง
⬅️ [[Week 04 - Algorithms & Programming Paradigms]] · ➡️ [[Week 06 - Computer Networks & Internet]]
