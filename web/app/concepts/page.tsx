import Link from "next/link";
import { BookMarked, ArrowRight } from "lucide-react";
import { manifest } from "@/lib/content";
import { course } from "@/lib/course";

export const metadata = {
  title: `พจนานุกรมศัพท์ (Concepts) | ${course.code}`,
  description: "รวมศัพท์และกรอบแนวคิดสำคัญของรายวิชาแก่นวิศวกรรมคอมพิวเตอร์",
};

export default function ConceptsPage() {
  const themes = manifest.docs.filter((d) => d.group === "theme");
  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 py-8">
      <nav className="flex items-center gap-2 text-sm text-gray-500 dark:text-gray-400 mb-6">
        <Link href="/" className="hover:text-blue-600 dark:hover:text-blue-400 transition-colors">
          หน้าหลัก
        </Link>
        <span>/</span>
        <span className="text-gray-900 dark:text-white font-medium">พจนานุกรมศัพท์</span>
      </nav>

      <div className="mb-8">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-orange-50 dark:bg-orange-900/30 text-orange-700 dark:text-orange-300 text-xs font-medium mb-3">
          <BookMarked className="w-3.5 h-3.5" /> Concepts
        </div>
        <h1 className="text-2xl md:text-3xl font-bold text-gray-900 dark:text-white mb-1">พจนานุกรมศัพท์และกรอบแนวคิด</h1>
        <p className="text-sm text-gray-500 dark:text-gray-400">{manifest.concepts.length} ศัพท์สำคัญที่ปรากฏซ้ำข้ามสัปดาห์ พร้อมบริบทในรายวิชาและแหล่งอ้างอิง</p>
      </div>

      <div className="grid md:grid-cols-2 gap-3 mb-12">
        {manifest.concepts.map((c) => (
          <Link
            key={c.slug}
            href={`/concept/${c.slug}`}
            className="group p-4 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 hover:border-orange-300 dark:hover:border-orange-700 hover:shadow-md transition-all"
          >
            <div className="flex items-start justify-between gap-2">
              <h3 className="font-semibold text-gray-900 dark:text-white group-hover:text-orange-600 dark:group-hover:text-orange-400 transition-colors">
                {c.title}
              </h3>
              <ArrowRight className="w-4 h-4 text-gray-300 dark:text-gray-600 flex-shrink-0 mt-1" />
            </div>
            <p className="text-sm text-gray-600 dark:text-gray-400 mt-1 line-clamp-3">{c.definition}</p>
            {c.weeks.length > 0 && (
              <p className="text-xs text-gray-400 dark:text-gray-500 mt-2">สัปดาห์: {c.weeks.map((w) => `W${Number(w)}`).join(", ")}</p>
            )}
          </Link>
        ))}
      </div>

      <h2 className="text-xl font-bold text-gray-900 dark:text-white mb-4">ธีมตัดขวางของรายวิชา</h2>
      <div className="grid md:grid-cols-2 gap-3">
        {themes.map((d) => (
          <Link
            key={d.slug}
            href={`/docs/${d.slug}`}
            className="p-4 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 hover:border-blue-300 dark:hover:border-blue-700 hover:shadow-md transition-all font-medium text-gray-900 dark:text-white"
          >
            {d.title}
          </Link>
        ))}
      </div>
    </div>
  );
}
