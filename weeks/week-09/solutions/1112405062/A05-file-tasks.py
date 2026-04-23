# A05. 綜合應用：僅寫新檔 + 目錄統計（5.5 / 5.13 / 5.1）
# Bloom: Apply — 把前面學到的 API 組起來解小任務
# 本範例綜合應用所學的檔案操作技能，完成實際的小任務

from pathlib import Path
from datetime import date

# ── 任務一：日記小工具（5.5 的 'x' 模式） ──────────────
#  規則：每天只能建一次；同一天重複執行要提示「已存在」。
#  mode='x' 是獨占建立模式，若檔案已存在會拋出 FileExistsError
today = date.today().isoformat()          # 例如 2026-04-23
diary = Path(f"diary-{today}.txt")

try:
    with open(diary, "x", encoding="utf-8") as f:   # 'x' = exclusive create（獨占建立）
        f.write(f"# {today} 日記\n")
        f.write("今天學了檔案 I/O。\n")
    print(f"已建立 {diary}")
except FileExistsError:
    print(f"{diary} 今天已寫過，保留原內容不覆蓋")
# ── 任務二：統計某資料夾裡 .py 檔的行數 ────────────────
#  走訪目錄 → 逐檔逐行讀 → 累計三個數字
#  total: 總行數
#  nonblank: 非空白行數
#  defs: 以 def 開頭的行數（函數定義）
def count_py(folder: Path):
    total, nonblank, defs = 0, 0, 0
    for p in folder.rglob("*.py"):  # 遞迴搜尋所有 .py 檔
        with open(p, "rt", encoding="utf-8", errors="replace") as f:
            for line in f:
                total += 1
                s = line.strip()
                if s:
                    nonblank += 1  # 非空白行
                if s.startswith("def "):
                    defs += 1  # 函數定義行
    return total, nonblank, defs

target = Path("..") / ".." / "week-04" / "in-class"
if target.exists():
    total, nonblank, defs = count_py(target)
    print(f"{target}")
    print(f"  總行數       : {total}")
    print(f"  非空白行     : {nonblank}")
    print(f"  def 起頭行數 : {defs}")
else:
    print(f"示範目錄不存在：{target}")

# ── 課堂延伸挑戰（自行嘗試） ───────────────────────────
# 1) 把日記工具改成「附加」模式 'a'：同一天可多次追寫一行時間戳。
# 2) count_py 再多算一個「註解行（以 # 開頭）」的數字。
# 3) 把統計結果用 print(..., sep='\t', file=f) 寫到 stats.tsv。