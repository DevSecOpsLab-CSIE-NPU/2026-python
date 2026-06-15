# R04. 十六進位與 Base64 編碼解碼（6.9–6.10）
# binascii / base64 / bytes.hex() / bytes.fromhex()
#
# 十六進位與 Base64 都是「二進位資料的文字表示方式」，不是加密。
# Hex    → 可讀性高，長度 2x，常見於 hash、MAC 位址、檔案横指
# Base64 → 長度約4/3，常見於 email 附件、HTTP 認證、JWT

import binascii
import base64

# ── 6.9 十六進位（Hex）────────────────────────────────────
# b"..." 是 bytes 字面尤，\xe4\xb8\x96\xe7\x95\x8c 是「世界」的 UTF-8 位元組
data = b"Hello, \xe4\xb8\x96\xe7\x95\x8c"   # "Hello, 世界" in UTF-8

# bytes → hex 字串（方法一）：binascii.b2a_hex 回傳 bytes 型式的十六進位字串
hex_str = binascii.b2a_hex(data)
print("b2a_hex：", hex_str)                   # b'48656c6c6f2c ...'

# bytes → hex 字串（方法二）：Python 3.5+ 內建方法，回傳純 str
hex_str2 = data.hex()
print(".hex()：", hex_str2)

# hex 字串 → bytes（方法一）
restored = binascii.a2b_hex(hex_str)
print("a2b_hex：", restored)

# hex 字串 → bytes（方法二）：Python 3.5+ 內建
restored2 = bytes.fromhex(hex_str2)
print("fromhex：", restored2)

# 確認雙向轉換結果一致，不一致會丟出 AssertionError
assert restored == data

# ── 6.10 Base64 ───────────────────────────────────────────
msg = b"Python Cookbook"

# 編碼：bytes → Base64，回傳的仍是 bytes（由 ASCII 可列印字元構成）
encoded = base64.b64encode(msg)
print("\nb64encode：", encoded)               # b'UHl0aG9uIENvb2tib29r'

# 解碼：Base64 bytes → 原始 bytes
decoded = base64.b64decode(encoded)
print("b64decode：", decoded)                 # b'Python Cookbook'

# URL-safe Base64：把 + 替換 -、/ 替換 _
# 適合嵌入 URL 查詢字串或 JWT，避免需要 URL 編碼
url_encoded = base64.urlsafe_b64encode(msg)
print("urlsafe：  ", url_encoded)

# ── 應用場景比較 ─────────────────────────────────────────
# Hex    → 可讀性高，長度 2x，常見於 hash / MAC 位址
# Base64 → 長度絀1.33x，常見於 email 附件、HTTP 認證、JWT
# ★ 兩者都只是「表示方式」，不是加密！
