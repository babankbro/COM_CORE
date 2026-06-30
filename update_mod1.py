import os
import re
import glob

base_dir = r"d:\work\KSU\COM_CORE"

# Update กิจกรรมปฏิบัติการและโครงงาน.md
syn_file = os.path.join(base_dir, r"wiki\synthesis\กิจกรรมปฏิบัติการและโครงงาน.md")
with open(syn_file, 'r', encoding='utf-8') as f:
    syn_content = f.read()
syn_content = syn_content.replace('**Mini Project 1: "Automated Data Processor"** (ทักษะเขียนโปรแกรมจัดการข้อมูล)', 
                                  '**Mini Project 1: "Simple Text/2D Game"** (ทักษะเขียนโปรแกรมเกมเบื้องต้น)')
syn_content = syn_content.replace('วางแผนทำ Automated Data Processor', 'วางแผนทำโปรเจกต์สร้างเกม')
syn_content = syn_content.replace('สรุปและนำเสนอ Automated Data Processor', 'นำเสนอเกมที่พัฒนาขึ้น')
with open(syn_file, 'w', encoding='utf-8') as f:
    f.write(syn_content)


# Update wiki/labs/_index.md
idx_file = os.path.join(base_dir, r"wiki\labs\_index.md")
with open(idx_file, 'r', encoding='utf-8') as f:
    idx_content = f.read()
idx_content = idx_content.replace('**เป้าหมาย:** สร้างโปรแกรมจัดการข้อมูลขนาดเล็ก (Automated Data Processor)',
                                  '**เป้าหมาย:** สร้างเกมเบื้องต้น (Simple Text/2D Game)')
with open(idx_file, 'w', encoding='utf-8') as f:
    f.write(idx_content)


# Update Lab 01
lab1 = os.path.join(base_dir, r"wiki\labs\Module 1 - Foundation & Programming\Lab 01 - IDE Setup and Project Planning.md")
with open(lab1, 'r', encoding='utf-8') as f:
    l1 = f.read()
l1 = l1.replace('Automated Data Processor', 'Simple Text/2D Game')
l1 = l1.replace('การตั้งค่าเครื่องมือ IDE (Python) และวางแผน Mini-Project 1', 'การตั้งค่าเครื่องมือ IDE (Python) และวางแผนพัฒนาเกม')
with open(lab1, 'w', encoding='utf-8') as f:
    f.write(l1)

# Update Lab 02
lab2 = os.path.join(base_dir, r"wiki\labs\Module 1 - Foundation & Programming\Lab 02 - Hardware Specs and Data Extraction.md")
with open(lab2, 'r', encoding='utf-8') as f:
    l2 = f.read()
l2 = l2.replace('เขียนโปรแกรมดึงข้อมูลระบบ/ไฟล์', 'เขียนโค้ดอ่านเขียนไฟล์ (ระบบบันทึกเกม)')
l2 = l2.replace('ใช้ Python ดึงข้อมูล OS/Hardware และอ่าน/เขียนไฟล์ (I/O)', 'ใช้ Python ดึงข้อมูล OS (System Req) และทำระบบ Save/Load ผ่านการอ่านเขียนไฟล์')
with open(lab2, 'w', encoding='utf-8') as f:
    f.write(l2)

# Update Lab 03
lab3 = os.path.join(base_dir, r"wiki\labs\Module 1 - Foundation & Programming\Lab 03 - Logic Circuit and Data Processing.md")
with open(lab3, 'r', encoding='utf-8') as f:
    l3 = f.read()
l3 = l3.replace('สร้างฟังก์ชันตรรกะประมวลผลข้อมูล', 'สร้างฟังก์ชันตรรกะสำหรับกติกาเกม (Game Logic)')
l3 = l3.replace('จำลองวงจรด้วย Logisim และเขียนฟังก์ชัน Python เชิงตรรกะเบื้องต้น', 'จำลองวงจรด้วย Logisim และเขียนเงื่อนไข/ตรรกะ (If-Else/Boolean) สำหรับกลไกเกม')
with open(lab3, 'w', encoding='utf-8') as f:
    f.write(l3)

# Update Lab 04
lab4 = os.path.join(base_dir, r"wiki\labs\Module 1 - Foundation & Programming\Lab 04 - Algorithm Flowchart and Module 1 Presentation.md")
with open(lab4, 'r', encoding='utf-8') as f:
    l4 = f.read()
l4 = l4.replace('นำเสนอ Automated Data Processor', 'นำเสนอเกมที่พัฒนาขึ้น')
l4 = l4.replace('วิเคราะห์ Big-O วาด Flowchart และนำเสนอ Automated Data Processor', 'วิเคราะห์ Big-O, วาด Flowchart ของ Game Loop และนำเสนอเกมเบื้องต้น')
with open(lab4, 'w', encoding='utf-8') as f:
    f.write(l4)

print("Update complete")
