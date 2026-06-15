"""
U04. 類檔案物件 StringIO 與逐行處理（5.6 / 5.1 逐行）
Bloom: Understand

本檔示範：
1) StringIO：把記憶體中的字串當成檔案來寫/讀。
2) file-like（鴨子型別）概念：只要介面像檔案就可被許多 API 接受。
3) 逐行處理真實檔案：過濾、編號、輸出新檔。
"""

import io
from pathlib import Path

# ── 5.6 StringIO：記憶體裡的「假檔案」 ─────────────────
# StringIO 建立後，可像一般文字檔案一樣給 print/write 使用。
buf = io.StringIO()
print("第一行", file=buf)
print("第二行", file=buf)
print("第三行", file=buf)

# getvalue() 可一次取得目前緩衝區的完整字串內容
text = buf.getvalue()
print("---StringIO 內容---")
print(text)

# 也能當讀檔用：seek(0) 回到開頭再逐行讀
buf.seek(0)
for i, line in enumerate(buf, 1):
    print(i, line.rstrip())

# 為什麼有用？任何收 file-like 的 API（csv、json、logging）
# 都能塞 StringIO，不必真的寫到磁碟，測試更快、也更乾淨。
import csv
mem = io.StringIO()
writer = csv.writer(mem)
writer.writerow(["name", "score"])
writer.writerow(["alice", 90])
print("---CSV in memory---")
print(mem.getvalue())

# ── 5.1 延伸：逐行處理檔案（大檔友善） ─────────────────
# 先造一個多行檔，包含空行，方便示範過濾流程。
src = Path("poem.txt")
src.write_text("床前明月光\n\n疑是地上霜\n\n舉頭望明月\n低頭思故鄉\n", encoding="utf-8")

# 任務：過濾空行、加上行號、寫到新檔
dst = Path("poem_numbered.txt")
with open(src, "rt", encoding="utf-8") as fin, \
     open(dst, "wt", encoding="utf-8") as fout:
    n = 0
    # 逐行處理：一次只讀一行到記憶體，適合大型檔案
    for line in fin:
        line = line.rstrip()
        if not line:
            continue               # 跳過空行
        n += 1
        # :02d 代表兩位數，不足補 0（01, 02, 03...）
        print(f"{n:02d}. {line}", file=fout)

print("---加行號後---")
print(dst.read_text(encoding="utf-8"))
