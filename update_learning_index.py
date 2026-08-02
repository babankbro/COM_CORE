import os
import re

index_path = r"d:\work\KSU\COM_CORE\wiki\learning\_index.md"
with open(index_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if "Learning Content Week 01 - ภาพรวมวิศวกรรมคอมพิวเตอร์และระบบสารสนเทศในยุค AI" in line:
        new_lines.append("- 📁 **Week 01:** [[Week 01/00_Overview - ภาพรวมวิศวกรรมคอมพิวเตอร์]]\n")
        new_lines.append("  - 📄 [[Week 01/01_วิวัฒนาการและประวัติศาสตร์ของวิศวกรรมคอมพิวเตอร์]]\n")
        new_lines.append("  - 📄 [[Week 01/02_เจาะลึกความแตกต่างระหว่างศาสตร์คอมพิวเตอร์]]\n")
        new_lines.append("  - 📄 [[Week 01/03_ทักษะหลักที่จำเป็นในยุค_AI-driven_Architecture]]\n")
        new_lines.append("  - 📄 [[Week 01/04_มาตรฐานหลักสูตร_ACM_IEEE]]\n")
        new_lines.append("  - 📄 [[Week 01/05_การประยุกต์ใช้ปัญญาประดิษฐ์ในฐานะวิศวกร]]\n")
    elif "Learning Content Week 02 - ฮาร์ดแวร์ ซอฟต์แวร์ และระบบนิเวศสมัยใหม่" in line:
        new_lines.append("- 📁 **Week 02:** [[Week 02/00_Overview - ฮาร์ดแวร์ ซอฟต์แวร์ และระบบนิเวศสมัยใหม่]]\n")
        new_lines.append("  - 📄 [[Week 02/01_สถาปัตยกรรมระดับฮาร์ดแวร์เชิงลึก]]\n")
        new_lines.append("  - 📄 [[Week 02/02_ระบบปฏิบัติการสมัยใหม่และคอนเทนเนอร์]]\n")
        new_lines.append("  - 📄 [[Week 02/03_สถาปัตยกรรม_Edge_Computing]]\n")
        new_lines.append("  - 📄 [[Week 02/04_Green_Computing]]\n")
        new_lines.append("  - 📄 [[Week 02/05_Heterogeneous_Computing]]\n")
    elif "Learning Content Week 03 - วงจรตรรกะและหน่วยประมวลผล" in line:
        new_lines.append("- 📁 **Week 03:** [[Week 03/00_Overview - วงจรตรรกะและหน่วยประมวลผล]]\n")
        new_lines.append("  - 📄 [[Week 03/01_พื้นฐานวงจรตรรกะสู่การออกแบบชิป]]\n")
        new_lines.append("  - 📄 [[Week 03/02_สถาปัตยกรรม_von_Neumann_และ_Harvard]]\n")
        new_lines.append("  - 📄 [[Week 03/03_เจาะลึกสถาปัตยกรรม_RISC-V]]\n")
        new_lines.append("  - 📄 [[Week 03/04_AI_Accelerators]]\n")
        new_lines.append("  - 📄 [[Week 03/05_Chiplet_และยุคหลังกฎของมัวร์]]\n")
    elif "Learning Content Week 04 - อัลกอริทึมและการเขียนโปรแกรม" in line:
        new_lines.append("- 📁 **Week 04:** [[Week 04/00_Overview - อัลกอริทึมและการเขียนโปรแกรม]]\n")
        new_lines.append("  - 📄 [[Week 04/01_การคิดเชิงคำนวณแบบเจาะลึก]]\n")
        new_lines.append("  - 📄 [[Week 04/02_การวิเคราะห์ความซับซ้อน_Big_O]]\n")
        new_lines.append("  - 📄 [[Week 04/03_OOP_vs_Functional]]\n")
        new_lines.append("  - 📄 [[Week 04/04_AI_Coding_Assistants]]\n")
        new_lines.append("  - 📄 [[Week 04/05_Version_Control_และ_Concurrency]]\n")
    elif "Learning Content Week 05 - ฐานข้อมูลและการจัดการข้อมูลขนาดใหญ่" in line:
        new_lines.append("- 📁 **Week 05:** [[Week 05/00_Overview - ฐานข้อมูล]]\n")
        new_lines.append("  - 📄 [[Week 05/01_กลไกเบื้องหลัง_RDBMS]]\n")
        new_lines.append("  - 📄 [[Week 05/02_การขยายระบบด้วย_NoSQL]]\n")
        new_lines.append("  - 📄 [[Week 05/03_แนวคิดของ_Vector_Database]]\n")
        new_lines.append("  - 📄 [[Week 05/04_สถาปัตยกรรม_Big_Data]]\n")
        new_lines.append("  - 📄 [[Week 05/05_Data_Privacy_and_Security]]\n")
    else:
        new_lines.append(line)

with open(index_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Index updated successfully.")
