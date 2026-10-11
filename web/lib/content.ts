import { readFile } from "fs/promises";
import path from "path";
import { manifest } from "./manifest";
import type { ExamData, TopicInfo, LabInfo, ConceptInfo, DocInfo, SlideInfo } from "./manifest";

export * from "./manifest";

const CONTENT_DIR = path.join(process.cwd(), "content");

async function readMarkdown(subdir: string, filename: string, fallback: string) {
  try {
    return await readFile(path.join(CONTENT_DIR, subdir, filename), "utf-8");
  } catch {
    return fallback;
  }
}

export function getModuleContent(id: string) {
  return readMarkdown("modules", `module-${id}.md`, `# ไม่พบเนื้อหาสัปดาห์ที่ ${id}`);
}

export function getTopicContent(id: string, n: string) {
  return readMarkdown(path.join("topics", id), `${n}.md`, `# ไม่พบเนื้อหาหัวข้อ ${id}/${n}`);
}

export function getTopics(id: string): TopicInfo[] {
  return manifest.topics[id] ?? [];
}

export function getTopic(id: string, n: string): TopicInfo | undefined {
  return getTopics(id).find((t) => t.n === n);
}

export function getLabContent(id: string) {
  return readMarkdown("labs", `lab-${id}.md`, `# ไม่พบใบงานที่ ${id}`);
}

export function getLab(id: string): LabInfo | undefined {
  return manifest.labs.find((l) => l.id === id);
}

export async function getExam(id: string): Promise<ExamData | undefined> {
  try {
    const raw = await readFile(path.join(CONTENT_DIR, "exams", `exam-${id}.json`), "utf-8");
    return JSON.parse(raw) as ExamData;
  } catch {
    return undefined;
  }
}

export function getConcept(slug: string): ConceptInfo | undefined {
  return manifest.concepts.find((c) => c.slug === slug);
}

export function getConceptContent(slug: string) {
  return readMarkdown("concepts", `${slug}.md`, `# ไม่พบศัพท์ ${slug}`);
}

export function getDoc(slug: string): DocInfo | undefined {
  return manifest.docs.find((d) => d.slug === slug);
}

export function getDocContent(slug: string) {
  return readMarkdown("docs", `${slug}.md`, `# ไม่พบเอกสาร ${slug}`);
}

export function getSlide(id: string): SlideInfo | undefined {
  return manifest.slides[id];
}

export function getCalcExamplesContent() {
  return readMarkdown("", "calc-examples.md", "# ยังไม่มีตัวอย่างโจทย์คำนวณ");
}
