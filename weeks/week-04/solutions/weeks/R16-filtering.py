# R16. 過濾：推導式 / generator / filter / compress（1.16）

mylist = [1, 4, -5, 10]

# 列表推導式：最直覺、最常用的過濾方式
[n for n in mylist if n > 0]        # → [1, 4, 10]

# 生成器表達式：不建立完整列表，節省記憶體
pos = (n for n in mylist if n > 0)  # → generator，可逐筆取值


# -------------------------------
# filter()：搭配函式過濾
# -------------------------------

values = ['1', '2', '-3', '-', 'N/A']

def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

# filter() 會保留 is_int(val) 為 True 的元素
list(filter(is_int, values))
# → ['1', '2', '-3']


# -------------------------------
# compress()：依布林遮罩過濾
# -------------------------------

from itertools import compress

addresses = ['a1', 'a2', 'a3']
counts = [0, 3, 10]

# 建立布林遮罩：大於 5 的為 True
more5 = [n > 5 for n in counts]     # → [False, False, True]

# compress() 會依照 more5 的 True/False 過濾 addresses
list(compress(addresses, more5))
# → ['a3']