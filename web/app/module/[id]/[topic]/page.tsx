import { notFound } from "next/navigation";
import Link from "next/link";
import { ArrowLeft, ArrowRight, BookOpen, BookMarked } from "lucide-react";
import { modules, getModuleById, colorMap } from "@/lib/modules-data";
import { getTopicContent, getTopics, getTopic, manifest } from "@/lib/content";
import { course } from "@/lib/course";
import MarkdownContent from "@/components/MarkdownContent";

interface PageProps {
  params: { id: string; topic: string };
}

export function generateStaticParams() {
  return Object.entries(manifest.topics).flatMap(([id, topics]) => topics.map((t) => ({ id, topic: t.n })));
}

export function generateMetadata({ params }: PageProps) {
  const mod = getModuleById(params.id);
  const topic = getTopic(params.id, params.topic);
  if (!mod || !topic) return { title: "Not Found" };
  return {
    title: `${topic.title} | W${mod.id} ${mod.titleTh} | ${course.code}`,
    description: `เนื้อหาเชิงลึกสัปดาห์ที่ ${mod.week}: ${topic.title}`,
  };
}

export default async function TopicPage({ params }: PageProps) {
  const mod = getModuleById(params.id);
  const topic = getTopic(params.id, params.topic);
  if (!mod || !topic) notFound();

  const markdown = await getTopicContent(params.id, params.topic);
  const topics = getTopics(params.id);
  const index = topics.findIndex((t) => t.n === params.topic);
  const prev = index > 0 ? topics[index - 1] : null;
  const next = index < topics.length - 1 ? topics[index + 1] : null;
  const colors = colorMap[mod.color] ?? colorMap.blue;

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 py-8">
      <nav className="flex items-center gap-2 text-sm text-gray-500 dark:text-gray-400 mb-6 flex-wrap">
        <Link href="/" className="hover:text-blue-600 dark:hover:text-blue-400 transition-colors">
          หน้าหลัก
        </Link>
        <span>/</span>
        <Link href={`/module/${mod.id}`} className="hover:text-blue-600 dark:hover:text-blue-400 transition-colors">
          สัปดาห์ที่ {mod.week}
        </Link>
        <span>/</span>
        <span className="text-gray-900 dark:text-white font-medium">หัวข้อ {topic.n}</span>
      </nav>

      <div className="mb-8">
        <div className={`inline-flex items-center gap-2 px-3 py-1 rounded-full ${colors.bg} ${colors.text} text-xs font-medium mb-3`}>
          <BookMarked className="w-3.5 h-3.5" />
          เนื้อหาเชิงลึก · สัปดาห์ที่ {mod.week} · หัวข้อที่ {Number(topic.n)}/{topics.length}
        </div>
        <h1 className="text-2xl md:text-3xl font-bold text-gray-900 dark:text-white mb-1">{topic.title}</h1>
        <p className="text-sm text-gray-500 dark:text-gray-400">
          {mod.titleTh} · {mod.clo.join(", ")}
        </p>
      </div>

      <div className="flex flex-wrap gap-2 mb-8">
        <Link
          href={`/module/${mod.id}`}
          className="inline-flex items-center gap-2 px-3 py-2 text-sm font-medium rounded-lg bg-blue-50 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300 border border-blue-200 dark:border-blue-800 hover:bg-blue-100 dark:hover:bg-blue-900/50 transition-colors"
        >
          <BookOpen className="w-4 h-4" /> กลับไปสัปดาห์ที่ {mod.week}
        </Link>
      </div>

      <div className="h-px bg-gray-200 dark:bg-gray-800 mb-8" />

      <article className="max-w-none">
        <MarkdownContent content={markdown} />
      </article>

      <div className="h-px bg-gray-200 dark:bg-gray-800 my-10" />

      <div className="flex flex-col sm:flex-row items-stretch gap-4">
        {prev ? (
          <Link
            href={`/module/${mod.id}/${prev.n}`}
            className="flex-1 group flex items-center gap-3 p-4 rounded-xl border border-gray-200 dark:border-gray-800 hover:border-indigo-300 dark:hover:border-indigo-700 hover:shadow-md transition-all"
          >
            <ArrowLeft className="w-5 h-5 text-gray-400 group-hover:text-indigo-500 transition-colors flex-shrink-0" />
            <div className="text-right flex-1">
              <p className="text-xs text-gray-400 dark:text-gray-500">ก่อนหน้า</p>
              <p className="text-sm font-medium text-gray-900 dark:text-white">
                {prev.n}. {prev.title}
              </p>
            </div>
          </Link>
        ) : (
          <div className="flex-1" />
        )}
        {next ? (
          <Link
            href={`/module/${mod.id}/${next.n}`}
            className="flex-1 group flex items-center gap-3 p-4 rounded-xl border border-gray-200 dark:border-gray-800 hover:border-indigo-300 dark:hover:border-indigo-700 hover:shadow-md transition-all"
          >
            <div className="flex-1">
              <p className="text-xs text-gray-400 dark:text-gray-500">ถัดไป</p>
              <p className="text-sm font-medium text-gray-900 dark:text-white">
                {next.n}. {next.title}
              </p>
            </div>
            <ArrowRight className="w-5 h-5 text-gray-400 group-hover:text-indigo-500 transition-colors flex-shrink-0" />
          </Link>
        ) : (
          <div className="flex-1" />
        )}
      </div>
    </div>
  );
}
