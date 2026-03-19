# R16. 過濾：推導式 / generator / filter / compress（1.16）
"""
本範例介紹 Python 中常見的過濾技巧，包含：
- 列表推導式（list comprehension）中的條件過濾
- 生成器表達式（generator expression）中的條件過濾
- filter() 函式搭配回呼函式進行篩選
- itertools.compress 依據布林選擇對應元素

過濾的核心概念是「從一個可迭代物件中挑出符合條件的元素」，
常用於清洗資料、只保留有效值、或透過條件判斷建立子集。
"""

# 範例 1：列表推導式過濾（返回新列表）
# mylist 中包含正數和負數，我們只保留正數
mylist = [1, 4, -5, 10]

# 列表推導式語法： [expression for item in iterable if condition]
# 這裡 condition 是 n > 0，表示只保留大於 0 的元素
[n for n in mylist if n > 0]

# 範例 2：生成器表達式過濾（返回生成器，不會立即建立整個列表）
# 生成器表達式適合用在需要延遲計算或在大型資料上節省記憶體的情境
pos = (n for n in mylist if n > 0)

# 範例 3：使用 filter() 搭配回呼函式過濾
# filter(function, iterable) 會將 iterable 中的每個元素傳到 function
# 只有 function 回傳 True 的元素會被保留
values = ['1', '2', '-3', '-', 'N/A']

# 判斷字串是否可以轉成整數
def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        # 不能轉成 int 的字串（像 '-'、'N/A'）會導致例外
        return False

# 透過 filter 將 values 中可轉成整數的字串過濾出來
list(filter(is_int, values))

# 範例 4：使用 itertools.compress 依布林序列過濾對應元素
# compress(data, selectors) 同時遍歷 data 與 selectors
# 只有 selectors 中對應為 True 的位置才會保留 data 元素
from itertools import compress

addresses = ['a1', 'a2', 'a3']
counts = [0, 3, 10]

# 先建立一個布林列表，表示 counts 中哪些值大於 5
more5 = [n > 5 for n in counts]

# 只保留 addresses 中對應 more5 為 True 的元素（即 index=2 的 'a3'）
list(compress(addresses, more5))
