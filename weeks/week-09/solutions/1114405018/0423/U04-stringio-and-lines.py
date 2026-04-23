# U04. 類檔案物件 StringIO 與逐行處理（5.6 / 5.1 逐行）
# Bloom: Understand — 知道 file-like 是鴨子型別，能把記憶體當檔案用

# io 模組提供很多輸入輸出工具；這裡最重要的是 StringIO，
# 它可以讓我們在「記憶體中」建立一個像檔案一樣的物件。
# Path 這裡用來建立與讀寫實際檔案。
import io
from pathlib import Path

# ── 5.6 StringIO：記憶體裡的「假檔案」 ─────────────────
# StringIO 是文字版的檔案緩衝區：
# - 可以像檔案一樣 write()
# - 可以像檔案一樣 read()/逐行迭代
# - 但內容其實存在記憶體裡，不會寫到硬碟
buf = io.StringIO()
# print(..., file=buf) 會把輸出寫進 StringIO，而不是印到螢幕。
# 這對測試、暫存資料、模擬檔案非常方便。
print("第一行", file=buf)
print("第二行", file=buf)
print("第三行", file=buf)

# 取出整段字串
# getvalue() 會把目前緩衝區的全部內容一次拿出來，型別是 str。
text = buf.getvalue()
print("---StringIO 內容---")
print(text)

# 也能當讀檔用：seek 回開頭再逐行讀
# seek(0) 表示把「游標」移回檔案開頭。
# 因為前面 getvalue() 或 write() 後，游標通常已在結尾；
# 若不回到開頭，後面的迭代可能會讀不到任何內容。
buf.seek(0)
# StringIO 可以直接被 for 迴圈逐行走訪，和真正檔案物件的用法一致。
for i, line in enumerate(buf, 1):
    # enumerate(..., 1) 讓行號從 1 開始，而不是預設的 0。
    # line.rstrip() 去掉右側換行，輸出比較乾淨。
    print(i, line.rstrip())

# 為什麼有用？任何收 file-like 的 API（csv、json、logging）
# 都能塞 StringIO，不必真的寫到磁碟、方便測試。
import csv
# csv.writer 只需要一個「像檔案的物件」；StringIO 完全符合這個需求。
# 這就是所謂的 file-like object（類檔案物件）：只要介面像就可以用。
mem = io.StringIO()
writer = csv.writer(mem)
writer.writerow(["name", "score"])
writer.writerow(["alice", 90])
print("---CSV in memory---")
# CSV 內容仍然存在記憶體中，因此可直接印出來檢查。
print(mem.getvalue())

# ── 5.1 延伸：逐行處理檔案（大檔友善） ─────────────────
# 先造一個多行檔
# Path.write_text() 會直接把文字寫進檔案，這裡用它先做一個測試檔。
src = Path("poem.txt")
src.write_text("床前明月光\n\n疑是地上霜\n\n舉頭望明月\n低頭思故鄉\n", encoding="utf-8")

# 任務：過濾空行、加上行號、寫到新檔
# 這段示範的是「逐行處理」：
# - 不一次把整個檔案讀進記憶體
# - 對大檔更省 RAM，也更適合串流處理
dst = Path("poem_numbered.txt")
# with 同時開啟來源檔與輸出檔，讀一行就處理一行，再立刻寫出去。
with open(src, "rt", encoding="utf-8") as fin, \
     open(dst, "wt", encoding="utf-8") as fout:
    # n 用來記錄非空行的行號；只在保留的行上遞增。
    n = 0
    for line in fin:               # 逐行：一次只讀一行到記憶體
        # rstrip() 去掉行尾換行，讓後續判斷與輸出更乾淨。
        line = line.rstrip()
        # 空行在教學文字處理中很常見，這裡示範如何略過它們。
        if not line:
            continue               # 跳過空行
        n += 1
        # 格式化字串 {n:02d} 表示兩位數、不足補 0，例如 01、02。
        # file=fout 代表把結果寫到輸出檔，而不是標準輸出。
        print(f"{n:02d}. {line}", file=fout)

print("---加行號後---")
# 讀回處理後的檔案，確認結果是否符合預期。
print(dst.read_text(encoding="utf-8"))
