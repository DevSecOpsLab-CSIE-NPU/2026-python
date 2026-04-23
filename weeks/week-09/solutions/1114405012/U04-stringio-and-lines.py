# U04. 類檔案物件 StringIO 與逐行處理（5.6 / 5.1 逐行）
# Bloom: Understand — 知道 file-like 是鴨子型別，能把記憶體當檔案用

import io
from pathlib import Path

# ============================================================================
# 區塊 1：StringIO（記憶體中的文字檔案）
# ----------------------------------------------------------------------------
# 目標：
# 1. 了解 StringIO 是 file-like 物件（有 write/read/seek 等介面），可當作「假檔案」。
# 2. 在不碰磁碟的情況下完成 I/O 流程，特別適合測試與暫存中間結果。
# 3. 觀察 print(file=...)、getvalue()、seek() 與逐行迭代在 StringIO 上的行為。
# ============================================================================
# ── 5.6 StringIO：記憶體裡的「假檔案」 ─────────────────
# 建立一個空的記憶體文字緩衝區。
buf = io.StringIO()
# print(..., file=buf) 會把輸出寫進 buf，而不是終端機。
print("第一行", file=buf)
print("第二行", file=buf)
print("第三行", file=buf)

# 取出整段字串
# getvalue() 可一次取得目前累積的所有文字內容。
text = buf.getvalue()
print("---StringIO 內容---")
print(text)

# 也能當讀檔用：seek 回開頭再逐行讀
# 目前游標在末端，先 seek(0) 回到開頭，才能從頭讀取。
buf.seek(0)
# enumerate(buf, 1) 會逐行迭代並從 1 開始編號。
for i, line in enumerate(buf, 1):
    # rstrip() 去除每行尾端換行，讓輸出格式更乾淨。
    print(i, line.rstrip())

# 為什麼有用？任何收 file-like 的 API（csv、json、logging）
# 都能塞 StringIO，不必真的寫到磁碟、方便測試。
import csv
# 再開一個記憶體緩衝區，示範 csv.writer 直接寫入。
mem = io.StringIO()
writer = csv.writer(mem)
writer.writerow(["name", "score"])
writer.writerow(["alice", 90])
print("---CSV in memory---")
# 直接檢視 CSV 文字結果，不需建立實體 .csv 檔案。
print(mem.getvalue())

# ============================================================================
# 區塊 2：逐行處理檔案（大檔友善）
# ----------------------------------------------------------------------------
# 目標：
# 1. 使用逐行迭代處理文字檔，避免一次讀入整檔造成記憶體壓力。
# 2. 練習常見資料清理流程：去除空白行、重新編號、輸出到新檔。
# 3. 透過 with 同時管理輸入與輸出檔案，確保自動關檔。
# ============================================================================
# ── 5.1 延伸：逐行處理檔案（大檔友善） ─────────────────
# 先造一個多行檔
src = Path("poem.txt")
# write_text() 以 UTF-8 建立範例檔案，內容包含空行供後續過濾。
src.write_text("床前明月光\n\n疑是地上霜\n\n舉頭望明月\n低頭思故鄉\n", encoding="utf-8")

# 任務：過濾空行、加上行號、寫到新檔
dst = Path("poem_numbered.txt")
# 同時開啟來源檔（讀）與目標檔（寫），離開 with 後會自動關閉。
with open(src, "rt", encoding="utf-8") as fin, \
     open(dst, "wt", encoding="utf-8") as fout:
    # n 表示「有效文字行」計數，不包含被跳過的空行。
    n = 0
    for line in fin:               # 逐行：一次只讀一行到記憶體
        # 去掉每行尾端空白與換行字元，方便判斷是否為空行。
        line = line.rstrip()
        if not line:
            continue               # 跳過空行
        n += 1
        # :02d 代表不足兩位時前面補 0，例如 01、02。
        print(f"{n:02d}. {line}", file=fout)

print("---加行號後---")
# 讀回結果檔，確認空行已被過濾且行號正確。
print(dst.read_text(encoding="utf-8"))
