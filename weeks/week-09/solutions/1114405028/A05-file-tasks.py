# A05-file-tasks.py
# 完整繁體中文註釋版：示範寫新檔、目錄遞迴與檔案行數統計

from pathlib import Path
from datetime import date

# ── 任務一：日記小工具（只允許每天建立一次） ─────────────────
# today 會是像 2026-04-23 的 ISO 格式字串
today = date.today().isoformat()
diary = Path(f"diary-{today}.txt")

try:
    # 'x' 表示 exclusive create；如果檔案已存在會丟出 FileExistsError
    with open(diary, "x", encoding="utf-8") as f:
        f.write(f"# {today} 日記\n")
        f.write("今天學了檔案 I/O。\n")
    print(f"已建立 {diary}")
except FileExistsError:
    # 當天已經寫過日記時，不覆蓋原有內容
    print(f"{diary} 今天已寫過，保留原內容不覆蓋")

# ── 任務二：統計資料夾內所有 .py 檔的行數 ───────────────────
# 使用 rglob 遞迴搜尋所有 Python 檔案

def count_py(folder: Path):
    total, nonblank, defs = 0, 0, 0
    for p in folder.rglob("*.py"):
        with open(p, "rt", encoding="utf-8", errors="replace") as f:
            for line in f:
                total += 1
                s = line.strip()        # 去除前後空白
                if s:
                    nonblank += 1
                if s.startswith("def "):
                    defs += 1
    return total, nonblank, defs

# 這裡示範統計週四前一週的 in-class 檔案
target = Path("..") / ".." / "week-04" / "in-class"
if target.exists():
    total, nonblank, defs = count_py(target)
    print(f"{target}")
    print(f"  總行數       : {total}")
    print(f"  非空白行     : {nonblank}")
    print(f"  def 起頭行數 : {defs}")
else:
    print(f"示範目錄不存在：{target}")

# ── 課堂延伸挑戰（可以自行練習） ───────────────────────────
# 1) 把日記工具改成附加模式 'a'：每次執行都加入一行時間戳記。
# 2) count_py 再多算一個「註解行（以 # 開頭）」的數量。
# 3) 把統計結果寫成 TSV 檔案，例如 print(..., sep='\t', file=f)。
