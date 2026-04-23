# U03. 文字 vs 位元組、編碼觀念（5.1 encoding / 5.4）
# Bloom: Understand — 能解釋什麼時候用 'rb'、為什麼要指定 encoding

# Pathlib 提供更直覺的檔案操作介面，例如 write_bytes / write_text。
# 這份範例重點在區分：
# - str：文字字串，適合人類閱讀
# - bytes：原始位元資料，適合檔案、網路、圖片、壓縮檔等
from pathlib import Path

# ── 5.4 二進位讀寫：圖片、zip、任何非文字 ───────────────
# 先造一個「假 PNG」：只寫前 8 bytes 的 magic number。
# PNG 檔案前 8 bytes 是固定簽章，用來辨識這是不是 PNG。
# 這裡只是教學示範，不是真正完整的圖片檔。
# bytes([...]) 會把整數清單轉成 bytes 物件。
magic = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])
# write_bytes() 直接寫入原始位元，不需要也不應該指定 encoding。
# 因為這不是文字資料，而是純 bytes。
Path("fake.png").write_bytes(magic)

# 讀回前 8 bytes，對照 PNG 檔頭
with open("fake.png", "rb") as f:
    # rb = read binary。
    # 二進位模式下 read() 回傳的是 bytes，不是 str。
    # 這很重要，因為圖片、zip、pickle 等資料都不能用文字模式硬讀。
    head = f.read(8)
print(head)           # b'\x89PNG\r\n\x1a\n'
# 比對讀回來的 bytes 是否與原始 magic number 一致。
# 這是檢查檔頭是否正確的一種基本方式。
print(head == magic)  # True

# bytes 可逐位元組迭代（拿到 int，不是 str）。
# 注意：for b in head 時，b 不是 '字元'，而是 0~255 的整數。
# 所以常會搭配 hex() 來看它的十六進位表示。
for b in head[:4]:
    print(b, hex(b))

# ── 文字 vs 位元組的型別差 ─────────────────────────────
# 文字字串（str）：是「已經解碼完成」的人類可讀文字。
# bytes：是「尚未解碼」或「已編碼後」的原始資料。
# 兩者不能混用，很多 TypeError / UnicodeError 都來自這裡。
s = "你好"
b = s.encode("utf-8")   # str → bytes
# encode(): 把文字轉成位元組，過程中要指定編碼規則。
# utf-8 是最常見、最安全的選擇之一。
print(s, type(s))       # <class 'str'>
print(b, type(b))       # <class 'bytes'>
# decode(): 把 bytes 解回文字，必須使用和編碼時一致的編碼。
# 若編碼/解碼規則不同，就可能出現亂碼或例外。
print(b.decode("utf-8"))  # bytes → str

# ── 5.1 encoding 參數：寫錯會爛掉 ──────────────────────
# write_text() 會把 str 寫成文字檔。
# 這裡明確指定 utf-8，避免不同系統的預設編碼造成問題。
Path("zh.txt").write_text("中文測試\n", encoding="utf-8")

# 正常：用 utf-8 讀 utf-8 寫的檔
# 讀取時也要用相同編碼，否則解碼出來的內容可能錯誤。
print(Path("zh.txt").read_text(encoding="utf-8"))

# 故意弄錯：用 big5 解 utf-8 → UnicodeDecodeError
try:
    # 這裡刻意示範錯誤情境：檔案實際是 utf-8，但我們硬用 big5 解碼。
    # 因為兩種編碼的位元對應不同，所以 Python 無法正確還原文字，
    # 最終會丟出 UnicodeDecodeError。
    print(Path("zh.txt").read_text(encoding="big5"))
except UnicodeDecodeError as e:
    # 實務上可用 try/except 捕捉解碼失敗，避免程式直接中斷。
    print("解碼錯誤:", e)

# 小結：
# - 文字檔 → 'rt'/'wt'，一律明示 encoding='utf-8'
# - 非文字（png/zip/pickle）→ 'rb'/'wb'，不談 encoding
# 核心觀念：
# - 只要資料是「人類文字」，就要考慮編碼/解碼。
# - 只要資料是「原始位元」，就應該用二進位模式，不要套用文字編碼。
