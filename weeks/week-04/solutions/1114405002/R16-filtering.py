# R16 條件過濾與資料挑選
# 主題：list comprehension、generator expression、filter、compress

mylist = [1, 4, -5, 10]

# 1) 立即產生清單。
[n for n in mylist if n > 0]

# 2) 以 generator 延遲計算，較省記憶體。
pos = (n for n in mylist if n > 0)

values = ["1", "2", "-3", "-", "N/A"]


def is_int(val):
    # 可轉成整數回傳 True，不可轉則 False。
    try:
        int(val)
        return True
    except ValueError:
        return False


list(filter(is_int, values))

from itertools import compress

addresses = ["a1", "a2", "a3"]
counts = [0, 3, 10]

# 遮罩清單：True 才保留對應項目。
more5 = [n > 5 for n in counts]
list(compress(addresses, more5))
