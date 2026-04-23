# U04. 類檔案物件 StringIO 與逐行處理（5.6 / 5.1 逐行）
# Bloom: Understand — 知道 file-like 是鴨子型別，能把記憶體當檔案用
#
# ── 核心觀念 ──────────────────────────────────────────
# Python 的「鴨子型別（duck typing）」：
#   只要一個物件有 .read() / .write() / .seek() 等方法，
#   就可以當作「檔案」傳給任何接受 file-like 的 API。
#
# io.StringIO → 記憶體中的「假文字檔」
#   - 不會真正寫到硬碟，速度快
#   - 適合：單元測試、暫存、中間處理再一次性輸出
#   - 配合 csv / json / logging 等模組使用特別方便

import io          # 標準函式庫：提供 StringIO、BytesIO 等記憶體串流
from pathlib import Path

# ── 5.6 StringIO：記憶體裡的「假檔案」 ─────────────────
# io.StringIO() 建立一個空的記憶體文字串流
# 把它想成「可讀可寫的文字緩衝區」，用法和真實檔案幾乎一樣
buf = io.StringIO()
print("第一行", file=buf)   # print() 的 file= 參數：把輸出導向 buf 而非螢幕
print("第二行", file=buf)
print("第三行", file=buf)

# getvalue()：取出 StringIO 目前所有內容（不移動游標位置）
text = buf.getvalue()
print("---StringIO 內容---")
print(text)   # 三行文字都在裡面

# 想要重新從頭讀，要先 seek(0) 把游標移回開頭
# 原因：剛才寫入後游標在最末端，直接讀會拿到空字串
buf.seek(0)   # seek(0) = 移到第 0 個字元位置（最開頭）
for i, line in enumerate(buf, 1):   # enumerate 從 1 開始計行號
    print(i, line.rstrip())          # rstrip() 去掉每行末尾的換行符 \n

# ── StringIO 實際應用：搭配 csv 模組 ──────────────────
# csv.writer 只要求傳入「有 .write() 方法的物件」
# 所以可以傳 StringIO，不必建立真實 CSV 檔
import csv
mem = io.StringIO()
writer = csv.writer(mem)             # 建立 CSV 寫入器，輸出到記憶體
writer.writerow(["name", "score"])   # 寫入標題列
writer.writerow(["alice", 90])       # 寫入一筆資料
print("---CSV in memory---")
print(mem.getvalue())   # name,score\nalice,90\n

# ── 5.1 延伸：逐行處理檔案（大檔友善） ─────────────────
# 為何要「逐行」？
# f.read() 會一次把整個檔案載入記憶體，大檔（GB 級）會 OOM（記憶體不足）
# 直接 for line in f 則是「懶讀取」，一次只讀一行進記憶體，非常省空間

# 先造一個多行檔（故意加入空行，待會要過濾掉）
src = Path("poem.txt")
src.write_text("床前明月光\n\n疑是地上霜\n\n舉頭望明月\n低頭思故鄉\n", encoding="utf-8")

# 任務：過濾空行、加上行號、寫到新檔
dst = Path("poem_numbered.txt")
# with 同時開兩個檔案：用反斜線 \ 接續下一行（Python 語法允許在括號或 \ 後換行）
# fin  = 來源檔（只讀）
# fout = 目的檔（只寫）
with open(src, "rt", encoding="utf-8") as fin, \
     open(dst, "wt", encoding="utf-8") as fout:
    n = 0
    for line in fin:               # 每次迭代只讀一行到記憶體（含末尾 \n）
        line = line.rstrip()       # rstrip() 去掉行尾空白與換行符
        if not line:               # 去掉換行後變成空字串 → 這是空行
            continue               # 跳過空行，不計行號也不寫入
        n += 1
        # f"{n:02d}" 代表「至少顯示 2 位數，不足補零」，例如 01 / 02 ... 10 / 11
        print(f"{n:02d}. {line}", file=fout)   # 寫入目的檔

print("---加行號後---")
print(dst.read_text(encoding="utf-8"))   # 讀出結果確認
