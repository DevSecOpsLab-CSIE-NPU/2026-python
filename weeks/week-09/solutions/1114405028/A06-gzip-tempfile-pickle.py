# A06. 壓縮檔、臨時資料夾、物件序列化（5.7 / 5.19 / 5.21）
# Bloom: Apply — 能把標準庫工具組合起來解一個小任務

import gzip
import pickle
import tempfile
from pathlib import Path

# ── 5.7 讀寫壓縮檔：gzip.open 幾乎和 open 一樣 ─────────
# gzip.open 可以直接讀寫 .gz 壓縮檔，文字模式可帶 encoding
with gzip.open("notes.txt.gz", "wt", encoding="utf-8") as f:
    f.write("第一行筆記\n")
    f.write("第二行筆記\n")

# 直接用 gzip.open 讀取壓縮檔，逐行處理就像普通文字檔
with gzip.open("notes.txt.gz", "rt", encoding="utf-8") as f:
    for line in f:
        print("gz:", line.rstrip())

# 也可以使用二進位模式，寫入 bytes 資料
with gzip.open("blob.bin.gz", "wb") as f:
    f.write(b"\x00\x01\x02\x03")

print("blob size:", Path("blob.bin.gz").stat().st_size, "bytes")

# ── 5.19 臨時檔案與資料夾：離開 with 自動清理 ──────────
# TemporaryDirectory 會建立一個臨時資料夾，離開 with 後自動刪除
with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)  # 把路徑轉成 Path 方便操作
    print("暫存資料夾:", tmp)

    # 在臨時資料夾裡寫入幾個檔案
    (tmp / "a.txt").write_text("hello\n", encoding="utf-8")
    (tmp / "b.txt").write_text("world\n", encoding="utf-8")

    # 讀取並列出臨時資料夾中的檔案
    for p in tmp.iterdir():
        print("  ", p.name, "→", p.read_text(encoding="utf-8").rstrip())

# 離開 with 後，臨時資料夾與其內容會被移除
print("離開後還存在嗎？", tmp.exists())  # False

# 如果想保留單一臨時檔案，可使用 NamedTemporaryFile
with tempfile.NamedTemporaryFile("wt", delete=False, suffix=".log",
                                 encoding="utf-8") as f:
    f.write("暫存 log\n")
    log_path = f.name
print("暫存檔位置:", log_path)
Path(log_path).unlink()  # 用完後自行刪除

# ── 5.21 pickle：把 Python 物件「原樣」存檔 ────────────
# pickle 會將 Python 物件序列化為 bytes，適合儲存 dict/list/自訂類別等
# 但 pickle 不適合跨語言或長期資料交換，這時 json 更合適。
scores = {
    "alice": [90, 85, 92],
    "bob":   [70, 75, 80],
    "carol": [88, 91, 95],
}

# 寫出 pickle 檔案，必須用二進位模式 'wb'
with open("scores.pkl", "wb") as f:
    pickle.dump(scores, f)

# 讀回 pickle 檔案，必須用二進位模式 'rb'
with open("scores.pkl", "rb") as f:
    loaded = pickle.load(f)

print("讀回的物件:", loaded)
print("型別一致?", type(loaded) is dict)         # True
print("內容相等?", loaded == scores)              # True
print("alice 平均:", sum(loaded["alice"]) / 3)   # 89.0

# ⚠️ 安全提醒：pickle.load 會執行內嵌指令，
# 絕對不要對「來路不明」的 .pkl 檔做 load。

# ── 課堂延伸挑戰 ───────────────────────────────────────
# 1) 把 scores 存成 gzip 壓縮後的 pickle：gzip.open('scores.pkl.gz','wb')
# 2) 用 TemporaryDirectory 跑完整流程（寫→讀→比對），不在專案留任何檔
# 3) 試著 pickle 一個 lambda，觀察錯誤訊息（pickle 不能存 lambda）
