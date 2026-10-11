import { notFound } from "next/navigation";
import Link from "next/link";
import { BookMarked } from "lucide-react";
import { manifest, getConcept, getConceptContent } from "@/lib/content";
import { getModuleById } from "@/lib/modules-data";
import { course } from "@/lib/course";
import MarkdownContent from "@/components/MarkdownContent";

interface PageProps {
  params: { slug: string };
}

export function generateStaticParams() {
  return manifest.concepts.map((c) => ({ slug: c.slug }));
}

export function generateMetadata({ params }: PageProps) {
  const c = getConcept(params.slug);
  if (!c) return { title: "Not Found" };
  return { title: `${c.title} | ศัพท์ | ${course.code}`, description: c.definition };
}

export default async function ConceptPage({ params }: PageProps) {
  const c = getConcept(params.slug);
  if (!c) notFound();
  const markdown = await getConceptContent(params.slug);

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 py-8">
      <nav className="flex items-center gap-2 text-sm text-gray-500 dark:text-gray-400 mb-6">
        <Link href="/" className="hover:text-blue-600 dark:hover:text-blue-400 transition-colors">
          หน้าหลัก
        </Link>
        <span>/</span>
        <Link href="/concepts" className="hover:text-blue-600 dark:hover:text-blue-400 transition-colors">
          พจนานุกรมศัพท์
        </Link>
        <span>/</span>
        <span className="text-gray-900 dark:text-white font-medium">{c.name}</span>
      </nav>

      <div className="mb-8">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-orange-50 dark:bg-orange-900/30 text-orange-700 dark:text-orange-300 text-xs font-medium mb-3">
          <BookMarked className="w-3.5 h-3.5" /> Concept
        </div>
        <h1 className="text-2xl md:text-3xl font-bold text-gray-900 dark:text-white mb-2">{c.title}</h1>
        {c.weeks.length > 0 && (
          <div className="flex flex-wrap gap-2">
            {c.weeks.map((w) => {
              const mod = getModuleById(w);
              return (
                <Link
                  key={w}
                  href={`/module/${w}`}
                  className="text-xs px-2.5 py-1 rounded-full bg-gray-100 dark:bg-gray-800 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-700"
                >
                  W{Number(w)}: {mod?.titleTh ?? ""}
                </Link>
              );
            })}
          </div>
        )}
      </div>

      <div className="h-px bg-gray-200 dark:bg-gray-800 mb-8" />

      <article className="max-w-none">
        <MarkdownContent content={markdown} />
      </article>
    </div>
  );
}
