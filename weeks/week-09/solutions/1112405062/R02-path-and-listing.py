# R02. 路徑操作與目錄列舉（5.11 / 5.12 / 5.13）
# Bloom: Remember — 會用 pathlib 組路徑、檢查存在、列出檔案
# 本範例介紹 Python 中路徑操作與目錄列舉的相關功能

import os
from pathlib import Path

# ── 5.11 組路徑：pathlib 是現代寫法 ────────────────────
#  Path 物件使用 / 運算子來組合路徑，自動處理不同作業系統的路徑分隔符
base = Path("weeks") / "week-09"
print(base)              # weeks/week-09（Windows 會自動變成反斜線）
print(base.name)         # 取得路徑的最後一部分：week-09
print(base.parent)       # 取得上層目錄：weeks
print(base.suffix)      # 取得副檔名（無副檔名則為空字串）：''

f = Path("hello.txt")
print(f.stem, f.suffix)  # hello（檔名） .txt（副檔名）

# 相容舊寫法：os.path.join
#  使用 os.path.join 來組合路徑（舊式寫法）
print(os.path.join("weeks", "week-09", "README.md"))

# ── 5.12 存在判斷 ──────────────────────────────────────
#  Path 物件提供多種方法來檢查路徑的狀態
p = Path("hello.txt")
print(p.exists())    # 檢查路徑是否存在（回傳布林值）
print(p.is_file())   # 檢查是否為檔案
print(p.is_dir())    # 檢查是否為目錄（資料夾）

missing = Path("no_such_file.txt")
if not missing.exists():
    print(f"{missing} 不存在，略過讀取")

# ── 5.13 列出資料夾內容 ────────────────────────────────
#  os.listdir 與 pathlib 的 glob 方法可用來列舉目錄內容
here = Path(".")

# 列出當前目錄的所有檔案與子目錄（不含子目錄內容）
for name in os.listdir(here):
    print("listdir:", name)

# 使用 glob 取得符合模式的檔案（只搜尋當層目錄）
for p in here.glob("*.py"):
    print("glob:", p)

# 使用 rglob 遞迴搜尋所有符合模式的檔案（含子目錄）
for p in Path("..").rglob("*.py"):
    print("rglob:", p)
    break  # 示範用，只印第一個