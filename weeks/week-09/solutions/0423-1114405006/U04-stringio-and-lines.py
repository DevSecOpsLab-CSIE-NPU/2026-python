"""U04. 類檔案物件 StringIO 與逐行處理（5.6 / 5.1 逐行）

Bloom: Understand
學習目標：
1) 理解 file-like（類檔案物件）與鴨子型別概念。
2) 會用 io.StringIO 在記憶體中模擬文字檔讀寫。
3) 掌握逐行處理大檔的基本模式（過濾、轉換、輸出）。

核心觀念：
- 只要物件提供 read/write/seek 等介面，就能被很多函式當成檔案使用。
- StringIO 適合測試、暫存、組裝輸出，不需要真的建立磁碟檔案。
- 真實檔案處理時，逐行讀取可降低記憶體占用，對大檔更安全。
"""

import io
from pathlib import Path

# ── 5.6 StringIO：記憶體裡的「假檔案」 ─────────────────
# StringIO 預設是空的文字緩衝區，行為很像 open(..., "wt+") 取得的檔案物件
buf = io.StringIO()
# print(..., file=buf) 會把文字寫到 buf，而不是終端機
print("第一行", file=buf)
print("第二行", file=buf)
print("第三行", file=buf)

# 取出整段字串
# getvalue() 會回傳目前緩衝區中的完整文字內容（str）
text = buf.getvalue()
print("---StringIO 內容---")
print(text)

# 也能當讀檔用：seek 回開頭再逐行讀
# 寫完後游標在尾端，若要從頭讀必須先 seek(0)
buf.seek(0)
# enumerate(buf, 1) 讓行號從 1 開始，符合人類閱讀習慣
for i, line in enumerate(buf, 1):
    # line 內通常含有結尾 \n，這裡用 rstrip() 去除後再顯示
    print(i, line.rstrip())

# 為什麼有用？任何收 file-like 的 API（csv、json、logging）
# 都能塞 StringIO，不必真的寫到磁碟、方便測試。
import csv

# 再建立一個記憶體緩衝區，示範 csv 模組直接輸出到記憶體
mem = io.StringIO()
writer = csv.writer(mem)
writer.writerow(["name", "score"])
writer.writerow(["alice", 90])
print("---CSV in memory---")
# 輸出結果會是標準 CSV 格式字串
print(mem.getvalue())

# ── 5.1 延伸：逐行處理檔案（大檔友善） ─────────────────
# 先造一個多行檔
src = Path("poem.txt")
src.write_text("床前明月光\n\n疑是地上霜\n\n舉頭望明月\n低頭思故鄉\n", encoding="utf-8")

# 任務：過濾空行、加上行號、寫到新檔
dst = Path("poem_numbered.txt")
with open(src, "rt", encoding="utf-8") as fin, \
     open(dst, "wt", encoding="utf-8") as fout:
    # n 是「有效行」計數器（空行不算）
    n = 0
    for line in fin:               # 逐行：一次只讀一行到記憶體
        # 去掉每行尾端換行，方便判斷空行與重新格式化
        line = line.rstrip()
        if not line:
            continue               # 跳過空行
        n += 1
        # :02d 表示補零到 2 位，例如 1 -> 01、9 -> 09
        print(f"{n:02d}. {line}", file=fout)

print("---加行號後---")
# 最後讀回結果檔，確認轉換流程是否正確
print(dst.read_text(encoding="utf-8"))
