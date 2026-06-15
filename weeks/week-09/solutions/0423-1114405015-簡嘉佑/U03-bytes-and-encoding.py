"""
U03. 文字 vs 位元組、編碼觀念（5.1 encoding / 5.4）
Bloom: Understand

本檔說明三件事：
1) 二進位模式（rb/wb）怎麼操作 bytes。
2) str 與 bytes 的 encode/decode 轉換。
3) 編碼讀錯時為什麼會出現 UnicodeDecodeError。
"""

from pathlib import Path

# ── 5.4 二進位讀寫：圖片、zip、任何非文字 ───────────────
# 先造一個「假 PNG」：只寫前 8 bytes 的 magic number
# PNG 標準檔頭固定為 89 50 4E 47 0D 0A 1A 0A
magic = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])
Path("fake.png").write_bytes(magic)

# 讀回前 8 bytes，對照 PNG 檔頭
# "rb" 模式讀到的是 bytes，不會經過文字解碼。
with open("fake.png", "rb") as f:
    head = f.read(8)
print(head)           # b'\x89PNG\r\n\x1a\n'
print(head == magic)  # True

# bytes 可逐位元組迭代（每個元素是 0~255 的 int，不是字串）
for b in head[:4]:
    print(b, hex(b))

# ── 文字 vs 位元組的型別差 ─────────────────────────────
# str 是「文字抽象」，bytes 是「實際位元組序列」。
s = "你好"
b = s.encode("utf-8")   # str -> bytes：依 UTF-8 規則編碼
print(s, type(s))       # <class 'str'>
print(b, type(b))       # <class 'bytes'>
print(b.decode("utf-8"))  # bytes -> str：依 UTF-8 規則解碼

# ── 5.1 encoding 參數：寫錯會爛掉 ──────────────────────
# 先用 UTF-8 寫入中文文字。
Path("zh.txt").write_text("中文測試\n", encoding="utf-8")

# 正常：用 utf-8 讀 utf-8 寫的檔
print(Path("zh.txt").read_text(encoding="utf-8"))

# 故意弄錯：用 big5 解 utf-8，通常會拋 UnicodeDecodeError
try:
    print(Path("zh.txt").read_text(encoding="big5"))
except UnicodeDecodeError as e:
    print("解碼錯誤:", e)

# 小結：
# - 文字檔 → 'rt'/'wt'，一律明示 encoding='utf-8'
# - 非文字（png/zip/pickle）→ 'rb'/'wb'，不談 encoding
