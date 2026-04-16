"""R04 位元組字串操作（2.20）。"""

# bytes / bytearray 看起來像字串，但索引、正則、格式化都有不同規則

import re

# bytes 也能做切片、startswith、split、replace
data = b"Hello World"
print(data[0:5])  # b'Hello'
print(data.startswith(b"Hello"))  # True
print(data.split())  # [b'Hello', b'World']
print(data.replace(b"Hello", b"Hello Cruel"))  # b'Hello Cruel World'

# 正則表達式處理 bytes 時，pattern 也必須是 bytes
raw = b"FOO:BAR,SPAM"
print(re.split(rb"[:,]", raw))  # [b'FOO', b'BAR', b'SPAM']

# 差異 1：bytes 索引回傳的是整數，不是單一字元字串
a = "Hello"
b = b"Hello"
print(a[0])  # 'H'（字元）
print(b[0])  # 72（整數，即 ord('H')）

# 差異 2：bytes 不能直接做字串格式化，通常要先 format 再 encode
formatted = "{:10s} {:10d}".format("ACME", 100).encode("ascii")
print(formatted)  # b'ACME            100'
