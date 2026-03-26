
# R04. 位元組字串操作（2.20）
#
# 本檔案示範 Python 中 bytes（位元組序列）與一般字串 str 的差異。
# 可以先記住一句話：
# - str 是「文字」（有編碼語意）
# - bytes 是「原始位元組資料」（常見於檔案、網路封包、二進位資料）
#
# bytes / bytearray 支援大部分「看起來像字串」的方法，
# 例如 startswith、split、replace 等；但在索引與格式化上有重要差異。

import re

# 建立一個 bytes 物件：前綴 b"..." 代表位元組字串常值
data = b"Hello World"

# 切片：行為和字串類似，會回傳 bytes
print(data[0:5])  # b'Hello'

# startswith 也可用，但參數必須是 bytes（不能直接放 str）
print(data.startswith(b"Hello"))  # True

# split：回傳的是 bytes 清單（list[bytes]）
print(data.split())  # [b'Hello', b'World']

# replace：bytes 取代 bytes，回傳新的 bytes
print(data.replace(b"Hello", b"Hello Cruel"))  # b'Hello Cruel World'

# 正則表達式也必須使用 bytes 模式
# 注意：當目標資料是 bytes，pattern 也要寫成 bytes（rb"..."）
# 否則會出現型別不相容（str 與 bytes 混用）的錯誤
raw = b"FOO:BAR,SPAM"
print(re.split(rb"[:,]", raw))  # [b'FOO', b'BAR', b'SPAM']

# 差異 1：索引回傳整數而非字元
# str 以「字元」為單位，bytes 以「0~255 的整數」為單位
# 因此 b"Hello"[0] 會得到 72（ASCII 中 'H' 的數值）
a = "Hello"
b = b"Hello"
print(a[0])  # 'H'（字元）
print(b[0])  # 72（整數，即 ord('H')）

# 差異 2：不能直接用 format()，需先編碼
# format() 產生的是 str；若最終要 bytes，必須再用 encode() 轉換
# 這裡示範用 ASCII 編碼將格式化後文字轉成 bytes
formatted = "{:10s} {:10d}".format("ACME", 100).encode("ascii")
print(formatted)  # b'ACME            100'
