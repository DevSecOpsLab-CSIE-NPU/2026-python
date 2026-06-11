# U04-stringio-and-lines.py
# 完整繁體中文註釋版：示範 StringIO 類檔案物件與逐行處理

import io
from pathlib import Path

# ── 5.6 StringIO：在記憶體中建立一個文字類檔案物件 ─────────
buf = io.StringIO()
print("第一行", file=buf)   # 將文字寫入 StringIO 物件
print("第二行", file=buf)
print("第三行", file=buf)

# 取得 StringIO 內部目前的所有文字內容
text = buf.getvalue()
print("---StringIO 內容---")
print(text)

# 將內部指標移回起始位置，才能重新從頭讀取
buf.seek(0)
for i, line in enumerate(buf, 1):
    print(i, line.rstrip())

# StringIO 的用途是在記憶體中模擬檔案，方便傳給接受檔案物件的 API 使用
import csv
mem = io.StringIO()
writer = csv.writer(mem)
writer.writerow(["name", "score"])
writer.writerow(["alice", 90])
print("---CSV in memory---")
print(mem.getvalue())

# ── 5.1 延伸：逐行處理檔案，通常用於大檔或需要過濾處理的情況 ─────
src = Path("poem.txt")
src.write_text("床前明月光\n\n疑是地上霜\n\n舉頭望明月\n低頭思故鄉\n", encoding="utf-8")

# 目標：過濾空行、加入行號、寫到新檔
dst = Path("poem_numbered.txt")
with open(src, "rt", encoding="utf-8") as fin, \
     open(dst, "wt", encoding="utf-8") as fout:
    n = 0
    for line in fin:               # 逐行讀取原始檔
        line = line.rstrip()       # 去除右側換行符與多餘空白
        if not line:
            continue               # 如果是空行就跳過
        n += 1
        print(f"{n:02d}. {line}", file=fout)  # 寫入新檔並加行號

print("---加行號後---")
print(dst.read_text(encoding="utf-8"))
