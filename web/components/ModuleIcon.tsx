import {
  BrainCircuit,
  Building2,
  CircuitBoard,
  ClipboardList,
  Code2,
  Compass,
  Cpu,
  Database,
  GraduationCap,
  Network,
  Presentation,
  Radio,
  Scale,
  Server,
  ShieldCheck,
  Sparkles,
  Workflow,
  type LucideIcon,
} from "lucide-react";

const ICONS: Record<string, LucideIcon> = {
  BrainCircuit,
  Building2,
  CircuitBoard,
  ClipboardList,
  Code2,
  Compass,
  Cpu,
  Database,
  GraduationCap,
  Network,
  Presentation,
  Radio,
  Scale,
  Server,
  ShieldCheck,
  Sparkles,
  Workflow,
};

export default function ModuleIcon({ name, className }: { name: string; className?: string }) {
  const Icon = ICONS[name] ?? Compass;
  return <Icon className={className} />;
}
