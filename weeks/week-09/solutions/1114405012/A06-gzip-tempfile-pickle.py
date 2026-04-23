# A06. 壓縮檔、臨時資料夾、物件序列化（5.7 / 5.19 / 5.21）
# Bloom: Apply — 能把標準庫工具組合起來解一個小任務

import gzip
import pickle
import tempfile
from pathlib import Path

# ============================================================================
# 區塊 1：gzip 壓縮檔讀寫
# ----------------------------------------------------------------------------
# 目標：
# 1. 了解 gzip.open() 的使用方式幾乎與 open() 相同。
# 2. 文字資料用 'wt'/'rt'，並明確指定 encoding。
# 3. 二進位資料用 'wb'/'rb'，不涉及文字編碼。
#
# 補充：
# - .gz 是在讀寫時即時壓縮/解壓，程式碼可維持接近一般檔案 I/O 的寫法。
# ============================================================================
# ── 5.7 讀寫壓縮檔：gzip.open 幾乎和 open 一樣 ─────────
# 寫 .gz（文字模式要記得 encoding）
# 以文字模式寫入 gzip 壓縮檔，內容會被壓縮成 notes.txt.gz。
with gzip.open("notes.txt.gz", "wt", encoding="utf-8") as f:
    f.write("第一行筆記\n")
    f.write("第二行筆記\n")

# 讀回：直接逐行迭代
# 以文字模式讀取時，gzip 會自動解壓並回傳 str。
with gzip.open("notes.txt.gz", "rt", encoding="utf-8") as f:
    for line in f:
        print("gz:", line.rstrip())

# 也能用 'wb'/'rb' 處理二進位資料
# 寫入原始 bytes（例如感測器資料、封包片段、二進位快取）。
with gzip.open("blob.bin.gz", "wb") as f:
    f.write(b"\x00\x01\x02\x03")

# 查看壓縮後檔案大小（單位 bytes）。
print("blob size:", Path("blob.bin.gz").stat().st_size, "bytes")

# ============================================================================
# 區塊 2：臨時檔案與臨時資料夾（tempfile）
# ----------------------------------------------------------------------------
# 目標：
# 1. 在不污染專案目錄的情況下執行測試、轉檔或中間處理。
# 2. TemporaryDirectory 離開 with 後自動刪除，適合短生命週期資料。
# 3. NamedTemporaryFile 可取得實體路徑，便於交給只收「檔名」的 API。
# ============================================================================
# ── 5.19 臨時檔案與資料夾：離開 with 自動清理 ──────────
# 場景：想跑個小實驗但不想在專案亂留檔
with tempfile.TemporaryDirectory() as tmp:
    # 將字串路徑包成 Path，方便使用 pathlib API。
    tmp = Path(tmp)
    print("暫存資料夾:", tmp)

    # 在裡面寫幾個檔
    (tmp / "a.txt").write_text("hello\n", encoding="utf-8")
    (tmp / "b.txt").write_text("world\n", encoding="utf-8")

    # 列出內容
    # iterdir() 走訪當層項目；此處示範讀回每個檔案內容。
    for p in tmp.iterdir():
        print("  ", p.name, "→", p.read_text(encoding="utf-8").rstrip())

# 離開 with 後，tmp 已自動刪除
print("離開後還存在嗎？", tmp.exists())  # False

# 單一臨時檔：NamedTemporaryFile
# delete=False 代表離開 with 不自動刪除，方便後續用路徑再操作一次。
with tempfile.NamedTemporaryFile("wt", delete=False, suffix=".log",
                                 encoding="utf-8") as f:
    f.write("暫存 log\n")
    # f.name 是實際建立出的臨時檔完整路徑。
    log_path = f.name
print("暫存檔位置:", log_path)
# 因為 delete=False，這裡手動刪除，避免留下垃圾檔。
Path(log_path).unlink()  # 用完自己刪

# ============================================================================
# 區塊 3：pickle 物件序列化
# ----------------------------------------------------------------------------
# 目標：
# 1. 將 Python 物件（dict/list 等）原樣存成二進位檔，再完整還原。
# 2. 理解 pickle 讀寫必須用二進位模式：'wb' / 'rb'。
# 3. 建立安全觀念：不要 load 不可信來源的 pickle 檔。
#
# 使用時機：
# - 適合 Python 內部短中期快取或中間資料。
# - 若需跨語言或長期相容，通常優先考慮 JSON 等格式。
# ============================================================================
# ── 5.21 pickle：把 Python 物件「原樣」存檔 ────────────
# 適用：dict/list/自訂類別；不適用：跨語言、長期存檔（用 json 更穩）
scores = {
    "alice": [90, 85, 92],
    "bob":   [70, 75, 80],
    "carol": [88, 91, 95],
}

# 注意：pickle 是 bytes → 一定要 'wb'/'rb'
# dump(): 把 Python 物件序列化後寫入檔案。
with open("scores.pkl", "wb") as f:
    pickle.dump(scores, f)

# load(): 從檔案反序列化回 Python 物件。
with open("scores.pkl", "rb") as f:
    loaded = pickle.load(f)

print("讀回的物件:", loaded)
print("型別一致?", type(loaded) is dict)         # True
print("內容相等?", loaded == scores)              # True
# 驗證資料可直接進行後續運算。
print("alice 平均:", sum(loaded["alice"]) / 3)   # 89.0

# ⚠️ 安全提醒：pickle.load 會執行內嵌指令，
# 絕對不要對「來路不明」的 .pkl 檔做 load。

# ============================================================================
# 區塊 4：課堂延伸挑戰
# ----------------------------------------------------------------------------
# 提供可自行練習的延伸方向，目的是把三種工具組合起來實作完整流程。
# ============================================================================
# ── 課堂延伸挑戰 ───────────────────────────────────────
# 1) 把 scores 存成 gzip 壓縮後的 pickle：gzip.open('scores.pkl.gz','wb')
# 2) 用 TemporaryDirectory 跑完整流程（寫→讀→比對），不在專案留任何檔
# 3) 試著 pickle 一個 lambda，觀察錯誤訊息（pickle 不能存 lambda）
