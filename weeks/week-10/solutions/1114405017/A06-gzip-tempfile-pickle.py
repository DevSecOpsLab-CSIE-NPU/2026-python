# A06. 壓縮檔、臨時資料夾、物件序列化（5.7 / 5.19 / 5.21）
# Bloom: Apply — 能把標準庫工具組合起來解一個小任務

import gzip
import pickle
import tempfile
from pathlib import Path

# ── 5.7 讀寫壓縮檔：gzip.open 幾乎和 open 一樣 ─────────
# 使用 gzip.open 可以直接對 .gz 壓縮檔進行讀寫，
# 接口和一般 open 很相似，因此學起來方便。

# 寫入壓縮文字檔：'wt' = write text，encoding='utf-8' 用於文字編碼
with gzip.open("notes.txt.gz", "wt", encoding="utf-8") as f:
    f.write("第一行筆記\n")
    f.write("第二行筆記\n")

# 讀取壓縮文字檔：'rt' = read text，讀出來的每一行都可以像一般檔案迭代
with gzip.open("notes.txt.gz", "rt", encoding="utf-8") as f:
    for line in f:
        # rstrip() 去除行尾換行符號，方便印出時不換兩次行
        print("gz:", line.rstrip())

# gzip 也可以處理二進位資料，使用 'wb' 或 'rb'
with gzip.open("blob.bin.gz", "wb") as f:
    f.write(b"\x00\x01\x02\x03")

# 透過 Path.stat().st_size 可以取得壓縮檔的大小
print("blob size:", Path("blob.bin.gz").stat().st_size, "bytes")

# ── 5.19 臨時檔案與資料夾：離開 with 自動清理 ──────────
# 有時候想做短暫實驗，不希望在專案資料夾留下暫存檔，
# 這時候 TemporaryDirectory 很好用。
with tempfile.TemporaryDirectory() as tmp:
    # tempfile.TemporaryDirectory() 會建立一個臨時資料夾，離開 with 自動刪除
    tmp = Path(tmp)
    print("暫存資料夾:", tmp)

    # 在臨時資料夾中寫入兩個文字檔
    (tmp / "a.txt").write_text("hello\n", encoding="utf-8")
    (tmp / "b.txt").write_text("world\n", encoding="utf-8")

    # iterdir() 會列出資料夾內的所有直接子項目
    for p in tmp.iterdir():
        print("  ", p.name, "→", p.read_text(encoding="utf-8").rstrip())

# 離開 with 區塊後，TemporaryDirectory 所建立的資料夾會自動刪除
print("離開後還存在嗎？", tmp.exists())  # False

# NamedTemporaryFile 可以建立單一暫存檔
# delete=False 表示關閉後不自動刪除，方便我們示範檔案路徑
with tempfile.NamedTemporaryFile("wt", delete=False, suffix=".log",
                                 encoding="utf-8") as f:
    f.write("暫存 log\n")
    log_path = f.name
print("暫存檔位置:", log_path)
# 用完後自行刪除暫存檔，避免殘留在專案中
Path(log_path).unlink()

# ── 5.21 pickle：把 Python 物件「原樣」存檔 ────────────
# pickle 會把 Python 物件序列化成 bytes，適合存 dict、list、tuple、自訂物件等。
# 但 pickle 不是跨語言格式，也不建議用於長期儲存；若要與其他程式交換資料，
# 通常用 json 會比較安全穩定。

scores = {
    "alice": [90, 85, 92],
    "bob":   [70, 75, 80],
    "carol": [88, 91, 95],
}

# pickle.dump 會把 Python 物件寫入檔案，因為內容是 bytes，所以要用 'wb'
with open("scores.pkl", "wb") as f:
    pickle.dump(scores, f)

# pickle.load 會從檔案讀取 bytes，並復原成原本的 Python 物件
with open("scores.pkl", "rb") as f:
    loaded = pickle.load(f)

print("讀回的物件:", loaded)
# type(loaded) is dict 用來確認讀回來的物件型別是否為 dict
print("型別一致?", type(loaded) is dict)         # True
# loaded == scores 用來確認物件內容是否與原始字典相同
print("內容相等?", loaded == scores)              # True
print("alice 平均:", sum(loaded["alice"]) / 3)   # 89.0

# ⚠️ 安全提醒：pickle.load 會執行內嵌指令，
# 絕對不要對「來路不明」的 .pkl 檔做 load，否則可能發生安全風險。

# ── 課堂延伸挑戰 ───────────────────────────────────────
# 1) 把 scores 存成 gzip 壓縮後的 pickle：gzip.open('scores.pkl.gz','wb')
# 2) 用 TemporaryDirectory 跑完整流程（寫→讀→比對），不在專案留任何檔
# 3) 試著 pickle 一個 lambda，觀察錯誤訊息（pickle 不能存 lambda）
