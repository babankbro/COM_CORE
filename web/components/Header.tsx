"use client";

import { useState, useEffect, useMemo } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { Menu, Moon, Sun, Cpu, Search, X, ExternalLink } from "lucide-react";
import { modules } from "@/lib/modules-data";
import { course } from "@/lib/course";
import { manifest } from "@/lib/manifest";

interface HeaderProps {
  onMenuToggle: () => void;
}

interface SearchItem {
  kind: "module" | "topic" | "lab" | "concept";
  badge: string;
  title: string;
  sub: string;
  href: string;
  haystack: string;
}

function buildIndex(): SearchItem[] {
  const items: SearchItem[] = [];
  for (const m of modules) {
    items.push({
      kind: "module",
      badge: `W${m.id}`,
      title: m.titleTh,
      sub: m.titleEn,
      href: `/module/${m.id}`,
      haystack: [m.titleTh, m.titleEn, m.description, ...m.topics, m.id].join(" ").toLowerCase(),
    });
    for (const t of manifest.topics[m.id] ?? []) {
      items.push({
        kind: "topic",
        badge: `${m.id}.${t.n}`,
        title: t.title,
        sub: `เนื้อหาเชิงลึก · สัปดาห์ที่ ${m.week}`,
        href: `/module/${m.id}/${t.n}`,
        haystack: `${t.title} ${m.titleTh}`.toLowerCase(),
      });
    }
  }
  for (const l of manifest.labs) {
    items.push({
      kind: "lab",
      badge: `Lab ${l.id}`,
      title: l.title,
      sub: `ใบงาน · Mini-Project ${l.module}`,
      href: `/lab/${l.id}`,
      haystack: `lab ${l.id} ${l.title}`.toLowerCase(),
    });
  }
  for (const c of manifest.concepts) {
    items.push({
      kind: "concept",
      badge: "ศัพท์",
      title: c.title,
      sub: c.definition.slice(0, 80),
      href: `/concept/${c.slug}`,
      haystack: `${c.title} ${c.name} ${c.definition}`.toLowerCase(),
    });
  }
  return items;
}

const BADGE_CLASS: Record<SearchItem["kind"], string> = {
  module: "text-blue-600 dark:text-blue-400 bg-blue-50 dark:bg-blue-900/30",
  topic: "text-indigo-600 dark:text-indigo-400 bg-indigo-50 dark:bg-indigo-900/30",
  lab: "text-green-600 dark:text-green-400 bg-green-50 dark:bg-green-900/30",
  concept: "text-orange-600 dark:text-orange-400 bg-orange-50 dark:bg-orange-900/30",
};

export default function Header({ onMenuToggle }: HeaderProps) {
  const [isDark, setIsDark] = useState(false);
  const [searchOpen, setSearchOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState("");
  const router = useRouter();
  const index = useMemo(buildIndex, []);

  const searchResults = useMemo(() => {
    const q = searchQuery.trim().toLowerCase();
    if (!q) return [];
    return index.filter((i) => i.haystack.includes(q)).slice(0, 10);
  }, [index, searchQuery]);

  useEffect(() => {
    setIsDark(document.documentElement.classList.contains("dark"));
  }, []);

  function toggleTheme() {
    const next = !isDark;
    setIsDark(next);
    document.documentElement.classList.toggle("dark", next);
    try {
      localStorage.setItem("theme", next ? "dark" : "light");
    } catch {
      // storage ถูกปิด — ใช้ธีมได้เฉพาะรอบนี้
    }
  }

  function closeSearch() {
    setSearchOpen(false);
    setSearchQuery("");
  }

  function handleResultClick(href: string) {
    closeSearch();
    router.push(href);
  }

  useEffect(() => {
    function onKeyDown(e: KeyboardEvent) {
      if ((e.ctrlKey || e.metaKey) && e.key === "k") {
        e.preventDefault();
        setSearchOpen(true);
        document.getElementById("site-search")?.focus();
      }
      if (e.key === "Escape") closeSearch();
    }
    document.addEventListener("keydown", onKeyDown);
    return () => document.removeEventListener("keydown", onKeyDown);
  }, []);

  const resultList = (
    <>
      {searchResults.map((item) => (
        <button
          key={item.href}
          onMouseDown={(e) => e.preventDefault()}
          onClick={() => handleResultClick(item.href)}
          className="w-full flex items-center gap-3 px-4 py-2.5 text-left hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors"
        >
          <span className={`text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap ${BADGE_CLASS[item.kind]}`}>
            {item.badge}
          </span>
          <div className="min-w-0">
            <p className="text-sm font-medium text-gray-900 dark:text-white truncate">{item.title}</p>
            <p className="text-xs text-gray-500 dark:text-gray-400 truncate">{item.sub}</p>
          </div>
        </button>
      ))}
    </>
  );

  return (
    <header className="fixed top-0 left-0 right-0 z-50 h-14 bg-white/80 dark:bg-gray-900/80 backdrop-blur-lg border-b border-gray-200 dark:border-gray-800 print:hidden">
      <div className="flex items-center justify-between h-full px-4">
        <div className="flex items-center gap-3">
          <button
            onClick={onMenuToggle}
            className="lg:hidden p-2 -ml-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
            aria-label="Toggle menu"
          >
            <Menu className="w-5 h-5" />
          </button>

          <Link href="/" className="flex items-center gap-2.5">
            <div className="w-8 h-8 bg-gradient-to-br from-blue-600 to-cyan-500 rounded-lg flex items-center justify-center shadow-sm">
              <Cpu className="w-4 h-4 text-white" />
            </div>
            <div className="hidden sm:block leading-tight">
              <span className="block text-sm font-semibold text-gray-900 dark:text-white">{course.titleEn}</span>
              <span className="block text-[11px] text-gray-500 dark:text-gray-400">
                {course.code} · {course.titleTh}
              </span>
            </div>
          </Link>
        </div>

        <div className="flex-1 max-w-md mx-4 hidden md:block">
          <div className="relative">
            <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" />
            <input
              id="site-search"
              type="text"
              placeholder="ค้นหาบทเรียน หัวข้อ ใบงาน หรือศัพท์... (Ctrl+K)"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              onFocus={() => setSearchOpen(true)}
              onBlur={() => setTimeout(() => setSearchOpen(false), 150)}
              className="w-full pl-9 pr-4 py-2 text-sm rounded-lg border border-gray-200 dark:border-gray-700 bg-gray-50 dark:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
            />
            {searchOpen && searchResults.length > 0 && (
              <div className="absolute top-full left-0 right-0 mt-1 bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-700 rounded-lg shadow-lg overflow-hidden z-50 max-h-[70vh] overflow-y-auto">
                {resultList}
              </div>
            )}
          </div>
        </div>

        <div className="flex items-center gap-1.5">
          <button
            onClick={() => setSearchOpen(!searchOpen)}
            className="md:hidden p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
            aria-label="Search"
          >
            <Search className="w-5 h-5" />
          </button>

          <a
            href="https://github.com/"
            target="_blank"
            rel="noopener noreferrer"
            className="hidden sm:flex items-center gap-1.5 px-3 py-1.5 text-sm font-medium rounded-lg text-gray-700 dark:text-gray-300 bg-gray-100 dark:bg-gray-800 hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors"
          >
            <ExternalLink className="w-4 h-4" />
            <span>GitHub</span>
          </a>

          <button
            onClick={toggleTheme}
            className="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
            aria-label="Toggle theme"
          >
            {isDark ? <Sun className="w-5 h-5" /> : <Moon className="w-5 h-5" />}
          </button>
        </div>
      </div>

      {searchOpen && (
        <div className="md:hidden border-t border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 p-3">
          <div className="relative">
            <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" />
            <input
              type="text"
              placeholder="ค้นหาบทเรียน..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              autoFocus
              className="w-full pl-9 pr-10 py-2.5 text-sm rounded-lg border border-gray-200 dark:border-gray-700 bg-gray-50 dark:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
            />
            <button
              onClick={closeSearch}
              className="absolute right-2 top-1/2 -translate-y-1/2 p-1 rounded hover:bg-gray-200 dark:hover:bg-gray-700"
              aria-label="Close search"
            >
              <X className="w-4 h-4" />
            </button>
          </div>
          {searchResults.length > 0 && (
            <div className="mt-2 border border-gray-200 dark:border-gray-700 rounded-lg overflow-hidden">{resultList}</div>
          )}
        </div>
      )}
    </header>
  );
}
