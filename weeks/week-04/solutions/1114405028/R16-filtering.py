# R16. 過濾：推導式 / generator / filter / compress（1.16）

mylist = [1, 4, -5, 10]
[n for n in mylist if n > 0]       # 列表推導式：一次建立新 list，保留正數
pos = (n for n in mylist if n > 0) # 生成器表達式：惰性求值，不立即產生全部元素，節省記憶體

values = ['1', '2', '-3', '-', 'N/A']

def is_int(val):
    try:
        int(val); return True   # 能轉成整數 → 回傳 True
    except ValueError:
        return False            # 無法轉換（如 '-' 或 'N/A'）→ 回傳 False

list(filter(is_int, values))       # filter：僅保留 is_int 回傳 True 的元素

from itertools import compress     # compress：依布林遮罩選取對應元素
addresses = ['a1', 'a2', 'a3']
counts = [0, 3, 10]
more5 = [n > 5 for n in counts]    # 產生布林遮罩：[False, False, True]
list(compress(addresses, more5))   # 只保留遮罩為 True 的地址 → ['a3']
