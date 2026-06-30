import os
import re
import glob

lab_plan = {
    1: "Lab 1 ชม. (ตั้งค่า IDE, Git) + Project 1 ชม. (วางแผนโปรเจกต์ Python) — **Module 1: Foundation & Programming**",
    2: "Lab 1 ชม. (ตรวจสอบสเปกฮาร์ดแวร์) + Project 1 ชม. (เขียนโปรแกรมดึงข้อมูลระบบ/ไฟล์) — **Module 1: Foundation & Programming**",
    3: "Lab 1 ชม. (จำลองวงจร Logisim) + Project 1 ชม. (สร้างฟังก์ชันตรรกะประมวลผลข้อมูล) — **Module 1: Foundation & Programming**",
    4: "Lab 1 ชม. (วิเคราะห์ Big-O/Flowchart) + Project 1 ชม. (สรุปและนำเสนอ Mini Project 1) — **Module 1: Foundation & Programming**",
    5: "Lab 1 ชม. (ออกแบบ ER และ SQL) + Project 1 ชม. (ต่อฐานข้อมูล SQLite กับ Python/Node.js) — **Module 2: Web Dev**",
    6: "Lab 1 ชม. (Network simulation/Ping) + Project 1 ชม. (สร้าง API และ Web Router) — **Module 2: Web Dev**",
    7: "Lab 1 ชม. (ทดลองใช้ Cloud/Docker เบื้องต้น) + Project 1 ชม. (Deploy เว็บแอปพลิเคชันขึ้นเซิร์ฟเวอร์) — **Module 2: Web Dev**",
    8: "สอบกลางภาค (ครอบคลุมทฤษฎีและเนื้อหา Module 1-2)",
    9: "Lab 1 ชม. (ทดลองรัน ML Model ง่ายๆ) + Project 1 ชม. (วางแผนสถาปัตยกรรม IoT) — **Module 3: IoT & Smart Systems**",
    10: "Lab 1 ชม. (เรียกใช้งาน GenAI API) + Project 1 ชม. (ต่อวงจรบอร์ด ESP32/Arduino และเซนเซอร์) — **Module 3: IoT & Smart Systems**",
    11: "Lab 1 ชม. (การส่งข้อมูลผ่าน MQTT) + Project 1 ชม. (เขียนโค้ดรับส่งข้อมูลเซนเซอร์ขึ้น Dashboard) — **Module 3: IoT & Smart Systems**",
    12: "Lab 1 ชม. (เทคนิคเข้ารหัสผ่าน/ความปลอดภัย) + Project 1 ชม. (ประยุกต์ใช้ความปลอดภัยในระบบ IoT + นำเสนอ) — **Module 3: IoT & Smart Systems**",
    13: "Lab 1 ชม. (อภิปราย Bias และจริยธรรม AI) + Project 1 ชม. (ดึงสตรีมภาพจากกล้องและทำ Object Detection เบื้องต้น) — **Module 4: Computer Vision**",
    14: "Lab 1 ชม. (สร้าง CI/CD Pipeline ขั้นต้น) + Project 1 ชม. (เชื่อมระบบ CV เข้ากับ Web/IoT Dashboard เดิม) — **Module 4: Computer Vision**",
    15: "Lab 1 ชม. (Virtual Tour/ดูงานศูนย์ข้อมูล) + Project 1 ชม. (เตรียมสไลด์รวมผลงาน 4 โมดูล) — **Module 4: Computer Vision**",
    16: "นำเสนอโครงงานประยุกต์รวม (Final Capstone Presentation) ครอบคลุมทั้ง 4 โมดูล",
    17: "สอบปลายภาค (Final Examination)"
}

timeline_dir = r"d:\work\KSU\COM_CORE\wiki\timeline"
files = glob.glob(os.path.join(timeline_dir, "Week *.md"))

for filepath in files:
    filename = os.path.basename(filepath)
    match = re.search(r'Week (\d+)', filename)
    if not match:
        continue
    week_num = int(match.group(1))
    
    if week_num not in lab_plan:
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # More flexible regex to catch headers like "## 🧪 กิจกรรม/ปฏิบัติการ (OBE) — Lab 1"
    pattern = re.compile(r'(## 🧪 กิจกรรม/ปฏิบัติการ \(OBE\)[^\n]*\n)(.*?)(?=\n## )', re.DOTALL)
    new_text = f"\\1{lab_plan[week_num]}\n> อ้างอิงจากแผน 4 โมดูล: ดูรายละเอียดเต็มที่ [[กิจกรรมปฏิบัติการและโครงงาน]]\n"
    new_content = pattern.sub(new_text, content)
    
    if new_content == content:
        pattern_end = re.compile(r'(## 🧪 กิจกรรม/ปฏิบัติการ \(OBE\)[^\n]*\n)(.*)', re.DOTALL)
        new_content = pattern_end.sub(new_text, content)
        
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"Skipped {filename} - section not found")
