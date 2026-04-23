# U03. 文字 vs 位元組、編碼觀念（5.1 encoding / 5.4）
# Bloom: Understand — 能解釋什麼時候用 'rb'、為什麼要指定 encoding

from pathlib import Path

# ── 5.4 二進位讀寫：圖片、zip、任何非文字 ───────────────
# 「二進位模式」適用於所有非純文字資料：圖片、音訊、壓縮檔、序列化資料等。
# 這些資料不是人類可直接閱讀的字元序列，因此要用 bytes 處理。
#
# 先造一個「假 PNG」：只寫前 8 bytes 的檔頭（magic number）。
# PNG 檔案規範的前 8 位元組固定為：89 50 4E 47 0D 0A 1A 0A
# 若檔案以這串 bytes 開頭，工具通常會辨識成 PNG 格式。
magic = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])
# write_bytes() 會直接把 bytes 寫入檔案，等價於 open(..., 'wb') + write(...)
Path("fake.png").write_bytes(magic)

# 讀回前 8 bytes，對照 PNG 檔頭
# 以 'rb'（read binary）讀檔時，read() 回傳型別是 bytes。
with open("fake.png", "rb") as f:
    head = f.read(8)
print(head)           # b'\x89PNG\r\n\x1a\n'
print(head == magic)  # True

# bytes 可逐位元組迭代（拿到 int，不是 str）
# 每次迭代得到的是 0~255 的整數，可再用 hex() 轉十六進位觀察原始值。
for b in head[:4]:
    print(b, hex(b))

# ── 文字 vs 位元組的型別差 ─────────────────────────────
s = "你好"
# encode()：把 Python 字串（Unicode）依指定編碼規則轉成 bytes
# UTF-8 是最常見、跨平台相容性最高的文字編碼。
b = s.encode("utf-8")   # str → bytes
print(s, type(s))       # <class 'str'>
print(b, type(b))       # <class 'bytes'>
# decode()：把 bytes 依同一套編碼規則還原成字串
# 重點：編碼與解碼必須配對，否則容易出現亂碼或解碼錯誤。
print(b.decode("utf-8"))  # bytes → str

# ── 5.1 encoding 參數：寫錯會爛掉 ──────────────────────
# write_text(..., encoding='utf-8') 會以 UTF-8 寫入文字，
# 這是課程中最推薦的預設做法。
Path("zh.txt").write_text("中文測試\n", encoding="utf-8")

# 正常：用 utf-8 讀 utf-8 寫的檔
print(Path("zh.txt").read_text(encoding="utf-8"))

# 故意弄錯：用 big5 解 utf-8 → UnicodeDecodeError
# 當「實際位元組內容」與「你宣告的 encoding」不一致時，
# Python 無法正確把 bytes 轉回字串，就會拋出 UnicodeDecodeError。
try:
    print(Path("zh.txt").read_text(encoding="big5"))
except UnicodeDecodeError as e:
    # 教學示範：攔截例外並印出細節，協助定位編碼不一致問題。
    print("解碼錯誤:", e)

# 小結：
# - 文字檔 → 'rt'/'wt'，一律明示 encoding='utf-8'
# - 非文字（png/zip/pickle）→ 'rb'/'wb'，不談 encoding
