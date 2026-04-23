"""U03. 文字 vs 位元組、編碼觀念（5.1 encoding / 5.4）

Bloom: Understand
學習目標：能清楚區分 str 與 bytes，並理解何時使用文字模式或二進位模式。

本檔想回答三個問題：
1) 為什麼圖片、zip 這類檔案要用 'rb'/'wb'？
2) str 與 bytes 如何互轉？
3) 為什麼文字讀寫要明確指定 encoding？

核心原則：
- 文字資料（str）需要編碼/解碼，常用 UTF-8。
- 二進位資料（bytes）是原始位元組，不適合用文字模式處理。
- 文字模式遇到錯誤編碼會觸發 UnicodeDecodeError。

閱讀建議：
- 先看「二進位讀寫」段落，建立 bytes 的直覺。
- 再看「encode/decode」段落，理解 str 與 bytes 的轉換方向。
- 最後看「故意解碼失敗」段落，學會辨識常見錯誤。
"""

from pathlib import Path

# ── 5.4 二進位讀寫：圖片、zip、任何非文字 ───────────────
# 先造一個「假 PNG」：只寫前 8 bytes 的 magic number。
# magic number 是很多檔案格式都會有的「檔頭簽名」，
# 可以讓程式在不看副檔名的情況下，也能辨識檔案類型。
# 這組數值是 PNG 標準檔頭：89 50 4E 47 0D 0A 1A 0A
magic = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])

# write_bytes() 是 pathlib 針對二進位資料的快捷寫法。
# 它等價於：open(..., "wb") 後呼叫 f.write(bytes_data)
Path("fake.png").write_bytes(magic)

# 讀回前 8 bytes，對照 PNG 檔頭
# 用 rb（read binary）讀到的是 bytes，不經過文字解碼。
# 注意：若改成 "rt"，Python 會嘗試把內容當文字解碼，
# 對圖片/壓縮檔通常會失敗或造成資料毀損。
with open("fake.png", "rb") as f:
    head = f.read(8)
print(head)           # b'\x89PNG\r\n\x1a\n'
print(head == magic)  # True

# bytes 可逐位元組迭代（拿到 int，不是 str）
# 每個元素範圍是 0~255，常用於協定解析、封包分析、檔頭檢查。
# 這裡只看前 4 個位元組，印十進位與十六進位表示。
for b in head[:4]:
    print(b, hex(b))

# ── 文字 vs 位元組的型別差 ─────────────────────────────
s = "你好"
b = s.encode("utf-8")   # str → bytes（把「文字」轉成「可儲存/傳輸的位元組」）
print(s, type(s))       # <class 'str'>
print(b, type(b))       # <class 'bytes'>
# decode 會依指定編碼把 bytes 還原成 str。
# 方向要記住：
# - encode：str -> bytes
# - decode：bytes -> str
print(b.decode("utf-8"))  # bytes → str

# ── 5.1 encoding 參數：寫錯會爛掉 ──────────────────────
# 明確指定 encoding="utf-8"，可避免不同平台預設編碼不一致。
# 在 Windows 上若省略 encoding，常見預設不是 UTF-8，容易出現亂碼。
Path("zh.txt").write_text("中文測試\n", encoding="utf-8")

# 正常：用 utf-8 讀 utf-8 寫的檔
print(Path("zh.txt").read_text(encoding="utf-8"))

# 故意弄錯：用 big5 解 utf-8 → UnicodeDecodeError
try:
    print(Path("zh.txt").read_text(encoding="big5"))
except UnicodeDecodeError as e:
    # 實務上看到這種錯誤，通常是「檔案實際編碼」與「讀取編碼」不一致。
    # 排查步驟常見是：
    # 1) 確認檔案來源（編輯器、下載來源、資料庫匯出）
    # 2) 嘗試常見編碼（utf-8、big5、cp950 等）
    # 3) 統一團隊寫入格式為 UTF-8
    print("解碼錯誤:", e)

# 小結：
# - 文字檔 → 'rt'/'wt'，一律明示 encoding='utf-8'
# - 非文字（png/zip/pickle）→ 'rb'/'wb'，不談 encoding
