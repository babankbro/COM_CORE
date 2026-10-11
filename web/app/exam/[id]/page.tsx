import { notFound } from "next/navigation";
import { modules, getModuleById } from "@/lib/modules-data";
import { getExam } from "@/lib/content";
import { course } from "@/lib/course";
import ExamClient from "@/components/ExamClient";

interface PageProps {
  params: { id: string };
}

export function generateStaticParams() {
  return modules.filter((m) => m.hasExam).map((mod) => ({ id: mod.id }));
}

export function generateMetadata({ params }: PageProps) {
  const mod = getModuleById(params.id);
  if (!mod) return {};
  return {
    title: `แบบทดสอบ W${mod.id}: ${mod.titleTh} | ${course.code}`,
    description: `แบบทดสอบประจำสัปดาห์ที่ ${mod.week} - ${mod.titleTh}`,
  };
}

export default async function ExamPage({ params }: PageProps) {
  const mod = getModuleById(params.id);
  if (!mod || !mod.hasExam) notFound();

  const exam = await getExam(params.id);
  if (!exam) notFound();

  return <ExamClient exam={exam} moduleTitleTh={mod.titleTh} />;
}
