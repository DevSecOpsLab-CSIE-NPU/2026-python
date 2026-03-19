# R16. 過濾資料：推導式 / generator / filter / compress（1.16）
# 說明：展示多種從列表或序列中篩選資料的方法。

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# 1. 列表推導式 (List Comprehension)：最直觀，會產生一個新的 list
pos_list = [n for n in mylist if n > 0] # [1, 4, 10, 2, 3]

# 2. 生成器表達式 (Generator Expression)：延遲計算，節省記憶體
pos_gen = (n for n in mylist if n > 0)

# 3. 使用 filter()：處理較複雜的篩選邏輯
values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
    """檢查字串是否可以轉為整數"""
    try:
        int(val)
        return True
    except ValueError:
        return False

# filter 會回傳一個疊代器，需要用 list() 轉換
ivals = list(filter(is_int, values)) # ['1', '2', '-3', '4', '5']

# 4. 使用 itertools.compress：利用布林序列來過濾
from itertools import compress
addresses = ['Addr1', 'Addr2', 'Addr3', 'Addr4']
counts = [0, 3, 10, 4]
# 篩選次數大於 5 的地址
more5 = [n > 5 for n in counts] # [False, False, True, False]
result = list(compress(addresses, more5)) # ['Addr3']