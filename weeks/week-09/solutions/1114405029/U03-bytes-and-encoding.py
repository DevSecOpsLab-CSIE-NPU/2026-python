# U03. 文字 vs 位元組、編碼觀念（5.1 encoding / 5.4）
# Bloom: Understand — 能解釋什麼時候用 'rb'、為什麼要指定 encoding

# 匯入 Path（用於簡潔地進行檔案讀寫）
from pathlib import Path

# ── 5.4 二進位讀寫：圖片、zip、任何非文字 ───────────────

# PNG 檔案開頭有固定的「魔術數字（magic number）」
# 這 8 個 bytes 用來辨識檔案格式是否為 PNG
# 這裡手動建立這 8 個位元組（bytes）
magic = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])

# write_bytes()：直接寫入「位元組資料」到檔案（binary write）
# 不涉及 encoding（因為不是文字）
Path("fake.png").write_bytes(magic)

# 以 "rb"（read binary）模式開啟檔案
# → 適用於所有「非文字資料」（圖片、影片、壓縮檔等）
with open("fake.png", "rb") as f:
    # 讀取前 8 bytes
    head = f.read(8)

# 印出讀到的 bytes（前面會有 b'' 表示是 bytes 型別）
print(head)           # b'\x89PNG\r\n\x1a\n'

# 比對讀取結果是否與原本寫入的 magic 一致
print(head == magic)  # True

# bytes 可以像序列一樣逐一取值
# 但每個元素是「整數」（0~255），不是字元
for b in head[:4]:
    print(b, hex(b))  # 同時印出十進位與十六進位

# ── 文字 vs 位元組的型別差 ─────────────────────────────

# s 是 Python 的字串（str），屬於「文字」
s = "你好"

# encode("utf-8")：將文字轉換為位元組（bytes）
# → 編碼（encoding）
b = s.encode("utf-8")   # str → bytes

# 印出內容與型別
print(s, type(s))       # <class 'str'>
print(b, type(b))       # <class 'bytes'>

# decode("utf-8")：將位元組還原為文字
# → 解碼（decoding）
print(b.decode("utf-8"))  # bytes → str

# ── 5.1 encoding 參數：寫錯會爛掉 ──────────────────────

# write_text()：寫入「文字檔」
# encoding="utf-8"：指定編碼方式（非常重要，避免跨平台亂碼）
Path("zh.txt").write_text("中文測試\n", encoding="utf-8")

# 正常情況：用相同的編碼（utf-8）讀取
# → 可以正確還原文字
print(Path("zh.txt").read_text(encoding="utf-8"))

# 故意錯誤示範：
# 用 big5 解讀 utf-8 編碼的檔案
# → 會產生 UnicodeDecodeError（解碼失敗）
try:
    print(Path("zh.txt").read_text(encoding="big5"))
except UnicodeDecodeError as e:
    # 捕捉錯誤並顯示
    print("解碼錯誤:", e)

# 小結：
# - 文字檔 → 使用 'rt'（讀）/ 'wt'（寫），一定要指定 encoding='utf-8'
# - 非文字（png/zip/pickle）→ 使用 'rb'（讀）/ 'wb'（寫），完全不涉及 encoding