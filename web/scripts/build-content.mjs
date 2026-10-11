// สร้างโฟลเดอร์ content/ จากคลังความรู้ Obsidian (../wiki) และสไลด์ (../slides)
//   content/modules/module-XX.md      ← เนื้อหาเรียนรู้รายสัปดาห์ + แผนการสอน
//   content/topics/XX/NN.md           ← เนื้อหาเชิงลึก (deep dive) ของสัปดาห์
//   content/labs/lab-XX.md            ← ใบงานปฏิบัติการ
//   content/concepts/<slug>.md        ← พจนานุกรมศัพท์
//   content/docs/<slug>.md            ← เอกสารรายวิชา (CLO, การประเมิน, ธีม ฯลฯ)
//   content/slides/week-XX.pptx       ← สไลด์ประจำสัปดาห์ (+ public/images/slides/week-XX.webp)
//   content/manifest.json             ← ดัชนีทุกอย่างข้างต้น
// รัน: npm run content   (ข้ามอัตโนมัติถ้าไม่พบ ../wiki เช่น ตอน deploy เฉพาะโฟลเดอร์ web/)
import { readdir, readFile, writeFile, mkdir, copyFile, stat, rm } from "fs/promises";
import path from "path";
import { fileURLToPath } from "url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const VAULT = path.resolve(ROOT, "..");
const WIKI = path.join(VAULT, "wiki");
const SLIDES = path.join(VAULT, "slides");
const OUT = path.join(ROOT, "content");
const PUBLIC_SLIDES = path.join(ROOT, "public", "images", "slides");

const WEEKS = Array.from({ length: 17 }, (_, i) => String(i + 1).padStart(2, "0"));

// ---------- slug maps (ชื่อโน้ต Obsidian → เส้นทางในเว็บ) ----------
const DOC_SLUGS = {
  "แผนการสอนและ CLO": "course-plan",
  "CLO-PLO-KSA Mapping": "clo-plo-mapping",
  "การวัดและประเมินผล": "assessment",
  "กิจกรรมปฏิบัติการและโครงงาน": "labs-projects",
  "รายงานวิชาการ-ภาพรวม": "course-report",
  "ปัญญาประดิษฐ์เป็นแรงขับเคลื่อนข้ามศาสตร์": "theme-ai",
  "Edge Computing และระบบกระจาย": "theme-edge",
  "Green Computing และความยั่งยืน": "theme-green",
  "ความปลอดภัยและสถาปัตยกรรมความน่าเชื่อถือ (ธีม)": "theme-security",
  "การกำกับดูแล จริยธรรม และกฎหมาย": "theme-governance",
};
const DOC_GROUPS = {
  "course-plan": "course", "clo-plo-mapping": "course", "assessment": "course", "labs-projects": "course", "course-report": "course",
  "theme-ai": "theme", "theme-edge": "theme", "theme-green": "theme", "theme-security": "theme", "theme-governance": "theme",
};
const INDEX_LINKS = {
  index: "/", overview: "/", _index: "/", "Learning Content Index": "/", "Timeline & Curriculum Map": "/",
  "Concepts Index": "/concepts", "Themes Index": "/concepts", "Synthesis Index": "/docs/course-plan", "Characters Index": "/",
};

function conceptSlug(name) {
  const ascii = name.replace(/[^\x00-\x7F]/g, " ").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "");
  return ascii || "concept";
}

// ---------- helpers ----------
async function exists(p) {
  try { await stat(p); return true; } catch { return false; }
}
async function listFiles(dir, pattern) {
  try {
    return (await readdir(dir)).filter((f) => pattern.test(f)).sort();
  } catch { return []; }
}
function stripFrontmatter(md) {
  return md.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n?/, "");
}
function firstH1(md) {
  return md.match(/^#\s+(.+?)\s*$/m)?.[1]?.trim();
}
function stripFirstH1(md) {
  return md.replace(/^#\s+.+\r?\n?/m, "");
}
function normalize(md) {
  return md.replace(/\r\n/g, "\n").trim() + "\n";
}
function demoteHeadings(md) {
  // ## → ###, ### → #### (ข้ามบล็อกโค้ด)
  return md
    .split(/(^```[\s\S]*?^```)/m)
    .map((part, i) => (i % 2 === 1 ? part : part.replace(/^(#{2,5})\s/gm, "#$1 ")))
    .join("");
}
function cleanTitle(t) {
  return t.replace(/^[\p{Extended_Pictographic}‍️\s]+/u, "").replace(/^(Lab \d+:|ธีม:)\s*/, "").trim();
}

// ---------- wikilink resolver ----------
let TOPIC_SET = new Set(); // "XX/NN"
let CONCEPT_MAP = new Map(); // name → slug

function resolveLink(target) {
  const t = target.trim().replace(/\\$/, "");
  let m;
  if ((m = /^Week (\d{2})\/(\d{2})_/.exec(t))) {
    return m[2] === "00" ? `/module/${m[1]}` : TOPIC_SET.has(`${m[1]}/${m[2]}`) ? `/module/${m[1]}/${m[2]}` : `/module/${m[1]}`;
  }
  if ((m = /^Week (\d{2})\b/.exec(t))) return `/module/${m[1]}`;
  if ((m = /^Learning Content Week (\d{2})/.exec(t))) return `/module/${m[1]}`;
  if ((m = /^Lab (\d{2})\b/.exec(t))) return `/lab/${m[1]}`;
  if (DOC_SLUGS[t]) return `/docs/${DOC_SLUGS[t]}`;
  if (CONCEPT_MAP.has(t)) return `/concept/${CONCEPT_MAP.get(t)}`;
  if (INDEX_LINKS[t] !== undefined) return INDEX_LINKS[t];
  return null;
}
function displayName(target) {
  const t = target.trim().replace(/\\$/, "");
  let m;
  if ((m = /^Week (\d{2})\/\d{2}_(.+)$/.exec(t))) return m[2].replace(/_/g, " ").replace(/^Overview - /, "");
  if ((m = /^Week (\d{2}) - (.+)$/.exec(t))) return `สัปดาห์ที่ ${Number(m[1])}: ${m[2]}`;
  if ((m = /^Week (\d{2})$/.exec(t))) return `สัปดาห์ที่ ${Number(m[1])}`;
  if ((m = /^Learning Content Week (\d{2}) - (.+)$/.exec(t))) return `สัปดาห์ที่ ${Number(m[1])}: ${m[2]}`;
  if (t === "_index") return "สารบัญ";
  return t;
}
function convertWikilinks(md) {
  return md
    .split(/(^```[\s\S]*?^```)/m)
    .map((part, i) => {
      if (i % 2 === 1) return part;
      return part.replace(/\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|([^\]]+))?\]\]/g, (_, target, alias) => {
        const href = resolveLink(target);
        const text = alias?.trim() || displayName(target);
        return href ? `[${text}](${href})` : text;
      });
    })
    .join("");
}

// ---------- builders ----------
async function readNote(p) {
  return normalize(stripFrontmatter(await readFile(p, "utf-8")));
}

async function buildTopics(manifest) {
  for (const w of WEEKS) {
    const dir = path.join(WIKI, "learning", `Week ${w}`);
    const files = await listFiles(dir, /^0[1-9]_.*\.md$/);
    for (const f of files) {
      const n = f.slice(0, 2);
      const raw = await readNote(path.join(dir, f));
      if (/ฉบับร่าง/.test(raw) || raw.length < 200) continue; // ข้ามหัวข้อที่ยังเป็นฉบับร่าง
      TOPIC_SET.add(`${w}/${n}`);
      manifest.topics[w] ??= [];
      manifest.topics[w].push({ n, title: cleanTitle(firstH1(raw) ?? f), file: f });
      manifest._topicRaw.push({ w, n, raw });
    }
  }
}

async function writeTopics(manifest) {
  for (const { w, n, raw } of manifest._topicRaw) {
    const body = convertWikilinks(stripFirstH1(raw)).replace(/^> \*\*หมวดหมู่:\*\*.*\n+/m, "");
    await mkdir(path.join(OUT, "topics", w), { recursive: true });
    await writeFile(path.join(OUT, "topics", w, `${n}.md`), normalize(body), "utf-8");
  }
  delete manifest._topicRaw;
}

async function buildModules(manifest) {
  await mkdir(path.join(OUT, "modules"), { recursive: true });
  const learningDir = path.join(WIKI, "learning");
  const timelineDir = path.join(WIKI, "timeline");
  const learningFlat = await listFiles(learningDir, /^Learning Content Week \d{2}.*\.md$/);
  const timelineFiles = await listFiles(timelineDir, /^Week \d{2} - .*\.md$/);

  for (const w of WEEKS) {
    const parts = [];
    // 1) เนื้อหาเรียนรู้: ใช้ Week XX/00_Overview ถ้ามีเนื้อหาจริง ไม่งั้นใช้ Learning Content Week XX
    const weekDir = path.join(learningDir, `Week ${w}`);
    const ov = (await listFiles(weekDir, /^00_.*\.md$/))[0];
    let overview = ov ? await readNote(path.join(weekDir, ov)) : "";
    const flat = learningFlat.find((f) => f.startsWith(`Learning Content Week ${w}`));
    const flatMd = flat ? await readNote(path.join(learningDir, flat)) : "";
    const overviewIsStub = !overview || overview.length < 400 || /เนื้อหาสรุปของสัปดาห์นี้/.test(overview);
    let learning = overviewIsStub ? flatMd : overview;
    if (!overviewIsStub && flatMd && flatMd !== overview) {
      // มีทั้ง overview จริงและไฟล์ learning content → ต่อกัน (overview ก่อน)
      learning = overview + "\n---\n\n" + stripFirstH1(flatMd);
    }
    if (learning) {
      let body = stripFirstH1(learning).replace(/^> ใช้คู่กับ .*\n+/m, "").replace(/^> กลับ \[\[Learning Content Index\]\].*$/m, "");
      parts.push(convertWikilinks(body).trim());
    }
    // 2) แผนการสอนรายสัปดาห์ (timeline)
    const tl = timelineFiles.find((f) => f.startsWith(`Week ${w} - `));
    if (tl) {
      let body = stripFirstH1(await readNote(path.join(timelineDir, tl)));
      body = body.replace(/^## 🔗 นำทาง[\s\S]*$/m, "").trim();
      parts.push(`## 🗓️ แผนการสอนประจำสัปดาห์ (Teaching Plan)\n\n${convertWikilinks(demoteHeadings(body))}`);
      manifest.modules[w] = { timelineTitle: tl.replace(/^Week \d{2} - /, "").replace(/\.md$/, "") };
    }
    // 3) รายการหัวข้อเชิงลึก
    const topics = manifest.topics[w] ?? [];
    if (topics.length) {
      parts.push(
        `## 📚 เนื้อหาเชิงลึกประจำสัปดาห์ (Deep Dive)\n\n` +
          topics.map((t) => `- [${t.n}. ${t.title}](/module/${w}/${t.n})`).join("\n")
      );
    }
    await writeFile(path.join(OUT, "modules", `module-${w}.md`), normalize(parts.join("\n\n---\n\n")), "utf-8");
  }
}

async function buildLabs(manifest) {
  await mkdir(path.join(OUT, "labs"), { recursive: true });
  const labsDir = path.join(WIKI, "labs");
  const moduleDirs = (await listFiles(labsDir, /^Module \d/));
  for (const md of moduleDirs) {
    const dir = path.join(labsDir, md);
    for (const f of await listFiles(dir, /^Lab \d{2} - .*\.md$/)) {
      const id = f.slice(4, 6);
      const raw = await readNote(path.join(dir, f));
      const title = cleanTitle(firstH1(raw) ?? f);
      let body = stripFirstH1(raw).replace(/^## 🔗 ลิงก์ที่เกี่ยวข้อง[\s\S]*$/m, "").trim();
      await writeFile(path.join(OUT, "labs", `lab-${id}.md`), normalize(convertWikilinks(body)), "utf-8");
      manifest.labs.push({ id, title, module: md.replace(/^Module (\d) - .*/, "$1") });
    }
  }
  manifest.labs.sort((a, b) => a.id.localeCompare(b.id));
}

async function buildConcepts(manifest) {
  await mkdir(path.join(OUT, "concepts"), { recursive: true });
  const dir = path.join(WIKI, "concepts");
  const files = (await listFiles(dir, /\.md$/)).filter((f) => !f.startsWith("_"));
  for (const f of files) CONCEPT_MAP.set(f.replace(/\.md$/, ""), conceptSlug(f.replace(/\.md$/, "")));
  for (const f of files) {
    const name = f.replace(/\.md$/, "");
    const slug = CONCEPT_MAP.get(name);
    const raw = await readNote(path.join(dir, f));
    const title = firstH1(raw) ?? name;
    const defRaw = raw.match(/## Definition\s*\n+([\s\S]*?)(?=\n## |\n*$)/)?.[1]?.replace(/\s+/g, " ").trim() ?? "";
    const def = convertWikilinks(defRaw).replace(/\[([^\]]+)\]\([^)]+\)/g, "$1");
    const weeks = [...raw.matchAll(/\[\[Week (\d{2})/g)].map((m) => m[1]);
    await writeFile(path.join(OUT, "concepts", `${slug}.md`), normalize(convertWikilinks(stripFirstH1(raw))), "utf-8");
    manifest.concepts.push({ slug, name, title, definition: def.replace(/\*\*/g, "").slice(0, 220), weeks: [...new Set(weeks)].sort() });
  }
  manifest.concepts.sort((a, b) => a.title.localeCompare(b.title, "en"));
}

async function buildDocs(manifest) {
  await mkdir(path.join(OUT, "docs"), { recursive: true });
  for (const sub of ["synthesis", "themes"]) {
    const dir = path.join(WIKI, sub);
    for (const f of await listFiles(dir, /\.md$/)) {
      const name = f.replace(/\.md$/, "");
      const slug = DOC_SLUGS[name];
      if (!slug) continue;
      const raw = await readNote(path.join(dir, f));
      const title = cleanTitle(firstH1(raw) ?? name);
      let body = stripFirstH1(raw).replace(/^## 🔗 ลิงก์\s*\n[\s\S]*$/m, "").trim();
      await writeFile(path.join(OUT, "docs", `${slug}.md`), normalize(convertWikilinks(body)), "utf-8");
      manifest.docs.push({ slug, title, group: DOC_GROUPS[slug] });
    }
  }
}

async function buildSlides(manifest) {
  if (!(await exists(SLIDES))) return;
  await mkdir(path.join(OUT, "slides"), { recursive: true });
  await mkdir(PUBLIC_SLIDES, { recursive: true });
  const dirs = await listFiles(SLIDES, /^Week \d{2} - /);
  for (const d of dirs) {
    const w = d.slice(5, 7);
    const files = await readdir(path.join(SLIDES, d));
    const pptx = files.find((f) => f.endsWith(".pptx"));
    const preview = files.find((f) => f.endsWith("preview.webp"));
    if (pptx) await copyFile(path.join(SLIDES, d, pptx), path.join(OUT, "slides", `week-${w}.pptx`));
    if (preview) await copyFile(path.join(SLIDES, d, preview), path.join(PUBLIC_SLIDES, `week-${w}.webp`));
    manifest.slides[w] = { pptx: pptx ? `week-${w}.pptx` : null, preview: preview ? `/images/slides/week-${w}.webp` : null, title: d.replace(/^Week \d{2} - /, "") };
  }
}

async function main() {
  if (!(await exists(WIKI))) {
    console.log("ไม่พบ ../wiki — ใช้ content/ ที่สร้างไว้แล้ว");
    return;
  }
  for (const sub of ["modules", "topics", "labs", "concepts", "docs"]) await rm(path.join(OUT, sub), { recursive: true, force: true });

  const manifest = { generated: new Date().toISOString(), modules: {}, topics: {}, _topicRaw: [], labs: [], concepts: [], docs: [], slides: {} };
  // ลำดับสำคัญ: concepts/topics ก่อน เพื่อให้ resolver รู้จักลิงก์
  const conceptFiles = (await listFiles(path.join(WIKI, "concepts"), /\.md$/)).filter((f) => !f.startsWith("_"));
  for (const f of conceptFiles) CONCEPT_MAP.set(f.replace(/\.md$/, ""), conceptSlug(f.replace(/\.md$/, "")));
  await buildTopics(manifest);
  await writeTopics(manifest);
  await buildModules(manifest);
  await buildLabs(manifest);
  await buildConcepts(manifest);
  await buildDocs(manifest);
  await buildSlides(manifest);
  await mkdir(OUT, { recursive: true });
  await writeFile(path.join(OUT, "manifest.json"), JSON.stringify(manifest, null, 2) + "\n", "utf-8");

  const topicCount = Object.values(manifest.topics).reduce((a, t) => a + t.length, 0);
  console.log(`modules: ${WEEKS.length} · topics: ${topicCount} · labs: ${manifest.labs.length} · concepts: ${manifest.concepts.length} · docs: ${manifest.docs.length} · slides: ${Object.keys(manifest.slides).length}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
