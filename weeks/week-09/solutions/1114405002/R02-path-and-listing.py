# R02. 路徑操作與目錄列舉（5.11 / 5.12 / 5.13）
# ============================================================================
# Bloom: Remember — 會用 pathlib 組路徑、檢查存在、列出檔案
# pathlib 是現代 Python（3.4+）推薦的路徑操作方式
# 相比舊的 os.path，pathlib 提供物件導向介面，跨平台相容性更好
# ============================================================================

import os
from pathlib import Path

# ── 5.11 組路徑：pathlib 是現代寫法 ────────────────────
# pathlib.Path 支援用 / 運算子組路徑（直觀推薦）
# 優點：自動處理平台差異（Windows 反斜線 / Unix 正斜線）
# 路徑屬性：
#   - .name：檔名+副檔名（最後一個部分）
#   - .stem：檔名不含副檔名
#   - .suffix：副檔名（含點）
#   - .parent：上层目錄

base = Path("weeks") / "week-09"  # 用 / 組路徑，比 os.path.join 直觀
print(base)              # weeks/week-09（Windows 會自動變成反斜線）
print(base.name)         # week-09（最後一個部分）
print(base.parent)       # weeks（上層目錄）
print(base.suffix)       # ''（無副檔名，因為是目錄）

f = Path("hello.txt")
print(f.stem, f.suffix)  # hello .txt（分別是檔名和副檔名）

# 舊寫法（相容性）：os.path.join（不推薦，但要認識）
print(os.path.join("weeks", "week-09", "README.md"))  # 輸出相同結果

# ── 5.12 存在判斷 ──────────────────────────────────────
# 三個常用判斷方法：
#   - .exists()：路徑是否存在（檔或目錄）
#   - .is_file()：是否為檔案
#   - .is_dir()：是否為目錄
# 應用場景：避免打開不存在的檔案、分別處理檔案和目錄

p = Path("hello.txt")
print(p.exists())    # True（檔案存在）
print(p.is_file())   # True（是檔案而不是目錄）
print(p.is_dir())    # False（不是目錄）

# 安全讀檔：先檢查再開啟
missing = Path("no_such_file.txt")
if not missing.exists():
    print(f"{missing} 不存在，略過讀取")  # 避免拋出 FileNotFoundError

# ── 5.13 列出資料夾內容 ────────────────────────────────
# 三種列舉方式：
#   1. os.listdir(path)：列出當層所有項目（舊方式，不推薦）
#   2. Path.glob(pattern)：當層內模式匹配的檔（如 *.py）
#   3. Path.rglob(pattern)：遞迴搜尋模式匹配的檔（包含子資料夾）

here = Path(".")

# 方式 1：os.listdir（舊方式，返回字串列表）
for name in os.listdir(here):
    print("listdir:", name)  # 只顯示名稱，要自己判斷是檔還是目錄

# 方式 2：glob（當層搜尋，推薦）
for p in here.glob("*.py"):  # 只找當層的所有 .py 檔
    print("glob:", p)        # 返回 Path 物件，可直接操作

# 方式 3：rglob（遞迴搜尋，包含子資料夾）
for p in Path("..").rglob("*.py"):  # 搜尋當前目錄及所有子目錄的 .py 檔
    print("rglob:", p)
    break  # 示範用，只印第一個（否則會輸出很多行）
   
# 小結：
# - 日常使用推薦 .glob() / .rglob()
# - os.listdir() 主要用於舊代碼兼容
