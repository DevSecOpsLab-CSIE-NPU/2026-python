# U03. 文字 vs 位元組、編碼觀念（5.1 encoding / 5.4）
# ============================================================================
# Bloom: Understand — 能解釋什麼時候用 'rb'、為什麼要指定 encoding
# 重要概念：
#   - str（文字）：Python 3 內部用 Unicode 表示
#   - bytes（位元組）：磁碟/網路上的二進位資料
#   - encoding（編碼）：str 和 bytes 之間的轉換規則
# ============================================================================

from pathlib import Path

# ── 5.4 二進位讀寫：圖片、zip、任何非文字 ───────────────
# 使用 'rb'/'wb' 模式處理二進位檔（如圖片、可執行檔、壓縮檔）
# 不涉及編碼問題，bytes 就是 bytes
# 應用場景：複製檔案、處理圖片元資料、讀取二進位協議

# 先造一個「假 PNG」：只寫前 8 bytes 的 magic number
# PNG 檔案的開頭簽名是固定的位元組序列，用來識別檔案格式
magic = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])  # PNG 的 magic number
Path("fake.png").write_bytes(magic)  # write_bytes = 二進位寫入（簡寫版本）

# 讀回前 8 bytes，對照 PNG 檔頭
with open("fake.png", "rb") as f:  # "rb" = read binary
    head = f.read(8)  # 讀 8 個位元組
print(head)           # b'\x89PNG\r\n\x1a\n'（16進位顯示）
print(head == magic)  # True（內容相等）

# bytes 可逐位元組迭代（拿到 int，不是 str）
for b in head[:4]:
    print(b, hex(b))  # 逐個位元組顯示，hex() 轉 16進位表示

# ── 文字 vs 位元組的型別差 ─────────────────────────────
# 關鍵概念：編碼（encode）和解碼（decode）
#   - encode：str → bytes（存檔時）
#   - decode：bytes → str（讀檔時）

s = "你好"  # Python 字串（內部用 Unicode）
b = s.encode("utf-8")   # 編碼：str → bytes（UTF-8 編碼方式）
print(s, type(s))       # <class 'str'>
print(b, type(b))       # <class 'bytes'>
print(b.decode("utf-8"))  # 解碼：bytes → str（用同樣的 UTF-8 解碼）

# 中文編碼說明：
#   "你好" 在 UTF-8：b'\xe4\xbd\xa0\xe5\xa5\xbd'（6 個位元組）
#   "你好" 在 Big5：b'\xa4\xe5\xb6\xb0'（4 個位元組）
# UTF-8 通用性好，Big5 只用於繁體中文舊系統

# ── 5.1 encoding 參數：寫錯會爛掉 ──────────────────────
# 常見問題：
#   1. 寫檔時不指定 encoding → 平台默認（通常是 utf-8，但不保證）
#   2. 讀檔時用錯 encoding → UnicodeDecodeError（亂碼或崩潰）
# 最安全的做法：永遠明示 encoding='utf-8'

# 寫檔時用 UTF-8
Path("zh.txt").write_text("中文測試\n", encoding="utf-8")

# 正常讀取：用 UTF-8 讀 UTF-8 寫的檔
print(Path("zh.txt").read_text(encoding="utf-8"))  # 正常顯示中文

# 故意弄錯：用 big5 解 utf-8 → 錯誤
try:
    print(Path("zh.txt").read_text(encoding="big5"))  # 用錯編碼
except UnicodeDecodeError as e:
    print("解碼錯誤:", e)  # UnicodeDecodeError: 'big5' codec can't decode...
    # 原因：UTF-8 的位元組序列在 Big5 解釋下無效

# ※ 中文編碼選擇建議：
#   - UTF-8：國際通用，推薦使用（Python 3 預設）
#   - Big5：只用於舊 Windows 繁體系統相容
