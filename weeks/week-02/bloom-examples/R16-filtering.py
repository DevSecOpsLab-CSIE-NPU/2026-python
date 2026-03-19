"""
R16: 過濾資料

示範串列推導式、generator、filter 與 compress。
"""

from itertools import compress


mylist = [1, 4, -5, 10]

# 直接產生一個新的串列。
[n for n in mylist if n > 0]

# generator 不會立刻把結果全部算出來。
pos = (n for n in mylist if n > 0)

values = ["1", "2", "-3", "-", "N/A"]


def is_int(val):
    """判斷字串能不能轉成整數。"""
    try:
        int(val)
        return True
    except ValueError:
        return False


list(filter(is_int, values))

addresses = ["a1", "a2", "a3"]
counts = [0, 3, 10]

# compress 會依照布林遮罩保留元素。
more5 = [n > 5 for n in counts]
list(compress(addresses, more5))
