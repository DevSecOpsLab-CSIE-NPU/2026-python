# U04. StringIO 與逐行處理
# 主題：file-like 物件概念、在記憶體操作文字、逐行處理大型文字檔

import io
from pathlib import Path

# ── 1) StringIO：記憶體中的文字檔案（對應 5.6） ─────────
# StringIO 提供「像檔案一樣」的介面，但資料存在記憶體
buf = io.StringIO()
print("第一行", file=buf)
print("第二行", file=buf)
print("第三行", file=buf)

# getvalue() 可一次拿出目前累積的完整文字
text = buf.getvalue()
print("---StringIO 內容---")
print(text)

# seek(0) 把讀寫游標移回開頭，之後可以像讀檔一樣逐行迭代
buf.seek(0)
for i, line in enumerate(buf, 1):
    print(i, line.rstrip())

# 為什麼好用：許多函式庫支援 file-like 物件，可直接拿 StringIO 測試
import csv

mem = io.StringIO()
writer = csv.writer(mem)
writer.writerow(["name", "score"])
writer.writerow(["alice", 90])
print("---CSV in memory---")
print(mem.getvalue())

# ── 2) 逐行處理文字檔（對應 5.1 延伸） ─────────────────
# 建立一個多行文字檔，含空行
src = Path("poem.txt")
src.write_text("床前明月光\n\n疑是地上霜\n\n舉頭望明月\n低頭思故鄉\n", encoding="utf-8")

# 任務：
# 1) 跳過空行
# 2) 為每行加上編號
# 3) 寫入新檔
# 逐行讀取的好處：一次只處理一行，對大檔更省記憶體
dst = Path("poem_numbered.txt")
with open(src, "rt", encoding="utf-8") as fin, \
     open(dst, "wt", encoding="utf-8") as fout:
    n = 0
    for line in fin:
        line = line.rstrip()
        if not line:
            continue
        n += 1
        print(f"{n:02d}. {line}", file=fout)

print("---加行號後---")
print(dst.read_text(encoding="utf-8"))
