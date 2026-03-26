# R04. 位元組字串操作（2.20）
#
# 這份範例要說明：
# 1) bytes / bytearray 與 str 一樣，支援很多「看起來像字串」的方法。
# 2) 但 bytes 的本質是「一串 0~255 的整數」，不是 Unicode 字元序列，
#    因此在索引結果、格式化、正則表達式使用方式上會有差異。
#
# 小提醒：
# - str 用來表示文字（Unicode）
# - bytes 用來表示原始二進位資料（例如網路封包、檔案內容）

import re

# b"..." 代表 bytes 常值。
# 這裡 data 內容是 ASCII 可見字元，所以印出時會看到類似文字的形式。
data = b"Hello World"

# 切片（slice）結果仍然是 bytes。
print(data[0:5])  # b'Hello'

# startswith() 參數也要用 bytes，不能混用 str。
print(data.startswith(b"Hello"))  # True

# split() 對 bytes 一樣可用，回傳 list[bytes]。
print(data.split())  # [b'Hello', b'World']

# replace() 會回傳新的 bytes，不會就地修改原物件。
print(data.replace(b"Hello", b"Hello Cruel"))  # b'Hello Cruel World'

# 正則表達式也必須使用 bytes 模式：
# - 被處理資料是 bytes -> pattern 也必須是 bytes（例如 rb"..."）
# - 若 pattern 是 str 會型別不相容
raw = b"FOO:BAR,SPAM"
# rb"[:,]"：原始 bytes 字串（raw bytes literal），表示以 ':' 或 ',' 當分隔符號
print(re.split(rb"[:,]", raw))  # [b'FOO', b'BAR', b'SPAM']

# 差異 1：索引回傳整數而非字元
a = "Hello"
b = b"Hello"
# str 索引回傳的是「單一字元 str」
print(a[0])  # 'H'（字元）
# bytes 索引回傳的是「該位元組的整數值」
# 72 剛好是 ASCII 中 'H' 的編碼值
print(b[0])  # 72（整數，即 ord('H')）

# 差異 2：bytes 不能直接做文字格式化（如 f-string 或 str.format 的 bytes 版本）
# 常見做法是：
# 1) 先用 str 完成格式化
# 2) 再用 encode() 轉成 bytes（這裡使用 ascii）
formatted = "{:10s} {:10d}".format("ACME", 100).encode("ascii")
print(formatted)  # b'ACME            100'
