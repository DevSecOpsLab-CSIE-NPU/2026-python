"""R02. 路徑操作與目錄列舉（5.11 / 5.12 / 5.13）

Bloom: Remember
學習目標：會用 pathlib 進行路徑組合、檔案存在判斷、與目錄列舉。

本檔重點：
1) 用 pathlib.Path 以物件方式操作路徑（可讀性高、跨平台）
2) 用 exists()/is_file()/is_dir() 做安全檢查
3) 用 listdir()/glob()/rglob() 列出目錄內容

觀念補充：
- pathlib 會依作業系統自動處理分隔符（Windows 的 \\、Unix 的 /）。
- 在讀檔前先判斷檔案存在，可避免 FileNotFoundError。
- rglob("*.py") 會遞迴搜尋，專案大時可能回傳很多結果。
"""

import os
from pathlib import Path

# ── 5.11 組路徑：pathlib 是現代寫法 ────────────────────
# Path 物件可用 / 直接組路徑，比字串串接更安全、清楚
base = Path("weeks") / "week-09"
print(base)              # weeks/week-09（Windows 會自動變成反斜線）
print(base.name)         # week-09
print(base.parent)       # weeks
print(base.suffix)       # ''（無副檔名）

# stem = 去掉副檔名後的檔名；suffix = 副檔名
f = Path("hello.txt")
print(f.stem, f.suffix)  # hello .txt

# 相容舊寫法：os.path.join
print(os.path.join("weeks", "week-09", "README.md"))

# ── 5.12 存在判斷 ──────────────────────────────────────
p = Path("hello.txt")
print(p.exists())    # 是否存在
print(p.is_file())   # 是否是檔案
print(p.is_dir())    # 是否是資料夾

# 實務上常見：不存在就略過，避免直接讀檔報錯
missing = Path("no_such_file.txt")
if not missing.exists():
    print(f"{missing} 不存在，略過讀取")

# ── 5.13 列出資料夾內容 ────────────────────────────────
here = Path(".")

# 只列當層
# os.listdir() 回傳名稱字串，不含完整路徑
for name in os.listdir(here):
    print("listdir:", name)

# 只抓 .py（當層）
# glob() 不遞迴，只找目前目錄
for p in here.glob("*.py"):
    print("glob:", p)

# 遞迴抓所有 .py（含子資料夾）
# rglob() 會往下搜尋子目錄，適合做專案掃描
for p in Path("..").rglob("*.py"):
    print("rglob:", p)
    break  # 示範用，只印第一個
