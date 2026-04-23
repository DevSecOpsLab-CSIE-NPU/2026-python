# U03. 文字 vs 位元組、編碼觀念（5.1 encoding / 5.4）
# Bloom: Understand — 能解釋什麼時候用 'rb'、為什麼要指定 encoding

from pathlib import Path

# ============================================================================
# 區塊 1：二進位讀寫（bytes）
# ----------------------------------------------------------------------------
# 這段示範「非文字檔」的基本處理方式。
# 重點：
# 1. 圖片、壓縮檔、音訊等資料都應以 bytes 讀寫，不使用文字編碼。
# 2. 寫入模式用 'wb'，讀取模式用 'rb'。
# 3. 這裡用 PNG 檔頭 magic number 做最小示範，驗證 bytes 是否正確寫入。
# ============================================================================
# ── 5.4 二進位讀寫：圖片、zip、任何非文字 ───────────────
# 先造一個「假 PNG」：只寫前 8 bytes 的 magic number
magic = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])
# write_bytes() 會直接以二進位方式寫入完整 bytes 內容。
Path("fake.png").write_bytes(magic)

# 讀回前 8 bytes，對照 PNG 檔頭
# 以 rb（read binary）讀取，f.read(8) 回傳 bytes 型別。
with open("fake.png", "rb") as f:
    head = f.read(8)
print(head)           # b'\x89PNG\r\n\x1a\n'
# 比對讀回內容是否等於原始 magic number，True 代表二進位內容一致。
print(head == magic)  # True

# bytes 可逐位元組迭代（拿到 int，不是 str）
# 每次迭代得到 0~255 的整數，可用 hex() 看十六進位表示法。
for b in head[:4]:
    print(b, hex(b))

# ============================================================================
# 區塊 2：文字（str）與位元組（bytes）的型別差異
# ----------------------------------------------------------------------------
# 這段示範 Python 文字與位元組的雙向轉換：
# 1. encode(): str -> bytes（把文字依指定編碼轉成位元組序列）
# 2. decode(): bytes -> str（把位元組依同一編碼還原回文字）
# 3. encode/decode 的編碼名稱必須相符，否則可能失敗或出現亂碼。
# ============================================================================
# ── 文字 vs 位元組的型別差 ─────────────────────────────
s = "你好"
# UTF-8 是常見且建議預設的編碼格式。
b = s.encode("utf-8")   # str → bytes
print(s, type(s))       # <class 'str'>
print(b, type(b))       # <class 'bytes'>
print(b.decode("utf-8"))  # bytes → str

# ============================================================================
# 區塊 3：encoding 參數的重要性
# ----------------------------------------------------------------------------
# 這段示範為什麼讀寫文字檔時要明確指定 encoding：
# 1. 寫入時若用 utf-8，就應該讀取時也用 utf-8。
# 2. 若讀取時使用錯誤編碼（例如拿 big5 解 utf-8），會觸發 UnicodeDecodeError。
# 3. 在跨平台開發中，明示 encoding 可避免系統預設值造成的不一致問題。
# ============================================================================
# ── 5.1 encoding 參數：寫錯會爛掉 ──────────────────────
# 先建立一個 UTF-8 編碼的中文文字檔。
Path("zh.txt").write_text("中文測試\n", encoding="utf-8")

# 正常：用 utf-8 讀 utf-8 寫的檔
print(Path("zh.txt").read_text(encoding="utf-8"))

# 故意弄錯：用 big5 解 utf-8 → UnicodeDecodeError
try:
    print(Path("zh.txt").read_text(encoding="big5"))
except UnicodeDecodeError as e:
    # 捕捉解碼例外，觀察錯誤訊息內容。
    print("解碼錯誤:", e)

# 小結：
# - 文字檔 → 'rt'/'wt'，一律明示 encoding='utf-8'
# - 非文字（png/zip/pickle）→ 'rb'/'wb'，不談 encoding
