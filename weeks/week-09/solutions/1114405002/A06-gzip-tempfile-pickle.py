# A06. 壓縮檔、臨時資料夾、物件序列化（5.7 / 5.19 / 5.21）
# ============================================================================
# Bloom: Apply — 能把標準庫工具組合起來解一個小任務
# 本檔介紹三個實務中常用的工具：
# 1. gzip：壓縮檔案，節省磁碟空間
# 2. tempfile：建立臨時檔/資料夾，用完自動刪除
# 3. pickle：序列化 Python 物件，快速存/讀複雜資料結構
# ============================================================================

import gzip
import pickle
import tempfile
from pathlib import Path

# ── 5.7 讀寫壓縮檔：gzip.open 幾乎和 open 一樣 ─────────
# gzip 是無損壓縮格式，特別適合文字檔（通常能達 50-90% 壓縮率）
# gzip.open() 的用法與 open() 完全相同，但自動壓縮/解壓

# 寫壓縮檔：.gz（文字模式要記得 encoding）
with gzip.open("notes.txt.gz", "wt", encoding="utf-8") as f:  # "wt" = write text
    f.write("第一行筆記\n")  # 自動壓縮存儲
    f.write("第二行筆記\n")

# 讀回：直接逐行迭代（自動解壓）
with gzip.open("notes.txt.gz", "rt", encoding="utf-8") as f:  # "rt" = read text
    for line in f:  # 就像讀普通文字檔一樣
        print("gz:", line.rstrip())  # rstrip() 移除行尾換行符

# 也能用 'wb'/'rb' 處理二進位資料（如圖片、PDF）
with gzip.open("blob.bin.gz", "wb") as f:  # "wb" = write binary
    f.write(b"\x00\x01\x02\x03")  # 寫入二進位資料

# 檢查壓縮效果：原始 4 bytes 被壓縮成多少？
print("blob size:", Path("blob.bin.gz").stat().st_size, "bytes")

# ── 5.19 臨時檔案與資料夾：離開 with 自動清理 ──────────
# tempfile 解決的問題：
#   - 避免在專案目錄亂留暫用檔案
#   - 隱私保護：檔案存放在系統預設暫存位置
#   - 自動清理：with 結束後自動刪除，無需手動
# 應用場景：單元測試、連線暫存、臨時計算結果

# 建立臨時資料夾（自動清理）
with tempfile.TemporaryDirectory() as tmp:  # with 結束後自動刪除整個目錄
    tmp = Path(tmp)  # 轉換成 Path 物件便於操作
    print("暫存資料夾:", tmp)

    # 在裡面寫幾個檔
    (tmp / "a.txt").write_text("hello\n", encoding="utf-8")  # 在暫存目錄建檔
    (tmp / "b.txt").write_text("world\n", encoding="utf-8")

    # 列出內容
    for p in tmp.iterdir():  # 列舉目錄內所有項目
        print("  ", p.name, "→", p.read_text(encoding="utf-8").rstrip())

# 離開 with 後，tmp 已自動刪除
print("離開後還存在嗎？", tmp.exists())  # False（已自動清理）

# 單一臨時檔：NamedTemporaryFile
# 優點：得到檔案路徑，能讀/寫多次
with tempfile.NamedTemporaryFile("wt", delete=False, suffix=".log",
                                 encoding="utf-8") as f:  # delete=False 預設要手動刪
    f.write("暫存 log\n")
    log_path = f.name  # 取得檔案路徑
print("暫存檔位置:", log_path)
Path(log_path).unlink()  # 用完自己刪（unlink = delete）

# ── 5.21 pickle：把 Python 物件「原樣」存檔 ────────────
# pickle 的用途：
#   - 序列化：將複雜 Python 物件轉成二進位格式存檔
#   - 反序列化：讀回時完全還原原物件（包括型別）
# 
# 適用場景：機器學習模型、快取複雜資料結構、遊戲存檔
# 不適用場景：
#   - 跨語言使用（其他語言讀不了 pickle 格式）
#   - 長期存檔（格式可能隨 Python 版本變化）→ 改用 json
#   - 安全考量（pickle 會執行內嵌代碼，來路不明檔案很危險）

scores = {
    "alice": [90, 85, 92],  # 用字典嵌套列表的複雜結構
    "bob":   [70, 75, 80],
    "carol": [88, 91, 95],
}

# 注意：pickle 是 bytes → 一定要 'wb'/'rb'（不是 'wt'）
with open("scores.pkl", "wb") as f:  # "wb" = write binary
    pickle.dump(scores, f)  # 序列化物件並寫入

# 讀回並驗證
with open("scores.pkl", "rb") as f:  # "rb" = read binary
    loaded = pickle.load(f)  # 反序列化：還原原物件

print("讀回的物件:", loaded)
print("型別一致?", type(loaded) is dict)         # True（完全還原為 dict）
print("內容相等?", loaded == scores)              # True（內容完全相同）
print("alice 平均:", sum(loaded["alice"]) / 3)   # 89.0（可直接使用）

# ⚠️ 安全提醒：pickle.load 會執行內嵌指令
# 絕對不要對「來路不明」的 .pkl 檔做 load（會被植入惡意代碼）

# ── 課堂延伸挑戰 ───────────────────────────────────────
# 進階練習題，整合以上三個工具：
#
# 1) 把 scores 存成 gzip 壓縮後的 pickle：
#    scores_path = "scores.pkl.gz"
#    with gzip.open(scores_path, 'wb') as f:
#        pickle.dump(scores, f)
#    # 好處：節省磁碟空間 + 保持 Python 物件格式
#
# 2) 用 TemporaryDirectory 跑完整流程（寫→讀→比對），不在專案留任何檔：
#    with tempfile.TemporaryDirectory() as tmp:
#        tmp_path = Path(tmp) / "scores.pkl"
#        # 在此進行寫/讀/驗證
#    # 所有檔案自動清理
#
# 3) 試著 pickle 一個 lambda，觀察錯誤訊息（pickle 不能存 lambda）：
#    try:
#        pickle.dumps(lambda x: x * 2)
#    除 AttributeError（lambda 無法序列化）
