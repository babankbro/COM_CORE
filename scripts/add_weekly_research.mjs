import fs from "node:fs/promises";
import path from "node:path";

const root = process.env.PROJECT_ROOT ? path.resolve(process.env.PROJECT_ROOT) : process.cwd();
const learningDir = path.join(root, "wiki", "learning");

const researchByWeek = {
  "01": {
    title: "ขอบเขตสาขาและมาตรฐานหลักสูตร",
    bullets: [
      "ACM/IEEE CE2016 ใช้เป็นฐานอธิบายว่า Computer Engineering ต้องบูรณาการ hardware, software, embedded systems, networks และ security ไม่ใช่เรียนเขียนโปรแกรมอย่างเดียว",
      "ACM/IEEE-CS/AAAI CS2023 ช่วยเสริมภาพรวมว่าสาขาคอมพิวเตอร์ยุคใหม่ให้ความสำคัญกับ AI, security, data และ professional practice มากขึ้น",
      "ใช้สอนโดยให้ผู้เรียนเทียบบทบาทงานจริงของ CE/CS/SE/IT/IS กับ knowledge area ในมาตรฐาน เพื่อเห็นเส้นทางอาชีพ",
    ],
    refs: [
      ["ACM/IEEE Computer Engineering Curricula 2016", "https://www.acm.org/binaries/content/assets/education/ce2016-final-report.pdf"],
      ["ACM Curricula Recommendations", "https://www.acm.org/education/curricula-recommendations"],
      ["ACM/IEEE-CS/AAAI Computer Science Curricula 2023", "https://dl.acm.org/doi/book/10.1145/3664191"],
    ],
  },
  "02": {
    title: "Hardware/software ecosystem, edge และพลังงาน",
    bullets: [
      "ระบบสมัยใหม่มี heterogeneous computing: CPU ทำงานทั่วไป, GPU/NPU เร่งงานขนานและ AI inference ทำให้ผู้เรียนต้องอ่านสเปกเครื่องมากกว่าแค่ความเร็ว CPU",
      "Edge computing ลด latency และลดการส่งข้อมูลขึ้น cloud แต่เพิ่มโจทย์ด้าน update, security, observability และพลังงานของอุปกรณ์ปลายทาง",
      "Green computing ควรเชื่อมกับการเลือก hardware, power profile, sleep mode และการออกแบบ workload ไม่ใช่พูดเฉพาะการประหยัดไฟทั่วไป",
    ],
    refs: [
      ["ACM/IEEE Computer Engineering Curricula 2016", "https://www.acm.org/binaries/content/assets/education/ce2016-final-report.pdf"],
      ["NIST Edge Computing definition and reference architecture", "https://www.nist.gov/publications/fog-computing-conceptual-model"],
      ["The Green Grid", "https://www.thegreengrid.org/home"],
    ],
  },
  "03": {
    title: "Digital logic, processor architecture และ RISC-V",
    bullets: [
      "RISC-V เป็น open standard ISA ที่ดีสำหรับการสอน เพราะแยกชัดเจนระหว่าง instruction set กับ implementation ของ processor",
      "แนวโน้ม chiplet และ accelerator ทำให้บทเรียน CPU/GPU/NPU ควรเน้น trade-off: งานทั่วไป งานขนาน งาน AI และข้อจำกัดด้านพลังงาน/ความร้อน",
      "กิจกรรมควรพาผู้เรียนจาก truth table ไปสู่ adder/register แล้วเชื่อมกับ fetch-decode-execute เพื่อไม่ให้วงจรตรรกะดูแยกจาก processor จริง",
    ],
    refs: [
      ["RISC-V International", "https://riscv.org/"],
      ["RISC-V Specifications", "https://riscv.org/technical/specifications/"],
      ["The RISC-V Instruction Set Manual", "https://github.com/riscv/riscv-isa-manual"],
    ],
  },
  "04": {
    title: "Algorithms, programming และ AI coding assistants",
    bullets: [
      "CS2023 วาง software development fundamentals และ algorithmic foundations เป็น competency หลัก ซึ่งใช้ยืนยันว่า AI assistant ไม่ได้แทนความเข้าใจอัลกอริทึม",
      "ผู้เรียนควรฝึกอ่าน code ที่ AI สร้างด้วย test case และ complexity analysis เพราะความถูกต้องของ syntax ไม่เท่ากับความถูกต้องของ algorithm",
      "จริยธรรมการใช้ AI ในงานเขียนโค้ดควรผูกกับ attribution, academic integrity, privacy ของ code/data และความรับผิดชอบต่อ bug",
    ],
    refs: [
      ["ACM/IEEE-CS/AAAI Computer Science Curricula 2023", "https://dl.acm.org/doi/book/10.1145/3664191"],
      ["ACM Code of Ethics and Professional Conduct", "https://www.acm.org/code-of-ethics"],
      ["GitHub Copilot documentation", "https://docs.github.com/en/copilot"],
    ],
  },
  "05": {
    title: "Database, vector search และ AI-ready data",
    bullets: [
      "Vector database เพิ่มความสามารถ semantic search จาก embedding จึงควรสอนคู่กับ SQL/NoSQL เพื่อให้ผู้เรียนเห็นว่าข้อมูลสำหรับ AI มีทั้ง structured และ unstructured",
      "pgvector แสดงแนวทาง practical ว่า relational database อย่าง PostgreSQL สามารถเก็บ vector และทำ similarity search ร่วมกับข้อมูลตารางเดิมได้",
      "SQL Server 2025 เพิ่ม vector data type อย่างเป็นทางการ สะท้อนว่า vector กลายเป็น capability ในฐานข้อมูลหลัก ไม่ใช่เครื่องมือเฉพาะทางเท่านั้น",
    ],
    refs: [
      ["pgvector: Open-source vector similarity search for Postgres", "https://github.com/pgvector/pgvector"],
      ["Microsoft Learn: Vectors in SQL Server", "https://learn.microsoft.com/en-us/sql/sql-server/ai/vectors?view=sql-server-ver17"],
      ["Microsoft Learn: Vector data type", "https://learn.microsoft.com/en-us/sql/t-sql/data-types/vector-data-type?view=sql-server-ver17"],
    ],
  },
  "06": {
    title: "Internet standards, Wi-Fi 7 และ 5G-Advanced",
    bullets: [
      "IETF RFC 8200 เป็นแหล่งหลักสำหรับ IPv6 ใช้สอนว่ามาตรฐานอินเทอร์เน็ตเกิดจาก consensus และ interoperability",
      "IEEE 802.11be-2024 หรือ Wi-Fi 7 เพิ่มเป้าหมาย throughput สูงมากและปรับ PHY/MAC เพื่อรองรับงาน latency ต่ำ เหมาะเชื่อมกับ real-time/edge applications",
      "3GPP Release 18 เป็นจุดเริ่มของ 5G-Advanced มีแนวทางใช้ AI/ML ในเครือข่ายและเพิ่มความสามารถของ mobile network",
    ],
    refs: [
      ["IETF RFC 8200: IPv6 Specification", "https://datatracker.ietf.org/doc/html/rfc8200"],
      ["IEEE 802.11be-2024", "https://standards.ieee.org/ieee/802.11be/7516/"],
      ["3GPP Release 18 overview", "https://www.3gpp.org/specifications-technologies/releases/release-18"],
    ],
  },
  "07": {
    title: "Cloud native, containers, Kubernetes และ PUE",
    bullets: [
      "Docker อธิบาย container ว่าเป็นการ package code กับ dependencies ให้รันสม่ำเสมอในหลาย environment เหมาะใช้สอนก่อนขึ้น Kubernetes",
      "Kubernetes เป็น platform สำหรับจัดการ containerized workloads และ services แบบ declarative/automation เหมาะกับบทเรียน DevOps และ cloud infrastructure",
      "The Green Grid PUE ใช้เป็น metric มาตรฐานของ data center energy efficiency และเชื่อมกับการเพิ่มขึ้นของ AI workload ได้ดี",
    ],
    refs: [
      ["Docker Docs: What is a container?", "https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/"],
      ["Kubernetes Documentation: Concepts", "https://kubernetes.io/docs/concepts/"],
      ["The Green Grid: PUE Comprehensive Examination", "https://www.thegreengrid.org/en/resources/library-and-tools/20-PUE%3A-A-Comprehensive-Examination-of-the-Metric"],
    ],
  },
  "08": {
    title: "Midterm integration research",
    bullets: [
      "การสอบกลางภาคควรใช้โจทย์บูรณาการจากมาตรฐาน CE/CS เช่น ให้ผู้เรียนอธิบายระบบหนึ่งตั้งแต่ hardware, software, algorithm, database, network ถึง cloud",
      "ใช้ ACM/IEEE outcome language เป็นแนวทางออกข้อสอบ: explain, apply, design, evaluate ไม่ใช่ถามจำคำศัพท์อย่างเดียว",
      "ควรมีข้อสอบที่ตรวจทั้ง concept map และ problem solving เช่น ER diagram, pseudocode, subnet/TCP reasoning และ PUE calculation",
    ],
    refs: [
      ["ACM/IEEE Computer Engineering Curricula 2016", "https://www.acm.org/binaries/content/assets/education/ce2016-final-report.pdf"],
      ["ACM/IEEE-CS/AAAI Computer Science Curricula 2023", "https://dl.acm.org/doi/book/10.1145/3664191"],
      ["ACM Curricula Recommendations", "https://www.acm.org/education/curricula-recommendations"],
    ],
  },
  "09": {
    title: "AI/ML lifecycle และ AI risk",
    bullets: [
      "NIST AI RMF เสนอกรอบ Govern, Map, Measure, Manage เพื่อจัดการความเสี่ยง AI ตลอด lifecycle ไม่ใช่ดูแค่ accuracy",
      "หัวข้อ MLOps ควรเน้น data quality, model versioning, evaluation, deployment, monitoring และ feedback loop",
      "ให้ผู้เรียนเชื่อม bias, hallucination, robustness และ privacy เข้ากับขั้นตอนข้อมูล/โมเดล/การนำไปใช้จริง",
    ],
    refs: [
      ["NIST AI Risk Management Framework", "https://www.nist.gov/itl/ai-risk-management-framework"],
      ["NIST AI RMF 1.0 PDF", "https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf"],
      ["Google Cloud: MLOps architecture and lifecycle", "https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning"],
    ],
  },
  "10": {
    title: "Generative AI, RAG, agents และ governance",
    bullets: [
      "NIST Generative AI Profile เป็น companion ของ AI RMF สำหรับความเสี่ยงเฉพาะ GenAI เช่น hallucination, misuse, synthetic content และ data/IP risk",
      "RAG ควรถูกสอนเป็น system pattern ที่รวม retrieval, ranking, prompt construction และ evaluation ไม่ใช่แค่เรียก LLM",
      "Agentic AI ต้องเพิ่ม guardrails เช่น tool permission, audit log, human approval, sandboxing และ failure recovery โดยเฉพาะเมื่อเชื่อมกับ robotics",
    ],
    refs: [
      ["NIST AI RMF Generative AI Profile", "https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence"],
      ["OWASP Top 10 for Large Language Model Applications", "https://owasp.org/www-project-top-10-for-large-language-model-applications/"],
      ["pgvector documentation", "https://github.com/pgvector/pgvector"],
    ],
  },
  "11": {
    title: "Embedded systems, IoT และ MQTT",
    bullets: [
      "MQTT เป็น OASIS standard แบบ lightweight publish/subscribe เหมาะกับ IoT เพราะรองรับอุปกรณ์และเครือข่ายที่มี resource จำกัด",
      "การสอน IoT ควรแยก device, connectivity, broker/backend, storage, dashboard และ security control เพื่อให้ผู้เรียนเห็น architecture ครบ",
      "QoS, retained messages, topic design และ authentication เป็นรายละเอียดที่ช่วยยกระดับจาก demo sensor ไปสู่ระบบที่เชื่อถือได้",
    ],
    refs: [
      ["MQTT.org: The Standard for IoT Messaging", "https://mqtt.org/"],
      ["OASIS MQTT Version 5.0 Standard", "https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html"],
      ["Eclipse Mosquitto MQTT broker", "https://mosquitto.org/"],
    ],
  },
  "12": {
    title: "Zero Trust, OWASP และ secure design",
    bullets: [
      "NIST SP 800-207 อธิบาย Zero Trust เป็นสถาปัตยกรรมที่ย้ายจุดเน้นจาก network perimeter ไปที่ users, assets และ resources",
      "OWASP Top 10 เป็น awareness baseline สำหรับนักพัฒนาเว็บ และควรโยงกับ secure coding เช่น access control, injection และ cryptographic failures",
      "สำหรับระบบ AI/IoT ควรเพิ่ม OWASP LLM risks และ device security เพราะ attack surface ขยายจากเว็บไปยัง prompt, model, vector store และ sensor/device",
    ],
    refs: [
      ["NIST SP 800-207 Zero Trust Architecture", "https://csrc.nist.gov/pubs/sp/800/207/final"],
      ["OWASP Top 10 Web Application Security Risks", "https://owasp.org/www-project-top-ten/"],
      ["OWASP Top 10 for LLM Applications", "https://owasp.org/www-project-top-10-for-large-language-model-applications/"],
    ],
  },
  "13": {
    title: "Ethics, PDPA, UNESCO AI Ethics และ EU AI Act",
    bullets: [
      "ACM Code of Ethics ใช้เป็นฐานอภิปรายว่าผู้พัฒนาระบบต้องคำนึงถึง public good, avoiding harm, privacy, honesty และ professional competence",
      "PDPA ไทยนิยามข้อมูลส่วนบุคคลและบทบาท data controller/data processor ใช้เชื่อมกับกรณีเก็บภาพ เสียง sensor หรือข้อมูลนักศึกษา",
      "UNESCO AI Ethics และ EU AI Act ช่วยให้เห็นทิศทางสากลของ AI governance: human rights, transparency, fairness, human oversight และ risk-based regulation",
    ],
    refs: [
      ["ACM Code of Ethics and Professional Conduct", "https://www.acm.org/code-of-ethics"],
      ["MDES: Personal Data Protection Act B.E. 2562", "https://mdes.go.th/law/detail/3577-Personal-Data-Protection-Act-B-E--2562--2019-"],
      ["UNESCO Recommendation on the Ethics of AI", "https://www.unesco.org/en/artificial-intelligence/recommendation-ethics"],
      ["European Commission: AI Act enters into force", "https://commission.europa.eu/news-and-media/news/ai-act-enters-force-2024-08-01_en"],
    ],
  },
  "14": {
    title: "DevOps, CI/CD และ cloud-native delivery",
    bullets: [
      "DevOps ควรถูกสอนเป็น culture + automation + feedback loop ไม่ใช่แค่เครื่องมือ deploy",
      "CI/CD ควรมีขั้นตอนขั้นต่ำคือ version control, automated build, automated test, artifact, deploy และ rollback plan",
      "Cloud-native delivery เชื่อม Docker/Kubernetes/CNCF กับ observability และ security เช่น secret management, image scanning และ least privilege",
    ],
    refs: [
      ["Cloud Native Computing Foundation", "https://www.cncf.io/"],
      ["Docker Documentation", "https://docs.docker.com/"],
      ["Kubernetes Documentation", "https://kubernetes.io/docs/concepts/"],
      ["GitHub Actions Documentation", "https://docs.github.com/en/actions"],
    ],
  },
  "15": {
    title: "Industry/site visit research framework",
    bullets: [
      "การดูงานควรใช้กรอบ evidence-based observation: สังเกต system, process, people, risk และ metric ไม่ใช่บันทึกเฉพาะสิ่งที่น่าสนใจ",
      "ถ้าไปดู data center ให้ใช้ PUE, redundancy, physical security, cooling และ access control เป็นหัวข้อสังเกต",
      "ถ้าไปดู software/AI company ให้ใช้ SDLC, DevOps, data governance, AI risk และ code review เป็นหัวข้อสังเกต พร้อมระวังข้อมูลลับและ PDPA",
    ],
    refs: [
      ["ACM Code of Ethics and Professional Conduct", "https://www.acm.org/code-of-ethics"],
      ["The Green Grid: PUE Comprehensive Examination", "https://www.thegreengrid.org/en/resources/library-and-tools/20-PUE%3A-A-Comprehensive-Examination-of-the-Metric"],
      ["NIST AI Risk Management Framework", "https://www.nist.gov/itl/ai-risk-management-framework"],
    ],
  },
  "16": {
    title: "Project presentation evidence and assessment",
    bullets: [
      "การนำเสนอโครงงานควรมีหลักฐาน 4 แบบ: requirement evidence, architecture evidence, implementation evidence และ evaluation evidence",
      "ให้ผู้เรียนอธิบาย trade-off เช่น performance vs cost, accuracy vs privacy, cloud vs edge, manual deployment vs CI/CD",
      "ควรประเมินทั้งผลลัพธ์และกระบวนการทีม: version history, issue tracking, test result, demo reliability และการตอบคำถาม",
    ],
    refs: [
      ["ACM/IEEE Computer Engineering Curricula 2016", "https://www.acm.org/binaries/content/assets/education/ce2016-final-report.pdf"],
      ["ACM Code of Ethics and Professional Conduct", "https://www.acm.org/code-of-ethics"],
      ["GitHub Docs: About issues", "https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues"],
    ],
  },
  "17": {
    title: "Final integration research",
    bullets: [
      "ข้อสอบปลายภาคควรวัดการบูรณาการ AI, IoT, security, cloud และ ethics ผ่าน case study มากกว่าการจำคำจำกัดความ",
      "ใช้ NIST AI RMF, NIST Zero Trust, MQTT และ PDPA เป็นแกนสร้างโจทย์ smart system เช่น smart classroom หรือ AI-enabled IoT dashboard",
      "คำตอบที่ดีควรมี architecture, data flow, risk analysis, mitigation และ ethical/legal consideration",
    ],
    refs: [
      ["NIST AI Risk Management Framework", "https://www.nist.gov/itl/ai-risk-management-framework"],
      ["NIST SP 800-207 Zero Trust Architecture", "https://csrc.nist.gov/pubs/sp/800/207/final"],
      ["MQTT.org", "https://mqtt.org/"],
      ["MDES: Personal Data Protection Act B.E. 2562", "https://mdes.go.th/law/detail/3577-Personal-Data-Protection-Act-B-E--2562--2019-"],
    ],
  },
};

function sectionText(entry) {
  return `## Research เพิ่มเติมและแหล่งอ้างอิง\n**หัวข้อวิจัยเสริม:** ${entry.title}\n\n${entry.bullets.map((x) => `- ${x}`).join("\n")}\n\n**แหล่งอ้างอิงข้อมูล:**\n${entry.refs.map(([label, url]) => `- [${label}](${url})`).join("\n")}\n\n`;
}

async function main() {
  for (const [week, entry] of Object.entries(researchByWeek)) {
    const files = await fs.readdir(learningDir);
    const file = files.find((name) => name.startsWith(`Learning Content Week ${week} - `));
    if (!file) throw new Error(`Missing learning file for week ${week}`);
    const filePath = path.join(learningDir, file);
    let text = await fs.readFile(filePath, "utf8");
    text = text.replace(/\n## Research เพิ่มเติมและแหล่งอ้างอิง\n[\s\S]*?(?=\n## แหล่งค้นคว้าเพิ่มเติม\n)/, "\n");
    text = text.replace("\n## แหล่งค้นคว้าเพิ่มเติม\n", `\n${sectionText(entry)}## แหล่งค้นคว้าเพิ่มเติม\n`);
    await fs.writeFile(filePath, text, "utf8");
  }
  console.log("Updated weekly research sections.");
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
