# R04. 十六進位與 Base64 編碼解碼（6.9–6.10）
# binascii / base64 / bytes.hex() / bytes.fromhex()

import binascii
import base64

# ── 6.9 十六進位（Hex）────────────────────────────────────
# 【詳解】
# Hex 編碼將每個 byte 用 2 個十六進位字元（0-9, a-f）表示。
# 特性：人類可讀、檔案大小為原始的 2 倍、常見於 hash、MAC 位址。
# binascii 是較低層的轉換工具。

data = b"Hello, \xe4\xb8\x96\xe7\x95\x8c" # "Hello, 世界" in UTF-8

# bytes → hex 字串
hex_str = binascii.b2a_hex(data)
print("b2a_hex：", hex_str) # b'48656c6c6f2c ...'

hex_str2 = data.hex() # Python 3.5+ 內建方法
print(".hex()：", hex_str2)

# hex 字串 → bytes
restored = binascii.a2b_hex(hex_str)
print("a2b_hex：", restored)

restored2 = bytes.fromhex(hex_str2) # Python 3.5+
print("fromhex：", restored2)

assert restored == data # 確認一致

# ── 6.10 Base64 ───────────────────────────────────────────
# 【詳解】
# Base64 使用 64 個可列印 ASCII 字元表示任意 bytes。
# 3 個 bytes → 4 個 Base64 字元，檔案大小約為原始的 4/3。
# 常見場景：email 附件、HTTP Basic Auth、JWT、Data URL。
# 末尾不足時用 = 補齊（padding）。
msg = b"Python Cookbook"

# 編碼
encoded = base64.b64encode(msg)
print("\nb64encode：", encoded) # b'UHl0aG9uIENvb2tib29r'

# 解碼
decoded = base64.b64decode(encoded)
print("b64decode：", decoded) # b'Python Cookbook'

# URL-safe Base64（不含 +/，改用 -_）
# 標準 Base64 的 + / 在 URL 中有特殊意義，會造成問題。
# URL-safe 版本將其改為 - _，可安全放在 URL 或檔案名稱中。
url_encoded = base64.urlsafe_b64encode(msg)
print("urlsafe： ", url_encoded)
