# U04. 類檔案物件 StringIO 與逐行處理（5.6 / 5.1 逐行）
# Bloom: Understand — 知道 file-like 是鴨子型別，能把記憶體當檔案用

# 匯入 io 模組（提供記憶體中的「類檔案物件」）
import io

# 匯入 Path（用於實際檔案操作）
from pathlib import Path

# ── 5.6 StringIO：記憶體裡的「假檔案」 ─────────────────

# 建立一個 StringIO 物件（存在記憶體中，不會真的產生檔案）
# 它的行為就像 open() 出來的檔案物件
buf = io.StringIO()

# print(..., file=buf)
# 將輸出寫入「記憶體中的檔案」而不是螢幕或磁碟
print("第一行", file=buf)
print("第二行", file=buf)
print("第三行", file=buf)

# getvalue()：把目前緩衝區的所有內容取出（回傳一個字串）
text = buf.getvalue()

print("---StringIO 內容---")
print(text)

# StringIO 也可以像檔案一樣「讀取」
# seek(0)：把游標移回開頭（很重要，否則會從尾端開始讀）
buf.seek(0)

# enumerate(buf, 1)
# → 逐行讀取，並從 1 開始編號
for i, line in enumerate(buf, 1):
    # rstrip() 去掉行尾的換行符號
    print(i, line.rstrip())

# 為什麼有用？
# 「file-like（類檔案物件）」= 只要有 read/write 介面即可
# 許多函式（csv、json、logging）只要求「像檔案」，不一定是真的檔案
# → 可以用 StringIO 取代實體檔案（測試更方便、不用 IO 成本）

# 匯入 csv 模組
import csv

# 再建立一個記憶體中的檔案
mem = io.StringIO()

# csv.writer 需要一個「可寫入的檔案物件」
# 這裡直接給 StringIO（完全合法）
writer = csv.writer(mem)

# 寫入 CSV 標頭
writer.writerow(["name", "score"])

# 寫入資料列
writer.writerow(["alice", 90])

print("---CSV in memory---")

# 取出記憶體中的 CSV 內容
print(mem.getvalue())

# ── 5.1 延伸：逐行處理檔案（大檔友善） ─────────────────

# 建立一個 Path 物件，代表來源檔案
src = Path("poem.txt")

# write_text()：一次寫入整個文字檔（會覆蓋原內容）
# 這裡包含空行（\n\n）
src.write_text("床前明月光\n\n疑是地上霜\n\n舉頭望明月\n低頭思故鄉\n", encoding="utf-8")

# 建立目標檔案 Path
dst = Path("poem_numbered.txt")

# 同時開兩個檔案：
# fin：讀取來源檔（rt = read text）
# fout：寫入目標檔（wt = write text）
# "\" 是換行接續符號（讓 with 可以寫在兩行）
with open(src, "rt", encoding="utf-8") as fin, \
     open(dst, "wt", encoding="utf-8") as fout:

    # 行號計數器
    n = 0

    # 逐行讀取來源檔（節省記憶體，適合大檔案）
    for line in fin:
        # 去掉行尾空白與換行
        line = line.rstrip()

        # 如果是空行（空字串）
        if not line:
            continue               # 跳過，不做任何處理

        # 行號 +1
        n += 1

        # 寫入新檔案，格式化輸出：
        # {n:02d} → 兩位數，不足補 0（01, 02, 03...）
        print(f"{n:02d}. {line}", file=fout)

print("---加行號後---")

# 讀取結果檔並印出
print(dst.read_text(encoding="utf-8"))