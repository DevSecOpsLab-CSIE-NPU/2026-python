# R04. 位元組字串操作（2.20）
# bytes / bytearray 支援大部分字串方法，但有幾個重要差異

import re

# bytes 常值要在字串前面加上 b，表示內容是位元組序列，不是一般字串
data = b"Hello World"
# 切片操作和一般字串類似，但結果仍然是 bytes 型別
print(data[0:5])  # b'Hello'
# bytes 版本的 startswith() 也要傳入 bytes 參數
print(data.startswith(b"Hello"))  # True
# split() 會把 bytes 依空白切開，回傳 bytes 組成的串列
print(data.split())  # [b'Hello', b'World']
# replace() 可以替換指定的位元組片段
print(data.replace(b"Hello", b"Hello Cruel"))  # b'Hello Cruel World'

# 正則表達式也必須使用 bytes 模式
raw = b"FOO:BAR,SPAM"
# rb"..." 表示 raw bytes 字面值，適合用來撰寫 bytes 用的正則模式
print(re.split(rb"[:,]", raw))  # [b'FOO', b'BAR', b'SPAM']

# 差異 1：索引回傳整數而非字元
a = "Hello"
b = b"Hello"
# 一般字串索引後得到的是單一字元
print(a[0])  # 'H'（字元）
# bytes 索引後得到的是該位元組的數值
print(b[0])  # 72（整數，即 ord('H')）

# 差異 2：不能直接用 format()，需先編碼
# 先用一般字串完成格式化，再用 encode() 轉成 bytes
formatted = "{:10s} {:10d}".format("ACME", 100).encode("ascii")
print(formatted)  # b'ACME            100'
