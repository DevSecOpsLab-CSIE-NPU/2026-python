# A05. 綜合應用：僅寫新檔 + 目錄統計（5.5 / 5.13 / 5.1）
# Bloom: Apply — 把前面學到的 API 組起來解小任務

from pathlib import Path
from datetime import date

# ── 任務一：日記小工具（5.5 的 'x' 模式） ──────────────
# 這個範例示範如何使用 open() 的 'x' 模式，表示「獨佔建立新檔案」。
# 若檔案已存在，open() 會丟出 FileExistsError，程式就可以改成提示用戶而不覆蓋。

today = date.today().isoformat()          # 取得今天日期字串，例如 2026-04-23
# diary 檔名會依日期不同而變動，今天執行就建立 diary-YYYY-MM-DD.txt

diary = Path(f"diary-{today}.txt")

try:
    # 'x' 模式只會在檔案不存在時建立新檔案，檔案已存在就失敗
    with open(diary, "x", encoding="utf-8") as f:
        # 這裡寫入兩行範例日記內容
        f.write(f"# {today} 日記\n")
        f.write("今天學了檔案 I/O。\n")
    print(f"已建立 {diary}")
except FileExistsError:
    # 如果同一天日記檔已存在，就提示使用者，不會覆蓋原本內容
    print(f"{diary} 今天已寫過，保留原內容不覆蓋")

# ── 任務二：統計某資料夾裡 .py 檔的行數 ────────────────
# 這個函式會遞迴走訪指定資料夾，統計所有 Python 檔案的總行數、非空白行數、def 定義行數。

def count_py(folder: Path):
    """統計 folder 下所有 .py 檔案的行數資訊。"""
    total, nonblank, defs = 0, 0, 0

    # Path.rglob() 可以遞迴搜尋所有符合模式的檔案
    for p in folder.rglob("*.py"):
        # 以文字模式讀取檔案並將編碼錯誤替換，避免因無法辨識某些字元而中斷
        with open(p, "rt", encoding="utf-8", errors="replace") as f:
            for line in f:
                total += 1

                # strip() 可以去掉前後空白，判斷是否為空白行
                s = line.strip()
                if s:
                    nonblank += 1

                # 以 def 開頭代表函式宣告，這裡簡單統計 def 數量
                if s.startswith("def "):
                    defs += 1

    return total, nonblank, defs

# 設定要統計的目錄，這裡示範相對路徑到 week-04/in-class
# 若執行檔案位置改變，這個相對路徑也需要更新

target = Path("..") / ".." / "week-04" / "in-class"
if target.exists():
    total, nonblank, defs = count_py(target)
    print(f"{target}")
    print(f"  總行數       : {total}")
    print(f"  非空白行     : {nonblank}")
    print(f"  def 起頭行數 : {defs}")
else:
    # 如果目標資料夾不存在，就印出錯誤資訊，方便除錯
    print(f"示範目錄不存在：{target}")

# ── 課堂延伸挑戰（自行嘗試） ───────────────────────────
# 1) 把日記工具改成「附加」模式 'a'：同一天可多次追寫一行時間戳。
#    例如：with open(diary, 'a', encoding='utf-8') as f: f.write('...\n')
# 2) count_py 再多算一個「註解行（以 # 開頭）」的數字。
#    可以在 for line in f: 迴圈中加入 if s.startswith('#'): comments += 1
# 3) 把統計結果用 print(..., sep='\t', file=f) 寫到 stats.tsv。
#    例如：with open('stats.tsv', 'w', encoding='utf-8') as out: print('path', 'total', sep='\t', file=out)
