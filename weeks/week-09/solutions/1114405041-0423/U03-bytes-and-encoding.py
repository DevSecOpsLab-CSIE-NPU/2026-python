# U03. 文字 vs 位元組、編碼觀念（5.1 encoding / 5.4）
# Bloom: Understand — 能解釋什麼時候用 'rb'、為什麼要指定 encoding
#
# ── 核心觀念 ──────────────────────────────────────────
# Python 把資料分成兩種型別：
#   str   → 純文字，Unicode 字元序列，人看得懂
#   bytes → 原始位元組序列，0~255 的整數集合，機器格式
#
# 開檔模式對應：
#   'rt' / 'wt' → 文字模式，Python 幫你做 encode/decode
#   'rb' / 'wb' → 二進位模式，原封不動讀寫位元組
#
# encoding 參數：
#   文字模式下「一定要指定」，否則跨平台會用不同預設值
#   常見：utf-8（最通用）、big5（舊版 Windows 中文）、cp950

from pathlib import Path

# ── 5.4 二進位讀寫：圖片、zip、任何非文字 ───────────────
# PNG、JPEG、zip 這類「非文字」格式不能用文字模式開，
# 否則 Python 會嘗試把位元組解讀成字元 → 通常直接 UnicodeDecodeError

# 先造一個「假 PNG」：只寫前 8 bytes 的 magic number
# PNG 格式規定：所有 PNG 檔案的最前面 8 bytes 固定是 89 50 4E 47 0D 0A 1A 0A
# 其中 0x50 0x4E 0x47 是 ASCII 的 'P' 'N' 'G'
magic = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])
Path("fake.png").write_bytes(magic)  # write_bytes()：二進位寫入，等同 'wb' 模式

# 讀回前 8 bytes，對照 PNG 檔頭
# 'rb' = read binary：逐 byte 讀取，不做任何字元轉換
with open("fake.png", "rb") as f:
    head = f.read(8)   # 讀取 8 個 bytes，回傳 bytes 物件
print(head)           # b'\x89PNG\r\n\x1a\n'（b'' 前綴代表 bytes 型別）
print(head == magic)  # True，bytes 支援 == 比對

# bytes 可逐位元組迭代
# 注意：迭代 bytes 拿到的是「整數 int」，不是字元 str！
# head[:4] 是切片，取前 4 個 bytes
for b in head[:4]:
    print(b, hex(b))   # 例如：137 0x89 / 80 0x50 / 78 0x4e / 71 0x47

# ── 文字 vs 位元組的型別差 ─────────────────────────────
# Python 明確區分 str 和 bytes，兩者不能直接混用
# 轉換流程：str --encode()--> bytes --decode()--> str
#
# UTF-8 中，一個中文字佔 3 個 bytes（"你" = b'\xe4\xbd\xa0'）
s = "你好"
b = s.encode("utf-8")   # str.encode(encoding) → bytes，相當於「打包」
print(s, type(s))       # 你好 <class 'str'>   — 人類看得懂的字串
print(b, type(b))       # b'\xe4\xbd\xa0\xe5\xa5\xbd' <class 'bytes'>  — 電腦儲存的位元組
print(b.decode("utf-8"))  # bytes.decode(encoding) → str，相當於「拆包」，印回 你好

# ── 5.1 encoding 參數：寫錯會爛掉 ──────────────────────
# write_text() 是 pathlib 的捷徑，等同 open(path,'wt',encoding=...) + f.write()
# 一定要明示 encoding='utf-8'，否則 Windows 預設 cp950 (big5)，跨機器會亂碼！
Path("zh.txt").write_text("中文測試\n", encoding="utf-8")

# 正常：用「寫時的 encoding」讀回就沒問題
print(Path("zh.txt").read_text(encoding="utf-8"))   # 印出：中文測試

# 故意用錯 encoding 示範錯誤：utf-8 的「中」是 0xE4 B8 AD
# big5 沒有這個 byte 序列的對應，所以會拋出 UnicodeDecodeError
try:
    print(Path("zh.txt").read_text(encoding="big5"))
except UnicodeDecodeError as e:
    print("解碼錯誤:", e)   # 說明哪個 byte 出問題

# ── 小結：如何選模式 ──────────────────────────────────
# - 文字檔（.txt/.csv/.json/.py 等）→ 用 'rt'/'wt' + encoding='utf-8'
# - 非文字（.png/.zip/.pdf/.pkl）  → 用 'rb'/'wb'，完全不指定 encoding
# 搞混兩者就會出現亂碼或 UnicodeDecodeError！
