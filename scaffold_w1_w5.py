import os
import shutil

base_dir = r"d:\work\KSU\COM_CORE\wiki\learning"

weeks = {
    "Week 01": {
        "old_file": "Learning Content Week 01 - ภาพรวมวิศวกรรมคอมพิวเตอร์และระบบสารสนเทศในยุค AI.md",
        "new_name": "00_Overview - ภาพรวมวิศวกรรมคอมพิวเตอร์.md",
        "pages": [
            ("01_วิวัฒนาการและประวัติศาสตร์ของวิศวกรรมคอมพิวเตอร์.md", "วิวัฒนาการและประวัติศาสตร์ของวิศวกรรมคอมพิวเตอร์ (Evolution of CE)", 
             "ครอบคลุมประวัติศาสตร์ตั้งแต่ยุคหลอดสุญญากาศ จนถึงทรานซิสเตอร์ การประดิษฐ์ IC (Integrated Circuit) และยุคของชิปที่มีหน่วยประมวลผล AI\n\n**แหล่งอ้างอิง:**\n- Patterson, D. A., & Hennessy, J. L. (2020). *Computer Organization and Design*\n- IEEE Computer Society History Center"),
            ("02_เจาะลึกความแตกต่างระหว่างศาสตร์คอมพิวเตอร์.md", "ความแตกต่างระหว่าง CE, CS, SE, IT, IS", 
             "เจาะลึกมาตรฐาน ACM/IEEE Computing Curricula:\n- **CE (Computer Engineering):** วงจร, ฮาร์ดแวร์, ไมโครคอนโทรลเลอร์\n- **CS (Computer Science):** อัลกอริทึม, AI, ทฤษฎีคอมพิวเตอร์\n- **SE (Software Engineering):** การออกแบบระบบสเกลใหญ่, SDLC\n- **IT/IS:** โครงสร้างพื้นฐาน, ธุรกิจ\n\n**อ้างอิง:**\n- ACM/IEEE CC2020 Computing Curricula"),
            ("03_ทักษะหลักที่จำเป็นในยุค_AI-driven_Architecture.md", "ทักษะหลักที่จำเป็นในยุค AI-driven Architecture", 
             "การปรับตัวจากวิศวกรแบบดั้งเดิมไปสู่วิศวกรยุค AI (AI-Enhanced Engineer) เช่น การทำ Prompt Engineering สำหรับโค้ด, การเข้าใจสถาปัตยกรรมของ LLM เบื้องต้น, การตรวจจับอคติ (Bias) ในโมเดล\n\n**อ้างอิง:**\n- Gartner: Top Strategic Technology Trends for 2025"),
            ("04_มาตรฐานหลักสูตร_ACM_IEEE.md", "ภาพรวมกรอบองค์ความรู้มาตรฐาน ACM/IEEE", 
             "การศึกษา Body of Knowledge เช่น CAO (Computer Architecture), SWE (Software Engineering), SEC (Security) ซึ่งถูกบรรจุอยู่ในหลักสูตรมาตรฐานสากล CE2016 และ CS2023\n\n**อ้างอิง:**\n- ACM/IEEE-CS CE2016 Final Report"),
            ("05_การประยุกต์ใช้ปัญญาประดิษฐ์ในฐานะวิศวกร.md", "การประยุกต์ใช้ Agentic AI ในการทำงาน", 
             "การใช้ AI แบบมีเอเจนต์ (Agentic AI) มาช่วยทดสอบระบบอัตโนมัติ (Automated Testing), การรีวิวโค้ด, และการทำ CI/CD แบบชาญฉลาด\n\n**อ้างอิง:**\n- AI Engineering: A Guide to the New Paradigm (2025)")
        ]
    },
    "Week 02": {
        "old_file": "Learning Content Week 02 - ฮาร์ดแวร์ ซอฟต์แวร์ และระบบนิเวศสมัยใหม่.md",
        "new_name": "00_Overview - ฮาร์ดแวร์ ซอฟต์แวร์ และระบบนิเวศสมัยใหม่.md",
        "pages": [
            ("01_สถาปัตยกรรมระดับฮาร์ดแวร์เชิงลึก.md", "สถาปัตยกรรมฮาร์ดแวร์สมัยใหม่ (Deep Dive)", 
             "การเจาะลึก Pipeline, Cache Hierarchy, และ Memory Management Unit (MMU) ของระบบซีพียูยุคใหม่\n\n**อ้างอิง:**\n- *Operating System Concepts* (10th ed.), Silberschatz et al."),
            ("02_ระบบปฏิบัติการสมัยใหม่และคอนเทนเนอร์.md", "ระบบปฏิบัติการและ Containers", 
             "ทำไม Docker และ Container ถึงมาแทนที่ Virtual Machine (VM) ในยุคคลาวด์? สถาปัตยกรรม cgroups, namespaces ใน Linux Kernel\n\n**อ้างอิง:**\n- Docker Documentation (2025)"),
            ("03_สถาปัตยกรรม_Edge_Computing.md", "สถาปัตยกรรม Edge Computing", 
             "การนำการประมวลผลมาไว้ใกล้ข้อมูล (Data Source) เพื่อลด Latency โดยเฉพาะในยุค IoT และ 5G/6G\n\n**อ้างอิง:**\n- Edge AI and Vision Alliance Report 2026"),
            ("04_Green_Computing.md", "การปฏิบัติเพื่อ Green Computing", 
             "วิกฤตพลังงานจาก Data Center และ AI Training การวัดค่า PUE (Power Usage Effectiveness) และสถาปัตยกรรมระบายความร้อนแบบ Liquid Cooling\n\n**อ้างอิง:**\n- The Green Grid: PUE Comprehensive Examination"),
            ("05_Heterogeneous_Computing.md", "Heterogeneous Computing (CPU + GPU + NPU)", 
             "การออกแบบ SoC (System on Chip) ยุคใหม่ที่ประกอบด้วยหน่วยประมวลผลเฉพาะทางร่วมกัน เพื่อประหยัดพลังงานสูงสุด\n\n**อ้างอิง:**\n- Apple Silicon & ARM Architecture References")
        ]
    },
    "Week 03": {
        "old_file": "Learning Content Week 03 - วงจรตรรกะและหน่วยประมวลผล.md",
        "new_name": "00_Overview - วงจรตรรกะและหน่วยประมวลผล.md",
        "pages": [
            ("01_พื้นฐานวงจรตรรกะสู่การออกแบบชิป.md", "จาก Logic Gates สู่ Chip Design", 
             "ตารางความจริง (Truth Tables), K-Maps และการสร้าง ALU (Arithmetic Logic Unit) จากทรานซิสเตอร์\n\n**อ้างอิง:**\n- *Digital Design*, Mano & Ciletti"),
            ("02_สถาปัตยกรรม_von_Neumann_และ_Harvard.md", "สถาปัตยกรรม von Neumann vs Harvard", 
             "ความแตกต่างระหว่างการแชร์บัสข้อมูลและคำสั่ง (von Neumann) กับการแยกบัส (Harvard) ข้อดีและข้อเสียในไมโครคอนโทรลเลอร์\n\n**อ้างอิง:**\n- *Computer Organization and Design*"),
            ("03_เจาะลึกสถาปัตยกรรม_RISC-V.md", "เจาะลึกสถาปัตยกรรม RISC-V", 
             "ทำไม Instruction Set Architecture (ISA) แบบเปิด (Open-source) ถึงพลิกโฉมวงการเซมิคอนดักเตอร์ การลดการผูกขาดของ x86 และ ARM\n\n**อ้างอิง:**\n- RISC-V International (riscv.org)"),
            ("04_AI_Accelerators.md", "หน่วยเร่งประมวลผล AI (NPU และ TPU)", 
             "ความสำคัญของ Matrix Multiplication ในระบบประสาทเทียม (Neural Networks) และฮาร์ดแวร์ที่ออกแบบมาเฉพาะ (Tensor Processing Units)\n\n**อ้างอิง:**\n- Google Cloud TPU Documentation"),
            ("05_Chiplet_และยุคหลังกฎของมัวร์.md", "เทคโนโลยี Chiplet และยุค Post-Moore's Law", 
             "การทลายข้อจำกัดการย่อขนาดทรานซิสเตอร์ด้วยการนำชิปเล็กๆ หลายอันมาประกอบกันด้วย Advanced Packaging\n\n**อ้างอิง:**\n- IEEE Solid-State Circuits Society")
        ]
    },
    "Week 04": {
        "old_file": "Learning Content Week 04 - อัลกอริทึมและการเขียนโปรแกรม.md",
        "new_name": "00_Overview - อัลกอริทึมและการเขียนโปรแกรม.md",
        "pages": [
            ("01_การคิดเชิงคำนวณแบบเจาะลึก.md", "Computational Thinking เชิงลึก", 
             "การแบ่งปัญหา (Decomposition), การหารูปแบบ (Pattern Recognition), การสร้างนามธรรม (Abstraction) และอัลกอริทึม\n\n**อ้างอิง:**\n- ACM CC2020 SDF"),
            ("02_การวิเคราะห์ความซับซ้อน_Big_O.md", "วิเคราะห์ความซับซ้อน (Big-O Notation)", 
             "O(1), O(log n), O(n), O(n log n), O(n^2) กับการประยุกต์ใช้เลือก Data Structure\n\n**อ้างอิง:**\n- *Introduction to Algorithms (CLRS)*"),
            ("03_OOP_vs_Functional.md", "OOP vs Functional Programming", 
             "ความแตกต่างระหว่างการมองทุกอย่างเป็นวัตถุ (Object) กับการมองเป็นการแปลงสถานะ (Pure Functions) ข้อดีข้อเสีย\n\n**อ้างอิง:**\n- Clean Code, Robert C. Martin"),
            ("04_AI_Coding_Assistants.md", "ทำงานคู่กับ AI Coding Assistants", 
             "หลักการ Pair-programming กับ GitHub Copilot และ Cursor ข้อควรระวังเรื่อง Code Hallucination\n\n**อ้างอิง:**\n- OWASP Top 10 for LLM Applications"),
            ("05_Version_Control_และ_Concurrency.md", "Version Control และ Concurrency", 
             "การจัดการปัญหา Race Condition เบื้องต้น และการทำงานร่วมกันผ่าน Git Flow\n\n**อ้างอิง:**\n- Pro Git Book")
        ]
    },
    "Week 05": {
        "old_file": "Learning Content Week 05 - ฐานข้อมูลและการจัดการข้อมูลขนาดใหญ่.md",
        "new_name": "00_Overview - ฐานข้อมูล.md",
        "pages": [
            ("01_กลไกเบื้องหลัง_RDBMS.md", "โครงสร้างการทำงานของ RDBMS", 
             "B-Tree Indexes, ACID Properties, และ Write-Ahead Logging (WAL) ใน PostgreSQL\n\n**อ้างอิง:**\n- *Database System Concepts*, Silberschatz"),
            ("02_การขยายระบบด้วย_NoSQL.md", "Scaling Data ด้วย NoSQL", 
             "CAP Theorem และ Eventual Consistency ในระบบ Document (MongoDB) และ Wide-Column (Cassandra)\n\n**อ้างอิง:**\n- *Designing Data-Intensive Applications*, Martin Kleppmann"),
            ("03_แนวคิดของ_Vector_Database.md", "แนวคิดเบื้องหลัง Vector Database", 
             "การสร้าง Embeddings, การคำนวณ Cosine Similarity, และเทคนิค Approximate Nearest Neighbor (ANN) สำหรับงาน LLM\n\n**อ้างอิง:**\n- Pinecone Architecture Docs"),
            ("04_สถาปัตยกรรม_Big_Data.md", "สถาปัตยกรรม Big Data และ Data Pipeline", 
             "Data Lake vs Data Warehouse, กระบวนการ ETL และ Apache Kafka สำหรับ Data Streaming\n\n**อ้างอิง:**\n- Apache Kafka Documentation"),
            ("05_Data_Privacy_and_Security.md", "ความท้าทายด้านความปลอดภัยและ Data Privacy", 
             "การทำ Data Masking, กฎหมาย PDPA/GDPR ในการจัดการข้อมูลอ่อนไหว และการเข้ารหัสข้อมูล (Encryption at Rest)\n\n**อ้างอิง:**\n- MDES: PDPA (2019)")
        ]
    }
}

template = """---
type: deep-dive
status: complete
tags: [{tags}]
created: "2026-08-03"
updated: "2026-08-03"
---

# {title}

> **หมวดหมู่:** เนื้อหาเชิงลึกประกอบการเรียนรู้ (Deep Dive Learning Content)

## 📖 เนื้อหาและคำอธิบาย
{content}

---
*เนื้อหานี้เป็นส่วนขยายของวิชาแก่นวิศวกรรมคอมพิวเตอร์ เพื่อให้ผู้เรียนค้นคว้าเพิ่มเติมได้*
"""

# Create directory structure and files
for week, data in weeks.items():
    week_dir = os.path.join(base_dir, week)
    os.makedirs(week_dir, exist_ok=True)
    
    old_path = os.path.join(base_dir, data["old_file"])
    new_path = os.path.join(week_dir, data["new_name"])
    
    # Move the old main file if it exists in base_dir
    if os.path.exists(old_path):
        shutil.move(old_path, new_path)
    
    # Generate the 5 new pages
    for filename, title, content in data["pages"]:
        filepath = os.path.join(week_dir, filename)
        tags = f"learning, {week.lower().replace(' ', '')}"
        file_content = template.format(tags=tags, title=title, content=content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(file_content)

print("Scaffolded Phase 1 (Week 1-5) successfully.")
