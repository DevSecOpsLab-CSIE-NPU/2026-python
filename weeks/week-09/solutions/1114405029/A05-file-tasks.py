# A05. 綜合應用：僅寫新檔 + 目錄統計（5.5 / 5.13 / 5.1）
# Bloom: Apply — 把前面學到的 API 組起來解小任務

# 匯入 Path（處理路徑）與 date（取得今天日期）
from pathlib import Path
from datetime import date

# ── 任務一：日記小工具（5.5 的 'x' 模式） ──────────────
# 規則：每天只能建一次；同一天重複執行要提示「已存在」。

# 取得今天日期，格式為 YYYY-MM-DD（ISO 格式）
today = date.today().isoformat()          # 例如 2026-04-23

# 建立日記檔案名稱，例如 diary-2026-04-23.txt
diary = Path(f"diary-{today}.txt")

try:
    # 使用 "x" 模式開檔（exclusive create）
    # → 檔案「不存在」才會建立
    # → 如果已存在會直接丟出 FileExistsError（不會覆蓋）
    with open(diary, "x", encoding="utf-8") as f:
        # 寫入標題（包含日期）
        f.write(f"# {today} 日記\n")

        # 寫入內容
        f.write("今天學了檔案 I/O。\n")

    # 成功建立時印出訊息
    print(f"已建立 {diary}")

# 如果檔案已存在（代表今天已經寫過）
except FileExistsError:
    # 不覆蓋原內容，提示使用者
    print(f"{diary} 今天已寫過，保留原內容不覆蓋")

# ── 任務二：統計某資料夾裡 .py 檔的行數 ────────────────
# 走訪目錄 → 逐檔逐行讀 → 累計三個數字

# 定義一個函式，用來統計 Python 檔案資訊
def count_py(folder: Path):
    # total：總行數
    # nonblank：非空白行數（去掉空行後）
    # defs：以 "def " 開頭的函式定義行數
    total, nonblank, defs = 0, 0, 0

    # rglob("*.py")：遞迴搜尋資料夾中所有 .py 檔（包含子目錄）
    for p in folder.rglob("*.py"):

        # 開啟每個 Python 檔案
        # errors="replace"：如果遇到編碼錯誤，用替代字元處理（避免程式崩潰）
        with open(p, "rt", encoding="utf-8", errors="replace") as f:

            # 逐行讀取（節省記憶體）
            for line in f:
                # 每讀一行就累加總行數
                total += 1

                # strip()：去掉前後空白（包含換行）
                s = line.strip()

                # 如果不是空字串 → 表示是「非空白行」
                if s:
                    nonblank += 1

                # 判斷是否為函式定義（以 "def " 開頭）
                if s.startswith("def "):
                    defs += 1

    # 回傳三個統計數值
    return total, nonblank, defs

# 指定要統計的資料夾（相對路徑往上兩層再進入 week-04/in-class）
target = Path("..") / ".." / "week-04" / "in-class"

# 如果目標資料夾存在
if target.exists():
    # 呼叫統計函式
    total, nonblank, defs = count_py(target)

    # 印出資料夾路徑
    print(f"{target}")

    # 印出統計結果
    print(f"  總行數       : {total}")
    print(f"  非空白行     : {nonblank}")
    print(f"  def 起頭行數 : {defs}")

# 如果資料夾不存在（避免錯誤）
else:
    print(f"示範目錄不存在：{target}")

# ── 課堂延伸挑戰（自行嘗試） ───────────────────────────
# 1) 把日記工具改成「附加」模式 'a'：同一天可多次追寫一行時間戳。
# 2) count_py 再多算一個「註解行（以 # 開頭）」的數字。
# 3) 把統計結果用 print(..., sep='\t', file=f) 寫到 stats.tsv。