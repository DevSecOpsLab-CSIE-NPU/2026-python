# R04. 十六進位與 Base64 編碼解碼（6.9–6.10）
# 主題：`binascii`、`base64`、`bytes.hex()`、`bytes.fromhex()` 的基本用法
# 註解語言：繁體中文（臺灣 zh-TW），並補充資料型別、用途與常見注意事項

import binascii
import base64

# ── 6.9 十六進位（Hex）────────────────────────────────────
# Hex 編碼常用來把二進位資料轉成「較容易閱讀或傳輸」的文字表示方式。
# 例如雜湊值、MAC 位址、原始位元組內容等，常會以十六進位形式呈現。

# 這裡的 `data` 是 bytes 物件，內容是 "Hello, 世界" 的 UTF-8 編碼。
# `\xe4\xb8\x96\xe7\x95\x8c` 就是「世界」兩個字在 UTF-8 下的位元組內容。
data = b"Hello, \xe4\xb8\x96\xe7\x95\x8c"   # "Hello, 世界" in UTF-8

# bytes → hex 字串
# `binascii.b2a_hex()` 會把 bytes 轉成十六進位表示；回傳值仍然是 bytes，
# 內容看起來像 ASCII 字串，但本質上還是 bytes。
hex_str = binascii.b2a_hex(data)
print("b2a_hex：", hex_str)                   # b'48656c6c6f2c ...'

# `bytes.hex()` 是 Python 3.5+ 提供的更直觀寫法，回傳的是純字串 `str`。
# 與 `b2a_hex()` 相比，它通常更適合直接顯示或拼接到文字中。
hex_str2 = data.hex()                         # Python 3.5+ 內建方法
print(".hex()：", hex_str2)

# hex 字串 → bytes
# `binascii.a2b_hex()` 可以把十六進位內容還原回 bytes。
# 這一步很常見於「從儲存格式還原原始資料」的情境。
restored = binascii.a2b_hex(hex_str)
print("a2b_hex：", restored)

# `bytes.fromhex()` 是對應的內建寫法，接受 hex 字串並回傳 bytes。
# 若資料是人類可讀的 hex 字串，這個方法通常更容易閱讀。
restored2 = bytes.fromhex(hex_str2)           # Python 3.5+
print("fromhex：", restored2)

# 用 assert 確認轉換前後資料一致。
# 這裡可以幫助我們確認編碼與解碼沒有遺失任何位元組。
assert restored == data     # 確認一致

# ── 6.10 Base64 ───────────────────────────────────────────
# Base64 是另一種「把 bytes 轉成文字」的編碼方式，常用於：
# - Email 附件
# - HTTP 認證資訊
# - JWT / API 傳輸內容
# - 某些只接受文字格式的欄位
# 注意：Base64 不是加密，它只是編碼，任何人都可以解碼還原。
msg = b"Python Cookbook"

# 編碼
# `base64.b64encode()` 會把 bytes 轉成 Base64 格式，回傳值仍是 bytes。
# 如果要顯示成一般字串，通常可再用 `.decode("ascii")`。
encoded = base64.b64encode(msg)
print("\nb64encode：", encoded)               # b'UHl0aG9uIENvb2tib29r'

# 解碼
# `base64.b64decode()` 可以把 Base64 bytes 還原回原始 bytes。
# 這通常用在收到文字格式的 Base64 資料後，還原出原本內容。
decoded = base64.b64decode(encoded)
print("b64decode：", decoded)                 # b'Python Cookbook'

# URL-safe Base64（不含 +/，改用 -_）
# 一般 Base64 會使用 `+` 與 `/`，但這些字元在 URL、檔名或某些系統中可能不方便。
# `urlsafe_b64encode()` 會改用 `-` 與 `_`，比較適合放在網址參數或路徑中。
url_encoded = base64.urlsafe_b64encode(msg)
print("urlsafe：  ", url_encoded)

# ── 應用場景比較 ──────────────────────────────────────────
# Hex：
# - 可讀性高，通常每 1 byte 會變成 2 個 hex 字元，因此長度約為原始資料的 2 倍。
# - 常見於 hash、MAC 位址、除錯輸出、低階資料檢視。
# Base64：
# - 長度較短，約為原始資料的 1.33 倍，適合傳輸與儲存。
# - 常見於 email 附件、HTTP 認證、JWT、API payload 中的二進位內容。
# 兩者都只是「表示方式」，不是加密；如果資料需要保密，應該使用真正的加密演算法。

# ── 常見提醒 ─────────────────────────────────────────────
# - `binascii` 與 `base64` 多半輸入/輸出都是 bytes。
# - 若想拿來直接印在畫面上或寫進純文字檔，常常要再做一次 `.decode("ascii")`。
# - `hex()` / `fromhex()` 是處理 hex 的簡潔寫法；Base64 則通常使用 `base64` 模組。
# - 解碼失敗通常表示資料格式不正確，實務上要搭配例外處理。