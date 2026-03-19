# R16. 過濾：推導式 / generator / filter / compress（1.16）
#
# 觀念重點：
# - 串列推導式：立刻產生 list。
# - 生成器表達式：延遲計算，較省記憶體。
# - filter：用函式決定要保留哪些元素。
# - compress：用布林選擇器（selector）進行過濾。

mylist = [1, 4, -5, 10]

# 只保留正數，直接得到新的 list。
[n for n in mylist if n > 0]

# 同樣條件，但回傳 generator，需要迭代才會取值。
pos = (n for n in mylist if n > 0)

values = ['1', '2', '-3', '-', 'N/A']


def is_int(val):
    # 可轉成 int 回傳 True，否則回傳 False。
    try:
        int(val)
        return True
    except ValueError:
        return False


# filter 只保留 is_int(val) 為 True 的字串。
list(filter(is_int, values))

from itertools import compress

addresses = ['a1', 'a2', 'a3']
counts = [0, 3, 10]

# 產生布林遮罩：>5 為 True，其他為 False。
more5 = [n > 5 for n in counts]

# 依 more5 的 True/False 對應保留 addresses。
list(compress(addresses, more5))
