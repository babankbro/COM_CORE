import Link from "next/link";
import {
  BookOpen,
  FileEdit,
  ArrowRight,
  GraduationCap,
  Layers,
  PenSquare,
  Target,
  Library,
  Presentation,
  BookMarked,
  FlaskConical,
  CalendarDays,
  Calculator,
} from "lucide-react";
import { modules, colorMap, projects } from "@/lib/modules-data";
import { course, clos, textbooks } from "@/lib/course";
import { manifest } from "@/lib/content";
import ModuleIcon from "@/components/ModuleIcon";

const topicCount = Object.values(manifest.topics).reduce((a, t) => a + t.length, 0);
const examCount = modules.filter((m) => m.hasExam).length;

const stats = [
  { icon: BookOpen, label: `${modules.length} สัปดาห์`, sub: `${topicCount} หัวข้อเชิงลึก`, color: "text-blue-600 dark:text-blue-400" },
  { icon: FileEdit, label: `${manifest.labs.length} ใบงาน`, sub: "4 Mini-Projects", color: "text-green-600 dark:text-green-400" },
  { icon: Presentation, label: `${Object.keys(manifest.slides).length} ชุดสไลด์`, sub: "PowerPoint ทุกสัปดาห์", color: "text-orange-600 dark:text-orange-400" },
  { icon: PenSquare, label: `${examCount} แบบทดสอบ`, sub: "Quiz ออนไลน์พร้อมเฉลย", color: "text-purple-600 dark:text-purple-400" },
];

const PROJECT_COLORS: Record<string, string> = {
  green: "border-green-200 dark:border-green-800 bg-green-50 dark:bg-green-900/20",
  blue: "border-blue-200 dark:border-blue-800 bg-blue-50 dark:bg-blue-900/20",
  orange: "border-orange-200 dark:border-orange-800 bg-orange-50 dark:bg-orange-900/20",
  purple: "border-purple-200 dark:border-purple-800 bg-purple-50 dark:bg-purple-900/20",
};

export default function HomePage() {
  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 py-10">
      {/* Hero */}
      <div className="mb-12">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-50 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300 text-xs font-medium mb-4">
          <GraduationCap className="w-3.5 h-3.5" />
          สื่อการสอนออนไลน์ · ภาคการศึกษาที่ 1/{course.year} · {course.credits}
        </div>
        <h1 className="text-3xl md:text-4xl font-bold text-gray-900 dark:text-white mb-2">
          {course.code} {course.titleEn}
        </h1>
        <h2 className="text-2xl md:text-3xl font-bold text-gray-900 dark:text-white mb-4">{course.titleTh}</h2>
        <p className="text-gray-500 dark:text-gray-400 mb-1">จัดทำโดย</p>
        <p className="text-xl font-semibold text-gray-900 dark:text-white mb-1">{course.instructor}</p>
        <p className="text-sm text-gray-500 dark:text-gray-400 mb-4">
          {course.program} {course.faculty}
        </p>
        <p className="text-gray-600 dark:text-gray-400 leading-relaxed max-w-3xl">
          ภาพรวมวิศวกรรมคอมพิวเตอร์ตั้งแต่ฮาร์ดแวร์ วงจรตรรกะ อัลกอริทึม ฐานข้อมูล เครือข่าย และศูนย์ข้อมูล
          ไปจนถึง AI, Generative AI, IoT, ความปลอดภัยไซเบอร์ จริยธรรม และ DevOps
          เรียนผ่าน 4 Mini-Projects (เกม, เว็บแอป, IoT, Computer Vision) ตลอด 17 สัปดาห์
        </p>
      </div>

      {/* Quick stats */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-3 mb-12">
        {stats.map(({ icon: Icon, label, sub, color }) => (
          <div key={sub} className="flex items-center gap-3 p-3 rounded-xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-800">
            <Icon className={`w-5 h-5 ${color}`} />
            <div>
              <p className="text-sm font-semibold text-gray-900 dark:text-white">{label}</p>
              <p className="text-xs text-gray-500 dark:text-gray-400">{sub}</p>
            </div>
          </div>
        ))}
      </div>

      {/* Quick links */}
      <div className="grid md:grid-cols-2 gap-4 mb-12">
        <Link
          href="/docs/course-plan"
          className="flex items-center gap-4 p-5 rounded-2xl border border-amber-200 dark:border-amber-800 bg-amber-50 dark:bg-amber-900/20 hover:shadow-md transition-all"
        >
          <div className="w-12 h-12 rounded-xl bg-amber-500 text-white flex items-center justify-center flex-shrink-0">
            <Target className="w-6 h-6" />
          </div>
          <div className="flex-1">
            <p className="font-bold text-gray-900 dark:text-white">แผนการสอนและผลลัพธ์การเรียนรู้ (CLO)</p>
            <p className="text-sm text-gray-600 dark:text-gray-400">CLO 6 ข้อ · ความสอดคล้อง PLO/KSA · รูปแบบคาบเรียน</p>
          </div>
          <ArrowRight className="w-5 h-5 text-amber-600 dark:text-amber-400" />
        </Link>
        <Link
          href="/docs/assessment"
          className="flex items-center gap-4 p-5 rounded-2xl border border-sky-200 dark:border-sky-800 bg-sky-50 dark:bg-sky-900/20 hover:shadow-md transition-all"
        >
          <div className="w-12 h-12 rounded-xl bg-sky-600 text-white flex items-center justify-center flex-shrink-0">
            <CalendarDays className="w-6 h-6" />
          </div>
          <div className="flex-1">
            <p className="font-bold text-gray-900 dark:text-white">การวัดและประเมินผล</p>
            <p className="text-sm text-gray-600 dark:text-gray-400">สัดส่วนคะแนน · เกณฑ์ตัดเกรด · Rubric โครงงานและจริยธรรม</p>
          </div>
          <ArrowRight className="w-5 h-5 text-sky-600 dark:text-sky-400" />
        </Link>
      </div>

      <Link
        href="/calc-examples"
        className="flex items-center gap-4 p-5 -mt-8 mb-12 rounded-2xl border border-violet-200 dark:border-violet-800 bg-violet-50 dark:bg-violet-900/20 hover:shadow-md transition-all"
      >
        <div className="w-12 h-12 rounded-xl bg-violet-600 text-white flex items-center justify-center flex-shrink-0">
          <Calculator className="w-6 h-6" />
        </div>
        <div className="flex-1">
          <p className="font-bold text-gray-900 dark:text-white">ตัวอย่างโจทย์คำนวณพร้อมวิธีทำ</p>
          <p className="text-sm text-gray-600 dark:text-gray-400">
            โจทย์จากข้อสอบชุดที่ 2–3 จัดเป็น 10 หมวด (เลขฐาน เกตตรรกะ Big-O PUE ESP32 I2C Regression IoU) พร้อม infographic
          </p>
        </div>
        <ArrowRight className="w-5 h-5 text-violet-600 dark:text-violet-400" />
      </Link>

      {/* Mini-projects */}
      <h2 className="text-xl font-bold text-gray-900 dark:text-white mb-5 flex items-center gap-2">
        <FlaskConical className="w-5 h-5" />4 Mini-Projects
      </h2>
      <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-3 mb-12">
        {projects.map((p) => (
          <Link
            key={p.id}
            href="/docs/labs-projects"
            className={`p-4 rounded-xl border hover:shadow-md transition-all ${PROJECT_COLORS[p.color]}`}
          >
            <p className="text-xs font-semibold text-gray-500 dark:text-gray-400 mb-1">{p.weeks}</p>
            <p className="font-semibold text-gray-900 dark:text-white text-sm leading-snug">{p.name}</p>
            <p className="text-xs text-gray-600 dark:text-gray-400 mt-2">🎯 {p.goal}</p>
          </Link>
        ))}
      </div>

      {/* Module List */}
      <h2 className="text-xl font-bold text-gray-900 dark:text-white mb-5 flex items-center gap-2">
        <Layers className="w-5 h-5" />
        บทเรียนรายสัปดาห์ (17 สัปดาห์)
      </h2>

      <div className="space-y-3">
        {modules.map((mod) => {
          const colors = colorMap[mod.color] ?? colorMap.blue;
          const topics = manifest.topics[mod.id] ?? [];
          const slide = manifest.slides[mod.id];
          return (
            <div
              key={mod.id}
              className={`group flex items-start gap-4 p-4 rounded-xl border ${colors.border} hover:shadow-md transition-all bg-white dark:bg-gray-900`}
            >
              <Link
                href={`/module/${mod.id}`}
                className={`flex-shrink-0 w-11 h-11 rounded-xl ${colors.bg} ${colors.text} flex flex-col items-center justify-center hover:opacity-80 transition-opacity`}
              >
                <ModuleIcon name={mod.icon} className="w-4 h-4" />
                <span className="text-[10px] font-bold leading-none mt-0.5">W{mod.id}</span>
              </Link>

              <div className="flex-1 min-w-0">
                <Link href={`/module/${mod.id}`} className="block">
                  <div className="flex flex-wrap items-baseline gap-x-2">
                    <h3 className="font-semibold text-gray-900 dark:text-white hover:text-blue-600 dark:hover:text-blue-400 transition-colors">
                      {mod.titleTh}
                    </h3>
                    <span className="text-[11px] text-gray-400 dark:text-gray-500">
                      สัปดาห์ที่ {mod.week} · {mod.clo.join(", ")}
                      {mod.project ? ` · Mini-Project ${mod.project}` : ""}
                    </span>
                  </div>
                  <p className="text-sm text-gray-500 dark:text-gray-400">{mod.titleEn}</p>
                  <p className="text-xs text-gray-400 dark:text-gray-500 mt-1">{mod.description}</p>
                </Link>

                <div className="flex flex-wrap gap-2 mt-3">
                  {topics.length > 0 && (
                    <span className="inline-flex items-center gap-1 px-2 py-1 text-[11px] font-medium rounded-md bg-indigo-50 dark:bg-indigo-900/30 text-indigo-700 dark:text-indigo-300">
                      <BookMarked className="w-3 h-3" /> {topics.length} หัวข้อเชิงลึก
                    </span>
                  )}
                  {mod.hasLab && (
                    <Link
                      href={`/lab/${mod.id}`}
                      className="inline-flex items-center gap-1 px-2 py-1 text-[11px] font-medium rounded-md bg-green-50 dark:bg-green-900/30 text-green-700 dark:text-green-300 hover:bg-green-100 dark:hover:bg-green-900/50 transition-colors"
                    >
                      <FileEdit className="w-3 h-3" /> Lab {mod.id}
                    </Link>
                  )}
                  {slide?.pptx && (
                    <a
                      href={`/api/content/slides/${slide.pptx}`}
                      className="inline-flex items-center gap-1 px-2 py-1 text-[11px] font-medium rounded-md bg-orange-50 dark:bg-orange-900/30 text-orange-700 dark:text-orange-300 hover:bg-orange-100 dark:hover:bg-orange-900/50 transition-colors"
                    >
                      <Presentation className="w-3 h-3" /> Slides
                    </a>
                  )}
                  {mod.hasExam && (
                    <Link
                      href={`/exam/${mod.id}`}
                      className="inline-flex items-center gap-1 px-2 py-1 text-[11px] font-semibold rounded-md bg-purple-600 dark:bg-purple-700 text-white hover:bg-purple-700 dark:hover:bg-purple-600 transition-colors"
                    >
                      <PenSquare className="w-3 h-3" /> Quiz
                    </Link>
                  )}
                </div>
              </div>

              <Link href={`/module/${mod.id}`} className="flex-shrink-0 mt-1" aria-label={`ไปที่สัปดาห์ที่ ${mod.week}`}>
                <ArrowRight className="w-5 h-5 text-gray-300 dark:text-gray-600 hover:text-blue-500 dark:hover:text-blue-400 transition-colors" />
              </Link>
            </div>
          );
        })}
      </div>

      {/* CLOs */}
      <h2 className="text-xl font-bold text-gray-900 dark:text-white mt-12 mb-5 flex items-center gap-2">
        <Target className="w-5 h-5" />
        ผลลัพธ์การเรียนรู้ระดับรายวิชา (CLOs)
      </h2>
      <div className="grid md:grid-cols-2 gap-3">
        {clos.map((clo) => {
          const related = modules.filter((m) => m.clo.includes(clo.id)).map((m) => `W${m.week}`);
          return (
            <div key={clo.id} className="p-4 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900">
              <p className="text-sm font-bold text-violet-700 dark:text-violet-300 mb-1">
                {clo.id} <span className="font-normal text-xs text-gray-400">· {clo.plo} · {clo.ksa}</span>
              </p>
              <p className="text-sm text-gray-700 dark:text-gray-300 mb-2">{clo.text}</p>
              <p className="text-xs text-gray-500 dark:text-gray-400">สัปดาห์: {related.join(", ")}</p>
            </div>
          );
        })}
      </div>

      {/* Textbooks */}
      <div className="mt-12 p-6 rounded-2xl bg-gradient-to-r from-blue-600 to-cyan-600 text-white">
        <div className="flex items-start gap-4">
          <div className="w-12 h-12 bg-white/20 rounded-xl flex items-center justify-center flex-shrink-0">
            <Library className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-lg font-bold mb-2">ตำราและเอกสารอ้างอิงหลัก</h3>
            <ul className="space-y-1.5 text-sm text-blue-50">
              {textbooks.map((t) => (
                <li key={t}>• {t}</li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}
