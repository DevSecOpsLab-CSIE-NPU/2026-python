# R04. 位元組字串操作（2.20）
# bytes / bytearray 支援大部分字串方法，但有幾個重要差異

import re

# bytes 物件的資料是不可變的位元組序列
# 在顯示時會以 b'' 形式表示
data = b"Hello World"
print(data[0:5])  # b'Hello'
print(data.startswith(b"Hello"))  # True
print(data.split())  # [b'Hello', b'World']
print(data.replace(b"Hello", b"Hello Cruel"))  # b'Hello Cruel World'

# 正則表達式也必須使用 bytes 模式，前面加上 b 或 rb
raw = b"FOO:BAR,SPAM"
print(re.split(rb"[:,]", raw))  # [b'FOO', b'BAR', b'SPAM']

# 差異 1：bytes 的索引會回傳整數，而不是字元
# 因為位元組代表的是數值 0~255
a = "Hello"
b = b"Hello"
print(a[0])  # 'H'（字元）
print(b[0])  # 72（整數，即 ord('H')）

# 差異 2：bytes 無法直接格式化字串
# 必須先格式化成 str 再編碼為 bytes
formatted = "{:10s} {:10d}".format("ACME", 100).encode("ascii")
print(formatted)  # b'ACME            100'
