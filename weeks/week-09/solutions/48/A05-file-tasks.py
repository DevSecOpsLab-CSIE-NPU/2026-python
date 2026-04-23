# A05. 綜合應用：只建立新檔 + 目錄統計
# 主題：'x' 模式避免覆蓋、遞迴列出 .py、逐行統計程式碼指標

from pathlib import Path
from datetime import date

# ── 任務一：日記小工具（對應 5.5 的 'x' 模式） ─────────
# 規則：同一天只建立一次日記。
# 如果重複執行，不能覆蓋舊內容，要提示「已存在」。
today = date.today().isoformat()   # 例：2026-04-23
diary = Path(f"diary-{today}.txt")

try:
    # 'x' = exclusive create：檔案已存在就直接丟 FileExistsError
    with open(diary, "x", encoding="utf-8") as f:
        f.write(f"# {today} 日記\n")
        f.write("今天學了檔案 I/O。\n")
    print(f"已建立 {diary}")
except FileExistsError:
    print(f"{diary} 今天已寫過，保留原內容不覆蓋")

# ── 任務二：統計資料夾中 .py 檔案資訊 ───────────────────
# 目標統計：
# 1) total    : 總行數
# 2) nonblank : 非空白行數
# 3) defs     : 以 def 開頭的函式宣告行數
def count_py(folder: Path):
    total, nonblank, defs = 0, 0, 0

    # rglob('*.py')：遞迴搜尋所有 Python 檔（包含子資料夾）
    for p in folder.rglob("*.py"):
        # errors='replace'：遇到少數編碼怪字元時以替代字元處理，避免中斷
        with open(p, "rt", encoding="utf-8", errors="replace") as f:
            for line in f:
                total += 1
                s = line.strip()
                if s:
                    nonblank += 1
                if s.startswith("def "):
                    defs += 1

    return total, nonblank, defs


# 指向 week-04/in-class 做示範統計
target = Path("..") / ".." / "week-04" / "in-class"
if target.exists():
    total, nonblank, defs = count_py(target)
    print(f"{target}")
    print(f"  總行數       : {total}")
    print(f"  非空白行     : {nonblank}")
    print(f"  def 起頭行數 : {defs}")
else:
    print(f"示範目錄不存在：{target}")

# ── 課堂延伸挑戰 ───────────────────────────────────────
# 1) 日記改成 'a' 追加模式：同一天可多次追寫時間戳記事。
# 2) count_py 多算「註解行（以 # 開頭）」數量。
# 3) 把統計結果寫成 stats.tsv（可用 print(..., sep='\t', file=f)）。
