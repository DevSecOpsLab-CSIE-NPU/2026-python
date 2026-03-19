# R16. 過濾：推導式 / generator / filter / compress（1.16）

mylist = [1, 4, -5, 10]

# 串列推導式：直接產生所有大於 0 的元素
[n for n in mylist if n > 0]

# 生成器表達式：延後產生資料，適合逐步處理
pos = (n for n in mylist if n > 0)

values = ['1', '2', '-3', '-', 'N/A']

# 檢查字串是否可以轉成整數
def is_int(val):
    try:
        int(val); return True
    except ValueError:
        return False

# filter 會保留函式回傳 True 的元素
list(filter(is_int, values))

from itertools import compress

# 依照布林遮罩挑出對應位置的元素
addresses = ['a1', 'a2', 'a3']
counts = [0, 3, 10]
more5 = [n > 5 for n in counts]
list(compress(addresses, more5))
