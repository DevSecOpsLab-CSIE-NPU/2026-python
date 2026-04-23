# R02. 路徑操作與目錄列舉（5.11 / 5.12 / 5.13）
# Bloom: Remember — 會用 pathlib 組路徑、檢查存在、列出檔案

import os
from pathlib import Path

# ── 5.11 組路徑：pathlib 是現代寫法 ────────────────────
# Path 物件會依作業系統自動使用正確分隔符，
# 使用 / 運算子串接路徑可讀性高，也能避免手動拼字串出錯。
base = Path("weeks") / "week-09"
print(base)              # weeks/week-09（Windows 會自動變成反斜線）
# .name：最後一層名稱（不含前面的路徑）
print(base.name)         # week-09
# .parent：上一層路徑
print(base.parent)       # weeks
# .suffix：副檔名（含點），資料夾通常為空字串
print(base.suffix)       # ''（無副檔名）

f = Path("hello.txt")
# .stem：檔名主體（不含副檔名）
# .suffix：副檔名（例如 .txt、.py）
print(f.stem, f.suffix)  # hello .txt

# 相容舊寫法：os.path.join
# 舊專案常見 os.path；若在新程式中，通常優先使用 pathlib。
print(os.path.join("weeks", "week-09", "README.md"))

# ── 5.12 存在判斷 ──────────────────────────────────────
p = Path("hello.txt")
# exists()：不分檔案/資料夾，只判斷路徑是否存在
print(p.exists())    # 是否存在
# is_file()：存在且是檔案才會 True
print(p.is_file())   # 是否是檔案
# is_dir()：存在且是資料夾才會 True
print(p.is_dir())    # 是否是資料夾

missing = Path("no_such_file.txt")
# 讀檔前先檢查 exists() 是常見防呆手法，可避免 FileNotFoundError。
if not missing.exists():
    print(f"{missing} 不存在，略過讀取")

# ── 5.13 列出資料夾內容 ────────────────────────────────
# Path('.') 代表目前工作目錄（current working directory）
here = Path(".")

# 只列當層
# os.listdir() 回傳名稱字串，不含完整路徑。
# 若需要更多檔案屬性或路徑操作能力，pathlib 通常更方便。
for name in os.listdir(here):
    print("listdir:", name)

# 只抓 .py（當層）
# glob('*.py')：只在目前這一層比對，不會往子資料夾走。
for p in here.glob("*.py"):
    print("glob:", p)

# 遞迴抓所有 .py（含子資料夾）
# rglob('*.py')：recursive glob，會遞迴進入所有子目錄。
# 專案大時結果可能很多，實務上常搭配條件過濾或限制輸出數量。
for p in Path("..").rglob("*.py"):
    print("rglob:", p)
    break  # 示範用，只印第一個
