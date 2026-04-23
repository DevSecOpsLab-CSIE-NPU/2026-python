# R02. 路徑操作與目錄列舉（5.11 / 5.12 / 5.13）
# Bloom: Remember — 會用 pathlib 組路徑、檢查存在、列出檔案
#
# 這份檔案的目的：
# 1) 學會用 pathlib.Path 組合路徑（比字串拼接更安全、跨平台）
# 2) 學會判斷路徑是否存在、是檔案還是資料夾
# 3) 學會列出目錄內容（只列當層 / 符合 pattern / 遞迴搜尋）

import os          # 傳統的路徑工具（os.path.join / os.listdir）
from pathlib import Path  # 現代化路徑物件，Python 3.4+ 內建

# ── 5.11 組路徑：pathlib 是現代寫法 ────────────────────
# Path 物件可以用 / 運算子接路徑段，比字串拼接更直觀且跨平台。
# Windows 會自動用反斜線 \，Linux/macOS 用正斜線 /，不用手動處理。
base = Path("weeks") / "week-09"
print(base)              # 印出完整路徑（Windows 上會是 weeks\week-09）
print(base.name)         # .name：只取最後一段資料夾 / 檔案名稱 → week-09
print(base.parent)       # .parent：取上一層目錄 → weeks
print(base.suffix)       # .suffix：副檔名，資料夾沒有副檔名所以是空字串 ''

f = Path("hello.txt")
print(f.stem, f.suffix)  # .stem：主檔名部分 → hello；.suffix：副檔名 → .txt

# 相容舊寫法：os.path.join
# 如果你要維護舊程式或與舊同事協作，os.path.join 仍然有效
print(os.path.join("weeks", "week-09", "README.md"))
# 以上兩種寫法結果相同，但 pathlib 更好讀

# ── 5.12 存在判斷 ──────────────────────────────────────
# 開啟檔案前先確認路徑是否存在，可以避免 FileNotFoundError。
p = Path("hello.txt")
print(p.exists())    # exists()：只要這個路徑存在就回傳 True（不管是檔案或資料夾）
print(p.is_file())   # is_file()：確認這個路徑是「一般檔案」才回傳 True
print(p.is_dir())    # is_dir()：確認這個路徑是「目錄」才回傳 True

missing = Path("no_such_file.txt")
if not missing.exists():
    # 這個判斷是「防禦性寫法」：不存在就跳過，不讓程式崩潰
    print(f"{missing} 不存在，略過讀取")

# ── 5.13 列出資料夾內容 ────────────────────────────────
# 三種常見的列目錄方式，依使用情境選擇：
# 1. os.listdir()   → 只列當層，回傳純字串名稱清單
# 2. Path.glob()    → 只列當層，但可以用 pattern 過濾
# 3. Path.rglob()   → 遞迴深入子資料夾，用 pattern 過濾
here = Path(".")   # "." 代表目前執行時的工作目錄

# 方法一：os.listdir —— 傳統寫法，回傳字串清單
# 注意：os.listdir 回傳的是字串，不是 Path 物件
for name in os.listdir(here):
    print("listdir:", name)

# 方法二：Path.glob —— 只搜尋當層，支援萬用字元 *
# "*.py" 表示「名稱結尾是 .py 的所有檔案」
for p in here.glob("*.py"):
    print("glob:", p)   # 這裡 p 是 Path 物件，可以直接做後續操作

# 方法三：Path.rglob —— 等同於 glob 加上 **/ 前綴，遞迴搜尋
# rglob("*.py") 會深入所有子資料夾找 .py 檔
for p in Path("..").rglob("*.py"):
    print("rglob:", p)
    break  # 這裡只印第一個示範，實際使用時可以移除 break 印全部
