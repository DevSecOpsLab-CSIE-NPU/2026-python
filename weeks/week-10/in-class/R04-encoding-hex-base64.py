# R04. 十六進位與 Base64 編碼解碼（6.9–6.10）
# binascii / base64 / bytes.hex() / bytes.fromhex()

import binascii
import base64

# ── 6.9 十六進位（Hex）────────────────────────────────────
data = b"Hello, \xe4\xb8\x96\xe7\x95\x8c"   # "Hello, 世界" in UTF-8

# bytes → hex 字串
hex_str = binascii.b2a_hex(data)
print("b2a_hex：", hex_str)                   # b'48656c6c6f2c ...'

hex_str2 = data.hex()                         # Python 3.5+ 內建方法
print(".hex()：", hex_str2)

# hex 字串 → bytes
restored = binascii.a2b_hex(hex_str)
print("a2b_hex：", restored)

restored2 = bytes.fromhex(hex_str2)           # Python 3.5+
print("fromhex：", restored2)

assert restored == data     # 確認一致

# ── 6.10 Base64 ───────────────────────────────────────────
msg = b"Python Cookbook"

# 編碼
encoded = base64.b64encode(msg)
print("\nb64encode：", encoded)               # b'UHl0aG9uIENvb2tib29r'

# 解碼
decoded = base64.b64decode(encoded)
print("b64decode：", decoded)                 # b'Python Cookbook'

# URL-safe Base64（不含 +/，改用 -_）
url_encoded = base64.urlsafe_b64encode(msg)
print("urlsafe：  ", url_encoded)

# ── 應用場景比較 ──────────────────────────────────────────
# Hex    → 可讀性高，長度 2x，常見於 hash / MAC 位址
# Base64 → 長度約 1.33x，常見於 email 附件、HTTP 認證、JWT
# 兩者都只是「表示方式」，不是加密！
