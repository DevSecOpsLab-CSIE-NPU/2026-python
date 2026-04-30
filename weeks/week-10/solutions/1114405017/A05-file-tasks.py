# A05. 綜合應用：僅寫新檔 + 目錄統計（5.5 / 5.13 / 5.1）
# Bloom: Apply — 把前面學到的 API 組起來解小任務

from pathlib import Path
from datetime import date

# ── 任務一：日記小工具（5.5 的 'x' 模式） ──────────────
# 這個範例示範如何用 'x' 模式建立新檔，若檔案已存在則會丟出 FileExistsError。
# 規則：每天只能建立一次日記，若同一天重複執行要提示「已存在」，並保留原本內容。

today = date.today().isoformat()          # 取得今天日期，格式為 YYYY-MM-DD，例如 2026-04-23
# diary 變數會是今天日記檔案的路徑，例如 diary-2026-04-23.txt
# Path() 會把字串轉成 pathlib.Path 物件，方便後續檔案操作。
diary = Path(f"diary-{today}.txt")

try:
    # open(..., 'x') 會嘗試建立新檔案，若檔案已經存在就會拋出 FileExistsError。
    with open(diary, "x", encoding="utf-8") as f:
        # 若成功建立，就把標題與內容寫入檔案
        f.write(f"# {today} 日記\n")
        f.write("今天學了檔案 I/O。\n")
    print(f"已建立 {diary}")
except FileExistsError:
    # 如果檔案已經存在，表示今天已經寫過日記，不覆蓋原內容
    print(f"{diary} 今天已寫過，保留原內容不覆蓋")

# ── 任務二：統計某資料夾裡 .py 檔的行數 ────────────────
# 這個函式會走訪指定資料夾內所有 .py 檔案，並累計總行數、非空白行數、以及 def 開頭的行數。

def count_py(folder: Path):
    # total: 檔案總行數
    # nonblank: 非空白行數（strip 後非空字串）
    # defs: 以 def 開頭的函式宣告行數
    total, nonblank, defs = 0, 0, 0

    # folder.rglob('*.py') 會遞迴搜尋資料夾下所有符合副檔名的檔案
    for p in folder.rglob("*.py"):
        # 以純文字模式讀取檔案，encoding='utf-8' 以及 errors='replace' 可避免編碼錯誤中斷程式
        with open(p, "rt", encoding="utf-8", errors="replace") as f:
            for line in f:
                total += 1
                # strip() 會移除前後空白，判斷是否為空白行
                s = line.strip()
                if s:
                    nonblank += 1
                # 若該行以 def + 空格開頭，代表是 Python 函式定義
                if s.startswith("def "):
                    defs += 1
    return total, nonblank, defs

# target 是要統計的範例資料夾，這裡用相對路徑往上兩層再進入 week-04/in-class
# Path("..") / ".." / "week-04" / "in-class" 等同於 '..\\..\\week-04\\in-class'
target = Path("..") / ".." / "week-04" / "in-class"

if target.exists():
    # 若目標資料夾存在，呼叫 count_py 並印出結果
    total, nonblank, defs = count_py(target)
    print(f"{target}")
    print(f"  總行數       : {total}")
    print(f"  非空白行     : {nonblank}")
    print(f"  def 起頭行數 : {defs}")
else:
    # 若資料夾不存在，提示使用者目標路徑不存在
    print(f"示範目錄不存在：{target}")

# ── 課堂延伸挑戰（自行嘗試） ───────────────────────────
# 1) 把日記工具改成「附加」模式 'a'：同一天可多次追寫一行時間戳。
# 2) count_py 再多算一個「註解行（以 # 開頭）」的數字。
# 3) 把統計結果用 print(..., sep='\t', file=f) 寫到 stats.tsv。
