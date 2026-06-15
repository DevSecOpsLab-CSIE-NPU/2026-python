"""
A06. 壓縮檔、臨時資料夾、物件序列化（5.7 / 5.19 / 5.21）
Bloom: Apply

本檔串接三個非常常用的標準庫工具：
1) gzip：把檔案壓縮成 .gz，節省空間。
2) tempfile：建立自動清理的暫存檔/暫存目錄。
3) pickle：把 Python 物件序列化為二進位檔案。
"""

import gzip
import pickle
import tempfile
from pathlib import Path

# ── 5.7 讀寫壓縮檔：gzip.open 幾乎和 open 一樣 ─────────
# 寫 .gz（文字模式要記得 encoding）
# "wt" = write text：你操作的是字串 str，gzip 會幫你壓縮。
with gzip.open("notes.txt.gz", "wt", encoding="utf-8") as f:
    f.write("第一行筆記\n")
    f.write("第二行筆記\n")

# 讀回：用 "rt" 文字模式，直接逐行迭代
with gzip.open("notes.txt.gz", "rt", encoding="utf-8") as f:
    for line in f:
        print("gz:", line.rstrip())

# 也能用 "wb"/"rb" 處理二進位資料（bytes）
with gzip.open("blob.bin.gz", "wb") as f:
    # 直接寫原始位元組，常見於影像/模型/封包資料
    f.write(b"\x00\x01\x02\x03")

# 檢查壓縮後檔案大小（單位 bytes）
print("blob size:", Path("blob.bin.gz").stat().st_size, "bytes")

# ── 5.19 臨時檔案與資料夾：離開 with 自動清理 ──────────
# 場景：想跑個小實驗但不想在專案亂留檔
with tempfile.TemporaryDirectory() as tmp:
    # tempfile 回傳的是字串路徑；轉成 Path 方便後續運算
    tmp = Path(tmp)
    print("暫存資料夾:", tmp)

    # 在暫存目錄裡建立測試檔案
    (tmp / "a.txt").write_text("hello\n", encoding="utf-8")
    (tmp / "b.txt").write_text("world\n", encoding="utf-8")

    # 列出暫存目錄內容並讀回
    for p in tmp.iterdir():
        print("  ", p.name, "→", p.read_text(encoding="utf-8").rstrip())

# 離開 with 後，TemporaryDirectory 會自動刪除整個資料夾
print("離開後還存在嗎？", tmp.exists())  # False

# 單一臨時檔：NamedTemporaryFile
# delete=False 表示離開 with 不自動刪，方便你拿路徑做後續處理。
with tempfile.NamedTemporaryFile("wt", delete=False, suffix=".log",
                                 encoding="utf-8") as f:
    f.write("暫存 log\n")
    log_path = f.name
print("暫存檔位置:", log_path)
# 既然選擇不自動刪，就要手動清理
Path(log_path).unlink()  # 用完自己刪

# ── 5.21 pickle：把 Python 物件「原樣」存檔 ────────────
# 適用：dict/list/自訂類別；不適用：跨語言、長期存檔（用 json 更穩）
# 這裡用字典 + 串列示範。
scores = {
    "alice": [90, 85, 92],
    "bob":   [70, 75, 80],
    "carol": [88, 91, 95],
}

# 注意：pickle 是 bytes，因此檔案模式一定要是 "wb"/"rb"
with open("scores.pkl", "wb") as f:
    pickle.dump(scores, f)

with open("scores.pkl", "rb") as f:
    loaded = pickle.load(f)

print("讀回的物件:", loaded)
print("型別一致?", type(loaded) is dict)         # True
print("內容相等?", loaded == scores)              # True
print("alice 平均:", sum(loaded["alice"]) / 3)   # 89.0

# ⚠️ 安全提醒：pickle.load 可能執行惡意物件內的還原邏輯，
# 絕對不要對「來路不明」的 .pkl 檔做 load。

# ── 課堂延伸挑戰 ───────────────────────────────────────
# 1) 把 scores 存成 gzip 壓縮後的 pickle：gzip.open('scores.pkl.gz','wb')
# 2) 用 TemporaryDirectory 跑完整流程（寫→讀→比對），不在專案留任何檔
# 3) 試著 pickle 一個 lambda，觀察錯誤訊息（pickle 不能存 lambda）
