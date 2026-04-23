# R02. 路徑操作與目錄列舉
# 主題：pathlib 路徑組合、檔案存在檢查、listdir/glob/rglob 差異

import os
from pathlib import Path

# ── 1) 組路徑與拆解屬性（對應 5.11） ─────────────────
# pathlib 寫法：用 / 來組路徑，跨作業系統更直觀
base = Path("weeks") / "week-09"
print(base)        # 例：weeks/week-09（Windows 會顯示為反斜線）
print(base.name)   # 最後一節名稱：week-09
print(base.parent) # 上一層：weeks
print(base.suffix) # 副檔名（資料夾通常是空字串）

f = Path("hello.txt")
print(f.stem, f.suffix)  # stem=檔名本體, suffix=副檔名

# 舊式但常見寫法：os.path.join
print(os.path.join("weeks", "week-09", "README.md"))

# ── 2) 路徑存在與型態檢查（對應 5.12） ───────────────
p = Path("hello.txt")
print(p.exists())   # 路徑是否存在
print(p.is_file())  # 是否為檔案
print(p.is_dir())   # 是否為資料夾

missing = Path("no_such_file.txt")
if not missing.exists():
    # 實務上先檢查再讀，避免 FileNotFoundError
    print(f"{missing} 不存在，略過讀取")

# ── 3) 列出資料夾內容（對應 5.13） ────────────────────
here = Path(".")

# A. os.listdir：只列「當前層」名稱，不會遞迴
for name in os.listdir(here):
    print("listdir:", name)

# B. Path.glob('*.py')：只抓當前層符合樣式的檔案
for p in here.glob("*.py"):
    print("glob:", p)

# C. Path.rglob('*.py')：遞迴搜尋子資料夾
for p in Path("..").rglob("*.py"):
    print("rglob:", p)
    break  # 示範用：避免輸出過長，只印第一筆
