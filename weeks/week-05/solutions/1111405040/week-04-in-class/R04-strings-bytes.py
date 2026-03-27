"""
R04: bytes 與字串的差異。

示範重點：
1. `bytes` 的切片、搜尋與取代。
2. 對 bytes 使用正規表達式。
3. 字串與 bytes 在索引與格式化上的差異。
"""

import re

data = b"Hello World"

# bytes 可以像字串一樣切片、比對開頭與切分。
print(data[0:5])  # b'Hello'
print(data.startswith(b"Hello"))  # True
print(data.split())  # [b'Hello', b'World']
print(data.replace(b"Hello", b"Hello Cruel"))  # b'Hello Cruel World'

# 若資料本身是 bytes，正規表達式樣式也要寫成 bytes 版本。
raw = b"FOO:BAR,SPAM"
print(re.split(rb"[:,]", raw))  # [b'FOO', b'BAR', b'SPAM']

# 一般字串索引後得到的是單一字元字串；
# bytes 索引後得到的是該位元組的整數值。
text = "Hello"
binary = b"Hello"
print(text[0])  # 'H'
print(binary[0])  # 72

# `format()` 先產生字串，再用 `encode()` 轉成 bytes。
formatted = "{:10s} {:10d}".format("ACME", 100).encode("ascii")
print(formatted)  # b'ACME            100'
