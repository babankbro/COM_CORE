---
type: learning
status: complete
week: 5
source_week: "Week 05 - Database & Data Management"
tags: [learning, week05, en-001-019]
created: "2026-08-03"
updated: "2026-10-12"
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

## 🧭 อธิบายเพิ่มเติม (ฉบับขยาย)

ส่วนนี้ขยายแก่นความรู้ด้านบนด้วยตัวอย่างใกล้ตัว ตัวอย่างที่รันได้จริง และตารางเปรียบเทียบ ถ้าต้องการรายละเอียดเชิงลึก ให้อ่านต่อที่ [หัวข้อ 1 กลไกเบื้องหลัง RDBMS](/module/05/01) · [หัวข้อ 2 NoSQL](/module/05/02) · [หัวข้อ 3 Vector Database](/module/05/03) · [หัวข้อ 4 Big Data](/module/05/04) · [หัวข้อ 5 Data Privacy and Security](/module/05/05)

### 1. ทำไมไม่เก็บทุกอย่างใน Excel: ฐานข้อมูลเหมือนห้องสมุดที่มีบรรณารักษ์

ไฟล์ Excel เหมือนกองหนังสือบนโต๊ะ คนเดียวใช้ได้สะดวก แต่เมื่อมีหลายคนแก้พร้อมกัน ข้อมูลเป็นแสนแถว หรือต้องเชื่อมหลายตารางเข้าด้วยกัน จะเริ่มมีปัญหา ส่วน DBMS เหมือนห้องสมุดที่มีบรรณารักษ์ (ตัวโปรแกรมฐานข้อมูล) คอยตรวจกฎก่อนรับของเข้า จัดสารบัญ (index) ให้ค้นเร็ว และจัดคิวให้หลายคนใช้ได้พร้อมกันโดยข้อมูลไม่เสีย

| ประเด็น | Spreadsheet (Excel/Sheets) | ฐานข้อมูล (DBMS) |
|---|---|---|
| ผู้ใช้พร้อมกัน | แก้ทับกันได้ง่าย | จัดการด้วย transaction และ lock |
| ความถูกต้อง | พิมพ์อะไรก็ได้ลงช่อง | บังคับด้วยชนิดข้อมูล PK, FK, CHECK |
| ความสัมพันธ์ | VLOOKUP ข้ามชีต เปราะง่าย | FK + JOIN เป็นกลไกหลัก |
| ปริมาณข้อมูล | ช้าลงชัดเจนเมื่อมีหลายแสนแถว | index ช่วยค้นเร็วแม้มีหลายล้านแถว |
| การเชื่อมกับแอป | export/import ด้วยมือ | แอปและเว็บส่ง SQL ได้โดยตรง |

### 2. ตัวอย่างทีละขั้น: จาก ER Diagram สู่ตารางและ JOIN

![ER Diagram ของระบบลงทะเบียน มี entity Student และ Course ที่มีความสัมพันธ์แบบ M:N ซึ่งแตกเป็นความสัมพันธ์ 1:N สองเส้นผ่านตารางเชื่อม Enrollment ที่มี student_id และ course_id เป็นทั้ง PK ผสมและ FK พร้อมคอลัมน์ grade](/images/weeks/w05-er-diagram.svg)

**ขั้นที่ 1 หา entity และความสัมพันธ์:** นักศึกษาหนึ่งคนลงได้หลายวิชา และวิชาหนึ่งมีนักศึกษาหลายคน จึงเป็น M:N ซึ่งเก็บตรง ๆ ในตารางเดียวไม่ได้ ต้องสร้างตารางเชื่อม `Enrollment` ไว้ตรงกลาง

**ขั้นที่ 2 สร้างตารางพร้อม key** (ทดสอบด้วย SQLite แล้ว)

```sql
PRAGMA foreign_keys = ON;   -- SQLite ต้องเปิดการตรวจ FK เองทุกครั้งที่เชื่อมต่อ
CREATE TABLE Student (student_id TEXT PRIMARY KEY, first_name TEXT NOT NULL, faculty TEXT);
CREATE TABLE Course  (course_id TEXT PRIMARY KEY, title TEXT NOT NULL,
                      credits INTEGER CHECK (credits > 0));
CREATE TABLE Enrollment (
    student_id TEXT REFERENCES Student(student_id),
    course_id  TEXT REFERENCES Course(course_id),
    grade      TEXT,
    PRIMARY KEY (student_id, course_id)          -- PK ผสม: คู่เดิมซ้ำไม่ได้
);
```

**ขั้นที่ 3 ถามข้อมูลข้ามตารางด้วย JOIN** เมื่อใส่นักศึกษา 3 คน วิชา 2 วิชา และการลงทะเบียน 4 แถว แล้วถามว่า "ใครเรียนวิชา EN001019 ได้เกรดอะไร"

```sql
SELECT s.first_name, c.title, e.grade
FROM Enrollment AS e
JOIN Student AS s ON s.student_id = e.student_id
JOIN Course  AS c ON c.course_id  = e.course_id
WHERE c.course_id = 'EN001019'
ORDER BY s.first_name;
```

| first_name | title | grade |
|---|---|---|
| สมชาย | แก่นวิศวกรรมคอมพิวเตอร์ | A |
| สมหญิง | แก่นวิศวกรรมคอมพิวเตอร์ | B |

**ขั้นที่ 4 ทดสอบว่า key ทำงานจริง:** ใส่การลงทะเบียนของรหัส `65019999` ที่ไม่มีในตาราง Student จะได้ `IntegrityError: FOREIGN KEY constraint failed` และใส่คู่ `('65010001', 'MA101')` ซ้ำจะได้ `UNIQUE constraint failed` แปลว่าฐานข้อมูลช่วยกันข้อมูลผิดตั้งแต่ทางเข้า ไม่ต้องรอให้แอปตรวจเอง

### 3. SQL เขียนเรียงแบบหนึ่ง แต่ประมวลผลอีกลำดับหนึ่ง

![แผนภาพลำดับการประมวลผล SQL เชิงตรรกะ 7 ขั้น FROM ได้ 15 แถว WHERE gpa มากกว่าหรือเท่ากับ 3.0 เหลือ 10 แถว GROUP BY faculty ได้ 3 กลุ่ม HAVING COUNT มากกว่าหรือเท่ากับ 3 เหลือ 3 กลุ่ม SELECT คำนวณคอลัมน์ ORDER BY เรียงค่าเฉลี่ยมากไปน้อย และ LIMIT 2 ได้ผลลัพธ์ 2 แถวคือวิทยาศาสตร์ 3.68 และวิศวกรรมศาสตร์ 3.49](/images/weeks/w05-sql-pipeline.svg)

เปรียบเหมือนการคัดนักกีฬา เริ่มจากรายชื่อทั้งหมด (FROM) คัดเฉพาะคนที่ผ่านเกณฑ์ (WHERE) แบ่งทีมตามคณะ (GROUP BY) ตัดทีมที่คนไม่พอ (HAVING) สรุปสถิติของแต่ละทีม (SELECT) จัดอันดับ (ORDER BY) แล้วประกาศแค่ 2 ทีมแรก (LIMIT) ตัวเลขในภาพได้จากการรัน SQL นี้กับข้อมูลนักศึกษา 15 คนของ Lab 05

```sql
SELECT faculty, COUNT(*) AS n, ROUND(AVG(gpa), 2) AS avg_gpa
FROM students
WHERE gpa >= 3.0
GROUP BY faculty
HAVING COUNT(*) >= 3
ORDER BY avg_gpa DESC
LIMIT 2;
```

การรู้ลำดับนี้อธิบายข้อผิดพลาดที่พบบ่อยได้ทันที เช่น เขียน `WHERE AVG(gpa) > 3` ไม่ได้ เพราะตอน WHERE ทำงานยังไม่มีการจัดกลุ่ม ต้องย้ายไปใช้ `HAVING` และใน SQL มาตรฐาน alias `avg_gpa` ที่ตั้งใน SELECT นำไปใช้ใน WHERE ไม่ได้ แต่ใช้ใน ORDER BY ได้ เพราะ ORDER BY ทำงานหลัง SELECT

### 4. Normalization: เขียนข้อมูลแต่ละเรื่องไว้ที่เดียว

ลองนึกถึงสมุดลงชื่อเรียนที่ทุกบรรทัดเขียนชื่อวิชาเต็ม ๆ ซ้ำ ถ้าวันหนึ่งเปลี่ยนชื่อวิชา ต้องตามแก้ทุกบรรทัด และถ้าพลาดไปหนึ่งบรรทัด ข้อมูลจะขัดแย้งกันเอง normalization คือการย้ายข้อมูลแต่ละเรื่องไปไว้ในตารางของตัวเอง แล้วโยงกันด้วย key

| ก่อน (ตารางเดียว) | ปัญหา | หลังแยกตาราง |
|---|---|---|
| `(student_id, first_name, course_id, title, grade)` | ชื่อวิชาซ้ำทุกแถว แก้ไม่ครบได้ (update anomaly) | `Course(course_id, title)` เก็บชื่อวิชาครั้งเดียว |
| ช่อง `courses = "MA101, EN001019"` | ค่าหลายค่าในช่องเดียว ผิด 1NF | 1 แถวใน `Enrollment` ต่อ 1 วิชา |
| เพิ่มวิชาใหม่ที่ยังไม่มีคนลง | ใส่ไม่ได้เพราะไม่มีนักศึกษา (insert anomaly) | เพิ่มใน `Course` ได้ทันที |

### 5. ACID: เทียบกับการโอนเงินผ่านแอปธนาคาร

| คุณสมบัติ | คำถามที่ตอบ | ตัวอย่างโอน 500 บาทจาก A ไป B |
|---|---|---|
| Atomicity | ทำครบทั้งหมดหรือไม่ทำเลย | หัก A แล้วไฟดับก่อนเพิ่ม B → ยกเลิกทั้งรายการ (rollback) |
| Consistency | ข้อมูลยังถูกตามกฎหรือไม่ | ยอดเงินห้ามติดลบ ผลรวมเงินในระบบต้องเท่าเดิม |
| Isolation | ธุรกรรมพร้อมกันรบกวนกันไหม | สองคนโอนออกจากบัญชี A พร้อมกัน ต้องได้ผลเหมือนทำทีละรายการ |
| Durability | ยืนยันแล้วจะหายไหม | แอปแจ้ง "โอนสำเร็จ" แล้วเครื่องล่ม ข้อมูลยังอยู่ |

ใน Python กับ SQLite คำสั่ง `INSERT/UPDATE/DELETE` จะยังไม่ถาวรจนกว่าจะเรียก `conn.commit()` ซึ่งเป็นรูปธรรมของ atomicity และ durability ที่ผู้เรียนจะทดลองใน Lab 05

### 6. เลือกฐานข้อมูลให้เหมาะกับงาน และ keyword vs vector search

![ตารางเปรียบเทียบฐานข้อมูล 3 กลุ่ม Relational SQL เก็บตารางที่มี schema ตายตัวและเด่นเรื่อง ACID NoSQL แบบ Document เก็บเอกสาร JSON ยืดหยุ่นและขยายแนวนอนได้ดี Vector Database เก็บ embedding เพื่อค้นหาความหมายใกล้เคียงสำหรับ RAG](/images/weeks/w05-db-families.svg)

ความต่างที่สำคัญที่สุดของ vector search คือ "ค้นหาด้วยความหมาย" แทน "ค้นหาด้วยคำตรงตัว" สมมติผู้ใช้ถามว่า "รีเซ็ตรหัสผ่านอย่างไร" keyword search จะหาเอกสารที่มีคำว่า "รีเซ็ต" หรือ "รหัสผ่าน" เท่านั้น จึงอาจพลาดเอกสารชื่อ "ลืม password เข้าระบบไม่ได้" ส่วน vector search แปลงทั้งคำถามและเอกสารเป็นเวกเตอร์ แล้ววัดความใกล้ด้วย cosine similarity

| เอกสาร | มีคำตรงกับคำถาม? | cosine similarity (เวกเตอร์ 3 มิติสมมติ) |
|---|---|---|
| ลืม password เข้าระบบไม่ได้ | ไม่มี | 0.996 |
| วิธีรีเซ็ตรหัสผ่าน | มี | 0.984 |
| ตารางสอบปลายภาค | ไม่มี | 0.271 |

ตัวเลขในตารางคำนวณจากเวกเตอร์สมมติ คำถาม = [0.9, 0.1, 0.3] และเอกสาร = [0.85, 0.15, 0.35], [0.8, 0.2, 0.4], [0.1, 0.9, 0.2] ด้วยสูตร cos θ = (a·b) / (‖a‖‖b‖) ส่วน embedding จริงมีหลายร้อยถึงหลายพันมิติและได้จาก embedding model ในระบบจริงจึงนิยมใช้ **hybrid search** ที่รวม keyword, vector และเงื่อนไข metadata (เช่น `WHERE faculty = ...`) เข้าด้วยกัน

### สรุปสั้น

- DBMS เหมือนห้องสมุดที่มีบรรณารักษ์ ตรวจกฎ จัด index และให้หลายคนใช้พร้อมกันได้ ซึ่ง spreadsheet ทำได้ไม่ดี
- ความสัมพันธ์ M:N ต้องแตกเป็น 1:N สองเส้นผ่านตารางเชื่อม เช่น `Enrollment` ที่มี PK ผสมและ FK สองตัว
- SQLite ต้อง `PRAGMA foreign_keys = ON` ก่อน FK จึงจะถูกตรวจ
- ลำดับประมวลผลเชิงตรรกะ: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT จึงใช้ aggregate ใน WHERE ไม่ได้
- Normalization ให้ข้อมูลแต่ละเรื่องอยู่ที่เดียว ลด update/insert/delete anomaly
- ACID ทำให้ธุรกรรมเชื่อถือได้ และใน Python ต้อง `commit()` ข้อมูลจึงถาวร
- เลือกฐานข้อมูลตามรูปข้อมูลและคำถาม: SQL สำหรับข้อมูลมีโครงสร้าง, Document สำหรับข้อมูลยืดหยุ่น, Vector สำหรับค้นหาความหมาย

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
