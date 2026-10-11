import Link from "next/link";
import { Presentation, Download } from "lucide-react";
import { modules, colorMap } from "@/lib/modules-data";
import { manifest } from "@/lib/content";
import { course } from "@/lib/course";

export const metadata = {
  title: `สไลด์ประกอบการสอน | ${course.code}`,
  description: "รวมสไลด์ PowerPoint ประกอบการสอนทั้ง 17 สัปดาห์",
};

export default function SlidesPage() {
  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 py-8">
      <nav className="flex items-center gap-2 text-sm text-gray-500 dark:text-gray-400 mb-6">
        <Link href="/" className="hover:text-blue-600 dark:hover:text-blue-400 transition-colors">
          หน้าหลัก
        </Link>
        <span>/</span>
        <span className="text-gray-900 dark:text-white font-medium">สไลด์ประกอบการสอน</span>
      </nav>

      <div className="mb-8">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-orange-50 dark:bg-orange-900/30 text-orange-700 dark:text-orange-300 text-xs font-medium mb-3">
          <Presentation className="w-3.5 h-3.5" /> Slides
        </div>
        <h1 className="text-2xl md:text-3xl font-bold text-gray-900 dark:text-white mb-1">สไลด์ประกอบการสอนรายสัปดาห์</h1>
        <p className="text-sm text-gray-500 dark:text-gray-400">ดาวน์โหลดเป็นไฟล์ PowerPoint (.pptx) เพื่อใช้ทบทวนก่อนและหลังเรียน</p>
      </div>

      <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {modules.map((mod) => {
          const slide = manifest.slides[mod.id];
          if (!slide) return null;
          const colors = colorMap[mod.color] ?? colorMap.blue;
          return (
            <div
              key={mod.id}
              className={`rounded-xl border ${colors.border} bg-white dark:bg-gray-900 overflow-hidden hover:shadow-md transition-all flex flex-col`}
            >
              {slide.preview && (
                // eslint-disable-next-line @next/next/no-img-element
                <img src={slide.preview} alt={slide.title} className="w-full aspect-video object-cover border-b border-gray-200 dark:border-gray-800" loading="lazy" />
              )}
              <div className="p-4 flex-1 flex flex-col">
                <p className={`text-xs font-semibold ${colors.text}`}>สัปดาห์ที่ {mod.week}</p>
                <Link href={`/module/${mod.id}`} className="font-semibold text-gray-900 dark:text-white text-sm leading-snug hover:text-blue-600 dark:hover:text-blue-400">
                  {mod.titleTh}
                </Link>
                <p className="text-xs text-gray-500 dark:text-gray-400 mb-3">{mod.titleEn}</p>
                {slide.pptx && (
                  <a
                    href={`/api/content/slides/${slide.pptx}`}
                    className="mt-auto inline-flex items-center justify-center gap-2 px-3 py-2 text-sm font-semibold rounded-lg bg-orange-600 text-white hover:bg-orange-700 transition-colors"
                  >
                    <Download className="w-4 h-4" /> ดาวน์โหลด .pptx
                  </a>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
