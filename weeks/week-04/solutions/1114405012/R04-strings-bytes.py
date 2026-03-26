# R04. 位元組字串操作（2.20）
# bytes / bytearray 支援大部分字串方法，但有幾個重要差異

import re

# 建立一個 bytes 物件（前綴 b 代表位元組字串）
data = b"Hello World"
# 切片操作和一般字串一樣，回傳仍是 bytes
print(data[0:5])  # b'Hello'
# bytes 版本的 startswith 參數也必須是 bytes
print(data.startswith(b"Hello"))  # True
# 以空白分割，結果是 bytes 清單
print(data.split())  # [b'Hello', b'World']
# 取代子字串，傳入與回傳都要是 bytes
print(data.replace(b"Hello", b"Hello Cruel"))  # b'Hello Cruel World'

# 正則表達式也必須使用 bytes 模式
raw = b"FOO:BAR,SPAM"
# rb"..."：r 代表 raw string、b 代表 bytes pattern
print(re.split(rb"[:,]", raw))  # [b'FOO', b'BAR', b'SPAM']

# 差異 1：索引回傳整數而非字元
a = "Hello"
b = b"Hello"
# str 索引回傳字元（型別是 str）
print(a[0])  # 'H'（字元）
# bytes 索引回傳 0~255 的整數（這裡是 ASCII 的 H = 72）
print(b[0])  # 72（整數，即 ord('H')）

# 差異 2：不能直接用 format()，需先編碼
# format() 會產生 str，若要變成 bytes，需再 encode()
formatted = "{:10s} {:10d}".format("ACME", 100).encode("ascii")
print(formatted)  # b'ACME            100'
