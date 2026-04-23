# A05. 綜合應用：僅寫新檔 + 目錄統計（5.5 / 5.13 / 5.1）
# Bloom: Apply — 把前面學到的 API 組起來解小任務
#
# 本檔目標：把「檔案建立策略 + 目錄走訪 + 逐行統計」串成可用小工具。
# 你會看到兩種常見場景：
# 1) 日記檔只允許建立一次（避免同名覆蓋）
# 2) 對一整個資料夾做批次程式碼統計

from pathlib import Path
from datetime import date

# ── 任務一：日記小工具（5.5 的 'x' 模式） ──────────────
# 規則：每天只能建一次；同一天重複執行要提示「已存在」。
# date.today().isoformat() 會產生 YYYY-MM-DD，最適合拿來當檔名日期標記。
today = date.today().isoformat()          # 例如 2026-04-23
diary = Path(f"diary-{today}.txt")       # 例如 diary-2026-04-23.txt

try:
    # 'x' = exclusive create：
    # - 若檔案不存在：建立成功並開啟
    # - 若檔案已存在：立刻拋 FileExistsError（不覆蓋原檔）
    with open(diary, "x", encoding="utf-8") as f:
        f.write(f"# {today} 日記\n")
        f.write("今天學了檔案 I/O。\n")
    print(f"已建立 {diary}")
except FileExistsError:
    # 這是故意設計的保護機制：同一天不覆蓋，避免手滑洗掉紀錄。
    print(f"{diary} 今天已寫過，保留原內容不覆蓋")

# ── 任務二：統計某資料夾裡 .py 檔的行數 ────────────────
# 走訪目錄 → 逐檔逐行讀 → 累計三個數字
def count_py(folder: Path):
    # total    : 總行數（含空白與註解）
    # nonblank : 非空白行（strip 後有內容）
    # defs     : 以 def 開頭的函式定義行
    total, nonblank, defs = 0, 0, 0
    # rglob("*.py")：遞迴搜尋 folder 下所有 .py 檔
    for p in folder.rglob("*.py"):
        # errors="replace"：如果某些檔案含有無法解碼字元，
        # 不讓整個流程中斷，改以替代字元繼續統計。
        with open(p, "rt", encoding="utf-8", errors="replace") as f:
            for line in f:
                total += 1
                s = line.strip()   # 去掉前後空白後再判斷是否為空行
                if s:
                    nonblank += 1
                if s.startswith("def "):
                    defs += 1
    return total, nonblank, defs

# 示範目標路徑：從目前資料夾往上兩層，再進到 week-04/in-class。
target = Path("..") / ".." / "week-04" / "in-class"
if target.exists():
    total, nonblank, defs = count_py(target)
    print(f"{target}")
    print(f"  總行數       : {total}")
    print(f"  非空白行     : {nonblank}")
    print(f"  def 起頭行數 : {defs}")
else:
    # 在不同機器或資料夾結構下，示範目錄可能不存在。
    print(f"示範目錄不存在：{target}")

# ── 課堂延伸挑戰（自行嘗試） ───────────────────────────
# 1) 把日記工具改成「附加」模式 'a'：同一天可多次追寫一行時間戳。
# 2) count_py 再多算一個「註解行（以 # 開頭）」的數字。
# 3) 把統計結果用 print(..., sep='\t', file=f) 寫到 stats.tsv。
