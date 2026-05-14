# R04. 十六進位與 Base64 編碼解碼（6.9–6.10）
# binascii / base64 / bytes.hex() / bytes.fromhex()

# 匯入 binascii 模組
# binascii 是 Python 內建的二進位與 ASCII 編碼轉換工具
# 常用來：
# 1. bytes 與十六進位互轉
# 2. Base16 / Base32 / Base64 編碼處理
# 3. 網路傳輸與資料封包分析
import binascii

# 匯入 base64 模組
# base64 模組專門處理 Base64 編碼與解碼
# 常見用途：
# 1. Email 附件
# 2. HTTP Basic Authentication
# 3. JWT Token
# 4. 圖片轉文字傳輸
import base64

# ── 6.9 十六進位（Hex）────────────────────────────────────

# b""：
# 代表 bytes（二進位資料）

# \xe4\xb8\x96\xe7\x95\x8c：
# 是 UTF-8 編碼後的「世界」

# data 實際內容為：
# "Hello, 世界"

# 但目前型態是 bytes
# 而不是 Python 字串 str
data = b"Hello, \xe4\xb8\x96\xe7\x95\x8c"   # "Hello, 世界" in UTF-8

# bytes → hex 字串

# binascii.b2a_hex()：
# 將 bytes 轉換成十六進位表示

# b2a：
# binary to ascii

# 回傳值型態仍然是 bytes
# 只是內容改成十六進位文字
hex_str = binascii.b2a_hex(data)

# 印出十六進位結果
# 例如：
# b'48656c6c6f2c20e4b896e7958c'
print("b2a_hex：", hex_str)                   # b'48656c6c6f2c ...'

# data.hex()：
# Python 3.5+ 提供的 bytes 內建方法

# 功能與 b2a_hex 類似
# 但回傳型態是 str，不是 bytes

# 通常實務上更常使用 .hex()
hex_str2 = data.hex()                         # Python 3.5+ 內建方法

# 印出 hex 字串
print(".hex()：", hex_str2)

# hex 字串 → bytes

# binascii.a2b_hex()：
# 將十六進位資料轉回原本 bytes

# a2b：
# ascii to binary
restored = binascii.a2b_hex(hex_str)

# 印出還原後 bytes
print("a2b_hex：", restored)

# bytes.fromhex()：
# Python 3.5+ 提供的內建方法

# 將十六進位字串轉回 bytes
restored2 = bytes.fromhex(hex_str2)           # Python 3.5+

# 印出結果
print("fromhex：", restored2)

# assert：
# 用來確認條件是否成立

# 如果 restored != data：
# 程式會發生 AssertionError

# 這裡是確認：
# 「轉成 hex 再轉回來」後資料沒有改變
assert restored == data     # 確認一致

# ── 6.10 Base64 ───────────────────────────────────────────

# 建立 bytes 資料
# Base64 處理的通常是 bytes
msg = b"Python Cookbook"

# 編碼

# base64.b64encode()：
# 將 bytes 編碼成 Base64 格式

# Base64 會把二進位資料轉成：
# A-Z a-z 0-9 + /

# 方便文字傳輸
encoded = base64.b64encode(msg)

# 印出 Base64 編碼結果
# b'UHl0aG9uIENvb2tib29r'
print("\nb64encode：", encoded)               # b'UHl0aG9uIENvb2tib29r'

# 解碼

# base64.b64decode()：
# 將 Base64 還原回原始 bytes
decoded = base64.b64decode(encoded)

# 印出解碼結果
print("b64decode：", decoded)                 # b'Python Cookbook'

# URL-safe Base64（不含 +/，改用 -_）

# 一般 Base64 的 + 與 /
# 在 URL 中可能有特殊用途

# urlsafe_b64encode()：
# 會改用：
# + → -
# / → _

# 適合放在 URL、JWT、Token
url_encoded = base64.urlsafe_b64encode(msg)

# 印出 URL-safe Base64
print("urlsafe：  ", url_encoded)

# ── 應用場景比較 ──────────────────────────────────────────

# Hex：
# 1 byte → 2 個十六進位字元
# 所以資料長度約變成原本 2 倍

# 優點：
# 可讀性高
# 常用於：
# 1. hash 值
# 2. MAC Address
# 3. 封包分析
# 4. 二進位除錯

# Base64：
# 長度約變成原本 1.33 倍
# 比 Hex 更節省空間

# 常用於：
# 1. Email 附件
# 2. HTTP 認證
# 3. JWT Token
# 4. 圖片傳輸
# 5. API 資料交換

# 注意：
# Hex 與 Base64 都不是加密技術

# 它們只是：
# 「資料表示方式（Encoding）」

# 任何人都可以輕易解碼還原
# 不能拿來保護敏感資料
# Hex    → 可讀性高，長度 2x，常見於 hash / MAC 位址
# Base64 → 長度約 1.33x，常見於 email 附件、HTTP 認證、JWT
# 兩者都只是「表示方式」，不是加密！