// ตรวจความครบถ้วนของเนื้อหาใน content/ (รัน: npm run check)
import { readFile, stat } from "fs/promises";
import path from "path";
import { fileURLToPath } from "url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const CONTENT = path.join(ROOT, "content");
const WEEKS = Array.from({ length: 17 }, (_, i) => String(i + 1).padStart(2, "0"));
const EXAM_WEEKS = WEEKS.filter((w) => !["08", "16", "17"].includes(w));
const LAB_WEEKS = WEEKS.filter((w) => !["08", "16", "17"].includes(w));

let errors = 0;
const fail = (msg) => { console.error("✗ " + msg); errors++; };
const ok = (msg) => console.log("✓ " + msg);
const exists = async (p) => { try { await stat(p); return true; } catch { return false; } };

for (const w of WEEKS) {
  const p = path.join(CONTENT, "modules", `module-${w}.md`);
  if (!(await exists(p))) fail(`module-${w}.md หายไป`);
  else if ((await readFile(p, "utf-8")).length < 500) fail(`module-${w}.md สั้นผิดปกติ`);
}
ok("modules");

for (const w of LAB_WEEKS) {
  if (!(await exists(path.join(CONTENT, "labs", `lab-${w}.md`)))) fail(`lab-${w}.md หายไป`);
}
ok("labs");

for (const w of EXAM_WEEKS) {
  const p = path.join(CONTENT, "exams", `exam-${w}.json`);
  if (!(await exists(p))) { fail(`exam-${w}.json หายไป`); continue; }
  const exam = JSON.parse(await readFile(p, "utf-8"));
  if (exam.moduleId !== w) fail(`exam-${w}.json: moduleId ไม่ตรง`);
  if (!Array.isArray(exam.questions) || exam.questions.length < 5) fail(`exam-${w}.json: คำถามน้อยกว่า 5 ข้อ`);
  exam.questions?.forEach((q, i) => {
    if (q.id !== i + 1) fail(`exam-${w}.json: ข้อ ${i + 1} id ไม่เรียงลำดับ`);
    if (!q.choices?.some((c) => c.key === q.answer)) fail(`exam-${w}.json: ข้อ ${q.id} เฉลยไม่ตรงกับตัวเลือก`);
    if (!q.explanation) fail(`exam-${w}.json: ข้อ ${q.id} ไม่มีคำอธิบาย`);
  });
}
ok("exams");

const manifest = JSON.parse(await readFile(path.join(CONTENT, "manifest.json"), "utf-8"));
for (const [w, topics] of Object.entries(manifest.topics)) {
  for (const t of topics) {
    if (!(await exists(path.join(CONTENT, "topics", w, `${t.n}.md`)))) fail(`topics/${w}/${t.n}.md หายไป`);
  }
}
for (const c of manifest.concepts) if (!(await exists(path.join(CONTENT, "concepts", `${c.slug}.md`)))) fail(`concepts/${c.slug}.md หายไป`);
for (const d of manifest.docs) if (!(await exists(path.join(CONTENT, "docs", `${d.slug}.md`)))) fail(`docs/${d.slug}.md หายไป`);
ok("manifest");

if (errors) { console.error(`\nพบปัญหา ${errors} รายการ`); process.exit(1); }
console.log("\nเนื้อหาครบถ้วน");
