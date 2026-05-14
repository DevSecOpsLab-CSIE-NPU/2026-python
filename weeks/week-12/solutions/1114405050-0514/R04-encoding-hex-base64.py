# R04. 十六進位與 Base64 編碼解碼（6.9–6.10）
# binascii / base64 / bytes.hex() / bytes.fromhex()

import binascii
import base64

# ── 6.9 十六進位（Hex）────────────────────────────────────
# b"..." 代表 bytes (位元組) 型別，\x 後面接的是十六進位編碼 (這裡示範 UTF-8 的中文編碼)
data = b"Hello, \xe4\xb8\x96\xe7\x95\x8c"   # "Hello, 世界" in UTF-8

# bytes → hex 字串
# binascii.b2a_hex (binary to ascii) 將 bytes 轉成十六進位表示的 bytes 字串
hex_str = binascii.b2a_hex(data)
print("b2a_hex：", hex_str)                   # b'48656c6c6f2c ...'

# data.hex() 是一般字串方法，轉出的是純文字的十六進位字串 (通常推薦使用這種方式)
hex_str2 = data.hex()                         # Python 3.5+ 內建方法
print(".hex()：", hex_str2)

# hex 字串 → bytes
# binascii.a2b_hex (ascii to binary) 將十六進位字串轉回原始 bytes
restored = binascii.a2b_hex(hex_str)
print("a2b_hex：", restored)

# bytes.fromhex() 將一般的純文字十六進位字串轉回 bytes (推薦使用)
restored2 = bytes.fromhex(hex_str2)           # Python 3.5+
print("fromhex：", restored2)

# assert 用於斷言，確保兩邊的資料相等，如果不等就會拋出 AssertionError 錯誤
assert restored == data     # 確認一致

# ── 6.10 Base64 ───────────────────────────────────────────
msg = b"Python Cookbook"

# 編碼
# base64.b64encode 會將二進位 bytes 資料編碼為 Base64 格式 (僅使用 64 個可列印字元)
encoded = base64.b64encode(msg)
print("\nb64encode：", encoded)               # b'UHl0aG9uIENvb2tib29r'

# 解碼
# base64.b64decode 將 Base64 格式轉換回原始的二進位 bytes 資料
decoded = base64.b64decode(encoded)
print("b64decode：", decoded)                 # b'Python Cookbook'

# URL-safe Base64（不含 +/，改用 -_）
# 標準 Base64 會產生 '+' 和 '/'，但這兩個字元在網址 URL 中有特殊意義容易衝突
# urlsafe_b64encode 會將 '+' 換成 '-'，'/' 換成 '_'，確保編碼後能安全地放在網址列中傳遞
url_encoded = base64.urlsafe_b64encode(msg)
print("urlsafe：  ", url_encoded)

# ── 應用場景比較 ──────────────────────────────────────────
# Hex    → 可讀性高，長度 2x，常見於 hash / MAC 位址
# Base64 → 長度約 1.33x，常見於 email 附件、HTTP 認證、JWT
# 兩者都只是「表示方式」，不是加密！
