# Computer Engineering Essentials: LLM Wiki

Mode: Mode F (Course notes wiki)
Purpose: 17-week study plan and knowledge base for EN-001-019 Computer Engineering Essentials
Owner: Student / Instructor
Created: 2026-06-30

## Structure

vault/
├── .raw/              # chapter notes, highlights, exercises, references
├── wiki/
│   ├── characters/    # experts, AI Agents, personas
│   ├── themes/        # major themes (AI, Hardware, Security)
│   ├── concepts/      # domain-specific terms and frameworks
│   ├── timeline/      # 17-week curriculum sequence
│   └── synthesis/     # takeaways, notes, applications
├── _meta/
│   ├── index.md       # Master index of the vault
│   └── log.md         # Chronological record of changes
└── CLAUDE.md

## Conventions

- All notes use YAML frontmatter: type, status, created, updated, tags (minimum)
- Wikilinks use [[Note Name]] format: filenames are unique, no paths needed
- .raw/ contains source documents: never modify them
- wiki/index.md is the master catalog: update on every ingest
- wiki/log.md is append-only: never edit past entries
- New log entries go at the TOP of the file

## Operations

- Ingest: drop source in .raw/, say "ingest [filename]"
- Query: ask any question: Claude reads index first, then drills in
- Lint: say "lint the wiki" to run a health check
- Archive: move cold sources to .archive/ to keep .raw/ clean

## Website (web/)

- `web/` is a Next.js 14 e-learning site (same style as EN-012-314-AI) generated from this vault
- `cd web && npm run content` rebuilds `web/content/` from `wiki/` and `slides/`; `npm run check` validates
- Quizzes live in `web/content/exams/exam-XX.json` and are hand-written (not regenerated)
- Week metadata (titles, CLO, icons) in `web/lib/modules-data.ts`; see `web/README.md`
