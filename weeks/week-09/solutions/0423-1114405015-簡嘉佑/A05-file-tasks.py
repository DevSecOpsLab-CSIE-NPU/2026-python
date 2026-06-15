"""
A05. 綜合應用：僅寫新檔 + 目錄統計（5.5 / 5.13 / 5.1）
Bloom: Apply

本檔示範兩個常見的小任務：
1) 用 'x' 模式建立「一天只寫一次」的日記檔。
2) 遞迴掃描資料夾，統計 .py 檔行數資訊。

重點是把檔案 I/O、例外處理、pathlib 路徑操作串起來。
"""

from pathlib import Path
from datetime import date

# ── 任務一：日記小工具（5.5 的 'x' 模式） ──────────────
# 規則：每天只能建一次；同一天重複執行要提示「已存在」。
# date.today().isoformat() 會產生 YYYY-MM-DD 字串，適合拿來當檔名的一部分。
today = date.today().isoformat()          # 例如 2026-04-23
# 透過 Path 建立「今天日記檔」路徑，例如 diary-2026-04-23.txt
diary = Path(f"diary-{today}.txt")

try:
    # 'x' = exclusive create：檔案不存在才允許建立；存在就丟 FileExistsError
    # 這正好符合「避免覆蓋舊內容」的需求。
    with open(diary, "x", encoding="utf-8") as f:
        f.write(f"# {today} 日記\n")
        f.write("今天學了檔案 I/O。\n")
    print(f"已建立 {diary}")
except FileExistsError:
    # 捕捉特定例外，讓程式能友善提示，而不是直接中斷。
    print(f"{diary} 今天已寫過，保留原內容不覆蓋")

# ── 任務二：統計某資料夾裡 .py 檔的行數 ────────────────
# 流程：走訪目錄 → 逐檔逐行讀 → 累計三個數字
# total    : 總行數（含空白行）
# nonblank : 非空白行
# defs     : 去頭尾空白後，以 "def " 開頭的行數
def count_py(folder: Path):
    total, nonblank, defs = 0, 0, 0
    # rglob("*.py") 會遞迴找出 folder 下所有 .py 檔
    for p in folder.rglob("*.py"):
        # errors="replace"：若檔案有少數非法位元組，仍可繼續統計，不會直接炸掉
        with open(p, "rt", encoding="utf-8", errors="replace") as f:
            for line in f:
                total += 1
                # strip() 後若還有字元，代表此行不是空白行
                s = line.strip()
                if s:
                    nonblank += 1
                # 這裡是簡單判定：只統計以 def 開頭的函式定義行
                # （不處理多行宣告、巢狀語法等進階情境）
                if s.startswith("def "):
                    defs += 1
    return total, nonblank, defs

# 目標資料夾示範：week-04/in-class
# 這裡用相對路徑組合，方便在課程資料夾內移動使用。
target = Path("..") / ".." / "week-04" / "in-class"
if target.exists():
    total, nonblank, defs = count_py(target)
    print(f"{target}")
    print(f"  總行數       : {total}")
    print(f"  非空白行     : {nonblank}")
    print(f"  def 起頭行數 : {defs}")
else:
    # 若路徑不存在，僅提示，不拋錯，保持示範腳本可直接執行。
    print(f"示範目錄不存在：{target}")

# ── 課堂延伸挑戰（自行嘗試） ───────────────────────────
# 1) 把日記工具改成「附加」模式 'a'：同一天可多次追寫一行時間戳。
# 2) count_py 再多算一個「註解行（以 # 開頭）」的數字。
# 3) 把統計結果用 print(..., sep='\t', file=f) 寫到 stats.tsv。
