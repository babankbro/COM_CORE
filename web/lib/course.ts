// ข้อมูลรายวิชา — ใช้ร่วมกันทุกหน้า
export const course = {
  code: "EN-001-019",
  titleTh: "แก่นวิศวกรรมคอมพิวเตอร์",
  titleEn: "Computer Engineering Essentials",
  credits: "3(2-2-5)",
  instructor: "ผศ.ดร. สรายุทธ กรวิรัตน์",
  program: "สาขาวิชาวิศวกรรมคอมพิวเตอร์",
  faculty: "คณะวิศวกรรมศาสตร์และเทคโนโลยีอุตสาหกรรม มหาวิทยาลัยกาฬสินธุ์",
  year: "2569",
  description:
    "Overview of computer engineering, information system and information technology; hardware and software; logic circuit and processor; algorithm and program; database; computer network and internet, artificial intelligence and robot; embedded system; data center; security; computer ethics; intellectual property; academic visits computer industry.",
};

export const courseLabel = `${course.code} ${course.titleEn}`;

export const clos = [
  { id: "CLO1", text: "อธิบายองค์ความรู้พื้นฐานเกี่ยวกับซอฟต์แวร์ ฮาร์ดแวร์ เครือข่ายคอมพิวเตอร์ และปัญญาประดิษฐ์ รวมถึงพื้นฐานคณิตศาสตร์/วิทยาศาสตร์/วิศวกรรมที่เกี่ยวข้อง", plo: "PLO1", ksa: "K3" },
  { id: "CLO2", text: "อธิบายหลักการและสถาปัตยกรรมของฮาร์ดแวร์และซอฟต์แวร์ขั้นสูง — วงจรตรรก หน่วยประมวลผล ระบบฝังตัว และศูนย์ข้อมูล", plo: "PLO2", ksa: "K5" },
  { id: "CLO3", text: "ออกแบบอัลกอริทึม เขียนโปรแกรม และจัดการฐานข้อมูลเบื้องต้น เพื่อแก้ปัญหาทางวิศวกรรมคอมพิวเตอร์", plo: "PLO2", ksa: "S4" },
  { id: "CLO4", text: "เลือกใช้เครื่องมือและเทคโนโลยีสมัยใหม่ในการพัฒนาระบบ และตระหนักถึงความสำคัญของการพัฒนาเทคโนโลยี", plo: "PLO4", ksa: "A8" },
  { id: "CLO5", text: "อธิบายและตระหนักถึงจรรยาบรรณวิชาชีพ กฎหมาย และทรัพย์สินทางปัญญาทางคอมพิวเตอร์", plo: "PLO2, PLO6", ksa: "A3, K14" },
  { id: "CLO6", text: "ทำงานเป็นทีม ประสานงาน และเข้าใจการบริหารโครงการ/การทำงานในองค์กร ผ่านโครงงานและการดูงานอุตสาหกรรม", plo: "PLO6", ksa: "K15, S14" },
];

export const textbooks = [
  "Patterson, D. A., & Hennessy, J. L. Computer Organization and Design (RISC-V ed.). Morgan Kaufmann, 2020.",
  "ACM/IEEE. Computer Engineering Curricula 2016 (CE2016).",
  "Kurose, J. F., & Ross, K. W. Computer Networking: A Top-Down Approach (8th ed.). Pearson, 2021.",
  "Russell, S., & Norvig, P. Artificial Intelligence: A Modern Approach (4th ed.). Pearson, 2021.",
];
