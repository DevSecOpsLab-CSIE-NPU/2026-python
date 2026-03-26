# R04. 位元組字串操作（2.20）
# 這份範例示範 Python 中 bytes / bytearray 的常見操作。
# 你可以把 bytes 想成「原始位元資料」，常用在：
# 1) 檔案二進位讀寫（例如圖片、壓縮檔）
# 2) 網路傳輸（socket、HTTP 原始封包）
# 3) 文字與編碼轉換前後的資料表示
#
# 注意：bytes 雖然提供不少看起來像字串的方法，
# 但它和 str（文字字串）的型別語意仍不同，
# 在索引、格式化、正則表達式等情境都要特別留意。

import re

# 建立一個 bytes 物件：前面加 b 表示「位元組字面值」。
data = b"Hello World"

# 切片操作與 str 類似，但結果仍是 bytes。
print(data[0:5])  # b'Hello'

# 判斷開頭是否符合指定 bytes 片段。
# 比對型別必須一致：bytes 要和 bytes 比。
print(data.startswith(b"Hello"))  # True

# split() 在 bytes 上也可用，回傳 list[bytes]。
# 預設以空白字元切割。
print(data.split())  # [b'Hello', b'World']

# replace() 也可直接替換 bytes 片段。
# 常用在處理協定資料或二進位內容中的固定標記。
print(data.replace(b"Hello", b"Hello Cruel"))  # b'Hello Cruel World'

# 正則表達式搭配 bytes 時，pattern 也必須是 bytes。
# 因此我們使用 rb"..."（raw bytes 字串）來撰寫模式。
# 這裡用 [:,] 表示「冒號或逗號」都拿來切割。
raw = b"FOO:BAR,SPAM"
print(re.split(rb"[:,]", raw))  # [b'FOO', b'BAR', b'SPAM']

# 差異 1：索引回傳整數而非字元
a = "Hello"
b = b"Hello"

# str 索引回傳的是「一個字元」（型別 str）。
print(a[0])  # 'H'（字元）

# bytes 索引回傳的是「該位元組的數值」（0~255 的 int）。
# 72 就是字母 'H' 的 ASCII 碼。
print(b[0])  # 72（整數，即 ord('H')）

# 差異 2：bytes 不能直接套用 str.format() 的文字格式化流程。
# 正確做法通常是：
# 1) 先用 str 完成格式化
# 2) 再依需求用指定編碼轉成 bytes（這裡使用 ASCII）
formatted = "{:10s} {:10d}".format("ACME", 100).encode("ascii")
print(formatted)  # b'ACME            100'
