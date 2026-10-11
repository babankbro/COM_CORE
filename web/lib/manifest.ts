// ชนิดข้อมูลและดัชนีเนื้อหา (client-safe: ไม่ใช้ fs) — manifest.json ถูกสร้างโดย scripts/build-content.mjs
import manifestJson from "@/content/manifest.json";

export interface ExamChoice {
  key: string;
  text: string;
}

export interface ExamQuestion {
  id: number;
  question: string;
  code?: string;
  choices: ExamChoice[];
  answer: string;
  explanation: string;
}

export interface ExamData {
  moduleId: string;
  title: string;
  titleTh: string;
  timeMinutes: number;
  questions: ExamQuestion[];
}

export interface TopicInfo {
  n: string;
  title: string;
  file: string;
}

export interface LabInfo {
  id: string;
  title: string;
  module: string;
}

export interface ConceptInfo {
  slug: string;
  name: string;
  title: string;
  definition: string;
  weeks: string[];
}

export interface DocInfo {
  slug: string;
  title: string;
  group: "course" | "theme";
}

export interface SlideInfo {
  pptx: string | null;
  preview: string | null;
  title: string;
}

export interface Manifest {
  generated: string;
  modules: Record<string, { timelineTitle: string }>;
  topics: Record<string, TopicInfo[]>;
  labs: LabInfo[];
  concepts: ConceptInfo[];
  docs: DocInfo[];
  slides: Record<string, SlideInfo>;
}

export const manifest = manifestJson as unknown as Manifest;
