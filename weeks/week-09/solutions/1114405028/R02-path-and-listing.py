# R02-path-and-listing.py
# 完整繁體中文註釋版：示範 pathlib 路徑操作、存在判斷與目錄列舉

import os
from pathlib import Path

# ── 5.11 組路徑：pathlib 是現代寫法 ────────────────────
base = Path("weeks") / "week-09"
# Path 物件可直接用 / 連接，會自動處理平台分隔符
print(base)              # windows 會顯示反斜線
print(base.name)         # 取得最後一層資料夾名稱
print(base.parent)       # 取得上層資料夾
print(base.suffix)       # 取得副檔名，資料夾沒有副檔名

f = Path("hello.txt")
print(f.stem, f.suffix)  # 取得檔名前綴與副檔名

# 這是舊式 os.path.join 寫法，仍然可以使用
print(os.path.join("weeks", "week-09", "README.md"))

# ── 5.12 存在判斷 ──────────────────────────────────────
p = Path("hello.txt")
print(p.exists())    # 檢查路徑是否存在
print(p.is_file())   # 是否為檔案
print(p.is_dir())    # 是否為資料夾

missing = Path("no_such_file.txt")
if not missing.exists():
    print(f"{missing} 不存在，略過讀取")

# ── 5.13 列出資料夾內容 ────────────────────────────────
here = Path(".")

# os.listdir 只列出當前資料夾的檔名/目錄名
for name in os.listdir(here):
    print("listdir:", name)

# glob 會依據模式列出當層符合條件的檔案
for p in here.glob("*.py"):
    print("glob:", p)

# rglob 會遞迴搜尋子資料夾中所有符合的檔案
for p in Path("..").rglob("*.py"):
    print("rglob:", p)
    break  # 示範用，只列出第一個結果
