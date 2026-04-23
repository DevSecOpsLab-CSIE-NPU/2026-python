# U04. 類檔案物件 StringIO 與逐行處理（5.6 / 5.1 逐行）
# Bloom: Understand — 知道 file-like 是鴨子型別，能把記憶體當檔案用

import io
from pathlib import Path

# ── 5.6 StringIO：記憶體裡的「假檔案」 ─────────────────
# io.StringIO() 會建立一個「文字型」的記憶體緩衝區，
# 介面長得像檔案（支援 write/read/seek 等方法），
# 但資料存在 RAM，不會真的寫到磁碟。
buf = io.StringIO()
# print(..., file=buf) 可把輸出導向這個記憶體緩衝區。
# 與寫入真實檔案的寫法幾乎相同，便於替換與測試。
print("第一行", file=buf)
print("第二行", file=buf)
print("第三行", file=buf)

# 取出整段字串
# getvalue() 會回傳目前緩衝區中的完整文字內容（str）。
text = buf.getvalue()
print("---StringIO 內容---")
print(text)

# 也能當讀檔用：seek 回開頭再逐行讀
# StringIO 也有「檔案游標」概念。
# 前面連續 write 後，游標已在尾端；若要重新讀，必須先 seek(0) 回到開頭。
buf.seek(0)
# enumerate(buf, 1) 會在逐行讀取時同時產生 1 起始的行號。
for i, line in enumerate(buf, 1):
    # line 通常帶有行尾換行符，rstrip() 可避免 print 額外空行。
    print(i, line.rstrip())

# 為什麼有用？任何收 file-like 的 API（csv、json、logging）
# 都能塞 StringIO，不必真的寫到磁碟、方便測試。
import csv
mem = io.StringIO()
# csv.writer 只要求目標物件有 write()，
# 因此 StringIO 可直接作為 CSV 輸出目的地（典型 duck typing）。
writer = csv.writer(mem)
writer.writerow(["name", "score"])
writer.writerow(["alice", 90])
print("---CSV in memory---")
print(mem.getvalue())

# ── 5.1 延伸：逐行處理檔案（大檔友善） ─────────────────
# 先造一個多行檔
src = Path("poem.txt")
# write_text() 會一次把整段文字寫入檔案。
# 這裡刻意放入空白行，後續示範如何過濾。
src.write_text("床前明月光\n\n疑是地上霜\n\n舉頭望明月\n低頭思故鄉\n", encoding="utf-8")

# 任務：過濾空行、加上行號、寫到新檔
dst = Path("poem_numbered.txt")
# 同一個 with 內同時開啟輸入與輸出檔：
# - fin: 來源檔（讀）
# - fout: 目標檔（寫，覆寫模式）
# 區塊結束會自動關閉兩個檔案。
with open(src, "rt", encoding="utf-8") as fin, \
     open(dst, "wt", encoding="utf-8") as fout:
    n = 0
    for line in fin:               # 逐行：一次只讀一行到記憶體
        # 去除行尾換行，方便後續判斷空行與格式化輸出。
        line = line.rstrip()
        if not line:
            continue               # 跳過空行
        n += 1
        # {n:02d}：數字補零到兩位，輸出如 01、02、03。
        print(f"{n:02d}. {line}", file=fout)

print("---加行號後---")
# read_text() 適合小檔示範；大檔仍建議採逐行讀取。
print(dst.read_text(encoding="utf-8"))
