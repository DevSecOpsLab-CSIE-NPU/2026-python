# A06. 壓縮檔、臨時資料夾、物件序列化（5.7 / 5.19 / 5.21）
# Bloom: Apply — 能把標準庫工具組合起來解一個小任務

import gzip
import pickle
import tempfile
from pathlib import Path

# ── 5.7 讀寫壓縮檔：gzip.open 幾乎和 open 一樣 ─────────
# gzip.open 可以直接讀寫 .gz 壓縮檔，與 open 的使用方式非常類似。
# 文字模式時要指定 encoding，否則在 Python 3 中會因為預設二進位模式而出錯。

with gzip.open("notes.txt.gz", "wt", encoding="utf-8") as f:
    # 'wt' 表示 write text，寫入文字並自動壓縮
    f.write("第一行筆記\n")
    f.write("第二行筆記\n")

# 讀回壓縮檔，同樣使用 gzip.open 並指定 'rt' 模式
with gzip.open("notes.txt.gz", "rt", encoding="utf-8") as f:
    for line in f:
        # rstrip() 去掉右側換行符，避免 print 再多一個空行
        print("gz:", line.rstrip())

# gzip 也可以處理二進位資料，使用 'wb' / 'rb'
with gzip.open("blob.bin.gz", "wb") as f:
    f.write(b"\x00\x01\x02\x03")

# 可以看到壓縮後檔案的大小，通常會比原始資料小一些
print("blob size:", Path("blob.bin.gz").stat().st_size, "bytes")

# ── 5.19 臨時檔案與資料夾：離開 with 自動清理 ──────────
# TemporaryDirectory 會建立一個可用的暫存資料夾，離開 with 區塊後自動刪除
with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)
    print("暫存資料夾:", tmp)

    # 在暫存資料夾中建立兩個檔案
    (tmp / "a.txt").write_text("hello\n", encoding="utf-8")
    (tmp / "b.txt").write_text("world\n", encoding="utf-8")

    # 讀回並列出暫存資料夾內的檔案內容
    for p in tmp.iterdir():
        print("  ", p.name, "→", p.read_text(encoding="utf-8").rstrip())

# 離開 with 後，python 會自動刪除整個暫存資料夾與裡面的檔案
print("離開後還存在嗎？", tmp.exists())  # False

# NamedTemporaryFile 可以建立一個臨時檔案，適合需要單一檔案的情境
# delete=False 表示關閉檔案後不要立即刪除，方便後續手動處理
with tempfile.NamedTemporaryFile("wt", delete=False, suffix=".log",
                                 encoding="utf-8") as f:
    f.write("暫存 log\n")
    log_path = f.name
print("暫存檔位置:", log_path)
# 這裡示範用完後自己刪除暫存檔案
Path(log_path).unlink()

# ── 5.21 pickle：把 Python 物件「原樣」存檔 ────────────
# pickle 可以把 Python 物件序列化成二進位資料，之後再還原成原本物件。
# 適用於存取 dict、list、tuple、自訂類別物件等；不適合跨語言或長期儲存。
# 若只要儲存簡單資料結構，json 通常更容易移植。

scores = {
    "alice": [90, 85, 92],
    "bob":   [70, 75, 80],
    "carol": [88, 91, 95],
}

# pickle.dump() 會把物件寫成二進位內容，因此要用 'wb'
with open("scores.pkl", "wb") as f:
    pickle.dump(scores, f)

# pickle.load() 會從檔案讀出二進位，並重新還原成 Python 物件
with open("scores.pkl", "rb") as f:
    loaded = pickle.load(f)

print("讀回的物件:", loaded)
print("型別一致?", type(loaded) is dict)         # True
print("內容相等?", loaded == scores)              # True
print("alice 平均:", sum(loaded["alice"]) / 3)   # 89.0

# 安全提醒：pickle.load() 會執行序列化資料中的指令碼，
# 所以不要對來路不明的 pickle 檔案進行載入。
# 若要分享資料給其他程式或其他語言，請改用 csv / json / msgpack 等格式。

# ── 課堂延伸挑戰 ───────────────────────────────────────
# 1) 把 scores 存成 gzip 壓縮後的 pickle：
#    with gzip.open('scores.pkl.gz', 'wb') as f: pickle.dump(scores, f)
# 2) 用 TemporaryDirectory 跑完整流程（寫→讀→比對），不在專案留任何檔
#    先用 tempfile.TemporaryDirectory() 產生暫存資料夾，再在裡面寫入與讀回 pickle。
# 3) 試著 pickle 一個 lambda，觀察錯誤訊息（pickle 不能存 lambda）
