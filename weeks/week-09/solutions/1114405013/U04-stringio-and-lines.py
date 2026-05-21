# U04. 類檔案物件 StringIO 與逐行處理（5.6 / 5.1 逐行）
# Bloom: Understand — 知道 file-like 是鴨子型別，能把記憶體當檔案用

import io
import csv
from pathlib import Path

# ── 5.6 StringIO：記憶體裡的「假檔案」 ─────────────────
# StringIO 提供一個像檔案一樣的物件，但資料存放在記憶體中，
# 不需要實際寫檔、讀檔到磁碟，非常適合測試或暫存文字資料。
buf = io.StringIO()
print("第一行", file=buf)
print("第二行", file=buf)
print("第三行", file=buf)

# getvalue() 會回傳目前記憶體中累積的整段文字內容
text = buf.getvalue()
print("---StringIO 內容---")
print(text)

# 內部指標已移到結尾，如果要重新讀取，就要 seek(0) 回到開頭
buf.seek(0)
for i, line in enumerate(buf, 1):
    # 逐行讀取 buffer，line 包含原本的換行符
    print(i, line.rstrip())

# StringIO 的好處在於它是一個「file-like」物件，
# 只要 API 接受檔案物件，就可以用 StringIO 取代真正的檔案。
# 例如 csv 模組可以直接寫到記憶體中的 StringIO。
mem = io.StringIO()
writer = csv.writer(mem)
writer.writerow(["name", "score"])
writer.writerow(["alice", 90])
print("---CSV in memory---")
print(mem.getvalue())

# ── 5.1 延伸：逐行處理檔案（大檔友善） ─────────────────
# 這裡示範用逐行讀取的方式處理檔案，避免一次把整個大檔載入記憶體。
src = Path("poem.txt")
src.write_text("床前明月光\n\n疑是地上霜\n\n舉頭望明月\n低頭思故鄉\n", encoding="utf-8")

# 目標：讀取原始詩句、過濾空行、加上行號，寫到新檔案中。
dst = Path("poem_numbered.txt")
with open(src, "rt", encoding="utf-8") as fin, \
     open(dst, "wt", encoding="utf-8") as fout:
    n = 0
    for line in fin:               # 逐行讀取：一次只讀一行，不會一次塞整個檔案
        line = line.rstrip()       # 去掉右側換行符與空白
        if not line:
            continue               # 如果是空行就跳過，不計入行號
        n += 1
        # print() 的 file 參數可以直接寫到 fout
        print(f"{n:02d}. {line}", file=fout)

print("---加行號後---")
print(dst.read_text(encoding="utf-8"))

# 小結：
# - StringIO 可以模擬檔案物件，方便測試與暫存文字資料
# - seek(0) 可以將讀寫位置重置到開頭
# - 任何接受 file-like 物件的函式都能搭配 StringIO 使用
# - 逐行讀取檔案適合大檔案，避免一次把整個檔案讀進記憶體
# - rstrip() 常用於移除每行末尾的換行符，避免輸出時多出空行
