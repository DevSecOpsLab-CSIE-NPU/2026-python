# U04. 類檔案物件 StringIO 與逐行處理（5.6 / 5.1 逐行）
# Bloom: Understand — 知道 file-like 是鴨子型別，能把記憶體當檔案用
# 本範例介紹 StringIO（記憶體中的檔案物件）與逐行處理檔案的方法

import io
from pathlib import Path

# ── 5.6 StringIO：記憶體裡的「假檔案」 ─────────────────
#  StringIO 是 IO 模組提供的類別，可在記憶體中建立類似檔案的物件
#  適用於：測試、避免實際寫入磁碟、對接需要 file-like 物件的 API
buf = io.StringIO()
print("第一行", file=buf)
print("第二行", file=buf)
print("第三行", file=buf)

#  取出整段字串（類似 read()）
text = buf.getvalue()
print("---StringIO 內容---")
print(text)
#  也能當讀檔用：seek 回開頭再逐行讀
buf.seek(0)
for i, line in enumerate(buf, 1):
    print(i, line.rstrip())

#  為什麼有用？任何收 file-like 物件的 API（csv、json、logging）
#  都能塞 StringIO，不必真的寫到磁碟、方便測試。
import csv
mem = io.StringIO()
writer = csv.writer(mem)
writer.writerow(["name", "score"])
writer.writerow(["alice", 90])
print("---CSV in memory---")
print(mem.getvalue())

# ── 5.1 延伸：逐行處理檔案（大檔友善） ─────────────────
#  處理大檔案時，應該逐行讀取而非一次讀入記憶體，避免記憶體不足
#  先建立一個多行測試檔案
src = Path("poem.txt")
src.write_text("床前明月光\n\n疑是地上霜\n\n舉頭望明月\n低頭思故鄉\n", encoding="utf-8")

#  任務：過濾空行、加上行號、寫到新檔
dst = Path("poem_numbered.txt")
with open(src, "rt", encoding="utf-8") as fin, \
     open(dst, "wt", encoding="utf-8") as fout:
    n = 0
    for line in fin:               # 逐行讀取：一次只讀一行到記憶體
        line = line.rstrip()
        if not line:
            continue               # 跳過空行
        n += 1
        print(f"{n:02d}. {line}", file=fout)

print("---加行號後---")
print(dst.read_text(encoding="utf-8"))