# R04. 十六進位與 Base64 編碼解碼（6.9–6.10）
# 本示例展示了二進位資料的兩種常見編碼方式：
# 1. 十六進位 (Hex)：每 1 byte (8 bits) 用 2 個十六進位數字表示
#    優點：簡潔易讀；缺點：編碼後長度是原來的 2 倍
# 2. Base64：每 3 bytes (24 bits) 用 4 個字元表示
#    優點：編碼後長度約原來的 1.33 倍；缺點：字元集較複雜
#
# 重要觀念：Hex 和 Base64 「不是加密」，只是編碼方式，任何人都能解碼
# 常見用途：傳輸二進位資料、HTTP 認證、email 附件、JWT 令牌

import binascii  # 標準庫：二進位 <> ASCII 轉換（Hex 操作）
import base64    # 標準庫：Base64 編碼/解碼

# ── 6.9 十六進位（Hex）────────────────────────────────────
# 十六進位是以 16 為基數的計數系統，用 0-9 和 A-F 表示（共 16 個符號）
# 優點：每個十六進位數字恰好代表 4 bits，方便與二進位互轉
# 用途：hash 值（MD5、SHA1）、MAC 位址、色碼 (#FF0000) 等
data = b"Hello, \xe4\xb8\x96\xe7\x95\x8c"   # "Hello, 世界" 的 UTF-8 位元組表示
# \xe4\xb8\x96\xe7\x95\x8c 是「世界」的 UTF-8 編碼（每個中文字占 3 bytes）

# bytes → hex 字串
# binascii.b2a_hex() 將二進位資料轉換為十六進位 ASCII 字串
# 結果為 b'...' 形式（仍是 bytes），需要解碼為 str 才能閱讀
hex_str = binascii.b2a_hex(data)
print("b2a_hex：", hex_str)                   # 預期：b'48656c6c6f2c20e4b896e7958c'

# Python 3.5+ 提供更簡潔的 .hex() 方法（推薦使用）
hex_str2 = data.hex()                         # 直接返回 str 型別，不需額外解碼
print(".hex()：", hex_str2)                   # 預期：'48656c6c6f2c20e4b896e7958c'

# hex 字串 → bytes
# binascii.a2b_hex() 反向操作：將十六進位字串轉回二進位資料
restored = binascii.a2b_hex(hex_str)
print("a2b_hex：", restored)                  # 預期：b'Hello, \xe4\xb8\x96\xe7\x95\x8c'

# Python 3.5+ 的 bytes.fromhex() 方法（推薦使用）
# 注意：fromhex() 只接受 str，不接受 bytes
restored2 = bytes.fromhex(hex_str2)           # 直接從 hex 字串還原為 bytes
print("fromhex：", restored2)                 # 預期：b'Hello, \xe4\xb8\x96\xe7\x95\x8c'

# 驗證編碼/解碼的正確性
assert restored == data     # 確認解碼後與原始資料一致

# ── 6.10 Base64 ───────────────────────────────────────────
# Base64 是以 64 為基數的編碼方式，用 A-Z、a-z、0-9、+、/ 表示（共 64 個符號）
# 原理：將 3 個 bytes (24 bits) 分成 4 組 6-bit，各自對應一個 Base64 字元
# 優點：編碼後長度約原來的 1.33 倍（比 Hex 的 2 倍更節省空間）
# 用途：email 附件、HTTP 認證、JSON Web Token (JWT)、API 金鑰傳輸
msg = b"Python Cookbook"

# 編碼（bytes → Base64 字串）
# base64.b64encode() 將二進位資料轉換為 Base64 編碼（結果為 bytes）
encoded = base64.b64encode(msg)
print("\nb64encode：", encoded)               # 預期：b'UHl0aG9uIENvb2tib29r'

# 解碼（Base64 字串 → bytes）
# base64.b64decode() 將 Base64 編碼還原為原始二進位資料
decoded = base64.b64decode(encoded)
print("b64decode：", decoded)                 # 預期：b'Python Cookbook'

# URL-safe Base64（用於 URL 和檔案名）
# 標準 Base64 用 +/ 可能在 URL 中產生問題（URL 保留字符）
# urlsafe 版本改用 -_，避免 URL 編碼問題
url_encoded = base64.urlsafe_b64encode(msg)
print("urlsafe：  ", url_encoded)             # 預期：b'UHl0aG9uIENvb2tib29r'（此例無 + 或 /）

# ── 應用場景比較 ──────────────────────────────────────────
# ┌─────────────┬────────────┬──────────────┬──────────────────────────┐
# │ 編碼方式    │ 編碼長度   │ 可讀性       │ 常見用途                 │
# ├─────────────┼────────────┼──────────────┼──────────────────────────┤
# │ Hex         │ 原來 2 倍  │ 高（0-9 A-F）│ hash 值、MAC 位址、色碼  │
# │ Base64      │ 原來 1.33x │ 中等         │ email、HTTP 認證、JWT    │
# └─────────────┴────────────┴──────────────┴──────────────────────────┘
#
# ⚠ 重要警告：Hex 和 Base64 「都不是加密」，只是編碼方式
#            任何人都能立即解碼，不提供安全性保護
#            要傳輸敏感資料必須使用加密（如 TLS/SSL、AES）
#
# 判斷標準：
#   選 Hex  → 需要易於閱讀、長度不重要（如調試 hash 值）
#   選 Base64 → 需要節省空間、安全傳輸文字資料（如 email）
