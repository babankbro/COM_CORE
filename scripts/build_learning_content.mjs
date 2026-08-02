import fs from "node:fs/promises";
import path from "node:path";

const root = process.env.PROJECT_ROOT ? path.resolve(process.env.PROJECT_ROOT) : process.cwd();
const outDir = path.join(root, "wiki", "learning");

const commonSources = {
  ce2016: ["ACM/IEEE Computer Engineering Curricula 2016", "https://www.acm.org/binaries/content/assets/education/ce2016-final-report.pdf"],
  cs2023: ["ACM/IEEE-CS/AAAI Computer Science Curricula 2023", "https://dl.acm.org/doi/book/10.1145/3664191"],
  acmEthics: ["ACM Code of Ethics and Professional Conduct", "https://www.acm.org/code-of-ethics"],
  docker: ["Docker Docs: What is a container?", "https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/"],
  kubernetes: ["Kubernetes Docs: Concepts", "https://kubernetes.io/docs/concepts/"],
  nistAi: ["NIST AI Risk Management Framework", "https://www.nist.gov/itl/ai-risk-management-framework"],
  nistGenAi: ["NIST AI RMF Generative AI Profile", "https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence"],
  zta: ["NIST SP 800-207 Zero Trust Architecture", "https://csrc.nist.gov/pubs/sp/800/207/final"],
  owasp: ["OWASP Top 10 Web Application Security Risks", "https://owasp.org/www-project-top-ten/"],
  mqtt: ["MQTT.org: The Standard for IoT Messaging", "https://mqtt.org/"],
  riscv: ["RISC-V International", "https://riscv.org/"],
  rfc8200: ["IETF RFC 8200 IPv6 Specification", "https://datatracker.ietf.org/doc/html/rfc8200"],
  cncf: ["Cloud Native Computing Foundation", "https://www.cncf.io/"],
  pue: ["The Green Grid: PUE Comprehensive Examination", "https://www.thegreengrid.org/en/resources/library-and-tools/20-PUE%3A-A-Comprehensive-Examination-of-the-Metric"],
  pgvector: ["pgvector: Vector similarity search for PostgreSQL", "https://github.com/pgvector/pgvector"],
  sqlVector: ["Microsoft Learn: SQL Server vector search", "https://learn.microsoft.com/en-us/sql/sql-server/ai/vectors?view=sql-server-ver17"],
  pdpa: ["MDES: Personal Data Protection Act B.E. 2562", "https://mdes.go.th/law/detail/3577-Personal-Data-Protection-Act-B-E--2562--2019-"],
};

const weeks = [
  {
    n: 1,
    title: "ภาพรวมวิศวกรรมคอมพิวเตอร์และระบบสารสนเทศในยุค AI",
    source: "Week 01 - Introduction to CE & IT",
    question: "วิศวกรรมคอมพิวเตอร์ต่างจากสายคอมพิวเตอร์อื่นอย่างไร และทำไมยุค AI ทำให้เส้นแบ่งสาขาเบลอลง?",
    goals: ["อธิบายบทบาทของ CE ในระบบคอมพิวเตอร์สมัยใหม่", "แยก CE, CS, SE, IT และ IS ด้วยมุมมองงานจริง", "เชื่อมภาพรวมรายวิชากับแนวโน้ม AI-driven systems"],
    ideas: [
      "CE คือสาขาที่เชื่อมฮาร์ดแวร์ ซอฟต์แวร์ และระบบจริงเข้าด้วยกัน ตั้งแต่วงจรจนถึงบริการที่ผู้ใช้สัมผัส",
      "CS เน้นแนวคิดและอัลกอริทึม, SE เน้นกระบวนการสร้างซอฟต์แวร์, IT เน้นดูแลบริการ, IS เน้นเทคโนโลยีกับองค์กร",
      "AI, edge, cloud และ cybersecurity ทำให้วิศวกรต้องเข้าใจข้ามชั้นของระบบ ไม่ใช่รู้เฉพาะโปรแกรมหรือฮาร์ดแวร์อย่างเดียว",
    ],
    lesson: [
      "เริ่มจากวาดระบบง่าย ๆ เช่นแอปเกมออนไลน์หนึ่งตัว แล้วแยกว่ามีฮาร์ดแวร์ เครื่องลูกข่าย เครือข่าย ฐานข้อมูล โค้ด และผู้ใช้อยู่ตรงไหน วิธีนี้ช่วยให้ผู้เรียนเห็นว่า CE ไม่ได้เรียนเฉพาะคอมพิวเตอร์เครื่องเดียว แต่เรียนระบบที่ประกอบกันหลายชั้น",
      "มาตรฐาน CE2016 ของ ACM/IEEE ใช้แนวคิด body of knowledge สำหรับหลักสูตรวิศวกรรมคอมพิวเตอร์ โดยเน้นการออกแบบและบูรณาการระบบคอมพิวเตอร์ทั้งฮาร์ดแวร์และซอฟต์แวร์ จึงเหมาะใช้เป็นกรอบอธิบายว่ารายวิชานี้กำลังปูพื้นอะไร",
      "ปิดบทเรียนด้วยคำถามว่า ถ้า AI agent เขียนโค้ด สั่งอุปกรณ์ และ deploy ระบบเองได้ นักศึกษายังต้องรู้อะไรบ้าง คำตอบคือยังต้องเข้าใจสถาปัตยกรรม ข้อจำกัด ความปลอดภัย และความรับผิดชอบของระบบ",
    ],
    activity: "ให้ผู้เรียนเลือกบริการดิจิทัล 1 อย่าง แล้วทำ system map แยกส่วน CE/CS/SE/IT/IS พร้อมระบุว่าจุดใดเกี่ยวข้องกับ AI",
    check: ["CE มีขอบเขตใดที่ CS อย่างเดียวไม่ครอบคลุม?", "ตัวอย่างงาน IT กับ IS ต่างกันอย่างไร?", "AI ทำให้วิศวกรคอมพิวเตอร์ต้องเพิ่มทักษะใด?"],
    sources: ["ce2016", "cs2023"],
  },
  {
    n: 2,
    title: "ฮาร์ดแวร์ ซอฟต์แวร์ และระบบนิเวศสมัยใหม่",
    source: "Week 02 - Hardware & Software Ecosystems",
    question: "โปรแกรมหนึ่งตัวทำงานผ่านชั้นฮาร์ดแวร์ ซอฟต์แวร์ และระบบปฏิบัติการอย่างไร?",
    goals: ["อธิบายลำดับชั้น hardware-firmware-OS-application", "เข้าใจ CPU/GPU/NPU, หน่วยความจำ, storage และ I/O", "เชื่อม edge computing กับ green computing"],
    ideas: [
      "คอมพิวเตอร์ทำงานเป็นชั้น: hardware ให้ทรัพยากร, OS จัดการทรัพยากร, application แก้ปัญหาผู้ใช้",
      "memory hierarchy คือการแลกเปลี่ยนระหว่างความเร็ว ราคา และขนาด ตั้งแต่ register/cache/RAM/storage",
      "edge computing ย้ายการประมวลผลเข้าใกล้แหล่งข้อมูล ส่วน green computing ทำให้การออกแบบระบบต้องคิดเรื่องพลังงานตั้งแต่ต้น",
    ],
    lesson: [
      "ให้เริ่มจากคำสั่งง่าย ๆ เช่นเปิดไฟล์หรือกดปุ่มในเกม แล้วตามรอยว่าคำสั่งเดินทางผ่าน application, system call, OS, driver, storage และ CPU อย่างไร",
      "เปรียบเทียบ CPU, GPU และ NPU ด้วยชนิดงาน: CPU เหมาะงานทั่วไปและควบคุมลำดับ, GPU เหมาะงานขนาน, NPU เหมาะ inference ของ AI บนอุปกรณ์",
      "โยงไปยังการออกแบบที่รับผิดชอบ: ถ้าระบบ AI ประมวลผลบน edge ได้ จะลด latency และลดการส่งข้อมูลบางส่วนขึ้น cloud แต่ต้องคุมพลังงาน ความร้อน และการอัปเดตซอฟต์แวร์ให้ดี",
    ],
    activity: "ให้ผู้เรียนตรวจสเปกเครื่องตนเอง แล้วอธิบายว่า CPU, RAM, storage และ GPU/NPU ส่งผลต่อการเรียนเขียนโปรแกรม/AI อย่างไร",
    check: ["ทำไม cache เร็วกว่า RAM แต่มีขนาดเล็กกว่า?", "OS ทำหน้าที่ใดระหว่างโปรแกรมกับฮาร์ดแวร์?", "edge computing ช่วยลด latency ได้อย่างไร?"],
    sources: ["ce2016", "cs2023"],
  },
  {
    n: 3,
    title: "วงจรตรรกะและหน่วยประมวลผล",
    source: "Week 03 - Digital Logic & Modern Processors",
    question: "คอมพิวเตอร์แปลง 0/1 ให้กลายเป็นการคำนวณและการตัดสินใจได้อย่างไร?",
    goals: ["อธิบาย Boolean algebra และ logic gates", "เชื่อมวงจรพื้นฐานกับ ALU/register/control unit", "เปรียบเทียบ CPU, GPU, NPU และ RISC-V"],
    ideas: [
      "logic gate เป็นหน่วยเล็กที่สุดของการตัดสินใจเชิงดิจิทัล เมื่อนำมาประกอบกันจะเกิด adder, register และวงจรควบคุม",
      "fetch-decode-execute คือวงจรพื้นฐานของ processor: ดึงคำสั่ง แปลคำสั่ง แล้วดำเนินการ",
      "RISC-V เป็น ISA แบบเปิด ทำให้ผู้เรียนเห็นว่าชุดคำสั่งเป็นสัญญาระหว่างซอฟต์แวร์กับฮาร์ดแวร์",
    ],
    lesson: [
      "เริ่มจากตารางความจริงของ AND, OR, XOR แล้วให้ผู้เรียนสร้าง half-adder จาก XOR และ AND เพื่อเห็นว่าการบวกเลขเริ่มจากตรรกะพื้นฐาน",
      "อธิบาย von Neumann architecture ด้วยเส้นทางข้อมูล: memory เก็บคำสั่งและข้อมูล, CPU มี ALU/control/register, bus เป็นทางสื่อสาร",
      "ปิดด้วย processor ยุค AI: GPU/NPU ไม่ได้แทน CPU แต่ทำหน้าที่เร่งงานเฉพาะ เช่น matrix multiplication และ inference",
    ],
    activity: "ใช้ Logisim หรือ simulator สร้าง half-adder/full-adder แล้วเขียนเงื่อนไขเกมที่ใช้ Boolean logic อย่างน้อย 3 เงื่อนไข",
    check: ["XOR ใช้ใน adder เพราะอะไร?", "fetch-decode-execute มีขั้นตอนใดบ้าง?", "RISC-V ต่างจาก ISA ปิดในเชิงการเรียนรู้และนวัตกรรมอย่างไร?"],
    sources: ["riscv", "ce2016"],
  },
  {
    n: 4,
    title: "อัลกอริทึมและการเขียนโปรแกรม",
    source: "Week 04 - Algorithms & Programming Paradigms",
    question: "ทำไมการคิดเชิงอัลกอริทึมยังสำคัญ แม้มี AI ช่วยเขียนโค้ด?",
    goals: ["ออกแบบขั้นตอนแก้ปัญหาด้วย decomposition และ abstraction", "เขียน pseudocode/flowchart สำหรับปัญหาง่าย", "วิเคราะห์ Big-O เบื้องต้นและใช้ AI assistant อย่างรับผิดชอบ"],
    ideas: [
      "algorithm คือขั้นตอนชัดเจน มีอินพุต เอาต์พุต และจบได้ ไม่ใช่แค่โค้ดในภาษาใดภาษาหนึ่ง",
      "Big-O ช่วยคิดว่าเมื่อข้อมูลใหญ่ขึ้น โปรแกรมจะช้าลงอย่างไร",
      "AI assistant ช่วยเร่งงานเขียนโค้ดได้ แต่ผู้เรียนยังต้องตรวจตรรกะ ทดสอบ และรับผิดชอบผลลัพธ์",
    ],
    lesson: [
      "ให้เริ่มจากปัญหาในชีวิตประจำวัน เช่นหาคะแนนสูงสุดในรายชื่อ แล้วแปลงเป็น decomposition, pseudocode และ flowchart",
      "เปรียบเทียบ linear search กับ binary search เพื่อให้เห็นว่าอัลกอริทึมต่างกันทำให้ประสิทธิภาพต่างกัน แม้คำตอบสุดท้ายเหมือนกัน",
      "สาธิตการใช้ AI ช่วยเขียนโค้ดอย่างถูกวิธี: เขียนโจทย์ให้ชัด ขอ test cases ขออธิบาย complexity แล้วผู้เรียนต้องรันและตรวจเอง",
    ],
    activity: "ให้ผู้เรียนเขียน pseudocode ของ mini game loop แล้วให้ AI ช่วยแปลงเป็น Python พร้อมอธิบายว่าต้องตรวจส่วนใดก่อนส่ง",
    check: ["O(n) ต่างจาก O(n²) อย่างไร?", "flowchart ช่วยก่อนเขียนโค้ดอย่างไร?", "ข้อควรระวัง 2 ข้อเมื่อใช้ AI assistant คืออะไร?"],
    sources: ["cs2023", "acmEthics"],
  },
  {
    n: 5,
    title: "ฐานข้อมูลและการจัดการข้อมูลขนาดใหญ่",
    source: "Week 05 - Database & Data Management",
    question: "ข้อมูลควรถูกจัดเก็บอย่างไรให้ค้นหา เชื่อมโยง และนำไปใช้กับ AI ได้?",
    goals: ["เข้าใจ relational database และ SQL", "อธิบาย key, ER diagram, normalization และ ACID", "รู้จัก vector database สำหรับ semantic search/RAG"],
    ideas: [
      "ฐานข้อมูลเชิงสัมพันธ์จัดข้อมูลเป็นตารางและความสัมพันธ์ ทำให้ลดความซ้ำซ้อนและ query ได้ชัดเจน",
      "SQL เป็นภาษากลางสำหรับถามข้อมูล เช่น SELECT, JOIN, WHERE, GROUP BY",
      "vector database เก็บ embedding เพื่อค้นหาความหมาย ไม่ใช่แค่คำตรงตัว จึงสำคัญกับ RAG และ LLM",
    ],
    lesson: [
      "เริ่มด้วยกรณีระบบนักศึกษา: ตาราง Student, Course, Enrollment ช่วยให้เห็น primary key และ foreign key ชัดกว่าอธิบายเชิงนิยามอย่างเดียว",
      "ACID คือหลักที่ทำให้ธุรกรรมเชื่อถือได้ เช่นการโอนเงินหรือบันทึกคะแนนต้องครบ ถูกต้อง แยกจากกัน และไม่หายเมื่อระบบล่ม",
      "เชื่อมสู่ยุค AI: embedding เปลี่ยนข้อความเป็นเวกเตอร์ แล้วค้นหาด้วย similarity search เช่น cosine distance เพื่อดึงเอกสารที่เกี่ยวข้องให้ LLM ตอบ",
    ],
    activity: "ออกแบบ ER diagram ของระบบเกม/ร้านค้าเล็ก ๆ แล้วเขียน SQL อย่างน้อย 3 คำสั่ง รวม SELECT แบบ JOIN",
    check: ["primary key กับ foreign key ต่างกันอย่างไร?", "normalization ช่วยลดปัญหาใด?", "vector search ต่างจาก keyword search อย่างไร?"],
    sources: ["pgvector", "sqlVector"],
  },
  {
    n: 6,
    title: "เครือข่ายคอมพิวเตอร์และอินเทอร์เน็ต",
    source: "Week 06 - Computer Networks & Internet",
    question: "ข้อมูลเดินทางจากเครื่องเราไปยังบริการบนอินเทอร์เน็ตผ่านชั้นใดบ้าง?",
    goals: ["อธิบาย OSI/TCP-IP model", "รู้จัก IP, TCP/UDP, DNS, HTTP/HTTPS และ subnet", "เข้าใจ latency, edge network และ cloud-native networking"],
    ideas: [
      "TCP/IP เป็นกรอบคิดหลักของอินเทอร์เน็ต แบ่งบทบาทตั้งแต่ link, internet, transport ถึง application",
      "TCP เน้นความครบถ้วนและลำดับข้อมูล ส่วน UDP ลด overhead เหมาะกับงาน real-time บางประเภท",
      "IPv6 ตาม RFC 8200 เป็นมาตรฐานสำคัญสำหรับพื้นที่ address และการเติบโตของอินเทอร์เน็ต",
    ],
    lesson: [
      "สอนด้วยการเปิดเว็บหนึ่งหน้า: DNS แปลงชื่อโดเมนเป็น IP, TCP/TLS สร้างการเชื่อมต่อ, HTTP ส่ง request/response, router ส่ง packet ผ่านหลายเครือข่าย",
      "ให้ผู้เรียนเห็นว่าเครือข่ายไม่ใช่แค่สายหรือ Wi-Fi แต่รวม protocol, addressing, routing, security และ performance",
      "โยง cloud-native: microservices จำนวนมากต้องสื่อสารกันผ่าน network ภายใน cluster ดังนั้น latency, retry, timeout และ observability กลายเป็นหัวข้อวิศวกรรมสำคัญ",
    ],
    activity: "ใช้ ping, tracert/traceroute และ nslookup ตรวจเส้นทางไปยังเว็บหนึ่ง แล้วอธิบายผลด้วย TCP/IP model",
    check: ["DNS ทำหน้าที่อะไร?", "TCP กับ UDP ต่างกันอย่างไร?", "IPv6 แก้ข้อจำกัดสำคัญใดของ IPv4?"],
    sources: ["rfc8200", "cncf"],
  },
  {
    n: 7,
    title: "ศูนย์ข้อมูลและโครงสร้างพื้นฐานระดับคลาวด์",
    source: "Week 07 - Data Center & Cloud Infrastructure",
    question: "บริการ cloud และ AI ต้องพึ่งพา data center อย่างไร?",
    goals: ["อธิบายองค์ประกอบ data center", "เข้าใจ virtualization, containerization, Docker/Kubernetes", "ใช้ PUE เป็นตัวชี้วัดพลังงาน"],
    ideas: [
      "data center รวม compute, storage, network, power, cooling และ physical security เพื่อให้บริการต่อเนื่อง",
      "container ช่วยแพ็กแอปกับ dependencies ให้รันได้สม่ำเสมอหลาย environment ส่วน Kubernetes ช่วยจัดการ workload จำนวนมาก",
      "PUE คือพลังงานรวมของ data center หารด้วยพลังงาน IT ยิ่งใกล้ 1 ยิ่งมีประสิทธิภาพ",
    ],
    lesson: [
      "เริ่มจากการเปรียบเทียบ server ห้องหนึ่งกับ hyperscale data center: สิ่งที่เพิ่มขึ้นคือ reliability, redundancy, cooling, monitoring และ automation",
      "อธิบาย container ด้วยภาพกล่องซอฟต์แวร์: ไม่ใช่ VM เต็มเครื่อง แต่เป็น process ที่แยกสภาพแวดล้อมและแชร์ kernel จึงเบากว่า",
      "เชื่อมกับ AI: workload ที่ใช้ GPU จำนวนมากทำให้ rack density และความร้อนสูงขึ้น การออกแบบพลังงานและ liquid cooling จึงกลายเป็นประเด็นวิศวกรรมหลัก",
    ],
    activity: "ทดลองรันแอปง่าย ๆ ด้วย Docker แล้วคำนวณ PUE จากโจทย์ตัวอย่าง 3 กรณี",
    check: ["container ต่างจาก VM อย่างไร?", "Kubernetes ช่วยจัดการอะไร?", "PUE 1.8 กับ 1.2 บอกอะไรเกี่ยวกับ data center?"],
    sources: ["docker", "kubernetes", "pue"],
  },
  {
    n: 8,
    title: "ทบทวนและสอบกลางภาค",
    source: "Week 08 - Midterm Examination",
    question: "เราจะเชื่อมความรู้สัปดาห์ 1-7 เป็นภาพระบบเดียวได้อย่างไร?",
    goals: ["ทบทวน CE ecosystem ตั้งแต่ hardware ถึง cloud", "ฝึกแก้โจทย์วิเคราะห์ ไม่ใช่จำคำศัพท์", "เตรียมสอบกลางภาคตาม CLO1-CLO3"],
    ideas: [
      "หัวข้อก่อนกลางภาคเรียงจากภาพรวมสาขา → hardware/software → logic/processor → programming → database → network → cloud",
      "โจทย์ที่ดีมักให้สถานการณ์ระบบหนึ่ง แล้วถามให้แยกองค์ประกอบ ออกแบบข้อมูล หรืออธิบาย trade-off",
      "การทบทวนควรทำเป็น concept map และ practice problems มากกว่าการอ่านซ้ำอย่างเดียว",
    ],
    lesson: [
      "ให้ผู้เรียนเลือกโครงงานเกม/web app ที่ทำมา แล้ว map ว่าใช้ความรู้จากสัปดาห์ใดบ้าง เช่น logic อยู่ใน game rule, database อยู่ใน save/load, network อยู่ใน API",
      "ทบทวนด้วยโจทย์ผสม: ออกแบบ ER diagram, เขียน pseudocode, คำนวณเลขฐาน, อธิบาย TCP/UDP และคำนวณ PUE",
      "ให้ผู้เรียนทำ one-page cheat sheet เชิงแนวคิด แม้ใช้ไม่ได้ในสอบ แต่กระบวนการสรุปจะเผยช่องว่างความเข้าใจ",
    ],
    activity: "จัด peer review: นักศึกษาแลกกันอธิบาย concept map แล้วเพื่อนตั้งคำถาม 3 ข้อ",
    check: ["สัปดาห์ 1-7 เชื่อมกันเป็นระบบอย่างไร?", "หัวข้อใดใช้ใน project มากที่สุด?", "ข้อสอบแบบกรณีศึกษาควรเริ่มวิเคราะห์จากอะไร?"],
    sources: ["ce2016", "cs2023"],
  },
  {
    n: 9,
    title: "ปัญญาประดิษฐ์และการเรียนรู้ของเครื่อง",
    source: "Week 09 - AI & Machine Learning Foundations",
    question: "เครื่องเรียนรู้จากข้อมูลได้อย่างไร และทำไมการนำโมเดลไปใช้จริงต้องมี MLOps?",
    goals: ["แยก AI, ML และ deep learning", "เข้าใจ supervised/unsupervised/reinforcement learning", "อธิบาย lifecycle ของโมเดลและ MLOps"],
    ideas: [
      "ML คือการสร้างโมเดลจากข้อมูลเพื่อทำนายหรือจัดกลุ่ม โดยไม่ได้เขียนกฎทุกข้อด้วยมือ",
      "คุณภาพข้อมูลส่งผลต่อคุณภาพโมเดลโดยตรง เพราะโมเดลเรียนรู้ pattern รวมถึง bias จากข้อมูล",
      "MLOps ทำให้การฝึก ประเมิน deploy และ monitor โมเดลเป็นกระบวนการที่ตรวจสอบซ้ำได้",
    ],
    lesson: [
      "เริ่มจากโจทย์จำแนกผลไม้ด้วยน้ำหนักและสี แล้วอธิบาย feature, label, training data, model และ prediction",
      "เปรียบเทียบ supervised learning กับ unsupervised learning: แบบแรกมีคำตอบให้เรียน แบบหลังหาโครงสร้างหรือกลุ่มในข้อมูล",
      "NIST AI RMF ช่วยให้มอง AI ไม่ใช่แค่ความแม่นยำ แต่รวม validity, safety, security, fairness, accountability และ governance",
    ],
    activity: "ใช้ dataset เล็ก ๆ ฝึก classification model แล้วบันทึก feature, metric, error case และข้อจำกัดของข้อมูล",
    check: ["training กับ inference ต่างกันอย่างไร?", "bias เกิดได้จากจุดใดของ lifecycle?", "ทำไมต้อง monitor โมเดลหลัง deploy?"],
    sources: ["nistAi", "cs2023"],
  },
  {
    n: 10,
    title: "Generative AI และวิทยาการหุ่นยนต์",
    source: "Week 10 - Generative AI & Modern Robotics",
    question: "Generative AI จากซอฟต์แวร์จะเชื่อมกับการลงมือทำในโลกจริงผ่านหุ่นยนต์ได้อย่างไร?",
    goals: ["เข้าใจ token, embedding, prompt, LLM และ RAG", "อธิบาย agentic AI และ sense-plan-act", "วิเคราะห์ความเสี่ยงของ generative AI และ robotics"],
    ideas: [
      "LLM ทำนาย token ถัดไปจากบริบทขนาดใหญ่ จึงสร้างข้อความ โค้ด และคำอธิบายได้ แต่ไม่ได้รับประกันว่าถูกเสมอ",
      "RAG ลดปัญหาความรู้ไม่ทันสมัยด้วยการค้นเอกสารที่เกี่ยวข้องแล้วส่งเข้า prompt",
      "หุ่นยนต์ใช้วงจร sense-plan-act และเมื่อนำ LLM/AI เข้าไปช่วยวางแผน ต้องคุม safety และ verification เข้มขึ้น",
    ],
    lesson: [
      "สอน LLM แบบไม่ลงคณิตหนัก: ข้อความถูกแปลงเป็น token, model ใช้บริบทเพื่อคาดการณ์, embedding ช่วยแทนความหมายในเชิงเวกเตอร์",
      "อธิบาย agentic AI ด้วยงานหลายขั้นตอน เช่นวางแผน ค้นข้อมูล เรียกเครื่องมือ เขียนไฟล์ และตรวจผล แต่ต้องมีขอบเขตสิทธิ์และ human oversight",
      "เชื่อม robotics: sensor รับโลกจริง, planner ตัดสินใจ, actuator ลงมือทำ ความผิดพลาดของ AI จึงอาจกลายเป็นความเสี่ยงทางกายภาพ",
    ],
    activity: "ให้ผู้เรียนออกแบบ prompt + retrieval source สำหรับผู้ช่วยตอบคำถามรายวิชา แล้วระบุ guardrails อย่างน้อย 3 ข้อ",
    check: ["RAG ต่างจากการถาม LLM ตรง ๆ อย่างไร?", "agentic AI ต้องมี control อะไร?", "ความเสี่ยงของ AI ในหุ่นยนต์ต่างจาก chatbot อย่างไร?"],
    sources: ["nistGenAi", "pgvector", "nistAi"],
  },
  {
    n: 11,
    title: "ระบบฝังตัวและอินเทอร์เน็ตของสรรพสิ่ง",
    source: "Week 11 - Embedded Systems & IoT",
    question: "อุปกรณ์ขนาดเล็กสื่อสารกับ cloud และ dashboard ได้อย่างไร?",
    goals: ["เข้าใจ embedded system, sensor, actuator และ microcontroller", "อธิบาย IoT architecture แบบ device-edge-cloud", "ใช้ MQTT publish/subscribe เป็นรูปแบบสื่อสาร"],
    ideas: [
      "embedded system คือคอมพิวเตอร์ที่ฝังอยู่ในอุปกรณ์เพื่อทำงานเฉพาะ เช่นอ่าน sensor และควบคุม actuator",
      "IoT รวม device, connectivity, backend, dashboard และ security เข้าด้วยกัน",
      "MQTT เป็น protocol แบบ publish/subscribe ที่เบา เหมาะกับอุปกรณ์และเครือข่ายจำกัด",
    ],
    lesson: [
      "เริ่มด้วยวงจร sensor → microcontroller → network → server → dashboard แล้วถามว่าข้อมูลผิดพลาดหรือหลุดได้ที่จุดใดบ้าง",
      "อธิบาย MQTT ผ่านบทบาท broker, publisher, subscriber, topic และ QoS เพื่อให้ผู้เรียนเห็นว่าการส่งข้อมูล sensor ไม่จำเป็นต้องเป็น request/response เสมอไป",
      "โยง TinyML และ edge AI: บางงาน เช่นตรวจจับเสียงหรือภาพเบื้องต้น สามารถทำบนอุปกรณ์เพื่อลด latency และลดข้อมูลที่ส่งออก",
    ],
    activity: "ต่อ ESP32/Arduino อ่านค่า sensor แล้วส่งค่าแบบจำลองผ่าน MQTT topic ไปยัง dashboard หรือ broker local",
    check: ["sensor กับ actuator ต่างกันอย่างไร?", "MQTT broker ทำหน้าที่อะไร?", "ทำไม IoT ต้องคิดเรื่องพลังงานและ security ตั้งแต่ต้น?"],
    sources: ["mqtt", "ce2016"],
  },
  {
    n: 12,
    title: "Cybersecurity และ Zero Trust",
    source: "Week 12 - Cybersecurity & Trust Architecture",
    question: "เราจะปกป้องระบบที่กระจายบน cloud, IoT และ AI ได้อย่างไร?",
    goals: ["อธิบาย CIA triad และ threat พื้นฐาน", "เข้าใจ least privilege, MFA, encryption และ secure coding", "อธิบาย Zero Trust และ OWASP Top 10"],
    ideas: [
      "CIA triad คือ confidentiality, integrity, availability เป็นกรอบแรกในการคิดความปลอดภัย",
      "Zero Trust ย้ายจากการเชื่อใจเครือข่ายภายใน ไปสู่การตรวจสอบ identity, device, context และ policy ทุกครั้ง",
      "OWASP Top 10 เป็นเอกสาร awareness สำหรับความเสี่ยงเว็บแอปที่นักพัฒนาควรรู้",
    ],
    lesson: [
      "เริ่มจาก incident สมมุติ เช่นเว็บแอปถูก SQL injection แล้วให้ผู้เรียนแยกว่า CIA ด้านใดเสียหายและควรป้องกันที่ชั้นใด",
      "อธิบาย defense-in-depth: ไม่มีมาตรการเดียวพอ ต้องรวม authentication, authorization, encryption, logging, backup และ patching",
      "NIST SP 800-207 ช่วยให้สอน Zero Trust เป็นสถาปัตยกรรม ไม่ใช่ผลิตภัณฑ์: ทุก request ต้องประเมินความเสี่ยงตาม policy ก่อนให้เข้าถึง resource",
    ],
    activity: "ให้ผู้เรียนทำ threat model ของ IoT dashboard ในโครงงาน แล้วกำหนด control อย่างน้อย 5 รายการ",
    check: ["CIA triad แต่ละข้อมีตัวอย่างอะไร?", "Zero Trust ต่างจาก perimeter security อย่างไร?", "OWASP Top 10 ช่วยนักพัฒนาอย่างไร?"],
    sources: ["zta", "owasp"],
  },
  {
    n: 13,
    title: "จริยธรรมทางคอมพิวเตอร์และทรัพย์สินทางปัญญา",
    source: "Week 13 - Computer Ethics & Intellectual Property",
    question: "วิศวกรคอมพิวเตอร์ควรตัดสินใจอย่างไรเมื่อเทคโนโลยีกระทบสิทธิ ความเป็นส่วนตัว และสังคม?",
    goals: ["ใช้กรอบจริยธรรมในการวิเคราะห์กรณีศึกษา", "เข้าใจ privacy, bias, accountability และ transparency", "รู้จัก PDPA, copyright, license และ open source"],
    ideas: [
      "จริยธรรมคอมพิวเตอร์ไม่ได้ถามแค่ว่าทำได้ไหม แต่ถามว่าควรทำไหม ใครได้ประโยชน์ ใครรับความเสี่ยง และใครรับผิดชอบ",
      "ACM Code of Ethics ให้กรอบเรื่อง public good, avoiding harm, honesty, privacy และ professional responsibility",
      "PDPA กำหนดหลักการคุ้มครองข้อมูลส่วนบุคคล รวมถึงบทบาท data controller และ data processor",
    ],
    lesson: [
      "ให้เริ่มจากกรณี AI ตรวจจับใบหน้าในห้องเรียน แล้วถามเรื่อง consent, purpose limitation, data retention, bias และทางเลือกที่ intrusive น้อยกว่า",
      "อธิบายทรัพย์สินทางปัญญาผ่านงานนักศึกษา: source code, dataset, model weight, prompt, image และ report มีสิทธิและ license ต่างกัน",
      "โยง open source: การใช้ library ไม่ได้แปลว่าทำอะไรก็ได้ ต้องอ่าน license และให้ attribution ตามเงื่อนไข",
    ],
    activity: "อภิปรายกรณีศึกษา generative AI ใช้สร้างงานส่งรายวิชา แล้วให้ผู้เรียนเขียน policy การใช้ AI ที่ยุติธรรมและตรวจสอบได้",
    check: ["public good ใน ACM Code ใช้ตัดสินใจอย่างไร?", "ข้อมูลส่วนบุคคลตาม PDPA คืออะไร?", "open source license สำคัญต่อโครงงานอย่างไร?"],
    sources: ["acmEthics", "pdpa", "nistAi"],
  },
  {
    n: 14,
    title: "โครงงานประยุกต์และวิศวกรรมระบบ",
    source: "Week 14 - Applied System Engineering & DevOps",
    question: "จะนำความรู้ทั้งรายวิชามาประกอบเป็นระบบที่สร้าง ทดสอบ และส่งมอบได้อย่างไร?",
    goals: ["เข้าใจ SDLC, Agile, DevOps และ CI/CD", "ออกแบบ architecture ของ capstone project", "เชื่อม version control, testing, deployment และ monitoring"],
    ideas: [
      "SDLC ทำให้การพัฒนาระบบมีขั้นตอนตั้งแต่ requirement ถึง maintenance",
      "DevOps ลดช่องว่างระหว่างการพัฒนาและการปฏิบัติการด้วย automation, feedback และ ownership ร่วม",
      "CI/CD ทำให้ build-test-deploy ทำซ้ำได้และลดความเสี่ยงจากการส่งงานแบบ manual",
    ],
    lesson: [
      "ให้ผู้เรียนแตกโครงงานเป็น requirement, architecture, backlog, task และ acceptance criteria เพื่อเปลี่ยนไอเดียเป็นแผนงาน",
      "สอน Git workflow ขั้นต่ำ: issue/task, branch, commit, pull request/review และ release tag เพื่อให้ทีมทำงานร่วมกันได้",
      "เชื่อม cloud-native: container ทำให้ส่งมอบ environment ได้ชัด ส่วน pipeline ช่วยให้ทุก commit ผ่าน test ก่อน deploy",
    ],
    activity: "สร้าง CI/CD pipeline เบื้องต้นที่รัน lint/test และ deploy demo หรือ build artifact ของโครงงาน",
    check: ["Agile ต่างจาก waterfall อย่างไร?", "CI กับ CD ต่างกันอย่างไร?", "acceptance criteria ช่วยลดปัญหาอะไรในทีม?"],
    sources: ["docker", "kubernetes", "cncf"],
  },
  {
    n: 15,
    title: "การดูงานเชิงวิชาการและอุตสาหกรรม",
    source: "Week 15 - Academic Visits & Computer Industry Tour",
    question: "เมื่อเห็นระบบจริงในอุตสาหกรรม เราควรสังเกตอะไรให้เชื่อมกับความรู้รายวิชา?",
    goals: ["เตรียมคำถามและกรอบสังเกตสำหรับ site visit", "เชื่อมเทคโนโลยีจริงกับหัวข้อรายสัปดาห์", "ฝึกเขียนรายงานเชิงวิชาชีพและคำนึงถึงข้อมูลลับ/PDPA"],
    ideas: [
      "การดูงานไม่ใช่การไปเยี่ยมชมอย่างเดียว แต่เป็นการเก็บหลักฐานการเรียนรู้จากระบบจริง",
      "ผู้เรียนควรสังเกต technology stack, workflow, role ของคน, security, reliability และ sustainability",
      "การถ่ายภาพหรือบันทึกข้อมูลต้องเคารพกฎองค์กร ความลับ และข้อมูลส่วนบุคคล",
    ],
    lesson: [
      "ก่อนดูงาน ให้ผู้เรียนเตรียม checklist ตาม 6 มุม: hardware, software, data, network, security, people/process",
      "ระหว่างดูงาน ให้จดสิ่งที่เห็นเป็น evidence ไม่ใช่ความรู้สึก เช่นเห็น rack, dashboard, access control, ticket workflow หรือ pipeline",
      "หลังดูงาน ให้เขียน reflection เชื่อมอย่างน้อย 3 สัปดาห์ของรายวิชา เช่น data center กับ PUE, IoT กับ MQTT, security กับ Zero Trust",
    ],
    activity: "ทำ field-note template และซ้อมตั้งคำถามกับวิทยากร 5 ข้อ โดยหลีกเลี่ยงคำถามที่ละเมิดข้อมูลลับ",
    check: ["หลักฐานจากการดูงานควรมีลักษณะอย่างไร?", "จะเชื่อมสิ่งที่เห็นกับ CLO ได้อย่างไร?", "ทำไม PDPA/CIA สำคัญระหว่าง site visit?"],
    sources: ["acmEthics", "pdpa", "pue"],
  },
  {
    n: 16,
    title: "นำเสนอโครงงานประยุกต์",
    source: "Week 16 - Final Project Presentation",
    question: "การนำเสนอที่ดีแสดงทั้งระบบ ผลลัพธ์ และการเรียนรู้ของทีมอย่างไร?",
    goals: ["เตรียมสไลด์และ demo ที่ตอบโจทย์ rubric", "สื่อสาร architecture, implementation, test และ limitation", "ฝึกตอบคำถามเชิงเทคนิคและเชิงจริยธรรม"],
    ideas: [
      "การนำเสนอ project ไม่ใช่เล่าเฉพาะฟีเจอร์ แต่ต้องอธิบายปัญหา วิธีออกแบบ หลักฐานการทำงาน และ trade-off",
      "demo ที่ดีต้องมี fallback เช่น screenshot/video/log หากระบบสดมีปัญหา",
      "ทีมควรแบ่งบทบาทการพูดให้สะท้อนการทำงานจริงและพร้อมตอบคำถามทุกคน",
    ],
    lesson: [
      "โครงเรื่องสไลด์ควรเรียง: problem → users → architecture → key implementation → demo → testing/result → limitation → next step",
      "ให้ผู้เรียนเตรียม architecture diagram ที่แสดง hardware/software/data/network/security ในภาพเดียว เพื่อเชื่อมกลับรายวิชา",
      "ฝึก Q&A ด้วยคำถาม rubric: ทำไมเลือกเทคโนโลยีนี้, ความเสี่ยงคืออะไร, ข้อมูลมาจากไหน, ถ้าขยายระบบต้องเปลี่ยนอะไร",
    ],
    activity: "จัด rehearsal แบบจับเวลา 7-10 นาที พร้อม peer feedback ตาม rubric และรายการแก้ไขก่อนนำเสนอจริง",
    check: ["สไลด์ใดพิสูจน์ว่า project ทำงานจริง?", "limitation ควรพูดอย่างไรให้เป็นมืออาชีพ?", "ทีมควรตอบคำถามที่ไม่รู้คำตอบอย่างไร?"],
    sources: ["ce2016", "acmEthics"],
  },
  {
    n: 17,
    title: "ทบทวนและสอบปลายภาค",
    source: "Week 17 - Final Examination",
    question: "ผู้เรียนสามารถอธิบายระบบคอมพิวเตอร์สมัยใหม่ตั้งแต่ AI, IoT, security ถึงจริยธรรมได้ครบวงจรหรือไม่?",
    goals: ["ทบทวนหลังกลางภาคและภาพรวมทั้งรายวิชา", "ฝึกวิเคราะห์กรณีศึกษา AI/IoT/security/ethics", "เตรียมสอบปลายภาคตาม CLO1, CLO2, CLO4, CLO5"],
    ideas: [
      "ครึ่งหลังของรายวิชาเน้นระบบอัจฉริยะ: AI/ML, GenAI, IoT, cybersecurity, ethics และ DevOps",
      "ข้อสอบปลายภาคมักเชื่อมหลายมิติ เช่นระบบ IoT ใช้ AI ต้องมี database, network, security และ PDPA",
      "คำตอบที่ดีควรมีทั้งหลักการ ตัวอย่าง และการประเมิน trade-off",
    ],
    lesson: [
      "ให้ผู้เรียนทำ case study เดียว เช่น smart classroom แล้ววิเคราะห์ครบ: sensor, MQTT, database, model, dashboard, Zero Trust, PDPA และ ethics",
      "ทบทวนคำศัพท์ด้วยการจับคู่: RAG-vector database, MQTT-IoT, Zero Trust-identity, PUE-data center, CI/CD-DevOps",
      "เตรียมสอบด้วยคำถามอัตนัยสั้น: อธิบาย trade-off และเสนอ mitigation มากกว่าท่องนิยาม",
    ],
    activity: "จัด mock exam แบบกรณีศึกษา 1 หน้า แล้วให้ผู้เรียนตอบเป็น architecture + risk + mitigation ภายในเวลาจำกัด",
    check: ["AI/IoT/security/ethics เชื่อมกันในระบบเดียวอย่างไร?", "กรณีศึกษาแบบใดต้องคิดถึง PDPA?", "คำตอบเชิงวิศวกรรมควรมี trade-off อะไรบ้าง?"],
    sources: ["nistAi", "zta", "mqtt", "pdpa"],
  },
];

function wikilink(week) {
  return `[[${week.source}]]`;
}

function sourceList(keys) {
  return keys
    .map((key) => {
      const [label, url] = commonSources[key];
      return `- [${label}](${url})`;
    })
    .join("\n");
}

function page(week) {
  const id = String(week.n).padStart(2, "0");
  return `---\ntype: learning\nstatus: complete\nweek: ${week.n}\nsource_week: "${week.source}"\ntags: [learning, week${id}, en-001-019]\ncreated: "2026-08-03"\nupdated: "2026-08-03"\n---\n\n# Learning Content Week ${id}: ${week.title}\n\n> ใช้คู่กับ ${wikilink(week)} สำหรับอ่านก่อนเรียน ทบทวนหลังเรียน และเตรียมกิจกรรมปฏิบัติการ\n\n## คำถามนำ\n${week.question}\n\n## ผลลัพธ์การเรียนรู้ย่อย\n${week.goals.map((x, i) => `${i + 1}. ${x}`).join("\n")}\n\n## แก่นความรู้ที่ต้องเข้าใจ\n${week.ideas.map((x) => `- ${x}`).join("\n")}\n\n## เนื้อหาเรียนรู้\n${week.lesson.map((x) => `- ${x}`).join("\n")}\n\n## กิจกรรมในชั้นเรียน / ปฏิบัติการ\n${week.activity}\n\n## คำถามตรวจความเข้าใจ\n${week.check.map((x, i) => `${i + 1}. ${x}`).join("\n")}\n\n## ชิ้นงาน / หลักฐานการเรียนรู้\n- สรุปแนวคิด 1 หน้า หรือ concept map ของสัปดาห์นี้\n- ผลกิจกรรม/โค้ด/diagram ตามโจทย์ประจำสัปดาห์\n- คำตอบสะท้อนคิด: วันนี้เข้าใจอะไรเพิ่ม และยังสงสัยอะไร\n\n## แหล่งค้นคว้าเพิ่มเติม\n${sourceList(week.sources)}\n\n> กลับ [[Learning Content Index]] · ดูแผนสัปดาห์ที่ ${week.n}: ${wikilink(week)}\n`;
}

function indexPage() {
  return `---\ntype: meta\ntitle: "Learning Content Index"\naliases: ["Learning Content Index"]\nupdated: "2026-08-03"\n---\n\n# Learning Content Index — เนื้อหาเรียนรู้รายสัปดาห์\n\nชุดเนื้อหาอ่านประกอบรายวิชา **EN-001-019 แก่นวิศวกรรมคอมพิวเตอร์** สร้างจากแผนสอนใน [[Timeline & Curriculum Map]] และเติมแหล่งอ้างอิงค้นคว้าจากเอกสารมาตรฐาน/เอกสารทางการ\n\n${weeks.map((week) => `- [[Learning Content Week ${String(week.n).padStart(2, "0")} - ${week.title}]] — คู่กับ [[${week.source}]]`).join("\n")}\n\n## แหล่งอ้างอิงหลักที่ใช้ทั้งชุด\n${Object.values(commonSources).map(([label, url]) => `- [${label}](${url})`).join("\n")}\n\n> กลับ [[index]]\n`;
}

async function main() {
  await fs.mkdir(outDir, { recursive: true });
  for (const week of weeks) {
    const id = String(week.n).padStart(2, "0");
    const file = `Learning Content Week ${id} - ${week.title}.md`;
    await fs.writeFile(path.join(outDir, file), page(week), "utf8");
  }
  await fs.writeFile(path.join(outDir, "_index.md"), indexPage(), "utf8");
  console.log(`Created ${weeks.length} learning pages in ${path.relative(root, outDir)}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
