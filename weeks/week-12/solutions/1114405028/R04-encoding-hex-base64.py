# R04-encoding-hex-base64.py
# 完整繁體中文註釋版：示範十六進位與 Base64 的編碼與解碼

import binascii
import base64

# ── 6.9 十六進位（Hex）編碼與解碼 ─────────────────────────
data = b"Hello, \xe4\xb8\x96\xe7\x95\x8c"   # "Hello, 世界" 的 UTF-8 bytes

# bytes → hex 字串
hex_str = binascii.b2a_hex(data)
print("b2a_hex：", hex_str)

# Python 內建 .hex() 也能產生十六進位字串
hex_str2 = data.hex()
print(".hex()：", hex_str2)

# hex 字串 → bytes
restored = binascii.a2b_hex(hex_str)
print("a2b_hex：", restored)

restored2 = bytes.fromhex(hex_str2)
print("fromhex：", restored2)

assert restored == data

# ── 6.10 Base64 ─────────────────────────────────────────────
msg = b"Python Cookbook"

# 編碼成 Base64 bytes
encoded = base64.b64encode(msg)
print("\nb64encode：", encoded)

# 從 Base64 bytes 解碼回原始 bytes
decoded = base64.b64decode(encoded)
print("b64decode：", decoded)

# URL-safe Base64：將 +/ 換成 -_，適合放在 URL 裡
url_encoded = base64.urlsafe_b64encode(msg)
print("urlsafe：  ", url_encoded)

# ── 應用場景比較 ──────────────────────────────────────────
# Hex    → 可讀性較高，長度為 2 倍，常見於 hash、MAC 地址
# Base64 → 長度約 1.33 倍，常見於 email 附件、HTTP Basic Auth、JWT
# 注意：Hex / Base64 都不是加密，僅是編碼格式。