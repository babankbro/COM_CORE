import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { Presentation, PresentationFile } from "@oai/artifact-tool";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = process.env.PROJECT_ROOT ? path.resolve(process.env.PROJECT_ROOT) : path.resolve(__dirname, "..");
const timelineDir = path.join(root, "wiki", "timeline");
const outputRoot = path.join(root, "slides");
const qaRoot = path.join(outputRoot, "_qa");

const W = 1280;
const H = 720;
const C = {
  ink: "#111111",
  muted: "#555555",
  rule: "#B8BCC4",
  panel: "#EFEFEF",
  canvas: "#FFFFFF",
  accent: "#0F766E",
  accent2: "#F97316",
  softAccent: "#E6F4F1",
  dark: "#1F2937",
};
const FONT = "Tahoma";

function cleanText(value = "") {
  return value
    .replace(/\r/g, "")
    .replace(/<!--[\s\S]*?-->/g, "")
    .replace(/```[\s\S]*?```/g, "")
    .replace(/^> \[![^\]]+\]\s*/gm, "")
    .replace(/^>\s?/gm, "")
    .replace(/\[\[([^\]|]+)\|?([^\]]*)\]\]/g, (_, a, b) => b || a)
    .replace(/\bดู\s+(overview|index)\b.*$/gi, "")
    .replace(/ดู\s+รายละเอียดเต็มที่.*$/gi, "")
    .replace(/\*\*([^*]+)\*\*/g, "$1")
    .replace(/\*([^*]+)\*/g, "$1")
    .replace(/`([^`]+)`/g, "$1")
    .replace(/^\s*[-*]\s+/gm, "")
    .replace(/^\s*\d+\.\s+/gm, "")
    .replace(/[ \t]+/g, " ")
    .trim();
}

function firstSentences(text, limit = 2) {
  const compact = cleanText(text);
  if (!compact) return "";
  const parts = compact
    .split(/(?<=[.!?])\s+|(?<=ได้|ครับ|ค่ะ|ศาสตร์|ระบบ|ข้อมูล|อินเทอร์เน็ต)\s+/u)
    .map((x) => x.trim())
    .filter(Boolean);
  return parts.slice(0, limit).join(" ");
}

function parseFrontmatter(raw) {
  const match = raw.match(/^---\n([\s\S]*?)\n---\n/);
  const fm = {};
  if (!match) return fm;
  for (const line of match[1].split("\n")) {
    const [key, ...rest] = line.split(":");
    if (!key || !rest.length) continue;
    fm[key.trim()] = rest.join(":").trim().replace(/^"|"$/g, "");
  }
  return fm;
}

function section(raw, headingText) {
  const lines = raw.replace(/\r/g, "").split("\n");
  const start = lines.findIndex((line) => line.startsWith("## ") && line.includes(headingText));
  if (start < 0) return "";
  const body = [];
  for (let i = start + 1; i < lines.length; i++) {
    if (lines[i].startsWith("## ")) break;
    body.push(lines[i]);
  }
  return body.join("\n").trim();
}

function listItems(text, max = 5) {
  const items = [];
  for (const line of text.split("\n")) {
    const m = line.match(/^\s*(?:[-*]|\d+\.)\s+(.+)/);
    if (m) items.push(cleanText(m[1]));
  }
  return items.filter(Boolean).slice(0, max);
}

function compactItems(items, maxChars = 88) {
  return items.map((item) => {
    const value = cleanText(item);
    if (value.length <= maxChars) return value;
    return `${value.slice(0, maxChars - 1).trim()}…`;
  });
}

function shorterItems(items, maxChars = 58, max = 3) {
  return compactItems(items, maxChars).slice(0, max);
}

function splitThaiTitle(title) {
  return cleanText(title.replace(/^#\s*/, "")).replace(/^สัปดาห์ที่\s+\d+:\s*/, "");
}

function safeFolderName(value) {
  return value
    .replace(/[<>:"/\\|?*]/g, "")
    .replace(/\s+/g, " ")
    .trim()
    .slice(0, 92);
}

function extractWeek(filepath, raw) {
  const filename = path.basename(filepath, ".md");
  const week = Number(filename.match(/Week\s+(\d+)/)?.[1] || 0);
  const fm = parseFrontmatter(raw);
  const title = raw.match(/^#\s+(.+)$/m)?.[1] || filename;
  const abstract = raw.match(/>\s*\[!abstract\][^\n]*\n([\s\S]*?)(?=\n##\s+)/)?.[1] || "";
  const objectives = listItems(section(raw, "วัตถุประสงค์การสอน"), 5);
  const topics = listItems(section(raw, "สรุปเนื้อหาหัวข้อ"), 5);
  const detail = section(raw, "เนื้อหาโดยละเอียด");
  const detailItems = listItems(detail, 6);
  const concepts = cleanText(section(raw, "แนวคิดหลัก"));
  const trends = listItems(section(raw, "แนวโน้มปัจจุบัน"), 4);
  const lab = firstSentences(section(raw, "กิจกรรม/ปฏิบัติการ"), 2);
  return {
    filename,
    week,
    fm,
    title: splitThaiTitle(title),
    abstract: firstSentences(abstract, 2),
    objectives: compactItems(objectives, 118),
    topics: compactItems(topics, 90),
    detailItems: compactItems(detailItems, 110),
    concepts,
    trends: compactItems(trends, 100),
    lab,
    clo: fm.clo || "",
  };
}

function shape(slide, position, fill = "none", lineFill = "none", name = "") {
  return slide.shapes.add({
    geometry: "rect",
    name,
    position,
    fill,
    line: { style: "solid", fill: lineFill, width: lineFill === "none" ? 0 : 1 },
  });
}

function text(slide, value, position, style = {}, name = "") {
  const s = slide.shapes.add({
    geometry: "textbox",
    name,
    position,
    fill: "none",
    line: { style: "solid", fill: "none", width: 0 },
  });
  s.text = value;
  s.text.style = {
    typeface: FONT,
    fontSize: 22,
    color: C.ink,
    lineSpacing: 1.15,
    ...style,
  };
  return s;
}

function footer(slide, week, index, total) {
  shape(slide, { left: 42, top: 666, width: 1196, height: 1 }, C.rule, "none", "footer-rule");
  text(slide, `EN-001-019 | Week ${String(week).padStart(2, "0")}`, { left: 42, top: 675, width: 420, height: 24 }, { fontSize: 14, color: C.muted }, "footer-left");
  text(slide, `${index}/${total}`, { left: 1180, top: 675, width: 58, height: 24 }, { fontSize: 14, color: C.muted, alignment: "right" }, "footer-page");
}

function addTitle(slide, label, title, subtitle, week) {
  slide.background.fill = C.canvas;
  text(slide, label, { left: 42, top: 42, width: 360, height: 30 }, { fontSize: 16, bold: true, color: C.accent }, "eyebrow");
  text(slide, title, { left: 42, top: 145, width: 860, height: 190 }, { fontSize: 52, bold: true, lineSpacing: 1.05 }, "title");
  shape(slide, { left: 942, top: 94, width: 246, height: 412 }, C.panel, "none", "week-block");
  text(slide, String(week).padStart(2, "0"), { left: 958, top: 148, width: 210, height: 130 }, { fontSize: 92, bold: true, color: C.dark, alignment: "center" }, "week-number");
  text(slide, "Computer Engineering Essentials", { left: 970, top: 304, width: 190, height: 76 }, { fontSize: 24, bold: true, color: C.dark, alignment: "center" }, "course-name");
  text(slide, subtitle, { left: 42, top: 390, width: 760, height: 130 }, { fontSize: 24, color: C.muted, lineSpacing: 1.25 }, "subtitle");
}

function addBullets(slide, items, left, top, width, opts = {}) {
  const size = opts.fontSize || 22;
  const gap = opts.gap || 70;
  items.slice(0, opts.max || 5).forEach((item, i) => {
    const y = top + i * gap;
    shape(slide, { left, top: y + 9, width: 12, height: 12 }, opts.dot || C.accent, "none", `dot-${i}`);
    text(slide, item, { left: left + 28, top: y, width, height: gap - 6 }, { fontSize: size, color: C.ink, lineSpacing: 1.18 }, `bullet-${i}`);
  });
}

function addThreeColumns(slide, columns) {
  const lefts = [64, 454, 844];
  columns.forEach((col, i) => {
    shape(slide, { left: lefts[i], top: 164, width: 330, height: 400 }, i === 1 ? C.softAccent : C.panel, "none", `panel-${i}`);
    text(slide, col.title, { left: lefts[i] + 24, top: 204, width: 282, height: 44 }, { fontSize: 25, bold: true, color: C.dark }, `panel-title-${i}`);
    addBullets(slide, shorterItems(col.items, 52, 3), lefts[i] + 28, 286, 260, { fontSize: 17, gap: 92, max: 3, dot: i === 1 ? C.accent : C.dark });
  });
}

function createDeck(data) {
  const presentation = Presentation.create({ slideSize: { width: W, height: H } });
  const total = 5;

  let slide = presentation.slides.add();
  addTitle(slide, `WEEK ${String(data.week).padStart(2, "0")}`, data.title, data.abstract || "สรุปความรู้สำคัญประจำสัปดาห์และกิจกรรมปฏิบัติการ", data.week);
  footer(slide, data.week, 1, total);

  slide = presentation.slides.add();
  slide.background.fill = C.canvas;
  text(slide, "Learning Objectives", { left: 42, top: 40, width: 720, height: 58 }, { fontSize: 40, bold: true }, "title");
  text(slide, data.clo ? `เชื่อมโยง ${data.clo}` : "เชื่อมโยง CLO ของรายวิชา", { left: 42, top: 104, width: 720, height: 32 }, { fontSize: 19, color: C.muted }, "subtitle");
  addBullets(slide, data.objectives.length ? data.objectives : data.topics, 88, 184, 1010, { fontSize: 24, gap: 82, max: 5 });
  footer(slide, data.week, 2, total);

  slide = presentation.slides.add();
  slide.background.fill = C.canvas;
  text(slide, "Knowledge Map", { left: 42, top: 40, width: 720, height: 58 }, { fontSize: 40, bold: true }, "title");
  addThreeColumns(slide, [
    { title: "หัวข้อหลัก", items: data.topics.length ? data.topics : data.detailItems },
    { title: "แก่นความรู้", items: data.detailItems },
    { title: "แนวคิดเชื่อมโยง", items: (data.concepts ? data.concepts.split("·").map((x) => cleanText(x)) : data.trends).filter(Boolean) },
  ]);
  footer(slide, data.week, 3, total);

  slide = presentation.slides.add();
  slide.background.fill = C.canvas;
  text(slide, "Core Content", { left: 42, top: 40, width: 720, height: 58 }, { fontSize: 40, bold: true }, "title");
  shape(slide, { left: 66, top: 148, width: 502, height: 398 }, C.panel, "none", "left-panel");
  shape(slide, { left: 642, top: 148, width: 502, height: 398 }, C.softAccent, "none", "right-panel");
  text(slide, "ต้องเข้าใจ", { left: 94, top: 184, width: 420, height: 40 }, { fontSize: 26, bold: true, color: C.dark }, "left-head");
  addBullets(slide, data.detailItems.slice(0, 3), 100, 256, 405, { fontSize: 20, gap: 76, max: 3, dot: C.dark });
  text(slide, "แนวโน้ม/บริบทปัจจุบัน", { left: 670, top: 184, width: 420, height: 40 }, { fontSize: 26, bold: true, color: C.accent }, "right-head");
  addBullets(slide, (data.trends.length ? data.trends : data.topics).slice(0, 3), 676, 256, 405, { fontSize: 20, gap: 76, max: 3, dot: C.accent });
  footer(slide, data.week, 4, total);

  slide = presentation.slides.add();
  slide.background.fill = C.canvas;
  text(slide, "Lab & Project Activity", { left: 42, top: 40, width: 800, height: 58 }, { fontSize: 40, bold: true }, "title");
  shape(slide, { left: 78, top: 158, width: 804, height: 252 }, C.panel, "none", "activity-panel");
  text(slide, data.lab || "กิจกรรมประจำสัปดาห์ตามแผน OBE", { left: 114, top: 206, width: 728, height: 150 }, { fontSize: 30, bold: true, color: C.dark, lineSpacing: 1.2 }, "activity");
  shape(slide, { left: 944, top: 158, width: 214, height: 252 }, C.dark, "none", "action-block");
  text(slide, "Output", { left: 974, top: 208, width: 154, height: 44 }, { fontSize: 26, bold: true, color: "#FFFFFF", alignment: "center" }, "output-label");
  text(slide, "ใบงาน\nโค้ด/แบบจำลอง\nreflection", { left: 974, top: 270, width: 154, height: 92 }, { fontSize: 20, color: "#FFFFFF", alignment: "center", lineSpacing: 1.25 }, "output-list");
  text(slide, "ใช้สไลด์ชุดนี้เป็นแกนบรรยายก่อนเข้าสู่กิจกรรมปฏิบัติการ", { left: 78, top: 468, width: 980, height: 54 }, { fontSize: 24, color: C.muted }, "closing");
  footer(slide, data.week, 5, total);

  return presentation;
}

async function writeBlob(file, blob) {
  await fs.writeFile(file, new Uint8Array(await blob.arrayBuffer()));
}

async function main() {
  await fs.mkdir(outputRoot, { recursive: true });
  await fs.mkdir(qaRoot, { recursive: true });

  const files = (await fs.readdir(timelineDir))
    .filter((x) => /^Week \d+ .*\.md$/.test(x))
    .sort();

  const manifest = [];
  for (const file of files) {
    const filepath = path.join(timelineDir, file);
    const raw = await fs.readFile(filepath, "utf8");
    const data = extractWeek(filepath, raw);
    const folder = `Week ${String(data.week).padStart(2, "0")} - ${safeFolderName(data.title)}`;
    const outDir = path.join(outputRoot, folder);
    await fs.mkdir(outDir, { recursive: true });

    const presentation = createDeck(data);
    const base = `Week ${String(data.week).padStart(2, "0")} - ${safeFolderName(data.title)}`;
    const pptxPath = path.join(outDir, `${base}.pptx`);
    const montagePath = path.join(outDir, `${base} - preview.webp`);
    const layoutDir = path.join(qaRoot, `week-${String(data.week).padStart(2, "0")}`);
    await fs.mkdir(layoutDir, { recursive: true });

    for (const [idx, slide] of presentation.slides.items.entries()) {
      const png = await presentation.export({ slide, format: "png", scale: 1 });
      await writeBlob(path.join(layoutDir, `slide-${String(idx + 1).padStart(2, "0")}.png`), png);
      const layout = await slide.export({ format: "layout" });
      await fs.writeFile(path.join(layoutDir, `slide-${String(idx + 1).padStart(2, "0")}.layout.json`), await layout.text());
    }

    const montage = await presentation.export({ format: "webp", montage: true, scale: 1 });
    await writeBlob(montagePath, montage);
    const pptx = await PresentationFile.exportPptx(presentation);
    await pptx.save(pptxPath);

    manifest.push({
      week: data.week,
      title: data.title,
      folder: path.relative(root, outDir),
      pptx: path.relative(root, pptxPath),
      preview: path.relative(root, montagePath),
    });
    console.log(`Created ${path.relative(root, pptxPath)}`);
  }

  await fs.writeFile(path.join(outputRoot, "manifest.json"), JSON.stringify(manifest, null, 2), "utf8");
  console.log(`Wrote ${path.relative(root, path.join(outputRoot, "manifest.json"))}`);
}

main().catch((err) => {
  console.error(err);
  process.exitCode = 1;
});
