"""A05. 綜合應用：僅寫新檔 + 目錄統計（5.5 / 5.13 / 5.1）

Bloom: Apply
學習目標：把前面學到的檔案 API 組合起來，完成兩個小任務。

本檔任務摘要：
1) 日記小工具：使用 'x' 模式，確保同一天只建立一次檔案。
2) 程式碼統計：遞迴掃描資料夾中的 .py，統計總行數/非空白行/def 行。

關鍵觀念：
- 'x'（exclusive create）是「不存在才建立」，若檔案已存在就丟 FileExistsError。
- rglob("*.py") 可遞迴找出所有 Python 檔。
- 逐行讀取（for line in f）對大檔更安全，記憶體占用較低。
"""

from pathlib import Path
from datetime import date

# ── 任務一：日記小工具（5.5 的 'x' 模式） ──────────────
# 規則：每天只能建一次；同一天重複執行要提示「已存在」。
today = date.today().isoformat()          # 例如 2026-04-23
diary = Path(f"diary-{today}.txt")

try:
    # 'x' = exclusive create：
    # - 檔案不存在：成功建立並可寫入
    # - 檔案已存在：立刻丟 FileExistsError，不會覆蓋舊內容
    with open(diary, "x", encoding="utf-8") as f:
        # 實務上常用日期當檔名，方便按天追蹤與查找
        f.write(f"# {today} 日記\n")
        f.write("今天學了檔案 I/O。\n")
    print(f"已建立 {diary}")
except FileExistsError:
    # 明確告知使用者：資料保留，程式沒有覆蓋既有檔案
    print(f"{diary} 今天已寫過，保留原內容不覆蓋")

# ── 任務二：統計某資料夾裡 .py 檔的行數 ────────────────
# 走訪目錄 → 逐檔逐行讀 → 累計三個數字
def count_py(folder: Path):
    # total: 檔案總行數（包含空白行）
    # nonblank: 非空白行數
    # defs: 去除前後空白後，以 "def " 開頭的行數
    total, nonblank, defs = 0, 0, 0

    # rglob 會遞迴掃描 folder 與所有子資料夾
    for p in folder.rglob("*.py"):
        # errors="replace"：遇到少數無法解碼字元時，用替代符號避免整個程式中斷
        # 這在混雜編碼的舊專案中很實用
        with open(p, "rt", encoding="utf-8", errors="replace") as f:
            for line in f:
                total += 1

                # strip() 後若為空字串，表示這行是空白行或只有空白字元
                s = line.strip()
                if s:
                    nonblank += 1

                # 只統計函式定義行（最基本版本）
                # 注意：這裡不含 async def，也不處理多行 def 的特殊情況
                if s.startswith("def "):
                    defs += 1

    # 回傳三個統計值，呼叫端再決定如何顯示
    return total, nonblank, defs

target = Path("..") / ".." / "week-04" / "in-class"
if target.exists():
    # 先檢查資料夾存在，再進行統計，避免路徑錯誤造成例外
    total, nonblank, defs = count_py(target)
    print(f"{target}")
    print(f"  總行數       : {total}")
    print(f"  非空白行     : {nonblank}")
    print(f"  def 起頭行數 : {defs}")
else:
    # 教學情境下若示範目錄不存在，給出清楚提示而不是讓程式崩潰
    print(f"示範目錄不存在：{target}")

# ── 課堂延伸挑戰（自行嘗試） ───────────────────────────
# 1) 把日記工具改成「附加」模式 'a'：同一天可多次追寫一行時間戳。
# 2) count_py 再多算一個「註解行（以 # 開頭）」的數字。
# 3) 把統計結果用 print(..., sep='\t', file=f) 寫到 stats.tsv。
