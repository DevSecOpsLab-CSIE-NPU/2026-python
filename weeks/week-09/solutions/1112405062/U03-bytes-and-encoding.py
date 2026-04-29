# U03. 文字 vs 位元組、編碼觀念（5.1 encoding / 5.4）
# Bloom: Understand — 能解釋什麼時候用 'rb'、為什麼要指定 encoding
# 本範例介紹 Python 中文字（str）與位元組（bytes）的區別，以及編碼的概念

from pathlib import Path

# ── 5.4 二進位讀寫：圖片、zip、任何非文字 ───────────────
#  二進位模式用於處理圖片、壓縮檔案等非文字資料
#  先建立一個「假 PNG」檔案：只寫入前 8 bytes 的魔數（magic number）
magic = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])
Path("fake.png").write_bytes(magic)

#  以二進位模式讀取檔案（'rb' = read binary）
with open("fake.png", "rb") as f:
    head = f.read(8)  # 讀取前 8 bytes
print(head)           # b'\x89PNG\r\n\x1a\n'
print(head == magic)  # True（確認讀取的資料與原本相同）

#  bytes 物件可以逐位元組迭代（拿到 int 型別，不是 str）
for b in head[:4]:
    print(b, hex(b))
# ── 文字 vs 位元組的型別差 ─────────────────────────────
#  str（文字）和 bytes（位元組）是兩種不同的型別
#  encode：將 str 轉換為 bytes（文字編碼）
s = "你好"
b = s.encode("utf-8")   # str → bytes
print(s, type(s))       # <class 'str'>
print(b, type(b))       # <class 'bytes'>
#  decode：將 bytes 轉換為 str（位元組解碼）
print(b.decode("utf-8"))  # bytes → str

# ── 5.1 encoding 參數：寫錯會爛掉 ──────────────────────
#  讀寫文字檔時，務必指定正確的 encoding，否則會造成編碼錯誤
Path("zh.txt").write_text("中文測試\n", encoding="utf-8")

#  正常讀取：用與寫入相同的 UTF-8 編碼
print(Path("zh.txt").read_text(encoding="utf-8"))

#  故意讀錯：用 Big5 解碼 UTF-8 的檔案 → UnicodeDecodeError
try:
    print(Path("zh.txt").read_text(encoding="big5"))
except UnicodeDecodeError as e:
    print("解碼錯誤:", e)

# 小結：
# - 文字檔 → 使用 'rt'/'wt' 模式，一律明示 encoding='utf-8'
# - 非文字檔（png/zip/pickle）→ 使用 'rb'/'wb' 模式，不需要 encoding 參數