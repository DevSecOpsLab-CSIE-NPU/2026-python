"""A06. 壓縮檔、臨時資料夾、物件序列化（5.7 / 5.19 / 5.21）

Bloom: Apply
學習目標：把標準庫工具組合起來，處理壓縮檔、暫存資源與物件保存。

本檔重點：
1) gzip：像 open 一樣讀寫 .gz 壓縮檔。
2) tempfile：建立臨時檔或臨時資料夾，離開作用域後自動清理。
3) pickle：把 Python 物件序列化成 bytes 存檔，再從 bytes 還原。

閱讀提醒：
- gzip.open 在文字模式時仍然要指定 encoding。
- tempfile 很適合測試與短期任務，避免專案目錄被暫存檔污染。
- pickle 適合 Python 內部保存，不適合拿來做跨語言交換或不明來源載入。
"""

import gzip
import pickle
import tempfile
from pathlib import Path

# ── 5.7 讀寫壓縮檔：gzip.open 幾乎和 open 一樣 ─────────
# 寫 .gz（文字模式要記得 encoding）
# gzip.open 回傳的是「類檔案物件」，用法與 open 非常接近。
# 這裡用 wt 代表文字寫入，內容會先用 UTF-8 編碼，再寫成 gzip 壓縮資料。
with gzip.open("notes.txt.gz", "wt", encoding="utf-8") as f:
    f.write("第一行筆記\n")
    f.write("第二行筆記\n")

# 讀回：直接逐行迭代
# rt = 文字讀取；逐行迭代的寫法與一般文字檔相同
with gzip.open("notes.txt.gz", "rt", encoding="utf-8") as f:
    for line in f:
        print("gz:", line.rstrip())

# 也能用 'wb'/'rb' 處理二進位資料
# 如果內容本來就是 bytes，就不要指定 encoding，直接用二進位模式即可
with gzip.open("blob.bin.gz", "wb") as f:
    f.write(b"\x00\x01\x02\x03")

# stat().st_size 可以看到壓縮後檔案的實際磁碟大小
print("blob size:", Path("blob.bin.gz").stat().st_size, "bytes")

# ── 5.19 臨時檔案與資料夾：離開 with 自動清理 ──────────
# 場景：想跑個小實驗但不想在專案亂留檔
# TemporaryDirectory 會建立一個暫時資料夾，離開 with 後自動刪除整個資料夾
with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)
    print("暫存資料夾:", tmp)

    # 在裡面寫幾個檔
    # 這裡示範用 pathlib 寫檔，讓暫存流程與一般檔案操作一致
    (tmp / "a.txt").write_text("hello\n", encoding="utf-8")
    (tmp / "b.txt").write_text("world\n", encoding="utf-8")

    # 列出內容
    # iterdir() 只列出當層內容，不會遞迴深入子資料夾
    for p in tmp.iterdir():
        print("  ", p.name, "→", p.read_text(encoding="utf-8").rstrip())

# 離開 with 後，tmp 已自動刪除
# 注意：tmp 變數還在，但實際對應的資料夾已經被清掉了
print("離開後還存在嗎？", tmp.exists())  # False

# 單一臨時檔：NamedTemporaryFile
# delete=False 表示離開 with 時不自動刪除，方便後續再手動處理
# suffix=".log" 讓臨時檔有副檔名，某些工具會更容易辨識
with tempfile.NamedTemporaryFile("wt", delete=False, suffix=".log",
                                 encoding="utf-8") as f:
    f.write("暫存 log\n")
    log_path = f.name
print("暫存檔位置:", log_path)
# 用完後手動刪除，避免暫存檔累積
Path(log_path).unlink()  # 用完自己刪

# ── 5.21 pickle：把 Python 物件「原樣」存檔 ────────────
# 適用：dict/list/自訂類別；不適用：跨語言、長期存檔（用 json 更穩）
# pickle 的核心是「序列化」：把 Python 物件轉成 bytes；
# load 時再把 bytes 還原成原本的 Python 物件。
scores = {
    "alice": [90, 85, 92],
    "bob":   [70, 75, 80],
    "carol": [88, 91, 95],
}

# 注意：pickle 是 bytes → 一定要 'wb'/'rb'
# dump() 會把物件寫成二進位格式，因此不能用文字模式
with open("scores.pkl", "wb") as f:
    pickle.dump(scores, f)

# load() 會讀回並還原成原本的 Python 物件
with open("scores.pkl", "rb") as f:
    loaded = pickle.load(f)

print("讀回的物件:", loaded)
print("型別一致?", type(loaded) is dict)         # True
print("內容相等?", loaded == scores)              # True
# 讀回後就能直接做一般 Python 運算
print("alice 平均:", sum(loaded["alice"]) / 3)   # 89.0

# ⚠️ 安全提醒：pickle.load 會執行內嵌指令，
# 絕對不要對「來路不明」的 .pkl 檔做 load。
# 這是 pickle 跟 json 最大的安全差異之一

# ── 課堂延伸挑戰 ───────────────────────────────────────
# 1) 把 scores 存成 gzip 壓縮後的 pickle：gzip.open('scores.pkl.gz','wb')
# 2) 用 TemporaryDirectory 跑完整流程（寫→讀→比對），不在專案留任何檔
# 3) 試著 pickle 一個 lambda，觀察錯誤訊息（pickle 不能存 lambda）
