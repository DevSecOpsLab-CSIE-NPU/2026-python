# R04. 十六進位與 Base64 編碼解碼（6.9–6.10）
# binascii / base64 / bytes.hex() / bytes.fromhex()

import binascii
import base64

# ── 6.9 十六進位（Hex）────────────────────────────────────
# 這裡用 bytes 直接模擬含中文的 UTF-8 資料，方便示範編碼與解碼。
data = b"Hello, \xe4\xb8\x96\xe7\x95\x8c"   # "Hello, 世界" in UTF-8

# bytes → hex 字串
# binascii.b2a_hex 會把 bytes 轉成十六進位表示法。
hex_str = binascii.b2a_hex(data)
print("b2a_hex：", hex_str)                   # b'48656c6c6f2c ...'

hex_str2 = data.hex()                         # Python 3.5+ 內建方法
# .hex() 是更直覺的寫法，效果和 b2a_hex 類似。
print(".hex()：", hex_str2)

# hex 字串 → bytes
# a2b_hex 會把十六進位字串還原回原始 bytes。
restored = binascii.a2b_hex(hex_str)
print("a2b_hex：", restored)

restored2 = bytes.fromhex(hex_str2)           # Python 3.5+
# bytes.fromhex 也是內建的還原方法。
print("fromhex：", restored2)

assert restored == data     # 確認一致

# ── 6.10 Base64 ───────────────────────────────────────────
# Base64 常用於把 binary 資料轉成可傳輸的文字格式。
msg = b"Python Cookbook"

# 編碼
# b64encode 會把 bytes 編成 Base64。
encoded = base64.b64encode(msg)
print("\nb64encode：", encoded)               # b'UHl0aG9uIENvb2tib29r'

# 解碼
# b64decode 則把 Base64 還原回原始 bytes。
decoded = base64.b64decode(encoded)
print("b64decode：", decoded)                 # b'Python Cookbook'

# URL-safe Base64（不含 +/，改用 -_）
# urlsafe 版本適合放在網址或檔名中，避免特殊字元造成問題。
url_encoded = base64.urlsafe_b64encode(msg)
print("urlsafe：  ", url_encoded)

# ── 應用場景比較 ──────────────────────────────────────────
# Hex    → 可讀性高，長度 2x，常見於 hash / MAC 位址
# Base64 → 長度約 1.33x，常見於 email 附件、HTTP 認證、JWT
# 兩者都只是「表示方式」，不是加密！
