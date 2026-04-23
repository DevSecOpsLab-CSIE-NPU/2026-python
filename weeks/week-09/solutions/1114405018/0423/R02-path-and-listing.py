# R02. 路徑操作與目錄列舉（5.11 / 5.12 / 5.13）
# Bloom: Remember — 會用 pathlib 組路徑、檢查存在、列出檔案

# os: 傳統作業系統介面工具（像是 os.path、listdir）
# pathlib.Path: 現代路徑物件寫法，語意清楚、跨平台更直覺
import os
from pathlib import Path

# ── 5.11 組路徑：pathlib 是現代寫法 ────────────────────
# 用 / 運算子拼接路徑，比字串相加更安全且可跨平台。
# Windows 會用 '\\'，Linux/macOS 會用 '/'，Path 會自動處理。
base = Path("weeks") / "week-09"
print(base)              # weeks/week-09（Windows 會自動變成反斜線）
# .name：最後一段名稱（不含前面路徑）
print(base.name)         # week-09
# .parent：上一層目錄
print(base.parent)       # weeks
# .suffix：副檔名（含點）；資料夾通常是空字串
print(base.suffix)       # ''（無副檔名）

f = Path("hello.txt")
# .stem：檔名主體（不含副檔名）
# .suffix：副檔名（含 .）
print(f.stem, f.suffix)  # hello .txt

# 相容舊寫法：os.path.join
# 若你在舊專案常見 os.path.join，功能是把多段路徑組合起來。
# 與 pathlib 相比可讀性稍差，但仍非常常見。
print(os.path.join("weeks", "week-09", "README.md"))

# ── 5.12 存在判斷 ──────────────────────────────────────
p = Path("hello.txt")
# exists()：路徑是否存在（檔案或資料夾都算）
print(p.exists())    # 是否存在
# is_file()：存在且為檔案才會 True
print(p.is_file())   # 是否是檔案
# is_dir()：存在且為資料夾才會 True
print(p.is_dir())    # 是否是資料夾

missing = Path("no_such_file.txt")
# 實務上建議先檢查 exists，再讀取，避免 FileNotFoundError。
if not missing.exists():
    print(f"{missing} 不存在，略過讀取")

# ── 5.13 列出資料夾內容 ────────────────────────────────
here = Path(".")
# Path('.') 代表目前工作目錄（current working directory）。

# 只列當層
# os.listdir(here)：只列出「名稱」，不會遞迴進子目錄。
# 回傳值不含完整路徑，因此常需要自行再組路徑。
for name in os.listdir(here):
    print("listdir:", name)

# 只抓 .py（當層）
# glob('*.py')：只匹配目前資料夾，不會往下掃子資料夾。
for p in here.glob("*.py"):
    print("glob:", p)

# 遞迴抓所有 .py（含子資料夾）
# rglob('*.py')：recursive glob，會往所有子目錄遞迴搜尋。
# 若資料夾很大，結果可能很多，實務上可加條件或限制層級。
for p in Path("..").rglob("*.py"):
    print("rglob:", p)
    break  # 示範用，只印第一個
