# Weekly Slide Decks — EN-001-019

ชุดสไลด์ความรู้รายสัปดาห์สำหรับรายวิชา **EN-001-019 แก่นวิศวกรรมคอมพิวเตอร์** สร้างจากเนื้อหาใน `wiki/timeline/`

## โครงสร้างไฟล์

- `Week XX - .../*.pptx` — ไฟล์ PowerPoint รายสัปดาห์
- `Week XX - .../* - preview.webp` — ภาพ preview ของ deck
- `_qa/week-XX/*.png` และ `*.layout.json` — ไฟล์ตรวจสอบการ render/layout
- `manifest.json` — รายการ deck ทั้งหมดแบบ machine-readable

## วิธี regenerate

รันสคริปต์:

```powershell
node scripts/build_week_slides.mjs
```

หมายเหตุ: สคริปต์ต้องรันใน environment ที่มี `@oai/artifact-tool` ตาม runtime ของ Codex presentations skill
