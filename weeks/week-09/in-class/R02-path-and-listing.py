# R02. 路徑操作與目錄列舉（5.11 / 5.12 / 5.13）
# Bloom: Remember — 會用 pathlib 組路徑、檢查存在、列出檔案

import os
from pathlib import Path

# ── 5.11 組路徑：pathlib 是現代寫法 ────────────────────
base = Path("weeks") / "week-09"
print(base)              # weeks/week-09（Windows 會自動變成反斜線）
print(base.name)         # week-09
print(base.parent)       # weeks
print(base.suffix)       # ''（無副檔名）

f = Path("hello.txt")
print(f.stem, f.suffix)  # hello .txt

# 相容舊寫法：os.path.join
print(os.path.join("weeks", "week-09", "README.md"))

# ── 5.12 存在判斷 ──────────────────────────────────────
p = Path("hello.txt")
print(p.exists())    # 是否存在
print(p.is_file())   # 是否是檔案
print(p.is_dir())    # 是否是資料夾

missing = Path("no_such_file.txt")
if not missing.exists():
    print(f"{missing} 不存在，略過讀取")

# ── 5.13 列出資料夾內容 ────────────────────────────────
here = Path(".")

# 只列當層
for name in os.listdir(here):
    print("listdir:", name)

# 只抓 .py（當層）
for p in here.glob("*.py"):
    print("glob:", p)

# 遞迴抓所有 .py（含子資料夾）
for p in Path("..").rglob("*.py"):
    print("rglob:", p)
    break  # 示範用，只印第一個
