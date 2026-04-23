# R02. 路徑操作與目錄列舉（5.11 / 5.12 / 5.13）
# Bloom: Remember — 會用 pathlib 組路徑、檢查存在、列出檔案

# 匯入 os 模組（舊式路徑與系統操作工具）
import os

# 匯入 pathlib 的 Path 類別（現代 Python 推薦用法）
from pathlib import Path

# ── 5.11 組路徑：pathlib 是現代寫法 ────────────────────

# 使用 Path 物件 + "/" 來組合路徑（跨平台，會自動處理 / 或 \）
base = Path("weeks") / "week-09"

# 印出完整路徑字串
print(base)              # weeks/week-09（Windows 會自動變成反斜線）

# .name：取得最後一層資料夾或檔名
print(base.name)         # week-09

# .parent：取得上一層目錄
print(base.parent)       # weeks

# .suffix：副檔名（若是資料夾或沒有副檔名則為空字串）
print(base.suffix)       # ''（無副檔名）

# 建立一個檔案路徑物件
f = Path("hello.txt")

# .stem：檔名（不含副檔名）
# .suffix：副檔名（包含 .）
print(f.stem, f.suffix)  # hello .txt

# 相容舊寫法：os.path.join
# 用字串方式拼接路徑（需要自己注意斜線問題）
print(os.path.join("weeks", "week-09", "README.md"))

# ── 5.12 存在判斷 ──────────────────────────────────────

# 建立一個 Path 物件（指向 hello.txt）
p = Path("hello.txt")

# .exists()：判斷路徑是否存在（檔案或資料夾都算）
print(p.exists())    # 是否存在

# .is_file()：是否為「檔案」
print(p.is_file())   # 是否是檔案

# .is_dir()：是否為「資料夾」
print(p.is_dir())    # 是否是資料夾

# 建立一個不存在的檔案路徑
missing = Path("no_such_file.txt")

# 如果檔案不存在
if not missing.exists():
    # 使用 f-string 輸出提示訊息
    print(f"{missing} 不存在，略過讀取")

# ── 5.13 列出資料夾內容 ────────────────────────────────

# Path(".") 代表目前所在目錄（current directory）
here = Path(".")

# 只列當層（不包含子資料夾）
# os.listdir() 回傳「檔名字串列表」
for name in os.listdir(here):
    print("listdir:", name)

# 只抓 .py（當層）
# glob("*.py")：只找當前目錄中副檔名為 .py 的檔案
# 回傳的是 Path 物件
for p in here.glob("*.py"):
    print("glob:", p)

# 遞迴抓所有 .py（含子資料夾）
# rglob("*.py")：recursive glob，會搜尋所有子目錄
for p in Path("..").rglob("*.py"):
    print("rglob:", p)
    break  # 示範用，只印第一個（避免輸出太多）