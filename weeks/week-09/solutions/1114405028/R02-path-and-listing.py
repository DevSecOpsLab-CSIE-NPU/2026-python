# R02. 路徑操作與目錄列舉（5.11 / 5.12 / 5.13）
# Bloom: Remember — 會用 pathlib 組路徑、檢查存在、列出檔案

import os
from pathlib import Path

# ── 5.11 組路徑：pathlib 是現代寫法 ────────────────────
# 使用 Path 物件可以像組字串一樣，用 / 連接各個路徑元件。
# 這種寫法比 os.path.join 更直觀，也會自動處理不同平台的分隔符。
base = Path("weeks") / "week-09"
print(base)              # 會輸出 weeks\week-09（Windows 會自動顯示反斜線）
print(base.name)         # 取得最後一個路徑名稱：week-09
print(base.parent)       # 取得父目錄：weeks
print(base.suffix)       # 取得副檔名；如果沒有副檔名，則空字串

# 另一個常見層級：檔名本體
f = Path("hello.txt")
print(f.stem, f.suffix)  # hello .txt

# 如果要和舊式程式碼兼容，還是可以用 os.path.join
print(os.path.join("weeks", "week-09", "README.md"))

# ── 5.12 存在判斷 ──────────────────────────────────────
# Path 提供 exists()/is_file()/is_dir() 來檢查是否存在，以及是檔案或目錄。
p = Path("hello.txt")
print(p.exists())    # 檔案是否存在
print(p.is_file())   # 是否為檔案
print(p.is_dir())    # 是否為目錄

missing = Path("no_such_file.txt")
if not missing.exists():
    print(f"{missing} 不存在，略過讀取")

# ── 5.13 列出資料夾內容 ────────────────────────────────
here = Path(".")

# os.listdir 會直接回傳當前目錄下的檔名清單（不含子目錄內容）
for name in os.listdir(here):
    print("listdir:", name)

# glob 會列出符合模式的檔案（當層）
for p in here.glob("*.py"):
    print("glob:", p)

# rglob 可以遞迴搜尋子目錄，抓出所有符合的檔案
for p in Path("..").rglob("*.py"):
    print("rglob:", p)
    break  # 示範用，只印第一個結果
