# สื่อการสอนรายวิชาแก่นวิศวกรรมคอมพิวเตอร์

> EN-001-019 Computer Engineering Essentials — Next.js e-Learning Site

เว็บไซต์สื่อการสอนออนไลน์ของรายวิชา EN-001-019 แก่นวิศวกรรมคอมพิวเตอร์ 3(2-2-5) ครบ 17 สัปดาห์
พร้อมเนื้อหาเชิงลึกรายหัวข้อ ใบงาน 4 Mini-Projects สไลด์ PowerPoint และแบบทดสอบออนไลน์พร้อมเฉลย
เนื้อหา **สร้างอัตโนมัติ** จากคลังความรู้ Obsidian ใน `../wiki/` และ `../slides/` ด้วย `npm run content`

## บทเรียน

| W | ชื่อสัปดาห์ | CLO | Mini-Project | Lab | Quiz |
|---|---|---|---|---|---|
| 01 | ภาพรวมวิศวกรรมคอมพิวเตอร์และระบบสารสนเทศในยุค AI | CLO1, CLO4 | 1 | ✓ | ✓ |
| 02 | ฮาร์ดแวร์ ซอฟต์แวร์ และระบบนิเวศสมัยใหม่ | CLO1 | 1 | ✓ | ✓ |
| 03 | วงจรตรรกะและหน่วยประมวลผล | CLO2 | 1 | ✓ | ✓ |
| 04 | อัลกอริทึมและการเขียนโปรแกรม | CLO3 | 1 | ✓ | ✓ |
| 05 | ฐานข้อมูลและการจัดการข้อมูลขนาดใหญ่ | CLO3 | 2 | ✓ | ✓ |
| 06 | เครือข่ายคอมพิวเตอร์และอินเทอร์เน็ต | CLO1 | 2 | ✓ | ✓ |
| 07 | ศูนย์ข้อมูลและโครงสร้างพื้นฐานระดับคลาวด์ | CLO2, CLO4 | 2 | ✓ | ✓ |
| 08 | ทบทวนและสอบกลางภาค | CLO1–3 | – | – | – |
| 09 | ปัญญาประดิษฐ์และการเรียนรู้ของเครื่อง | CLO1 | 3 | ✓ | ✓ |
| 10 | Generative AI และวิทยาการหุ่นยนต์ | CLO1, CLO4 | 3 | ✓ | ✓ |
| 11 | ระบบฝังตัวและอินเทอร์เน็ตของสรรพสิ่ง | CLO2, CLO4 | 3 | ✓ | ✓ |
| 12 | ความปลอดภัยไซเบอร์และสถาปัตยกรรม Zero Trust | CLO1, CLO4 | 3 | ✓ | ✓ |
| 13 | จริยธรรมทางคอมพิวเตอร์และทรัพย์สินทางปัญญา | CLO5 | 4 | ✓ | ✓ |
| 14 | โครงงานประยุกต์และวิศวกรรมระบบ DevOps | CLO3, CLO6 | 4 | ✓ | ✓ |
| 15 | การดูงานเชิงวิชาการและอุตสาหกรรมคอมพิวเตอร์ | CLO4, CLO6 | 4 | ✓ | ✓ |
| 16 | นำเสนอโครงงานประยุกต์ | CLO3, CLO6 | – | – | – |
| 17 | ทบทวนและสอบปลายภาค | CLO1,2,4,5 | – | – | – |

## วิธีใช้งาน

```bash
npm install
npm run content      # สร้าง content/ จาก ../wiki และ ../slides (ข้ามอัตโนมัติถ้าไม่มี ../wiki)
npm run check        # ตรวจความครบถ้วนของเนื้อหาและแบบทดสอบ
npm run dev          # เปิด http://localhost:3000
npm run build        # build สำหรับ production (รัน content ให้อัตโนมัติ)
npm start
```

## โครงสร้างโปรเจกต์

```
web/
├── app/
│   ├── layout.tsx                  ← Root layout (ฟอนต์ Prompt, KaTeX, AppShell)
│   ├── page.tsx                    ← หน้าหลัก (ภาพรวมรายวิชา + 4 Mini-Projects + CLO)
│   ├── module/[id]/page.tsx        ← เนื้อหารายสัปดาห์ + แผนการสอน + สไลด์ + Deep Dive
│   ├── module/[id]/[topic]/        ← เนื้อหาเชิงลึก (Deep Dive) รายหัวข้อ
│   ├── lab/[id]/page.tsx           ← ใบงานปฏิบัติการ
│   ├── exam/[id]/page.tsx          ← แบบทดสอบออนไลน์ (จับเวลา ตรวจ เฉลย พิมพ์ผล)
│   ├── slides/page.tsx             ← รวมสไลด์ทุกสัปดาห์
│   ├── concepts/ + concept/[slug]/ ← พจนานุกรมศัพท์
│   ├── docs/[slug]/page.tsx        ← เอกสารรายวิชา (CLO, การประเมิน, ธีม)
│   └── api/content/[...path]/      ← ให้บริการไฟล์ใน content/ (pptx ฯลฯ)
├── components/                     ← Header (ค้นหา Ctrl+K), Sidebar, MarkdownContent, Mermaid, ExamClient
├── lib/
│   ├── course.ts                   ← ข้อมูลรายวิชาและ CLO
│   ├── modules-data.ts             ← ข้อมูล 17 สัปดาห์ (ชื่อ, CLO, Mini-Project, ไอคอน, สี)
│   ├── manifest.ts                 ← ดัชนีเนื้อหา (client-safe)
│   └── content.ts                  ← อ่าน markdown / exam JSON (server)
├── content/                        ← สร้างโดย scripts/build-content.mjs (ยกเว้น exams/)
│   ├── modules/module-XX.md        ← เนื้อหาเรียนรู้ + แผนการสอนรายสัปดาห์
│   ├── topics/XX/NN.md             ← เนื้อหาเชิงลึก
│   ├── labs/lab-XX.md              ← ใบงาน
│   ├── concepts/<slug>.md          ← ศัพท์
│   ├── docs/<slug>.md              ← เอกสารรายวิชา/ธีม
│   ├── slides/week-XX.pptx         ← สไลด์
│   ├── exams/exam-XX.json          ← แบบทดสอบ 10 ข้อ/สัปดาห์ (เขียนเอง ไม่ถูก generate ทับ)
│   └── manifest.json               ← ดัชนีทั้งหมด
├── public/images/slides/           ← ภาพ preview สไลด์
└── scripts/
    ├── build-content.mjs           ← แปลง wiki (wikilink → ลิงก์เว็บ, callout, frontmatter)
    └── check-content.mjs           ← ตรวจความครบถ้วน
```

## การแก้ไขเนื้อหา

- **เนื้อหาเรียน/ใบงาน/ศัพท์:** แก้ไขใน `../wiki/` (Obsidian) แล้วรัน `npm run content`
  - สัปดาห์ 1–5 ใช้ `wiki/learning/Week XX/00_Overview*.md` · สัปดาห์ 6–17 ใช้ `wiki/learning/Learning Content Week XX*.md`
  - แผนการสอนต่อท้ายจาก `wiki/timeline/Week XX - *.md`
  - หัวข้อ Deep Dive ที่ยังมีคำว่า "ฉบับร่าง" จะถูกข้ามอัตโนมัติ
- **แบบทดสอบ:** แก้ไข `content/exams/exam-XX.json` โดยตรง (รูปแบบเดียวกับ EN-012-314)
- **ข้อมูลสัปดาห์ (ชื่อ, CLO, ไอคอน):** `lib/modules-data.ts`

## ฟีเจอร์

- **Docs-style Layout** — Sidebar + Content แบบเดียวกับเว็บรายวิชา EN-012-314
- **Markdown + KaTeX + Mermaid + Callout** (`> [!abstract]`, `[!note]`, `[!tip]`, `[!warning]`)
- **Wikilink → ลิงก์เว็บ** — `[[Week 07 - ...]]`, `[[PUE]]`, `[[Lab 05 - ...]]` กลายเป็นลิงก์ภายในอัตโนมัติ
- **แบบทดสอบออนไลน์** — จับเวลา ตรวจอัตโนมัติ เฉลยพร้อมคำอธิบาย พิมพ์ผลได้ (เกณฑ์ผ่าน 50%)
- **สไลด์** — ดาวน์โหลด .pptx + ภาพ preview ทุกสัปดาห์
- **Dark / Light Mode**, **ค้นหา (Ctrl+K)** ครอบคลุมบทเรียน หัวข้อ ใบงาน ศัพท์, **Responsive**

## เทคโนโลยี

Next.js 14 (App Router) · TailwindCSS · react-markdown + remark-gfm + remark-math + rehype-katex · Mermaid · Lucide React
