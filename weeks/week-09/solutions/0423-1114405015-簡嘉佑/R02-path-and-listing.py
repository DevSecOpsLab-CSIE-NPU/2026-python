"""
R02. 路徑操作與目錄列舉（5.11 / 5.12 / 5.13）
Bloom: Remember

本檔重點：
1) 用 pathlib 進行路徑組合與屬性查詢。
2) 檢查檔案/資料夾是否存在。
3) 使用 listdir、glob、rglob 列舉檔案。
"""

import os
from pathlib import Path

# ── 5.11 組路徑：pathlib 是現代寫法 ────────────────────
# Path 物件可用 / 直接串接路徑片段，跨平台可攜。
base = Path("weeks") / "week-09"
print(base)              # weeks/week-09（Windows 會自動變成反斜線）
print(base.name)         # week-09
print(base.parent)       # weeks
print(base.suffix)       # ''（無副檔名）

# 對檔案路徑來說，stem 是主檔名、suffix 是副檔名
f = Path("hello.txt")
print(f.stem, f.suffix)  # hello .txt

# 相容舊寫法：os.path.join（舊專案常見）
print(os.path.join("weeks", "week-09", "README.md"))

# ── 5.12 存在判斷 ──────────────────────────────────────
# exists/is_file/is_dir 是最常用的三個檢查。
p = Path("hello.txt")
print(p.exists())    # 是否存在
print(p.is_file())   # 是否是檔案
print(p.is_dir())    # 是否是資料夾

missing = Path("no_such_file.txt")
if not missing.exists():
    print(f"{missing} 不存在，略過讀取")

# ── 5.13 列出資料夾內容 ────────────────────────────────
# listdir 只列當層名稱；glob/rglob 可直接做樣式過濾。
here = Path(".")

# 只列當層
for name in os.listdir(here):
    print("listdir:", name)

# 只抓 .py（當層，不含子資料夾）
for p in here.glob("*.py"):
    print("glob:", p)

# 遞迴抓所有 .py（含子資料夾）
for p in Path("..").rglob("*.py"):
    print("rglob:", p)
    break  # 示範用，只印第一個
