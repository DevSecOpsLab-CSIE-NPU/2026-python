# R02. 路徑操作與目錄列舉（5.11 / 5.12 / 5.13）
# Bloom: Remember — 會用 pathlib 組路徑、檢查存在、列出檔案

import os
from pathlib import Path

# ── 5.11 組路徑：pathlib 是現代寫法 ────────────────────
# Path 物件可以用 / 運算子安全地組合路徑，會自動處理不同作業系統的分隔符
base = Path("weeks") / "week-09"
print(base)              # weeks/week-09（Windows 會自動變成反斜線）
print(base.name)         # 檔案或資料夾名稱，不含上層路徑
print(base.parent)       # 上一層路徑
print(base.suffix)       # 副檔名，若沒有副檔名則是空字串

f = Path("hello.txt")
print(f.stem, f.suffix)  # stem = hello, suffix = .txt

# 舊式寫法：os.path.join 也能組路徑，但 pathlib 更直觀
print(os.path.join("weeks", "week-09", "README.md"))

# ── 5.12 存在判斷 ──────────────────────────────────────
# Path.exists() 會檢查路徑是否存在，Path.is_file() 會檢查是否為檔案，
# Path.is_dir() 會檢查是否為資料夾
p = Path("hello.txt")
print(p.exists())    # 檔案或資料夾是否存在
print(p.is_file())   # 是否存在且為檔案
print(p.is_dir())    # 是否存在且為資料夾

missing = Path("no_such_file.txt")
if not missing.exists():
    # 讀檔之前先檢查存在性，可以避免 FileNotFoundError
    print(f"{missing} 不存在，略過讀取")

# ── 5.13 列出資料夾內容 ────────────────────────────────
here = Path(".")

# os.listdir() 只會列出當層項目名稱，不會回傳完整路徑
for name in os.listdir(here):
    print("listdir:", name)

# pathlib.Path.glob() 可以列出符合模式的檔案，僅限當層目錄
# return Path 物件，可直接用於後續操作
for p in here.glob("*.py"):
    print("glob:", p)

# pathlib.Path.rglob() 會遞迴搜尋子目錄，可抓到所有子目錄中的檔案
for p in Path("..").rglob("*.py"):
    print("rglob:", p)
    break  # 示範用，只印第一個結果，避免列出太多
