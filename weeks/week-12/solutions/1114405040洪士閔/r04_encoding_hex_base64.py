"""R04. 十六進位與 Base64 編碼解碼。

這份版本整理 bytes.hex()、bytes.fromhex()、binascii 與 base64 的基本用法，
也順便說明它們不是加密，而是「表示方式」的轉換。
"""

import base64
import binascii


# 先準備一段 bytes 資料，內容包含英文與 UTF-8 編碼的中文。
data = b"Hello, \xe4\xb8\x96\xe7\x95\x8c"  # Hello, 世界


# bytes → hex 字串。
hex_str = binascii.b2a_hex(data)
print("b2a_hex：", hex_str)

hex_str2 = data.hex()  # Python 內建方法，寫法更簡單。
print(".hex()：", hex_str2)


# hex 字串 → bytes。
restored = binascii.a2b_hex(hex_str)
print("a2b_hex：", restored)

restored2 = bytes.fromhex(hex_str2)
print("fromhex：", restored2)

# 驗證來回轉換後的內容沒有變。
assert restored == data


# Base64 常用於傳輸或儲存二進位資料，不是用來加密。
msg = b"Python Cookbook"


# 編碼：bytes → base64 bytes。
encoded = base64.b64encode(msg)
print("\nb64encode：", encoded)


# 解碼：base64 bytes → 原始 bytes。
decoded = base64.b64decode(encoded)
print("b64decode：", decoded)


# urlsafe_base64 編碼會把 + / 改成 - _，比較適合放在 URL。
url_encoded = base64.urlsafe_b64encode(msg)
print("urlsafe：  ", url_encoded)


# 概念補充：Hex 字串較長，但可讀性高；Base64 更短，常見於網路傳輸。
# 兩者都只是編碼，不是加密。
