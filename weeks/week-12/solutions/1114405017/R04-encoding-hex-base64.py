# R04. 十六進位與 Base64 編碼解碼（6.9–6.10）
# binascii / base64 / bytes.hex() / bytes.fromhex()

# 匯入必要的模組
import binascii  # 用於二進位資料與ASCII之間的轉換
import base64    # 用於Base64編碼解碼

# ── 6.9 十六進位（Hex）────────────────────────────────────
# 定義一個包含UTF-8編碼中文的bytes物件
data = b"Hello, \xe4\xb8\x96\xe7\x95\x8c"   # "Hello, 世界" in UTF-8

# bytes → hex 字串：使用binascii.b2a_hex()將bytes轉換為十六進位字串
hex_str = binascii.b2a_hex(data)
print("b2a_hex：", hex_str)                   # 輸出十六進位字串

# 使用Python 3.5+的內建方法.hex()將bytes轉換為十六進位字串
hex_str2 = data.hex()                         # Python 3.5+ 內建方法
print(".hex()：", hex_str2)

# hex 字串 → bytes：使用binascii.a2b_hex()將十六進位字串轉換回bytes
restored = binascii.a2b_hex(hex_str)
print("a2b_hex：", restored)

# 使用bytes.fromhex()將十六進位字串轉換回bytes（Python 3.5+）
restored2 = bytes.fromhex(hex_str2)           # Python 3.5+
print("fromhex：", restored2)

# 驗證還原的資料是否與原始資料相同
assert restored == data     # 斷言檢查一致性

# ── 6.10 Base64 ───────────────────────────────────────────
# 定義一個bytes物件作為範例訊息
msg = b"Python Cookbook"

# 編碼：使用base64.b64encode()將bytes編碼為Base64格式
encoded = base64.b64encode(msg)
print("\nb64encode：", encoded)               # 輸出Base64編碼結果

# 解碼：使用base64.b64decode()將Base64編碼轉換回原始bytes
decoded = base64.b64decode(encoded)
print("b64decode：", decoded)                 # 輸出解碼結果

# URL-safe Base64：使用base64.urlsafe_b64encode()產生URL安全的Base64編碼
# 將原本的+/替換為-_，避免在URL中出現問題
url_encoded = base64.urlsafe_b64encode(msg)
print("urlsafe：  ", url_encoded)

# ── 應用場景比較 ──────────────────────────────────────────
# Hex（十六進位）：
# - 可讀性高，長度為原始資料的2倍
# - 常用於雜湊值（hash）/ MAC位址的表示
# - 每個位元組轉換為兩個十六進位字元
#
# Base64：
# - 長度約為原始資料的1.33倍（因為6位元編碼為8位元字元）
# - 常用於email附件、HTTP認證、JWT（JSON Web Token）
# - 兩者都只是「表示方式」，並不是加密方法！
