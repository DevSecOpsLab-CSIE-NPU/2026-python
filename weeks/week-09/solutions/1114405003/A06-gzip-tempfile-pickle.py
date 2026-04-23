# A06. 壓縮檔、臨時資料夾、物件序列化（5.7 / 5.19 / 5.21）
# Bloom: Apply — 能把標準庫工具組合起來解一個小任務

import gzip
import pickle
import tempfile
from pathlib import Path

# ── 5.7 讀寫壓縮檔：gzip.open 幾乎和 open 一樣 ─────────
# gzip.open 的用法與一般 open 很接近：
# - 文字模式：'wt' / 'rt'，需要指定 encoding（例如 utf-8）
# - 二進位模式：'wb' / 'rb'，處理 bytes，不談 encoding
# 這讓你可在幾乎不改寫邏輯下，直接把文字或二進位資料改成壓縮儲存。

# 寫入 .gz 文字檔。
# 這裡會建立 notes.txt.gz，內容會先以 UTF-8 編碼，再經 gzip 壓縮。
with gzip.open("notes.txt.gz", "wt", encoding="utf-8") as f:
    f.write("第一行筆記\n")
    f.write("第二行筆記\n")

# 讀回壓縮文字檔：
# gzip 會在讀取時自動解壓，程式看起來就像在讀一般文字檔。
with gzip.open("notes.txt.gz", "rt", encoding="utf-8") as f:
    for line in f:
        # line 通常自帶換行符，rstrip() 可避免 print 產生多餘空行。
        print("gz:", line.rstrip())

# gzip 也可處理純二進位資料（例如封包片段、機器資料）。
with gzip.open("blob.bin.gz", "wb") as f:
    f.write(b"\x00\x01\x02\x03")

# 查看壓縮後檔案大小（單位 bytes）。
# 注意：很小的資料不一定會壓得更小，因為壓縮格式本身也有標頭成本。
print("blob size:", Path("blob.bin.gz").stat().st_size, "bytes")

# ── 5.19 臨時檔案與資料夾：離開 with 自動清理 ──────────
# TemporaryDirectory 常見於：
# - 測試流程（不想污染專案目錄）
# - 中繼檔暫存
# - 需要短生命週期工作空間的工具程式
with tempfile.TemporaryDirectory() as tmp:
    # tempfile 回傳的是路徑字串，轉成 Path 便於後續操作。
    tmp = Path(tmp)
    print("暫存資料夾:", tmp)

    # 在暫存目錄建立兩個文字檔。
    (tmp / "a.txt").write_text("hello\n", encoding="utf-8")
    (tmp / "b.txt").write_text("world\n", encoding="utf-8")

    # 掃描暫存目錄內容並讀出檔案內容。
    for p in tmp.iterdir():
        print("  ", p.name, "→", p.read_text(encoding="utf-8").rstrip())

# 離開 with 區塊後，TemporaryDirectory 會自動刪除整個資料夾與其內容。
print("離開後還存在嗎？", tmp.exists())  # False

# 單一臨時檔：NamedTemporaryFile
# delete=False 代表離開 with 後檔案不會自動刪除，
# 適合你還需要在外部流程中使用該檔名的情境。
with tempfile.NamedTemporaryFile("wt", delete=False, suffix=".log",
                                 encoding="utf-8") as f:
    f.write("暫存 log\n")
    log_path = f.name

print("暫存檔位置:", log_path)

# 使用完手動刪除，避免暫存檔殘留。
Path(log_path).unlink()

# ── 5.21 pickle：把 Python 物件「原樣」存檔 ────────────
# pickle 的定位：
# - 優點：可保存 Python 物件結構（例如 dict/list/tuple/部分自訂物件）
# - 限制：不適合跨語言交換（他語言通常讀不懂）
# - 風險：不可信來源的 pickle 可能帶惡意行為（load 時可執行程式碼）
# 若要跨平台、跨語言長期資料交換，通常優先考慮 JSON。
scores = {
    "alice": [90, 85, 92],
    "bob":   [70, 75, 80],
    "carol": [88, 91, 95],
}

# pickle 輸出是 bytes，因此一定要用二進位模式 'wb' / 'rb'。
with open("scores.pkl", "wb") as f:
    pickle.dump(scores, f)

with open("scores.pkl", "rb") as f:
    loaded = pickle.load(f)

# 驗證讀回結果：
# 1) 印出內容
# 2) 確認型別是否為 dict
# 3) 確認內容是否與原始資料相同
print("讀回的物件:", loaded)
print("型別一致?", type(loaded) is dict)         # True
print("內容相等?", loaded == scores)              # True
print("alice 平均:", sum(loaded["alice"]) / 3)   # 89.0

# ⚠️ 安全提醒：
# pickle.load 會在反序列化過程中執行特定指令，
# 絕對不要載入來源不明或未經驗證的 .pkl 檔。

# ── 課堂延伸挑戰 ───────────────────────────────────────
# 1) 把 scores 存成 gzip 壓縮後的 pickle：gzip.open('scores.pkl.gz','wb')
# 2) 用 TemporaryDirectory 跑完整流程（寫→讀→比對），不在專案留任何檔
# 3) 試著 pickle 一個 lambda，觀察錯誤訊息（pickle 不能存 lambda）
