# U04. 類檔案物件 StringIO 與逐行處理（5.6 / 5.1 逐行）
# Bloom: Understand — 知道 file-like 是鴨子型別，能把記憶體當檔案用

import io
from pathlib import Path

# ── 5.6 StringIO：記憶體裡的「假檔案」 ─────────────────
# StringIO 提供一個類似檔案的介面，但資料存在記憶體中。
buf = io.StringIO()
print("第一行", file=buf)
print("第二行", file=buf)
print("第三行", file=buf)

# 取出整段字串，這和讀實體檔案不同：資料已經在記憶體裡。
text = buf.getvalue()
print("---StringIO 內容---")
print(text)

# 也能當讀檔用：seek 回到開頭後再逐行讀取
buf.seek(0)
for i, line in enumerate(buf, 1):
    print(i, line.rstrip())

# 為什麼有用？任何接受 file-like 物件的 API 都能使用 StringIO。
# 例如 csv、json、logging 測試時可以不用真實檔案。
import csv
mem = io.StringIO()
writer = csv.writer(mem)
writer.writerow(["name", "score"])
writer.writerow(["alice", 90])
print("---CSV in memory---")
print(mem.getvalue())

# ── 5.1 延伸：逐行處理檔案（大檔友善） ─────────────────
# 先建立一個多行文字檔，方便示範逐行讀寫。
src = Path("poem.txt")
src.write_text("床前明月光\n\n疑是地上霜\n\n舉頭望明月\n低頭思故鄉\n", encoding="utf-8")

# 任務：讀取原本的詩，過濾空行、加上行號，再寫到新檔。
dst = Path("poem_numbered.txt")
with open(src, "rt", encoding="utf-8") as fin, \
     open(dst, "wt", encoding="utf-8") as fout:
    n = 0
    for line in fin:               # 逐行讀取檔案，記憶體使用量穩定
        line = line.rstrip()        # 去掉每行結尾的 \\n
        if not line:
            continue               # 空白行不寫入輸出檔

        n += 1
        print(f"{n:02d}. {line}", file=fout)

print("---加行號後---")
print(dst.read_text(encoding="utf-8"))
