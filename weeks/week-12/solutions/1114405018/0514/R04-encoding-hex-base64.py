"""R04. 十六進位與 Base64 編碼解碼（6.9–6.10）

說明（繁體中文詳細註解）：
- Hex 與 Base64 都是將二進位資料轉為文字表示的常用方法，常見於資料傳輸、儲存或除錯。
- 十六進位（hex）常用於顯示原始 bytes（例如雜湊值、記憶體檢視），每個 byte 由兩個 hex 字元表示。
- Base64 則用 64 個可列印字元表示 bytes，常用於電子郵件附件、URL-safe 表示、JWT 等。

重要觀念：這些編碼是「編碼」不是「加密」，無法提供隱私或安全保護。
"""

import binascii
import base64


# 6.9 十六進位（Hex）
data = b"Hello, \xe4\xb8\x96\xe7\x95\x8c"   # "Hello, 世界" in UTF-8

# 將 bytes 轉為 hex 字串（表示時通常是 bytes 顯示形式或 str）
hex_str = binascii.b2a_hex(data)
print("b2a_hex：", hex_str)                   # b'48656c6c6f2c ...'

hex_str2 = data.hex()                         # Python 3.5+ 提供的內建方法，回傳 str
print(".hex()：", hex_str2)


# hex 字串還原為 bytes
restored = binascii.a2b_hex(hex_str)
print("a2b_hex：", restored)

restored2 = bytes.fromhex(hex_str2)           # Python 3.5+ 內建方法
print("fromhex：", restored2)

assert restored == data     # 驗證還原一致


# 6.10 Base64
msg = b"Python Cookbook"

# 編碼：bytes -> base64 bytes
encoded = base64.b64encode(msg)
print("\nb64encode：", encoded)               # b'UHl0aG9uIENvb2tib29r'

# 解碼：base64 bytes -> 原始 bytes
decoded = base64.b64decode(encoded)
print("b64decode：", decoded)                 # b'Python Cookbook'


# URL-safe Base64（避免 +/，改用 -_，可直接放在 URL 中）
url_encoded = base64.urlsafe_b64encode(msg)
print("urlsafe：  ", url_encoded)


# 應用場景比較（補充）
# - Hex    → 可讀性高（以十六進位表示），但字元數為 bytes 的兩倍
# - Base64 → 表示更緊湊（約 4/3 倍），常用於 HTTP 與網路傳輸
# 註：若要在 URL 中使用 Base64，請使用 urlsafe 變體並注意 padding (=)
