# A05. 綜合應用：僅寫新檔 + 目錄統計（5.5 / 5.13 / 5.1）
# Bloom: Apply — 把前面學到的 API 組起來解小任務

from pathlib import Path
from datetime import date

# ── 任務一：日記小工具（5.5 的 'x' 模式） ──────────────
# 目標：每天建立一份日記檔，且「同一天只允許建立一次」。
# 核心做法：使用 open(..., 'x')（exclusive create，獨占建立模式）。
# - 檔案不存在：成功建立並寫入內容。
# - 檔案已存在：立即拋出 FileExistsError，不會覆蓋舊內容。
# 這很適合用在「避免覆寫」的安全寫檔情境。

# date.today().isoformat() 會得到 YYYY-MM-DD 格式字串，例如 2026-04-23
# 用日期當檔名的一部分，能自然做到每日一檔。
today = date.today().isoformat()
diary = Path(f"diary-{today}.txt")

try:
    # 'x' = 僅在檔案不存在時建立新檔。
    # encoding='utf-8'：明確指定編碼，避免跨平台預設編碼差異。
    with open(diary, "x", encoding="utf-8") as f:
        # 寫入固定模板內容，示範可替換成課堂筆記或每日心得。
        f.write(f"# {today} 日記\n")
        f.write("今天學了檔案 I/O。\n")
    print(f"已建立 {diary}")
except FileExistsError:
    # 若同一天重複執行，會走到這裡。
    # 訊息明確說明：保留原檔，不做覆蓋。
    print(f"{diary} 今天已寫過，保留原內容不覆蓋")

# ── 任務二：統計某資料夾裡 .py 檔的行數 ────────────────
# 任務需求：
# 1) 走訪指定資料夾（含子資料夾）所有 .py 檔
# 2) 累計「總行數」
# 3) 累計「非空白行」
# 4) 累計「以 def 開頭的行數」（粗略估計函式宣告數）

def count_py(folder: Path):
    # total    : 所有讀到的行（包含空行、註解、程式碼）
    # nonblank : 去掉前後空白後仍有內容的行
    # defs     : 去空白後以 "def " 開頭的行
    total, nonblank, defs = 0, 0, 0

    # rglob('*.py') 會遞迴搜尋 folder 底下所有 Python 檔。
    for p in folder.rglob("*.py"):
        # errors='replace'：若遇到非 UTF-8 字元，
        # 以替代字元取代，避免整個統計因解碼錯誤中斷。
        with open(p, "rt", encoding="utf-8", errors="replace") as f:
            for line in f:
                total += 1

                # strip() 去除前後空白字元，
                # 便於判斷空行與是否為 def 起頭。
                s = line.strip()

                # 非空字串代表非空白行。
                if s:
                    nonblank += 1

                # 粗略判斷函式宣告：以 def + 空白開頭。
                # 注意：這是行文字判斷，不是語法樹解析。
                if s.startswith("def "):
                    defs += 1

    return total, nonblank, defs

# 目標資料夾：從目前檔案所在邏輯位置往上兩層，再進 week-04/in-class
# 實際等同於 ../../week-04/in-class
# 這裡保留課堂示範寫法，方便理解 Path 串接。
target = Path("..") / ".." / "week-04" / "in-class"

# 防呆：先檢查目錄是否存在，再執行統計。
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
