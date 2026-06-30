import os
import re

base_dir = r"d:\work\KSU\COM_CORE\wiki\timeline"

updates = {
    "Week 01 - Introduction to CE & IT.md": ("(วางแผนโปรเจกต์ Python)", "(ออกแบบโครงสร้างและกติกาเกมด้วย Python)"),
    "Week 02 - Hardware & Software Ecosystems.md": ("(เขียนโปรแกรมดึงข้อมูลระบบ/ไฟล์)", "(ทำระบบ Save/Load และเขียนโค้ดอ่านเขียนไฟล์)"),
    "Week 03 - Digital Logic & Modern Processors.md": ("(สร้างฟังก์ชันตรรกะประมวลผลข้อมูล)", "(เขียนเงื่อนไข/ตรรกะ (Game Logic) ของตัวเกม)"),
    "Week 04 - Algorithms & Programming Paradigms.md": ("(สรุปและนำเสนอ Mini Project 1)", "(สรุป นำเสนอ และสาธิตการเล่นเกม)")
}

for filename, (old_text, new_text) in updates.items():
    filepath = os.path.join(base_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = content.replace(old_text, new_text)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
