# A06. 壓縮檔、臨時資料夾、物件序列化（5.7 / 5.19 / 5.21）
# Bloom: Apply — 能把標準庫工具組合起來解一個小任務
# 本範例介紹 gzip 壓縮檔、tempfile 臨時資料夾、以及 pickle 物件序列化

import gzip
import pickle
import tempfile
from pathlib import Path

# ── 5.7 讀寫壓縮檔：gzip.open 幾乎和 open 一樣 ─────────
#  gzip.open 的使用方式與一般 open 類似，支援文字模式和二進位模式
#  寫入 .gz 壓縮檔（文字模式要記得 encoding）
with gzip.open("notes.txt.gz", "wt", encoding="utf-8") as f:
    f.write("第一行筆記\n")
    f.write("第二行筆記\n")
#  讀回：直接逐行迭代（與一般檔案相同）
with gzip.open("notes.txt.gz", "rt", encoding="utf-8") as f:
    for line in f:
        print("gz:", line.rstrip())

#  也能用 'wb'/'rb' 處理二進位資料
with gzip.open("blob.bin.gz", "wb") as f:
    f.write(b"\x00\x01\x02\x03")

print("blob size:", Path("blob.bin.gz").stat().st_size, "bytes")

# ── 5.19 臨時檔案與資料夾：離開 with 自動清理 ──────────
#  場景：想跑個小實驗但不想在專案亂留檔
#  tempfile.TemporaryDirectory：自動建立並在離開 with 區塊後刪除
with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)
    print("暫存資料夾:", tmp)

    # 在裡面寫幾個檔
    (tmp / "a.txt").write_text("hello\n", encoding="utf-8")
    (tmp / "b.txt").write_text("world\n", encoding="utf-8")

    # 列出內容
    for p in tmp.iterdir():
        print("  ", p.name, "→", p.read_text(encoding="utf-8").rstrip())

# 離開 with 後，tmp 已自動刪除
print("離開後還存在嗎？", tmp.exists())  # False

# 單一臨時檔：NamedTemporaryFile
#  delete=False 表示離開區塊後不自動刪除，需手動處理
with tempfile.NamedTemporaryFile("wt", delete=False, suffix=".log",
                             encoding="utf-8") as f:
    f.write("暫存 log\n")
    log_path = f.name
print("暫存檔位置:", log_path)
Path(log_path).unlink()  # 用完自己刪

# ── 5.21 pickle：把 Python 物件「原樣」存檔 ────────────
#  pickle 是 Python 專用的序列化模組，可將物件完整存入檔案
#  適用：dict/list/自訂類別物件
#  不適用：跨語言、長期存檔（建議用 json 更穩定）
scores = {
    "alice": [90, 85, 92],
    "bob":   [70, 75, 80],
    "carol": [88, 91, 95],
}

# 注意：pickle 序列化後是 bytes → 一定要用 'wb' 寫入/'rb' 讀取
with open("scores.pkl", "wb") as f:
    pickle.dump(scores, f)

with open("scores.pkl", "rb") as f:
    loaded = pickle.load(f)

print("讀回的物件:", loaded)
print("型別一致?", type(loaded) is dict)         # True
print("內容相等?", loaded == scores)              # True
print("alice 平均:", sum(loaded["alice"]) / 3)   # 89.0

# ⚠️ 安全提醒：pickle.load 會執行內嵌程式碼，
# 絕對不要對「來路不明」的 .pkl 檔做 load，以免安全風險。

# ── 課堂延伸挑戰 ───────────────────────────────────────
# 1) 把 scores 存成 gzip 壓縮後的 pickle：gzip.open('scores.pkl.gz','wb')
# 2) 用 TemporaryDirectory 跑完整流程（寫→讀→比對），不在專案留任何檔
# 3) 試著 pickle 一個 lambda，觀察錯誤訊息（pickle 不能存 lambda）