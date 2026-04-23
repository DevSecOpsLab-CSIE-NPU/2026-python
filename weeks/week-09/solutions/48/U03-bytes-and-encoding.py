# U03. 文字與位元組、編碼觀念
# 主題：什麼時候用 'rb'/'wb'、str 與 bytes 轉換、encoding 讀寫一致性

from pathlib import Path

# ── 1) 二進位讀寫（對應 5.4） ─────────────────────────
# 二進位模式適合處理非文字資料：圖片、壓縮檔、音訊等
# 這裡建立一個「假 PNG 檔」，只寫入 PNG 檔頭的前 8 bytes（magic number）
magic = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])
Path("fake.png").write_bytes(magic)

# 用 rb 讀回前 8 bytes，確認與原始 magic 一致
with open("fake.png", "rb") as f:
    head = f.read(8)
print(head)           # b'\x89PNG\r\n\x1a\n'
print(head == magic)  # True

# bytes 可逐一迭代，每個元素是 0~255 的 int，不是字元 str
for b in head[:4]:
    print(b, hex(b))

# ── 2) str 與 bytes 的轉換 ────────────────────────────
# Python 文字是 str（Unicode），要儲存/傳輸時通常轉成 bytes
s = "你好"
b = s.encode("utf-8")     # str -> bytes（編碼）
print(s, type(s))         # <class 'str'>
print(b, type(b))         # <class 'bytes'>
print(b.decode("utf-8")) # bytes -> str（解碼）

# ── 3) encoding 一致性（對應 5.1） ───────────────────
# 用 utf-8 寫入中文檔案
Path("zh.txt").write_text("中文測試\n", encoding="utf-8")

# 正確做法：用相同編碼讀取
print(Path("zh.txt").read_text(encoding="utf-8"))

# 錯誤示範：用 big5 讀 utf-8 檔案，通常會噴解碼錯誤
try:
    print(Path("zh.txt").read_text(encoding="big5"))
except UnicodeDecodeError as e:
    print("解碼錯誤:", e)

# 小結：
# 1. 文字檔：使用 'rt'/'wt'，並明確指定 encoding='utf-8'
# 2. 非文字檔：使用 'rb'/'wb'，資料本體是 bytes，不需要 encoding
