from pathlib import Path
from datetime import date

today = date.today().isoformat()
diary = Path(f"diary-{today}.txt")

try:
    with open(diary, "x", encoding="utf-8") as f:
        f.write(f"# {today} 日記\n")
        f.write("今天學了檔案 I/O。\n")
    print(f"已建立 {diary}")
except FileExistsError:
    print(f"{diary} 今天已寫過，保留原內容不覆蓋")

def count_py(folder: Path):
    total, nonblank, defs = 0, 0, 0
    for p in folder.rglob("*.py"):
        with open(p, "rt", encoding="utf-8", errors="replace") as f:
            for line in f:
                total += 1
                s = line.strip()
                if s:
                    nonblank += 1
                if s.startswith("def "):
                    defs += 1
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