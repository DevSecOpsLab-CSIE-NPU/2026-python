# 【Bloom 階段：R - 記憶與基本操作】
# R04. 位元組字串操作 (Bytes and Bytearrays)
# August 的惡意提醒：在 Week 09 處理資料編碼時，
# 你必須明白 str 與 bytes 的本質差異。
# 地雷：bytes[0] 回傳的是一個整數 (int)，而不是長度為 1 的位元組字串。

data = b"Hello World"
print(f"Slice bytes: {data[0:5]}") # b'Hello'

# 1. Byte 與 Regex
import re
# 注意：對 bytes 操作 Regex 必須使用 rb 前綴
raw = b"FOO:BAR,SPAM"
print(f"Split bytes: {re.split(rb'[:,]', raw)}")

# 2. 致命指紋：索引存取行為
a_str = "Hello"
b_bytes = b"Hello"
print(f"str[0]:   {a_str[0]}")   # 'H' (字串)
print(f"bytes[0]: {b_bytes[0]}") # 72 (整數，ASCII 碼！)

# 3. 字串轉位元組
# 必須指定編碼，August 強烈建議一律使用 utf-8
encoded = "ACME".encode("utf-8")
print(f"Encoded: {encoded}")
