export interface ModuleData {
  id: string;
  week: number;
  titleTh: string;
  titleEn: string;
  description: string;
  clo: string[];
  topics: string[];
  /** Mini-Project module (1–4) หรือ null สำหรับสัปดาห์สอบ/นำเสนอ */
  project: number | null;
  /** มีใบงาน (Lab) ประจำสัปดาห์หรือไม่ (ใช้เลขเดียวกับ week) */
  hasLab: boolean;
  /** มีแบบทดสอบประจำสัปดาห์หรือไม่ */
  hasExam: boolean;
  labTitle?: string;
  icon: string;
  color: string;
}

export const projects = [
  { id: 1, name: "Module 1: Foundation & Programming", goal: "Simple Text/2D Game", weeks: "W1–W4", color: "green" },
  { id: 2, name: "Module 2: Web Development & Infrastructure", goal: "Asset Management Web App", weeks: "W5–W7", color: "blue" },
  { id: 3, name: "Module 3: IoT & Smart Systems", goal: "Smart Environment Monitor", weeks: "W9–W12", color: "orange" },
  { id: 4, name: "Module 4: Computer Vision & System Integration", goal: "AI Object Detection System", weeks: "W13–W15", color: "purple" },
];

// 17 สัปดาห์ ตามแผนการสอน (รวมสอบกลางภาค W8 และปลายภาค W17)
export const modules: ModuleData[] = [
  {
    id: "01", week: 1,
    titleTh: "ภาพรวมวิศวกรรมคอมพิวเตอร์และระบบสารสนเทศในยุค AI",
    titleEn: "Introduction to Computer Engineering, IS & IT",
    description: "บทบาทของ CE ในระบบคอมพิวเตอร์สมัยใหม่ ความแตกต่างระหว่าง CE/CS/SE/IT/IS มาตรฐาน ACM/IEEE CE2016 และแนวโน้ม AI-driven architecture",
    clo: ["CLO1", "CLO4"],
    topics: ["CE vs CS vs SE vs IT vs IS", "ACM/IEEE CE2016", "AI-driven architecture", "Agentic AI", "วิวัฒนาการคอมพิวเตอร์"],
    project: 1, hasLab: true, hasExam: true,
    labTitle: "ตั้งค่า IDE (Python) และวางแผนพัฒนาเกม",
    icon: "Compass", color: "blue",
  },
  {
    id: "02", week: 2,
    titleTh: "ฮาร์ดแวร์ ซอฟต์แวร์ และระบบนิเวศสมัยใหม่",
    titleEn: "Hardware & Software Ecosystems",
    description: "ลำดับชั้น hardware–firmware–OS–application, CPU/GPU/NPU, memory hierarchy, container, Edge Computing และ Green Computing",
    clo: ["CLO1"],
    topics: ["CPU / GPU / NPU", "Memory hierarchy", "Operating System", "Container", "Edge Computing", "Green Computing", "Heterogeneous Computing"],
    project: 1, hasLab: true, hasExam: true,
    labTitle: "สำรวจสเปกฮาร์ดแวร์และเขียนโค้ดดึงข้อมูลระบบ",
    icon: "Cpu", color: "teal",
  },
  {
    id: "03", week: 3,
    titleTh: "วงจรตรรกะและหน่วยประมวลผล",
    titleEn: "Digital Logic & Modern Processors",
    description: "Boolean algebra, logic gates, half-adder, von Neumann/Harvard, fetch-decode-execute, RISC-V, AI accelerators และ Chiplet",
    clo: ["CLO2"],
    topics: ["Boolean Algebra", "Logic Gates", "von Neumann", "Harvard", "RISC-V", "NPU / TPU", "Chiplet", "Moore's Law"],
    project: 1, hasLab: true, hasExam: true,
    labTitle: "วงจรตรรกะและการประมวลผลข้อมูล",
    icon: "CircuitBoard", color: "indigo",
  },
  {
    id: "04", week: 4,
    titleTh: "อัลกอริทึมและการเขียนโปรแกรม",
    titleEn: "Algorithms & Programming Paradigms",
    description: "Computational thinking, pseudocode/flowchart, Big-O, OOP vs Functional, AI coding assistants, Version control และ Concurrency",
    clo: ["CLO3"],
    topics: ["Computational Thinking", "Pseudocode / Flowchart", "Big-O", "Linear vs Binary search", "OOP vs Functional", "AI Coding Assistant", "Git"],
    project: 1, hasLab: true, hasExam: true,
    labTitle: "อัลกอริทึมและสรุป Mini-Project 1",
    icon: "Code2", color: "green",
  },
  {
    id: "05", week: 5,
    titleTh: "ฐานข้อมูลและการจัดการข้อมูลขนาดใหญ่",
    titleEn: "Database & Data Management",
    description: "Relational database, SQL, key/ER diagram/normalization, ACID, NoSQL, Vector database สำหรับ RAG, Big Data และ Data privacy",
    clo: ["CLO3"],
    topics: ["RDBMS", "SQL", "ER Diagram", "Normalization", "ACID", "NoSQL", "Vector Database", "Embedding", "Big Data"],
    project: 2, hasLab: true, hasExam: true,
    labTitle: "การออกแบบฐานข้อมูลเชิงสัมพันธ์",
    icon: "Database", color: "yellow",
  },
  {
    id: "06", week: 6,
    titleTh: "เครือข่ายคอมพิวเตอร์และอินเทอร์เน็ต",
    titleEn: "Computer Networks & Internet",
    description: "OSI/TCP-IP model, IP/TCP/UDP/DNS/HTTP(S), IPv6, cloud-native networking, edge network และการจำลองเครือข่าย/API เบื้องต้น",
    clo: ["CLO1"],
    topics: ["OSI Model", "TCP/IP", "DNS", "HTTP / HTTPS", "TCP vs UDP", "IPv6", "Wi-Fi 7 / 5G", "Microservices networking", "REST API"],
    project: 2, hasLab: true, hasExam: true,
    labTitle: "เครือข่ายคอมพิวเตอร์และการสร้าง API",
    icon: "Network", color: "sky",
  },
  {
    id: "07", week: 7,
    titleTh: "ศูนย์ข้อมูลและโครงสร้างพื้นฐานระดับคลาวด์",
    titleEn: "Data Center & Cloud Infrastructure",
    description: "องค์ประกอบ data center, virtualization, Docker/Kubernetes, Public/Private/Sovereign cloud, PUE, liquid cooling และ hyperscale",
    clo: ["CLO2", "CLO4"],
    topics: ["Data Center", "Virtualization", "Docker", "Kubernetes", "Cloud service models", "PUE", "Liquid Cooling", "Hyperscale"],
    project: 2, hasLab: true, hasExam: true,
    labTitle: "สถาปัตยกรรมคลาวด์และการ Deploy",
    icon: "Server", color: "cyan",
  },
  {
    id: "08", week: 8,
    titleTh: "ทบทวนและสอบกลางภาค",
    titleEn: "Midterm Examination",
    description: "ทบทวนภาพรวมสัปดาห์ 1–7 เป็นภาพระบบเดียว ฝึกโจทย์วิเคราะห์ และสอบกลางภาคตาม CLO1–CLO3",
    clo: ["CLO1", "CLO2", "CLO3"],
    topics: ["Midterm", "Review", "Concept map"],
    project: null, hasLab: false, hasExam: false,
    icon: "ClipboardList", color: "slate",
  },
  {
    id: "09", week: 9,
    titleTh: "ปัญญาประดิษฐ์และการเรียนรู้ของเครื่อง",
    titleEn: "AI & Machine Learning Foundations",
    description: "AI vs ML vs Deep Learning, supervised/unsupervised/reinforcement learning, feature/label/model, วงจรชีวิตข้อมูล และ MLOps",
    clo: ["CLO1"],
    topics: ["AI / ML / DL", "Supervised vs Unsupervised", "Neural Networks", "Feature / Label", "NIST AI RMF", "MLOps"],
    project: 3, hasLab: true, hasExam: true,
    labTitle: "พื้นฐาน ML และสถาปัตยกรรม IoT",
    icon: "BrainCircuit", color: "purple",
  },
  {
    id: "10", week: 10,
    titleTh: "Generative AI และวิทยาการหุ่นยนต์",
    titleEn: "Generative AI & Modern Robotics",
    description: "Token/embedding/prompt, LLM, RAG, Agentic AI, Physical AI, sense-plan-act และความเสี่ยงของ Generative AI",
    clo: ["CLO1", "CLO4"],
    topics: ["LLM", "Token / Embedding", "Prompt", "RAG", "Agentic AI", "Robotics", "Sense-Plan-Act", "Hallucination"],
    project: 3, hasLab: true, hasExam: true,
    labTitle: "GenAI และฮาร์ดแวร์ไมโครคอนโทรลเลอร์",
    icon: "Sparkles", color: "violet",
  },
  {
    id: "11", week: 11,
    titleTh: "ระบบฝังตัวและอินเทอร์เน็ตของสรรพสิ่ง",
    titleEn: "Embedded Systems & IoT",
    description: "Microcontroller, sensor/actuator, IoT architecture แบบ device–edge–cloud, MQTT/CoAP/Zigbee, TinyML และกรณีศึกษา Smart Home/Factory",
    clo: ["CLO2", "CLO4"],
    topics: ["Embedded System", "ESP32 / Arduino", "Sensor / Actuator", "IoT Architecture", "MQTT", "CoAP", "Zigbee", "TinyML", "Edge AI"],
    project: 3, hasLab: true, hasExam: true,
    labTitle: "การรับส่งข้อมูลผ่านโปรโตคอล MQTT",
    icon: "Radio", color: "orange",
  },
  {
    id: "12", week: 12,
    titleTh: "ความปลอดภัยไซเบอร์และสถาปัตยกรรม Zero Trust",
    titleEn: "Cybersecurity & Trust Architecture",
    description: "CIA triad, cryptography, ภัยคุกคามและการป้องกัน, defense-in-depth, Zero Trust (NIST SP 800-207), OWASP Top 10 และ AI deepfakes",
    clo: ["CLO1", "CLO4"],
    topics: ["CIA Triad", "Cryptography", "Symmetric / Asymmetric", "OWASP Top 10", "Zero Trust", "MFA", "Deepfake", "Digital Provenance"],
    project: 3, hasLab: true, hasExam: true,
    labTitle: "ความปลอดภัยไซเบอร์และนำเสนอ IoT",
    icon: "ShieldCheck", color: "red",
  },
  {
    id: "13", week: 13,
    titleTh: "จริยธรรมทางคอมพิวเตอร์และทรัพย์สินทางปัญญา",
    titleEn: "Computer Ethics & Intellectual Property",
    description: "AI ethics, ACM Code of Ethics, privacy/bias/accountability, ลิขสิทธิ์/สิทธิบัตร, Open source license, PDPA และ GDPR",
    clo: ["CLO5"],
    topics: ["AI Ethics", "ACM Code of Ethics", "Copyright", "Patent", "Open Source License", "PDPA", "GDPR", "Bias"],
    project: 4, hasLab: true, hasExam: true,
    labTitle: "จริยธรรม AI และพื้นฐานวิทัศน์คอมพิวเตอร์",
    icon: "Scale", color: "rose",
  },
  {
    id: "14", week: 14,
    titleTh: "โครงงานประยุกต์และวิศวกรรมระบบ DevOps",
    titleEn: "Applied System Engineering & DevOps",
    description: "SDLC, Agile, DevOps, CI/CD, MLOps/AIOps, Git workflow และการเตรียมโครงงานประยุกต์ (Capstone)",
    clo: ["CLO3", "CLO6"],
    topics: ["SDLC", "Agile", "DevOps", "CI/CD", "MLOps / AIOps", "Git workflow", "Capstone"],
    project: 4, hasLab: true, hasExam: true,
    labTitle: "การบูรณาการระบบและ DevOps",
    icon: "Workflow", color: "emerald",
  },
  {
    id: "15", week: 15,
    titleTh: "การดูงานเชิงวิชาการและอุตสาหกรรมคอมพิวเตอร์",
    titleEn: "Academic Visits & Computer Industry Tour",
    description: "ภาพรวมอุตสาหกรรมและ data center, เตรียมความพร้อมสู่การทำงาน, virtual field trip, บทบาทอาชีพ และการเขียนรายงานดูงาน",
    clo: ["CLO4", "CLO6"],
    topics: ["Site visit", "Industry", "Career path", "Soft skills", "Report writing", "PDPA ในการดูงาน"],
    project: 4, hasLab: true, hasExam: true,
    labTitle: "การเตรียมนำเสนอโครงงานประยุกต์รวม",
    icon: "Building2", color: "amber",
  },
  {
    id: "16", week: 16,
    titleTh: "นำเสนอโครงงานประยุกต์",
    titleEn: "Final Project Presentation",
    description: "การนำเสนอโครงงานรวม 4 โมดูล: problem → architecture → demo → result → limitation และการตอบคำถามเชิงเทคนิค/จริยธรรม",
    clo: ["CLO3", "CLO6"],
    topics: ["Presentation", "Demo", "Rubric", "Q&A"],
    project: null, hasLab: false, hasExam: false,
    icon: "Presentation", color: "fuchsia",
  },
  {
    id: "17", week: 17,
    titleTh: "ทบทวนและสอบปลายภาค",
    titleEn: "Final Examination",
    description: "ทบทวนครึ่งหลังของรายวิชา (AI, GenAI, IoT, security, ethics, DevOps) ด้วยกรณีศึกษา และสอบปลายภาคตาม CLO1, CLO2, CLO4, CLO5",
    clo: ["CLO1", "CLO2", "CLO4", "CLO5"],
    topics: ["Final exam", "Case study", "Review"],
    project: null, hasLab: false, hasExam: false,
    icon: "GraduationCap", color: "slate",
  },
];

export function getModuleById(id: string): ModuleData | undefined {
  return modules.find((m) => m.id === id);
}

export const colorMap: Record<string, { bg: string; text: string; border: string; accent: string }> = {
  slate: { bg: "bg-slate-100 dark:bg-slate-800/40", text: "text-slate-700 dark:text-slate-300", border: "border-slate-200 dark:border-slate-700", accent: "from-slate-500 to-gray-500" },
  blue: { bg: "bg-blue-50 dark:bg-blue-900/20", text: "text-blue-700 dark:text-blue-300", border: "border-blue-200 dark:border-blue-800", accent: "from-blue-500 to-cyan-500" },
  sky: { bg: "bg-sky-50 dark:bg-sky-900/20", text: "text-sky-700 dark:text-sky-300", border: "border-sky-200 dark:border-sky-800", accent: "from-sky-500 to-blue-500" },
  cyan: { bg: "bg-cyan-50 dark:bg-cyan-900/20", text: "text-cyan-700 dark:text-cyan-300", border: "border-cyan-200 dark:border-cyan-800", accent: "from-cyan-500 to-teal-500" },
  green: { bg: "bg-green-50 dark:bg-green-900/20", text: "text-green-700 dark:text-green-300", border: "border-green-200 dark:border-green-800", accent: "from-green-500 to-emerald-500" },
  emerald: { bg: "bg-emerald-50 dark:bg-emerald-900/20", text: "text-emerald-700 dark:text-emerald-300", border: "border-emerald-200 dark:border-emerald-800", accent: "from-emerald-500 to-green-500" },
  yellow: { bg: "bg-yellow-50 dark:bg-yellow-900/20", text: "text-yellow-700 dark:text-yellow-300", border: "border-yellow-200 dark:border-yellow-800", accent: "from-yellow-500 to-orange-500" },
  amber: { bg: "bg-amber-50 dark:bg-amber-900/20", text: "text-amber-700 dark:text-amber-300", border: "border-amber-200 dark:border-amber-800", accent: "from-amber-500 to-yellow-500" },
  red: { bg: "bg-red-50 dark:bg-red-900/20", text: "text-red-700 dark:text-red-300", border: "border-red-200 dark:border-red-800", accent: "from-red-500 to-pink-500" },
  purple: { bg: "bg-purple-50 dark:bg-purple-900/20", text: "text-purple-700 dark:text-purple-300", border: "border-purple-200 dark:border-purple-800", accent: "from-purple-500 to-violet-500" },
  violet: { bg: "bg-violet-50 dark:bg-violet-900/20", text: "text-violet-700 dark:text-violet-300", border: "border-violet-200 dark:border-violet-800", accent: "from-violet-500 to-purple-500" },
  fuchsia: { bg: "bg-fuchsia-50 dark:bg-fuchsia-900/20", text: "text-fuchsia-700 dark:text-fuchsia-300", border: "border-fuchsia-200 dark:border-fuchsia-800", accent: "from-fuchsia-500 to-pink-500" },
  teal: { bg: "bg-teal-50 dark:bg-teal-900/20", text: "text-teal-700 dark:text-teal-300", border: "border-teal-200 dark:border-teal-800", accent: "from-teal-500 to-cyan-500" },
  indigo: { bg: "bg-indigo-50 dark:bg-indigo-900/20", text: "text-indigo-700 dark:text-indigo-300", border: "border-indigo-200 dark:border-indigo-800", accent: "from-indigo-500 to-blue-500" },
  orange: { bg: "bg-orange-50 dark:bg-orange-900/20", text: "text-orange-700 dark:text-orange-300", border: "border-orange-200 dark:border-orange-800", accent: "from-orange-500 to-amber-500" },
  rose: { bg: "bg-rose-50 dark:bg-rose-900/20", text: "text-rose-700 dark:text-rose-300", border: "border-rose-200 dark:border-rose-800", accent: "from-rose-500 to-pink-500" },
};
