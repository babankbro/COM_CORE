"""รันสคริปต์ infographic รายสัปดาห์ทั้งหมด (scripts/figures/wXX.py) → public/images/weeks/
รัน: python scripts/make_week_figures.py [01 02 ...]   (ต้องมีฟอนต์ Prompt)
"""
import runpy
import sys
from pathlib import Path

FIG_DIR = Path(__file__).resolve().parent / "figures"
sys.path.insert(0, str(FIG_DIR))
weeks = sys.argv[1:] or [p.stem[1:] for p in sorted(FIG_DIR.glob("w[0-9][0-9].py"))]
for w in weeks:
    runpy.run_path(str(FIG_DIR / f"w{w}.py"), run_name="__main__")
