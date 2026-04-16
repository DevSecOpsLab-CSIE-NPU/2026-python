"""R4. heapq 取 Top-N（1.4）

heapq 提供了堆積（heap）相關操作，常用在：
1. 找出最大 N 個值（Top-N）
2. 找出最小 N 個值
3. 處理需要快速取出最大 / 最小元素的情境
"""

import heapq

# 一般數字列表，方便示範 nlargest / nsmallest
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# 取出最大的 3 個值（回傳新列表，且由大到小排序）
heapq.nlargest(3, nums)
# 取出最小的 3 個值（回傳新列表，且由小到大排序）
heapq.nsmallest(3, nums)

# 也可以對「物件 / 字典列表」做 Top-N，比較時用 key 指定欄位
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
]
# 依照 price 欄位找出最小的一筆資料
# lambda s: s['price'] 的意思是：用每個字典的 price 值作為比較依據
heapq.nsmallest(1, portfolio, key=lambda s: s['price'])

# heapify() 會把一般列表轉成「最小堆」結構
# 最小堆的特性：堆頂永遠是最小元素
heap = list(nums)
heapq.heapify(heap)
# heappop() 會把堆頂（最小值）取出並移除
heapq.heappop(heap)
