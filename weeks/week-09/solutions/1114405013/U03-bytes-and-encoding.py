# U03. 文字 vs 位元組、編碼觀念（5.1 encoding / 5.4）
# Bloom: Understand — 能解釋什麼時候用 'rb'、為什麼要指定 encoding

from pathlib import Path

# ── 5.4 二進位讀寫：圖片、zip、任何非文字 ───────────────
# 非文字檔（例如影像、壓縮檔、pickle）必須以二進位模式讀寫，
# 因為這類檔案的內容不是可直接解釋成文字的字元序列。
magic = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])
# PNG 檔案的前 8 bytes 是固定的檔頭，也稱為 magic number
Path("fake.png").write_bytes(magic)

# 讀回前 8 bytes，檢查是否與我們寫入的 binary 內容相同
with open("fake.png", "rb") as f:
    head = f.read(8)
print(head)           # b'\x89PNG\r\n\x1a\n'
print(head == magic)  # True

# bytes 物件可逐位元組迭代，每一項是 int，非字串
for b in head[:4]:
    print(b, hex(b))

# ── 文字 vs 位元組的型別差 ─────────────────────────────
# str 代表文字（Unicode 字元），bytes 代表原始位元組資料
s = "你好"
b = s.encode("utf-8")   # 將文字編碼成 UTF-8 bytes
print(s, type(s))         # <class 'str'>
print(b, type(b))         # <class 'bytes'>
print(b.decode("utf-8"))  # 將 bytes 解碼回 str

# bytes 和 str 不是同一種型別，必須用 encode()/decode() 轉換
# 這也是為什麼 open(..., 'rb') 和 open(..., 'rt') 不能混用的原因

# ── 5.1 encoding 參數：寫錯會爛掉 ──────────────────────
# 文字檔需要指定 encoding，才能正確把 Python 字符串轉成檔案內容
Path("zh.txt").write_text("中文測試\n", encoding="utf-8")

# 正常讀回：寫什麼編碼就用相同編碼讀
print(Path("zh.txt").read_text(encoding="utf-8"))

# 如果編碼不一致，就會遇到解碼錯誤
try:
    print(Path("zh.txt").read_text(encoding="big5"))
except UnicodeDecodeError as e:
    print("解碼錯誤:", e)

# 進一步說明：
# - 'rt' / 'wt' 是文字模式，讀寫的是 str，必須指定 encoding
# - 'rb' / 'wb' 是二進位模式，讀寫的是 bytes，不能指定 encoding
# - 若把 bytes 當成 str 讀，或把 str 當成 bytes 寫，會發生 TypeError 或 UnicodeDecodeError

# 小結：
# - 文字檔（例如 .txt / .csv / .py）要用文字模式，並指定 encoding='utf-8'
# - 非文字檔（例如圖片、壓縮檔、視訊）要用二進位模式，不要用 encoding
# - bytes 與 str 之間的轉換，靠 .encode() 和 .decode() 完成
