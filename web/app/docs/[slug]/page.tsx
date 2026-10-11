import { notFound } from "next/navigation";
import Link from "next/link";
import { FileText, Layers } from "lucide-react";
import { manifest, getDoc, getDocContent } from "@/lib/content";
import { course } from "@/lib/course";
import MarkdownContent from "@/components/MarkdownContent";

interface PageProps {
  params: { slug: string };
}

export function generateStaticParams() {
  return manifest.docs.map((d) => ({ slug: d.slug }));
}

export function generateMetadata({ params }: PageProps) {
  const d = getDoc(params.slug);
  if (!d) return { title: "Not Found" };
  return { title: `${d.title} | ${course.code}` };
}

export default async function DocPage({ params }: PageProps) {
  const d = getDoc(params.slug);
  if (!d) notFound();
  const markdown = await getDocContent(params.slug);
  const isTheme = d.group === "theme";

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 py-8">
      <nav className="flex items-center gap-2 text-sm text-gray-500 dark:text-gray-400 mb-6">
        <Link href="/" className="hover:text-blue-600 dark:hover:text-blue-400 transition-colors">
          หน้าหลัก
        </Link>
        <span>/</span>
        <span className="text-gray-900 dark:text-white font-medium">{d.title}</span>
      </nav>

      <div className="mb-8">
        <div
          className={`inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-medium mb-3 ${
            isTheme
              ? "bg-violet-50 dark:bg-violet-900/30 text-violet-700 dark:text-violet-300"
              : "bg-amber-50 dark:bg-amber-900/30 text-amber-700 dark:text-amber-300"
          }`}
        >
          {isTheme ? <Layers className="w-3.5 h-3.5" /> : <FileText className="w-3.5 h-3.5" />}
          {isTheme ? "ธีมตัดขวาง" : "เอกสารรายวิชา"}
        </div>
        <h1 className="text-2xl md:text-3xl font-bold text-gray-900 dark:text-white mb-1">{d.title}</h1>
        <p className="text-sm text-gray-500 dark:text-gray-400">
          {course.code} {course.titleTh}
        </p>
      </div>

      <div className="h-px bg-gray-200 dark:bg-gray-800 mb-8" />

      <article className="max-w-none">
        <MarkdownContent content={markdown} />
      </article>
    </div>
  );
}
