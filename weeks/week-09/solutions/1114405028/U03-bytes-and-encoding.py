# U03-bytes-and-encoding.py
# 完整繁體中文註釋版：示範文字與位元組、編碼、解碼，以及讀寫二進位檔案

from pathlib import Path

# ── 5.4 二進位讀寫：圖片、zip、任何非文字檔案 ───────────────
# 先建立一個簡單的假 PNG 檔案，只寫入 PNG 檔頭 magic number
magic = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])
Path("fake.png").write_bytes(magic)

# 用二進位模式讀取前 8 個位元組，對照是否等於剛剛寫入的 magic number
with open("fake.png", "rb") as f:
    head = f.read(8)
print(head)           # b'\x89PNG\r\n\x1a\n'
print(head == magic)  # True，表示讀取成功

# bytes 可以逐位元組迭代，拿到的元素是 int
for b in head[:4]:
    print(b, hex(b))

# ── 文字與位元組的型別差異 ─────────────────────────────
s = "你好"
b = s.encode("utf-8")   # 將文字字串轉成 utf-8 編碼的 bytes
print(s, type(s))         # str
print(b, type(b))         # bytes
print(b.decode("utf-8")) # 將 bytes 解碼回 str

# ── 5.1 encoding 參數：要寫入文字檔時一定要指定 encoding
Path("zh.txt").write_text("中文測試\n", encoding="utf-8")

# 正常讀取方式：用相同編碼讀取
print(Path("zh.txt").read_text(encoding="utf-8"))

# 故意用錯編碼讀取，會發生 UnicodeDecodeError
try:
    print(Path("zh.txt").read_text(encoding="big5"))
except UnicodeDecodeError as e:
    print("解碼錯誤:", e)

# 小結：
# - 文字檔案應該使用 'rt' / 'wt' 模式，並明確指定 encoding='utf-8'
# - 非文字檔案（如 png、zip、pickle）應該使用 'rb' / 'wb' 模式
# - 文字與位元組不是同一個型別，不能混用
