# A06. 壓縮檔、臨時資料夾、物件序列化（5.7 / 5.19 / 5.21）
# Bloom: Apply — 能把標準庫工具組合起來解一個小任務

# gzip：處理 .gz 壓縮檔
# pickle：把 Python 物件序列化成 bytes / 再還原回 Python 物件
# tempfile：建立臨時檔案與暫存資料夾，離開作用域後可自動清理
# Path：方便做檔案大小、路徑操作
import gzip
import pickle
import tempfile
from pathlib import Path

# ── 5.7 讀寫壓縮檔：gzip.open 幾乎和 open 一樣 ─────────
# 寫 .gz（文字模式要記得 encoding）
# gzip.open() 的介面和 open() 很像，但它會在底層自動做壓縮/解壓縮。
# 文字模式 'wt' / 'rt' 要搭配 encoding，因為內容本質上仍是文字。
with gzip.open("notes.txt.gz", "wt", encoding="utf-8") as f:
    # 寫入兩行中文筆記；實際存進檔案時會先被編碼，再壓縮成 .gz。
    f.write("第一行筆記\n")
    f.write("第二行筆記\n")

# 讀回：直接逐行迭代
with gzip.open("notes.txt.gz", "rt", encoding="utf-8") as f:
    # 讀取壓縮檔時，gzip 會先解壓縮，再把結果當文字逐行提供。
    for line in f:
        print("gz:", line.rstrip())

# 也能用 'wb'/'rb' 處理二進位資料
# 若資料本身不是文字（例如原始 bytes、圖片片段），就用二進位模式。
with gzip.open("blob.bin.gz", "wb") as f:
    f.write(b"\x00\x01\x02\x03")

# stat().st_size 會回傳檔案大小（位元組數）。
# 壓縮後檔案通常會比原始資料更大或更小，取決於內容是否容易壓縮。
print("blob size:", Path("blob.bin.gz").stat().st_size, "bytes")

# ── 5.19 臨時檔案與資料夾：離開 with 自動清理 ──────────
# 場景：想跑個小實驗但不想在專案亂留檔
# TemporaryDirectory() 會建立一個暫存資料夾，離開 with 後自動刪除。
with tempfile.TemporaryDirectory() as tmp:
    # 剛建立時回傳的是字串路徑，轉成 Path 後比較好操作。
    tmp = Path(tmp)
    print("暫存資料夾:", tmp)

    # 在裡面寫幾個檔
    # write_text() 直接把內容寫進檔案；這裡示範暫存資料夾內的檔案操作。
    (tmp / "a.txt").write_text("hello\n", encoding="utf-8")
    (tmp / "b.txt").write_text("world\n", encoding="utf-8")

    # 列出內容
    # iterdir() 只列出當層內容，不會遞迴子目錄。
    for p in tmp.iterdir():
        print("  ", p.name, "→", p.read_text(encoding="utf-8").rstrip())

# 離開 with 後，tmp 已自動刪除
# 這裡的 tmp 變數仍存在，但實際資料夾已經不在磁碟上了。
print("離開後還存在嗎？", tmp.exists())  # False

# 單一臨時檔：NamedTemporaryFile
# NamedTemporaryFile 會建立一個「有名字」的暫存檔。
# delete=False 代表離開 with 時不要自動刪，方便後續再次讀取或示範手動刪除。
with tempfile.NamedTemporaryFile("wt", delete=False, suffix=".log",
                                 encoding="utf-8") as f:
    f.write("暫存 log\n")
    # f.name 是實際檔案路徑，常用來把暫存檔交給其他函式處理。
    log_path = f.name
print("暫存檔位置:", log_path)
# 用完之後手動刪掉，避免暫存檔殘留。
Path(log_path).unlink()  # 用完自己刪

# ── 5.21 pickle：把 Python 物件「原樣」存檔 ────────────
# 適用：dict/list/自訂類別；不適用：跨語言、長期存檔（用 json 更穩）
# pickle 的優點：可以直接保留 Python 物件結構。
# 缺點：格式是 Python 專用，版本相依性與安全性都要注意。
scores = {
    "alice": [90, 85, 92],
    "bob":   [70, 75, 80],
    "carol": [88, 91, 95],
}

# 注意：pickle 是 bytes → 一定要 'wb'/'rb'
# dump()：把 Python 物件序列化並寫入檔案。
# load()：從檔案讀出 bytes，再還原成 Python 物件。
with open("scores.pkl", "wb") as f:
    pickle.dump(scores, f)

with open("scores.pkl", "rb") as f:
    loaded = pickle.load(f)

# 以下幾行是驗證：
# - 型別是否還是 dict
# - 內容是否與原本相同
# - 是否能正常做後續運算
print("讀回的物件:", loaded)
print("型別一致?", type(loaded) is dict)         # True
print("內容相等?", loaded == scores)              # True
print("alice 平均:", sum(loaded["alice"]) / 3)   # 89.0

# ⚠️ 安全提醒：pickle.load 會執行內嵌指令，
# 絕對不要對「來路不明」的 .pkl 檔做 load。
# 原因是 pickle 不是單純資料格式，它可能包含可執行的反序列化指令。
# 所以只應對你完全信任的來源使用。

# ── 課堂延伸挑戰 ───────────────────────────────────────
# 1) 把 scores 存成 gzip 壓縮後的 pickle：gzip.open('scores.pkl.gz','wb')
# 2) 用 TemporaryDirectory 跑完整流程（寫→讀→比對），不在專案留任何檔
# 3) 試著 pickle 一個 lambda，觀察錯誤訊息（pickle 不能存 lambda）
