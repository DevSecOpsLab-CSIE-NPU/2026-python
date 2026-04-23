# A06. gzip / tempfile / pickle 綜合應用
# 主題：壓縮讀寫、臨時資源管理、Python 物件序列化與安全注意事項

import gzip
import pickle
import tempfile
from pathlib import Path

# ── 1) gzip：壓縮檔讀寫（對應 5.7） ───────────────────
# gzip.open 的操作方式和 open 幾乎相同。
# 文字模式要記得給 encoding；二進位模式則使用 bytes。

# 寫入壓縮文字檔（wt = write text）
with gzip.open("notes.txt.gz", "wt", encoding="utf-8") as f:
    f.write("第一行筆記\n")
    f.write("第二行筆記\n")

# 讀回壓縮文字檔（rt = read text）
with gzip.open("notes.txt.gz", "rt", encoding="utf-8") as f:
    for line in f:
        print("gz:", line.rstrip())

# 也可用二進位模式處理 bytes（wb/rb）
with gzip.open("blob.bin.gz", "wb") as f:
    f.write(b"\x00\x01\x02\x03")

print("blob size:", Path("blob.bin.gz").stat().st_size, "bytes")

# ── 2) tempfile：臨時資料夾與檔案（對應 5.19） ─────────
# TemporaryDirectory 在離開 with 區塊後會自動刪除。
# 適合做測試、中間產物處理，避免專案目錄殘留垃圾檔案。
with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)
    print("暫存資料夾:", tmp)

    (tmp / "a.txt").write_text("hello\n", encoding="utf-8")
    (tmp / "b.txt").write_text("world\n", encoding="utf-8")

    for p in tmp.iterdir():
        print("  ", p.name, "→", p.read_text(encoding="utf-8").rstrip())

# 區塊結束後暫存資料夾應該不存在
print("離開後還存在嗎？", tmp.exists())  # 預期 False

# NamedTemporaryFile：單一暫存檔
# delete=False 表示離開 with 後先保留，稍後可手動刪除
with tempfile.NamedTemporaryFile("wt", delete=False, suffix=".log", encoding="utf-8") as f:
    f.write("暫存 log\n")
    log_path = f.name

print("暫存檔位置:", log_path)
Path(log_path).unlink()  # 用完刪除，避免殘留

# ── 3) pickle：Python 物件序列化（對應 5.21） ───────────
# pickle 適合快速存取 Python 原生物件（dict/list/自訂類別）。
# 但不適合跨語言與長期交換格式；跨系統交換通常建議 json。
scores = {
    "alice": [90, 85, 92],
    "bob": [70, 75, 80],
    "carol": [88, 91, 95],
}

# pickle 是二進位資料，必須用 wb/rb
with open("scores.pkl", "wb") as f:
    pickle.dump(scores, f)

with open("scores.pkl", "rb") as f:
    loaded = pickle.load(f)

print("讀回的物件:", loaded)
print("型別一致?", type(loaded) is dict)        # True
print("內容相等?", loaded == scores)             # True
print("alice 平均:", sum(loaded["alice"]) / 3)  # 89.0

# 安全提醒：
# pickle.load 可能執行惡意內容，禁止載入來源不明的 .pkl。

# ── 課堂延伸挑戰 ───────────────────────────────────────
# 1) 把 scores 存成 gzip 壓縮 pickle：gzip.open('scores.pkl.gz', 'wb')。
# 2) 用 TemporaryDirectory 包住完整流程（寫 -> 讀 -> 比對），不留檔案。
# 3) 試著 pickle 一個 lambda，觀察例外訊息。
