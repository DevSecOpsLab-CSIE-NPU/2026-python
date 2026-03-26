# R04. 位元組字串操作（2.20）
# 主題：bytes / bytearray 的常見操作與和 str 的關鍵差異

import re

# ------------------------------------------------------------
# 一、bytes 的基本操作
# ------------------------------------------------------------
# bytes 是不可變的「位元組序列」，常見於網路封包、檔案二進位內容。
# b"..." 代表 bytes 常值。
data = b"Hello World"

# 切片：和一般字串相同，回傳 bytes
print(data[0:5])  # b'Hello'

# startswith：前綴判斷也要用 bytes 參數
print(data.startswith(b"Hello"))  # True

# split：依空白切割，回傳 bytes 清單
print(data.split())  # [b'Hello', b'World']

# replace：替換子序列，一樣使用 bytes
print(data.replace(b"Hello", b"Hello Cruel"))  # b'Hello Cruel World'

# ------------------------------------------------------------
# 二、bytes + 正則表達式
# ------------------------------------------------------------
# 使用 re 時，pattern 與資料必須「同型別」：
# bytes 資料就要搭配 bytes pattern（寫法常見為 rb"..."）。
raw = b"FOO:BAR,SPAM"
print(re.split(rb"[:,]", raw))  # [b'FOO', b'BAR', b'SPAM']

# ------------------------------------------------------------
# 三、str 與 bytes 差異
# ------------------------------------------------------------
a = "Hello"     # Unicode 字串
b = b"Hello"    # 位元組字串

# 差異 1：索引結果不同
# str 索引回傳「字元」；bytes 索引回傳「整數（0~255）」。
print(a[0])  # 'H'
print(b[0])  # 72（ord('H')）

# 差異 2：格式化流程
# bytes 沒有像 str 一樣直接使用 format 的流程，
# 實務上通常先組好 str，再 encode 成 bytes。
formatted = "{:10s} {:10d}".format("ACME", 100).encode("ascii")
print(formatted)  # b'ACME            100'

# 小結：
# 1) bytes 專注在「原始位元組」
# 2) str 專注在「文字語意」
# 3) 二者之間靠 encode/decode 轉換
