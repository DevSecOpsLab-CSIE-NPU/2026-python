# A06. 壓縮檔、臨時資料夾、物件序列化（5.7 / 5.19 / 5.21）
# Bloom: Apply — 能把標準庫工具組合起來解一個小任務

# gzip：用來讀寫 .gz 壓縮檔（支援文字與二進位模式）
import gzip

# pickle：用來將 Python 物件序列化（serialize）成 bytes，或反序列化（deserialize）
import pickle

# tempfile：建立「暫時檔案 / 暫時資料夾」，用完會自動清除
import tempfile

# Path：用來操作檔案與路徑（現代寫法）
from pathlib import Path

# ── 5.7 讀寫壓縮檔：gzip.open 幾乎和 open 一樣 ─────────

# 寫入 gzip 壓縮檔（文字模式）
# "wt" = write text（寫文字）
# encoding="utf-8"：一定要指定，避免中文亂碼
with gzip.open("notes.txt.gz", "wt", encoding="utf-8") as f:
    f.write("第一行筆記\n")
    f.write("第二行筆記\n")

# 讀取 gzip 壓縮檔（文字模式）
# 可以像一般檔案一樣逐行讀取
with gzip.open("notes.txt.gz", "rt", encoding="utf-8") as f:
    for line in f:
        # rstrip() 去掉行尾換行，避免 print 多印空行
        print("gz:", line.rstrip())

# 也可以用二進位模式寫入壓縮檔
# "wb" = write binary（寫入 bytes）
with gzip.open("blob.bin.gz", "wb") as f:
    # 寫入原始 bytes 資料（不涉及 encoding）
    f.write(b"\x00\x01\x02\x03")

# 查看壓縮後檔案大小（單位：bytes）
print("blob size:", Path("blob.bin.gz").stat().st_size, "bytes")

# ── 5.19 臨時檔案與資料夾：離開 with 自動清理 ──────────

# TemporaryDirectory：建立一個暫時資料夾
# with 結束後會「自動刪除整個資料夾與內容」
with tempfile.TemporaryDirectory() as tmp:
    # 將字串路徑轉成 Path 物件，方便操作
    tmp = Path(tmp)
    print("暫存資料夾:", tmp)

    # 在暫存資料夾中建立檔案並寫入內容
    (tmp / "a.txt").write_text("hello\n", encoding="utf-8")
    (tmp / "b.txt").write_text("world\n", encoding="utf-8")

    # 列出資料夾內所有檔案
    for p in tmp.iterdir():
        # p.name：檔名
        # read_text()：讀取檔案內容
        print("  ", p.name, "→", p.read_text(encoding="utf-8").rstrip())

# 離開 with 區塊後，暫存資料夾會自動被刪除
print("離開後還存在嗎？", tmp.exists())  # False

# NamedTemporaryFile：建立一個「暫時檔案」
# delete=False → 不會自動刪除（需要手動刪）
# suffix=".log" → 設定副檔名
with tempfile.NamedTemporaryFile("wt", delete=False, suffix=".log",
                                 encoding="utf-8") as f:
    f.write("暫存 log\n")
    # f.name：取得暫存檔的實際路徑
    log_path = f.name

# 印出暫存檔位置（實際存在於系統暫存目錄）
print("暫存檔位置:", log_path)

# 用 Path.unlink() 手動刪除檔案
Path(log_path).unlink()

# ── 5.21 pickle：把 Python 物件「原樣」存檔 ────────────

# 建立一個字典（包含 list）
# 這種複雜資料結構很適合用 pickle 存
scores = {
    "alice": [90, 85, 92],
    "bob":   [70, 75, 80],
    "carol": [88, 91, 95],
}

# 注意：pickle 處理的是 bytes，不是文字
# 所以一定要用 "wb"（write binary）
with open("scores.pkl", "wb") as f:
    # dump：將 Python 物件轉成 bytes 並寫入檔案
    pickle.dump(scores, f)

# 讀回 pickle 檔案
# 一樣要用 "rb"（read binary）
with open("scores.pkl", "rb") as f:
    # load：從檔案讀取 bytes，還原成 Python 物件
    loaded = pickle.load(f)

# 印出讀回的資料
print("讀回的物件:", loaded)

# 檢查型別是否一致
print("型別一致?", type(loaded) is dict)         # True

# 檢查內容是否相等
print("內容相等?", loaded == scores)              # True

# 計算 alice 的平均分數
print("alice 平均:", sum(loaded["alice"]) / 3)   # 89.0

# ⚠️ 安全提醒：pickle.load 會執行內嵌指令，
# 如果檔案被惡意修改，可能會執行危險程式碼
# → 絕對不要讀取來源不明的 .pkl 檔案！

# ── 課堂延伸挑戰 ───────────────────────────────────────
# 1) 把 scores 存成 gzip 壓縮後的 pickle：gzip.open('scores.pkl.gz','wb')
# 2) 用 TemporaryDirectory 跑完整流程（寫→讀→比對），不在專案留任何檔
# 3) 試著 pickle 一個 lambda，觀察錯誤訊息（pickle 不能存 lambda）