# A05. 綜合應用：僅寫新檔 + 目錄統計（5.5 / 5.13 / 5.1）
# Bloom: Apply — 把前面學到的 API 組起來解小任務

# Path 用來處理路徑；date 用來取得今天日期。
# 這個範例把「建立檔案」和「掃描資料夾」兩種常見任務串在一起。
from pathlib import Path
from datetime import date

# ── 任務一：日記小工具（5.5 的 'x' 模式） ──────────────
# 規則：每天只能建一次；同一天重複執行要提示「已存在」。
# 'x' 模式代表 exclusive create：
# - 檔案不存在時才允許建立
# - 如果檔案已存在，open() 會直接丟出 FileExistsError
# 這很適合做「不可覆蓋」的建立動作，例如每日日記、一次性報表。
today = date.today().isoformat()          # 例如 2026-04-23
# 用日期組出檔名，讓每天都有獨立的日記檔。
diary = Path(f"diary-{today}.txt")

try:
    # with open(..., "x")：只建立新檔，不會覆蓋舊檔。
    # encoding='utf-8'：寫入中文內容時明確指定編碼，避免亂碼。
    with open(diary, "x", encoding="utf-8") as f:   # 'x' = exclusive create
        # 先寫入標題，再寫入正文。
        # f.write() 寫入的是字串，不需要 print 的格式控制。
        f.write(f"# {today} 日記\n")
        f.write("今天學了檔案 I/O。\n")
    print(f"已建立 {diary}")
except FileExistsError:
    # 如果同一天已經執行過一次，就不要覆蓋原內容。
    # 這裡用例外處理把「重複建立」轉成友善提示。
    print(f"{diary} 今天已寫過，保留原內容不覆蓋")

# ── 任務二：統計某資料夾裡 .py 檔的行數 ────────────────
# 走訪目錄 → 逐檔逐行讀 → 累計三個數字
# 這個函式示範如何用遞迴掃描資料夾中的所有 .py 檔，
# 然後逐行統計：
# - total：總行數
# - nonblank：非空白行數
# - defs：以 def 開頭的函式定義行數
def count_py(folder: Path):
    total, nonblank, defs = 0, 0, 0
    # rglob("*.py") 會遞迴搜尋 folder 底下所有子目錄中的 .py 檔。
    for p in folder.rglob("*.py"):
        # errors="replace"：若檔案含有無法解碼的字元，改用替代字元繼續讀。
        # 這樣可以避免整個統計流程因單一壞檔而中斷。
        with open(p, "rt", encoding="utf-8", errors="replace") as f:
            # 逐行讀取比一次 read() 更省記憶體，特別適合大檔案或大量檔案。
            for line in f:
                total += 1
                # strip() 會去掉左右空白與換行，方便判斷是否為空白行。
                s = line.strip()
                if s:
                    nonblank += 1
                # 只統計最前面是 "def " 的行，作為函式定義數量。
                # 這裡是簡單字串判斷，不是完整語法分析。
                if s.startswith("def "):
                    defs += 1
    return total, nonblank, defs

# 目標資料夾：往上兩層，再進到 week-04/in-class。
# 這種寫法可以避免手動寫死完整絕對路徑。
target = Path("..") / ".." / "week-04" / "in-class"
if target.exists():
    # 如果目錄存在，就執行統計並列印結果。
    total, nonblank, defs = count_py(target)
    print(f"{target}")
    print(f"  總行數       : {total}")
    print(f"  非空白行     : {nonblank}")
    print(f"  def 起頭行數 : {defs}")
else:
    # 如果示範資料夾不存在，就印出提示，不讓程式報錯中斷。
    print(f"示範目錄不存在：{target}")

# ── 課堂延伸挑戰（自行嘗試） ───────────────────────────
# 1) 把日記工具改成「附加」模式 'a'：同一天可多次追寫一行時間戳。
# 2) count_py 再多算一個「註解行（以 # 開頭）」的數字。
# 3) 把統計結果用 print(..., sep='\t', file=f) 寫到 stats.tsv。
