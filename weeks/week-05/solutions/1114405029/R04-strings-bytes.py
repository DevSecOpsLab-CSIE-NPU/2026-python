# R04. 位元組字串操作（2.20）
#
# 這份範例要說明：
# 1. bytes 與 str 很像，都能做切片、查找、分割、取代。
# 2. 但 bytes 代表的是「原始位元組資料」，不是文字本身。
# 3. 因此在某些操作上，行為會和 str 不同，尤其是索引結果與格式化方式。
#
# 常見使用情境：
# - 讀寫檔案的二進位內容
# - 網路封包
# - 編碼/解碼前的資料處理

import re

# data 是 bytes 字面值，前面的 b 表示這不是一般字串，而是位元組序列。
data = b"Hello World"

# bytes 一樣可以切片；切片結果仍然是 bytes。
print(data[0:5])  # b'Hello'

# startswith() 也能用，但比對值必須同樣是 bytes，不能混用一般 str。
print(data.startswith(b"Hello"))  # True

# split() 會依空白切開，回傳的清單元素也都是 bytes。
print(data.split())  # [b'Hello', b'World']

# replace() 能替換其中一段位元組內容，回傳新的 bytes 物件。
print(data.replace(b"Hello", b"Hello Cruel"))  # b'Hello Cruel World'

# 正則表達式如果要處理 bytes，模式本身也必須寫成 bytes 形式。
# 也就是說，要用 rb"..." 而不是一般的 "..."。
raw = b"FOO:BAR,SPAM"
print(re.split(rb"[:,]", raw))  # [b'FOO', b'BAR', b'SPAM']

# 差異 1：索引回傳值不同。
# str 的單一索引會得到「字元」；bytes 的單一索引會得到「0~255 的整數」。
# 這是因為 bytes 的每個元素本質上就是一個位元組值。
a = "Hello"
b = b"Hello"
print(a[0])  # 'H'（字元）
print(b[0])  # 72（整數，即 ord('H')）

# 差異 2：bytes 沒有像 str 那樣完整的 format() 格式化介面。
# 一般做法是：先用 str 完成格式化，再依需求編碼成 bytes。
# 這裡選用 ASCII，是因為輸出內容只包含英數字與空白。
formatted = "{:10s} {:10d}".format("ACME", 100).encode("ascii")
print(formatted)  # b'ACME            100'
