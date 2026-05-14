# R04. 十六進位與 Base64 編碼解碼（6.9–6.10）
# 本範例示範兩種常見的資料表示法：
# 1. 十六進位（Hex）
# 2. Base64
#
# 它們的用途是「資料編碼」而不是「資料加密」。
# 也就是說，轉換後的內容仍然可以還原回原始 bytes。

import binascii
import base64

# -----------------------------------------------------------------------------
# 一、十六進位（Hex）
# -----------------------------------------------------------------------------
# Hex 是把每個 byte 轉成兩個十六進位字元表示。
# 例如一個 byte 的範圍是 0~255，用 16 進位表示會比二進位更容易閱讀。
#
# 這裡先準備一段 bytes 資料。
# b"Hello, \xe4\xb8\x96\xe7\x95\x8c" 的內容其實就是 UTF-8 編碼後的 "Hello, 世界"。
data = b"Hello, \xe4\xb8\x96\xe7\x95\x8c"

# binascii.b2a_hex() 會把 bytes 轉成 hex 表示的 bytes。
# 注意回傳值仍然是 bytes，不是一般字串。
hex_str = binascii.b2a_hex(data)
print("b2a_hex：", hex_str)                   # b'48656c6c6f2c ...'

# bytes.hex() 是 Python 3.5 之後提供的內建方法，功能與上面類似。
# 不過它直接回傳字串，所以在顯示或記錄時通常更方便。
hex_str2 = data.hex()
print(".hex()：", hex_str2)

# -----------------------------------------------------------------------------
# 二、Hex 還原成 bytes
# -----------------------------------------------------------------------------
# a2b_hex() 會把 hex 內容轉回 bytes。
# 這通常用在你從 log、檔案或協定中讀到十六進位字串後，要還原原始資料的情境。
restored = binascii.a2b_hex(hex_str)
print("a2b_hex：", restored)

# bytes.fromhex() 也是 Python 3.5+ 的便利寫法。
# 它接受的是 hex 字串，因此很適合搭配 .hex() 的輸出使用。
restored2 = bytes.fromhex(hex_str2)
print("fromhex：", restored2)

# 這裡用 assert 檢查還原後的結果是否和原始資料完全一致。
# 若不一致，程式會直接拋出 AssertionError，提醒我們轉換過程有問題。
assert restored == data     # 確認一致

# -----------------------------------------------------------------------------
# 三、Base64
# -----------------------------------------------------------------------------
# Base64 是另一種常見的二進位資料表示方式。
# 它的特色是：可以用可列印的 ASCII 字元表示任意 bytes。
#
# Base64 的字元集合比 Hex 更精簡，所以相同資料通常會比 Hex 短。
msg = b"Python Cookbook"

# base64.b64encode() 會把 bytes 編碼成 Base64。
# 回傳值仍然是 bytes，內容則是 Base64 字元。
encoded = base64.b64encode(msg)
print("\nb64encode：", encoded)               # b'UHl0aG9uIENvb2tib29r'

# base64.b64decode() 則是把 Base64 還原回原始 bytes。
# 這個操作在 API、Token、附件資料等場景非常常見。
decoded = base64.b64decode(encoded)
print("b64decode：", decoded)                 # b'Python Cookbook'

# -----------------------------------------------------------------------------
# 四、URL-safe Base64
# -----------------------------------------------------------------------------
# 標準 Base64 會使用 + 和 / 兩個字元。
# 但這兩個字元在 URL 裡可能需要額外轉義，因此 Python 提供 urlsafe 版本。
# urlsafe Base64 會把 + / 改成 - _，更適合放在網址或查詢參數中。
url_encoded = base64.urlsafe_b64encode(msg)
print("urlsafe：  ", url_encoded)

# -----------------------------------------------------------------------------
# 五、應用場景比較
# -----------------------------------------------------------------------------
# Hex：
# - 可讀性高
# - 長度約為原始資料的 2 倍
# - 常見於 hash、MAC 位址、除錯輸出
#
# Base64：
# - 長度約為原始資料的 1.33 倍
# - 比 Hex 更省空間
# - 常見於 email 附件、HTTP 認證、JWT、API token
#
# 兩者都不是加密方法，只是資料表示方式。
# 如果需要保密，仍然要搭配真正的加密演算法。
