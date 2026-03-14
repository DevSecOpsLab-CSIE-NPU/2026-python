# R4. heapq 取 Top-N（1.4）
#
# heapq 是 Python 內建的「最小堆（min-heap）」工具：
# - 能快速取得最小值。
# - 也提供 nlargest / nsmallest 方便抓前 N 大或前 N 小。

import heapq

# 一組整數資料
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# 取前 3 大（由大到小回傳 list）
# 預期結果類似：[42, 37, 23]
# 注意：這裡沒有用變數接住結果，所以計算後不會保留在程式中。
heapq.nlargest(3, nums)

# 取前 3 小（由小到大回傳 list）
# 預期結果類似：[-4, 1, 2]
heapq.nsmallest(3, nums)


# 股票組合資料：每筆是 dict
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
]

# 用 key 指定比較欄位：依 price 比大小
# nsmallest(1, ...) 代表找「價格最低」的 1 筆
# lambda s: s['price'] 的意思是「每筆資料用 price 當排序依據」
heapq.nsmallest(1, portfolio, key=lambda s: s['price'])


# 把 nums 複製成另一個 list，避免直接改到原資料
heap = list(nums)

# 就地轉成最小堆結構（in-place）
# 轉完後 heap 內容看起來不一定是完整排序，但會滿足堆性質：
# - 父節點 <= 子節點
# - 因此最小值會在 heap[0]
heapq.heapify(heap)

# 彈出並回傳最小值（min-heap 的特性）
# 這行會拿到 -4，並且 heap 會重新調整成合法的最小堆
heapq.heappop(heap)


# 讀懂這份程式的步驟：
# 1. 先區分「Top-N 工具函式」與「真正建立堆」是兩件事。
# 2. nlargest/nsmallest：給資料、給 N，直接回傳結果清單。
# 3. 若資料是複合型別（dict/物件），用 key 指定比較準則。
# 4. heapify + heappop 是操作最小堆的基本流程：
#    先建堆，再重複彈出最小值。
