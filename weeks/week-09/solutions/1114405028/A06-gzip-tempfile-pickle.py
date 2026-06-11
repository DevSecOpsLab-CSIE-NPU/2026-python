# A06-gzip-tempfile-pickle.py
# 完整繁體中文註釋版：示範 gzip 壓縮、臨時資料夾與 pickle 序列化

import gzip
import pickle
import tempfile
from pathlib import Path

# ── 5.7 讀寫壓縮檔：gzip.open 的使用方式類似 open ───────────
with gzip.open("notes.txt.gz", "wt", encoding="utf-8") as f:
    f.write("第一行筆記\n")
    f.write("第二行筆記\n")

# 讀取 gzip 壓縮檔，一樣可以逐行迭代
with gzip.open("notes.txt.gz", "rt", encoding="utf-8") as f:
    for line in f:
        print("gz:", line.rstrip())

# 也可以用二進位模式寫入非文字內容
with gzip.open("blob.bin.gz", "wb") as f:
    f.write(b"\x00\x01\x02\x03")

print("blob size:", Path("blob.bin.gz").stat().st_size, "bytes")

# ── 5.19 臨時檔案與資料夾：離開 with 後自動清理 ─────────────
with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)
    print("暫存資料夾:", tmp)

    # 在臨時資料夾內建立兩個測試檔
    (tmp / "a.txt").write_text("hello\n", encoding="utf-8")
    (tmp / "b.txt").write_text("world\n", encoding="utf-8")

    # 列出暫存資料夾內容並讀取文字
    for p in tmp.iterdir():
        print("  ", p.name, "→", p.read_text(encoding="utf-8").rstrip())

# 離開 TemporaryDirectory 之後，資料夾會自動刪除
print("離開後還存在嗎？", tmp.exists())  # False

# 單一臨時檔：NamedTemporaryFile
with tempfile.NamedTemporaryFile("wt", delete=False, suffix=".log",
                                 encoding="utf-8") as f:
    f.write("暫存 log\n")
    log_path = f.name
print("暫存檔位置:", log_path)
Path(log_path).unlink()  # 用完後自行刪除

# ── 5.21 pickle：將 Python 物件序列化到檔案，再讀回
scores = {
    "alice": [90, 85, 92],
    "bob":   [70, 75, 80],
    "carol": [88, 91, 95],
}

with open("scores.pkl", "wb") as f:
    pickle.dump(scores, f)  # pickle 會把 Python 物件轉成 bytes

with open("scores.pkl", "rb") as f:
    loaded = pickle.load(f)

print("讀回的物件:", loaded)
print("型別一致?", type(loaded) is dict)
print("內容相等?", loaded == scores)
print("alice 平均:", sum(loaded["alice"]) / 3)

# 安全提醒：pickle.load 會執行內部序列化資料中的指令，
# 不要對不可信來源的 pickle 檔案使用 load。

# ── 課堂延伸挑戰 ─────────────────────────────────────
# 1) 把 scores 存成 gzip 壓縮後的 pickle：gzip.open('scores.pkl.gz','wb')
# 2) 用 TemporaryDirectory 跑完整流程（寫→讀→比對），不在專案留任何檔案
# 3) 試著 pickle 一個 lambda，觀察是否會失敗
