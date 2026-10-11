"use client";

import { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import {
  BookOpen,
  ChevronDown,
  ChevronRight,
  FileText,
  FlaskConical,
  ExternalLink,
  PenSquare,
  Presentation,
  BookMarked,
  Layers,
  ClipboardCheck,
} from "lucide-react";
import { modules, projects } from "@/lib/modules-data";
import { manifest } from "@/lib/manifest";

interface SidebarProps {
  isOpen: boolean;
  onClose: () => void;
}

function SidebarSection({
  title,
  icon,
  children,
  defaultOpen = false,
}: {
  title: string;
  icon: React.ReactNode;
  children: React.ReactNode;
  defaultOpen?: boolean;
}) {
  const [isOpen, setIsOpen] = useState(defaultOpen);

  return (
    <div className="mb-1">
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="flex items-center gap-2 w-full px-3 py-2 text-sm font-semibold text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg transition-colors"
      >
        {icon}
        <span className="flex-1 text-left">{title}</span>
        {isOpen ? <ChevronDown className="w-4 h-4" /> : <ChevronRight className="w-4 h-4" />}
      </button>
      {isOpen && <div className="ml-2 mt-0.5">{children}</div>}
    </div>
  );
}

function SidebarLink({
  href,
  label,
  isActive,
  external,
  onClick,
}: {
  href: string;
  label: string;
  isActive?: boolean;
  external?: boolean;
  onClick?: () => void;
}) {
  const baseClass = "flex items-center gap-2 px-3 py-1.5 text-[13px] rounded-lg transition-colors w-full";
  const activeClass = "bg-blue-50 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300 font-medium";
  const inactiveClass =
    "text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-800";

  if (external) {
    return (
      <a href={href} target="_blank" rel="noopener noreferrer" className={`${baseClass} ${inactiveClass}`} onClick={onClick}>
        <span className="truncate flex-1">{label}</span>
        <ExternalLink className="w-3 h-3 flex-shrink-0 opacity-50" />
      </a>
    );
  }

  return (
    <Link href={href} className={`${baseClass} ${isActive ? activeClass : inactiveClass}`} onClick={onClick}>
      <span className="truncate">{label}</span>
    </Link>
  );
}

export default function Sidebar({ isOpen, onClose }: SidebarProps) {
  const pathname = usePathname();
  const courseDocs = manifest.docs.filter((d) => d.group === "course");
  const themeDocs = manifest.docs.filter((d) => d.group === "theme");

  return (
    <>
      {isOpen && <div className="fixed inset-0 bg-black/40 z-40 lg:hidden" onClick={onClose} />}

      <aside
        className={`
          fixed top-14 bottom-0 left-0 z-40 w-72 bg-white dark:bg-gray-900
          border-r border-gray-200 dark:border-gray-800
          overflow-y-auto overscroll-contain
          transition-transform duration-300 ease-in-out
          lg:translate-x-0 lg:sticky lg:top-14 lg:h-[calc(100vh-3.5rem)]
          print:hidden
          ${isOpen ? "translate-x-0" : "-translate-x-full"}
        `}
      >
        <nav className="p-3 pb-20">
          <SidebarLink href="/" label="ภาพรวมรายวิชา" isActive={pathname === "/"} onClick={onClose} />
          <SidebarLink href="/docs/course-plan" label="🎯 แผนการสอนและ CLO" isActive={pathname === "/docs/course-plan"} onClick={onClose} />
          <SidebarLink href="/docs/assessment" label="📊 การวัดและประเมินผล" isActive={pathname === "/docs/assessment"} onClick={onClose} />
          <SidebarLink href="/docs/labs-projects" label="🧪 4 Mini-Projects" isActive={pathname === "/docs/labs-projects"} onClick={onClose} />
          <SidebarLink href="/exam-prep" label="🎓 แนวทางเตรียมสอบ" isActive={pathname === "/exam-prep"} onClick={onClose} />
          <SidebarLink href="/calc-examples" label="🧮 ตัวอย่างโจทย์คำนวณ" isActive={pathname === "/calc-examples"} onClick={onClose} />

          <div className="h-px bg-gray-200 dark:bg-gray-800 my-2" />

          <SidebarSection title="บทเรียนรายสัปดาห์ (17 สัปดาห์)" icon={<BookOpen className="w-4 h-4" />} defaultOpen>
            {modules.map((mod) => (
              <SidebarLink
                key={mod.id}
                href={`/module/${mod.id}`}
                label={`W${mod.id}. ${mod.titleTh}`}
                isActive={pathname === `/module/${mod.id}` || pathname.startsWith(`/module/${mod.id}/`)}
                onClick={onClose}
              />
            ))}
          </SidebarSection>

          <SidebarSection title="ใบงาน (Labs)" icon={<FlaskConical className="w-4 h-4" />}>
            {projects.map((p) => (
              <div key={p.id} className="mb-1">
                <p className="px-3 pt-2 pb-1 text-[11px] font-semibold uppercase tracking-wide text-gray-400 dark:text-gray-500">
                  {p.name}
                </p>
                {manifest.labs
                  .filter((l) => l.module === String(p.id))
                  .map((l) => (
                    <SidebarLink
                      key={l.id}
                      href={`/lab/${l.id}`}
                      label={`Lab ${l.id}: ${l.title}`}
                      isActive={pathname === `/lab/${l.id}`}
                      onClick={onClose}
                    />
                  ))}
              </div>
            ))}
          </SidebarSection>

          <SidebarSection title="สไลด์ประกอบการสอน" icon={<Presentation className="w-4 h-4" />}>
            <SidebarLink href="/slides" label="รวมสไลด์ทุกสัปดาห์" isActive={pathname === "/slides"} onClick={onClose} />
            {modules.map((mod) =>
              manifest.slides[mod.id]?.pptx ? (
                <SidebarLink
                  key={mod.id}
                  href={`/api/content/slides/${manifest.slides[mod.id].pptx}`}
                  label={`W${mod.id}: ${mod.titleTh}`}
                  external
                  onClick={onClose}
                />
              ) : null
            )}
          </SidebarSection>

          <SidebarSection title="แบบทบทวน (Review Sheets)" icon={<ClipboardCheck className="w-4 h-4" />}>
            {modules.map((mod) => (
              <SidebarLink
                key={mod.id}
                href={`/api/content/SHEET/review_sheet_${mod.id}.html`}
                label={`Review W${mod.id}: ${mod.titleTh}`}
                external
                onClick={onClose}
              />
            ))}
          </SidebarSection>

          <SidebarSection title="แบบทดสอบ (Quizzes)" icon={<PenSquare className="w-4 h-4" />}>
            {modules
              .filter((m) => m.hasExam)
              .map((mod) => (
                <SidebarLink
                  key={mod.id}
                  href={`/exam/${mod.id}`}
                  label={`Quiz W${mod.id}: ${mod.titleTh}`}
                  isActive={pathname === `/exam/${mod.id}`}
                  onClick={onClose}
                />
              ))}
          </SidebarSection>

          <div className="h-px bg-gray-200 dark:bg-gray-800 my-2" />

          <SidebarSection title="พจนานุกรมศัพท์ (Concepts)" icon={<BookMarked className="w-4 h-4" />}>
            <SidebarLink href="/concepts" label="ดูศัพท์ทั้งหมด" isActive={pathname === "/concepts"} onClick={onClose} />
            {manifest.concepts.map((c) => (
              <SidebarLink
                key={c.slug}
                href={`/concept/${c.slug}`}
                label={c.title}
                isActive={pathname === `/concept/${c.slug}`}
                onClick={onClose}
              />
            ))}
          </SidebarSection>

          <SidebarSection title="ธีมตัดขวาง (Themes)" icon={<Layers className="w-4 h-4" />}>
            {themeDocs.map((d) => (
              <SidebarLink key={d.slug} href={`/docs/${d.slug}`} label={d.title} isActive={pathname === `/docs/${d.slug}`} onClick={onClose} />
            ))}
          </SidebarSection>

          <SidebarSection title="เอกสารรายวิชา" icon={<FileText className="w-4 h-4" />}>
            {courseDocs.map((d) => (
              <SidebarLink key={d.slug} href={`/docs/${d.slug}`} label={d.title} isActive={pathname === `/docs/${d.slug}`} onClick={onClose} />
            ))}
            <SidebarLink href="https://www.acm.org/binaries/content/assets/education/ce2016-final-report.pdf" label="ACM/IEEE CE2016" external onClick={onClose} />
            <SidebarLink href="https://www.acm.org/code-of-ethics" label="ACM Code of Ethics" external onClick={onClose} />
            <SidebarLink href="https://csrc.nist.gov/pubs/sp/800/207/final" label="NIST SP 800-207 Zero Trust" external onClick={onClose} />
            <SidebarLink href="https://owasp.org/www-project-top-ten/" label="OWASP Top 10" external onClick={onClose} />
            <SidebarLink href="https://mqtt.org/" label="MQTT.org" external onClick={onClose} />
            <SidebarLink href="https://riscv.org/" label="RISC-V International" external onClick={onClose} />
          </SidebarSection>
        </nav>
      </aside>
    </>
  );
}
